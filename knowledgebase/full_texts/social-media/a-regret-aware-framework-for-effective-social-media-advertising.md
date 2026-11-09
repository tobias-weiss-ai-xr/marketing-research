---
title: A Regret-Aware Framework for Effective Social Media Advertising
url: https://arxiv.org/abs/2504.00451
category: social-media
subcategory: empirical
date: 2025-04
venue: ''
authors:
- Poonam Sharma
- Dildar Ali
- Suman Banerjee
source: arxiv
pdf_url: https://arxiv.org/pdf/2504.00451
pages: 45
chars: 176147
fetched_at: '2026-11-08T13:01:22+00:00'
kb_version: 1
---

# A Regret-Aware Framework for Effective Social Media Advertising

A Regret-Aware Framework for Effective Social
Media Advertising
Poonam Sharma, Dildar Ali, Suman Banerjee
Department of Computer Science and Engineering, Indian Institute of
Technology Jammu, 181221, Jammu and Kashmir, India.
*Corresponding author(s). E-mail(s): suman.banerjee@iitjammu.ac.in;
Contributing authors: poonam.sharma@iitjammu.ac.in;
2021rcs2009@iitjammu.ac.in;
Social Media Advertisement has emerged as an effective approach for promoting the
brands of a commercial house. Hence, many of them have started using this medium to
maximize the influence among the users and create a customer base. In recent times,
several companies have emerged as Influence Provider who provides views of adver-
tisement content depending on the budget provided by the commercial house. In this
process, the influence provider tries to exploit the information diffusion phenomenon
of a social network, and a limited number of highly influential users are chosen and
activated initially. Due to diffusion phenomenon, the hope is that the advertisement
content will reach a large number of people.
Now, consider that a group of advertisers is approaching an influence provider with
their respective budget and influence demand. Now, for any advertiser, if the influence
provider provides more or less influence, it will be a loss for the influence provider. It
is an important problem from the influence provider’s point of view, as it is important
to allocate the seed nodes to the advertisers so that the loss is minimized. In this
paper, we study this problem, which we formally referred to as Regret Minimization
in Social Media Advertisement Problem. We propose a ‘noble regret model’ that
captures the aggregated loss encountered by the influence provider while allocating
the seed nodes. We have shown that this problem is a computationally hard problem
to solve. We have proposed three efficient heuristic solutions to solve our problem. All
proposed solution approaches have been analyzed to understand their time and space
requirements. They have been implemented with real-world social network datasets,
and several experiments have been conducted. From the experiments, we have observed
1
arXiv:2504.00451v1  [cs.SI]  1 Apr 2025

that the proposed solution approaches lead to the allocation of seed nodes among the
advertisers, which results in much less regrets compared to many baseline methods.
1 Introduction
A social network is defined as an interconnected structure among a group of human
beings created for social interactions [1]. Due to the advancement of wireless internet
technologies and hand-holding mobile devices, the use of social media has become
an integral part of human life. In recent times, several social network datasets have
been publicly available. As per the reported recent statistics, every year, the number
of active social media users is increasing 1. Many problems have been studied in this
domain, such as community detection [2–4], information diffusion [5, 6], influence
maximization [7–9], opinion dynamics [10, 11], and many more. Commercial houses
have exploited social media to promote their brands and make advertisements. In
this case, the key phenomenon of social networks that have been exploited is the
diffusion of information [6]. This phenomenon says that every user of an online social
network tends to share information with their neighbor. This way, the information,
innovation, ideas, etc., spreads through the network and goes viral. Commercial houses
have exploited this phenomenon to promote their brands and create their customer
base [12, 13]. The key question that arises in this context is how we can select a
limited number of highly influential users from the network such that the influence in
the network gets maximized. This question remains an active area of research in the
domain of Social Network Analysis. An enormous amount of research on this problem
leads to a significant amount of literature [7], [9], [14], [8], [15], [16], [17], [18].
In recent times, several media houses have emerged that conduct social media
marketing. Technically, they are called Influence Provider. In this approach, a set of
commercial houses approaches an influence provider with their respective influence
demand and budget. Here, the payment rule is as follows. If the influence provider
provides the required or more influence, the advertiser will give the mentioned bud-
get; otherwise, a partial payment (on a pro-rata basis) will be made to the influence
provider. Now, if the influence provider provides more or less influence than the influ-
ence demand, it is a loss for the influence provider. This happens due to the following
reasons. Consider the influence provider provides less influence to an advertiser, and
as per the payment rule, the influence provider will receive a partial payment, which
is a loss.
On the other hand, if the influence provider provides more influence, then there
is no additional payment for the extra influence. However, this extra influence can be
provided to advertisers whose demand for influence has yet to be satisfied. Now, the
task of the influence provider is to return respective seed sets to the advertisers so
that this leads to the least regret. This is the key problem that we have studied in
this paper. This process has been shown diagrammatically in Figure 1.
‘Regret’ in the context of billboard advertisement has been studied, and some
studies are available. To the best of our knowledge, Zhang et al. [19] was the first to
1https://backlinko.com/social-media-users
2

Social Network
Influence Provider
Advertisers
Allocated Seed Nodes to
Advertisers
Fig. 1: A schematic diagram showing the allocation of seed nodes to advertisers in a
social network.
study the Regret Minimization Problem. They posed this problem as a discrete opti-
mization problem and showed that this problem is NP-hard and had to approximate
beyond any constant factor. They proposed two local search-based heuristic solutions
for this problem. Later, Ali et al. [20, 21] proposed several heuristic solutions for this
problem, and from the experimental evaluations, it can be observed that the proposed
solutions by Ali et al.[20] lead to much less regret compared to the methods proposed
by Zhang et al [19]. However, to the best of my knowledge, regret in the context of
social media advertisements has yet to be defined. In this paper, we bridge this gap by
defining the notion of regret in the context of social media advertisement and propose
several seed selection strategies to minimize the regret. Mainly, we make the following
contributions:
• We have formally defined ‘Regret’ in the context of social media advertisements.
• We introduce and study the noble problem of Regret Minimization in Social
Media Advertisement, and formally, we call it RMSMA Problem.
• We formulate this problem as a discrete optimization problem and show that the
problem is NP-hard and hard to approximate beyond any constant factor.
• We propose two solution approaches for this problem with their detailed analysis
and complexity calculation.
• The proposed solution approaches have been experimentally evaluated to show
their effectiveness and efficiency.
The rest of the paper is organized as follows. Section 2 describes relevant studies
from the literature. Section 3 describes the relevant concepts and defines our prob-
lem formally. Section 4 describes the proposed solution approaches. The experimental
3

evaluation has been described in Section 5. Finally, Section 6 concludes our study and
reports a few future research directions.
2 Related Work
In this section, we describe some relevant studies from the literature. Our study comes
under the two broad domains, namely, influence and its analysis in social network
and regret analysis in advertisement. In the following two subsections, we describe the
relevant studies on both of this topics.
2.1 Influence and its Analysis in Social Networks
In past two decades, there has been significant amount of study on the information
diffusion in social networks and its applications. Several diffusion models have been
introduced and among many the most well studied problem in the context of infor-
mation diffusion is the Problem of Influence Maximization. Given a social network,
a diffusion model, and a positive integer k, this problem aims at identifying k many
highly influential users in the network such that their initial activation leads to the
maximum influence in the network. Due to the direct application of this problem in
the domain of viral marketing, this problem has been studied in different variants and
a plethora of solution methodologies have been proposed in the literature.
To the best of our knowledge, Domingos and Reichardson were the first to intro-
duce the problem of influence maximization in the context of viral marketing. Though,
Kempe at al. [22–24] were the first to study this problem as a discrete optimiza-
tion problem. They showed that if the underlying diffusion model is linear threshold
or independent cascade, the influence function becomes non-negative, monotone, and
submodular. Also they showed that the iterative greedy algorithm which works based
on marginal gain computation, leads to (1 − 1 e )-factor approximation guarantee. Sub-
sequently there are several studies and the proposed solution methodologies have been
classified into many categories such as approximation algorithms, heuristic solution
approaches, community-based solution approaches, reverse reachable set computation-
based approaches, and many more. The solution methodologies that belongs to the
approximation algorithm category, provides a seed set of a given cardinality whose
expected influence is a constant factor approximation with respect to an optimal seed
set of same cardinality. The first approximation algorithm was proposed by Kempe
at al. [22]. Subsequently, Leskovic et al. [25] proposed an approximation algorithm
having approximation ratio same as one proposed by Kempe at al. [22]. However, the
number of function evaluation performed by their method is much less. Hence, the
method proposed by Leskovic et al. [25]. Subsequently, there are many studies in this
directions.
Subsequently, a different class of approximation algorithm has been proposed whose
initial study was done by Brogs et al. [26] which works based on the computation of
reverse reachable sets. The basic idea of this approach is as follows. For every node,
a set is constructed which contains the set of other nodes which can influence this
node. This set is called as the reverse reachable set or RR set. For all the nodes of the
network, once the reverse reachable sets are computed, a small subset of nodes are find
4

out using some coverage algorithm such that the intersection of these nodes with RR
sets of the nodes becomes non empty. Following the study by Brogs et al. [26], several
approaches have been proposed in this direction such as TIM [27], TIM+ [27], IMM
[28], and many more. The other category of solution approaches can process a million
scale social network in couple of seconds. However, solution methodologies of this kind
does not give any guarantee on the quality of solution. Solution methodology of this
kind includes IRIE [29], Staticgreedy [30], IMRANK [31] and many more. Another
kind of solution methodologies exist where the community structure of the network has
been exploited. We call such methodologies as community-based solution approaches.
There are many solution approaches which belongs to this category [32–35]. There are
another class of solution approaches that uses optimization tools from soft computing
and nature inspired techniques. We call such approaches as soft computing-based
approaches. Plenty of approaches have been proposed which belongs to this category
[36–38].
In past one decade, the problem of influence maximization has been studied in
different variants. Nugyan et al. introduced the Budgeted Influence Maximization
Problem where every node of the network is assigned with a selection cost and a
fixed amount of budget has been allocated. This problem asks to choose a seed set
such that the total selection cost of the seed set is less than or equal to the allocated
budget. At the same time, the influence spread by the seed set is maximum among
all the seed sets of the same budget. They proposed a (1 − 1√e )-factor approximation
algorithm and a heuristic solution for this problem. Later, there are a few studies
on this problem which includes a community-based solution approach proposed by
Banerjee et al. [39], a bunch of heuristic solution proposed by Han et al. [40] and many
more. Another kind of influence diffusion problem that has been studied is the Target
Set Selection Problem and its different variants. In this problem, every node of the
network is assigned with a positive number which we call as threshold and this value
signifies that this node will be influenced once that many nodes among its neighbors
are already influenced. There are many studies on this problem [41–44].
2.2 Regret Analysis in Computational Advertisement
To the best of our knowledge, there has been limited amount of literature available
on the regret analysis in ‘computational advertisement’. The first study on this topic
was done by Zhang et al. [19] who formulated the regret minimization problem in the
context of billboard advertisement. They posed this problem as a discrete optimization
problem and showed that this problem is NP-hard and hard to approximate beyond
any constant factor. They also proposed several heuristic solution and experimented
with benchmark datasets. Later on there are several studies on this problem by Ali
et al. [45–47]. In [47], Ali et al. proposed a local search-based approach. In [45], Ali
et al. studied the regret minimization problem in billboard advertisement under zonal
influence constraint. They proposed a sampling-based approach to solve this problem.
However, to the best of our knowledge, the regret minimization problem has not
been studied in the context of social media advertisement context. In this paper, we
bridge this gap by studying the regret minimization problem in the context of social
networks. Next, we proceed to describe the problem statement subsequently.
5

3 Background and Problem Definition
In this section, we describe the background information and defines our problem
formally. Initially, we start by describing the notion of social network.
3.1 Social Network and Its Diffusion Phenomena
A social network is defined as an interconnected structure among a group of users and
often represented by a simple, weighted, undirected graph G(V, E, P) where the set of
users {u1, u2, . . . , um} constitute the vertex set V. There is an edge between the user
ui and uj, if ui and uj has social relationship. P is the edge weight function that maps
each edge to its corresponding influence probability, i.e, P : E − →(0, 1]. For any edge
(uiuj), its influence probability is denoted by P(ui, uj) and defined as the probability
by which the user ui will be able to influence uj. For any user ui, the set of neighbors
is denoted as N (ui) and defined as the set of users with which ui is directly linked,
i.e., N (ui) = {uj : (uiuj) ∈ E}.
One of the important phenomenon of social network is the diffusion of information
which says that the users of a social network tend to share the information and in this
way information propagates through the network and become viral. This phenomenon
has been adopted by the commercial houses for promoting their brands and creating
influence among its prospective customers. Several models have been introduced in
the literature to study the diffusion process in a social network. One of the widely
studied is the Independent Cascade Model which has been stated in Definition 1.
Definition 1 (Independent Cascade Model). [48] In Independent Cascade Model, the
rules for the diffusion are as follows:
1. The diffusion process starts from a set of initially active nodes (called seed nodes)
information is diffused in discrete time stamps.
2. A node can be in either of two states: active (influenced) or inactive (non-
influenced).
3. A node can change its state from inactive to active, but not vice versa.
4. The diffusion process stops when no more node activation is possible.
3.2 Influence Maximization Problem
In general, the users of a social network is formed by rational and self interested human
beings, and hence, they need to incentivize if they are chosen as seed nodes. This has
been formalized as the cost function C : V − →R+. For any user u ∈ V, the selection
cost of u is denoted by C(u). A fixed amount of budget B is available. Now, given
this information, the social influence maximization problem (cost version) is stated in
Definition 2
Definition 2 (Influence Maximization Problem (cost version)) . Given a social net-
work G(V, E, P), a cost function C : V − →R+, and a budget B, this problem asks to
choose a subset of the users such that the total selection cost is less than the budget
and the influence in the network is maximized. Mathematically, this problem can be
expressed as a discrete optimization problem and written in Equation 1.
6

SOP T← − argmax
S⊆V and C(S)≤B
σ(S) (1)
Here, C(S) denotes the total selection cost of all the nodes in S, i.e., C(S) =P
u∈S
C(u). As mentioned in [22], this has been reported that this is a computationally
hard problem to solve. The main result is reported in Theorem 1.
Theorem 1. Given a social network G(V, E, P), and two positive integers B and ℓ,
even if the selection cost of all the users is 1, still it is NP-complete to decide whether
G has an influence at least ℓ.
3.3 Social Media Advertisement through External Agent
In recent times, several influence providers have emerged who conducts social media
advertisement on a payment basis and the process goes in the following way. A com-
mercial house approaches to an influence provider to obtain certain number of views
of an advertisement content (e.g., video, animation etc.) on a payment basis. The
payment rule is as follows: If the required or more influence is provided then the full
payment will be made else a partial payment. Now, from the influence provider’s point
of view whether it provides more or less influence it is loss for them. Because, if it
provides less influence then it will have the partial payment. On the other hand, if it
provides more influence then the influence provider does not get any extra incentive
for it. This loss has been mathematically formalized as regret. Depending upon the
mentioned two cases, two different kinds of regret is possible:
• Revenue Regret: This kind of regret happens when the influence provider pro-
vides less influence compared to the influence demand. For any seed set S, the
revenue regret associated with the seed set S is denoted by Rr and can be defined
using Equation 2.
Rr(Si) = Bi · (1 − γ · I(Si) σi ) + δ · |Si| (2)
• Excessive Regret : This kind of regret happens when the influence provider
provides more influence than the required.
Re(Si) = Bi · I(Si) − Ii Ii + δ · |Si| (3)
Regret Model.
Following the above, we formulate the regret model for the influence provider per-
spective to assign seed set Si to the advertisers ai and it is stated in Definition
3.
Definition 3 (The Regret Model). Let, for the advertiser ai ∈ A, the allocated seed set
is Si and the regret associated with this allocation is denoted by R(Si). This quantity
can be defined by the following conditional equation:
7

