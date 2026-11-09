---
title: Understanding Emotional Disclosure via Diary-keeping in Quarantine on Social Media
url: https://arxiv.org/abs/2401.07230
category: social-media
subcategory: empirical
date: 2024-01
venue: ''
authors:
- Yue Deng
- Changyang He
- Bo Li
source: arxiv
pdf_url: https://arxiv.org/pdf/2401.07230
pages: 13
chars: 81823
fetched_at: '2026-11-08T13:11:03+00:00'
kb_version: 1
---

# Understanding Emotional Disclosure via Diary-keeping in Quarantine on Social Media

Understanding Emotional Disclosure via Diary-keeping in
Quarantine on Social Media
Yue Deng
Department of Computer Science and
Engineering, Hong Kong University
of Science and Technology
Hong Kong SAR, China
ydengbi@connect.ust.hk
Changyang He
Department of Computer Science and
Engineering, Hong Kong University
of Science and Technology
Hong Kong SAR, China
cheai@cse.ust.hk
Bo Li
Department of Computer Science and
Engineering, Hong Kong University
of Science and Technology
Hong Kong SAR, China
bli@cse.ust.hk
ABSTRACT
Quarantine is a widely-adopted measure during health crises caused
by highly-contagious diseases like COVID-19, yet it poses critical
challenges to public mental health. Given this context, emotional
disclosure on social media in the form of keeping a diary emerges
as a popular way for individuals to express emotions and record
their mental health status. However, the exploration of emotional
disclosure via diary-keeping on social media during quarantine
is underexplored, understanding which could be beneficial to fa-
cilitate emotional connections and enlighten health intervention
measures. Focusing on this particular form of self-disclosure, this
work proposes a quantitative approach to figure out the prevalence
and changing patterns of emotional disclosure during quarantine,
and the possible factors contributing to the negative emotions. We
collected 58, 796 posts with the "Quarantine Diary" keyword on
Weibo, a popular social media website in China. Through text clas-
sification, we capture diverse emotion categories that characterize
public emotion disclosure during quarantine, such as annoyed, anx-
ious, boring, happy, hopeful and appreciative. Based on temporal
analysis, we uncover the changing patterns of emotional disclosure
from long-term perspectives and period-based perspectives (e.g.,
the gradual decline of all negative emotions and the upsurge of the
annoyed emotion near the end of quarantine). Leveraging topic
modeling, we also encapsulate the possible influencing factors of
negative emotions, such as freedom restriction and solitude, and
uncertainty of infection and supply. We reflect on how our findings
could deepen the understanding of mental health on social media
and further provide practical and design implications to mitigate
mental health issues during quarantine.
CCS CONCEPTS
• Human-centered computing→ Empirical studies in HCI .
KEYWORDS
emotional disclosure, quarantine, mental health, social media, diary-
keeping
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
CHCHI 2023, November 13–16, 2023, Denpasar, Bali, Indonesia
© 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 979-8-4007-1645-4/23/11. . . $15.00
https://doi.org/10.1145/3629606.3629623
ACM Reference Format:
Yue Deng, Changyang He, and Bo Li. 2023. Understanding Emotional Dis-
closure via Diary-keeping in Quarantine on Social Media. In Chinese CHI
2023 (CHCHI 2023), November 13–16, 2023, Denpasar, Bali, Indonesia. ACM,
New York, NY, USA, 13 pages. https://doi.org/10.1145/3629606.3629623
1 INTRODUCTION
The detrimental effects on mental health caused by the COVID-19
pandemic are rampant [42, 52, 62], although it has been a long time
since its first outbreak in December 2019 [74]. In light of the virus
transmission mechanism and the unprecedented sphere of influ-
ence, quarantine, a direct and effective social distancing strategy, is
adopted by most governments around the world [73]. However, an
emerging body of research warns of the exacerbated threat of vig-
orous confinement for the public’s mental health under quarantine,
like depression [12], suicide [48], and post-traumatic stress disor-
der (PTSD) [36]. Understanding mental health challenges during
quarantine is warranted for further research to propose supporting
technologies and improve intervention measures that could help
the public obtain psychological balance.
Owing to the forced reduction in physical interaction by social
distancing measures, social media has become a hub where people
gather to share information and establish emotional connections
[2, 60]. Keeping diaries in quarantine on social media emerges as a
popular channel for citizens to share daily lives, express opinions,
and vent emotions, which is a large-scale resource for understand-
ing the mental health of individuals in quarantine. These diaries
typically adhere to a specific format, recording quarantine life along
with the keyword "Quarantine Diary" and the number of days in
quarantine, an example of which is shown in Figure 1. Unlike tradi-
tional surveys, diary-keeping on social media have distinct features:
(1) proactivity. The majority of diaries are spontaneous instead of
deliberately organized, featuring fragmented and piecemeal content
[57]. These unintentional recordings of everyday life facilitate a
natural understanding of people’s mental health. (2) richness. The
demographic diversity on social media helps to cover different types
of quarantine (e.g., home quarantine and centralized quarantine),
and the measurement of mental health is not limited to psychologi-
cal measurement scales [16]. (3) timeliness. Timely psychological
states can be reflected to help take preventive actions on mental
health. Arguably, the unique characteristics of social media make
it possible to comprehensively investigate the context of mental
health during quarantine.
Emotion disclosure on social media is a prevalent expression
of mental well-being [ 33, 45, 61, 66]. A rich stream of previous
arXiv:2401.07230v1  [cs.HC]  14 Jan 2024

CHCHI 2023, November 13–16, 2023, Denpasar, Bali, Indonesia Deng, et al.
work has convincingly demonstrated that various emotions during
the epidemic undergo changes over time [ 1, 30, 35]. Unpacking
the dynamics of emotional disclosure can shed light on significant
implications for tracking public emotional wellness and detecting
signs of distress, thereby supporting health interventions and rele-
vant policy-making. Nevertheless, previous research has primarily
focused on the overall emotional patterns throughout the entire
epidemic (e.g., several months or years) [6, 69] rather than quar-
antine, or within a specific duration of quarantine (e.g., a 14-day
quarantine study) [52]. There is still a lack of comprehensive un-
derstanding regarding how the public discloses nuanced emotions
during quarantine on social media, and how these subtle emotion
dimensions change over time and vary between different quaran-
tine durations (e.g., 7-day quarantine or 14-day quarantine). Besides,
the factors potentially influencing public mental well-being, par-
ticularly those contributing to distress, are also less investigated.
Understanding these questions provides valuable insights for devel-
oping precise health intervention measures and informing future
potential isolation situations. In this setting, the practice of con-
tinuously recording life and updating emotional status through
quarantine diaries with "Quarantine Diary" keyword and the num-
ber of days in quarantine manifests unique values in providing
temporal information of changing patterns of emotional disclosure.
Figure 1: Example of a quarantine diary. Individuals sponta-
neously label the post with the hashtag #Quarantine Diary#
and the Day No., and describe the contents of the diary ( "[Nu-
cleic acid test] Since I received the call in the morning, I have
been looking forward to picking us up from 18:00 to 22:30. The
days of centralized quarantine are finally over. I can’t drink
milk but I am very healthy. I put on protective clothing, like
stealing adult clothes. Then I carry my big suitcase, get on
the bus arranged by the community, and continue the home
quarantine [location]").
To this end, this paper explores how the public discloses emotions
through diary keeping on social media during quarantine. First,
identifying nuanced categories of disclosed emotions is meaningful
to track public mental well-being, especially capturing potential
mental health problems in quarantine. Second, given changeable
emotions in quarantine, unveiling the changing patterns of emo-
tional disclosure from the perspectives of an overall trend and
multiple quarantine durations is of great importance. Third, when
negative emotions have a stronger influence on behaviors and cog-
nition of people (i.e., negativity bias theory [1]), deriving insight
into what possible factors devoting negative emotional disclosure is
warranted. As such, the following research questions are proposed:
• RQ1: What are the categories of emotional disclosure on
social media in quarantine?
• RQ2: What are the changing patterns of emotional disclosure
through diary-keeping on social media from the perspectives
of the long-term trend and various durations of quarantine?
• RQ3: What factors might contribute to negative emotional
disclosure on social media in quarantine?
To answer these questions, we collected 58, 796 posts from Weibo,
one of the largest social media platforms, with the "Quarantine Di-
ary" keyword from April 29, 2020 to July 25, 2022, and performed
a quantitative study. Through an open coding approach and text
classifiers (RQ1), we identify six categories of emotions during
quarantine (i.e., annoyed, anxious, boring, appreciative, hopeful and
happy). By extracting temporal information with regular expression
matching and statistical analysis (RQ2), we discover that posts with
negative emotions occupy almost half of all posts where annoyed
was the predominant category. We further unpack the changing
patterns of emotional disclosure such as the gradual decrease of
negative emotions and the upsurge of annoyed emotion near the
end of quarantine. Through a topic modeling technique (RQ3), we
reveal that the latent factors might account for negative emotions,
such as freedom restriction and unsatisfied infrastructure for an-
noyed, and uncertainty of infection and influences by management
measures for anxious. The findings shed light on health interven-
tion measures and design implications to effectively relieve mental
health problems during quarantine.
This work enriches the mental health venue in HCI community
mainly by: (1) exploring prevalent emotional categories during
quarantine; (2) uncovering the changing patterns of emotional dis-
closure from both long-term and period-based views; (3) discovering
the possible factors might contributing to negative emotions; (4)
proposing design implications to facilitate emotional tracking dur-
ing quarantine; (5) substantiating the feasibility and importance of
performing emotion analysis in the field of affective computing by
a bottom-up approach that focuses on identifying context-specific
emotions, rather than relying on generic sentiment analysis tools.
Our study reveals emotional features and provides insights into the
future direction for specific health intervention measures.
2 RELATED WORK
2.1 The Role of Social Media in Unveiling
Mental Health During Quarantine
Quarantine, as a restriction on the movement of people, is intended
to prevent the spread of disease. To contain COVID-19, unprece-
dented quarantine strategies are operated and dynamically adjusted
corresponding to the pandemic development. With the epidemic
panic, the confinement policy tends to exacerbate mental health
problems [9, 52]. In this vein, social media platforms have become
popular sites for individuals to express their opinions, describe
their lives and interact with social networks, thus mapping individ-
uals’ responses and behaviors to their psychological traits [4, 43].

