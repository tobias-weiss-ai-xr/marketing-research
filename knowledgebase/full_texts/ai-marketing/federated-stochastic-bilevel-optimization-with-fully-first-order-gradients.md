---
title: Federated stochastic bilevel optimization with fully first-order gradients
url: https://arxiv.org/abs/2609.16350
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Yihan Zhang
- Rohit Dhaipule
- Chiu C Tan
- Haibin Ling
- Hongchang Gao
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.16350
pages: 44
chars: 102488
fetched_at: '2026-11-08T13:25:13+00:00'
kb_version: 1
---

# Federated stochastic bilevel optimization with fully first-order gradients

Federated Stochastic Bilevel Optimization with Fully First-Order Gradients
Yihan Zhang1 , Rohit Dhaipule2 , Chiu C. Tan1 , Haibin Ling2 and Hongchang Gao1∗
1Temple University
2Stony Brook University
{rdhaipule, hling}@cs.stonybrook.edu, {yihan.zhang0002, chiu.tan, hongchang.gao}@temple.edu
Abstract
Federated stochastic bilevel optimization has been
actively studied in recent years due to its
widespread applications in machine learning. How-
ever, most existing federated stochastic bilevel op-
timization algorithms require the computation of
second-order Hessian and Jacobian matrices, which
leads to longer running times in practice. To ad-
dress these challenges, we propose a novel fed-
erated stochastic variance-reduced bilevel gradient
descent algorithm that relies solely on first-order
oracles. Specifically, our approach does not require
the computation of second-order Hessian and Jaco-
bian matrices, significantly reducing running time.
Furthermore, we introduce a novel learning rate
mechanism, i.e., a constant single-timescale learn-
ing rate, to coordinate the update of different vari-
ables. We also present a new strategy to establish
the convergence rate of our algorithm. Finally, the
extensive experimental results confirm the efficacy
of our proposed algorithm.
1 Introduction
In this paper, we focus on the following federated stochastic
bilevel optimization (FedSBO) problem:
min
x∈Rdx
f (x, y∗(x)) ≜ 1 N
NX
n=1
f (n)(x, y∗(x))
s.t., y∗(x) = arg min
y∈Rdy
g(x, y) ≜ 1 N
NX
n=1
g(n)(x, y) . (1)
Here, g(x, y) ≜ 1 N PN n=1 g(n)(x, y) denotes the lower-
level loss function, where g(n)(x, y) = E[g(n)(x, y; ξ(n))]
denotes the lower-level loss function on the n-th de-
vice, and f (x, y∗(x)) ≜ 1 N PN n=1 f (n)(x, y∗(x)) repre-
sents the upper-level loss function, where f (n)(x, y∗(x)) =
E[f (n)(x, y∗(x); ξ(n))] represents the upper-level loss func-
tion on the n-th device. Throughout this paper, we assume
that the upper-level loss function is nonconvex with respect
∗Corresponding author
to both variables and the lower-level loss function is strongly
convex with respect to y, which is a commonly used as-
sumption in the existing literature[Ghadimi and Wang, 2018;
Ji et al., 2021; Chen et al., 2021; Tarzanagh et al., 2022].
The stochastic bilevel optimization problem has attracted
increasing attention recently because many machine learn-
ing models belong to this class of optimization problem,
such as model-agnostic meta-learning [Finn et al. , 2017 ],
hyperparameter optimization [Ji et al. , 2021 ], neural ar-
chitecture search [Liu et al. , 2018 ], etc. To solve the
stochastic bilevel optimization problem, numerous optimiza-
tion algorithms [Ghadimi and Wang, 2018; Ji et al. , 2021;
Chen et al., 2021; Hong et al., 2020; Khanduri et al., 2021;
Yang et al., 2021; Guo and Yang, 2021; Dagr´eou et al., 2022;
Chu et al., 2024; Dagr ´eou et al., 2024] have been developed
in the single machine setting in the past few years. However,
enabling federated learning for the stochastic bilevel opti-
mization problem is much more challenging than the standard
single-level optimization problem. Specifically, as shown in
Eq. (1), the upper-level problem on each device depends on
the optimal solution y∗(x) of the global lower-level problem.
As a result, computing the stochastic hypergradient for the
upper-level loss function on each device requires the global
Jacobian and Hessian matrices, which introduce significant
challenges for local computation and global communication
in federated learning.
In recent years, numerous efforts [Gao, 2022; Tarzanagh
et al. , 2022; Li et al. , 2024; Yang et al. , 2024; Huang et
al., 2023] have been made to address the unique challenges
in FedSBO problems. For example, [Gao, 2022] developed
a local stochastic bilevel gradient descent with momentum
algorithms under the homogeneous setting, which can re-
move the dependence on global Jacobian and Hessian ma-
trices due to the homogeneous data distribution. [Tarzanagh
et al., 2022] proposed FedNEST in the heterogeneous setting.
It employs the Neumann series expansion approach in an in-
ner loop to estimate Hessian-inverse-vector product. How-
ever, this method suffers from a large communication com-
plexity because it requires to communicate every intermediate
Hessian-inverse-vector product in that inner loop. [Li et al.,
2024] proposed a single-loop algorithm to address the issue
of large communication complexity. In particular, it intro-
duces an additional gradient descent procedure to replace the
Neumann series expansion approach to estimate the Hessian
arXiv:2609.16350v1  [cs.LG]  14 Sep 2026

inverse vector product.
Nevertheless, the aforementioned federated stochastic
bilevel optimization algorithms still suffer from high com-
putation costs. Specifically, those algorithms need to com-
pute the second-order Jacobian and Hessian matrices. It is
computationally expensive, especially when the problem is
high-dimensional. In fact, to avoid computing the second-
order Jacobian and Hessian matrices, [Kwon et al. , 2023;
Shen and Chen, 2023; Kwon et al., 2024; Chen et al., 2023]
developed a fully first-order method in the single-machine
setting. Specifically, [Kwon et al., 2023] converts the bilevel
optimization problem into a single-level one, and then only
the first-order gradient is required to solve it, significantly
reducing computational costs. More specifically, [Kwon et
al., 2023] converts the lower-level optimization problem as a
constraint and then leverages the penalty approach to further
convert it to an unconstrained minimax optimization prob-
lem, which can be solved by the first-order stochastic gra-
dient descent ascent algorithm. Inspired by this, we aim to
develop an efficient federated stochastic bilevel optimization
algorithm that uses only first-order gradients to address the
aforementioned challenges. However, developing first-order
methods for the FedSBO problem in Eq. (1) presents unique
challenges, which are outlined below.
• First, existing first-order methods [Kwon et al., 2023 ]
for the single-machine setting employ the iteration-
dependent learning rate to guarantee convergence.
However, this strategy is not practical in federated learn-
ing. Specifically, from the iteration-dependent learning
rate, the participating device is able to infer the current
training stage, which could be used to attack the train-
ing procedure by attackers. Therefore, it is necessary to
develop a constant learning rate to avoid this problem
while guaranteeing convergence.
• Second, existing first-order methods [Kwon et al. ,
2023] under the single-machine setting employ a
two-timescale learning rate to guarantee convergence.
Specifically, some variables have an order-wise larger
learning rate than the others. This kind of learning
rate is difficult to tune for practical federated learning
practitioners. Thus, it is necessary to propose a single-
timescale learning rate to make it easy to tune while en-
suring convergence.
• Third, the first-order method under the single-machine
setting requires a penalty hyperparameter to guarantee
convergence. However, it is unclear how this penalty
hyperparameter affects the consensus error in federated
learning. Specifically, it is unclear whether the impact of
the penalty hyperparameter on the consensus error will
lead to a slower convergence rate. Therefore, it is neces-
sary to establish the theoretical convergence rate, reveal-
ing how the penalty hyperparameter affects the consen-
sus error and the convergence rate in federated learning.
To address the aforementioned unique challenges, we de-
velop a novel federated stochastic variance-reduced bilevel
gradient descent algorithm with fully first-order oracles.
Specifically, on the algorithm design side, we develop a novel
single-timescale constant learning rate, where we demon-
strate how this new learning rate depends on the penalty hy-
perparameter. On the theoretical analysis side, we propose
a novel strategy to establish the convergence rate of our al-
gorithm. In particular, we develop a novel potential function
for convergence analysis, where we demonstrate how to com-
bine different components together with carefully designed
coefficients. With these novel algorithmic and theoretical de-
signs, our algorithm can achieve the O( 1 N ϵ5 ) convergence rate to obtain the ϵ-accuracy solution, which indicates the lin-
ear speedup with respect to the number of devicesN. Finally,
extensive experimental results confirm the efficacy of our new
algorithm. In summary, our paper has made the following
contributions.
• We develop a novel federated stochastic variance-
reduced bilevel gradient descent algorithm, which uses
the fully first-order gradient and the single-timescale
constant learning rate. To the best of our knowledge, this
is the first time a single-timescale constant learning rate
has been shown to be applied to the first-order bilevel
optimization algorithms.
• We establish the convergence rate of our algorithm,
where we demonstrate how to use a potential function to
combine different estimation errors together with care-
fully designed coefficients. As far as we know, this is the
first work to provide convergence guarantees for first-
order federated bilevel optimization algorithms with the
single-timescale constant learning rate .
• Our extensive experimental results on various tasks con-
firm the efficacy of our algorithm, i.e., our new algorithm
is more computationally efficient than existing second-
order methods.
2 Related Works
2.1 Stochastic Bilevel Optimization
Since the upper-level loss function depends on the optimal
solution of the lower-level optimization problem, the hyper-
gradient of the upper-level loss function needs to compute
∂y ∗(x)/∂x, which brings unique challenges for optimizing
this class of optimization problems. Specifically, computing
∂y ∗(x)/∂x depends on Jacobian and Hessian inverse matri-
ces. To compute them, many efforts [Ghadimi and Wang,
2018; Ji et al., 2021; Chen et al., 2021; Hong et al., 2020;
Khanduri et al., 2021; Yanget al., 2021; Guo and Yang, 2021;
Dagr´eou et al., 2022; Chu et al., 2024; Dagr´eou et al., 2024]
have been made in the single machine setting recently. For
example, [Ghadimi and Wang, 2018] proposed using the Neu-
mann series expansion approach to approximate the Hessian-
inverse-vector product, based on which the convergence rate
of the stochastic gradient descent is established. In this di-
rection, several improved algorithms have been developed.
For example, [Ji et al., 2021] developed a mini-batch stochas-
tic gradient descent method to improve the convergence rate
with a large batch size. [Hong et al. , 2020 ] studied the
convergence rate of the stochastic gradient descent with a
two-timescale learning rate. [Chen et al., 2021] established
the convergence rate of the stochastic gradient descent with

an alternating update strategy. To further improve the con-
vergence rate, [Khanduri et al. , 2021; Yang et al. , 2021;
Guo and Yang, 2021] introduces the variance reduction tech-
niques [Cutkosky and Orabona, 2019; Fang et al. , 2018;
Nguyen et al. , 2017 ] into stochastic bilevel optimization,
whose convergence rate O(ϵ−3) can match their counterparts
for the single-level optimization problem. In addition to the
Neumann series expansion approach, there exists another ap-
proach for estimating the hypergradient. Specifically, the
Hessian-inverse-vector product is viewed as the optimal so-
lution of a quadratic optimization problem, and then an ad-
ditional gradient descent procedure is introduced to estimate
the Hessian-inverse-vector product. Based on this approach,
a couple of algorithms have been developed. For example,
[Dagr´eou et al., 2022; Chu et al., 2024; Dagr´eou et al., 2024]
combined it with variance reduction techniques, whose con-
vergence rates O(ϵ−3) can also match their counterparts for
the single-level optimization problem.
Since the aforementioned approaches need to compute the
second-order Jacobian and Hessian inverse matrices, [Kwon
et al., 2023; Shen and Chen, 2023 ] developed the fully first-
order method to address this issue. In particular, they trans-
formed the lower-level optimization problem as a constraint
and then used the penalty approach to further convert it as an
unconstrained minimax optimization problem. However, the
penalty hyperparameter significantly affects the convergence
rate. For example, [Kwon et al., 2023] shows that the stan-
dard stochastic gradient descent ascent algorithm can only
achieve the convergence rate of O(ϵ−7) and can be improved
to O(ϵ−5) with the variance reduction technique. However,
these methods do not require computation of the second-order
Jacobian and Hessian inverse matrices. As a result, their prac-
tical performance is more efficient in terms of running time,
especially when the problem is high-dimensional.
2.2 Federated Stochastic Bilevel Optimization
To enable distributed optimization for stochastic bilevel
optimization problems, numerous algorithms [Gao, 2022;
Tarzanagh et al. , 2022; Li et al. , 2024; Yang et al. , 2024;
Huang et al., 2023; Gao et al., 2023; ?] have recently been
developed. For example, based on the Neumann series ex-
pansion approach, [Gao, 2022 ] developed local stochastic
bilevel gradient descent with momentum algorithms under
the homogeneous setting, which only need to communicate
two variables and their gradient estimators. Its communi-
cation complexity O(ϵ−1) can match its counterpart for the
single machine setting. [Tarzanagh et al. , 2022 ] proposed
FedNEST for the heterogeneous setting, where every inter-
mediate Hessian-inverse-vector product in the the Neumann
series expansion approach should be communicated, lead-
ing to a large communication complexity. Later, [Huang et
al., 2023] developed the FedMBO algorithm, which does not
need to communicate the intermediate Hessian-inverse-vector
product. However, the upper-level variable in FedMBO needs
to be communicated in every iteration, which also leads to
a large communication complexity. Based on the other ap-
proach for estimating Hessian-inverse-vector product, [Li et
al., 2024] developed a federated stochastic bilevel optimiza-
tion algorithm with the variance reduction technique, whose
communication complexity can match that of its counterpart
for the single-level problem. However, all these existing algo-
rithms need to compute the second-order Jacobian and Hes-
sian matrices, which is computationally expensive for high-
dimensional problems. As far as we know, there do not exist
first-order federated bilevel optimization algorithms.
3 Algorithm Design
3.1 Problem Definition
According to [Kwon et al., 2023], Eq. (1) can be converted to
a constrained optimization problem as follows:
min
x∈Rdx ,y∈Rdy
f (x, y) ,
s.t. g (x, y) − g(x, y∗(x)) ≤ 0 . (2)
Then, by leveraging the penalty approach, this constrained
optimization problem can be converted to an unconstrained
minimax optimization problem as follows:
min
x∈Rdx ,y∈Rdy
max
z∈Rdy
f (x, y) + λ(g(x, y) − g(x, z))| {z }
Lλ(x,y,z)
, (3)
where λ >0 is the penalty hyperparameter. Denoting
L(x) = f (x, y∗(x)) ,
L∗ λ(x) = f (x, y∗ λ(x)) + λ(g(x, y∗ λ(x)) − g(x, y∗(x))) ,
where y∗ λ(x) = arg min y∈Rdy f (x, y) + λ(g(x, y) −
g(x, y∗(x))), existing works [Kwon et al., 2023] have shown
that L∗ λ(x) is a good approximation to L(x) when given an
appropriate penalty hyperparameter λ.
Based on this reformulation, we can solve Eq. (1) by opti-
mizing the following minimax problem:
min
x,y
max
z
1
N
NX
n=1

f (n)(x, y) + λ(g(n)(x, y) − g(n)(x, z)) 
| {z }
L(n) λ (x,y,z)
.
(4)
Obviously, the gradients ∇xL(n) λ (x, y, z), ∇yL(n) λ (x, y, z),
and ∇zL(n) λ (x, y, z) on the n-th device do not depend on the second-order Jacobian and Hessian matrices. Thus, Eq. (4)
can be solved efficiently.
3.2 Our Algorithm
To solve Eq. (4), we develop a novel federated stochas-
tic variance-reduced bilevel gradient descent algorithm with
fully first-order oracles (FedSVRBGD-FO) in Algorithm 1.
Specifically, in the t-th iteration, device n computes the
stochastic variance-reduced gradient for each component of
∇xL(n) λ (x, y, z) as follows:
u(n) 1,t = (1 − βxη2)(u(n) 1,t−1 − ∇1f (n)(x(n) t−1, y(n) t−1; ξ(n) t ))
+ ∇1f (n)(x(n) t , y(n) t ; ξ(n) t ) ,
u(n) 2,t = (1 − βxη2)(u(n) 2,t − ∇1g(n)(x(n) t−1, y(n) t−1; ξ(n) t ))
+ ∇1g(n)(x(n) t , y(n) t ; ξ(n) t ) ,

Algorithm 1 FedSVRBGD-FO
Input: x0, y0, z0, η >0, αx > 0, αy > 0, αz > 0, βx > 0, βy > 0, βz > 0.
1: Initialization when t = 0 : compute the stochastic gradient with a mini-batch of samples where the batch size is B:
m(n) x,0 = ∇1f (n)(x(n) 0 , y(n) 0 ; ξ(n) 0 ) + λ(∇1g(n)(x(n) 0 , y(n) 0 ; ξ(n) 0 ) − ∇1g(n)(x(n) 0 , z(n) 0 ; ξ(n) 0 )) ,
m(n) y,0 = ∇2f (n)(x(n) 0 , y(n) 0 ; ξ(n) 0 ) + λ∇2g(n)(x(n) 0 , y(n) 0 ; ξ(n) 0 ) , m(n) z,0 = λ∇2g(n)(x(n) 0 , z(n) 0 ; ξ(n) 0 ) ,
2: for t = 0, · · ·, T− 1, each device n do
3: Update x: x(n) t+1 = x(n) t − αxηm(n) x,t ,
4: Update y : y(n) t+1 = y(n) t − αyηm(n) y,t ,
5: Update z: z(n) t+1 = z(n) t − αzηm(n) z,t ,
6: Update the variance-reduced gradient m(n) x,t+1:
u(n) 1,t+1 = (1 − βxη2)(u(n) 1,t − ∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1)) + ∇1f (n)(x(n) t+1, y(n) t+1; ξ(n) t+1) ,
u(n) 2,t+1 = (1 − βxη2)(u(n) 2,t − ∇1g(n)(x(n) t , y(n) t ; ξ(n) t+1)) + ∇1g(n)(x(n) t+1, y(n) t+1; ξ(n) t+1) ,
u(n) 3,t+1 = (1 − βxη2)(u(n) 3,t − ∇1g(n)(x(n) t , z(n) t ; ξ(n) t+1)) + ∇1g(n)(x(n) t+1, z(n) t+1; ξ(n) t+1) ,
m(n) x,t+1 = u(n) 1,t+1 + λ(u(n) 2,t+1 − u(n) 3,t+1) ,
7: Update the variance-reduced gradient m(n) y,t+1:
v(n) 1,t+1 = (1 − βyη2)(v(n) 1,t − ∇2f (n)(x(n) t , y(n) t ; ξ(n) t+1)) + ∇2f (n)(x(n) t+1, y(n) t+1; ξ(n) t+1) ,
v(n) 2,t+1 = (1 − βyη2)(v(n) 2,t − ∇2g(n)(x(n) t , y(n) t ; ξ(n) t+1)) + ∇2g(n)(x(n) t+1, y(n) t+1; ξ(n) t+1) ,
m(n) y,t+1 = v(n) 1,t+1 + λv(n) 2,t+1 ,
8: Update the variance-reduced gradient m(n) z,t+1:
w(n) 1,t+1 = (1 − βzη2)(w(n) 1,t − ∇2g(n)(x(n) t , z(n) t ; ξ(n) t+1)) + ∇2g(n)(x(n) t+1, z(n) t+1; ξ(n) t+1) ,
m(n) z,t+1 = λw(n) 1,t+1 ,
9: if mod(t + 1, p) == 0 then
10: x(n) t+1 = ¯xt+1 = 1 N PN n′=1 x(n′) t+1 , y(n) t+1 = ¯yt+1 = 1 N PN n′=1 y(n′) t+1 , z(n) t+1 = ¯zt+1 = 1 N PN n′=1 z(n′) t+1 ,
u(n) 1,t+1 = ¯u1,t+1 = 1 N PN n′=1 u(n′) 1,t+1 , u(n) 2,t+1 = ¯u2,t+1 = 1 N PN n′=1 u(n′) 2,t+1 , u(n) 3,t+1 = ¯u3,t+1 = 1 N PN n′=1 u(n′) 3,t+1 ,
v(n) 1,t+1 = ¯v1,t+1 = 1 N PN n′=1 v(n′) 1,t+1 , v(n) 2,t+1 = ¯v2,t+1 = 1 N PN n′=1 v(n′) 2,t+1 , w(n) 1,t+1 = ¯w1,t+1 = 1 N PN n′=1 w(n′) 1,t+1 ,
11: end if
12: end for
u(n) 3,t = (1 − βxη2)(u(n) 3,t − ∇1g(n)(x(n) t−1, z(n) t−1; ξ(n) t ))
+ ∇1g(n)(x(n) t , z(n) t ; ξ(n) t ) , (5)
where η > 0 is the learning rate and βx > 0 is a constant
hyperparameter, which satisfies βxη2 < 1. Then, our algo-
rithm composes the variance-reduced gradient estimator for
∇xL(n) λ (x, y, z) as follows:
m(n) x,t = u(n) 1,t + λ(u(n) 2,t − u(n) 3,t ) . (6)
This gradient estimator is then used to update the local vari-
able as follows:
x(n) t+1 = x(n) t − αxηm(n) x,t , (7)
where αx > 0 is a constant hyperparameter. Then, at every p
iterations, where p >1, the local variable x(n) t+1 and gradient
estimators u(n) 1,t+1, u(n) 2,t+1, u(n) 3,t+1 are uploaded to the central
server and then reset to the global ones, which is shown in
Step 9 in Algorithm 1. The other two variables are updated in
the same way.
It is worth noting that the learning rate η and the associ-
ated hyperparameters αx, αy, αz in our Algorithm 1 are con-
stant, rather than iteration-dependent as existing methods in
the single-machine setting.
4 Convergence Analysis
4.1 Assumption
To establish the convergence rate of our Algorithm 1, we in-
troduce the following assumptions that are commonly used in
existing work [Kwon et al., 2023; Chen et al., 2023].
Assumption 4.1. For n ∈ {1, · · ·, N}, the upper-level func-
tion f (n)(·, ·) is Lf -smooth in expectation where Lf > 0 is
a constant, and it is Cf -Lipschitz with respect to the second
variable in expectation.
Assumption 4.2. For n ∈ {1, · · ·, N}, the lower-level func-
tion g(n)(·, ·) is Lg,1-smooth in expectation where Lg,1 > 0
is a constant and ∇2g(·, ·) is Lg,2-Lipschitz in expectation
where Lg,2 > 0 is a constant.
Assumption 4.3. For n ∈ {1, · · ·, N}, the lower-level func-
tion g(n)(·, ·) is µ-strongly-convex with respect to the second
variable.

