---
title: Who is driving the conversation? Analysing the nodality of British MPs and journalists on social
  media
url: https://arxiv.org/abs/2402.08765
category: social-media
subcategory: empirical
date: 2024-02
venue: ''
authors:
- Sukankana Chakraborty
- Leonardo Castro-Gonzalez
- Helen Margetts
- Hardik Rajpal
- Daniele Guariso
source: arxiv
pdf_url: https://arxiv.org/pdf/2402.08765
pages: 15
chars: 56419
fetched_at: '2026-11-08T13:06:20+00:00'
kb_version: 1
---

# Who is driving the conversation? Analysing the nodality of British MPs and journalists on social media

arXiv:2402.08765v3  [cs.SI]  27 Jun 2025
Who is driving the conversation? Analysing the nodality of
British MPs and journalists on social media
Sukankana Chakraborty1,2,*,†, Leonardo Castro-Gonzalez1,*, Helen Margetts1,3, Hardik
Rajpal1,4, Daniele Guariso1, and Jonathan Bright1
1Public Policy Programme, The Alan Turing Institute, British Library, 96 Euston Rd,
London, NW1 2DB, UK.
2Centre for Advanced Spatial Analysis, University College London, Gower Street,
London, WC1E 6BT, UK
3Oxford Internet Institute, University of Oxford, 1 St Giles, Oxford, OX1 3JS, UK
4Department of Mathematics, Imperial College London, South Kensington Campus,
London, SW7 2AZ, UK
*These authors contributed equally
†corresponding author: sukankana.chakraborty@ucl.ac.uk
Abstract
With the rise of social media, political conversations now take place in more diffuse environ-
ments. In this context, it is not always clear why some actors, more than others, have greater
influence on how discussions are shaped. To investigate the factors behind such influence, we build
on “nodality” a concept in political science which describes the capacity of an actor to exchange
information within discourse networks. This concept goes beyond traditional network metrics that
describe the position of an actor in the network to include exogenous drivers of influence (e.g. fac-
tors relating to organisational hierarchies). We study online discourse on Twitter (now X) in the
UK to measure the relative nodality of two sets of policy actors - Members of Parliament (MPs)
and accredited journalists - on four policy topics. We find that influence on the platform is driven
by two key factors: (i) “active nodality”, derived from the actor’s level of topic-related engagement
and (ii) “inherent nodality” which is independent of the platform discourse and reflects the actor’s
institutional position. These findings significantly further our understanding of the origins of in-
fluence on social media platforms, and suggest in which contexts influence is transferable across
topics.
1 Introduction
In recent decades, internet-based platforms have transformed policy discourse significantly by reducing
the costs of exchanging information and by providing a more democratised environment for discussions
in which individuals from diverse backgrounds - elite politicians and members of the public alike - can
engage in conversations. This has led to interesting, complex online dynamics in which some actors,
often driven by factors that are poorly understood, wield greater influence than others on the course
of the conversation [Harris et al., 2024, Bright, 2016, Bright et al., 2020, Sprejer et al., 2022, Parmelee,
2013, Usherwood and Wright, 2017]. Understanding these drivers of influence is crucial in order to
better gauge which actors have the capacity to shape policy debates and online narratives —in some
cases spontaneously leading to significant and undesirable real-world outcomes (such as the UK riots
of 2024 [Boukari and Devakumar, 2024]). Although, much research has been dedicated to understand-
ing the relative influence of actors on social media [Dubois and Gaffney, 2014, Beguerisse-D ´ ıaz et al.,
2014, Anger and Kittl, 2011, Bakshy et al., 2011, Mei et al., 2015, Riquelme and Gonz´ alez-Cantergiani,
2016, Esteve Del Valle and Borge Bravo, 2018, Rezaie et al., 2020, Kolic et al., 2022, Flamino et al.,
2023, Zhang et al., 2023] —much of this work is centred around communications literature which uses
1

traditional network metrics to examine the roles of actors in the online network, rarely examining exter-
nal factors - such as institutional or individual characteristics - that could potentially drive differential
online attention towards these actors. Particularly in the context of political actors, a long-standing
question has been to what extent does the eliteness of an actor contribute to their role in online dis-
cussions? [Meraz, 2009, Steinberg et al., 2016, Barber´ a et al., 2019]. For instance, do frontbench
Members of Parliament (MPs) always attract greater online attention than backbench MPs, therefore
giving them a bigger say in the policy discourse? Or can individual factors, such as active engagement
with a specific issue within their constituency outweigh the significance of institutional status?
With this is in mind, here we tackle the question of ‘who drives political discourse, and how?’
through the lens of nodality [Castelnovo and Sorrentino, 2021, Howlett, 2009, Howlett, 2022]. Nodality
is a concept in political science that goes beyond simple network metrics and describes thecapacity of an
actor to be at the centre of information networks [Hood, 1983, Hood and Margetts, 2008, Margetts and
John, 2023]. Nodality used to be something that government —as a set of organisations —possessed
almost by virtue of being the “water mill” at the centre of society’s information networks [Margetts and
John, 2023]. But in a digital era, where policy debates take place in more open and diffuse information
environments, governmental actors face greater competition for nodality [Castelnovo and Sorrentino,
2021]. Widespread use of the internet means that non-governmental organisations or individuals such
as journalists, politicians, public figures and even citizens themselves can acquire nodality, which can
challenge the government’s capacity to capture public attention and drive policy and media agendas
[Margetts et al., 2019, Howlett, 2009, Howlett, 2022, Shearing and Wood, 2003]. So far there has been
little effort to quantify nodality, or the extent to which an actor can influence a discourse, beyond
simple metrics derived from network structure alone [Margetts and Escher, 2006, Petricek et al., 2006].
Framed within the context of policy-related discourse in the UK, here we propose a method that
measures the relative nodality of policy-actors as a means to determine the extent to which they shape
policy conversations. We construct a discourse network for each of the topics and a corresponding
null network which captures all the interactions that occur outside the topic. We measure the relative
nodality of actors, specifically their inherent and active nodalities by comparing their centrality metrics
across these two networks in a principal component analysis (PCA). We assume that inherent nodality
is high when centrality metrics are high across both networks, and active nodality is high when the
centrality of the actor is high in the topic network but low in the null network. In an independent
group-level transfer entropy (TE) analysis we show how the mean nodalities of a group of actors relate
to their capacity to drive activity . This method is then used to analyse a subset of political actors in
the UK: Members of Parliament (MPs) and accredited journalists, as both MPs and journalists play
key roles in the British policy system. More specifically, we examine to what extent institutional and
individual characteristics drive their interactions with each other. We study conversations around four
policy topics in the year 2022: (1) the Russia-Ukraine war (2) the challenging economic situation facing
ordinary citizens in the UK (Cost-of-Living crisis) (3) Britain’s departure from the EU (Brexit) and (4)
the aftermath of the COVID-19 pandemic. All four issues were contested in policy terms and related
to an increasingly challenging economic situation in 2022, driven by Brexit [Diamond, 2023, Dhingra
and Sampson, 2022], the pandemic [Blundell et al., 2022], the Russia-Ukraine war [Mbah and Wasum,
2022, Liadze et al., 2023] and the resulting energy crisis [Harari et al., 2022, Francis-Devine et al.,
2022], as well as a “mini-budget” in the autumn of 2022 which led to sharp and sustained rises in
interest rates [Chadha, 2022, Tosun and Lucey, 2023, Li, 2023].
For the purpose of our study, we examine the nodality of actors along two key dimensions: (i)
inherent nodality, which is earned by virtue of one’s institutional role (such as a frontbench position)
and (ii) active or “topic specific” nodality, which is earned through engagement on a particular topic.
We show that inherent nodality —which is independent of the platform —is a useful indicator of
the actor’s influence on the platform, but that both dimensions of nodality (inherent and active)
significantly impact the capacity of an actor to influence activity (e.g., drive activity of others) on the
platform. Analysing these two types of nodality is crucial to understanding the dynamics of influence
in real-world policy networks. By distinguishing the influence that is derived from institutional status,
we are able to determine the nodal advantage of actors across topics, but also uncover early signs
of emerging policy actors in specific topics, such as the opposition backbencher Zarah Sultana, who
figured prominently in our early analysis of the cost-of-living crisis discourse, and during the 2024
general election was recognised as the most influential MP on TikTok 1.
1standard.co.uk/news/politics/zarah-sultana-labour-mp-coventry-south-tiktok-b1159562.html
2

