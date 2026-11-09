---
title: Heuristics for Influence Maximization with Tiered Influence and Activation thresholds
url: https://arxiv.org/abs/2406.08876
category: social-media
subcategory: empirical
date: 2024-06
venue: ''
authors:
- Rahul Kumar Gautam
- Anjeneya Swami Kare
- Durga Bhavani S
source: arxiv
pdf_url: https://arxiv.org/pdf/2406.08876
pages: 15
chars: 30433
fetched_at: '2026-11-08T13:11:14+00:00'
kb_version: 1
---

# Heuristics for Influence Maximization with Tiered Influence and Activation thresholds

Heuristics for Influence Maximization with Tiered Influence
and Activation thresholds
Rahul Kumar Gautam0009−0009−7693−3863, Anjeneya Swami Kare0000−0003−3644−4802, and Durga
Bhavani S.0000−0003−4413−0328
School of Computer and Information Sciences,
University of Hyderabad,
Hyderabad, India
19mcpc06@uohyd.ac.in,askcs@uohyd.ac.in,sdbcs@uohyd.ac.in
Abstract. The information flows among the people while they communicate through social
media websites. Due to the dependency on digital media, a person shares important informa-
tion or regular updates with friends and family. The set of persons on social media forms a
social network. Influence Maximization (IM) is a known problem in social networks. In social
networks, information flows from one person to another using an underlying diffusion model.
There are two fundamental diffusion models: the Independent Cascade Model (ICM) and the
Linear Threshold Model (LTM). In this paper, we study a variant of the IM problem called
Minimum Influential Seeds (MINFS) problem proposed by Qiang et al.[16]. It generalizes the
classical IM problem with LTM as the diffusion model. Compared to IM, this variant has
additional parameters: the influence threshold for each node and the propagation range. The
propagation range is a positive integer that specifies how far the information can propagate
from a node. A node on the network is not immediately influenced until it receives the same
information from enough number of neighbors (influence threshold). Similarly, any node does
not forward information until it receives the same information from a sufficient number of
neighbors (activation threshold). Once a node becomes activated, it tries to activate or in-
fluence its neighbors. The MINFS problem aims to select the minimum number of initial
spreader nodes such that all nodes of the graph are influenced.
In this paper, we extend the study of the MINFS problem. We propose heuristics that
construct seed sets based on the average degree of non-activated nodes, closest first, and
backbone-based heaviest path. We have also proposed a pruning technique that further re-
duces the size of the seed sets. We have implemented the existing heuristics and the proposed
heuristics. We have done extensive experimentation on18 real-world data sets. The proposed
heuristics give improved seed sets compared to the existing heuristics.
1 Introduction
Inthisdigitalworld,peoplegetnewsorinformationdigitallyontheirgadgets.Duetotheadvantages
of social media, human beings are rapidly adopting social media in their daily life. However, there
are some pros and cons of social media. Some disadvantages are rumor-spreading, privacy-related
issues, data theft, etc. Nevertheless, getting important information about what is happening in
society becomes essential. As we have seen during the COVID-19 pandemic, the government has to
make people aware of the pandemic and related safety measures. Almost all countries’ governments
use social media to run awareness campaigns as it saves the time and effort of the government.
On account of the enormous applications of social media, the discussion on how information
propagates on social media networks becomes very important. The influence maximization problem
arXiv:2406.08876v1  [cs.SI]  13 Jun 2024

