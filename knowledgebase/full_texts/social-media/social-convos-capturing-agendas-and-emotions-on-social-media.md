---
title: 'Social Convos: Capturing Agendas and Emotions on Social Media'
url: https://arxiv.org/abs/2402.15571
category: social-media
subcategory: empirical
date: 2024-02
venue: ''
authors:
- Ankita Bhaumik
- Ning Sa
- Gregorios Katsios
- Tomek Strzalkowski
source: arxiv
pdf_url: https://arxiv.org/pdf/2402.15571
pages: 10
chars: 38044
fetched_at: '2026-11-08T13:05:38+00:00'
kb_version: 1
---

# Social Convos: Capturing Agendas and Emotions on Social Media

Social Convos: Capturing Agendas and Emotions on Social Media
Ankita Bhaumik, Ning Sa, Gregorios Katsios, Tomek Strzalkowski
Rensselaer Polytechnic Institute
Troy, New York
{bhauma, san2, katsig, tomek}@rpi.edu
Abstract
Social media platforms are popular tools for disseminating targeted information during major public events
like elections or pandemics. Systematic analysis of the message traffic can provide valuable insights into
prevailing opinions and social dynamics among different segments of the population. We are specifically
interested in influence spread, and in particular whether more deliberateinfluence operationscan be detected.
However, filtering out the essential messages with telltale influence indicators from the extensive and often
chaotic social media traffic is a major challenge. In this paper we present a novel approach to extract influence
indicators from messages circulating among groups of users discussing particular topics. We build upon the
concept of aconvo to identify influential authors who are actively promoting some particular agenda around that
topicwithinthegroup. Wefocusontwoinfluenceindicators: the(controlof)agendaandtheuseofemotionallanguage.
Keywords:agenda, emotions, social networks, campaigns
1. Introduction
Popular social media platforms, such as Twitter
(nowX),Facebook,Instagram,andothers,havebe-
come global, wide reaching communication chan-
nels that remain largely unregulated for access and
content. They are an ideal vehicle for placing pre-
cisely targeted commercial advertising and other
types of outreach activities. Social media have
also become means of choice for spreading pro-
paganda, disinformation, and for running influence
operations. In this paper we focus on this last phe-
nomenon; more specifically: how the presence of
deliberate influence operations can be detected
among the overall message traffic.
While at the first glance the social media mes-
sage traffic may appear random and chaotic, it is
in fact an environment where all kinds of social
phenomena obtain, not unlike in any other forms of
human interaction, except at a much larger scale.
Social media is thus as an extensive repository of
information to study group dynamics at scale, in-
cluding sociolinguistic behaviors such as agenda
control and influence, as well as the methods and
techniques deployed to achieve them (Del Vicario
et al., 2017; Bovet and Makse, 2019; Caldarelli
et al., 2020).
At the same time, a crucial challenge for an ef-
fective analysis of the message traffic is separating
specific interactions from among many that may
be occurring at the same time, all set against the
backdrop of largely unrelated "noise". If we want to
analyze an potential influence operation, we must
zero in on a subset of messages shared between
the possible influencers and their targets, as well
as many onlookers. It is within this potentially large
group where the key social behaviors can be ob-
served with sufficient clarity. Previous work has
been done on the representation of such behaviors
on social media as a landscape ofconvos(Katsios
et al., 2019), and this paper builds upon it.
Katsios et al., 2019 define aconvo as an on-
linesocialphenomenonwherepeopleareengaged
aroundatopicoranactivity. A convocanbeformed
among users who read, edit, comment or forward
an information artifact, which could be a document,
a project, a topic, or an idea. Some examples can
be a repository on GitHub, a subreddit on Reddit
or a hashtag group on Twitter. We hypothesize that
convos can be used to detect focused groups of
messages around a particular topic, which can be
further used for detecting influence operations.
One well-documented situation where social me-
dia can be used to run influence operations is dur-
ingnationalelectionsandpublicemergencies,such
astherecentCOVID-19pandemic(KarlsenandEn-
jolras, 2016; Jungherr, 2016; Badawy et al., 2019).
Theseoperationsaredrivenbygroupsofusersand
characterized by the specific agendas they aim to
promote. We deploy the concept of aconvo to
extract the subsets of social media traffic devoted
to popular topics arising within the specified time
periods, e.g., during French national elections in
2022. From the convo traffic, we extract the mes-
sages related to its main topic, as well as a network
of influential authors who are actively promoting a
particular viewpoint, or agenda within the convo.
We characterize theconvo representation using
well-established influence indicators, specifically,
agenda control (Broadwell et al., 2013) and use of
emotional language(Bhaumik et al., 2023). This
allows us to identify the most influential members
of the convo, as well as to uncover a network of
relationships between them. Our hypothesis is that
arXiv:2402.15571v1  [cs.SI]  23 Feb 2024

