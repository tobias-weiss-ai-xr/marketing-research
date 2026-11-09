---
title: Analyzing User Characteristics of Hate Speech Spreaders on Social Media
url: https://arxiv.org/abs/2310.15772
category: social-media
subcategory: empirical
date: 2023-10
venue: ''
authors:
- Dominique Geissler
- Abdurahman Maarouf
- Stefan Feuerriegel
source: arxiv
pdf_url: https://arxiv.org/pdf/2310.15772
pages: 12
chars: 66144
fetched_at: '2026-11-08T13:07:36+00:00'
kb_version: 1
---

# Analyzing User Characteristics of Hate Speech Spreaders on Social Media

Analyzing User Characteristics of Hate Speech Spreaders on
Social Media
Dominique Geissler
LMU Munich & Munich Center for
Machine Learning
Munich, Germany
d.geissler@lmu.de
Abdurahman Maarouf
LMU Munich & Munich Center for
Machine Learning
Munich, Germany
a.maarouf@lmu.de
Stefan Feuerriegel
LMU Munich & Munich Center for
Machine Learning
Munich, Germany
feuerriegel@lmu.de
ABSTRACT
Hate speech on social media threatens the mental and physical
well-being of individuals and contributes to real-world violence.
Resharing is an important driver behind the spread of hate speech
on social media. Yet, little is known aboutwho reshares hate speech
and what their characteristics are. In this paper, we analyze the
role of user characteristics in hate speech resharing across different
types of hate speech (e.g., political hate). For this, we first cluster
hate speech posts using large language models into different types
of hate speech. Then we model the effects of user attributes on users’
probability to reshare hate speech using an explainable machine
learning model. To do so, we apply debiasing to control for selection
bias in our observational social media data and further control for
the latent vulnerability of users to hate speech. We find that, all
else equal, users with fewer followers, fewer friends, fewer posts,
and older accounts share more hate speech. This shows that users
with little social influence tend to share more hate speech. Further,
we find substantial heterogeneity across different types of hate
speech. For example, racist and misogynistic hate is spread mostly
by users with little social influence. In contrast, political anti-Trump
and anti-right-wing hate is reshared by users with larger social
influence. Overall, understanding the factors that drive users to
share hate speech is crucial for detecting individuals at risk of
engaging in harmful behavior and for designing effective mitigation
strategies. Disclaimer: This work contains terms that are offensive
and hateful. to the nature of the work.
CCS CONCEPTS
• Social and professional topics→ User characteristics; • Human-
centered computing→ Social content sharing; Social media;
• Applied computing→ Sociology.
KEYWORDS
hate speech, social media, propensity score, recommender systems,
user characteristics, resharing
1 INTRODUCTION
Online hate speech poses a significant problem to society. Around
one in four U.S. adults has experienced online hate [ 49], and, in
particular, young adults suffer from the psychological consequences
[40]. Hate speech not only threatens users’ mental and physical
well-being but also has the potential to fuel radicalization and incite
Conference’17, July 2017, Washington, DC, USA
2025. ACM ISBN 978-x-xxxx-xxxx-x/YY/MM. . . $15.00
https://doi.org/10.1145/nnnnnnn.nnnnnnn
real-world violence [29], as was the case for the suspect of the 2018
Pittsburgh synagogue shooting [37].
On social media, reshares are vital in disseminating content
beyond immediate circles [45]. One risk of reshares is that harmful
content can go viral, such as propaganda [15], fake news [8, 31, 32,
43], and content from untrustworthy sources [18]. Prior research
found that reshares also make hate speech go disproportionally
more viral than normal content [ 24, 25], which is exploited by
hateful users to reach more people [16].
However, prior work has mostly looked into who posts hate
speech [19, 35] and who is targeted by it [ 11]. Hateful users are
characterized by high activity levels, complex word usage, and
high connectivity among each other [19, 35]. Similarly, targets of
hate speech show high levels of activity, but they also tend to be
older accounts and have more followers [11]. However, no work
has been conducted to profile the users who reshare hate speech,
although reshares help hate speech reach larger audiences and are
an important driver to the virality of hate speech [24]. Hence, in
this work, we analyze the effects of attributes (such as, e.g., verified
status, account age, or number of posts, followers, and friends)
of users who reshare hate speech while taking into account the
different types of hate speech.
Estimating the effects of user attributes on users’ probability
to reshare hate speech is difficult. One challenge is the inherent
selection bias in observational social media click data, which comes
from the users’ self-selection of which content to interact with
as well as the recommendations from online platforms [ 42]. For
example, users only interact with content that they choose and
online platforms only recommend content that they assume a user
is likely to engage with. We later employ inverse propensity scoring
(IPS) [38] to reweight the observed interactions between users and
hate speech posts for debiasing. Another reason is that we have
to control for the varying vulnerability of users to hate speech as
that can cause bias in the estimates of the effects being studied.
Previous research argued that past latent vulnerability (PLV) of a
user to specific content influences both the user attributes and the
probability to reshare [5, 8]. Users may have varying PLV as some
users simply share more hate speech than others. Also, the risk of
exposure to hate speech is different for each user, e.g. how many
times a user has seen hate speech in their feed. In our setting, we
control for PLV to hate speech.
In this work, we analyze the role of user characteristics in hate
speech resharing across different types of hate speech. Our frame-
work follows three steps: 1 We first cluster hate speech posts into
their type using BERTopic [17] and employ automatic cluster label-
ing with LLAMA-3 [26]. This way, we obtain a topic label for each
arXiv:2310.15772v3  [cs.SI]  27 Jan 2025

