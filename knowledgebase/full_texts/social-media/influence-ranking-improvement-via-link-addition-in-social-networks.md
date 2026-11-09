---
title: Influence Ranking Improvement via Link Addition in Social Networks
url: https://arxiv.org/abs/2609.36791
category: social-media
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Taiki Ikemoto
- Sho Tsugawa
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.36791
pages: 15
chars: 38600
fetched_at: '2026-11-08T13:12:26+00:00'
kb_version: 1
---

# Influence Ranking Improvement via Link Addition in Social Networks

Influence Ranking Improvement
via Link Addition in Social Networks
Taiki Ikemoto1 and Sho Tsugawa2
1 Graduate School of Science and Technology, University of Tsukuba
1–1–1 Tennodai, Tsukuba, Ibaraki, 305–8573 Japan
t.ikemoto@snlab.cs.tsukuba.ac.jp
2 Institute of Systems and Information Engineering, University of Tsukuba
1–1–1 Tennodai, Tsukuba, Ibaraki, 305–8573 Japan
s-tugawa@cs.tsukuba.ac.jp
Abstract.Social media platforms increasingly rely on influential users
for information dissemination in domains such as marketing and political
campaigns. As the value of being recognized as influential grows, users
mayhaveincentivestostrategicallyenhancetheirinfluence.Inthisstudy,
we investigate whether and to what extent the influence ranking of a tar-
get node can be improved by adding a limited number of outgoing links
in the context of influence maximization (IM). We formulate the Link
Selection Problem for Influence Ranking Improvement (LSP-IRI) as the
problem of selecting a fixed-size set of additional outgoing links from a
target node in order to maximize its rank improvement. To examine this
problem, we consider two representative heuristic strategies: a greedy
method that directly optimizes rank improvement and a computation-
ally efficient random search method. We conduct experiments on four
real-world networks ranging from thousands to hundreds of thousands of
nodes. The results show that even a few added links can substantially
improve IM-based influence rankings. In particular, the greedy method
improves the ranks of nodes initially ranked around 50 by several tens
of positions on average with only three added links, sometimes moving
them into the top 10. The random search method achieves smaller gains
under strict budgets but reduces computation time by up to approxi-
mately 98% compared with the greedy method and becomes effective
when larger budgets are allowed. These findings show that IM-based in-
fluence rankings are sensitive to limited local structural modifications
and highlight a trade-off between ranking improvement and computa-
tional efficiency.
Keywords:Social Networks·Influence Maximization·Influence Rank-
ing Improvement·Link Addition
1 Introduction
The global rise of influencer marketing, which leverages influential users to pro-
mote products and services, has made algorithmic assessments of user influence
arXiv:2609.36791v1  [cs.SI]  29 Sep 2026

2 T. Ikemoto and S. Tsugawa
increasingly consequential. Because influential individuals play a critical role in
shaping consumer awareness and purchasing behavior [1], social media platforms
have evolved into competitive environments where user visibility and influence
translate directly into economic and social capital. As recognition as aninflu-
encerbecomes increasingly associated with professional and social success, users
may have incentives to strategically enhance their perceived influence [2]. This
trendhighlightstheimportanceofinfluence-rankingalgorithms,notonlyastools
for identifying influential users, but also as algorithmic mechanisms whose ro-
bustness must be carefully examined. If small changes in the network structure
can substantially alter influence rankings, then influence-based selection mecha-
nisms may be more vulnerable to strategic behavior than previously understood.
Whileextensiveresearchhasfocusedonidentifyinginfluencersfromaplatform-
centric perspective, relatively little attention has been paid to the perspective
of individual users who seek to be selected as influencers. Among existing ap-
proaches, influence maximization (IM) is one of the most widely studied frame-
works for identifying influential seed nodes [3]. Given a network and a diffusion
model, IM algorithms aim to identify a set of seed nodes that maximizes the
expected influence spread during information propagation. A substantial body
of work has developed efficient and scalable algorithms capable of identifying
such highly influential nodes, even in large-scale networks. Recent studies have
further extended IM to practical settings, including fairness-aware influencer rec-
ommendation and multi-objective influence maximization [4,5]. However, these
studiesprimarilyaddresstheplatform’sobjectiveofmaximizingglobalreachand
typically assume a fixed network structure. In contrast, real social networks are
dynamic, and users can modify their local connectivity through link formation.
Despite its importance, little is known about how susceptible IM-based influence
rankings are to such small structural changes. This gap raises a fundamental re-
search question: how vulnerable are influence rankings to limited link additions,
and to what extent can the ranking of a target node be improved through local
network interventions? Conceptually, this problem differs from conventional IM
because the IM algorithm is treated as a ranking mechanism rather than as an
optimizer of a platform-wide seed set. It also differs from link recommendation
because the objective is not to predict likely links but to select links according
to their effect on the target node’s IM-based rank.
In this paper, to understand the feasibility of influence ranking modification,
we tackle the Link Selection Problem for Influence Ranking Improvement (LSP-
IRI). Given a target user and a fixed link budget, the goal of LSP-IRI is to
select a set of links that maximizes the improvement in the target user’s ranking
under an IM-based influence measure. Figure 1 provides an illustrative overview
of the LSP-IRI. In many IM settings, nodes with more outgoing information-
flow links tend to achieve larger influence spread. Thus, increasing the number
of outgoing information-flow links from the target user to other users, which
corresponds to gaining additional followers, can be viewed as a practically mo-
tivated local intervention for increasing the target user’s influence. By studying
such link additions, we aim not merely to improve a particular user’s ranking,

