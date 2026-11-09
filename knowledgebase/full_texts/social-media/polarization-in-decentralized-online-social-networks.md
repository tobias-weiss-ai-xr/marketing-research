---
title: Polarization in Decentralized Online Social Networks
url: https://arxiv.org/abs/2312.05668
category: social-media
subcategory: empirical
date: 2023-12
venue: ''
authors:
- Lucio La Cava
- Domenico Mandaglio
- Andrea Tagarelli
source: arxiv
pdf_url: https://arxiv.org/pdf/2312.05668
pages: 5
chars: 31163
fetched_at: '2026-11-08T13:12:06+00:00'
kb_version: 1
---

# Polarization in Decentralized Online Social Networks

Polarization in Decentralized Online Social Networks
Lucio La Cava
DIMES Dept., University of Calabria
Rende, Italy
lucio.lacava@dimes.unical.it
Domenico Mandaglio
DIMES Dept., University of Calabria
Rende, Italy
d.mandaglio@dimes.unical.it
Andrea Tagarelli
DIMES Dept., University of Calabria
Rende, Italy
andrea.tagarelli@unical.it
ABSTRACT
Centralized social media platforms are currently experiencing a
shift in user engagement, drawing attention to alternative paradigms
like Decentralized Online Social Networks (DOSNs). The rising pop-
ularity of DOSNsfinds its root in the accessibility of open-source
software, enabling anyone to create a new instance (i.e., server)
and participate in a decentralized network known as Fediverse.
Despite this growing momentum, there has been a lack of studies
addressing the effect of positive and negative interactions among
instances within DOSNs. This work aims tofill this gap by present-
ing a preliminary examination of instances’ polarization in DOSNs,
focusing on Mastodon — the most widely recognized decentralized
social media platform, boasting over 10M users and nearly 20K
instances to date. Our results suggest that polarization in the Fedi-
verse emerges in unique ways, influenced by the desire to foster
a federated environment between instances, also facilitating the
isolation of instances that may pose potential risks to the Fediverse.
KEYWORDS
Fediverse, Polarization, Mastodon, Signed Network
1 INTRODUCTION
Centralized social media platforms are nowadays facing a trans-
formative shift, pushing users to seek new social interaction cues.
In this regard, an increasing number of users are turning their
attention toward alternative paradigms, with Decentralized On-
line Social Networks (DOSNs) [ 8, 11] emerging as prominent con-
tenders [13, 15, 19].
The allure of DOSNs relies upon the availability of open-source
software, allowing individuals to createinstances(i.e., servers) and
seamlessly interact with other instances, similarly to email services,
in a decentralized network known as theFediverse.
Among the plethora of decentralized services developed in recent
years, Mastodon stems as the most widely recognized and studied [3,
23, 24, 26, 27] decentralized social media, boasting a user base
exceeding 10M and nearly 20K instances to date, thus serving as
the best representative for delving into the Fediverse.
The steady growth of Mastodon users has fostered the prolifer-
ation of social interactions that are articulated on two relational
fronts: interactions among users spread across different instances,
and interactions among instances deriving from the former. Exist-
ing studies mainly focused on characterizing the typical relational
front, i.e., those among users. In this regard, the followers-followee
distribution on Mastodon is found to be more balanced than on
Twitter [27], with a lower presence of social bots and unusual dis-
assortative traits. The impact of decentralization of user relations
has been also investigated, unveiling the emergence of strategic
user roles [ 21] and characterizing the information consumption-
production dichotomy in such a novel social context [ 22]. Con-
versely, the novel relational front among instances has been little
investigated, with the unveiling and characterization of the struc-
tural footprint of the network of Mastodon instances [20].
However, despite such a body of studies has provided consider-
able insights into the decentralized social ecosystem, the seman-
tics associated with relationships — being them among users or
instances — was overlooked. Indeed, users establishpositiverela-
tionships such as friendships, agreements, and supports, as well as
negativerelationships such as foes, disagreements, and distrust. The
existence of such mixed interactions has led to an ever-growing
polarizationphenomenon, i.e., a division of the set of users into
groups with opposite views on controversial topics (e.g., politics,
religion, sport).
In the past few years, we have witnessed a plethora of studies
about user polarization on social media [ 5, 6, 9, 10, 14, 17]. Interest-
ingly, in DOSNs, we can also witness instances establishing positive
relationships — which involve cooperation among servers, shared
topics, common language, etc. — and negative relationships, such
as those involving banning, blocking, moderation. Consequently,
the phenomenon of polarization on a DOSN like Mastodon extends
beyond individual users, manifesting at the instance level as well.
To date, however, the exploration of polarization phenomena,
both at the user and instance level within DOSNs remains an under-
researched area, lacking comprehensive analysis or empirical in-
vestigation. Understanding polarization in Mastodon is crucial as it
reveals how communities form and interact within decentralized
networks, guiding interventions to foster healthier online environ-
ments and mitigate negative effects on user experience.
Contributions.This work aims to address the aforementioned
gap in the literature by conducting thefirst investigation of the
polarization phenomena at the instance level within Mastodon. The
choice to focus on instances is all but arbitrary, as gaining a macro-
perspective of the polarization within Fediverse serves as a key
precursor for the user level, yet still bears significant implications
for the underlying user base.
To characterize polarization in DOSNs, we aim to answer the
following research questions:
(RQ1)How many polarized groups can be found in Mastodon?
(RQ2) What is the polarization structure in Mastodon, that is, how
are polarized groups linked internally and to each other?
(RQ3) What are the main characteristics of the instances within
the detected polarized groups?
To answer the above RQs, our approach is built on ( 𝑖) model-
ing the interactions among Mastodon instances throughsigned
graphswhere edges are labeled positively or negatively, indicating
whether the connection they represent is friendly or antagonistic,

