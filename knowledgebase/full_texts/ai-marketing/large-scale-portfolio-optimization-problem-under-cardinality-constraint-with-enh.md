---
title: Large-Scale Portfolio Optimization Problem Under Cardinality Constraint With Enhanced Multi-Objective
  Evolutionary Algorithms
url: https://arxiv.org/abs/2607.09566
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Danial Ramezani
- Mostafa Abouei Ardakan
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.09566
pages: 37
chars: 113391
fetched_at: '2026-11-08T13:07:37+00:00'
kb_version: 1
---

# Large-Scale Portfolio Optimization Problem Under Cardinality Constraint With Enhanced Multi-Objective Evolutionary Algorithms

Large-Scale Portfolio Optimization Problem Under Cardinality
Constraint With Enhanced Multi-Objective Evolutionary
Algorithms
Danial Ramezani a, Mostafa Abouei Ardakan a
a Department of Industrial Engineering, Faculty of Engineering, Kharazmi University, Tehran, Iran
Abstract.Decision-making is posing an increasingly formidable challenge to investors because of the
growing number of alternatives available in financial markets. A hot area of research over the past few
decades has been portfolio optimization that seeks to determine how much an investor should invest
in which asset. Introducing real-world conditions to the optimization model turns the problem into an
NP-hard one for whose solution exact methods become inefficient; hence, researchers have turned to
evolutionary algorithms to approximate solutions. In this paper, strengthening strategies are presented
for multi-objective evolutionary algorithms that can provide a faster convergence rate and extensive
search ability in the portfolio optimization problem under the cardinality constraint. To implement those
features, a unique solution representation, a novel operator, and new repair mechanisms are introduced
for solving the aforementioned problem in which lower and upper limits are set on the number of assets in
the portfolio. For this purpose, new mating strategies along with the aforesaid package are implemented
in well-known multi-objective evolutionary algorithms to solve the problem. The customized algorithms
are subsequently tested against traditional ones using well-known market indices as benchmarks. Results
indicate that the proposed strategy not only provides better approximations but also converges faster
as well at no loss of performance with increasing number of assets in the market.
Keywords:Cardinality-constrained portfolio optimization·Multi-objective optimization·Mixed-integer
programming·Evolutionary algorithms·Asset allocation
1 Introdution:
Portfolio selection is well-known to investors and fund managers and is a widely used strategy in financial
markets. It, indeed, involves the selection of capital and its proper allocation to various potential assets
aimed at maximizing return but minimizing risk.
Investors and portfolio managers seek to identify the best investment opportunities with the highest
return and lowest risk (Pedersen et al. (2021)). Modern portfolio theory was pioneered by Harry Markowitz
who put forth the concept of diversification as a solution to mitigating portfolio risk. He introduced variance
as a risk measurement; his mean-variance (MV) model is based on minimizing risk for a certain level of
return (Markowitz (1952)). Although Markowitz’s revolutionary work altered quantitative finance, it suffered
from certain shortcomings from a practical perspective; for instance, it ignored such real-world constraints
(Ertenlice and Kalayci (2018)) as cardinality constraint (CC) that puts limits on the number of stocks in the
portfolio, boundary constraint (BC) that imposes a limit on the portion of capital allowed for investment in
an individual asset within a portfolio, transaction costs (Thakkar and Chaudhari (2021)), round lot constraint
(Almahdi and Yang (2019)), class constraint (Almahdi and Yang (2019)), sector capitalization constraint
(Golmakani and Fazel (2011)), and turnover constraint (Clarke et al. (2002)). The portfolio optimization
problem (POP) has attracted researchers’ attention and encouraged a significant amount of research work
to extend the MV model or to incorporate real-world constraints.
Konno and Yamazaki (1991) considered mean absolute error as a risk measure for addressing nonlinearity
in the MV model. Later, value at risk (VaR) (Jorion (1997)) gained attention in modeling portfolio risks.
Due to its shortcomings, namely subadditivity and convexity, Rockafellar et al. (2000) put forth the concept
of minimizing conditional value at risk (CVaR) instead of VaR. Using S&P 500 data, Shalu et al. (2024)
demonstrated that expectile-based portfolio optimization models outperform the CVaR objective function.
arXiv:2607.09566v1  [cs.CE]  10 Jul 2026

The selection of a method for solving an optimization problem largely depends on the researcher’s objec-
tives regarding desired outcomes. When models are complex, non-exact methods, which offer faster, approx-
imate solutions that can still be considered feasible in many cases, are generally preferred due to their ability
to handle higher complexity more efficiently. On the other hand, exact methods are more time-intensive but
guarantee optimal solutions (Milhomem and Dantas (2020)). On account of the fact that adding the above
constraints would make the problem an NP-hard one (Erwin and Engelbrecht (2023)), almost one fifth of
the studies reported in the literature made use of exact approaches and machine learning (ML) algorithms
to solve POPs (Kalayci et al. (2019)).
Portfolio optimization can be addressed using various exact algorithms and techniques. Xu et al. (2024)
formulated the POP, where they considered only a limited number of assets for investment, as a max-min
optimization problem using dual theory, and employed the depth-first branch and bound method to identify
the globally optimal investment selection strategy. Kobayashi et al. (2021) reformulated the POP with CVaR
as a risk measure into a bilevel optimization problem and presented a cutting-plane algorithm to solve it
exactly. Cui et al. (2020) also considered CVaR as a risk measure in their proposed two-stage stochastic POP.
To solve this model, they employed a hybrid combinatorial approach that integrates a hybrid algorithm with
a linear programming solver. Vielma et al. (2008) utilized a branch-and-bound based algorithm for a multiple
POP with different objective functions such as classical MV and shortfall. Results demonstrated that their
algorithm outperformed common solvers. Akbay et al. (2020) presented an algorithm that divided POP into
two parts: choosing stocks via the variable neighborhood search (VNS) algorithm, and assigning weights
using the quadratic programming.
Instances of using ML and deep learning techniques, either to solve the problem directly, to predict
parameters, or alongside other methods, can also be found in the literature. Fern´ andez and G´ omez (2007)
applied Hopfield networks, a type of neural network designed to solve optimization problems, to solve the
POP. Chen et al. (2021a) applied XGBoost with improved firefly algorithm for predicting stock prices and
utilized Monte-Carlo simulation to construct optimal portfolio out of good-quality stocks. Paiva et al. (2019)
proposed the support vector machine for identifying eligible stocks and the MV model for assigning weights
to the portfolio. Behera et al. (2023) applied various ML regression algorithms along with the mean–VaR
model to solve the POP; results indicated that the mean–VaR model accompanied by adaptive boosting
outperformed the other models. Wang et al. (2020) deployed various ML techniques to forecast stock returns
and identify the most promising ones out of a pool of assets and, further, used MV to optimize allocations.
Wu et al. (2022) argued that conventional methods were unable to consider the market condition impacts
and that they would fail to select assets from a large pool of stocks. They, therefore, proposed an ML
technique and the K-means algorithm to predict trends and select stocks for optimization, respectively.
Zhang et al. (2020) presented a novel cost-sensitive reward function that incorporates patterns in prices and
correlations among assets. The goal was to maximize the accumulated return while adhering to constraints
such as transaction costs and risk management. Ma et al. (2021) integrated ML and deep learning models
with portfolio optimization techniques to enhance stock selection and return prediction, showing that the MV
method combined with random forest forecasting outperforms other approaches. Sadik et al. (2023) proposed
using regularization techniques to optimize predictability through computer simulations for mean-reverting
portfolio selection.
Since exact techniques fail to render efficient solutions for POP, nearly four-fifths of researchers have
turned to metaheuristic algorithms (Kalayci et al. (2019)). Chang et al. (2000) included CC and BC in
the MV model and showed that efficient frontier (EF) might become discontinuous and invisible to exact
approaches when each of the aforementioned constraints are introduced into a model. They, therefore, em-
ployed genetic algorithm (GA), tabu search, and simulated annealing in their model and tested the results
on 5 market indices for a stock number of up to 225. Additionally, a greater body of literature has been over
the past few years devoted to multi-objective models compared to single-objective ones due to the nature of
conflicting objectives of the MV model (Mansour et al. (2019)). What’s more, the multi-objective approach
is found to be capable of providing sets of portfolios that appeal to all investors, as they have different
preferences for portfolio types based on their desired risk levels (Gunjan and Bhattacharyya (2022)). Kalayci
et al. (2020) proposed a hybrid metaheuristic algorithm based on the key features of GA, ant colony opti-
mization, and artificial bee colony optimization to address the cardinality-constrained portfolio optimization
problem (CCPOP). Song et al. (2023) proposed a co-evolutionary multi-swarm adaptive differential evolu-
tion algorithm that was capable of resolving problems of premature convergence and search stagnation by

distinguishing between population and multi-operator parallel search strategy. Kizys et al. (2022) merged
VNS with Monte-Carlo simulation both to improve the performance of the algorithm and to deal with un-
certainty in their model. Morteza et al. (2023) proposed a multi-population whale optimization algorithm
with three objective functions, namely, return, risk, and liquidity. Moreover, they updated parameters with
reward and penalty using reinforcement learning. Moehle et al. (2023) developed a heuristic algorithm based
on the alternating direction method of multipliers alternating direction method of multipliers for separable
and nonconvex terms in the objective function, solving the problem with moderate accuracy. Corazza et al.
(2021) presented a hybrid particle swarm optimization (PSO) algorithm. They reformulated POP as an un-
constrained problem with an exact penalty function, which dynamically changes its parameters in order to
reduce possible infeasible solutions throughout the process. Silva et al. (2019) proposed an adaptive ranking
PSO algorithm that is based on three mechanisms for ranking solutions. In this model, the non-dominated
sorting and crowding distance are initially applied before solutions are ranked based on crowding distance
and cost-benefit (CB) defined as the ratio of expected return to risk. The summation of scores assigned
from each ranking method determines the final rank; if there is a tie, the particle with the higher CB will
be chosen. Sadeghi Hesar and Houshmand (2024) proposed a memetic quantum-inspired genetic algorithm
integrating quantum rotation gate mutations with tabu search to balance exploration and exploitation, en-
hancing convergence speed and solution accuracy, and demonstrate its superiority over existing methods on
benchmark optimization problems. Gunjan and Bhattacharyya (2024) proposed quantum-inspired versions
of GA, differential evolution, and PSO with enhanced crossover, regularization, and dynamic parameter tun-
ing to solve constrained portfolio optimization using over a decade of stock data from NASDAQ, BSE, and
Dow Jones.
Zheng and Zheng (2022) proposed a multi-population parallel non-dominated sorting genetic algorithm
(NSGA-II) with distinct evolutionary strategies that both employed normal distribution crossover and sim-
ulated binary crossover for each population. Furthermore, the algorithm used the Fuzzy C-means and grey
relational projection to yield compromised portfolios for various investors with different risk profiles. Wang
et al. (2022) took market impact cost into account and appended a new local search operator to the NSGA-
II algorithm along with features from global search derived from NSGA-II. Solares et al. (2019) proposed
a multi-objective evolutionary algorithm based on decomposition with confidence intervals that describes
the solutions. Sanjalawe et al. (2025) provided a comprehensive review of the secretary bird optimization
algorithm, detailing its recent advancements, variants, and applications across multiple domains, including
portfolio optimization, while addressing challenges like premature convergence and parameter sensitivity,
and highlighting future research directions for hybridization and adaptive improvements.
Although some reports in the literature make use of penalty functions and infeasibility tolerance for
handling constraints, the vast majority employ a repair mechanism to address this issue (Kalayci et al.
(2019)). Chang et al. (2000) proposed a method to handle CC in portfolio and to ensure that the number of
assets remains within bounded limits. In their repair procedure for GA, if the number of stocks in portfolio
are greater than a maximum K, the asset with the lowest weight would be eliminated from the portfolio. On
the other hand, if it is lower than K, a random stock from parents will be selected. Anagnostopoulos and
Mamanis (2010) presented a tri-objective portfolio optimization model such that the number of assets in the
portfolio should be minimized. Pai and Michel (2009) applied k-means clustering to tackle CC. The k clusters
in k-means would be the maximum number of stocks that the investor would have to choose from among
N investible assets; the authors addressed the problem by selecting only one stock out of each cluster. Cura
(2009) proposed a probabilistic repair method for CC. According to this method, when an asset is to be added
to the portfolio, either a random asset is chosen or one is added with equal probability that has the highest
c-value defined as the mean return to mean risk with respect to the aversion parameter which is not present
in the portfolio. For removing additional stocks, either a random stock is removed or that with the lowest
c-value is with equal probability. For BC, if the weight of an asset is higher or lower than the maximum or the
minimum bound, either the upper bound or the lower one, respectively, is assigned to the asset; otherwise,
the weight of the asset is determined via a formula given in their paper. Zhao et al. (2021) used a similar
approach to handling CC, but the risk aversion parameter was disregarded. Kaucic et al. (2019) proposed
the combined NSGA-II and strength Pareto evolutionary algorithm with a new reproduction process and
compared it with the reproduction process used by Anagnostopoulos and Mamanis (2011). Moreover, they
used the method in Liagkouras and Metaxiotis (2015) to repair solutions to repair solutions. de Melo et al.
(2022) proposed operators within a multi-objective genetic algorithm whose constraints were handled within

