---
title: Price of Anarchy of First-Price Auctions in Agentic Markets
url: https://arxiv.org/abs/2610.20587
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Shubhendu Trivedi
- Jacob Eisenstein
- Alekh Agarwal
- Ian Gemp
- Michael Kaisers
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.20587
pages: 40
chars: 124335
fetched_at: '2026-11-08T13:26:12+00:00'
kb_version: 1
---

# Price of Anarchy of First-Price Auctions in Agentic Markets

2026-10-15
Price of Anarchy of First-Price Auctions in
Agentic Markets
Shubhendu Trivedi1, Jacob Eisenstein1, Alekh Agarwal2, Ian Gemp1, Michael Kaisers1, Adam Fisch1
1Google DeepMind, 2Google Research
An agentic market is a decentralized serving-time market where AI agents bid to claim each user prompt.
An agent’s bid is based on its expected value for the prompt, which is the expectation of the reward for
its response minus its inference costs. First-price auctions (FPAs), in which the highest bidder pays its bid
and receives the prompt, are a natural way to allocate prompts in such a market, since they are simple
and transparent to run, and do not require central knowledge of private capabilities and costs. However,
FPAs are not truthful: participants may bid less than their true value in the hope of a larger profit,
and the prompt may then be allocated to someone other than the bidder who values it the most. This
welfare loss is quantified by theprice-of-anarchy(PoA). In this paper, we argue that agentic markets are
likely to possess features that reduce the price-of-anarchy. The first is acompetitive floor, which occurs
when multiple bidders usually value the prompt above some baseline share of the optimal welfare (e.g.,
because the best models are often distilled into cheaper alternatives, which perform similarly). We show
that competition among them then limits the welfare loss, which can be driven to zero as the floor rises.
The second feature isnear-independenceof values after conditioning on the prompt, which occurs when
most of the predictable variation in the expected value is determined by the difficulty of the prompt.
As the value distribution approaches conditional independence, we can derive an efficiency guarantee
that approaches a factor of1− 1/𝑒2 of the optimal welfare. Thus, both features give rise to welfare lower
bounds that are significantly better than the well-known general case of1− 1/𝑒. We validate these results
empirically using auctions with strategic bidders simulated on the EmbedLLM prompt routing dataset.
1. Introduction
Consider a user with a task that could be serviced by any one of many AI agents, where each AI agent
has a different expected cost and response quality. The user could choose among the agents directly,
but that requires knowledge about every option on the market. Alternatively, aggregators and routers
can make this choice on the user’s behalf—e.g., by establishing a central view of which agent is good
at which tasks, and directing users’ prompts accordingly (Aubakirova et al., 2025; Chen et al., 2024;
Ding et al., 2024; Ong et al., 2025). That view has to be measured and maintained, however, which
becomes harder as the candidate pool grows beyond well-known providers. A third, and emerging,
approach is the "agentic market," which is a serving-time market where possible responding agents bid
to claim each prompt, and are rewarded according to the quality of the response they provide (Chang
et al., 2020; Liu et al., 2026; Qi et al., 2026). Each responder is assumed to privately know (or
estimate) its expected quality and cost on the current prompt, which the market must elicit efficiently
and transparently, without assuming that responders are honest. Being decentralized, the market also
scales with the number of participants rather than with the platform’s ability to track them.
Themaindesignchoiceinsuchamarketishowtoallocatepromptsbasedontheagents’bids, andwhat
price to charge the agent who wins the auction. Many mechanisms exist, and recent work on agentic
markets has largely favored those that are dominant-strategy incentive compatible, such as second-
price and Vickrey-Clarke-Groves (VCG) variants, under which bidding one’s true value is optimal
regardless of what other bidders do (Cao et al., 2026; Chang et al., 2020; Liu et al., 2026).
In this paper, we analyze the viability of the first-price auction (FPA), which is an especially simple
Correspondence to{shubhendut, jeisenstein, alekhagarwal, imgemp, mkaisers, fisch}@google.com.
©2026 Google. All rights reserved
arXiv:2610.20587v1  [cs.GT]  14 Oct 2026

Price of Anarchy of First-Price Auctions in Agentic Markets
mechanism. Here, each responder bids for the right to service the current prompt. The highest bidder
wins, pays its bid to the platform, submits its response, and collects a reward based on quality (Chang
et al., 2020; Qi et al., 2026). FPAs have several advantages. The payment rule is transparent,
since the winner pays its own bid, with no need to trust the platform to truthfully report a second
price (Rothkopf et al., 1990). Bidders can be strategic, but do not need to be: a nonnegative bid
below expected quality minus cost results in a nonnegative expected surplus when it wins, regardless
of what others bid. FPAs are also simple to implement, which partly explains why some of the largest
markets, such as display advertising auctions, use them (Cox, 2019; Paes Leme et al., 2020).
While FPAs are successful in practice, they are less appreciated in theory. Unlike VCG-style mecha-
nisms, first-price auctions are not truthful: strategic agents “shade” their bids below their true values to
increaseprofit, andifhigher-valuedagentsshadetooaggressively, theycanlosetolower-valuedagents,
which decreasessocial welfare(the total value generated by the allocation). The ratio of the welfare
at a strategic equilibrium to the best achievable welfare is called theprice of anarchy(Roughgarden
et al., 2017), and for FPAs it can be as low as1−1/𝑒≈63%(Syrgkanis and Tardos, 2013).
A potential1/𝑒≈ 37%loss in efficiency may seem severe, but it is a worst case bound over arbitrary
value distributions. We empirically show that in representative agentic markets simulated on the
large-scale EmbedLLM dataset (Zhuang et al., 2025), realized welfare losses are often much smaller.
To understand this gap between theory and practice, we derive new bounds that show that the worst
case improves substantially under structural conditions that are natural in agentic markets. The
primary condition is acompetitive floor, which occurs when several bidders usually value the query
above a certain baseline. Competition among these bidders then keeps the winning bid high and limits
how much welfare can be lost. Competitive floor conditions can arise when agents have comparable
substitutes, e.g., due to distillation or similar training data and capabilities (Aubakirova et al., 2025;
Cao et al., 2026). Our bounds depend on how many bidders are competitive, how high the floor
is, and how reliably it holds. As a secondary result, we show that the PoA bound can also improve
throughnear-independence, even when no such floor exists. When bidder values are independent,
Jin and Lu (2023a) show that the price of anarchy improves to1− 1/𝑒2≈ 86.5%. We prove that
this guarantee still holds approximately under small perturbations from independence in terms of
total-variation distance. This is practically relevant because shared query features (such as prompt
difficulty or type) account for much of the co-movement across models; the idea being that once this
information is conditioned out, the residual dependence may be much weaker.
These results show that when models (1) compete closely on capability or (2) share task difficulty
that can be conditioned out, the equilibrium allocation preserves substantially more welfare than
worst-casetheorypredicts. Muchofthemotivationformorecomplexmechanismsthenfallsaway—the
simple and transparent FPA can already capture most of the available welfare under conditions that
agentic markets tend to satisfy. A market platform also does not have to treat these conditions as
purely exogenous. In retail, for example, operators often stock “private labels” alongside third-party
sellers to discipline markups (Ding et al., 2025; Shopova, 2023). In the same spirit, we examine how
a platform can steer market conditions, either by introducing its own model to increase competition
(acting like a reserve price) or by filtering out low-performing responders before bidding begins.
Contributionsofthiswork.Insummary, thispaperprovidestheoreticalandempiricaltoolstoanalyze
first-price auctions under what practitioners may expect from typical agentic market structure:
1. Competitive floors (§3):We derive price-of-anarchy bounds that improve when several bidders
usually value the query above a certain baseline, a fixed fraction of the optimal welfare.
2. Near-independence (§4):We show the1− 1/𝑒2 bound for independent values (Jin and Lu, 2023a)
still holds approximately when values are nearly independent after conditioning on the query.
3. Platform design (§5):We show that platforms can create these conditions, by filtering out weak
2

Price of Anarchy of First-Price Auctions in Agentic Markets
responders before bidding or by entering in-house models that act as reserve prices.
4. Empirical analysis (§6):On EmbedLLM (Zhuang et al., 2025), we find that competitive floors
and conditional independence emerge and yield high efficiency, even in adversarial equilibria.
2. Preliminaries
We begin by briefly reviewing the first-price auction (FPA). Consider a single user prompt that is to be
serviced by one of𝑛bidders (also called “providers” or “agents”) for some user-provided reward.1 Each
bidder 𝑖 has a value𝑣𝑖 for the request, defined as its expected reward minus its cost of service:
𝑣𝑖 =𝔼[reward(response 𝑖)−cost 𝑖|query].(1)
In a standard auction, the item for sale is the only source of randomness: each bidder knows its
own value, which is random only from the perspective of others. But in agentic markets, the reward
and cost of a response is typically not known until it is produced. Simply letting bidder𝑖 take the
expectation of the response reward minus cost reduces the setting to the standard one. If bidder𝑖
wins the request and pays a price𝑝𝑖, its expected payoff (orsurplus) is then simply𝑣𝑖−𝑝 𝑖.
In a sealed-bid FPA, every bidder𝑖 submits a bid𝑏𝑖. The bidder with the highest bid wins, and pays its
own bid. We write𝑖∗(b) for the index of the winning bidder whereb=(𝑏 1,...,𝑏 𝑛), with ties broken by
an announced measurable bid-only rule, possibly randomized. A rational bidder, however, may prefer
not to bid its true value, as doing so guarantees zero expected surplus. Bidders may therefore strategi-
callyshadetheir bids below their values to gain positive surplus. We model this strategic interaction as
a Bayesian game of incomplete information (Roughgarden et al., 2017). Specifically, we model bidder
valuesv =(𝑣 1,...,𝑣 𝑛) as draws from a joint value prior𝜇, and a strategy for bidder𝑖 is a possibly
randomized function𝑠𝑖 mapping a value𝑣𝑖 to a bid𝑏𝑖 =𝑠 𝑖(𝑣𝑖). A strategy profiles=(𝑠 1,...,𝑠 𝑛) is a
Bayes-Nash equilibrium(BNE) if, for every bidder𝑖 and almost every value𝑣𝑖, the bid𝑠𝑖(𝑣𝑖) maximizes
bidder𝑖’s expected surplus given the strategies of the other bidders (s−𝑖) and the value prior (𝜇).
Onatechnicallevel, weassumethroughoutthatbiddersneverbidmorethantheirvalueatequilibrium,
i.e.,0 ≤𝑠 𝑖(𝑣𝑖)≤𝑣 𝑖 almost surely for each𝑖∈[𝑛] and almost every𝑣𝑖≥ 0. This is standard in the litera-
ture, since overbidding risks negative surplus (Jin and Lu, 2023a; Syrgkanis and Tardos, 2013).
Throughout the rest of this paper, expectations and probabilities are taken over the joint randomness
in values, private bidding randomization, and tie-breaking. We write𝔼𝜇 and ℙ𝜇 only when more than
one value distribution is in play, as in the PoA (2); when the prior is fixed, we write𝔼andℙ.
2.1. Social welfare and the price of anarchy
It is natural to measure an auction’s performance by the totalsocial welfare(which we will just refer to
as thewelfare) it generates, which is the sum of the bidder utilities, plus the revenue of the auctioneer.2
In the simple single-item setting we consider for agentic markets, the welfare reduces to the value of
the winning bidder,𝑊(b,v):=𝑣 𝑖∗(b). Theoptimal welfareis thenOPT(v):=max 𝑖𝑣𝑖.3
Since FPAs allocate to the highestbidderrather than the highest-value provider, shading can cause
the auction to select a suboptimal provider. Theprice of anarchy(PoA) quantifies the worst-case
welfare loss due to strategic behavior. Formally, the PoA is the infimum, over all settings (number
1Where do these rewards come from? The theory that follows is agnostic to this question, but a few concrete
instantiations can be helpful to keep in mind. The simplest is a binary reward such as a thumbs up/down reported back
by the platform or user (assumed, honestly). More generally, the platform could use any agreed-upon function𝜙(𝑞,𝑦)
that takes a prompt𝑞 and response𝑦 and outputs a reward𝑟 funded by the user (e.g., a reward in escrow is released
contingent upon the agent’s response𝑦passing a collection of unit tests or clearing a third-party autorater / verifier).
2We model a user’s value as being equal to the price they pay for the response, so that their utility is always0.
3We do not consider externalities, such as𝑖∗ getting additional private utility by placing an advertisement.
3

Price of Anarchy of First-Price Auctions in Agentic Markets
of bidders, joint value distribution𝜇) and BNE, of the ratio of the expected welfare to the optimal
welfare, i.e.,
PoA:=inf
𝜇
inf
s∈BNE(𝜇)
𝔼𝜇[𝑊(s(V),V)]
𝔼𝜇[OPT(V)] .(2)
The infimum is restricted to priors with0<𝔼 𝜇[OPT( V)]<∞ and a nonempty set of equilibria (that,
recall, we assume are non-overbidding). In symmetric settings (where all bidders draw values from
the same distribution), the BNE of a first-price auction is unique and fully efficient (Chawla and
Hartline, 2013), and the PoA is1. In asymmetric settings, which arise when bidders have different
expected values, as expected in agentic markets, equilibria are generally inefficient.
A foundational result establishes that every BNE of a first-price single-item auction achieves≥
(1− 1/𝑒) ≈63.2%of optimal welfare (Roughgarden et al., 2017; Syrgkanis and Tardos, 2013).
Under the stronger assumption that bidders’ values are drawn independently (but not identically), Jin
and Lu (2023a) obtain the tight bound of(1− 1/𝑒2)≈ 86.5%. These bounds are important, though
they do paint a pessimistic picture of first-price auctions. A potential welfare loss of37%(or even
13.5%) is large enough to make a platform hesitant to deploy first-price orchestration at all. These
bounds, however, are worst-case lower bounds over all possible value distributions. As we will see,
agentic markets often possess structural features that push their realized welfare higher.
3. First-price auctions with competitive floors
The price of anarchy fundamentally depends on what is at stake. If all bidders value an item identically,
then any allocation achieves full efficiency. More generally, no matter which bidder wins, welfare is at
least the lowest bidder value, which therefore acts as a "floor" on the welfare. Write𝑉(1)≥···≥𝑉 (𝑛)
for the bidder values in decreasing order. Then for any given value prior𝜇, we must have
inf
s∈BNE(𝜇)
𝔼[𝑊(s(V),V)]
𝔼[OPT(V)] ≥ 𝔼[𝑉(𝑛)] 𝔼[𝑉(1)],(3)
which does not require strategic analysis. Note that Equation (3), as well as the other bounds we will
present here, are specific to the prior𝜇. Section B.1 then shows how these bounds are uniform over
any family of priors that satisfy the same minimal conditions. Looking at Equation (3), when𝔼[𝑉(𝑛)]
is close to𝔼[𝑉(1)] (e.g., when all models perform similarly on user queries), the bound is close to1.
A single weak bidder, however, might pull it far below1. The rest of this section analyzes competition
in the auction to obtain a bound that depends only on the strongest few bidders.
Intuitively, markets only require competition at the top (that is, just between the highest-valued bid-
ders) to be efficient. In other words, it should be enough for more than one, but not all, bidders to usu-
ally value the query highly. We formalize this via a notion of a "competitive floor" for the market.
Definition 1(Competitive floor).Fix a fraction𝛼∈[ 0, 1] of the optimal welfare, a number of bidders
𝑚∈{ 2,...,𝑛} , and a failure rate𝜖∈[ 0, 1]. A market has an(𝛼,𝑚,𝜖) -competitive floorif at least𝑚
biddersvaluethequeryat 𝛼𝔼[𝑉(1)] orhigherwithprobabilityatleast1 −𝜖, i.e.,ℙ 𝑉(𝑚)≥𝛼𝔼[𝑉(1)]≥ 1−𝜖.
3.1. Deterministic competitive floors
As a warmup, suppose two biddersalwaysclear𝛼𝔼[𝑉(1)]. The PoA bound then rises with𝛼.
Proposition 2.Suppose0<𝔼[𝑉 (1)]<∞and𝑉 (2)≥𝛼𝔼[𝑉(1)]almost surely for𝛼∈[0,1]. Then
inf
s∈BNE(𝜇)
𝔼[𝑊(s(V),V)]
𝔼[OPT(V)] ≥

1− 1 𝑒  + 𝛼 𝑒.(4)
4

Price of Anarchy of First-Price Auctions in Agentic Markets
𝑚=2 4 8 16 32 64
0.6
0.7
0.8
0.9
1
PoA bound
𝛼=0.50
𝑚=2 4 8 16 32 64
𝛼=0.70
𝑚=2 4 8 16 32 64
𝛼=0.90
𝜖=0
𝜖=0.01
𝜖=0.05
𝜖=0.10
𝜖=0.15
1−1/𝑒
Figure 1| Price-of-anarchy bounds under competitive floors, for various settings of(𝛼,𝑚,𝜖) . Each
entry represents the bound for any distribution withℙ(𝑉(𝑚) < 𝛼𝔼[𝑉(1)])≤𝜖 . At𝜖= 0, we recover the
deterministic floor bound from Equation (4); higher𝜖 start to degrade the efficiency. Larger numbers
of credible competitors (𝑚≥4) stabilize the market, and preserve efficiency even under high𝜖.
All proofs are in the appendix. At a high level, we first prove that deterministic competition from the
runner-up ensures that the equilibrium winning bid is at least𝛼𝔼[𝑉(1)], which also guarantees that the
welfareisatleast 𝛼𝔼[𝑉(1)]. Anyequilibriumthenfurtherrecoversatleasta (1−1/𝑒)-fractionoftheopti-
mal welfare remainingabovethe floor, i.e.,(1−𝛼)𝔼[𝑉(1)]. As an example, suppose a rival always values
the query at least half the expected top value (𝛼= 0.50). The bound rises from≈ 63%to≈ 82%.
3.2. Probabilistic competitive floors
Proposition 2 corresponds to a competitive floor with𝑚= 2and 𝜖= 0. That is, it requires at least two
bidders to clear the floor oneveryquery. This is not realistic: on unusual queries for instance, only
one model may be able to do well, even if several models usually compete closely on most queries.
When bidders know that a second credible competitor is sometimes lacking, they can shade more,
and the winning bid may fall below the floor. Combining a bound on how far it can fall (Section E.2)
with a similar argument to that of Proposition 2 gives the following bound.
Theorem 3.Suppose0<𝔼[𝑉 (1)]<∞and the market has an(𝛼,𝑚,𝜖)-competitive floor. Then
inf
s∈BNE(𝜇)
𝔼[𝑊(s(V),V)]
𝔼[OPT(V)] ≥

1− 1 𝑒  +𝛼  1 𝑒−𝑆 𝑚(𝜖)  + ,(5)
where𝑆 𝑚(𝜖):=𝐼 𝜖(𝑚−1,2) 1/𝑚,𝐼 𝜖 is the regularized incomplete beta function, and[·]+ =max(0,·).
Remark 4.𝑆𝑚(𝜖) is a penalty that increases from0to1as𝜖goes from0to1, and decreases toward𝜖as𝑚
grows. It also satisfies the simple bound𝑆𝑚(𝜖)≤𝑚 1/𝑚𝜖1−1/𝑚. For example, it is at most √ 2𝜖 when 𝑚= 2.
ComparedtoProposition2,theboundinTheorem3subtractsapenalty 𝛼𝑆𝑚(𝜖) thatdepends,inasense,
on how reliably the competition holds. The penalty is zero when𝜖= 0, in which case Theorem 3 recov-
ers Proposition 2, and it shrinks when more bidders (𝑚) clear the floor (at the same rate,1−𝜖).
To further illustrate how the bound in Equation (5) behaves, in Figure 1 we plot its value while varying
𝑚,𝛼, andahypotheticalfailurerate 𝜖. Weseethatevenifthefailurerate 𝜖ishigh(e.g., ≈ 0.10), wecan
stillguaranteeastrongerPoAifthefloorholdsforseveralcompetitors. Forexample, suppose 𝑚models
achieve90%of the mean best value at least90%of the time. If only two models clear this threshold
(𝑚=2), the bound stays at≈63%. With𝑚=4it rises to≈74%, and with𝑚=16to≈84%.
For a given𝜇, Theorem 3 holds for all𝛼∈[ 0, 1] and𝑚∈{ 2,...,𝑛} , so we can take the supremum over
both.4 For each(𝛼,𝑚) , the smallest valid failure rate is𝜖∗ 𝛼,𝑚 =ℙ 𝜇(𝑉(𝑚) < 𝛼𝔼𝜇[𝑉(1)]), which gives
inf
s∈BNE(𝜇)
𝔼[𝑊(s(V),V)]
𝔼[OPT(V)] ≥

1− 1 𝑒  +sup 𝛼,𝑚 𝛼 h 1 𝑒−𝑆 𝑚(𝜖∗ 𝛼,𝑚) i + .(6)
4Likewise, since the non-strategic bound in Equation (3) holds for the same𝜇, the larger of the two bounds also holds.
5

