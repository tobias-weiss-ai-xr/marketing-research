---
title: A Momentum-Based Variance-Reduced Algorithm for Federated Multiobjective Optimization
url: https://arxiv.org/abs/2608.22945
category: ai-marketing
subcategory: measurement
date: 2026-08
venue: ''
authors:
- Yong Zhao
- Chunlin You
- Minh N. Dao
- Zai-Yun Peng
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.22945
pages: 36
chars: 75203
fetched_at: '2026-11-08T13:29:49+00:00'
kb_version: 1
---

# A Momentum-Based Variance-Reduced Algorithm for Federated Multiobjective Optimization

A Momentum-Based Variance-Reduced Algorithm for
Federated Multiobjective Optimization
Yong Zhao∗†, Chunlin You ‡, Minh N. Dao §, and Zai-Yun Peng ¶ ‖
August 24, 2026
Abstract
Federated learning has traditionally been formulated as a single-objective optimization prob-
lem, primarily focused on maximizing model utility. In real-world applications, however, machine
learning models often need to optimize multiple and potentially conflicting objectives simultane-
ously. This motivates federated multiobjective optimization (FMOO), which provides a natural
framework for jointly handling multiple task-specific objectives in federated learning. In this
paper, we propose a momentum-based variance-reduced algorithm for federated multiobjective
optimization. The method incorporates a momentum-driven gradient estimator into the local
updates to reduce the variance of stochastic updates, leading to an improved convergence rate.
We establish theoretical guarantees showing that the expected Pareto stationarity measure of a
randomly selected output iterate decays at a rate ofO(T−2/3), improving upon theO(T −1/2)
rates established for existing methods such as FSMGDA and FedCMOO. Numerical experi-
ments on federated multiobjective optimization benchmarks demonstrate the effectiveness and
competitive performance of the proposed algorithm.
Keywords:Federated multiobjective optimization, nonconvex optimization, momentum-based
variance reduction, communication complexity, stochastic multi-gradient methods.
Mathematics Subject Classification (MSC 2020):90C29, 90C15, 90C26.
1. Introduction
In recent years, multiobjective optimization (MOO) has emerged as a foundational paradigm for
multi-agent and multi-task learning, with broad applications spanning multi-task neural network
training [1], recommender systems [2], learning-to-rank tasks [3,4], and economic or transportation
∗College of Mathematics and Statistics, Chongqing Jiaotong University, Chongqing 400074, China.
†Key Laboratory of Complex Systems Optimization and Intelligent Control of Chongqing Municipal Education
Commission, Chongqing 400074, China. Email: zhaoyongty@126.com.
‡College of Mathematics and Statistics, Chongqing Jiaotong University, Chongqing 400074, China. E-
mail:1332967558@qq.com.
§Corresponding author. School of Science, RMIT University, Melbourne, VIC 3000, Australia. E-mail:
minh.dao@rmit.edu.au
¶School of Mathematics, Yunnan Normal University, 650092 Kunming, Yunnan, China.
‖Yunnan Key Laboratory of Modern Analytical Mathematics and Applications, Kunming, 650500, People’s Re-
public of China. E-mail: pengzaiyun@126.com.
1
arXiv:2608.22945v1  [cs.LG]  24 Aug 2026

scheduling [5–7]. Unlike single-objective optimization, MOO seeks to simultaneously optimize mul-
tiple interrelated and often conflicting objectives. Consequently, it is typically impossible to find a
single solution that minimizes all objectives at once. Therefore, MOO algorithms instead aim to
find aPareto optimal/stationarysolution, where any further improvement in one loss necessarily
worsens another. Existing MOO algorithms are predominantly designed for centralized learning
settings, where data from all participants must be aggregated on a central server for joint optimiza-
tion. This centralized paradigm not only limits scalability in distributed multi-agent systems but
also conflicts with increasingly stringent privacy and data localization requirements, particularly in
sensitive domains such as healthcare and finance.
Federated learning (FL) has emerged as a transformative distributed machine learning paradigm
that enables multiple participants to collaboratively train models without sharing raw data, thereby
addressing critical challenges related to data privacy and data silos [8,9]. Since the seminal work by
McMahan et al. [8], which introduced FedAvg as the first representative FL algorithm, substantial
research efforts have been devoted to understanding and extending this approach. FedAvg follows
a client–server architecture: in each communication round, participating clients perform several
steps of local stochastic gradient descent (SGD) on their private datasets, after which the server
aggregates the uploaded local model parameters via weighted averaging to update the global model.
Under standard assumptions, it has been shown that FedAvg achieves a sublinear convergence rate
when decaying learning rates are employed [10,11]. However, despite SGD’s statistically optimal
convergence rate, its performance often depends on careful tuning of the learning rate, and this
sensitivity is also inherited by FedAvg. To address these challenges, a wide range of methodological
innovations have been proposed. Regularization-based methods [12–16] modify the local objective
by introducing a proximal term that penalizes deviations from the global model, thereby promoting
consistency across clients and mitigating client drift. Laplacian regularization is also employed
in federated multitask learning to exploit relationships among client models [17]. Momentum-
based techniques [18–21] accumulate historical gradient information to correct update directions,
accelerating convergence and reducing bias induced by non-IID data. In response to difficulties in
learning rate tuning and unstable local optimization, recent studies [22] have integrated adaptive
optimization algorithms—such as Yogi [23], Adagrad [24] and Adam —into the federated setting.
These methods enable automatic adjustment of step sizes based on gradient statistics at both
the local and global levels, providing convergence guarantees under suitable assumptions for both
IID and non-IID settings. Variance reduction (VR) techniques [25–30] further improve convergence
stability by employing control variates or historical global gradient corrections to mitigate the client
drift and variance caused by data heterogeneity. For more research progress on federated learning
algorithms, please refer to [31].
Despite a rich body of literature on federated learning algorithms, most existing studies remain
limited to single-objective optimization, where all clients jointly minimize one global loss function.
However, in real-world applications, machine learning models often need to optimize multiple ob-
jectives simultaneously—such as improving model accuracy, and reducing training costs—which
frequently conflict with one another. It is in this context that federated multiobjective optimiza-
tion (FMOO) has emerged. By integrating the principles of federated learning and multiobjec-
tive optimization, it aims to achieve the synergistic optimization of multiple learning goals while
preserving data privacy, thereby meeting the diverse demands of practical applications. Yang et
al. [32] propose two federated multiobjective optimization (FMOO) algorithms called federated
multi-gradient descent averaging (FMGDA) and federated stochastic multi-gradient descent aver-
aging (FSMGDA) to solve FMOO, and establish the convergence of the two proposed algorithms
under suitable conditions. Askin et al. [33] introduce FedCMOO, a communication-efficient feder-
2

ated multiobjective optimization algorithm that improves convergence performance without scaling
communication costs with the number of objectives. Furthermore, the effectiveness and advantages
of the proposed method are empirically validated through extensive comparisons with FSMGDA.
Hartmann et al. [34] present the first comprehensive survey on the integration of multiobjective
methods with federated learning, introducing a novel taxonomy to systematically classify existing
works while offering insights into recent trends, open challenges, and future research directions.
Inspired by the work in [29–35], we propose FSMGDA-M-VR, a momentum-based variance-
reduced algorithm for federated multiobjective optimization. The design of our method is moti-
vated by two related but previously separate research directions. The first is momentum-based
variance reduction in federated learning, where methods such as STEM [30] improve the quality
of stochastic descent directions and mitigate the effect of client-side sampling noise. The second
is variance-reduced stochastic multiobjective optimization, where recent methods such as [35] show
that tracking or momentum-type estimators can effectively reduce the bias and variance in multi-
gradient construction. However, existing federated variance-reduction methods are mainly designed
for single-objective optimization, while existing variance-reduced multiobjective methods are typ-
ically developed in centralized environments. Thus, they do not directly address the combined
challenges of multiple conflicting objectives, heterogeneous clients, local stochastic updates, and
server-client communication.
FSMGDA-M-VR addresses these challenges by reorganizing how objective-wise descent informa-
tion and Pareto weights are computed in federated multiobjective training. Unlike FSMGDA [32],
which aggregates accumulated stochastic gradients without explicit variance reduction, FSMGDA-
M-VR constructs objective-wise momentum variance-reduced directions at each client. This reduces
the stochastic error accumulated across local steps and provides more stable objective-wise infor-
mation for server aggregation. It also differs from FedCMOO [33]. In FedCMOO, the server first
approximates the Gram matrix of the objective gradients, updates the task weights through pro-
jected gradient steps, and then sends these weights to clients for weighted local updates. In contrast,
FSMGDA-M-VR does not compute the Pareto weights before local training. Instead, clients first
maintain objective-wise variance-reduced directions, and the server computes the Pareto balanc-
ing weights only after aggregating these directions. Therefore, the common descent direction is
constructed from variance-reduced multiobjective information rather than from a pre-local-update
weight vector.
This design leads to a clear communication–convergence trade-off. FedCMOO enjoys the ad-
vantage that its per-round communication cost can be independent of the number of objectives,
whereas FSMGDA-M-VR requires each client to transmit one direction per objective and hence its
per-round communication cost scales linearly with the number of objectives. The benefit is that
the server receives richer objective-wise and variance-reduced information, which helps construct
a more stable Pareto common descent direction. In this sense, FSMGDA-M-VR can be viewed
as a federated multiobjective adaptation of momentum-based variance reduction, where objective-
wise local momentum tracking, federated aggregation, and adaptive Pareto direction construction
are integrated into a single training protocol. The main technical contribution lies in the conver-
gence analysis of this scheme under federated multiobjective stochastic updates, showing that the
estimator error can be controlled across local steps and communication rounds. Furthermore, we
establish a convergence rate ofO(T−2/3), improving upon theO(T −1/2)rates of FSMGDA [32]
and FedCMOO [33]. Extensive experiments further demonstrate the competitive performance of
FSMGDA-M-VR over existing federated multiobjective optimization methods.
3

2. Preliminaries
FMOO aims at optimizing multiple objectives simultaneously:
min
x∈Rd
F(x) := (f 1(x),...,f S(x)),(2.1)
wherex∈R d is the model parameter, and eachfs represents the objective function of tasks∈
[S] :={1,...,S}, defined by
fs(x) = 1 M M∑ i=1 fs,i(x),
with
fs,i(x) =E ξi∼Di[Fs(x;ξi)],
Here,Mdenotes the number of clients, and the random variableξ i represents a local data point
available at clienti. We consider a synchronous full-participation federated setting, where all
clients participate in each communication round with equal weights. Client dropout, communication
compression, and quantization are not considered in the present analysis.
Unlike single-objective optimization, in MOO there generally does not exist a single solution
that simultaneously minimizes all objectives. Therefore, a more appropriate notion of optimality in
MOO is Pareto optimality, which is formally defined as follows.
Definition 2.1 (Pareto optimality).For any two solutionsx,y∈R d, we sayxdominatesyif
and only iffs(x)≤f s(y),∀s∈[S]andf s(x)<f s(y),∃s∈[S]. A solutionx∈R d isPareto optimal
if it is not dominated by any other solution. A solutionx∈Rd isweakly Pareto optimalif there
does not exist a solutionysuch thatfs(y)<f s(x),∀s∈[S].
Similar to single-objective non-convex optimization, finding a Pareto optimal solution in MOO
can be computationally challenging, particularly in non-convex settings. Therefore, Pareto station-
arity is commonly adopted as a practical first-order optimality criterion.
Definition 2.2 (Pareto stationarity).A solutionx∈R d is said to bePareto stationaryif there
is no common descent directiond∈Rd such that∇fs(x)⊤d<0,∀s∈[S].
Gradient-based MOO algorithms typically seek a common descent directiond∈Rd such that
∇fs(x)⊤d<0for alls∈[S]. If no such common descent direction exists at a given point, then ac-
cording to Definition 2.2,xis a Pareto stationary solution. To determine such a direction, the multi-
gradient method constructs the gradient matrixG(x) := [∇f1(x),...,∇f S(x)]∈R d×S and identifies
the optimal weightλ∗ by solving the quadratic optimization problemλ∗(x)∈arg min λ∈C∥G(x)λ∥2,
whereC:={λ∈[0,1] S : ∑ s∈[S]λs = 1}. It then defines the multi-gradient direction as
g=G(x)λ ∗ =∑ s∈[S]λ∗ s∇fs(x). If∥g∥= 0, thenxisaParetostationary solution; otherwise,d=−g
is a common descent direction, and the iteration is performed according tox←x+ηd, or equiva-
lently,x←x−ηg, whereηdenotes the learning rate, until a Pareto stationary solution is reached.
The SMGD method follows a similar procedure to MGD, with the main difference being that the
exact gradient matrixG(x)is replaced by its stochastic counterpart. Thus,∥g∥2 =∥G(x)λ∗∥2 can
serve as a stationarity measure for assessing the convergence of non-convex MOO algorithms.
Definition 2.3 (ϵ-Pareto stationarity [36]).An iteratext generated by a stochastic algorithm
is said to be anϵ-Pareto stationary solution in expectationif
E
[
G(xt) ] ≤ϵ,
4