Emotional Disclosure via Diary-keeping in Quarantine CHCHI 2023, November 13–16, 2023, Denpasar, Bali, Indonesia
Owing to the prevalence of social media, researchers have paid
great attention to how social media help disclose mental health,
like discovering the shifts of suicidal ideation [27], understanding
the virtual attributes of mental health [53] and proposing Mental
Well-being Index drawing on social media [7]. Compared with tra-
ditional methods in mental health (e.g., questionnaires and scales),
social media could naturally, expediently, and timely collect emo-
tional and behavioral information, becoming a promising place for
recognizing psychological effects [1, 50]. Although social media ex-
pressions cannot guarantee the identical emotional intensity or ab-
solute authenticity of feelings with privacy or sensitivity concerns
[10], they showcase users’ thoughts, emotions, and experiences to
some extent.
Hence, this work explores mental well-being during quarantine
by comprehensively understanding the characteristics of emotional
disclosure via social media (RQ1), changing patterns of emotional
disclosure (RQ2) and specific concerns of the public which provide
guidelines to mitigate mental health disorders (RQ3).
2.2 Emotional Disclosure on Social Media in
Quarantine
Social media has become a widely used channel to express emotions
[26, 27, 38, 45]. A burgeoning body of research investigated how
emotions were disclosed with the extensive use of social media
during quarantine. One strand of work focused on emotional differ-
ences between various groups of individuals [73, 79]. For example,
Zhu et al. revealed the anxiety difference between six types of quar-
antine (e.g., forced quarantine at home and centralized quarantine)
[79]. Another stream of research centered on the changes of emo-
tions where interesting changing patterns usually hide [17, 30, 50].
For example, Cao et al. uncovered emotional evolution during each
phase of Wuhan lockdown including the incubation phase, explo-
sive phase, declining phase and stable phase [17].
In previous research the measurement of emotions was mostly
based on existing API [43, 48], psychological scale [16], or only from
the perspective of words and themes [5] rather than scenario-based
analysis. However, emotions are comprehensive manifestations of
not only words but also contexts. Furthermore, the majority of
previous studies about emotion categories were theory-driven, e.g.,
drawing on Plutchik’s model with basic emotions [1] or LIWC with
various emotional dimensions [6] to determine emotion categories.
The specific emotions expressed by individuals in quarantine,
utilizing a bottom-up approach to emotion categorization, remain
yet to be established. Thereby, this study contributes to this area by
employing an inductive approach to investigate common emotions
that align closely with the context of quarantine.
2.3 Online Diaries on Social Media in
Quarantine
An online diary, also known as a web diary, is defined as a personal
journal or diary that individuals choose to publish on the World
Wide Web 1. The United States witnessed the emergence of the
earliest online diaries around 1994 [11]. In China, the rise of online
diary-writing began in 2000 when Lu Youqing’s cancer battle diary
1https://en.wikipedia.org/wiki/Online_diary
was serialized on a popular online literature website, attracting a
significant number of followers [40]. The introduction of blogs to
China in 2002 further popularized online diary-writing, making it
widely recognized. Thus, online diaries have a significant and exten-
sive history, serving as a common form for people to document their
daily lives. During the lockdown in Wuhan, residents turned to so-
cial media like WeChat and Weibo, and started writing and sharing
their experiences via "Lockdown Diaries", providing a glimpse into
life in a sealed city [57]. The diaries attracted scholarly attention,
with studies focusing on various aspects such as feminist issues [8],
and the impact of the pandemic on daily life and work. They were
part of a global trend, with pandemic diaries appearing worldwide,
offering access to wider audiences and facilitating interaction [58].
However, this online exposure also brought unwanted attention and
censorship. Previous studies primarily focused on Wuhan, includ-
ing lockdown diaries in Wuhan or nationwide quarantine diaries
during the outbreak period in Wuhan [30]. Nevertheless, this diary
form exists nationwide, and the quarantine measures have been in
place for an extended period of time.
In general, diaries that convey emotional disclosure across the
country during the extended period of quarantine remain unex-
plored. This research gathers nationwide data spanning approx-
imately 2 years to uncover the changing patterns of emotional
disclosure as quarantine becomes a new normal, as well as to iden-
tify potential factors associated with negative emotions.
3 METHOD
We adopted a quantitative study to comprehensively understand
emotional disclosure during quarantine. More specifically, we first
described the process of data selection and collection (Section 3.1)
to contextualize our scenario. Then we applied inductive coding
and text classifiers to comprehend the emotions during quarantine
(RQ1, Section 3.2), utilized regex-matching-based statistical analysis
to unveil the changing process of emotions (RQ2, Section 3.3), and
leveraged topic modeling to unpack the possible related factors
affecting negative emotions (RQ3, Section 3.4). Figure 2 exhibits the
overall flowchart.
3.1 Data Selection and Collection
Weibo, one of the largest microblogging websites in China similar
to Twitter, has become a dominant site for understanding the well-
being and health trends of the public due to its characteristics of
sharing, disseminating and receiving instant information [19, 37,
47]. Weibo was a significant and popular channel for recording
daily life and expressing feelings during quarantine, where posts
with hashtag "#Quarantine Diary#" had owned more than 1.2 billion
reads and more than 0.5 million discussions (including original
posts and retweets) 2.
To obtain a preliminary understanding of the emotional status in
quarantine, we kept track of posts related to quarantine on Weibo
in advance. We found users applied some strategies to identify
topic-related posts including hashtags, Super Topic (i.e., communi-
ties consisting of people having common interests and following
2https://m.s.weibo.com/vtopic/detail_new?click_from=searchpc&q=%23%E9%9A%
94%E7%A6%BB%E6%97%A5%E8%AE%B0%23

CHCHI 2023, November 13–16, 2023, Denpasar, Bali, Indonesia Deng, et al.
58, 796 Posts with the
“Quarantine Diary”
Keyword
31, 714
Emotional Posts
Model 1: Relevant Posts Filter
    Model 2: Emotional Posts Filter
13, 679
Posts with Negative
Emotions
RQ1: Situation of
Emotion Disclosure
RQ2: Changing Patterns of
Emotion Disclosure
15, 256
Posts with Temporal
Information
RQ3: Latent Factors Contributing
to Negative Emotions
Model 3:
 Emotion Type Classifier
annoyed
anxious
boring
happy
 hopeful
appre-ciative
Long-term Changing Patterns
Period-based Changing Patterns
21-day Global
Changing Patterns
7-day and 14-day
Grouped Changing Patterns
Priority-based
Regular Expression Matching
Freedom Restriction
and Solitude
Uncertainty of Infection
Uncertainty of Influences by
Management Measures
…
LDA
Selection
Statistical Analysis
Statistical Analysis
…
Inductive Coding
Figure 2: The overall flow chart to understand the emotional disclosure during quarantine.
specific topics [75]) and keywords. In order to make the data com-
prehensive, we selected the keyword-based collection approach
rather than other approaches based on hashtags or Super Topic.
Moreover, the most straightforward keyword was " Quarantine",
but posts with "Quarantine" were miscellaneous containing official
quarantine policies, suggestions after quarantine or even advertise-
ments of primers (i.e., cosmetics). Compared with "Quarantine", we
noticed that posts with the " Quarantine Diary " keyword, where
users tended to record and share their activities and emotions for
one day or several days, getting closer to the personal quarantine
lives and self-expression. Hence, we chose "Quarantine Diary" as the
keyword, so as to make the collected data align with our scenario.
We collected the data with the assistance of the WeiboSuperSpi-
der tool [77] ranging from April 29, 2020, to July 25, 2022. Since we
only considered the quarantine in China, we removed the overseas
posts (i.e., the quarantine locations are not in China) by identifying
the keyword "Overseas Quarantine" and the locations of posts in
self-identified profiles.
In total, 58, 796 original posts were retrieved with the keyword
"Quarantine Diary" from 34, 677 distinct users.
3.2 RQ1: Understanding Emotional Disclosure
Categories
This section described how we constructed two filtering models
for obtaining emotional posts and one classification model for emo-
tional categories, to understand the categories of emotional disclo-
sure in quarantine.
3.2.1 Filtering. Although we had chosen a suitable keyword, it was
inevitable that the data might contain a substantial amount of noise.
After manually analyzing a random set of 200 posts (saturation was
achieved after coding 80-100 posts), we found the majority of such
noisy posts could be divided into two types: (1) irrelevant to the
scenario (e.g., posts published by quarantine volunteers and fans
caring about their superstars in quarantine, and official blogs or
news); (2) relevant but emotionless such as posts with mild and
neutral attitudes (e.g., "take things as they come"), and those without
obvious emotions (e.g., "In the morning, I had a COVID-19 test, took
the blood pressure and did my homework. ").
To remove these noisy data, we constructed two deep-learning-
based models. Model 1 (relevant posts filter) was a text classifier
determining whether posts were related to the quarantine con-
text and Model 2 (emotional posts filter) decided whether posts
expressed emotions. To prepare the training data, two authors first
manually coded a random sample of 200 posts independently. Co-
hen’s Kappa, a statistical measure for evaluating agreement between
raters in qualitative items, is favored over percent agreement due to
its consideration of chance agreement likelihood [54]. A significant
level of agreement was achieved between the two raters (Model
1: Cohen’s Kappa: 0.89; Model 2: Cohen’s Kappa: 0.90). Following
their discussion, the two coders successfully reached a consensus
on annotations. Then, each annotator separately coded another
400 posts, reaching a total of 1, 000 training samples for Model 1
and 781 training samples for Model 2, since some posts might be
irrelevant among the 1, 000 samples. Based on the training datasets,
we tried traditional machine-learning-based methods (SVM [24]and
XGBoost [18]) and deep-learning-based methods (GRU [21], LSTM
[39], and BERT [28]) to build our filters. In order to prevent over-
fitting due to the limited labeled data, we utilized Adam as an
optimizer and set the parameter of the Dropout layer as 0.2 during
the training of deep learning models. BERT was fine-tuned based
on BERT-wwm whose corpus was Chinese Wikipedia [25]. Finally,
BERT achieved the best performance for both Model 1 (F1 score:

Emotional Disclosure via Diary-keeping in Quarantine CHCHI 2023, November 13–16, 2023, Denpasar, Bali, Indonesia
95.4%) and Model 2 (F1 score: 88.1%). The two models were applied
to filter all posts, so the remaining posts were probably emotional.
3.2.2 Emotion Category Identification and Classification. In order
to investigate common emotions that align closely with the context
of quarantine and considering the limited effectiveness of existing
sentiment analysis models, we manually constructed a codebook
of emotional categories by corpus annotation, and developed a
multi-class text classifier to quantify posts with various emotions
specifically related to the "Quarantine Diary" keyword.
We first employed an open coding approach [ 32] to identify
the common emotions in quarantine. By taking this inductive ap-
proach, we allowed the codes to emerge naturally from the analysis.
Specifically, two authors conducted manual coding of 200 randomly
selected posts independently (saturation was achieved after cod-
ing about 100 posts) and generated initial codes from a nuanced
perspective (e.g., "joy", "extremely happy", "worried"). Subsequently,
several rounds of meetings, comparisons, and discussions were
held to merge the initial codes, and finally generated a codebook
with high-level emotional categories (e.g., "happy" and "anxious").
Through the data-driven inductive coding, there were six categories
of emotions where annoyed, anxious and boring reflected the neg-
ative emotional disclosure, and appreciative, hopeful and happy
captured the positive emotion characteristics, shown in Table 1.
To provide a quantitative description of emotional posts and pre-
pare for subsequent analysis, it was necessary to determine which
emotion was specifically expressed in each post. The open cod-
ing revealed that the majority of posts contained a single emotion,
with only a very small number exhibiting mixed emotions, often
with one primary emotion. With this understanding, we developed
Model 3, a single-label emotion classifier to identify the emotion
categories within these potentially emotional posts. The annotation
process of the training dataset is similar to Model 1 and Model 2,
and the annotation data is the 1, 000 unfiltered training samples in
Model 1 (Model 3: Cohen’s Kappa: 0.79). Coding unfiltered samples
could simultaneously validate the manual annotation accuracy for
two previous models. To enhance the classification performance,
one of the authors manually coded an additional 1, 500 samples,
resulting in a total of 1, 237 training samples. Due to the outstand-
ing performance of BERT in Section 3.2.1, we also selected BERT as
our classifier. We fine-tuned BERT with RoBERTa-wwm-ext-large
[25] based on the complexity of multi-class classification (F1 score:
66.13%, with the similar level of performance to other works in mul-
ticlass classification of emotions on social media [ 13, 29, 65, 78]).
Then, we applied the classification model to 31, 714 potentially
emotional posts.
3.3 RQ2: Investigating the Changing Patterns of
Emotional Disclosure
In this section, we described how we identified the temporal in-
formation in posts and investigated temporal characteristics from
long-term and period-based views.
Data utilized for this section was 31, 714 emotional posts. After
browsing these emotional posts, we found the temporal informa-
tion of posts would be expressed in three ways as follows: (1) "Day"
or "D" plus a number (e.g., "Day 9" or "D 9"); (2) using an ordinal
number (e.g., "the first day "); (3) "Quarantine Diary" plus a number
(e.g., "Quarantine Diary 9 "). Moreover, there was multiple tempo-
ral information in some posts containing two or three types of
temporal information or utilizing one type of temporal informa-
tion more than once. To circumvent this challenge, we adopted
a priority-based regular expression matching approach to extract
the temporal information for each post. The priority was the same
as the order mentioned above. If there was more than one tempo-
ral number in one type, we selected the maximum number as the
temporal information. Note that the priority order and the maxi-
mum temporal approach were determined based on the accuracy
of temporal information after manual coding. After the extraction
operation, there existed 15, 256 posts with temporal information.
To comprehensively explore how emotional status changed dur-
ing quarantine, we considered it from two views: (1) long-term
changing patterns, the temporal characteristics of emotions from
April 2020 to July 2022 to have an overall exploration of emotional
disclosure; (2) period-based changing patterns, the temporal charac-
teristics of emotions related to quarantine durations to further un-
derstand the day-by-day emotions, including 21-day global chang-
ing patterns (i.e., based on posts whose temporal information was
within 21 days, e.g., " Quarantine Diary 6 "), as well as 7-day and
14-day grouped changing patterns (i.e., based on users whose quar-
antine duration were 7 days or 14 days). Note that 7 days and 14 days
were two typical quarantine periods adopted by the government
in China [23] and recommended by WHO [59]. We used propor-
tions instead of numbers to capture changing patterns of emotional
disclosure. By doing so, it allows us to effectively unveil relative
distribution changes among emotional categories, considering the
varying number of posts collected at different points in time.
3.4 RQ3: Exploring Possible Factors
Contributing to Negative Emotions
The negativity bias theory [1] indicates that negative emotions play
a more significant role in the public’s behaviors and cognition. In
the context of quarantine, annoyed and anxious generally exhibit
a stronger expression of personal concerns and potentially have
more direct impacts on emotional well-being, relationships, and
life quality, while boring typically represents a mundane account
of daily life. Hence, in this section, we described how we explored
factors that might lead to annoyed and anxious.
3.4.1 Topic Model Building. To keep track of what individuals
disclose about their quarantine lives, we conducted a topic modeling
technique to characterize the topics of post contents. Specifically,
we adopted Latent Dirichlet Allocation (LDA) [14], a type of classic
and useful unsupervised topic extraction model, to explore potential
and abstract topics in a large number of posts where each topic
was composed of a set of frequent keywords. LDA was a widely-
adopted approach for understanding social media data by prior
work [44, 49, 64]. The first exploratory attempt of LDA suggested
that there still remained a lot of meaningless or irrelevant keywords
in each topic (e.g., 像是-seem, 感觉-feel, 我会-I will). To make
keywords more amenable and reliable for analysis, we applied
a two-iteration LDA framework that updated stopwords during
the process. LDA was applied to 11, 525 annoyed posts and 2, 154
anxious posts, respectively. The details were as below:

CHCHI 2023, November 13–16, 2023, Denpasar, Bali, Indonesia Deng, et al.
Discovering context stopwords (iteration 1):
• Preprocessing: First we implemented a noise removal op-
eration to delete URLs and punctuations, and convert tradi-
tional characters. Jieba, a widely used tokenization tool, was
applied to segment Chinese texts [70]. We chose the HIT Chi-
nese stopwords table as the basic stopwords set [34]. Then
we also further filtered words by taking into account part
of speech and frequency of words. In particular, we only re-
tained nouns and verbs after tokenization which could show
clearer and more explicit meanings and help authors to infer
the topics. Moreover, we removed extreme low-frequency
words (i.e., words whose frequency was smaller than 5) and
extreme high-frequency words (i.e., occurrence proportion
was more than 0.5). Words with extremely high frequency
suggested that they might lack representativeness. We also
built bigrams to represent two frequently co-occurring words
(e.g., 核酸_检测-nucleic acid test).
• Hyperparameter tuning: The most significant parameter
in LDA was the number of topics k. We chose k based on the
coherence score 𝐶𝑣, a widely-adopted coherence metric [67].
Consequently, we set the parameter space between 2 and
15. With a systematic grid search of the range, the optimal
value of k was 6 and 12 forannoyed and anxious, respectively.
Then, we applied k-topic LDA and output 50 keywords for
each topic.
• Stopwords updating: In our specific context, we included
words that lacked clear and evident implications for human
interpretation into the basic stopwords set. Additionally, we
combined the high-frequency keywords, which appeared in
more than one-third of all topics, with the basic set.
Unveiling topic clusters (iteration 2): We added the context
stopwords into the basic stopwords set and other steps of prepro-
cessing and hyperparameter tuning remained unchanged. The opti-
mal numbers of topics k were 15 and 14 for annoyed and anxious,
respectively, and then we ran LDA again.
3.4.2 Interpretation of Topics with Thematic Analyasis. The results
of LDA were sets of representative keywords for topics. We tried to
figure out discussion themes for annoyed and anxious posts. There-
fore, we applied an inductive thematic analysis [ 15] to annotate
each topic based on the understanding of posts and human interpre-
tation. Specifically, two authors, who had experienced quarantine
themselves and comprehended the scenario, individually distributed
theme labels to topics and generated initial labels based on these
sets of keywords and original posts. Through several rounds of
comparison and discussion, they merged some topics describing
similar themes, deleted those containing miscellaneous information,
and inductively concluded final topical themes.
4 FINDINGS
In this section, we reported the findings on the categories of emo-
tional disclosure in quarantine. In Section 4.1, we unveiled the
willingness of people to express various emotions on social media
during quarantine. In Section 4.2, we described how emotional sta-
tus changed from the long-term and period-based perspectives to
probe into the changing patterns. In Section 4.3, we discovered the
latent factors that might give rise to negative emotions. The find-
ings elucidated mental health challenges of quarantine (RQ1), the
evolutionary process of emotional disclosure (RQ2) and potential
influencing factors corresponding to negative affections (RQ3).
4.1 RQ1: Emotional Disclosure Categories
The statistical results of emotional disclosure during quarantine
were demonstrated in Figure 3. Based on the results of three models
constructed in Section 3.2, we concluded the following findings: (1)
Most posts (79.57%, N=46, 785) containing the "Quarantine Diary"
keyword tallied with our research context shown in Figure 3 (a),
proving that this type of data collection approach was feasible; (2)
Emotional posts were predominant (67.78%, N=31, 714) compared
with emotionless ones indicated in Figure 3 (b), which demonstrated
that people in quarantine were willing to express their emotions
on social media; In Figure 3 (c), (3) Posts with negative emotions
(45.77%, N=14, 516) in quarantine occupied almost the half of all
emotional posts; (4) Annoyed (36.34%, N=11, 525) was the dominant
category in amount compared with anxious (6.79%, N=2, 154) and
boring (2.64%, N=837); (5) In terms of positive emotions, happy
(35.96%, N=11, 405), hopeful (13.42%, N=4, 256) and appreciative
(4.85%, N=1, 537) were sorted in descending order.
4.2 RQ2: Changing Patterns of Emotional
Disclosure
We focused on how emotional disclosure changes during quarantine
from long-term and period-based perspectives. More specifically,
we first unveiled the changing patterns from April 2020 to July 2022
to have an overall exploration of emotions in this context, and then
investigated those related to quarantine durations, which further
understood the day-by-day emotions during quarantine.
4.2.1 Long-term Changing Patterns. Figure 4 delineated the long-
term changing patterns. Several general trends could be discovered:
(1) The overall increase in the proportion of annoyed indicated a
growing trend of individuals expressing and emphasizing their an-
noyance over other emotions; (2) All emotion proportions gradually
stabilized on the whole, probably due to the stability of the quaran-
tine policy and the spread of the vaccine, which brought support to
the public emotions; (3) Appreciative and boring proportions were
very stable in the whole process.
4.2.2 Period-based Changing Patterns. Except for the temporal
characteristics from a long-term perspective, changing patterns in
different durations of quarantine were also noteworthy. In particu-
lar, we focused on the 21-day global changing patterns based on
posts whose labels of quarantine day were within 21 days, prompt-
ing a comprehensive understanding of temporal characteristics as
quarantine time went by. Then we uncovered 7-day and 14-day
grouped changing patterns based on users whose quarantine du-
rations were 7 days or 14 days, to unearth the similarities and
differences of emotions in different quarantine durations.
21-day global changing patterns: To begin with, we statisti-
cally illustrated the trend of post number as the increase of quaran-
tine duration. Based on Figure 5 (a), we noticed that the post number
after the 21st day was less than 100, not enough to implement a

Emotional Disclosure via Diary-keeping in Quarantine CHCHI 2023, November 13–16, 2023, Denpasar, Bali, Indonesia
Table 1: The codebook of emotional categories with the "Quarantine Diary" keyword.
Polarity Category Description Example
Negative
annoyed a feeling of irritation and anger. It also
includes complaining and feeling im-
prisoned.
There is a time limit even in jail.
When can we get out?
anxious a feeling of uneasiness and worry. Be-
ing nervous about health, food and sit-
uation.
My roommate has a fever and
sometimes coughs. I don’t know
when I can get a second test. I’m
really scared.
boring a feeling of no interest and tediousness.
Being numb, tired or negatively describ-
ing trivia.
I feel like I’m in a cycle every day.
Positive
appreciative a feeling of gratitude or pleasure. It in-
cludes gratitude to servers, the govern-
ment and families.
I received vegetables and eggs
from the government. Thanks to
our country and the staff.
hopeful a feeling of optimism about the future.
It contains being hopeful about them-
selves and the epidemic.
Only one day left! come on!
happy a feeling of pleasure or contentment.
It also includes being relaxed and posi-
tively describing daily life.
I am happy today. I drank a cup
of milk tea, and the egg-fried rice
tasted good.
!"#$!%
&'#()%
'
'#*
'#&
'#)
'#(
'#$
'#+
'#!
'#,
'#"
-./.0123 4--./.0123
!"#$% &'()*$&+$,*'*-"./$".0$122*'*-"./$3&4/4$
!"#"$%
&'#'(%
)
)#(
)#'
)#&
)#*
)#+
)#!
)#"
)#,
-./01/234 -./01/24-55
!"#$% &'()*$&+$,)&-.&/0'$0/1$,)&-.&/'*22$3&2-2$
!"#!$%
"#&'%
(#"$%
!)#'"%
*!#$(%
$#+)%
,
,#,)
,#*
,#*)
,#(
,#()
,#!
,#!)
,#$
!""#$%& !"'(#)* +#,("- .!//$ .#/%0)1 !//,%2(!3(4%
!"#$% &'()*$&+$,-++*.*/0$1)&0-&/2'$3&40$567*4$
Figure 3: The distribution of (a) relevant posts, (b) emotional posts and (c) six categories of emotional posts. The results indicated
negative emotions were non-negligible.
sufficient and adequate analysis, so we chose 21 days as the analysis
range. Figure 6 (a) demonstrated the changing patterns of emotional
disclosure during a 21-day diary-keeping. The results showed peo-
ple in quarantine were able to adjust their mental health to some
extent. In particular, the negative emotional disclosure relatively
occupied high positions at the beginning of quarantine, then gradu-
ally decreased, except for some fluctuation foranxious later on. The
gradual decrease in the proportion of negative emotions indicated
that individuals in quarantine tended to achieve a psychological
balance as they might gain a better understanding of the nature of
the epidemic. Furthermore, positive emotions could also validate
the idea: hopeful as a whole were on the rise, especially near the
end of quarantine (i.e., 14th, 20th, 21st days). The changing pattern
of appreciative showed that people maybe initially felt appreciative
of the support received from others, but as time went on, the nov-
elty wore off and feeling of isolation might arise, contributing to a
decrease. However, as the quarantine neared its end, appreciation
could be rekindled since people built up anticipation and excite-
ment, accompanied by renewed support and encouragement from
their surroundings.
7-day and 14-day grouped changing patterns: Figure 5 (a)
delineated that the number of posts had continuously dropped for
the first 14 days and stabilized thereafter, where the difference was
relatively large for the first 7 days and around the 14th day. Figure
5 (b) demonstrated that 7 days and 14 days were the dominant
quarantine durations. The results were in line with the quarantine
policy [23] which recommended 7 days and 14 days as quarantine
or health-monitoring periods. The 7-day and 14-day diary-keeping
of emotional disclosure were indicated in Figure 6 (b) and (c). The
results yielded some detailed and interesting characteristics: (1) On
the 3rd and 4th day,anxious and boring were increasing andannoyed
maintained at a relatively high level, which suggested that these
two days might have posed significant challenges for individuals;
(2) Anxious showed a pattern of first decline and then rise between
the 4th day and 12th day, with a notable increase starting on the 8th