Influence Ranking Improvement via Link Addition 3
1
23
4
5
6
7
8
9
10
Rank: 8th
Before Link Addition
T arget node
Other nodes
Added links
1
23
4
5
6
7
8
9
10
Rank: 5th
Link Addition Pattern 1
1
23
4
5
6
7
8
9
10
Rank: 1st
Selected
Link Addition Pattern 2
1
23
4
5
6
7
8
9
10
Rank: 3rd
Link Addition Pattern 3
1
23
4
5
6
7
8
9
10
Rank: 7th
...
Link Addition Pattern 4
Fig.1: Illustration of the Link Selection Problem for Influence Ranking Improve-
ment (LSP-IRI). Different link addition patterns lead to different rank improve-
ments for the same target node, and the goal is to select the link set that yields
the largest improvement.
but to assess how susceptible IM-based influence rankings are to limited, local
structural modifications. Despite the simplicity of this objective, the underlying
technical challenges are substantial. First, the search space for link addition is
inherently combinatorial: selecting a limited number of new connections from
a large set of candidates leads to a combinatorial explosion, making exhaustive
search infeasible in large-scale networks. Second, evaluating the impact of each
candidate modification is computationally expensive because exactly computing
the expected influence spread under the IC model is #P-hard [8]. Furthermore,
unlike traditional IM, which optimizes the absolute value of influence spread,
our objective concerns a node’s relative ranking. This requires not only estimat-
ing the target node’s influence but also accounting for how the rankings of all
other nodes may change. These challenges call for efficient heuristics and scal-
able estimation techniques that balance computational efficiency with ranking
accuracy.
To address the LSP-IRI and systematically examine the feasibility of in-
fluence ranking modification, we examine two representative heuristic strategies
withdifferentcomputationalcharacteristics.Thefirstmethodisagreedymethod
that iteratively selects links that maximize rank improvement. This method is
expected to achieve large ranking gains under small link budgets, but it incurs
high computational cost because it repeatedly evaluates candidate links. The
second is a random search method that samples multiple candidate link sets and
selects the best-performing one across several trials. While this method yields

4 T. Ikemoto and S. Tsugawa
comparatively moderate improvements, it significantly reduces computational
overhead and remains scalable when the number of added links is large. These
methods allow us to analyze the trade-off between ranking improvement and
computational efficiency, thereby providing a practical basis for assessing the
susceptibility of IM-based influence rankings under different link budgets and
computational constraints.
The main contributions of this study are summarized as follows:
–We formulate the LSP-IRI, which captures how the influence ranking of a
target node can be changed through limited link additions under the IM
framework. Beyond ranking optimization, this formulation provides a way
to assess the robustness of IM-based influence rankings to small structural
modifications.
–We examine two complementary link selection strategies: a greedy method
that directly optimizes rank improvement and a random search method that
substantially reduces computational cost while maintaining scalability for
larger link budgets.
–We conduct experiments on multiple real-world networks and show that a
small number of added links can substantially improve the ranking of target
nodes. These results demonstrate the susceptibility of IM-based influence
rankings to local structural changes and reveal the trade-off between ranking
gain and computational efficiency.
2 Related Work
Influence maximization has been extensively studied as a framework for selecting
influential seed nodes, with substantial efforts devoted to improving the scala-
bility of influence estimation and seed selection. The IM problem, introduced
by Kempe et al. [3], aims to find a seed set that maximizes expected influ-
ence spread under a diffusion model. Because exact influence computation and
repeated marginal-gain evaluation are computationally expensive, many studies
have developed scalable IM algorithms, including greedy-based acceleration tech-
niques and local-structure-based approximation methods [6–9]. Among scalable
IM approaches, Reverse Influence Sampling (RIS) estimates influence spread
using reverse-reachable (RR) sets rather than repeated forward diffusion simula-
tions [10]. An RR set is generated by sampling a node and tracing the diffusion
process in reverse, and the influence spread of a seed set is estimated from the
fraction of RR sets it covers. In this study, we adopt RR-set-based estimation to
compute IM-based influence rankings on the original graph and on graphs after
link addition.
Recent studies have further extended IM-based techniques to practical in-
fluencer recommendation and optimization settings, but they still primarily ad-
dress the platform-side task of selecting influential users. For example, Dam et
al. [4] studied fairness- and topic-aware influencer recommendation, and Biswas
et al. [5] investigated multi-objective influence maximization under varying-size
solutions and constraints. These studies show that IM-related techniques are