a dense network of mutual connections among the
key influencers in the convo indicates a deliberate
influence operation. This may be contrasted with
a more organic message traffic where individual
influencers are acting largely independently of one
another.
Existing works on extracting influence indica-
tors from social media has been performed on
a message level (Mather et al., 2022; Bhaumik
et al., 2023). After tagging individual messages
with agenda and emotion labels, the aggregate
agendas and emotions in the dataset are typically
obtained by calculating a relative distribution or
density of each label. However, this bottom-up
approach has several drawbacks. Firstly, by work-
ing on individual messages, this approach under-
estimates the semantic and social links between
the messages, thus treating them as independent
events. Secondly, by ignoring duplicate messages
and reposts (retweets on Twitter), this approach
weighs each unique message equally and ignores
the differences in their popularity. Thirdly, although
there are predefined emotion categories, the set of
agendasgermaneineachtypeofeventaretypically
unknown in advance. As a result, some amount
of human annotation may be needed in order to
obtain the relevant agenda labels.
To mitigate the above drawbacks, we propose a
novel top-down approach to detect agendas (and
who pushed them) and emotions (and who uses
them) simultaneously from focused groups of mes-
sages in aconvo. We use instruction tuned pre-
trained large language models (LLMs) that have
theabilitytoprocesscollectionsofmessagesasop-
posed to fine-tuned models that work at a message
level.
We perform our experiments on the 2022 French
Election Twitter dataset to study popular influence
operations, such as #Frexit (Wikipedia, 2023), that
promoted France’s exit from the European Union.
We outline the complete methodology of extracting
convosfrom a social media corpus, identification
of influential authors in a convo and characterizing
them using agendas and emotions in Section 2.
Thoughourexperimentshavebeencarriedoutona
Twitterdataset,ourapproachhasbeengeneralized
for multiple social media platforms like Reddit or
public forums which do not use hashtags.
2. Methodology
Ourapproachtoidentify convonetworkscomprises
of three major steps (Fig. 1):
1. Identification of a convo using hashtag or topic
groups around the keywords of interest.
2. Identification of authors who act as top influ-
ential users in a convo.
3. Detection of entities, agendas and emotions
from the convo.
In the following subsections, we outline every
step in detail.
2.1. Identification of Convos
As described by Katsios et al., the definition of a
convo depends on the type of social media under
examination. For example, on Twitter, convos typ-
ically form around hashtag groups and on Reddit
they arise in subreddits discussing similar topics.
Therefore, given a set of terms of interest, the first
step in our approach is to identify these hashtag or
topic groups in the input corpus.
Employing a keyword search mechanism to iden-
tify the hashtag or topic groups on social media
is a less effective approach due to the inherent
complexities of the medium. Social media mes-
sages are often short and may not mention certain
keywords directly. For example, when examining
tweets from the 2022 French Elections presiden-
tial campaign, its not guaranteed that the terms
France, president, orelection will be explic-
itly mentioned. To address this challenge, we first
identify hashtag groups on Twitter, or topic groups
in other social media platforms, and we use these
groups to gather messages related to keywords of
interest, allowing for a more comprehensive and
accurate analysis.
To identify hashtag convos, we create a co-
occurrence based distance matrix of the top 6000
tokensinthehashtagvocabularyofthecorpus. Us-
ing this as our feature representation, we perform
dimensionality reduction via UMAP (McInnes et al.,
2018) and then use HDBSCAN (Campello et al.,
2013) to cluster them into hashtag groups. Some
examples of hashtag groups are listed in Table 1.
For datasets from other social media like Reddit
or public forums, we use the LDA topic modeling al-
gorithmtoidentifytopicdistributionsintheinputcor-
pus (Blei et al., 2003). Finally, we identify convos
around a particular topic using the hashtag/topic
groups containing any of the terms of interest.
2.2. Identification of the Top Influencers
As previously discussed, not all messages within
a hashtag convo carry equal significance. The
weight of a message is determined by the number
of retweets, reflecting broader agreement among
users. Conversely, a collection of messages from
a single user can provide a more comprehensive
expressionoftheirideasandpositionscomparedto
a single message. Therefore, instead of analyzing
all tweets in a convo, we prioritize the examina-
tion of tweets from influential users, who are often
retweeted.

