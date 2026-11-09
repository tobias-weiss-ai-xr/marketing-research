---
title: Learning the Cost of Reliable Inference
url: https://arxiv.org/abs/2609.28322
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Dimitrios Rontogiannis
- Ander Artola Velasco
- Manuel Gomez Rodriguez
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.28322
pages: 77
chars: 173722
fetched_at: '2026-11-08T13:22:29+00:00'
kb_version: 1
---

# Learning the Cost of Reliable Inference

Learning the Cost of Reliable Inference
Dimitrios Rontogiannis, Ander Artola Velasco, and Manuel Gomez Rodriguez
Max Planck Institute for Software Systems
Kaiserslautern, Germany
{drontogi, avelasco, manuel}@mpi-sws.org
Abstract
Benchmarking and routing platforms increasingly act as intermediaries connecting large language
model providers with end-users. However, providers on these platforms typically use a fixed price per
token, preventing users from achieving the most competitive price for their tasks. In this work, we design a
procurement platform where token prices for each task are driven by provider competition, enabling users
to secure competitive pricing for guaranteed quality levels. To this end, the platform sequentially routes
queries via a reverse second-price auction that incentivizes model providers to truthfully bid their best
estimate of the average cost to serve a user’s query. As it routes queries, the platform learns the quality
offered by each provider and progressively routes queries to the most cost-competitive provider among
those meeting a desired quality threshold. To validate our design, we conduct experiments with multiple
LLMs from the Llama and Qwen families on popular mathematical reasoning and question-answering
benchmarks. The results show that the pricing margin of the most cost-competitive provider on our
platform varies significantly—from10%to71%—depending on the task and quality threshold. This
suggests a substantial inefficiency in the current fixed-price market, and it demonstrates that our platform
may enable users to capture maximum savings whenever competitive market conditions permit.
1 Introduction
The rapid proliferation of large language models (LLMs) has led to a highly competitive market of online
service providers offering models of varying capabilities at different prices. To help users navigate their
choice of models, benchmarking and routing platforms have become popular, letting users compare model
performance on well-established tasks and even automatically selecting a provider to serve their queries.1
However, existing platforms do not allow users to achieve the most competitive price for their tasks. This
is because providers on these platforms typically charge users a fixed price per token,2 which fails to reflect
that a provider’s cost to serve a model and the response quality the user obtains in return depend heavily on
the specific task. As a concrete illustration, consider a user who wants to use an LLM to assist with medical
diagnosis and can choose between two providers, each offering a different model. Suppose the providers
charge$0 .06and$0 .07per token, while generating a token costs them$0.01and$0 .04, respectively. Then, if
both models produce responses of similar quality and number of tokens for the user’s task, the user—acting
rationally—would select the cheapest model and pay$0.06per token. However, if the providers competed
on price for the user’s task, the user could in principle pay as little as$0.04per token: the first provider
would lower its per-token price down to this point, since below this the second provider—which cannot
profitably price below its own cost—would no longer be a competitive alternative [Milgrom and Roberts,
1982, Mahmood, 2024, Bergemann et al., 2025a].
In this work, we design a procurement platform that addresses this price inefficiency, enabling users to
secure competitive pricing on their tasks for guaranteed quality levels. To this end, the platform sequentially
1See,e.g.,https://artificialanalysis.ai,https://openrouter.ai, andhttps://thegrid.ai.
2https://ai.google.dev/gemini-api/docs/pricing,https://openai.com/api/pricing/,https://www.claude.com/pricing.
1
arXiv:2609.28322v2  [cs.AI]  24 Sep 2026

routes queries via a reverse second-price auction that incentivizes providers to truthfully bid their best
estimate of the average cost to serve a user’s query. As it routes queries, the platform learns the quality
offered by each provider and progressively routes queries to the most cost-competitive provider among those
meeting a desired quality threshold. More formally, we show that, with high probability, the platform routes
all but a vanishing fraction of the user’s queries to the most cost-competitive provider, whose (average)
pricing margin converges to the difference between the second-lowest average cost among qualified providers
and its own average cost.
To validate our platform, we conduct experiments with multiple LLMs from theLlama and Qwen families
on popular mathematical reasoning and question-answering benchmarks. We find that the pricing margin of
the most cost-competitive provider varies significantly—from10%to71%—depending on the task and quality
threshold. This suggests a substantial inefficiency in the current fixed-price market, and it demonstrates that
our platform may enable users to capture maximum savings whenever competitive market conditions permit.
Further related work.Our work contributes to a rapidly growing body of literature on the economic
aspects of LLMs-as-a-service [Mahmood, 2024, Bergemann et al., 2025a, Raghavan, 2024, La Malfa et al.,
2024, Laufer et al., 2024, Bergemann et al., 2025b, Olmedo et al., 2026, Velasco et al., 2026a,b,c]. Within this
literature, the works most closely related to ours characterize how LLM providers price their models when
serving users in a competitive market. Specifically, Mahmood [2024] study the price competition between
providers serving models of varying quality across different tasks, while Bergemann et al. [2025a] characterize
the menu of token prices that maximizes a provider’s revenue across heterogeneous users. Our work also
relates to a recent line that evaluates LLMs not only by their capabilities but also by the price users pay [Wang
et al., 2024a, Zellinger and Thomson, 2025, Erol et al., 2026, Chen et al., 2026a]. This alternative view has
very recently materialized in already-deployed platforms: some platforms publish provider rankings that
explicitly factor in their prices, while others act as routers that lower the price by letting providers compete
on their rates.1 In contrast to these solutions, our platform explicitly ensures that the user asymptotically
pays the most competitive market price for their specific task at guaranteed quality levels.
Our work also builds on a large body of literature on mechanism and auction design [McAfee and McMillan,
1986, Ledyard, 1987, Che, 1993, Bar-Yossef et al., 2002, Roughgarden et al., 2017, Akbarpour and Li, 2020,
Awaya et al., 2025, Cai and Liao, 2026]. In this context, our sequential setting connects to a strand on
dynamic auctions, where bidders sequentially learn private information, such as their type, that determines
their utility, and the objective is to design mechanisms that ensure truthful bidding over multiple time
steps [Hossain, 2008, Pavan et al., 2014, Weed et al., 2016, Feng et al., 2018, Bergemann and Välimäki, 2019,
Bergemann et al., 2025c]. To the best of our knowledge, however, we are the first to consider a setting where
LLM providers act as bidders whose operational costs and serving qualities vary across tasks.
Lastly, at a technical level, our work relates to a strand of the multi-armed bandit literature in which
the learner must choose among alternatives that are themselves strategic agents seeking to maximize their
utility, requiring learning algorithms that explicitly account for these incentives [Auer et al., 2002, Even-Dar
et al., 2006, Babaioff et al., 2009, Bubeck and Cesa-Bianchi, 2012, Jain et al., 2015, Braverman et al., 2019,
Lattimore and Szepesvári, 2020, Freeman et al., 2020, Padmanabhan et al., 2022]. Therein, the closest works
to ours are those that study procurement auctions through a bandit lens [Singla and Krause, 2013, Chen
et al., 2026b, Patra et al., 2026]. Specifically, both Chen et al. [2026b] and Patra et al. [2026] formulate
procurement as a contextual bandit problem, with the latter studying the selection of LLM providers through
a reverse auction where providers report their generation costs and the user learns query-dependent model
quality. Unlike Patra et al. [2026], however, we do not assume that providers know their model’s cost on
the user’s task, and our payment rule asymptotically converges to the most competitive price, equal to the
second-lowest average cost among qualified providers. In a similar LLM routing setting, Cao et al. [2026]
instead design an allocation and payment mechanism that disincentivizes providers from misreporting their
capabilities or manipulating the token bills charged to the user.
2

2 A Procurement Platform for Reliable Inference
In this section, we introduce a procurement platform that acts as an intermediary between a user who seeks
to solve a specific task (e.g., coding, mathematical reasoning, or question answering) and a set ofN LLM
providers. By incentivizing providers to compete on price, the platform ensures the user secures the most
competitive pricing at a guaranteed quality level on all but a vanishing fraction of queries.
The platform operates sequentially over time stepst = 1, 2, . . . , T, where the total number of queriesT is
unknown to the providers but assumed to be at least the number of providersN. At any given time step,
each provider participates in the platform by maintaining a standing bidbi,t ∈ [0, cmax], where cmax > 0
is an upper bound on the cost of serving a single query. Given the current bid vectorbt = (b1,t, . . . , bN,t),
the platform receives a queryxt ∈ Xthat the user wishes to solve, whereX is the space of possible queries
characterizing the user’s task, and selects the providerIt ∈ [N ]that serves it. ProviderIt generates a response
yt ∈ Yto the query, whereY is the space of possible responses,3 and, by doing so, it incurs a generation
cost cIt,t ∈ [0, cmax], which includes the cost of energy, compute, or hardware. The platform then grades the
response using a scorer(xt, yt) ∈ [0, 1], ranging from unsatisfactory(0)to fully satisfactory(1), and sets the
payment the user makes to providerIt. Finally, providerIt may update its standing bid tobIt,t+1, while the
bid of every other provider remains unchanged:bi,t+1 = bi,t for all i̸ = It. In what follows, we denote the
distribution of the query asP x, the distribution of the cost incurred by provideri as P c i , and the distribution
of the score received by provideri’s response asP r i , with a meanqi ∈ [0, 1]that we refer to as the (average)
quality of the provider.
We now describe the rules used by the platform to allocate queries and pay the providers. Our key idea is
to combine an allocation rule based on confidence bounds—which progressively narrows the search to the
qualifiedprovider offering the lowest price to the user—with a second-price payment rule that incentivizes
providers to bid as low as possible without risking an unprofitable win. Specifically, the platform begins with
an initialization phase spanning the firstN time steps, during which it assigns one query to each provider
in turn and pays themcmax. This ensures every provider serves at least one query, rendering the estimates
below well-defined from roundN+ 1onward.
Thereafter, at each roundt > N, the platform maintains a running estimate of each provider’s quality,
ˆqi,t = 1 mi,t
t−1X
τ=1
r(xτ , yτ )1{I τ =i},(1)
where mi,t = Pt−1 τ=1 1{I τ = i} counts how many times provideri has been selected before roundt. The goal
of these estimates is to identify the set of qualified providersQ = {i∈ [N ] : qi ≥q min}, meeting a user-defined
quality threshold qmin, which we assume contains at least two providers4. Since the true qualitiesqi are
unknown, the platform instead forms an optimistic estimate ofQ,
ˆQt =  i∈[N] : ˆq i,t +β(m i,t)≥q min 	 ,whereβ(m i,t) =
vuut 1
2mi,t
ln

2π2N m2 i,t
3δ
!
.(2)
Here, β(mi,t)is a confidence radius at a levelδ∈ (0, 1)fixed by the platform that accounts for the error
in the empirical estimateˆqi,t, so that ˆQt contains every provider whose upper confidence bound on quality
exceeds the thresholdqmin. In Appendices A.1 and A.2, we show that, with probability at least1−δ , this
optimistic estimate never excludes a qualified provider,i.e.,Q ⊆ˆQt holds simultaneously across all time
stepst > N.
Using the set ˆQt, the platform allocates the query by prioritizing providers with lower bids while giving an
explicit advantage to those that have not yet been selected often. More concretely, letg(t)be an increasing
3In practice, the provider generatesyt by sampling a sequence of tokens from its model, and soY is the set of finite-length token
sequences.
4This assumption is needed only for the analysis. If a single provider is estimated to be qualified, the minimum in Eq. 4 is over
an empty set and the provider is paidcmax.
3

function specified by the platform that grows sublinearly int, and St = {i∈ ˆQt : mi,t < g(t) } denote the
set of estimated-qualified providers selected fewer thang(t)times so far. Then, at each roundt > N, the
platform selects:5
It =



Uniform(S t)ifS t ̸=∅,
argmin
i∈ ˆQt

bi,t −c max β(mi,t)

otherwise,
(3)
with ties broken arbitrarily. That is, ifSt ̸= ∅, which we refer to as an exploration step, the platform selects at
random an estimated-qualified provider that has not been sampled sufficiently according to the functiong(t).
Otherwise, the rule selects the provider minimizing an optimistic bidding index, where the termcmax β(mi,t)
gives an additional advantage to providers whose confidence radius remains large. Altogether, this allocation
rule ensures that qualified providers are selected often enough for the platform to reliably estimate their
quality and, as we will see in Section 3, for the providers to learn their own costs.
To design the payment rule, we build on the classical second-price rule from the auction and mechanism
design literature [Vickrey, 1961, Nisan et al., 2011]. Specifically, for any provideri, we define the critical
paymentP i,t as
Pi,t =c max β(mi,t) + min
j∈ ˆQt\{i}

bj,t −c max β(mj,t)

,(4)
where the minimum over an empty set is taken to be+∞ by convention. The actual payment made to the
selected providerI t is then set to
πt =
(
cmax ifS t ̸=∅,
min{P It,t, cmax}otherwise. (5)
In words, in an exploration step, the provider selected uniformly at random from the setSt is paid cmax.
Otherwise, the selected providerIt receives a payment that depends on how often the providers have been
selected in the past and on the other providers’ bidsb−It,t = (bj,t)j̸=It, but not on its own bidbIt,t. Overall,
the complete operation of our procurement platform is summarized in Algorithm 1.
3 Pricing Inference Through Competition
In this section, we study the incentives that providers face when participating in our procurement platform
and characterize their optimal bidding strategy. As a first step, we analyze the conditions under which a
provider is selected to serve a query as a function of their bid. Concretely, the following proposition shows
that, when St = ∅, a provider’s assignment is determined by whether their standing bid falls below the critical
paymentP i,t.6
Proposition 1.Fix a step t > Nwith St = ∅, a provideri∈ ˆQt, and the other providers’ bidsb−i,t. Then,
provideriis assigned the queryx t if they bidbi,t < Pi,t, and is not assigned the query ifbi,t > Pi,t.
The above proposition does not fully characterize how a providershouldbid; however, it already offers
valuable intuition. WhenSt ̸= ∅, the query is assigned independently of the bidsbt, meaning a provider’s bid
only influences the allocation whenSt = ∅. In this case, a provider is assigned the query only if it bids below
the threshold Pi,t. Because this threshold depends on the other providers’ bids, it is unknown to provider
i in advance, which incentivizes it to bid as low as possible. Conversely, once a provider bids low enough
to secure the query, due to the payment rule in Eq. 5, their final payout remains independent of their own
bid. Together, these properties suggest that providers are incentivized to bid truthfully according to the
generation costs they incur. In the remainder of this section, we formalize this intuition and characterize the
resulting equilibrium.
5If ˆQt = ∅, thenIt is chosen uniformly at random. However, this occurs with probability at mostδ (see Appendices A.1 and A.2).
6All proofs are deferred to Appendix A.
4

Algorithm 1It routes the user’s queries to a qualified provider at the lowest competitive price.
1: Input:providers[ N ], quality thresholdqmin, confidence levelδ, allocation parametersk, α, user-defined
scorer, cost boundc max
2: Initialization:assign one query to each provideri∈ [N ], pay themcmax, and receive their first standing
bidb i
3:Setm i ←1andˆq i ←r(x i, yi)for alli∈[N]
4:fort=N+ 1, N+ 2, . . .do
5:Receive user queryx t ∼P x
6:β i ←
q
1
2mi ln
 2π2N m2 i
3δ

for alli∈[N]▷confidence radius
7: ˆQ ← {i∈[N] : ˆqi +β i ≥q min }▷optimistic qualified set
8:g←k(t/N) α ▷target selection count
9:if ˆQ=∅then
10:I t ←a provider chosen uniformly at random from[N];π t ←c max
11:else ifm i < gfor somei∈ ˆQthen
12:I t ←a provider chosen uniformly at random from{i∈ ˆQ:m i < g};π t ←c max
13:else
14:I t ←argmin i∈ ˆQ

bi −c max βi

▷allocation rule, ties broken arbitrarily
15:P←c max βIt + minj∈ ˆQ\{It}

bj −c max βj

16:π t ←min{P, cmax}▷second-price payment
17:end if
18:The user pays providerI t the amountπ t
19:ProviderI t serves the query, returning a responseyt
20:Observe the scorer(x t, yt)and setˆqIt ← mIt ˆqIt +r(xt,yt) mIt +1 andm It ←m It + 1
21:ProviderI t may revise its standing bidbIt; all other bids are unchanged
22:end for
We cast the interaction among theN providers on the platform as a multi-stage game [Fudenberg and
Tirole, 1991]. In this game, each provideri is characterized by its score and cost distributionsθi = (P r i , Pc i )
on the user’s task, which need not be known even to the provider itself; we writeθ = (θ1, . . . , θN ).7 Moreover,
its action in the game corresponds to choosing a bidding strategyσi that determines its standing bidbi,t based
on its observed historyHi,t, which collects the costsci,τ and scores r(xτ , yτ )of every query that provideri
has served before time stept,i.e.,8
bi,t =σ i(Hi,t)whereH i,t =

ci,τ , r(xτ , yτ )

τ <t:Iτ =i.(6)
In what follows, we denote the providers’ overall history asHt and say that provideri’s history Hi,t is
compatible withH t if it is contained inHt.
Crucially, although a provider does not necessarily know its true mean cost¯ci of serving a user query, it
can use its observed history to compute an estimate of the conditional mean cost of serving the next query,
E

ci,t |H i,t

. For ease of exposition, we focus on providers that compute this estimate as the empirical
average of past costs, given by
ˆci,t = 1 mi,t
t−1X
τ=1
ci,τ 1{I τ =i}.
In Appendix B, we show that Theorem 2 holds for any cost estimator and, if the platform widens the
cost radius cmaxβ(·)to(1 + γ)cmaxβ(·), Theorems 3 and 4 hold for providers that computeˆci,t through
7In the game theory literature, this corresponds to an incomplete-information setting in whichθi is the (private)typeof each
provider [Hossain, 2008, Feng et al., 2018, Harsanyi, 2004].
8Our theoretical results also hold if each provideri is allowed to use a time-varying bidding strategyσi,t. This is because, as we
will show later, our notion of bidding strategy optimality applies to any arbitrary strategy at any timet. However, to lighten
the notation, we focus on time-invariant bidding strategies mapping histories to bids.
5

Bayesian estimators whose estimates deviates from the empirical mean by at most a constant multipleγ of
the confidence radius.
Then, at time stept > N, the utility that a provideri expects to receive from participating in the platform
under any possible historyHt that is compatible with its observed historyHi,t is the conditional average of
payments received minus the mean cost it estimates to incur by serving queries over the remaining horizon
fromttoT,i.e.,
Ui|Ht (σi,σ −i;θ −i, T) =E
" TX
s=t
(πs −ˆci,s)·1{I s =i} |Ht
#
,(7)
where σ−i = (σj)j̸=i denotes the strategies of all providers other thani, and the expectation is over the
randomness in the providers’ generations conditional on the historyHt, which depends implicitly onθ.
Having formalized the providers’ interaction as a game, we now turn to characterizing their equilibrium
bidding strategies. Specifically, since a provider i knows neither the score and cost distributions θ−i
characterizing the other providers nor the total number of user queriesT, we focus on strategies that
maximize its utility under this uncertainty using the framework of robust game theory [Aghassi and Bertsimas,
2006]. Formally, the next theorem shows that the strategyσ∗ i that bids the provider’s cost estimate for the
next query,i.e.,
σ∗ i (Hi,t) = ˆci,t,(8)
offers every provider the best worst-case utility over its uncertainty aboutθ−i and T for any given historyHt
that is compatible with its observed historyHi,t.
Theorem 2.For any provider i∈ [N ], any strategy profileσ−i of all other providers, and any historyHt
witht > Nthat is compatible with provideri’s observed historyHi,t, the strategyσ∗ i satisfies:
i) for everyT≥tandθ −i,U i|Ht (σ∗ i ,σ −i;θ −i, T)≥0;
ii) for everyσ i,inf T≥t,θ −i Ui|Ht (σ∗ i ,σ −i;θ −i, T)≥inf T≥t,θ −i Ui|Ht (σi,σ −i;θ −i, T);
iii) for everyσ i, ifS t =∅,i∈ ˆQt and(σ ∗ i (Hi,t)−P i,t)(σi(Hi,t)−P i,t)<0, the inequality in ii) is strict.
In the above theorem, claim i) states thatσ∗ i never incurs an expected loss, and it holds because a provider
bidding its cost estimate serves a query only when the payment covers that estimate. Claim ii) states that
σ∗ i maximizes the worst-case utility, and it holds because a provider who does not knowT cannot rule out
that the current query is the last one; consequently, the worst-case utility of any strategy is bounded above
by its net payment from the current query. Moreover, underσ∗ i, the worst-case utility matches this upper
bound exactly because, by claim i), no later query can reduce it. Since this worst-case scenario effectively
isolates the current query, and because the payment does not depend on the provider’s own bid, the optimal
bid is the lowest possible value that avoids an expected loss—which is precisely the provider’s cost estimate.
Claim iii) states that any deviation changing whether the provider is assigned the query yields a strictly lower
worst-case utility, and it holds because, if the current query happens to be the last one, such a deviation
either causes the provider to forgo a profitable query or forces it to serve an unprofitable one.
Furthermore, as an immediate consequence of Theorem 2, the choice of bidding strategiesσ∗ = (σ∗ 1, . . . , σ∗ N )
is a robust equilibrium,i.e., for everyσi
inf
T≥t,θ −i
Ui|Ht (σ∗ i ,σ ∗ −i;θ −i, T)≥inf T≥t,θ −i Ui|Ht (σi,σ ∗ −i;θ −i, T).(9)
In words, at every stept > Nand after every history, no provideri can improve its worst-case utility by
deviating fromσ ∗ i when the other providers followσ∗ −i.
4 Finding the Lowest Competitive Inference Price
In this section, we show that, when all providers choose their equilibrium strategyσ∗ i, the user is served by a
provider meeting their quality thresholdqmin on all but a vanishing fraction of the queries, while the price
6

they pay converges to the most competitive price the market can offer for their task. For concreteness, in the
remainder of the section, we specify the functiong(t)to be of the formg(t) = k(t/N)α, where α∈ (0, 1)and
k >0are given parameters.
We begin by identifying the provider that serves most of the user’s queries. More precisely, we show that,
on all but a vanishing fraction of queries, the platform selects the qualified provideri∗ with the lowest cost,
i.e.,
i∗ = argmin
i∈Q
¯ci,(10)
which we refer to as the optimal provider and assume to be unique. The number of queries not served by
the optimal provider depends on the specific parametersα and k chosen by the platform as well as on the
difficulty of distinguishing each provider fromi∗, which we characterize using two quantities for each provider.
First, for an unqualified provideri /∈ Q, we letεi = qmin −q i > 0measure how far its quality falls below the
quality threshold. Second, for a qualified provideri∈ Q \ {i∗}, we let∆i = ¯ci −¯ci∗ > 0measure how far
its mean cost exceeds that ofi∗. Intuitively, the smallerεi or∆ i, the harder the corresponding provider is
to distinguish fromi∗, and the more queries the platform may allocate to them, as formalized in the next
theorem.
Theorem 3.When all providers choose their equilibrium strategyσ∗, with probability at least1−δ , the
number of time steps in which the platform does not assign the query to the lowest-cost qualified provider,i.e.,
It ̸=i ∗, is at mostN−1 +B id(T), where
Bid(T) :=
X
i /∈Q
M(ε i) +
X
i∈Q\{i∗}
max

M
 ∆i
cmax

, k·
 T
N
α
,(11)
where, for anyx >0,
M(x) =
 4
x2 ln
 57N
δx4

.
In the above theorem, the bound consists of theN− 1initialization steps not served byi∗ alongside a
sum of per-provider terms. For an unqualified provider, the term grows as1/ε2 i up to logarithmic factors.
Conversely, for a qualified provider other thani∗, the term is determined by the maximum of two terms: a
term growing as1/∆2 i that bounds the steps in which it outbidsi∗ and a termk(T /N)α that bounds the
exploration steps in which it is selected. Crucially, this bound depends sublinearly on the total number of
queries T. Hence, the platform allocates the query to the optimal provider on all but a vanishing fraction of
the user’s queries.
We now turn to the price the user pays on the platform for a query,i.e., the paymentπt made to the
provider serving it. More concretely, we focus on comparing this payment with the second-lowest mean
cost among qualified providers,¯c(2) = mini∈Q\{i∗} ¯ci. This cost represents the most competitive (average)
price the user could hope to pay for a query: it is the lowest price the optimal provideri∗ would need to
offer to remain cheaper than every other qualified provider, since the next-cheapest cannot profitably offer
a price below its own mean cost¯c(2). The next theorem shows that the average payment converges to the
second-lowest mean cost among qualified providers.
Theorem 4.When all providers choose their equilibrium strategyσ∗ and the user submits a minimum
numberT 0 of queries, with probability at least1−δthe payments made by the user satisfy
1
T
TX
t=1