Based on Assumptions 4.1-4.3, [Kwon et al., 2023] shows
that Lλ(x, y, z) is λµ 2 -strongly-convex in y when λ >2Lf µ .
Assumption 4.4. The stochastic gradients of the loss func-
tions at the upper and lower levels have an upper bounded
variance σ2 where σ >0 is a constant.
Assumption 4.5. The data distribution between workers is
heterogeneous and the upper-level and lower-level gradients
satisfy the following conditions:
1
N
NX
n=1
∥∇f (n)(x, y) − 1 N
NX
n′=1
∇f (n′)(x, y)∥2 ≤ δ2 ,
1
N
NX
n=1
∥∇g(n)(x, y) − 1 N
NX
n′=1
∇g(n′)(x, y)∥2 ≤ δ2 , (8)
where δ >0 is a constant, x ∈ Rdx, and y ∈ Rdy.
Following [Chen et al., 2023], we introduce the following
definition.
Definition 4.6. Given Assumptions 4.1-4.3, we denote ℓ =
max{Cf , Lf , Lg,1, Lg,2} and κ = ℓ/µ.
With the aforementioned assumptions and definitions, the
following lemma shows how well L∗ λ(x) approximates L(x).
Lemma 4.7. [Chen et al., 2023; Kwon et al., 2023 ] Given
Assumptions 4.1-4.3, by settingλ >2Lf µ , then L∗ λ(x) satisfies
the following conditions:
• ∇L∗ λ(x) is L-Lipschitz, where L = O(ℓκ3);
• ∥∇L∗ λ(x) − ∇L(x)∥ = O(ℓκ3/λ) for any x ∈ Rdx;
• |L∗ λ(x) − L(x)| = O(ℓκ2/λ) for any x ∈ Rdx.
4.2 Convergence Rate
Based on Assumptions 4.1-4.5, we established the conver-
gence rate of our algorithm below, whose proof can be found
in Appendix A.2.
Theorem 4.8. Given Assumptions 4.1-4.5, by setting λ =
O

κ3
ϵ

, βx = O
 1
N

, βy = O
 1
N

, βz = O
 1
N

, αx =
O
 1
λκ3

, αy = O
 1
λκ

, αz = O
 1
λκ

, η = O

N ϵ2
κ4

, p =
O
 κ
N ϵ

, B = O

κ6
N ϵ3

, and T = O

κ10
N ϵ5

, Algorithm 1
can achieve the ϵ-accuracy solution as follows:
1
T
T −1X
t=0
E[∥∇L(¯xt)∥2] ≤ O  ϵ2 . (9)
Remark 4.9. The complexity of the iteration T = O

κ10
N ϵ5

indicates that our algorithm can achieve a linear speedup with
respect to the number of devicesN. To the best of our knowl-
edge, this is the first time that the first-order algorithm can
achieve the linear speedup for federated bilevel optimization
problems. Moreover, when N = 1, i.e., the single-machine
setting, our convergence rate can match that of the single-
machine counterpart in [Kwon et al., 2023]. Furthermore, the
communication complexity of Algorithm 1 is T p = O  κ9 ϵ4  .
Remark 4.10. The existing method [Kwon et al., 2023] under
the single-machine setting employs a time-dependent learn-
ing rate. For example, the learning rate in the t-th iteration
for x is of the order of O(t−3/5). On the contrary, our Algo-
rithm 1 employs a constant learning rateη that is independent
of the current iteration. Moreover, [Kwon et al., 2023] em-
ploys a two-timescale learning rate. Specifically, the learning
rate for x is O(t−3/5), while that for z is O(t−2/5). Then,
limt→∞ t−3/5/t−2/5 = 0 . In contrast, the learning rate for
three variables in Algorithm 1, i.e., αxη, αyη, and αzη, are
in the same timescale 1. Therefore, our learning rate setting
is easier to tune in practice.
4.3 Proof Sketch
To establish the convergence of Algorithm 1, we develop a
novel potential function as follows:
Pt = E[L∗ λ(¯xt)] + c1λE[∥¯yt − y∗ λ(¯xt)∥2] + c2λE[∥¯zt − y∗(¯xt)∥2]
+ c3E[∥ 1 N
NX
n=1
∇1f (n)(x(n) t , y(n) t ) − 1 N
NX
n=1
u(n) 1,t ∥2]
+ c4λ2E[∥ 1 N
NX
n=1
∇1g(n)(x(n) t , y(n) t ) − 1 N
NX
n=1
u(n) 2,t ∥2]
+ c5λ2E[∥ 1 N
NX
n=1
∇1g(n)(x(n) t , z(n) t ) − 1 N
NX
n=1
u(n) 3,t ∥2]
+ c6E[∥ 1 N
NX
n=1
∇2f (n)(x(n) t , y(n) t ) − 1 N
NX
n=1
v(n) 1,t ∥2]
+ c7λ2E[∥ 1 N
NX
n=1
∇2g(n)(x(n) t , y(n) t ) − 1 N
NX
n=1
v(n) 2,t ∥2]
+ c8λ2E[∥ 1 N
NX
n=1
∇2g(n)(x(n) t , z(n) t ) − 1 N
NX
n=1
w(n) 1,t ∥2] ,
(10)
where {ci}8 i=1 are positive coefficients.
A key design in our potential function is that c1 and c2 are
associated with λ while c4, c5, c7, and c8 are associated with
λ2. As such, all coefficients {ci}8 i=1 are independent of the
penalty parameter λ. Otherwise, {ci}8 i=1 will depend on
λ, which will further affect the variance term and then re-
sult in a worse convergence rate. For example, as shown in
Eq. (68), the coefficient {ci}8 i=3 affects the terms regarding
the variance in the last line. If they depended on the penalty
parameter, the learning rate η has to be much smaller to con-
trol the variance term. For example, when c4 = O(λ2), η
should be as small as O(ϵ6) because of λ = O( 1 ϵ ), leading to a much slower convergence rate.
Based on this potential function, we first establish the up-
per bound for each term of this potential function in the Ap-
pendix A.1 and then identify the coefficient {ci}8 i=1 in Ap-
pendix A.2 to eliminate all their associated terms in the upper
bound of Pt+1 − Pt, resulting in Eq. (131). Then, we can
establish the convergence rate of our Algorithm 1.
1In this paper, the same timescale refers to having the same order
with respect to ϵ or the number of iterations.

0 250 500 750 1000 1250 1500 1750 2000
Time
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8Loss
FedNest
FedMBO
LocalBSGVRM
FedBiOAcc
FedSVRBGD-FO
(a) a9a
0 1000 2000 3000 4000
Time
0.5
1.0
1.5
2.0Loss
FedNest
FedMBO
LocalBSGVRM
FedBiOAcc
FedSVRBGD-FO (b) w8a
0 200 400 600 800 1000 1200
Time
0.5
1.0
1.5
2.0
2.5Loss
FedNest
FedMBO
LocalBSGVRM
FedBiOAcc
FedSVRBGD-FO (c) covtype
Figure 1: The upper-level loss function value versus the running time (seconds). Communication period p = 4.
Moreover, a key step for establishing the final convergence
rate is to bound the consensus error in the following lemma,
whose proof can be found in Appendix A.1.
Lemma 4.11. Given Assumptions 4.1-4.5, and η ≤
1
500p
√
L2 f +L2 g,1λ2 , βx ≤
L2 f +L2 g,1λ2
N , βy ≤
L2 f +L2 g,1λ2
N , βz ≤
L2 f +L2 g,1λ2
N , αx ≤ 10, αy ≤ 10, αz ≤ 10, we have
1
T
T −1X
t=0
1
N
NX
n=1

E[∥u(n) 1,t − ¯u1,t∥2] + λ2E[∥u(n) 2,t − ¯u2,t∥2]
+ λ2E[∥u(n) 3,t − ¯u3,t∥2] + E[∥v(n) 1,t − ¯v1,t∥2]
+ λ2E[∥v(n) 2,t − ¯v2,t∥2] + λ2E[∥w(n) 1,t − ¯w1,t∥2] 
≤ 576p2α2 xη2

L2 f + L2 g,1λ2
 1
T
T −1X
t=0
E[∥ ¯mx,t∥2]
+ 576p2α2 yη2

L2 f + L2 g,1λ2
 1
T
T −1X
t=0
E[∥ ¯my,t∥2]
+ 576p2α2 zη2

L2 f + L2 g,1λ2
 1
T
T −1X
t=0
E[∥ ¯mz,t∥2]
+ 576p2β2 xη4(1 + λ2)δ2 + 576p2β2 yη4(1 + λ2)δ2
+ 576p2β2 xη4(1 + λ2)σ2 + 576p2β2 yη4(1 + λ2)σ2
+ 576p2β2 z η4λ2δ2 + 576p2β2 z η4λ2σ2 . (11)
In this lemma, we reveal how the penalty hyperparameter
λ and the communication period p affect the consensus error.
With such a lemma, we can then establish the convergence
rate of our Algorithm 1.
5 Experiments
In this section, we evaluate the performance of our Algo-
rithm 1 on the commonly used benchmark task: hyperparam-
eter optimization and hyper-representation learning.
5.1 Hyperparameter Optimization
In the experiment, we apply Algorithm 1 to the following hy-
perparameter optimization problem:
min
x∈Rd
1
N
NX
n=1
1
m(n)
m(n) X
i=1
ℓ(y∗(x)T a(n) v,i , b(n) v,i )
s.t. y∗(x) = arg min
y∈Rd×c
1
N
NX
n=1
1
m(n)
m(n) X
i=1
ℓ(yT a(n) t,i , b(n) t,i )
+ 1 cd
cX
p=1
dX
q=1
exp(xq)y2 pq ,
(12)
where the lower-level problem is to learn the parameter
y ∈ Rd×c of the logistic regression model with the train-
ing set {(a(n) t,i , b(n) t,i )}m(n) i=1 , the upper-level problem learns the
the regularization coefficient x ∈ Rd with the validation set
{(a(n) v,i , b(n) v,i )}m(n) i=1 .
In this experiment, we used three benchmark datasets: a9a,
w8a, covtype, which are obtained from LIBSVM datasets 2.
Here, 10% of the samples are randomly selected as the test
set. For the remaining samples, 70% of them are randomly
selected as the training set and the others are used as the vali-
dation set. The training and validation sets are then randomly
distributed to eight workers. The batch size for each worker
is set to 10 in this experiment. To verify the performance
of our Algorithm 1, we compare it with four state-of-the-art
second-order methods: FedNEST [Tarzanagh et al., 2022 ],
FedMBO [Huang et al., 2023], LocalBSGVRM [Gao, 2022],
and FedBiOAcc [Li et al., 2024]. In our experiment, we set
the solution accuracy ϵ to 0.1. Then, according to the theo-
retical results in [Tarzanagh et al., 2022; Huang et al., 2023;
Gao, 2022; Li et al. , 2024 ], the learning rate of FedNEST
and FedMBO is set to ϵ2, while that of LocalBSGVRM and
FedBiOAcc is set to ϵ. Regarding our method, according to
Theorem 4.8, we set the learning rate η to ϵ2, the coefficient
αx = αy = αz = ϵ, and the penalty λ = 5 /ϵ. Moreover,
for all methods using the momentum-based variance reduc-
tion technique, we set the the coefficient of the momentum
to 0.1. Then, we run all experiments on a workstation with
4 NVIDIA A5000 GPU cards, each of which accommodates
two threads to simulate eight workers.
2https://www.csie.ntu.edu.tw/∼cjlin/libsvmtools/datasets/

In Figure 1, we plot the upper-level loss function value ver-
sus the running time (seconds). Specifically, to make a fair
comparison, we ran all methods to update x for 16,000 iter-
ations on all datasets. The communication period is set to 4
in this experiment. From Figure 1, we can find that our al-
gorithm requires much less time to converge than all baseline
methods. This confirms the advantage of using the fully first-
order gradient in practical applications.
0 250 500 750 1000 1250 1500 1750 2000
Time
0.68
0.70
0.72
0.74
0.76
0.78
0.80
0.82
0.84Accuracy
 FedNest
FedMBO
LocalBSGVRM
FedBiOAcc
FedSVRBGD-FO
Figure 2: The test accuracy ver-
sus the running time (seconds) for
a9a dataset. Communication pe-
riod p = 4.
In addition, in Figure 2,
we plot the accuracy in
the test set versus the
running time for the a9a
dataset. In Figure 2, we
can still find that our al-
gorithm uses much less
time to achieve almost
the same accuracy as the
baseline methods, further
confirming the efficacy of
using fully first-order gra-
dients for federated bilevel optimization.
0 5 10 15 20 25 30
Time
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8Loss
= 0.05
= 0.1
= 0.15
= 0.2
= 0.25
= 0.3
Figure 3: The upper-level loss
function value when using dif-
ferent ϵ for our method on a9a
dataset. Communication period
p = 4.
Because the learning
rate and penalty param-
eter are set according to
the accuracy of the so-
lution ϵ as suggested by
Theorem 4.8, we added
an additional experiment
to show the influence of
ϵ on the convergence rate,
which is shown in Fig-
ure 3. It can be observed
that a smaller ϵ leads to a
slower convergence rate.
The reason is that a smaller ϵ results in a smaller learning
rate as shown in Theorem 4.8, slowing the convergence.
Furthermore, to verify the impact of the communication
period on convergence performance, we performed an addi-
tional experiment with p = 16 . In Figure 4, we plot the
upper-level loss function value versus the running time in Fig-
ure 4(a) and plot the test accuracy in Figure 4(b). Note that
FedNest becomes more efficient than FedBiOAcc because it
computes the second-order Hessian and Jacobian matrices in
each communication round, rather than each iteration. Thus,
it computes second-order information less frequently when
the communication period becomes large. However, we can
still find that our algorithm needs less time to converge than
all baseline methods when the communication period is 16.
5.2 Hyper-representation Learning
To further verify the performance of our algorithm, we ap-
ply our algorithm to the hyper-representation learning task as
[Tarzanagh et al. , 2022 ]. Specifically, given a deep neural
network, the upper-level problem learns the weight of hid-
den layers, while the lower-level problem learns the weight
of the classifier. As such, the upper-level problem is noncon-
vex and the lower-level one is strongly convex when using
the cross-entropy loss function with ℓ2-norm regularization
for the classifier’s weight. In our experiment, we used a fully
0 500 1000 1500 2000
Time
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8Loss
FedNest
FedMBO
LocalBSGVRM
FedBiOAcc
FedSVRBGD-FO
(a) Loss
0 500 1000 1500 2000
Time
0.68
0.70
0.72
0.74
0.76
0.78
0.80
0.82
0.84Accuracy
 FedNest
FedMBO
LocalBSGVRM
FedBiOAcc
FedSVRBGD-FO (b) Accuracy
Figure 4: The upper-level loss function value and the test accuracy
versus the running time (seconds) for a9a dataset. Communication
period p = 16.
connected two-layer neural network. Its dimensionality of the
input, hidden, and output layer is 54, 30, and 7, respectively.
The dataset is covtype, which has seven classes. The batch
size is 100. The communication period p = 4. All the other
settings are the same as the first experiment.
In Figure 5, we plot the loss function value versus the run-
ning time (seconds) for the hyper-representation task. It can
be seen that our algorithm converges much faster than all
baseline methods in terms of running time, which further con-
firms the advantages of using the first-order gradient over the
second-order ones.
Figure 5: The upper-level loss function value versus the running
time (seconds) for the hyper-representation task.
6 Conclusions
In this paper, we develop a novel federated stochastic bilevel
optimization algorithm based on the fully first-order gradi-
ent. In particular, each work only needs to compute the
first-order stochastic variance-reduced gradient to update the
upper- and lower-level variables. This can significantly save
running time because our algorithm does not need to compute
the second-order Hessian and Jacobian matrices. Moreover,
we developed a novel single-timescale constant learning rate
to coordinate the update of different variables and presented
a novel strategy to establish the convergence rate of our al-
gorithm. The extensive experimental results confirm the effi-
cacy of our algorithm.

Acknowledgments
Y . Zhang and H. Gao were partially supported by U.S. NSF
CAREER 2339545, NSF IIS 2416607, NSF CNS 2107014.
References
[Chen et al., 2021] Tianyi Chen, Yuejiao Sun, and Wotao
Yin. Tighter analysis of alternating stochastic gradient
method for stochastic nested problems. arXiv preprint
arXiv:2106.13781, 2021.
[Chen et al., 2023] Lesi Chen, Yaohua Ma, and Jingzhao
Zhang. Near-optimal fully first-order algorithms for
finding stationary points in bilevel optimization. arXiv
preprint arXiv:2306.14853, 2023.
[Chu et al., 2024] Tianshu Chu, Dachuan Xu, Wei Yao, and
Jin Zhang. Spaba: A single-loop and probabilistic stochas-
tic bilevel algorithm achieving optimal sample complexity.
arXiv preprint arXiv:2405.18777, 2024.
[Cutkosky and Orabona, 2019] Ashok Cutkosky and
Francesco Orabona. Momentum-based variance reduction
in non-convex sgd. Advances in neural information
processing systems, 32, 2019.
[Dagr´eou et al., 2022] Mathieu Dagr ´eou, Pierre Ablin,
Samuel Vaiter, and Thomas Moreau. A framework
for bilevel optimization that enables stochastic and
global variance reduction algorithms. arXiv preprint
arXiv:2201.13409, 2022.
[Dagr´eou et al., 2024] Mathieu Dagr ´eou, Thomas Moreau,
Samuel Vaiter, and Pierre Ablin. A lower bound and
a near-optimal algorithm for bilevel empirical risk mini-
mization. In International Conference on Artificial Intelli-
gence and Statistics, pages 82–90. PMLR, 2024.
[Fang et al., 2018] Cong Fang, Chris Junchi Li, Zhouchen
Lin, and Tong Zhang. Spider: Near-optimal non-convex
optimization via stochastic path-integrated differential es-
timator. Advances in Neural Information Processing Sys-
tems, 31, 2018.
[Finn et al., 2017] Chelsea Finn, Pieter Abbeel, and Sergey
Levine. Model-agnostic meta-learning for fast adaptation
of deep networks. In International conference on machine
learning, pages 1126–1135. PMLR, 2017.
[Gao et al., 2023] Hongchang Gao, Bin Gu, and My T Thai.
On the convergence of distributed stochastic bilevel op-
timization algorithms over a network. In International
Conference on Artificial Intelligence and Statistics , pages
9238–9281. PMLR, 2023.
[Gao, 2022] Hongchang Gao. On the convergence
of momentum-based algorithms for federated stochas-
tic bilevel optimization problems. arXiv preprint
arXiv:2204.13299, 2022.
[Ghadimi and Wang, 2018] Saeed Ghadimi and Mengdi
Wang. Approximation methods for bilevel programming.
arXiv preprint arXiv:1802.02246, 2018.
[Guo and Yang, 2021] Zhishuai Guo and Tianbao Yang.
Randomized stochastic variance-reduced methods for
stochastic bilevel optimization. arXiv e-prints , pages
arXiv–2105, 2021.
[Hong et al., 2020] Mingyi Hong, Hoi-To Wai, Zhaoran
Wang, and Zhuoran Yang. A two-timescale framework for
bilevel optimization: Complexity analysis and application
to actor-critic. arXiv preprint arXiv:2007.05170, 2020.
[Huang et al., 2020] Feihu Huang, Shangqian Gao, Jian Pei,
and Heng Huang. Accelerated zeroth-order momentum
methods from mini to minimax optimization. arXiv e-
prints, pages arXiv–2008, 2020.
[Huang et al., 2023] Minhui Huang, Dewei Zhang, and
Kaiyi Ji. Achieving linear speedup in non-iid federated
bilevel learning. arXiv preprint arXiv:2302.05412, 2023.
[Ji et al., 2021] Kaiyi Ji, Junjie Yang, and Yingbin Liang.
Bilevel optimization: Convergence analysis and enhanced
design. In International Conference on Machine Learning,
pages 4882–4892. PMLR, 2021.
[Khanduri et al., 2021] Prashant Khanduri, Siliang Zeng,
Mingyi Hong, Hoi-To Wai, Zhaoran Wang, and Zhuoran
Yang. A near-optimal algorithm for stochastic bilevel op-
timization via double-momentum. Advances in Neural In-
formation Processing Systems, 34, 2021.
[Kwon et al., 2023] Jeongyeol Kwon, Dohyun Kwon,
Stephen Wright, and Robert D Nowak. A fully first-
order method for stochastic bilevel optimization. In
International Conference on Machine Learning , pages
18083–18113. PMLR, 2023.
[Kwon et al., 2024] Jeongyeol Kwon, Dohyun Kwon, and
Hanbaek Lyu. On the complexity of first-order meth-
ods in stochastic bilevel optimization. arXiv preprint
arXiv:2402.07101, 2024.
[Li et al., 2024] Junyi Li, Feihu Huang, and Heng Huang.
Communication-efficient federated bilevel optimization
with global and local lower level problems. Advances in
Neural Information Processing Systems, 36, 2024.
[Liu et al., 2018] Hanxiao Liu, Karen Simonyan, and Yim-
ing Yang. Darts: Differentiable architecture search. arXiv
preprint arXiv:1806.09055, 2018.
[Nguyen et al., 2017] Lam M Nguyen, Jie Liu, Katya
Scheinberg, and Martin Tak´aˇc. Sarah: A novel method for
machine learning problems using stochastic recursive gra-
dient. In International Conference on Machine Learning,
pages 2613–2621. PMLR, 2017.
[Shen and Chen, 2023] Han Shen and Tianyi Chen. On
penalty-based bilevel gradient descent method. In Inter-
national Conference on Machine Learning, pages 30992–
31015. PMLR, 2023.
[Tarzanagh et al., 2022] Davoud Ataee Tarzanagh,
Mingchen Li, Christos Thrampoulidis, and Samet
Oymak. Fednest: Federated bilevel, minimax, and
compositional optimization. In International Conference
on Machine Learning, pages 21146–21179. PMLR, 2022.
[Yang et al., 2021] Junjie Yang, Kaiyi Ji, and Yingbin Liang.
Provably faster algorithms for bilevel optimization. Ad-

