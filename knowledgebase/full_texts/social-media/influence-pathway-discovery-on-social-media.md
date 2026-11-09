---
title: Influence Pathway Discovery on Social Media
url: https://arxiv.org/abs/2309.16071
category: social-media
subcategory: empirical
date: 2023-09
venue: ''
authors:
- Xinyi Liu
- Ruijie Wang
- Dachun Sun
- Jinning Li
- Christina Youn
source: arxiv
pdf_url: https://arxiv.org/pdf/2309.16071
pages: 7
chars: 33886
fetched_at: '2026-11-08T13:07:04+00:00'
kb_version: 1
---

# Influence Pathway Discovery on Social Media

Influence Pathway Discovery on Social Media
Xinyi Liu§, Ruijie Wang §, Dachun Sun §, Jinning Li, Christina Youn, You Lyu, Jianyuan Zhan, Dayou Wu,
Xinhe Xu, Mingjun Liu, Xinshuo Lei, Zhihao Xu, Yutong Zhang, Zehao Li, Qikai Yang, Tarek Abdelzaher
Department of Computer Science
University of Illinois at Urbana-Champaign
Urbana, IL 61801
{liu323, ruijiew2, dsun18, jinning4, youn13, youlyu2, zhan32, dayouwu2, xinhexu2,
mingjun6, xinshuo3, zhihaox3, yutongz7, zehao3, qikaiy2, zaher }@illinois.edu
Abstract—This paper addresses influence pathway discovery ,
a key emerging problem in today’s online media. We propose
a discovery algorithm that leverages recently published work
on unsupervised interpretable ideological embedding , a mapping
of ideological beliefs (done in a self-supervised fashion) into
interpretable low-dimensional spaces. Computing the ideological
embedding at scale allows one to analyze correlations between
the ideological positions of leaders, influencers, news portals,
or population segments, deriving potential influence pathways.
The work is motivated by the importance of social media as
the preeminent means for global interactions and collaborations
on today’s Internet, as well as their frequent (mis-)use to wield
influence that targets social beliefs and attitudes of selected
populations. Tools that enable the understanding and mapping
of influence propagation through population segments on social
media are therefore increasingly important. In this paper, influ-
ence is measured by the perceived ideological shift over time that
is correlated with influencers’ activity. Correlated shifts in ide-
ological embeddings indicate changes, such as swings/switching
(among competing ideologies), polarization (depletion of neutral
ideological positions), escalation/radicalization (shifts to more
extreme versions of the ideology), or unification/cooldown (shifts
towards more neutral stances). Case-studies are presented to
explore selected influence pathways (i) in a recent French election,
(ii) during political discussions in the Philippines, and (iii) for
some Russian messaging during the Russia/Ukraine conflict.
Index Terms —Social Network Analysis, Influence Network,
Ideological Embedding, Social Analysis Pipeline
I. I NTRODUCTION
The paper advances the science of influence network tomog-
raphy - the empirical mapping of influence pathways on social
media, derived from observable node behaviors. The work is
motivated by the exploding popularity of social networks and
their growing impact on population beliefs and attitudes. The
paper posits that interpretable unsupervised ideological em-
bedding [1], a recently proposed belief embedding approach,
is a crucial enabler towards inferring potential influence among
a diverse range of node types. Being unsupervised, it can be
computed at scale for many parties with no need for human la-
beling. Being interpretable, it yields actionable insights. Since
influence produces correlated changes in belief, computing the
This work was supported in part by DARPA award HR001121C0165
and HR00112290105, and in part under DoD Basic Research Office award
HQ00342110002. It is also supported in part by ACE, one of the seven
centers in JUMP 2.0, a Semiconductor Research Corporation (SRC) program
sponsored by DARPA.
§Equal contributions.
interpretable unsupervised ideological embedding at scale can
serve as a new foundation for influence network tomography.
As a proof of concept, an end-to-end self-supervised solution
is developed that relies on uncovering correlated changes in
nodes’ ideological embeddings to discover potential influence
pathways. Example outputs are presented based on multiple
social media datasets that illustrate the versatility of the
approach.
Modern solutions for influence estimation on social net-
works generally rely on a combination of (i) node embeddings
(that distill node attributes correlated with predisposition to
exert/follow influence), and (ii) neural networks that learn
to estimate influence among nodes given their computed
embeddings. A pioneering paper in that space is DeepInf [2],
but many variations exist [3]–[7]. The ideological embedding
we leverage [1], contrary to the aforementioned literature, is
an interpretable node representation (computed using a self-
supervised representation learning approach) that summarizes
ideological beliefs. Changes in ideological embedding there-
fore directly denote interpretable phenomena such as polariza-
tion, radicalization, reconciliation, or desertion of ideological
positions. Models that describe how changes in the embedding
of one node affect another can therefore serve as interpretable
indicators of ideological influence.
The rest of this paper is organized as follows. Section II
briefly covers key elements of related work. Section III
presents the problem definition of influence network tomogra-
phy. Section IV describes the proposed approach for mapping
influence pathways among diverse node types. Example case
studies are covered in Section V based on several social
media datasets. Section VI describes insights gained from the
evaluation and discusses opportunities for future extensions.
The paper concludes with Section VII.
II. R ELATED WORK
The work described in this paper falls in the broad category
of influence estimation on social media. Early work on influ-
ence analysis in social networks generally computed influence
either directly for individual network edges (resulting in such
measures as tie strength [8] and edge betweenness [9]) or inde-
pendently for individual nodes (resulting in such measures as
node centrality [10] and closeness [11]). Early work also con-
cerned itself with the analysis of epidemic diffusion cascades,
arXiv:2309.16071v1  [cs.SI]  27 Sep 2023