R(Si) =



Bi · (1 − γ · I(Si) Ii ) + δ · |Si|, if ai · Ii > I(Si)
Bi · I(Si)−Ii Ii + δ · |Si|, if ai · Ii < I(Si)
0, otherwise
Here, the fraction I(Si) Ii ) is part of the satisfied influence for the advertiser ai and γ is a parameter which is called as the penalty ratio due to the unsatisfied demand.
Note that in the regret model definition, we discriminate between small and large
seed sets S1 and S2 with the same influence value with |S1| << |S2| or |S1| >> |S2|.
In practice, achieving lower regret with fewer seed sets is desirable. We discourage
using a larger seed set because it consumes a higher cost than the smaller one while
both return the same amount of influence value. Hence, the parameter δ is there as
cardinality penalty ratio.
3.4 Problem Definition
Now, we define our problem formally. Consider a set of ℓ advertisers A =
{a1, a2, . . . , aℓ} are approaching to an influence provider X with their respective influ-
ence demand and corresponding budget. For the i-th advertiser ai, we denote its
corresponding influence demand and budget by σi and Bi, respectively. This has been
diagrammatically represented in Figure 1. The influence provider has the access of the
social network G and it returns the seed sets and their corresponding influence value
to the respective advertiser. Here, the constraint is that for any pair of advertisers
ai, aj ∈ A, Si ∩ Sj = ∅. Consider, Π = {S1, S2, . . . , Sℓ} is a selection of ℓ seed sets.
Here, we define the notion of feasible selection in Definition 4.
Definition 4 (Feasible Selection). Given a set of ℓ advertisers with their respective
influence demand and budget (σi, Bi)ℓ i=1, an influence provider X , a social network
G(V, E, P), a selection Π = {S1, S2, . . . , Sℓ} is said to be a feasible selection when for
all i ∈ {1, 2, . . . , ℓ}, C(Si) ≤ Bi.
For any problem instance, the set of all possible feasible selection is denoted by
Σ. Now, for any selection Π, the regret associated with this is denoted by Q(Π) and
stated in Definition 5.
Definition 5 (Regret Associated with a Selection) . Given a set of ℓ advertisers
A = {a1, a2, . . . , aℓ} with their respective influence demand and corresponding budget
(σi, Bi)ℓ i=1, a social network G, and a feasible selection Π = {S1, S2, . . . , Sℓ} ∈Σ, the
regret associated with the selection Π is denoted by Q(Π) and defined as the sum of
the regret for each of the seed sets which has been written in Equation 4.
Q(Π) =
X
S∈{S1,S2,...,Sℓ}
R(S) (4)
Now, we formally define the Regret Minimization in Social Media Advertisement
Problem in Definition 6.
Definition 6 (Regret Minimization in Social Media Advertisement Problem) . Given
a set of ℓ advertisers A = {a1, a2, . . . , aℓ} with their respective influence demand and
corresponding budget (σi, Bi)ℓ i=1, and a social network G, the Regret Minimization in
8

Social Media Advertisement Problem (RMSMA Problem) asks to find out a selection
that leads to the least regret for the influence provider. Mathematically, this problem
can be posed as a discrete optimization problem and expressed in Equation 5.
Π∗ ← −argmin
Π∈Σ
R(Π) (5)
Here, Π∗ denotes the optimal selection. From the computational point of view, this
problem can be posed as follows:
RMSMA Problem
Input: Advertisers A = {a1, a2, . . . , aℓ}, The Social Network G(V, E, P), Influ-
ence Demand and Budget ( σi, Bi)ℓ i=1.
Problem: Find out the seed sets and the expected influence (Si, I(Si))n i=1 such
that for any ai, aj ∈ A, Si ∩ Sj = ∅ and the regret as defined in Equation 4 is
minimized.
Output: For all ai ∈ A, the corresponding Seed Set Si and its expected
influence I(Si).
The symbols and notations used in this paper has been mentioned in Table 1.
Next, we proceed to describe the hardness result of the problem.
T able 1: Symbols and Notations with Their Interpretations
Notation Description
G(V, E, P) The social network
V, E Nodes and edges of G
n, m Number of nodes and edges of G
P Edge weight function of G
(uiuj ) An arbitrary edge of G
P r(ui, uj ) Influence probability between users ui and uj
N (ui) Neighbor set of user ui
A Set of advertisers
ℓ Number of advertisers
Si Seed set for advertiser ai
I(Si) Influence of seed set Si
R(Si) Regret for advertiser ai with seed set Si
R(u|Si) Marginal regret decrease for user u wrt Si
σi Influence demand of advertiser ai
Bi Budget of advertiser ai
C(ui) Selection cost of user ui
γ Influence penalty ratio
δ Cardinality penalty ratio
λ Demand-supply ratio
ω Average individual demand ratio
Π Allocation of seed set to advertiser
k Regret tolerance parameter
R+ 0 Set of non-negative real numbers
9

4 Proposed Solution Approaches
In this section we describe the proposed solution approaches. Initially, we start by
defining the notion of marginal decrease in regret which has been stated in Definition
7.
Definition 7 (Marginal Decrease in Regret) . Given a Social Network G(V, E, P), for
any advertiser ai ∈ Athe corresponding seed set is Si. The marginal decrease in regret
for the user u with respect to the seed set Si is denoted by R(u|Si) and defined as the
difference between the regret values when the user u has not been included and when
not. Mathematically, this can be expressed in Equation
R(u|Si) = R(Si) − R(Si ∪ {u}) (6)
4.1 Budget Effective Greedy (BG) Approach
On the basis of Definition 7 first we describe budget effective greedy approach. The
idea for this approach is to select the nodes which are within the budget and also gives
us the minimum regret. Hence, it is named Budget Effective Greedy Approach. Here
we explain how this approach actually works and it is as follows.
Algorithm 1 is a heuristic greedy approach. In Line No. 1, we order all the adver-
tisers based on the budget effectiveness i.e., budget over influence demand. We also
initialize empty set Q of seed sets for each advertiser (Line No. 2). Next, in Line No.
3 to 8 a greedy heuristic is employed to select seed nodes that can reduce the regret
(i.e., maximizing (R(Qi) − R(Qi ∪ {u})/I({u}))) best to the advertisers. After all the
advertisers are satisfied or influence provider runs out of seed nodes, Algorithm 1 will
return seed nodes set Q (Line No. 9).
Now, we analyze Algorithm 1 to understand its time and space requirement. For all
the advertisers, computing their budget per unit influence will take O(n) time. Then
sorting the advertisers based on this value will take O(n log n) time. Hence, Line No.
1 will take O(n log n) time to execute. Line No. 2 is an assignment statement and it
will take O(1) time. The for loop at Line No. 3, will execute O(n) times. However, it
is important to infer how many times the while loop in Line No. 4 will execute. We
have infrared this in the following way. Consider Cmin denotes the minimum selection
cost among all the users, i.e., Cmin = min u∈V C(u). So, for the i-th advertiser in the worst
case, the while loop can execute at most ⌈ Bi Cmin ⌉ times. Now, it can be observed that for any advertiser aj ∈ A, maximum number of times the while loop is executed is
max
aj ∈A
⌈ Bj Cmin ⌉. We call this quantity as x. Now, considering the fact that the diffusion
is happening based on the IC Model, computing the element which reduces the regret
the most can be found in O(n2 · (m + n)) time. All the statements in Line No. 6, 7,
and 8 will take O(1) time to execute where x = max
aj ∈A
⌈ Bj Cmin ⌉. Hence, the total time
requirement by Algorithm 1 will be of O(n log n + x · n3 · (m + n)) and this reduces to
O(x · n3 · (m + n)). The extra space consumed by Algorithm 1 to store the marginal
gain of the users which will take O(n) in the worst case. Hence, Theorem 2 holds.
10

Theorem 2. The running time and space requirement of Algorithm 1 will be of O(x ·
n3 · (m + n)) and O(n), respectively.
Algorithm 1: Budget Effective Greedy Approach for the RMSMA Problem
Input : The Social Network G(V, E, P), The Set of Advertisers
A = {a1, a2, . . . , al}, Their Influence Demand and Corresponding
Budget (σi, Bi)l i=1
Result: An allocation Π
1 Order each advertiser ai ∈ Abased on descending order of Bi σi ;
2 Initialize Π = {S1, S2, . . . Sl};
3 for i = 1 to l do
4 while I(Si) < σi and Bi > 0 and |V| ̸= 0 do
5 u∗ ← −argmax
u∈V
R(Si)−R(Si∪{u})
I({u}) ; Si ← Si ∪ {u∗};
6 V ← V \ {u∗}; Bi ← Bi − C(u∗);
7 return Π;
4.2 Advertiser Elimination Approach (AEA)
Our second proposed approach is the Advertiser Elimination Approach for the
RMSMA Problem which is a two step strategy. This approach is an improvised version
of the Algorithm 1. In first step, The idea of this approach is that it allocates resources
in a social network to meet advertisers’ influence demands while respecting their bud-
get constraints. After that if multiple advertisers remain undersatisfied, the algorithm
strategically eliminates the least promising candidate based on a secondary budget-
to-demand sorting, ensuring computational efficiency and a more focused allocation.
That’s why we call it Advertiser Elimination Approach. Ultimately, this approach bal-
ances influence maximization with cost constraints, yielding an allocation that strives
to satisfy maximum advertisers within the available network resources. Technically, in
this approach, first the advertisers are sorted in descending order based on the budget
per unit influence demand value. Next, we initialize the seed set for all the advertisers.
Now, for each advertiser, we perform the following task. Until the influence demand
is satisfied, budget and non seed node is available, we keep on finding the node that
leads to the maximum decrease in regret within the available budget. The node is
added to the seed set of the corresponding advertiser and the selection cost of the
node is subtracted from the available budget. Next, we count the number of advertiser
and the set of advertisers whose influence demand has not been satisfied. If this num-
ber of unsatisfied advertisers is more than k (where k is the input parameter called
regret tolerance) then the unsatisfied advertisers are sorted in ascending order based
on the budget per unit influence demand value. In this sorted list, the first advertiser
is one who expects more influence by spending less budget, and of course, making such
advertisers satisfied does not make much sense. Hence, we remove the first advertiser
11