vances in Neural Information Processing Systems , 34,
2021.
[Yang et al., 2024] Yifan Yang, Peiyao Xiao, and Kaiyi Ji.
Simfbo: Towards simple, flexible and communication-
efficient federated bilevel learning. Advances in Neural
Information Processing Systems, 36, 2024.

A Appendix
A.1 Fundamental Lemmas
Lemma A.1. Given Assumptions 4.1-4.5, by setting η ≤ 1 2αxL, we have
E[L∗ λ(¯xt+1)] ≤ E[L∗ λ(¯xt)] − αxη 2 E[∥∇L∗ λ(¯xt)∥2] − αxη 4 E[∥ ¯mx,t∥2]
+ 9αxη 2 (L2 f + λ2L2 g,1)E[∥y∗ λ(¯xt) − ¯yt∥2] + 9αxη 2 λ2L2 g,1E[∥y∗(¯xt) − ¯zt∥2]
+ 9αxη 2 (L2 f + λ2L2 g,1 + λ2L2 g,1) 1 N
NX
n=1
E[∥x(n) t − ¯xt∥2] + 9αxη 2 (L2 f + λ2L2 g,1) 1 N
NX
n=1
E[∥y(n) t − ¯yt∥2]
+ 9αxη 2 λ2L2 g,1 1 N
NX
n=1
E[∥z(n) t − ¯zt∥2] + 9αxη 2 E[∥ 1 N
NX
n=1
∇1f (n)(x(n) t , y(n) t ) − 1 N
NX
n=1
u(n) 1,t ∥2]
+ 9αxηλ2
2 E[∥ 1 N
NX
n=1
∇1g(n)(x(n) t , y(n) t ) − 1 N
NX
n=1
u(n) 2,t ∥2]
+ 9αxηλ2
2 E[∥ 1 N
NX
n=1
∇1g(n)(x(n) t , z(n) t ) − 1 N
NX
n=1
u(n) 3,t ∥2] . (13)
Proof.
E[L∗ λ(¯xt+1)] ≤ E[L∗ λ(¯xt)] + E[⟨∇L∗ λ(¯xt), ¯xt+1 − ¯xt⟩] + L 2 E[∥¯xt+1 − ¯xt∥2]
= E[L∗ λ(¯xt)] − αxηE[⟨∇L∗ λ(¯xt), ¯mx,t⟩] + α2 xη2L 2 E[∥ ¯mx,t∥2]
= E[L∗ λ(¯xt)] − αxη 2 E[∥∇L∗ λ(¯xt)∥2] − αxη 2 E[∥ ¯mx,t∥2] + αxη 2 E[∥∇L∗ λ(¯xt) − ¯mx,t∥2] + α2 xη2L 2 E[∥ ¯mx,t∥2]
≤ E[L∗ λ(¯xt)] − αxη 2 E[∥∇L∗ λ(¯xt)∥2] − αxη 4 E[∥ ¯mx,t∥2] + αxη 2 E[∥∇L∗ λ(¯xt) − ¯mx,t∥2]
≤ E[L∗ λ(¯xt)] − αxη 2 E[∥∇L∗ λ(¯xt)∥2] − αxη 4 E[∥ ¯mx,t∥2]
+ 3αxη 2 E[∥∇L∗ λ(¯xt) − (∇1f (¯xt, ¯yt) + λ(∇1g(¯xt, ¯yt) − ∇1g(¯xt, ¯zt)))∥2]
+ 3αxη 2 E[∥(∇1f (¯xt, ¯yt) + λ(∇1g(¯xt, ¯yt) − ∇1g(¯xt, ¯zt)))
− 1 N
NX
n=1
(∇1f (n)(x(n) t , y(n) t ) + λ(∇1g(n)(x(n) t , y(n) t ) − ∇1g(n)(x(n) t , z(n) t )))∥2]
+ 3αxη 2 E[∥ 1 N
NX
n=1
(∇1f (n)(x(n) t , y(n) t ) + λ(∇1g(n)(x(n) t , y(n) t ) − ∇1g(n)(x(n) t , z(n) t ))) − 1 N
NX
n=1
m(n) x,t ∥2]
≤ E[L∗ λ(¯xt)] − αxη 2 E[∥∇L∗ λ(¯xt)∥2] − αxη 4 E[∥ ¯mx,t∥2]
+ 9αxη 2 (L2 f + λ2L2 g,1)E[∥y∗ λ(¯xt) − ¯yt∥2] + 9αxη 2 λ2L2 g,1E[∥y∗(¯xt) − ¯zt∥2]
+ 9αxη 2 (L2 f + λ2L2 g,1 + λ2L2 g,1) 1 N
NX
n=1
E[∥x(n) t − ¯xt∥2] + 9αxη 2 (L2 f + λ2L2 g,1) 1 N
NX
n=1
E[∥y(n) t − ¯yt∥2]
+ 9αxη 2 λ2L2 g,1 1 N
NX
n=1
E[∥z(n) t − ¯zt∥2] + 9αxη 2 E[∥ 1 N
NX
n=1
∇1f (n)(x(n) t , y(n) t ) − 1 N
NX
n=1
u(n) 1,t ∥2]
+ 9αxηλ2
2 E[∥ 1 N
NX
n=1
∇1g(n)(x(n) t , y(n) t ) − 1 N
NX
n=1
u(n) 2,t ∥2]

+ 9αxηλ2
2 E[∥ 1 N
NX
n=1
∇1g(n)(x(n) t , z(n) t ) − 1 N
NX
n=1
u(n) 3,t ∥2] , (14)
where the fourth step follows from η ≤ 1 2αxL, the last step follows from the following two inequalities:
E[∥∇L∗ λ(¯xt) − (∇1f (¯xt, ¯yt) + λ(∇1g(¯xt, ¯yt) − ∇1g(¯xt, ¯zt)))∥2]
= E[∥∇1f (¯xt, y∗ λ(¯xt)) + λ(∇1g(¯xt, y∗ λ(¯xt)) − ∇1g(¯xt, y∗(¯xt))) − (∇1f (¯xt, ¯yt) + λ(∇1g(¯xt, ¯yt) − ∇1g(¯xt, ¯zt)))∥2]
≤ 3(L2 f + λ2L2 g,1)E[∥y∗ λ(¯xt) − ¯yt∥2] + 3λ2L2 g,1E[∥y∗(¯xt) − ¯zt∥2] , (15)
and
E[∥∇Lλ(¯xt, ¯yt, ¯zt) − 1 N
NX
n=1
∇L(n) λ (x(n) t , y(n) t , z(n) t )∥2]
= 1 N
NX
n=1
E[∥∇1f (n)(¯xt, ¯yt) + λ(∇1g(n)(¯xt, ¯yt) − ∇1g(n)(¯xt, ¯zt))
− (∇1f (n)(x(n) t , y(n) t ) + λ(∇1g(n)(x(n) t , y(n) t ) − ∇1g(n)(x(n) t , z(n) t )))∥2]
≤ 3(L2 f + λ2L2 g,1 + λ2L2 g,1) 1 N
NX
n=1
E[∥x(n) t − ¯xt∥2] + 3(L2 f + λ2L2 g,1) 1 N
NX
n=1
E[∥y(n) t − ¯yt∥2]
+ 3λ2L2 g,1 1 N
NX
n=1
E[∥z(n) t − ¯zt∥2] . (16)
Lemma A.2. Given Assumptions 4.1-4.5, by setting αy ≤ 1 6(Lf +λLg,1), we have
E[∥¯yt+1 − y∗ λ(¯xt+1)∥2] ≤ (1 − ηαyµλ 8 )E[∥¯yt − y∗ λ(¯xt)∥2] − 3ηα2 y 4 E[∥ ¯my,t∥2] + 100ηα2 x(Lf + λLg,1)2 3αyλ3µ3 E[∥ ¯mx,t∥2]
+ 100ηαy
3λµ (L2 f + λ2L2 g,1) 1 N
NX
n=1
E[∥¯xt − x(n) t ∥2] + 100ηαy 3λµ (L2 f + λ2L2 g,1) 1 N
NX
n=1
E[∥¯yt − y(n) t ∥2]
+ 100ηαy
3λµ E[∥ 1 N
NX
n=1
∇2f (n)(x(n) t , y(n) t ) − 1 N
NX
n=1
v(n) 1,t ∥2]
+ 100ηαy
3λµ λ2E[∥ 1 N
NX
n=1
∇2g(n)(x(n) t , y(n) t ) − 1 N
NX
n=1
v(n) 2,t ∥2] . (17)
Proof. According to our algorithm, it is easy to know that the updating of y is to solve the following sub-problem:
min
y∈Rdy
Lλ(x, y) = f (x, y) + λg(x, y) . (18)
In terms of Assumptions 4.1-4.5,Lλ(x, y) is µy ≜ λµ 2 strongly-convex iny when λ >2Lf µ , and it isLy ≜ (Lf +λLg,1)-smooth
in y. Then, we can get
E[∥¯yt+1 − y∗ λ(¯xt+1)∥2]
≤ (1 − ηαyµy
4 )E[∥¯yt − y∗ λ(¯xt)∥2] − 3ηα2 y 4 E[∥ ¯my,t∥2] + 25ηα2 xL2 y 6αyµ3y E[∥ ¯mx,t∥2] + 25ηαy 6µy E[∥∇2Lλ(¯xt, ¯yt) − ¯my,t∥2]
≤ (1 − ηαyµy
4 )E[∥¯yt − y∗ λ(¯xt)∥2] − 3ηα2 y 4 E[∥ ¯my,t∥2] + 25ηα2 xL2 y 6αyµ3y E[∥ ¯mx,t∥2]
+ 25ηαy
3µy
E[∥∇2f (¯xt, ¯yt) + λ∇2g(¯xt, ¯yt) − 1 N
NX
n=1
(∇2f (n)(x(n) t , y(n) t ) + λ∇2g(n)(x(n) t , y(n) t ))∥2]

+ 25ηαy
3µy
E[∥ 1 N
NX
n=1
(∇2f (n)(x(n) t , y(n) t ) + λ∇2g(n)(x(n) t , y(n) t )) − 1 N
NX
n=1
m(n) y,t ∥2]
≤ (1 − ηαyµy
4 )E[∥¯yt − y∗ λ(¯xt)∥2] − 3ηα2 y 4 E[∥ ¯my,t∥2] + 25ηα2 xL2 y 6αyµ3y E[∥ ¯mx,t∥2]
+ 50ηαy
3µy
E[∥∇2f (¯xt, ¯yt) − 1 N
NX
n=1
∇2f (n)(x(n) t , y(n) t )∥2]
+ 50ηαy
3µy
λ2E[∥∇2g(¯xt, ¯yt) − 1 N
NX
n=1
∇2g(n)(x(n) t , y(n) t )∥2]
+ 50ηαy
3µy
E[∥ 1 N
NX
n=1
∇2f (n)(x(n) t , y(n) t ) − 1 N
NX
n=1
v(n) 1,t ∥2]
+ 50ηαy
3µy
λ2E[∥ 1 N
NX
n=1
∇2g(n)(x(n) t , y(n) t ) − 1 N
NX
n=1
v(n) 2,t ∥2]
≤ (1 − ηαyµy
4 )E[∥¯yt − y∗ λ(¯xt)∥2] − 3ηα2 y 4 E[∥ ¯my,t∥2] + 25ηα2 xL2 y 6αyµ3y E[∥ ¯mx,t∥2]
+ 50ηαy
3µy
(L2 f + λ2L2 g,1) 1 N
NX
n=1
E[∥¯xt − x(n) t ∥2] + 50ηαy 3µy (L2 f + λ2L2 g,1) 1 N
NX
n=1
E[∥¯yt − y(n) t ∥2]
+ 50ηαy
3µy
E[∥ 1 N
NX
n=1
∇2f (n)(x(n) t , y(n) t ) − 1 N
NX
n=1
v(n) 1,t ∥2]
+ 50ηαy
3µy
λ2E[∥ 1 N
NX
n=1
∇2g(n)(x(n) t , y(n) t ) − 1 N
NX
n=1
v(n) 2,t ∥2] , (19)
where the first step follows from [Huang et al., 2020] by setting αy ≤ 1 6Ly .
Lemma A.3. Given Assumptions 4.1-4.5, by setting αz ≤ 1 6λLg,1 , we have
E[∥¯zt+1 − y∗(¯xt+1)∥2] ≤ (1 − ηαzλµ 4 )E[∥¯zt − y∗(¯xt)∥2] − 3ηα2 z 4 E[∥ ¯mz,t∥2] + 25ηα2 xL2 g,1 6αzλµ3 E[∥ ¯mx,t∥2]
+ 25ηαz
3µ λL2 g,1 1 N
NX
n=1
E[∥¯xt − x(n) t ∥2] + 25ηαz 3µ λL2 g,1 1 N
NX
n=1
E[∥¯zt − z(n) t ∥2]
+ 25ηαz
3µ λE[∥ 1 N
NX
n=1
∇2g(n)(x(n) t , z(n) t ) − 1 N
NX
n=1
w(n) 1,t ∥2] . (20)
Proof. According to our algorithm, it is easy to know that the updating of z is to solve the sub-problem: minz∈Rdy gλ(x, z) ≜
λg(x, z). In terms of Assumptions 4.1-4.5, gλ(x, z) is µz ≜ λµ strongly-convex in z and Lz ≜ λLg,1-smooth in y. Then, we
can get
E[∥¯zt+1 − y∗(¯xt+1)∥2]
≤ (1 − ηαzµz
4 )E[∥¯zt − y∗(¯xt)∥2] − 3ηα2 z 4 E[∥ ¯mz,t∥2] + 25ηα2 xL2 z 6αzµ3z E[∥ ¯mx,t∥2] + 25ηαz 6µz E[∥λ∇2g(¯xt, ¯zt) − ¯mz,t∥2]
≤ (1 − ηαzµz
4 )E[∥¯zt − y∗(¯xt)∥2] − 3ηα2 z 4 E[∥ ¯mz,t∥2] + 25ηα2 xL2 z 6αzµ3z E[∥ ¯mx,t∥2]
+ 25ηαz
6µz
λ2E[∥∇2g(¯xt, ¯zt) − ¯w1,t∥2]
≤ (1 − ηαzµz
4 )E[∥¯zt − y∗(¯xt)∥2] − 3ηα2 z 4 E[∥ ¯mz,t∥2] + 25ηα2 xL2 z 6αzµ3z E[∥ ¯mx,t∥2]

+ 25ηαz
3µz
λ2E[∥∇2g(¯xt, ¯zt) − 1 N
NX
n=1
∇2g(n)(x(n) t , z(n) t )∥2]
+ 25ηαz
3µz
λ2E[∥ 1 N
NX
n=1
∇2g(n)(x(n) t , z(n) t ) − 1 N
NX
n=1
w(n) 1,t ∥2]
≤ (1 − ηαzµz
4 )E[∥¯zt − y∗(¯xt)∥2] − 3ηα2 z 4 E[∥ ¯mz,t∥2] + 25ηα2 xL2 z 6αzµ3z E[∥ ¯mx,t∥2]
+ 25ηαz
3µz
λ2L2 g,1 1 N
NX
n=1
E[∥¯xt − x(n) t ∥2] + 25ηαz 3µλ λ2L2 g,1 1 N
NX
n=1
E[∥¯zt − z(n) t ∥2]
+ 25ηαz
3µz
λ2E[∥ 1 N
NX
n=1
∇2g(n)(x(n) t , z(n) t ) − 1 N
NX
n=1
w(n) 1,t ∥2] , (21)
where the first step follows from [Huang et al., 2020] by setting αz ≤ 1 6Lz .
Lemma A.4. Given Assumptions 4.1-4.5, we have the following inequalities:
1
N
NX
n=1
E[∥x(n) t+1 − x(n) t ∥2] ≤ 6α2 xη2 1 N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2] + 6α2 xη2λ2 1 N
NX
n=1
E[∥u(n) 2,t − ¯u2,t∥2]
+ 6α2 xη2λ2 1 N
NX
n=1
E[∥u(n) 3,t − ¯u3,t∥2] + 6α2 xη2E[∥ ¯mx,t∥2] , (22)
1
N
NX
n=1
E[∥y(n) t+1 − y(n) t ∥2] ≤ 4α2 yη2 1 N
NX
n=1
E[∥v(n) 1,t − ¯v1,t∥2] + 4α2 yη2λ2 1 N
NX
n=1
E[∥v(n) 2,t − ¯v2,t∥2]
+ 4α2 yη2E[∥ ¯my,t∥2] , (23)
1
N
NX
n=1
E[∥z(n) t+1 − z(n) t ∥2] ≤ 2λ2α2 zη2 1 N
NX
n=1
E[∥w(n) 1,t − ¯w1,t∥2] + 2α2 zη2E[∥ ¯mz,t∥2] . (24)
Proof. Due to x(n) t+1 = x(n) t − αxηm(n) x,t , we have
1
N
NX
n=1
E[∥x(n) t+1 − x(n) t ∥2]
= 1 N
NX
n=1
E[∥αxηm(n) x,t ∥2]
≤ 2α2 xη2 1 N
NX
n=1
E[∥m(n) x,t − ¯mx,t∥2] + 2α2 xη2E[∥ ¯mx,t∥2]
= 2α2 xη2 1 N
NX
n=1
E[∥u(n) 1,t + λ(u(n) 2,t − u(n) 3,t ) − ¯u1,t − λ(¯u2,t − ¯u3,t)∥2] + 2α2 xη2E[∥ ¯mx,t∥2]
≤ 6α2 xη2 1 N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2] + 6α2 xη2λ2 1 N
NX
n=1
E[∥u(n) 2,t − ¯u2,t∥2] + 6α2 xη2λ2 1 N
NX
n=1
E[∥u(n) 3,t − ¯u3,t∥2]
+ 6α2 xη2E[∥ ¯mx,t∥2] . (25)
Similarly, due to y(n) t+1 = y(n) t − αyηm(n) y,t , we have
1
N
NX
n=1
E[∥y(n) t+1 − y(n) t ∥2]

= 1 N
NX
n=1
E[∥αyηm(n) y,t ∥2]
≤ 2α2 yη2 1 N
NX
n=1
E[∥m(n) y,t − ¯my,t∥2] + 2α2 yη2E[∥ ¯my,t∥2]
= 2α2 yη2 1 N
NX
n=1
E[∥v(n) 1,t + λv(n) 2,t − ¯v1,t − λ¯v2,t∥2] + 2α2 yη2E[∥ ¯my,t∥2]
≤ 4α2 yη2 1 N
NX
n=1
E[∥v(n) 1,t − ¯v1,t∥2] + 4α2 yη2λ2 1 N
NX
n=1
E[∥v(n) 2,t − ¯v2,t∥2] + 4α2 yη2E[∥ ¯my,t∥2] . (26)
Moreover, due to z(n) t+1 = z(n) t − αzηm(n) z,t , we have
1
N
NX
n=1
E[∥z(n) t+1 − z(n) t ∥2]
= 1 N
NX
n=1
E[∥αzηm(n) z,t ∥2]
≤ 2α2 zη2 1 N
NX
n=1
E[∥m(n) z,t − ¯mz,t∥2] + 2α2 zη2E[∥ ¯mz,t∥2]
= 2λ2α2 zη2 1 N
NX
n=1
E[∥w(n) 1,t − ¯w1,t∥2] + 2α2 zη2E[∥ ¯mz,t∥2] . (27)
Lemma A.5. Given Assumptions 4.1-4.5, by setting η ≤ min{ 1√βx , 1√ βy , 1√βz }, we have the following inequalities:
E[∥ 1 N
NX
n=1
∇1f (n)(x(n) t+1, y(n) t+1) − 1 N
NX
n=1
u(n) 1,t+1∥2] ≤ (1 − βxη2)E[∥ 1 N
NX
n=1
u(n) 1,t − ∇1f (n)(x(n) t , y(n) t )∥2] + 2β2 xη4σ2 1 N
+
12α2 xη2L2 f
N
1
N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2] + 12α2 xη2λ2L2 f N 1 N NX n=1 E[∥u(n) 2,t − ¯u2,t∥2] + 12α2 xη2λ2L2 f N 1 N NX n=1 E[∥u(n) 3,t − ¯u3,t∥2]
+
8α2 yη2L2 f
N
1
N
NX
n=1
E[∥v(n) 1,t − ¯v1,t∥2] + 8α2 yη2λ2L2 f N 1 N NX n=1 E[∥v(n) 2,t − ¯v2,t∥2]
+
12α2 xη2L2 f
N E[∥ ¯mx,t∥2] + 8α2 yη2L2 f N E[∥ ¯my,t∥2] , (28)
E[∥ 1 N
NX
n=1
∇1g(n)(x(n) t+1, y(n) t+1) − 1 N
NX
n=1
u(n) 2,t+1∥2] ≤ (1 − βxη2)E[∥ 1 N
NX
n=1
∇1g(n)(x(n) t , y(n) t ) − 1 N
NX
n=1
u(n) 2,t ∥2] + 2β2 xη4σ2 1 N
+ 12α2 xη2L2 g,1
N
1
N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2] + 12α2 xη2λ2L2 g,1 N 1 N NX n=1 E[∥u(n) 2,t − ¯u2,t∥2] + 12α2 xη2λ2L2 g,1 N 1 N NX n=1 E[∥u(n) 3,t − ¯u3,t∥2]
+ 8α2 yη2L2 g,1
N
1
N
NX
n=1
E[∥v(n) 1,t − ¯v1,t∥2] + 8α2 yη2λ2L2 g,1 N 1 N NX n=1 E[∥v(n) 2,t − ¯v2,t∥2]
+ 12α2 xη2L2 g,1
N E[∥ ¯mx,t∥2] + 8α2 yη2L2 g,1 N E[∥ ¯my,t∥2] , (29)
E[∥ 1 N
NX
n=1
∇1g(n)(x(n) t+1, z(n) t+1) − 1 N
NX
n=1
u(n) 3,t+1∥2] ≤ (1 − βxη2)E[∥ 1 N
NX
n=1
∇1g(n)(x(n) t , z(n) t ) − 1 N
NX
n=1
u(n) 3,t ∥2] + 2β2 xη4σ2 1 N