producing stylized models that predict cascade propagation,
such as the linear threshold model [12] and the independent
cascade model [13]. A large number of subsequent models
were developed that differ in how diffusion probabilities were
computed [14]. More recently, such models were adapted to
utilize node embeddings and neural networks for diffusion
prediction [15], [16].
Influence estimation can be thought of as a generalization
of diffusion prediction with the idea that information diffusion
from one node to another is one manifestation of influence.
Modern influence estimation literature has focused on different
flavors of node embeddings, where network nodes are mapped
into latent spaces in a manner that allows predicting influence
relations from such mappings. An example is Inf2vec [17],
which used relations among node embeddings to infer in-
fluence, and Multi-Influor [18] that extended the approach
to multiple influence factors from which influence could be
predicted along network edges. Node embeddings are powerful
because they can, in general, capture pairwise node interac-
tions, local network structures, and global similarity across
node categories. Furthermore, they allow the development of
neural networks that take such embeddings as input and predict
influence along edges as output. A well-cited early example
of such an approach to influence estimation is DeepInf [2].
It inspired many subsequent variants to use node embeddings
and deep learning for influence prediction, differing in the
details of the embedding used to capture node attributes and
the subsequent neural network used to infer influence (e.g.,
see [3]–[7]).
In the fast-changing world of social media, it was also
recognized that the underlying networks and attention patterns
are not static. Influence relations are thus very time-dependent
(in addition to being topic-dependent). Recent research there-
fore introduced time-sensitive and topic-specific solutions for
influence measurement [19] and diffusion prediction [20]. Our
approach is an instance of this latter category of techniques.
As alluded to in the introduction, our approach is novel in
its reliance on a new type of node embedding that we call
interpretable unsupervised ideological embedding [1]. As its
name suggests, the novelty of that embedding comes from
being both interpretable and unsupervised – a combination
that had not been previously accomplished jointly in ideolog-
ical mapping solutions. The embedding projects nodes into
an ideological space, where different axes denote different
ideologies (automatically disentangled in a self-supervised
fashion from observing social media posts). On each axis, a
positioning further up the axis denotes adherence to a more
extreme version of the underlying ideology. A change in a
node’s embedding represents a change in the node’s beliefs.
The approach projects both users and content into the same
latent space. Thus, the embedding (and subsequently influence
propagation) can be computed for a more diverse set of node
types, including individuals, communities, articles, and news
portals. Furthermore, the projection into the ideological space
is independent of the underlying social network platform;
the embedding can be computed for users and posts on
different social media platforms regardless of their format,
such as text [1], [21], [22] and images [23]. Below, we present
the problem definition in more detail and then describe the
solution architecture.
III. P ROBLEM DEFINITION
Given posts on some set of social media, the purpose
of this work is to uncover the latent influence network ,
comprised of entities and directional edges , that summarize
how influence propagates on the media considered. In this
network, the entities refer to objects in either the physical
world or online that can influence one another. Each directional
edge represents influence exerted by one entity on another.
To set the scope, we consider four types of entities in
analyzing influence pathways: (i) physical entities , such as
events that transpire in the physical world, external to the
social medium (such as protests, hospitalizations, donations, or
deaths), (ii) individual influencers, whose positions allow them
to impact larger population segments, (iii) user community
clusters representing communities on social platforms defined
by a clustering algorithm or according to the operator, and
(iv) information domains , each associated with a specific
agency portal ( e.g., YouTube, individual News media, etc)
that publish information of a given type, such as cnn.com,
foxnews.com, or infowars.com. Of the above types of
entities, the first type is represented by a directly measured
time-series. For example, we can use the GDELT database 1 to
count physical events of a particular type over time. Broadly
speaking, physical entities can denote any real-valued time-
series measurement to correlate other nodes’ embeddings
with. For example, economic indicators such as the price of
crude oil or the consumer confidence index could constitute
valid entities to consider in the influence network (e.g., to
help understand the impact of social media activity on such
indicators or vice versa). The remaining three types of entities
are represented by a time-series of ideological embedding
versus time, computed as we describe later.
Figure 1 shows an example latent influence network (com-
puted by the proposed algorithm), including the four types of
entities we defined above.
IV. T HE SOLUTION PIPELINE
To compute the latent influence network, we organize the
set of media posts (provided as input) into a graph, compute
ideological embeddings for graph nodes, decide on entities to
consider, and finally test these entities for significant pairwise
directional influence relations. The resulting set of uncovered
directional influence links (together with the entities they
link) then constitutes the produced latent influence network.
The pairwise influence test itself is a plug-in module in the
framework that determines whether or not directional influence
is likely between a given pair of entities. For simplicity,
below we shall use lagged correlations in belief embedding as
an indicator of potential influence, implying that a potential
1https://www.GDELTproject.org/