Influence Ranking Improvement via Link Addition 5
increasingly being adapted to practical recommendation and decision-making
settings. However, they mainly focus on how a platform or system should se-
lect influential users under additional objectives or constraints. In contrast, our
work shifts the focus to the target-node perspective and examines how the rela-
tive ranking of a target node can be modified through limited link additions.
Link interventions in social networks have been studied for multiple purposes,
including augmenting influence diffusion, suppressing misinformation, and ma-
nipulating centrality-based node rankings, but their effect on IM-based influence
rankings remains insufficiently understood. Chen et al. [11] studied link addition
for increasing the overall influence spread from given seed nodes, whereas Bayiz
and Topcu [12] considered graph alterations for reducing misinformation diffu-
sion. Waniek et al. [13] examined link addition strategies for manipulating rank-
ings defined by centrality measures such as degree, closeness, and betweenness
centrality. Such centrality-based rankings primarily capture structural promi-
nenceratherthandiffusion-basedinfluence.Takentogether,thesestudiessuggest
thatevenlimitedstructuralinterventionscaninducemeasurablechangesindiffu-
sion outcomes and node rankings. However, existing work has mainly focused on
global diffusion maximization, misinformation suppression, or centrality-based
ranking manipulation. In contrast, our work investigates how limited link addi-
tions affect the relative ranking of a target node under an IM-based influence
measure.
3 Problem Formulation
3.1 Preliminaries
We model a social network as a directed graphG= (V, E), whereVis the
set of nodes representing users andEis the set of directed edges representing
relationships such as following or information flow. Each directed edge(u, v)∈E
indicates that information can propagate from nodeuto nodev, for example,
when nodevfollows nodeuon a social media platform.
To model information diffusion, we adopt the Independent Cascade (IC)
model [3]. Under the IC model, each newly activated node is given a single
chance to activate each of its inactive out-neighbors. For each edge(u, v)∈E,
the activation attempt fromutovsucceeds independently with probability
p(u, v). The diffusion process continues until no further activations are possible.
For a seed setS⊆V, letσ G(S)denote the expected number of activated
nodes inGunder the IC model. The IM problem introduced by Kempe et al. [3]
is formulated as follows:
Problem 1 (Influence Maximization (IM)).Given a directed graphG=
(V, E), a diffusion model, and a seed budgetk, the IM problem is to find a seed
setS⊆Vwith|S|=kthat maximizes the expected influence spread:
S∗ k ∈argmax
S⊆V,|S|=k
σG(S).(1)

