---
title: How neighbourhood ideology shapes misinformation belief in densely tied social networks
url: https://arxiv.org/abs/2609.10277
category: social-media
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Soroush Karimi
- Marcos Oliveira
- Diogo Pacheco
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.10277
pages: 18
chars: 35043
fetched_at: '2026-11-08T13:13:06+00:00'
kb_version: 1
---

# How neighbourhood ideology shapes misinformation belief in densely tied social networks

How neighbourhood ideology shapes misinformation
belief in densely tied social networks
Soroush Karimi,1∗ Marcos Oliveira,1,2 and Diogo Pacheco1
1Department of Computer Science, University of Exeter, UK
2Vrije Universiteit Amsterdam, Amsterdam, Netherlands
∗sk931@exeter.ac.uk
Abstract.With the rapid spread of news on social media, understanding the prop-
agation of misinformation is becoming increasingly important. One factor that af-
fects individuals’ vulnerability to false information is their ideological predisposi-
tion. Despite the large number of agent-based models that focus on social influence
as a driver of the spread of false claims, they often fail to explicitly integrate per-
sonal ideological biases into belief formation. In this work, we explore how misin-
formation spreads through the interaction between individuals’ ideological biases
and social influence. Our model accounts for both the strength of individuals’ ide-
ological biases and the extent to which a false claim aligns with their ideology. So-
cial influence modifies the effects of ideological intensity and false claim alignment
through network interactions. Notably, the influence of neighbours’ ideological in-
tensity on belief is strongly affected by how well those neighbours are connected
to one another. These results highlight the importance of considering both network
structure and personal ideological biases when modelling misinformation propaga-
tion.
Introduction
The mechanism of belief formation and information sharing is a social activity (1), while per-
sonal biases play a key role in the way we process information (2). The impact of ideology
and social influence has traditionally been decoupled in simulation models, and emerging uni-
fied frameworks have begun to integrate individual bias with network exposure (3). However,
current models that combine the effects of social influence and personal bias lack an explicit
1
arXiv:2609.10277v1  [cs.SI]  9 Sep 2026

mechanism that includes a range of bias toward an ideology and belief formation toward false
claims from opposite to aligned.
Social media platforms provide an environment where individuals with varying levels of
ideological intensity encounter false claims that differ in their ideological alignment. They now
serve as news sources (4) and may increase the spread of unreliable information (5) and toxic
content (6). Individuals receive content primarily from their social connections, and such expo-
sure has a considerable impact on belief formation (7,8). However, network and social influence
alone do not explain all individual differences in what individuals believe and share (9).
One factor contributing to differences in belief and sharing is partisan or ideological bias
(i.e., motivated reasoning) (10). Experimental evidence shows that people systematically trust
information more when it aligns with their political identity (11). Ideological thinking is not
restricted to political attitudes but is a broader domain-general cognitive style that varies along
a spectrum from moderation to extremism (12). Together, these findings suggest that models of
misinformation diffusion should account for variation in individuals’ ideological intensity.
Simulation models, such as agent-based and epidemic contagion models, have been used to
analyse the spread of misinformation (13), as they can capture social influence through feed-
back loops that reinforce acceptance of a false claim (10). More recently, frameworks have
been developed that incorporate ideology into these contagion dynamics to better capture belief
formation. For instance, Stein et al. (14) demonstrated that, in ideologically segregated net-
works, the prevalence of misinformation is higher in both experimental results and simulations,
underscoring the joint importance of individual ideology and network topology. To capture the
interaction aspect, Brooks et al. (15) examined how media accounts with fixed ideological po-
sitions shape the spread of online content, modelling ordinary users who adopt ideologies and
share content strictly within a designated “ideology band”. Similarly, tracking multi-topic dy-
namics, Rodriguez et al. (16) combined psychological and social factors into a single framework
to observe how public opinion transitions across multiple topics change. Their model explains
how macro-level social phenomena, such as societal upheavals and the entrenchment of fringe
groups, emerge from the interaction of cognitive and social forces. Moreover, in confirmation-
bias models (17), an agent’s opinion and the information they encounter are treated as identical,
thereby explaining how multiple beliefs can coexist. More explicit models have begun to de-
velop to capture how bias shapes single-topic diffusion in the presence of cognitive forces. For
example, Sikder et al. (3) introduced a social learning model in which a fixed parameter deter-
2