the algorithm. Yang et al. (2024) presented a dynamic tri-population multi-objective evolutionary algorithm
that balances convergence, feasibility, and diversity for constrained multi-objective optimization by evolving
multiple populations with adaptive resource allocation and constraint violation handling, demonstrating
competitive performance on 57 benchmarks and 21 real-world problems.
This study presents fast-converging and extensive search strategies in evolutionary algorithms for portfolio
optimization problem under the cardinality constraint, with two conflicting objectives. One feature of the
study is a new encoding procedure designed to facilitate more efficient handling of the CC, which also
enables us to introduce and implement our strategies more easily. A second aspect involves a novel handling
mechanism and a new operator, both introduced not only to ensure the feasibility of the generated solutions
but also to make them feasible in the best possible way. Third, new mating strategies are proposed for
producing solutions and optimizing the searching process. Aforesaid novelties are meant to achieve faster
convergence rate and improve the process of exploration for faster and better approximations, especially in
larger markets. To test the proposed package, it is implemented in multi-objective evolutionary algorithms,
and the improved algorithms are tested and validated against the conventional versions applied to three
well-known indices from the OR-library (Beasley (1990)), namely S&P 100, German DAX 100, Japanese
Nikkei 225, and Tehran Stock Exchange (TSE).
The rest of the paper is organized as follows. Section 2 presents the mathematical model of the cardi-
nality constrained mean-variance portfolio optimization problem. Section 3 describes the proposed approach
including mating strategies, the new operator, CC, and the BC repair techniques. Section 4 presents and
discusses the experimental results. Finally, Section 5 concludes the work and suggests future directions.
2 Mathematical formulation:
MV portfolio optimization consists of a pair of conflicting objectives: maximizing return and minimizing risk.
The multi-objective approach results in a variety of non-dominated portfolios with varying levels of risk and
return suitable for different classes of investors. Each solution represents a tradeoff between the objectives,
forming a curve known as the EF. The EF is a graphical representation of the set of optimal portfolios in a
feasible search space, where no objective can be improved without worsening another. The EF shows the best
possible tradeoff between risk and return, highlighting the set of portfolios that offer the highest expected
return for a given level of risk, or the lowest risk for a given return. The adoption of a multi-objective
approach in this study arises from the knowledge that finding a single solution as a compromise between
both objectives is arduous due to the divergent preferences of investors.
Additionally, incorporating a cardinality constraint in portfolio optimization is particularly important,
especially in real-world scenarios. Generally, achieving diversification does not require investing in all assets
in the market; selecting a subset ofKassets can provide similar benefits at a lower cost for the investor,
although the optimal value ofKremains unclear (Jimbo et al. (2017)). Considering the CC makes the
problem more realistic by reducing management costs and complexity, which are often associated with the
transactions required for large portfolios (Esmaeily and Loge (2023)). It simplifies the monitoring and control
of unrealized profits and losses for investors (Tadonki and Vial (2003)). The concept of CC is widely used in
portfolio optimization, from large firms to high-frequency traders (Leung and Wang (2022)).
The multi-objective CCPOP can be mathematically formulated as follows:
minf 1 =
NX
i=1
NX
j=1
wiwjσij (1)
maxf 2 =
NX
i=1
wiµi (2)
Subject to:
NX
i=1
wi = 1 (3)

Kmin ≤
NX
i=1
zi ≤K max (4)
ϵizi ≤w i ≤δ izi,∀i= 1, ..., N(5)
wi ≥0,∀i= 1, ..., N(6)
zi ∈ {0,1},∀i= 1, ..., N(7)
Equations (1) and (2) are objective functions that seek to minimize risk and maximize return, respectively,
whereNis the number of available assets,w i andw j are the decision variables that represent the proportion
of budget allocated to assetsiandj, respectively,σ ij is the covariance between assetsiandj, andµ i is the
expected return of asseti. Equation (3) ensures that all the budget has to be invested. Equation (4) is the
CC that limits the number of assets in the portfolio, which is delineated byK max andK min representing the
maximum and minimum numbers of assets that can be included in the portfolio, respectively. Furthermore,
zi is an integer variable which is 1 if assetiis included in the portfolio, and 0, otherwise. In this study, we
impose upper and lower limits on CC instead of a fixed number of desirable assets known asK; clearly, this is
more flexible and can cover other types of formulations, as well. It can be transposed either to PN i=1 zi ≤K
when (K min = 1,K max =K,K < N), which means that the number of assets in the portfolio should not
exceed an integer numberK; or to its strict formulation PN i=1 zi =Kwhen (K min, Kmax =K, K < N),
which can lead to rigorous limits on the number of assets. Equation (5) guarantees that if assetiis chosen,
its dedicated proportion lies between [ϵ i,δi] where 0≤ϵ i ≤δ i ≤1,(i= 1, ..., N). Finally, equations (6)
and (7) disallows short selling and specify domains of the decision variables.
3 Methodology:
As mentioned before, approximation algorithms, compared to exact methods, are more effective and reason-
able approaches for addressing the portfolio optimization problem as an NP-hard. Moreover, a multi-objective
approach is preferable due to the opposing objectives sought in such problems. NSGA-II is a well-known
algorithm that is widely used in the literature because of its merits, including its ability to explore the
problem’s search space (Verma et al. (2021)). It also has proven effective in multi-objective optimization,
including portfolio optimization, and is well-recognized within the engineering community (Ma et al. (2023)).
For the purposes of this study, the NSGA-II algorithm was selected to be modified by adopting a new solu-
tion encoding system with new handling mechanisms, and incorporating a new operator to address the CC.
Additionally, its mating strategies were altered to enhance both exploration and exploitation capabilities.
Below is a desctiption of the approach adopted to tackle the cardinality constrained portfolio optimization
problem.
In Subsection 3.1, the solution representation and the approach proposed for handling constraints are
introduced. The overview of NSGA-II is provided in Subsection 3.2. In Subsection 3.3, we present our mating
strategies and the new operator. Subsection 3.4 describes the techniques proposed for handling CC. Finally,
the mechanisms for handling BC are described in Subsection 3.5.
3.1 Solution encoding:
Representing solutions and measuring objective(s) are crucial prerequisites to the application of an EA to
a problem. Although measurement of the objective function for each optimization model is straightforward,
encoding the solution might vary with each model. Encoding solutions has a tremendous impact on the
performance of an EA. When applied to optimization problems, wide use is made of real-coding solution
representation in EAs. In EAs, the size of the solution representation is fixed to the number of assets in the
market and each cell represents the weight of each asset. For CCPOP, this approach requires mechanisms to
remove or add assets if the portfolios are to be made feasible in terms of CC. From a practical perspective
and due to the costs of monitoring and transactions, the most commonly imposed constraint involves a limit
on the maximum, rather than the minimum, number of assets in the portfolio. Furthermore, CC handling
techniques employed for removing additional assets from the portfolio in the encoding systems in question
are typically more time consuming than adding stocks since the number of desirable assets are generally

far less than that of investable ones. Moreover, imposing a minimum of diversification is less common and
less time-consuming since the gap betweenK min and the number of assets in the infeasible portfolio is not
generally large.
We restricted the decision variables from the universe of assets to the upper bound of CC. Our chromosome
is composed of two rows of a fixed size,K max, where each element in the first row is the asset selected for
the portfolio and its corresponding element in the second row indicates its weight in the portfolio.
For better illustration, imagine a POP withK min = 3 andK max = 5. It must be noted that it is
impossible to have more than five assets in this approach because the size of each chromosome is restricted
to five and any values less than that would cause duplicate stocks. However, duplication does not necessarily
mean infeasibility; rather, the chromosome would be feasible as long as there are at least three unique assets
in it. If the number of unique assets in the chromosome falls below three, then the proposed CC handling
techniques come into play to repair the chromosome. Figure 1 depicts the structure of a feasible chromosome
in the above POP example where there are three unique assets (i, j, k) and assetjis repeated three times
in the portfolio. The proportional weights of assetsiandkare their corresponding weights in the second
vector while that ofjis the summation of those of the positions in the second row in which assetjappears
on the first vector. Hence, The capital allocated to assetiis 0.20 that to assetjis (0.15 + 0.25 + 0.10) and
one tokis 0.30 percent of the total budget.
i j j j k
0.20 0.15 0.25 0.10 0.30
Fig. 1: Structure of a chromosome in a POP with size 5
We believe this representation is superior to the standard ones along the following lines. Equation (4)
forces the number of assets in each solution to fall within a predetermined range. However, there could be
violations in both directions that need to be fixed. As opposed to the repairing techniques reported in the
literature that consider both situations, a violation in terms of exceedingK max has already been taken care
of in this approach by the fact that the maximum size of each chromosome is equal toK max.
3.2 Non-Dominated Sorting Genetic Algorithm II:
It is straightforward in single-objective optimization algorithms to determine the fitness and the supremacy
of solutions in the population via sorting them with regard to the objective(s); however, it is slightly different
in multi-objective algorithms. Understanding the concept of dominance is a key point toward understanding
multi-objective optimization problems in which solution (a) is considered superior to (b) if it were better
in at least one objective and equal or better in other objectives. In this case, we would say solution (a)
dominates solution (b) or, conversely, solution (b) is dominated by solution (a). Additionally, if there exist
solutions (a) and (b) and if solution (a), in comparison with solution (b), is superior in one objective but
underperforms in another, then both solutions (a) and (b) are non-dominated since none is superior to the
other.
NSGA-II is a multi-objective algorithm based on GA that is commonly used to solve multi-objective
optimization problems. Similar to other EAs, this algorithm is also based on Darwin’s theory of “survival
of the fittest”. It preserves the better solutions in each generation, known as non-dominated solutions, to
survive and reproduce similar solutions.
The algorithm initializes with a random population of solutions from which offspring solutions are subse-
quently generated via crossover and mutation operators to be added to the original population. Afterwards,
the solutions thus generated are evaluated and sorted to select the better ones for the next generation. A
non-dominated sorting is performed on chromosomes to determine the rank of each individual, with a lower
rank implying better performance. All the individuals in the first rank are initially added, which will survive
in the next generation and are thus eliminated from the sorting process. This process continues until the

number of individuals added reaches a predetermined population size. If the number of individuals with rank
(n) is greater than the remaining capacity of the population size, the crowding distance is applied to main-
tain solution diversity in each front. This approach ensures two advantages; first, solutions with better ranks,
compared to others, survive through each generation and, second, solutions close to each other are elimi-
nated by choosing individuals with distances farther from the others in order to achieve a well-distributed
Pareto front (PF). Once sorting is completed, the same processes are repeated until the algorithm reaches
its stopping criteria. The pseudo code of NSGA-II is given in Algorithm 1.
Algorithm 1Non-Dominated Sorting Genetic Algorithm II
Initialize a random populationp;
whileStopping criteria is not truedo
Produce offspringp
′
with crossover and mutation;
A=p∪p
′
;
Evaluate individuals inA;
Pick the best individuals of size|p|from setAwith respect to their rank and crowding distance values for next
generation;
end while
3.3 Our proposed strategy:
CCPOP can be considered as a two-step optimization problem. In the first step, a subset of stocks out of
the universe of assets has to be determined and in the next phase, capital allocation to selected assets has to
be decided. We, therefore, modified NSGA-II to be more focused on exploring the search space in order to
find high-quality combinations of assets (i.e., the first row of chromosomes) in the specified initial iterations.
Next, the algorithm devotes more efforts to adjusting the proportional weights of portfolios to find their
optimal capital allocations (i.e., the second row of chromosomes). To achieve these goal, new tournament
selections and a modified mutation operator were developed while a strategy was deployed to employ them
throughout the optimization process. Finally, a novel operator referred to as the ‘explorer’ was developed.
T ournament selection:Tournament selection in EAs is meant to manage the selection of individuals to
generate offspring. It is characterized by certain benefits and challenges; while the benefit involves awarding
higher chances to elite solutions to generate offspring that would lead to more promising generations, the
challenge lies in the resulting increased complexity of the algorithm. Two kinds of tournament selection are
then used whose domains of activation are presented in Figure 2.
Knee-based Similarity-based matrix
Iterations
Fig. 2: Range of activation of each tournament selection technique.
The first method is based on the Euclidian distance of points from the utopia point (EP); this is repre-
sented by a knee-based index in Figure 2 and is active forα% of early iterations. In our case, EP is the
imaginary point that entails a solution with the highest return and the lowest risk. It is obvious that if such
a point ever existed, it would dominate all the points in PF. Moreover, points located in the knee area of
PF represent a balance between the two objectives; in other words, they are not too risky and provide more
returns compared to the less risky assets.
If the algorithm finds a proper combination of assets in a shorter time, the savings on computational
resources and time can then be dedicated to readjustment of capital allocations in portfolios. Also, randomly
mating early individual solutions might waste computational resources, resulting in lower convergence rates

