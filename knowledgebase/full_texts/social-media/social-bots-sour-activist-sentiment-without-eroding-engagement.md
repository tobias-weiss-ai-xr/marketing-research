---
title: Social bots sour activist sentiment without eroding engagement
url: https://arxiv.org/abs/2403.12904
category: social-media
subcategory: empirical
date: 2024-03
venue: ''
authors:
- Linda Li
- Orsolya Vasarhelyi
- Balazs Vedres
source: arxiv
pdf_url: https://arxiv.org/pdf/2403.12904
pages: 46
chars: 123248
fetched_at: '2026-11-08T13:11:55+00:00'
kb_version: 1
---

# Social bots sour activist sentiment without eroding engagement

Social bots sour activist sentiment without
eroding engagement
Linda Lia, Orsolya V´as´arhelyib,c,d, and Bal´azs Vedrese,a,b
aOxford Internet Institute, University of Oxford, Oxford, UK
bCenter for Collective Learning, Corvinus Institute for Advanced Studies, Corvinus
University, Budapest, Hungary
cInstitute of Data Analytics and Information Systems, Corvinus University, Budapest,
Hungary
dCEU Democracy Institute, Budapest, Hungary
eDepartment of Network and Data Science, Central European University, Vienna, Austria
Corresponding author:
Bal´azs Vedrese,a,b
Email address: vedresb@ceu.edu
ABSTRACT
Social media platforms have witnessed a substantial increase in social bot activity, significantly affecting
online discourse. Our study explores the dynamic nature of bot engagement related to Extinction Rebellion
climate change protests from 18 November 2019 to 10 December 2019. We find that bots exert a greater
influence on human behavior than vice versa during heated online periods. To assess the causal impact of
human-bot communication, we compared communication histories between human users who directly
interacted with bots and matched human users who did not. Our findings demonstrate a consistent negative
impact of bot interactions on subsequent human sentiment, with exposed users displaying significantly
more negative sentiment than their counterparts. Furthermore, the nature of bot interaction influences
human tweeting activity and the sentiment towards protests. Political astroturfing bots increase activity,
whereas other bots decrease it. Sentiment changes towards protests depend on the user’s original support
level, indicating targeted manipulation. However, bot interactions do not change activists’ engagement
towards protests. Despite the seemingly minor impact of individual bot encounters, the cumulative effect
is profound due to the large volume of bot communication. Our findings underscore the importance of
unrestricted access to social media data for studying the prevalence and influence of social bots, as with
new technological advancements distinguishing between bots and humans becomes nearly impossible.
Keywords: social bots; human-bot interaction; information cascades; political communication; protests
1 INTRODUCTION
Social media has become the primary channel to learn about and spread news, engage in political discus-
sions, and participate in collective actions over the past decade [1, 2, 3]. Automated agents, or so-called
”social bots,” are increasingly active in our social and political publics online [ 4], creating content and
interacting with humans [5]. The resulting hybrid ecosystem where algorithmic agents and humans co-
exist can fundamentally alter the nature of democracy, political accountability, transparency, and civic
participation [6]. Automated accounts can propagate a large volume of messages at minimal expense, and
engage with users promptly and excessively, far exceeding human capacities [7]. As a consequence, the
algorithmic share of social media content is now on par with human participation: Automated users were
estimated to be responsible for generating 10% to 40% of tweets in recent political events, such as the 2016
US presidential election, the Brexit referendum, the yellow vests movement, the Catalan referendum, or
the 2019 United Nations Climate Change Conference [8, 9, 10].
Recent studies have found that social bots – especially those designed to mimic human behavior –,
disrupt online political discussions [11], and there is overwhelming evidence that they significantly influence
political debates and activism[11, 12, 13]. Such bots are frequently designed to pass as human accounts,
and occasionally explicitly mimic known political figures and government accounts to gain the attention
and trust of human users [14]. Bots are often highly active during the flare-up of discussions around new
political events [15], and disseminate targeted messages ranging from fabricated news to contentious,
divisive, and negative content[16, 17, 18], blending legitimate messages and misinformation. Furthermore,
arXiv:2403.12904v1  [cs.CY]  19 Mar 2024

bots are also often deployed in orchestrated efforts to generate the facade of a seemingly vibrant discussion
conforming with hidden agendas [19, 20] by retweeting each other (known as ”astroturfing”), targeting
susceptible users[8].
Research on bot-human interaction found that bots can often hijack the collective attention of human
users [10, 16], can increase the visibility of extreme views [8, 16, 21], influence communication sentiment
[22], and can even alter human communication networks [23, 24]. Although social bot presence has been
studied before at the macro scale, less is known about the micro-level impact of human-bot encounters on
subsequent human activism. Small-scale simulations and experiments indicate that bots can alter expressed
human values [24] and behaviors [25], particularly driving users towards more extreme viewpoints [26]
and potentially silencing them [27]. However, there is little empirical evidence regarding the capacity of
bots to modify human behavior in real-life political communication[17, 19, 23, 28].
Today, online activism constitutes an essential part of democracy, but most of the existing research
focuses on institutionalized political processes such as elections [ 22, 29, 30, 21], while few studies
examined the role of bots within activism related to online protests [10, 23, 31]. Furthermore, these studies
have often collapsed acts of communication, analyzing them in aggregate. The dynamics of social media
use in online activism differs markedly from communication around other political events [32, 33], and is
also a critical component of online political discourse [34, 35]. Since social bots are designed to be more
responsive than humans [36], it is common to observe an increase in bot activity during the peak of heated
online debates, followed by a decrease in their presence[8]. Although the bursty nature of social media
communication of protests is known [37, 38], the impact of social bots on human activity during and after
bursty periods has not been investigated.
How does interacting with social bots impact human behavior in online activism? We address this
question with data on Twitter discourse on climate-change-related social movements. We analyze the
dynamics of bots and humans engaging with each other, and we also compare the difference in impact of
bot encounters to activists who did not engage with bots. Our analysis focuses on protest-related discourse
during a series of protest events that erupted from November to December 2019. We decided to concentrate
on online activism related to climate change as our case study, as algorithmic threats to engagement in
climate change activism can have profound consequences on societal agreement on the public good in a
critical issue [39]. We analyze communication around the Extinction Rebellion (XR), as the highest profile
activist group online.
The topic of climate change has been shown to attract highly engaged, active, and committed partic-
ipants [40], while there is also substantial bot activity [ 41, 42]. This enables us to analyze the impact
of human-bot interactions on humans during information cascades [ 19], and measure the effect of bot
encounters on tweeting activity[27] and sentiment [26]. Our findings contribute to the growing body of
research on machine behaviour[6], particularly in terms of understanding how rapidly developing hybrid
human-machine systems could potentially modify human opinion over an extended period.
Early work related to human-bot interactions on social media found that user sociability and network
size predict who will be interacted with by a bot [ 43, 15]. Our results show that bots have become so
widespread that it is unlikely that an active user of X will not interact with a bot online. Our research
extends previous work by focusing on quantifying the impact of direct human-bot communication. We
found that bot type matters for the impact on users’ tweeting activity, and the initial level of support a
user has toward the climate change movement determines how a bot encounter impacts their sentiment on
climate change. Our results have important policy implications for increasing platform transparency in
how they handle automated profiles.
RESULTS
Proportions of bot and human communication
We found 48% of all accounts to fall into the bot category within our sample from Twitter ( 44,121 of
the total 93,499 users). We identified automation through a combined approach [44, 45] that integrates
the results of commonly used bot identification methods, Botometer[ 46] and our self-trained machine
learning-based algorithms. Botometer is a widely adopted open source tool to identify bots on Twitter
[47]. Our self-trained models used various data sets tailored to identify users with automated behavior
that attempts to mimic humans on social networks, especially in the context of political behavior [ 46].
Bots reported in the main text are the combined results of these two models, with a fixed threshold for
the Botometer (CAP >= 0.65). Since the concept of ”bot” encompasses varying degrees of automation,
using one fixed bot classification threshold is always a simplification. Therefore, we repeated all analyzes
reported in the main text at various bot thresholds, and we report these results in the SI.(See Materials &
Methods, Bot Identification and SI Bot Identification for more details).
2/46

23% 35%
26%
16%
Human
52%
Bot
48%
Figure 1. Information flow of humans and bots. The directions and amount of tweets retweeted between
bots and humans.
81% of tweets were replies or retweets in our database, and 51% of these retweets originated from
bots. In general, bot activity is mainly the posting of original messages or the retweeting of each other
(35% of all retweets and 71% of bot retweets were retweeting other bots), and only a small portion of bot
retweets were retweets originating from humans (29%). At the same time, humans spread roughly the
same number of messages produced by bots (54%) and humans (46% ). If the bot threshold is increased
to CAP >= 0.75, still 48% of the retweets originate from bots, and 45% of the human retweets originate
from bots (see SI Information cascades and SI Tables S5 to S7 for information flows).
Temporal co-dependence of bot and human tweeting
We found that the quantity, intensity, direction and the sentiment of the information flow between humans
and bots are highly topic-dependent. We identified seven topics related to XR protests associated with news
events, political campaigns, or outbursts of sentiments (for example, climate change denial) by applying
bi-term topic models [ 48]. (See Materials & Methods, Topic Modeling for more details and SI Table
S4 for a brief summary of the topics, including their content, top hashtags, and sample tweets). Out of
these seven topics, four were highly bursty: Topic-related activity increased sharply periodically and then
decreased suddenly[49], resulting in information cascades. Information cascades occur when users follow
the behavior of other individuals on social networks (e.g. retweeting the same message) [50]. (See Table
S8 in Supplementary Information on Burstiness Scores).
Figure 2 shows the temporal distribution of human and bot tweets at a 5-minute interval within an
illustrative bursty period of climate change discussions on Twitter. Although human users (red line)
generated a higher volume of tweets during the cascade’s peak, the tweeting frequency trend is jointly
influenced by both bots and humans. Table 1 shows the results of Granger Causality tests, which examine
whether one time series could be used to predict another after introducing a time lag [ 51]. Our results
indicate that in all identified cascades, the number of bot tweets during bursty periods could be used to
predict human activity. Also, in 3 cases, the number of tweets by humans could be used to predict bots’
activities, suggesting that the effect was mutually driven, indicting that bots and humans drove the cascade
together. The effect was stronger on bots’ side in two of those three mutually-driven cascades, and in 3 out
of 4 cascades humans retweeted bots much more than bots retweeted humans. Furthermore, in 3 out of
4 cascades, the sentiment of bot tweets could be used to predict human sentiment after introducing a 30-
or 35-minute time lag. The effect was mutual only for ’Anti XR protests’, but the effect was stronger on
bots’ side. This suggests that bots not only capture human attention, but also have an immediate impact
on the sentiment of humans exposed to them. The effect remains consistent across bot CAP thresholds
ranging from 0.50 to 0.75 for 3 of the identified 4 cascades. (See more details on Burstiness in Materials
& Methods, Identifying cascades, SI Cascades, SI Table S8-S10 for Granger Causality Results across
different CAP thresholds and for Topic Burstiness Scores).
Predicting the impact of direct bot interactions
To test whether bot encounters have any influence on human users - beyond their above shown immediate
collective effect in bursty periods - we developed two models focusing on 1) Amount and 2) Sentiment.
Specifically, we analyzed how human communication evolves over a span of 30 days after the first
interactions with a bot in the discussion related to climate change on Twitter. The first model captures the
inclination to ”speak out” quantified by the average number of tweets posted related to the XR protest.
The second model predicts the change in sentiment about the climate change protest (measured on a scale
ranging from −1 to 1, with −1 representing the most negative sentiment and 1 the most extreme sentiment).
3/46

0
20
40Number of tweets
Granger Causual Inference
F = 2.77**Bots Humans
F = 2.54**Humans Bots
A
Humans
Bots
00:0018:00 20:00 22:00 02:00 04:00
Time (hours EST, Nov. 30., 2019)
0
20
40
60
80
100Percentage of tweets
68%
46%
B
Humans
Bots
Figure 2. Panel A: Number of tweets posted by bots (blue line) and humans (red line) in a cascade
mutually-driven by bots and humans within the ”Anti-XR protests” topic. Panel B: Ratio of bot and human
generated tweets throughout the time period of the cascade. The number of tweets is the rolling average
aggregated on 5-minute intervals.
Topic Bots→Humans Humans →Bots Amount Sentiment Amount Sentiment
”Football game
protests” 2.27 * 0.38 3.97 *** 0.92
”Disruptive
engagement” 15.60 *** 2.17 * 2.68 ** 1.91
”Anti-XR
protests” 2.77 ** 3.96 *** 2.54 ** 3.08 **
”Politicized
activism” 6.06 *** 11.40 *** 1.50 2.24
Table 1. Granger causality test results between bot and human communication amount and sentiment. *:
p < 0.05, **: p < 0.01, ***:p < 0.001. Granger causality tests whether bot activities can predict human
activities (bot-human) or human activities can predict bot activities (human-bot) in all four identified
cascades. These tests were performed on the first-order differences for both the number of tweets
(aggregated in 5-minute intervals) and the average sentiment (calculated over 5-minute intervals). The time
lags used in the tests were set at 30 or 35 minutes.
4/46

Botencounter
Matched
Bot impacted
−30 −20 −10 0 10 20 30
Days
−1.0−.5 .0 .5 1.0
Sentiment
Figure 3. Two examples of Twitter timelines. Top timeline shows daily tweet counts and daily mean
sentiment for a human account that directly interacted with a bot on day 0; bottom timeline shows a
matched account without a direct bot interaction. Bar heights are proportional to tweet counts, color
indicates sentiment from −1 to 1.
To quantify the impact of bot interaction on human communication change, we used a three-step
process. This includes: 1) we sampled N = 303 users who directly interacted with bot accounts (bot-
exposed) - replied or commented to a tweet/comment originated from a bot; 2) we collected a matched
sample of N = 184 users, who were active in the XR related protest discussion on Twitter but had no direct
interaction with bots. Matching users were selected on the basis of the similarity score calculated pairwise
to our original sample considering publicly available metrics on human users’ profiles. (See Materials and
Methods, Matching Sample for more details.) 3) Figure 3 shows two example timelines, one human user
who directly interacted with a bot (the interaction is shown at time 0), and a matched user that did not
encounter a bot.
3) Finally, we applied Difference-in-Difference (DiD) [52] regression models to quantify the casual
effect of meeting a bot on outcomes by comparing a set of humans who directly interacted with bots
(human replying or commenting bot tweets) with those who did not. Our observation units are the daily
activity of human users relative to the time of interaction with bots - 30 days before and 30 days after. This
setting allows us to quantify the prolonged impact of bot interaction on the frequency of tweeting and
sentiment of tweets compared to users who did not meet a bot.
Botometer provides prediction values for belonging to seven subbot categories ranging from 0 to 5.
We classify a bot into a subcategory if its bot-specific probability is greater than 2.5. Our biggest group is
’miscellaneous other bots’ which are bots that are similar to various type of manually annotated bots (23%),
followed by manually labeled political bots, so-called ’astroturfs’ (14%),’fake followers’ bots purchased to
increase follower counts (7%), ’self declared’ bots from botwiki.org (5%), ’spammers’ (2%) and ’financial
bots’ (0.4%). Although ’miscellaneous other bots’ are quite well represented within the XR discourse
online, only 17% of human users had direct interaction with them. As implied by the topic of our analysis,
the individuals in our sample primarily engaged with ’astrotufs’ (38%). These automated accounts are
specifically designed to participate in political discussions [2], leading us to analyze users interacting with
astroturfs separately from those who interacted with non-astroturfs.
Figure 4. visualizes the predicted daily change in the average number of daily tweet counts (Panel A),
and the sentiment of the tweets (Panel B) grouped by different bot probabilities (65,70,75) and subbot
category (astroturf or other type of bots). We found that encounters with astroturf bots result in an increase
in the number of tweets, while encounters with other kind of bots result in a decrease in the number of
tweets. This suggests that the most politically relevant bot category - astroturf bots - drive the conversation
by provoking engagement from human users, while other kinds of bots have a rather negative, silencing
effect. Regardless of the bot type, direct interaction with a bot decreases the average sentiment of human
users. (See Table S12-S17 for DID models)
Astroturfs tend to be mobilized in a targeted way against users with a specific opinion[15, 53]. Therefore,
we classified bot-exposed and matched human users by their support of XR Protests: Supporters (Pro -
52%), Neutral (27%), and Anti-XR (Con - 21%) using ChatGPT. (See Materials and Methods on Support
Categorization). Figure 4, panel C-D indicates that human users who support or have a neutral opinion
about XR are significantly affected by interacting with bots, while anti-XR users are not affected. Bot
interaction has the strongest negative impact on the sentiment of bot-exposed users with neutral opinion,
indicating that bots might target those users whose opinion can be changed [15, 54]. The change in the
number of tweets was significantly increased by bot interaction for XR supporters within the least selective
bot probability category (65), although the trends are similar in the more selective categories (.70,.75). In
5/46

