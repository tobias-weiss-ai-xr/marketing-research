---
title: 'Digital Persuasion: Understanding the Impact of Online Influencers on Public Opinion'
url: https://arxiv.org/abs/2609.16062
category: social-media
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Omran Berjawi
- Rida Khatoun
- Giuseppe Fenza
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.16062
pages: 11
chars: 27119
fetched_at: '2026-11-08T13:12:22+00:00'
kb_version: 1
---

# Digital Persuasion: Understanding the Impact of Online Influencers on Public Opinion

Digital Persuasion: Understanding the Impact of
Online Influencers on Public Opinion
Omran Berjawi1[0009−0008−6763−9630], Rida Khatoun2[0009−0004−8282−136X], and
Giuseppe Fenza3[0000−0002−4736−0113]
1 IMT School for Advanced Studies Lucca, 55100 Lucca, LU, Italy,
omran.berjawi@imtlucca.it
2 Institut Polytechnique de Paris, 91120 Palaiseau, France
rida.khatoun@telecom-paris.fr
3 University of Salerno, 84084 Fisciano, SA, Italygfenza@unisa.it
Abstract.Thestudyingofopiniondynamicsanditspropagationwithin
social networks is crucial for addressing a wide range of challenges, in-
cluding political polarization, public health, and marketing strategies.
In this work, we study the problem of opinion dynamics by proposing a
framework based on Friedkin-Johnsen (FJ) to identifies influential users
and study their impact on dynamics opinions of community. The FJ
model assume each individual have two opinions: initial and expressed.
Through a series of initial opinion manipulation experiments, the pro-
posed framework assesses the impact of influential versus random users
on the overall community opinion. The proposed framework is validated
using a tweet dataset representing the U.S. presidential election. The re-
sults shows that influencers with highest influencing score, significantly
shift the overall community opinion. Moreover, the results shows that
the impact of influencers not limited to direct neighbors , but beyond
it, to their neighbors of neighbors . This study demonstrates how digital
influencers on social media can shape public opinion regarding a subject
or cause.
Keywords:Friedkin-Johnsen Model·Opinion Dynamics·Social Net-
works·Persuasion·Influencers·Sentiment Analysis.
1 Introduction
Social media platforms have grown tremendously and changed the way we com-
municate, exchange ideas, and form opinions. They have become a space through
which any individual can express their opinions on any issue and anywhere in
our world without any obstacles, which has led to their use as a sharpened tool
in various aspects, including political discourse, consumer behaviors, and public
health campaigns [11]. To understand the mechanisms of individuals’ opinion
formation and how it is reshaped, it is significant to understand the relation
between the intrinsic factors (e.g., pre-existing beliefs) and extrinsic influences
(e.g., influencers, and media exposure). An important factor in this relationship
arXiv:2609.16062v1  [cs.SI]  13 Sep 2026

2 Omran Berjawi, Rida Khatoun, and Giuseppe Fenza
is the role of influential users on reshaping opinions, and behaviors of their au-
dience within their networks [6]. For instance, celebrities can play a significant
role in public opinion during election campaigns. In the U.S. presidential elec-
tion of 2020, figures like Dwayne "The Rock" Johnson and Taylor Swift allocated
their platforms to promote voter participation and share their political beliefs.
In 2024, Taylor Swift and Jennifer Lopez have publicly endorsed Kamala Harris,
while Donald Trump has garnered support from prominent figures such as Elon
Musk, Kid Rock, and Hulk Hogan.
Various recent works have proposed various methods to identify influencers
andstudytheirrelationshipwithopiniondynamics.Forinstance,thefactorsthat
influence the spread of opinion have been investigated in [15]. Other researchers
investigated this relationship through optimizing opinion dynamic models [13].
Some studies modify the user opinions in a graph [17], while other approaches
optimize the average opinion in the FJ [9]. More recent studies show the effec-
tiveness of mathematical models in studying opinion dynamics within social net-
works. Among these models, the Friedkin-Johnsen (FJ) model [7] has provided a
foundational framework for studying opinion dynamics and has been confirmed
by a sustained line of experiments [16]. The FJ model simulates how opinions
evolve through iterative interactions between individuals’ intrinsic beliefs and
the expressed views of their neighbors. While the FJ model has been extensively
applied in theoretical and empirical studies, its application to identifying influ-
ential users and simulating the impact of targeted opinion manipulation remains
an area with significant potential for further exploration.
In this context, we study the mechanisms of opinion dynamics within the
social network graph by proposing an approach based on the FJ model. Specif-
ically, this study focuses on the role of influencers and how manipulating their
opinions can affect public opinion. By utilizing a publicly available dataset from
Kaggle [10], which includes tweets collected during the U.S. presidential election
of 2020, we demonstrate that interactions between certain influencers and vari-
ous tweeters can change the opinions and convictions of the latter. The primary
contributions of this research are threefold:
–Influencer identification: Identify and rank influential users within commu-
nities by interpreting the influence matrix from the FJ model at equilibrium.
–Sentiment manipulation: Examine the impact of influencers on overall opin-
ion by manipulating the initial opinions of influential users versus random
users.
–Propagation analysis: Analysis of the users most affected by the manipu-
lation, who are directly related (neighbors) to the influencers or indirectly
related (neighbors of neighbors).
This paper is organized as follows: In Section 2, an overview of the existing
literature on opinion dynamics models was discussed. Section 3 details the ap-
proach used in this research. The experimental results are presented in Section
4. Finally, Section 5 summarizes the key contributions and concludes the paper.