πt −¯c(2)

 ≤ T0 T cmax +k  N T 1−α  cmax −¯c(2) 
+ 6c max
2−α
vuut 1
2k
 N
T
α
ln

2π2N k2
3δ
 T
N
2α!
,(12)
whereT 0 =Nmax

1,( ¯M /k)1/α	 and ¯M= max  1,max i /∈QM(ε i) 	 . Hence, 1 T PT t=1 πt →¯c(2) asT→ ∞.
7

BenchmarkN q min |Q|i ∗ ¯ci∗ ¯vi∗ ¯c(2) Paymentπ t Margin Share ofi ∗
GSM8K9 0.764 3Qwen2.5-3B16.1 20.1 34.4 30.3 (27.5)71%0.96
GPQA4 0.145 2Llama-3.1-8B43.0 53.8 50.7 48.3 (47.4)10%0.97
Table 1:Our procurement platform on queries fromGSM8K and GPQA.The table reports the number
of simulated providersN, the quality thresholdqmin, the number of qualified providers|Q|, the most cost-
competitive provideri∗ and its mean cost¯ci∗ and price ¯vi∗, the mean cost of the second most cost-competitive
provider ¯c(2), the average paymentπt over all steps and, in parentheses, over non-exploration steps, the
average pricing margin of the winner over non-exploration steps, and the share of queries routed toi∗. The
last three quantities are computed over the lastK queries, averaged across30independent runs, where K is
the size of the benchmark. Monetary quantities are in units of10−6 USD.
In the above theorem, the first term accounts for the firstT0 time steps, which include theN initialization
steps and the non-exploration steps during which an unqualified provider may still belong toˆQt; the second
term accounts for the exploration steps afterT0, in which the selected provider is paidcmax; and the third
term accounts for the remaining steps. AsT grows, the average difference between the payment and the
second-lowest mean cost¯c(2) of a qualified provider vanishes at a ratemax{T −(1−α), T−α/2}, up to logarithmic
factors. In Corollary 12 in Appendix A.9, we show that this rate is maximized when the platform sets
α= 2/3, giving a rate ofT −1/3.
5 Experiments
In this section, we evaluate our platform on simulated providers serving real LLMs from theLlama and Qwen
families. Specifically, we evaluate whether the platform learns the set of qualified providers and progressively
routes queries to the optimal provideri∗. We then compare the price paid on our platform against the average
per-token price listed by inference providers on Hugging Face9. Appendix D and Appendices E–G contain
further details on our experimental setup and additional experimental results, respectively.
Experimental setup.Each of the N simulated providers serves one LLM, which we use to identify
them. We consider two settings: (i) N = 9providers, each serving a model from the Llama family
(Llama-{3-8B, 3.1-8B, 3.2-1B, 3.2-3B}-Instruct ) or theQwen family (Qwen-{2-0.5B, 2-1.5B, 2-7B,
2.5-3B, 2.5-7B}-Instruct ), and (ii) N = 4providers serving the newest of the largest models and the
smallest model of each family,i.e.,Llama-3.1-8B,Llama-3.2-1B,Qwen2.5-7BandQwen2-0.5B.
In both settings, the user’s queries are drawn from one of two widely used benchmarks. In the setting with
N = 9providers, we draw queries from theGSM8K dataset [Cobbe et al., 2021], which consists ofK = 1,319
grade-school mathematical reasoning problems. In the setting withN = 4providers, we draw queries from
the GPQA [Rein et al., 2024] dataset, which consists ofK = 546graduate-level science questions. Both
benchmarks feature verifiable ground-truth answers, and the scorer(xt, yt)represents whether the response
is correct (1) or incorrect (0). Consequently, the qualityqi of a provider corresponds to the probability
that the model generates a correct answer. We rely on a public dataset of recorded generations,10 which
contains128generations per model for every question across both benchmarks. In each experiment, we
simulate T = 70,000queries by taking53 .07and128 .21passes over all queries inGSM8K and GPQA, respectively,
sampling without replacement. At each step, once a provider is selected, its response is sampled uniformly at
random from its128recorded generations for that query. We repeat each experiment across30independent
runs to report averaged results.
Since the public dataset we use lacks generation costs, we construct them using real-world market signals.
In particular, the cost of each recorded generation is determined by its token count and the model’s average per-
token price on the Hugging Face inference-provider list—on the order of$0.1per million tokens—discounted
by a fixed25%margin (i.e., divided by1.25), common to all providers and unknown to the platform (see
9https://huggingface.co/docs/inference-providers/index, consulted on December 30, 2025.
10https://huggingface.co/datasets/Human-Centric-Machine-Learning/strategic-ttc-data
8

Payment in non-exploration steps
Winning bid
¯c(2): second-lowest qualiﬁed cost
Payment πt
Query price of the same generations
¯vi∗ : listed query price of i∗
Generation cost
¯ci∗ : cost of i∗
101 102 103 104
Time step t
0
10
20
30
40
50Amount per query
one pass Tid
¯c(2) = 34 .4
¯vi∗ = 20 .1
¯ci∗ = 16 .1
(a)GSM8K, weak competition
101 102 103 104
Time step t
0
20
40
60
80Amount per query
one pass
¯c(2) = 50 .7
¯vi∗ = 53 .8
¯ci∗ = 43 .0 (b)GPQA, strong competition
Figure 1:Temporal evolution of the winning bids, payments, and costs.For each reported quantity,
every point corresponds to the median over30independent runs of a moving average whose window size
equals the benchmark sizeK, and the shaded regions span the10th to90th percentiles across runs. The
vertical lines mark one complete pass over the benchmark queries and, where applicable within the time
horizon, the time stepTid beyond which Theorem 3 guarantees thati∗ becomes the unique most selected
provider. Amount per query is in units of10−6 USD.
Appendix D, Table 2). We define¯vi = 1.25 ¯ci as the mean query price of provideri, representing the average
amount a user pays per query under publicly listed prices. Further, we place the quality thresholdqmin at the
midpoint between two adjacent provider qualities, so that three providers qualify onGSM8K and two onGPQA.
We purposely choose these two settings to vary the intensity of competition among qualified providers,
which fundamentally determines the user’s final payment. Specifically, since the average payment converges
to the second-lowest mean cost¯c(2) among qualified providers by Theorem 4, we call competition strong
when ¯c(2) is smaller than the listed query price of the optimal provider¯vi∗, and weak otherwise. OnGSM8K,
the qualified competitors ofi∗ are considerably more expensive (¯c(2) >¯vi∗, weak), whereas onGPQA, the sole
competitor is only slightly more expensive (¯c(2) <¯vi∗, strong). Table 1 summarizes both settings.
The platform runs Algorithm 1 with confidence levelδ = 0.05and exploration function g(t) = k(t/N)α,
with k = 2and α = 3/4. We choose this value over the rate-optimalα = 2/3from Corollary 12 to induce
greater early exploration at the expense of a slower asymptotic rate. Under this setup, the simulated providers
follow their equilibrium strategyσ∗.
Results.Table 1 summarizes our main results. We find that the platform successfully identifies the optimal
provider: over the final pass of the benchmark, it routes at least96%of all queries toi∗, and i∗ becomes
the most selected provider after roughly10,000and30 ,000queries on GSM8K and GPQA respectively. In both
cases, this occurs well before the time stepTid = min{T : T > N+ 2Bid(T )},i.e., the time step beyond
which Theorem 3 guarantees, with probability at least1−δ , that i∗ is the unique most-selected provider
(63,740and153 ,697queries, respectively; see Appendices E.1 and G.1). This gap demonstrates that our
sample complexity bounds are highly conservative in practice. The delayed convergence onGPQA stems from
the presence of the unqualifiedLlama-3.2-1B model; because its quality falls a mere0.037below qmin, the
platform requires approximately11,000queries to statistically exclude it from ˆQt.
Figure 1 provides additional insight into the temporal evolution of the winning bids, payments and costs.
In agreement with Theorem 4, we find that, for the initial queries, the payment on non-exploration steps lies
below ¯ci∗; this occurs because cheaper, unqualified providers that the platform has not yet excluded from ˆQt are still selected and influence the pricing mechanism. However, as the platform routes more queries,
9

the payment converges towards¯c(2). Importantly, we also find that the user’s payment for a guaranteed
quality level is fundamentally determined by the intensity of competition among qualified providers on
each benchmark. On the final pass, under strong competition onGPQA, the average payment per query on
non-exploration steps lies10%above the generation cost ¯ci∗ and12%below the listed price ¯vi∗ that the
user would pay in the current fixed-price market. Conversely, under weak competition onGSM8K, the average
payment lies71%above ¯ci∗ and37%above ¯vi∗, due to the higher cost of the nearest qualified competitor.
Altogether, the results suggest that our platform allows users to pay a price that approaches the one supported
by provider competition on their specific task, capturing substantial savings whenever the market-clearing
price falls below public fixed listings.
6 Discussion and Limitations
In this section, we highlight several limitations of our work and discuss avenues for future research.
Methodology.We assume that a provider maximizes its worst-case utility by bidding its current cost
estimate, since it knows neither the total number of user queries nor the score and cost distributions of its
competitors. However, because providers may violate this assumption in practice, we extend our theoretical
results in Appendix C to a setting where bids can deviate above or below the cost estimate by bounded
amounts. In this context, analyzing our platform using other game-theoretic solution concepts remains an
interesting direction for future work. Further, whenever the cost difference across providers is small, or the
providers’ quality sits right on the threshold, our platform requires a relatively large number of queries to
secure the best price for the user. In such cases, future work could lower query requirements by leveraging
quality and cost estimates across tasks. Finally, in our platform, users carry the cost of exploration. However,
because the most cost-competitive provider directly benefits from this exploration, one may argue that this
burden should be shifted to, or at least shared with, the providers, who typically possess greater financial
resources. Exploring alternative payment rules that redistribute such a burden represents an interesting
direction for future work.
Evaluation.We evaluated our platform using simulated providers who compete to serve queries from
benchmarking datasets with verifiable ground truth. An important next step would be to evaluate our
platform in settings where providers compete to serve open-ended queries and quality is measured automatically
without relying on predefined correct outputs. Further, in our experiments, we estimated the generation costs
by discounting publicly listed token prices by a fixed25%profit margin. Future research should leverage
specialized profiling tools to measure these true costs precisely. Ultimately, deploying and evaluating the
proposed platform in a real-world production environment remains crucial.
Practical considerations.We assume that our platform can accurately estimate the quality of the responses
generated by the providers. In many domains where LLMs are routinely used, such as coding or mathematical
reasoning, automated evaluation procedures make this feasible with minimal overhead. Moving forward, the
viability of our platform in settings with less well-established quality metrics and benchmarks will depend on
continued progress in the LLM evaluation literature. Lastly, we note that, while second-price auctions possess
many desirable properties, they also make a provider’s payment dependent on the bids of its competitors.
This dependence leaves the mechanism potentially vulnerable to manipulation or collusion [Hendricks and
Porter, 1989, Mailath and Zemsky, 1991, Che et al., 2018].
7 Conclusions
In this work, we introduced a procurement platform that connects large language model providers with
end-users, where token prices are driven by provider competition via reverse second-price auctions. More
concretely, this mechanism incentivizes providers to truthfully bid their best estimate of the average cost to
serve a user’s query. We demonstrated that, with high probability, the platform routes all but a vanishing
fraction of the user’s queries to the most cost-competitive provider meeting a desired quality threshold.
Moreover, this provider’s average pricing margin converges to the difference between the second-lowest average
10

cost among such providers and its own average cost. Empirically, we demonstrated that the pricing margin on
our platform varies significantly—from10%to71%—depending on the task and quality threshold, revealing
a substantial inefficiency in the current fixed-price market. Ultimately, we hope that our work inspires users,
providers, and routing platforms to explore alternative, more efficient economic paradigms for the market of
LLM-as-a-service.
Acknowledgements.We thank Stratis Tsirtsis for feedback and fruitful discussions. Gomez-Rodriguez
acknowledges support from the European Research Council (ERC) under the European Union’s Horizon 2020
research and innovation programme (grant agreement No. 101169607).
References
Paul Milgrom and John Roberts. Predation, reputation, and entry deterrence.Journal of Economic Theory, 27
(2):280–312, 1982. ISSN 0022-0531. doi: https://doi.org/10.1016/0022-0531(82)90031-X. URL https://www.
sciencedirect.com/science/article/pii/002205318290031X.
Rafid Mahmood. Pricing and Competition for Generative AI. InThe Thirty-eighth Annual Conference on Neural
Information Processing Systems, 2024. URLhttps://openreview.net/forum?id=8LbJfEjIrT.
Dirk Bergemann, Alessandro Bonatti, and Alex Smolin. Menu pricing of large language models.arXiv preprint
arXiv:2502.07736, 2025a.
Manish Raghavan. Competition and Diversity in Generative AI.arXiv preprint arXiv:2412.08610, 2024.
Emanuele La Malfa, Aleksandar Petrov, Simon Frieder, Christoph Weinhuber, Ryan Burnell, Raza Nazar, Anthony
Cohn, Nigel Shadbolt, and Michael Wooldridge. Language-models-as-a-service: Overview of a new paradigm and
its challenges.Journal of Artificial Intelligence Research, 80:1497–1523, 2024.
Benjamin Laufer, Jon Kleinberg, and Hoda Heidari. Fine-Tuning Games: Bargaining and Adaptation for General-
Purpose Models. InProceedings of the ACM Web Conference 2024, WWW ’24, page 66–76, New York, NY,
USA, 2024. Association for Computing Machinery. ISBN 9798400701719. doi: 10.1145/3589334.3645366. URL
https://doi.org/10.1145/3589334.3645366.
Dirk Bergemann, Alessandro Bonatti, and Alex Smolin. The economics of large language models: Token allocation,
fine-tuning, and optimal pricing. InProceedings of the 26th ACM Conference on Economics and Computation,
EC ’25, page 786, New York, NY, USA, 2025b. Association for Computing Machinery. ISBN 9798400719431. doi:
10.1145/3736252.3742625. URLhttps://doi.org/10.1145/3736252.3742625.
Ricardo Olmedo, Bernhard Schölkopf, and Moritz Hardt. Computational Arbitrage in AI Model Markets. InForty-third
International Conference on Machine Learning, 2026. URLhttps://openreview.net/forum?id=0xUvKZSQxV.
Ander Artola Velasco, Stratis Tsirtsis, and Manuel Gomez-Rodriguez. Auditing pay-per-token in large language
models. InThe 29th International Conference on Artificial Intelligence and Statistics, 2026a.
Ander Artola Velasco, Stratis Tsirtsis, Nastaran Okati, and Manuel Gomez Rodriguez. Is Your LLM Overcharging
You? Tokenization, Transparency, and Incentives. InForty-third International Conference on Machine Learning,
2026b. URLhttps://openreview.net/forum?id=aGaBFE9pta.
Ander Artola Velasco, Dimitrios Rontogiannis, Stratis Tsirtsis, and Manuel Gomez-Rodriguez. Test-Time Compute
Games, 2026c. URLhttps://arxiv.org/abs/2601.21839.
Junlin Wang, Siddhartha Jain, Dejiao Zhang, Baishakhi Ray, Varun Kumar, and Ben Athiwaratkun. Reasoning
in token economies: Budget-aware evaluation of LLM reasoning strategies. In Yaser Al-Onaizan, Mohit Bansal,
and Yun-Nung Chen, editors,Proceedings of the 2024 Conference on Empirical Methods in Natural Language
Processing, pages 19916–19939, Miami, Florida, USA, November 2024a. Association for Computational Linguistics.
doi: 10.18653/v1/2024.emnlp-main.1112. URLhttps://aclanthology.org/2024.emnlp-main.1112/.
Michael J. Zellinger and Matt Thomson. Economic evaluation of llms, 2025. URLhttps://arxiv.org/abs/2507.
03834.
11

Mehmet Hamza Erol, Batu El, Mirac Suzgun, Mert Yuksekgonul, and James Zou. Cost-of-pass: An economic
framework for evaluating language models. InThe Fourteenth International Conference on Learning Representations,
2026. URLhttps://openreview.net/forum?id=vC9S20zsgN.
Lingjiao Chen, Chi Zhang, Yeye He, Ion Stoica, Matei Zaharia, and James Zou. The price reversal phenomenon:
When cheaper reasoning models cost more.arXiv preprint arXiv:2603.23971, 2026a.
R Preston McAfee and John McMillan. Bidding for contracts: A principal-agent analysis.Rand J. Econ., 17(3):326,
1986.
John O Ledyard. Incentive compatibility. InThe New Palgrave dictionary of economics, pages 1–9. Springer, 1987.
Yeon-Koo Che. Design competition through multidimensional auctions.The RAND Journal of Economics, 24(4):
668–680, 1993. ISSN 07416261. URLhttp://www.jstor.org/stable/2555752.
Ziv Bar-Yossef, Kirsten Hildrum, and Felix Wu. Incentive-compatible online auctions for digital goods. InSODA,
volume 2, pages 964–970, 2002.
Tim Roughgarden, Vasilis Syrgkanis, and Eva Tardos. The price of anarchy in auctions.Journal of Artificial
Intelligence Research, 59:59–101, 2017.
Mohammad Akbarpour and Shengwu Li. Credible auctions: A trilemma.Econometrica, 88(2):425–467, 2020.
Yu Awaya, Naoki Fujiwara, and Marton Szabo. Quality and price in scoring auctions.Journal of Mathematical
Economics, 116:103083, 2025. ISSN 0304-4068. doi: https://doi.org/10.1016/j.jmateco.2024.103083. URLhttps:
//www.sciencedirect.com/science/article/pii/S0304406824001435.
Yuhang Cai and Huchang Liao. An overview of multi-attribute auctions: bibliometrics, methodologies, applications
and future directions.Expert Systems with Applications, 299:130083, 2026. ISSN 0957-4174. doi: https://doi.org/
10.1016/j.eswa.2025.130083. URLhttps://www.sciencedirect.com/science/article/pii/S0957417425036991.
Tanjim Hossain. Learning by bidding.The RAND Journal of Economics, 39(2):509–529, 2008. ISSN 07416261. URL
http://www.jstor.org/stable/25474380.
Alessandro Pavan, Ilya Segal, and Juuso Toikka. Dynamic mechanism design: A myersonian approach.Econometrica,
82(2):601–653, 2014. ISSN 00129682, 14680262. URLhttp://www.jstor.org/stable/24029270.
Jonathan Weed, Vianney Perchet, and Philippe Rigollet. Online learning in repeated auctions. In Vitaly Feldman,
Alexander Rakhlin, and Ohad Shamir, editors,29th Annual Conference on Learning Theory, volume 49 ofProceedings
of Machine Learning Research, pages 1562–1583, Columbia University, New York, New York, USA, 23–26 Jun 2016.
PMLR. URLhttps://proceedings.mlr.press/v49/weed16.html.
Zhe Feng, Chara Podimata, and Vasilis Syrgkanis. Learning to bid without knowing your value. InProceedings
of the 2018 ACM Conference on Economics and Computation, EC ’18, page 505–522, New York, NY, USA,
2018. Association for Computing Machinery. ISBN 9781450358293. doi: 10.1145/3219166.3219208. URLhttps:
//doi.org/10.1145/3219166.3219208.
Dirk Bergemann and Juuso Välimäki. Dynamic mechanism design: An introduction.J. Econ. Lit., 57(2):235–274,
June 2019.
Dirk Bergemann, Marek Bojko, Paul Duetting, Renato Paes Leme, Haifeng Xu, and Song Zuo. Data-driven mechanism
design: Jointly eliciting preferences and information. InProceedings of the 26th ACM Conference on Economics
and Computation, EC ’25, page 507, New York, NY, USA, 2025c. Association for Computing Machinery. ISBN
9798400719431. doi: 10.1145/3736252.3742578. URLhttps://doi.org/10.1145/3736252.3742578.
Peter Auer, Nicolò Cesa-Bianchi, and Paul Fischer. Finite-time analysis of the multiarmed bandit problem.Mach.
Learn., 47(2-3):235–256, May 2002.
Eyal Even-Dar, Shie Mannor, and Yishay Mansour. Action elimination and stopping conditions for the multi-armed
bandit and reinforcement learning problems.Journal of Machine Learning Research, 7(39):1079–1105, 2006. URL
http://jmlr.org/papers/v7/evendar06a.html.
12

Moshe Babaioff, Yogeshwer Sharma, and Aleksandrs Slivkins. Characterizing truthful multi-armed bandit mechanisms.
InProceedings of the 10th ACM conference on Electronic commerce, pages 79–88, New York, NY, USA, July 2009.
ACM.
Sébastien Bubeck and Nicolò Cesa-Bianchi. Regret analysis of stochastic and nonstochastic multi-armed bandit
problems.Found. Trends®Mach. Learn., 5(1):1–122, December 2012.
Shweta Jain, Sujit Gujar, Satyanath Bhat, Onno Zoeter, and Y. Narahari. An incentive compatible multi-armed-bandit
crowdsourcing mechanism with quality assurance, 2015. URLhttps://arxiv.org/abs/1406.7157.
Mark Braverman, Jieming Mao, Jon Schneider, and S. Matthew Weinberg. Multi-armed bandit problems with strategic
arms. In Alina Beygelzimer and Daniel Hsu, editors,Proceedings of the Thirty-Second Conference on Learning
Theory, volume 99 ofProceedings of Machine Learning Research, pages 383–416. PMLR, 25–28 Jun 2019. URL
https://proceedings.mlr.press/v99/braverman19b.html.
Tor Lattimore and Csaba Szepesvári.Bandit algorithms. Cambridge University Press, Cambridge, England, July 2020.
Rupert Freeman, David Pennock, Chara Podimata, and Jennifer Wortman Vaughan. No-regret and incentive-
compatible online learning. In Hal Daumé III and Aarti Singh, editors,Proceedings of the 37th International
Conference on Machine Learning, volume 119 ofProceedings of Machine Learning Research, pages 3270–3279.
PMLR, 13–18 Jul 2020. URLhttps://proceedings.mlr.press/v119/freeman20a.html.
Divya Padmanabhan, Satyanath Bhat, K J Prabuchandran, Shirish Shevade, and Y Narahari. Dominant strategy
truthful, deterministic multi-armed bandit mechanisms with logarithmic regret for sponsored search auctions.Appl.
Intell., 52(3):3209–3226, February 2022.
Adish Singla and Andreas Krause. Truthful incentives in crowdsourcing tasks using regret minimization mechanisms.
InProceedings of the 22nd international conference on World Wide Web, New York, NY, USA, May 2013. ACM.
Yiling Chen, Shi Feng, and Sadie Zhao. Contextual procurement auctions with bandit learning.arXiv preprint
arXiv:2607.05813, 2026b.
Pronoy Patra, Sankarshan Damle, Manisha Padala, and Sujit Gujar. Truthful reverse auctions for adaptive selection
via contextual multi-armed bandits. InProceedings of the 25th International Conference on Autonomous Agents
and Multiagent Systems, AAMAS ’26, page 578–586, Richland, SC, 2026. International Foundation for Autonomous
Agents and Multiagent Systems. ISBN 9798400723179. doi: 10.65109/MBRQ7564. URLhttps://doi.org/10.
65109/MBRQ7564.
Yuhan Cao, Yu Wang, Sitong Liu, Miao Li, Yixin Tao, and Tianxing He. Pay for the second-best service: A
game-theoretic approach against dishonest llm providers. InProceedings of the ACM Web Conference 2026, WWW
’26, page 249–260, New York, NY, USA, 2026. Association for Computing Machinery. ISBN 9798400723070. doi:
10.1145/3774904.3792446. URLhttps://doi.org/10.1145/3774904.3792446.
William Vickrey. Counterspeculation, auctions, and competitive sealed tenders.The Journal of Finance, 16(1):8–37,
1961. ISSN 00221082, 15406261. URLhttp://www.jstor.org/stable/2977633.
Noam Nisan, Tim Roughgarden, Eva Tardos, and Vijay V Vazirani, editors.Algorithmic game theory. Cambridge
University Press, Cambridge, England, January 2011.
Drew Fudenberg and Jean Tirole.Game Theory. MIT Press, 1991.
John C. Harsanyi. Games with incomplete information played by "bayesian" players, i-iii: Part i. the basic model.
Management Science, 50(12):1804–1817, 2004. ISSN 00251909, 15265501. URLhttp://www.jstor.org/stable/
30046151.
Michele Aghassi and Dimitris Bertsimas. Robust game theory.Math. Program., 107(1–2):231–273, June 2006. ISSN
0025-5610. doi: 10.1007/s10107-005-0686-0. URLhttps://doi.org/10.1007/s10107-005-0686-0.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert,
Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, and John Schulman. Training verifiers to solve
math word problems, 2021. URLhttps://arxiv.org/abs/2110.14168.
13