Conference’17, July 2017, Washington, DC, USA Dominique Geissler, Abdurahman Maarouf, and Stefan Feuerriegel
hate speech post. 2 We then model the past latent vulnerability
of each user to hate speech. For this, we debias the observational
data by adapting inverse propensity scoring (IPS) from causal in-
ference [38]. This reweights the likelihood of users to be exposed
to hate speech [22, 42] and we obtain debiased propensity scores.
We employ the debiased propensity scores to model the debiased
PLV of users to hate speech by learning latent representations in
the form of debiased embeddings. 3 We then model the effects
of user attributes on the probability to reshare hate speech while
controlling for the PLV. Here, we compute the likelihood to reshare
each type of hate speech per user by looking at past reshares. Then,
we model the (non-linear) effects of the user attributes (verified
status, account age, number of posts, followers, and friends) on
the user’s probability to reshare hate speech in the future using an
explainable boosting machine (EBM) [30].1
2 RELATED WORK
2.1 Hate speech on social media
Hate speech is defined as “abusive speech targeting specific group
characteristics, such as ethnic origin, religion, gender, or sexual
orientation” [51]. As such, hate speech expresses animosity against
specific groups and might even call for real-world violence. In gen-
eral, hateful posts tend to go more viral than normal content since
their cascades are larger, live longer, and are of larger structural
virality [24, 25].
One stream of literature conducted content-level analyses. Here
a frequent theme is to develop machine learning models that can
detect and subsequentially remove hate speech. Such systems aim
to detect hate speech, for example by using large language models
[3, 10, 28] or other natural language processing methods [2, 9].
Another stream of literature conducted user-level analyses. Tar-
gets of hate speech tend to be more popular or high-profile users
[11], while users that post hate speech are characterized by higher
social media activity and tend to act in more connected networks
[19, 35]. When looking at hate speech in online political discourse,
people of color of the Democratic Party, white Republicans, and
women in general tend to be the main targets [44].
However, none of the above works analyze resharing of hate
speech. Yet, reshares are what makes content go viral and play a
vital role in the dissemination of hate speech online. Moreover, no
work has been conducted that analyzes who reshares hate speech
and specifically which type of hate speech. This is in contrast to
our work, which aims to answer which user attributes make users
reshare hate speech and specifically the different types of hate
speech.
2.2 Inverse propensity scoring
Click data from observational social media data are subject to se-
lection bias. Specifically, previous research identifies two sources
of selection bias: self-selection by the users and recommendations
from online platforms [42]. On the one hand, users self-select the
content they interact with on social media. On the other hand,
1Codes and data for reproducibility are available via an anonymous reposi-
tory for review and will be available in a public repository upon publica-
tion: https://anonymous.4open.science/r/analyzing_user_characteristics_hatespeech_
spreaders-2042/README.md
online platforms tend to recommend only content to users, that a
user is likely interested in. This means that click data are biased
because the observed interactions were influenced by self-selection
and recommendation bias. Hence, we must carefully account for
selection bias in our observational click data.
To alleviate selection bias in observational click data, previous
works draw upon a popular technique from causal inference, specif-
ically inverse propensity scoring (IPS) [20, 38, 39]. Each hate speech
post is reweighted with its inverse propensity score, i.e. the prob-
ability that a user is exposed to the post. This way, we transform
the observational click data as though it came from a randomized
trial where users are randomly shown items [22, 42]. By doing so,
the selection bias is alleviated and debiased propensity scores are
obtained. Some works have applied IPS to learn and evaluate debi-
ased recommendation models [22, 42]. Others have applied IPS to
debias observational data used to learn users’ fake news resharing
behavior on social media [8]. In particular, the estimated propensity
scores of fake news were debiased in three ways: (a) by using the
popularity of shared fake news items; (b) by using the popularity
of resharing users; or (c) by employing a neural network [8].
In the context of our work, the propensity scores describe the
probability that a user is exposed to hate speech. Here, we also deal
with selection bias of our observational click data. Hence, we later
also adopt the debiased propensity score estimations and integrate
them into our framework for modeling hate speech resharing. This
way, we obtain debiased propensity scores for the exposure of
users to hate speech, which we can use to model debiased, latent
representations of the vulnerability to hate speech.
2.3 Modeling past latent vulnerability
In general, the vulnerability of users to specific online content can-
not be directly observed from data but instead can be represented
by latent embeddings. Previous work modeled PLV through rec-
ommendation algorithms [6]. Recommendation algorithms take
into account previous interactions of users with online content in
order to suggest new content the user is likely to interact with. The
recommendation algorithms are then evaluated by the coherence
of recommendation candidates with past user behavior. This way,
they inherently mimic user behavior [6]. For example, prior work
leveraged recommendation algorithms to model the PLV of users
to fake news, which was used as a confounder to find the attributes
that cause users to reshare fake news online [8]. However, to the
best of our knowledge, no work modeled the PLV of users to hate
speech on social media.
We later transfer the idea of recommendation algorithms to
model the PLV of users to hate speech. In particular, we employ
recommendation algorithms to learn the debiased PLV of users to
hate speech from IPS-reweighted data. By doing so, we represent
the PLV as a debiased embedding.
3 METHODOLOGY
3.1 Overview
Our objective is to model the effects of user attributes 𝐴 on the
users’ probability to reshare different types of hate speech𝑌 while
accounting for the user’s (latent) vulnerability to hate speech 𝑋 .
For this, we use BERTopic to cluster posts into different types of

Analyzing User Characteristics of Hate Speech Spreaders on Social Media Conference’17, July 2017, Washington, DC, USA
hate speech and employ a state-of-the-art, explainable debiasing
framework to model the effects.
Input: We input the interactions of users with hate speech posts
as a bipartite graph into our framework. Let U = {𝑢1,...,𝑢 𝑖}
denote users andH ={ℎ1,...,ℎ 𝑗} denote the hate speech posts.
The interaction between user𝑢∈U and hate speech postℎ∈H
is then a binary variable denoted as𝑆𝑢ℎ ={0, 1}, where𝑆𝑢ℎ = 1 if
user𝑢 shared hate speech postℎ, otherwise𝑆𝑢ℎ = 0.
1 Clustering hate speech: In the first step, we employ BERTopic
[17] combined with HDBSCAN to cluster hate speech posts H.
Subsequently, we label the clusters using automatic labeling with
LLAMA-3 [26]. Hence, we generate clusters of types of hate speech
C ={𝑐1,...,𝑐 𝑛}.
2 Modeling past latent vulnerability: In the next step, we
model the past latent vulnerability𝑋 of users to hate speech. For
this, we first apply IPS reweighting to debias our observational data,
which reweights the propensity𝜋 of hate speech posts to mimic
a randomized trial, and, thereby, we address the issue of selection
bias from above. Then, we model the past latent vulnerability to
hate speech𝑋𝑢 for each user𝑢.
3 Modeling hate speech resharing: In the final step, we
model the effects of user attributes 𝐴 on users’ probability to re-
share hate speech 𝑌 while controlling for PLV 𝑋 . We write the
individual user’s probability to reshare hate speech in general as
outcome variable𝑌𝑢∈[ 0, 1] and the probability to reshare hate
speech type𝑐 as𝑌𝑢𝑐∈[ 0, 1]. Then, we use an explainable boost-
ing machine (EBM) [30] to predict the probability to reshare hate
speech. For each user𝑢 with𝑚 user attributes denoted as vector
𝑎𝑢 =(𝑎1,...,𝑎 𝑚),𝑎𝑢∈ 𝐴 and PLV embedding𝑋𝑢 we model the
probability to reshare hate speech𝑌𝑢 (𝑌𝑢𝑐 for different types of hate
speech𝑐).
3.2 Clustering hate speech (Step 1)
Given hate speech postsH, we employ BERTopic [17], which lever-
ages BERT embeddings and topic modeling, combined with HDB-
SCAN for clustering. First, we remove stop words, URLs, and emojis.
Then, we generate embeddings for each hate speech post using the
pre-trained BERT model all-MiniLM-L6-v2 to capture the seman-
tic content. Next, we reduce the embedding dimensionality using
UMAP to enhance performance and interpretability. Lastly, we ap-
ply HDBSCAN to the reduced embeddings to identify clustersC.
HDBSCAN is highly flexible as it does not require pre-specified
numbers of clusters and it is suitable for noisy data, which makes
it an ideal choice for social media data. In addition, HDBSCAN can
deal well with clusters that vary in shape and size [7].
Subsequently, we label the clusters using automatic labeling us-
ing LLAMA-3 model Llama-3-70b-chat-hf [26]. We generate five
names per cluster and manually pick the most fitting one by ana-
lyzing representative posts. We hereby obtain concise summaries
of the primary themes within each cluster, thus providing clear and
contextually relevant labels.
3.3 Modeling past latent vulnerability (Step 2)
3.3.1 IPS reweighting. Given the usersU, the hate speech postsH,
and the user-hate speech interactions𝑆𝑢ℎ, we apply IPS reweighting
to alleviate selection bias and obtain debiased propensity scores𝜋.
The propensity score describes the probability that a user is exposed
to hate speech.
Assumption: As in [21], we assume that users share posts when
(a) they have been exposed to the post, denoted as binary variable
𝐸𝑢ℎ∈{ 0, 1} (𝐸𝑢ℎ = 1 if user𝑢 was exposed to hate speech post
ℎ,𝐸𝑢ℎ = 0, otherwise), and (b) when they are interested in the
post, denoted as binary variable 𝐼𝑢ℎ∈{ 0, 1} (𝐼𝑢ℎ = 1 if the user
is interested in the post, 𝐼𝑢ℎ = 0, otherwise). We further assume
that resharing of hate speech is missing-not-at-random (MNAR)
[23]. Hence, the probability of user𝑢∈U spreading a hate speech
postℎ∈H is a product of the probability of exposure and the
probability of interestingness of a post [41]. Formally, we have
𝑃(𝑆𝑢ℎ = 1) = 𝑃(𝐸𝑢ℎ = 1) |       {z       }
exposure prob.
· 𝑃(𝐼𝑢ℎ = 1) |      {z      }
interestingness prob.
=𝜃𝑢ℎ·𝜄𝑢ℎ
(1)
for all𝑆𝑢ℎ∈𝑆 and where𝜃𝑢ℎ > 0 is the probability that user𝑢 is
exposed to hate speech postℎ and𝜄𝑢ℎ > 0 is the probability that
user𝑢 is interested in hate speech postℎ. Hence, the question arises
how to compute𝜃𝑢ℎ. Our idea in the following is to leverage the
propensity score𝜋 for that, where the propensity score is defined
as𝜋 =𝑃(𝐸𝑢ℎ = 1). However, the propensity score gives a biased
estimate of𝜃𝑢ℎ due to the observational nature of social media data,
and, instead, we then use a debiased propensity score.
Why the propensity score is a biased estimate of𝜃𝑢ℎ : Simply
computing𝜋 from our data gives a biased estimate for 𝜃𝑢ℎ. The
reason is that, when working with observational click data, we face
two major challenges: First, we only record positive interactions
between users and hate speech posts (i.e., hate speech posts that are
reshared by the user). Negative interactions (i.e., hate speech posts
that were not reshared by the users) arenot recorded. Therefore, we
do not know whether (a) the user was not interested in a given post
or whether (b) the user was not exposed to the post. Second, the
observed interactions are likely subject to selection bias. Users are
more likely to reshare hate speech posts that are more prevalent,
and online platforms are more likely to recommend popular posts
to users. Because of the above, the propensity scores 𝜋 is biased
when computed from observational social media data, i.e.,
𝜋biased =𝑃(𝑆𝑢ℎ = 1| 𝐼𝑢ℎ = 1) ≠𝜃𝑢ℎ (2)
Debiasing the propensity score: Here, we propose to leverage
IPS to learn debiased propensity scores based on the observed social
media data. IPS acts as a reweighting mechanism that assigns larger
weights to hate speech posts that are less likely to be observed,
thereby creating a pseudo-randomized trial where users are shown
posts at random. By doing so, we will later be able to learn debi-
ased embeddings of the past latent vulnerability to hate speech.
Following earlier research [8], we use three different estimation
procedures to obtain unbiased propensity scores:
(1) Virality-based propensity score: This propensity score takes into
account the virality of a hate speech postℎ, i.e.,
𝜋 virality ℎ = ˆ𝜃 virality ℎ =
 ˝
