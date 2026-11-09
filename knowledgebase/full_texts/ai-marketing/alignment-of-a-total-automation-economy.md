---
title: Alignment of a Total Automation Economy
url: https://arxiv.org/abs/2607.17015
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- David McAllester
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.17015
pages: 4
chars: 12207
fetched_at: '2026-11-08T13:21:05+00:00'
kb_version: 1
---

# Alignment of a Total Automation Economy

Alignment of a Total Automation Economy
David McAllester
July 22, 2026
Consumption is the end purpose of production.
Adam Smith
History is driven by economics.
Historical Materialism — Karl Marx
Government of the people, by the people, and for the people, must not perish.
Abraham Lincoln, The Gettysburg Address
Abstract
We consider economic theory from the perspective of a total automation economy, one with no
human involvement in production either in manufacturing or in management. One can naturally
ask whether a total automation economy is fundamentally a centrally planned economy or, alter-
natively, whether efficiency demands decentralization into local decisions by competing agents —
agentic production. A soviet economist, Leonid Kantorovich, developed linear programming as a
method companies or governments can use to optimize production. Ironically, he is also generally
credited with showing that the most efficient production is achieved through decentralization — a
free market economy with competing agents. Here we review Kantorovich’s dualization in detail.
We take the objective of the economy to be maximizing production weighted by (human) market
price. A fundamental issue is whether an automated pursuit of this objective might have alignment
vulnerabilities as the economy evolves. Another question is whether dualization provides insight
into the utility of agentic AI systems (multi-agent AI systems) generally.
1 Introduction
Here we consider Kantorovich’s dualization theorem [Kan39] from the perspective of a total automation
economy — one where no human is used in the production of goods and services. The statement of
the theorem assumes that the goal of industrial production is maximizing consumption weighted by
market price. One can think of market pricing as a form of democracy where people “vote” on what
is to be produced simply by purchasing what they want. The ability of the economy to respond to the
purchases of consumers can be viewed as a form of alignment of the economy with human value.
There are valid fairness issues to be address in treating purchases as reflective of social welfare.
Obviously rich people have more ”voting power” (purchasing power) than poor people. The needs of
poor people are more pressing and should perhaps be given even more weight than the needs of rich
people (instead of the reverse). Also, people in different states of health have different significance of
their needs. A final issue is that different people simply have different fundamental values perhaps
stemming from differences in their fundamental natures. Market pricing would seem to better reflect
human value if we assume that all consumers have the same universal basic income. However, here
1
arXiv:2607.17015v2  [physics.soc-ph]  21 Jul 2026

we put the fairness issues aside and simply assume a mathematical model in which the objective is to
maximize consumption weighted by price.
In this brief paper we review Kantorovich’s dualization theorem and informally consider some issues
related to it’s application. Although we present only a static optimality condition in a linear model
of production processes, in practice the economy would evolve due to advances in technology and the
production processes would be nonlinear. Control of the economy would presumably be based on some
form of gradient ascent on the objective. It seems that attention must be paid to the existence of
any possible alignment vulnerabilities. Another issue is whether dualization of an objective function
provides understanding of the general value of agentic AI systems — problem solving using a variety
of differently motivated agents.
2 Formal Set Up
The formal set up here is due to Kantorovich [Kan39], who won a Nobel Prize in economics (1975)
for formulating and analyzing this model. We assume a set ofNcommodities indexed byi. We
assumeKprocesses indexed bykand letz k be a rate at which processkruns. Each process consumes
commodities as inputs and produces commodities as outputs. For commodityiand processkwe
write In k,i for the rate commodityiis consumed by processkwhen processkruns at a unit rate.
Similarly Outk,i denotes the rate of production ofiwhenkis run at unit rate. We assume an industrial
endowment which is a supply of natural resources (for example land) and let Endowi be a rate at which
commodityiis produced as an endowment. Given a set of processes running at given ratesz k we have
a net production of ratex i for commodityigiven by
xi(z) = Endowi +
X
k
zk(Outk,i −In k,i)
We say that a set of ratesz k ≥0 is feasible if for each commodityiwe havex i(z)≥0. We cannot
consume more of commodityiin production than is made available by the endowment plus production.
A commodityiwithx i(z) = 0 will be called an internal commodity — internal commodities are used
in production but are not provided to consumers. Engines might be used in making cars but never
offered to consumers. A commodity will be called external if it is not internal (and hence offered to
consumers in a market).
We define the purpose of the the economy to be that of maximizing consumption weighted by
price. To define prices we invoke the Arrow-Debreu theorem [AD54] which implies that for a given net
productionx 1, . . . , xn there exists a market equalibrium price vectorp 1, . . . , pn such that when human
consumers are offered the commodities in quantityx 1, . . . , xn at pricesp 1, . . . , pn the market clears —
consumers buy exactly the amount produced. A fundamental issue is thatp i is not defined for internal
commodities which are not offered to consumers. This is a wrinkle in the optimization problem that
is not present in the general analysis of KKT conditions for constrained optimization. However, as
explained below, we adopt the convention thatp i = 0 for any internal commodityi.
3 A Central Planning Optimality Condition
We will work with differential changes in production ratesdz 1, . . . dzk. Differentiating the definition of
xi(z) we have
dxi =
X
k
(Outk,i −In k,i)dzk
A processkwill be called inactive ifz k = 0 and called active otherwise. For feasible production rates
zwe say that a differential update directiondz 1, . . . , dzK is feasible if for each inactice processz k we
havedz k ≥0 and for each internal commodityiwe havedx i ≥0. A feasible update direction must not
violate the feasibility restrictions onz. However a feasible update direction might convert an internal
commodity to an external commodity or vice-versa or convert an inactive process to an active process
or vice-versa.
2

