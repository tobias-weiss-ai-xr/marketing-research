---
title: Learning Fair Demand Models
url: https://arxiv.org/abs/2606.06830
category: ai-marketing
subcategory: measurement
date: 2026-06
venue: ''
authors:
- Adam N. Elmachtoub
- Hyemi Kim
- Jonathan Y. Tan
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.06830
pages: 63
chars: 150746
fetched_at: '2026-11-08T13:27:25+00:00'
kb_version: 1
---

# Learning Fair Demand Models

.
Learning Fair Demand Models
Adam N. Elmachtoub
Department of Industrial Engineering and Operations Research and Data Science Institute, Columbia University, New York,
NY 10027, adam@ieor.columbia.edu
Hyemi Kim
Department of Industrial Engineering and Operations Research, Columbia University, New York, NY 10027,
hk3181@columbia.edu
Jonathan Y. Tan
Department of Industrial Engineering and Operations Research, Columbia University, New York, NY 10027,
jyt2123@columbia.edu
Data-driven pricing is increasingly prevalent in sectors such as airlines, lending, insurance, and retail. By
learning demand models from customer features and setting prices accordingly, these systems may generate
discriminatory outcomes that raise fairness concerns. This leads to fundamental questions – how and where
should systems incorporate fairness considerations in the pricing pipeline, and how does it ultimately affect
societal outcomes? To answer these, we study a stylized model where a seller has a two-stage decision pipeline
comprising linear demand model estimation followed by price optimization. The seller considers fairness
notions in training loss, price, and demand, under both parity-wise and Rawlsian perspectives.
We show that equalizing training loss across consumer groups leads to multiple solutions, which in turn
can result in undesirable outcomes despite being a standard approach in fair machine learning. Focusing
instead on fairness applied directly to prices or demand, we compare two strategies that enforce fairness in
either the demand estimation stage or the price optimization stage. For parity-wise fairness, we characterize
when each strategy yields higher social welfare under small fairness levels. We show that when market sizes
and prices in the dataset are similar, imposing price fairness in the estimation stage is more beneficial to
consumers, whereas imposing demand fairness in the optimization stage yields better consumer outcomes.
For Rawlsian fairness, the two strategies coincide exactly. Lastly, we extend our model to alternate demand
functions and conduct a case study using real-world vaccine pricing data.
Key words: fairness; pricing; machine learning
1. Introduction
Data-driven pricing is now pervasive in practice across sectors including airlines, loans, insurance,
transportation services, and retail. These systems estimate heterogeneous demand and set prices
using customer features or segment-level attributes that incorporate behavioral, geographic, and
demographic information, which raise broader concerns about transparency, consumer agency, and
fairness.1 For instance, Delta Air Lines recently faced criticism from U.S. lawmakers over fears
1 https://www.nytimes.com/2025/11/28/opinion/dynamic-pricing-algorithms.html
1
arXiv:2606.06830v1  [cs.CY]  5 Jun 2026

2 Elmachtoub, Kim, and T an:Learning Fair Demand Models
that its planned use of artificial intelligence (AI) pricing tools could set individualized fares up to
each consumer’s “pain point”. 2. Likewise, field experiments on the Instacart platform show that
prices for products from the same store at the same time can vary across consumers, breaking the
commonly held notion that prices are uniform. 3 Beyond price disparities, fairness concerns also
arise through market access. Survey evidence on vaccines shows willingness-to-pay differs strongly
by income and socioeconomic status, implying that pricing policies can translate directly into
access gaps (Wong et al. 2024). Together, these examples highlight a fundamental tension between
profit-oriented algorithmic pricing and fairness in both price and demand.
In this paper, we investigate how to learn demand models to ensure fairness and what the
resulting consequences are on social outcomes. A substantial body of research has focused on
defining and enforcing fairness in machine learning (Mehrabi et al. 2021). However, a lot of existing
approaches treat fairness as a property of the predictive model instead of downstream decisions
such as pricing. Wang et al. (2024) point out that systems that leverage machine learning to guide
real-world decisions rely on proxy targets and produce disparate outcomes across groups. Similarly,
Scantamburlo et al. (2025) emphasize the need for a clear conceptual separation between prediction
and decision-making. This motivates us to examine how fairness can be incorporated across the
pricing pipeline.
In particular, we consider a pricing process that involves two stages. First, in the estimation stage,
a demand model is learned from observed data. Second, in the decision-making, an optimization
problem is solved to find the profit-maximizing price. Several complementary questions arise which
we address in this paper:What are the appropriate notions of fairness in this setting? Where
should fairness be imposed – the estimation stage or the decision-making stage? What are the
corresponding impacts on societal outcomes?
To begin, we consider prediction loss fairness (Khalili et al. 2023), which is a common fairness
notion in machine learning. We next study two fairness notions that directly align with downstream
objectives, originally proposed by Cohen et al. (2022):price fairness, which considers disparities
in prices across groups, anddemand fairness, which considers disparities in market share (or
access) across groups. We also consider two normative perspectives on fairness: parity-wise fairness
and Rawlsian fairness. Parity-wise fairness focuses on reducing disparities in price and demand
across groups. In many cases, fairness concerns arise at the group level, where pricing policies
should not produce systematic disparities across protected attributes. For instance, New York has
prohibited the so-called “pink tax” – i.e., charging different prices for similar products based on
2 https://www.reuters.com/business/delta-air-assures-us-lawmakers-it-will-not-personalize-fares-using-ai-2025-08-
01/
3 https://www.nytimes.com/2025/12/09/business/instacart-algorithmic-pricing.html

Elmachtoub, Kim, and T an:Learning Fair Demand Models3
gender – since 2020. 4 Rawlsian fairness, in contrast, emphasizes improving outcomes for the least
advantaged individual. In markets tied to essential goods and services, this concern is reflected
in policy safeguards such as price caps that protect economically vulnerable consumers, including
statutory caps on insulin out-of-pocket costs 5 and regulations that limit allowable rent increases 6.
To formalize our analysis, we employ a stylized model with two customer groups and linear
demand functions. Under this stylized model, we compare two frameworks. The first, which we term
Fair-Estimate-then-Optimize(FEO), incorporates fairness during the estimation of the demand
function and subsequently uses the estimated model for pricing. The second,Estimate-then-Fair-
Optimize(EFO), applies fairness constraints in the pricing phase only similar to Cohen et al. (2022).
The two frameworks offer distinct advantages. FEO leaves the optimization stage untouched, allow-
ing sales teams to focus solely on profit and commissions. In contrast, EFO produces an unbiased
demand model. To provide a deeper comparison, we analytically compare the EFO and FEO frame-
works under the proposed fairness criteria in terms of profit, consumer surplus, and social welfare.
Our contributions can be summarized as follows:
1. We demonstrate that under a stylized model, imposing parity-wise prediction loss fairness
yields two potential solutions that induce opposite effects on consumer surplus and social
welfare (Proposition 1). When one of these solutions is chosen uniformly at random, both
expected consumer surplus and social welfare decrease initially as the fairness level increases
(Corollary 1).
2. We analyze the impact of applying a little parity-wise fairness in the two frameworks. There
exists a unique threshold, determined by the market sizes and price distributions, that charac-
terizes whether EFO or FEO performs better in terms of consumer surplus and social welfare
(Proposition 2). We show that when the two groups have approximately the same market sizes
and the same average prices in the training data, FEO is more beneficial to customers under
parity-wise price fairness, whereas EFO is more beneficial under parity-wise demand fairness
(Corollary 2).
3. We compare the seller’s profit for FEO and EFO when imposing a little parity-wise fairness,
and provide sufficient conditions under which FEO acts as a regularizer, improves estimation
accuracy, and achieves higher profit than EFO (Proposition 3).
4. Under Rawlsian fairness, EFO and FEO lead to the same outcome. Under certain conditions,
fairness can increase profit, consumer surplus, and social welfare, challenging the conventional
view that fairness constraints necessarily come at the cost of profit (Proposition 4).
4 https://dos.ny.gov/news/former-governor-cuomo-reminds-new-yorkers-pink-tax-ban-goes-effect-today
5 S.954 – Affordable Insulin Now Act of 2023: https://www.congress.gov/bill/118th-congress/senate-bill/954
6 Rent Stabilization in NYC: https://www.nyc.gov/site/mayorspeu/programs/rent-stabilization.page

4 Elmachtoub, Kim, and T an:Learning Fair Demand Models
5. We extend the two frameworks to linear and logistic demand models with personalized fea-
tures. The corresponding problems are all convex optimization problems (Proposition 6 and
7).
6. We evaluate our frameworks on synthetic datasets and through a real-world case study of
vaccination against tick-borne encephalitis (TBE). We define two groups based on income level,
and estimate a logistic demand model using customer features such as socioeconomic status.
Under parity-wise demand fairness, EFO strictly dominates FEO by delivering higher profit,
consumer surplus, and social welfare. Other criteria offer no clear winner, instead requiring a
policy choice to navigate the trade-off between profit and consumer surplus.
1.1. Related Literature
Our work builds on and bridges three key areas of related literature: fairness in pricing, fairness in
machine learning, and fairness in decision-making.
Fairness in pricing.There has been growing interest in developing fair pricing policies. Cohen
et al. (2022) introduce formal fairness definitions in pricing and evaluate their implications in
both infinite supply and monopolistic market settings. In a related vein, Elmachtoub and Kim
(2026) examine fairness considerations under finite supply conditions, with a particular focus on
vehicle-sharing systems. Kallus and Zhou (2021) provide a comprehensive taxonomy of fairness
and welfare principles for personalized pricing across various domains, including lending, consumer
goods, and public services, highlighting the inherent trade-offs among revenue, accessibility, and
social equity. Xu et al. (2022) propose two regulatory policy instruments: theϵ-difference constraint
and theγ-ratio constraint, designed to balance consumer and producer surplus in the context of
personalized pricing. Several papers investigate dynamic pricing and learning algorithms under
fairness constraints (Cohen et al. 2025, Chen et al. 2025a,b). Gillis and Spiess (2019) highlight
that complex machine learning algorithms in pricing limit the applicability of existing law. Quan
et al. (2026) provide field-experimental evidence that greater consumer data availability intensifies
data-driven price discrimination, while regulatory intervention effectively alleviate its extent.
Fairness in Machine Learning.In the machine learning literature, fairness has been extensively
studied at the level of predictive models. Numerous formal definitions have been proposed, including
statistical parity or group fairness (Dwork et al. 2012), equalized loss (Khalili et al. 2023), equal
opportunity (Chouldechova 2017), equalized odds (Hardt et al. 2016), accuracy equality (Berk
et al. 2021), calibration (Kleinberg et al. 2016), and counterfactual fairness (Kusner et al. 2017).
These criteria are designed to mitigate disparate impact or disparate treatment by ensuring that
predictive models do not systematically favor or disadvantage specific subpopulations. Kallus et al.
(2022) provide bounds on disparity when protected class membership is not observed in the data.

Elmachtoub, Kim, and T an:Learning Fair Demand Models5
Fairness in Decision-Making.In addition to the pricing context, a growing body of work –
particularly in operations research and operations management – studies fairness at the level of
decision-making, emphasizing fairness criteria defined over the outcomes induced by decisions.
Chen and Hooker (2023) provide a comprehensive survey of how equity and fairness are formu-
lated within optimization models, covering a wide range of decision-level criteria that integrate
efficiency and fairness considerations. In this line of work, Bertsimas et al. (2011, 2012) study
resource allocation problems under a broad class of fairness objectives, including max–min and
proportional fairness, characterizing the efficiency–fairness trade-off by quantifying the “price of
fairness.” Beyond foundational formulations, related work also develops algorithms for decision-
level fairness in specific operational contexts. Several works provide fair algorithms for assortment
planning (Chen et al. 2022, Housni et al. 2025, Lu et al. 2023) and online matching (Ma et al. 2020,
2023). Freund et al. (2023) develop algorithms to access group fairness in dynamic refugee assign-
ment problems. In particular, Tang et al. (2023) develop fair policies for online resource allocation
from collected data, showing how fairness can be embedded into data-driven decision pipelines at
the allocation stage. Tsang and Shehadeh (2026) develop a unified framework for convex fairness
measures, providing an axiomatic characterization and a dual representation, and analyzing how
different fairness measures affect the optimal value and solution in fairness-promoting optimization
problems.
A growing literature studies settings in which predictions are used to inform decisions, and
examines where fairness constraints should be imposed within this prediction–decision pipeline.
Kleinberg et al. (2018) distinguish prediction from decision-making, showing that improvements in
predictive accuracy do not necessarily lead to better decisions or outcomes. McLaughlin et al. (2022)
show that excluding information about protected groups from the prediction may fail to reduce
disparities in machine-assisted human decisions. Corbett-Davies et al. (2017) formulate fairness
in pretrial decision-making as a constrained optimization problem that seeks to maximize utility
while satisfying fairness constraints. Liu et al. (2018) demonstrate that focusing solely on fairness
in prediction, particularly in the context of lending, can adversely affect customer utility. Chohlas-
Wood et al. (2024) propose a consequentialist framework that learns optimal decision policies by
maximizing stakeholder-defined utility, thereby balancing fairness and practical outcomes through
the use of contextual bandits and linear programming.
2. Modeling Framework
In Section 2.1, we introduce a stylized model to analyze how fairness constraints influence pricing
decisions and measures such as profit, consumer surplus, and social welfare. In Section 2.2, we
describe the two-stage pricing pipeline comprising of demand estimation and pricing optimization.

6 Elmachtoub, Kim, and T an:Learning Fair Demand Models
In Section 2.3, we present several fairness criteria – prediction loss, price, and demand – under two
normative perspectives: parity-wise and Rawlsian fairness. Finally in Section 2.4, we distinguish
between two implementation frameworks, Fair-Estimate-then-Optimize (FEO) and Estimate-then-
Fair-Optimize (EFO), which impose fairness at different stages of the pipeline.
2.1. Demand Model
We consider a stylized model in which a seller offers a single product, with a costc≥0, to two
distinct customer groups. The seller must determine a price for each group to maximize profit.
Customers are distinguished based on an observable binary attributeg∈ {0,1}, which allows the
seller to set group-specific pricesp g. For example,gmay correspond to attributes such as operating
system, income level, or geographic location. We assume a linear demand function,
ag +b gp+ϵ g,
wherea g is the market size of groupg,b g is the price sensitivity of groupg, andϵ g is some random
noise for groupg. We assumeE[ϵ g] = 0 forg∈ {0,1}. The variance ofϵ g, denoted byσ 2 g :=E[ϵ 2 g],
differs across groups. This reflects heterogeneous demand uncertainty across customer segments,
which commonly arises in practice from varying measurement noise or data quality across groups.
We assumeb 0 <0 andb 1 <0, implying that demand is downward sloping with respect to price.
To assess the implications of fairness criteria, we evaluate their impact using canonical economic
measures:profit,consumer surplus, andsocial welfare. Theprofitwith prices (p 0, p1) is
R(p0, p1) :=
X
g∈{0,1}
(pg −c) max (0, ag +b gpg).(1)
Theconsumer surplusfor groupgis thenS g(pg) = 1 2 (ag +b gpg) max  − ag bg −p g,0  , and thetotal
surplusisS(p 0, p1) =S 0(p0) +S 1(p1). Finally, we definesocial welfareas the sum of profit and
consumer surplus, i.e.,W(p 0, p1) :=R(p 0, p1) +S(p 0, p1), which shall quantifies the overall societal
impact of fairness constraints.
2.2. Pricing Pipeline
The pricing process typically involves two stages: learning (or estimating) a demand model, followed
by pricing decisions (or optimization). Machine learning models primarily address the first stage
while the outputs of these models are subsequently used in downstream decision-making processes,
such as profit maximization. Our work assumes that the downstream decision-maker seeks to
maximize profit using a pretrained demand model. We formulate these two stages below.

Elmachtoub, Kim, and T an:Learning Fair Demand Models7
Estimation Stage.Suppose the machine learning team is given a datasetD:={(g (i), p(i), d(i))}n i=1,
whereg (i) ∈ {0,1}represents the group label,p (i) ∈R ≥0 denotes the price, andd (i) ∈R ≥0 indicates
the demand of customeriat pricep (i). Here, we assume that the market sizes,a 0 anda 1, are
known (as in Qiang and Bayati (2016)). The machine learning model aims to estimate the demand
parameterb g from the data. In this work, we adopt the classical mean squared error as the loss
function. Thus, the optimal estimate ignoring fairness is obtained by

ˆbLS 0 , ˆbLS 1

:= arg min
ˆb0,ˆb1≤0
X
g∈{0,1}
ℓg(ˆbg), (2)
whereℓ g(ˆbg) := 1 ng P {i|g(i)=g}  ag + ˆbgp(i) −d (i) 2 andn g :=

 i|g(i) =g

 denotes the number of
samples in groupg.
Optimization Stage.Given an estimated demand model with estimated parameters ˆb0 and ˆb1,
the optimization team aims to maximize the expected profit based on the demand model. More
specifically, we denote by ˆRthe profit function computed by the least squares estimators, i.e.,
ˆR(p0, p1; ˆb0, ˆb1) := X
g∈{0,1}
(pg −c) max

0, ag + ˆbgpg

.
Therefore, the optimal price is set by

p∗ 0(ˆb0, ˆb1), p∗ 1(ˆb0, ˆb1)  := arg max p0,p1≥0 ˆR(p0, p1; ˆb0, ˆb1). (3)
Since the company cannot make any profit when setting a price less or equal thanc, we have the
following assumption:
Assumption 1.The least squares estimator satisfiesa g + ˆbLS g c >0forg∈ {0,1}.
For simplicity, we usep LS g andd LS g to denote the optimal prices and corresponding estimated
demand of least squares estimators, i.e.,p LS g :=p ∗ g

ˆbLS 0 , ˆbLS 1

andd LS g :=a g +ˆbLS g pLS g . Under Assump-
tion 1, they can be written asp LS g =− ag 2ˆbLSg + c 2 andd LS g = ag 2 + cˆbLS g 2 .
2.3. F airness Criteria
Fairness concerns in pricing systems can arise at multiple stages of the pricing pipeline, from
learning demand models to setting prices and determining market outcomes. As a result, what it
means for a pricing system to be “fair” depends on which aspect of the system is being evaluated.
In this section, we first clarify the objects of fairness considered in this paper. We consider three
objects of fairness: prediction loss, price, and demand. Each captures a distinct dimension at which
unfairness may arise.
First, we consider fairness in prediction loss (or estimation error), which captures how accurately
each group’s demand model is learned. Because demand learning underlies subsequent pricing

8 Elmachtoub, Kim, and T an:Learning Fair Demand Models
decisions, disparities in learning loss across groups indicate that the algorithm is systematically less
accurate for some groups than for others. These learning-stage disparities shape the information
on which pricing decisions are based and may therefore affect downstream pricing outcomes even
when pricing policies appear similar across groups. Moreover, considering fairness in prediction loss
across groups is a standard notion of fairness in machine learning.
Second, we consider price fairness. Because price reflects the pricing policy itself, differences
in prices across groups are directly interpretable as differences in how the algorithm treats those
groups. This interpretability makes price-based fairness particularly salient in practice and closely
aligned with regulatory approaches, such as bans on particular types of price discrimination.
Finally, we consider demand fairness. Because demand captures who participates in the market
and at what level, disparities in demand across groups indicate differences in access or exclusion
resulting from pricing decisions. These outcome-level disparities matter because they capture the
ultimate consequences of pricing algorithms. This is particularly important in setting such as
education and healthcare.
For each type of fairness, we consider two normative notions: parity-wise fairness and Rawlsian
fairness. Parity-wise fairness is a group fairness criterion that aims to equalize the corresponding
metric across groups. For example, parity-wise price fairness requires prices to be (near) equal
across groups. In contrast, Rawlsian fairness, also known as max-min fairness (Bertsimas et al.
2011), is an individual fairness notion that prioritizes protecting the worst-off individuals in terms
of price or demand. For instance, Rawlsian demand fairness focuses on improving the demand of
the group with the lowest demand.
Mathematically, learning demand models with parity-wise loss fairness can be formulated as the
following constrained optimization problem:
min
ˆb0,ˆb1≤0
ℓ0(ˆb0) +ℓ1(ˆb1)
s.t.

 ℓ0(ˆb0)−ℓ 1(ˆb1)

 ≤(1−α)

 ℓ0(ˆbLS 0 )−ℓ 1(ˆbLS 1 )

 .
The unit-less parameterα∈[0,1] controls the level of fairness. Whenα= 0, the fairness constraint
is inactive, corresponding to the status quo (2) in which the optimization is fairness-agnostic. In
contrast,α= 1 enforces perfect fairness by requiring equal loss (i.e., equal error) across the two
groups. Note that Rawlsian loss fairness is vacuous in our stylized model because losses across
groups are uncoupled. Specifically, each group’s loss depends only on its own group parameter,
and the unconstrained optimization already minimizes each group’s loss independently, leaving no
scope for further improvement under a Rawlsian objective.
Table 1 summarizes the corresponding constraints for price and demand fairness under parity-
wise and Rawlsian notions. These constraints can appear either in the estimation stage or the

Elmachtoub, Kim, and T an:Learning Fair Demand Models9
optimization stage, as we shall discuss in the next subsection. The parameters ¯p,p , ¯d, andd in
Table 1 can be chosen manually depending on the desired maximum or minimum price or demand
levels. For one specific fairness criterion, denoteF(α) as the set of feasible prices that satisfy
this fairness criterion. For instance, under parity-wise price fairness,F(α) ={(p 0, p1) :|p 0 −p 1| ≤
(1−α)|p LS 0 −p LS 1 |}.
Table 1 Price and demand fairness under Rawlsian and parity-wise perspectives
Parity-wise Rawlsian
Price |p 0 −p 1| ≤(1−α)|pLS 0 −p LS 1 |p g ≤(1−α) ¯p+αp
Demand |d0/a0 − d1/a1| ≤(1−α)|dLS 0 /a0 − dLS 1 /a1| dg/ag ≥(1−α)d +α ¯d
Note.d g represents the ex-ante demand for groupg, derived from the firm’s pricing decisionp g, i.e.,a g + ˆbgpg.
2.4. F air-Estimate-then-Optimize (FEO) vs. Estimate-then-F air-Optimize (EFO)
Equalized loss fairness is naturally imposed at the estimation stage – where model predictions
directly inform downstream decisions. In contrast, Rawlsian and parity-wise fairness can be applied
either during demand estimation or at the decision stage. We formalize this distinction through
two frameworks:Fair-Estimate-then-Optimize (FEO), which imposes fairness during estimation,
andEstimate-then-Fair-Optimize (EFO), which enforces fairness during decision making. Mathe-
matically, for a certain fairness criterion, FEO can be written as:
min
ˆb0,ˆb1≤0
X
g∈{0,1}
ℓg(ˆbg) s.t.

p∗ 0(ˆb0, ˆb1), p∗ 1(ˆb0, ˆb1)  ∈ F(α). (4)
We replace the unconstrained problem (2) with the fairness-constrained formulation (4), which
can be interpreted as a bilevel optimization problem. In this formulation, the upper-level prob-
lem selects the estimators ( ˆb0, ˆb1) by minimizing the estimation lossℓ g(ˆbg), while the lower-level
problem determines the induced optimal pricesp ∗ g as a function of ( ˆb0, ˆb1) by maximizing the
profit in (3). This internalizes fairness constraints within the estimation stage, ensuring that the
resulting decisions satisfy the desired fairness criteria even when the downstream decision stage
is purely profit-maximizing. We denote

ˆbFEO 0 , ˆbFEO 1