CHCHI 2023, November 13–16, 2023, Denpasar, Bali, Indonesia Deng, et al.
2
0/42 0/52 0/62 0/72 0/82 0/92 0/102 0/112 0/122 1/12 1/22 1/32 1/42 1/52 1/62 1/72 1/82 1/92 1/102 1/112 1/122 2/12 2/22 2/32 2/42 2/52 2/62 2/70
.00
.10
.20
.30
.40
.5E
motion (proportion)T
ime
a nnoyed                      a nxious                  b oring
a ppreciative                h opeful                  h appy
Figure 4: The long-term changing patterns of emotional dis-
closure from April 2020 to July 2022.
0 5 10 15 20 25 30 35 40
0
500
1000
1500
2000
2500
(a) Number of Posts per Day
Post Number
Day
7 14
0
1000
2000
3000
4000
5000
6000
7000
8000
3163
4746
7347
Others
Post Number
Group
(b) Number of Posts for Different Groups
Figure 5: The statistical results of post number for (a) per day
and (b) different groups (including 7-day quarantine group,
14-day quarantine group and the remaining group).
day. It indicated that during shorter durations (e.g., from the 4th day
to the 8th day), anxious emotions tended to be alleviated. However,
for longer durations (e.g., from the 8th day to the 12th day), anxiety
could become more prominent; (3) An interesting finding was that
on the last day of the quarantine, annoyed would upsurge from a
relatively low proportion. This could be attributed to the common
quarantine durations, where people might have anticipated the end
of quarantine on either the 7th or 14th day, only to discover that the
quarantine period was extended. The uncertainty and unexpected
prolongation of the isolation period might lead to a higher level of
annoyance among individuals.
The comparison between the two kinds of grouped changing
patterns signified that although the overall trends of emotional
disclosure were similar, there still existed differences during the
same period to some extent. For instance, from the 4th to 6th day,
7-day quarantined people reported a decrease in annoyed, possibly
due to a sense of relief as their isolation period neared its end. How-
ever, individuals who were quarantined for 14 days experienced
an increase in annoyed on the 5th day. This increase could be at-
tributed to the realization of a longer remaining isolation period,
leading to frustration and irritation. Moreover, in terms of anxious,
individuals in 7-day diary-keeping stayed at a high level for the first
2 days while those in the 14-day grouped diary-keeping exhibited
a decrease after the first day.
4.3 RQ3: Latent Factors Contributing to
Negative Emotional Disclosure
After keeping track of some interesting temporal characteristics
of emotional disclosure, we probed further into the latent factors
that might contribute to negative emotional disclosure, attempting
to explore effective countermeasures. Table 2 and Table 3 summa-
rized the topical themes and corresponding keywords with LDA
after an inductive thematic analysis described in Section 3.4. The
abundance of topical themes indicated there were diverse possible
factors denoting negative emotional disclosure, and the reasons
behind each negative emotion were also extensive. To effectively
and precisely alleviate negative emotions, managers of epidemic
prevention and control were suspected to pay more attention to
divergent and fundamental measures instead of purely providing
psychological counseling to regulate emotions in quarantine.
4.3.1 Latent annoyed Factors. Based on the results of Table 2 and
the corresponding posts, there were four topical themes related to
annoyed: (1) Individuals in quarantine were inclined to complain
about the endless epidemic about the frequent nucleic acid test
requirements, a flurry of reports about the virus and confirmed
cases, etc; (2) During quarantine, people felt physically and mentally
restricted as if they were in jail and longed for spirit disinhibition
such as going out and enjoying the scenery of the world. Moreover,
the solitude property profoundly aroused a sense of loneliness,
evoking the eagerness for companionship; (3) The management
measures and sometimes disorderly arrangement also irritated people
in quarantine due to sporadic cases and the local implementation. It
was argued that some local arrangements were suddenly changed
and the attitude of services and efficiency of implementations could
lead to annoyance; (4) Poor infrastructure was also one of the major
reasons for provoking exasperation, such as the accommodation,
accessibility (e.g., takeout and express delivery), and supply or taste
of food.
4.3.2 Latent anxious Factors. Table 3 signified the following five
latent anxious factors: (1) Quarantine had disrupted our lives, both
in terms of physical adaptation (e.g., internal clock) and mundane
goings-on of their lives (e.g., work and study); (2) Despite being
in quarantine, they still worried about being infected during transit
from home to quarantine locations, on the way to the nucleic acid
test, or due to the confirmed cases around (e.g., communities and
companies); (3) A sense of apprehensiveness might be engendered
on account of the uncertainty of influences by management mea-
sures. For example, the public did not know when and how long
they would be in quarantine. An unexpected finding was that a
knock on the door made people feel anxious; (4) Individuals felt anx-
ious about both the mental and physical health . The state of mind
was easy to break down and insomnia was a normal phenomenon
during quarantine. In addition, the illness rather than COVID-19
(e.g., common cold or fever) was very anxiety-provoking; (5) The
supply of food was of great importance, in particular for people in
home quarantine who had to vie for food on online food delivery
apps usually with a high price, also causing concern of finance.
Based on these potential factors of negative emotional disclosure,
a series of strategies and countermeasures could be considered by
governments, Centers for Disease Control and Prevention (CDC)