mines an agent’s probability of rejecting incongruent information. However, these frameworks
fail to account for the interplay among social influence, individual ideological bias, and the
ideological alignment of a specific false claim. Moreover, existing models lack a mechanism
for representing how individuals with different levels of ideological intensity respond to false
claims based on the claims’ ideological alignment with their worldview.
In this work, we address the gap by explicitly focusing on belief formation about a false
claim, integrating individual biases and social impact to determine whether individuals believe
it. Unlike confirmation-bias models, by distinguishing between personal biases and the claim’s
ideological alignment, we can capture how behaviours differ based on the claim’s ideological
leaning. The distinction allows the model to describe the spread of misinformation. We show
how network structure shapes belief dynamics and how the distribution of extremists alters
social impact. We find that the effect of social influence is most pronounced in networks with
dense communities. It implies that, beyond personal biases and the people we interact with,
the structure of the community we belong to may increase our vulnerability to believing and
sharing misinformation.
The Ideological Misinformation Contagion Model
We introduce a contagion model that integrates individual ideological predisposition with social
influence as joint drivers of misinformation propagation. Susceptibility to misinformation is
affected by ideological congruence, as individuals tend to be more receptive to information
that aligns with their existing beliefs and more sceptical of counter-attitudinal content (18, 19).
Psychological research indicates that the strength of ideological commitment differs among
individuals (12). We capture this variation by assigning each individual an ideological intensity
score, which indicates the extent to which their prior ideological beliefs shape their reaction to
information.
Belief formation can also be reinforced through social interactions, since exposure to like-
minded peers can strengthen existing biases and promote the diffusion of misinformation (18).
We use the SBFC model (20) as the basis for our framework because it represents misinfor-
mation propagation through social interactions. We extend this framework by distinguishing
an individual’s ideological intensity from the ideological alignment of the false claim, and by
incorporating their interaction into the transition dynamics. This allows the same individual to
3

respond differently to different false claims according to how strongly each claim aligns with
their ideology, while social interactions determine how these individual-level predispositions
propagate through the network.
In broad terms, the model describes the propagation and rejection of a single false claim
over a social network (hereafter, we refer to a ‘false claim’ simply as a ‘claim’). Individuals can
transition between susceptible, believer, and fact-checker states as a result of local social influ-
ence and the ideological relationship between the individual and the claim. This formulation
allows the same individual to respond differently to different claims depending on their ideo-
logical alignment, while also allowing neighbouring agents to influence the individual’s belief
dynamics. For more details on the model, agent states and transitioning among them, see the
Method Section.
Results
The proposed model suggests that individual ideology and social influence jointly influence
misinformation propagation. The simulation results further show that, in addition to an indi-
vidual’s ideological intensity, the influence of neighbours becomes increasingly important in
highly clustered networks. We begin by examining the impact of ideological alignment of a
claim on the overall percentage of believers. Then, we investigate belief formation at the node
level to show how individuals respond differently to claims with different levels of ideological
alignment. Lastly, we quantify the relative contributions of personal ideology and neighbours’
ideological intensity across different network structures.
Greater Ideological Alignment Leads to More Believers
To examine how the ideological alignment of a claim influences its spread, we compare how
likely individuals are to believe it. We evaluate the percentage of believers across a continu-
ous range of claim alignment, from completely opposite (A factor =−1) to completely aligned
(Afactor = 1), using an Erd˝os–R´enyi random network (see Methods).
We find that when the claim is neutral with respect to individuals’ ideology (A factor = 0),
individuals’ ideological intensity does not affect the percentage of believers. When the claim is
ideologically aligned with the individual (A factor >0), individuals are more likely to believe a
claim, and the percentage of believers increases with ideological intensity (see Fig. 1). By con-
4