6 T. Ikemoto and S. Tsugawa
3.2 Link Selection Problem for Influence Ranking Improvement
(LSP-IRI)
We next formalize the problem of improving the relative influence ranking of a
target node by adding a limited number of outgoing links from the target node.
LetAdenote a given IM algorithm, and letA k(G)denote the seed set of size
kreturned byAon graphG. To quantify the position of a node underA, we
introduce the influence ranking in Definition 1.
Definition 1 (Influence Ranking).Given a graphG, a nodev∈V, and an
IM algorithmA, the influence ranking ofvis defined as
rA(v, G) = min{k∈ {1, . . . ,|V|} |v∈ Ak(G)}.(2)
That is,r A(v, G)is the smallest seed budget at whichvis selected byA.
Given a target nodev, we define the set of candidate outgoing links fromv
as
C(v) ={(v, u)∈ {v} ×V|u̸=v,(v, u)/∈E}.(3)
In other words,C(v)consists of all non-existing outgoing information-flow edges
fromv, excluding self-loops.
For any feasible link setL⊆ C(v), let
GL = (V, E∪L)(4)
denote the graph obtained by adding all links inLtoG. To evaluate the effect of
a feasible link set on the target node’s ranking, we introduce rank improvement
in Definition 2.
Definition 2 (Rank Improvement).Given a graphG, a target nodev, an
IM algorithmA, and a feasible link setL⊆ C(v), the rank improvement ofv
underLis defined as
∆A(v, L;G) =rA(v, G)−rA(v, GL).(5)
A larger value of∆ A(v, L;G)indicates a greater improvement in the relative
influence ranking of the target node.
Using the above definitions, LSP-IRI captures the task of selecting a limited
number of new outgoing links from the target node so as to maximize its rank
improvement under the IM framework. It is formulated as follows:
Problem 2 (Link Selection Problem for Influence Ranking Improve-
ment (LSP-IRI)).Given a directed graphG= (V, E), a target nodev∈V, a
link budgetl, and an IM algorithmA, the LSP-IRI is to find a link setL⊆ C(v)
with|L|=lthat maximizes the rank improvement ofv:
L∗ ∈argmax
L⊆C(v),|L|=l
∆A(v, L;G).(6)

Influence Ranking Improvement via Link Addition 7
4 Link Addition Methods for Influence Ranking
Improvement
Because exactly solving the LSP-IRI requires evaluating a combinatorial number
of feasible link sets, we use RIS-based heuristic methods that approximate rank
improvement with substantially fewer evaluations. Recall that the objective is
to find a link setL⊆ C(v)with|L|=lthat maximizes the rank improvement
∆A(v, L;G)of a target nodev, where the influence ranking is evaluated by a
given IM algorithmA.
In our algorithms, we estimate influence rankings using a RIS-based IM al-
gorithm [10]. More specifically, for each graph instance, we generate RR sets
and use them to efficiently estimate influence spread and compute the seed sets
returned byA. Since an exhaustive search over all feasible link sets is compu-
tationally infeasible, we adopt two heuristic strategies: a greedy method and a
random search method.
Method 1 (Greedy Method).Starting from an empty link setL0 =∅, the
greedy method incrementally adds one link at a time. At stept∈ {1, . . . , l},
letL t−1 denote the set of links selected so far. The next link is chosen so as to
maximize the rank improvement of the target node after the addition:
e∗ t ∈argmax
e∈C(v)\L t−1
∆A(v, Lt−1 ∪ {e};G).(7)
The selected link is then added to the current solution, that is,
Lt ←L t−1 ∪ {e∗ t }.(8)
This procedure is repeated until|L t|=l, and the final output of the greedy
method is denoted by
ˆLGR =L l.(9)
The greedy method locally maximizes rank improvement at each step and is
therefore expected to identify highly effective link additions, especially when the
link budget is small. However, this advantage comes at a substantial computa-
tional cost. At each iteration, the method must evaluate all remaining candidate
links inC(v)\L t−1, and each evaluation requires recomputing the target node’s
influence ranking under the modified graph. LetMv =|C(v)|denote the number
of candidate outgoing links from the target node. Since the method evaluates up
toM v candidate links at each of thelsteps, the total number of rank evaluations
isO(lM v). In the worst case, becauseMv ≤ |V| −1, this isO(l|V|).
Method 2 (Random Search Method).The random search method gener-
ates multiple feasible link sets of sizelby random sampling. Specifically, at each
triali∈ {1, . . . , n}, a candidate link set
L(i) ⊆ C(v),|L (i)|=l,(10)