where
G(x) := min
λ∈C
‖‖‖‖‖ S∑ s=1 λs∇fs(x) ‖‖‖‖‖ 2 .
The expectation is taken with respect to all the randomness generated by the algorithm up to
iterationt.
To facilitate the subsequent convergence analysis, we introduce the following assumptions.
Assumption 2.1.(A1)For eachs∈[S],f s isL-smooth, i.e.,∥∇f s(x)−∇f s(y)∥≤L∥x−y∥, for
anyx,y∈R d;
(A2)For eachs∈[S],i∈[M], and any realizationξ i drawn fromDi,F s(·;ξi)isL-smooth, i.e.,
∥∇Fs(x;ξi)−∇F s(y;ξi)∥≤L∥x−y∥,∀x,y∈R d.
By Assumption 2.1 (A2) and Jensen’s inequality, eachfs,i is alsoL-smooth. Indeed,
∥∇fs,i(x)−∇f s,i(y)∥=∥E ξi [∇Fs(x;ξi)−∇F s(y;ξi)]∥
≤E ξi [∥∇Fs(x;ξi)−∇F s(y;ξi)∥]
≤L∥x−y∥,∀x,y.
Assumption 2.2.There exists a constantσ >0such that, for anyx∈R d,s∈[S], andi∈[M],
Eξi∼Di [∇Fs(x;ξi)] =∇f s,i(x),
and
Eξi∼Di
[
∥∇Fs(x;ξi)−∇f s,i(x)∥2
]
≤σ 2.
3. FSMGDA-M-VR algorithm
In what follows, we propose a momentum-based variance-reduced federated stochastic multi-
gradient descent algorithm (FSMGDA-M-VR) for solving (2.1), as outlined in Algorithm 1.
At communication roundtand local stepk, each clientiindependently draws a sampleξt,k i ∼D i.
The samples are independent across clients, local steps, and communication rounds, but are not
necessarily identically distributed across clients since the distributions{Di}M i=1 may differ. For each
fixed(t,k,i), the same sampleξ t,k i is used for all objectivess∈[S]. In particular, the variance-
reduction mechanism evaluates∇Fs(xt,k s,i;ξt,k i )and∇F s(xt−1;ξt,k i )using the same realizationξt,k i .
As shown in Algorithm 1, after initializing the model parameters and historical gradients, the
algorithm proceeds iteratively over multiple communication rounds. At each communication round
t, all clients receive the current global modelxt and, in parallel, performKlocal update steps for
each objective functions∈[S]. In each local stepk, clienticomputes a variance-reduced descent
direction for objectivesby combining the current stochastic gradient with a momentum-based
correction term:
gt,k s,i =∇F s(xt,k s,i;ξt,k i ) + (1−β) ( gt−1 s −∇Fs(xt−1;ξt,k i ) ) .
The local model is then updated asx t,k+1 s,i =x t,k s,i−ηg t,k s,i. After completing allKlocal steps,
each client computes the average gradient estimate for each objectiveg t s,i = 1 K ∑K−1 k=0 gt,k s,i and
sends the directions to the server. On the server side, the uploaded estimates are aggregated
across clients to formg t s = 1 M ∑M i=1gt s,i. To determine a multi-gradient direction that balances
5

Algorithm 1:FSMGDA-M-VR
Input:Initial modelx −1 =x 0, initialization batch sizeB∈N, initial gradient estimate
g−1 s = 1 BM ∑M i=1 ∑B b=1∇Fs(x−1;ξb i )fors∈[S]with mutually independent samples
{ξb i :i∈[M], b∈[B]}andξ b i∼D i, local learning rateη >0, global learning rate
γ >0, and momentum parameterβ∈(0,1)
Output:(x a,λa), whereais chosen uniformly at random from{0,1,...,T−1}.
fort= 0,1,...,T−1do
foreach clientiin paralleldo
Initial local modelxt,0 s,i =x t foreachsin paralleldo
fork= 0,1,...,K−1do
Compute directiongt,k s,i =∇F s(xt,k s,i;ξt,k i ) + (1−β) ( gt−1 s −∇Fs(xt−1;ξt,k i ) )
Update local modelxt,k+1 s,i =x t,k s,i−ηg t,k s,i
end
Aggregate local updatesgt s,i = 1 K ∑K−1 k=0 gt,k s,i
end
end
Computeg t s = 1 M ∑M i=1gt s,i,∀s∈[S]
Computeλ t,∗∈[0,1] S by solving
min
λts≥0
‖‖‖‖‖‖ ∑ s∈[S] λt sgt s ‖‖‖‖‖‖ 2 ,s.t. ∑ s∈[S] λt s = 1
Compute global multi-gradient directiongt =∑ s∈[S]λt,∗ s gt s
Update global modelxt+1 =x t−γg t
end
multiple objectives, the server solves the following convex quadratic optimization problem with
linear constraints:min
λts≥0, ∑ s∈[S]λts=1
‖‖‖∑ s∈[S]λt sgt s ‖‖‖ 2 , which yields the optimal weight coefficientsλt,∗ s .
These coefficients are used to construct the global directiongt = ∑S s=1λt,∗ s gt s. Finally, the global
model is updated asxt+1 =x t−γg t.
Remark 3.1.Relative to FSMGDA, the server-side Pareto aggregation mechanism remains un-
changed. The main algorithmic modification is the introduction of an objective-wise momentum
variance-reduced estimator into the local updates. The principal technical contribution is the anal-
ysis showing that this modification improves the stationarity rate fromO(T−1/2)toO(T −2/3).
4. Convergence analysis
In this section, we show that Algorithm 1 achieves a convergence rate ofO(T− 2 3 )in the nonconvex
case. To facilitate the theoretical analysis, we first introduce the filtration used to characterize the
evolution of the iterates and the randomness generated during the execution of the algorithm.
Let
F0 =σ ({ ξb i : 1≤i≤M,1≤b≤B }) ,
6

where{ξ b i : 1≤i≤M,1≤b≤B}are the samples used to initializeg −1 s , withξ b i ∼D i. These
initialization samples are mutually independent and are independent of all samples generated in
the subsequent communication rounds. Hence, the initial gradient estimatesg−1 s ,s∈[S], areF 0-
measurable. For each communication roundt,Ft denotes theσ-algebra containing all randomness
revealed before the beginning of roundt. Within roundt, we define the local-step filtration
Ft,k =σ ( Ft∪ { ξt,j i : 1≤i≤M,0≤j <k }) , k= 0,1,...,K.
Thus,F t,0 =F t, andF t,k contains all randomness revealed before thek-th local update in round
t. After completing theKlocal steps, we set
Ft+1 =F t,K =σ ( Ft∪ { ξt,j i : 1≤i≤M,0≤j <K }) .
Under this definition, the local variablesx t,k s,i and all global quantities available before thek-th
local update, includingx t,x t−1, andg t−1 s , areF t,k-measurable, whereas the fresh sampleξt,k i is
independent ofF t,k. Moreover, conditioned onFt,k, the samples{ξt,k i }M i=1 are independent across
clients and satisfyξ t,k i ∼D i.We useE[·|F t,k]to denote the conditional expectation given the
σ-algebraF t,k, which contains all randomness revealed before thek-th local update in roundt,
andE[·]to denote the expectation over all randomness in the algorithm. Throughout the proofs,
we use∑ i to denote the summation overi∈{1,...,M}and ∑ k to denote the summation over
k∈{0,...,K−1}. For allt≥0, we define the auxiliary variables as follows:
Et s :=E[∥∇f s(xt)−g t s∥2],
Ut s := 1 KM ∑ i ∑ k E[∥xt,k s,i−xt∥2],
ζt,k s,i :=E[x t,k+1 s,i −xt,k s,i|Ft,k],
Ξt s := 1 M M∑ i=1 E[∥ζt,0 s,i∥2].
Furthermore, letx−1 :=x 0 andE −1 s :=E [ ∥∇fs(x0)−g −1 s ∥2] . For the subsequent analysis, we
also define the auxiliary initial aggregated multi-gradient direction using the same minimum-norm
aggregation rule as in Algorithm 1. Specifically, let
λ−1,∗∈arg min
λ∈C
‖‖‖‖‖‖ ∑ s∈[S] λsg−1 s ‖‖‖‖‖‖ 2 ,
and define
g−1 := ∑
s∈[S]
λ−1,∗ s g−1 s .
By construction,g−1 isF 0-measurable.
To establish the convergence properties of Algorithm 1, we further impose the following bound-
edness condition along the sequence of iterates generated by the algorithm.
Assumption 4.1.Let{x t}t≥0 be the sequence generated by Algorithm 1. There exists a constant
D>0such that
sup
t≥0,s∈[S]
1
M
M∑
i=1
E
[
∥∇fs,i(xt)∥2
]
≤D 2,
where the expectation is taken with respect to the randomness of the algorithm up to iterationt.
7

Remark 4.1.Assumption 4.1 controls the local expected gradients along the sequence generated
by Algorithm 1. Specifically, it requires the client-averaged squared norms of the local expected
gradients, evaluated along the generated trajectory, to be uniformly bounded in expectation. Such
boundedness conditions are commonly adopted in the analysis of federated learning and federated
multiobjective learning [13,22,30,32], as well as in stochastic multiobjective optimization [36–
39]. Unlike a global bounded-gradient condition imposed for allx, Assumption 4.1 only requires
boundedness along the sequence generated by the algorithm and is sufficient for our convergence
analysis.
Our subsequent analysis will be based on the following foundational lemmas.
Lemma 4.1.Under Assumption 2.1, ifγL≤ 1 2, then, for allt≥0,
E[fs(xt+1)]≤E[f s(xt)]− γ 4 E[∥gt∥2] +γ 2Et s, s∈[S].
and
2
(
E[fs(xT )]−f s(x0) )
γ + 1 2 T−1∑ t=0 E[∥gt∥2]≤ T−1∑ t=0 Et s, s∈[S].
Proof.By theL-smoothness off s, we have
fs(xt+1)≤f s(xt) + ⟨ ∇fs(xt),−γg t ⟩ + 1 2L∥γgt∥2
=f s(xt) + ⟨ ∇fs(xt)−g t s,−γg t ⟩ −γ ⟨ gt s,gt ⟩ + 1 2L∥γgt∥2
≤f s(xt)−γ ⟨ ∇fs(xt)−g t s,gt ⟩ −γ∥g t∥2 + 1 2L∥γgt∥2
≤f s(xt) +γ 2∥∇fs(xt)−g t s∥2 + γ 2∥gt∥2−γ∥g t∥2 + 1 2Lγ2∥gt∥2
=f s(xt) +γ 2∥∇fs(xt)−g t s∥2−γ (1 2− 1 2Lγ ) ∥gt∥2,
where the second inequality follows from the fact thatgt is the minimum-norm element inconv{gt s :
s∈[S]}. By the first-order optimality condition of this projection problem,
⟨gt s−g t,gt⟩≥0,∀s∈[S],
which implies that
⟨gt s,gt⟩≥∥g t∥2,∀s∈[S].
Withγ≤ 1 2L and taking the global expectation, we obtain
E[fs(xt+1)]≤E[f s(xt)]− γ 4 E[∥gt∥2] +γ 2Et s.
Then, summing the above inequality overt= 0,...,T−1yields
2
γ
T−1∑
t=0
(
E[fs(xt+1)−f s(xt)] ) + 1 2 T−1∑ t=0 E[∥gt∥2] = 2
(
E[fs(xT )]−f s(x0) )
γ + 1 2 T−1∑ t=0 E[∥gt∥2]≤ T−1∑ t=0 Et s,
which completes the proof.■
To handle local updates and client sampling, we will also use the following technical lemmas.
Lemma 4.2(See [25, Lemma 4]).Let{X1,...,X τ}be a collection ofRd-valued random variables
that are potentially dependent. Suppose thatE[Xi] =µ i andE[∥X i−µi∥2]≤σ 2,i= 1,...,τ. Then
E


‖‖‖‖‖ τ∑ i=1 Xi ‖‖‖‖‖ 2 ≤ ‖‖‖‖‖ τ∑ i=1 µi ‖‖‖‖‖ 2 +τ 2σ2.
8

Suppose that{Gi}τ i=0 is a filtration, i.e.,
G0⊆G 1⊆···⊆G τ
and thatXi isG i-measurable for eachi= 1,...,τ. Define
µi =E[X i|G i−1],
and suppose that
E
[
∥Xi−µi∥2|G i−1
]
≤σ 2, i= 1,...,τ.
Then{X i−µi}τ i=1 forms a martingale-difference sequence with respect to{Gi}τ i=0, and
E


‖‖‖‖‖ τ∑ i=1 Xi ‖‖‖‖‖ 2 ≤2E   ‖‖‖‖‖ τ∑ i=1 µi ‖‖‖‖‖ 2  + 2τσ2.
Lemma 4.3.Suppose that Assumptions 2.1–2.2 hold. IfγL≤
√
βKM
54 , then, for allt≥1,
Et s≤(1−β)E t−1 s + 4 βL2Ut s + 3β2σ2 KM + 2β 9 E[∥gt−1∥2].
and fort= 0,
E0 s≤(1−β)E −1 s + 4 βL2U 0 s + 3β2σ2 KM .
Proof.By the definition ofE t s, we have
Et s =E


‖‖‖‖‖‖ 1 KM ∑ i,k ∇Fs(xt,k s,i;ξt,k i ) + (1−β)  gt−1 s − 1 KM ∑ i,k ∇Fs(xt−1;ξt,k i )  −∇fs(xt) ‖‖‖‖‖‖ 2 
=E
[‖‖‖‖‖(1−β) ( gt−1 s −∇fs(xt−1) ) + 1 KM ∑ i,k ∇Fs(xt,k s,i;ξt,k i )−∇f s(xt)
+ (1−β)
(
∇fs(xt−1)− 1 KM ∑ i,k ∇Fs(xt−1;ξt,k i ) )‖‖‖‖‖ 2]
=(1−β) 2Et−1 s + 2E