.50 .00 .50
65
70
75Bot Probability
other
astroturf
A
.20 .15 .10 .05 .00 .05
B
1.00 .50 .00 .50
Predicted Amount Change
65
70
75Bot Probability
pro
con
neutral
C
.40 .30 .20 .10 .00 .10
Predicted Sentiment Change
D
Figure 4. Predicted change resulting from a bot interaction. Panel A, C: Predicted change in Amount
(number of tweets). Panel B,D: Predicted change in Sentiment. Panel A-B separate predictions (by color)
are shown for astroturf bots (light blue), and other bots (dark blue), while Panel C-D separate predictions
by users support level towards XR - supporters (green), neutral users (blue), anti-XR (purple)
6/46

these models, we control for the astroturf score of the interacted bot, which has a strong positive significant
relationship with the change in amount. Our results indicate that the type of bot matters more for the
activity change than the original support towards protests. However, the level of sentiment change depends
on the original support level of users exposed to bots. (See SI Table S18-S23 for DID models)
We also investigated if users affected by bots alter their levels of support as a result of bot interaction.
There were no significant differences between the distribution of bot-exposed users’ support level before,
and after interacting with a bot (Mann-Whitney U=45536.00, p=0.86).There was no significant difference
either between users exposed to bots and those matched in terms of the change in support level.(See Model
Tables 23-24 in SI on Opinion Change). Out of the users who interacted with bots, only 9% experienced a
shift towards neutrality, while 10% of the opinions of the users in the matched group became more neutral
towards XR protests. Additionally, 7% of the users exposed to bots and 6% of the matched users changed
their opinion completely, shifting from negative to positive or the other way around.
LIMITATIONS
There are two potential limitations to our current research design. The first is the relatively short time range
and sample size of our dataset on XR protests. Our dataset covers several waves of XR protests within a
month, but XR is a global phenomenon that has been going on for several years. However, comparing our
sample size to previous studies on online activism and political communications on Twitter[34, 32], we
believe that it is a valid and representative case to illustrate the studied aspects of bot activities on online
activism. The Twitter academic product track API (available at the time of data collection) provided the
full archive of tweets based on specific search queries; therefore, our dataset is a comprehensive sample of
the online record of bot and human activities during the protest period.
The second limitation concerns our binary bot detection method. It has three main drawbacks, each
of which we address through additional efforts and measures. First, similar to other bot identification
approaches [46, 55, 10, 56], and due to the nature of unsupervised learning, our method cannot be a 100%
sure whether a user classified as a bot is genuinely a bot. Second, the concept of ”bot” encompasses varying
degrees of automation among Twitter users, and using a fixed bot classification threshold overlooks these
nuances. We are aware that being a bot, similar to the concept of gender [57], is not a binary classification
problem. Many human users apply automation to increase their efficiency [58], which does not turn them
into bots, but they are no longer non-automated human users. Third, a fixed threshold-based approach can
still lead to false positives and false negatives, potentially undermining the validity of our causal inferences
regarding bot activities. To address those concerns, we ran our models with varied CAP scores. We also
performed a series of robustness checks involving various thresholds for all of our analysis and reported
them in the main text. (See Discussions, SI Information flow, Cascades, and Difference-in-Difference
regression results).
DISCUSSION
Bot presence is considerable and possibly increasing in the public sphere. Even with stricter thresholds, bot
activity is higher in our sample than in previous related work published on the 2017 Catalan referendum by
Stella et al. [16], where only 19% of all interactions were from bots to humans. It was shown that tweets
from conservative bots are more retweeted by humans, which can indicate that this difference is not only
due to the continuously increasing presence of bots [59], but could be due to the highly politicized and
international nature of our context.
We have adopted a dynamic approach to political communication, and we have found that bots should
not be thought of a constant presence, but rather bots react in a dynamic fashion, and are driving the amount
and sentiment of heated and bursty discussions. By our analysis of Granger causality, bots impact human
behavior more, than the other way around.
To quantify the causal impact of human-bot communication, we have compared the communication
histories of human users who have directly interacted with a bot with those matched human users who have
not. This allowed us to see a consistently negative impact of any kind of bot interaction on the sentiment of
subsequent human communications: Humans who have interacted with a bot displayed considerably more
negative sentiment than matched users.
The change in tweeting activity after a bot interaction depends on the nature of the bot: On one hand,
decidedly political astroturfing bots (aiming to influence public opinion behind an impression of grassroots
opinion) result in an increased activity. On the other hand, interacting with other kinds of bots (spammers,
fake followers) results in a decrease in activity. However, change in sentiment towards the protests depends
on the original support level of the user, supporting, neutral, or against XR. Our results indicate that bots
might target users whose opinions are easier to change, since the sentiment of bot-exposed users with
7/46

neutral opinion decreased the most. However, bots do not make human users switch their support level.
In sum, bot interaction is not without impact, even if one encounter itself has only a small effect (it takes
about two bot encoutners to induce one additional tweet). Nevertheless, since there is an exceeding amount
of bot communication, these small impacts add up to influence the public sphere in a profound way.
Although our analysis covers a period of time prior to the launch of ChatGPT (2022.11.30), it is be-
coming increasingly difficult to identify bots due to the rapid advancement mimicking human behavior[60].
As large language models are becoming widespread and easily accessible through APIs, new social bots
can act extremely human, making it currently almost impossible to distinguish between bots and humans,
even for experts [61, 62].
Therefore, it is crucial to have unrestricted access to social media data to assess the influence and
prevalence of these new types of social bots, although recent trends show that social media platforms
are less willing to share free data for research purposes [ 63, 64]. Since financial evaluations are highly
correlated with the size of the (human) user base [65], platforms have no interest in quantifying the ratio of
non-human accounts and their impact on misinformation [15]. Most users still underestimate the effect
of bots on themselves, but as they are exposed to increased bot presence, they tend to prefer stricter
bot-regulation policies [66]. That is why we welcome the news that the European Union requires larger
platforms to provide researchers with access to data to study systemic risks arising from the use of their
services, such as disinformation [67]. Such legislative actions can help the scientific community continue
its work to understand the consequences of this abrupt change in technology that will alter the nature of
human-bot interactions [61, 68, 69, 70].
DATA AND METHODS
Data
Our data is made up of Twitter activity around several waves of Extinction Rebellion climate change
protests from 18 November 2019 to 10 December 2019. The dataset was collected from November to
December 2022 via the Academic Research product track API provided by Twitter[71], which enabled
users to collect a full archive sample of historical tweets filtered based on keywords and conditions. We
collected all tweets posted during this period of time that contained the keyword ’Extinction Rebellion’,
’climate change protest’, ’XRebellion’, ’XR’ and multiple variants of keywords with slightly different
spelling. (The complete list of keywords used can be found in SI Table S1) In total, the final data set
contained 201,010 tweets and 122,130 users.
Bot Identification
To identify social bots on Twitter, we used a combination of two sets of bot identification methods. The
first is a popular Twitter bot identification tool known as the ’botometer’ (formerly BotorNot), which
was primarly used as a benchmark to compare other methods. The second is a set of our self-trained bot
identification model trained with open source data of bots and humans to train supervised machine learning
models.
Botometer is a publicly available tool that relies on machine learning. It is designed to calculate a
score where low scores indicate likely human accounts, while high scores suggest likely bot accounts [72].
The algorithm considers more than 1,000 features related to user profiles, friends, network structure, and
activity patterns, among others. Another part of our bot identification pipeline comes from self-trained
models. Training sets were derived from existing open-source data from Twitter accounts identified as
’bots’ and ’humans’.
We trained bot identification models with 70% training and 30% of testing set with five types of
algorithms: random forest(RF), support vector machine(SVM), logistic regression(LOG), XGboost classi-
fication (XGB) and deep learning (DL). We developed two versions of our mdoels with ten and twenty
features that were proved to be most effective for bot identification by previous studies [ 73, 10]. The
evaluation of the models demonstrated that the RF, DL, and XGB models with 20 traits surpassed other
models in terms of sensitivity (true positive rate), balanced precision, precision, and F1 score. Additionally,
these models exhibited strong performance in an independent test carried out on a dataset consisting of
influential bots and human mimics that were active during the 2018 midterm election of the United States.
In our final bot identification approach, we combined the results derived from both sets of bot identifi-
cation methods. Due to the potential false positive issues inherent in both methods, they yielded somewhat
divergent results [47]. To reconcile this disparity, we classified users based on the overlapping results of
botometer and our proprietary algorithms (DL, RF, or XGB). If both the botometer and at least one of
our algorithms identified a user as a bot, the user was classified as such; conversely, the same principle
was applied to the classification of humans. To account for the potential error in bot identification, we
8/46

performed all our analyzes with a varying baseline CAP score ranging between 0.60 − 0.75 (See more
details in Supplementary Information, Bot Identification).
Topic Modeling
We first identified the themes emerging in the protest-related discourse with the increasingly popular
bi-term topic models [48, 74] that learn topics by modeling word-word co-occurrence patterns [75]. After
removing all retweets, to preprocess the data we used the nltk python package [76] to remove stopwords,
usernames, emojis and links from the tweets, and lemmtize and stemm every word.
We then trained bi-term topic models on our preprocessed data with the bitermplus package[77]. We
set up a biterm topic model of all the tweets related to XR, which classified all tweets into 8 different
topics. Based on the u mass coherence scores [78], we determined that 8 topics fits our dataset the best.
After evaluating the meaning of topics we dropped one topic whose keywords and content were too diverse
to extract a meaningful media agenda from it. (See more details in Supplementary Information, Topic
Modeling).
Granger Causality
We tested whether bots attracted people’s attention to given topics, through ’granger causality’ tests.
Granger causality is a time-series-based method that tests whether one time series sequence could be used
to predict another. If A is proved to be effective in predicting B, then A is called to granger cause B [79].
We created an aggregated time series of five minutes of the number of posts by bots and humans, then
introduced a time lag (6 time lags, or 5*6 = 30 minutes) between the number of tweets by bots and by
humans. The augmented Dickey-Fuller (ADF) test and the Kwiatkowski-Phillips-Schmidt-Shin (KPSS)
tests suggested that all time series we tested were non-stationary (e.g., the mean or variant was not constant
or there were seasonal fluctuations in the time series trend), which can impact the accuracy of estimation.
Therefore, we used the first-order difference for all Granger causality tests. If the number of posts by bots
granger cause that of humans, then we would infer that bots were directing humans’ attention, and vice
versa. If no granger casuality was observed on both sides, or if the effect was mutual, following existing
research practice[79, 80, 81], we conclude that bots and humans were driving the cascade together. The
formula for the test is as follows, in which X1 and X2 are items in time-series vectors:
X1(t) =∑p j=1 A11, jX1(t − j) +∑p j=1 A12, jX2(t − j) +E1(t)
X2(t) =∑p j=1 A21, jX1(t − j) +∑p j=1 A22, jX2(t − j) +E2(t)
In the model, p stands for the time gap between the two vectors for prediction, A is the coefficient or
how much lagged observation can contribute to the prediction of the model, and ε as residuals. X1 is said
to granger cause X2 if the inclusion of X1 reduces the variance of the residuals. (See SI Cascades, Table 1
for detailed information of the granger causality results on all identified cascades).
Sentiment Analysis
For sentiment analysis, the V ADER package was used, which is an open source rule-based model and has
been proven particularly effective for the classification of feelings in text from social media [82]. We used
the raw text of tweets for sentiment analysis, as suggested by the package documentation. For each tweet,
the algorithm assigns a sentiment score from −1 to +1, with −1 being the most negative, +1 the most
positive, and 0 neutral. (See SI Figure S6 and S7 for the distribution of sentiment of all tweets by exposed
and matched users.)
Matched Sample
In order to understand how bots shape in the longer term (30 days after bot interaction) human tweeting
activity and tweet sentiment related to XR, we created a sample of matched human users who did not
interact with bots in our dataset to compare with ’bot-exposed’ human users. We first identified a group
of 506 users in our dataset as our exposed sample, the ones who directly interacted with bots by quoting
or replying to bots. Then we calculated a similarity metric between all the ’non-exposed’ human users
and exposed users. Specifically, we calculated Eucledian distance based on the following metrics: statuses
count, followers count, friends count, favorites count, listed count, followers growth (average number of
followers increased on a daily basis), friends growth, favorites growth, listed growth, follower friend ratio.
These traits were selected and/or calculated based on the user profile collected via Twitter API V1.2. The
formula for the Euclidian distance is as follows, in which pn and qn means the Nth trait for the sample and
the matching:
9/46

d(p,q) =
q
(p1 − q1)2 + (p2 − q2)2 + ... + (pn − qn)2
It is worth mentioning that not all exposed users have matched users, and not all matched users were
active during the time window in discussions related to XR. This is because the distribution of activity
levels in online political communication is right skewed [32]; half of the users posted less than five times
about XR in our data set. After dropping non-active potentially matched users, in total we had184 matched
users for 303 exposed users. If a user has more than one matched users, we include up to the top five
matched users in our dataset.
Identifying cascades
Cascades were identified by calculating the temporal density (the percentage of tweets that belong to a
given topic in a given time period) of each topic. Based on previous studies on the life cycle of information
cascades online [83, 84], the time window was specified as 1 hour. To identify cascades, we identified
bursty periods by calculating the Z scores of the average topic density per hour for each topic. Then filtered
out all time units that had a Z score larger than 2 (> 95% percentile) in any two or more consecutively two
one hour time windows. Because the z score and the topic density could be high in time windows with
only a few tweets, we also dropped those topics with no more than 50 tweets in at least one hourly time
window. (See SI cascades for detailed information on all identified cascades.)
Support group categorization using ChatGPT
For our research objectives, we also categorize users’ opinions regarding the protests they engage in
discussions about. To achieve this, we seek to determine whether users are in favor of or against the
protests they discuss. This is measured using a scoring system ranging from -1 to 1, where -1 indicates
complete opposition to the protest, 1 denotes strong support for the protest, and 0 signifies a neutral stance
or unrelated discussion in their tweets. Subsequently, we employ a tri-category classification scheme for
further analysis: scores between -1 and -0.1 are classified as ”Anti-XR (Con protest)”, those from 0.1 to 1
as ”Supporters (Pro protest),” and scores between -0.1 and 0.1 as ”Neutral.”
The data used for this classification consists of users’ tweets from our dataset. We evaluate the opinion
expressed in all interactions (human replies to bots) between our sample users and bots. Additionally, for
each bot-exposed user and their matched counterparts, we classify their opinions based on all tweets from
their timeline before bot interaction.
We employed OpenAI’s large language model (LLM), ChatGPT 3.5 [85], to classify users’ standpoints.
This method has been raised and adopted in various studies [86, 87]. For each user, we provide the model
with an instruction prompt on how to classify their opinion toward climate change protests in general,
along with the text to classify (users’ tweets), and the model outputs the aforementioned score. To generate
the three opinion scores mentioned above, we used the full timeline for each user before bot interaction
(for opinion before), the full timeline after bot interaction (for opinion after), and human replies to bots’
tweets during bot interaction (for opinion during interaction). (See SI Support group categorization for
detailed information on prompt engineering and verification.)
Difference-in-Difference Models
We apply difference-in-differences (DiD) analysis to assess the effects of the two-way treatment on human
users who directly engaged with bots. DiD is a statistical model design that incorporates both a treatment
and a control group. In this approach, we estimate the causal effect of treatment by analyzing time series
data from both treatment and control groups. We compare the treatment effect of users who had direct
interaction with bots and those who did not, 30 days after direct interaction.
The estimator and formula of a DiD model is as followed [52]:
Yit = α + β1Treati + β2Postt + β3(Treati × Postt ) +εit
In the estimator, Treati is the key explanatory variable of differences in the treatment state, and Postt is
the dummy temporal variable that says if it is before or after treatment.
For models estimating impacts on tweeting ’amount’, we included days without any records of tweets
(zero-tweet days) into our dataset for estimation. Because of the excessive number of zeros in the dependent
variable in this case, we used zero-inflated negative binomial models to calculate the effect of bot interaction
on the number of tweets. Since average daily sentiment is normally distributed, we used Linear Models to
estimate bot impact.
10/46