2 Data
The data for our study was collected using the Twitter API. We study 6M tweets that were published
by UK MPs and journalists between January 14, 2022 and January 13, 2023. Of the 650 House of
Commons MPs at the time, we found that 581 MPs have active Twitter accounts and a total of 580,312
tweets were collected from these accounts. We also obtained a list of UK journalists and their Twitter
handles from journalism.co.uk. Of the 9594 journalists on the list, we were able to collect tweets from
8606 journalist accounts and over 5M tweets were collected from these accounts.
Our study examines the discourse between MPs and journalists on four policy topics: Russia-
Ukraine War, cost-of-living crisis, Brexit, COVID-19. Tweets were classified into each of these topics
using a weak supervision approach [Ratner et al., 2019, Castro-Gonzalez et al., 2024]. Details of the
approach can be found in the 4. Tweets that were not assigned to any of the above topics were left
unlabelled. We visualise the discourse on each topic by building a weighted, directed graph where
nodes represent actors and any interaction from an actor j to an actor i, such as a retweet, mention
or reply, is captured as an edge i → j. As nodality describes the capacity of a node to transmit
information, we consider any interaction in the form of retweets, mentions and replies from actor j
to i as a flow of information from i → j. The edge weight wij corresponds to the number of times a
target node interacted with the source node, thus capturing the volume of information passing from
the source actor to the target actor.
3 Results
3.1 The multi-dimensional nature of influence
We begin by qualitatively analysing the discourse networks for each topic. To do this, we employ
centrality metrics —a key concept in network analysis which describes the position of an actor in a
social network [Anger and Kittl, 2011, Bakshy et al., 2011, Mei et al., 2015, Riquelme and Gonz´ alez-
Cantergiani, 2016, Rezaie et al., 2020, Zhang et al., 2023, Essaidi et al., 2020]. In particular, we examine
the outdegree of the actors in the discourse network as an indication of how much information they
are able to transmit in the rest of the network.
Our analysis shows that some nodes —typically MPs with front-bench positions —appear promi-
nent in all four conversations. As an example we present the cost-of-living crisis network in Figure
1. We find that nodes with the highest outdegrees, i.e., with the most engagement, are MPs with
important parliamentary positions i.e. Cabinet and Shadow Cabinet MPs during 2022-2023, such as
Boris Johnson, Rishi Sunak, Liz Truss, Keir Starmer, Rachel Reeves and Ed Milliband, and political
editors at leading UK newspapers, such as Pippa Crerar (from The Guardian), Steven Swindon (The
Times), and Jim Pickard (Financial Times). Rishi Sunak has the highest outdegree in the network
which can be attributed to the two key roles he held during the year 2022-23 —the Chancellor of the
Exchequer, a pivotal role in public spending, and eventually that of the Prime Minister of the UK. We
find that Rachel Reeves, the Shadow Chancellor of the Exchequer, and Nadhim Zahawi, who was the
Chancellor under Liz Truss’ premiership in 2022, are also among the key actors in the cost-of-living
crisis discussion.
At the same time, we find that some actors appear prominent only in specific discourse networks.
For instance, in the case of the cost-of-living crisis discussion we find that Zarah Sultana, a Backbench
Labour MP, despite their less significant role in the parliament plays a key role in the conversation
(Figure 1). Furthermore, we find that their centrality in the cost-of-living crisis discussion does not
extend to any of the other topics studied here. Whereas actors with more senior positions within
the Cabinet (or shadow frontbench) in 2022 such as Boris Johnson, Rishi Sunak, Liz Truss and Keir
Starmer appear consistently central in all four topics of discussion, suggesting that influence on these
platforms can be multi-dimensional [Dubois and Gaffney, 2014].
While centrality metrics are useful for qualitatively analysing an actor’s influence in online discourse,
it ultimately falls short in determining factors driving such influence, such as to what extent does an
actor’s institutional status or level of engagement on a topic contribute to their influence on the
platform? We rely on the concept of nodality to answer these questions [Margetts and John, 2023].
Nodality describes the capacity of an actor to be in the centre of an information network and thus draws
out factors driving an actor’s influence on a platform, specifically by capturing multiple dimensions of
3