Conference’17, July 2017, Washington, DC, USA La Cava et al.
respectively, and (𝑖𝑖) adopting existing methodologies for detecting
polarization phenomena on signed graphs.
Our methodology builds on the body of studies formulating the
problem of detecting polarization as partitioning the node set in a
signed graph into 𝑘 non-overlapping sets, generally referred to as
groups or poles, of the input signed graph [ 4, 7, 18]. In particular,
following previous methods [2, 25], we recognize that the identified
groups do not necessarily need to cover the entire node set, thus
complying the most with real-world situations allowing neutrality.
2 DATA
Due to Mastodon’s decentralized and scattered footprint, identify-
ing the plethora of currently existing instances is a complex task.
However, for obtaining the latest information about the Mastodon
instance landscape, the instances.social1 website is widely uti-
lized as a de-facto tracker. To start building our data, we leveraged
this platform to compile a seed set of instances to investigate, cor-
responding to those active at the time of writing this work. We
thus explored such instances to define a seed set of around 270K
Mastodon users.
Subsequently, we conducted abreadth-firstsearch over them,
identifying both incoming and outgoing links (via the/api/v1/acco
unts/:id/followers and /api/v1/accounts/:id /following end-
points). As part of this process, already having been proven mean-
ingful in [ 20], we systematically expanded the user exploration
by incrementally discovering new users through the link detec-
tion mechanism. We let this crawling process go for the past nine
months and eventually came up with more than 2M users and 116M
unique links among them.
To the aim of our work, we used the following relations to infer
thepositive links among instances, deriving from social interac-
tions between their users, as outlined in the following section.
Furthermore, to define thenegative links among instances,
we leveraged the /api/v1/instance/domain_blocks endpoint,
which enables the detection of the set of moderated instances
through a list ofDomainBlocksobjects, 2 i.e., JSONfiles contain-
ing blocked instances and associated metadata (e.g., the severity
and motivation of the block). We crawled blocked domains from
our seed set of instances between July and November, obtaining
more than 135K raw enforced blocks among instances.
We emphasize that according to the concept of federation un-
derlying DOSNs, Mastodon users, and hence their instances, can
engage seamlessly with other services in the Fediverse that adopt
the same protocol (i.e.,ActivityPub). Consequently, our crawled
links also encompass interactions from/to other services within the
Fediverse (e.g., Pleroma). However, these might provide valuable
insights into ourfirst exploration of polarization within DOSNs,
and to this aim, we have chosen not tofilter them out.
3 METHODOLOGY
Network Modeling.Let us denote with U the set of users and I
the set of instances extracted from our data. We can infer a graph
modeling positive relations among instances in I as a directed-
weighted network G+ =⟨𝑉 +,𝐸 +,𝑤⟩ , where 𝑉 + ⊆I is the set of
1https://instances.social/
2https://docs.joinmastodon.org/entities/DomainBlock/
nodes, 𝐸+ is the set ofpositiveedges such that (𝑖,𝑗)∈𝐸 + means
that there exists at least one user in instance 𝑖 that follows a user
in instance 𝑗, and 𝑤 : 𝐸+ ↦→R is an edge weighing function such
that, for any (𝑖,𝑗)∈𝐸 +, 𝑤(𝑖,𝑗) indicates the number of users from
instance 𝑖 following users in instance 𝑗. Our network G+ contains
37,529 nodes and 1,335,490 edges. Similarly, we infer a graph model-
ing negative relations among instances in I as a directed network
G− =⟨𝑉 −,𝐸 − ⟩, where 𝑉 − ⊆I is the set of nodes, 𝐸− is the set of
negativeedges such that (𝑖,𝑗)∈𝐸 − means that instance 𝑖 banned
instance 𝑗 during our crawling period. Our network G− contains
11,401 nodes and 105,465 edges.
Before shaping our signed graph model for identifying polarized
groups within Mastodon and the broadest Fediverse, we conducted
anetwork simplification taskaimed at pruning noisy or statistically
irrelevant edges from our G+. Indeed, 𝐸+ might also contain inter-
actions among instances that are driven by spurious interactions
by a pair of users within such instances. This is all but desirable, as
it would impact our identification step. Therefore, we resorted to
the theoretically well-rootedDisparity Filter[ 28] method, which
exploits agenerative null modelbuilt on node strengths to prune
networks from statistically irrelevant edges based on 𝑝-value com-
putation and specific significance thresholds. Specifically, the null
hypothesis underlying the Disparity Filter states that the strength
of a node is redistributed uniformly at random over its incident
edges, thus evaluating the strength and degree of each node locally.
We utilized the official Python implementation of Disparity Fil-
ter,3 tofilter 𝐺+ removing irrelevant edges based on a significance
threshold of 𝛼= 0.05. This eventually results in a set of 117,422
edges in 𝐸+. By contrast, we point out that the simplification step
is not required for G− , as blocks among instances are explicitly
declared by instances’ administrators and not due to randomness.
Finally, we created oursigned instance-network G=⟨𝑉,𝐸,𝑠⟩ ,
where 𝑉⊆I , 𝐸=𝐸 + ∪𝐸 − , and 𝑠 : 𝐸↦→{+ 1,− 1} is a func-
tion that assigns each edge (𝑖,𝑗)∈𝐸 to the corresponding sign,
such that 𝑤(𝑖,𝑗)=+ 1 if (𝑖,𝑗)∈𝐸 +, −1 otherwise. Our network G
contains contains 19,738 nodes (i.e., instances) and 222,887 (posi-
tive/negative) relations among them. We emphasize that, during
this merging step, we also accounted for the removal of ambiguous
links, i.e., those existing with both signs due to the existence of
a subsequent ban enforced toward instances already spotted as
“positive” during our breadth-first search.
Identification of Polarized Groups.Let 𝐸+ (𝑃𝑖 ,𝑃 𝑗 ) (resp. 𝐸− (𝑃𝑖 ,𝑃 𝑗 ))
be the set of positive (resp. negative) edges between two subsets
𝑃𝑖 ,𝑃 𝑗 ⊆𝑉 . We define 𝐸+ (𝑃𝑖 ) (resp. 𝐸− (𝑃𝑖 )) to be 𝐸+ (𝑃𝑖 ,𝑃 𝑖 ) (resp.
𝐸− (𝑃𝑖 ,𝑃 𝑖 )) as the set of positive (resp. negative) intra-group edges,
for any 𝑃𝑖 ⊆𝑉 . For a set of groups P={𝑃 1,· · ·,𝑃 𝑘 } as a candidate
solution, [25] quantifies the goodness of the solution by maximizing
a function of the intra/inter-group connectivity as follows:
𝑓(𝑃 1,· · ·,𝑃 𝑘 )=
∑︁
𝑃𝑖 ∈P