David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael,
and Samuel R. Bowman. GPQA: A graduate-level google-proof q&a benchmark. InFirst Conference on Language
Modeling, 2024. URLhttps://openreview.net/forum?id=Ti67584b98.
Kenneth Hendricks and Robert H. Porter. Collusion in auctions.Annales d’Économie et de Statistique, (15/16):
217–230, 1989. ISSN 0769489X, 22726497. URLhttp://www.jstor.org/stable/20075758.
George J Mailath and Peter Zemsky. Collusion in second price auctions with heterogeneous bidders.Games and
Economic Behavior, 3(4):467–486, 1991. ISSN 0899-8256. doi: https://doi.org/10.1016/0899-8256(91)90016-8. URL
https://www.sciencedirect.com/science/article/pii/0899825691900168.
Yeon-Koo Che, Daniele Condorelli, and Jinwoo Kim. Weak cartels and collusion-proof auctions.Journal of
Economic Theory, 178:398–435, 2018. ISSN 0022-0531. doi: https://doi.org/10.1016/j.jet.2018.09.005. URL
https://www.sciencedirect.com/science/article/pii/S0022053118305842.
Haoxiang Wang, Wei Xiong, Tengyang Xie, Han Zhao, and Tong Zhang. Interpretable preferences via multi-objective
reward modeling and mixture-of-experts, 2024b. URLhttps://arxiv.org/abs/2406.12845.
14

A Proofs
A.1 Concentration inequalities for the qualities and costs
In this section, we characterize the relationship between the estimated confidence setsˆQt, introduced in
Eq. 2, and the setQ of qualified providers. To this end, we first define a high-probability event under which,
for every provider and every selection count, the empirical quality and cost averages are simultaneously close
to their corresponding population averages. For each provideri∈ [N ]and m≥ 1, let ˆqi,m and ˆci,m denote
the empirical means of the scores and generation costs observed over the firstm queries served by provideri,
respectively. Recall that
β(m) =
s
1
2m ln
 2π2N m2
3δ

.
Lemma 1.LetEdenote the event that, simultaneously for every provideri∈[N]and everym≥1,
|ˆqi,m −q i| ≤β(m),|ˆc i,m −¯ci| ≤cmaxβ(m).(13)
Then,Pr(E)≥1−δ.
Proof. Fix a provideri∈ [N ], and letτi(1) < τi(2) <· · ·denote the steps in which provideri is selected.
Since the platform selects a provider before the score and generation cost of that step are realized, the
successive observations
r(xτi(1), yτi(1)), r(xτi(2), yτi(2)), . . .
are i.i.d. draws fromPr i with meanq i, and the successive realized costs
ci,τi(1), ci,τi(2), . . .
are i.i.d. draws fromP c i with mean ¯ci. Thus, for every fixed selection countm≥ 1, Hoeffding’s inequality
and the fact that scores lie in[0,1]give
Pr(|ˆqi,m −q i|> β(m))≤2 exp

−2mβ(m)2 .
Similarly, since generation costs lie in[0, cmax],
Pr(|ˆci,m −¯ci|> cmaxβ(m))≤2 exp

−2mβ(m)2 .
By the definition ofβ(m),
2 exp

−2mβ(m)2 = 3δ π2N m2 .
A union bound over the two estimates, all providers, and all selection counts therefore gives
Pr(E c)≤
NX
i=1
∞X
m=1
2 3δ π2N m2
= 6δ π2
∞X
m=1
1
m2 =δ,
where P∞ m=1 m−2 =π 2/6. Hence,
Pr(E)≥1−δ.
We next prove a technical result showing that a lower bound on the confidence radiusβ(m)implies an
upper bound on the selection countm. We will use this result in the proof of Lemma 7 and Lemma 8.
15

Lemma 2.For anya >0andm≥1, if
a≤2β(m),(14)
then
m≤ 4 a2 ln  57N δa4  .(15)
Proof.By (14) and the definition ofβ(m),
1
2m ln
 2π2N m2
3δ

≥ a2
4 .
Equivalently,
m≤ 2 a2 ln  2π2N m2 3δ  = 2 a2 ln  2π2N 3δ  + 4 a2 lnm.
Set
A= 2 a2 ln  2π2N 3δ  , B= 4 a2 ,
so thatm≤A+Blnm. For everyr >0, the inequalitylnx≤x−1gives
lnm= ln
 m
r

+ lnr≤ m r + lnr−1.
Hence, 
1− B r  m≤A+B(lnr−1).
Choosingr= 2B= 8/a 2 yields
m
2 ≤A+B

ln
 8
a2

−1

.
Therefore,
m≤2A+ 2B

ln
 8
a2

−1

= 4 a2

ln
 2π2N
3δ

+ 2 ln
 8
a2

−2

= 4 a2 ln  128π2N 3e2δa4 
≤ 4 a2 ln  57N δa4  ,
where the final inequality follows from128π2/(3e2)<57.
A.2 Properties of exploration steps
We next establish several basic properties of the allocation rule that will be used when proving the theoretical
results stated in Section 3 and Section 4.
Lemma 3.On E, every qualified provider remains in the estimated-qualified set at every post-initialization
step:
Q ⊆ˆQt, t > N.(16)
In particular, ˆQt ̸=∅for everyt > N.
16

Proof.Fixi∈ Qandt > N. Sinceiis qualified,
qi ≥q min.
OnE, Lemma 1 gives, for any provideriand time stept > N,
ˆqi,t ≥q i −β(m i,t).
Therefore,
ˆqi,t +β(m i,t)≥q i ≥q min,
and hence i∈ ˆQt by the definition of the estimated-qualified set. Since this holds for everyi∈ Q, we obtain
Q ⊆ˆQt. Finally, Q contains at least two providers by assumption, soˆQt is nonempty under the eventE.
Lemma 4.Suppose that g:N→R is non-decreasing, and fix a total number of user queriesT > N. If
provideriis selected in an exploration stept≤T, then
mi,t < g(t)≤g(T).(17)
Consequently, providerican be selected in an exploration step at most
⌈g(T)⌉ −1(18)
times, and the total number of post-initialization exploration steps up toTqueries is at most
N(⌈g(T)⌉ −1).(19)
Proof.If provideriis selected in an exploration stept, theni∈ S t. By definition ofSt,
mi,t < g(t).
Sincegis non-decreasing andt≤T,
mi,t < g(t)≤g(T),
which proves (17).
Now suppose thatt is an exploration step in which provideri is selected. Since mi,t is a positive integer
after initialization, (17) implies
mi,t ≤ ⌈g(T)⌉ −1.
Thus, provider i can therefore be selected in an exploration step at most⌈g(T )⌉ −1when the total number
of user queries isT. Summing this bound over allNproviders gives (19).
A.3 Properties of non-exploration steps
We next establish properties of the allocation rule on non-exploration steps, that is, whenSt = ∅ and the
selection of providerIt depends on the bidsbt. We begin by proving Proposition 1.
Proof of Proposition 1.
Proof of Proposition 1.Fix a time stept > Nwith St = ∅, a provideri∈ ˆQt, and the other providers’ bids
b−i,t. Since t is not an exploration step, the allocation rule (Eq. 3) selects a provider minimizing the adjusted
bid
bj,t −c maxβ(mj,t)(20)
overj∈ ˆQt.
17

Provideriis therefore selected whenever
bi,t −c maxβ(mi,t)<min
j∈ ˆQt\{i}
(bj,t −c maxβ(mj,t)).
Rearranging gives
bi,t < cmaxβ(mi,t) + min
j∈ ˆQt\{i}
(bj,t −c maxβ(mj,t)) =P i,t,
where the equality follows from the definition ofPi,t. Thusb i,t < Pi,t implies that provideriis selected.
Similarly, if
bi,t > Pi,t,
then
bi,t −c maxβ(mi,t)>min
j∈ ˆQt\{i}
(bj,t −c maxβ(mj,t)).
so provideridoes not minimize the adjusted bid and is therefore not selected. This proves the claim.
Lemma 5.Suppose that all providers use their equilibrium strategyσ∗. On E, for every provideri∈ [N ]
and every stept > N,
¯ci −2c maxβ(mi,t)≤b i,t −c maxβ(mi,t)≤¯ci.(21)
Proof.Fix a provideri∈[N]and a stept > N. Under the equilibrium strategyσ ∗,
bi,t = ˆci,t.
Thus, onE,
¯ci −c maxβ(mi,t)≤ˆci,t ≤¯ci +c maxβ(mi,t).(22)
Substitutingb i,t = ˆci,t and subtractingc maxβ(mi,t)yields
¯ci −2c maxβ(mi,t)≤b i,t −c maxβ(mi,t)≤¯ci.
which proves the claim.
Lemma 6.Suppose that all providers use their equilibrium strategyσ∗. On E, if a provideri∈ Q \ {i∗} is
selected at a non-exploration stept > N, then
∆i ≤2c maxβ(mi,t),(23)
where∆ i = ¯ci −¯ci∗ >0.
Proof. Fix a non-exploration stept > Nin which i∈ Q \ {i∗} is selected. Under the eventE, Lemma 3
implies thati ∗ ∈ ˆQt. Sincetis a non-exploration step, the allocation rule therefore implies
bi,t −c maxβ(mi,t)≤b i∗,t −c maxβ(mi∗,t).
Applying Lemma 5 to both providers gives
¯ci −2c maxβ(mi,t)≤b i,t −c maxβ(mi,t)≤b i∗,t −c maxβ(mi∗,t)≤¯ci∗ .
Hence,
¯ci −¯ci∗ ≤2c maxβ(mi,t).
Since∆ i = ¯ci −¯ci∗, this proves (23).
18

Lemma 7.Suppose that all providers use their equilibrium strategyσ∗. On E, if a provideri∈ Q \ {i∗} is
selected at a non-exploration stept > N, then
mi,t ≤L i :=
 4c2 max
∆2 i ln
 57N c4 max
δ∆4 i

.(24)
Consequently, oncem i,t > Li, providericannot be selected at a non-exploration step
Proof.By Lemma 6, if provideri∈ Q \ {i∗}is selected at a non-exploration stept > N, then
∆i ≤2c maxβ(mi,t).
Dividing byc max gives
∆i
cmax
≤2β(m i,t).
Applying Lemma 2 with
a= ∆i
cmax
therefore yields
mi,t ≤ 4c2 max ∆2 i ln  57N c4 max δ∆4 i  ≤L i.
Thus, ifm i,t > Li, providericannot be selected by the allocation rule at a non-exploration step.
A.4 Elimination of unqualified providers
We next bound the number of times an unqualified provider can be selected on the platform, including both
non-exploration and exploration steps.
Lemma 8.OnE, every unqualified provideri /∈ Q, with quality gap
εi :=q min −q i >0,
is selected at most
Mi :=
 4
ε2 i ln
 57N
δε4 i

(25)
times in post-initialization steps.
Proof. Fix an unqualified provideri /∈ Qand a post-initialization stept > Nin which It = i. Whether t is a
non-exploration or exploration step, providerican be selected only ifi∈ ˆQt. Hence,
ˆqi,t +β(m i,t)≥q min.
OnE, Lemma 1 gives
ˆqi,t ≤q i +β(m i,t).
Combining the two inequalities yields
qmin ≤q i + 2β(mi,t),
and therefore
εi ≤2β(m i,t).(26)
Applying Lemma 2 witha=ε i gives
mi,t ≤ 4 ε2 i ln  57N δε4 i  ≤M i.
Since this holds whenever provideri is selected in a post-initialization step, provideri is selected at mostMi
times after initialization. Consequently, oncemi,t > Mi, provider i cannot be selected at any stept > N.
19

A.5 Selection and identification bounds
We now bound the total number of times a qualified suboptimal provider can be selected.
Lemma 9.Suppose that all providers use their equilibrium strategyσ∗. On E, for every provideri∈ Q \ {i∗},
the number of post-initialization stepst≤Tin whichI t =iis at most
max{L i,⌈g(T)⌉ −1},(27)
whereL i is defined in Lemma 7.
Proof. Fix T > Nand a provideri∈ Q \ {i∗}, and consider any post-initialization stept≤T in which It = i.
Iftis a non-exploration step, Lemma 7 gives
mi,t ≤L i.
If insteadtis an exploration step, Lemma 4 gives
mi,t < g(t)≤g(T).
Sincem i,t is an integer,
mi,t ≤ ⌈g(T)⌉ −1.
Thus, in either case,
mi,t ≤max{L i,⌈g(T)⌉ −1}.
Since provider i is selected once during initialization andmi,t increases by one at each of its selections,
its ℓ-th post-initialization selection occurs at a stept with mi,t = ℓ. Hence, provider i is selected at most
max{Li,⌈g(T)⌉ −1}times in post-initialization stepst≤T.
Proof of Theorem 3.
Proof of Theorem 3.We work under the eventE, which by Lemma 1 occurs with probability at least1−δ .
In the firstN initialization steps, each provider is selected exactly once. Hence, at mostN− 1initialization
steps are not assigned toi∗.
We next consider the post-initialization steps. Every provideri̸ = i∗ is either unqualified or qualified and
suboptimal. By Lemma 8, each provideri /∈ Qis selected at most
Mi =
 4
ε2 i ln
 57N
δε4 i

=M(ε i)
times after initialization.
For each provideri∈ Q \ {i∗}, Lemma 9 gives at most
max{L i,⌈g(T)⌉ −1}
post-initialization selections, whereLi =M(∆ i/cmax)by Lemma 7 and, for
g(t) =k
 t
N
α
,
we have⌈g(T)⌉ −1 =⌈k(T /N)α⌉ −1.
Since every step withIt ̸= i∗ selects exactly one provider other thani∗, summing these bounds and adding
theN−1initialization steps gives
TX
t=1
1{I t ̸=i ∗} ≤N−1 + X
i /∈Q
Mi +
X
i∈Q\{i∗}
max{L i,⌈g(T)⌉ −1}
=N−1 +
X
i /∈Q
M(ε i) +
X
i∈Q\{i∗}
max

M
 ∆i
cmax

,

k
 T
N
α
−1

≤N−1 +B id(T),
20

which proves the claimed bound.
Corollary 5.Suppose that all providers use their equilibrium strategyσ∗. With probability at least1−δ,
1
T
TX
t=1
1{I t ̸=i ∗} − →0asT→ ∞.(28)
In particular, the platform assigns a fraction tending to one of the user’s queries to the lowest-cost qualified
provideri ∗.
Proof.On the eventE, Theorem 3 gives
TX
t=1
1{I t ̸=i ∗} ≤N−1 + X
i /∈Q
Mi +
X
i∈Q\{i∗}
max

Li, k
 T
N
α
.
Dividing byTyields
1
T
TX
t=1
1{I t ̸=i ∗} ≤N−1 + P i /∈QMi T + 1 T X i∈Q\{i∗} max  Li, k  T N α .
The quantitiesM i andL i are independent ofT. Moreover, sinceα∈(0,1),
k(T /N)α
T = k N α T α−1 T→∞ − − − − →0.
Hence every term on the right-hand side converges to zero, which proves(28). Since Pr(E) ≥ 1 −δ by
Lemma 1, the result holds with probability at least1−δ.
Corollary 6.Suppose that all providers use their equilibrium strategyσ∗. OnE, if at some stept > N,
mi,t > Mi for everyi /∈ Q,andm i,t > Li for everyi∈ Q \ {i∗},(29)
then every non-exploration stepτ≥tis assigned to the optimal provideri ∗.
Proof.Fix an ordinary stepτ≥t. Since selection counts are non-decreasing,
mi,τ > Mi for everyi /∈ Q, mi,τ > Li for everyi∈ Q \ {i∗}.
By Lemma 8, no unqualified provider can be selected at step τ. By Lemma 7, no qualified provider
i∈ Q \ {i∗} can be selected at non-exploration stepτ. Finally, Lemma 3 guarantees thati∗ ∈ ˆQτ. Hence, in
a non-exploration step, the allocation rule must selecti∗.
A.6 Generic cumulative counting and confidence-radius bounds
In this section, we establish a bound on sums of confidence radii along the sequence of selected providers.
This counting argument is independent of whether a step is exploratory or non-exploratory and will be used
in the proof of Theorem 7.
Lemma 10(Radius sum).FixT≥Nand let(a t)T t=N+1 be nonnegative numbers satisfying
at ≤κ β(mIt,t), t=N+ 1, . . . , T,
for someκ≥0. Then,
TX
t=N+1
at ≤κ
s
2N(T−N) ln
 2π2N T2
3δ

.(30)
21

Proof.For each provideri∈[N], let
Di =m i,T+1 −1
denote the number of times provideri is selected after initialization up to and including time stepT. Since
exactly one provider is selected at every post-initialization step,
NX
i=1
Di =T−N.
Therefore,
TX
t=N+1
at ≤κ
NX
i=1
DiX
ℓ=1
β(ℓ)
=κ
NX
i=1
DiX
ℓ=1
s
1
2ℓ ln
 2π2N ℓ2
3δ

.
Sinceℓ≤D i ≤T,
β(ℓ)≤
s
1
2ℓ ln
 2π2N T2
3δ

.
Hence,
TX
t=N+1
at ≤κ
s
1
2 ln
 2π2N T2
3δ
 NX
i=1
DiX
ℓ=1
1√
ℓ
≤κ
s
2 ln
 2π2N T2
3δ
 NX
i=1
p
Di,
where we usedPD ℓ=1 ℓ−1/2 ≤2 √ D. Finally, using the Cauchy–Schwarz inequality,
NX
i=1
p
Di ≤
vuutN NX
i=1
Di =
p
N(T−N).
Combining the preceding inequalities gives
TX
t=N+1
at ≤κ
s
2N(T−N) ln
 2π2N T2
3δ

,
as claimed.
A.7 User performance guarantees
We now derive the quality guarantees that the user obtains on the platform.
Theorem 7.On the eventE, the sum
Rqual T =
TX
t=1

qmin −q It
+
,
22

which measures the cumulative quality underqmin obtained by the user, satisfies,
Rqual T ≤min
(
N+ 2
s
2N(T−N) ln
 2π2N T2
3δ

,
X
i /∈Q

Mi + 1

εi
)
.(31)
Moreover, the number of queries assigned to unqualified providers satisfies,
TX
t=1
1{I t /∈ Q} ≤
X
i /∈Q
(Mi + 1).(32)
Consequently,
Rqual T
T =O
 1
T

− →0, 1 T
TX
t=1
1{I t /∈ Q}=O
 1
T

− →0(33)
Proof. In the first N initialization steps, every provider is selected once. Since( qmin −q i)+ ≤ 1, the
contribution of the firstNsteps to the sumR qual T is at mostN.
Consider now a post-initialization stept > N. If It ∈ Q, then qIt ≥q min and the step does not contribute
to the sumRqual T . If It /∈ Q, then the selected provider must belong toˆQt. In the proof of Lemma 8 (Eq. 26),
we showed that this implies that:
εIt =

qmin −q It
+
≤2β(m It,t).
Applying Lemma 10 withκ= 2therefore gives
TX
t=N+1

qmin −q It
+
≤2
s
2N(T−N) ln
 2π2N T2
3δ

.
Adding the initialization contribution proves the first bound in (31).
Alternatively, Lemma 8, the elimination bound for unqualified providers, shows that everyi /∈ Qis selected
at most Mi times after initialization. Including its initialization selection, provideri therefore contributes at
most
(Mi + 1)εi
to the cumulative quality regret. Summing over alli /∈ Qproves the second bound in (31).
The same selection bound immediately gives
TX
t=1
1{I t /∈ Q} ≤
X
i /∈Q
(Mi + 1).
proving (32).
Finally, the right-hand sides of the second bound in(31) and of(32) are independent ofT. Dividing both
inequalities byTtherefore gives (33).
We next bound the cumulative excess mean generation cost of the selected providers relative to the
optimal provider i∗, i.e., how much more the user’s queries cost to serve than they would if every query were
served byi ∗. We refer to this quantity as the generation-cost regret.
Theorem 8.Suppose that all providers use their equilibrium strategyσ∗. On the eventE, the sum
Rgen T =
TX
t=1

¯cIt −¯ci∗
+
23

satisfies
Rgen T ≤min
(
(N−1)⌈g(T)⌉c max + 2cmax
s
2N(T−N) ln
 2π2N T2
3δ

,
X
i /∈Q
(Mi + 1)

¯ci −¯ci∗
+
+
X
i∈Q\{i∗}

max{Li,⌈g(T)⌉ −1}+ 1

∆i
)
.(34)
Proof. Since every mean cost lies in[0, cmax], each term ofRgen T is at mostcmax, and it vanishes whenever
It =i ∗.
For the first bound, we partition the time steps up toT into initialization steps, exploration steps, and
non-exploration steps. During initialization, at mostN− 1steps are not assigned toi∗, which contribute at
most( N− 1)cmax. By Lemma 4, every provider is selected in at most⌈g(T )⌉ −1exploration steps, so the
exploration steps assigned to a provider other thani∗ contribute at most(N− 1)(⌈g(T )⌉ −1)cmax. Finally,
consider a non-exploration stept > Nwith It = i̸ = i∗. On E, Lemma 3 givesi∗ ∈ ˆQt, so the allocation rule
(Eq. 3) implies
bi,t −c maxβ(mi,t)≤b i∗,t −c maxβ(mi∗,t),
and Lemma 5, applied to both providers, yields¯ci − 2cmaxβ(mi,t) ≤¯ci∗. Hence, letting at = (¯cIt −¯ci∗ )+ on
non-exploration steps andat = 0on exploration steps, we haveat ≤ 2cmaxβ(mIt,t)for every t = N + 1, . . . , T,
and Lemma 10 withκ= 2c max gives
TX
t=N+1
at ≤2c max
s
2N(T−N) ln
 2π2N T2
3δ

.
Summing the three contributions proves the first bound.
For the second bound, Lemma 8 shows that everyi /∈ Qis selected at mostMi times after initialization,
and Lemma 9 shows that everyi∈ Q \ {i∗} is selected at mostmax{Li,⌈g (T )⌉ −1} times after initialization.
Including its initialization selection, each provideri̸ = i∗ therefore contributes at most its number of selections
times( ¯ci −¯ci∗ )+ to Rgen T , where( ¯ci −¯ci∗ )+ = ∆i for i∈ Q \ {i∗}. Summing overi̸ = i∗ proves the second
bound.
A.8 Payments on exploration and non-exploration steps
We next bound the payments made by the user. On an exploration step, the selected provider is paidcmax,
whereas on an non-exploration step the payment is determined by the adjusted bid of the cheapest competing
eligible provider.
Lemma 11.On E, suppose that all providers use their equilibrium strategyσ∗. For every non-exploration
stept > NwithI t =i,
πt ≤min

cmax,¯c(2) +c maxβ(mi,t)

.(35)
Consequently,
πt −¯c(2)
+
≤c maxβ(mi,t).(36)
Proof.Fix a non-exploration stept > NwithI t =i. Then, the payment rule (Eq. 5) gives
πt = min
(
cmaxβ(mi,t) + min
j∈ ˆQt\{i}
(bj,t −c maxβ(mj,t)), cmax
)
.
If i = i∗, let j be a second-cheapest qualified provider, so that¯cj = ¯c(2). If i̸ = i∗, let j = i∗, in which case
¯cj = ¯ci∗ ≤¯c(2). In either case,j∈ Qandj̸=iandj∈ ˆQt on the eventE. Moreover, using Lemma 5,
bj,t −c maxβ(mj,t)≤¯cj ≤¯c(2).
24

