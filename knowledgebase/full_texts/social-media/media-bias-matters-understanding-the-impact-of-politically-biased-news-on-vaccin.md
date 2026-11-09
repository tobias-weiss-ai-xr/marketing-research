---
title: 'Media Bias Matters: Understanding the Impact of Politically Biased News on Vaccine Attitudes in
  Social Media'
url: https://arxiv.org/abs/2403.04009
category: social-media
subcategory: empirical
date: 2024-03
venue: ''
authors:
- Bohan Jiang
- Lu Cheng
- Zhen Tan
- Ruocheng Guo
- Huan Liu
source: arxiv
pdf_url: https://arxiv.org/pdf/2403.04009
pages: 9
chars: 45214
fetched_at: '2026-11-08T13:04:26+00:00'
kb_version: 1
---

# Media Bias Matters: Understanding the Impact of Politically Biased News on Vaccine Attitudes in Social Media

Media Bias Matters: Understanding the Impact of Politically Biased News
on Vaccine Attitudes in Social Media
Bohan Jiang1 , Lu Cheng2 , Zhen Tan1 , Ruocheng Guo3 and Huan Liu1
1School of Computing and AI, Arizona State University
2Department of Computer Science, University of Illinois Chicago
3ByteDance Research
{bjiang14, ztan36, huanliu}@asu.edu, lucheng@uic.edu, ruocheng.guo@bytedance.com
Abstract
News media has been utilized as a political tool to
stray from facts, presenting biased claims without
evidence. Amid the COVID-19 pandemic, polit-
ically biased news (PBN) has significantly under-
mined public trust in vaccines, despite strong medi-
cal evidence supporting their efficacy. In this paper,
we analyze: ( i) how inherent vaccine stances sub-
tly influence individuals’ selection of news sources
and participation in social media discussions; and
(ii) the impact of exposure to PBN on users’ atti-
tudes toward vaccines. In doing so, we first curate a
comprehensive dataset that connects PBN with re-
lated social media discourse. Utilizing advanced
deep learning and causal inference techniques, we
reveal distinct user behaviors between social me-
dia groups with various vaccine stances. Moreover,
we observe that individuals with moderate stances,
particularly the vaccine-hesitant majority, are more
vulnerable to the influence of PBN compared to
those with extreme views. Our findings provide
critical insights to foster this line of research.
1 Introduction
The pervasive impact of the COVID-19 pandemic transcends
geographic and social boundaries [Haleem et al., 2020], hav-
ing claimed over 7 million lives globally as of February
20241. Although vaccination emerges as the most effica-
cious defense, a substantial proportion of the population has
shown vaccine hesitancy [Dror et al. , 2020 ]. A KFF sur-
vey [Kirzinger et al. , 2021 ] reported that more than 40%
of parents in the U.S. are hesitant to get their children vac-
cinated due to safety and efficacy concerns. Meanwhile,
hundreds of mainstream media are responsible for publish-
ing COVID-related politically biased news (PBN), turning
the vaccine campaign into a political campaign [Bolsen and
Palm, 2022]. While the skepticism around vaccines isn’t new,
when intertwined with news media, it exacerbates polarized
opinions and conspiracy theories, thereby posing substantial
challenges to public health efforts [Sorell and Butler, 2022].
1https://covid19.who.int/
Figure 1: An overview of our research pipeline. On the left, it de-
picts news outlets disseminating COVID-related PBN to wide audi-
ences via social media platforms. The right side illustrates the poten-
tial influence of such PBN exposure on users’ vaccine stances. We
define exposure as instances where a user engages with PBN through
Retweets or Quote-tweets (Retweets with added comments). Dis-
cussion refers to user involvement in vaccine-related conversations
after PBN exposure. Change denotes the variation in users’ vaccine
stances resulting from PBN exposure.
Recent research has examined the impact of news cov-
erage [Le Qu ´er´e et al. , 2022 ], political polarization [Ebel-
ing et al. , 2022 ], and misinformation dissemination in so-
cial media [Miyazaki et al. , 2023 ]. However, few efforts
have been focused on: (i) providing a comprehensive dataset
that connects news media data with associated social me-
dia data; and ( ii) understanding the causal relationship be-
tween exposure to PBN and people’s vaccine stance changes.
Most existing works [Joseph et al., 2022; Poddar et al., 2022;
Spiteri, 2021 ] studied their correlation instead of causa-
tion, the latter of which is the key to understanding the im-
pact of a PBN intervention (i.e., reading a COVID-vaccine-
related PBN) on the outcome (i.e., COVID-19 vaccine stance
changes). While [Fowler et al., 2022] examined the causal re-
lationship via surveys, it is limited to a small sample size and
overlooks potential confounders such as user heterogeneity
and social media features related to treatment and outcome.
Modeling confounders is challenging due to the scarcity of
arXiv:2403.04009v1  [cs.SI]  6 Mar 2024