Individual Influencers
User  Communities
Physical Events
Information Domains
Fig. 1: An illustrative example of a derived influence network.
influence link is suspected when the time-series of one entity
can predict the time-series of another. This concept aligns with
Granger causality [24] but is not in itself a proof of causal
relations. Future incarnations of the framework can replace
this test with others that align better with actual causality [25]
(based on observations of belief embedding). More specifi-
cally, the execution pipeline consists of four stages:
1) Interaction graph construction: This stage involves or-
ganizing the input posts into a bipartite interaction graph
whose nodes are (i) the individual users (who posted on
the media), and (ii) their posts.
2) Interaction graph cleaning: Since we might not have
visibility into all interactions, a missing-link prediction
approach [26] is used to predict (likely) missing links
in the computed graph, as well as to eliminate spurious
(i.e., unlikely) ones.
3) Dynamic ideological representation learning: Next, we
compute the unsupervised interpretable ideological em-
bedding [1] for all nodes in the (cleaned) interac-
tion graph, mapping them (both users and posts) into
an interpretable, low-dimensional, latent space. These
lower-dimensional latent representations are computed
for successive time intervals to capture the evolution of
espoused beliefs over time.
4) Influence pathway discovery: This stage focuses on iden-
tifying meaningful entities and valuable patterns of in-
fluence propagation among those entities. A community
detection toolkit is first used to group individual users
in the interaction graph into user community entities.
For each found community, the ideological embeddings
of community members are averaged to yield a single
community-wide time-series. Popular users are sepa-
rately cast as potential individual influencer entities.
Popularly cited URLs are similarly cast as information
domain entities. Finally, physical entities are added
based on supplied input. Correlations are then computed
between all entity time-series involved. Edges are plotted
…
…
…
…
…
…
Graph
Construction
(Section IV-B)
Graph
Cleaning
(Section IV-C)
InfoVGAE
Embedding
(Section IV-D1)
Embedding
Propagation
(Section IV-D2)
Timeseries
Generation
(Section IV-D3)
Correlation
Calculation
(Section IV-F)
Pathway
Visualization
(Section IV-F)
Fig. 2: An overview of the proposed pipeline.
to depict large correlations. These edges (and the entities
they connect) form the output latent influence network.
Figure 2 depicts the overall workflow. The four stages men-
tioned above are discussed in more detail in Section IV-A,
Section IV-B, Section IV-C, and Section IV-D, respectively.
A. Interaction Graph Construction
The first step of the pipeline is to design a data structure that
can model the relationship between the users and the content
they post. The datasets collected for this paper are from Twitter
(currently X), where posted tweets can be collected using
API calls (subject to a rate limit) together with the posting
users and timestamps. Based on the raw data, we extend the
user-post graph by extracting embedded URLs in the posted
tweets and treating them as separate nodes linked back to the
posting users. The result is a bipartite graph of user-content
relationships, where the two types of nodes are media users
and posts (e.g., tweets and posted URLs). We call them user
nodes and assertion nodes, respectively.
B. Graph Cleaning: nPUGraph
The initial interaction graph we create may suffer false
positives (i.e., incorrectly attributed interactions) and false neg-
atives (unobserved interactions). These instances of incorrect
or missing interactions can significantly distort the subsequent
process of learning ideology representations, resulting in the
introduction of noticeable noise into the ideological embed-
ding time-series data. To address this issue, we incorporate the
nPUGraph method [26], previously introduced in our research,
as a data-cleaning step. This method effectively addresses
both the prediction of missing interactions and the removal
of erroneous ones, thereby enhancing the overall quality of
the interaction graph.