trast, for opposing claims (A factor <0), the percentage of believers decreases with ideological
intensity. We complement the simulation results with a numerical solution of the Markov chain
and an analytical treatment that formally characterises the steady-state belief dynamics. Both
approaches closely match the simulation results.
0.8
 0.4
 0.0 0.4 0.8
AFactor
0
20
40
60Percentage of Believers
Ideological Intensity
I=0.75
I=0.5
I=0.25
No Ideology (I=0)
Numerical Result
Fig. 1.When the ideological intensity level is greater than zero, the percentage of believers increases with claim
alignment. The ideological alignment factor indicates how closely the claim aligns with a specific ideology (e.g.,
right-wing). The simulation results align well with the numerical solution.
To understand how individual ideological strength and claim alignment influence belief,
we examine how these effects vary with individuals’ baseline vulnerability to claims, which
we refer to as gullibility. In the low-gullibility case (α= 0.05), few moderate individuals
believe the claim, and greater ideological intensity is required for them to become believers. At
higher gullibility levels, a fraction of moderate individuals become believers even at low levels
of ideological intensity, reflecting their greater baseline gullibility (Fig. 2). By comparing the
panels at low ideological intensities, we observe that increasingαincreases the probability that
moderate individuals become believers.
Individual Belief Responses Vary with Claim Ideological Alignment
To investigate how ideology and social influence affect individuals’ beliefs about a claim, we
examine each node separately. We conduct a node-level analysis by measuring the proportion
of simulation runs that terminate in the believer state. We define this measurement as the belief
5

-1.0 -0.6 -0.2 0.2 0.6 1.0
Ifactor
Iintensity
= 0.05
0.08
0.16
0.24
0.32
0.40
0.48
0.56 0.64
-1.0 -0.6 -0.2 0.2 0.6 1.0
Ifactor
= 0.1
0.08
0.16
0.24
0.32
0.40
0.48
0.56
0.64
0.72
-1.0 -0.6 -0.2 0.2 0.6 1.0
Ifactor
= 0.15
0.08
0.16
0.24
0.32
0.40
0.48
0.56
0.64
0.72
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
Fig. 2.The fraction of believers as a function of ideological alignment factor (x-axis) and ideological intensity
(y-axis).
probability and capture individuals’ behaviour towards the claim. In this context, individuals
are classified as either moderates, lacking strong ideological biases, or extremists, who possess
high ideological intensity. Most extremists are grouped within a single cluster.
We compare the belief probability for three types of claims: opposing, neutral, and aligned
with the nodes’ ideology. We find that when the claim opposes the nodes’ ideology, extremists
predominantly become fact-checkers, resulting in low belief probabilities. For neutral claims,
ideological intensity has little effect, and moderates and extremists behave similarly. In contrast,
when the claim aligns with the nodes’ ideology, extremists are more likely to become believers.
Additionally, as moderates are connected to extremist neighbours, their belief probabilities also
increase (see Fig. 3). In the next subsection, we investigate how this neighbourhood effect varies
across different strategies for distributing extremists within the networks.
Network Clustering Amplifies the Influence of Neighbourhood Ideology
To understand how network structure affects social influence, we examine belief dynamics
across four different network topologies and three strategies for placing extremists. Since an
individual’s state transitions are shaped by their neighbours, the positioning of extremists alters
the ideological makeup of local communities. For each scenario, we define the belief proba-
bility as the proportion of simulation runs in which a node ends up in the believer state. We
then explore how this probability is influenced by the node’s own ideological strength and the
average ideological intensity of its neighbours.
We sample ideological intensities uniformly (I intensity ∈[0,1]) and classify the top 30 per
6