Therefore,
min
j′∈ ˆQt\{i}
(bj′,t −c maxβ(mj′,t))≤¯c(2),
and hence
πt ≤min

cmax,¯c(2) +c maxβ(mi,t)

.
The second claim follows immediately.
Theorem 9.OnE, when all providers use their equilibrium strategyσ∗,
TX
t=1

πt −¯c(2)
+
≤

N+N

⌈g(T)⌉ −1

cmax −¯c(2)

+c max
s
2N(T−N) ln
 2π2N T2
3δ

.(37)
Proof. Partition the time steps up toT into initialization steps, exploration steps, and non-exploration steps.
During initialization, each of theN providers is paidcmax, so the total excess payment contributed by
these steps is
N

cmax −¯c(2)

.
On every exploration step, the selected provider is also paidcmax. By Lemma 4, there are at most
N(⌈g(T)⌉ −1)such steps. Their total contribution is therefore at most
N

⌈g(T)⌉ −1

cmax −¯c(2)

.
Finally, on every non-exploration stept > N, Lemma 11 gives

πt −¯c(2)
+
≤c maxβ(mIt,t).
Hence, for the non-exploration steps, applying Lemma 10,
TX
t=N+1
tnon-exploration

πt −¯c(2)
+
≤c max
TX
t=N+1
β(mIt,t)
≤c max
s
2N(T−N) ln
 2π2N T2
3δ

.
Summing the three contributions proves (37).
Corollary 10.Suppose
g(t) =k
 t
N
α
, k >0, α∈(0,1).
OnE, when all providers use their equilibrium strategyσ∗,
1
T
TX
t=1

πt −¯c(2)
+
≤

N
T +k
 N
T
1−α!
cmax −¯c(2)

+c max
s
2N
T ln
 2π2N T2
3δ

.(38)
25

Proof.Since
g(T) =k
 T
N
α
,
the forced exploration term in Theorem 9 satisfies
N

⌈g(T)⌉ −1

≤N g(T) =kN
 T
N
α
(39)
Substituting this into (37) and dividing byTgives
N g(T)
T =k
 N
T
1−α
which proves the result.
A.9 Payment convergence
We finally show that, on non-exploration steps, the payment converges to¯c(2). Throughout, we write
¯M= max  1,max
i /∈Q
Mi

, T 0 =Nmax

1,( ¯M /k)1/α
so that every time stept > T0 comes after initialization and satisfiesg(t)> ¯M
Lemma 12.For every realx≥1, let
β(x) =
s
1
2x ln
 2π2N x2
3δ

.(40)
Thenβis decreasing on[1,∞). Consequently,β(m)≤β(x)for everym≥x≥1.
Proof. Let C = 2π2N/(3δ)and h(x) = β(x)2 = ln(Cx 2)/(2x) ≥ 0. Since Q ⊆[N ]contains at least two
providers,N≥2. Since moreoverδ <1, for everyx≥1,
Cx 2 ≥C > 4π2
3 > e2.
Differentiating gives
h′(x) = 2−ln(Cx 2) 2x2 <0,
sohis decreasing on[1,∞), and so isβ=
√
h.
Lemma 13.OnE, for every unqualified provideri /∈ Qand every stept > N, ifi∈ˆQt, then
mi,t ≤M i.
Proof.Fixi /∈ Qand a stept > Nwithi∈ ˆQt. By the definition of estimated-qualified set and Lemma 1,
qmin ≤ˆqi,t +β(m i,t)≤q i + 2β(mi,t),
and thereforeε i ≤2β(m i,t). Applying Lemma 2 witha=ε i gives
mi,t ≤ 4 ε2 i ln  57N δε4 i  ≤M i,
which proves the claim.
26

Lemma 14.For every non-exploration stept > N,
mj,t ≥g(t)for everyj∈ ˆQt.(41)
If, moreover,Eholds andt > T0, then ˆQt =Q.
Proof. Fix an ordinary stept > N, so that St = ∅. By the definition of St, no provider j∈ ˆQt satisfies
mj,t < g(t), which proves (41).
Now suppose thatE holds and t > T0, so thatg(t) > ¯M. By Lemma 3,Q ⊆ˆQt. Conversely, suppose that
some unqualified provideri /∈ Qbelongs toˆQt. Then (41) gives
mi,t ≥g(t)> ¯M≥M i,
whereas Lemma 13 givesmi,t ≤M i, a contradiction. Hence, ˆQt ⊆ Q, and thereforeˆQt =Q.
Lemma 15.For every stept≥1,0≤π t ≤c max. Consequently,

πt −¯c(2)

 ≤c max, t≥1.(42)
Proof. By the payment rule,πt ≤c max, with equality during initialization, on exploration steps, and whenever ˆQt = ∅. On an ordinary round, Proposition 1 implies that the selected provider bidsbIt,t ≤P It,t, and
therefore
πt = min{PIt,t, cmax} ≥min{bIt,t, cmax}=b It,t ≥0.
Since also¯c(2) ∈[0, cmax], (42) follows.
Lemma 16.Suppose that all providers use their equilibrium strategyσ∗. On E, for every non-exploration
stept > T0,
¯c(2) −3c maxβ(g(t))≤π t ≤¯c(2) +c maxβ(g(t)).(43)
Proof. Fix a non-exploration stept > T0 and let i = It. By Lemma 14, ˆQt = Q and mj,t ≥g (t)for every
j∈ Q. Moreover,g(t)> ¯M≥1, so Lemma 12 gives
β(mj,t)≤β(g(t)), j∈ Q.(44)
We start with the upper bound. Lemma 11 and Eq. 44 give
πt ≤¯c(2) +c maxβ(mi,t)≤¯c(2) +c maxβ(g(t)).
We next turn to the lower bound. SinceˆQt = Q, the selected provider satisfiesi∈ Q, and the payment
rule gives
πt = min

cmaxβ(mi,t) + min j∈Q\{i}

bj,t −c maxβ(mj,t)

, cmax

.
For everyj∈ Q \ {i}, Lemma 5 and Eq. 44 give
bj,t −c maxβ(mj,t)≥¯cj −2c maxβ(g(t)).(45)
Ifi=i ∗, then¯cj ≥¯c(2) for everyj∈ Q \ {i∗}, and Eq. 45 yields
cmaxβ(mi∗,t) + min j∈Q\{i∗}

bj,t −c maxβ(mj,t)

≥¯c(2) −2c maxβ(g(t))≥¯c (2) −3c maxβ(g(t)).
If insteadi̸=i ∗, theni ∗ ∈ Q \ {i}and¯cj ≥¯ci∗ for everyj∈ Q \ {i}, so Eq. 45 yields
min
j∈Q\{i}

bj,t −c maxβ(mj,t)

≥¯ci∗ −2c maxβ(g(t)).
27

Further, Lemma 6 gives¯ci −¯ci∗ ≤2c maxβ(mi,t), and since¯ci ≥¯c(2),
¯ci∗ ≥¯c(2) −2c maxβ(mi,t).
Therefore,
cmaxβ(mi,t) + min j∈Q\{i}

bj,t −c maxβ(mj,t)

≥¯c(2) −c maxβ(mi,t)−2c maxβ(g(t))
≥¯c(2) −3c maxβ(g(t)),
where the last inequality uses Eq. 44. In both cases, the first argument of the minimum definingπt is at least
¯c(2) −3c maxβ(g(t)), and, since¯c(2) ≤c max, so is the second. Hence,
πt ≥¯c(2) −3c maxβ(g(t)),
which completes the proof.
Theorem 11.When all providers choose their equilibrium strategyσ∗, with probability at least1−δ , for
every time stept > T0 that is not an exploration step,i.e.,St =∅, the payment satisfies
¯c(2) −3c max β(g(t))≤π t ≤¯c(2) +c max β(g(t)).(46)
Hence,π t →¯c(2) ast→ ∞along these time steps. Moreover, for everyT > T0,
1
T
TX
t=1

πt −¯c(2)

 ≤ T0 T cmax +k  N T 1−α  cmax −¯c(2) 
+ 6c max
2−α
vuut 1
2k
 N
T
α
ln

2π2N k2
3δ
 T
N
2α!
.(47)
Proof.We work under the eventE, which by Lemma 1 occurs with probability at least1−δ.
The first claim, Eq.46, is Lemma 16. Sinceg(t) → ∞and β(x) → 0as x→ ∞, we haveβ(g(t)) → 0, and
henceπ t →¯c(2) in non-exploration steps.
For the second claim, fixT > T0. In E, every post-initialization step is either an exploration step or a
non-exploration step, so we partition the stepst≤Tinto the three sets
R1 ={t≤T 0},R 2 ={T 0 < t≤T:S t ̸=∅},R 3 ={T 0 < t≤T:S t =∅}.
The set R1 contains at mostT0 steps, each of which contributes at mostcmax to the sum in the left-hand
side of Eq. 47 by Lemma 15. Hence, X
t∈R1

πt −¯c(2)

 ≤T 0 cmax.
On every step inR2, the selected provider is paidcmax, so the step contributescmax −¯c(2). By Lemma 4,
there are at mostN(⌈g(T)⌉ −1)≤N g(T) =kN(T /N)α exploration steps. Hence,
X
t∈R2

πt −¯c(2)

 ≤kN  T N α  cmax −¯c(2)  .
Finally, for everyt∈ R3, Lemma 16 gives

πt −¯c(2)

 ≤3c maxβ(g(t)).
Since1≤ ¯M < g(t)≤g(T)and1/g(t) = (N/t) α/k,
β(g(t)) =
s
1
2g(t) ln
 2π2N g(t)2
3δ

≤
vuut 1
2k ln

2π2N k2
3δ
 T
N
2α!  N
t
α/2
.
28

Moreover,
TX
t=1
t−α/2 ≤
Z T
0
x−α/2 dx= 2 2−α T 1−α/2.
Combining the two preceding inequalities gives
X
t∈R3

πt −¯c(2)

 ≤ 6cmax 2−α
vuut N α
2k ln

2π2N k2
3δ
 T
N
2α!
T 1−α/2.
Summing the contributions ofR1,R 2, andR 3 and dividing byT, together with
kN(T /N)α
T =k
 N
T
1−α
, N α/2 T 1−α/2
T =
 N
T
α/2
,
proves (47).
Proof of Theorem 4.Theorem 4 is the second claim of Theorem 11.
Corollary 12.Under the assumptions of Theorem 11, forN, k, δ fixed and T→ ∞, the right-hand side of
Eq. 47 is
O

T −(1−α)

+O

T −α/2√ lnT  =O  T −min{1−α, α/2}√ lnT  .
The exponentmin{1−α, α/2} is maximized overα∈ (0, 1)at α = 2/3, for which the bound isO

T −1/3√ lnT  .
Proof. The first term of Eq. 47 isO(1/T )and the second isO(T −(1−α)); since α >0, the first is dominated by
the second. In the third term,ln
 2π2N k2
3δ (T /N)2α = O(lnT ), so the term isO(T −α/2√ lnT ). Finally,1 −α
is decreasing andα/2is increasing in α, so min{1 −α, α/2} is maximized where they coincide,1−α = α/2,
i.e., atα= 2/3, where both equal1/3.
A.10 Robust optimality of the truthful strategy
Throughout, we fix a provideri∈ [N ], the strategiesσ−i of the other providers, and a historyHt of the
platform before stept > N, containing the observed historyHi,t of provider i. For every steps≥t , we write
Gi,s =

πs −ˆci,s

1{I s =i}
for the net payment of provideriat steps, so thatUi|Ht (σi,σ −i;θ −i, T) =E[PT s=t Gi,s |H t]by Eq. 7.
The proof rests on a single observation: once the history before a step is fixed, the net payment of provider
i at that step depends on its own bid only through whether it is assigned the query, and bidding the cost
estimate is the best choice.
Lemma 17.Fix a step s > Nand a historyHs of the platform before steps, containing the observed history
Hi,s. For b∈ [0, cmax], let Gi,s(b)denote the net payment of provideri at step s if it bidsbi,s = b. Then, for
everyb∈[0, c max],
a)G i,s(ˆci,s)≥0;
b)G i,s(ˆci,s)≥G i,s(b);
c) ifS s =∅,i∈ ˆQs, and(ˆci,s −P i,s)(b−P i,s)<0, thenG i,s(b)< Gi,s(ˆci,s).
29

Proof. If ˆQs = ∅ or Ss ̸= ∅, the allocation does not depend on the bids and the selected provider is paidcmax.
Hence Gi,s(b) = (cmax −ˆci,s) 1{I s = i} ≥0for every b, which proves a) and b), while c) does not apply. If
Ss = ∅ and i /∈ˆQ, provider i is not selected whatever it bids, soGi,s(b) = 0for every b and all three claims
hold.
It remains to considerSs = ∅ and i∈ ˆQs. By Proposition 1, provideri is selected ifb < Pi,s. Whenever it
is selected, the payment rule (Eq. 5) pays itπs = min{Pi,s, cmax}, which does not depend onb. Therefore,
Gi,s(b) =

min{Pi,s, cmax} −ˆci,s

1{I s =i} ∈

0,min{P i,s, cmax} −ˆci,s

.(48)
We first computeGi,s(ˆci,s). If ˆci,s < Pi,s, provider i is selected and, sinceˆci,s ≤c max, min{Pi,s, cmax} ≥
min{ˆci,s, cmax} = ˆci,s, so Gi,s(ˆci,s) = min{Pi,s, cmax} −ˆci,s ≥ 0. If ˆci,s > Pi,s, provider i is not selected and
Gi,s(ˆci,s) = 0, while min{Pi,s, cmax} −ˆci,s ≤P i,s −ˆci,s < 0. If ˆci,s = Pi,s, the factormin{Pi,s, cmax} −ˆci,s in
Eq. 48 equalsmin{ˆci,s, cmax} −ˆci,s = 0, soG i,s(ˆci,s) = 0whether or notiis selected. In all three cases,
Gi,s(ˆci,s

=

min{Pi,s, cmax} −ˆci,s
+
≥0(49)
which proves a). Claim b) follows since, by Eq. 48,Gi,s(b)is either0or min{Pi,s, cmax} −ˆci,s, both of which
are at most the right-hand side of Eq. 49.
For c), suppose first thatˆci,s < Pi,s < b. Then bidding ˆci,s gets the query while biddingb does not, so
Gi,s(b) = 0. Moreover, ˆci,s < b≤c max and ˆci,s < Pi,s give min{Pi,s, cmax}>ˆci,s, so Gi,s(ˆci,s) > 0 = Gi,s(b)
by Eq. 49. Suppose instead thatb < Pi,s <ˆci,s. Then biddingb gets the query while biddingˆci,s does not, so
Gi,s(ˆci,s) = 0, whereasG i,s(b) = min{Pi,s, cmax} −ˆci,s ≤P i,s −ˆci,s <0by Eq. 48.
Proof of Theorem 2.
Proof of Theorem 2.To lighten the notation, we omit the fixed argumentsσ−i and θ−i, and writeUi|Ht (σi; T ).
By Eq. 8,σ∗ i (Hi,s) = ˆci,s at every steps.
Claim i).Under σ∗ i, provider i bids ˆci,s at every steps≥t , so Lemma 17a), applied at steps to the
realized history before it, givesGi,s ≥ 0. Summing overs = t, . . . , Tand taking the expectation conditional
onH t yieldsU i|Ht (σ∗ i ;T)≥0for everyT≥tand everyθ −i.
Claim ii).By Lemma 17a), every termGi,s is non-negative underσ∗ i, so Ui|Ht (σ∗ i ; T )is non-decreasing in
T, and its infimum overT≥t is attained atT = t. Conditional on Ht, all standing bids, selection counts,
and estimates entering the allocation and payment rules at stept are fixed, so the net payment at stept does
not depend further onθ−i, andU i|Ht (σ∗ i ;t) =E[G i,t(ˆci,t)|H t]for everyθ −i. Hence,
inf
T≥t,θ −i
Ui|Ht (σ∗ i ;T) =E  Gi,t(ˆci,t)|H t  .(50)
Now fix any strategyσi and let b = σi(Hi,t)be its bid at step t. Taking T = t in the infimum and then
applying Lemma 17b) for every realization of the platform’s draw at stept,
inf
T≥t,θ −i
Ui|Ht (σi;T)≤U i|Ht (σi;t) =E

Gi,t(b)|H t

≤E

Gi,t(ˆci,t)|H t

.(51)
Combining Eqs. 50 and 51 proves claim ii).
Claim iii).Under the assumptions of claim iii), stept is not an exploration step, soGi,t(b)and Gi,t(ˆci,t)
are determined byHt, and Lemma 17c) givesGi,t(b) < Gi,t(ˆci,t). The last inequality in Eq. 51 is therefore
strict, and so is the inequality in claim ii).
30

B Bayesian cost estimation
The analysis in Appendix A considers providers that bid the empirical meanˆci,t of their observed generation
costs. In this section, we show that the robust optimality of bidding one’s current cost estimate (Theorem 2)
holds verbatim for any estimator, and that the user-facing guarantees of Section 4 extend to Bayesian
estimators whose prior is eventually dominated by the data, with the cost-estimation radius widened by a
factor1 +γand unchanged asymptotic rates. No proof of Appendix A is repeated; instead, we identify the
properties of the bids that those proofs use and verify them for Bayesian estimates.
Estimation model.Each provider i∈ [N ]forms its cost estimate through a mapei from histories to
[0, cmax], and we write ei,t = ei(Hi,t)for its estimate before step t. Since Hi,t consists of the first mi,t
observations of provideri, we also writeei,m for the estimate afterm selections, so thatei,t = ei,mi,t, in the
same way thatˆqi,t = ˆqi,mi,t and ˆci,t = ˆci,mi,t. For a Bayesian provider,ei,m is the posterior mean of the cost
of serving its next query given a prior and itsm observed costs; it lies in[0, cmax]because the cost does. We
require that the prior does not pull the estimate away from the empirical mean by more than a fixed multiple
of the confidence radius.
Assumption 1.There exists a constantγ≥0such that, for every provideri∈[N]and everym≥1,

ei,m −ˆci,m

 ≤γ cmax β(m).(52)
The constantγis a property of the estimation rule, andγ= 0recovers the empirical mean.
Lemma 18.Under Assumption 1, on the eventE of Lemma 1, for every provideri∈ [N ]and every m≥ 1,

ei,m −¯ci

 ≤(1 +γ)c max β(m).(53)
Proof.OnE,|ˆc i,m −¯ci| ≤cmaxβ(m)by Eq. 13. By the triangle inequality and Eq. 52,

ei,m −¯ci

 ≤

ei,m −ˆci,m

 +

ˆci,m −¯ci

 ≤γc maxβ(m) +c maxβ(m).
Bayesian variant of the mechanism.The platform uses a known upper boundγ satisfying Assumption 1—
any larger valid bound may be used, since Eq. 52 is monotone inγ—and replaces the cost-estimation radius
cmaxβ(mi,t)by(1 + γ)cmaxβ(mi,t)in the adjusted bids of the allocation rule (Eq. 3) and in the critical
payment (Eq. 4),i.e.,
It = argmin
i∈ ˆQt

bi,t −(1 +γ)c maxβ(mi,t)

,ifS t =∅,
Pi,t = (1 +γ)c maxβ(mi,t) + min
j∈ ˆQt\{i}

bj,t −(1 +γ)c maxβ(mj,t)

.
(54)
The quality estimates ˆqi,t, the estimated-qualified set ˆQt, the exploration set St, the schedule g, the
initialization and exploration paymentscmax, and the payment cap in Eq. 5 are unchanged, andγ = 0
recovers the mechanism of Section 2. Providers bid their current estimate,bi,t = ei,t, and the utility in Eq. 7
is evaluated withei,s in place ofˆci,s.
The widening of the radius is necessary: if the platform keptcmaxβ, the adjusted bid ofi∗ would only
satisfy bi∗,t −c maxβ(mi∗,t) ≤¯ci∗ + γcmaxβ(mi∗,t), and the optimism propertybi,t −c maxβ(mi,t) ≤¯ci on which
Lemma 6 rests would fail.
Proposition 13.Consider the Bayesian variant of the mechanism in Eq. 54 with all providers bidding
bi,t =e i,t, and letL(γ) i =M  ∆i/((1 +γ)c max)  , whereM(·)is defined in Theorem 3.
i) Without Assumption 1: Lemmas 1, 2, 3, 4, 8, 10, 12, 13, 14, and 15, Theorem 7, and the quantities
Mi, ¯M, and T0 hold exactly as stated, under arbitrary bids; and Proposition 1, Lemma 17, Theorem 2,
and the robust-equilibrium property that follows it hold withei,t in place ofˆci,t, for any estimatorei
with values in[0, cmax].
31

ii) Under Assumption 1: Lemmas 5, 6, 7, 9, 11, and 16, Theorems 3, 8, 9, 11, and 4, and Corollaries 5,
6, 10, and 12 hold after replacing each cost-estimation radiuscmaxβ(·)by(1 + γ)cmaxβ(·)in their
statements, with the corresponding replacementLi →L (γ) i .
Proof. Claim i).The results in the first group concern the quality estimates, the estimated-qualified set, the
exploration rule, or the confidence radius alone; their proofs do not involve the bids or the cost estimates,
all of which the Bayesian variant leaves unchanged, so they hold as stated under arbitrary bids. For the
second group, the proofs of Proposition 1 and Lemma 17 use only that the allocation rule selects a minimizer
of bj,t −ρ j,t over ˆQt and pays min{Pi,t, cmax} with Pi,t = ρi,t + minj∈ ˆQt\{i}(bj,t −ρ j,t), for arbitrary radii ρj,t ≥ 0determined by the history, together with the fact that the bid compared toPi,t and the estimate
entering the net paymentGi,s coincide and lie in[0, cmax]. Both hold for ρj,t = (1 + γ)cmaxβ(mj,t)and
ei,t ∈ [0, cmax]. The proof of Theorem 2 uses only Lemma 17 and that the truthful strategy bids the estimate
entering Eq. 7 at every step. None of these proofs uses the eventEor the form of the estimator.
Claim ii).The only property of the bids used in the listed proofs is the adjusted-bid bound of Lemma 5,
which in the Bayesian variant reads, onEand by Lemma 18,
¯ci −2(1 +γ)c maxβ(mi,t)≤b i,t −(1 +γ)c maxβ(mi,t)≤¯ci,(55)
with the same one-line proof. Downstream of this bound, the radius enters only through the choicea = ∆i/cmax
in the application of Lemma 2 (proof of Lemma 7), which becomesa = ∆i/((1 +γ)cmax)and yields L(γ) i , and
the choices κ = cmax and κ = 2cmax in the applications of Lemma 10 (proofs of Theorems 9 and 8), which
become κ = (1 + γ)cmax and κ = 2(1 + γ)cmax; both lemmas hold for arbitrarya >0and κ≥ 0. Every other
occurrence of cmax in these proofs—the bid range, the initialization and exploration payments, the payment
cap, the bound |πt −¯c(2)| ≤cmax, and the factorcmax −¯c(2)—refers to the range of costs and payments,
which is unchanged. Hence each listed proof goes through verbatim under the stated replacement.
Resulting guarantees.Two consequences of Proposition 13ii) are worth recording. First, Theorem 3
holds with M (∆i/cmax)replaced by L(γ) i = M  ∆i/((1 + γ)cmax)  : the ordinary-step selection threshold of
a qualified suboptimal provider grows withγ, while the terms for unqualified providers, the exploration
term, and the quality guarantee of Theorem 7 are unchanged. Second, Theorem 4 holds with the coefficient
6c max
2−α of its last term replaced by6(1+γ)c max 2−α , and its first two terms unchanged; likewise, Lemma 16 gives
¯c(2) − 3(1 + γ)cmaxβ(g(t)) ≤π t ≤¯c(2) + (1 + γ)cmaxβ(g(t))on every non-exploration step t > T0. Hence, for
fixed γ, the average absolute deviation of the payments from¯c(2) is O