Graph
Convolutional
Encoder
Inner Product
Decoder
μx σx z
Input Graph Reconstruction
Rectiﬁed
Gaussian
Unsupervised Ideological Embedding
Fig. 3: The InfoVGAE architecture.
C. Dynamic Ideological Representation Learning
We map the users and assertions into an explainable latent
space using InfoVGAE [1], shown in Figure 3. InfoVGAE
is a variational graph auto-encoder that projects inputs into
the positive quadrant only (of the latent space). Its overall
loss function is further modified to ensure orthogonality of
projection coordinates, in addition to optimizing the evidence
lower bound (ELBO) of the typical V AE. Prior work has
shown that these changes lead to interpretable embedding
properties, as the orthogonality constraints (combined with
restrictions to the positive quadrant) cause different ideological
echo-chambers to be mapped onto orthogonal axes, while users
and posts at the intersection of the echo-chambers (i.e., those
who are more neutral) are mapped closer to the origin [1].
The above characteristics have important consequences.
They imply that the coordinate value of an entity’s embedding
on a given axis has an interpretable meaning. When that
value decreases, the entity must be expressing more neutral
beliefs with respect to the ideology represented by that axis.
Similarly, when the coordinate value increases, the entity must
be getting more entrenched in the ideology represented by
the axis. Said differently, changes towards higher coordinate
values on an axis represent ideological rhetoric escalation (for
the corresponding ideology). Similarly, changes towards lower
coordinate values on the axis represent rhetoric de-escalation
(for the corresponding ideology).
Unfortunately, the space complexity of InfoVGAE is of
the order of the product of users and assertions. To make
it scale, we use InfoVGAE to compute the embedding for
popular users and assertions only, then propagate the computed
node embeddings to their neighbors in the bipartite user-
assertion graph, such that previously excluded less popular
nodes inherit the average of their neighbors with known
ideology embeddings. The process is repeated in successive
time windows.
D. Influence Pathway Discovery
After the ideological embedding is computed for all users
and assertions, we identify the important entities to be included
in our influence network. As mentioned earlier, we include as
entities all nodes corresponding to popular referenced URLs
(information domain entities) and all popular users (individual
influencer entities), then lump the remaining users into com-
munity entities, computing an average embedding time-series
for each. We then introduce physical entities. For a proof of
concept, we consider events from GDELT, an external database
of the world’s real-life events. Among 311 event types that
GDELT provides, we selected 15 that are relevant to political
activity, such as “provide economic aid”, “investigate military
action”, and “obstruct passage”. For each such event type,
we produce a time series of event counts versus time. With
candidate entities selected as discussed above, we calculate
a lagged Pearson correlation for each entity pair. If a spike
occurs at a given offset, we say that an influence edge was
found (in the direction from the leading time-series to the
lagging one). The identification of all such (high-correlation)
edges completes graph construction.
V. C ASE STUDIES
Next, we offer a brief example of using this approach on
social media data sets collected on recent events.
A. Datasets
We test our pipeline on three datasets collected from X
(formerly Twitter). They are (i) the 2022 French election, (ii)
recent geopolitical events in the Philippines, and (iii) a Russian
influence campaign aiming to garner sympathy from claims
of “Western Russophobia”. Some basic statistics for each are
shown in Table I. The corresponding user interaction graphs
are displayed in Figure 4.
1) 2022 French Election: The dataset focuses on the mul-
tiple presidential candidates, the relevant media outlets,
and the candidates’ supporters during the time leading to
the 2022 French presidential election. Figure 4a shows
the corresponding user interaction graph, where one can
distinguish several clusters. They happen to correspond
to the different candidates and their followers.
2) Philippines: The dataset covers a multitude of topics
from the Philippines’ geopolitical landscape from the
first half of the year 2023. User interactions are shown
in Figure 4b.
3) Russophobia: The dataset covers posts on a key talk-
ing point of pro-Russian messaging during the Russia-
Ukraine war, namely, the claims of “Western Russopho-
bia” (referring to the allegation of unfair/hostile world
attitudes towards citizens of Russia), collected for nearly
a year starting 05/01/2022. Posts reacting to this line of
messaging are also included. Figure 4c shows the user
interaction graph, where one can clearly distinguish two
groups of users. They happen to be those siding with
the pro-Russia messaging and those against it.
Table II reports empirically tuned parameter settings for op-
timal performance on each dataset, including Window Length
(the interval of time, in days, over which each ideological
embedding value is computed), Time Shift (how much to slide
this window by in each step for time-series generation), Time
Lag Threshold (the maximum time lag we consider between
two time-series in searching for correlations), and Correlation
Threshold (the minimum Pearson-correlation used to identify
an influence edge).