since the majority of the solutions in early generations are far from PF. Considering the fact that the
unconstrained PF is oriented toward EP in each iteration and that ease of finding better solutions is sought
in early iterations, the tournament selection as captured by Algorithm 2.
Algorithm 2Knee-based tournament selection
Letp i beith solution from populationp;
Letf i be the coordinate ofp i in the objective space;
Letcbe the coordinate of the eutopia point in iterationi;
Letr e ∼Exp( |p| υ )υ∈Z +;
Letn ci be the rate of crossover in iterationi;
L={x|x⊂p,|x|= [|p|(n ci)],x follows uniform distribution};
di =
p
(fi −c) 2,∀i= 1, ...,|p|;
d
′
= Sortedpbased on their value ofdin ascending order;
forj= 1 to [|p| ∗n ci]do
MateL j withd
′
min(|p|,[re∗|p|]);
Normalize weights considering boundaries;
end for
By picking out individuals from two different sets in Algorithm 2 solutions closer to EP are selected that
can outperform their rivals with respect to offspring generation. Moreover, equal chances are given to the
remaining solutions so that the algorithm would not stuck in local optima by only mating points closer to
EP. By applying minimal guidance, it was ensured that the algorithm would not mate two unsatisfactory
solutions with each other; this additionally led to faster convergence.
The second type of tournament selection is based on similarity of individuals and is activated during
final iterations to mate closer solutions. The idea behind this tournament is that once a decent number of
solutions are found, similar pairs of portfolios that share the same or almost the same combinations of assets
are selected for generating offspring. This ensures that almost the same portfolios with slightly different
weights are produced during the mating process, which in turn guarantees that the algorithm searches for
better capital allocations for each solution. To achieve this goal, it is essential to measure the distance between
each two portfolios only based on their asset combinations in order to mate the most similar solutions. This
is captured by Algorithm 3, in whichDis a|p| ∗ |p|upper triangular matrix whose main diagonal is set to
a large negative number such that no solution is picked out with itself as a pair.
Algorithm 3Similarity-based matrix tournament selection
LetMbe a big number;
Lets i be set of assets incorporated inp i;
forj= 1 to|p|do
fork=jto|p|do
ifj=kthen
Djk =−M;
else
Djk =|{s j} ∩ {sk}|;
end if
end for
end for
forl= 1 to [|p| ∗n ci]do
U={(p j, pk)|D jk = max(D)};
Djk =−1;
Mate solutions inUwith each other;
Normalize weights considering boundaries;
end for

Mutation:Mutation operators are used to explore the whole search space in order to guarantee that the
algorithm will not get trapped in local optima. As already mentioned, the algorithm is designed to explore the
whole search space globally in its initial iterations and search more locally in final iterations. Since mutations
have important impacts on this goal, use is made of various types of problem-specific mutations that may
be divided up into three kinds based on their features and exploration capacity for use at each stage of
optimization. Unlike the crossover operator that chooses an asset and its corresponding weight from parents,
the mutation one operates in a slightly different manner. This operator for our solution representation has
two steps: mutating the first vector holding a combination of stocks, followed by changing the weight of the
incorporated assets. The representation provides the opportunity for various levels of mutation based on its
exploration capabilities. It should be noted that, compared to merely changing the weight of an asset of a
chromosome, swapping an asset in the first vector has a greater power for exploring the search space. The
former most likely finds a solution near its parents and is capable of searching more locally and accurately;
it, however, has less capable of throwing a point farther away in the search space. Adversely, the latter type
of mutation possibly generates offspring much farther away from the chosen parent. It has more power to
throw a point away from its initial position but less accurately. Algorithm 4 presents the mutation techniques
used in the current study.
A dynamic combination of the mutations cited above was employed to achieve an equilibrium among the
blindly created points far from the original ones in order to explore the search space and transfer points
intelligently through the process. Excluding the initial and final iterations that are somewhat biased toward
exploring purposes, the second type of mutation won a greater chance of being selected for mutating solutions.
Regarding the initial iterations where the objective is to find appropriate asset combinations, it is the
third and second types of mutations that are mainly in charge with the setP. As is clear from Figure 3,
creating new portfolios generally yields offspring far from the population, especially in the initial iteration
that is meanwhile capable of preserving diversity and introducing new mixes of assets to the population pool.
Although these features are beneficial throughout the optimization process, they are more valuable in early
iterations.
The principle that supports the use of various sets alongside exponential probability distribution in
the second type of mutations is investors’ propensity to take risks. Assets are characterized by return and
standard deviation (SD) of returns (also called volatility) as their features. Since the historical return of
stocks directly influences Equation (2), assets with higher average returns exhibit a better performance
in one objective. Even though risk objective determination depends on the correlation of assets within a
portfolio, it is also affected by SD of returns; this is shown in Equation (8) whereσ i is SD of returns of asset
iandρis the correlation coefficient.
ρ= σij
σi ∗σ j
σij = (σi ∗σ j)∗ρ
(8)
P s is sorted by the ratio of returns to risks. Assets with a higher ratio are preferable for all investors
with any risk profile since everybody prefers to invest in securities with higher returns and less volatility.

0.0004 0.0006 0.0008 0.0010 0.0012 0.0014 0.0016
Risk
0.003
0.004
0.005
0.006
0.007
0.008
0.009Return
1st type-N(o)
1st type-N(m)
1st type-new weights(o)
1st type-new weights(m)
3rd type(o)
3rd type(m)
2nd type-r(o)
2nd type-r(m)
2nd type-R(o)
2nd type-R(m)
2nd type-r/R ratio(o)
2nd type-r/R ratio(m)
Fig. 3: Effect of each mutation on random individuals in random and different iterations.
Risky assets are more attractive to risk-taking investors who seek to invest and build a diversified portfolio;
hence, stocks with these attributes are more favored and more welcomed in half of the PF that contains
portfolios with higher returns and volatility. The same logic justifies the employment of setP R for risk-averse
investors. Although using an exponential distribution provides a chance of selection for all assets in the sets,
we did not thoroughly disregard setPwith a uniform probability distribution so as to maintain diversity in
the solutions. Using this technique, the algorithm was able to cover more of the search space.
Ultimately, the first type of mutations is more likely to be chosen in the final stage for better allocations of
wealth to selected portfolios since the chance of modifying their asset combination is diminished. Moreover,
according to Figure 3, this type is better capable of searching more locally near selected individuals.
Figure 3 demonstrates the fitness of random points before and after implementing the mutation tech-
niques. The original point for the third type is a random sample from the population and the mutated point
is a randomly generated portfolio. The fitness of points is recorded from different PFs and different iterations
but only graphed together for better depiction of scalability. In this algorithm,randRstand for return and
risk, whileoandmfor original and mutated solutions, respectively. Also,Nstands for the normal random
number method that is the first type.

Algorithm 4Mutations
Letn mi be the rate of mutation in iterationi;
LetP m be the probability of each element being changed;
LetPbe the set holding universe of assets;
LetP r,P R,P s be the universe of assets sorted with respect to their returns,σof returns and ratio of µ σ in descending,
ascending and descending orders, respectively;
Letr u ∼ U(0,1),re ∼Exp( |N| β ),r n ∼ N(0, 1 (Kmax)2α ) ,α, β∈Z +;
ifthe condition for the first type mutations is satisfiedthen
P m = 1 2 (P m);
Perform mutation on assets and pickP {[(ru)|P|]} if replacement is required;
P m = 2(P m);
ifthe condition for normal search near weights is satisfiedthen
wi =w i + max(0, wi +r n) whenever the weight of theith element has to be changed and leave it asw i
otherwise;
else
Generate a new budget allocation for the subjected individuals;
end if
end if
ifthe condition for the second type mutations is satisfiedthen
ifthe condition for setPis satisfiedthen
Perform mutation on assets and pickP {[(ru)|P|]} if replacement is required;;
end if
ifthe condition for setP r is satisfiedthen
Pick random individuals with higher returns than the average in populationi;
Perform mutation on them and pickP r {min(|P|,[r e∗|P|])} if replacement is required;
end if
ifthe condition for setP R is satisfiedthen
Pick random individuals with less risk than the average in populationi;
Perform mutation on them and pickP R {min(|P|,[r e∗|P|])} if replacement is required;
end if
ifthe condition for setP s is satisfiedthen
Perform mutation on them and pickP s {min(|P|,[r e∗|P|])} if replacement is required;
end if
wi =r u whenever the weight of theith element has to be changed and leave it asw i otherwise;
end if
ifthe condition for the third type mutation is satisfiedthen
Create [nmi ∗ |p|] completely new portfolios;
end if
Normalize weights considering boundaries;
Explorer:Assume an individual that violates CC. To repair it, additional asset(s) must be added to it while
its previous capital distribution is assigned without the possibility for additional asset(s). Clearly, adding new
stock(s) with no readjustment in fund allocation might lead to the worst performance regarding objectives.
However, modification of weights might help obtain better results when new portfolios or new combinations
of assets are added to the population. With these considerations in mind, we designed a new operator called
‘explorer’ to readjust capital allocation of individuals so that better solutions could be sought. As it intends
to readjust budget allocation in the portfolio, the main purpose behind the explorer is to find better weights
for repaired individuals while it could be generally used to find better solutions as well. If the latter purpose
is intended, it should be activated only after phase two has started.
The idea is to move a solution (subjected individual) in the search space toward another (candidate
solution) that is not dominated by the chosen solution and, thus, explore the space in quest of better results.
A candidate solution is the subjected portfolio with a new distribution of wealth that is produced either by
a heuristic capital distribution technique or randomly. Since it is mandatory to pick out only one portfolio as
the candidate one and because several budget allocation methods are employed, the non-dominated solutions
need to be modified in order to pick out the best in case multiple alternatives are available. To achieve this

goal, improvements in the objectives gained by each heuristic technique, as compared to the subjected
individual, may be calculated via Equation (9).
I(T, C) =λ( Cr
Tr
−1) + (1−λ)(1− CR
TR
) (9)
where,T r andT R represent the return and risk associated with the targeted portfolio, respectively;C r
andC R are potential candidate’s return and risk; andλis an importance coefficient of objectives, where
λ= 0,λ= 1 only consider improvements gained in risk and return objectives, respectively. Meanwhile,
λ= 0.5 means no objective is superior to another. Finally, it should be noted that alteringλvalues can skew
the exploration process in favor of certain objectives.
Algorithm 5 is the pseudo-code for selecting the candidate individual from a targeted portfolio. The
H 1 technique involves equal distribution of money among all the assets in the portfolio while random fund
allocation is represented byH 2. In theH 3 technique, an asset with a high volatility receives a lower proportion
of the budget; this technique is more suitable for risk-averse investors.H 4 allocates funds to each asset based
on their return volatility ratio such that the higher the return of an asset compared to its volatility, the more money
is invested in that asset in the portfolio. Finally,H 5 is similar toH 4 but only more sensitive to volatility so
that assets with higher volatility values are restricted in the portfolio.
Using this approach to select one individual out of a non-dominated set, we prefer the one solution that
contributes more to one objective and sacrifices less of another. Figure 4 depicts all the possible outcomes
of the operator indicating that the individuals dominated by the targeted portfolio are deleted from the
selection procedure. Figure 4(a) shows the situation in which none of the heuristic techniques dominates the
original solution, nor are they dominated by it. In this situation, a solution with a higher value of Equation
(9) is chosen for exploration purposes. Figure 4(b) illustrates the condition that some techniques, namely,
H 1, H4 andH 5, dominate the targeted portfolio; in this case, only these methods are selected for evaluation
against Equation (9). This signifies that the one solution with higher contributions to both objectives is
selected since it dominates the original solution. In the next step, the space between the targeted portfolio
and the candidate is explored using Equation (10).
0.00060 0.00065 0.00070 0.00075 0.00080 0.00085
Risk
0.0066
0.0067
0.0068
0.0069
0.0070
0.0071
0.0072
0.0073Return
Original portfolio
H4
H5
H2
H1
H3
(a)H js and original portfolio are in a non-dominated set.
0.00019 0.00020 0.00021 0.00022 0.00023 0.00024 0.00025 0.00026
Risk
0.0032
0.0034
0.0036
0.0038
0.0040Return
Original portfolio
H4
H5
H2
H1
H3 (b)H 1, H4, H5 dominate the original portfolio.
Fig. 4: Heuristic fund allocation methods in the explorer operator.
w1 i =



w1 i + (ru(0, c))(w2 i −w 1 i )r u(0, c)≥ −w1 i w2 i −w 1 i
ru(w1 i , w2 i ) otherwise
, i= 1, ..., K max (10)

wherew 1 i ,w 2 i represent allocations to the asset in positioniin the subjected individual and candidate
solutions, respectively.r u(0, c) andru(w1 i , w2 i ) are the uniform random numbers between (0, c) and (w1 i , w2 i )
respectively wherec= 2.
Algorithm 6 explains the process of exploring and selecting the best individual for a targeted solution and
a candidate. The main goal of this operator is to find a better allocation of wealth to the chosen individual
that is randomly picked out at no more thanΩattempts. In this situation, three possible scenarios can be
envisioned. First, all the heuristic methods fail to detect a portfolio that is not dominated byT. In this case,
we skip Algorithm 6. Second, portfolioCdominatesT. In this case, only the solution that dominatesCis
accepted as an offspring and is passed on for subjection to the non-dominated sorting procedure since we
already haveC. The last possible and more common situation is whenCandTare in a non-dominated
set. In this scenario, Algorithm 6 explores their surrounding space for a maximum number ofΩtimes. If
a better solution dominatingTis found beforeΩis reached, the search process will be terminated. This
will save computational resources for the obvious reason that it is pointless to continue the search process.
However, ifTremains undominated by the solutions found, once the dominated portfolios are eliminated by
T, the algorithm turns to equation (9) to select the individual that adds more value to one objective while
it sacrifices less of the other.
Algorithm 5Selecting the candidate individual
LetS i be the assetiin the targeted portfolio;
LetH j i beSwhere its corresponding capital allocated to assetiis determined with methodj;
Letηbe a small positive number;
z={};
for allassets inSdo
H 1 i =k −1 max;
H 2 i =r u(0,1);
H 3 i = 1 σi ; ifµ i ≥0then
H 4 i = µi σi ;
H 5 i = µi σ2 i ;
else
H 4 i , H5 i =η;
end if
end for
Normalize eachH j considering boundaries if necessary;
H={H j |H j is not dominated by S};
z={z∪H j |H j dominatesS};
ifz=∅then
Candidate ={H j |arg max j∈H I(T, Hj)};
end if
if|z|= 1then
Candidate =z;
end if
if|z|>1then
Candidate ={H j |arg max j∈z I(T, Hj)};
Preserve rest of them;
end if