Emotional Disclosure via Diary-keeping in Quarantine CHCHI 2023, November 13–16, 2023, Denpasar, Bali, Indonesia
0 2 4 6 8 10 12 14 16 18 20 22
0.294
0.343
0.392
0.441
0.040
0.060
0.080
0.100
0.000
0.010
0.020
0.030
0.000
0.039
0.078
0.117
0.156
0.12
0.18
0.24
0.30
0 2 4 6 8 10 12 14 16 18 20 22
0.258
0.344
0.430
0.516Annoyed
Day
Anxious Boring Appreciative Hopeful
(a) 21-day Global Changing Patterns
Happy
0 2 4 6 8
0.357
0.374
0.391
0.408
0.061
0.066
0.071
0.075
0.023
0.026
0.029
0.032
0.038
0.048
0.057
0.067
0.087
0.116
0.145
0.174
0 2 4 6 8
0.306
0.324
0.342
0.360Annoyed
Day
(b) 7-day Grouped Changing Patterns
Anxious Boring Appreciative Hopeful Happy
0 2 4 6 8 10 12 14
0.294
0.336
0.378
0.420
0.038
0.057
0.076
0.095
0.000
0.011
0.022
0.033
0.044
0.014
0.028
0.042
0.056
0.078
0.156
0.234
0.312
0 2 4 6 8 10 12 14
0.160
0.240
0.320
0.400Annoyed
Day
Anxious Boring Appreciative
(c)14-day Grouped Changing Patterns
Hopeful Happy
Figure 6: The period-based changing patterns from (a) 21-day global perspective, as well as (b) 7-day and (c) 14-day grouped
perspectives.
Table 2: List of topical themes and representative keywords with snippets of example posts in annoyed.
Topical Theme Keywords Example
endless epidemic nucleic acid (test), epidemic
situation, notification, lifting
(lockdowns), diagnosis, report,
global, virus, release, informa-
tion
I have to do the nucleic acid test every day, and
can’t even attend the class. The epidemic is really
annoying. When will this epidemic end?
freedom restriction and
solitude
expect, monotony, go out, ac-
company, world, scenery, re-
lease from prison, closure, spirit,
liberation
Tomorrow is another week, but I still don’t know
when I can go out.
management measures
and disorderly arrange-
ment
policy, rule, management,
street, service, measure, adjust-
ment, wait, postpone, efficiency
. . . Why is the policy so rigid. . . Not everyone can
sit at home all the time without earning money. .
. How can there be different quarantine methods
in the same area? When consulting the policy, no
department can give a reasonable explanation or
document.
infrastructure (food, ac-
commodation)
room, boxed meal, takeaway,
quilt, bread, window, express
delivery, disinfect, vegetables,
eggs
As soon as I entered the room, I was stunned. A
lot of hair on the ground and unknown marks on
the pillow and bed. Dirty and messy!
and other official organizations. For instance, governments could
provide basic food, common medicines, psychological counseling
and free online consultation to deal with unsatisfied infrastructure
and health concerns; the staff could try to ensure that they knock
on the door at a fixed time period to relieve the anxiety caused
by uncertainty of management measures ; during the nucleic acid
test, dividing people in quarantine into batches or taking other
preventive measures to avoid cross-infection could be considered,
in order to reduce uncertainty of infection ; schools or companies
would adopt specialized management requirements for personnel
in quarantine, reducing the stress of disturbance of daily routine .