We also control for variables that can provide alternative explanations for our findings. Our topic
analysis revealed that bot activity is topic dependent and bots generate cascades, consequently influencing
human communication. Throughout this process, bots might interact with humans multiple times. There-
fore, we control for burstiness, the topic of the interaction, and the total number of bot interactions for each
user. The sentiment of the interaction and the popularity of the original tweets could impact the level of
activity in a thread. Longer threads may attract more bots, and we take these factors into account as well.
In our models that compare the impact of bot interaction by support categories, we also control the support
level of the interacted bot and their astroturf score. (See SI Table S12-S23 for full model tables).
AUTHOR CONTRIBUTIONS
L.L., O.V ., and B.V . designed research; L.L., O.V ., and B.V . performed research; L.L. O.V . and B.V .
analyzed data; and L.L., O.V ., and B.V . wrote the paper. L.L and O.V contributed equally to this work.
LICENSE
For the purpose of open access, the author has applied a CC BY public copyright licence to any Author
Accepted Manuscript version arising from this submission.
CONFLICTS OF INTEREST
The authors declare no conflict of interest.
REFERENCES
[1] H. Farrell, “The Consequences of the Internet for Politics,” Annual Review of Political Science ,
vol. 15, no. 1, pp. 35–52, 2012. [Online]. Available: http://www.annualreviews.org/doi/10.1146/
annurev-polisci-030810-110815
[2] F. B. Keller, D. Schoch, S. Stier, and J. H. Yang, “Political Astroturfing on Twitter: How to Coordinate
a Disinformation Campaign,” Political Communication, vol. 37, no. 2, pp. 256–280, 2020. [Online].
Available: https://doi.org/10.1080/10584609.2019.1661888
[3] N. Caren, K. T. Andrews, and T. Lu, “Contemporary social movements in a hybrid media environment,”
Annual Review of Sociology, vol. 46, pp. 443–465, 2020.
[4] A. Hepp, “Artificial companions, social bots and work bots: communicative robots as research objects
of media and communication studies,” Media, Culture and Society, vol. 42, no. 7-8, pp. 1410–1426,
2020.
[5] J. Seering, J. P. Flores, S. Savage, and J. Hammer, “The Social Roles of Bots,” Proceedings of the
ACM on Human-Computer Interaction, vol. 2, no. CSCW, pp. 1–29, 2018.
[6] I. Rahwan, M. Cebrian, N. Obradovich, J. Bongard, J. F. Bonnefon, C. Breazeal, J. W. Crandall, N. A.
Christakis, I. D. Couzin, M. O. Jackson, N. R. Jennings, E. Kamar, I. M. Kloumann, H. Larochelle,
D. Lazer, R. McElreath, A. Mislove, D. C. Parkes, A. S. Pentland, M. E. Roberts, A. Shariff, J. B.
Tenenbaum, and M. Wellman, “Machine behaviour,”Nature, vol. 568, no. 7753, pp. 477–486, 2019.
[Online]. Available: http://dx.doi.org/10.1038/s41586-019-1138-y
[7] D. Assenmacher, L. Clever, L. Frischlich, T. Quandt, H. Trautmann, and C. Grimme, “Demystifying
Social Bots: On the Intelligence of Automated Social Media Actors,” Social Media and Society, vol. 6,
no. 3, 2020.
[8] M. T. Bastos and D. Mercea, “The Brexit Botnet and User-Generated Hyperpartisan News,”Social
Science Computer Review, vol. 37, no. 1, pp. 38–54, 2019.
[9] T. R. Keller and U. Klinger, “Social Bots in Election Campaigns: Theoretical, Empirical, and Method-
ological Implications,” Political Communication, vol. 36, no. 1, pp. 171–189, 2019.
[10] S. Gonz ´alez-Bail´on and M. De Domenico, “Bots are less central than verified accounts during
contentious political events,” Proceedings of the National Academy of Sciences of the United States of
America, vol. 118, no. 11, 2021.
[11] S. C. Woolley and P. N. Howard, “Political communication, Computational Propaganda, and au-
tonomous agents: Introduction,” International Journal of Communication, vol. 10, pp. 4882–4890,
2016.
[12] E. Ferrara, O. Varol, C. Davis, F. Menczer, and A. Flammin, “The rise of social
robots,” Communi- cations of the ACM , vol. 59, no. 7, 2016. [Online]. Available:
https://www.ted.com/talks/cynthia{ }breazeal{ }the{ }rise{ }of{ }personal{ }robots
11/46

[13] E. Ferrara, “Measuring Social Spam and the Effect of Bots on Information Diffusion in Social Media,”
Complex spreading phenomena in social systems: Influence and contagion in real-world social
networks, pp. 229–255, 2018.
[14] M. C. Forelle, P. N. Howard, A. Monroy-Hernandez, and S. Savage, “Political Bots and the Manipula-
tion of Public Opinion in Venezuela,”SSRN Electronic Journal, pp. 1–8, 2015.
[15] C. Shao, G. L. Ciampaglia, O. Varol, K. C. Yang, A. Flammini, and F. Menczer, “The spread of
low-credibility content by social bots,” Nature Communications, vol. 9, no. 1, 2018.
[16] M. Stella, E. Ferrara, and M. De Domenico, “Bots increase exposure to negative and inflammatory
content in online social systems,” Proceedings of the National Academy of Sciences of the United
States of America, vol. 115, no. 49, pp. 12 435–12 440, 2018.
[17] N. Grinberg, K. Joseph, L. Friedland, B. Swire-Thompson, and D. Lazer, “Political science: Fake
news on Twitter during the 2016 U.S. presidential election,”Science, vol. 363, no. 6425, pp. 374–378,
2019.
[18] S. V osoughi, D. Roy, and S. Aral, “The spread of true and false news online,”Science, vol. 359, no.
6380, pp. 1146–1151, 2018.
[19] M. Stella, M. Cristoforetti, and M. De Domenico, “Influence of augmented humans in online interac-
tions during voting events,”PLoS ONE, vol. 14, no. 5, pp. 1–8, 2019.
[20] R. W. Gehl and M. Bakardjieva,Socialbots and Their Friends: Digital Media and the Automation of
Sociality, 1st ed. USA: Routledge, 2016.
[21] F. Sch¨afer, S. Evert, and P. Heinrich, “Japan’s 2014 General Election: Political Bots, Right-Wing
Internet Activism, and Prime Minister Shinz¯o Abe’s Hidden Nationalist Agenda,”Big Data, vol. 5,
no. 4, pp. 294–309, 2017.
[22] L. Hagen, S. Neely, T. E. Keller, R. Scharf, and F. E. Vasquez, “Rise of the Machines? Examining the
Influence of Social Bots on a Political Discussion Network,” Social Science Computer Review, 2020.
[23] E. T. C. D. Oliveira, F. O. D. Franca, D. H. Goya, and C. L. D. C. Penteado, “The influence of retweeting
robots during brazilian protests,” Proceedings of the Annual Hawaii International Conference on
System Sciences, vol. 2016-March, pp. 2068–2076, 2016.
[24] N. K ¨obis, J. F. Bonnefon, and I. Rahwan, “Bad machines corrupt good morals,” Nature Human
Behaviour, vol. 5, no. 6, pp. 679–685, 2021. [Online]. Available: http://dx.doi.org/10.1038/
s41562-021-01128-2
[25] M. Mosleh, C. Martel, D. Eckles, and D. G. Rand, “Shared partisanship dramatically increases
social tie formation in a Twitter field experiment,”Proceedings of the National Academy of Sciences
of the United States of America , vol. 118, no. 7, p. e2022761118, feb 2021. [Online]. Available:
https://www.pnas.org/doi/abs/10.1073/pnas.2022761118
[26] C. A. Bail, L. P. Argyle, T. W. Brown, J. P. Bumpus, H. Chen, M. B. F. Hunzaker, J. Lee, M. Mann,
F. Merhout, and A. V olfovsky, “Exposure to opposing views on social media can increase political
polarization,” Proceedings of the National Academy of Sciences, vol. 115, no. 37, pp. 9216–9221, sep
2018. [Online]. Available: http://www.pnas.org/lookup/doi/10.1073/pnas.1804840115
[27] B. Ross, L. Pilz, B. Cabrera, F. Brachten, G. Neubaum, and S. Stieglitz, “Are social bots a real threat?
An agent-based model of the spiral of silence to analyse the impact of manipulative actors in social
networks,” European Journal of Information Systems, vol. 28, no. 4, pp. 394–412, 2019.
[28] R. Schuchard, A. T. Crooks, A. Stefanidis, and A. Croitoru, “Bot stamina: examining the influence
and staying power of bots in online social networks,” Applied Network Science, vol. 4, no. 1, 2019.
[29] D. Stukal, S. Sanovich, J. A. Tucker, and R. Bonneau, “For Whom the Bot Tolls: A Neural Networks
Approach to Measuring Political Orientation of Twitter Bots in Russia,” SAGE Open, vol. 9, no. 2,
2019.
[30] D. Murthy, A. B. Powell, R. Tinati, N. Anstead, L. Carr, S. J. Halford, and M. Weal, “Bots and
political influence: A sociotechnical investigation of social network capital,” International Journal of
Communication, vol. 10, no. June, pp. 4952–4971, 2016.
[31] C. A. D. L. Salge and E. Karahanna, “Protesting Corruption on Twitter: Is It a Bot or Is It a Person?”
Academy of Management Discoveries, vol. 4, no. 1, pp. 32–49, 2018.
[32] S. Gonz´alez-Bail´on, J. Borge-Holthoefer, and Y . Moreno, “Broadcasters and Hidden Influentials in
Online Protest Diffusion,” American Behavioral Scientist, vol. 57, no. 7, pp. 943–965, 2013.
[33] J. Earl, T. V . Maher, and J. Pan, “The digital repression of social movements, protest, and activism: A
synthetic review,” pp. 1–16, 2022.
[34] D. Freelon, C. McIlwain, and M. Clark, “Quantifying the power and consequences of social media
protest,” New Media and Society, vol. 20, no. 3, pp. 990–1011, 2018.
[35] W. Jennings and C. Saunders, “Street Demonstrations and the Media Agenda: An Analysis of the
Dynamics of Protest Agenda Setting,” Comparative Political Studies, vol. 52, no. 13-14, pp. 2283–
12/46

2313, 2019.
[36] Z. Gilani, R. Farahbakhsh, G. Tyson, and J. Crowcroft, “A large-scale behavioural analysis of bots and
humans on twitter,” ACM Transactions on the Web (TWEB), vol. 13, no. 1, pp. 1–23, 2019.
[37] M. Shirakawa, T. Hara, and T. Maekawa, “Never abandon minorities: Exhaustive extraction of bursty
phrases on microblogs using set cover problem,” in Proceedings of the 2017 Conference on Empirical
Methods in Natural Language Processing. Copenhagen, Denmark: Association for Computational
Linguistics, Sep. 2017, pp. 2358–2367. [Online]. Available: https://aclanthology.org/D17-1251
[38] C. Comito, A. Forestiero, and C. Pizzuti, “Bursty event detection in twitter streams,”ACM Transactions
on Knowledge Discovery from Data (TKDD), vol. 13, no. 4, pp. 1–28, 2019.
[39] N. Carter, The Politics of the Environment: Ideas, Activism, Policy, 3rd ed. Cambridge University
Press, 2018.
[40] W. L. Bennett and A. Segerberg, “The logic of connective action: Digital media and the personalization
of contentious politics,” Information Communication and Society, vol. 15, no. 5, pp. 739–768, 2012.
[41] T. Marlow, S. Miller, and J. T. Roberts, “Bots and online climate discourses: Twitter discourse on
president trump’s announcement of u.s. withdrawal from the paris agreement,” Climate Policy, vol. 21,
no. 6, pp. 765–777, 2021. [Online]. Available: https://doi.org/10.1080/14693062.2020.1870098
[42] C. F. Chen, W. Shi, J. Yang, and H. H. Fu, “Social bots’ role in climate change discussion on Twitter:
Measuring standpoints, topics, and interaction strategies,” Advances in Climate Change Research,
vol. 12, no. 6, pp. 913–923, 2021. [Online]. Available: https://doi.org/10.1016/j.accre.2021.09.011
[43] C. Wagner, S. Mitter, C. K¨orner, M. Strohmaieret al., “When social bots attack: Modeling susceptibility
of users in online social networks.” in # MSM, 2012, pp. 41–48.
[44] E. Alothali, N. Zaki, E. A. Mohamed, and H. Alashwal, “Detecting social bots on twitter: a literature
review,” in2018 International conference on innovations in information technology (IIT). IEEE,
2018, pp. 175–180.
[45] F. Martini, P. Samula, T. R. Keller, and U. Klinger, “Bot, or not? comparing three methods for detecting
social bots in five political discourses,”Big data & society, vol. 8, no. 2, p. 20539517211033566, 2021.
[46] K. Yang, E. Ferrara, and F. Menczer, “Botometer 101: Social bot practicum for computational social
scientists,” CoRR, vol. abs/2201.01608, 2022. [Online]. Available: https://arxiv.org/abs/2201.01608
[47] A. Rauchfleisch and J. Kaiser, “The false positive problem of automatic bot detection in
social science research,” PLOS ONE , vol. 15, no. 10, pp. 1–20, 10 2020. [Online]. Available:
https://doi.org/10.1371/journal.pone.0241045
[48] X. Yan, J. Guo, Y . Lan, and X. Cheng, “2013-a Bitem Topic Model for Short Texts.Pdf,”
Www, pp. 1445–1455, 2013. [Online]. Available: http://delivery.acm.org/10.1145/2490000/
2488514/p1445-yan.pdf?ip=137.189.241.20{&}id=2488514{&}acc=ACTIVESERVICE{&}key=
CDD1E79C27AC4E65.63D3CA449C1BD759.4D4702B0C3E38B35.4D4702B0C3E38B35{&}{ }
{ }acm{ }{ }=1548658783{ }4fb56b68e11530cddd7103a94a10778c
[49] K.-I. Goh and A.-L. Barabasi, “Burstiness and memory in complex systems,” 2006.
[50] B. D. Easley, “Chapter 16 Information Cascades,” Networks, Crowds, and Markets , pp. 483–508,
2010.
[51] C. Hsiao, “Causality tests in econometrics,” Journal of Economic Dynamics and Control , vol. 1,
no. 4, pp. 321–346, nov 1979. [Online]. Available: https://www.sciencedirect.com/science/article/pii/
S0165188979901945
[52] S. Athey and G. W. Imbens, “Identification and inference in nonlinear difference-in-differences models,”
Econometrica, vol. 74, no. 2, pp. 431–497, 2006.
[53] O. Varol, E. Ferrara, C. Davis, F. Menczer, and A. Flammini, “Online human-bot interactions:
Detection, estimation, and characterization,” in Proceedings of the international AAAI conference on
web and social media, vol. 11, no. 1, 2017, pp. 280–289.
[54] O. Varol, E. Ferrara, C. A. Davis, F. Menczer, and A. Flammini, “Online human-bot interactions:
Detection, estimation, and characterization,” Proceedings of the 11th International Conference on Web
and Social Media, ICWSM 2017, no. Icwsm, pp. 280–289, 2017.
[55] K. Yang, O. Varol, C. A. Davis, E. Ferrara, A. Flammini, and F. Menczer, “Arming the
public with AI to counter social bots,” CoRR, vol. abs/1901.00912, 2019. [Online]. Available:
http://arxiv.org/abs/1901.00912
[56] S. Feng, Z. Tan, H. Wan, N. Wang, Z. Chen, B. Zhang, Q. Zheng, W. Zhang, Z. Lei, S. Yang,
X. Feng, Q. Zhang, H. Wang, Y . Liu, Y . Bai, H. Wang, Z. Cai, Y . Wang, L. Zheng, Z. Ma, J. Li, and
M. Luo, “TwiBot-22: Towards Graph-Based Twitter Bot Detection,”Advances in Neural Information
Processing Systems, pp. 1–25, 2022. [Online]. Available: http://arxiv.org/abs/2206.04564
[57] B. Vedres and O. Vasarhelyi, “Gendered behavior as a disadvantage in open source software develop-
ment,” EPJ Data Science, vol. 8, no. 1, p. 25, 2019.
13/46