Price of Anarchy of First-Price Auctions in Agentic Markets
Section B contains additional results on competitive floors. Section B.3 conditions Theorem 3 on public
information𝑋 about the query, such as the prompt text. The floor𝛼𝔼[𝑉(1)|𝑋=𝑥] then adapts to how
hard each query is, and the resulting bound is never weaker than the pooled one. Section B.2 also
explores a related setting in which positively dependent (e.g., affiliated) values always raise the bound
in Equation (3) compared to independent values with the same marginal bidder distributions.
4. First-price auctions with near-independent values
In the previous section we showed that competitive floors on the values limit welfare loss. A separate
questionishowthedependencestructureamongvalues(orlackthereof)affectsstrategicbehavior. More
specifically, underindependentprivatevalues(IPV;where 𝑉1⊥···⊥𝑉 𝑛),JinandLu(2023a)showthat
the PoA improves from1− 1/𝑒≈ 0.632to1 − 1/𝑒2≈ 0.865. In practice, bidder values are rarelystrictly
independent—yet they may be nearly independent. In agentic markets, values co-vary across queries
due to shared task difficulty and similar model costs, but we conjecture that much of this common
variationcanbeexplainedbyobservablequerymetadata. Ifso,oncequerymetadata 𝑋 isobserved(e.g.,
the prompt text, its topic, how response quality is measured, the model tiers of the other bidders, etc.),
agent values may be approximately independent, where𝜇(𝑣1,...,𝑣 𝑛|𝑋) ≈ ˛𝑛 𝑖=1𝜇𝑖(𝑣𝑖|𝑋).
Whether this holds in practice is an empirical question that we examine in Section C.1. But first we
must ask whether we can approach the1−1/𝑒2 guarantee withapproximateconditional independence.
We prove that we can. Specifically, for each realization of the public state𝑋=𝑥 , let𝜇𝑥 :=𝜇(·|𝑋=𝑥)
and𝜈𝑥 := ˛𝑛 𝑖=1𝜇𝑖(·|𝑋=𝑥) , andwrite𝜏(𝑥) :=∥𝜇 𝑥−𝜈𝑥∥TV forthetotalvariationdistancebetweenthe
conditional joint distribution and the product of its marginals. We use∥𝜇−𝜈∥ TV :=sup 𝐴|𝜇(𝐴)−𝜈(𝐴)| .
When the conditional total variation distance𝜏(𝑥)= 0, values are conditionally independent given
𝑋=𝑥. We then can show the following qualitative result.
Theorem 5.For every fixed 𝑛≥ 2, there is a nondecreasing function𝜂cont 𝑛 :[ 0, 1] → [0,∞) with
𝜂cont 𝑛 (0)= 0and 𝜂cont 𝑛 (𝑡)→ 0as 𝑡↓ 0such that the following holds. Suppose0≤𝑉 𝑖≤ 𝑣(𝑋)<∞ almost
surely. Then everys∈BNE(𝜇)satisfies, for almost every𝑥,
𝔼[𝑊(s(V),V)|𝑋=𝑥] ≥

1− 1 𝑒2

𝔼[𝑉(1)|𝑋=𝑥] − 𝑣(𝑥)𝜂 cont 𝑛 (𝜏(𝑥)).(7)
When 𝜏(𝑥)= 0, the error term vanishes and we recover the1− 1/𝑒2 bound exactly, even if values
are arbitrarily correlatedacrossqueries. Small departures from conditional independence incur an
additive penalty scaled by the conditional value bound𝑣(𝑥). Converting to a ratio bound requires that
𝑣(𝑥) is not too large relative to𝔼[𝑉(1)|𝑋=𝑥] ; integrating over𝑋 gives the unconditional guarantee.
The proof accounts for changes in both welfare expectations and bidding incentives when the joint law
is replaced by the product law. Appendix F gives the full argument, with additional refinements.
Note that competitive floors and near-independence are not mutually exclusive, despite perhaps
seeming so. For instance, suppose𝑉𝑖 =𝑎(𝑋)+𝜃𝑍 𝑖, where𝑎(𝑋)≥𝜃 and, conditional on𝑋, 𝑍𝑖 are
zero-mean, independent random variables in[−1, 1]. Then𝑉𝑖 are conditionally independent and lie in
an interval of width2𝜃. When𝜃is small relative to𝑎(𝑋) , they also share a high competitive floor.
5. On implications for agentic market platform design
The market structure supporting our bounds is partly under the platform’s control, leading to some
very simple design recommendations to protect market efficiency. In this section we explore what
happens if the platform restricts which models bid on a query, or if it honestly enters its own in-house
model (e.g., if it has privately developed one, or hosts an open-weight model) into the auction.
6

Price of Anarchy of First-Price Auctions in Agentic Markets
Pre-auction filtering.Many platforms already run a lightweight router that picks a subsetS(𝑋)⊆[𝑛]
of models based on the public query information𝑋 (Hu et al., 2024; Ong et al., 2025,inter alia). Let
𝑊S be the welfare at an equilibrium of the auction in which only models inS(𝑋) bid (note that the
randomness in𝑊S also depends onS(𝑋) ). The winner of this auction is always inS(𝑋) by definition,
so simply applying the naive bound of Equation (3) within it, and marginalizing over𝑋, gives
𝔼[min𝑖∈S(𝑋) 𝑉𝑖]
𝔼[𝑉(1)] ≤ 𝔼[𝑊S] 𝔼[𝑉(1)] ≤ 𝔼[max𝑖∈S(𝑋) 𝑉𝑖] 𝔼[𝑉(1)] .(8)
While this bound might be weak for a market with open participation (where a single poor model can
drag the welfare bound down, as discussed at the start of Section 3), a platform thatcontrolswho
competes can make it stronger by removing weak models, which raises the lower bound. Removing the
best model (i.e., if𝑉(1) ∉S(𝑋)) , however, also lowers the upper bound; thus filtering does incur some
risk. Still, that risk can be mitigated by being more conservative in filtering, and as long as the router
keeps the strongest models, the bounds of Section B.3 still apply to the filtered marketS(𝑋).
Platform participation.A platform can also enter its own in-house model into the auction. We study a
simple version of this, in which the platform publicly announces its model’s value𝑉0 for each query and
then bids exactly𝑉0. Since𝑉0 is then part of the public state𝑋, every model can condition on it, and
the platform’s model acts as a query-specific reserve price. This mirrors private-label strategies from
retail economics (see, e.g., Ding et al., 2025; Shopova, 2023). Similar to the deterministic competitive
floor in Section 3.1, the platform’s bid keeps the winning bid, and hence the welfare, at least𝑉0.
On top of this, any equilibrium recovers at least a(1− 1/𝑒)-fraction of the optimal welfare above𝑉0.
WriteV =(𝑉 0,𝑉 1,...,𝑉 𝑛) ands =(𝑠 0,𝑠 1,...,𝑠 𝑛) with 𝑠0(𝑉0)=𝑉 0, so that𝑉(1) =max 𝑖≥0𝑉𝑖 includes the
platform’s model. Then everys∈BNE(𝜇)satisfies (see Section E.3 for the derivation):
𝔼[𝑊(s(V),V)]
𝔼[𝑉(1)] ≥

1− 1 𝑒  + 1 𝑒 𝔼[𝑉0] 𝔼[𝑉(1)].(9)
Notice that if 𝔼[𝑉0] ≥𝛼𝔼[𝑉(1)], this bound is at least that of Proposition 2. The assumptions of
Proposition 2, however, require a rival𝑉(2)≥𝛼𝔼[𝑉(1)] almost surely (i.e., oneveryquery), whereas the
platform model’s value (which is effectively a rival) only needs to exceed𝛼𝔼[𝑉(1)] on average.
6. Experiments
We now test how well our bounds describe welfare in a realistic LLM market. We run one auction with
allmodelsonthefullEmbedLLMdataset(Zhuangetal.,2025),comparethecompetitive-floorboundto
realized welfare over many random sub-markets, and then also study hand-picked, illustrative cohorts
that fix optimal welfare while varying market structure. The appendix contains additional results that
analyze, empirically, how weakly dependent values are after conditioning on the query (Section C.1),
as well as results with platform-owned bidders and pre-auction filtering (Sections C.2 and C.3).
6.1. Setting
Dataset.We simulate auctions with strategic bidders on the EmbedLLM routing dataset (Zhuang et al.,
2025), which aggregates over30𝑘 prompts across math, code, question answering, and reasoning
benchmarks, along with the scored responses from112models of various sizes. To align with our
convention that a model’s value is its expected reward minus its cost, we set𝑣𝑖(𝑞)=max( 0, ˆ𝔼[acc𝑖|
𝑞]−𝑐 𝑖), whereˆ𝔼[acc𝑖|𝑞] estimates the probability that model𝑖answers query𝑞correctly, computed by
𝑘-nearest neighbors (𝑘= 16) over Gemini prompt embeddings (Shanbhogue et al., 2026), excluding𝑞.
FollowingJitkrittumetal.(2025), weset 𝑐𝑖 tobelinearinparametercount, at1pertrillionparameters,
so that, e.g., Qwen-1.5-7B-Chat has a cost of.00772and Qwen-1.5-32B-Chat has a cost of.0325. Two
modelswereexcludedbecausetheirparametercountcouldnotbedetermined, leaving110total.
7

Price of Anarchy of First-Price Auctions in Agentic Markets
Oracle Random Best single Best per cluster FPA FPA (adv)
Full dataset Empirical welfare0.768 0.416 0.600 0.686 0.762 0.758 Empirical PoA1.000 0.542 0.781 0.894 0.992 0.988
Worst cluster Empirical PoA1.000 0.083 0.060 0.640 0.960 0.930
Table 1| Realized welfare on the full EmbedLLM market under different allocation rules, raw and
as a fraction of the optimal welfare. As baselines,Randomallocates queries randomly, whileBest
singleandBest per clusteruse the model with the highest average value overall or within each cluster,
respectively; the latter is a router that sees only the prompt’s cluster, the same public state the bidders
condition on.FPAandFPA (adv)use a typical and an adversarially chosen (approximate) equilibrium
(§6.1). Worst-cluster welfare is averaged on each rule’s lowest-welfare prompt cluster (out of20).
Strategic bidding.Each model submits a sealed bid𝑏𝑖(𝑞)≤𝑣 𝑖(𝑞) for each query𝑞, and the highest bid-
der wins and pays its bid. We partition the prompts into20𝐾-means clusters using their embeddings,
and bidders condition their strategies on the cluster and their own value𝑣𝑖(𝑞). A bidder therefore
knows the approximate type of prompt it is bidding on and its own estimated value, but knows its
rivals’ values only through the prior distribution, conditioned on the cluster. Within each cluster we
solve for (approximate) Bayes–Nash equilibria by fictitious play using a discretized grid over both
values and possible bids (see Section D for details). Equilibria are not necessarily unique, and certain
equilibria might have substantially worse welfare than others. We therefore solve every market twice:
once for atypicalequilibrium, where at each iteration bidders update their strategy to the best (surplus
maximizing) response nearest its current bid until convergence, and once for an (also approximate)ad-
versarialequilibrium, where at each iteration each bidder takes the welfare-minimizingresponse that
still retains at most5%relative regret of its best possible individual surplus until convergence.
Metrics.Welfare within a market is pooled over all prompts and reported as a fraction of the first-best
oracle, OPT=𝔼[max 𝑖𝑣𝑖(𝑞)], which we call the “realized PoA” to distinguish it from the worst-case
boundsofSection3. Bya“market”wemeanasubsetofthe110modelsbiddingagainsteachother, and
most of our experiments draw many such subsets at random, with the sampling scheme stated in each
case. Every number we report is therefore computed over prompts and over sampled markets. Since
the bounds we are testing are worst-case statements, we report both the mean and the0.1-percentile
(p0.1) of realized PoA across markets,5 and we compare both against the competitive-floor bound
of Theorem 3 evaluated on the same market (where like the equilibrium strategies, the bound is com-
putedusingtheempiricaldistributionofthebiddervalues). Wealsotrackhowmuchthewinnershades,
1−𝔼[𝐵 winner/𝑉winner]. Note, however, that shading (i.e., low winning bids) on its own does not cost wel-
fare, since queries are misallocated only when bidders shade by (problematically) different amounts.
Finally, as bidders condition on the cluster (see "Strategic bidding" above), each of the20clusters is
effectively its own auction, and the pooled welfare averages over them. As a robustness measure, we
also report welfare on theworst cluster, i.e., the cluster where a given allocation rule does worst.
6.2. Results
ResultsonthefullEmbedLLMmarket.Table1reportsasingleauctionrunonthefulldatasetwithall
110modelsbiddingagainsteachother. Theauctionatequilibriumisnearlyperfectlyefficient, reaching
99.2%of oracle welfare at the typical equilibrium and98.8%at the adversarial one. Both exceed
the baseline of routing each cluster to its own best model (89.4%), and are well above the baseline
of committing to one model everywhere (78.1%). The gap widens on each rule’s worst cluster, where
the single best model retains only6.0%of first-best and per-cluster routing64.0%, while the auction
holds96 .0%and93 .0%. Bidders see their own value𝑣𝑖(𝑞) before bidding, so a specialist can outbid
5We use99.9%coverage instead of the minimum to avoid outlier markets where the solver has not converged.
8

Price of Anarchy of First-Price Auctions in Agentic Markets
0.65 0.70 0.75 0.80 0.85 0.90 0.95 1.00
0
40
80
Empirical PoA
Empirical Frequency
Empirical PoA Distribution
𝑛=2
𝑛=5
𝑛=10
Competitive-floor bound
Realized
1−1/𝑒
[.63, .64) [.64, .66) [.66, .70) [.70, .75) [.75, .80) [.80, .90) [.90, 1.00)
0.70
0.80
0.90
1.00
0.82
0.86
0.90 0.92 0.93
0.95 0.96
0.85
0.90
0.93 0.95 0.95 0.97 0.96
Competitive-floor bound bin
Empirical PoA
PoA Bounds vs Empirical PoA
Realized equilibria (p0.1)
Realized equilibria (p0.1, adv)
1−1/𝑒
Figure 2| Left:Empirical distributions of the Theorem 3 bound (dotted) and the empirical PoA
(solid) across100𝑘 random 𝑛-model subsets of EmbedLLM, for𝑛∈{ 2, 5, 10}. Both distributions
tighten as𝑛 grows, and are well above the distribution-free baseline (dashed).Right:Bottom0.1%
of empirical PoA across sub-markets grouped by bound bin (100𝑘 samples per bin), for both typical
equilibria (solid green) and approximate, adversarial equilibria (hatched red).
the cluster leader on exactly the prompts where the leader is weak, which is what a fixed rule cannot
do. On the full market and prompt distribution, Theorem 3 guarantees a welfare ratio≥ 79.9%(and a
minimum bound of67.6%on the worst cluster). Both are substantially above the naive1− 1/𝑒 bound,
though still below what the market achieves. The1− 1/𝑒 bound holds for every market and so cannot
indicate anything more specific about this one, whereas79.9%is computed from the empirical value
prior of this market, and correctly signals that welfare will be high. Note that we do not expect it to be
tight, since the bound only uses the competitive floor and treats everything else as worst case, while
near-independence (Section 4) is a second and separate reason this market can be efficient.
Results on randomly sampled EmbedLLM sub-markets.Moving beyond the full EmbedLLM market
setting, wenextlookatwelfareinthousandsofauctionsamongsubsetsofEmbedLLMmodels. Figure2
(left) plots the empirical distributions of both (a) the competitive-floor bound of Theorem 3, and
(b) the realized welfare ratio at a typical equilibrium over100𝑘 randomly sampled model subsets
of market size𝑛∈{ 2, 5, 10}. Both distributions concentrate as𝑛 grows, and their lower tails move up.
Realized welfare is much higher than1− 1/𝑒, as are our bounds (though while the competitive-floor
bounds are tighter, they are still conservative). In practice, the realized welfare ratio of the vast
majority of sampled auctions falls above95%. That said, unlike the worst-case1− 1/𝑒 bound, which is
the same for every market, the competitive-floor bounds aresensitiveto the market they are computed
for. Figure 2 (right) groups randomly sampled model subsets for market sizes𝑛∈{ 2,..., 25} into
bins according to their competitive-floor bound, where the bins span[1− 1/𝑒, 1.00). We sample100𝑘
subsets per bin, and report the bottom0.1%of realized welfare ratios within each bin, for both the
typical and the adversarial strategy solver. The realized welfare at an adversarial equilibrium rises
with the bins, from0.82in the[0.63, 0.64) bin to0.96in the[0.90, 1.00) bin. At a typical equilibrium
it rises from0.85in the lowest bin to0.97in the[0.80,0.90)bin, and is0.96in the top bin.
Results on illustrative EmbedLLM cohorts.Random sub-markets vary in both how good their best
model is and how much competition it faces. To separate the two, Table 2 shows results for four hand-
picked cohorts of𝑛= 4models with nearly identical first-best welfare (𝔼[max𝑖𝑉𝑖]≈ 0.55) but different
market structure. In thesimilarcohort, the four models are comparable7B chat models (Starling-
LM-7B-beta, OpenChat-3.5-0106, Zephyr-7B-beta, and Mistral-7B-Instruct-v0.1) with average values
between0 .43and0 .51. In thediversecohort (Qwen-1.5-7B-Chat, BioMistral-7B-DARE, ANIMA-
Nectar-v2, and Zephyr-beta-math), the models have an even tighter range of average values (0.42
to0 .46), but they are good at different things, so on a given prompt the runner-up tends to trail
the winner by more (17.1%versus7 .7%). For both cohorts the competitive-floor bound limits the
9

Price of Anarchy of First-Price Auctions in Agentic Markets
Cohort𝔼[max 𝑖𝑉𝑖]1−𝔼[𝑉 (2)]/𝔼[𝑉(1)]Loss bound Shading Welfare loss (adv)
Generalists (similar)0.557 7.7% 24.2% 12.3% 0.4%
Generalists (diverse)0.553 17.1% 27.4% 19.8% 1.2%
Generalists (1) + niche (3)0.552 35.6% 29.9% 29.1% 5.1%
Generalists (2) + niche (2)0.555 15.9% 27.9% 22.3% 0.8%
Table 2| Four cohorts constructed to have comparable𝔼[max𝑖𝑉𝑖], but different value structure. We
report welfare as a loss, i.e., as the fraction of optimal welfare that is lost.Loss boundis one minus
the competitive-floor bound of Theorem 3 (worst case is1/𝑒≈ 36.8%), andWelfare lossis one minus
the realized PoA (at the adversarially-chosen equilibrium). Shading is1−𝔼[𝐵winner/𝑉winner].
welfare loss to well below the worst case of1/𝑒≈ 36.8%, and the limit is lower for the similar cohort
(24.2%versus27 .4%). Actual losses are small in both, but the winner shades much more in the
diverse cohort (19.8%versus12 .3%), so the similar cohort loses slightly less welfare (0.4%versus
1.2%). Nevertheless, the bidder diversity here is only mild, as every model is still a credible rival on
many prompts. When a "generalist" (Yi-34B-Chat) is paired with three weaker, "niche" models (Qwen-
1.5-0.5B-Chat, DeepSeek-Coder-6.7B-Instruct, and Gemma-2B-it), the runner-up trails by35.6%on
average, the winner shades by29.1%, the loss bound rises to29.9%, and the welfare loss rises to5.1%.
Swapping one niche model for a second generalist is enough to bring the welfare loss back down to
0.8%, even though half the cohort is still weak (here the generalists are SOLAR-10.7B-Instruct and
Neural-Chat-7B-v3-3, paired with Qwen-1.5-0.5B-Chat and Gemma-2B-it). These results support our
core intuition that value concentration limits shading and thereby reduces overall welfare loss.
7. Related work
Prior work on agentic markets has focused on dominant strategy incentive-compatible (DSIC) mech-
anisms, where bidding one’s true value (or cost, in a procurement auction) is optimal. Chang et al.
(2020) first used second-price auctions to solve general, sequential Markov decision problems (though
not with modern AI agents), while more recent work has used Vickrey-Clarke-Groves (VCG) auctions
to orchestrate LLM agents (Liu et al., 2026) and reverse second-price auctions to allocate test-time
compute (Velasco et al., 2026). These mechanisms, however, do have significant weaknesses—such as
being susceptible to collusion (Robinson, 1985) and requiring bidders to trust the auctioneer (Ausubel
and Milgrom, 2004; Rothkopf et al., 1990). In this paper we study the viability of the first-price
auction, and argue that its lack of truthfulness is less of a concern under value structures we expect
agentic markets to have, such as competitive floors and weakly dependent values.
The price of anarchy (PoA) of first-price auctions is well studied. Smoothness arguments (Roughgar-
den et al., 2017) give a universal1− 1/𝑒≈ 0.632bound under arbitrary correlation (Christodoulou
et al., 2016; Syrgkanis and Tardos, 2013). For independent private values, the bound was later
raised to0.743(Hoy et al., 2018), and then to1− 1/𝑒2≈ 0.865, which is tight (Jin and Lu, 2023a).
All of these bounds are worst case over the value distribution, and they remain tight even for the
best equilibrium (Jin and Lu, 2023b). We show how these boundscanimprove under additional
structure on the values. Related settings have their own beyond-worst-case results. For example,
when a bidder’s value depends on what others privately know, the PoA of simple auctions can be
poor, but improves when information is spread evenly (Eden et al., 2021). Revenue guarantees can
also be shown to be robust to small changes in the prior (Brustle et al., 2020), similar in spirit to
our weak dependence result (Section 4), where the1− 1/𝑒2 bound degrades smoothly with distance
from independence even as equilibrium strategies shift. Finally, our experiments connect to empirical
approaches to the PoA (Hartline, 2026; Hoy et al., 2017), and to average-case analyses that weight
equilibria by how likely learning dynamics are to reach them (Panageas and Piliouras, 2016).
10

