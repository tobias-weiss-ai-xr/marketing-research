---
title: Accelerating Optimization and Machine Learning through Decentralization
url: https://arxiv.org/abs/2604.19518
category: ai-marketing
subcategory: measurement
date: 2026-04
venue: ''
authors:
- Ziqin Chen
- Zuang Wang
- Yongqiang Wang
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.19518
pages: 18
chars: 69397
fetched_at: '2026-11-08T13:27:26+00:00'
kb_version: 1
---

# Accelerating Optimization and Machine Learning through Decentralization

Accelerating Optimization and Machine Learning
through Decentralization
Ziqin Chen†
Clemson University
ziqinc@g.clemson.edu
Zuang Wang†
Clemson University
zuangw@clemson.edu
Yongqiang Wang∗
Clemson University
yongqiw@clemson.edu
Abstract
Decentralized optimization enables multiple devices to learn a global machine
learning model while each individual device only has access to its local dataset. By
avoiding the need for training data to leave individual users’ devices, it enhances
privacy and scalability compared to conventional centralized learning, where all
data has to be aggregated to a central server. However, decentralized optimization
has traditionally been viewed as a necessary compromise, used only when central-
ized processing is impractical due to communication constraints or data privacy
concerns. In this study, we show that decentralization can paradoxically accelerate
convergence, outperforming centralized methods in the number of iterations needed
to reach optimal solutions. Through examples in logistic regression and neural
network training, we demonstrate that distributing data and computation across
multiple agents can lead to faster learning than centralized approaches—even when
each iteration is assumed to take the same amount of time, whether performed
centrally on the full dataset or decentrally on local subsets. This finding challenges
longstanding assumptions and reveals decentralization as a strategic advantage,
offering new opportunities for more efficient optimization and machine learning.
1 Introduction
We focus on the fundamental task of mathematical optimization—the process of iteratively refining a
solution to minimize a loss function with respect to a given metric. In typical application domains
such as machine learning and operations research, the loss is usually defined on a large number of
samples or measurements collected from multiple locations [1]. For example, the development of
machine learning based disease classifiers needs a large amount of training data to ensure accuracy
and minimize bias [2, 3, 4]. In sensor network based environment, sensing and climate monitoring, a
sufficient amount of measurement data is needed to suppress the noise inherent in low-cost sensors
[5, 6]. Although a natural approach to learning on such data is to aggregate everything on a central
server and train a model directly, limitations in computational and storage capacity on individual
devices have led to growing interest in decentralized learning methods. These methods are uniquely
suited to handle the rapid growth in data volume and model complexity in modern training tasks
[7, 8]. Moreover, training data may sometimes involve sensitive information, such as medical records,
and legislation may prohibit aggregating data from distributed sources like hospitals [ 2]. In such
cases, decentralized learning becomes the only viable option.
∗Corresponding author
†These authors contributed equally to this work
Preprint.
arXiv:2604.19518v1  [cs.LG]  21 Apr 2026

In the past decade, substantial progress has been made towards developing efficient decentralized
machine learning algorithms, both in the fully decentralized server-free case (which is also called
consensus optimization [ 9, 10, 8]) and the parameter-server assisted case (which is also called
federated optimization [11, 12] or cloud-based optimization [13]). However, it is generally believed
that such decentralized learning cannot match the performance of its centralized counterpart, where a
powerful server performs computation directly on aggregated data. (It is important to note that the
commonly cited “linear speedup” in distributed optimization with an increasing number of computing
devices, as shown by [14] and [15], assumes that each device has fixed computing power, so that
adding more devices effectively increases total computational capacity. This assumption is orthogonal
to our setting, where the central server has computing power equivalent to the combined capacity of
all distributed devices.) In this paper, we challenge this widely held belief and demonstrate—both
theoretically and empirically—that decentralization can accelerate optimization by reducing the
number of iterations required compared to centralized methods.
To establish this claim on firm theoretical grounds, we leverage and extend the performance estimation
problem (PEP) framework [ 16]. We stress that ourPEP-based results are formally valid and
mathematically rigorous, as they characterize the exact worst-case performance of optimization
algorithms overa prescribed function class[ 16]. This stands in contrast to conventional analyses,
which typically rely on analytical upper bounds that may be loose, overly conservative, or even
misleading [17]. Moreover, it is fundamentally distinct from numerical simulations on specific
function instances, as it provides guarantees that hold uniformly acrossthe entire function class.
2 Problem statement and context
2.1 Preliminaries
Definition 1(Strong Convexity).A function f:R d →R is strongly convex if there exists a constant
µ >0 such that for all x, y∈R d, the following inequality holds: f(y)≥f(x) +∇f(x) ⊤(y−x) +
µ
2 ∥y−x∥ 2.
Definition 2(Lipschitz Smoothness).A function f:R d →R is Lipschitz smooth with constant
L >0if for allx, y∈R d, the following inequality holds:∥∇f(x)− ∇f(y)∥ ≤L∥x−y∥.
2.2 Optimization problem
Let D={ξ 1, ξ2,· · ·, ξ|D|} represent a set of data samples with ξi denoting the ith data sample and
|D| denoting the size of the dataset. Then, most optimization or machine learning tasks on the dataset
Dcan be mathematically formulated as the following problem:
min
x∈X
f(x) := 1 |D|
|D|X
i=1
ℓ(x, ξi),(1)
where X denotes the set of all models/solutions that are of interest, ℓ denotes the loss function, and
ℓ(x, ξi) represents the loss of a model x evaluated on data sample ξi. For example, in the popular
empirical risk minimization problem [ 18], ξi is of the form of (ai, bi) with ai denoting the input
(feature) and bi denoting the output (label). A model x predicts an output x(ai) and the precision of
this prediction is measured by the loss ℓ(x, ξi) =ℓ(x,(a i, bi)). Commonly used models x include
linear/logistic regression models and neural networks. And commonly used examples of the loss
function include cross-entropy functions, Kullback–Leibler (KL) divergence, regression functions,
and many others [19].
2.3 Optimization algorithms
To solve problem (1), many algorithms have been proposed, including gradient descent methods
(e.g., [20, 21]), distributed ADMM (e.g., [22]), Newton’s methods (e.g., [23]), and many others. We
focus on gradient methods, as they—and their stochastic variants—are among the most widely used
techniques and are widely regarded as the primary workhorse and cornerstone for training modern
neural networks, as shown in [24]. The standard gradient descent method takes the following form:
xk+1 =x k −αg k,(2)
2

where xk denotes the model value in the kth iteration, α is the step size, and gk denotes the gradient
evaluated at xk. In machine learning applications, usually a stochastic estimate of the gradient (based
on mini-batch sampling of available data) is employed. When the objective function is convex and
L-smooth, i.e., there is a constant L such that ∥g(x)−g(x ′)∥ ≤L∥x−x′∥ holds for all x, x′ ∈ X,
it is well known that a stepsize 1 L gives guaranteed convergence to an optimal solution.
Recent years have also witnessed the development of numerous decentralized gradient methods that
enable multiple devices to learn a common optimal solution while each device can only have access
to a subset of the total dataset (see, e.g., [25, 10, 26, 27, 28, 29, 30]). In these studies, the objective
function is usually assumed to be of a form f(x) = PN i=1 fi(x) with N denoting the number of participating devices and fi(x) denoting the loss of the subset of data only accessible to device
i. There are two commonly studied decentralized gradient methods: server-assisted decentralized
gradient methods (see, e.g., [11, 30, 31]) and server-free decentralized gradient methods (see, e.g.,
[25, 32]). In the former method, a central server is responsible for updating the optimization variable,
while each participating device i is only tasked with computing gradients gk i based on its local
function fi and the variable x received from the server. In this case, the update usually takes the
form xk+1 =x k −α
PN
i=1 gk i
N . In the latter, server-free case, each participating agent maintains a local copy of x, denoted xi. Each device updates its local copy xi based on information received
from its neighbors and its local gradient gi. Assuming that device j shares wij(xk j −αg k j ) at the kth
iteration to its neighbors with wij ≥0 denoting the influence of device j on device i, the update
of every device i takes the form xk+1 i = PN j=1 wij(xk j −αg k j ). It is worth noting that when the
coupling coefficient wij is set to 1 N for all 1≤i, j≤N , the dynamics of the server-free decentralized optimization become equivalent to those of the server-assisted case when the initial values of all
devices (i.e.,x 0 i for alli) are set as the same value.
It is worth noting that although those distributed versions of gradient methods allow (1) to be solved
in a distributed manner with each participating device only having a subset of the total data, they
generally require more iterations to reach a given accuracy level (or, at best, perform on par) compared
to their centralized counterparts, in which a single device performs gradient descent on the full dataset.
Algorithm 1
1: Initialization: x0, step size αi = 1 Li for device i, switching threshold ϵ >0, switching state S=F.
2:fork= 1,· · ·, Kdo
3:if∥ PN i=1 αigk i ∥ ≤ϵandS=Fthen
4:SetS=Tand resetα i = 1 L withL=
PN
i=1 Li
N ;
5:end if
6: Each device receives xk−1 from the server, computes gk−1 i , and then sends it back to the
server;
7:The server updates
xk =x k−1 −
PN
i=1 αigk−1 i
N ;
8:end for
3 Decentralization approach and theoretical performance evaluation
3.1 Decentralization approach
When data are generated across different devices and locations, a natural approach to solving
optimization problem (1) is to aggregate all data on a central server and then apply a centralized
optimization method, such as the centralized gradient method. In fact, since data collected from
different locations often exhibit heterogeneous distributions—for example, facial images captured
by cameras tend to reflect the demographics of each location, and images of kangaroos are typically
collected only from cameras in Australia or zoos [33]—this heterogeneity poses a significant challenge
to decentralized learning algorithms [33]. Consequently, it is widely believed that aggregating all
datasets and performing learning centrally is a more desirable approach. However, we argue that
3

