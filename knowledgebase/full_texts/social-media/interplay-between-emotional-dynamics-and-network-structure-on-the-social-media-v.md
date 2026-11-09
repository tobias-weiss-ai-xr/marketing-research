---
title: Interplay between Emotional Dynamics and Network Structure on the Social Media Vent
url: https://arxiv.org/abs/2609.31129
category: social-media
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Yuina Takahashi
- Sho Tsugawa
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.31129
pages: 8
chars: 26676
fetched_at: '2026-11-08T13:12:56+00:00'
kb_version: 1
---

# Interplay between Emotional Dynamics and Network Structure on the Social Media Vent

Interplay between Emotional Dynamics and
Network Structure on the Social Media Vent
Yuina Takahashi1 and Sho Tsugawa2
1 Graduate School of Science and Technology, University of Tsukuba
1-1-1 Tennodai, Tsukuba, Ibaraki 305-8573, Japan
y.takahashi@snlab.cs.tsukuba.ac.jp
2 Institute of Systems and Information Engineering, University of Tsukuba
1-1-1 Tennodai, Tsukuba, Ibaraki 305-8573, Japan
s-tugawa@cs.tsukuba.ac.jp
Abstract.The sharing and contagion of emotions on social media in-
fluence online interactions and users’ psychological states. This study
analyzes emotional dynamics on Vent, an emotion-sharing social me-
dia platform where users explicitly assign emotional labels to their own
posts. Using a large-scale dataset, we examine how emotions in users’
pre-posting timelines are associated with their subsequent emotional la-
bels and how such associations vary across users. Our analysis reveals
three key findings. First, users’ subsequent emotional labels are associ-
ated with the emotional composition of their pre-posting timelines, with
same-category emotions being overrepresented before posts in all ana-
lyzedcategories.Second,severalcross-categoryassociationsareobserved;
for example, Surprise was overrepresented before Fear posts; Affection
and Happiness were overrepresented before Anger posts; and Affection
was overrepresented before Sadness posts. Third, users differ in their
degree of alignment with timeline emotional fluctuations, and highly
aligned users tend to be located close to one another in the network.
These findings provide large-scale observational evidence that emotional
expression on Vent is associated with both short-term timeline context
and network structure.
Keywords:Social Media·Social Network·Emotional Contagion·Vent
1 Introduction
On social media, interactions among users through the expression and shar-
ing of emotions are highly active, giving rise to phenomena such as emotional
homophily [4] and emotional contagion [5,2,7,3,14]. Emotional homophily is
defined as the tendency for individuals with similar emotional dispositions to
connect with one another, while emotional contagion refers to the phenomenon
where a user’s emotional state influences the emotions of others. These phenom-
ena exert a profound impact on community formation and information diffusion
within social media ecosystems.
arXiv:2609.31129v1  [cs.SI]  25 Sep 2026