observational data and domain knowledge. Moreover, little
existing work differentiates the causal effect of groups with
various vaccine stances. Large-scale studies on social media
can complement prior research in the field to better under-
stand how PBN shapes people’s stances toward vaccines.
To address aforementioned limitations and challenges, we
construct CovNS (Covid-19 biased News and Social me-
dia dataset), the first dataset which bridges the gap between
COVID-related PBN and the corresponding social media dis-
cussions. Utilizing CovNS, we propose a research pipeline
(see Figure 1) to study the following research questions:
• RQ1: How do PBN consumption and social media discus-
sion vary with different vaccine stance groups?
• RQ2: To what extent does PBN exposure contribute to the
reversal and reinforcement of vaccine stances?
In summary, this study makes the following contributions
to systematically address the posed research questions:
• Dataset Curation: We build CovNS, the first dataset that
establishes a connection between the COVID-related PBN
and the social media data, enabling future research by pro-
viding sufficient annotations.
• Behavior Analysis: We characterize pro-vaccine, anti-
vaccine, and vaccine-hesitant groups on Twitter. We delve
into the differences in PBN consumption preference and
social media discussions across these groups.
• Causal Effect Estimation: We employ advanced causal
learning methods to estimate the causal effect of reading
PBN on users’ vaccine stance changes.
Our observations reveal that the three vaccine stance
groups demonstrate significantly different user behaviors.
Meanwhile, exposure to left-leaning and right-leaning news
sources generally causes social media users to be more pro-
vaccine and anti-vaccine, respectively. Notably, users who
are hesitant about vaccination show a greater vulnerability to
the influence of PBN, underscoring the significant challenges
faced in promoting vaccination campaigns.
2 Related Work
In this section, we review three existing bodies of literature
that lay the foundation for this work: (i) long-standing litera-
ture on the political bias in news media in the United States;
(ii) fast-rising literature on the COVID-19 vaccine stance;
and (iii) well-established work on applying causal inference
methods on COVID-related problems.
2.1 Political Bias in News Media
Political bias in news media has been studied extensively in
the areas of political science, social science, etc [Eberl et al.,
2017]. It is an inherent bias of journalists and media out-
lets that makes them intentionally report biased news articles
in order to serve a political agenda. The alteration of the
news content usually operates in two ways: (i) issue framing,
i.e., presenting an issue in a way that will likely get the most
agreement from supporters; and (ii) issue filtering, i.e., selec-
tively omit information that supports an alternative opinion on
the other political side [Iyengar, 1994]. As a result, readers
were manipulated by misleading or false viewpoints and nar-
ratives. Prior work examining political bias using both qual-
itative and quantitative methods, has shown that U.S. news
media differs ideologically and can create a highly polarized
social environment [Budak et al., 2016]. During the COVID-
19 pandemic, much scholarly attention has been devoted to
understanding the influence of PBN on public health. For ex-
ample, some have shown that misleading information down-
plays the severity of COVID [Teng et al., 2022], false claims
prevent people from knowing the fact [Seo et al., 2022], and
conspiracy communities use PBN to distance users from sci-
ence [Sharma et al., 2022].
2.2 COVID-19 Vaccine Stance
Various studies have investigated the COVID-19 vaccine
stance in social media. Among them, some works contributed
to providing labeled datasets regarding COVID-19 vaccine
stance [Mu et al. , 2023; Glandt et al. , 2021 ] These works
use either manual or algorithmic annotations to label a post
as anti-vaccine, pro-vaccine, or vaccine-hesitant. There exist
other works that focus on building machine learning mod-
els to predict the COVID-19 vaccine stance, using linguistic
features [Poddar et al., 2022], auxiliary information [Tahir et
al., 2022], or large language models [Riaz et al., 2022]. Be-
sides, another line of research has been devoted to collecting
COVID-vaccine-related datasets from news media. [Semer-
aro et al., 2022] collected 5,745 news from 17 Italian news
media. [Joseph et al., 2022] collected 750k articles from over
300 local news outlets to analyze relations between news cov-
erage and offline behaviors.
However, little prior work provided labeled datasets of
COVID-vaccine-related PBN and social media discussion. To
bridge this gap, our dataset combines both social media (e.g.,
tweets) and news media (e.g., news articles) data with multi-
level manual and algorithmic annotations on news articles,
posts, and users.
2.3 Causal Analysis of COVID-Related Factors
Well-established literature is built around learning causality
with machine learning and big data [Guo et al., 2020]. Much
of the recent work examined the causal relationships among
COVID-related factors. For instance, [Hsiang et al., 2020 ]
and [Ma et al. , 2022 ] estimated the causal effect of differ-
ent government efforts (e.g., COVID-19 policies) on offline
statistics (e.g., number of infections and deaths). Other stud-
ies investigated the causal impact of online COVID-19 misin-
formation on one’s mental health [Verma et al., 2022] or vac-
cine hesitancy [Pierri et al., 2022]. [Fowler et al., 2022] con-
ducted a survey to study the effect of exposure to politicized
media coverage on people’s negative emotional responses.
However, there is little understanding of the impact of con-
suming COVID-related PBN on social media users’ willing-
ness toward the COVID-19 vaccine uptake. As a remedy, we
work on this problem by exploiting advanced causal machine-
learning methods on the collected real-world dataset and pro-
posed causal graphs.