Algorithm 6Searching process
LetTandCbe the targeted and candidate solution respectively;
LetΩbe the maximum number of attempts to find a desirable solution;
LetFbe a boolean flag that is True ifCdominatesTand False otherwise;
y={};
fori= 1 toΩdo
Ei = ChangedTwith equation (10);
NormalizeE i considering boundaries if necessary;
ifFis Truethen
ifE i dominatesCthen
ReturnE i;
Break;
else
Continue;
end if
else
ifE i dominatesTthen
ReturnE i;
Break;
else
ifI(E i, T)>0then
y=y∪E i;
end if
end if
end if
end for
ify=∅then
ReturnC;
else
Return theE i inywith the highest value ofI(E i, T);
end if
Figure 5 demonstrates eachE i found by the operator along withTandCin the last scenario, where no
better solution that dominatesThas been found. Green points represent the chosenE i. Whilst this operator
is suitable for such general purposes as generating elite offspring, its main objective is to readjust the capital
allocation of solutions that are repaired via the CC handling algorithms. It is also worth noting that, as
opposed to the other operators, this operator offers the possibility for variable rates of offspring generation.
In each iteration, the repaired individuals have a higher priority for selection as a targeted portfolio. If the
repaired solutions are not sufficient to promote a predetermined rate of offspring generation, then random
individuals will be chosen to fill the gap. Nevertheless, there is a subtle contrast between these situations in
that if the targeted portfolio is merely a repaired individual, the output is then either the individual itself or
a portfolio that dominates it, in which case the portfolio will directly replace the solution since our purpose is
improving the solution rather than exploring the space or generating new offspring. However, if the targeted
portfolio is not a repaired individual, the discovered solution will be substituted for the targeted portfolio
if it is a superior one. It will be appended to the pool of solutions as an offspring provided it is neither
dominated by the targeted portfolio nor does it dominate it.

0.00044 0.00046 0.00048 0.00050 0.00052
Risk
0.0062
0.0063
0.0064
0.0065
0.0066
0.0067Return
T
C
Chosen E(i)
E(i)
0.0016 0.0017 0.0018 0.0019 0.0020 0.0021 0.0022 0.0023
Risk
0.0087
0.0088
0.0089
0.0090Return
T
C
Chosen E(i)
E(i)
0.00095 0.00100 0.00105 0.00110 0.00115 0.00120
Risk
0.0073
0.0074
0.0075
0.0076
0.0077
0.0078
0.0079Return
T
C
Chosen E(i)
E(i)
0.00017 0.00018 0.00019 0.00020 0.00021
Risk
0.0025
0.0026
0.0027
0.0028
0.0029
0.0030
0.0031Return
T
C
Chosen E(i)
E(i)
Fig. 5: Explorer operator and its output (Ω= 5).
3.4 Cardinality constraint handling techniques:
This Section presents an approach to handling CC. Given the solution representation explained above, it is
solely necessary to repair algorithms to append assets to those portfolios that violate Equation (11) since
violation in Equation (12) is not possible.
NX
i=1
zi < Kmin, i= 1, ..., N(11)
NX
i=1
zi > Kmax, i= 1, ..., N(12)
The salient question to ask with regard to appending new assets to a portfolio in the repairing stage
is which stocks must be added. We propose three techniques to answer this question. The first one is
called ‘associated-based technique’, which is blind to asset features. It repairs portfolios by analyzing the
approximation curve and extracting the patterns of the current generation to repair solutions for the selection
of the next generations. The second, called ‘clustered-based technique’, evaluates assets to determine a cluster
of them suitable for the repairing process. Finally, the ‘threshold-based technique’ searches for a combination
of low-correlated assets to append to the violated portfolio; the assets thus found are compatible with all in
the portfolio.
Once the assets to be included in the portfolio are identified, they will be replaced for the repeated
stocks. Owing to the fact that the repaired solutions are being marked for weight readjustment purposes
via the explorer operator, no specific method is required for replacement but it will simply suffice to replace
them with the repeated ones. In all the methods to be discussed more thoroughly in this article, the chosen
assets are appended to a set representing unique assets in the relevant solution representation before they
are replaced in the encoding system with the lowest allocated repeated stocks.
Three cardinality handling techniques are proposed herein to keep the solutions feasible. Subsection 3.4.1
describes the associated-based technique while the score-based and the threshold-based ones are described
in Subsection 3.4.2 and Subsection 3.4.3 respectively.
Associated-based technique:Individuals in each zone of the PF vary in their composition of assets and
their attributes. An asset can appear anywhere in the approximation curve accompanied by different stocks.
Since greedy EAs rely on the idea that only the fittest can survive and thrive, solutions that survive and
reach generationienjoy more qualified features. We applied a technique to repair individuals based on the
frequency with which assets appear in the violated portfolio. The idea behind the associated-based technique
is to extract and exploit these features in the process of repairing cardinality violations. By adopting this
strategy, even minute features of groups of solutions that were more qualified than others are incorporated
into violated solutions to handle CC.
To determine how strong the relationships of assets are in each iteration, a comparison set is needed that
is defined as a set containing the mix of assets selected through the evolution process by the algorithm to
construct portfolios in the approximation curve for generationi. Given that the comparison set can be as
large as the population size, it is time-consuming to check the stock associations in all the portfolios in each

generation. Additionally, an asset appears alongside various other assets in each region of the approximated
curve. Moreover, it may not be appropriate to repair a portfolio placed in a segment where high-risk solutions
are located in the curve based on the data extracted from risk-averse individuals because it combines the
features of different kinds of solutions. Finally, each solution in the approximated PF has features closer to
its neighboring individuals.
To address these issues, we reduce the size of the comparison set by clustering solutions in PF. Clustering
is the process of grouping individuals with the intention of maximizing similarities and minimizing dissim-
ilarities within the clusters. By reducing the size of the comparison set in this way, we diminish the size of
assets from all those present in the current generation to the adjacent stocks, creating solutions close to the
violated portfolio, and picking out those that more regularly co-occur with the elements of the solution that
did not satisfy CC.
Clustering solutions have a direct impact on the quality of this technique. There are several options for
clustering. The ideal one is the k-means algorithm employed to determine the number of clusters via the
elbow method. The obvious drawback associated with this method is the additional complexity that k-means
will add to our algorithm. Given the fact that the individuals in POP have to be clustered based on their
returns and risks, clustering them based on solely one of the objectives (risk values used in the present case)
can be a reliable estimate that avoids the use of K-means algorithm with numerous features. Another option
is to divide the risk objective up into equal intervals based on the highest and lowest risk values at intervals
defined by Equation (13):
Intervali = [Rmin + (i−1)x, Rmin + (i)x], i= 1, ..., m(13)
whereR min andR max , respectively, are the minimum and maximum risks of the present portfolios in the
iteration;mis number of clusters, andxis the step size calculated as Rmax−Rmin m . Each solution whose risk
value lies within periodibelongs to clusteri.
In this clustering technique, compared to the previous ones, more solutions are labeled as prime clusters,
even in curves where all the solutions are equidistant from their neighbors. This is because, at equal intervals,
more portfolios can lie on steep lines compared to nearly horizontally-shaped individuals in high-risk areas.
In a situation with a greater density in low-risk areas in the approximation curve, the comparison set in the
initial clusters contains many more assets while the last clusters suffer from inadequacy of stocks to allow
accurate assessment of their relationships. To address this issue, we consider another clustering method that
groups individuals into equal portfolios. Solutions are sorted in an ascending order based on their risk values
with members of clusterispecified as follows:
Clusteri = [ i−1 m (P), i m (P)], i= 1, ...,m (14)
wherePis population size.
The range of sorted solutions that belong to clusteriis determined for each value ofi. Thus, high values
ofmyield sparse comparison sets while large comparison sets arise from smaller values. It is, therefore,
clear that the value ofmshould be specified in such a way that a balance is maintained among the various
scenarios described above.
The general idea behind this method is to repair each individual based on the data provided by the
comparison set in its cluster. Nevertheless, if a problem arises with the comparison set of portfolioi, such
as low size or lack of sufficient assets, another set must be constructed for comparison. Solutions located in
the knee area of the PF are assumed to be more desirable to decision-makers due to the balance between
the two objectives. Accordingly, the following normal random number whose mean is the middle cluster was
adopted to select a comparison set for these occasions:
rn ∼ N(m 2 ,1) (15)
It must be mentioned that the underlying idea is to repair portfolios based on good individuals, rather
than random ones, to reproduce their features. It is, therefore, crucial to give some time to the algorithm to
build a reasonably reliable Pareto curve for the repairing process. To this end, the technique is deactivated
until certain iterations have passed. Algorithm 7 captures the associated-based handling strategy.