8 T. Ikemoto and S. Tsugawa
is sampled uniformly at random from all feasible link sets of sizel, and its rank
improvement∆ A(v, L(i);G)is evaluated. Afterntrials, the method selects the
trial with the largest rank improvement:
i∗ ∈argmax
i∈{1,...,n}
∆A(v, L(i);G).(11)
The final output of the random search method is then given by
ˆLRS =L (i∗).(12)
Compared with the greedy method, the random search method substantially
reduces the computational burden because it evaluates onlynsampled link sets,
resulting inO(n)rank evaluations in total. Although this method does not ex-
ploit marginal gains and may therefore miss high-quality solutions, it remains
practical for larger link budgets and large-scale networks, where exhaustive can-
didate evaluation becomes prohibitively expensive.
Overall, the two methods provide complementary approaches for examining
the trade-off between rank-improvement effectiveness and computational effi-
ciency.
5 Experimental Methodology
5.1 Datasets
We use four real-world social networks selected from the datasets used by Chen
et al. [11]. GRQC, NetHEPT, and DBLP are co-authorship networks, while
Epinions is a directed trust network derived from an online consumer review
platform. GRQC represents a co-authorship network in the field of general rela-
tivity and quantum cosmology, NetHEPT represents a co-authorship network in
high-energy physics, and DBLP represents a large-scale co-authorship network
in computer science. For the undirected co-authorship networks, we extract the
largest connected component (LCC), whereas for the directed Epinions network,
we extract the largest weakly connected component (LWCC), to remove isolated
nodes and focus on structurally meaningful regions of the networks. Table 1
summarizes the statistics of the components used in our experiments.
Table 1: Statistics of the datasets after extracting the largest connected compo-
nent for undirected networks and the largest weakly connected component for
the directed network
Network #Nodes #Edges Avg. Degree
GRQC 4,158 13,428 6.46
NetHEPT 8,638 24,827 5.75
Epinions 75,877 508,836 13.41
DBLP 317,080 1,049,866 6.62

Influence Ranking Improvement via Link Addition 9
5.2 Comparison Methods
We compare three link addition methods: the greedy method, the random search
method, and a naive random baseline. The greedy and random search methods
correspond to Method 1 and Method 2, respectively.
The naive random baseline samples a feasible link setL⊆ C(v)with|L|=l
uniformly at random. To mitigate the variance inherent in this stochastic base-
line, we repeat the link sampling and ranking evaluation process 100 times and
report the average performance. The present evaluation compares two basic
search strategies with an unoptimized random reference. The results should be
interpreted as a proof-of-concept evaluation of LSP-IRI rather than as a com-
prehensive comparison with all possible link-selection heuristics.
For all methods, we use 10,000 RR sets to estimate influence spread and com-
pute influence rankings. This RR-set size is chosen as a practical computational
setting, motivated by prior empirical observations that reducing the number of
RR sets can substantially improve efficiency while maintaining reasonable solu-
tion quality [11]. In the random search method, the number of sampled candidate
link sets is set ton= 100.
5.3 Experimental Settings
We adopt the Weighted Cascade (WC) model [3] to instantiate the propagation
probabilities in the IC model. For each directed edge(u, v), where information
propagates fromutov, we setp(u, v) = 1/deg −(v), wheredeg −(v)denotes
the indegree of nodev. This setting reflects the assumption that a node with
many incoming information-flow links is less likely to be activated by any single
in-neighbor, and it has been used in prior IM studies [11]. For undirected co-
authorship networks, we treat each undirected edge as bidirectional and use the
node degree in place of the indegree.
We vary the initial rank of the target node and the number of added links
as experimental parameters. For each dataset, the target nodes are selected ac-
cording to their initial influence rankings. Specifically, we consider nodes initially
ranked 50 and 100, as well as nodes whose initial ranks correspond to the top
5%, 10%, 25%, 50%, and 75% positions in the influence ranking. The number
of added links is set tol∈ {3,10,30}. By evaluating all combinations of these
parameters, we analyze how the link budget and the initial rank of the target
node affect influence ranking improvement.
5.4 Evaluation Metrics
We evaluate the effectiveness of each method using two metrics: rank improve-
ment and rank improvement ratio. The rank improvement∆A(v, L;G)is defined
in Section 3. A larger value of∆A(v, L;G)indicates a greater improvement in the
relative influence ranking of the target node. To compare results across different
initial-rank settings and network sizes, we also use the rank improvement ratio