2 Y. Takahashi et al.
Extensive research has investigated emotional contagion and emotional dy-
namics on social media [2–7,11]. Kramer et al. [7] experimentally showed that
emotional content in Facebook News Feeds affects users’ subsequent emotional
expressions, while Ferrara et al. [5] examined emotional contagion on Twitter by
comparing users’ posts with the emotional content in their social surroundings.
Furthermore, analyses utilizing more granular classifications have revealed that
specific emotions, such as anger, tend to spread more rapidly and extensively
than others, such as joy [4,3].
More recent work has examined finer emotional categories: Hossain et al. [6]
analyzed 28 types of emotions in social media comments and proposed a frame-
work for extracting and predicting emotional trends across discussion threads,
while Sener et al. [11] analyzed fine-grained emotional dynamics on Twitter using
valence, arousal, and dominance.
However, despite these advances, three limitations remain in existing stud-
ies of emotional dynamics on social media. First, although some studies have
adopted finer emotion categories, much prior work still relies on coarse-grained
or binary emotional classifications, such as positive and negative emotions. Sec-
ond, prior studies have mainly focused on intra-emotional patterns, while cross-
emotional associations remain insufficiently explored. Third, individual differ-
ences in users’ alignment with surrounding emotional fluctuations and their
network structure remain unclear. Understanding these patterns may inform
healthier social media design.
In this paper, we analyze temporal associations between pre-posting timeline
emotions and users’ subsequent emotional labels using theVentdataset [10],
which allows for finer emotional granularity than datasets used in many prior
studies. In this paper, we address two research questions to examine emotional
dynamics on social media: RQ1 investigates how emotions in users’ pre-posting
timelines are associated with their subsequent emotional labels, and RQ2 ex-
amines how users’ susceptibility to timeline emotional fluctuations varies and
whether highly susceptible users are close to one another in the network.
The contribution of this paper is threefold. First, we analyze temporal asso-
ciations between pre-posting timeline emotions and users’ subsequent emotional
labels using a large-scale Vent dataset with explicit emotion labels. Second, we
examine both within-category and cross-category emotional associations. Third,
we quantify users’ alignment with timeline emotional fluctuations and analyze
whether highly aligned users are located close to one another in the social net-
work.
2 The Vent Dataset
Vent, the platform analyzed in this study, is a social media platform where
users can assign emotional labels to their own posts. Unlike typical social media
platforms,Ventrequiresuserstoselectalabelrepresentingtheircurrentemotion,
such as Sad or Happy, at the time of posting. This unique feature allows us

Emotional Dynamics and Network Structure on Vent 3
Table 1: Target emotional categories, example labels, and the distribution of
posts.
Category Example Labels Number of Posts (%)
Sadness Sad, Lonely, Miserable 5,122,245 (27.4%)
Happiness Amused, Happy, Excited 3,646,174 (19.5%)
Anger Annoyed, Frustrated, Irritated 2,930,447 (15.7%)
Fear Anxious, Stressed, Afraid 2,626,845 (14.1%)
Affection Loving, Needy, Adoring 1,770,829 (9.5%)
Surprise Confused, Curious, Surprised 1,657,497 (8.9%)
Positivity Hyped, Hopeful, Determined 927,766 (5.0%)
to analyze subjective emotions explicitly stated by users without the need for
sentiment estimation via text analysis.
The public Vent dataset [10] used in this study contains data for 934,095
users, 33,623,414 posts, and a social graph consisting of 13,605,522 following
edges. It includes 705 types of labels organized into 63 categories, with each
post linked to these emotional labels.
From this public dataset, we focused on posts assigned with labels belonging
to eight broad categories: Sadness, Fear, Anger, Surprise, Positivity, Affection,
Happiness, and Feelings. However, because the Feelings category contains het-
erogeneous labels such as Tired, Meh, and Sleepy, it was excluded from the
category-level analyses. We therefore defined active users as those who posted
at least 30 times using labels in the remaining seven categories, and filtered the
dataset accordingly. As a result of this extraction process, our analysis targeted
18,681,803 posts by 137,822 active users and 4,103,692 following edges. Table
1 presents the seven target emotional categories, including their representative
labels and the distribution of posts (number and percentage) among active users.
3 Analysis of Timeline Emotional Associations
This section examines temporal associations between emotions in users’ pre-
postingtimelinesandtheirsubsequentemotionallabels.Weanalyzebothwithin-
category associations, where the same emotion appears in the timeline and the
subsequent post, and cross-category associations, where different emotion cat-
egories are involved. We focus on seven emotional categories: Sadness, Fear,
Anger, Surprise, Positivity, Affection, and Happiness.
3.1 Quantification of Pre-posting Emotional Exposure
First, we define the timeline immediately preceding useru’s posttas the set of
postsH t made byu’s followees within three hours prior tot. To mitigate noise
from timelines with extremely sparse activity, we only included poststwhere
the number of posts in the timeline|Ht|exceeded 20. The final analysis targeted
a total of 1,035,304 posts from 29,454 users.