TABLE I: Dataset Statistics.
#Users #Messages #Assertions Date Range
2022 French Election 389,187 3,195,579 829,484 02/15/2022-04/11-2022
Philippine 204,320 354,370 220,169 01/01/2023-06/28/2023
Russophobia 103,917 243,088 101,057 05/01/2022-04/15/2023
(a) The French election dataset user graph.
 (b) The Philippines dataset user graph.
 (c) The Russophobia dataset user graph.
Fig. 4: User graph visualizations. Nodes are colored dark blue. Repost (retweet) edges are colored blue, reply edges are colored
red, and quotation edges are colored green.
TABLE II: Algorithm Settings.
Window Length Time Shift Time Lag Threshold Correlation Threshold
2022 French Election 20 days 1 day 5 days 0.7
Philippine 20 days 2 days 5 days 0.5
Russophobia 20 days 2 days 5 days 0.4
B. Selected Observations
Figure 5 shows the interface used to inspect discovered
influence pathways. The screen allows the operator to inspect
parts of the influence network, view a heatmap of identified
(lagged) correlations between key entities, drill down into the
involved entity-pair’s ideological embedding time-series for
any cell in the heatmap, list the specific posts that explain the
underlying entity-espoused beliefs (for influencers, domains,
and communities), and control entity selection to view specific
parts of the overall influence graph. Example snippets of the
computed influence graphs are shown in Figure 6.
It is not the purpose of this paper to report political findings.
Thus, we obscure the names of the entities depicted and
focus on the general interpretations of the discovered pathway
examples. Following the influence graphs shown Figure 6 (in
the direction of the arrows, left-to-right), Figure 6a shows a
key influencer in the French election, and identifies two Twitter
communities influenced by them, as well as a news portal that
correlates with their view. Other links are also shown, such
as a downstream community influenced by the news portal.
Figure 6b shows another example from the French election,
where the rhetoric of a news portal and an online community
seem to predict protest counts. The graph also shows other
entities apparently influenced by the protests. Figure 6c shows
the impact of a key influencer in the Philippines dataset, as
well as multiple news media that follow their view, including
the reuters.com domain. Finally, Figure 6d shows a pathway
from the Russophobia dataset, depicting how a series of
GDELT events, including military aid (to Ukraine) incite
increased Russophibia rhetoric within a downstream Twitter
community.
These examples offer a flavor of what the pathway discovery
analysis can support. The actual results can be fine-tuned
by controlling the selection of entities to consider. Such
control may be exerted either directly (e.g., by selecting the
appropriate physical events, portals, or influencers to include)
or indirectly (e.g., by selecting the population segmentation
algorithm responsible for generating the community entities
of interest).
VI. D ISCUSSION AND FUTURE WORK
This influence pathway discovery solution presented in
this paper opens up opportunities for future expansion. It
is meant to offer a flexible framework where individual
modules can be replaced and enhanced over time. Some
such opportunities are discussed below. The first desirable
improvement lies in replacing the lagged correlation approach
(inspired by Granger causality) with alternative methods that
more accurately capture genuine causal effects. Identified
(ideally, causal) links can further be viewed as dynamical
stimulus/response systems modeled by transfer functions that
capture the (stimulus/response) relation between their input
and output time-series. An advantage of such models is
that they can capture (possibly nonlinear) cumulative effects
(where a response is a function of the integral of the stimulus)