Conservative MPs
Labour MPs
Other Party MPs
Journalists
Node X:
MP/journalist
Node Y:
MP/journalistb)
retweet/reply/mention
Information edge
from Y to X
a)
MPs
Journalists
Figure 1: Qualitative analysis of the cost-of-living crisis discourse. Figure (a) shows the daily tweet
volumes from MP and Journalist accounts related to the cost-of-living crisis discussion between January
14,2022 and January 13, 2023. We generally observe similar levels of activity from both actors. Figure
(b) shows the giant connected component of the cost-of-living crisis conversation network. Nodes
representing journalists are shown in grey, while MPs are represented using coloured nodes where the
colour signifies the political party they are affiliated with (Conservative, Labour, other parties). Edges
here take the colour of the target node. The force-layout algorithm was used to visualise the network
and we find that nodes appear clustered based on party affiliations. The size of a node corresponds
to the weighted out-degree which reflects the number of times a user has been retweeted (replied to
or mentioned) by others in the network. Some actors who stand out in the network and appear to be
central to high levels of activity on the topic have been explicitly labelled.
influence such as extroversion (from engagement on the platform), visibility (from institutional status)
etc., which cannot be fully described by any one centrality measure but can be captured by using a
combination of centrality metrics. Authors in prior work show how each centrality metric relates to
different dimensions of nodality [Margetts and Escher, 2006, Petricek et al., 2006], and building on this
work, we establish a methodology that combines several centrality measures to quantify the relative
nodality of actors in a discourse network. We measure nodality along two dimensions —inherent
nodality which tells us the extent to which an actor’s institutional role contributes to their influence
on the platform and active nodality which highlights the topic-related influence the actor has on the
platform.
We consider six centrality metrics in our work —degree centrality, betweenness centrality, Eigen-
value centrality, Authority and Hub score [Kleinberg, 1999] and finally the strength of a node. Each of
these metrics describe dimensions of nodality such as extroversion, authority and visibility of actors,
which are key to determining the capacity of actors to transmit information [Margetts and Escher,
2006]. In addition to the traditional centrality measures, we add two new metrics that are specific
to the Twitter platform and that explore the follower count of users to estimate their popularity and
reach on the platform [Riquelme and Gonz´ alez-Cantergiani, 2016]. We term these metrics: (i) the
funnel bandwidth and (ii) the amplification bandwidth of an actor. The funnel bandwidth of an actor
is a measure of the extent to which they facilitate the passage of information in the network. This is
quantified in terms of the volume of interactions (retweets, mentions, replies), weighted by the actor’s
follower count. Amplification bandwidth, on the other hand, measures the exposure of information
from a user in two hops. We measure this as the number of times a user i interacts with others,
weighted by the number of followers of each target user j. More specifically, these metrics are defined
4

respectively as:
νi = 1 ⟨kin⟩ X h f iwhi and µi = 1 ⟨kout⟩ X j f jwij. (1)
Here f i represents the number of followers of node i, wij is the weight of link i → j, ⟨kin⟩ is the average
in-degree of the weighted network and ⟨kout⟩ is the average out-degree.
3.2 Inherent and active nodality of individual actors
Our aim is to measure the relative nodality of actors along two dimensions: institutional nodality
and topic-related (active) nodality. To do this, we first construct two networks for each topic —the
topic-related discourse network and a corresponding null network that captures all the interactions
outside the topic. In order to capture the inherent and active nodality of actors we compare their
centrality measures across the topic and the null network. More specifically, since inherent nodality is
driven by institutional status and thus is independent of the topic, we assume that inherent nodality
is high for an actor when centrality measures are high across both topic and null networks. Similarly,
we assume that active (or topic-specific) nodality is high when centrality measure is low in the null
network but high in the topic network, i.e. the actor has no ‘eliteness’ on the platform but has gained
nodality only on the specific topic.
To quantify the two types of nodality, we perform a principal component analysis (PCA) on an n
x 2m matrix with rows corresponding to n nodes, and columns corresponding to m centrality metrics
(computed for each network and so 2m columns in total). We enforce conditions for inherent and active
nodality by introducing an eigenvector test. The eigenvector test checks the first two eigenvectors of
the PCA transformation to verify that in the case of inherent nodality, centrality measures across both
networks are all positively (or all negatively) correlated with the first principal component. In the case
of active nodality we check if the centrality measures on the topic network are positively correlated with
the second principal component and centrality measures on the null network are negatively correlated
to the second principal component. If for example we perform a PCA with any three centrality
measures, such that the eigenvectors in the PCA transformation is given by e = (f t 1, ft 2, ft 3, f0 1 , f0 2 , f0 3 ),
where fn refers to the centrality measures and the superscript t/0 indicates the type of network, i.e.
topic or null network. Then we say a configuration passes the eigenvector test if the first eigenvector is
of the form e1 = (1, 1, 1, 1, 1, 1) or e1 = (−1, −1, −1, −1, −1, −1) and the second eigenvector is of the
form e2 = (−1, −1, −1, 1, 1, 1) or et = (1, 1, 1, −1, −1, −1). At this stage, we generate all combinations
of three or more centrality metrics and only retain combinations that pass the eigenvector test (i.e.
satisfy our conditions of inherent and active nodality).
Next, to determine the set of centrality measures that best captures inherent and active nodality of
actors we apply an additional condition to the PCA-transformed data. Given that inherent nodality is
topic-agnostic, we assume that the group of actors with high relative inherent nodality will be similar
across all four topics. To apply this condition, we use a k−means clustering method on the PCA-
transformed data to cluster nodes based on their relative nodalities. We find that k = 3 optimally
divides the population along the first principal component axis, i.e. based on their inherent nodality.
More specifically, we obtain three clusters: actors with inherent nodality (i) higher than the mean of
the population, (ii) same as the mean and (iii) lower than the mean. We compare the cluster of actors
with high inherent nodality across all four topics. The combination of metrics that maximises the
number of shared actors across all four topics includes: the strength of a node, their degree centrality
and the funnel bandwidth of the node. In the rest of the paper, we use this set of centrality metrics
to measure the relative inherent and active nodalities of actors.
We visualise the cost-of-living-crisis network using these results. Each node is coloured based on
the cluster they belong to (i.e., high, low, mean inherent nodality). We observe that the three clusters
form three separate tiers in the conversation network. Nodes with high inherent nodality assume
central positions in the conversation, i.e. we find that most of the interactions in the network are
centred around these nodes. We term these nodes leaders. Nodes with less than average inherent
nodality typically appear on the periphery of the network with limited connections to the rest of the
network (average degree of 2). As these nodes appear to be at the periphery or at the receiving end of
the information spread process, we term them receivers. Finally, we observe that nodes with average
nodality (as the rest of the studied population) form the layer between the central nodes and the
5