is related to information propagation and maximizing the influenced people in social networks. A
node in the social network is said to be influenced by a message when it starts believing the message.
On the other hand, a node is said to be activated when it starts forwarding (spreading) the message
to its neighbors.
Kempe et al.[10] introduced the Influence Maximization (IM) problem. The IM problem is
also called the Target Set Selection (TSS) problem. Using the Linear Threshold Model (LTM) of
diffusion, there are primarily two variants of the TSS problem: the maximization version and the
minimization version. For the maximization version, input is a graphG = (V, E) and a positive
integer k, and the problem asks to compute a target set (seed set)S ⊆ V of size at mostk that
activates the maximum number of vertices. For the minimization version, input is a graphG and
an integer inputℓ, and the problem asks to compute a target set (seed set)S ⊆ V of the minimum
size that activates at leastℓ vertices. If ℓ = |V |, then the problem asks to compute a target set
S ⊆ V of the minimum size that activates all the vertices of the graph.
Cordasco et al.[5] studied a variant of the TSS problem, which they called the Perfect Evan-
gelizing Set (PES) problem. For the PES problem, input is a graphG, influence and activation
(evangelizing ) thresholdstI , tA : V → {0, 1, 2, . . . ,} and the problem asks to compute a target set
(seed set) S ⊆ V of minimum size that influences all the vertices of the graph. Cordasco et al.[6]
also introduced a problem called the Perfect Awareness (PA) problem, which is a specialization of
the PES problem. In the PA problemtI (v) = 1, ∀v ∈ V.
Qiang et al.[16] proposed a variant of the TSS problem, which they call the Minimum Influential
Seeds (MINFS) problem, which is a generalization of the PES problem. Compared to the PES
problem, the MINFS problem has an additional input parameter called the propagation range
p ∈ Z+. The propagation range indicates how far the information propagates from one node to
another node. The MINFS problem withp = Diameter(G) is equivalent to the PES problem. For
the experimentation Qiang et al.[16] used two input parametersθ and α such that 0 < θ ≤ α ≤
1. For each vertex u ∈ V, they set the influence threshold tI (u) = θ.deg(u) and the activation
threshold tA(u) = α.deg(u). In the MINFS problem, the information can flow from the sources
(initial spreaders) up to p ∈ Z+ distance. If a vertex u receives information from at least tI (u)
neighbors, u becomes influenced. Likewise, If a vertexu receives information from at leasttA(u)
neighbors, u becomes activated and forwards information to the neighbors. An initial spreader can
not activate or contribute to activating vertices at more thanp distance. The set of initial spreaders
is called a seed set. The objective is to find the set of initial spreaders (seed set) of minimum size,
which influences all the vertices of the graph.
Qiang et al.[16] proposed minimization and maximization variants of the Influential Seeds
problem. They have proposed heuristics for the MINFS problem. In this paper, we extend the
study of the MINFS problem. We propose three heuristics and a pruning strategy to improve the
solutions obtained by the heuristics. We have the following results:
- The first heuristic picks the average number of highly influential inactive vertices for the seed
set in each iteration. It improves the quality of the result and running time compared to existing
heuristics for the problem.
- The second heuristic finds the closest highly influential seed vertex from the seed set.
- The third heuristic, a backbone-based heuristic, finds the dominant path and selects vertices
from the dominant path for the seed set.
- The proposed pruning technique is applied to solutions returned by the existing and as well as
the proposed heuristics. The pruning technique improves the quality of the solutions.