CHCHI 2023, November 13–16, 2023, Denpasar, Bali, Indonesia Deng, et al.
Table 3: List of topical themes and representative keywords with snippets of example posts in anxious.
Topical Theme Keywords Example
disturbance of daily rou-
tine
wake up, internal clock, adjust-
ment, job, work, online course,
work from home, study, punch
in, homework
My internal clock is completely messed up. I don’t
want to sleep every night and can’t wake up in the
morning. The worst thing about quarantine is the
exhaustion of mental energy, and the living space,
workspace and study space are very chaotic.
uncertainty of infection virus, protective clothing, con-
tact, nucleic acid, infection, di-
agnosis, transit, unit, commu-
nity, positive
It is hoped that the process of nucleic acid test
can be more standardized so that there will be no
more cross-infection.
uncertainty of influ-
ences by management
measures
staff, concentrated (quaran-
tine), knocking, government,
accommodation, inn, ambu-
lance, hotel, home, reception
I used to feel the epidemic was far away from
me, but this time I really feel the fear. One is the
anxiety of waiting and not knowing when I will
be taken away for quarantine. The other is...
health insomnia, see a doctor, sleep-
less, cough, fever, throat, sick-
ness, state of mind, spirit,
breakdown
My head is about to explode probably because
the hotel is so cold and I didn’t dry my hair after
washing.
supply starve to death, steamed buns,
food, rice, instant noodles,
grocery shopping, refrigerator,
sustenance, eggs, stock
Insomnia until six o’clock in the morning...who
knows...I went to [a food delivery app] to grab
food at six o’clock and didn’t get it.
5 DISCUSSION
In this section, we reflect on our findings and enlighten practical
and design implications to drive the understanding of emotional
disclosure on social media in quarantine. First, we probe into the
responses of people in quarantine under the emotional challenges,
and propose implications for better balancing emotions in Section
5.1. Then, we highlight design implications on social media and
reflect on the health interventions in Section 5.2. Afterwards, we
think over how latent factors of negative emotions enlighten social
support to mitigate negative psychological impacts in Section 5.3.
5.1 Immersed in Emotional Situation:
Responses and Implications
By identifying quarantine-specific emotional categories, this work
enriches the understanding of emotional disclosure from the per-
spectives of how individuals respond to quarantine, and how the
responses demystify the practical and design implications to aid
psychological balance during quarantine.
First, this work revealed the resilience and adaptivity of the
public in the scenario of quarantine to some degree. As shown in
Section 4.1, the proportion of positive emotions was slightly higher
than negative ones, and happy (35.96%) played the most significant
role in positive emotions, indicating the emotional well-being of the
population on average was challenging but not as bad as imagined.
Meanwhile, our findings in Section 4.2 further demonstrated that
negative emotions diminished over time. Indeed, a type of natural
recovery capability (i.e., resilience and adaptivity) was corrobo-
rated. It also dovetailed with the cognitive dissonance theory [31],
pointing out that in order to reduce negative psychological effects,
people are more likely to change their cognition if there is no way
of changing the environment. In this regard, adding the recovery
capability as a reference index during the psychological treatment
process in quarantine, would be promising to better help mental
health management.
Second, this work also uncovered severe psychological stress in
people during quarantine. As demonstrated in Section 4.1, the pro-
portion of posts with negative emotions was 45.77% among all posts.
The massive negative content on social media could form a vicious
circle like pyramid schemes. From the perspective of receivers, it
is common that people have more engagement in negative con-
tent on social media [56, 63]. Negativity bias theory [1] indicates
that people’s behavior and cognition are more likely to be affected
by negative emotions. From the other perspective of posters, on
account of social compensation theory [72], people with psycho-
logical distress have more intense motives to disclose on social
media who desire more social connection and affiliation [41, 46, 71].
Furthermore, recall that the most predominant negative category
was annoyed exhibited in Section 4.1, rather thananxious. The more
outstanding performance of annoyed compared with anxious bears
out the fatigue phenomenon during quarantine due to endless epi-
demic [68, 76]. Angry speech is proven to be more likely to receive
abusive language, in turn, [55]. Then, a new round of negative out-
comes emerges on social media. Thus, detecting and moderating
negative emotional disclosure on social media is of great imperative,
especially with the extensive negative exposure to social media dur-
ing quarantine. In light of the fatigue phenomenon, how to adjust
social support measures accordingly (e.g., maybe from previously
disseminating professional information about the virus and de-
bunking misinformation to providing more emotional accompany),
deserves more in-depth exploration. Moreover, the emotion analysis