Feature 1: Influence network
Feature 2: heatmap
Feature 3: time-series
Feature 4: detailed information
Feature 4: detailed information
Feature 5: entity selection
Fig. 5: An overview of the user interface. The service can be publicly accessed via https://incas.csl.illinois.edu/tasks.
as well as novelty effects (where a response is proportional
to the change in stimulus), among other functions that better
model the dynamics of social belief adoption.
The framework also offers the flexibility to integrate new
types of entities for analysis. For example, new types of
user communities may be identified by alternative community
detection algorithms, and new physical entity types can be
integrated besides GDELT events. The community and event
names can be automatically generated using large language
models (LLMs), applied to summarize or label sets of com-
munity posts. More substantial extensions are also possible,
such as what-if analysis. We can simulate how influence might
spread among entities when newly generated messages or
information campaigns are introduced into the social medium.
Finally, scalability remains a challenge. Our ideological
embedding and community detection methods do tackle scala-
bility concerns, allowing us to directly analyze extensive social
graphs comprising millions of nodes. Next, streaming versions
of these solutions are desired to allow continuous updates as
new social media posts arrive. We hope the above framework
will ultimately contribute to the mitigation of misuse in the
information space.
VII. C ONCLUSIONS
We presented a novel influence graph discovery pipeline
that differs from existing methods in its reliance on ideological
embedding to uncover evidence of influence. It defines influ-
ence as the act of impacting human beliefs and infers changes
in beliefs by mapping observed posts to an appropriately-
constructed interpretable latent space. An interactive user
interface and the corresponding backend were also imple-
mented that enable us to analyze real-world data sets. Case
studies were conducted to demonstrate the functionality of the
proposed approach. The work serves as a proof of concept for
influence network tomography based on belief embedding.
ACKNOWLEDGEMENTS
Research reported in this paper was sponsored in
part by DARPA award HR001121C0165, DARPA award
HR00112290105, and DoD Basic Research Office award
HQ00342110002. It was also supported in part by ACE, one
of the seven centers in JUMP 2.0, a Semiconductor Research
Corporation (SRC) program sponsored by DARPA.
REFERENCES
[1] J. Li, H. Shao, D. Sun, R. Wang, Y . Yan, J. Li, S. Liu, H. Tong,
and T. Abdelzaher, “Unsupervised belief representation learning with
information-theoretic variational graph auto-encoders,” in Proceedings
of the 45th International ACM SIGIR Conference on Research and
Development in Information Retrieval , 2022, pp. 1728–1738.
[2] J. Qiu, J. Tang, H. Ma, Y . Dong, K. Wang, and J. Tang, “Deepinf:
Social influence prediction with deep learning,” in Proceedings of the
24th ACM SIGKDD international conference on knowledge discovery
& data mining , 2018, pp. 2110–2119.
[3] C. K. Leung, A. Cuzzocrea, J. J. Mai, D. Deng, and F. Jiang, “Person-
alized deepinf: enhanced social influence prediction with deep learning
and transfer learning,” in 2019 IEEE international conference on big
data (big data) . IEEE, 2019, pp. 2871–2880.
[4] Y . Liu, J. Cao, J. Wu, and D. Pi, “Modeling the social influence of
covid-19 via personalized propagation with deep learning,” World Wide
Web, pp. 1–23, 2022.
[5] A. Cuzzocrea, C. K. Leung, D. Deng, J. J. Mai, F. Jiang, and E. Fadda,
“A combined deep-learning and transfer-learning approach for support-
ing social influence prediction,” Procedia Computer Science , vol. 177,
pp. 170–177, 2020.
[6] H. Xu, B. Jiang, and C. Ding, “Mvinf: Social influence prediction with
multi-view graph attention learning,” Cognitive Computation , pp. 1–7,
2022.
[7] L. Gao, H. Wang, Z. Zhang, H. Zhuang, and B. Zhou, “Hetinf:
social influence prediction with heterogeneous graph neural network,”
Frontiers in Physics, vol. 9, p. 787185, 2022.

(a) Example pathway 1 from the French election dataset.
 (b) Example pathway 2 from the French election dataset.
(c) Example pathway from the Philippines dataset.
 (d) Example pathway from the Russophobia dataset.