𝑢∈U 𝑆𝑢ℎ
maxℎ∈H
˝
𝑢∈U 𝑆𝑢ℎ
𝜇
, (3)
where we assume that the probability that a user𝑢 is exposed
to a hate speech postℎ is higher if the post has gone more viral
(as measured by the number of reshares in the bipartite graph).

Conference’17, July 2017, Washington, DC, USA Dominique Geissler, Abdurahman Maarouf, and Stefan Feuerriegel
The IPS for rare events could be very high. Hence, we apply a
smoothing operator𝜇 = 0.5 for more stable propensity scores
(see Appendix D for a robustness check with varying𝜇).
(2) Follower-based propensity score: This propensity score takes into
account the virality of the hate speech post ℎ as well as the
popularity of the resharing user𝑢 (as measured as the number
of followers𝐹𝑢). Formally, it is given by
𝜋 follower ℎ = ˆ𝜃 follower 𝑢ℎ =
 ˝
𝑢∈U 𝑆𝑢ℎ·𝐹𝑢
𝑚𝑎𝑥ℎ∈H
˝
𝑢∈U 𝑆𝑢ℎ·𝐹𝑢
𝜇
, (4)
with𝜇 = 0.5. Here, we also account for the bias induced by the
popularity of the user, since popular users are more likely to be
exposed to hate speech [11].
(3) Neural network-based propensity score: This propensity score is
estimated by a neural network via
𝜋 neural ℎ = ˆ𝜃 neural ℎ =𝜎(𝑒ℎ), (5)
where𝑒ℎ is the content of a given hate speech post as learned
by LDA topic modeling and𝜎() is the sigmoid function. This
way, we implicitly encode the hate speech post’s content in the
latent representation.
As a result, we obtain debiased propensity scores. Later, we perform
an ablation study where we compare the three variants (1)–(3) of
our recommendation algorithm to the biased algorithm and find
that the debiased recommendation algorithms perform better.
3.3.2 Modeling past latent vulnerability. To model the past latent
vulnerability (PLV) of users to hate speech (which gives our control
variable𝑋 ), we build upon concepts from recommendation sys-
tems [6]. Thereby, we address one particular difficulty in that both
the interestingness𝐼𝑢ℎ and the exposure 𝐸𝑢ℎ are not observable.
Rather, only the interactions𝑆𝑢ℎ between users and hate speech
posts are observable on social media platforms. Hence, we learn a
recommender algorithm that ranks content according to the inter-
estingness of users simply using the observed interactions.
Recommender algorithm: In our framework, we employ a
Bayesian personalized ranking matrix factorization (BPRMF) [34].
We optimize the parameters in the BPRMF using a pairwise Bayesian
personalized ranking (BPR) loss [34]. By using BPRMF, we address
the challenges of missing negative interactions, since it assumes
that the observed interactions better explain users’ preferences than
unobserved ones and should hence be assigned a higher predictive
score. Since we employ three different ways to debias propensity
scores, we also obtain three different variants of our debiased rec-
ommendation model: BPRMF-V (using𝜋virality); BPRMF-F (using
𝜋follower); and BPRMF-NN (using𝜋neural). In Appendix D we per-
form a robustness check where we compare the performance of our
unbiased recommendation models and the biased recommender. We
find that the recommendation algorithms with debiased propensity
scores are better at predicting the users vulnerability to hate speech.
For each user𝑢, we model PLV to hate speech as a 64-dimensional
embedding𝑋𝑢. For comparison, the base model BPRMF is biased
since it uses𝜋biased as the propensity score.
Loss: Formally, letD =U×H×H be the set of all observed
interactions(𝑢,ℎ) and unobserved interactions(𝑢,𝑔 ), for each pair
(ℎ,𝑔) of hate speech posts, whereℎ ≠𝑔. We model PLV as a per-
sonalized ranking task with a recommendation algorithm from
observed interaction. Based on previous research [41], the ideal loss
of pairwise BPR is:
𝐿ideal( ˆ𝑅) = 1 |D| ∑︁ (𝑢,ℎ,𝑔)∈D 𝜄𝑢ℎ(1−𝜄𝑢𝑔)ℓ( ˆ𝑅𝑢ℎ𝑔), (6)
whereℓ =−ln𝜎(·) is the local loss for the triplet(𝑢,ℎ,𝑔),𝜄𝑢ℎ is the
interestingness of the postℎ for user𝑢, and ˆ𝑅𝑢ℎ𝑔 is the difference
between the predicted scores for hate speech postsℎ and𝑔. However,
the interestingness is unobservable and only the interactions 𝑆𝑢ℎ
are available. BPR then assumes that interacted messages should
be ranked higher than all the other non-interacted messages and
optimizes the following loss function to obtain latent factors:
𝐿BPR( ˆ𝑅) = 1 |D| ∑︁ (𝑢,ℎ,𝑔)∈D 𝑆𝑢ℎ(1−𝑆𝑢𝑔)ℓ( ˆ𝑅𝑢ℎ𝑔). (7)
However, the loss function of the BPR model is biased towards the
ideal pairwise loss, because BPR treats all non-interacted messages
as if the user was not interested in them and does not deal with
messages the user was not exposed to [41]. To deal with the miss-
ing data in implicit feedback , we follow previous research [8] and
employ propensity scores as𝜃𝑢ℎ for the unbiased estimator of the
ideal pairwise loss as follows
𝐿unbiased( ˆ𝑅) = 1 |D| ∑︁ (𝑢,ℎ,𝑔)∈D 𝑆𝑢ℎ 𝜃𝑢ℎ (1−𝑆𝑢𝑔 𝜃𝑢𝑔 )ℓ( ˆ𝑅𝑢ℎ𝑔). (8)
Of note, propensity scores can often become extremely small, e.g.,
hate speech posts with low virality also have low exposure prob-
ability. This leads to large variances in IPS-based approaches. We
reduce the variance by employing a non-negative loss [41] given
by
ˆ𝐿non-neg( ˆ𝑅) = 1 |D| ∑︁ (𝑢,ℎ,𝑔)∈D max{ℓ( ˆ𝑅𝑢ℎ𝑔), 0}. (9)
In addition, we add a𝑙2-regularization for the user embeddings and
post embeddings,𝑈 and𝐻, respectively. The final loss function
is
arg min
𝑈,𝐻
ˆ𝐿non-neg( ˆ𝑅)+ 𝜆(||𝑈|| 2 2+|| 𝐻|| 2 2), (10)
where𝜆 is the weight of the𝑙2-regularization for the latent repre-
sentations.
3.4 Modeling hate speech resharing (Step 3)
3.4.1 Likelihood to reshare hate speech. For each user𝑢, we now
compute the probability to reshare hate speech in general 𝑌𝑢 as
well as the probability to reshare different types of hate speech𝑌𝑢𝑐 .
Formally, we define the user’s probability to reshare hate speech
𝑌𝑢∈[ 0, 1] as
𝑌𝑢 =
𝑛𝑢 hate
𝑛𝑢 hate+𝑛𝑢 normal , (11)
where𝑛𝑢 hate and𝑛𝑢 normal are the number of hate speech posts and
normal posts that user𝑢 shared, respectively.
Similarly, the probability to reshare a specific type of hate speech
𝑌𝑢𝑐∈[ 0, 1] is defined as
𝑌𝑢𝑐 = 𝑛𝑢𝑐 𝑛𝑢 hate+𝑛𝑢 normal , (12)