+ 12α2 xη2L2 g,1
N
1
N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2] + 12α2 xη2λ2L2 g,1 N 1 N NX n=1 E[∥u(n) 2,t − ¯u2,t∥2] + 12α2 xη2λ2L2 g,1 N 1 N NX n=1 E[∥u(n) 3,t − ¯u3,t∥2]
+ 4λ2α2 zη2L2 g,1
N
1
N
NX
n=1
E[∥w(n) 1,t − ¯w1,t∥2] + 12α2 xη2L2 g,1 N E[∥ ¯mx,t∥2] + 4α2 zη2L2 g,1 N E[∥ ¯mz,t∥2] , (30)
E[∥ 1 N
NX
n=1
∇2f (n)(x(n) t+1, y(n) t+1) − 1 N
NX
n=1
v(n) 1,t+1∥2] ≤ (1 − βyη2)E[∥ 1 N
NX
n=1
∇2f (n)(x(n) t , y(n) t ) − 1 N
NX
n=1
v(n) 1,t ∥2] + 2β2 yη4σ2 1 N
+
12α2 xη2L2 f
N
1
N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2] + 12α2 xη2λ2L2 f N 1 N NX n=1 E[∥u(n) 2,t − ¯u2,t∥2] + 12α2 xη2λ2L2 f N 1 N NX n=1 E[∥u(n) 3,t − ¯u3,t∥2]
+
8α2 yη2L2 f
N
1
N
NX
n=1
E[∥v(n) 1,t − ¯v1,t∥2] + 8α2 yη2λ2L2 f N 1 N NX n=1 E[∥v(n) 2,t − ¯v2,t∥2]
+
12α2 xη2L2 f
N E[∥ ¯mx,t∥2] + 8α2 yη2L2 f N E[∥ ¯my,t∥2] , (31)
E[∥ 1 N
NX
n=1
∇2g(n)(x(n) t+1, y(n) t+1) − 1 N
NX
n=1
v(n) 2,t+1∥2] ≤ (1 − βyη2)E[∥ 1 N
NX
n=1
∇2g(n)(x(n) t , y(n) t ) − 1 N
NX
n=1
v(n) 2,t ∥2] + 2β2 yη4σ2 1 N
+ 12α2 xη2L2 g,1
N
1
N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2] + 12α2 xη2λ2L2 g,1 N 1 N NX n=1 E[∥u(n) 2,t − ¯u2,t∥2] + 12α2 xη2λ2L2 g,1 N 1 N NX n=1 E[∥u(n) 3,t − ¯u3,t∥2]
+ 8α2 yη2L2 g,1
N
1
N
NX
n=1
E[∥v(n) 1,t − ¯v1,t∥2] + 8α2 yη2λ2L2 g,1 N 1 N NX n=1 E[∥v(n) 2,t − ¯v2,t∥2]
+ 12α2 xη2L2 g,1
N E[∥ ¯mx,t∥2] + 8α2 yη2L2 g,1 N E[∥ ¯my,t∥2] , (32)
E[∥ 1 N
NX
n=1
∇2g(n)(x(n) t+1, z(n) t+1) − 1 N
NX
n=1
w(n) 1,t+1∥2] ≤ (1 − βzη2)E[∥ 1 N
NX
n=1
∇2g(n)(x(n) t , z(n) t ) − 1 N
NX
n=1
w(n) 1,t ∥2] + 2β2 z η4σ2 1 N
+ 12α2 xη2L2 g,1
N
1
N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2] + 12α2 xη2λ2L2 g,1 N 1 N NX n=1 E[∥u(n) 2,t − ¯u2,t∥2] + 12α2 xη2λ2L2 g,1 N 1 N NX n=1 E[∥u(n) 3,t − ¯u3,t∥2]
+ 4λ2α2 zη2L2 g,1
N
1
N
NX
n=1
E[∥w(n) 1,t − ¯w1,t∥2] + 12α2 xη2L2 g,1 N E[∥ ¯mx,t∥2] + 4α2 zη2L2 g,1 N E[∥ ¯mz,t∥2] . (33)
Proof.
E[∥ 1 N
NX
n=1
∇1f (n)(x(n) t+1, y(n) t+1) − 1 N
NX
n=1
u(n) 1,t+1∥2]
= E[∥ 1 N
NX
n=1
((1 − βxη2)(u(n) 1,t − ∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1)) + ∇1f (n)(x(n) t+1, y(n) t+1; ξ(n) t+1)) − 1 N
NX
n=1
∇1f (n)(x(n) t+1, y(n) t+1)∥2]
= E[∥ 1 N
NX
n=1

(1 − βxη2)(u(n) 1,t − ∇1f (n)(x(n) t , y(n) t ))
+ (1 − βxη2)(∇1f (n)(x(n) t , y(n) t ) − ∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1)) + ∇1f (n)(x(n) t+1, y(n) t+1; ξ(n) t+1) 
− 1 N
NX
n=1
∇1f (n)(x(n) t+1, y(n) t+1)∥2]

= E[∥ 1 N
NX
n=1

(1 − βxη2)(u(n) 1,t − ∇1f (n)(x(n) t , y(n) t ) 
+ 1 N
NX
n=1

∇1f (n)(x(n) t , y(n) t ) − ∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1) + ∇1f (n)(x(n) t+1, y(n) t+1; ξ(n) t+1) − ∇1f (n)(x(n) t+1, y(n) t+1) 
+ 1 N
NX
n=1
βxη2(∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1) − ∇1f (n)(x(n) t , y(n) t ))∥2]
≤ E[∥ 1 N
NX
n=1
(1 − βxη2)(u(n) 1,t − ∇1f (n)(x(n) t , y(n) t )∥2]
+ 2E[∥ 1 N
NX
n=1
(∇1f (n)(x(n) t , y(n) t ) − ∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1) + ∇1f (n)(x(n) t+1, y(n) t+1; ξ(n) t+1) − ∇1f (n)(x(n) t+1, y(n) t+1))∥2]
+ 2E[∥ 1 N
NX
n=1
βxη2(∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1) − ∇1f (n)(x(n) t , y(n) t ))∥2]
≤ (1 − βxη2)2E[∥ 1 N
NX
n=1
u(n) 1,t − ∇1f (n)(x(n) t , y(n) t )∥2]
+ 2 1 N 2
NX
n=1
E[∥∇1f (n)(x(n) t+1, y(n) t+1; ξ(n) t+1) − ∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1)∥2]
+ 2β2 xη4 1 N 2
NX
n=1
E[∥∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1) − ∇1f (n)(x(n) t , y(n) t )∥2]
≤ (1 − βxη2)E[∥ 1 N
NX
n=1
u(n) 1,t − ∇1f (n)(x(n) t , y(n) t )∥2]
+ 2L2 f 1 N 2
NX
n=1
E[∥x(n) t+1 − x(n) t ∥2] + 2L2 f 1 N 2
NX
n=1
E[∥y(n) t+1 − y(n) t ∥2] + 2β2 xη4σ2 1 N
≤ (1 − βxη2)E[∥ 1 N
NX
n=1
u(n) 1,t − ∇1f (n)(x(n) t , y(n) t )∥2] + 2β2 xη4σ2 1 N
+
12α2 xη2L2 f
N
1
N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2] + 12α2 xη2λ2L2 f N 1 N NX n=1 E[∥u(n) 2,t − ¯u2,t∥2] + 12α2 xη2λ2L2 f N 1 N NX n=1 E[∥u(n) 3,t − ¯u3,t∥2]
+
8α2 yη2L2 f
N
1
N
NX
n=1
E[∥v(n) 1,t − ¯v1,t∥2] + 8α2 yη2λ2L2 f N 1 N NX n=1 E[∥v(n) 2,t − ¯v2,t∥2]
+
12α2 xη2L2 f
N E[∥ ¯mx,t∥2] + 8α2 yη2L2 f N E[∥ ¯my,t∥2] , (34)
where the first inequality follows from E[∇1f (n)(x(n) t , y(n) t ) − ∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1) + ∇1f (n)(x(n) t+1, y(n) t+1; ξ(n) t+1) −
∇1f (n)(x(n) t+1, y(n) t+1)] + βxη2(∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1) − ∇1f (n)(x(n) t , y(n) t )) = 0 , the second inequality follows from the
fact that the sampling operation on different workers is independent, and the last inequality follows from Lemma A.4.
Following the proof of Eq. (34), we can prove the other inequalities. Therefore, we omit the detailed proof to save space.
Lemma A.6. Given Assumptions 4.1-4.5, we have the following inequalities:
1
N
NX
n=1
E[∥∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1) − 1 N
NX
m=1
∇1f (m)(x(m) t , y(m) t ; ξ(m) t+1 )∥2]

≤ 18L2 f 1 N
NX
n=1
E[∥x(n) t − ¯xt∥2] + 18L2 f 1 N
NX
n=1
E[∥y(n) t − ¯yt∥2] + 9δ2 + 6σ2 , (35)
1
N
NX
n=1
E[∥∇2f (n)(x(n) t , y(n) t ; ξ(n) t+1) − 1 N
NX
m=1
∇2f (m)(x(m) t , y(m) t ; ξ(m) t+1 )∥2]
≤ 18L2 f 1 N
NX
n=1
E[∥x(n) t − ¯xt∥2] + 18L2 f 1 N
NX
n=1
E[∥y(n) t − ¯yt∥2] + 9δ2 + 6σ2 , (36)
1
N
NX
n=1
E[∥∇1g(n)(x(n) t , y(n) t ; ξ(n) t+1) − 1 N
NX
m=1
∇1g(m)(x(m) t , y(m) t ; ξ(m) t+1 )∥2]
≤ 18L2 g,1 1 N
NX
n=1
E[∥x(n) t − ¯xt∥2] + 18L2 g,1 1 N
NX
n=1
E[∥y(n) t − ¯yt∥2] + 9δ2 + 6σ2 , (37)
1
N
NX
n=1
E[∥∇2g(n)(x(n) t , y(n) t ; ξ(n) t+1) − 1 N
NX
m=1
∇2g(m)(x(m) t , y(m) t ; ξ(m) t+1 )∥2]
≤ 18L2 g,1 1 N
NX
n=1
E[∥x(n) t − ¯xt∥2] + 18L2 g,1 1 N
NX
n=1
E[∥y(n) t − ¯yt∥2] + 9δ2 + 6σ2 , (38)
1
N
NX
n=1
E[∥∇2g(n)(x(n) t , z(n) t ; ξ(n) t+1) − 1 N
NX
m=1
∇2g(m)(x(m) t , z(m) t ; ξ(m) t+1 )∥2]
≤ 18L2 g,1 1 N
NX
n=1
E[∥x(n) t − ¯xt∥2] + 18L2 g,1 1 N
NX
n=1
E[∥z(n) t − ¯zt∥2] + 9δ2 + 6σ2 . (39)
Proof.
1
N
NX
n=1
E[∥∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1) − 1 N
NX
m=1
∇1f (m)(x(m) t , y(m) t ; ξ(m) t+1 )∥2]
= 1 N
NX
n=1
E[∥∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1) − ∇1f (n)(x(n) t , y(n) t )
+ ∇1f (n)(x(n) t , y(n) t ) − 1 N
NX
m=1
∇1f (m)(x(m) t , y(m) t )
+ 1 N
NX
m=1
∇1f (m)(x(m) t , y(m) t ) − 1 N
NX
m=1
∇1f (m)(x(m) t , y(m) t ; ξ(m) t+1 )∥2]
≤ 3 1 N
NX
n=1
E[∥∇1f (n)(x(n) t , y(n) t ) − 1 N
NX
m=1
∇1f (m)(x(m) t , y(m) t )∥2] + 6σ2
= 3 1 N
NX
n=1
E[∥∇1f (n)(x(n) t , y(n) t ) − ∇1f (n)(¯xt, ¯yt)
+ ∇1f (n)(¯xt, ¯yt) − 1 N
NX
m=1
∇1f (m)(¯x(m) t , ¯y(m) t )
+ 1 N
NX
m=1
∇1f (m)(¯x(m) t , ¯y(m) t ) − 1 N
NX
m=1
∇1f (m)(x(m) t , y(m) t )∥2] + 6σ2

≤ 9 1 N
NX
n=1
E[∥∇1f (n)(x(n) t , y(n) t ) − ∇1f (n)(¯xt, ¯yt)∥2]
+ 9 1 N
NX
n=1
E[∥∇1f (n)(¯xt, ¯yt) − 1 N
NX
m=1
∇1f (m)(¯x(m) t , ¯y(m) t )∥2]
+ 9 1 N
NX
n=1
E[∥ 1 N
NX
m=1
∇1f (m)(¯x(m) t , ¯y(m) t ) − 1 N
NX
m=1
∇1f (m)(x(m) t , y(m) t )∥2]
≤ 18L2 f 1 N
NX
n=1
E[∥x(n) t − ¯xt∥2] + 18L2 f 1 N
NX
n=1
E[∥y(n) t − ¯yt∥2] + 9δ2 + 6σ2 , (40)
where the last step follows from Assumptions 4.1, 4.4, 4.5.
The other inequalities can be proved in the same way. Therefore, we omit their detailed proof.
Lemma A.7. Given Assumptions 4.1-4.5, by setting η ≤ min{ 1√βx , 1√ βy , 1√βz }, we have the following inequalities:
1
N
NX
n=1
E[∥u(n) 1,t+1 − ¯u1,t+1∥2] ≤ (1 + 1 p + 24pL2 f α2 xη2) 1 N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2] + 24pL2 f α2 xη2λ2 1 N
NX
n=1
E[∥u(n) 2,t − ¯u2,t∥2]
+ 24pL2 f α2 xη2λ2 1 N
NX
n=1
E[∥u(n) 3,t − ¯u3,t∥2] + 16pL2 f α2 yη2 1 N
NX
n=1
E[∥v(n) 1,t − ¯v1,t∥2] + 16pL2 f α2 yη2λ2 1 N
NX
n=1
E[∥v(n) 2,t − ¯v2,t∥2]
+ 72pβ2 xη4L2 f 1 N
NX
n=1
E[∥x(n) t − ¯xt∥2] + 72pβ2 xη4L2 f 1 N
NX
n=1
E[∥y(n) t − ¯yt∥2]
+ 24pL2 f α2 xη2E[∥ ¯mx,t∥2] + 16pL2 f α2 yη2E[∥ ¯my,t∥2] + 36pβ2 xη4δ2 + 24pβ2 xη4σ2 , (41)
1
N
NX
n=1
E[∥u(n) 2,t+1 − ¯u2,t+1∥2] ≤ (1 + 1 p + 24pL2 g,1α2 xη2λ2) 1 N
NX
n=1
E[∥u(n) 2,t − ¯u2,t∥2] + 24pL2 g,1α2 xη2 1 N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2]
+ 24pL2 g,1α2 xη2λ2 1 N
NX
n=1
E[∥u(n) 3,t − ¯u3,t∥2] + 16pL2 g,1α2 yη2 1 N
NX
n=1
E[∥v(n) 1,t − ¯v1,t∥2] + 16pL2 g,1α2 yη2λ2 1 N
NX
n=1
E[∥v(n) 2,t − ¯v2,t∥2]
+ 72pβ2 xη4L2 g,1 1 N
NX
n=1
E[∥x(n) t − ¯xt∥2] + 72pβ2 xη4L2 g,1 1 N
NX
n=1
E[∥y(n) t − ¯yt∥2]
+ 24pL2 g,1α2 xη2E[∥ ¯mx,t∥2] + 16pL2 g,1α2 yη2E[∥ ¯my,t∥2] + 36pβ2 xη4δ2 + 24pβ2 xη4σ2 , (42)
1
N
NX
n=1
E[∥u(n) 3,t+1 − ¯u3,t+1∥2] ≤ (1 + 1 p + 24pL2 g,1α2 xη2λ2) 1 N
NX
n=1
E[∥u(n) 3,t − ¯u3,t∥2] + 24pL2 g,1α2 xη2 1 N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2]
+ 24pL2 g,1α2 xη2λ2 1 N
NX
n=1
E[∥u(n) 2,t − ¯u2,t∥2] + 8pL2 g,1λ2α2 zη2 1 N
NX
n=1
E[∥w(n) 1,t − ¯w1,t∥2]
+ 72pβ2 xη4L2 g,1 1 N
NX
n=1
E[∥x(n) t − ¯xt∥2] + 72pβ2 xη4L2 g,1 1 N
NX
n=1
E[∥z(n) t − ¯zt∥2]
+ 24pL2 g,1α2 xη2E[∥ ¯mx,t∥2] + 8pL2 g,1α2 zη2E[∥ ¯mz,t∥2] + 36pβ2 xη4δ2 + 24pβ2 xη4σ2 , (43)
1
N
NX
n=1
E[∥v(n) 1,t+1 − ¯v1,t+1∥2] ≤ (1 + 1 p + 16pL2 f α2 yη2) 1 N
NX
n=1
E[∥v(n) 1,t − ¯v1,t∥2] + 24pL2 f α2 xη2 1 N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2]
+ 24pL2 f α2 xη2λ2 1 N
NX
n=1
E[∥u(n) 2,t − ¯u2,t∥2] + 24pL2 f α2 xη2λ2 1 N
NX
n=1
E[∥u(n) 3,t − ¯u3,t∥2] + 16pL2 f α2 yη2λ2 1 N
NX
n=1
E[∥v(n) 2,t − ¯v2,t∥2]

+ 72pβ2 yη4L2 f 1 N
NX
n=1
E[∥x(n) t − ¯xt∥2] + 72pβ2 yη4L2 f 1 N
NX
n=1
E[∥y(n) t − ¯yt∥2]
+ 24pL2 f α2 xη2E[∥ ¯mx,t∥2] + 16pL2 f α2 yη2E[∥ ¯my,t∥2] + 36pβ2 yη4δ2 + 24pβ2 yη4σ2 , (44)
1
N
NX
n=1
E[∥v(n) 2,t+1 − ¯v2,t+1∥2] ≤ (1 + 1 p + 16pL2 g,1α2 yη2λ2) 1 N
NX
n=1
E[∥v(n) 2,t − ¯v2,t∥2] + 24pL2 g,1α2 xη2 1 N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2]
+ 24pL2 g,1α2 xη2λ2 1 N
NX
n=1
E[∥u(n) 2,t − ¯u2,t∥2] + 24pL2 g,1α2 xη2λ2 1 N
NX
n=1
E[∥u(n) 3,t − ¯u3,t∥2] + 16pL2 g,1α2 yη2 1 N
NX
n=1
E[∥v(n) 1,t − ¯v1,t∥2]
+ 72pβ2 yη4L2 g,1 1 N
NX
n=1
E[∥x(n) t − ¯xt∥2] + 72pβ2 yη4L2 g,1 1 N
NX
n=1
E[∥y(n) t − ¯yt∥2]
+ 24pL2 g,1α2 xη2E[∥ ¯mx,t∥2] + 16pL2 g,1α2 yη2E[∥ ¯my,t∥2] + 36pβ2 yη4δ2 + 24pβ2 yη4σ2 , (45)
1
N
NX
n=1
E[∥w(n) 1,t+1 − ¯w1,t+1∥2] ≤ (1 + 1 p + 8pL2 g,1λ2α2 zη2) 1 N
NX
n=1
E[∥w(n) 1,t − ¯w1,t∥2] + 24pL2 g,1α2 xη2 1 N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2]
+ 24pL2 g,1α2 xη2λ2 1 N
NX
n=1
E[∥u(n) 2,t − ¯u2,t∥2] + 24pL2 g,1α2 xη2λ2 1 N
NX
n=1
E[∥u(n) 3,t − ¯u3,t∥2]
+ 72pβ2 z η4L2 g,1 1 N
NX
n=1
E[∥x(n) t − ¯xt∥2] + 72pβ2 z η4L2 g,1 1 N
NX
n=1
E[∥z(n) t − ¯zt∥2]
+ 24pL2 g,1α2 xη2E[∥ ¯mx,t∥2] + 8pL2 g,1α2 zη2E[∥ ¯mz,t∥2] + 36pβ2 z η4δ2 + 24pβ2 z η4σ2 . (46)
Proof.
1
N
NX
n=1
E[∥u(n) 1,t+1 − ¯u1,t+1∥2]
= 1 N
NX
n=1
E[∥

(1 − βxη2)(u(n) 1,t − ∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1)) + ∇1f (n)(x(n) t+1, y(n) t+1; ξ(n) t+1) 
− 1 N
NX
m=1

(1 − βxη2)(u(m) 1,t − ∇1f (m)(x(m) t , y(m) t ; ξ(m) t+1 )) + ∇1f (m)(x(m) t+1, y(m) t+1 ; ξ(m) t+1 )  ∥2]
= 1 N
NX
n=1
E[∥(1 − βxη2)(u(n) 1,t − 1 N
NX
m=1
u(m) 1,t )
− ∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1) + ∇1f (n)(x(n) t+1, y(n) t+1; ξ(n) t+1) + βxη2∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1)
− 1 N
NX
m=1

− ∇1f (m)(x(m) t , y(m) t ; ξ(m) t+1 ) + ∇1f (m)(x(m) t+1, y(m) t+1 ; ξ(m) t+1 ) + βxη2∇1f (m)(x(m) t , y(m) t ; ξ(m) t+1 )  ∥2]
≤ (1 − βxη2)2(1 + c) 1 N
NX
n=1
E[∥u(n) 1,t − 1 N
NX
m=1
u(m) 1,t ∥2]
+ (1 + c−1) 1 N
NX
n=1
E[∥ − ∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1) + ∇1f (n)(x(n) t+1, y(n) t+1; ξ(n) t+1) + βxη2∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1)
− 1 N
NX
m=1