Fig. 3.Different claims, different acceptance rates: At the top, we see the distribution of extremists, which are
mostly clustered. In the second row, there are belief percentages for each node for cases where the claim is against,
neutral toward, or aligned with the node’s ideology.
cent as extremists. Extremists are distributed using three topological strategies: uniformly at
random, preferentially on high-degree hubs, and via breadth-first search (BFS) to form tight
local clusters (see Methods). We evaluate belief formation under a claim that is strongly aligned
with individuals’ ideology (Afactor = 0.8).
We observe that the influence of neighbours becomes much more significant in networks
where neighbouring nodes are highly interconnected, as indicated by higher clustering coeffi-
cients (Table 1). Networks like Facebook (average clustering coefficient of 0.606) exemplify
strong clustering, which is closely matched by the Watts–Strogatz (WS) model (0.537), whereas
models like Barab ´asi–Albert (BA) and Erd ˝os–R´enyi (ER) have much lower values (0.037 and
0.011, respectively). Although Facebook and WS differ in degree distribution and community
structure, both show a noticeable increase in the standardised regression coefficient for neigh-
bours’ ideological strength (Fig. 4).
7

StructureNEdges Avg. Degree (⟨k⟩) Avg. Clustering Coeff.
FB (empirical) 4039 88,234 43.7 0.606
WS 4039 88,858 44.0 0.537
BA 4039 88,374 43.8 0.037
ER 4039 88,234 43.7 0.011
Table 1.Node count, edge count, average degree, and average local clustering coefficient for each network struc-
ture used in the node-level comparison. WS, BA, and ER were generated to match FB’s node count and mean
degree (see Networks section).
We find that in highly clustered networks, local peer pressure can match personal ideolog-
ical bias in driving misinformation adoption. While personal ideological intensity is explicitly
encoded in the transition probabilities, neighbourhood ideological intensity is not; this ampli-
fication emerges naturally from repeated local interactions constrained by network topology.
Whereas network density has previously been shown to increase belief via baseline gullibility
(α) (21), our result reveals how dense local communities specifically amplify the influence of
neighbouring agents’ ideologies. Finally, as general gullibility (α) increases, individuals are
generally more likely to become believers, while the relative effects of personal ideology and
neighbours’ ideological intensity are reduced.
Conclusion
In this work, we introduce a contagion model that integrates individuals’ ideological intensity
with a claim’s ideological alignment. While previous frameworks failed to account for this
interaction alongside social influence, we show that dense network clustering endogenously
amplifies the influence of neighbouring ideology, driving misinformation adoption beyond indi-
vidual predispositions alone. Including individual biases provides a more plausible view of how
misinformation spreads across the network. The model was implemented in various network
structures to examine the impact of ideology alignment and individual biases. The simulations
show that when individuals are unbiased, they behave similarly towards the claim, regardless
of how aligned it is with their ideology. Claims that go against extremist values are debunked,
and claims aligned with their ideology are believed. Furthermore, simulation results indicate
that even small populations of highly ideological agents can significantly increase the adoption
of misinformation among neighbouring moderates, especially within clustered network struc-
8

0.00
0.01
0.02
0.03
0.04Standardized Coefficient
= 0.05
 = 0.1
 = 0.15
0.00
0.01
0.02
0.03
0.04Standardized Coefficient
0.00
0.01
0.02
0.03
0.04Standardized Coefficient
Random Degree BFS
0.00
0.01
0.02
0.03
0.04Standardized Coefficient
Random Degree BFS Random Degree BFS
FBWSBAER
Personal Intensity Ave. of Neighbours' Intensity
Fig. 4.The impact of personal and neighbourhood ideology on belief probability using standardised regression co-
efficients. Personal intensity has a robust impact across different network structures and decreases with increasing
general gullibility. The role of neighbours’ intensity is greater in network structures with high clustering coeffi-
cients (e.g., Facebook and Watts-Strogatz).
tures. This amplification is not directly encoded in the transition rules; rather, it arises from the
interaction between ideological alignment and network topology. Here, we considered a single
dimension of ideology and its alignment; in future work, there is room to study cases where
individuals have multi-dimensional ideologies and claims with different alignment factors for
each dimension.
9