Emotional Disclosure via Diary-keeping in Quarantine CHCHI 2023, November 13–16, 2023, Denpasar, Bali, Indonesia
approach in our work, which focuses on identifying quarantine-
specific emotional categories, investigating emotional changing
patterns and exploring latent factors of emotions, could be consid-
ered as an adjunct in mental health diagnosis during quarantine or
subsequent epidemic era. Taking a broader perspective, our work
offers compelling evidence supporting the feasibility and signifi-
cance of conducting emotion analysis in affective computing by
annotating context-specific emotions. By focusing on the emotions
experienced within particular contexts, we can gain valuable in-
sights into individuals’ mental well-being and tailor interventions
and support accordingly.
5.2 Driven from Diary-keeping: Designs and
Interventions
In the specific setting of quarantine, we notice a novel form of
emotional disclosure: people in quarantine spontaneously write
diaries on social media for mundane recording, experience sharing
and opinion expression. By uncovering the diary-keeping behaviors
on social media, we reflect on the design implications of how diaries
during extraordinary times could be supported via social media, and
the practical implications of health intervention strategies based
on emotional disclosure.
The intimacy with data is well exhibited via social-media-based
diary-keeping in our work. The narration technique on social me-
dia, leveraged by users to delineate their daily life, provides a com-
plementary perspective for application-centered numerical track-
ing techniques (e.g. Personal Informatics apps [20]) in the way of
person-centered instructive description. The functions on social me-
dia like sharing, forwarding, commenting and mentioning (i.e., @)
provide a platform for users to communicate with each other, stim-
ulating and boosting the social and cultural potential. The changing
patterns in Section 4.2 provided evidence that employing large-scale
observation of quarantine diaries could, to some degree, serve as a
viable approach for identifying and comprehending emotional dis-
closure. On this note, emotion-detecting systems and system-level
interventions (e.g., reverse recommendation of positive information
when detecting extreme negative emotions) could come into being
by future designers and researchers. Note that we do not instigate
users to open their private and specific data on social media but
just encourage the narrative way of diaries. On the long view, the
present identification approach of diary-self-tracking is based on
the keyword (e.g.,Quarantine Diary) and temporal label (e.g., Day 1)
which is manually tracked by users. To this end, system-facilitated
construction of diaries (e.g., providing an elaborately-designed di-
ary template) may be considered for future researchers. Also, in-
tegrating diary apps or other self-tracking functions into social
media, and whether the diary interface should become more strict
like numerical recording or more flexible like paper journaling, are
a worth-exploring research direction. Nevertheless, some studies
have shown that self-disclosure on social media, especially negative
sharing, can engender a lot of risks (e.g., privacy) [ 10] and need
to be carefully created and negotiated [3]. Social media posts are
also subject to content moderation and surveillance, so it is hard to
assume that people share experiences and opinions of quarantine
without concern.
Drawing on the outcomes of social-media-based diary-keeping,
health intervention strategies are engendered. As shown in Sec-
tion 4.2, the discrepancy of each group in emotional disclosure
demonstrated individuals might have different psychological sta-
tuses and concerns at the same period. Such different patterns
enable governments to comprehend the people in quarantine from
multiple perspectives when making healthcare policies, and spe-
cialized healthcare measures for each group are recommended.
Meanwhile, health intervention strategies (e.g., psychological crisis
consultation time) are suspected to dynamically adjust and focus on
several days, such as the 3rd and 4th days when all negative emo-
tions were at a high level. A bounce came up in annoyed near the
end of quarantine, indicating the health management department
cannot ignore the negative emotions close to the end. A plausible
interpretation is that approaching the end of quarantine, people
are suddenly informed to remain in quarantine with the annoyed
increasing. These findings empirically validated the feasibility of
understanding emotional disclosure from a quantitative perspective.
The changing patterns can also enlighten mental health regulations
during similar public health emergencies.
5.3 Enlightened by Latent Factors of Negative
Emotional Disclosure: Insights on the Social
Support
Prior work ascribed great importance to self-disclosure and social
support as critical approaches to improving living standards and
self-efficacy. Negative emotional disclosure demonstrates the latent
concerns and dissatisfaction of the public and functions as an im-
petus to provide available direction for social support. This section
further discusses what kind of social support could be provided to
alleviate negative emotions based on self-disclosure.
This work comprehensively signified the intricate characteristics
of factors that might account for negative emotions and revealed
the potential need for social support. Driven by the social support
theory [22], and the effect mechanism of self-disclosure and psycho-
logical well-being [51], typical social support categories consist of
instrumental (i.e., the enacted supportive behaviors) and emotional
(i.e., the perceived impression) support. In essence, our observations
of potential social support needs in Section 4.3 were in line with
the theory-driven category. On the one hand, instrumental social
support to deal with practical difficulties like short supply and poor
infrastructure from governments and related departments, is im-
perative. Also, given that uncertainty is a remarkable factor during
quarantine, construing a channel on social media to interpret poli-
cies and measures, may be beneficial to mitigate negative emotions
and avoid more serious situations caused by misinformation. On
the other hand, social media together with official organizations,
could be taken into account for emotional social support. The emo-
tional needs like freedom restriction and solitude and feeling the
epidemic is endless, verified online accompany is vital due to abrupt
reduction of physical interactions. On this note, tailored accompa-
nying communities consisting of experienced people, professionals
or digital volunteers, and interactive chatbots on social media are
recommended for future designers to cure people in quarantine
who are grappling with negative emotions.