The whole paper is organized as follows. In section 2, we present related and recent studies on
the MINFS problem, such as influence maximization, perfect awareness problem, and the target set
selection problem. Section 4 covers our proposed heuristics. In section 5, we analyze the performance
of algorithms and present results on the real datasets. The final section of the article concludes the
paper.
2 Related Work
Influence Maximization (IM) in social networks is an essential area of research due to its applications
in business advertisements, viral marketing, and campaigning. The IM problem is also known as
the Target Set Selection (TSS) problem. Kempe et al.[10] introduced the IM problem. They proved
that the IM problem is NP-hard and proposed experimental algorithms for the problem. The greedy
algorithm by Kempe et al.[10] guarantees approximation1 − (1/e) (e is logarithmic base). For the
TSS problem based on the decreasing cascade model, the1 − (1/e) − ϵ-approximation algorithm
was studied by Kempe et al.[10]. Chen[4] studied the hardness of the TSS problem and proved that
the problem is hard to approximate within a poly-logarithmic factor. There are two fundamental
diffusion models: the Independent Cascade Model (ICM) and the Linear Threshold Model (LTM).
A vertex influences its neighbors with some probability in an independent cascade model. In the
linear threshold model, each vertex is activated or influenced if the vertex has a number of active
neighbor spreaders greater than or equal to the threshold value of the vertex. Cordasco et al.[5]
studies evangelism in social networks based on the linear threshold model, in which each vertex
has an influence threshold and activation threshold. When a vertex receives information from an
influencethresholdnumberofneighbors,itbecomesinfluenced.Foravertextobecomeactivated,the
vertex should have at least an activation threshold number of activated neighbors. Later, Cordasco
et al.[6] presented a Perfect Awareness (PA) problem on the linear threshold model in which the
influential threshold for each vertex is considered one. The heuristics [8, 15] of the PA problem are
proposed.
The k-center problem [2], PA problem [6], evangelism in social networks [5], graph burning prob-
lem [3], opinion maximization [1], target influence maximization in competitive social networks[12]
under the independent cascade model, and rumor minimization [19] are related problems to the
MINFS problem. The experimental works on the problems PA, graph burning number, and opinion
maximization are proposed in [8, 15, 9, 7, 13, 1, 20].
In the real-life scenario, the information does not flow continuously in the social media net-
works. Over time, the propagation of information or advertisements in social media networks gets
exhausted due to people’s waning interest. So, the distance traversed by the information in social
media networks needs to be addressed. Qiang et al.[16] study the issue in the diffusion process and
introduce a significant constraint as propagation range (information can traverse distance up to the
propagation range from the initial spreaders). Due to the importance of propagation range in real
scenarios, we study the MINFS problem and propose three heuristics for the MINFS problem.
3 Problem Definition
In a given graphG(V, E) and a set S ⊆ V, initially, only the vertices of the setS are influenced
and activated. The variablep ∈ Z+ denotes the propagation range. LetA be the set of activated
vertices initially A = S. Initially, each activated vertexu ∈ S can send the information up top

distance. In the diffusion process, If|NA(v)| ≥α ∗ deg(v) where NA(v) is a set of active neighbors of
v, thenv is added toA with the condition thatv is activated by a smallest subsetS′ ̸= ϕ. Similarly,
if |NA(v)| ≥θ ∗ deg(v), then v becomes influenced. We repeat the above steps until all the vertices
of the setV are influenced. The objective is to find the minimum set of seed nodes ( seed setS of
minimum size).
4 Proposed Algorithms
In this section, we propose three heuristics for the MINFS problem. The approach constitutes two
significant steps. In the first step, the heuristics compute a potential seed set iteratively. In the
second step, the potential seed set is pruned to obtain the smallest seed set.
The tricky part of solving the MINFS problem is to find the smallest seed set S ⊆ V. In
this paper, the heuristic algorithms construct the seed setS with criteria such that the algorithm
influences the set of verticesV through the diffusion process. The diffusion process is implemented
using the Breath First Search approach [16].
4.1 A verage Degree Heuristic
The high-level idea of the proposedGET-POTENTIAL-SEEDS method as given in Algorithm 1 is
as follows. TheGET-POTENTIAL-SEEDS takes input parameters of graphG, propagation rangep,
influence threshold θ, and activation thresholdα. Initially, all the vertices ofG(V, E) are inactive,
so initialize activated setA = ϕ, influenced set I = ϕ, and initial spreader listˆS= [ ]. ˆS contains
the potential seed nodes and is treated as a list since the order in which the nodes are added toˆS is
important for PRUNING step. Repeat the following steps (1 and 2) if a non-influenced node exists
in the graphG.
1. Select a potential list of spreadersL by calling the GET-MOST-INACTIVE-VER TICESmethod
as given in Algorithm 2.
2. For all vertices ofu ∈ L.
(a) Append u to ˆS.
(b) Add u to the activation setA.
(c) DIFFUSION function updates activation setA and influence setI.
As given in Algorithm 2, GET-MOST-INACTIVE-VER TICESmethod returns ⌈ n′′ n′ ⌉ number of
highly influential vertices where n′ is the number of inactive vertices in the graphG, and n′′ is
the sum of the inactive-degree of inactive vertices ( inactive-degreedV \A(v) means the number of
inactive neighbors of v). The number⌈ n′′ n′ ⌉ indicates the average degree of the graphG(V \A, E).
In each iteration (in Algorithm 2, lines 6-10), select a vertexw /∈ L with maximum dV \A(w) value
and append w to L.
We use PRUNING to refine the spreader list ˆS obtained by the above steps (1 and 2). The
PRUNINGmethod, as given in algorithm 3, removes the extra spreaders from the listˆS and returns
the final seed setS. The importance of pruning is illustrated in Figure 1.
The PRUNING method reverses the list ˆS. For each vertexu ∈ ˆS, check whether the diffusion
process can influence all vertices of the graph by spreader listˆS\{u}. If yes, remove the vertexu
from ˆS; otherwise, u must be present in the spreader listˆS. The PRUNING method removes the
extra spreader nodes fromˆS and returns the final seed setS. The PRUNING method gives results