Title Suppressed Due to Excessive Length 3
2 Related Works
The study on the opinion dynamic within online communities have become an
hot topic, specifically, understand how opinion change and evolve between indi-
viduals. This section present the works the deal with these phenomena.
Okawa et al. [12] proposed a hybrid method that integrates opinion dynam-
ics models with deep learning techniques to enhance the predictive accuracy of
opinion dynamics models. Zhou et al. [18] used user past opinions, their context,
neighbours opinions, as input to neural network to predict the user opinion.
Other researches aimed in analyzing the role of influencers within social net-
work. Arruda et al. [1] study the how influencers behavior increase the intensity
of echo chamber. In the same context, Galante et al. [8] focused on how influ-
encers’ content spreading the emergence of echo chambers.
In another line of research, other studies extend of the FJ model. For in-
stance, Jia et al. [14] examined the evolution of social influence within the FJ
framework, highlighting how individuals’ susceptibility to influence changes over
time. [3] proposed a extension of the FJ model, including a dynamic network
structure in which connections are added or removed over time according to rec-
ommendationsfromthenetwork.[2]utilizedFJmodelforanalyzinghowpeople’s
opinions propagate through social networks and how influencers can affect these
dynamics.
In same context, several studies employ the FJ model to analyze equilibrium
opinions in social networks. Biondi et al. [4] extract the conditions that FJ model
induces opinion polarization in social networks by analyzing equilibrium opin-
ions. In a similar vein, Zhou et al. [16] interpreting equilibrium opinions of nodes
through absorbing random walks to address challenges posed by signed relation-
ships, such as the absence of doubly stochastic properties in the fundamental
matrix.
Zhang [13] provides a valuable contribution by addressing the problem of
opinion optimization in directed social networks using the FJ model. Their work
focuses on minimizing and maximizing the average equilibrium opinion by mod-
ifying the internal opinions of selected K nodes to 0 and 1. Building on their
approach, this work extends the use of the fundamental matrixΩ. Specifically,
the fundamental matrix was used to identify influential users whose opinions im-
pact the equilibrium state of the network. Our contribution complements their
work by shifting the focus from optimization strategies to influencer identifica-
tion and manipulation analysis. This approach provides a deeper understanding
of the structural dynamics of opinion propagation and highlights the role of
influencers in shifting sentiment changes by comparing the effects of targeted
interventions at influential nodes to random interventions.
3 Methodology
This section describes in detail the employed methodology to study the opin-
ion dynamics within social networks. The complete methodology is composed as