Analyzing User Characteristics of Hate Speech Spreaders on Social Media Conference’17, July 2017, Washington, DC, USA
where𝑛𝑢𝑐 is the number of hate speech posts that user𝑢 has shared
from cluster𝑐.
3.4.2 Effect estimation. We now model the relationships between
the user attributes 𝐴 and the users’ probability to reshare hate
speech𝑌 while controlling for PLV𝑋 for each user𝑢. We model
the effects using an explainable boosting machine (EBM) [30]. EBM
is a tree-based, cyclic gradient boosting GAM (generalized additive
model) with automatic interaction detection. It provides state-of-
the-art performance while being fully explainable.
In our work, we are interested in understanding the effects of the
following user attributes𝑎∈𝐴: verified (= 1 if the user is verified,
0 otherwise), account age (in days), #posts (number of posts the
user did), #followers, and #friends. Formally, we model
𝑔(𝐸[𝑌𝑢]) =𝛽0+
∑︁
𝑓𝑚(𝑎𝑚)+
∑︁
𝑓(𝑋𝑢), (13)
where𝑔 is the link function that adapts the GAM to the regression
task. For simplicity, we use 𝑌𝑢 in above equation, which can be
replaced by𝑌𝑢𝑐 for each hate speech cluster𝑐∈𝐶. By using EBM
instead of traditional, linear regression [8], we are able to model the
non-linear effects of each user attribute on the users’ probability to
reshare hate speech. Still, our results are explainable in that we can
interpret the estimated effects.
4 EXPERIMENTAL SETUP
4.1 Data
To understand who shares hate speech and which type, we apply
our framework to a comprehensive, state-of-the-art dataset [ 14].
The dataset consists of normal and hate speech posts from the
social media platform X (formerly Twitter) that were human-labeled
following the definitions and procedures described in [14]. For all
posts in the original dataset, we then additionally collected the
corresponding reshares. As a result, our augmented dataset consists
of 25,196 root posts (96.05% normal and 3.95% hateful posts) from
31,905 users. The root posts received𝑁 = 65,920 reshares by 61,961
users, out of which 43,929 (66.64%) were reshares of normal root
posts and 21,991 (33.36%) were reshares of hateful root posts. As
such, hateful root posts were reshared disproportionally often.
Model variables: We analyze the effects of five user attributes
on the probability to reshare: 𝒂1: verified (= 1 if the user is verified,
0 otherwise); 𝒂2: account age (in days); 𝒂3: #post (number of posts
by the user); 𝒂4: #follower (number of followers of the user); and𝒂5:
#friend (number of friends of the user). The distributions of #post,
#follower, and #friend are highly right-skewed, because of which
we log these user attributes. Appendix Table 3 shows summary
statistics for the different user attributes.
Ethical statement: Data collection was conducted by follow-
ing standards for ethical research [36]. Our analyses are based on
publicly available data, and we only report aggregated results. We
respect users’ privacy by not publishing usernames and do not
attempt to track or de-identify users who decided to remain anony-
mous. We have received ethical approval by our ethics committee
(=IRB) at the University of (anonymized). The approval number is
(anonymized).
4.2 Baselines
In this work, we leverage a debiasing framework to model the ef-
fects of user attributes on users’ probability to reshare hate speech
using an EBM. We refer to our framework as DF-EBM. Note that,
for benchmarking, our setting requires baselines that provide ex-
plainable results since we aim to provide an understanding of the
user attributes that make users reshare hate speech. To the best
of our knowledge, we are aware of only one benchmark where
the effects of user attributes on the probability to reshare content
were modeled: (1) DF-linear [8] performs debiasing but, in contrast
to our framework, is fully linear. Formally, instead of allowing for
non-linear relationships in step 3 , DF-linear models linear effects
of user attributes on the probability to reshare content. It is thus
explainable as it outputs coefficients for each user attribute, but
it cannot capture non-linearities and is thus not flexible since the
modeled effects are assumed to be linear.
In addition, we design the following variants of our debiasing
framework that we also use as baselines: (2) DF-ExNN where we
replace the EBM with an explainable neural network [53]. The ex-
plainable neural network enhances the explainability of a vanilla
neural network by adding architecture constraints, which is to
achieve a balance between prediction performance and model ex-
plainability. (3) DF-NAM where we replace the EBM with a neural
additive model [1], which learns a linear combination of neural
networks that each attend to a single input feature. This way, it
remains explainable while being able to model non-linear effects.
4.3 Implementation details
We implemented our framework in Python 3.8. For the hate speech
clustering, we use BERTopic model all-MiniLM-L6-v2 [17] to gen-
erate embeddings and UMAP to reduce the embeddings into a
seven-dimensional space. To cluster, we use HDBSCAN with a min-
imum cluster size of 10. We name the resulting cluster with the
LLAMA-3 model Llama-3-70b-chat-hf [26]. To model the effects, we
use the EBMRegressor of InterpretML [30]. We allow for ten inter-
actions in the EBM model and run it for a maximum of 5,000 rounds.
Moreover, we performed hyperparameter tuning (see Appendix B).
For evaluation, we split our dataset into train/test set (80/20). To
evaluate the performance of the entire framework (step 3 ), we use
the root mean squared error (RMSE). We average the performance
of the EBMRegressor as well as our baselines over five runs. To
model PLV, we use BPRMF [34]. We set the learning rate of our
BPRMF model to 0.001, the batch size to 64, and the embedding
size to 64. We average the performance over five runs with varying
train/test splits. For the IPS reweighting with𝜋𝑛𝑒𝑢𝑟𝑎𝑙 ℎ , we employ
linear discriminant analysis (LDA) topic modeling2 to get a latent
representation𝑒ℎ of the topics in the posts.
5 RESULTS
5.1 Hate speech cluster
We begin by reporting the hate speech clusters resulting from our
topic modeling. We cluster the 270 hate speech root posts into four
clusters, which we labeled automatically. The optimal number of
2https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.
LinearDiscriminantAnalysis.html

Conference’17, July 2017, Washington, DC, USA Dominique Geissler, Abdurahman Maarouf, and Stefan Feuerriegel
clusters is determined automatically by HDBSCAN, which allows
us more flexibility since we do not have to determine the number
of clusters beforehand [7].
The largest cluster contains 123 posts and got the label “racist
and misogynistic rants”. The posts in this cluster received a total of
15.219 reshares and mostly contained racial and misogynistic slurs
as well as angry, abusive, and offensive language. The second cluster
contains 93 posts with “anti-Trump and anti-right wing rants” and
received 6.207 reshares. The posts share political hate, specifically
discriminating against Trump and right-wing politics. The third
cluster contains 36 hate speech posts with the label “toxic rants”
and received 512 reshares. These posts are hateful and offensive in
general and do not have a common group that is being targeted. The
last cluster contains only 16 posts with the label “social media noise”.
The posts in this cluster are mostly spam and received 51 reshares.
Together, this shows that most of the reshares in our dataset are
racial and misogynistic hate, hate against Trump and right-wing
politicians, as well as general hateful comments. Appendix C shows
the characteristic words and example posts for each cluster.
Model Explainable Flexible RMSE
DF-linear
 0.0885
DF-ExNN
 0.0911
DF-NAM
 0.1342
0.0863DF-EBM (ours)
 (−2.5%)
