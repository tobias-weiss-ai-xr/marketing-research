---
title: 'A Survey of Stance Detection on Social Media: New Directions and Perspectives'
url: https://arxiv.org/abs/2409.15690
category: social-media
subcategory: empirical
date: 2024-09
venue: ''
authors:
- Bowen Zhang
- Genan Dai
- Fuqiang Niu
- Nan Yin
- Xiaomao Fan
source: arxiv
pdf_url: https://arxiv.org/pdf/2409.15690
pages: 19
chars: 98853
fetched_at: '2026-11-08T13:03:39+00:00'
kb_version: 1
---

# A Survey of Stance Detection on Social Media: New Directions and Perspectives

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2015 1
A Survey of Stance Detection on Social Media:
New Directions and Perspectives
Bowen Zhang†, Genan Dai†, Fuqiang Niu, Nan Yin, Xiaomao Fan, Senzhang Wang,
Xiaochun Cao, Senior Member, IEEE, and Hu Huang∗
Abstract—In modern digital environments, users frequently express opinions on contentious topics, providing a wealth of information
on prevailing attitudes. The systematic analysis of these opinions offers valuable insights for decision-making in various sectors,
including marketing and politics. As a result, stance detection has emerged as a crucial subfield within affective computing, enabling
the automatic detection of user stances in social media conversations and providing a nuanced understanding of public sentiment on
complex issues. Recent years have seen a surge of research interest in developing effective stance detection methods, with
contributions from multiple communities, including natural language processing, web science, and social computing. This paper
provides a comprehensive survey of stance detection techniques on social media, covering task definitions, datasets, approaches, and
future works. We review traditional stance detection models, as well as state-of-the-art methods based on large language models, and
discuss their strengths and limitations. Our survey highlights the importance of stance detection in understanding public opinion and
sentiment, and identifies gaps in current research. We conclude by outlining potential future directions for stance detection on social
media, including the need for more robust and generalizable models, and the importance of addressing emerging challenges such as
multi-modal stance detection and stance detection in low-resource languages.
Index Terms—Stance Detection, Future Directions in Stance Detection, Opinion Mining
✦
1 I NTRODUCTION
The proliferation of social media platforms has revolu-
tionized modern communication, transforming these plat-
forms into a primary source of news and information for
individuals. By facilitating user-generated content, these
platforms enable individuals to articulate their opinions,
share perspectives, and explore diverse facets of emerging
topics [1, 2]. The widespread adoption of social media has
yielded a treasure trove of data for researchers to investigate
various aspects of online human behavior, including the
public’s stance on social and political issues [3]. Through the
analysis and aggregation of user perspectives, researchers
can identify dominant trends and opinions on polarizing
topics. This vast repository of data holds significant poten-
tial for web mining and content analysis, with the insights
gleaned from such analysis having far-reaching implications
for decision-making processes, including advertising strate-
gies and political elections [4, 5]. Consequently, automated
stance detection on social media has become a crucial aspect
of opinion mining, enabling a more nuanced understanding
of user attitudes towards a diverse range of issues [6].
Bowen Zhang, Genan Dai and Xiaomao Fan are with the College of Big Data
and Internet, Shenzhen Technology University, Shenzhen, 518000, China.
Fuqiang Niu is with the College of Computer Science and Software, Shenzhen
University, Shenzhen, 518000, China.
Nan Yin is affiliated with Hong Kong University of Science and Technology,
Hong Kong, 999077, China.
Senzhang Wang is with the School of Computer Science and Engineering,
Central South University, Changsha 410083, China.
Xiaochun Cao is with the School of Cyber Science and Technology, Shenzhen
Campus of Sun Yat-sen University, Shenzhen 518107, China.
Hu Huang is affiliated with the Peking University Shenzhen Graduate School,
Shenzhen, 518000, China.
† Equal contribution.
∗ Corresponding author: Hu Huang (Email: huanghu@mail.ustc.edu.cn).
Manuscript received NOV 25, 2024.
The aim of stance detection is to determine the stance
of a text’s author towards a target, which can be an entity,
concept, event, idea, opinion, claim, or topic that is either
explicitly mentioned or implied within the text [7, 8]. Early
research on stance detection primarily focused on analyzing
debates on online forums, which differs from more recent
work that has emphasized social media platforms [9], par-
ticularly X (Twitter)1. Online forum debates typically have a
clear, single context compared to social media platforms. In
forum discussions, users engage in threaded conversations
where information flow is usually focused on a specific
topic. In contrast, social media discussions on a given topic
are more dispersed, although they can sometimes be linked
through hashtags2. However, social media platforms offer a
wealth of additional features, such as user networks, which
web science and computational social science researchers
have utilized to develop stance detection techniques that do
not rely solely on text [10, 11].
Related surveys. Recently, several research surveys on
stance detection have been conducted. Zubiaga et al. [12] fo-
cused on stance detection in product reviews, with a partic-
ular emphasis on feature-level stance detection techniques.
K ¨uc ¸¨uk and Can [13] provided a comprehensive review of
stance detection definitions, task classifications, and the
relationships between stance detection and related subtasks,
primarily focusing on natural language processing (NLP)
based methods. AlDayel and Magdy [14] were the first to
survey stance detection techniques for social media, cov-
ering not only NLP techniques but also network-level and
1. https://x.com/home
2. Hashtags are words and numbers following the # symbol that
categorize and track content on social media.
arXiv:2409.15690v2  [cs.CL]  25 Nov 2024

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2015 2
multi-modal information, providing a more comprehensive
overview of stance detection research in social media.
Our motivation. In this paper, we present an overview
of stance detection on social media and discuss promising
research directions. The key motivations of this survey are
summarized as follows:
• Recent advances in stance detection have shown signifi-
cant progress. However, existing surveys primarily con-
centrate on conventional approaches, including feature
engineering, traditional neural networks, and early pre-
trained language models such as BERT. These reviews
have not comprehensively analyzed the potential of
emerging large language models (LLM), particularly
the GPT family, in stance detection tasks. Therefore,
to comprehensively survey and synthesize the state-of-
the-art, it is imperative to consolidate and distill these
recent works.
• The rapid evolution of social media has led to an
increasing presence of multi-modal information and
interactive patterns, rendering traditional text-based
stance detection methods inadequate for these emerg-
ing contexts. In response, recent years have witnessed a
proliferation of novel tasks specifically designed for so-
cial media, underscoring the need for a comprehensive
review and synthesis of these advances.
• Despite the promising potential of LLMs for stance de-
tection, their application is still in an initial exploratory
phase. Effective techniques to adapt and utilize these
models for specific stance detection tasks remain an
open research challenge. Moreover, the roles, back-
ground knowledge understanding, and biases of LLMs
in stance detection contexts need to be further ex-
amined. Consequently, consolidating findings on these
outstanding issues will provide significant motivation
for authoring a new survey paper.
• As LLM continues to advance, stance detection appli-
cations are expanding. While traditionally focused on
sentence-level textual analysis, stance detection now
shows potential for richer data types and settings.
Moreover, new domains beyond text could benefit from
stance detection. Looking ahead, it is necessary to
discuss potential research directions that can improve
stance detection and mitigation capabilities.
Methodology for literature review. For our literature
review, we conducted a search on Google Scholar, DBLP ,
and Web of Science using the keywords “stance detec-
tion/prediction/classification” and other related terms such
as “viewpoint” and “perspective”. We focused on studies
where the search keywords were mentioned in the title
or abstract. The search results were refined using vari-
ous parameters, including the number of citations, year of
publication, and the ranking of the journal or conference.
We placed a special emphasis on venues related to NLP ,
computational social science, Web science, and information
processing. The list of relevant studies was then inspected,
and additional relevant studies were identified from the
reference lists of those papers and the papers that cited
them. We also conducted an extensive inspection of papers
citing the SemEval 2016 [5] stance detection task.
The remainder of this survey is structured as follows.
Section 2 provides an overview of related tasks in stance
detection. Section 3 presents datasets for stance detection
under various tasks. We then review traditional stance de-
tection methods in Section 4, tracing the technical develop-
ment trajectory. Next, we introduce state-of-the-art stance
detection methods based on LLMs in Section 5. Finally, we
discuss the challenges faced by stance detection in the era of
LLM in Section 6, as well as future research directions and
potential development paths.
2 S TANCE DETECTION TASKS
According to the literature, stance detection tasks can be
categorized from two primary perspectives: data-centric
and method development. From a data-centric perspec-
tive, stance detection encompasses several subtasks: target-
specific stance detection, multi-target stance detection,
claim-based stance detection, conversational stance detec-
tion, multi-modal stance detection, and user-level stance
detection. From a method development perspective, the
tasks can be classified into in-target stance detection, cross-
target stance detection, zero-shot stance detection, and
cross-lingual stance detection, each addressing different de-
ployment scenarios and technical challenges.
2.1 Data-Centric Perspective
From the perspectives of target types, data modalities, and
categories, this section provides a detailed introduction to
related tasks.
Target-specific stance detection. The target-specific
stance detection task is the most common task setting in
the literature. In this paradigm, stance is inferred with
respect to a predefined set of targets. Most previous studies
have focused on this paradigm, including works such as
Augenstein et al. [15], Darwish et al. [16], Igarashi et al.
[17], Liu and Zhang [18], and Mohammad et al. [5]. In
this approach, the input text is used to predict the stance
towards a specific, predefined single target.
Multi-target stance detection. Building on the foun-
dation of target-specific stance detection, the multi-target
stance detection task addresses the scenario where a sin-
gle tweet may contain multiple related targets. This task
involves predicting the stance polarity of multiple targets
within the same tweet (or statement). The concept of multi-
target stance detection is commonly used to analyze the
relationships between multiple targets, which often exhibit
strong correlations, such as multiple candidates in a political
election [33, 41, 53].
Claim-based stance detection. In contrast to target-
specific stance detection, which focuses on explicit entities
or topics, claim-based stance detection involves analyzing
the stance towards a specific claim or news article. The
primary objective is to determine the stance of comments
responding to the news, whether they confirm or challenge
the claim’s validity. The prediction labels typically take
the form of confirming or denying the claim. Claim-based
stance detection is a crucial approach for evaluating the
veracity of misinformation. By leveraging the stance of
replies to predict the claim’s veracity [34], this method has
been recognized as a key technique for rumor and fake news

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2015 3
TABLE 1: Target-specific stance detection datasets
Dataset-name/Authors Target(s) Source Size Time Language Annotation Classes
SemEval-2016 Task 6 [5] Atheism, Climate Change is
Concern, Feminist Movement,
Hillary Clinton, Legalization of
Abortion, Donald Trump
X (Twitter) 4,870 tweets 2016 English Favor, Against, Neither
NLPCC-2016 [19] iPhone SE, Set off firecrackers in the
Spring Festival, Russia’s
anti-terrorist operations in Syria,
Two-child policy, Prohibition of
motorcycles and restrictions on
electric vehicles in Shenzhen,
Genetically modified food, Nuclear
test in DPRK
Weibo 4,000
annotated and
2,400
unannotated
tweets
2016 Chinese Favor, Against, None
K ¨uc ¸¨uk [11] Galatasaray, Fenerbahc ¸e X (Twitter) 700 tweets 2017 Turkish Favor, Against
SemEval-2017 [7] Atheism, Climate Change is
Concern, Feminist Movement,
Hillary Clinton, Legalization of
Abortion, Donald Trump
X (Twitter) 4,870 tweets 2017 English Favor, Against, Neither
for stance; Positive,
Negative, and Neither for
sentiment
Addawood et al. [10] Individual privacy, Natural security,
Other, Irrelevant
X (Twitter) 3,000 tweets 2017 English Favor, Against, Neutral
Darwish et al. [16] Transfer of two islands from Egypt
to Saudi Arabia
X (Twitter) 33,024 tweets 2017 Arabic Favor (Positive), Against
(Negative)
Hercig et al. [20] Milo ˇs Zeman, Smoking ban in
restaurants
iDNES.cz 5,423 news
comments
2017 Czech Support, Deny, Query,
Comment
K ¨uc ¸¨uk and Can [21] Galatasaray, Fenerbahc ¸e X (Twitter) 1,065 tweets 2018 Turkish Favor, Against
Me Too dataset [22] Me Too movement X (Twitter) 9,973 tweets 2019 English Supprt, Opposition
TSE2020 [23] Donald Trump, Joe Biden X (Twitter) 2,500 tweets 2020 English Favor, Against, Neither
P-stance [3] Donald Trump, Joe Biden, Bernie
Sanders
X (Twitter) 21,574 tweets 2020 English Favor, Against, Neither
WT-WT [24] Aetna, Express Scripts, Cigna,
Humana, 21st Century Fox
X (Twitter) 51,284 tweets 2020 English Favor, Against, Neither
COVID-19-Stance [1] Anthony S. Fauci, M.D., Keeping
Schools Closed, Stay At Home
Orders, Wearing a Face Mask
X (Twitter) 7,122 tweets 2020 English Favor, Against, Neither
VAST [25] Various topics The New York
Times
23,525 tweets 2020 English Favor, Against, Neither
Mawqif [26] COVID-19 vaccine, digital
transformation, women
empowerment
X (Twitter) 4,121 tweets 2022 Arabic Favor, Against, None
C-STANCE Subtask
A [27]
Covid Epidemic, World Events,
Cultural and Education,
Entertainment and Consumption,
Sports, Rights, Environmental
Protection
Weibo 19,038 tweets 2023 Chinese Favor, Against, Neutral
ClimaConvo Task B [28] climate change objectives and
related activist movement
X (Twitter) 15,309 tweets 2024 English Support, Neutral, Oppose
EcoVerse [29] environmental topics X (Twitter) 3,023 tweets 2024 English eco-related / not
eco-related; negative,
positive, neutral;
supportive, neutral,
skepti- cal/opposing
EZ-STANCE [30] Covid Epidemic, World Events,
Education and Culture,
Entertainment and Consumption,
Sports, Rights, Environmental
Protection, and Politics
X (Twitter) 30,606 tweets 2024 English Favor, Against, Neutral
GunStance [31] Regulating guns, Banning guns X (Twitter) 5,500 tweets 2024 English In-Favor, Against,
Neutral
GenderStance [32] Gender Bias Kialo 36k sen-
tences(automatic
annotation)
2024 English In-Favor, Against, None
TABLE 2: Multi-target stance detection datasets
Dataset-name Target(s) Source Size Time Language Annotation Classes
Multi-Target Stance [8] {Clinton-Sanders},
{Clinton-Trump},
{Cruz-Trump}
X (Twitter) 4,455 tweets 2017 English Favor, Against, Neither
Trump-Hillary [33] Hillary Clinton, Donald
Trump
X (Twitter) 3,450 tweets 2017 English support Trump, attack
Trump, support Clinton,
attack Clinton,
neutral/irrelevant

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2015 4
TABLE 3: Claim-based stance detection datasets
Dataset-name/Authors Target(s) Source Size Time Language Annotation Classes
Emergent [34] Claims and news headlines snopes.com
and X
(Twitter)
300 claims
and 2,595
headlines
2016 English For, Against, Observing
PHEME [35] Claims X (Twitter),
Reddit
330 rumour
threads (4,842
tweets)
2017 English Rumours, Non-Rumours
RumourEval [36] Rumorous tweets X (Twitter),
Reddit
5,568 tweets
(4,519 + 1,049)
2017 English Support, Deny, Query,
Comment
FNC [37] News headlines FNC 49,972
annotated and
25,413
unannotate
headline-body
pairs
2017 English Agrees, Disagrees,
Discusses, Unrelated
Rohit and Singh [38] The bill/issue of the speech under
consideration
Indian
Parliament
1,201 speeches 2018 English Favor, Against for stance;
Appreciate, Blame, Call
for Action, Issue for
purpose
Baly et al. [39] Claims extracted from Web sites VERIFY &
REUTERS
402 claims
and 3,042
annotated
documents
2018 Arabic Agree, Disagree, Discuss,
Unrelated
Lozhnikov et al. [40] Claims extracted from news and
tweets
X (Twitter) 700 tweets
and 200 news
articles
2018 Russian Support, Deny, Query,
Comment
C-STANCE Subtask B [27] Covid Epidemic Weibo 29,088 tweets 2023 Chinese Favor, Against, Neutral
TABLE 4: Coversational-based stance detection datasets
Dataset-name/Authors Target(s) Source Size Time Language Annotation Classes
Lai et al. [41] 2016 referendum on reform
of the Italian Constitution
X (Twitter) 993 triplets (2,889 tweets) 2018 Italian Favor, Against, None
SRQ [42] Student Marches, Iran Deal,
Santa Fe Shooting, General
Terms
X (Twitter) 5,220 tweets 2020 English Comment, Explicit
Denial, Implicit Denial,
Explicit Support, Implicit
Support, Queries
Cantonese-CSD [43] Covid-19 Hong Kong Social media 5,876 items 2022 Cantonese Favor, Against, Neither
MT-CSD [4] Bitcoin, Tesla, SpaceX,
Donald Trump, Joe Biden
Reddit 15,876 items 2023 English Favor, Against, None
Type Sentence-level Conversation-based
Classif. Task Sentence classification Conversation history classification
Label Favor, Against, None
Work
SEM16, P-stance
COVID-19-Stance
VAST, WT-WT
SRQ Cantonese-CSD MT-CSD
Target-nums ≥4 4 1 5
Multi-turn - × ✓ ✓
English ✓ ✓ × ✓
TABLE 5: Comparison of different stance detection datasets
detection [12], highlighting its importance in assessing the
credibility of online information.
Conversational stance detection. In the domain of so-
cial media analysis, users frequently express their opinions
within conversational threads. However, traditional stance
detection techniques often struggle to accurately identify
stances in such dialogic environments due to their limited
ability to understand contextual nuances. To address this
limitation, coversational-based stance detection tasks have
been proposed [43]. Typically, these tasks involve predicting
the stance polarity of a given tweet (or statement) based on
the conversation history, the current tweet (or statement),
and the stance target.
Multi-modal stance detection. With the rapid evolution
of social media, users increasingly express their opinions
not only through text, but also through diverse multime-
dia content, such as audio, images, videos, and emojis.
To address this trend, multi-modal stance detection has
emerged as a research area, aiming to predict stance polarity
by integrating various data forms, including text, images,
videos, and audio.
User-level stance detection. The user-level stance de-
tection task involves predicting a user’s stance towards a
given topic. In this context, various user attributes can be
integrated with the text of their posts to enhance the predic-
tive model [14, 54]. Notably, most studies in this area have
adopted a binary classification approach, categorizing users’
stances into two polarized classes: support and against [16].
This simplification is often justified by the assumption that
users will exhibit a clear stance, even if their posts appear
neutral.
2.2 Method Development Perspective
From a method development perspective, this section pro-
vides a detailed introduction to several task categorization
approaches.
In-target stance detection. In the early stages of stance
detection research, the in-target stance detection task was
the most extensively studied task. This task is closely related
to the development of text classification techniques. The in-
target stance detection task involves training and inferring
stance detection models on the same target. Over the years,
a large body of work has focused on this task, exploring

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2015 5
TABLE 6: Multi-modal stance detection datasets
Dataset-name Target(s) Source Size Time Language Annotation Classes Modal
Levow et al. [44] Decisions on item placement
(inventory task) and
whether to fund or cut
expenses (budget task) in a
superstore
Spontaneous speech ∼7.6 hours 2014 English No Stance, Weak Stance,
Moderate Stance, Strong
Stance, Unclear for stance;
Positive, Negative, Neutral,
Unclear for polarity
aural
MMVAX-STANCE [45] Covid-19 X (Twitter) 4,870 tweets 2023 English Accept, Reject, No Stance,
Not Relevant
visual
MSDD [46] Various topics Friends and The Big Bang
Theory
1,296 video 2023 English Postitive, Negative, Neutral visual, aural
MMSD [47] Twitter Stance Election,
COVID-CQ, MWTWT,
Russo-Ukrainian Conflict,
Taiwan Question,
X (Twitter) 17,544 tweets 2024 English Favor, Against, Neutral visual
MmMtCSD [48] Bitcoin, Tesla, Post-T Reddit 21,340 items 2024 English Favor, Against, None visual
TABLE 7: Multilingual stance detection datasets
Dataset-name/Authors Target(s) Source Size Time Language Annotation Classes
IberEval-2017 [49] Independence of Catalonia X (Twitter) 5,400 tweets
in Spanish
and 5,400
tweets in
Catalan
2017 Catalan and Spanish Favor, Against, None
Swami et al. [50] Demonetisation in India in
2016
X (Twitter) 3,545 tweets 2018 English-Hindi Favor, Against, None
MultiStanceCat [51] Catalan Referendum X (Twitter) 11,398 tweets 2018 Catalan and Spanish Favor, Against, Neither
X-Stance [52] 175 communal, cantonal and
national elections between
2011 and 2020
Smartvote 67,000
comments
2020 German and French Favor, Against
various approaches and methodologies. The task is formally
defined as:
Let X = {xi, qi}N i=1 represent the labeled data collec-
tion, where x refers to the input text and q corresponds
to the target. N denotes the total number of instances
in X. Each sentence-target pair (x, q) ∈ X is assigned a
stance label y. In-target stance detection aims to predict
the stance label for x towards target q.
Cross-target stance detection. In real-world applica-
tions, obtaining rich annotated data for each target is a
time-consuming and labor-intensive process. Conventional
stance detection methods struggle to generalize well across
targets. Cross-target stance detection [55] aims to infer the
attitude towards a target by leveraging a large amount of
annotated data from another target. Typically, most works
in this area focus on targets within the same domain, such as
Trump and Hillary in the politics domain. However, some
studies also explore cross-domain stance detection, where
the source and target domains differ, such as training on
Trump data and inferring stance on feminist movement
data. This approach enables the model to generalize stance
detection across different domains and contexts. The task is
formally defined as:
Let X s = (xs i , qs i )N s i=1 denote the labeled dataset in the
source domain, where each tuple (xs i , qs i ) consists of
an input text xs i and its corresponding target qs i . The
dataset contains N s instances, each associated with a
stance label ys. Given an input sentence xd and a target
qd in the target domain, the goal of cross-target stance
detection is to predict the stance label for xd towards qd
by leveraging the model learned from the labeled data
X s in the source domain.
Zero-shot stance detection. In real-world applications,
test data often involves unseen targets during training. As
a special case of cross-target stance detection, the zero-
shot stance detection Task involves training a model on
annotated data from a specific target and directly predicting
the stance on unseen targets. Pioneering work by Allaway
and McKeown [25] first introduced the zero-shot stance de-
tection task and proposed the VAST dataset, which contains
a large number of targets with no overlap between training
and testing targets. Furthermore, some studies have begun
to explore open-domain zero-shot stance detection, aiming
to simulate real-world scenarios and reduce the need for
training samples. The task is formally defined as:
Let X s = ( xs i , qs i )N s i=1 denote the labeled dataset in
the source domain, where each tuple (xs i , qs i ) consists
of an input text xs i and its corresponding target qs i .
X d = (xd i , qd i ) N d i=1 denote a set of unlabeled instances
towards unseen or testing targets. Note that there is
no overlap between X s and X d. The aim of zero-shot
stance detection is to train a model from each sentence
xs i towards the source known target qs i from X s, and
infer the stance polarity for each sentence xd i towards
an unseen target qd i in X d.
Cross-lingual stance detection. In today’s globalized
world, understanding and analyzing stances in multiple
languages is crucial, particularly given the linguistic diver-
sity of online platforms such as social media, forums, and
news websites. However, traditional monolingual stance
detection methods often fall short in multilingual applica-
tions due to language and cultural variations. This has led
to the development of multilingual stance detection tasks,
which aim to expand the scope and applicability of stance
detection research [50]. The task is formally defined as:

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2015 6
Let X s = ( xs i , qs i , ls i )N s i=1 denote the labeled dataset
in the source language, where each tuple (xs i , qs i , ls i )
consists of an input text xs i , its corresponding target qs i ,
and the language label ls i . X t = (xt i, qt i , lt i)N t i=1 denote
a set of unlabeled instances in the target language.
Note that there is no overlap between X s and X t, and
ls i ̸= lt i. The aim of cross-lingual stance detection is
to train a model from each sentence (xs i towards the
source known target qs i from X s, and infer the stance
polarity for each sentence xt i towards an unseen target
qt i in X t, despite the language difference between ls i
and lt i.
3 S TANCE DETECTION DATASETS
This section provides a comprehensive overview of existing
stance detection task datasets, presented in the order of their
release.
3.1 Target-Specific Datasets
As discussed earlier, target-specific stance detection is the
most widely studied task in this field. Therefore, a large
number of datasets have been made available, including
multi-modal and multilingual resources.
Among these, the SemEval stance detection dataset
SemEval-2016 task 6 [5] is the most widely used, providing
two sub-datasets to support both supervised (Task A) and
weakly supervised (Task B) frameworks. It contains 4,870
labeled tweets. NLPCC-2016 is the first widely used Chinese
benchmark dataset, collected from Weibo. It contains 4,000
labeled sentences [19]. P-stance dataset [3] was introduced
for the political domain, featuring three targets (Donald
Trump, Joe Biden, and Bernie Sanders) and collected during
the 2020 US presidential election. The WT-WT dataset [24]
is one of the largest manually annotated datasets, covering
multiple domains and containing 51,284 annotated samples.
The COVID-19-Stance dataset [1] focuses on the public
health domain, with targets such as Anthony S. Fauci, M.D.,
and policies like Keeping Schools Closed and Wearing a
Face Mask, comprising 7,122 samples. Furthermore, the EZ-
STANCE dataset [30] expands the scope to various domains,
including Covid Epidemic, World Events, Education and
Culture, Entertainment and Consumption, Sports, Rights,
Environmental Protection, and Politics, with 30,606 anno-
tated samples. A more detailed description of these datasets
can be found in Table 1.
3.2 Multi-Targets Datasets
Multi-target stance detection datasets primarily focus on the
political domain, such as the US presidential election. Two
notable datasets are the Multi-targets dataset [8] and the
Trump vs. Hillary dataset [33]. The Multi-targets dataset in-
volves annotating each tweet with stance labels for both can-
didates simultaneously, with target pairs including Clinton-
Sanders, Clinton-Trump, and Cruz-Trump. The labels used
are Favor, Against, and Neither. Similarly, the Trump vs.
Hillary dataset annotates each tweet with stance labels for
both candidates, such as supporting Hillary and opposing
Trump. A more detailed description of these datasets can be
found in Table 2.
3.3 Claim-based Datasets
In stance detection datasets, the target is typically a single
statement, such as a tweet post. The Emergent dataset [34]
consists of claims extracted from rumor sites and X (Twit-
ter), comprising 300 claims and 2,595 corresponding head-
lines. The RumourEval dataset [36] is a claim-based stance
detection dataset designed for rumor resolution, comprising
5,568 tweets from X platform and Reddit. Each rumor tweet
is evaluated against a set of other tweets to determine the
stance of these tweets in supporting or denying the source
of the rumor. Additionally, the FNC dataset [37] targets
news headlines, with 49,972 annotated labels and 25,413
unannotated headline-body pairs. Rohit and Singh [38] ex-
tracted 1,200 samples from the Indian Parliament dataset,
focusing on the target of “The bill/issue of the speech
under consideration”. Multilingual datasets have also been
developed, such as the SemEval 2019 rumors detection
dataset [56], which extends the SemEval 2017 dataset by
adding new data from Reddit and incorporating Russian as
a new topic. Baly et al. [39] developed the Russian dataset,
and C-STANCE Subtask B is the Chinese dataset collected
from Weibo. A more detailed description of these datasets
can be found in Table 3.
3.4 Coversational-based Datasets
Recent years have seen a growing interest in conversational
stance detection datasets focused on social media comment
data. One of the first datasets is proposed by Lai et al.
[41], which explores the 2016 referendum on the reform
of the Italian Constitution. The SRQ dataset [42], collected
from the X platform, contains 5,220 tweets with a primary
focus on single-round reply conversations. The Cantonese-
CSD dataset [43], sourced from a Hong Kong social media
platform, targets Covid-related discussions in Cantonese.
The MT-CSD dataset [4] is currently the largest and most
in-depth conversational stance detection dataset, featuring
multiple targets such as “Bitcoin, Tesla, SpaceX, Donald
Trump, and Joe Biden”, with a total of 15,876 annotated
samples. A detailed description of the dataset is provided
in Table 4. Additionally, we present a comparison between
conversation-level and sentence-level stance detection in
Table 5.
3.5 Multi-Modal Datasets
The earliest multi-modal stance detection dataset, proposed
by Levow et al. [44], focused on spontaneous speech au-
dio data, with targets including decisions on item place-
ment and budget allocation in a superstore. The MMVAX-
STANCE dataset [45], comprising 4,870 tweets, targets
Covid-19 and incorporates visual information. The MSDD
dataset [46], sourced from TV shows Friends and The Big
Bang Theory, contains 1,296 video clips with multiple tar-
gets. The MMSD dataset [47], collected from X platform, in-
cludes 17,544 tweets with targets such as X (Twitter) Stance
Election, COVID-CQ, MWTWT, Russo-Ukrainian Conflict,
and Taiwan Question. The MmMtCSD dataset [48] is the
first multi-modal, conversational stance detection dataset,
featuring text, image, and video modalities, with 21,340
items. Detailed information is presented in Table 6.

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2015 7
TABLE 8: User-level stance detection datasets
Dataset-name/Authors Target(s) Source Size Time Language Annotation Classes
Darwish et al. [57] Kavanaugh, Trump,
Erdogan
X (Twitter) 72690 user
(automatic
annotation)
2020 Kavanaugh
and Trump
dataset
(English),
Erdogan
dataset
(Turkish)
pro, anti
Elzanfaly et al. [58] tweet and article X (Twitter) 32,905 user 2022 English, Unsupervised task
Zhang et al. [59] Joe Biden, Donald Trump X (Twitter) 1,123,749
tweets
(automatic
annotation)
2024 English pro-Trump, pro-Biden
3.6 Multilingual Datasets
In the previous section, we introduced several datasets from
different languages. This section focuses on datasets that
encompass multiple languages for stance detection tasks.
For instance, the IberEval-2017 dataset [49] contains 5,400
tweets in Spanish and 5,400 tweets in Catalan, with the
goal of determining the independence of Catalonia. Swami
et al. [50] introduced an English-Hindi language dataset
consisting of 3,545 tweets. The MultiStanceCat dataset [51]
is annotated with the Catalan Referendum as the target,
comprising 11,398 tweets from 2018 in both Catalan and
Spanish languages. The X-Stance dataset [52] is a German
and French dataset, consisting of 67,000 comments. Detailed
information is provided in Table 7.
3.7 User-level Datasets
Due to the challenges of manual annotation, user stance
detection datasets often employ automatic annotation meth-
ods, such as leveraging hashtags from social media plat-
forms. For instance, Darwish et al. [57] utilized automatic
annotation to label 72,690 users with respect to their stances
on Kavanaugh, Trump, and Erdogan. Elzanfaly et al. [58]
proposed an unsupervised task involving 32,905 users.
Zhang et al. [59] constructed a dataset in the political
domain, focusing on Joe Biden and Donald Trump as tar-
gets, and employed automatic annotation to label 1,123,749
tweets. The details of these datasets are presented in Table 8.
4 T RADITIONAL STANCE DETECTION ALGO -
RITHMS
As mentioned earlier, the development of stance detection
models is closely related to the advancement of text classi-
fication models. Various approaches have been employed
to model and train stance classifiers. Fig. 1 presents the
evolution of methods. In this section, we review traditional
stance detection methods, including early machine learning-
based approaches, conventional deep learning methods,
fine-tuning methods based on pre-trained models, and
prompt-based fine-tuning methods for stance detection.
4.1 Feature-Based Machine Learning Approaches
Early stance detection methods primarily relied on tradi-
tional machine learning approaches. Their basic framework
is illustrated in Fig. 2 (a). First, a feature identifier is con-
structed to recognize important features, followed by the
development of a traditional machine learning model to
achieve classification and prediction. The mainstream meth-
ods can be broadly categorized into several types, including
Support Vector Machines (SVMs), logistic regression, deci-
sion trees, and k-Nearest Neighbors (KNN).
Among these methods, SVMs are the most widely em-
ployed approach for stance detection. They have been used
in over 40 studies, either as the primary approach or as
a baseline for comparison with other methods. Notable
examples of studies that have utilized SVMs for stance
detection include [10], [60], and [61].
Logistic regression is another popular approach for
stance detection, appearing in over 15 studies. This method
has been used in various forms, including as a standalone
classifier and as part of an ensemble classifier. Examples
of studies that have employed logistic regression for stance
detection include [34], [62], and [63].
Decision trees and random forests are also commonly
used approaches for stance detection. Decision trees have
been employed in several studies, including [10] and [64].
Random forests, which are ensemble classifiers based on
decision trees, have been used in studies such as [11] and
[65].
Finally, artificial neural networks (ANNs) have also been
applied to stance detection tasks. Examples of studies that
have used ANNs for stance detection include [66] and
[63]. Specifically, classifiers based on Multilayer Perceptron
(MLP) have been successfully applied to stance detection
tasks in studies such as [67] and [68]. Detailed information
is provided in Table 9.
4.2 Traditional Deep Learning Approaches
The development of deep learning techniques in stance
detection has been marked by several significant advance-
ments, each contributing uniquely to the field.
One notable example is the Long Short-Term Memory
(LSTM) network, introduced by Hochreiter and Schmidhu-
ber in 1997, which has been widely adopted in over ten stud-
ies. The LSTM’s ability to capture long-term dependencies
in text data has consistently yielded superior results, making
it a preferred choice for stance detection tasks. Following the
LSTM, Convolutional Neural Networks (CNNs) have also
been extensively employed, with notable contributions from
studies including Sobhani et al. [8], Lynn et al. [54], Zarrella

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2015 8
TABLE 9: Feature-based machine learning approaches
Study Task Features Approach Dataset
Rajadesingan and Liu [69] target-specific unigrams, bigrams and trigrams Naive Bayes Debate
Dias and Becker [70] target-specific n-gram and sentiment SVM SemEval-2016
Krejzl and Steinberger [71] target-specific hashtags, n-grams, tweet length,
Part-of-speech, General Inquirer,
entity-centered sentiment dictionaries,
Domain Stance Dictionary
Maximum entropy classifier SemEval-2016
Ebrahimi et al. [72] target-specific n-gram and sentiments Discriminative and generative
models
SemEval-2016
Elfardy and Diab [73] target-specific Lexical Features, Latent Semantics,
Sentiment, Linguistic Inquiry, Word Count
and Frame Semantics features
SVM SemEval-2016
Siddiqua et al. [74] target-specific Tweets content SVM Tree Kernel SemEval-2016
Lai et al. [75] target-specific Sentiment, opinion target, structural
features (hashtags, mentions, punctuation
marks), text-Based features
Gaussian Naive Bayes classifier SemEval-2016
Aldayel and Magdy [76] target-specific Networks features SVM SemEval-2016
Aker et al. [77] claim-based Linguistic, message-based, and topic-based
such as (Bag of words, POS tag, Sentiment,
Named entity and others
Random Forest, Decision tree and
Instance Based classifier (K-NN)
RumourEval, PHEME
TABLE 10: Traditional deep learning approaches
Study Task Features Approach Dataset
Zarrella and Marsh [78] target-specific word2vec and hash-tags LSTM SemEval-2016
Wei et al. [79] target-specific Content and Sentiment lexicon BiLSTM SemEval-2016
Igarashi et al. [17] target-specific Reply, BagOfWord, BagOfDependencies,
POS tags Sentiment WordNet, Sentiment
Word Subject, Target Sentiment and
Point-wise Mutual Information
CNN SemEval-2016
koc [80] claim-based word2vec, Tweet lexicon, Punctuation,
Attachments,Relation to other tweets,
Content length and Tweet role.
Branch-LSTM RumourEval
Sobhani et al. [8] multi-target word vectors Bidirectional RNN Multi-Target Stance
Wei et al. [81] target-specific Content, Noisy stance labeling and Topic
Modeling
BiGRU SemEval-2016
Zhou et al. [82] target-specific word embeddings Bi-directional GRU-CNN SemEval-2016
Vinayakumar et al. [83] multilingual Word embeddings RNN, LSTM, GRU, and logistic
regression
MultiStanceCat
Ambrosini and Nicol `o [84] multilingual Word embeddings LSTM, bidirectional LSTM, CNN MultiStanceCat
Siddiqua et al. [85] multi-target Tweets content Multi-kernel convolution and
attentive LSTM
Multi-Target Stance
Lynn et al. [54] target-specific word2vec RNN SemEval-2016
SEKT [86] target-specific Tweets content, ,semantic and emotion
lexicons
LSTM + GCN SemEval-2016
TABLE 11: Pre-trained language models (PLMs)
Study Task Features Approach Dataset
Bert-GCN [87] target-specific Tweets content, commonsense
knowledge graph
Bert + GCN VAST
Li et al. [3] target-specific Word Embedding BERTweet(Pre-train Bert) P-stance
Hardalov et al. [88] target-specific Word Embedding Roberta + MoE + DANN SemEval-2016, VAST,
WT-WT
TarBK [89] target-specific Tweets content, targeted
background knowledge from
Wikipedia
Bert SemEval-2016, VAST,
WT-WT
WS-BERT [90] target-specific Word Embedding, Encoding
Wikipedia Knowledge
Bert + BertTweet COVID-19-Stance,
P-stance
JointCL [91] target-specific Word Embedding Bert + Contrastive Learning +
Clustering + GAT
SemEval-2016, VAST,
WT-WT
Branch-Bert [43] Coversational-based Word Embedding, Conversation
structure
Bert + CNN Cantonese-CSD
Zhang et al. [92] target-specific Word Embedding, Knowledge
Graph
RoBERTa + bidirectional conditional
encoding layer + Node2Vec
SemEval-2016, VAST
GLAN [4] Coversational-based Word Embedding, structural Graph Bert + CNN + GCN MT-CSD
MSFR [93] target-specific Tweets content Bert WT-WT,VAST
MPT [94] target-specific Tweets content, prompt framework Bert+prompt learning SemEval-2016, VAST
KEPrompt [95] target-specific Tweets content, prompt framework,
external lexicons
Bert+prompt learning SemEval-2016, VAST
TMPT [47] Multi-modal Word Embedding, Image
Embedding
Bert + Vit + prompt learning MMSD
TCP [96] target-specific Tweets content, prompt framework RoBERTa + prompt learning SemEval-2016, P-stance

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2015 9
Method
K-NN(1967)
Cover, Thomas, and Peter Hart
SVM(1998)
Burges, Christopher JC
Naive Bayes(1973)
Hart et al.
Rajadesingan and
Liu(2014)
Naive Bayes
unigrams, bigrams and
trigrams
Krejzl and Steinberger
(2016)
Maximum entropy classifier
hashtags, n-grams, tweet
length.....
Lai et al. (2017)
Gaussian Naive Bayes
Sentiment, opinion target,
structural features
Aker et al.(2017)
Random Forest, Decision tree,
K-NN Linguistic, message-
based, and topic-based
Dias and Becker (2016)
SVM
n-gram and sentiment
Siddiqua et al.  (2016)
SVM Tree Kernel
Tweets content
LSTM(1997)
Sepp Hochreiter &
Jürgen Schmidhuber
Attention(2014)
Volodymyr Mnih et al.
CNN(1998)
Yann LeCun et al.
GRU(2014)
Junyoung Chung et al.
GNN(2008)
Franco Scarselli et al.
RNN(1990)
Jeffrey L. Elman
Method Zarrella and Marsh(2016)
LSTM
word2vec and hash-tags
Igarashi et al.(2016)
CNN
Reply, BagOfWord, Bag Of
Dependencies, POS tags...
Wei et al.(2016)
Bi-directional GRU
Content, Noisy stance labeling
and Topic Modeling
Lynn et al. (2019)
RNN
word2vec
Zhou et al.(2017)
Bi-directional GRU-CNN
word embeddings
Vinayakumar et al. (2017)
RNN, LSTM, GRU, and logistic
regression
Word embeddings
Ambrosini and Nicolo(2017)
Bi-directional LSTM
word embeddings
Siddiqua et al. (2019)
Multi-kernel convolution and
attentive LSTM
Tweets content
Model
GPT(2018)
Alec Radford et al.
Bert(2018)
Jacob Devlin et al.
ERNIR(2019)
Yu Sun et al.
Roberta(2019)
Yinhan Liu et al.
ViT(2010)
Alexey Dosovitskiy et al.
Fine-
tuning
Prompt-
tuning
Bert-GCN(2021)
Bert, GCN
Tweets content, commonsense
knowledge graph
Hardalov et al.(2021)
Roberta, MoE, DANN
Word Embedding
JointCL(2022)
Bert, Contrastive Learning,
Clustering, GAT
Word Embedding
Branch-Bert(2022)
Bert, CNN
Word Embedding, Conversation
structure
GLAN(2024)
Bert, CNN
Word Embedding,
structural Graph
MPT(2021)
Bert
Tweets content, Prompt
framework
KEPrompt (2022)
Bert
Tweets content, Prompt framework,
External lexicons
TMPT(2024)
Bert + Vit
Word Embedding, Image
Embedding
TCP(2024)
Roberta
Tweets content, Prompt
framework
Model
COLA(2024)
Three-stage CoT
DEEM(2024)
Two-step CoT
Fraile-Hernandez and Penas(2024)
Llama 2 7B
MLLM-SD(2024)
Llama 2 7B LoRA + ViT
ChatGPT(2022)
OpenAI
Claude(2023)
Anthropic
LLAMA(2023)
Meta AI
Grok(2024)
X (Twitter) AI
Vicuna(2023)
Meta AI
LoRA
Edward J. Hu et al.
Ilker Gul et al.(2024)
LLaMa-2 LoRA and Mistral-7B
DS-ESD(2024)
ChatGPT, Bart, Bert
EDDA(2024)
ChatGPT, Bert
MB-Cal(2024)
ChatGPT, GAT
CoT
Jason Wei et al.
Machine Learning
Deep Learning
Large Language Models
Pre-trained Language Models
Times
Fig. 1: The taxonomy of stance detection methods.
TABLE 12: Approaches based on large language models
Study Task Approach Dataset
KASD [97] target-specific LLM(CoT) + Bert SemEval-2016, P-Stance, COVID-19-Stance, VAST
EDDA [98] target-specific LLM(CoT) + Bert SemEval-2016, VAST
COLA [99] target-specific three-stage LLM (CoT) SemEval-2016, P-Stance, VAST
MB-Cal [100] target-specific LLM(CoT) + GAT SemEval-2016, VAST
DS-ESD [101] target-specific LLM(CoT) + Bart +Bert SemEval-2016, COVID-19-Stance, VAST
SQBC [102] multilingual LLM (CoT) + Bert X-Stance
Fraile-Hernandez and
Pe˜nas [103]
target-specific Llama 2 7B LoRA ClimaConvo Task B
G ¨ul et al. [104] target-specific LLaMa-2 LoRA and Mistral-7B
LoRA
SemEval-2016
DEEM [105] multi-target two-step LLM P-stance, SemEval-2016, Multi-Target Stance
Taranukhin et al. [106] target-specific LLM(CoT) SemEval-2016, WT-WT, COVID-19-Stance
KAI [107] target-specific LLM(CoT) + Bert SemEval-2016, P-Stance, VAST
MPPT [108] target-specific LLM(CoT) + Bert + prompt learning SemEval-2016, VAST
LKI-BART [109] target-specific LLM(CoT) + Bart P-Stance, VAST
MLLM-SD [48] Multi-modal Llama 2 7B LoRA + ViT MmMtCSD
TR-ZSSD [110] target-specific LLM(CoT) SemEval-2016, CoVaxFrames, MMVax-Stance
and Marsh [78], koc [80]. CNNs have proven effective
in extracting spatial hierarchies of features, making them
well-suited for processing structured text data [17]. The
advent of attention mechanisms has further enhanced the
performance of stance detection models, mitigating issues
such as the LSTM’s limited long-term memory capacity.
Attention-based approaches have garnered significant at-
tention, with notable examples including the combination
of LSTM and attention mechanisms, as well as CNNs with
attention mechanisms [79, 85]. The attention mechanism
has increased the association between stance targets and
informative words or phrases, leading to improved accuracy
in stance detection.
Furthermore, text classification methods based on Graph
Convolutional Networks (GCNs) have also contributed to
the advancement of stance detection [86, 111, 112]. The
graph-based approach can effectively integrate syntactic tree
structures and contextual knowledge of text and stance tar-
gets, thereby enhancing the performance of stance detection
models.
As illustrated in Fig. 2 (b), the overall framework of these
works can be divided into three primary steps: (1) Vector-
ization of text and target features: first, the input text and
target features are converted into vectors using word em-
bedding techniques, such as GloVe [113] or Word2Vec [114].
(2) Construction of deep learning stance models: next, a
deep learning model is built to analyze the stance of the
text. (3) Design of loss function and model training: Finally,

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2015 10
(a) Feature-Based Machine
Learning Approaches
(b) Traditional Deep Learning
Approaches.
Fig. 2: Framework of traditional methods.
Fig. 3: Framework of fine-tuning approaches.
an appropriate loss function is designed, and the model
is trained and optimized through backpropagation using
a large number of annotated samples. A list of specific
methods is provided in Table 10.
4.3 Fine-Tuning Stance Detection Methods
The advancement of deep learning techniques has led to
significant performance improvements in text classification
tasks using pre-trained language models (PLMs). As a re-
sult, PLMs have gained considerable attention in stance
detection research. One effective approach is fine-tuning,
which involves reformatting the input tweet and target into
a new format, such as “ <CLS> Tweet <SEP> Target”,
and then feeding it into a PLM to obtain the hidden state
vector at the CLS position. This is followed by designing a
loss function and training the model using labeled samples
through backpropagation. The basic structure is shown in
Fig. 3.
To enhance the applicability of PLMs in stance detec-
tion, some methods draw inspiration from the pre-training
process of PLMs and retrain the PLM on additional social
media data. For example, He et al. [90] retrained a PLM
on social media tweet data. Another approach is to use
frozen PLM parameters, which is a common method due
to its efficiency and minimal computational overhead. By
adjusting a small portion of the model parameters and keep-
ing the remaining parameters unchanged, PLMs can adapt
to stance detection tasks while minimizing computational
costs and data requirements [99, 100, 104]. This method
typically involves adding additional neural network layers
Fig. 4: Framework of prompt-tuning approaches.
on top of the CLS hidden state vector and only learning the
additional parameters during training.
Some studies have also combined PLMs with traditional
neural networks, such as RNNs and CNNs, to leverage the
strengths of both approaches [4, 43]. Furthermore, incor-
porating attention mechanisms with fine-tuning methods
has been shown to significantly improve stance detection
performance, leading to a large body of work focused on
customizing attention mechanisms to address specific prob-
lems. A list of specific methods is provided in Table 11.
4.4 Prompt-Tuning Stance Detection Methods
Prompt-tuning is an improvement over fine-tuning methods
for stance detection. This approach formulates the stance
detection task as a masked language modeling task. Specif-
ically, prompt-tuning combines the given post and target
with a template, typically written as “The attitude to the
<Target> is [MASK]”. The template is then packed with the
input, and then fed into a PLM. Subsequently, the hidden
state at the mask position generates a prediction probability.
This probability corresponds to a word or phrase defined
in a verbalizer. The basic structure is shown in Fig. 4.
To enhance performance, Huang et al. [95] proposed a
method for automatically constructing a verbalizer tailored
to the stance detection task. Wang and Pan [96] is a flexible
prompt-tuning approach that can be applied to various
domains, thanks to its target-adaptive nature. To address the
challenge of multi-modal stance detection, Liang et al. [47]
further introduced a visual prompt model. A list of specific
methods is provided in Table 11.
5 A PPROACHES BASED ON LARGE LANGUAGE
MODELS
Recently, the release of GPT-3.5 in November 30, 2022 has
sparked significant interest in LLMs, such as the GPT-
series, which have demonstrated impressive zero-shot per-
formance on commonsense reasoning tasks [115]. This has
led to a new research direction in stance detection, focusing
on utilizing LLMs. The way LLMs are employed has a
substantial impact on the construction of stance detection
models. A list of specific methods is provided in Table 12.
5.1 LLM-as-Predictors
Utilizing their extensive internal knowledge and emerging rea-
soning abilities for stance detection.

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2015 11
Fig. 5: Framework of zero-shot prompt methods.
Fig. 6: Framework of chain-of-thought prompt method from
[116].
LLM-as-Predictors methods aim to leverage the inher-
ent reasoning capabilities of LLMs by providing direct
prompts, thereby treating LLMs as efficient knowledge ex-
perts [97, 99, 117]. This approach enables the prediction of
user stance without requiring training samples or further
model training, making model deployment more efficient.
Zero-shot prompt method : Zhang et al. [117] first pro-
posed a zero-shot prompting method for stance detection,
which is a simple yet effective approach. By crafting inquiry
instructions, the LLM is directly asked to predict the stance
polarity of the input. Experimental results demonstrate that
this approach can achieve satisfactory stance detection ac-
curacy. Fig. 5 illustrates the framework architecture.
Chain-of-Thought prompt method : Building on the
Fig. 7: Framework of background knowledge integrated
prompt method from [97].
zero-shot prompting method, Zhang et al. [116] proposed a
one-shot stance detection method based on thought chains.
Fig. 6 shows the framework. By providing a pre-defined ex-
ample for the LLM to learn from, the model is then asked to
predict the stance of the input through inquiry. Experiments
show that providing a single example significantly improves
the model’s prediction accuracy. This method also provides
a potential prompting approach for future work.
Background knowledge integrated prompt method : Li
et al. [97] divides the prompting process into two stages, first
acquiring the LLM’s knowledge of the background through
prompting, and then feeding the background knowledge
and input into a second-stage LLM to predict stance polarity
(Fig. 7). Weinzierl and Harabagiu [110] further extends the
prompting method to the multi-modal domain, demonstrat-
ing the effectiveness of prompting learning methods.
5.2 LLM-as-Enhancers
Augmenting data and existing approaches with enhanced external
knowledge and analytical prowess.
Several studies argue that even LLMs often lack suffi-
cient domain-specific knowledge to complete tasks, and the
world knowledge embedded in LLMs can become outdated
over time. Therefore, some works explore using sample
prompts to elicit stance detection-related knowledge from
LLMs, and then combine it with traditional deep learning
methods, fine-tuning methods, or prompt-tuning methods
to improve stance detection accuracy. We refer to this ap-
proach as LLM-enhanced fine-tuning methods [107–109].
This type of method typically involves at least two stages:
first, it uses prompt learning to acquire relevant background
knowledge; then, it inputs the acquired knowledge along
with the original text into a trainable stance detection model.
This approach effectively combines the reasoning capabil-
ities of LLMs with the learning capabilities of annotated
samples, enhancing the model’s zero-shot learning ability.
In the work of Li et al. [97], in addition to directly
prompting the model to acquire background knowledge
and subsequently feeding it into the LLM to obtain the
final stance (as mentioned above), the authors also proposed
a fine-tuning approach in the second stage. Specifically,
the extracted background knowledge is combined with the
input tweet and target, and then fed into the fine-tuning
method, which leverages labeled samples to learn through
backpropagation.
The MPPT method [108] further expands the utilization
of LLM knowledge by leveraging the CoT approach to
extract the LLM’s analysis of different perspectives on a
target. Fig. 8 shows the framework. For example, for the
target “Trump”, the analysis perspectives might include
“politician, president, and Republican party member, etc.”.
These perspectives can be regarded as domain-invariant
knowledge that can be transferred to other targets, such
as “Hillary”. By incorporating the perspective information
into the prompt-based fine-tuning method, MPPT enhances
the accuracy and generalizability of stance detection across
multiple targets.
KAI [107] further extends the idea of leveraging LLMs
to enhance reasoning by explicitly representing the logic
of stance prediction using first-order logic rules. It is then

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2015 12
Fig. 8: Framework of MPPT [108].
Fig. 9: Framework of KAI [107].
combined with fine-tuning methods to improve the inter-
pretability and accuracy of stance detection. Fig. 9 shows
the framework. EDDA [98] expands the generality of stance
detection tasks by proposing a data augmentation-based
approach. Using first-order logic rules as the foundation
for data augmentation, EDDA generates new tweet-category
sample pairs through prompt-based learning. Furthermore,
by incorporating first-order logic rules as external knowl-
edge, EDDA significantly improves the accuracy of current
stance detection methods when combined with traditional
fine-tuning models.
5.3 LLM-as-Agents
Transcending conventional roles to actively engage in and trans-
form stance detection.
The COLA [99] model views the LLM as an agent and
enhances stance detection accuracy by allowing multiple
independent LLMs to interact through prompting. Building
upon COLA, the DEEM method[105] further extends this
approach by leveraging generated expert representations
to facilitate semi-parametric reasoning in LLMs, thereby
increasing the generalizability and reliability of the experts.
Fig. 10 shows the framework. In this kind of approach,
LLMs are assigned three roles: linguistic expert, domain
specialist, and social media veteran. Each role analyzes the
text from a distinct perspective, focusing on syntax and
Fig. 10: Framework of multi-agent prompt method from
[105].
diction, characters and events, and platform-specific termi-
nology, respectively. The combined insights from these roles
help identify stance indicators in the text. Next, advocates
for each potential stance category present arguments based
on evidence from the preceding phase, forcing the LLMs
to discern the latent logic connecting textual features and
actual stances. The stance conclusion stage then determines
the text’s stance, integrating insights from both the text itself
and the debates.
6 D ISCUSSIONS AND FUTURE WORK
Building on previous work, we observe that the rapid ad-
vancement of LLMs has significantly improved the accuracy
of traditional methods, achieving F1 scores of 80% or higher
on various tasks. This prompts us to predict that future
research will move beyond current single-text or multi-
modal content-level stance detection methods, expanding
into more complex and realistic application scenarios. From
the perspective of LLMs, we re-examine the development
trajectory of stance detection tasks and propose several
potential avenues for future research.
6.1 Specializing in Social Media-Specific Data for
Stance Detection
Future research in stance detection should prioritize the
development of datasets that more accurately reflect the
complexities of real-world social media content. Social me-
dia platforms feature diverse and evolving content, posing
a challenge for researchers to create datasets that accurately
capture these characteristics. Although existing multi-modal
and multi-turn dialogue stance detection datasets have par-
tially simulated social media interactions, they are limited
in number and scope. This highlights the need for future
research to develop more comprehensive datasets that cover
a broader range of social media formats, including com-
ments, community interactions, and user-generated multi-
media content such as images, videos, and text. The de-
velopment of such datasets faces several challenges. Firstly,
the high heterogeneity and dynamic nature of social media
data make it difficult to extract useful information. Users’

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2015 13
expression styles are diverse and constantly evolving with
social media trends. Secondly, annotating such data requires
a significant amount of precise and labor-intensive work,
and current automated annotation tools are insufficient for
handling such complex data. Therefore, researching and
developing efficient data processing and annotation tech-
niques that can adapt to these new forms of data is essential
for future research.
6.2 Real-Time Stance Detection
Currently, most stance detection tasks focus on static data
from social media. However, in real-time stance detection,
the primary goal is to immediately capture public opinion
during live events such as political debates or breaking
news. This requires continuously updating models to reflect
current trends and sentiment shifts, enabling organizations
to make timely decisions based on public reactions.
However, achieving real-time analysis poses several
challenges. A major difficulty is handling the vast amounts
of data streaming from social media and other platforms.
Algorithms must be both fast and efficient, processing large
volumes of data without compromising accuracy. Addition-
ally, filtering out irrelevant or noisy data is crucial to ensure
that analysis remains reliable and meaningful.
Another challenge is ensuring that models adapt to the
rapid evolution of public discourse. As opinions change,
models must remain accurate and relevant, which requires
continuous updates and improvements. Scalability is also
a concern, as systems need to effectively handle varying
data loads and adapt to different languages or regions.
Addressing these challenges is essential for effective real-
time stance detection.
6.3 User-Level Stance Detection
Existing research on stance detection primarily focuses on
content-level analysis, but user-level stance detection is
crucial for understanding individuals’ sustained attitudes
towards various topics. To our knowledge, only two studies
have explored user-level stance detection, both using non-
human-annotated datasets, revealing the potential value
and research gap in this area. The goal of user-level stance
detection is to capture and analyze users’ overall attitudes
across multiple interactions, rather than just a single text.
This is particularly important for brand management, po-
litical analysis, and social movement research, as it can
reveal changes in user attitudes and underlying trends. By
understanding users’ overall stances, we can more accu-
rately predict their future behavior and decision-making.
However, achieving this goal is challenging. Data collection
and privacy protection are significant hurdles, as user data is
often scattered across multiple platforms and subject to strict
privacy policies. Additionally, users’ expressed stances may
be inconsistent due to contextual changes, requiring com-
plex models that can capture these changes. Furthermore,
annotating user-level data is costly and time-consuming,
necessitating the development of automated annotation
techniques to improve efficiency. In summary, user-level
stance detection has immense application potential but faces
numerous challenges. Future research must overcome these
challenges in data acquisition, model design, and annotation
efficiency to advance this field.
6.4 Ethical Considerations and Bias Mitigation
In stance detection, ethical considerations and bias miti-
gation are crucial, particularly when using LLMs. These
models can amplify biases present in the training data,
which may contain imbalanced and biased information.
Developing debiased datasets and model training methods
is essential but challenging. The hallucination problem in
LLMs, where they generate inaccurate or false informa-
tion, is a key challenge. This can lead to incorrect stance
detection results, affecting decision-making. Ensuring the
reliability and accuracy of large model outputs is the first
step in mitigating this issue. Researchers need to incorporate
mechanisms into model training to detect and correct these
hallucinations. Debiasing methods in LLMs require special
attention. While developing debiased datasets is one direc-
tion, it is difficult to achieve complete debiasing due to the
massive scale of LLMs. Therefore, research should focus on
the model training process, adopting dynamic adjustment
and debiasing algorithms that can identify and adjust biased
outputs in real-time, providing more fair results. Moreover,
transparency and explainability are crucial in LLMs. Due
to their complexity, understanding their decision-making
processes is a challenge. Developing tools and methods to
explain model decisions can help users trust and accept
model outputs. In summary, as LLMs become increasingly
applied in stance detection, the urgency to address bias
and hallucination issues grows. Future research needs to
innovate in model training, data processing, and result in-
terpretation to ensure the ethicality, fairness, and reliability
of stance detection technology.
6.5 Cross-Platform Stance Detection
Cross-platform stance detection is crucial for understanding
users’ overall attitudes and social dynamics. By integrating
data from multiple social media platforms, this approach
provides a more comprehensive analysis of user opinions.
It can reveal cross-platform consistency and changes in
stance, offering richer contextual information for decision-
making. However, this field faces numerous challenges.
Firstly, standardizing and integrating data from different
platforms is a complex task due to varying data formats
and features. Additionally, users’ stance expressions may
differ across platforms due to platform-specific cultures and
characteristics, requiring models to recognize and adapt
to these differences. Another significant challenge is data
privacy and security. Cross-platform data collection may
involve user privacy issues, necessitating secure and com-
pliant data usage in accordance with laws and regulations.
Furthermore, platform competition and data sharing restric-
tions can hinder data acquisition. Technically, developing
models that can handle multi-source heterogeneous data
is a major challenge. This requires innovative algorithms
and architectures to process text, images, and other multi-
modal data simultaneously. Moreover, cross-platform stance
detection models must be highly scalable to accommo-
date diverse platforms and languages. In summary, cross-
platform stance detection offers a new perspective on user
attitude research but demands breakthroughs in data in-
tegration, privacy protection, and technical development.

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2015 14
Future research must innovate in these areas to drive the
development and application of this field.
6.6 Virtual-Real Fusion Stance Detection
The demand for virtual-real fusion stance detection arises
from the pursuit of comprehensively understanding user
attitudes. In today’s interconnected world, users’ opinions
and behaviors are influenced by both online interactions
and real-world contexts. By combining virtual and real-
world data, we can gain deeper insights into user behavior.
Virtual-real fusion in stance detection provides a more com-
prehensive and realistic user portrait. By integrating virtual
and real-world data, we can obtain more accurate user
attitude analysis. This approach can reveal users’ behavioral
consistency and differences across various contexts, offering
a new perspective on complex social dynamics. Virtual-real
fusion significantly improves tasks, particularly in social
behavior research, personalized services, and smart city
management. For instance, researchers can analyze the rela-
tionship between online mobilization and offline participa-
tion in social movements, enabling a better understanding
of social change drivers. By combining online preferences
and offline activity data, personalized services can provide
more dynamic and tailored recommendations, enhancing
user experience. Moreover, virtual-real fusion enables more
personalized and dynamic applications. By integrating on-
line and offline information in real-time, systems can adapt
to users’ changing needs and environments, providing more
accurate services and suggestions. However, this field faces
several challenges. Firstly, data integration complexity is a
major obstacle. Online and offline data differ significantly in
format and content, requiring effective integration methods.
Additionally, collecting and using offline data while respect-
ing user privacy is an important ethical concern. Technically,
achieving virtual-real fusion stance detection requires inno-
vative algorithms that can handle and analyze multi-source
heterogeneous data, including text, images, and sensor data.
Models must also possess dynamic updating capabilities
to adapt to rapidly changing real-world and virtual envi-
ronments. Finally, virtual-real fusion stance detection has
vast application potential, including smart cities and aug-
mented reality experiences. Therefore, research must delve
deeper into application-level exploration to fully exploit this
method’s potential. By addressing these challenges, virtual-
real fusion stance detection can provide new insights into
understanding and predicting user behavior.
7 CONCLUSION
This comprehensive survey has explored the rapidly evolv-
ing field of stance detection on social media, emphasizing
the integration of large language models (LLMs) and their
prospective contributions to understanding public senti-
ment on complex topics. First, the survey presented a vari-
ety of targets for stance detection, including entities, events,
and claims, reflecting the multifaceted nature of social me-
dia discussions. Second, this paper reviewed both tradi-
tional and novel methodologies in stance detection, high-
lighting the transition from feature-based machine learning
techniques to more advanced deep learning and LLM-
based approaches. In particular, the utility of LLMs like
the GPT series in stance detection was critically analyzed,
acknowledging their potential to revolutionize the field by
leveraging their deep contextual understanding capabilities.
Moreover, the paper addressed emerging avenues such as
the detection of unexpressed stances and the application
of stance detection tools in new domains like fake news
identification. These applications underscore the broader
relevance and utility of stance detection beyond academic
research. In conclusion, the survey underscored the need for
ongoing research to develop more generalized and robust
stance detection models capable of handling the dynamic
and diverse nature of social media. It called for the creation
of new, more comprehensive datasets and the continued
exploration of NLP and social computing techniques. These
efforts are crucial for advancing the field and for better
harnessing the power of stance detection to inform decision-
making processes in various sectors.
REFERENCES
[1] K. Glandt, S. Khanal, Y. Li, D. Caragea, and
C. Caragea, “Stance detection in covid-19 tweets,” in
Proceedings of the 59th annual meeting of the association
for computational linguistics and the 11th international
joint conference on natural language processing (long pa-
pers), vol. 1, 2021.
[2] G. Giasemidis, N. Kaplis, I. Agrafiotis, and J. R. Nurse,
“A semi-supervised approach to message stance clas-
sification,” IEEE Transactions on Knowledge and Data
Engineering, vol. 32, no. 1, pp. 1–11, 2018.
[3] Y. Li, T. Sosea, A. Sawant, A. J. Nair, D. Inkpen,
and C. Caragea, “P-stance: A large dataset for stance
detection in political domain,” in Findings of the Asso-
ciation for Computational Linguistics: ACL/IJCNLP , ser.
Findings of ACL, 2021, pp. 2355–2365.
[4] F. Niu, M. Yang, A. Li, B. Zhang, X. Peng, and
B. Zhang, “A challenge dataset and effective models
for conversational stance detection,” in Proceedings
of the 2024 Joint International Conference on Computa-
tional Linguistics, Language Resources and Evaluation,
LREC/COLING, 2024, pp. 122–132.
[5] S. M. Mohammad, S. Kiritchenko, P . Sobhani, X. Zhu,
and C. Cherry, “Semeval-2016 task 6: Detecting stance
in tweets,” in Proceedings of the 10th International
Workshop on Semantic Evaluation, SemEval@NAACL-
HLT 2016, 2016, pp. 31–41.
[6] W.-F. Chen and L.-W. Ku, “We like, we post: A joint
user-post approach for facebook post stance labeling,”
IEEE Transactions on Knowledge and Data Engineering ,
vol. 30, no. 10, pp. 2013–2023, 2018.
[7] S. M. Mohammad, P . Sobhani, and S. Kiritchenko,
“Stance and sentiment in tweets,” ACM Trans. Internet
Techn., vol. 17, no. 3, pp. 26:1–26:23, 2017.
[8] P . Sobhani, D. Inkpen, and X. Zhu, “A dataset for
multi-target stance detection,” inProceedings of the 15th
Conference of the European Chapter of the Association for
Computational Linguistics, EACL, 2017, pp. 551–557.
[9] M. Pontiki, D. Galanis, H. Papageorgiou, I. Androut-
sopoulos, S. Manandhar, M. Al-Smadi, M. Al-Ayyoub,
Y. Zhao, B. Qin, O. D. Clercq, V . Hoste, M. Apidianaki,
X. Tannier, N. V . Loukachevitch, E. V . Kotelnikov,

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2015 15
N. Bel, S. M. Jim ´enez-Zafra, and G. Eryigit, “Semeval-
2016 task 5: Aspect based sentiment analysis,” in Pro-
ceedings of the 10th International Workshop on Semantic
Evaluation, SemEval@NAACL-HLT 2016 , 2016, pp. 19–
30.
[10] A. Addawood, J. Schneider, and M. N. Bashir, “Stance
classification of twitter debates: The encryption debate
as A use case,” in Proceedings of the 8th International
Conference on Social Media & Society, 2017, pp. 2:1–2:10.
[11] D. K ¨uc ¸¨uk, “Stance detection in turkish tweets,” in
Workshops Proceedings and Tutorials of the 28th ACM
Conference on Hypertext and Social Media , ser. CEUR
Workshop Proceedings, vol. 1914, 2017.
[12] A. Zubiaga, A. Aker, K. Bontcheva, M. Liakata, and
R. Procter, “Detection and resolution of rumours in
social media: A survey,” ACM Comput. Surv., vol. 51,
no. 2, pp. 32:1–32:36, 2018.
[13] D. K ¨uc ¸¨uk and F. Can, “Stance detection: A survey,”
ACM Comput. Surv., vol. 53, no. 1, pp. 12:1–12:37, 2021.
[14] A. AlDayel and W. Magdy, “Stance detection on social
media: State of the art and trends,”Inf. Process. Manag.,
vol. 58, no. 4, p. 102597, 2021.
[15] I. Augenstein, T. Rockt ¨aschel, A. Vlachos, and
K. Bontcheva, “Stance detection with bidirectional
conditional encoding,” in Proceedings of the 2016 Con-
ference on Empirical Methods in Natural Language Pro-
cessing, EMNLP 2016, 2016, pp. 876–885.
[16] K. Darwish, W. Magdy, and T. Zanouda, “Improved
stance prediction in a user similarity feature space,”
in Proceedings of the 2017 IEEE/ACM International Con-
ference on Advances in Social Networks Analysis and
Mining, 2017, pp. 145–148.
[17] Y. Igarashi, H. Komatsu, S. Kobayashi, N. Okazaki,
and K. Inui, “Tohoku at semeval-2016 task 6:
Feature-based model versus convolutional neural net-
work for stance detection,” in Proceedings of the
10th International Workshop on Semantic Evaluation,
SemEval@NAACL-HLT, 2016, pp. 401–407.
[18] J. Liu and Y. Zhang, “Attention modeling for targeted
sentiment,” in Proceedings of the 15th Conference of the
European Chapter of the Association for Computational
Linguistics, EACL, 2017, pp. 572–577.
[19] R. Xu, Y. Zhou, D. Wu, L. Gui, J. Du, and Y. Xue,
“Overview of NLPCC shared task 4: Stance detection
in chinese microblogs,” in 5th CCF Conference on Natu-
ral Language Processing and Chinese Computing, NLPCC,
ser. Lecture Notes in Computer Science, vol. 10102,
2016, pp. 907–916.
[20] T. Hercig, P . Krejzl, B. Hourov ´a, J. Steinberger, and
L. Lenc, “Detecting stance in czech news commen-
taries,” in Proceedings of the 17th Conference on Infor-
mation Technologies - Applications and Theory (ITAT) ,
ser. CEUR Workshop Proceedings, vol. 1885, 2017, pp.
176–180.
[21] D. K ¨uc ¸¨uk and F. Can, “Stance detection on tweets:
An svm-based approach,” CoRR, vol. abs/1803.08910,
2018.
[22] A. K. Gautam, P . Mathur, R. Gosangi, D. Mahata,
R. Sawhney, and R. R. Shah, “#metooma: Multi-aspect
annotations of tweets related to the metoo move-
ment,” in Proceedings of the Fourteenth International
AAAI Conference on Web and Social Media , 2020, pp.
209–216.
[23] K. Kawintiranon and L. Singh, “Knowledge enhanced
masked language model for stance detection,” in Pro-
ceedings of the 2021 Conference of the North American
Chapter of the Association for Computational Linguistics:
Human Language Technologies, NAACL-HLT , 2021, pp.
4725–4735.
[24] C. Conforti, J. Berndt, M. T. Pilehvar, C. Giannitsarou,
F. Toxvaerd, and N. Collier, “Will-they-won’t-they: A
very large dataset for stance detection on twitter,” in
Proceedings of the 58th Annual Meeting of the Association
for Computational Linguistics, ACL, 2020, pp. 1715–1724.
[25] E. Allaway and K. R. McKeown, “Zero-shot stance de-
tection: A dataset and model using generalized topic
representations,” in Proceedings of the 2020 Conference
on Empirical Methods in Natural Language Processing,
EMNLP, 2020, pp. 8913–8931.
[26] N. S. Alturayeif, H. Luqman, and M. A. Ahmed,
“Mawqif: A multi-label arabic dataset for target-
specific stance detection,” in Proceedings of the The
Seventh Arabic Natural Language Processing Workshop,
WANLP@EMNLP, 2022, pp. 174–184.
[27] C. Zhao, Y. Li, and C. Caragea, “C-STANCE: A large
dataset for chinese zero-shot stance detection,” in Pro-
ceedings of the 61st Annual Meeting of the Association for
Computational Linguistics, ACL, 2023, pp. 13 369–13 385.
[28] S. Shiwakoti, S. Thapa, K. Rauniyar, A. Shah, A. Bhan-
dari, and U. Naseem, “Analyzing the dynamics of
climate change discourse on twitter: A new annotated
corpus and multi-aspect classification,” in Proceedings
of the 2024 Joint International Conference on Computa-
tional Linguistics, Language Resources and Evaluation,
LREC/COLING, 2024, pp. 984–994.
[29] F. Grasso, S. Locci, G. Siragusa, and L. D. Caro,
“Ecoverse: An annotated twitter dataset for eco-
relevance classification, environmental impact analy-
sis, and stance detection,” in Proceedings of the 2024
Joint International Conference on Computational Linguis-
tics, Language Resources and Evaluation, LREC/COLING,
2024, pp. 5461–5472.
[30] C. Zhao and C. Caragea, “EZ-STANCE: A large
dataset for zero-shot stance detection,” in Findings of
the Association for Computational Linguistics: EMNLP ,
2023, pp. 897–911.
[31] N. Gyawali, I. Sirbu, T. Sosea, S. Khanal, D. Caragea,
T. Rebedea, and C. Caragea, “Gunstance: Stance de-
tection for gun control and gun regulation,” in Pro-
ceedings of the 62nd Annual Meeting of the Association for
Computational Linguistics, ACL, 2024, pp. 12 027–12 044.
[32] Y. Li and Y. Zhang, “Pro-woman, anti-man? identify-
ing gender bias in stance detection,” in Findings of the
Association for Computational Linguistics, ACL, 2024, pp.
3229–3236.
[33] K. Darwish, W. Magdy, and T. Zanouda, “Trump vs.
hillary: What went viral during the 2016 US presiden-
tial election,” in Social Informatics - 9th International
Conference, SocInfo 2017, Oxford, UK, September 13-15,
2017, Proceedings, Part I , ser. Lecture Notes in Com-
puter Science, vol. 10539, 2017, pp. 143–161.
[34] W. Ferreira and A. Vlachos, “Emergent: a novel data-

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2015 16
set for stance classification,” in NAACL HLT 2016, The
2016 Conference of the North American Chapter of the As-
sociation for Computational Linguistics: Human Language
Technologies, 2016, pp. 1163–1168.
[35] A. Zubiaga, G. W. S. Hoi, M. Liakata, R. Procter,
and P . Tolmie, “Analysing how people orient to and
spread rumours in social media by looking at conver-
sational threads,” CoRR, vol. abs/1511.07487, 2015.
[36] L. Derczynski, K. Bontcheva, M. Liakata, R. Procter,
G. W. S. Hoi, and A. Zubiaga, “Semeval-2017 task 8:
Rumoureval: Determining rumour veracity and sup-
port for rumours,” in Proceedings of the 11th Interna-
tional Workshop on Semantic Evaluation, 2017, pp. 69–76.
[37] D. Pomerleau and D. Rao, “Fake news challenge stage
1 (fnc-i): Stance detection,” URL www. fakenewschal-
lenge. org, 2017.
[38] S. V . K. Rohit and N. Singh, “Analysis of speeches
in indian parliamentary debates,” in Computational
Linguistics and Intelligent Text Processing - 19th Inter-
national Conference , ser. Lecture Notes in Computer
Science, vol. 13396, 2018, pp. 236–249.
[39] R. Baly, M. Mohtarami, J. R. Glass, L. M `arquez,
A. Moschitti, and P . Nakov, “Integrating stance de-
tection and fact checking in a unified corpus,” in
Proceedings of the 2018 Conference of the North American
Chapter of the Association for Computational Linguistics:
Human Language Technologies, NAACL-HLT , 2018, pp.
21–27.
[40] N. Lozhnikov, L. Derczynski, and M. Mazzara,
“Stance prediction for russian: Data and analysis,”
in Proceedings of 6th International Conference in Soft-
ware Engineering for Defence Applications, SEDA , ser.
Advances in Intelligent Systems and Computing, vol.
925, 2018, pp. 176–186.
[41] M. Lai, V . Patti, G. Ruffo, and P . Rosso, “Stance evo-
lution and twitter interactions in an italian political
debate,” in Natural Language Processing and Information
Systems - 23rd International Conference on Applications
of Natural Language to Information Systems, NLDB , ser.
Lecture Notes in Computer Science, vol. 10859, 2018,
pp. 15–27.
[42] R. A. V . Cox, S. Kumar, M. Babcock, and K. M. Carley,
“Stance in replies and quotes (SRQ): A new dataset
for learning stance in twitter conversations,” CoRR,
vol. abs/2006.00691, 2020.
[43] Y. Li, H. He, S. Wang, F. C. M. Lau, and Y. Song, “Im-
proved target-specific stance detection on social media
platforms by delving into conversation threads,” IEEE
Trans. Comput. Soc. Syst., vol. 10, no. 6, pp. 3031–3042,
2023.
[44] G. Levow, V . Freeman, A. Hrynkevich, M. Ostendorf,
R. A. Wright, J. Chan, Y. Luan, and T. Tran, “Recogni-
tion of stance strength and polarity in spontaneous
speech,” in 2014 IEEE Spoken Language Technology
Workshop, SLT, 2014, pp. 236–241.
[45] M. A. Weinzierl and S. M. Harabagiu, “Identification
of multimodal stance towards frames of communica-
tion,” in Proceedings of the 2023 Conference on Empirical
Methods in Natural Language Processing, EMNLP , 2023,
pp. 12 597–12 609.
[46] M. Hu, P . Liu, W. Wang, H. Zhang, and C. Lin,
“MSDD: A multimodal language dateset for stance
detection,” in Chinese Lexical Semantics - 23rd Workshop,
CLSW, ser. Lecture Notes in Computer Science, vol.
13495, 2022, pp. 112–124.
[47] B. Liang, A. Li, J. Zhao, L. Gui, M. Yang, Y. Yu,
K. Wong, and R. Xu, “Multi-modal stance detection:
New datasets and model,” inFindings of the Association
for Computational Linguistics, ACL , 2024, pp. 12 373–
12 387.
[48] F. Niu, Z. Cheng, X. Fu, X. Peng, G. Dai, Y. Chen,
H. Huang, and B. Zhang, “Multimodal multi-turn
conversation stance detection: A challenge dataset
and effective model,” in ACM Multimedia 2024, 2024.
[49] M. Taul ´e, M. A. Mart ´ı, F. M. R. Pardo, P . Rosso,
C. Bosco, and V . Patti, “Overview of the task on
stance and gender detection in tweets on catalan
independence,” in Proceedings of the Second Workshop
on Evaluation of Human Language Technologies for Iberian
Languages (IberEval 2017) co-located with 33th Conference
of the Spanish Society for Natural Language Processing ,
ser. CEUR Workshop Proceedings, vol. 1881, 2017, pp.
157–177.
[50] S. Swami, A. Khandelwal, V . Singh, S. S. Akhtar, and
M. Shrivastava, “An english-hindi code-mixed cor-
pus: Stance annotation and baseline system,” CoRR,
vol. abs/1805.11868, 2018.
[51] M. Taul ´e, F. M. R. Pardo, M. A. Mart ´ı, and P . Rosso,
“Overview of the task on multimodal stance detection
in tweets on catalan #1oct referendum,” in Proceedings
of the Third Workshop on Evaluation of Human Language
Technologies for Iberian Languages (IberEval 2018) co-
located with 34th Conference of the Spanish Society for
Natural Language Processing, ser. CEUR Workshop Pro-
ceedings, vol. 2150, 2018, pp. 149–166.
[52] J. Vamvas and R. Sennrich, “X-stance: A multilingual
multi-target dataset for stance detection,” CoRR, vol.
abs/2003.08385, 2020.
[53] P . Wei, J. Lin, and W. Mao, “Multi-target stance de-
tection via a dynamic memory-augmented network,”
in The 41st International ACM SIGIR Conference on
Research & Development in Information Retrieval, SIGIR ,
2018, pp. 1229–1232.
[54] V . Lynn, S. Giorgi, N. Balasubramanian, and H. A.
Schwartz, “Tweet classification without the tweet:
An empirical examination of user versus document
attributes,” in Proceedings of the Third Workshop on
Natural Language Processing and Computational Social
Science, Minneapolis, Minnesota, June 2019, pp. 18–28.
[55] P . Wei and W. Mao, “Modeling transferable topics
for cross-target stance detection,” in Proceedings of the
42nd International ACM SIGIR Conference on Research
and Development in Information Retrieval , 2019, pp.
1173–1176.
[56] Q. Li, Q. Zhang, and L. Si, “eventai at semeval-
2019 task 7: Rumor detection on social media by
exploiting content, user credibility and propagation
information,” in Proceedings of the 13th International
Workshop on Semantic Evaluation, 2019, pp. 855–859.
[57] K. Darwish, P . Stefanov, M. J. Aupetit, and P . Nakov,
“Unsupervised user stance detection on twitter,” in
Proceedings of the Fourteenth International AAAI Confer-

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2015 17
ence on Web and Social Media , 2020, pp. 141–152.
[58] D. S. Elzanfaly, Z. Radwan, and N. A. Othman, “User
stance detection and prediction considering most fre-
quent interactions,” in Artificial Intelligence and Online
Engineering - Proceedings of the 19th International Confer-
ence on Remote Engineering and Virtual Instrumentation ,
ser. Lecture Notes in Networks and Systems, vol. 524,
2022, pp. 421–433.
[59] C. Zhang, Z. Zhou, X. Peng, and K. Xu, “Doubleh:
Twitter user stance detection via bipartite graph neu-
ral networks,” in Proceedings of the Eighteenth Interna-
tional AAAI Conference on Web and Social Media , 2024,
pp. 1766–1778.
[60] R. Bar-Haim, I. Bhattacharya, F. Dinuzzo, A. Saha, and
N. Slonim, “Stance classification of context-dependent
claims,” in Proceedings of the 15th Conference of the
European Chapter of the Association for Computational
Linguistics, EACL, 2017, pp. 251–261.
[61] D. K ¨uc ¸¨uk, “Joint named entity recognition and stance
detection in tweets,” CoRR, vol. abs/1707.09611, 2017.
[62] Y. HaCohen-Kerner, Z. Ido, and R. Ya’akobov, “Stance
classification of tweets using skip char ngrams,” in
Machine Learning and Knowledge Discovery in Databases
- European Conference, ECML PKDD, ser. Lecture Notes
in Computer Science, vol. 10536, 2017, pp. 266–278.
[63] A. Tsakalidis, N. Aletras, A. I. Cristea, and M. Liakata,
“Nowcasting the stance of social media users in a
sudden vote: The case of the greek referendum,” in
Proceedings of the 27th ACM International Conference on
Information and Knowledge Management, CIKM , 2018,
pp. 367–376.
[64] V . Simaki, C. Paradis, and A. Kerren, “Stance classi-
fication in texts from blogs on the 2016 british ref-
erendum,” in Speech and Computer - 19th International
Conference, SPECOM, ser. Lecture Notes in Computer
Science, vol. 10458, 2017, pp. 700–709.
[65] M. Wojatzki and T. Zesch, “Stance-based argument
mining - modeling implicit argumentation using
stance,” in Proceedings of the 13th Conference on Nat-
ural Language Processing , ser. Bochumer Linguistische
Arbeitsberichte, vol. 16, 2016.
[66] A. Sen, M. Sinha, S. Mannarswamy, and S. Roy,
“Stance classification of multi-perspective consumer
health information,” in Proceedings of the ACM India
Joint International Conference on Data Science and Man-
agement of Data, 2018, pp. 273–281.
[67] G. Rajendran, B. Chitturi, and P . Poornachandran,
“Stance-in-depth deep neural approach to stance clas-
sification,” Procedia computer science , vol. 132, pp.
1646–1653, 2018.
[68] Q. Zhang, E. Yilmaz, and S. Liang, “Ranking-based
method for news stance detection,” in Companion of
the The Web Conference 2018 on The Web Conference 2018,
WWW, 2018, pp. 41–42.
[69] A. Rajadesingan and H. Liu, “Identifying users with
opposing opinions in twitter debates,” in Social Com-
puting, Behavioral-Cultural Modeling and Prediction - 7th
International Conference, SBP, 2014, pp. 153–160.
[70] M. Dias and K. Becker, “INF-UFRGS-OPINION-
MINING at semeval-2016 task 6: Automatic gener-
ation of a training corpus for unsupervised iden-
tification of stance in tweets,” in Proceedings of the
10th International Workshop on Semantic Evaluation,
SemEval@NAACL-HLT, 2016, pp. 378–383.
[71] P . Krejzl and J. Steinberger, “UWB at semeval-
2016 task 6: Stance detection,” in Proceedings of the
10th International Workshop on Semantic Evaluation,
SemEval@NAACL-HLT, 2016, pp. 408–412.
[72] J. Ebrahimi, D. Dou, and D. Lowd, “A joint
sentiment-target-stance model for stance classification
in tweets,” in COLING, 26th International Conference on
Computational Linguistics, Proceedings of the Conference:
Technical Papers, 2016, pp. 2656–2665.
[73] H. Elfardy and M. T. Diab, “CU-GWU perspective at
semeval-2016 task 6: Ideological stance detection in
informal text,” in Proceedings of the 10th International
Workshop on Semantic Evaluation, SemEval@NAACL-
HLT, 2016, pp. 434–439.
[74] U. A. Siddiqua, A. N. Chy, and M. Aono, “Stance
detection on microblog focusing on syntactic tree
representation,” in Data Mining and Big Data - Third
International Conference, DMBD , ser. Lecture Notes in
Computer Science, vol. 10943, 2018, pp. 478–490.
[75] M. Lai, D. I. H. Far ´ıas, V . Patti, and P . Rosso, “Friends
and enemies of clinton and trump: Using context
for detecting stance in political tweets,” CoRR, vol.
abs/1702.08021, 2017.
[76] A. Aldayel and W. Magdy, “Your stance is exposed!
analysing possible factors for stance detection on so-
cial media,” Proc. ACM Hum. Comput. Interact. , vol. 3,
no. CSCW, pp. 205:1–205:20, 2019.
[77] A. Aker, L. Derczynski, and K. Bontcheva, “Simple
open stance classification for rumour analysis,” inPro-
ceedings of the International Conference Recent Advances
in Natural Language Processing, RANLP , 2017, pp. 31–
39.
[78] G. Zarrella and A. Marsh, “MITRE at semeval-2016
task 6: Transfer learning for stance detection,” in Pro-
ceedings of the 10th International Workshop on Semantic
Evaluation, SemEval@NAACL-HLT, 2016, pp. 458–463.
[79] P . Wei, W. Mao, and G. Chen, “A topic-aware rein-
forced model for weakly supervised stance detection,”
in The Thirty-Third AAAI Conference on Artificial Intelli-
gence, AAAI , The Thirty-First Innovative Applications
of Artificial Intelligence Conference, IAAI , The Ninth
AAAI Symposium on Educational Advances in Artificial
Intelligence, EAAI, 2019, pp. 7249–7256.
[80] “Turing at semeval-2017 task 8: Sequential approach
to rumour stance classification with branch-lstm,” in
Proceedings of the 10th International Workshop on Seman-
tic Evaluation, SemEval@NAACL-HLT , 2017, pp. 475–
480.
[81] W. Wei, X. Zhang, X. Liu, W. Chen, and T. Wang,
“pkudblab at semeval-2016 task 6 : A specific con-
volutional neural network system for effective stance
detection,” in Proceedings of the 10th International Work-
shop on Semantic Evaluation, SemEval@NAACL-HLT ,
2016, pp. 384–388.
[82] Y. Zhou, A. I. Cristea, and L. Shi, “Connecting targets
to tweets: Semantic attention-based model for target-
specific stance detection,” in Web Information Systems
Engineering - WISE - 18th International Conference, 2017,

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2015 18
pp. 18–32.
[83] R. Vinayakumar, S. S. Kumar, B. Premjith, P . Poor-
nachandran, and S. K. Padannayil, “Deep stance
and gender detection in tweets on catalan indepen-
dence@ibereval 2017,” in Proceedings of the Second
Workshop on Evaluation of Human Language Technolo-
gies for Iberian Languages (IberEval) co-located with 33th
Conference of the Spanish Society for Natural Language
Processing (SEPLN), ser. CEUR Workshop Proceedings,
2017, pp. 222–229.
[84] L. Ambrosini and G. Nicol `o, “Neural models for
stancecat shared task at ibereval 2017,” in Proceedings
of the Second Workshop on Evaluation of Human Language
Technologies for Iberian Languages (IberEval) co-located
with 33th Conference of the Spanish Society for Natural
Language Processing (SEPLN) , ser. CEUR Workshop
Proceedings, vol. 1881, 2017, pp. 210–216.
[85] U. A. Siddiqua, A. N. Chy, and M. Aono, “Tweet
stance detection using multi-kernel convolution and
attentive LSTM variants,” IEICE Trans. Inf. Syst. , vol.
102-D, no. 12, pp. 2493–2503, 2019.
[86] B. Zhang, M. Yang, X. Li, Y. Ye, X. Xu, and K. Dai, “En-
hancing cross-target stance detection with transferable
semantic-emotion knowledge,” in Proceedings of the
58th Annual Meeting of the Association for Computational
Linguistics, ACL, 2020, pp. 3188–3197.
[87] R. Liu, Z. Lin, Y. Tan, and W. Wang, “Enhancing zero-
shot and few-shot stance detection with commonsense
knowledge graph,” in Findings of the Association for
Computational Linguistics: ACL/IJCNLP, 2021, pp. 3152–
3157.
[88] M. Hardalov, A. Arora, P . Nakov, and I. Augenstein,
“Cross-domain label-adaptive stance detection,” in
Proceedings of the 2021 Conference on Empirical Meth-
ods in Natural Language Processing, EMNLP , 2021, pp.
9011–9028.
[89] Q. Zhu, B. Liang, J. Sun, J. Du, L. Zhou, and R. Xu,
“Enhancing zero-shot stance detection via targeted
background knowledge,” in SIGIR ’22: The 45th Inter-
national ACM SIGIR Conference on Research and Devel-
opment in Information Retrieval, 2022, pp. 2070–2075.
[90] Z. He, N. Mokhberian, and K. Lerman, “Infusing
knowledge from wikipedia to enhance stance detec-
tion,” in Proceedings of the 12th Workshop on Compu-
tational Approaches to Subjectivity, Sentiment & Social
Media Analysis, WASSA@ACL, 2022, pp. 71–77.
[91] B. Liang, Q. Zhu, X. Li, M. Yang, L. Gui, Y. He, and
R. Xu, “Jointcl: A joint contrastive learning framework
for zero-shot stance detection,” in Proceedings of the
60th Annual Meeting of the Association for Computational
Linguistics (Long Papers), ACL, 2022, pp. 81–91.
[92] H. Zhang, Y. Li, T. Zhu, and C. Li, “Commonsense-
based adversarial learning framework for zero-shot
stance detection,” Neurocomputing, vol. 563, p. 126943,
2024.
[93] X. Zhao, L. Tian, F. Xie, B. Zhou, H. Wang, H. Wu,
and L. Gao, “MSFR: stance detection based on multi-
aspect semantic feature representation via hierarchical
contrastive learning,” in IEEE International Conference
on Acoustics, Speech and Signal Processing, ICASSP ,
2024, pp. 11 726–11 730.
[94] S. Hu, N. Ding, H. Wang, Z. Liu, J. Wang, J. Li,
W. Wu, and M. Sun, “Knowledgeable prompt-tuning:
Incorporating knowledge into prompt verbalizer for
text classification,” in Proceedings of the 60th Annual
Meeting of the Association for Computational Linguistics
(Long Papers), ACL, 2022, pp. 2225–2240.
[95] H. Huang, B. Zhang, X. Li, B. Zhang, Y. Sun, C. Luo,
and C. Peng, “Knowledge-enhanced prompt-tuning
for stance detection,” ACM Trans. Asian Low Resour.
Lang. Inf. Process., vol. 22, no. 6, pp. 159:1–159:20, 2023.
[96] S. Wang and L. Pan, “Target-adaptive consistency
enhanced prompt-tuning for multi-domain stance
detection,” in Proceedings of the 2024 Joint Interna-
tional Conference on Computational Linguistics, Language
Resources and Evaluation, LREC/COLING , 2024, pp.
15 585–15 594.
[97] A. Li, B. Liang, J. Zhao, B. Zhang, M. Yang, and
R. Xu, “Stance detection on social media with back-
ground knowledge,” in Proceedings of the 2023 Confer-
ence on Empirical Methods in Natural Language Process-
ing, EMNLP, 2023, pp. 15 703–15 717.
[98] D. Ding, L. Dong, Z. Huang, G. Xu, X. Huang, B. Liu,
L. Jing, and B. Zhang, “EDDA: A encoder-decoder
data augmentation framework for zero-shot stance
detection,” CoRR, vol. abs/2403.15715, 2024.
[99] X. Lan, C. Gao, D. Jin, and Y. Li, “Stance detection with
collaborative role-infused llm-based agents,” in Pro-
ceedings of the Eighteenth International AAAI Conference
on Web and Social Media, ICWSM , 2024, pp. 891–903.
[100] A. Li, J. Zhao, B. Liang, L. Gui, H. Wang, X. Zeng,
K. Wong, and R. Xu, “Mitigating biases of large lan-
guage models in stance detection with calibration,”
CoRR, vol. abs/2402.14296, 2024.
[101] D. Ding, G. Dai, C. Peng, X. Peng, B. Zhang, and
H. Huang, “Distantly supervised explainable stance
detection via chain-of-thought supervision,” Mathe-
matics, vol. 12, no. 7, p. 1119, 2024.
[102] S. S. Wagner, M. Behrendt, M. Ziegele, and S. Harmel-
ing, “SQBC: active learning using llm-generated syn-
thetic data for stance detection in online political
discussions,” CoRR, vol. abs/2404.08078, 2024.
[103] J. M. Fraile-Hernandez and A. Pe ˜nas, “Hamison-
generative at climateactivism 2024: Stance detection
using generative large language models,” in Proceed-
ings of the 7th Workshop on Challenges and Applications of
Automated Extraction of Socio-political Events from Text,
CASE, 2024, pp. 79–84.
[104] I. G ¨ul, R. Lebret, and K. Aberer, “Stance detection on
social media with fine-tuned large language models,”
CoRR, vol. abs/2404.12171, 2024.
[105] X. Wang, Y. Wang, S. Cheng, P . Li, and Y. Liu, “DEEM:
dynamic experienced expert modeling for stance de-
tection,” in Proceedings of the 2024 Joint International
Conference on Computational Linguistics, Language Re-
sources and Evaluation, LREC/COLING, 2024, pp. 4530–
4541.
[106] M. Taranukhin, V . Shwartz, and E. Milios, “Stance
reasoner: Zero-shot stance detection on social media
with explicit reasoning,” in Proceedings of the 2024
Joint International Conference on Computational Linguis-
tics, Language Resources and Evaluation, LREC/COLING,

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2015 19
2024, pp. 15 257–15 272.
[107] B. Zhang, D. Ding, Z. Huang, A. Li, Y. Li, B. Zhang,
and H. Huang, “Knowledge-augmented interpretable
network for zero-shot stance detection on social me-
dia,” 2024.
[108] D. Ding, R. Chen, L. Jing, B. Zhang, X. Huang,
L. Dong, X. Zhao, and G. Song, “Cross-target stance
detection by exploiting target analytical perspectives,”
in IEEE International Conference on Acoustics, Speech and
Signal Processing, ICASSP, 2024, pp. 10 651–10 655.
[109] Z. Zhang, Y. Li, J. Zhang, and H. Xu, “Llm-driven
knowledge injection advances zero-shot and cross-
target stance detection,” in Proceedings of the 2024
Conference of the North American Chapter of the Asso-
ciation for Computational Linguistics: Human Language
Technologies (Short Papers),NAACL, 2024, pp. 371–378.
[110] M. A. Weinzierl and S. M. Harabagiu, “Tree-of-
counterfactual prompting for zero-shot stance detec-
tion,” in Proceedings of the 62nd Annual Meeting of the
Association for Computational Linguistics (Long Papers),
ACL, 2024, pp. 861–880.
[111] B. Liang, Y. Fu, L. Gui, M. Yang, J. Du, Y. He, and
R. Xu, “Target-adaptive graph for cross-target stance
detection,” in WWW ’21: The Web Conference, 2021, pp.
3453–3464.
[112] Z. Zhou and E. Elejalde, “Stance inference in twitter
through graph convolutional collaborative filtering
networks with minimal supervision,” in Companion
Proceedings of the ACM Web Conference, WWW , 2023,
pp. 1030–1038.
[113] J. Pennington, R. Socher, and C. D. Manning, “Glove:
Global vectors for word representation,” inProceedings
of the 2014 Conference on Empirical Methods in Natural
Language Processing, EMNLP, 2014, pp. 1532–1543.
[114] T. Mikolov, K. Chen, G. Corrado, and J. Dean, “Ef-
ficient estimation of word representations in vector
space,” in 1st International Conference on Learning Rep-
resentations, ICLR, Workshop Track Proceedings, 2013.
[115] M. Binz and E. Schulz, “Using cognitive psychology to
understand GPT-3,” CoRR, vol. abs/2206.14576, 2022.
[116] B. Zhang, X. Fu, D. Ding, H. Huang, Y. Li, and
L. Jing, “Investigating chain-of-thought with chatgpt
for stance detection on social media,” CoRR, vol.
abs/2304.03087, 2023.
[117] B. Zhang, D. Ding, and L. Jing, “How would stance
detection techniques evolve after the launch of chat-
gpt?” arXiv preprint arXiv:2212.14548, 2022.