Ideological Intensity Ideological Alignment Factor
-1
(Opposite)
0 1
(Neutral) (Aligned)10
Fig. 5.Ideological intensity is an individual attribute that quantifies the strength of an individual’s ideological
commitment (0-1). Meanwhile, the ideological alignment factor (Afactor) is an attribute of a claim that indicates its
position on the ideological spectrum, ranging from−1(completely opposite) to1(fully aligned), with0represent-
ing neutral content toward that specific ideology.
Methods
Model
In our model, agent occupies one of three discrete states regarding the misinformation item: a
susceptible agent (S) is not aware of the item, a believer (B) thinks it is true, and a fact-checker
(F) is aware that it is a claim and debunks it. To build the connection structure of the agents, we
use a static, undirected social networkG= (V, E), where the nodesi∈Vrepresent individuals
and the edgesErepresent social ties. We definen B i (t)andn F i (t)as the numbers of neighbours
of individualiwho are believers and fact-checkers, respectively, at timet.
We include ideological mechanisms whereby individuals are more likely to accept misinfor-
mation aligned with their worldview and reject content that conflicts with it. For each nodei, the
ideological intensityI i ∈[0,1]specifies the strength ofi’s commitment. The ideological align-
ment of the claim is represented byA factor ∈[−1,1]. A value ofA factor =−1represents content
that is completely opposed to the relevant ideology,A factor = 0represents ideologically neutral
content, andA factor = 1denotes content that is fully aligned with it. Thus,I i is an individual-
level attribute, whileA factor is a property of the misinformation (Fig.5). By this distinction, the
same individual responds differently to claims with different ideological alignments.
A positive value ofA factorIi indicates ideological alignment, a negative value indicates ideo-
logical mismatch, and a value close to zero indicates that ideological considerations have little
influence on the individual’s response. In the multidimensional case, this scalar product can be
extended to a dot product between an individual’s ideological-intensity vector and the claim’s
alignment vector. In addition to ideological motivation for either believing or debunking a
claim, there is a certain level of vulnerability to believing the claim, which is determined by
10

α∈[0,1]. We define
Li = α+A factorIi
2
which combines the baseline vulnerability with ideological motivation. The spreading rate is
determined byβ∈[0,1]. The probability that a susceptible individual becomes a believer is
equal to:
fi(t) =β nB i (t)(1 +Li) nB i (t)(1 +Li) +nF i (t)(1−L i) ,(1)
The corresponding probability of transitioning from susceptible to fact-checker is:
gi(t) =β nF i (t)(1−L i) nB i (t)(1 +Li) +nF i (t)(1−L i) .(2)
When the claim is aligned with an individual’s ideology (A factor >0), greater ideological
intensity increases their relative susceptibility to believer influence. Conversely, when opposed
(Afactor <0), greater ideological intensity decreasesL i and increases the relative weight placed
on fact-checker influence. For ideologically neutral content (A factor = 0), there is no differ-
ence between nodes with different ideological intensities, which reduces the framework to the
baseline SBFC misinformation model (20).
Fig. 6.Transition diagram
In this model, individuals may change their state after initially adopting or rejecting the
claim with fixed probabilities. A believer can verify the information and become a fact-checker
with probabilityp verify, halting the spread of the claim and contributing to debunking. Both
believers and fact-checkers can also forget their current position towards the claim and return
11