Score-based technique:In this method, assets are clustered and portfolios repaired based on the com-
parative overall performance of clusters. The idea is to limit the number of assets from the universe of assets
Pto a cluster of assetsP Rso that fewer assets are analyzed more accurately. Having clustered assets into
mgroups, a measurement approach is required to evaluate the performance of each cluster to select one.
SupposeObe the file containing the correlation data of all the assets sorted in an ascending order based on
correlation values. The score for clustersiandjwill be the numbers of times an asset from clustersiand
jhas appeared in the topα% ofO. Ifαis too small, the data may not be reliable and if it is too large,
it takes highly correlated stocks into account which are of no interest to our purposes. Once the value ofα
is determined, the value ofmmay be said to play a crucial role. If the assets do not cluster uniformly, the
score of clusteri, which contains a larger population of assets compared to those of the rest of the clusters,
is expected to be higher only due to the frequency the assets from clusteriappear in the topα% of the
records, rather than due to their lower correlation values.
Algorithm 7Associated-based handling
LetG i be required assets to append to the solutionito repair CC;
LetP Vi be the set of assets that is included in the portfolioithat violated CC;
LetP Cij be the portfoliojin comparison set related to the violated portfolioi;
for allViolated individualsdo
qi ={P Vi};
Create a key-value arrayVwith keys of{
|P Cij |[
j=1
(P Cij)} \ {P Vi}and initial values of 0;
for allP Cij do
ifP Vi ∩P Cij =∅then
Continue;
end if
ifP Vi ∩P Cij ̸=∅andP V i ̸=P Cij then
Add|P Vi ∩P Cij|to values ofP V i△P Cij inV;
end if
end for
if|V|=G i then
qi =q i ∪V;
end if
if|V|< G i then
qi =q i ∪V;
qi =q i ∪ {x|x∈ {P\q i},|x|=G i − |V|};
end if
SortVin descending order based on its values;
if|V|> G i andthe value ofG ith element ofVis greater thanG i + 1ththen
Add firstG ith elements ofVto theq i;
end if
if|V|> G i andthe value ofG ith element ofVis equal toG i + 1ththen
v= value ofG ith elements ofV;
U= assets inVthat have a lower value thanv;
qi =q i ∪U;
AddG i − |U|assets with the value ofvthat have highest µi σi ratio to the violated portfolio; end if
Mark theq i to be optimized with the explorer operator;
end for
Returnq i;
While equally and randomly grouping assets is a solution that immediately comes to mind, this approach
entails running the risk of having unreliable random data. In this case, the assets were clustered using the
K-means algorithm to overcome the above problem and the elbow method was employed to determine the

value ofm. Subsequently, the score set was normalized by dividing the score values of clustersiandjby
the sum of the sizes of both clusters. Algorithm 8 is the pseudo code capturing the score-based technique.
To recapitulate, a cluster will be picked out from the set of candidate clusters based on the score values
of the clusters. Next, either a random stock from the selected cluster will be picked out or the assets in the
cluster are analyzed and the best one is selected based on the normalized sets ofWandY, withλbeing a
parameter ranging between 0 and 1 that specifies the importance ofWandY. In the final stage, an asset
from the chosen cluster that has achieved a higher rank will be appended to the violated portfolio. It is worth
mentioning that, if CC is to be tackled via this technique, sets likepv, CRandFare generated once for each
market data to serve as input to the algorithm and not to be calculated through the process of optimization.
Threshold-based technique:The goal in this technique is to append assets that have low correlations
with already chosen assets in the violated portfolios. Even though the process seems straightforward, it is
not rational to check all the possible assets with all the elements in violated individuals since the process is
cumbersome. Also, the difficulty increases significantly with growing number of assets. To address this issue,
a new set was built and fed into the algorithm in order to limit the number of assets; the number is limited
by a correlation thresholdγthat can be any value in the top percentile and is dependent on the data of
each market. Basically, the value ofγdefines a trade-off point between time and accuracy in this method.
Algorithm 9 explains our approach.
Initially, a stock should be picked out from a violated portfolio to analyze the candidate assets. Since not
all the assets are to be considered for comparison against each selected stock, the order in which the assets
are selected affects the outcome; this is because the candidates will form a new pool of assets as a result each
asset being picked out. In this situation, either of two approaches could be adopted. Random rearrangement
is one possible option; however, we opted for the second one that orders them based on their ratios of µ σstating that the higher the ratio, the sooner the asset will be selected.
Ift=|P V i|the candidate has a correlation of less thanγwith all the assets in the violated portfolio; this
is the ideal scenario for our purposes. What we call ‘the strictness coefficient’ is captured by |B| φ ; it starts
with a value of 1, meaning that either a chosen asset has a correlation lower thanγwith all the assets in the
portfolio or that candidate is discarded. This coefficient is dependent on setBsuch that the more stocks get
eliminated fromB, the less rigid it becomes due to the fact that fewer stocks are available for comparison,
and that if no stocks are left, the portfolio cannot be repaired. Stocks with a higher correlation thanγare
gradually permitted to be added during the repair process. Finally, each setuis sorted, which helps the
low-correlated ones to be found faster.

Algorithm 8Score-based handling
LetP Ri be assets in clusteri;
Letpv j be the cluster of assetjinP V i;
LetCR ij be the correlation score of clusteriandj;
Letτbe the chance of adding a random asset from the chosen cluster;
LetF i be the topΨhigh scored clusters withpv j,Ψ∈N +, Ψ≤number of clusters;
for allViolated individualsdo
whileG i ̸= 0do
Q={
|P Vi|[
i=1
Fi};
Θi =
X
j∈pv
CR ij,∀i∈Q;
U={P R i :i= arg max i∈Q Θi} \ {P Vi};
ifrand(0,1)< τthen
Add a random asset fromUtoP V i;
Gi =G i −1;
else
Wi = µi
σi
,∀i∈U;
Yk =
X
j∈P Vi
σkj ,∀k∈U;
W={ x max(W) :x∈W};
Y={ min(Y) x :x∈Y};
κi =λ(W i) + (1−λ)(Y i),∀i= 1, ...,|U|;
AddU arg max
i∈U
κi toP Vi;
Gi =G i −1;
end if
end while
Mark the repaired portfolios to be optimized with the explorer operator;
end for

Algorithm 9Threshold-based handling
LetIbe a binary flag that take value 1 if assetsi, jhave lower correlation ofγand 0 otherwise;
LetSC i be the assets that have correlation less thanγwith assetithat is sorted in ascending order;
for allViolated portfoliosdo
φ=|P Vi|;
B={P V i};
for allP Vi do
ifG i = 0then
Break;
end if
b={x|arg max
x∈B
( µx
σx
)};
U={SC i |i∈b} \ {P Vi};
for allu∈Udo
ifG i = 0then
Break;
end if
t=
X
x∈P Vi
Iux;
ift=|P V i|then
P Vi =P Vi ∪u;
Gi =G i −1;
else ift≥( |B| φ )(|P Vi|)then
P Vi =P Vi ∪u;
Gi =G i −1;
end if
end for
B={B} \ {b};
end for
Mark the repaired portfolios to be optimized with the explorer operator;
end for
3.5 Boundary constraint handling technique:
To handle BC, a modified version due to Chang et al. (2000) was employed to ensure boundary feasibility
in our solution representation. The constraint guarantees that the position of each allocated capital corre-
sponding to assetiin the encoded solution stays betweenϵ i, δi while the summation of all the positions
is equal to unity. In our encoded solution, this technique exhibits perfect performance in handling BC for
Kmin =K max However, the moreK min andK max diverge from each other, the chances for the method to fail
increases due to repeating assets. In our problem, if assetiappears more than once in the encoded solution,
the summation of all those positions should also vary betweenϵ i, δi; this calls for the repair of these types
of violations to be duly considered. The BC repairing stage is the last step in each run of the algorithm
proposed in this study. Hence, all the chromosomes follow the cardinality policy, all positions observe BC,
and the total proportion of money allocated to all is equal to our budget. Thus, there is nothing else to do
but to check for the boundary violation of repeated assets and, thereby, either to assign the violated amount
to one asset or to distribute it among others.
Nonetheless, the repair will not be possible if either of two conditions hold. The first involves the non-
uniqueness of assets in a chromosome in the sense that if there are only a few unique assets in the encoded
solution while the rest of the positions are just duplicates of those assets, it is possible that the total budget
allocated to assetiwill violateδ i even if all the positions have a value ofϵ i; that is, the lowest possible weight
allowed for investment below which the chromosome will be overexposed to asseti. The second situation
causing a problem is when the summation of the upper bounds of all unique assets falls below unity while
the summation of all the positions equals unity. These two situations indicate that even though the solution
follows the cardinality policy, assets are noticeably inadequate. Both cases will cause problems to the repair
process. Although one approach to address this problem is to delete such problematic portfolios on grounds of
low chances for such situations to occur, these solutions are still repaired for the BC repairing process because

the computational resources, time, and energy are spent on them. Algorithm 10 captures this approach for
lifting the problems cited.
In both scenarios, a new asset has to be replaced with another in an encoded solution. Because this is the
last step in a run, unlike in the CC handling techniques in which weights are to be optimized after the process,
it does matter which position of the stock to remove from the chromosome. New assets are replaced for those
in positions with the least contribution to the assets’ total allocation so that the original portfolio experiences
a minimal change. The contribution of each position is defined as the capital proportion associated with the
asset in that position divided by the weight of that asset in the portfolio. When the problem is a lack
of unique assets, assets from the current generation are selected to repair them. Moreover, if an encoded
solution is over-exposed to an asset, an initial attempt is to determine whether it could be repaired using its
constituent assets since, in this way, the modification the portfolio undergoes is less than that due to adding
another asset from the generation.
Once all the solutions are converted into the desirable format, the violated chromosomes will have to be
readjusted. The only violation that can take place is that of the upper bound of assets due to duplication.
So, it is necessary to figure out the extent of upper bound violation by an asset. Moreover, the amount of
capital that assets are allowed to absorb in order for them to stay feasible needs to be determined. This is a
two-stage process. First, the violated amount should be subtracted from the specific position that violated
the upper bound. In the next step, this amount must be allocated to another feasible position of another
asset in our encoded solution. The question that arises at this juncture is which position of an asset can be
subtracted from or allocated to. Clearly, it is reasonable to terminate the process in a minimum number of
iterations. In each step, therefore, we need to determine the violated amounts that can be subtracted from
or allocated to a position. This is advantageous on economic grounds since it would take place in one swoop,
rather than in several steps, without the need for removing that amount in fractions and distributing them
among multiple positions. Algorithm 11 explicitly illustrates the BC handling technique.

Algorithm 10Controlling cardinality
Letp j i be the assetjfrom the portfoliop i;
Letm jk i be the proportion allocated to assetjin positionkfromp i in our solution representation;
LetS jk i be the assetjin positionkfromp i in our solution representation;
Letχ j i be the lowest contributed position of assetjinp i in encoded solution;
LetP Gbe the set of all assets that participated in the approximation curve in current generation;
fori= 1 to|p|do
while
X
j∈pi
δj <1do
if|p i|=K max then
U={x|x∈ {P G\p i}, δ x ≥(1−
X
j∈pi
δj),|x|= 1};
pi =p i \ {pl i |l= min(χ j i )∀j∈p i};
Sjk i =U,wherek={min(χ j i )∀j∈p i};
end if
if|p i|=K max −1then
U={x|x∈ {P G\p i}, δ x ≥(1−
X
j∈pi
δj),|x|= 1};
Sjk i =U,wherek={χ j i | |mj i |>1,∀j∈p i,};
else
U={x|x∈ {P G\p i},|x|= 1};
Sjk i =U,wherek={min(χ j i ),|m j i |>1,∀j∈p i};
end if
pi =p i ∪U;
end while
forj= 1 to|p i|do
whileϵ j|mj i |> δj,do
U={x|x∈ {p j i |ϵ j(|mj i |+ 1)≤δ j,∀j∈p i},|x|= 1};
ifU̸=∅then
Sjk i =U,wherek=χ j i ;
else
U={x|x∈ {P G\p i},|x|= 1};
pi =p i ∪U;
Sjk i =U,wherek=χ j i ;
end if
end while
end for
end for

Algorithm 11Allocation repairing process
Letϕ j i be the total proportion of budget allocated to assetjinp i;
fori= 1 topdo
aj =ϕ j i −δ j,∀j= 1, ...,|p i|;
for allAssets inp i witha j >0do
ifmax(m j i )−a j ≥ϵ j then
max(mj i ) = max(mj i )−a j;//Subtracta j from the largest position
l, h={(l, h)|(ϕ l i +a j)≤δ l, a l <0,|l|,|h|= 1,∀l∈p i , h∈m l i};
ifh̸=∅then
al =a l +a j, mlh i =m lh i +a j;
aj = 0;
else
whilea j >0do
l, h={(l, h)|a l <0,|l|,|h|= 1,∀, l∈p i , h∈m l i};
t=m lh i ;
mlh i = min(δl, mlh i +a j);
aj =a j −(m lh i −t), al =a l + (mlh i −t);
end while
end if
else
whilea j >0do
U= max(m j i );
max(mj i ) = max(ϵj,max(m j i )−a j);//Remove maximum allowed weight from the largest position
aj =a j −(U−max(m j i ));
l, h={(l, h)|ϕ l i + (U−max(m j i ))≤δ l, a l <0,|l|,|h|= 1,∀l∈p i , h∈m l i};
ifh̸=∅then
mlh i =m lh i + (U−max(m j i ));
al =a l + (U−max(m j i ));
else
t=U−max(m j i );
whilet >0do
l, h={(l, h)|a l <0,|l|,|h|= 1,∀, l∈p i , h∈m l i};
t
′
=m lh i ;
mlh i = min(δl, mlh i +t);
al =a l + (mlh i −t ′ ), t=t−(m lh i −t ′ );
end while
end if
end while
end if
end for
end for
Algorithm 12 summarizes the modified NSGA-II, on which our strategies are implemented to illustrate
the chronological order of each step, all in a single view. It is seen that a random population of portfolios
of the upper bound of cardinality is initially generated. Next, the algorithm starts its search for the mating
process using phase one policies. After mating solutions and generating offspring, cardinality and boundary
constraints are handled. In this process, use is made of a combination of all the repair techniques described
above. If the associated-based handling technique is adopted for repairing the portfolios, the algorithm checks
whether a certain number of iterations has passed or not. If not, then solutions in that specific generation are
not repaired. The reason behind this strategy is to give time to the solution to mate with themselves rather
than artificially manipulating them from the beginning. The maximum number of iterations for the handling
technique to remain deactivated is less than that at the beginning of stage two. Once CC is repaired, the
solutions that violated BC are also repaired. As a last step of each iteration, the parents and offspring are
subjected to the non-dominated sorting process and crowding distance functions whereby the best individuals
are selected for the next generation. Phase two is accomplished in almost the same manner with some minute

changes. In addition to changes in mutations and crossover policies, the explorer operator is activated in
even iterations to generate offspring independently if the number of repaired individuals falls below certain
levels.
Algorithm 12Proposed approach implemented on NSGA-II
LetI M be the maximum iteration;
LetΠbe the first iteration of the second phase, 1 2 IM < Π < IM ;
Letn i mark be the number of repaired solutions in iterationi;
Letn opt be rate of producing offspring with explorer operator;
LetΦbe the last iteration that Algorithm 7 stays deactivated;
Initiate a random population p;
fori=: 1 toI M do
ifi < Πthen
C= Crossover(p, Phase one policies for mating individuals in iterationi);
M= Mutation(p, Phase one policies for mutating individuals, Exclude first-type);
A=M∪C;
ifAlgorithm 7 is a candidate for handling CCandi≤Φthen
Do not repair CC in violated solutions inA;
else
Repair CC in violated solutions inA;
end if
else
C= Crossover(p, Phase two policies for mating individuals in iterationi);
M= Mutation(p, Phase two policies for mutating individuals,Exclude third-type);
A=M∪C;
Repair CC in violated solutions inA;
ifn i mark <[(p)n opt]andi%2 = 0then
O= ([(p)n opt]−n i mark) offspring produced by explorer(p);
A=A∪O;
end if
end if
repair BC in violated solutions inA;
p= individuals of size|p|selected with Non-dominated sorting and crowding distance(A);
end for
4 Experiment results and discussion
This section compares the performance of the proposed strategy against the conventional solution-encoded
NSGA-II. Comparisons are also made between the proposed approach and the conventional NSGA-II using
our solution representation but only with normal mating strategies in order to verify the effectiveness of the
proposed strategies and their impacts on convergence rate. For this purpose, the approach proposed herein
was implemented on three markets in the OR-library benchmark dataset, namely, DAX 100, S&P 100, and
Nikkei 225 containing 85, 98, and 225 assets, respectively. Moreover, weekly prices of the assets obtained
from TSE over the period from 29 March 2017 to 3 May 2023 were exploited while the stocks that had not
been traded more than several weeks during the study period were excluded; this resulted in a pool of 418
assets.
For evaluation and comparison of the algorithms, the following four performance indicators were em-
ployed. 1) Hypervolume (HV) (Zitzler et al. (2003)) measures the area under the approximation curve with
respect to a reference point which is a point dominated by all the solutions; 2) Generational Distance (GD)
(Hemici and Zouache (2023)) measures the average distance of points of the approximation curve to their
closest point in the unconstrained PF; 3) Inverted Generational Distance (IGD)(Chen et al. (2021b)) is
similar to GD but calculates the distance of each point in unconstrained PF to its closest point in the
approximated curve; and, 4) Diversity metric∆(Deb et al. (2002)) measures the spread in solutions by
calculating the distance of consecutive solutions while considering the distance of the approximated curve

