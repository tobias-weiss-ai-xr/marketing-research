---
title: Differentiable Electricity-Market Clearing for Gradient-Based Planning
url: https://arxiv.org/abs/2609.02646
category: digital-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Luca Mungo
- Maarten P. Scholl
- Arnau Quera-Bofarull
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.02646
pages: 9
chars: 31598
fetched_at: '2026-11-08T13:19:20+00:00'
kb_version: 1
---

# Differentiable Electricity-Market Clearing for Gradient-Based Planning

Differentiable Electricity-Market Clearing for
Gradient-Based Planning
Luca Mungo1,2
luca@mcsm.ai
Maarten P . Scholl1
maarten@mcsm.ai
Arnau Quera-Bofarull1
arnau@mcsm.ai
1Macrocosm Inc. 2Institute for New Economic Thinking, University of Oxford
Abstract
Planning a large data center is difficult because a facility big enough to matter
changes the electricity prices it will pay. Those prices are set by market clearing, a
constrained optimization problem solved anew in every operating condition. How-
ever, simulating the market tells a planner how a candidate plan performs but not
how to improve it. Here we treat market clearing as a differentiable optimization
layer: each forward pass solves the market, and reverse-mode automatic differentia-
tion propagates the planning cost back through the cleared prices to the plan. After
validating these gradients against finite differences, we apply them to a concrete
problem: allocating 50 MW of data-center load across six candidate buses in two
synthetic networks, under a fixed cost per active site, evaluated over 36 operating
states. Judged against exhaustive enumeration of all site combinations, gradient
optimization recovers the continuous allocations almost exactly, with worst-case
objective gaps of 2.3% and 8.5% of the cost difference between the best and worst
single site. Its one systematic error is instructive: near the costs at which a site
should close, the smooth relaxation of the discrete site count shrinks the site rather
than closing it, so discrete transitions arrive late. Differentiable market clearing
thus turns market-aware planning into a problem gradients can search.
1 Introduction
Planning investments in electricity markets is challenging because investment decisions can substan-
tially alter dispatch, congestion, and electricity prices. These outcomes are determined by market
clearing, an optimization problem that minimizes generation costs subject to system constraints
and, in doing so, determines generator dispatch and electricity prices [Kirschen and Strbac, 2004].
Evaluating a candidate investment therefore requires clearing the market under that investment,
often across many operating conditions. This process tells the planner how a proposed investment
will perform, but not how the investment should be adjusted, so finding the best plan may require
searching a large space of alternatives. We study this problem in a simple setting: how should a
planner distribute 50 MW of new data-center load across six candidate buses when each allocation
changes the prices the data centers will pay?
We ask whether the gradient of the planning objective with respect to the investment decision can
guide the search over candidate plans. Obtaining these sensitivities requires differentiating through
the market-clearing problem itself. The planning objective depends on nodal prices, which are dual
outputs of a constrained optimization problem, so its gradient must account for how those prices
respond to changes in the plan. Optimization layers and automatic implicit differentiation provide
the computational tools for obtaining these gradients [Amos and Kolter, 2017, Agrawal et al., 2019,
Preprint.
arXiv:2609.02646v1  [cs.LG]  2 Sep 2026

Blondel et al., 2022, Besanc ¸on et al., 2024]. This yields a differentiable market-clearing model that
can be embedded directly within a gradient-based planning procedure.
Each candidate plan is evaluated by clearing the market across its operating states, and reverse-mode
automatic differentiation propagates the resulting cost through nodal prices to the planning variables;
electricity-market clearing becomes a differentiable optimization layer. We use this approach to
allocate a load across candidate buses in two families of synthetic networks. Because site selection
is discrete, we optimize a smooth relaxation of the site-count penalty, then commit and refine the
resulting plans.
Across both fixed-cost sweeps, the gradient-based procedure produces plans whose objective values
closely track the numerical optimum defined in Appendix B. This pattern persists across five near-
uniform initializations, with the largest departures from the numerical optimum and the greatest
variation occurring near portfolio switches. Although we evaluate only one instance of each network
family, these case studies show that differentiable market clearing can guide an end-to-end planning
procedure toward near-optimal solutions, while also exposing the difficulty of smooth relaxations
near discrete portfolio switches.
Our approach builds on two established lines of work. Sensitivity analysis of optimal power flow has
long been used to characterize how locational marginal prices respond to changes in demand and other
market parameters [Conejo et al., 2005, Yang and Deng, 2014], while differentiable optimization
layers provide general tools for propagating derivatives through constrained optimization problems
[Amos and Kolter, 2017, Agrawal et al., 2019, Blondel et al., 2022, Besan c ¸on et al., 2024]. Data-
center siting has likewise been formulated as a bilevel formulation (a nested optimization problem
in which location decisions affect subsequent electricity-market outcomes) [Zeng et al., 2024] but
has typically been addressed using reformulation and decomposition techniques. While small bilevel
problems can be addressed through single-level reformulations, evidence from large-scale electricity-
grid planning suggests that implicit-gradient methods can outperform reformulation-based approaches
as the problem size and number of operating scenarios grow [Degleris et al., 2026]. This motivates
studying gradient-based methods for market-aware data-center planning. Our setting combines these
threads by propagating derivatives through cleared nodal prices to optimize the spatial allocation of
a large new load. Unlike continuous capacity-expansion settings, the resulting outer problem also
contains a discrete site-selection decision; we address it through a smooth relaxation and evaluate the
resulting plans against an enumerated numerical reference.
2 Differentiable market-aware planning
Let x∈ Xdenote a decision available to the planner, let θ collect the fixed physical properties of the
electricity system, and let ωs describe the demand and generation offers in operating state s. Given
these three inputs, the market clears by solving
y⋆ s (x;θ, ωs)∈arg min
ys∈Ys
Cs(ys)subject tob s,i(ys, x) = 0,|f s,ℓ(ys, x)| ≤f ℓ.(1)
Here ys is the market dispatch, while Cs and Ys, determined by ωs, specify the generation cost and
available quantities. The constraints apply to every bus i and line ℓ. The function bs,i is the balance
at bus i (demand and exports minus local generation and imports) and fs,ℓ is the flow on a line with
capacity f ℓ; these depend on the fixed system θ. The dual variable of bs,i = 0 is the nodal price
λs,i(x;θ, ωs); λs collects these prices. Holding θ and the market states fixed, we write λs(x) below.
The planner solves
min
x∈X
J(x), J(x) =
X
s∈S
ℓs(x, λs(x)) +R(x),(2)
where ℓs is the state-specific market-dependent cost evaluated from the plan and the cleared nodal
prices, with any state weights absorbed into ℓs, and R contains costs incurred directly by the plan.
Evaluating J(x) therefore requires solving the market-clearing problem in every operating state, and
the dependence of λs on x captures the market response to the plan. In our application, x=q is the
allocation of additional nodal load, θ encodes the network and its line properties, and ωs contains
baseline demand and generation offers. The expenditure of the additional load in state s is q·λ s(q),
whose gradient is
∇q[q·λ s(q)] =λ s(q) +
 ∂λs