⟨
(1−β)(g t−1 s −∇fs(xt−1)), 1 KM ∑ i,k ∇fs,i(xt,k s,i)−∇f s(xt) ⟩  /bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
Λ1
+E


‖‖‖‖‖‖ 1 KM ∑ i,k ∇Fs(xt,k s,i;ξt,k i )−∇f s(xt) + (1−β)  ∇fs(xt−1)− 1 KM ∑ i,k ∇Fs(xt−1;ξt,k i )   ‖‖‖‖‖‖ 2 
/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
Λ2
.
By the AM-GM inequality and Assumption 2.1,
Λ1≤β(1−β) 2Et−1 s + 1 β E


‖‖‖‖‖‖ 1 KM ∑ i,k ∇fs,i(xt,k s,i)−∇f s(xt) ‖‖‖‖‖‖ 2 
≤β(1−β) 2Et−1 s + 1 β 1 K2M 2 E


‖‖‖‖‖‖ ∑ i,k ( ∇fs,i(xt,k s,i)−∇f s,i(xt) ) ‖‖‖‖‖‖ 2 
9

≤β(1−β) 2Et−1 s + 1 β 1 KM E

∑
i,k
‖‖‖∇fs,i(xt,k s,i)−∇f s,i(xt) ‖‖‖ 2


≤β(1−β) 2Et−1 s + 1 β 1 KM E

∑
i,k
L2∥xt,k s,i−xt∥2


≤β(1−β) 2Et−1 s + 1 βL2Ut s.
ForΛ 2, we decompose it into three terms as
Λ2 =E


‖‖‖‖‖‖ 1 KM ∑ i,k ( ∇Fs(xt,k s,i;ξt,k i )−∇F s(xt;ξt,k i ) ) +β   1 KM ∑ i,k ∇Fs(xt;ξt,k i )−∇f s(xt)  
+ (1−β)

 1
KM
∑
i,k
(
∇Fs(xt;ξt,k i )−∇F s(xt−1;ξt,k i ) ) −∇fs(xt) +∇fs(xt−1)


‖‖‖‖‖ 2]
≤3E


‖‖‖‖‖‖ 1 KM ∑ i,k ( ∇Fs(xt,k s,i;ξt,k i )−∇F s(xt;ξt,k i ) ) ‖‖‖‖‖‖ 2 
/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
Φ1
+3E


‖‖‖‖‖‖ β   1 KM ∑ i,k ∇Fs(xt;ξt,k i )−∇f s(xt)   ‖‖‖‖‖‖ 2 
/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
Φ2
+3E


‖‖‖‖‖‖ (1−β)   1 KM ∑ i,k ( ∇Fs(xt;ξt,k i )−∇F s(xt−1;ξt,k i ) )  −∇fs(xt) +∇fs(xt−1) ‖‖‖‖‖‖ 2 
/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
Φ3
.
By Assumption 2.1,
Φ1 = 3 K2M 2 E


‖‖‖‖‖‖ ∑ i,k ( ∇Fs(xt,k s,i;ξt,k i )−∇F s(xt;ξt,k i ) ) ‖‖‖‖‖‖ 2 
≤ 3 KM E

∑
i,k
‖‖‖∇Fs(xt,k s,i;ξt,k i )−∇F s(xt;ξt,k i ) ‖‖‖ 2


≤ 3 KM ∑ i,k E [ L2 ‖‖‖xt,k s,i−xt ‖‖‖ 2]
= 3L2Ut s.
By Assumption 2.2,
Φ2 = 3β2 K2M 2 E


‖‖‖‖‖‖ ∑ i,k ( ∇Fs(xt;ξt,k i )−∇f s,i(xt) ) ‖‖‖‖‖‖ 2 
= 3β2
K2M 2 E

∑
i,k
‖‖‖∇Fs(xt;ξt,k i )−∇f s,i(xt) ‖‖‖ 2
10

+2
∑
(i,k)̸=(j,l)
⟨
∇Fs(xt;ξt,k i )−∇f s,i(xt),∇Fs(xt;ξt,l j )−∇f s,j(xt) ⟩


≤ 3β2
K2M 2
∑
i,k
σ2 = 3β2σ2
KM .
Again using Assumption 2.1, we have
Φ3 = 3(1−β) 2 K2M 2 E


‖‖‖‖‖‖ ∑ i,k ( ∇Fs(xt;ξt,k i )−∇F s(xt−1;ξt,k i ) +∇fs,i(xt−1)−∇f s,i(xt) ) ‖‖‖‖‖‖ 2 
= 3(1−β) 2
K2M 2 E

∑
i,k
‖‖‖∇Fs(xt;ξt,k i )−∇F s(xt−1;ξt,k i ) +∇fs,i(xt−1)−∇f s,i(xt) ‖‖‖ 2
+ 2
∑
(i,k)̸=(j,l)
⟨
∇Fs(xt;ξt,k i )−∇F s(xt−1;ξt,k i ) +∇fs,i(xt−1)−∇f s,i(xt),
∇Fs(xt;ξt,l j )−∇F s(xt−1;ξt,l j ) +∇fs,j(xt−1)−∇f s,j(xt) ⟩]
= 3(1−β) 2
K2M 2 E

∑
i,k
‖‖‖∇Fs(xt;ξt,k i )−∇F s(xt−1;ξt,k i ) +∇fs,i(xt−1)−∇f s,i(xt) ‖‖‖ 2


≤ 6(1−β) 2
K2M 2 E

∑
i,k
‖‖‖∇Fs(xt;ξt,k i )−∇F s(xt−1;ξt,k i ) ‖‖‖ 2 + ∑
i,k
‖‖‖∇fs,i(xt−1)−∇f s,i(xt) ‖‖‖ 2


≤ 6(1−β) 2
K2M 2 E

∑
i,k
L2∥xt−xt−1∥2 + ∑
i,k
L2∥xt−1−xt∥2


= 12(1−β) 2L2
KM E
[
||xt−xt−1∥2
]
.
Substituting these three bounds, we obtain
Λ2≤3L 2Ut s + 3β2σ2 KM + 12(1−β) 2 L2 KM E[∥xt−xt−1∥2].
Therefore, fort≥1,
Et s≤(1−β)E t−1 s + 4 βL2Ut s + 3β2σ2 KM + 12(1−β) 2 L2 KM E[∥xt−xt−1∥2]
≤(1−β)E t−1 s + 4 βL2Ut s + 3β2σ2 KM + 2β 9 E[∥gt−1∥2],
where the last inequality is derived byxt =x t−1−γg t−1 andγL≤
√
βKM
54 . Similarly, fort= 0, we
can obtain
E0 s≤(1−β)E −1 s + 4 βL2U 0 s + 3β2σ2 KM ,
which completes the proof.■
Lemma 4.4.Suppose that Assumptions 2.1–2.2 hold. IfηLK≤1and24e 2(ηL)4K4 + 24η2L2K≤
1
2, then
Ut s≤4e 2K2Ξt s + 12(ηK)2
(
8(ηKL) 2 +K−1
)(
β2σ2 + 4(γL)2E[∥gt−1∥2] ) .
11

Proof.Note that
ζt,k s,i =E[x t,k+1 s,i −xt,k s,i|F t,k] =E[−ηg t,k s,i|F t,k]
=−η
(
∇fs,i(xt,k s,i) + (1−β) ( gt−1 s −∇fs,i(xt−1) )) .
Throughout this proof, for a square-integrable random vectorX, we use the scalar conditional
variance
Var(X|F) :=E
[
∥X−E[X|F]∥ 2|F ] .
Thus, we have
E[∥ζt,j s,i−ζ t,j−1 s,i ∥2] =E [‖‖‖−η ( ∇fs,i(xt,j s,i) + (1−β) ( gt−1 s −∇fs,i(xt−1) ))
+η
(
∇fs,i(xt,j−1 s,i ) + (1−β) ( gt−1 s −∇fs,i(xt−1) ))‖‖‖ 2]
=E
[‖‖‖−η∇fs,i(xt,j s,i) +η∇fs,i(xt,j−1 s,i ) ‖‖‖ 2]
≤η2L2E[∥xt,j s,i−xt,j−1 s,i ∥2]
=η2L2
(
E[∥ζt,j−1 s,i ∥2] +E [ Var(xt,j s,i−xt,j−1 s,i |F t,j−1) ]) ,
where the last identity is the conditional bias–variance decomposition. Since
E
[
Var(xt,j s,i−xt,j−1 s,i |F t,j−1) ]
=E
[
Var(−ηgt,j−1 s,i |F t,j−1) ]
=E
[
E
[
∥−ηg t,j−1 s,i −E[−ηg t,j−1 s,i |F t,j−1]∥2|F t,j−1 ]]
=η2E
[‖‖‖∇Fs(xt,j−1 s,i ;ξt,j−1 i )−∇f s,i(xt,j−1 s,i )−(1−β) ( ∇Fs(xt−1;ξt,j−1 i )−∇f s,i(xt−1) )‖‖‖ 2]
=η2E [‖‖‖β ( ∇Fs(xt,j−1 s,i ;ξt,j−1 i )−∇f s,i(xt,j−1 s,i ) ) + (1−β) ( ∇Fs(xt,j−1 s,i ;ξt,j−1 i )−∇F s(xt−1;ξt,j−1 i ) )
+(1−β)
(
∇fs,i(xt−1)−∇f s,i(xt,j−1 s,i ) )‖‖‖ 2]
≤η2E
[
3β2
‖‖‖∇Fs(xt,j−1 s,i ;ξt,j−1 i )−∇f s,i(xt,j−1 s,i ) ‖‖‖ 2
+3(1−β) 2
‖‖‖∇Fs(xt,j−1 s,i ;ξt,j−1 i )−∇F s(xt−1;ξt,j−1 i ) ‖‖‖ 2 + 3(1−β) 2 ‖‖‖∇fs,i(xt−1)−∇f s,i(xt,j−1 s,i ) ‖‖‖ 2]
≤η2
(
3β2σ2 + 6(1−β) 2L2E[∥xt−1−xt,j−1 s,i ∥2] ) ,
where the last inequality follows from Assumptions 2.1 and 2.2. Thus, we have
E[∥ζt,j s,i−ζ t,j−1 s,i ∥2]
≤η2L2
(
E[∥ζt,j−1 s,i ∥2] + 3β2η2σ2 + 6η2(1−β) 2L2E[∥xt−1−xt,j−1 s,i ∥2] )
≤η2L2
(
E[∥ζt,j−1 s,i ∥2] + 3β2η2σ2 + 12η2L2E[∥xt−1−xt∥2 +∥xt−xt,j−1 s,i ∥2] ) .
Fixk∈{1,...,K−1}. For everyj∈{1,...,k−1}, Young’s inequality andηL≤K −1≤(k+ 1)−1
give
E[∥ζt,j s,i∥2]≤(1 + 1 k )E[∥ζt,j−1 s,i ∥2] + (1 +k)E[∥ζt,j s,i−ζ t,j−1 s,i ∥2]
≤(1 + 2 k )E[∥ζt,j−1 s,i ∥2] + (1 +k)η 2L2 ( 3β2η2σ2 + 12η2L2E[∥xt−1−xt∥2 +∥xt−xt,j−1 s,i ∥2] )
12

=(1 + 2 k )E[∥ζt,j−1 s,i ∥2] + 12(1 +k)(ηL) 4E[∥xt−xt,j−1 s,i ∥2] + (1 +k)η 4L2 ( 3β2σ2 + 12L2E[∥xt−1−xt∥2] )
≤(1 + 2 k ) ( (1 + 2 k )E[∥ζt,j−2 s,i ∥2] + 12(1 +k)(ηL) 4E[∥xt−xt,j−2 s,i ∥2]
+ (1 +k)η 4L2
(
3β2σ2 + 12L2E[∥xt−1−xt∥2] )) + 12(1 +k)(ηL) 4E[∥xt−xt,j−1 s,i ∥2]
+ (1 +k)η 4L2
(
3β2σ2 + 12L2E[∥xt−1−xt∥2] )
=(1 + 2 k )2E[∥ζt,j−2 s,i ∥2] + (1 + 2 k )12(1 +k)(ηL) 4E[∥xt−xt,j−2 s,i ∥2] + 12(1 +k)(ηL) 4E[∥xt−xt,j−1 s,i ∥2]
+ (1 + 2 k )(1 +k)η 4L2 ( 3β2σ2 + 12L2E[∥xt−1−xt∥2] ) + (1 +k)η 4L2 ( 3β2σ2 + 12L2E[∥xt−1−xt∥2] )
...
≤(1 + 2 k )jE[∥ζt,0 s,i∥2] + 12(1 +k)(ηL) 4
(
(1 + 2 k )j−1E[∥xt−xt,0 s,i∥2] +···+ (1 + 2 k )0E[∥xt−xt,j−1 s,i ∥2] )
+ (1 +k)η 4L2
(
3β2σ2 + 12L2E[∥xt−1−xt∥2] )( (1 + 2 k )0 +···+ (1 + 2 k )j−1 )
≤(1 + 2 k )k−1E[∥ζt,0 s,i∥2] + 12(1 +k)(ηL) 4 j−1∑ j′=0 ( (1 + 2 k )j−1−j ′ E[∥xt−xt,j′ s,i∥2] )
+
1−
(
1 + 2 k
)j
1−
(
1 + 2 k
) (1 +k)η 4L2
(
3β2σ2 + 12L2E[∥xt−1−xt∥2] )
≤e2E[∥ζt,0 s,i∥2] + 12e2k(ηL)4
j−1∑
j′=0
E[∥xt,j′ s,i −xt∥2] + 8k2L2η4 ( 3β2σ2 + 12L2E[∥xt−xt−1∥2] ) ,(4.2)
where the recursion is unrolled only over the indexj(withkfixed), and we use1 +k≤2k, and(
1 + 2 k
)k
≤e 2. Define
∆j :=x t,j+1 s,i −xt,j s,i, ε j := ∆j−ζ t,j s,i,0≤j≤k−1.
Thenε j isF t,j+1-measurable andE[εj|F t,j] = 0. If0≤j <ℓ≤k−1, thenε j isF t,ℓ-measurable,
and hence the tower property yields the martingale orthogonality relation
E⟨εj,εℓ⟩=E
[
E
[
⟨εj,εℓ⟩|F t,ℓ]] =E [⟨ εj,E[εℓ|F t,ℓ] ⟩] = 0.
Consequently,
E[∥xt,k s,i−xt∥2] =E