4 Omran Berjawi, Rida Khatoun, and Giuseppe Fenza
follows: data preparation, graph construction & community detection, and opin-
ion dynamics modeling. The subsequent subsections outline each component in
detail.
3.1 Data Preparation
First as preliminary data processing, the data used in this work consists of tweets
shared by users within a social network. On Twitter, the interaction among
users extend beyond static relationships (e.g., followers or friends), it consists of
various content-based engagement such as mentions, replies, and retweets. The
data preparation phase consists of the following steps:
–Interaction Extraction: This step aims to extract the mention engagement
within a tweet to represent the interaction between users, if one user men-
tions another user in their tweet, the frequency of mentions between users
was calculated. These frequencies are associated as weights of interactions,
reflecting the strength of influence between users.
–Sentiment Analysis: This steps focuses on measuring the user emotional
stanceonaspecifictopicthroughusertweets.Forthispurpose,theRoBERTa
pre-trained model was employed to determine the sentiment polarity, rang-
ing from negative to positive. The average sentiment score for each user was
calculated and used as their initial opinion, providing a quantitative measure
of the user’s overall stance.
3.2 Graph Construction and Community Detection
This component involves constructing a directed interaction graph,G= (V, E),
to represent user interactions. Here,V={v 1, v2,· · ·, vn}denotes the set of
users, andErepresents the edges between users. The edges are created between
two users if one mentioned the other in their tweets, with edge weightsa(vi,vj )
assigned as the frequency of mentions fromvi tov j. Once the network is con-
structed, the Louvain method [5], a modularity-based optimization algorithm,
was employed to detect communities within the network.
3.3 Opinion Dynamics Modeling
This phase represents the core of this research, which employs FJ model to
simulate opinion dynamics. The FJ model assumes that each node in the network
is characterized by two types of opinions: an initial opinionsi and an expressed
opinionx i(t)atanygiventimet.Theinitialopinions i representstheindividual’s
inherentstanceonaspecifictopic,expressedasavalueintherange[−1,1],where
si =−1indicates complete opposition to the topic, ands i = 1denotes full
support. Importantly,s i remains constant throughout the process. In contrast,
the expressed opinionx i(t)evolves over time, influenced by interactions with
other users in the social network. The progression of these expressed opinions at
(t+ 1)is governed by the following equation:

Title Suppressed Due to Excessive Length 5
xi(t+ 1) =
si + P j∈N(i) aijxj(t)
1 +P j∈N(i) aij (1)
Here,a ij represents the weight of the interaction betweenvi andv j, andN(i)
denotes the set of neighbors ofvi .
Inthisstudy,theFJmodelwasappliedtotheconstructedgraph.Theaverage
sentiment score (see Section 3.1) was used assi, while the weights of the connec-
tions between users were represented byaij. The model iteratively updates each
user’sx i(t)until the opinions converge, which means that each individual has
stabilized into a fixed opinion. This process reaches a steady state represented
by the equilibrium vector
x= (I+L) −1.s(2)
whereIis the identity matrix, andLis the Laplacian matrix.
The matrix(I+L) −1, also known as the fundamental matrix [9], summarizes
the structural relationships within the network, reflecting how the interactions
and initial opinions of individuals shape the final steady-state opinions. This
formulation allows us to reveal how much initial opinion of each node influences
other nodes’ opinions and, conversely, how each node’s opinion is influenced by
the opinions of others in the network.
Influence IdentificationWe define influencers as those whose opinions signifi-
cantly impact the opinions of others. This step is aimed at detecting and ranking
the influential users by extracting their influence scoresInScorei through the
following equation:
InScore i = 1 n
nX
j=1
ωij (3)
whereω ij are the fundamental matrix elements at the i-th row and the j-th
column of the matrix.
This score quantifies the influence of userion the equilibrium opinions of the
network. A higherInScorei indicates that userihas a high impact on the users
final opinions. Using this score, users were ranked to identify key influencers
within the community.
Opinion ManipulationTo study the impact of influencers on overall opin-
ion,two sentiment manipulations was performed to assess how modifying the
initial opinions of influential users, as compared to random users, affects the
overall community sentiment. The two types of manipulation simulations are as
follows:
–Positive Manipulation: In this simulation, the initial opinionssi of the tar-
geted user were set to+1, indicating a strongly positive sentiment.
–Negative Manipulation: In the second simulation, the initial opinionssi were
set to−1, reflecting a strongly negative sentiment.