[58] Z. Chu, S. Gianvecchio, H. Wang, and S. Jajodia, “Detecting automation of Twitter accounts: Are you
a human, bot, or cyborg?” IEEE Transactions on Dependable and Secure Computing, vol. 9, no. 6, pp.
811–824, 2012.
[59] L. Luceri, A. Deb, A. Badawy, and E. Ferrara, “Red bots do it better: Comparative analysis of social
bot partisan behavior,” inCompanion proceedings of the 2019 world wide web conference, 2019, pp.
1007–1012.
[60] Q. Mei, Y . Xie, W. Yuan, and M. O. Jackson, “A turing test of whether ai chatbots are behaviorally
similar to humans,” Proceedings of the National Academy of Sciences, vol. 121, no. 9, p. e2313925121,
2024.
[61] A. Jo, “The promise and peril of generative ai,” Nature, vol. 614, no. 1, pp. 214–216, 2023.
[62] K.-C. Yang and F. Menczer, “Anatomy of an ai-powered malicious social botnet,” arXiv preprint
arXiv:2307.16336, 2023.
[63] The Verge, “Twitter’s new Elon Musk API policy is already chilling academic research,” https://www.
theverge.com/2023/5/31/23739084/twitter-elon-musk-api-policy-chilling-academic-research, May
2023.
[64] ——, “Reddit’s API changes are already starting to shut down some apps,” https://www.theverge.com/
2023/6/9/23755640/reddit-api-changes-apps-apollo-shut-down-ama-spez-steve-huffman, June 2023.
[65] TechCrunch, “IRL shuts down, citing issues with fake users,” https://techcrunch.com/2023/06/26/
irl-shut-down-fake-users/, June 2023.
[66] H. Y . Yan, K.-C. Yang, J. Shanahan, and F. Menczer, “Exposure to social bots amplifies perceptual
biases and regulation propensity,”Scientific Reports, vol. 13, no. 1, p. 20707, 2023.
[67] European Commission, “Digital Services Act (DSA) overview,” https://commission.europa.
eu/strategy-and-policy/priorities-2019-2024/europe-fit-digital-age/digital-services-act en#:
∼:text=Digital%20Services%20Act%20(DSA)%20overview,online%20travel%20and%
20accommodation%20platforms., August 2023.
[68] I. Solaiman, “The gradient of generative ai release: Methods and considerations,” in Proceedings of
the 2023 ACM Conference on Fairness, Accountability, and Transparency, ser. FAccT ’23. New
York, NY , USA: Association for Computing Machinery, 2023, p. 111–122. [Online]. Available:
https://doi.org/10.1145/3593013.3593981
[69] S. Li, J. Yang, and K. Zhao, “Are you in a masquerade? exploring the behavior and impact of large
language model driven social bots in online social networks,” arXiv preprint arXiv:2307.10337, 2023.
[70] M. del Rio-Chanona, N. Laurentsyeva, and J. Wachs, “Are large language models a threat to digital
public goods? evidence from activity on stack overflow,”arXiv preprint arXiv:2307.07367, 2023.
[71] Twitter, “Twitter API for Academic Research — Products — Twitter Developer Platform,” 2022.
[Online]. Available: https://developer.twitter.com/en/products/twitter-api/academic-research
[72] M. Sayyadiharikandeh, O. Varol, K. Yang, A. Flammini, and F. Menczer, “Detection of novel social
bots by ensembles of specialized classifiers,” CoRR, vol. abs/2006.06867, 2020. [Online]. Available:
https://arxiv.org/abs/2006.06867
[73] K.-C. Yang, O. Varol, P.-M. Hui, and F. Menczer, “Scalable and Generalizable Social Bot Detection
through Data Selection,” Proceedings of the AAAI Conference on Artificial Intelligence, vol. 34, no. 01,
pp. 1096–1103, apr 2020. [Online]. Available: https://ojs.aaai.org/index.php/AAAI/article/view/5460
[74] L. Shi, G. Cheng, S. R. Xie, and G. Xie, “A word embedding topic model for topic detection and
summary in social networks,” Measurement and Control (United Kingdom), vol. 52, no. 9-10, pp.
1289–1298, 2019.
[75] J. Wijffels, BTM: Biterm Topic Models for Short Text , 2023, r package version 0.3.7. [Online].
Available: https://CRAN.R-project.org/package=BTM
[76] S. Bird, E. Klein, and E. Loper, Natural language processing with Python: analyzing text with the
natural language toolkit. ” O’Reilly Media, Inc.”, 2009.
[77] M. Terpilovskii and C. K¨alin, “Bitermplus package,” 2022. [Online]. Available: https://bitermplus.
readthedocs.io/en/latest/index.htmlhttps://bitermplus.readthedocs.io/en/latest/install.html
[78] M. R ¨oder, A. Both, and A. Hinneburg, “Exploring the space of topic coherence measures,” in
Proceedings of the Eighth ACM International Conference on Web Search and Data Mining , ser.
WSDM ’15. New York, NY , USA: Association for Computing Machinery, 2015, p. 399–408.
[Online]. Available: https://doi.org/10.1145/2684822.2685324
[79] M. T. Bahadori and Y . Liu, “An examination of practical granger causality inference,”Proceedings of
the 2013 SIAM International Conference on Data Mining, SDM 2013, pp. 467–475, 2013.
[80] A. Ceron, L. Curini, and S. M. Iacus, “First- and second-level agenda setting in the Twittersphere: An
application to the Italian political debate,” Journal of Information Technology and Politics, vol. 13,
no. 2, pp. 159–174, 2016. [Online]. Available: http://dx.doi.org/10.1080/19331681.2016.1160266https:
14/46

//doi.org/10.1080/19331681.2016.1160266
[81] M. T. Bastos, D. Mercea, and A. Charpentier, “Tents, tweets, and events: The interplay between
ongoing protests and social media,” Journal of Communication, vol. 65, no. 2, pp. 320–350, 2015.
[82] C. J. Hutto and E. Gilbert, “Vader: A parsimonious rule-based model for sentiment analysis of social
media text.” in ICWSM, E. Adar, P. Resnick, M. D. Choudhury, B. Hogan, and A. H. Oh, Eds. The
AAAI Press, 2014. [Online]. Available: http://dblp.uni-trier.de/db/conf/icwsm/icwsm2014.html
[83] P. Xu, Y . Wu, E. Wei, T. Q. Peng, S. Liu, J. J. H. Zhu, and H. Qu, “Visual analysis of topic competition
on social media,” IEEE Transactions on Visualization and Computer Graphics, vol. 19, no. 12, pp.
2012–2021, 2013.
[84] M. D. Vicario, A. Bessi, F. Zollo, F. Petroni, A. Scala, G. Caldarelli, H. E. Stanley, and W. Quattro-
ciocchi, “The spreading of misinformation online,” Proceedings of the National Academy of Sciences
of the United States of America, vol. 113, no. 3, pp. 554–559, 2016.
[85] OpenAI, “ChatGPT: A large language model trained by openai,” https://openai.com/chatgpt, 2024,
accessed on March 13, 2024.
[86] Y . Zhu, P. Zhang, E.-U. Haq, P. Hui, and G. Tyson, “Can chatgpt reproduce human-generated labels? a
study of social computing tasks,” arXiv preprint arXiv:2304.10145, 2023.
[87] L. Wu, Y . Chen, J. Yang, G. Shi, X. Qi, and S. Deng, “Event-centric opinion mining via in-context
learning with chatgpt,” inChina Conference on Knowledge Graph and Semantic Computing. Springer,
2023, pp. 83–94.
15/46

Supporting Information for1
Social bots sour activist sentiment without eroding engagement2
Linda Li, Orsolya Vásárhelyi and Balázs Vedres3
Balázs Vedres4
E-mail: vedresb@ceu.edu5
This PDF ﬁle includes:6
Supporting text7
Figs. S1 to S78
Tables S1 to S259
SI References10
Linda Li, Orsolya Vásárhelyi and Balázs Vedres 1 of 31

Supporting Information Text11
Data Sampling12
Because the API provided access to a full archive of tweets, we believe this to be a relatively comprehensive sample of all13
politician communication related to XR on the Twitter-sphere. However, it is worth noticing that we are collecting the data in14
a retrospective manner. Twitter imposes some extent of censorship on spam messages, and users may remove their account or15
messages between the protests events and the time point of our data collection. Because of the controversy of the subject16
(protests), the volatile behaviour of social bots and their often one-oﬀ nature, there is a higher possibility for social bots to17
have their messages deleted or accounts suspended, as compared to human users. For example, an active bot account run by18
XR activists, the @xr_bot, was suspended when the data was collected. Neither the user proﬁle nor their timeline could be19
retrieved if that is the case. Therefore, our estimation of the size, amount and impact of bot activities may be slightly lower20
than that in reality.21
Furthermore, when collecting the tweets by our sample and their matching users, because we were collecting archived data,22
there is the possibility that the number of likes changes after the users interact with the bots. However, we were analysing a23
series of regional and time-sensitive protest events that only caught attention in a relatively small scale ( 200k tweets in total).24
Therefore, we suppose that the number of "likes" for a tweet shall remain relatively stable after the protests faded out of public25
attention.26
Keywords
XRebellion
xrebellion
#ExtinctionRebellion
extinction rebellion
XR
climate change protest
Table S1. Keywords for tweet collection.
Bot identiﬁcation27
Botometer.We began our bot identiﬁcation process by adopting the widely adopted Twitter bot identiﬁcation tool known as28
botometer. This publicly available tool relies on machine learning and was initially released on May 1, 2014, with the latest29
update in September 2020. The developers of botometer explain that it is designed to calculate a score where low scores30
indicate likely human accounts, while high scores suggest likely bot accounts (1). The algorithm considers over 1,000 features31
related to user proﬁles, friends, network structure, and activity patterns, among others. Due to its widespread use by social32
scientists for identifying Twitter bots in research, we decided to adopt botometer as the baseline model of our bot identiﬁcation33
method. We will mostly use its results and compare our self-trained models to it.34
The botometer tool works as follows. For each classiﬁed user, botometer generates a list of scores representing the user’s bot35
probabilities. The scores include an overall score and sub-scores categorised based on the nature of bots: echo-chamber, fake36
follower, ﬁnancial bots, self-declared bots, spammers and other. According to the developers, these scores, also referred to as37
complete automation probabilities (CAP), represent the probability that an account with a score equal to or greater than38
the given value is controlled by softwares. (1). For instance, a user with an overall CAP of 0.96 means 96% of the users with39
similar proﬁles are highly likely to be fully automated. Since our research design required binary bot identiﬁcation results, we40
followed the common practice observed in existing studies. We deﬁned a threshold, and users with an overall CAP exceeding41
this threshold were considered "bots," while those below it were classiﬁed as "humans." This approach allowed us to distinguish42
between automated and human-operated accounts."43
However, considerable debate surrounds the appropriate usage and interpretation of these scores (2, 3). To address the44
controversies and concerns, we conducted a series of robustness checks. The primary concerns is about determining the best45
practices in interpreting the botometer scores. As previously mentioned, a threshold is necessary for binary classiﬁcation, and it46
must be deﬁned by researchers. Existing studies have employed various standards, ranging from 0.25 to 0.76. These thresholds47
are often justiﬁed based on the following standards:48
• Common practice in machine learning, where 0.5 serves as a widely used threshold for binary classiﬁcation tasks.49
• A "tipping point" approach, where the threshold is set at a value where the majority of users’ bot probabilities fall below50
it.51
• Insights derived from the botometer team’s reports on model performance on their training data, utilizing metrics such52
as the F1 score and Receiver Operating Characteristic - Area Under the Curve (ROC-AUC).53
• Tailoring the threshold to the speciﬁc context and research needs of the study.54
2 of 31 Linda Li, Orsolya Vásárhelyi and Balázs Vedres

Fig. S1. Proportion of user classiﬁed as "bots" (red) and "humans" (blues) in the data set, with bot thresholds ranging from 0.5 to 1.0.
By exploring and accounting for these diﬀerent threshold options, we aim to ensure the robustness and accuracy of our55
bot identiﬁcation methodology. This approach allows us to adapt the classiﬁcation to the nuances and unique aspects of our56
research, enhancing the reliability of our ﬁndings.57
Based on the methods adopted by previous studies, we have chosen to use the thresholds of 0.65 and 0.5 to classify bots.58
Speciﬁcally, users with a CAP higher than 0.65 are categorized as "automated," those with a CAP less than 0.5 as "human,"59
and those falling in between as "unknown." This decision is based on the following rationales: Firstly, we adopt 0.5 as the60
threshold for humans, following common practices (method a). Secondly, our research focuses on investigating the impact61
of social bots on human behavior at both the individual (micro) and network (meso) levels. Therefore, the validity of our62
results is particularly sensitive to false positives (incorrectly classifying humans as bots). As a result, we lean towards using a63
more conservative threshold for bot identiﬁcation to avoid false positives. However, an excessively strict threshold could lead64
to an underestimation of the scale and extent of bot impact. To address this concern, we have improved upon the approach65
described in standard b) above: we classify bots using the strictest threshold possible before the tipping point, ensuring that66
we do not experience a signiﬁcant drop in the sample size available for analysis. Figure S1 illustrates the distribution of users67
classiﬁed as "bot" or "human" at diﬀerent thresholds in the case of XR Twitter discussions, while Figure S2 displays the users68
and bots ﬁltered for our matching-based research design. After considering the aforementioned rationales, we have determined69
0.65 to be the most suitable threshold for bot identiﬁcation in our study.70
Self-trained models.To identify political bots on the Twittersphere, this research employed supervised machine learning models71
trained on open-source data containing both bots and humans. The training sets were sourced from existing open-source72
data of Twitter accounts categorised as ’bots’ and ’humans’. Table S3 provides a list of all the training datasets that we used.73
These datasets encompassed various types of political bots identiﬁed through previous research and user feedback, such as fake74
followers, spam message bots, and astroturﬁng bots. Some of those users were known to be active in political events, including75
the 2018 U.S. midterm election election. The data was divided into a 70% training set and a 30% testing set. In total, the76
training and testing sets consisted of 24,596 users, with 9,813 classiﬁed as non-bots and 14,783 as bots. Since only 40% of77
the training set comprised bots, we applied appropriate weights to the training dataset for both bots and non-bots to ensure78
balanced learning. As this research focuses on bot activities in 2019 and 2020, only bots identiﬁed from 2017 onwards up until79
2020 were included, as bot strategies continually evolve, and older training sets may be outdated. Each dataset contained80
Twitter accounts marked as humans or bots, along with their full user proﬁle metrics. To train all models eﬀectively, we81
employed grid search methods to determine the optimal parameters for each model, ensuring robust performance and accurate82
identiﬁcation of political bots.83
This research then trained bot identiﬁcation models with ﬁve types of algorithms: random forest(RF), support vector84
machine(SVM), logistic regression(LOG), XGboost classiﬁcation (XGB) and deep learning (DL). Based on existing research(4),85
we ﬁrst adopted ten features that were proved most eﬀective for bot identiﬁcation: (1) statuses count; (2) followers count; (3)86
friends count; (4) favourites count; (5) listed count; (6) default proﬁle; (7) geo enabled; (8) proﬁle use background image; (9)87
protected; and (10) veriﬁed. Other state-of-art bot identiﬁcation research stated 10 other features that was shown to be also88
potentially useful and scalable (5, 6), so we further trained 20-feature models with the ten traits above and these traits added:89
(1) follower-friend ratio; (2) screen name length; (3) favorites growth (average daily number of favourited tweets); (4) digits in90
name; (5) listed growth; (6) tweeting freq (average daily number of tweets) (7) followers growth; (8) friends growth; (9) name91
length; (10) description length. For the DL models, we adopted an approach similar to Gonzalez-Bailon et al(2021)’s existing92
research of bot identiﬁcation in the political context. The DL model includes four fully-connected hidden layers, and they93
included 2 x N feats, 4 x N feats, Nfeats and 2 hidden nodes respectively. Besides, the model also introduced a dropout rate of94
Linda Li, Orsolya Vásárhelyi and Balázs Vedres 3 of 31

Fig. S2. Number of sample users and matched users and the total number of their posted tweets, with bot thresholds ranging from 0.5 to 0.85.
Table S2. List of the training datasets
Dataset
Twibot-20
veriﬁed-2019
vendor-purchased-2019
political-bots-2019
cresci-rtbust-2019
botometer-feedback-2019
botwiki-2019
midterm-2018
0.2 between hidden layers to prevent overﬁtting. All models besides DL were ﬁtted with the scikit-learn package, while the DL95
model used Tensorﬂow(7) and Keras(8).96
Figure S3 provides a comparison of the performance of all four models (10 and 20-feature variations) we selected on the97
testing sets. Among the best models in each category, their performance was evaluated using ﬁve metrics: speciﬁcity (True98
Negative Rate), sensitivity (True Positive Rate), Balanced Accuracy, Accuracy, and F1 score. Figure S3 demonstrates that99
the 20-trait RF, DL, and XGB models slightly outperformed other models across all metrics. The RF model exhibited high100
sensitivity, while the DL and XGB models showed higher speciﬁcity. Both of these traits are crucial for this research, as it aims101
to understand the impact of bots in the political communication domain. Type I error (false positive) could introduce more102
noise and decrease the reliability of our causal inference regarding bots’ impact on human actions. On the other hand, Type II103
error (false negative) might lead us to underestimate the size of bots. Since bots are known for generating a signiﬁcant number104
of messages and creating information cascades, a high Type II error rate could result in an underestimation of the scale and105
importance of their impact in our case. Considering that each model has its advantages and drawbacks, further comparison106
and evaluation are necessary.107
To conduct a more in-depth comparison and evaluation, this study proceed to test the DL model, the 20-feature RF model,108
and the XGB model on an independent dataset. This dataset included both bots and humans active during the 2018 United109
States midterm election (9). In both cases, the bots were active in political events and demonstrated their ability to disguise as110
humans to inﬂuence political debates on the Twittersphere, particularly in immigration-related discussions before the midterm111
elections. These bots align with the characteristics we aimed to detect: human-mimicking, inﬂuential bots actively participating112
in political communication on Twitter. The publicly available nature of the dataset and its relevance to our research made it a113
suitable choice for model evaluation.114
Figure S4 provides an overview of seven metrics representing the testing results of the models. It’s essential to note that the115
US midterm election dataset was highly skewed, with predominantly 90% bot users, which may have impacted the evaluation116
metrics. Figure S4 shows that all models exhibited satisfactory performance, surpassing the existing bot identiﬁcation methods117
tested on the same datasets in previous research (4). The RF and DL models displayed high precision (93% weighted average),118
4 of 31 Linda Li, Orsolya Vásárhelyi and Balázs Vedres