a) b)
Figure 2: PCA results for the cost-of-living crisis conversation. Figure (a) showing PCA results for
the cost-of-living crisis topic. PC1 captures the inherent nodality of actors and PC2 captures the
active nodalities. We cluster nodes using k-means clustering algorithm. We obtain 3 stable clusters
that groups actors based on their inherent nodalities. Actors with high inherent nodality, are termed
Leaders. Those with inherent nodality similar to that of the mean of the population are termed
Funnelers and actors with less than average nodality are termed Receivers. Figure (b) shows the
visualisation of the cost-of-living crisis network. We use the force-atlas algorithm for the layout.
Nodes are coloured based on their cluster membership from the PCA. The size of the nodes reflects
their weighted outdegrees. Actors with prominent parliamentary positions appear to be in the Leader
cluster along with some other actors such as Zarah Sultana who has a back-bench parliamentary
position but appear to have high active nodality on the topic (PCA results on the left).
peripheral nodes. We find that these nodes appear to bridge the interactions between the leaders and
the receivers, by receiving information from the leaders (through retweets/mentions and replies) and
passing it onto the receivers, and hence we term them funnelers.
3.3 How does nodality explain influence on the platform?
To examine how the relative nodality of an actor relates to their influence on the platform we employ
a transfer entropy (TE) analysis which is independent of the conversation networks and studies the
time-series of the actors’ activities. More specifically, the TE analysis helps us measure the extent
to which the activity of a group of actors can predict the activity of the rest of the actors in the
conversation. In this instance, we study the groups of actors clustered based on their inherent nodality
scores (as above) and perform a TE analysis across all four topics to examine how actors with different
inherent nodalities influence the conversations.
TE analysis typically captures the flow of information between two time-series and can be inter-
preted as the extent to which Y’s current activity can be predicted by X’s past. We determine the net
information flow from X to Y as follows:
φ(X, Y, t, k= 1) = TX→Y (t, k= 1) HY (t) − TY →X (t, k= 1) HX (t) , (2)
where HX (t) is the entropy of X at time t. and similarly HY (t) is the entropy of Y at time t. The
share of influence φ at time t gives the net flow of information between X and Y with a time-lag k, at
time t. φ lies on the interval [-1, 1]. If this quantity is positive, then there is an information flow from
X → Y , whereas if it is negative, information flows from Y → X [Schreiber, 2000].
6

The results of the TE analysis aggregated across all four topics are shown in Figure 3. We find
that leaders, i.e. the group of actors with high inherent nodality consistently influence the rest of the
population positively. Receivers, on the other hand, have a negative share of influence, which indicates
that they mainly respond to the ongoing activity in the network and primarily receive information.
Whereas funnelers demonstrate low positive values suggesting that while their activity may influence
the activity of the receivers, their own activity is influenced by the activity of theleaders. This suggests
that nodality can be a useful tool to study the roles of actors in online discourse, and help determine
who has the capacity to shape the discourse (by influencing the activity related to the topic).
TE analysis
Figure 3: PCA results for all four topics. Figure on the left shows the PCA results for each of the
four topics: the Russia-Ukraine War, Covid, cost-of-living crisis and Brexit. In each case, we run the
k-means clustering algorithm where k = 3. We find that this consistently groups actors based on their
inherent nodality (i.e. along PC1). We then take the clusters of nodes for each topic and independently
perform a transfer entropy (TE) analysis where we determine the impact of each cluster on the rest of
the population. The results are then aggregated across all four topics and presented in the figure on
the right. We find that the Leader cluster on average has higher influence than the other two clusters
on the activity of the population across all four topics.
We now use the approach proposed above to answer our original research question —who between
the MPs and journalists leads the conversation on the policy topics studied here? Specifically, we
want to determine who is leading whom (i.e. MPs leading journalists or vice-versa) in each of the four
discussions. For a more effective analysis, we split MPs and journalists into sub-groups to reflect their
organisational roles (in order to capture influence related to institutional nodality). We exploit the
structure of the British parliament and classify MPs into four groups: the Cabinet, which forms the
executive power; the Shadow Cabinet, formed by the Opposition party that oversees the activities of
the Cabinet; the Backbench, formed by MPs of the ruling party who do not have a place in the Cabinet;
and its analogous for the opposition party, simply called the Opposition. We also divide journalists
into two groups based on their follower counts. We find that the ratio of the Cabinet to the Backbench
MPs and of the Shadow Cabinet to the Opposition (backbench) MPs is roughly 10%. We also split
the journalists by separating the 10% most-followed journalists from the rest of the journalists (and
term them prominent journalists).
Next, we repeat the PCA analysis as above, but assign the nodality scores as the mean values
for each group. Results of the PCA are shown in Figure 4. We find that Cabinet MPs and Shadow
Cabinet MPs have the highest inherent nodality for all four topics, along with prominent journalists.
This implies that actors with higher institutional status inherently have more visibility and engagement
7

from the other actors on each of the four topics. On examining the active nodality of actors, we find
that on average more Shadow Cabinet ministers have nodality specific to the topic of cost-of-living
crisis and limited active nodality on the topic of Brexit. We further observe that the Opposition
back-bench has relatively high active nodality on the cost-of-living crisis topic, suggesting that the
Opposition Party as a whole had more engagement from journalists and MPs on the platform on the
issue of the economic crisis under the Conservative government, which also went onto being a focus of
the Labour Party’s election manifesto in 2024 [Stafford et al., 2024].
Figure 4: Inherent and active nodality of all sub-groups of actors across all four topics. The boxplot
on the left shows the inherent nodality of actors for each sub-group and on each topic. We find similar
trends across all topics, where MPs with key parliamentary positions have highest inherent nodalities,
followed by the most followed journalists and then the rest of the actors. The boxplot on the right
summarises the active nodality of the sub-groups. We obtain more nuanced results where different
sub-groups of actors have different rankings across topics.
So far both inherent and active nodalities have been found to play an important role in the level of
engagement an actor receives on a given topic on the platform. However, does one of the dimensions
matter more than the other in driving influence on the platform?
To analyse the association between the share of influence and the two types of nodality, we perform
a regression analysis given by:
φ(G, ¬G, t) = constant + γt +
X
i∈G
αinherentPC1t i + X
i∈G
αactivePC2t i
+
X
i∈G
βPC1t i × PC2t i, (3)
where G refers to a given group, which in our case is the Cabinet, the Shadow Cabinet, etc. ¬G
refers to the complement of G, thus all nodes not belonging to G. PC1 and PC2 refer to the first
two components of the resulting PCA. αinherent, αactive and β are three independent coefficients. The
combined term PC1×PC2 is included to determine any interaction effect. A temporal term γt is also
included to capture the effect of time. We fit the LHS of Eq. (3) with the influence score of each group
from the TE analysis. The RHS of the equation is fitted with the mean inherent and active nodalities
at group level, obtained from the PCA. We standardise the time-period across the TE analysis and
the PCA, by creating snapshots of networks over a period two weeks (for the PCA), which is also the
time-lag considered in the TE analysis.
Results of the regression analysis are presented in Table 1. We make three key observations: (i) the
capacity of a group to influence the discussion related to a topic depends both on their engagement
on the topic as well as their institutional status; (ii) the capacity of a group to influence topic-related
activity is positively related to the mean inherent and active nodalities of the group; and finally, (iii)
we also show that the two dimensions of nodality (inherent and active) are independent of each other,
since the crossed term (inherent-active) does not contribute to the capacity of the group to influence
activity. Thus establishing a robust methodology to quantify nodality of actors along two independent
8