6 Omran Berjawi, Rida Khatoun, and Giuseppe Fenza
For each simulation, the FJ model was running to calculate a new set of
equilibrium opinions,x i. To study the changes in opinion of influencers versus
random users, the average equilibrium opinion, denoted asAvg(z), was calcu-
lated, which capture the overall change in network sentiment.
4 Experiments and Results
This section detailed the experiments performed and present the result obtained
from this work. First the influential users within community were identified and
ranked. Following by studying their roles in shifting community opinion via
manipulation their initial opinion.
4.1 Dataset
In this work, a publicly available dataset was employed from Kaggle [10], which
contains more than 1.7 million tweets collected during the 2020 U.S. election and
spansoveronemonth.Thedatasetincludesvaluablemetadataforeachuser,such
as the number of followers, likes, retweets, and other engagement metrics. This
dataset was selected due to its relevance in examining opinion dynamics within
the context of a political event and allowing for a deeper analysis of user activity
and interaction.
4.2 Influencer Identification
The influencer identification approach outlined in Subsection 3.3 was applied in
this experiment to detect the influential users. We ranked the top 15 influencers
based on theirInScore, and split them into three distinct batches:
–Batch 1: Top 5 influencers.
–Batch 2: Influencers ranked 6–10.
–Batch 3: Influencers ranked 11–15.
The purpose of distributing influencers users to several batches is to analyze
the impact ofInScoreon opinion dynamics. To validate the effectiveness of the
proposed approach in identifying the influencers, we compared the results with
the normalized centrality metric [2], which is used to identify influencers.
Theresults,assummarizedinTable1,detectthetop15influencerswithinthe
network. It reveal that the FJ model successfully detected the same influential
users as the normalized centrality metric method. Moreover, the FJ model shows
its efficacy in ranking them by assigningInScoreto each user.
Additionally, the correlation betweenInScoreand the user engagements (to-
tal number of retweets, number of tweets, and follower count) of the identified
influencers was investigated. As seen in Table 1, the correlation shows that there
is a positive correlation betweenInScoreand Follower Count, as well asInScore
and Retweets (Sum). It highlights that influencers with higher follower counts

Title Suppressed Due to Excessive Length 7
Table 1.Detected Influencers
Rank User Batch Influence ScoreRetweets (Sum)Number of TweetsFollowers Count
1 RealJamesWoods Batch 1 0.8908 109251 8 2,685,154
2 w_terrence Batch 1 0.8805 42741 15 1,188,925
3 Varneyco Batch 1 0.8523 4800 55 663,854
4 Rasmussen_Poll Batch 1 0.7605 2505 52 358,137
5 JudicialWatch Batch 1 0.7009 42773 87 1,843,739
6 EpochTimes Batch 2 0.5169 3232 36 319,635
7 trish_regan Batch 2 0.4883 3152 6 737,555
8 WayneDupreeShowBatch 2 0.3430 1385 20 504,846
9 Styx666Official Batch 2 0.2417 417 6 90,474
10 realTrumpForce Batch 2 0.1662 12682 88 87,096
11 RealMattCouch Batch 3 0.1549 730 10 439,534
12 JoeTalkShow Batch 3 0.1159 12369 110 107,473
13 Wizard_Predicts Batch 3 0.1155 1967 57 12,659
14 Out5p0ken Batch 3 0.1088 12 6 27,476
15 MarkSimoneNY Batch 3 0.1001 13579 97 193,717
and retweet engagements are associated with highInScore, while on the other
hand, the number of tweets generated by influencers does not directly contribute
to a user’s influence.
These results indicate that some users engagement levels do not necessarily
represent their influence, even if there is a large number of tweets. In contrast,
some engagements, like the number of followers and retweets, have more meaning
when studying their relation to the influence of the user.
4.3 Sentiment Manipulation
This experiment aims to investigate the impact of sentiment manipulation on
the overall dynamic of community opinion. Specifically, we compare the opinion
at equilibrium after simulating the positive and negative manipulation on the
influential users versus random users.
The results demonstrate that the top influencers (Batch 1) exerted a signifi-
cantly stronger influence on the network’s equilibrium opinion than lower-ranked
influencers (Batch 2 and Batch 3) or random users. Specifically, as shown in Fig-
ure 1.a (top row) and Table 2, positive sentiment manipulation on Batch 1 re-
sulted in a significant rise in the average network opinion, from -0.3932 to 0.0866,
whereas negative sentiment interventions amplified polarization by reducing the
average opinion from -0.3932 to -0.5857.
For Batch 2, the results in Figure 1.b show a rise in the average network
opinion for positive manipulation, from -0.3932 to -0.3408, whereas negative
sentiment manipulation reduces the average opinion from -0.3932 to -0.429. On
the other hand, for Batch 3, as shown in Figure 2.a and Table 2, there are minor
changes in the average sentiment for both types of manipulation.
Finally, the last batch, which represents the random users, shows a negligible
impact on the overall sentiment. As depicted in Figures 2.b (bottom row), and
Table 2, for positive manipulation, the average opinion for both manipulation
types provides negligible shifts in the network’s average opinion, which suggests