Fig. 6: Examples of ideology influence pathways.
[8] M. S. Granovetter, “The strength of weak ties,” American journal of
sociology, vol. 78, no. 6, pp. 1360–1380, 1973.
[9] L. C. Freeman, “A set of measures of centrality based on betweenness,”
Sociometry, pp. 35–41, 1977.
[10] P. Bonacich, “Factoring and weighting approaches to status scores and
clique identification,” Journal of mathematical sociology , vol. 2, no. 1,
pp. 113–120, 1972.
[11] L. C. Freeman et al., “Centrality in social networks: Conceptual clarifica-
tion,” Social network: critical concepts in sociology. Londres: Routledge,
vol. 1, pp. 238–263, 2002.
[12] M. Granovetter, “Threshold models of collective behavior,” American
journal of sociology , vol. 83, no. 6, pp. 1420–1443, 1978.
[13] J. Goldenberg, B. Libai, and E. Muller, “Talk of the network: A complex
systems look at the underlying process of word-of-mouth,” Marketing
letters, vol. 12, pp. 211–223, 2001.
[14] A. Guille, H. Hacid, C. Favre, and D. A. Zighed, “Information diffusion
in online social networks: A survey,” ACM Sigmod Record , vol. 42,
no. 2, pp. 17–28, 2013.
[15] S. Bourigault, S. Lamprier, and P. Gallinari, “Representation learning
for information diffusion through social networks: an embedded cascade
model,” in Proceedings of the Ninth ACM international conference on
Web Search and Data Mining , 2016, pp. 573–582.
[16] R. Wang, Z. Huang, S. Liu, H. Shao, D. Liu, J. Li, T. Wang, D. Sun,
S. Yao, and T. Abdelzaher, “Dydiff-vae: A dynamic variational frame-
work for information diffusion prediction,” in Proceedings of the 44th
International ACM SIGIR Conference on Research and Development in
Information Retrieval, 2021, pp. 163–172.
[17] S. Feng, G. Cong, A. Khan, X. Li, Y . Liu, and Y . M. Chee, “Inf2vec:
Latent representation model for social influence embedding,” in 2018
IEEE 34th International Conference on Data Engineering (ICDE) .
IEEE, 2018, pp. 941–952.
[18] F. Wang, J. She, Y . Ohyama, and M. Wu, “Learning multiple net-
work embeddings for social influence prediction,” IFAC-PapersOnLine,
vol. 53, no. 2, pp. 2868–2873, 2020.
[19] C. Zheng, Q. Zhang, G. Long, C. Zhang, S. D. Young, and W. Wang,
“Measuring time-sensitive and topic-specific influence in social networks
with lstm and self-attention,” IEEE Access , vol. 8, pp. 82 481–82 492,
2020.
[20] A. Sankar, X. Zhang, A. Krishnan, and J. Han, “Inf-vae: A variational
autoencoder framework to integrate homophily and influence in diffusion
prediction,” in Proceedings of the 13th international conference on web
search and data mining , 2020, pp. 510–518.
[21] C. Yang, J. Li, R. Wang, S. Yao, H. Shao, D. Liu, S. Liu, T. Wang,
and T. F. Abdelzaher, “Hierarchical overlapping belief estimation by
structured matrix factorization,” in ASONAM’20, 2020.
[22] D. Sun, C. Yang, J. Li, R. Wang, S. Yao, H. Shao, D. Liu, S. Liu,
T. Wang, and T. F. Abdelzaher, “Computational modeling of hierarchi-
cally polarized groups by structured matrix factorization,” Frontiers in
Big Data, vol. 4, 2021.
[23] X. Liu, J. Li, D. Sun, R. Wang, T. Abdelzaher, M. Brown, A. Barricelli,
M. Kirchner, and A. Basharat, “Unsupervised image classification by
ideological affiliation from user-content interaction patterns,” in Pro-
ceedings of PhoMemes (in conjunction with ICWSM) , June 2023.
[24] A. Seth, “Granger causality,” Scholarpedia, vol. 2, no. 7, p. 1667, 2007.
[25] J. Pearl, Causality. Cambridge university press, 2009.
[26] R. Wang, B. Li, Y . Lu, D. Sun, J. Li, Y . Yan, S. Liu, H. Tong, and
T. Abdelzaher, “Noisy positive-unlabeled learning with self-training for
speculative knowledge graph reasoning,” in Findings of the Association
for Computational Linguistics: ACL 2023 , Jul. 2023, pp. 2440–2457.