∂q
⊤
q.(3)
2

The first term measures the effect of moving load while holding prices fixed. The second measures
the effect of the resulting price changes on the whole portfolio. Figure 1 summarizes the forward
market evaluation and reverse propagation of the planning gradient.
x arg minys∈Ys Cs(ys) s.t.b s,i(ys, x) = 0,|fs,ℓ(ys, x)| ≤f ℓ y⋆ s , λs ℓs(x, λs) J(x)
fixed systemθ market statesω s
P
s
+R(x)
reverse pass∇ xJ, differentiated through the solved market
Figure 1: Forward evaluation and reverse pass of the planning objective. The plan x sets the inputs of
every state’s market-clearing problem, whose solved dispatch and nodal prices price the plan; the
fixed system θ and market state ωs enter as data and are not differentiated. The state costs ℓs, which
depend on x directly and through the prices, sum with the direct cost R to J(x); the dashed path
propagates the planning gradient back through the solved clearing problem of every state.
Advances in differentiable optimization make it possible to differentiate through the solutions of
constrained optimization problems [Amos and Kolter, 2017, Blondel et al., 2022]. We treat electricity-
market clearing as a differentiable layer using DiffOpt.jl [Besanc ¸on et al., 2024]: each forward
pass solves the market, and reverse-mode differentiation propagates the planning loss through both
its direct dependence on x and its market-mediated dependence through nodal prices. We use the
resulting gradients to minimize Equation (2) with a standard gradient-based optimizer.
3 Data-center planning experiment
3.1 Experimental setup
We consider the problem of building a portfolio of data centers to serve a total load of D= 50 MW.
We run the experiment on two synthetic network instances: a connected Erd˝os–R´enyi graph [Newman,
2010] and a GeoDe graph [Dey et al., 2023]. The Erd ˝os–R´enyi model provides a nonspatial baseline
in which connections are sampled at random, conditional on the network being connected. GeoDe
instead uses a geometric construction with predominantly local connections to model the sparse,
spatial structure of power grids. In each instance, we allow construction at six candidate buses and let
wi denote the fraction of the total load assigned to candidate i; the allocation satisfies wi ≥0 andP
i wi = 1, and the load at candidate i is qi =Dw i. We imagine that the data centers will operate over a set S of 36 operating states. For state s, the additional load changes market clearing and hence
the locational marginal pricesλ s(q)faced by the portfolio.
We model a fixed construction costκper active site. The physical planning objective is
J(q;κ) = 1 |S| X s∈S q·λ s(q) +κ∥q∥ 0.(4)
The first term is the mean nodal expenditure after re-clearing every state. The second term is a fixed
charge for the number of sites receiving a positive allocation. Thus, the construction term addsκ once
for each active candidate site, irrespective of the load assigned to that site. In the reported physical
evaluation, we apply this count after the 1 MW commitment rule described below. The exact site count
jumps whenever a site opens or closes and therefore provides no useful gradient. During optimization
we parameterize w= softmax(z) and replace the site count by Kτ (w) = P i[1−exp(−w i/τ)]. The forward pass uses a sharp site-count approximation, while the straight-through backward pass
uses a smoother temperature that is annealed during training. This relaxation affects only the
construction-cost term; every market clear receives the full fractional loadq=Dw.
For each κ, Adam produces five dense relaxed allocations from near-uniform initializations. We
obtain physical solutions by discarding allocations below 1 MW, refining on the committed support,
and re-clearing all 36 states. We report the run with the lowest resulting objective; Appendix B.6
summarizes the results across all five initializations. As a numerical reference, we enumerate all
possible nonempty supports and optimize the allocation conditional on each support. Appendix B
gives the numerical settings.
3