Table 1: Performance comparison (measured by the RMSE)
for predicting users’ probability to reshare hate speech. Our
debiasing framework performs best (relative improvement
of 2.5% over the best baseline, whereby DF-linear is the only
baseline that we are aware of in the literature).
5.2 Performance comparison
We next report the performance of our framework when predicting
the effects of user attributes on the users’ probability to reshare
hate speech. We compare our framework against multiple baselines
based on the RMSE (root mean squared error). To the best of our
knowledge, there is only one baseline in the literature: DF-linear
[8], which builds upon a linear approach and thus can not account
for non-linearites. All of the baselines as well as our model are
explainable since we aim to provide an understanding of the user
attributes that make users reshare hate speech.
Table 1 shows the RMSE for each variant of our framework. Our
debiasing framework DF-EBM outperforms the DF-linear baseline
with a relative improvement of 2.5%. The improvement is statis-
tically significant according to Welch’s𝑡-test [52] at a𝑝 < 0.001
level. Importantly, both frameworks have access to identical data so
the performance gain must be attributed solely to the flexibility of
our framework in capturing nonlinearities. Moreover, ourDF-EBM
also outperforms the other custom baselines that are non-linear.
Here, the Welch’s𝑡-tests [52] are again statistically significant at
the𝑝 < 0.01 level. Together, this demonstrates that our debasing
framework DF-EBM is superior.
5.3 Analyzing hate speech resharing
We now leverage the explainability of our framework to understand
which user attributes affect the users’ probability to reshare hate
speech. For this, we analyzed the effects of users’ verified status,
account age, number of posts, number of followers, and number
of friends. We first look at the feature importance for each user at-
tribute, which is computed as the average absolute predicted value
of each feature for the training set (i.e., for each feature, we predict
the absolute value for each sample in the training set and then aver-
age these scores). This is weighted by the relative frequency of each
feature in the train set. Here, we find that the number of posts is the
most influential user attribute when predicting users’ probability
to reshare hate speech (see Figure 1). Moreover, the second most
influential attribute is the number of followers. Thereby, we add
to the literature where the popularity of a user and their activity
level are important indicators as to whether they post hate speech
[19, 35], whereas we show that the number of posts and followers
also cause a larger propensity to reshare hate speech.
We next look at the effects of each user attribute on the probabil-
ity to reshare hate speech. Figure 2 shows the contribution of each
user attribute. The contribution is shown on the same scale as the
output variable, and the graph is normalized so that the average
prediction is at 0. For example, a score of−0.1 at an account age of
100 days would mean that a user with a 100-day-old account is 10
percentage points less likely to reshare hate speech than the aver-
age prediction. Overall, we find that users with fewer posts, fewer
followers, and fewer friends are more likely to reshare hate speech.
In return, newer accounts are less likely to do so. Moreover, we
find that verified users are 0.016 (±0.004) percentage points more
likely to reshare hate speech than the average prediction, which
is contrary to our expectations that a verified status is typically
linked to users with a large reputation who should thus engage
less with hate speech. We further perform a comparison of PLV to
hate speech and PLV to normal content (see Appendix E for the
complete analysis).
YHULILHG DFFRXQWDJH SRVWV IROORZHUV IULHQGV









Figure 1: Feature importance of the user attributes when
predicting the users’ probability to reshare hate speech.
5.4 Resharing of types of hate speech
We now split the hate speech posts into their respective types and
analyze the resharing for each type separately. Here, we look at
the effects of users’ verified status, account age, number of posts,
followers, and friends on the resharing behavior. Similar to above,
the contribution of each user attribute is shown on the same scale
as the output variable.

Analyzing User Characteristics of Hate Speech Spreaders on Social Media Conference’17, July 2017, Washington, DC, USA
     
DFFRXQWDJH








6FRUH
(a) account age
      
SRVWV






6FRUH (b) #posts (in log scale)
       
IROORZHUV






6FRUH (c) #followers (in log scale)
     
IULHQGV








6FRUH (d) #friends (in log scale)
Figure 2: Contributions of the user attributes to the users’ probability to reshare hate speech as estimated by our debiasing
framework (both y-axis and outcome 𝑌 are shown on the same scale). Each graph is normalized for better comparability such
that the average prediction on the train set is at 0. The blue curve shows the predicted effect, while the orange curves show the
upper and lower bounds of our model.
For “racial and misogynistic rants”, we find that newer accounts,
accounts with fewer posts, and accounts with fewer friends tend to
share more racist and misogynistic rants (see Figure 3). At the same
time, users with very few or a lot of followers share less racist and
misogynistic rants. Verified users are 0.083 (±0.0002) percentage
points less likely to reshare racist and misogynistic rants. These
findings are in part similar to overall hate sharing, where users with
fewer posts and friends also tend to share more hate in general.
When looking at “anti-Trump and anti-right wing rants”, we find
opposite effects to racial and misogynistic rants: newer accounts,
users with fewer posts, and users with fewer friends share less
anti-Trump hate (see Figure 4). Also the contribution curve for the
number of followers is reversed, where now users with very few or
a lot of followers share less anti-Trump hate. Moreover, the effect of
verified status is reversed with verified users being 0.075 (±0.0002)
percentage points more likely to reshare anti-Trump hate.
For “toxic rants”, we find similar trends to anti-Trump hate re-
sharing: younger accounts and users with fewer posts also share
less toxic rants (see Figure 5). The effects for the number of fol-
lowers and friends are different in that users with fewer followers
share less toxic rants and users with very few or a lot of friends
share more toxic rants. Verified users are 0.001 (±0.000) percentage
points less likely to reshare toxic rants.
5.5 Ablation study
We performed an ablation study to analyze the differences in per-
formance when using different inputs to the past latent vulnera-
bility (PLV). In particular, we compare four different inputs: (1) a
base model where we do not control for PLV; (2) BPRMF-V model
with the virality-based PLV using𝑃virality; (3) BPRMF-F with the
follower-based PLV using 𝑃follower; and (4) BPRMF-NN with the
neural network-based PLV using𝑃neural. Table 2 shows the RMSE
for the five different inputs. Overall, all models that control for PLV
outperform the base model that does not control for it, although we
do not see a performance gain that is statistically significant based
on Welch’s𝑡-test at the𝑝 < 0.05 level. In sum, the ablation study
confirms the effectiveness of IPS reweighting for modeling PLV. In
the following experiments, we will use the debiasing framework
with the virality-based PLV.
UserModel attributes PLV RMSE
Base
 — 0.0866
BPRMF-V
 Virality-based propensity 0.0863
BPRMF-F
 Follower-based propensity 0.0864
BPRMF-NN
 NN-based propensity 0.0865
Table 2: Ablation study using different inputs for the past
latent vulnerability. Results are averaged over 5 runs.
6 DISCUSSION
Summary of findings: In our paper, we show the effects of user
attributes on hate speech resharing while controlling for the past
latent vulnerability of a user to hate speech. We find that users
with fewer posts, fewer followers, and fewer friends tend to reshare
more hate speech and newer accounts tend to reshare less. When
splitting hate speech into different types, we find that racist and
misogynistic rants are spread mostly by newer accounts, accounts
with fewer posts, accounts with fewer friends, and accounts with
a moderate number of friends. In return, political anti-Trump and
anti-right-wing rants are reshared by older accounts, accounts with
a moderate number of posts, and accounts with many followers and
friends. Toxic rants are also shared by older accounts and accounts
with a large number of posts, followers, and friends.
Interpretation: A possible explanation for our findings might
be the concept of social influence. Social influence is one of the
most important determinants in explaining the spread of informa-
tion on social media [54]. Users with many followers tend to have
more social influence, and, therefore, their posts reach a large au-
dience [24, 33, 46, 50, 54]. Similarly, verified users are perceived to
have more credibility online [ 27] and, hence, have higher social
influence. Users with a large social influence (e.g. verified, older
accounts, more posts, more friends, and more followers) might be
more concerned about having a positive image [47], resulting in a
lower probability to reshare harmful content in general.
When looking at the different types of hate speech, we make
the interesting observation that the dynamics behind the of spread
racial and misogynistic hate and political hate differ. Users with
little social influence tend to spread more racial and misogynistic
hate while users with high social influence tend to spread political
hate. This might be the case because racial and misogynistic hate
is socially unacceptable and circulates primarily in small online