|𝐸+ (𝑃𝑖 )|−|𝐸 − (𝑃𝑖 )| 
+ 1 𝑘−1 ∑︁ 𝑃𝑖 ,𝑃𝑗 ∈P  |𝐸 − (𝑃𝑖 ,𝑃 𝑗 )|−|𝐸 + (𝑃𝑖 ,𝑃 𝑗 )|  .
3https://github.com/malcolmvr/backbone_network

Polarization in Decentralized Online Social Networks Conference’17, July 2017, Washington, DC, USA
It should be noted that the approach proposed in [ 25] is, to the
best of our knowledge, the only existing method discovering an
arbitrary number 𝑘 of polarized groups that admitsneutral nodes,
i.e., nodes that are not assigned to any of the polarized groups.
The latter is an essential requirement to our problem under study,
which significantly differs from conventional community detection
and graph clustering problems. Please also note that comparing
different algorithms for detecting polarized groups on Mastodon is
beyond the scope of this work.
The identification of polarized groups is based on the following
optimization problem, which is a special instance of the correlation
clustering problem [1].
Problem1 (k-conflicting groups[ 25]).Given a signed graph G
and an integer k,find k mutually-disjoint node sets P={𝑃 ∗ 1 ,· · ·,𝑃 ∗ 𝑘 }
such that:
𝑃∗ 1 ,· · ·,𝑃 ∗ 𝑘 =arg max 𝑃1,···,𝑃 𝑘 ⊆𝑉 𝑓(𝑃 1,· · ·,𝑃 𝑘 )

 ∪𝑘 𝑖=1 𝑃𝑖

 (1)