Figure 2: Portfolio recovery on the Erd ˝os–R´enyi and GeoDe instances. In the top row, solid lines
show the numerical reference conditional on site count; squares show the committed and refined run
with the lowest re-cleared objective among five initializations; and triangles show the raw relaxed
result from that run. The bottom row compares reference, committed, and relaxed site counts. Each
column subtracts its zero-penalty objective offset and divides by its one-site energy-cost spread, ∆E.
For both graph types, we study one randomly generated network. Both are composed of 12 nodes,
use the same demand, generation, candidate sites, line properties, and operating-state variations; only
the connections between buses differ. We scale κ by ∆E, the difference between the worst and best
one-site mean energy expenditures within each instance. Appendix B gives additional details.
3.2 Planning results
Across both cost sweeps, the committed-and-refined objective closely tracks the numerical reference.
The largest positive objective gap is 0.023∆E for Erd˝os–R´enyi and 0.085∆E for GeoDe; both occur
where the learned procedure retains one additional site. Appendix C traces this delayed support
switch to the smooth site-count relaxation itself rather than to an optimization failure.
Appendix B.6 shows this tracking is not an artifact of reporting the best initialization: the mean
re-cleared objective also remains close to the reference. Deviations and variation are largest near
portfolio switches, where the site choice is most sensitive to the fixed cost.
4 Discussion and conclusion
These experiments separate two questions. Can market gradients identify where the load should
be placed? In both networks, they reliably find the attractive buses and produce near-reference
allocations.
Can a smooth relaxation determine exactly when a site should close? Here the answer is less
satisfactory: near portfolio switches, the relaxation gradually shrinks a secondary site instead of
closing it at the correct fixed cost.
This result is encouraging, but its scope is limited. Our experiments use two small synthetic instances,
with six candidate sites and a limited set of operating states. They do not establish performance
across networks or at realistic system scale. Larger problems will also make exhaustive enumeration
impossible and may make initialization, local minima, and computational cost more important.
Future work should test the approach on larger power systems and historical market conditions.
Another direction combines differentiable market clearing with explicit site-selection methods:
gradients locate and size the load while a separate step selects the active sites.
4

