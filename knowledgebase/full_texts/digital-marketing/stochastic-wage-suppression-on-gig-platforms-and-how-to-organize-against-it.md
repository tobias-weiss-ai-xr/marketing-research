---
title: Stochastic wage suppression on gig platforms and how to organize against it
url: https://arxiv.org/abs/2604.15962
category: digital-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Ana-Andreea Stoica
- Celestine Mendler-Duenner
- Moritz Hardt
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.15962
pages: 22
chars: 76149
fetched_at: '2026-11-08T13:03:48+00:00'
kb_version: 1
---

# Stochastic wage suppression on gig platforms and how to organize against it

Stochastic wage suppression on gig platforms
and how to organize against it
Ana-Andreea Stoica1, Celestine Mendler-Dünner 1,2, and Moritz Hardt 1
1Max Planck Institute for Intelligent Systems, Tübingen, and Tübingen AI Center
2ELLIS Institute Tübingen
Abstract
Digital labor platforms are increasingly used to procure human input, ranging from annotating
data and red-teaming AI models, to ride-sharing and food delivery. A central concern in such
markets is the ability of platforms to suppress wages by exploiting the abundance of low-cost
labor. To study this exploitation pattern, we introduce a novel posted-price procurement model
with coverage objectives. A platform seeks to completeM tasks by posting prices to sequentially
arriving workers, each of whom accepts a task if it exceeds their private cost. First, we show that
under natural assumptions on the workers’ estimated cost, there exists a simple pricing strategy for
the platform to cover allM tasks with wait timeO(M ), while paying only aO(log(M )/M)fraction
of the total cost of labor. This result highlights how platforms can exploit workers’ uncertainty
about the cost of labor to effectively suppress wages. Then, we study collective action as a lever
to increase wages and promote welfare in digital labor markets. In particular, we show how a
small coalition of targeted low-cost workers who commit to a price floor forces the platform’s total
spending from logarithmic to linear inM. In contrast, a randomly sampled coalition of equal size
remains largely ineffective. We complement our theory with synthetic experiments, showcasing the
benefits of collective action across different market regimes.
1 Introduction
The rise of the gig economy has changed the way people get paid for work [Taylor et al., 2017]. Gig
platforms increasingly fragment work into hundreds of fine-grained microtasks—from labeling data and
verifying outputs of AI models to moderating online content, and delivering meals. At the same time,
employers can post wages on platforms and dynamically adapt their pricing to worker supply. As a
consequence, workers are in a position where they constantly make decisions about whether to accept a
task, or not, in a highly strategic and ever changing environment.
A growing concern is that platforms can exploit the high uncertainty of workers about task costs
to suppress wages [Hara et al., 2018, Muller, 2019]. In fact, empirical research on gig platforms shows
that workers not only exhibit high uncertainty around their own costs [Hara et al., 2018] but also
often overlook the hidden costs of searching, monitoring, and payment management [Crain et al., 2016,
Toxtli et al., 2021]. Dubal [2023] argues that employers on crowdsourcing platforms are able to exploit
this and “[...] produce unpredictable, variable, and personalized hourly pay.” However, while wage
variability and underpayment have been documented empirically, the theoretical foundations linking
pricing strategies to wage suppression remain underexplored.
Collective action—through coordinated price floors, information campaigns, or shared organizing
tools—has emerged as one of the few levers available to workers [Irani and Silberman, 2013, Woodcock,
2021, Savage et al., 2020, Sigg et al., 2025]. Our work provides a formal model that explains when
and how such coordination can counteract algorithmic wage suppression. We provide a theoretical
framework studying wage suppression on gig platforms and design interventions that mitigate worker
exploitation through coordinated action of low-cost workers.
1
arXiv:2604.15962v1  [cs.HC]  17 Apr 2026

(Highly) dispersed
market
Coordinated
market
(a) Market regimes
O(M)
Wage
suppression
O(log(M))
O(√M)) (b) Total cost as a function ofM
Figure 1: An illustration of possible market regimes and corresponding wages under a linear wait
time constraint. Dispersed markets (blue and red) are emblematic of workers’ high uncertainty over
their own costs and presence of workers willing to take arbitrarily low prices for tasks. In contrast,
coordinated markets (green) represent cases where workers have coordinated on a price floor. A
principal necessarily pays prices on the order ofO(M )in coordinated markets to achieve a linear
wait time, however, he can exploit dispersed markets and reduces his total cost to sublinear, even
logarithmic or constant with respect toM, preserving the same wait time guarantees.
1.1 Our contributions
We propose a novel procurement model to understand wage suppression due to task uncertainty. In
our model, a principal wishes to obtain the completion of tasks acrossM categories. These categories
might represent different types of data annotation (e.g., labeling images, annotating medical data)
or tasks such as red-teaming exercises for machine-learning models. The principal represents a firm1
and repeatedly posts prices with the goal of attracting workers who will complete the tasks. Workers
arrive sequentially and decide whether they are willing to complete the tasks for the given price. Upon
completion the worker obtains the posted price, and the principal incurs the corresponding cost for
payments together with the associated time they had to wait until a worker accepted the task.
More formally, the process unfolds in iterations. At the start, allM categories are active. At
iterationt, the principal posts a pricept that applies to any task from the currently active categories.
Workershaveatruecostassociatedwitheachtaskcategory, forwhichtheyhaveanoisyestimate, denoted
as theirvaluation. Workers draw their valuations from a set of distributions, one for each task category.
These distributions model the workers’ uncertainty in their cost estimate. Workers arrive sequentially
and a worker accepts a task if and only if their valuation for one of the tasks is at most the posted price.
Asuccess eventfor the principal occurs when a worker accepts a task. In this case, the principal
pays the posted pricept, and the corresponding category is removed from the active set. The process
continues with the reduced set of categories and a (possibly updated) pricept+1. Thewait timefor
iterationtis the number of workers that had to be drawn until the first success.
We show that if there is a non-negligible price floorp for each category (e.g., the market rate), the
principal must pay a total cost ofpM to ensure coverage of allM categories in finite time. However,
if such a floor does not exist (i.e., workers accept a task at arbitrarily low wages), the principal can
exploit thetailsof the valuations distributions and suppress wages while still preserving a wait time
on the order ofO(M )with high probability. We denote this strategy asstochastic wage suppression
and analyze its implications for workers’ total welfare:
• We discuss properties of the workers’ valuations distributions, connect these properties with
empirical observations in the gig economy, and formally link them to different wage suppression
regimes. Figure 1 showcases our main results: workers who have a price floor obtain a total wage
ofΘ( M ); as their uncertainty increases and low-wage workers appear, the principal can suppress
wages down to a sublinear regime, while maintaining a wait timeO(M)with high probability.
1Throughout our paper, we use the terms principal, firm, and platform interchangeably, leaving for future work the
problem whenmultiplefirms compete on the same platform for attracting workers (e.g., multiple machine learning models
competing for data annotators on MTurk or Prolific).
2