Specificity Sensitivity Balanced Accuracy Accuracy F1
0.0
0.2
0.4
0.6
0.8Metric value
RF
SVM
LOGR
DL
XGB
Fig. S3. Comparison of metrics between ﬁve bot identiﬁcation models trained on the training data set.
Specificity Sensitivity Precision Balanced AccuracyAccuracy F1
0.0
0.2
0.4
0.6
0.8
1.0Value
RF
DL
XGB
Fig. S4. Comparison of metrics between the Random forest(RF), XGboost (XGB) and Deep learning (DL) models with an external dataset - the US midterm election bot data
set from (9).
while the XGB model demonstrated a good recall rate (89%). This indicates that XGB is a stricter identiﬁcation method that119
can reduce the Type II error rate, whereas RF and DL excel at decreasing the Type I error rate.120
The ﬁnal combined approach. Our ﬁnal bot identiﬁcation approach combines the results from both sets of bot identiﬁcation121
methods: the botometer output and our self-trained algorithm output. As described earlier, we optimized both bot identiﬁcation122
pipelines, carefully selecting the best threshold for the botometer-based approach based on past literature and established123
scientiﬁc standards. Additionally, we ﬁne-tuned and validated our self-trained machine learning models, speciﬁcally trained with124
data from political bots. However, due to potential false positive issues in both methods, they produced somewhat diﬀerent125
results (2). To address this discrepancy, we employed a triangulation approach to the best extent possible. This involved126
classifying a user based on the intersection of the results from botometer and our own algorithms (DL, RF, or XGB). If both127
botometer and at least one of our own algorithms identiﬁed a user as a bot, they were classiﬁed as a bot, and vice versa for128
humans.129
Support group categorization130
We used ChatGPT 3.5 to categorize the users’ opinion on protests. The full prompt is as follows:131
On the text that I will give you in the following dialogues, please interpret it as a human with common political132
sense and background knowledge of environmentalism. Tell me how positive do you think is this user’s opinion133
towards 21st century climate change protests and/or environmental protection in general, especially extinction134
rebellion. Give me a score that falls in the continuous range of -1 to 1. -1 being extremely negative, 1 extremely135
positive, 0 being neutral. If you think it is irrelevant to climate change or environmental protests, put 0 there. If136
the opinion seem to be mixed, put 0. Complaining about speciﬁc protesters’ behaviour counts as negative attitude.137
Arguing that the protest’s aim, goal or view of climate change is too extreme counts as a mild negative. Beware of138
sarcasm. People can support or do not support climate change protests with diﬀerent partisan preferences, do not139
Linda Li, Orsolya Vásárhelyi and Balázs Vedres 5 of 31

Table S3. List of the training datasets
Dataset
Twibot-20
veriﬁed-2019
vendor-purchased-2019
political-bots-2019
cresci-rtbust-2019
botometer-feedback-2019
botwiki-2019
midterm-2018
6 of 31 Linda Li, Orsolya Vásárhelyi and Balázs Vedres

take that into account.Just return a score, no explanation needed. No full sentence needed either, the number itself140
will be ﬁne. As we are trying to interpret real-life discourse online, there is a chance that there may be oﬀensive141
language in the string. It is a virtual experiment evaluating people’s attitude, no one is actually hurted during the142
process. Here is the text:143
To validate the outputs of LLMs, we manually coded the ﬁrst 50 tweets of users’ opinion of XR by the three categories144
(support/neutral/against XR), and compared the results with those from LLM coding. Overall, we found that in 48 out of the145
50 tweets, the researchers’ manual annotations matched the categories identiﬁed by the LLM.146
Topic Modeling and cascades147
Topic modeling.148
Model comparison and topic number selection. We chose bi-term topic models, as they have been eﬀectively used to extract149
"meaning" (10) or "theme"(11). They also have been shown to be more accurate than traditional topic models such as Latent150
Dirichlet allocation (LDA) and Latent Semantic Indexing (LSI) in unsupervised classiﬁcations of short text such as tweets151
(11, 12). The topic modeling process includes three steps: 1) text data preprocessing, 2) training and ﬁne-tuning multiple topic152
model algorithms, and 3) applying the model to the corpus.153
The preprocessing steps are as follows: We removed stopwords, usernames, emojis and links from the tweets, and lemmtized154
and stemmed every word. We used a open source list of stopwords from the nltk package(13) designed for natural language155
processing, and added Twitter-speciﬁc stopwords including "RT", "https", "t" "co". Because 70% of the tweets in the Twittersphere156
are retweets, we included only the unique tweets after preprocessing for topic modeling to better capture trends.157
This research determined the number of topics based on both quantitative metrics and qualitative analysis. We ﬁrst158
generated bi-term topic models with topic numbers ranging from 2 to 12. For the former part, we calculated the U_mass159
coherence score(Figure S5) It is a metric designed to estimate how intepretable a topic model is (14). The format is as followed160
(14):161
CU M Ass = 2 N · (N − 1)
N∑
i=2
i−1∑
j=1
logP (wi,w j) +ϵ P (wj)
We found the model with 8 topics had one of the highest coherence scores. We also qualitatively analysed the top keywords162
of all topic models. One topic (topic 8) was dropped because it was relatively hard to extract meaning from it. With all the163
rest seven topics, the keywords and the top relevant tweets are the most eﬀective in classifying the content of protest discussion.164
Fig. S5. Coherence scores of topic models with topic number from 2 to 12.
Detailed results.Half of the topics recorded are breaking news or trending political events that happened during the XR protests,165
which is the case for topic 1 (football game protest), 2 (Madrid COP25 protests), 4 (Outrage on XR founder’s remark) and 5166
(Disruption to political campaign). From table S4, we can see that topic 1 is almost entirely about the Harvard-Yale football167
match on November 23, 2019, which was disrupted by fossil fuel protesters who occupied the ﬁeld mid-game.(15) Topic 2168
included news reports and discussions of the XR protests which happened outside the location of the 2019 United Nations169
Climate Change Conference held in Madrid, Spain.(16) The keywords, such as “strike, hunger, global, emergency, youth,170
school” suggest the protests was linked to the global hunger strike and the school strike against climate change. Topic 4 was171
predominately related to reports and comments related to the Extinction Rebellion founder’s comment on the Holocaust (just172
another f–kery in human history). Topic 5 mostly discussed a speciﬁc protest event happened in December 4, 2019, in which173
several protesters dressed up as bees and glued themselves to the campaign buses of Liberal Democrats. (17) It also included174
Linda Li, Orsolya Vásárhelyi and Balázs Vedres 7 of 31

Table S4. Summary of topics, top keywords and sample tweets
Topic Keywords Sample Tweet(s)
Topic 1 - Protest at the Harvard-Y ale football game
protest, yale, harvard, game,
football, ﬁeld, delayed, fossil,
activitists, parliament, disrupt,
stormed, boomer
"Harvard-Y ale football game interrupted by climate protest"
Topic 2 - Madrid COP25 protests
strike, hunger, action,
global, emergency, crisis,
cop, activists, madrid, youth,
join, school, leaders
"Thousands in Madrid are marching to protest the climate emergency.
#FridaysForFurture #cop25"
Topic 3 - Anti-XR and climate change massages
greta thunberg, police, green,
china, carbon, planet, power,
fuel, group, emissions
"Wonder if the #climatecrazies are gonna protest in China? This proves
the Paris Agreement is a joke."
Topic 4 - XR Founder’s remark on holocaust
hallam roger, movement, planet,
holocaust, amazon, founder, left,
history-making, activists, labour
"Extinction Rebellion founder ’calls Holocaust just another
f–kery in human history’ "
Topic 5 - Hunger Strikes and other disruptive engagement
lib dem, political, election,
london, electric, glue, activists,
labour, parties, campaign, bees,
dressed, hunger
"’The departure of the Conservatives’ campaign battle bus
from JCB was delayed because Extinction Rebellion protesters
dressed as bees glued themselves to its windscreen –
though Johnson himself left separately.’"
Topic 6 - Anti London protests messages
london, police, black, teens,
enchanting, arrested, fuck, air,
block, bridge, ﬁre, members,
jet, airport, geneva
"Teens chanting ‘fuck the police’ on a climate change protest
when only an hour later the very same Police were facing a
Suicide bomber on #LondonBridge, saving many lives.
#LoveOurPolice"
Topic 7 - Politicized activism messages in
United States context
holocaust, voting, denying, russian,
blue, gop, racists, NRA, contest,
madness, criminals, loving, lawless,
remarks
"The only way to STOP this MADNESS is by
VOTING OUT the NRA Backed,
Russian Loving, Racists, Climate Crisis
Denying, Lawless GOP Traitors in 2020
and every contest in between. No ’protest votes’!
Get everyone you know to VOTE BLUE like
YOUR life depends on it. It does..."
some tweets concerning the election campaigns by labour and conservative and how XR protesters attempted or claimed to175
disrupt them (keywords like “labour” and “parties”). In those four topics, the attitude and/or sentiment towards those events176
were mixed, including neutral narrative of the event, and both pro- and con- protest messages.177
Other topics was clustered based on sentiment or ideology instead of a speciﬁc event. Topic 6 (anti XR messages) and topic178
3 (criticism of protest motivation and goal) was clearly classiﬁed based on outbursts of anti-protest or anti-climate change179
sentiment. Topic 6 (outburst of anti-protest sentiment) was dominated by one single tweet with anti-protest attitude that went180
viral - 70% of the tweets in the topic was retweets and replies to this tweet:181
”Teens chanting ‘fuck the police’ on a climate change protest when only an hour later the very same Police were182
facing a Suicide bomber on #LondonBridge, saving many lives. #LoveOurPolice”183
Similarly, topic 3 was clustered around an opinion: criticisms to XR protests and its organisers, such as messages criticising184
the motivation, content, location and goals of the XR protests. Topic 7 (Politicized activism ) dealt with US election campaign185
messages pro Democrats that accused Republicans as climate change denying. Similar to topic 6, most of the tweets under this186
topic are also retweets or variants of this message:“The only way to STOP this MADNESS is by VOTING OUT the NRA187
Backed, Russian Loving, Racists, Climate Crisis Denying, Lawless GOP Traitors in 2020 and every contest in between. No188
’protest votes’! Get everyone you know to VOTE BLUE like YOUR life depends on it.”189
Information ﬂow.Apart from the main information ﬂow chart (Figure 1) in the main text, we also estimated information ﬂows190
between bots and humans by diﬀerent CAP thresholds (0.5 to 0.8) (Table S5), and information ﬂow inside each topics (Table191
S6). Original tweets by bots or humans are calculated as bot-bot, or human-human information ﬂow, respectively. Regarding192
Table S6, the information ﬂow associated with each topic is established based on a correspondence criterion: if at least one193
tweet from either side pertains to the topic, it is considered in the information ﬂow analysis.194
8 of 31 Linda Li, Orsolya Vásárhelyi and Balázs Vedres

Table S5. Information ﬂow between bots and humans at different bot thresholds.
Threshold Human RT human (%) Bot RT bot (%) Human RT bot (%) Bot RT human (%) Human total Bot total Human RT human sentiment Bot RT bot sentiment Human RT bot sentiment Bot RT human sentiment
0.50 20.41 47.99 22.67 8.92 78722 103991 -0.17 -0.11 -0.40 -0.25
0.55 23.39 43.68 23.43 9.50 85549 97164 -0.16 -0.11 -0.40 -0.24
0.60 25.95 40.34 24.34 9.37 91885 90828 -0.16 -0.11 -0.39 -0.23
0.65 29.79 35.58 25.42 9.20 100890 81823 -0.15 -0.11 -0.39 -0.22
0.70 33.85 31.02 26.00 9.13 109360 73353 -0.14 -0.11 -0.40 -0.18
0.75 40.83 24.40 25.80 8.97 121732 60981 -0.14 -0.11 -0.40 -0.17
0.80 85.42 5.90 3.51 5.16 162501 20212 -0.21 -0.06 -0.20 -0.18
Linda Li, Orsolya Vásárhelyi and Balázs Vedres 9 of 31

Table S6. Information ﬂow between bots and humans for tweets belonging to each topic, throughout the whole protest period.
Topics Human RT human (%) Bot RT bot (%) Human RT bot (%) Bot RT human (%) Human total Bot total Human RT human sentiment Bot RT bot sentiment Human RT bot sentiment Bot RT human sentiment
1 17.24 26.36 50.09 6.32 31237 15160 -0.06 -0.16 -0.59 -0.10
2 28.12 39.36 19.84 12.68 13388 14528 -0.11 -0.08 -0.10 -0.15
3 40.78 28.54 15.78 14.90 21258 16325 -0.42 -0.12 -0.16 -0.41
4 27.08 37.50 21.75 13.67 14693 15397 -0.08 -0.15 -0.20 -0.15
5 16.18 29.28 47.90 6.64 32822 18398 -0.06 -0.14 -0.61 -0.17
6 39.85 29.22 17.15 13.78 21211 16000 -0.41 -0.14 -0.18 -0.41
7 24.72 36.90 27.66 10.73 16645 15137 -0.06 -0.16 -0.25 -0.10
10 of 31 Linda Li, Orsolya Vásárhelyi and Balázs Vedres

Cascades.Table S8 and S9 show all the cascades identiﬁed, including their time range, the topic they belong to and the granger195
casuality results between bots’ and humans’ number of tweets/average sentiment, aggregated on a ﬁve-minute basis. Table S10196
and S11 shows the granger causality testing results for all bot thresholds ranging from 0.5 to 0.75.197
Sentiment Analysis.We classiﬁed all tweets’ sentiment and assigned them a sentiment score from−1 (most negative) to1198
(most positive) with the VADER package. Figure S6 and Figure S7 show the distribution of the sentiment scores of the bot199
exposed sample and their matching group.200
Fig. S6. Distribution (kernel density) of the sentiment scores of the bot exposed sample.
Fig. S7. Distribution (kernel density) of the sentiment scores of the matched users.
Linda Li, Orsolya Vásárhelyi and Balázs Vedres 11 of 31

Table S7. Information ﬂow between bots and humans for tweets belonging to each topic, during cascades identiﬁed only.
Topic with cascade Human RT human (%) Bot RT bot (%) Human RT bot (%) Bot RT human (%) Human total Bot total Human RT human sentiment Bot RT bot sentiment Human RT bot sentiment Bot RT human sentiment
Football game protest 2.46 9.62 87.11 0.81 18193 2118 -0.20 -0.38 -0.71 -0.13
Disruptive engagement 1.59 11.13 86.35 0.93 19326 2649 -0.21 -0.54 -0.72 -0.35
Anti XR protests sentiment 65.01 6.30 5.37 23.33 2492 1049 -0.64 0.02 -0.02 -0.66
Politicized activism 4.99 34.31 59.67 1.02 3096 1692 -0.12 -0.26 -0.34 -0.13
12 of 31 Linda Li, Orsolya Vásárhelyi and Balázs Vedres

Table S8. Cascades identiﬁed with burstiness score and granger causality results (F-test score) between the number of posts (5-min aggre-
gated total) by bots and humans.
Topic Cascade period Burstiness score (at peak) F-score (bot predict human) F-score (human predict bot) Time lag (n * 5mins)
Football game protests 11-24 00:00 - 11:24 04:00 3.79 2.27 * 3.97 *** 6
Disruptive engagement 11-23 19:00 - 11-23 20:00 4.88 15.60 *** 2.68 ** 7
Anti XR protests sentiment 11-29 21:00 - 11-30 04:00 6.39 2.77 ** 2.54 ** 6
Politicized activism 11-23 21:00 - 11-23 24:00 3.56 6.06 *** 1.50 7
Note: ∗p < 0.05;∗∗ p < 0.01;∗∗∗ p < 0.001
Linda Li, Orsolya Vásárhelyi and Balázs Vedres 13 of 31

Table S9. Cascades identiﬁed with burstiness score and granger causality results (F-test score) between sentiment of posts (5-min aggre-
gated mean) by bots and humans.
Topic Cascade period Burstiness score (at peak) F-score (bot predict human) F-score (human predict bot) Time lag (n * 5mins)
Football game protests 11-24 00:00 - 11:24 04:00 3.79 0.38 0.92 6
Disruptive engagement 11-23 19:00 - 11-23 20:00 4.88 2.17 * 1.91 7
Anti XR protests sentiment 11-29 21:00 - 11-30 04:00 6.39 3.96 *** 3.08 *** 6
Politicized activism 11-23 21:00 - 11-23 24:00 3.56 11.40 *** 2.24 * 7
Note: ∗p < 0.05;∗∗ p < 0.01;∗∗∗ p < 0.001
14 of 31 Linda Li, Orsolya Vásárhelyi and Balázs Vedres

Table S10. Cascades identiﬁed with burstiness score and granger causality results (F-test score) between tweeting frequency (5-min aggre-
gated total) by bots and humans, for CAP thresholds 0.5 to 0.75.
Topic Cascade period Burstiness score (at peak) Time lag (n * 5mins) F-score (bot predict human) F-score (human predict bot) CAP threshold
Football game protests 11-24 00:00 - 11:24 04:00 3.79 6 2.27 * 3.89 ** 0.5
1.59 3.53 *** 0.55
1.13 3.38 *** 0.6
1.01 2.73 ** 0.7
0.57 2.94 * 0.75
Disruptive
engagement
11-23 19:00 -
11-23 20:00 4.88 7 22.28 *** 5.18 *** 0.5
20.38 *** 3.64 *** 0.55
17.28 *** 3.05 ** 0.6
16.13 *** 1.22 0.7
23.39 *** 1.67 0.75
Anti XR protests
sentiment
11-29 21:00 -
11-30 04:00 6.39 6 2.75 ** 2.63 ** 0.5
3.27 *** 3.21 *** 0.55
2.52 ** 3.25 *** 0.6
1.99 3.87 *** 0.7
0.65 3.60 *** 0.75
Politicized activism 11-23 21:00 - 11-23 24:00 3.56 7 5.66 *** 1.57 0.5
6.64 *** 1.43 0.55
7.21 *** 1.46 0.6
5.19 *** 2.08 0.7
3.09 ** 1.53 0.75
Note: ∗p < 0.05;∗∗ p < 0.01;∗∗∗ p < 0.001
Linda Li, Orsolya Vásárhelyi and Balázs Vedres 15 of 31