Price of Anarchy of First-Price Auctions in Agentic Markets
8. Conclusion
This paper analyzes the welfare of first-price auctions (FPAs) among AI agents, where the main
objection to non-truthful mechanisms like the FPA is that they are vulnerable to welfare loss from bid
shading. Worst-case price of anarchy bounds are pessimistic, but agentic markets often have structure
that narrows the gap. We prove that the welfare guarantee rises toward full efficiency when the
strongest few bidders have similar values, and that the1−1/𝑒2 bound for independent values degrades
smoothly when values are only weakly dependent (e.g., given the query). Finally, we show that plat-
forms themselves can take simple steps to protect the efficiency of their markets, such as filtering out
weak bidders with routing rules, or entering their own models to set competitive reserve prices.
References
O. Armantier, J.-P. Florens, and J.-F. Richard. Approximation of nash equilibria in bayesian games.
Journal of Applied Econometrics, 23(7):965–981, 2008. doi: https://doi.org/10.1002/jae.1040.
URL https://onlinelibrary.wiley.com/doi/abs/10.1002/jae.1040.
M. Aubakirova, A. Atallah, C. Clark, J. Summerville, and A. Midha. State of AI: An empirical 100
trillion token study with OpenRouter. https://openrouter.ai/state-of-ai, December 2025. a16z and
OpenRouter Inc.
L. M. Ausubel and P. Milgrom. The lovely but lonely vickrey auction. Discussion Papers 03-036,
Stanford Institute for Economic Policy Research, 2004. URL https://EconPapers.repec.org/RePEc:
sip:dpaper:03-036.
V. Bosshard, B. Bünz, B. Lubin, and S. Seuken. Computing bayes-nash equilibria in combinatorial
auctions with verification.Journal of Artificial Intelligence Research, 69:531–570, 2020.
G. W. Brown. Iterative solution of games by fictitious play. In T. C. Koopmans, editor,Activity Analysis
of Production and Allocation, pages 374–376. Wiley, New York, 1951.
J. Brustle, Y. Cai, and C. Daskalakis. Multi-item mechanisms without item-independence: Learnability
via robustness. InProceedings of the 21st ACM Conference on Economics and Computation (EC),
2020.
Y. Cao, Y. Wang, S. Liu, M. Li, Y. Tao, and T. He. Pay for the second-best service: A game-theoretic
approach against dishonest llm providers. InProceedings of the ACM Web Conference 2026, WWW
’26, page 249–260, New York, NY, USA, 2026. Association for Computing Machinery. ISBN
9798400723070. doi: 10.1145/3774904.3792446. URL https://doi.org/10.1145/3774904.
3792446.
M. Chang, S. Kaushik, S. M. Weinberg, T. Griffiths, and S. Levine. Decentralized reinforcement
learning: Global decision-making via local economic transactions. InInternational Conference on
Machine Learning, pages 1437–1447. PMLR, 2020.
S. Chawla and J. D. Hartline. Auctions with unique equilibria. InProceedings of the Fourteenth ACM
Conference on Electronic Commerce, EC ’13, page 181–196, New York, NY, USA, 2013. Association
for Computing Machinery. ISBN 9781450319621. doi: 10.1145/2492002.2483188. URL https:
//doi.org/10.1145/2492002.2483188.
L. Chen, M. Zaharia, and J. Zou. FrugalGPT: How to use large language models while reducing cost
and improving performance.Transactions on Machine Learning Research, 2024. ISSN 2835-8856.
URL https://openreview.net/forum?id=cSimKw5p6R. Featured Certification.
11

Price of Anarchy of First-Price Auctions in Agentic Markets
G. Christodoulou, A. Kovács, A. Sgouritsa, and B. Tang. Tight bounds for the price of anarchy of
simultaneous first-price auctions.ACM Trans. Econ. Comput., 4(2), Jan. 2016. ISSN 2167-8375.
doi: 10.1145/2847520. URL https://doi.org/10.1145/2847520.
T. C. Christofides and E. Vaggelatou. A connection between supermodular ordering and positive/neg-
ative association.Journal of Multivariate Analysis, 88(1):138–151, 2004. ISSN 0047-259X. doi:
https://doi.org/10.1016/S0047-259X(03)00064-2. URL https://www.sciencedirect.com/science/
article/pii/S0047259X03000642.
S. Cox. Simplifying programmatic: First price auctions for Google Ad Manager. https://blog.google/
products/admanager/simplifying-programmatic-first-price-auctions-google-ad-manager/, March
2019. Google Ad Manager Blog.
D.Ding, A.Mallick, C.Wang, R.Sim, S.Mukherjee, V.Rühle, L.V.S.Lakshmanan, andA.H.Awadallah.
Hybrid LLM: Cost-efficient and quality-aware query routing. InThe Twelfth International Conference
on Learning Representations, 2024. URL https://openreview.net/forum?id=02f3mUtqnM.
T. Ding, D. Perrault-Joncas, O. Ronen, M. I. Jordan, D. Bergemann, D. Foster, and O. Gottesman.
Marketplace operators can induce competitive pricing, 2025. URL https://arxiv.org/abs/2503.
06582.
A. Eden, M. Feldman, I. Talgam-Cohen, and O. Zviran. Poa of simple auctions with interdependent
values. InProceedings of the AAAI Conference on Artificial Intelligence, 2021.
A. Fisch, J. Maynez, R. A. Hofer, B. Dhingra, A. Globerson, and W. W. Cohen. Stratified prediction-
powered inference for effective hybrid evaluation of language models. InAdvances in Neural
Information Processing Systems, 2024.
J. Hartline. The economics of no-regret learning algorithms, 2026. URL https://arxiv.org/abs/2601.
22079.
J. Hartline, D. Hoy, and S. Taggart. Price of anarchy for auction revenue. InProceedings of the Fifteenth
ACM Conference on Economics and Computation, EC ’14, page 693–710, New York, NY, USA, 2014.
Association for Computing Machinery. ISBN 9781450325653. doi: 10.1145/2600057.2602878.
URL https://doi.org/10.1145/2600057.2602878.
B. Heymann and P. Mertikopoulos. An empirical study of fictitious play for estimating nash equilibria
in first-price auctions with correlated values.arXiv preprint arXiv:2606.16389, 2026. URL https:
//arxiv.org/abs/2606.16389.
V. Hofmann, D. Heineman, I. Magnusson, K. Lo, J. Dodge, M. Sap, P. W. Koh, C. Wang, H. Hajishirzi,
and N. A. Smith. Fluid language model benchmarking.arXiv preprint arXiv:2509.11106, 2025.
D. Hoy, D. Nekipelov, and V. Syrgkanis. Welfare guarantees from data. In I. Guyon, U. V. Luxburg,
S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett, editors,Advances in Neural
Information Processing Systems, volume 30. Curran Associates, Inc., 2017. URL https://proceedings.
neurips.cc/paper_files/paper/2017/file/d3a7f48c12e697d50c8a7ae7684644ef-Paper.pdf.
D. Hoy, S. Taggart, and Z. Wang. A tighter welfare guarantee for first-price auctions. InProceedings
of the 50th Annual ACM SIGACT Symposium on Theory of Computing, STOC 2018, page 132–137,
New York, NY, USA, 2018. Association for Computing Machinery. ISBN 9781450355599. doi:
10.1145/3188745.3188944. URL https://doi.org/10.1145/3188745.3188944.
Q. J. Hu, J. Bieker, X. Li, N. Jiang, B. Keigwin, G. Ranganath, K. Keutzer, and S. K. Upadhyay.
Routerbench: A benchmark for multi-llm routing system.arXiv preprint arXiv: 2403.12031, 2024.
12

Price of Anarchy of First-Price Auctions in Agentic Markets
Y. Jin and P. Lu. First price auction is1− 1/𝑒2 efficient.J. ACM, 70(5), Oct. 2023a. ISSN 0004-5411.
doi: 10.1145/3617902. URL https://doi.org/10.1145/3617902.
Y. Jin and P. Lu. The price of stability for first price auction. InProceedings of the 2023 Annual
ACM-SIAM Symposium on Discrete Algorithms (SODA), pages 332–352, 2023b. doi: 10.1137/1.
9781611977554.ch14. URL https://epubs.siam.org/doi/abs/10.1137/1.9781611977554.ch14.
W. Jitkrittum, H. Narasimhan, A. S. Rawat, J. Juneja, C. Wang, Z. Wang, A. Go, C.-Y. Lee,
P. Shenoy, R. Panigrahy, et al. Universal model routing for efficient LLM inference.arXiv preprint
arXiv:2502.08773, 2025.
X. Liu, H. Li, S. Li, H. Fang, F. Xu, F. Shi, and J. Evans. Markets, not planners: Decentralized
orchestration of llm agents with private information.arXiv preprint arXiv:2608.23867, 2026.
A. Maimon, A. D. N. Cohen, G. Vishne, S. Ravfogel, and R. Tsarfaty. From benchmarks to skills:
Low-rank factors for LLM evaluation.Transactions of the Association for Computational Linguistics,
14:1660–1684, 2026. doi: 10.1162/tacl.a.745. URL https://aclanthology.org/2026.tacl-1.75/.
P. R. Milgrom and R. J. Weber. A theory of auctions and competitive bidding.Econometrica: Journal
of the Econometric Society, pages 1089–1122, 1982.
I. Ong, A. Almahairi, V. Wu, W.-L. Chiang, T. Wu, J. E. Gonzalez, M. W. Kadous, and I. Stoica.
RouteLLM: Learning to route LLMs from preference data. InThe Thirteenth International Conference
on Learning Representations, 2025. URL https://openreview.net/forum?id=8sSqNntaMr.
R. Paes Leme, B. Sivan, and Y. Teng. Why do competitive markets converge to first-price auctions?
InProceedings of The Web Conference 2020, WWW ’20, page 596–605, New York, NY, USA, 2020.
Association for Computing Machinery. ISBN 9781450370233. doi: 10.1145/3366423.3380142.
URL https://doi.org/10.1145/3366423.3380142.
I. Panageas and G. Piliouras. Average case performance of replicator dynamics in potential games
via computing regions of attraction. InProceedings of the 2016 ACM Conference on Economics
and Computation, EC ’16, page 703–720, New York, NY, USA, 2016. Association for Computing
Machinery. ISBN 9781450339360. doi: 10.1145/2940716.2940784. URL https://doi.org/10.
1145/2940716.2940784.
Z. Qi, H. Su, A. Qu, C. Wang, Y. Yao, H. Zheng, K. Chattopadhyay, G. Xu, Z. Wang, W. Ye, V. J.
Reddi, J. Li, P. P. Liang, H. Lakkaraju, S. Kakade, and Y. Du. Economy of minds: Emerging
multi-agent intelligence with economic interactions.ArXiv preprint: 2606.02859, 2026. URL
https://arxiv.org/abs/2606.02859.
Z. Rabinovich, V. Naroditskiy, E. H. Gerding, and N. R. Jennings. Computing pure bayesian-nash
equilibria in games with finite actions and continuous types.Artificial Intelligence, 195:106–
139, 2013. ISSN 0004-3702. doi: https://doi.org/10.1016/j.artint.2012.09.007. URL https:
//www.sciencedirect.com/science/article/pii/S0004370212001191.
M. S. Robinson. Collusion and the choice of auction.The RAND Journal of Economics, pages 141–145,
1985.
M. H. Rothkopf, T. J. Teisberg, and E. P. Kahn. Why are vickrey auctions rare?Journal of Political
Economy, 98(1):94–109, 1990.
T. Roughgarden, V. Syrgkanis, and E. Tardos. The price of anarchy in auctions.J. Artif. Int. Res., 59
(1):59–101, May 2017. ISSN 1076-9757.
13

Price of Anarchy of First-Price Auctions in Agentic Markets
M. Shanbhogue, Z. Li, S. Zhang, G. H. Ábrego, S.-C. Huang, A. Jain, D. Salz, S. Goenka, C. Hegde,
J. Ma, F. Chen, J. Wu, T. Dabral, B. Samari, K. Poulet, D. Cer, K. Chen, P. Suganathan, H. Hui,
J. Andonov, P. Schlattner, J. Han, I. Naim, W. Lowe, V. Pchelin, A. Yang, Y.-T. Chen, Z. Ding, G. Zhang,
G. Heigold, Y. Chen, A. Reveillon, B. Mccloskey, W. Zhou, D. Kim, R. Meng, E. Wang, J. Zheng,
H. Fede, Z. Yang, K. Mosley, B. Potetz, S. Dua, H. S. Vera, S. Gao, H. Zhang, A. Hess, H. Ying,
A. Montes, K. Gill, M. Choi, S. Russo, A. Hauth, J. Lee, M. Boratko, M. Barnes, V. Rao, C. Musat,
C. Allauzen, E. Variani, S. Kumar, T. Bagby, J. Jiao, Y. Gu, T. Li, A. Agrawal, R. Santana, D. Nath,
S. Karukas, S. Han, L. Loher, A. Twu, N. Vyas, S. Bhai, F. P. Gomez, W. Zhang, C. Liu, J. Yang, S. Qiu,
S. Zhang, S. Kulkarni, S. Rothe, S. Nakamoto, R. Hoffmann, Z. Gleicher, Y. Sung, Q. Yin, T. Duerig,
and M. Seyedhosseini. Gemini embedding 2: A native multimodal embedding model from gemini.
arXiv preprint: arXiv 2605.27295, 2026. URL https://arxiv.org/abs/2605.27295.
R. Shopova. Private labels in marketplaces.International Journal of Industrial Organization, 89:
102949, 2023. ISSN 0167-7187. doi: https://doi.org/10.1016/j.ijindorg.2023.102949. URL
https://www.sciencedirect.com/science/article/pii/S0167718723000309.
V. Syrgkanis and E. Tardos. Composable and efficient mechanisms. InProceedings of the Forty-Fifth
AnnualACMSymposiumonTheoryofComputing,STOC’13,page211–220,NewYork,NY,USA,2013.
Association for Computing Machinery. ISBN 9781450320290. doi: 10.1145/2488608.2488635.
URL https://doi.org/10.1145/2488608.2488635.
A. A. Velasco, D. Rontogiannis, S. Tsirtsis, and M. Gomez-Rodriguez. Test-time compute games.arXiv
preprint arXiv:2601.21839, 2026.
R. Zhuang, T. Wu, Z. Wen, A. Li, J. Jiao, and K. Ramchandran. Embedllm: Learning compact
representations of large language models. InInternational Conference on Learning Representations,
volume 2025, pages 76913–76926, 2025.
14

Price of Anarchy of First-Price Auctions in Agentic Markets
Contents
A Limitations and future work 16
B Additional theoretical results 16
B.1 Bounds that hold over a family of priors . . . . . . . . . . . . . . . . . . . . . . . . . 16
B.2 Positively dependent values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
B.3 Query-conditional competitive floors . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
B.4 Example: Competitive floors from specialist models . . . . . . . . . . . . . . . . . . . 17
C Additional experimental results 18
C.1 Near-independence given the prompt . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
C.2 Platform-owned bidder . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
C.3 Pre-auction filtering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
D Equilibrium solver 20
E Proofs for competitive floors 22
E.1 Deterministic competitive floor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
E.2 Probabilistic competitive floor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
E.3 Welfare with a committed platform bidder . . . . . . . . . . . . . . . . . . . . . . . . 26
F Proofs and additional results for weak dependence 26
F.1 Warmup: Robustness of the1− 1 𝑒  bound . . . . . . . . . . . . . . . . . . . . . . . . 26
F.2 Proof overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
F.3 Welfare shortfall under small regret . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
F.4 Proof of the main qualitative theorem (Theorem 5). . . . . . . . . . . . . . . . . . . . 31
F.5 A quantitative bound for weakly-dependent values . . . . . . . . . . . . . . . . . . . 31
15

Price of Anarchy of First-Price Auctions in Agentic Markets
A. Limitations and future work
We assume that models and users are aligned in the sense that positive utility derives only from
providing value to the user; external sources of utility, such as advertising placement, would obviously
require additional analysis. Second, like all price of anarchy results, our bounds only describe bidders
who play equilibrium strategies. Auctions composed of agents that are still learning how to bid, or
that bid by simple heuristics, could result in realized welfare that is quite a bit worse (or better!)
than the welfare at any equilibrium bidding strategy. Extending our analysis to include realistic
learning dynamics for first-price auctions in agentic markets is a valuable next step. Third, we
analyze competitive floors and near-independence separately, and in experiments we only compute
the competitive-floor bound. Real markets like EmbedLLM appear to have both properties (Section 6
and Section C.1). Taking the larger of the two guarantees is immediate, but a bound that uses both
properties together could be stronger, but is non-trivial. We leave this to future work.
Finally, we focus on welfare in this paper. Revenue matters to the platform and its price of anarchy can
behave quite differently (Hartline et al., 2014); we leave revenue guarantees to future work.
B. Additional theoretical results
B.1. Bounds that hold over a family of priors
Each bound in Sections 3 and 4 holds for every equilibrium under a single prior𝜇. Write𝐿(𝜇) for that
bound, where each prior can satisfy the assumptions with its own parameters (e.g., its own𝛼, 𝑚, and
𝜖 in Theorem 3). For a family of priorsM, the PoA is then at least the smallest of these bounds:
inf
𝜇∈M
inf
s∈BNE(𝜇)
𝔼𝜇[𝑊(s(V),V)]
𝔼𝜇[𝑉(1)] ≥inf 𝜇∈M 𝐿(𝜇).(10)
For example, fix𝑚, a bound¯𝑣 >0, and a distribution function𝐺, and letM contain every prior with
0 <𝔼 𝜇[𝑉(1)]≤¯𝑣 under which𝑉(𝑚) stochastically dominates𝐺, i.e., ℙ𝜇(𝑉(𝑚) < 𝑡)≤𝐺(𝑡) for all𝑡. Then
for every𝛼∈[0,1]and𝜇∈M,
ℙ𝜇

𝑉(𝑚) < 𝛼𝔼𝜇[𝑉(1)]≤ℙ 𝜇  𝑉(𝑚) < 𝛼¯𝑣 ≤𝐺(𝛼¯𝑣),
so every𝜇∈Mhas an(𝛼,𝑚,𝐺(𝛼¯𝑣))-competitive floor, and applying Theorem 3 gives:
inf
𝜇∈M
inf
s∈BNE(𝜇)
𝔼𝜇[𝑊(s(V),V)]
𝔼𝜇[𝑉(1)] ≥

1− 1 𝑒  +sup 𝛼∈[0,1] 𝛼 h 1 𝑒−𝑆 𝑚  𝐺(𝛼¯𝑣)i + .(11)
B.2. Positively dependent values
In auction theory, positive dependence between bidder values is usually modeled by affiliation (Mil-
grom and Weber, 1982). It is interesting to consider what this implies with respect to our bounds
in Section 3. Informally, values are affiliated if learning that some bidders value a query highly
makes it more likely that the others do too, as when all models tend to do well on easy queries
and poorly on hard ones. Affiliated values areassociated, meaning that any two functions ofVthat
are nondecreasing in every coordinate are nonnegatively correlated. For associated values, it is
straightforward to show that the floor in Equation (3) is always at least as high as it would be if the
same values were independent. LetV∗ have independent coordinates with𝑉∗ 𝑖 distributed as𝑉𝑖, and
write𝑉∗ (1) and𝑉∗ (𝑛) for its largest and smallest coordinates. Then the following result holds.
Proposition B.1.IfVis associated and0 <𝔼[𝑉 (1)]<∞ , then 𝔼[𝑉(𝑛)]≥𝔼[𝑉 ∗ (𝑛)] and 𝔼[𝑉(1)]≤𝔼[𝑉 ∗ (1)].
In particular,𝔼[𝑉(𝑛)]/𝔼[𝑉(1)]≥𝔼[𝑉 ∗ (𝑛)]/𝔼[𝑉∗ (1)].
16