from extreme solutions. While lower values of GD, IGD, and diversity metric are desirable, higher HV values
represent better solutions. However, GD can cause confusion in the comparison of two curves when they are
not distributed within the same range. Imagine two approximation curves A and B where A dominates all
points in B with few additional points of a greater range compared to B located in the tail of A. In this case,
the GD of A could be even higher than that of B due to those points. To deal with this, we normalized the
generational distance metric by dividing it by the distance of boundary points found by each algorithm. To
prevent confusion with GD, this new metric was named ‘Modified Generational Distance’ (MGD). Figures
6,7,8,9 demonstrate box plots of the performance indicators for NSGA-II with standard solution representa-
tions (real-value coded chromosomes with the population size of universe of assets) and the modified NSGA-II
proposed herein. The reported results are obtained from 100 iterations for both algorithms with population
size of 100,ϵ i = 0.01, δi = 0.99∀i, and PN i=1 zi = 10. In the standard encoded NSGA-II, the BC handling
follows Chang et al. (2000) and whenever the number of assets in the portfolio violates the upper or lower
bounds of CC, a random stock is removed from or added to the portfolio, respectively. All the algorithms
are implemented in Python and ran on a personal computer Intel(R) Core(TM) i7-4500U CPU @ 1.80GHz
and the results are recorded in 10 runs. Evidently, the approach proposed in this study is superior in all
performance indicators for all the selected markets to the commonly encoded NSGA-II. Furthermore, the
gap between the mean values of each indicator become more obvious as the number of assets increases. These
results indicate the effectiveness of our approach regarding searching ability.
Our NSGA-II NSGA-II
0.0030
0.0035
0.0040
0.0045
0.0050MGD
Our NSGA-II NSGA-II
0.0002
0.0003
0.0004
0.0005
0.0006IGD
Our NSGA-II NSGA-II
1.95
2.00
2.05
2.10
2.15
2.20
2.25
2.30HV
1e 5
Our NSGA-II NSGA-II
0.625
0.650
0.675
0.700
0.725
0.750
0.775
0.800Diversity Metric
Fig. 6: Comparison of performance indicators for DAX 100.
Our NSGA-II NSGA-II
0.0030
0.0035
0.0040
0.0045
0.0050
0.0055
0.0060
0.0065MGD
Our NSGA-II NSGA-II
0.00010
0.00015
0.00020
0.00025
0.00030IGD
Our NSGA-II NSGA-II
1.55
1.60
1.65
1.70
1.75HV
1e 5
Our NSGA-II NSGA-II
0.64
0.66
0.68
0.70
0.72
0.74Diversity Metric
Fig. 7: Comparison of performance indicators for S&P 100.

Our NSGA-II NSGA-II
0.004
0.006
0.008
0.010MGD
Our NSGA-II NSGA-II
0.00004
0.00006
0.00008
0.00010
0.00012
0.00014
0.00016IGD
Our NSGA-II NSGA-II
5.2
5.3
5.4
5.5
5.6
5.7
5.8HV
1e 6
Our NSGA-II NSGA-II
0.575
0.600
0.625
0.650
0.675
0.700
0.725
0.750Diversity Metric
Fig. 8: Comparison of performance indicators for Nikkei 225.
Our NSGA-II NSGA-II
0.006
0.008
0.010
0.012
0.014MGD
Our NSGA-II NSGA-II
0.0006
0.0008
0.0010
0.0012
0.0014
0.0016
0.0018
0.0020IGD
Our NSGA-II NSGA-II
0.000102
0.000104
0.000106
0.000108
0.000110HV
Our NSGA-II NSGA-II
0.60
0.65
0.70
0.75
0.80Diversity Metric
Fig. 9: Comparison of performance indicators for TSE.
Figure 10 indicates the approximation curves obtained from both NGSA-II and the proposed algorithms
for each market along with their EF marked by black line. The results show the superiority of the proposed
approach to the conventional NSGA-II. It is obvious from the plots that both algorithms yield close results
for relatively small universes of assets in the markets. While the differences become more conspicuous with
growing numbers of assets. One drawback, however, is that the data for the unconstrained Pareto front for
the TSE market was not available to us and we, therefore, not only executed our algorithm with somewhat
relaxed constraints for longer iterations but multiplied each return and risk of each data point from the
approximated curve by a factor with equal positive and negative deviations from one, respectively, and
extrapolated the tails of the curve along the slope of the last change in the data points only to ensure no
feasible solution capable of dominating that artificial Pareto front is left out. This is also the reason why
algorithms are more distant away from the black line in the TSE market compared to other markets.
Figure 11 and Figure 12 show comparisons of the two algorithms for different values ofK min andK max.
Obviously, the proposed approach was capable of discovering solutions superior to those found by NSGA-II
with different CC setups, especially with increasing pools of assets. Furthermore, the difference between the
conventional NSGA-II and the version proposed in this article increased with increasing numbers of assets
in the portfolio. Aforementioned results further approve our overall strategies since customized NSGA-II
are able to find both better and wider ranges of portfolios. Further results for more sparse cardinality
configurations are provided in Appendix A. Additionally, Appendix B presents the results of implementing
our mechanisms on another multi-objective algorithm.
Figure 13 compares the two algorithms with the setup as previously described except for CC whose
parameters are set toK min = 2,K max = 10. Comparison of the approximated curves reveals that the
proposed package found better portfolios and covered a wider range of unconstrained PF even with increasing
pools of assets. Similar to previous plots, the results for the relatively small market data obtained from the
two algorithms shown in this Figure are competitively close. While the conventional NSGA-II failed to keep
the same performance, approximated smaller ranges of unconstrained PF, and yielded less efficient solutions
with a growing universe of assets, the approach proposed herein not only found better dominant portfolios
but also kept the same performance and approximated a wider range of unconstrained PF with increasing
numbers of stocks.

0.0005 0.0010 0.0015 0.0020 0.0025
Risk
0.002
0.003
0.004
0.005
0.006
0.007
0.008
0.009
0.010Return
Unconstrained Pareto front
Our NSGA-II
NSGA-II
(a) DAX 100
0.0000 0.0005 0.0010 0.0015 0.0020 0.0025 0.0030
Risk
0.002
0.003
0.004
0.005
0.006
0.007
0.008
0.009Return
Unconstrained Pareto front
Our NSGA-II
NSGA-II (b) S&P 100
0.0004 0.0006 0.0008 0.0010 0.0012 0.0014 0.0016
Risk
0.0000
0.0005
0.0010
0.0015
0.0020
0.0025
0.0030
0.0035
0.0040Return
Unconstrained Pareto front
Our NSGA-II
NSGA-II
(c) Nikkei 225
0.000 0.001 0.002 0.003 0.004 0.005
Risk
0.005
0.010
0.015
0.020Return
Unconstrained Pareto front
Our NSGA-II
NSGA-II (d) TSE
Fig. 10: Comparison of approximated efficient frontiers ( PN i=1 zi = 10).
0.0005 0.0010 0.0015 0.0020 0.0025
Risk
0.002
0.003
0.004
0.005
0.006
0.007
0.008
0.009
0.010Return
Unconstrained Pareto front
NSGA-II
Our NSGA-II
(a) DAX 100
0.0000 0.0005 0.0010 0.0015 0.0020 0.0025 0.0030
Risk
0.002
0.003
0.004
0.005
0.006
0.007
0.008
0.009Return
Unconstrained Pareto front
NSGA-II
Our NSGA-II (b) S&P 100
0.0004 0.0006 0.0008 0.0010 0.0012 0.0014 0.0016
Risk
0.0000
0.0005
0.0010
0.0015
0.0020
0.0025
0.0030
0.0035
0.0040Return
Unconstrained Pareto front
NSGA-II
Our NSGA-II (c) Nikkei 225
0.000 0.001 0.002 0.003 0.004
Risk
0.005
0.010
0.015
0.020Return
Unconstrained Pareto front
NSGA-II
Our NSGA-II (d) TSE
Fig. 11: Comparison of approximated efficient frontiers ( PN i=1 zi = 5).

0.0005 0.0010 0.0015 0.0020 0.0025
Risk
0.002
0.003
0.004
0.005
0.006
0.007
0.008
0.009
0.010Return
Unconstrained Pareto front
NSGA-II
Our NSGA-II
(a) DAX 100
0.0000 0.0005 0.0010 0.0015 0.0020 0.0025 0.0030
Risk
0.002
0.003
0.004
0.005
0.006
0.007
0.008
0.009Return
Unconstrained Pareto front
NSGA-II
Our NSGA-II (b) S&P 100
0.0004 0.0006 0.0008 0.0010 0.0012 0.0014 0.0016
Risk
0.0000
0.0005
0.0010
0.0015
0.0020
0.0025
0.0030
0.0035
0.0040Return
Unconstrained Pareto front
NSGA-II
Our NSGA-II (c) Nikkei 225
0.000 0.001 0.002 0.003 0.004
Risk
0.0025
0.0050
0.0075
0.0100
0.0125
0.0150
0.0175
0.0200
0.0225Return
Unconstrained Pareto front
NSGA-II
Our NSGA-II (d) TSE
Fig. 12: Comparison of approximated efficient frontiers ( PN i=1 zi = 15).
0.0005 0.0010 0.0015 0.0020 0.0025
Risk
0.002
0.003
0.004
0.005
0.006
0.007
0.008
0.009
0.010Return
Unconstrained Pareto front
NSGA-II
Our NSGA-II
(a) DAX 100
0.0000 0.0005 0.0010 0.0015 0.0020 0.0025 0.0030
Risk
0.002
0.003
0.004
0.005
0.006
0.007
0.008
0.009Return
Unconstrained Pareto front
NSGA-II
Our NSGA-II
 (b) S&P 100
0.0004 0.0006 0.0008 0.0010 0.0012 0.0014 0.0016
Risk
0.0000
0.0005
0.0010
0.0015
0.0020
0.0025
0.0030
0.0035
0.0040Return
Unconstrained Pareto front
NSGA-II
Our NSGA-II
(c) Nikkei 225
0.000 0.001 0.002 0.003 0.004 0.005
Risk
0.005
0.010
0.015
0.020Return
Unconstrained Pareto front
NSGA-II
Our NSGA-II
 (d) TSE
Fig. 13: Comparison of approximated efficient frontiers (K min = 2, Kmax = 10).
Figure 14 presents the effects of upper and lower bounds of CC on PF generated by the modified NSGA-II
in the TSE market for longer iterations. In situations with the lower bound of CC equal to 2 but a fluctuating

upper bound, it is clear that the best choice for an investor who seeks a profitable portfolio of low risk (i.e.,
portfolios in the knee area of the curve) would be diversified assets. This is evidenced by the major risk
reduction in portfolios (namely, a clear shift toward the left side of PF) with increasing maximum number
of assets in the portfolio from three to five. Even though the risk of the portfolio decreases with a greater
overall diversification in assets, the amount of risk reduction (shifts) grows smaller with increasing numbers
of assets in the portfolio, proving that diversification can be achieved with a portfolio of fewer assets. Beyond
a maximum number of ten stocks, the difference becomes almost negligible and the investor gains not much
benefit from adding more assets to the portfolio. Another important factor that comes into play with growing
numbers of assets in the portfolio is the rise in holding costs, including transaction and monitoring costs.
Meanwhile, holding a portfolio of less than three or five assets does not seem a rational decision for a risk-
averse investor since the investor can achieve a safer investment by adding just a few assets while avoiding
high transaction and monitoring costs. Hence, it is costly to hold more than ten to twenty stocks but perilous
at the same time for a risk-averse investor to hold a portfolio with assets fewer than the number of fingers
on one hand.
Although imposing a limit on the maximum number of assets in the portfolio changes the left side of the
approximation curves, at some point, curves with differentK max values coincide at some point with each
other for identicalK min values. In cases with fixed values ofK max but varyingK min the only part that
varies is the right side of the curves. The lower bound of CC could be considered by fund managers and
regulators to ensure a minimal diversification since it reduces the number of extremely risky portfolios or
eliminates them altogether from the search space. Over-diversified portfolios could end in inefficient solutions
for risk-taking investors since they can choose less risky investments with more returns that would entail a
portfolio with fewer assets.
Figure 15 compares the IGDs of both the proposed approach and the conventional NSGA-II that have the
same solutions encoded with previously explained parameters and iterations for different markets, illustrating
the effectiveness of our mating strategies due to the faster convergence of the proposed strategy against the
same encoding system in NSGA-II. The plots in this Figure also indicate that our approach is capable of
yielding closer approximations for the same number of generations. Furthermore, the distance between the
two lines grows larger and more conspicuous as the universe of assets grows.
Regarding computation time, running codes in Python is slower than that in such other programming
languages as C/C++ or machine codes. Indeed, we identified functions that required more computation
power and acted as bottlenecks in the algorithm. It was found that multiprocessing or translating them
into machine code using the Just In Time (JIT) complier provided by Numba library (Lam et al. (2015))
would reduce the overall execution time. Multiprocessing, which involves distributing computation across
various CPU cores, allows code to execute faster because more computational power is allocated by the
CPU. Moreover, optimized functions translated into machine code via Numba are executed faster after each
iteration. This is because the compiled code is reused after its initial compilation during the first execution,
and it is cached to eliminate the need for recompilation in subsequent calls, making it ideal for use in repeated
calls, such as loops. Figure 16 presents a comparison of the computation times for TSE and S&P100 markets
by both the conventional and modified NSGA-II algorithms (modified with the above boosting execution
techniques); both follow our solution encoding system. Results indicate a significantly lower computation
time for the proposed approach and almost identical execution times for both markets despite the larger size
of one market by four times.