when local devices possess computing capabilities, retaining data on the devices and solving the
problem in (1) via decentralized optimization can lead to faster convergence—especially in cases
where the data distribution is skewed across devices. More specifically, we demonstrate that when
data across different devices follow heterogeneous distributions, the local geometric properties of
these datasets can be leveraged to accelerate optimization by reducing the number of iterations needed
for solving (1).
Our key idea for exploiting the local geometry of individual objective functions is to employ a
server-assisted decentralized optimization algorithm, where each device uses a local step size tailored
to the smoothness constant of its own dataset. Specifically, represent the dataset on device i as Di.
Then device i’s local loss function is given by fi(x) := 1 |Di| P|Di| j=1 ℓ(x, ξj) and we can obtain its
local smoothness constant Li and set its local step size as 1 Li . Note that the definition of the loss
function f(·) in (1), which is the average over all data samples, implies L=
PN
i=1 |Di|LiPN
i=1 |Di| (which
reduces to L=
PN
i=1 Li
N when the sizes of datasets |Di| are equal). Of course, with each device i
using a heterogeneous step size 1 Li , different devices’ gradients are weighted unevenly in the update of x, which will result in a deviation from the original optimal solution [34]. To mitigate the resulting
optimization errors, we propose switching from heterogeneous step sizes to a universal step size,
1
L, once convergence plateaus under the heterogeneous step size regime. This strategy can ensure convergence to an exact optimal solution (as confirmed by our theoretical evaluation in Fig. 1). The
detailed algorithm is summarized in Algorithm 1.
It is worth noting that even when the data are already centralized on a server, this approach can still
be applied by intentionally partitioning the data in a non-uniform manner—for example, by dividing
it according to data labels.
GD
Algorithm 1 (switch time 12)
Algorithm 1 (switch time 10)
Algorithm 1 (switch time 8)
DGD (𝛼ൌ 1/𝐿௜)
𝑓𝑥௞െ𝑓 ሺ 𝑥∗ሻ
10ିଶ
10ିଵ
10଴
10ଵ
48 1 2 16 20 24 28
Iterations
1.1
1.0
0.9
0.8
0.7
0
2
4
6
8
161412108642
Errorୈୋୈ/Errorୋୈ
048 1 2 16 20
10ିଵ.ସ
10ିଵ
10ି଴.ସ
10଴.ଶ
10଴
10ି଴.ଶ
10ି଴.଺
10ି଴.଼
10ିଵ.ଶ
Errorୈୋୈ/Errorୋୈ
Iterations
(𝐿ଵ,𝐿ଶ) = (1,1)
(𝐿ଵ,𝐿ଶ) = (1.5,0.5)
(𝐿ଵ,𝐿ଶ) = (1.6,0.4)
(𝐿ଵ,𝐿ଶ) = (1.7,0.3)
(𝐿ଵ,𝐿ଶ) = (1.8,0.2)
(a)
GD
Algorithm 1 (switch time 12)
Algorithm 1 (switch time 10)
Algorithm 1 (switch time 8)
DGD (𝛼ൌ 1/𝐿௜)
𝑓𝑥௞െ𝑓 ሺ 𝑥∗ሻ
10ିଶ
10ିଵ
10଴
10ଵ
48 1 2 16 20 24 28
Iterations
1.1
1.0
0.9
0.8
0.7
0
2
4
6
8
161412108642
Errorୈୋୈ/Errorୋୈ
048 1 2 16 20
10ିଵ.ସ
10ିଵ
10ି଴.ସ
10଴.ଶ
10଴
10ି଴.ଶ
10ି଴.଺
10ି଴.଼
10ିଵ.ଶ
Errorୈୋୈ/Errorୋୈ
Iterations
(𝐿ଵ,𝐿ଶ) = (1,1)
(𝐿ଵ,𝐿ଶ) = (1.5,0.5)
(𝐿ଵ,𝐿ଶ) = (1.6,0.4)
(𝐿ଵ,𝐿ଶ) = (1.7,0.3)
(𝐿ଵ,𝐿ଶ) = (1.8,0.2) (b)
GD
Algorithm 1 (switch time 12)
Algorithm 1 (switch time 10)
Algorithm 1 (switch time 8)
DGD (𝛼ൌ 1/𝐿௜)
𝑓𝑥௞െ𝑓 ሺ 𝑥∗ሻ
10ିଶ
10ିଵ
10଴
10ଵ
48 1 2 16 20 24 28
Iterations
1.1
1.0
0.9
0.8
0.7
0
2
4
6
8
161412108642
Errorୈୋୈ/Errorୋୈ
048 1 2 16 20
10ିଵ.ସ
10ିଵ
10ି଴.ସ
10଴.ଶ
10଴
10ି଴.ଶ
10ି଴.଺
10ି଴.଼
10ିଵ.ଶ
Errorୈୋୈ/Errorୋୈ
Iterations
(𝐿ଵ,𝐿ଶ) = (1,1)
(𝐿ଵ,𝐿ଶ) = (1.5,0.5)
(𝐿ଵ,𝐿ଶ) = (1.6,0.4)
(𝐿ଵ,𝐿ଶ) = (1.7,0.3)
(𝐿ଵ,𝐿ଶ) = (1.8,0.2) (c)
Figure 1: Performance comparison of Algorithm 1 with its centralized counterpart (GD) using PEP
based theoretical analysis. (a) shows the acceleration of Algorithm 1 (results under three switch time
instants are given, represented by three red curves with varying shades) over its centralized counterpart
(termed GD and represented by the blue curve). The centralized approach uses a step size 1 L with
L= 1 N PN i=1 Li. The gray curve represents the performance of the conventional decentralized
gradient descent (termed DGD) algorithm with local step sizes, i.e., agent i using a step size 1 Li , which is subject to a steady-state error. In this subplot, we consider two agents with heterogeneous
local smoothness constants L1 = 1 3 and L2 = 3 . (b) demonstrates that a greater heterogeneity between L1 and L2 leads to more acceleration via decentralization. The y-axis represents the ratio
of optimization errors obtained by PEP under Algorithm 1 and GD. A ratio less than 1 indicates
Algorithm 1 gaining acceleration over its centralized counterpart. (c) considers the more than two-
agent setting with half of the agents having a smoothness constant of 1 3, whereas the other half have a smoothness constant of3. The strongly convex parameter is set toµ= 0.1.
3.2 Theoretical evaluation
Recently, a framework known as the Performance Estimation Problem (PEP) [35, 16] was introduced
to precisely characterize the theoretical worst-case performance of optimization algorithms. In
contrast to traditional asymptotic analyses, which often provide conservative or loose guarantees [17],
PEP yields exact performance bounds for algorithms over specified function classes.
4

To describe the PEP framework, we first define the augmented states as xk = [xk 1, xk 2, . . . , xk N ]∈
Rd×N , where the superscript k belongs to the index set IK ={0, . . . , K}. Similarly, we
define the augmented local optimum and global optimum as x⋆ = [x ⋆ 1, x ⋆ 2, . . . , x⋆ N ] and
x∗ = [x ∗ 1, x∗ 2, . . . , x∗ N ], respectively (where x∗ 1 =x ∗ 2 =· · ·=x∗ N will be enforced in the
PEP formulation). To simplify notation, we extend the index set IK for augmented states to include
these two optimal states, defining the augmented index set asI ⋆,∗ K ={0, . . . , K, ⋆,∗}.
In a similar manner, we define the augmented gradients and function values as
gk = [gk 1 , gk 2 , . . . , gk N ]∈R d×N , f k = [f k 1 , fk 2 , . . . , fk N ]∈R N ,fork∈I ⋆,∗ K .
We use Fµ,L to denote the class of functions such that each f∈ Fµ,L is µ-strongly convex and
L-smooth.
Under these definitions and denoting S+ as the set of all symmetric positive semidefinite matrices,
we have
P= [x 0, g0, g1, . . . , gK, g⋆, g∗, x⋆, x∗]∈R d×[(K+6)N] ,
G=P ⊤P∈S ((K+6)N)×((K+6)N) + , F= [f 0, f1, . . . , fK, f⋆, f∗]∈R 1×(K+3)N ,
which allows us to formulate the PEP as:
max
x0, g0, g1, ..., gK ,
g⋆, g∗,x⋆, x∗
f(¯xK)−f(x ∗)
s.t.{x k i , gk i , fk i }, k∈I ⋆,∗ K are interpolated for each local function classF µi,Li ,
{xk i }i∈[N], k∈IK ,¯xKare generated recursively by algorithm 1 andx k 1 =x k i ,∀i∈[N], k∈I K,
1
N
NX
i=1
g∗ i = 1 N
NX
i=1
∇fi(x∗) = 0,such thatx ∗ is the global optimum andx ∗ 1 =x ∗ i ,∀i∈[N],
g⋆ i =∇f i(x⋆ i ) = 0,∀i∈[N],such thatx ⋆ i is the local optimum forf i,
∥x0 i −x ∗∥2 ≤R 2 0,∀i∈[N],∥x ⋆ i −x ∗∥2 ≤R 2 ∗,∀i∈[N].
The last two constraints are standard in the PEP literature. The PEP formulation above can be
transformed into anequivalentsemidefinite programming (SDP) problem, which is convex and can
therefore be solved efficiently. As long as the condition dim(G)≤d holds, theexactworst-case
optimization error afterKiterations of Algorithm 1 is equal to the optimal value of this SDP.
This equivalence implies that for the given function class, there exists a specific function on which
Algorithm 1 achieves precisely the worst-case error predicted by the PEP. Moreover, no function
in the class can lead to a larger error under the same algorithm. A more detailed derivation of this
formulation, along with its final SDP representation, is provided in theAppendix.
To efficiently solve the resulting SDPs arising from the PEP formulation, we utilize the JuMP
modeling language in Julia. JuMP [ 36] offers a flexible and high-level interface for formulating
convex optimization problems, including SDPs, and facilitates seamless integration with state-of-
the-art solvers. For this work, we employ the MOSEK solver [ 37], which is well-suited for large-
scale and structured convex optimization problems, particularly semidefinite and conic programs.
This combination enables us to model and solve the PEP instances accurately and efficiently. All
experiments are conducted on a computing platform equipped with dual AMD EPYC 9654 processors
(each with 96 cores) and 256 GB of RAM.
Using this approach, we rigorously compare the performance of the proposed Algorithm 1 with its
centralized counterpart, i.e., the update rule in (2). Without loss of generality, we first consider a
dataset composed of N= 2 types of data samples. In this case, we have f(x) = 1 2 P2 i=1 fi(x). We assume that the data distributions are heterogeneous and hence f1 and f2 have different smoothness
properties (e.g., L1 = 1 3 and L2 = 3). The results are summarized in Fig. 1(a). It is evident that Algorithm 1 can significantly reduce the number of iterations required to achieve a given accuracy
level, compared to its centralized counterpart (denoted as “GD”). It is worth noting that although we
leverage local geometry—captured by the local smoothness constants Li—to accelerate convergence,
directly applying this strategy to existing decentralized gradient methods is not viable, as it leads
5