Figure 2: An example of the data collection process. We first collect
a set of COVID-related news triplets containing articles from left-
leaning, center-leaning, and right-leaning outlets fromAllsides (top).
We then obtain associated Twitter data (bottom).
Fields Stats Labels
Twitter Tweets 243,412,961 VS User metadata (e.g., id) 36,172 VS
Allsides
Stories (news triples) 732 VS
News articles 2,196 VS, PL
News metadata (e.g., url) 2,196 -
News Media 160 PL
Table 1: Overview of CovNS. Note that VS = vaccine stance; PL =
political leaning.
3 Bridging News Media and Social Media
In this section, we introduce how we build the dataset, includ-
ing detailed data collection, annotation, and selection process.
Figure 2 exemplifies the data collection process. We rely on
two resources: Allsides2 and Twitter, to collect PBN and so-
cial media data, respectively. We obtain human-annotated la-
bels such as political leaning fromAllsides. We then annotate
the vaccine stances for the collected data using manual and
algorithmic labeling strategies. At last, we apply filters to
compose a high-quality dataset for our experiment. Table 1
provides an overview of CovNS.
3.1 Data Collection
PBN from Allsides. We gather COVID-related PBN from
Allsides, a website that assesses the political bias of promi-
nent media outlets, and presents different versions of similar
news stories from sources of the political right, left, and cen-
ter. It shows readers news coverage and diverse perspectives
from all across the American political spectrum. In addition,
it also provides a neutral summary to recapitulate the story
and discuss how different news outlets spin or manipulate the
facts. Note that Allsides currently only focuses on English
2https://www.allsides.com/unbiased-balanced-news
news from American media outlets.
For each news story, we collect the triplets of
PBN {NL, NC, NR} denoting news articles from left-
leaning, center-leaning, and right-leaning news media,
respectively. They are associated with correspond-
ing titles {TL, TC, TR}, contents {CL, CC, CR}, and
URLs {UL, UC, UR}. We also collect meta-information
such as publication date, topics, media name, and URLs of
banners or pictures for each news article. In total, there are
732 COVID-related news triplets (i.e., 2,196 news articles)
from 160 U.S. media outlets.
Social Media Data from Twitter . We construct a large-
scale Twitter dataset using the official academic research API.
Following previous work on collecting news articles in so-
cial media [Shu et al. , 2020 ], we use the URL of original
PBN as the search query on Twitter to collect all the avail-
able social media discourses such as tweets, retweets, and
replies. Moreover, we collect historical tweets and profile in-
formation from users who have participated in the discussion
about COVID-related PBN. Overall, this dataset consists of
243,412,961 historical tweets from 36,172 unique accounts.
3.2 Data Annotation
Two sets of labels are essential to analyze the relationship be-
tween PBN consumption and vaccine stance changes of social
media users: political leaning and vaccine stance.
We adopt labels on political leaning ( left, lean-left, cen-
ter, lean-right, or right) from Allsides. For each news arti-
cle, the rating process includes ( i) editorial review, (ii) blind
bias survey, (iii) independent review, (iv) third-party review,
(v) community feedback, and ( vi) confidence level. 3 How-
ever, both data sources (Allsides and Twitter) do not provide
human-annotated labels on COVID-19 vaccine stances. As it
is a time-consuming and labor-intensive task to annotate vac-
cine stances for the entire collected dataset with 2,196 news
articles and 243,412,961 tweets, we follow the method men-
tioned in [Lyu et al., 2022] and leverage a human-in-the-loop
machine-learning strategy to minimize the manual annotation
effort meanwhile maintaining high-quality labels.
Specifically, we first identify common COVID-related key-
words ( covid, coronavirus, and SARS-CoV-2) to filter out
news articles and tweets unrelated to COVID-19. After that,
we invite two annotators in the area to inspect the headline
and content to assign one of the four labels for each news
article:
• Pro-vaccine, i.e., news that promotes the willingness of
vaccine acceptance and uptake;
• Anti-vaccine, i.e., news that discourages the willingness of
vaccine acceptance and uptake;
• Mixed, i.e., news that contains controversial opinions about
COVID-19 vaccines; and
• Other, i.e., news that contains general COVID-19 informa-
tion, but are unrelated to vaccines.
3https://www.allsides.com/media-bias/
media-bias-rating-methods

Before annotating, we inform the annotators of a few exam-
ples of each category. With the collected annotations, we cal-
culate Cohen’s Kappa Score (k) to assess the inter-annotator
agreement for the selected PBN dataset. We get k = 0.83,
which is considered “almost perfect” agreement according
to [Cohen, 1960 ]. To further obtain the ground truth, we
only considered the annotations that both annotators agreed
on. This results in 410 pro-vaccine, 395 anti-vaccine, 409
mixed, and 772 other news articles.
For our large-scale Twitter dataset, we finetune a pre-
trained CT-BERT [M¨uller et al. , 2020 ] on three publicly
available Twitter datasets for COVID-19 vaccine stance de-
tection [Glandt et al., 2021; Cotfas et al., 2021; Jiang et al.,
2023]. The final downstream task is designed to be a bi-
nary classification, i.e., infer the stance of COVID-vaccine-
related tweets as pro-vaccine (+1) or anti-vaccine (-1). Our
final model achieves a high F1 score and accuracy, yield-
ing respectively 0.833 and 0.845. To further evaluate our
dataset’s final model, we adopt a set of COVID-vaccine-
stance-related keywords fromCoVaxxy[DeVernaet al., 2021]
to extract relevant tweets. Then we manually check the
machine-generated stance labels. Specifically, we randomly
select 500 COVID-vaccine-related tweets (250 pro-vaccine
and 250 anti-vaccine) from our dataset and manually anno-
tate them. Algorithmic and manual annotations have a “al-
most perfect” agreement with Cohen’s Kappa Scorek = 0.84.
This suggests that the final model is capable and reliable in la-
beling the rest COVID-vaccine-related tweets in our dataset.
3.3 Data Selection
To compose a high-quality dataset for the experiment, we
apply filters to obtain a set of COVID-vaccine-related PBN
with extreme political bias and relatively high social media
engagement from 2021/06 to 2022/06. Particularly, we ex-
clude PBN that is ( i) unrelated to COVID-19 vaccines; ( ii)
from lean-left and lean-right news media; and (iii) with fewer
than 100 related social engagements (retweets and replies).
As bot accounts are active on Twitter, we apply Botome-
ter [Yang et al. , 2022 ] to filter out malicious bots in our
dataset. After that, we apply additional filters to exclude users
(i) whose locations are outside the United States; and (ii) who
do not have at least one COVID-vaccine-related tweet before
and after consuming COVID-vaccine-related PBN in seven
days. After doing so, the subset contains 250 news triplets
and 89,535,833 tweets from 17,643 unique users.
4 RQ1. Behavior Analysis of Three Vaccine
Stance Groups
People with different vaccine stances can have different news
consumption behaviors, e.g., pro-vaxxers read more news
from the left-leaning media. How they react to a PBN read-
ing intervention may also differ significantly. Therefore, it
is critical to identify groups with different vaccine stances to
mitigate potential selection and sampling bias. In this sec-
tion, we ( i) categorize users into anti-vaccine, pro-vaccine,
and vaccine-hesitant groups and then (ii) compare their PBN
consumption behaviors and social media discussions.
Figure 3: Ratio of left-, right-, and center-leaning news media of
pro-vaccine, anti-vaccine, and vaccine-hesitant groups.
Vaccine Stance Groups. Based on a study from the SAGE
working group [MacDonald and others, 2015 ], vaccine hes-
itancy occurs on the continuum between two extremes, i.e.,
completely accepting (pro-vaccine) and refusing all vaccines
(anti-vaccine). Intuitively, vaccine-hesitant users change their
stances more frequently compared to anti-vaxxers and pro-
vaxxers. Therefore, we first calculate the monthly COVID-
vaccine stance changes:
stance = Pbefore − Abefore
Pbefore + Abefore
. (1)
Note that Pbefore and Abefore denote the number of pro-vaccine
and anti-vaccine tweets before a user reads PBN, respectively.
Similar to [Mitra et al., 2016], we then determine three types
of vaccine stance groups based on the following criteria:
• pro-vaccine group, users whose monthly COVID-19 vac-
cine stance are always greater than 0.8;
• anti-vaccine group, users whose monthly COVID-19 vac-
cine stance are always less than -0.8; and
• vaccine-hesitant group, users whose monthly COVID-19
vaccine stance are changing between 0.8 and -0.8.
In total, we identify 2,377 pro-vaccine, 1,238 anti-vaccine,
and 10,428 vaccine-hesitant users.
News Consumption Behavior . Next, we compare the se-
lection bias of three types of news sources in the pro-vaccine
group, anti-vaccine group, and vaccine-hesitant group in Fig-
ure 3. A notable observation is that the pro-vaccine and anti-
vaccine groups display a highly unbalanced distributioncom-
pared to the vaccine-hesitant group. Left-leaning and right-
leaning news dominate among the pro-vaccine (around 75%)
and anti-vaccine groups (around 91%), respectively. Mean-
while, users in the vaccine-hesitant group read news mainly
from center-leaning (around 43%) and left-leaning (around
35%) media outlets.
Sociel Media Discussion. We further use topic modeling
on the collected COVID-vaccine-related tweets to investi-
gate topics each group is interested in after reading PBN.
The text is pre-processed by punctuation removal, URL
removal, stop words removal, hashtag removal, tokeniza-
tion, stemming, and lemmatization. The cleaned data is
then fed into BERTopic [Grootendorst, 2022], a state-of-the-
art topic modeling technique that leverages Sentence-Bert
(SBERT) [Reimers and Gurevych, 2019] for text embedding,
UMAP [McInnes et al., 2018] for dimensionality reduction,
HDBSCAN [McInnes et al., 2017] for clustering, and a class-
based TF-IDF for topic representation. To verify the quality