Table S11. Cascades identiﬁed with burstiness score and granger causality results (F-test score) between tweet sentiments (5-min aggregated
mean) of posts by bots and humans, for CAP thresholds 0.5 to 0.75.
Topic Cascade period Burstiness score (at peak) Time lag (n * 5mins) F-score (bot predict human) F-score (human predict bot) CAP threshold
Football game protests 11-24 00:00 - 11:24 04:00 3.79 6 2.10 2.41 * 0.5
0.23 1.08 0.55
1.08 0.68 0.6
1.55 2.66 ** 0.7
0.99 3.53 *** 0.75
Disruptive
engagement
11-23 19:00 -
11-23 20:00 4.88 7 0.74 1.19 0.5
0.89 1.45 0.55
0.50 1.95 0.6
0.30 2.01 0.7
0.52 1.18 0.75
Anti XR protests
sentiment
11-29 21:00 -
11-30 04:00 6.39 6 2.20 * 2.12 0.5
4.89 *** 1.58 0.55
3.05 *** 1.42 0.6
3.01 *** 1.99 0.7
1.96 3.16 *** 0.75
Politicized activism 11-23 21:00 - 11-23 24:00 3.56 7 8.19 *** 2.97 ** 0.5
8.49 *** 3.21 *** 0.55
3.20 *** 2.71 ** 0.6
9.28 *** 3.05 * 0.7
5.49 *** 2.11 0.75
Note: ∗p < 0.05;∗∗ p < 0.01;∗∗∗ p < 0.001
16 of 31 Linda Li, Orsolya Vásárhelyi and Balázs Vedres

Model Tables201
Table S12. Negative Binomial DiD Model Predicting the Average Daily Tweet Count 30 days after interaction with bots
Dependent variable:
Amount
65 70 75 80 65 70
(1) (2) (3) (4) (5) (6)
Constant −0.056 −0.489∗∗ −0.188∗∗ 0.051 −0.066 0.266
p = 0.274 p = 0.002 p = 0.004 p = 0.756 p = 0.230 p = 0.180
Bot interaction (yes = 1) −0.414∗∗∗ −0.344∗∗∗ −0.608∗∗∗ −0.414∗∗∗ −0.567∗∗∗ −0.440∗∗∗
p = 0.000 p = 0.00000 p = 0.000 p = 0.000 p = 0.000 p = 0.00000
after (yes = 1) −0.090 −0.058 0.078 −0.053 −0.066 0.041
p = 0.215 p = 0.432 p = 0.395 p = 0.504 p = 0.395 p = 0.652
Bot interaction*after 0.333 ∗∗∗ 0.211∗ −0.126 0.046 0.059 −0.099
p = 0.0004 p = 0.028 p = 0.288 p = 0.656 p = 0.553 p = 0.409
Sentiment of interaction −0.134∗∗ −0.116∗ −0.077
p = 0.008 p = 0.031 p = 0.199
Number of retweet of interaction 0.002 ∗∗∗ 0.0004 0.001 ∗
p = 0.000 p = 0.149 p = 0.024
Number of likes of interaction 0.004 −0.023∗∗∗ −0.025∗∗∗
p = 0.353 p = 0.00001 p = 0.00001
Topic 1 (Football game protest) 0.480 ∗∗ 0.064 −0.351
p = 0.003 p = 0.715 p = 0.098
Topic 2 (COP25 protest) 0.432 ∗∗ −0.011 0.150
p = 0.007 p = 0.948 p = 0.461
Topic 3 (Anti-XR messages) 0.025 −1.406∗∗∗ −2.024∗∗∗
p = 0.883 p = 0.000 p = 0.000
Topic 4 (XR founder’s remark on holocaust) 0.728 ∗∗∗ 0.047 −0.952∗∗∗
p = 0.00001 p = 0.786 p = 0.00001
Topic 5 (Disruptive engagement) 0.441 ∗∗ 0.131 −0.227
p = 0.006 p = 0.432 p = 0.260
Topic 6 (Anti London XR protest messages) 0.141 −0.342∗ −0.521∗∗
p = 0.378 p = 0.042 p = 0.009
Topic 7 (Politicized activism) −0.398∗ −0.703∗∗∗ −0.755∗∗∗
p = 0.017 p = 0.00005 p = 0.0003
Burstiness −0.090∗∗∗ −0.240∗∗∗ −0.085∗∗
p = 0.001 p = 0.000 p = 0.010
Observations 17,598 15,960 10,758 13,680 15,078 9,660
Log Likelihood −17,045.970 −15,415.660 −9,297.998 −12,420.390 −13,693.760 −8,448.931
Akaike Inf. Crit. 34,099.940 30,861.310 18,604.000 24,870.790 27,395.530 16,927.860
Note: ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001
Linda Li, Orsolya Vásárhelyi and Balázs Vedres 17 of 31

Table S13. Linear DiD Model Predicting the Average Sentiment of Tweets 30 days after interaction with bots
Dependent variable:
Sentiment
65 70 75 80 65 70
(1) (2) (3) (4) (5) (6)
Constant −0.121∗∗∗ −0.160∗∗∗ −0.132∗∗∗ −0.145∗∗∗ −0.114∗∗∗ −0.131∗∗∗
p = 0.000 p = 0.000 p = 0.000 p = 0.000 p = 0.000 p = 0.00005
Bot interaction (yes = 1) 0.099 ∗∗∗ 0.069∗∗∗ 0.095∗∗∗ 0.059∗∗∗ 0.059∗∗∗ 0.021
p = 0.000 p = 0.000 p = 0.000 p = 0.00000 p = 0.00001 p = 0.106
After (yes = 1) 0.095 ∗∗∗ 0.089∗∗∗ 0.098∗∗∗ 0.093∗∗∗ 0.115∗∗∗ 0.116∗∗∗
p = 0.000 p = 0.000 p = 0.000 p = 0.000 p = 0.000 p = 0.000
Bot interaction*After −0.112∗∗∗ −0.102∗∗∗ −0.099∗∗∗ −0.090∗∗∗ −0.098∗∗∗ −0.091∗∗∗
p = 0.000 p = 0.000 p = 0.000 p = 0.000 p = 0.00000 p = 0.00000
Sentiment of interaction 0.031 ∗∗∗ 0.018∗ −0.002
p = 0.00003 p = 0.023 p = 0.814
Number of retweet of interaction 0.0001 ∗∗∗ 0.0001∗∗ 0.0003∗∗∗
p = 0.0003 p = 0.003 p = 0.00000
Number of likes of interaction −0.002∗∗∗ −0.002∗∗ −0.003∗∗∗
p = 0.001 p = 0.006 p = 0.00005
Topic 1 (Football game protest) 0.068 ∗∗ 0.001 −0.010
p = 0.005 p = 0.958 p = 0.777
Topic 2 (COP25 protest) 0.048 ∗ 0.030 −0.017
p = 0.042 p = 0.241 p = 0.614
Topic 3 (Anti-XR messages) 0.085 ∗∗∗ 0.046 0.064
p = 0.001 p = 0.089 p = 0.061
Topic 4 (XR founder’s remark on holocaust) 0.007 −0.026 −0.019
p = 0.770 p = 0.326 p = 0.571
Topic 5 (Disruptive engagement) −0.004 −0.016 0.003
p = 0.866 p = 0.532 p = 0.937
Topic 6 (Anti London XR protest messages) 0.056 ∗ 0.040 0.042
p = 0.017 p = 0.113 p = 0.195
Topic 7 (Politicized activism) 0.165 ∗∗∗ 0.157∗∗∗ 0.160∗∗∗
p = 0.000 p = 0.000 p = 0.00001
Burstiness 0.013 ∗∗∗ 0.011∗ 0.004
p = 0.001 p = 0.014 p = 0.378
Observations 17,598 15,960 15,078 13,680 10,758 9,660
R2 0.007 0.021 0.007 0.022 0.007 0.028
Adjusted R2 0.007 0.020 0.007 0.021 0.006 0.026
Note: ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001
18 of 31 Linda Li, Orsolya Vásárhelyi and Balázs Vedres

Table S14. Negative Binomial DiD Model Predicting the Average Daily Tweet Count 30 days after interaction with non astroturfers
Dependent variable:
Amount
65 65 70 70 75 75
Constant −0.544∗∗∗ 0.039 −0.784∗∗∗ −0.084 −0.710∗∗∗ 0.021
(0.030) (0.035) (0.036)
Bot interaction (yes = 1) −0.075 0.326 ∗∗∗ −0.039 0.254 ∗∗ −0.209∗ 0.078
(0.079) (0.082) (0.085) (0.088) (0.099) (0.099)
After (yes = 1) 0.084 0.092 0.204 ∗ 0.113 0.220 ∗ 0.054
(0.081) (0.085) (0.087) (0.089) (0.100) (0.099)
Bot interaction*After −0.062 −0.069 −0.367∗∗ −0.278∗ −0.325∗ −0.175
(0.111) (0.114) (0.121) (0.122) (0.139) (0.138)
(0.058) (0.233) (0.062) (0.218) (0.071) (0.218)
Sentiment of interaction −0.257∗∗∗ −0.478∗∗∗ −0.317∗∗∗
(0.062) (0.066) (0.074)
Number of retweet of interaction 0.0001 −0.0004 −0.001∗
(0.0004) (0.0004) (0.001)
Number of likes of interaction −0.021∗∗∗ −0.013∗∗ −0.016∗∗
(0.005) (0.005) (0.005)
Topic 1 (Football game protest) −0.615∗ −0.521∗ −0.987∗∗∗
(0.245) (0.239) (0.249)
Topic 2 (COP25 protest) −1.282∗∗∗ −1.179∗∗∗ −1.037∗∗∗
(0.242) (0.231) (0.234)
Topic 3 (Anti-XR messages) −0.774∗∗ −2.132∗∗∗ −1.961∗∗∗
(0.249) (0.262) (0.265)
Topic 4 (XR founder’s remark on holocaust) −0.090 −0.539∗ −0.628∗∗
(0.245) (0.234) (0.233)
Topic 5 (Disruptive engagement) −0.306 −0.200 0.062
(0.242) (0.227) (0.231)
Topic 6 (Anti London XR protest messages) −1.072∗∗∗ −0.900∗∗∗ −0.849∗∗∗
(0.242) (0.227) (0.228)
Topic 7 (Politicized activism ) −1.760∗∗∗ −1.416∗∗∗ −2.405∗∗∗
(0.254) (0.241) (0.277)
Burstiness 0.246 ∗∗∗ 0.145∗∗∗ 0.100∗∗
Observations 10,547 9,300 8,687 7,680 6,827 6,000
Log Likelihood −9,366.087 −8,135.180 −6,971.166 −6,080.994 −5,434.130 −4,792.660
Akaike Inf. Crit. 18,740.170 16,300.360 13,950.330 12,191.990 10,876.260 9,615.319
Note: ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001
Linda Li, Orsolya Vásárhelyi and Balázs Vedres 19 of 31

Table S15. Linear DiD Model Predicting the Average Sentiment of Tweets 30 days after interaction with spammer, fake follower or ﬁnancial
bots
Dependent variable:
Sentiment
65 65 70 70 75 75
Constant −0.101∗∗∗ −0.134∗∗ −0.113∗∗∗ −0.146∗∗∗ −0.097∗∗∗ −0.183∗∗∗
(0.009) (0.041) (0.010) (0.041) (0.011) (0.039)
Bot interaction (yes = 1) 0.093 ∗∗∗ 0.067∗∗∗ 0.078∗∗∗ 0.041∗∗ 0.041∗∗ 0.032∗
(0.012) (0.013) (0.014) (0.014) (0.015) (0.015)
After (yes = 1) 0.090 ∗∗∗ 0.082∗∗∗ 0.089∗∗∗ 0.084∗∗∗ 0.107∗∗∗ 0.110∗∗∗
(0.013) (0.013) (0.014) (0.014) (0.016) (0.015)
Bot interaction*After −0.118∗∗∗ −0.105∗∗∗ −0.094∗∗∗ −0.084∗∗∗ −0.082∗∗∗ −0.078∗∗∗
(0.018) (0.018) (0.019) (0.020) (0.022) (0.021)
Sentiment of interaction 0.077 ∗∗∗ 0.051∗∗∗ 0.070∗∗∗
(0.010) (0.011) (0.011)
Number of retweet of interaction 0.0003 ∗∗∗ 0.0003∗∗∗ 0.001∗∗∗
(0.0001) (0.0001) (0.0001)
Number of likes of interaction −0.001 −0.001 −0.004∗∗∗
(0.001) (0.001) (0.001)
Topic 1 (Football game protest) 0.085 ∗ 0.011 0.091 ∗
(0.043) (0.044) (0.043)
Topic 2 (COP25 protest) 0.047 0.064 0.023
(0.042) (0.042) (0.041)
Topic 3 (Anti-XR messages) 0.138 ∗∗ 0.175∗∗∗ 0.299∗∗∗
(0.043) (0.044) (0.043)
Topic 4 (XR founder’s remark on holocaust) −0.123∗∗ −0.158∗∗∗ −0.125∗∗
(0.043) (0.043) (0.041)
Topic 5 (Disruptive engagement) 0.007 0.029 0.099 ∗
(0.042) (0.042) (0.041)
Topic 6 (Anti London XR protest messages) −0.007 0.014 0.014
(0.042) (0.042) (0.040)
Topic 7 (Politicized activism ) 0.154 ∗∗∗ 0.200∗∗∗ 0.320∗∗∗
(0.043) (0.043) (0.042)
Burstiness −0.010∗ −0.019∗∗ −0.021∗∗∗
(0.005) (0.006) (0.006)
Observations 10,547 9,300 8,687 7,680 6,827 6,000
R2 0.007 0.044 0.006 0.057 0.007 0.128
Adjusted R2 0.006 0.042 0.005 0.055 0.007 0.126
Note: ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001
20 of 31 Linda Li, Orsolya Vásárhelyi and Balázs Vedres

Table S16. Negative Binomial DiD Model Predicting the Average Daily Tweet Count 30 days after interaction with astroturfer bots
Dependent variable:
Amount
65 65 70 70 75 75
Constant 0.626 ∗∗∗ −0.436∗ 0.735∗∗∗ −0.211 0.744 ∗∗∗ 0.441
(0.098) (0.194) (0.100) (0.239) (0.138) (0.360)
Bot interaction (yes = 1) −0.953∗∗∗ −0.617∗∗∗ −1.209∗∗∗ −0.718∗∗∗ −1.412∗∗∗ −0.943∗∗∗
(0.117) (0.112) (0.118) (0.119) (0.158) (0.159)
After (yes = 1) −0.254 −0.234 −0.247 −0.243 −0.072 −0.209
(0.140) (0.131) (0.142) (0.141) (0.195) (0.188)
Bot interaction*After 0.651 ∗∗∗ 0.455∗∗ 0.339∗ 0.393∗ 0.076 0.159
(0.165) (0.156) (0.168) (0.167) (0.224) (0.214)
Sentiment of interaction 0.237 ∗∗ 0.262∗∗ 0.319∗∗∗
(0.081) (0.089) (0.096)
Number of retweet of interaction −0.0002 −0.0002 0.001
(0.0004) (0.0004) (0.0005)
Number of likes of interaction 0.133 ∗∗∗ 0.167∗∗∗ 0.097∗∗
(0.012) (0.024) (0.032)
Topic 1 (Football game protest) 0.185 0.041 −0.213
(0.195) (0.238) (0.350)
Topic 2 (COP25 protest) 1.087 ∗∗∗ 0.947∗∗∗ 1.023∗∗
(0.209) (0.245) (0.352)
Topic 3 (Anti-XR messages) −0.590∗∗ −1.172∗∗∗ −2.618∗∗∗
(0.212) (0.251) (0.373)
Topic 4 (XR founder’s remark on holocaust) 0.414 ∗ 0.122 −1.280∗∗∗
(0.202) (0.236) (0.354)
Topic 5 (Disruptive engagement) 0.399 ∗ 0.355 −1.206∗∗∗
(0.194) (0.234) (0.340)
Topic 6 (Anti London XR protest messages) 0.480 ∗ 0.416 0.272
(0.211) (0.249) (0.346)
Topic 7 (Politicized activism ) 0.212 0.114 0.164
(0.206) (0.241) (0.340)
Burstiness −0.657∗∗∗ −0.644∗∗∗ −0.208∗∗∗
(0.047) (0.049) (0.056)
Observations 7,051 6,660 6,391 6,000 3,931 3,660
Log Likelihood −7,524.297 −6,852.443 −6,532.538 −5,988.802 −3,761.728 −3,346.734
Akaike Inf. Crit. 15,056.590 13,734.890 13,073.080 12,007.600 7,531.455 6,723.467
Note: ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001
Linda Li, Orsolya Vásárhelyi and Balázs Vedres 21 of 31