to a steady-state error (see the result represented by the black curve in Fig. 1(a)). This highlights
the necessity and significance of our proposed design. Moreover, to assess the impact of switching
timing in Algorithm 1, we present results for three different switching points, represented by the three
curves with varying shades of red in Fig. 1(a). In all cases, Algorithm 1 achieves faster convergence
than the centralized counterpart, demonstrating that its performance is not sensitive to the choice of
switching timing.
Theorem 1.(Convergence Acceleration of Algorithm 1) Consider the optimization problem defined
in (1), where the function f belongs to the class Fµ,L, characterized by the smoothness parameter
L and strong convexity parameter µ. Let A1 denote Algorithm 1 with local step sizes 1 Li , and Ac
denote centralized gradient descent with a uniform step size 1 L. For the performance metric
PA = max f∈F µ,L
(
1
N
NX
i=1
||xk i,A −x ∗||2
)
,
which measures the worst-case optimization error at iteration k over all f∈ Fµ,L, we consider the
ratio PA1 /PAc as the relative acceleration of Algorithm 1 compared with centralized gradient descent
(with values below 1 indicating acceleration and smaller ratios indicating stronger acceleration).
Figure 1(b) gives the exact ratio values under different function classes, and the ratio values being
strictly less than 1 for all tested function classes Fµ,L in the heterogeneous setting confirm that
Algorithm 1 with local step sizes achieves a strictly faster convergence rate than centralized gradient
descent under all considered function classes.
Proof.See Appendix A.2.
To examine how the difference between the smoothness constants L1 and L2 influences the ac-
celeration achieved by Algorithm 1 over its centralized counterpart, we compute the ratio of the
optimization error of Algorithm 1 to that of the centralized method across various values of the
smoothness constants. As presented in Theorem 1, a ratio smaller than one clearly indicates that
Algorithm 1 outperforms its centralized counterpart, with smaller ratios corresponding to greater
acceleration. Fig. 1(b) presents the comparison results when Algorithm 1 is under different (L1, L2)
pairs with a fixed sum. Note that for all such pairs, the centralized counterpart has a fixed smoothness
constant of L= L1+L2 2 = 1. The results indicate that a larger difference between the smoothness constants—which corresponds to greater heterogeneity in the data distributions across the two de-
vices—yields greater acceleration of Algorithm 1 over its centralized counterpart. In Fig. 1(c), we
evaluate the influence of the number of devices on this acceleration. The results clearly show that the
acceleration remains essentially unchanged regardless of the number of devices involved.
4 Experimental results
In this section, we present three experiments on benchmark datasets to validate the finding that
decentralization can indeed reduce the number of iterations required to reach an optimal solution†.
Additional results on the MNIST dataset and ablation studies are presented in the Appendix B.
4.1 Logistic regression based Web categorization
In this experiment, we consider a logistic regression categorization task using the W8A dataset [38].
In the dataset, each entry contains one feature and one label. The feature is a vector of 300 sparse
keyword attributes extracted from each web page, and the label indicates the category of the entry
[39]. We consider a logistic regression model for the data, where the local loss function is given by
the following function:
fi(x) = 1 m
mX
j=1
log

1 + exp(−bjaT j x)  + µ 2 ∥x∥2 2,(3)
where aj ∈R 300 denotes the feature of the jth data entry, bj ∈ {−1,1}denotes its label and m
denotes the number of data samples.
†Code available athttps://anonymous.4open.science/r/Acc-ML-via-Decentral-050D/README.md
6

Iterations
GD
Algorithm 1 (by eigenvalues)
Algorithm 1 (by norms)
Algorithm 1 (by labels)
0 200 400 600 800
0Smoothness Constant
Device Index
Dଵ Dଶ C Dଵ Dଶ C Dଵ Dଶ C
1
2
3
4
5
By
labels
By
norms
By
eigen-
values
Gradient Norm
10ିଵ
10ି଴.଼
10଴
10ି଴.଺
10ି଴.ସ
10ି଴.ଶ
10ଷ.ଷ
10ଷ.ହ
10ସ.ଷ
10ଷ.଻
10ଷ.ଽ
10ସ.ଵ
Loss
0 200 400 600 800
Iterations
GD
Algorithm 1 (by eigenvalues)
Algorithm 1 (by norms)
Algorithm 1 (by labels)
(a)
Iterations
GD
Algorithm 1 (by eigenvalues)
Algorithm 1 (by norms)
Algorithm 1 (by labels)
0 200 400 600 800
0Smoothness Constant
Device Index
Dଵ Dଶ C Dଵ Dଶ C Dଵ Dଶ C
1
2
3
4
5
By
labels
By
norms
By
eigen-
values
Gradient Norm
10ିଵ
10ି଴.଼
10଴
10ି଴.଺
10ି଴.ସ
10ି଴.ଶ
10ଷ.ଷ
10ଷ.ହ
10ସ.ଷ
10ଷ.଻
10ଷ.ଽ
10ସ.ଵ
Loss
0 200 400 600 800
Iterations
GD
Algorithm 1 (by eigenvalues)
Algorithm 1 (by norms)
Algorithm 1 (by labels) (b)
Iterations
GD
Algorithm 1 (by eigenvalues)
Algorithm 1 (by norms)
Algorithm 1 (by labels)
0 200 400 600 800
0Smoothness Constant
Device Index
Dଵ Dଶ C Dଵ Dଶ C Dଵ Dଶ C
1
2
3
4
5
By
labels
By
norms
By
eigen-
values
Gradient Norm
10ିଵ
10ି଴.଼
10଴
10ି଴.଺
10ି଴.ସ
10ି଴.ଶ
10ଷ.ଷ
10ଷ.ହ
10ସ.ଷ
10ଷ.଻
10ଷ.ଽ
10ସ.ଵ
Loss
0 200 400 600 800
Iterations
GD
Algorithm 1 (by eigenvalues)
Algorithm 1 (by norms)
Algorithm 1 (by labels) (c)
Figure 2: Comparison of Algorithm 1 with its centralized counterpart (labeled GD) using the
W8A dataset. (a) and (c) compare the convergence performance between the centralized approach
(labeled GD) and our proposed decentralized method under three partitioning schemes for the entire
data, labeled Algorithm 1 (by labels), Algorithm 1 (by norms), and Algorithm 1 (by eigenvalues),
respectively. The results show that in all data partitioning schemes, using decentralization substantially
reduces the number of iterations required to reach a certain accuracy level. (b) plots the resulting
smoothness constants under the three partitioning schemes, respectively, where on the x-axis, “C”
represents the smoothness constant of the entire dataset (used in the centralized case), and “D1” and
“D2” represent the smoothness constants for device 1 and device 2, respectively.
In the experiment, we compare our decentralized optimization approach to (3) (i.e., Algorithm 1)
and its centralized counterpart (see update rule in (2)). Based on our results in Section 3.2, greater
heterogeneity in data distributions leads to increased acceleration of Algorithm 1. Therefore, we
consider three data partitioning schemes that produce heterogeneous data distributions. In the first
partitioning scheme, we split the data into two groups based on their label values: all entries with
label “1” are assigned to one device, while all entries with label “ −1” are assigned to the other
device. In the second partitioning scheme, we sort all data entries based on the norm of the feature
vector ∥aj∥ and assign the smaller half to device 1, while the larger half is assigned to device 2. In
the third partitioning scheme, we order the data entries according to the maximum eigenvalue of
ajaT j and allocate the smaller half to device 1 and the remainder to device 2. Since the smoothness
constants are determined by the Hessian matrix—which is directly influenced by the factors used
in the three partitioning schemes—the two devices have different smoothness constants in all cases.
In the decentralized case, we run a centralized gradient descent (labeled as GD) with the gradient
calculated from all data entries without any partitioning. The comparison results are summarized in
Fig. 2. It is clear that decentralization can indeed significantly enhance convergence speed.
4.2 Image classification on CIFAR-10
In this experiment, we train a deep neural network on the CIFAR-10 dataset [40], which offers greater
diversity and complexity compared to the MNIST dataset. The CIFAR-10 dataset consists of 60,000
color images of size 32×32 pixels, divided into 10 classes. Each class contains 6,000 images,
with 5,000 allocated for training and 1,000 for testing. In this experiment, we employ a four-level
CNN–based classifier. The architecture consists of four convolutional layers with 32, 64, 128, and
128 filters, respectively. Max pooling layers are applied after the second and fourth convolutional
layers. Finally, the network includes a global average pooling layer and a fully connected dense layer
that maps the extracted features to 10 output classes. In our implementation of the decentralized
Algorithm 1, we partition the entire dataset across ten devices based on labels—that is, all data
entries with the same label are assigned to the same device. Similar to the previous experiment,
we used a small number of samples to estimate the smoothness constant for each device. However,
instead of using full-batch gradient computation, we employ mini-batch based gradient computation,
which only uses a few training samples at an iteration. To ensure a fair comparison, in Algorithm 1,
each device selects a single random sample for gradient computation in each iteration, while the
centralized approach selects 10 random samples per iteration. In this way, both algorithms process
the same total number of samples in each iteration. The results are summarized in Fig. 3. It is
evident that decentralization can substantially reduce the number of iterations required to reach an
7