as the optimal solution of (4) andp FEO g :=
p∗ g(ˆbFEO 0 , ˆbFEO 1 ).
On the other hand, EFO can be written as optimization problem (5).
max
p0,p1≥0
ˆR(p0, p1; ˆbLS 0 , ˆbLS 1 ) s.t. (p 0, p1)∈ F(α). (5)
Here, we utilize the estimates ( ˆbLS 0 , ˆbLS 1 ) to solve a profit-maximization problem under fairness
constraints. This ensures the resulting prices are optimal given the estimated parameters while
satisfying the fairness criterion. We denote (p EFO 0 , pEFO 1 ) as the optimal solution of (5).

10 Elmachtoub, Kim, and T an:Learning Fair Demand Models
The detailed comparison between the two frameworks, FEO and EFO, will be discussed in Section
3. It is worth noting that, from a practical standpoint, there are clear distinctions between the
two frameworks in terms of flexibility and the scope of fairness enforcement. Under FEO, fairness
is incorporated at the estimation stage, leaving the downstream optimization stage untouched.
This is particularly convenient when the optimization engine may be a complex black box or
when sales agents are only driven by profits. Once the demand model is estimated under a given
fairness constraint, the decision maker can reuse it without having to further account for fairness.
In contrast, EFO enforces fairness only at the optimization (decision) stage, allowing the decision
maker greater flexibility to adjust fairness levels to specific contexts or objectives without retraining
the demand model. Moreover, the demand model is unbiased and may yield higher profit. Beyond
these differences, we will theoretically study the impact on how these strategies affect consumer
surplus and social welfare in Section 3.
3. Theoretical Analysis
In this section, we analytically compare two frameworks, Fair-Estimate-then-Optimize (FEO) and
Estimate-then-Fair-Optimize (EFO), through the lens of Rawlsian and parity-wise perspectives.
3.1. Parity-wise F airness
Prediction Loss Fairness.Within parity-wise fairness, we first consider loss fairness. Since the
mean squared error (MSE) is a quadratic function, enforcing parity-wise loss fairness with a
quadratic objective may result in two optimal solutions. Proposition 1 shows that the choice
between these two optimal solutions has a distinct impact on downstream outcomes such as total
surplus and social welfare, even with infinite data. Notably, one may be considered more effective
than the other. All proofs are provided in Appendix A.
Proposition 1.Without loss of generality, assumeσ 2 1 > σ2 0 andn g → ∞for allg∈ {0,1}. For
α≤α ⋆ := (b0) 2 E[p2|g=0] σ2 1 −σ2 0 , there are two optimal solutions:  b− 0 (α), b1  and  b+ 0 (α), b1  .
•Under

b− 0 (α), b1  , both consumer surplus and social welfare increase monotonically withα.
•Under

b+ 0 (α), b1  , both consumer surplus and social welfare decrease monotonically withα.
•Profit with

b+ 0 (α), b1  decreases more sharply than under  b− 0 (α), b1  for allαup to a certain
threshold¯α. In the remaining range, the profit under at least one of the cases,b + 0 orb − 0 ,
becomes zero.
Forα > α⋆, the unique solution is  b− 0 (α), b1  , and the changes in profit, consumer surplus, and
social welfare match those forα < α⋆.
Figure 1a illustrates the statements of Proposition 1. With respect to metrics such as profit, con-
sumer surplus, and social welfare, the solutionb −(α) is preferable tob +(α). In practice, however,

Elmachtoub, Kim, and T an:Learning Fair Demand Models11
when an optimization problem admits multiple optimal solutions, solvers – such as Gurobi (Gurobi
Optimization, LLC 2024) or Pyomo (Bynum et al. 2021) – return a single optimal solution, selected
according to internal heuristics and default solver behavior. In the absence of specific user config-
urations (e.g., enabling solution pools, setting deterministic options, or applying post-processing),
no attempt is made to identify or enumerate alternative optimal solutions.
Figure 1 Results under Parity-wise Loss Fairness
0.0 0.2 0.4 0.6 0.8 1.0
2.5
5.0
7.5
10.0
12.5
+
 +
 +
(a) FEO
0.0 0.2 0.4 0.6 0.8 1.0
2
4
6
8
10
E[ ]
 E[ ]
 E[ ]
 (b) EFO
Note.Figures 1a and 1b correspond to Proposition 1 and Corollary 1, respectively. The parameters area 0 = 3.8,
a1 = 4,b 0 =−3.2,b 1 =−4,σ 0 = 0.1,σ 1 = 0.5, andc= 0.1.
Reflecting this scenario, we now consider the case in which the solver selects among optimal
solutions uniformly at random. Corollary 1 demonstrates that, under these conditions, the expected
value of relevant metrics – consumer surplus and social welfare – decline up to a certain point.
Corollary 1.Consider the case whereb −(α)andb +(α)each are returned with probability 1/2.
The expected consumer surplus and social welfare decrease withαwhenα≤¯α.
Corollary 1 illustrates that ignoring how an estimator affects downstream metrics can lead to
undesirable outcomes. The second plot in Figure 1b demonstrates this result: up to a certain
threshold ¯α, the expected profit, consumer surplus, and social welfare all decrease asαincreases.
Price and Demand Fairness.Unlike loss fairness, fairness in prices and demand admits the two
frameworks: FEO and EFO. We focus on the non-trivial case wherep LS 0 ̸=p LS 1 . If the unconstrained
prices were already equal, adding price or demand fairness constraints would be unnecessary. We
restrict our attention to the setting in which only a small amount of fairness is imposed, meaning
the fairness levelαincreases from 0 to a small positive valueϵ. This focus is motivated by the fact
thatα= 0 corresponds to the prevailing practice in which firms typically do not incorporate fairness
considerations. In other words,α= 0 represents the status quo. Therefore, our main interest lies in
understanding how introducing a small degree of fairness – increasingαslightly from zero – affects

12 Elmachtoub, Kim, and T an:Learning Fair Demand Models
the resulting outcomes under this realistic baseline setting. Moreover, focusing on the neighborhood
ofα= 0 allows tractable analytical characterization with the status quo regime. Since closed-form
comparisons are generally difficult to obtain for arbitrary values ofα, this difficulty motivates our
local comparative analysis aroundα= 0. By Assumption 1, we can also assume that when there is
a small amount of fairness applied, the optimal prices of FEO and EFO are still abovec.
Proposition 2 shows that, under a little fairness, either FEO or EFO can yield higher consumer
surplus and social welfare, depending on the specific fairness criterion and a threshold determined
by the ratio of the estimated price distribution.
Proposition 2.Suppose Assumption 1 holds. Define
τp :=

a2 0 1 n1 P {i:g(i)=1} p(i)2
a2 1 1 n0 P {i:g(i)=0} p(i)2
!1/3
, τ a := a0
a1
, τ b :=
ˆbLS 0
ˆbLS 1 .
Then there existsξ >0such that the following statements hold for allα∈(0, ξ).
1.Consider parity-wise price fairness.
(a)If(τ p −τ b)(τa −τ b)>0, thenp FEO 0 < pEFO 0 andp FEO 1 < pEFO 1 . Consequently,S FEO >S EFO
andW FEO >W EFO.
(b)If(τ p −τ b)(τa −τ b)≤0, thenp FEO 0 > pEFO 0 andp FEO 1 > pEFO 1 . Consequently,S FEO <S EFO
andW FEO <W EFO.
2.Consider parity-wise demand fairness and assumec >0.
(a)If(τ p −τ b)(τa −τ b)≥0, thenp FEO 0 > pEFO 0 andp FEO 1 > pEFO 1 . Consequently,S FEO <S EFO
andW FEO <W EFO.
(b)If(τ p −τ b)(τa −τ b)<0, thenp FEO 0 < pEFO 0 andp FEO 1 < pEFO 1 . Consequently,S FEO >S EFO
andW FEO >W EFO.
Figure 2 and Figure 3 visualize the results for each case. To compare consumer surplus and social
welfare between FEO and EFO, we only have to compare the price decisions. Lower prices always
leave more surplus to consumers, and it always brings in more consumers. Since each consumer
contributes positively to social welfare, lower prices also lead to higher overall welfare.
τp can be interpreted as a balance index of the historical pricing data. It is determined by the
average squared prices of each group in the training dataset and the market sizesag. To illustrate its
dependence on these two components, we consider two simple cases. First, assuming equal market
sizes (a0 =a 1), the loss function simplifies to
ℓ0(ˆb0) +ℓ1(ˆb1)∝( ˆb0 − ˆbLS 0 )2 +τ 3 p (ˆb1 − ˆbLS 1 )2 +C,
whereCis a constant. This formulation reveals thatτ p dictates the relative weight of the two
groups: a smallerτ p assigns greater penalty weight to group 0’s fit. Consequently, under price

Elmachtoub, Kim, and T an:Learning Fair Demand Models13
Figure 2 Different cases in Proposition 2: parity-wise price fairness
0.0 0.2 0.4 0.6 0.8 1.0
8
9
10
11
pFEO 0
pEFO 0
pFEO 1
pEFO 1
Case (1a): Price
0.0 0.2 0.4 0.6 0.8 1.0
4
6
8
FEO
EFO
FEO
EFO
 Case (1a): Outcomes
0.0 0.2 0.4 0.6 0.8 1.0
8
9
10
11
pFEO 0
pEFO 0
pFEO 1
pEFO 1 Case (1b): Price
0.0 0.2 0.4 0.6 0.8 1.0
2
4
6
8
FEO
EFO
FEO
EFO
 Case (1b): Outcomes
Note.The parameters area 0 = 1,a 1 = 1,b 0 =−0.08,b 1 =−0.05 andc= 2. For Case (1a), prices of group 0 are
generated from Unif[4,8] and prices of group 0 are generated from Unif[4,10]; for Case (1b), prices of group 0 are
generated from Unif[2,3] and prices of group 0 are generated from Unif[11,12].
Figure 3 Different cases in Proposition 2: parity-wise demand fairness
0.0 0.2 0.4 0.6 0.8 1.0
7
8
9
10
11
pFEO 0
pEFO 0
pFEO 1
pEFO 1
Case (2a): Price
0.0 0.2 0.4 0.6 0.8 1.0
4
6
8
FEO
EFO
FEO
EFO
0.00 0.05 0.10 0.15 0.20
2.90
2.95
3.00
0.00 0.05 0.10 0.15 0.20
9.150
9.175
9.200
9.225
9.250
 Case (2a): Outcomes
0.0 0.2 0.4 0.6 0.8 1.0
8
9
10
11
pFEO 0
pEFO 0
pFEO 1
pEFO 1 Case (2b): Price
0.0 0.2 0.4 0.6 0.8 1.0
3
4
5
6
7
8
9
FEO
EFO
FEO
EFO
0.00 0.05 0.10 0.15 0.20
2.80
2.85
2.90
0.00 0.05 0.10 0.15 0.20
9.050
9.075
9.100
9.125
9.150
 Case (2b): Outcomes
Note.The parameters are the same as Figure 2. Training data used for Case (2a) and Case (2b) are the same as
Case (1a) and Case (1b), respectively.
fairness, a smallτ p restricts FEO from increasingp 0 as rapidly as EFO (corresponding to Case 1a).
Since the model preserves a price gap,p 1 is similarly lower under FEO, which drives up overall
consumer surplus under FEO.
Second, suppose the average squared prices in the training data are equal across both groups,
i.e., 1 n1 P {i:g(i)=1} p(i)2 = 1 n0 P {i:g(i)=0} p(i)2 . The index reduces toτ p =τ 2/3 a , implying thatτ p strictly
increases with the market size ratioτ a. Therefore, the terms (τp −τ b) and (τa −τ b) are more likely to
share the same sign, making the surplus-enhancing outcomes of Cases (1a) and (2a) in Proposition
2 much more likely to occur.
One practical scenario is that two different groups have similar market sizes, firms charge similar
prices to all customers, and data are collected randomly across groups. Corollary 2 shows that
if the market sizes and average squared prices in the training dataset are the same between two

14 Elmachtoub, Kim, and T an:Learning Fair Demand Models
groups, Cases (1a) and (2a) in Proposition 2 apply. In these cases, FEO yields higher consumer
surplus and social welfare than EFO under parity-wise price fairness, while the opposite holds
under parity-wise demand fairness.
Corollary 2.Suppose Assumption 1 holds. If 1 n0 P {i|g(i)=0} p(i)2 = 1 n1 P {i|g(i)=1} p(i)2 anda 0 =
a1, then for parity-wise price fairness,S FEO >S EFO andW FEO >W EFO. For parity-wise demand
fairness,S FEO <S EFO andW FEO <W EFO.
Notice that, under the same condition, parity-wise price fairness and parity-wise demand fairness
lead to opposite results. This is because price fairness constraints and demand fairness constraints
are pushing prices to different directions. For the group with higher price, adding price fairness
constraints decreases the price of this group. However, at the same time, it has larger demand, so
adding demand fairness constraints increases the price of this group to decrease the demand.
Comparing the profit of FEO and EFO also depends on different cases and fairness criteria. The
objective of EFO is to maximize the estimated profit under certain fairness constraints, but there
is a gap between the estimated profit and the real expected profit, since we can only estimate
unknown parameters (b0, b1) from historical data. Therefore, we are able to determine several cases
where the profit of FEO is larger than that of EFO in Proposition 3.
Proposition 3.Suppose Assumption 1 holds. Defineτ p,τ a andτ b the same as in Proposition 2.
There existsξ >0such that the following statements hold for allα∈(0, ξ).
1.Consider parity-wise price fairness.
(a)If(τ p −τ b)(τa −τ b)>0, thenR FEO >R EFO whena 0

1− b0 ˆbLS 0

+a 1

1− b1 ˆbLS 1

<0and
RFEO <R EFO whena 0

1− b0 ˆbLS 0

+a 1

1− b1 ˆbLS 1

>0.
(b)If(τ p −τ b)(τa −τ b)≤0, thenR FEO >R EFO whena 0

1− b0 ˆbLS 0

+a 1

1− b1 ˆbLS 1

>0and
RFEO <R EFO whena 0

1− b0 ˆbLS 0

+a 1

1− b1 ˆbLS 1

<0.
2.Consider parity-wise price fairness.
(a)If(τ p −τ b)(τa −τ b)≥0, thenR FEO >R EFO whena 0

1− b0 ˆbLS 0

+a 1

1− b1 ˆbLS 1

>0and
RFEO <R EFO whena 0

1− b0 ˆbLS 0

+a 1

1− b1 ˆbLS 1

<0.
(b)If(τ p −τ b)(τa −τ b)<0, thenR FEO >R EFO whena 0

1− b0 ˆbLS 0

+a 1

1− b1 ˆbLS 1

<0and
RFEO <R EFO whena 0

1− b0 ˆbLS 0

+a 1

1− b1 ˆbLS 1

>0.
Proposition 3 shows that fairness constraints in the estimation stage can sometimes act as a
regularizer. When the unknown parameters are accurately estimated, i.e., ˆbLS 0 =b 0 and ˆbLS 1 =b 1,
there is no gap between the estimated profit and the real expected profit, and it is easy to show
that EFO will give larger profit than FEO. The benefit of fairness constraints therefore arises in
the presence of estimation error, where they can improve parameter accuracy and, consequently,
increase profit.

Elmachtoub, Kim, and T an:Learning Fair Demand Models15
3.2. Rawlsian F airness
Rawlsian fairness seeks to protect the least advantaged individuals. More specifically, for price
fairness it minimizes the maximum price charged to customers, while in demand fairness, it maxi-
mizes the minimum demand faced by customers. For Rawlsian price fairness and Rawlsian demand
fairness, Proposition 4 shows that FEO and EFO lead to the same exact prices. Thus, one can
choose FEO or EFO based on discussion in Section 2.4.
Proposition 4.Suppose Assumption 1 holds. Then, under either Rawlsian price or demand
fairness with fairness levelα,
p∗ 0

ˆbFEO 0 , ˆbFEO 1

=p EFO 0 andp ∗ 1

ˆbFEO 0 , ˆbFEO 1

=p EFO 1 .
Ifp ∗ 0(ˆbLS 0 , ˆbLS 1 )< p∗ 1(b0, b1)< p∗ 1(ˆbLS 0 , ˆbLS 1 ), then both profit and total surplus can increase simultane-
ously up to a certain threshold, thereby improving overall social welfare.
The conditionp ∗ 0(ˆbLS 0 , ˆbLS 1 )< p∗ 1(b0, b1)< p∗ 1(ˆbLS 0 , ˆbLS 1 ) in Proposition 4 implies that group 1 is
overcharged relative to its true optimal price. This case corresponds to the scenario shown in
Figure 4. Under Rawlsian price fairness, increasingα– which lowers the price cap – brings the
price of group 1 closer to its true optimal price,p ∗ 1(b0, b1) (see Figure 4a) and can lead to higher
profit (see Figure 4b). Since prices decrease, consumer surplus increases, implying that both the
firm and consumers benefit. A similar mechanism operates under Rawlsian demand fairness, where
lowering the price for group 1 increases demand and yields higher profit and consumer surplus
(see Figure 4c and 4d). This challenges the conventional view that fairness constraints inherently
involve a trade-off with efficiency, and instead suggests that, under certain conditions, fairness can
improve outcomes for both the firm and consumers.
Figure 4 Rawlsian Price/Demand Fairness
0.0 0.2 0.4 0.6 0.8 1.0
1.00
1.25
1.50
1.75
2.00
p0 p1 p * 1
(a) Price
0.0 0.2 0.4 0.6 0.8 1.0
100
150
200
250
0.00 0.15
144.6
144.8 (b) Outcomes
0.0 0.2 0.4 0.6 0.8 1.0
0.47
0.48
0.49
0.50
0.51
d0 d1 (c) Demand
0.0 0.2 0.4 0.6 0.8 1.0
100
150
200
0.0 0.8
144.6
144.8 (d) Outcomes
Note.Figures 4a–4b (resp. 4c–4d) present outcomes under Rawlsian price (resp. demand) fairness. The parameters
area 0 = 1,a 1 = 1,b 0 =−0.5,b 1 =−0.25, ˆbLS 0 =−0.5124, ˆbLS 1 =−0.2320, andc= 0. Note thatp ∗ 1(b0, b1) = 2.

16 Elmachtoub, Kim, and T an:Learning Fair Demand Models
4. Extensions
The analysis in the previous section develops intuition in a stylized setting. We now turn to
more general environments. More specifically, we extend the stylized model to include scenarios
with unknown market sizes, i.e., unknown (a 0, a1) (Section 4.1), a linear model with features
(Section 4.2), and a logistic demand model with features (Section 4.3).
4.1. Unknown Market Sizes
In this section, we explore the case where both the market size and price elasticity are unknown
in the demand estimation stage. Similar to Assumption 1, we also assume that there exist prices
abovecfor the seller to get positive estimated demand with the least square estimator.
Assumption 2.The least square estimator satisfyˆa LS g + ˆbLS g c >0forg∈ {0,1}.
First, for parity-wise loss fairness, similar to the case with known market size, the optimization
problem admits multiple solutions that satisfy the fairness constraint and attain the same objective
value, resulting in model multiplicity. Importantly, different solutions can lead to either increases
or decreases in consumer surplus.
For parity-wise price and demand fairness, we generalize Proposition 2 to Proposition 5 which
shows that there is also a threshold that determines whether FEO or EFO provides higher consumer
surplus and social welfare under a certain fairness levelα.
Proposition 5.Suppose Assumption 2 holds. Define
Mg :=
"
1 1 ng P {i|g(i)=g} p(i)
1
ng
P
{i|g(i)=g} p(i) 1 ng P {i|g(i)=g} p(i)2
#
, v g :=

−
ˆbLS g
2
ˆaLS g
2

 ,
and
τp :=
 v⊤ 0 M −1 0 v0
v⊤ 1 M −1 1 v1
1/3
, τ a := ˆaLS 0
ˆaLS 1 , τ b :=
ˆbLS 0
ˆbLS 1 .
Then there existsξ >0such that the following statements hold for allα∈(0, ξ).
1.Consider parity-wise price fairness.
(a)If(τ p −τ b)(τa −τ b)>0, thenp FEO 0 < pEFO 0 andp FEO 1 < pEFO 1 . Consequently,S FEO >S EFO
andW FEO >W EFO.
(b)If(τ p −τ b)(τa −τ b)<0, thenp FEO 0 > pEFO 0 andp FEO 1 > pEFO 1 . Consequently,S FEO <S EFO
andW FEO <W EFO.
2.Consider parity-wise demand fairness and assumec >0.
(a)If(τ p −τ b)(τa −τ b)>0, thenp FEO 0 > pEFO 0 andp FEO 1 > pEFO 1 . Consequently,S FEO <S EFO
andW FEO <W EFO.
(b)If(τ p −τ b)(τa −τ b)<0, thenp FEO 0 < pEFO 0 andp FEO 1 < pEFO 1 . Consequently,S FEO >S EFO
andW FEO >W EFO.

Elmachtoub, Kim, and T an:Learning Fair Demand Models17
For Rawlsian fairness, we obtain the same result as in Proposition 4. The key reason is that, in
our demand model, each group is governed by an independent parameter pair (ag, bg). To illustrate,
consider Rawlsian price fairness. As the price cap decreases, only the group whose price exceeds
the cap needs to adjust its parameter to satisfy the constraint. Under FEO, this group optimally
sets its price exactly equal to the cap, rather than below it, since any further price reduction would
strictly increase loss. Similarly, under EFO, only the group with a price above the cap reduces its
price, again stopping exactly at the cap to avoid unnecessary profit loss. As a result, the optimal
solutions under FEO and EFO coincide under Rawlsian price fairness. An analogous argument
applies to Rawlsian demand fairness.
4.2. F eature-based Linear Demand Models
In this section, we extend the framework introduced so far to the setting with features, which can
be interpreted as the case of personalized pricing. We describe how to solve this problem, discuss
the properties that arise in this setting, and examine whether the results observed in the stylized
model continue to hold.
We consider a feature vectorx (i) = [1, x(i) 1 , x(i) 2 , . . . , x(i) m ]∈R m+1 that encodes the characteristics of
customeri∈[n] (or the product). The first component ofx (i) is fixed at 1 to capture the intercept.
This formulation enables personalized pricing and provides a more accurate characterization of the
demand function. Under the linear demand function,
dLS(x, p;a, b) =a⊤x+ (b⊤x)p.
Note that when there are only two feature vectors,x= [1,0] andx= [1,1], the model reduces to
the stylized setting in Section 3. Here, we interpret the feature as one that may embed information
correlated withg.
Similar to Section 3, the optimal estimates of the demand parameters (ˆaLS, ˆbLS) can be obtained
by minimizing the following loss function,
ℓLS(ˆa,ˆb) = X
g∈{0,1}
X
{i|g(i)=g}
1
ng

dLS  x(i), p(i);a, b  −d (i)2 .
Given a feature vectorxand the estimated parameters (ˆa, ˆb), the optimal pricep ∗ is defined as
p∗(x; ˆa,ˆb) := arg max
p≥0
(p−c) max

0, d(x, p; ˆa,ˆb)

.
Building on this setup, we introduce the definitions of parity-wise fairness and Rawlsian fairness
within this feature-based framework.

18 Elmachtoub, Kim, and T an:Learning Fair Demand Models
Parity-wise Fairness.We formulate theα-parity-wise price fairness criterion under the FEO
framework as follows.
min
ˆa,ˆb≤0
ℓLS(ˆa,ˆb)
s.t.

 1 n0 X {i|g(i)=0} p∗(x(i); ˆa,ˆb)− 1 n1 X {i|g(i)=1} p∗(x(i); ˆa,ˆb)

 ≤(1−α)∆ p, (6)