4 Y. Takahashi et al.
/aj17/aj15/aj17 /aj17/aj15/aj19 /aj17/aj15/aj21 /aj17/aj15/aj23 /aj17/aj15/aj25 /aj18/aj15/aj17
/aj38/aj78/aj80/aj85/aj74/aj80/aj79/aj66/aj77/aj1/aj37/aj74/aj84/aj85/aj83/aj74/aj67/aj86/aj85/aj74/aj80/aj79/aj1/aj80/aj79/aj1/aj53/aj74/aj78/aj70/aj77/aj74/aj79/aj70
/aj41/aj66/aj81/aj81/aj74/aj79/aj70/aj84/aj84
/aj34/aj71/aj71/aj70/aj68/aj85/aj74/aj80/aj79
/aj49/aj80/aj84/aj74/aj85/aj74/aj87/aj74/aj85/aj90
/aj52/aj86/aj83/aj81/aj83/aj74/aj84/aj70
/aj34/aj79/aj72/aj70/aj83
/aj39/aj70/aj66/aj83
/aj52/aj66/aj69/aj79/aj70/aj84/aj84
/aj35/aj66/aj84/aj70/aj77/aj74/aj79/aj70
/aj35/aj66/aj84/aj70/aj77/aj74/aj79/aj70/aj1/aj66/aj79/aj69/aj1/aj53/aj66/aj83/aj72/aj70/aj85/aj1/aj54/aj84/aj70/aj83/aj8/aj84/aj1/aj38/aj78/aj80/aj85/aj74/aj80/aj79
/aj17/aj15/aj19/aj19/aj21
/aj17/aj15/aj19/aj19/aj24
/aj17/aj15/aj19/aj19/aj19
/aj17/aj15/aj19/aj19/aj18
/aj17/aj15/aj19/aj19/aj25
/aj17/aj15/aj19/aj20/aj19
/aj17/aj15/aj19/aj21/aj26
/aj17/aj15/aj19/aj20/aj24
/aj17/aj15/aj18/aj18/aj22
/aj17/aj15/aj18/aj18/aj21
/aj17/aj15/aj18/aj18/aj20
/aj17/aj15/aj18/aj18/aj26
/aj17/aj15/aj18/aj18/aj26
/aj17/aj15/aj18/aj19/aj22
/aj17/aj15/aj18/aj18/aj25
/aj17/aj15/aj18/aj19/aj18
/aj17/aj15/aj18/aj21/aj17
/aj17/aj15/aj18/aj20/aj23
/aj17/aj15/aj18/aj19/aj24
/aj17/aj15/aj18/aj20/aj24
/aj17/aj15/aj18/aj21/aj23
/aj17/aj15/aj18/aj21/aj17
/aj17/aj15/aj18/aj20/aj24
/aj17/aj15/aj18/aj21/aj18
/aj17/aj15/aj17/aj26/aj26
/aj17/aj15/aj17/aj26/aj21
/aj17/aj15/aj17/aj26/aj19
/aj17/aj15/aj18/aj19/aj20
/aj17/aj15/aj18/aj17/aj17
/aj17/aj15/aj18/aj17/aj19
/aj17/aj15/aj17/aj26/aj23
/aj17/aj15/aj17/aj26/aj23
/aj17/aj15/aj17/aj22/aj18
/aj17/aj15/aj17/aj22/aj22
/aj17/aj15/aj17/aj25/aj23
/aj17/aj15/aj17/aj21/aj26
/aj17/aj15/aj17/aj21/aj24
/aj17/aj15/aj17/aj22/aj17
/aj17/aj15/aj17/aj22/aj17
/aj17/aj15/aj17/aj22/aj21
/aj17/aj15/aj18/aj18/aj26
/aj17/aj15/aj18/aj20/aj22
/aj17/aj15/aj18/aj19/aj23
/aj17/aj15/aj18/aj18/aj21
/aj17/aj15/aj18/aj18/aj25
/aj17/aj15/aj18/aj18/aj23
/aj17/aj15/aj18/aj18/aj26
/aj17/aj15/aj18/aj18/aj23
/aj17/aj15/aj19/aj22/aj19
/aj17/aj15/aj19/aj20/aj25
/aj17/aj15/aj19/aj20/aj21
/aj17/aj15/aj19/aj20/aj23
/aj17/aj15/aj19/aj21/aj19
/aj17/aj15/aj19/aj20/aj22
/aj17/aj15/aj19/aj20/aj19
/aj17/aj15/aj19/aj20/aj22
/aj52/aj66/aj69/aj79/aj70/aj84/aj84
/aj39/aj70/aj66/aj83
/aj34/aj79/aj72/aj70/aj83
/aj52/aj86/aj83/aj81/aj83/aj74/aj84/aj70
/aj49/aj80/aj84/aj74/aj85/aj74/aj87/aj74/aj85/aj90
/aj34/aj71/aj71/aj70/aj68/aj85/aj74/aj80/aj79
/aj41/aj66/aj81/aj81/aj74/aj79/aj70/aj84/aj84
(a) Comparison with baseline
/aj52/aj66/aj69/aj79/aj70/aj84/aj84
/aj39/aj70/aj66/aj83
/aj34/aj79/aj72/aj70/aj83
/aj52/aj86/aj83/aj81/aj83/aj74/aj84/aj70
/aj49/aj80/aj84/aj74/aj85/aj74/aj87/aj74/aj85/aj90
/aj34/aj71/aj71/aj70/aj68/aj85/aj74/aj80/aj79
/aj41/aj66/aj81/aj81/aj74/aj79/aj70/aj84/aj84
/aj49/aj83/aj70/aj14/aj81/aj80/aj84/aj85/aj74/aj79/aj72/aj1/aj53/aj74/aj78/aj70/aj77/aj74/aj79/aj70/aj1/aj38/aj78/aj80/aj85/aj74/aj80/aj79
/aj52/aj66/aj69/aj79/aj70/aj84/aj84
/aj39/aj70/aj66/aj83
/aj34/aj79/aj72/aj70/aj83
/aj52/aj86/aj83/aj81/aj83/aj74/aj84/aj70
/aj49/aj80/aj84/aj74/aj85/aj74/aj87/aj74/aj85/aj90
/aj34/aj71/aj71/aj70/aj68/aj85/aj74/aj80/aj79
/aj41/aj66/aj81/aj81/aj74/aj79/aj70/aj84/aj84/aj53/aj66/aj83/aj72/aj70/aj85/aj1/aj54/aj84/aj70/aj83/aj8/aj84/aj1/aj38/aj78/aj80/aj85/aj74/aj80/aj79
/aj18/aj15/aj17/aj21/aj24 /aj17/aj15/aj26/aj24/aj20 /aj17/aj15/aj26/aj24/aj21 /aj17/aj15/aj26/aj26/aj26 /aj17/aj15/aj26/aj20/aj25 /aj18/aj15/aj17/aj19/aj23 /aj17/aj15/aj26/aj25/aj21
/aj17/aj15/aj26/aj24/aj24 /aj18/aj15/aj17/aj20/aj23 /aj17/aj15/aj26/aj26/aj23 /aj18/aj15/aj17/aj23/aj24 /aj17/aj15/aj26/aj19/aj24 /aj17/aj15/aj26/aj26/aj26 /aj17/aj15/aj26/aj26/aj24
/aj17/aj15/aj26/aj23/aj17 /aj17/aj15/aj26/aj25/aj17 /aj18/aj15/aj17/aj20/aj22 /aj18/aj15/aj17/aj21/aj21 /aj17/aj15/aj25/aj25/aj23 /aj18/aj15/aj17/aj18/aj22 /aj18/aj15/aj17/aj20/aj17
/aj17/aj15/aj26/aj20/aj19 /aj17/aj15/aj26/aj25/aj24 /aj17/aj15/aj26/aj24/aj21 /aj18/aj15/aj19/aj25/aj20 /aj17/aj15/aj26/aj18/aj20 /aj17/aj15/aj26/aj25/aj22 /aj18/aj15/aj17/aj17/aj20
/aj17/aj15/aj26/aj20/aj22 /aj17/aj15/aj26/aj20/aj20 /aj17/aj15/aj25/aj26/aj26 /aj17/aj15/aj26/aj23/aj19 /aj18/aj15/aj23/aj17/aj24 /aj18/aj15/aj17/aj25/aj26 /aj17/aj15/aj26/aj26/aj21
/aj17/aj15/aj26/aj22/aj25 /aj17/aj15/aj26/aj20/aj26 /aj17/aj15/aj26/aj23/aj25 /aj17/aj15/aj26/aj25/aj22 /aj18/aj15/aj17/aj20/aj19 /aj18/aj15/aj18/aj23/aj22 /aj18/aj15/aj17/aj18/aj18
/aj17/aj15/aj26/aj21/aj20 /aj17/aj15/aj26/aj21/aj25 /aj17/aj15/aj26/aj26/aj22 /aj18/aj15/aj17/aj20/aj21 /aj17/aj15/aj26/aj22/aj17 /aj18/aj15/aj17/aj19/aj26 /aj18/aj15/aj17/aj24/aj17
/aj17/aj15/aj25
/aj17/aj15/aj26
/aj18/aj15/aj17
/aj18/aj15/aj18
/aj18/aj15/aj19
/aj18/aj15/aj20
/aj18/aj15/aj21
/aj18/aj15/aj22
/aj18/aj15/aj23 (b) Ratio to baseline
Fig.1: Emotional distribution in the timeline immediately prior to posting: (a)
comparison of absolute distributions and (b) ratio of the timeline distribution
to the baseline.
Consistent with existing research on the contagion of positive and negative
affects [5], we calculated a baseline distribution representing the average emo-
tional distribution on timelines and determined the difference between the actual
distribution inH t and this baseline. The baseline distribution was calculated as
follows: First, allH t sets associated with all analyzed posts were aggregated
into a single population. For each posttby useru, a virtual timeline was con-
structed by randomly sampling a number of posts from this population equal
to the actual timeline size|Ht|. The average emotional distribution across these
virtual timelines was defined as the baseline distribution. We confirmed that the
standard error for all emotional categories during this calculation was less than
0.0001, ensuring sufficient statistical precision for subsequent analyses.
3.2 Within- and Cross-Category Emotional Associations
To clarify how user emotions are influenced by their preceding timelines, we
analyzed emotional biases just before a post is made. Figure 1a compares the
emotional distribution of pre-posting timelines with the baseline, and Figure
1b illustrates the ratio between these distributions. Mann-Whitney U tests con-
firmed significant differences from the baseline for all combinations of timeline
emotions and user posting emotions.
As shown in Figure 1b, the proportion of the same emotion in the time-
line increases prior to a post for all categories, suggesting the occurrence of
intra-emotional contagion on Vent. Notably, the proportion of Positivity in the
timeline showed the largest relative increase—1.607 times the baseline—just be-
fore a user posted a Positivity label. This indicates that Positivity possesses the
highest infectivity among the seven analyzed emotions, aligning with prior find-
ings that positive emotions spread more readily than negative ones [5,2]. The
second highest increase was observed for Surprise (1.283 times). Berger et al.
[1] noted that the virality of online content depends not only on valence (posi-
tive vs. negative) but also on arousal—the degree to which an emotion activates