References
Akshay Agrawal, Brandon Amos, Shane Barratt, Stephen Boyd, Steven Diamond, and J. Zico Kolter.
Differentiable convex optimization layers. InAdvances in Neural Information Processing Systems,
volume 32, pages 9558–9570, 2019. URL https://papers.neurips.cc/paper/2019/hash/
9ce3c52fc54362e22053399d3181c638-Abstract.html.
Brandon Amos and J. Zico Kolter. Optnet: differentiable optimization as a layer in neural networks. In
Proceedings of the 34th International Conference on Machine Learning, volume 70 ofProceedings
of Machine Learning Research, pages 136–145. PMLR, 2017. URL https://proceedings.
mlr.press/v70/amos17a.html.
Mathieu Besanc ¸on, Joaquim Dias Garcia, Benoˆıt Legat, and Akshay Sharma. Flexible differentiable
optimization via model transformations.INFORMS Journal on Computing, 36(2):456–478, March
2024. ISSN 1526-5528. doi: 10.1287/ijoc.2022.0283. URL https://doi.org/10.1287/ijoc.
2022.0283.
Mathieu Blondel, Quentin Berthet, Marco Cuturi, Roy Frostig, Stephan Hoyer, Felipe Llinares-
L´opez, Fabian Pedregosa, and Jean-Philippe Vert. Efficient and modular implicit differ-
entiation. InAdvances in Neural Information Processing Systems, volume 35 ofNIPS
’22, Red Hook, NY , USA, 2022. Curran Associates Inc. ISBN 9781713871088. doi:
10.52202/068431-0378. URL https://papers.neurips.cc/paper_files/paper/2022/
hash/228b9279ecf9bbafe582406850c57115-Abstract-Conference.html.
Antonio J. Conejo, Enrique Castillo, Roberto M´ınguez, and Federico Milano. Locational marginal
price sensitivities.IEEE Transactions on Power Systems, 20(4):2026–2033, November 2005. doi:
10.1109/TPWRS.2005.857918.
Anthony Degleris, Abbas El Gamal, and Ram Rajagopal. Gradient methods for bilevel electricity grid
expansion planning.Applied Energy, 418:128044, 2026. doi: 10.1016/j.apenergy.2026.128044.
URLhttps://doi.org/10.1016/j.apenergy.2026.128044.
Asim K Dey, Stephen J Young, and Yulia R Gel. From Delaunay triangulation to topological
data analysis: generation of more realistic synthetic power grid networks.Journal of the Royal
Statistical Society Series A: Statistics in Society, 186(3):335–354, 07 2023. ISSN 0964-1998. doi:
10.1093/jrsssa/qnad066. URLhttps://doi.org/10.1093/jrsssa/qnad066.
Daniel S. Kirschen and Goran Strbac.Fundamentals of Power System Economics. John Wiley &
Sons, Chichester, UK, 2004.
Mark E. J. Newman.Networks: An Introduction. Oxford University Press, 2010. ISBN
9780199206650. doi: 10.1093/acprof:oso/9780199206650.001.0001.
Brian Stott, Jorge Jardim, and Ongun Alsac. DC power flow revisited.IEEE Transactions on Power
Systems, 24(3):1290–1300, 2009. doi: 10.1109/TPWRS.2009.2021235.
Liu Yang and Chunlin Deng. A united method for sensitivity analysis of the locational marginal price
based on the optimal power flow.Mathematical Problems in Engineering, 2014:1–7, 2014. doi:
10.1155/2014/141636. URLhttps://doi.org/10.1155/2014/141636.
Bo Zeng, Yinyu Zhou, Xinzhu Xu, and Danting Cai. Bi-level planning approach for incorporating
the demand-side flexibility of cloud data centers under electricity-carbon markets.Applied Energy,
357:122406, 2024. doi: 10.1016/j.apenergy.2023.122406. URL https://doi.org/10.1016/j.
apenergy.2023.122406.
5