T −(1−α) + O  (1 + γ) T −α/2√ lnT  ,
the exponent is still maximized atα = 2/3(Corollary 12), and 1 T PT t=1 πt →¯c(2) as T→ ∞. The average
excess-payment bound of Corollary 10 receives the same radius substitution in its last term only.
Provider incentives.By Proposition 13i), bidding one’s current cost estimate,σ∗ i (Hi,t) = ei,t, is worst-case
optimal in the sense of Theorem 2 for any estimator with values in[0, cmax], in the Bayesian variant of the
mechanism as well as in the original one. The robust-optimality result is thus estimator-agnostic: once a
provider’s utility is evaluated relative to its current estimate, the threshold structure of the allocation rule
makes bidding that estimate optimal. Assumption 1 plays no role in this result; it is needed only to relate
the providers’ estimates to their true mean costs, and thereby obtain the user-facing guarantees above.
32

C Robustness to deviations from cost-estimate bidding
Theorem 2 shows that, for a provider, bidding its current cost estimate is worst-case optimal, but a provider
may nevertheless deviate from it. In this section, we quantify how the user-facing guarantees of Section 4
change when bids may fall below or above the cost estimate by bounded amounts.
Assumption 2.There exist constants d−, d+ ≥ 0such that every provider i∈ [N ]follows a strategy σi with
−d− ≤σ i(Hi,t)−ˆci,t ≤d + for every historyHi,t, t > N.(56)
The constant d− bounds underbidding and d+ overbidding relative to the empirical mean cost; the
equilibrium strategyσ ∗ of Eq. 8 is the cased− =d + = 0.
The good-event, quality-estimation, and forced-exploration results of Appendix A do not use the providers’
bids. In particular, Lemmas 1, 2, 3, 4, 8, 10, 12, 13, 14, and 15, Theorem 7, and the quantitiesMi, ¯M,
and T0 hold under Assumption 2 exactly as stated; unqualified providers are therefore eliminated, and the
quality guarantee holds, unchanged. The remaining results depend on the bids only through Lemma 5, whose
counterpart under deviations is the following:
Lemma 19.Under Assumption 2, on the eventE, for every provideri∈[N]and stept > N,
¯ci −2c maxβ(mi,t)−d − ≤b i,t −c maxβ(mi,t)≤¯c i +d +.(57)
Proof.OnE,|ˆc i,t −¯ci| ≤cmaxβ(mi,t)by Eq. 13; combine withˆci,t −d − ≤b i,t ≤ˆci,t +d +.
The adjusted bid is no longer optimistic, since its upper bound exceeds¯ci by d+, and its lower bound is
lowered byd −. Tracing these two shifts through the proofs of Appendix A gives the results below.
Selection and identification.Underbidding by a competitor and overbidding by i∗ both help the
competitor win a non-exploration round, so the two deviations enter the selection analysis.
Proposition 14.Under Assumption 2, on the eventE:
i) On every non-exploration stept > N, the selected provider satisfies
¯cIt −¯ci∗ ≤2c maxβ(mIt,t) +d − +d +.(58)
ii) Every qualified provider i∈ Q \ {i∗} with∆ i > d− + d+ is selected after initialization at most
max{L(d) i ,⌈g(T)⌉ −1}times, where
L(d) i :=M
 ∆i −d − −d +
cmax

(59)
andM(·)is defined in Theorem 3.
iii) If∆ i > d− + d+ for every i∈ Q \ {i∗}, then Theorem 3 and Corollaries 5 and 6 hold withM (∆i/cmax)
replaced byL(d) i .
Proof. Claim i).As in the proof of Lemma 6: onE, i∗ ∈ ˆQt by Lemma 3, so the selected providerIt = i
satisfies bi,t −c maxβ(mi,t) ≤b i∗,t −c maxβ(mi∗,t). Bounding the left side from below and the right side from
above with Eq. 57 gives¯ci − 2cmaxβ(mi,t) −d − ≤¯ci∗ + d+. This holds for everyi∈ ˆQt, qualified or not, since
Eq. 57 holds for every provider.
Claim ii).At every non-exploration selection ofi∈ Q \ {i∗}, claim i) gives(∆i −d − −d +)/cmax ≤ 2β(mi,t),
and Lemma 2 witha = (∆i −d − −d +)/cmax > 0gives mi,t ≤L (d) i . The rest is the proof of Lemma 9 with
Li replaced byL (d) i .
Claim iii).The proofs of Theorem 3 and its corollaries use the bids only through Lemma 9, which claim
ii) replaces.
33

The condition∆ i > d− + d+ cannot be dropped: if∆ i ≤d − + d+, the bids bi,t = ˆci,t −d − and
bi∗,t = ˆci∗,t +d + satisfy Assumption 2 and, once the two providers have comparable selection counts, givei
an adjusted bid at most that ofi∗ up to the confidence radii, soi may win every ordinary round. When some
qualified competitor is withind− + d+ of i∗, the platform therefore need not identifyi∗; claim i) shows what
it guarantees instead: on every ordinary round it selects a provider whose mean cost exceeds¯ci∗ by at most
d− +d + plus a vanishing term, and that provider is qualified on all but the rounds bounded by Lemma 8.
Theorem 15.Under Assumption 2, on the eventE, the generation-cost regret of Theorem 8 satisfies
Rgen T ≤(N−1)⌈g(T)⌉c max + 2cmax
s
2N(T−N) ln
 2π2N T2
3δ

+ (d− +d +)(T−N).(60)
If moreover∆ i > d− + d+ for every i∈ Q \ {i∗}, the second bound of Theorem 8 holds withLi replaced by
L(d) i .
Proof. In the proof of the first bound of Theorem 8, the inequality¯ci − 2cmaxβ(mi,t) ≤¯ci∗ on non-exploration
steps is replaced by Eq. 58. Splittingat ≤ 2cmaxβ(mIt,t) + (d− + d+), Lemma 10 withκ = 2cmax bounds the
sum of the first terms as before, and the second terms contribute at most(d− + d+)(T−N ). The second
bound uses the bids only through Lemma 9, which Proposition 14ii) replaces.
Dividing by T, the average generation-cost regret is at mostd− + d+ up to a term of orderT −(1−α) +p
lnT /T, whatever the cost gaps.
Payments.Overbidding and underbidding affect the two sides of the payment bounds separately: the
payment is set by the adjusted bid of the cheapest competing provider, which overbidding raises by at most
d+ and underbidding lowers by at mostd−.
Lemma 20.Under Assumption 2, on the eventE, on every non-exploration stept > NwithIt =i,
πt ≤min

cmax,¯c(2) +c maxβ(mi,t) +d +

,(61)
and, if moreovert > T0,
πt ≥¯c(2) −3c maxβ(g(t))−d −.(62)
Proof.Upper bound.As in the proof of Lemma 11, with j = i∗ if i̸ = i∗ and j the second-cheapest
qualified provider ifi = i∗: by Eq. 57,Pi,t ≤c maxβ(mi,t) + bj,t −c maxβ(mj,t) ≤c maxβ(mi,t) + ¯cj + d+ ≤
cmaxβ(mi,t) + ¯c(2) +d +.
Lower bound.For t > T0, Lemma 14 givesˆQt = Q and mj,t ≥g (t)for every j∈ Q, so β(mj,t) ≤β (g(t))
by Lemma 12. Write Aj,t = bj,t −c maxβ(mj,t), so that Pi,t = cmaxβ(mi,t) + minj∈Q\{i} Aj,t. For every
j∈ Q \ {i, i∗}, Eq. 57 and¯cj ≥¯c(2) give Aj,t ≥¯c(2) − 2cmaxβ(g(t)) −d −. If i = i∗, this covers everyj∈ Q \ {i}
and Pi,t ≥¯c(2) − 2cmaxβ(g(t)) −d −. If i̸ = i∗, the remaining competitor isi∗, and since i was selected,
Ai∗,t ≥A i,t, so that
cmaxβ(mi,t) +A i∗,t ≥c maxβ(mi,t) +A i,t =b i,t ≥ˆci,t −d −
≥¯ci −c maxβ(g(t))−d − ≥¯c(2) −c maxβ(g(t))−d −
using i∈ Q \ {i∗} in the last step. Hence Pi,t ≥¯c(2) − 2cmaxβ(g(t)) −d − in both cases, and πt =
min{Pi,t, cmax} ≥¯c(2) −2c maxβ(g(t))−d − ≥¯c(2) −3c maxβ(g(t))−d −, since¯c(2) ≤c max.
Atd − =d + = 0, Eqs. 61 and 62 are Lemmas 11 and 16.
34

Theorem 16.Under Assumption 2, with probability at least1−δ, for everyT≥T 0,
1
T
TX
t=1

πt −¯c(2)

 ≤ T0 T cmax +k  N T 1−α  cmax −¯c(2)  + max{d−, d+}
+ 6c max
2−α
vuut 1
2k
 N
T
α
ln

2π2N k2
3δ
 T
N
2α!
(63)
and consequently
¯c(2) −d − ≤lim inf T→∞
1
T
TX
t=1
πt ≤lim sup
T→∞
1
T
TX
t=1
πt ≤¯c(2) +d +.(64)
Moreover, the average excess payment of Corollary 10 is bounded by its right-hand side plusd+.
Proof. In the proof of Theorem 11, the only change is on the non-exploration stepst > T0, where Lemma 20
gives |πt −¯c(2)| ≤3cmaxβ(g(t)) + max{d−, d+} in place of3cmaxβ(g(t)); summing the additional term over at
most T steps and dividing byT gives Eq. 63. For Eq. 64, the same decomposition applied toπt −¯c(2) without
absolute values gives, for the non-exploration stepst > T0, −3cmaxβ(g(t)) −d − ≤π t −¯c(2) ≤c maxβ(g(t)) +d+,
while the firstT0 steps and the exploration steps contributeO(T0/T + T −(1−α))to the average; the vanishing
terms are those of Eq. 63. The excess-payment claim follows from Eq. 61 in the proof of Theorem 9, whose√·term is unchanged and which acquires the additional termd+(T−N).
Summary.Under bounded deviations, the platform still serves qualified providers on all but a bounded
number of rounds; it identifiesi∗ whenever every qualified competitor is more thand− + d+ costlier, and
otherwise selects a qualified provider withind− + d+ of ¯ci∗ in mean cost; and the average payment converges to
within[ ¯c(2) −d −,¯c(2) + d+]at the rate of Theorem 4. Underbidding thus affects the lower side of the payment
guarantee by at mostd−, whereas overbidding affects the upper side by at mostd+; neither affects the
quality guarantee, and both slow identification through the reduced gaps∆i −d − −d +. Setting d− = d+ = 0
recovers Theorems 3, 8, and 4 verbatim. Finally, for the Bayesian variant of Appendix B, with Assumption 2
stated relative toei,t in place ofˆci,t, the same statements hold withcmaxβ(·)replaced by(1 + γ)cmaxβ(·)
throughout and L(d) i replaced by M  (∆i −d − −d +)/((1 + γ)cmax)  , since the proofs above use the empirical
mean only through Eq. 13, which Lemma 18 replaces.
35

D Experimental details
In this section, we describe the experimental setup we use to evaluate our platform (Algorithm 1). Here,
our goal is twofold: first, to instantiate the model of Section 2 using recorded generations from real LLMs,
so that provider qualities and generation costs are grounded in observed data; and second, to compare the
platform against practical routing policies that a platform could deploy today. In what follows, we describe
the data, the construction of providers, the experimental settings, the routing policies we compare against,
and the metrics we report.
Recorded generation data.We evaluate the platform using a publicly available dataset of recorded LLM
generations.11 The data coverGSM8K [Cobbe et al., 2021] andGPQA [Rein et al., 2024], spanning a wide range
of difficulty. For every model–question pair, the data contain 128 recorded generations, each annotated with
a binary correctness label, an output-token count, and, when needed for Best-of-ni service, a score from the
reward model ArmoRM-Llama3-8B-v0.1 [Wang et al., 2024b]. Our simulator retains only these quantities and
a question identifier; i.e., neither the prompts nor the generated text are used. The data contain 1,319GSM8K
questions and 546GPQA questions. Since Best-of-ni service requires the correctness, token, and reward records
to be aligned for every included model, we remove oneGPQA question that fails this alignment check jointly
from all models whenever Best-of-ni variants are in use, leaving 545GPQA questions in those experiments;
no questions are removed fromGSM8K. As a result, every retained model has the same question set and 128
recorded generations per question.
Base models and listed prices.We use the nine base models listed in Table 2, together with their
publicly listed prices. To determine the per-output-token price of each model, we follow the procedure of
Velasco et al. [2026c]: we refer to the Hugging Face list of inference providers12 and, for each model, compute
the average output-token price across the listed providers that offer access to that model. More formally, we
denote by λm the resulting listed price of modelm in USD per106 output tokens. Throughout, all monetary
quantities are reported in units of10−6 USD, so that the numerical value ofλm coincides with the price per
output token in these units.
Modelλ m Modelλ m
Llama-3-8B0.1455Qwen2-0.5B0.1000
Llama-3.1-8B0.1245Qwen2-1.5B0.1000
Llama-3.2-1B0.1000Qwen2-7B0.2000
Llama-3.2-3B0.0800Qwen2.5-3B0.0650
Qwen2.5-7B0.1465
Table 2: Listed output-token prices used in the experiments, in USD per106 output tokens.
Provider construction.To instantiate providers with a cost–quality trade-off, we build each provider
from a base modelm and a service multiplicityni, and writei = (m, ni)to identify the provider by this
pair. A base provider, withni = 1, serves a query with a single generation of modelm, whereas a Best-of-ni
provider generates ni candidate responses, incurs the generation cost of allni candidates, and returns the
candidate with the highest recorded reward score. More concretely, for each question, the simulator samples
ni distinct generations uniformly without replacement from the 128 recorded generations of modelm and,
if ni > 1, returns the sampled generation with the highest reward score, resolving ties uniformly through
the random ordering of the sampled generations. The correctness of the response, which serves as the score
r(xt, yt)of Section 2, is the binary correctness of the returned generation, while the token count used for
pricing and cost includes allni candidates. We consider three rosters. Thefullroster contains all nine base
11https://huggingface.co/datasets/Human-Centric-Machine-Learning/strategic-ttc-data
12https://huggingface.co/docs/inference-providers/index, consulted on December 30, 2025.
36

Benchmark RosterN K q min |Q|i ∗
GSM8Kfull 9 1319 0.7640 3Qwen2.5-3B
GPQAfull 9 546 0.0790 8Qwen2-1.5B
GSM8Kladder 12 1319 0.8050 3Qwen2.5-7B
GPQAladder 12 545 0.2396 4Llama-3-8B
GPQAstrong-competition 4 546 0.1451 2Llama-3.1-8B
Table 3: Experimental settings. The benchmark sizeK equals the number of aligned benchmark questions
available to the corresponding roster.
models withn i = 1. Theladderroster contains
m∈ {Llama-3-8B,Llama-3.2-1B,Qwen2-1.5B,Qwen2.5-7B}
at each multiplicity ni ∈ {1, 2, 4}, for a total of 12 providers. The ladder roster therefore introduces a
direct cost–quality trade-off within each base model, in addition to the variation across model families. The
strong-competitionroster is used onGPQA only and contains the newest large model and the smallest model of
each family,Llama-3.1-8B,Llama-3.2-1B,Qwen2.5-7BandQwen2-0.5B, all withn i = 1.
Empirical quality, price, and cost.We now specify how the quantities of Section 2 are instantiated
from the recorded data. To this end, it is important to distinguish the listed price, the query price, and the
generation cost. Thelisted price λm is the public per-token rate in Table 2; it is known before routing and
does not depend on the realized output length. We define the realizedquery priceVi,t of provider i = (m, ni)
in step t as the listed priceλm times the total number of output tokens across theni recorded generations
sampled in that step, i.e., the amount a platform using the model at its listed rate would be invoiced once
the output lengths are known. Thus, a Best-of-ni query is billed for every generated candidate, not only for
the returned response. Since the data do not contain the providers’ true generation costs, we construct the
private realizedgeneration costas
ci,t := Vi,t 1 +µ , µ= 0.25,(65)
where µ is a (fixed) margin. It is worth noting that the marginµ is used only to construct the latent
cost observations, and it is neither supplied to nor used by the platform. Building on the above, the
empirical quality qi of provider i is their expected correctness under a uniformly sampled benchmark question
and the generation-sampling procedure above. For a base provider, it is the mean correctness over all
recorded question–generation pairs, while for a Best-of-ni provider, it is computed exactly from the empirical
joint distribution of reward scores and correctness, including uniform tie-breaking. Analogously, the cost
distribution P c i of provider i is the distribution of the realized generation costci,t in Eq. (65) under the
same sampling procedure asqi, and ¯ci is its mean. Since query price and generation cost are proportional
by construction, the mean query price of provideri is ¯vi = (1 + µ)¯ci. These quantities are used only for
evaluation and for constructing perfect-information reference quantities; they are not given to the platform.
Finally, in our primary experiments, providers bid their empirical-mean cost estimateˆci,t,i.e., they follow
the equilibrium strategyσ∗ i of Eq. (8), and payments follow the rule of Eq. (5).
Settings and platform parameters.For each roster and benchmark, we place the quality thresholdqmin
at the midpoint between two adjacent empirical provider qualities. Table 3 reports, for each of the resulting
five settings, the exact threshold, the benchmark sizeK, the number of empirically qualified providers, and
the lowest-cost qualified provideri∗ of Eq. (10).
We set the confidence level toδ = 0 .05. The output-token cap entering the cost bound is fixed at
Lmax = 512, and the cost boundcmax of Section 2, which also caps every payment, is set to
cmax =L max max i=(m,ni) niλm,(66)
37

which gives cmax ≈ 102for the full roster, cmax ≈ 300for the ladder roster and cmax ≈ 75for the strong-
competition roster. Since private costs are obtained by deflating query prices by1 +µ, this ceiling also bounds
every realized provider cost, as required by our model. Interestingly, the two full-roster settings provide
qualitatively different tests of routing by listed price. The lowest listed rate belongs toQwen2.5-3B, which is
i∗ on GSM8K and is qualified but noti∗ on GPQA. Listed-price routing is therefore, respectively, aligned with
and only partially informative about the platform’s target decision.
Episode construction and randomization.At the beginning of every episode, the benchmark questions
are placed in a seeded random permutation. For every step and every provider, the simulator preassigns a
potential outcome using the recorded-generation sampling rule above; only the selected provider’s outcome
is then revealed, while the potential outcomes of nonselected providers remain unavailable to the platform.
This preserves the platform’s information design of Section 2 while allowing different policies to be evaluated
on matched potential outcomes. The firstN steps initialize the platform as prescribed in Section 2, selecting
every provider exactly once in a seeded random order, and all subsequent steps follow the platform’s selection
and payment rules using the pre-step state.
Exploration steps.In every experiment of this appendix the platform runs with the exploration rule of
Eq. (3). At the beginning of stept > N, if some estimated-qualified provideri∈ ˆQt (Eq. (2)), which we also
refer to as aneligibleprovider, has been selected fewer than
g(t) =k(t/N) α, k= 2, α= 3/4,
times,i.e., if St ̸= ∅, the step is an exploration step: one of the under-sampled eligible providers inSt is
drawn uniformly at random, serves the query and is paidcmax; otherwise it is a non-exploration step, selected
and paid according to Eqs.(3) and (5). Exploration steps count toward every selection statistic, regret,
generation cost, query price and amount paid; the winning bid and the payment on non-exploration steps are
reported over those steps only. The routing baselines and the no-quality-filter ablation do not explore.
Routing policies.Our primary comparison uses three routing policies, none of which observes private
generation costs: (i)uniform routing among eligible providers, (ii)lowest-listed-price routing among eligible
providers, and (iii)lowest-listed-price routing without quality screening. Policy (i) constructs the same online
estimated-qualified set ˆQt as the platform, i.e., it may use the observed scores, the selection counts, the
threshold qmin, and the confidence radiusβ(mi,t)of Eq. (2), and selects uniformly at random fromˆQt; it
uses neither bids nor listed prices, and thus isolates the contribution of cost-sensitive selection after online
quality screening. Policy (ii) constructs the sameˆQt and then minimizes the public effective listed rate
¯λi :=n iλm fori= (m, n i),
breaking ties uniformly at random; it observes listed rates but neither provider bids nor generation costs, and
the realized response length is not known at selection time. Policy (iii) is static: it minimizes¯λi over the
entire roster, irrespective of observed quality, and requires only the public listed rates. It therefore provides a
direct measure of the reliability lost when routing ignores the quality requirement. In addition, we consider a
no-quality-filterablation of the platform, which retains the optimistic bidding indexbi,t −c max β(mi,t)of
Eq. (3), the confidence radiusβ(mi,t), and the critical payment of Eq.(4), but minimizes the index over
the full roster rather than overˆQt; this ablation isolates the contribution of online quality screening. The
platform pays πt as in Eq.(5), the routing policies pay the query price of the selected provider, and both are
reported as the amount paid.
Horizons and long-run evaluation.To examine longer-run behavior, we additionally run every setting
for T = 70,000queries and 30 independent runs, paired across rules, corresponding to 54 passes over the
GSM8K benchmark and 129 passes overGPQA, with the final pass only partially used. At the beginning of each
additional pass, the simulator draws a fresh seeded permutation of all benchmark questions and fresh recorded
38

generations for every provider–question pair, so that the same generation may reappear in different passes;
extending the horizon leaves the complete first pass unchanged. This resampling procedure approximates
repeated draws from each provider’s empirical outcome distribution. It does not create new questions or new
model generations, and the resulting long-horizon evidence remains conditional on the observed benchmark
and generation pools.
Metrics.Our main metrics are the quality regret Rqual T = PT t=1(qmin −q It )+ of Theorem 7 and the
generation-cost regret Rgen T = PT t=1(¯cIt −¯ci∗ )+ of Theorem 8, reported both cumulatively and per query.
Note that both regrets are computed using the empirical provider parametersqi and ¯ci rather than the realized
correctness labels and costs, which are subject to sampling noise. We report realized accuracy separately as
dAccT = 1 T
TX
t=1
r(xt, yt),
together with the share of unqualified selections,
1
T
TX
t=1
1{I t /∈ Q},
the selection share ofi∗, provider-level selection counts, and whetheri∗ is the unique most selected provider.
The economic outcomes comprise realized generation cost per query, query price per query, and the amount
paid per query under the policy-specific convention above. For the platform and its no-quality-filter ablation,
we additionally report the winning standing bid, the total payment on non-exploration steps, the cumulative
excess payment Epay T = PT t=1(πt −¯c(2))+ bounded in Theorem 9, and the provider payoffP t:It=i  πt −
ci,t

. Where useful, these quantities are reported both over the full episode and after initialization, since
initialization pays cmax by construction. Payment diagnostics compare the realized payments on non-
exploration steps with the upper boundπt ≤min{c max,¯c(2) + cmax β(mIt,t)} of Lemma 11 and with the lower
bound πt ≥max{ 0,¯cIt −c max β(mIt,t)}, which holds onE because, by Proposition 1, the selected provider
bids ˆcIt,t ≤P It,t. We further report the realized frequency of the good eventE of Lemma 1 and compare
the post-initialization selections of providersi̸ = i∗ with the corresponding bounds Mi of Lemma 8 for
unqualified providers andmax{Li,⌈g (T )⌉ −1} of Lemma 9 for qualified ones, whereLi is defined in Lemma 7.
Accordingly, when reportingBid(T )and Tid, we replace the exploration termk(T /N)α of Theorem 3 by the
cap ⌈g(T )⌉ −1 < k(T /N)α of Lemma 9, which yields a slightly tighter bound that is also valid by the proof
of Theorem 3. For the long-horizon experiment, we additionally report the size of the estimated-qualified set
ˆQt, the probability thati∗ is the unique most selected provider, and moving-average selection and payment
statistics with window sizeK.
Aggregation and uncertainty.Episode-level tables report the mean and standard deviation across
runs. For one-pass figures, points and selection shares are shown with normal-approximation 95% intervals,
x± 1.96 sx/
√
R, where R is the number of runs andsx is their sample standard deviation. Long-horizon
trajectory figures use the pointwise median across runs as the central trajectory and the empirical 10th–90th
percentile range as a band. Long-horizon checkpoint tables report means across runs, while identification
probabilities are the corresponding empirical fractions of runs.
39