(a) Overall percentage.
(b) Monthly percentage.
Figure 4: Overall (a) and monthly (b) percentage of Twitter discus-
sions associated with five COVID-vaccine-related topics among the
pro-vaccine group, anti-vaccine group, and vaccine-hesitant group.
of the result from BERTopic, we manually inspect represen-
tative tweets (i.e., tweets nearest to the cluster centroid) for
each topic cluster. Finally, we merge over-partitioned clus-
ters to obtain the final list of COVID-related topic clusters.
In Table 2, we identify five major COVID-vaccine-
related topics: “vaccine refusal”, “vaccine acceptance”,
“conspiracy theory”, “scientific fact”, and “political narra-
tive”. We illustrate a large variation in the results across these
topics in Figure 4a:
• The pro-vaccine group prefers discussions about “vaccine
acceptance” (46.5%) and “scientific argument” (23.3%).
• The anti-vaccine group tends to post “conspiracy theories”
(42.4%) and “vaccine refusal” (35.6%).
• The vaccine-hesitant group tends to discuss “scientific ar-
guments” (36.0%) and “politics” (28.8%).
Figure 4b shows how the discussion changes over time in
each stance group. We find that:
• “Vaccine acceptance” (green) and “scientific argument”
(blue) discussions have grown steadily in the pro-vaccine
and vaccine-hesitant groups.
• Percentages of tweets about “conspiracy theories” (purple)
and “vaccine refusal” (red) show a rapid increase between
2022/04 and 2022/05 in the anti-vaccine group.
• The trending around “political discussion” (grey) of the
three groups shows a similar pattern.
5 RQ2. Estimating Causal Effect of Reading
PBN on Stance Change
One of the primary challenges in causal effect estimation with
observational data is controlling for confounders. In this re-
search question, we (i) identify two types of social media fea-
tures as potential confounders : users’ statistical profile fea-
ture (e.g., number of tweets) and textual content feature (e.g.,
historical tweets) [Veitch et al., 2020; Cheng et al., 2022a].
With the identified potential confounders, we ( i) estimate
the causal effect of reading COVID-vaccine-related PBN on
Twitter users’ vaccine stance changes. We hypothesize that
reading COVID-vaccine-related news from left-leaning and
right-leaning media will cause people’s COVID-19 vaccine
stance to shift toward pro-vaccine and anti-vaccine, respec-
tively. To validate this hypothesis, we begin by formulat-
ing the problem as a causal effect estimation task. We use
causal graphs [Pearl, 2009] to represent the two scenarios we
consider – (1) when the causal effect is confounded only by
observed variables (see Figure 5a); and (2) when there exist
unobserved confounders (see Figure 5b). With them, we ap-
ply state-of-the-art causal learning methods to quantitatively
estimate the causal effect using data from CovNS. We also
compare the results obtained by the causal learning models
and that from a correlation-based model.
Potential Confounders. We consider the following profile
features as potential confounders:
• The log-transformed number of historical tweets,
likes, followers, and friends;
• The 2020 U.S. presidential election results of the
location, (0 =blue state, 1 =red state);
• The age (months) of the account;
• The Twitter account is verified or not, (0 =unverified,
1 =verified); and
• The proportion of COVID-vaccine-related tweets, i.e.,
a continuum between 0 and 1.
For the textual feature, we extract the text embedding of the
most recent one-week historical tweets before a user
reads PBN from the fine-tuned CT-BERT. These statistical
and textual features can reflect user characteristics, which are
related to users’ online behaviors. Therefore, we select these
important social media features as potential confounders for
discovering the causal relation in the next phase.
Modeling Causal Relations. We define the causal ef-
fect we aim to estimate – reading COVID-vaccine-related
PBN ( treatment) denoted by T on one’s COVID-vaccine
stance shifting ( outcome) denoted by Y . We represent the
causal relations among variables with two different causal
graphs [Pearl, 2009] to consider two possible scenarios (see
Figure 5). We consider four different settings in terms of how
the values of T and Y are defined (see Table 3). Then, with
do-calculus [Pearl, 2009], we define the causal estimand, i.e.,
the average treatment effect (ATE):
AT E= E[Y |do(T = 1)]− E[Y |do(T = 0)], (2)
where E[Y |do(T = t)] is the expectation of Y when T is in-
tervened to take value t. As aforementioned, we consider the
user characteristics, i.e., a set of selected profile features and
user history, are related to one’s PBN consumption behavior
(T ) and change in COVID-19 vaccine stance (Y ).
In scenario 1, we let the confounder W be these user char-
acteristics. Thus, by conditioning on them, we can block
the backdoor path (treatment-confounder-outcome) to handle
confounding bias. With Figure 5a, we assume that there is no