0.000 0.001 0.002 0.003 0.004
Risk
0.000
0.005
0.010
0.015
0.020Return
k_min =2,k_max = 3
k_min =2,k_max = 5
k_min =2,k_max = 7
k_min =2,k_max = 10
k_min =2,k_max = 20
k_min =2,k_max = 30
k_min =2,k_max = 40
(a) FixK min.
0.000 0.001 0.002 0.003 0.004
Risk
0.005
0.010
0.015
0.020Return
k_min =2,k_max = 10
k_min =4,k_max = 10
k_min =7,k_max = 10
k_min =10,k_max = 10 (b) FixK max.
Fig. 14: Pareto front with the different cardinality settings.
0 20 40 60 80 100
Generation
0.0000
0.0005
0.0010
0.0015
0.0020
0.0025IGD
Our approach
Normal NSGA-II
(a) DAX 100
0 20 40 60 80 100
Generation
0.0000
0.0002
0.0004
0.0006
0.0008
0.0010
0.0012
0.0014IGD
Our approach
Normal NSGA-II (b) S&P 100
0 20 40 60 80 100
Generation
0.00000
0.00025
0.00050
0.00075
0.00100
0.00125
0.00150IGD
Our approach
Normal NSGA-II (c) Nikkei 225
0 20 40 60 80 100
Generation
0.000
0.001
0.002
0.003
0.004IGD
Our approach
Normal NSGA-II (d) TSE
Fig. 15: Comparison of IGD of our approach and normal NSGA-II with our encoding system.

Our NSGA-II(TSE) Our NSGA-II(S&P100)
10.5
11.0
11.5
12.0
12.5
13.0
13.5Time(s)
(a) Magnified view
Our NSGA-II(TSE) Our NSGA-II(S&P100) NSGA-II(TSE) NSGA-II(S&P100)
10
15
20
25
30
35Time(s) (b) Original view
Fig. 16: Comparison of computation times of the conventional and modified NSGA-II involving the proposed
solution encoding.
Additionally, two non-parametric tests are performed to analyze the effectiveness of our approach. All
four previously-discussed performance metrics are used for evaluation in these two tests.
The first test is the sign test, as demonstrated in Table 1. The critical value for this test is 9 wins out
of 10 forα= 0.05 and 8 out of 10 forα= 0.1. In this study, we considerα= 0.05. As shown in the table,
although there was no significant improvement in the MGD metric for the DAX 100 and S&P 100 markets
atα= 0.05, our strategies proved effective in all other metrics across all other markets.
Table 1: Sign Test. Wins and Losses per Market
Market MGD IGD HV Diversity Metric
Wins Losses Wins Losses Wins Losses Wins Losses
DAX 100 7 3 10 0 10 0 10 0
S&P 100 8 2 10 0 10 0 9 1
Nikkei 225 10 0 10 0 10 0 9 1
TSE 10 0 10 0 10 0 10 0
However, there is a downside to the sign test, as it does not consider the extent to which a performance
metric performed better for each market. To address this issue, we performed the Wilcoxon signed-rank
test, which accounts for this limitation. Table 2 presents the results of the Wilcoxon signed-rank test for
the markets used in this study. It includes the values ofR +,R −, and the P-value for each metric. The
symbol ”∼” indicates no significant difference, while an asterisk (*) denotes a significant improvement of our
approach over the traditional NSGA-II. As shown in the table, our approach was effective across all metrics
and markets with a significance level ofα= 0.05, except for the MGD metric in the DAX 100 market.

Table 2: Wilcoxon Signed-Rank Test Results (Two-Tailed)
Performance Metric MarketR + R− P-value Result
MGD
DAX 100 11 44 0.1054∼
S&P 100 3 52 0.0097 *
Nikkei 225 0 55 0.0019 *
TSE 0 55 0.0019 *
IGD
DAX 100 0 55 0.0019 *
S&P 100 0 55 0.0019 *
Nikkei 225 0 55 0.0019 *
TSE 0 55 0.0019 *
HV
DAX 100 55 0 0.0019 *
S&P 100 55 0 0.0019 *
Nikkei 225 55 0 0.0019 *
TSE 55 0 0.0019 *
Diversity Metric
DAX 100 0 55 0.0019 *
S&P 100 1 54 0.0039 *
Nikkei 225 5 50 0.0195 *
TSE 0 55 0.0019 *
5 Conclusion and future research
In this study, promising strategies are presented to improve the performance of multi-objective evolutionary
algorithms, aiming to achieve a better convergence rate, strengthen search power, and find higher-quality
portfolios in less time for large-scale portfolio optimization problems under cardinality constraints, a well-
known issue in finance with numerous real-world applications. The aforementioned strategies are applied to a
multi-objective evolutionary algorithm and tested against a standard one, using four stock market datasets,
three of which are benchmark data from well-established stock markets around the world. In order to maintain
the feasibility of the solutions, a novel solution representation was used in lieu of the standard real-value
vector of sizeNalong with a novel operator and specially designed repair mechanisms. Moreover, new mating
strategies were used for producing high-quality solutions. Results revealed the faster convergence rate of the
proposed approach as well as its capability to explore a broader range of the search space in comparison
with the original version of the algorithm. Furthermore, the proposed handling techniques proved effective
for different CC settings, and our approach was also shown to be effective through the use of two non-
parametric statistical tests, demonstrating superior performance across four common performance metrics
in all markets. Finally, it was observed that the proposed approach was more appropriate for application to
larger markets when CC is present since, unlike the the original algorithm, our approach did not decline in
performance with increasing number of assets.
While our approach has shown promising results, several opportunities for future research remain. Al-
though the formulation used in this paper is widely studied in the literature (Kalayci et al. (2019)), there
are additional constraints that investors may be concerned about, such as transaction costs or liquidity con-
straints. Since we did not use penalty functions to ensure the feasibility of these constraints, due to their
limitations (Yeniay (2005)), incorporating such constraints into our model would require modifications to
the proposed approach. Future work could explore these adaptations.
Appendix A: Comparison with fewer assets
As mentioned in the text, it is not a wise choice to opt for portfolios with few assets, such as two or three,
as portfolios of this size are inefficient and one can significantly reduce investment risk by adding more
assets. Nevertheless, to demonstrate that our approach is not limited to the tested cardinality settings and
to illustrate the discontinuity in the efficient frontiers, we also provide a comparison between these portfolios
for our improved NSGA-II and the standard version.

0.0005 0.0010 0.0015 0.0020 0.0025
Risk
0.002
0.003
0.004
0.005
0.006
0.007
0.008
0.009
0.010Return
Unconstrained Pareto front
NSGA-II
Our NSGA-II
(a) DAX 100
0.0000 0.0005 0.0010 0.0015 0.0020 0.0025 0.0030
Risk
0.002
0.003
0.004
0.005
0.006
0.007
0.008
0.009Return
Unconstrained Pareto front
NSGA-II
Our NSGA-II (b) S&P 100
0.0004 0.0006 0.0008 0.0010 0.0012 0.0014 0.0016
Risk
0.000
0.001
0.002
0.003
0.004Return
Unconstrained Pareto front
NSGA-II
Our NSGA-II (c) Nikkei 225
0.000 0.001 0.002 0.003 0.004
Risk
0.000
0.005
0.010
0.015
0.020Return
Unconstrained Pareto front
NSGA-II
Our NSGA-II (d) TSE
Fig. 17: Comparing NSGA-II algorithms with PN i=1 zi = 2.
0.0005 0.0010 0.0015 0.0020 0.0025
Risk
0.002
0.003
0.004
0.005
0.006
0.007
0.008
0.009
0.010Return
Unconstrained Pareto front
NSGA-II
Our NSGA-II
(a) DAX 100
0.0000 0.0005 0.0010 0.0015 0.0020 0.0025 0.0030
Risk
0.002
0.003
0.004
0.005
0.006
0.007
0.008
0.009Return
Unconstrained Pareto front
NSGA-II
Our NSGA-II (b) S&P 100
0.0004 0.0006 0.0008 0.0010 0.0012 0.0014 0.0016
Risk
0.000
0.001
0.002
0.003
0.004Return
Unconstrained Pareto front
NSGA-II
Our NSGA-II (c) Nikkei 225
0.000 0.001 0.002 0.003 0.004
Risk
0.005
0.010
0.015
0.020Return
Unconstrained Pareto front
NSGA-II
Our NSGA-II (d) TSE
Fig. 18: Comparing NSGA-II algorithms with PN i=1 zi = 3.
Appendix B: SPEA-II algorithm
The SPEA-II algorithm is also used for comparison to demonstrate that our strategies are applicable and
generalizable to other multi-objective algorithms, and not specific to NSGA-II. To avoid redundancy and
manage the length of the paper, and given that the improved NSGA-II consistently outperformed its standard
version, we did not repeat all evaluations for every market. Instead, due to the consistent results, further
validation with SPEA-II was conducted using only the largest and most complex market dataset, TSE, under
identical configurations. Figure 19 illustrates the performance of the improved SPEA-II and its standard
version. As evident from the indicators, the algorithm enhanced with our mechanisms outperformed the
regular SPEA-II across all metrics.
Our SPEA-II SPEA-II
0.00
0.05
0.10
0.15
0.20
0.25
0.30MGD
Our SPEA-II SPEA-II
0.0006
0.0008
0.0010
0.0012
0.0014
0.0016IGD
Our SPEA-II SPEA-II
0.000100
0.000102
0.000104
0.000106
0.000108
0.000110HV
Our SPEA-II SPEA-II
0.80
0.82
0.84
0.86
0.88Diversity Metric
Fig. 19: Comparison of performance indicators for TSE using SPEA-II.
Additionally, Figure 20 presents the efficient frontiers under three cardinality settings. Consistent with
previous results, our improved SPEA-II dominated the standard version, consistently generating superior
portfolios in terms of risk and return.

0.000 0.001 0.002 0.003 0.004 0.005
Risk
0.005
0.010
0.015
0.020Return
Unconstrained Pareto front
SPEA-II
Our SPEA-II
(a) PN i=1 zi = 5
0.000 0.001 0.002 0.003 0.004 0.005
Risk
0.005
0.010
0.015
0.020Return
Unconstrained Pareto front
SPEA-II
Our SPEA-II (b) PN i=1 zi = 10
0.000 0.001 0.002 0.003 0.004 0.005
Risk
0.005
0.010
0.015
0.020Return
Unconstrained Pareto front
SPEA-II
Our SPEA-II (c) PN i=1 zi = 15
Fig. 20: Comparison of approximated efficient frontiers for TSE using SPEA-II.
Declarations
Ethics approval and consent to participate:
Not applicable.
Consent for publication:
Not applicable.
F unding:
This research received no specific grant from any funding agency in the public, commercial, or not-for-profit
sectors.
Availability of data and materials:
The code for our approach, along with the data we used in addition to the publicly available OR-library
benchmark, will be available upon request.
Competing interests:
The authors declare that they have no competing interests.
Authors’ contributions:
Danial Ramezani contributed to conceptualization, methodology, software, and writing - original draft prepa-
ration.
Mostafa Abouei Ardakan contributed to supervision, conceptualization, methodology, and writing - review-
ing and editing.
All authors read and approved the final manuscript.
Acknowledgements:
No acknowledgements to declare.
Corresponding author:
Danial Ramezani
danialramezani@khu.ac.ir