Table 1: Results of the linear regression.
N = 1045, R2 = 0.6137
Variable Coefficient p-value
Inherent*** 0.010 ± 0.001 0.000
Active* 0.008 ± 0.004 0.025
Inherent-Active −0.001 ± 0.001 0.111
Time*** −0.002 ± 0.000 0.000
Intercept** 0.088 ± 0.029 0.002
dimensions —(i) institutional status related nodality (or inherent nodality) which is transferable across
topics and (ii) topic-specific nodality (or active nodality).
4 Discussion
To date, the concept of nodality has been studied largely from a theoretical perspective [Margetts and
John, 2023, Castelnovo and Sorrentino, 2021, Howlett, 2009, Howlett, 2022], with very few attempts
to quantify nodality in an empirical setting [Margetts and Escher, 2006, Petricek et al., 2006]. Here
for the first time, we focus on computing nodality scores for individual actors in policy conversations
as a tool to gauge their relative influences in policy-related online discourse. More specifically, for
our two sets of elite actors (MPs and journalists), we distinguish and measure two dimensions of
nodality; (i) topic-specific active nodality at the individual level, relating to the activity of an actor
on a specific topic, and (ii) inherent nodality relating to the actor’s institutional role and status. We
show that distinguishing between the two types of nodalities provides a useful way to determine the
nodal advantage of actors in prominent roles, such as in the case of Ministers and political editors,
who by virtue of their institutional status possess nodality which can be transferred across topics. Our
main finding is that, while both institutional status and platform activity is important, activity can
generate limited topic-specific influence whereas institutional status tends to bestow influence across
topics.
This work enriches our understanding of the role of policy-actors in policy-related conversations,
as it goes beyond studies which look at the influence of individuals in a conversation only in terms
of their network attributes or positions in the network (i.e. centrality metrics) [Dubois and Gaffney,
2014, Riquelme and Gonz´ alez-Cantergiani, 2016, Esteve Del Valle and Borge Bravo, 2018, Zhang et al.,
2023]. Indeed, we introduce a methodology that measures the capacity of an actor to influence others
in an online policy conversation —either on the basis of their institutional status (which is platform-
and topic-independent), or as an emerging leader with growing topic-specific nodality. Our study also
expands on the literature of politics and journalists on Twitter [Mosleh and Rand, 2022, Parmelee,
2013, Romenskyy et al., 2018, Jungherr, 2014, Kim and Park, 2012, Graham et al., 2013, Graham et al.,
2015, Bovet and Makse, 2019, No˙ zewski and Baranowski, 2021, Shapiro and Hemphill, 2017, Bright,
2018, Mosleh et al., 2024, Li et al., 2024], introducing the actor’s role in their institutions and their
individual activity on a topic as key elements in understanding the influence they exert.
Going forward, our methodology could support further research investigating the activities and in-
fluence of politicians on online platforms. For instance, here we classify inherent nodality as pertaining
to institutional status, but there are other potential drivers of inherent nodality that our approach
might help to identify, such as educational background, that could contribute to their ‘eliteness’ by
virtue of being within specific social circles that in turn could then drive their nodality on the platform,
independent of individual levels of activity. Alternatively, our methodology might assist the study of
different, more negative kinds of attention, such as hate speech directed at political representatives,
where our approach might help assess which element of the hate directed at ministers relates to their
institutional role or their individual characteristics. This has been a challenge to examine in the past
[Gorrell et al., 2020], given that ministers are more well-known and hence get more hate, regardless of
race or gender [Agarwal et al., 2021]. Likewise, for journalists, who are increasingly suffering threats
of violence online, such an approach might help determine whether the hate they receive relates to the
publications they work for, or to their historic activity on policy-topics such as gender.
9

Finally, there are some limitations to this work. First, our elite networks include only British
journalists and MPs. This is a limited set of individual actors, albeit an important one in terms of
nodes that have both individual and institutional nodality, and who play an important role in setting
the policy agenda. Second, we have covered only four policy topics. Future work might focus on larger
domains, such as defence and security (rather than the Ukraine war as focused on here), which could
allow us to say something generalisable about elite networks in broader domains. Third, our results
represent an analysis of the volume of activity – and not the content, which could also be insightful
[Jim´ enez-Zafra et al., 2021]. Fourth, we have looked at only one specific social media platform -
Twitter, now X, a platform currently experiencing a decline 2, which may not be possible to analyse in
this way in the future, due to the lack of data and also lack of universality (due to the 2024/25 exit
from X). It will be increasingly important therefore, to conduct such research on different platforms.
Acknowledgments
The authors would like to thank Angus R. Williams for providing the first list of Twitter handles
associated with MPs. The authors would also like to thank Eirini Koutsouroupa for her support and
effort to get this work published.
Funding
This work was supported by the Public Policy Programme of The Alan Turing Institute under the
EPSRC grant EP/N510129/1. This work was supported by the Ecosystem Leadership Award under
the EPSRC Grant EP/X03870X/1 & The Alan Turing Institute.
Author contributions statement
L.CG., S.C., H.R., H.M., D.G. and J.B. conceived the experiment(s), L.CG. and S.C. conducted the
experiment(s), L.CG., S.C., H.R and H.M. analysed the results. L.CG., S.C. and H.M. wrote the
manuscript and L.CG., S.C., H.R., H.M, D.G and J.B. reviewed the manuscript.
Data availability
Twitter data is made available in accordance with Twitter’s terms of service. Tweet IDs and analysis
code are available at https://github.com/Turing-Online-Safety-Codebase/nodality . The cor-
responding tweets can be downloaded using the official Twitter API ( https://developer.twitter.
com/en/docs/twitter-api).
Appendix
4.1 Weak supervision classifier
To classify tweets by topic, we build a classifier using a weak supervision approach. This allows us to
move beyond keyword search and create heuristic rules tailored to specific topics. Weak supervision
has found application in various contexts such as medicine and health sciences [Fries et al., 2021, Silva
et al., 2022], chemistry [Mallory et al., 2020], detection of fake news [Shu et al., 2021], and more
generally to study sentiment analysis [Jain, 2021, Castro-Gonzalez et al., 2024], and ontology and
computational linguistics problems [Maresca et al., 2021, Berger and Goldstein, 2021].
The classifier is based on a set of labelling functions (LFs) and a probabilistic model that applies
these functions to the unlabelled data. LFs are rule-based functions that assign labels based on specific
criteria, such as keywords, regular expressions, Named-Entity Recognition (NER) systems, and NLP
features like polarity and subjectivity. This diverse set of criteria results in topic-specific LFs that
are tailored to the nuances of each topic, offering a more sophisticated approach than simple keyword
2variety.com/2023/digital/news/musk-twitter-x-acquisition-one-year-user-revenue-decline-1235770297/
10