1
0 2
3
4
5
67
8
9
10
11
12
13
1
0 2
3
4
5
67
8
9
10
11
12
13
Fig. 1. The spreader list of nodes(in light red color) isˆS = [5, 1, 4, 9, 8, 10, 6] and influenced vertices
are in white (shown in the left). ThePRUNING removes extra spreader node 5(in red) and returns
[1, 4, 9, 8, 10, 6] because 5 is activated by4, 8, 9, 10 (shown on the right).
based on the order of vertices selected as the initial spreader. So, if we applyPRUNINGon two lists
of equal sizes but with different sequences of spreader lists having the same elements thenPRUNING
may return two reduced lists of different sizes of initial spreaders in both cases. Therefore,PRUNING
performance depends on how we construct the potential spreader listˆS.
4.2 Closest First Heuristic
Suppose dV \A(u) ( wheredV \A(u) is the number of inactive neighbors of the vertexu) anddV \A(v)
are the top two highest values in the graphG(V \A, E), where d(u, v) ≤ 2. Both u and v together
can activate and influence more vertices. As given in Fig. 2, the vertices2 and 5 activate and
influence 4 immediately. Therefore, the next seed vertexw is selected within two hops from theˆS
nodes with a maximumdV \A(w) value.
Initially, the spreader listˆS is empty. Find a vertexw with the most inactive neighbors within
two hops from all vertices inˆS and add w to ˆS. If no inactive vertex exists within two hops from
the nodes in ˆS and the whole graph G(V, E) is not influenced, a vertex with the most inactive
neighbors is added to ˆS. On each addition of a seed vertex to listˆS, the diffusion process diffuses
the information in graphG and updates influenced and activated setsI and A. The process stops
when all vertices are influenced. After finding listˆS, the PRUNINGprocess removes extra spreaders
from the list ˆS and returns the final seed setS.

Algorithm 1: Get potential seed nodes.
Input : Graph G(V, E), propagation rangep, influential and activation thresholds (θ and α).
Output: Potential spreader list ˆS
1 GET-POTENTIAL-SEEDS (G, p, θ, α) begin
2 A ← ϕ
3 I ← ϕ
4 ˆS← [ ]
5 while |I| ̸= |V (G)| do
6 L ← GET-MOST-INACTIVE-VER TICES(G,A)
7 for u ∈ L do
8 append( ˆS, u)
9 A = A ∪ {u}
10 [I, A] ← DIFFUSION (G, u, p, A, α, θ)
11 if |I| = |V (G)| then
12 break
13 return ˆS
1
0 2
3
4
5
67
8
9
10
11
12
13
Fig. 2. The first seed vertex is2 and the second most inactive vertex within two hops is5. We see
here 2 and 5 are activating vertex4.
4.3 Backbone-Based Heuristic
As we saw in the previous algorithm, given in the algorithm 1 where GET-MOST-INACTIVE-
VER TICESmethod returns highly influential list L. We add each vertex of listL one by one to
the spreader list ˆS. Instead of adding all vertices fromL to spreader list ˆS, append-only a vertexu
from list L with the most inactive surrounding vertices. The reason for selecting a vertexu is that
u belongs to a dense sub-graph of inactive vertices.
As given in algorithm 4, theGET-POTENTIAL-NODE-BY-BFS-TREE method finds a tree simul-
taneously from the list of rootsL by assuming the weight on the vertices as the number of inactive
neighbor vertices in the graphG(V \A, E). It returns a rootw ∈ L associated with the heaviest BFS
tree. The vertexw is included in ˆS and A, and theDIFFUSION process marks vertices as activated