E GSM8K weak-competition experiments
This section reports the completeGSM8K results for the full and ladder rosters; Appendix D provides the
experimental details. The platform runs with the exploration rule described there,k = 2and α = 3 /4.
One-pass results are averaged over30independent runs, paired across rules and reported with95%confidence
intervals, while long-horizon trajectories report the median and10–90%range over30independent runs.
Monetary quantities are per query unless stated otherwise. A moving average has window sizeK = 1,319,
one pass over the benchmark, so that it reflects a rule’s current behaviour rather than its whole history. For
the platform and its no-quality-filter ablation the amount paid is the paymentπt; for the routing baselines it
is the query price of the selected provider. On the full roster¯c(2) = 34.4lies above the mean query price ofi∗,
¯vi∗ = 20.1, so this is the weak-competition case in which a payment that approaches¯c(2) exceeds the listed
price ofi ∗.
E.1 Providers and environment
i∗ Other qualiﬁed provider Unqualiﬁed provider Lowest listed price
20 30 40
Expected query price ($)
0.0
0.2
0.4
0.6
0.8
1.0
Quality
Qwen2-0.5B
Llama-3.2-1B
Qwen2-1.5B
Llama-3.1-8B
Llama-3-8B
Llama-3.2-3B
Qwen2-7B
Qwen2.5-3B
Qwen2.5-7B
Θ = 0 .764
(a) Quality against mean query price, full roster
50 100 150
Expected query price ($)
0.0
0.2
0.4
0.6
0.8
1.0
Quality
Llama-3.2-1B
Llama-3.2-1B@2
Llama-3.2-1B@4
Qwen2-1.5B
Llama-3-8B
Qwen2-1.5B@2
Llama-3-8B@2
Llama-3-8B@4
Qwen2-1.5B@4
Qwen2.5-7B
Qwen2.5-7B@2
Qwen2.5-7B@4
Θ = 0 .805 (b) Quality against mean query price, ladder roster
Figure 2: GSM8K providers. Each point is one provider at its qualityqi and mean query price; the dotted
line is the quality thresholdqmin, and the ring marks the provider with the lowest listed price. Monetary
quantities are in units of10−6 USD. On the full roster the lowest listed price belongs toi∗; on the ladder
roster it is shared by two unqualified providers.
40

Table 4:GSM8Ksetting constants for the two rosters. Costs and prices are expected values per query.
Quantity Full roster Ladder roster
ProvidersN9 12
Benchmark sizeK(queries in one pass) 1,319 1,319
Quality thresholdq min 0.764 0.805
Qualified providers|Q|3 3
i∗ Qwen2.5-3B Qwen2.5-7B
¯ci∗ 16.1 34.4
¯vi∗ 20.1 43.0
¯c(2) 34.4 68.7
¯c(2) −¯ci∗ 18.3 34.4
Lowest listed price Qwen2.5-3B Llama-3.2-1B, Qwen2-1.5B
qualified yes no
equalsi ∗ yes no
cmax 102.4 300.0P
i /∈QMi 28,296 23,132P
i∈Q\{i∗} Li 3,464 6,012
⌈g(T)⌉ −11,656 1,334
Bid(T)31,977 30,010
Tid 63,740 59,735
Table 5: GSM8K providers, sorted by mean generation cost. Listed price is in USD per106 output tokens;
tokens are the mean number of generated tokens per query (summed over theni generations of a Best-of-ni
provider); query price and¯ci are expected values per query. The gap isεi = qmin −q i for an unqualified
provider and∆ i = ¯ci −¯ci∗ for a qualified one, with the corresponding selection boundMi from (25) or
Li from (24); where the exploration-step cap ⌈g(T )⌉ −1at T = 70 ,000exceeds Li, the applicable cap
max{Li,⌈g(T)⌉ −1}of Lemma 9 follows it.
Provider Listed price Tokens Query price¯c i qi Qualified Gap Bound
Full roster
Llama-3.2-3B 0.08 196 15.7 12.5 0.692 noε i = 0.072M= 15,141
Qwen2-0.5B 0.1 181 18.1 14.5 0.351 noε i = 0.413M= 299
Qwen2-1.5B 0.1 189 18.9 15.1 0.574 noε i = 0.190M= 1,770
Llama-3.2-1B 0.1 199 19.9 15.9 0.364 noε i = 0.400M= 324
Qwen2.5-3B (i∗) 0.065 309 20.1 16.1 0.839 yes – –
Llama-3-8B 0.1455 192 27.9 22.3 0.650 noε i = 0.114M= 5,466
Llama-3.1-8B 0.1245 233 29.1 23.3 0.648 noε i = 0.116M= 5,296
Qwen2.5-7B 0.1465 293 43.0 34.4 0.907 yes∆ i = 18.3L= 2,025
Qwen2-7B 0.2 234 46.7 37.4 0.836 yes∆ i = 21.3L= 1,439; cap 1,656
Ladder roster
Qwen2-1.5B 0.1 189 18.9 15.1 0.574 noε i = 0.231M= 1,159
Llama-3.2-1B 0.1 199 19.9 15.9 0.364 noε i = 0.441M= 264
Llama-3-8B 0.1455 192 27.9 22.3 0.650 noε i = 0.155M= 2,809
Qwen2-1.5B@2 0.1 379 37.9 30.3 0.652 noε i = 0.153M= 2,910
Llama-3.2-1B@2 0.1 398 39.8 31.8 0.410 noε i = 0.395M= 340
Qwen2.5-7B (i∗) 0.1465 293 43.0 34.4 0.907 yes – –
Llama-3-8B@2 0.1455 384 55.9 44.7 0.669 noε i = 0.136M= 3,768
Qwen2-1.5B@4 0.1 757 75.7 60.6 0.703 noε i = 0.102M= 7,118
Llama-3.2-1B@4 0.1 795 79.5 63.6 0.440 noε i = 0.365M= 408
Qwen2.5-7B@2 0.1465 587 85.9 68.7 0.923 yes∆ i = 34.4L= 5,544
Llama-3-8B@4 0.1455 768 111.7 89.4 0.677 noε i = 0.128M= 4,356
Qwen2.5-7B@4 0.1465 1,173 171.9 137.5 0.930 yes∆ i = 103.1L= 468; cap 1,334
41

E.2 One-pass behavior
Table 6: GSM8K one-pass outcomes, mean± 95%half-width over30independent runs, paired across rules.
Generation cost and amount paid are per query; the amount paid is the paymentπt for the platform and its
ablation, and the query price for the other rules.
Policy Unqualified shareR qual T /T R gen T /TAccuracy Share ofi ∗ Generation cost Amount paid
Full roster
Platform0.692±0.003 0.099±0.002 3.81±0.02 0.692±0.004 0.179±0.003 18.7±0.0 37.0±0.3
Uniform among
eligible
0.598±0.007 0.094±0.002 7.05±0.12 0.707±0.003 0.136±0.004 22.5±0.1 28.1±0.2
Lowest listed price
among eligible
0.005±0.000 0.001±0.000 0.04±0.00 0.837±0.002 0.994±0.000 16.1±0.0 20.1±0.0
Lowest listed price,
no quality filter
0.005±0.000 0.001±0.000 0.04±0.00 0.837±0.002 0.994±0.000 16.1±0.0 20.1±0.0
No quality filter
(ablation)
0.799±0.003 0.182±0.001 2.30±0.03 0.600±0.004 0.135±0.002 17.2±0.0 17.9±0.1
Ladder roster
Platform0.771±0.005 0.148±0.003 13.69±0.15 0.684±0.003 0.125±0.005 42.1±0.4 118.1±1.5
Uniform among
eligible
0.690±0.005 0.126±0.003 24.81±0.37 0.711±0.003 0.103±0.003 55.3±0.5 69.2±0.7
Lowest listed price
among eligible
0.446±0.031 0.087±0.005 0.20±0.00 0.775±0.007 0.552±0.031 28.2±0.4 35.2±0.5
Lowest listed price,
no quality filter
0.998±0.000 0.333±0.001 0.20±0.00 0.477±0.004 0.001±0.000 15.8±0.1 19.8±0.1
No quality filter
(ablation)
0.855±0.001 0.220±0.000 7.57±0.09 0.600±0.003 0.091±0.001 33.5±0.1 36.0±0.1
Platform
Uniform among eligible
Lowest listed price among eligible
Lowest listed price, no quality ﬁlter
No quality ﬁlter
16 18 20 22
Generation cost per query ($)
0.00
0.05
0.10
0.15
0.20
Quality regret per round Rqual T /T
(a) Quality regret against generation cost, full roster
20 30 40 50
Generation cost per query ($)
0.0
0.1
0.2
0.3
0.4
Quality regret per round Rqual T /T (b) Quality regret against generation cost, ladder roster
Figure 3: GSM8K one pass: quality regret per step against generation cost per query for every routing rule,
mean with95%confidence intervals across runs. Monetary quantities are in units of10−6 USD. The two
listed-price rules coincide on the full roster, where the lowest listed price isi∗.
42

0.0 0.1 0.2 0.3
Share of time steps (95% CI across runs)
Qwen2-0.5B
Llama-3.2-1B
Qwen2-1.5B
Llama-3.1-8B
Llama-3-8B
Llama-3.2-3B
Qwen2-7B
Qwen2.5-3B ( i∗)
Qwen2.5-7B
(a) Platform selection shares, full roster
0.00 0.05 0.10 0.15 0.20
Share of time steps (95% CI across runs)
Llama-3.2-1B
Llama-3.2-1B@2
Llama-3.2-1B@4
Qwen2-1.5B
Llama-3-8B
Qwen2-1.5B@2
Llama-3-8B@2
Llama-3-8B@4
Qwen2-1.5B@4
Qwen2.5-7B ( i∗)
Qwen2.5-7B@2
Qwen2.5-7B@4 (b) Platform selection shares, ladder roster
Figure 4: GSM8K one pass: share of steps the platform assigned to each provider, exploration steps included,
mean with95%confidence intervals across runs. Green marks i∗, blue the other qualified providers and
orange the unqualified providers; the platform never observes these labels.
43

E.3 Long-horizon learning and identification
Platform
Uniform among eligible
Lowest listed price among eligible
Lowest listed price, no quality ﬁlter
No quality ﬁlter
One pass over the benchmark
Identiﬁcation horizon Tid
101 102 103 104
Time step t
0.00
0.25
0.50
0.75
1.00
Share of i∗
(moving average, one pass)
(a) Share ofi∗, full roster
102 103 104
Time step t
0.00
0.25
0.50
0.75
1.00
Share of i∗
(moving average, one pass) (b) Share ofi∗, ladder roster
101 102 103 104
Time step t
0.00
0.25
0.50
0.75
1.00
Share of unqualiﬁed selections
(moving average, one pass)
(c) Share of unqualified selections, full roster
102 103 104
Time step t
0.00
0.25
0.50
0.75
1.00
Share of unqualiﬁed selections
(moving average, one pass) (d) Share of unqualified selections, ladder roster
101 102 103 104
Time step t
0.00
0.25
0.50
0.75
1.00
Fraction of runs
(e)i ∗ is the unique most selected provider, full roster
102 103 104
Time step t
0.00
0.25
0.50
0.75
1.00
Fraction of runs (f)i ∗ is the unique most selected provider, ladder
roster
Figure 5: GSM8K long horizon: identification ofi∗ under every routing rule. Shares are moving averages with
window sizeK, exploration steps included, median over30independent runs with a10–90%band; the bottom
row is the fraction of runs in whichi∗ has strictly more selections than every other provider. Vertical lines
mark one pass and the identification horizonTid. On the full roster the two listed-price rules coincide.
44

Platform
Uniform among eligible
Lowest listed price among eligible
Lowest listed price, no quality ﬁlter
No quality ﬁlter
One pass over the benchmark
Identiﬁcation horizon Tid
101 102 103 104
Time step t
4
6
8Number of eligible providers
|Q| = 3
(a) Number of eligible providers, full roster
102 103 104
Time step t
4
6
8
10
12Number of eligible providers
|Q| = 3 (b) Number of eligible providers, ladder roster
Figure 6: GSM8K long horizon: the number of providers not yet ruled out by the quality filter under every
rule, median over30independent runs with a10–90%band. The two rules without a filter stay atN; the
listed-price rule inside a quality set learned with the same filter rules out only the providers it samples before
settling oni ∗; the dash-dotted line marks|Q|.
Table 7: GSM8K long horizon: outcomes atT = 70,000, means over30independent runs. Shares of i∗ and of
unqualified selections are cumulative unless marked as moving averages and include the exploration steps; “i∗
most selected” is the fraction of runs in whichi∗ is the unique most selected provider;| ˆQt| is the number of
eligible providers atT. Generation cost and amount paid are cumulative per query; for the platform the
amount paid includes the exploration steps.
Policy
Share
ofi ∗
Moving
avg.
Unqualified
shareR qual t /t R gen t /t Generation cost Amount paid i∗ most selected| ˆQt|
Full roster
Platform 0.899 0.964 0.054 0.0056 1.077 17.1 28.2 1.00 3.0
Uniform among eligible 0.314 0.333 0.057 0.0059 12.580 28.6 35.7 0.30 3.0
Lowest listed price
among eligible
1.000 1.000 0.000 0.0000 0.001 16.1 20.1 1.00 9.0
Lowest listed price, no
quality filter
1.000 1.000 0.000 0.0000 0.001 16.1 20.1 1.00 9.0
No quality filter
(ablation)
0.061 0.029 0.935 0.1466 0.219 13.8 13.8 0.00 9.0
Ladder roster
Platform 0.914 0.970 0.048 0.0070 3.643 37.9 50.5 1.00 3.2
Uniform among eligible 0.319 0.334 0.044 0.0064 44.670 78.9 98.6 0.33 3.0
Lowest listed price
among eligible
0.992 1.000 0.008 0.0016 0.004 34.3 42.8 1.00 9.0
Lowest listed price, no
quality filter
0.000 0.000 1.000 0.3355 0.004 15.5 19.4 0.00 12.0
No quality filter
(ablation)
0.022 0.007 0.974 0.2934 0.609 18.5 18.5 0.00 12.0
45

Platform
Uniform among eligible
Lowest listed price among eligible
Lowest listed price, no quality ﬁlter
No quality ﬁlter
One pass over the benchmark
Identiﬁcation horizon Tid
101 102 103 104
Time step t
15
20
25
30
Generation cost per query ($)
(moving average, one pass)
¯ci∗ = 16 .1
(a) Generation cost per query, full roster
102 103 104
Time step t
20
40
60
80
Generation cost per query ($)
(moving average, one pass)
¯ci∗ = 34 .4 (b) Generation cost per query, ladder roster
101 102 103 104
Time step t
0
10
20
30
40
50
Amount paid per query ($)
(moving average, after initialization)
¯ci∗ = 16 .1
¯vi∗ = 20 .1
¯c(2) = 34 .4
(c) Amount paid per query, full roster
102 103 104
Time step t
0
20
40
60
80
100
Amount paid per query ($)
(moving average, after initialization)
¯ci∗ = 34 .4
¯vi∗ = 43 .0
¯c(2) = 68 .7 (d) Amount paid per query, ladder roster
Figure 7: GSM8K long horizon: generation cost per query as a moving average with window sizeK (top) and
amount paid per query as a moving average with window sizeK over the steps after initialization (bottom),
under every rule, median over30independent runs with a10–90%band. Monetary quantities are in units of
10−6 USD. The reference lines mark¯ci∗, the mean query price¯vi∗ of i∗ and ¯c(2). The platform’s paymentπt
includes its exploration steps atcmax, which are most of the steps early in the run; the vertical axis of the
bottom panels is cut, so the platform’s curve enters from above.
46

Table 8: GSM8K exploration steps of the platform, means over30independent runs, over one pass and over
the long run ofT = 70,000queries. Shares are of the steps after initialization; payments and costs are per
step of the corresponding horizon, the long-run values as moving averages with window sizeK at T. The last
two rows give the platform’s moving-average paymentπt on non-exploration steps and over all steps atT,
per query.
Quantity Full roster Ladder roster
one pass long run one pass long run
Exploration steps (mean) 314 3,458 422 3,348
Share of exploration steps after initialization 0.240 0.049 0.323 0.048
Share of exploration steps atT(moving avg.) – 0.036 – 0.030
Exploration-step payment per step 24.40 3.73 95.92 9.14
Exploration-step generation cost per step 6.58 1.27 22.26 3.01
Share of exploration steps given toi∗ 0.057 0.005 0.047 0.006
Share of exploration steps given to unqualified providers 0.408 0.037 0.641 0.307
Paymentπ t atT, non-exploration steps (moving avg.) – 27.52 – 44.27
Paymentπ t atT, all steps (moving avg.) – 30.25 – 52.09
47

E.4 Regret and theoretical bounds
Platform
Uniform among eligible
Lowest listed price among eligible
Lowest listed price, no quality ﬁlter
No quality ﬁlter
One pass over the benchmark
Identiﬁcation horizon Tid
101 102 103 104
Time step t
10−4
10−3
10−2
10−1
Rqual t /t
(a) Average quality regret, full roster
102 103 104
Time step t
10−3
10−2
10−1
Rqual t /t (b) Average quality regret, ladder roster
101 102 103 104
Time step t
10−3
10−2
10−1
100
101
Rgen t /t ($)
(c) Average generation regret, full roster
102 103 104
Time step t
10−2
10−1
100
101
Rgen t /t ($) (d) Average generation regret, ladder roster
Figure 8: GSM8K long horizon: average quality regretRqual t /t and average generation regretRgen t /t of every
routing rule, median over30independent runs with a10–90%band, on logarithmic axes. Monetary quantities
are in units of10−6 USD. The platform’s regrets include its exploration steps.
48

Platform, realized (median)
10–90% band across runs
Bound, anytime branch
Bound, gap-dependent branch
One pass over the benchmark
Identiﬁcation horizon Tid
101 102 103 104
Time step t
100
101
102
103
104
Cumulative Rqual t
(a) Quality regret, full roster
102 103 104
Time step t
101
102
103
104
Cumulative Rqual t (b) Quality regret, ladder roster
101 102 103 104
Time step t
102
103
104
105
106
Cumulative Rgen t ($)
(c) Generation regret, full roster
102 103 104
Time step t
103
104
105
106
107
Cumulative Rgen t ($) (d) Generation regret, ladder roster
101 102 103 104
Time step t
103
104
105
Cumulative Epay t ($)
(e) Excess payment, full roster
102 103 104
Time step t
104
105
106
Cumulative Epay t ($) (f) Excess payment, ladder roster
Figure 9: GSM8K long horizon: the platform’s cumulative quality regret, generation regret and excess payment
against their bounds, evaluated at every time step. Monetary quantities are in units of10−6 USD. The
bounds are those for the platform with exploration steps, each with an anytime branch and a gap-dependent
branch; the excess-payment bound(37) without its exploration term has a single branch. The regrets include
the exploration steps; the excess payment excludes them.
49

Table 9:GSM8Ktheoretical diagnostics of the platform over the long run (T= 70,000,30independent runs).
Realized quantities are means over runs; each regret bound is the smaller of its two branches atT, for the
platform with exploration steps. Selections and regrets include the exploration steps and are compared with
Bid(T )and the bounds that account for them; the excess payment is given without the exploration steps,
against (37) without its exploration term, and with them, against(37). The good event is checked at every
selection count of every provider; the payment bounds are those of Appendix D, checked on non-exploration
steps.
Quantity Full roster Ladder roster
Bid(T)31,977 30,010
Tid 63,740 59,735
HorizonTof the long run 70,000 70,000
Selections of providers other thani∗ after initialization (mean) 7,094 6,034
ratio toB id(T)0.222 0.201
Runs in whichi∗ is the most selected provider att= 5,0000.20 1.00
att= 10,0001.00 1.00
att=T id 1.00 1.00
att=T1.00 1.00
Rqual T , realized (mean) 392 487
bound (31) 2,924 3,349
ratio 0.134 0.145
Rgen T , realized (mean) 75,384 254,988
bound (34) 144,428 805,387
ratio 0.522 0.317
Epay T without the exploration steps, realized (mean) 612 2,956
bound (37) without its exploration term 623,706 2,121,117
ratio 0.001 0.001
Epay T incl. exploration steps, realized (mean) 235,875 777,199
bound (37) 1,637,592 5,823,569
ratio 0.144 0.133
Good event held, one pass (runs) 30 of 30 30 of 30
Good event held, long run, platform 30 of 30 30 of 30
Good event held, long run, no quality filter 30 of 30 30 of 30
Payment-bound violations, one pass (steps) 0 0
50

Table 10:GSM8Klong horizon: selections of every provider other thani∗ by the platform after initialization,
over30independent runs of T = 70 ,000queries, against its cap, Mi for an unqualified provider and
max{Li,⌈g (T )⌉ −1} for a qualified one (Lemma 9), shown as⌈g(T )⌉ −1where the exploration-step cap
exceeds Li; the last row of each roster compares the total withBid(T ). Providers are sorted by mean
generation cost, as in Table 5. Selections are the mean and the maximum over runs of the number of
post-initialization selections, exploration steps included; the exploration column is the mean number of
exploration steps among them; the last selection is the mean over runs of the step of the provider’s last
selection; the ratio is the mean number of selections divided by the cap.
Provider Gap Selections Exploration Last selection Bound Ratio
mean max (mean) (mean step)
Full roster
Llama-3.2-3Bε i = 0.0722,008 3,240 16 4,182M= 15,1410.133
Qwen2-0.5Bε i = 0.41335 59 16 280M= 2990.118
Qwen2-1.5Bε i = 0.190221 361 17 1,184M= 1,7700.125
Llama-3.2-1Bε i = 0.40051 142 17 391M= 3240.158
Llama-3-8Bε i = 0.114745 1,271 30 8,845M= 5,4660.136
Llama-3.1-8Bε i = 0.116721 1,156 32 11,280M= 5,2960.136
Qwen2.5-7B∆ i = 18.31,656 1,656 1,656 69,977L= 2,0250.818
Qwen2-7B∆ i = 21.31,656 1,656 1,656 69,978⌈g(T)⌉ −1 = 1,6561.000
All providers other thani∗ 7,094 3,440B id(T) = 31,9770.222
Ladder roster
Qwen2-1.5Bε i = 0.231181 340 16 963M= 1,1590.157
Llama-3.2-1Bε i = 0.44137 76 15 337M= 2640.140
Llama-3-8Bε i = 0.155401 820 17 1,746M= 2,8090.143
Qwen2-1.5B@2ε i = 0.153426 599 18 2,144M= 2,9100.146
Llama-3.2-1B@2ε i = 0.39545 103 18 482M= 3400.132
Llama-3-8B@2ε i = 0.136490 1,015 25 3,231M= 3,7680.130
Qwen2-1.5B@4ε i = 0.1021,059 1,334 215 49,140M= 7,1180.149
Llama-3.2-1B@4ε i = 0.36558 106 46 1,013M= 4080.141
Qwen2.5-7B@2∆ i = 34.41,334 1,334 954 69,935L= 5,5440.241
Llama-3-8B@4ε i = 0.128669 1,227 669 28,411M= 4,3560.154
Qwen2.5-7B@4∆ i = 103.11,334 1,334 1,334 69,934⌈g(T)⌉ −1 = 1,3341.000
All providers other thani∗ 6,034 3,328B id(T) = 30,0100.201
51