A Gradient-validation details
Directional checks.For one operating state s, let fs(z) =q(z) ⊤λs(q(z)), where q(z) =
Dsoftmax(z) . We compare the reverse-mode directional derivative of fs along a centered unit
vector v with [fs(z+ϵv)−f s(z−ϵv)]/(2ϵ) . For each of the Erd ˝os–R´enyi and GeoDe families, we
use topology seeds 1–3, load capacities 25, 50, and 100 MW, four of 12 generated operating states,
three allocation seeds, three direction seeds, and ϵ∈ {10−3,10 −4,10 −5}. This gives 972 checks per
topology family.
We describe an active set by the lower, interior, or upper status of each line constraint and by the offer
interval containing each generator dispatch. A finite-difference stencil is stable when its center and
both endpoints have the same signature. All 1,944 directional stencils were stable. We treat directions
whose analytic magnitude is below 10−3 as near zero and assess them by absolute rather than relative
error. Grouping the remaining directions by topology, capacity, congestion regime, and ϵ, the largest
groupwise 90th-percentile relative error was 7.94×10 −5 for Erd ˝os–R´enyi and 1.48×10 −4 for
GeoDe. These checks validate the physical energy expenditure path; they intentionally exclude the
straight-through derivative of the relaxed site count.
Active-set boundaries.We also scan 200-interval paths between concentrated candidate-site
allocations, locate changes in the active-set signature by bisection, and test the appropriate derivative
on each side. We request distances 10−2, 10−3, and 10−4 from the boundary and use a finite-
difference step equal to 0.2 times that distance. When a stencil leaves its expected adjacent regime,
we halve the distance down to a minimum of 10−4; if no valid stencil remains, we mark that side
unresolved. We do not assert or test a derivative exactly at a boundary.
Each topology family produced 18 detected transitions. Table 1 reports the checks at requested
distance 10−3. Unresolved transitions are excluded from the error summaries rather than counted as
successful checks.
Table 1: One-sided boundary checks at requested distance 10−3. Errors summarize informative
resolved sides.
Topology Change Found Resolved 90th percentile Maximum
Erd˝os–R´enyi line 10 82.44×10 −4 2.73×10 −4
Erd˝os–R´enyi offer 8 29.41×10 −6 9.83×10 −6
GeoDe line 8 75.61×10 −3 1.43×10 −2
GeoDe offer 10 51.23×10 −1 3.34×10 −1
The boundary study is therefore diagnostic rather than a blanket accuracy claim. In particular, a
narrow GeoDe offer regime yields a maximum relative discrepancy of 0.334 at the requested 10−3
distance, and solver noise becomes more prominent at 10−4. We retain these cases as limitations of
finite-difference validation near active-set changes.
B Planning-experiment details
B.1 Network construction and operating states
Both cases place 50 MW of data-center load across six candidate buses. We first construct a common
base system containing bus-level demand, generation offers, and a collection of line properties. We
then connect the buses according to either the Erd˝os–R´enyi or GeoDe topology, using the original
thermal ratings without rescaling. Finally, we generate 36 matched one-hour operating states by
perturbing demand, offer prices, and available generation in the same way for both networks.
6