References
Mehmet Anil Akbay, Can B Kalayci, and Olcay Polat. A parallel variable neighborhood search algorithm
with quadratic programming for cardinality constrained portfolio optimization.Knowledge-Based Systems,
198:105944, 2020.
Saud Almahdi and Steve Y Yang. A constrained portfolio trading system using particle swarm algorithm
and recurrent reinforcement learning.Expert Systems with Applications, 130:145–156, 2019.
Konstantinos P Anagnostopoulos and Georgios Mamanis. A portfolio optimization model with three objec-
tives and discrete variables.Computers & Operations Research, 37(7):1285–1297, 2010.
Konstantinos P Anagnostopoulos and Georgios Mamanis. The mean–variance cardinality constrained port-
folio optimization problem: An experimental evaluation of five multiobjective evolutionary algorithms.
Expert Systems with Applications, 38(11):14208–14217, 2011.
John E Beasley. Or-library: distributing test problems by electronic mail.Journal of the operational research
society, 41(11):1069–1072, 1990.
Jyotirmayee Behera, Ajit Kumar Pasayat, Harekrushna Behera, and Pankaj Kumar. Prediction based mean-
value-at-risk portfolio optimization using machine learning regression algorithms for multi-national stock
markets.Engineering Applications of Artificial Intelligence, 120:105843, 2023.
T-J Chang, Nigel Meade, John E Beasley, and Yazid M Sharaiha. Heuristics for cardinality constrained
portfolio optimisation.Computers & Operations Research, 27(13):1271–1302, 2000.
Wei Chen, Haoyu Zhang, Mukesh Kumar Mehlawat, and Lifen Jia. Mean–variance portfolio optimization
using machine learning-based stock price prediction.Applied Soft Computing, 100:106943, 2021a.
Yi Chen, Aimin Zhou, and Swagatam Das. Utilizing dependence among variables in evolutionary algorithms
for mixed-integer programming: A case study on multi-objective constrained portfolio optimization.Swarm
and Evolutionary Computation, 66:100928, 2021b.
Roger Clarke, Harindra De Silva, and Steven Thorley. Portfolio constraints and the fundamental law of
active management.Financial Analysts Journal, 58(5):48–66, 2002.
Marco Corazza, Giacomo di Tollo, Giovanni Fasano, and Raffaele Pesenti. A novel hybrid pso-based meta-
heuristic for costly portfolio selection problems.Annals of Operations Research, 304(1-2):109–137, 2021.
Tianxiang Cui, Ruibin Bai, Shusheng Ding, Andrew J Parkes, Rong Qu, Fang He, and Jingpeng Li. A hybrid
combinatorial approach to a two-stage stochastic portfolio optimization model with uncertain asset prices.
Soft Computing, 24:2809–2831, 2020.
Tunchan Cura. Particle swarm optimization approach to portfolio optimization.Nonlinear analysis: Real
world applications, 10(4):2396–2406, 2009.
Ma ´ ısa Kely de Melo, Rodrigo Tom´ as Nogueira Cardoso, and Tales Argolo Jesus. Multiobjective model
predictive control for portfolio optimization with cardinality constraint.Expert Systems with Applications,
205:117639, 2022.
Kalyanmoy Deb, Amrit Pratap, Sameer Agarwal, and TAMT Meyarivan. A fast and elitist multiobjective
genetic algorithm: Nsga-ii.IEEE transactions on evolutionary computation, 6(2):182–197, 2002.
Okkes Ertenlice and Can B Kalayci. A survey of swarm intelligence for portfolio optimization: Algorithms
and applications.Swarm and evolutionary computation, 39:36–52, 2018.
Kyle Erwin and Andries Engelbrecht. Meta-heuristics for portfolio optimization.Soft Computing, 27(24):
19045–19073, 2023.
Abolgasem Esmaeily and Felix Loge. Portfolio optimization problems with cardinality constraints, 2023.
Alberto Fern´ andez and Sergio G´ omez. Portfolio selection using neural networks.Computers & operations
research, 34(4):1177–1191, 2007.
Hamid Reza Golmakani and Mehrshad Fazel. Constrained portfolio selection using particle swarm optimiza-
tion.Expert Systems with Applications, 38(7):8327–8335, 2011.
Abhishek Gunjan and Siddhartha Bhattacharyya. A brief review of portfolio optimization techniques.Ar-
tificial Intelligence Review, pages 1–40, 2022.
Abhishek Gunjan and Siddhartha Bhattacharyya. Quantum-inspired meta-heuristic approaches for a con-
strained portfolio optimization problem.Evolutionary Intelligence, 17(4):3061–3100, 2024.
Meriem Hemici and Djaafar Zouache. A multi-population evolutionary algorithm for multi-objective con-
strained portfolio optimization problem.Artificial Intelligence Review, pages 1–42, 2023.

Henri Claver Jimbo, Isidore Seraphin Ngongo, Nicolas Gabriel Andjiga, Takeru Suzuki, and Charles Awona
Onana. Portfolio optimization under cardinality constraints: a comparative study.Open Journal of Statis-
tics, 7(4):731–742, 2017.
Philippe Jorion. Value at risk: the new benchmark for controlling market risk.(No Title), 1997.
Can B Kalayci, Okkes Ertenlice, and Mehmet Anil Akbay. A comprehensive review of deterministic models
and applications for mean-variance portfolio optimization.Expert Systems with Applications, 125:345–368,
2019.
Can B Kalayci, Olcay Polat, and Mehmet A Akbay. An efficient hybrid metaheuristic algorithm for cardi-
nality constrained portfolio optimization.Swarm and Evolutionary Computation, 54:100662, 2020.
Massimiliano Kaucic, Mojtaba Moradi, and Mohmmad Mirzazadeh. Portfolio optimization by improved
nsga-ii and spea 2 based on different risk measures.Financial Innovation, 5:1–28, 2019.
Renatas Kizys, Jana Doering, Angel A Juan, Onur Polat, Laura Calvet, and Javier Panadero. A simheuristic
algorithm for the portfolio optimization problem with random returns and noisy covariances.Computers
& Operations Research, 139:105631, 2022.
Ken Kobayashi, Yuichi Takano, and Kazuhide Nakata. Bilevel cutting-plane algorithm for cardinality-
constrained mean-cvar portfolio optimization.Journal of Global Optimization, 81(2):493–528, 2021.
Hiroshi Konno and Hiroaki Yamazaki. Mean-absolute deviation portfolio optimization model and its appli-
cations to tokyo stock market.Management science, 37(5):519–531, 1991.
Siu Kwan Lam, Antoine Pitrou, and Stanley Seibert. Numba: A llvm-based python jit compiler. InProceed-
ings of the Second Workshop on the LL VM Compiler Infrastructure in HPC, pages 1–6, 2015.
Man-Fai Leung and Jun Wang. Cardinality-constrained portfolio selection based on collaborative neurody-
namic optimization.Neural Networks, 145:68–79, 2022.
Konstantinos Liagkouras and Konstantinos Metaxiotis. Efficient portfolio construction with the use of mul-
tiobjective evolutionary algorithms: Best practices and performance metrics.International Journal of
Information Technology & Decision Making, 14(03):535–564, 2015.
Haiping Ma, Yajing Zhang, Shengyi Sun, Ting Liu, and Yu Shan. A comprehensive survey on nsga-ii for
multi-objective optimization and applications.Artificial Intelligence Review, pages 1–54, 2023.
Yilin Ma, Ruizhu Han, and Weizhong Wang. Portfolio optimization with return prediction using deep
learning and machine learning.Expert Systems with Applications, 165:113973, 2021.
Nabil Mansour, Mohamed Sadok Cherif, and Walid Abdelfattah. Multi-objective imprecise programming
for financial portfolio selection with fuzzy returns.Expert Systems with Applications, 138:112810, 2019.
Harry Markowitz. Portfolio Selection.Journal of Finance, 7(1):77–91, March 1952.https://doi.org/j.
1540-6261.1952.tb01525.URLhttps://ideas.repec.org/a/bla/jfinan/v7y1952i1p77-91.html.
Danilo Alcantara Milhomem and Maria Jos´ e Pereira Dantas. Analysis of new approaches used in portfolio
optimization: a systematic literature review.Production, 30:e20190144, 2020.
Nicholas Moehle, Jack Gindi, Stephen Boyd, and Mykel J Kochenderfer. Portfolio construction as linearly
constrained separable optimization.Optimization and Engineering, 24(3):1667–1687, 2023.
Hakimeh Morteza, Seyed Mahdi Jameii, and Mohammad Karim Sohrabi. An improved learning automata
based multi-objective whale optimization approach for multi-objective portfolio optimization in financial
markets.Expert Systems with Applications, 224:119970, 2023.
GA Vijayalakshmi Pai and Thierry Michel. Evolutionary optimization of constrainedk-means clustered
assets for diversification in small portfolios.IEEE Transactions on Evolutionary Computation, 13(5):
1030–1053, 2009.
Felipe Dias Paiva, Rodrigo Tom´ as Nogueira Cardoso, Gustavo Peixoto Hanaoka, and Wendel Moreira Duarte.
Decision-making for financial trading: A fusion approach of machine learning and portfolio selection.Expert
Systems with Applications, 115:635–655, 2019.
Lasse Heje Pedersen, Abhilash Babu, and Ari Levine. Enhanced portfolio optimization.Financial Analysts
Journal, 77(2):124–151, 2021.
R Tyrrell Rockafellar, Stanislav Uryasev, et al. Optimization of conditional value-at-risk.Journal of risk, 2:
21–42, 2000.
Alireza Sadeghi Hesar and Mahboobeh Houshmand. A memetic quantum-inspired genetic algorithm based
on tabu search.Evolutionary Intelligence, 17(3):1837–1853, 2024.
Somaya Sadik, Mohamed Et-tolba, and Benayad Nsiri. A novel regularization-based optimization approach
to sparse mean-reverting portfolios selection.Optimization and Engineering, 24(4):2549–2577, 2023.

Yousef Sanjalawe, Salam Al-E’mari, Mosleh Abualhaj, Sharif Naser Makhadmeh, Mohammad A Alsharaiah,
and Duaa H Hijazi. Recent advances in secretary bird optimization algorithm, its variants and applications.
Evolutionary Intelligence, 18(3):1–32, 2025.
Shalu, Amita Sharma, and Ruchika Sehgal. Computational analysis of expectile and deviation expectile
portfolio optimization models.Optimization and Engineering, pages 1–29, 2024.
Yuri Laio TV Silva, Ana Beatriz Herthel, and Anand Subramanian. A multi-objective evolutionary algorithm
for a class of mean-variance portfolio selection problems.Expert Systems with Applications, 133:225–241,
2019.
Efrain Solares, Carlos A Coello Coello, Eduardo Fernandez, and Jorge Navarro. Handling uncertainty through
confidence intervals in portfolio optimization.Swarm and evolutionary computation, 44:774–787, 2019.
Yingjie Song, Gaoyang Zhao, Bin Zhang, Huayue Chen, Wuquan Deng, and Wu Deng. An enhanced dis-
tributed differential evolution algorithm for portfolio optimization problems.Engineering Applications of
Artificial Intelligence, 121:106004, 2023.
C Tadonki and J-Ph Vial. Portfolio selection with cardinality and bound constraints.University of Geneva,
2003.
Ankit Thakkar and Kinjal Chaudhari. A comprehensive survey on portfolio optimization, stock price and
trend prediction using particle swarm optimization.Archives of Computational Methods in Engineering,
28:2133–2164, 2021.
Shanu Verma, Millie Pant, and Vaclav Snasel. A comprehensive review on nsga-ii for multi-objective com-
binatorial optimization problems.Ieee Access, 9:57757–57791, 2021.
Juan Pablo Vielma, Shabbir Ahmed, and George L Nemhauser. A lifted linear programming branch-and-
bound algorithm for mixed-integer conic quadratic programs.INFORMS Journal on Computing, 20(3):
438–450, 2008.
Hongze Wang, Xuerong Li, Wenjing Hong, and Ke Tang. Multi-objective approaches to portfolio optimization
with market impact costs.Memetic Computing, pages 1–11, 2022.
Wuyu Wang, Weizi Li, Ning Zhang, and Kecheng Liu. Portfolio formation with preselection using deep
learning from long-term financial data.Expert Systems with Applications, 143:113042, 2020.
Dingming Wu, Xiaolong Wang, and Shaocong Wu. Construction of stock portfolios based on k-means
clustering of continuous trend features.Knowledge-Based Systems, 252:109358, 2022.
Wei Xu, Jie Tang, Ka Fai Cedric Yiu, and Jian Wen Peng. An efficient global optimal method for cardinality
constrained portfolio optimization.INFORMS Journal on Computing, 36(2):690–704, 2024.
Yongkuan Yang, Bing Yan, and Xiangsong Kong. A dynamic tri-population multi-objective evolutionary
algorithm for constrained multi-objective optimization problems.Evolutionary Intelligence, 17(4):2791–
2806, 2024.
¨Ozg¨ ur Yeniay. Penalty function methods for constrained optimization with genetic algorithms.Mathematical
and computational Applications, 10(1):45–56, 2005.
Yifan Zhang, Peilin Zhao, Qingyao Wu, Bin Li, Junzhou Huang, and Mingkui Tan. Cost-sensitive portfolio
selection via deep reinforcement learning.IEEE Transactions on Knowledge and Data Engineering, 34(1):
236–248, 2020.
Hong Zhao, Zong-Gan Chen, Zhi-Hui Zhan, Sam Kwong, and Jun Zhang. Multiple populations co-
evolutionary particle swarm optimization for multi-objective cardinality constrained portfolio optimization
problem.Neurocomputing, 430:58–70, 2021.
Yongjie Zheng and Jiming Zheng. A novel portfolio optimization model via combining multi-objective
optimization and multi-attribute decision making.Applied Intelligence, 52(5):5684–5695, 2022.
Eckart Zitzler, Lothar Thiele, Marco Laumanns, Carlos M Fonseca, and Viviane Grunert Da Fonseca. Per-
formance assessment of multiobjective optimizers: An analysis and review.IEEE Transactions on evolu-
tionary computation, 7(2):117–132, 2003.