CHCHI 2023, November 13–16, 2023, Denpasar, Bali, Indonesia Deng, et al.
5.4 Limitations and Future Work
This work adopted a quantitative approach to comprehensively
investigate the categories of emotional disclosure, the changing
patterns of emotional disclosure and factors that might give rise to
negative emotions during quarantine, which enlighten the practical
and design implications for better relieving mental health issues.
Nonetheless, this work has the following limitations: (1) While so-
cial media can serve as a means of communication, posts shared on
social media may not completely capture or convey the full range
of emotions or explicit and implicit needs of the public. Individu-
als moderating their content and engaging in self-surveillance on
social media could present a curated version that doesn’t reflect
true emotions or comprehensive needs. (2) Due to the presence of
multiple or repeated types of temporal information within posts,
the exact accuracy of the extracted temporal information cannot be
guaranteed, even though we have employed rules based on manual
encoding and extensive experience.
When keeping a diary on social media becomes prevalent but
related interface designs are still limited, we encourage a customized
diary interface while combining the features of personalization
and flexibility on social media in the future. Additionally, future
work could focus on the difference between social-media-based
diaries and paper journaling to obtain valuable inspiration for a
user-friendly interface.
6 CONCLUSION
In this paper, we explore the categories of emotional disclosure
during quarantine, the changing patterns of emotional disclosure
and possible factors that might contribute to negative emotions
through a quantitative approach. By investigating the posts during
quarantine on a popular Chinese social media platform Weibo, we
identify emotional categories in quarantine, and discover the dis-
tribution of different emotions. The results demonstrate that posts
with negative emotions are non-negligible which approximately
account for half of all posts. Furthermore, the changing patterns
of emotional disclosure indicate the resilience of the public with
a declining trend of negative emotions during quarantine, yet the
annoyed emotions upsurge near the end of the quarantine period.
Finally, we uncover the possible influencing factors of negative
emotions like disturbance of daily routine, poor infrastructure as
well as the uncertainty of influences by management measures.
Based on the findings, we propose practical and design implications
to ease the psychological stress during quarantine.
ACKNOWLEDGMENTS
The research was supported in part by a RGC RIF grant under the
contract R6021-20, RGC CRF grants under the contracts C7004-22G
and C1029-22G, and RGC GRF grants under the contracts 16209120,
16200221 and 16207922.
REFERENCES
[1] Achini Adikari, Rashmika Nawaratne, Daswin De Silva, Sajani Ranasinghe, Os-
hadi Alahakoon, Damminda Alahakoon, et al . 2021. Emotions of COVID-19:
content analysis of self-reported information using artificial intelligence. Journal
of medical Internet research 23, 4 (2021), e27341.
[2] David E Alexander. 2014. Social media in disaster risk reduction and crisis
management. Science and engineering ethics 20, 3 (2014), 717–733.
[3] Nazanin Andalibi and Andrea Forte. 2018. Responding to sensitive disclosures
on social media: A decision-making framework. ACM Transactions on Computer-
Human Interaction (TOCHI) 25, 6 (2018), 1–29.
[4] LI Ang, HAO BiBo, BAI ShuoTian, and Zhu Tingshao. 2015. Predicting psycholog-
ical features based on web behavioral data: Mental health status and subjective
well-being. Chinese Science Bulletin 60, 11 (2015), 994–1001.
[5] Anshika Arora, Pinaki Chakraborty, MPS Bhatia, and Prabhat Mittal. 2021. Role
of emotion in excessive use of Twitter during COVID-19 imposed lockdown in
India. Journal of Technology in Behavioral Science 6, 2 (2021), 370–377.
[6] Ashwini Ashokkumar and James W Pennebaker. 2021. Social media conversations
reveal large psychological shifts caused by COVID-19’s onset across US cities.
Science advances 7, 39 (2021), eabg7843.
[7] Shrey Bagroy, Ponnurangam Kumaraguru, and Munmun De Choudhury. 2017. A
social media based index of mental well-being in college campuses. InProceedings
of the 2017 CHI Conference on Human factors in Computing Systems . 1634–1646.
[8] Hongwei Bao. 2020. Three Women and Their Wuhan Diaries: Women’s Writing
in a Quarantined Chinese City. Cha (2020).
[9] Jay J Van Bavel, Katherine Baicker, Paulo S Boggio, Valerio Capraro, Aleksandra
Cichocka, Mina Cikara, Molly J Crockett, Alia J Crum, Karen M Douglas, James N
Druckman, et al. 2020. Using social and behavioural science to support COVID-19
pandemic response. Nature human behaviour 4, 5 (2020), 460–471.
[10] Natalya N Bazarova and Yoon Hyung Choi. 2014. Self-disclosure in social media:
Extending the functional approach to disclosure motivations and characteristics
on social network sites. Journal of communication 64, 4 (2014), 635–657.
[11] Batsheva Ben-Amos and Dan Ben-Amos. 2020. The diary: the epic of everyday
life. Indiana University Press.
[12] Christoph Benke, Lara K Autenrieth, Eva Asselmann, and Christiane A Pané-
Farré. 2020. Lockdown, quarantine measures, and social distancing: Associations
with depression, anxiety and distress at the beginning of the COVID-19 pandemic
among adults from Germany. Psychiatry research 293 (2020), 113462.
[13] Manisha Bhende, Anuradha Thakare, Bhasker Pant, Piyush Singhal, Swati Shinde,
and Betty Nokobi Dugbakie. 2022. Integrating Multiclass Light Weighted BiL-
STM Model for Classifying Negative Emotions. Computational Intelligence and
Neuroscience 2022 (2022).
[14] David M Blei, Andrew Y Ng, and Michael I Jordan. 2003. Latent dirichlet allocation.
Journal of machine Learning research 3, Jan (2003), 993–1022.
[15] Virginia Braun and Victoria Clarke. 2012. Thematic analysis. American Psycho-
logical Association.
[16] Lorena Canet-Juric, María Laura Andrés, Macarena Del Valle, Hernán López-
Morales, Fernando Poó, Juan Ignacio Galli, Matías Yerro, and Sebastián Urquijo.
2020. A longitudinal study on the emotional impact cause by the COVID-19
pandemic quarantine on general population. Frontiers in Psychology (2020), 2431.
[17] Guang Cao, Lining Shen, Richard Evans, Zhiguo Zhang, Qiqing Bi, Wenjing
Huang, Rui Yao, and Wenli Zhang. 2021. Analysis of social media data for
public emotion on the Wuhan lockdown event during the COVID-19 pandemic.
Computer Methods and Programs in Biomedicine 212 (2021), 106468.
[18] Tianqi Chen and Carlos Guestrin. 2016. Xgboost: A scalable tree boosting system.
In Proceedings of the 22nd acm sigkdd international conference on knowledge
discovery and data mining . 785–794.
[19] Yixin Chen, Ke-Rou Wang, Weikai Xu, and Yun Huang. 2021. Exploring com-
menting behavior in the COVID-19 super-topic on Weibo. In Extended Abstracts
of the 2021 CHI Conference on Human Factors in Computing Systems . 1–7.
[20] Janghee Cho, Tian Xu, Abigail Zimmermann-Niefield, and Stephen Voida. 2022.
Reflection in Theory and Reflection in Practice: An Exploration of the Gaps
in Reflection Support among Personal Informatics Apps. In CHI Conference on
Human Factors in Computing Systems . 1–23.
[21] Kyunghyun Cho, Bart Van Merriënboer, Caglar Gulcehre, Dzmitry Bahdanau,
Fethi Bougares, Holger Schwenk, and Yoshua Bengio. 2014. Learning phrase
representations using RNN encoder-decoder for statistical machine translation.
arXiv preprint arXiv:1406.1078 (2014).
[22] Sheldon Cohen and Thomas A Wills. 1985. Stress, social support, and the buffering
hypothesis. Psychological bulletin 98, 2 (1985), 310.
[23] National Health Commission. 2021. Notice on Issuing the Eighth Edition of the
Novel Coronavirus Pneumonia Prevention and Control Plan (Chinese). http://
www.nhc.gov.cn/jkj/s3577/202105/6f1e8ec6c4a540d99fafef52fc86d0f8.shtml. Ac-
cessed: 2023-10-22.
[24] Nello Cristianini, John Shawe-Taylor, et al. 2000. An introduction to support vector
machines and other kernel-based learning methods . Cambridge university press.
[25] Yiming Cui, Wanxiang Che, Ting Liu, Bing Qin, and Ziqing Yang. 2021. Pre-
training with whole word masking for chinese bert. IEEE/ACM Transactions on
Audio, Speech, and Language Processing 29 (2021), 3504–3514.
[26] Munmun De Choudhury, Michael Gamon, Scott Counts, and Eric Horvitz. 2013.
Predicting depression via social media. In Seventh international AAAI conference
on weblogs and social media .
[27] Munmun De Choudhury, Emre Kiciman, Mark Dredze, Glen Coppersmith, and
Mrinal Kumar. 2016. Discovering shifts to suicidal ideation from mental health
content in social media. InProceedings of the 2016 CHI conference on human factors
in computing systems. 2098–2110.