optimal solution. It is worth noting that the experiment was conducted multiple times using different
smoothness constants, each estimated from distinct subsets of data (see Fig. 3(c) for three instances
of estimated smoothness constants). Despite variations in these estimates, the results consistently
demonstrate that decentralization achieves clear acceleration compared to the centralized case.
Training Loss
1.0
1.5
2.0
2.5
Epochs
Epochs
1.0
1.5
2.0
2.5 Training Loss
Epochs
1.0
1.5
2.0
2.5 Training Loss
Expr. 10.0
0.5
1.0
1.5 Training Loss
Experiment Numbers
GD (mini batch) Algorithm 1 (mini batch)
0.9075
1.0868 1.0687
0.9208
1.2462
1.0519
1.1884
0.9805
1.1977
1.0460
1.2839
1.0886
1.1373
0.9417
1.1505
0.9505
Smoothness Constant
Expr. 4
Expr. 8
Expr. 2 Expr. 3 Expr. 4 Expr. 5 Expr. 6 Expr. 7 Expr. 8
Training Loss
1.0
1.5
2.0
2.5
3.0
Epochs
GD (mini batch)
Algorithm 1 (mini batch)
0 25 50 75 100 125 150
0 25 50 75 100 120 150
0 25 50 75 100 120 150
0 25 50 75 100 120 150
Device Index
Algorithm 1 (mini batch)GD (mini batch)
Expr. 1
350
400
450
500
550
Expr. 1
Device Index
Expr. 4
350
400
450
500
300
Device Index
Expr. 8
400
450
500
550
350
1.0
0.9
0.8
0.7
0.6
0.5
0.4
0.3
Training Accuracy
Epochs
0 25 50 75 100 125 150
GD (mini batch)
Algorithm 1 (mini batch)
Test Accuracy
Epochs
0.60
0.45
0.48
0.51
0.54
0.57
0.63
0 25 50 75 100 125 150
GD (mini batch)
Algorithm 1 (mini batch)
Dଵ Dଶ Dଷ Dସ Dହ D଺ D଻ D଼ Dଽ Dଵ଴C
Dଵ Dଶ Dଷ Dସ Dହ D଺ D଻ D଼ Dଽ Dଵ଴C
Dଵ Dଶ Dଷ Dସ Dହ D଺ D଻ D଼ Dଽ Dଵ଴C
Smoothness Constant Smoothness Constant
(a)
Training Loss
1.0
1.5
2.0
2.5
Epochs
Epochs
1.0
1.5
2.0
2.5 Training Loss
Epochs
1.0
1.5
2.0
2.5 Training Loss
Expr. 10.0
0.5
1.0
1.5 Training Loss
Experiment Numbers
GD (mini batch) Algorithm 1 (mini batch)
0.9075
1.0868 1.0687
0.9208
1.2462
1.0519
1.1884
0.9805
1.1977
1.0460
1.2839
1.0886
1.1373
0.9417
1.1505
0.9505
Smoothness Constant
Expr. 4
Expr. 8
Expr. 2 Expr. 3 Expr. 4 Expr. 5 Expr. 6 Expr. 7 Expr. 8
Training Loss
1.0
1.5
2.0
2.5
3.0
Epochs
GD (mini batch)
Algorithm 1 (mini batch)
0 25 50 75 100 125 150
0 25 50 75 100 120 150
0 25 50 75 100 120 150
0 25 50 75 100 120 150
Device Index
Algorithm 1 (mini batch)GD (mini batch)
Expr. 1
350
400
450
500
550
Expr. 1
Device Index
Expr. 4
350
400
450
500
300
Device Index
Expr. 8
400
450
500
550
350
1.0
0.9
0.8
0.7
0.6
0.5
0.4
0.3
Training Accuracy
Epochs
0 25 50 75 100 125 150
GD (mini batch)
Algorithm 1 (mini batch)
Test Accuracy
Epochs
0.60
0.45
0.48
0.51
0.54
0.57
0.63
0 25 50 75 100 125 150
GD (mini batch)
Algorithm 1 (mini batch)
Dଵ Dଶ Dଷ Dସ Dହ D଺ D଻ D଼ Dଽ Dଵ଴C
Dଵ Dଶ Dଷ Dସ Dହ D଺ D଻ D଼ Dଽ Dଵ଴C
Dଵ Dଶ Dଷ Dସ Dହ D଺ D଻ D଼ Dଽ Dଵ଴C
Smoothness Constant Smoothness Constant
(b)
Training Loss
1.0
1.5
2.0
2.5
Epochs
Epochs
1.0
1.5
2.0
2.5 Training Loss
Epochs
1.0
1.5
2.0
2.5 Training Loss
Expr. 10.0
0.5
1.0
1.5 Training Loss
Experiment Numbers
GD (mini batch) Algorithm 1 (mini batch)
0.9075
1.0868 1.0687
0.9208
1.2462
1.0519
1.1884
0.9805
1.1977
1.0460
1.2839
1.0886
1.1373
0.9417
1.1505
0.9505
Smoothness Constant
Expr. 4
Expr. 8
Expr. 2 Expr. 3 Expr. 4 Expr. 5 Expr. 6 Expr. 7 Expr. 8
Training Loss
1.0
1.5
2.0
2.5
3.0
Epochs
GD (mini batch)
Algorithm 1 (mini batch)
0 25 50 75 100 125 150
0 25 50 75 100 120 150
0 25 50 75 100 120 150
0 25 50 75 100 120 150
Device Index
Algorithm 1 (mini batch)GD (mini batch)
Expr. 1
350
400
450
500
550
Expr. 1
Device Index
Expr. 4
350
400
450
500
300
Device Index
Expr. 8
400
450
500
550
350
1.0
0.9
0.8
0.7
0.6
0.5
0.4
0.3
Training Accuracy
Epochs
0 25 50 75 100 125 150
GD (mini batch)
Algorithm 1 (mini batch)
Test Accuracy
Epochs
0.60
0.45
0.48
0.51
0.54
0.57
0.63
0 25 50 75 100 125 150
GD (mini batch)
Algorithm 1 (mini batch)
Dଵ Dଶ Dଷ Dସ Dହ D଺ D଻ D଼ Dଽ Dଵ଴C
Dଵ Dଶ Dଷ Dସ Dହ D଺ D଻ D଼ Dଽ Dଵ଴C
Dଵ Dଶ Dଷ Dସ Dହ D଺ D଻ D଼ Dଽ Dଵ଴C
Smoothness Constant Smoothness Constant (c)
Figure 3: Comparison of Algorithm 1 with its centralized counterpart (labeled GD) using the
CIFAR-10 dataset. In this experiment, both algorithms use mini-batch gradient computation: in
each iteration, the centralized approach processes ten randomly selected samples, while each device
in the decentralized approach computes gradients using one sample from the data allocated to it
(so both approaches process the same number of ten samples in each iteration). (a) shows that the
decentralized approach achieves faster convergence than the centralized counterpart in terms of
training loss, training accuracy, and test accuracy. (b) compares the training loss over eight runs with
different estimated smoothness constants and random initializations. (c) illustrates the estimated
smoothness constants alongside the training loss trajectories of three selected runs from the eight. On
the x-axis representing the device index, the label “C” denotes the centralized case, and “D1” through
“D10” represent the devices in the decentralized case.
4.3 Sentiment analysis on SST-2
In this experiment, we consider a BERT-based classifier for the Stanford Sentiment Treebank (SST-2)
dataset [41], a widely used benchmark for evaluating language-model fine-tuning in the field of
natural language processing [42]. SST-2 is a binary sentiment classification dataset with positive and
negative labels, containing a total of 67,349 training samples. We partition the training dataset across
five devices using a Dirichlet distribution with parameter 0.1, creating a high degree of label-based
heterogeneity among the devices. Our classifier employs a BERT-base encoder with a classification
head [43]. The BERT layers are frozen except for the last encoder layer, which is fine-tuned along
with the classification head to adapt the representations to the SST-2 task. Both centralized gradient
descent (GD) and our proposed Algorithm 1 are evaluated under this setup. Since the labels of the
test dataset are not publicly available, we evaluate the test accuracy on the validation dataset instead.
8