Topic Top Words Representative Tweets
Vaccine
Refusal
die, kill, serious, allergic, side,
effect, risk, freedom
I won’t EVER comply. #NOmasks #NOVaccine. I will deal only in cash,
and will only do business with like-minded patriots ...
Vaccine
Acceptance
boost, cdc, fight, child, protect,
strong, together, immunity
I am thankful to be fully vaccinated, as earlier this month I recovered from
COVID, having had only mild symptoms. I encourage everyone ...
Conspiracy
Theory
fauci, bill, gates, chip, track, lie,
kill, bio, weapon, lab, leak
BILL GATES: NOT a doctor. NOT a Scientist. IS a College Dropout. IS a
Eugenicist. KNOWN FOR making a computer system susceptible ...
Scientific
Argument
cell, mrna, evidence, study,
immunity, doctor, symptom
According to a study published in Lancet, a single dose of Pfizer or As-
traZeneca Covid vaccine offers around 60% protection against ...
Political
Narrative
trump, biden, plan, fund, mayor,
congress, campaign
The PA legislature has 7 billion from Biden’s American Rescue Plan to help
PA and they’re doing anything else. Political theater on COVID. Not ...
Table 2: Five topic clusters along with top words (highest TF-IDF scores) and representative tweets (closest to cluster centroids).
backdoor path between T and Y by conditioning on the ob-
served user characteristics W . This leads to the identification
of ATE through backdoor criterion [Pearl, 2009]:
P (Y |do(T )) =
Z
P (Y |T, W)P (W )dW. (3)
In this scenario, we estimate ATE with two state-of-the-
art causal learning methods. Double machine learning
(DML) [Chernozhukov et al., 2018] – DML estimates hetero-
geneous treatment effects from observational data with ma-
chine learning algorithms. It contains two predictive tasks
(i.e., predict the treatment and outcome from the confounder)
to ensure unbiased estimates of the causal effect. We use
a linear DML in this study. Causal Forest (CF) [Athey et
al., 2019 ] – CF is widely adopted for causal effect estima-
tion, which performs recursive partition in the confounder
space s.t. each leaf of a tree in CF corresponds to a homo-
geneous subpopulation with similar causal effect. Compared
to linear DML, CF models the relationship between the con-
founder and the treatment with a tree-based model and infers
the causal effect of a test instance by looking up the treatment
effect of the subpopulation this instance is mapped to.
Scenario 1 relies on a strong causal assumption that all con-
founders are observable/measurable (i.e., the unconfounded-
ness assumption [Pearl, 2009]). However, in practice, some
confounders are hidden or unmeasurable. For example, one’s
education and occupation may not be explicitly stated in the
user profile. We cannot hope to measure all possible con-
founders. A common practice is to adopt the “proxy vari-
ables” [Cheng et al., 2022b]. For example, some textual clues
from historical tweets can implicitly reflect users’ education
levels and jobs. Therefore, in scenario 2, we further relax
the unconfoundedness assumption and consider the observed
user characteristics X as the proxies of the latent confounder
W . The causal graph is illustrated in Figure 5b. Then we
can leverage proximal causal inference methods [Miao et al.,
2018] to identify ATE. Specifically, we consider Causal ef-
fect variational autoencoder (CEVAE) [Louizos et al., 2017]
as the estimator. CEV AE leverages deep variational autoen-
coders (V AE) to learn the representation of the latent con-
founder given the observed proxy variables.
For comparison, we include a correlation-based method.
Specifically, we implement a simple logistic regression on
treatment that predicts the outcome Y with the treatment T
as its input. It can be considered as a generalized version of
the naive estimator [Rubin, 1978 ] that does not control the
effect of confounding variables.
(a)
 (b)