Algorithm 2: List of most inactive vertices.
Input : Graph G(V, E) and activated setA.
Output: List of verticesL which have highly inactive neighbors.
1 GET-MOST-INACTIVE-VERTICES (G, A) begin
2 L ← [ ]
3 n′ = |{v : v ∈ V \A}|
4 n′′ = P
u∈V \A
dV \A(u)
// dV \A(u) number of inactive neighbors of u
5 for 1 to ⌈ n′′ n′ ⌉ do
6 w = argmax
v
{dV \A(v) :v ∈ V \L}
7 if w ̸= −1 then
8 append(L, w)
9 return L
Algorithm 3: Final seed setS after pruning the listˆS.
Input : Graph G(V, E), propagation stepp, potential spreader listˆS, influential and activation
thresholds ( θ and α).
Output: Final seed setS.
1 PRUNING (G, p, α, θ, ˆS) begin
2 S ← ϕ
3 ˆS′ ← reverse( ˆS)
4 for u ∈ ˆS′ do
5 S ← ˆS\{u}
6 [A, I] ← DIFFUSION (G, p, α, θ, S)
7 if |I| = |V (G)| then
8 ˆS ← S
9 return S
or influenced. The process stops when all the vertices ofG(V, E) become influenced. ThePRUNING
method removes the extra spreaders from the listˆS and returns the seed setS.
As given in algorithm 5, the inputs for theGET-POTENTIAL-NODE-BY-BFS-TREE method are
G(V, E), A, and L. The method uses the queue data structure to find the heaviest BFS tree. The
initial step is to en-queue each vertexu ∈ L to queueQ and initializeW [v] = 0∀v ∈ V. Do de-queue
u from queue Q. For each unmarked vertexv ∈ N (u)\A, update W [v] by W [v] +W [u], enqueue
v to queue Q, Db[v] =u ( where Db array keeps track of the rootu that discovers the vertexv. )
and mark v as visited. If W [v] > max, then update w by Db[v] and max = W [v]. If Q becomes
empty, stop; otherwise, repeat. In the last step, TheGET-POTENTIAL-NODE-BY-BFS-TREEmethod
returns the vertexw ∈ L associated with the heaviest BFS tree.

Algorithm 4: Get potential seeds by using GET-POTENTIAL-NODE-BY-BFS-TREE
method.
Input : Graph G(V, E), propagation stepp, influential and activation thresholds (θ and α).
Output: Final spreader listS
1 BACKBONE-BASED-SEED-NODES(G, p, θ, α) begin
2 S ← ϕ
3 A ← ϕ
4 I ← ϕ
5 ˆS ← [ ]
6 while I ̸= V (G) do
7 L ← GET-MOST-INACTIVE-VER TICES(G,A)
8 u ← GET-POTENTIAL-NODE-BY-BFS-TREE (G, A, L)
9 append( ˆS, u)
10 A = A ∪ {u}
11 [I, A] ← DIFFUSION (G, u, p, A, α, θ)
12 return S
4.4 BFS and DFS Greedy Heuristics
Qiang et al. proposed two heuristics, BFS-GREEDY and DFS-GREEDY. We also apply thePRUN-
ING technique on the seed set returned by these heuristics to improve the seed set.
5 Result and discussion
We implemented our algorithms on the Ubuntu Operating System, and the hardware specifications
are the processor Intel CoreT Mi7-8700CPU@3.2Ghz and 16GB RAM.
For comparison purposes, we set the parameters used in the algorithms as the propagation
range P = 3and P = diameter(G), the activation thresholdα = 0.6, and the influence threshold
θ = 0.4. The proposed algorithms are compared with recently published efficient algorithms by
Qiang et al.[16]. The sources of datasets are network repository [18], SNAP dataset[11], social
networks [17], and data collected by Newman[14]. The results are shown for propagation range
p = 3 in Figure 3 and Table 2. The results for p=diameter are shown in Figure4 and Table 3.
In the tables, the algorithms from [16] are referred to as DFS-GREEDY (DFS-GD) and BFS-
GREEDY (BFS-GD) while the proposed heuristics DFS-GREEDY-PRUNNING as DFS-PRUN,
BFS-GREEDY-PRUNNING as BFS-PRUN, BACKBONE-BASED as BBH, AVERAGE-DEGREE
as ADH and CLOSEST-FIRST as CFH.
AveragedegreeheuristicandbackboneheuristicsperformwellfordensedatasetslikeKarate[14],
Reed98 [18], musae-squirrel [11], and Web-pol blogs as both the algorithms find spreader vertices
based on the importance of the degree of inactive vertices. Average Degree (ADH) and Closest-
First (CFH) heuristics perform well on dense graphs with a high average clustering coefficient and
a high average degree.BFS-GREEDY-PRUNNING and BACKBONE-BASED heuristics work well on
sparse graphs. The PRUNING works efficiently and effectively if the selected spreaders are in the
neighborhood of each other. OurBACKBONE-BASED algorithm uses Prim’s algorithm to find the
dominated path based on degree, which can activate more vertices. Therefore, all our proposed four
heuristics are improving recent results given by Qiang et al.[16].