• Next we study collective efforts of workers coordinating their costs. We show that such strategies
are ineffective with only partial participation when workers are randomly recruited: if a random
α-fraction of workers coordinate on a price floor in each category, the wage suppression bounds
remain unchanged for any fixed collective of relative sizeα <1. Borrowing from labor economics
terminology, we denote this type of strategies ashorizontalstrategies, as participants are recruited
with equal probability across the entire population.
• In contrast, we show thatverticalstrategies where we recruit a specific segment of the population
are effective for a smaller number of participants: for anyα-fraction of categories, we find a
closed-form condition for the minimum budget required to design a targeted intervention for the
workers at the low-end of the valuations distributions. These targeted interventions restore wages
from any sublinear regime toΘ(M ), while maintaining a wait time ofO(M )with high probability.
Thus, building on a versatile model with minimal assumption, our work illustrates how the power of
collective bargaining is dependent on the ability of a firm to wait out high-priced workers as well as the
workers’ ability to strategically coordinate. More specifically, we compare two types of collective action:
horizontalcoordination in which workers in the collective are sampled randomly across categories versus
verticalcoordination in which workers in the collective are sampled from a specific market segment.
Whereas horizontal coordination essentially requires full worker participation to restore wages, vertical
coordination is effective with only a fraction of workers joining the collective. We complement our
theory with synthetic experiments.2
1.2 Related work
Our model is a dual to classical posted-price mechanisms [Chawla et al., 2007, Hartline and Roughgarden,
2009, Chawla et al., 2010, Babaioff et al., 2017, Dütting and Kesselheim, 2019, Jullien and Pavan, 2019],
where some works assess monopolistic tendencies of platforms [Eren and Maglaras, 2010, van Eck et al.,
2024]. In these models, workers exhibit a take-it-or-leave-it behavior based on their valuations and firms
optimize to maximize average revenue under full or partial knowledge of valuations distributions. Recent
works in this space optimize revenue regret bounds when the valuation distribution is unknown [Leme
and Schneider, 2018, Cohen et al., 2020, Liu et al., 2021, Tullii et al., 2024, Bacchiocchi et al., 2025]
or heterogeneous [Cesa-Bianchi et al., 2019, Lykouris et al., 2025], by developing dynamic pricing
algorithms that learn this distribution (for a survey see Den Boer [2015]). Our work differs in two
ways: first, it does not focus on learning the optimal pricing under no information about the valuation
distribution (but rather, it analyzes the effect of allowing quantile information to a principal to minimize
wages as a function of the market size); second, we analyze the effect of pricing strategies as the number
of tasks increases, showcasing the effect onworkers’ wagesover time, as well as the effectiveness of
collective action strategies in improving wages.
In our model, instead of a seller maximizing revenue, a buyer (the principal, for example a platform
or a model developer) minimizes procurement cost under coverage constraints by posting tasks with
associated wages. Our model draws from economic models that study monopsony power in digital
labor markets. The labor economics literature has documented that employers exercise significant
wage-setting power due to search frictions and information asymmetries, especially in so-called “thick
markets,” where there is a large number of buyers and sellers [Manning, 2013, Kingsley et al., 2015,
Naidu and Posner, 2022, Azar and Marinescu, 2024], which motivates us to analyze wages as a function
of the number of tasks set by a principal. Our posted-wage setting models truthfully gig economy
platforms like Amazon Mechanical Turk (MTurk and Upwork [AWS, Upwork], which have been shown
to exhibit substantial monopsony power. In particular, Dube et al. [2020] empirically estimates labor
supply elasticities to quantify the wage markdown on MTurk, whereas Horton and Chilton [2010]
directly estimate the workers’ reservation prices distribution properties. In contrast, our model takes a
complementary perspective by characterizing the pricing strategy a principal uses and their resulting
total cost as a function of distributional properties of the workers’ valuations.
Our model is closest in spirit to posted-price procurement models [Badanidiyuru et al., 2012, Singer
and Mittal, 2013, Singla and Krause, 2013, Charalampopoulos et al., 2025], but differs in objective and
feedback: rather than maximizing the submodular value subject to a budget while learning an estimate of
2Code is available online at https://github.com/astoica/pricing_strategies_gig_economy. All experiments use Monte
Carlo simulations of various distributions averaged over60runs and were run in Python 3.9 on local computers.
3

the optimal revenue in hindsight, we optimize the principal’s cost to ensure coverage of all categories. An
alternative framework models workers and tasks as a two-sided market with bilateral arrival uncertainty
and creates optimal mechanisms for task assignment [Dickerson et al., 2024]. We showcase that a simple
pricing strategy based on distribution quantiles knowledge allows a principal to suppress prices with
bounded guarantees. Quantile information has been recently used in pricing to show that it can lead
to robust pricing menus [Suzdaltsev, 2022, Wang, 2025]. Moreover, we analyze strategies for collective
action that prevent a principal from exploiting low-wage workers, which differs from earlier works.
Our work is inspired by recent initiatives to organize workers on gig platforms, through information
campaigns such as Turkopticon [Irani and Silberman, 2013], FairWork [Graham and Woodcock, 2018],
ShiptCalculator [Calacci and Pentland, 2022], platform interventions to set minimum wages on driving
gig economy [Parrott and Reich, 2018, Cachon et al., 2021], and self-organizing campaigns [Ongweso Jr.,
2021, Salehi et al., 2015, Savage et al., 2020, Sweeney, 2019, Umney et al., 2024] (for a survey see Sigg
et al. [2025]). Recently, collective action has gained attention in the machine learning literature where
researchers investigate new levers specific to algorithmic systems [c.f., Vincent et al., 2021, Hardt et al.,
2023, Baumann and Mendler-Dünner, 2024, Solanki et al., 2025, Gauthier et al., 2025, Zhu et al., 2025].
Most theoretical works assume randomly sampled collectives, with recent ones focused on randomly draw-
ing collectives from minority groups [Ben-Dov et al., 2025]. We refer to collectives formed by randomly
recruiting workers ashorizontalcollective action. In contrast, we refer to collectives in which workers are
recruited from a specific market segment asverticalcollective action, (in our model, in a particular task
category or set of task categories). We compare these collective action strategies in our model. This is
motivated by extensive literature on labor organizing Commons [1955], Calmfors and Driffill [1988], Ol-
son [2012] which compares economic outcomes under different collective formation principles. Our work
complements these studies by demonstrating the benefits of targeted recruiting on digital platforms.
2 Market model
We model a simple market in which there is a set of workersW. Each worker is associated with
valuations overM categories of data, denoting workers’ perceived cost for completing a task in each
category. We usefi to denote the pdf of workers’ valuations distribution for categoryi∈ [M ], with
associated CDF Di and (left) quantile Qi(u) := D−1 i (u) := inf{x : Di(x) ≥u} for u∈ [0, 1]. We
denote[ M ] = {1, 2,· · ·, M}. Hence, the workers’ valuations are i.i.d. draws from a product distribution
D = D1 × · · · ×DM and bounded in[0, 1]. We assume the workers behave rationally and accept a task
that pays higher than their valuation (they have a positive profit), keeping the option to defer at zero
profit.3 As such, the valuations are equivalent to areservation price, a canonical quantity in models
of labor markets that represents the minimum price for which a worker would accept a task [Manski
and Straub, 1999, Burbano, 2016, Krueger and Mueller, 2016].
The principal wishes to complete a setA of M tasks. To this end, they post a sequence of pricesp=
(p1, . . . , pM ). For each pricept ∈ p, workers arrive sequentially and decide whether to complete one of the
remaining tasksa∈A or to defer. The pricept remains posted until the task is completed. Once a task is
completed it is removed from the active setA. The number of deferred events at pricept is denoted asNt.
This leads to the dynamic outlined in Algorithm 1. We denote byqt the probability of obtaining a com-
pleted task in iterationt, which depends on the pricing strategy and the workers’ valuation distributions.
Wait time constraint.A central quantity in our model is the wait time. Thewait timefor the
principal, for a sequence of pricespis
W AIT(p) =
X
t
Nt.(1)
Canonical works in matching markets and labor economics show that price and wait time for task
uptake are often at a trade-off [Mortensen and Pissarides, 1999, Mertikopoulos et al., 2020] and wait
time varies as a function of market size [Ashlagi et al., 2019]. To navigate this, empirical studies of the
gig economy also show that employers often impose a wait time constraint through algorithmic means
or penalties [Maffie, 2024, Johnston et al., 2024].
3Alternatively, a worker can choose the category with the largest margini∗ = argmaxj∈At pt −v j, noting that our
results hold since prices are postedex-ante.
4

Algorithm 1:Platform-worker interaction
Input:Start withA 1 = [M]. Define a sequence of pricesp:
1Fort≥1proceed as follows:
1. The principal posts a pricept for the completion of a task in the set of active categoriesAt.
2. Repeat until success:
(a) A worker is drawn uniformly at random from a distribution of workers. The worker is
characterized by a valuation profilevwithv j ∼D j,∀j, each drawn independently.
(b) A “success” event is defined as
S= 1

∃j∈A t :v j ≤p t

.
Namely, there is a categoryjfor which the worker’s valuationvj—a proxy for his cost of
the task—is lower than the principal’s posted pricept.
•IfS= 1, the worker completes a task for one of the available categories
i∗ ∈ {j∈At :v j ≤p t}
•IfS= 0a new worker is sampled, independently, and the process repeats from (a).
3. The principal payspt and the categoryi∗ gets removed from the set of categories that the
principal is willing to pay for in the future:
At+1 =A t\{i∗}.
We advance to iterationt+ 1as long asA t+1 ̸=∅. LetN t count the number of unsuccessful
events that occurred at stept.
In the following, we are interested in pricing strategies that guarantees the firm a linear expected
wait time as a function ofM, i.e.,
∃C >0 :E[W AIT(p)]< CM∀M,(2)
where randomness comes from the stochastic arrival process. Under this constraint a principal may
care about the cost-time trade-off. We are particularly interested in this trade-off in the regime of large
M given the proliferation of microtasks in digital crowdwork platforms, whose number and diversity in
categories continues to expand [Alkhatib et al., 2017, Wood et al., 2019, Gray and Suri, 2019] as well
as the rapid expansion of the gig economy into new market segments [Garin et al., 2023].
Payment and wage suppression.The principal’stotal costfor a pricing strategypis the sum of
the prices for all the success events (note that we are guaranteed a success event in each price stage by
definition of the model, what varies is the wait time):
COST(p) =
MX
t=1
pt (3)
We assume that the platform does not take a cut, so the principal’s total cost equals the total
wages earned by workers. Without much information about the workers’ valuations, a principal is
limited in their ability to minimize cost and therefore may use a noisy statistic such as pricing at the
mean, median, or simply pay the maximum allowed price. Since valuations lie in[0, 1], paying a total
cost of M guarantees a wait time of exactlyM. By contrast, access to information about valuation
distributions allows a price-conscious principal to strategically ‘wait out’ higher-priced workers and
therefore pay below-market wages (a strategy observed in markets where employers have significant
information about workers’ reservation prices or labor supply [Allon et al., 2012, Cachon et al., 2021]).
We refer to regimes in which total payments scale sublinearly inM as regimes ofwage suppression.
We show that depending on the shape of the valuation distributions, even partial information—such
5

as oracle access to quantile values—allows a principal to achieve sublinear total payments, including
logarithmic or constant regimes in certain cases.
2.1 Workers’ task valuations
In our setup, the workers have valuations that correspond to their perceived cost for completing a task
from a given category. The distributionsDi for i∈ [M ]model the workers’ uncertainty over their own
costs: for example, if a categoryi corresponds to annotating images on Mechanical Turk, the workers
will estimate their market rate ofp dollars per hour for this task category. In our model, the properties
of these distributions characterize different market regimes and determine the principal’s ability to
suppress wages. We discuss some key characteristics of these distributions.
Dispersion.In reality, in many market segments workers have uncertainty over their costs and thus
exhibit high dispersion of perceived costs, a phenomenon observed by measuring workers’ heterogeneity
in reported reservation prices [Chen et al., 2025]. In online markets, unpaid work is shown to increase
workers’ uncertainty over their costs [Gray and Suri, 2019, Saito et al., 2019, Toxtli et al., 2021] and
lead to highly dispersed reported bids or accepted wages. We exemplify this case through the uniform
distribution Unif[0, 1]. In contrast, a market with no uncertainty overp would be equivalent to setting
Di as the Dirac distribution atp (v∼δ p). Highly dispersed markets are vulnerable to wage suppression.
A principal is able to exploit the positive mass of low-priced workers (who accept a task at arbitrarily
low wages) and benefits from a pricing strategy that pays significantly under the mean or median.
We provide conditions for distributions that exhibit dispersion to be exploited. In contrast, more
concentrated distributions are more resilient to wage suppression. We illustrate dispersed markets in
blue and red in Figure 1.
Right-skew.A prevalent case in online markets features valuations heavily skewed toward zero, i.e., a
significant mass of workers accept tasks at arbitrarily low wages. Empirically, reservation prices often
exhibit high skewness [Krueger and Mueller, 2016] (often exogenous to the market and influenced by
previous wages and time in unemployment). In online markets specifically, wages are often skewed
towards the low-earners [Horton and Chilton, 2010, Hara et al., 2018, Hornuf and Vrankar, 2022] with
reported wage depreciation due to unpaid work. We note that such markets are particularly vulnerable
to wage suppression by a principal who strategically sets low prices. We exemplify this case with the
Beta(a<1,1 )distribution and give a condition based on left-tail properties to show that a principal
can achieve a constant total cost as a function ofMin such vulnerable market regimes.
Tail properties.In our setting, the relevant behavior for characterizing wage suppression is the
distributions’ behavior near zero: we characterize the rate of growth of the total cost under strategic
pricing as a function of tail growth rate near0(i.e., a function characterizing the spread of workers
who take arbitrarily low prices). An important special case is when there is a price floorp∗, i.e. a price
below which no single worker will perform the task, and thus there is no left tail near0. When the
market value is positive and accurately reflects workers’ cost, this essentially imposes afloor reservation
price, seen in empirical studies of labor markets [Krueger and Mueller, 2016] and collective action [Jäger
et al., 2025]. We call these marketscoordinated marketsand illustrate this case in green in Figure 1.
As we will see the existence of a price floor makes markets resilient to wage suppression, limiting a
principal’s ability to strategically suppress prices while preserving his wait time guarantee.
Next, we analyze a natural and versatile pricing strategy that guarantees linear expected wait
time for any valuation distribution. For this strategy, we are interested in characterizing payments in
different market regimes by analyzing the limit dependence of the principal’s cost onM.
3 Stochastic wage suppression strategy
We propose a general pricing rule that ensures that the expected wait time isO(M )with high probability
for any valuation distribution. It is based on evaluating the left quantiles of the distribution, assuming
that partial knowledge through oracle access is available to the principal:
Definition 3.1(Stochastic wage suppression).We define the stochastic wage suppression pricing
strategy pSWS by setting the posted price at iterationt to the θ/|At| quantile of the workers’ valuations
6

distributions:
pt = max i∈At Qi
 θ
|At|

t= 1,2, . . . , M,(4)
for some θ∈ (0, 1]. In our model, exactly one category is removed at each iteration, so|At| = M−t + 1
by construction.
We denote this strategy as thestochastic wage suppression pricing strategybecause it exploits the
tails of the valuation distribution to reduce payments for the principal.
3.1 Linear wait time guarantee
Our first main result is that thepSWS satisfies the linear expected wait time constraint(2) for any
valuation distribution. To show that, we note a sufficient condition that lower-bounds the probability
of success for each iteration:
Lemma 3.2(Lower bound on success probability).For the stochastic wage suppression pricing strategy
pSWS, there exists a constantq∗ > 0independent of M for which the success probabilities satisfy
qt ≥q ∗,∀t∈[M].
Proof.We can compute the success probabilities as
qt = 1−
Y
i∈At

1−D i(pt)

≥1−

1− θ M−t+1
M−t+1
≥1−e −θ =:q ∗,∀t∈[M],
(5)
since for each activei, Di

pt

≥D i

Qi(θ/|At|)

= θ/|At|. By construction, |At| = M−t + 1,∀t∈ [M ].
Independence across categories givesqt = 1 − Q i∈At (1 −D i(pt)) ≥ 1 − (1 −θ/|A t|)|At| ≥ 1 −e −θ. Here
we used that(1 −θ/x )x ≤e −θ,∀x, θ >0. The Nt are Geometric random variables since the process is
sequential and each worker is drawn independently,Nt ∼Geom(q t)on{1,2, . . .}.
Theorem 3.3(Wait time).Consider the stochastic wage suppression strategypSWS defined in Defini-
tion 3.1, and letq∗ = 1−e −θ. Then
E[W AIT(pSWS)]≤ M q∗ =O(M).(6)
Moreover, the iteration-wise wait times{Nt}M t=1 are independent sub-exponential random variables with
parameters depending only onq∗. Hence, for anyδ∈(0,1),
W AIT(pSWS) =O  M+ p Mlog(1/δ) + log(1/δ)  (7)
with probability at least1−δ.
Proof sketch.We use a standard result on Geometric random variables that are sub-exponential with
ψ1-norm bounded by a constant depending only onq∗ (shown in Lemma A.1 in the Appendix). We then
use the independence of the wait times at every iteration to compute the total wait time in expectation
as E[W AIT(pSWS)] ≤M/q ∗. Finally, we show that the total wait timeW AIT(pSWS) = P t Nt satisfies a
Bernstein (sub-exponential) tail and we use Bernstein’s inequality to prove the concentration bound.
The pSWS strategy has a natural interpretation through quantile access at the inverse number of
active categories, which gives the constant lower bound of success in each iteration. WhenM = 2,
pSWS is pricing at the median forθ = 1; as M increases, access to lower quantile values allows the
principal to price under the median while maintaining the wait time. Figure 2 shows the total wait
time under thepSWS strategy, noting that theO(M )time guarantee holds, with different constants
depending on the exact valuations distributions.
7

0 250 500 750 1000 1250 1500 1750 2000
M categories
0
500
1000
1500
2000
2500
3000
3500T otal completion time
Uniform
Gaussian
Exponential
Beta(2,1)
Figure 2: Total wait time for thepSWS pricing strategy for different distributions, asMvaries.
3.2 Total payments
While holding the expected wait time fixed, the stochastic wage suppression pricing strategy achieves
a different total cost depending on the distribution of valuations among workers. In the following we
use the characteristics outlined in Section 2.1 to describe different cost regimes.
No wage suppression.In coordinated markets where all workers have a minimum positive market
price for each categoryi∈ [M ](e.g., there is a minimum wage requirement or there is no uncertainty
or dispersion in the workers’ costs), the principal pays a total price ofΘ(M ). We characterize this
property as a sufficient condition on the total cost bound below:
Lemma 3.4(Linear total cost).For each categoryi, let gi := inf{x∈ [0, 1] : Di(x) > 0} denote the
left endpoint of the support (informally, the gap at zero price). There is a positive left gap if
g∗ := min i∈[M] gi >0.(8)
For any distributions{Di}i∈[M] with property(8), the pSWS pricing strategy pays a total cost ofΘ(M ).
Examples of such distributions include point-mass distributions atpj > 0for each category j (e.g.,
a collective contract that sets wages in each market segment) or truncated distributions for which there
is no worker density below a price floorp >0. Such markets can occur naturally when the workers do
not have uncertainty over their costs.
Sublinear wage suppression regime.Empirical research shows that markets in the gig economy
are not often coordinated. Without the positive left gap property, we transition to a regime where the
total cost will achieve a sublinear bound:
Lemma 3.5(Sublinear total cost).If for eachi∈[M],
inf{x∈[0,1] :D i(x)>0}= 0,(9)
thep SWS pricing strategy pays a total cost ofo(M).
A large array of distributions fall under this regime. For example, CDFs with polynomially vanishing
density at0such as a power left tail:∃a >1, K >0s.t. D(x) = Kx a(1 + o(1))as x→ 0. A specific
example is theBeta(a >1, 1)distribution, noting that varyinga achieves a sublinear boundΘ(M 1−1/a)
with any exponent (see Observation A.2 in the Appendix for computation and further examples). As
such, a positive density at0implies a phase transition in the total wages to become sublinear.
Logarithmic wage suppression regime.A further transition occurs when the left tail grows linearly,
as a special case of the aforementioned polynomial; in this regime, the stochastic wage suppression
strategy achieves a total cost bound ofO(log(M )). As described in Section 2, this regime can be
exemplified ashigh dispersion marketswhere workers have high uncertainty over their costs. We state
a distribution-agnostic sufficient regularity condition that allows a strategic principal to achieve a cost
of O(logM )while preserving the linear wait time guarantee. Informally, this condition implies a “linear
left-tail growth,” i.e.,D i(x)≳xnear0.
8

Lemma 3.6(Logarithmic total cost).We denote by left-tail regularity the following condition: there
exist constantsc >0andx 0 ∈(0,1]such that for alli∈[M]and allx∈[0, x 0],
Di(x)≥c x.(10)
Equivalently, for all u∈ [0, cx0], Qi(u) ≤u/c , or P(vi < 1/t) = Ω(1/t),∀t∈ [M ]. For any distributions
{Di}i∈[M] with property 10, thepSWS pricing strategy pays a total cost ofO(log(M)).
Examples of distributions that fall under property 10 are the uniform distribution, the exponential
distribution, and any left-skewed power law with a heavy tail, such asBeta(1, b)for b < 1(see
Observation A.3 in the Appendix for exact computations).
Constant wage suppression regime.A further phase transition occurs where there is a significant
mass concentrated near0(so, most workers will have valuations arbitrarily close to0): in this regime,
the principal’s pricing strategy suppresses wages down to a total cost ofO(1)with respect to M. This
regime is emblematic of distributions exhibiting aright-skewdescribed in Section 2, which character-
izesvulnerable markets. We express a formal criterion below, with a generalization in the Appendix
(Proposition A.4).
Lemma 3.7(Constant total cost).If distributions Di have a heavier than linear left tail, such as a
polynomial,∃x 0 ∈(0,1], b∈(0,1), c >0s.t.∀i∈[M], x∈[0, x 0]
Di(x)≥c x b.(11)
Equivalently, for all u∈ [0, cx0], Qi(u) ≤ (u/c)1/b, or P(vi < 1/t) = Ω( t−b),∀t∈ [M ]. For any
distributions {Di}i∈[M] with property 11, thepSWS strategy pays a total cost ofO(1)with respect to M.
In addition, any distribution with an atom at0will also satisfy the same properties from Lemma 3.7.
We remark on the phase transition that the principal’s strategy achieves: without collective action,
pricing at the quantiles obtains sublinear total cost for the principal; depending on the exact distribution
family, the total cost can vary from any sublinear bound, down to a logarithmic, and even a constant
wage suppression regime as a function ofM. These regimes mirror reported empirical properties of
workers’ valuations distributions in the gig economy. We provide sufficient conditions to characterize
the principal’s ability to suppress wages in different regimes. Figure 4 presents the total cost thatpSWS
achieves for different regimes (top row, in blue forα = 0, equivalent to no collective action). Different
wage suppression regimes are exemplified through different distributions:O(1)in panel (a), O(log(M ))
in panels (b)-(c) andO(M1/2)in panel (d) for the total cost.
Remark 3.8(A note on cost optimality).The pSWS strategy is cost-optimal among all strategies
satisfying the per-iteration success probability constraintqt ≥q ∗ when distributions are identical across
categories. This follows directly: with|At| = M−t + 1categories at iteration t, the minimum price
ensuring qt ≥q ∗ is pt = Q  1−(1−q ∗)1/|At| , which is exactly the price defined by thepSWS strategy.
When these distributions come from a heterogeneous family of distributions, the principal may further
optimize his cost by exploiting the heterogeneity (e.g., via contextual bandits [Lykouris et al., 2025]).
Methods for optimizing the absolute cost of the principal are left for future work.
4 Horizontal collective action fails to prevent wage suppression
In this section, we exploreuntargetedcollective action strategies: in these strategies, a random
fraction of the workers coordinate on a price floor (similar to the process described in Hardt et al.
[2023]), essentially only accepting tasks that are offered by the principal above a certain price. If all
workers fully coordinate on all categories, that imposes a minimum price floor and thus prevents wage
suppression as the total cost isΘ(M ). Here, we are interested in the power of the collective as a
function of its size.
Horizontal α-fraction coordination.Let α∈ [0, 1)denote the participation rate in the collective. A
collective sets a category-specific minimum pricepj,∀j∈ [M ]. Since each arriving worker independently
9

belongs to the collective with probabilityα,4 we model their valuations as drawn from the mixture
distribution:
vj ∼(1−α)·D j +α·δ pj ,(12)
where δpj is a point mass at the collective-set pricepj ∈ [0, 1]. Then, the CDF of this mixture
distribution is
Dmix j (x) = (1−α)·D j(x) +α·1{x≥ pj}, x∈[0,1].(13)
We show that under this data-generating distribution, the stochastic wage suppression pricing
strategy achieves a wait time for the principal ofO(M )with high probability, no matter the size of
the collective (the value ofα). Essentially, the random collectivesthinthe arrival rate of successful
workers, but leave a positive mass of workers who take up a task at low prices which can continue to
be exploited by a principal with only a constant factor in the wait time.
Lemma4.1.Letp SWS α denote the SWS pricing strategy applied to the mixture distributions{Dmix j }j∈[M].
Then
E[W AIT(pSWS α )]≤ M q∗(α) =O(M),
W AIT(pSWS α ) =O  M+ p Mlog(1/δ) + log(1/δ)  (14)
with probability at least1−δ, where q∗(α) := 1 −exp

−(1 −α ) θ

and with constants depending only on
θandα.
Proof sketch.We note that the success probability in each iteration will still be lower bounded by a
constant, which now depends onα. This gives the same computation for the expected wait time, scaled
by an α-dependent constant, and the concentration inequality follows exactly like in Theorem 3.3.
Furthermore, the effect of the random collective only affects the principal’s strategy by a constant
in the total cost for anyα <1:
Lemma 4.2.Fixα∈[0,1)andθ >0, and let p− := mini∈[M] pi denote the minimum collective price
floor (assumed positive). Then, across all market regimes analyzed in Section 3,
COST(pSWS α ) = Θ  COST(pSWS)  (15)
as a function of the number of categoriesM.
Proof sketch.The mixture distribution forces the stochastic wage suppression strategy to increase prices,
as the quantile values shift: the new quantile values are either the original quantile values of the original
distributions Di shifted by a factor of1/(1 −α )(when the worker is not part of the collective), or equal
to the minimal price floorp−. In total, this shifts the total cost by a factor of1/(1 −α )that follows from
quantile reweighting under the mixture distribution and a constant addition for the collective workers.
For the regimes described in Section 3, this translates toCOST(pSWS α ) = 1 1−α COST(pSWS) + O(1)
(full proof in the Appendix). Thus, the total cost will undergo the same phase transitions as described
in the case without any collective action.
Figure 4 showcases the total cost (top row) and the total wait time (bottom row) for various values
of α for thep SWS α pricing strategy. The collective size does not affect the asymptotic growth rate of
cost or wait time, but it does change constants (computed in closed form in the Appendix): larger
collectives increase both cost and wait time by constant factors.
Remark 4.3(Information campaigns).The horizontal collective action model is inspired by decentralized
organizing mechanisms [Hardt et al., 2023, Umney et al., 2024]. Our results show that such uncoordinated
efforts cannot overcome structural wage suppression: recruiting anything less than all low-valuation
workers preserves our bounds qualitatively, since horizontal coordination primarilythinsthe arrival
rate of low-cost acceptances. For this reason, while information campaigns have been deemed helpful for
worker organizing [Irani and Silberman, 2013, Woodcock, 2021], their efficacy may be limited if they fail to
reach essentially all lowest-paid workers. In our model, information about a category’s market price may
reduce variance yet still leave tail properties that sustain sublinear or constant wage suppression regimes.
4Note: this is consistent with sampling with replacement from a population with collective fractionα.
10

HorizontalVertical
Figure 3: A comparison of the total cost achieved by a horizontal collective vs a vertical collective with
a budget ofϵ= 0.01under thep SWS pricing strategy and uniform valuations distributions.
0 250 500 750 1000 1250 1500 1750 2000
M categories
2
3
4
5
6
7T otal cost
alpha=0.0
alpha=0.2
alpha=0.4
alpha=0.6
alpha=0.8
(a) Beta(0.5,1)
101 102 103
M categories (log scale)
5
10
15
20
25T otal cost
alpha=0.0
alpha=0.2
alpha=0.4
alpha=0.6
alpha=0.8 (b) Uniform
101 102 103
M categories (log scale)
2
4
6
8
10
12T otal cost
alpha=0.0
alpha=0.2
alpha=0.4
alpha=0.6
alpha=0.8 (c) Exponential,λ= 3
101 102 103
M categories (log scale)
101
102
T otal cost (log scale)
alpha=0.0
alpha=0.2
alpha=0.4
alpha=0.6
alpha=0.8 (d) Beta(2,1)
0 250 500 750 1000 1250 1500 1750 2000
M categories
0
500
1000
1500
2000
2500
3000T otal completion time
alpha=0.0
alpha=0.2
alpha=0.4
alpha=0.6
alpha=0.8
(e) Beta(0.5,1)
0 250 500 750 1000 1250 1500 1750 2000
M categories
0
2000
4000
6000
8000
10000
12000T otal completion time
alpha=0.0
alpha=0.2
alpha=0.4
alpha=0.6
alpha=0.8 (f) Uniform
0 250 500 750 1000 1250 1500 1750 2000
M categories
0
2000
4000
6000
8000
10000
12000T otal completion time
alpha=0.0
alpha=0.2
alpha=0.4
alpha=0.6
alpha=0.8 (g) Exponential,λ= 3
0 250 500 750 1000 1250 1500 1750 2000
M categories
0
2000
4000
6000
8000
10000
12000T otal completion time
alpha=0.0
alpha=0.2
alpha=0.4
alpha=0.6
alpha=0.8 (h) Beta(2,1)
Figure 4: Total cost (top row) and total wait time (bottom row) underpSWS for various values ofα
and M, for a collective price floor value of0.2and different workers’ valuations distributions. Panel (a)
highlights the O(1)total cost regime, panels (b)–(c) highlight theO(log(M ))total cost regime in log
scale, and panel (d) highlights aO(M 1/2)regime of total cost in log-log scale (dashed line represents the
0.5slope line). The total wait time isO(M )with constants depending on α and distribution families.
5 Vertical collective action as (re)distribution
In contrast to horizontal collectives,targetedcollectives strategically allocate limited organizing
resources (e.g., pointed information campaigns or price-floor agreements) to the lowest quantiles, where
wage suppression originates. In our model, this means focusing onα-fraction segments of the market
and concentrating a small “budget”ϵof organizing effort in each by targeting the lowest-cost workers.
We refer to such targeted strategies asvertical coordination, where “vertical” means organizing within
entire market segments (here, segments correspond to task categories). We draw on classical organizing
strategies in collective action: vertical collectives can be more effective in dispersed markets [Olson,
2012], can address fairness concerns in economic models [Kopel et al., 2019], and have been applied as
industry-region organizing in countries like Germany [Jäger et al., 2022]. Both recent [Diani, 2025]
and longitudinal [Martin et al., 2004, Milkman and Wong, 2001] studies show that the shift from
trade-based organizational unionizing to more heterogeneous movements across sectors can reduce
bargaining power.
Clearly, vertical coordination places workers in thecoordinated marketsregime: for anα-fraction
of categories, the intervention instills a price floor, and thus the principal must pay a total cost at
leastΘ( αM )(as property 8 is satisfied for anα-fraction of categories). We consider the fractionα a
constant and show that even for smallα, Lemma 3.4 applies and we recover the tight linear cost regime.
We next quantify the minimum budget required to deploy such targeted interventions in terms of total
variation distance on valuation distributions.
11

Theorem 5.1.Define thecritical budgetfor vertical collective action as
ϵ∗ := inf{ϵ >0 : inf
i
Qi(ϵ)>0}.(16)
For anyϵ > ϵ∗, we can construct a new set of valuations distributions{D∗ i }i∈[M] such thatTV(D∗ i , Di) ≤
ϵ for all i∈ [M ], and under which the stochastic wage suppression pricing strategy must incur total cost
COST(pSWS) = Θ(M).
Proof sketch. For any ϵ≥ϵ ∗, define the valuation distributions after vertical collective action for
categoryiby removingϵmass from the lowest-cost region and placing it at1:
D∗ i (x) := max{D i(x)−ϵ,0}forx <1, D ∗ i (1) = 1.(17)
This transformation moves at mostϵ probability mass, henceTV(D∗ i , Di) ≤ϵ . We then claim that
for every u∈ (0, 1 −ϵ ), the quantiles of the adjusted distribution satisfyQ∗ i (u) ≥Q i(u + ϵ)(proved in
Proposition A.7 in the Appendix). Next, we note that thepSWS strategy satisfies a constant probability
of success of at least1−e −θ for some θ >0in each iteration t (more precisely, forθ >1 −ϵ ), since it
is defined as
pt ≥max i∈At Q∗ i
 θ
M−t+ 1

≥max
i∈At
Qi

ϵ+ θ M−t+ 1  ≥max i∈At Qi(ϵ).(18)
Hence the total payment obeys
COST(pSWS) =
MX
t=1
pt ≥
MX
t=1
max
i∈At
Qi(ϵ)≥M·q ϵ,
whereq ϵ := min i∈[M] Qi(ϵ).
(19)
In particular, as long asqϵ > 0(a constant independent of M), the principal’s cost isΘ(M ), with a wait time ofO(M )with constants depending on ϵ. Without this condition, the principal can still
exploit tail behavior and achieve sublinear total cost: we need that the lowestϵ-mass of the distribution
is not “free”, so the workers in this region do not take arbitrarily low payments. In that case, we need a
critical budget high enough to cover the entire mass.
Remark 5.2.For clarity, in Theorem 5.1 the intervention is applied to all categories; applying it to
an α-fraction forces costΘ(αM ). We connect Theorem 5.1 with different market regimes in terms of
the critical budget necessary to prevent wage suppression:
• No campaign is needed in coordinated markets:in markets where there is already a positive
price floor (property(8)), collective action is not necessary, since the total cost isΘ(M).
• When any vertical campaign prevents wage suppression:if targeted categories have no
atom at0(and whose support’s left endpoint becomes positive after anyϵ-shift), then ϵ∗ = 0
for those categories. This can restore any sublinear wage suppression regime to a linear one,
including logarithmic and constant. This is significant as it includes a wide range of distributions,
as described in Section 3, and hence various market conditions.
• When a vertical campaign needs a minimum budget:if more than(1 −α )-fraction of the
valuations distributions have an atom at0, i.e.ϵ∗ = ρ for some ρ >0, that means that a vertical
collective must ‘move’ the entire atom in order to shift the total price fromO(1)to O(M ). This
implies a choice on the side of the decision-maker: choose a target fractionα that allows targeting
distributions without this property, or choose a high enough budgetϵ to cover the mass at0. Our
model allows a decision-maker to make this choice by providing a guarantee ofwhentargeting
works and what budget it requires.
12

This shows thepower of targeted recruitingin collective action: horizontal collectives preserve
wage suppression, whereas vertical collectives restore the cost bound toΘ(M )for any small budget as
long as anα-fraction of categories do not have an atom at0. Instead of thinning arrivals, they lift the free-
laborregion. Whensuchregionshavesignificantmass, collectivesarestilleffectiveaslongasthetargeting
budget exceeds the atom size. This difference captures the classic tension between breadth and focus
in collective action: horizontal collectives diffuse effort across many categories, while vertical collectives
spend their limitedϵ budget where it matters most—on the lowest quantiles that cause wage suppression.
Figure 3 illustrates the asymptotic difference between the power of a collective in horizontal versus
vertical coordination: for any fixedα <1, a principal can obtain theO(M )wait time guarantee with
the stochastic wage suppression strategy in horizontal coordination (in red), essentially keeping the total
cost of orderO(log(M )). However, vertical coordination (in green) quickly forces a wage increase asM
increases, even for small collective sizes and a small budgetϵ for targeting, restoring a total cost ofΘ(M ).
6 Discussion
Our work has implications for both platform designers and worker advocates. On the one hand,
it provides a versatile theoretical model for diagnosing when algorithmic pricing can lead to wage
suppression, based on the structure of workers’ perceived cost distributions. On the other hand, it offers
concrete guidance for designing collective interventions that counteract procurement power, highlighting
when and why targeted organizing can be effective.
Several open directions emerge. First, our pricing strategy could be extended to dynamic pricing
models that learn workers’ valuation distributions online from task uptake. While the stochastic wage
suppression strategy we analyze is not intended to be cost-optimal, it provides a natural benchmark
under partial distributional knowledge and reveals sharp phase transitions in workers’ wages. Second,
future work could evaluate platform-side interventions that reduce workers’ uncertainty about their
costs and study how these interact with different models of collective action, including alternative
targeting and redistribution mechanisms. In this work, we consideredα as ana priorichosen collective
fraction. The problem of dynamically adjustingα with M is also interesting as a future direction.
Third, an important empirical direction is to characterize valuation distributions in real-world platforms
and to examine how they evolve under sustained pricing strategies and organizing efforts.
Overall, our results underscore a structural asymmetry in digital labor markets: while random,
untargeted coordination tends to thin participation without altering wage suppression regimes, even
modestly targeted collective action can fundamentally change market outcomes.
Acknowledgements
Celestine Mendler-Dünner acknowledges financial support of the Hector Foundation.
References
Ali Alkhatib, Michael S Bernstein, and Margaret Levi. Examining crowd work and gig work through
the historical lens of piecework. InProceedings of the 2017 CHI conference on human factors in
computing systems, pages 4599–4616, 2017.
Gad Allon, Achal Bassamboo, and Eren B Cil. Large-scale service marketplaces: The role of the
moderating firm.Management Science, 58(10):1854–1872, 2012.
Itai Ashlagi, Maximilien Burq, Patrick Jaillet, and Vahideh Manshadi. On matching and thickness in
heterogeneous dynamic markets.Operations Research, 67(4):927–949, 2019.
AWS. Pricing. URLhttps://www.mturk.com/pricing.
José Azar and Ioana Marinescu. Monopsony power in the labor market: From theory to policy.Annual
Review of Economics, 16(1):491–518, 2024.
Moshe Babaioff, Liad Blumrosen, Shaddin Dughmi, and Yaron Singer. Posting prices with unknown
distributions.ACM Transactions on Economics and Computation (TEAC), 5(2):1–20, 2017.
13

Francesco Bacchiocchi, Matteo Castiglioni, Alberto Marchesi, and Nicola Gatti. Regret minimization
for piecewise linear rewards: Contracts, auctions, and beyond. InProceedings of the 26th ACM
Conference on Economics and Computation, pages 1020–1020, 2025.
Ashwinkumar Badanidiyuru, Robert Kleinberg, and Yaron Singer. Learning on a budget: posted
price mechanisms for online procurement. InProceedings of the 13th ACM conference on electronic
commerce, pages 128–145, 2012.
Joachim Baumann and Celestine Mendler-Dünner. Algorithmic collective action in recommender
systems: promoting songs by reordering playlists.Advances in Neural Information Processing
Systems, 37:119123–119149, 2024.
Omri Ben-Dov, Samira Samadi, Amartya Sanyal, and Alexandru Ţifrea. Fairness for the people, by the
people: Minority collective action.arXiv preprint arXiv:2508.15374, 2025.
Vanessa C Burbano. Social responsibility messages and worker wage requirements: Field experimental
evidence from online labor marketplaces.Organization Science, 27(4):1010–1028, 2016.
Gérard P Cachon, Tolga Dizdarer, and Gerry Tsoukalas. Pricing in service platforms: Who should set
the prices. Technical report, Working Paper, 2021.
Dan Calacci and Alex Pentland. Bargaining with the black-box: Designing and deploying worker-centric
tools to audit algorithmic management.Proceedings of the ACM on Human-Computer Interaction, 6
(CSCW2):1–24, 2022.
Lars Calmfors and John Driffill. Bargaining structure, corporatism and macroeconomic performance.
Economic policy, 3(6):13–61, 1988.
Nicolo Cesa-Bianchi, Tommaso Cesari, and Vianney Perchet. Dynamic pricing with finitely many
unknown valuations. InAlgorithmic Learning Theory, pages 247–273. PMLR, 2019.
Andreas Charalampopoulos, Dimitris Fotakis, Panagiotis Patsilinakos, and Thanos Tolias. A competi-
tive posted-price mechanism for online budget-feasible auctions. InProceedings of the 26th ACM
Conference on Economics and Computation, pages 1046–1075, 2025.
Shuchi Chawla, Jason D Hartline, and Robert Kleinberg. Algorithmic pricing via virtual valuations. In
Proceedings of the 8th ACM Conference on Electronic Commerce, pages 243–251, 2007.
Shuchi Chawla, Jason D Hartline, David L Malec, and Balasubramanian Sivan. Multi-parameter
mechanism design and sequential posted pricing. InProceedings of the forty-second ACM symposium
on Theory of computing, pages 311–320, 2010.
Kuan-Ming Chen, Ning Ding, John A List, and Magne Mogstad. Reservation wages and workers’
valuation of job flexibility: Evidence from a natural field experiment.Journal of the European
Economic Association, page jvaf022, 2025.
Maxime C Cohen, Ilan Lobel, and Renato Paes Leme. Feature-based dynamic pricing.Management
Science, 66(11):4921–4943, 2020.
John Rogers Commons.History of Labour in the United States, volume 4. Harvard University Press,
1955.
Marion Crain, Winifred Poster, and Miriam Cherry.Invisible labor: Hidden work in the contemporary
world. Univ of California Press, 2016.
Arnoud V Den Boer. Dynamic pricing and learning: Historical origins, current research, and new
directions.Surveys in operations research and management science, 20(1):1–18, 2015.
Mario Diani. The embeddedness of unions in collective action fields: ‘organizational’ vs ‘social movement’
unionism.Social Movement Studies, pages 1–21, 2025.
John P Dickerson, Karthik Sankararaman, Aravind Srinivasan, Pan Xu, and Yifan Xu. Matching tasks
and workers under known arrival distributions: Online task assignment with two-sided arrivals.ACM
Transactions on Economics and Computation, 12(2):1–28, 2024.
14

Veena Dubal. On algorithmic wage discrimination.Columbia Law Review, 123(7):1929–1992, 2023.
Arindrajit Dube, Jeff Jacobs, Suresh Naidu, and Siddharth Suri. Monopsony in online labor markets.
American Economic Review: Insights, 2(1):33–46, 2020.
Paul Dütting and Thomas Kesselheim. Posted pricing and prophet inequalities with inaccurate priors.
InProceedings of the 2019 ACM Conference on Economics and Computation, pages 111–129, 2019.
Serkan S Eren and Costis Maglaras. Monopoly pricing with limited demand information.Journal of
revenue and pricing management, 9(1):23–48, 2010.
Andrew Garin, Emilie Jackson, Dmitri K Koustas, and Alicia Miller. The evolution of platform gig
work, 2012-2021. Technical report, National Bureau of Economic Research, 2023.
Etienne Gauthier, Francis Bach, and Michael I. Jordan. Statistical collusion by collectives on learning
platforms. InForty-second International Conference on Machine Learning, 2025.
Mark Graham and Jamie Woodcock. Towards a fairer platform economy: introducing the Fairwork
Foundation.Alternate Routes, 29, 2018.
Mary L Gray and Siddharth Suri.Ghost work: How to stop Silicon Valley from building a new global
underclass. Harper Business, 2019.
Kotaro Hara, Abigail Adams, Kristy Milland, Saiph Savage, Chris Callison-Burch, and Jeffrey P Bigham.
A data-driven analysis of workers’ earnings on Amazon Mechanical Turk. InProceedings of the 2018
CHI conference on human factors in computing systems, pages 1–14, 2018.
Moritz Hardt, Eric Mazumdar, Celestine Mendler-Dünner, and Tijana Zrnic. Algorithmic collective
action in machine learning. InInternational Conference on Machine Learning, pages 12570–12586.
PMLR, 2023.
Jason D Hartline and Tim Roughgarden. Simple versus optimal mechanisms. InProceedings of the
10th ACM conference on Electronic commerce, pages 225–234, 2009.
Lars Hornuf and Daniel Vrankar. Hourly wages in crowdworking: A meta-analysis.Business &
Information Systems Engineering, 64(5):553–573, 2022.
John Joseph Horton and Lydia B Chilton. The labor economics of paid crowdsourcing. InProceedings
of the 11th ACM conference on Electronic commerce, pages 209–218, 2010.
Lilly C Irani and M Six Silberman. Turkopticon: Interrupting worker invisibility in Amazon Mechanical
Turk. InProceedings of the SIGCHI conference on human factors in computing systems, pages
611–620, 2013.
Simon Jäger, Shakked Noy, and Benjamin Schoefer. The German model of industrial relations: Balancing
flexibility and collective action.Journal of Economic Perspectives, 36(4):53–80, 2022.
Simon Jäger, Suresh Naidu, and Benjamin Schoefer. Collective bargaining, unions, and the wage
structure: An international perspective. InHandbook of Labor Economics, volume 6, pages 229–372.
Elsevier, 2025.
Hannah Johnston, Ozlem Ergun, Juliet Schor, and Lidong Chen. Employment status and the on-demand
economy: a natural experiment on reclassification.Socio-Economic Review, 22(1):169–194, 2024.
Bruno Jullien and Alessandro Pavan. Information management and pricing in platform markets.The
Review of Economic Studies, 86(4):1666–1703, 2019.
Sara Constance Kingsley, Mary L Gray, and Siddharth Suri. Accounting for market frictions and power
asymmetries in online labor markets.Policy & Internet, 7(4):383–400, 2015.
Michael Kopel, Emmanuel Petrakis, and Anna Ressi. Endogenous scope of firm-union bargaining with
vertical pay comparisons.Journal of Economic Behavior & Organization, 167:39–52, 2019.
15

Alan B Krueger and Andreas I Mueller. A contribution to the empirics of reservation wages.American
Economic Journal: Economic Policy, 8(1):142–179, 2016.
Renato Paes Leme and Jon Schneider. Contextual search via intrinsic volumes. In2018 IEEE 59th
Annual Symposium on Foundations of Computer Science (FOCS), pages 268–282. IEEE, 2018.
Allen Liu, Renato Paes Leme, and Jon Schneider. Optimal contextual pricing and extensions. In
Proceedings of the 2021 ACM-SIAM Symposium on Discrete Algorithms (SODA), pages 1059–1078.
SIAM, 2021.
Thodoris Lykouris, Sloan Nietert, Princewill Okoroafor, Chara Podimata, and Julian Zimmert. Contex-
tual dynamic pricing with heterogeneous buyers. InThe Thirty-ninth Annual Conference on Neural
Information Processing Systems, 2025.
Michael David Maffie. Visible hands: How gig companies shape workers’ exposure to market risk.
Industrial Relations: A Journal of Economy and Society, 63(1):59–79, 2024.
Alan Manning. Monopsony in motion: Imperfect competition in labor markets. 2013.
Charles F Manski and John D Straub. Worker perceptions of job insecurity in the mid-1990s: Evidence
from the survey of economic expectations, 1999.
Behrens Martin, Hamann Kerstin, Hurd Richard, et al. Conceptualizing labour union revitalization.
InVarieties of unionism: Strategies for union revitalization in a globalizing economy, pages 11–29.
Oxford University, 2004.
Panayotis Mertikopoulos, Heinrich H Nax, and Bary SR Pradelski. Quick or cheap? Breaking points
in dynamic markets. InProceedings of the 21st ACM Conference on Economics and Computation,
pages 877–878, 2020.
Ruth Milkman and Kent Wong. Organizing immigrant workers: Case studies from Southern California.
Rekindling the movement: Labor’s quest for relevance in the twenty-first century, pages 99–128, 2001.
Dale T Mortensen and Christopher A Pissarides. New developments in models of search in the labor
market.Handbook of labor economics, 3:2567–2627, 1999.
Zane Muller. Algorithmic harms to workers in the platform economy: The case of Uber.Colum. JL &
Soc. Probs., 53:167, 2019.
Suresh Naidu and Eric A Posner. Labor monopsony and the limits of the law.Journal of Human
Resources, 57(S):S284–S323, 2022.
Mancur Olson. The logic of collective action [1965].Contemporary sociological theory, 124:62–63, 2012.
Edward Ongweso Jr. Organized DoorDash drivers’ #DeclineNow strategy is driv-
ing up their pay.Vice, 2021. URL https://www.vice.com/en/article/
organized-doordash-drivers-declinenow-strategy-is-driving-up-their-pay.
James A Parrott and Michael Reich. An earnings standard for New York City’s app-based drivers.
New York: The New School: Center for New York City Affairs, 2018.
Susumu Saito, Chun-Wei Chiang, Saiph Savage, Teppei Nakano, Tetsunori Kobayashi, and Jeffrey P
Bigham. Turkscanner: Predicting the hourly wage of microtasks. InThe World Wide Web Conference,
pages 3187–3193, 2019.
Niloufar Salehi, Lilly C Irani, Michael S Bernstein, Ali Alkhatib, Eva Ogbe, Kristy Milland, and
Clickhappier. We are dynamo: Overcoming stalling and friction in collective action for crowd workers.
InProceedings of the 33rd annual ACM conference on human factors in computing systems, pages
1621–1630, 2015.
Saiph Savage, Chun Wei Chiang, Susumu Saito, Carlos Toxtli, and Jeffrey Bigham. Becoming the
super turker: Increasing wages via a strategy from high earning workers. InProceedings of the web
conference 2020, pages 1241–1252, 2020.
16

Dorothee Sigg, Moritz Hardt, and Celestine Mendler-Dünner. Decline now: A combinatorial model
for algorithmic collective action. InProceedings of the 2025 CHI Conference on Human Factors in
Computing Systems, pages 1–17, 2025.
Yaron Singer and Manas Mittal. Pricing mechanisms for crowdsourcing markets. InProceedings of the
22nd international conference on World Wide Web, pages 1157–1166, 2013.
Adish Singla and Andreas Krause. Truthful incentives in crowdsourcing tasks using regret minimization
mechanisms. InProceedings of the 22nd international conference on World Wide Web, pages 1167–
1178, 2013.
Rushabh Solanki, Meghana Bhange, Ulrich Aïvodji, and Elliot Creager. Crowding out the noise:
Algorithmic collective action under differential privacy.arXiv preprint arXiv:2505.05707, 2025.
Alex Suzdaltsev. Distributionally robust pricing in independent private value auctions.Journal of
Economic Theory, 206:105555, 2022.
Sam Sweeney. Uber, Lyft drivers manipulate fares at Reagan National causing ar-
tificial price surges. WJLA ABC 7, 2019. URL https://wjla.com/news/local/
uber-and-lyft-drivers-fares-at-reagan-national.
Matthew Taylor, Greg Marsh, Diane Nicol, and Paul Broadbent.Good work: The Taylor review of
modern working practices, volume 116. Department for Business, Energy & Industrial Strategy
London, 2017.
Carlos Toxtli, Siddharth Suri, and Saiph Savage. Quantifying the invisible labor in crowd work.
Proceedings of the ACM on human-computer interaction, 5(CSCW2):1–26, 2021.
Matilde Tullii, Solenne Gaucher, Nadav Merlis, and Vianney Perchet. Improved algorithms for contextual
dynamic pricing.Advances in Neural Information Processing Systems, 37:126088–126117, 2024.
Charles Umney, Mark Stuart, Ioulia Bessa, Simon Joyce, Denis Neumann, and Vera Trappmann.
Platform labour unrest in a global perspective: How, where and why do platform workers protest?
Work, Employment and Society, 38(1):3–26, 2024.
Upwork. Review and pay for fixed-price contracts and mile-
stones. URL https://support.upwork.com/hc/en-us/articles/
17974824831507--Review-and-pay-for-fixed-price-contracts-and-milestones.
Tim SG van Eck, Pieter Kleer, and Johan SH van Leeuwaarden. Distributionally robust monopoly
pricing: Switching from low to high prices in volatile markets.arXiv preprint arXiv:2403.19486,
2024.
Nicholas Vincent, Hanlin Li, Nicole Tilly, Stevie Chancellor, and Brent Hecht. Data leverage: A
framework for empowering the public in its relationship with technology companies. InProceedings
of the 2021 ACM Conference on Fairness, Accountability, and Transparency, pages 215–227, 2021.
Shixin Wang. The power of simple menus in robust selling mechanisms.Management Science, 71(6):
5268–5287, 2025.
Alex J Wood, Mark Graham, Vili Lehdonvirta, and Isis Hjorth. Good gig, bad gig: autonomy and
algorithmic control in the global gig economy.Work, employment and society, 33(1):56–75, 2019.
Jamie Woodcock.The fight against platform capitalism: An inquiry into the global struggles of the gig
economy. University of Westminster Press, 2021.
Haiqing Zhu, Tijana Zrnic, and Celestine Mendler-Dünner. Look-ahead reasoning on learning platforms.
InAdvances in Neural Information Processing Systems, 2025.
17

A Appendix
We detail proofs of the main results presented in the main text.
A.1 Wait time of SWS
We start with basic properties of the wait time and success probability at iterationt: since workers are
drawn sequentially until the first success occurs,Nt ∼Geom(q t), with mean and variance
E[Nt] = 1 qt ,Var(N t) = 1−q t q2 t .(20)
As defined before, the total number of workers needed across all iterations is equal to the total wait
timeW AIT(pSWS) := PM t=1 Nt. Clearly,N t ⊥N t+1, so
E[W AIT(pSWS)] =
MX
t=1
1
qt
,Var(W AIT(p SWS)) =
MX
t=1
1−q t
q2 t .(21)
As part of our proofs, we also need a standard result on sub-exponential behavior of Geometric
variables:
Lemma A.1(Sub-exponential property of Geometric random variables).If∆∼Geom (q)on {1, 2, . . .},
thenE∆ = 1/q,Var(∆) = (1−q)/q 2. Moreover, there exists a universalC >0such that
∥∆−E∆∥ ψ1 ≤ C q ,(22)
i.e.,∆−E∆is sub-exponential with scaleO(1/q).
Proof. The mgf of∆is M∆(λ) = qeλ 1−(1−q)eλ for λ <−ln (1 −q ). For |λ| ≤c qwith a small enough
absolute c > 0, a Taylor expansion of logM ∆(λ) −λE ∆yields logEe λ(∆−E∆) ≤C 1λ2/q2. Since
this holds for |λ| ≤cq, we also get logEe λ(∆−E∆) ≤C 1cλ/q, which is the standard criterion for
sub-exponentiality with parameterO(1/q).
Proof of Theorem 3.3.By Lemma 3.2, we haveqt ≥q ∗ := 1 −e −θ for all t∈ [M ]. Since Nt ∼Geom (qt)
and theN t are independent acrosst,
E[W AIT(pSWS)] =
MX
t=1
E[Nt] =
MX
t=1
1
qt
≤ M q∗ .
We also note that there exists a constant0< q− <1(depending only onθ) such that
q− ≤q t for allt∈ {1, . . . , M}.(23)
as per Lemma 3.2, withq∗ as defined above. As such, we can also compute the variance of the wait
time under the pricing strategypSWS as
Var(W AIT(pSWS))≤
MX
t=1
1−q −
q2 − =O(M). (24)
For the concentration bound, apply Lemma A.1 withq = qt ≥q ∗ to find ψ1 control ∥Nt −EN t∥ψ1 ≤
C/q∗ for some constantC. Since all Nt are independent, we can apply Bernstein’s inequality for the
sum of independent sub-exponential variablesXt =N t −E[N t], which sum up toW AIT(pSWS).
We thus find that exists a constantc=c(θ)>0s.t.∀x >0,
P

W AIT(pSWS)−E[W AIT(pSWS)]≥x  ≤exp  −cmin{x 2/M, x}  ,(25)
18

or, equivalently,∃c∗ >0that depends only oncs.t.∀ϵ∈(0,1),
Pr


 W AIT(pSWS) E[W AIT(pSWS)] −1

 ≥ϵ  ≤2 exp  −c ∗ ϵ2M  .(26)
We note that the wait time concentration bound is distribution-agnostic and holds for anyDi under
the independence assumptions of the model.
Table 1: Left-tail properties ofDand implications for the total cost achieved bypSWS.
Left-tail class Total cost underpSWS
Gap(g >0) Θ(M)
D(x)≍x Θ(logM)
D(x)≍x α, α >1 Θ(M 1−1/α)
D(x)≳x β, β <1 O(1)
Atom at0 O(1)
A.2 Total cost of SWS
See Table 1 for different left-tail properties ofD.5.
Proof of Lemma 3.4.We show that the stochastic wage suppression strategy satisfies
M g∗ ≤COST(p SWS)≤M·max i∈[M] Qi(θ)≤M,(27)
and thus COST(p) = Θ(M )(with constants depending only ong∗ and θ). If Di(x) = 0for all x < gi,
then Qi(u) ≥g i for every u∈ (0, 1]. Thus for every iterationt, pt = maxi∈At Qi(θ/(M−t + 1)) ≥
maxi∈At gi ≥g ∗, so P t pt ≥M g∗. For the upper bound, use the monotonicity ofQi in its argument:
Qi(θ/(M−t+ 1))≤Q i(θ)≤1, hencep t ≤max i Qi(θ)≤1and the sum is at mostM.
We note that to achieveΘ(M ), only a fraction of categories need a gap: ifαM categories (for some
constantα∈(0,1]) satisfyg i ≥g 0 >0, thenCOST(p SWS)≥αg 0 Mand stillCOST(p SWS)≤M.
Proof of Lemma 3.5.Fix ε >0. Since inf{x : Di(x) > 0} = 0, we haveQi(u) → 0as u↓ 0for every i.
Hence, for eachi there exists δi > 0such that Qi(u) ≤ε for all u∈ (0, δi]. Let δ := mini∈[M] δi > 0.
LetJ:=⌈θ/δ⌉. For allj≥J, we haveθ/j≤δ, and therefore
Qmax(θ/j) = max i Qi(θ/j)≤ε.
Writing the total cost asPM j=1 Qmax(θ/j)(withj=M−t+ 1), we obtain
COST(pSWS)≤
J−1X
j=1
Qmax(θ/j) +
MX
j=J
ε≤C(ε) +εM,
where C(ε) := PJ−1 j=1 Qmax(θ/j)is finite and independent ofM. Dividing byM and taking M→ ∞
yieldslim sup M→∞ COST(pSWS)/M≤ε. Sinceεwas arbitrary,COST(p SWS) =o(M).
Observation A.2.Canonical examples of distributions with property 9:
• Beta(a, 1)on[0 , 1]with a > 1(exactly D(x) = xa) gives a total cost of COST(pSWS) =
Θ(M 1−1/a). Similarly, theGamma( k >1, λ)on[0 ,∞ )with k >1and theWeibull( k >1, λ)
distributions reduce to the same computations.
5In Table 1, the≍ notation means that iff (x) ≍g (x), then ∃c1, c2 > 0s.t. c1g(x) ≤f (x) ≤c 2g(x)for small x; the ≳
notation means that iff(x)≳g(x),then∃c >0s.t.f(x)≥cg(x)for smallx.
19

• Weibull-at-zero typedistribution (stretched–exponential left tails). Take a CDF of the form
D(x) = exp

−λ x−β (1 +o(1))  asx→0,forβ, λ >0. Then
Q(u) =
 λ
ln(1/u)
1/β
(1 +o(1)),(28)
giving COST(pSWS) = Θ  M (lnM) 1/β  . This issublinear but can get arbitrarily close to linear: for
any fixedϵ >0and largeM,M/(lnM) 1/β ≫M 1−ϵ.
•Lognormal left tail.Take theLogNormal(µ, σ 2)with a super-light tail. For smallu,
Q(u) = exp

µ+σΦ −1(u)  = exp  µ−σ p 2 ln(1/u) (1 +o(1))  .(29)
Withu=θ/|A t|,
Q(θ/|At|) = exp

µ−σ
p
2 ln|At|(1 +o(1))

,(30)
Taking the integral gives a total cost bound of
COST(pSWS) =
MX
j=1
Q(θ/j) = Θ

Mexp

−σ
√
2 lnM

.(31)
Proof of Lemma 3.6.Property 10 implies that there are constantsc, t0 > 0such that for all t > t0 and
all category indicesi, P[vi ≤ 1/t] ≥c/t . Thus, forx≤ 1/t0, Di(x) ≥cx , or equivalently,Qi(u) ≤u/c .
Thus, we can split the total cost in two sets: a set ofj≥ ⌊θt0/c⌋ for whichpt ≤ θ cj and a setj≤ ⌊θt0/c⌋
which is finite and constant (denoted byC) with respect toM. Then, the total cost can be bounded as
COST(pSWS) =
MX
t=1
pt ≤C+
MX
j=⌊θt 0/c⌋
θ
cj =O(log(M))(32)
Observation A.3.Canonical examples of distributions with property 10 (note that any log-concave
law with pdff(0)>0will satisfy this bound):
•Uniform[0,1].Q(u) =u, sop t =θ/(M−t+ 1)andCOST =θ PM j=1 1 j = Θ(logM).
• Exponential( λ)truncated to[0 , 1].Near0, D(x) ∼λx , hence property 10 holds withc = λ/2
for small enough x0, so COST(pSWS) = O(logM ). A direct calculation of the quantiles of
D(x) = 1 −e −λx gives Q(1/t) = −1/λln (1 − 1/t) = Θ(1/t)through a simple Taylor expansion,
thus summing toCOST(pSWS) = Θ(logM).
• Beta(1, b)with b <1: we can compute the quantiles asQ(1/t) = 1 − (1 − 1/t)1/b = Θ(1/t)by a
similar Taylor expansion, obtaining againCOST(pSWS) = Θ(logM).
We formulate a general criterion for the total price to stay constant with respect toM:
Proposition A.4.The total cost of the principal isO(1)with respect to M if there exist constants
c1, c2 >0such that for allM≥2,
c1
Z M
1
Qmax
 θ
x

dx≤
MX
j=1
Qmax
 θ
j

≤c 2

Qmax(θ) +
Z M
1
Qmax
 θ
x

dx
!
,
(33)
forQ max(u) = maxi Qi(u). Equivalently, with the change of variablesu=θ/x,
Z M
1
Qmax
 θ
x

dx=θ
Z θ
θ/M
Qmax(u)
u2 du.(34)
20

The total cost is finite if and only if
R θ
0+
Qmax(u)
u2 du <∞.
Proof. The proposition follows from the nondecreasing property ofQmax(u)and applying the integral
test for monotone sequences toQmax(θ/x)with the mentioned change of variables.
Proof of Lemma 3.7.If there existx0 ∈ (0, 1], β∈ (0, 1)and c >0such that for all i and x∈ [0, x0],
Di(x)≥c x β, we can compute the quantiles for all smallu,Qi(u)≤(u/c) 1/β. Thus,
pt ≤Q max(θ/j)≤(θ/c) 1/β j−1/β.(35)
Since1 /β >1, P j≥1 j−1/β <∞ , P t pt = O(1)w.r.t. M. Finally, if the distributionsDi have an atom
at0, it means that Di(0) ≥ρ i > 0, then forj≥θ/ρ i, Qi(θ/j) ≤ 0. Given nonnegative prices, only
finitely many terms are positive, soP t pt =O(1)w.r.t.M.
Observation A.5(Phase transition behavior for theBeta(a, 1)distribution family).The Beta distribu-
tion can be used to illustrate all regimes of growth for the total price of the principal under the stochastic
wage suppression pricing strategy discussed in the main text. IfD(x) = xa (i.e., X∼Beta (a, 1)), then
Q(u) =u 1/a, sop t = (θ/(M−t+ 1)) 1/a .Then
COST(pSWS) =
MX
j=1
 θ
j
1/a
=



Θ(M 1−1/a), a >1,
Θ(logM), a= 1,
Θ(1), a <1.
(36)
Proof. The quantiles of theBeta distribution can be computed in closed form asQ(u) = u1/a. Then,
the standard asymptotics ofPM j=1 j−α apply: it diverges likeM 1−α for α∈ (0, 1), like logM for α = 1,
and converges forα >1.
Observation A.6(On optimality under distributional knowledge.).Given full knowledge of{Di}i∈At,
the minimum price at iterationtnecessary to satisfy the iteration-level success floorq∗ is
p∗ t ∈arg min p∈[0,1]
n
p: 1−
Y
i∈At

1−D i(p)

≥q ∗
o
.(37)
The pricing strategy based on the1/|At| quantiles essentially assumes that the principal has partial
knowledge, through an oracle access to the{Qi(u) :i∈A t}atu= 1/|A t|.
A.3 Random collective action
Proof of Lemma 4.1.For clarity, we present the calculation for the uniform family; the same argument
extends to distributions satisfying left-tail regularityDi(x) ≥cx . We compute at iterationt and for an
active categoryi,
Dmix i (pt)≥(1−α)p t,(38)
hence the probability of success in iterationtcan be written as
qt = 1−
Y
i∈At

1−D mix i (pt)  ≥1−  1−(1−α)p t |At|
≥1−exp

−(1−α)θ

=:q ∗(α).
(39)
Thus, we obtain again that∆t ∼Geom(q t)withq t ≥q ∗(α), and thus
E[W AIT(pSWS α )]≤ M q∗(α) =O(M). (40)
The concentration proof aroundE[W AIT(pSWS α )]follows exactly like in the proof of Theorem 3.3:
for any x, Di(x) ≥ (1 −α )x because the uniform component contributes(1−α )x and the point mass
only increases the CDF. We plugx = pt and note that the success probabilities are still geometric due
to the independence of theNt random variables. The rest of the proof is identical to Theorem 3.3, as
the tail bound follows from applying Bernstein’s inequality for the sum of independent sub-exponential
variables, withq ∗ replaced byq ∗(α).
21

Proof of Lemma 4.2.Let p− := pi and let Di(p−)denote the left limit atp−. For the mixture CDF
Dmix i (x) = (1−α)D i(x) +α1{x≥p −}, the left-quantile functionQα i satisfies
Qα i (u) =



Qi

u
1−α

,0≤u <(1−α)D i(p−),
p−,(1−α)D i(p−)≤u≤α+ (1−α)D i(p−),
Qi

u−α
1−α

, α+ (1−α)D i(p−)< u≤1.
We partition the sum of the quantiles in three parts over the quantilesθ/|At|, a first threshold
u1 = ⌈θ/(1 −α )Di(p−)⌉ and a second threshold u2 = ⌊θ/(α + (1 −α )Di(p−))⌋ for the index set
1, 2, . . . , M. These thresholds are independent ofM, and thus we have a constant number of them in the
price floor regimep− and in the upper regime, whereas the lower quantile regime is just shifted by a factor
of1 /(1 −α )from the sum in the original distributionDi. We apply the same for taking the maximum
over the quantiles in the computation ofpSWS α evaluated at each quantile. As such, for the distribution
regimes we have analyzed in closed-form as a functionM, there exists constantsC1, C2 >0s.t.
1
1−α COST(pSWS)−C 1 ≤COST(p SWS α )≤ 1 1−α COST(pSWS) +C 2 (41)
This is because for any distributions with properties 9, 10, or 11, we can use a change of variable
u→u/ (1 −α ). In the case where all distributionsDi are the same with quantilesQi := Q, it is trivial
to notice thatCOST(pSWS α ) = PM j=1 Qα  θ(1−α) |At|  is approximately 1 1−α R M(1−α) 1−α Q(θ/x)dx. The same
argument follows for different distributionsDi that come from the same category (or families with the
same tail properties). For distributions that have a positive gap at0, collective action is not actually
needed, since the total cost paid by the principal isΘ(M)in the absence of any collective.
A.4 Targeted collective action
Proposition A.7.For everyu∈(0,1−ϵ), the quantiles of the adjusted distribution
D∗ i (x) := max{D i(x)−ϵ,0}forx <1, D ∗ i (1) = 1.(42)
satisfyQ ∗ i (u)≥Q i(u+ϵ)for anyi∈[M].
Proof. For an x that satisfies D∗ i (x) ≥u > 0, it means that max(Di(x) −ϵ, 0) = Di(x) −ϵ , so
D∗ i (x) = Di(x) −ϵ≥u, so Di(x) ≥ϵ + u. Coming back to the definition of the quantiles and taking
infimums overx, we obtain the desired inequality. The inequality does not hold foru = 0, but that
case is not needed in our set-up since our quantile prices are set for non-negative quantiles. Note that
for u≥ 1 −ϵ, both quantiles are1: Q∗ i (u) = Qi(u + ϵ) = Qi(1), since the distributions have support on
[0,1]. This holds for anyi∈[M].
Then, we can show thatTV(D∗ i , Di) ≤ϵ for all i. To see this, take an arbitrary categoryi∈ [M ]
and denote byµi the measure on[0, 1]associated to the CDF Di. We assume thatϵ < µ([0, 1])(so we
shave off less than the available total mass). By construction, we had removed the lowestϵ mass, but
this holds for any measure with massϵ, so let’s denote byl a measure on[0, 1]with l([0, 1]) = ϵ. Then,
we can define another measureνas
ν=µ−l+ϵδ 1,(43)
where δ1 is just the Dirac function at1(where we placed theϵ mass). Then, we associatedD∗ i with ν
and see thatTV(D∗ i , Di) =ϵ. By the total variation distance,
TV(D∗ i , Di) = sup
A⊆[0,1]
|µ(A)−ν(A)|(44)
For any Borel setA, µ(A) −ν (A) = l(A) −ϵδ 1∈A. If1 /∈A, this is equal tol(A) ≤l ([0, 1]) = ϵ since
A⊆ [0, 1]. If1 ∈A , then its absolute value is less thanmax(l(A) −ϵ, ϵ−l (A)) ≤ϵ as above. Finally,
takeA= [0,1)to see thatµ(A)−ν(A) =l([0,1)) =ϵ, henceTV(D ∗ i , Di) =ϵ.
22