in the sorted list and the same process is repeated. Algorithm 2 describes the process
in the form of pseudocode.
Algorithm 2: Advertiser Elimination Approach for the RMSMA Problem
Input : The Social Network G(V, E, P), The Set of Advertisers
A = {a1, a2, . . . , al}, Their Influence Demand and Corresponding
Budget (σi, Bi)l i=1, Regret Tolerance parameter k
Result: An allocation Π
1 Order each advertiser ai ∈ Abased on descending order of Bi σi ;
2 Initialize Π = {S1, S2, . . . Sl}, k;
3 while T RU Edo
4 for each ai ∈ Ado
5 while I(Si) < σi and Bi > 0 and |V| ̸= 0 do
6 u∗ ← −argmax
u∈V
R(Si)−R(Si∪{u})
I({u}) ; Si ← Si ∪ {u∗};
7 V ← V \ {u∗}; Bi ← Bi − C(u∗);
8 count = 0, Au = [ ];
9 for each ai ∈ Ado
10 if I(Si) < σi then
11 count = count + 1; Au[count] ← ai;
12 if count ≥ k then
13 Au ← sort each advertiser ai ∈ Au in ascending order of Bi σi ;
14 A ← A \ Au[1]
15 return Π;
We analyze Algorithm 2 to understand its time and space requirement. As men-
tioned previously, execution of Line No. 1 will takeO(n log n) time. It is easy to observe
that in the worst case, the while loop at Line No. 3 will execute O(n − k + 1) times. In
worst case scenario whenk ≪ n then it will run inO(n) time. As mentioned previously,
similar to the Algorithm 1 Line No. 4 to 8 in the Algorithm 2 will takeO(x·n3 ·(m+n))
time. Next, in Line No. 9 initializing count, Au will take time O(n) each and in Line
No. 11 to 15 will take O(n) time to execute. Line No. 16 the if condition can be satis-
fies closer to n times in the worst case and in Line No. 17 sorting advertisers will take
O(n log n) time. So, Line No. 16 to 19 will take O(n log n) time. Therefore, the total
time taken by Algorithm 2 will be of O(n((x · n3.(m + n)) + n + (n log n))) and this
will be reduced to O((x · n4(m + n)). The additional space requirement for Algorithm
2 will be of O(n). Hence, the following theorem statement holds.
Theorem 3. The running time and space requirement of Algorithm 2 will be of O((x ·
n4(m + n)) and O(n), respectively.
12

4.3 Advertiser Driven Local Search (ADLS) Approach
Our third approach, the Advertiser Driven Local Search Approach for the RMSMA
Problem is again a two step heuristic designed to efficiently allocate social network
nodes to multiple advertisers while balancing their influence demands and budget con-
straints. In the initial step, advertisers are prioritized by their budget to influence
demand ratios, and a greedy strategy is used to iteratively assign nodes each chosen
to maximize the reduction in overall regret relative to the influence it provides until
the advertiser’s influence requirement is met or budget exhausted. After this initial
allocation, in second step the algorithm calculates a threshold based on the average
regret and identifies advertisers whose regret exceeds this level. For these under sat-
isfied advertisers, a localized reallocation is triggered, where the greedy process is
reapplied using the remaining network nodes and updated budgets to further improve
the allocation. This local search refinement helps enhance overall satisfaction, ensuring
a more balanced and cost effective resource distribution across all advertisers. Hence,
we call it an Advertiser Driven Local Search Approach.
Here we understand our third approach line by line as written in Algorithm 3. The
first step will be to sort advertisers in decreasing order of their budget to demand ratio
Bi
σi as done in our previous algorithms, Algorithm 1 and Algorithm 2. This prioritizes advertisers with a higher “value for money” ensuring more efficient budget usage. Next,
we will initialize allocation set for each adveriser as empty set and initialize the regret
for all advertiser with the initial regret value. After all the initialization we will do the
further exploration by iterating over each advertiserai. For each advertiser, repeatedly
allocate nodes until the total influence I(Si) of the nodes in Si meets or exceeds the
influence demand σi or the budget Bi of the advertiser is exhausted or there are no
remaining nodes in V. Identify the node u∗ from the remaining set V that provides
the highest marginal gain per unit of influence when added to Si. The marginal gain
is measured by the decrease in regret R(Si) when u is added, divided by the influence
I(u) provided by u. Once all the advertisers are processed we will have their allocated
seed set, influence and regret. Thereafter, we compute the threshold τ as the average
of all advertisers’ regret values. This threshold identifies advertisers with significantly
higher regret. So, we identify advertisers whose regret exceeds the threshold τ . These
advertisers are considered underperforming and require further attention. If there are
any high-regret advertisers then we rerun the greedy allocation (Lines 5–11) for these
advertisers. For allocating the seed set for these advertisers we will allocate the seed
nodes from the remaining nodes of the previous run and the allocated nodes of the
advertisers having regret higher than the threshold. The outcome of this will be the
Π with the new allocations and hence, the final allocation Π for all advertisers.
We analyze Algorithm 3 to understand its time and space complexity. In Line No.
1, ordering all advertisers in decreasing manner on the basis of the ratio Bi σi will take O(n log n) time. The Line No. 2 will take O(n) time to execute. The Line No. 3 will
execute O(n) times. The while loop in this algorithm will execute in O(x · n2(m + n))
times which is same as discussed in Algorithm 1. In while loop O(1) time will be taken
to execute Lines 6, 7 and 8 each. Hence, this part of the Algorithm 3 from Line No. 3
to 10 will take O(x · n3(m + n)) time to execute. The mean calculation at the Line No.
11 will be in O(n) time. The time taken to identify the advertisers with the high regret
13

Algorithm 3: Advertiser Driven Local Search Approach for the RMSMA
Problem
Input : The Social Network G(V, E, P), The Set of Advertisers
A = {a1, a2, . . . , al}, Their Influence Demand and Corresponding
Budget (σi, Bi)l i=1
Output: An Allocation Π
1 Order each advertiser ai ∈ Abased on descending order of Bi σi ;
2 Initialize Π = {S1, S2, . . . , Sl};
3 for i = 1 to l do
4 while I(Si) < σi and Bi > 0 and |V| ̸= 0 do
5 u∗ ← −arg max
u∈V
R(Si)−R(Si∪{u})
I({u}) ;
6 Si ← Si ∪ {u∗};
7 V ← V \ {u∗};
8 Bi ← Bi − C(u∗);
9 Calculate the threshold τ as a function of average regret: τ ← −mean(R);
10 Identify advertisers with high regret: Ahigh = {ai ∈ A |ri > τ};
11 if Ahigh ̸= ∅ then
12 for i = 1 to |Ahigh| do
13 Re-run the greedy algorithm (from Line 4 - 9) with the remaining
nodes in V and their allocated budgets B respectively;
14 Update Π accordingly;
15 return Π;
in Line No. 12 will be O(n). The Line No. 13 will take O(1) time for comparison. And
afterwards, again we run the greedy method, so the same time O(x · n2(m + n)) will
be taken from Line No. 15. Overall, from Line No. 13 to 18, it takes O(x · n3(m + n)).
Hence, the total time requirement is O(n log n + x · n3(m + n) + x · n3(m + n)) which
finally reduces to O(x·n3(m+n) time. The additional space requirement for Algorithm
3 will be of O(n). Hence, Theorem 4 holds.
Theorem 4. The running time and space requirement of Algorithm 3 will be of O(x ·
n3(m + n) and O(n), respectively.
An Illustrative Example.
Consider an influence provider with a social network G, contains 12 nodes V =
{u1, u2, . . . , u12} with corresponding individual influence value and six advertisers
A = {a1, a2, . . . , a6} with individual influence demands reported in Table 2a and 2b,
respectively. So, the order of budget effective advertisers is < a2, a1, a4, a3, a5, a6 >. In
the seed node allotment of Algorithm 1 advertiser a1, a2, a3, a4 are fully satisfied with
no excessive regret (ER) or unsatisfied regret (UR) however advertiser a5 and a6 not
satisfied due to the seed node runs out i.e., |S| = ∅ as shown in Table 2c. Next, when
the social network and advertiser information shown in Table 2a and 2b used in Algo-
rithm 2 by setting the regret tolerance parameter k = 1, advertiser a6 is removed
14

from the advertiser set. The allocation of nodes is presented in Table 2d. The “ADLS”
approach extends the “AEA” approach to minimize the regret further. Table 2e shows
that the allocation from the “AEA” approach advertiser a3, a4, a5 and a6 are reallo-
cated because these advertiser generate regrets. After reallocation, advertiser a6 only
generates regret, i.e., unsatisfied regret as presented in Table 2e. Hence, the “ADLS”
approach minimize the regret better.
Table (2) Illustrative Example
V u1 u2 u3 u4 u5 u6 u7 u8 u9 u10 u11 u12
σ(ui) 4 6 5 4 5 2 3 2 3 2 2 5
Cost(ui) $6 $9 $7.5 $6 $7.5 $3 $4.5 $3 $4.5 $3 $3 $7.5
(a) Nodes information.
A a1 a2 a3 a4 a5 a6
σi 10 8 6 10 9 5
Bi $18 $17 $10 $17 $11 $5
(b) Advertisers information.
A a1 a2 a3 a4 a5 a6
S {u3, u12} {u2, u6} {u4, u7} {u1, u5, u8} {u9, u10, u11} {}
Satisfied Y Y Y Y N N
Regret - - ER ER UR UR
(c) Allotment after the “BG” approach.
A a1 a2 a3 a4 a5
S {u3, u12} {u2, u6} {u4, u7} {u1, u5, u8} {u9, u10, u11}
Satisfied Y Y Y Y N
Regret - - ER ER UR
(d) Allotment after the “AEA” approach.
A a1 a2 a3 a4 a5 a6
S {u3, u12} {u2, u6} {u1, u8} {u5, u9, u10} {u4, u7, u11} {}
Satisfied Y Y Y Y Y N
Regret - - - - - UR
(e) Allotment after the “ADLS” approach.
5 Experimental Details
In this section, we describe the experimental evaluation of the proposed solution
approach. Initially, we start by describing the datasets.
5.1 Dataset Description
Now, we describe the datasets that we have used in our experiments.
15

• Congress-Twitter Dataset [49]: This network represents the Twitter interac-
tion network for the 117th United States Congress, both House of Representatives
and Senate. The base data was collected via the Twitter’s API, then the empir-
ical transmission probabilities were quantified according to the fraction of times
one member retweeted, quote tweeted, replied to, or mentioned another member’s
tweet.
• Email-Eu-Core Dataset [50] The network was generated using email data from
a large European research institution. The information about all incoming and
outgoing email between members of the research institution is anonymized by
them. There is an edge (u, v) in the network if person u sent person v at least one
email. The e-mails only represent communication between institution members
(the core), and the dataset does not contain incoming messages from or outgoing
messages to the rest of the world.
• F acebook Dataset[51]: This dataset consists of ‘circles’ (or ‘friends lists’) from
Facebook. Facebook data was collected from survey participants using this Face-
book app. The dataset includes node features (profiles), circles, and ego networks.
However, in this study, we have not considered any node feature.
• Wikivote Dataset [52] The network contains all the Wikipedia voting data
from the inception of Wikipedia till January 2008. Nodes in the network represent
wikipedia users and a directed edge from node i to node j represents that user i
voted on user j.
The basic statistics of the datasets has been mentioned in Table 3.
Dataset Type Number
of Nodes
|V|
Number
of Edges
|E|
Average
Degree
davg
Maximum
Degree
dmax
Congress-Twitter Directed 475 13289 55.95 284
Email-Eu-Core Directed 1005 25571 50.88 546
Facebook Undirected 4039 88234 43.69 1045
Wikivote Directed 7115 103689 29.15 1167
T able 3: Description of Graph Datasets
5.2 Experimental Setup
In our study, there are following parameters whose value need to be set up.
Influence Probability
In our experiments, we have used the following two influence probability set up: (i)
Uniform and (ii) Trivalency. In Uniform probability setting, all the edges of the network
will have the same probability value, i.e., for all ( uiuj) ∈ E, P(ui, uj) = pc. In this
study, we have considered value of pc = 0.1. In the Trivalency setting, the influence
probability of each edge is chosen uniformly at random from the set {0.1, 0.01, 0.001}.
16

Selection Cost of the Users
In this study, we have considered the degree proportional cost setting . This setting
has also been considered [53]. This means that more the degree of an user, more
costly the user is to select as seed node. The selection cost of any user u is defined as
C(u) = h · (|V|/ P v∈V deg(v)) · deg(u). Here, h is a constant and in our study we have
considered the value of h is 1000.
The Number of Advertisers
We have considered the following values as the number of advertisers: 5, 10, 20, 50,
and 100.
5.2.1 Key Parameters
All the key parameters are summarized in Table 4. This table includes the demand-
supply ratio (λ), average individual demand ratio (ω), influence penalty ratio (γ), and
cardinality penalty ratio (δ). In each experiment, we vary only one parameter and set
the remaining parameter in the default setting (highlighted in bold).
T able 4: Key Parameters
Parameter Values
λ 40%, 60%, 80%, 100%, 120%
ω 1%, 2%, 5%, 10%, 20%
γ 0, 0.25, 0.5, 0.75, 1
δ 0.01, 0.02, 0.03, 0.04, 0.05
Demand Supply Ratio λ
It refers to the ratio of global influence demand of the advertisers over the influence
provider influence supply, i.e., λ = I d/I s, where I d = Pn i=1 Ii represent the global
influence demand and I s = P s∈S I({s}) is the influence provider supply. We have
considered five values of λ, i.e., 40% , 60%, 80%, 100%, 120%, which denotes low,
medium, high full, and excessive, respectively.
Average Individual Demand Ratio ω
It is the percentage of average individual demand of the advertisers over the influ-
ence provider supply i.e., ω = I avg /I s, where I avg = I d/|A| is the average individual
demand of the advertisers. This parameter is useful for simulating the individual
demands of the advertiser.
Advertisers Demand I
Once the I d is fixed, I avg can be easily computed i.e., I avg = ω · Is. Also, we can
generate the influence demand of each advertiser using I a = ⌊α · Is · ω⌋, where α is a
factor randomly generated to simulate different demand setting.
17

Advertiser Payment B
We set the payment of an advertiser as proportional to his influence demand, Ba =
⌊β · Ia⌋, where β is a parameter to simulate different payment.
Influence Penalty Ratio γ
This parameter decides the penalty imposed on the influence provider due to the
influence supply to the advertisers. We vary γ from 0 , 0.25, 0.5, 0.75, 1, where two
extreme cases when γ = 0, the influence provider cannot receive any payment if
the advertisers required influence is satisfied and when γ = 1, the influence provider
can receive the same fraction of payment the fraction of influence he provides to the
advertisers.
Cardinality Penalty Ratio δ
This parameter imposes a penalty if the influence provider provides less or more
amount of influence to the advertiser based on the cardinality of the allocated seed
set to the advertisers. We vary δ from 0.01, 0.02, 0.03, 0.04, 0.05 to simulate different
penalties imposed on the advertiser.
5.2.2 Other Setups
Environment Setup
All the codes are implemented in Python and executed on HPC cluster run under
CentOS-7.8 (a specific version of Red Hat Enterprise Linux). The processor archi-
tecture of HPC cluster is for CPU node is Intel Xeon Gold 6248 with 32 GB
memory.
Performance Metrics
The effectiveness metrics measure total regret, including unsatisfied and excessive
regret. The efficiency metrics include the running time of the proposed approaches.
5.3 Baseline Methods
We compared our proposed approaches with the following baseline methods.
Random
In this baseline method we randomly select the nodes of the graph within the assigned
payment B.
Top-K
The top influential users are selected within the assigned payment B.
5.4 Goals of the Experimentation
In this study, we have fixed the following research questions (RQ) and through our
experimental study we have found out the explanations of these questions.
18

• RQ1: What will happen if we increase the global influence demand ( I d) of the
advertisers to low, normal, high, full and excessive.
• RQ2: Which kind of advertisers are more beneficial for the influence providers
perspective. A small number of advertisers with high individual influence demand
or large number of advertisers with small individual influence demand.
• RQ3: How the computational time varies when we vary λ, ωand γ for the
proposed and baseline methods.
5.5 Experimental Results and Discussion
Now, we report the obtained results from our experiments and describe them in order
to get the answers of the research questions.
5.5.1 Effectiveness Study
At first we evaluate how varying λ and ω impacts the total regret. This total regret
includes unsatisfied and excessive regret and we report each of them separately in our
experiments. The experiments for each datasets are conducted for two different prob-
ability settings, Uniform (0.1) and Trivalency. Now, to ease our discussion we consider
four different cases for each dataset. We examine four distinct cases that represent
different combinations of global ( λ) and individual ( ω) influence demands. In Case
1, both the global and individual influence demands are low, meaning the influence
provider serves a large number of advertisers with modest requirements. Case 2 fea-
tures low global but high individual influence demand, leading to fewer advertisers
with significantly larger influence requirements and a unique interplay between exces-
sive and unsatisfied regret. In Case 3, high global influence demand coupled with low
individual influence demand creates a scenario where most advertisers receive suffi-
cient influence, though the overall allocation efficiency varies. Finally, Case 4 considers
the situation where both global and individual influence demands are high, resulting
in a dynamic interplay: while increased individual influence demand can reduce exces-
sive regret, it may also raise unsatisfied regret if advertiser requirements are not fully
met. These cases provide a comprehensive framework for analyzing and comparing the
performance of different allocation algorithms under diverse demand conditions.
Case 1: low λ, low ω
In Case 1, we consider scenarios whereλ ≤ 60% and ω ≤ 30%, indicating that both the
global and individual influence demands from advertisers are low. This implies that
the influence provider serves a large number of advertisers with relatively low influence
requirements. Since λ is small, the global influence demand remains significantly lower
than the available supply. In both probability settings, we observe that as global
influence demand increases, excessive regret also rises.
Now, firstly we analyse Uniform (0.1) probability setting results. In Email-Eu-Core
dataset (Figures 2 (a) & (b) and 3 (a) & (b)), the best performing algorithm is “ADLS”
with an average total regret of 2061 .31. The “Top-K” algorithm performs the worst,
with 4695.14% higher regret than “ADLS”. “BG” and “AEA” perform relatively well
but still show 16 .01% and 25 .04% higher regret than “ADLS”. In Facebook dataset
19

(Figures 12 (a) & (b) and 13 (a) & (b)), the best performing algorithm is “ADLS”
with an average total regret of 3563 .17. The highest regret is from “Top- K”, which
is 15806 .38% worse than “ADLS”. “BG” and “AEA” perform moderately but still
show 24.20% and 24 .20% higher regret than “ADLS”. In Wikivote dataset (Figures
22 (a) & (b) and 23 (a) & (b)), “ADLS” achieved the lowest total regret across
multiple instances. For example, in one instance (Figure (22 (a)), “ADLS” had a total
regret of 2294 .16, whereas “Random” and “Top- K” had significantly higher values
(222618.28 and 367158.72, respectively). This represents an improvement of over 98%
compared to “Random”, proving “ADLS”’s effectiveness in minimizing regret. In Table
5, we observe Congress-Twitter dataset. In it “Random” and “Top- K” algorithms
consistently yield the highest regret across all scenarios. For instance, at λ = 60%,
ω = 10%, the regret for “Top- K” is 29737 .52, whereas “BG” achieves a significantly
lower regret of 19828 .20. The “BG”, “AEA”, and “ADLS” algorithms consistently
outperform “Random” and “Top- K”, reducing regret by 20 − 75% in most cases.
Now we analyse Trivalency probability setting results of all datasets for this case.
In Email-Eu-Core dataset (Figures 7 (a) & (b) and 8 (a) & (b)), the best perform-
ing algorithm is “ADLS” with an average total regret of 1920 .50. The highest regret
is from “Top-K”, which is 779 .16% worse than “ADLS”. “BG” and “AEA” perform
moderately but still show approximately 65.16% higher regret than “ADLS”. In Face-
book dataset (Figures 17 (a) & (b) and 18 (a) & (b)), the best performing algorithm
is “ADLS” with an average total regret of 1998 .71. The highest regret is from “Top-
K”, which is 10391 .13% worse than “ADLS”. “BG” and “AEA” perform moderately
but still show 38 .53% and 38 .53% higher regret than “ADLS”. In Wikivote dataset,
in this case, the total regret is analyzed across different algorithms and shown in
Figures 27 (a) & (b) and 28 (a) & (b). From the dataset results, the “ADLS” algo-
rithm consistently achieves the lowest total regret compared to others. For example,
in the Wikivote dataset, in percentage terms, “ADLS” achieves an improvement of
approximately 10 − 25% compared to “BG” and “AEA”, making it the best perform-
ing algorithm in this case. In Table 6 for Congress-Twitter dataset, “BG” algorithm
consistently achieves the lowest regret, followed closely by “AEA” and “ADLS”. In
contrast, “Random” and “Top- K” exhibit significantly higher regret, making them
less effective choices. As λ increases, regret increases across all methods, but “BG”
maintains its advantage, demonstrating superior optimization.
Case 2: Low λ, High ω
In Case 2, we consider scenarios where λ ≤ 60% and ω ≥ 50%. Here, the global
demand remains low, but the individual influence demand is significantly higher. This
implies that the influence provider serves a smaller number of advertisers with larger
influence requirements. In both probability settings, we observe that as individual
influence demand increases, the overall regret decreases. While global demand remains
constant, the increasing individual demand leads to a reduction in excessive regret,
thereby lowering total regret. However, we also notice the emergence of unsatisfied
regret, indicating that some advertiser demands are not being fully met. Our algo-
rithms—“BG”, “AEA”, and “ADLS”—consistently outperform the baseline methods.
Our observations under Uniform probability setting is as follows. In Email-Eu-Core
20

dataset (Figures 4 (a) & (b), 5 (a) & (b) and 6 (a) & (b)), “ADLS” remains the best
with an average regret of 691.83. “BG” performs better than “Random” and “Top-K”
but is 0 .06% worse than “ADLS”. The “Random” algorithm has the highest regret,
performing 2347.09% worse than “ADLS”. In Facebook dataset (Figures 14 (a) & (b),
15 (a) & (b) and 16 (a) & (b)), “ADLS” is the best with an average regret of 1340 .51.
“BG” performs better than “Random” and “Top-K” but is 5.26% worse than “ADLS”.
The “Random” algorithm has significantly high regret, performing “5580.58%” worse
than “ADLS”. In Wikivote dataset (Figures 24 (a) & (b), 25 (a) & (b) and 26 (a) &
(b)), for higher individual advertiser demand, “ADLS” still performed the best, with
minimal regret values. For example, in one instance in Figure 24 (a), “ADLS” had
a total regret of 15212 .98, whereas “Random” had 37012 .21, showing a decrease of
approximately 58.9%. This consistent reduction highlights “ADLS”’s ability to manage
higher advertiser demands effectively. In Congress dataset, from Table 5, we observe
that “Random” and “Top-K” continue to yield significantly higher regret compared to
“BG”, “AEA”, and “ADLS” in most instances. Among all methods, “BG” consistently
achieves the lowest regret, making it the best-performing algorithm in this setting. At
ω = 90%, regret is negligible across all methods, indicating efficient allocation at high
influence demand.
These performance trends are consistent across all datasets under Trivalency prob-
ability settings. In Email-Eu-Core (Figures 9 (a) & (b), 10 (a) & (b) and 11 (a) &
(b)), “ADLS” is the best with an average regret of 5741 .57. “BG” performs better
than “Random” and “Top- K” but is 31 .42% worse than “ADLS”. The “Random”
algorithm has significantly high regret, performing 41 .99% worse than “ADLS”. In
Facebook dataset (Figures 19 (a) & (b), 20 (a) & (b) and 21 (a) & (b)), “ADLS” is
the best with an average regret of 6485.85. “BG” performs better than “Random” and
“Top-K”. The “Random” algorithm has significantly high regret, performing 334.91%
worse than “ADLS”. In Wikivote dataset (Figures 29 (a) & (b), 30 (a) & (b) and 31
(a) & (b)), for advertisers with low global demand but high individual demand, the
“ADLS” algorithm again reports the lowest regret. For Congress-Twitter dataset in
Table 6, algorithms “BG”, “AEA”, and “ADLS” perform better than “Random” and
“Top-K” in this setting. At ω = 90%, regret is minimal across all methods, indicat-
ing that higher individual influence demand leads to efficient allocation. Despite this,
“Top-K” and “Random” remain the worst-performing methods.
Case 3: High λ, Low ω
In Case 3, we consider scenarios where λ ≥ 80% and ω ≤ 30%. Here, the global
demand is high, but the individual influence demand from advertisers remains low.
As λ increases, the influence provider has access to the maximum or entire supply
available to distribute among advertisers. Since ω is still low, it is expected that most
or all advertisers can be provided with sufficient influence. Our observations indicate
that as individual influence demand increases, regret decreases when the global influ-
ence demand remains constant. Conversely, when individual demand is held constant,
increasing the global influence demand does not significantly impact regret, either pos-
itively or negatively. We will firstly understand the results from the Uniform probaility
setting. In Email-Eu-Core dataset (Figures 2 (c)-(e) and 3 (c)-(e)), “ADLS” continues
21

to outperform with the lowest regret of 1803 .08. “BG” and “AEA” show moderate
results but still have 13 .33% and 12 .83% higher regret than “ADLS”. “Top- K” has
the worst performance, with regret being 5667 .82% higher than “ADLS”. In Face-
book dataset (Figures 12 (c)-(e) and 13 (c)-(e)), “ADLS” continues to be the best
with the lowest regret of 4537 .30. “BG” and “AEA” show higher regret by 34 .12%
and 34.12% compared to “ADLS”. “Top- K” has the worst performance, with regret
being 11147.15% higher than “ADLS”. In Wikivote dataset (Figures 22 (c)-(e) and 23
(c)-(e)), when global influence demand is high but individual demand is low, “ADLS”
remained the best performing algorithm. Anotable instance in Figure 22 (c) showed
“ADLS” achieving a total regret of 3716 .52, whereas “Random” and “Top- K” had
much higher values of 234796.95 and 314244.96, respectively. This represents a reduc-
tion of over 98% compared to “Random”, emphasizing “ADLS”’s efficiency. Both
“Random” and “Top- K” exhibit extremely high regret across all scenarios, making
them unsuitable choices in Congress-Twiiter dataset as listed in Table 5. For exam-
ple, at λ = 80%, ω = 10%, with |A| = 100, the regret for “Top- K” is 49987 .67, while
“AEA” achieves a significantly lower regret of 29574 .21. In most cases, “AEA” and
“ADLS” outperform “BG” by 10 − 30%, demonstrating superior regret minimization.
Under the Trivalency probability setting, our proposed algorithms continue to
perform better across all datasets, further validating their robustness in minimizing
regret. To support our statement we see in Figures 7 (c)-(e) and 8 (c)-(e) of Email-Eu-
Core dataset that “ADLS” continues to be the best with the lowest regret. “BG” and
“AEA” show higher regret by maximum 85 .22% compared to “ADLS”. “Top- K” has
the worst performance, with regret being 204 .37% higher than “ADLS”. In Facebook
dataset (Figures 17 (c)-(e) and 18 (c)-(e)), ADLS continues to be the best with the
lowest average regret of 2237.80. “BG” and “AEA” show higher regret by 79 .02% and
79.02% compared to “ADLS”. “Top-K” has the worst performance, with regret being
7868.41% higher than “ADLS”. In Wikivote dataset (Figures 27 (c)-(e) and 28 (c)-(e))
for advertisers with high global demand but low individual demand, “ADLS” remains
the best performer. “Regret” values are the highest across all methods in Table 6 for
Congress-Twitter dataset, suggesting that low individual influence demand (ω) results
in inefficient allocation. The “BG” algorithm performs better than “Top-K” and “Ran-
dom”, but at λ = 120%, regret reaches its peak across all methods, confirming that
high global influence demand with low individual demand is problematic.
Case 4: High λ, High ω
In Case 4, we consider scenarios where λ ≥ 80% and ω ≥ 50%. Here, both global
demand and individual influence demand are high. As the global demand λ increases,
excessive regret decreases, but unsatisfied regret increases. Consequently, each unsatis-
fied advertiser contributes to a higher total regret. When individual demand increases
while keeping the global influence demand constant, regret decreases. However, when
global influence demand increases, regret also increases. This is because a higher global
influence demand results in a proportional increase in individual influence demand,
thereby contributing to higher regret. The results of Uniform probbility setting are as
follows. In Email-Eu-Core dataset (Figures 4 (c)-(e), 5 (c)-(e) and 6 (c)-(e)), “ADLS”
achieves the lowest average regret at 7949.21. “BG” and “AEA” are significantly worse,
22

with regrets maximum to 4 .43% higher than “ADLS”. The “Random” algorithm per-
forms the worst again, with a regret 61.48% higher than “ADLS”. In Facebook dataset
(Figures 14 (c)-(e), 15 (c)-(e) and 16 (c)-(e)), “ADLS” achieves the lowest average
regret at 10556.87. “BG” and “AEA” perform significantly worse, with regrets 1 .46%
and 1.60% higher than “ADLS”. The “Random” algorithm is again the worst, with a
regret that is 417 .71% higher than “ADLS”. In Wikivote dataset (Figures 24 (c)-(e),
25 (c)-(e) and 26 (c)-(e)), in the scenario where both global and individual influ-
ence demands are high, “ADLS” continued to outperform the other algorithms. In
one case (Figure 26 (e)), it achieved a total regret of 210489 .62, whereas “Random”
had 210875.27, indicating an overall improvement. While the percentage difference is
lower here, “ADLS” still maintains its superiority in regret minimization. In Congress-
Twitter dataset, from the Table 5 we see that as ω increases from 50% to 70%, regret
values drop significantly across all methods, indicating that higher individual influ-
ence demand leads to better optimization. For example, at ω = 50%, λ = 80%, the
regret values are as follows.“BG” has lowest regret of 612 .18, “AEA” has 544 .19, and
“ADLS” has 183 .18. While “ADLS” is not always the best, it achieves the lowest
regret in certain instances, particularly when λ = 80%, ω = 70%. “Top-K” should be
avoided, as it consistently exhibits the highest regret across all scenarios.
Our observation for Trivalency probability setting is as follows. For Email-Eu-Core
dataset (Figures 9 (c)-(e), 10 (c)-(e) and 11 (c)-(e)), “ADLS” achieves the lowest aver-
age regret at 20015 .18. “BG” and “AEA” perform significantly worse, with regrets
12.25% and 8.49% higher than “ADLS”. The “Random” algorithm is again the worst,
with a regret that is 6.05% higher than “ADLS”. In Facebook dataset (Figures 19 (c)-
(e), 20 (c)-(e) and 21 (c)-(e)), “ADLS” achieves the lowest average regret at 45297.33.
“BG” and “AEA” perform significantly worse, with regrets 1 .51% and 0 .02% higher
than “ADLS”. The “Random” algorithm is again the worst, with a regret that is
19.59% higher than “ADLS”. In Wikivote dataset (Figures 29 (c)-(e), 30 (c)-(e) and
31 (c)-(e)), when both global and individual demand are high, the results indicate that
“ADLS” continues to be the optimal algorithm. For instance, in the Wikivote dataset,
“ADLS” records a total regret of around 1294, while “BG” and “AEA” exceed 1500.
The percentage difference highlights a 20 − 25% improvement, reinforcing the robust-
ness of “ADLS” across different demand scenarios. In Trivalency probability setting,
for Congress-Twitter dataset, regret values drop significantly as observed in Table 6,
reinforcing the idea that higher ω leads to better optimization. The algorithms “BG”,
“AEA”, and “ADLS” perform similarly, with minimal differences in regret values. At
ω = 70%, all methods converge to similar regret values, indicating diminishing returns
of increasing individual demand. Despite the improvement in regret, “Top-K” and
“Random” remain the least effective choices.
Comprehensive Observation
In conclusion, our analysis across all four cases reveals that the performance of the
evaluated algorithms is highly sensitive to the variations in global ( λ) and individual
(ω) influence demands. In scenarios with low λ and ω (Case 1), where the overall
demand is modest, the “ADLS” algorithm consistently minimizes regret significantly
better than alternatives such as “Top- K” and “Random”, while “BG” and “AEA”
23

perform moderately well. When individual influence demand is high despite low global
demand (Case 2), the overall regret decreases, yet unsatisfied advertiser demands
emerge, with “ADLS” maintaining strong performance and “BG” often leading in
specific instances. In cases where global demand is high but individual demand remains
low (Case 3), the abundance of available influence results in lower regret levels, again
favoring “ADLS”, while “BG” and “AEA” show competitive performance. Finally,
when both global and individual demands are high (Case 4), although excessive regret
decreases and unsatisfied regret becomes a concern, “ADLS” consistently achieves
the lowest regret, and the performance gap between “ADLS” and the other methods
narrows, with “BG” and “AEA” trailing only slightly in some settings. Overall, these
findings underscore the robustness of the “ADLS” algorithm in efficiently allocating
influence across diverse demand scenarios, while simpler approaches such as “Top- K”
and “Random” prove to be considerably less effective.
24

Excessive Regret
 Unsatisfied Regret
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s48/s107
/s56/s48/s107
/s49/s50/s48/s107
/s49/s54/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s57/s57/s32/s37
/s49/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s55/s56/s32/s37
/s50/s50/s32/s37
/s56/s52/s32/s37
/s49/s54/s32/s37
/s55/s55/s32/s37
/s50/s51/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s48/s107
/s56/s48/s107
/s49/s50/s48/s107
/s49/s54/s48/s107
/s50/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s57/s57/s32/s37
/s49/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s54/s48/s32/s37
/s52/s48/s32/s37
/s56/s50/s32/s37
/s49/s56/s32/s37
/s54/s52/s32/s37
/s51/s54/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s48/s107
/s56/s48/s107
/s49/s50/s48/s107
/s49/s54/s48/s107
/s50/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s56/s48/s32/s37
/s50/s48/s32/s37
/s56/s50/s32/s37
/s49/s56/s32/s37
/s57/s49/s32/s37
/s57/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s48/s107
/s56/s48/s107
/s49/s50/s48/s107
/s49/s54/s48/s107
/s50/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s57/s57/s32/s37
/s49/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s57/s51/s32/s37
/s55/s32/s37
/s56/s48/s32/s37
/s50/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s48/s107
/s56/s48/s107
/s49/s50/s48/s107
/s49/s54/s48/s107
/s50/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s56/s53/s32/s37
/s49/s53/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 2: Regret of varying the demand-supply ratio λ when ω = 10% (Email-Eu-Core,
|A| = 100, pc : U nif orm(0.1))
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s49/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s57/s57/s32/s37
/s49/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s56/s48/s32/s37
/s50/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s57/s57/s32/s37
/s49/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s55/s49/s32/s37
/s50/s57/s32/s37
/s55/s53/s32/s37
/s50/s53/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s57/s57/s32/s37
/s49/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s54/s52/s32/s37
/s51/s54/s32/s37
/s54/s54/s32/s37
/s51/s52/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s57/s57/s32/s37
/s49/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s54/s54/s32/s37
/s51/s52/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s55/s56/s32/s37
/s50/s50/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 3: Regret of varying the demand-supply ratio λ when ω = 30% (Email-Eu-Core,
|A| = 50, pc : U nif orm(0.1))
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s57/s57/s32/s37
/s49/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s55/s49/s32/s37
/s50/s57/s32/s37
/s53/s48/s32/s37
/s53/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s107
/s50/s48/s107
/s51/s48/s107
/s52/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s53/s54/s32/s37
/s52/s52/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s49/s50/s107
/s49/s54/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s57/s57/s32/s37
/s54/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s50/s57/s32/s37
/s55/s49/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s49/s50/s107
/s49/s54/s107
/s50/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s52/s52/s32/s37
/s53/s54/s32/s37
/s53/s48/s32/s37
/s53/s48/s32/s37
/s53/s32/s37
/s57/s53/s32/s37
/s52/s32/s37
/s57/s54/s32/s37
/s53/s32/s37
/s57/s53/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s49/s50/s107
/s49/s54/s107
/s50/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s52/s55/s32/s37
/s53/s51/s32/s37
/s52/s54/s32/s37
/s53/s52/s32/s37
/s50/s32/s37
/s57/s56/s32/s37 /s54/s32/s37
/s57/s52/s32/s37
/s52/s32/s37
/s57/s54/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 4: Regret of varying the demand-supply ratio λ when ω = 50% (Email-Eu-Core,
|A| = 20, pc : U nif orm(0.1))
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s49/s50/s107
/s49/s54/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s51/s51/s32/s37
/s54/s55/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s32/s37
/s57/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s107
/s52/s107
/s54/s107
/s56/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s107
/s52/s107
/s54/s107
/s56/s107
/s49/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s55/s32/s37
/s56/s51/s32/s37
/s49/s55/s32/s37
/s56/s51/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s50/s32/s37
/s57/s56/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s49/s50/s107
/s49/s54/s107
/s50/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s52/s32/s37
/s57/s54/s32/s37
/s52/s32/s37
/s57/s54/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s49/s50/s107
/s49/s54/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s51/s32/s37
/s56/s55/s32/s37 /s49/s32/s37
/s57/s57/s32/s37
/s50/s32/s37
/s57/s56/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s49/s50/s32/s37
/s56/s56/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 5: Regret of varying the demand-supply ratio λ when ω = 70% (Email-Eu-Core,
|A| = 10, pc : U nif orm(0.1))
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s107
/s52/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s107
/s52/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s52/s53/s32/s37
/s53/s53/s32/s37
/s55/s48/s32/s37
/s51/s48/s32/s37
/s49/s52/s32/s37
/s56/s54/s32/s37
/s51/s32/s37
/s57/s55/s32/s37
/s55/s32/s37
/s57/s51/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s107
/s52/s107
/s54/s107
/s56/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s53/s32/s37
/s57/s53/s32/s37
/s53/s32/s37
/s57/s53/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s107
/s52/s107
/s54/s107
/s56/s107
/s49/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s56/s107
/s49/s54/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 6: Regret of varying the demand-supply ratio λ when ω = 90% (Email-Eu-Core,
|A| = 5, pc : U nif orm(0.1))
25

Excessive Regret
 Unsatisfied Regret
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s49/s50/s107
/s49/s54/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s54/s50/s32/s37
/s51/s56/s32/s37
/s57/s51/s32/s37
/s55/s32/s37
/s57/s48/s32/s37
/s49/s48/s32/s37
/s56/s49/s32/s37
/s49/s57/s32/s37
/s55/s50/s32/s37
/s50/s56/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s56/s107
/s49/s54/s107
/s50/s52/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s54/s52/s32/s37
/s51/s54/s32/s37
/s57/s53/s32/s37
/s53/s32/s37
/s52/s52/s32/s37
/s53/s54/s32/s37
/s56/s56/s32/s37
/s49/s50/s32/s37
/s55/s54/s32/s37
/s50/s52/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s56/s107
/s49/s54/s107
/s50/s52/s107
/s51/s50/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s53/s50/s32/s37
/s52/s56/s32/s37
/s57/s51/s32/s37
/s55/s32/s37
/s52/s48/s32/s37
/s54/s48/s32/s37
/s55/s55/s32/s37
/s50/s51/s32/s37
/s56/s52/s32/s37
/s49/s54/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s56/s107
/s49/s54/s107
/s50/s52/s107
/s51/s50/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s52/s56/s32/s37
/s53/s50/s32/s37
/s57/s49/s32/s37
/s57/s32/s37
/s50/s57/s32/s37
/s55/s49/s32/s37
/s55/s55/s32/s37
/s50/s51/s32/s37
/s55/s56/s32/s37
/s50/s50/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s56/s107
/s49/s54/s107
/s50/s52/s107
/s51/s50/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s52/s49/s32/s37
/s53/s57/s32/s37
/s57/s48/s32/s37
/s49/s48/s32/s37
/s51/s49/s32/s37
/s54/s57/s32/s37
/s55/s48/s32/s37
/s51/s48/s32/s37
/s52/s50/s32/s37
/s53/s56/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 7: Regret of varying the demand-supply ratio λ when ω = 10% (Email-Eu-Core,
|A| = 100, pc : T rivalency)
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s49/s50/s107
/s49/s54/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s51/s56/s32/s37
/s54/s50/s32/s37
/s57/s55/s32/s37
/s51/s32/s37
/s50/s56/s32/s37
/s55/s50/s32/s37
/s53/s56/s32/s37
/s52/s50/s32/s37
/s51/s50/s32/s37
/s54/s56/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s49/s50/s107
/s49/s54/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s50/s48/s32/s37
/s56/s48/s32/s37
/s56/s50/s32/s37
/s49/s56/s32/s37
/s57/s32/s37
/s57/s49/s32/s37
/s50/s53/s32/s37
/s55/s53/s32/s37
/s49/s54/s32/s37
/s56/s52/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s56/s107
/s49/s54/s107
/s50/s52/s107
/s51/s50/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s56/s32/s37
/s57/s50/s32/s37
/s53/s52/s32/s37
/s52/s54/s32/s37
/s51/s32/s37
/s57/s55/s32/s37
/s49/s49/s32/s37
/s56/s57/s32/s37
/s54/s32/s37
/s57/s52/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s56/s107
/s49/s54/s107
/s50/s52/s107
/s51/s50/s107
/s52/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s51/s32/s37
/s57/s55/s32/s37
/s50/s53/s32/s37
/s55/s53/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s51/s32/s37
/s57/s55/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s107
/s50/s48/s107
/s51/s48/s107
/s52/s48/s107
/s53/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s32/s37
/s57/s57/s32/s37
/s49/s49/s32/s37
/s56/s57/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 8: Regret of varying the demand-supply ratio λ when ω = 30% (Email-Eu-Core,
|A| = 50, pc : T rivalency)
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s50/s50/s32/s37
/s55/s56/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s57/s32/s37
/s57/s49/s32/s37
/s49/s54/s32/s37
/s56/s52/s32/s37
/s49/s53/s32/s37
/s56/s53/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s49/s50/s107
/s49/s54/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s51/s32/s37
/s57/s55/s32/s37
/s51/s52/s32/s37
/s54/s54/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s51/s32/s37
/s57/s55/s32/s37
/s51/s32/s37
/s57/s55/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s54/s107
/s49/s50/s107
/s49/s56/s107
/s50/s52/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s51/s32/s37
/s57/s55/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s56/s107
/s49/s54/s107
/s50/s52/s107
/s51/s50/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s56/s107
/s49/s54/s107
/s50/s52/s107
/s51/s50/s107
/s52/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 9: Regret of varying the demand-supply ratio λ when ω = 50% (Email-Eu-Core,
|A| = 20, pc : T rivalency)
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s51/s32/s37
/s56/s55/s32/s37
/s53/s53/s32/s37
/s52/s53/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s53/s32/s37
/s57/s53/s32/s37
/s50/s32/s37
/s57/s56/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s49/s50/s107
/s49/s54/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s54/s107
/s49/s50/s107
/s49/s56/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s54/s107
/s49/s50/s107
/s49/s56/s107
/s50/s52/s107
/s51/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s56/s107
/s49/s54/s107
/s50/s52/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 10: Regret of varying the demand-supply ratio λ when ω = 70% (Email-Eu-Core,
|A| = 10, pc : T rivalency)
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s107
/s52/s107
/s54/s107
/s56/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s107
/s52/s107
/s54/s107
/s56/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s49/s50/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s49/s50/s107
/s49/s54/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s54/s107
/s49/s50/s107
/s49/s56/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 11: Regret of varying the demand-supply ratio λ when ω = 90% (Email-Eu-Core,
|A| = 5, pc : T rivalency)
26

Excessive Regret
 Unsatisfied Regret
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s48/s107
/s52/s48/s48/s107
/s54/s48/s48/s107
/s56/s48/s48/s107
/s49/s77
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s48/s107
/s52/s48/s48/s107
/s54/s48/s48/s107
/s56/s48/s48/s107
/s49/s77
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s48/s107
/s52/s48/s48/s107
/s54/s48/s48/s107
/s56/s48/s48/s107
/s49/s77
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s48/s107
/s52/s48/s48/s107
/s54/s48/s48/s107
/s56/s48/s48/s107
/s49/s77
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s48/s107
/s52/s48/s48/s107
/s54/s48/s48/s107
/s56/s48/s48/s107
/s49/s77
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 12 : Regret of varying the demand-supply ratio λ when ω = 10% (Facebook,
|A| = 100, pc : U nif orm(0.1))
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s48/s107
/s50/s48/s48/s107
/s51/s48/s48/s107
/s52/s48/s48/s107
/s53/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s48/s107
/s50/s48/s48/s107
/s51/s48/s48/s107
/s52/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s48/s107
/s50/s48/s48/s107
/s51/s48/s48/s107
/s52/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s48/s107
/s50/s48/s48/s107
/s51/s48/s48/s107
/s52/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s48/s107
/s50/s48/s48/s107
/s51/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 13 : Regret of varying the demand-supply ratio λ when ω = 30% (Facebook,
|A| = 50, pc : U nif orm(0.1))
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s53/s48/s107
/s49/s48/s48/s107
/s49/s53/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s53/s48/s107
/s49/s48/s48/s107
/s49/s53/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s53/s48/s107
/s49/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37 /s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s49/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s53/s51/s32/s37
/s52/s55/s32/s37
/s52/s54/s32/s37
/s53/s52/s32/s37
/s52/s32/s37
/s57/s54/s32/s37
/s54/s32/s37
/s57/s52/s32/s37
/s51/s32/s37
/s57/s55/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 14 : Regret of varying the demand-supply ratio λ when ω = 50% (Facebook,
|A| = 20, pc : U nif orm(0.1))
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s52/s48/s32/s37
/s54/s48/s32/s37
/s51/s51/s32/s37
/s54/s55/s32/s37
/s50/s32/s37
/s57/s56/s32/s37
/s51/s32/s37
/s57/s55/s32/s37
/s51/s32/s37
/s57/s55/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s52/s54/s32/s37
/s53/s52/s32/s37
/s52/s52/s32/s37
/s53/s54/s32/s37
/s51/s32/s37
/s57/s55/s32/s37
/s51/s32/s37
/s57/s55/s32/s37
/s50/s32/s37
/s57/s56/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s51/s32/s37
/s56/s55/s32/s37
/s49/s50/s32/s37
/s56/s56/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 15 : Regret of varying the demand-supply ratio λ when ω = 70% (Facebook,
|A| = 10, pc : U nif orm(0.1))
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s107
/s50/s48/s107
/s51/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s107
/s50/s48/s107
/s51/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s107
/s50/s48/s107
/s51/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s52/s49/s32/s37
/s53/s57/s32/s37
/s51/s55/s32/s37
/s54/s51/s32/s37
/s53/s32/s37
/s57/s53/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s107
/s50/s48/s107
/s51/s48/s107
/s52/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s55/s32/s37
/s57/s51/s32/s37
/s54/s32/s37
/s57/s52/s32/s37 /s49/s32/s37
/s57/s57/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s107
/s50/s48/s107
/s51/s48/s107
/s52/s48/s107
/s53/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s55/s32/s37
/s57/s51/s32/s37
/s54/s32/s37
/s57/s52/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 16 : Regret of varying the demand-supply ratio λ when ω = 90% (Facebook,
|A| = 5, pc : U nif orm(0.1))
27

Excessive Regret
 Unsatisfied Regret
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s48/s107
/s52/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s57/s57/s32/s37
/s49/s32/s37
/s57/s54/s32/s37
/s52/s32/s37
/s57/s54/s32/s37
/s52/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s48/s107
/s52/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s57/s51/s32/s37
/s55/s32/s37
/s57/s51/s32/s37
/s55/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s48/s107
/s52/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s48/s107
/s52/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s48/s107
/s52/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 17 : Regret of varying the demand-supply ratio λ when ω = 10% (Facebook,
|A| = 100, pc : T rivalency)
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s48/s107
/s50/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s57/s57/s32/s37
/s49/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s48/s107
/s50/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s48/s107
/s50/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s56/s52/s32/s37
/s49/s54/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s48/s107
/s50/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s56/s49/s32/s37
/s49/s57/s32/s37
/s53/s48/s32/s37
/s53/s48/s32/s37
/s52/s55/s32/s37
/s53/s51/s32/s37
/s52/s55/s32/s37
/s53/s51/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s48/s107
/s50/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s50/s56/s32/s37
/s55/s50/s32/s37
/s49/s54/s32/s37
/s56/s52/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s50/s32/s37
/s57/s56/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 18 : Regret of varying the demand-supply ratio λ when ω = 30% (Facebook,
|A| = 50, pc : T rivalency)
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s54/s49/s32/s37
/s51/s57/s32/s37
/s51/s48/s32/s37
/s55/s48/s32/s37
/s50/s53/s32/s37
/s55/s53/s32/s37
/s50/s53/s32/s37
/s55/s53/s32/s37
/s50/s49/s32/s37
/s55/s57/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s50/s50/s32/s37
/s55/s56/s32/s37
/s49/s48/s32/s37
/s57/s48/s32/s37
/s50/s32/s37
/s57/s56/s32/s37
/s50/s32/s37
/s57/s56/s32/s37
/s50/s32/s37
/s57/s56/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s49/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s50/s32/s37
/s57/s56/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s49/s48/s48/s107
/s49/s50/s48/s107
/s49/s52/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s32/s37
/s57/s57/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 19 : Regret of varying the demand-supply ratio λ when ω = 50% (Facebook,
|A| = 20, pc : T rivalency)
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s55/s48/s32/s37
/s51/s48/s32/s37
/s52/s50/s32/s37
/s53/s56/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s56/s32/s37
/s56/s50/s32/s37
/s49/s48/s32/s37
/s57/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s51/s32/s37
/s57/s55/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s32/s37
/s57/s57/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s49/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 20 : Regret of varying the demand-supply ratio λ when ω = 70% (Facebook,
|A| = 10, pc : T rivalency)
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s107
/s50/s48/s107
/s51/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s51/s32/s37
/s56/s55/s32/s37
/s57/s32/s37
/s57/s49/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s107
/s50/s48/s107
/s51/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s57/s32/s37
/s56/s49/s32/s37
/s52/s32/s37
/s57/s54/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s107
/s50/s48/s107
/s51/s48/s107
/s52/s48/s107
/s53/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s107
/s50/s48/s107
/s51/s48/s107
/s52/s48/s107
/s53/s48/s107
/s54/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s71/s114/s101/s101/s100/s121 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s107
/s50/s48/s107
/s51/s48/s107
/s52/s48/s107
/s53/s48/s107
/s54/s48/s107
/s55/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 21 : Regret of varying the demand-supply ratio λ when ω = 90% (Facebook,
|A| = 5, pc : T rivalency)
28

Excessive Regret
 Unsatisfied Regret
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s48/s107
/s50/s48/s48/s107
/s51/s48/s48/s107
/s52/s48/s48/s107
/s53/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s57/s57/s32/s37
/s49/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s53/s53/s32/s37
/s52/s53/s32/s37
/s56/s52/s32/s37
/s49/s54/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s48/s107
/s50/s48/s48/s107
/s51/s48/s48/s107
/s52/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s57/s57/s32/s37
/s49/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s55/s48/s32/s37
/s51/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s48/s107
/s50/s48/s48/s107
/s51/s48/s48/s107
/s52/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s54/s49/s32/s37
/s51/s57/s32/s37
/s56/s55/s32/s37
/s49/s51/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s48/s107
/s50/s48/s48/s107
/s51/s48/s48/s107
/s52/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s57/s56/s32/s37
/s50/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s57/s49/s32/s37
/s57/s32/s37
/s57/s49/s32/s37
/s57/s32/s37
/s56/s48/s32/s37
/s50/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s48/s107
/s50/s48/s48/s107
/s51/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s57/s57/s32/s37
/s49/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s56/s51/s32/s37
/s49/s55/s32/s37
/s56/s51/s32/s37
/s49/s55/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 22 : Regret of varying the demand-supply ratio λ when ω = 10% (Wikivote,
|A| = 100, pc : U nif orm(0.1))
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s48/s107
/s50/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s55/s55/s32/s37
/s50/s51/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s55/s55/s32/s37
/s50/s51/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s53/s48/s107
/s49/s48/s48/s107
/s49/s53/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s54/s56/s32/s37
/s51/s50/s32/s37
/s54/s57/s32/s37
/s51/s49/s32/s37
/s57/s32/s37
/s57/s49/s32/s37
/s57/s32/s37
/s57/s49/s32/s37
/s56/s32/s37
/s57/s50/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s53/s48/s107
/s49/s48/s48/s107
/s49/s53/s48/s107
/s50/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s50/s32/s37
/s56/s56/s32/s37
/s49/s52/s32/s37
/s56/s54/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s53/s48/s107
/s49/s48/s48/s107
/s49/s53/s48/s107
/s50/s48/s48/s107
/s50/s53/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s52/s32/s37
/s57/s54/s32/s37
/s52/s32/s37
/s57/s54/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s53/s48/s107
/s49/s48/s48/s107
/s49/s53/s48/s107
/s50/s48/s48/s107
/s50/s53/s48/s107
/s51/s48/s48/s107
/s51/s53/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 23 : Regret of varying the demand-supply ratio λ when ω = 30% (Wikivote,
|A| = 50, pc : U nif orm(0.1))
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s108/s103/s111/s51
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s53/s52/s32/s37
/s52/s54/s32/s37
/s53/s54/s32/s37
/s52/s52/s32/s37
/s53/s32/s37
/s57/s53/s32/s37
/s52/s32/s37
/s57/s54/s32/s37
/s51/s32/s37
/s57/s55/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s54/s32/s37
/s57/s52/s32/s37
/s54/s32/s37
/s57/s52/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s53/s48/s107
/s49/s48/s48/s107
/s49/s53/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s53/s48/s107
/s49/s48/s48/s107
/s49/s53/s48/s107
/s50/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s53/s48/s107
/s49/s48/s48/s107
/s49/s53/s48/s107
/s50/s48/s48/s107
/s50/s53/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 24 : Regret of varying the demand-supply ratio λ when ω = 50% (Wikivote,
|A| = 20, pc : U nif orm(0.1))
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s51/s32/s37
/s57/s55/s32/s37
/s51/s32/s37
/s57/s55/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s48/s107
/s56/s48/s107
/s49/s50/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s54/s48/s107
/s49/s50/s48/s107
/s49/s56/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s53/s48/s107
/s49/s48/s48/s107
/s49/s53/s48/s107
/s50/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 25 : Regret of varying the demand-supply ratio λ when ω = 70% (Wikivote,
|A| = 10, pc : U nif orm(0.1))
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s107
/s50/s48/s107
/s51/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s107
/s50/s48/s107
/s51/s48/s107
/s52/s48/s107
/s53/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s107
/s50/s48/s107
/s51/s48/s107
/s52/s48/s107
/s53/s48/s107
/s54/s48/s107
/s55/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s48/s107
/s56/s48/s107
/s49/s50/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 26 : Regret of varying the demand-supply ratio λ when ω = 90% (Wikivote,
|A| = 5, pc : U nif orm(0.1))
29

Excessive Regret
 Unsatisfied Regret
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s49/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s49/s52/s32/s37
/s56/s54/s32/s37
/s50/s32/s37
/s57/s56/s32/s37
/s49/s53/s32/s37
/s56/s53/s32/s37
/s53/s32/s37
/s57/s53/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s49/s48/s48/s107
/s49/s50/s48/s107
/s49/s52/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s52/s32/s37
/s57/s54/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s51/s32/s37
/s57/s55/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s48/s107
/s56/s48/s107
/s49/s50/s48/s107
/s49/s54/s48/s107
/s50/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s48/s107
/s56/s48/s107
/s49/s50/s48/s107
/s49/s54/s48/s107
/s50/s48/s48/s107
/s50/s52/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s48/s107
/s56/s48/s107
/s49/s50/s48/s107
/s49/s54/s48/s107
/s50/s48/s48/s107
/s50/s52/s48/s107
/s50/s56/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 27 : Regret of varying the demand-supply ratio λ when ω = 10% (Wikivote,
|A| = 100, pc : T rivalency)
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s48/s107
/s56/s48/s107
/s49/s50/s48/s107
/s49/s54/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s48/s107
/s56/s48/s107
/s49/s50/s48/s107
/s49/s54/s48/s107
/s50/s48/s48/s107
/s50/s52/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s48/s107
/s56/s48/s107
/s49/s50/s48/s107
/s49/s54/s48/s107
/s50/s48/s48/s107
/s50/s52/s48/s107
/s50/s56/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s54/s48/s107
/s49/s50/s48/s107
/s49/s56/s48/s107
/s50/s52/s48/s107
/s51/s48/s48/s107
/s51/s54/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s54/s48/s107
/s49/s50/s48/s107
/s49/s56/s48/s107
/s50/s52/s48/s107
/s51/s48/s48/s107
/s51/s54/s48/s107
/s52/s50/s48/s107
/s52/s56/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 28 : Regret of varying the demand-supply ratio λ when ω = 30% (Wikivote,
|A| = 50, pc : T rivalency)
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s108/s103/s111/s51
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s49/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s48/s107
/s56/s48/s107
/s49/s50/s48/s107
/s49/s54/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s48/s107
/s56/s48/s107
/s49/s50/s48/s107
/s49/s54/s48/s107
/s50/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s48/s107
/s56/s48/s107
/s49/s50/s48/s107
/s49/s54/s48/s107
/s50/s48/s48/s107
/s50/s52/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s48/s107
/s56/s48/s107
/s49/s50/s48/s107
/s49/s54/s48/s107
/s50/s48/s48/s107
/s50/s52/s48/s107
/s50/s56/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 29 : Regret of varying the demand-supply ratio λ when ω = 50% (Wikivote,
|A| = 20, pc : T rivalency)
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s49/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s48/s107
/s56/s48/s107
/s49/s50/s48/s107
/s49/s54/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s48/s107
/s56/s48/s107
/s49/s50/s48/s107
/s49/s54/s48/s107
/s50/s48/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s48/s107
/s56/s48/s107
/s49/s50/s48/s107
/s49/s54/s48/s107
/s50/s48/s48/s107
/s50/s52/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 30 : Regret of varying the demand-supply ratio λ when ω = 70% (Wikivote,
|A| = 10, pc : T rivalency)
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s49/s48/s107
/s50/s48/s107
/s51/s48/s107
/s52/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s48/s107
/s56/s48/s107
/s49/s50/s48/s107
/s49/s54/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s50/s48/s107
/s52/s48/s107
/s54/s48/s107
/s56/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
(a) λ = 40% (b) λ = 60% (c) λ = 80% (d) λ = 100% (e) λ = 120%
Fig. 31 : Regret of varying the demand-supply ratio λ when ω = 90% (Wikivote,
|A| = 5, pc : T rivalency)
30

/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
(a) ω = 10%(|A| = 100) (b) ω = 30%(|A| = 50) (c) ω = 50%(|A| = 20)
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
(d) ω = 70%(|A| = 10) (e) ω = 90%(|A| = 5)
Fig. 32: Efficiency Study Uniform (0.1) Probability Setting (Email-Eu-Core)
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
(a) ω = 10%(|A| = 100) (b) ω = 30%(|A| = 50) (c) ω = 50%(|A| = 20)
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
(d) ω = 70%(|A| = 10) (e) ω = 90%(|A| = 5)
Fig. 33: Efficiency Study for Trivalency Probability Setting (Email-Eu-Core)
31

/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s49/s48
/s54
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
(a) ω = 10%(|A| = 100) (b) ω = 30%(|A| = 50) (c) ω = 50%(|A| = 20)
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s49/s48
/s54
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s49/s48
/s54
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
(d) ω = 70%(|A| = 10) (e) ω = 90%(|A| = 5)
Fig. 34: Efficiency Study Uniform (0.1) Probability Setting (Facebook)
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s49/s48
/s54
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s49/s48
/s54
/s49/s48
/s55
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s49/s48
/s54
/s49/s48
/s55
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
(a) ω = 10%(|A| = 100) (b) ω = 30%(|A| = 50) (c) ω = 50%(|A| = 20)
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s49/s48
/s54
/s49/s48
/s55
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s49/s48
/s54
/s49/s48
/s55
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
(d) ω = 70%(|A| = 10) (e) ω = 90%(|A| = 5)
Fig. 35: Efficiency Study for Trivalency Probability Setting (Facebook)
32

/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s49/s48
/s54
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s49/s48
/s54
/s49/s48
/s55
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s49/s48
/s54
/s49/s48
/s55
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
(a) ω = 10%(|A| = 100) (b) ω = 30%(|A| = 50) (c) ω = 50%(|A| = 20)
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s49/s48
/s54
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s49/s48
/s54
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
(d) ω = 70%(|A| = 10) (e) ω = 90%(|A| = 5)
Fig. 36: Efficiency Study Uniform (0.1) Probability Setting (Wikivote)
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s49/s48
/s54
/s49/s48
/s55
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s49/s48
/s54
/s49/s48
/s55
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s49/s48
/s54
/s49/s48
/s55
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
(a) ω = 10%(|A| = 100) (b) ω = 30%(|A| = 50) (c) ω = 50%(|A| = 20)
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s49/s48
/s54
/s49/s48
/s55
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
/s52/s48/s37 /s54/s48/s37 /s56/s48/s37 /s49/s48/s48/s37 /s49/s50/s48/s37
/s49/s48
/s48
/s49/s48
/s49
/s49/s48
/s50
/s49/s48
/s51
/s49/s48
/s52
/s49/s48
/s53
/s49/s48
/s54
/s49/s48
/s55
/s84/s105/s109/s101/s32/s40/s115/s101/s99/s46/s41
/s108
/s32/s82/s97/s110/s100/s111/s109 /s32/s84/s111/s112/s45/s75 /s32/s66/s71 /s32/s65/s69/s65 /s32/s65/s68/s76/s67
(d) ω = 70%(|A| = 10) (e) ω = 90%(|A| = 5)
Fig. 37: Efficiency Study for Trivalency Probability Setting (Wikivote)
33

/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s49/s50/s107
/s49/s54/s107
/s50/s48/s107
/s50/s52/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s56/s32/s37
/s57/s50/s32/s37
/s56/s32/s37
/s57/s50/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s49/s50/s107
/s49/s54/s107
/s50/s48/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s48/s32/s37
/s57/s48/s32/s37
/s49/s48/s32/s37
/s57/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s49/s50/s107
/s49/s54/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s50/s32/s37
/s56/s56/s32/s37
/s49/s51/s32/s37
/s56/s55/s32/s37
/s50/s32/s37
/s49/s48/s48/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s49/s50/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s55/s32/s37
/s56/s51/s32/s37
/s49/s54/s32/s37
/s56/s52/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s50/s32/s37
/s57/s56/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s50/s53/s32/s37
/s55/s53/s32/s37
/s50/s50/s32/s37
/s55/s56/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
(a) γ = 0 (b) γ = 0.25 (c) γ = 0.5 (d) γ = 0.75 (e) γ = 1
Fig. 38: Parameter Study for γ (|A| = 20) Uniform(0.1) Probability Setting (Email-
Eu-Core)
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s56/s107
/s49/s54/s107
/s50/s52/s107
/s51/s50/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s56/s107
/s49/s54/s107
/s50/s52/s107
/s51/s50/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s56/s107
/s49/s54/s107
/s50/s52/s107
/s51/s50/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s56/s107
/s49/s54/s107
/s50/s52/s107
/s51/s50/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s56/s107
/s49/s54/s107
/s50/s52/s107
/s51/s50/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
(a) γ = 0 (b) γ = 0.25 (c) γ = 0.5 (d) γ = 0.75 (e) γ = 1
Fig. 39: Parameter Study for γ (|A| = 20) Trivalency Probability Setting (Email-Eu-
Core)
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s49/s50/s107
/s49/s54/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s51/s32/s37
/s56/s55/s32/s37
/s49/s50/s32/s37
/s56/s56/s32/s37
/s50/s32/s37
/s57/s56/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s49/s50/s107
/s49/s54/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s50/s32/s37
/s56/s56/s32/s37
/s49/s51/s32/s37
/s56/s55/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s50/s32/s37
/s57/s56/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s49/s50/s107
/s49/s54/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s50/s32/s37
/s56/s56/s32/s37
/s49/s50/s32/s37
/s56/s56/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s49/s50/s107
/s49/s54/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s49/s51/s32/s37
/s56/s55/s32/s37
/s49/s50/s32/s37
/s56/s56/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s52/s107
/s56/s107
/s49/s50/s107
/s49/s54/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s50/s53/s32/s37
/s55/s53/s32/s37
/s50/s50/s32/s37
/s55/s56/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s49/s32/s37
/s57/s57/s32/s37
(a) δ = 0.01 (b) δ = 0.02 (c) δ = 0.03 (d) δ = 0.04 (e) δ = 0.05
Fig. 40: Parameter Study for δ (|A| = 20) Uniform(0.1) Probability Setting (Email-
Eu-Core)
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s56/s107
/s49/s54/s107
/s50/s52/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s56/s107
/s49/s54/s107
/s50/s52/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s56/s107
/s49/s54/s107
/s50/s52/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s56/s107
/s49/s54/s107
/s50/s52/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s82/s97/s110/s100/s111/s109 /s84/s111/s112/s45/s75 /s66/s71 /s65 /s69/s65 /s65 /s68/s76/s83
/s48
/s56/s107
/s49/s54/s107
/s50/s52/s107
/s82/s101/s103/s114/s101/s116
/s65 /s108/s103/s111/s114/s105/s116/s104/s109/s115
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
/s48/s32/s37
/s49/s48/s48/s32/s37
(a) δ = 0.01 (b) δ = 0.02 (c) δ = 0.03 (d) δ = 0.04 (e) δ = 0.05
Fig. 41: Parameter Study for δ (|A| = 20) Trivalency Probability Setting (Email-Eu-
Core)
34

T able 5: Congress-Twitter dataset Regret Values for Uniform (0.1) probability setting
Parameters T otal Regret[Uniform(0.1)]
λ (%) ω (%) |A| Random T op-K BG AEA ADLC
40 10 100 13376.81 13291.20 12585.92 12233.51 12385.94
60 10 100 25391.24 29737.52 19828.20 20616.84 20321.09
80 10 100 40645.32 49987.67 29950.00 29574.21 30191.59
100 10 100 48480.66 62314.09 34377.04 32877.58 32745.78
120 10 100 48100.90 62781.68 32706.01 33093.89 32975.50
40 30 50 29930.27 35879.33 14809.39 15269.76 15060.02
60 30 50 30837.08 36511.97 11417.71 11343.79 11059.94
80 30 50 31338.21 34550.39 7838.85 7446.80 8054.58
100 30 50 31674.46 33847.93 6234.60 5960.76 5731.31
120 30 50 26419.24 28204.20 2351.29 2242.49 2311.27
40 50 20 13943.05 15392.76 3104.46 2228.51 2130.25
60 50 20 12498.76 13435.49 1231.86 871.70 1299.96
80 50 20 9665.56 9815.74 612.18 544.19 183.18
100 50 20 5763.34 5944.84 292.41 391.36 330.03
120 50 20 6850.75 7004.29 2485.93 2550.49 2366.90
40 70 10 7420.95 7627.62 615.99 349.83 424.97
60 70 10 4478.94 4479.50 264.57 388.92 102.01
80 70 10 3349.17 3428.69 109.65 544.19 86.99
100 70 10 2486.22 2469.15 1143.57 1179.31 1209.06
120 70 10 4553.62 4552.75 3451.22 3453.11 3464.08
40 90 5 103.92 2270.01 103.92 205.75 140.66
60 90 5 1459.10 1437.23 76.28 95.48 80.89
80 90 5 1249.21 1271.37 113.75 30.89 18.53
100 90 5 4517.31 4519.45 4202.07 4215.36 4158.72
120 90 5 4280.22 4297.56 4256.82 4258.16 4252.55
T able 6: Congress-Twitter dataset Regret Values for Trivalency probability setting
Parameters T otal Regret[T rivalency]
λ (%) ω (%) |A| Random T op-K BG AEA ADLC
40 10 100 5408.10 5392.73 5341.50 5212.88 5333.35
60 10 100 7625.98 7505.07 7529.86 7348.92 7533.65
80 10 100 10822.32 10296.99 10307.54 10187.87 10360.18
100 10 100 13672.16 13205.79 13174.69 13180.11 13144.07
120 10 100 14720.62 13965.16 14134.05 14074.29 14085.10
40 30 50 7627.89 7202.01 7366.88 7272.52 7244.92
60 30 50 11601.32 11078.86 11139.29 11223.31 11166.68
80 30 50 16490.07 16026.52 15949.91 16035.33 15907.54
100 30 50 19289.97 18549.26 18655.92 18655.25 18786.29
120 30 50 24352.64 23760.72 23720.73 23646.37 23630.90
35

Parameters T otal Regret[T rivalency]
λ (%) ω (%) |A| Random T op-K BG AEA ADLC
40 50 20 5370.53 5108.19 5142.21 5111.93 5205.76
60 50 20 7517.58 7244.32 7336.24 7354.96 7388.99
80 50 20 11010.57 10853.53 10830.52 10751.62 10696.79
100 50 20 13254.92 13146.44 13100.62 13170.93 13053.65
120 50 20 15965.48 15828.96 15746.81 15611.16 15652.43
40 70 10 3601.80 3385.32 3504.88 3518.55 3569.36
60 70 10 6456.80 6325.75 6274.40 6361.20 6385.23
80 70 10 6772.42 6674.18 6675.38 6657.01 6643.59
100 70 10 8989.62 8774.30 8790.65 8757.08 8729.84
120 70 10 9706.76 9535.63 9524.20 9490.06 9555.73
40 90 5 2106.98 1998.88 2063.29 2027.96 2052.88
60 90 5 3427.91 3362.02 3427.96 3396.55 3398.36
80 90 5 3075.56 3022.17 3010.51 3013.27 2994.31
100 90 5 7639.66 7565.15 7497.26 7565.56 7507.93
120 90 5 6199.22 6132.95 6061.32 6127.57 6086.78
T able 7: Congress-Twitter dataset Execution Time for Uniform (0.1) probability
setting
Parameters Execution Time (in seconds) [Uniform(0.1)]
λ (%) ω (%) |A| Random T op-K BG AEA ADLC
40 10 100 56.700 58.294 21.560 617.561 42.581
60 10 100 59.154 57.799 27.865 410.538 50.779
80 10 100 59.630 59.489 36.364 217.782 65.914
100 10 100 60.598 55.892 41.825 120.250 79.034
120 10 100 59.907 60.782 43.828 96.583 73.505
40 30 50 28.110 28.026 26.351 26.746 48.043
60 30 50 29.416 28.035 36.856 37.348 67.160
80 30 50 30.369 28.308 46.156 46.348 73.318
100 30 50 30.636 30.306 52.008 49.424 81.446
120 30 50 28.198 28.068 54.379 53.014 84.192
40 50 20 12.615 11.962 18.744 18.006 32.183
60 50 20 11.947 11.520 21.731 21.294 37.474
80 50 20 11.387 11.236 23.005 23.528 37.381
100 50 20 11.577 11.266 24.025 24.708 45.604
120 50 20 12.357 11.694 40.065 61.440 66.244
40 70 10 5.920 5.541 11.663 11.136 20.477
60 70 10 6.059 5.343 12.429 13.122 21.577
80 70 10 6.124 5.913 12.646 23.528 21.289
100 70 10 5.974 5.929 21.483 22.676 36.107
120 70 10 5.945 5.798 33.944 61.832 61.117
36

Parameters Execution Time (in seconds) [Uniform(0.1)]
λ(%) ω(%) |A| Random T op-K BG AEA ADLC
40 90 5 6.076 2.894 6.076 6.377 11.728
60 90 5 3.307 2.853 6.843 7.212 11.962
80 90 5 3.012 2.800 6.304 8.973 11.807
100 90 5 3.082 2.634 28.086 26.290 61.309
120 90 5 2.985 2.862 35.007 83.346 71.825
T able 8: Congress-Twitter dataset Execution Time for Trivalency probability setting
Parameters Execution Time (in seconds) [T rivalency]
λ(%) ω(%) |A| Random T op-K BG AEA ADLC
40 10 100 53.777 54.330 20.077 1138.233 42.125
60 10 100 55.575 53.374 24.601 1589.903 43.460
80 10 100 56.355 54.696 28.813 2028.303 56.383
100 10 100 56.469 52.144 36.997 2276.420 75.952
120 10 100 55.759 55.878 38.417 2375.799 77.629
40 30 50 26.555 26.205 23.594 737.068 46.575
60 30 50 27.850 26.171 37.201 1115.152 74.822
80 30 50 28.025 26.693 53.038 1558.651 100.934
100 30 50 27.678 28.107 60.515 1820.305 126.381
120 30 50 26.191 26.370 70.493 2206.092 144.770
40 50 20 11.496 11.051 20.936 236.706 40.878
60 50 20 10.717 11.020 27.708 334.341 57.799
80 50 20 10.750 10.504 38.430 482.269 79.048
100 50 20 10.784 10.693 45.404 570.981 97.108
120 50 20 11.047 11.111 53.045 637.845 110.611
40 70 10 5.418 5.334 15.222 90.399 31.693
60 70 10 5.601 5.076 27.653 152.869 54.503
80 70 10 5.453 5.482 26.960 159.808 54.537
100 70 10 5.253 5.587 33.953 197.508 68.735
120 70 10 5.408 5.305 41.818 215.469 68.627
40 90 5 2.911 3.116 8.624 23.895 20.076
60 90 5 2.992 2.877 16.033 36.620 30.203
80 90 5 2.995 4.058 12.650 37.197 28.992
100 90 5 3.002 3.007 31.186 76.602 67.955
120 90 5 3.147 2.914 25.742 66.259 48.551
5.5.2 Efficiency Study
This section analyzes the execution time performance of various algorithms, “Top-K”,
“Random”, “BG”, “AEA”, and “ADLS”— across multiple datasets under both Uni-
form and Trivalency influence probability settings. The evaluation considers the effects
of parameters ω (individual influence demand) and λ (global influence demand) on
37

computational efficiency. The execution time under Uniform (0.1) probability setting is
observed as follows. In Figures 32, for the Email-Eu-Core dataset, as ω increases, exe-
cution times decrease for all methods. The “Top-K” algorithm is the fastest across all
settings, followed closely by “Random”. The algorithms “BG”, “AEA”, and “ADLS”
exhibit significantly higher execution times, particularly at lowω values. Among these,
“ADLS” is generally the slowest algorithm, with execution times up to 292% longer
than “Random” at ω = 10%. The “BG” algorithm is also slower than “Random”,
with execution times ranging from 50% to 150% higher. Both “AEA” and “ADLS”
show extreme delays, particularly under high λ and low ω conditions. For instance, at
ω = 50% and λ = 100%, the execution time of “AEA” reaches 1002 seconds, exceeding
that of “Random” by more than 1000%. Similarly, “ADLS” is over 500% slower than
“Random” in several cases. In Figures 34, for the Facebook dataset, across all meth-
ods, execution times decrease as ω increases, indicating that as individual influence
demand grows, computations become less intensive. The “Top- K” algorithm consis-
tently achieves the lowest execution times, followed closely by “Random”. Conversely,
“ADLS” consistently exhibits the highest execution times, particularly at low ω val-
ues, where it is up to 292% slower than “Random”. The “BG” algorithm is generally
50% to 150% slower than “Random”. Both “AEA” and “ADLS” experience extreme
delays, especially when λ is high and ω is low. The “BG”, “AEA”, and “ADLS” algo-
rithms incur significantly higher computation times, with “ADLS” reaching 17753
seconds at λ = 120%, which is over 57 times slower than “Random” (310 .67 seconds).
For the Wikivote dataset, in Figure 36, the “Top- K” and “Random” algorithms are
the fastest across all settings. In contrast, “BG”, “AEA”, and “ADLS” exhibit signif-
icant increases in execution time, particularly at low ω values. Among all methods,
“AEA” is the slowest overall, especially when λ is high. Execution times decrease as
ω increases, indicating that higher ω leads to more efficient computations. At low val-
ues of ω = 10% and ω = 30%, execution times remain significantly high across all
algorithms. For instance, at ω = 10% and λ = 120%, the execution times are “BG”:
∼ 11288 seconds, “AEA”: ∼ 11288 seconds, and “ADLS”: ∼ 14600 seconds (extremely
slow). At ω = 30% and λ = 120%, “AEA” reaches an enormous execution time of
712164 seconds. Conversely, at high values of ω = 70% and ω = 90%, execution times
drop significantly. At ω = 90% and λ = 120%, the execution times are “Random”:
∼ 21 seconds, “Top- K”: ∼ 18 seconds, “BG”: ∼ 9993 seconds, “AEA”: ∼ 21387
seconds, and “ADLS”: ∼ 17351 seconds. These results suggest that higher values of
ω significantly reduce computational overhead. From Table 7, for Congress-Twitter
dataset we analyze that “ADLS” performs better than “AEA” but worse than “BG”,
“Top-K”, and “Random”. The “Top- K” algorithm is slightly faster than “Random”
at high ω values.
We also observe the performance of all algorithms for all datasets under the Triva-
lency probability setting. From Figures 33, our observations for the Email-Eu-Core
dataset are as follows. The “Random” and “Top- K” algorithms perform best. In
contrast, “BG”, “AEA”, and “ADLS” scale poorly as λ increases. “AEA” exhibits
extremely high execution times for large λ values, making it highly inefficient. From
Figures 35, for the Facebook dataset, we observe that the algorithms “BG”, “AEA”,
and “ADLS” experience significant increases in execution time for high λ. Among
38

them, “AEA” has the worst performance, particularly at low ω. Execution times are
higher across all algorithms compared to other datasets in the Wikivote dataset, as
shown in Figure 37. “AEA” incurs extreme computation times, rendering it highly inef-
ficient. “ADLS” also suffers from large execution times, although it performs slightly
better than “AEA”. From Table 8, for the Congress-Twitter dataset, our observations
indicate that “ADLS” is slower than “BG”, “Random”, and “Top-K”, but much faster
than “AEA”. “Random” and “Top- K” have similar performance, with “Random”
being slightly faster at high ω.
In general, “Top- K” and “Random” are the fastest methods, while “AEA” and
“ADLS” exhibit significantly higher execution times, especially under lowω and high λ
conditions. The results highlight the computational challenges faced by more sophisti-
cated algorithms like “AEA” and “ADLS”, particularly in large-scale or high-demand
scenarios.
5.5.3 Other Parameter Study
The additional parameters we have used in our experiments are γ and δ. First we
discuss the effect of γ in our experiment. We have taken five different values of this
parameter. From the Figures 38 and 39, we see that as γ increases, the total regret
for all algorithms decreases. In the Figure 38 (a), when γ = 0, that means there is
no penalty on the provided influence. In this situation the regret is highest as the
full budget contribute to the regret. On the other hand, when γ = 1, the total regret
is lowest, which means that the influence provider receives a payment proportional
to the ratio of the influence it provided. The other parameter we have considered
is δ, for its five different values. In the Figures 40 and 41, the effect of increasing
the value of δ is nearly same. There is no significant increase or decrease with these
values of δ. Another parameter which is already discussed is the influence probability
setting. We have used Uniform (0 .1) and Trivalency influence probability settings for
our experiments on all datasets. Our approach “ADLS” dominates across all cases in
both probability settings giving lower regrets. The only difference is between the two
probability settings is that under Uniform, the regret values are generally higher than
that of Trivalency.
6 Concluding Remarks and Future Research
Directions
In this paper we have studied the Regret Minimization in Social Media Advertise-
ment Problem and posed this problem as a discrete optimization problem. We have
shown that this problem is computationally hard and also hard to approximate within
a constant factor. We have proposed three efficient heuristic solution approaches with
a detailed complexity analysis. The proposed methodologies have been elaborated on
with an example. A number of experiments have been conducted to show the effec-
tiveness and efficiency of all the algorithms. From the reported results, it has been
observed that the proposed solution approaches lead to much less regret compared to
the baseline methods. “ADLS” consistently performs best in minimizing regret, mak-
ing it the optimal choice for advertiser allocation under different probability settings.
39

“BG” and “AEA” are competitive but fail in high demand scenarios where “ADLS”
excels. “Random” and “Top-K” methods are ineffective, leading to significantly higher
total regret. Now, this study can be extended in the following directions. More effi-
cient solution methodologies are of thrust. Also, a new regret model may be proposed,
which will capture the loss in a much better way. The scalable algorithms for regret
minimization in large-scale online social networks are to be designed.
Acknowledgement
The authors would like to acknowledge Indian Institute of Technology (IIT) Jammu,
India, with grant number SG100047, for providing the funds required for the project.
References
[1] Wasserman, S.: Social network analysis: Methods and applications. Cambridge
University Press google schola 2, 131–134 (1994)
[2] Chunaev, P.: Community detection in node-attributed social networks: a survey.
Computer Science Review 37, 100286 (2020)
[3] Papadopoulos, S., Kompatsiaris, Y., Vakali, A., Spyridonos, P.: Community detec-
tion in social media: Performance and application considerations. Data mining
and knowledge discovery 24, 515–554 (2012)
[4] Javed, M.A., Younis, M.S., Latif, S., Qadir, J., Baig, A.: Community detec-
tion in networks: A multidisciplinary review. Journal of Network and Computer
Applications 108, 87–111 (2018)
[5] Kimura, M., Saito, K.: Tractable models for information diffusion in social net-
works. In: European Conference on Principles of Data Mining and Knowledge
Discovery, pp. 259–271 (2006). Springer
[6] Bakshy, E., Rosenn, I., Marlow, C., Adamic, L.: The role of social networks in
information diffusion. In: Proceedings of the 21st International Conference on
World Wide Web, pp. 519–528 (2012)
[7] Li, Y., Fan, J., Wang, Y., Tan, K.-L.: Influence maximization on social graphs:
A survey. IEEE Transactions on Knowledge and Data Engineering 30(10), 1852–
1872 (2018)
[8] Azaouzi, M., Mnasri, W., Romdhane, L.B.: New trends in influence maximization
models. Computer Science Review 40, 100393 (2021)
[9] Banerjee, S., Jenamani, M., Pratihar, D.K.: A survey on influence maximization
in a social network. Knowledge and Information Systems 62, 3417–3455 (2020)
40

[10] Das, A., Gollapudi, S., Munagala, K.: Modeling opinion dynamics in social net-
works. In: Proceedings of the 7th ACM International Conference on Web Search
and Data Mining, pp. 403–412 (2014)
[11] De, A., Valera, I., Ganguly, N., Bhattacharya, S., Gomez Rodriguez, M.: Learn-
ing and forecasting opinion dynamics in social networks. Advances in neural
information processing systems 29 (2016)
[12] Richardson, M., Domingos, P.: Mining knowledge-sharing sites for viral market-
ing. In: Proceedings of the Eighth ACM SIGKDD International Conference on
Knowledge Discovery and Data Mining, pp. 61–70 (2002)
[13] Domingos, P., Richardson, M.: Mining the network value of customers. In: Pro-
ceedings of the Seventh ACM SIGKDD International Conference on Knowledge
Discovery and Data Mining, pp. 57–66 (2001)
[14] Liang, Z., He, Q., Du, H., Xu, W.: Targeted influence maximization in competitive
social networks. Information Sciences 619, 390–405 (2023)
[15] Chen, W., Lin, T., Tan, Z., Zhao, M., Zhou, X.: Robust influence maximiza-
tion. In: Proceedings of the 22nd ACM SIGKDD International Conference on
Knowledge Discovery and Data Mining, pp. 795–804 (2016)
[16] Chen, W., Collins, A., Cummings, R., Ke, T., Liu, Z., Rincon, D., Sun, X.,
Wang, Y., Wei, W., Yuan, Y.: Influence maximization in social networks when
negative opinions may emerge and propagate. In: Proceedings of the 2011 Siam
International Conference on Data Mining, pp. 379–390 (2011). SIAM
[17] Peng, B.: Dynamic influence maximization. Advances in Neural Information
Processing Systems 34, 10718–10731 (2021)
[18] Cautis, B., Maniu, S., Tziortziotis, N.: Adaptive influence maximization. In: Pro-
ceedings of the 25th ACM SIGKDD International Conference on Knowledge
Discovery & Data Mining, pp. 3185–3186 (2019)
[19] Zhang, Y., Li, Y., Bao, Z., Zheng, B., Jagadish, H.: Minimizing the regret of
an influence provider. In: Proceedings of the 2021 International Conference on
Management of Data, pp. 2115–2127 (2021)
[20] Ali, D., Bhagat, A.K., Banerjee, S., Prasad, Y.: Efficient algorithms for regret
minimization in billboard advertisement (student abstract). In: Proceedings of
the AAAI Conference on Artificial Intelligence, vol. 37, pp. 16148–16149 (2023)
[21] Ali, D., Banerjee, S., Prasad, Y.: Toward regret-free slot allocation in billboard
advertisement. International Journal of Data Science and Analytics, 1–25 (2024)
[22] Kempe, D., Kleinberg, J., Tardos, E.: Maximizing the spread of influence through
41

a social network. In: Proceedings of the Ninth ACM SIGKDD International
Conference on Knowledge Discovery and Data Mining. KDD ’03, pp. 137–
146. Association for Computing Machinery, New York, NY, USA (2003). https:
//doi.org/10.1145/956750.956769 . https://doi.org/10.1145/956750.956769
[23] Kempe, D., Kleinberg, J., Tardos, ´E.: Influential nodes in a diffusion model for
social networks. In: Caires, L., Italiano, G.F., Monteiro, L., Palamidessi, C., Yung,
M. (eds.) Automata, Languages and Programming, pp. 1127–1138. Springer,
Berlin, Heidelberg (2005)
[24] Kempe, D., Kleinberg, J.M., Tardos, ´E.: Maximizing the spread of influence
through a social network. Theory Comput. 11, 105–147 (2015) https://doi.org/
10.4086/TOC.2015.V011A004
[25] Leskovec, J., Krause, A., Guestrin, C., Faloutsos, C., VanBriesen, J., Glance,
N.: Cost-effective outbreak detection in networks. In: Proceedings of the 13th
ACM SIGKDD International Conference on Knowledge Discovery and Data Min-
ing. KDD ’07, pp. 420–429. Association for Computing Machinery, New York,
NY, USA (2007). https://doi.org/10.1145/1281192.1281239 . https://doi.org/10.
1145/1281192.1281239
[26] Borgs, C., Brautbar, M., Chayes, J., Lucier, B.: Maximizing Social Influence in
Nearly Optimal Time, pp. 946–957. https://doi.org/10.1137/1.9781611973402.70
. https://epubs.siam.org/doi/abs/10.1137/1.9781611973402.70
[27] Tang, Y., Xiao, X., Shi, Y.: Influence maximization: near-optimal time complexity
meets practical efficiency. In: Proceedings of the 2014 ACM SIGMOD Interna-
tional Conference on Management of Data. SIGMOD ’14, pp. 75–86. Association
for Computing Machinery, New York, NY, USA (2014). https://doi.org/10.1145/
2588555.2593670 . https://doi.org/10.1145/2588555.2593670
[28] Tang, Y., Shi, Y., Xiao, X.: Influence maximization in near-linear time: A mar-
tingale approach. In: Proceedings of the 2015 ACM SIGMOD International
Conference on Management of Data. SIGMOD ’15, pp. 1539–1554. Association
for Computing Machinery, New York, NY, USA (2015). https://doi.org/10.1145/
2723372.2723734 . https://doi.org/10.1145/2723372.2723734
[29] Jung, K., Heo, W., Chen, W.: Irie: Scalable and robust influence maximization
in social networks. In: 2012 IEEE 12th International Conference on Data Mining,
pp. 918–923 (2012). IEEE
[30] Cheng, S., Shen, H., Huang, J., Zhang, G., Cheng, X.: Staticgreedy: solving the
scalability-accuracy dilemma in influence maximization. In: Proceedings of the
22nd ACM International Conference on Information & Knowledge Management,
pp. 509–518 (2013)
42

[31] Cheng, S., Shen, H., Huang, J., Chen, W., Cheng, X.: Imrank: influence maximiza-
tion via finding self-consistent ranking. In: Proceedings of the 37th International
ACM SIGIR Conference on Research & Development in Information Retrieval,
pp. 475–484 (2014)
[32] Chen, Y.-C., Zhu, W.-Y., Peng, W.-C., Lee, W.-C., Lee, S.-Y.: Cim: Community-
based influence maximization in social networks. ACM Transactions on Intelligent
Systems and Technology (TIST) 5(2), 1–31 (2014)
[33] Bozorgi, A., Haghighi, H., Zahedi, M.S., Rezvani, M.: Incim: A community-based
algorithm for influence maximization problem under the linear threshold model.
Information Processing & Management 52(6), 1188–1199 (2016)
[34] Shang, J., Zhou, S., Li, X., Liu, L., Wu, H.: Cofim: A community-based framework
for influence maximization on large-scale networks. Knowledge-Based Systems
117, 88–100 (2017)
[35] Bozorgi, A., Samet, S., Kwisthout, J., Wareham, T.: Community-based influ-
ence maximization in social networks under a competitive linear threshold model.
Knowledge-Based Systems 134, 149–158 (2017)
[36] Gong, M., Yan, J., Shen, B., Ma, L., Cai, Q.: Influence maximization in social
networks based on discrete particle swarm optimization. Information Sciences
367, 600–614 (2016)
[37] S ¸˙IMS ¸EK, A., Resul, K.: Using swarm intelligence algorithms to detect influential
individuals for influence maximization in social networks. Expert Systems with
Applications 114, 224–236 (2018)
[38] Bucur, D., Iacca, G.: Influence maximization in social networks with genetic
algorithms. In: Applications of Evolutionary Computation: 19th European
Conference, EvoApplications 2016, Porto, Portugal, March 30–April 1, 2016,
Proceedings, Part I 19, pp. 379–392 (2016). Springer
[39] Banerjee, S., Jenamani, M., Pratihar, D.K.: Combim: A community-based solu-
tion approach for the budgeted influence maximization problem. Expert Systems
with Applications 125, 1–13 (2019)
[40] Han, S., Zhuang, F., He, Q., Shi, Z.: Balanced seed selection for budgeted influence
maximization in social networks. In: Advances in Knowledge Discovery and Data
Mining: 18th Pacific-Asia Conference, PAKDD 2014, Tainan, Taiwan, May 13-16,
2014. Proceedings, Part I 18, pp. 65–77 (2014). Springer
[41] Raghavan, S., Zhang, R.: A branch-and-cut approach for the weighted target set
selection problem on social networks. INFORMS Journal on Optimization 1(4),
304–322 (2019)
43

[42] Cicalese, F., Cordasco, G., Gargano, L., Milaniˇ c, M., Vaccaro, U.: Latency-
bounded target set selection in social networks. Theoretical Computer Science
535, 1–15 (2014)
[43] Chu, H., Lin, B.: Fpt approximation using treewidth: Capacitated vertex cover,
target set selection and vector dominating set. arXiv preprint arXiv:2312.11944
(2023)
[44] Hartmann, T.A.: Target set selection parameterized by clique-width and maxi-
mum threshold. In: SOFSEM 2018: Theory and Practice of Computer Science:
44th International Conference on Current Trends in Theory and Practice of Com-
puter Science, Krems, Austria, January 29-February 2, 2018, Proceedings 44, pp.
137–149 (2018). Springer
[45] Ali, D., Banerjee, S., Prasad, Y.: Regret minimization in billboard advertise-
ment under zonal influence constraint. In: Proceedings of the 39th ACM/SIGAPP
Symposium on Applied Computing. SAC ’24, pp. 329–336. Association for Com-
puting Machinery, New York, NY, USA (2024). https://doi.org/10.1145/3605098.
3636052 . https://doi.org/10.1145/3605098.3636052
[46] Ali, D., Banerjee, S., Prasad, Y.: Towards regret free slot allocation in bill-
board advertisement. CoRR abs/2401.16464 (2024) https://doi.org/10.48550/
ARXIV.2401.16464 2401.16464
[47] Ali, D., Bhagat, A.K., Banerjee, S., Prasad, Y.: Efficient algorithms for regret
minimization in billboard advertisement (student abstract). Proceedings of the
AAAI Conference on Artificial Intelligence 37(13), 16148–16149 (2024) https:
//doi.org/10.1609/aaai.v37i13.26934
[48] Wang, C., Chen, W., Wang, Y.: Scalable influence maximization for indepen-
dent cascade model in large-scale social networks. Data Mining and Knowledge
Discovery 25, 545–576 (2012)
[49] Fink, C.G., Omodt, N., Zinnecker, S., Sprint, G.: A congressional twitter network
dataset quantifying pairwise probability of influence. Data in Brief (2023)
[50] Yin, H., Benson, A.R., Leskovec, J., Gleich, D.F.: Local higher-order graph clus-
tering. In: Proceedings of the 23rd ACM SIGKDD International Conference on
Knowledge Discovery and Data Mining. KDD ’17, pp. 555–564. Association for
Computing Machinery, New York, NY, USA (2017). https://doi.org/10.1145/
3097983.3098069 . https://doi.org/10.1145/3097983.3098069
[51] Leskovec, J., Mcauley, J.: Learning to discover social circles in ego networks.
Advances in neural information processing systems 25 (2012)
[52] Leskovec, J., Huttenlocher, D., Kleinberg, J.: Predicting positive and nega-
tive links in online social networks. In: Proceedings of the 19th International
44

Conference on World Wide Web. WWW ’10, pp. 641–650. Association for Com-
puting Machinery, New York, NY, USA (2010). https://doi.org/10.1145/1772690.
1772756 . https://doi.org/10.1145/1772690.1772756
[53] Nguyen, H.T., Thai, M.T., Dinh, T.N.: A billion-scale approximation algorithm
for maximizing benefit in viral marketing. IEEE/ACM Trans. Netw.25(4), 2419–
2429 (2017) https://doi.org/10.1109/TNET.2017.2691544
45