Figure 5: Two causal DAG of our studied problem. The left one (a)
assumes all confounding variables are observed. The right one (b)
uses proxies to approximate latent confounders.
Setting Treatment (T) Outcome (Y)
1 0: read center news 0: unchanged stance 1: read left news 1: move toward pro-vax
2 0: read center news 0: unchanged stance 1: read left news 1: move toward anti-vax
3 0: read center news 0: unchanged stance 1: read right news 1: move toward pro-vax
4 0: read center news 0: unchanged stance 1: read right news 1: move toward anti-vax
Table 3: Experiment settings for the causal study.
Estimating Causal Effects. Figure 6 shows the compari-
son of the overall estimated ATE by different methods and
that of the pro-vaccine group (6b), anti-vaccine group (6c),
and vaccine-hesitant group (6d). The estimated ATE from
DML, CF, and CEV AE are similar (p >0.05).
• Comparing the results from settings 1 and 2, we observe
that reading PBN from left-leaning media causes individ-
uals to be more pro-vaccine . In contrast, results from set-
tings 3 and 4 show that consuming PBN from right-leaning
media causes people to be more anti-vaccine.
• Results from logistic regression (LR) on treatment are out-
liers in all experiments ( p < 0.001). For example, the es-
timated ATEs of LR in setting 3 show that reading right-
leaning PBN will make people more pro-vaccine, which is
opposite to the results from causal learning models. A pos-
sible explanation is that the results of correlation-based ob-
servational studies usually suffer from spurious correlation
due to confounding bias, especially when the confounding
effect is important [Austin, 2011].
• In addition, we find that the magnitudes of the es-
timated ATE of the vaccine-hesitant group are higher

(a) Overall.
 (b) Pro-vaccine group.
(c) Anti-vaccine group.
 (d) Vaccine-hesitant group.
Figure 6: The overall estimated ATE and that of each (pre-treatment) stance group: we compare correlation-based (red) and causal learning
models (green) in 4 experimental settings. We ran each model 10 times to report the mean values (histograms) and standard deviations (error
bars). Note that the ATE inferred by the causal learning methods are similar ( p >0.05 for t-test) while they are significantly different from
the one estimated by the correlation-based model (p <0.001 for t-test).
than the pro-vaccine group and anti-vaccine group, in-
dicating that vaccine-hesitant people are more likely to
change their vaccine stances after consuming PBN.
6 Implications
RQ1. Users with varying stances on vaccines display unique
patterns of PBN consumption and social media discussion.
Future research should consider the disparity when studying
vaccine-related problems in social media.
• Compared to the vaccine-hesitant people, the pro-vaccine
and anti-vaccine group members are more likely to read
PBN from far-left and far-right news media, respectively.
Intensive exposure to highly biased news may explain the
occurrence of extreme COVID-19 vaccine stances.
• As “scientific arguments” and “political narratives” usu-
ally contain debatable opinions, the vaccine-hesitant group
member is able to gather diverse information from both
sides. Thus, their stances may move back and forth.
• The pattern of increasing interest in “vaccine acceptance”
and a decline in “vaccine refusal” indicates that the vaccine-
hesitant group is becoming more positiveabout the vaccine.
RQ2. The exposure to COVID-vaccine-related news from
left- and right-leaning media causes one’s COVID-19 vaccine
stance shift toward pro- and anti-vaccine respectively, espe-
cially for users in the vaccine-hesitant group. This suggests
that it is possible for malicious people to manipulate public
opinion through PBN interventions.
• The similar estimated causal effects from causal learning
models indicate that the unobserved confounding variables
may have limited impacts on the treatment and outcome.
• Comparing the magnitudes of the estimated ATE (see Fig-
ure 6a), we observe that left-leaning news (setting 1 and 2)
is more influential than right-leaning news (setting 3 and 4).
We speculate that vaccine-hesitant people are more likely
to become pro-vaxxers than anti-vaxxers over time through
the influence of PBN.
• As reading left-leaning news has a very small causal ef-
fect (around 0.1) on anti-vaxxers’ vaccine stance changes
(see Figure 6c), it is unlikely to alter anti-vaxxers to pro-
vaxxers through PBN reading interventions. Meanwhile,
pro-vaxxers are difficult to become anti-vaxxers by con-
suming PBN (see Figure 6b). This indicates that people
with extreme views about vaccines tend to reinforce their
existing stances. On the other hand, the vaccine-hesitant
majority are vulnerable to the influence of PBN and, thus,
may frequently reverse their minds.
7 Conclusions
This paper investigates the impact of PBN consumption on
the vaccine stance changes of social media users. We con-
struct CovNS, which contains data from both news media
and social media. We compare the PBN consumption be-
havior and social media discussion between three vaccine
stance groups. By identifying potential confounders, we
leverage state-of-the-art causal inference methods to estimate
the causal effect. Our experiments and analyses have im-
plications for fostering the research of vaccine hesitancy in
social media. We conclude that consuming left-leaning and
right-leaning news causes people to be pro-vaccine and anti-
vaccine, respectively. More importantly, there is only a small
possibility for anti-vaxxers to become pro-vaxxers via PBN
reading interventions on social media, and vice versa.

