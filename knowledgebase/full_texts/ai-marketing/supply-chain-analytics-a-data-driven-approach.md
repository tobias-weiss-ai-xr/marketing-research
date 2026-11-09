---
title: 'Supply Chain Analytics: A Data-Driven Approach'
url: https://arxiv.org/abs/2609.10563
category: ai-marketing
subcategory: measurement
date: 2026-08
venue: ''
authors:
- Elioth Sanabria
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.10563
pages: 101
chars: 210190
fetched_at: '2026-11-08T13:27:39+00:00'
kb_version: 1
---

# Supply Chain Analytics: A Data-Driven Approach

Supply Chain Analytics: A Data-Driven Approach
Elioth Sanabria
Spring 2026
arXiv:2609.10563v1  [math.OC]  17 Aug 2026

Supply Chain Analytics: A data-driven approach2

Contents
1 Demand Estimation and F orecasting 1
1.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2 The Demand as a Random Variable . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2.1 Useful Probability Calculations . . . . . . . . . . . . . . . . . . . . . . . . 3
1.2.2 Side Information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.3 Demand Evolution over Time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.3.1 Modeling Seasonality and Time-varying Factors . . . . . . . . . . . . . . . 7
1.3.2 Other Modeling Specifications . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.4 Demand Estimation in Practice . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
1.4.1 Data-driven Demand Estimation . . . . . . . . . . . . . . . . . . . . . . . 12
2 Inventory Management Models 17
2.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.2 The Newsvendor Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.2.1 Empirical Distributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.3 Inventory Replenishment - The (s, S) rule . . . . . . . . . . . . . . . . . . . . . . 22
2.3.1 Finding the (s, S) values in the i.i.d. case . . . . . . . . . . . . . . . . . . 24
2.3.2 The time-varying demand optimal inventory . . . . . . . . . . . . . . . . . 26
3 Network F ulfilment Models 31
3.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
3.2 Warehouse consolidation and positioning . . . . . . . . . . . . . . . . . . . . . . . 31
3.2.1 Single Location Warehouse . . . . . . . . . . . . . . . . . . . . . . . . . . 33
3.2.2 Multiple Location Warehouses . . . . . . . . . . . . . . . . . . . . . . . . 36
3.3 Distributionally Robust Warehouse Location Optimization . . . . . . . . . . . . . 39
3.3.1 A reformulation using duality and optimal transport . . . . . . . . . . . . 41
4 Scheduling Models 45
4.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
4.2 A set covering problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
4.2.1 Data Uncertainty . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
4.3 Production Scheduling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
4.4 A knapsack problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
5 V ehicle Routing Problems 55
5.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
5.2 The Traveling Salesman Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
5.2.1 Incorporating Randomness and Risk Awareness . . . . . . . . . . . . . . . 59
5.3 The Vehicle Routing Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
5.3.1 On Capacities and Similar Issues . . . . . . . . . . . . . . . . . . . . . . . 61
5.3.2 Time-window constraints: Column generation . . . . . . . . . . . . . . . . 63
3

Supply Chain Analytics: A data-driven approach4
6 Systemic Demand Uncertainty and Chain Effects 67
6.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
6.2 Basic Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
6.2.1 The bullwhip effect and other sensitivities . . . . . . . . . . . . . . . . . . 69
6.2.2 Volatility Propagation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
6.3 Dynamic Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
6.3.1 Sequential dynamics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
7 Queueing Models 77
7.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
7.2 A network view of a queueing system . . . . . . . . . . . . . . . . . . . . . . . . . 77
7.3 Time-varying arrivals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
7.3.1 Time-varying arrivals with infinite servers . . . . . . . . . . . . . . . . . . 84
7.3.2 Time-varying arrivals with finite servers . . . . . . . . . . . . . . . . . . . 86
8 Optimization of Queueing Systems 91
8.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
8.2 Linear Allocation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
8.2.1 Mean-variance optimization . . . . . . . . . . . . . . . . . . . . . . . . . . 93
8.3 Accuracy and non-exponential service times . . . . . . . . . . . . . . . . . . . . . 94
8.3.1 Non-exponential service times . . . . . . . . . . . . . . . . . . . . . . . . . 96

Chapter 1
Demand Estimation and Forecasting
1.1 Introduction
Demand forecasting is an important tool to make decisions such as financial projections, capacity
planning and allocation of resources for a productive activity. The demand for any product,
service or good in the future is a random variable. That is, it is unknowable before it is
realized. The demand that already occurred is calledrealized demandor can also be called
historical demand.
In fact, only the past is really known, everything happening in the future has to be guessed.
In these lectures notes we deal with the most common practices inguessingthe future quantities
of the demand. Mathematically, it is useful to model the demand as a random variable. Random
variables are a mathematical construct to capture events and their randomness. We will cover
the basics building up the necessary knowledge to manipulate and eventually model and estimate
demand in the future.
1.2 The Demand as a Random Variable
Suppose we want to model the demand quantity once in the future (say, next week or next
month or next year). We denote this random quantity by the capital letterD. This random
variableDis in fact a function that takes as input a random mechanismωand outputs an
event, in our case a number for the demand 1. For example, the demand can be a number like
D= 14 with probabilityp 14, or it could beD= 5,000 with a probabilityp 5,000.
As normally the demand is acount(of products, goods or services) we will assume the
demand cannot take negative values. Then, we can describe the probability of any outcome
1The space of random mechanism is normally called sample space, and is denoted as the set Ω. Then, formally
the random variable is a function mappingD: Ω→Eto a set of possible eventsE.
1

Supply Chain Analytics: A data-driven approach2
of the demand by aprobability mass functionor pmf asp i =P(D=i) for all possible values
i= 0,1, . . .For the pmf to be correctly defined two things must happen: First, each outcome
must occur with a probability between 0 and 1, that is 0≤p i ≤1 and adding over all outcomes
should add up to 1, that is, P∞ i=0 pi = 1.
With this framework, we can already solve interesting questions: For example, ifDis the
quantity of semiconductor chips sold in the next quarter, we can askwhat is the probability that
the demand is at least 10 million chips?. To answer this, the event{D >10 7}is the same as
the events{D= 10 7 + 1, D= 107 + 2, ...}, then we can simply do:
P(D >107) =P(D= 10 7 + 1, D= 107 + 2, . . .) =
∞X
i=107+1
pi,(1.1)
Throughout the topic it is often useful to get used to manipulate event sets. For example,
in the previous example we exploited the fact that the event{D >10 7}can be written as the
union that the demand takes exactly each value greater than 10 7, noting that each of these
events is disjoint (it can be a value or another but not two at the same time). We could have
also taken an alternative approach by calculating the probability of thecomplementevent, that
is, that the demand is less or equal to 10 7 and then, given that the probability of all outcomes
is 1, subtractP(D≤10 7). In other words:
P(D >107) = 1−P(D≤10 7).(1.2)
For a given numberi, the probabilityF D(i) =P(D≤i) is known as thecumulative mass
functionor cmf. The usefulness of the cmf, is related again to event calculus, for example asking
the probability that the demand is between 1 and 10 million units. That is,P(10 6 < D≤10 7)
can be expressed in terms of the cmf asF D(107)−F D(106).
Another very important quantity is known as the mean, or average. This comes from
averaging all possible outcomes for the demand weighted by their probabilities. This quantity
is denoted asµ D =E(D) = P∞ i=0 ipi = 0p0 +1p1 +2p2 +. . .2 Averages are important for demand
estimation, because they provide a scenario that is centered around the more likely outcomes
for the demand. For example, when making a resource allocation decision, such as building a
factory or a data-center, the capacity should comfortably handle the average demand for the
facility. But then, the next immediate question is how much slack capacity should the factory
have?
The variance of a random variable is a measure of how much the random variabledeviates
from its meanµ D. The variance is defined asσ 2 D =Var(D) =E[(D−µ D)2], theEoperator
(or function) denotes the operation of multiplying each possibly outcome by its probability. So,
E[(D−µ D)2] can be computed as P∞ i=0(i−µ D)2pi. The square root of the variance is known
as thestandard deviationas is denoted by the symbolσ D.
2Related to event calculus, the meanµ D is also equal to P∞ i=0 ¯FD(i), where ¯FD(i) = 1−F D(i). Why is this
the case?

3Instructor: Elioth Sanabria
1.2.1 Useful Probability Calculations
So far, we have reviewed basic concepts in probability that can answer some questions about
the random outcome of the demand. We can go one step further and with some knowledge of
the distribution, answer other questions: For example, say that you only know the meanµ D of
the demand, and they ask you, if the average demand is 1 million units, what’s the probability
that the demand is less than 5 million?
A useful relation known asMarkov’s Inequalitystates thatP(D≥a)≤µ D/a, replacing
a= 5×10 6 tells us that the probability that the demand exceeds 5 million units is at most
µD/(5×10 6). If the average demandµ D is 1 million, the probability that it is at least 5 million
is at mostµ D/a= 10 6/(5×10 6) = 1/5 = 20%. Therefore, the probability that the demand
is less than 5 million is at least 80% (could be more). That being said, this estimate is rather
loose as the inequality isat mostthe value. In the previous example, it could be the case that
the probability that the production exceeds 5 million is exactly 0.
Another useful inequality is known asChebyschev’s Inequalitystating thatP(|µ D −D| ≥
kσD)≤1/k 2. Going back to our previous example, suppose that additionally to knowing that
the average demandµ D is 1 million, we also know that its standard deviationσD is 100,000 units.
Applying this inequality, the probability that the demand is below 800,000 or above 1,200,000
is at most 25% (using the inequality withk= 2). Going back to the previous question about
the probability that the demand exceeds 5 million is at most 1/40 2 = 0.06%. Even more can be
said, for example the probability that the demand exceeds 2 million is less than 1/100 = 1%.
The moral of this, is that with just the meanµ D and the standard deviation of the demand
σD there is already a lot of useful information that can be inferred about the demand without
knowing the full probability distribution of all its outcomes.
1.2.2 Side Information
The demand is clearly influenced by other variables (random or deterministic): the economic
cycle, interest rates, competitors prices, the demand of other products, weather and so on.
Having a framework to understand how a variable affects the demand is crucial to better estimate
and anticipate the demand.
Suppose you are in charge of the production of the Airpods wireless earphones. Intuitively,
the demand of Airpods ispositivelyrelated to the demand of other products in the iOS ecosys-
tem (such as laptops, iPhones, etc) andnegativelyto competitor products, such as Android
headphones. Moreover, the demand for Airpods should not be affected by the demand of apples
or oranges.
Ideally, it would be great to have a mathematical functiong, that given an outcome of a
related random variableX=xgives us the best estimate of the random demandD. You

Supply Chain Analytics: A data-driven approach4
can imagineXas the demand for iPhones in the AirPods example (as a significant portion of
AirPods users own iPhones). Then, we would like to find the functiongthat in average gives
the closest prediction of the demandD. One such formulation is
min
g
E

(g(X)−D) 2 ,(1.3)
This way of thinking is a strategy that we will repeatedly use in the exposition of the topic.
That is, to ask what’s the best possible data-driven way to make guesses about the random
nature of the demand. AssumingXcan takex 1, x2, . . .different values. The expected value
E

(g(X)−D) 2 , takingp ix =P(D=i, X=x) can be written as:
E

(g(X)−D) 2 = ∞X
i=0
X
x=x1,...
(g(x)−i) 2pix,(1.4)
The strategy to solve a seemingly complex problem like this is to break down a complex problem
into smaller and easier problems to solve (a well known paradigm in Computer Science known
as divide-and-conquer). Then, the first observation is that the solution only depends on the
values of the random variableX. That is, for a givenX=x, the functiong(x) is a single value
guessing the most likely outcome of the demandD. Taking only a single value ofX=xgives
the expression P∞ i=0(g(x)−i) 2pix. This expression has a single unknowng(x), which is a convex
function3. Taking derivatives and equating to 0 leads to the following expression forg(x):
g(x) =
∞X
i=0
i pix
px
=E(D|X=x),
This expression intuitively says, that the best predictor for the demandDwhen the side variable
Xis equal toxis the expected value of the demand given thatX=x. This is the so-called
conditional expectation, which can be seen as simply taking the well known expected value with
new probabilitiesp ix/px representing the likelihood of each outcome of the demand given a
certain outcome for the side variableX. The denominatorp x scales the new probabilitiesp ix
of the demand so that they add up to 1, because instead of considering all outcomes ofX, only
the case whereX=xis considered.
Example 1.1(Hydroelectric Plant).Suppose you are managing a hydroelectric plant sup-
plying electric energy to a major city.Xrepresents whether or not it is an extremely hot day
(X= 1 means it is extremely hot, andX= 0 means it is not), extremely hot days occur rarely,
sayP(X= 1) =p h = 5%. But when they occur, the demand for electricity is very high (due
to the usage of Air Conditioner and other appliances). The conditional distribution of (D|X)
is given byP(D= 5Mw|X= 0) =P(D= 15Mw|X= 1) = 1. Given this distribution, what is
3A sum of convex functions is convex.

5Instructor: Elioth Sanabria
the average demandµ D of the power plant? The average demand of the power plant is:
µD =E[D] =E[E[D|X]] = 5Mw(1−p h) + 15Mwph = 5.5Mw.(1.5)
This relationship clearly shows one of the main ideas of this course: While the demand in
average is relatively stable at a level of 5.5Mw most days, with a small probability it can jump
to almost a 300% increase if it’s a very hot day. If the power plant does not have the capacity
to service the demand, it can be a catastrophic event for the city, since many crucial services
including hospitals and other vital supply chains rely on electricity. Hedging against rare events
is the whole point of a resilient supply chain. See Figure 1.1.
1 2 3 4 5 6 7 8 90
5
10
15
Extremely Hot Day (X= 1)
Normal Days (X= 0)
Time (Days)
Energy Consumption (Mw)
Realized Demand (D)
Average Demand (µ D = 5.5)
Figure 1.1: Energy consumption over time. The spike represents a rare event where temperature
(X) affects the demand (D).
1.3 Demand Evolution over Time
So far, we have presented a static view of the demand as random variable. While useful as a
first order tool of analysis, it is easy to imagine that the demand of many products is in fact
time-dependent: Ice cream sales peak in the summer, airline traffic peaks around holidays and
restaurants demand has modes around lunch and dinner. Similar to last example of the previous
section, averaging without side information can generate misleading estimates for the demand.
Therefore, if the demand is time-dependent it makes sense to include time in its modeling.
Time is represented as a variablet= 0,1,2, . . .where each value oftrepresents a moment in
time. The unit of time can be taken as seconds, hours, days or years. Depending on the context
of the specific supply chain decision: For example, in analysing the demand behaviour in an

Supply Chain Analytics: A data-driven approach6
online store, it makes sense to have relatively small units of time. Conversely, when planning
capacities or resources for facilities, it makes sense to consider the demand over years. Later it
will also become evident that there is a trade-off between the historical amount of data available
and the quality of the estimation of the demand.
Incorporating time into the demand estimation leads to indexing the demand random vari-
able by time asD t, denoting the random demand at timet. In most scenarios, we have access
to the demand up to some point in time in the past. For example, suppose that you are given
the monthly historical demand for the last 5 years. Chronologically, these are 60 datapoints
d0, d1, d2,· · ·, d59. Data like this can be denoted compactly as{d s}t s=0 (imagine a spreadsheet
with a single column and a row for each entry of the demand at every date). The distinction
between the capital and lowercase symbols for the demand denote the random variableD t and
certain outcome for itd t. This is important, as even though the past is a realization of the de-
mand, the outcome was a result of the probabilistic nature of the demand (for example, a month
of low demand could be caused by an unexpected shock, and it might provide information for
future outcomes of the demand).
Random variables that evolve over time are referred asStochastic Processes. We present
a couple of examples to get a feel for stochastic processes. One of the simplest models is the
following:
Dt+1 =α+βD t +V t,(1.6)
We call this theBase Modelas it will allow us to model some common behaviours of the demand
over time. In this modelα, β∈Rare two constants whileV t is an independent random variable.
In plain words, the equation says that the demand at timet+ 1 is equal to a constantαplus
a term multiplying the previous period demandD t, plus a random quantityV t (normally this
quantity expresses what’s commonly referred as an error or simply unexplained variation of the
demand). This model is related to the previous one (independent of time) whenβ= 0 4.
To see the dependence over time, assume that at time 0, there is an initial demandD 0 ≥0.
D1 =α+βD 0+V0, andD 2 =α+βD 1+V1 =α+β(α+βD 0+V0)+V 1 =α+βα+V 1+αV0+β 2D0.
Continuing this iterative process leads to the following expression:
Dt+1 =
t−1X
j=0
(α+V t−j)βj +β tD0,(1.7)
AssumingV t fort= 0,1, . . .has identical and independent distribution withE(V t) = 0. Taking
expectations yields the following:
E(Dt+1) =α 1−β t 1−β +β tE(D0),(1.8)
The first term of the right hand side comes from the finite sum of a geometric series 5. Then,
4IfV t is a random variable so isα+V t. In fact, constants are random variables with their probability mass
concentrated at a single value.
5Takes t = 1 +β+· · ·+βt andβs t =β+· · ·+βt+1, subtracting the two equations yields the result shown.

7Instructor: Elioth Sanabria
the expected value of the demand depends on the expected value of the initial demand, plus
a term that converges toα/(1−β) attgoes to∞. Moreover, this convergence only occurs if
|β|<1. If|β|>1 the demand explodes as time goes by (think why this is the case). When
β= 1 withP(V t = 1) =P(V t =−1) = 1/2. The model retrieved is called aRandom Walk.
Among other interesting properties, random walks drift away indefinitely to±∞and can also
be negative. See Figure 1.2 to see the different models. With a small modification, of taking
ln(Dt) instead ofD t aGeometric Random Walkcan be used to model the demand.
0 10 20 300
50
100
Mean≈33.3
Time (t)
Demand (Dt)
Mean Reverting (β= 0.7)
0 10 20 30
100
200
300
400
Time (t)
Demand (Dt)
Random W alk (β= 1.0)
0 10 20 300
0.5
1
·104
Time (t)
Demand (Dt)
Explosive (β= 1.15)
Figure 1.2: Stochastic demand simulations (α= 10, D0 = 100, Vt ∼U(−15,15)) illustrating the
impact ofβ. TheMean Reverting(β= 0.7) case centers aroundα/(1−β), theRandom
W alk(β= 1) exhibits non-stationary drift, and theExplosive(β= 1.15) case follows a steep
exponential trajectory.
1.3.1 Modeling Seasonality and Time-varying Factors
Another common feature of the demand isseasonality. Seasonality is defined as the fluctuation of
the demand caused by the passage of time or certain time-dependent events (such as holidays or
weather variations). Think of holidays and demand that changes due to weather or temperature.