Table S17. Linear DiD Model Predicting the Average Sentiment of Tweets 30 days after interaction with astroturfer bots
Dependent variable:
Sentiment
65 65 70 70 75 75
Constant −0.170∗∗∗ −0.171∗∗∗ −0.178∗∗∗ −0.121∗∗∗ −0.182∗∗∗ 0.188∗∗
(0.014) (0.028) (0.015) (0.034) (0.022) (0.058)
Bot interaction (yes = 1) 0.133 ∗∗∗ 0.097∗∗∗ 0.139∗∗∗ 0.107∗∗∗ 0.126∗∗∗ 0.017
(0.016) (0.016) (0.017) (0.017) (0.024) (0.025)
After (yes = 1) 0.109 ∗∗∗ 0.105∗∗∗ 0.120∗∗∗ 0.115∗∗∗ 0.147∗∗∗ 0.139∗∗∗
(0.019) (0.019) (0.021) (0.021) (0.031) (0.030)
Bot interaction*After −0.113∗∗∗ −0.107∗∗∗ −0.116∗∗∗ −0.109∗∗∗ −0.140∗∗∗ −0.122∗∗∗
(0.023) (0.023) (0.024) (0.024) (0.034) (0.034)
Sentiment of interaction −0.0004 0.035 ∗∗ 0.0003
(0.012) (0.013) (0.015)
Number of retweet of interaction 0.0001 0.0001 −0.0003∗∗∗
(0.0001) (0.0001) (0.0001)
Number of likes of interaction −0.004∗ −0.021∗∗∗ 0.005
(0.002) (0.004) (0.005)
Topic 1 (Football game protest) 0.030 −0.013 −0.382∗∗∗
(0.028) (0.034) (0.057)
Topic 2 (COP25 protest) −0.065∗ −0.089∗ −0.403∗∗∗
(0.030) (0.035) (0.058)
Topic 3 (Anti-XR messages) 0.001 −0.090∗∗ −0.478∗∗∗
(0.030) (0.034) (0.055)
Topic 4 (XR founder’s remark on holocaust) 0.100 ∗∗∗ 0.086∗∗ −0.156∗∗
(0.029) (0.033) (0.056)
Topic 5 (Disruptive engagement) −0.061∗ −0.116∗∗∗ −0.396∗∗∗
(0.028) (0.033) (0.054)
Topic 6 (Anti London XR protest messages) 0.150 ∗∗∗ 0.098∗∗ −0.084
(0.031) (0.035) (0.056)
Topic 7 (Politicized activism ) 0.109 ∗∗∗ 0.061 −0.257∗∗∗
(0.030) (0.034) (0.055)
Burstiness 0.051 ∗∗∗ 0.047∗∗∗ 0.036∗∗∗
(0.006) (0.006) (0.008)
Observations 7,051 6,660 6,391 6,000 3,931 3,660
R2 0.011 0.047 0.012 0.055 0.009 0.103
Adjusted R2 0.010 0.045 0.012 0.053 0.008 0.100
Note: ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001
22 of 31 Linda Li, Orsolya Vásárhelyi and Balázs Vedres

Table S18. Negative Binomial DiD Model Predicting the Average Daily Tweet Count 30 days after interaction for users who Support, Neutral
or Against XR, botometer CAP=.65
Dependent variable:
Amount
Pro Pro Neutral Neutral Con Con
(1) (2) (3) (4) (5) (6)
Constant 0.248 ∗∗∗ −0.822∗∗ −2.338∗∗∗ −3.156∗∗∗ −1.373∗∗∗ 0.330
(0.056) (0.258) (0.196) (0.578) (0.154) (0.256)
Bot interaction (yes = 1) −0.561∗∗∗ −0.675∗∗∗ 0.995∗∗∗ 0.693∗∗ 0.985∗∗∗ 1.907∗∗∗
(0.077) (0.084) (0.230) (0.231) (0.171) (0.187)
After (yes = 1) −0.086 −0.012 0.182 0.033 −0.342 −0.452∗
(0.079) (0.080) (0.271) (0.266) (0.226) (0.214)
Bot interaction*after 0.494 ∗∗∗ 0.255∗ 0.397 0.263 −0.031 0.168
(0.108) (0.111) (0.318) (0.310) (0.249) (0.234)
Sentiment of interaction −0.412∗∗∗ −0.794∗∗∗ 0.352∗∗
(0.057) (0.172) (0.125)
Opinion of user interaction 0.242 ∗∗∗ 0.439∗ 0.831∗∗∗
(0.060) (0.195) (0.125)
Number of retweet of interaction 0.003 ∗∗∗ 0.0004 −0.0003
(0.0003) (0.001) (0.0003)
Number of likes of interaction −0.015∗∗∗ 0.089∗∗ 0.0005
(0.005) (0.030) (0.015)
Bot score (astroturf) 0.279 ∗∗∗ 0.049 −0.176∗∗∗
(0.027) (0.068) (0.044)
Topic 1 (Football game protest) 0.018 0.606 −0.910∗∗∗
(0.257) (0.546) (0.233)
Topic 2 (COP25 protest) 0.854 ∗∗∗ 0.662 −2.258∗∗∗
(0.257) (0.514) (0.255)
Topic 3 (Anti-XR messages) −0.285 1.560 ∗∗ −3.164∗∗∗
(0.267) (0.504) (0.387)
Topic 4 (XR founder’s remark on holocaust) 0.930 ∗∗∗ −0.440 −1.899∗∗∗
(0.257) (0.541) (0.256)
Topic 5 (Disruptive engagement) 0.584 ∗ 0.927 −2.792∗∗∗
(0.252) (0.534) (0.264)
Topic 6 (Anti London XR protest messages) 0.245 −0.926 −2.504∗∗∗
(0.253) (0.613) (0.279)
Topic 7 (Politicized activism ) −0.435 0.708 −3.410∗∗∗
(0.259) (0.556) (0.296)
Burstiness 0.060 0.177 ∗ −0.059
(0.031) (0.076) (0.078)
Observations 10,398 9,420 3,240 2,880 3,960 3,660
Log Likelihood −11,905.070 −10,472.790 −1,654.172 −1,520.042 −3,138.700 −2,779.994
Akaike Inf. Crit. 23,818.150 20,979.580 3,316.344 3,074.083 6,285.401 5,593.989
Note: ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001
Linda Li, Orsolya Vásárhelyi and Balázs Vedres 23 of 31

Table S19. Linear DiD Model Predicting the Average Sentiment of Tweets 30 days after interaction for users who Support, Neutral or Against
XR, botometer CAP=.65
Dependent variable:
Sentiment
Pro Pro Neutral Neutral Con Con
(1) (2) (3) (4) (5) (6)
Constant −0.142∗∗∗ −0.032 −0.041∗ −0.032 −0.108∗∗∗ 0.064
(0.009) (0.065) (0.019) (0.065) (0.021) (0.041)
Bot interaction (yes = 1) 0.148 ∗∗∗ −0.007 −0.003 −0.007 0.050 ∗ 0.051∗
(0.012) (0.024) (0.023) (0.024) (0.023) (0.024)
After (yes = 1) 0.082 ∗∗∗ 0.287∗∗∗ 0.267∗∗∗ 0.287∗∗∗ −0.054 −0.054∗
(0.013) (0.027) (0.026) (0.027) (0.029) (0.026)
Bot interaction*after −0.110∗∗∗ −0.248∗∗∗ −0.236∗∗∗ −0.248∗∗∗ 0.027 0.036
(0.017) (0.033) (0.033) (0.033) (0.033) (0.030)
Sentiment of interaction −0.102∗∗∗ −0.102∗∗∗ 0.285∗∗∗
(0.020) (0.020) (0.018)
Opinion of user interaction 0.157 ∗∗∗ 0.157∗∗∗ −0.042∗
(0.019) (0.019) (0.020)
Number of retweet of interaction −0.0004∗∗∗ −0.0004∗∗∗ −0.0001
(0.0001) (0.0001) (0.0001)
Number of likes of interaction −0.012∗∗∗ −0.012∗∗∗ −0.014∗∗∗
(0.003) (0.003) (0.002)
Bot score (astroturf) −0.053∗∗∗ −0.053∗∗∗ −0.020∗∗
(0.008) (0.008) (0.007)
Topic 1 (Football game protest) 0.037 0.037 −0.025
(0.062) (0.062) (0.037)
Topic 2 (COP25 protest) 0.137 ∗ 0.137∗ −0.097∗
(0.058) (0.058) (0.038)
Topic 3 (Anti-XR messages) 0.135 ∗ 0.135∗ −0.064
(0.057) (0.057) (0.048)
Topic 4 (XR founder’s remark on holocaust) 0.142 ∗ 0.142∗ −0.157∗∗∗
(0.059) (0.059) (0.038)
Topic 5 (Disruptive engagement) 0.041 0.041 −0.255∗∗∗
(0.060) (0.060) (0.037)
Topic 6 (Anti London XR protest messages) 0.229 ∗∗∗ 0.229∗∗∗ −0.286∗∗∗
(0.062) (0.062) (0.041)
Topic 7 (Politicized activism ) 0.271 ∗∗∗ 0.271∗∗∗ 0.013
(0.062) (0.062) (0.041)
Burstiness 0.013 0.013 0.012
(0.009) (0.009) (0.011)
Observations 10,398 2,880 3,240 2,880 3,960 3,660
R2 0.016 0.142 0.048 0.142 0.005 0.115
Adjusted R2 0.015 0.137 0.047 0.137 0.005 0.111
Note: ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001
24 of 31 Linda Li, Orsolya Vásárhelyi and Balázs Vedres

Table S20. Negative Binomial DiD Model Predicting the Average Daily Tweet Count 30 days after interaction for users who Support, Neutral
or Against XR, botometer CAP=.70
Dependent variable:
Amount
Pro Pro Neutral Neutral Con Con
(1) (2) (3) (4) (5) (6)
Constant 0.219 ∗∗∗ −3.511∗∗∗ −2.303∗∗∗ −3.511∗∗∗ −1.455∗∗∗ −0.203
(0.060) (0.531) (0.197) (0.531) (0.170) (0.264)
Bot interaction (yes = 1) −0.644∗∗∗ 0.944∗∗∗ 0.588∗ 0.944∗∗∗ 0.856∗∗∗ 1.326∗∗∗
(0.083) (0.234) (0.231) (0.234) (0.185) (0.206)
After (yes = 1) −0.065 0.120 0.236 0.120 −0.241 −0.407
(0.085) (0.259) (0.271) (0.259) (0.247) (0.233)
Bot interaction*After 0.190 −0.290 −0.274 −0.290 −0.067 0.156
(0.118) (0.309) (0.320) (0.309) (0.269) (0.252)
Sentiment of interaction −1.324∗∗∗ −1.324∗∗∗ 0.031
(0.205) (0.205) (0.130)
Opinion of user interaction 0.121 0.121 0.323 ∗
(0.230) (0.230) (0.126)
Number of retweet of interaction 0.0004 0.0004 −0.0001
(0.001) (0.001) (0.0004)
Number of likes of interaction 0.0001 0.0001 0.021
(0.034) (0.034) (0.015)
Bot score (astroturf) 0.200 ∗∗ 0.200∗∗ 0.014
(0.075) (0.075) (0.045)
Topic 1 (Football game protest) 0.651 0.651 −0.585∗
(0.510) (0.510) (0.259)
Topic 2 (COP25 protest) 0.416 0.416 −1.896∗∗∗
(0.447) (0.447) (0.286)
Topic 3 (Anti-XR messages) 0.584 0.584 −2.312∗∗∗
(0.455) (0.455) (0.393)
Topic 4 (XR founder’s remark on holocaust) −0.503 −0.503 −2.762∗∗∗
(0.483) (0.483) (0.294)
Topic 5 (Disruptive engagement) 1.274 ∗∗ 1.274∗∗ −2.482∗∗∗
(0.473) (0.473) (0.285)
Topic 6 (Anti London XR protest messages) −0.747 −0.747 −2.283∗∗∗
(0.592) (0.592) (0.305)
Topic 7 (Politicized activism ) 0.857 0.857 −2.820∗∗∗
(0.506) (0.506) (0.312)
Burstiness 0.019 0.019 −0.087
(0.085) (0.085) (0.082)
Observations 8,778 2,460 2,700 2,460 3,600 3,300
Log Likelihood −9,543.139 −1,040.597 −1,134.655 −1,040.597 −2,713.683 −2,364.884
Akaike Inf. Crit. 19,094.280 2,115.195 2,277.310 2,115.195 5,435.366 4,763.769
Note: ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001
Linda Li, Orsolya Vásárhelyi and Balázs Vedres 25 of 31

Table S21. Linear DiD Model Predicting the Average Sentiment of Tweets 30 days after interaction for users who Support, Neutral or Against
XR, botometer CAP=.70
Dependent variable:
Sentiment
Pro Pro Neutral Neutral Con Con
(1) (2) (3) (4) (5) (6)
Constant −0.147∗∗∗ 0.028 −0.063∗∗ 0.028 −0.134∗∗∗ 0.063
(0.010) (0.068) (0.021) (0.068) (0.023) (0.046)
Bot interaction (yes = 1) 0.141 ∗∗∗ 0.010 0.004 0.010 0.061 ∗ 0.044
(0.013) (0.027) (0.026) (0.027) (0.026) (0.028)
After (yes = 1) 0.075 ∗∗∗ 0.328∗∗∗ 0.306∗∗∗ 0.328∗∗∗ −0.031 −0.031
(0.014) (0.029) (0.030) (0.029) (0.033) (0.030)
Bot interaction*After −0.077∗∗∗ −0.279∗∗∗ −0.267∗∗∗ −0.279∗∗∗ 0.009 0.020
(0.018) (0.036) (0.036) (0.036) (0.037) (0.034)
Sentiment of interaction −0.081∗∗∗ −0.081∗∗∗ 0.267∗∗∗
(0.024) (0.024) (0.020)
Opinion of user interaction 0.155 ∗∗∗ 0.155∗∗∗ −0.044∗
(0.021) (0.021) (0.021)
Number of retweet of interaction −0.0004∗∗∗ −0.0004∗∗∗ −0.0001∗
(0.0001) (0.0001) (0.0001)
Number of likes of interaction −0.020∗∗∗ −0.020∗∗∗ −0.011∗∗∗
(0.003) (0.003) (0.002)
Bot score (astroturf) −0.073∗∗∗ −0.073∗∗∗ −0.013
(0.010) (0.010) (0.007)
Topic 1 (Football game protest) 0.151 ∗ 0.151∗ −0.080
(0.066) (0.066) (0.045)
Topic 2 (COP25 protest) 0.133 ∗ 0.133∗ −0.133∗∗
(0.060) (0.060) (0.047)
Topic 3 (Anti-XR messages) 0.077 0.077 −0.172∗∗
(0.060) (0.060) (0.056)
Topic 4 (XR founder’s remark on holocaust) 0.137 ∗ 0.137∗ −0.197∗∗∗
(0.060) (0.060) (0.045)
Topic 5 (Disruptive engagement) 0.018 0.018 −0.271∗∗∗
(0.062) (0.062) (0.045)
Topic 6 (Anti London XR protest messages) 0.210 ∗∗ 0.210∗∗ −0.307∗∗∗
(0.064) (0.064) (0.049)
Topic 7 (Politicized activism ) 0.210 ∗∗ 0.210∗∗ −0.009
(0.066) (0.066) (0.048)
Burstiness 0.007 0.007 0.038 ∗∗
(0.010) (0.010) (0.013)
Observations 8,778 2,460 2,700 2,460 3,600 3,300
R2 0.017 0.169 0.057 0.169 0.004 0.098
Adjusted R2 0.017 0.164 0.056 0.164 0.004 0.094
Note: ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001
26 of 31 Linda Li, Orsolya Vásárhelyi and Balázs Vedres