Price of Anarchy of First-Price Auctions in Agentic Markets
Proof. Christofides and Vaggelatou (2004) show that𝔼[𝑓( V)]≥𝔼[𝑓( V∗)] for every supermodular𝑓,
i.e., every𝑓 with 𝑓( x∨ y)+𝑓( x∧ y)≥𝑓( x)+𝑓( y), where∨ and∧ are the coordinatewise maximum
and minimum. Bothmin𝑖𝑥𝑖 and−max𝑖𝑥𝑖 are supermodular, sincemin𝑖(𝑥𝑖∧𝑦𝑖)=min{min 𝑖𝑥𝑖,min𝑖 𝑦𝑖}
and min𝑖(𝑥𝑖∨𝑦 𝑖)≥max{min 𝑖𝑥𝑖,min𝑖 𝑦𝑖}, while a symmetric argument applies for the maximum.
Applying the result to both functions gives the two inequalities.□
Note, however, that a similar straightforward connection cannot be made to Theorem 3! In fact, the
bound in Theorem 3 can get worse, since positive dependence can make bidders fall below the floor
on the same queries, which raises𝜖 relative to independent values with the same marginals. We leave
a closer study of how dependence between values affects competitive floors to future work.
B.3. Query-conditional competitive floors
The results in the main text apply to a fixed value prior𝜇. However, as in Section 4, it is reasonable to
assume that each query in an agentic market comes with public information𝑋 that all bidders see
before they bid (such as the prompt text), which induces a conditional prior𝜇𝑥 :=𝜇(·|𝑋=𝑥) . As
with 𝜇, we assume each𝜇𝑥 is common knowledge among the bidders. We can then apply Theorem 3
conditionally to each query, with its own𝛼𝑥,𝑚 𝑥, and𝜖𝑥, and subsequently average over𝑋.
Corollary B.2.Suppose0 <𝔼[𝑉 (1)]<∞ and that for almost every𝑥, 𝜇𝑥 has an(𝛼𝑥,𝑚 𝑥,𝜖𝑥)-competitive
floor, i.e.,ℙ 𝑉(𝑚𝑥)≥𝛼 𝑥𝔼[𝑉(1)|𝑋=𝑥]|𝑋=𝑥 ≥1−𝜖 𝑥. Then everys∈BNE(𝜇)satisfies
𝔼[𝑊(s(V),V)]≥𝔼 𝑋
h
1− 1 𝑒  +𝛼 𝑋 h 1 𝑒−𝑆 𝑚𝑋  𝜖𝑋 i +  𝔼[𝑉(1)|𝑋] i .(12)
Proof.Fix𝑥with𝔼[𝑉 (1)|𝑋=𝑥]>0. Applying Theorem 3 under𝜇 𝑥 gives
𝔼[𝑊(s(V),V)|𝑋=𝑥]≥

1− 1 𝑒  +𝛼 𝑥 h 1 𝑒−𝑆 𝑚𝑥  𝜖𝑥 i +  𝔼[𝑉(1)|𝑋=𝑥].
If𝔼[𝑉(1)|𝑋=𝑥]=0, both sides are0. Taking expectations over𝑋proves the claim.□
The conditional bound improves on applying Theorem 3 to𝜇 directly because the floor𝛼𝑥𝔼[𝑉(1)|𝑋=
𝑥] adapts to each query. A single floor𝛼𝔼[𝑉(1)] is too high for hard queries, which inflates𝜖, and too
low for easy ones.
B.4. Example: Competitive floors from specialist models
We give a stylized example that illustrates a competitive floor in a (toy) agentic market. Suppose there
are 𝑑 "capabilities" that models in the market may posses; write model𝑖 as having a capability set
𝐴𝑖⊆[𝑑] . Further suppose that each query requires a set of capabilities𝑌⊆[𝑑] to solve it. A model can
"handle" the query if it has every required capability,𝑌⊆𝐴 𝑖. Normalize values to[0, 1]. Then suppose
any model that can "handle" the query has value at least𝛼 for some0< 𝛼≤ 1, and a model that cannot
has value0. The values of the models that can handle the query may be arbitrarily dependent.
For a given requirement set𝑌, let𝑁𝑌 :=|{𝑖 : 𝑌⊆𝐴 𝑖}| be the number of models that can handle it.
Since 𝔼[𝑉(1)]≤ 1, on the event𝑁𝑌≥𝑚 we have𝑉(𝑚)≥𝛼≥𝛼𝔼[𝑉 (1)]. The market therefore has an
(𝛼,𝑚,𝜖) -competitive floor with𝜖=ℙ(𝑁 𝑌 < 𝑚)—i.e., the probability that a random query drawn from
the market’s query distribution requires a capability combination that fewer than𝑚models have.
To see when𝜖 is small, suppose each model has each capability independently with probability𝑝,
and group queries by the number𝑇 :=|𝑌| of capabilities they require. A query requiring𝑡 capabilities
can be handled by each model with probability𝑝𝑡, so it has𝑁𝑌∼Bin(𝑛,𝑝 𝑡) capable models and fails
to have𝑚of them with probability𝜖𝑡 :=ℙ(Bin(𝑛,𝑝 𝑡)< 𝑚). Then𝜖= ˝ 𝑡 ℙ(𝑇=𝑡)𝜖 𝑡.
17

Price of Anarchy of First-Price Auctions in Agentic Markets
0 0.2 0.4 0.6 0.8 1
0
5
10
𝑅2 of𝑣 𝑖
Density
rival only
rival after prompt
prompt only
(a) Variance of𝑣𝑖 explained
0 0.2 0.4 0.6 0.8 1
0
0.2
0.4
0.6
0.8
1
𝑅2 from rival only
Δ𝑅2 from rival after prompt
(b) Rival information left after prompt
Figure 3| How well the prompt and a rival predict each model’s value𝑣𝑖.(a)Distribution of 𝑅2 from
the held-out ridge prediction𝑔𝑖(𝑞) alone (one value per model), and from a rival’s value𝑣𝑗 alone
and the gain from adding the rival once the prompt is known (one value per ordered model pair
(𝑖, 𝑗)).(b)Each point is one of2 ,000randomly sampled model pairs(𝑖, 𝑗), plotting the rival’s𝑅2
on its own against the gain it adds once the prompt is known. The dashed line is𝑦=𝑥 . For points
far below it, most of what the rival’s value predicts about𝑣𝑖 is already captured by the prompt.
As a further simplification, we can write a loose upper bound for𝜖 as follows. Pick a cutoff𝑡0≥ 0, and
assume that any query requiring𝑡 > 𝑡0 capabilities always has fewer than𝑚 models that can handle it
(i.e.,𝜖 𝑡 =1for𝑡 > 𝑡 0). Then, since𝜖𝑡 increases in𝑡, we can write
𝜖=
∑︁
𝑡
ℙ(𝑇=𝑡)𝜖 𝑡≤
𝑡0∑︁
𝑡=0
ℙ(𝑇=𝑡)𝜖 𝑡+ℙ(𝑇 > 𝑡0)
≤
𝑡0∑︁
𝑡=0
ℙ(𝑇=𝑡)𝜖 𝑡0+ℙ(𝑇 > 𝑡0)
≤𝜖 𝑡0+ℙ(𝑇 > 𝑡0).
For example, with𝑛= 100models, 𝑚= 8, and𝑝= 0.8, a query requiring𝑡0 = 9capabilities has13 .4
capable models on average and𝜖9 = 0.03. So if at most3%of queries require more than9capabilities,
then𝜖≤ 0.06. Finally, suppose the reward for a "handled" query is always1(i.e., the response is either
right or wrong), so𝛼= 1. Then Theorem 3 guarantees at least(1− 1/𝑒)+[ 1/𝑒−𝑆 8(0.06)]≈ 0.89of
the optimal welfare, compared with≈ 0.63from the1 − 1/𝑒 bound alone. This holds even though the
values are dependent through the shared query.
A similar argument applies when model𝑖 has capability𝑗 with probability𝑝𝑖𝑗, with𝜇𝑌 = ˝ 𝑖 ˛ 𝑗∈𝑌 𝑝𝑖𝑗.
Thefloorthenfailsonqueriesthatrequireararecapabilityormanycapabilities, where 𝜇𝑌 issmall, and
it holds on everything else as long as several models have high𝑝𝑖𝑗 on the required capabilities.
C. Additional experimental results
This section gives additional results for the EmbedLLM market experiments described in Section 6.
Specifically, Section C.1 tests the conjecture from Section 4 that bidder values are close to independent
once the prompt is known. Sections C.2 and C.3 then empirically evaluate the two platform design
choices from Section 5: a platform-owned bidder and pre-auction filtering of weak models.
C.1. Near-independence given the prompt
Section 4 conjectures that most of the dependence between bidder values in agentic markets can
be eliminated by conditioning on thequery, so that values are close to independent once the query
18

Price of Anarchy of First-Price Auctions in Agentic Markets
is known. Recall from Section 6 that𝑣𝑖(𝑞)=max( 0, ˆ𝔼[acc𝑖|𝑞]−𝑐 𝑖), where the accuracy estimate
averages over the𝑘= 16nearest neighbors of𝑞. These estimates follow the intuition that a model
performs similarly on similar queries. In our construction this holds exactly by design, since every
model’s value on a prompt is averaged over the same neighbors, which favors the prompt as a predictor
here. The general idea still holds more broadly. Much of what makes models succeed or fail together
is a property of the query itself, such as its difficulty, its topic, or how clearly it is specified (Fisch
et al., 2024; Hofmann et al., 2025; Maimon et al., 2026)—and routers already estimate per-query
model performance from the prompt (Hu et al., 2024; Ong et al., 2025; Zhuang et al., 2025).
To test how much of this the prompt alone can predict, we fit a ridge regression𝑓𝑖 from the prompt
embedding to𝑣𝑖 for each model, using 5-fold cross-validation. For every ordered pair(𝑖, 𝑗)of the
110 models, we then compare how well𝑣𝑖 is predicted by𝑓𝑖(𝑞) alone, by the rival’s value𝑣𝑗 alone,
and by both. We measure each fit by its𝑅2, the proportion of the variance of𝑣𝑖 across prompts
that the predictors explain in a linear regression. The gain from adding𝑣𝑗 as a feature, i.e., taking
𝑓𝑖(𝑞)→𝑓 ′ 𝑖(𝑞,𝑣 𝑗), is what rival𝑗’s value still tells us about𝑣𝑖 once the prompt is known.
Results are in Figure 3. Averaged over all ordered pairs(𝑖, 𝑗), the prompt alone gives𝑅2 = 0.67, the
rival’s value alone gives𝑅2 = 0.50, and adding the rival once the prompt is known raises𝑅2 by only
0.05(0.09at the 90th percentile across pairs). The prompt therefore accounts for90%of what a rival’s
value explains, and is already the better predictor in84%of pairs. The pairs with the most dependence
left over are near-duplicate models whose values are almost perfectly correlated to begin with.
To be clear, these results support, but do not imply, the condition behind Theorem 5. If values were
independent given the prompt, a rival’s value would add no information about𝑣𝑖 once the prompt is
known, and this is roughly what we see. However, small gains in𝑅2 do not bound the total variation
distance 𝜏(𝑥), which we do not attempt to directly estimate. That said, it is still informative. For
example, if we make a simplifying assumption that the remaining dependence is roughly Gaussian,
𝜏(𝑥) is at most of the order of the correlations between values given𝑋=𝑥 , which scale with the
square root of the gains in𝑅2, up to a factor of at most √︁ 𝑛(𝑛−1)/2 from summing over pairs.6
C.2. Platform-owned bidder
Next, we test the platform participation strategy of Section 5 on randomly sampled markets from
EmbedLLM. Each market contains the strongest EmbedLLM model,𝑛 rivals drawn at random, and
a platform model that bids its own value on every prompt. The platform model is the EmbedLLM
model at a given percentile of the ranking by average value, where0is the weakest model and1is
the strongest (so at1the platform runs a copy of the best model). Rivals are never drawn from the
platform models used at any percentile. This lets us reuse the same random draws of rivals at every
percentile, so each curve compares the same markets. For each percentile and𝑛∈{ 5, 10} we draw
10,000random markets and solve for typical and adversarial equilibria as in Section 6.
6To see this, supposeV= f(𝑞)+𝜺 with 𝜺∼N( 0,Σ) independent of the prompt, with correlation matrix𝜌=[𝜌 𝑖𝑗]. Then
Δ𝑅2 𝑖𝑗 = Var(𝑉𝑖|𝑋)−Var(𝑉 𝑖|𝑋,𝑉 𝑗) Var(𝑉𝑖) =𝜌 2 𝑖𝑗(1−𝑅 2 prompt).
Write𝑃=N( f(𝑞),Σ) for this joint distribution and𝑄=N( f(𝑞),Σ 0) for the product of its marginals, whereΣ0 is the diagonal
ofΣ(corresponding to the conditionally independent distribution). Sincetr(Σ−1 0 Σ)=𝑛anddetΣ=detΣ 0 det𝜌, we have
𝐷KL(𝑃∥𝑄)= 1 2 h tr(Σ−1 0 Σ)−𝑛+ln detΣ 0 detΣ i =− 1 2 ln det𝜌≈ 1 2 ∑︁ 𝑖<𝑗 𝜌2 𝑖𝑗
for small correlations, so Pinsker’s inequality bounds their total variation distance by about1 2(˝ 𝑖<𝑗 𝜌2 𝑖𝑗)1/2. Hence𝜏(𝑥) is at
most of order(˝ 𝑖<𝑗 𝜌2 𝑖𝑗)1/2≤ √︁ 𝑛(𝑛−1)/2 max 𝑖<𝑗|𝜌𝑖𝑗|, where|𝜌 𝑖𝑗|= √︃ Δ𝑅2 𝑖𝑗/(1−𝑅 2 prompt).
19

Price of Anarchy of First-Price Auctions in Agentic Markets
0.0 0.2 0.4 0.6 0.8 1.0
0.90
0.92
0.94
0.96
0.98
1.00
cluster router (mean)
cluster router (p0.1)
Platform model percentile
Empirical PoA
(a)𝑛=5
0.0 0.2 0.4 0.6 0.8 1.0
0.90
0.92
0.94
0.96
0.98
1.00
cluster router (mean)
cluster router (p0.1)
Platform model percentile
Typical (mean) Typical (p0.1) Adversarial (mean) Adversarial (p0.1)
(b)𝑛=10
Figure 4| Empirical PoA with a platform-owned bidder, as a function of where the platform model
sits in the ranking of EmbedLLM models by average value. Each point averages10,000markets made
of the strongest model,𝑛 random rivals, and the platform model. Solid lines are means and dashed
lines are the0.1percentile across markets, for typical (blue) and adversarial (orange) equilibria. Gray
lines mark the cluster router on the same markets (mean solid,0.1percentile dash-dotted).
Results are shown in Figure 4. These markets always include the strongest model and are already
efficient, with a mean PoA of about0.98, so a weak or average platform model changes welfare very
little. The adversarial lower tail, however, improves noticeably as the platform model moves into the
top half, from0.94to0 .96at 𝑛= 5, and a platform model that matches the best model lifts every curve
to about0.98–0.99(note that the bestsinglemodel is not the same as the optimal composite model
that yields𝔼[max𝑖𝑉𝑖] welfare). As expected, the larger markets at𝑛= 10are already inherently more
efficient, and depend less on the platform model to keep bids competitive.
C.3. Pre-auction filtering
Finally, we test pre-auction filtering with a router that admits a model to a prompt’s auction only if the
model is close to the strongest model on the prompt’s cluster. Specifically, model𝑖 may bid on cluster
𝑐 if 𝔼[𝑉𝑖|𝑐]≥𝛽max 𝑗 𝔼[𝑉𝑗|𝑐] , where the maximum runs over the models in the market. Setting
𝛽= 0admits everyone, and𝛽= 1admits only the cluster leader. Because the rule works at the cluster
level, it can drop the model with the highest value on a particular prompt. We therefore measure
welfare against the first-best of the unfiltered market, and also report the filtered oracle, which is
the upper bound of Equation (8). For each𝛽 and 𝑛∈{ 5, 10} we draw10,000random markets.
ResultsareshowninFigure5. For 𝛽≤ 0.6therouterremovesonlyweakmodels, andthefilteredoracle
stays near1while mean welfare is unchanged at about0.99. The adversarial lower tail, however,does
improve slightly over this range, from0.947to0 .960at 𝑛= 5and from0 .964to0 .968at 𝑛= 10. Past
𝛽= 0.7the router starts dropping models that would have been best on some prompts. Consequently,
the filtered oracle falls, and realized welfare falls with it, down to about0.91when only the cluster
leader bids. As expected, filtering with a router helps only while it keeps the strongest models. At𝛽= 1
the auction reduces to a cluster router that sends every prompt to its cluster’s best model, and this
baseline (gray lines) is below the auction at every𝛽 <1, in both the mean and the0.1percentile.
D. Equilibrium solver
We compute approximate Bayes–Nash equilibria with a damped form of fictitious play (Heymann and
Mertikopoulos, 2026; Rabinovich et al., 2013), implemented directly on the empirical distribution
of values. Fictitious play goes back to Brown (1951), and approximating Bayes–Nash equilibria
20