searches. Given m labelling functions and n unlabelled data points, the process of applying all labelling
functions to the entire data set will result in an n × m matrix M where each entry reflects how a
given labelling function acted on a data point. By having a training data set with golden labels Y ,
the probabilistic LabelModel [Ratner et al., 2019] computes the conditional probability of labelling
functions given the matrix M , P (LF |M , Y ). The latter probabilities are used as parameters to then
obtain a final label for each data point.
In our case, we build a collection of labelling functions for each one of the four studied topics. A
detailed list of these functions can be found in our GitHub repository3. With the purpose of illustrating
how labelling functions are created, we give two examples of pseudo LFs for the topic of the Cost of
Living Crisis:
LF1 : label CRISIS if any keyword in keywords in datapoint else ABSTAIN.
LF2 : label CRISIS if ‘(rising|inflation|rise)\W+(?:\w+\W+)0,6?
(inflation|is rising)’ in datapoint else ABSTAIN
While LF1 refers to a normal keyword search, LF2 refers to a more complex regular expression regarding
the rise of inflation. LF2 allows us to look for different forms of the same sentence “The inflation is
rising”.
Confusion matrix of the classifier
Table 2: Confusion matrix of the classifier. The size of the test data sample is N = 598.
Actual Topic
Predicted Topic
Other Ukraine COVID-19 Cost of Living Crisis Brexit
Other 8.99e-1 1.65e-2 2.27e-2 5.98e-2 2.00e-3
Ukraine 0.00 1.00 0.00 0.00 0.00
COVID-19 0.00 0.00 1.00 0.00 0.00
Cost of Living Crisis 0.00 0.04 0.00 0.96 0.00
Brexit 0.00 0.00 0.25 0.00 0.75
References
[Agarwal et al., 2021] Agarwal, P., Hawkins, O., Amaxopoulou, M., Dempsey, N., Sastry, N., and
Wood, E. (2021). Hate speech in political discourse: A case study of UK MPs on twitter. In
Proceedings of the 32nd ACM Conference on Hypertext and Social Media , HT ’21, pages 5–16.
Association for Computing Machinery.
[Anger and Kittl, 2011] Anger, I. and Kittl, C. (2011). Measuring influence on Twitter. In Proceedings
of the 11th International Conference on Knowledge Management and Knowledge Technologies, pages
1–4, Graz Austria. ACM.
[Bakshy et al., 2011] Bakshy, E., Hofman, J. M., Mason, W. A., and Watts, D. J. (2011). Everyone’s
an influencer: quantifying influence on twitter. In Proceedings of the fourth ACM international con-
ference on Web search and data mining , WSDM ’11, pages 65–74, New York, NY, USA. Association
for Computing Machinery.
[Barber´ a et al., 2019] Barber´ a, P., Casas, A., Nagler, J., Egan, P. J., Bonneau, R., Jost, J. T., and
Tucker, J. A. (2019). Who leads? who follows? measuring issue attention and agenda setting
by legislators and the mass public using social media data. American Political Science Review ,
113(4):883–901.
3https://github.com/Turing-Online-Safety-Codebase/nodality
11

[Beguerisse-D ´ ıaz et al., 2014] Beguerisse-D ´ ıaz, M., Garduno-Hern´ andez, G., Vangelov, B., Yaliraki,
S. N., and Barahona, M. (2014). Interest communities and flow roles in directed networks: the
twitter network of the uk riots. Journal of The Royal Society Interface , 11(101):20140940.
[Berger and Goldstein, 2021] Berger, M. and Goldstein, E. (2021). Increasing sentence-level compre-
hension through text classification of epistemic functions. null.
[Blundell et al., 2022] Blundell, R., Costa Dias, M., Cribb, J., Joyce, R., Waters, T., Wernham, T.,
and Xu, X. (2022). Inequality and the COVID-19 Crisis in the United Kingdom. Annual Review of
Economics, 14(1):607–636. eprint: https://doi.org/10.1146/annurev-economics-051520-030252.
[Boukari and Devakumar, 2024] Boukari, Y. and Devakumar, D. (2024). Far-right riots in the uk: the
culmination of years of rhetoric and policies. The Lancet, 404(10456):931.
[Bovet and Makse, 2019] Bovet, A. and Makse, H. A. (2019). Influence of fake news in Twitter during
the 2016 US presidential election. Nature Communications, 10(1):7. Publisher: Nature Publishing
Group.
[Bright, 2016] Bright, J. (2016). The Social News Gap: How News Reading and
News Sharing Diverge. Journal of Communication , 66(3):343–365. eprint:
https://onlinelibrary.wiley.com/doi/pdf/10.1111/jcom.12232.
[Bright, 2018] Bright, J. (2018). Explaining the Emergence of Political Fragmentation on Social Media:
The Role of Ideology and Extremism. Journal of Computer-Mediated Communication , 23(1):17–33.
[Bright et al., 2020] Bright, J., Hale, S., Ganesh, B., Bulovsky, A., Margetts, H., and Howard, P.
(2020). Does Campaigning on Social Media Make a Difference? Evidence From Candidate Use
of Twitter During the 2015 and 2017 U.K. Elections. Communication Research, 47(7):988–1009.
Publisher: SAGE Publications Inc.
[Castelnovo and Sorrentino, 2021] Castelnovo, W. and Sorrentino, M. (2021). The Nodality Discon-
nect of Data-Driven Government. Administration & Society , 53(9):1418–1442. Publisher: SAGE
Publications Inc.
[Castro-Gonzalez et al., 2024] Castro-Gonzalez, L., Chung, Y.-L., Kirk, H. R., Francis, J., Williams,
A. R., Johansson, P., and Bright, J. (2024). Cheap Learning: Maximising Performance of Language
Models for Social Data Science Using Minimal Data. ArXiv. arXiv:2401.12295 [cs].
[Chadha, 2022] Chadha, J. S. (2022). MONETARY AND FISCAL POLICY REDUX—THE MINI-
BUDGET. National Institute Economic Review , 262:1–7.
[Dhingra and Sampson, 2022] Dhingra, S. and Sampson, T. (2022). Expecting Brexit. Annual Review
of Economics, 14(1):495–519. eprint: https://doi.org/10.1146/annurev-economics-051420-104231.
[Diamond, 2023] Diamond, P. (2023). Post-Brexit challenges to the UK machinery of government in
an ‘Age of Fiasco’: the dangers of muddling through? Journal of European Public Policy, 0(0):1–24.
Publisher: Routledge eprint: https://doi.org/10.1080/13501763.2023.2225562.
[Dubois and Gaffney, 2014] Dubois, E. and Gaffney, D. (2014). The Multiple Facets of Influence:
Identifying Political Influentials and Opinion Leaders on Twitter. American Behavioral Scientist ,
58(10):1260–1277. Publisher: SAGE Publications Inc.
[Essaidi et al., 2020] Essaidi, A., Zaidouni, D., and Bellafkih, M. (2020). New method to measure the
influence of Twitter users. In 2020 Fourth International Conference On Intelligent Computing in
Data Sciences (ICDS) , pages 1–5.
[Esteve Del Valle and Borge Bravo, 2018] Esteve Del Valle, M. and Borge Bravo, R. (2018). Leaders
or brokers? potential influencers in online parliamentary networks. Policy & Internet , 10(1):61–86.
eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1002/poi3.150.
12