Conference’17, July 2017, Washington, DC, USA Dominique Geissler, Abdurahman Maarouf, and Stefan Feuerriegel
     
DFFRXQWDJH






6FRUH
(a) account age
      
SRVWV





6FRUH (b) #posts (in log scale)
       
IROORZHUV









6FRUH (c) #followers (in log scale)
     
IULHQGV









6FRUH (d) #friends (in log scale)
Figure 3: Contributions of the user attributes to the users’ probability to reshare racist and misogynistic rants as estimated
by our debiasing framework (both y-axis and outcome 𝑌 are shown on the same scale). Each graph is normalized for better
comparability such that the average prediction on the train set is at 0. The blue curve shows the predicted effect, while the
orange curves show the upper and lower bounds of our model.
     
DFFRXQWDJH





6FRUH
(a) account age
      
SRVWV





6FRUH (b) #posts (in log scale)
       
IROORZHUV









6FRUH (c) #followers (in log scale)
     
IULHQGV







6FRUH (d) #friends (in log scale)
Figure 4: Contributions of the user attributes to the users’ probability to reshare anti-Trump and anti-right wing rants as
estimated by our debiasing framework (both y-axis and outcome 𝑌 are shown on the same scale). Each graph is normalized for
better comparability such that the average prediction on the train set is at 0. The blue curve shows the predicted effect, while
the orange curves show the upper and lower bounds of our model.
     
DFFRXQWDJH








6FRUH
(a) account age
      
SRVWV







6FRUH (b) #posts (in log scale)
       
IROORZHUV





6FRUH (c) #followers (in log scale)
     
IULHQGV




6FRUH (d) #friends (in log scale)
Figure 5: Contributions of the user attributes to the users’ probability to reshare toxic rants as estimated by our debiasing
framework (both y-axis and outcome 𝑌 are shown on the same scale). Each graph is normalized for better comparability such
that the average prediction on the train set is at 0. The blue curve shows the predicted effect, while the orange curves show the
upper and lower bounds of our model.
communities where extreme views are normalized and users do not
have to fear backlash for resharing. In return, the political landscape
is widely discussed online and political hate might border what is
still deemed acceptable to express online or is harder to detect for
moderation efforts.
Relevance: Regulatory initiatives in many countries around the
world (e.g., the Digital Services Act in the European Union) compel
social media platforms to limit the spread of online hate speech.
In this regard, our framework helps platform providers identify
which user attributes make users reshare hate speech. This allows
for the adoption of a user-centric design approach when devel-
oping targeted and data-driven mitigation strategies. By tailoring
interventions to address the roots of hate speech resharing, we can
implement more effective measures to prevent users from sharing
hate speech and, thereby, counter its spread.
Implications: Our framework shows the influences of user
attributes on the probability to reshare hate speech and therefore
generates insights on how to take action against the resharing
of hate speech. For example, online platforms might consider not
showing the popularity of a user by removing follower counts from
the profile information. This way, users are unaware of how many
people see their posts, which might lead them to be more selective
in the content they share.
Platforms could also vary their moderation measures depending
on the user’s follower count, e.g., decrease the response times to re-
ports against hate speech from popular users. However, this would
require a shift in resources and could raise ethical considerations