Table S22. Negative Binomial DiD Model Predicting the Average Daily Tweet Count 30 days after interaction for users who Support, Neutral
or Against XR, botometer CAP=.75
Dependent variable:
Amount
Pro Pro Neutral Neutral Con Con
(1) (2) (3) (4) (5) (6)
Constant 0.060 −3.378∗∗∗ −2.568∗∗∗ −3.378∗∗∗ −1.415∗∗∗ 0.334
(0.069) (0.482) (0.282) (0.482) (0.206) (0.297)
Bot interaction (yes = 1) −0.487∗∗∗ 0.716∗ 0.758∗ 0.716∗ 0.306 1.256 ∗∗∗
(0.097) (0.319) (0.324) (0.319) (0.223) (0.279)
After (yes = 1) 0.082 0.084 0.197 0.084 −0.061 −0.153
(0.097) (0.365) (0.388) (0.365) (0.294) (0.292)
Bot interaction*After −0.097 −0.486 −0.294 −0.486 −0.055 −0.020
(0.138) (0.427) (0.451) (0.427) (0.317) (0.311)
Sentiment of interaction −1.588∗∗∗ −1.588∗∗∗ 0.710∗∗∗
(0.297) (0.297) (0.171)
Opinion of user interaction 0.518 0.518 0.017
(0.266) (0.266) (0.183)
Number of retweet of interaction −0.004 −0.004 −0.001∗
(0.002) (0.002) (0.0004)
Number of likes of interaction −0.013 −0.013 0.003
(0.039) (0.039) (0.017)
Bot score (astroturf) 0.252 ∗ 0.252∗ 0.104
(0.102) (0.102) (0.054)
Topic 1 (Football game protest) −1.866∗∗∗
(0.325)
Topic 2 (COP25 protest) 0.354 0.354 −2.300∗∗∗
(0.446) (0.446) (0.345)
Topic 3 (Anti-XR messages) 0.886 ∗ 0.886∗ −3.175∗∗∗
(0.421) (0.421) (0.411)
Topic 4 (XR founder’s remark on holocaust) −0.637 −0.637 −3.689∗∗∗
(0.492) (0.492) (0.363)
Topic 5 (Disruptive engagement) 1.694 ∗∗∗ 1.694∗∗∗ −3.877∗∗∗
(0.451) (0.451) (0.365)
Topic 6 (Anti London XR protest messages) −0.329 −0.329 −3.233∗∗∗
(0.519) (0.519) (0.386)
Topic 7 (Politicized activism ) 0.668 0.668 −3.562∗∗∗
(0.521) (0.521) (0.368)
Burstiness 0.167 0.167 −0.014
(0.116) (0.116) (0.104)
Observations 6,198 1,680 1,920 1,680 2,640 2,340
Log Likelihood −6,622.960 −617.740 −699.774 −617.740 −1,740.707 −1,450.346
Akaike Inf. Crit. 13,253.920 1,267.480 1,407.548 1,267.480 3,489.414 2,934.692
Note: ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001
Linda Li, Orsolya Vásárhelyi and Balázs Vedres 27 of 31

Table S23. Linear DiD Model Predicting the Average Sentiment of Tweets 30 days after interaction for users who Support, Neutral or Against
XR, botometer CAP=.75
Dependent variable:
Sentiment
Pro Pro Neutral Neutral Con Con
(1) (2) (3) (4) (5) (6)
Constant −0.133∗∗∗ −0.204∗∗∗ 0.010 −0.204∗∗∗ −0.162∗∗∗ 0.234∗∗∗
(0.011) (0.052) (0.026) (0.052) (0.031) (0.061)
Bot interaction (yes = 1) 0.098 ∗∗∗ −0.002 −0.073∗ −0.002 0.081 ∗ 0.063
(0.015) (0.030) (0.031) (0.030) (0.034) (0.036)
After (yes = 1) 0.076 ∗∗∗ 0.356∗∗∗ 0.320∗∗∗ 0.356∗∗∗ 0.099∗ 0.099∗
(0.016) (0.033) (0.036) (0.033) (0.044) (0.039)
Bot interaction*After −0.040 −0.320∗∗∗ −0.297∗∗∗ −0.320∗∗∗ −0.114∗ −0.099∗
(0.022) (0.041) (0.044) (0.041) (0.048) (0.043)
Sentiment of interaction −0.388∗∗∗ −0.388∗∗∗ 0.273∗∗∗
(0.031) (0.031) (0.026)
Opinion of user interaction 0.276 ∗∗∗ 0.276∗∗∗ −0.130∗∗∗
(0.022) (0.022) (0.030)
Number of retweet of interaction 0.001 ∗∗ 0.001∗∗ −0.0003∗∗∗
(0.0002) (0.0002) (0.0001)
Number of likes of interaction −0.033∗∗∗ −0.033∗∗∗ −0.012∗∗∗
(0.004) (0.004) (0.003)
Bot score (astroturf) −0.016 −0.016 −0.031∗∗∗
(0.011) (0.011) (0.008)
Topic 1 (Football game protest) −0.291∗∗∗
(0.063)
Topic 2 (COP25 protest) 0.013 0.013 −0.367∗∗∗
(0.050) (0.050) (0.065)
Topic 3 (Anti-XR messages) 0.351 ∗∗∗ 0.351∗∗∗ −0.412∗∗∗
(0.048) (0.048) (0.069)
Topic 4 (XR founder’s remark on holocaust) 0.152 ∗∗ 0.152∗∗ −0.355∗∗∗
(0.047) (0.047) (0.063)
Topic 5 (Disruptive engagement) 0.315 ∗∗∗ 0.315∗∗∗ −0.456∗∗∗
(0.051) (0.051) (0.065)
Topic 6 (Anti London XR protest messages) 0.479 ∗∗∗ 0.479∗∗∗ −0.527∗∗∗
(0.049) (0.049) (0.068)
Topic 7 (Politicized activism ) 0.546 ∗∗∗ 0.546∗∗∗ −0.159∗
(0.054) (0.054) (0.064)
Burstiness −0.018 −0.018 0.085 ∗∗∗
(0.011) (0.011) (0.017)
Observations 6,198 1,680 1,920 1,680 2,640 2,340
R2 0.013 0.307 0.087 0.307 0.002 0.122
Adjusted R2 0.012 0.300 0.086 0.300 0.001 0.116
Note: ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001
28 of 31 Linda Li, Orsolya Vásárhelyi and Balázs Vedres

Table S24. Linear DiD Model Predicting the Change in Support 30 days after interaction for users who Support, Neutral or Against XR, with
varied botometer CAP scores, without controls
Dependent variable:
Opinion Change
Pro Neutral Con Pro Neutral Con Pro Neutral Con
Constant 0.172 ∗∗∗ 0.105∗∗∗ −0.520∗∗∗ 0.204∗∗∗ 0.133∗∗∗ −0.583∗∗∗ 0.204∗∗∗ 0.133∗∗∗ −0.857∗∗∗
(0.009) (0.014) (0.026) (0.010) (0.016) (0.029) (0.010) (0.016) (0.037)
Bot interaction (yes = 1) −0.008 −0.220∗∗∗ 0.195∗∗∗ −0.051∗∗∗ −0.217∗∗∗ 0.265∗∗∗ −0.051∗∗∗ −0.217∗∗∗ 0.525∗∗∗
(0.012) (0.018) (0.030) (0.013) (0.020) (0.032) (0.013) (0.020) (0.041)
After (yes = 1) −0.001 −0.000 −0.000 −0.001 0.000 −0.000 −0.001 0.000 −0.000
(0.013) (0.020) (0.037) (0.014) (0.023) (0.040) (0.014) (0.023) (0.053)
Bot interaction*After −0.003 0.000 0.000 −0.004 −0.000 0.000 −0.004 −0.000 0.000
(0.017) (0.025) (0.042) (0.019) (0.028) (0.045) (0.019) (0.028) (0.058)
CAP 65 70 75 65 70 75 65 70 75
Observations 10,398 3,240 3,960 8,778 2,700 3,600 8,778 2,700 2,640
R2 0.0001 0.086 0.021 0.004 0.082 0.037 0.004 0.082 0.112
Adjusted R2 −0.0002 0.085 0.021 0.003 0.081 0.036 0.003 0.081 0.111
Note: ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001
Linda Li, Orsolya Vásárhelyi and Balázs Vedres 29 of 31

Table S25. Linear DiD Model Predicting the Change in Support 30 days after interaction for users who Support, Neutral or Against XR, with
varied botometer CAP scores, with controls
Dependent variable:
Opinion Change
Pro Neutral Con Pro Neutral Con Pro Neutral Con
Constant 0.819 ∗∗∗ −0.793∗∗∗ −0.133∗∗ 0.868∗∗∗ −0.798∗∗∗ −0.061 0.868 ∗∗∗ −0.798∗∗∗ −0.031
(0.040) (0.048) (0.051) (0.041) (0.042) (0.056) (0.041) (0.042) (0.068)
Bot interaction (yes = 1) 0.070 ∗∗∗ −0.214∗∗∗ 0.389∗∗∗ 0.026 −0.106∗∗∗ 0.490∗∗∗ 0.026 −0.106∗∗∗ 0.705∗∗∗
(0.013) (0.018) (0.030) (0.014) (0.016) (0.034) (0.014) (0.016) (0.039)
After (yes = 1) −0.000 0.000 −0.000 0.000 −0.000 0.000 0.000 −0.000 −0.000
(0.013) (0.020) (0.033) (0.014) (0.018) (0.036) (0.014) (0.018) (0.043)
Bot interaction*After 0.000 0.000 0.000 0.000 0.000 −0.000 0.000 0.000 0.000
(0.017) (0.024) (0.038) (0.019) (0.022) (0.041) (0.019) (0.022) (0.048)
Sentiment of interaction −0.044∗∗∗ −0.081∗∗∗ −0.328∗∗∗ −0.040∗∗∗ −0.136∗∗∗ −0.214∗∗∗ −0.040∗∗∗ −0.136∗∗∗ −0.067∗
(0.009) (0.015) (0.022) (0.010) (0.015) (0.024) (0.010) (0.015) (0.028)
Opinion of user interaction −0.027∗∗ −0.073∗∗∗ 0.243∗∗∗ −0.027∗∗ 0.022 0.243 ∗∗∗ −0.027∗∗ 0.022 −0.250∗∗∗
(0.009) (0.014) (0.025) (0.010) (0.013) (0.026) (0.010) (0.013) (0.033)
Num. of retweet of interaction −0.0003∗∗∗ 0.00003 −0.001∗∗∗ −0.0004∗∗∗ 0.0004∗∗∗ −0.001∗∗∗ −0.0004∗∗∗ 0.0004∗∗∗ −0.001∗∗∗
(0.0001) (0.0001) (0.0001) (0.0001) (0.0001) (0.0001) (0.0001) (0.0001) (0.0001)
Num. of likes of interaction 0.008 ∗∗∗ 0.020∗∗∗ 0.037∗∗∗ 0.007∗∗∗ 0.026∗∗∗ 0.030∗∗∗ 0.007∗∗∗ 0.026∗∗∗ 0.019∗∗∗
(0.001) (0.002) (0.003) (0.001) (0.002) (0.003) (0.001) (0.002) (0.003)
Bot score (astroturf) −0.090∗∗∗ −0.003 0.012 −0.099∗∗∗ −0.052∗∗∗ −0.023∗∗ −0.099∗∗∗ −0.052∗∗∗ −0.027∗∗
(0.004) (0.006) (0.008) (0.005) (0.006) (0.009) (0.005) (0.006) (0.009)
Topic 1 (Football game protest) −0.614∗∗∗ 1.078∗∗∗ −0.385∗∗∗ −0.537∗∗∗ 1.396∗∗∗ −0.417∗∗∗ −0.537∗∗∗ 1.396∗∗∗ −0.662∗∗∗
(0.040) (0.046) (0.046) (0.042) (0.041) (0.054) (0.042) (0.041) (0.070)
Topic 2 (COP25 protest) −0.518∗∗∗ 0.723∗∗∗ −0.503∗∗∗ −0.540∗∗∗ 0.836∗∗∗ −0.572∗∗∗ −0.540∗∗∗ 0.836∗∗∗ −1.076∗∗∗
(0.040) (0.043) (0.047) (0.041) (0.036) (0.057) (0.041) (0.036) (0.072)
Topic 3 (Anti-XR messages) −0.292∗∗∗ 0.868∗∗∗ −0.602∗∗∗ −0.188∗∗∗ 0.872∗∗∗ −0.748∗∗∗ −0.188∗∗∗ 0.872∗∗∗ −0.921∗∗∗
(0.041) (0.043) (0.059) (0.042) (0.037) (0.067) (0.042) (0.037) (0.076)
Topic 4 (XR founder’s remark on holocaust) −0.562∗∗∗ 0.928∗∗∗ −0.646∗∗∗ −0.552∗∗∗ 0.852∗∗∗ −0.592∗∗∗ −0.552∗∗∗ 0.852∗∗∗ −0.988∗∗∗
(0.040) (0.044) (0.047) (0.041) (0.037) (0.055) (0.041) (0.037) (0.069)
Topic 5 (Disruptive engagement) −0.415∗∗∗ 0.887∗∗∗ −0.665∗∗∗ −0.418∗∗∗ 0.934∗∗∗ −0.745∗∗∗ −0.418∗∗∗ 0.934∗∗∗ −1.368∗∗∗
(0.039) (0.045) (0.046) (0.040) (0.038) (0.055) (0.040) (0.038) (0.071)
Topic 6 (Anti London XR protest messages) −0.540∗∗∗ 0.803∗∗∗ −0.504∗∗∗ −0.539∗∗∗ 0.860∗∗∗ −0.583∗∗∗ −0.539∗∗∗ 0.860∗∗∗ −1.180∗∗∗
(0.039) (0.046) (0.050) (0.040) (0.039) (0.059) (0.040) (0.039) (0.075)
Topic 7 (Politicized activism ) −0.451∗∗∗ 0.978∗∗∗ −0.621∗∗∗ −0.464∗∗∗ 0.986∗∗∗ −0.675∗∗∗ −0.464∗∗∗ 0.986∗∗∗ −0.787∗∗∗
(0.040) (0.046) (0.050) (0.040) (0.040) (0.058) (0.040) (0.040) (0.070)
Burstiness 0.005 0.025 ∗∗∗ −0.014 0.009 0.094 ∗∗∗ −0.135∗∗∗ 0.009 0.094 ∗∗∗ −0.213∗∗∗
(0.005) (0.006) (0.013) (0.005) (0.006) (0.015) (0.005) (0.006) (0.019)
CAP 65 70 75 65 70 75 65 70 75
Observations 9,420 2,880 3,660 7,920 2,460 3,300 7,920 2,460 2,340
R2 0.118 0.348 0.238 0.132 0.537 0.229 0.132 0.537 0.420
Adjusted R2 0.117 0.344 0.234 0.130 0.534 0.225 0.130 0.534 0.416
Note: ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001
30 of 31 Linda Li, Orsolya Vásárhelyi and Balázs Vedres

References202
1. K Yang, E Ferrara, F Menczer, Botometer 101: Social bot practicum for computational social scientists. CoRR203
abs/2201.01608 (2022).204
2. A Rauchﬂeisch, J Kaiser, The false positive problem of automatic bot detection in social science research.PLOS ONE 15,205
1–20 (2020).206
3. F Martini, P Samula, TR Keller, U Klinger, Bot, or not? Comparing three methods for detecting social bots in ﬁve207
political discourses. Big Data & Soc. 8, 205395172110335 (2021).208
4. S González-Bailón, M De Domenico, Bots are less central than veriﬁed accounts during contentious political events.Proc.209
Natl. Acad. Sci. United States Am. 118 (2021).210
5. S Feng, H Wan, N Wang, J Li, M Luo, Twibot-20: A comprehensive twitter bot detection benchmark inProceedings of211
the 30th ACM International Conference on Information & Knowledge Management. pp. 4485–4494 (2021).212
6. S Feng, et al., TwiBot-22: Towards Graph-Based Twitter Bot Detection.Adv. Neural Inf. Process. Syst. pp. 1–25 (2022).213
7. M Abadi, et al., TensorFlow: Large-scale machine learning on heterogeneous systems (2015) Software available from214
tensorﬂow.org.215
8. F Chollet, , et al., Keras (https://keras.io) (2015).216
9. KC Yang, O Varol, PM Hui, F Menczer, Scalable and Generalizable Social Bot Detection through Data Selection.Proc.217
AAAI Conf. on Artif. Intell. 34, 1096–1103 (2020).218
10. HR Greve, H Rao, P Vicinanza, EY Zhou, Online Conspiracy Groups: Micro-Bloggers, Bots, and Coronavirus Conspiracy219
Talk on Twitter.Am. Sociol. Rev. (2022).220
11. X Yan, J Guo, Y Lan, X Cheng, 2013-a Bitem Topic Model for Short Texts.Pdf.Www pp. 1445–1455 (2013).221
12. L Shi, G Cheng, SR Xie, G Xie, A word embedding topic model for topic detection and summary in social networks.Meas.222
Control. (United Kingdom)52, 1289–1298 (2019).223
13. S Bird, E Klein, E Loper,Natural language processing with Python: analyzing text with the natural language toolkit. ("224
O’Reilly Media, Inc."), (2009).225
14. M Röder, A Both, A Hinneburg, Exploring the space of topic coherence measures inProceedings of the Eighth ACM226
International Conference on Web Search and Data Mining, WSDM ’15. (Association for Computing Machinery, New York,227
NY, USA), p. 399–408 (2015).228
15. Harvard and Yale students disrupt football game for fossil fuel protest | US universities (2019).229
16. B News, COP25: Thousands gather for change climate protests in Madrid — bbc.co.uk (https://www.bbc.co.uk/news/230
world-europe-50694361) (year?) [Accessed 07-09-2023].231
17. D Gayle, Extinction Rebellion bee protester glues himself to Lib Dem bus — theguardian.com (https://www.theguardian.232
com/environment/2019/dec/04/extinction-rebellion-protester-glues-himself-lib-dem-battlebus ) (year?) [Accessed 07-09-2023].233
Linda Li, Orsolya Vásárhelyi and Balázs Vedres 31 of 31
