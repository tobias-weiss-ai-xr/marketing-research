---
title: A Reverse Reachable Set Based Approach for Motif Oriented Profit maximization in Social Networks
url: https://arxiv.org/abs/2512.19237
category: social-media
subcategory: empirical
date: 2025-12
venue: ''
authors:
- Poonam Sharma
- Suman Banerjee
source: arxiv
pdf_url: https://arxiv.org/pdf/2512.19237
pages: 16
chars: 49149
fetched_at: '2026-11-08T13:09:31+00:00'
kb_version: 1
---

# A Reverse Reachable Set Based Approach for Motif Oriented Profit maximization in Social Networks

A Reverse Reachable Set Based Approach for
Motif Oriented Proﬁt maximization in Social
Networks
Poonam Sharma and Suman Banerjee
Indian Institute of Technology Jammu, J & K-181221, India.
{poonam.sharma,suman.banerjee}@iitjammu.ac.in
Abstract. Proﬁt Maximization is one of the key objectives for social
media marketing, where the task is to choose a limited number of highly
inﬂuential nodes such that their initial activation leads t o maximum
proﬁt. In this paper, we introduce a variant of the Proﬁt Maxi mization
Problem where we consider that instead of nodes, beneﬁts are assigned
to some of the motifs of the graph, and these beneﬁt values can be
earned once a given threshold count of nodes from the motifs i s inﬂu-
enced. The goal here is to choose a limited number of nodes for initial
activation (called ‘seed nodes’) such that the motif-orien ted proﬁt gets
maximized. Formally, we call our problem the Motif Oriented Profit
Maximiza tionProblem. We show that the problem is NP-hard to solve
optimally. We propose a Reverse Reachable Set-based framew ork to solve
our problem. The proposed methodology broadly divides into three steps:
KPT Estimation and RR Set generation, Seed Set Selection, and Motif
Oriented Proﬁt Estimation. The proposed methodology has be en ana-
lyzed to understand its time and space requirements. It has b een im-
plemented with real-world social network datasets, and the results are
reported. We observe that the seed set selected by the propos ed solution
approaches leads to more proﬁt compared to the seed sets sele cted by
the existing methods. The whole implementation and data are available
at: https://github.com/PoonamSharma-PY/MotifProﬁt.
Keywords: Social Networks, Motif, Proﬁt Maximization Problem, Seed
Set, Information Diﬀusion.
1 Introduction
In recent times, Online Social Networks play a pivotal role in spreading news,
ideas, rumors, etc., and this happens due to the diﬀusion of i nformation [ 1, 2].
People tend to share the information through social media po sts, and people
who are in the friend (or follower) list may wish to like, shar e, comment, etc. on
the post. If the person is inﬂuential, then there is a very hig h chance that many
of the users of the network will come to know about the fact. Th is phenomenon
has been exploited by commercial houses for promoting their brands. For this
purpose, they choose a limited number of inﬂuential people f rom the network
arXiv:2512.19237v1  [cs.SI]  22 Dec 2025

2 Sharma and Banerjee
and distribute free (or discounted) products with the hope t hat they will spread
positive words about the product due to word-of-mouth. This notion is called
Viral Marketing through Social Media. In recent times, comm ercial houses spend
a signiﬁcant portion of their revenue on Social Media advert isements.
To study the diﬀusion process in a social network, several mo dels have been
introduced and studied in the literature. Among them, the In dependent Cas-
cade Model is the most popular one. In the context of viral mar keting, the
key computational problem that arises is that given a social network, how can
we eﬀectively select a limited number of nodes for initial ac tivation such that
the inﬂuence gets maximized? Initially, this problem was po sed by Domingos
and Richardson [ 4, 14]. Later, Kempe et al. [ 7, 8] showed that this problem is
NP-hard to solve optimally under the IC Model of diﬀusion. Th ey proposed an
iterative greedy approach based on marginal inﬂuence gain c omputation, which
provides a (1− 1 e )-factor approximate solution. This study triggers a signiﬁ cant
amount of research in this direction, and a huge amount of lit erature is avail-
able. The proposed solution approaches for this problem can be classiﬁed into
the following categories: Approximation Algorithms [ 12], Heuristic Solutions [ 3],
Soft Computing-based Approaches, Reverse Reachable Set-b ased Approaches,
and many more.
In practice, social networks are formed by rational human be ings, which
means if a user is acting as a seed user, then (s)he must be ince ntivized. Also,
in commercial advertising, the key objective is to maximize proﬁt. Hence, the
following problem is of immense importance: Given a social n etwork, the cost
and beneﬁt of each user, and a ﬁxed budget, how can we select a s eed set within
the budget to maximize the proﬁt? This problem has been refer red to as the
Proﬁt Maximization Problem. In the past decade, this proble m has been studied
extensively in the literature. In most of the studies, it has been considered that
every user of the network has some beneﬁt value that can be ear ned if the user
is inﬂuenced. Now, consider the following scenario. A group of friends wants to
dine in a restaurant. Now, any restaurant brand will be able t o attract this group
and earn some proﬁt if that brand can inﬂuence the whole group . A small group
of nodes in a network is called a motif. Sometimes it is import ant to consider
inﬂuencing a whole motif rather than an individual user. To i nﬂuence a motif,
it may be suﬃcient to inﬂuence the majority of the users prese nt in the motif.
In this paper, we consider the problem of maximizing the proﬁ t of a commercial
campaign by inﬂuencing the motifs. We call this problem the Motif Oriented
Profit Maximization Problem. In this problem, we are given a social network
where each user is assigned a selection cost, a set of motifs a long with their
corresponding beneﬁt value, and a budget. This problem asks to choose a subset
of nodes within the allocated budget such that the earned pro ﬁt by maximizing
the inﬂuence among the motifs is maximized. To the best of our knowledge, we
are the ﬁrst to study the Proﬁt Maximization Problem under th e motif-oriented
setup. In particular, we make the following contributions i n this paper:
– We introduce and study the Motif Oriented Profit Maximization
Problem for which there does not exist any literature.