Emotional Dynamics and Network Structure on Vent 5
and drives an individual to action. This suggests that the high-arousal nature of
Surprise contributes to its high transmissibility.
Furthermore, Figure 1b suggests that users’ subsequent emotional labels are
associated not only with the same emotion but also with different emotion cat-
egories in their pre-posting timelines. First, before Fear posts, the proportion of
Surprise in the timeline increased by a factor of 1.067. This pattern is consistent
with prior work suggesting that surprise can be related to uncertainty and may
precede other emotional responses in social media discussions [14,12]. Second,
before Anger posts, Affection and Happiness increased by factors of 1.015 and
1.030, respectively. This may be related to social comparison, as prior work has
reported that passively viewing others’ happiness on Facebook can be associated
with envy [8]. Third, before Sadness posts, the proportion of Affection was 1.026
times higher. Since the Affection category includes labels related to longing and
bittersweetness, such as Needy, this association may reflect emotional proximity
between affectionate and sad expressions.
Collectively, these findings answer RQ1 by showing that pre-posting timeline
emotions are associated with users’ subsequent emotional labels both within and
across emotion categories. These cross-category patterns should be interpreted
as observational associations rather than causal mechanisms.
4 Analysis of Susceptibility
The analysis results in Section 3 suggest that, as an average trend across all
users, the emotional distribution on the timeline may influence the emotions
expressed in their posts. However, it is expected that susceptibility to such in-
fluence varies among individual users. To address RQ2, this section investigates
the differences in user susceptibility to emotions on their timelines and explores
how this susceptibility is characterized.
4.1 Quantification and Distribution of Susceptibility
Following Ferrara et al. [5], we quantified users’ susceptibility to emotional con-
tagion by examining whether their expressed emotions aligned with recent emo-
tional fluctuations in their timelines. For each post by a user, we first computed
the emotional distribution of posts appearing in the user’s timeline during the
preceding three hours and compared it with the baseline emotional distribution.
We then identified the emotion that showed the largest increase relative to the
baseline. A match was defined as a case in which the emotion expressed in the
user’s post was identical to this most strongly increased emotion in the preced-
ing timeline. The susceptibility index is then derived from the frequency of these
matches across all of a user’s posts. A higher value of this index indicates that
the user’s emotional expression is more likely to align with short-term emotional
fluctuations in their surrounding information environment, suggesting greater
susceptibility to emotional contagion. To eliminate the influence of users with
a low volume of activity, the final analysis targets 6,908 users who have made