to the susceptible state with probabilityp forget (Fig.6). In this way, the model permits exposure
to the claim and transitions between states.
Simulation
We performed simulations on static, undirected networks across discrete time steps. Each node
could occupy one of three states: susceptible (S), believer (B), or fact-checker (F). We ini-
tialised node states with 98% susceptible, 1% believer, and 1% fact-checker.
At each discrete time step, transition probabilities were determined based on the transition
rates shown in Fig. 6. We set the model parameters toβ= 0.5,α= 0.1,p verif y = 0.01and
pf orget= 0.1. We selected the parameters in the range that avoids trivial absorbing states (e.g.,
complete elimination of believers) so that the influence of ideology and social interactions on
belief formation can be analysed. Each simulation was run for 500 time steps, which exceeded
the number of steps required to reach a steady state.
To investigate the influence of ideological alignment, the alignment factor was varied from
−1to1, while ideological intensity took the values0,0.25,0.5, and0.75. For each parameter
combination, ran 50 trials. The reported percentage of believers is the mean, and the uncertainty
is given as the 95% confidence interval.
Markov Representation
In addition to agent-based simulations, we provide complementary numerical and analytical
solutions (see the appendix) to validate our simulation findings and formally characterise the
steady-state belief dynamics. Based on this model, in which the current state of each individual
is determined solely by its previous state, we constructed a Markov chain in which the tran-
sition rates from the susceptible state to the believer and susceptible-to-fact-checker states are
functions of the probabilities of being in different states. Eq. (3) shows the transition matrix and
how the probability of being in each state updates.


P S(t+ 1)
P F (t+ 1)
P B(t+ 1)

 =


1−f i(t)−g i(t)p forget pforget
gi(t) 1−p forget pverify
fi(t) 0 1−p forget −p verify




P S(t)
P F (t)
P B(t)

 (3)
12

Statistical Analysis
At the node level, we calculated the belief probability as the proportion of simulation runs in
which the node ended in the believer state. We used ordinary least squares (OLS) regression
models to quantify the relative contributions of a node’s ideological intensity and the mean ide-
ological intensity of its neighbours to belief probability. To compare the regression coefficients
directly, we standardised the predictor variables (z-scores) before fitting the model. We ob-
tained confidence intervals for the regression coefficients from the fitted models. We repeated
the procedure for different network structures and three extremist placement strategies at fixed
Afactor = 0.8and across three values ofα(0.05,0.1,0.15).
Networks
For the baseline simulations (Fig. 1), we generated Erd˝os-R´enyi (ER) networks withN= 1000
nodes and edge probabilityp= 0.04(average degree⟨k⟩ ≈40). For the empirical network
analysis, we used a network sample structure from Facebook (22) comprisingN= 4039nodes
with an average degree of⟨k⟩ ≈43.7. For the comparative node-level analysis, we used the
NetworkXPython package to generate synthetic network structures, including Erd ˝os-R´enyi
(ER), Watts-Strogatz (WS), and Barab ´asi-Albert (BA) models, preserving a closely matched
number of nodes (N= 4039) and mean degree as the empirical Facebook network.
Ideological Intensity and Extremist Definitions
To analyse the impact of individual bias on misinformation dynamics, we consider three con-
figurations of ideological intensity (Iintensity), as shown in Fig. 7:
1.Homogeneous Baseline:To examine the general effect of ideology in terms of believing
a claim, we assume the same ideological intensity for all individuals (Fig. 7A). This
reveals the relationship between a claim’s ideological alignment (A factor) and the global
spread of misinformation.
2.Binary Case:For demonstration purposes, we utilise a binary distribution in which nodes
are strictly assigned to either a ”moderate” or an ”extremist” intensity value. This simpli-
fies the observation of how extreme bias affects individual state transitions (Fig. 7B).
13