References
[Athey et al., 2019] Susan Athey, Julie Tibshirani, and Ste-
fan Wager. Generalized random forests. The Annals of
Statistics, 47(2):1148–1178, 2019.
[Austin, 2011] Peter C Austin. An introduction to propensity
score methods for reducing the effects of confounding in
observational studies. Multivariate behavioral research ,
46(3):399–424, 2011.
[Bolsen and Palm, 2022] Toby Bolsen and Risa Palm. Politi-
cization and covid-19 vaccine resistance in the us.PMBTS,
2022.
[Budak et al., 2016] Ceren Budak, Sharad Goel, and
Justin M Rao. Fair and balanced? quantifying media bias
through crowdsourced content analysis. Public Opinion
Quarterly, 80(S1):250–271, 2016.
[Cheng et al., 2022a] Lu Cheng, Ruocheng Guo, Kasim
Candan, and Huan Liu. Effects of multi-aspect online re-
views with unobserved confounders: Estimation and im-
plication. In ICWSM, 2022.
[Cheng et al., 2022b] Lu Cheng, Ruocheng Guo, and Huan
Liu. Estimating causal effects of multi-aspect online re-
views with multi-modal proxies. In WSDM, 2022.
[Chernozhukov et al., 2018] Victor Chernozhukov, Denis
Chetverikov, Mert Demirer, Esther Duflo, Christian
Hansen, Whitney Newey, and James Robins. Double/debi-
ased machine learning for treatment and structural param-
eters. The Econometrics Journal, 2018.
[Cohen, 1960] Jacob Cohen. A coefficient of agreement for
nominal scales. Educational and psychological measure-
ment, 20(1):37–46, 1960.
[Cotfas et al., 2021] Liviu-Adrian Cotfas, Camelia Delcea,
Ioan Roxin, Corina Ioan˘as ¸, Dana Simona Gherai, and Fed-
erico Tajariol. The longest month: analyzing covid-19
vaccination opinions dynamics from tweets in the month
following the first vaccine announcement. IEEE Access,
9:33203–33223, 2021.
[DeVerna et al., 2021] Matthew R DeVerna, Francesco
Pierri, Bao Tran Truong, John Bollenbacher, David Axel-
rod, Niklas Loynes, Christopher Torres-Lugo, Kai-Cheng
Yang, Filippo Menczer, and John Bryden. Covaxxy:
A collection of english-language twitter posts about
covid-19 vaccines. In ICWSM, 2021.
[Dror et al., 2020] Amiel A Dror, Netanel Eisenbach, Shahar
Taiber, Nicole G Morozov, Matti Mizrachi, Asaf Zigron,
Samer Srouji, and Eyal Sela. Vaccine hesitancy: the next
challenge in the fight against covid-19. European journal
of epidemiology, 35(8):775–779, 2020.
[Ebeling et al., 2022] R´egis Ebeling, Carlos Abel C ´ordova
S´aenz, J´eferson Campos Nobre, and Karin Becker. Anal-
ysis of the influence of political polarization in the vacci-
nation stance: the brazilian covid-19 scenario. In ICWSM,
2022.
[Eberl et al., 2017] Jakob-Moritz Eberl, Hajo G Boomgaar-
den, and Markus Wagner. One bias fits all? three types of
media bias and their effects on party preferences.Commu-
nication Research, 44(8):1125–1148, 2017.
[Fowler et al., 2022] Erika Franklin Fowler, Rebekah H Na-
gler, Darshana Banka, and Sarah E Gollust. Effects of
politicized media coverage: Experimental evidence from
the hpv vaccine and covid-19. PMBTS, 2022.
[Glandt et al., 2021] Kyle Glandt, Sarthak Khanal, Yingjie
Li, Doina Caragea, and Cornelia Caragea. Stance detec-
tion in covid-19 tweets. In ACL-IJCNLP, 2021.
[Grootendorst, 2022] Maarten Grootendorst. Bertopic: Neu-
ral topic modeling with a class-based tf-idf procedure.
arXiv preprint arXiv:2203.05794, 2022.
[Guo et al., 2020] Ruocheng Guo, Lu Cheng, Jundong Li,
P Richard Hahn, and Huan Liu. A survey of learning
causality with data: Problems and methods. ACM Com-
puting Surveys (CSUR), 53(4):1–37, 2020.
[Haleem et al., 2020] Abid Haleem, Mohd Javaid, and Raju
Vaishya. Effects of covid-19 pandemic in daily life. Cur-
rent medicine research and practice, 2020.
[Hsiang et al., 2020] Solomon Hsiang, Daniel Allen,
S´ebastien Annan-Phan, Kendon Bell, Ian Bolliger,
Trinetta Chong, Hannah Druckenmiller, Luna Yue Huang,
Andrew Hultgren, Emma Krasovich, et al. The effect
of large-scale anti-contagion policies on the covid-19
pandemic. Nature, 584(7820):262–267, 2020.
[Iyengar, 1994] Shanto Iyengar. Is anyone responsible?:
How television frames political issues . University of
Chicago Press, 1994.
[Jiang et al., 2023] Bohan Jiang, Paras Sheth, Baoxin Li, and
Huan Liu. Covaxnet: An online-offline repository for
covid-19 vaccine hesitancy. In ICWSM workshop, 2023.
[Joseph et al., 2022] Kenneth Joseph, Benjamin D Horne,
Jon Green, and John P Wihbey. Local news online and
covid in the us: Relationships among coverage, cases,
deaths, and audience. In ICWSM, 2022.
[Kirzinger et al., 2021] Ashley Kirzinger, Grace Sparks, Liz
Hamel, Lunna Lopes, Audrey Kearney, Mellisha Stokes,
and Mollyann Brodie. Kff covid-19 vaccine monitor: July
2021. Kaiser Family Foundation, 2021.
[Le Qu´er´e et al., 2022] Marianne Aubin Le Qu´er´e, Ting-Wei
Chiang, and Mor Naaman. Understanding local news so-
cial coverage and engagement at scale during the covid-19
pandemic. In ICWSM, 2022.
[Louizos et al., 2017] Christos Louizos, Uri Shalit, Joris M
Mooij, David Sontag, Richard Zemel, and Max Welling.
Causal effect inference with deep latent-variable models.
NeurIPS, 2017.
[Lyu et al., 2022] Hanjia Lyu, Junda Wang, Wei Wu, Viet
Duong, Xiyang Zhang, Timothy D Dye, and Jiebo Luo.
Social media study of public opinions on potential covid-
19 vaccines: informing dissent, disparities, and dissemina-
tion. Intelligent medicine, 2(01):1–12, 2022.
[Ma et al., 2022] Jing Ma, Yushun Dong, Zheng Huang,
Daniel Mietchen, and Jundong Li. Assessing the causal