which enforces that the disparity in predicted prices between the two groups is bounded. Here,
∆p denotes the original average price gap between the two groups before applying the fairness
criterion. Furthermore, under parity-wise price fairness, we additionally impose an individual-level
price cap, such as
p∗(x(i); ˆa,ˆb)≤˜p∀i∈[n],
to prevent the decision maker from setting excessively high prices. This is because constraint (6)
only restricts the average price disparity across groups, and without an explicit cap, the optimiza-
tion problem could satisfy the parity constraint by assigning extreme prices to a single individual.
Similarly, the formulation of demand fairness shares the same objective structure as that in (6).
In demand fairness, we consider normalized ex-ante demand for each datai,
dEA

x(i); ˆa,ˆb  := 1 (ˆaLS)⊤x(i) dLS  x(i), p∗(x(i); ˆa,ˆb); ˆaLS, ˆbLS  .(7)
Here, we adopt the least-squares parameters (ˆaLS, ˆbLS) as the fixed baseline for demand evaluation.
Then, the ex-ante demand is evaluated by applying the optimal pricep ∗(x(i); ˆa,ˆb) to this baseline.
Then, parity-wise demand fairness replaces the constraint in (6) with

 1 n0 X {i|g(i)=0} dEA  x(i); ˆa,ˆb  − 1 n1 X {i|g(i)=1} dEA  x(i); ˆa,ˆb 

 ≤(1−α)∆ d,
where ∆d denotes the initial demand gap between two groups.
On the other hand, the EFO framework operates under the assumption that the estimated
demand function,d LS(x, p; ˆaLS, ˆbLS), is the ground truth. Given this assumption, it seeks to maxi-
mize total profit subject to a set of fairness constraints.
Theα-parity-wise price fairness problem can be formulated as
max
pi≥0
nX
i=1
(pi −c) max

0,(ˆaLS)⊤x(i) + ((ˆbLS)⊤x(i))pi

s.t.

 1 n0 X {i|g(i)=0} pi − 1 n1 X {i|g(i)=1} pi

 ≤(1−α)∆ p. (8)
The demand fairness can be defined analogously by modifying the fairness constraint accordingly.

Elmachtoub, Kim, and T an:Learning Fair Demand Models19
For parity-wise fairness, the optimization problem is non-convex. Therefore, in our numerical
analysis, we employ standard nonlinear optimization solvers to obtain approximate solutions. When
the demand function is specified asd=a ⊤x+b gp, both parity-wise price and demand fairness for
FEO can be efficiently addressed through a one-dimensional parameter search combined with a
convex optimization subproblem. The detailed algorithmic procedure is described in Appendix B.2.
Rawlsian Fairness.Under the FEO framework, theα-Rawlsian price fairness formulation adopts
the same objective as in (6) but replaces the constraint with
p∗(x(i); ˆa,ˆb)≤(1−α)¯p+αp ,∀i∈[n],(9)
where ¯p(resp.p ) represents the upper (resp. lower) bound of price determined by the practi-
tioner. Rawlsian demand fairness ensures that the ex-ante normalized demand exceeds a prescribed
minimum level. Mathematically,
dEA

x(i); ˆa,ˆb  ≥α ¯d+ (1−α)d ,∀i∈[n],
where ¯d(resp.d ) is the maximum (resp. minimum) normalized demand.
On the other hand, under the EFO framework, the objective remains the same as in (8), but the
constraint is modified to capture different notions of fairness. Rawlsian price fairness replaces the
constraint with
pi ≤(1−α)¯p+αp ,∀i∈[n].
Demand fairness is defined in a similar manner by replacing the constraint with a requirement that
the induced demand with respect top i exceeds a certain threshold.
One of the key differences between the EFO and FEO frameworks lies in the number of decision
variables involved in the optimization problem. In the FEO framework, there are 2m+ 2 decision
variables – twice the dimension of the feature space – whereas in the EFO framework, there are
ndecision variables corresponding to the number of data points. Consequently, in personalized
pricing settings with a large number of consumers (i.e., largen), EFO may face an increased
computational burden. In contrast, FEO may offer relative scalability advantages since the number
of featuresmis typically much smaller thann.
Regarding the nature of the optimization problems, the two frameworks exhibit different convex-
ity properties. In the EFO setting, Rawlsian fairness formulations are non-convex, as the objective
in (8) involves a multiplicative interaction between the pricepi and a piecewise-linear demand func-
tion, resulting in a non-concave profit function in the decision variables. In the FEO framework,
Proposition 6 illustrates that FEO frameworks can be reformulated as convex quadratic programs
(QPs). Although the formulation in (6), under both price and demand fairness, contains a non-
linear constraint, Proposition 6 demonstrates that the problem can nevertheless be rewritten as a
convex optimization problem.

20 Elmachtoub, Kim, and T an:Learning Fair Demand Models
Proposition 6.Within the FEO framework, Rawlsian price and demand fairness can be for-
mulated as convex optimization problems under linear demand.
Numerical AnalysisWe conduct experiments under the linear demand model. Specifically, we
consider four types of fairness, given by{Rawlsian,Parity-wise} × {price,demand}fairness. We
generate 1,000 synthetic samples following the procedure described in Appendix B.1. We varyα
from 0 to 1 on a grid with step size 0.2. To validate the performance of our frameworks, we split
the dataset into training and test data with an 80:20 ratio, and show the results on test data.
We consider a linear demand function with parameters (a 0, a1, b0, b1) = (30,10,−4,−4), i.e.,d=
(30 + 10x)−(4 + 4x)p. All parameters are assumed unknown, and the cost isc= 1. We impose an
individual-level price cap ˜p= 10 to ensure that fairness constraints are not satisfied by changing
the price of a single customer. We solve the constrained optimization problem using theSequential
Least Squares Quadratic Programming(SLSQP) algorithm inSciPy(Virtanen et al. 2020).
Figure 5 presents the price distributions under parity-wise price fairness. As the parity-wise
price fairness constraint are tightened in the estimation stage, the demand function being learned
becomes less personalized to reduce the difference between the two groups. Consequently, the
price distributions of group 0 and group 1 converge rapidly for FEO, and whenα= 1.0, all the
customers receive the same price. In contrast, imposing parity-wise price fairness constraints in
the optimization stage uses the same demand function as the model without fairness constraints,
preserving the effectiveness of the features. Table 2 shows that consumer surplus and social welfare
under FEO are higher than those under EFO at the same fairness level, consistent with Corollary 2.
Figure 5 Price distributions for FEO and EFO under parity-wise price fairness
0.0 0.2 0.4 0.6 0.8 1.0
3
4
5
6
7
p0 p1 Mean
(a) Price (FEO)
0.0 0.2 0.4 0.6 0.8 1.0
3
4
5
6
7
p0 p1 Mean (b) Price (EFO)
Figure 6 presents the demand distributions under parity-wise demand fairness. Here, ex-ante
demand is the normalized demand calculated by the estimated demand function using the least
square estimator, whereas ex-post demand is calculated by the true demand function. Notice that
only ex-ante demand is available to the decision maker. Therefore, the true fairness level is not the