B.2 Market-clearing formulation
Let A be the oriented bus–line incidence matrix, let B be the diagonal matrix of line susceptances,
and let M map the six candidate-site loads to their corresponding buses. For an allocation q, the
nodal demand in operating state s is eds(q) =d s +M q. We clear that state with the convex DC
optimal-power-flow problem, which instantiates Equation (1) withx=qandy s = (gs, fs, ϕs):
minimize
gs,fs,ϕs
X
j∈G
Cs,j(gs,j)
subject to eds,i(q) + (Afs)i − X
j:b(j)=i
gs,j = 0, i∈ N,
fs =BA ⊤ϕs, ϕ s,r = 0,
0≤g s,j ≤ gs,j, j∈ G,
− f ℓ ≤f s,ℓ ≤ f ℓ, ℓ∈ L,
(5)
where gs is generator dispatch, fs is line flow, ϕs is the vector of bus voltage angles, b(j) is the
bus containing generator j, and r is the reference bus. The sets N , G, and L collect the buses,
generators, and lines; the dispatch bounds and the flow–angle relation carve out the feasible set
Ys of Equation (1), and the state ωs supplies the demand ds, the offer curves, and the available
quantities gs. Each generator offer contains three quantity–marginal-price breakpoints (ξs,j,k, ps,j,k).
If πs,j denotes their piecewise-linear interpolation, then the production cost used in Equation (5) is
its integral,
Cs,j(g) =
Z g
0
πs,j(u) du,
πs,j(u) =p s,j,k + ps,j,k+1 −p s,j,k ξs,j,k+1 −ξ s,j,k (u−ξ s,j,k), u∈[ξ s,j,k, ξs,j,k+1]. (6)
Thus, the increasing interpolated marginal offers produce piecewise-quadratic, strictly convex genera-
tion costs. The dual variable of the nodal-balance constraint at busiis the locational marginal price
(LMP) λs,i(q) used in the planning objective. Within a fixed nondegenerate active-set regime, the
market KKT system defines a locally differentiable primal–dual solution map, and the LMPs generally
vary with the data-center allocation. Some directions can nevertheless have zero sensitivity—for
example, reallocating a fixed total load in an uncongested state with a uniform nodal price—and a
unique derivative need not exist exactly where an offer segment or transmission constraint changes
status. Section A evaluates both stable active-set regimes and one-sided behavior near such changes.
B.3 Shift-factor implementation and LMP recovery
The implementation (DiffOpt.jl over Ipopt) clears each state in an equivalent shift-factor form
of Equation (5) [Stott et al., 2009] rather than in the angle form above. Eliminating fs and ϕs
through fs =BA ⊤ϕs aggregates the nodal balances into a single system-wide balance equality
and expresses each line limit as a pair of inequalities on shift-factor-weighted net nodal injections,
with the shift-factor matrix H computed from A and B relative to the reference bus r. Every line
is monitored in both directions at its original rating, so the two forms have identical solutions. For
numerical robustness, the solved model softens these constraints with penalized slack variables, at
penalty prices of 5000 (line limits) and 10000 (system balance) in the market’s price units. The
penalties cap the corresponding duals but sit far above every cleared price, and the recorded maximum
constraint violation is zero across all reported runs, so the reported results coincide with the hard-
constrained model of Equation (5). Nodal prices are recovered from the duals of the shift-factor form
as λs,i =σ s + P k Hki µs,k, where σs is the dual of the system balance and µs,k are the duals of the line inequalities. This composition equals the nodal-balance duals of the angle form, and it is the
map through which reverse-mode differentiation propagates price sensitivities, with the entries of H
entering the chain rule as constants.
B.4 Objective normalization and optimization protocol
We express the fixed site cost as κ/∆E, where ∆E is the difference between the worst and best
one-site mean energy expenditures in that instance. This normalization measures construction cost
7