‖‖‖‖‖‖ k−1∑ j=0 (ζt,j s,i +εj) ‖‖‖‖‖‖ 2 
≤2E


‖‖‖‖‖‖ k−1∑ j=0 ζt,j s,i ‖‖‖‖‖‖ 2  + 2E   ‖‖‖‖‖‖ k−1∑ j=0 εj ‖‖‖‖‖‖ 2 
= 2E


‖‖‖‖‖‖ k−1∑ j=0 ζt,j s,i ‖‖‖‖‖‖ 2  + 2 k−1∑ j=0 E[∥εj∥2]
= 2E


‖‖‖‖‖‖ k−1∑ j=0 ζt,j s,i ‖‖‖‖‖‖ 2  + 2 k−1∑ j=0 E [ Var(∆j|F t,j) ]
13

≤2k
k−1∑
j=0
E[∥ζt,j s,i∥2] + 2
k−1∑
j=0
(
3β2η2σ2 + 12η2L2E[∥xt−1−xt∥2 +∥xt−xt,j s,i∥2] ) ,(4.3)
where the last line uses Cauchy–Schwarz and the conditional-variance bound proved above. By
combining (4.2) and (4.3),
E[∥xt,k s,i−xt∥2]
≤2k
k−1∑
j=0

e2E[∥ζt,0 s,i∥2] + 12e2k(ηL)4
j−1∑
j′=0
E[∥xt,j′ s,i −xt∥2] + 8k2L2η4 ( 3β2σ2 + 12L2E[∥xt−xt−1∥2] )


+ 2
k−1∑
j=0
(
3β2η2σ2 + 12η2L2E[∥xt−1−xt∥2 +∥xt−xt,j s,i∥2] ) .(4.4)
Summing (4.4) overk= 0,1,...,K−1, we have
K−1∑
k=0
E[∥xt,k s,i−xt∥2]
≤
K−1∑
k=0
2k
k−1∑
j=0
e2E[∥ζt,0 s,i∥2]
/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
1
+
K−1∑
k=0
2k
k−1∑
j=0
12e2k(ηL)4
j−1∑
j′=0
E[∥xt,j′ s,i −xt∥2]
/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
2
+
K−1∑
k=0
2k
k−1∑
j=0
8k2L2η4
(
3β2σ2 + 12L2E[∥xt−xt−1∥2] )
/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
3
+
K−1∑
k=0
2
k−1∑
j=0
(
3β2η2σ2 + 12η2L2E[∥xt−1−xt∥2] )
/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
4
+
K−1∑
k=0
2
k−1∑
j=0
12η2L2E[∥xt−xt,j s,i∥2]
/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
5
.
For 1 , we have
K−1∑
k=0
2k
k−1∑
j=0
e2E[∥ζt,0 s,i∥2] =
K−1∑
k=0
2k2e2E[∥ζt,0 s,i∥2]≤2K 3e2E[∥ζt,0 s,i∥2].
For 2 , we have
K−1∑
k=0
2k
k−1∑
j=0
12e2k(ηL)4
j−1∑
j′=0
E[∥xt,j′ s,i −xt∥2]
=
K−1∑
k=0
24e2k2(ηL)4
k−1∑
j=0
(
E[∥xt,0 s,i−xt∥2] +E[∥xt,1 s,i−xt∥2] +···+E[∥x t,j−1 s,i −xt∥2] )
=
K−1∑
k=0
24e2k2(ηL)4
(
E[∥xt,0 s,i−xt∥2] + ( E[∥xt,0 s,i−xt∥2] +E[∥xt,1 s,i−xt∥2] )
+···+
(
E[∥xt,1 s,i−xt∥2] +···+E[∥x t,k−2 s,i −xt∥2] ))
=
K−1∑
k=0
24e2k2(ηL)4
(
(k−2)E[∥x t,1 s,i−xt∥2] + (k−3)E[∥x t,2 s,i−xt∥2] +···+E[∥x t,k−2 s,i −xt∥2] )
14

≤
K−1∑
k=0
24e2k2(ηL)4
(
kE[∥xt,1 s,i−xt∥2] +kE[∥xt,2 s,i−xt∥2] +···+kE[∥x t,k−2 s,i −xt∥2] )
=24e2(ηL)4
K−1∑
k=0
k3
(
E[∥xt,1 s,i−xt∥2] +E[∥xt,2 s,i−xt∥2] +···+E[∥x t,k−2 s,i −xt∥2] )
=24e2(ηL)4
(
33E[∥xt,1 s,i−xt∥2] + 43 ( E[∥xt,1 s,i−xt∥2] +E[∥xt,2 s,i−xt∥2] )
+···+ (K−1) 3
(
E[∥xt,1 s,i−xt∥2] +···+E[∥x t,K−3 s,i −xt∥2] ))
≤24e2(ηL)4
(
K3E[∥xt,1 s,i−xt∥2] +K 3 ( E[∥xt,1 s,i−xt∥2] +E[∥xt,2 s,i−xt∥2] )
+···+K 3
(
E[∥xt,1 s,i−xt∥2] +···+E[∥x t,K−3 s,i −xt∥2] ))
=24e2(ηL)4
(
(K−3)K 3E[∥xt,1 s,i−xt∥2] +···+K 3E[∥xt,K−3 s,i −xt∥2] )
≤24e2(ηL)4K4
K−1∑
k=0
E[∥xt,k s,i−xt∥2].
For 3 , we have
K−1∑
k=0
2k
k−1∑
j=0
8k2L2η4
(
3β2σ2 + 12L2E[∥xt−xt−1∥2] )
=
K−1∑
k=0
16k4L2η4
(
3β2σ2 + 12L2E[∥xt−xt−1∥2] )
≤16K5L2η4
(
3β2σ2 + 12L2E[∥xt−xt−1∥2] ) .
For 4 , we have
K−1∑
k=0
2
k−1∑
j=0
(
3β2η2σ2 + 12η2L2E[∥xt−1−xt∥2] )
=
K−1∑
k=0
2k
(
3β2η2σ2 + 12η2L2E[∥xt−1−xt∥2] )
≤2K2
(
3β2η2σ2 + 12η2L2E[∥xt−1−xt∥2] ) .
For 5 , we have
K−1∑
k=0
2
k−1∑
j=0
12η2L2E[∥xt−xt,j s,i∥2]
=
K−1∑
k=0
24η2L2
(
E[∥xt−xt,1 s,i∥2] +···+E[∥x t−xt,k−1 s,i ∥2] )
=24η2L2
(
E[∥xt−xt,1 s,i∥2] + ( E[∥xt−xt,1 s,i∥2] +E[∥xt−xt,2 s,i∥2] )
+···+
(
E[∥xt−xt,1 s,i∥2] +···+E[∥x t−xt,K−2 s,i ∥2] ))
=24η2L2
(
(K−2)E[∥x t−xt,1 s,i∥2] + (K−3)E[∥x t−xt,2 s,i∥2] +···+E[∥x t−xt,K−2 s,i ∥2] )
≤24η2L2K
K−1∑
k=0
E[∥xt−xt,k s,i∥2].
15

Combining 1 – 5 yields
K−1∑
k=0
E[∥xt,k s,i−xt∥2]
≤2K3e2E[∥ζt,0 s,i∥2] + 24e2(ηL)4K4
K−1∑
k=0
E[∥xt,k s,i−xt∥2] + 16K5L2η4 ( 3β2σ2 + 12L2E[∥xt−xt−1∥2] )
+ 2K2
(
3β2η2σ2 + 12η2L2E[∥xt−1−xt∥2] ) + 24η2L2K K−1∑
k=0
E[∥xt−xt,k s,i∥2]
=2K3e2E[∥ζt,0 s,i∥2] + (48K5η4L2 + 6K2η2) ( β2σ2 + 4L2E[∥xt−xt−1∥2] )
+
(
24e2(ηL)4K4 + 24η2L2K )K−1∑
k=0
E[∥xt−xt,k s,i∥2]
≤2K3e2E[∥ζt,0 s,i∥2] + (48K5η4L2 + 6K2η2) ( β2σ2 + 4L2E[∥xt−xt−1∥2] ) + 1 2 K−1∑ k=0 E[∥xt−xt,k s,i∥2],
where the last inequality follows from24e2(ηL)4K4 + 24η2L2K≤ 1 2. Thus, we obtain
K−1∑
k=0
E[∥xt,k s,i−xt∥2]≤4K 3e2E[∥ζt,0 s,i∥2] + 12(ηK)2(8K3η2L2 + 1) ( β2σ2 + 4L2E[∥xt−xt−1∥2] ) ,
Finally, summing overi= 1,...,M, dividing byKM, using the definitions ofU t s andΞ t s, and
substitutingx t−xt−1 =γg t−1, the conclusion follows.■
Lemma 4.5.Suppose that Assumptions 2.1 and 4.1 hold. Ifmax{1152e2(1−β)2 (ηKL) 2,1152e 2(1−
β)2( ηγKL 2)2}≤β 2, then the following inequality holds:
T−1∑
t=0
Ξt s≤ β2 288e2K2L2 T−1∑ t=0 ( Et−1 s +E[∥g t−1∥2] ) + 4η2TD 2.
Proof.Recall thatζ t,0 s,i =−η ( (1−β) ( gt−1 s −∇fs,i(xt−1) ) +∇fs,i(xt) ) . Consequently,
∥ζt,0 s,i∥2≤2η 2 ( (1−β) 2∥gt−1 s ∥2 +∥∇fs,i(xt)−(1−β)∇f s,i(xt−1)∥2 )
= 2η2(1−β) 2∥gt−1 s ∥2 + 2η2
‖‖‖(1−β) ( ∇fs,i(xt)−∇f s,i(xt−1) ) +β∇f s,i(xt) ‖‖‖ 2
≤2η 2(1−β) 2∥gt−1 s ∥2 + 4η2(1−β) 2∥∇fs,i(xt)−∇f s,i(xt−1)∥2 + 4(ηβ)2∥∇fs,i(xt)∥2
≤2η 2(1−β) 2∥gt−1 s ∥2 + 4(ηL)2(1−β) 2∥xt−xt−1∥2 + 4(ηβ)2∥∇fs,i(xt)∥2,
where the last inequality follows from Assumption 2.1. By Assumption 4.1 and the definition ofΞt s,
and summing overt= 0,...,T−1, we have
T−1∑
t=0
Ξt s =
T−1∑
t=0
1
M
M∑
i=1
E[∥ζt,0 s,i∥2]
≤
T−1∑
t=0
E
(
2η2(1−β) 2∥gt−1 s ∥2 + 4(ηL)2(1−β) 2∥xt−xt−1∥2 + 4(ηβ)2 1 M M∑ i=1 ∥∇fs,i(xt)∥2 )
≤
T−1∑
t=0
E
(
4η2(1−β) 2
(
∥gt−1 s −∇fs(xt−1)∥2 +∥∇fs(xt−1)∥2
)
+ 4(ηL)2(1−β) 2∥xt−xt−1∥2
+4(ηβ)2 1 M M∑ i=1 ∥∇fs,i(xt)∥2 )
16

≤4η2(1−β) 2
T−1∑
t=0
Et−1 s + 4η2(1−β) 2TD 2 + 4η2(1−β) 2(γL)2
T−1∑
t=0
E[∥gt−1∥2] + 4η2β2TD 2
=4η2(1−β) 2
T−1∑
t=0
Et−1 s + 4η2(1−β) 2(γL)2
T−1∑
t=0
E[∥gt−1∥2] + 4(1−2β+ 2β 2)η2TD 2
≤ β2
288e2K2L2
T−1∑
t=0
Et−1 s + β2 288e2K2L2 T−1∑ t=0 E[∥gt−1∥2] + 4η2TD 2,
where the last inequality follows frommax{1152e2(1−β) 2 (ηKL) 2,1152e 2(1−β) 2( ηγKL 2)2}≤
β2. ■
In the following theorem, we establish the convergence rate of the proposed algorithm.
Theorem 4.1.Suppose that Assumptions 2.1–2.2 and 4.1 hold, and thatfs(x)has a lower bound
f min s for allx∈R d. Let∆ := max s∈[S](fs(x0)−f min s ). If we set
β=
(
MKL 2( 1 +D 2)2 ∆2
σ4T 2
)1/3
<1, γ= min



1
2L, 1 L
√
βKM
54


,
ηKL≤c η min