10 T. Ikemoto and S. Tsugawa
(RIR), which normalizes rank improvement by the maximum possible improve-
ment from the initial rank. For a target node with initial rankrA(v, G)>1, RIR
is defined as
RIRA(v, L;G) =∆A(v, L;G) rA(v, G)−1 .(13)
This metric represents the proportion of the maximum possible upward rank
improvement achieved by link addition. An RIR value close to one indicates
that the target node moves close to the top of the ranking, whereas a value close
to zero indicates limited improvement. A negative RIR value indicates that the
target node’s ranking becomes worse after link addition.
In addition to effectiveness, we evaluate computational efficiency by measur-
ing the single-execution runtime required for link addition and influence-ranking
evaluation for each target node. For the naive random baseline, we conduct 100
independent trials and report the average single-execution runtime over these
trials. This evaluation allows us to analyze the trade-off between ranking im-
provement and computational cost and to characterize the strengths of each
method from both effectiveness and efficiency perspectives.
6 Experimental Results
6.1 Rank Improvement
We present the rank-improvement results using two complementary visualiza-
tions: raw rank-improvement plots for representative cases and RIR bar charts
for the full set of evaluated experimental settings. First, to illustrate the detailed
behavior of the proposed methods, Figure 2 shows the raw rank improvement
∆A(v, L;G)on GRQC for four upper-ranked target nodes, where the horizontal
axis represents the number of added links and the vertical axis represents the
resulting rank improvement. Second, to provide a compact comparison across
networks, link budgets, and initial-rank settings, Figure 3 reports the RIR val-
ues defined in Section 5. Each row corresponds to a dataset, each column corre-
sponds to a link budget, and the bars compare the three link addition methods
across different initial-rank settings. For DBLP, some settings are omitted from
the figure because they were not evaluated. Specifically, the initial-rank settings
corresponding to the top 25%, 50%, and 75% nodes are omitted because many
peripheral nodes have zero estimated influence, making fine-grained ranking be-
yond approximately the 40,000th position unreliable. In addition, the greedy
results forl= 30on DBLP are not reported because all evaluated target nodes
reached rank 1 withl= 10, making further greedy evaluations redundant.
Figure2showsthatthegreedymethodachievesthelargestrankimprovement
in the representative GRQC cases. The random search method provides mod-
erate rank improvement, indicating that sampling-based link selection can still
improve the target node’s ranking. In contrast, the naive random baseline shows
unstableperformanceundersmallandmoderatelinkbudgets,indicatingthatun-
guided link addition does not reliably improve influence ranking. As the number

Influence Ranking Improvement via Link Addition 11
3 10 30
Link budget
0
10
20
30
40
50Rank improvement
A: Greedy
B: Random search
C: Naive
(a) Initial rank: 50th
3 10 30
Link budget
25
0
25
50
75
100Rank improvement
A: Greedy
B: Random search
C: Naive (b) Initial rank: 100th
3 10 30
Link budget
50
0
50
100
150
200Rank improvement
A: Greedy
B: Random search
C: Naive
(c) Initial rank: 207th (top 5%)
3 10 30
Link budget
0
100
200
300
400Rank improvement
A: Greedy
B: Random search
C: Naive (d) Initial rank: 415th (top 10%)
Fig.2: Relation between link budget and rank improvement on GRQC. The
greedy method achieves large improvements even with a small link budget, while
the random search method tends to approach the greedy method as the link
budget increases.
of added links increases, all methods tend to achieve larger improvements, and
the performance gaps between the greedy method and the randomized methods
become smaller in several settings. Figure 3 further shows that these tendencies
are broadly consistent across different networks, link budgets, and initial-rank
settings. However, in larger networks such as Epinions and DBLP, lower-ranked
target nodes do not always achieve substantial rank improvement. This result
suggests that mid- and high-ranked nodes often already have substantially more
connections, and that adding even 30 links may be insufficient for lower-ranked
nodes to close this connectivity gap.
6.2 Computational Efficiency
We evaluate computational efficiency by measuring the average runtime required
to select the link set for each target node. Figure 4 compares the runtime of the
three link addition methods across datasets and link budgets. The vertical axis
is shown on a logarithmic scale to make the large differences among methods
visible. Each panel corresponds to a dataset, and the horizontal axis represents
the link budgetl.
Figure 4 shows that the greedy method requires the longest runtime across
all datasets. Its runtime increases as the link budget grows, because it repeatedly
evaluates candidate links at each step. This tendency becomes more pronounced