Under the formulation of Problem 1, the quality of the solution
depends only on the polarized groups, and not on the neutral group
𝑃𝑁 =𝑉\∪ 𝑘 𝑖=1 𝑃𝑖 , which fulfills the above stated requirement. The
proposed approach in [ 25] relies on interpreting the problem objec-
tive in terms of the Laplacian of a complete graph, characterizing
the spectral properties of this matrix, and identifying each conflict-
ing group as the solution to a maximumDiscrete Rayleigh Quotient
(DRQ) problem [ 25]. More specifically, the objective function in
Eq. 1 is found in [ 25] as a convex combination of 𝑘− 1 DRQ prob-
lems, whose solution to the 𝑖-th DRQ problem characterizes the
group 𝑃𝑖 that conflicts the most with the remaining groups 𝑃𝑗 , for
𝑗>𝑖 , yet to be investigated. The intensity of such conflict, char-
acterizing group 𝑃𝑖 , is referred to as theDRQ value. This value,
having similar rationale to Eq. 1, should be maximized. Based on
this observation, [ 25] proposes an iterative algorithm, dubbed SCG
(Spectral Conflicting Groups), executing 𝑘− 1 iterations that involve
solving a DRQ problem.
4 RESULTS
Determining the number of polarized groups 𝑘.We adopted
the heuristic proposed in [ 25], which is analogous to the “elbow”
heuristic for 𝑘-means-like clustering methods. This involves the
following steps: (𝑖) executing the SCG method by different 𝑘 values,
(𝑖𝑖) producing a plot of the DRQ values from each run, arranged
in ascending order, plotting the 𝑖-th largest DRQ value at the 𝑖-th
position, and (𝑖𝑖𝑖 ) determining 𝑘 to be one of the discernible “knees”
on the resulting curve. We employed this heuristic by varying 𝑘
from 2 to 10 by increments of 1. For each 𝑘 value, we executed SCG
10 times and averaged the results, which are shown in Figure 1.
Our analysis indicates the presence of 4 conflicting groups in
our signed instance-network, as the most distinct inflection point
emerges during the 3rd iteration for multiple 𝑘 values. However,
running SCG with 𝑘= 4 resulted in one empty polarized group,
leaving us with 3 actual polarized groups that, alongside the neutral
group𝑃 𝑁 , will be the focus of our subsequent analysis.
Characterizing main traits of the polarized groups.We started
gaining insights into the obtained polarized groups by means of
the statistics shown in Figure 2 (top-left). Groups are all but evenly
� � � � � � � � �
������������
�
��
��
��
��
���
���
���
������������
�� �
�� �
�� �
�� �
�� �
�� �
�� �
�� �
�� ��
Figure 1: DRQ plot from SCG runs by varying𝑘.
distributed, as the neutral group (or pole) 𝑃𝑁 encompasses more
than 97% of the instances in our signed instance-network. This
predominance of neutral instances perfectly aligns with the idea of
Fediverse, supporting the co-existence of independent yet cooperat-
ing instances. Nonetheless, as previously mentioned, the Fediverse
embraces multiple services, and we found evidence of such a feature
in our groups. Indeed, while we spotted some almostMastodon-
puregroups (i.e., the non-neutral 𝑃1 and 𝑃3), the remainder (i.e., the
neutral 𝑃𝑁 and the non-neutral 𝑃2) are characterized by a fraction
of Mastodon instances that does not exceed half of the group.
We also investigated the extent of “negative” edges (i.e., mod-
eration actions) toward our spotted polarized groups, discovering
that 𝑃𝑁 and 𝑃2 stem as the groups collecting more bans within the
Fediverse. However, while delving into the average number of bans
within each group, we found that 𝑃1 and 𝑃3 receive a very small
amount of bans, whereas the neutral group 𝑃𝑁 almost doubles the
bans of the former groups, despite remaining on admissible values.
Remarkably, the group 𝑃2 emerges with a striking number of bans,
which is almost 16𝑥, resp. 26𝑥, the average amount of received bans
by 𝑃𝑁 , resp. 𝑃1 and 𝑃3, hence stemming as theban-sinkpole of
the Fediverse. Further confirmation of this trait emerges from the
percentage of instances having received at least a ban within each
pole: in fact, while the neutral and Mastodon-pure poles present
a percentage of instances with at least one ban not exceeding half
of the entire group (and in the best case, a quarter), the ban-sink
pole 𝑃2 stands out with a remarkable trait, with all encompassed
instances having received at least a ban.
Exploring relations between the polarized groups.Once we
identified the poles in the Fediverse, we focused on shaping the
positiveflows (i.e., interactions) and negativeflows (i.e., bans) be-
tween their instances. As illustrated in Figure 2 (center), we observe
that most interactions involve or are directed to the neutral group
𝑃𝑁 , further corroborating the idea of neutrality that, in princi-
ple, characterizes the Fediverse. The remainder is split toward the
Mastodon-pure groups, while the ban-sink one only receives inter-
actions from itself. This isolation from interactions that characterize
𝑃2 hints at a form of segregation toward its negative shade.
As concerns the negativeflows, shown in Figure 2 (right), we
unveiled an intriguing bipartite mode as bans appear to be split
between 𝑃𝑁 and 𝑃2. While the high number of incoming bans in the
neutral group is affected by its large size, this does not hold for the
ban-sink one, which appears once again to be segregated within the