8 Omran Berjawi, Rida Khatoun, and Giuseppe Fenza
Fig.1.A comparison of opinion distributions before and after positive and negative
manipulation for Batch 1 and Batch 2.
Fig.2.A comparison of opinion distributions before and after positive and negative
manipulation for Batch 3 and random Batch.

Title Suppressed Due to Excessive Length 9
their limited roles. From -0.3932 to -0.3904 and from -0.3932 to -0.3940, respec-
tively.
Based on the above results, the findings support the hypothesis that influen-
tial users exhibit a clear ability to influence community opinion more effectively
than other users, whether by amplifying positive emotions or exacerbating neg-
ative emotions. As observed, there is a strong relation betweenInScoreand
the ability to shift the overall opinion of the community. When theInScore
increases, the opinion-shifting impact increases. Specifically, those with higher
InScoreswere able to induce significant changes in the community’s sentiment,
both in positive and negative directions. These results underline the importance
of identifying and ranking influential users based on their influence score, as
their influence score plays a crucial role in the impact on overall opinion of the
community.
Table 2.Equilibrium Opinion Changes by Batch
Batch Original Positive Negative
Opinion Manipulation Manipulation
Batch 1 -0.3932 0.0866 -0.5857
Batch 2 -0.3932 -0.3408 -0.4291
Batch 3 -0.3932 -0.3647 -0.4120
Random Batch -0.3932 -0.3904 -0.3940
4.4 Propagation Analysis
Table 3.Top 10 Affected Users for Positive/Negative Manipulation
Direct ConnectionIndirect Connection
Batch 1Batch 2 Batch 1Batch 2
Positive Intervention 7 8 3 2
Negative Intervention 6 9 4 1
After detecting the influencers and studying the relation between manipulat-
ing the initial opinion of influencers and its impact on the overall opinion of the
community, we study how the influence propagate within the network. The prop-
agation analysis investigates how opinion changes spread through the network
through analyzing who the most affected users are by the opinion manipulation
simulation.
This experiment examined the top 10 most affected users for Batch 1 and
Batch 2 influencers, who were identified as having the most substantial impact
on the community’s collective sentiment, whether these users are directly con-
nected to the influencers or influenced indirectly through neighbors of neighbors.

10 Omran Berjawi, Rida Khatoun, and Giuseppe Fenza
As shown in Table 3, we have seen a consistent pattern in the spread of senti-
ment changes for Batch 1 influencers. Both direct and indirect connections to
the influencers are impacted by the two types of sentiment manipulation. The
most impacted users are the influencers’ neighbors; however, the impact also
reached the indirect connections, demonstrating that the influencers can spread
their influence through the network. On the other hand, for Batch 2, for both
manipulations, most impacted users are the influencers’ neighbors, in which 8
out of 10 for positive and 9 out of 10 for negative are the directed neighbors.
In summary, regardless of the type of manipulation (positive or negative),
the experiments provide valuable understanding into who is most affected by
opinon manipulation. The findings validate that manipulating the initial opin-
ion of the top influencer users (Batch 1) not limited to their neighbours, rather,
it extends to neighbour of neighbours and, ultimately, to the broader commu-
nity. In contrast, manipulating the initial opinion of Batch 2 influencers is more
confined to their direct neighbors. These results suggest that as the influencer
score increases, the influencer’s impact expands beyond their immediate network
to indirectly connected users and, eventually, to the overall network.
5 Conclusion
This paper proposes a framework based on the FJ model to study the opinion
dynamics within online communities. The proposed approach identifies the in-
fluential users and their impact on community opinion by analyzing the effects
of manipulating their initial opinions, and examines how targeted manipulation
of influential users can propagate through the network. The findings show that,
in contrast to more traditional approaches, the suggested approach may iden-
tify influencers and rank them according to their influence score. The findings
also highlight the fact that users with higher influence ratings have a signifi-
cant impact on shifting opinions in the community and that their power extends
beyond their immediate neighbors to include indirect relationships. In future re-
search directions, the manipulation of opinion in real time may be investigated,
in addition to validating the approach across different social network platforms.
References
1. de Arruda, H.F., Oliveira, K.A., Moreno, Y.: Echo chamber formation sharpened
by priority users. iScience27(11) (2024)
2. Berjawi1, O., Cavaliere, D.: Dynamic analysis of influencer impact on opinion for-
mation in social networks. In: Web Information Systems Engineering–WISE 2024
PhD Symposium, Demos and Workshops: WEB-for-GOOD 2024, AIWDA 2024,
SWIFT-AG 2024, and Demos, Doha, Qatar, December 2–5, 2024, Proceedings.
p. 394. Springer Nature
3. Bhalla, N., Lechowicz, A., Musco, C.: Local edge dynamics and opinion polar-
ization. In: Proceedings of the Sixteenth ACM International Conference on Web
Search and Data Mining. pp. 6–14 (2023)