− ∇1f (m)(x(m) t , y(m) t ; ξ(m) t+1 ) + ∇1f (m)(x(m) t+1, y(m) t+1 ; ξ(m) t+1 ) + βxη2∇1f (m)(x(m) t , y(m) t ; ξ(m) t+1 )  ∥2]
≤ (1 − βxη2)2(1 + c) 1 N
NX
n=1
E[∥u(n) 1,t − 1 N
NX
m=1
u(m) 1,t ∥2]

+ 2(1 + c−1) 1 N
NX
n=1
E[∥ − ∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1) + ∇1f (n)(x(n) t+1, y(n) t+1; ξ(n) t+1)
− 1 N
NX
m=1

− ∇1f (m)(x(m) t , y(m) t ; ξ(m) t+1 ) + ∇1f (m)(x(m) t+1, y(m) t+1 ; ξ(m) t+1 )  ∥2]
+ 2(1 + c−1) 1 N
NX
n=1
E[∥βxη2∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1) − 1 N
NX
m=1
βxη2∇1f (m)(x(m) t , y(m) t ; ξ(m) t+1 )∥2]
≤ (1 − βxη2)2(1 + c) 1 N
NX
n=1
E[∥u(n) 1,t − 1 N
NX
m=1
u(m) 1,t ∥2]
+ 2(1 + c−1) 1 N
NX
n=1
E[∥ − ∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1) + ∇1f (n)(x(n) t+1, y(n) t+1; ξ(n) t+1)∥2]
+ 2(1 + c−1)β2 xη4 1 N
NX
n=1
E[∥∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1) − 1 N
NX
m=1
∇1f (m)(x(m) t , y(m) t ; ξ(m) t+1 )∥2]
≤ (1 − βxη2)2(1 + c) 1 N
NX
n=1
E[∥u(n) 1,t − 1 N
NX
m=1
u(m) 1,t ∥2]
+ 2(1 + c−1)L2 f 1 N
NX
n=1
E[∥x(n) t − x(n) t+1∥2 + 2(1 + c−1)L2 f 1 N
NX
n=1
E[∥y(n) t − y(n) t+1∥2
+ 2(1 + c−1)β2 xη4 1 N
NX
n=1
E[∥∇1f (n)(x(n) t , y(n) t ; ξ(n) t+1) − 1 N
NX
m=1
∇1f (m)(x(m) t , y(m) t ; ξ(m) t+1 )∥2]
≤ (1 − βxη2)2(1 + c) 1 N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2]
+ 12(1 + c−1)L2 f α2 xη2 1 N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2] + 12(1 +c−1)L2 f α2 xη2λ2 1 N
NX
n=1
E[∥u(n) 2,t − ¯u2,t∥2]
+ 12(1 + c−1)L2 f α2 xη2λ2 1 N
NX
n=1
E[∥u(n) 3,t − ¯u3,t∥2] + 12(1 +c−1)L2 f α2 xη2E[∥ ¯mx,t∥2]
+ 8(1 + c−1)L2 f α2 yη2 1 N
NX
n=1
E[∥v(n) 1,t − ¯v1,t∥2] + 8(1 +c−1)L2 f α2 yη2λ2 1 N
NX
n=1
E[∥v(n) 2,t − ¯v2,t∥2]
+ 8(1 + c−1)L2 f α2 yη2E[∥ ¯my,t∥2]
+ 36(1 + c−1)β2 xη4L2 f 1 N
NX
n=1
E[∥x(n) t − ¯xt∥2] + 36(1 +c−1)β2 xη4L2 f 1 N
NX
n=1
E[∥y(n) t − ¯yt∥2]
+ 18(1 + c−1)β2 xη4δ2 + 12(1 + c−1)β2 xη4σ2
≤ (1 + 1 p ) 1 N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2] + 24pL2 f α2 xη2 1 N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2] + 24pL2 f α2 xη2λ2 1 N
NX
n=1
E[∥u(n) 2,t − ¯u2,t∥2]
+ 24pL2 f α2 xη2λ2 1 N
NX
n=1
E[∥u(n) 3,t − ¯u3,t∥2] + 16pL2 f α2 yη2 1 N
NX
n=1
E[∥v(n) 1,t − ¯v1,t∥2] + 16pL2 f α2 yη2λ2 1 N
NX
n=1
E[∥v(n) 2,t − ¯v2,t∥2]
+ 72pβ2 xη4L2 f 1 N
NX
n=1
E[∥x(n) t − ¯xt∥2] + 72pβ2 xη4L2 f 1 N
NX
n=1
E[∥y(n) t − ¯yt∥2]
+ 24pL2 f α2 xη2E[∥ ¯mx,t∥2] + 16pL2 f α2 yη2E[∥ ¯my,t∥2] + 36pβ2 xη4δ2 + 24pβ2 xη4σ2 , (47)

where the second to last step follows from Lemma A.4 and Lemma A.6, the last step follows from η ≤ 1√βx , c = 1 p and p >1.
The other inequalities can be proved in the same way. Therefore, we omit their detailed proof.
Lemma A.8. Given Assumptions 4.1-4.5, by denoting st = ⌊t/p⌋, we have the following inequalities:
1
N
NX
n=1
E[∥x(n) t − ¯xt∥2] ≤ 3pα2 xη2
t−1X
t′=stp
1
N
NX
n=1
E[∥u(n) 1,t′ − ¯u1,t′∥2] + 3pα2 xη2λ2
t−1X
t′=stp
1
N
NX
n=1
E[∥u(n) 2,t′ − ¯u2,t′∥2]
+ 3pα2 xη2λ2
t−1X
t′=stp
1
N
NX
n=1
E[∥u(n) 3,t′ − ¯u3,t′∥2] , (48)
1
N
NX
n=1
E[∥y(n) t − ¯yt∥2] ≤ 2pα2 yη2
t−1X
t′=stp
1
N
NX
n=1
E[∥v(n) 1,t′ − ¯v1,t′∥2] + 2pα2 yη2λ2
t−1X
t′=stp
1
N
NX
n=1
E[∥v(n) 2,t′ − ¯v2,t′∥2] , (49)
1
N
NX
n=1
E[∥z(n) t − ¯zt∥2] ≤ pλ2α2 zη2
t−1X
t′=stp
1
N
NX
n=1
E[∥w(n) 1,t′ − ¯w1,t′∥2] . (50)
Proof. By denoting st = ⌊t/p⌋, we have
1
N
NX
n=1
E[∥x(n) t − ¯xt∥2]
= 1 N
NX
n=1
E[∥x(n) stp − αxη
t−1X
t′=stp
m(n) x,t′ − ¯xstp + αxη
t−1X
t′=stp
¯mx,t′∥2]
= 1 N
NX
n=1
E[∥ −αxη
t−1X
t′=stp
m(n) x,t′ + αxη
t−1X
t′=stp
¯mx,t′∥2]
≤ pα2 xη2
t−1X
t′=stp
1
N
NX
n=1
E[∥ −m(n) x,t′ + ¯mx,t′∥2]
= pα2 xη2
t−1X
t′=stp
1
N
NX
n=1
E[∥u(n) 1,t′ + λ(u(n) 2,t′ − u(n) 3,t′) − ¯u1,t′ − λ(¯u2,t′ − ¯u3,t′)∥2]
≤ 3pα2 xη2
t−1X
t′=stp
1
N
NX
n=1
E[∥u(n) 1,t′ − ¯u1,t′∥2] + 3pα2 xη2λ2
t−1X
t′=stp
1
N
NX
n=1
E[∥u(n) 2,t′ − ¯u2,t′∥2]
+ 3pα2 xη2λ2
t−1X
t′=stp
1
N
NX
n=1
E[∥u(n) 3,t′ − ¯u3,t′∥2] . (51)
The other two inequalities can be proved in the same way. Therefore, we omit their detailed proof.
Lemma A.9. (Restatement of Lemma 4.11) Given Assumptions 4.1-4.5, and
η ≤ 1
500p
q
L2 f + L2 g,1λ2
, βx ≤
L2 f + L2 g,1λ2
N , βy ≤
L2 f + L2 g,1λ2
N , βz ≤
L2 f + L2 g,1λ2
N ,
αx ≤ 10 , αy ≤ 10 , αz ≤ 10 , (52)
we have
1
T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2] + λ2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 2,t − ¯u2,t∥2] + λ2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 3,t − ¯u3,t∥2]

+ 1 T
T −1X
t=0
1
N
NX
n=1
E[∥v(n) 1,t − ¯v1,t∥2] + λ2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥v(n) 2,t − ¯v2,t∥2] + λ2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥w(n) 1,t − ¯w1,t∥2]
≤ 576p2α2 xη2

L2 f + L2 g,1λ2
 1
T
T −1X
t=0
E[∥ ¯mx,t∥2] + 576p2α2 yη2

L2 f + L2 g,1λ2
 1
T
T −1X
t=0
E[∥ ¯my,t∥2]
+ 576p2α2 zη2

L2 f + L2 g,1λ2
 1
T
T −1X
t=0
E[∥ ¯mz,t∥2] + 576p2β2 xη4(1 + λ2)δ2 + 576p2β2 yη4(1 + λ2)δ2 + 576p2β2 z η4λ2δ2
+ 576p2β2 xη4(1 + λ2)σ2 + 576p2β2 yη4(1 + λ2)σ2 + 576p2β2 z η4λ2σ2 . (53)
Proof.
1
N
NX
n=1
E[∥u(n) 1,t+1 − ¯u1,t+1∥2] + λ2 1 N
NX
n=1
E[∥u(n) 2,t+1 − ¯u2,t+1∥2] + λ2 1 N
NX
n=1
E[∥u(n) 3,t+1 − ¯u3,t+1∥2]
+ 1 N
NX
n=1
E[∥v(n) 1,t+1 − ¯v1,t+1∥2] + λ2 1 N
NX
n=1
E[∥v(n) 2,t+1 − ¯v2,t+1∥2] + λ2 1 N
NX
n=1
E[∥w(n) 1,t+1 − ¯w1,t+1∥2]
≤

1 + 1 p + 48pL2 f α2 xη2 + 96pL2 g,1α2 xη2λ2  1 N NX n=1 E[∥u(n) 1,t − ¯u1,t∥2]
+

1 + 1 p + 48pL2 f α2 xη2 + 96pL2 g,1α2 xη2λ2  λ2 1 N NX n=1 E[∥u(n) 2,t − ¯u2,t∥2]
+

1 + 1 p + 48pL2 f α2 xη2 + 96pL2 g,1α2 xη2λ2  λ2 1 N NX n=1 E[∥u(n) 3,t − ¯u3,t∥2]
+

1 + 1 p + 32pL2 f α2 yη2 + 32pL2 g,1α2 yη2λ2  1 N NX n=1 E[∥v(n) 1,t − ¯v1,t∥2]
+

1 + 1 p + 32pL2 f α2 yη2 + 32pL2 g,1α2 yη2λ2  λ2 1 N NX n=1 E[∥v(n) 2,t − ¯v2,t∥2]
+

1 + 1 p + 16pL2 g,1λ2α2 zη2  λ2 1 N NX n=1 E[∥w(n) 1,t − ¯w1,t∥2]
+

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 144pβ2 xη4L2 g,1λ2 + 72pβ2 yη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2
 1
N
NX
n=1
E[∥x(n) t − ¯xt∥2]
+

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 72pβ2 xη4L2 g,1λ2 + 72pβ2 yη4L2 g,1λ2
 1
N
NX
n=1
E[∥y(n) t − ¯yt∥2]
+

72pβ2 xη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2
 1
N
NX
n=1
E[∥z(n) t − ¯zt∥2]
+

48pL2 f α2 xη2 + 96pL2 g,1α2 xη2λ2

E[∥ ¯mx,t∥2] +  32pL2 f α2 yη2 + 32pL2 g,1α2 yη2λ2  E[∥ ¯my,t∥2]
+ 16pL2 g,1λ2α2 zη2E[∥ ¯mz,t∥2] + 36pβ2 xη4δ2 + 72pλ2β2 xη4δ2 + 36pβ2 yη4δ2 + 36pλ2β2 yη4δ2 + 36pλ2β2 z η4δ2
+ 24pβ2 xη4σ2 + 48pλ2β2 xη4σ2 + 24pβ2 yη4σ2 + 24pλ2β2 yη4σ2 + 24pλ2β2 z η4σ2
≤

1 + 26 25p  1 N NX n=1  E[∥u(n) 1,t − ¯u1,t∥2] + λ2E[∥u(n) 2,t − ¯u2,t∥2] + λ2E[∥u(n) 3,t − ¯u3,t∥2]
+ E[∥v(n) 1,t − ¯v1,t∥2] + λ2E[∥v(n) 2,t − ¯v2,t∥2] + λ2E[∥w(n) 1,t − ¯w1,t∥2] 

+

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 144pβ2 xη4L2 g,1λ2 + 72pβ2 yη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2
 1
N
NX
n=1
E[∥x(n) t − ¯xt∥2]
+

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 72pβ2 xη4L2 g,1λ2 + 72pβ2 yη4L2 g,1λ2
 1
N
NX
n=1
E[∥y(n) t − ¯yt∥2]
+

72pβ2 xη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2
 1
N
NX
n=1
E[∥z(n) t − ¯zt∥2]
+

48pL2 f α2 xη2 + 96pL2 g,1α2 xη2λ2

E[∥ ¯mx,t∥2] +  32pL2 f α2 yη2 + 32pL2 g,1α2 yη2λ2  E[∥ ¯my,t∥2]
+ 16pL2 g,1λ2α2 zη2E[∥ ¯mz,t∥2] + 36pβ2 xη4δ2 + 72pλ2β2 xη4δ2 + 36pβ2 yη4δ2 + 36pλ2β2 yη4δ2 + 36pλ2β2 z η4δ2
+ 24pβ2 xη4σ2 + 48pλ2β2 xη4σ2 + 24pβ2 yη4σ2 + 24pλ2β2 yη4σ2 + 24pλ2β2 z η4σ2
≤

1 + 26 25p  1 N NX n=1  E[∥u(n) 1,t − ¯u1,t∥2] + λ2E[∥u(n) 2,t − ¯u2,t∥2] + λ2E[∥u(n) 3,t − ¯u3,t∥2]
+ E[∥v(n) 1,t − ¯v1,t∥2] + λ2E[∥v(n) 2,t − ¯v2,t∥2] + λ2E[∥w(n) 1,t − ¯w1,t∥2] 
+ 3pα2 xη2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 144pβ2 xη4L2 g,1λ2
+ 72pβ2 yη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2
 t−1X
t′=stp
1
N
NX
n=1
E[∥u(n) 1,t′ − ¯u1,t′∥2]
+ 3pα2 xη2λ2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 144pβ2 xη4L2 g,1λ2
+ 72pβ2 yη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2
 t−1X
t′=stp
1
N
NX
n=1
E[∥u(n) 2,t′ − ¯u2,t′∥2]
+ 3pα2 xη2λ2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 144pβ2 xη4L2 g,1λ2
+ 72pβ2 yη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2
 t−1X
t′=stp
1
N
NX
n=1
E[∥u(n) 3,t′ − ¯u3,t′∥2]
+ 2pα2 yη2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 72pβ2 xη4L2 g,1λ2 + 72pβ2 yη4L2 g,1λ2
 t−1X
t′=stp
1
N
NX
n=1
E[∥v(n) 1,t′ − ¯v1,t′∥2]
+ 2pα2 yη2λ2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 72pβ2 xη4L2 g,1λ2 + 72pβ2 yη4L2 g,1λ2
 t−1X
t′=stp
1
N
NX
n=1
E[∥v(n) 2,t′ − ¯v2,t′∥2]
+

72pβ2 xη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2

pλ2α2 zη2
t−1X
t′=stp
1
N
NX
n=1
E[∥w(n) 1,t′ − ¯w1,t′∥2]
+

48pL2 f α2 xη2 + 96pL2 g,1α2 xη2λ2

E[∥ ¯mx,t∥2] +  32pL2 f α2 yη2 + 32pL2 g,1α2 yη2λ2  E[∥ ¯my,t∥2]
+ 16pL2 g,1λ2α2 zη2E[∥ ¯mz,t∥2] + 36pβ2 xη4δ2 + 72pλ2β2 xη4δ2 + 36pβ2 yη4δ2 + 36pλ2β2 yη4δ2 + 36pλ2β2 z η4δ2
+ 24pβ2 xη4σ2 + 48pλ2β2 xη4σ2 + 24pβ2 yη4σ2 + 24pλ2β2 yη4σ2 + 24pλ2β2 z η4σ2
≤ 3pα2 xη2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 144pβ2 xη4L2 g,1λ2
+ 72pβ2 yη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2
 tX
i=stp

1 + 26 25p t−i i−1X t′=stp 1 N NX n=1 E[∥u(n) 1,t′ − ¯u1,t′∥2]
+ 3pα2 xη2λ2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 144pβ2 xη4L2 g,1λ2

+ 72pβ2 yη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2
 tX
i=stp

1 + 26 25p t−i i−1X t′=stp 1 N NX n=1 E[∥u(n) 2,t′ − ¯u2,t′∥2]
+ 3pα2 xη2λ2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 144pβ2 xη4L2 g,1λ2
+ 72pβ2 yη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2
 tX
i=stp

1 + 26 25p t−i i−1X t′=stp 1 N NX n=1 E[∥u(n) 3,t′ − ¯u3,t′∥2]
+ 2pα2 yη2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 72pβ2 xη4L2 g,1λ2
+ 72pβ2 yη4L2 g,1λ2
 tX
i=stp

1 + 26 25p t−i i−1X t′=stp 1 N NX n=1 E[∥v(n) 1,t′ − ¯v1,t′∥2]
+ 2pα2 yη2λ2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 72pβ2 xη4L2 g,1λ2
+ 72pβ2 yη4L2 g,1λ2
 tX
i=stp

1 + 26 25p t−i i−1X t′=stp 1 N NX n=1 E[∥v(n) 2,t′ − ¯v2,t′∥2]
+

72pβ2 xη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2

pλ2α2 zη2
tX
i=stp

1 + 26 25p t−i i−1X t′=stp 1 N NX n=1 E[∥w(n) 1,t′ − ¯w1,t′∥2]
+

48pL2 f α2 xη2 + 96pL2 g,1α2 xη2λ2
 tX
i=stp

1 + 26 25p t−i E[∥ ¯mx,i∥2]
+

32pL2 f α2 yη2 + 32pL2 g,1α2 yη2λ2
 tX
i=stp

1 + 26 25p t−i E[∥ ¯my,i∥2]
+ 16pL2 g,1λ2α2 zη2
tX
i=stp

1 + 26 25p t−i E[∥ ¯mz,i∥2]
+ (36pβ2 xη4δ2 + 72pλ2β2 xη4δ2 + 36pβ2 yη4δ2 + 36pλ2β2 yη4δ2 + 36pλ2β2 z η4δ2)
tX
i=stp

1 + 26 25p t−i
+ (24pβ2 xη4σ2 + 48pλ2β2 xη4σ2 + 24pβ2 yη4σ2 + 24pλ2β2 yη4σ2 + 24pλ2β2 z η4σ2)
tX
i=stp

1 + 26 25p t−i
≤ 9p3α2 xη2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 144pβ2 xη4L2 g,1λ2
+ 72pβ2 yη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2
 tX
t′=stp
1
N
NX
n=1
E[∥u(n) 1,t′ − ¯u1,t′∥2]
+ 9p2α2 xη2λ2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 144pβ2 xη4L2 g,1λ2
+ 72pβ2 yη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2
 tX
t′=stp
1
N
NX
n=1
E[∥u(n) 2,t′ − ¯u2,t′∥2]
+ 9p2α2 xη2λ2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 144pβ2 xη4L2 g,1λ2
+ 72pβ2 yη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2
 tX
t′=stp
1
N
NX
n=1
E[∥u(n) 3,t′ − ¯u3,t′∥2]
+ 6p2α2 yη2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 72pβ2 xη4L2 g,1λ2 + 72pβ2 yη4L2 g,1λ2
 tX
t′=stp
1
N
NX
n=1
E[∥v(n) 1,t′ − ¯v1,t′∥2]

+ 6p2α2 yη2λ2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 72pβ2 xη4L2 g,1λ2 + 72pβ2 yη4L2 g,1λ2
 tX
t′=stp
1
N
NX
n=1
E[∥v(n) 2,t′ − ¯v2,t′∥2]
+ 3p2λ2α2 zη2

72pβ2 xη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2
 tX
t′=stp
1
N
NX
n=1
E[∥w(n) 1,t′ − ¯w1,t′∥2]
+ 3

48pL2 f α2 xη2 + 96pL2 g,1α2 xη2λ2
 tX
t′=stp
E[∥ ¯mx,t′∥2] + 3  32pL2 f α2 yη2 + 32pL2 g,1α2 yη2λ2  tX
t′=stp
E[∥ ¯my,t′∥2]
+ 3

16pL2 g,1λ2α2 zη2
 tX
t′=stp
E[∥ ¯mz,t′∥2]
+
tX
i=stp
3(36pβ2 xη4δ2 + 72pλ2β2 xη4δ2 + 36pβ2 yη4δ2 + 36pλ2β2 yη4δ2 + 36pλ2β2 z η4δ2)
+
tX
i=stp
3(24pβ2 xη4σ2 + 48pλ2β2 xη4σ2 + 24pβ2 yη4σ2 + 24pλ2β2 yη4σ2 + 24pλ2β2 z η4σ2) , (54)
where the first step follows from Lemma A.7, the second step follows fromαx ≤ 10, αy < 10, αz < 10, η ≤ 1 500p √ L2 f +L2 g,1λ2 ,
η ≤ 1 500p √ L2 f +L2 g,1λ2 , and η ≤ 1 500p √ L2 f +L2 g,1λ2 , the third step follows from Lemma A.8, the fourth step follows from periodic
communication at the stp iteration, the last step follows from

1 + 26 25p
t−i
≤

1 + 26 25p
p
≤ 3.
As a result, we have
1
T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2] + λ2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 2,t − ¯u2,t∥2] + λ2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 3,t − ¯u3,t∥2]
+ 1 T
T −1X
t=0
1
N
NX
n=1
E[∥v(n) 1,t − ¯v1,t∥2] + λ2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥v(n) 2,t − ¯v2,t∥2] + λ2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥w(n) 1,t − ¯w1,t∥2]
≤ 9p2α2 xη2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 144pβ2 xη4L2 g,1λ2
+ 72pβ2 yη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2
 1