6 Y. Takahashi et al.
/aj17/aj15/aj17 /aj17/aj15/aj19 /aj17/aj15/aj21 /aj17/aj15/aj23 /aj17/aj15/aj25 /aj18/aj15/aj17
/aj38/aj78/aj80/aj85/aj74/aj80/aj79/aj1/aj46/aj66/aj85/aj68/aj73/aj74/aj79/aj72/aj1/aj51/aj66/aj85/aj70/aj1/aj9/aj54/aj84/aj70/aj83/aj1/aj49/aj80/aj84/aj85/aj1/aj87/aj84/aj15/aj1/aj46/aj66/aj89/aj1/aj53/aj74/aj78/aj70/aj77/aj74/aj79/aj70/aj1/aj42/aj79/aj68/aj83/aj70/aj66/aj84/aj70/aj10
/aj17
/aj18/aj17/aj17
/aj19/aj17/aj17
/aj20/aj17/aj17
/aj21/aj17/aj17/aj39/aj83/aj70/aj82/aj86/aj70/aj79/aj68/aj90
(a) Histogram
/aj17/aj15/aj17 /aj17/aj15/aj19 /aj17/aj15/aj21 /aj17/aj15/aj23 /aj17/aj15/aj25 /aj18/aj15/aj17
/aj38/aj78/aj80/aj85/aj74/aj80/aj79/aj1/aj46/aj66/aj85/aj68/aj73/aj74/aj79/aj72/aj1/aj51/aj66/aj85/aj70/aj1/aj9/aj54/aj84/aj70/aj83/aj1/aj49/aj80/aj84/aj85/aj1/aj87/aj84/aj15/aj1/aj46/aj66/aj89/aj1/aj53/aj74/aj78/aj70/aj77/aj74/aj79/aj70/aj1/aj42/aj79/aj68/aj83/aj70/aj66/aj84/aj70/aj10
/aj17/aj15/aj17
/aj17/aj15/aj19
/aj17/aj15/aj21
/aj17/aj15/aj23
/aj17/aj15/aj25
/aj18/aj15/aj17/aj36/aj86/aj78/aj86/aj77/aj66/aj85/aj74/aj87/aj70/aj1/aj49/aj83/aj80/aj67/aj66/aj67/aj74/aj77/aj74/aj85/aj90 (b) Cumulative Distribution
Fig.2: Distribution of matching rates between the posted emotion and the emo-
tion with the highest increase rate on the timeline. The distribution is right-
skewed, with a small number of users exhibiting high matching rates.
at least 20 qualifying posts (t) where the number of preceding timeline posts
within three hours (|Ht|) exceeded 20, consistent with the criteria established in
Section 3.
Figure 2 presents the histogram and cumulative distribution of the match
rate between the emotion posted by a user and the emotion with the highest
increase rate on their timeline. From Figure 2, it is evident that a small number
of highly susceptible users exist who react sensitively to timeline trends and
exhibit extremely high match rates. This user segment is at risk of excessively
synchronizing with the negative emotional expressions of their surroundings,
which may result in increased psychological distress.
4.2 Homophily in Susceptibility
Itisknownthathomophilyexistsinsusceptibilitytoinformationdiffusion—referring
to the degree to which a user reacts to information from their surroundings—and
that individuals with similar levels of susceptibility tend to connect with one an-
other [9,13]. In this section, we examine whether a similar tendency can be
observed for users’ alignment with emotional fluctuations in their timelines. For
the following network analysis, we define high-susceptibility users as those in the
top 15% of the susceptibility index.
First, we calculated the correlation between each user’s susceptibility and
that of their followees. The correlation coefficient was 0.437, confirming a mod-
erate positive correlation. This finding suggests that users with similar levels of
susceptibility to emotional contagion tend to be connected within the network.
Next, to clarify the proximity between highly susceptible users, we calcu-
lated the distribution of shortest path lengths for all pairs of high-susceptibility
users. As a baseline for comparison, we constructed a null model by randomly
rewiring edges connected to high-susceptibility users while preserving their orig-
inal degrees. The values for the null model represent the average of 10 trials.