Fig. 3. When propagation rangep = 3, comparison of the results between the proposed algorithms
and [16]. Algorithm numbers 1 (DFS-GREEDY [16]) and 2 (BFS-GREEDY [16]) are proposed
by [16], and we are proposing algorithm numbers 3 (DFS-GREEDY-PRUNNING), 4 (BFS-GREEDY-
PRUNNING), 5(BACKBONE-BASED), 6(A VERAGE-DEGREE). The algorithm numbers are denoted
on the X-axis of the bars, and the Y-axis denotes the size of the seed set.

Fig. 4. When propagation rangp = diameter(G), the comparison of the results between the pro-
posed algorithms and [16]. Algorithm numbers 1 (DFS-GREEDY [16]) and 2 (BFS-GREEDY [16])
are proposed by [16], and we are proposing algorithm numbers 3 (DFS-GREEDY-PRUNNING ), 4
(BFS-GREEDY-PRUNNING), 5(BACKBONE-BASED), 6(A VERAGE-DEGREE). The algorithm num-
bers are denoted on the X-axis of the bars, and the Y-axis denotes the size of the seed set.

Algorithm 5: Get potential vertex using BFS-tree.
Input : Graph G(V, E), activation setA and list L.
Output: Highest Influenced Vertexw.
1 GET-POTENTIAL-NODE-BY-BFS-TREE (G, A, L) begin
2 Q ← ϕ
// Q is a Queue
3 A ← ϕ
4 Q.push(u), Db[u] =u, V IS[u] =T rue,∀u ∈ L
// V IS is an array that will keep track of visited vertices.
5 W [u] =deg(u), V IS[u] =F alse,∀u ∈ L
6 max ← −1
7 w ← −1
8 while Q is not empty do
9 u ← Q.dequeue()
10 for v ∈ N (u) do
11 if V IS[v] =F alseand v /∈ A then
12 Db[v] ← Db[u]
13 W [v] ← W [v] +W [u]
14 V IS[v] ← T rue
15 Q.enqueue(v)
16 if max < W[v] then
17 max ← W [v]
18 w ← Db[u]
19 return w
T able 1.Network properties of the data sets [14, 11, 17, 18] used in this paper.
Network Nodes Edges Density A vg-triangles A vg-Degree A vg-CC
power 4941 6594 0.0005 0.3953 2.669 0.08
BlogCatalog 10312 333983 0.0063 1631.6905 64.776 0.463
lastfm 7624 27806 0.001 15.9102 7.294 0.219
tvshow 3892 17262 0.0023 67.13 8.871 0.374
web-polblogs 643 2280 0.011 14.0156 7.092 0.232
CA-HepTh 9877 25998 0.0005 8.6076 5.264 0.471
polblogs 1224 16718 0.0223 247.6544 27.317 0.32
Karate 34 78 0.139 3.9706 4.588 0.571
hamster 1858 12534 0.0073 27.0452 13.492 0.141
musae-crocodile 11631 170918 0.0025 160.8029 29.39 0.336
facebook 4039 88234 0.0108 1197.3335 43.691 0.606
CA-GrQc 5242 14496 0.0011 27.6192 5.531 0.53
Reed98 962 18812 0.0407 302.922 39.11 0.318
musae-squirrel 5201 198493 0.0147 5534.8639 76.329 0.422
government 7057 89455 0.0036 222.6955 25.352 0.411
musae-chameleon 2277 31421 0.0121 451.9974 27.599 0.481
politician 5908 41729 0.0024 88.6757 14.126 0.385
CA-HepPh 12008 118521 0.0016 839.0654 19.74 0.611