relative to the energy savings available from choosing a better single site. The resulting dimensionless
sweep spans 0 to 0.12 for Erd˝os–R´enyi and 0 to 0.26 for GeoDe. The scale factors are computed
from the instances, rather than chosen: ∆E≈735 for Erd˝os–R´enyi and ∆E≈566 for GeoDe, in
the objective’s units.
The forward-pass temperature is τ= 0.02 , while the straight-through backward-pass temperature
is geometrically annealed from 2.0 to 0.2 over training. For each penalty, the learned method runs
full-batch Adam for 450 iterations with learning rate 0.02. Its five initial logits are seeded Gaussian
perturbations with standard deviation 0.01 around zero, and hence near the uniform allocation. We
discard sites assigned less than 1 MW, renormalize the remaining allocation to 50 MW, and refine it
on the committed support using two 50-step Adam runs followed by pairwise coordinate refinement.
We then re-clear all 36 states with the exact number of retained sites and select the run with the lowest
resulting objective. These five runs vary only the nearby optimizer initialization, not the network or
market states.
B.5 Numerical reference and validation
For the numerical reference, we enumerate all 26 −1 = 63 nonempty supports and numerically
minimize mean energy expenditure conditional on each support, requiring every selected site to
receive at least 1 MW. Supports of size at most three use a simplex grid with denominator 25; larger
supports use four 150-step Adam runs with learning rate 0.03. Pairwise coordinate refinement starts
at a 1 MW step and terminates at 0.02 MW or after 20 sweeps. We add κ times the support size and
take the lower envelope over supports. We refer to this lower envelope as thenumerical optimum.
This is an operational term rather than a claim of solver-certified global optimality: the discrete
support search is exhaustive, but the allocation conditional on each support is solved numerically.
Single-site values are exact. As an additional check, we independently probed all 15 two-site supports
in each instance. Combining this search with the conditional optimizer produces no material change
in the best two-site value: it finds no improvement for Erd ˝os–R´enyi and an improvement of only
6.6×10 −5 objective units for GeoDe. The GeoDe reference envelope uses only one- and two-site
portfolios, as does the Erd˝os–R´enyi envelope except at zero fixed cost, where it uses three sites. These
checks provide strong evidence that the numerical optimum is close to the global optimum, while the
three-site Erd˝os–R´enyi solution remains uncertified. The experiment records every support, optimizer
seed, and training trace; parallel execution changes scheduling but not the seeded problem or per-run
configuration.
B.6 Initialization sensitivity
Figure 3 aggregates all five runs at each evaluated penalty instead of selecting the lowest-objective
run. The error bars measure variation across the five tested optimizer initializations only: the network
instance, market states, hyperparameters, commitment rule, and post-commitment refinement remain
fixed. They are descriptive sample standard deviations, not confidence intervals over networks or
operating states. Thus, this analysis characterizes local initialization stability around the near-uniform
allocation; broader basin sensitivity would require a wider initialization study.
C Why the learned support switch lags the reference
In Figure 2, the learned portfolios keep a second site open at fixed costs where the numerical reference
has already switched to a single site. This appendix shows that the lag is a measurable property of
the relaxed objective the optimizer is given, not a failure to minimize it: training replaces the site
count ∥q∥0 with the smooth count Kτ (w), so the relevant question is how much load thesmoothed
objective assigns to a second site at each fixed cost.
We answer this question by direct measurement, without any training. For each instance we interpolate
linearly between the best single-site allocation and the reference two-site allocation, and evaluate
the smoothed objective E(w) +κK τ (w) at every intermediate allocation, where E(w) is the mean
re-cleared energy expenditure obtained from forward market clears and τ= 0.2 is the terminal
backward temperature of the annealing schedule. For eachκwe then follow this objective downhill
from the two-site end of the path and record the second-site load at which descent stops. Figure 4
compares this prediction with the relaxed allocations that the trained runs actually reach.
8

Figure 3: Mean ± one sample standard deviation across five seeded optimizer initializations. Squares
aggregate the committed and refined objectives and site counts; triangles aggregate the relaxed
objectives and smooth site counts. Away from the two sampled transition points, this aggregation
preserves the qualitative pattern shown by the best-of-five curves.
Two mechanisms are visible. First, because Kτ charges a partially open site less than a fully open
one, the smoothed objective responds to a rising fixed cost by shrinking the second site rather than
closing it: its preferred second-site load decreases smoothly through the true-objective breakpoint and
collapses to zero only at κ/∆E≈0.049 on Erd˝os–R´enyi and ≈0.13 on GeoDe, versus breakpoints
of 0.032 and 0.090. The trained runs track the measured curve closely throughout this region, which
accounts for most of the observed lag. Second, near the collapse the smoothed objective is bistable:
the shrunken two-site configuration and the collapsed one-site configuration are separated by a barrier,
so gradient descent keeps whichever configuration it approaches from, and a collapsed iterate cannot
reopen the second site. This bistability matches the disagreement between initializations observed
exactly at the switch points (Appendix B.6). The short tail of small second-site loads beyond the
predicted collapse, up to κ/∆E≈0.06 and ≈0.18 , reflects the finite annealing schedule: the penalty
reaches its terminal temperature only late in training, and the remaining drain does not complete
within the 450 iterations before commitment.
Figure 4: Second-site load requested by the smoothed training objective (solid line), measured by
evaluating E(w) +κK τ (w) with forward market clears along the path between the best one-site and
reference two-site allocations, compared with the relaxed allocations reached by the trained runs
(squares; five initializations per fixed cost). The dashed line marks the fixed cost at which the true
objective closes the second site. The smoothed objective shrinks the second site past this breakpoint
instead of closing it, and the trained runs follow the measured curve.
9