3.Continuous Heterogeneous Distribution:For node-level analysis, ideological intensity
values are selected from a uniform distribution in the interval[0,1]. We defineextremists
as the 30% of the population with the highest intensity values (at or above the 70th per-
centile), while the remaining 70% are moderates (Fig. 7C). It is approximately equivalent
to assigning ideological intensity values greater than 0.7 to extremists and the remaining
values to moderates.
In the heterogeneous scenario, a single set of values is sampled from this distribution for the
entire population and ranked; the top 30% form the extremist pool and the remainder form the
moderate pool. The values within these pools are shuffled before being assigned to nodes. Thus,
the extremists are always more intense than the moderates, but the exact value does not depend
on the network position, unless a specific placement strategy (e.g. degree-based or BFS-based
placement) is adopted.
Extremist Extremist
X-axis: Ideological intensity
A B C
Fig. 7.Ideological intensity choices. A) There is a single value for all the nodes. B) The binary case, when we
have two intensity values, one for moderates and one for extremists. C) Ideological intensity forms a uniform
distribution, in which the extremists are the nodes with the 30 per cent highest ideological intensity values.
Extremist Placement Strategies
Once the extremist nodes are defined, they are seeded into the network according to three dis-
tinct topological strategies (Fig. 8).
1.Random Placement:Extremist nodes are selected uniformly at random from the set of
all nodes.
2.Degree-Based Placement:Nodes are ranked by degree centrality, and theN ext nodes
with the most connections are designated as extremists. This strategy simulates a scenario
in which ”hubs” or influential individuals are the primary drivers of the ideology.
3.Localized (BFS) Placement:To simulate ideological clusters or ”echo chambers,” we
employ a Breadth-First Search (BFS) approach. A seed node is selected at random and
14

assigned as an extremist, followed by its immediate neighbours (depth-1). If the required
count of extremists is not met, a new random seed is chosen, and the process repeats until
30% of the population is seeded.
1
Breadth-First Search (BFS)
A seed node is picked, here
node 1, followed by its
immediate neighbourhood.
Random Placement
Nodes are selected uniformly
at random.
Degree Centrality
Nodes are selected based on
their number of connections.
Fig. 8.Extremist agents are seeded into the network according to three distinct topological strategies: Random
Placement, Degree Centrality, and Localised (BFS) Search.
References
1. Chung, N., Nam, K. & Koo, C. Examining information sharing in social networking com-
munities: Applying theories of social capital and attachment.Telematics and Informatics
33, 77–91 (2016).
2. Van Bavel, J. J. & Pereira, A. The partisan brain: An identity-based model of political
belief.Trends in cognitive sciences22, 213–224 (2018).
3. Sikder, O., Smith, R. E., Vivo, P. & Livan, G. A minimalistic model of bias, polarization
and misinformation in social networks.Scientific reports10, 5493 (2020).
4. Fletcher, R.et al.The link between changing news use and trust: longitudinal analysis of
46 countries.Journal of Communication75, 1–15 (2025).
5. Allcott, H. & Gentzkow, M. Social media and fake news in the 2016 election.Journal of
economic perspectives31, 211–236 (2017).
6. Chetty, N. & Alathur, S. Hate speech review in the context of online social networks.
Aggression and violent behavior40, 108–118 (2018).
15

7. Pennycook, G. & Rand, D. G. The psychology of fake news.Trends in cognitive sciences
25, 388–402 (2021).
8. Puthineedi, V . & Jha, A. K. Where the ball starts rolling? an empirical investigation into
initial opinion formation on social media platforms.Information Systems Research(2026).
9. Buchanan, T. Why do people spread false information online? the effects of message and
viewer characteristics on self-reported likelihood of sharing social media disinformation.
Plos one15, e0239666 (2020).
10. Van Der Linden, S. Misinformation: susceptibility, spread, and interventions to immunize
the public.Nature medicine28, 460–467 (2022).
11. Thaler, M. The fake news effect: Experimentally identifying motivated reasoning using
trust in news.American Economic Journal: Microeconomics16, 1–38 (2024).
12. Zmigrod, L. A psychology of ideology: Unpacking the psychological structure of ideolog-
ical thinking.Perspectives on Psychological Science17, 1072–1092 (2022).
13. Raponi, S., Khalifa, Z., Oligeri, G. & Di Pietro, R. Fake news propagation: a review of
epidemic models, datasets, and insights.ACM Transactions on the Web (TWEB)16, 1–34
(2022).
14. Stein, J., Keuschnigg, M. & van de Rijt, A. Network segregation and the propagation of
misinformation.Scientific Reports13, 917 (2023).
15. Brooks, H. Z. & Porter, M. A. A model for the influence of media on the ideology of
content in online social networks.Physical Review Research2, 023041 (2020).
16. Rodriguez, N., Bollen, J. & Ahn, Y .-Y . Collective dynamics of belief evolution under
cognitive coherence and social conformity.PLoS one11, e0165910 (2016).
17. Del Vicario, M., Scala, A., Caldarelli, G., Stanley, H. E. & Quattrociocchi, W. Modeling
confirmation bias and polarization.Scientific reports7, 40391 (2017).
18. Stein, J., Keuschnigg, M. & van de Rijt, A. Partisan belief in new misinformation is resis-
tant to accuracy incentives.PNAS nexus3, pgae506 (2024).
16