T able 2.Comparison of estimated seed set size when the propagation range isp = 3.
Network DFS- GD [16] BFS- GD [16] DFS-PRUN BFS-PRUN BBH ADH CFH
BlogCatalog 631 600 613 493 481 486 484
CA-GrQc 1814 1824 1814 1396 1417 1418 1397
CA-HepPh 3700 3702 3700 2755 2770 2766 2746
CA-HepTh 3014 3031 3014 2411 2428 2428 2409
Karate 7 7 6 6 6 6 6
Reed98 277 262 228 230 238 228 232
facebook 1227 1237 1227 1046 1037 1042 1038
governmen 1581 1594 1581 1295 1290 1287 1288
hamster 326 327 318 286 286 284 284
lastfm 1697 1675 1697 1423 1427 1430 1427
musae-chameleon 349 347 349 302 296 296 300
musae-crocodile 1252 1242 1252 1005 1008 1005 1003
musae-squirrel 767 745 736 595 591 595 602
polblogs 176 175 170 154 155 150 149
politician 1258 1251 1258 1064 1075 1074 1071
power 1735 1735 1439 1439 1438 1435 1475
tvshow 1092 1076 1092 943 957 957 947
web-polblogs 104 108 104 94 94 92 93

T able 3. Comparison of estimated seed set size when the propagation range equals the graph’s
diameter.
Network DFS- GD [16] BFS- GD [16] DFS-PRUN BFS-PRUN BBH ADH CFH
BlogCatalog 254 254 252 252 267 249 252
CA-GrQc 1727 1727 1312 1312 1326 1326 1318
CA-HepPh 3004 3004 2205 2205 2216 2216 2208
CA-HepTh 2731 2731 2095 2095 2109 2109 2100
Karate 7 7 6 6 6 6 6
Reed98 155 155 139 139 133 138 132
facebook 848 848 768 768 768 769 767
governmen 824 824 723 723 729 724 725
hamster 186 186 167 167 165 164 173
lastfm 1143 1143 934 934 953 952 942
musae-chameleon 262 262 246 246 246 244 244
musae-crocodile 814 814 710 710 713 710 704
musae-squirrel 405 405 362 362 364 360 363
polblogs 107 107 98 98 100 97 100
politician 849 849 752 752 751 752 747
power 1711 1711 1421 1421 1419 1419 1450
tvshow 960 960 819 819 822 822 820
web-polblogs 66 66 59 59 61 60 59
6 Conclusion
Due to the importance of social media networks in daily life, this paper studies the influence
maximization problem with propagation range. If a vertex receives the same information sufficient
times from its neighbors, the vertex in the network becomes influenced. Similarly, an influenced
vertex in the network starts spreading information if the vertex receives the same information from
enough neighbors. Indeed, information originating from a source does not flow continuously. So,
the influence model includes the propagation range of information from the originating vertex.
This paper proposes heuristics based on backbone-based heaviest paths and the average degree
of non-activated vertices. The proposed heuristics and the pruning techniques give improved seed
sets compared to existing heuristics. Applying genetic algorithms, particle swarm optimization, and
other metaheuristic techniques to this problem is an interesting future direction.