[Flamino et al., 2023] Flamino, J., Galeazzi, A., Feldman, S., Macy, M. W., Cross, B., Zhou, Z.,
Serafino, M., Bovet, A., Makse, H. A., and Szymanski, B. K. (2023). Political polarization of news
media and influencers on Twitter in the 2016 and 2020 US presidential elections. Nature Human
Behaviour, 7(6):904–916. Publisher: Nature Publishing Group.
[Francis-Devine et al., 2022] Francis-Devine, B., Bolton, P., Keep, M., and Harari, D. (2022). Rising
cost of living in the UK . House of Commons Library.
[Fries et al., 2021] Fries, J. A., Steinberg, E., Khattar, S., Fleming, S. L., Posada, J., Callahan, A., and
Shah, N. H. (2021). Ontology-driven weak supervision for clinical entity classification in electronic
health records. Nature Communications , 12(1):2017. Number: 1 Publisher: Nature Publishing
Group.
[Gorrell et al., 2020] Gorrell, G., Bakir, M., Roberts, I., Greenwood, M., and Bontcheva, K. (2020).
Which politicians receive abuse? four factors illuminated in the UK general election 2019. EPJ
Data Science, 9.
[Graham et al., 2015] Graham, M. W., Avery, E. J., and Park, S. (2015). The role of social media in
local government crisis communications. Public Relations Review , 41(3):386–394.
[Graham et al., 2013] Graham, T., Broersma, M., Hazelhoff, K., and van ’t Haar, G. (2013). Between
Broadcasting Political Messages and Interacting with Voters. Information, Communication & Soci-
ety, 16(5):692–716. Publisher: Routledge eprint: https://doi.org/10.1080/1369118X.2013.785581.
[Harari et al., 2022] Harari, D., Francis-Devine, B., Bolton, P., and Keep, M. (2022). Rising cost of
living in the UK . House of Commons Library.
[Harris et al., 2024] Harris, M. J., Murtfeldt, R., Wang, S., Mordecai, E. A., and West, J. D. (2024).
Perceived experts are prevalent and influential within an antivaccine community on twitter. PNAS
nexus, 3(2):pgae007.
[Hood, 1983] Hood, C. C. (1983). The Tools of Government . Macmillan Education UK, London.
[Hood and Margetts, 2008] Hood, C. C. and Margetts, H. Z. (2008). The Tools of Government in the
Digital Age . Palgrave Macmillan.
[Howlett, 2009] Howlett, M. (2009). Government Communication as a Policy Tool: A Framework for
Analysis. Canadian Political Science Review , 3(2):23–37. Number: 2.
[Howlett, 2022] Howlett, M. (2022). Information as a Policy Tool: The Role of Government Commu-
nication. In The Routledge Handbook of Policy Tools . Routledge. Num Pages: 11.
[Jain, 2021] Jain, N. (2021). Customer sentiment analysis using weak supervision for customer-agent
chat. arXiv: Computation and Language .
[Jim´ enez-Zafra et al., 2021] Jim´ enez-Zafra, S. M., S´ aez-Castillo, A. J., Conde-S´ anchez, A., and
Mart ´ ın-Valdivia, M. T. (2021). How do sentiments affect virality on twitter? Royal Society Open
Science, 8(4):201756.
[Jungherr, 2014] Jungherr, A. (2014). Twitter in Politics: A Comprehensive Literature Review.
[Kim and Park, 2012] Kim, M. and Park, H. W. (2012). Measuring Twitter-based political partic-
ipation and deliberation in the South Korean context by using social network and Triple Helix
indicators. Scientometrics, 90(1):121–140.
[Kleinberg, 1999] Kleinberg, J. M. (1999). Authoritative sources in a hyperlinked environment. Journal
of the ACM , 46(5):604–632.
[Kolic et al., 2022] Kolic, B., Aguirre-L´ opez, F., Hern´ andez-Williams, S., and Gardu˜ no-Hern´ andez, G.
(2022). Quantifying the structure of controversial discussions with unsupervised methods: a look
into the Twitter climate change conversation. arXiv:2206.14501 [cs].
13