Title Suppressed Due to Excessive Length 11
4. Biondi, E., Boldrini, C., Passarella, A., Conti, M.: Dynamics of opinion polar-
ization. IEEE Transactions on Systems, Man, and Cybernetics: Systems53(9),
5381–5392 (2023)
5. Blondel, V.D., Guillaume, J.L., Lambiotte, R., Lefebvre, E.: Fast unfolding of com-
munities in large networks. Journal of statistical mechanics: theory and experiment
2008(10), P10008 (2008)
6. Erikson, R.S., Tedin, K.L.: American public opinion: Its origins, content, and im-
pact. Routledge (2019)
7. Friedkin, N.E., Johnsen, E.C.: Social influence and opinions. Journal of mathemat-
ical sociology15(3-4), 193–206 (1990)
8. Galante, F., Vassio, L., Garetto, M., Leonardi, E.: Modeling communication asym-
metry and content personalization in online social networks. Online Social Net-
works and Media37, 100269 (2023)
9. Gionis, A., Terzi, E., Tsaparas, P.: Opinion maximization in social networks. In:
Proceedings of the 2013 SIAM international conference on data mining. pp. 387–
395. SIAM (2013)
10. Hui, M.C.: Us election 2020 tweets (2020),
https://www.kaggle.com/datasets/manchunhui/us-election-2020-tweets, accessed:
2025-01-16
11. Khanom, M.T.: Using social media marketing in the digital era: A necessity or
a choice. International Journal of Research in Business and Social Science (2147-
4478)12(3), 88–98 (2023)
12. Okawa,M.,Iwata,T.:Predictingopiniondynamicsviasociologically-informedneu-
ral networks. In: Proceedings of the 28th ACM SIGKDD Conference on Knowledge
Discovery and Data Mining. pp. 1306–1316 (2022)
13. Sun, H., Zhang, Z.: Opinion optimization in directed social networks. In: Pro-
ceedings of the AAAI Conference on Artificial Intelligence. vol. 37, pp. 4623–4632
(2023)
14. Tian, Y., Wang, L.: Opinion dynamics in social networks with stubborn agents:
An issue-based perspective. Automatica96, 213–223 (2018)
15. Zhan, M., Kou, G., Dong, Y., Chiclana, F., Herrera-Viedma, E.: Bounded confi-
dence evolution of opinions and actions in social networks. IEEE Transactions on
Cybernetics52(7), 7017–7028 (2021)
16. Zhou, X., Sun, H., Xu, W., Li, W., Zhang, Z.: Friedkin-johnsen model for opinion
dynamics on signed graphs. IEEE Transactions on Knowledge and Data Engineer-
ing (2024)
17. Zhou, X., Zhang, Z.: Opinion maximization in social networks via leader selection.
In: Proceedings of the ACM Web Conference 2023. pp. 133–142 (2023)
18. Zhu, L., He, Y., Zhou, D.: Neural opinion dynamics model for the prediction of
user-level stance dynamics. Information Processing & Management57(2), 102031
(2020)