T
T −1X
t=0
tX
t′=stp
1
N
NX
n=1
E[∥u(n) 1,t′ − ¯u1,t′∥2]
+ 9p2α2 xη2λ2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 144pβ2 xη4L2 g,1λ2
+ 72pβ2 yη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2
 1
T
T −1X
t=0
tX
t′=stp
1
N
NX
n=1
E[∥u(n) 2,t′ − ¯u2,t′∥2]
+ 9p2α2 xη2λ2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 144pβ2 xη4L2 g,1λ2
+ 72pβ2 yη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2
 1
T
T −1X
t=0
tX
t′=stp
1
N
NX
n=1
E[∥u(n) 3,t′ − ¯u3,t′∥2]
+ 6p2α2 yη2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 72pβ2 xη4L2 g,1λ2 + 72pβ2 yη4L2 g,1λ2
 1
T
T −1X
t=0
tX
t′=stp
1
N
NX
n=1
E[∥v(n) 1,t′ − ¯v1,t′∥2]
+ 6p2α2 yη2λ2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 72pβ2 xη4L2 g,1λ2 + 72pβ2 yη4L2 g,1λ2
 1
T
T −1X
t=0
tX
t′=stp
1
N
NX
n=1
E[∥v(n) 2,t′ − ¯v2,t′∥2]
+ 3p2λ2α2 zη2

72pβ2 xη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2
 1
T
T −1X
t=0
tX
t′=stp
1
N
NX
n=1
E[∥w(n) 1,t′ − ¯w1,t′∥2]

+ 3

48pL2 f α2 xη2 + 96pL2 g,1α2 xη2λ2
 1
T
T −1X
t=0
tX
t′=stp
E[∥ ¯mx,t′∥2]
+ 3

32pL2 f α2 yη2 + 32pL2 g,1α2 yη2λ2
 1
T
T −1X
t=0
tX
t′=stp
E[∥ ¯my,t′∥2]
+ 3

16pL2 g,1λ2α2 zη2
 1
T
T −1X
t=0
tX
t′=stp
E[∥ ¯mz,t′∥2]
+ 1 T
T −1X
t=0
tX
i=stp
3(36pβ2 xη4δ2 + 72pλ2β2 xη4δ2 + 36pβ2 yη4δ2 + 36pλ2β2 yη4δ2 + 36pλ2β2 z η4δ2)
+ 1 T
T −1X
t=0
tX
i=stp
3(24pβ2 xη4σ2 + 48pλ2β2 xη4σ2 + 24pβ2 yη4σ2 + 24pλ2β2 yη4σ2 + 24pλ2β2 z η4σ2)
≤ 9p3α2 xη2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 144pβ2 xη4L2 g,1λ2
+ 72pβ2 yη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2
 1
T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2]
+ 9p3α2 xη2λ2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 144pβ2 xη4L2 g,1λ2
+ 72pβ2 yη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2
 1
T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 2,t − ¯u2,t∥2]
+ 9p3α2 xη2λ2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 144pβ2 xη4L2 g,1λ2
+ 72pβ2 yη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2
 1
T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 3,t − ¯u3,t∥2]
+ 6p3α2 yη2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 72pβ2 xη4L2 g,1λ2 + 72pβ2 yη4L2 g,1λ2
 1
T
T −1X
t=0
1
N
NX
n=1
E[∥v(n) 1,t − ¯v1,t∥2]
+ 6p3α2 yη2λ2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 72pβ2 xη4L2 g,1λ2 + 72pβ2 yη4L2 g,1λ2
 1
T
T −1X
t=0
1
N
NX
n=1
E[∥v(n) 2,t − ¯v2,t∥2]
+ 3p3λ2α2 zη2

72pβ2 xη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2
 1
T
T −1X
t=0
1
N
NX
n=1
E[∥w(n) 1,t − ¯w1,t∥2]
+ 3p

48pL2 f α2 xη2 + 96pL2 g,1α2 xη2λ2
 1
T
T −1X
t=0
E[∥ ¯mx,t∥2] + 3p  32pL2 f α2 yη2 + 32pL2 g,1α2 yη2λ2  1 T T −1X t=0 E[∥ ¯my,t∥2]
+ 3p

16pL2 g,1λ2α2 zη2
 1
T
T −1X
t=0
E[∥ ¯mz,t∥2]
+ 3p(36pβ2 xη4δ2 + 72pλ2β2 xη4δ2 + 36pβ2 yη4δ2 + 36pλ2β2 yη4δ2 + 36pλ2β2 z η4δ2)
+ 3p(24pβ2 xη4σ2 + 48pλ2β2 xη4σ2 + 24pβ2 yη4σ2 + 24pλ2β2 yη4σ2 + 24pλ2β2 z η4σ2) . (55)
Then, by setting αx ≤ 10, we enforce
1 − 9p3α2 xη2

72pβ2 xη4L2 f + 144pβ2 xη4L2 g,1λ2 + 72pβ2 yη4L2 f + 72pβ2 yη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2

≥ 1 − 1296p3α2 xη2

pβ2 xη4L2 f + pβ2 xη4L2 g,1λ2 + pβ2 yη4L2 f + pβ2 yη4L2 g,1λ2 + pβ2 z η4L2 g,1λ2

≥ 1 − 129600p3η2

pβ2 xη4L2 f + pβ2 xη4L2 g,1λ2 + pβ2 yη4L2 f + pβ2 yη4L2 g,1λ2 + pβ2 z η4L2 g,1λ2


≥ 1 2 . (56)
This can be done by setting βx ≤
L2 f +L2 g,1λ2
N , βy ≤
L2 f +L2 g,1λ2
N , βz ≤
L2 f +L2 g,1λ2
N , and η ≤ 1 500p √ L2 f +L2 g,1λ2 such that
129600p4β2 xη6(L2 f + L2 g,1λ2)
≤ 129600p4(L2 f + L2 g,1λ2) 1 5006p6(L2 f + L2 g,1λ2)3 (L2 f + L2 g,1λ2)2 N 2
= 1296 5006N 2p2
≤ 1296 5006
≤ 1 6 , (57)
129600p4β2 yη6(L2 f + L2 g,1λ2)
≤ 129600p4(L2 f + L2 g,1λ2) 1 5006p6(L2 f + L2 g,1λ2)3 (L2 f + L2 g,1λ2)2 N 2
≤ 1 6 , (58)
and
129600p4β2 z η6L2 g,1λ2
≤ 129600p4β2 z η6(L2 f,1 + L2 g,1λ2)
≤ 1 6 . (59)
Similarly, by setting αy ≤ 10, we enforce
1 − 6p3α2 yη2

72pβ2 xη4L2 f + 72pβ2 yη4L2 f + 72pβ2 xη4L2 g,1λ2 + 72pβ2 yη4L2 g,1λ2

≥ 1 − 1296p4α2 yη6

β2 xL2 f + β2 xL2 g,1λ2 + β2 yL2 f + β2 yL2 g,1λ2

≥ 1 − 129600p4η6

β2 xL2 f + β2 xL2 g,1λ2 + β2 yL2 f + β2 yL2 g,1λ2

≥ 1 2 . (60)
This can be done by setting βx ≤
L2 f +L2 g,1λ2
N , βy ≤
L2 f +L2 g,1λ2
N , and η ≤ 1 500p √ L2 f +L2 g,1λ2 such that
129600p4β2 xη6(L2 f + L2 g,1λ2)
≤ 1296p4α2 yη6(L2 f + L2 g,1λ2) (L2 f + L2 g,1λ2)2 N 2

 1
500p
q
L2 f + L2 g,1λ2


6
≤ 1 6 , (61)
and
129600p4β2 yη6(L2 f + L2 g,1λ2) ≤ 1 6 . (62)
Moreover, by setting αz ≤ 10, we enforce
1 − 3p3λ2α2 zη2

72pβ2 xη4L2 g,1λ2 + 72pβ2 z η4L2 g,1λ2

≥ 1 − 1296p4λ2α2 zη6

β2 x(L2 f,1 + L2 g,1λ2) + β2 z (L2 f,1 + L2 g,1λ2) 

≥ 1 − 129600p4λ2η6

β2 x(L2 f,1 + L2 g,1λ2) + β2 z (L2 f,1 + L2 g,1λ2) 
≥ 1 2 . (63)
This can be done by setting βx ≤
L2 f +L2 g,1λ2
N , βz ≤
L2 f +L2 g,1λ2
N , and η ≤ 1 500p √ L2 f +L2 g,1λ2 such that
129600p4λ2η6β2 x(L2 f,1 + L2 g,1λ2) ≤ 1 6 ,
129600p4λ2η6β2 z (L2 f,1 + L2 g,1λ2) ≤ 1 6 . (64)
In summary, by setting
η ≤ 1
500p
q
L2 f + L2 g,1λ2
,
βx ≤
L2 f + L2 g,1λ2
N , βy ≤
L2 f + L2 g,1λ2
N , βz ≤
L2 f + L2 g,1λ2
N ,
αx ≤ 10 , αy ≤ 10 , αz ≤ 10 , (65)
we have
1
T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2] + λ2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 2,t − ¯u2,t∥2] + λ2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 3,t − ¯u3,t∥2]
+ 1 T
T −1X
t=0
1
N
NX
n=1
E[∥v(n) 1,t − ¯v1,t∥2] + λ2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥v(n) 2,t − ¯v2,t∥2] + λ2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥w(n) 1,t − ¯w1,t∥2]
≤ 6p2

48L2 f α2 xη2 + 96L2 g,1α2 xη2λ2
 1
T
T −1X
t=0
E[∥ ¯mx,t∥2] + 6p2

32L2 f α2 yη2 + 32L2 g,1α2 yη2λ2
 1
T
T −1X
t=0
E[∥ ¯mx,t∥2]
+ 6p2

16L2 g,1λ2α2 zη2
 1
T
T −1X
t=0
E[∥ ¯mz,t∥2]
+ 6p2(36β2 xη4δ2 + 72λ2β2 xη4δ2 + 36β2 yη4δ2 + 36λ2β2 yη4δ2 + 36λ2β2 z η4δ2)
+ 6p2(24β2 xη4σ2 + 48λ2β2 xη4σ2 + 24β2 yη4σ2 + 24λ2β2 yη4σ2 + 24λ2β2 z η4σ2)
≤ 576p2α2 xη2

L2 f + L2 g,1λ2
 1
T
T −1X
t=0
E[∥ ¯mx,t∥2] + 576p2α2 yη2

L2 f + L2 g,1λ2
 1
T
T −1X
t=0
E[∥ ¯my,t∥2]
+ 576p2α2 zη2

L2 f + L2 g,1λ2
 1
T
T −1X
t=0
E[∥ ¯mz,t∥2]
+ 576p2β2 xη4(1 + λ2)δ2 + 576p2β2 yη4(1 + λ2)δ2 + 576p2β2 z η4λ2δ2
+ 576p2β2 xη4(1 + λ2)σ2 + 576p2β2 yη4(1 + λ2)σ2 + 576p2β2 z η4λ2σ2 . (66)
A.2 Proof of Theorem 4.8
Based on these fundamental lemmas, we are ready to prove the convergence rate of our Algorithm 1 in Theorem 4.8.
Proof. At first, we propose a novel potential function as follows:
Pt+1 = E[L∗ λ(¯xt+1)] + c1λE[∥¯yt+1 − y∗ λ(¯xt+1)∥2] + c2λE[∥¯zt+1 − y∗(¯xt+1)∥2]
+ c3E[∥ 1 N
NX
n=1
∇1f (n)(x(n) t+1, y(n) t+1) − 1 N
NX
n=1
u(n) 1,t+1∥2] + c4λ2E[∥ 1 N
NX
n=1
∇1g(n)(x(n) t+1, y(n) t+1) − 1 N
NX
n=1
u(n) 2,t+1∥2]
+ c5λ2E[∥ 1 N
NX
n=1
∇1g(n)(x(n) t+1, z(n) t+1) − 1 N
NX
n=1
u(n) 3,t+1∥2] + c6E[∥ 1 N
NX
n=1
∇2f (n)(x(n) t+1, y(n) t+1) − 1 N
NX
n=1
v(n) 1,t+1∥2]

+ c7λ2E[∥ 1 N
NX
n=1
∇2g(n)(x(n) t+1, y(n) t+1) − 1 N
NX
n=1
v(n) 2,t+1∥2] + c8λ2E[∥ 1 N
NX
n=1
∇2g(n)(x(n) t+1, z(n) t+1) − 1 N
NX
n=1
w(n) 1,t+1∥2] .
(67)
Then, we have
Pt+1 − Pt
≤ −αxη 2 E[∥∇L∗ λ(¯xt)∥2]
+

− αxη 4 + 100ηα2 x(Lf + λLg,1)2 3αyλ2µ3 c1 + 25ηα2 xL2 g,1 6αzµ3 c2 + C1  E[∥ ¯mx,t∥2]
+

− 3ηα2 yλ 4 c1 + C2  E[∥ ¯my,t∥2]
+

− 3ηα2 zλ 4 c2 + C3  E[∥ ¯mz,t∥2]
+
 9αxη
2 (L2 f + λ2L2 g,1) − ηαyµλ2 8 c1  E[∥y∗ λ(¯xt) − ¯yt∥2]
+
 9αxη
2 λ2L2 g,1 − ηαzλ2µ 4 c2  E[∥y∗(¯xt) − ¯zt∥2]
+ C4
1
N
NX
n=1
E[∥x(n) t − ¯xt∥2] + C5 1 N
NX
n=1
E[∥y(n) t − ¯yt∥2] + C6 1 N
NX
n=1
E[∥z(n) t − ¯zt∥2]
+ C1
1
N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2] + λ2C1 1 N
NX
n=1
E[∥u(n) 2,t − ¯u2,t∥2] + λ2C1 1 N
NX
n=1
E[∥u(n) 3,t − ¯u3,t∥2]
+ C2
1
N
NX
n=1
E[∥v(n) 1,t − ¯v1,t∥2] + λ2C2 1 N
NX
n=1
E[∥v(n) 2,t − ¯v2,t∥2] + λ2C3 1 N
NX
n=1
E[∥w(n) 1,t − ¯w1,t∥2]
+ (9αxη 2 − βxη2c3)E[∥ 1 N
NX
n=1
∇1f (n)(x(n) t , y(n) t ) − 1 N
NX
n=1
u(n) 1,t ∥2]
+ (9αxηλ2
2 − βxη2λ2c4)E[∥ 1 N
NX
n=1
∇1g(n)(x(n) t , y(n) t ) − 1 N
NX
n=1
u(n) 2,t ∥2]
+ (9αxηλ2
2 − βxη2λ2c5)E[∥ 1 N
NX
n=1
∇1g(n)(x(n) t , z(n) t ) − 1 N
NX
n=1
u(n) 3,t ∥2]
+ (100ηαy
3µ c1 − βyη2c6)E[∥ 1 N
NX
n=1
∇2f (n)(x(n) t , y(n) t ) − 1 N
NX
n=1
v(n) 1,t ∥2]
+ (100ηαy
3µ λ2c1 − βyη2λ2c7)E[∥ 1 N
NX
n=1
∇2g(n)(x(n) t , y(n) t ) − 1 N
NX
n=1
v(n) 2,t ∥2]
+ (25ηαz
3µ λ2c2 − βzη2λ2c8)E[∥ 1 N
NX
n=1
∇2g(n)(x(n) t , z(n) t ) − 1 N
NX
n=1
w(n) 1,t ∥2]
+ 2β2 xη4σ2 1 N c3 + 2β2 xη4σ2 1 N λ2c4 + 2β2 xη4σ2 1 N λ2c5 + 2β2 yη4σ2 1 N c6 + 2β2 yη4σ2 1 N λ2c7 + 2β2 z η4σ2 1 N λ2c8 , (68)
where
C1 =
12α2 xη2L2 f
N c3 + 12α2 xη2L2 g,1 N λ2c4 + 12α2 xη2L2 g,1 N λ2c5 + 12α2 xη2L2 f N c6 + 12α2 xη2L2 g,1 N λ2c7 + 12α2 xη2L2 g,1 N λ2c8 ,
C2 =
8α2 yη2L2 f
N c3 + 8α2 yη2L2 g,1 N λ2c4 + 8α2 yη2L2 f N c6 + 8α2 yη2L2 g,1 N λ2c7 ,
C3 = 4α2 zη2L2 g,1 N λ2c5 + 4α2 zη2L2 g,1 N λ2c8 ,

C4 = 9αxη 2 (L2 f + λ2L2 g,1 + λ2L2 g,1) + 100ηαy 3µ (L2 f + λ2L2 g,1)c1 + 25ηαz 3µ λ2L2 g,1c2 ,
C5 = 9αxη 2 (L2 f + λ2L2 g,1) + 100ηαy 3µ (L2 f + λ2L2 g,1)c1 ,
C6 = 9αxη 2 λ2L2 g,1 + 25ηαz 3µ λ2L2 g,1c2 . (69)
By setting λ >1 and
c1 =
72αx(L2 f + L2 g,1)
αyµ , c2 = 36αxL2 g,1 αzµ , c3 = 9αx 2βxη , c4 = 9αx 2βxη ,
c5 = 9αx 2βxη , c6 = 1200αx(L2 f + L2 g,1) µ2βyη , c7 = 1200αx(L2 f + L2 g,1) µ2βyη , c8 = 1200αx(L2 f + L2 g,1) µ2βzη , (70)
we have
Pt+1 − Pt
≤ −αxη 2 E[∥∇L∗ λ(¯xt)∥2] − 9αxη 2 (L2 f + L2 g,1)λ2E[∥y∗ λ(¯xt) − ¯yt∥2] − 9αxη 2 λ2L2 g,1E[∥y∗(¯xt) − ¯zt∥2]
+

− αxη 4 + 100ηα2 x(Lf + λLg,1)2 3αyλ2µ3 c1 + 25ηα2 xL2 g,1 6αzµ3 c2 + C1  E[∥ ¯mx,t∥2]
+

− 3ηα2 yλ 4 c1 + C2  E[∥ ¯my,t∥2]
+

− 3ηα2 zλ 4 c2 + C3  E[∥ ¯mz,t∥2]
+ C4
1
N
NX
n=1
E[∥x(n) t − ¯xt∥2] + C5 1 N
NX
n=1
E[∥y(n) t − ¯yt∥2] + C6 1 N
NX
n=1
E[∥z(n) t − ¯zt∥2]
+ C1
1
N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2] + λ2C1 1 N
NX
n=1
E[∥u(n) 2,t − ¯u2,t∥2] + λ2C1 1 N
NX
n=1
E[∥u(n) 3,t − ¯u3,t∥2]
+ C2
1
N
NX
n=1
E[∥v(n) 1,t − ¯v1,t∥2] + λ2C2 1 N
NX
n=1
E[∥v(n) 2,t − ¯v2,t∥2] + λ2C3 1 N
NX
n=1
E[∥w(n) 1,t − ¯w1,t∥2]
+ 2β2 xη4σ2 1 N c3 + 2β2 xη4σ2 1 N λ2c4 + 2β2 xη4σ2 1 N λ2c5 + 2β2 yη4σ2 1 N c6 + 2β2 yη4σ2 1 N λ2c7 + 2β2 z η4σ2 1 N λ2c8 . (71)
By summing over t from 0 to T − 1, we have
αxη
2
1
T
T −1X
t=0
E[∥∇L∗ λ(¯xt)∥2]
≤ P0 − PT
T +

− αxη 4 + 100ηα2 x(Lf + λLg,1)2 3αyλ2µ3 c1 + 25ηα2 xL2 g,1 6αzµ3 c2 + C1  1 T T −1X t=0 E[∥ ¯mx,t∥2]
+

− 3ηα2 yλ 4 c1 + C2  1 T T −1X t=0 E[∥ ¯my,t∥2] +  − 3ηα2 zλ 4 c2 + C3  1 T T −1X t=0 E[∥ ¯mz,t∥2]
+ C4
1
T
T −1X
t=0
1
N
NX
n=1
E[∥x(n) t − ¯xt∥2] + C5 1 T
T −1X
t=0
1
N
NX
n=1
E[∥y(n) t − ¯yt∥2] + C6 1 T
T −1X
t=0
1
N
NX
n=1
E[∥z(n) t − ¯zt∥2]
+ C1
1
T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2] + λ2C1 1 T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 2,t − ¯u2,t∥2] + λ2C1 1 T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 3,t − ¯u3,t∥2]
+ C2
1
T
T −1X
t=0
1
N
NX
n=1
E[∥v(n) 1,t − ¯v1,t∥2] + λ2C2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥v(n) 2,t − ¯v2,t∥2] + λ2C3 1 T
T −1X
t=0
1
N
NX
n=1
E[∥w(n) 1,t − ¯w1,t∥2]

+ 2β2 xη4σ2 1 N c3 + 2β2 xη4σ2 1 N λ2c4 + 2β2 xη4σ2 1 N λ2c5 + 2β2 yη4σ2 1 N c6 + 2β2 yη4σ2 1 N λ2c7 + 2β2 z η4σ2 1 N λ2c8 . (72)
Based on Lemma A.8, we have
1
T
T −1X
t=0
1
N
NX
n=1
E[∥x(n) t − ¯xt∥2] ≤ 3p2α2 xη2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2] + 3p2α2 xη2λ2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 2,t − ¯u2,t∥2]
+ 3p2α2 xη2λ2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 3,t − ¯u3,t∥2] ,
1
T
T −1X
t=0
1
N
NX
n=1
E[∥y(n) t − ¯yt∥2] ≤ 2p2α2 yη2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥v(n) 1,t − ¯v1,t∥2] + 2p2α2 yη2λ2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥v(n) 2,t − ¯v2,t∥2] ,
1
T
T −1X
t=0
1
N
NX
n=1
E[∥z(n) t − ¯zt∥2] ≤ p2λ2α2 zη2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥w(n) 1,t − ¯w1,t∥2] . (73)
Then, we have
αxη
2
1
T
T −1X
t=0
E[∥∇L∗ λ(¯xt)∥2]
≤ P0 − PT
T +

− αxη 4 + 100ηα2 x(Lf + λLg,1)2 3αyλ2µ3 c1 + 25ηα2 xL2 g,1 6αzµ3 c2 + C1  1 T T −1X t=0 E[∥ ¯mx,t∥2]
+