The results are summarized in Fig. 4. It is evident that our approach outperforms the centralized
baseline, achieving accelerated convergence in language-model fine-tuning.
Remark1.In logistic regression experiments, the smoothness constant Li for each client is computed
directly from the local Hessian matrix using its largest eigenvalue. In neural network training,
including CNN training and BERT fine-tuning, since a closed-form expression of Li is generally
unavailable, we estimate it numerically using a gradient difference approximation. Specifically, a
mini-batch of local data is fixed, and multiple model parametersx are randomly sampled from a region
that empirically covers typical parameter variations during training. For each sampled parameter,
a small perturbation ε is applied, and the ratio of gradient difference to parameter difference is
computed. This procedure is repeated tens of thousands of times, and then the maximal value of the
resulting ratios is taken as an estimate of the local smoothness constantL i.
(a) Training Loss
 (b) Training Accuracy
 (c) Test Accuracy
Figure 4: Comparison of Algorithm 1 with its centralized counterpart (labeled GD) on the SST-2
dataset. In this experiment, both algorithms use full-batch gradient computation: the centralized
approach processes the entire dataset, while in our decentralization based approach, each device
computes gradients using all the data allocated to it. (a)-(c) show that our approach converges faster
than the centralized counterpart.
5 Discussion and conclusion
Our finding—that decentralization can accelerate the convergence of optimization algorithms—is
surprising, but it carries significant implications. Faster convergence, meaning fewer iterations to
reach a satisfactory solution, is critical for meeting the timing constraints of real-time systems such
as autonomous vehicles. Additionally, reducing computational complexity is essential when training
large-scale neural networks. Our finding provides strong support for the development of decentralized
optimization algorithms—not only as a workaround when centralized approaches are infeasible due to
data aggregation constraints imposed by privacy regulations, but also as a more powerful alternative
when convergence speed is critical. Notably, our result was obtained under the assumption that the
centralized server possesses computational power equal to the combined capabilities of all devices in
the decentralized setup. This already gives the centralized approach an advantage in comparison. In
practice, however, decentralized systems can harness the aggregate computational power of multiple
devices, while a single centralized server remains inherently limited. A limitation of the current
study is that it does not account for communication overhead, which may become non-negligible in
settings where high-speed communication channels are unavailable. In fact, when data are distributed
across multiple locations, the communication overhead required to aggregate raw data for centralized
optimization is typically much greater than that incurred by exchanging optimization variables in
decentralized approaches. Therefore, we expect that a similar conclusion holds in this case and plan
to systematically investigate this problem in future work.
9

References
[1] Yann LeCun, Yoshua Bengio, and Geoffrey Hinton. Deep learning.Nature, 521(7553):436–444,
2015.
[2] Stefanie Warnat-Herresthal, Hartmut Schultze, Krishnaprasad Lingadahalli Shastry, Sathya-
narayanan Manamohan, Saikat Mukherjee, Vishesh Garg, Ravi Sarveswara, Kristian Händler,
Peter Pickkers, N Ahmad Aziz, et al. Swarm learning for decentralized and confidential clinical
machine learning.Nature, 594(7862):265–270, 2021.
[3] Joshua C Peterson, David D Bourgin, Mayank Agrawal, Daniel Reichman, and Thomas L
Griffiths. Using large-scale experiments and machine learning to discover theories of human
decision-making.Science, 372(6547):1209–1214, 2021.
[4] Hanchen Wang, Tianfan Fu, Yuanqi Du, Wenhao Gao, Kexin Huang, Ziming Liu, Payal
Chandak, Shengchao Liu, Peter Van Katwyk, Andreea Deac, et al. Scientific discovery in the
age of artificial intelligence.Nature, 620(7972):47–60, 2023.
[5] Vikram Iyer, Hans Gaensbauer, Thomas L Daniel, and Shyamnath Gollakota. Wind dispersal of
battery-free wireless devices.Nature, 603(7901):427–433, 2022.
[6] Tom Beucler, Pierre Gentine, Janni Yuval, Ankitesh Gupta, Liran Peng, Jerry Lin, Sungduk
Yu, Stephan Rasp, Fiaz Ahmed, Paul A O’Gorman, J. David Neelin, Nicholas J. Lutsko, and
Michael Pritchard. Climate-invariant machine learning.Science Advances, 10(6):eadj7250,
2024.
[7] Zhanhong Jiang, Aditya Balu, Chinmay Hegde, and Soumik Sarkar. Collaborative deep learning
in fixed topology networks.Advances in Neural Information Processing Systems, 30, 2017.
[8] Anastasia Koloskova, Tao Lin, Sebastian U Stich, and Martin Jaggi. Decentralized deep
learning with arbitrary communication compression. InInternational Conference on Learning
Representations, 2019.
[9] A. Nedic, A. Ozdaglar, and P. A. Parrilo. Constrained consensus and optimization in multi-agent
networks.IEEE Transactions on Automatic Control, 55(4):922–938, 2010.
[10] Wei Shi, Qing Ling, Gang Wu, and Wotao Yin. Extra: An exact first-order algorithm for
decentralized consensus optimization.SIAM Journal on Optimization, 25(2):944–966, 2015.
[11] Brendan McMahan, Eider Moore, Daniel Ramage, Seth Hampson, and Blaise Aguera y Arcas.
Communication-efficient learning of deep networks from decentralized data. InArtificial
Intelligence and Statistics, pages 1273–1282. PMLR, 2017.
[12] Peter Kairouz, H Brendan McMahan, Brendan Avent, Aurélien Bellet, Mehdi Bennis, Ar-
jun Nitin Bhagoji, Kallista Bonawitz, Zachary Charles, Graham Cormode, Rachel Cummings,
et al. Advances and open problems in federated learning.Foundations and Trends in Machine
Learning, 14(1–2):1–210, 2021.
[13] Angelia Nedi´c and Ji Liu. Distributed optimization for control.Annual Review of Control,
Robotics, and Autonomous Systems, 1(1):77–103, 2018.
[14] Xiangru Lian, Ce Zhang, Huan Zhang, Cho-Jui Hsieh, Wei Zhang, and Ji Liu. Can decentralized
algorithms outperform centralized algorithms? a case study for decentralized parallel stochastic
gradient descent.Advances in Neural Information Processing Systems, 30, 2017.
[15] Hao Yu, Rong Jin, and Sen Yang. On the linear speedup analysis of communication efficient
momentum sgd for distributed non-convex optimization. InInternational Conference on
Machine Learning, pages 7184–7193. PMLR, 2019.
[16] Adrien B Taylor, Julien M Hendrickx, and François Glineur. Smooth strongly convex interpo-
lation and exact worst-case performance of first-order methods.Mathematical Programming,
161:307–345, 2017.
[17] Erwan Meunier and Julien M Hendrickx. Several performance bounds on decentralized online
optimization are highly conservative and potentially misleading. InProc. IEEE 64th Conf.
Decis. Control, pages 6201–6207. IEEE, 2025.
[18] Vladimir Vapnik.Estimation of dependences based on empirical data. Springer Science &
Business Media, New York, 2006.
[19] Shai Shalev-Shwartz and Shai Ben-David.Understanding machine learning: From theory to
algorithms. Cambridge University Press, Cambridge, 2014.
10