Figure 1: Overview of our approach to extract and characterizeconvos.
Hashtag Groups
#frexit, #ue, #asselineau, #reprenonslecontrôle,
#schengen
#stopputin, #stoprussia, #standwithukraine,
#closetheskyoverukraine,
#noflyzoneoverukraine
#covid19, #covid, #covid_19, #omicron,
#vaccine
#passvaccinal, #passevaccinal, #passsanitaire,
#passdelahonte, #passevaccinaldelahonte
#mckinseygate, #macronmckinsey, #macronas-
sassin, #macronmckinseygate, #macroncnon
Table 1: Examples of hashtag groups extracted
from the French Elections 2022 dataset, showing
top 5 hashtags in each group.
To characterize these influential tweets we cat-
egorize them by topic, allowing us to extract the
agendas and emotions associated with each topic
group. We use a two-level hierarchical cluster-
ing method to identify distinct topics within bigger
groups of messages (Grootendorst, 2022). The
agendas and emotions expressed by these influen-
tial users serve as a representative sample of the
entire convo.
Furthermore, we explore the underlying efforts
driving these agendas by scrutinizing the tweeting
behavior of influential users and exploring the con-
nections within the cross-influencer network. We
hypothesize that in a targeted influence operation
these authors would be actively retweeting each
other to promote similar ideas.
2.3. Agenda and Emotion Detection
In order to effectively perform the tasks of agenda
and emotion detection across a collection of mes-
sages, we utilize large language models (LLMs)
as they have a large context window. Existing
fine-tuned models are not suitable for these tasks,
primarily due to their limitations in processing sin-
gle messages within specific domains. Recent
advancements in pre-trained LLMs have demon-
strated remarkable capabilities in zero-shot sum-
marization across diverse domains (Zhang et al.,
2023; Yang et al., 2023). Leveraging these break-
throughs, we have developed an instruction-tuned
model for agenda and emotion detection.
Inourapproach,weprovidetheLLMwithaglobal
context that acts as an instructional guide for its
intended task. We adopt a prompt-based template
to extract both the agendas and emotions from a
collection of messages. Additionally, we employ an
output template designedtosteer the LLM ingener-
atingoutputsinaformatconducivetovisualizingall
components within the convo network. This output
template replicates a JSON file structure, enhanc-
ing its utility for seamless downstream processing.
We design prompts to direct the model to answer
the questions and accomplish the following tasks:
• Prompt 1: What are the top distinct entities
(maximum5)mentionedinseveralmessages?
• Prompt 2: What are the authors promoting
about each entity? Give me 1 phrase for each.
• Prompt 3:What are the emotions expressed
towards each entity?
• Prompt 4:Combine the entities, promoted ac-
tions and emotions in the output template.
The prompts are used to fill out an output JSON
template:
output = [
{
"entity": {entity},
"promoted_actions": {action},
"emotions": {emotion}
},
...
]
This yields a file that contains information regard-
ing the entities, agendas, and emotions within the
conversation.
3. Experiments
3.1. Dataset
We run our experiments on a publicly available
dataset from the 2022 French presidential elec-
tions (Daignan, 2022). It contains 45 million tweets
and retweets from Nov. 12, 2021 to Apr. 03, 2022,