[Li et al., 2024] Li, Q., King, B. G., and Uzzi, B. (2024). Quantifying social media predictors of
violence during the 6 january us capitol insurrection using granger causality. Journal of the Royal
Society Interface, 21(220):20240314.
[Li, 2023] Li, Y. Y. (2023). Britain’s economic crisis in Mini-budget perspective. Academic Journal of
Management and Social Sciences , 2(1):1–5. Number: 1.
[Liadze et al., 2023] Liadze, I., Macchiarelli, C., Mortimer-Lee, P., and Juanino, P. S. (2023). Economic
costs of the Russia-Ukraine war. The World Economy , 46(4):874–886. Publisher: John Wiley &
Sons, Ltd.
[Mallory et al., 2020] Mallory, E. K., de Rochemonteix, M., Ratner, A., Acharya, A., R´ e, C., Bright,
R. A., and Altman, R. B. (2020). Extracting chemical reactions from text using snorkel. BMC
Bioinformatics.
[Maresca et al., 2021] Maresca, F., Solmaz, G., and Cirillo, F. (2021). Ontoaugment: Ontology match-
ing through weakly-supervised label augmentation. null.
[Margetts et al., 2019] Margetts, H., Hale, S., and John, P. (2019). Political Turbulence: How Social
Media Shapes Political Participation and the Democratic Landscape. In Graham, M. and Dutton,
W. H., editors, Society and the Internet: How Networks of Information and Communication are
Changing Our Lives , page 0. Oxford University Press.
[Margetts and John, 2023] Margetts, H. and John, P. (2023). How rediscovering nodality can im-
prove democratic governance in a digital world. Public Administration , n/a(n/a). eprint:
https://onlinelibrary.wiley.com/doi/pdf/10.1111/padm.12960.
[Margetts and Escher, 2006] Margetts, H. Z. and Escher, T. (2006). Governing from the Centre?
Comparing the Nodality of Digital Governments.
[Mbah and Wasum, 2022] Mbah, R. E. and Wasum, F. (2022). Russian-Ukraine 2022 War: A Review
of the Economic Impact of Russian-Ukraine Crisis on the USA.Advances in Social Sciences Research
Journal, 9:144–153.
[Mei et al., 2015] Mei, Y., Zhong, Y., and Yang, J. (2015). Finding and Analyzing Principal Features
for Measuring User Influence on Twitter. In 2015 IEEE First International Conference on Big Data
Computing Service and Applications , pages 478–486.
[Meraz, 2009] Meraz, S. (2009). Is there an elite hold? traditional media to social media agenda setting
influence in blog networks. Journal of computer-mediated communication, 14(3):682–707.
[Mosleh et al., 2024] Mosleh, M., Cole, R., and Rand, D. G. (2024). Misinformation and harmful
language are interconnected, rather than distinct, challenges. PNAS Nexus , 3(3):pgae111.
[Mosleh and Rand, 2022] Mosleh, M. and Rand, D. G. (2022). Measuring exposure to misinformation
from political elites on Twitter. Nature Communications, 13(1):7144. Number: 1 Publisher: Nature
Publishing Group.
[No˙ zewski and Baranowski, 2021] No˙ zewski, J. and Baranowski, P. (2021). “Birds of a Feather Flock
Together” : Bipolarity, Homophily and Intra-Party Communication Degree of Polish MPs on Twit-
ter. Athenaeum Polskie Studia Politologiczne , 72(4):7–28.
[Parmelee, 2013] Parmelee, J. H. (2013). Political journalists and Twitter: Influences on norms
and practices. Journal of Media Practice , 14(4):291–305. Publisher: Routledge eprint:
https://doi.org/10.1386/jmpr.14.4.291 1.
[Petricek et al., 2006] Petricek, V., Escher, T., Cox, I. J., and Margetts, H. (2006). The web structure
of e-government - developing a methodology for quantitative evaluation. In Proceedings of the 15th
international conference on World Wide Web , WWW ’06, pages 669–678, New York, NY, USA.
Association for Computing Machinery.
14

[Ratner et al., 2019] Ratner, A., Hancock, B., Dunnmon, J., Sala, F., Pandey, S., and R´ e, C. (2019).
Training complex models with multi-task weak supervision. Proceedings of the AAAI Conference
on Artificial Intelligence. AAAI Conference on Artificial Intelligence , 33:4763–4771.
[Rezaie et al., 2020] Rezaie, B., Zahedi, M., and Mashayekhi, H. (2020). Measuring time-sensitive user
influence in Twitter. Knowledge and Information Systems , 62(9):3481–3508.
[Riquelme and Gonz´ alez-Cantergiani, 2016] Riquelme, F. and Gonz´ alez-Cantergiani, P. (2016). Mea-
suring user influence on Twitter: A survey. Information Processing & Management , 52(5):949–975.
[Romenskyy et al., 2018] Romenskyy, M., Spaiser, V., Ihle, T., and Lobaskin, V. (2018). Polarized
ukraine 2014: opinion and territorial split demonstrated with the bounded confidence xy model,
parametrized by twitter data. Royal Society open science , 5(8):171935.
[Schreiber, 2000] Schreiber, T. (2000). Measuring Information Transfer. Physical Review Letters ,
85(2):461–464. Publisher: American Physical Society.
[Shapiro and Hemphill, 2017] Shapiro, M. and Hemphill, L. (2017). Politicians and the Policy Agenda:
Does Use of Twitter by the U.S. Congress Direct New York Times Content? Policy and Internet ,
9:109–132.
[Shearing and Wood, 2003] Shearing, C. and Wood, J. (2003). Nodal Governance, Democ-
racy, and the New ‘Denizens’. Journal of Law and Society , 30(3):400–419. eprint:
https://onlinelibrary.wiley.com/doi/pdf/10.1111/1467-6478.00263.
[Shu et al., 2021] Shu, K., Zheng, G., Li, Y., Mukherjee, S., Awadallah, A. H., Peter, B., Ruston,
S., Ruston, S. W., and Liu, H. (2021). Early detection of fake news with multi-source weak social
supervision. null.
[Silva et al., 2022] Silva, C. A. O., Gonzalez-Otero, R., Bessani, M., Mendoza, L. M. O., Otero, L.,
and de Castro, C. L. (2022). Interpretable risk models for sleep apnea and coronary diseases from
structured and non-structured data. Expert Systems With Applications .
[Sprejer et al., 2022] Sprejer, L., Margetts, H., Oliveira, K., O’Sullivan, D. J., and Vidgen, B.
(2022). An actor-based approach to understanding radical right viral tweets in the UK. Jour-
nal of Policing, Intelligence and Counter Terrorism , 0(0):1–19. Publisher: Routledge eprint:
https://doi.org/10.1080/18335330.2022.2086440.
[Stafford et al., 2024] Stafford, R., Alexander, J., Axon, S., Boakes, Z., Cantarello, E., Croker, A.,
Cvitanovi´ c, M., Almela, V. D., Ginige, T., Harris, N., et al. (2024). 2024 uk general election
manifesto commitments: implications for the economy, environment, and society.
[Steinberg et al., 2016] Steinberg, A., Wukich, C., and Wu, H.-C. (2016). Central social media actors
in disaster information networks. International Journal of Mass Emergencies & Disasters , 34(1):47–
74.
[Tosun and Lucey, 2023] Tosun, O. K. and Lucey, B. (2023). Growth . . . What growth? Finance
Research Letters, 52:103594.
[Usherwood and Wright, 2017] Usherwood, S. and Wright, K. A. (2017). Sticks and stones: Comparing
Twitter campaigning strategies in the European Union referendum. The British Journal of Politics
and International Relations . Publisher: SAGE PublicationsSage UK: London, England.
[Zhang et al., 2023] Zhang, M., Zhang, D., Zhang, Y., Yeager, K., and Fields, T. N. (2023). An
exploratory study of Twitter metrics for measuring user influence. Journal of Informetrics ,
17(4):101454.
15