[20] Dimitri P Bertsekas and John N Tsitsiklis. Gradient convergence in gradient methods with
errors.SIAM Journal on Optimization, 10(3):627–642, 2000.
[21] Yurii Nesterov.Introductory lectures on convex optimization: A basic course, volume 87.
Springer Science & Business Media, New York, 2013.
[22] Stephen Boyd, Neal Parikh, Eric Chu, Borja Peleato, Jonathan Eckstein, et al. Distributed opti-
mization and statistical learning via the alternating direction method of multipliers.Foundations
and Trends in Machine learning, 3(1):1–122, 2011.
[23] John E Dennis, Jr and Jorge J Moré. Quasi-newton methods, motivation and theory.SIAM
Review, 19(1):46–89, 1977.
[24] Mahmoud Assran, Nicolas Loizou, Nicolas Ballas, and Mike Rabbat. Stochastic gradient push
for distributed deep learning. InInternational Conference on Machine Learning, pages 344–353.
PMLR, 2019.
[25] Angelia Nedic and Asuman Ozdaglar. Distributed subgradient methods for multi-agent opti-
mization.IEEE Transactions on Automatic Control, 54(1):48–61, 2009.
[26] Paolo Di Lorenzo and Gesualdo Scutari. Distributed nonconvex optimization over networks. In
6th International Workshop on Computational Advances in Multi-Sensor Adaptive Processing
(CAMSAP), pages 229–232. IEEE, 2015.
[27] Angelia Nedic, Alex Olshevsky, and Wei Shi. Achieving geometric convergence for distributed
optimization over time-varying graphs.SIAM Journal on Optimization, 27(4):2597–2633, 2017.
[28] Guannan Qu and Na Li. Harnessing smoothness to accelerate distributed optimization.IEEE
Transactions on Control of Network Systems, 5(3):1245–1260, 2017.
[29] Jinming Xu, Shanying Zhu, Yeng Chai Soh, and Lihua Xie. Convergence of asynchronous
distributed gradient methods over stochastic networks.IEEE Transactions on Automatic Control,
63(2):434–448, 2017.
[30] Sai Praneeth Karimireddy, Satyen Kale, Mehryar Mohri, Sashank Reddi, Sebastian Stich, and
Ananda Theertha Suresh. Scaffold: Stochastic controlled averaging for federated learning. In
International Conference on Machine Learning, pages 5132–5143. PMLR, 2020.
[31] Ming Xiang, Stratis Ioannidis, Edmund Yeh, Carlee Joe-Wong, and Lili Su. Efficient federated
learning against heterogeneous and non-stationary client unavailability.Advances in Neural
Information Processing Systems, 37:104281–104328, 2024.
[32] Youssef Allouah, Anastasia Koloskova, Aymane El Firdoussi, Martin Jaggi, and Rachid Guer-
raoui. The privacy power of correlated noise in decentralized learning. InForty-first Interna-
tional Conference on Machine Learning, 2024.
[33] Kevin Hsieh, Amar Phanishayee, Onur Mutlu, and Phillip Gibbons. The non-iid data quagmire
of decentralized machine learning. InInternational Conference on Machine Learning, pages
4387–4398. PMLR, 2020.
[34] Yongqiang Wang and Angelia Nedi ´c. Decentralized gradient methods with time-varying
uncoordinated stepsizes: Convergence analysis and privacy design.IEEE Transactions on
Automatic Control, 69(8):5352–5367, 2023.
[35] Yoel Drori and Marc Teboulle. Performance of first-order methods for smooth convex mini-
mization: a novel approach.Mathematical Programming, 145(1):451–482, 2014.
[36] Miles Lubin, Oscar Dowson, Joaquim Dias Garcia, Joey Huchette, Benoît Legat, and Juan Pablo
Vielma. Jump 1.0: Recent improvements to a modeling language for mathematical optimization.
Mathematical Programming Computation, 15(3):581–589, 2023.
[37] MOSEK ApS.The MOSEK Optimization Software, 2019. URLhttps://www.mosek.com/.
[38] Chih-Chung Chang and Chih-Jen Lin. LIBSVM: a library for support vector ma-
chines.ACM Transactions on Intelligent Systems and Technology (TIST), 2(3):1–27, 2011.
https://www.csie.ntu.edu.tw/ cjlin/libsvmtools/datasets/binary.html.
[39] John C Platt. 12 fast training of support vector machines using sequential minimal optimization.
Advances in Kernel Methods, pages 185–208, 1999.
[40] Alex Krizhevsky, Geoffrey Hinton, et al. Learning multiple layers of features from tiny images.
Technical Report, 2009. https://www.cs.toronto.edu/ kriz/cifar.html.
11

[41] Richard Socher, Alex Perelygin, Jean Wu, Jason Chuang, Christopher D Manning, Andrew Y
Ng, and Christopher Potts. Recursive deep models for semantic compositionality over a
sentiment treebank. InProceedings of the 2013 Conference on Empirical Methods in Natural
Language Processing, pages 1631–1642, 2013.
[42] Alex Wang, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel Bowman.
GLUE: A multi-task benchmark and analysis platform for natural language understanding. In
Proceedings of the 2018 EMNLP Workshop BlackboxNLP: Analyzing and Interpreting Neural
Networks for NLP, pages 353–355, 2018.
[43] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: Pre-training
of deep bidirectional transformers for language understanding. InProceedings of the 2019
Conference of the North American Chapter of the Association for Computational Linguistics:
Human Language Technologies, pages 4171–4186, 2019.
[44] Arkadi Memirovski and David Yudin.Problem complexity and method efficiency in optimization.
Wiley-Interscience, New York, 1983.
[45] Boris Polyak. Introduction to optimization.Optimization Software Inc., Publications Division,
New York, 1, 1987.
[46] Lieven Vandenberghe and Stephen Boyd. Semidefinite programming.SIAM Review, 38(1):
49–95, 1996.
[47] Sebastien Colla and Julien M Hendrickx. Automatic performance estimation for decentralized
optimization.IEEE Transactions on Automatic Control, 68(12):7136–7150, 2023.
[48] Adrien B Taylor, Julien M Hendrickx, and François Glineur. Exact worst-case performance of
first-order methods for composite convex optimization.SIAM Journal on Optimization, 27(3):
1283–1313, 2017.
[49] Y . LeCun, C. Cortes, and C. Burges. The MNIST database of handwritten digits, 1994.
http://yann.lecun.com/exdb/mnist/.
[50] L. Deng. The MNIST database of handwritten digit images for machine learning research.
IEEE Signal Processing Magazine, 29(6):141–142, 2012.
[51] Shi Pu, Wei Shi, Jinming Xu, and Angelia Nedi´c. Push–pull gradient methods for distributed
optimization in networks.IEEE Transactions on Automatic Control, 66(1):1–16, 2020.
[52] Sashank Reddi, Zachary Charles, Manzil Zaheer, Zachary Garrett, Keith Rush, Jakub Koneˇcný,
Sanjiv Kumar, and H. Brendan McMahan. Adaptive federated optimization, 2021. URL
https://arxiv.org/abs/2003.00295.
[53] Ziheng Cheng, Xinmeng Huang, Pengfei Wu, and Kun Yuan. Momentum benefits non-iid
federated learning simply and provably, 2024. URL https://arxiv.org/abs/2306.16504.
A Performance evaluation
A.1 PEP formulation
It is worth noting that although numerous optimization algorithms have been proposed, quantifying
and comparing their performance—typically evaluated through worst-case guarantees in the opti-
mization and machine learning communities [44, 45, 21]—remains intrinsically challenging. This
difficulty arises because most existing results, which are primarily based on analytical methods, tend
to be overly conservative: they generally provide only sufficient (but not necessary) conditions for
convergence, or offer asymptotic rates of convergence rather than exact quantitative characterizations
[16]. Recently, a computational approach was proposed that can provide theexactworst-case perfor-
mance of an optimization algorithm. This approach is based on formulating performance analysis as a
semidefinite program (see, e.g., [46]) and is also known as the performance estimation problem (PEP)
[35, 16]. This approach can obtain exact performance bounds for algorithms over specified function
classes [16], in contrast to traditional asymptotic analyses that often produce loose guarantees. This
approach has recently been extended to the decentralized case [47].
The idea behind the PEP is to frame the worst-case performance evaluation of an algorithm as an
optimization problem over all admissible functions (e.g., smooth and convex) and initial conditions.
12

Although this optimization is inherently infinite-dimensional, as it involves a continuous function
over its variables, [48, 16] demonstrate that it can be solvedexactlyas a finite-dimensional convex
optimization problem by replacing the function constraint with an equivalent finite dimensional
interpolation condition. Generally, the framework can be formulated as follows:
sup
f,x0,...,xK ,x∗
P(O f , x0, . . . , xK, x∗)(PEP)
such thatf∈ F,
x∗ is optimal forf,
x1, . . . , xK are generated fromx 0 by methodMwithO f ,
∥x0 −x ∗∥2 ≤R,
where M denotes an optimization algorithm, Of denotes the oracle that returns the corresponding
function value and gradient at a given point of the function f, F is the class of functions to which f
belongs (e.g., strongly convex functions or general convex functions), K is the number of steps the
algorithm M performs, and R is a given constant. By solving the PEP, one can obtainexactperfor-
mance bounds for algorithms over designated function classes, in contrast to traditional asymptotic
analyses, which often yield loose guarantees.
The PEP framework can be directly applied to evaluate the performance of centralized gradient
descent algorithms. To evaluate the performance of our proposed decentralized approach, we extend
the result in [47] for homogeneous step sizes to the heterogeneous step size case and provide a new
PEP formulation.
To describe the PEP framework, we first define the augmented states as xk = [xk 1, xk 2, . . . , xk N ]∈
Rd×N , where the superscript k belongs to the index set IK ={0, . . . , K}. Similarly, we
define the augmented local optimum and global optimum as x⋆ = [x ⋆ 1, x ⋆ 2, . . . , x⋆ N ] and
x∗ = [x ∗ 1, x∗ 2, . . . , x∗ N ], respectively (where x∗ 1 =x ∗ 2 =· · ·=x∗ N will be enforced in the
PEP formulation). To simplify notation, we extend the index set IK for augmented states to include
these two optimal states, defining the augmented index set asI ⋆,∗ K ={0, . . . , K, ⋆,∗}.
In a similar manner, we define the augmented gradients and function values as
gk = [gk 1 , gk 2 , . . . , gk N ]∈R d×N , f k = [f k 1 , fk 2 , . . . , fk N ]∈R 1×N ,fork∈I ⋆,∗ K .
Under these definitions, we have
P= [x 0 g0 g1 ... g K g⋆ g∗ x⋆ x∗]∈R d×[(K+6)N] ,
G=P T P∈S ((K+6)N)×((K+6)N) + , F= [f 0 f 1 ... f K f ⋆ f ∗]∈R 1×(K+3)N ,
where S+ denotes the set of symmetric positive semidefinite matrices. We use the standard notation
ei ∈R d to denote the unit d-dimensional vector with a single 1 in the i-th component and 1N ∈R N
as the all one vector. The following vectors are employed to select specific columns inPandF:
fk i =e kN+i ∈R (K+3)N ,g k i =e (k+1)N+i ∈R (K+6)N ,g ∗ i =e (K+3)N+i ∈R (K+6)N ,
g⋆ i =e (K+2)N+i ∈R (K+6)N ,x ⋆ i =e (K+4)N+i ∈R (K+6)N ,
f⋆ i =e (K+1)N+i ∈R (K+3)N ,f ∗ i =e (K+3)N+i ∈R (K+3)N ,
x0 i =e i ∈R (K+6)N ,∀i∈[N], k∈I K;x ∗ =e (K+5)N+i ∈R (K+6)N .
13