β, 1√ K ,
√
β
M, β3/4
( L∆
(KM) 1/2T
)1/2  
,
wherec η >0is a sufficiently small absolute constant, and chooseB=
⌈
K
Tβ 2
⌉
, then Algorithm 1
admits the convergence guarantee
E[G(xa)]≲
(
L
(
1 +D 2) σ∆
KMT
) 2
3
(1 +S 2) +LS2∆ T
+ (1 +S 2)G2 0
T + (1 +S 2)σ2 KM ( MKL 2(1 +D 2)2∆2 σ4T 2 )2/3 ,
whereG 2 0 := 1 S ∑ s∈[S] ‖‖∇fs(x0) ‖‖2.Alternatively, ifB= Θ(KT)andβ= max
{
1
T,
(
MKL 2(1+D2) 2 ∆2
σ4T 2
)1/3}
,
then Algorithm 1 admits the convergence guarantee
E[G(xa)]≲ σ2(1 +S 2) KMT + ( L ( 1 +D 2) σ∆ KMT ) 2 3 (1 +S 2)
+ LS2∆ T + (1 +S 2)G2 0 T + (1 +S 2)σ2 KMT 2 .
Proof.With the above choice of parameters, the conditions required in Lemmas 4.3–4.5 are satisfied.
Indeed, by the definition ofγ, we have
γ≤ 1 2L, γL≤
√
βKM
54 .
Moreover, sinceηKL≤c ηβ,β≤c<1, andK≥1, by choosingc η >0sufficiently small, we obtain
ηKL≤1,
and
24e2(ηL)4K4 + 24η2L2K= 24e 2(ηKL) 4 + 24(ηKL) 2
K
1The notation≲absorbs numerical constants.
17

≤24e 2c4 η + 24c2 η≤ 1 2.
Similarly,
1152e2(1−β) 2(ηKL) 2≤1152e 2c2 ηβ2≤β 2.
SinceγL≤1/2, we also have
1152e2(1−β) 2(ηγKL 2)2 = 1152e2(1−β) 2(ηKL) 2(γL)2
≤1152e 2(1−β) 2(ηKL) 2≤β 2.
Therefore, all the conditions in Lemmas 4.3–4.5 hold.
It follows from Lemmas 4.3 and 4.4 that
Et s≤(1−β)E t−1 s + 2β 9 E[∥gt−1∥2] + 3β2σ2 KM + 4 βL2Ut s
≤(1−β)E t−1 s + 2β 9 E[∥gt−1∥2] + 3β2σ2 KM
+ 4 βL2 ( 4e2K2Ξt s + 12(ηK)2 ( 8(ηKL) 2 +K−1 )( β2σ2 + 4(γL)2E[∥gt−1∥2] ))
=(1−β)E t−1 s + 2β 9 E[∥gt−1∥2] + 3β2σ2 KM + 16(eLK)2 β Ξt s + 48β(ηKL) 2 ( 8(ηKL) 2 +K−1 ) σ2
+ 192 β (ηKL) 2 ( 8(ηKL) 2 +K−1 ) (γL)2E[∥gt−1∥2]
≤(1−β)E t−1 s + 4β2σ2 KM + 5β 18 E[∥gt−1∥2] + 16(eLK)2 β Ξt s,
where the third inequality follows from



48β(ηKL) 2( 8(ηKL) 2 +K−1) ≤ β2
KM,
192(ηKL) 2
β
(
8(ηKL) 2 +K−1) (γL)2≤ β 18.
Indeed, letq:=ηKL. The stated stepsize condition gives
q2≤c 2 η β M, q 2≤ c2 η K,8q 2 +K−1≤ 8c2 η + 1 K .
Consequently,
48βq2(8q2 +K−1)≤48c 2 η(8c2 η + 1) β2 KM ≤ β2 KM,
provided that48c 2 η(8c2 η + 1)≤1. Moreover, the definition ofγgives(γL) 2≤βKM/54, so
192q2
β (8q2 +K−1)(γL)2≤ 32 9 KMq 2(8q2 +K−1)
≤ 32 9 c2 η(8c2 η + 1)β≤ β 18,
where the last inequality holds ifc 2 η(8c2 η + 1)≤1/64. Thus, by choosing the absolute constant
cη >0sufficiently small, both required inequalities hold.
Summing overtfrom 0 toT−1and applying Lemma 4.5, we get
T−1∑
t=0
Et s≤(1−β)
T−1∑
t=0
Et−1 s + 4β2σ2 KM T+ 5β 18 T−1∑ t=0 E[∥gt−1∥2] + 16(eLK)2 β T−1∑ t=0 Ξt s
18

≤(1−β)
T−1∑
t=0
Et−1 s + 4β2σ2 KM T+ 5β 18 T−1∑ t=0 E[∥gt−1∥2]
+ 16(eLK)2
β
(
β2
288e2K2L2
T−1∑
t=0
(
Et−1 s +E[∥g t−1∥2] ) + 4η2TD 2 )
=
(
1− 17β 18 ) T−2∑ t=−1 Et s + β 3 T−1∑ t=0 E[∥gt−1∥2] + 4β2σ2 KM T+ 64 β (eηKL) 2TD 2.
Thus,
17β
18
T−2∑
t=−1
Et s≤E−1 s −E T−1 s + β 3 T−1∑ t=0 E[∥gt−1∥2] + 4β2σ2 KM T+ 64 β (eηKL) 2TD 2,
which implies that
T−2∑
t=−1
Et s≤ 18 17βE−1 s − 18 17βET−1 s + 6 17 T−1∑ t=0 E[∥gt−1∥2] + 72βσ2 17KMT+ 1152 17β2 (eηKL) 2TD 2.
Therefore,
T−1∑
t=−1
Et s≤ 18 17βE−1 s + 6 17 T−1∑ t=0 E [ ∥gt−1∥2 ] + 72βσ2 17KMT+ 1152 17β2 (eηKL) 2TD 2.(4.5)
Notice that
T−1∑
t=0
E
[
∥gt−1∥2
]
=
T−1∑
t=0
E
[
∥gt∥2
]
+E
[
∥g−1∥2
]
−E
[
∥gT−1∥2
]
.
Hence,
T−1∑
t=0
E
[
∥gt−1∥2
]
≤
T−1∑
t=0
E
[
∥gt∥2
]
+E
[
∥g−1∥2
]
.
By Lemma 4.1,
2
(
E[fs(xT )]−f s(x0) )
γ + 1 2 T−1∑ t=0 E [ ∥gt∥2 ] ≤ T−1∑ t=0 Et s≤ T−1∑ t=−1 Et s.
Combining the above inequality with (4.5), we get
1
2
T−1∑
t=0
E
[
∥gt∥2
]
≤
2
(
fs(x0)−E[f s(xT )] )
γ + 18 17βE−1 s + 6 17 T−1∑ t=0 E [ ∥gt∥2 ]
+ 6 17 E [ ∥g−1∥2 ] + 72βσ2 17KMT+ 1152 17β2 (eηKL) 2TD 2,
which implies that
T−1∑
t=0
E
[
∥gt∥2
]
≤
68
(
fs(x0)−E[f s(xT )] )
5γ + 36 5βE−1 s + 144βσ2 5KM T
+ 2304 5β2 (eηKL) 2TD 2 + 12 5 E [ ∥g−1∥2 ]
≤68∆ 5γ + 36 5βE−1 s + 144βσ2 5KM T
+ 2304 5β2 (eηKL) 2TD 2 + 12 5 E [ ∥g−1∥2 ] .(4.6)
19

Averaging (4.6) overs∈[S], we obtain
T−1∑
t=0
E
[
∥gt∥2
]
≤68∆ 5γ + 36 5βS ∑ s∈[S] E−1 s + 144βσ2 5KM T
+ 2304 5β2 (eηKL) 2TD 2 + 12 5 E [ ∥g−1∥2 ] .(4.7)
Moreover, from (4.5), we have
T−1∑
t=0
Et s≤ 18 17βE−1 s + 6 17 T−1∑ t=0 E [ ∥gt−1∥2 ] + 72βσ2 17KMT+ 1152 17β2 (eηKL) 2TD 2
≤ 18 17βE−1 s + 6 17 T−1∑ t=0 E [ ∥gt∥2 ] + 6 17 E [ ∥g−1∥2 ]
+ 72βσ2
17KMT+ 1152 17β2 (eηKL) 2TD 2.
Substituting (4.6) into the above inequality gives
T−1∑
t=0
Et s≤ 306 85βE−1 s + 24∆ 5γ + 72βσ2 5KM T+ 1152 5β2 (eηKL) 2TD 2
+ 102 85 E [ ∥g−1∥2 ] .(4.8)
Summing (4.8) overs∈[S]gives
∑
s∈[S]
T−1∑
t=0
Et s≤ 306 85β ∑ s∈[S] E−1 s + 24S∆ 5γ + 72Sβσ 2 5KM T
+ 1152S 5β2 (eηKL) 2TD 2 + 102S 85 E [ ∥g−1∥2 ] .(4.9)
Hence,
1
T
T−1∑
t=0
E


‖‖‖‖‖‖ ∑ s∈[S] λt,∗ s ∇fs(xt) ‖‖‖‖‖‖ 2 ≤ 2 T T−1∑ t=0 E   ‖‖‖‖‖‖ ∑ s∈[S] λt,∗ s ∇fs(xt)−g t ‖‖‖‖‖‖ 2  + 2 T T−1∑ t=0 E [ ∥gt∥2 ]
= 2 T T−1∑ t=0 E


‖‖‖‖‖‖ ∑ s∈[S] λt,∗ s ( ∇fs(xt)−g t s ) ‖‖‖‖‖‖ 2  + 2 T T−1∑ t=0 E [ ∥gt∥2 ]
≤ 2 T T−1∑ t=0 E  ∑ s∈[S] λt,∗ s ‖‖‖∇fs(xt)−g t s ‖‖‖ 2   + 2 T T−1∑ t=0 E [ ∥gt∥2 ]
≤ 2 T T−1∑ t=0 ∑ s∈[S] E [‖‖‖∇fs(xt)−g t s ‖‖‖ 2] + 2 T T−1∑ t=0 E [ ∥gt∥2 ]
= 2 T ∑ s∈[S] T−1∑ t=0 Et s + 2 T T−1∑ t=0 E[∥gt∥2],
where the second inequality follows from the convexity of∥·∥2. Plugging (4.7) and (4.9) into the
20

above inequality, we have
1
T
T−1∑
t=0
E


‖‖‖‖‖‖ ∑ s∈[S] λt,∗ s ∇fs(xt) ‖‖‖‖‖‖ 2 
≤ 612 85βT ∑ s∈[S] E−1 s + 48S∆ 5γT + 144Sβσ 2 5KM
+ 2304S 5β2 (eηKLD) 2 + 204S 85T E[∥g−1∥2] + 72 5βST ∑ s∈[S] E−1 s
+ 136∆ 5γT + 288βσ2 5KM + 4608 5β2 (eηKLD) 2 + 24 5T E[∥g−1∥2].
Finally, forB=
⌈
K
Tβ 2
⌉
, noticing that
g−1 s = 1 BM M∑ i=1 B∑ b=1 ∇Fs,i(x−1;ξb i ),
we have
E−1 s =E[∥∇fs(x−1)−g −1 s ∥2]
=E


‖‖‖‖‖‖ 1 BM ∑ i,b ∇fs,i(x−1)− 1 BM ∑ i,b ∇Fs,i(x−1;ξb i ) ‖‖‖‖‖‖ 2 
= 1 B2M 2 E


‖‖‖‖‖‖ ∑ i,b ( ∇fs,i(x−1)−∇F s,i(x−1;ξb i ) ) ‖‖‖‖‖‖ 2 
= 1 B2M 2 E

∑
i,b
‖‖‖∇fs,i(x−1)−∇F s,i(x−1;ξb i ) ‖‖‖ 2
+2
∑
(i,b)̸=(j,d)
⟨
∇fs,i(x−1)−∇F s,i(x−1;ξb i ),∇fs,j(x−1)−∇F s,j(x−1;ξd j ) ⟩


≤ 1 B2M 2 E

∑
i,b
σ2

 = σ2
BM ≤ β2σ2T KM .
Moreover, sinceg−1 is obtained by applying the same Pareto aggregation rule to{g−1 s }s∈[S], it holds
that
g−1 = ∑
s∈[S]
λ−1,∗ s g−1 s ,
whereλ−1,∗∈[0,1] S solves
min
λs≥0,∑
s∈[S]λs=1
‖‖‖‖‖‖ ∑ s∈[S] λsd−1 s ‖‖‖‖‖‖ 2 .
By the optimality ofλ−1,∗, choosing the uniform weightλs = 1/Sgives
E∥g−1∥2≤E


‖‖‖‖‖‖ 1 S ∑ s∈[S] g−1 s ‖‖‖‖‖‖ 2 
21

≤ 1 S ∑ s∈[S] E [ ∥g−1 s ∥2 ] .
For eachs∈[S], we have
E
[
∥g−1 s ∥2
]
=E
[‖‖‖∇fs(x−1) +g−1 s −∇fs(x−1) ‖‖‖ 2]
≤2
‖‖‖∇fs(x−1) ‖‖‖ 2 + 2E [‖‖‖g−1 s −∇fs(x−1) ‖‖‖ 2]
= 2
‖‖‖∇fs(x−1) ‖‖‖ 2 + 2E−1 s .
Sincex−1 =x 0, let
G2 0 := 1 S ∑ s∈[S] ‖‖‖∇fs(x0) ‖‖‖ 2 .
Then
E∥g−1∥2≤2G 2 0 + 2 S ∑ s∈[S] E−1 s ≤2G 2 0 + 2β2σ2T KM .
Thus,
1
T
T−1∑
t=0
E