Optimality: We say that a feasible setting for production ratesz 1, . . . , zk is (first order)
optimal if for any feasible update directiondz 1, . . . , dzK we have P i pidxi ≤0.
If this optimality condition fails then there exists an update condition with positive gradient of the
objective. If this first order optimality condition holds then we might still be at saddle points or even
local minima. There might also be a differential update direction that converts an internal commodity
to an external commodity and improves the objective of converting an an internal commodityi, with
pi = 0, to an external commodity with a strictly positive market value.
In practice the economy would evolve by some form of gradient ascent on the production ratesz k.
Note that the market prices are allowed to be nonlinear in the production ratesz k and therefore must
be measured repeatedly during any gradient ascent process.
4 Agents Arising from Duality
We now apply the KKT (Karush-Kuhn-Tucker) conditions on constrained optimization [KT51, Kar39].
We take the objective function to be P i pixi withp i defined on all commoditiesibut set to zero on
internal commodities. Applying the KKT conditions we introduce a Lagrange multiplierλ i ≥0 for
each constraintx i ≥0 and a Lagrange multiplierµ k ≥0 for each constraintz k ≥0. We setλ i = 0 on
external commodities andµ k = 0 on active processes.
We have that only one ofp i andλ i can be non-zero. This is not just complementary slackness and
is not a property of constrained optimization generally. In the general case of constrained optimization
the ”price vector”pis just the gradient of a fixed objective. Herepcan vary at different settings of
zas commodities switch from being internal to being external. We havedefinedp i = 0 for internal
commodities. The KKT conditions will apply to the price vector as if that vector is a well-defined
gradient of the objective.
Before applying the KKT conditions we first note that
∇zxi(z) =
X
k
(Outk,i −In k,i)δk
Here we have that∇ zxi(z) is a K-dimensional vector and (Out k,i −In k,i) is the partial derivative of
xi(z) with respect toz k — a scalar. This scalar becomes aK-dimensional vector when multiplied by
δk — the vector whosekth component is 1 and all other components are zero.
For maximizing P i pixi with constraints of the formx i(z)≥0 andz k ≥0 the KKT condition is
0 =
X
i
pi∇zxi(z) +
X
i
λi∇zxi(z) +
X
k
µkδk
=
X
k
δk

µk +
X
i
(pi +λ i)(Outk,i −In k,i)
!
The sum overkis summing over orthogonal vectors so this equation yields that for eachkwe have
µk +
X
i
(pi +λ i)(Outki −In k,i) = 0
For every active process we have thatµ k = 0 and hence all active processes must operating at zero
profit under the pricing (p i +λ i). For each inactive process we can satisfy the equation by settingµ k
provided that (p i +λ i)(Outk,i −In k,i)≤0. We now have the following localization theorem.
Kantorovich Dualization:A feasible setting of the process weightszis first order optimal
(as defined previously) if and only if there exists a ”shadow price”λ i ≥0 for each internal
commodityisuch that under the commodity pricingp+λeach active process is operating
at break-even (zero profit) and no inactive process is operating at a strictly positive profit.
The shadow pricesλ i are Kantorovich’s “objectively determined valuations” [Kan65] — imputed
prices for internal commodities supplied by the optimization itself rather than by any human consump-
tion market.
3

5 Summary
A total automation economy run by AI should serve humanity by providing what people want as
indicated by the purchases that they make. Kantorovich showed that a certain notion of centralized
optimization of industrial production (setting prices to zero for internal commodities) is essentially
equivalent to free market economics with agents pursuing profit.
Here we have discussed an optimality condition. In practice we must find some form a gradient
ascent involving states of the economy with prices, shadow process and possibly nonzero profits and
losses. A fundamental design criterion of such a gradient ascent algorithm is that it remain aligned to
the gradient of consumption weighted by price.
A independent question is under what conditions is the dual of an optimization problem usefully
viewed as defining a collection of agents. Might this explain the value of agentic AI more generally?
Acknowledgments
I would like to thank Sergiy Verstyuk and Claude AI for useful comments on this paper.
References
[AD54] Kenneth J. Arrow and Gerard Debreu. Existence of an equilibrium for a competitive economy.
Econometrica, 22(3):265–290, 1954.
[Kan39] Leonid V. Kantorovich. Mathematical methods of organizing and planning production.Man-
agement Science, 6(4):366–422, 1939. Russian original, Leningrad State University. English
translation by R. W. Campbell and W. H. Marlow inManagement Science, vol. 6, no. 4 (July
1960), pp. 366–422.
[Kan65] Leonid V. Kantorovich.The Best Use of Economic Resources. Harvard University Press,
Cambridge, MA, 1965. Translated from the 1959 Russian original; source of the “objectively
determined valuations” (shadow prices).
[Kar39] William Karush. Minima of functions of several variables with inequalities as side conditions.
Master’s thesis, Department of Mathematics, University of Chicago, Chicago, IL, 1939. M.Sc.
dissertation; origin of the “K” in the KKT conditions.
[KT51] Harold W. Kuhn and Albert W. Tucker. Nonlinear programming. In Jerzy Neyman, editor,
Proceedings of the Second Berkeley Symposium on Mathematical Statistics and Probability,
pages 481–492. University of California Press, Berkeley, CA, 1951.
4