The stacked version of these vectors is analogous to the formulation above. Now we are in a position
to give our formulation of the PEP for the decentralized algorithm as follows
max
F,G
F∗
 NX
i=1
fK i −f ∗1N
!
(4)
subject to⟨G, A({x k i ,g k i ,f k i }k∈{p,q}, µi, Li)⟩ ≤F∗(f p i −f q i ),∀i∈[N], p, q∈I ⋆,∗ K ,(5)
{xk i }i∈[N],k∈I K are generated recursively by Algorithm 1,(6)
⟨G ,g∗1N 1T N g∗T ⟩= 0,⟨G,g ⋆ i g⋆T i ⟩= 0,∀i∈[N],(7)
⟨G,(x 0 i −x ∗)(x0 i −x ∗)T ⟩ ≤R2 0,∀i∈[N],(8)
⟨G,(x ⋆ i −x ∗)(x⋆ i −x ∗)T ⟩ ≤R2 ∗,∀i∈[N],(9)
⟨G,(x 0 1 −x 0 i )(x0 1 −x 0 i )T ⟩= 0,∀i∈[N],(10)
⟨G,(x ∗ 1 −x ∗ i )(x∗ 1 −x ∗ i )T ⟩= 0,∀i∈[N],(11)
G⪰0,(12)
rank(G)≤d,(13)
where
A({xk i ,g k i ,f k i }k∈{p,q}, µi, Li)
= 1 2 h (xp i −x q i )gq i T +g q i (xp i −x q i )T i
− µi(Li −µ i) 2L2 i  (xq i −x p i )(gq i −g p i )T + (gq i −g p i )(xq i −x p i )T 
+ 1 2  1− µi Li  1 Li (gp i −g q i )(gp i −g q i )T +µ i(xp i −x q i )(xp i −x q i )T  ,
and ⟨·,·⟩ denotes the standard matrix inner product defined as ⟨A, B⟩= trace(ABT ), R∗ bounds the
distance between local and global optima, i.e., ∥x⋆ i −x ∗∥ ≤R∗, R0 bounds the distance between
the initial point and the global optimum, i.e., ∥x0 i −x ∗∥ ≤R0, and generally R∗ ≪R 0. We use the
measure here because an equal start guarantees that the algorithm generates local states uniformly
across all agents. Thus, we do not explicitly make use of f(¯x)here. The constraints in (4)–(8) are
standard in the formulation of the PEP [ 16]. The constraints in (10) enforce an identical starting
point, while the constraints in (11) ensure that the global optimum is consistent across all agents.
A.2 Proof of Theorem 1
Theorem 2.(Convergence Acceleration of Algorithm 1) Consider the optimization problem defined
in (1), where the function f belongs to the class Fµ,L, characterized by the smoothness parameter
L and strong convexity parameter µ. Let A1 denote Algorithm 1 with local step sizes 1 Li , and Ac
denote centralized gradient descent with a uniform step size 1 L. For the performance metric
PA = max f∈F µ,L
(
1
N
NX
i=1
||xk i,A −x ∗||2
)
,
which measures the worst-case optimization error at iteration k over all f∈ Fµ,L, we consider the
ratio PA1 /PAc as the relative acceleration of Algorithm 1 compared with centralized gradient descent
(with values below 1 indicating acceleration and smaller ratios indicating stronger acceleration).
Figure 1(b) gives the exact ratio values under different function classes, and the ratio values being
strictly less than 1 for all tested function classes Fµ,L in the heterogeneous setting confirm that
Algorithm 1 with local step sizes achieves a strictly faster convergence rate than centralized gradient
descent under all considered function classes.
Proof. First, we have PA <∞ for any finite k, which implies that the worst-case optimization
error of Algorithm 1 over the function class Fµ,L is always finite for any k. Therefore, the set
arg maxf∈F µ,L
n
1
N
PN
i=1 ∥xk i,A −x ∗∥2
o
is guaranteed to be nonempty. This means that there
14

exists at least one function instance f ∗ A such that, Algorithm 1, when executed with step-size scheme
A, indeed attains its worst-case performance at iterationk.
For any such maximizer f ∗ A ∈arg max f∈F µ,L
n
1
N
PN
i=1 ∥xk i,A −x ∗∥2
o
, the value PA returned by
the PEP is therefore anexact, not merely upper-bounding, characterization of the true worst-case
error over Fµ,L. In other words, the PEP does not produce a loose bound: it identifies a specific
problem instance on which Algorithm 1 performs exactly as poorly as the bound indicates. With
this interpretation, the ratio
PA1
PAc directly compares the exact worst-case optimization errors of
Algorithm 1 versus centralized gradient descent. A value
PA1
PAc <1 therefore means that—in the worst case—Algorithm 1 has strictly smaller optimization error than centralized gradient descent
at iteration k. Hence, the ratio values in Figure 1(b) quantitatively capture the exact speed gains
achieved by Algorithm 1.
B Additional experimental results
B.1 Handwritten digits classification on MNIST
In this experiment, we consider a neural network based classifier for the MNIST dataset of handwritten
digits [49], a widely used benchmark for training and evaluating models in the field of machine
learning [50]. The dataset contains 60,000 training images and 10,000 testing images, with each
set containing a roughly equal number of images for each digit from 0 to 9. We employ a classifier
based on a deep convolutional neural network (CNN). The architecture begins with two convolutional
layers, with 16 and 32 filters respectively, each followed by a max pooling layer. Finally, the network
includes a fully connected dense layer that maps the extracted features to 10 output classes. In
the decentralized case, the data are partitioned across five devices in a label-based, heterogeneous
manner. Specifically, all data entries with the same label are assigned to the same device, and each
device holds data corresponding to two distinct labels. For each device, we estimate the smoothness
constant using 1,000 data entries, following its formal definition. The results are summarized in
Fig. 5. It is evident that decentralization can substantially reduce the number of iterations required
to reach an optimal solution. It is worth noting that the experiment was conducted multiple times
using different smoothness constants, each estimated from distinct subsets of data (see Fig. 5(c) for
three instances of estimated smoothness constants). Despite variations in these estimates, the results
consistently indicate that decentralization yields significant acceleration over the centralized approach.
Furthermore, in this experiment, we use the entire dataset (full batch) for gradient calculation, which
may become computationally expensive for more complex images. Therefore, in the next experiment,
where we consider a dataset with more complicated images, we employ mini-batch sampling to
compute gradients at each iteration.
B.2 Experimental results on various heterogeneous data distributions
We have conducted additional experiments to evaluate the learning performance of our Algorithm 1
under different levels of data heterogeneity using the MNIST dataset. More specifically, the training
dataset consists of 10 classes. For each class, we partitioned the data across 5 agents according to
a Dirichlet distribution with parameters α∈ {0.1,0.5,1,5} . Note that the parameter α measures
the heterogeneity in data distribution among all agents. A smaller α leads to a higher degree of data
heterogeneity. Both Algorithm 1 and its centralized counterpart (called GD) used full-batch gradient
computation.
15