Emotional Disclosure via Diary-keeping in Quarantine CHCHI 2023, November 13–16, 2023, Denpasar, Bali, Indonesia
[28] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2018. Bert:
Pre-training of deep bidirectional transformers for language understanding.arXiv
preprint arXiv:1810.04805 (2018).
[29] Hanane Elfaik et al. 2021. Social Arabic Emotion Analysis: A Comparative Study
of Multiclass Classification Techniques. In 2021 Fifth International Conference On
Intelligent Computing in Data Sciences (ICDS) . IEEE, 1–8.
[30] Ran Feng and Alex Ivanov. 2022. Gender Differences in Emotional Valence and
Social Media Content Engagement Behaviors in Pandemic Diaries: An Analysis
Based on Microblog Texts. Behavioral Sciences 13, 1 (2022), 34.
[31] Leon Festinger. 1962. A theory of cognitive dissonance . Vol. 2. Stanford university
press.
[32] Uwe Flick. 2022. An introduction to qualitative research. An introduction to
qualitative research (2022), 1–100.
[33] Huiji Gao, Geoffrey Barbier, and Rebecca Goolsby. 2011. Harnessing the crowd-
sourcing power of social media for disaster relief. IEEE Intelligent Systems 26, 3
(2011), 10–14.
[34] goto456. 2019. Chinese Stop Words List. https://github.com/goto456/stopwords.
[35] Sharath Chandra Guntuku, Garrick Sherman, Daniel C Stokes, Anish K Agarwal,
Emily Seltzer, Raina M Merchant, and Lyle H Ungar. 2020. Tracking mental
health and symptom mentions on Twitter during COVID-19. Journal of general
internal medicine 35 (2020), 2798–2800.
[36] Laura Hawryluck, Wayne L Gold, Susan Robinson, Stephen Pogorski, Sandro
Galea, and Rima Styra. 2004. SARS control and psychological effects of quarantine,
Toronto, Canada. Emerging infectious diseases 10, 7 (2004), 1206.
[37] Changyang He, Yue Deng, Wenjie Yang, and Bo Li. 2022. " Help! Can You Hear
Me?": Understanding How Help-Seeking Posts are Overwhelmed on Social Media
during a Natural Disaster.Proceedings of the ACM on Human-Computer Interaction
6, CSCW2 (2022), 1–25.
[38] Changyang He, Lu He, Tun Lu, and Bo Li. 2021. Beyond Entertainment: Unpacking
Danmaku and Comments’ Role of Information Sharing and Sentiment Expression
in Online Crisis Videos. Proceedings of the ACM on Human-Computer Interaction
5, CSCW2 (2021), 1–27.
[39] Sepp Hochreiter and Jürgen Schmidhuber. 1997. Long short-term memory.Neural
computation 9, 8 (1997), 1735–1780.
[40] Michel Hockx. 2015. Internet literature in China . Columbia University Press.
[41] Erin E Hollenbaugh and Amber L Ferris. 2014. Facebook self-disclosure: Examin-
ing the role of traits, social cohesion, and motives. Computers in Human Behavior
30 (2014), 50–58.
[42] Md Mahbub Hossain, Samia Tasnim, Abida Sultana, Farah Faizah, Hoimonty
Mazumder, Liye Zou, E Lisako J McKyer, Helal Uddin Ahmed, and Ping Ma. 2020.
Epidemiology of mental health problems in COVID-19: a review. F1000Research
9 (2020).
[43] Man Hung, Evelyn Lauren, Eric S Hon, Wendy C Birmingham, Julie Xu, Sharon
Su, Shirley D Hon, Jungweon Park, Peter Dang, Martin S Lipsky, et al. 2020. Social
network analysis of COVID-19 sentiments: Application of artificial intelligence.
Journal of medical Internet research 22, 8 (2020), e22590.
[44] Shagun Jhaver, Amy Bruckman, and Eric Gilbert. 2019. Does transparency in
moderation really matter? User behavior after content removal explanations on
reddit. Proceedings of the ACM on Human-Computer Interaction 3, CSCW (2019),
1–27.
[45] Sean W Kelley and Claire M Gillan. 2022. Using language in social media posts to
study the network dynamics of depression longitudinally.Nature communications
13, 1 (2022), 1–11.
[46] Kyung-Tag Lee, Mi-Jin Noh, and Dong-Mo Koo. 2013. Lonely people are no
longer lonely on social networking sites: The mediating role of self-disclosure
and social support. Cyberpsychology, Behavior, and Social Networking 16, 6 (2013),
413–418.
[47] Sijia Li, Yilin Wang, Jia Xue, Nan Zhao, and Tingshao Zhu. 2020. The impact
of COVID-19 epidemic declaration on psychological consequences: a study on
active Weibo users. International journal of environmental research and public
health 17, 6 (2020), 2032.
[48] Sijia Li, Jia Xue, Xiaoqian Liu, Peijing Wu, Tianli Liu, Meng Zhu, Nan Zhao,
and Tingshao Zhu. 2022. Exploring the changes of suicide probability during
COVID-19 among Chinese Weibo users. Crisis: The Journal of Crisis Intervention
and Suicide Prevention 43, 3 (2022), 197.
[49] Xuyang Li, Antara Bahursettiwar, and Marina Kogan. 2021. Hello? Is There
Anybody in There? Analysis of Factors Promoting Response From Authoritative
Sources in Crisis. Proceedings of the ACM on Human-Computer Interaction 5,
CSCW1 (2021), 1–21.
[50] Weisheng Lu, Liang Yuan, Jinying Xu, Fan Xue, Bin Zhao, and Chris Webster. 2020.
The psychological effects of quarantine during COVID-19 outbreak: Sentiment
analysis of social media data. medRxiv (2020).
[51] Mufan Luo and Jeffrey T Hancock. 2020. Self-disclosure and social media: motiva-
tions, mechanisms and psychological well-being. Current Opinion in Psychology
31 (2020), 110–115.
[52] Shaozhuang Ma, Weilong Zeng, Andreia Borges, Yiqing Xu, and Jinrui Zhang.
2021. Emotional well-being in COVID-19 mass quarantine: the role of personal
response and life activity: a 14-day diary study in China. Psychology & Health
(2021), 1–23.
[53] Lydia Manikonda and Munmun De Choudhury. 2017. Modeling and understand-
ing visual attributes of mental health disclosures in social media. In Proceedings
of the 2017 CHI Conference on Human Factors in Computing Systems . 170–181.
[54] Mary L McHugh. 2012. Interrater reliability: the kappa statistic. Biochemia
medica 22, 3 (2012), 276–282.
[55] Valeriya Mechkova and Steven L Wilson. 2021. Norms and rage: Gender and
social media in the 2018 US mid-term elections.Electoral Studies 69 (2021), 102268.
[56] Nasir Naveed, Thomas Gottron, Jérôme Kunegis, and Arifah Che Alhadi. 2011.
Bad news travel fast: A content-based analysis of interestingness on twitter. In
Proceedings of the 3rd international web science conference . 1–7.
[57] Yanping Ni, Morris Fabbri, Chi Zhang, and Kearsley A Stewart. 2020. Reciprocity
in quarantine: observations from Wuhan’s COVID-19 digital landscapes. Asian
bioethics review 12, 4 (2020), 435–457.
[58] Amelia Nierenberg. 2020. The Quarantine Diaries. https://www.nytimes.com/
2020/03/30/style/coronavirus-diaries-social-history.html. Accessed on August
12, 2023.
[59] World Health Organization et al. 2020. Considerations for quarantine of contacts
of COVID-19 cases: interim guidance, 19 August 2020 . Technical Report. World
Health Organization.
[60] Leysia Palen and Amanda L Hughes. 2018. Social media in disaster communica-
tion. Handbook of disaster research (2018), 497–518.
[61] Georgia Panayiotou, Maria Panteli, and Chrysanthi Leonidou. 2021. Coping with
the invisible enemy: The role of emotion regulation and awareness in quality of
life during the COVID-19 pandemic. Journal of Contextual Behavioral Science 19
(2021), 17–27.
[62] Deeksha Pandey, Suvrati Bansal, Shubham Goyal, Akanksha Garg, Nikita Sethi,
Dan Isaac Pothiyill, Edavana Santhosh Sreelakshmi, Mehmood Gulab Sayyad,
and Rishi Sethi. 2020. Psychological impact of mass quarantine on population
during pandemics—The COVID-19 Lock-Down (COLD) study. Plos one 15, 10
(2020), e0240501.
[63] Wei Peng, Achini Adikari, Damminda Alahakoon, and John Gero. 2019. Discov-
ering the influence of sarcasm in social media responses. Wiley Interdisciplinary
Reviews: Data Mining and Knowledge Discovery 9, 6 (2019), e1331.
[64] Marco Pennacchiotti and Siva Gurumurthy. 2011. Investigating topic models
for social media user recommendation. In Proceedings of the 20th international
conference companion on World wide web . 101–102.
[65] Hameedur Rahman, Junaid Tariq, M Ali Masood, Ahmad F Subahi,
Osamah Ibrahim Khalaf, and Youseef Alotaibi. 2023. Multi-tier sentiment analysis
of social media text using supervised machine learning. Comput. Mater. Contin
74 (2023), 5527–5543.
[66] Simon Lloyd D Restubog, Anna Carmella G Ocampo, and Lu Wang. 2020. Taking
control amidst the chaos: Emotion regulation during the COVID-19 pandemic. ,
103440 pages.
[67] Michael Röder, Andreas Both, and Alexander Hinneburg. 2015. Exploring the
space of topic coherence measures. InProceedings of the eighth ACM international
conference on Web search and data mining . 399–408.
[68] Stuart Ross, George Breckenridge, Mengdie Zhuang, and Ed Manley. 2021. House-
hold visitation during the COVID-19 pandemic. Scientific reports 11, 1 (2021),
1–11.
[69] Koustuv Saha, John Torous, Eric D Caine, Munmun De Choudhury, et al. 2020.
Psychosocial effects of the COVID-19 pandemic: large-scale quasi-experimental
study on social media. Journal of medical internet research 22, 11 (2020), e22600.
[70] Junyi Sun. 2020. Jieba Chinese text segmentation. https://github.com/fxsjy/jieba.
[71] Qing Tian. 2013. Social anxiety, motivation, self-disclosure, and computer-
mediated friendship: A path analysis of the social interaction in the blogosphere.
Communication Research 40, 2 (2013), 237–260.
[72] Patti M Valkenburg and Jochen Peter. 2007. Preadolescents’ and adolescents’
online communication and their closeness to friends. Developmental psychology
43, 2 (2007), 267.
[73] Yilin Wang, Peijing Wu, Xiaoqian Liu, Sijia Li, Tingshao Zhu, Nan Zhao, et al.
2020. Subjective well-being of Chinese Sina Weibo users in residential lockdown
during the COVID-19 pandemic: machine learning analysis. Journal of medical
Internet research 22, 12 (2020), e24775.
[74] Organization WH. 2020. Coronavirus disease (COVID-2019) situation reports.
Geneva: WHO (2020).
[75] Demetrius Williams. 2019. Understanding Weibo’s "Super Topics". https://www.
translatemedia.com/translationblog/understanding-weibos-super-topics/
[76] Simon Nicholas WIlliams and Kimberly Dienes. 2021. ’Variant fatigue’? Public
attitudes to COVID-19 18 months into the pandemic: A qualitative study. (2021).
[77] Tao Xiao. 2019. WeiboSuperSpider. https://github.com/Python3Spiders/
WeiboSuperSpider.
[78] Changhua Yang, Kevin Hsin-Yih Lin, and Hsin-Hsi Chen. 2007. Emotion Classifi-
cation Using Web Blog Corpora. In IEEE/WIC/ACM International Conference on
Web Intelligence (WI’07). 275–278. https://doi.org/10.1109/WI.2007.51
[79] Jing Zhu, Li Su, Yi Zhou, Juan Qiao, and Wei Hu. 2021. The effect of nationwide
quarantine on anxiety levels during the COVID-19 outbreak in China. Brain and
Behavior 11, 1 (2021), e01938.