− 3ηα2 yλ 4 c1 + C2  1 T T −1X t=0 E[∥ ¯my,t∥2] +  − 3ηα2 zλ 4 c2 + C3  1 T T −1X t=0 E[∥ ¯mz,t∥2]
+

C1 + 3C4p2α2 xη2
 1
T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2]
+

C1 + 3C4p2α2 xη2

λ2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 2,t − ¯u2,t∥2]
+

C1 + 3C4p2α2 xη2

λ2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 3,t − ¯u3,t∥2]
+

C2 + 2C5p2α2 yη2
 1
T
T −1X
t=0
1
N
NX
n=1
E[∥v(n) 1,t − ¯v1,t∥2]
+

C2 + 2C5p2α2 yη2

λ2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥v(n) 2,t − ¯v2,t∥2]
+

C3 + C6p2α2 zη2

λ2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥w(n) 1,t − ¯w1,t∥2]
+ 2β2 xη4σ2 1 N c3 + 2β2 xη4σ2 1 N λ2c4 + 2β2 xη4σ2 1 N λ2c5 + 2β2 yη4σ2 1 N c6 + 2β2 yη4σ2 1 N λ2c7 + 2β2 z η4σ2 1 N λ2c8
≤ P0 − PT
T +

− αxη 4 + 100ηα2 x(Lf + λLg,1)2 3αyλ2µ3 c1 + 25ηα2 xL2 g,1 6αzµ3 c2 + C1  1 T T −1X t=0 E[∥ ¯mx,t∥2]
+

− 3ηα2 yλ 4 c1 + C2  1 T T −1X t=0 E[∥ ¯my,t∥2] +  − 3ηα2 zλ 4 c2 + C3  1 T T −1X t=0 E[∥ ¯mz,t∥2]
+

C1 + 3C4p2α2 xη2 + C2 + 2C5p2α2 yη2 + C3 + C6p2α2 zη2
 1
T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 1,t − ¯u1,t∥2]

+ λ2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 2,t − ¯u2,t∥2] + λ2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥u(n) 3,t − ¯u3,t∥2]
+ 1 T
T −1X
t=0
1
N
NX
n=1
E[∥v(n) 1,t − ¯v1,t∥2] + λ2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥v(n) 2,t − ¯v2,t∥2] + λ2 1 T
T −1X
t=0
1
N
NX
n=1
E[∥w(n) 1,t − ¯w1,t∥2] 
+ 2β2 xη4σ2 1 N c3 + 2β2 xη4σ2 1 N λ2c4 + 2β2 xη4σ2 1 N λ2c5 + 2β2 yη4σ2 1 N c6 + 2β2 yη4σ2 1 N λ2c7 + 2β2 z η4σ2 1 N λ2c8
≤ P0 − PT
T +

− αxη 4 + 100ηα2 x(Lf + λLg,1)2 3αyλ2µ3 c1 + 25ηα2 xL2 g,1 6αzµ3 c2 + C1  1 T T −1X t=0 E[∥ ¯mx,t∥2]
+

− 3ηα2 yλ 4 c1 + C2  1 T T −1X t=0 E[∥ ¯my,t∥2] +  − 3ηα2 zλ 4 c2 + C3  1 T T −1X t=0 E[∥ ¯mz,t∥2]
+ 576p2α2 xη2

L2 f + L2 g,1λ2

C7
1
T
T −1X
t=0
E[∥ ¯mx,t∥2] + 576p2α2 yη2

L2 f + L2 g,1λ2

C7
1
T
T −1X
t=0
E[∥ ¯my,t∥2]
+ 576p2α2 zη2

L2 f + L2 g,1λ2

C7
1
T
T −1X
t=0
E[∥ ¯mz,t∥2]
+ 576p2β2 xη4(1 + λ2)δ2C7 + 576p2β2 yη4(1 + λ2)δ2C7 + 576p2β2 z η4λ2δ2C7
+ 576p2β2 xη4(1 + λ2)σ2C7 + 576p2β2 yη4(1 + λ2)σ2C7 + 576p2β2 z η4λ2σ2C7
+ 2β2 xη4σ2 1 N c3 + 2β2 xη4σ2 1 N λ2c4 + 2β2 xη4σ2 1 N λ2c5 + 2β2 yη4σ2 1 N c6 + 2β2 yη4σ2 1 N λ2c7 + 2β2 z η4σ2 1 N λ2c8
= P0 − PT
T +

− αxη 4 + 100ηα2 x(Lf + λLg,1)2 3αyλ2µ3 c1 + 25ηα2 xL2 g,1 6αzµ3 c2 + C1 + 576p2α2 xη2  L2 f + L2 g,1λ2  C7
!
1
T
T −1X
t=0
E[∥ ¯mx,t∥2]
+

− 3ηα2 yλ 4 c1 + C2 + 576p2α2 yη2  L2 f + L2 g,1λ2  C7
!
1
T
T −1X
t=0
E[∥ ¯my,t∥2]
+

− 3ηα2 zλ 4 c2 + C3 + 576p2α2 zη2  L2 f + L2 g,1λ2  C7  1 T T −1X t=0 E[∥ ¯mz,t∥2]
+ 576p2β2 xη4(1 + λ2)δ2C7 + 576p2β2 yη4(1 + λ2)δ2C7 + 576p2β2 z η4λ2δ2C7
+ 576p2β2 xη4(1 + λ2)σ2C7 + 576p2β2 yη4(1 + λ2)σ2C7 + 576p2β2 z η4λ2σ2C7
+ 2β2 xη4σ2 1 N c3 + 2β2 xη4σ2 1 N λ2c4 + 2β2 xη4σ2 1 N λ2c5 + 2β2 yη4σ2 1 N c6 + 2β2 yη4σ2 1 N λ2c7 + 2β2 z η4σ2 1 N λ2c8 , (74)
where the third step follows from Lemma A.7 and
C7 = C1 + 3C4p2α2 xη2 + C2 + 2C5p2α2 yη2 + C3 + C6p2α2 zη2 . (75)
In the following, we select hyperparameters to eliminate 1 T PT −1 t=0 E[∥ ¯mx,t∥2], 1 T PT −1 t=0 E[∥ ¯my,t∥2], and
1
T
PT −1
t=0 E[∥ ¯mz,t∥2] from the upper bound.
At first, based on Eq. (70), Lg,1 > µ, and λ ≥ max{ 2Lf µ , 1}, we have
C1 ≤
 1
βxN + 1 βyN + 1 βzN  28800α3 xη(L2 f + L2 g,1)2 µ2 λ2 ,
C2 ≤
 1
βxN + 1 βyN  19200α2 yαxη(L2 f + L2 g,1)2 µ2 λ2 ,
C3 ≤ 1 βzN 4818α2 zαxη(L2 f + L2 g,1)2 µ2 λ2 ,
C4 ≤
1360αxη(L2 f + L2 g,1)2
µ2 λ2 ,

C5 ≤
1210αxη(L2 f + L2 g,1)2
µ2 λ2 ,
C6 ≤
160αxη(L2 f + L2 g,1)2
µ2 λ2 ,
C7 ≤
 1
βxN + 1 βyN + 1 βzN  28800α3 xη(L2 f + L2 g,1)2 µ2 λ2 +  1 βxN + 1 βyN  19200α2 yαxη(L2 f + L2 g,1)2 µ2 λ2
+ 1 βzN 4818α2 zαxη(L2 f + L2 g,1)2 µ2 λ2 + 4080α3 xp2η3(L2 f + L2 g,1)2 µ2 λ2
+
2420αxα2 yp2η3(L2 f + L2 g,1)2
µ2 λ2 + 160αxα2 zp2η3(L2 f + L2 g,1)2 µ2 λ2 . (76)
Then, to eliminate 1 T PT −1 t=0 E[∥ ¯mx,t∥2], we enforce
− αxη 4 + 100ηα2 x(Lf + λLg,1)2 3αyλ2µ3 c1 + 25ηα2 xL2 g,1 6αzµ3 c2 + C1 + 576p2α2 xη2  L2 f + L2 g,1λ2  C7
≤ −αxη 4 + 100ηα2 x(Lf + λLg,1)2 3αyλ2µ3 c1 + 25ηα2 xL2 g,1 6αzµ3 c2 + C1 + 576p2α2 xη2  L2 f + L2 g,1  λ2C7
≤ −αxη 4 + 100ηα2 x(Lf + λLg,1)2 3αyλ2µ3 36αx(L2 f + L2 g,1) αyµ + 25ηα2 xL2 g,1 6αzµ3 18αxL2 g,1 αzµ
+
 1
βxN + 1 βyN + 1 βzN  28800α3 xη(L2 f + L2 g,1)2 µ2 λ2
+ 576p2α2 xη2

L2 f + L2 g,1

λ2
 1
βxN + 1 βyN + 1 βzN  28800α3 xη(L2 f + L2 g,1)2 µ2 λ2
+ 576p2α2 xη2

L2 f + L2 g,1

λ2
 1
βxN + 1 βyN  19200α2 yαxη(L2 f + L2 g,1)2 µ2 λ2
+ 576p2α2 xη2

L2 f + L2 g,1

λ2 1 βzN 4818α2 zαxη(L2 f + L2 g,1)2 µ2 λ2
+ 576p2α2 xη2

L2 f + L2 g,1

λ2 4080α3 xp2η3(L2 f + L2 g,1)2
µ2 λ2
+ 576p2α2 xη2

L2 f + L2 g,1

λ2 2420αxα2 yp2η3(L2 f + L2 g,1)2
µ2 λ2
+ 576p2α2 xη2

L2 f + L2 g,1

λ2 160αxα2 zp2η3(L2 f + L2 g,1)2
µ2 λ2
≤ 0 . (77)
This can be done by setting
100ηα2 x(Lf + λLg,1)2
3αyλ2µ3
36αx(L2 f + L2 g,1)
αyµ ≤ αxη 36 ,
25ηα2 xL2 g,1
6αzµ3
18αxL2 g,1
αzµ ≤ αxη 36 ,  1
βxN + 1 βyN + 1 βzN  28800α3 xη(L2 f + L2 g,1)2 µ2 λ2 ≤ αxη 36 ,
576p2α2 xη2

L2 f + L2 g,1

λ2
 1
βxN + 1 βyN + 1 βzN  28800α3 xη(L2 f + L2 g,1)2 µ2 λ2 ≤ αxη 36 ,
576p2α2 xη2

L2 f + L2 g,1

λ2
 1
βxN + 1 βyN  19200α2 yαxη(L2 f + L2 g,1)2 µ2 λ2 ≤ αxη 36 ,

576p2α2 xη2

L2 f + L2 g,1

λ2 1 βzN 4818α2 zαxη(L2 f + L2 g,1)2 µ2 λ2 ≤ αxη 36 ,
576p2α2 xη2

L2 f + L2 g,1

λ2 4080α3 xp2η3(L2 f + L2 g,1)2
µ2 λ2 ≤ αxη 36 ,
576p2α2 xη2

L2 f + L2 g,1

λ2 2420αxα2 yp2η3(L2 f + L2 g,1)2
µ2 λ2 ≤ αxη 36 ,
576p2α2 xη2

L2 f + L2 g,1

λ2 160αxα2 zp2η3(L2 f + L2 g,1)2
µ2 λ2 ≤ αxη 36 . (78)
To solve the first inequality in Eq. (78), we enforce
100ηα2 x(Lf + λLg,1)2
3αyλ2µ3
36αx(L2 f + L2 g,1)
αyµ
≤ 100ηα2 x(Lf + Lg,1)2λ2
3αyλ2µ3
36αx(Lf + Lg,1)2
αyµ
≤ αxη 36 . (79)
Then, we can obtain
αx ≤ αyµ2 360(Lf + Lg,1)2 . (80)
By solving the second inequality in Eq. (78), we can obtain
αx ≤ αzµ2 60(Lf + Lg,1)2 . (81)
By solving the third inequality in Eq. (78), we can obtain
αx ≤ µ 100λ(Lf + Lg,1)2
,s
1
βxN + 1 βyN + 1 βzN . (82)
To solve the fourth inequality in Eq. (78), we enforce
576p2α2 xη2

L2 f + L2 g,1

λ2
 1
βxN + 1 βyN + 1 βzN  28800α3 xη(L2 f + L2 g,1)2 µ2 λ2
≤ 576 × 28800αxηα4 xp2η2λ4
 1
βxN + 1 βyN + 1 βzN  (Lf + Lg,1)6 µ2
≤ αxη 36 . (83)
Then, we can obtain
αx ≤ 1 160λ(pη)1/2 µ1/2 (Lf + Lg,1)3/2
,  1
βxN + 1 βyN + 1 βzN 1/4 . (84)
To solve the fifth inequality in Eq. (78), we enforce
576p2α2 xη2

L2 f + L2 g,1

λ2
 1
βxN + 1 βyN  19200α2 yαxη(L2 f + L2 g,1)2 µ2 λ2
≤ 576 × 19200α2 yα2 xp2η2λ4
 1
βxN + 1 βyN  (Lf + Lg,1)6 µ2 αxη
≤ 576 × 19200α2 y α2 yµ4 3602(Lf + Lg,1)4 p2η2λ4  1 βxN + 1 βyN  (Lf + Lg,1)6 µ2 αxη
≤ αxη 36 . (85)

Then, we can obtain
αy ≤ 1 8λ(pη)1/2 1p µ(Lf + Lg,1)
,  1
βxN + 1 βyN 1/4 . (86)
To solve the sixth inequality in Eq. (78), we enforce
576p2α2 xη2

L2 f + L2 g,1

λ2 1 βzN 4818α2 zαxη(L2 f + L2 g,1)2 µ2 λ2
≤ 576 × 4818α2 zα2 xp2η2λ4 1 βzN (Lf + Lg,1)6 µ2 αxη
≤ 576 × 4818α2 z α2 zµ4 602(Lf + Lg,1)4 p2η2λ4 1 βzN (Lf + Lg,1)6 µ2 αxη
≤ αxη 36 . (87)
Then, we can obtain
αz ≤ 1 λ(pη)1/2 1p µ(Lf + Lg,1)
,  1
βzN
1/4
. (88)
To solve the seventh inequality in Eq. (78), we enforce
576p2α2 xη2

L2 f + L2 g,1

λ2 4080α3 xp2η3(L2 f + L2 g,1)2
µ2 λ2
≤ 576 × 4080α4 xp4η4λ4 (Lf + Lg,1)6 µ2 αxη
≤ αxη 36 . (89)
Then, we can obtain
αx ≤ 1 100λpη µ1/2 (Lf + Lg,1)3/2 . (90)
To solve the eighth inequality in Eq. (78), we enforce
576p2α2 xη2

L2 f + L2 g,1

λ2 2420αxα2 yp2η3(L2 f + L2 g,1)2
µ2 λ2 (91)
≤ 576 × 2420α2 yα2 xp4η4λ4 (Lf + Lg,1)6 µ2 αxη
≤ 576 × 2420α2 y α2 yµ4 3602(Lf + Lg,1)4 p4η4λ4 (Lf + Lg,1)6 µ2 αxη
≤ αxη 36 . (92)
Then, we can obtain
αy ≤ 1 λpη 1p µ(Lf + Lg,1) . (93)
To solve the last inequality in Eq. (78), we enforce
576p2α2 xη2

L2 f + L2 g,1

λ2 160αxα2 zp2η3(L2 f + L2 g,1)2
µ2 λ2
≤ 576 × 160α2 zα2 xp4η4λ4 (Lf + Lg,1)6 µ2 αxη
≤ 576 × 160α2 z α2 zµ4 602(Lf + Lg,1)4 p4η4λ4 (Lf + Lg,1)6 µ2 αxη

≤ αxη 36 . (94)
Then, we can obtain
αz ≤ 1 λpη 1p µ(Lf + Lg,1) . (95)
In summary, by setting
αx ≤ min
(
αyµ2
360(Lf + Lg,1)2 , αzµ2 60(Lf + Lg,1)2 , µ 100λ(Lf + Lg,1)2
,s
1
βxN + 1 βyN + 1 βzN ,
1
160λ(pη)1/2
µ1/2
(Lf + Lg,1)3/2
,  1
βxN + 1 βyN + 1 βzN 1/4 , 1 100λpη µ1/2 (Lf + Lg,1)3/2 ) ,
αy ≤ min
(
1
8λ(pη)1/2
1p
µ(Lf + Lg,1)
,  1
βxN + 1 βyN 1/4 , 1 λpη 1p µ(Lf + Lg,1) ) ,
αz ≤ min
(
1
λ(pη)1/2
1p
µ(Lf + Lg,1)
,  1
βzN
1/4
, 1 λpη 1p µ(Lf + Lg,1)
)
, (96)
we can eliminate 1 T PT −1 t=0 E[∥ ¯mx,t∥2].
Similarly, to eliminate 1 T PT −1 t=0 E[∥ ¯my,t∥2], we enforce
− 3ηα2 yλ 4 c1 + C2 + 576p2α2 yη2  L2 f + L2 g,1λ2  C7
≤ −3ηα2 yλ 4 c1 + C2 + 576p2α2 yη2  L2 f + L2 g,1  λ2C7
≤ −3ηα2 yλ 4 36αx(L2 f + L2 g,1) αyµ +  1 βxN + 1 βyN  19200α2 yαxη(L2 f + L2 g,1)2 µ2 λ2
+ 576p2α2 yη2

L2 f + L2 g,1

λ2
 1
βxN + 1 βyN + 1 βzN  28800α3 xη(L2 f + L2 g,1)2 µ2 λ2
+ 576p2α2 yη2

L2 f + L2 g,1

λ2
 1
βxN + 1 βyN  19200α2 yαxη(L2 f + L2 g,1)2 µ2 λ2
+ 576p2α2 yη2

L2 f + L2 g,1

λ2 1 βzN 4818α2 zαxη(L2 f + L2 g,1)2 µ2 λ2
+ 576p2α2 yη2

L2 f + L2 g,1

λ2 4080α3 xp2η3(L2 f + L2 g,1)2
µ2 λ2
+ 576p2α2 yη2

L2 f + L2 g,1

λ2 2420αxα2 yp2η3(L2 f + L2 g,1)2
µ2 λ2
+ 576p2α2 yη2

L2 f + L2 g,1

λ2 160αxα2 zp2η3(L2 f + L2 g,1)2
µ2 λ2
≤ 0 . (97)
This can be done by setting
 1
βxN + 1 βyN  19200α2 yαxη(L2 f + L2 g,1)2 µ2 λ2 ≤ 3αyαxη(L2 f + L2 g,1) µ λ ,
576p2α2 yη2

L2 f + L2 g,1

λ2
 1
βxN + 1 βyN + 1 βzN  28800α3 xη(L2 f + L2 g,1)2 µ2 λ2 ≤ 3αyαxη(L2 f + L2 g,1) µ λ ,
576p2α2 yη2

L2 f + L2 g,1

λ2
 1
βxN + 1 βyN  19200α2 yαxη(L2 f + L2 g,1)2 µ2 λ2 ≤ 3αyαxη(L2 f + L2 g,1) µ λ ,

576p2α2 yη2

L2 f + L2 g,1

λ2 1 βzN 4818α2 zαxη(L2 f + L2 g,1)2 µ2 λ2 ≤ 3αyαxη(L2 f + L2 g,1) µ λ ,
576p2α2 yη2

L2 f + L2 g,1

λ2 4080α3 xp2η3(L2 f + L2 g,1)2
µ2 λ2 ≤ 3αyαxη(L2 f + L2 g,1) µ λ ,
576p2α2 yη2

L2 f + L2 g,1

λ2 2420αxα2 yp2η3(L2 f + L2 g,1)2
µ2 λ2 ≤ 3αyαxη(L2 f + L2 g,1) µ λ ,
576p2α2 yη2

L2 f + L2 g,1

λ2 160αxα2 zp2η3(L2 f + L2 g,1)2
µ2 λ2 ≤ 3αyαxη(L2 f + L2 g,1) µ λ . (98)
By solving the first inequality in Eq. (98), we can obtain
αy ≤ µ 6400λ(Lf + Lg,1)2
,  1
βxN + 1 βyN  . (99)
To solve the second inequality in Eq. (98), we enforce
576p2α2 yη2

L2 f + L2 g,1

λ2
 1
βxN + 1 βyN + 1 βzN  28800α3 xη(L2 f + L2 g,1)2 µ2 λ2
≤ 576 × 28800αyα2 xp2η2λ4
 1
βxN + 1 βyN + 1 βzN  (L2 f + L2 g,1)3 µ2 αyαxη
≤ 576 × 28800αy
α2 yµ4
3602(Lf + Lg,1)4 p2η2λ4
 1
βxN + 1 βyN + 1 βzN  (L2 f + L2 g,1)3 µ2 αyαxη
≤
3αyαxη(L2 f + L2 g,1)
µ λ . (100)
Then, we can obtain
αy ≤ 1 10λ(pη)2/3 1 µ
,  1
βxN + 1 βyN + 1 βzN 1/3 . (101)
To solve the third inequality in Eq. (98), we enforce
576p2α2 yη2

L2 f + L2 g,1

λ2
 1
βxN + 1 βyN  19200α2 yαxη(L2 f + L2 g,1)2 µ2 λ2
≤ 576 × 19200α3 yp2η2λ4
 1
βxN + 1 βyN  (L2 f + L2 g,1)3 µ2 αyαxη
≤
3αyαxη(L2 f + L2 g,1)
µ λ . (102)
Then, we can obtain
αy ≤ 1 200λ(pη)2/3 µ1/3 (Lf + Lg,1)4/3
,  1
βxN + 1 βyN 1/3 . (103)
To solve the fourth inequality in Eq. (98), we enforce
576p2α2 yη2

L2 f + L2 g,1

λ2 1 βzN 4818α2 zαxη(L2 f + L2 g,1)2 µ2 λ2
≤ 576 × 4818α2 zαyη2p2λ4 1 βzN (L2 f + L2 g,1)3 µ2 αyαxη
≤ 576 × 4818α2 z 1 2λµ(pη)4/3 η2p2λ4 1 βzN (L2 f + L2 g,1)3 µ2 αyαxη
≤
3αyαxη(L2 f + L2 g,1)
µ λ , (104)