References
1. Leela Srija Alla and Anjeneya Swami Kare. Opinion maximization in signed social networks
using centrality measures and clustering techniques. InDistributed Computing and Intelligent
Technology: 19th International Conference, ICDCIT 2023, Bhubaneswar, India, January 18–22,
2023, Proceedings, pages 125–140. Springer, 2023.
2. Binay Bhattacharya, Sandip Das, and Subhadeep Ranjan Dev. The weighted k-center problem
in trees for fixed k. Theoretical Computer Science, 906:64–75, 2022. ISSN 0304-3975. doi:
https://doi.org/10.1016/j.tcs.2022.01.005. URL https://www.sciencedirect.com/science/
article/pii/S0304397522000135.
3. Anthony Bonato, Jeannette Janssen, and Elham Roshanbin. How to burn a graph.Internet
Mathematics, 12(1-2):85–100, 2016.
4. Ning Chen. On the approximability of influence in social networks.SIAM Journal on Discrete
Mathematics, 23(3):1400–1415, 2009.
5. Gennaro Cordasco, Luisa Gargano, Adele Anna Rescigno, and Ugo Vaccaro. Evangelism in
social networks: Algorithms and complexity.Networks, 71(4):346–357, 2018.
6. Gennaro Cordasco, Luisa Gargano, and Adele A Rescigno. Active influence spreading in social
networks. Theoretical Computer Science, 764:15–29, 2019.
7. Rahul Kumar Gautam, Anjeneya Swami Kare, and S. Durga Bhavani. Faster heuristics for
graph burning. Applied Intelligence, pages 1–11, 2022.
8. Rahul Kumar Gautam, Anjeneya Swami Kare, and S. Durga Bhavani. Centrality measures
based heuristics for perfect awareness problem in social networks. In Raghava Morusu-
palli, Teja Santosh Dandibhotla, Vani Vathsala Atluri, David Windridge, Pawan Lingras, and
Venkateswara Rao Komati, editors,Multi-disciplinary Trends in Artificial Intelligence, pages
91–100, Cham, 2023. Springer Nature Switzerland.
9. Farzaneh Kazemzadeh, Ali Asghar Safaei, and Mitra Mirzarezaee. Influence maximization in
social networks using effective community detection.Physica A: Statistical Mechanics and its
Applications, 598:127314, 2022.
10. David Kempe, Jon Kleinberg, and Éva Tardos. Maximizing the spread of influence through a so-
cial network. InProceedings of the ninth ACM SIGKDD international conference on Knowledge
discovery and data mining, pages 137–146, 2003.
11. Jure Leskovec and Andrej Krevl. SNAP Datasets: Stanford large network dataset collection.
http://snap.stanford.edu/data, June 2014.
12. Ziwei Liang, Qiang He, Hongwei Du, and Wen Xu. Targeted influence maximization in com-
petitive social networks.Information Sciences, 619:390–405, 2023.
13. Mahdi Nazeri, Ali Mollahosseini, and Iman Izadi. A centrality based genetic algorithm for the
graph burning problem.Available at SSRN 4224314, 2022.
14. Mark Newman. Network data.http://www-personal.umich.edu/~mejn/netdata/, 2015.
15. Felipe de C Pereira, Pedro J de Rezende, and Cid C de Souza. Effective heuristics for the
perfect awareness problem.Procedia Computer Science, 195:489–498, 2021.
16. Zhecheng Qiang, Eduardo L Pasiliao, and Qipeng P Zheng. Target set selection in social
networks with tiered influence and activation thresholds.Journal of combinatorial optimization,
45:117, 2023. doi: https://doi.org/10.1007/s10878-023-01023-8.
17. Zafarani Reza and Liu Huan. Social computing data repository.http://datasets.syr.edu/
pages/datasets.html, 2009.
18. Ryan A. Rossi and Nesreen K. Ahmed. The network data repository with interactive graph
analytics and visualization. InAAAI, 2015. https://networkrepository.com.

19. Ahmad Zareie and Rizos Sakellariou. Rumour spread minimization in social networks: A source-
ignorant approach. Online Social Networks and Media, 29:100206, 2022. ISSN 2468-6964.
doi: https://doi.org/10.1016/j.osnem.2022.100206. URL https://www.sciencedirect.com/
science/article/pii/S2468696422000106.
20. Marek Šimon, Ladislav Huraj, Iveta Luptáková, and Jiří Pospíchal. Heuristics for spreading
alarm throughout a network.Applied Sciences, 9:3269, 2019.