19. Facciani, M. & Steenbuch-Traberg, C. Personal network composition and cognitive reflec-
tion predict susceptibility to different types of misinformation.Connections44, 165–180
(2024).
20. Tambuscio, M., Ruffo, G., Flammini, A. & Menczer, F. Fact-checking effect on viral
hoaxes: A model of misinformation spread in social networks. InProceedings of the 24th
international conference on World Wide Web, 977–982 (2015).
21. Karimi, S., Oliveira, M. & Pacheco, D. Modelling Misinformation Spread: The Role of
Network Density in Diverse Social Structures. In Czupryna, M., Kami´nski, B. & Verhagen,
H. (eds.)Advances in Social Simulation, Springer Proceedings in Complexity, 223–230
(Springer, Cham, 2025).
22. Leskovec, J. & Mcauley, J. Learning to discover social circles in ego networks.Advances
in neural information processing systems25(2012).
Appendix
The main text focuses on agent-based simulations of the proposed model. In addition, when
all individuals are assumed to have the same level of ideological intensity, the model admits
a mean-field analytical treatment. Here we provide the analytical solution for the steady-state
fraction of believers for the homogeneous-intensity case.
The corresponding state probabilities evolve according to
pB i (t+ 1) =fi(t)P S i (t) + (1−pf orget−p verif y)P B i (t)(4)
pF i (t+ 1) =gi(t)P S i (t) +pverif yP B i (t) + (1−pf orget)P F i (t)(5)
pS i (t+ 1) = [1−fi(t)−g i(t)]P S i (t) +pf orgetP B i (t) +pf orgetP F i (t).(6)
At steady state, we haveP X(t+ 1) =P X(t) =P(X). In the mean-field approximation,
the transition probabilitiesf i(t)andg i(t)are replaced by population-level expressionsfandg:
f=β P(B)(1 +L) P(B)(1 +L) +P(F)(1−L) , g=β P(F)(1−L) P(B)(1 +L) +P(F)(1−L) (7)
17

By rearranging equations 4 and 5 at the steady state we have:
f P(S) = (pforget +p verify)P(B),(8)
gP(S) +p verifyP(B) =p forgetP(F).(9)
Furthermore, the sum of the probabilities must equal 1:
P(S) +P(B) +P(F) = 1.(10)
Solving the equations forP(B)results the steady-state fraction of believers:
P(B) =



β[2Lp forget −(1−L)p verify]
2L(β+p forget)(pforget +p verify) ,ifβ[2Lp forget −(1−L)p verify]>0
0,otherwise
The outcome of the analytical solution is shown in Fig.9.
-1.0 -0.5 0.0 0.5 1.0
Afactor
Iintensity
= 0.05
0.00
0.10
0.20
0.30
0.40
0.50
0.60 0.70
-1.0 -0.5 0.0 0.5 1.0
Afactor
= 0.1
0.00
0.10
0.20
0.30
0.40
0.50
0.60 0.70
-1.0 -0.5 0.0 0.5 1.0
Afactor
= 0.15
0.00
0.10
0.20
0.30
0.40
0.50
0.60 0.70
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
Fig. 9.Fraction of believers as a function of ideological alignment factor and ideological intensity, obtained from
the analytical solution.
18