E.5 Payments and provider outcomes
Realized generation cost
Winning bid
Payment in non-exploration steps
Query price of the same generations
Payment πt
One pass over the benchmark
Identiﬁcation horizon Tid
101 102 103 104
Time step t
0
10
20
30
40
50
Amount per query ($)
(moving average, after initialization)
¯ci∗ = 16 .1
¯c(2) = 34 .4
¯vi∗ = 20 .1
(a) Cost, bid, payment and query price, full roster
102 103 104
Time step t
0
20
40
60
80
100
Amount per query ($)
(moving average, after initialization)
¯ci∗ = 34 .4
¯c(2) = 68 .7
¯vi∗ = 43 .0 (b) Cost, bid, payment and query price, ladder roster
Figure 10: GSM8K long horizon: the platform’s realized generation cost, the query price of the same generations
and the paymentπt, as a moving average with window sizeK over the steps after initialization, and its
winning bid and payment on non-exploration steps in the same window, median over30independent runs
with a10–90%band. Monetary quantities are in units of10−6 USD. The dotted, dash-dotted and dashed
lines mark ¯ci∗, ¯c(2) and the mean query price¯vi∗ of i∗. The vertical axis is cut;πt enters from above, since
early in the run most steps are exploration steps and paidcmax.
Table 11: GSM8K one pass: the platform’s economic quantities, mean± 95%half-width over30independent
runs. The paymentπt is over all steps; the winning bid, the payment on non-exploration steps and the second
excess-payment row are over non-exploration steps only. A provider’s payoff is its total payment minus its
total generation cost over the pass.
Quantity Full roster Ladder roster
Generation cost per query, whole pass18.68±0.05 42.10±0.36
Query price per query, whole pass23.35±0.06 52.62±0.44
Paymentπ t per query, whole pass37.03±0.29 118.10±1.49
Generation cost per query, after initialization18.67±0.05 42.01±0.36
Query price per query, after initialization23.34±0.06 52.51±0.45
Paymentπ t per query, after initialization36.58±0.29 116.43±1.51
Winning bid, non-exploration steps15.75±0.07 28.77±0.75
Paymentπ t per query, non-exploration steps15.80±0.07 28.93±0.75
Exploration-step payment per query, after initialization24.40±0.36 95.92±1.98
Share of exploration steps after initialization0.240±0.004 0.323±0.007
Excess payment per stepEpay T /T, whole pass16.676±0.238 76.051±1.524
Excess payment per query, non-exploration steps0.000±0.000 0.002±0.004
Mean provider payoff over the pass2688.6±43.6 8353.3±170.9
Lowest provider payoff over providers and runs 903.8 2814.4
52

Payment in non-exploration steps
Payment bounds
¯ci∗
¯c(2)
One pass over the benchmark
Identiﬁcation horizon Tid
101 102 103 104
Time step t
0
10
20
30
40
50Payment per query ($)
(a) Payment on non-exploration steps and its bounds,
full roster
102 103 104
Time step t
0
20
40
60
80
100Payment per query ($)
(b) Payment on non-exploration steps and its bounds,
ladder roster
Figure 11: GSM8K long horizon: the payment πt of the first run on non-exploration steps, sampled at
logarithmically spaced time steps, inside the payment bounds of Appendix D for the provider selected in that
step; sampled steps that were exploration steps are left blank. Monetary quantities are in units of10−6 USD.
The bounds depend on the selected provider’s cost and selection count, and close in as the counts grow.
Table 12: GSM8K one pass: each provider’s selections and payoff under the platform over30independent runs,
exploration steps included, with providers sorted by mean generation cost as in Table 5. The last column
counts the runs in which the provider’s payoff over the pass was negative.
Provider Selections (mean) Payoff (mean) Payoff (min) Payoff (max) Negative runs
Full roster
Llama-3.2-3B 366.6 1506.2 1264.8 1675.0 0
Qwen2-0.5B 36.3 1516.9 903.8 1872.4 0
Qwen2-1.5B 210.2 1576.2 1257.8 1877.1 0
Llama-3.2-1B 52.3 1584.3 1166.0 1943.0 0
Qwen2.5-3B (i∗) 236.0 1618.9 1243.1 1848.1 0
Llama-3-8B 128.6 2464.5 1764.6 3205.6 0
Llama-3.1-8B 118.9 2613.9 1708.6 3915.3 0
Qwen2.5-7B 85.0 5795.4 5587.7 5932.6 0
Qwen2-7B 85.0 5520.5 5261.4 5733.9 0
Ladder roster
Qwen2-1.5B 177.8 4814.9 4303.1 4955.2 0
Llama-3.2-1B 37.8 4671.6 2814.4 4881.2 0
Llama-3-8B 241.5 4908.6 4503.1 5163.9 0
Qwen2-1.5B@2 189.9 5156.8 4516.7 5882.3 0
Llama-3.2-1B@2 45.8 5225.4 4016.8 5863.3 0
Qwen2.5-7B (i∗) 165.2 5567.6 4594.4 6821.7 0
Llama-3-8B@2 121.9 6622.6 5220.5 7875.4 0
Qwen2-1.5B@4 80.2 11988.5 6944.9 16058.1 0
Llama-3.2-1B@4 53.6 10912.0 3421.6 16011.6 0
Qwen2.5-7B@2 69.2 15030.6 10862.7 15919.4 0
Llama-3-8B@4 68.0 14278.0 13922.0 14696.6 0
Qwen2.5-7B@4 68.0 11062.7 10464.0 11551.1 0
53

F GPQA weak-competition experiments
This section reports the completeGPQA results for the full and ladder rosters, in the same form as theGSM8K
section; Appendix D provides the experimental details, and the platform runs with the exploration rule
described there. One-pass results are averaged over30independent runs, paired across rules and reported
with95%confidence intervals, while long-horizon trajectories report the median and10–90%range over30
independent runs. Monetary quantities are per query unless stated otherwise. A moving average has window
size K, one pass over the benchmark,i.e.,546steps on the full roster and545on the ladder roster, where
the reward alignment drops one question. The amount paid follows the convention of Appendix E. On both
rosters the identification horizonTid lies beyond the long run ofT = 70,000queries, so the long-horizon
results describe learning before that horizon, and no vertical line marks it in the figures. On both rosters
¯c(2) lies above the mean query price¯vi∗ of i∗, as on GSM8K, but here unqualified providers remain inˆQt
throughout the run, so the payment on non-exploration steps does not approach¯c(2); the strong-competition
roster of Appendix G is theGPQAsetting in which it does.
F.1 Providers and environment
i∗ Other qualiﬁed provider Unqualiﬁed provider Lowest listed price
15 30 45 60
Expected query price ($)
0.00
0.05
0.10
0.15
0.20
0.25
0.30
Quality
Qwen2-0.5B
Llama-3.2-1B
Qwen2.5-3B
Qwen2-1.5B
Llama-3.1-8B
Llama-3.2-3B
Qwen2.5-7B
Qwen2-7B
Llama-3-8B
Θ = 0 .079
(a) Quality against mean query price, full roster
80 160 240
Expected query price ($)
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
Quality
Llama-3.2-1B
Llama-3.2-1B@2
Qwen2-1.5B
Llama-3.2-1B@4
Qwen2-1.5B@2
Qwen2.5-7B
Qwen2-1.5B@4
Qwen2.5-7B@2
Qwen2.5-7B@4
Llama-3-8B
Llama-3-8B@2
Llama-3-8B@4
Θ = 0 .2396 (b) Quality against mean query price, ladder roster
Figure 12: GPQA providers. Each point is one provider at its qualityqi and mean query price; the dotted
line is the quality thresholdqmin, and the ring marks the provider with the lowest listed price. Monetary
quantities are in units of10−6 USD. On the full roster the lowest listed price belongs to a qualified provider
that is noti∗; on the ladder roster it is shared by two unqualified providers.
54

Table 13:GPQAsetting constants for the two rosters. Costs and prices are mean values per query.
Quantity Full roster Ladder roster
ProvidersN9 12
Benchmark sizeK(queries in one pass) 546 545
Quality thresholdq min 0.079 0.2396
Qualified providers|Q|8 4
i∗ Qwen2-1.5B Llama-3-8B
¯ci∗ 13.0 37.1
¯vi∗ 16.2 46.4
¯c(2) 23.6 74.2
¯c(2) −¯ci∗ 10.6 37.1
Lowest listed price Qwen2.5-3B Llama-3.2-1B, Qwen2-1.5B
qualified yes no
equalsi ∗ no no
cmax 102.4 300.0P
i /∈QMi 120,055 1,211,234P
i∈Q\{i∗} Li 17,090 5,222
⌈g(T)⌉ −11,656 1,334
Bid(T)141,210 1,218,576
Tid 315,294 2,540,927
Table 14: GPQA providers, sorted by mean generation cost. Listed price is in USD per106 output tokens;
tokens are the mean number of generated tokens per query (summed over theni generations of a Best-of-ni
provider); query price and¯ci are mean values per query. The gap isεi = qmin −q i for an unqualified provider
and∆ i = ¯ci −¯ci∗ for a qualified one, with the corresponding selection boundMi from (25) orLi from (24);
where the exploration-step cap⌈g(T )⌉ −1at T = 70,000exceeds Li, the applicable capmax{Li,⌈g (T )⌉ −1}
of Lemma 9 follows it.
Provider Listed price Tokens Query price¯c i qi Qualified Gap Bound
Full roster
Qwen2-1.5B (i∗) 0.1 162 16.2 13.0 0.152 yes – –
Qwen2-0.5B 0.1 184 18.4 14.7 0.051 noε i = 0.028M= 120,055
Qwen2.5-3B 0.065 453 29.5 23.6 0.141 yes∆ i = 10.6L= 6,861
Llama-3.2-3B 0.08 392 31.3 25.1 0.194 yes∆ i = 12.1L= 5,106
Llama-3.2-1B 0.1 368 36.8 29.4 0.108 yes∆ i = 16.5L= 2,564
Llama-3-8B 0.1455 319 46.4 37.1 0.259 yes∆ i = 24.1L= 1,085; cap 1,656
Llama-3.1-8B 0.1245 432 53.8 43.0 0.182 yes∆ i = 30.0L= 658; cap 1,656
Qwen2-7B 0.2 308 61.7 49.3 0.206 yes∆ i = 36.3L= 426; cap 1,656
Qwen2.5-7B 0.1465 433 63.4 50.7 0.197 yes∆ i = 37.7L= 390; cap 1,656
Ladder roster
Qwen2-1.5B 0.1 163 16.3 13.0 0.152 noε i = 0.088M= 9,964
Qwen2-1.5B@2 0.1 325 32.5 26.0 0.192 noε i = 0.047M= 38,751
Llama-3.2-1B 0.1 368 36.8 29.5 0.108 noε i = 0.132M= 4,063
Llama-3-8B (i∗) 0.1455 319 46.4 37.1 0.260 yes – –
Qwen2.5-7B 0.1465 433 63.4 50.7 0.197 noε i = 0.043M= 47,908
Qwen2-1.5B@4 0.1 651 65.1 52.1 0.223 noε i = 0.017M= 357,226
Llama-3.2-1B@2 0.1 736 73.6 58.9 0.151 noε i = 0.088M= 9,906
Llama-3-8B@2 0.1455 638 92.8 74.2 0.280 yes∆ i = 37.1L= 4,674
Qwen2.5-7B@2 0.1465 866 126.9 101.5 0.227 noε i = 0.012M= 705,391
Llama-3.2-1B@4 0.1 1,473 147.3 117.8 0.192 noε i = 0.048M= 38,025
Llama-3-8B@4 0.1455 1,276 185.6 148.5 0.290 yes∆ i = 111.4L= 392; cap 1,334
Qwen2.5-7B@4 0.1465 1,732 253.7 203.0 0.252 yes∆ i = 165.8L= 156; cap 1,334
55

F.2 One-pass behavior
Table 15: GPQA one-pass outcomes, mean± 95%half-width over30independent runs, paired across rules.
Generation cost and amount paid are per query; the amount paid is the paymentπt for the platform and its
ablation, and the query price for the other rules. Within one pass the quality filter rules out no provider on
either roster, so the two listed-price rules coincide.
Policy Unqualified shareR qual T /T R gen T /TAccuracy Share ofi ∗ Generation cost Amount paid
Full roster
Platform0.185±0.006 0.005±0.000 14.22±0.04 0.154±0.004 0.214±0.006 27.4±0.2 64.4±0.2
Uniform among
eligible
0.112±0.005 0.003±0.000 18.84±0.22 0.161±0.005 0.109±0.005 31.9±0.3 39.9±0.4
Lowest listed price
among eligible
0.002±0.000 0.000±0.000 10.72±0.00 0.143±0.004 0.002±0.000 23.7±0.0 29.6±0.1
Lowest listed price,
no quality filter
0.002±0.000 0.000±0.000 10.72±0.00 0.143±0.004 0.002±0.000 23.7±0.0 29.6±0.1
No quality filter
(ablation)
0.233±0.007 0.007±0.000 9.73±0.14 0.139±0.004 0.279±0.008 22.6±0.2 24.0±0.3
Ladder roster
Platform0.715±0.001 0.047±0.000 32.96±0.04 0.201±0.006 0.092±0.001 64.4±0.2 196.5±0.8
Uniform among
eligible
0.664±0.008 0.039±0.001 42.11±0.85 0.211±0.005 0.087±0.005 75.9±1.0 94.9±1.2
Lowest listed price
among eligible
0.993±0.000 0.108±0.000 0.94±0.00 0.130±0.003 0.002±0.000 22.3±0.2 27.9±0.3
Lowest listed price,
no quality filter
0.993±0.000 0.108±0.000 0.94±0.00 0.130±0.003 0.002±0.000 22.3±0.2 27.9±0.3
No quality filter
(ablation)
0.794±0.002 0.056±0.000 15.94±0.20 0.193±0.005 0.113±0.001 45.4±0.3 51.0±0.5
Platform
Uniform among eligible
Lowest listed price among eligible
Lowest listed price, no quality ﬁlter
No quality ﬁlter
22 24 26 28 30 32
Generation cost per query ($)
0.000
0.002
0.004
0.006
0.008
Quality regret per round Rqual T /T
(a) Quality regret against generation cost, full roster
20 40 60
Generation cost per query ($)
0.00
0.05
0.10
Quality regret per round Rqual T /T (b) Quality regret against generation cost, ladder roster
Figure 13: GPQA one pass: quality regret per step against generation cost per query for every routing rule,
mean with95%confidence intervals across runs. Monetary quantities are in units of10−6 USD. On both
rosters the two listed-price rules coincide, since the quality filter rules out no provider within one pass.
56

0.0 0.1 0.2
Share of time steps (95% CI across runs)
Qwen2-0.5B
Llama-3.2-1B
Qwen2.5-3B
Qwen2-1.5B ( i∗)
Llama-3.1-8B
Llama-3.2-3B
Qwen2.5-7B
Qwen2-7B
Llama-3-8B
(a) Platform selection shares, full roster
0.00 0.05 0.10 0.15
Share of time steps (95% CI across runs)
Llama-3.2-1B
Llama-3.2-1B@2
Qwen2-1.5B
Llama-3.2-1B@4
Qwen2-1.5B@2
Qwen2.5-7B
Qwen2-1.5B@4
Qwen2.5-7B@2
Qwen2.5-7B@4
Llama-3-8B ( i∗)
Llama-3-8B@2
Llama-3-8B@4 (b) Platform selection shares, ladder roster
Figure 14: GPQA one pass: share of steps the platform assigned to each provider, exploration steps included,
mean with95%confidence intervals across runs. Green marks i∗, blue the other qualified providers and
orange the unqualified providers; the platform never observes these labels.
57

F.3 Long-horizon learning and identification
Platform
Uniform among eligible
Lowest listed price among eligible
Lowest listed price, no quality ﬁlter
No quality ﬁlter
One pass over the benchmark
101 102 103 104
Time step t
0.00
0.25
0.50
0.75
1.00
Share of i∗
(moving average, one pass)
(a) Share ofi∗, full roster
102 103 104
Time step t
0.00
0.25
0.50
0.75
1.00
Share of i∗
(moving average, one pass) (b) Share ofi∗, ladder roster
101 102 103 104
Time step t
0.00
0.25
0.50
0.75
1.00
Share of unqualiﬁed selections
(moving average, one pass)
(c) Share of unqualified selections, full roster
102 103 104
Time step t
0.00
0.25
0.50
0.75
1.00
Share of unqualiﬁed selections
(moving average, one pass) (d) Share of unqualified selections, ladder roster
101 102 103 104
Time step t
0.00
0.25
0.50
0.75
1.00
Fraction of runs
(e)i ∗ is the unique most selected provider, full roster
102 103 104
Time step t
0.00
0.25
0.50
0.75
1.00
Fraction of runs (f)i ∗ is the unique most selected provider, ladder
roster
Figure 15: GPQA long horizon: identification ofi∗ under every routing rule. Shares are moving averages with
window sizeK, exploration steps included, median over30independent runs with a10–90%band; the bottom
row is the fraction of runs in whichi∗ has strictly more selections than every other provider. The vertical
line marks one pass over the benchmark; the identification horizon lies beyondT. On the full roster the two
listed-price rules coincide.
58

Platform
Uniform among eligible
Lowest listed price among eligible
Lowest listed price, no quality ﬁlter
No quality ﬁlter
One pass over the benchmark
101 102 103 104
Time step t
8.0
8.2
8.4
8.6
8.8
9.0
Number of eligible providers
|Q| = 8
(a) Number of eligible providers, full roster
102 103 104
Time step t
4
6
8
10
12Number of eligible providers
|Q| = 4 (b) Number of eligible providers, ladder roster
Figure 16: GPQA long horizon: the number of providers not yet ruled out by the quality filter under every
rule, median over30independent runs with a10–90%band. On the full roster the single unqualified provider
is never ruled out, so every curve stays atN; on the ladder roster the two rules without a filter stay atN,
and the dash-dotted line marks|Q|.
Table 16: GPQA long horizon: outcomes atT = 70,000, means over30independent runs. Shares of i∗ and of
unqualified selections are cumulative unless marked as moving averages and include the exploration steps; “i∗
most selected” is the fraction of runs in whichi∗ is the unique most selected provider;| ˆQt| is the number of
eligible providers atT. Generation cost and amount paid are cumulative per query; for the platform the
amount paid includes the exploration steps.
Policy
Share
ofi ∗
Moving
avg.
Unqualified
shareR qual t /t R gen t /t Generation cost Amount paid i∗ most selected| ˆQt|
Full roster
Platform 0.676 0.779 0.158 0.0044 4.234 17.2 27.4 1.00 9.0
Uniform among eligible 0.111 0.111 0.111 0.0031 18.785 31.8 39.7 0.10 9.0
Lowest listed price
among eligible
0.000 0.000 0.000 0.0000 10.582 23.6 29.5 0.00 9.0
Lowest listed price, no
quality filter
0.000 0.000 0.000 0.0000 10.582 23.6 29.5 0.00 9.0
No quality filter
(ablation)
0.801 0.913 0.172 0.0048 0.709 13.7 13.7 1.00 9.0
Ladder roster
Platform 0.701 0.909 0.242 0.0117 10.288 46.0 63.2 1.00 8.5
Uniform among eligible 0.117 0.161 0.533 0.0196 54.062 89.7 112.2 0.10 6.3
Lowest listed price
among eligible
0.972 1.000 0.027 0.0028 0.007 36.6 45.7 1.00 10.0
Lowest listed price, no
quality filter
0.000 0.000 1.000 0.1098 0.007 21.2 26.6 0.00 12.0
No quality filter
(ablation)
0.017 0.003 0.980 0.0847 0.635 15.8 15.9 0.00 12.0
59

Platform
Uniform among eligible
Lowest listed price among eligible
Lowest listed price, no quality ﬁlter
No quality ﬁlter
One pass over the benchmark
101 102 103 104
Time step t
15
20
25
30
35
Generation cost per query ($)
(moving average, one pass)¯ci∗ = 13 .0
cheapest listed qualiﬁed: 23.6
(a) Generation cost per query, full roster
102 103 104
Time step t
20
40
60
80
100
Generation cost per query ($)
(moving average, one pass)
¯ci∗ = 37 .1 (b) Generation cost per query, ladder roster
101 102 103 104
Time step t
0
10
20
30
40
Amount paid per query ($)
(moving average, after initialization)
¯ci∗ = 13 .0
¯vi∗ = 16 .2
¯c(2) = 23 .6
(c) Amount paid per query, full roster
102 103 104
Time step t
0
25
50
75
100
125
Amount paid per query ($)
(moving average, after initialization)
¯ci∗ = 37 .1
¯vi∗ = 46 .4
¯c(2) = 74 .2 (d) Amount paid per query, ladder roster
Figure 17: GPQA long horizon: generation cost per query as a moving average with window sizeK (top) and
amount paid per query as a moving average with window sizeK over the steps after initialization (bottom),
under every rule, median over30independent runs with a10–90%band. Monetary quantities are in units
of10 −6 USD. The reference lines mark¯ci∗, the mean query price¯vi∗ of i∗, ¯c(2) and, on the full roster, the
cost of the qualified provider with the lowest listed price. The platform’s paymentπt includes its exploration
steps atc max; the vertical axis of the bottom panels is cut, so the platform’s curve enters from above.
60

Table 17: GPQA exploration steps of the platform, means over30independent runs, over one pass and over
the long run ofT = 70,000queries. Shares are of the steps after initialization; payments and costs are per
step of the corresponding horizon, the long-run values as moving averages with window sizeK at T. The last
two rows give the platform’s moving-average paymentπt on non-exploration steps and over all steps atT,
per query.
Quantity Full roster Ladder roster
one pass long run one pass long run
Exploration steps (mean) 295 10,967 326 6,916
Share of exploration steps after initialization 0.550 0.157 0.612 0.099
Share of exploration steps atT(moving avg.) – 0.128 – 0.066
Exploration-step payment per step 55.39 13.13 179.69 19.78
Exploration-step generation cost per step 19.62 4.68 52.58 8.38
Share of exploration steps given toi∗ 0.055 0.001 0.059 0.003
Share of exploration steps given to unqualified providers 0.057 0.002 0.629 0.419
Paymentπ t atT, non-exploration steps (moving avg.) – 13.19 – 37.49
Paymentπ t atT, all steps (moving avg.) – 24.63 – 54.80
61

F.4 Regret and theoretical bounds
Platform
Uniform among eligible
Lowest listed price among eligible
Lowest listed price, no quality ﬁlter
No quality ﬁlter
One pass over the benchmark
101 102 103 104
Time step t
10−6
10−5
10−4
10−3
10−2
Rqual t /t
(a) Average quality regret, full roster
102 103 104
Time step t
10−2
10−1
Rqual t /t (b) Average quality regret, ladder roster
101 102 103 104
Time step t
100
101
Rgen t /t ($)
(c) Average generation regret, full roster
102 103 104
Time step t
10−2
10−1
100
101
Rgen t /t ($) (d) Average generation regret, ladder roster
Figure 18: GPQA long horizon: average quality regretRqual t /t and average generation regretRgen t /t of every
routing rule, median over30independent runs with a10–90%band, on logarithmic axes. Monetary quantities
are in units of10−6 USD. The platform’s regrets include its exploration steps.
62

Platform, realized (median)
10–90% band across runs
Bound, anytime branch
Bound, gap-dependent branch
One pass over the benchmark
101 102 103 104
Time step t
10−1
100
101
102
103
104
Cumulative Rqual t
(a) Quality regret, full roster
102 103 104
Time step t
100
101
102
103
104
Cumulative Rqual t (b) Quality regret, ladder roster
101 102 103 104
Time step t
103
104
105
106
Cumulative Rgen t ($)
(c) Generation regret, full roster
102 103 104
Time step t
103
104
105
106
107
Cumulative Rgen t ($) (d) Generation regret, ladder roster
101 102 103 104
Time step t
103
104
105
Cumulative Epay t ($)
(e) Excess payment, full roster
102 103 104
Time step t
104
105
106
Cumulative Epay t ($) (f) Excess payment, ladder roster
Figure 19: GPQA long horizon: the platform’s cumulative quality regret, generation regret and excess payment
against their bounds, evaluated at every time step. Monetary quantities are in units of10−6 USD. The
bounds are those for the platform with exploration steps, Theorems 7 and 8, each with an anytime branch
and a gap-dependent branch; the excess-payment bound(37) without its exploration term has a single branch.
The regrets include the exploration steps; the excess payment excludes them.
63