‖‖‖‖‖‖ ∑ s∈[S] λt,∗ s ∇fs(xt) ‖‖‖‖‖‖ 2  ≲ 1 βT ∑ s∈[S] E−1 s + S∆ γT + Sβσ 2 KM + S β2 (ηKLD) 2
+ 1 βTS ∑ s∈[S] E−1 s + ∆ γT + βσ2 KM + 1 β2 (ηKLD) 2
+ 1 +S T E[∥g−1∥2]
≲βσ2
KM (1 +S) + (ηKL) 2 β2 D2(1 +S) + S∆ γT
+ (1 +S)G 2 0
T + (1 +S)β 2σ2 KM .(4.10)
By the choice ofη,
(ηKL) 2
β2 ≲ L∆ β1/2(KM) 1/2T.
Moreover,
1
γ≤2L+
√
54 L√βKM ,
which implies that
S∆
γT ≲ LS∆ T + LS∆ β1/2(KM) 1/2T.
Therefore, from (4.10), we have
1
T
T−1∑
t=0
E


‖‖‖‖‖‖ ∑ s∈[S] λt,∗ s ∇fs(xt) ‖‖‖‖‖‖ 2  ≲ βσ2 KM (1+S)+ L(1 +D 2)∆ β1/2(KM) 1/2T (1+S)+LS∆ T +(1 +S)G 2 0 T +(1 +S)β 2σ2 KM .
Taking
β=
(
MKL 2(1 +D 2)2∆2
σ4T 2
)1/3
22

gives
1
T
T−1∑
t=0
E


‖‖‖‖‖‖ ∑ s∈[S] λt,∗ s ∇fs(xt) ‖‖‖‖‖‖ 2 
≲
(
L(1 +D 2)σ∆
KMT
)2/3
(1 +S) + LS∆ T + (1 +S)G 2 0 T
+ (1 +S)σ 2
KM
(
MKL 2(1 +D 2)2∆2
σ4T 2
)2/3
.
Sinceλ t,∗∈C, by the definition ofG(xt),
G(xt) = min
λ∈C
‖‖‖‖‖‖ ∑ s∈[S] λs∇fs(xt) ‖‖‖‖‖‖ 2 ≤ ‖‖‖‖‖‖ ∑ s∈[S] λt,∗ s ∇fs(xt) ‖‖‖‖‖‖ 2 .
Taking expectations and averaging overt= 0,...,T−1, we obtain
1
T
T−1∑
t=0
E
[
G(xt) ] ≤ 1 T T−1∑ t=0 E


‖‖‖‖‖‖ ∑ s∈[S] λt,∗ s ∇fs(xt) ‖‖‖‖‖‖ 2 .
Sinceais chosen uniformly at random from{0,1,...,T−1},
E[G(xa)] = 1 T T−1∑ t=0 E [ G(xt) ]
≤ 1 T T−1∑ t=0 E


‖‖‖‖‖‖ ∑ s∈[S] λt,∗ s ∇fs(xt) ‖‖‖‖‖‖ 2 
≲
(
L(1 +D 2)σ∆
KMT
) 2
3
(1 +S) + LS∆ T + (1 +S)G 2 0 T
+ (1 +S)σ 2
KM
(
MKL 2(1 +D 2)2∆2
σ4T 2
) 2
3
.
Similarly, ifB= Θ(KT), then
E−1 s ≤ σ2 BM ≲ σ2 KMT .
Moreover, by the same argument as above,
E∥d−1∥2 ≲G 2 0 + σ2 KMT .
Using the preceding estimate, we have
1
T
T−1∑
t=0
E


‖‖‖‖‖‖ ∑ s∈[S] λt,∗ s ∇fs(xt) ‖‖‖‖‖‖ 2 
≲ σ2
KMβT 2 (1 +S) + βσ2 KM (1 +S) + (ηKL) 2 β2 D2(1 +S)
+ S∆ γT + (1 +S)G 2 0 T + (1 +S)σ 2 KMT 2 .
23

By the choice ofη,
(ηKL) 2
β2 ≲ L∆ β1/2(KM) 1/2T.
Moreover, since
γ= min



1
2L, 1 L
√
βKM
54


,
it follows that
1
γ≤2L+
√
54 L√βKM .
Thus,
S∆
γT ≲ LS∆ T + LS∆ β1/2(KM) 1/2T.
Combining the above estimates gives
1
T
T−1∑
t=0
E


‖‖‖‖‖‖ ∑ s∈[S] λt,∗ s ∇fs(xt) ‖‖‖‖‖‖ 2  ≲ σ2 KMβT 2 (1 +S) + βσ2 KM (1 +S)
+ L(1 +D 2)∆ β1/2(KM) 1/2T (1 +S) + LS∆ T + (1 +S)G 2 0 T .
Now take
β= max



1
T,
(
MKL 2(1 +D 2)2∆2
σ4T 2
)1/3 
.
Sinceβ≥1/T, we have
σ2
KMβT 2≤ σ2 KMT .
Furthermore, by the definition ofβ,
βσ2
KM + L(1 +D 2)∆ β1/2(KM) 1/2T ≲ σ2 KMT + ( L(1 +D 2)σ∆ KMT )2/3 .
Therefore,
1
T
T−1∑
t=0
E


‖‖‖‖‖‖ ∑ s∈[S] λt,∗ s ∇fs(xt) ‖‖‖‖‖‖ 2  ≲ σ2(1 +S) KMT + ( L(1 +D 2)σ∆ KMT )2/3 (1 +S)
+ LS∆ T + (1 +S)G 2 0 T + (1 +S)σ 2 KMT 2 ,
which implies that
E[G(xa)]≲ σ2(1 +S) KMT + ( L(1 +D 2)σ∆ KMT )2/3 (1 +S)
+ LS∆ T + (1 +S)G 2 0 T + (1 +S)σ 2 KMT 2 .
The proof is complete.■
Remark4.2.Theorem4.1establishesarandom-iterateParetostationarityguaranteeforAlgorithm
1. Specifically, the algorithm returns an iteratexa, whereais chosen uniformly at random from
{0,...,T−1}, and the corresponding expected Pareto stationarity measureE[G(x a)]decreases at
a rate ofO(T−2/3). This improves upon theO(T−1/2)rate established in [32,33].
24

Corollary 4.1.Under the conditions of Theorem 4.1, FSMGDA-M-VR attains anϵ-Pareto sta-
tionary solution with communication complexity
O

max



L(1 +D 2)σ∆(1 +S) 3 2
KMϵ
3
2
,LS∆ ϵ , (1 +S)G 2 0 ϵ , (C1 ϵ ) 3 4 ,σ2(1 +S) KMϵ , ( (1 +S)σ 2 KMϵ ) 1 2     ,
where
C1 := (1 +S)σ 2 KM ( MKL 2(1 +D 2)2∆2 σ4 )2/3 .
Moreover, the corresponding sample complexity is
O

SMKmax



L(1 +D 2)σ∆(1 +S) 3 2
KMϵ
3
2
,LS∆ ϵ , (1 +S)G 2 0 ϵ , (C1 ϵ ) 3 4 ,σ2(1 +S) KMϵ , ( (1 +S)σ 2 KMϵ ) 1 2     .
Proof.For the first caseB=
⌈
K
Tβ 2
⌉
, by Theorem 4.1,
E[G(xa)]≲
(
L
(
1 +D 2) σ∆
KMT
) 2
3
(1 +S) + LS∆ T
+(1 +S)G 2 0
T + (1 +S)σ 2 KM ( MKL 2(1 +D 2)2∆2 σ4T 2 )2/3 .
To obtain anϵ-Pareto stationary solution, it is sufficient, up to absolute constant factors hidden in
≲, to require
(
L(1 +D 2)σ∆
KMT
) 2
3
(1 +S)≤ ϵ 4,
LS∆
T ≤ ϵ 4, (1 +S)G 2 0 T ≤ ϵ 4,
and
(1 +S)σ 2
KM
(
MKL 2(1 +D 2)2∆2
σ4T 2
) 2
3
≤ ϵ 4.
The first inequality yields
T≥ L(1 +D 2)σ∆ KM (4(1 +S) ϵ ) 3 2 ,
and hence
T=O
(
L(1 +D 2)σ∆(1 +S) 3 2
KMϵ
3
2
)
.
The second and third inequalities give
T=O
(LS∆
ϵ
)
, T=O
(
(1 +S)G 2 0
ϵ
)
.
For the last inequality, letC1 := (1+S)σ 2 KM (MKL 2(1+D2)2∆2 σ4 ) 2 3 . Thus, it is sufficient to require
C1
T
4
3
≤ ϵ 4,
which yields
T=O
((C1
ϵ
) 3
4
)
.
25

Therefore, for the first choice ofB=
⌈
K
Tβ 2
⌉
, it suffices to take
T=O
(
max
{
L(1 +D 2)σ∆(1 +S) 3 2
KMϵ
3
2
,LS∆ ϵ , (1 +S)G 2 0 ϵ , (C1 ϵ ) 3 4 }) .
Next, for the second caseB= Θ(KT), Theorem 4.1 gives
E[G(xa)]≲ σ2(1 +S) KMT + ( L(1 +D 2)σ∆ KMT ) 2 3 (1 +S) + LS∆ T + (1 +S)G 2 0 T + (1 +S)σ 2 KMT 2 .
To obtain anϵ-Pareto stationary solution, it is sufficient, up to absolute constant factors hidden in
≲, to require
σ2(1 +S)
KMT ≤ ϵ 5,
(
L(1 +D 2)σ∆
KMT
) 2
3
(1 +S)≤ ϵ 5,
LS∆
T ≤ ϵ 5, (1 +S)G 2 0 T ≤ ϵ 5,
and
(1 +S)σ 2
KMT 2 ≤ ϵ 5.
These inequalities respectively yield
T=O
(
σ2(1 +S)
KMϵ
)
,
T=O
(
L(1 +D 2)σ∆(1 +S) 3 2
KMϵ
3
2
)
,
T=O
(LS∆
ϵ
)
, T=O
(
(1 +S)G 2 0
ϵ
)
,
and
T=O


(
(1 +S)σ 2
KMϵ
) 1
2

.
Therefore, for the second choiceB= Θ(KT), it suffices to take
T=O

max



L(1 +D 2)σ∆(1 +S) 3 2
KMϵ
3
2
,LS∆ ϵ , (1 +S)G 2 0 ϵ ,σ2(1 +S) KMϵ , ( (1 +S)σ 2 KMϵ ) 1 2     .
We next derive the communication complexity and the sample complexity.
•Communication complexity:In FSMGDA-M-VR, each global iteration corresponds to one
round of communication between the clients and the server. Therefore, the total communication
complexity is equal to the total number of global roundsT. Combining the above two cases, the
communication complexity can be expressed as
O

max



L(1 +D 2)σ∆(1 +S) 3 2
KMϵ
3
2
,LS∆ ϵ , (1 +S)G 2 0 ϵ , (C1 ϵ ) 3 4 ,σ2(1 +S) KMϵ , ( (1 +S)σ 2 KMϵ ) 1 2     .
•Sample Complexity:Next, we estimate the total number of stochastic gradient computations.
26

At the initialization stage, the algorithm requiresSMBstochastic gradient computations. At each
local update, the algorithm computes stochastic gradients for allSobjectives, and both the current
stochastic gradient and the gradient at the previous global model are involved in the momentum
estimator. Therefore, each communication round requires2SMKstochastic gradient computations.
Hence, the total number of stochastic gradient computations is
SMB+ 2SMKT.
It remains to compare the initialization costSMBwith the training-stage cost2SMKT. We
consider the following two cases.
(1)B=
⌈
K
Tβ 2
⌉
. In this case,
SMB
2SMKT = B 2KT.
Since
B=
⌈ K
Tβ 2
⌉
≤ K Tβ 2 + 1,
we have
B
2KT ≤ 1 2T 2β2 + 1 2KT.
Recall that
β=
(
MKL 2(1 +D 2)2∆2
σ4T 2
)1/3
,
then
1
T 2β2 = σ8/3 M 2/3K2/3L4/3(1 +D 2)4/3∆4/3· 1 T 2/3→0 (T→∞).
Therefore,
SMB
2SMKT →0.
Thus, the initialization costSMBis of lower order than the training-stage cost2SMKT, and hence
SMB+ 2SMKT=O(SMKT).
(2)B= Θ(KT). In this case, we haveSMB= Θ(SMKT), and hence
SMB+ 2SMKT=O(SMKT),
which implies that the total number of stochastic gradient computations is also of orderO(SMKT).
Combining the above two cases, for either choice ofB, the total number of stochastic gradient
computations is of orderO(SMKT). Multiplying the above communication complexity bySMK,
we obtain the sample complexity
O

SMKmax



L(1 +D 2)σ∆(1 +S) 3 2
KMϵ
3
2
,LS∆ ϵ , (1 +S)G 2 0 ϵ , (C1 ϵ ) 3 4 ,σ2(1 +S) KMϵ , ( (1 +S)σ 2 KMϵ ) 1 2     ,
which completes the proof.■
Remark 4.3.Compared with FSMGDA and FedCMOO, the proposed FSMGDA-M-VR improves
the dependence on the target accuracy in terms of both communication-round complexity and the
total number of stochastic gradient computations. Specifically, to obtain anϵ-Pareto stationary
27

solution in expectation, FSMGDA-M-VR requires
T=O

max