Emotional Dynamics and Network Structure on Vent 7
Table 2: Number of high-susceptibility user pairs by shortest path length com-
pared to the null model
High Susceptibility Null Model (SEM)
1 hop 3,782 457.4 (5.6)
2 hops 345,503 45,227.1 (87.5)
3 hops 188,547 293,805.9 (1708.8)
4 hops 1,406 199,747.4 (1754.2)
5 hops 3 3.2 (2.0)
The results are presented in Tab. 2. The number of high-susceptibility user pairs
in a direct following relationship (1-hop) was approximately 8.3 times higher
than that in the null model. Furthermore, the average number of hops between
high-susceptibility users was 2.35, shorter than the 3.29 hops observed in the null
model. Additionally, while only about 63.0% of pairs were located within three
hops in the null model, this proportion reached approximately 99.7% among
high-susceptibility users.
These results indicate that high-susceptibility users are more strongly clus-
tered in the network than expected under the null model. Such proximity may
create conditions for local reinforcement of emotional expressions, although the
present analysis does not directly establish an echo-chamber effect.
5 Conclusion
In this paper, we analyzed emotional dynamics on Vent, an emotion-sharing
social media platform with explicit user-assigned emotion labels. For RQ1, we
found that users’ subsequent emotional labels are associated with the emotional
composition of their pre-posting timelines, with both within-category and cross-
category associations observed among several emotion categories. For RQ2, we
quantified users’ alignment with timeline emotional fluctuations and found that
highly aligned users tend to be located close to one another in the network
compared with a degree-preserving null model. Overall, these findings provide
large-scale observational evidence that emotional expression on Vent is related
to both short-term timeline context and network structure. Because our analysis
is based on followee posts within a preceding time window, it captures potential
rather than actual exposure. Moreover, the observed associations may also reflect
stable user-specific emotion profiles, emotional homophily, or common external
events, rather than short-term emotional contagion alone. Future work should
further examine causal identification and the generalizability of these patterns
to other social media platforms.
Acknowledgments.This work was supported by JSPS KAKENHI Grant Number
JP25K03105 and JST ERATO Grant Number JPMJER2502.