Elmachtoub, Kim, and T an:Learning Fair Demand Models21
Table 2 Normalized performance measures for FEO and EFO under parity-wise price fairness (%)
FEO (α) EFO (α)
Measure 0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0
R(α)/R(0) 99.74 98.82 97.34 95.43 93.04 99.92 99.61 99.08 98.32 97.34
S(α)/S(0) 106.80 113.76 119.95 123.57 122.37 101.22 102.66 104.34 106.23 108.36
W(α)/W(0) 102.08 103.78 104.84 104.77 102.78 100.35 100.63 100.83 100.95 101.00
same as the fairness level set by the decision maker, and the gap between average ex-post demands
of group 0 and group 1 does not become 0 whenα= 1.0. In addition, FEO has a generalization
error on test data, resulting in additional gaps than EFO in both ex-ante and ex-post demands.
In Table 3, we observe that profit, surplus, and social welfare of FEO are all lower than those of
EFO. The opposite results between parity-wise price fairness and parity-wise demand fairness also
aligns with Proposition 2 of the non-contextual case.
Figure 6 Demand distributions for FEO and EFO under parity-wise demand fairness
0.0 0.2 0.4 0.6 0.8 1.0
0.36
0.38
0.40
0.42
0.44
0.46
d0 d1 Mean
(a) Ex Ante Demand (FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.36
0.38
0.40
0.42
0.44
0.46
d0 d1 Mean (b) Ex Ante Demand (EFO)
0.0 0.2 0.4 0.6 0.8 1.0
0.36
0.38
0.40
0.42
0.44
d0 d1 Mean
(c) Ex Post Demand (FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.36
0.38
0.40
0.42
0.44
d0 d1 Mean (d) Ex Post Demand (EFO)
Figure 7 illustrates the results under Rawlsian price fairness. Unlike Proposition 4, FEO and
EFO give different optimal prices under the sameα. This is because, for feature-based demand
models, imposing Rawlsian price fairness constraints in the estimation stage changes the demand
function itself, thereby shifting the entire demand distribution. In contrast, imposing Rawlsian
price fairness constraints in the optimization stage affects only the subset of the population facing

22 Elmachtoub, Kim, and T an:Learning Fair Demand Models
Table 3 Normalized performance measures for FEO and EFO under parity-wise demand fairness (%)
FEO (α) EFO (α)
Measure 0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0
R(α)/R(0) 99.96 99.89 99.79 99.65 99.48 99.99 99.99 99.97 99.95 99.93
S(α)/S(0) 98.72 97.45 96.19 94.96 93.74 99.99 99.99 99.97 99.95 99.93
W(α)/W(0) 99.55 99.08 98.60 98.09 97.57 99.99 99.98 99.97 99.96 99.94
high prices. Table 4 shows that the consumer surplus and social welfare of FEO are higher than
those of EFO asαincreases, and eventually become the same atα= 1.0.
Figure 7 Price distributions for FEO and EFO under Rawlsian price fairness
0.0 0.2 0.4 0.6 0.8 1.0
3
4
5
6
7
(a) Price under FEO
0.0 0.2 0.4 0.6 0.8 1.0
3
4
5
6
7
 (b) Price under EFO
Table 4 Normalized performance measures for FEO and EFO under Rawlsian price fairness (%)
FEO (α) EFO (α)
Measure 0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0
R(α)/R(0) 99.85 99.13 97.58 94.62 86.35 99.99 99.72 98.69 95.78 86.35
S(α)/S(0) 105.46 112.29 121.00 132.33 178.65 100.74 104.26 111.61 128.27 178.65
W(α)/W(0) 101.71 103.50 105.35 107.14 116.98 100.24 101.23 102.98 106.56 116.98
Figure 8 illustrates the results of Rawlsian demand fairness. In this case, FEO and EFO also lead
to different optimal price distributions. In Table 5, consumer surplus and social welfare of FEO are
higher than those of EFO. Notably, for both Rawlsian price fairness and Rawlsian demand fairness,
the gap between FEO and EFO in terms of profit, surplus and social welfare are relatively small.
4.3. F eature-based Logistic Demand Models
In this section, we examine an alternative specification of the demand function, namely the logistic
model. Following the approach in Section 4.2, we formulate the problem, analyze its key properties,
and investigate whether the results obtained in the stylized model continue to hold in this setting.

Elmachtoub, Kim, and T an:Learning Fair Demand Models23
Figure 8 Demand distributions for FEO and EFO under Rawlsian demand fairness
0.0 0.2 0.4 0.6 0.8 1.0
0.40
0.42
0.44
0.46
0.48
0.50
(a) Ex Ante Demand
(FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.40
0.42
0.44
0.46
0.48
0.50
(b) Ex Ante Demand
(EFO)
0.0 0.2 0.4 0.6 0.8 1.0
0.40
0.42
0.44
0.46
0.48
0.50
(c) Ex Post Demand
(FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.40
0.42
0.44
0.46
0.48
0.50
(d) Ex Post Demand
(EFO)
Table 5 Normalized performance measures for FEO and EFO under Rawlsian demand fairness (%)
FEO (α) EFO (α)
Measure 0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0
R(α)/R(0) 99.77 99.39 98.60 97.44 95.96 99.96 99.67 98.97 97.75 95.96
S(α)/S(0) 103.42 113.44 123.48 133.39 143.33 102.04 108.99 118.86 130.77 143.31
W(α)/W(0) 100.98 104.05 106.86 109.38 111.68 100.65 102.77 105.57 108.71 111.68
We consider the same feature vectorx (i) = [1, x(i) 1 , x(i) 2 , . . . , x(i) m ]∈R m+1 as in Section 4.2. The
logistic demand function is defined as
dCE(x, p;a, b) :=σ(a⊤x+bp),
whereσ(z) := 1 1+exp(−z) is the sigmoid function. CE denotes the cross-entropy loss, which is equiv-
alent (up to a constant factor) to the deviance of the logistic demand model, given by
ℓCE(ˆa,ˆb) =− X
g∈{0,1}
X
{i|g(i)=g}
1
ng
h
d(i) logσ  ˆa⊤x(i) + ˆbp(i) + (1−d (i)) log  1−σ(ˆa⊤x(i) + ˆbp(i)) i .
Given a feature vectorxand the estimated parameters (ˆa, ˆb), the optimal pricep ∗ is defined as
p∗(x; ˆa,ˆb) := arg max
p≥0
(p−c)d CE(x, p; ˆa,ˆb) = 1 +W0

eˆa⊤x(i)+ˆbc−1
−ˆb +c,
whereW 0(·) is the LambertWfunction.
Parity-wise Fairness.We first discuss how to formulate price and demand fairness under FEO.
Following the structure of (6), we formulate theα-parity-wise price fairness criterion as follows.
min
ˆa,ˆb≤0
ℓCE(ˆa,ˆb)
s.t.

 1 n0 X {i|g(i)=0} p∗(x(i); ˆa,ˆb)− 1 n1 X {i|g(i)=1} p∗(x(i); ˆa,ˆb)

 ≤(1−α)∆ p,
p∗(x(i); ˆa,ˆb)≤˜p,∀i∈[n],
(10)

24 Elmachtoub, Kim, and T an:Learning Fair Demand Models
where ∆ p denotes the baseline price gap observed when no fairness constraint is applied (i.e.,
α= 0), and ˜pis the price cap.
Similarly, the formulation of demand fairness follows the same structure as in (10), with the
fairness constraint replaced by

 1 n0 X {i|g(i)=0} dCE  x, p∗(x; ˆa,ˆb); ˆaCE, ˆbCE  − 1 n1 X {i|g(i)=1} dCE  x, p∗(x; ˆaCE, ˆbCE); ˆa,ˆb 

 ≤(1−α)∆ d.
Here, ∆ d denotes the initial demand gap between two groups, and (ˆaCE, ˆbCE) denotes the optimal
solution obtained in the absence of fairness criteria, i.e., (ˆa CE, ˆbCE) := arg minˆa,ˆb≤0 ℓCE(ˆa,ˆb). The
termd CE(x, p∗(x; ˆa,ˆb); ˆaCE, ˆbCE) represents the ex-ante demand. Analogous to the linear demand
case in (7), this is derived by treating the estimates (ˆaCE, ˆbCE) as the ground-truth demand param-
eters. The demand is evaluated based on these fixed parameters, while the price follows the optimal
pricing policyp ∗(x; ˆa,ˆb) dictated by the current decision parameters (ˆa,ˆb).
Under the EFO framework, we assume the estimated parameters (ˆa CE, ˆbCE) to be the ground
truth and maximize total profit based on this fixed model. Specifically, the parity-wise price fairness
problem is formulated as follows.
max
pi≥0
X
i∈[n]
(pi −c)d CE(x(i), pi; ˆaCE, ˆbCE)
s.t.

 1 n0 X {i|g(i)=0} pi − 1 n1 X {i|g(i)=1} pi

 ≤(1−α)∆ p,
pi ≤˜p,∀i∈[n].
(11)
Similarly, parity-wise demand fairness shares the same objective function, while the fairness con-
straint is defined by the difference in the mean predicted demand between the two groups.
Rawlsian Fairness.First, within the FEO framework, the objective remains the minimization of
the loss function, consistent with (10). Depending on the fairness criteria employed, the constraints
are adapted accordingly. For instance, under Rawlsian price fairness, the estimated parameters
(ˆa,ˆb) must ensure that the resulting optimal price for every individual does not exceed a specified
threshold, i.e.,
p∗(x(i); ˆa,ˆb)≤(1−α)¯p+αp ,∀i∈[n].
Under Rawlsian demand fairness, the framework ensures that each individual’s demand is main-
tained above a specific threshold, i.e.,
dCE

x(i), p∗(x(i); ˆa,ˆb); ˆaCE, ˆbCE

≥α ¯d+ (1−α)d ,∀i∈[n].
Within the EFO framework, the objective is to maximize the profit as defined in (11), withp i as
the decision variable. For instance, Rawlsian price fairness imposes the following constraint while
keeping the same objective:
pi ≤(1−α)¯p+αp ,∀i∈[n].

Elmachtoub, Kim, and T an:Learning Fair Demand Models25
Similarly, Rawlsian demand fairness sets a lower bound for the demand, which is determined by
the decision variablep i and estimates (ˆaCE, ˆbCE).
Under both price and demand fairness, the FEO problem is not a convex optimization problem.
However, similar to the linear demand case, Proposition 7 shows that, despite this non-linearity,
the problem can be reformulated as a convex optimization problem.
Proposition 7.Within the FEO framework, Rawlsian price and demand fairness can be for-
mulated as convex optimization problems under logistic demand.
5. Case Study: Experiments on Real-World Data
We conduct a case study based on survey data about vaccination against tick-borne encephalitis
(TBE) in Sweden from Slunge (2015), which includes an assessment of individuals’ willingness to
receive the TBE vaccine at randomly assigned prices. This dataset is particularly suitable for our
purposes because vaccination decisions are influenced not only by willingness-to-pay and socioe-
conomic status, but also by broader considerations of public health and equity. In such policy
contexts, pricing may be guided by profit motives as well as concerns about fairness.
5.1. Dataset and Setup
The dataset contains information on price (p), willingness to buy (d∈ {0,1}), and a range of
covariates, including age, gender, income, education level, area of residence, knowledge about TBE,
health status, trust in vaccine recommendations, and risk-related factors. Slunge (2015) indicates
that a substantial proportion of low-income individuals at risk of TBE are deterred from vaccination
due to the prevailing market price of the vaccine. Accordingly, we define the income indicatorg,
whereg= 1 (resp.g= 0) denotes low (resp. high) income, with individuals classified as low (resp.
high) income if their income is below (resp. above) 20,000 SEK, following Slunge (2015). The
dataset has also been used in recent fair pricing studies (Kallus and Zhou 2021, Xu et al. 2022).
After excluding entries with missing values and restricting to individuals who have not previously
been vaccinated, the dataset comprises 1,151 observations. As covariates, we includefemale,age,
income,university,urban,tbeincidence,summerhouserisk,outTBEarea,worktickrisk,knowledge,
tickbiteever,diseaseexperience,healthrisktickbite, andlowtrustvaccinerecin the feature vectorx,
following the set of variables identified as significant in Slunge (2015). All feature vectors are
normalized, and prices are scaled to lie within the interval [0,1]. We set the (normalized) unit
cost to 0.05 (corresponding to 50 SEK without normalization), which is set below the minimum
observed price (0.1), and impose a (normalized) price cap of 2.0 (corresponding to 2000 SEK),
which is set above the maximum observed price (1.0). We adopt an 80/20 split between the training
and test sets, and all reported results are based on the test set.

26 Elmachtoub, Kim, and T an:Learning Fair Demand Models
We use a logistic demand model,d=σ(a ⊤x+bp), for estimation in our case study. To evaluate
profit, consumer surplus, and social welfare, it is necessary to recover the true demand at each
price conditional on the observed features. For this purpose, we consider two scenarios. In the first,
the true demand is logistic, which we refer to as thewell-specifiedcase (Section 5.2). In the second,
the true demand follows a linear model,d= 1 + (b ⊤x)p, which we treat as themis-specifiedcase
(Appendix C.3). We also consider estimation using a linaer demand model, and results for the
well-specified and mis-specified cases are reported in Appendix C.1 and Appendix C.2, respectively.
To ensure that the data used for training are generated consistently with the assumed true
model, we regenerate demand outcomes based on the corresponding demand function. Lastly, we
set ¯p(resp.p ) in (9) as the highest (resp. lowest) optimal price obtained on the training set using
parameters estimated without fairness constraints. We set ¯das the lowest demand in the training
set when charging everybody pricep=c, andd as the lowest demand observed in the training set
without fairness constraints.
5.2. Results
Table 6 illustrates the outcomes under parity-wise loss fairness. Whenα≥0.6, the profit, consumer
surplus and social welfare are all lower than the no-fairness baseline, implying that parity-wise loss
fairness may harm the whole system.
Table 6 Normalized performance measures acrossαunder parity-wise loss fairness (%)
α
Measure 0.2 0.4 0.6 0.8 1.0
R(α)/R(0) 100.11 100.01 99.86 99.77 99.64
S(α)/S(0) 95.04 92.04 90.99 91.52 91.90
W(α)/W(0) 97.84 96.44 95.89 96.08 96.17
Figure 9 shows the price distributions under parity-wise price fairness. Atα= 1, the average
prices charged to the low-income and high-income groups become identical under EFO, whereas
this is not the case under FEO. This discrepancy arises because the model is evaluated on test data
with a finite sample size, where the empirical distribution of the test set inevitably deviates from
that of the training set. Table 7 shows that FEO yields higher consumer surplus and social welfare,
which implies that Corollary 2 not only holds for linear demand models but also for logistic demand
models. For instance, When we aim to reduce the mean price gap by 40% (α= 0.4), allowing an
additional 0.65% loss in profit leads FEO to achieve 11.39% higher consumer surplus, whereas EFO
does not make improvements in consumer surplus. This suggests that imposing parity-wise price
fairness in FEO is more beneficial to customers.

Elmachtoub, Kim, and T an:Learning Fair Demand Models27
Figure 9 Price distributions for FEO and EFO under parity-wise price fairness
0.0 0.2 0.4 0.6 0.8 1.0
0.7
0.8
0.9
1.0
1.1
1.2
1.3
1.4
p0 p1 Mean
(a) Price (FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.7
0.8
0.9
1.0
1.1
1.2
1.3
1.4
p0 p1 Mean (b) Price (EFO)
Table 7 Normalized performance measures for FEO and EFO under parity-wise price fairness (%)
FEO (α) EFO (α)
Measure 0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0
R(α)/R(0) 99.81 99.35 99.02 99.01 99.33 100.0 100.0 99.99 99.98 99.96
S(α)/S(0) 106.46 111.39 113.52 112.43 106.94 100.0 100.0 99.99 99.97 99.95
W(α)/W(0) 102.79 104.74 105.51 105.02 102.73 100.0 100.0 99.99 99.97 99.95
Figure 10 presents the results of parity-wise demand fairness. First, the ex-ante demand under
EFO achieves perfect demand fairness, whereas FEO does not. Similar to parity-wise price fairness,
this discrepancy arises from differences between the empirical distributions of the training and test
data. Due to estimation error, the estimated demand function differs from the true demand model.
Nevertheless, the fairness constraints still effectively shift the ex-post demand gap between the two
groups in a similar way to the ex-ante demand for both FEO and EFO.
Table 8 shows that, to achieve the same fairness levelα, EFO leads to much smaller changes in
profit, consumer surplus and social welfare than FEO. Moreover, whenα≤0.8, the profit, consumer
surplus and social welfare of EFO are all higher than FEO. This suggests that using EFO to achieve
parity-wise demand fairness is a safer option for both customers and the seller.
Table 8 Normalized performance measures for FEO and EFO under parity-wise demand fairness (%)
FEO (α) EFO (α)
Measure 0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0
R(α)/R(0) 97.50 89.15 91.61 95.62 93.10 100.0 99.99 99.92 99.79 99.60
S(α)/S(0) 78.76 57.37 65.71 97.26 111.32 100.0 99.90 99.81 99.77 99.76
W(α)/W(0) 89.11 74.93 80.01 96.35 101.26 100.0 99.95 99.87 99.78 99.67
Figure 11 illustrates the price distribution under Rawlsian price fairness. For both FEO and
EFO, the maximum price decreases as the fairness levelαincreases, showing that Rawlsian price

28 Elmachtoub, Kim, and T an:Learning Fair Demand Models
Figure 10 Demand distributions for FEO and EFO under parity-wise demand fairness
0.0 0.2 0.4 0.6 0.8 1.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
d0 d1 Mean
(a) Ex Ante Demand (FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
d0 d1 Mean (b) Ex Ante Demand (EFO)
0.0 0.2 0.4 0.6 0.8 1.0
0.1
0.2
0.3
0.4
0.5
0.6
d0 d1 Mean
(c) Ex Post Demand (FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.1
0.2
0.3
0.4
0.5
0.6
d0 d1 Mean (d) Ex Post Demand (EFO)
fairness effectively protects individuals facing excessively high prices. However, the two approaches
affect the distribution differently: FEO shifts the entire price distribution downward, whereas EFO
only adjusts prices that violate the fairness constraint. Table 9 shows that FEO leads to higher
consumer surplus and social welfare than EFO. Notably, at fairness levelα= 0.2, profit, consumer
surplus and social welfare for FEO are all higher than the baseline (i.e.,α= 0), showing that a
small level of Rawlsian price fairness for FEO can lead to a win-win outcome.
Figure 11 Price distributions for FEO and EFO under Rawlsian price fairness
0.0 0.2 0.4 0.6 0.8 1.0
0.6
0.8
1.0
1.2
1.4
(a) Price under FEO
0.0 0.2 0.4 0.6 0.8 1.0
0.6
0.8
1.0
1.2
1.4
 (b) Price under EFO
Lastly, Figure 12 presents the demand distributions under Rawlsian demand fairness. Similarly,
FEO changes the entire demand distribution, whereas EFO only modifies the portion of the pop-

Elmachtoub, Kim, and T an:Learning Fair Demand Models29
Table 9 Normalized performance measures for FEO and EFO under Rawlsian price fairness (%)
FEO (α) EFO (α)
Measure 0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0
R(α)/R(0) 100.01 99.27 97.02 93.39 87.48 100.0 100.01 100.00 99.48 94.76
S(α)/S(0) 101.88 113.06 126.25 139.70 155.82 100.0 100.03 100.76 107.16 132.54
W(α)/W(0) 100.84 105.44 110.11 114.12 118.07 100.0 100.02 100.34 102.92 111.67
ulation that violates the demand lower bound. Table 10 highlights a substantial trade-off: under
perfect demand fairness, while FEO delivers a large consumer surplus gain (113.22% increase), it
comes at a significant reduction in profit (a loss of more than 43.45%), which may limit its practical
feasibility. In contrast, EFO achieves a more modest surplus improvement (4% increase) with a
small impact on profit (0.91% loss), making it a more implementable policy choice.
Figure 12 Demand distributions for FEO and EFO under Rawlsian demand fairness
0.0 0.2 0.4 0.6 0.8 1.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
(a) Ex Ante Demand
(FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
(b) Ex Ante Demand
(EFO)
0.0 0.2 0.4 0.6 0.8 1.0
0.2
0.4
0.6
0.8
(c) Ex Post Demand
(FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.2
0.4
0.6
0.8
(d) Ex Post Demand
(EFO)
Table 10 Normalized performance measures for FEO and EFO under Rawlsian demand fairness (%)
FEO (α) EFO (α)
Measure 0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0
R(α)/R(0) 96.24 87.18 75.39 62.97 56.55 99.99 99.95 99.82 99.56 99.09
S(α)/S(0) 129.59 156.99 181.95 203.53 213.22 100.07 100.36 101.00 102.16 104.34
W(α)/W(0) 111.17 118.43 123.09 125.90 126.69 100.03 100.14 100.35 100.73 101.44
6. Conclusion
This paper studies fairness in a data-driven pricing pipeline consisting of a demand estimation
stage, where the firm learns a predictive demand model from data, and a price optimization stage,
where prices are determined to maximize expected profit based on the estimated demand model.
To this end, we develop a comprehensive framework to compare the outcomes that arise when
different fairness criteria are enforced at distinct stages of this pipeline.

30 Elmachtoub, Kim, and T an:Learning Fair Demand Models
Focusing on a stylized model with two groups and linear demand, we examine how pricing
decisions and societal outcomes are affected by using different fairness criteria and imposing fairness
in different stages. Our analysis yields three main insights. First, for loss fairness, which can only
be applied in the estimation stage, we show that it can yield multiple feasible solutions that lead to
substantially different prices and welfare outcomes. These observations highlight the importance of
considering downstream consequences during demand estimation. Second, for parity-wise fairness,
we find that when the two groups have similar market sizes and price distributions, where fairness
is imposed plays a crucial role. Price fairness at the estimation stage benefits consumers more, while
demand fairness at the optimization stage leads to better consumer outcomes. Third, for Rawlsian
fairness, imposing fairness in either the estimation or optimization stage leads to identical outcomes.
More strikingly, in certain settings, fairness can increase both profit and consumer surplus, yielding
a win–win outcome rather than the typical perceived trade-off.
To enhance the practical relevance of our findings, we generalize our framework to a more
realistic setting that incorporates customer features and considers a logistic demand model. We
then evaluate our results under this feature-based pricing using real-world vaccination data. Under
parity-wise demand fairness, we find that EFO strictly dominates FEO, yielding higher profit,
consumer surplus, and social welfare. Consequently, EFO emerges as the preferred approach. For
the other fairness criteria, however, no dominance emerges. Instead, we observe a clear trade-off
in which profit declines are accompanied by gains in consumer surplus. Our findings show how a
policymaker’s regulatory priority – whether to safeguard profits or maximize consumer surplus –
determines where fairness must be enforced within the algorithmic pricing pipeline.
There are many interesting extensions from our framework for future studies. While our theo-
retical results are derived under a stylized model, our experiments and case study indicate that
the qualitative insights extend to more general demand models. Extending theoretical results to
richer demand functions, multiple groups, and alternative market structures would further enhance
our understanding of fairness in data-driven pricing systems. In addition, our results highlight the
central role that the dataset plays in the performance of fairness-aware demand estimation. A
systematic study of the statistical properties of the framework, including sample complexity and
generalization error, would help clarify how limitations in data interact with fairness constraints to
shape downstream pricing decisions and social outcomes. More broadly, our findings raise impor-
tant questions about the governance of algorithmic pricing systems. Because fairness interventions
can have different effects depending on where they are applied, it is important to examine where
accountability and regulatory oversight should reside – whether in data collection, demand estima-
tion, price optimization, or post-processing. Understanding how auditing and regulation interact
with fairness-aware pricing systems remains an important direction for future research.

Elmachtoub, Kim, and T an:Learning Fair Demand Models31
References
Berk, Richard, Hoda Heidari, Shahin Jabbari, Michael Kearns, Aaron Roth. 2021. Fairness in criminal justice
risk assessments: The state of the art.Sociological Methods & Research50(1) 3–44.
Bertsimas, Dimitris, Vivek F Farias, Nikolaos Trichakis. 2011. The price of fairness.Operations research
59(1) 17–31.
Bertsimas, Dimitris, Vivek F Farias, Nikolaos Trichakis. 2012. On the efficiency-fairness trade-off.Manage-
ment Science58(12) 2234–2250.
Bynum, Michael L., Gabriel A. Hackebeil, William E. Hart, Carl D. Laird, Bethany L. Nicholson, John D.
Siirola, Jean-Paul Watson, David L. Woodruff. 2021.Pyomo–optimization modeling in python, vol. 67.
3rd ed. Springer Science & Business Media.
Chen, Qinyi, Negin Golrezaei, Fransisca Susan. 2022. Fair assortment planning.arXiv preprint
arXiv:2208.07341.
Chen, Violet Xinying, John N. Hooker. 2023. A guide to formulating fairness in an optimization model.
Annals of Operations Research326(1) 581–619.
Chen, Xi, Jiameng Lyu, Xuan Zhang, Yuan Zhou. 2025a. Fairness-aware online price discrimination with
nonparametric demand models.Operations Research.
Chen, Xi, David Simchi-Levi, Yining Wang. 2025b. Utility fairness in contextual dynamic pricing with
demand learning.Management Science.
Chohlas-Wood, Alex, Madison Coots, Henry Zhu, Emma Brunskill, Sharad Goel. 2024. Learning to be fair:
A consequentialist approach to equitable decision making.Management Science.
Chouldechova, Alexandra. 2017. Fair prediction with disparate impact: A study of bias in recidivism predic-
tion instruments.Big data5(2) 153–163.
Cohen, Maxime C, Adam N Elmachtoub, Xiao Lei. 2022. Price discrimination with fairness constraints.
Management Science68(12) 8536–8552.
Cohen, Maxime C, Sentao Miao, Yining Wang. 2025. Dynamic pricing with fairness constraints.Operations
Research.
Corbett-Davies, Sam, Emma Pierson, Avi Feller, Sharad Goel, Aziz Huq. 2017. Algorithmic decision making
and the cost of fairness.Proceedings of the 23rd acm sigkdd international conference on knowledge
discovery and data mining. 797–806.
Dwork, Cynthia, Moritz Hardt, Toniann Pitassi, Omer Reingold, Richard Zemel. 2012. Fairness through
awareness.Proceedings of the 3rd innovations in theoretical computer science conference. 214–226.
Elmachtoub, Adam N, Hyemi Kim. 2026. Fair fares for vehicle sharing systems.Operations Research.
Freund, Daniel, Thodoris Lykouris, Elisabeth Paulson, Bradley Sturt, Wentao Weng. 2023. Group fairness
in dynamic refugee assignment.arXiv preprint arXiv:2301.10642.

32 Elmachtoub, Kim, and T an:Learning Fair Demand Models
Gillis, Talia B, Jann L Spiess. 2019. Big data and discrimination.The University of Chicago Law Review
86(2) 459–488.
Gurobi Optimization, LLC. 2024. Gurobi Optimizer Reference Manual. URLhttps://www.gurobi.com.
Hardt, Moritz, Eric Price, Nati Srebro. 2016. Equality of opportunity in supervised learning.Advances in
neural information processing systems29.
Housni, Omar El, Qing Feng, Huseyin Topaloglu. 2025. Fairness-aware static and dynamic assortment
optimization: Optimal selection with balanced market share.arXiv preprint arXiv:2507.05606.
Kallus, Nathan, Xiaojie Mao, Angela Zhou. 2022. Assessing algorithmic fairness with unobserved protected
class using data combination.Management Science68(3) 1959–1981.
Kallus, Nathan, Angela Zhou. 2021. Fairness, welfare, and equity in personalized pricing.Proceedings of the
2021 ACM conference on fairness, accountability, and transparency. 296–314.
Khalili, Mohammad Mahdi, Xueru Zhang, Mahed Abroshan. 2023. Loss balancing for fair supervised learning.
International Conference on Machine Learning. PMLR, 16271–16290.
Kleinberg, Jon, Himabindu Lakkaraju, Jure Leskovec, Jens Ludwig, Sendhil Mullainathan. 2018. Human
decisions and machine predictions.The quarterly journal of economics133(1) 237–293.
Kleinberg, Jon, Sendhil Mullainathan, Manish Raghavan. 2016. Inherent trade-offs in the fair determination
of risk scores.arXiv preprint arXiv:1609.05807.
Kusner, Matt J, Joshua Loftus, Chris Russell, Ricardo Silva. 2017. Counterfactual fairness.Advances in
neural information processing systems30.
Liu, Lydia T, Sarah Dean, Esther Rolf, Max Simchowitz, Moritz Hardt. 2018. Delayed impact of fair machine
learning.International Conference on Machine Learning. PMLR, 3150–3158.
Lu, Wentao, Ozge Sahin, Ruxian Wang. 2023.A simple way towards fair assortment planning: Algorithms
and welfare implications. SSRN.
Ma, Will, Pan Xu, Yifan Xu. 2020. Group-level fairness maximization in online bipartite matching.arXiv
preprint arXiv:2011.13908.
Ma, Will, Pan Xu, Yifan Xu. 2023. Fairness maximization among offline agents in online-matching markets.
ACM Transactions on Economics and Computation10(4) 1–27.
McLaughlin, Bryce, Jann Spiess, Talia Gillis. 2022. On the fairness of machine-assisted human decisions.
Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency. 890–890.
Mehrabi, Ninareh, Fred Morstatter, Nripsuta Saxena, Kristina Lerman, Aram Galstyan. 2021. A survey on
bias and fairness in machine learning.ACM computing surveys (CSUR)54(6) 1–35.
Qiang, Sheng, Mohsen Bayati. 2016. Dynamic pricing with demand covariates.arXiv preprint
arXiv:1604.07463.

Elmachtoub, Kim, and T an:Learning Fair Demand Models33
Quan, Shanshan, Zhiqiang Zheng, Mingzheng Wang, Xiangpei Hu. 2026. Express: Data-driven price dis-
crimination, regulation, and platform compliance: Evidence from a field experiment and a natural
experiment.Production and Operations Management10591478251408177.
Scantamburlo, Teresa, Joachim Baumann, Christoph Heitz. 2025. On prediction-modelers and decision-
makers: why fairness requires more than a fair prediction model.Ai & Society40(2) 353–369.
Slunge, Daniel. 2015. The willingness to pay for vaccination against tick-borne encephalitis and implications
for public health policy: evidence from sweden.PloS one10(12) e0143875.
Tang, Bill, C ¸ a˘ gıl Ko¸ cyi˘ git, Eric Rice, Phebe Vayanos. 2023. Learning optimal and fair policies for online allo-
cation of scarce societal resources from data collected in deployment.arXiv preprint arXiv:2311.13765
.
Tsang, Man Yiu, Karmel S Shehadeh. 2026. A unified framework for analyzing and optimizing a class of
convex fairness measures.Operations Research74(2) 1087–1103.
Virtanen, Pauli, Ralf Gommers, Travis E. Oliphant, Matt Haberland, Tyler Reddy, David Cournapeau,
Evgeni Burovski, Pearu Peterson, Warren Weckesser, Jonathan Bright, St´ efan J. van der Walt, Matthew
Brett, Joshua Wilson, K. Jarrod Millman, Nikolay Mayorov, Andrew R. J. Nelson, Eric Jones, Robert
Kern, Eric Larson, C J Carey, ˙Ilhan Polat, Yu Feng, Eric W. Moore, Jake VanderPlas, Denis Laxalde,
Josef Perktold, Robert Cimrman, Ian Henriksen, E. A. Quintero, Charles R. Harris, Anne M. Archibald,
Antˆ onio H. Ribeiro, Fabian Pedregosa, Paul van Mulbregt, SciPy 1.0 Contributors. 2020. SciPy 1.0:
Fundamental Algorithms for Scientific Computing in Python.Nature Methods17261–272. doi:10.
1038/s41592-019-0686-2.
Wang, Angelina, Sayash Kapoor, Solon Barocas, Arvind Narayanan. 2024. Against predictive optimization:
On the legitimacy of decision-making algorithms that optimize predictive accuracy.ACM Journal on
Responsible Computing1(1) 1–45.
Wong, Li Ping, Hai Yen Lee, Haridah Alias, Gregory Zimet, Tongyu Liu, Yulan Lin, Zhijian Hu. 2024.
Cost-based covid-19 vaccination and willingness to pay: A post-pandemic review.Human Vaccines &
Immunotherapeutics20(1) 2313860.
Xu, Renzhe, Xingxuan Zhang, Peng Cui, Bo Li, Zheyan Shen, Jiazheng Xu. 2022. Regulatory instruments
for fair personalized pricing.Proceedings of the ACM Web Conference 2022. 4–15.

Elmachtoub, Kim, and T an:Learning Fair Demand Models1
Appendix
A. Proofs
Proof of Proposition 1.For simplicity, denoteℓ g
ˆbg(α)  byℓ g(α) underα-loss fairness. Without loss of
generality, supposeℓ 1(0)> ℓ0(0). Sinceℓ 0(0) andℓ 1(0) are at their minimum achievable values, they cannot
be further reduced. Therefore, to satisfy the fairness constraint withα, the only option is to increaseℓ 0(ˆb0)
while keepingℓ 1(ˆb1) unchanged. Thus,ℓ 1(α) =ℓ 1
ˆb1  , which impliesb 1(α) =b 1. Moreover,
ℓ0(α) =ℓ 1(α)−

1−α

ℓ1(0)−ℓ 0(0)

= (1−α)ℓ 0(0) +α ℓ1(0) = (1−α)σ 2 0 +ασ 2 1,(12)
where the last equality follows from the fact thatℓ g =σ 2 g whenn g → ∞for anyg∈ {0,1}.
Sincen g → ∞, we can rewrite the loss function as follows,
ℓg(ˆb) :=E

ag + ˆbgp−d
2 
=E

ˆbg −b g

p−ϵ g
2 
=

ˆbg −b g
2
E

p2|g  +σ 2 g.(13)
Then, by (12) and (13),
(b0 (α)−b 0)2 E  p2|g= 0  +σ 2 0 = (1−α)ℓ 0 +αℓ 2 1 = (1−α)σ 2 0 +ασ 2 1.
The solution isb 0(α) =b 0 ±
q
σ2 1 −σ2 0
E[p2|g=0] α. Letb + 0 (resp.b − 0 ) denoteb 0 + q σ2 1 −σ2 0 E[p2|g=0] α(resp.b 0 − q σ2 1 −σ2 0 E[p2|g=0] α).
Note that whenα > α⋆ := (b0)2 E[p2|g=0] σ2 1 −σ2 0 ,b + 0 (α)>0, which is infeasible under the constraintb g ≤0. Therefore,
ifα≤α ⋆, there are two optimal solutions, otherwise, only  b− 0 (α), b1  is the optimal solution.
Given the optimal solution

b± 0 (α), b1  , the optimal price of (1) is
p+ 0 (α) =− a0 2b+ 0 (α) + c 2 , p − 0 (α) =
(
− a0
2b− 0 (α) + c 2 ,ifα≤α −,
c,otherwise,
p1(α) =− a1
2b1
+ c 2 ,
whereα − :=  1 + a0 b0c 2 α⋆ is the point at whichp − 0 (α) =c.
Differentiating the prices with respect toα, forα≤α −,
dp± 0 (α)
dα = a0 2  b± 0 (α) 2 db± 0 (α) dα =± a0 4  b± 0 (α) 2
s
σ2 1 −σ 2 0
E[p2 |g= 0] · 1√α .
Otherwise,
dp+ 0 (α)
dα remains as above, while
dp− 0 (α)
dα = 0. Finally, dp1(α) dα = 0, as it does not depend onα.
Denote consumer surplus (respectively, profit and social welfare) under (p± 0 (α), p1(α)) asS ± (respectively,
R± andW ±). Then, the derivative of consumer surplus with respect toαis as follows.
dS ±
dα =−max

0, a0 +b 0p± 0 (α)  dp± 0 (α) dα . (14)
Note that dp1(α) dα = 0, so this term does not appear in dS± dα . Substituting dp± 0 (α) dα into (14), we obtain the
following.
dS −
dα >0 for 0≤α≤min

α−, α⋆	 and dS −
dα = 0 for min

α−, α⋆	 < α≤1.
dS +
dα <0 for 0≤α≤min

α+, α⋆	 and dS +
dα = 0 for min

α+, α⋆	 < α≤min(1, α⋆),

2 Elmachtoub, Kim, and T an:Learning Fair Demand Models
whereα + :=  a0+b0c 2a0+b0c 2 α⋆2 is the point at whicha 0 +b 0p+ 0 (α) = 0. dS+ dα is not defined forα > α ⋆, since
b+ 0 (α) does not exist.
The derivative of profit with respect toαis,
dR±
dα =

a0 + 2b0p± 0 (α)−b 0c  dp± 0 (α) dα I  p± 0 (α)≤ −a0 b0  .
Note that the optimal price with respect tob 0(0) is max

− a0 2b0 + c 2 , c  , which maximizes profit. Therefore,
for anyb ± 0 (α) withα >0, the corresponding profit is strictly lower. If we compare the ratio of the changes
in profit for 0≤α <min{α +, α−, α⋆}, we obtain
dR+(α)
dα
dR−(α)
dα
=
− a0 2b0 + c 2 −p + 0 (α)
− a0 2b0 + c 2 −p − 0 (α)
dp+ 0 (α)
dα
dp− 0 (α)
dα
=
 b− 0 (α)
b+ 0 (α)
3
>1.
Therefore, dR+(α) dα < dR−(α) dα .
Lastly, for social welfare, it is clear thatW + is decreasing up to min{α −, α⋆}, since both profit and
consumer surplus are decreasing withα(note that social welfare is the sum of these two components). For
min{α+, α⋆}< α < α⋆, it is 0. In the case ofW −, whereα <min{α −, α⋆},
dW −
dα =−b 0

−p− 0 (α) +c  dp− 0 (α) dα ≥0.
Otherwise, dW − dα = 0. □
Proof of Corollary 1.According to the proof of Proposition 1, forα <min{α +, α−, α⋆}, we know that
dS−
dα >0 and dS+ dα <0. Then,
E
 dS(α)
dα

= 1 2 dS −(α) dα + 1 2 dS +(α) dα = 1 2 dS −(α) dα  1 + dS+(α) dα dS−(α)
dα
!
= 1 2 dS −(α) dα| {z }
>0

1−  a0 +b 0p+ 0 (α) a0 +b 0p− 0 (α)  b− 0 (α) b+ 0 (α) 2 | {z }
(∗)

 .
Therefore,E
h
dS(α)
dα
i
<0, if (∗) is less than 0.
1−
 a0 +b 0p+ 0 (α)
a0 +b 0p− 0 (α)
 b− 0 (α)
b+ 0 (α)
2
<0⇔

a0 +b 0p−(α)  (b+ 0 (α))2 <  a0 +b 0p+(α)  (b− 0 (α))2
⇔a 0

b+ 0 (α)2 −b − 0 (α)2 <−b 0 c 2  b+ 0 (α)2 −b − 0 (α)2 + b0a0 2 b+ 0 (α) 3 −b − 0 (α) 3 b+ 0 (α)b− 0 (α)
⇔

a0 +b 0
c
2

b+ 0 (α)2 −b − 0 (α)2 < b0a0 2 b+ 0 (α) 3 −b − 0 (α) 3 b+ 0 (α)b− 0 (α)
⇔

a0 +b 0
c
2

b+ 0 (α) +b− 0 (α)  < b0a0 2 b+ 0 (α) 2 +b + 0 (α)b− 0 (α) +b− 0 (α) 2 b+ 0 (α)b− 0 (α)
⇔

a0 +b 0
c
2

2b0 < b0a0
2
3b2 0 −Kα
b2 0 −Kα
⇔ 4a0 + 2b0c a0 > 3b2 0 −Kα b2 0 −Kα
⇔ a0b2 0 + 2b3 0c (3a0 + 2b0c)K > α
⇔ a0 + 2b0c 3a0 + 2b0c α⋆ =: ¯α > α.

Elmachtoub, Kim, and T an:Learning Fair Demand Models3
Here,K:=
σ2 1 −σ2 0
E[p2|g=0] , which means thatb ± 0 (α) =b 0 ± √ Kαandα ⋆ =b 2 0/K. Given that dS+ dα <0, dS− dα >0,
andE
 dS
dα

<0, we obtain the inequality− dS+ dα > dS− dα .
In Proposition 1,R + decreases sharply. Therefore, combining the facts that− dS+ dα > dS− dα >0 and dR+ dα <
dR−
dα <0, we conclude that− dW + dα > dW − dα >0, which implies thatE  dW dα  <0.□
Proof of Proposition 2.Without loss of generality, we can assumep LS 0 < pLS 1 because group 0 and group
1 are symmetric. Then we haveτ a < τb. Therefore, we only have to compareτ p andτ b.
We first prove the results of each case for parity-wise price fairness. In order to compare FEO and EFO,
we first calculate the first order derivatives of the optimal prices with respect toα.
Under parity-wise price fairness, FEO is written as (15):
min
ˆb0,ˆb1
1
n0
X
i:g(i)=0

a0 + ˆb0p(i) −d (i)
2
+ 1 n1 X i:g(i)=1  a1 + ˆb1p(i) −d (i) 2
s.t.

p∗ 1  ˆb0, ˆb1  −p ∗ 0  ˆb0, ˆb1 

 ≤(1−α)

p∗ 1  ˆbLS 0 , ˆbLS 1  −p ∗ 0  ˆbLS 0 , ˆbLS 1 

 . (15)
The objective function can be written as (16)
1
n0
X
i:g(i)=0

a0 + ˆb0p(i) −d (i)
2
+ 1 n1 X i:g(i)=1  a1 + ˆb1p(i) −d (i) 2
=A

 1
p∗ 0

ˆb0, ˆb1

− c 2
− 1
p∗ 0

ˆbLS 0 , ˆbLS 1

− c 2


2
+B

 1
p∗ 1

ˆb0, ˆb1

− c 2
− 1
p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2


2
+C,
(16)
whereA=a 2 0

1
n0
P
i:g(i)=0 p(i)2

,B=a 2 1

1
n1
P
i:g(i)=1 p(i)2

,C= 1 n0 P i:g(i)=0  a0 + ˆbLS 0 p(i) −d (i) 2 +
1
n1
P
i:g(i)=1

a1 + ˆbLS 1 p(i) −d (i)
2
are constants. So the problem (15) is equivalent to
min
ˆb0,ˆb1
A

 1
p∗ 0

ˆb0, ˆb1

− c 2
− 1
p∗ 0

ˆbLS 0 , ˆbLS 1

− c 2


2
+B

 1
p∗ 1

ˆb0, ˆb1

− c 2
− 1
p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2


2
s.t.

p∗ 1  ˆb0, ˆb1  −p ∗ 0  ˆb0, ˆb1 

 ≤(1−α)

p∗ 1  ˆbLS 0 , ˆbLS 1  −p ∗ 0  ˆbLS 0 , ˆbLS 1 

 .
(17)
We can change the decision variables in (17) top 0, p1 instead of ˆb0, ˆb1 to get
min
p0,p1
A

 1
p0 − c 2 − 1 p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2


2
+B

 1
p1 − c 2 − 1 p∗ 1  ˆbLS 0 , ˆbLS 1  − c 2


2
s.t.|p 1 −p 0| ≤(1−α)

p∗ 1  ˆbLS 0 , ˆbLS 1  −p ∗ 0  ˆbLS 0 , ˆbLS 1 

 .
(18)
Denotep F EO 0 , pF EO 1 as the optimal solution to (18). First, we show that
pF EO 1 −p F EO 0 = (1−α)  p∗ 1  ˆbLS 0 , ˆbLS 1  −p ∗ 0  ˆbLS 0 , ˆbLS 1  .(19)
Supposep F EO 1 −p F EO 0 <(1−α)  p∗ 1  ˆbLS 0 , ˆbLS 1  −p ∗ 0  ˆbLS 0 , ˆbLS 1  , then eitherp F EO 1 < p∗ 1  ˆbLS 0 , ˆbLS 1  orp F EO 0 >
p∗ 0

ˆbLS 0 , ˆbLS 1

. Without loss of generality, supposep F EO 1 < p∗ 1

ˆbLS 0 , ˆbLS 1

. Then∃ξ 1 >0, such thatp F EO 1 +
ξ1 ≤p ∗ 1

ˆbLS 0 , ˆbLS 1

andp F EO 1 +ξ 1 −p F EO 0 ≤(1−α)  p∗ 1  ˆbLS 0 , ˆbLS 1  −p ∗ 0  ˆbLS 0 , ˆbLS 1  . This implies that
(pF EO 0 , pF EO 1 +ξ 1) is a feasible solution to (18).
A

 1
pF EO 0 − c 2 − 1 p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2


2
+B

 1
pF EO 1 − c 2 − 1 p∗ 1  ˆbLS 0 , ˆbLS 1  − c 2


2

4 Elmachtoub, Kim, and T an:Learning Fair Demand Models
> A

 1
pF EO 0 − c 2 − 1 p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2


2
+B

 1
pF EO 1 +ξ 1 − c 2 − 1 p∗ 1  ˆbLS 0 , ˆbLS 1  − c 2


2
,
which contradicts the definition of (p F EO 0 , pF EO 1 ).
Therefore,p F EO 1 −p F EO 0 = (1−α)  p∗ 1  ˆbLS 0 , ˆbLS 1  −p ∗ 0  ˆbLS 0 , ˆbLS 1  . Sop F EO 0 is the optimal solution to the
unconstrained optimization problem
min
p0
A

 1
p0 − c 2 − 1 p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2


2
+B

 1
p0 + (1−α)

p∗ 1

ˆbLS 0 , ˆbLS 1

−p ∗ 0

ˆbLS 0 , ˆbLS 1

− c 2
− 1
p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2


2
.
If we apply the first-order condition top F EO 0 , we have
A

 1
pF EO 0 − c 2 − 1 p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2

 1
pF EO 0 − c 2 2 +B

 1
pF EO 1 − c 2 − 1 p∗ 1  ˆbLS 0 , ˆbLS 1  − c 2

 1
pF EO 1 − c 2 2 = 0.
Sincep F EO g − c 2 ̸= 0 andp ∗ g

ˆbLS 0 , ˆbLS 1

− c 2 ̸= 0,
A

p∗ 0

ˆbLS 0 , ˆbLS 1

−p F EO 0
 
pF EO 1 − c 2 3  p∗ 1  ˆbLS 0 , ˆbLS 1  − c 2 
+B

p∗ 1

ˆbLS 0 , ˆbLS 1

−p F EO 1
 
pF EO 0 − c 2 3  p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2  = 0. (20)
Differentiate both sides with respect toα, and setα= 0, we have
A

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2 4  dpF EO 0 (0) dα  +B  p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2 4  dpF EO 1 (0) dα  = 0.(21)
From (19) we have
dpF EO 0 (0)
dα − dpF EO 1 (0) dα =−  p∗ 1  ˆbLS 0 , ˆbLS 1  −p ∗ 0  ˆbLS 0 , ˆbLS 1  .(22)
Combining (21) and (22) we have
dpF EO 0 (0)
dα =
B

p∗ 0

ˆbLS 0 , ˆbLS 1

− c 2
4
A

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2
4
+B

p∗ 0

ˆbLS 0 , ˆbLS 1

− c 2
4

p∗ 1

ˆbLS 0 , ˆbLS 1

−p ∗ 0

ˆbLS 0 , ˆbLS 1

.
On the other hand, EFO is written as (23):
max
p0,p1
(p0 −c) max

ˆbLS 0 p0 +a 0,0  + (p1 −c) max  ˆbLS 1 p1 +a 1,0 
s.t.|p 1 −p 0| ≤(1−α)

p∗ 1  ˆbLS 0 , ˆbLS 1  −p ∗ 0  ˆbLS 0 , ˆbLS 1 

 . (23)
Since the estimated demand with no fairness ˆbLS 0 p∗ 0

ˆbLS 0 , ˆbLS 1

+a 0, ˆbLS 1 p∗ 1

ˆbLS 0 , ˆbLS 1

+a 1 >0, there exists
ξ2 >0, such that when 0≤α≤ξ 2, ˆbLS 0 p0(α) +a 0, ˆbLS 1 p1(α) +a 1 >0. Therefore, when 0≤α≤ξ 2, (23) is
equivalent to
max
p0,p1
(p0 −c)

ˆbLS 0 p0 +a 0

+ (p1 −c)

ˆbLS 1 p1 +a 1

s.t.|p 1 −p 0| ≤(1−α)

p∗ 1  ˆbLS 0 , ˆbLS 1  −p ∗ 0  ˆbLS 0 , ˆbLS 1 

 . (24)

Elmachtoub, Kim, and T an:Learning Fair Demand Models5
Denotep EF O 0 , pEF O 1 as the optimal solution to (24). We can also prove that
pEF O 1 −p EF O 0 = (1−α)  p∗ 1  ˆbLS 0 , ˆbLS 1  −p ∗ 0  ˆbLS 0 , ˆbLS 1  .
Supposep EF O 1 −p EF O 0 <(1−α)  p∗ 1  ˆbLS 0 , ˆbLS 1  −p ∗ 0  ˆbLS 0 , ˆbLS 1  , then eitherp EF O 1 < p∗ 1  ˆbLS 0 , ˆbLS 1  orp EF O 0 >
p∗ 0

ˆbLS 0 , ˆbLS 1

. Without loss of generality, supposep EF O 1 < p∗ 1

ˆbLS 0 , ˆbLS 1

. Then∃ξ 3 >0, such thatp EF O 1 +
ξ3 ≤p ∗ 1

ˆbLS 0 , ˆbLS 1

andp EF O 1 +ξ 3 −p EF O 0 ≤(1−α)  p∗ 1  ˆbLS 0 , ˆbLS 1  −p ∗ 0  ˆbLS 0 , ˆbLS 1  . This implies that
(pEF O 0 , pEF O 1 +ξ 3) is a feasible solution to (24).
Sincep ∗ 1

ˆbLS 0 , ˆbLS 1

is the maximum point of quadratic function (p1 −c)

ˆbLS 1 p1 +a 1

, andp EF O 1 < pEF O 1 +
ξ3 < p∗ 1

ˆbLS 0 , ˆbLS 1

,

pEF O 0 −c   ˆbLS 0 pEF O 0 +a 0  +  pEF O 1 +ξ 3 −c   ˆbLS 1  pEF O 1 +ξ 3  +a 1 
>

pEF O 0 −c   ˆbLS 0 pEF O 0 +a 0  +  pEF O 1 −c   ˆbLS 1 pEF O 1 +a 1  ,
which contradicts to the definition of (p EF O 0 , pEF O 1 ).
Therefore,p EF O 1 −p EF O 0 = (1−α)  p∗ 1  ˆbLS 0 , ˆbLS 1  −p ∗ 0  ˆbLS 0 , ˆbLS 1  . Sop EF O 0 is the optimal solution to the
unconstrained optimization problem
max
p0
(p0 −c)

ˆbLS 0 p0 +a 0

+

p0 + (1−α)

p∗ 1

ˆbLS 0 , ˆbLS 1

−p ∗ 0

ˆbLS 0 , ˆbLS 1

−c

·

ˆbLS 1

p0 + (1−α)

p∗ 1

ˆbLS 0 , ˆbLS 1

−p ∗ 0

ˆbLS 0 , ˆbLS 1

+a 1

.
The objective function is a quadratic function, so we can get the closed form solution ofp EF O 0 andp EF O 1
respectively,
pEF O 0 = (1−α)p ∗ 0

ˆbLS 0 , ˆbLS 1

+α

− a0 +a 1
2

ˆbLS 0 + ˆbLS 1
 + c 2

 ,
pEF O 1 = (1−α)p ∗ 1

ˆbLS 0 , ˆbLS 1

+α

− a0 +a 1
2

ˆbLS 0 + ˆbLS 1
 + c 2

 .
Taking derivative for both sides and setα= 0, we have
dpEF O 0 (0)
dα =
ˆbLS 1
ˆbLS 0 + ˆbLS 1

p∗ 1

ˆbLS 0 , ˆbLS 1

−p ∗ 0

ˆbLS 0 , ˆbLS 1

.
Next, we show thatτ b > τp implies
dpF EO 0 (0)
dα <
dpEF O 0 (0)
dα .
dpF EO 0 (0)
dα < dpEF O 0 (0) dα ,
⇔

 B

p∗ 0

ˆbLS 0 , ˆbLS 1

− c 2
4
A

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2
4
+B

p∗ 0

ˆbLS 0 , ˆbLS 1

− c 2
4 −
ˆbLS 1
ˆbLS 0 + ˆbLS 1

  p∗ 1  ˆbLS 0 , ˆbLS 1  −p ∗ 0  ˆbLS 0 , ˆbLS 1  <0,
⇔
B

p∗ 0

ˆbLS 0 , ˆbLS 1

− c 2
4
A

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2
4
+B

p∗ 0

ˆbLS 0 , ˆbLS 1

− c 2
4 <
ˆbLS 1
ˆbLS 0 + ˆbLS 1 ,

6 Elmachtoub, Kim, and T an:Learning Fair Demand Models
⇔
A

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2
4
B

p∗ 0

ˆbLS 0 , ˆbLS 1

− c 2
4 >
ˆbLS 0
ˆbLS 1 ,
⇔

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2
4

p∗ 0

ˆbLS 0 , ˆbLS 1

− c 2
4 >
a1 1 n1 P i:g(i)=1 p(i)2  p∗ 1  ˆbLS 0 , ˆbLS 1  − c 2 
a0 1 n0 P i:g(i)=0 p(i)2  p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2  ,
⇔

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2


p∗ 0

ˆbLS 0 , ˆbLS 1

− c 2
 >

a1 1 n1 P i:g(i)=1 p(i)2
a0 1 n0 P i:g(i)=0 p(i)2
! 1
3
⇔
ˆbLS 0
ˆbLS 1 > τp.
Therefore, there existsξ >0, when the level of price fairness constraintsαsatisfies 0< α < ξ,p F EO 0 < pEF O 0 .
This also impliesp F EO 1 < pEF O 1 .
Notice thatSandWare decreasing with respect top 0 andp 1. Therefore,S F EO>S EF O,W F EO>W EF O.
Similarly, we can get that
dpF EO 0 (0)
dα > dpEF O 0 (0) dα ⇔τ b < τp.
Therefore, there existsξ >0, when the level of price fairness constraintsαsatisfies 0< α < ξ,p F EO 0 > pEF O 0 .
This also impliesp F EO 1 > pEF O 1 ,S F EO<S EF O, andW F EO<W EF O.
Ifτ b =τ p,
dpF EO 0 (0)
dα =
dpEF O 0 (0)
dα . In this case we prove that
d2pF EO 0 (0)
dα2 >0 and
d2pEF O 0 (0)
dα2 = 0. For FEO, take
the second-order derivative with respect toαfor equation (20) and setα= 0, we have
A

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2 4 d2pF EO 0 (0) dα2 + 6A  p∗ 1  ˆbLS 0 , ˆbLS 1  − c 2 3 dpF EO 0 (0) dα dpF EO 1 (0) dα
+B

p∗ 0

ˆbLS 0 , ˆbLS 1

− c 2 4 d2pF EO 1 (0) dα2 + 6B  p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2 3 dpF EO 0 (0) dα dpF EO 1 (0) dα = 0.
From equation (19) we have
d2pF EO 0 (0)
dα2 =
d2pF EO 1 (0)
dα2 . Notice that
dpF EO 0 (0)
dα >0 and
dpF EO 1 (0)
dα <0, so we have
A

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2 4 d2pF EO 0 (0) dα2 +B  p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2 4 d2pF EO 0 (0) dα2
=−6A

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2 3 dpF EO 0 (0) dα dpF EO 1 (0) dα −6B  p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2 3 dpF EO 0 (0) dα dpF EO 1 (0) dα >0.
Therefore,
d2pF EO 0 (0)
dα2 >0. On the other hand, sincep EF O 0 = (1−α)p ∗ 0

ˆbLS 0 , ˆbLS 1

+α

− a0+a1
2(ˆbLS 0 +ˆbLS 1 ) + c 2

for
0≤α≤ξ 2, we have
d2pEF O 0 (0)
dα2 = 0. Then we have
d2pF EO 0 (0)
dα2 >
d2pEF O 0 (0)
dα2 . By comparing the second-order
Taylor expansion ofp F EO 0 andp EF O 1 , there existsξ >0, when the level of price fairness constraintsαsatisfies
0< α < ξ,pF EO 0 > pEF O 0 . This also impliesp F EO 1 > pEF O 1 ,S F EO<S EF O, andW F EO<W EF O.
Next, we prove the corresponding results for parity-wise demand fairness. Similar to parity-wise price
fairness, we first calculate the first order derivatives of the optimal prices with respect toα.
For parity-wise demand fairness, FEO and EFO are written as (25) and (26):
min
ˆb0,ˆb1
1
n0
X
i:g(i)=0

a0 + ˆb0p(i) −d (i)
2
+ 1 n1 X i:g(i)=1  a1 + ˆb1p(i) −d (i) 2
s.t.

 1 a1  a1 + ˆbLS 1 p∗ 1  ˆb0, ˆb1  − 1 a0  a0 +b LS 0 p∗ 0  ˆb0, ˆb1 

≤(1−α)

 1 a1  a1 + ˆbLS 1 p∗ 1  ˆbLS 0 , ˆbLS 1  − 1 a0  a0 +b LS 0 p∗ 0  ˆbLS 0 , ˆbLS 1 

 .
(25)

Elmachtoub, Kim, and T an:Learning Fair Demand Models7
and
max
p0,p1
(p0 −c) max

ˆbLS 0 p0 +a 0,0  + (p1 −c) max  ˆbLS 1 p1 +a 1,0 
s.t.

 1 a1  a1 + ˆbLS 1 p1  − 1 a0  a0 + ˆbLS 0 p0 

≤(1−α)

 1 a1  a1 + ˆbLS 1 p∗ 1  ˆbLS 0 , ˆbLS 1  − 1 a0  a0 + ˆbLS 0 p∗ 0  ˆbLS 0 , ˆbLS 1 

 .
(26)
For FEO, using (16) and changing the decision variables in (25) top 0, p1 instead of ˆb0, ˆb1, we can get the
equivalent problem
min
p0,p1
A

 1
p0 − c 2 − 1 p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2


2
+B

 1
p1 − c 2 − 1 p∗ 1  ˆbLS 0 , ˆbLS 1  − c 2


2
s.t.

 ˆbLS 1 a1 p1 − ˆbLS 0 a0 p0

 ≤(1−α)

 ˆbLS 1 a1 p∗ 1  ˆbLS 0 , ˆbLS 1  − ˆbLS 0 a0 p∗ 0  ˆbLS 0 , ˆbLS 1 

 . (27)
Similar to price fairness, denotep F EO 0 , pF EO 1 as the optimal solution to (27). We can prove that
ˆbLS 1
a1
pF EO 1 − ˆbLS 0 a0 pF EO 0 = (1−α)  ˆbLS 1 a1 p∗ 1  ˆbLS 0 , ˆbLS 1  − ˆbLS 0 a0 p∗ 0  ˆbLS 0 , ˆbLS 1 ! .(28)
Suppose
ˆbLS 1
a1 pF EO 1 − ˆbLS 0 a0 pF EO 0 <(1−α)  ˆbLS 1 a1 p∗ 1  ˆbLS 0 , ˆbLS 1  − ˆbLS 0 a0 p∗ 0  ˆbLS 0 , ˆbLS 1  , then eitherp F EO 1 >
p∗ 1

ˆbLS 0 , ˆbLS 1

orp F EO 0 < p∗ 0

ˆbLS 0 , ˆbLS 1

. Without loss of generality, supposep F EO 1 > p∗ 1

ˆbLS 0 , ˆbLS 1

.
Then∃ξ 4 >0, such thatp EF O 1 −ξ 4 ≥p ∗ 1

ˆbLS 0 , ˆbLS 1

and
ˆbLS 1
a1

pF EO 1 −ξ 4  − ˆbLS 0 a0 pF EO 0 <
(1−α)
 ˆbLS 1
a1 p∗ 1

ˆbLS 0 , ˆbLS 1

−
ˆbLS 0
a0 p∗ 0

ˆbLS 0 , ˆbLS 1

. This implies that (p F EO 0 , pF EO 1 −ξ 4) is a feasible solution to
(27).
However,
A

 1
pF EO 0 − c 2 − 1 p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2


2
+B

 1
pF EO 1 − c 2 − 1 p∗ 1  ˆbLS 0 , ˆbLS 1  − c 2


2
> A

 1
pF EO 0 − c 2 − 1 p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2


2
+B

 1
pF EO 1 −ξ 4 − c 2 − 1 p∗ 1  ˆbLS 0 , ˆbLS 1  − c 2


2
,
which contradicts to the definition of (p F EO 0 , pF EO 1 ).
Therefore,
ˆbLS 1
a1 pF EO 1 − ˆbLS 0 a0 pF EO 0 = (1−α)  ˆbLS 1 a1 p∗ 1  ˆbLS 0 , ˆbLS 1  − ˆbLS 0 a0 p∗ 0  ˆbLS 0 , ˆbLS 1  . Sop F EO 0 is the optimal
solution to the unconstrained optimization problem
min
p0
A

 1
p0 − c 2 − 1 p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2


2
+B

 1
a1
ˆbLS 1
 ˆbLS 0
a0 pF EO 0 + (1−α)  ˆbLS 1 a1 p∗ 1  ˆbLS 0 , ˆbLS 1  − ˆbLS 0 a0 p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2 − 1 p∗ 1  ˆbLS 0 , ˆbLS 1  − c 2


2
.
Apply the first-order condition top F EO 0 , we have
2A

 1
pF EO 0 − c 2 − 1 p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2



− 1
pF EO 0 − c 2 2
!
+

8 Elmachtoub, Kim, and T an:Learning Fair Demand Models
2B

 1
a1
ˆbLS 1
 ˆbLS 0
a0 pF EO 0 + (1−α)  ˆbLS 1 a1 p∗ 1  ˆbLS 0 , ˆbLS 1  − ˆbLS 0 a0 p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2 − 1 p∗ 1  ˆbLS 0 , ˆbLS 1  − c 2

 ·

− 1
a1
ˆbLS 1
 ˆbLS 0
a0 pF EO 0 + (1−α)  ˆbLS 1 a1 p∗ 1  ˆbLS 0 , ˆbLS 1  − ˆbLS 0 a0 p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2 2

 a1ˆbLS 0
a0ˆbLS 1 = 0,
which is equivalent to
A

 1
pF EO 0 − c 2 − 1 p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2

 1
pF EO 0 − c 2 2 +B

 1
pF EO 1 − c 2 − 1 p∗ 1  ˆbLS 0 , ˆbLS 1  − c 2

 1
pF EO 1 − c 2 2
a1ˆbLS 0
a0ˆbLS 1 = 0.
sincep F EO g − c 2 ̸= 0 andp ∗ g

ˆbLS 0 , ˆbLS 1

− c 2 ̸= 0,
A

p∗ 0

ˆbLS 0 , ˆbLS 1

−p F EO 0
 
pF EO 1 − c 2 3 +B  p∗ 1  ˆbLS 0 , ˆbLS 1  −p F EO 1   pF EO 0 − c 2 3 = 0.(29)
Differentiate both sides with respect toα, and setα= 0, we have
A

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2 3  dpF EO 0 (0) dα  +B  p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2 3  dpF EO 1 (0) dα  = 0.(30)
From (28) we have
ˆbLS 1
a1
dpF EO 1 (0)
dα −
ˆbLS 0
a0
dpF EO 0 (0)
dα =−
 ˆbLS 1
a1
p∗ 1

ˆbLS 0 , ˆbLS 1

−
ˆbLS 0
a0
p∗ 0

ˆbLS 0 , ˆbLS 1
!
,(31)
so combining (30) and (31) we have
dpF EO 0 (0)
dα =
B

p∗ 0

ˆbLS 0 , ˆbLS 1

− c 2
2
A

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2
2
+B

p∗ 0

ˆbLS 0 , ˆbLS 1

− c 2
2

p∗ 0

ˆbLS 0 , ˆbLS 1

−p ∗ 1

ˆbLS 0 , ˆbLS 1

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2
c
2
for the FEO problem.
For the EFO problem, since the estimated demand with no fairnessˆbLS 0 p∗ 0

ˆbLS 0 , ˆbLS 1

+a 0, ˆbLS 1 p∗ 1

ˆbLS 0 , ˆbLS 1

+
a1 >0, there existsξ 2 >0, such that when 0≤α≤ξ 5, ˆbLS 0 p0(α) +a 0, ˆbLS 1 p1(α) +a 1 >0. Therefore, when
0≤α≤ξ 5, (23) is equivalent to
max
p0,p1
(p0 −c)

ˆbLS 0 p0 +a 0

+ (p1 −c)

ˆbLS 1 p1 +a 1

s.t.

 1 a1  a1 + ˆbLS 1 p1  − 1 a0  a0 + ˆbLS 0 p0 

≤(1−α)

 1 a1  a1 + ˆbLS 1 p∗ 1  ˆbLS 0 , ˆbLS 1  − 1 a0  a0 + ˆbLS 0 p∗ 0  ˆbLS 0 , ˆbLS 1 

 .
(32)
Denotep EF O 0 , pEF O 1 as the optimal solution to (32). We can also prove that
ˆbLS 1
a1
pEF O 1 − ˆbLS 0 a0 pEF O 0 = (1−α)  ˆbLS 1 a1 p∗ 1  ˆbLS 0 , ˆbLS 1  − ˆbLS 0 a0 p∗ 0  ˆbLS 0 , ˆbLS 1 ! .
Suppose
ˆbLS 1
a1 pEF O 1 − ˆbLS 0 a0 pEF O 0 <(1−α)  ˆbLS 1 a1 p∗ 1  ˆbLS 0 , ˆbLS 1  − ˆbLS 0 a0 p∗ 0  ˆbLS 0 , ˆbLS 1  , then eitherp EF O 1 >
p∗ 1

ˆbLS 0 , ˆbLS 1

orp EF O 0 < p∗ 0

ˆbLS 0 , ˆbLS 1

. Without loss of generality, supposep EF O 1 > p∗ 1

ˆbLS 0 , ˆbLS 1

.
Then∃ξ 6 >0, such thatp EF O 1 −ξ 6 ≥p ∗ 1

ˆbLS 0 , ˆbLS 1

and
ˆbLS 1
a1

pEF O 1 −ξ 6  − ˆbLS 0 a0 pEF O 0 <

Elmachtoub, Kim, and T an:Learning Fair Demand Models9
(1−α)
 ˆbLS 1
a1 p∗ 1

ˆbLS 0 , ˆbLS 1

−
ˆbLS 0
a0 p∗ 0

ˆbLS 0 , ˆbLS 1

. This implies that (p EF O 0 , pEF O 1 −ξ 6) is a feasible solution to
(24).
Sincep ∗ 1

ˆbLS 0 , ˆbLS 1

is the maximum point of quadratic function (p1 −c)

ˆbLS 1 p1 +a 1

, andp EF O 1 > pEF O 1 −
ξ6 > p∗ 1

ˆbLS 0 , ˆbLS 1

,

pEF O 0 −c   ˆbLS 0 pEF O 0 +a 0  +  pEF O 1 −ξ 6 −c   ˆbLS 1  pEF O 1 −ξ 6  +a 1 
>

pEF O 0 −c   ˆbLS 0 pEF O 0 +a 0  +  pEF O 1 −c   ˆbLS 1 pEF O 1 +a 1  ,
which contradicts to the definition of (p EF O 0 , pEF O 1 ).
Therefore,
ˆbLS 1
a1 pEF O 1 − ˆbLS 0 a0 pEF O 0 = (1−α)  ˆbLS 1 a1 p∗ 1  ˆbLS 0 , ˆbLS 1  − ˆbLS 0 a0 p∗ 0  ˆbLS 0 , ˆbLS 1  . Sop EF O 0 is the optimal
solution to the unconstrained optimization problem
max
p0
(p0 −c)

ˆbLS 0 p0 +a 0

+

a1
ˆbLS 1
 ˆbLS 0
a0
pF EO 0 + (1−α)
 ˆbLS 1
a1
p∗ 1

ˆbLS 0 , ˆbLS 1

−
ˆbLS 0
a0
p∗ 0

ˆbLS 0 , ˆbLS 1
!!
−c
!
·

ˆbLS 1

a1
ˆbLS 1
 ˆbLS 0
a0
pF EO 0 + (1−α)
 ˆbLS 1
a1
p∗ 1

ˆbLS 0 , ˆbLS 1

−
ˆbLS 0
a0
p∗ 0

ˆbLS 0 , ˆbLS 1
!!!
+a 1
!
.
The objective function is a quadratic function with respect top 0, so we can get the closed form solution of
pEF O 0 andp EF O 1 respectively,
pEF O 0 = (1−α)p ∗ 0

ˆbLS 0 , ˆbLS 1

+α a0
ˆbLS 0

− 1 2 + c 2 a0 +a 1 a2 0
ˆbLS 0 +
a2 1
ˆbLS 1

 ,
pEF O 1 = (1−α)p ∗ 1

ˆbLS 0 , ˆbLS 1

+α a1
ˆbLS 1

− 1 2 + c 2 a0 +a 1 a2 0
ˆbLS 0 +
a2 1
ˆbLS 1

 .
Taking the derivative of both sides, we have
dpEF O 0
dα = c 2
a0a1
ˆbLS 0 −
a2 1
ˆbLS 1
a2 0
ˆbLS 0 +
a2 1
ˆbLS 1
.
Next, we show thatτ b > τp implies
dpF EO 0 (0)
dα >
dpEF O 0 (0)
dα .
dpF EO 0 (0)
dα =
B

p∗ 0

ˆbLS 0 , ˆbLS 1

− c 2
2
A

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2
2
+B

p∗ 0

ˆbLS 0 , ˆbLS 1

− c 2
2

p∗ 0

ˆbLS 0 , ˆbLS 1

−p ∗ 1

ˆbLS 0 , ˆbLS 1

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2
c
2 > c 2
a0a1
ˆbLS 0 −
a2 1
ˆbLS 1
a2 0
ˆbLS 0 +
a2 1
ˆbLS 1
⇔
B

p∗ 0

ˆbLS 0 , ˆbLS 1

− c 2
2
A

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2
2
+B

p∗ 0

ˆbLS 0 , ˆbLS 1

− c 2
2 <
a1

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2

a0

p∗ 0

ˆbLS 0 , ˆbLS 1

− c 2

+a 1

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2

⇔
A

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2
2
B

p∗ 0

ˆbLS 0 , ˆbLS 1

− c 2
2 >
a0

p∗ 0

ˆbLS 0 , ˆbLS 1

− c 2

a1

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2

⇔

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2


p∗ 0

ˆbLS 0 , ˆbLS 1

− c 2
 >

a1 1 n1 P i:g(i)=1 p(i)2
a0 1 n0 P i:g(i)=0 p(i)2
! 1
3

10 Elmachtoub, Kim, and T an:Learning Fair Demand Models
⇔
ˆbLS 0
ˆbLS 1
> τp.
Therefore, there existsξ >0, when the level of price fairness constraintsαsatisfies 0< α < ξ,p F EO 0 > pEF O 0 .
This also impliesp F EO 1 > pEF O 1 .
Notice thatSandRare decreasing with respect top 0 andp 1. Therefore,S F EO<S EF O,W F EO<W EF O.
Similarly, we have
dpF EO 0 (0)
dα < dpEF O 0 (0) dα ⇔τ b < τp
Therefore, there existsξ >0, when the level of price fairness constraintsαsatisfies 0< α < ξ,p F EO 0 < pEF O 0 .
This also impliesp F EO 1 < pEF O 1 ,S F EO>S EF O, andW F EO>W EF O.
Ifτ b =τ p,
dpF EO 0 (0)
dα =
dpEF O 0 (0)
dα . Similar to parity-wise price fairness, we take the second-order derivative
ofαin equation (29) and setα= 0 to get
A

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2 3 d2pF EO 0 (0) dα2 + 6A  p∗ 1  ˆbLS 0 , ˆbLS 1  − c 2 2 dpF EO 0 (0) dα dpF EO 1 (0) dα
+B

p∗ 0

ˆbLS 0 , ˆbLS 1

− c 2 3 d2pF EO 1 (0) dα2 + 6B  p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2 2 dpF EO 0 (0) dα dpF EO 1 (0) dα = 0.
From equation (28) we have
ˆbLS 0
a0
d2pF EO 0 (0)
dα2 =
ˆbLS 1
a1
d2pF EO 1 (0)
dα2 . Notice that
dpF EO 0 (0)
dα <0 and
dpF EO 1 (0)
dα >0, so
we have
A

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2 3 d2pF EO 0 (0) dα2 +B  p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2 3 d2pF EO 0 (0) dα2
=−6A

p∗ 1

ˆbLS 0 , ˆbLS 1

− c 2 2 dpF EO 0 (0) dα dpF EO 1 (0) dα −6B  p∗ 0  ˆbLS 0 , ˆbLS 1  − c 2 2 dpF EO 0 (0) dα dpF EO 1 (0) dα >0.
Therefore,
d2pF EO 0
dα2 >0. On the other hand
d2pEF O 0
dα2 = 0. So
d2pF EO 0
dα2 >
d2pEF O 0
dα2 . By comparing the second-order
Taylor expansion ofp F EO 0 andp EF O 1 , there existsξ >0, when the level of price fairness constraintsαsatisfies
0< α < ξ,pF EO 0 > pEF O 0 . This also impliesp F EO 1 > pEF O 1 ,S F EO<S EF O, andW F EO<W EF O.□
Proof of Proposition 3.Without loss of generality, supposep LS 0 < pLS 1 . Thenτ b > τa.
R(p0, p1) =
X
g∈{0,1}
ng (pg −c) max (0, ag +b gpg),
There existsξ 3 >0, such that when 0< α < ξ3,a 0 +b 0p0, a1 +b 1p1 >0.
R

pF EO 0 , pF EO 1  − R  pEF O 0 , pEF O 1  = X
g∈{0,1}

pF EO g −c   ag +b gpF EO g  −  pEF O g −c   ag +b gpEF O g 
=
X
g∈{0,1}
bg

pF EO g −

− ag
2bg
+ c 2 2 −b g  pEF O g −  − ag 2bg + c 2 2
=
X
g∈{0,1}
bg

pF EO g −p EF O g   pF EO g +p EF O g −  − ag bg +c  .
d

R

pF EO 0 , pF EO 1  − R  pEF O 0 , pEF O 1 
dα =
X
g∈{0,1}
bg
 dpF EO g
dα − dpEF O g dα   pF EO g +p EF O g −  − ag bg +c 
+bg

pF EO g −p EF O g   dpF EO g dα + dpEF O g dα  .

Elmachtoub, Kim, and T an:Learning Fair Demand Models11
Whenα= 0,
d

R

pF EO 0 , pF EO 1  − R  pEF O 0 , pEF O 1 
dα
α=0 =
X
g∈{0,1}
bg
 dpF EO g
dα
α=0 − dpEF O g
dα
α=0
 
2pLS g −

− ag
bg
+c

=
 dpF EO 0
dα
α=0 − dpEF O 0
dα
α=0

a0

1− b0
ˆbLS 0
!
+a 1

1− b1
ˆbLS 1
!!
For parity-wise price fairness, by Proposition 2,
dpF EO 0
dα
α=0 − dpEF O 0
dα
α=0 <0⇔τ b > τp,
therefore, ifτ b > τp and
a0

1− b0
ˆbLS 0
!
+a 1

1− b1
ˆbLS 1
!
<0,
we have
d

R

pF EO 0 , pF EO 1  − R  pEF O 0 , pEF O 1 
dα
α=0 >0,
then there existsξ >0, when the fairness levelαsatisfies 0< α < ξ,R F EO>R EF O. Similarly, ifτ b < τp and
a0

1− b0
ˆbLS 0
!
+a 1

1− b1
ˆbLS 1
!
>0,
we have
d

R

pF EO 0 , pF EO 1  − R  pEF O 0 , pEF O 1 
dα
α=0 >0.
For parity-wise demand fairness,
dpF EO 0
dα
α=0 − dpEF O 0
dα
α=0 <0⇔τ b < τp,
therefore, ifτ b > τp and
a0

1− b0
ˆbLS 0
!
+a 1

1− b1
ˆbLS 1
!
>0,
we have
d

R

pF EO 0 , pF EO 1  − R  pEF O 0 , pEF O 1 
dα
α=0 >0,
then there existsξ >0, when the fairness levelαsatisfies 0< α < ξ,R F EO>R EF O. Similarly, ifτ b < τp and
a0

1− b0
ˆbLS 0
!
+a 1

1− b1
ˆbLS 1
!
<0,
we have
d

R

pF EO 0 , pF EO 1  − R  pEF O 0 , pEF O 1 
dα
α=0 >0.
Next we consider the case whereτ b =τ p. Then,
d

R

pF EO 0 , pF EO 1  − R  pEF O 0 , pEF O 1 
dα
α=0 = 0.
Taking the second order derivative ofαand setα= 0, we have
d2  R  pF EO 0 , pF EO 1  − R  pEF O 0 , pEF O 1 
dα2 α=0 =
 d2pF EO 0
dα2 α=0 − d2pEF O 0 dα2 α=0   a0  1− b0 ˆbLS 0 ! +a 1  1− b1 ˆbLS 1 !!
= d2pF EO 0
dα2 α=0

a0

1− b0
ˆbLS 0
!
+a 1

1− b1
ˆbLS 1
!!
.

12 Elmachtoub, Kim, and T an:Learning Fair Demand Models
Notice that
d2pF EO 0
dα2 α=0 >0, therefore, when
a0

1− b0
ˆbLS 0
!
+a 1

1− b1
ˆbLS 1
!
>0,
we have
d

R

pF EO 0 , pF EO 1  − R  pEF O 0 , pEF O 1 
dα
α=0 >0,
then there existsξ >0, when the fairness levelαsatisfies 0< α < ξ,R F EO>R EF O.
In all these cases above, if the sign ofa 0

1− b0 ˆbLS 0

+a 1

1− b1 ˆbLS 1

changes, the sign of
d

R

pF EO 0 , pF EO 1  − R  pEF O 0 , pEF O 1 
dα
α=0
also changes. Therefore, we are able to characterize the cases whereR FEO <R EFO accordingly.□
Proof of Proposition 4.Without loss of generality, supposep LS 0 < pLS 1 . For Rawlsian price fairness, FEO
is written as (33)
min
ˆb0,ˆb1
1
n0
X
i:g(i)=0

a0 + ˆb0p(i) −d (i)
2
+ 1 n1 X i:g(i)=1  a1 + ˆb1p(i) −d (i) 2
s.t.p ∗ g

ˆb0, ˆb1

≤(1−α)¯p+αp , g= 0,1.
(33)
Sincep LS 0 < pLS 1 , ¯p=p LS 1 ,p =p LS 0 . Notice thatp LS g =− ag 2ˆbLS g + c 2 , so problem (33) can be divided into two
subproblems
min
ˆbg
1
ng
X
i:g(i)=g

ag + ˆbgp(i) −d (i)
2
s.t.− ag
2ˆbLS g
+ c 2 ≤(1−α)¯p+αp . (34)
forg∈ {0,1}.
For group 0, sincep LS 0 =p ≤(1−α)¯p+αp , the optimal solution for (34) is still ˆbLS 0 . For group 1, (34) can
be written as a convex optimization problem
min
ˆb1
1
n1
X
i:g(i)=1

a1 + ˆb1p(i) −d (i)
2
s.t.− a1
2 ≥

(1−α)¯p+αp − c 2  ˆbLS 1 .
with a single variable ˆb1. We can get the closed form solution ˆbFEO 1 =− a1 2((1−α) ¯p+αp− c 2 ) . Therefore,
p∗ 0

ˆbFEO 0 , ˆbFEO 1

=p LS 0 andp ∗ 1

ˆbFEO 0 , ˆbFEO 1

= (1−α)p LS 1 +αp LS 0 .
On the other hand, EFO can be written as (35)
max
p0,p1
(p0 −c) max

ˆbLS 0 p0 +a 0,0  + (p1 −c) max  ˆbLS 1 p1 +a 1,0 
s.t.p g ≤(1−α)¯p+αp ,∀g∈ {0,1}.
(35)
which can also be divided into two subproblems
max
pg
(pg −c) max

ˆbLS g pg +a g,0 
s.t.p g ≤(1−α)¯p+αp ,∀g∈ {0,1}.
(36)

Elmachtoub, Kim, and T an:Learning Fair Demand Models13
For group 0, sincep LS 0 =p ≤(1−α)¯p+αp , the optimal solution for (34) is still ˆbLS 0 . For group 1, with
the Rawlsian price fairness constraints,p 1 ≤¯p, so ˆbLS 1 p1 +a 1 ≥ ˆbLS 1 ¯p+a1 = ˆbLS 1 pLS 1 +a 1 >0. Then (36) is
maximizing a quadratic function with boundary constraints, from which we can get the closed form optimal
solutionp EFO 1 =p LS 1 .
Therefore, we have
p∗ 0

ˆbFEO 0 , ˆbFEO 1

=p EFO 0 =p LS 0 , p ∗ 1

ˆbFEO 0 , ˆbFEO 1

=p EFO 1 = (1−α)p LS 1 +αp LS 0 .
For Rawlsian demand fairness, FEO is written as (37)
min
ˆb0,ˆb1
1
n0
X
i:g(i)=0

a0 + ˆb0p(i) −d (i)
2
+ 1 n1 X i:g(i)=1  a1 + ˆb1p(i) −d (i) 2
s.t. 1 ag  ag + ˆbgp∗ g  ˆb0, ˆb1  ≥(1−α)d +α ¯d,∀g∈ {0,1}, (37)
where
d = a1 + ˆbLS 1 pLS 1
a1
= 1 +
ˆbLS 1
a1
pLS 1 = 1 2 − cˆbLS 1 2a1 and ¯d= a0 + ˆbLS 0 pLS 0 a0 = 1 + ˆbLS 0 a0 pLS 0 = 1 2 − cˆbLS 0 2a0 .
Since− a0
2ˆbLS 0 + c 2 =p LS 1 > pLS 1 =− a1 2ˆbLS 1 + c 2 , ¯d > d. (37) can be divided into two subproblems
min
ˆbg
1
ng
X
i:g(i)=g

ag + ˆbgp(i) −d (i)
2
s.t. 1 +
ˆbg
ag
p∗ g

ˆb0, ˆb1

≥(1−α)d +α ¯d,∀g∈ {0,1}.
Only group 1 is binding. Therefore,p FEO 0 =p LS 0 and
pFEO 1 = (1−α)d +α ¯d−1 = (1−α)p LS 1 +α a1 a0 ˆbLS 0 ˆbLS 1 pLS 0 .
On the other hand, EFO can be written as (38)
max
p0,p1
(p0 −c) max

ˆbLS 0 p0 +a 0,0  + (p1 −c) max  ˆbLS 1 p1 +a 1,0 
s.t. 1 ag  ag + ˆbgpg  ≥(1−α)d +α ¯d,∀g∈ {0,1}, (38)
which can also be divided into two subproblems
max
pg
(pg −c) max

ˆbLS g pg +a g,0 
s.t. 1 ag  ag + ˆbgpg  ≥(1−α)d +α ¯d,∀g∈ {0,1},
which are also maximizing quadratic functions with linear constraints. Therefore, same as price fairness, the
closed form solution satisfies
p∗ 0

ˆbFEO 0 , ˆbFEO 1

=p EFO 0 =p LS 0 , p ∗ 1

ˆbFEO 0 , ˆbFEO 1

= (1−α)p LS 1 +α a1ˆbLS 0
a0ˆbLS 1 pLS 0 .
Lastly, in the case wherep ∗ 0(ˆbLS 0 , ˆbLS 1 )< p∗ 1(b0, b1)< p∗ 1(ˆbLS 0 , ˆbLS 1 ), an increase inαfrom zero causes the
prices under both FEO and EFO to decrease until they converge to the true optimal price,p ∗ 1(b0, b1). Within
this range ofα, the decrease inp 1 directly enhances total surplus. Furthermore, asp 1 approaches the true
optimal pricep ∗ 1(b0, b1), the firm’s profit also increases. Consequently, social welfare, the sum of profit and
surplus, increases as well. □

14 Elmachtoub, Kim, and T an:Learning Fair Demand Models
Proof of Proposition 5Without loss of generality, supposep LS 0 < pLS 1 . Then we haveτ b > τa. Denote
qg = 1 ˆbLS g vg.
For parity-wiseprice fairness, FEO is written as (39)
min
ˆa0,ˆb0,ˆa1,ˆb1
1
n0
X
i:g(i)=0

ˆa0 + ˆb0p(i) −d (i)
2
+ 1 n1 X i:g(i)=1  ˆa1 + ˆb1p(i) −d (i) 2
s.t.

p∗ 1  ˆa1, ˆb1  −p ∗ 0  ˆa0, ˆb0 

 ≤(1−α)

pLS 1 −p LS 0

 , (39)
wherep ∗ g

ˆag, ˆbg

=− ˆag
2ˆbg + c 2 . Denoteθ g =
ˆag
ˆbg

, we can rewrite problem (39) as (40):
min
θ0,θ1

θ0 −θ LS 0 T M0  θ0 −θ LS 0  +  θ1 −θ LS 1 T M1  θ1 −θ LS 1 
s.t.|p ∗ 1 (θ1)−p ∗ 0 (θ0)| ≤(1−α)

pLS 1 −p LS 0

 . (40)
First, we can show that the optimal solution of problem (40) (θ FEO 0 , θFEO 1 ) satisfy
p∗ 1  θFEO 1  −p ∗ 0  θFEO 0  = (1−α)  pLS 1 −p LS 0  .(41)
Ifp ∗ 1 (θ1)−p ∗ 0 (θ0)<(1−α)  pLS 1 −p LS 0  , eitherp ∗ 1 (θ1)< pLS 1 orp ∗ 0 (θ0)> pLS 0 . Without loss of generality,
supposep ∗ 0 (θ0)> pLS 0 . sincep ∗ 0(θ) is continuous with respect toθ, there existsξ 1 ∈(0,1], such thatp ∗ 1 (θ1)−
p∗ 0  ξ1θ0 + (1−ξ 1)θ LS 0  <(1−α)  pLS 1 −p LS 0  . Therefore, (ξ1θFEO 0 + (1−ξ 1)θ LS 0 , θFEO 1 ) is a feasible solution to
(40) with strictly smaller objective value, which contradicts to the definition of (θ FEO 0 , θFEO 1 ).
Therefore, the optimal solution of problem (40) is equivalent to the optimal solution of
min
θ0,θ1

θ0 −θ LS 0 T M0  θ0 −θ LS 0  +  θ1 −θ LS 1 T M1  θ1 −θ LS 1 
s.t.p ∗ 1 (θ1)−p ∗ 0 (θ0) = (1−α)  pLS 1 −p LS 0  . (42)
The KKT conditions of problem (42) with LagrangianL(θ 0, θ1, λ) =

θ0 −θ LS 0 T M0  θ0 −θ LS 0  +
θ1 −θ LS 1 T M1  θ1 −θ LS 1  +λ  p∗ 1 (θ1)−p ∗ 0 (θ0)−(1−α)  pLS 1 −p LS 0  are
∂L
∂θ0
= 2M0

θ0 −θ LS 0  −λ
" 1
2ˆb0
− ˆa0
2ˆb2 0
#
= 0,(43a)
∂L
∂θ1
= 2M1

θ1 −θ LS 1  +λ
" 1
2ˆb1
− ˆa1
2ˆb2 1
#
= 0,(43b)
λ

p∗ 1 (θ1)−p ∗ 0 (θ0)−(1−α)  pLS 1 −p LS 0  = 0.
Differentiate (43a) and (43b) with respect toα, we have
2M0∇αθ0 − dλ dα
" 1
2ˆb0
− ˆa0
2ˆb2 0
#
−λ∇ α
 " 1
2ˆb0
− ˆa0
2ˆb2 0
#!
= 0,
2M1∇αθ1 + dλ dα
" 1
2ˆb1
− ˆa1
2ˆb2 1
#
+λ∇ α
 " 1
2ˆb1
− ˆa1
2ˆb2 1
#!
= 0.
Whenα= 0, we haveλ= 0. Therefore,
2M0∇αθ0|α=0 −q 0
dλ
dα

α=0
= 0,
2M1∇αθ1|α=0 +q 1
dλ
dα

α=0
= 0.

Elmachtoub, Kim, and T an:Learning Fair Demand Models15
sinceM 0,M 1 are invertible, we have
∇αθ0|α=0 = 1 2 M −1 0 q0 dλ dα

 α=0 ,
∇αθ1|α=0 =− 1 2 M −1 1 q1 dλ dα

 α=0 .
On the other hand, differentiate both sides of (41) and setα= 0, we have
qT 1 ∇αθ1|α=0 −q T 0 ∇αθ0|α=0 =−(p LS 1 −p LS 0 ).
Replace∇ αθ0|α=0 and∇ αθ1|α=0 by 1 2 M −1 0 q0 dλ dα

 α=0 and− 1 2 M −1 1 q1 dλ dα

 α=0, we have
1
2 (qT 1 M −1 1 q1 +q T 0 M −1 0 q0) dλ dα

 α=0 =p LS 1 −p LS 0 .
Therefore,
dλ
dα

α=0
= 2

pLS 1 −p LS 0 
qT 1 M −1 1 q1 +q T 0 M −1 0 q0 ,
and
dp∗ 0  θFEO 0 
dα

α=0
=q T 0 ∇αθ0|α=0 = qT 0 M −1 0 q0 qT 1 M −1 1 q1 +q T 0 M −1 0 q0  pLS 1 −p LS 0  .
On the other hand,
dpEFO 0
dα

α=0
=
ˆbLS 1
ˆbLS 0 + ˆbLS 1

pLS 1 −p LS 0  ,
so
dp∗ 0  θFEO 0 
dα

α=0
< dpEFO 0
dα

α=0
⇔ qT 0 M −1 0 q0
qT 1 M −1 1 q1 +q T 0 M −1 0 q0

pLS 1 −p LS 0  < ˆbLS 1 ˆbLS 0 + ˆbLS 1  pLS 1 −p LS 0 
⇔q T 0 M −1 0 q0ˆbLS 0 > qT 1 M −1 1 q1ˆbLS 1 .
Therefore, ifq T 0 M −1 0 q0ˆbLS 0 > qT 1 M −1 1 q1ˆbLS 1 , there existsξ >0 such that when 0< α < ξ, FEO leads to lower
prices than EFO and hence FEO gives higher consumer surplus and social welfare. Similarly, ifqT 0 M −1 0 q0ˆbLS 0 <
qT 1 M −1 1 q1ˆbLS 1 , dp∗ 0(θFEO 0 ) dα |α=0 > dpEFO 0 dα |α=0, then FEO leads to higher prices than EFO and gives lower con-
sumer surplus and social welfare.
For parity-wisedemand fairness, FEO is written as (44)
min
ˆa0,ˆb0,ˆa1ˆb1
1
n0
X
i:g(i)=0

ˆa0 + ˆb0p(i) −d (i)
2
+ 1 n1 X i:g(i)=1  ˆa1 + ˆb1p(i) −d (i) 2
s.t.

 1 ˆaLS 1  ˆaLS 1 + ˆbLS 1 p∗ 1  ˆa1, ˆb1  − 1 ˆaLS 0  ˆaLS 1 + ˆbLS 0 p∗ 0  ˆa0, ˆb0 

≤(1−α)

 1 ˆaLS 1  ˆaLS 1 + ˆbLS 1 pLS 1  − 1 ˆaLS 0  ˆaLS 1 + ˆbLS 0 pLS 0 

 ,
(44)
which can be rewritten as (45):
min
θ0,θ1

θ0 −θ LS 0 T M0  θ0 −θ LS 0  +  θ1 −θ LS 1 T M1  θ1 −θ LS 1 
s.t.

 ˆbLS 1 ˆaLS 1 p∗ 1 (θ1)− ˆbLS 0 ˆaLS 0 p∗ 0 (θ0)

 ≤(1−α)

 ˆbLS 1 ˆaLS 1 pLS 1 − ˆbLS 0 ˆaLS 0 pLS 0

 . (45)

16 Elmachtoub, Kim, and T an:Learning Fair Demand Models
Similar to the case of parity-wise price fairness, we can show that the optimal solution of problem (45)

θFEO 0 , θFEO 1  satisfy
ˆbLS 1
ˆaLS 1 p∗ 1 (θ1)− ˆbLS 0 ˆaLS 0 p∗ 0 (θ0) = (1−α)  ˆbLS 1 ˆaLS 1 pLS 1 − ˆbLS 0 ˆaLS 0 pLS 0 ! .(46)
If
ˆbLS 1
ˆaLS 1 p∗ 1 (θ1)− ˆbLS 0 ˆaLS 0 p∗ 0 (θ0)<(1−α)  ˆbLS 1 ˆaLS 1 pLS 1 − ˆbLS 0 ˆaLS 0 pLS 0  , eitherp ∗ 1 (θ1)> pLS 1 orp ∗ 0 (θ0)< pLS 0 . Without loss
of generality, supposep ∗ 0 (θ0)< pLS 0 . sincep ∗ 0(θ) is continuous with respect to theta, there existsξ 1 ∈
(0,1], such that
ˆbLS 1
ˆaLS 1 p∗ 1 (θ1)− ˆbLS 0 ˆaLS 0 p∗ 0  ξ1θFEO 0 + (1−ξ 1)θ LS 0  <(1−α)  ˆbLS 1 ˆaLS 1 pLS 1 − ˆbLS 0 ˆaLS 0 pLS 0  . Therefore, (ξ1θFEO 0 +
(1−ξ 1)θ LS 0 , θFEO 1 ) is a feasible solution to (40) with strictly smaller objective value, which contradicts to the
definition of (θ FEO 0 , θFEO 1 ).
Then the optimal solution to problem (45) is the same as the optimal solution to
min
θ0,θ1

θ0 −θ LS 0 T M0  θ0 −θ LS 0  +  θ1 −θ LS 1 T M1  θ1 −θ LS 1 
s.t.
ˆbLS 1
ˆaLS 1 p∗ 1 (θ1)− ˆbLS 0 ˆaLS 0 p∗ 0 (θ0) = (1−α)  ˆbLS 1 ˆaLS 1 pLS 1 − ˆbLS 0 ˆaLS 0 pLS 0 ! . (47)
The KKT conditions of problem (47) with LagrangianL(θ 0, θ1, λ) =

θ0 −θ LS 0 T M0  θ0 −θ LS 0  +
θ1 −θ LS 1 T M1  θ1 −θ LS 1  +λ  ˆbLS 1 ˆaLS 1 p∗ 1 (θ1)− ˆbLS 0 ˆaLS 0 p∗ 0 (θ0)−(1−α)  ˆbLS 1 ˆaLS 1 pLS 1 − ˆbLS 0 ˆaLS 0 pLS 0  are
∂L
∂θ0
= 2M0

θ0 −θ LS 0  −λ ˆbLS 0 ˆaLS 0
" 1
2ˆb0
− ˆa0
2ˆb2 0
#
= 0,(48a)
∂L
∂θ1
= 2M1

θ1 −θ LS 1  +λ ˆbLS 1 ˆaLS 1
" 1
2ˆb1
− ˆa1
2ˆb2 1
#
= 0,(48b)
λ
 ˆbLS 1
ˆaLS 1 p∗ 1 (θ1)− ˆbLS 0 ˆaLS 0 p∗ 0 (θ0)−(1−α)  ˆbLS 1 ˆaLS 1 pLS 1 − ˆbLS 0 ˆaLS 0 pLS 0 !! = 0.
Differentiate (48a) and (48b) with respect toα, we have
2M0∇αθ0 − dλ dα ˆbLS 0 ˆaLS 0
" 1
2ˆb0
− ˆa0
2ˆb2 0
#
−λ
ˆbLS 0
ˆaLS 0 ∇α
 " 1
2ˆb0
− ˆa0
2ˆb2 0
#!
= 0,
2M1∇αθ1 + dλ dα ˆbLS 1 ˆaLS 1
" 1
2ˆb1
− ˆa1
2ˆb2 1
#
+λ
ˆbLS 1
ˆaLS 1 ∇α
 " 1
2ˆb1
− ˆa1
2ˆb2 1
#!
= 0.
Whenα= 0, we haveλ= 0. Therefore,
∇αθ0|α=0 = 1 2 ˆbLS 0 ˆaLS 0 M −1 0 q0 dλ dα

 α=0 ,
∇αθ1|α=0 =− 1 2 ˆbLS 1 ˆaLS 1 M −1 1 q1 dλ dα

 α=0 .
On the other hand, differentiate both sides of (46) with respect toαand setα= 0, we have
ˆbLS 1
ˆaLS 1 qT 1 ∇αθ1|α=0 − ˆbLS 0 ˆaLS 0 qT 0 ∇αθ0|α=0 =−  ˆbLS 1 ˆaLS 1 pLS 1 − ˆbLS 0 ˆaLS 0 pLS 0 ! .
Replace∇ αθ0|α=0 and∇ αθ1|α=0 by 1 2 ˆbLS 0 ˆaLS 0 M −1 0 q0 dλ dα

 α=0 and− 1 2 ˆbLS 1 ˆaLS 1 M −1 1 q1 dλ dα

 α=0, we have
1
2
  ˆbLS 1
ˆaLS 1
!2
qT 1 M T 1 q1 +
 ˆbLS 0
ˆaLS 0
!2
qT 0 M0q0
!
dλ
dα

α=0
=
ˆbLS 1
ˆaLS 1 pLS 1 − ˆbLS 0 ˆaLS 0 pLS 0 .

Elmachtoub, Kim, and T an:Learning Fair Demand Models17
Hence,
dλ
dα

α=0
=
2
 ˆbLS 1
ˆaLS 1 pLS 1 − ˆbLS 0 ˆaLS 0 pLS 0   ˆbLS 1
ˆaLS 1
2
qT 1 M T 1 q1 +  ˆbLS 0 ˆaLS 0 2 qT 0 M0q0 ,
and
dp∗ 0  θFEO 0 
dα

α=0
=q T 0 ∇αθ0|α=0 =
ˆbLS 0
ˆaLS 0 qT 0 M0q0  ˆbLS 1
ˆaLS 1
2
qT 1 M T 1 q1 +  ˆbLS 0 ˆaLS 0 2 qT 0 M0q0
 ˆbLS 1
ˆaLS 1 pLS 1 − ˆbLS 0 ˆaLS 0 pLS 0
!
=
ˆbLS 0
ˆaLS 0 qT 0 M0q0  ˆbLS 1
ˆaLS 1
2
qT 1 M T 1 q1 +  ˆbLS 0 ˆaLS 0 2 qT 0 M0q0
c
2
 ˆbLS 1
ˆaLS 1 −
ˆbLS 0
ˆaLS 0
!
.
On the other hand, for EFO with parity-wise demand fairness constraints,
dpEFO 0
dα

α=0
= c 2
ˆaLS 0 ˆaLS 1
ˆbLS 0 −
ˆaLS2 1
ˆbLS 1
ˆaLS2 0
ˆbLS 0 +
ˆaLS2 1
ˆbLS 1
,
so
dp∗ 0  θFEO 0 
dα

α=0
< dpEFO 0
dα

α=0
⇔
ˆbLS 0
ˆaLS 0 qT 0 M0q0  ˆbLS 1
ˆaLS 1
2
qT 1 M T 1 q1 +  ˆbLS 0 ˆaLS 0 2 qT 0 M0q0
c
2
 ˆbLS 1
ˆaLS 1 −
ˆbLS 0
ˆaLS 0
!
< c 2
ˆaLS 0 ˆaLS 1
ˆbLS 0 −
ˆaLS2 1
ˆbLS 1
ˆaLS2 0
ˆbLS 0 +
ˆaLS2 1
ˆbLS 1
⇔q T 0 M −1 0 q0ˆbLS 0 < qT 1 M −1 1 q1ˆbLS 1 .
Therefore, ifq T 0 M −1 0 q0ˆbLS 0 < qT 1 M −1 1 q1ˆbLS 1 , there existsξ >0 such that when 0< α < ξ, FEO leads to lower
prices than EFO and hence FEO gives higher consumer surplus and social welfare. Similarly, ifqT 0 M −1 0 q0ˆbLS 0 >
qT 1 M −1 1 q1ˆbLS 1 , dp∗ 0(θFEO 0 ) dα |α=0 > dpEFO 0 dα |α=0, then FEO leads to higher prices than EFO and gives lower con-
sumer surplus and social welfare.□
Proof of Proposition 6.To prove that (6) can be solved as a convex optimization problem under the
linear demand model, it suffices to transform the constraints into standard form, since the loss, least square
error, in the objective is already convex.
Forprice fairnessconstraints, we have
− ˆa⊤x(i)
2ˆb⊤x(i)
+ c 2 ≤˜α,
where ˜αdenotes (1−α)¯p+αp . This can be rewritten as
ˆa⊤x(i) + (2 ˜α−c)  ˆb⊤x(i)  ≤0.
The left-hand side is affine in ˆaand ˆb, and therefore this is a convex constraint. Consequently, the overall
problem can be written as a convex optimization problem.
Fordemand fairnessconstraints, we have

ˆaLS⊤ x(i) + ˆbLS

− ˆa⊤x(i)
2ˆb⊤x(i)
+ c 2  ≥˜α,
which is equivalent to,

2

ˆaLS⊤ x(i) +c ˆbLS −2 ˜α   ˆb⊤x(i)  − ˆbLS  ˆa⊤x(i) ≤0,
where the left-hand side is affine in ˆaand ˆb. Therefore, the overall problem is formulated as a convex
optimization problem. □

18 Elmachtoub, Kim, and T an:Learning Fair Demand Models
Proof of Proposition 7.Similar to the proof of Proposition 6, the proof of Proposition 7 relies on refor-
mulating the constraints in standard form. Since the cross-entropy loss in the objective is already convex, it
suffices to show that the constraints can be expressed linearly.
Forprice fairnessconstraints, we have
1 +W0

exp

ˆa⊤x(i) + ˆbc−1  + ˜αb≤0,(49)
whereW 0(·) denotes the principal branch of the Lambert–W function and ˜α= (1−α)¯p+αp −c. More
specifically, the (multi-valued) Lambert–W functionW(z) is defined as the solution toW(z)e W(z) =z. When
z >0, the function admits a unique real solutionW 0(z)>0. In our case, sincez= exp

a⊤xi + ˆbc−1  >0,
we focus on the principal branchW 0.
In addition, by implicit differentiation, we have
z(1 +W 0(z)) dW0(z) dz =W 0(z).
As a consequence, this gets the following formula for the derivative ofW 0(z), dW0(z) dz = W0(z) z(1+W0(z)) . Then,
dW0(ex)
dx =e x dW0(ex) dex = W0(ex) 1 +W0(ex) ,
d2W0(ex)
dx2 = 1 (1 +W0 (ex))2

W0(ex)− W0(ex)2
1 +W0(ex)

>0.
Therefore,W 0(ex) is a convex function. Since ˆa⊤x(i) +ˆb−1 is affine in (ˆa,ˆb), it follows from the composition
rule thatW 0

exp

ˆa⊤x(i) + ˆbc−1  is also convex. Furthermore, since 1 + ˜αˆbis affine (and hence convex),
the sum of two convex functions is convex. Therefore, the left-hand side of (49) is convex.
In conclusion, the Rawlsian price fairness constraint can be expressed in convex form, and thus the overall
problem can be reformulated as a convex optimization problem.
Similarly, we only need to verify that thedemand fairnessconstraints can be cast into standard convex
form. In particular, the demand fairness constraints take the form
1
1 + exp

−

(ˆaCE )⊤x(i) + ˆbCEpCE∗(x(i); ˆa,ˆb)
 ≥˜α⇔exp

−

(ˆaCE )⊤x(i) + ˆbCEp∗

≤ 1−˜α ˜α ,
where ˜α= (1−α) ¯d+αd . Take the logarithm of both sides, we have
−(ˆaCE )⊤x(i) − ˆbCE


1 +W0

exp

ˆa⊤x(i) + ˆbc−1 
−ˆb +c

 ≤ln
 1−˜α
˜α

,
which is equivalent to
1 +W0

exp

ˆa⊤x(i) + ˆbc−1  − 1 ˆbCE  (ˆaCE)⊤x(i) + ln  1−˜α ˜α  ˆb−c ˆb≤0.
From price fairness, we know thatW 0

exp

ˆa⊤x(i) + ˆbc−1  is a convex function. The remaining term,
1− 1 ˆbCE

(ˆaCE)⊤x(i) + ln  1−˜α ˜α   ˆbis affine in ˆb. Since the sum of a convex function and an affine function is
convex, the left-hand side of the constraint is convex. In conclusion, the optimization from with Rawlsian
access fairness can be reformulated as a convex optimization problem.□

Elmachtoub, Kim, and T an:Learning Fair Demand Models19
B. Numerical Results
B.1. Synthetic Data Generation
To evaluate our framework in a controlled environment, we construct a synthetic dataset in which both the
correlation between features and group labels, as well as the demand function, can be explicitly parameter-
ized.
We consider a binary group label, i.e.,g∈ {0,1}, drawn independently from a Bernoulli distribution with
parameterθ g. For the numerical experiments, we setm= 1 and, for simplicity, denotex i1 asxanda(resp.
b) as (a0, a1) (resp. (b0, b1)). We then generate a continuous featurexthat is correlated with the group label
gat a pre-specified point-biserial correlation coefficientρ∈[0,1]. Formally, define the standardized group
variable
z= g−θ gp
θg(1−θ g)
.
Then we construct
x=σ X

ρ z+
p
1−ρ 2 ε  +κ,
whereεis independent ofg, withE[ε] = 0 andV ar(ε) = 1. The constantκis a location parameter that
can be chosen freely to shift the support ofx(e.g., to ensurex >0). By construction,V ar(x) =σ 2 X and
Corr(x, g) =ρ(Refer to Lemma 1 provided at the end of this section.). For instance, if we setρ= 1,
σX =
p
θg(1−θ g), andκ=θ g, thenx=g.
This simulation design allows us to flexibly control (1) the marginal distribution of the group label,
(2) the correlation between features and group identity, and (3) the sensitivity of valuations to observed
characteristics. In this paper, we setρ= 0.5, which represents a practically relevant case: features are typically
correlated with demographic attributes that are sometimes legally protected (e.g., gender), but the correlation
is neither perfect nor zero.
Lemma 1.Letg∈ {0,1}be drawn from a Bernoulli distribution with parameterθ g, and definez=
g−θg√
θg (1−θg )
. Letεis independent ofg, withE[ε] = 0andVar(ε) = 1, and definex=σ X

ρz+ √1−ρ 2 ε  +κ.
ThenVar(x) =σ 2 X andCorr(x, g) =ρ.
Proof.Sinceg∼Bernoulli(θ g), we haveE[g] =θ g and Var(g) =θ g(1−θ g). Therefore, Var(z) = 1. By
independence ofzandε,
Var(x) =σ 2 X  ρ2 Var(z) + (1−ρ 2) Var(ε)  =σ 2 X (ρ2 + 1−ρ 2) =σ 2 X .
Next, sinceE[z] = 0 andE[εz] = 0, we have:
Cov(x, z) =E
h
σX (ρz+
p
1−ρ 2ε) +κ

z
i
−E[x]E[z]
=σ X ρE[z2] +σX p 1−ρ 2E[εz] +κE[z]
=σ X ρE[z2] =σ X ρ  Var(z) +E[z] 2 =σ X ρ.
Thus,
Corr(x, z) = Cov(x, z)p
Var(x)
p
Var(z)
= σX ρ σX ·1 =ρ.
Sincezis a standardized linear transformation ofg, we also haveCorr(x, g) =ρ.□

20 Elmachtoub, Kim, and T an:Learning Fair Demand Models
B.2. Heuristic Solution for Parity-wise F airness
If the demand function isd=a ⊤xi +b gpi, then parity-wise price and demand fairness can be solved by a
one-dimensional parameter search with convex optimization subproblems. The original problem is
ℓ(w, α) := min
ˆa,ˆb0≤0, ˆb1≤0
X
g∈{0,1}
1
ng
X
{i|gi=g}

ˆa⊤xi + ˆbgpi 2
s.t.

 1 n1 X {i|gi=1} ˆa⊤xi (−2ˆb1) − 1 n0 X {i|gi=0} ˆa⊤xi (−2ˆb0)

 ≤(1−α)∆.
The terms ˆa⊤xi
2ˆb0 and ˆa⊤xi 2ˆb1 induce non-convexity. We can rewrite the constraint as

 1 n1 X {i|gi=1} ˆa⊤xi (−2ˆb1) − 1 n0 X {i|gi=0} ˆa⊤xi (−2ˆb0)

 ≤(1−α)∆
⇔ ˆa⊤ ¯x1
(−2ˆb1) − ˆa⊤ ¯x0 (−2ˆb0) ≤(1−α)∆ and ˆa⊤ ¯x0 (−2ˆb0) − ˆa⊤ ¯x1 (−2ˆb1) ≤(1−α)∆
⇔ˆa⊤ ¯x1 −(−2 ˆb1) ˆa⊤ ¯x0
(−2ˆb0) ≤(1−α)∆(−2 ˆb1),
(−2ˆb1) ˆa⊤ ¯x0
(−2ˆb0) −ˆa⊤ ¯x1 ≤(1−α)∆(−2 ˆb1),
where ¯xg = 1 ng P {i|gi=g} xi. Now, introduce the parameterw= ˆa⊤ ¯x0 (−2ˆb0) . Then the subproblems take the form
ℓ(w, α) := min
ˆa,ˆb0≤0, ˆb1≤0
X
g∈{0,1}
1
ng
X
{i|gi=g}

ˆa⊤xi + ˆbgpi 2
s.t. ˆa ⊤ ¯x1 −(−2 ˆb1)w≤(1−α)∆(−2 ˆb1),
(−2ˆb1)w−ˆa⊤ ¯x1 ≤(1−α)∆(−2 ˆb1),
ˆa⊤ ¯x0 ≤w(−2 ˆb0),
ˆa⊤ ¯x0 ≥w(−2 ˆb0).
(50)
This problem is convex for each fixedwandα. Since we replace ˆa⊤ ¯x0
(−2ˆb0) (which corresponds to the optimal
price minus c 2 ) byw, the feasible range ofwlies between c 2 and the price cap minus c 2 .
C. Case Study
In Appendix C.1 and Appendix C.2, we consider estimation using a linear demand model, when the true
demand model is well-specified and mis-specified. Similar to Section 5.2, we set a normalized unit cost to
0.05 (corresponding to 50 SEK without normalization), and a normalized price cap to 1.2 (corresponding
to 1200 SEK without normalization). For Rawlsian fairness, we set ¯p(resp.p ) in (9) as the highest (resp.
lowest) optimal price obtained on the training set using parameters estimated without fairness constraints.
We set ¯das 0.5 andd as the lowest demand observed in the training set without fairness constraints.
C.1. Linear Demand Estimation with Linear T rue Demand
We examine a linear demand setting under the assumption that the true demand model is also linear.
First, Table 11 illustrates the variations in profit, consumer surplus, and social welfare asαincreases. We
observe that whenα= 0.4 and 0.6, the profit, consumer surplus, and social welfare are all lower than those

Elmachtoub, Kim, and T an:Learning Fair Demand Models21
Algorithm 1Grid Search overwwith Convex Optimization Subproblems
Require:Step sizeδ, fairness parameterα
1:Initializeℓ ∗ ←+∞
2:foreachw∈
 c
2 , c 2 +δ, . . . , pcap − c 2  do
3:Solve (50)
4:ifℓ(w, α)< ℓ ∗ then
5:ℓ ∗ ←ℓ(w, α)
6:(ˆa, ˆb0, ˆb1)←

ˆa(w, α),ˆb0(w, α),ˆb1(w, α)

7:end if
8:end for
9:returnˆa, ˆb0, ˆb1
Table 11 Normalized performance measures acrossαunder parity-wise loss fairness (%)
α
Measure 0.2 0.4 0.6 0.8 1.0
R(α)/R(0) 100.19 99.68 99.45 99.31 99.20
S(α)/S(0) 98.00 98.48 99.38 100.29 101.15
W(α)/W(0) 99.41 99.26 99.43 99.66 99.90
achieved without fairness constraints, suggesting that imposing parity-wise loss fairness may lead to negative
outcomes.
Figure 13 illustrates the outcomes under parity-wise price fairness. Similar to Section 5.2, whenα= 1,
the average prices of two groups become the same only for EFO due to the generalization error of FEO.
Consistent with the implication of Corollary 2, Table 12 shows that FEO yields higher consumer surplus
and social welfare. More specifically, accepting 1.13% greater profit loss under FEO unlocks an 8.34% higher
gain in consumer surplus than EFO under perfect fairness (i.e.,α= 1). Thus, using FEO under parity-wise
price fairness will be more beneficial to customers.
Figure 13 Price distributions for FEO and EFO under parity-wise price fairness
0.0 0.2 0.4 0.6 0.8 1.0
0.4
0.5
0.6
0.7
0.8
0.9
1.0
1.1
p0 p1 Mean
(a) Price (FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.4
0.5
0.6
0.7
0.8
0.9
1.0
1.1
p0 p1 Mean (b) Price (EFO)

22 Elmachtoub, Kim, and T an:Learning Fair Demand Models
Table 12 Normalized performance measures for FEO and EFO under parity-wise price fairness (%)
FEO (α) EFO (α)
Measure 0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0
R(α)/R(0) 99.73 99.53 99.26 98.94 98.58 99.96 99.92 99.86 99.79 99.71
S(α)/S(0) 101.97 104.14 106.02 107.59 108.83 100.08 100.17 100.28 100.39 100.51
W(α)/W(0) 100.53 101.17 101.66 102.01 102.22 100.01 100.01 100.01 100.00 100.00
Figure 14 presents the results of parity-wise demand fairness. Similar to Section 5.2, due to the estimation
error, the estimated demand function differs from the true demand model. As a result, there exists a dis-
crepancy between the ex-ante and ex-post demand under both EFO and FEO, and a small ex-ante demand
gap may not accurately reflect the true demand gap, which is different from logistic demand estimation.
Consequently, the ex-post demand does not change significantly for both FEO and EFO, and Table 13 shows
that imposing parity-wise demand fairness on ex-ante demand does not lead to substantial changes in profit,
consumer surplus, or social welfare. This suggests that implementing parity-wise demand fairness in practice
may be challenging.
Figure 14 Demand distributions for FEO and EFO under parity-wise demand fairness
0.0 0.2 0.4 0.6 0.8 1.0
0.470
0.475
0.480
0.485
0.490
d0 d1 Mean
(a) Ex Ante Demand (FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.470
0.475
0.480
0.485
0.490
d0 d1 Mean (b) Ex Ante Demand (EFO)
0.0 0.2 0.4 0.6 0.8 1.0
0.3
0.4
0.5
0.6
0.7
d0 d1 Mean
(c) Ex Post Demand (FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.3
0.4
0.5
0.6
0.7
d0 d1 Mean (d) Ex Post Demand (EFO)
Figure 15 illustrates the price distribution under Rawlsian price fairness. In both FEO and EFO settings,
the maximum price declines monotonically withα, effectively curbing extreme price points. In Table 14,
while the profit difference between the two remains marginal, FEO consistently delivers better consumer
surplus and social welfare, particularly up toα= 0.6, the threshold before the distribution collapses into a

Elmachtoub, Kim, and T an:Learning Fair Demand Models23
Table 13 Normalized performance measures for FEO and EFO under parity-wise demand fairness (%)
FEO (α) EFO (α)
Measure 0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0
R(α)/R(0) 100.01 100.02 100.04 100.05 100.06 100.0 100.0 100.0 100.01 100.01
S(α)/S(0) 99.95 99.89 99.84 99.78 99.73 100.0 100.0 100.0 99.99 99.99
W(α)/W(0) 99.99 99.98 99.97 99.95 99.94 100.0 100.0 100.0 100.00 100.00
few discrete points (See Figure 15). This performance gap stems from FEO’s ability to reshape the entire
price distribution, whereas EFO merely imposes a cap on high-end prices. Therefore, FEO is an effective
path for firms prioritizing consumer surplus with a slight profit trade-off. This is especially true at moderate
αlevels, where the approach curbs extreme pricing while retaining the benefits of personalization. Similar
to Section 5.2, when we impose Rawlsian price fairness for FEO at fairness levelα= 0.2, profit, consumer
surplus and social welfare are all higher than the baseline (i.e.,α= 0), showing that a small level of Rawlsian
price fairness for FEO can lead to a win-win outcome.
Figure 15 Price distributions for FEO and EFO under Rawlsian price fairness
0.0 0.2 0.4 0.6 0.8 1.0
0.4
0.6
0.8
1.0
(a) Price under FEO
0.0 0.2 0.4 0.6 0.8 1.0
0.4
0.6
0.8
1.0
 (b) Price under EFO
Table 14 Normalized performance measures for FEO and EFO under Rawlsian price fairness (%)
FEO (α) EFO (α)
Measure 0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0
R(α)/R(0) 100.01 99.70 98.61 95.61 81.14 99.99 99.93 99.61 96.01 81.13
S(α)/S(0) 102.70 108.27 116.41 130.20 191.43 100.05 101.02 105.55 130.61 191.57
W(α)/W(0) 100.97 102.74 104.94 107.91 120.35 100.01 100.32 101.72 108.31 120.38
Lastly, Figure 16 illustrates the resulting demand distribution under Rawlsian fairness. Asαincreases,
the minimum ex-ante and ex-post demand rises under both FEO and EFO, ensuring that no individual
faces a demand level below a certain threshold. Moreover, the minimum ex-post demand also increases for
both FEO and EFO, showing that imposing Rawlsian demand fairness indeed benefits individuals with low

24 Elmachtoub, Kim, and T an:Learning Fair Demand Models
demand. Table 15 shows that profit, consumer surplus, and social welfare are closely aligned between the two
settings. For instance, atα= 1, both settings yield similar trade-offs: FEO (resp. EFO) incurs a marginal
profit loss of 0.53% (resp. 0.31%) to achieve a relatively substantial increase in consumer surplus of 9.95%
(resp. 8.10%).
Figure 16 Demand distributions for FEO and EFO under Rawlsian demand fairness
0.0 0.2 0.4 0.6 0.8 1.0
0.47
0.48
0.49
0.50
0.51
(a) Ex Ante Demand
(FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.47
0.48
0.49
0.50
0.51
(b) Ex Ante Demand
(EFO)
0.0 0.2 0.4 0.6 0.8 1.0
0.3
0.4
0.5
0.6
0.7
(c) Ex Post Demand
(FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.3
0.4
0.5
0.6
0.7
(d) Ex Post Demand
(EFO)
Table 15 Normalized performance measures for FEO and EFO under Rawlsian demand fairness (%)
FEO (α) EFO (α)
Measure 0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0
R(α)/R(0) 99.97 99.94 99.85 99.73 99.57 100.00 99.99 99.92 99.82 99.69
S(α)/S(0) 100.09 102.13 104.60 107.22 109.95 100.02 100.58 102.71 105.38 108.10
W(α)/W(0) 100.01 100.72 101.54 102.39 103.26 100.01 100.20 100.91 101.80 102.68
C.2. Linear Demand Estimation with Logistic T rue Demand
This case considers a linear demand setting while assuming that the true underlying demand model follows
a logistic form. Under parity-wise loss fairness, Table 16 indicates that firm profit increases, whereas both
consumer surplus and social welfare decrease. These results suggest that, in this setting, the imposition of
loss fairness may lead to outcomes that are detrimental to consumers, thereby deviating from the normative
objective typically associated with fairness considerations. Moreover, comparison with Table 11 highlights
that the effects of loss fairness on performance measures are setting-dependent and cannot be characterized
uniformly across different model specifications.
Table 16 Normalized performance measures acrossαunder parity-wise loss fairness (%)
α
Measure 0.2 0.4 0.6 0.8 1.0
ˆR(α)/ ˆR(0) 100.65 100.99 101.24 101.45 101.65
ˆS(α)/ ˆS(0) 99.16 98.69 98.35 98.07 97.76
ˆW(α)/ ˆW(0) 99.78 99.64 99.55 99.47 99.37

Elmachtoub, Kim, and T an:Learning Fair Demand Models25
Figure 17 and Table 17 report the results under parity-wise price fairness. Although the true demand
model is logistic, the qualitative insights remain consistent with those obtained under linear demand. In
particular, FEO achieves higher consumer surplus and social welfare than EFO. Furthermore, under perfect
fairness (i.e.,α= 1), accepting an additional 3.08% reduction in profit under FEO results in a 3.97% greater
increase in consumer surplus relative to EFO. These findings suggest that, under parity-wise price fairness,
FEO provides more favorable outcomes for consumers.
Figure 17 Price distributions for FEO and EFO under parity-wise price fairness
0.0 0.2 0.4 0.6 0.8 1.0
0.4
0.5
0.6
0.7
0.8
0.9
1.0
1.1
p0 p1 Mean
(a) Price (FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.4
0.5
0.6
0.7
0.8
0.9
1.0
1.1
p0 p1 Mean (b) Price (EFO)
Table 17 Normalized performance measures for FEO and EFO under parity-wise price fairness (%)
FEO (α) EFO (α)
Measure 0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0
R(α)/R(0) 99.25 98.46 97.69 97.00 96.42 99.92 99.83 99.73 99.62 99.50
S(α)/S(0) 100.98 102.08 103.07 103.93 104.57 100.11 100.23 100.35 100.47 100.60
W(α)/W(0) 100.27 100.58 100.85 101.06 101.20 100.03 100.07 100.09 100.12 100.15
Figure 18 illustrates the demand distributions under parity-wise demand fairness. Here, only the ex-ante
demand from EFO satisfies demand fairness, while the others do not. This is mainly because the true linear
demand function differs from the estimated demand model. Table 18 summarizes the outcomes under parity-
wise demand fairness. Consistent with the case in which the true demand model is linear, the changes in
profit, consumer surplus, and social welfare are relatively small. An interesting observation, however, is that
both FEO and EFO exhibit slight increases in profit. This arises from the mismatch between the true and
estimated demand functions, where the fairness constraint acts as a form of regularization.
Figure 19 shows the price distributions under Rawlsian price fairness. Similar to the other cases in Sec-
tion 5.2 and Section C.1, FEO reduces the spread of the price distribution. Table 19 shows that, consistent
with the case of a true linear demand model, FEO achieves higher consumer surplus and social welfare. An
interesting observation is that, as in the setting with a linear estimated demand function, the differences in
profit, consumer surplus, and social welfare are most pronounced at intermediate values ofα, rather than
at extreme cases such asα= 1. This is because, whenα= 1, prices become nearly static, thereby limiting
variation in outcomes across framework.

26 Elmachtoub, Kim, and T an:Learning Fair Demand Models
Figure 18 Demand distributions for FEO and EFO under parity-wise demand fairness
0.0 0.2 0.4 0.6 0.8 1.0
0.465
0.470
0.475
0.480
0.485
0.490
0.495
d0 d1 Mean
(a) Ex Ante Demand (FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.465
0.470
0.475
0.480
0.485
0.490
0.495
d0 d1 Mean (b) Ex Ante Demand (EFO)
0.0 0.2 0.4 0.6 0.8 1.0
0.2
0.3
0.4
0.5
0.6
0.7
d0 d1 Mean
(c) Ex Post Demand (FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.2
0.3
0.4
0.5
0.6
0.7
d0 d1 Mean (d) Ex Post Demand (EFO)
Table 18 Normalized performance measures for FEO and EFO under parity-wise demand fairness (%)
FEO (α) EFO (α)
Measure 0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0
R(α)/R(0) 100.03 100.04 100.07 100.09 100.11 100.00 100.00 100.01 100.01 100.01
S(α)/S(0) 99.97 99.95 99.92 99.89 99.87 100.00 99.99 99.99 99.99 99.99
W(α)/W(0) 99.99 99.99 99.98 99.98 99.97 100.00 100.00 100.00 100.00 100.00
Figure 19 Price distributions for FEO and EFO under Rawlsian price fairness
0.0 0.2 0.4 0.6 0.8 1.0
0.4
0.6
0.8
1.0
(a) Price under FEO
0.0 0.2 0.4 0.6 0.8 1.0
0.4
0.6
0.8
1.0
 (b) Price under EFO
Lastly, Figure 20 illustrates how ex-ante and ex-post demand change under FEO and EFO. Similar to
the case in Section C.1, the ex post demand changes less under EFO than under FEO. Table 20 shows
the effects of Rawlsian demand fairness on profit, consumer surplus, and social welfare. Consistent with the

Elmachtoub, Kim, and T an:Learning Fair Demand Models27
Table 19 Normalized performance measures for FEO and EFO under Rawlsian price fairness (%)
FEO (α) EFO (α)
Measure 0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0
R(α)/R(0) 98.59 96.54 93.30 87.60 67.65 99.98 99.54 97.02 88.53 67.65
S(α)/S(0) 102.22 105.05 108.96 115.11 135.26 100.06 100.86 104.42 114.25 135.26
W(α)/W(0) 100.72 101.53 102.48 103.73 107.30 100.03 100.31 101.36 103.61 107.30
case of a true linear demand model, FEO and EFO yield broadly similar results. When comparing the two,
FEO entails a slightly larger reduction in profit, but achieves higher consumer surplus and social welfare.
This pattern is also generally observed under Rawlsian price fairness and in the true linear demand setting.
Overall, these results suggest that Rawlsian fairness with feature-based implementation favors consumers
when using FEO, whereas EFO may be preferred when the objective is to mitigate profit losses.
Figure 20 Demand distributions for FEO and EFO under Rawlsian demand fairness
0.0 0.2 0.4 0.6 0.8 1.0
0.47
0.48
0.49
0.50
0.51
(a) Ex Ante Demand
(FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.47
0.48
0.49
0.50
0.51
(b) Ex Ante Demand
(EFO)
0.0 0.2 0.4 0.6 0.8 1.0
0.2
0.3
0.4
0.5
0.6
0.7
(c) Ex Post Demand
(FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.2
0.3
0.4
0.5
0.6
0.7
(d) Ex Post Demand
(EFO)
Table 20 Normalized performance measures for FEO and EFO under Rawlsian demand fairness (%)
FEO (α) EFO (α)
Measure 0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0
R(α)/R(0) 99.66 99.17 98.63 97.93 97.14 99.98 99.80 99.26 98.52 97.74
S(α)/S(0) 100.50 101.19 101.94 102.90 104.00 100.02 100.26 100.98 102.04 103.14
W(α)/W(0) 100.15 100.35 100.57 100.84 101.16 100.01 100.07 100.27 100.59 100.91
C.3. Logistic Demand Estimation with Linear T rue Demand
We consider a mis-specified setting where we assume the true demand function is linear but the decision
maker uses a logistic demand model for estimation. In this case, both FEO and EFO suffer from the error
in estimation.
Table 21 presents the results under parity-wise loss fairness. When increasingα, profit first increases then
decreases, whereas consumer surplus and social welfare keep decreasing, which is different from Table 6,
Table 11 and Table 16. Taken together, these findings indicate that parity-wise loss fairness does not nec-
essarily lead to desirable downstream social outcomes and may not align with the fairness objectives of
policymakers, sellers, and customers.

28 Elmachtoub, Kim, and T an:Learning Fair Demand Models
Table 21 Normalized performance measures acrossαunder parity-wise loss fairness (%)
α
Measure 0.2 0.4 0.6 0.8 1.0
R(α)/R(0) 101.12 101.95 102.39 102.47 102.30
S(α)/S(0) 95.98 92.35 89.73 88.30 88.04
W(α)/W(0) 98.95 97.89 97.04 96.49 96.26
Figure 21 presents the price distributions under parity-wise price fairness. In the setting where the true
demand model is not included in the hypothesis class, parity-wise price fairness remains achievable because
price is the directly controllable decision variable. However, due to model mis-specification, the resulting
pricing decisions lead to worse downstream outcomes. As shown in Table 22, profit, consumer surplus, and
social welfare all decrease under EFO. This differs from the results in Cohen et al. (2022), where consumer
surplus and social welfare initially increase when the true demand model is known.
Figure 21 Price distributions for FEO and EFO under parity-wise price fairness
0.0 0.2 0.4 0.6 0.8 1.0
0.35
0.40
0.45
0.50
0.55
0.60
0.65
0.70
p0 p1 Mean
(a) Price (FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.35
0.40
0.45
0.50
0.55
0.60
0.65
0.70
p0 p1 Mean (b) Price (EFO)
Table 22 Normalized performance measures for FEO and EFO under parity-wise price fairness (%)
FEO (α) EFO (α)
Measure 0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0
R(α)/R(0) 99.72 99.44 99.07 98.76 98.43 99.99 99.98 99.95 99.93 99.89
S(α)/S(0) 101.18 102.21 103.49 104.49 105.41 99.98 99.97 99.95 99.92 99.89
W(α)/W(0) 100.34 100.61 100.94 101.18 101.38 99.99 99.97 99.95 99.93 99.89
Figure 22 illustrates the demand distributions under parity-wise demand fairness. The decision maker only
has access to the estimated demand function, so they can only control the ex-ante demand gaps between two
groups. However, the ex-post demand gaps even become larger for FEO and EFO whenα= 1.0. Table 23
shows that for FEO, profit increases whereas consumer surplus and social welfare decrease, and for EFO
there is no significant change in this metrics. The increase in profit under FEO arises because the fairness
constraints act as a regularization term, which is consistent with Proposition 3.

Elmachtoub, Kim, and T an:Learning Fair Demand Models29
Figure 22 Demand distributions for FEO and EFO under parity-wise demand fairness
0.0 0.2 0.4 0.6 0.8 1.0
0.3
0.4
0.5
0.6
0.7
d0 d1 Mean
(a) Ex Ante Demand (FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.3
0.4
0.5
0.6
0.7
d0 d1 Mean (b) Ex Ante Demand (EFO)
0.0 0.2 0.4 0.6 0.8 1.0
0.35
0.40
0.45
0.50
0.55
0.60
0.65
0.70
d0 d1 Mean
(c) Ex Post Demand (FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.35
0.40
0.45
0.50
0.55
0.60
0.65
0.70
d0 d1 Mean (d) Ex Post Demand (EFO)
Table 23 Normalized performance measures for FEO and EFO under parity-wise demand fairness (%)
FEO (α) EFO (α)
Measure 0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0
R(α)/R(0) 100.25 100.48 100.69 100.95 101.15 100.00 100.00 99.99 99.98 99.97
S(α)/S(0) 98.86 97.69 96.45 94.89 93.46 100.01 100.03 100.04 100.06 100.08
W(α)/W(0) 99.66 99.30 98.90 98.39 97.90 100.01 100.01 100.02 100.02 100.01
Figure 23 and Table 24 present the results for Rawlsian price fairness. The change in price distributions
and downstream outcomes are similar to well-specified cases. This suggests that Rawlsian price fairness can
remain effective even when the estimated demand model is mis-specified.
Table 24 Normalized performance measures for FEO and EFO under Rawlsian price fairness (%)
FEO (α) EFO (α)
Measure 0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0
R(α)/R(0) 98.92 96.88 94.13 89.91 79.30 99.94 99.31 96.31 89.78 79.30
S(α)/S(0) 104.63 112.02 120.24 131.44 157.21 100.16 102.62 113.17 132.21 157.21
W(α)/W(0) 101.34 103.28 105.17 107.47 112.25 100.03 100.71 103.44 107.72 112.25
Figure 24 shows the results under Rawlsian demand fairness. Similar to parity-wise demand fairness,
imposing Rawlsian demand fairness constraints has a much smaller effect on ex-post demand than on ex-ante

30 Elmachtoub, Kim, and T an:Learning Fair Demand Models
Figure 23 Price distributions for FEO and EFO under Rawlsian price fairness
0.0 0.2 0.4 0.6 0.8 1.0
0.4
0.5
0.6
0.7
(a) Price under FEO
0.0 0.2 0.4 0.6 0.8 1.0
0.4
0.5
0.6
0.7
 (b) Price under EFO
demand. Under both FEO and EFO, the minimum ex-post demand increases only slightly, or even decreases
for someα. Moreover, the maximum ex-post demand increases substantially. This suggests that Rawlsian
demand fairness constraints may be imposed on the wrong population. Therefore, even though in Table 25
consumer surplus and social welfare increase for both FEO and EFO, the intended fairness objective may
still not be achieved. This leaves an open question of how to ensure demand fairness when the demand
estimation is insufficiently accurate.
Figure 24 Demand distributions for FEO and EFO under Rawlsian demand fairness
0.0 0.2 0.4 0.6 0.8 1.0
0.4
0.5
0.6
0.7
(a) Ex Ante Demand
(FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.4
0.5
0.6
0.7
(b) Ex Ante Demand
(EFO)
0.0 0.2 0.4 0.6 0.8 1.0
0.4
0.5
0.6
0.7
0.8
0.9
(c) Ex Post Demand
(FEO)
0.0 0.2 0.4 0.6 0.8 1.0
0.4
0.5
0.6
0.7
0.8
0.9
(d) Ex Post Demand
(EFO)
Table 25 Normalized performance measures for FEO and EFO under Rawlsian demand fairness (%)
FEO (α) EFO (α)
Measure 0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0
R(α)/R(0) 98.51 96.37 93.35 88.38 85.95 99.98 99.68 98.66 96.15 90.51
S(α)/S(0) 106.29 113.00 120.61 133.08 138.68 100.09 101.15 104.29 111.91 128.11
W(α)/W(0) 101.80 103.40 104.88 107.28 108.25 100.03 100.30 101.04 102.81 106.41