12 T. Ikemoto and S. Tsugawa
50th 100th T op
5%
T op
10%
T op
25%
T op
50%
T op
75%
0.00
0.25
0.50
0.75
1.00
GRQC
RIR
l = 3
50th 100th T op
5%
T op
10%
T op
25%
T op
50%
T op
75%
l = 10
50th 100th T op
5%
T op
10%
T op
25%
T op
50%
T op
75%
l = 30
50th 100th T op
5%
T op
10%
T op
25%
T op
50%
T op
75%
0.00
0.25
0.50
0.75
1.00
NetHEPT
RIR
50th 100th T op
5%
T op
10%
T op
25%
T op
50%
T op
75%
50th 100th T op
5%
T op
10%
T op
25%
T op
50%
T op
75%
50th 100th T op
5%
T op
10%
T op
25%
T op
50%
T op
75%
0.00
0.25
0.50
0.75
1.00
Epinions
RIR
50th 100th T op
5%
T op
10%
T op
25%
T op
50%
T op
75%
50th 100th T op
5%
T op
10%
T op
25%
T op
50%
T op
75%
50th 100th T op
5%
T op
10%
T op
25%
T op
50%
T op
75%
0.00
0.25
0.50
0.75
1.00
DBLP
RIR
50th 100th T op
5%
T op
10%
T op
25%
T op
50%
T op
75%
50th 100th T op
5%
T op
10%
T op
25%
T op
50%
T op
75%
Initial rank
Greedy Random search Naive
Fig.3: RIR across networks and link budgets. Each panel corresponds to a com-
bination of a network and a link budget. The horizontal axis represents the
initial-rank setting, and the vertical axis represents RIR. The greedy method
generally achieves the highest RIR, while the random search method becomes
competitive as the link budget increases.
on larger networks, where the number of candidate links and the cost of ranking
evaluation are higher. In contrast, the random search method shows a much
smaller increase in runtime because it evaluates only a fixed number of sampled
link sets. The naive random baseline achieves the lowest runtime, as it does not
perform optimization during link selection. These results show that the random
search method provides a computationally efficient alternative to the greedy
method while still achieving meaningful rank improvement in many settings.
7 Discussion
The experimental results provide two main implications for influence ranking
improvement through link addition.

Influence Ranking Improvement via Link Addition 13
3 10 30
Link budget
101
102
103
Average computation time [s]
GRQC
3 10 30
Link budget
101
102
103
104
Average computation time [s]
NetHEPT
3 10 30
Link budget
102
103
104
105
Average computation time [s]
Epinions
3 10 30
Link budget
100
101
102
103
104
105
106
Average computation time [s]
DBLP
A: Greedy B: Random search C: Naive
Fig.4: Runtime comparison across datasets and link budgets. Each panel corre-
sponds to a dataset, and the vertical axis is plotted on a logarithmic scale. The
greedy method incurs substantially higher runtime, especially for larger link bud-
gets and larger networks, whereas the random search method maintains much
lower computational cost by evaluating a fixed number of sampled link sets.
First, IM-based influence rankings can be substantially altered by a small
number of local link additions. This finding indicates that influence ranking is
not merely a static outcome of the original network structure, but can be sen-
sitive to limited local interventions. From an individual-node perspective, this
suggests that strategically forming a small number of connections can increase
the likelihood of being selected as influential under an IM-based ranking mech-
anism. From the perspective of algorithmic influence assessment, however, the
same result reveals a potential vulnerability: influence rankings may be manipu-
lated through relatively simple structural modifications. Thus, the LSP-IRI for-
mulation provides a useful framework not only for studying rank improvement,
but also for assessing the robustness of influence-based ranking mechanisms.
Second, effective rank-improving links can be identified even under practical
constraints such as limited link budgets and large network sizes. In realistic social
networks, a target user cannot freely acquire a large number of new connections,
and exhaustive search over all candidate links is computationally infeasible. Nev-
ertheless, the greedy method achieves substantial ranking gains under small link
budgets, indicating that carefully selected links can have a strong effect even

14 T. Ikemoto and S. Tsugawa
when only a few additions are allowed. At the same time, the random search
method provides a computationally feasible alternative by evaluating only a
limited number of sampled link sets while still achieving meaningful rank im-
provement in many settings. Although the improvement may remain moderate
when the link budget is small relative to the network scale or when the target
node is initially ranked very low, these results suggest that influence ranking
improvement can be realized under limited link budgets and computational con-
straints.
Several limitations should be considered when interpreting the empirical find-
ings of this study, and they also suggest directions for future work.
First, the experiments were conducted on a limited number of real-world net-
works that are still smaller than very large online social platforms. Future work
should evaluate the proposed framework on larger and more diverse networks to
further examine its generalizability and scalability.
Second, this study does not provide theoretical guarantees for the proposed
methods. Theoretical analysis is needed to clarify when substantial rank im-
provement can be expected and to characterize the behavior of the methods
beyond empirical observations.
Third, the experiments are based on the IC model with the WC setting.
Future studies should examine whether the findings remain robust under al-
ternative diffusion models and propagation probabilities estimated from real
behavioral data.
Fourth, our evaluation is limited to two heuristic strategies and a naive ran-
dom baseline. Since existing link-intervention methods optimize different objec-
tives, the results should be viewed as a proof of concept for LSP-IRI rather than
a comprehensive benchmark.
Finally, the current formulation assumes that each candidate link has the
same cost and can be added if selected. Incorporating heterogeneous link costs,
link-formation feasibility, and acceptance probabilities would make the problem
setting more applicable to practical scenarios.
8 Conclusion
This paper formulated the LSP-IRI, which captures how the influence ranking
of a target node can be modified through limited link additions under the IM
framework. To address the LSP-IRI, we examined two complementary link se-
lection strategies: a greedy method that directly optimizes rank improvement
and a random search method that reduces computational cost. Experiments on
multiple real-world networks showed that a small number of added links can
substantially improve the ranking of target nodes, demonstrating that IM-based
influence rankings can be susceptible to local structural changes. Overall, the
LSP-IRI provides a framework for analyzing the extent to which IM-based in-
fluence rankings can be modified through limited local link additions.
Acknowledgments.This work was partly supported by JSPS KAKENHI Grant No.
JP25K03105 and JST ERATO Grant No. JPMJER2502.