Supply Chain Analytics: A data-driven approach8
The most common way to model this is to follow the method in the weather example of the
previous section, by adding an extra variable codifying the side-information of interest. In the
case of seasonality, this can be achieved by adding binary variables that are equal to 1 whentis
equal to that time. For example, think of daily data where we can to capture day of week effect
on the demand (think of a restaurant or retail business). A way to achieve this, is to modify
theαterm in Equation (1.6) as:
αt =
s−1X
d=0
1{tmods=d}γ d,(1.9)
In this case, the indicator1{tmods=d}is only one everysobservations. In the days of the
week example,s= 7 as there are 7 days in a week. Putting this expression back in the base
model yields:
Dt+1 =
s−1X
d=0
1{tmods=d}γ d +βD t +V t,(1.10)
The model is quite similar to the original one (that had only one constant termαwhile this
one has a constant term for every day of the week). In general, we can also include time-
varying factors, such as seasons (also encoded in indicators or numerical variables. A clean
way to include these factors is to flatten these variables into a vectorh t. For example, letting
ht = (1, t)′ retrieves a model with a constant plus a linear trend allows to express the original
αt term asα t =Ah t whereAin this case is a vector of parameters with the same dimension as
the number of time-varying variables, that isA∈R |ht|. This allows to re-write the base model
as:
Dt+1 =α t +βD t +V t =Ah t +βD t +V t,(1.11)
This instance of the base model allows for arbitrary specifications of time-dependent variables.
See Figure 1.3 for an example of the decomposition of the demand into different components.
1.3.2 Other Modeling Specifications
It is easy to imagine that a similar strategy can be employed to add arbitrary random variables
or other stochastic processesX t of variables that are related to the demandD t. In general,
one can imagine that any arbitrary real-valued function can be calibrated to solve the following
problem:
min
g
E[(g(Dt, Dt−1 . . . , Xt, Xt−1, . . .)−Dt+j)2].(1.12)
It should be evident that this is exactly the same problem in Section [1.2.2] where the optimal
solution isg(D t, Dt−1 . . . , Xt, Xt−1, . . .) =E(Dt+j|Dt, Dt−1 . . . , Xt, Xt−1, . . .). Then, speaking
strictly from an optimization point of view, what matters is that the family of functionsgcan

9Instructor: Elioth Sanabria
40
60
80
Dt
Demand T rajectory Fitted ˆDt
RealD t
0
20
40
60
80
αt
Seasonality (Indicators)
20
30
40
βDt
Autoregressive Part
0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30
−5
0
5
Time (t)
Vt
Noise (Residuals)
Figure 1.3: Demand decomposition into different components: Seasonal, autoregressive, and
noise. Corresponding to each term in the specification of the demand.
express the conditional expectation of the demandD t+j as a function of the other variables.
Whether the model is a simple linear regression or a sophisticated neural network, what matters
is that it can capture the shape of the conditional expectation. As we will see next, there is
another tension related to the fact that in general the probabilistic distribution of the demand
is unknown and only a finite sample of the variables has to be used for estimation.
1.4 Demand Estimation in Practice
So far, we have built a methodological theory to study the evolution of the demand over time.
The core message is that the best possible guess for the demand is the conditional expectation
of the demand taking into account information provided by other relevant variables. In practice,
the situation is significantly different: At best there are limited observations of the historical
demand (or no information at all in the worst case). The side-variables that affect the demand
are unknown or unobservable and in many cases they are endogenous (competitors set prices
reactively to their own demand and compete against each other for market domination). The
latter situation is more complex and will be studied in a later chapter. In this section, we focus

Supply Chain Analytics: A data-driven approach10
on the case where we have limited data and want to predict the demand in theshort-term.
Here, short-term is used loosely as the foreseeable future.
The main estimation problem for the demand is that its true probabilistic distribution
is unknown. Then, the goal is to learn the demand fromsampleobservations. Suppose, a
historical yearly demand of salmon in a country. This demand should be stable and more or
less proportional to the population of the country, to account for the population fluctuation,
consider theper capitademand. This historical demand is represented by the observations
{ds}t s=1. Estimating the average demand from samples is calculated as:
µD(t) = 1 t tX s=1 ds,(1.13)
This average converges to a stable (constant value) in various cases: For example, when the
demand samples areindependent and identically distributed, or i.i.d. Meaning that they come
from the same probabilistic distribution, and the previous values do not affect the probability
of new outcomes of the demand. One can see getting observations of the demand as sampling
the outcome of an experiment repeatedly and measuring the demand after each trial.
It is important to determine how reliable this estimate is, especially when managing a supply
chain as making resource allocation decisions in the future can be extremely costly. Probability
theory has two answers regarding how trusted this estimator can be: TheLaw of Large Numbers
and theCentral Limit Theorem.
The Law of Large Numbers (LLN) states that for a large enought, the average demand
(sampled i.i.d. with finite mean and variance)µ D(t) converges to the true average valueµ D.
That is,µ D(t)→µ D ast→ ∞. As mentioned before, this is important because there is
a probabilistic guarantee that sampling the demand i.i.d. and averaging its values over time
recovers the true average demand.
The Central Limit Theorem (CLT) goes a step further and provides a probability distribution
for the randomness of the demand. Given an i.i.d. sample of the demand{d s}t s=1. The random
variable defined by
√
t(µD(t)−µD)
σD converges in distribution to a random variableZdistributed
as a standard normal random variable 6.
Example 1.2(Rice Storage Levels).The government of Japan asks you to conduct a study
to determine what level of rice reserves they should hold. Their first question is how many years
tof data they should look at to get a 95% confidence estimate of the average demandµ D that
is within 10% of the true value, using the sample estimateµ D(t). Suppose you are told that
the standard deviation of the demandσ D is 30% of the meanµ D. That is,σ D =µ D30%.
6A standard normal random variable has probability density function (pdf)f(x) =e −x2/2/ √ 2π. A pdf is the
continuous analogous to the pmf in the sense that for a random variableXwith densityf(x) the probability
P[X∈(x, x+δ x)] =f(x)δ x for a smallδ x >0.

11Instructor: Elioth Sanabria
Using the CLT we get that the sample average demand is equal in distribution to:
µD(t) d= σD√ t Z+µ D,(1.14)
Dividing byµ D yields the percentage error σD µD √ t Z+ 1. Where σD µD √ t Zis the error in terms
of the demand, which can be positive or negative. Then, for this expression to within 10% of
the true value with 95% confidence we need the following to be true:
P


 σD µD √ t Z

 ≤10%  = 95%,(1.15)
Using the fact thatσ D/µD = 30%, the probability can be rearranged toP(|Z| ≤
√
t/3) =
1−P(|Z|>
√
t/3) = 95% orP(Z >
√
t/3) = 5%/2 = 2.5%. That is, the tail cdf of the standard
normal distribution ¯Φ( √ t/3) = 2.5%. Applying the inverse 7 tail cdf yields:
√
t/3 = ¯Φ−1(2.5%) = 1.96.(1.16)
With this, we get our answer that the number of observationstneeded for the sample average
to be within 10% of the mean is at leastt= (3(1.96)) 2 = 34.5 years.
In general, the above example is the best possible case. In probability textbooks, a commonly
encountered rule is that the sample size for estimation should be at least 30 observations. As
both the LLN and the CLT relied on the i.i.d. property of the samples for convergence.
To illustrate this, consider a random demand that follows the following demand process
Dt+1 =D t +c+σZ, withD 0 = 0. Note that this process is an instance of the base model with
α=c,β= 1 andV t =σZ. In this case,c+σZis called a normal random variable with meanc
and varianceσ 2 (likewise, a normal random variable can be transformed in a standard normal
by subtracting its mean and dividing byσ. This operation is useful to make computations
always in terms of standard normal random variables).
The demand process is equal toD t =ct+σ Pt i=1 Zt. The expected value of the demand
E(Dt) =tc, since each independent standard normalZ t has mean 0. Likewise, the sample mean
(extracted from historical observations of the demand) will be approximately this expected
value, that is,µ D(t)≈tc. Astincreases indefinitely, so will the sample mean, that is,µ D(t)→
∞ast→ ∞. So, how can we estimate the demand in these cases?
Most textbooks in Time Series spend a significant amount of their exposition in studying
stationarystochastic processes. That is, processes that converge to a stable mean in the long-
term and do not explode indefinitely. The textbook solution is to apply a transformation to the
original series, such that the transformation is stationary. In the previous example, a solution
7An inverse functionf −1(x) is a function such thatf −1(f(x)) =x. For example, the inverse function of
f(x) =e x isf −1(x) = ln(x).

Supply Chain Analytics: A data-driven approach12
is to consider a new series taking the differences of the demand. For example, consider the
difference process ∆ t =D t −D t−1 =c+σZ, which as discussed previously is a normal random
variable with meancand varianceσ 2. The sample mean of historical observations of ∆ t should
be the same as sampling standard normal observations.
1.4.1 Data-driven Demand Estimation
In practice we cannot expect to know beforehand the actual transformation that makes the de-
mand stationary, since we only have access to a historical demand series{ds}t s=1 ={d 1, d2, . . . , dt}
that is sampled from an unknown stochastic process (with unknown mean, variance, seasonality
and functional form).
The strategy that we will implement consists of the following steps:
1. Propose a functional form rich enough to capture the demand within a well-defined family
of functional forms.
2. Calibrate the parameters of the function that fit the demand closest via optimization.
3. Evaluate the performance of the proposed function out-of-sample.
For Step 1, we can use some of the modeling techniques that we have discussed in Section
1.3. For example, we can use for example the model presented in the previous section, ˆDt+1 =
ˆAht + ˆβDt. Here, the hats above the expression denote quantities that are calibrated from data.
Recalling the definition of conditional expectation in Section 1.2.2, a reasonable approach to
calculate the parameters for the demand is to solve the following optimization problem:
min
ˆA, ˆβ
E[( ˆDt( ˆA, ˆβ)−D t)2],(1.17)
This expression can be seen as an instance of the conditional expectation defined as the best
predictor for a random variable. The solution of this problem, is in fact an approximation of
the conditional expectation of the demand, that is, ˆDt(A∗, β∗)≈E[D t|Dt−1, . . .]. The quality
of the approximation depends crucially on two factors: That the functional form ˆDt allows to
approximate the conditional expectation. And also, on the sample sizetof historical observa-
tions for the demand. Moreover, note that when the true parameters of the demandAandβ
are used, the difference ˆDt(A, β)−Dt d=V t. In general,E(V t) should be equal to 0 (in terms of
the base model, ifV t has non-zero meanc, define new variablesα ′ =α+candV ′ t =V t −c,
thenE(V ′ t ) = 0). Therefore, this gives us another clue thatE( ˆDt(A∗, β∗)−D t) should be
approximately 0 when solving the optimization problem of fitting the demand.
To solve the optimization problem in Step 2, we solve the data-driven analogous of the
problem in (1.17) with a sample of demand observations{ds}t s=0 (in this case with the particular

13Instructor: Elioth Sanabria
choice of demand function in Step 1):
min
ˆA, ˆβ
1
t
tX
s=1
( ˆAhs−1 + ˆβds−1 −d s)2,(1.18)
This problem is a convex optimization program with a unique solution, that can be solved with
any off-the-shelf quadratic optimization solver 8.
It is appealing to use a family of functions that can express very rich functional forms
(for example, for a closed interval it is well-known that a Fourier basis can approximate any
continuous function). The formalism would be to express the fitted demand ˆDt(θ) as a function
of parametersθ, for example, the weights of a deep neural network, or the collection of splits in
a random forest. The approach would be the same, that is, to solve the optimization problem
minθ E[( ˆDt(θ)−D t)2].
The issue with this approach is that if the family of functions is too rich, the sample mini-
mization would be too optimistic (potentially 0 error as ˆDt(θ∗) =d t, for all observations in the
sample{d s}t s=1) and the performance for future predictions could be arbitrarily off. The two
main reasons for this phenomenon are: First, in practice we only have access tofinitesamples
that might not represent the full geometry of the conditional distribution (a well-known phe-
nomenon in statistical analysis). Second, real-life stochastic process are in general changing in
distribution over time (a so-calleddoubly stochastic process, where the original process changes
distribution based on another unknown random variable). In the context of demand estimation,
this could be a shock to the demand or a technological change. For example, the demand for
horse carriages catastrophically decreased with the invention and mass production of mechan-
ical engine cars (think that the measure of power of engines is calledhorsepower) in the early
twentieth century. Likewise, the introduction of new competitors, or shocks to the demand or
supply can change the trajectory of the demand.
While this problem cannot be fully mitigated, if there is enough data we can use what
we have learned to come up with a partial solution: For the first problem of over-fitting the
demand, we can sub-divide our full sample of historical observation into multiple sub-samples
where by setting up an experiment, we can use the LLN and the CLT to get an idea of the
performance of our demand estimation strategy out-of-sample. For the second problem, imagine
that distribution changes at random with a throw of a coin with small probabilityp, then, the
timeτin between changes in distribution is in averageE(τ) = 1/p. Then, if instead of training
our model with all of the historical observations, we train the model withkobservations, such
thatk <E(τ), with probability (1−p) k ≈1 we are in the current distribution of the demand
(another approach would be to weight the observations with a decaying weight). To see the
point of usingkobservations imagine a sudden financial crisis that impacts the demand of luxury
8Linear least squares is an instance of Quadratic Programming. Note that in matrix form linear least squares
has the objective||βX−y|| 2 2 = 2(βXX T β/2−βXy T +yy T /2) which is a quadratic program by lettingQ=XX T /2
andc T =−Xy T . Then, min β ||βX−y|| 2 2 = 2 minβ(βQβ T +βc T ) +yy T .

Supply Chain Analytics: A data-driven approach14
goods, such as designer bags. Using the whole historical demand will make the estimates to
continue growing if the historical data includes most of the period before the crisis. Using the
lastkobservation makes the estimates adjust faster to the new distribution of the demand. For
another example, imagine a positive shock to the demand, in Figure 1.4 a fixed model cannot
update to changes in the distribution of the demand.
50 60 70 80 90 100 110 120 130 140 15050
100
150
200
250
Shock (τ)
Time (t)
Demand (Dt)
Observed Demand (D t)
Stale Forecast (Fixed)
Updated Forecast ( ˆDt)
Figure 1.4: The impact of structural shocks on forecast divergence. Prior to the shock (t <100),
both models track the same pre-shock parameters; an alternating dash pattern (red/orange) is
used to display both distinct forecasting paths. After the shock (τ), the stale model (red) fails
to account for the change, while the updated model (orange) recalibrates and captures the new
demand trajectory.
Then, for Step 3 we take the following approach: Given historical observations of the demand
{ds}T s=1, a estimation window sizekand a prediction horizonj. Define the sample optimization
problem asℓ(t, t′) = 1/(t′ −(t+ 1)) Pt′ s=t+1(Ahs−1 +βd s−1 −d s)2. Likewise, define the absolute
error|ε t+j(A, β)|=| ˆDt+j(A, β)−d t+j|. The strategy is going to be to estimate multiple
observations of the error out-of-sample, and average them as a measure of how the model
performs out of sample. The pseudo-code routine to perform thebacktestcan be written as:
With this procedure, given two models (say the linear one that we have been exploring)
and a more sophisticated one like a Deep Neural Network model. The estimates of the mean
absolute errorµ ε can be used to compare the performance of the model out-of-sample. This
procedure is commonly used in finance to backtest algorithms. The key concept is that the
measurement of the error is done outside of the training data of the model, thus, mimicking
the behavior of the model in real life. Likewise, the choosing of the training window sizekcan
be evaluated with running this procedure multiple times with different sizes ofk. Of course,
to make the comparison fair, some exclusion of data might be needed as a larger window size

15Instructor: Elioth Sanabria
Algorithm 1Backtesting Demand Prediction
1:Input:Historical observations for the demandd 1, . . . , dT . A training windowk, and a
prediction horizonj. And a model specification for the demand ˆDt+j(·)
2:Output:The average out-of-sample absolute errorE(|ε t+j|)
3:procedureBacktest({d s}T s=1, k, j)
4:µ |ε| = 0
5:fort=ktoT−jdo
6:A ∗, β∗ ←argminℓ(t−k+ 1, t)
7:|ε t+j(A∗, β∗)|=| ˆDt+j(A∗, β∗)−d t+j|
8:µ |ε| =µ |ε| +|ε t+j(A∗, β∗)|/(T−k−j)
9:end for
10:returnµ |ε|
11:end procedure
needs more observations, and the number of observations for the errorε t+j will differ depending
on the window size. Lastly, this procedure can be easily modified to estimate the variance of
the error or other metrics of interest.
The errors are themselves objects of interest. As discussed previouslyV t+j d= ˆDt+j(A, β)−
Dt+j =ε t+j(A, β). Then, the meanµ ε(t+j) and the variance of the errorsσ 2 ε(t+j) can be used
to approximate the error of predictions. For example, approximatingV t+j =µ ε(t+j) +σ ε(t+j)Z
allows to construct confidence intervals for the demand. For example, the probability that the
forecasted demand at timet+jexceeds the quantityxis equal to:
P(Dt+j > x) =P( ˆDt+j(A, β) +Vt+j > x) =P

Z >x− ˆDt+j(A, β)−µε(t+j)
σε(t+j)
!
.(1.19)
Which is the well-known tail cdf of a standard normal distribution ¯Φ

x− ˆDt+j (A,β)−µε(t+j)
σε(t+j)

. It
is important to note that the prediction horizonjis crucial, because in general the longer the
prediction horizon, the larger the errors. That being said, there is no free lunch in prediction
since the estimation of the mean error and its variance is in itself a random variable. Moreover,
there is an implicit assumption that the distribution of the stochastic process is in some sense
stationary or fixed within a time interval. In the real-world there is no guarantee that this is
the case.

Supply Chain Analytics: A data-driven approach16
60 80 100 120 140 160 180
100
200
0.5
1
Time (t)
Demand (D
t)
Density (f)
Figure 1.5: The prediction trajectory ˆDt+j is plotted against Time (t), with the vertical Z-axis
representing the probability density function. The increasing spread of the normal distributions
illustrates the growing uncertaintyσ ε(t+j) over the prediction horizon.

Chapter 2
Inventory Management Models
2.1 Introduction
Even with a good grasp of the magnitude and direction of the randomness affecting the future
demand, there is always a decision behind predicting the future demand. Allocating resources
to match random demand is a difficult problem. The difficulty lies in that resources are often
fixed and not flexible: Determining the production capacity of a building, ordering a fixed
amount of materials to manufacture products, or scheduling workers ahead of time to service a
facility or store. What all these decision have in common is that there is an inherent trade-off
between allocating too many resources or allocating too little. On one hand, allocating too many
resources is costly and inefficient, and on the other, allocating too little, leads to congestion and
lost sales. Both are undesirable outcomes that have to be balanced in an optimal manner. In
this chapter, we present strategies to balance optimally these trade-offs in a data-driven way.
2.2 The Newsvendor Model
Following our exposition of characterizing the demand as a Stochastic Process{D t}∞ t=0, one of
the most popular production models is known as the Newsvendor Model [2]. In this model, a
production or inventory decision quantityqhas to be taken at timet= 0 to satisfy a random
demandD T at horizon timeT. The goal of the model is to determine what is the optimal
quantity of product that should be produced/ordered. Product is sold at a pricepwith a unit
costc. The objective function of the seller is their expected profit, defined as:
max
q
E[(DT ∧q)p−qc],(2.1)
The revenue of the firm is the minimum operator (denoted bya∧b= min(a, b)) between the
production/inventory quantityqand the random demandD T multiplied by the pricep. As the
17

Supply Chain Analytics: A data-driven approach18
production cost of each unit isc, the total variable cost isqc. Subtracting the cost from the
revenue gives the profit (note that fixed costs do not affect the production quantity as they do
not depend onq).
The first step to solve this problem is to note for any numbersa, b∈Rwe havea∧
b=a−(a−b) + where (x) + = max(x,0). With this fact, the profit can be re-written as
(DT ∧q)p−qc= [q−(q−D T )+]p−qc=q(p−c)−p(q−D T )+. Then, the profit can be
re-written as:
max
q
q(p−c)−pE(q−D T )+,(2.2)
To solve the problem we need to calculate what is the critical pointq ∗ such that the first
derivative of the profit is equal to 0. We also need to check that the function is concave, as this
will ensure that the critical point of the unique optimal solution maximizing the profit. Taking
derivate and equating to 0, yields ∂E(q−D T )+ ∂q = p−c p . We can use our definition of expected value
(in Section 1.2) to write ∂E(q−D T )+ ∂q as follows:
∂
∂q
∞X
i=0
(q−i) +pi = ∂ ∂q ∞X i=0 (q−i)p i1{i≤q}= ∂ ∂q qX i=0 (q−i)p i =P(D t ≤q) =F DT (q).(2.3)
The first equality is just a re-writting of the event (x) + =x1{x≥0}. The second one just
changes the limit of the sumation where the inner term is non-negative. The third equality
exploits the fact that the derivative is a linear operator1 and that the derivative ofqp i isp i with
respect toq. The second derivative is equal to 0, thus making the profit function concave and
ensuring that the critical point in indeed the quantity that maximizes the profit. The optimal
quantity is:
q∗ =F −1 DT
 p−c
p

,(2.4)
F −1 DT denotes the inverse cdf of the distribution of the demand. Connecting this to the demand
distribution Section 1, for example by taking the data-driven estimate of the demand as the
approximationD T = ˆDT (θ) +V T d=µ+σZwithµ= ˆDT (θ) (in general, an arbitrary functional
form for the demand. Withθ=A, βwe can take this as an instance thebase model) and
σ=
p
Var(VT ). With this approximation, the optimal quantity becomes:
q∗ =µ+ Φ −1
 p−c
p

σ.(2.5)
Where Φ −1 is the inverse cdf of the normal distribution. The interpretation of this expression
is that the optimal quantityq ∗ is the predicted value from the modelµ= ˆDT (θ), plus a buffer
proportional to the standard deviation of the demandσ=
p
Var(VT ). The multiplier Φ−1

p−c
p

balances how aggressive the provisioning of inventory should be. First, the pricepis normally
higher than the costc, that is,p > c. To get a feel for the multiplier, suppose the price is
1The derivative of a sum is the sum of the derivatives of its terms.

19Instructor: Elioth Sanabria
3 times the cost, orp= 3c(a typical pricing strategy in the absence of information), then
(p−c)/p= 2/3. Evaluating the inverse at this value gives Φ −1(2/3)≈43%, meaning that the
extra buffer above the predicted demandµis 43% of its standard deviationσ. The larger the
difference between the price and cost isp−c, the greater the amount of provisioning should
be (because the loss of profit from a sale lost is orders of magnitude higher than the cost). As
we will see next, we can modify this model to more complex situations where there are costs
associated with unsold product. See Figure 2.1 for a visual representation.
µ q∗
q∗ =µ+σΦ −1

p−c
p

Demand (DT )
Density
Figure 2.1: Optimal inventory levelq ∗ in the Newsvendor Model. The shaded area represents
the probability of meeting all demand, corresponding to the critical ratio (p−c)/p.
Example 2.1(Avocado T oast Restaurant).A national restaurant chain serves a signature
avocado toast dish in their menu. The restaurant procures avocados from a wholesale producer
and can purchase avocados at a pricec= $0.68 per unit. Every avocado dish is sold at a price
p= $12, other variable costs add up toc a = $3 per dish (other ingredients and labor). Every
unused avocado has to be disposed at a cost ofc d = $0.20. The distribution of the demand at
timeTis estimated as a normal random variable with meanµ= 70 and standard deviation
σ= 10 dishes for a specific location of the restaurant. Also, when customers arrive and the
avocado toast is sold-out, with probabilityp r = 1% they never come back (imagine a binary
random variableB r withP(B r = 1) =p r = 1−P(B r = 0), independent of the demand). The
average lifetime profit per customer is estimated to beℓ= $200. What is the optimal quantity
of avocados that maximizes the expected profit for this location? What happens when the
lifetime profit per customer increases toℓ= $2,000?
The expected profit for the restaurant can be written as:
max
q
E[(DT ∧q)p−q(c+c a)−(q−D T )+cd −(D T −q) +Bℓ],(2.6)

Supply Chain Analytics: A data-driven approach20
Rearranging terms (notinga∧b=a−(a−b) + as in Equation (2.2)) leads to this expression:
max
q
q(p−c−c a)−(c d +p)E(q−D T )+ −p rℓE(DT −q) +,(2.7)
Similar to the previous example, the strategy to solve the problem is to take derivatives with
respect toqand equate to 0. The derivative ∂E(DT −q)+ ∂q is equal to− ¯FDT (q) =F DT (q)−1 (the
trick is the same as in Equation (2.3), noting that the expression is non zero when the demand
is betweenqand∞). Grouping terms leads to the following optimal demand quantity:
q∗ =F −1 DT
 p−c−c a −p rℓ
p+c d −p rℓ

.(2.8)
In the case of this example, this leads toq ∗ =µ+σΦ −1

p−c−ca−prℓ
p+cd−prℓ

≈76.03 avocados. When
the lifetime profit per customerℓis $2,000 the optimal quantity rises toq ∗ ≈81.72 avocados.
2.2.1 Empirical Distributions
The Newsvendor model relies heavily on the accuracy of the inverse cdfF −1 DT . In real life, the
true distribution of the demand is rarely known, and the estimation has to be done on the
empirical distribution from a sample. The empirical distribution of the demand is constructed
by first sorting observations of the demand in ascending order. A sample of i.i.d. observations
of the demand{d i}N i=1 (here, the big assumption is that these are all independently sampled
observations of the demandD T ). Letd (i) be thei-th smallest element of the sample, such
thatd (1) ≤d (2) ≤ · · · ≤d(N) . TheEmpirical probability measureassigns each sample a equal
probability 1/n. The sample or empirical mean is then defined as 1 n Pn i=1 di which by the LLN
converges to the true mean as we discussed in the previous chapter. Likewise, the empirical cdf
is defined as ˆFn(q) =i/nfori= argmax{i:d (i) ≤q}. Similarly, the empirical inverse cdf is
defined as ˆF −1 n (p) =d (i) fori= argmin{i:i≥pn}. A natural question is how far off is the
Newsvendor inventory quantity when using the empirical cdf in lieu of the real one.
A useful bound for the divergence of the empirical cdf and the actual one was developed in
two papers [6, 7] and is commonly known as theDKW bound(due to the authors of the first
paper, which was later refined by the second one). The bound is stated as follows:
P

sup
q
|F(q)− ˆFn(q)|> λ

≤2e −2nλ2 ,(2.9)
What this bound states is that the probability that the deviation from the empirical and the
actual cdf exceeds a valueλ(for any valueq) is less than 2e −2nλ2 . Asnincreases, this probability
decays to 0. Meaning that as the sample size increases, the accuracy of the empirical cdf
converges to the true one. Interestingly, we can use this inequality to build confidence intervals
on the empirical cdf. For example, with probability 1−αthe true value of the cdfF(q) is within
ˆFn(q)±
q
1
2n ln
 2
α

(hint: equate the right hand side of (2.9) toα) for anyq.

21Instructor: Elioth Sanabria
Going back to our topic of interest, we want to know how far is the solution of the empirical
Newsvendor model ˆq∗ n =F −1 n (γ) with respect to the real solutionq ∗ =F −1(γ) (here,γdenotes
the optimal constant in the Newsvendor model, for exampleγ= p−c c in the plain vanilla
formulation). In Section 1 we emphasized that event calculus is a powerful problem solving
tool. That is, to write complex events in terms of events that we know well probabilistically.
In this case, we know about bounding the empirical cdf in Equation (2.9) and need to find the
right event to express the relation to the empirical inverse cdfF −1 n (γ).
The optimal quantityq ∗ =F −1(γ) = inf{q:F(q)≥γ}. Now we know thatF(q) is within
ˆFn(q)±
q
1
2n ln
 2
α

with probability at least 1−α. Putting these two facts together we get that
q∗ ∈inf{q: ˆFn(q)± q 1 2n ln  2 α  ≥γ}orq ∗ ∈F −1 n  γ± q 1 2n ln  2 α  with probability 1−α.
Note that this bound is not symmetric and not centered atF −1 n (γ) =q ∗ n. See Figure 2.2.
γ−ϵ γ γ+ϵ
qL
ˆq∗ n
qU
ˆF −1 n (p)
(γ,ˆq∗ n)
Probability (p)
Quantity (q= ˆF −1 n (p))
Figure 2.2: Mapping the DKW confidence interval. The symmetric intervalγ±ϵresults in a
non-symmetric confidence interval [q L, qU ] due to the nonlinearity of the inverse CDF.
Often, it is also a natural question what should be the average profit using a quantity ˆq
(for example, the optimal sample inventoryq ∗ n) given a series ofnhistorical observations of the
demand. The sample average profitµ π(n) of the plain vanilla Newsvendor model is:
µπ(n) = 1 n nX i=1 ˆq(p−c)−p(ˆq−d i)+,(2.10)
We know that because of the CLT, this mean will converge to the true average profitµ π =
ˆq(p−c)−pE(ˆq−D T )+. The variance of the profit isVar(p[(ˆq−D T )+]) =p 2Var(ˆq−DT )+, for
any distribution of the demandD T , this variance is at mostq 2/42. Then, we have the following
probabilistic relationship between the sample and true profit:
µπ(n) d=µ π + p
p
Var(ˆq−DT )+ √n Z≤µ π + pˆq 2√n Z,(2.11)
2This is the so-called Popovicius’s variance inequality. LetXbe a random variable such thatP(X∈[a, b]) = 1,
then,Var(X)≤(b−a) 2/4.

Supply Chain Analytics: A data-driven approach22
The first equality is the equality in distribution of the CLT. The second is the result of bounding
the variance with the inequality above. The result says that for any distribution of the demand,
in the i.i.d. case solving the plain vanilla Newsvendor problem converges to the true demand
asngrows, and that the noise is bounded by the product of the pricepand the quantity ˆq
divided by a factor of 2 √n. For example, to obtain a confidence interval with probability 1−α
of the true average profitµ π by using quantity ˆq, we have that the error|µπ −µ π(n)| d= pˆq 2√n |Z|.
Then, we want to find the valueϵsuch thatP(|Z|pˆq/(2 √n)> ϵ) =α, which is the same as
P(Z >2ϵ √n/(pˆq)) =α/2. Applying the inverse tail cdf of the normal distribution, we get
solving forϵ:
µπ ∈µ π(n)± ¯Φ−1(α/2) pˆq 2√n w.p. 1−α,(2.12)
For example, choosingα= 5%, ¯Φ−1(α/2) = 1.96, meaning that the true profit is with 95%
probability within 1.96 pˆq 2√n of the sample profit in the plain vanilla Newsvendor model. This
technique can also be used for all variations of the Newsvendor problem in the i.i.d. case, noting
that the complement varianceVar(D T −ˆq)+ is also bounded.
These bounds are very useful because the do not depend on the distribution of the demand
and allow to infer the true performance of the model as a function of the sample size. We
illustrate this in the following example.
Example 2.2(Launching a new product).A supermarket chain is planning to release a
new bottled orange juice. They perform a pilot of 30 days (n= 30), observing an average daily
profit of$1,500. The price of the juice is$3.49 and they produce per store ˆq= 100. Assuming
the distribution of the demand of juices is i.i.d. in the plain vanilla Newsvendor model. The
shelf opportunity cost of the supermarket (the minimum profit that a product makes in that
shelf area) is$1,450 per day. With this data, the supermarket wants to conduct a hypothesis
test to decide whether to include the orange juice permanently or continue the pilot. What’s
the probability that the daily profit is less than$1,450?
With our analysis we know the true profitµ π is bounded in distribution toµ π(n) + pˆq 2√n Z=
$1,500 + ($349/2
√
30)Z. ThenP($1,500 + ($349/2
√
30)Z <$1,450) simplifies toP(Z <
−$50(2
√
30)/$349), which isP(Z <−1.56) = Φ(−1.56) = 5.9%. Which means that for a
95% confidence one sided test, the pilot should continue (as the probability is above 5%).
2.3 Inventory Replenishment - The(s, S)rule
In the previous section, we proposed a model for optimizing a production quantity such that
profit is maximized in a static setting. The methodology can be extended to optimize multiple

23Instructor: Elioth Sanabria
products and locations. As well as optimizing production accross time. In this section, we deal
with a common inventory policy taking into account the evolution of the demand over time.
In the previous chapter, we characterized the randomness of the demand as a Stochastic
Process{D t}∞ t=0. Assuming the distribution of the demand is known, define the inventory level
at periodtbyI t. The inventory can be defined as the quantity of a commodity or product that
is stored to service a random demand. The simplest rule to replenish the inventory is known as
the (s, S) rule. This rule works as follows: at the end of periodt, if the inventoryI t is below
a levels. An order (assumed to fulfill instantaneously) replenishes the inventory to a levelS.
Then, the inventoryI t+1 is equal toS−D t+1 whenI t ≤s, and it isI t −D t+1 otherwise (in the
case whenI t > s). Clearly, the time between inventory replenishments is random and depends
on the distribution of the demand.
Under the (s, S) rule, the inventory is in itself a random variable that depends on the
demand. The conditional distribution of the inventory is given by:
P(It+1 =j|I t =i) =P(D t+1 =S1{i < s}+i1{s≤i≤S} −j),(2.13)
When the distribution of the demand is i.i.d., that is,D t d=Dfor allt. We can express the
inventory processI t as a Markov Chain 3 with transition probabilitiesp ij =P(D=S1{i <
s}+i1{s≤i≤S} −j). Note that the inventory can take negative values as the demand can
exceed the inventory quantityI t. Conversely, under the (s, S) rule, the inventory never exceeds
Sby construction. See Figure 2.3.
1 2 3 4 5 6 7 8 9 10 11 12 13 14
s
S
Order toS
Order toS
Order toS
S
s
Time (t)
Inventory Level (It)
Figure 2.3: Inventory levelI t over time under the (s, S) policy. Replenishment is triggered the
momentI t < s, instantly bringing the stock back to the maximum levelS.
With these elements we have enough building blocks to express problems of interest: For
example, suppose that everytime there is a replenishment of inventory, there is a fixed costK
3A Markov Chain is a special class of Stochastic Processes, where the distribution of the processX t depends
only on the realization of the process the previous periodX t−1.

Supply Chain Analytics: A data-driven approach24
plus a variable cost ofcper unit. Likewise, suppose there is a holding cost ofc h per day the
inventory is stored. Finally, when the inventory is negative (meaning that there was not enough
inventory to service the demand), those sales are lost, a loss of a net revenue ˜pper unit. We
can summarize these costs as a functionc(i) for each possible state of the inventory:
c(i) =



ich,ifs≤i≤S,
ich +K+ (S−i)c,if 0≤i < s,
K+Sc−i˜p,ifi <0.
(2.14)
A Markov Chain transitions between states forever (even when it gets absorbed into a single
state). When the transitions can be expressed with a fixed matrixPwith elementsp ij denoting
the probability that the chain at stateitransitions to statej. The so-called limiting distribution
is given by a vectorπas:
lim
t→∞
P t =πorπP=π,(2.15)
Verbally, the vectorπdenotes the distribution of the states long-term. For example,π(i) =
limt→∞
Pt
s=1 E1{Xs =i}/tshows what proportion of time (out oft) is spent in stateifor a
Markov Chain{X t}.
In our case, this limiting distributionπis useful because we know we can express our
inventory model as a Markov Chain with transition probabilitiesp ij =P(D=S1{i < s}+
i1{s≤i≤S} −j). Then, the long-term cost of the (s, S) inventory rule is given by:
SX
i=s−M
π(i)c(i),(2.16)
WhereMis given by a value such thatP(D≤M) = 1. That is, the largest the demand can
be (why is the lower limit of this Markov Chains−M?). To compute the limiting distribution
we just need to solve the system of equationsπP=πnumerically. We spend the rest of this
section discussing how to find actual values for (s, S). See Figure 2.4 for an example analysis.
2.3.1 Finding the(s, S)values in the i.i.d. case
The most direct approach to find a pair of values 0≤s < Sthat is optimal in the sense
of minimizing is to enumerate all possible combinations of values ofs, Sand calculate the
stationary distribution by solvingπP(s, S) =π, whereP(s, S) is the transition matrix under
the policy (s, S) (recall, the transition probabilities depend on bothsandS, asp ij(s, S) =
P(D=S1{i < s}+i1{s≤i≤S} −j)). We summarize the procedure in the following
algorithm:

25Instructor: Elioth Sanabria
Algorithm 2Finding Optimal(s ∗, S∗)Inventory Policy - i.i.d. case
1:Input:A distribution of the demandP(D=i). A cost functionc θ(i) such as the one in
Equation (2.14) with parametersθ. And upper limit of inventory capacityS max, and for
the demandM.
2:Output:The optimal inventory policy parameters (s ∗, S∗).
3:procedureOptimalInventory(F D, cθ, Smax)
4:S, s ∗, S∗ =S max
5:c ∗,¯c=∞
6:forS= 1toS max do
7:fors= 0toS−1do
8:P←[p ij] = [P(D=S1{i < s}+i1{s≤i≤S} −j)] fori, j∈ {s−M,· · ·, S}.
9:Solveπsuch thatπ=πPand|π|= 1.
10:Update and compute ¯c←c ′ θπ.
11:if¯c < c ∗ then
12:Updatec ∗ ←¯c, s∗ ←s, S∗ ←S.
13:end if
14:end for
15:end for
16:returns ∗, S∗, c∗.
17:end procedure

Supply Chain Analytics: A data-driven approach26
−2 −1 0 1 2 3 4 5 6
0
0.2
0.4
0.6
0.8
1
1.2 Lost Sales
i <0
Replenish
0≤i < s
Holding
i≥s
Inventory State (i)
Magnitude
π(i) c(i) π(i)c(i)
Figure 2.4: Long-term inventory cost analysis. The purple bars represent the weighted cost
contribution of each state to the total expected cost P π(i)c(i). Optimization aims to chooses
andSsuch that the high-probability states (π) align with low-cost states (c).
Given the structure of the transitions of the inventory, this is not the most efficient algorithm
to solve the inventory policy, but it is the easiest to implement as a computational routine. Next
we examine the case to find policies for time-varying demands.
2.3.2 The time-varying demand optimal inventory
The key observation in the previous subsection was that the inventory process is a Markov
Chain, that is, that the transition probabilities are time-homogeneous. As we explored in
Section 1, demand is often seasonal and time-dependent. In this section, we present a useful
technique to solve problems that have a time-dependent structure.
In the time-dependent setting, the demand distributionF Dt(i) =P(D t ≤i) changes from
period to period. Suppose we want to derive an inventory policy, that at each period tells us
the optimal ordering level that minimizes some cost (for example, the cost function in Equation
(2.14)). Given a time horizon ofTperiods in the future. The objective is to minimize a cost
over the time horizon as:
E
" TX
t=1
ct(It)
#
,(2.17)
The trajectory of the inventoryI t depends on the previous periods and is not time homo-
geneous, making the problem seemingly hard to solve. A useful technique to solve sequential

27Instructor: Elioth Sanabria
problems is to look one step ahead (or behind) and try to define a recursive relation that allows
to solve the problem going to the last periodT(where the decision is normally trivial) and solve
the problembackwards, in a recursive way. The easiest way to set up such relation is to define the
actionthat can be taken separated from thestateof the system, so that at each step the prob-
lem reduces to find the optimal action at that state in that time step. The state of the system in
this case is already defined as the inventory levelI t, an integer (potentially negative) denoting
the inventory amount at the end of periodt. In the previous section, for the (s, S) policy, the
action was coded in an indicator function (asI t+1 =S1{I t < s}+I t(1−1{I t < s})−D t+1
orI t+1 =I t + (S−I t)1{It < s} −Dt+1). Inspired by this, we can express the state and the
action of the systemI t+1 =j−D t+1 such thatj≥I t =i. In this case,jrepresents the new
level of replenishment of the inventory (or rather, the inventory at the beginning oft+ 1, before
the demandD t+1 is subtracted). The strategy is then to write a function ¯Ct(i) that represents
the optimal expected cost from timettoT, that is, ¯Ct(i) =E
hPT
s=t c∗ s(Is)|It =i i , wherec ∗ is
the optimal cost of taking the best inventory actions. The strategy is then, to write down a
one-step recursion that allows us to break down the problem to a single replenishment decision
at every timet. With our representation, we can express the optimal cost between states and
actions by the following relation:
¯Ct(i) = min j≥i E  c(i, j) +¯Ct+1(j−D t+1)  ,(2.18)
The interpretation of this equation is that the optimal cost ¯Ct(i) at timetwhen the last
inventoryI t =iis the expected cost of that stateiand the optimal actionj, for that period in
the functionc(i, j). Plus, the expected optimal cost of the new inventory at a levelj−D t+1.
The minimum denotes choosing the actionj≥ithat minimizes this cost.
With this recursion, it is possible to solve for allC t(i) for alli=−M, . . . , Smax and times
t= 0,1, . . . , T, starting from the end at timeT. And populating entries backwards (it is easier
to imagine a matrix ¯Cwith entriesc i,t = ¯Ct(i)). This problem solving technique is known
asDynamic Programmingand Equation (2.18) is aBellman Equation 4. Storing the optimal
replenishment levelsj ∗ t,i = argminj≥iE  c(i, j) +¯Ct+1(j−D t+1)  is also a good idea, as they will
be adictionaryto the optimal replenishment level when the inventory isiat timet. See Figure
2.5 to visualize the dynamic inventory policy.
The modeling aspect is captured in the cost functionc(i, j). The goal is to modify this
function to correctly capture the underlying business problem that we want to solve. We
illustrate this with the following example:
Example 2.3(Oxygen Concentrator Distribution Center).An oxygen concentrator com-
pany that delivers oxygen concentrators (a device used for patients that need a constant flow
of oxygen while they are at home) rents a warehouse to be a distribution center for the con-
centrators in a major city. They have a random seasonal daily demand for concentratorsD t,
4A equation representing a recursive relation of the optimal decision of a dynamic problem.

Supply Chain Analytics: A data-driven approach28
2 4 6 8 10 12 14
Slow
slow
Speak
speak
Order toS t
Order toS t
Order toS t
Low Demand High Demand Transition
Time (t)
Inventory Level (It)
Figure 2.5: Inventory process with time-varying demand. As the depletion rate (slope) increases
during peak periods, the Dynamic Programming solution adjusts the optimals t andS t levels
to minimize expected costs over the horizonT.
that among other features, depends on the atmospheric humidity levelX t (there is a correlation
between respiratory diseases and the level of humidity in the air). The cost structure of running
the warehouse works as follows: orders that are fulfilled with stock from the warehouse have
a unit cost ofcdollars (using an in-house delivery system). Orders that are fulfilled when the
demand exceeds the stock cost ˜cdollars using an external courier that picks up a concentrator
in another facility and delivers it to the client, this cost is higher than the in-house system, that
is ˜c > c. Stock replenishment orders have a fixed costKper truck plus a unit costc r (the lead
time is overnight, and each truck can store up toLconcentrators). Holding the concentrators
in the facility has an associated daily costc h (including maintenance and the internal logistics
of the warehouse that are proportional to the number of concentrators). How to model and
minimize this cost over the next month (T= 30, assuming today ist= 0) assuming a known
high-fidelity forecast of the humidity levelsX t for next month{x t}T t=0?
The first step is to write the cost functionc(i, j) to reflect these costs. For example,c(i, j) =
i+ch + ˜c(Dt+1 −j) + +1{j > i}(⌈(j+ −i +)/L⌉K+ (j + −i +)cr), note thei + = max(i,0) reflects
that when the inventory ends up negative, these orders are notback-orderedas they still end up
fulfilled at the higher cost ˜c. (j+ −i +) denotes the order quantity. The quantity⌈(j + −i +)/L⌉
denotes the number of trucks needed (⌈a⌉is the closest integer abovea, typically referred in
programing as the ceiling function 5).
The second step is to incorporate the humidity forecast{x t}T t=0. To do this, recall in Section
1 that a way to incorporate side-information is to analyze the conditional random variable, that
5A definition is⌈a⌉= min{x∈Z:x≥a}.

29Instructor: Elioth Sanabria
is,D t|Xt. Calibrating this conditional distribution results in conditional probabilitiesP(D t =
i|{Xt =x t}T t=0). Solving the problem with this side information amounts to calculate the
expectations with these conditional probabilities (instead of the unconditional ones). Replacing
both the new costc(i, j) and taking expectations conditional toX t =x t in (2.18). Explicitly,
this yields the recursion for ¯Ct(i) = minj≥i E[i+ch + ˜c(Dt+1 −j) + +1{j > i}(⌈(j+ −i +)/L⌉K+
(j+ −i +)cr) + ¯Ct+1(j−D t+1)|{Xt =x t}T t=0].

Supply Chain Analytics: A data-driven approach30

Chapter 3
Network Fulfilment Models
3.1 Introduction
So far, we have described mathematical models to match the random demand in the time
dimension. In this Chapter, we change the pace by thinking of problems satisfying the demand
physically in the space dimension. Most if not all problems in supply chain analysis deal with
some form of transportation problem as the demand requires moving goods or supplies between
the producers and customers.
Matching the demand in space also adds a non-trivial time delay that needs to be accounted
for when matching resources to satisfy the demand. Large companies like Amazon have to
optimize the location of their warehouses and orchestrate a large chain of distribution networks
to deliver their products in record time. Likewise, ridesharing marketplaces (such as Uber
or Doordash) have to balance a demand that changes in space and time with a supply side
of workers and drivers that will service different geographical locations as they finish their
deliveries and rides.
We will explore a series of common problems and solutions to supply chain management
problems in space, as well as algorithms and heuristics to solve them.
3.2 Warehouse consolidation and positioning
Imagine a supplier wanting to build a warehouse to service demand in a city or geographical
location. The supplier would want to build the warehouse in a place that is economically viable
and resource efficient to service this demand.
While the physical world that we inhabit is 3-dimensional, it is often useful to think of ab-
stractions that simplify the problem: For example, most geographical maps use a 2-dimensional
31

Supply Chain Analytics: A data-driven approach32
representation of the Earth (this makes sense as the Earth is more or less a manifold locally,
i.e. locally, we live in a flat world). Perhaps, one of the most powerful abstractions for physical
spaces are graphs. A graphGis defined as a set of verticesVand edgesE.
Graphs can be seen as discretization of a continuous space into a disjoint partition, connect-
ing with edges all physically adjacent partitions. For example, take a map such as in the left
side of Figure 3.1 with the five Boroughs of New York City (Manhattan, The Bronx, Queens,
Brooklyn and Staten Island) and make each Borough a vertex, drawing an edge if there is a
road connection between two Boroughs (vertices).
(a) Geographic Map of NYC’s Five Boroughs.
The Bronx
Manhattan Queens
Brooklyn
Staten Island
(b) Graph abstraction of NYC.
Figure 3.1: Graph abstraction of NYC representing each of the five Boroughs as vertices, and
their roads connections as edges.
Modeling a physical space as a graph has the natural trade-off of having tractable algorithms
to solve a wide-range of problems while losing some of the accuracy and resolution of the
underlying modeled real-world system. For example, in the graph of the figure, direct travels
between Manhattan and Queens can occur via two different bridges, but there is only one edge
representing their connection. In modeling traveling times, there is either the choice of creating
more nodes and egdes to represent the different routes and to attach numerically the respective
travel time to each edge, or toaverageinto the single edge all the possible routes between Queens
and Manhattan. Clearly, the tradeoff is between accuracy of the abstraction and tractability of
the solution, as most optimization algorithms scale proportional to the size of the Graph. In
general, mathematical modeling is the art of choosing an appropriate abstraction of a real-life
system that preserves the behavior of interest while being algorithmically tractable.
Going back to the problem of choosing a location for a warehouse, start with a graphG,
composed byNverticesV={1,2, . . . , N}and edgesE⊆ {(i, j)|(i, j)∈V2}. For example, the
graph in Figure 3.1 is composed byN= 5 verticesV={1,2,3,4,5}, each vertex corresponds

33Instructor: Elioth Sanabria
to a Borough: 1→Manhattan, 2→The Bronx, 3→Queens, 4→Brooklyn and 5↣
Staten Island. And edgesE={(1,2),(1,3),(1,4),(2,3),(3,4),(4,5)}.
Vertices can have different unique attributes, for example, in the model of this section each
vertex has an associated random demandD i fori= 1, . . . , N. This demand, is the usual demand
random variable and denotes the random realization of the demand (in this case, there is not yet
a temporal element to the demand and it can be taken as a static model with i.i.d. realizations
of the demand that repeat every day). Likewise, every edge (i, j) fori, j∈ {1, . . . , N}also has
a random variableT ij denoting the random traveling time of a vehicle starting in vertexito
vertexj.
3.2.1 Single Location Warehouse
With these elements, we can now start to model the problem of choosing a location to build
a warehouse. Letc i be the cost of running a warehouse in locationiwith enough capacity to
service the demand PN i=1 Di with high probability (see Chapters 1 and 2 on how this number
can be calculated, here it is taken as given 1). In this scenario, if it’s not possible to run a
warehouse in some vertex, then let the cost bec i =∞for such vertex (or exclude it from the
set of possible locations to run the warehouse). Likewise, let the cost of transports between
vertices (i, j) be equal to2 cij ∝T ij, for example the cost of the labor of a courier plus the cost
of gas that is proportional to the random traveling timeT ij, that isc ij =γ ijTij, clearlyc ij is
also a random variable.
For a warehouse built on locationi, the cost is equal toc i + PN j=1 Djcij. As this number
is a random variable, a first approximation is to look at the expected value and choose over all
possible locations, that is, solving the enumeration problem:
min
i=1,...,N
E

ci +
NX
j=1
Djcij

 ,(3.1)
It is an enumeration problem because it amounts to calculate the cost for each location and
choose the minimum. The emphasis in writing the costs as random variables instead of the more
common practice of writing them as constants is that there is a conscious choice to solve the
problem only in expected value or to consider other moments of their distribution. For example,
it could be the case that running the warehouse in one location has the lowest cost in expected
value, but the variation (either of the demands and the trips) is higher than another location
that has a slightly higher cost in expected value, but less variance (in this case, variance denotes
1In practice, one way would be to calculate a capacityϵsuch thatP( PN i=1 Di > ϵ)≤1−αand then quote
or calculate the actual cost of running a warehouse of that capacity for the value ofc i. You can also set up a
Newsvendor-like model to calculate a capacity that is also sensitive to missed sales or holding costs.
2a∝bdenotes thatbis proportional toaup to a constant, sayb= 2a.

Supply Chain Analytics: A data-driven approach34
the daily variation of running the warehouse satisfying random demands every day or period).
See Figure 3.2 to get a feel for evaluating the cost of building a single warehouse in Manhattan.
Evaluating Total Cost fori= 1:c 1 + P j Djc1j
The Bronx (D 2)
Manhattan (i= 1) Queens (D3)
Brooklyn (D 4)
Staten Island (D 5)
W arehouse Site
c12
c13
c14
c15
c11
Figure 3.2: Visualization of the enumeration step fori= 1 (Manhattan). To solve the problem,
the supplier calculates the expected total cost (warehouse overheadc i plus weighted transporta-
tion costs to all demand nodesD jcij) for each potential vertex and selects the minimum.
In general, for problems involving a random amount of money (either a cost or a payoff)
there is an amount of risk aversion that the decision-maker is willing to take, and it needs to
be made explicit in the problem formulation, or otherwise be acknowledged by the modeler.
For example, given two lotteries: one that paysX 1 = $100,000B 1 + (−$100,000)(1−B 1) and
anotherX 2 = $100B2 + (−$100)(1−B 2) with two independent coinsB 1, B2 withP(B= 1) =
P(B= 0) = 1/2. That is, two loteries that with 50% chance pay a positive amount and with
the same chance the player loses the same amount, in the first case$100,000 and in the other
$100. While both lotteries pay in average$0, that isE(X 1) =E(X 2) = $0 they are clearly not
the same game. Depending on their risk aversion, some players would choose to play lottery 1,
while others would play lottery 2 (or even choose not to play at all). The quantitative difference
between the two games is their variance. We have that the variance of the first lottery is
Var(X1) = 2 2($100,000) 2Var(B1) = ($100,000) 2 and the second oneVar(X 2) = ($100) 2. The
risk ratio between the two lotteries isVar(X 1)/Var(X2) = 10 6. In other words, playing the
first lottery has a million times higher variance than the second. While exaggerated, this
example shows the potential literal risk of only modeling decisions based on their expected
value. A quantitative approach to evaluate each lottery could be toweightthe variance or
the standard deviation, for exampleE(X 1) +λ
p
Var(X1) weights the standard deviation (in
dollars). A weightλ= 0 denotes risk indifference (thus, only caring for the expected return of

35Instructor: Elioth Sanabria
the lottery).λ <0 denotes risk aversion, whileλ >0 implies risk appetite. Note that the units
ofE(X 1) +λ
p
Var(X1) is dollars.
Another justification coming from the study of risk measures also justifies this by defining
the risk measure of a random variableXasR λ(X) = 1 λ lnE(e λX ). This risk measure is used in
risk management as it captures risk aversion, is convex and coherent and it is sensitive to tail
risks. In fact, we show that our strategy of weighting the risk is approximately equivalent to
this risk measure. To see why, note thate u = 1 +u+u 2/2 +. . .. Then,E(eλX ) =E(1 +λX+
λ2X 2
2 +. . .) = 1 +λE(X) +λ2 2 E(X 2) +· · ·= 1 +vwherev=λE(X) + λ2 2 E(X 2) +. . ., also note
that ln(1 +v) =v− v2 2 +. . .. Using these relations and noting that terms withv 3 and higher
vanish, we get:
lnE(e λX ) =λE(X) + λ2
2 E(X 2)− 1 2  λE(X) + λ2 2 E(X 2) 2 +. . .(3.2)
=λE(X) + λ2
2 E(X 2)− λ2 2 [E(X)] 2 +. . .
=λE(X) + λ2
2 [E(X 2)−E(X) 2] +. . .
=λE(X) + λ2
2 Var(X) +O(λ 3)
Noting that the termO(λ 3) vanishes to 0 and dividing both sides byλyields the desired
relation.
This shows that optimizing the objectiveE(X)+λVar(X) is a principled way of handling the
risk. An important aspect in practice is calibrating the risk aversion parameterλ. A well-known
principle to do this, is known as theCertainty Equivalent. This is simply an amount of money
that the decision maker is willing to pay (or receive) to be indiferent between the lottery and
a certain payoff. Solving for that amount would yield the implied risk aversion coefficient. For
example, suppose there is a lotteryX=−$100B+ $0(1−B) =−$100B, that is, losing a$100
with probabilityP(B= 1) or losing 0 with probabilityP(B= 0). SupposeP(B= 1) = 1/2, we
haveE(X) =−$50 andVar(X) = ($100) 2/4. A person is willing to pay$40 to exit the lottery,
this implies a Certainty Equivalent (CE) given by−40 =−50 + λ 8 1002 orλ= 80/100 2. In
general, giving the stakeholders similar lotteries and with their CEs is a standard way to learn
the risk aversion of a stakeholder, we will illustrate numerically how the trade-off between risk
and expected cost plays out later.
Going back to the warehouse location problem, the problem incorporating variance can be
stated as follows:
min
i=1,...,N
E

ci +
NX
j=1
Djcij

 +λ
vuuutVar   NX
j=1
Djcij

,(3.3)
Withλ >0 this optimization problem models a risk-averse decision-maker that penalizes vari-
ance in their cost (caused by both variance in the demand and in the transportation times).

Supply Chain Analytics: A data-driven approach36
This is again an enumeration problem that amounts to calculate the objective for each potential
warehouse location. It is also possible to consider other risk measures that penalize variation.
In the case where the cost of the facilitiesc i is fixed. The variance of the costVar[c k + PN
j=1 Djckj ] can be calculated asVar[ PN j=1 Djckj ] =1Σ k1⊺ where the entryi, jof the matrix
Σk isCov(D icki, Djckj ) =γ kiγkj Cov(DiTki, DjTkj ). For example, in the case of the diagonal
we haveCov(D icki, Dicki) =γ 2 kiVar(DiTki) if the demand and the travel times are independent
then this is equal toγ 2 kiVar(Di)Var(Tki). For the other elements off-diagonal we use the def-
inition of covariance 3, then,Cov(D iTki, DjTkj ) =E(D iTkiDjTkj )−E(D iTki)E(DjTkj ). With
the assumption that while the demands and the travel times are independent, but not the de-
mands and the travel times with each other. For example, it makes sense that travel jams in
Manhattan could affect traffic in The Bronx, and also that the demand for a product is Brook-
lyn is correlated with the demand for the same product in Queens. With this assumption,
we have thatE(D iTkiDjTkj ) is equal toE(D iDj)E(TkiTkj ) andE(D iTki)E(DjTkj ) is equal to
E(Di)E(Tki)E(Dj)E(Tkj ). In summary, the covariance matrix Σ k has entriesi, jequal to:
Σk(i, j) =
(
γ2 kiVar(Di)Var(Tki),fori=j
γkiγkj [E(DiDj)E(TkiTkj )−E(D i)E(Dj)E(Tki)E(Tkj )],fori̸=j. (3.4)
3.2.2 Multiple Location Warehouses
Sometimes it can be more efficient to choose multiple locations to satisfy the geographical de-
mand of multiple locations than a single warehouse location. This can be because the cost
structure is more favorable (closer deliveries are cheaper), due to economies of scale, or simply
ease of logistical burden by breaking down the demand to multiple difference warehouses. The
problem can also be interpreted as choosing providers to satisfy demand for different geograph-
ical locations.
To modify the previous section formulation, now each candidate location has a finite capacity
Ci to service demand. Likewise, we modify the costc i to be a fixed (and given) cost of running
the warehousei. The second and more important modification is that since multiple locations
can be chosen to service the demand, brute enumeration is in general not a great strategy, except
for small instances of the problem. To see why, suppose there areMcandidate locations, all
possible choices of subsets of locations is 2 M , which is a number that grows exponentially in the
number of possible locations4. Combinatorial Optimization studies algorithms to solve problems
where the solution takes the form of subsets by exploiting the internal structure of the problem,
not to be forced to enumerate all possible 2 M candidate solutions. A very powerful technique
to solve this problems is called Mixed Integer Programming, that is very similar to Linear
Programming (both in structure and algorithmically) by allowing integer variables (normally
3Cov(X, Y) =E(XY)−E(X)E(Y).
4Given a set ofMelements, each can be either included or not included in a subset. Since this is true for all
elements, the total number of subsets is 2 M , also called thepower set.

37Instructor: Elioth Sanabria
encoding either counting quantities or codyfing yes-no decisions as variables). See Figure 3.3
for a typical representation of the problem of matching possibleMwarehouses locations with
Ndemand target locations.
W1
W2
W3
WM
Candidates
Inactive (xi = 0)
D1
D2
D3
DN
Targets
q11
q12
q22
q23
qM3
qM N
2M possible
warehouse subsets
Figure 3.3: Bipartite representation of the Multiple Location Warehouse problem. Solid blue
lines represent an active assignmentq ij from selected warehouses (x i = 1). The light dashed
lines represent the combinatorial complexity: the model must select a subset ofMlocations
and then optimize the flows toNtargets.
A Mixed Integer Programming formulation of this problem entails adding binary variables
xi ∈ {0,1}denoting whether or not the location is chosen. Also, the variablesq ij ≥0 denote
the amount of demand (quantity) satisfied from warehouseito locationj= 1, . . . , N. The
next modeling step is to relate variablesx i andq ij to each other in an equation (that normally
becomes a constraint of the problem). For each warehouse it must be true that when it is
selected (x i = 1), the total quantity that can be serviced from the location cannot exceed its
capacityC i. In other words, PN j=1 qij ≤C i whenx i = 1, and conversely whenx i = 0 it should
be PN j=1 qij = 0. MIP formulations normally involve tricks manipulating real-world conditions
into equations (see [1] for some of the most common tricks). In this case, the trick is to write
the constraint as PN j=1 qij ≤x iCi. It is immediate that this constraint achieves the goal of
encoding both situations.
Likewise, it must be true that the random demand is satisfied to some level. For example, if
looking at the problem in expected value, that the demand is satisfied in average is the constraint
PM
i=1 qij ≥E(D j). Another common technique to deal with this type of constraints is to write a
constraint asP( PM i=1 qij ≤D j)≤η, meaning that with probability not exceedingη(say a small
percentage like 5%) the random demand will be satistied. In the case where the demand can be
approximated as a normal random variable, that is,D j d=E(D j) + p Var(Dj)Z. The constraint
P(PM i=1 qij ≤D j)≤ηcan then be written asP(Z≤[ PM i=1 qij −E(D j)]/ p Var(Dj))≥1−η, or
the constraint PM i=1 qij ≥E(D j)+ p Var(Dj)Φ−1(1−η), the similarity to the Newsvendor model
studied in Chapter 2 should be evident, as the contraint conveys that the quantity delivered

Supply Chain Analytics: A data-driven approach38
should be the mean of the demand plus a buffer proportional to the standard deviation of the
demand. The last constraint to be enforced is thatq ij = 0 whenx i = 0 and positive otherwise.
Letting ¯dj be an upper bound for the demand such thatP(D j > ¯dj) = 0, this can be achieved
with the constraintq ij ≤x i ¯dj With these constraints, we can write a first fomulation of the
problem in expected value as (letW⊆Vbe the set of possible locations for the warehouses to
make the notation cleaner):
min
qij ≥0,xi∈{0,1}
E



X
i∈W
cixi +
X
i∈W
X
j∈V
cijqij


 (3.5)
s.t.
X
i∈W
qij ≥E(D j) forj∈V,
X
j∈V
qij ≤x iCi fori∈W,
qij ≤x i ¯dj fori, j∈W×V.
As the costsc i are fixed, the objective can be written as P i∈W cixi + P i∈W P j∈V E(cij)qij.
This formulation is the typical warehouse optimization found in textbooks and can be solved
with off-the-shelf MIP solvers.
Similar to the discussion of the single warehouse model, as is, the model is only minimizing
the cost in expected value (both in the objectuve and the first constraint). Variations in the
travel timesT ij will cause fluctuations in the cost. We can take a similar strategy to hedge
this variation using a similar reasoning as in the single warehouse case. To do so, note that the
varianceVar[ P i∈W P j∈V cijqij] is equal to P i∈W P j∈V P k∈W P l∈V qijCov(cij, clk)qlk which
can be written in matrix form asqΣq ⊺ where Σ has entries:
Cov(cij, clk) =
(
γ2 ijVar(Tij),fori, j=k, l
γijγkl[E(TijTkl)−E(T ij)E(Tkl)],fori, j̸=k, l. (3.6)
Also using the chance constraint for the demand, the risk aware formulation of the problem can
be written as a Mixed Integer Quadratic Program (MIQP):
min
qij ≥0,xi∈{0,1}
E



X
i∈W
cixi +
X
i∈W
X
j∈V
cijqij


 +λVar

X
i∈W
X
j∈V
cijqij

 (3.7)
s.t.
X
i∈W
qij ≥E(D j) +
q
Var(Dj)Φ−1(1−η) forj∈V,
X
j∈V
qij ≤x iCi fori∈W,
qij ≤x i ¯dj fori, j∈W×V.
This formulation of the problem can be solved with a MIQP solver. Note that in this case
the objective uses the variance instead of the standard deviation as in the single warehouse
section. The problem can still be solved as a Mixed Integer Second-Order Conic Program
(MISOCP). The formulation is also implicitly assuming that the travel times and the demands

39Instructor: Elioth Sanabria
are independent from each other. In Figure 3.4 we can see the trade-off we mentioned earlier
considering different values ofλ.
12000 14000 16000 18000 20000 22000 24000 26000
Operational Variance
3600
3800
4000
4200
4400
4600
4800
5000Expected Total Cost
Efficient Frontier
Risk Averse
Risk Neutral
Figure 3.4: The Efficient Frontier for the warehouse location problem. The curve illustrates
the trade-off between minimizing expected operational costs and reducing cost variance (risk).
The green marker represents a risk-neutral approach (λ= 0), while the red marker indicates
increasing risk aversion.
3.3 Distributionally Robust Warehouse Location Optimization
Readers of the first sections should be feeling slightly uneasy regarding the sensitivity of these
optimization problems. By sensitivity, we mean how the optimal solution changes when the
input data changes. For example, there is a lot of expected values for the demandE(D j), that
as we have seen, when there is a small number of observations or it is in reality time-varying,
the sample mean PT t=1 dt might be within ax range of the true value. Compounding this effect
across all expected values and variances (which are in turn expected values as well) creates an
effect where the optimal solution of solving the warehouse problem with a sample observations
ˆq∗ ij might be substantially different from the true optimal solutionq ∗ ij.
Given a fixed solutionq ∗ ij we have explored previously how to build confidence intervals using
the CLT (see Chapter 2 and the empirical distributions section to see some of these techniques).
To get a feel for the interplay between the sample sizenand the number of verticesNwe use
a different but useful way of building confidence intervals, we illustrate this with an example:
Example 3.1(Local fulfillment centers).A last-mile delivery company wants to know the

Supply Chain Analytics: A data-driven approach40
optimal location to build their fulfillment centers to serve the New York metropolitan area.
Geographically, this area is composed by 23 counties, which makes a graph withN= 23 nodes.
The company has a sample size of daily orders for each of the counties going over 4 years
for a total of aroundn= 1,460 observations. Their data-scientist solves the basic warehouse
location problem in Equation (3.5) obtaining a solutionx ∗ i , q∗ ij for the optimal locations of the
warehouses and the quantity that each should deliver to each county. The management of the
company seems skeptical of the solution and ask the data-scientist for confidence intervals for
their estimation. Specifically, they want to know with 1−α= 95% confidence what is a range
for the variable cost component of the cost (involving the quantitiesq ij), as they know with
certainty how much it costs to run each of the facilities once active.
To solve this problem, we use a very useful result known asHoeffding’s Inequalitywhich
states the following for a sum of independent random variablesS n =X 1 +· · ·+Xn, where all
variables are bounded, that is,P(X i ∈[ℓ, u]) = 1. Then, we have5
P(S n −E[S n]≥ε)≤exp
 −2ε2
n(u−ℓ) 2

,(3.8)
The trick to use this bound is to express the objective value as a function operating on a real
valued function. We initially have a random vector for the demandsD= (D 1, . . . , DN ), given
a solutionx= (x 1, . . . , xM ) andq= (q 11, . . . , qM N) with cost vectorc= (c 11, . . . , cM N). The
value that we want to bound isE[cq ⊺]. The first observation is noting that for any solution, in
practice is should be the case that P i∈W qij =D j for all nodesj∈V. Then, by letting the
vector ¯c= (¯c1, . . . ,¯cN ) where ¯cj = ( P i∈W cijqij)/(P i∈W qij) forj∈V. In other words, the
vector ¯cj is the average cost to deliver to each location. With this, we havecq ⊺ = ¯cD⊺. Now
we can use Hoeffding’s inequality to build our cost bound. The function ¯cD ⊺ can be seen as
the generic random variableXin the inequality. The first step is to determine its bound. Note
that all demands are bounded below by 0, that is,ℓ= 0. Likewise, each demand is bounded
by above by ¯dj, then, all of them are bounded by ¯d= max j∈V ¯dj. Then, it follows that the
cost is bounded as ¯cD⊺ ≤ |¯c|¯d(we abuse notation by letting| · |be theL−1 norm for vectors.
For example,|¯c|= P j∈V |¯cj|). This norm|¯c|is bounded byNmax{c ij}where max{c ij}is the
highest possible cost, theNis simply the number of vertices in the graph. Then, the random
variableP(¯cD⊺ ∈[0, Nmax{c ij} ¯d]) = 1.
An i.i.d sample of the demand vectorDis represented as vectorsd k fork= 1, . . . , n, where
dk is a vector withNelements, the demand for each region. The sample expected cost is
5The more general version, states that when each random variable is bounded asP(X i ∈[ℓ i, ui]) = 1 the
denominator of the exponential is Pn i=1(ui −ℓ i)2 instead ofn(u−ℓ) 2.

41Instructor: Elioth Sanabria
thenE Pn[¯cD] =1 n Pn k=1 ¯cdk while the true cost is the expected valueE[¯cD]. Using Hoeffding’s
inequality we get that:
P(E Pn[¯cD]−E[¯cD]≥ϵ)≤exp
 −2n2ε2
n(Nmax{c ij} ¯d)2

,(3.9)
With 1−α= 95% probability, we get that the true cost is bounded by (solving forϵ):
E[¯cD]≤E Pn[¯cD] +Nmax{cij} ¯d
s
1
2n ln
 1
α

.(3.10)
This means that solving the problem with a sample ofnobservations is likely underestimating
the true expected cost due to the uncertainty caused by the number of geographical locations
N. To mitigate this uncertainty requires at least a quadratic increase in the sample sizen. In
the next section, we present a strategy to deal with solving an alternative optimization problem
that deals with the fact that the true distribution is in a neighborhood of the true distribution.
3.3.1 A reformulation using duality and optimal transport
Back in the first chapter, we defined both the actual expected value of a random variable and
their sample counterpart. A specially important random variable is the indicator function1 e
that is equal to 1 if eventeoccurs, and 0 otherwise.ecould be for example the event that today
rains, or that the demand exceeds a thousand units. The expected value of an indicatorE(1 e)
is equal to the probability of the eventP(e). And the sample estimate is the same as we defined
before, that is,p n(e) = 1 n Pn i=1 1{ei}. For example, the sample probability that the demand is
equal to 10, is the sample probabilityp n(D= 10) = Pn i=1 1{di = 10}/n. Sample probabilities
behave the same as expected values, that is, they converge to their true value if the distribution
is i.i.d.
For a random variableXtaking values in the setX(for example, in the case of the demand
random variableD, the demand takes values in the set of the natural numbersN), the collection
of sample probabilitiesp n(X=x) = Pn i=1 1{Xi =x}for allx∈ X, forms anempirical
distributionofX. This distribution is typically denoted byP n instead of the true probability
distributionP. The reader can already imagine that as the sample sizenincreases, the empirical
distribution will converge to the true one by the LLN, that isP n →P. It is also, expected that
the empirical distribution ofnobservations will overestimate the probability of some events,
while also underestimating others. In fact, since both probability distributions add up to 1, the
amount of overestimation is exactly the amount of underestimation (think of why this is the
case).
Given these facts, the methodology known asDistributionally Robust Optimization(DRO)
aims to incorporate the idea that the true distributionPof the data is within some neighbor-
hood of the empirical distributionP n. Here, neighborhood is taken as adistance metricbetween

Supply Chain Analytics: A data-driven approach42
the true and empirical distribution. LetDdenote a metric distance function between distri-
butions6. Then, we want to consider distributionsPthat are around the observed empirical
distributionP n within a distanceδ, that is, distributionsP:D(P n,P)≤δ. In plain terms,
a decision-maker acknowledges that their finite data samples might bias their estimates and
wants to optimize considering the case where the true distribution is in some neighborhood of
the empirical distributionP n, in this case, neighborhood means the set of possible distributions
that are in aballof radiusδaroundP n. The decision-maker picks the radius according the
their risk aversion (similar to choosingλin the previous examples). A larger radiusδmeans
less trust in the empirical distribution (for example, due to a low sample size) while a small
radius means that there is high confidence in the empirical distribution. See Figure 3.5 for a
conceptual representation of the DRO approach.
Demand
Prob
Zero Data
EmpiricalP n
(a) Sparse & Fragile
Demand
Prob
Risk recognized
RobustP∈ Pδ
(b) Spread & Robust
Figure 3.5: Comparison of fulfillment modeling. The empirical approach (left) ignores events
not present in the sample, leading toq ij = 0 for potentially critical regions. The DRO approach
(right) considers a distribution that spreads probability mass into those gaps, forcing the opti-
mization to allocate resources (q ij >0) for unobserved but plausible demand.
The DRO formulation can be set up in many ways. We will focus in a paradigm that uses
duality theory and optimal transport. To simplify the problem we will only consider variation in
the demand, that is, the costsc ij are assumed to be known and fixed. Moreover, the historical
(sample) demand is the matrixD n = (d k) fork= 1, . . . , n, wheredk is a vector with the
historical demands for eachi∈V, that is,d k is a vector of sizeN. Each of these vectors
is an i.i.d. sample of the vectorD. Denote the set of distributions withinδdistance of the
empirical distributions asP δ ={P:D(P n,P)≤δ}. Letx= (x 1, . . . , xM ). First, we re-write
the warehouse problem in this setting as:
min
(
˜cx⊺ + sup
Pδ
E[mincq ⊺|Aq⊺ +Bx ⊺ ≥(D,0) ⊺]
)
,(3.11)
This formulation is a matrix form re-write of the problem of interest that is going to be useful for
some algebraic manipulations that we are performing. For example, ˜cx ⊺ is equal to P i∈W cixi
6A distance metric is a functionD:M × M →Rthat operates on a setXwith the properties: For
p1, p2, p3 ∈ Mit is satisfiedD(p1, p1) = 0,D(p 1, p2)>0 forp 1 ̸=p 2,D(p 1, p2) =D(p 2, p1) for allp 1, p2 ∈ Mand
D(p1, p3)≤ D(p1, p2) +D(p 2, p3) which is the so-called triangle inequality.

43Instructor: Elioth Sanabria
andcq ⊺ = P i∈W P j∈V cijqij. The constraintsAq ⊺ +Bx ⊺ ≥(D,0) ⊺ are the usual constraints
of the problem, such as demand satisfaction, e.g. see the constraints in (3.5),Awould be
the matrix of coefficients multiplying theqvariables, while the right hand side is the random
demandDfor the demand satisfaction constraints and0for the constraints that only depend
on variables. The interpretation of the problem is quite similar: minimize the overall cost of
building the facilities, subject to the worst distributionP δ. Typically, the intuitive explanation
is that nature chooses the worst distribution givenx(the sup part) and then the optimization
chooses the optimal quantitiesq.
The first step to solve this problem is to re-formulate the sup by exploiting duality and
results from Transport Theory. LettingQ(x,D) = mincq ⊺|Aq⊺ +Bx ⊺ ≥(D,0) ⊺, we are going
to write the Lagrangian of sup Pδ E[Q(x,D)] (noting that the definition ofP δ is a constraint
defined by the distance of the distributions), for a pair of variablesP, λ:
sup
Pδ
E[Q(x,D)] = min
λ≥0
sup
P
{EP[Q(x,D)] +λ(δ− D(P,Pn))},(3.12)
The next step is to choose a distance metricDthat makes the problem tractable. One such
metric, is the so-calledWasserstein-1distance. Choosing this distanceD=W 1 has the following
property for any functiong(D):
sup
P
[EP[g(D)]−λW 1(P,P n))] =E Pn

sup
D
{g(D)−λ|D−D k|}

,(3.13)
WhereD k is a generic sample of the empirical distributionP n and| · |for vectors denotes
theL−1 norm. We can letg(D) =Q(x,D). The math behind the result is somewhat
technical and outside the scope of this section. By lettingg(D) =Q(x,D) and rearranging
minλ≥0 supP{EP[Q(x,D)] +λ(δ− D(P,Pn))}as min λ≥0(λδ+ sup P{EP[Q(x,D)]−λD(P,P n)})
combining the two equations yields:
sup
Pδ
E[Q(x,D)] = min
λ≥0

λδ+E Pn

sup
D
{Q(x,D)−λ|D−D k|}

,(3.14)
Which is great news as we know how to estimate expected values in the empirical distribution,
combining the original objective we get:
min
λ≥0
(
˜cx⊺ +λδ+ 1 n nX k=1 sup D {Q(x,D)−λ|D−d k|} ) ,(3.15)
RecallingQ(x,D) = min q≥0 cq⊺|Aq⊺ +Bx ⊺ ≥(D,0) ⊺, we can calculate the dual of this problem
as max η≥0 η[(D,0) ⊺ −Bx ⊺]|ηA≤c. Each of the terms sup D{Q(x,D)−λ|D−d k|}can be
then written as sup D{η[(D,0) ⊺ −Bx ⊺]−λ|D−d k|}. Exchanging the sup and the max and
isolating the terms depending on the vectorDyields:
max
η≥0,ηA≤c
−ηBx ⊺ + sup
D
{ηN D⊺ −λ|D−d k|},(3.16)
Whereη N are the firstNelements ofηcorresponding to the dual variables of the demand
satisfaction constraints of the warehouse problem. Next, define the variablev k =D−d k. The

Supply Chain Analytics: A data-driven approach44
inner problem sup D{ηN D⊺ −λ|D−d k|}can be re-written asη N d⊺ k + supvk {ηN v⊺ k −λ|v k|}.
The last term is the convex conjugate of theL−1 norm and is equal to 0 when|maxη N | ≤λ
or equal to∞otherwise. That it is equal to 0 is achieved by the constraints−1λ≤η N ≤1λ.
See Figure 3.6 for the intuition behind these constraints.
With this we can finally finish the rewrite of the problem as:
minλ,η,x
(
˜cx⊺ +λδ+ 1 n nX k=1 (ηN d⊺ k −ηBx ⊺) ) (3.17)
s.t.ηA≤c,−1λ≤η N ≤1λ,
λ≥0,η≥0, x∈ {0,1} M .
Which is almost a MIP except for the variablesηBx ⊺. The standard way of dealing with
this, is to define new variablesz ij =η ixj and add the constraintsz ij ≤ ˜M xj, zij ≤η i, zij ≥
ηi − ˜M(1−x j), zij ≥0 for a large enough ˜M(this is commonly known as the big-M method).
−3 −2 −1 1 2 3
Risk Penalty
ηN < λ
ηN > λ
v
y
Uncertainty Cost:λ|v|
(a) Cost of deviationv
−λ λ
Feasible Region
∞∞
ηN
f ∗(ηN )
Dual Constraint:|η N | ≤λ
(b) Shadow Price ”Discounting”
Figure 3.6: The relationship between deviation cost and shadow prices. In (a), if the shadow
priceη N (the marginal cost of demand) is steeper than the risk penaltyλ, the sup-problem
becomes unbounded. In (b), this translates to a hard constraint: the robust optimizer only
considers shadow prices ”discounted” within the [−λ, λ] interval, effectively capping the system’s
sensitivity to demand uncertainty.

Chapter 4
Scheduling Models
4.1 Introduction
Matching supply and demand is commonly referred to as an atemporal event, as if markets clear
instantaneously. Even in the most sophisticated financial markets, matching supply and demand
is far from an instantaneous affair where order matters and makes a significant difference in
the outcome. For example, the price difference between transactions can amount to very large
amounts of money in a matter of milliseconds.
In physical markets, the problem is even more pronounced. For example, in the warehouse
setting considered in the previous section, demand is fulfilled in a specific order that if not
properly optimized can lead to congestion, lost sales and waste of resources. Many of these
problems are very simple to describe but difficult to solve: the order of packaging boxes in a
warehouse, the order of manufacturing different products, or deciding the schedules of workers
to fulfill a productive activity.
Similar to other chapters when we studied the demand, scheduling can be studied as a
time-space matching problem. We start by studying what would be thespacevariant (which
could also be seen as discrete time). Then, we will move to consider the problem when time is
a random variable and finally consider both problems simultaneously in future chapters.
4.2 A set covering problem
A lot of scheduling problems take the form of an abstract problem: tocovera set at minimum
cost. Here, set can be understood in a general way as a demand that extends over either time
or space, and certain resources are available to satisfy it. For example, a fixed number of trucks
need to be assigned to cover deliveries in a city, or workers need to be assigned tasks to complete
a production process. Many of these problems are combinatorial in nature, meaning that finding
45

Supply Chain Analytics: A data-driven approach46
optimal solutions is in general hard, except in the simplest cases.
Like in previous chapters, we start with the simplest formulation that we will extend to other
special cases. Consider a demand vectorD, that like in previous chapters can represent the
demand for multiple locations or time-periods, the demand commonly has a task interpretation,
let the dimension of the demand vector beN. LetSbe a set of differentJschedules available
to fulfill some task. Moreover, define the matrixAwith dimensionsN×J, and elementsa ij = 1
if taskiis covered by schedulej. Letxbe a decision variable (a vector of sizeJ) in some space
of feasible assignmentsX(for example,X={0,1} J ). The scheduling problem normally takes
the form:
minf(x) (4.1)
s.t.Ax ⊺ ≥bE(D),
x∈ X.
See Figure 4.1 to see the structure of the problem.
a11 a12 . . . a1J
a21 a22 . . . a2J
... ... . . . ...
aN1 aN2 . . .aN J




Incidence MatrixA(N×J)
JSchedules (S)
NTasks x=

 x1 x2 ...
xJ


Decision V ectorx
(Selected Schedules)
≥ bE(D) =

 bE(D1) bE(D2) ...
bE(DN )


Demand / Bounds
(Time/Space OverD)
Multiply
Set Covering Constraint:Ax≥b(D)
Figure 4.1: Structural breakdown of the matrix-vector alignment in the set covering scheduling
formulation, where available schedules (S) map onto structural demands over a space-time
domain.
We illustrate next with a couple of examples the flexibility of this formulation.
Example 4.1(Shift Scheduling).A warehouse wants to schedule workers to process packages
in a 24 hour basis. Every hour, the warehouse has a demand of packages represented by a vector
D= (D 0, . . . , D23). The warehouse has a headcount ofHworkers that it has to allocate for
8-hour consecutive shifts. That is, there are possible 24 different shifts each starting every hour.
A worker can processbpackages per hour, therefore the need of workers is in expected value
bE(D). LetAbe a matrix with 24 columns and 24 rows and entriesa tj = 1 if schedulejcovers
hourt. Moreover, letxbe a vector withJ= 24 elements denoting the headcount of workers

47Instructor: Elioth Sanabria
assigned to each schedule. The manager wants to maximize the expected buffer between supply
and demand across all hours of the day.
The first step to solve the problem is to define the objective functionf(x). In this case,
the gap between supply and demand at every hour isAx ⊺ −bE(D), asAx ⊺ is the number
of scheduled workers every hour. Then, the minimum buffer between supply and demand is
v= min t{(Ax⊺)t −bE(D t)}. As we want to make this as large as possible,f(x) =−vachieves
the goal of increasing the gap between supply and demand as much as possible between supply
and demand. Finally, the constraint|x|=Hachieves the goal of assigning all workers (recall
that for vectors|x|= PJ j=1 |xj|). The final formulation results in the following MIP:
maxv(4.2)
s.t.Ax ⊺ −bE(D)≥v,
v∈R, x∈N J ,|x|=H.
As a follow-up, the business managers want to know instead the minimum amount of workers
such that they can cover their operation in expected value.
This can be achieved by modifying the functionf(x) to|x|, that we previously shown is the
total number of workers. Also, the constraint that represents that the demand is covered at all
hours in expected value isAx ⊺ ≥bE(D). Leading to the alternative formulation:
min|x|(4.3)
s.t.Ax ⊺ ≥bE(D),
x∈N J .
The last example can also be easily modified when each schedule has a cost vectorcassociated
to each entry ofx, and minimizingf(x) =cx ⊺. When the cost of all schedules is the same, or
the cost is proportional to number of hours (at the same rate), then the optimal valuex ∗ is the
same as the previous problem withf(x) =|x|.
4.2.1 Data Uncertainty
We revisit a technique in the warehouse allocation problem to deal with uncertainty in the data
matrixA. In the previous formulation. The matrixAhad entriesa ij = 1 whenever schedulej
is covering the period or locationi. The 1 has a direct meaning that every resource allocated
on that schedule is going tocertainlybe allocated. In real life this is rarely the case as there
are many occasions when an allocated resource might not fully work: in the case of people it

Supply Chain Analytics: A data-driven approach48
can be because of a curve of productivity (that is not uniform across all hours of the shift). In
the case of a machine it can be because of a failure that occurs with a small probability. Here
we provide a data-driven framework to deal with these kind of uncertainty:
Consider each row of the matrixAas a multi-variate normal random variablea i with mean
¯ai and covariance matrix Σ i. For example, in the productivity curve case where each hour
of the shift has their own productivity levela i ∈[0,1] J is a random vector with the different
productivity levels. The mean and the variance could be estimated from a sample size ofn
observations for example. Each constrain for the demand satisfaction can be transformed into
the probabilistic constraint:
P(aix⊺ ≥bD i)≥1−η,(4.4)
Assuming the demandD i is another independent random variable, the linear combinationaix⊺−
bDi is another random variable. The mean of this random variable is ¯a ix⊺ −bE(D i) and its
variance isxΣ ix⊺ +b 2Var(Di). Using the usual trick with the inverse of the normal random
variable trick seen in other chapters, we have thatP(a ix⊺ ≥bD i) is equal toP(Z≥ −(¯aix⊺ −
bE(Di))/
p
xΣix+b 2Var(Di)) or 1−P(Z≤ −(¯a ix⊺ −bE(D i))/ p xΣix+b 2Var(Di)). Making
the inequality equal toP(Z≤ −(¯aix⊺ −bE(D i))/ p xΣix+b 2Var(Di))≤η. Taking the inverse
cdf of the normal yields the equivalent constraint:
¯aix⊺ + Φ−1(η) p xΣix+b 2Var(Di)≥bE(D i),(4.5)
Thematically, this constraint follows a similar pattern through the book that hedging the risk
of allocating resources not only involves demand risk, but also the risk associated to allocating
the resources.
Next, we need to transform this constraint into a tractable formulation as the termxΣ ix⊺ is
not linear inx, thus, not directly a MIP. A powerful paradigm for these kind of problems is known
asSecond-order Cone Programmingor SOCP. Note that
p
xΣix⊺ +b 2Var(Di) is equivalent to
||(Σ1/2 i x⊺, p Var(bDi))||2, where Σ1/2 i is a matrix such that Σ1/2 i (Σ1/2 i )⊺ = Σi, for example, think
of Cholesky decomposition. Using this fact, the original scheduling program can be rewritten
as:
minf(x) (4.6)
s.t.−Φ −1(η)
  Σ1/2 i x⊺ p Var(bDi) ! 2 ≤¯aix⊺ −bE(D i) fori= 1, . . . , N,
x∈ X.
Whenf(x) is an affine function, this optimization program can be solved by a MISOCP solver.
This formulation is flexible to accomodate an interesting range of applications: for example, a
finite sample observation of ¯ai

49Instructor: Elioth Sanabria
Feasiblex
x1
x2
z= Gap F easible Region Boundary:
The “Gap” ( aixT −bE(D i)) must
be greater than or equal to the
scaled norm of the uncertainty
terms.
Figure 4.2: The Lorentz Cone representation. The vertical axis represents the supply-demand
gap, while the interior represents the feasible set for the SOCP constraint.
4.3 Production Scheduling
We change pace by describing a different kind of scheduling models closely related to closest
route problems, and that provide a useful : Suppose a production planning problem over a
horizon ofTperiods in the future. We start with the simplest case when the demand is known,
that is, at every period the demandsd 1, d2, . . . , dT are known in advance. Definec(s, t) as the
production and holding costs of periodss, . . . , tfors≤t∈ {0, . . . , T}(inclusive of all periods
in the range and the starting and endpoint) so that demand is satisfied exactly.
For example,c(0,4) includes the setup cost for production, plus the variable cost of produc-
ing for demandsd 1, . . . , d4 and the cost of storing the demand all the way to period 4 (starting
production at time 0). The key observation is that once this production is finished, starting
at period 5, the systemrenewsand the past production decision can be ignored. As an exam-
ple, this cost can be a setup costK 0 of starting production at period 0, plus a variable cost P4
t=1 v0(dt) and holding costsh 0(d1, . . . , d4) until the respective demand period. Then,c(0,4)
could be:
c(0,4) =K 0 +
4X
t=1
v0(dt) +h 0(d1, . . . , d4),(4.7)
Nonetheless, this is not the only possible specification for the costs. The important part is that
all these costs are deterministic and can be computed.
This structure of the problem allows us to use a powerful paradigm to solve the problem.
Letc(t) be defined as the minimum cost of meeting demand for periodst, . . . , T. Then, we have
the following recursion:
c(s) = min
t:t≥s
[c(s, t) +c(t+ 1)],(4.8)
This recursion implies a similar structure to a shortest-path-problem in a graph with nodes

Supply Chain Analytics: A data-driven approach50
V={0,1, . . . , T}and edgesE={(s, t) :s≤t∈ {0, . . . , T}}with distancesc(s, t). The
technique to solve the problem is to start withc(T+ 1) = 0, and solve recursively backwards
until arriving toc(0). The solution is a shortest-path between nodes 0 andTof the graph. Each
node visited represents the periods where production should take place. When the demands
are random and the costs have non-linearities. The model reduces to the dynamic inventory
management case studied in Chapter 2.
0 1 2 3 4 5
c(0,0)
c(0,1)
c(0,2)
c(0,3)
c(0,4)
c(1,1)
c(1,2)
c(1,3)
c(2,2)
c(2,3)
c(3,3)
c(3,4)
c(4,4)
Start (s= 0) T erminal (c(5) = 0)
Optimal Path Solution shown in Orange: Produce at Period 0 (covers
demands up to Period 2), then renew and produce at Period 3 (covers
up to Period 4).
Figure 4.3: Production scheduling mapped as a shortest path network over a horizon where
T= 4. Edge weightsc(s, t) represent setup, variable production, and holding costs. Visited
nodes on the optimal shortest path (highlighted in orange) signal the optimal periods where
regeneration takes place and production runs must occur.
4.4 A knapsack problem
Lastly, we cover a problem that while not necessarily deals with scheduling in a nominal way, it
is closely related as it deals with fitting objects in a limited space and can be interpreted in many
ways: for example choosing jobs to perform in a limited time, or choosing investments subject
a budget. This problem is known as theKnapsack Problem. The most common variations of
this problem can be formulated in the following setting. Imagine a knapsack (or a warehouse)
where a series of objectsi= 1, . . . , Nhas a profit or benefit expressed asfi(xi) and a capacity
of the knapsack consumedc i(xi)≥0. This capacity is assumed to be positive and increasing in
xi.x i ∈ Xeither expresses a quantity or indicator of how much of each object is used in the
knapsack. The objective is to pack the knapsack with the objects that have maximum benefit,

51Instructor: Elioth Sanabria
subject to not exceeding the total capacity of the knapsack.
max
NX
i=1
fi(xi) (4.9)
s.t.
NX
i=1
ci(xi)≤C,
xi ∈ Xfori= 1, . . . , N.
This is again a difficult combinatorial problem, as the greedy heuristics of sorting objects
with respect to the metricf i(xi)/ci(xi) might not lead to an optimal assortment of objects.
This problem can be solved in multiple ways: For example, the problem can be expressed
as a Mixed-Integer Program and be solved directly with solvers. Although, when the benefit
functionf i(xi) is non-linear this is not the case, see Figure 4.4 for an example.
0 1 2 3 4 5
0
40
80
120
Truck Threshold Penalty
fi(2) = 68
xi (Allocated Quantity)
fi(xi) Non-linear Profit with Capacity Threshold Discontinuity
0 1 2 3 4 5
0
5
10
15
ci(2) = 3.8
xi (Allocated Quantity)
ci(xi) Resource Capacity Overhead Curve
Figure 4.4: Visualizing a non-linear knapsack problem where the profit function incorporates
a structural step-down penalty. When the allocated allocation quantity crosses the threshold
(xi = 3), the sudden acquisition cost of an additional delivery vehicle drops total net profit
before marginal returns resume growth.
For a general benefit function, we present an alternative procedure to achieve the same

Supply Chain Analytics: A data-driven approach52
result. This procedure is calledforward-recursionorDynamic Programmingdepending on the
textbook. In fact, this is similar to the production example or the dynamic inventory model
presented in Chapter 2). First define the optimal benefit for a knapsack of capacityk≤Cusing
the firstj≤Nobjects:
Fj(k) := maxPj
i=1 ci(xi)≤k,xi∈X
 jX
i=1
fi(xi)
!
,(4.10)
The solution of the problem is by definitionF N (C). Now, the trick is again to create a one-step
recursion that relates these quantities to their predecessors (as we are going forwards instead of
backwards). This recursion is:
Fj(k) = max xj ∈X {fj(xj) +F j−1(k−c j(xj))},(4.11)
The intuition is clear: the maximum benefit of a knapsack of capacitykusing the firstjobjects
is equal to the largest benefit of the objectj, that is,f j(xj) plus the optimal benefit of a
knapsack using the previousj−1 objects with capacityk−c j(xj). The only thing left is to
define the boundary conditions to start the recursion. These can be defined as:
F0(k) =
(
0,fork≥0
−∞,fork <0. (4.12)
Then, the solution can be computed recursively by filling out the elementsF j(k) in a forward
fashion. The underlying assumption is that the capacity functionc i is a non-decreasing function
ofx i. And the number of operations is of orderO(CN|X |). See Figure 4.5 for a schematic of
the DP recursion.

53Instructor: Elioth Sanabria
0 . . . . . . . . . . . . . . .
... . . . ... ... ... ...
... . . . Fj−1(k−c j) . . . . . . . . .
... . . . ... ... ... ...
... . . . Fj−1(k) Fj(k) . . . . . .
... . . . ... ... . . . ...
0 . . . . . . . . . . . . FN (C)
0 j−1 j N
Stages / Time Steps (j)
0
k−c j(xj)
k
C
Available Capacity (k) Skip (xj = 0)
Pack (+fj )
Base CasesF 0(k) = 0
←Solution
FN (C)
Figure 4.5: Matrix representation of the forward-recursion Dynamic Programming state space
for the Knapsack problem. Columns represent sequential decision horizons (stages/time), while
rows represent the remaining sub-problem capacity. Computing the cellF j(k) evaluates the
maximum option between state transitions in stagej−1.

Supply Chain Analytics: A data-driven approach54

Chapter 5
Vehicle Routing Problems
5.1 Introduction
In previous chapters we have described matching the supply and demand in abstract sets,
either in the time or space domain. In this chapter we combine both into a single optimization
paradigm the optimization of both at the same time. The most common instance of this problem
is optimizing transportation routes for vehicles. In a practical sense, this is a key problem to
match supply and demand as the feasibility of the supply chain operation is not a given. For
example, how many vehicles are needed to transport X amount of material within a Y timeframe
is far from evident. Computationally, these belong to a family of problems that are hard to solve.
Similar to the set covering problems studied in the previous chapter, these are combinatorial
problems where time and space have to be allocated simultaneously.
While solving these problems to optimality is very hard, we will study some heuristic so-
lutions that will allow us to get feasible solutions in computationally tractable time. These
algorithms are a combination of the optimization algorithms that we have studied for ware-
house allocation, minimizing the traveling time while fulfilling the demand.
5.2 The Traveling Salesman Problem
The cornerstone of transportation algorithms is known as the Traveling Salesman Problem
(TSP), and it describes the following situation: imagine a salesman that has a list of locations
that they have to visit (as a side-note, the forefather of Operations Research in the U.S., Phillip
Morse, described himself primarily as a “salesman”, so in a way, everyone involved with Oper-
ations Research or Operations Management is in fact a kind of salesman, even unknowingly).
This salesman wants to visit the locations in an order that minimizes their cost in some way
(time, effort, transportation costs, etc).
55

Supply Chain Analytics: A data-driven approach56
Intuitively, the reader can already guess how a formulation would work: the objective func-
tion is to minimize a cost that will be associated to the specifictourthat the salesman will take,
subject to constraints on the validity of the tour. The challenge is then to express everything
in a single formulation.
Similar to previous chapters, we start by defining locations as vertices in a graphG=V, E,
with a collection of verticesV={1, . . . , N}and edgesE⊆ {(i, j) :i, j∈V}. As a first
primitive we consider the cost of traveling between nodesiandjasc ij. For example, this cost
can follow a similar structure to the warehouse location problem where it was dependent on
a random variableT i,j and a constant. Traversing the graph, can be uderstood as a tour, a
tourτ= (i 1, . . . , iN ) denotes a sequence ofNvertices that will be visited in that specific order:
starting ati 1 ∈V, then going toi 2 ∈V, and so on untili N ∈Vis reached where the tour ends.
Then, the objective in the TSP is to find a tour that minimizes the traveling cost.
A natural way to describe whether an edge belongs to the minimum cost tour in this graph
is to define a decision variablex i,j = 1 if edge (i, j) is part of the optimal tour and 0 otherwise.
Then, the only challenge left is to express the constraints that define what a valid tour is.
The first property is that from every edge there is only one entering edge and one outgoing
edge. Mathematically, this can be written as the constraints P i̸=j xi,j = 1 for allj∈Vand P
j̸=i xi,j = 1 for all nodesi∈V. To better visualize this, let the solution be stored in a
matrixX= [x i,j] where the elementi, jisx i,j. For example, consider the points in Figure 5.1
representing the optimal tour for 4 arbitrary points in a plane, and their corresponding solution
X.
1
2
3
4
(a) Optimal tourτ= (1,4,3,2) on an irregular
polygon.
X=

 0 0 0 1 1 0 0 0 0 1 0 0
0 0 1 0


(b) Corresponding adjacency matrixx i,j
Figure 5.1: Visualizing the relationship between a physical TSP tour on an irregular polygon
and its mathematical representation in the decision matrixX.
Enforcing the constraints that there is only one incoming and outgoing edge from every tour
is equivalent to making the matrixXrow and column sum to be equal to1. That is,1X=1
andX1 ⊺ =1 ⊺. With these, an initial formulation of the TSP minimizing the expected travel
cost is (lettingc i,i =∞to avoid solutions where a point goes to itself):

57Instructor: Elioth Sanabria
minE



NX
i=1
NX
j=1
xi,jci,j


 (5.1)
s.t.X= [x i,j], xi,j ∈ {0,1},
1X=1, X1 ⊺ =1 ⊺.
When solving this problem as is there are two possible outcomes: the first, is that the
problem results in a valid tour that will be optimal. The second, is that these constraints might
not be enough to enforce a tour that visits all points and the result might be a collection of
subtours that do not visit all points, see Figure 5.2 for an example of this situation.
1
3
4
2
5
6
(a) Disjoint Subtours:{1,3,4}and{2,5,6}
X=

 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 1
0 1 0 0 0 0


(b) MatrixXsatisfying assignment constraints
Figure 5.2: An example where the assignment constraints1X=1andX1 ⊺ =1 ⊺ are satisfied,
yet the solution consists of two disconnected subtours.
Clearly, the solution satiesfies the constraints we originally imposed, but it ended up produc-
ing two subtours instead of 1 tour that visits all the nodes. Here, the most practical approach
is to impose a constraint that after seeing this solution, imposes that the two subtours must
communicate with each other. In this example, letv s be an indicator vector equal to 1 if node
i belongs to subtours. For example, for the subtour composed by the nodess={1,3,4},
vs = (1,0,1,1,0,0). Likewise, 1−v s is an indicator of the nodes not belonging tos, that is
V\s. Enforcing that the subtoursis connected outside, amounts to the statement: make that
at least one of the outgoing connections insgoes outside it. The vectorv sXrepresents all the
connections starting atsandX(1−v s)⊺ means all the connections going to elements outside
ofs. Then, we can put both conditions together into a single expression and force that there
is at least one such connection fromsto outside it, that is,v sX(1−v s)⊺ ≥1. If we add this
constraint to our original formulation we end up with:

Supply Chain Analytics: A data-driven approach58
minE



NX
i=1
NX
j=1
xi,jci,j


 (5.2)
s.t.X= [x i,j], xi,j ∈ {0,1},
1X=1, X1 ⊺ =1 ⊺,
vsX(1−v s)⊺ ≥1.
After solving this formulation, we finally end up with a solution that not only yields a valid
tour, but it is the optimal one. See Figure 5.3 for the same instance of the previous problem with
subtours. The solution of adding all subtours as constraints is known as the Dantzig-Fulkerson-
Johnson formulation of the TSP (see [4]). Their algorithm would amount to add constraints
for all possible subtourss⊆V. Needless to say, this is an exponentially large set of constraints
that in real-life is rarely implemented as is. Instead, modern TSP solvers have a feature called
lazy constraintswhere the solver sequentially adds the subtour elimination constraints as they
emerge in the optimization process.
1
3
4
2
5
6
(a) Optimal tourτ= (1,4,2,6,5,3)
X=

 0 0 0 1 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0
0 0 0 0 1 0


(b) MatrixXwith Subtour Elimination
Figure 5.3: The optimal solution after imposingv sX(1−v s)⊺ ≥1. The matrix now represents
a single connected cycle visiting all six nodes.
If there is not access to a solver that can add these constraints automatically, the algorithmic
procedure is just to solve the problem sequentially and add constraints if the optimal solution
is not a valid tour that visits all the vertices. In practice, this procedure converges relatively
quickly. In Algorithm 3 we summarize the procedure.
The difference between this procedure and what the solvers do is that the solver can incor-
porate the new constraints while keeping the information of the branch and bound tree (in a
very simplified summary, MIP solvers solve a sequence of linear programs by sequentially adding
constraints to a “tree” of candidate solutions until an LP with an integral solution is reached).

59Instructor: Elioth Sanabria
Algorithm 3Subtour Elimination Algorithm
1:Input:CostsC, nodesV.Output:Optimal tourX ∗.
2:procedureTSP-Iterative(V, C)
3:S,K ← ∅
4:while|K| ̸= 1do
5:X ∗ ←argmin{ P ci,jxi,j :1X=1, X1 ⊺ =1 ⊺,S}
6:K ←DisjointCycles(X ∗)
7:S ← S ∪ {v sX(1−v s)⊺ ≥1|s∈ K}
8:end while
9:returnX ∗
10:end procedure
5.2.1 Incorporating Randomness and Risk Awareness
We can incorporate the techniques that we learned previously in the warehouse location opti-
mization Chapter 3 to incorporate randomness and create routes that are robust to variance in
the cost. A classical example is the case when the costc i,j is the random transportation time
Ti,j between nodeiand nodej. This is an important case because as we have seen, points that
have in expected value a smaller traveling time could potentially have a high variance which
could make some travels experience longer travel times. Which depending on the risk aversion
of the decision-maker could be possible unnaceptably long. For example, consider a medical
transportation problem where a patient needs to be picked up at their home and transported
to a hospital. The goal is to bring the patient as fast as possible while hedging the risk of a
potentially fatal longer travel. In general supply chains, time is always a tight constraint, where
products have to be delivered under strict delivery windows.
The first of these models is the same technique that we studied to solve a mean-variance
version of the problem. The variance of the sum PN i=1 PN j=1 xi,jci,j is equal to the same ex-
pression for the variance of a sum of random variables that we studied previously in Chapter 3
P
i,j∈V 2
P
k,l∈V 2 xi,jCov(ci,j, ck,l)xk,l, or more succintly,xCov(c)x ⊺ withxas the flattened vector
ofX(andcsimilarly defined). With these, the optimization problem can be stated as:
minE



NX
i=1
NX
j=1
xi,jci,j


 +λVar



NX
i=1
NX
j=1
xi,jci,j


 (5.3)
s.t.X= [x i,j], xi,j ∈ {0,1},
1X=1, X1 ⊺ =1 ⊺,
vsX(1−v s)⊺ ≥1.

Supply Chain Analytics: A data-driven approach60
Where the subtour constraints can be added on the fly as in algorithm 3 if they are random.
5.3 The Vehicle Routing Problem
We have explored and defined the problem with only one salesman, representing a single resource
like a vehicle, that must visit allNnodes. In this subsection we extend the formulation to
optimizeKvehicle routes. The simplest way to extend our original formulation is to add a
special node, numbered 0, representing a warehouse or depot where all vehicles depart to make
their routes and return once they have finished their assigned routes.
Given that each location still will be visited only once, we can try to retain most of the
structure of the problem that we have already studied. The only node that is going to behave
differently, is the depot node 0, as all vehicles will depart and return to the same location. The
number of vehicles departing and arriving to node 0 is exactlyK. That is, P j̸=0 x0,j =Kfor
the outgoing vehicles, and P j̸=0 xj,0 =Kfor the entering vehicles. Note that the number of
nodes is nowN+ 1 instead ofN. Similar to the previous section, this leads to a basic and
incomplete formulation, missing the equivalent of the subtour elimination constraints:
minE



NX
i=0
NX
j=0
xi,jci,j


 (5.4)
s.t.X= [x i,j], xi,j ∈ {0,1},
(K,1)X= (K,1),
X(K,1) ⊺ = (K,1) ⊺.
Similar to the previous section, solving this problem directly might result in one of two
outcomes: The first is that the optimization solves the problem and there is a valid assignment
ofKroutes where all vehicles have non-overlapping routes starting and ending at node 0. The
other, is that there might be isolated islands of customers that are not served from a truck that
departed from the warehouse. Theseghostislands that are not served from a truck, have again
to be connected to a truck that visits the depot. For example, see Figure 5.4 for an example of
this phenomenon. In this example there are two trucks that visit customes 1 to 4, but customers
5 and 6 are not visited.
Similar to the previous section, we can force the solver to eliminate the customer’s only
islands by adding subtour elimination constraints. In this case, the island of customerss=
{5,6}is represented by the the vectorv s = (0,0,0,0,0,1,1). Then, adding the constraint
vsX(1−v s)⊺ ≥1 to the original problem will eliminate that specific isolated island. Then,
after solving the problem with the new constraint might again have new islands, or yield a valid
solution that will be optimal.

61Instructor: Elioth Sanabria
0
1 2
3 4
5
6
(a) Two valid routes and one isolated island
{5,6}.
X=

 0 1 0 1 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 1 0


(b) MatrixXwithx i,j ∈ {0,1}.
Figure 5.4: The row/column sum for the depot is 2, but customers 5 and 6 are never reached
by a truck starting at 0.
We can apply the same strategy as in the TSP, to solve a formulation adding a subtour
elimination constraint to eliminate the islands. The algorithmic procedure to solve the problem
would be identical to the TSP, with the only change of changing the DisjointCycles subroutine,
to an IsolatedCycles one that instead detects the “customers only” islands generated by the
solution in the current step. The master problem is remarkably similar to the TSP one:
minE



NX
i=0
NX
j=0
xi,jci,j


 (5.5)
s.t.X= [x i,j], xi,j ∈ {0,1},
(K,1)X= (K,1),
X(K,1) ⊺ = (K,1) ⊺,
vsX(1−v s)⊺ ≥1.
As a final note, similar techniques for risk hedging can be applied to the same problem where
the shape of the covariance is remarkably similar.
5.3.1 On Capacities and Similar Issues
So far, we have studied algorithms that minimize a cost measurec i,j that is independent of the
routes and the vehicles. An avid reader might be rightfully asking questions about different
operational issues that happen with vehicles such as capacities, time-window arrivals and other
operational constraints. We present two schools of thought regarding these issues and present
our biased assessment of the right modeling approach.
We call the first school of thought the school of themasochists. This modeling school wants

Supply Chain Analytics: A data-driven approach62
to include in a single formulation all the constraints of the problem and through indicators,
counter variables and the big-M method ensure that the solution of the problem (however long
it might take, thus the masochism part) returns a feasible and optimal solution. Except in
the smallest instances, this approach tends to fail as the linear programming relaxation of the
resulting problem isweak. In the sense that the solver starts very far away from a set of cuts
that can even yield a feasible solution. An example of masochism is to try to formulate the
staff scheduling problem studied in Chapter 4 with modeling every single worker (out ofH)
with an indicator variable if workeriis active and hourtand try to brute-force the formulation
by writing a large number of constraints ensuring that the shift is no longer than 8 hours and
so on. Masochists are often limited by their own lifespan in their endeavor of trying to force
structure by enumeration and straitjackets. That being said, for small problem instances one
can get away with a formulation that gets the job done in a reasonable time.
The second school of thought corresponds naturally to thesadists. The sadists start with a
very lean formulation that often yields unfeasible solutions, and through a process of hammer-
ing down constraints, eventually a feasible solution is reached. The exposition in this section
corresponds to some degree of sadism in the formulation taste. The sadism comes from the
fact that the number of interations needed for the process to converge to a feasible and optimal
solution is uncertain. While there is some empirical evidence that when starting with astrong
formulation, the number of iterations to reach optimality, that is, of adding constraints (out of
exponentially many) consists of an unknown number of iterations, there is a proof that this will
always be the case. Moreover, the ultimate bottleneck is the inherent comobinatorial nature of
the problem.
The latter paradigm leads to an interesting strategy to deal with certain common patterns
in this type of problems. The first one is capacities. Normally, most vehicles are constrained
by a physical limit on their capacity, for imagine the case where all vehicles have a capacityC.
Going back to our usual exposition, imagine a vector of demandsD= (D 1, . . . , DN ) that needs
to be satisfied. After solving the VRP the resulting tour for each vehiclek= 1, . . . , Kisτk, or
the set of nodess k. Then, it could be the case that the sum of all the demands exceeds the
capacity of some vehicle(s)k. That is, P i∈sk E[Di]≥Cfor some vehicle(s)k, in which case
the solution is unfeasible. This kind of unfeasibility can be again tackled by the same technique
to eliminate the subtours that violated the feasibility of the TSP or VRP. The key observation
is that in the subset of nodess k in the tourτ k there are not enough vehicles to service their
cumulative required demand. The minimum number of vehicles that satisfies the demand is
m(sk) :=⌈ P i∈sk E[Di]/C⌉. Then, it must be the case that for this specific group of nodes, the
number of outgoing vehicles is at leastm(s k). The logic is that this enforces that at least this
amount of vehicles enters the specific subset of nodes. Then, the constraint that enforces this
condition is similarlyv sk X(1−v sk )⊺ ≥m(s k) for all vehiclesk.
The exact same algorithm for the TSP and VRP can be applied by addinglazy constraints

63Instructor: Elioth Sanabria
with an additional subroutine calledCapacityUnfeasibilitychecking the subsets of customers
that violate the capacity constraints and adding the constraintsv sk X(1−v sk )⊺ ≥m(s k) accord-
ingly, until feasibility is reached. On the capacities, they can be calculated as a number that
hedges the risk that the demand exceeds certain level as in the Newsvendor model in Chapter
2.
5.3.2 Time-window constraints: Column generation
A common business requirement in transportation problems is that deliveries have to be per-
formed at specific hours for certain clients. For example, transporting perishables or food
products often requires deliveries to occur during specific time slots. This is a challenging con-
straint to incorporate in our formulation as the temporal dimension is somewhat abstracted in
the decision variables and there is not a direct mechanism built-in to keep track of the times
the deliveries occur.
One might think to use the same approach of adding constraints to the main problem when
the deliveries do not occur at the specified time-window. This approach is not the strongest as
the constraints just force to shuffle the order of the tours, which amounts to a slow andthincut
in the geometry of the solution. In the capacity case, the cuts (of the feasible set) are stronger
as they force a minimum number of vehicles within a certain subset, which in subsequent runs
of the optimization problem greatly reduces the space of candidate solutions.
To make an interesting parallel, in the staff scheduling model in Chapter 4 the decision
variables were the number of resources (people) assigned to each of the possible schedules. This
was possible because the possible schedules were a relatively small set due to their structure.
The resulting formulation had a clean and direct interpretation. As we discussed in the previous
subsection, our modeling approach for the routes is equivalent to create indicator variables for
each of the workers and whether or not they are active during a certain hour. In hindsight, this
seems like a silly modeling choice when the cleaner formulation is known.
If we wanted to formulate the TSP with time-window constraints using the same approach
as the staff scheduling formulation we would set a problem to choose from a universe of routes
that already satisfies the time-window constraints, and then we would let the formulation choose
the one that minimizes the cost function. The formulation would look something like this:
minE
"X
τ∈Ω
cτ yτ
#
(5.6)
s.t.
X
τ∈Ω
aiτ yτ = 1,for alli∈V,
yτ ∈ {0,1}.
Ω represents all the tours where locations are visited on time (each locationi∈Vhas a time

Supply Chain Analytics: A data-driven approach64
window [si, ti] for arrival).a iτ is the indicator that tourτvisits locationi. The first constraint
represents that each location must be visited exactly once. Since all toursτin the set Ω are
feasible, that is, they visit the locations in their corresponding arrival windows. This problem
is ensured to find the optimal solution of the problem.
The issue is that in this case it is difficult to know beforehand the set of tours that are
feasible (in the staff scheduling case, the columns of the matrixAwere evident from the context
of the problem). The goal is then to generatecolumnsin this problem so that a feasible tour
that is optimal is found. Moreover, there are exponentially many of these columns, which makes
enumeration difficult.
Suppose that we are able to generate some routes that are feasible. The question is then,
how can we define a procedure to create new routes to eventually find an optimal one. Here, we
are going to use a technique that we used already in Chapter 4 to solve a dynamic programming
problem to generate new feasible (and better routes).
To build such a procedure, we need a way to peek into the structure of the problem to
get a numerical estimate on how to modify a route and then apply a similar logic to the
Knapsack iteration to build feasible routes that have lower costs. Duality offers an interesting
insight to build such estimate: Imagine that we solve the linear problem relaxation of the
formulation (with the constraints 0≤y τ ≤1 instead of the binary ones). By duality, each of
the constraints P τ∈Ω aiτ yτ = 1 has a corresponding dual variableπ i, the so-calledshadow price
of the constraint. In this case, the variable represents the increase in cost of adding locationito
a tour. When this increase is negative, it means that routes passing through that location reduce
the cost. Imagine for a routeτwith costc τ the corresponding dual prices in the relaxation are P
i∈V aiτ πi. Then, ifc τ < P i∈V aiτ πi adding this route will result in a reduced cost, because
in the current solution we areoverpayingto visit all the customers. Define the reduced cost ¯c τ
of a route as:
¯cτ :=c τ −
X
i∈V
aiτ πi,(5.7)
Routesτwhere ¯c τ is negative are good condidates to include in the main optimization problem.
When no such routes exist, we know that the optimal route is within the set of routes that we
have considered. Then, we have found an optimal route.
Next, we discuss how to generate feasible routes. As discussed before, this is hard on face
value, because just generating a route is a difficult combinatorial problem in itself. The structure
of the problem is in fact similar to theknapsackproblem studied in the previous chapter. We
defineF j(k) as the minimum reduced cost of reaching nodejin a valid tour arriving at timek.
As before, the key is to establish this recursion in a one-step way as:

65Instructor: Elioth Sanabria
Fj(k) = min i̸=j∈V {(ci,j −π i) +F i(k−t ij)},(5.8)
In principle, solving the Dynamic Program defined by this recursion should result in tours
cτ =F 0(k)<0 with negative reduced cost that in principle are candidates to be added to the
master program. The challenge is ensuring that at every step of the DP, the resulting tours
are cycle free and feasible. The first step in ensuring feasibility is that the tours respect the
delivery windows. This can be easily enforced asF j(k) =∞ifk /∈[s j, tj], that is,kis not in
the delivery window.
We initialize the DP with the boundary conditionsF 0(0) = 0 andF k(j) =∞for all other
j, k. In other words, the tours start at the warehouse at time 0 and all the other entries will be
updated as the DP recursion continues.
To populate the entries of the DP, we iterate on time fromk= 0, . . . , Tmax and through
the nodesj= 1, . . . , N. What can happen, is that for a given nodej, we might have visited
it before (at a time earlier thank) and also with lower reduced cost. Therefore it makes sense
that this is not a better tour than one we have found already. This can be stated in the updated
DP recursion:
Fj(k) =
(
mini̸=j∈V {(ci,j −π i) +F i(k−t ij)}ifF j(k)<min t<k Fj(t), k∈[s j, tj].
∞otherwise (5.9)
This updated recursion ensures that the resulting tours are prunned and non-improving tours
are not considered. We summarize the full algorithm in 4. In principle, once these columns are
generated, we can combine the procedure with the capacity variation to obtain capacitated and
time-window constraints.
As a last note, if the time windows are not very tight. There might be some resulting tours
with cycles. In this case, the simplest approach would be to eliminate them during the DP
recursion, by checking that at every step a node is not revisited in the lastℓsteps.

Supply Chain Analytics: A data-driven approach66
Algorithm 4Column Generation for VRPTW
1:Input:CostsC, nodesV, time windows [s i, ti], depot 0.
2:Output:Optimal set of routesy ∗.
3:procedureVRPTW-ColumnGen(V, C,[s, t])
4:Ω ′ ← {initial feasible routes}▷e.g., one route per customer
5:¯c min ← −∞
6:while¯c min <0do
7:Solve RMP Linear Relaxation:
8:min P τ∈Ω ′ cτ yτ
9:s.t. P τ∈Ω ′ aiτ yτ = 1,∀i∈V
10:Extract dual variablesπ i from coverage constraints.
11:(τ new,¯cmin)←PricingSubproblem(V, C,[s, t], π)
12:if¯c min <0then
13:Ω ′ ←Ω ′ ∪ {τnew}
14:end if
15:end while
16:y ∗ ←solve-MIP(Ω ′)▷Solve withy τ ∈ {0,1}
17:returny ∗
18:end procedure
19:procedurePricingSubproblem(V, C,[s, t], π)
20:Find routeτminimizing ¯c τ = P (i,j)∈τ (cij −π i)
21:s.t. Arrival i ∈[s i, ti] for alli∈τ
22:returnτ best,¯cbest
23:end procedure

Chapter 6
Systemic Demand Uncertainty and
Chain Effects
6.1 Introduction
Supply chains are complex networks composed of entities that order and selsl products: for
example a reseller or a distributor orders from a factory and resells product to other customers,
that in turn might be further reselling or be final customers. In our exposition we have empha-
sized on the random nature of the demand. In this chapter we study quantitatively how risk
propagates in a supply chain network.
Intuitively, when producing or selling a product, the optimal behavior is to produce/order
the average plus a buffer to cover for the variance of the demand depending on its distribution
according to the profit structure of the business in an optimal way. In a supply chain, the risk
propagates andbubble-upthroughout the network, making the risk of a stockout higher. Lead
times, that is, the time orders take to be fulfilled also adds a layer of propagation of risk that
could affect the supply chain adversely. We formalize these insights into a powerful paradigm
(based on Stochastic Networks theory, see§7.3 [3]) that will allow us to study these effects in
detail quantitatively.
6.2 Basic Model
To start, consider a single business buying/producing certain product and selling it to many
different customers (potentially other businesses), all participants constitute a network withN
nodes. As we studied in Chapter 2, when the demand is normally distributed (which in this
67

Supply Chain Analytics: A data-driven approach68
case simplifies the analysis greatly), the optimal quantity for a businessiis to order a quantity:
qN V i =µ i +z iσi,(6.1)
Whereµ i is the average demand,σ i is the demand standard deviation andz i = Φ −1(ρi) is
the optimal factor in the Newsvendor model, whereρ i is the critical ratio given by the profit
structure in the objective function (for exampleρ i = (pi −c i)/pi in the plain vanilla specification
in Chapter 2.2).
Nodeihas an average demandµ i that needs to be satisfied in equilibrium as:
µi =
X
j
pijqj +v i,(6.2)
Whereq j is the effective quantity produced by nodejandp ij ∈(0,1) is the proportion of
the demand ofjproduced by nodeiandv i is the external average demand. Then, assuming
independence between the nodes (here the variance is assumed exogenous from the external
demand), the varianceσ 2 i is equal to:
σ2 i = X
j
p2 ijσ2 j +w 2 i ,(6.3)
Wherew 2 i is theexternal varianceof the demand (which can be 0 if nodeidoes not serve an
external demand). Then, the effective quantity that nodeineeds to produce is given by:
qi = min

X
j
pijqj +α i, Ci

 ,(6.4)
Whereα i =v i +z iσi. When the constraint holds with equality, this is the optimal quantity
according to the Newsvendor model (asq i =µ i +z iσi = P j pijqj +α i) or the maximum physical
capacityC i of nodei. Since this is true for all nodes in the network, then, the maximum flow
of product in the supply chain network is obtained by solving the following LP:
max|q|(6.5)
s.t. (I−P)q ⊺ ≤α ⊺,
0≤q≤C.
WherePis a sub-stochastic matrix with entriesp ij andαis a vector with entryiequal to
αi =v i +z iσi. For most nodesv i andw i will be assumed to be 0 (think of producers/resellers
that do not sell directly to consumers) and it will be positive for retailers (or nodes that face
external demand directly).Cis a vector with entryiequal toC i, the capacity of that node. In
Figure 6.1 we see an example of a supply chain network with a producer, resellers and retailers.
To solve the problem there are multiple strategies: the simplest one is to solve directly the
LP obtaining a solutionq ∗ for the maximum flow of product. Since there areNnodes, a basic
feasible solution of the problem will have exactlyNbinding constraints in the optimal solution

69Instructor: Elioth Sanabria
Producer (1)
Reseller (2) Reseller (3)
Retailer (5)Retailer (4) Retailer (6)
p12 p13
p24
p25 p35
p36
p45, p54 p56, p65
v4 v5 v6
Model V ariables:
qi: Production Quantity
Ci: Capacity
pij: Flow Proportions
vi: Avg External Demand
αi:v i +z iσi
Figure 6.1: Example of a supply chain network with a single producer (represented by a node
1), 2 resellers (nodes 2,3) and 3 retailers (nodes 4,5,6) that potentially sell to each other as well
as servicing the external demands (v 4, v5, v6).
(ignoring potential degeneracies). For example, for the constraintsq≤Cthe nodes will be
divided into two sets: one set of nodesU⊆ {1, . . . , N}that will be producing at capacity
qU =C U , these nodes areun-hedgedagainst the risk implied by the Newsvendor model. In
other words, they are limited by their capacity and with a non-negligible chance might suffer
a stock-out of product. Conversely, the other set of nodesH={1,· · ·, N} \Uis producing at
the maximum possible given the external demand and the structure of the network.
Then, the other flow constraints should hold with equality for the other variables, that is,
(IH −P H)q⊺ H + (IH,U −P H,U )C ⊺ U =α ⊺ H. Which simplifies toq ⊺ H = (IH −P H)−1(α⊺ H +P H,U C⊺ U ).
Then, it must be that the optimal is given by:
q⊺ U =C ⊺ U , q ⊺ H = (IH −P H)−1(α⊺ H +P H,U C⊺ U ).(6.6)
The optimality of this solution can be verified using duality checking that the solution satisfies
the complimentary slackness conditions.
More importantly, the solution highlights the structure of the problem: namely, some nodes
will be capped by their capacity and will not be producing enough to optimally hedge their risk.
6.2.1 The bullwhip effect and other sensitivities
In the supply chain literature there is an empirical principle known as thebullwhip effect. The
bullwhip effect is the downstream increase in demand throughout the supply chain network

Supply Chain Analytics: A data-driven approach70
caused by an increase in customer demand, which in turn ripples increasingly throughout the
network.
In our model this and other effects can be quantified, we will see that the bullwhip effect is
not only caused by increases in demand, but it is also exacerbated by the structure of the supply
chain network and how it also propagates the variance of the external demands. The first step
is to calculate the sensitivities, which is a fancy name for the derivatives of the solution with
respect to some variables. The sensitivity with respect toα i (capturing both the sensitivity to
the demand and the volatility) is given by:
∂qH
∂αi
= (I H −P H)−1e⊺ i fori∈ H,(6.7)
∂qH
∂Cj
= (I H −P H)−1PH,U e⊺ j forj∈U.(6.8)
Wheree i is a basis vector with entryiequal to 1 and the rest equal to zero. In both sensitivities,
we can see the role of the matrix (I H −P H)−1. This matrix is commonly called thenetwork
multipliermatrix. Intuitively, recall that for a geometric series we have the well known result:
1 +δ+δ 2 +δ 3 +· · ·= (1−δ)−1,(6.9)
Which is true as long as|δ|<1, which intuitively means that the termsδ k fork→ ∞not
only decrease to 0, but their order of magnitude vanish as the partial sum goes to infinity (the
mathematical notion of convergence of a series). Imagine the following situation to get some
intuition: An oil producer, generages a quantityq=D+ 5%qof oil, that is, their external
demandDplus 5% of their own output that they consume to re-refine the oil. Rearranging
the terms yieldsq= D 1−5% =D(95%) −1. The total quantity is the demand multiplied by a
feedbackfactor (95%) −1 ≈105.3%. This can be seen as a feedback loop in the production
caused by output that reenters the production process. The same happens in a network case
with matrices, where we have that:
I+P+P 2 +P 3 +· · ·= (I−P)−1,(6.10)
It is also expected that for the result to hold, the higher powers ofP k go to 0 ask→ ∞and
vanish from the partial sums. Luckily, this holds true for substochastic matrices in our base
model1. Moreover, the same intuition applies, each product of the matrix can be seen as a
feedback loop of an increase of the required production coming from neighboring nodes, that
in turn increase the production requirements for their neighbor nodes. This back and forth
stabilizes in the form of multipliers (like in the above paragraph example of (95%) −1), and
the entries of (I H −P H)−1 represent exactly the multiplier of node in a row to a node in a
column. That is why the sensitivity (I H −P H)−1e⊺ i is the row sum of of all columns entering
1In general, what is required for the result to hold is that the largest eigenvalue of the matrix is less than 1
in absolute value.

71Instructor: Elioth Sanabria
into nodei∈ H. Likewise, the sensitivity (IH −P H)−1PH,U e⊺ j represents the weighted (byP H,U )
multipliers of the hedged nodes into the unhedged ones.
By the chain rule, it is straightforward to calculate the effect of a change in the demand as
∂qH
∂vi = ∂qH ∂αi ∂αi ∂vi and ∂αi ∂vi = 1 recallingα i =v i +σ izi. Therefore, ∂qH ∂vi = (I H −P H)−1e⊺ i is the
same sensitivity as before.
The bullwhip effectis known as the empirical phenomenon when an increase of the
demand ripples with increasing magnitude accross the supply chain. With our framework, we
can study permanent increases in the demand, as well as increases in the volatility that as we
will see, quantitatively ripple differently in the network. Suppose, the demand in one of the
customer facing nodes increases, that is,v i increases for some nodei. We are then interested
in quantifying the impact of this increase in the demand.
To make the analysis easier, suppose the structure of the network is as follows: the graph
is an acyclic directed graph and the matrixPis substochastic, where nodes are ordered in a
way that they provide their output to nodes numbered higher than them. For example, in the
graph in Figure 6.1 the node 1 represents a producer, which supplies their output to the reseller
nodes 2 and 3. In turn, node 2 sells their output to retailers 4 and 5, and node 3 sells to 5 and
6. Note that the retailer nodes, 4 sells to 5, and 5 sells to 4 which violates our assumption. So,
imagine the same network, but without node 5 selling to 4 and withouth 6 selling to 5. Later
we will see that this is not really a necessary condition, but it makes the next argument easier
to explain.
Imagine there is a permanent shock to the demand in a node that increases it to a new
level, for example, in the graph in Figure 6.1 without the cycles, imagine that node 6 demand
increases to a new levelv ′ 6 =v 6 +ϵfrom the previousv 6. This increase affects first node 6,
which increases their production by an amountϵ. Next, the nodes that are affected are nodes 3
(a reseller) and 5 (another retailer). These in turn increase their demand by a magnitudeϵp 36
andϵp 56 respectively. This continues happening so forth throughout all the network (and note
that sometimes the effect will go forward again, as after node 3 increases their production, so
will the output that node 5 does).
A way to analyze this effect numerically, is to look at thenetwork multipliers. Moreover,
suppose that all nodes have infinite capacityC i → ∞, so that all nodes are producing at their
hedged level, so thatq= (I−P) −1α⊺. Since the network is free of cycles, the multiplier matrix
(I−P) −1. The multiplier effect of a shock in nodejinto nodeiis the element [(I−P) −1]i,j.
In the expanded form this is:
[(I−P) −1]i,j =I i,j +P i,j +P 2 i,j +· · ·+PN−1 i,j ,(6.11)
First note that there areNelements in the summation, as there no longer thanNsteps
between 2 nodes. Next, see that each term exactly reflects how an increase in the demand
travels throughout the network. The first node affected isI i,j that will feel the full effect only

Supply Chain Analytics: A data-driven approach72
ifi=j(for example, the node 6 in the previous paragraph). Next, the effect is the nodes that
can be reached by one stepP i,j (the nodes 3 and 6). Next, the ones that can be reached exactly
in two stepsP 2 i,j, in 3 stepsP 3 i,j and so on (in fact, the same analysis holds for matrices with
cycles, instead ofN+ 1 there is a large enough termKfrom which further terms vanish).
This is exactly what the bullwhip effect is, nodes that are directly affected see a lower order
of magnitude effect, than deeper nodes (producers or reseller) as the shock is transmitted and
amplified throughout all the network.
6.2.2 Volatility Propagation
In the literature the Bullwhip effect is also associated to the propagation of variance throughout
the supply chain (affecting again the innermost nodes rather than the consumer facing ones).
In our model this mechanism is captured by the structure of the variance. We can write the
variance Equation in (6.3) as:
(σ2)⊺ = (P⊙P)(σ 2)⊺ + (w2)⊺,(6.12)
Whereσ 2 = (σ2 1, . . . , σ2 N ),w 2 = (w2 1, . . . , w2 N ) and⊙is the element-wise product of two matrices
of the same dimension, such that thei, j-th element of the matrix (P⊙P) isp 2 ij. The equation
becomes (I−(P⊙P))(σ 2)⊺ = (w2)⊺, or:
(σ2)⊺ = (I−(P⊙P)) −1(w2)⊺.(6.13)
This expression should be already familiar from the previous exposition. The matrix (I−(P⊙
P)) −1 is again a multiplier, but this time of the variance, denote asMσ = (I−(P⊙P)) −1. Similar
to the previous case, this shows how the variance of the external demandw 2 propagates inside
the network. Taking element-wise square root in both sides yields the equivalent expression
σ⊺ = p Mσ(w2)⊺.
The change in the variance of nodes by a change in the external demand standard deviation
wj in nodejis given by:
∂σ ⊺
∂wj
= diag

1/
p
Mσ(w2)⊺

mjwj,(6.14)
Wherem j is a column vector ofM σ. Then, we can finally express the sensitivity of the demand
with respect to changes in the external variance. We have by the chain rule that ∂qH ∂wi = ∂qH ∂αi ∂αi ∂wi
and in turn ∂αi ∂wi =z i ∂σi ∂wi =z i mii√ Mσ(w2)⊺ i wi or:
∂q ⊺ H
∂wi
= (IH −P H)−1e⊺ i
"
miip
Mσ(w2)⊺ i ziwi
#
.(6.15)
The intuition is quite interesting: on one hand there is a network multiplier effect as before, but
there is a further variance multiplier effect (in square brackets) that further exacerbates a shock

73Instructor: Elioth Sanabria
to the standard deviation of the external demand. Note that the shock is also proportional to
the current standard deviationw i, accentuating shocks even further.
Outdated interpretations of the Bullwhip effect attribute it to the lack of information and
coordination between nodes or noise coming from forecasting and lead times. Suggesting that
the lack of better information systems is the main reason behind the bubbling-up of demand
shocks.
In this chapter we showed mathematically that even with perfect information and coordina-
tion (all the nodes in the network can see the production quantities and uncertainty of adjacent
nodes),the Bullwhip effect is an unavoidable and an inherent topological property
of supply chain networks. Even in the perfect information case, with instantaneous order
fulfillment, hedging against risk implies the Bullwhip effect.
Example 6.1(Rare earth supply chain).A supply chain network composed of a producer
(node 1) and a seller/country (node 2). The external average demandv 2 = 100 tons per year,
the external standard deviation of the demandw 2 = 10 tons. The seller buys all of its product
from the producer, that isp 12 = 1, the routing matrix is:
P=

0 1
0 0

 ,
With a safety levelz 1 =z 2 = 1.645 what are the optimal production quantities in this network?
While maintaining the same average demand, how much an increase of 1 ton of the standard
deviation of the demand increases the quantities for the producer?
For the first question, we have the following quantities:
q2 =v 2 +z 2w2 = 100 + 1.645(10) = 116.45
q1 =p 12q2 +z 1
q
p12σ2 2 = 116.45 + 1.645(10) = 132.9
Even when the network only has 2 nodes, the producer has to produce way above node 1 to be
optimally hedged against the demand fluctuation of the seller.
For the second question, we make use of the network multiplier matrix:
(I−P) =

1−1
0 1

 ⇒(I−P) −1 =

1 1
0 1

 ,
Also note thatP=P⊙P, then the network multiplier matrix (I−P) −1 and the variance
multiplierM σ are the same. For node 1 we have that the sensitivity is:
∂q1
∂w2
= [(I−P) −1]1,2 ×
 m22
σ2
z2w2

= 1×
 1
10 1.645(10)

= 1.645 (6.16)

Supply Chain Analytics: A data-driven approach74
Then, an increase of the demand volatility by 1 ton increases production by 1.645 tons in the
producer node.
6.3 Dynamic Model
In practice, knowing only the new equilibrium quantities is important, but also the timing on
how the network adapts to shocks and their magnitude. In this section we extend our model to a
dynamic setting to answer questions related to the timing and magnitude of theBullwhip effect
and other shocks. The standard way to incorporate a dynamic version, is to solve a so-called
Skorokhod Problem(see [8]).
Consider the evolution of the inventory if there are no capacity constraints, a so-calledfree
inventory process:
Xi(t) =Z i(0) + (Productioni −Internal Demand i −External Demand i)t,(6.17)
WhereZ i(0) is an initial level of inventory (not to be confused by the safety marginzi). Call the
expression in parenthesisθ i showing the net-rate that the inventory changes. In matrix-form,
the free inventory process can be written as:
X(t) =Z(0) +θt,(6.18)
In this case,θ=C−α−(λ∧C) as the maximum production capacity of a node is their capacity,
that is,λ≤C, recallingC= (C 1, . . . , CN ).θ i denotes the rate the inventory increases ifθ i >0
or decreasesθ j <0, eventually reaching 0. Letλbe the effective production rate of each node.
LetZ(t) be the actual inventory process. As the inventory cannot be negative, that is,
Z(t)≥0, the Skorokhod problem trick is to create a functionY(t) that cancels out when the
inventory is negative. As this must happen for all the nodes we have the relation:
Z(t) =X(t) +Y(t)−Y(t)P=X(t) +Y(t)(I−P),(6.19)
In this case,Y(t) appears first as it is cancelling out whenX(t) is negative, but it also must
account when other nodes have a shortfall that affects nodei, therefore the need for the term
−Y(t)P, or− P j Yj(t)pji. This keeps track of the propagation when other nodes have shortfalls,
which is a mathematical way of tracking the contagion between nodes.
It must also be the case that whenZ(t)>0, thendY(t) = 0, because there is still enough
inventory to satisfy incoming orders. Likewise, whenZ(t) = 0, thendY(t)>0, meaning
that there is not enough production capacity to satisfy the demand. All the conditions can be
summarized in the program:
Z(t) =X(t) +Y(t)(I−P),(6.20)
s.t.Y(0) = 0, ˙Y(t)≥0, Z(t)≥0, Z(t) ˙Y(t) = 0.

75Instructor: Elioth Sanabria
Where ˙Ydenotes the time derivative ofY, that is, ˙Y(t) =dY(t)/dt. In the long term, it must
be the case that the equilibrium of the dynamic model is the same as the static one. To see
why, first considering the case where all the production capacities are large enough so that any
production level is possible. In this case, the evolution of the system is given by the equation:
˙Z(t) = ˙X(t) + ˙Y(t) =θ+ ˙Y(t)(I−P),(6.21)
IfZ(t)>0 ends in a positive level, thendY(t) = 0. Likewise, ifZ(t) reaches an equilibrium
point, thendZ(t) = 0. Leading to the equation:
0 =θ=C(I−P)−α⇒
C=λ
λ=α(I−P) −1,(6.22)
Whereλrepresents the effective production rate of each node. In the limit, this is the same
production quantity that we derived in the static case. That is lim t→∞ λ(t) =q ∗. In practice,
we will see that because of their physical capacity, some nodes will be unable to produce their
required quantity and they will be again partition into disjoint hedgedHand un-hedgedU
nodes. In the case where nodes hit a capacity limit, this refines to the so-calledflow equation:
λ=α+ (λ∧C)P,(6.23)
Where∧is the element-wise minimum operator. Whenλ∧C=λthe previous equation holds.
Following our previous analysis, at any pointtthe nodes are divided into two disjoint sets
of hedgedHand un-hedgedUsets. For a given timetthat nodes are divided into hedgeHand
un-hedged setsU. Then, the flow Equation 6.23 refines to:
λH =α H +λ HPH +C U PU,H,(6.24)
λU =α U +λ HPH,U +C U PU ,(6.25)
Solving yields the following flows at timet:
λH = (α H +C U PU,H)(I−P H)−1,(6.26)
λU =α U + (αH +C U PU,H)(I−P H)−1PH,U +C U PU ,(6.27)
Note that as time moves forward, the set of hedged nodes might decrease as a result of increased
demand. The rates the inventory is accumulated are given by:
θ=C−α−(λ∧C)P=C−λ(6.28)
6.3.1 Sequential dynamics
In principle, we have all the ingredients to describe the evolution over time of the supply chain
network. The nodes start att= 0 with some inventory positionZ(0)≥0 with production rates
λ(t) dividing the nodes into disjoint setsH(t) andU(t). Suppose, the sets are initially known

Supply Chain Analytics: A data-driven approach76
as well, that isH(0) andU(0). Then, we just need to describe the evolution of the system until
the timeτwhen the sets change (possibly because a set of nodes had to increase production
until a time that their production limit is reached). When that timeτis reached we can just
restart the clock and simulate the system again.
The evolution of the system is linear between time 0 and the time where the sets of nodes
change. For all nodes already at capacityZ U (0) = 0 andZ H(0)>0. We also have the following
dynamics for the hedged nodes:
ZH(t) =Z H(0) +θ Ht+Y U (t)(I−P U,H) (6.29)
WhereY U (t) = (λU −C U )tandθ H =C H −λ H.
The system keeps evolving linearly according to these dynamics until the timeτwhere a
node in the setHcannot satisfy all their production obligations. This time is given by:
τ= min
j∈H,θj <0
 Zj(0)
−θj

,(6.30)
This follows from the fact that a node inHwithθ j <0 implies thatC j < λj, meaning that
even at maximum capacity they will eventually reach their production limit. This will happen
whenZ j(0) +θ jt= 0 or att=−Z j(0)/θj.

Chapter 7
Queueing Models
7.1 Introduction
In this chapter we continue studying operations in the time dimension. For example, in a
production activity or a warehouse operation, the order that tasks are performed affects the
final result. For example, in a production line, some stations might process jobs faster than
others, and the throughput will be affected by how the production line is configured. In a
warehouse operation, when many trucks arrive at the same time, the number of loading stations
and workers will affect the effective throughput of the operation. Knowing how to assign and
configure manufacturing systems to be faster and more resilient is a key strategic tool to develop
supply chain operations.
Mathematically, we leverage our study of networks and probabilistic theory to describe
common problems in queueing systems.
7.2 A network view of a queueing system
Queueing systems are defined as a probabilistic system where jobs, customers or tasksevolve
inside a well limited system: for example, a production line queue, cars passing through a bridge
or a flower plantation.
The primitive unit in all these systems is the number of jobs (or customers, tasks, etc) in the
system. At any timetthe number of jobsN= 0,1,2, . . .is a unique value, this feature makes
us think that in time-homogeneous systems (the arrivals, processing and departures are time-
independent), we can think of a probabilistic distribution of observing the number in system as
a proportion of time:
πi := lim t→∞
Z t
0
1{Xs =i}
t ds(7.1)
77

Supply Chain Analytics: A data-driven approach78
WhereX t is the stochastic process counting the number in system at timet.
The time-homogenous process by excellence is the Markov Chain. We previously studied it
in Chapter 2. In fact, this is the same definition of stationary distribution that we described
in the study of inventory processes. Then, it is a reasonable goal to define a type of Markov
Chains that can model manufacturing processes. The main class of Markov Chains used to
model manufacturing processes are known asContinuous Time Markov Chainsor CTMC. The
simplest way to construct such chain requires two ingredients: First, a transition matrixP
between statesN, with elementsp ij denoting the probability of transitioning from stateito
statej. Second, an average time the chain stays in a state that is also time homogeneous.
For a random timeTto be time-homogeneous it is necessary that for anys, t≥0, we have
P(T≥t) =P(T≥t+s|T≥s). Meaning that the tail CDF is the same regardless of time-shifts.
Using Bayes’s rule and rearranging yields the relation:
P(T≥t)P(T≥s) =P(T≥t+s) orR(t)R(s) =R(t+s),(7.2)
When definingR(t) :=P(T≥t). Then, the goal is to find a distribution that satisfies this
property. This implies that for ∆t=t/kwe haveR(t) =R(∆t) k. In the discrete case,
P(T≤i) = 1−R(i+ 1) and alsoR(i+ 1) =R(1) i+1. Putting these two relations together
yieldsP(T≤i) = 1−R(1) i+1, letting 1−p=R(1), we will call this ageometric distribution.
In the continuous case, something very similar can be done. For example,R(t) =R(1) t.
Changing the base of the exponential1 we haveR(t) =R(1) t =e tlnR(1) . Lettingµ=−ln(R(1))>
0 we have a distribution with tail cdfR(t) =e −µt, we call this distribution theexponential dis-
tribution. See Figure 7.1 for a visual representation of the survival probabilities.
Having sorted out the time-homogeneous aspect of the average time in a state (what we
need to do is simply calibrate the parameters of the discrete geometric distributionpor the
exponentialµso that they match a target expected value). For example, in the exponential
distribution case, we have that the average time in a statei, denoted asT i is equal toE(T i) = R ∞
0 e−µitdt= h − 1 µi e−µit i∞ 0 = 1/µi.
Now, we can think of a very small time interval ∆tand think of the transition probability
Pij(t) of our Markov Chain where time passes continously. The first observation, is that from
the memoryless property the probability of leaving a state is a constant times the time interval,
for example, in the exponential case this isµ i∆t. Therefore, the probability of staying in the
same state is 1−µ i∆t. If we extend this logic to all the states, we end up with this relation:
Pij(t+ ∆t)≈P ij(t)(1−µ j∆t) +
X
k̸=j
Pik(t)(pkj µk∆t),(7.3)
The interpretation of this equation is that at timet+ ∆tone of two outcomes occured: first,
the chain simply stayed at statej. Or second, the chain transition to other state k, left that
1x=e logx , thenx t =e tlnx .

79Instructor: Elioth Sanabria
0 s s+t0
0.5
1
Intervals Intervalt
R(s+t)
R(s) =R(t)
Ratio is invariant
to the shifts.
Time (t)
Survival ProbabilityP(T > t)
Continuous: Exponential T ailR(t) =e −µt
0 s s+k0
0.5
1
Stepss Stepsk
R(s+k) =R(s)R(k)
Each step drops by
a constant factor (1−p).
Steps (k)
Survival ProbabilityP(T > k)
Discrete: Geometric T ailR(k) = (1−p) k
Figure 7.1: The visual architecture of memorylessness. The continuous Exponential curve (left)
and discrete Geometric bars (right) represent the unique configurations where the relative re-
maining lifetime layout above a survival milestonesmaintains a constant, self-similar proportion
directly identical to the original starting profile at point 0.
state (with probabilityµ k∆t) to statej(with probabilityp kj ). Rearranging this term, we get:
Pij(t+ ∆t)−P ij(t)
∆t ≈ −Pij(t)µj +
X
k̸=j
Pik(t)(pkj µk),(7.4)
Which is the definition of the derivative (or change) when ∆tis small, leading to the equation:
dPij(t)
dt =−P ij(t)µj +
X
k̸=j
Pik(t)(pkj µk),(7.5)
When grouping all the elements, we get the equation dP(t) dt =P(t)Q, whereQis a matrix
with elementsq ii =−µ i andq ij =p ijµi. For readers familiar with calculus, the differential
equation should be familiar: if we were to imagineP(t) is a single variable equation (which it
IS NOT, is a matrix), we could rearrange terms to dP(t) P(t) =Qdt, integrate on both sides, getting
lnP(t)−lnP(0) =Qt. LettingP(0) = 1 (or actually the identity matrix), then ln(P(0)) = 0.
Taking exponential on both sides yieldsP(t) =e Qt. Turns out that this intuition is also correct
in the matrix case 2.
What we get from this is remarkable: the fact that to describe all the transitions we just
need a matrix of constantsQ, and that the transition is only proportional to the time interval
∆t. The fact thatP(t) =e Qt also gives us for free the equilibrium distribution. Assuming
a very small time interval ∆t, we haveP(∆t)≈I+Q∆tfrom the Taylor expansion in the
2Instead of integrating, use the fact thate Qt =I+Qt+ (Qt) 2/2! + (Qt)3/3! +· · ·Guess thatP(t) =e Qt,
then P(t) dt =Q+Q 2t+Q 3t2/2! +· · ·. Factor theQto get exactly P(t) dt =QP(t). Lastly,P(0) =I, that is the
system is in the initial state with probability 1.

Supply Chain Analytics: A data-driven approach80
previous footnote. We know that the equilibrium distribution follows:
πP(∆t) =π,(7.6)
Then, we can just replace to getπ(I+Q∆t) =π, which simplifies to the equilibrium distribution
in CTMC:
πQ=0,(7.7)
Solving this system gives us exactly the equilibrium distribution of a system that evolves ac-
cording the the probabilitiesp ij and stays in stateifor an exponential amount of timeT i.
As we studied in previous chapters, getting a close expression for the equilibrium distribution
is a powerful modeling tool to understand the behaviour of a stochastic system. We illustrate
this with an example:
Example 7.1.A strait (or a man-made waterway) is a passage connecting two large bodies of
water. Imagine a country wants to inspect and charge ships as they cross. They can inspect
up to 5 ships at the same time, in 5 stations. Each inspection takes in averageE(τ) = 2 hours
per ship per station. The demand for the use of the strait depends on the fee ships are charged
to pass. The random quantity of arriving shipsadepends on this fee asE(a) =e −5p ships per
hour wherepis the fee a ship is charged per unit of time in the strait. Givenpwhat is the
average revenue that the country receives per hour assuminga(p) ships arrive per hour? Also,
what is the average amount of time a ship spends in this system? If instead of charging per
hour, the country charges per ship, what’s the new revenue?
The first step in solving this problem is defining the state space, that is, the set of states
that we are going to analyze. From the statement of the problem there can be up to 5 ships
in processing at any given time. Nonetheless, it is easy to imagine that a ship can arrive
while 5 others are in processing, and potentially one more and so on. Also, the system can
sometimes be empty. Then, it makes sense to let the state of the system be the integers
N= 0,1, . . .representing the number of ships in the system. The strategy will be to estimate
the average number of ships in the system (at any time), that is,E(N) = 0π 0 + 1π1 + 2π2 . . ..
The system earnspE(N) in the long term. To solve forπ, we need to find it withπQ=0.
To do this, we simply need to describe how the system evolves: from any state withi >0
ships in the system there are two posible outcomes, either a ship finish their service from a
station or a new ship arrives. The arrival of ships ise −5p per hour, soλ i :=q i,i+1 =e −5p.
Likewise, because of the memoryless property of the exponential distribution, the minimum of
kexponential random variablesmin(τ 1, . . . , τk) is another exponential distribution 3 with rate
3Note thatP(min(τ 1, . . . , τk)≥t) =P(τ 1 ≥t, . . . , τk ≥t) =P(τ 1 ≥t)· · ·P(τk ≥t) =e −t/Eτ1 · · ·e−t/Eτk =

81Instructor: Elioth Sanabria
equal to the sum of the rates of thekexponentials. In our case, there are at most 5 stations
or less active, then the transition occurs at a rateµ i :=q i,i−1 = min(i,5) 1 E(τ) = min(i,5)/2.
Finally,q i,i =−(q i,i−1 +q i,i+1). With this entries ofQsolving the equilibriumπQ=0gives
the equilibrium distribution of the system, from whichpE(N) is the rate the system earns.
This type of process is commonly called aBirth-Death Process, as from any statei, in
principle there will be a transition to eitheri+ 1 ori−1 with ratesλ i andµ i respectively.
Computing the equilibrium distribution is also easy for these processes, as the equilibrium
equation looks like:
−π0λ0 +π 1µ1 = 0
π0λ0 −π 1µ1 −π 1λ1 +π 2µ2 = 0
...
The first equation impliesπ 0λ0 =π 1µ1, which in turn cancels out the same term in the second
equation leavingπ 1λ1 =π 2µ2. The same continues occuring, thus havingπ kλk =π k+1µk+1.
Replacingπ 1 =π 0 λ0 µ1 andπ 2 =π 1 λ1 µ2 =π 0 λ0λ1 µ1µ2 from which we can deduce thatπ k =π 0 λ0···λk−1 µ1···µk .
Lastly, sinceπmust be a valid distribution (adding to 1) then we have 1 =π 0 +π 1 +· · ·, then
1 =π 0[1 +λ 0/µ1 +· · ·]. Which yieldsπ0 = [1 +λ 0/µ1 +· · ·]−1. After calculating these, the
average money that the country earns ispE(N) =p[0π 0 + 1π1 + 2π2 +· · ·].
Estimating the average waiting time seems hard, as in principle it would require to average
many possible paths for different number of ships in the system. But we can try to use what
we know to make this estimation. For any ship arriving at random, this ship will experience a
random amount of time in the systemW. This ship would have to paypE(W) in average. In
an hour, there areE(a) =e −5p ships arriving per hour, then, the amount they pay should be
E(q)pE(W). Note that the amount the ships pay is in fact the same revenue we found before.
Then, it must be true thatpE(N) =E(q)pEW. This is known asLittle’s law:
E(W) = E(N) E(a) ,(7.8)
This law is extremely useful, because we got the expected value of the waiting timeE(W) for
free, just knowing the arrival rateE(a) and the average number in the systemE(N). In general,
with this relation, we need only two of the quantities to guess the third. In most textbooks
this law is stated asE(N) =E(a)E(W). In Figure 7.2 there is a graphical representation of the
principle.
e−t[1/Eτ1+···+1/Eτk]. That is, an exponential distribution with a rate equal to the sum of the rates of the other
exponentials.

Supply Chain Analytics: A data-driven approach82
View 1: Time Snapshot
Counting the proportion of time
the system spends at each state
Time (t)
Ships (N)
0 T
1
2
3
Area =E(N)×T
Identical
Area
View 2: Ledger Spreadsheet
Summing up horizontal wait times
(Wi) row by row forCships
Duration (W)
Ledger Row
Ship 1
Ship 2
Ship 3
ShipC
W1
W2
W3
WC
Area = PC i=1 Wi =C×E(W)
Figure 7.2: Geometric derivation of Little’s Law by equating total system revenue over an
observation intervalT. View 1 scales the time-weighted average number of ships in the system
(E(N)×T) by a feep. View 2 scales the spreadsheet accounting record of individual random
turnaround times experienced byCarriving ships ( P Wi =C×E(W)) by the same feep.
Equating both operational perspectives balances the ledger, yieldingpE(N)T=pCE(W), which
simplifies directly toE(N) =E(a)E(W) given the average arrival rateE(a) =C/T.
For the last situation, the country notes an interesting fact: as long as the system is flowing,
that is, the rate of arrivalsE(a) is lower than the maximum rate of service 5/E(τ). Meaning
that the line of ships will not grow indefinitely, it must be the case that the rate of departures
is the same as the rate of arrivals. The logic follows from the fact that it cannot be the case
that the rate of departures is higher than the rate of arrivals as this would imply that somehow
more ships are created during the inspection, which is impossible. On the other hand, the rate
of departures cannot be less than that of departures as it would imply a collapse of the system
longterm (remember, everything is time-homogenous so far).
If we think about why this is the case, recall that in the derivation of the equilibrium
distribution, we had that for every stateπ kλk =π k+1µk+1. Which in plain words means that in
equilibrium between two states, the inflow and outflow of that partition is exactly the same. This
property is often calleddetailed balance 4 and means that the chain behaves the same forward
or backwards (think that there is a perfect symmetry of the flows forwards or backwards).
Imagining an alternative process, where time is reversed, that is arrivals are departures and
departures are arrivals, will distribute exactly the same. The key is that there is a strong
symmetry that allows this.
The conclusion is extremely powerful, because if departures behave the same probabilistically
than arrivals then it means that when you connect queues together, you can study them each
4This property is described asπ kqk,k+1 =π k+1qk+1,k

83Instructor: Elioth Sanabria
individually as the output will behave the same as the input (in this case a so-called Poisson
process, which only means that the time between arrivals follows an exponential distribution).
If for example the country wished to connect multiple queues in tandem (sayℓ) or in a
network where the next tandem is selected with a fixed probability (a so-called routing matrix),
starting with Poisson arrivals at a rateE(a) =e −5p. Then, the equilibrium distribution of the
number in each queue is just the product of the equilibrium distributions of each queue as:
π(N1,· · ·, Nℓ) =π 1(N1)× · · · ×πℓ(Nℓ),(7.9)
Likewise, this also implies that after the tandem of queues, the departure rate is identical in
distribution to the arrivals. Therefore, the revenue of charging ships only once ispE(a) =pe −5p.
The price that maximizes the revenue is given by equating the derivative to 0, that is,pe −5p5 =
e−5p orp= 1/5.
7.3 Time-varying arrivals
Time homogeneity (in both arrivals and processing times) is often an unrealistic assumption.
Many manufacturing processes are subject to time-varying demand patterns. For example, ports
have different demand patterns depending of the time of the year and time of day. Likewise,
certain manufacturing processes see a spike of the demand at certain times of the year. Toy
manufacturers see an increase towards the holidays. Certain rare events such as pandemics
increase the demand for medical supplies and so on. All of these examples emphasize the need
to extend the analysis to systems where the arrival changes over time.
The need to consider time-varying arrivals seem to contradict the time-homogenous struc-
ture of the (Continuous) Markov Chains that we have studied. To see why, suppose that the
random arrivalsachange in average over time. From our equilibrium analysis, we get away
by considering time by having that the interarrival times follow an exponential distribution,
where the probability of seeing a new arrival in an interval ∆tisλ∆tfor an exponential random
variable with rateµ. If we wanted to change this rate to be time dependent asλ(t) it would
break the equilibrium conditions everywhere, as dP(t) dt is not a constant anymore.
Before throwing the time-homogenous time into the garbage, one can imagine a way to
salvage the model, while still allowing some degree of change in the arrivals: The strategy is to
consider dividing time into relativelylongintervals where the arrivals remain with a constant
rater 0 and then change to another rater 1. For example, this can happen every 12 hours. You
can extend the strait example to imagine that there is a higher demand rater 0 during the
daytime hours (say 7am-7pm) than during the other 12 night hours.
We can imagine in this mental experiment, the system is going to behave almost like the

Supply Chain Analytics: A data-driven approach84
homogeneous case in the middle of each period. For example, at noon the system pretty much
should look as if the arrival rate is exactlyr 1 all the time. The problem is going to be at the
times that the rate changes. But if we are willing to ignore this, then the approximation should
still work with some caveats. For example, Little’s Law states that the average number in
systemE(N) is equal toE(W)E(a). In this case, we should expect thatE(N) =E(W)r 0 during
the daytime range andE(N) =E(W)r 1 during the night, assuming the service rate is also the
same. If the processing is very fast compared to the arrival rate, meaning that the system is
empty most of the time. Then, these approximations should hold relatively well. The problem
is that if the processing is slow, ifr 0 > r1, at the beginning of the night shift at 7pm there
might be still jobs in process from the earlier part of the day.
This phenomenon is in fact very common in a lot of manufacturing and retail systems: pro-
cessing is high-traffic, that is the system sees a number of arrivals that it can barely process. In
a way, this makes economic sense, as a faster system means spending more money on processing
resources (workers, servers, stations, etc), and unless there is a reward for higher throughput,
the company will spend the minimum amount of resources that allows to meet the demand or
target throughput. In other words, it makes economic sense to have a system that is barely
stable. In a way it makes sense that some unprocessed work accumulates over less busy periods.
Going back to our mental experiment, at 7am the system should start almost empty. At
7pm, lettingt= 0, suppose that the system hasN(0)>0 jobs that are still in processing when
the arrival rates changes to the lower intensityr 1. Then, we would like to know how many jobs
are in the system at 8pm, that is,t= 1. We can do multiple analyses. First we start with the
case where there are infinite servers (while unrealistic, there are some systems that behave like
this). Suppose, each server servers at a rateµ. See Figure 7.3 for a visual representation.
7.3.1 Time-varying arrivals with infinite servers
Since there are always available servers, we can treat the two populations separately: on one
hand the previous jobsN(0) plus the new jobs that arrive between 7pm and 8pm, that is, from
t= 0 tot= 1. For the new jobs, because of the memoryless property, their time to service is
the exponential rate. Att= 1 we have:
E


N(0)X
i=1
1{Ti ≥t= 1}

 =
N(0)X
i=1
P(Ti ≥1) =N(0)e −1µ,(7.10)
For the new arrivals, betweent= 0 andt= 1 we have that at each small intervaldtthere
is a new arrival with rater 1 and each of these arrivals will still be in the system at 8 pm, that
is,t= 1 with probability equal to the exponential. For example, an arrival ats∈(0,1) will
still be in processing with probabilitye −(1−s)µ, which is exactly the definition of the reliability
functionR(1−s). Since at eachdtthere is an arrival with probabilityr 1dt, and the interval is

85Instructor: Elioth Sanabria
3pm 7pm
(t= 0)
11pm
r1 (Night)
r0 (Day)
Arrival Rateλ(t)
Time-V arying Step Demand Profile
3pm 7pm
(t= 0)
11pm
E[Nnight]
E[Nday]
Day Equilibrium:E[N] =E[W]r 0
Night Equilibrium:E[N] =E[W]r 1
Backlog Residual
N(0)>0 att= 0
Time of Day
Avg. JobsE[N(t)]
System Congestion & Backlog Hangover (r 0 > r1)
Figure 7.3: The mechanics of a non-homogeneous queueing system switching operational
regimes. The upper axis illustrates a piece-wise constant arrival pattern splitting daytime
demand (r 0) from nighttime demand (r 1). The lower axis visualizes the transient response of
the expected inventoryE[N(t)]. If processing speeds are tight, the system creates an inventory
carryover at the 7pm boundary (t= 0), meaning remnants of daytime congestion bleed into the
night shift.
so small that the probability that 2 arrivals occur is 0. We can do this calculation for eachdt
as:
Z 1
0
e−(1−s)µr1ds=r 1
Z 1
0
e−(1−s)µds=r 1
Z 1
0
e−sµds= r1
µ (1−e −1µ),(7.11)
Now that we know the expected numbers from each population (the new and old), we can put
them together as:
E[N(1)|N(0)] =N(0)e −1/E(W) +E(a(0,1))E(W)(1−e −1/E(W) ) (7.12)
WhereE(W) =µ −1 andE(a(0,1)) =r 1. This equation can be seen as a transient version of
Little’s Lawwhere whenE(W)→0, meaning that the system is fast enough to process the
jobs quickly and the system just converges to the expected Little’s Law (as the terme −1/E(W)
vanishes) and all that is left isE[N(1)|N(0)] =E(a(0,1))E(W). Since this relation applies
between any two time intervals, we can apply it to systems when the arrival rates change (and
remain constant) in known intervals.

Supply Chain Analytics: A data-driven approach86
Then, for a situation when the rates change every period, sayr 1 =E(a(0,1)),r 2 =
E(a(1,2)), . . ., we can conclude the following relation:
E[N(t)|N(t−1)] =N(t−1)e −1/E(W) +r kE(W)(1−e −1/E(W) ),(7.13)
If we take expectation on both sides, we end up with the relation:
E[N(t)] =E[N(t−1)]α+βr t,(7.14)
Withα=e −1/E(W) andβ=E(W)(1−α). Solving this equation recursively starting atN(0),
so thatE[N(1)] =αN(0) +βr 1.E[N(2)] =α(αN(0) +βr 1) +βr 2 and so on, yieldsE[N(t)] =
αtN(0) +β Pt i=1 αi−tri, or the relation:
E[N(t)] =e −t/E(W) N(0) +E(W)(1−e −1/E(W) )
tX
i=1
rie−(i−t)/E(W) ,(7.15)
Intuitively this result can be seen as an average over the entire history of the process. The first
term represents the oldest arrivals starting at time 0, and each term of the summation is the
contribution of arrivals each time step. Similar as before, whenE(W)→0, all the terms of the
summation vanish, except the last one (ase −(t−t)/E(W) = 1), leavingE[N(t)] =E(W)r t which
is Little’s Law as expected.
This kind of recursion is useful when we have a system that has stable service rate, but
time varying arrivals. These arrivals can be a seasonal demand that can be estimated with
the methods in Chapter 1 and we want to know how much resources are needed to sustain the
operation in the future: imagine a factory with fixed and enough machinery which staffing levels
are proportional to the number of jobs in the systemE[N(t)] for a distantt. This recursion
would allow us to estimate the staffing load knowing the number of jobs today atN(0).
7.3.2 Time-varying arrivals with finite servers
The infinite server case is a useful approximation in cases where the servers are not the bottle-
neck of the system, that is, relative to the amount of arrivals there is always enough processing
capacity. This is the case in certain manufacturing and computing systems. When the pro-
cessing capacity is limited by the number of servers, saykof them each serving at a rate
µ= 1/E(W), the situation is different. Starting theN(0)>0 jobs in queue, whenN(0)≤kwe
are in a similar situation to the infinite server case, as the number in system will keep decreasing
at an exponential rate towards equilibrium to Little’s law.
Suppose the arrival rateE(a(0,1)) is againr 1 andN(0)> kmeaning that the system starts
with more jobs than available servers. At maximum capacity the effective service rate iskµ(all
servers are active). In this case, the system will behave linearly, with arrivals growing at a rate
ofr 1 and exiting at a ratekµ. In this case, the case behaves in a linear fashion as the number
in system is (r 1 −kµ)t. Ifr 1 > kµthe queue will keep growing as the server at maximum

87Instructor: Elioth Sanabria
capacity is not able to process jobs fast enough to vacate the queue. Likewise, whenr 1 ≤kµ,
the number in system will decrease linearly until either the arrival rate changes att= 1 tor 2
or the number in the system is equal tok. More explicitly, for a timet∈(0,1) the number in
system is in averageN(t) =N(0) + (r 1 −kµ)t.
If for example, (r 1 −kµ)tis decreasing fast enough it could happen that there is at <1
that the system now has less thankjobs, that is, aN(t)< k. In this case, as jobs get processed
the system becomes exactly like the infinite server case as jobs that arrive will find a server and
will behave statistically the same way as the previous section. This time will bet ∗ = k−N(0) r1−kµ if
this is less than 1, then the change in the dynamic will occur by then and the system will start
behaving as the infinite server regime. That is,E[N(1)] =E[N(t ∗)]e−(1−t∗)/E(W) +r 1E(W)(1−
e−(1−t∗)/E(W) ). This can be seen as restarting the system at timet ∗.
As the rates change the system can alternate between the linear regimeE[N(t)]> kor the
exponential regimeE[N(t)]≤k. Even though it is called exponential regime, it does not mean
that it is faster than the linear one. In fact, it is slower as less thankservers are in operation
while the arrival rate remains the same. For a system starting at timet−1 withN(t−1) jobs
there are the following cases:
•N(t−1)> ka linear system: The system evolves asE[N(t)] =E[N(t−1)] + (r t −kµ)t
either until the next rate change or until a timeτ > t−1 when the system enters the
exponential regime.
•N(t−1)≤kan exponential system: The system evolves asE[N(t)] =E[N(t−1)]α(∆t) +
(1−α(∆t))E(W)r t until the change of arrival rate or until a timeτ > t−1 when the
system enters the linear regime.
We illustrate this with an example:
Example 7.2(World Cup Tickets).A cloud provider service hosts an application to sell World
Cup tickets. They have staggered access to the website starting at 9am to 10 thousand premium
customers, the system starts withN(0) = 5 thousand and the arrival rate for the next hour is
the other 5 thousand. The general population will have access starting at 10am, arriving at a
rate of 20 thousand per hour until noon when the sale closes. Each person takes in average 10
minutes to complete their purchase. The cloud computing company wants to know how much
computing power to allocate. They can choose between two configurationsk= 3 ork= 5
thousand capacity servers. Plot the average number of customers in the system.
The first aspect to determine is in what regime the system starts. In the case of the
configuration withk= 5 thousand servers the system starts in the exponential system. As
time progresses, the average number in systemE[N(t)] converges to Little’s law: The average

Supply Chain Analytics: A data-driven approach88
time in system isE[W] = 1/µ= 1/6 and the arrival rate isE(a(0,1)) = 5 thousand. Then,
the system decays until convergence atE(W)E(a(0,1)) = 5/6 thousand (approximately 833
customers). This will continue until timet= 1, corresponding to 10am when the arrival rate
E(a(1,3)) changes to 20 thousand per hour. In this case, since we start at the exponential
regime at time 1 with 833 average customers. The new equilibrium implied by Little’s law is
E(a(1,3))E(W) = 20/6 thousand (approximately 3,333 customers). Since this is belowk= 5000,
the system should continue in the exponential regime until closing at time 3 (noon).
The other configuration is slighly more interesting. First, the system starts in the linear
regime asN(0) = 5 thousand is greater than the availablek= 3 thousand servers. The slope
of the system isE(a(0,1))−kµ= 5−3(6) =−13 thousand customers per hour. Starting at
N(0) = 5 the time that the system reach the exponential regime is 5−13t= 3 ort= 2/13≈
0.15 or around 9:10am. At this time the system enters the exponential regime and converges
again to the equilibrium point of 833 customers. Likewise, at 10am the system starts in the
exponential regime towards 3,333 customers. But before that, it must reach 3000 (the number
of servers) at a timee −6t(5/6) + (1−e −6t)(20/6) = 3 or just 2/6 =e −6t(15/6) which simplifies
tot= ln(15/2)/6≈0.33 or around 10:20am. At this time, the system enters the linear regime
growing a rate ofE(a(1,3))−kµ= 20−3(6) = 2 thousand customers per hour. This linear
growth will continue until the sales closing time at noon, the system will never recover or reach
equilibrium. See Figure 7.4.

89Instructor: Elioth Sanabria
0 1 2 30
2,000
4,000
6,000
N(0) = 5000
Hours (from 9am)
E[N(t)]
k= 5000
0 1 2 30
2,000
4,000
6,000
Capacityk
Hours (from 9am)
k= 3000
Figure 7.4: Transient behavior of the average number of customers in the systemE[N(t)] over
a 3-hour window for two capacity configurations. The left plot (k= 5000) shows a system that
remains entirely in the exponential regime, successfully absorbing both the initial workload
and the 10am demand surge well below capacity limits. The right plot (k= 3000) exhibits
alternating regimes: an initial linear drain down to the capacity boundary, a stable exponential
phase chasing an 833-customer equilibrium, followed by a post-10am surge that crosses back
over the capacity line into an unsustainable, linear growth phase.

Supply Chain Analytics: A data-driven approach90

Chapter 8
Optimization of Queueing Systems
8.1 Introduction
We have built a decent understanding of queueing systems by analyzing the variants derived
from the memoryless property with changes in the arrival rates and the number of servers. In
real life, every queueing system is tied to some resource that needs to be optimized: the staff
scheduling of a retail store, the server capacity of an online application, the number of active
stations serving a manufacturing process. As mentioned in the previous Chapter, the matching
of resources needs to make economic sense in the context of the business goal: satisfiying some
target demand within a prescribed time, sustaining a level of service for all incoming customers,
etc.
8.2 Linear Allocation
Going back to the staff scheduling models studied in 4 imagine that you want to schedule a
facility that serves customers, each taking a random timeτin service. This setting is typically a
call center, a retail store, a restaurant, a factory or any system where when jobs accumulate past
certain level they wait in queue. The resource is an integer number representing the number of
servers available to serve customers: such as employees. The rate the system serves isµ.
It would be great if there is a system where the serviceE(W), say the waiting time a customer
spends in the system: waiting in queue plus their service time behaves linearly. The simplest
model is a single server, operating at a rateµ. In this case, we can apply the same logic: a
customer arriving sees in averageE(N) customers, each served in average at a time 1/µper
customer, plus their own service time 1/µ. Then, a random customer waits in this system as:
E(W) =E(N)(1/µ) + 1/µ,(8.1)
91

Supply Chain Analytics: A data-driven approach92
But we also know that by Little’s law thatE(N) =E(a)E(W), replacing this in the equation
yieldsµE(W) =E(a)E(W) + 1 or:
E(W) = 1 µ−E(a) ,(8.2)
The implicit assumption is that the system is stable, that is, that the arrival rateE(a) is less
than the processing rate of the serverµ. This expression is great because it is almost linear on
the server termµ. Then, we could approximate the rate of the serverµto be proportional to
the number of resources, sayx˜µ, choosing ˜µin such way that it matches the desired processing
rate. Wherexis a vector choosing the number of resources assigned to a given collection of
schedules such as in Chapter 4, this leads to the following scheduling formulation:
minf(x) (8.3)
s.t.µAx ⊺ ≥E(A),
1≤(˜µAx⊺ −E(A)) ¯W ,
x∈ X.
The first constraint just represents the stability condition of the system, ensuring that the
demandE(A), which is a vector with elementsE(a(t−1, t)) is below the processing capacity
of the system. The second constraint represents limiting the average waiting time to some
maximum level ¯W, such that, at all hours the service is in average below this level. As before,
f(x) can be choosen to be the payroll. Or even a more elaborate measure, we illustrate this
with an example:
Example 8.1(Car Wash Scheduling).An owner of a car wash wants to minimize their op-
erating costs which are proportional to their payroll, expressed as a vectorcx ⊺ and the water
and electricity costs of their car wash, which areγdollars per unit of time when each station
is on (there are in totalKstations). While servicing all the demand, the owner wants to do a
scheduling at minimum cost. How to model this problem?
First, satisfying all the demand is the constraintµAx ⊺ ≥E(A), which is the same stability
condition of the queueing system. The cost part is more elaborated: the payroll cost iscx ⊺
as in the Scheduling chapter, but the variable cost is in principle a complex calculation as it
would require in principle estimating the average behaviour of the system for different staffing
configurationsAx ⊺. Then, we want to know how to expressf(x) =cx ⊺ + Variable Cost. To do
this, we can use what we learned in the Chapter 7 via Little’s law, we know that the average
number in system is given by:
E(N(t)) =E(a(t−1, t))E(W) =E(a(t−1, t)) 1 ˜µ(Ax⊺)t −E(a(t−1, t)) ,(8.4)

93Instructor: Elioth Sanabria
Then, the cost over the periods the car-wash is opent= 1,2, . . . , Tis approximatelyPT t=1 γE(N(t)).
Then, the next step is to linearize the variable cost part of the objective PT t=1 γE(N(t)) on
xso that we can use an optimizer to solve the problem. A way to write this problem as
a MIP is to estimateE(N(t)) for the range of possible values it can take, for example, let
Ek(N(t)) = E(a(t−1,t)) ˜µk−E(a(t−1,t))and then creating a variablez k,t selecting the corresponding value to
1 if (Ax ⊺)t =k. Then, the problem can be written as:
mincx ⊺ +γ
TX
t=1
Ek(N(t))z k,t (8.5)
s.t.µAx ⊺ ≥E(A),
(Ax⊺)t =
KX
k=1
kzk,t,fort= 1, . . . , T,
KX
k=1
zk,t = 1 fort= 1, . . . , T,
x∈ X, zi,k ∈ {0,1}.
Clearly, this type of formulation has its pros and cons: on one hand it is a tractable for-
mulation that in a single pass allows to solve a seemingly complex problem without multiple
simulation runs in a difficult combinatorial space. On the other hand, it is still an approximation
on many levels.
The first element, is that ˜µshould be chosen carefully as one mega-server working always
at a ratekµis not the same askservers at a rateµ. To see why, when there is less thank
jobs in the system, sayi < kthe superserver operates at a ratekµwhile the multiple servers
operate at a rate min(i, k)µ. Then, it makes sense to deteriorate the rate ˜µto be slower to
compensate for the speedup. A simple way is to define a factor ˜µ k =η kµwhereη k <1, thus
slowing down the server. One such value forηcould be the probability that all servers are active
ηk =P(i≥k) = P∞ i=k πi in the originalM/M/kqueue, this slows down the server to reflect
that wheni < ksome servers are idle in the original model, thus making the approximation
better reflect the original behavior ofkservers into a single one with normalized rateµη k.
8.2.1 Mean-variance optimization
Another common feature throughout out exposition is modeling the risk-aware version of the
problem. In this case, we can exploit the same approximation to consider the variance of the
number in system, that isVar k(N(t)) with multiplierλ(see Chapter 3 to see different ways to
choose the parameter). This leads to the equivalent risk aware formulation:

Supply Chain Analytics: A data-driven approach94
mincx ⊺ +γ
TX
t=1
Ek(N(t))z k,t +λ
TX
t=1
Vark(N(t))z k,t (8.6)
s.t.µAx ⊺ ≥E(A),
(Ax⊺)t =
KX
k=1
kzk,t,fort= 1, . . . , T,
KX
k=1
zk,t = 1 fort= 1, . . . , T,
x∈ X, zi,k ∈ {0,1}.
Closed expressions for the Variance of queueing systems are widely known, for example, for the
M/M/1 approximation, we haveVar k(N(t)) = E(a(t−1,t))k˜µ [k˜µ−E(a(t−1,t))]2 .
8.3 Accuracy and non-exponential service times
The approach presented is compelling in the sense that it allows to model service times at
determistic epochst, t+1, ...that are useful for planning horizons where the accuracy is tolerable
(this is true for many manufacturing systems where noise averages out) and the resources
scheduled have a difficult combinatorial nature (for example, scheduling people).
There are other systems that have a mathematically more amenable description of their
resource space but require more accuracy. One key example of such system are computer services
that deal with thousands of client request simultaneously. Large Language Models (LLMs)
providers have to solve a server allocation problem to service their demand within a reasonable
time in system for hundreds of thousands of concurrent requests. Here, our understanding of
queueing systems shines to solve these kind of problems. Imagine the following problem:
minE
Z T
0
[c(kt) +γ(N t)]dt

(8.7)
s.t.P(W > s)≤α.
Wherek t is the number of active servers at timet,N t is the number in system at timetandc
andc(k t) is a cost function dependent on the number of active servers, whileγ(N t) is a variable
cost function depending on the number of queries in the system.Wrepresents the random
amount of time in system the customers face. The problem can be stated as finding the number
of servers that in average keeps the system at minimum cost while with a low probabilityα
makes that the time in system does not exceed a thresholds. This could easily represent the
problem that a cloud provider has to solve to service an application or service (such as providing
inference for LLMs). In principle we could apply the same strategy that we proposed in the
exposition of the previous section, but in this case we can do better.

95Instructor: Elioth Sanabria
Recalling Chapter 4 we can apply a similar dynamic programming principle, were we can
solve the problem using the same iterative procedure. Start with a set of actions, the number
of servers, that is,k= 0,1, . . . , Kand discretize the time horizon at intervals of size ∆t. The
key as always is to set up a recursive relation for the problem, in this case:
Vt(N) = min k [c(k, N)∆t+V t+1(f(N, k, rt))],(8.8)
Wherer t :=E(a(t, t+ ∆t)) andf(N, k, rt) represents the transition function of a system that
currently hasNcustomers,kactive servers and a expected arrival rater t. The first and easiest
part is defining the loss functionc(k, N) which is justc(k) +γ(N).
For the dynamics of the systemf(N, k, rt), we can exploit what we know about the transient
behaviour of a queueing system. For a small ∆twe have that in expected value:
Nnext =f(N, k, rt) =
(
N+ (r t −kµ)∆tifN≥k(Linear/Saturated)
N e−µ∆t + rt µ (1−e −µ∆t) ifN < k(Exponential/Recovery) (8.9)
Similar to the previous chapters, a way to incorporate the service constraintP(W > s)≤α
is to prune the paths where this occurs. The trick is to express this probability in terms of the
primitives of the model.
There are many ways to achieve this, perhaps the simplest is the argument that we used to
derive the waiting time of the single server queue. In this case, when the server is saturated
N > k, the waiting time a new customer faces is the waiting time of people in queue (N−k),
each entering service at a ratekµ. And after that, the customer enters their own service at
a rateµ. That is, the time theN-th customer stays in the system withkactive servers is in
average:
E(W(N)) = (N−k) +
kµ + 1 µ ,(8.10)
Likewise, its variance is the variance of the exponential times, which are independent from each
other, that is:
Var(W(N)) = (N−k) +
(kµ)2 + 1 µ2 ,(8.11)
Then, we can approximate the random waiting time at each step as:
W(N)≈ max(N, k) kµ +Z
s
max(N, k)
(kµ)2 ,(8.12)
Therefore, the probabilityP(W(N)> s)≤αorP(W(N)≤s)≥1−α, is given by the
expression:
skµ≥max(N, k) +
p
max(N, k)Φ−1(1−α),(8.13)
Then, combinations ofN, kthat violate this condition are not admissible in the DP iteration.

Supply Chain Analytics: A data-driven approach96
8.3.1 Non-exponential service times
Throughout our exposition we have considered exponential service times. The exponential
service times have allowed us to use the memoryless property and analyze the system at each
snapshot of time. Considering non-exponential service times tends to make control problems
intractable as there is a need to keep track of either the elapsed or remaining service times as
they are no longer memory-less. The reason is that the reliability function in general does not
follow time-homogeneity, that is,R(s)R(t)̸=R(s+t).
In recent years, a new framework called QPLEX (see [5]) allows to estimate transition
dynamics without doing full simulations or having to keep track of an explosive state-space.
The key insight is that given a specific number of customers in the system we sample a single
customer in service remaining time (sayN t =N, that in the previous subsection we were
taking as the expected value). Conditional onNthe remaining time in service can be seen
as an i.i.d. random variable. CallLas the random remaining service time of a job picked at
random. Estimating the distribution ofLfor a given timetis what QPLEX does through a
series of clever tricks. Call this distributionν t. With this distribution as input, conditioning
on a starting number of jobsN t we can express most of the primitives of the problem. For
example, the number of expected departures isN tνt(L= ∆t|N t). In fact, QPLEX estimates
the distributions of the number in system at the next steppt and the remaining service durations
νt, call these pair of distributionsp t, νt.
QPLEX is able to approximate these sequential distributions through clever conditionings.
Using the distributionsp t, νt we can redo our dynamic programming procedure as:
Vt(N) = min k [Ept(c(k, N))∆t+E νt(Vt+1|N, k, rt)].(8.14)

Bibliography
[1] BV Aimms. “AIMMS modeling guide—integer programming tricks”. In:Pinedo, Michael.
Scheduling: Theory, Algorithms, and Systems; AIMMS BV(2018).
[2] Kenneth J Arrow, Theodore Harris, and Jacob Marschak. “Optimal inventory policy”. In:
Econometrica: Journal of the Econometric Society(1951), pp. 250–272.
[3] Hong Chen and David D Yao.Fundamentals of queueing networks: Performance, asymp-
totics, and optimization. Vol. 46. Springer Science & Business Media, 2001.
[4] George Dantzig, Ray Fulkerson, and Selmer Johnson. “Solution of a large-scale traveling-
salesman problem”. In:Journal of the operations research society of America2.4 (1954),
pp. 393–410.
[5] Antonius B Dieker and Steven T Hackman.QPLEX: A Computational Modeling and Anal-
ysis Methodology for Stochastic Systems. Springer, 2025.
[6] Aryeh Dvoretzky, Jack Kiefer, and Jacob Wolfowitz. “Asymptotic minimax character of the
sample distribution function and of the classical multinomial estimator”. In:The Annals
of Mathematical Statistics(1956), pp. 642–669.
[7] Pascal Massart. “The tight constant in the Dvoretzky-Kiefer-Wolfowitz inequality”. In:
The annals of Probability(1990), pp. 1269–1283.
[8] Anatoliy V Skorokhod. “Stochastic equations for diffusion processes in a bounded region”.
In:Theory of Probability & Its Applications6.3 (1961), pp. 264–274.
97