Motif Oriented Proﬁt maximization in Social Networks 3
– We propose a reverse reachable set-based solution approach to solve our
problem with a detailed analysis and illustration.
– A number of experiments have been conducted on real-world so cial network
datasets, and the results are compared with the existing met hods to show
the eﬀectiveness and eﬃciency of the proposed solution appr oach.
The rest of the paper has been organized as follows. Section 2 describes back-
ground information and deﬁnes the problem formally. Sectio n 3 describes the
proposed solution approaches with a detailed analysis. The experimental eval-
uation of the proposed solution approaches has been describ ed in Section 4.
Finally, Section 5 concludes our study and gives future research directions.
2 Background and Problem Deﬁnition
In this section, we describe the required preliminary conce pts and subsequently
deﬁne our problem formally. Initially, we start by describi ng the notion of social
networks.
2.1 Social Networks
A social network is deﬁned as an interconnected structure am ong a group of
people, which has been formally stated in Deﬁnition 1.
Deﬁnition 1 (Social Networks). A social network is often represented as a
simple, (un)directed, weighted graphG(V,E,P) where the vertex set V represents
the set of users connected through the network, the edge set rep resents the social
relationships, and the edge weight function P maps each edge to its corresponding
inﬂuence probability, i.e., P :E−→ (0, 1].
For any edge (uiuj)∈E , it means that ui and uj are in the social relationship.
We reserve n and m to denote the number of nodes and edges, respectively.
For any edge (uiuj)∈E , its inﬂuence probability is denoted by P(uiuj). In our
study, we assume that every edge has a non-zero inﬂuence prob ability, i.e., for
any edge (uiuj)∈E , 0 <P(uiuj)≤ 1.
In graph data analytics, there has always been an interest in understanding
how large networks (e.g., Social Networks, Biological Netw orks, etc.) have been
formed. It has been found that a large network is formed using small networks
as a building block, which is also called a Motif, as stated in Deﬁnition 2.
Deﬁnition 2 (Motif ). A motif is a subgraph that appears signiﬁcantly more
often in a real network than would be expected in a randomized n etwork with the
same number of nodes and edges.
2.2 Information Diﬀusion and Social Inﬂuence Maximization
Among many, one of the properties of social networks is the di ﬀusion of infor-
mation, which says that an individual connected through onl ine social networks

4 Sharma and Banerjee
tends to share the information. Now, it is expected that if th e person is inﬂuen-
tial, then he will have many social neighbors, and a large num ber of them will
be inﬂuenced by the information and share it further. This pr ocess will be con-
tinued, and the hope is that at the end of the diﬀusion process , a large number
of people will be inﬂuenced. The entire process is referred t o as the Information
Diﬀusion. This process starts from a set of initially active nodes ref erred to as
Seed Nodes. How the information diﬀusion happens in the netw ork depends on
the diﬀusion model that has been chosen. In this study, we ass ume that the dif-
fusion of information is happening by the rule of the IC Model , which has been
stated in Deﬁnition 3.
Deﬁnition 3 (Independent Cascade Model). As per the IC Model, the dif-
fusion process starts from a set of initially active nodes cal led seed nodes and
proceeds in discrete time steps. In the diﬀusion process, an a ctive node at time
step t will get a single chance to activate its inactive neighbors. A node’s state
can be either ‘activated’ (also known as inﬂuenced) or ‘non- activated’ (also called
non-inﬂuenced). A node can change its state from ‘non-activ ated’ to ‘activated’;
however, it cannot do so vice versa. The diﬀusion process stops when no more
node activation is possible.
At the end of the diﬀusion process, the number of inﬂuenced no des is called the
inﬂuence of the seed set. For any given seed set S ⊆V, I(S) denotes the set
of inﬂuenced nodes and σ(S) denotes the inﬂuence of S, where σ() is the social
inﬂuence function (a set function deﬁned on the ground set V) which maps each
subset of the users of the network to their expected inﬂuence , i.e., σ : 2 V−→ R+ 0 .
In the IC Model, for a given seed set, its inﬂuence can be compu ted by construct-
ing 2m many live graphs and taking the expected value as described i n [ 7]. As
mentioned in the literature, the inﬂuence under the IC Model of diﬀusion is non-
negative, monotone, and sub-modular. In the context of info rmation diﬀusion,
one well-studied problem is the Social Inﬂuence Maximizati on Problem which
has been stated in Deﬁnition 4.
Deﬁnition 4 (Social Inﬂuence Maximization Problem). Given a social
network G(V,E,P), and a positive integer k, the problem of social inﬂuence
maximization asks to choose k many users to activate initially, such that the
maximum number of nodes gets inﬂuenced at the end of the diﬀus ion process.
Mathematically, this problem can be posed as an optimizatio n problem as men-
tioned in Equation 1.
SOP T←− argmax
S⊆V and |S|=k
σ(S) (1)
2.3 Proﬁt Maximization in Social Networks
In commercial campaigns, the users of the network need to be i ncentivized, and
every user of the network is assigned some beneﬁt value, whic h can be earned
if the user is inﬂuenced. These notions have been formalized by the Cost and
Beneﬁt functions which are denoted by C and b, respectively, i.e., C :V−→ R+