Training Loss
0.5
1.0
2.0
2.5
Epochs
Epochs
0.5
1.5
2.0
2.5 Training Loss
Epochs
0.5
1.5
2.0
2.5 Training Loss
Training Loss
GD (full batch) Algorithm 1 (full batch)
Smoothness Constant
Expr. 5
Expr. 8
Training Loss
Epochs
GD (full batch)
Algorithm 1 (full batch)
0 200 400 600 800 1000
0 100 200 300 400 500
Algorithm 1 (full batch)GD (full batch)
Expr. 2
Device Index
Expr. 5
Device Index
Expr. 8
0.90
0.85
0.80
0.75
0.70
0.65Training Accuracy
Epochs
400 600 800 1000
GD (full batch)
Algorithm 1 (full batch)
Test Accuracy
Epochs
400 600 800 1000
GD (full batch)
Algorithm 1 (full batch)0.3
0.6
1.5
1.8
2.4
0.9
1.2
2.1
Expr. 10.0
0.5
1.0
1.5
2.0
Experiment Numbers
1.1419
1.5457
1.6792
1.0432
1.4987
1.1429
1.7327
1.0998
1.7852
1.0845
1.7955
1.0731
1.8390
0.9413
1.7138
1.0129
Expr. 2 Expr. 3 Expr. 4 Expr. 5 Expr. 6 Expr. 7 Expr. 8
Device Index
Expr. 2
Dଵ Dଶ Dଷ Dସ Dହ C0
100
500
200
300
400
Dଵ Dଶ Dଷ Dସ Dହ C
Dଵ Dଶ Dଷ Dସ Dହ C
1.5
1.0
1.0
0 100 200 300 400 500
0 100 200 300 400 500
0.90
0.85
0.80
0.75
0.70
0.65
Smoothness Constant Smoothness Constant
0
100
500
200
300
400
0
100
500
200
300
400
(a)
Training Loss
0.5
1.0
2.0
2.5
Epochs
Epochs
0.5
1.5
2.0
2.5 Training Loss
Epochs
0.5
1.5
2.0
2.5 Training Loss
Training Loss
GD (full batch) Algorithm 1 (full batch)
Smoothness Constant
Expr. 5
Expr. 8
Training Loss
Epochs
GD (full batch)
Algorithm 1 (full batch)
0 200 400 600 800 1000
0 100 200 300 400 500
Algorithm 1 (full batch)GD (full batch)
Expr. 2
Device Index
Expr. 5
Device Index
Expr. 8
0.90
0.85
0.80
0.75
0.70
0.65Training Accuracy
Epochs
400 600 800 1000
GD (full batch)
Algorithm 1 (full batch)
Test Accuracy
Epochs
400 600 800 1000
GD (full batch)
Algorithm 1 (full batch)0.3
0.6
1.5
1.8
2.4
0.9
1.2
2.1
Expr. 10.0
0.5
1.0
1.5
2.0
Experiment Numbers
1.1419
1.5457
1.6792
1.0432
1.4987
1.1429
1.7327
1.0998
1.7852
1.0845
1.7955
1.0731
1.8390
0.9413
1.7138
1.0129
Expr. 2 Expr. 3 Expr. 4 Expr. 5 Expr. 6 Expr. 7 Expr. 8
Device Index
Expr. 2
Dଵ Dଶ Dଷ Dସ Dହ C0
100
500
200
300
400
Dଵ Dଶ Dଷ Dସ Dହ C
Dଵ Dଶ Dଷ Dସ Dହ C
1.5
1.0
1.0
0 100 200 300 400 500
0 100 200 300 400 500
0.90
0.85
0.80
0.75
0.70
0.65
Smoothness Constant Smoothness Constant
0
100
500
200
300
400
0
100
500
200
300
400
(b)
Training Loss
0.5
1.0
2.0
2.5
Epochs
Epochs
0.5
1.5
2.0
2.5 Training Loss
Epochs
0.5
1.5
2.0
2.5 Training Loss
Training Loss
GD (full batch) Algorithm 1 (full batch)
Smoothness Constant
Expr. 5
Expr. 8
Training Loss
Epochs
GD (full batch)
Algorithm 1 (full batch)
0 200 400 600 800 1000
0 100 200 300 400 500
Algorithm 1 (full batch)GD (full batch)
Expr. 2
Device Index
Expr. 5
Device Index
Expr. 8
0.90
0.85
0.80
0.75
0.70
0.65Training Accuracy
Epochs
400 600 800 1000
GD (full batch)
Algorithm 1 (full batch)
Test Accuracy
Epochs
400 600 800 1000
GD (full batch)
Algorithm 1 (full batch)0.3
0.6
1.5
1.8
2.4
0.9
1.2
2.1
Expr. 10.0
0.5
1.0
1.5
2.0
Experiment Numbers
1.1419
1.5457
1.6792
1.0432
1.4987
1.1429
1.7327
1.0998
1.7852
1.0845
1.7955
1.0731
1.8390
0.9413
1.7138
1.0129
Expr. 2 Expr. 3 Expr. 4 Expr. 5 Expr. 6 Expr. 7 Expr. 8
Device Index
Expr. 2
Dଵ Dଶ Dଷ Dସ Dହ C0
100
500
200
300
400
Dଵ Dଶ Dଷ Dସ Dହ C
Dଵ Dଶ Dଷ Dସ Dହ C
1.5
1.0
1.0
0 100 200 300 400 500
0 100 200 300 400 500
0.90
0.85
0.80
0.75
0.70
0.65
Smoothness Constant Smoothness Constant
0
100
500
200
300
400
0
100
500
200
300
400 (c)
Figure 5: Comparison of Algorithm 1 with its centralized counterpart (labeled GD) using the MNIST
dataset. In this experiment, both algorithms use full-batch gradient computation: the centralized
approach processes the entire dataset, while in the decentralized approach, each device computes
gradients using all the data allocated to it. (a) shows that the decentralized approach achieves faster
convergence than the centralized counterpart in terms of training loss, training accuracy, and test
accuracy. (b) compares the training loss over eight runs with different estimated smoothness constants
and random initializations. (c) illustrates the estimated smoothness constants alongside the training
loss trajectories of three selected runs from the eight. On the x-axis representing the device index,
the label “C” denotes the centralized case, and “ D1” through “ D5” represent the devices in the
decentralized case.
(a)α= 0.1
 (b)α= 0.5
 (c)α= 1
 (d)α= 5
Figure 6: Training losses of Algorithm 1 and its centralized counterpart (labeled GD) for hetero-
geneous data distributions under different Dirichlet parameters α∈ {0.1,0.5,1,5} on the MNIST
dataset.
Fig. 6 shows that a smaller Dirichlet parameter α (corresponding to a higher degree of heterogeneity
in data distributions among agents) leads to more acceleration via decentralization.
16

B.3 Experimental results on various network sizes
We have also conducted additional experiments to evaluate the efficacy of our Algorithm 1 under dif-
ferent network sizes (i.e., different number of devices). Specifically, we considered N= 2,5,15,25
devices, respectively. The data are partitioned across agents according to a Dirichlet distribution with
parameterα= 0.1. All other parameters are the same as those in Section B.1.
(a)N= 2
 (b)N= 5
 (c)N= 15
 (d)N= 25
Figure 7: Training losses of Algorithm 1 and its centralized counterpart (labeled GD) for different
network sizesN, N∈ {2,5,15,25}on the MNIST dataset.
The results in Fig. 7 show that increasing the number of devices strengthens the performance
advantage of our Algorithm 1 over its centralized counterpart.
B.4 Comparison between Algorithm 1 with Decentralized GD and gradient tracking
To further evaluate the performance of Algorithm 1, we conducted additional experiments comparing
it with decentralized gradient descent (labeled decentralized GD) from [14] and gradient tracking
from [51] on the MNIST dataset. The data were partitioned across 5 devices according to a Dirichlet
distribution with parameter α= 0.1 . For each device, we estimated the smoothness constant using
1,000 data samples, based on its formal definition. The step sizes for decentralized GD and gradient
tracking were set to the reciprocal of the average estimated smoothness constants. All algorithms
used full-batch gradient computation.
(a) Training Loss
 (b) Training Accuracy
 (c) Test Accuracy
Figure 8: Comparison of Algorithm 1 with decentralized GD in [14] and gradient tracking in [51]
using the MNIST dataset. In this experiment, all algorithms use full-batch gradient computation,
meaning that each device computes gradients using all the data allocated to it.
Fig. 8 shows that Algorithm 1 achieves faster convergence than both the decentralized GD and
gradient tracking in terms of training loss, training accuracy, and test accuracy.
B.5 Comparison of Algorithm 1 with FedOpt Variants and FedAvgM
To further evaluate the performance of Algorithm 1, we conducted additional experiments comparing
it with FedOpt variants, including FedAdam, FedYogi, and FedAdagrad from [ 52], as well as
17

FedAvgM from [53], on the MNIST dataset. The data were partitioned across 5 devices, with each
device containing samples from only two classes, corresponding to a highly heterogeneous (non-IID)
setting. For each device, we estimated the smoothness constant using 1,000 data samples based on its
formal definition. All algorithms employed full-batch gradient computation.
0 200 400 600 800 1000
Epochs
0.50
0.75
1.00
1.25
1.50
1.75
2.00
2.25Training Loss
FedAdaGrad
FedYogi
FedAdam
FedAvgM
GD
Algorithm 1
(a) Training Loss
0 200 400 600 800 1000
Epochs
0.2
0.4
0.6
0.8Training Accuracy
FedAdaGrad
FedYogi
FedAdam
FedAvgM
GD
Algorithm 1 (b) Training Accuracy
0 200 400 600 800 1000
Epochs
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8Test Accuracy
FedAdaGrad
FedYogi
FedAdam
FedAvgM
GD
Algorithm 1 (c) Test Accuracy
Figure 9: Comparison of Algorithm 1 with FedOpt variants including FedAdam, FedYogi, and
FedAdagrad from [52], as well as FedAvgM from [53]. In this experiment, all algorithms use full-
batch gradient computation, meaning that each device computes gradients using all the data allocated
to it.
Fig. 9 shows that Algorithm 1 achieves faster convergence than FedOpt-based methods, including
FedAdam, FedYogi, FedAdagrad, and FedAvgM, in terms of training loss, training accuracy, and test
accuracy.
B.6 Ablation study of Algorithm 1 with partial agent participation
We evaluate the proposed Algorithm 1 under a partial participation scheme, where at each commu-
nication round, some agents may be unable to participate due to failures in their local functions or
communication delays. Specifically, at each communication round, each agent participates with
probability p∈ {0.7,0.8,0.9,1.0}, with p= 1.0 denoting participation in every round. The results
shown in Fig. 10 demonstrate the robustness of our algorithm under partial participation in a 20-agent
setting, where each agent possesses data from only two classes.
0 200 400 600 800 1000
Epochs
0.50
0.75
1.00
1.25
1.50
1.75
2.00
2.25Training Loss
DSGD(p=1.0)
DSGD(p=0.9)
DSGD(p=0.8)
DSGD(p=0.7)
(a) Training Loss
0 200 400 600 800 1000
Epochs
0.2
0.4
0.6
0.8Training Accuracy
DSGD(p=1.0)
DSGD(p=0.9)
DSGD(p=0.8)
DSGD(p=0.7) (b) Training Accuracy
0 200 400 600 800 1000
Epochs
0.2
0.4
0.6
0.8Test Accuracy
DSGD(p=1.0)
DSGD(p=0.9)
DSGD(p=0.8)
DSGD(p=0.7) (c) Test Accuracy
Figure 10: Algorithm 1 with each agent having a participation probability of p∈ {0.7,0.8,0.9,1.0}
at each communication round on the MNIST dataset. In this experiment, all algorithms employ
full-batch gradient computation, meaning that each device computes gradients using all locally
allocated data.
The results demonstrate that the proposed Algorithm 1 remains robust under partial agent participation.
18