Price of Anarchy of First-Price Auctions in Agentic Markets
0.0 0.2 0.4 0.6 0.8 1.0
0.84
0.88
0.92
0.96
1.00
cluster router (mean)
cluster router (p0.1)
Eligibility cutoff𝛽
Empirical PoA
Typical (mean) Typical (p0.1) Adversarial (mean) Adversarial (p0.1) Filtered oracle
(a)𝑛=5
0.0 0.2 0.4 0.6 0.8 1.0
0.84
0.88
0.92
0.96
1.00
cluster router (mean)
cluster router (p0.1)
Eligibility cutoff𝛽
(b)𝑛=10
Figure 5| Empirical PoA under pre-auction filtering, as a function of the eligibility cutoff𝛽. Each point
averages10,000random markets of𝑛 models. Solid lines are means and dashed lines are the0.1
percentile across markets, for typical (blue) and adversarial (orange) equilibria. The dotted line is the
filtered oracle, the welfare of always allocating to the bestadmittedmodel. Gray lines mark the cluster
router, which sends every prompt to its cluster’s best model (mean solid,0.1percentile dash-dotted).
numerically by iterating best responses over a restricted family of strategies is standard for auctions
withoutclosed-formsolutions(Armantieretal.,2008;Bosshardetal.,2020). Eachclusterofpromptsis
solved on its own. Within a cluster, every prompt is one draw from the joint distribution of the bidders’
values, so the solver keeps whatever correlation the data has and never replaces it with a product
of marginals or a smoothed prior. Fictitious play has no general convergence guarantee in first-price
auctions, but Heymann and Mertikopoulos (2026) find that it converges numerically to approximate
equilibria across a wide range of first-price auctions with correlated values, which is our setting.
Strategies.Let Q𝑐 be the set of prompts in cluster𝑐. For each bidder𝑖, we split its values onQ𝑐 into
𝐾= 5bins of equal mass, and write𝑘𝑖(𝑞)∈{ 1,...,𝐾} for the bin that contains𝑣𝑖(𝑞). We define a
bidder’sstrategytobeoneshadingfactorperbin,soonprompt 𝑞∈Q 𝑐 bidder𝑖bids𝑏𝑖(𝑞)=𝛾 𝑖,𝑐,𝑘𝑖(𝑞) 𝑣𝑖(𝑞).
Such bids never result in over-bidding. The bidder knows the prompt’s cluster and its own value, and it
knows its rivals only through the empirical distribution of their values and bids within the cluster.
Best responses.Fix bidder 𝑖, cluster𝑐, and bin𝑘, and letQ𝑘 𝑐 ={𝑞∈Q 𝑐 : 𝑘𝑖(𝑞)=𝑘} . For every
prompt𝑞∈Q 𝑘 𝑐 we record the highest rival bid𝑟(𝑞), the number𝑡(𝑞) of rivals that bid it, and their
average value. When the platform enters its own model (Section C.2), it bids its value𝑣0(𝑞), and
this bid counts as one more rival bid. The platform’s bid is public (Section 5), and any bid below
it loses, so a bidder that values the prompt above the platform’s bid never bids below it. Writing
𝑣0(𝑞)=𝑣 0(𝑞)+2·10 −6, the bid of factor𝛾on prompt𝑞is
𝑏𝛾 𝑖(𝑞)=
(
max{𝛾𝑣 𝑖(𝑞), 𝑣0(𝑞)}if𝑣 𝑖(𝑞)> 𝑣 0(𝑞),
𝛾𝑣 𝑖(𝑞)otherwise,
which never exceeds𝑣𝑖(𝑞). Without the platform,𝑏𝛾 𝑖(𝑞)=𝛾𝑣 𝑖(𝑞). If bidder𝑖 bids 𝑏 on prompt𝑞, it
wins when𝑏 > 𝑟(𝑞). Ties are split randomly among the𝑡(𝑞)+ 1tied bidders. As the winner pays its
bid, bidder𝑖’s utility is
𝑢𝑞(𝑏)=  𝑣𝑖(𝑞)−𝑏   1[𝑏 > 𝑟(𝑞)]+ 1[𝑏=𝑟(𝑞)] 𝑡(𝑞)+1  .(13)
21

Price of Anarchy of First-Price Auctions in Agentic Markets
Bidder𝑖’s average utility overQ𝑘 𝑐 from factor𝛾is
𝑈(𝛾)= 1 |Q𝑘 𝑐| ∑︁ 𝑞∈Q 𝑘 𝑐 𝑢𝑞(𝑏𝛾 𝑖(𝑞)).
The welfare𝑊(𝛾) , meanwhile, is the average overQ𝑘 𝑐 of the winner’s expected value, which is bidder
𝑖’s value when it wins and the average value of the top rivals when it loses. We search over the grid
𝛾∈{ 0, 0.01,..., 1} together with the factors𝛾=(𝑟(𝑞)+ 10−6)/𝑣𝑖(𝑞)≤ 1that just outbid the rivals
on some prompt𝑞∈Q 𝑘 𝑐. For thetypicalequilibrium, the best response is the factor with the highest
utility, and ties go to the factor closest to the current one. For theadversarialequilibrium, the best
response is the factor with the lowest welfare among those whose utility is positive and at least95%
of the highest utility. If no factor meets both conditions, the bidder keeps its current bids.
Updates.All bidders start by bidding their values. In each round, we visit the bidders in turn, and for
each of its bins a bidder moves its bids toward its best response to the current bids of the others,
𝑏𝑖(𝑞)←(1−𝜂)𝑏 𝑖(𝑞)+𝜂𝑏 ˆ𝛾 𝑖(𝑞), 𝑞∈Q 𝑘 𝑐,(14)
where ˆ𝛾is the best response. Bids start at values, so when the platform’s floor applies both terms
are at least𝑣0(𝑞) and the damped bid stays above the platform’s bid. We use𝜂= 1in the first round
and𝜂= 0.25afterwards; bids are then an exponentially weighted average of the bidder’s past best
responses. This averaging is what makes the procedure a form of fictitious play, and it helps avoid
the cycling that undamped best responses can produce. The solver stops once no bid has moved by
more than10−3 for10consecutive rounds, or after100rounds. Note that starting from truthful bids
means the dynamics mostly shade down, so the solver finds equilibria reachable by lowering bids
from truthful bidding and may miss others.
Checks.The typical and adversarial runs share everything except the choice among best responses, so
an adversarial equilibrium should never have higher welfare than a typical one on the same market.
When it does, the solver has not settled, and we drop the market (for example, this removes at most
9%of markets in the filtering experiment of Section C.3). The check compares welfare over all of a
market’s prompts, not cluster by cluster. We also report the0.1percentile of welfare across markets
in place of the minimum, so that a few unsettled markets do not drive the results.
E. Proofs for competitive floors
In this section, we prove results for general mixed (randomized) equilibrias, representing each bid
as𝐵 𝑖 =𝑠 𝑖(𝑉𝑖,𝑍 𝑖)for private seeds𝑍 𝑖 that are independent across bidders and of the values.
Our first lemma establishes a lower bound on welfare anchored at an arbitrary threshold𝑐≥ 0.
Specifically, let𝑅=max 𝑖𝐵𝑖, which is the amount the winning bidder pays and is the revenue of
the platform. For any constant 𝑐≥ 0, we can bound welfare by the sum of𝔼[min{𝑅,𝑐}] and
(1− 1/𝑒)𝔼[(𝑉(1)−𝑐)+]. The first is the expected revenue, capped at𝑐. The second is a(1− 1/𝑒)-fraction
of the expected amount by which the top value (𝑉(1)) exceeds𝑐. When𝑐= 0, the first term is zero
and the lemma recovers the standard1−1/𝑒guarantee (Roughgarden et al., 2017).
Lemma E.1.For every constant𝑐≥0and any prior𝜇, everys∈BNE(𝜇)satisfies
𝔼[𝑊(s(V),V)]≥(1−1/𝑒)𝔼[(𝑉 (1)−𝑐)+]+𝔼[min{𝑅,𝑐}].(15)
Proof. Inequilibrium, nobiddercanincreaseitsexpectedutility(i.e., surplus)byaunilateraldeviation.
That is, for each𝑖 and each alternative strategy𝑠′ 𝑖, 𝔼[𝑈𝑖]≥𝔼[𝑈 ′ 𝑖], where𝑈𝑖 is bidder𝑖’s utility unders
and𝑈′ 𝑖 is its utility under(𝑠′ 𝑖, s−𝑖), i.e., when𝑖 alone switches to𝑠′ 𝑖 and its rivals keep playings. We
22

Price of Anarchy of First-Price Auctions in Agentic Markets
exploit this fact by constructing a deviation𝑠′ 𝑖 for each bidder and summing the resulting𝑛inequalities.
Each inequality is evaluated against the equilibrium rivals; the bidders do not deviate together.
The deviation𝑠′ 𝑖 is as follows. If𝑉𝑖≤𝑐 , bidder𝑖 bids zero. If𝑉𝑖 > 𝑐, it bids𝑏′ 𝑖 =𝑐+𝑇 𝑖, where𝑇𝑖 is drawn
independently of everything else with density
𝑓𝑖(𝑡)= 1 𝑉𝑖−𝑐−𝑡 ,0≤𝑡≤𝐿 𝑖 :=(1−1/𝑒)(𝑉 𝑖−𝑐).
This density integrates to one becauselog(𝑉𝑖−𝑐)/(𝑉 𝑖−𝑐−𝐿 𝑖) =log𝑒= 1. The deviation also never
exceeds𝑉 𝑖, so it is never over-bidding.
Let 𝑃𝑖 :=max 𝑗≠𝑖 𝐵𝑗 be the highest rival bid, where the𝐵𝑗 are the equilibrium bids. Condition on𝑉𝑖 =𝑣 𝑖
and 𝑃𝑖 =𝑝 𝑖. If𝑣𝑖 > 𝑐, the deviation wins when𝑇𝑖 > 𝑝𝑖−𝑐 , and then earns𝑣𝑖−𝑐−𝑇 𝑖. If𝑣𝑖≤𝑐 , the
deviation bids zero and its utility is zero. Integrating gives
𝔼[𝑈′ 𝑖|𝑉 𝑖 =𝑣 𝑖,𝑃 𝑖 =𝑝 𝑖]≥
∫ (1−1/𝑒)(𝑣 𝑖−𝑐)
(𝑝𝑖−𝑐)+
(𝑣𝑖−𝑐−𝑡)𝑓 𝑖(𝑡)𝑑𝑡
≥(1−1/𝑒)(𝑣 𝑖−𝑐)+−(𝑝 𝑖−𝑐)+.
The integral is read as zero when(𝑝𝑖−𝑐)+ >(1−1/𝑒)(𝑣 𝑖−𝑐).
Nowsumoverbidders. Let 𝑖∗ bea(measurablychosen)highest-valuebidder. Everytermisnonnegative
and𝑃 𝑖∗≤𝑅, so conditional on the values and rival bids,
∑︁
𝑖
𝔼[𝑈′ 𝑖|𝑉 𝑖,𝑃 𝑖]≥(1−1/𝑒)(𝑉 (1)−𝑐)+−(𝑃 𝑖∗−𝑐)+≥(1−1/𝑒)(𝑉 (1)−𝑐)+−(𝑅−𝑐) +.
Taking expectations and summing the equilibrium inequalities,
∑︁
𝑖
𝔼[𝑈𝑖]≥
∑︁
𝑖
𝔼[𝑈′ 𝑖]= ∑︁
𝑖
𝔼[𝔼[𝑈′ 𝑖|𝑉 𝑖,𝑃 𝑖]]≥(1−1/𝑒)𝔼[(𝑉 (1)−𝑐)+]−𝔼[(𝑅−𝑐) +].(16)
By definition,𝔼[𝑊]= ˝ 𝑖 𝔼[𝑈𝑖]+𝔼[𝑅]. Adding expected revenue𝔼[𝑅] to Equation (16) and using the
identity𝑅−(𝑅−𝑐) + =min{𝑅,𝑐}then proves the result.□
E.1. Deterministic competitive floor
WenowproveProposition2, startingwithalowerboundon 𝑅whencompetitionisdeterministic.
Lemma E.2.Let 𝜇 be a prior under which𝑉(2) ≥𝑐 almost surely for a constant𝑐≥ 0. Then every
Bayes–Nash equilibriums∈BNE(𝜇)satisfiesmax 𝑖𝐵𝑖≥𝑐almost surely.
Proof. Fix any Bayes–Nash equilibriums, and let𝑟min :=ess inf𝑅 be the largest constant such that
𝑅≥𝑟 min almost surely. Suppose𝑟min < 𝑐. As in Lemma E.1, write𝑈𝑖 for bidder𝑖’s utility undersand
𝑈′ 𝑖 for its utility under(𝑠′ 𝑖, s−𝑖). We now construct a unilateral deviation𝑠′ 𝑖 for each bidder such that
the gains 𝔼[𝑈′ 𝑖]−𝔼[𝑈 𝑖] sum to a strictly positive number. Then at least one gain is positive, which
contradicts the equilibrium conditions.
Choose a constant𝑏dev with𝑟min < 𝑏dev <(𝑐+𝑟 min)/2. Then ℙ(𝑅 < 𝑏dev)> 0by the definition of𝑟min,
and𝛿 :=𝑐+𝑟 min− 2𝑏dev > 0. Under𝑠′ 𝑖, bidder𝑖 bids max{𝐵𝑖,𝑏 dev} when𝑉𝑖≥𝑐 and keeps𝐵𝑖 otherwise.
Note that this deviation is admissible, as it uses only the bidder’s own value and equilibrium bid. It
also never overbids, since𝐵𝑖≤𝑉 𝑖, and the bid is raised only when𝑉𝑖≥𝑐 > 𝑏dev.
We compare𝑈′ 𝑖 with𝑈𝑖 for each bidder on each realized value profileV= vand equilibrium winning
bid 𝑅=𝑟 . When𝑟≥𝑏 dev, the deviation never lowers the bidder’s utility, so𝑈′ 𝑖≥𝑈 𝑖. When𝑟 < 𝑏dev, let
23

Price of Anarchy of First-Price Auctions in Agentic Markets
𝐴 :={𝑖 : 𝑣𝑖≥𝑐} be the index set of all bidders with value at least𝑐, which has at least two members by
assumption. Let𝑎𝑖 be bidder𝑖’s probability of winning in equilibrium under the tie rule givenV= v
and 𝑅=𝑟 , so˝ 𝑖∈𝐴 𝑎𝑖≤ 1. Each𝑖∈𝐴 that unilaterally deviates wins at price𝑏dev and earns𝑣𝑖−𝑏 dev,
compared with𝑎𝑖(𝑣𝑖−𝑟)in equilibrium. Summing these gains over𝐴,
∑︁
𝑖∈𝐴
𝔼[𝑈′ 𝑖−𝑈 𝑖|V=v,𝑅=𝑟]= ∑︁
𝑖∈𝐴

(𝑣𝑖−𝑏 dev)−𝑎 𝑖(𝑣𝑖−𝑟)

=
∑︁
𝑖∈𝐴

(1−𝑎 𝑖)𝑣𝑖+𝑎 𝑖𝑟−𝑏 dev

≥|𝐴|(𝑐−𝑏 dev)−(𝑐−𝑟)
≥𝑐+𝑟−2𝑏 dev
≥𝑐+𝑟 min−2𝑏 dev =𝛿 >0,
using 𝑟≥𝑟 min in the last step. Bidders outside𝐴 keep their equilibrium bids, so their gains are
zero. Let 𝐷 := ˝ 𝑖(𝑈′ 𝑖−𝑈 𝑖) be the total gain. We have shown𝔼[𝐷| V,𝑅]≥𝛿 on{𝑅 < 𝑏dev} and
𝔼[𝐷|V,𝑅]≥0otherwise, so
∑︁
𝑖
𝔼[𝑈′ 𝑖]−𝔼[𝑈 𝑖] =𝔼  𝔼[𝐷|V,𝑅]  ≥𝛿ℙ(𝑅 < 𝑏dev)>0.
Hence some bidder’s expected utility rises by deviating alone. This contradicts the equilibrium
conditions ofs, so𝑟 min≥𝑐, i.e.,𝑅≥𝑐almost surely.□
Proof of Proposition 2.Recall that𝑀 :=𝔼[𝑉 (1)]. Then set𝑐 :=𝛼𝑀 . Lemma E.2 gives𝑅≥𝑐 almost
surely, and the hypothesis also gives𝑉(1)≥𝑐almost surely. Therefore Lemma E.1 yields
𝔼[𝑊]≥(1−1/𝑒)(𝑀−𝑐)+𝑐=(1−1/𝑒)𝑀+𝑐/𝑒.
Divide by𝑀. □
E.2. Probabilistic competitive floor
We now prove Theorem 3. When the competitive floor can fail, the winning bid𝑅 can fall below𝑐, so
Lemma E.2 no longer applies. Instead, the next lemma bounds the expected shortfall𝔼[(𝑐−𝑅) +] when
at least𝑚 bidders clear𝑐 with probability at least1−𝜖. The deviation is the same as in Lemma E.2,
where each bidder with value at least𝑐 raises its bid to a constant𝑏dev. There, a single𝑏dev just above
𝑟min sufficed. Here the deviation can lose when fewer than𝑚 bidders clear𝑐, so we apply it at every
𝑏dev∈(0,𝑐)and obtain a differential inequality for𝔼[(𝑏 dev−𝑅)+].
Lemma E.3.Let 𝜇 be a prior under whichℙ(𝑉(𝑚)≥𝑐)≥ 1−𝜖 for a constant𝑐 >0, some2≤𝑚≤𝑛 ,
and𝜖∈[0,1]. Then every Bayes–Nash equilibriums∈BNE(𝜇)satisfies
𝔼[(𝑐−𝑅) +]
𝑐 ≤𝑆 𝑚(𝜖).
Proof of Lemma E.3.Fix any Bayes–Nash equilibriumsand a constant𝑏dev∈( 0,𝑐) . As before, write
𝑈𝑖 for bidder𝑖’s utility undersand 𝑈′ 𝑖 for its utility under(𝑠′ 𝑖, s−𝑖), where under𝑠′ 𝑖 bidder 𝑖 bids
max{𝐵𝑖,𝑏 dev} when𝑉𝑖≥𝑐 and keeps𝐵𝑖 otherwise. This deviation is admissible and never overbids, by
the same argument as in Lemma E.2. Let𝐷 := ˝ 𝑖(𝑈′ 𝑖−𝑈 𝑖) be the total gain. In equilibrium,𝔼[𝐷]≤ 0.
We lower bound𝔼[𝐷| V = v,𝑅=𝑟] on each realization, as in Lemma E.2. Let𝐴 :={𝑖 : 𝑣𝑖≥𝑐} and
𝑎𝑖 be bidder𝑖’s probability of winning in equilibrium under the tie rule givenV= vand 𝑅=𝑟 , so
24

Price of Anarchy of First-Price Auctions in Agentic Markets
˝
𝑖∈𝐴 𝑎𝑖≤ 1. When𝑟≥𝑏 dev, the deviation never lowers any bidder’s utility, so the conditional gain is
nonnegative. When𝑟 < 𝑏dev, the same computation as in Lemma E.2 gives
𝔼[𝐷|V=v,𝑅=𝑟]=
∑︁
𝑖∈𝐴

(𝑣𝑖−𝑏 dev)−𝑎 𝑖(𝑣𝑖−𝑟)

≥|𝐴|(𝑐−𝑏 dev)−(𝑐−𝑟)
=(|𝐴|−1)(𝑐−𝑏 dev)−(𝑏 dev−𝑟).
Let 𝐺 :={𝑉(𝑚)≥𝑐} , soℙ(𝐺𝑐)≤𝜖 . On𝐺 and{𝑅 < 𝑏dev} we have|𝐴|≥𝑚 , so the conditional gain is at
least(𝑚− 1)(𝑐−𝑏 dev)−(𝑏 dev−𝑅) . On𝐺𝑐 and{𝑅 < 𝑏dev}, it is at least−(𝑏 dev−𝑅) , since|𝐴|≥ 1gives
this from the display above and|𝐴|= 0gives zero gain, as there is no deviation. Finally, as mentioned
above, on{𝑅≥𝑏 dev}the gain is non-negative. The three conditional bounds combine into
𝔼[𝐷|V,𝑅]≥(𝑚−1)(𝑐−𝑏 dev)1{𝑅 < 𝑏dev}1𝐺−(𝑏 dev−𝑅)+.
Let 𝐹(𝑏) :=ℙ(𝑅 < 𝑏), 𝑄(𝑏) :=ℙ({𝑅 < 𝑏}∩𝐺 𝑐)≤ℙ(𝐺 𝑐)≤𝜖 , and𝐻(𝑏) :=𝔼[(𝑏−𝑅) +]= ∫ 𝑏 0 𝐹(𝑡)𝑑𝑡 ,
where 𝑅≥ 0by no overbidding, so𝐻( 0)= 0, 𝐻′ =𝐹 almost everywhere, and𝐻(𝑐)=𝔼[(𝑐−𝑅) +].
Taking expectations and usingℙ({𝑅 < 𝑏dev}∩𝐺)=𝐹(𝑏 dev)−𝑄(𝑏 dev)gives
0≥𝔼[𝐷]≥(𝑚−1)(𝑐−𝑏 dev)

𝐹(𝑏 dev)−𝑄(𝑏 dev)

−𝐻(𝑏 dev).
Since𝑏 dev∈(0,𝑐)was arbitrary and𝑄≤𝜖, this gives
𝐻′(𝑏)≤𝜖+ 𝐻(𝑏) (𝑚−1)(𝑐−𝑏) for almost every𝑏∈(0,𝑐), 𝐻(0)=0.
Multiplying by(𝑐−𝑏) 1/(𝑚−1) and integrating gives
𝐻(𝑏)≤ (𝑚−1)𝜖 𝑚 h 𝑐𝑚/(𝑚−1)(𝑐−𝑏) −1/(𝑚−1) −(𝑐−𝑏) i .
Also,𝐹≤1implies𝐻(𝑐)≤𝐻(𝑏)+𝑐−𝑏. Setting𝑧:=(𝑐−𝑏)/𝑐, we obtain
𝔼[(𝑐−𝑅) +]
𝑐 = 𝐻(𝑐) 𝑐 ≤(𝑚−1)𝜖 𝑚 𝑧−1/(𝑚−1) +  1− (𝑚−1)𝜖 𝑚  𝑧,0< 𝑧≤1.
For0< 𝜖 <1, this expression is minimized at
𝑧∗ =
h 𝜖
𝑚−(𝑚−1)𝜖
i(𝑚−1)/𝑚
∈(0,1],
and substitution gives𝔼[(𝑐−𝑅) +]/𝑐≤

𝜖𝑚−1(𝑚−(𝑚− 1)𝜖)  1/𝑚 =𝑆 𝑚(𝜖). When𝜖= 0, the integrated
inequality gives𝐻(𝑏)= 0for every 𝑏 < 𝑐, and continuity gives𝐻(𝑐)= 0. When 𝜖= 1, the bound
follows from(𝑐−𝑅) +≤𝑐.□
Proof of Remark 4.Note that the properties in Remark 4 follow from the closed form𝐼𝜖(𝑚− 1, 2)=
𝜖𝑚−1(𝑚−(𝑚− 1)𝜖). It equals0at 𝜖= 0and1at 𝜖= 1. Using𝑚−(𝑚− 1)𝜖≤𝑚 gives the simple
bound. Finally, for𝜖∈ (0, 1), write 𝑢 :=( 1−𝜖)/𝜖 . Then 𝜖𝑚−1(𝑚−(𝑚− 1)𝜖)=𝜖 𝑚(1+𝑢𝑚) , so
𝑆𝑚(𝜖)=𝜖( 1+𝑢𝑚) 1/𝑚. The factor(1+𝑢𝑚) 1/𝑚 decreases strictly in𝑚, becauselog(1+𝑥)> 𝑥/( 1+𝑥)
for𝑥 >0, and tends to1as𝑚→∞. Hence𝑆 𝑚(𝜖)decreases strictly to𝜖.□
Proof of Theorem 3.Set 𝑐 :=𝛼𝑀 . If 𝛼= 0or 𝑆𝑚(𝜖) ≥1/𝑒, Lemma E.1 with𝑐= 0gives 𝔼[𝑊] ≥
(1−1/𝑒)𝑀, which is the claim. Otherwise𝑐 >0, and Lemma E.3 gives
𝔼[min{𝑅,𝑐}]=𝑐−𝔼[(𝑐−𝑅) +]≥𝑐
1−𝑆 𝑚(𝜖) .
Since𝔼[(𝑉 (1)−𝑐)+]≥𝑀−𝑐, Lemma E.1 gives
𝔼[𝑊]≥(1−1/𝑒)(𝑀−𝑐)+𝑐
1−𝑆 𝑚(𝜖) =(1−1/𝑒)𝑀+𝛼𝑀 1/𝑒−𝑆 𝑚(𝜖) .
Divide by𝑀. □
25

Price of Anarchy of First-Price Auctions in Agentic Markets
E.3. Welfare with a committed platform bidder
We prove Equation (9) for a platform model that publicly announces its value𝑉0 =𝑣 0(𝑋) and commits
to bidding it. The other bidders play a no-overbidding Bayes–Nash equilibrium of the induced auction.
Write𝑉(1) =max{𝑉 0,𝑉 1,...,𝑉 𝑛}.
Proof. Fix 𝑋=𝑥 and write𝑣0 =𝑣 0(𝑥). Since the platform bids𝑣0, the winning bid satisfies𝑅≥𝑣 0.
Run the argument of Lemma E.1 under the conditional law given𝑋=𝑥 with 𝑐=𝑣 0, using deviations
only for the strategic bidders; these deviations may depend on𝑥 because 𝑥 is public. On profiles
where a strategic bidder has the top value, the argument is unchanged, since the highest rival bid is
still at most𝑅. On profiles where the platform has the top value,(𝑉(1)−𝑐)+ = 0, and the required
inequality holds because deviation utilities are nonnegative. The platform’s utility is always zero, so
welfare still equals total bidder utility plus revenue. Hence, using𝑉(1)≥𝑣 0 and𝑅≥𝑣 0,
𝔼[𝑊|𝑋=𝑥]≥(1−1/𝑒) 𝔼[𝑉(1)|𝑋=𝑥]−𝑣 0 +𝑣 0 =(1−1/𝑒)𝔼[𝑉 (1)|𝑋=𝑥]+ 1 𝑒 𝑣0.
Taking expectations over𝑋and dividing by𝔼[𝑉(1)]gives Equation (9).□
F. Proofs and additional results for weak dependence
We prove the qualitative Theorem 5 by comparing an equilibrium under the conditional joint distribu-
tion𝜇𝑥 with the same strategies under the product of its marginals,𝜈𝑥. Changing the distribution
mildly can destroy exact optimality, but it creates only small regret. The main step is to show that
small regret under independence also leaves only a small shortfall from the Jin–Lu welfare guarantee.
We then transfer this bound back to𝜇𝑥. Before moving to the proof of the weak dependence result
(Theorem 5), we first record the simpler robustness argument for the1− 1/𝑒 guarantee, which allows
arbitrary correlation (Roughgarden et al., 2017).
F.1. Warmup: Robustness of the1− 1 𝑒  bound
Fix a public state𝑋=𝑥 and a value distribution𝜆. Suppose no bidder can improve its ex ante expected
utility by more than𝑟 through a unilateral change of strategy. The proof of Lemma E.1 with𝑐= 0
gives
𝔼𝜆[𝑊]≥(1−1/𝑒)𝔼 𝜆[𝑉(1)]−𝑛𝑟.
Each of the𝑛 best-response inequalities incurs at most𝑟; summing them and adding revenue proves
the bound. The deviations depend only on each bidder’s own value, so the argument allows arbitrary
correlation (Roughgarden et al., 2017, Definition 4.5, Eq. (18), and Theorem 4.6). At exact equi-
librium, the1− 1/𝑒 guarantee therefore holds under every joint distribution. The sharper1− 1/𝑒2
guarantee requires a separate argument exploiting independence.
F.2. Proof overview
The proof of Theorem 5 has three steps. First, an equilibrium under𝜇𝑥 has regret at most2¯𝑣(𝑥)𝜏(𝑥)
when evaluated under 𝜈𝑥. Second, Proposition F.1 shows that, for a fixed number of bidders,
independent-values auctions with vanishing regret cannot retain a positive welfare shortfall be-
low the Jin–Lu guarantee. In its proof, Lemma F.2 takes a convergent subsequence of auctions and
recovers an exact equilibrium with the same limiting welfare. Finally, using Lemma F.3 we transfer
welfare and optimal welfare from𝜈𝑥 back to𝜇𝑥. Ties require care in the second step because the
winning bidder need not be determined by the limiting bids alone.
F.3. Welfare shortfall under small regret
Write𝑐 JL :=1−1/𝑒 2. For a value distribution𝜈, define bidder𝑖’s ex ante regret by
Reg𝜈 𝑖(𝑠):=sup
b𝑠𝑖
𝔼𝜈[𝑢𝑖(𝑉𝑖,b𝑠𝑖(𝑉𝑖),𝑠−𝑖(𝑉−𝑖))−𝑢 𝑖(𝑉𝑖,𝑠 𝑖(𝑉𝑖),𝑠−𝑖(𝑉−𝑖))].
26

Price of Anarchy of First-Price Auctions in Agentic Markets
Here𝑢𝑖 is value minus bid on winning and zero otherwise. The alternative strategy may choose a
different bid for each own value and may be mixed, but never overbids. Regret measures the average
gain available from such a change, with rivals’ strategies held fixed.
For values in[0, 1], let𝛿𝑛(𝑟) be the supremum additive shortfall below the Jin–Lu guarantee among
independent-values auctions with each bidder’s regret at most𝑟:
𝛿𝑛(𝑟):=sup
𝜈,𝑠∈S𝜈(𝑟),𝜋

𝑐JL𝔼𝜈[𝑉(1)]−𝔼 𝜈[𝑊(𝑠)]

+.
The supremum ranges over product distributions on[0, 1]𝑛, mixed no-overbidding profiles satisfying
max𝑖 Reg𝜈 𝑖(𝑠)≤𝑟 , and announced measurable bid-only tie rules𝜋, possibly randomized. All utilities
are evaluated using the auction’s announced tie rule.
Proposition F.1.For each fixed𝑛≥2,𝛿 𝑛 is nondecreasing,0≤𝛿 𝑛(𝑟)≤1, and𝛿 𝑛(0)=0. Moreover,
𝛿𝑛(𝑟)−→0as𝑟↓0.(17)
Thus sufficiently small regret guarantees a small welfare shortfall uniformly over all the auctions in
the definition. For Theorem 5, set
𝜂cont 𝑛 (𝑡):=(1+𝑐 JL)𝑡+𝛿 𝑛(2𝑡).(18)
The term𝛿𝑛(2𝑡) accounts for the regret created by changing the distribution;(1+𝑐 JL)𝑡 accounts for
the two welfare expectations. The proposition implies that𝜂cont 𝑛 is nondecreasing,𝜂cont 𝑛 (0)= 0, and
𝜂cont 𝑛 (𝑡)→0as𝑡↓0.
F.3.1. Proof of Proposition F.1
For a high-level overview of the proof, suppose small regret could coexist with a fixed positive
welfare shortfall. Choose a sequence of such independent-values auctions with regret tending to zero.
Compactness gives limiting value–bid distributions, and recording the winner preserves the limiting
utilities and welfare. Lemma F.2 ensures that feasible deviations still attain nearly the best limiting
utility. Lemma F.3 then shows that the limit can be represented as an exact equilibrium, including a
bid-only rule for newly formed ties. The positive shortfall would contradict the Jin–Lu bound.
Let⇒ denote weak convergence of probability measures. A bid just above𝑡 beats all rivals bidding at
most𝑡, regardless of how ties are resolved. We can choose such bids away from atoms of the limiting
rival distributions, where winning probabilities converge. A finite partition of the value interval makes
these choices into one measurable deviation that never overbids. This is encapsulated in the following
Lemma about approximating limiting deviation utility.
Lemma F.2.Fix bidder 𝑖. Suppose𝐹𝑘⇒𝐹 are its value distributions on[0, 1] and 𝐻𝑘 𝑗 ⇒𝐻 𝑗 are its
rivals’ bid distributions. In each auction, the value and rival bids are mutually independent. Let𝑦𝑘 𝑖(𝑡) be
its winning probability from bidding𝑡under that auction’s announced bid-only tie rule, and put
𝐺𝑖(𝑡):=
Ö
𝑗≠𝑖
𝐻𝑗(𝑡), 𝑀 𝑖(𝑣):=sup
0≤𝑡≤𝑣
(𝑣−𝑡)𝐺 𝑖(𝑡).
For every𝜖 >0, there is a measurable deviation0≤𝑑(𝑣)≤𝑣, the same for every𝑘, such that
lim inf
𝑘→∞
∫
(𝑣−𝑑(𝑣))𝑦 𝑘 𝑖(𝑑(𝑣))𝑑𝐹 𝑘(𝑣)≥
∫
𝑀𝑖(𝑣)𝑑𝐹(𝑣)−𝜀.(19)
27

Price of Anarchy of First-Price Auctions in Agentic Markets
Proof. For0≤𝑤≤𝑣 , bids𝑡≤𝑤 increase utility by at most𝑣−𝑤 , while bids𝑤 < 𝑡≤𝑣 yield at most
𝑣−𝑤. Hence0≤𝑀 𝑖(𝑣)−𝑀 𝑖(𝑤)≤𝑣−𝑤, and𝑀 𝑖(0)=0. Choose a partition
0=𝑎 0 < 𝑎1 <···< 𝑎 𝑚 =1
with mesh at most𝜁, where every interior endpoint is a continuity point of𝐹. Such a partition exists
because𝐹has only countably many atoms.
Fix ℓ≥ 2. The union of the atoms of the finitely many limiting rival bid distributions𝐻𝑗 is countable.
Right continuity permits us to choose𝑡ℓ < 𝑎ℓ−1 outside that union such that
(𝑎ℓ−1−𝑡 ℓ)𝐺𝑖(𝑡ℓ)≥𝑀 𝑖(𝑎ℓ−1)−𝜁.(20)
If 𝑀𝑖(𝑎ℓ−1)> 𝜁 , choose a nearly optimal bid strictly below𝑎ℓ−1 and move it slightly upward to a
common continuity point of the𝐻𝑗, still below𝑎ℓ−1. Right continuity gives the desired approximation.
If𝑀 𝑖(𝑎ℓ−1)≤𝜁, any such continuity point in[0,𝑎 ℓ−1)suffices because its utility is nonnegative.
Define𝑑(𝑣)= 0on [0,𝑎 1] and𝑑(𝑣)=𝑡 ℓ on(𝑎ℓ−1,𝑎 ℓ]. Values at partition endpoints may be assigned
to either adjacent interval. This deviation never overbids. A bid𝑡ℓ wins whenever every rival bid is
strictly below it, regardless of the tie rule, so
𝑦𝑘 𝑖(𝑡ℓ)≥ Ö
𝑗≠𝑖
𝐻𝑘 𝑗(𝑡ℓ−).
For a distribution function𝐻, write𝐻(𝑡−) :=lim 𝑧↑𝑡 𝐻(𝑧) . At each selected𝑡ℓ, weak convergence gives
𝐻𝑘 𝑗(𝑡ℓ−)→𝐻 𝑗(𝑡ℓ). Each partition interval has value-atom-free interior boundaries, so its weighted
integral also converges under𝐹𝑘⇒𝐹 . The endpoint1is a boundary of the underlying space[0, 1], so
an atom there causes no problem.
For𝑣∈(𝑎 ℓ−1,𝑎 ℓ], Equation (20) and the Lipschitz property imply
(𝑣−𝑡 ℓ)𝐺𝑖(𝑡ℓ)≥𝑀 𝑖(𝑣)−2𝜁.
On the first interval,0≤𝑀 𝑖(𝑣)≤𝜁 , while the zero bid has nonnegative utility. The left side of(19) is
therefore at least
∫
𝑀𝑖𝑑𝐹−3𝜁. Choose𝜁 < 𝜀/3.□
Lemma F.3.Fix 𝑛. Consider a sequence of independent-values first-price auctions on[0, 1]𝑛. In auction
𝑘, let𝑠𝑘 be a mixed no-overbidding profile, let𝜋𝑘 be a publicly announced randomized bid-only tie rule,
and suppose
max
𝑖
Reg𝜈𝑘 𝑖 (𝑠𝑘)−→0.
There are a subsequence, an independent prior𝜈, a mixed no-overbidding profile𝑠, and a publicly
announced randomized bid-only tie rule𝜋such that𝑠∈BNE(𝜈)and, along the subsequence,
𝔼𝜈𝑘[𝑉(1)]−→𝔼 𝜈[𝑉(1)],𝔼 𝜈𝑘[𝑊(𝑠𝑘)]−→𝔼 𝜈[𝑊(𝑠)].(21)
For the limit of the auction itself, we keep each bidder’s joint distribution of value and bid, rather
than take pointwise limits of bidding functions. These distributions lie in the compact set{(𝑣,𝑏) :
0≤𝑏≤𝑣≤ 1}. We also record the winner, so utility and welfare pass to the limit even if distinct
bids become tied. The remaining issue is to realize that limiting outcome with a rule depending
only on bids. We will show that vanishing regret forces any bidder tied at the top with positive
surplus to win. Independence then implies that at most one bidder can require this priority at each
positive-probability tie level. This allows a bid-only rule that preserves welfare.
28

Price of Anarchy of First-Price Auctions in Agentic Markets
Proof. Let 𝐷 :={(𝑣,𝑏)∈[ 0, 1]2 : 0≤𝑏≤𝑣}. For bidder𝑖 in auction𝑘, let𝑞𝑘 𝑖 be the distribution of
(𝑉𝑘 𝑖 ,𝐵 𝑘 𝑖) on 𝐷. Independence of values and private randomizations implies that the distribution of
all value–bid pairs is𝑞𝑘 := ∯ 𝑖𝑞𝑘 𝑖. Probability measures on the compact metric space𝐷 are weakly
compact. After taking a common subsequence,
𝑞𝑘 𝑖⇒𝑞 𝑖, 𝑞 𝑘⇒𝑞:= Ì
𝑖
𝑞𝑖.(22)
Write𝐹𝑖 and 𝐻𝑖 for the value and bid marginals of𝑞𝑖. Disintegrate𝑞𝑖(𝑑𝑣,𝑑𝑏)=𝐹 𝑖(𝑑𝑣)𝑠 𝑖(𝑑𝑏|𝑣) . The
product of the value marginals is the limiting independent prior𝜈 := ∯ 𝑖𝐹𝑖, and closedness of𝐷
preserves no overbidding.
Let 𝐼𝑘∈[𝑛] be the winner, including the randomization in𝜋𝑘, and let𝜆𝑘 be the distribution of all
value–bid pairs together with𝐼𝑘. Pass to a further subsequence for which𝜆𝑘⇒𝜆 . Its marginal on𝐷𝑛
is𝑞, and
𝜆{𝑏𝐼 =max 𝑗 𝑏𝑗}=1,(23)
because the displayed event is closed. With[𝑛]carrying the discrete topology, the functions
(𝑣,𝑏,𝐼)↦−→(𝑣 𝑖−𝑏 𝑖)1{𝐼=𝑖},(𝑣,𝑏,𝐼)↦−→𝑣 𝐼
are continuous. Hence, writing
𝑈∗ 𝑖 :=
∫
(𝑣𝑖−𝑏 𝑖)1{𝐼=𝑖} 𝑑𝜆, 𝑊 ∗ :=
∫
𝑣𝐼𝑑𝜆,
the utilities converge to𝑈∗ 𝑖 and auction welfare converges to𝑊∗. Also,
𝔼𝜈𝑘[𝑉(1)]−→
∫
max
𝑖
𝑣𝑖𝑑𝑞=𝔼 𝜈[𝑉(1)],(24)
because the maximum is continuous.
For the limiting bid marginals, put
𝐺𝑖(𝑡):=
Ö
𝑗≠𝑖
𝐻𝑗(𝑡), 𝑀 𝑖(𝑣):=sup
0≤𝑡≤𝑣
(𝑣−𝑡)𝐺 𝑖(𝑡).
Apply Lemma F.2 to bidder𝑖. For every𝜖 > 0, the regret inequality in auction𝑘, followed by the
lemma and vanishing regret, gives
𝑈∗ 𝑖≥
∫
𝑀𝑖(𝑣)𝑑𝐹 𝑖(𝑣).(25)
There is a matching upper bound that uses only feasibility of the limiting winner. On the event𝐼=𝑖 ,
every rival bid is at most𝑏𝑖. Since𝑣𝑖−𝑏 𝑖≥0and𝜆has marginal𝑞,
𝑈∗ 𝑖≤
∫
(𝑣𝑖−𝑏 𝑖)1{𝑏𝑗≤𝑏𝑖∀𝑗≠𝑖} 𝑑𝑞
=
∫
(𝑣−𝑏)𝐺 𝑖(𝑏)𝑑𝑞 𝑖(𝑣,𝑏)≤
∫
𝑀𝑖(𝑣)𝑑𝐹 𝑖(𝑣).(26)
Every inequality in (25)– (26) is therefore an equality. In particular,
(𝑣−𝑏)𝐺 𝑖(𝑏)=𝑀 𝑖(𝑣)for𝑞 𝑖-almost every(𝑣,𝑏),(27)
29

Price of Anarchy of First-Price Auctions in Agentic Markets
and
(𝑣𝑖−𝑏 𝑖)

1{𝑏𝑗≤𝑏𝑖∀𝑗≠𝑖}−1{𝐼=𝑖}

=0𝜆-almost surely.(28)
Thus, whenever bidder𝑖 has a highest bid and𝑉𝑖 > 𝐵𝑖, the limiting outcome must select𝑖, and that
ff it lost with positive probability, bidding just above the tie would improve its utility, contrary to
vanishing regret.
We now construct an ordinary bid-only tie rule. A positive-probability tie at a level𝑡 under a product
bid distribution requires at least two bid marginals to have atoms at𝑡; there are only countably many
such levels. At any level that can be the top bid with positive probability, at most one bidder𝑖 can
satisfy
𝑞𝑖{𝐵𝑖 =𝑡, 𝑉𝑖 > 𝑡}>0.(29)
Otherwise two such bidders𝑖 and 𝑗, and the positive-probability event that all remaining bids are at
most𝑡, wouldwithpositiveprobabilitybothtieatthetopandbothhavepositivesurplus. Equation (28)
would require both𝐼=𝑖and𝐼=𝑗, an impossibility.
At any level𝑡 that can be the top bid with positive probability, call the unique bidder in(29), if it
exists,ℎ(𝑡). At a tie for the highest bid𝑡, let the new rule𝜋 award the item toℎ(𝑡) if that bidder is
among those tied; otherwise award it to the lowest-index tied bidder. Away from ties, award it to the
unique highest bidder. The exceptional levels are countable, so this is a Borel bid-only rule.
This repair preserves welfare. At a top tie, every tied bidder other thanℎ(𝑡) has value exactly𝑡 almost
surely. Ifℎ(𝑡) is tied and has value above𝑡, Equation(28) says that𝜆 already selectsℎ(𝑡). In every
remaining case all tied bidders have value𝑡. Consequently,
𝔼𝜈[𝑊(𝑠)]=𝑊 ∗.(30)
Finally, under𝜋, a bidder with a bid𝑏 and positive surplus wins every positive-probability tie at𝑏.
Its interim allocation is therefore𝐺𝑖(𝑏)for𝑞 𝑖-almost every(𝑣,𝑏)with𝑣 > 𝑏. When𝑣=𝑏, its payoff is
zero and(27) gives 𝑀𝑖(𝑣)= 0. Thus the on-path expected utility of almost every type𝑣 is 𝑀𝑖(𝑣). Any
deviation to𝑡has interim allocation at most𝐺𝑖(𝑡)and utility at most
(𝑣−𝑡) +𝐺𝑖(𝑡)≤𝑀 𝑖(𝑣).
The same holds for mixed deviations. Therefore𝑠∈BNE(𝜈) under𝜋. Equations(24) and (30) give
(21). □
The argument is uniform over the auctions in the definition, but gives no explicit rate and does not
require equilibrium strategies to vary continuously with the value distribution.
With all the ingredients in place, we can finally state the main proof of this section.
Proof of Proposition F.1
Proof. Monotonicity and0≤𝛿 𝑛(𝑟)≤ 1are immediate, and the Jin–Lu theorem gives𝛿𝑛(0)= 0. If
𝛿𝑛(𝑟)̸→ 0, choose𝜖 > 0and 𝑟𝑘↓ 0with 𝛿𝑛(𝑟𝑘)> 2𝜖. By the definition of the supremum, there are
auctions with maximal regret at most𝑟𝑘 and welfare shortfall at least𝜖.
𝑐JL𝔼[𝑉(1)]−𝔼[𝑊]≥𝜀.
Lemma F.3 produces an exact mixed Bayes–Nash equilibrium of an independent-values first-price
auction to which both welfare terms converge. The limiting defect remains at least𝜀, contrary to the
Jin–Lu bound. Hence (17) holds.□
30

Price of Anarchy of First-Price Auctions in Agentic Markets
F.4. Proof of the main qualitative theorem (Theorem 5).
Proof of Theorem 5.Fix a public state𝑥 where the hypotheses hold, and abbreviate𝜇 :=𝜇 𝑥,𝜈 :=𝜈 𝑥,
𝜏 :=𝜏(𝑥) , and ¯𝑣:=¯𝑣(𝑥). If ¯𝑣= 0, the claim is immediate. Otherwise evaluate the equilibrium
strategies under𝜈 without changing them. The own-value marginals are unchanged, so the same
no-overbidding deviations remain available.
For any fixed deviation, its utility and the utility lie in[0,¯𝑣]. Changing the value distribution by TV
distance𝜏changes each expectation by at most¯𝑣𝜏. Equilibrium under𝜇therefore implies
max
𝑖
Reg𝜈 𝑖(𝑠)≤2¯𝑣𝜏.
After dividing values and bids by¯𝑣, Proposition F.1 gives
𝔼𝜈[𝑊]≥𝑐 JL𝔼𝜈[𝑉(1)]−¯𝑣𝛿𝑛(2𝜏).
Since𝑊,𝑉 (1)∈[0,¯𝑣], transferring both expectations back to𝜇yields
𝔼𝜇[𝑊]≥𝔼 𝜈[𝑊]−¯𝑣𝜏
≥𝑐 JL𝔼𝜇[𝑉(1)]−¯𝑣

𝛿𝑛(2𝜏)+(1+𝑐 JL)𝜏

.
This proves(7) with the error𝜂cont 𝑛 as defined in(18). Applying the argument for almost every public
state proves the theorem.□
F.5. A quantitative bound for weakly-dependent values
Theorem 5 gives qualitative stability for arbitrary bounded value distributions. Under additional
regularity of the conditional value distribution, its error can be bounded linearly in the total variation
distance from independence. The marginals may differ, and the result applies to every no-overbidding
Bayes–Nash equilibrium, including mixed equilibria.
Fix𝑛≥ 2and a public state, and normalize the value bound to one. Let𝐹𝑖 be the marginal distribution
of𝑉𝑖, put𝜈= ∯ 𝑖𝐹𝑖, and write𝑟=𝑑𝜇/𝑑𝜈 and 𝜀=∥𝑟− 1∥∞. Assume that each𝐹𝑖 has a continuous
density on[0,1]and that
0< ℓ≤𝑓 𝑖(𝑣)≤𝑢 <∞, 𝑟∈𝐶 1([0,1] 𝑛),(31)
max
𝑖
∥𝜕𝑖𝑟∥∞≤𝐿𝜀,0≤𝜀≤ 1 4𝐿+1 , 𝐿≥1.(32)
The derivative bound scales with the departure from independence. It prevents𝑟− 1from being
confined to an arbitrarily small region; at the end of the proof, this allows us to bound𝜖 by a constant
times𝜏. No derivative bounds on the marginal densities are needed.
Theorem F.4(A quantitative refinement of Theorem 5).Under(31)–(32), there is a constant𝐶=
𝐶(𝑛,ℓ,𝑢,𝐿) , given explicitly at theend of theproof, such that every no-overbidding Bayes–Nash equilibrium
satisfies
𝔼𝜇[𝑊]≥𝑐 JL𝔼𝜇[𝑉(1)]−𝐶𝜏, 𝜏:=∥𝜇−𝜈∥ TV.
For the public-state setting of Theorem 5, suppose the conditional distributions of(𝑉𝑖/¯𝑣(𝑥))𝑛 𝑖=1 satisfy
these assumptions whenever¯𝑣(𝑥)> 0, withℓ,𝑢,𝐿 uniform in𝑥. Rescaling does not change total
variation, so for almost every𝑥,
𝔼[𝑊|𝑋=𝑥]≥𝑐 JL𝔼[𝑉(1)|𝑋=𝑥]−¯𝑣(𝑥)𝐶𝜏(𝑥).
31

Price of Anarchy of First-Price Auctions in Agentic Markets
The case¯𝑣(𝑥)=0is immediate. If𝔼[¯𝑣(𝑋)]<∞, averaging gives
𝔼[𝑊]≥𝑐 JL𝔼[𝑉(1)]−𝐶𝔼[¯𝑣(𝑋)𝜏(𝑋)].
The proof first derives regularity of equilibrium bids, then constructs a nearby exact equilibrium with
independent values. We transfer the Jin–Lu welfare guarantee from this equilibrium and express the
error in terms of total variation.
Conditional probabilities.Put
𝜌= 1+𝜀 1−𝜀 ≤ 3 2, 𝜅= 𝐿𝜀 1−𝜀 ≤ 1 4.
Since 𝐹𝑖 is the actual marginal of𝜇,
∫
𝑟(𝑣,𝑣−𝑖)𝑑𝜈−𝑖(𝑣−𝑖)= 1, differentiating its explicit integral
representation is legitimate under the𝐶1 assumption. Thus every nonnegative function𝑘 of rival
values and private random seeds satisfies, for almost every𝑣
(1−𝜀)𝔼 𝜈[𝑘]≤𝔼 𝜇[𝑘|𝑉 𝑖 =𝑣]≤(1+𝜀)𝔼 𝜈[𝑘].(33)
If 𝑘 is fixed as𝑣 varies and this expectation is positive, its logarithmic derivative has absolute value at
most𝜅: the derivative is a weighted average of𝜕𝑖 log𝑟.
F.5.1. Proof Overview
Lemma F.5 first shows that higher values lead to higher bids and that no single bid amount has
positive probability. Lemma F.6 then bounds the value associated with each bid and the surplus
retained by the bidder. These bounds allow Lemma F.7 to compare how raising a bid changes the
chance of winning under the dependent prior and under independence. Lemma F.8 uses these facts
to construct a nearby equlibrium with independent values in three steps. First, it determines the
required changes in the bidder’ bid distributions jointly, accounting for intervals in which a bidder
originally places no bids. Second, it bounds the size of these changes using the preceding optimality
comparisons. Third, it proves that the constructed bids are globally optimal for their assigned values
and controls the resulting change in bid distributions in total variation. In the proof of Theorem F.4,
we apply the Jin–Lu guarantee to this equilibrium and transfer the welfare bound back to the original
auction. Finally, the derivative assumption bounds the uniform departure from independence by a
constant times the total variation distance, giving the claimed linear error.
F.5.2. Proof of Theorem F.4
We state and prove four auxiliary lemmas that will be used for a proof of theorem F.4.
Lemma F.5.Under the stated prior assumptions, every equilibrium has atomless marginal bid distribu-
tions and is outcome-equivalent to a profile of pure nondecreasing strategies, up to null sets of values. Let
𝐻𝑖 be its marginal bid CDF, for0≤𝑏≤𝛽, define
𝑣𝑖(𝑏):=𝐹 −1 𝑖 (𝐻𝑖(𝑏)), 𝐾 𝑖 :=supp(𝑑𝐻 𝑖), 𝛽:=max 𝑖 sup𝐾 𝑖.(34)
Then 𝑣𝑖 is continuous and nondecreasing,𝑉𝑖 =𝑣 𝑖(𝐵𝑖) almost surely, and𝐻𝑖(𝑏)≥𝐹 𝑖(𝑏)> 0for 𝑏 >0. The
union of the𝐾𝑖 is[0,𝛽] , and every𝑏∈( 0,𝛽) belongs to at least two of them. For𝑏∈𝐾 𝑖, 𝑏 is a best
response for the cutoff type𝑣𝑖(𝑏), including support endpoints interpreted by continuity.
Individual supports may have gaps or end below𝛽. Accordingly, we use a bidder’s first-order condition
only on its support in𝐾𝑖.
32

Price of Anarchy of First-Price Auctions in Agentic Markets
Proof. Positive utility and atoms.A type𝑣 >0can bid 𝑣/2and win whenever all rival values are below
𝑣/2. No overbidding and (33) imply
𝑈𝑖(𝑣)≥(1−𝜀)ℓ 𝑛−1𝑣𝑛/2𝑛 >0.(35)
Consequently, every sampled equilibrium bid of a positive type has positive surplus. Suppose two or
more bidders have atoms at the same positive bid𝑡. The event that both bid𝑡 and all other values
are below𝑡 has positive probability. For each bidder with such an atom, consider the unilateral
deviation that raises𝑡 to𝑡+𝜂 whenever𝑣 > 𝑡+𝜂. As𝜂↓ 0, the sum of these deviations’ gains has a
strictly positive limit on this top-tie event and a nonnegative limit elsewhere. Bounded convergence
contradicts the equilibrium inequalities.
If every bidder has an atom at zero, the same argument applies to the all-zero tie: all values are
positive almost surely, and raising a zero bid breaks the tie at a vanishing cost. If some bidder has no
zero atom, any other bidder’s zero bid wins with probability zero, contrary to(35). Hence there are
no atoms at zero.
Suppose only bidder𝑖has an atom at a positive bid𝑡. Put
𝑢0 =(1−𝜀)ℓ 𝑛−1(𝑡/4)𝑛, 𝑝 0 =(1−𝜀)Pr(𝐵 𝑖 =𝑡)(ℓ𝑡/2) 𝑛−2 >0.
Choose0 < 𝛿 < 𝑡/2and 𝜂 >0so that 𝛿+𝜂 < 𝑝0𝑢0/4. Any rival equilibrium bid in(𝑡−𝛿,𝑡) has value
at least𝑡/2and surplus at least𝑢0, by the half-value deviation. Raising it to𝑡+𝜂 is therefore feasible.
Conditional on the rival’s own value, the event that𝑖 bids𝑡 and all remaining bidders have values
below𝑡/2has probability at least𝑝0. The deviation gains at least𝑢0/2on this event and loses at most
𝛿+𝜂 elsewhere. Its conditional expected gain is strictly positive. Hence no rival places positive mass
in(𝑡−𝛿,𝑡).
By the preceding argument, no rival can have an atom at𝑡. The profitable upward deviations show
that rivals also place no mass immediately below𝑡. Bidder𝑖 can therefore lower its bid at the atom
without changing its winning probability. This probability is positive, so the lower payment gives a
strict gain, a contradiction.
Ordering best responses.Once atoms have been excluded, conditional winning probabilities𝑝𝑏(𝑣) are
continuous in𝑏 and 𝑣. Fix𝑎 > 𝑏 >0and let 𝑝𝐷(𝑣)=𝑝 𝑎(𝑣)−𝑝 𝑏(𝑣). If the higher bid can be optimal
then 𝑝𝐷 > 0; otherwise it only increases the payment. Both𝑝𝑏 and a positive𝑝𝐷 are expectations of
nonnegative rival-event indicators, so their logarithmic derivatives are bounded in absolute value by
𝜅. For𝑣 > 𝑎,
𝑑
𝑑𝑣 log(𝑣−𝑎)𝑝 𝐷(𝑣) (𝑎−𝑏)𝑝 𝑏(𝑣) ≥ 1 𝑣−𝑎 −2𝜅≥ 1 2.(36)
The higher bid is preferred precisely when this ratio is at least one. Thus, if a lower type weakly
prefers𝑎 to𝑏, every higher type strictly prefers𝑎. Bid zero cannot be optimal for a positive type. It
follows that the sets of optimal bids are ordered across types. For each type with more than one
optimal bid, choose two such bids and the open interval between them. The ordering of optimal bids
makes these intervals disjoint across types. Each contains a rational number, so there are at most
countably many such types. The value distributions have densities, and hence the equilibrium is pure
and nondecreasing outside a null set of values.
Cutoffs and supports.Monotone quantile coupling gives𝑉𝑖 =𝑣 𝑖(𝐵𝑖) almost surely. Continuity of𝐹−1 𝑖
and 𝐻𝑖 gives continuity of𝑣𝑖; no overbidding gives𝐻𝑖(𝑏)≥𝐹 𝑖(𝑏). At a support point, approximate
(𝑣𝑖(𝑏),𝑏) byvalue–bidpairsfromthe equilibrium. Conditionalpayoffcontinuity passes theiroptimality
inequalities to this pair. In particular the cutoff type is strictly above a positive support bid, by (35).
33

Price of Anarchy of First-Price Auctions in Agentic Markets
There can be no open gap in the union of bid supports: a bidder at its right endpoint could lower
its bid into the gap and save money without changing its winning probability. The union begins at
zero because𝐻𝑖(𝑏)≥𝐹 𝑖(𝑏)> 0for every 𝑏 >0. Nor can a positive support point belong to just one
bidder’s support. All of that bidder’s rivals would then have constant bid CDFs in a neighborhood,
again permitting a profitable small reduction. This proves the remaining assertions.□
The next lemma bounds value cutoffs and surplus uniformly over equilibria.
Lemma F.6.There are constants𝑄≥4and𝜎 >0, depending only on𝑛,ℓ,𝑢, such that
(1+𝜎)𝑏≤𝑣 𝑖(𝑏)≤min{1,𝑄𝑏} (0< 𝑏≤𝛽), 𝛽≤ 1 1+𝜎 .(37)
In particular,𝐻𝑖(𝑏)≤𝑢𝑄𝑏.
Proof. Fix0 < 𝑎≤ 1/4andwrite 𝑦𝑖 =𝑣 𝑖(𝑎), 𝑦min =min 𝑖 𝑦𝑖, and𝑦max =max 𝑖 𝑦𝑖. Theevent{max𝑖𝐵𝑖≤𝑎}
is, up to null sets, the value rectangle𝐸≡{𝑉 𝑖≤𝑦 𝑖∀𝑖}. Write𝑅0 =𝑢/ℓ . Under the product distribution
conditioned on that rectangle, each of two fixed bidders has probability at leastℓ/( 2𝑢)= 1/(2𝑅0)
of having value at least𝑦min/2. Conditional on the rectangle under𝜇, the probability of both such
values is therefore at least1/(4𝜌𝑅2 0)≥ 1/(6𝑅2 0). Put𝑑=𝑦 min/2. If𝑑 >2𝑎, let every bidder with value
at least𝑑 and bid at most𝑎 raise that bid to2𝑎. These are separate feasible unilateral deviations. Let
𝐸={max 𝑖𝐵𝑖≤𝑎} and let𝑁 count bidders with𝑉𝑖≥𝑑 and 𝐵𝑖≤𝑎 . For any event𝐴 inside the rectangle
𝐸, the density bounds givePr𝜇(𝐴|𝐸)≥𝜌 −1 Pr𝜈(𝐴|𝐸) . Write Δ𝑖 for bidder𝑖’s gain from its unilateral
deviation. On𝐸, ∑︁
𝑖
Δ𝑖≥(𝑑−2𝑎)1 {𝑁≥2} −2𝑎.
Indeed, if𝑁≥ 2, each selected bidder wins when it deviates, whereas the original allocation has only
one winner. Outside𝐸, any changed bidder originally lost, so its gain is nonnegative. The equilibrium
inequalities consequently give
(𝑑−2𝑎)Pr(at least two such values,max
𝑖
𝐵𝑖≤𝑎)≤2𝑎Pr(max 𝑖 𝐵𝑖≤𝑎).
Using the conditional probability just bounded yields𝑦min≤ 4𝑎(1+ 6𝑅2 0)≤ 28𝑅2 0𝑎. When𝑑≤ 2𝑎, this
bound is immediate as well.
Choose 𝑖 with 𝑦𝑖 =𝑦 max =: 𝑡. Choose equilibrium types v<t tending to𝑡; their bids are at most𝑎.
Their equilibrium utility is at most𝑣(1+𝜀) ˛ 𝑗≠𝑖 𝐻𝑗(𝑎); their deviation to𝑣/2gives (35). Letting𝑣↑𝑡 ,
Ö
𝑗≠𝑖
𝐻𝑗(𝑎)≥ ℓ𝑛−1𝑡𝑛−1 𝜌2𝑛 .
At least one of the other cutoffs equals𝑦min, unless all are equal, in which case any other one does.
Therefore Ö
𝑗≠𝑖
𝐻𝑗(𝑎)≤𝑢 𝑛−1𝑦min𝑡𝑛−2, 𝑡≤𝜌2 𝑛𝑅𝑛−1 0 𝑦min≤42·2 𝑛𝑅𝑛+1 0 𝑎.
For𝑎 >1/4, the bound𝑡≤1gives𝑡≤4𝑎. We may therefore take
𝑄:=2 𝑛+6𝑅𝑛+1 0 ,
which proves𝑣𝑖(𝑏)≤𝑄𝑏for every positive bid.
34

Price of Anarchy of First-Price Auctions in Agentic Markets
For a used positive bid𝑏 of type𝑣, compare(35) with the upper bound(𝑣−𝑏)( 1+𝜀)(𝑢𝑄𝑏) 𝑛−1 on its
utility. Since𝑣≥𝑏and𝜌≤2,
𝑣−𝑏≥ 𝑣𝑛
𝜌2𝑛(𝑅 0𝑄)𝑛−1𝑏𝑛−1≥ 𝑏 2𝑛+1(𝑅 0𝑄)𝑛−1.
Set
𝜎:=2 −(𝑛+1)(𝑅 0𝑄)−(𝑛−1) .
Continuity extends this bound to every point of the bidder’s support. Taking support bids tending
to 𝛽 gives 𝛽≤ 1/(1+𝜎) . Inside a gap of bidder𝑖’s support,𝑣𝑖 is constant. If the gap has a right
endpoint in its support, the surplus bound at that endpoint proves the bound throughout the gap. If
its support has already ended,𝑣𝑖 = 1and the bound follows from𝑏≤𝛽≤ 1/(1+𝜎) . This establishes
(37) everywhere on the stated interval.□
Lemma F.7(Bid densities and first-order conditions).The functions𝐻𝑖 and 𝑣𝑖 are locally Lipschitz on
(0,𝛽]. At their common differentiability points put
ℎ𝑖 =𝐻′ 𝑖/𝐻𝑖, 𝑆= ∑︁
𝑖
ℎ𝑖, 𝑔 𝑖 =𝑆−ℎ 𝑖, 𝜔 𝑖 = 1 𝑣𝑖−𝑏 , 𝐴(𝑏)={𝑖:𝑏∈𝐾 𝑖}.
For almost every𝑏∈(0,𝛽),𝑆 >0,ℎ 𝑖 =0outside𝐴(𝑏), and
𝜌−1𝑔𝑖≤𝜔 𝑖≤𝜌𝑔 𝑖 (𝑖∈𝐴(𝑏)), 𝑆≤ 2𝜌 𝜎𝑏.(38)
At least twoℎ𝑖 are positive almost everywhere.
Proof.Write
𝑃𝑖(𝑡,𝑣)=Pr 𝜇 (max 𝑗≠𝑖 𝐵𝑗≤𝑡|𝑉 𝑖 =𝑣), 𝐺 𝑖(𝑡)=
Ö
𝑗≠𝑖
𝐻𝑗(𝑡).
Fix0 < 𝑎 < 𝛽and a support point𝑏≥𝑎 for bidder𝑖. Its cutoff value𝑣=𝑣 𝑖(𝑏) has surplus at least𝜎𝑎.
Optimality against𝑡∈[𝑏,𝑏+𝜎𝑎/2]gives
𝑃𝑖(𝑡,𝑣)−𝑃 𝑖(𝑏,𝑣)≤ 𝑡−𝑏 𝑣−𝑡 𝑃𝑖(𝑏,𝑣)≤ 2(1+𝜀) 𝜎𝑎 (𝑡−𝑏).
The nonnegative interval-event comparison in(33) implies𝐺𝑖(𝑡)−𝐺 𝑖(𝑏)≤ 2𝜌(𝑡−𝑏)/(𝜎𝑎) . For𝑗≠𝑖 ,
positivity of the other factors gives
𝐻𝑗(𝑡)−𝐻 𝑗(𝑏)≤ 2𝜌 𝜎𝑎(ℓ𝑎) 𝑛−2(𝑡−𝑏).
Put 𝑀𝑎 := 2𝜌/[𝜎𝑎(ℓ𝑎) 𝑛−2] and Δ𝑎 :=𝜎𝑎/ 2. Fix𝑎≤𝑥 < 𝑦≤𝛽 with 𝑦−𝑥≤Δ 𝑎. If𝐾𝑗∩[𝑥,𝑦) is empty,
continuity gives𝐻𝑗(𝑦)=𝐻 𝑗(𝑥). Otherwise, let𝑏 be the first point of𝐾𝑗∩[𝑥,𝑦] . Then 𝑏 < 𝑦and
𝐻𝑗(𝑏)=𝐻 𝑗(𝑥). Another bidder’s support contains𝑏, so the preceding increment estimate gives
𝐻𝑗(𝑦)−𝐻 𝑗(𝑥)=𝐻 𝑗(𝑦)−𝐻 𝑗(𝑏)≤𝑀 𝑎(𝑦−𝑏)≤𝑀 𝑎(𝑦−𝑥).
Partitioning any longer interval into pieces of length at mostΔ𝑎 proves that𝐻𝑗 is Lipschitz on[𝑎,𝛽] .
In particular, it has no singular continuous part there. Since𝐹−1 𝑖 is1/ℓ-Lipschitz, each𝑣𝑖 is locally
Lipschitz on(0,𝛽].
We have
𝑃𝑖(𝑡,𝑣)=
∫
{𝑧𝑗≤𝑣𝑗(𝑡), 𝑗≠𝑖}
𝑟(𝑣,𝑧 −𝑖)
Ö
𝑗≠𝑖
𝑓𝑗(𝑧𝑗)𝑑𝑧−𝑖.
35

Price of Anarchy of First-Price Auctions in Agentic Markets
At a common differentiability point of the cutoff functions, this expression is differentiable in𝑡 for
every fixed𝑣. If𝑏∈𝐾 𝑖∩(0,𝛽), optimality of𝑏for type𝑣 𝑖(𝑏)gives
𝜕𝑡 log𝑃 𝑖(𝑡,𝑣)|𝑡=𝑏, 𝑣=𝑣𝑖(𝑏) = 1 𝑣𝑖(𝑏)−𝑏 =𝜔 𝑖(𝑏).
The derivative holds the own value fixed. Boundary differentiation and the bounds on𝑟give
(1−𝜀)𝐺 ′ 𝑖(𝑏)≤𝜕 𝑡𝑃𝑖(𝑏,𝑣 𝑖(𝑏))≤(1+𝜀)𝐺 ′ 𝑖(𝑏),
as well as(1−𝜀)𝐺 𝑖(𝑏)≤𝑃 𝑖(𝑏,𝑣 𝑖(𝑏))≤( 1+𝜀)𝐺 𝑖(𝑏). If𝐺′ 𝑖(𝑏)= 0, the first-order condition is impossible.
Otherwise, dividing these inequalities proves the first bound in(38). Outside 𝐾𝑖, ℎ𝑖 = 0. Since
|𝐴(𝑏)|=𝑚≥ 2, ˝ 𝑖∈𝐴 𝑔𝑖 =(𝑚− 1)𝑆. Summing the lower bounds for𝜔𝑖 and using𝜔𝑖≤ 1/(𝜎𝑏) gives
𝑆≤ 2𝜌/(𝜎𝑏). If just oneℎ𝑖 were positive, that bidder would have𝑔𝑖 = 0; if all were zero, every support
bidder would have𝑔𝑖 = 0. Both possibilities contradict the same first-order condition. All statements
hold off a common null set.□
The next lemma uses these facts to write an independent comparison equilibrium.
Lemma F.8.There is 𝜀0 =𝜀 0(𝑛,ℓ,𝑢)> 0such that, for𝜀≤𝜀 0, there are atomless bid distributions𝐻∗ 𝑖
with the following properties. Independent draws𝐵∗ 𝑖∼𝐻 ∗ 𝑖 , assigned values𝑉∗ 𝑖 =𝑣 𝑖(𝐵∗ 𝑖), induce an exact
no-overbidding Bayes–Nash equilibrium with independent values. Moreover,
∑︁
𝑖
∥𝐻𝑖−𝐻∗ 𝑖∥TV≤ 64𝑢𝑛(𝑛+1)𝑄 2 𝜎2 𝜀.(39)
Here total variation is between probability distributions. The independent value marginals in this
comparison auction may differ from the original𝐹𝑖.
Proof. We keep the value cutoffs𝑣𝑖 and choose new logarithmic bid derivatives. For a bidder placing
positive bid density at𝑏, the independent first-order condition requires˝ 𝑗≠𝑖ℎ∗ 𝑗 = 1/(𝑣𝑖(𝑏)−𝑏)=𝜔 𝑖(𝑏).
The following construction satisfies these equalities while allowing a bidder to have zero density. For
𝑏∈(0,𝛽], order the𝜔 𝑖(𝑏)increasingly and define
𝑆∗(𝑏)=min 2≤𝑘≤𝑛
˝𝑘
𝑗=1𝜔(𝑗)(𝑏)
𝑘−1 , ℎ ∗ 𝑖(𝑏)=[𝑆 ∗(𝑏)−𝜔 𝑖(𝑏)]+, 𝑧(𝑏)=𝑏+ 1 𝑆∗(𝑏).(40)
The functions in(40) satisfy the following properties of the construction, which we will verify in what
follows: ∑︁
𝑖
ℎ∗ 𝑖 =𝑆∗, 𝑔 ∗ 𝑖 := ∑︁
𝑗≠𝑖
ℎ∗ 𝑗 =min{𝑆∗,𝜔 𝑖}, 1 𝑄𝑏≤𝑆∗≤ 2 𝜎𝑏.(41)
The function𝑧 is continuous and nondecreasing. Almost everywhere,𝑆∗≤𝜌𝑆 . On every open interval
disjoint from𝐾𝑖,
[𝑣𝑖(𝑏)−𝑧(𝑏)] +≤𝑞𝑄𝑏, 𝑞:=1−𝜌 −2≤4𝜀.(42)
For positive𝜔1,...,𝜔 𝑛, put𝐹(𝑠) := ˝ 𝑖(𝑠−𝜔 𝑖)+−𝑠 . At𝑠=𝜔 (2), 𝐹(𝑠)=−𝜔 (1) < 0. Above𝜔(2), 𝐹 is
strictly increasing and tends to infinity, so it has a unique root𝑠there. For every𝑘≥2,
(𝑘−1)𝑠−
𝑘∑︁
𝑗=1
𝜔(𝑗) =
𝑘∑︁
𝑗=1
(𝑠−𝜔 (𝑗))−𝑠≤𝐹(𝑠)=0.
Equality holds when𝑘 is the number of coordinates strictly below𝑠, which is at least two. Hence
𝑠=min 2≤𝑘≤𝑛
˝𝑘
𝑗=1𝜔(𝑗)/(𝑘− 1), as in(40). Scaling the coordinates scales the root, and increasing any
36

Price of Anarchy of First-Price Auctions in Agentic Markets
coordinate decreases𝐹 at a fixed𝑠, so the root is homogeneous and nondecreasing in each coordinate.
It follows that˝ 𝑖ℎ∗ 𝑖 =𝑆∗ and 𝑔∗ 𝑖 =min{𝑆∗,𝜔 𝑖}. The bounds in(41) follow from1/(𝑄𝑏)≤𝜔 𝑖≤ 1/(𝜎𝑏).
The equation for the common value level is
∑︁
𝑖
[𝑣𝑖(𝑏)−𝑧(𝑏)] +
𝑣𝑖(𝑏)−𝑏 =1.(43)
For fixed𝑧 > 𝑏, the left side increases with𝑏 and with each𝑣𝑖, and decreases with𝑧 near its unique
solution. Since each𝑣𝑖(𝑏) is nondecreasing,𝑧(𝑏) is nondecreasing as well. If the old solution lies
below the new bid, the conclusion is immediate. Continuity follows from(41) and the positive surplus
bounds.
At a common differentiability point take𝐴=𝐴(𝑏) , of size𝑚≥ 2. The minimum over all bidders is at
most the ratio formed from these𝑚coordinates. Thus (38) gives
𝑆∗≤
˝
𝑖∈𝐴 𝜔𝑖
𝑚−1 ≤𝜌𝑆.
Now let(𝑙,𝑟) be a component of the complement of𝐾𝑖 in(0,𝛽) , allowing𝑟=𝛽 for a terminal interval.
Necessarily 𝑙 > 0: an initial gap would contradict𝐻𝑖(𝑏)≥𝐹 𝑖(𝑏)> 0and 𝐻𝑖(0)= 0. The cutoff𝑣𝑖 is
constant there, say𝑤, and𝑙 is an optimal bid for type𝑤. By Lemma F.5,𝑙 is an optimal bid for the
cutoff type𝑤. For𝑙 < 𝑡 < 𝑟, optimality implies
log𝑃 𝑖(𝑡,𝑤)−log𝑃 𝑖(𝑙,𝑤)≤log 𝑤−𝑙 𝑤−𝑡 = ∫ 𝑡 𝑙 𝑑𝑏 𝑤−𝑏 .
On this intervalℎ𝑖 = 0, so𝑔𝑖 =𝑆 . The density comparisons in the proof of Lemma F.7 apply at every
fixed own value, including𝑤; they do not require the bid to lie in𝐾𝑖. Together with𝑆∗≤𝜌𝑆 , they give
𝜕𝑏 log𝑃 𝑖(𝑏,𝑤)≥𝑆 ∗(𝑏)/𝜌 2 almost everywhere. Integrate this inequality, divide by𝑡−𝑙 , and let𝑡↓𝑙 . By
continuity,
𝑆∗(𝑙)≤ 𝜌2 𝑤−𝑙 , 𝑧(𝑙)≥𝑤−(1−𝜌 −2)(𝑤−𝑙).
Since 𝑧 is nondecreasing and𝑤≤𝑄𝑙 , it follows that[𝑤−𝑧(𝑏)] +≤𝑞(𝑤−𝑙)≤𝑞𝑄𝑏 . This proves the gap
estimate, including a bidder’s terminal interval, where𝑤=1.
Next, we need to establish a uniform comparison of the logarithmic derivatives.
Comparison of derivatives.At a common differentiability point, write𝐴=𝐴(𝑏) and𝜂= ˝ 𝑖∉𝐴 ℎ∗ 𝑖. If
ℎ∗ 𝑖 >0, the identity𝑧=𝑏+1/𝑆 ∗ givesℎ∗ 𝑖≤(𝑆 ∗)2[𝑣𝑖−𝑧]+.
For𝑖∉𝐴, the unused-interval estimate gives
𝜂≤ 4𝑛𝑞𝑄 𝜎2𝑏 ≤ 16𝑛𝑄𝜀 𝜎2𝑏 .(44)
We choose𝜖0 :=𝜎 2/(32𝑛𝑄 2), so that𝜖≤𝜖 0 ensures𝜂≤1/(2𝑄𝑏). That is,
𝜀≤𝜀 0 := 𝜎2 32𝑛𝑄2.
Let 𝑆𝐴 be the scalar root formed using just the coordinates𝜔𝑖 with 𝑖∈𝐴 . Applying the same root to
the coordinates𝑔𝑖 =𝑆−ℎ 𝑖 gives𝑆, since˝ 𝑖∈𝐴 ℎ𝑖 =𝑆 and at least two of thoseℎ𝑖 are positive, so𝑆 is the
root above the second-smallest𝑔𝑖. Homogeneity, monotonicity, and(38) imply𝑆/𝜌≤𝑆 𝐴≤𝜌𝑆 , while
adding the other coordinates gives𝑆∗≤𝑆 𝐴.
37

Price of Anarchy of First-Price Auctions in Agentic Markets
At𝑡=𝑆 ∗, the function𝐹𝐴(𝑡)= ˝ 𝑖∈𝐴(𝑡−𝜔 𝑖)+−𝑡 equals−𝜂. There must be at least two𝜔𝑖,𝑖∈𝐴 , strictly
below𝑆∗. Otherwise𝐹𝐴(𝑆∗) would be−𝑆∗ or−𝜔𝑖, at most−1/(𝑄𝑏), contradicting(44). Consequently
𝐹𝐴 has slope at least one for𝑡≥𝑆∗. Since𝐹 𝐴(𝑆𝐴)=0, we obtain
0≤𝑆 𝐴−𝑆∗≤𝜂,|𝑆 ∗−𝑆|≤(𝜌−1)𝑆+𝜂.
For𝑖∈𝐴, the positive-part map is1-Lipschitz, so
|ℎ∗ 𝑖−ℎ 𝑖|≤|𝑆 ∗−𝑆|+|𝜔 𝑖−𝑔 𝑖|≤2(𝜌−1)𝑆+𝜂.
Adding the inactive coordinates gives
∑︁
𝑖
|ℎ∗ 𝑖−ℎ 𝑖|≤2𝑛(𝜌−1)𝑆+(𝑛+1)𝜂(45)
≤
 15𝑛
𝜎 + 16𝑛(𝑛+1)𝑄 𝜎2
 𝜀
𝑏≤ 𝐾𝜀 𝑏 ,(46)
where we take
𝐾:= 32𝑛(𝑛+1)𝑄 𝜎2 .
Here𝜌−1≤5𝜀/2and𝑆≤2𝜌/(𝜎𝑏). Our choice of𝜀 0 also gives
𝐾𝜀≤ 𝑛+1 𝑄 ≤ 1 2.
The factor1/𝑏will be offset by the small-bid probability𝐻𝑖(𝑏)≤𝑢𝑄𝑏in the coupling below.
As a last step, we need to do an exact independent comparison and calculate its total-variation error.
Exact independent comparison and TV error.For𝜀≤𝜀 0 define
𝐻∗ 𝑖(𝑏)=exp

−
∫ 𝛽
𝑏
ℎ∗ 𝑖(𝑡)𝑑𝑡

(0< 𝑏≤𝛽), 𝐻 ∗ 𝑖(0)=0.(47)
Nonnegativity ofℎ∗ 𝑖 makes (47) nondecreasing, with value one at𝛽. It is locally absolutely continuous
away from zero. Write𝑑=𝐾𝜀≤ 1/2. The original distributions also satisfy𝐻𝑖(𝑏)=exp(−
∫ 𝛽
𝑏 ℎ𝑖), and
hence
𝐻∗ 𝑖(𝑏)≤𝐻 𝑖(𝑏)(𝛽/𝑏) 𝑑≤𝑢𝑄𝑏(𝛽/𝑏) 𝑑−→0(𝑏↓0).(48)
Thus there is no missing mass or atom at zero. Both the original and new distributions have densities
on the positive bid interval.
Global best responses and distintegration.The new competing distribution𝐺∗ 𝑖 = ˛ 𝑗≠𝑖 𝐻∗ 𝑗 has logarithmic
derivative𝑔∗ 𝑖 =min{𝑆∗,𝜔 𝑖}. Put
𝜙∗ 𝑖(𝑏)=𝑏+1/𝑔 ∗ 𝑖(𝑏)=max{𝑣 𝑖(𝑏),𝑧(𝑏)}.
This function is nondecreasing. Whereℎ∗ 𝑖 > 0, 𝜔𝑖 < 𝑆∗, so𝜙∗ 𝑖 =𝑣 𝑖. For a fixed value𝑣, expected utility
from a positive bid𝑡is(𝑣−𝑡)𝐺 ∗ 𝑖(𝑡), whose derivative is
𝐺∗ 𝑖(𝑡)𝑔∗ 𝑖(𝑡)[𝑣−𝜙 ∗ 𝑖(𝑡)]
almost everywhere. At𝑣=𝜙 ∗ 𝑖(𝑏) it is nonnegative before𝑏 and nonpositive afterward. Thus𝑏 is a
global best response, not just a stationary bid. Bid zero wins with probability zero, and bids above𝛽
38

Price of Anarchy of First-Price Auctions in Agentic Markets
pay more for the same certain allocation. Since a new sampled bid lies whereℎ∗ 𝑖 > 0almost surely,
its assigned value is𝑣𝑖(𝑏)=𝜙 ∗ 𝑖(𝑏). Let 𝐹∗ 𝑖 be the distribution of𝑣𝑖(𝐵∗ 𝑖), and let𝑠∗ 𝑖(𝑣) be a regular
conditional distribution of𝐵∗ 𝑖 given𝑣𝑖(𝐵∗ 𝑖)=𝑣 . The independent value–bid pairs induce independent
values with distribution𝜈∗ = ∯ 𝑖𝐹∗ 𝑖. Almost every sampled bid is a global best response for its assigned
value, so the kernels𝑠∗ 𝑖 form a Bayes–Nash equilibrium under𝜈∗. Flat parts of𝑣𝑖 may produce value
atoms and mixed conditional bids. The surplus bound ensures no overbidding, and all constructed
values lie in[0,1].
Total Variation.For a fixed bidder put𝑚𝑖 =min{ℎ 𝑖,ℎ∗ 𝑖}and define
𝐽𝑖(𝑏)=exp

−
∫ 𝛽
𝑏
𝑚𝑖(𝑡)𝑑𝑡

, 𝐸 𝑖(𝑏)=exp

−
∫ 𝛽
𝑏
(ℎ𝑖−𝑚 𝑖)(𝑡)𝑑𝑡

,
and define𝐸∗ 𝑖 similarly withℎ∗ 𝑖−𝑚 𝑖. Extend these CDFs by their limits at zero and by one above
𝛽. Draw independent𝐶𝑖,𝐷 𝑖,𝐷∗ 𝑖 with these distributions. Thenmax{𝐶𝑖,𝐷 𝑖} has distribution𝐻𝑖 =𝐽 𝑖𝐸𝑖,
and max{𝐶𝑖,𝐷∗ 𝑖} has distribution𝐻∗ 𝑖 =𝐽 𝑖𝐸∗ 𝑖. The two bids agree unless an excess draw exceeds the
common draw. Since𝐸′ 𝑖 =(ℎ 𝑖−𝑚 𝑖)𝐸𝑖≤ℎ 𝑖−𝑚 𝑖 on(0,𝛽),
∥𝐻𝑖−𝐻∗ 𝑖∥TV≤Pr(𝐷 𝑖 > 𝐶𝑖)+Pr(𝐷 ∗ 𝑖 > 𝐶𝑖)
=
∫ 𝛽
0
𝐽𝑖(𝑏)[𝐸 ′ 𝑖(𝑏)+(𝐸 ∗ 𝑖)′(𝑏)]𝑑𝑏
≤
∫ 𝛽
0
𝐽𝑖(𝑏)|ℎ 𝑖(𝑏)−ℎ ∗ 𝑖(𝑏)|𝑑𝑏.
Atoms of the component distributions at zero contribute nothing to the strict exceedance events. Also,
𝐽𝑖(𝑏)≤𝐻 𝑖(𝑏)exp
∫ 𝛽
𝑏
|ℎ𝑖−ℎ∗ 𝑖|

≤𝑢𝑄𝑏(𝛽/𝑏) 𝑑.
Summing over bidders and using˝ 𝑖|ℎ𝑖−ℎ∗ 𝑖|≤𝑑/𝑏gives:
∑︁
𝑖
∥𝐻𝑖−𝐻∗ 𝑖∥TV≤𝑢𝑄𝑑 𝛽𝑑
∫ 𝛽
0
𝑏−𝑑 𝑑𝑏= 𝑢𝑄𝑑𝛽 1−𝑑 ≤2𝑢𝑄𝐾𝜀= 64𝑢𝑛(𝑛+1)𝑄 2 𝜎2 𝜀.
This proves (39). □
Proof of Theorem F.4
Proof.Write
𝐵:= 64𝑢𝑛(𝑛+1)𝑄 2
𝜎2 ,
the coefficient obtained in Lemma F.8. Suppose first that𝜀≤𝜀 0. Evaluate the original strategies under
𝜈, so their bids have product distribution∯ 𝑖𝐻𝑖, and use the independent comparison equilibrium
from that lemma. Let𝑖∗(𝑏) be the winning bidder. Under the original product prior𝜈, Lemma F.5
gives independent bids𝐵𝑖∼𝐻 𝑖 with values𝑣𝑖(𝐵𝑖). The comparison equilibrium has independent bids
𝐵∗ 𝑖∼𝐻 ∗ 𝑖 with the same value cutoffs. Thus the same function
𝐷(𝑏):=𝑐 JL max 𝑖 𝑣𝑖(𝑏𝑖)−𝑣 𝑖∗(𝑏)(𝑏𝑖∗(𝑏))
39

Price of Anarchy of First-Price Auctions in Agentic Markets
represents the welfare shortfall in both auctions. Both product bid distributions are atomless. The
function𝐷 takes values in[𝑐JL−1,𝑐 JL], an interval of length one. The Jin–Lu theorem gives𝔼[𝐷(𝐵∗)]≤
0. Coupling the bids independently across bidders gives
 Ì 𝑖 𝐻𝑖− Ì 𝑖 𝐻∗ 𝑖  TV ≤ ∑︁ 𝑖 ∥𝐻𝑖−𝐻∗ 𝑖∥TV≤𝐵𝜖.
The product bid distributions differ in total variation by at most𝐵𝜀, so
𝑐JL𝔼𝜈[𝑉(1)]−𝔼 𝜈[𝑊]≤𝐵𝜀.
Changing the value distribution from𝜈 to𝜇 changes the expectation of this signed shortfall by at most
𝜏. Consequently,
𝔼𝜇[𝑊]≥𝑐 JL𝔼𝜇[𝑉(1)]−𝜏−𝐵𝜀.(49)
For𝜀 > 𝜀0, the same inequality is immediate:𝐵𝜀 > 𝐵𝜀0 = 2𝑢(𝑛+ 1)> 𝑐 JL, while the signed shortfall is
at most𝑐JL. Evaluated at the original strategies,𝐷(𝑠(𝑉)) is a bounded function of values with range of
length 1. Changing the prior from𝜈to𝜇therefore changes its expectation by at most𝜏.
It remains to bound𝜀 by𝜏. Since𝜏= 1 2 ∫ |𝑟− 1|𝑑𝜈 , take a point where|𝑟− 1|=𝜀 > 0. The derivative
bound ensures|𝑟−1|≥𝜀/2within within sup-norm distance1/(2𝑛𝐿)of this point. The intersection
of this cube with[0,1]𝑛 has volume at least(2𝑛𝐿)−𝑛 and product density at leastℓ𝑛. Thus
𝜏≥ ℓ𝑛𝜀 4(2𝑛𝐿)𝑛, 𝜀≤4  2𝑛𝐿 ℓ 𝑛 𝜏.
Substituting in (49) proves the claim with
𝐶=1+4𝐵
 2𝑛𝐿
ℓ
𝑛
.
At𝜀=0, the independent-values theorem applies directly.□
The universal1− 1/𝑒 bound leaves shortfall at most(𝑒−1−𝑒−2)𝔼[𝑉(1)]≤𝑒 −1−𝑒−2 after normalization.
Thus on this class of priors we may take
𝜂reg 𝑛 (𝑡):=min{𝑒 −1−𝑒−2,𝐶𝑡}.
as the additive-error function in Theorem 5 on this class of priors. Importantly, we note that we have
not attempted to optimize for the constant.
An example.Let 𝑓𝑖(𝑣)= 1+𝛼 𝑖(2𝑣− 1),with|𝛼 𝑖|≤ 1 2, and define the joint density relative to the
product of these marginals by
𝑟(𝑣)=1+𝜀(2𝐹 1(𝑣1)−1)(2𝐹 2(𝑣2)−1),0≤𝜀≤ 1 13.
The centered factors preserve the marginals. These priors satisfy the assumptions withℓ= 1/2,
𝑢= 3/2, and𝐿= 3, even when the marginals differ. Since𝐹𝑖(𝑉𝑖) is uniform under𝐹𝑖,∥𝑟− 1∥∞ =𝜀 and
𝜏=𝜀/8. To see this, observe𝜖 2 𝔼𝜈[|2𝐹 1(𝑉1)−1||2𝐹 2(𝑉2)−1| ] = 𝜖 8.
40