Conference’17, July 2017, Washington, DC, USA La Cava et al.
𝑃𝑁 𝑃1 𝑃2 𝑃3
# Instances 19,241 189 122 186
% Mastodon 43.6 92.6 36.1 91.4
# Incoming bans 79,690 728 24,651 396
Avg. # bans 12.94 7.35 202.06 7.62
% Instances≥1 ban 32.0 52.4 100 28.0
Most interacted Most banned
𝑃𝑁 mstdn.jp geofront.rocks
𝑃1 mastodon.social botsin.space
𝑃2 pawoo.net poa.st
𝑃3 det.social aethy.com
Figure 2: (Top-left) Main characteristics of the polarized groups. (Bottom-left) Most interacted and banned instances for each
group. (Center/Right) Positive/Negativeflows of interaction among groups. Normalized percentages are to be read row-wise.
Volume Avg Top-active Instance % Volume
𝑃𝑁 2.37×10 7 3,654 mstdn.jp7.65%
𝑃1 2.36×10 7 139,511 mastodon.social32.84%
𝑃2 1.74×10 6 158,065 pawoo.net54.55%
𝑃3 2.38×10 6 14,356 mstdn.ca15.19%
Table 1: Pole activity (i.e., created posts) in the last 12 weeks,
and corresponding most active instance.
Fediverse. As a side yet relevant remark, while the Mastodon-pure
group 𝑃1 almost does not receive bans, 𝑃3 receives almost half of
the bans enforced from𝑃 2, warranting further exploration.
Unveiling main representative instances in polarized groups.
To further shed light on the group division that emerged above,
we delved into each pole to unveil the most representative in-
stances. Figure 2 (bottom-left) summarizes the most interacted,
resp. banned, instances obtained through the in-strength of the
positive edges, resp. in-degree of the negative ones. Below we dis-
cuss the most interesting instances we spotted. As concerns the
neutral 𝑃𝑁 , mstdn.jp emerges as the instance receiving the most
positive interactions; this is not surprising as it turns out to be one
of the earliest instances embracing the Mastodon rise, as well as the
second largest Japanese instance in the Fediverse. The Mastodon-
pure group 𝑃1 sees mastodon.social as the most relevant positive
instance, i.e., the official andfirst instance of the Mastodon project,
whereas botsin.space arises as the most banned. For the latter,
the reason is self-explanatory, as it hosts and runs Mastodon bots.
Valuable insights emerge from the ban-sink group 𝑃2. Indeed, the
most interacted instance turns out to be pawoo.net, i.e., the second
largest Mastodon instance in terms of users, recently under the
spotlight due to the hosting of controversial content. The most
banned instance in 𝑃2 is poa.st, a non-Mastodon instance that
advertises itself as the “Fediverse for shitposters”, 4 further corrobo-
rating the negative connotation of that group of instances. Finally,
another noteworthy trait involves the most banned instance in 𝑃3,
namelyaethy.com, a server hosting potentially NSFW content.
Activity in polarized groups.We also characterized polarized
groups in terms of activity via the /api/v1/instance/activity
4https://globalextremism.org/post/poast/
endpoint of the Mastodon API, by collecting for each pole, the
number of statuses created in the last 12 weeks (up to the time of
writing this paper). As reported in Table 1, despite the large volume
produced from all groups, two of them stand out, namely the neu-
tral 𝑃𝑁 and the Mastodon-pure 𝑃1. Nonetheless, the disparity in the
average number of posts per instance within each group suggests
the presence of a large tail of small instances within 𝑃𝑁 , and iden-
tifies 𝑃1 as the “beating core” of the Fediverse, as further confirmed
by the presence of mastodon.social as the most prolific instance,
covering one-third of the entire statuses created in 𝑃1. Notably, the
high average number of posts produced in the group 𝑃2, coupled
with the dominant role of pawoo.net (i.e., the instance producing
more than half of the content) demand further investigation for
unveiling the roots of such anomaly.
To this aim, we analyzed the most frequently used keywords for
banning instances within our identified groups. As illustrated in
Figure 3, and matching our previous insights from Figure 2 (left)
witnessing the groups 𝑃1 and 𝑃3 as the least banned ones, we do not
spot particularly evident motivations in their bannings. Conversely,
valuable observations emerge from the remaining poles. Indeed, the
ban-sink 𝑃2 appears to be frequently banned for “speech” (hinting
at hate-speech), “racism”, and “harassment”, providing additional
shreds of evidence to our hypothesis of negativity. Finally, the most
used ban keywords toward the neutral pole fuel the idea of feder-
ation, as “fedi” and “federate” emerge, suggesting the willingness
to moderate instances that federate with unwelcome ones. The
case in point is the presence of “facebook/meta” among the top-5
keywords, as a result of the emergence ofThreads, the new social
platform by Meta, as a potential “threat” to the Fediverse, following
the desire to adopt the ActivityPub protocol. 5
5 DISCUSSION
We conceived a signed network model aimed at detecting polarized
groups in the Fediverse through the lens of Mastodon. Based on this
model, we carried out thefirst explorative analysis of polarization
phenomena among instances. Below we report the mainfindings
that emerged through answering our research questions:
5https://about.fb.com/news/2023/07/introducing-threads-new-app-text-sharing/