where the third step follows from Eq. (107). Then, we can obtain
αz ≤ 1 1000(pη)1/3λ µ (L2 f + L2 g,1)
,  1
βzN
1/2
. (105)
To solve the fifth inequality in Eq. (98), we enforce
576p2α2 yη2

L2 f + L2 g,1

λ2 4080α3 xp2η3(L2 f + L2 g,1)2
µ2 λ2
≤ 576 × 4080α2 xαyp4η4λ4 (L2 f + L2 g,1)3 µ2 αxαyη
≤ 576 × 4080 α2 yµ4
3602(Lf + Lg,1)4 αyp4η4λ4 (Lf + Lg,1)6 µ2 αxαyη
≤
3αyαxη(L2 f + L2 g,1)
µ λ . (106)
Then, we can obtain
αy ≤ 1 2λµ(pη)4/3 . (107)
To solve the sixth inequality in Eq. (98), we enforce
576p2α2 yη2

L2 f + L2 g,1

λ2 2420αxα2 yp2η3(L2 f + L2 g,1)2
µ2 λ2
≤ 576 × 2420α3 yp4η4λ4 (L2 f + L2 g,1)3 µ2 αxαyη
≤
3αyαxη(L2 f + L2 g,1)
µ λ . (108)
Then, we can obtain
αy ≤ 1 100(pη)4/3λ µ1/3 (Lf + Lg,1)4/3 . (109)
To solve the last inequality in Eq. (98), we enforce
576p2α2 yη2

L2 f + L2 g,1

λ2 160αxα2 zp2η3(L2 f + L2 g,1)2
µ2 λ2
≤ 576 × 160α2 zαyp4η4λ4 (L2 f + L2 g,1)3 µ2 αxαyη
≤ 576 × 160α2 z 1 2λµ(pη)4/3 p4η4λ4 (L2 f + L2 g,1)3 µ2 αxαyη
≤
3αyαxη(L2 f + L2 g,1)
µ λ . (110)
Then, we can obtain
αz ≤ 1 1000(pη)4/3λ µ (L2 f + L2 g,1) . (111)
In summary, by setting
αy ≤ min
n µ
6400λ(Lf + Lg,1)2
,  1
βxN + 1 βyN  , 1 10λ(pη)2/3 1 µ ,  1 βxN + 1 βyN + 1 βzN 1/3 ,
1
200λ(pη)2/3
µ1/3
(Lf + Lg,1)4/3
,  1
βxN + 1 βyN 1/3 , 1 2λµ(pη)4/3 , 1 100(pη)4/3λ µ1/3 (Lf + Lg,1)4/3 o ,

αz ≤ min
(
1
1000(pη)1/3λ
µ
(L2 f + L2 g,1)
,  1
βzN
1/2
, 1 1000(pη)4/3λ µ (L2 f + L2 g,1)
)
, (112)
we can eliminate 1 T PT −1 t=0 E[∥ ¯my,t∥2]
Moreover, to eliminate 1 T PT −1 t=0 E[∥ ¯mz,t∥2], we enforce
− 3ηα2 zλ 4 c2 + C3 + 576p2α2 zη2  L2 f + L2 g,1λ2  C7
≤ −3ηα2 zλ 4 c2 + C3 + 576p2α2 zη2  L2 f + L2 g,1  λ2C7
≤ −27αzαxη 2 L2 g,1 µ λ + 1 βzN 4818α2 zαxη(L2 f + L2 g,1)2 µ2 λ2
+ 576p2α2 zη2

L2 f + L2 g,1

λ2
 1
βxN + 1 βyN + 1 βzN  28800α3 xη(L2 f + L2 g,1)2 µ2 λ2
+ 576p2α2 zη2

L2 f + L2 g,1

λ2
 1
βxN + 1 βyN  19200α2 yαxη(L2 f + L2 g,1)2 µ2 λ2
+ 576p2α2 zη2

L2 f + L2 g,1

λ2 1 βzN 4818α2 zαxη(L2 f + L2 g,1)2 µ2 λ2
+ 576p2α2 zη2

L2 f + L2 g,1

λ2 4080α3 xp2η3(L2 f + L2 g,1)2
µ2 λ2
+ 576p2α2 zη2

L2 f + L2 g,1

λ2 2420αxα2 yp2η3(L2 f + L2 g,1)2
µ2 λ2
+ 576p2α2 zη2

L2 f + L2 g,1

λ2 160αxα2 zp2η3(L2 f + L2 g,1)2
µ2 λ2
≤ 0 . (113)
This can be done by setting
1
βzN
4818α2 zαxη(L2 f + L2 g,1)2
µ2 λ2 ≤ αzαxηL2 g,1 µ λ ,
576p2α2 zη2

L2 f + L2 g,1

λ2
 1
βxN + 1 βyN + 1 βzN  28800α3 xη(L2 f + L2 g,1)2 µ2 λ2 ≤ αzαxηL2 g,1 µ λ ,
576p2α2 zη2

L2 f + L2 g,1

λ2
 1
βxN + 1 βyN  19200α2 yαxη(L2 f + L2 g,1)2 µ2 λ2 ≤ αzαxηL2 g,1 µ λ ,
576p2α2 zη2

L2 f + L2 g,1

λ2 1 βzN 4818α2 zαxη(L2 f + L2 g,1)2 µ2 λ2 ≤ αzαxηL2 g,1 µ λ ,
576p2α2 zη2

L2 f + L2 g,1

λ2 4080α3 xp2η3(L2 f + L2 g,1)2
µ2 λ2 ≤ αzαxηL2 g,1 µ λ ,
576p2α2 zη2

L2 f + L2 g,1

λ2 2420αxα2 yp2η3(L2 f + L2 g,1)2
µ2 λ2 ≤ αzαxηL2 g,1 µ λ ,
576p2α2 zη2

L2 f + L2 g,1

λ2 160αxα2 zp2η3(L2 f + L2 g,1)2
µ2 λ2 ≤ αzαxηL2 g,1 µ λ . (114)
By solving the first inequality in Eq. (114), we obtain
αz ≤ 1 4818λ µL2 g,1 (L2 f + L2 g,1)2
,
1
βzN . (115)
To solve the second inequality in Eq. (114), we enforce
576p2α2 zη2

L2 f + L2 g,1

λ2
 1
βxN + 1 βyN + 1 βzN  28800α3 xη(L2 f + L2 g,1)2 µ2 λ2

≤ 576 × 28800αzα2 xp2η2λ4
 1
βxN + 1 βyN + 1 βzN  (L2 f + L2 g,1)3 µ2 αzαxη
≤ 576 × 28800αz
α2 zµ4
602(Lf + Lg,1)4 p2η2λ4
 1
βxN + 1 βyN + 1 βzN  (L2 f + L2 g,1)3 µ2 αzαxη
≤ αzαxηL2 g,1
µ λ . (116)
Then, we can obtain
αz ≤ 1 20(pη)2/3λ Lg,1 µ
,  1
βxN + 1 βyN + 1 βzN 1/3 . (117)
To solve the third inequality in Eq. (114), we enforce
576p2α2 zη2

L2 f + L2 g,1

λ2
 1
βxN + 1 βyN  19200α2 yαxη(L2 f + L2 g,1)2 µ2 λ2
≤ 576 × 19200αzα2 yp2η2λ4
 1
βxN + 1 βyN  (L2 f + L2 g,1)3 µ2 αzαxη
≤ 576 × 19200αz
µ2
64002λ2(Lf + Lg,1)4
,  1
βxN + 1 βyN 2 p2η2λ4  1 βxN + 1 βyN  (L2 f + L2 g,1)3 µ2 αzαxη
≤ αzαxηL2 g,1
µ λ . (118)
Then, we can obtain
αz ≤ 4 p2η2λ L2 g,1 µ(Lf + Lg,1)2  1 βxN + 1 βyN  . (119)
To solve the fourth inequality in Eq. (114), we enforce
576p2α2 zη2

L2 f + L2 g,1

λ2 1 βzN 4818α2 zαxη(L2 f + L2 g,1)2 µ2 λ2
≤ 576 × 4818α3 zp2η2λ4 1 βzN (L2 f + L2 g,1)3 µ2 αzαxη
≤ αzαxηL2 g,1
µ λ . (120)
Then, we can obtain
αz ≤ 1 150(pη)2/3λ µ1/3L2/3 g,1 L2 f + L2 g,1 ,  1 βzN 1/3 . (121)
To solve the fifth inequality in Eq. (114), we enforce
576p2α2 zη2

L2 f + L2 g,1

λ2 4080α3 xp2η3(L2 f + L2 g,1)2
µ2 λ2
≤ 576 × 4080αzα2 xp4η4λ4 (L2 f + L2 g,1)3 µ2 αzαxη
≤ 576 × 4080αz
α2 zµ4
602(Lf + Lg,1)4 p4η4λ4 (L2 f + L2 g,1)3 µ2 αzαxη
≤ αzαxηL2 g,1
µ λ . (122)
Then, we can obtain
αz ≤ 1 10(pη)4/3λ Lg,1 µ . (123)

To solve the sixth inequality in Eq. (114), we enforce
576p2α2 zη2

L2 f + L2 g,1

λ2 2420αxα2 yp2η3(L2 f + L2 g,1)2
µ2 λ2
≤ 576 × 2420αzα2 yp4η4λ4 (L2 f + L2 g,1)3 µ2 αxαzη
≤ 576 × 2420αz
µ2
64002λ2(Lf + Lg,1)4
,  1
βxN + 1 βyN 2 p4η4λ4 (L2 f + L2 g,1)3 µ2 αxαzη
≤ αzαxηL2 g,1
µ λ . (124)
Then, we can obtain
αz ≤ 30 p4η4λ L2 g,1 µ(Lf + Lg,1)2  1 βxN + 1 βyN 2 . (125)
To solve the last inequality in Eq. (114), we enforce
576p2α2 zη2

L2 f + L2 g,1

λ2 160αxα2 zp2η3(L2 f + L2 g,1)2
µ2 λ2
≤ 576 × 160α3 zp4η4λ4 (L2 f + L2 g,1)3 µ2 αxαzη
≤ αzαxηL2 g,1
µ λ . (126)
Then, we can obtain
αz ≤ 1 50(pη)4/3λ µL2/3 g,1 (L2 f + L2 g,1) . (127)
In summary, by setting
αz ≤ min
n 1
4818λ
µL2 g,1
(L2 f + L2 g,1)2
,
1
βzN , 1 20(pη)2/3λ Lg,1 µ
,  1
βxN + 1 βyN + 1 βzN 1/3 ,
4
p2η2λ
L2 g,1
µ(Lf + Lg,1)2
 1
βxN + 1 βyN  , 1 150(pη)2/3λ µ1/3L2/3 g,1 L2 f + L2 g,1 ,  1 βzN 1/3 ,
1
10(pη)4/3λ
Lg,1
µ , 1 50(pη)4/3λ µL2/3 g,1 (L2 f + L2 g,1) o , (128)
we can eliminate 1 T PT −1 t=0 E[∥ ¯mz,t∥2]. As a result, by setting
αx ≤ min
(
αyµ2
360(Lf + Lg,1)2 , αzµ2 60(Lf + Lg,1)2 , µ 100λ(Lf + Lg,1)2
,s
1
βxN + 1 βyN + 1 βzN ,
1
160λ(pη)1/2
µ1/2
(Lf + Lg,1)3/2
,  1
βxN + 1 βyN + 1 βzN 1/4 , 1 100λpη µ1/2 (Lf + Lg,1)3/2 , 10 ) ,
αy ≤ min
(
1
8λ(pη)1/2
1p
µ(Lf + Lg,1)
,  1
βxN + 1 βyN 1/4 , 1 λpη 1p µ(Lf + Lg,1) ,
µ
6400λ(Lf + Lg,1)2
,  1
βxN + 1 βyN  , 1 10λ(pη)2/3 1 µ ,  1 βxN + 1 βyN + 1 βzN 1/3 ,
1
200λ(pη)2/3
µ1/3
(Lf + Lg,1)4/3
,  1
βxN + 1 βyN 1/3 , 1 2λµ(pη)4/3 , 1 100(pη)4/3λ µ1/3 (Lf + Lg,1)4/3 , 1 6(Lf + λLg,1) , 10 ) ,

αz ≤ min
(
1
λ(pη)1/2
1p
µ(Lf + Lg,1)
,  1
βzN
1/4
, 1 λpη 1p µ(Lf + Lg,1) ,
1
1000(pη)1/3λ
µ
(L2 f + L2 g,1)
,  1
βzN
1/2
, 1 1000(pη)4/3λ µ (L2 f + L2 g,1) ,
1
4818λ
µL2 g,1
(L2 f + L2 g,1)2
,
1
βzN , 1 20(pη)2/3λ Lg,1 µ
,  1
βxN + 1 βyN + 1 βzN 1/3 ,
4
p2η2λ
L2 g,1
µ(Lf + Lg,1)2
 1
βxN + 1 βyN  , 1 150(pη)2/3λ µ1/3L2/3 g,1 L2 f + L2 g,1 ,  1 βzN 1/3 ,
1
10(pη)4/3λ
Lg,1
µ , 1 50(pη)4/3λ µL2/3 g,1 (L2 f + L2 g,1) , 1 6λLg,1 , 10 ) ,
η ≤ min
(
1
500p
q
L2 f + L2 g,1λ2
, 1 2αxL , 1√βx , 1p βy , 1√βz
)
,
βx ≤
L2 f + L2 g,1λ2
N , βy ≤
L2 f + L2 g,1λ2
N , βz ≤
L2 f + L2 g,1λ2
N ,
λ ≥ max

1, 2Lf
µ

, (129)
we have
1
T
T −1X
t=0
E[∥∇L∗ λ(¯xt)∥2]
≤ 2 αxη P0 − PT T + 2C7 αxη  576p2β2 xη4(1 + λ2)δ2 + 576p2β2 yη4(1 + λ2)δ2 + 576p2β2 z η4λ2δ2
+ 576p2β2 xη4(1 + λ2)σ2 + 576p2β2 yη4(1 + λ2)σ2 + 576p2β2 z η4λ2σ2

+ 2β2 xη4σ2 1 N c3 2 αxη + 2β2 xη4σ2 1 N λ2c4 2 αxη + 2β2 xη4σ2 1 N λ2c5 2 αxη
+ 2β2 yη4σ2 1 N c6 2 αxη + 2β2 yη4σ2 1 N λ2c7 2 αxη + 2β2 z η4σ2 1 N λ2c8 2 αxη
≤ 2 αxη P0 − PT T
+ 2
"  1
βxN + 1 βyN + 1 βzN  28800α2 x(L2 f + L2 g,1)2 µ2 λ2 +  1 βxN + 1 βyN  19200α2 y(L2 f + L2 g,1)2 µ2 λ2
+ 1 βzN 4818α2 z(L2 f + L2 g,1)2 µ2 λ2 + 4080α2 xp2η2(L2 f + L2 g,1)2 µ2 λ2
+
2420α2 yp2η2(L2 f + L2 g,1)2
µ2 λ2 + 160α2 zp2η2(L2 f + L2 g,1)2 µ2 λ2 #
×

576p2β2 xη4(1 + λ2)δ2 + 576p2β2 yη4(1 + λ2)δ2 + 576p2β2 z η4λ2δ2
+ 576p2β2 xη4(1 + λ2)σ2 + 576p2β2 yη4(1 + λ2)σ2 + 576p2β2 z η4λ2σ2

+ 18βxη2σ2 1 N + 18βxη2σ2 1 N λ2 + 18βxη2σ2 1 N λ2
+ 4800βyη2σ2 1 N (L2 f + L2 g,1) µ2 + 4800βyη2σ2 1 N λ2 (L2 f + L2 g,1) µ2 + 4800βzη2σ2 1 N λ2 (L2 f + L2 g,1) µ2 . (130)
When t = 0, we have
P0 = E[L∗ λ(¯x0)] + c1λE[∥¯y0 − y∗ λ(¯x0)∥2] + c2λE[∥¯z0 − y∗(¯x0)∥2]

+ c3E[∥ 1 N
NX
n=1
∇1f (n)(x(n) 0 , y(n) 0 ) − 1 N
NX
n=1
u(n) 1,0 ∥2] + c4λ2E[∥ 1 N
NX
n=1
∇1g(n)(x(n) 0 , y(n) 0 ) − 1 N
NX
n=1
u(n) 2,0 ∥2]
+ c5λ2E[∥ 1 N
NX
n=1
∇1g(n)(x(n) 0 , z(n) 0 ) − 1 N
NX
n=1
u(n) 3,0 ∥2] + c6E[∥ 1 N
NX
n=1
∇2f (n)(x(n) 0 , y(n) 0 ) − 1 N
NX
n=1
v(n) 1,0 ∥2]
+ c7λ2E[∥ 1 N
NX
n=1
∇2g(n)(x(n) 0 , y(n) 0 ) − 1 N
NX
n=1
v(n) 2,0 ∥2] + c8λ2E[∥ 1 N
NX
n=1
∇2g(n)(x(n) 0 , z(n) 0 ) − 1 N
NX
n=1
w(n) 1,0 ∥2]
≤ E[L∗ λ(¯x0)] + 36αx(L2 f + L2 g,1) αyµ λE[∥¯y0 − y∗ λ(¯x0)∥2] + 18αxL2 g,1 αzµ λE[∥¯z0 − y∗(¯x0)∥2]
+ 9αx
2βxη
σ2
BN + 9αx 2βxη λ2 σ2 BN + 9αx 2βxη λ2 σ2 BN + 1200αx(L2 f + L2 g,1) µ2βyη σ2 BN
+
1200αx(L2 f + L2 g,1)
µ2βyη λ2 σ2 BN + 1200αx(L2 f + L2 g,1) µ2βzη λ2 σ2 BN , (131)
where B is the batch size in the initial step. Then, we have
1
T
T −1X
t=0
E[∥∇L(¯xt)∥2]
≤ 2 1 T
T −1X
t=0
E[∥∇L∗ λ(¯xt)∥2] + 2 1 T
T −1X
t=0
E[∥∇L∗ λ(¯xt) − ∇L(¯xt)∥2]
≤ 4 αxη E[L∗ λ(¯x0)] T + 4 ηT 36(L2 f + L2 g,1) αyµ λE[∥¯y0 − y∗ λ(¯x0)∥2] + 4 ηT 18L2 g,1 αzµ λE[∥¯z0 − y∗(¯x0)∥2]
+ 2 1 T
T −1X
t=0
E[∥∇L∗ λ(¯xt) − ∇L(¯xt)∥2] + 18 βxη2T σ2 BN + 36 βxη2T λ2 σ2 BN + 4800(L2 f + L2 g,1) µ2βyη2T σ2 BN
+
4800(L2 f + L2 g,1)
µ2βyη2T λ2 σ2 BN + 4800(L2 f + L2 g,1) µ2βzη2T λ2 σ2 BN
+ 4
"  1
βxN + 1 βyN + 1 βzN  28800α2 x(L2 f + L2 g,1)2 µ2 λ2 +  1 βxN + 1 βyN  19200α2 y(L2 f + L2 g,1)2 µ2 λ2
+ 1 βzN 4818α2 z(L2 f + L2 g,1)2 µ2 λ2 + 4080α2 xp2η2(L2 f + L2 g,1)2 µ2 λ2
+
2420α2 yp2η2(L2 f + L2 g,1)2
µ2 λ2 + 160α2 zp2η2(L2 f + L2 g,1)2 µ2 λ2 #
×

576p2β2 xη4(1 + λ2)δ2 + 576p2β2 yη4(1 + λ2)δ2 + 576p2β2 z η4λ2δ2
+ 576p2β2 xη4(1 + λ2)σ2 + 576p2β2 yη4(1 + λ2)σ2 + 576p2β2 z η4λ2σ2

+ 36βxη2σ2 1 N + 36βxη2σ2 1 N λ2 + 36βxη2σ2 1 N λ2
+ 9600βyη2σ2 1 N (L2 f + L2 g,1) µ2 + 9600βyη2σ2 1 N λ2 (L2 f + L2 g,1) µ2 + 9600βzη2σ2 1 N λ2 (L2 f + L2 g,1) µ2 . (132)
According to Lemma 4.7 and Eq. (129), to achieve the ϵ-accuracy solution where ϵ ∈ (0, 1), we can set
λ = O
 κ3
ϵ

,
βx = O
 1
N

, βy = O
 1
N

, βz = O
 1
N

,

αx = O
 1
λκ3

= O
 ϵ
κ6

, αy = O
 1
λκ

= O
 ϵ
κ4

, αz = O
 1
λκ

= O
 ϵ
κ4

,
η = O
 N ϵ2
κ4

, p= O
 κ
N ϵ

, B= O
 κ6
N ϵ3

, T= O
 κ10
N ϵ5

. (133)
Then, by initializing y0 and z0 such that E[∥y0 − y∗ λ(x0)∥2] ≤ O(ϵ2) and E[∥z0 − y∗(x0)∥2] ≤ O(ϵ2), it is easy to know that
1
T
T −1X
t=0
E[∥∇L(¯xt)∥2]
≤ O

ϵ2 E[L∗ λ(¯x0)] + O  κ2ϵ3 + O  κ2ϵ3
+ O

ϵ2 + O  ϵ4
κ8

σ2 + O
 ϵ2
κ2

σ2 + O
 ϵ4
κ6

σ2 + O  ϵ2 σ2 + O  ϵ2 σ2
+ 4
"
O
 1
κ4

+ O (1) + O (1) + O
 ϵ2
κ10

+ O
 ϵ2
κ6

+ O
 ϵ2
κ6
 #
×

O
 ϵ4
κ8

δ2 + O
 ϵ4
κ8

δ2 + O
 ϵ4
κ8

δ2 + O
 ϵ4
κ8

δ2σ2 + O
 ϵ4
κ8

δ2σ2 + O
 ϵ4
κ8

δ2σ2

+ O
 ϵ4
κ8

σ2 + O
 ϵ2
κ2

σ2 + O
 ϵ2
κ2

σ2 + O
 ϵ4
κ6

σ2 + O  ϵ2 σ2 + O  ϵ2 σ2 , (134)
which indicates
1
T
T −1X
t=0
E[∥∇L(¯xt)∥2] ≤ O  ϵ2 . (135)