8 Y. Takahashi et al.
Disclosure of Interests.The authors have no competing interests to declare that
are relevant to the content of this article.
References
1. Berger, J., Milkman, K.L.: What makes online content viral? Journal of Marketing
Research49(2), 192–205 (2012)
2. Coviello, L., Sohn, Y., Kramer, A.D., Marlow, C., Franceschetti, M., Christakis,
N.A., Fowler, J.H.: Detecting Emotional Contagion in Massive Social Networks.
PLOS ONE9(3), e90315 (2014)
3. Fan, R., Xu, K., Zhao, J.: Higher contagion and weaker ties mean anger spreads
faster than joy in social media. arXiv preprint arXiv:1608.03656 (2016)
4. Fan, R., Zhao, J., Chen, Y., Xu, K.: Anger Is More Influential than Joy: Sentiment
Correlation in Weibo. PLOS ONE9(10), e110184 (2014)
5. Ferrara,E.,Yang,Z.:MeasuringEmotionalContagioninSocialMedia.PLOSONE
10(11), e0142390 (2015)
6. Hossain, I., Puppala, S., Alam, M.J., Talukder, S.: Monitoring dynamics of emo-
tional sentiment in social network commentaries. In: Proceedings of the Interna-
tional Conference on Advances in Social Networks Analysis and Mining. pp. 51–55
(2023)
7. Kramer, A.D., Guillory, J.E., Hancock, J.T.: Experimental evidence of massive-
scale emotional contagion through social networks. Proceedings of the National
Academy of Sciences111(24), 8788–8790 (2014)
8. Krasnova, H., Wenninger, H., Widjaja, T., Buxmann, P.: Envy on Facebook: A
Hidden Threat to Users’ Life Satisfaction? In: Wirtschaftsinformatik Proceedings
2013 (2013)
9. Luceri, L., Ye, J., Jiang, J., Ferrara, E.: The susceptibility paradox in online social
influence. In: Proceedings of the International AAAI Conference on Web and Social
Media. vol. 19, pp. 1122–1138 (2025)
10. Lykousas, N., Patsakis, C., Kaltenbrunner, A., Gómez, V.: Sharing Emotions at
Scale: The Vent Dataset. Proceedings of the International AAAI Conference on
Web and Social Media13(01), 611–619 (2019)
11. Sener, B., Akpinar, E., Ataman, M.B.: Unveiling the dynamics of emotions in so-
ciety through an analysis of online social network conversations. Scientific Reports
13(1), 14997 (2023)
12. Smith, C.A., Ellsworth, P.C.: Patterns of cognitive appraisal in emotion. Journal
of Personality and Social Psychology48(4), 813–838 (1985)
13. Tamura, Y., Tsugawa, S., Watabe, K.: Revisiting information diffusion beyond
explicit social ties: A study of implicit-link diffusion on Twitter. Social Network
Analysis and Mining (2026)
14. Xing, R., Sun, B., Zhang, K., Nakov, P., Baldwin, T., Lau, J.H.: An analytical emo-
tionframeworkofrumourthreadsonsocialmedia.arXivpreprintarXiv:2502.16560
(2025)