Influence Ranking Improvement via Link Addition 15
Disclosure of Interests.The authors have no competing interests to declare that
are relevant to the content of this article.
References
1. Barari, M., Eisend, M., Jain, S.P.: A meta-analysis of the effectiveness of social me-
dia influencers: Mechanisms and moderation. Journal of the Academy of Marketing
Science54, 28–48 (2026).
2. Fetter, S., Coyne, P., Monk, S., Woodruff, S.J.: An exploration of social media
users’ desires to become social media influencers. Media Watch14(2), 200–216
(2023).
3. Kempe, D., Kleinberg, J., Tardos, É.: Maximizing the spread of influence through a
social network. In: Proceedings of the 9th ACM SIGKDD International Conference
on Knowledge Discovery and Data Mining, pp. 137–146 (2003).
4. Dam, A., Pathak, S., Mitra, B.: Fair2Vec: Learning Fair and Topic-Aware Repre-
sentations for Influencer Recommendation. In: An, A., Cuzzocrea, A., Hu, H. (eds.)
Social Networks Analysis and Mining. ASONAM 2025. Lecture Notes in Computer
Science, vol. 16323, pp. 346–362. Springer, Cham (2026).
5. Biswas, T.K., Abbasi, A., Chakrabortty, R.K.: Multi-objective influence maxi-
mization under varying-size solutions and constraints. In: Proceedings of the 2022
IEEE/ACM International Conference on Advances in Social Networks Analysis
and Mining (ASONAM), pp. 285–292 (2022).
6. Leskovec, J., Krause, A., Guestrin, C., Faloutsos, C., VanBriesen, J., Glance, N.:
Cost-effective outbreak detection in networks. In: Proceedings of the 13th ACM
SIGKDD International Conference on Knowledge Discovery and Data Mining, pp.
420–429 (2007).
7. Goyal, A., Lu, W., Lakshmanan, L.V.S.:CELF++: Optimizing the greedy algo-
rithm for influence maximization in social networks. In: Proceedings of the 20th
International Conference Companion on World Wide Web, pp. 47–48 (2011).
8. Chen, W., Wang, C., Wang, Y.: Scalable influence maximization for prevalent
viral marketing in large-scale social networks. In: Proceedings of the 16th ACM
SIGKDD International Conference on Knowledge Discovery and Data Mining, pp.
1029–1038 (2010).
9. Chen, W., Yuan, Y., Zhang, L.: Scalable influence maximization in social networks
under the linear threshold model. In: Proceedings of the 10th IEEE International
Conference on Data Mining, pp. 88–97 (2010).
10. Borgs, C., Brautbar, M., Chayes, J., Lucier, B.: Maximizing social influence in
nearly optimal time. In: Proceedings of the Twenty-Fifth Annual ACM-SIAM Sym-
posium on Discrete Algorithms, pp. 946–957 (2014).
11. Chen, X., Song, Y., Tang, J.: Link recommendation to augment influence diffusion
with provable guarantees. In: Proceedings of the ACM Web Conference 2024, pp.
2509–2518 (2024).
12. Bayiz, Y.E., Topcu, U.: Countering misinformation on social networks using graph
alterations. arXiv preprint arXiv:2211.04617 (2022).
13. Waniek, M., Michalak, T.P., Wooldridge, M.J., Rahwan, T.: How members of
covert networks conceal the identities of their leaders. ACM Transactions on Intel-
ligent Systems and Technology13(1), Article 12, 29 pages (2021).