Motif Oriented Proﬁt maximization in Social Networks 5
and b :V−→ R+ 0 . For any user u∈V , its cost and beneﬁt are denoted by C(u)
and b(u), respectively. Now, we deﬁne the notion of the earned proﬁt b y a seed
setS in Deﬁnition 5.
Deﬁnition 5 (Earned Proﬁt). Given a seed set S, the earned proﬁt by S is
deﬁned as the diﬀerence between the earned beneﬁt by the seed s et and the cost
of the seed set. This is denoted by Φ(S) and can be mathematically posed in
Equation 2.
Φ(S) =
∑
u∈I(S)
b(u)−
∑
u∈S
C(u) (2)
Naturally, in a commercial campaign, it is important to sele ct a limited number
of inﬂuential nodes within the budget to maximize the proﬁt. This problem has
been referred to as the Proﬁt Maximization Problem in the lit erature and stated
in the Deﬁnition 6.
Deﬁnition 6 (Proﬁt Maximization Problem). Given a social network,
G(V,E,P) with the Cost and Beneﬁt functions C :V−→ R+ and b :V−→ R+ 0 ,
respectively, and a ﬁxed budgetB, the proﬁt maximization problem asks to choose
a set of nodes for initial activation such that the earned proﬁ t by the seed set is
maximized. Mathematically, this problem can be posed as sho wn in Equation 3.
SOP T←− argmax
S⊆V and ∑
u∈S
C(u)≤B
Φ(S) (3)
SOP T denotes the optimal seed set for the budget B inG. As mentioned previ-
ously, this problem has been studied in the literature and a n umber of solution
methodologies have been proposed. However, as mentioned in Section 1, we study
the Motif Oriented Proﬁt Maximization Problem. In this prob lem, we assume
that along with the input social network G(V,E,P), we are also given a set of
ℓ motifsM ={m1, m2, . . . , mℓ} and a beneﬁt function b that maps each of the
motifs to its corresponding beneﬁt value, i.e., b :M−→ R+ 0 . For any arbitrary
motif mj ∈M ,|mj| denotes the number of vertices that the motif contains.
The associated beneﬁt with the motif is denoted by b(mj). This beneﬁt can be
earned if the motif is inﬂuenced. Now, how do we decide whethe r a motif has
been inﬂuenced or not? This depends on the inﬂuence model. In this study, we
assume that a threshold has been given, and if at least the thr eshold number
of nodes of the motif are inﬂuenced, for the motif mj ∈ M, its threshold is
denoted by τj, 1≤ τj≤| mj|. Given a seed set S⊆V , for every motif mj∈M ,
we deﬁne an indicator boolean variable Imj (S) which takes the value 1 if the
motif is inﬂuenced and 0, otherwise. This has been mentioned in the Conditional
Equation 4.
Imj (S) =
{
1, if|I(S)∩ V (mj)|≥ τj
0, otherwise (4)
Now, we deﬁne the notion of Motif Oriented Earned Proﬁt by a gi ven seed set,
which is stated in Deﬁnition 7.

6 Sharma and Banerjee
Deﬁnition 7 (Motif Oriented Earned Proﬁt). Given a Social Network
G(V,E,P), a seed setS, and a set of motifs M ={m1, m2, . . . , mℓ} with the cor-
responding beneﬁt function b :M−→ R+ 0 , and the cost function C :V−→ R+,
the motif oriented earned proﬁt by the seed set S is deﬁned as the diﬀerence
between the expected motif oriented earned beneﬁt by the seed s et and the cost of
the seed set. This has been mathematically represented in Eq uation 5.
ΦM(S) =
∑
g∈L(G)
P r(g)
∑
mj ∈M
Imj (S)· b(mj)−
∑
u∈S
C(u) (5)
The following question arises: Given a seed set, how eﬃcient ly can we compute
its motif-oriented earned proﬁt? Theorem 1 states the fact.
Theorem 1. Given a Social Network G(V,E,P), a seed set S, and a set of
motifsM ={m1, m2, . . . , mℓ}, accurately computing the motif oriented earned
proﬁt is a #P-Complete Problem.
Now, in a commercial campaign, of course, it is important to c hoose the seed set
eﬀectively. Within the allocated budget, we formally state the Motif Oriented
Proﬁt Maximization Problem in Deﬁnition 8.
Deﬁnition 8 (Motif Oriented Proﬁt Maximization Problem). Given a
Social NetworkG(V,E,P), a set of motifs M ={m1, m2, . . . , mℓ} with the cor-
responding beneﬁt function b :M−→ R+ 0 , cost function C :V −→R+, and
a ﬁxed budget B, this problem asks to choose a seed set to maximize the Motif
Oriented Earned Proﬁt as stated in Deﬁnition 7 such that the total cost of the
seed set is less than the budget. Mathematically, this probl em has been stated in
Equation 6.
SOP T←− argmax
S⊆V and ∑
u∈S
C(u)≤B
ΦM(S) (6)
As mentioned in [ 13], the Proﬁt Maximization Problem is NP-hard. Motif Ori-
ented Proﬁt Maximization Problem is a generalization of the Proﬁt Maximiza-
tion Problem; hence, Motif Oriented Proﬁt Maximization Pro blem will also re-
main NP-hard. This has been formally stated in Theorem 2.
Theorem 2. Given a Social Network G(V,E,P), a set of motifs M ={m1, m2,
. . . , mℓ} with the corresponding beneﬁt function b :M−→ R+ 0 , cost function
C :V−→ R+, and a ﬁxed budget B, ﬁnding an optimal seed set to maximize the
Motif Oriented earned proﬁt is NP-hard.
Next, we proceed to describe the solution methodologies sub sequently.
3 Proposed Approach
Our proposed solution approach is based on the notion of Reve rse Reachable
Set, which has been stated in Deﬁnition 9.

Motif Oriented Proﬁt maximization in Social Networks 7
Deﬁnition 9 (Reverse Reachable Set). [15] Given a Social NetworkG(V,E,P),
and a node v, the reverse reachable set of v is denoted by RR(v) and deﬁned as
the set of nodes from which there exists a directed path to the node v which has
been stated in Equation 7
RR(v) ={u : There exists a path from u to v} (7)
Algorithm 1 Motif Oriented RIS Framework
Input: GraphG(V,E ,P), Cost function C(·), Beneﬁt function b(·), Motif set M,
Budgets B, Thresholds τ , Simulation count T
Output: Seed setS⊆V
1: for each budgetB∈ B do
2: k←⌊B / minvC(v)⌋
3: κ← Estima teKPT(G, k,C, b)
4: θ← ComputeTheta(κ,|V|, k)
5: R← Genera teRRsets(θ,G)
6: S← GreedySeedSelection(R,C, b,B)
7: Perform T Monte Carlo simulations of diﬀusion from S to obtain
{A1, A2, . . . , AT}
8: Compute average inﬂuence beneﬁt: Π← 1 T ∑T i=1 ∑ v∈Ai b(v) 9: for each threshold τ∈ Thresholds do
10: MotifProfit← ComputeMotifProfit({Ai},M, b, τ,C(S))
11: Log result: Budget B, Seed set S, Π, MotifProﬁt, θ, κ
12: end for
13: end for
The Reverse Inﬂuence Sampling (RIS) framework enhances cla ssical inﬂuence
maximization by incorporating motif-aware evaluation. It consists of three main
parts: (i) estimation of KPT and generation ofRR sets, (ii) greedy node selection
for the seed set, and (iii) computation of motif-based proﬁt . Algorithm 1 illus-
trates this process. Given a graphG = (V,E,P), node costC(·), beneﬁt b(·), motif
setM, budgets B, thresholds τ , and simulation count T , the algorithm iteratively
processes each budget B. For each budget, it estimates the maximum number
of seeds k and computes the inﬂuence lower bound κ using the EstimateKPT
procedure (Line 4). This value determines the required numb er of reverse reach-
able sets θ (Line 5).RR sets are generated ( GenerateRRSets, Line 6), and a
greedy strategy then selects the seed set S under the budget constraint (Line 7).
The diﬀusion process is simulated T times to obtain the average proﬁt (Lines 8–
9). Finally, for each threshold τ , motifs activated in the simulations are identiﬁed,
their motif-based proﬁt is computed ( ComputeMotifProfit, Line 11), and re-
sults such as seed sets, inﬂuence proﬁt, motif proﬁt, and sam pling parameters
are recorded (Line 12).
3.1 Part (i): Estimation of KPT and Generation of RR sets
The EstimateKPT procedure (Algorithm 2) estimates the KPT value, a key
parameter for determining the number of reverse reachable ( RR) sets needed in

8 Sharma and Banerjee
Algorithm 2 EstimateKPT
Input: GraphG(V,E ,P), Seed count k, Cost function C(·), Beneﬁt function b(·)
Output: Estimated KPT value κ
1: η←|V| , m←|E|
2: Deﬁne pv∝ b(v) C(v) for all v
3: for i = 1 to log2(n)− 1 do
4: ci← Required samples at round i
5: Initialize sum← 0
6: for j = 1 to ci do
7: Sample node v using pv
8: Generate RR(v) set
9: Estimate κv = 1− (1− (|RR(v)|/m))k
10: sum← sum + κv
11: end for
12: if sum ci > 1 2i then 13: return κ = n·sum 2ci
14: end if
15: end for
16: return κ = 1
RIS-based algorithms. It ﬁrst identiﬁes the number of nodes n =|V| and edges
m =|E| (Line 3). To emphasize nodes with higher inﬂuence, an import ance sam-
pling distribution is deﬁned with probabilities proportio nal to b(v)/C(v) (Line 4).
The estimation runs iteratively over logarithmic rounds i = 1 to log2(n)− 1
(Line 5). In each round, ci samples are drawn (Line 6), and for each sample a
node v is selected (Line 9), its RR setRR(v) is generated (Line 10), and the
contribution κv = 1− (1−|RR (v)|/m)k is computed (Line 11). The results are
aggregated (Line 12), and the average sum ci is compared with 1/2i (Line 14). If satisﬁed, the algorithm returns κ = n·sum 2ci (Line 15); otherwise, if no threshold is met in any round, it returns κ = 1 (Line 18).
Complexity Analysis. In Algorithm 2, the main cost lies in the inner loop
(Lines 6–10), where each of the ci samples requires generating an RR set. A
singleRR set generation may, in the worst case, traverse all n =|V| nodes
and m =|E| edges. The outer loop (Line 3) executes for O(log n) rounds, so
the overall time complexity is O((n + m) log n), as proved in [ 17]. The space
complexity is O(n + m), dominated by storing the graph and temporary RR
sets.
Algorithm 3 GenerateRRsets
Input: θ,G(V,E ,P)
Output: Set ofRR setsR
1: Sample θ start nodes using importance probabilities
2: For each node, perform reverse BFS
3: returnR

Motif Oriented Proﬁt maximization in Social Networks 9
The GenerateRRsets procedure (Algorithm 3) generates a collection of
Reverse Reachable (RR) sets, the core data structure in RIS-based inﬂuence
maximization. The number of sets is given by θ =
(8+2ǫ) n ( l log n+log
(n
k
)
+log 2 )
KPT ǫ2 ,
with ǫ = 0.3 and l = 1 as in [ 17]. Given θ, the algorithm samples nodes using an
importance distribution proportional to their inﬂuence po tential (Line 3). For
each sampled node, a reverse BFS is performed (Line 4) to iden tify nodes that
could reach it under the IC diﬀusion model. After all samples are processed, the
complete set of θ manyRR sets in R is returned (Line 5) for evaluating seed
coverage in later steps.
Complexity Analysis. In Algorithm 3, eachRR set is constructed by per-
forming a reverse breadth-ﬁrst search (BFS) on a randomly sa mpled live-edge
graph under the IC model (Line 2). A single reverse BFS may, in the worst case,
traverse all n =|V| nodes and m =|E| edges of the graph, leading to a cost of
O(n + m) perRR set. Since the algorithm generates θ manyRR sets, the total
worst-case time complexity is O(θ(n + m)). The space complexity is O(θ·|RR| )
=O(θ· n) (when in the worst case, the size of an RR set is n), for storing all
generatedRR sets.
3.2 Part (ii): Greedy-Based approach for node selection of t he seed
set
Algorithm 4 GreedySeedSelection
Input:RR setsR, Cost function C(·), Beneﬁt function b(·), BudgetB
Output: Seed setS
1: Initialize S←∅ , RemainingBudget←B
2: while RemainingBudget > 0 do
3: for all nodes v /∈S do
4: Compute coverage score: number of RR sets containing v
5: Compute normalized score: score /C(v)
6: end for
7: Select node v∗ with highest normalized score within budget
8: if no such node exists then
9: break
10: end if
11: S←S∪{ v∗}, RemainingBudget← RemainingBudget -C(v∗)
12: Mark RR sets covered by v∗
13: end while
14: returnS
The GreedySeedSelection procedure (Algorithm 4) selects an optimal
seed set under a budget constraint using precomputed RR sets. It starts with
an empty seed setS and budgetB (Line 1), then iteratively adds nodes while the
budget remains (Line 2). In each round, all candidate nodes v /∈S are evaluated:
their coverage score is the number of RR sets containing v (Line 4), normalized

10 Sharma and Banerjee
by costC(v) (Line 5). The node v∗ with the highest aﬀordable normalized score
is chosen (Line 7). If no node ﬁts the budget, the loop termina tes (Lines 8–10).
Otherwise, v∗ is added toS, its cost subtracted, and its covered RR sets marked
(Lines 11–12) to avoid double counting. This process repeat s until the budget is
exhausted or no nodes remain, and the ﬁnal seed set S is returned (Line 14).
Complexity Analysis. In Algorithm 4, initialization (Line 1) takes O(1)
time. The main cost is the while loop (Lines 2–13), which may run up to B/Cmin
times, where Cmin = min v∈VC(v). In each iteration, computing coverage scores
for all n =|V| nodes requires processing θRR sets, givingO(n· θ·|RR (v)|). In
the worst case|RR(v)| = n, i.e.,O(θ·n2). Normalized score computation (Line 5)
and node selection (Line 7) add O(n) each, but are dominated as well. Marking
coveredRR sets (Line 12) takes O(θ· n). Hence, each iteration costs O(θ· n2),
and the overall time complexity is O
(
B
Cmin · θ· n2
)
. The space complexity is
O(n + θ· n) =O(θ· n) (asRR sets dominate the overall cost), for maintaining
node scores and marked RR sets.
3.3 Part (iii): Computation of Motif-based Proﬁt
Algorithm 5 ProcessMotifProﬁt
Input: Simulation results {Ai}, Motifs M, Beneﬁt b(·), Threshold τ , Seed cost
C(S)
Output: A verage motif-based proﬁt
1: for each simulation Ai do
2: Identify Mi←{ m∈M|| m∩ Ai|≥ τ}
3: Bi← ∑ v∈∪Mi b(v) 4: Πi← Bi−C (S)
5: end for
6: return 1 T ∑ i Πi
The ProcessMotifProfit procedure (Algorithm 5) concludes the RIS
framework by computing the average motif-based proﬁt from a given seed set
using multiple diﬀusion simulations under the IC model. It t akes as input the sim-
ulation results{Ai}, a motif set M, beneﬁt function b(·), threshold τ , and seed
cost C. For each simulation Ai, motifsMi are considered active if |m∩ Ai|≥ τ
(Line 1–2). The beneﬁt Bi is then the sum of b(v) over all nodes in the union
of active motifs (Line 3), and the net proﬁt Πi is Bi−C (S) (Line 4). After T
simulations, the average proﬁt 1 T ∑ i Πi is returned (Line 6).
Complexity Analysis. The time complexity of Algorithm 5 depends on
the number of simulations T , motifs |M|, motif size s, and nodes n. In each
simulation, checking threshold activation costs O(s) per motif, or O(|M| s) in
total. Computing the beneﬁt Bi then requires at most O(n) time. Hence, the
per-simulation cost is O(|M| s + n), and over T simulations the total runtime
isO(T (|M| s + n)). The space complexity is O(|M|s + n), for storing motif
deﬁnitions and activated nodes.

Motif Oriented Proﬁt maximization in Social Networks 11
Therefore, the overall time complexity of our proposed appr oach (Algo-
rithm 1) isO
(
(n + m) log n + θ(n + m) + B Cmin · θ· n2 + T (|M| s + n)
)
. The
overall space complexity is O(n + m + θ· n +|M| s + T· n).
4 Experimental Evaluation
We next present the experimental evaluation of the proposed approach, begin-
ning with the datasets.
4.1 Dataset Description
Our experiments use the following networks:
– US Congress (Congress) [ 5, 6]: Twitter interaction network for the 117th
United States Congress (House and Senate).
– Email-Eu-Core (Euemail) [ 11, 16]: Built from email exchanges in a large
European research institution; an edge (u, v) exists if u sent v at least one
email.
– Wikipedia V ote (Wikivote) [9,10]: Voting data from Wikipedia’s inception
to Jan 2008; nodes are users and a directed edge (u, v) means u voted on v.
Dataset Name Type of Graph Number of Nodes |V| Number of Edges |E| Maximum Degree dmax A verage Degree davg
US Congress Directed 475 13289 284 55.95
Email-Eu-Core Directed 1005 25571 546 50.89
Wiki-Vote Directed 7115 103689 1167 29.15
Table 1: Basic statistics of the datasets used in our experim ents.
All the datasets have been downloaded from Stanford Large Ne twork Dataset
Collection 1. Table 1 describes the basic statistics of the datasets.
4.2 Experimental Setup
In our study, several parameters need to be deﬁned, beginnin g with the inﬂuence
probability setting.
Inﬂuence Probability : We consider two settings:
– T rivalency: Each edge is assigned a probability uniformly at random fro m
{0.1, 0.01, 0.001}.
– Weighted Cascade : Each edge (u, v) has probability inversely proportional
to the in-degree of v, i.e., 1 degin(v) .
1 https://snap.stanford.edu/data/index.html

12 Sharma and Banerjee
Cost and Beneﬁt Values : We use a degree-proportional cost setting, where a
higher out-degree implies a higher cost, as in practice (e.g ., celebrities with more
followers demand higher fees). The beneﬁt of each node is the n assigned by
scaling its cost.
4.3 Baseline Methods
We compare our proposed methodology against the following b aselines:
– Random : Nodes are selected randomly until the budget is exhausted.
– High Degree : Nodes are ranked by degree and selected in order until the
budget is exhausted.
– CELF : A popular inﬂuence maximization algorithm by Leskovec et a l. [12],
adapted here for proﬁt maximization.
– Simple Greedy : Starting with an empty set, nodes are added iteratively
based on marginal proﬁt gain [ 7].
All baselines were implemented in Python 3.0.1+ with Networ kX 2.2.1, and
experiments were run on a Linux desktop with 64 GB RAM and a 32- core Intel
i9 processor.
4.4 Experimental Results and Discussions
We have analyzed three datasets for our experiments, which a re listed in Table 1.
Our research objective is to evaluate how well the algorithm s work with the
structural pattern of the graph, i.e., motifs. The metric us ed for comparison is
the motif-based proﬁt earned under a given budget. We also ai m to understand
which threshold values are eﬀective in maximizing motif-ba sed proﬁt. For the
Congress dataset (Figures 1 and 2), experiments were conducted for motif sizes
2, 3, and 4. We compared Random, High Degree, CELF, and Simple Greedy
with the Motif Oriented RIS approach. Across all probabilit y settings, motif
proﬁt increases monotonically with budget, and RIS consist ently outperforms
all other algorithms. Simple Greedy and CELF are often compe titive, while
Random and High Degree perform similarly. For instance, at b udget 10 under
Trivalency probability settings, RIS achieves 1323.8 unit s of proﬁt, compared to
794.9 for Simple Greedy (66% less) and 770.5 for CELF (71% les s). High Degree
and Random perform much worse, with RIS producing 110% and 15 3% higher
proﬁts, respectively. Similar trends are observed across o ther budgets and motif
sizes. In the Weighted Cascade probability setting, RIS aga in outperforms all
approaches by large margins (Figures 2 (a)–(f)). On average, RIS generates about
10990% more proﬁt than Random, 4644% more than High Degree, 2 222% more
than CELF, and 5873% more than Simple Greedy. The Euemail dat aset shows
even more striking results (Figures 3, 4). Under Trivalency, RIS outperforms by
260% over Random, 229% over High Degree, 188% over CELF, and 1 93% over
Simple Greedy. Under Weighted Cascade, RIS gains are enormo us, reaching
up to 85586% compared to Random, 22509% over High Degree, 161 05% over

Motif Oriented Proﬁt maximization in Social Networks 13
CELF, and 81017% over Simple Greedy. The Wikivote dataset (F igure 5) further
conﬁrms this trend. Random, High Degree, and Simple Greedy p erform about
105% worse than RIS, while CELF is 102% worse.
We next analyze the impact of threshold values of diﬀerent mo tif sizes. In the
Congress dataset, at threshold 2, motif proﬁts are higher as motifs are activated
more easily. RIS remains the best performer, e.g., achievin g 1755 units at budget
50 under Weighted Cascade probability setting for motif siz e 2 (Figure 2 (a)).
CELF and Simple Greedy reach about 60–100% of RIS’s performa nce, while
Random and High Degree remain signiﬁcantly lower. At thresh old 3, proﬁts de-
cline for all algorithms, though RIS still leads. Stricter t hresholds reduce overall
proﬁts since fewer motifs activate, but RIS continues to dom inate. For example,
at budget 40 under Weighted Cascade, RIS proﬁts are reduced b ut still higher
than all baselines, with Random and High Degree nearly negli gible. In Figure 1,
CELF achieves up to 79% of RIS at threshold 2 for motif size 2 an d remains
closer to RIS in motif sizes 3 and 4 for thresholds 2 and 3. The E uemail dataset
shows similar threshold eﬀects. Lower thresholds yield hig her proﬁts, while val-
ues closer to motif size reduce proﬁts. For example, in Triva lency with motif
size 4 at budget 10 (Figure 3 (d)–(f)), Random achieves 8410.31 at threshold 2,
5403.61 at threshold 3, and only 1997.59 at threshold 4. RIS c onsistently leads:
in Weighted Cascade with motif size 4 at budget 10 (Figure 4 (d)–(f)), it per-
forms 326% better than Simple Greedy at threshold 2, 1506% be tter at threshold
3, and 20483% better at threshold 4. The Wikivote dataset als o reﬂects these
eﬀects (Figure 5 (b)–(c)): at budget 30 for motif size 3, Simple Greedy perfor ms
97% worse (threshold 2) and 103% worse (threshold 3) than RIS .
Across all datasets, RIS consistently outperforms Random, High Degree,
CELF, and Simple Greedy, conﬁrming its superiority in explo iting motifs. While
CELF and Simple Greedy are occasionally competitive, Rando m and High De-
gree perform poorly, especially under the Weighted Cascade probability set-
ting. Threshold analysis shows that smaller thresholds giv e higher proﬁts, while
stricter ones reduce them across all algorithms. Nonethele ss, RIS remains the
clear leader, showing robustness under varying activation criteria.
5 Concluding Remarks
In this paper, we have studied the Motif-Oriented Proﬁt Maxi mization Prob-
lem, where, given a social network with the selection cost of the nodes and a set
of motifs with their corresponding beneﬁt value, this probl em asks to choose a
limited number of highly inﬂuential nodes within a budget su ch that the motif
oriented earned proﬁt gets maximized. This problem is NP-ha rd to solve opti-
mally. We have proposed a reverse reachable set-based solut ion approach. The
experimental results with real-world social network datas ets show the eﬀective-
ness of the proposed solution approach, motif oriented RIS. Our approach proves
to be robust across datasets, probability settings, and thr eshold values, estab-
lishing its eﬀectiveness in exploiting motif structures fo r proﬁt maximization.

14 Sharma and Banerjee
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s48
/s49/s107
/s50/s107
/s51/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40/s97/s41
/s32/s82/s97/s110/s100/s111/s109 /s32/s72/s105/s103/s104/s32/s68/s101/s103/s114/s101/s101 /s32/s67/s69/s76/s70 /s32/s83/s105/s109/s112/s108/s101/s32/s71/s114/s101/s101/s100/s121 /s32/s82/s73/s83
/s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32/s61/s32/s50/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s50
/s40/s98/s41
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s49/s107
/s50/s107
/s51/s107
/s52/s107
/s53/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32/s61/s32/s50/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s51
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s48
/s49/s107
/s50/s107
/s51/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32/s61/s32/s51/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s51
/s40/s99/s41
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s49/s107
/s50/s107
/s51/s107
/s52/s107
/s53/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32/s61/s32/s50/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s52
/s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32/s61/s32/s51/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s52 /s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32 /s61/s32/s52/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s52
/s40/s100/s41
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s48
/s49/s107
/s50/s107
/s51/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40/s101/s41
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s48
/s53/s48/s48
/s49/s107
/s50/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40/s102/s41
Fig. 1: Budget vs. Motif-Proﬁt for Congress (Trivalency).
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s48
/s49/s107
/s50/s107
/s51/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40/s97/s41
/s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32/s61/s32/s50/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s50
/s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32/s61/s32/s50/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s51 /s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32 /s61/s32/s51/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s51
/s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32/s61/s32/s50/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s52
/s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32/s61/s32/s51/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s52 /s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32 /s61/s32/s52/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s52
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s48
/s49/s107
/s50/s107
/s51/s107
/s52/s107
/s53/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40/s98/s41
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s48
/s49/s107
/s50/s107
/s51/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40/s99/s41
/s49/s48 /s49/s53 /s50/s48 /s50/s53 /s51/s48 /s51/s53 /s52/s48 /s52/s53 /s53/s48
/s48
/s49/s107
/s50/s107
/s51/s107
/s52/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40/s100/s41
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s48
/s49/s107
/s50/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40/s101/s41
/s32/s82/s97/s110/s100/s111/s109 /s32/s72/s105/s103/s104/s32/s68/s101/s103/s114/s101/s101 /s32/s67/s69/s76/s70 /s32/s83/s105/s109/s112/s108/s101/s32/s71/s114/s101/s101/s100/s121 /s32/s82/s73/s83
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s48
/s49/s107
/s50/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40/s102/s41
Fig. 2: Budget vs. Motif-Proﬁt for Congress (Weighted Casca de).
Now, our future study on this problem will remain concentrat ed on developing
more eﬃcient solution methodologies.

Motif Oriented Proﬁt maximization in Social Networks 15
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s53/s107
/s54/s107
/s55/s107
/s56/s107
/s57/s107
/s49/s48/s107
/s49/s49/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40/s97/s41
/s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32/s61/s32/s50/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s50
/s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32/s61/s32/s50/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s51 /s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32 /s61/s32/s51/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s51
/s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32/s61/s32/s50/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s52
/s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32/s61/s32/s51/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s52 /s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32 /s61/s32/s52/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s52
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s56/s107
/s57/s107
/s49/s48/s107
/s49/s49/s107
/s49/s50/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40/s98/s41
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s52/s107
/s54/s107
/s56/s107
/s49/s48/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40/s99/s41
/s32/s82/s97/s110/s100/s111/s109 /s32/s72/s105/s103/s104/s32/s68/s101/s103/s114/s101/s101 /s32/s67/s69/s76/s70 /s32/s83/s105/s109/s112/s108/s101/s32/s71/s114/s101/s101/s100/s121 /s32/s82/s73/s83
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s56/s107
/s57/s107
/s49/s48/s107
/s49/s49/s107
/s49/s50/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40/s100/s41
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s53/s107
/s54/s107
/s55/s107
/s56/s107
/s57/s107
/s49/s48/s107
/s49/s49/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40/s101/s41
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s50/s107
/s51/s107
/s52/s107
/s53/s107
/s54/s107
/s55/s107
/s56/s107
/s57/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40/s102/s41
Fig. 3: Budget vs. Motif-Proﬁt for Euemail (Trivalency).
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s48
/s50/s107
/s52/s107
/s54/s107
/s56/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40/s97/s41
/s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32/s61/s32/s50/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s50
/s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32/s61/s32/s50/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s51 /s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32 /s61/s32/s51/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s51
/s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32/s61/s32/s50/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s52
/s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32/s61/s32/s51/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s52 /s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32 /s61/s32/s52/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s52
/s32/s82/s97/s110/s100/s111/s109 /s32/s72/s105/s103/s104/s32/s68/s101/s103/s114/s101/s101 /s32/s67/s69/s76/s70 /s32/s83/s105/s109/s112/s108/s101/s32/s71/s114/s101/s101/s100/s121 /s32/s82/s73/s83
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s48
/s50/s107
/s52/s107
/s54/s107
/s56/s107
/s49/s48/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40/s98/s41
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s48
/s49/s107
/s50/s107
/s51/s107
/s52/s107
/s53/s107
/s54/s107
/s55/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40/s99/s41
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s48
/s50/s107
/s52/s107
/s54/s107
/s56/s107
/s49/s48/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40/s100/s41
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s48
/s50/s107
/s52/s107
/s54/s107
/s56/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40/s101/s41
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s48
/s49/s107
/s50/s107
/s51/s107
/s52/s107
/s53/s107
/s54/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40/s102/s41
Fig. 4: Budget vs. Motif-Proﬁt for Euemail (Weighted Cascad e).
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s48
/s49/s107
/s50/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40 /s97 /s41
/s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32/s61/s32/s50/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s50 /s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32/s61/s32/s50/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s51 /s77 /s111/s116/s105/s102/s32/s84/s104/s114/s101/s115/s104/s111/s108/s100/s32/s61/s32/s51/s44/s32/s77 /s111/s116/s105/s102/s32/s83/s105/s122/s101/s32/s61/s32/s51
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s48
/s49/s107
/s50/s107
/s51/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40 /s98 /s41
/s32/s82/s97/s110/s100/s111/s109 /s32/s72/s105/s103/s104/s32/s68/s101/s103/s114/s101/s101 /s32/s67/s69/s76/s70 /s32/s83/s105/s109/s112/s108/s101/s32/s71/s114/s101/s101/s100/s121 /s32/s82/s73/s83
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48
/s48
/s49/s107
/s50/s107
/s77/s111/s116/s105/s102/s45/s80/s114/s111/s102/s105/s116/s32/s69/s97/s114/s110/s101/s100
/s66/s117/s100/s103/s101/s116
/s40 /s99 /s41
Fig. 5: Budget vs. Motif-Proﬁt for Wikivote (Weighted Casca de).
References
1. Arnaboldi, V., Conti, M., Passarella, A., Dunbar, R.I.: O nline social networks and
information diﬀusion: The role of ego networks. Online Soci al Networks and Media

16 Sharma and Banerjee
1, 44–55 (2017)
2. Bakshy, E., Rosenn, I., Marlow, C., Adamic, L.: The role of social networks in
information diﬀusion. In: Proceedings of the 21st internat ional conference on World
Wide Web. pp. 519–528 (2012)
3. Chen, W., Wang, C., Wang, Y.: Scalable inﬂuence maximizat ion for prevalent
viral marketing in large-scale social networks. In: Procee dings of the 16th ACM
SIGKDD international conference on Knowledge discovery an d data mining. pp.
1029–1038. ACM (2010)
4. Domingos, P., Richardson, M.: Mining the network value of customers. In: Pro-
ceedings of the seventh ACM SIGKDD international conferenc e on Knowledge
discovery and data mining. pp. 57–66. ACM (2001)
5. Fink, C.G., Fullin, K., Gutierrez, G., Omodt, N., Zinneck er, S., Sprint, G., Mc-
Culloch, S.: A centrality measure for quantifying spread on weighted, directed
networks. Physica A (2023)
6. Fink, C.G., Omodt, N., Zinnecker, S., Sprint, G.: A congre ssional twitter network
dataset quantifying pairwise probability of inﬂuence. Dat a in Brief (2023)
7. Kempe, D., Kleinberg, J., Tardos, É.: Maximizing the spre ad of inﬂuence through
a social network. In: Proceedings of the ninth ACM SIGKDD int ernational confer-
ence on Knowledge discovery and data mining. pp. 137–146. AC M (2003)
8. Kempe, D., Kleinberg, J., Tardos, É.: Inﬂuential nodes in a diﬀusion model for
social networks. In: International Colloquium on Automata , Languages, and Pro-
gramming. pp. 1127–1138. Springer (2005)
9. Leskovec, J., Huttenlocher, D., Kleinberg, J.: Predicti ng positive and negative links
in online social networks. In: Proceedings of the 19th inter national conference on
World wide web. pp. 641–650 (2010)
10. Leskovec, J., Huttenlocher, D., Kleinberg, J.: Signed n etworks in social media. In:
Proceedings of the SIGCHI conference on human factors in com puting systems.
pp. 1361–1370 (2010)
11. Leskovec, J., Kleinberg, J., Faloutsos, C.: Graph evolu tion: Densiﬁcation and
shrinking diameters. ACM Transactions on Knowledge Discov ery from Data
(TKDD) 1(1), 2 (2007)
12. Leskovec, J., Krause, A., Guestrin, C., Faloutsos, C., F aloutsos, C., VanBriesen, J.,
Glance, N.: Cost-eﬀective outbreak detection in networks. In: Proceedings of the
13th ACM SIGKDD international conference on Knowledge disc overy and data
mining. pp. 420–429. ACM (2007)
13. Lu, W., Lakshmanan, L.V.: Proﬁt maximization over socia l networks. In: 2012
IEEE 12th international conference on data mining. pp. 479– 488. IEEE (2012)
14. Richardson, M., Domingos, P.: Mining knowledge-sharin g sites for viral marketing.
In: Proceedings of the eighth ACM SIGKDD international conf erence on Knowl-
edge discovery and data mining. pp. 61–70. ACM (2002)
15. Tang, Y., Xiao, X., Shi, Y.: Inﬂuence maximization: Near -optimal time complexity
meets practical eﬃciency. In: Proceedings of the 2014 ACM SI GMOD international
conference on Management of data. pp. 75–86. ACM (2014)
16. Yin, H., Benson, A.R., Leskovec, J., Gleich, D.F.: Local higher-order graph clus-
tering. In: Proceedings of the 23rd ACM SIGKDD internationa l conference on
knowledge discovery and data mining. pp. 555–564 (2017)
17. Zhou, M., Cao, W., Liao, H., Mao, R.: Motif-oriented inﬂu ence maximization for
viral marketing in large-scale social networks. In: Glober son, A., Mackey, L., Bel-
grave, D., Fan, A., Paquet, U., Tomczak, J., Zhang, C. (eds.) Advances in Neural
Information Processing Systems. vol. 37, pp. 135861–13588 2. Curran Associates,
Inc. (2024)