around the main actors in the election. French is
the dominant language of the dataset, and there
are also certain amount of tweets written in English.
This dataset contains all retweet information about
the tweets which makes it an ideal choice to iden-
tify influential message groups in this corpus. We
choose two keywords of interest that were popular
topicsduringtheFrenchelectioncampaignasstud-
ied from news articles and online forums : #frexit
and #covid_19 (Wikipedia, 2023).
3.2. Implementation
To make a traceable retweet network, we pre-
process the original dataset to link all retweets to
the original tweet. We also remove emojis, hyper-
links and tweets having less than 3 textual tokens.
To pick the most influential messages in aconvo
we examine at the messages by the top 10 most
retweeted authors in thatconvo. Alternatively, this
value could be determined based on the propor-
tion of messages contributed by each author in a
convo. We use multilingual BERTopic to separate
the convomessages into smaller groups (Grooten-
dorst, 2022).
To implement the agenda and emotion detection
system we use a LLM with a sufficiently large con-
text window. We perform our experiments using
Llama-2-13b-chat model with a context length of
4096 tokens (Touvron et al., 2023). We provide the
global context in the system prompt and use the
prompts to further probe the LLM. We use nucleus
sampling with p as 0.9 for generating responses
andlimitthenumberofnewtokensto500. Wealso
tested our approach using ChatGPT to achieve
comparable performance (Ouyang et al., 2022).
The experiments are performed on 2 NVIDIA A100
GPUs.
3.3. Results
To establish a mapping between each tweet and its
corresponding retweets, we preprocess the original
corpus, resulting in a dataset comprising of 16.7
million tweets. On further removal of emojis, hyper-
links, tweets without hashtags, and tweets having
less than 3 textual tokens, we arrive at 2.8m tweets
and their associated retweet information.
Our first step to identify all hashtag groups in the
corpus results in more than 40 hashtag groups (Ta-
ble 1). We select the two that contain our terms of
interest, frexit and covid_19, to extract the hashtag
convosaround them. Table 2 lists the total number
of authors, tweets and retweets in each of these
convos. We then select the messages by the top
10 retweeted authors. In the #frexit convo, the top
influencers’ messages account for 5% of total mes-
sages in the convo and comprise around 44% of
the total retweets (20,135 out of 44,859). Whereas
for the larger #covid_19 convo, that has a larger
number of tweets and authors, the top influencers
contribute1%ofalltweetsandtheirretweetnumber
comprise 28% of the total retweets.
To understand the connections among the top
10 influencers, we construct a network based on
their retweet behavior in the whole corpus (Fig. 2).
The nodes in Fig. 2 represent the authors and
the weight of the edges represent the number of
retweetsbetweenthem,balloonsontopofthenode
indicate instances of self-retweeting by that author.
Weconstructagraphforeachconvoandnoticethat
there is no overlap in top influencers between the
two,signifyingthattheseauthorsarepredominantly
dedicated to promoting specific agendas. While
the top 10 influencers in the #Frexit convo (Fig.2a)
are connected by a dense network of retweet or
self-retweet, the network for #covid_19 (Fig. 2b)
contains only 8 authors.
#Frexit #Covid_19
Inf. Convo Inf. Convo
No. authors 10 3,572 10 10,239
No. tweets 902 16,406 403 39,719
No. RT count 20,135 44,859 38,144 133,457
Table 2: Descriptive results of influencers (Inf.) in
the #Frexit and the #Covid_19 convo
We cluster the influencers’ messages in each
convo into smaller topic groups to be able to ana-
lyze the content more effectively. We run our emo-
tionandagendadetectionmodeloverthemessage
clusters to characterize the influence indicators in
eachinfluentialconvo. Fig3visualizesthejsonout-
puts we obtain to depict the top entities, promoted
actions and emotions of two selected message
clusters from each convo. The generated agenda
summaries, listed in Table 3, provide us with a con-
ciseandinformativesnapshotoftheconvosaround
the topic of interest.
#frexit convo (Fig 3a): In the first message clus-
ter of this convo, the influencers promote the can-
didacy of François Asselineau and advocate for
France leaving the EU. The first snapshot also il-
lustrates a similar idea: the influencers support
François Asselineauwho advocates for #Frexit, en-
courage the French peopleto take back control of
their country, and admireCharles de Gaullewho
represented French independence and greatness.
They also accuseEmmanuel Macronfor suppress-
ingtheFrenchpeople’sopinionandareangryabout
EU for manipulating the French people and dam-
aging France’s economy and sovereignty.
The second influential message group in the
same convo represents another view of the influ-
encers where they advocate for another candidate
in the election:Florian Philippotand support the

(a) #Frexit convo
 (b) #covid_19 convo
Figure 2: Influencer Networks among top influencers in each convos. Each node (red point) represents
an influencer, with her index marked below the node. The arrows indicate the direction of the connections
and the numbers above show the weight of the connections. A balloon on top of a node means a self-RT
link.
(a) Convos in the #frexit clusters
(b) Convos in the #covid_19 clusters
Figure 3: Different clusters in theconvosabout #Frexit and #covid_19. They are characterized by the
indicators of top entities, promoted actions, and emotions. Theinfluencers are the top 10 retweeted
authors in that convo. The expanded network of the influencers are illustrated in Fig. 2a and 2b.
Entities are grey blobs and promoted actions are the grey edge labels. Emotion labels over the edges are
colored as negative/positive ones. The model also generates an agenda summary, given in Table 3.
LesPatriotes party he leads. They also criticize
president Macron and call for a campaign against
his policy onPassVaccinal.
#covid_19convo(Fig. 3b): Inboththeinfluential
message clusters of this convo, the influencers feel
concernedabout COVID19andcriticize Emmanuel
Macron for using the crisis for electoral gain and
the improper policies. In the first message cluster,
Vaccination passportis supported and thought to
be able to protect public health, while theGovern-
ment is accused for easing theHealth constraints