Analyzing User Characteristics of Hate Speech Spreaders on Social Media Conference’17, July 2017, Washington, DC, USA
about the uneven moderation of users. Given the positive effects of
a verified status on hate speech resharing, online platforms might
also consider removing the verified status. This might lead to users
being more responsible in the content they reshare.
Conclusion: In this work, we leverage a state-of-the-art debias-
ing framework to model the effects of user attributes on the proba-
bility to reshare hate speech while controlling for the past latent
vulnerability to hate speech. Our framework provides flexible and
explainable results while achieving state-of-the-art performance.
We also cluster hate speech into its multiple types, which allows us
to model the resharing dynamics individually.
AUTHOR CONTRIBUTIONS
All authors contributed to conceptualization, results interpretation,
and manuscript writing. First author contributed to data analysis.
All authors approved the manuscript.
REFERENCES
[1] Rishabh Agarwal, Levi Melnick, Nicholas Frosst, Xuezhou Zhang, Ben Lengerich,
Rich Caruana, and Geoffrey E. Hinton. 2021. Neural additive models: Interpretable
machine learning with neural nets. NeurIPS (2021).
[2] Pinkesh Badjatiya, Shashank Gupta, Manish Gupta, and Vasudeva Varma. 2017.
Deep learning for hate speech detection in tweets. WWW Companion (2017).
[3] Francesco Barbieri, Jose Camacho-Collados, Luis Espinosa Anke, and Leonardo
Neves. 2020. TweetEval: Unified benchmark and comparative evaluation for
tweet classification. EMNLP (2020).
[4] Matthew Beatty. 2020. Classification methods for hate speech diffusion: Detecting
the spread of hate speech on Twitter. Congress on Electrical Engineering and
Computer Systems (2020).
[5] Fabrício Benevenuto, Tiago Rodrigues, Meeyoung Cha, and Virgílio Almeida. 2009.
Characterizing user behavior in online social networks. Internet Measurement
Conference (2009).
[6] Stephen Bonner and Flavian Vasile. 2018. Causal embeddings for recommendation.
RecSys (2018).
[7] Campello, Ricardo J. G. B., Davoud Moulavi, and Joerg Sander. 2013. Density-
based clustering based on hierarchical density estimates. PAKDD (2013).
[8] Lu Cheng, Ruocheng Guo, Kai Shu, and Huan Liu. 2021. Causal understanding
of fake news dissemination on social media. KDD (2021).
[9] Thomas Davidson, Dana Warmsley, Michael Macy, and Ingmar Weber. 2017.
Automated hate speech detection and the problem of offensive language. ICWSM
(2017).
[10] Nemanja Djuric, Jing Zhou, Robin Morris, Mihajlo Grbovic, Vladan Radosavl-
jevic, and Narayan Bhamidipati. 2015. Hate speech detection with comment
embeddings. WWW Companion (2015).
[11] Mai ElSherief, Shirin Nilizadeh, Dana Nguyen, Giovanni Vigna, and Elizabeth
Belding. 2018. Peer to peer hate: Hate speech instigators and their targets.ICWSM
(2018).
[12] Martin Ester, Hans-Peter Kriegel, Jörg Sander, and Xiaowei Xu. 1996. A density-
based algorithm for discovering clusters in large spatial databases with noise.
KDD (1996).
[13] Bojan Evkoski, Andraž Pelicon, Igor Mozetič, Nikola Ljubešić, and Petra Kralj
Novak. 2022. Retweet communities reveal the main sources of hate speech. PLOS
ONE 17, 3 (2022), e0265602.
[14] Antigoni Founta, Constantinos Djouvas, Despoina Chatzakou, Ilias Leontiadis,
Jeremy Blackburn, Gianluca Stringhini, Athena Vakali, Michael Sirivianos, and
Nicolas Kourtellis. 2018. Large scale crowdsourcing and characterization of
Twitter abusive behavior. ICWSM (2018).
[15] Dominique Geissler, Dominik Bär, Nicolas Pröllochs, and Stefan Feuerriegel. 2023.
Russian propaganda on social media during the 2022 invasion of Ukraine. EPJ
Data Science 12 (2023).
[16] Vasu Goel, Dhruv Sahnan, Subhabrata Dutta, Anil Bandhakavi, and Tanmoy
Chakraborty. 2023. Hatemongers ride on echo chambers to escalate hate speech
diffusion. PNAS Nexus 2, 3 (2023), pgad041.
[17] Maarten Grootendorst. 2022. BERTopic: Neural topic modeling with a class-based
TF-IDF procedure. (2022). arXiv:2203.05794
[18] Andrew M. Guess, Neil Malhotra, Jennifer Pan, Pablo Barberá, Hunt Allcott,
Taylor Brown, Adriana Crespo-Tenorio, Drew Dimmery, Deen Freelon, Matthew
Gentzkow, Sandra González-Bailón, Edward Kennedy, Young Mie Kim, David
Lazer, Devra Moehler, Brendan Nyhan, Carlos Velasco Rivera, Jaime Settle,
Daniel Robert Thomas, Emily Thorson, Rebekah Tromble, Arjun Wilkins, Mag-
dalena Wojcieszak, Beixian Xiong, Chad Kiewiet de Jonge, Annie Franco, Winter
Mason, Natalie Jomini Stroud, and Joshua A. Tucker. 2023. Reshares on social
media amplify political news but do not detectably affect beliefs or opinions.
Science 381, 6656 (2023), 404–408.
[19] Yiping Hua, Mor Naaman, and Thomas Ristenpart. 2020. Characterizing Twitter
users who engage in adversarial interactions against political candidates. CHI
(2020).
[20] Guido Imbens and Donald B. Rubin. 2015. Causal inference for statistics, social,
and biomedical sciences: An introduction . Cambridge University Press.
[21] Thorsten Joachims, Adith Swaminathan, and Tobias Schnabel. 2017. Unbiased
learning-to-rank with biased feedback. WSDM (2017), 781–789.
[22] Dawen Liang, Laurent Charlin, and David M. Blei. 2016. Causal inference for
recommendation. Causation: Foundation to Application Workshop at UAI (2016).
[23] Roderick J. A. Little and Donald B. Rubin. 2020. Statistical analysis with missing
data. Wiley.
[24] Abdurahman Maarouf, Nicolas Pröllochs, and Stefan Feuerriegel. 2024. The
virality of hate speech on social media. CSCW (2024).
[25] Binny Mathew, Ritam Dutt, Pawan Goyal, and Animesh Mukherjee. 2019. Spread
of hate speech in online social media. WebSci (2019).
[26] Meta. 2024. Llama 3. (2024). https://github.com/meta-llama/llama3
[27] Meredith Ringel Morris, Scott Counts, Asta Roseway, Aaron Hoff, and Julia
Schwarz. 2012. Tweeting is believing? CSCW (2012).
[28] Marzieh Mozafari, Reza Farahbakhsh, and Noël Crespi. 2019. A BERT-based
transfer learning approach for hate speech detection in online social media.
International Conference on Complex Networks and their Applications (2019).
[29] Karsten Müller and Carlo Schwarz. 2021. Fanning the flames of hate: Social
media and hate crime. Journal of the European Economic Association 19, 4 (2021),
2131–2167.
[30] Harsha Nori, Samuel Jenkins, Paul Koch, and Rich Caruana. 2019. InterpretML: A
unified framework for machine learning interpretability. (2019). arXiv:1909.09223
[31] Nicolas Pröllochs, Dominik Bär, and Stefan Feuerriegel. 2021. Emotions explain
differences in the diffusion of true vs. false social media rumors. Sci Rep 11, 1
(2021), 22721.
[32] Nicolas Pröllochs, Dominik Bär, and Stefan Feuerriegel. 2021. Emotions in online
rumor diffusion. EPJ Data Science 10 (2021).
[33] Nicolas Pröllochs and Stefan Feuerriegel. 2023. Mechanisms of true and false
rumor sharing in social media: Collective intelligence or herd behavior? CSCW
(2023).
[34] Steffen Rendle, Christoph Freudenthaler, Zeno Gantner, and Lars Schmidt-Thieme.
2009. BPR: Bayesian personalized ranking from implicit feedback. UAI (2009).
[35] Manoel Horta Ribeiro, Pedro H. Calais, Yuri A. Santos, Virgílio A. F. Almeida, and
Wagner Meira Jr. 2018. Characterizing and detecting hateful users on Twitter.
ICWSM (2018).
[36] Caitlin M. Rivers and Bryan L. Lewis. 2014. Ethical research standards in a world
of big data. F1000Research 3 (2014), 38.
[37] Kevin Roose. 2018. On Gab, an extremist-friendly site, Pittsburgh shooting
suspect aired his hatred in full. The New York Times (2018). https://www.nytimes.
com/2018/10/28/us/gab-robert-bowers-pittsburgh-synagogue-shootings.html
[38] Paul R. Rosenbaum and Donald B. Rubin. 1983. The central role of the propensity
score in observational studies for causal effects. Biometrika 70, 1 (1983), 41–55.
[39] Donald B. Rubin. 2001. Using propensity scores to help design observational
studies: Application to the tobacco litigation.Health Services & Outcomes Research
Methodology 2 (2001), 169–188.
[40] Koustuv Saha, Eshwar Chandrasekharan, and Munmun de Choudhury. 2019.
Prevalence and psychological effects of hateful speech in online college commu-
nities. WebSci (2019).
[41] Yuta Saito. 2020. Unbiased pairwise learning from biased implicit feedback.
International Conference on Theory of Information Retrieval (2020), 5–12.
[42] Tobias Schnabel, Adith Swaminathan, Ashudeep Singh, Navin Chandak, and
Thorsten Joachims. 2016. Recommendations as treatments: Debiasing learning
and evaluation. ICML (2016).
[43] Chengcheng Shao, Giovanni Luca Ciampaglia, Onur Varol, Kai-Cheng Yang,
Alessandro Flammini, and Filippo Menczer. 2018. The spread of low-credibility
content by social bots. Nature Communications 9, 1 (2018), 4787.
[44] Kirill Solovev and Nicolas Pröllochs. 2022. Hate speech in the political discourse
on social media: Disparities across parties, gender, and ethnicity. WWW (2022).
[45] Karthik Subbian, B. Aditya Prakash, and Lada Adamic. 2017. Detecting large
reshare cascades in social networks. WWW (2017), 597–605.
[46] Bongwon Suh, Lichan Hong, Peter Pirolli, and Ed H. Chi. 2010. Want to be
retweeted? Large scale analytics on factors impacting retweet in Twitter network.
International Conference on Social Computing (2010).
[47] Shalini Talwar, Amandeep Dhir, Puneet Kaur, Nida Zafar, and Melfi Alrasheedy.
2019. Why do people share fake news? Associations between the dark side of
social media use and fake news sharing behavior. 51 (2019), 72–82.
[48] Laurens van der Maaten and Geoffrey Hinton. 2008. Visualizing data using t-SNE.
JMLR (2008), 2579–2605.
[49] Emily A. Vogels. 2021. The state of online harassment. Pew Research Center
(2021). https://www.pewresearch.org/internet/2021/01/13/the-state-of-online-
harassment/

Conference’17, July 2017, Washington, DC, USA Dominique Geissler, Abdurahman Maarouf, and Stefan Feuerriegel
[50] Soroush Vosoughi, Deb Roy, and Sinan Aral. 2018. The spread of true and false
news online. Science 359, 6380 (2018), 1146–1151.
[51] William Warner and Julia Hirschberg. 2012. Detecting hate speech on the world
wide web. Workshop on Language in Social Media at ACL (2012), 19–26.
[52] Bernard Lewis Welch. 1947. The generalisation of student’s problems when
several different population variances are involved. Biometrika 34, 1-2 (1947),
28–35.
[53] Zebin Yang, Aijun Zhang, and Agus Sudjianto. 2020. Enhancing explainability of
neural networks through architecture constraints. IEEE Transactions on Neural
Networks and Learning Systems (2020).
[54] Tauhid Zaman, Emily B. Fox, and Eric T. Bradlow. 2014. A Bayesian approach for
predicting the popularity of tweets. The Annals of Applied Statistics 8, 3 (2014),
1583–1611.
A STATISTICS OF USER ATTRIBUTES
In our work, we estimate the effects of five user attributes on the
probability to reshare: verified (= 1 if the user is verified, 0 other-
wise); account age (in days); #post (number of posts by the user);
#follower (number of followers of the user); and #friend (number of
friends of the user). The below Table 3 shows the summary statistics
of the user attributes.
User attributes Mean Median Std. dev.
verified 0.003 0 0.05
account age (in days) 3663.74 3585 833.51
#post 57588.09 24465.5 106129.73
#follower 2230.27 546 33567.04
#friend 1253.2 491 3639.85
Table 3: Summary statistics of the user attributes.
B HYPERPARAMETER TUNING
Hyperparameters are tuned via cross-validation with a 70/30 split.
Table 4 shows the list of hyperparameters of DF-EBM. We fine-
tuned the DF-EBM with the BPRMF-V confounder and applied the
best-performing parameters to all our variants of DF-EBM model.
As a result, we set the learning rate to 0.01, the number of maximum
bin to 512, and the minimum sample leaf to 3.
Model Hyperparameter Search range
Learning rate 0.1, 0.01, 0.001
Maximum bins 128, 256, 512 DF-EBM
Minimum sample leaf 1, 2, 3
Table 4: Hyperparameters and search ranges for DF-EBM.
C INSIGHTS INTO THE DIFFERENT TYPES OF
HATE SPEECH
We cluster 270 hate speech root posts into four types using unsu-
pervised machine learning and automatically label them using a
large language model. Table 5 shows the accumulative number of
reshares for posts in each cluster as well as the top-10 character-
istics words in each cluster. We observe that clusters “Racist and
misogynistic rants”, “Anti-Trump and anti-right wing rants”, and
“Toxic rants” contain a multitude of offensive and swear words as
characteristics words while the smallest cluster of social media
noise does not. Moreover, Table 6 shows example posts from each
cluster.
D ROBUSTNESS CHECKS
Modeling past latent vulnerability: We perform a robustness
check to validate our choice of how we model the past latent vul-
nerability (PLV). Recall that we model PLV using the recommenda-
tion algorithm BPRMF. However, we have multiple ways to debias
propensity scores, implying that we can use multiple inputs to the
BPRMF model. Here, we check the prediction performance of the
BPRMF with different propensity score inputs. We measure the
prediction performance using recall@𝑘 and NDCG@𝑘. The former