Polarization in Decentralized Online Social Networks Conference’17, July 2017, Washington, DC, USA
Figure 3: Top-5 most frequent ban reasons for each pole.
• (RQ1)The Mastodon-centric Fediverse instance network encom-
passes four non-overlapping groups of instances identified as poles.
• (RQ2)We unveil a unique polarization structure, featuring a
predominant neutral group encompassing also instances from other
services in the Fediverse, matching with the idea federation. The
remaining instances are divided into twoMastodon-puregroups and
aban-sinkgroup. Notably, positive interactions are predominantly
observed between the neutral and pure groups, while the ban-sink
group consistently receives negative links, as a protective measure
against potential harm to the Fediverse.
• (RQ3)The Mastodon-pure group containing the most representa-
tive instance of the Fediverse ( mastodon.social) and the neutral
group exceed the other two groups in terms of created content
volume. Besides, theban-sinkgroup exhibits anomalous trends in
content production, characterized by particularly strong modera-
tion due to the presence of harmful and inappropriate content.
Future work might delve into user-level polarization in DOSNs,
comparing different algorithms for identifying polarized groups
while also considering fairness aspects [12] and other ethical dimen-
sions [16] throughout the detection process of polarized groups.
REFERENCES
[1] Nikhil Bansal, Avrim Blum, and Shuchi Chawla. 2004. Correlation clustering.
Machine learning 56 (2004), 89–113.
[2] Francesco Bonchi, Edoardo Galimberti, Aristides Gionis, Bruno Ordozgoiti, and
Giancarlo Ruffo. 2019. Discovering polarized communities in signed networks.
In Proc. CIKM Conf. 961–970.
[3] Christophe Cerisara, Somayeh Jafaritazehjani, Adedayo Oluokun, and Hoa T.
Le. 2018. Multi-task dialog act and sentiment recognition on Mastodon. In Proc.
ACL Conf. 745–754.
[4] Kai-Yang Chiang, Joyce Jiyoung Whang, and Inderjit S Dhillon. 2012. Scalable
clustering of signed networks using balance normalized cut. In Proc. CIKM Conf.
615–624.
[5] M. Conover, J. Ratkiewicz, M. Francisco, B. Goncalves, F. Menczer, and A. Flam-
mini. 2011. Political polarization on Twitter. In Proc. ICWSM Conf. 89–96.
[6] M. Coscia and L. Rossi. 2022. How minimizing conflicts could lead to polarization
on social media: An agent-based model investigation. PLOS ONE 17 (2022),
e0263184.
[7] Mihai Cucuringu, Peter Davies, Aldo Glielmo, and Hemant Tyagi. 2019. SPONGE:
A generalized eigenproblem for clustering signed networks. In Proc. AISTATS
Conf. 1088–1098.
[8] Anwitaman Datta, Sonja Buchegger, Le-Hung Vu, Thorsten Strufe, and Krzysztof
Rzadca. 2010. Decentralized Online Social Networks. Springer US, Boston, MA,
349–378. https://doi.org/10.1007/978-1-4419-7142-5_17
[9] Kiran Garimella, Gianmarco De Francisci Morales, Aristides Gionis, and Michael
Mathioudakis. 2017. Reducing controversy by connecting opposing views. In
Proc. WSDM Conf. 81–90.
[10] Kiran Garimella, Gianmarco De Francisci Morales, Aristides Gionis, and Michael
Mathioudakis. 2018. Quantifying controversy on social media. TSC 1, 1 (2018),
1–27.
[11] Barbara Guidi, Marco Conti, Andrea Passarella, and Laura Ricci. 2018. Managing
social contents in Decentralized Online Social Networks: A survey. Online Social
Networks and Media 7 (2018), 12–29. https://doi.org/doi.org/10.1016/j.osnem.
2018.07.001
[12] Francesco Gullo, Lucio La Cava, Domenico Mandaglio, and Andrea Tagarelli.
2022. When Correlation Clustering Meets Fairness Constraints. In Proc. DS Conf.,
Vol. 13601. Springer, 302–317. https://doi.org/10.1007/978-3-031-18840-4_22
[13] Jiahui He, Haris Bin Zia, Ignacio Castro, Aravindh Raman, Nishanth Sastry, and
Gareth Tyson. 2023. Flocking to Mastodon: Tracking the Great Twitter Migration.
In Proc. IMC Conf. Association for Computing Machinery, New York, NY, USA,
111–123. https://doi.org/10.1145/3618257.3624819
[14] Marilena Hohmann, Karel Devriendt, and Michele Coscia. 2023. Quantifying ide-
ological polarization on a network using generalized Euclidean distance. Science
Advances 9, 9 (2023).
[15] Ujun Jeong, Ayushi Nirmal, Kritshekhar Jha, Xu Tang, H Russell Bernard, and
Huan Liu. 2023. User Migration across Multiple Social Media Platforms. arXiv
preprint arXiv:2309.12613 (2023).
[16] Anna Jobin, Marcello Ienca, and Effy Vayena. 2019. The global landscape of AI
ethics guidelines. Nature machine intelligence 1, 9 (2019), 389–399.
[17] Srijan Kumar, William L Hamilton, Jure Leskovec, and Dan Jurafsky. 2018. Com-
munity interaction and conflict on the Web. In Proc. WWW Conf. 933–943.
[18] Jérôme Kunegis, Stephan Schmidt, Andreas Lommatzsch, Jürgen Lerner, Ernesto
William De Luca, and Sahin Albayrak. 2010. Spectral Analysis of Signed Graphs
for Clustering, Prediction and Visualization. In Proc. SDM Conf. 559–570.
[19] Lucio La Cava, Luca Maria Aiello, and Andrea Tagarelli. 2023. Drivers of social
influence in the Twitter migration to Mastodon. Scientific Reports 13, 1 (2023),
21626. https://doi.org/10.1038/s41598-023-48200-7
[20] Lucio La Cava, Sergio Greco, and Andrea Tagarelli. 2021. Understanding the
growth of the Fediverse through the lens of Mastodon. Appl. Netw. Sci. 6, 1
(2021), 64. https://doi.org/10.1007/s41109-021-00392-5
[21] Lucio La Cava, Sergio Greco, and Andrea Tagarelli. 2022. Information con-
sumption and boundary spanning in Decentralized Online Social Networks: The
case of Mastodon users. Online Social Networks and Media 30 (2022), 100220.
https://doi.org/10.1016/j.osnem.2022.100220
[22] Lucio La Cava, Sergio Greco, and Andrea Tagarelli. 2022. Network Analysis of the
Information Consumption-Production Dichotomy in Mastodon User Behaviors.
Proc. ICWSM Conf. 16, 1 (May 2022), 1378–1382. https://doi.org/10.1609/icwsm.
v16i1.19391
[23] Aravindh Raman, Sagar Joglekar, Emiliano De Cristofaro, Nishanth Sastry, and
Gareth Tyson. 2019. Challenges in the Decentralised Web: The Mastodon Case.
In Proc. IMC Conf. 217–229. https://doi.org/10.1145/3355369.3355572
[24] Jan Trienes, Andrés Torres Cano, and Djoerd Hiemstra. 2018. Recommending
Users: Whom to Follow on Federated Social Networks. CoRR abs/1811.09292
(2018).
[25] Ruo-Chun Tzeng, Bruno Ordozgoiti, and Aristides Gionis. 2020. Discovering
conflicting groups in signed networks. Proc. NIPS Conf. 33 (2020), 10974–10985.
[26] Matteo Zignani, Sabrina Gaito, and Gian Paolo Rossi. 2018. Follow the “Mastodon”:
Structure and Evolution of a Decentralized Online Social Network. In Proc.
ICWSM Conf. AAAI Press, 541–551.
[27] Matteo Zignani, Christian Quadri, Sabrina Gaito, Hocine Cherifi, and Gian Paolo
Rossi. 2019. The Footprints of a “Mastodon”: How a Decentralized Architecture
Influences Online Social Relationships. In Proc. of the IEEE Conf. on Computer
Communications Workshops (INFOCOM WKSHPS). 472–477.
[28] M. Ángeles Serrano, Marián Boguñá, and Alessandro Vespignani. 2009. Extracting
the multiscale backbone of complex weighted networks. Proceedings of the
National Academy of Sciences 106, 16 (2009), 6483–6488. https://doi.org/10.
1073/pnas.0808904106