Table 18: GPQA theoretical diagnostics of the platform over the long run (T = 70,000,30independent runs).
Realized quantities are means over runs; each regret bound is the smaller of its two branches atT, for the
platform with exploration steps. Selections and regrets include the exploration steps and are compared with
Bid(T )and the bounds that account for them; the excess payment is given without the exploration steps,
against (37) without its exploration term, and with them, against(37). The identification horizonTid lies
beyond T on both rosters, so the corresponding row is empty. The good event is checked at every selection
count of every provider; the payment bounds are those of Appendix D, checked on non-exploration steps.
Quantity Full roster Ladder roster
Bid(T)141,210 1,218,576
Tid 315,294 2,540,927
HorizonTof the long run 70,000 70,000
Selections of providers other thani∗ after initialization (mean) 22,641 20,907
ratio toB id(T)0.160 0.017
Runs in whichi∗ is the most selected provider att= 5,0001.00 0.00
att= 10,0001.00 0.00
att=T id – –
att=T1.00 1.00
Rqual T , realized (mean) 309 818
bound (31) 3,362 14,133
ratio 0.092 0.058
Rgen T , realized (mean) 296,412 720,159
bound (34) 596,889 8,642,653
ratio 0.497 0.083
Epay T without the exploration steps, realized (mean) 1,149 2,710
bound (37) without its exploration term 623,803 2,121,051
ratio 0.002 0.001
Epay T incl. exploration steps, realized (mean) 865,643 1,564,346
bound (37) 1,798,620 5,735,545
ratio 0.481 0.273
Good event held, one pass (runs) 30 of 30 30 of 30
Good event held, long run, platform 30 of 30 30 of 30
Good event held, long run, no quality filter 30 of 30 30 of 30
Payment-bound violations, one pass (steps) 0 0
64

Table 19: GPQA long horizon: selections of every provider other thani∗ by the platform after initialization,
over30independent runs of T = 70 ,000queries, against its cap, Mi for an unqualified provider and
max{Li,⌈g (T )⌉ −1} for a qualified one (Lemma 9), shown as⌈g(T )⌉ −1where the exploration-step cap
exceeds Li; the last row of each roster compares the total withBid(T ). Providers are sorted by mean
generation cost, as in Table 14. Selections are the mean and the maximum over runs of the number of
post-initialization selections, exploration steps included; the exploration column is the mean number of
exploration steps among them; the last selection is the mean over runs of the step of the provider’s last
selection; the ratio is the mean number of selections divided by the cap.
Provider Gap Selections Exploration Last selection Bound Ratio
mean max (mean) (mean step)
Full roster
Qwen2-0.5Bε i = 0.02811,049 12,859 17 69,838M= 120,0550.092
Qwen2.5-3B∆ i = 10.61,656 1,656 1,255 69,981L= 6,8610.241
Llama-3.2-3B∆ i = 12.11,656 1,656 1,406 69,980L= 5,1060.324
Llama-3.2-1B∆ i = 16.51,656 1,656 1,649 69,980L= 2,5640.646
Llama-3-8B∆ i = 24.11,656 1,656 1,656 69,979⌈g(T)⌉ −1 = 1,6561.000
Llama-3.1-8B∆ i = 30.01,656 1,656 1,656 69,980⌈g(T)⌉ −1 = 1,6561.000
Qwen2-7B∆ i = 36.31,656 1,656 1,656 69,980⌈g(T)⌉ −1 = 1,6561.000
Qwen2.5-7B∆ i = 37.71,656 1,656 1,656 69,980⌈g(T)⌉ −1 = 1,6561.000
All providers other thani∗ 22,641 10,951B id(T) = 141,2100.160
Ladder roster
Qwen2-1.5Bε i = 0.0881,379 1,979 16 4,064M= 9,9640.138
Qwen2-1.5B@2ε i = 0.0475,486 7,649 17 12,345M= 38,7510.142
Llama-3.2-1Bε i = 0.132545 716 17 4,314M= 4,0630.134
Qwen2.5-7Bε i = 0.0432,983 3,157 27 69,918M= 47,9080.062
Qwen2-1.5B@4ε i = 0.0172,563 3,051 37 69,716M= 357,2260.007
Llama-3.2-1B@2ε i = 0.0881,281 1,456 113 59,060M= 9,9060.129
Llama-3-8B@2∆ i = 37.11,334 1,334 1,334 69,936L= 4,6740.285
Qwen2.5-7B@2ε i = 0.0121,334 1,334 1,334 69,936M= 705,3910.002
Llama-3.2-1B@4ε i = 0.0481,334 1,334 1,334 69,936M= 38,0250.035
Llama-3-8B@4∆ i = 111.41,334 1,334 1,334 69,936⌈g(T)⌉ −1 = 1,3341.000
Qwen2.5-7B@4∆ i = 165.81,334 1,334 1,334 69,936⌈g(T)⌉ −1 = 1,3341.000
All providers other thani∗ 20,907 6,897B id(T) = 1,218,5760.017
65

F.5 Payments and provider outcomes
Realized generation cost
Winning bid
Payment in non-exploration steps
Query price of the same generations
Payment πt
One pass over the benchmark
101 102 103 104
Time step t
0
10
20
30
40
Amount per query ($)
(moving average, after initialization)
¯ci∗ = 13 .0
¯c(2) = 23 .6
¯vi∗ = 16 .2
(a) Cost, bid, payment and query price, full roster
102 103 104
Time step t
0
25
50
75
100
125
Amount per query ($)
(moving average, after initialization)
¯ci∗ = 37 .1
¯c(2) = 74 .2
¯vi∗ = 46 .4 (b) Cost, bid, payment and query price, ladder roster
Figure 20: GPQA long horizon: the platform’s realized generation cost, the query price of the same generations
and the paymentπt, as a moving average with window sizeK over the steps after initialization, and its
winning bid and payment on non-exploration steps in the same window, median over30independent runs
with a10–90%band. Monetary quantities are in units of10−6 USD. The dotted, dash-dotted and dashed
lines mark ¯ci∗, ¯c(2) and the mean query price¯vi∗ of i∗. The vertical axis is cut;πt enters from above, since
early in the run most steps are exploration steps and paidcmax.
Table 20: GPQA one pass: the platform’s economic quantities, mean± 95%half-width over30independent
runs. The paymentπt is over all steps; the winning bid, the payment on non-exploration steps and the second
excess-payment row are over non-exploration steps only. A provider’s payoff is its total payment minus its
total generation cost over the pass.
Quantity Full roster Ladder roster
Generation cost per query, whole pass27.45±0.20 64.42±0.21
Query price per query, whole pass34.31±0.24 80.53±0.26
Paymentπ t per query, whole pass64.43±0.25 196.53±0.84
Generation cost per query, after initialization27.37±0.20 64.14±0.21
Query price per query, after initialization34.21±0.25 80.18±0.26
Paymentπ t per query, after initialization63.80±0.25 194.20±0.86
Winning bid, non-exploration steps16.35±0.45 26.43±0.59
Paymentπ t per query, non-exploration steps16.59±0.45 26.96±0.59
Exploration-step payment per query, after initialization55.39±0.47 179.69±1.08
Share of exploration steps after initialization0.550±0.005 0.612±0.004
Excess payment per stepEpay T /T, whole pass44.018±0.352 140.199±0.810
Excess payment per query, non-exploration steps0.182±0.042 0.000±0.000
Mean provider payoff over the pass2243.8±19.5 5999.7±40.6
Lowest provider payoff over providers and runs 1343.3 2870.6
66

Payment in non-exploration steps
Payment bounds
¯ci∗
¯c(2)
One pass over the benchmark
101 102 103 104
Time step t
0
10
20
30Payment per query ($)
(a) Payment on non-exploration steps and its bounds,
full roster
102 103 104
Time step t
0
20
40
60
80
100Payment per query ($)
(b) Payment on non-exploration steps and its bounds,
ladder roster
Figure 21: GPQA long horizon: the payment πt of the first run on non-exploration steps, sampled at
logarithmically spaced time steps, inside the payment bounds of Appendix D for the provider selected in that
step; sampled steps that were exploration steps are left blank. Monetary quantities are in units of10−6 USD.
The bounds depend on the selected provider’s cost and selection count, and close in as the counts grow; the
vertical axis is cut at1.6 ¯c(2), above which the upper bound sits atcmax in the early time steps.
Table 21: GPQA one pass: each provider’s selections and payoff under the platform over30independent runs,
exploration steps included, with providers sorted by mean generation cost as in Table 14. The last column
counts the runs in which the provider’s payoff over the pass was negative.
Provider Selections (mean) Payoff (mean) Payoff (min) Payoff (max) Negative runs
Full roster
Qwen2-1.5B (i∗) 116.7 1555.1 1343.3 1986.5 0
Qwen2-0.5B 101.1 1594.5 1435.4 1888.2 0
Qwen2.5-3B 56.5 1883.0 1560.1 2205.5 0
Llama-3.2-3B 51.4 2100.5 1593.1 2870.4 0
Llama-3.2-1B 44.2 3063.6 1996.9 3278.2 0
Llama-3-8B 44.0 2861.2 2719.4 2994.6 0
Llama-3.1-8B 44.0 2609.1 2493.5 2728.7 0
Qwen2-7B 44.0 2247.9 1844.5 2560.2 0
Qwen2.5-7B 44.0 2278.8 2122.5 2431.9 0
Ladder roster
Qwen2-1.5B 84.5 4935.4 4805.1 5068.8 0
Qwen2-1.5B@2 62.8 4886.1 4441.9 5491.0 0
Llama-3.2-1B 58.8 4942.7 4600.5 5403.9 0
Llama-3-8B (i∗) 50.3 5308.7 4857.2 5847.9 0
Qwen2.5-7B 38.7 6965.4 5994.6 7906.3 0
Qwen2-1.5B@4 39.4 6897.7 4887.2 8577.4 0
Llama-3.2-1B@2 35.3 8251.0 7355.8 8529.1 0
Llama-3-8B@2 35.0 7929.8 7581.1 8159.3 0
Qwen2.5-7B@2 35.0 6918.9 6730.4 7165.6 0
Llama-3.2-1B@4 35.0 6327.6 6072.9 6828.6 0
Llama-3-8B@4 35.0 5278.7 4828.8 5951.7 0
Qwen2.5-7B@4 35.0 3354.2 2870.6 3942.7 0
67

G GPQA strong-competition experiment
This section reports the results for the strong-competition roster onGPQA, in the same form as the two
preceding sections; Appendix D provides the experimental details, and the platform runs with the exploration
rule described there. The roster is the newest large model and the smallest model of each family, and the
threshold is placed so that both large models qualify and both small ones do not. The setting is chosen for
its payment ordering: the second-lowest qualified cost¯c(2) = 50.7lies below the mean query price¯vi∗ of i∗,
53.8, and above¯ci∗ = 43.0, so a payment that approaches¯c(2) pays the providers more than the generation
cost of i∗ and the platform less than the listed price ofi∗. Conventions are those of Appendix F; a moving
average has window sizeK = 546. The exploration-step cap atT = 70,000, ⌈g(T )⌉ −1 = 3,043, lies below
Li = 6,659of the single qualified competitor, so the cap isLi itself, and Bid(T ) = 76,846; the identification
horizonT id = 153,697lies beyond the long run, so no vertical line marks it.
G.1 Providers and environment
i∗ Other qualiﬁed provider Unqualiﬁed provider Lowest listed price
30 45 60
Expected query price ($)
0.00
0.05
0.10
0.15
0.20
Quality
Qwen2-0.5B
Llama-3.2-1B
Llama-3.1-8B
Qwen2.5-7B
Θ = 0 .1451
(a) Quality against mean query price
Figure 22: GPQA strong-competition roster. Each point is one provider at its qualityqi and mean query price;
the dotted line is the quality thresholdqmin, and the ring marks the providers with the lowest listed price,
both unqualified. Monetary quantities are in units of10−6 USD.
68

Table 22:GPQAstrong-competition setting constants. Costs and prices are mean values per query.
Quantity Strong-competition roster
ProvidersN4
Benchmark sizeK(queries in one pass) 546
Quality thresholdq min 0.1451107
Qualified providers|Q|2
i∗ Llama-3.1-8B
¯ci∗ 43.0
¯vi∗ 53.8
¯c(2) 50.7
¯c(2) −¯ci∗ 7.7
Lowest listed price Llama-3.2-1B, Qwen2-0.5B
qualified no
equalsi ∗ no
cmax 75.0P
i /∈QMi 70,187P
i∈Q\{i∗} Li 6,659
⌈g(T)⌉ −13,043
Bid(T)76,846
Tid 153,697
Table 23:GPQAstrong-competition providers, sorted by mean generation cost; columns as in Table 14.
Provider Listed price Tokens Query price¯c i qi Qualified Gap Bound
Strong-competition roster
Qwen2-0.5B 0.1 184 18.4 14.7 0.051 noε i = 0.094M= 8,074
Llama-3.2-1B 0.1 368 36.8 29.4 0.108 noε i = 0.037M= 62,113
Llama-3.1-8B (i∗) 0.1245 432 53.8 43.0 0.182 yes – –
Qwen2.5-7B 0.1465 433 63.4 50.7 0.197 yes∆ i = 7.7L= 6,659
69

G.2 One-pass behavior
Table 24: GPQA strong-competition one-pass outcomes, mean± 95%half-width over30independent runs,
paired across rules; columns and the amount-paid convention as in Table 15. Within one pass the quality
filter rules out no provider, so the two listed-price rules coincide.
Policy Unqualified shareR qual T /T R gen T /TAccuracy Share ofi ∗ Generation cost Amount paid
Strong-competition roster
Platform0.707±0.000 0.058±0.000 1.13±0.00 0.100±0.004 0.147±0.000 26.4±0.1 46.0±0.3
Uniform among
eligible
0.503±0.008 0.033±0.001 1.93±0.04 0.136±0.005 0.246±0.007 34.4±0.2 42.9±0.3
Lowest listed price
among eligible
0.996±0.000 0.066±0.000 0.01±0.00 0.085±0.004 0.002±0.000 22.1±0.2 27.6±0.2
Lowest listed price,
no quality filter
0.996±0.000 0.066±0.000 0.01±0.00 0.085±0.004 0.002±0.000 22.1±0.2 27.6±0.2
No quality filter
(ablation)
0.930±0.002 0.081±0.000 0.22±0.01 0.071±0.004 0.042±0.002 18.6±0.2 19.2±0.2
Platform
Uniform among eligible
Lowest listed price among eligible
Lowest listed price, no quality ﬁlter
No quality ﬁlter
20 25 30 35
Generation cost per query ($)
0.000
0.025
0.050
0.075
0.100
Quality regret per round Rqual T /T
(a) Quality regret against generation cost
0.0 0.2 0.4 0.6
Share of time steps (95% CI across runs)
Qwen2-0.5B
Llama-3.2-1B
Llama-3.1-8B ( i∗)
Qwen2.5-7B (b) Platform selection shares
Figure 23: GPQA strong-competition one pass: quality regret per step against generation cost per query for
every routing rule (left), and the share of steps the platform assigned to each provider, exploration steps
included (right), means with95%confidence intervals across runs. Monetary quantities are in units of10−6
USD. In the right panel green marksi∗, blue the other qualified provider and orange the unqualified providers.
70

G.3 Long-horizon learning and identification
Platform
Uniform among eligible
Lowest listed price among eligible
Lowest listed price, no quality ﬁlter
No quality ﬁlter
One pass over the benchmark
101 102 103 104
Time step t
0.00
0.25
0.50
0.75
1.00
Share of i∗
(moving average, one pass)
(a) Share ofi∗
101 102 103 104
Time step t
0.00
0.25
0.50
0.75
1.00
Share of unqualiﬁed selections
(moving average, one pass) (b) Share of unqualified selections
101 102 103 104
Time step t
0.00
0.25
0.50
0.75
1.00
Fraction of runs
(c)i ∗ is the unique most selected provider
101 102 103 104
Time step t
2.0
2.5
3.0
3.5
4.0
Number of eligible providers
|Q| = 2 (d) Number of eligible providers
Figure 24: GPQA strong-competition long horizon: identification ofi∗ under every routing rule. Shares are
moving averages with window sizeK, exploration steps included, median over30independent runs with a
10–90%band; the leader panel is the fraction of runs in whichi∗ has strictly more selections than every other
provider; the last panel is the number of providers not yet ruled out, with the dash-dotted line at|Q|. The
vertical line marks one pass over the benchmark. The two listed-price rules coincide until the filter rules out
the two cheap providers.
71

Platform
Uniform among eligible
Lowest listed price among eligible
Lowest listed price, no quality ﬁlter
No quality ﬁlter
One pass over the benchmark
101 102 103 104
Time step t
20
30
40
Generation cost per query ($)
(moving average, one pass)
¯ci∗ = 43 .0
(a) Generation cost per query
101 102 103 104
Time step t
0
20
40
60
80
Amount paid per query ($)
(moving average, after initialization)
¯ci∗ = 43 .0
¯vi∗ = 53 .8
¯c(2) = 50 .7 (b) Amount paid per query
Figure 25: GPQA strong-competition long horizon: generation cost per query as a moving average with window
size K (left) and amount paid per query as a moving average with window sizeK over the steps after
initialization (right), under every rule, median over30independent runs with a10–90%band. Monetary
quantities are in units of10−6 USD. The reference lines mark¯ci∗, ¯c(2) and the mean query price¯vi∗ of i∗.
The platform’s paymentπt includes its exploration steps atcmax; the vertical axis of the right panel is cut.
Table 25: GPQA strong-competition long horizon: outcomes atT = 70,000, means over30independent runs;
columns as in Table 16.
Policy
Share
ofi ∗
Moving
avg.
Unqualified
shareR qual t /t R gen t /t Generation cost Amount paid i∗ most selected| ˆQt|
Strong-competition roster
Platform 0.821 0.967 0.135 0.0060 0.335 41.3 47.0 1.00 2.0
Uniform among eligible 0.428 0.498 0.144 0.0063 3.291 44.1 55.1 0.60 2.0
Lowest listed price
among eligible
0.865 1.000 0.135 0.0060 0.000 41.0 51.2 1.00 2.0
Lowest listed price, no
quality filter
0.000 0.000 1.000 0.0657 0.000 22.1 27.6 0.00 4.0
No quality filter
(ablation)
0.001 0.000 0.999 0.0939 0.003 14.8 14.8 0.00 4.0
Table 26: GPQA strong-competition exploration steps of the platform, means over30independent runs, over
one pass and over the long run; rows as in Table 17.
Quantity Strong-competition roster
one pass long run
Exploration steps (mean) 253 4,005
Share of exploration steps after initialization 0.467 0.057
Share of exploration steps atT(moving avg.) – 0.033
Exploration-step payment per step 34.76 2.47
Exploration-step generation cost per step 18.30 1.70
Share of exploration steps given toi∗ 0.312 0.188
Share of exploration steps given to unqualified providers 0.375 0.051
Paymentπ t atT, non-exploration steps (moving avg.) – 47.37
Paymentπ t atT, all steps (moving avg.) – 48.28
72

G.4 Regret and theoretical bounds
Platform
Uniform among eligible
Lowest listed price among eligible
Lowest listed price, no quality ﬁlter
No quality ﬁlter
One pass over the benchmark
101 102 103 104
Time step t
10−2
10−1
Rqual t /t
(a) Average quality regret
101 102 103 104
Time step t
10−4
10−3
10−2
10−1
100
Rgen t /t ($) (b) Average generation regret
Figure 26: GPQA strong-competition long horizon: average quality regretRqual t /t and average generation
regret Rgen t /t of every routing rule, median over30independent runs with a10–90%band, on logarithmic
axes. Monetary quantities are in units of10−6 USD. The platform’s regrets include its exploration steps.
73

Platform, realized (median)
10–90% band across runs
Bound, anytime branch
Bound, gap-dependent branch
One pass over the benchmark
101 102 103 104
Time step t
10−1
100
101
102
103
104
Cumulative Rqual t
(a) Quality regret
101 102 103 104
Time step t
101
102
103
104
105
106
Cumulative Rgen t ($) (b) Generation regret
101 102 103 104
Time step t
102
103
104
105
Cumulative Epay t ($)
(c) Excess payment
Figure 27: GPQA strong-competition long horizon: the platform’s cumulative quality regret, generation regret
and excess payment against their bounds, evaluated at every time step. Monetary quantities are in units
of10 −6 USD. The bounds are those of Theorems 7 and 8 and of(37) without its exploration term, as in
Figure 19. The regrets include the exploration steps; the excess payment excludes them.
74

Table 27: GPQA strong-competition theoretical diagnostics of the platform over the long run (T = 70,000,30
independent runs); rows as in Table 18.
Quantity Strong-competition roster
Bid(T) 76,846
Tid 153,697
HorizonTof the long run 70,000
Selections of providers other thani∗ after initialization (mean) 12,508
ratio toB id(T)0.163
Runs in whichi∗ is the most selected provider att= 5,0000.00
att= 10,0000.00
att=T id –
att=T 1.00
Rqual T , realized (mean) 420
bound (31) 3,076
ratio 0.136
Rgen T , realized (mean) 23,433
bound (34) 51,268
ratio 0.457
Epay T without the exploration steps, realized (mean) 111
bound (37) without its exploration term 300,158
ratio 0.000
Epay T incl. exploration steps, realized (mean) 97,343
bound (37) 595,681
ratio 0.163
Good event held, one pass (runs) 30 of 30
Good event held, long run, platform 30 of 30
Good event held, long run, no quality filter 30 of 30
Payment-bound violations, one pass (steps) 0
Table 28: GPQA strong-competition long horizon: selections of every provider other thani∗ by the platform
after initialization, over30independent runs of T = 70,000queries, against its cap; columns as in Table 19.
Provider Gap Selections Exploration Last selection Bound Ratio
mean max (mean) (mean step)
Strong-competition roster
Qwen2-0.5Bε i = 0.0941,172 1,585 16 1,746M= 8,0740.145
Llama-3.2-1Bε i = 0.0378,293 12,542 190 10,980M= 62,1130.134
Qwen2.5-7B∆ i = 7.73,043 3,043 3,043 69,999L= 6,6590.457
All providers other thani∗ 12,508 3,249B id(T) = 76,8460.163
75

G.5 Payments and provider outcomes
Realized generation cost
Winning bid
Payment in non-exploration steps
Query price of the same generations
Payment πt
One pass over the benchmark
Payment in non-exploration steps
Payment bounds
¯ci∗
¯c(2)
One pass over the benchmark
101 102 103 104
Time step t
0
20
40
60
80
Amount per query ($)
(moving average, after initialization)
¯ci∗ = 43 .0
¯c(2) = 50 .7
¯vi∗ = 53 .8
(a) Cost, bid, payment and query price
101 102 103 104
Time step t
0
20
40
60
80Payment per query ($) (b) Payment on non-exploration steps and its bounds
Figure 28: GPQA strong-competition long horizon. Left: the platform’s realized generation cost, the query price
of the same generations and the paymentπt, as a moving average with window sizeK over the steps after
initialization, and its winning bid and payment on non-exploration steps in the same window, median over30
independent runs with a10–90%band; the dotted, dash-dotted and dashed lines mark¯ci∗, ¯c(2) and the mean
query price ¯vi∗ of i∗, and the vertical axis is cut. Right: the paymentπt of the first run on non-exploration
steps, sampled at logarithmically spaced time steps, inside the payment bounds of Appendix D for the
provider selected in that step; sampled steps that were exploration steps are left blank. Monetary quantities
are in units of10−6 USD.
Table 29: GPQA strong-competition one pass: the platform’s economic quantities, mean± 95%half-width
over30independent runs; rows as in Table 20.
Quantity Strong-competition roster
Generation cost per query, whole pass26.36±0.13
Query price per query, whole pass32.94±0.16
Paymentπ t per query, whole pass45.96±0.27
Generation cost per query, after initialization26.29±0.13
Query price per query, after initialization32.87±0.16
Paymentπ t per query, after initialization45.75±0.27
Winning bid, non-exploration steps14.66±0.32
Paymentπ t per query, non-exploration steps20.13±0.51
Exploration-step payment per query, after initialization34.76±0.00
Share of exploration steps after initialization0.467±0.000
Excess payment per stepEpay T /T, whole pass11.428±0.000
Excess payment per query, non-exploration steps0.000±0.000
Mean provider payoff over the pass2675.9±35.2
Lowest provider payoff over providers and runs 1726.3
76

Table 30: GPQA strong-competition one pass: each provider’s selections and payoff under the platform over
30independent runs, exploration steps included, with providers sorted by mean generation cost. The last
column counts the runs in which the provider’s payoff over the pass was negative.
Provider Selections (mean) Payoff (mean) Payoff (min) Payoff (max) Negative runs
Strong-competition roster
Qwen2-0.5B 306.0 2581.9 1726.3 3657.6 0
Llama-3.2-1B 80.0 3637.5 3389.7 3815.3 0
Llama-3.1-8B (i∗) 80.0 2564.5 2386.3 2730.8 0
Qwen2.5-7B 80.0 1919.8 1749.9 2130.2 0
77