Analyzing User Characteristics of Hate Speech Spreaders on Social Media Conference’17, July 2017, Washington, DC, USA
Hate speech cluster Reshares Characteristic words
Racist and
misogynistic rants
15.219 hate, niggas, nigga, dont, yall, like, ass, ugly,
bitch, fucking
Anti-Trump and
anti-right wing rants
6.207 idiot, trump, isis, idiots, syria, says, attack,
obama, war, run
Toxic rants 512 dont, women, fucking, brutal, disgusting,
life, white, just, bad, lifequotes
Social media noise 51 summer, tomorrow, selby, model, focus,
views, hes, make, time, just
Table 5: Number of reshares and characteristic words of each
hate speech cluster defined as the top-10 words with regard
to c-TF-IDF weighting.
Hate speech cluster Example posts
Racist and
misogynistic rants
•“I understand why niggas dont wanna be in relationships
girls annoying af ”
•“I hate Niggaas that act like bitches ”
•“RT if you still hate this nigga ”
Anti-Trump and
anti-right wing rants
•“Join us today on the DC mall for Pussy March 2 against evil
fascist dictator Drumpf. #RESISTANCE #NOTMYPRESIDENT
#IMWITHHER”
•“Breathtaking.....making money from the Presidency and
his idiot supporters don’t see a problem.... ”
•“RT if you’re sick of these Nazis #trumprussia ”
Toxic rants •“Dasani water is fucking disgusting and if you don’t agree I
literally can’t even with you ”
•“I wanna beat his ass so bad ”
•“People are dumb af in these Jurassic Park movies! Just
screaming knowing damn well not to because it attracts at-
tention!!”
Social media noise •“They’ve booked shows for Efe even when he’s still in the
house.And some idiot who’s just model in payporte said he’s
talentless #BBNaija”
•“Last day to make this a reality- Don’t be fooled by the
countdown, every donation still makes a HUGE difference! ”
•“Lovely little cove, time for some holiday painting @USER
you would be proud! ”
Table 6: Example posts from each hate speech cluster
measures how many of the predicted posts were interesting to the
user out of those that the model predicted to be interesting as the
top-𝑘 posts. The latter measures the accuracy of the prediction
by comparing the ground-truth interestingness to the predicted
ranking of posts for the top-𝑘 ranked posts. This way, we can get
an estimate of how well the recommendation algorithm was able
to model PLV for each user.
Table 7 shows the prediction performance of BPRMF with dif-
ferent inputs. We find that the BPRMF algorithms with debiased
propensity scores are better at predicting hate speech that the user
is vulnerable to. This confirms our choice to employ IPS reweighting
in our debiasing framework when modeling PLV.
Robustness check for smoothing operatorIn IPS for reweight-
ing observational social media data, the IPS for rare events could be
very high. A smoothing operator can lead to more stable propensity
scores and prevent overfitting. In this work, 𝜇 is the smoothing
operator. We chose𝜇 = 0.5 since popularity-related measures fol-
low a power law distribution, i.e., 𝜇 ≤ 1. We performed a new
robustness check to study the sensitivity of the recommendation
recall@𝑘
Model 𝑘 = 20 𝑘 = 40 𝑘 = 60 𝑘 = 80
BPRMF 19.35 30.90 36.20 40.17
BPRMF-V 18.02 31.18 36.76 40.69
BPRMF-F 19.48 32.11 * 37.92* 42.16*
BPRMF-NN 19.23 31.16 36.62 40.80
(a) Performance evaluated based on recall@𝑘
NDCG@𝑘
Model 𝑘 = 20 𝑘 = 40 𝑘 = 60 𝑘 = 80
BPRMF 7.02 9.39 10.33 10.97
BPRMF-V 6.67 9.37 10.36 11.00
BPRMF-F 7.04 9.63 10.66 11.35 *
BPRMF-NN 6.82 9.27 10.24 10.92
(b) Performance evaluated based on NDCG@𝑘
Table 7: Comparison of the prediction performance (mea-
sured in recall@𝑘 and NDCG@𝑘) of BPRMF when modeling
PLV with different propensity score inputs. An asterisk * in-
dicates that the improvement measured with Welch’s 𝑡-test
[52] is statistically significant at 𝑝 < 0.05 level.
algorithm with𝜇 =[0.1, 0.5, 1.0] for the virality and the follower-
based propensity score. The results with respect to recall@𝑘 are in
Table 8. We found that the overall findings remain robust.
recall@𝑘
Model 𝑘 = 20 𝑘 = 40 𝑘 = 60 𝑘 = 80
BPRMF-V𝜇 = 0.1 19.41 31.47 36.40 40.50
BPRMF-V𝜇 = 0.5 18.02 31.18 36.76 40.69
BPRMF-V𝜇 = 1.0 18.56 31.08 36.72 40.53
BPRMF-F𝜇 = 0.1 18.73 30.10 35.28 39.32
BPRMF-F𝜇 = 0.5 19.48 32.11 37.92 42.16
BPRMF-F𝜇 = 1.0 18.52 31.74 37.04 41.14
Table 8: Performance comparison of BPRMF with varying
degrees of𝜇.
E COMPARISON OF THE PAST LATENT
VULNERABILITY TO NORMAL AND HATE
SPEECH
To see whether PLV to hate speech is different from PLV to normal
content, we apply the above recommendation model to users who
share normal content. We then compare the PLV embeddings of
hate speech and normal content by visualizing the differences with
t-SNE [48]. In addition, we cluster the hate speech and normal con-
tent embeddings using DBSCAN [12] and compute the silhouette
score. The silhouette score ranges from−1 to+1 and measures the
separability of clusters.
Overall, we observed the following. In the t-SNE plot, we show
that PLV embeddings of normal content are mostly concentrated
in one broad cluster whereas the embeddings of hate speech are
separated into multiple, clearly defined clusters (see Figure 9). We
also find slightly higher silhouette scores for hate speech than
normal content (0.609 and 0.539, respectively) when keeping the
DBSCAN parameters constant (eps = 0.5 and minimum samples
= 10). This suggests that PLV to hate speech is more homogenous

Conference’17, July 2017, Washington, DC, USA Dominique Geissler, Abdurahman Maarouf, and Stefan Feuerriegel
within clusters and heterogenous across clusters, whereas PLV to
normal content cannot be clustered into clearly distinct groups as
well. This is in line with previous research which states that hate
speech spreaders are more similar to each other [4, 13] and interact
in highly connected networks [24, 25].
60
 40
 20
 0 20 40 60 80
80
60
40
20
0
20
40
60
80
(a) Past latent vulnerability
to hate speech (Silhouette
score = 0.609)
(b) Past latent vulnerability
to normal content (Silhouette
score = 0.539)
Table 9: Comparison of the past latent vulnerability for
(a) hate speech and (b) normal speech using a 2D 𝑡-SNE plot
[48].