Message Cluster Agenda Summary
Fig. 3a - left The agenda behind this set of tweets is to promote the candidacy of François
Asselineau for the French presidency in 2022 and to advocate for France’s
withdrawal from the European Union (#Frexit)
Fig. 3a - right The agenda behind this set of tweets is to promote the political movement
#LesPatriotes and its leader, Florian Philippot, and to campaign against the
current French President Emmanuel Macron and his policies, particularly the
controversial vaccine pass
Fig. 3b - left The agenda behind this set of tweets is primarily focused on the French
government’s handling of the COVID-19 pandemic, specifically the use of
vaccination passports, the easing of health constraints, and the perceived
political motivations behind these actions
Fig. 3b - right The agenda behind this set of tweets is to criticize and scrutinize the actions
and words of French President Emmanuel Macron regarding the COVID-19
pandemic and vaccination
Table 3: Summarized agendas of the messages clusters shown in Fig.3
for political purposes. Whereas in the second mes-
sage cluster, people show desire fornightclubs,
advocate forIvermectinas a possible treatment for
Covid-19, and thinkSudRadiois a trustful resource
of information and opinion.
3.4. Analysis and Discussion
To validate our hypotheses, we manually analyze
the generated convo visualizations and influencer
networks. Inaddition,weverifythegeneratedagen-
das by comparing them with news articles and on-
line forums. By this process we ascertain that they
are correct representations of the broader corpus
of data.
ThenumbersinTable2showthatinboththecon-
vos, the top 10 influencers generate a very small
fraction (5% and 1%) of the tweets in the convo,
but receive a large proportion of retweets (44%
and 28%). Therefore, we can reasonably extract
the tweets by the top influencers to represent the
influential or popular messages in the convo. A
noticeable difference between the two convos is
that, the number of the influential tweets in the
#Frexit convo is more than twice of the number in
the #covid_19 convo. This signifies that the influ-
encers in the #Frexit convo have been much more
active in generating content to drive their agendas.
We closely examine the network of influencers
to analyze their retweet behavior. The#frexit influ-
encer network (Fig. 2a) is strongly connected by
a large number of retweets. Bi-directional retweet-
ing is also found between 4 pairs of authors. On
the contrary, in the #covid_19 influencer network,
the connections are notably weaker. All the con-
nections are one-directional and majority of them
originate from one author. We hypothesize that a
combinationoftheinfluencers’effortsingenerating
the tweets and the density of their retweet network
may serve as an early sign of a potential influence
operation within the convo. Consequently, though
the influencers’ receive a substantial number of
retweets in both convos, it is plausible that an in-
fluence operation may be more prominent in the
#Frexit convo compared to the #covid_19 convo.
Next, we analyze the agendas and convos snap-
shots generated by our model. In the #Frexit convo,
both the message clusters in Fig. 2a criticize presi-
dent Macron but they advocate for different candi-
dates 1. The first cluster focuses more on France’s
withdrawalfromtheEU,andsupportFrançoisAsse-
lineau who is a lead character in the #Frexit move-
ment 2. However, the second cluster advocates for
Florian Philippot and his party, and shows strong
opposition against the vaccine pass3. Influencer
I4 and I1 are the top contributors in the first cluster,
while more than 90% of the tweets in the second
cluster come fromI6. Fig 2a also depicts thatI4
and I1 retweet each other, andI6 is not directly
connected to either of them. Hence, we can de-
duce that even within the same convo, distinct sub-
groups of influencers and their respective retweet-
ing users tend to agree on specific topics while
disagreeing on others. Similarly, the agendas in
the #covid_19 convo discuss several topics around
the vaccine pass in France and criticize Macron for
his handling of the pandemic4.
1https://www.thenationalnews.com/worl
d/europe/2022/04/13/marine- le- pen- den
ies-frexit-agenda-as-presidential-rival
s-clash-over-europe/
2https://international.la-croix.com/n
ews/politics/frances-frexit-presidentia
l-candidate/4821
3https://www.thelocal.fr/20180219/les
-patriotes-florian-philippot-what-you-n
eed-to-know-france-newest-far-right-par
ty
4https://www.france24.com/en/europe/2
0211014-macron-s-covid-health-pass-a-s

Therefore, these visualizations of the focused
message groups in the convos provide a concise
representation of the ongoing discussions among
popular authors around that topic. Extracting such
detailed analysis would require significant manual
effort and time from experienced analysts. To-
gether with the influencer networks, they provide
valuable insights about targeted operations in a
corpus.
4. Related Work
4.1. Agenda and Emotion Detection
In previous studies, agenda and emotion detection
are usually presented as individual tasks. Most of
the work on agenda theory focus on the agenda
setting process between the media and the audi-
ence, between different types of media, or between
different groups of people (Ceron et al., 2016; Guo,
2019; McCombs et al., 1997; Vargo et al., 2014).
In (McCombs et al., 1997), the authors investigate
the images of the election candidates presented by
mass media and shaped among the voters. Doc-
ument level content analysis is performed on TV
news and newspaper stories, and the voters’ opin-
ions towards the candidates are collected by sur-
veys.
The agendas in any political campaign are usu-
ally candidate names, their personalities, ideolo-
gies, and qualifications, and whether their images
are built to be positive, neutral, or negative. The
authors compare the proportion of each agenda
between the media and voters to understand the
effects of media on the general population. With
the emergence of social media, similar research
has been performed to explore the agenda-setting
dynamics between mass media and social media,
to identify the roles of the agenda setter between
them (Su and Borah, 2019; Conway et al., 2015).
The use of emotional language has also been an
important indicator during any political campaign
(Grüning and Schubert, 2022). With the availability
of deep learning models and annotated datasets,
fine-tuning models for emotion detection in partic-
ular domains have become a popular approach
for emotion detecteion (Cai and Hao, 2018; Huang
et al., 2019; Chiorrini et al., 2021). Prompting tech-
niques using pre-trained large larguage models
havealsobeendeployedtoperformzero-shotemo-
tion detection in unknown domains (Plaza-del Arco
et al., 2022). Although there has been significant
research on emotion detection over individual mes-
sages on social media, our work is dedicated to
detecting emotions expressed in groups of mes-
sages towards specific entities or topics.
uccess-in-overcoming-france-s-vaccine-s
cepticism
All the works mentioned above aim to clarify the
phenomena of information flow from one source to
another, and ignore the possible influence opera-
tions behind the information flow. In contrast, our
approach addresses this missing piece by identify-
ing the influencers in the dynamic process and an-
alyzing their behaviors and their inter-connections.
Additionally, our break-down and summary method
works efficiently as it requires lesser human anno-
tation, which is a necessary step in most of the pre-
vious works (Guo, 2019; Su, 2022; Subbiah et al.,
2023).
5. Conclusion
In this work we introduce a novel systematic ap-
proach to identify influential message subsets from
social media datasets. We build upon the idea
of aconvo to extract concise snapshots of these
online discussions around particular events or top-
ics. We characterize theseconvosusing agendas
and emotions to enable us to detect targeted influ-
ence operations by a group of influencers. We also
create a network of these influencers to analyze
the retweet behavior and group dynamics among
them. A case study around prominent campaigns
during the 2022 French Elections helps us to eval-
uate our proposed approach. Future work would
include application of our approach on other types
of social media and definition of concrete metrics to
measuredegreesofinfluenceandpreciselyidentify
influence operations.
6. Acknowledgements
This paper is based upon work supported by
the Defense Advanced Research Projects Agency
(DARPA) under Contract No. HR001121C0186.
Any opinions, findings and conclusions or recom-
mendations expressed in this material are those of
theauthorsand donotnecessarilyreflecttheviews
of DARPA or the U.S. Government.
7. Limitations and Ethical
Considerations
Given the nature of the proposed task and the role
ofLLMinourapproach,thisworkdoeshaveseveral
limitations. Firstly, we analyze our approach on a
publicly available Twitter dataset. The dataset con-
tains retweet information but does not differentiate
between tweets, quotes, and replies. In future, we
plantoextendtootherplatformsandotherdatasets
withmorediverseuserinteractionsinordertobetter
understand the group dynamics of online commu-
nities. Secondly, it is well known that the current
largelanguagemodelshaveawiderangeofbiases.

Consequently, it is possible that our findings reflect
the biased opinions nested in the LLM rather than
from the dataset (Rozado, 2023).
We do not use or analyze any personally identifi-
able data in our experiments. The outputs gener-
ated are solely based on summaries generated by
filtering popular messages on Twitter and the use
of popular LLMs. They may reflect various political
agendas or opinions of particular candidates. They
must be verified by expert analysts before use in
any downstream application.
8. Bibliographical References
Adam Badawy, Aseel Addawood, Kristina Lerman,
and Emilio Ferrara. 2019. Characterizing the
2016 russian ira influence campaign.Social Net-
work Analysis and Mining, 9:1–11.
Francesco Barbieri, Jose Camacho-Collados,
Luis Espinosa Anke, and Leonardo Neves. 2020.
TweetEval: Unified Benchmark and Comparative
Evaluation for Tweet Classification. InFindings
of the Association for Computational Linguistics:
EMNLP 2020, pages 1644–1650.
Ankita Bhaumik, Andy Bernhardt, Gregorios Kat-
sios, Ning Sa, and Tomek Strzalkowski. 2023.
Adapting emotion detection to analyze influence
campaigns on social media. In Proceedings
of the 13th Workshop on Computational Ap-
proaches to Subjectivity, Sentiment, & Social
Media Analysis, pages 441–451.
David M Blei, Andrew Y Ng, and Michael I Jordan.
2003. Latent dirichlet allocation.Journal of ma-
chine Learning research, 3(Jan):993–1022.
Alexandre Bovet and Hernán A Makse. 2019. In-
fluence of fake news in twitter during the 2016
us presidential election.Nature communications,
10(1):7.
George Aaron Broadwell, Jennifer Stromer-Galley,
Tomek Strzalkowski, Samira Shaikh, Sarah Tay-
lor, Ting Liu, Umit Boz, Alana Elia, Laura Jiao,
and Nick Webb. 2013. Modeling sociocultural
phenomena in discourse.Natural Language En-
gineering, 19(2):213–257.
Xiaofeng Cai and Zhifeng Hao. 2018. Multi-view
and attention-based bi-LSTM for Weibo emotion
recognition. In2018 International Conference on
Network, Communication, Computer Engineer-
ing, pages 772–779.
GuidoCaldarelli,RoccoDeNicola,FabioDelVigna,
Marinella Petrocchi, and Fabio Saracco. 2020.
Theroleofbotsquadsinthepoliticalpropaganda
on twitter.Communications Physics, 3(1):81.
Ricardo JGB Campello, Davoud Moulavi, and Jörg
Sander. 2013. Density-based clustering based
on hierarchical density estimates. InPacific-Asia
conference on knowledge discovery and data
mining, pages 160–172. Springer.
Andrea Ceron, Luigi Curini, and Stefano M Iacus.
2016. First-and second-level agenda setting in
the twittersphere: An application to the italian po-
litical debate.Journal of Information Technology
& Politics, 13(2):159–174.
Zhuo Chen, Chris Chao Su, and Anfan Chen. 2019.
Top-down or bottom-up? a network agenda-
setting study of chinese nationalism on social
media. Journal of Broadcasting & Electronic Me-
dia, 63(3):512–533.
Andrea Chiorrini, Claudia Diamantini, Alex Mir-
coli, and Domenico Potena. 2021. Emotion and
sentiment analysis of tweets using BERT. In
EDBT/ICDT Workshops.
B.A. Conway, K. Kenski, and D Wang. 2015. The
riseoftwitterinthepoliticalcampaign: Searching
for intermedia agenda-setting effects in the pres-
idential primary.Journal of Computer-Mediated
Communication, 20(4):363–380.
Jean-Michel Daignan. 2022. French presidential
election 2022.
Munmun De Choudhury, Hari Sundaram, Ajita
John, Doree Duncan Seligmann, and Aisling Kel-
liher. 2010. " birds of a feather": Does user ho-
mophilyimpactinformationdiffusioninsocialme-
dia? arXiv preprint arXiv:1006.1702.
Michela Del Vicario, Fabiana Zollo, Guido Cal-
darelli, Antonio Scala, and Walter Quattrociocchi.
2017. Mapping social dynamics on facebook:
The brexit debate.Social Networks, 50:6–16.
Maarten Grootendorst. 2022. Bertopic: Neural
topic modeling with a class-based tf-idf proce-
dure. arXiv preprint arXiv:2203.05794.
David J Grüning and Thomas W Schubert. 2022.
EmotionalCampaigninginPolitics: BeingMoved
and Anger in Political Ads Motivate to Support
Candidate and Party.Frontiers in Psychology,
12:6337.
Lei Guo. 2019. Media agenda diversity and in-
termedia agenda setting in a controlled media
environment: Acomputationalanalysisofchina’s
online news.Journalism Studies, 20(16):2460–
2477.

Yen-Hao Huang, Ssu-Rui Lee, Mau-Yun Ma, Yi-
Hsin Chen, Ya-Wen Yu, and Yi-Shin Chen.
2019. EmotionX-IDEA: Emotion BERT- an Af-
fectional Model for Conversation.arXiv preprint
arXiv:1908.06264.
Andreas Jungherr. 2016. Twitter use in election
campaigns: A systematic literature review.Jour-
nalofinformationtechnology&politics ,13(1):72–
91.
Rune Karlsen and Bernard Enjolras. 2016. Styles
of social media campaigning and influence in
a hybrid political communication system: Link-
ing candidate survey data with twitter data.The
InternationalJournalofPress/Politics ,21(3):338–
357.
G.Katsios,N.Sa,andT.Strzalkowski.2019. Social
convos: A new approach to modeling informa-
tion diffusion in social media. InProceedings of
Advances in Artificial Intelligence, Software and
SystemsEngineering(AHFE2019) ,pages3746–
3753, Cham. Springer International Publishing.
Brodie Mather, Bonnie Dorr, Adam Dalton, William
de Beaumont, Owen Rambow, and Sonja
Schmer-Galunder. 2022. From stance to con-
cern: Adaptation of propositional analysis to new
tasks and domains. InFindings of the Associ-
ation for Computational Linguistics: ACL 2022,
pages 3354–3367.
Maxwell McCombs, Juan Pablo Llamas, Esteban
Lopez-Escobar, and Federico Rey. 1997. Candi-
date images in spanish elections: Second-level
agenda-setting effects.Journalism & Mass Com-
munication Quarterly, 74(4):703–717.
L. McInnes, J. Healy, and J. Melville. 2018. UMAP:
Uniform Manifold Approximation and Projection
for Dimension Reduction.ArXiv e-prints.
LongOuyang,JeffreyWu,XuJiang,DiogoAlmeida,
Carroll Wainwright, Pamela Mishkin, Chong
Zhang, Sandhini Agarwal, Katarina Slama, Alex
Ray, et al. 2022. Training language models to
follow instructions with human feedback. Ad-
vances in Neural Information Processing Sys-
tems, 35:27730–27744.
Flor Miriam Plaza-del Arco, María-Teresa Martín-
Valdivia, and Roman Klinger. 2022. Natural lan-
guage inference prompts for zero-shot emotion
classification in text across corpora. In Pro-
ceedings of the 29th International Conference on
Computational Linguistics, pages 6805–6817.
DavidRozado.2023. Thepoliticalbiasesofchatgpt.
Social Sciences, 12(3):148.
Yan Su. 2022. Networked agenda flow between
elite us newspapers and twitter: A case study of
the 2020 black lives matter movement.Journal-
ism, page 14648849221092521.
Yan Su and Porismita Borah. 2019. Who is
the agenda setter? examining the intermedia
agenda-setting effect between twitter and news-
papers. Journal of Information Technology &
Politics, 16(3):236–249.
Melanie Subbiah, Amrita Bhattacharjee, Yilun Hua,
Tharindu Kumarage, Huan Liu, and Kathleen
McKeown. 2023. Towards detecting harmful
agendas in news articles. InProceedings of the
13th Workshop on Computational Approaches to
Subjectivity, Sentiment, & Social Media Analysis,
pages 110–128, Toronto, Canada. Association
for Computational Linguistics.
Hugo Touvron, Louis Martin, Kevin Stone, Peter
Albert, Amjad Almahairi, Yasmine Babaei, Niko-
lay Bashlykov, Soumya Batra, Prajjwal Bhargava,
Shruti Bhosale, et al. 2023. Llama 2: Open foun-
dationandfine-tunedchatmodels. arXivpreprint
arXiv:2307.09288.
Chris J Vargo, Lei Guo, Maxwell McCombs, and
Donald L Shaw. 2014. Network issue agendas
ontwitterduringthe2012uspresidentialelection.
Journal of communication, 64(2):296–316.
Wikipedia. 2023. Frexit — Wikipedia, the free ency-
clopedia. [Online; accessed 17-October-2023].
Xianjun Yang, Yan Li, Xinlu Zhang, Haifeng Chen,
and Wei Cheng. 2023. Exploring the limits of
chatgpt for query or aspect-based text summa-
rization. arXiv preprint arXiv:2302.08081.
Tianyi Zhang, Faisal Ladhak, Esin Durmus, Percy
Liang, Kathleen McKeown, and Tatsunori B
Hashimoto. 2023. Benchmarking large language
models for news summarization.arXiv preprint
arXiv:2301.13848.
A. Appendices
A.1. Appendix: Agenda and Emotion
Detection Prompts

[INST] <<SYS>>
You are a helpful, respectful and honest agenda detection assistant.
Read the list of messages given and understand the hidden agendas behind them.
Please do not share false information. If you are unable to understand the agenda,
simply say "No agenda".
<</SYS>>
What is the overall agenda behind this set of messages? Give me a short summary.
Messages: {input_text}
[/INST]
The agenda behind this set of tweets is
Table 4: System Prompt use to characterize convos using Llama-2-13b-chat
What are the top distinct entities (maximum 5) mentioned in several messages?
What are the authors promoting about each entity? Give me 1 phrase for each.
Give the emotions expressed towards each entity.
Combine the entities, promoted actions and emotions in the following format:
output = [
{
"entity": {entity},
"promoted_actions": {action},
"emotions": {emotion}
},
...
]
Table 5: Prompts and output template to extract entities, promoted actions and emotions