L(1 +D 2)σ∆(1 +S) 3 2
KMϵ
3
2
,LS∆ ϵ , (1 +S)G 2 0 ϵ , (C1 ϵ ) 3 4 ,σ2(1 +S) KMϵ , ( (1 +S)σ 2 KMϵ ) 1 2     
communication rounds. Hence, for fixed problem-dependent constants and in the high-accuracy
regime where the first term dominates, its communication-round complexity is of orderO(ϵ−3/2),
improving upon theO(ϵ−2)communication-round complexity of FSMGDA and FedCMOO.
5. Numerical experiments
In this section, we evaluate Algorithm 1 on three federated multiobjective learning benchmarks. We
first describe the experimental setup in Section 5.1 and then present the results in Sections 5.2–5.5.
5.1. Datasets and implementation
We consider the following experimental settings:
1) MultiMNIST:We construct a two-objective dataset from MNIST by placing two randomly
selected digits in each image—one in the top-left corner and the other in the bottom-right cor-
ner—while preserving the original image size.
2) MNIST+FMNIST:We generate a new dataset by randomly combining one image from
MNIST and one from FashionMNIST, following a construction method similar to MultiMNIST.
3) CIFAR10+MNIST:We synthesize images by superimposing a randomly selected MNIST digit
at a fixed location onto all three channels of CIFAR10 images.
In our experiments, we employ convolutional neural networks of varying scales, with model
sizes spanning from 34.6k parameters to 1.73m parameters in the largest model, ResNet-18. All
architectures are based on a shared encoder for all the objective functions, coupled with task-specific
decoders comprising the final one or two linear layers.
Unless the number of clients is varied in Section 5.5, the main experiments use 100 clients. To
induce data heterogeneity across clients, we follow the implementation in [40] and use a Dirichlet dis-
tribution with concentration parameterα= 0.3to determine the class proportions assigned to each
client, while keeping the total number of data points equal across clients. To ensure a fair compari-
son, the same Dirichlet client partition, training/validation split, model initialization, random seeds,
and minibatch sequences are used for all methods. For the MultiMNIST and MNIST+FMNIST
datasets, we employ a LeNet-like CNN encoder [1], with two linear layers per task as decoders,
resulting in a total of 34.6k parameters. For the CIFAR10+MNIST dataset, we use a CNN encoder
adapted from [40], along with a single linear layer decoder, totaling 1.73m parameters. In terms
of training configuration, we apply the negative log-likelihood loss across all three datasets and
incorporate random image rotation for data augmentation during training. The batch size is set to
128, and unless otherwise noted, each training round comprises 10 local steps. Each experiment is
repeated with 10 different random seeds. We report the mean and standard deviation across the
runs, with the shaded regions in the figures indicating one standard deviation around the mean.
All datasets come with predefined training and test splits, which we adopt together with the
default validation splits when available. In cases where a validation split is not provided, we
randomly partition the training set into 80% for training and 20% for validation. Throughout all
experiments, constant learning rates are used without any schedule or decay. The learning rates are
28

selected by running each method under the corresponding experimental setting and choosing the
value that yields the best performance on the validation set.
For the MultiMNIST experiments, different learning-rate configurations are adopted across al-
gorithms. Specifically, FSMGDA [32] uses a global learning rate of 2 and a local learning rate of 0.1;
FedCMOO [33] employs a global learning rate of 1 and a local learning rate of 0.25; and FSMGDA-
M-VR adopts a global learning rate of 1 with a local learning rate of 0.5. For the MNIST+FMNIST
experiments, a similar configuration strategy is followed. FSMGDA uses global and local learning
rates of 2 and 0.1, respectively; FedCMOO uses 1.2 and 0.2; and FSMGDA-M-VR uses 1.2 and 0.5.
For the CIFAR10+MNIST experiments, FSMGDA and FedCMOO share the same learning-rate
settings, with a global learning rate of 1.6 and a local learning rate of 0.3, whereas FSMGDA-M-VR
uses a global learning rate of 1.6 and a local learning rate of 0.5.
5.2. Comparative analysis of algorithm performance
As shown in Figures 1 and 2, FSMGDA-M-VR demonstrates clear advantages over FedCMOO
and FSMGDA in terms test accuracy and test loss on the MultiMNIST, MNIST+FMNIST, and
CIFAR10+MNIST datasets. In terms of accuracy, FSMGDA-M-VR consistently achieves faster
convergence in the early training rounds, reaching higher performance levels more rapidly than the
other methods, particularly on the MultiMNIST and MNIST+FMNIST datasets, while matching or
slightly surpassing the final accuracy of FedCMOO. Regarding test loss, FSMGDA-M-VR exhibits a
steeper and more stable decline, indicating more efficient optimization and better robustness against
gradient fluctuations. This smoother loss reduction, coupled with its rapid accuracy improvement,
suggests that the momentum-based variance reduction mechanism effectively enhances training sta-
bility and convergence speed. Overall, FSMGDA-M-VR maintains communication efficiency while
delivering superior or comparable optimization performance relative to FedCMOO and significantly
outperforming FSMGDA in both convergence rate and stability.
0 100 200 300 400
Rounds
0.70
0.75
0.80
0.85
0.90
0.95Accuracy
MultiMNIST Mean T est Accuracy
FSMGDA-M-VR
FSMGDA
FedCMOO
0 100 200 300 400
Rounds
0.5
0.6
0.7
0.8
0.9Accuracy
MNIST_FMNIST Mean T est Accuracy
FSMGDA-M-VR
FSMGDA
FedCMOO
0 100 200 300 400
Rounds
0.4
0.5
0.6
0.7
0.8Accuracy
CIFAR10_MNIST Mean T est Accuracy
FSMGDA-M-VR
FSMGDA
FedCMOO
Figure 1: Mean test accuracy with MultiMNIST, MNIST+FMNIST and CIFAR10+MNIST
datasets.
Table 1 reports the final test accuracies of the three algorithms on the three bi-objective tasks,
reported as mean±standard deviation over 10 different random seeds. FSMGDA-M-VR performs
particularly well on MultiMNIST and CIFAR10+MNIST: it achieves the highest mean accuracy
on the first objective and ties with FedCMOO in mean accuracy on the second objective of Mul-
tiMNIST, while obtaining the highest mean accuracies on both objectives of CIFAR10+MNIST.
On MNIST+FMNIST, FSMGDA-M-VR achieves the highest mean accuracy on the first objective,
whereas FedCMOO performs better on the second objective.
29

0 100 200 300 400
Rounds
0.5
1.0
1.5
2.0
2.5Loss
MultiMNIST Mean T est Loss
FSMGDA-M-VR
FSMGDA
FedCMOO
0 100 200 300 400
Rounds
0.5
1.0
1.5
2.0
2.5Loss
MNIST_FMNIST Mean T est Loss
FSMGDA-M-VR
FSMGDA
FedCMOO
0 100 200 300 400
Rounds
0.75
1.00
1.25
1.50
1.75
2.00
2.25Loss
CIFAR10_MNIST Mean T est Loss
FSMGDA-M-VR
FSMGDA
FedCMOO
Figure 2: Mean test loss in MultiMNIST, MNIST+FMNIST and CIFAR10+MNIST datasets.
Experiment MNIST+FMNIST MultiMNIST CIFAR10+MNIST
FSMGDA 93.2±1.1 / 73.4±0.9 91.1±0.6 / 87.1±0.9 54.2±0.7 / 93.3±1.1
FedCMOO 94.9±1.0 /77.5±0.894.3±0.7 / 91.1±0.8 55.2±0.6 / 93.7±1.0
FSMGDA-M-VR96.4±0.5/ 76.0±0.494.5±0.3/91.1±0.3 57.2±0.3/96.0±0.5
Table 1: The final accuracies (%) of the first/second objectives in 2-objective settings. The bold
values indicate the best accuracy for each objective.
5.3. Comparison in terms of sample access cost
Figures 3 and 4 report the mean test accuracy and mean test loss of FSMGDA, FedCMOO, and
FSMGDA-M-VR against the cumulative number of samples accessed per client. On MultiMNIST,
FSMGDA-M-VR achieves higher test accuracy than the other two methods over most of the consid-
ered range of sample accesses and yields the lowest final test loss. On MNIST+FMNIST, FSMGDA-
M-VR generally achieves higher test accuracy over a substantial portion of the sample-access range
and exhibits lower test loss than the other two methods. On CIFAR10+MNIST, FedCMOO exhibits
faster initial accuracy improvement, while FSMGDA-M-VR catches up in later stages and attains
a comparable final accuracy; its final test loss is also close to the lowest among the three methods.
0 2 4 6 8 10 12
Samples Accessed (×104)
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9Accuracy
MultiMNIST — Mean T est Accuracy
FSMGDA-M-VR
FSMGDA
FedCMOO
0 2 4 6 8 10 12
Samples Accessed (×104)
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8Accuracy
MNIST+FMNIST — Mean T est Accuracy
FSMGDA-M-VR
FSMGDA
FedCMOO
0 2 4 6 8 10 12
Samples Accessed (×104)
0.1
0.2
0.3
0.4
0.5
0.6
0.7Accuracy
CIFAR10+MNIST — Mean T est Accuracy
FSMGDA-M-VR
FSMGDA
FedCMOO
Figure 3: Test accuracy versus cumulative samples accessed per client on the MultiMNIST,
MNIST+FMNIST, and CIFAR10+MNIST datasets.
30

0 2 4 6 8 10 12
Samples Accessed (×104)
0.5
1.0
1.5
2.0Loss
MultiMNIST — Mean T est Loss
FSMGDA-M-VR
FSMGDA
FedCMOO
0 2 4 6 8 10 12
Samples Accessed (×104)
0.50
0.75
1.00
1.25
1.50
1.75
2.00
2.25Loss
MNIST+FMNIST — Mean T est Loss
FSMGDA-M-VR
FSMGDA
FedCMOO
0 2 4 6 8 10 12
Samples Accessed (×104)
0.8
1.0
1.2
1.4
1.6
1.8
2.0
2.2
2.4Loss
CIFAR10+MNIST — Mean T est Loss
FSMGDA-M-VR
FSMGDA
FedCMOO
Figure 4: Test loss versus cumulative samples accessed per client on the MultiMNIST,
MNIST+FMNIST, and CIFAR10+MNIST datasets.
5.4. Comparing the local training performance of FSMGDA-M-VR, FSMGDA,
and FedCMOO
Figure 5 compares the average local training progress across clients in terms of loss decrease and
accuracy improvement. It can be observed that FSMGDA-M-VR demonstrates superior local opti-
mization performance compared to FSMGDA, while maintaining results comparable to FedCMOO.
Specifically, in terms of local loss reduction, FSMGDA-M-VR consistently achieves a steeper and
larger decrease in loss, especially during the early rounds, indicating that it optimizes local objec-
tives more effectively and rapidly. Regarding local accuracy improvement, FSMGDA-M-VR also
exhibits sharper gains and faster convergence in the initial training phase, with its trajectory closely
aligning with that of FedCMOO across both datasets.
Figure 5: Comparison of average local training progress (loss↓and accuracy↑) across clients
among FSMGDA, FedCMOO, and FSMGDA-M-VR.
5.5. Analysis of hyperparameter effects on convergence
1) Impact of the batch size:Figures 6 and 7 compare the performance of FSMGDA-M-VR with
different batch sizes on the MultiMNIST, MNIST+FMNIST, and CIFAR10+MNIST datasets. The
results indicate that increasing the batch size generally leads to faster convergence, higher final
test accuracy, and lower test loss, while also reducing the fluctuations of the training curves. On
31

MultiMNIST, the larger batch sizes, particularly 128 and 256, converge substantially faster than
the batch size of 16 and attain higher final accuracy and lower loss. A similar trend is observed
on MNIST+FMNIST, where the performance differences between batch sizes 128 and 256 become
relatively small in the later stages of training. On CIFAR10+MNIST, the effect of the batch size
is more pronounced: batch sizes 128 and 256 yield much faster convergence and noticeably better
final accuracy and loss than the smaller batch sizes, especially compared with the batch size of 16.
    
5RXQGV



$FFXUDF\
0XOWL01,670HDQ7 HVW$FFXUDF\
EDWFK 
EDWFK 
EDWFK 
EDWFK 
 



    
5RXQGV








$FFXUDF\
01,67B)01,670HDQ7 HVW$FFXUDF\
EDWFK 
EDWFK 
EDWFK 
EDWFK 
 



    
5RXQGV







$FFXUDF\
&,)$5B01,670HDQ7 HVW$FFXUDF\
EDWFK 
EDWFK 
EDWFK 
EDWFK 
Figure 6: Mean test accuracy of different batch sizes on MultiMNIST, MNIST+FMNIST and
CIFAR10+MNIST datasets.
    
5RXQGV



/RVV
0XOWL01,670HDQ7 HVW/RVV
EDWFK 
EDWFK 
EDWFK 
EDWFK 
    
5RXQGV







/RVV
01,67B)01,670HDQ7 HVW/RVV
EDWFK 
EDWFK 
EDWFK 
EDWFK 
    
5RXQGV