impact of covid-19 related policies on outbreak dynamics:
A case study in the us. In WWW, 2022.
[MacDonald and others, 2015] Noni E MacDonald et al.
Vaccine hesitancy: Definition, scope and determinants.
Vaccine, 33(34):4161–4164, 2015.
[McInnes et al., 2017] Leland McInnes, John Healy, and
Steve Astels. hdbscan: Hierarchical density based clus-
tering. J. Open Source Softw., 2(11):205, 2017.
[McInnes et al., 2018] Leland McInnes, John Healy, and
James Melville. Umap: Uniform manifold approximation
and projection for dimension reduction. arXiv preprint
arXiv:1802.03426, 2018.
[Miao et al., 2018] Wang Miao, Zhi Geng, and Eric J Tch-
etgen Tchetgen. Identifying causal effects with proxy
variables of an unmeasured confounder. Biometrika,
105(4):987–993, 2018.
[Mitra et al., 2016] Tanushree Mitra, Scott Counts, and
James Pennebaker. Understanding anti-vaccination atti-
tudes in social media. In ICWSM, 2016.
[Miyazaki et al., 2023] Kunihiro Miyazaki, Takayuki
Uchiba, Kenji Tanaka, Jisun An, Haewoon Kwak, and
Kazutoshi Sasahara. ” this is fake news”: Characterizing
the spontaneous debunking from twitter users to covid-19
false information. In ICWSM, 2023.
[Mu et al., 2023] Yida Mu, Mali Jin, Charlie Grimshaw,
Carolina Scarton, Kalina Bontcheva, and Xingyi Song.
Vaxxhesitancy: A dataset for studying hesitancy towards
covid-19 vaccination on twitter. In ICWSM, 2023.
[M¨uller et al., 2020] Martin M ¨uller, Marcel Salath ´e, and
Per E Kummervold. Covid-twitter-bert: A natural lan-
guage processing model to analyse covid-19 content on
twitter. arXiv preprint arXiv:2005.07503, 2020.
[Pearl, 2009] Judea Pearl. Causality. Cambridge university
press, 2009.
[Pierri et al., 2022] Francesco Pierri, Brea L Perry,
Matthew R DeVerna, Kai-Cheng Yang, Alessandro
Flammini, Filippo Menczer, and John Bryden. Online
misinformation is linked to early covid-19 vaccination
hesitancy and refusal. Scientific reports, 12(1):1–7, 2022.
[Poddar et al., 2022] Soham Poddar, Mainack Mondal, Ja-
nardan Misra, Niloy Ganguly, and Saptarshi Ghosh. Winds
of change: Impact of covid-19 on vaccine-related opinions
of twitter users. In ICWSM, 2022.
[Reimers and Gurevych, 2019] Nils Reimers and Iryna
Gurevych. Sentence-bert: Sentence embeddings using
siamese bert-networks. In EMNLP, 2019.
[Riaz et al., 2022] Muhammad Talha Riaz, Muham-
mad Shah Jahan, Sajid Gul Khawaja, Arslan Shaukat, and
Jahan Zeb. Tm-bert: A twitter modified bert for sentiment
analysis on covid-19 vaccination tweets. In ICoDT2.
IEEE, 2022.
[Rubin, 1978] Donald B Rubin. Bayesian inference for
causal effects: The role of randomization. The Annals of
statistics, pages 34–58, 1978.
[Semeraro et al., 2022] Alfonso Semeraro, Salvatore Vilella,
Giancarlo Ruffo, and Massimo Stella. Writing about
covid-19 vaccines: Emotional profiling unravels how
mainstream and alternative press framed astrazeneca,
pfizer and vaccination campaigns. arXiv preprint
arXiv:2201.07538, 2022.
[Seo et al., 2022] Haeseung Seo, Aiping Xiong, Sian Lee,
and Dongwon Lee. If you have a reliable source, say some-
thing: Effects of correction comments on covid-19 misin-
formation. In ICWSM, 2022.
[Sharma et al., 2022] Karishma Sharma, Yizhou Zhang, and
Yan Liu. Covid-19 vaccine misinformation campaigns and
social media narratives. In ICWSM, 2022.
[Shu et al., 2020] Kai Shu, Deepak Mahudeswaran, Suhang
Wang, Dongwon Lee, and Huan Liu. Fakenewsnet: A
data repository with news content, social context, and spa-
tiotemporal information for studying fake news on social
media. Big data, 8(3):171–188, 2020.
[Sorell and Butler, 2022] Tom Sorell and Jethro Butler. The
politics of covid vaccine hesitancy and opposition. The
Political Quarterly, 93(2):347–351, 2022.
[Spiteri, 2021] Jonathan Spiteri. Media bias exposure and
the incidence of covid-19 in the usa. BMJ global health,
6(9):e006798, 2021.
[Tahir et al., 2022] Anique Tahir, Lu Cheng, Paras Sheth,
and Huan Liu. Improving vaccine stance detection by
combining online and offline data. SBP-BRiMS, 2022.
[Teng et al., 2022] Xian Teng, Yu-Ru Lin, Wen-Ting Chung,
Ang Li, and Adriana Kovashka. Characterizing user
susceptibility to covid-19 misinformation on twitter. In
ICWSM, 2022.
[Veitch et al., 2020] Victor Veitch, Dhanya Sridhar, and
David Blei. Adapting text embeddings for causal infer-
ence. In UAI, 2020.
[Verma et al., 2022] Gaurav Verma, Ankur Bhardwaj, Ta-
layeh Aledavood, Munmun De Choudhury, and Srijan Ku-
mar. Examining the impact of sharing covid-19 misin-
formation online on mental health. Scientific Reports ,
12(1):1–9, 2022.
[Yang et al., 2022] Kai-Cheng Yang, Emilio Ferrara, and
Filippo Menczer. Botometer 101: Social bot practicum for
computational social scientists. Journal of Computational
Social Science, 2022.