/RVV
&,)$5B01,670HDQ7 HVW/RVV
EDWFK 
EDWFK 
EDWFK 
EDWFK 
Figure 7: Mean test loss of different batch sizes on MultiMNIST, MNIST+FMNIST and
CIFAR10+MNIST datasets.
2) Impact of the number of clients:Figures 8 and 9 show how the number of clients af-
fects the performance of FSMGDA-M-VR across the MultiMNIST, MNIST+FMNIST, and CI-
FAR10+MNIST datasets. The results indicate that using more clients (e.g., 30) consistently leads
to higher final test accuracy and lower final test loss. This improvement is most noticeable on the
more heterogeneous CIFAR10+MNIST dataset, where a larger client pool better captures diverse
data, and on MultiMNIST, where correlated objectives benefit from updates aggregated across more
participants. On the relatively balanced MNIST+FMNIST tasks, increasing the number of clients
has little impact on final test accuracy and final test loss.
3) Impact of local stepsK:As shown in Figures 10 and 11, which depict the test accuracy
and loss curves, moderately increasing the number of local stepsK—typically within a low to
medium range—effectively accelerates convergence, improves final accuracy, and reduces loss. For
instance, increasing the number of local stepsKfrom 1 to 5 yields clear and consistent improvements
in both performance and training stability across all datasets. However, further increasing the
number of local stepsK, for example to 50, yields diminishing returns, with no significant additional
32

    
5RXQGV



$FFXUDF\
0XOWL01,670HDQ7 HVW$FFXUDF\
FOLHQW 
FOLHQW 
FOLHQW 
 



    
5RXQGV








$FFXUDF\
01,67B)01,670HDQ7 HVW$FFXUDF\
FOLHQW 
FOLHQW 
FOLHQW 
 


    
5RXQGV







$FFXUDF\
&,)$5B01,670HDQ7 HVW$FFXUDF\
FOLHQW 
FOLHQW 
FOLHQW 
Figure 8: Mean test accuracy of different client numbers on MultiMNIST, MNIST+FMNIST and
CIFAR10+MNIST datasets.
    
5RXQGV



/RVV
0XOWL01,670HDQ7 HVW/RVV
FOLHQW 
FOLHQW 
FOLHQW 
 


    
5RXQGV








/RVV
01,67B)01,670HDQ7 HVW/RVV
FOLHQW 
FOLHQW 
FOLHQW 
 



    
5RXQGV







/RVV
&,)$5B01,670HDQ7 HVW/RVV
FOLHQW 
FOLHQW 
FOLHQW 
Figure 9: Mean test loss of different client numbers on MultiMNIST, MNIST+FMNIST and
CIFAR10+MNIST datasets.
improvement in accuracy or reduction in loss.
    
5RXQGV



$FFXUDF\
0XOWL01,670HDQ7 HVW$FFXUDF\
. 
. 
. 
. 
. 
 



    
5RXQGV








$FFXUDF\
01,67B)01,670HDQ7 HVW$FFXUDF\
. 
. 
. 
. 
. 
 


    
5RXQGV







$FFXUDF\
&,)$5B01,670HDQ7 HVW$FFXUDF\
. 
. 
. 
. 
. 
Figure 10: Mean test accuracy for different numbers of local stepsK.
6. Conclusion
This paper addressed federated multiobjective optimization by proposing a momentum-based
variance-reduced algorithm that incorporates a momentum-driven gradient estimator into the local
updates to reduce the variance and bias of stochastic updates. Theoretically, under the stated
assumptions, the proposed algorithm achieves a convergence rate ofO(T−2/3), improving upon the
33

    
5RXQGV



/RVV
0XOWL01,670HDQ7 HVW/RVV
. 
. 
. 
. 
. 
 



    
5RXQGV








/RVV
01,67B)01,670HDQ7 HVW/RVV
. 
. 
. 
. 
. 
 



    
5RXQGV








/RVV
&,)$5B01,670HDQ7 HVW/RVV
. 
. 
. 
. 
. 
Figure 11: Mean test loss for different numbers of local stepsK.
O(T−1/2)rates of existing methods such as FSMGDA and FedCMOO. Extensive experiments on
federated multiobjective optimization benchmarks further demonstrated the practical effectiveness
and competitive performance of the proposed method.
Acknowledgements.This work was supported in part by NSFC (No. 12271067), the Natural
Science Foundation of Chongqing (No. CSTB2025NSCQ-LZX0060), the Science and Technology
Research Program of Chongqing Education Commission (No. KJQN202400760), and the Australian
Research Council (ARC DP230101749).
References
[1] O. Sener, V. Koltun, Multi-task learning as multi-objective optimization, Advances in Neural
Information Processing Systems, 31 (2018).
[2] T. C. Zhou, M. Momma, C. S. Dong, F. Yang, C. H. Guo, J. Shang, J. K. Liu, Multi-task
learning on heterogeneous graph neural network for substitute recommendation, Proceedings
of the 19th International Workshop on Mining and Learning with Graphs (MLG) (2023).
[3] D. Mahapatra, C. S. Dong, Y. T. Chen, M. Momma, Multi-label learning to rank through
multi-objectiveoptimization, Proceedingsofthe29thACMSIGKDDConferenceonKnowledge
Discovery and Data Mining, 4605–4616 (2023).
[4] M. Momma, A. Bagheri Garakani, N. Ma, Y. Sun, Multi-objective ranking via constrained
optimization, Companion Proceedings of the Web Conference 2020, 111–112 (2020).
[5] N. Mohamed Alshabibi, A.-H. Matar, M. H. Abdelati, Multi-objective mixed-integer linear
programming for dynamic fleet scheduling, multi-modal transport optimization, and risk-aware
logistics, Sustainability, 17(10): 4707 (2025).
[6] A. R. Jafarian-Moghaddam, Economical speed for optimizing the travel time and energy
consumption in train scheduling using a fuzzy multi-objective model, Urban Rail Transit, 7(3):
191–208 (2021).
[7] X.F.Yang, Y.C.Qi, Researchonoptimizationofmulti-objectiveregionalpublictransportation
scheduling, Algorithms, 14(4): 108 (2021).
[8] B. H. McMahan, E. Moore, D. Ramage, S. Hampson, B. Agüera y Arcas, Communication-
efficient learning of deep networks from decentralized data, Proceedings of the 20th Interna-
tional Conference on Artificial Intelligence and Statistics (AISTATS), 54: 1273–1282 (2017).
34

[9] P. Kairouz, H. B. McMahan, B. Avent, A. Bellet, M. Bennis, A. N. Bhagoji, K. Bonawitz, Z.
Charles, G. Cormode, R. Cummings, et al., Advances and open problems in federated learning,
Foundations and Trends in Machine Learning, 14(1–2): 1–210 (2021).
[10] S. U. Stich, S. P. Karimireddy, The error-feedback framework: Better rates for SGD with
delayed gradients and compressed communication, Journal of Machine Learning Research, 21:
1–36 (2020).
[11] H. Yu, S. Yang, S. H. Zhu, Parallel restarted SGD with faster convergence and less communi-
cation: Demystifying why model averaging works for deep learning, Proceedings of the AAAI
Conference on Artificial Intelligence, 33(01): 5693–5700 (2019).
[12] T. Li, A. K. Sahu, M. Zaheer, M. Sanjabi, A. Talwalkar, V. Smith, Federated optimization in
heterogeneous networks, Proceedings of Machine Learning and Systems, 2: 429–450 (2020).
[13] T. Li, S. Y. Hu, A. Beirami, V. Smith, Ditto: Fair and robust federated learning through per-
sonalization, Proceedings of the 38th International Conference on Machine Learning (ICML),
139: 6357–6368 (2021).
[14] C. T. Dinh, N. H. Tran, T. D. Nguyen, Personalized federated learning with Moreau envelopes,
Advances in Neural Information Processing Systems, 33: 21394–21405 (2020).
[15] Y. Mansour, M. Mohri, J. Ro, A. T. Suresh, Three approaches for personalization with appli-
cations to federated learning, arXiv preprint arXiv:2002.10619 (2020).
[16] Y. Sun, L. Shen, S. X. Chen, L. Ding, D. C. Tao, Dynamic regularized sharpness aware
minimization in federated learning: Approaching global consistency and smooth landscape,
Proceedings of the 40th International Conference on Machine Learning (ICML), 202: 32991–
33013 (2023).
[17] C. T. Dinh, T. T. Vu, N. H. Tran, M. N. Dao, H. Zhang, A new look and convergence rate
of federated multitask learning with Laplacian regularization, IEEE Transactions on Neural
Networks and Learning Systems, 35(6): 8075–8085 (2024).
[18] W. Liu, L. Chen, Y. F. Chen, W. Y. Zhang, Accelerating federated learning via momentum
gradient descent, IEEE Transactions on Parallel and Distributed Systems, 31(8): 1754–1766
(2020).
[19] Z. Y. Huo, Q. Yang, B. Gu, L. Carin, H. Huang, Faster on-device training using new federated
momentum algorithm, arXiv preprint arXiv:2002.02090 (2020).
[20] J. Xu, S. Wang, L. W. Wang, A. C.-C. Yao, FedCM: Federated learning with client-level
momentum, arXiv preprint arXiv:2106.10874 (2021).
[21] J. H. Sun, X. D. Wu, H. Huang, A. D. Zhang, On the role of server momentum in federated
learning, Proceedings of the AAAI Conference on Artificial Intelligence, 38(13): 15164–15172
(2024).
[22] S. J. Reddi, Z. Charles, M. Zaheer, Z. Garrett, K. Rush, J. Konečný, S. Kumar, H. B. McMa-
han, Adaptive federated optimization, International Conference on Learning Representations
(ICLR) (2021).
[23] S. J. Reddi, M. Zaheer, D. Sachan, S. Kale, S. Kumar, Adaptive methods for nonconvex
optimization, Advances in Neural Information Processing Systems, 31 (2018).
[24] R. Ward, X. X. Wu, L. Bottou, Adagrad stepsizes: Sharp convergence over nonconvex land-
scapes, Proceedings of the 36th International Conference on Machine Learning (ICML), 97:
6677–6686 (2019).
[25] S. P. Karimireddy, S. Kale, M. Mohri, S. Reddi, S. Stich, A. T. Suresh, SCAFFOLD: Stochastic
controlled averaging for federated learning, Proceedings of the 37th International Conference
on Machine Learning (ICML), 119: 5132–5143 (2020).
35

[26] X. F. Liang, S. H. Shen, J. C. Liu, Z. Pan, E. H. Chen, Y. F. Cheng, Variance reduced local
SGD with lower communication complexity, arXiv preprint arXiv:1912.12844 (2019).
[27] T. Murata, T. Suzuki, Bias-variance reduced local SGD for less heterogeneous federated learn-
ing, Proceedings of the 38th International Conference on Machine Learning (ICML), 139:
7872–7881 (2021).
[28] L. Gao, H. Z. Fu, L. Li, Y. W. Chen, M. Xu, C.-Z. Xu, FedDC: Federated learning with non-IID
data via local drift decoupling and correction, Proceedings of the IEEE/CVF Conference on
Computer Vision and Pattern Recognition (CVPR), 10112–10121 (2022).
[29] Z. H. Cheng, X. M. Huang, P. F. Wu, K. Yuan, Momentum benefits non-IID federated learning
simply and provably, International Conference on Learning Representations (ICLR) (2024).
[30] P.Khanduri, P.Sharma, H.B.Yang, M.Y.Hong, J.Liu, K.Rajawat, P.K.Varshney, STEM:A
stochastic two-sided momentum algorithm achieving near-optimal sample and communication
complexities for federated learning, Advances in Neural Information Processing Systems, 34:
6050–6061 (2021).
[31] S. S. Yang, F. Y. Zhao, Z. H. Zhou, L. Shi, X. B. Ren, Z. B. Xu, Review of mathematical
optimization in federated learning, CSIAM Transactions on Applied Mathematics, 6(2): 207–
249 (2025).
[32] H. B. Yang, Z. Q. Liu, J. Liu, C. S. Dong, M. Momma, Federated multi-objective learning,
Advances in Neural Information Processing Systems, 36: 39602–39625 (2023).
[33] B.Askin, P.Sharma, G.Joshi, C.Joe-Wong, Federatedcommunication-efficientmulti-objective
optimization, Proceedings of the 28th International Conference on Artificial Intelligence and
Statistics (AISTATS), 258: 4627–4635 (2025).
[34] M. Hartmann, G. Danoy, P. Bouvry, Multi-objective methods in federated learning: A survey
and taxonomy, arXiv preprint arXiv:2502.03108 (2025).
[35] H. Fernando, L. S. Chen, S. T. Lu, P.-Y. Chen, M. Liu, S. Chaudhury, K. Murugesan, G.
W. Liu, M. Wang, T. Y. Chen, Variance reduction can improve trade-off in multi-objective
learning, IEEEInternationalConferenceonAcoustics, SpeechandSignalProcessing(ICASSP),
6975–6979 (2024).
[36] S. J. Zhou, W. P. Zhang, J. Y. Jiang, W. L. Zhong, J. J. Gu, W. W. Zhu, On the convergence of
stochastic multi-objective gradient manipulation and beyond, Advances in Neural Information
Processing Systems, 35: 38103–38115 (2022).
[37] H. Fernando, H. Shen, M. Liu, S. Chaudhury, K. Murugesan, T. Y. Chen, Mitigating gradient
bias in multi-objective learning: A provably convergent approach, International Conference on
Learning Representations (ICLR) (2023).
[38] P. Y. Xiao, H. Ban, K. Y. Ji, Direction-oriented multi-objective learning: Simple and provable
stochastic algorithms, Advances in Neural Information Processing Systems, 36: 4509–4533
(2023).
[39] M. J. Xu, P. Z. Ju, J. Liu, H. B. Yang, PSMGD: Periodic stochastic multi-gradient descent
for fast multi-objective optimization, Proceedings of the AAAI Conference on Artificial Intel-
ligence, 39(20): 21770–21778 (2025).
[40] D. A. E. Acar, Y. Zhao, R. Matas, M. Mattina, P. Whatmough, V. Saligrama, Federated learn-
ing based on dynamic regularization, International Conference on Learning Representations
(ICLR) (2021).
36
