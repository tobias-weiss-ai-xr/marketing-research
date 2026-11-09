---
title: 'Political Narratives in the 2024 Moldovan Presidential Election: Stance, Amplification, and Influence'
url: https://arxiv.org/abs/2610.22464
category: social-media
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Andrea Piras
- Osman Rahmoun
- Elena Zheleva
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.22464
pages: 12
chars: 67033
fetched_at: '2026-11-08T13:13:48+00:00'
kb_version: 1
---

# Political Narratives in the 2024 Moldovan Presidential Election: Stance, Amplification, and Influence

Political Narratives
in the 2024 Moldovan Presidential Election:
Stance, Amplification, and Influence
1st Andrea Piras
Department of Computer Science
University of Illinois Chicago
Chicago, USA
apiras2@uic.edu
2nd Osman Rahmoun
Department of Computer Science
University of Illinois Chicago
Chicago, USA
orahm2@uic.edu
3rd Elena Zheleva
Department of Computer Science
University of Illinois Chicago
Chicago, USA
ezheleva@uic.edu
Abstract—Social media platforms play a central role in shaping
political discourse during elections, particularly in geopolitically
contested regions. We study how political narratives emerged,
aligned, and propagated during the 2024 Moldovan presidential
election by analyzing publicly available posts collected from
X, Facebook, and Reddit between August and October 2024.
Combining multilingual stance detection, coordination analysis,
and causal inference, we examine both descriptive and causal
mechanisms underlying online political discourse. First, we ap-
ply large language models to classify stance toward European
integration, Russia, and the two main presidential candidates,
revealing clear cross-platform and cross-linguistic differences
in how political positions are expressed. Second, we construct
retweet-based and semantic alignment networks on X to identify
amplification and aligned framing of dominating narratives.
Finally, we use a proximal causal inference framework to estimate
peer influence effects in stance formation. Our results indicate
consistently positive and statistically significant average treatment
effects across major stance categories. These findings provide
evidence that amplification and peer exposure contribute to the
reinforcement of political narratives online. This work offers the
first analysis of social media discourse surrounding the 2024
Moldovan presidential election and demonstrates the value of
integrating language-based annotation, network analysis, and
causal inference for studying political influence in multilingual
and geopolitically sensitive contexts.
Index Terms—political discourse, stance detection, multilingual
social media, coordination analysis, causal effect estimation
I. INTRODUCTION
Social media platforms have become pivotal places for po-
litical contestation, shaping both the circulation of information
and the formation of public opinion during elections. Research
has shown that online discussions mirror and amplify offline
divisions, with coordinated campaigns and partisan hostility
emerging as key features of digital political debate [1], [2]. At
the same time, platforms serve as spaces where diverse actors,
including citizens, journalists, and anonymous accounts, com-
pete to push narratives and provide support. Understanding
these dynamics is fundamental in elections held in strategi-
cally contested regions, where geopolitical orientations can
influence outcomes that extend beyond the national borders.
The 2024 Moldovan presidential election is a clear example
of this dynamic. Positioned between Europe and Russia,
Moldova has long been at the center of political and cultural
controversies. This election became a focal point for debates
over European integration and Russian influence, particularly
between the two main Moldovan candidates, Maia Sandu (who
ultimately won the election) and former Prosecutor General
Alexandr Stoianoglo. Sandu is often described by major outlets
as pro-European, as her campaign was tied to EU integration,
including the EU accession referendum held alongside the first
round. Stoianoglo, on the other hand, is widely described as
backed by a party traditionally linked to Russia (PSRM), while
publicly expressing opposition against European integration.
In this paper, we present an analysis of election-related so-
cial media posts collected during the election period (between
August 1 and October 25, 2024) from three social media sites:
X (formerly Twitter), Facebook, and Reddit. To the best of our
knowledge, no prior work has conducted a comprehensive and
systematic analysis of social media discourse surrounding the
2024 Moldovan presidential election. Our approach integrates
stance detection, network analysis, and amplification measures
to examine how narratives and alignments unfolded online. To
identify both consistent and contradictory cases that reveal the
fluidity of political discourse, we perform several analyses.
First, we employ large language models (LLMs) to classify
stance toward Europe, Russia, and the Moldovan candidates
Sandu and Stoianoglo. Second, we construct temporally prox-
imate retweet and semantic similarity networks, which cap-
ture amplification and content alignment across communities.
These networks allow us to identify central actors, information
flows, and potential signals of aligned narrative activity. Fi-
nally, we employ causal analysis to understand which stances
are influential and contribute to social contagion.
Specifically, in this paper, we address the following ques-
tions related to political discussion on social media:
•Distribution of political stances (RQ1): How were
© 2026 IEEE. Personal use of this material is permitted. Permission from IEEE must
be obtained for all other uses, in any current or future media, including
reprinting/republishing this material for advertising or promotional purposes, creating
new collective works, for resale or redistribution to servers or lists, or reuse of any
copyrighted component of this work in other works.
arXiv:2610.22464v1  [cs.SI]  15 Oct 2026

stances aligned with the main candidates’ positions on EU
integration and relations with Russia distributed across
election-related online discourse?
•Amplification dynamics (RQ2): To what extent do
amplification signals, e.g., rapid retweets and temporally
proximate sharing of similar tweets, shape narrative vis-
ibility and alignment during the elections?
•Network influence of stances (RQ3): Does exposure
to tweets with a political stance (e.g., pro-Europe, anti-
Russia) causally increase the probability that a user later
expresses the same stance?
Our contributions are: (1) we provide the first systematic
account of social media discourse around the 2024 Moldovan
presidential elections, (2) we combine stance classification
with amplification analyses to methodologically analyze elec-
toral data, and (3) we evaluate model-based estimates of peer-
exposure effects to understand the spread of ideas in the
network.
Our code, LLM prompts, and tools are available in the pub-
lic repository: https://github.com/edgeslab/moldova-elections.
II. RELATEDWORK
Research at the intersection of political communication and
computational social science has extensively examined how
social media platforms shape, mediate, and amplify politi-
cal ideas during elections [3], [4]. Platforms like X serve
not only as channels of information but as spaces where
politicians, media, and ordinary users compete to shape the
conversation. In computational approaches, such dynamics
are often measured through network structure and content
signals. For example, [5] propose Retweet-BERT, a model that
infers political leaning from language and retweet patterns,
showing how textual and structural features can jointly reveal
ideological alignments. Different studies have documented
polarization across major electoral events, such as U.S. pres-
idential campaigns [1], [3] and European elections [6]–[8],
illustrating how political cleavages are mirrored in network
connectivity, stance expression, and engagement. Similar work
examines the effect of political discourse on echo chambers,
self-reinforcing network structures in which users are dis-
proportionately exposed to ideologically aligned content [9]–
[11]. Other work on polarization highlights how emotionally-
charged content drives engagement between groups [12], [13],
shaping the diffusion of political narratives online.
A second group of research focuses on coordinated be-
havior and amplification, a central theme in recent studies
of campaign dynamics. Synchronization in posting activity,
especially through retweets and news-sharing, can signal or-
ganized efforts to boost specific narratives or actors [14],
[15]. Classic approaches leveraged engagement networks to
classify coordinated campaigns [16], [17]. More recent studies
identified coordination by detecting temporal clustering, co-
retweeting, and domain-sharing spikes [8].
A third group of work focuses on stance detection and
topic modeling, both of which are widely used to map user
attitudes and ideological alignments. Stance detection has
evolved from lexicon-based and supervised approaches [18], to
zero-shot transformer-based methods capable of scaling across
domains [19]. This shift has enabled researchers to analyze
topics in low-resource contexts where labeled data are scarce.
Cross-lingual stance and topic detection techniques [20], [21]
have enabled the examination of how narratives are framed
across linguistic communities. Applications to politics are
common, with work analyzing major political elections [7]
and events, such as international conflicts [22].
Finally, a growing line of research applies causal inference
methods to social platforms to estimate how exposure to infor-
mation shapes user behavior. Traditional observational analy-
ses are often limited by latent homophily, making it difficult
to distinguish peer influence from shared preferences. Recent
work has used matching and instrumental variable approaches
to separate influence from selection in network data [23], often
in the context of social contagion and diffusion. Similar work
demonstrates that high-dimensional adjustment can reduce
bias relative to experimental benchmarks [24], [25]. More
recently, attention has shifted toward the role of interference in
networked settings. [26] show that cluster-based randomization
can be biased in settings where influence propagates through
multi-hop cascades. They propose a cascade-aware experimen-
tal design that underscores the importance of accounting for
this interference in studies of social media influence. Recent
methodological advances also focus on estimating individual
and heterogeneous causal effects under complex peer influence
mechanisms, including approaches that explicitly model the
influence of neighbors’ behaviors on outcomes [27], [28], but
do not address hidden confounding. Within this context, [29]
combine representation learning and balancing techniques to
estimate contagion effects under hidden confounding.
Our work brings these works together by combining multi-
lingual topic and political stance detection, coordination anal-
ysis, and causal effect estimation in the context of a politically
sensitive election that has received little prior attention. Un-
like other studies, which focused on major Western electoral
contexts, this work examines an underexplored region with
complex linguistic and geopolitical divisions, offering new
insights into how narratives spread, align, and gain traction
during political campaigns.
III. DATA
Our study analyzes election-related discourse surrounding
the 2024 Moldovan presidential election using social media
data obtained as part of a broader, grant-funded data collection
program. The program used a third-party provider to collect
election-related posts from X, Facebook, and Reddit based
on specific keywords (provided in the Appendix). The data
was accessed in accordance with platform terms of service
and regulatory constraints. The program did not reveal the
budgetary constraints of the data collection or the name of
the data provider. The extraction strategy was designed by
the program to maximize topical and actor-level coverage
of election-related discourse across platforms. As a result,
the completeness of interaction data vary by platform: X

provides the most comprehensive interaction data (retweets),
whereas Reddit and Facebook offer limited engagement infor-
mation beyond each individual post. The dataset consists of
52,696 publicly available posts posted between August 1 and
October 25, 2024, covering the main campaign period and
the first round of the Moldovan presidential election. Daily
volume remains relatively low from August through mid-
October, followed by a sharp spike around the election date on
October 20, 2024. Approximately 34.7% of all collected posts
were published within the three-day election window from
October 19-21, indicating that a substantial share of the dataset
captures discourse during the immediate election-period surge.
After filtering duplicate content and posts without textual
content, X includes 45,695 posts from 30,940 unique ac-
counts. When available, missing parent tweets were retrieved
to preserve conversational context and enable analyses of
retweet and reply behavior. Each tweet is associated with
its full text, timestamp, detected language, and engagement
metrics, including retweets, quotes, replies, and likes. Reddit
and Facebook data provide complementary perspectives, albeit
with less information available on engagement and interactions
(e.g., reposts). Reddit includes 3,555 posts and comments
from 2,812 unique accounts, which contain textual content,
timestamps, and author identifiers, allowing partial recon-
struction of reply relationships, though parent–child links are
incomplete for a substantial fraction of comments. Facebook
includes 3,446 posts from 393 users, containing post text and
timestamps, but lacking information on reshares, replies, or
interaction networks. As a result, network and causal analyses
requiring fine-grained interaction structure are restricted to X.
Fig. 1 reports the distribution of languages across platforms,
highlighting the prominence of Romanian (80%) and Russian
(10%) in Facebook posts, and of English (77% and 75%) and
Romanian (21% and 7%) within Reddit and X communities.
Fig. 1. Normalized heatmap of language share within each platform. Only the
eight most frequent languages are shown individually; all remaining languages
are aggregated into an “Other” category. For Facebook, 80% of posts are in
Romanian, while for Reddit and X, more than 75% of posts are in English.
Text preprocessing included lowercasing, punctuation re-
moval, language detection, and machine translation for
non-English content, enabling cross-lingual analysis. Mul-
tilingual sentence embeddings were generated for all
posts using theSentenceTransformer-paraphrase
multilingual-mpnet-base-v2model [30].
To uncover the themes driving political debates, we first per-
formed topic modeling on the posts from all three platforms.
We adopted an embedding-based topic extraction pipeline as
implemented in BERTopic [31], which has been shown to
perform better than other topic models [32]. This approach
provides fine-grained yet interpretable clusters and is more
robust to the linguistic variability and fragmentary nature of
social media posts, making it well-suited to the structure of
our dataset. While BERTopic produces high-quality clusters
and representative keywords, it does not automatically gen-
erate human-readable topic labels. To do so, we extracted
the most informative keywords for each cluster based on
their TF–IDF scores and used these as the basis for expert
interpretation. Domain experts reviewed the top-ranked words
and associated post samples for each cluster to assign short,
human-readable labels summarizing the main theme. Finally,
we excluded topics deemed not relevant to the elections. The
top three identified topics (“Moldova, EU membership, Russia,
and regional identity”, “Ukraine, Russia, NATO, and post-
Soviet geopolitics”, and “President Maia Sandu and Moldovan
presidential elections”) account for64%of all posts in the
dataset. The complete list of topics and their frequencies can
be found in the Appendix.
Fig. 2 further compares the relative prevalence of major
topics across platforms, restricting attention to topics that
account for at least2%of posts on at least one platform.
Fig. 2. Distribution of topics accounting for at least2%of posts on
at least one platform. X and Reddit communities display similar attention
to geopolitical issues, whereas Facebook users predominantly engage with
discussions centered on domestic governance.
Across all three platforms, discussion is strongly dominated
by a small set of high-level themes, most notably the one
related to Moldova’s geopolitical positioning, European in-
tegration, and relations with Russia. This topic consistently
represents the single largest share of posts on X, Reddit, and

Fig. 3. Distribution of macro-topics within each language community across platforms. Across X, Facebook, and Reddit, “Domestic Politics & Governance”
accounts for the largest share of posts in all language groups, particularly on Facebook, where it represents60%-80%of content. “Geopolitics & EU
Integration” is comparatively more prominent among English and Russian posts, especially on Reddit and X. “Society & Civic Life” receives greater attention
within Romanian-language discourse across platforms, while “Culture, Religion, & Conflict” consistently represents a small fraction of discussion.
Facebook (57%,55%, and50%of posts, respectively), indicat-
ing a shared core focus across platforms. Beyond this dominant
theme, however, the distribution of attention varies by plat-
form. On X and Reddit, secondary topics remain relatively
broad and internationally oriented, with substantial attention
devoted to Ukraine-Russia geopolitics and NATO, as well as
to broader regional dynamics. In contrast, Facebook shows
greater emphasis on domestic political processes, including
referendum outcomes, voter turnout, Chisinau events, and
campaign-specific developments. Fig. 3 further analyzes these
differences by showing how language communities are dis-
tributed across topics within each platform. For interpretability,
we manually grouped fine-grained topics into a smaller set
of macro-topics capturing broader narrative categories: 1)
“Geopolitics and EU Integration”; 2) “Society and Civil Life”;
3) “Domestic Politics and Governance”; 4) “Culture, Religion,
and Conflict”. The topic grouping and mapping procedure is in
the Appendix. On X, the majority of posts for each language
(>60%) focus on “Domestic Politics and Governance”,
indicating that election-related discourse is primarily framed
around internal political dynamics across language commu-
nities. The Romanian community then focuses on “Society
and Civil Life” (∼20%), suggesting greater attention to the
election’s social and civic implications. A similar but more
balanced pattern appears on Reddit for the Romanian, English,
and “Other” language communities (25−50%for “Domestic
Politics and Governance” and “Geopolitics and EU Integra-
tion”). In contrast, Russian-language posts focus primarily on
“Geopolitics and EU Integration” (∼60%), consistent with
a discourse that accentuates external relations over internal
governance. On Facebook, all language communities show a
stronger concentration on “Domestic Politics and Governance”
(60−80%of the share), reinforcing the platform’s role as a
space for locally oriented political discussion, with a secondary
share (∼25%) of “Society and Civil Life” posts among the
Romanian and Russian communities. Across all languages
and platforms, “Culture, Religion, & Conflict” consistently
represents the least-discussed topic, accounting for only a
small fraction within each language community.
IV. DISTRIBUTION OF POLITICAL STANCES(RQ1)
A central goal of this work is to characterize the emer-
gence and evolution of geopolitical alignments during the
2024 Moldovan presidential election. To this end, we identify
political stance expressed at the tweet level and analyze
how these alignments vary over time and across platforms
and language communities. Each tweet was annotated along
two primary axes reflecting the main political cleavage in
the Moldovan election: stance toward the European Union
and/or the presidential candidate Maia Sandu (which we call
the “Europe” stance), and stance toward Russia and/or the
candidate Alexandr Stoianoglo (which we call the “Russia”
stance). For each axis, tweets were assigned one of three
labels:pro,anti, orneutral. Posts were allowed to receive mul-
tiple labels across axes (e.g., “pro-Europe” and “anti-Russia”),
reflecting the mixed framing of political discourse during
the campaign. Political stance annotation was performed us-
ing a large language model (LLM), Gemini [33], through
a structured prompting pipeline. We employed a few-shot
prompting strategy augmented with chain-of-thought (CoT)
reasoning [34], in which the model was provided with concise
labeled examples and instructed to produce both a short
rationale and a final stance label for each target dimension.
This design was chosen to improve consistency and robustness
in the presence of sarcasm and indirect political references,
which are common in election-related social media content.
We evaluated multiple prompting configurations, including
zero-shot, few-shot without reasoning, and few-shot with CoT,
against a manually annotated validation set of 200 randomly
selected tweets curated by two domain experts, with disagree-
ments adjudicated through a consensus process. Accuracy was
computed as the proportion of model predictions whose final

stance label matched the annotated human label. The CoT few-
shot configuration achieved the highest agreement and stable
accuracy exceeding 90%, and was therefore applied to the
full dataset. More information on the labeling process and
the different prompting configurations can be found in the
Appendix. Ambiguous or seemingly contradictory cases (e.g.,
simultaneous pro- and anti-stance assignments) were retained
rather than collapsed, as manual inspection indicated that such
cases often arise from quoting, irony, or mixed framing. The
resulting stance annotations form the basis for all downstream
analyses, including temporal trend analysis, coordination and
network-based studies, and causal effect estimation.
Fig. 4. Aggregate distribution of major political stances expressed in election-
related posts. Excluding neutral stance, “anti-Russia”, “anti-Russia & pro-
Europe”, and “pro-Europe” stances constitute the majority of observed content
(5−20%across all platforms), while “pro-Russia” and “anti-Europe” stances
appear less frequently (<5%).
We first examine how contrasting geopolitical and
candidate-aligned stances were distributed across election-
related discourse. Fig. 4 reports the aggregate prevalence of
each major stance category over the full observation period.
Neutral posts represent the largest share of content (43%
for X, and∼70%for Reddit and Facebook). For non-
neutral posts, the conversation is consistently dominated by
“anti-Russia”, “anti-Russia & pro-Europe”, and “pro-Europe”
framing, though the relative proportion differs by platform. X
content has20%of “anti-Russia” posts, and similarly13%
of both “anti-Russia & pro-Europe” and “pro-Europe” posts,
suggesting a discourse that frequently leans towards favoring
a European stance. Reddit shows a less balanced profile, with
“anti-Russia” occupying13%of content, while the remaining
stances each account for less than5%of posts. Facebook,
in contrast, places greater weight on “pro-Europe” (13%)
than on “anti-Russia” and “anti-Russia & pro-Europe”, each
amounting to less than5%of posts. Explicitly “pro-Russia”
or “anti-Europe” positions remain rare across platforms.
To examine temporal dynamics, we focus on non-neutral
stance categories that account for at least5%of posts in at
least one of the social media, ensuring sufficient volume for
reliable trend analysis. Fig. 5 shows the daily volume of these
dominant stances over time. Two patterns stand out. First, posts
with “pro-Europe” and “anti-Russia & pro-Europe” stances
show pronounced temporal variability, with increases to 3,600
and 2,700 posts shared immediately after the first round of
the election on October 20, 2024. Second, the composition of
this peak is highly asymmetric: posts expressing “pro-Europe”,
Fig. 5. Daily volume of stance-labeled posts over time. The vertical line marks
the first round of the Moldovan presidential election on October 20, 2024.
“pro-Europe”, “anti-Russia”, and “anti-Russia & pro-Europe” stances exhibit
the most pronounced post-election surge.
“anti-Russia”, and “anti-Russia & pro-Europe” stances account
for the vast majority of the surge, with activity increasing by
orders of magnitude relative to earlier baselines. In contrast,
“anti-Europe” content also rises but remains substantially
lower in volume, peaking at approximately 1,200 posts.
V. AMPLIFICATIONDYNAMICS(RQ2)
To examine how narratives were amplified and aligned dur-
ing the 2024 Moldovan presidential elections, we conducted
a amplification analysis on X accounts. Given the lack of
reshare information on Reddit and Facebook, we excluded
these platforms from the analysis. Amplification can emerge
both organically (e.g., reactions to a breaking event) and strate-
gically (e.g., organized campaigns or information operations).
Identifying these patterns provides insight into how infor-
mation is propagated collectively, which actors contribute to
narrative diffusion, and how different groups structure their ac-
tivity for visibility. Our analysis builds on two complementary
amplification signals, temporal synchronization in retweeting
and message posting, which reflect behavior in amplifying or
repeating messages. Inspired by the methodology proposed
by [35] and [16], we analyze these signals using rapid-retweet
and rapid semantic-similarity networks.
Rapid Retweet Networks.We first constructed rapid retweet
networks. To select the temporal threshold, we conducted
a sensitivity analysis following the approach of [35]. We
evaluated three candidate values for∆t(60 s, 1 hour, 24 hours)
and examined their effects on network density, clustering
coefficient, and edge weight distribution (Analysis shown in
the Appendix). The 60 s threshold provides the best signal
for rapid synchronization and coordination (similar works
use up to 5 minutes as the threshold [36], [37]), but cov-
ers only a small fraction of the retweet activity and yields
a much smaller network. We therefore use 1 hour as the
primary descriptive threshold for event-scale synchronized
engagement, while interpreting it as a broad amplification
signal rather than evidence of orchestrated coordination. The
resulting rapid retweet network, constructed using the 1-hour
temporal threshold, exhibits a sparse global structure with
a pronounced, more connected core of 5,501 nodes with
an average degree of 2.32. Fig. 6 shows the core subgraph
with nodes representing users and edges indicating amplifi-
cation, through retweets, of the same content within the 1-

Fig. 6. Rapid retweet subgraph using a 1-hour temporal threshold. Nodes
represent users; edges connect users who retweeted another user’s content
within the threshold. The node size reflects the number of interacting users.
hour window. This central component concentrates a large
fraction of amplification activity and is surrounded by smaller,
weakly connected clusters (1-5 users). Manual inspection
of the highest-degree nodes in the core reveals that they
correspond primarily to prominent political actors, interna-
tional news outlets, journalists, activist accounts, and satirical
collectives. Examples include official political accounts (e.g.,
@SanduMaiaMd, @vonderleyen), Russo-Ukrainian war re-
porting accounts (e.g., @wartranslated), journalists monitoring
Russian state media (e.g., @JuliaDavisNews), and opposition-
aligned Eastern European news outlets (e.g., @visegrad24).
Despite their heterogeneity in role and affiliation, these ac-
counts overwhelmingly express or amplify “anti-Russia” and
“pro-Europe” narratives. Illustrative examples are reported in
the Appendix. Thus, amplification during the election was
not evenly distributed across stances: narratives from news
outlet and political actors opposing Russian influence and
supporting European integration were the primary objects
of amplification. In contrast, “pro-Russia” and “anti-Europe”
content appears in smaller, more fragmented clusters that
remain weakly connected to the central component, suggesting
lower visibility within this retweet-based structure.
Rapid Semantic Networks.We extended this logic to original
tweet content by detecting temporally proximate posting of
semantically similar messages. This step captures cases where
accounts may not retweet the same post but instead produce
similar framing within the same event-scale time window,
highlighting semantic alignment patterns that can arise from
coordinated messaging, shared attention to events, or common
narratives. We first removed retweets from the dataset, as this
would cause same-text posts to be connected in the resulting
network, without providing any additional insight. We then
generated multilingual sentence embeddings for all tweets and
computed pairwise cosine similarity. Tweets exceeding a co-
sine similarity threshold and posted within the same temporal
window were clustered, and accounts involved were connected
in a semantic alignment network. While the retweet network
captures synchronized amplification of the same content, the
semantic network offers a complementary perspective on how
similar narratives circulate across accounts.
We applied a cosine similarity threshold of 0.85, chosen
through sensitivity analysis analogous to the retweet case.
Lower thresholds (e.g., 0.70) resulted in overly dense graphs
dominated by weak, noisy matches, while higher thresholds
(e.g., 0.90) produced very sparse networks dominated by near-
duplicate content. The 0.85 threshold balanced network inter-
pretability and cluster detection, aligning with prior findings
in coordinated behavior research [35]. As with the retweet
network, we interpret the 1-hour temporal window as capturing
event-scale semantic alignment and trending information.
Compared to the rapid retweet network, this graph is
substantially smaller (436 users) and forms a single, more
interconnected core, surrounded by a larger set of small
clusters (1-2 users), albeit with a higher average degree of
5.5. This indicates that semantic alignment captures a narrower
set of behaviors, primarily reflecting near-duplicate or closely
related framing. Within this semantic network, we focused
on alignment around non-neutral stances. Fig. 7 presents the
rapid semantic similarity alignment network core, excluding
the “neutral” stance-aligned posts. Due to the lack of direct
information about usernames, we were unable to infer knowl-
edge about hub accounts at the center of the clusters.
Fig. 7. Semantic similarity alignment subgraph capturing posts that are both
semantically similar and temporally proximate. Edges indicate high cosine
similarity. The node size reflects the number of users posting similar tweets.
The alignment clusters show a prevalence of “pro-Europe” discourse.
There is a concentration, particularly of “pro-Europe” and,
secondly, of “anti-Russia & pro-Europe” and “anti-Russia” po-
sitions. The cluster corresponds to bursts of similar messaging
around topics opposing Russian influence, including foreign
interference, electoral legitimacy, and regional security.
VI. CAUSALEFFECTS OFEXPOSURE ONSTANCE
EXPRESSION(RQ3)
The final component of our analysis examines whether
exposure to political stance content affects users’ subsequent
expression of similar views. To move beyond correlation, we
adopt a proximal causal inference framework [38] that lever-
ages high-dimensional proxies to estimate treatment effects

under unobserved confounding. Specifically, we would like
to understand whether certain stances are contagious and can
influence people on social media. Unlike descriptive correla-
tions between political language and engagement, measuring
peer influence in social media requires accounting for latent
confounders such as homophily and network clustering.
Our causal setup follows the proximal embeddings
(ProEmb) framework for estimating contagion effects in social
networks [29]. We focus on one stance dimension at a time
(e.g., “anti-Europe”), which we call the target stance, and
construct tweet-level observations for each user. For each
target stance, we define theoutcomefor each tweet based
on whether it expresses that stance (binary indicator based
on our stance labels). Thetreatmentfor that tweet captures
whether the user had prior observable exposure to that stance
through the user’s peers. We define peers as the authors
of tweets that a user has retweeted in the past, and then
aggregate all of these peers’ tweets posted before each ego
tweet timestamp. Treatment is set to one if at least one of
these peer tweets expresses the target stance; otherwise, it is
zero. Our treatment estimation captures the effect of prior
stance-aligned content produced by accounts to whom the
ego has revealed attention through retweeting. As platform
exposure logs are not available, this treatment definition should
be interpreted as interacted exposure, rather than as complete
exposure to all content a user may have seen. For each target
stances, we define causal effects at the tweet level. LetY (s) i,t
denote the outcome for an ego tweet posted by useriat
timet, representing whether the tweet expresses stances. Let
T (s) i,t denote the treatment indicator capturing prior exposure
to stancesthrough the user’s peers. The individual treatment
effect (ITE) measures how exposure to stancescausally
changes the expected outcome for a specific ego tweet, by
comparing the counterfactual scenarios in which the tweet is
exposed,T (s) i,t = 1, versus not exposed,T (s) i,t = 0:
ITE(s) i,t =E h Y (s) i,t |do  T (s) i,t = 1 i −E h Y (s) i,t |do  T (s) i,t = 0 i .
The average treatment effect (ATE) aggregates these indi-
vidual effects across all ego tweets and captures the average
causal impact of prior exposure to stanceson stance expres-
sion in the population:
ATE(s) =E  Y (s) |do  T (s) = 1  −E  Y (s) |do  T (s) = 0  .
ProEmb relies on a set of explicit assumptions: Rather than
assuming that all confounders are directly measured, ProEmb
leverages high-dimensional proxy variables constructed from
observed ego and peer content that are informative of these
latent factors. Thus, conditional on a suitable representation
of these proxies, the unobserved confounders affecting both
network formation and individual behavior are sufficiently
accounted for, enabling identification of causal effects of
exposure through the ego network [29].
To construct the high-dimensional proxies used in ProEmb,
we start from the full stance-annotated dataset and restrict it to
X posts, due to the less consistent information across the other
platforms. For each tweet, we retain the author ID, timestamp,
text, stance label for the target category, and emotion scores
(already available in the provided dataset). We then build an
ego–peer structure from the retweet graph: for each retweet,
we record the retweeter (ego) and the original author (peer),
and group tweets chronologically by user. For every ego tweet,
we gather (i) the ego’s own text and emotion scores at that
time, and (ii) the collection of all past tweets by their peers
(those authored before the ego tweet). Peer texts are concate-
nated and embedded, and peer emotion scores are averaged
across tweets. This yields two feature vectors: anegofeature
vector (embedding of the current tweet plus its emotions) and
apeerfeature vector (embedding of accumulated peer content
plus mean peer emotions). Given the presence of multiple
languages in the dataset, we use the multilingual model
paraphrase-multilingual-MiniLM-L12-v2[39] to
generate sentence embeddings. In our implementation, we
concatenate ego and peer features to form the proxy input,
which is then encoded into a latent representation. This latent
code acts as a balancing score: treated and control observa-
tions with similar latent representations are comparable under
the proximal causal framework. Using these representations,
ProEmb estimates causal effects by explicitly modeling coun-
terfactual outcomes. For each target stances, two outcome
models are trained: one using ego tweets observed under
exposure to that stance (T (s) i,t = 1) and one using ego tweets
observed without such exposure ((T (s) i,t = 0). Each model
predicts the probability that an ego tweet expresses the target
stance. Counterfactual outcomes are obtained by applying
these models crosswise: the model trained on exposed tweets
is applied to unexposed tweets to predict outcomes as if they
had been exposed, and vice versa. The ITE for a tweet is
computed as the difference between these two predicted out-
comes, holding observed covariates fixed. The ATE is obtained
by aggregating ITEs across tweets, and is also estimated via
inverse probability weighting in the latent space [29].
TABLE I
AVERAGE TREATMENT EFFECT(ATE) PROEMB ESTIMATES OF EXPOSURE
TO STANCE-ALIGNED CONTENT ON SUBSEQUENT STANCE EXPRESSION.
n1/n0 DENOTES THE TREATED/CONTROL SAMPLE SIZES.
Stance ATE (ProEmb)n 1/n0
Pro-Europe0.218±0.034 614/703
Pro-Russia0.517±0.0002 21/1,296
Anti-Europe0.251±0.043 160/1,157
Anti-Russia0.253±0.021 840/477
Table I reports the ProEmb estimates averaged across ten
random seeds, together with the treated and control sample
sizes. Across all stance categories, ProEmb yields positive and
statistically significant average causal effect estimates, indicat-
ing that prior exposure to stance-aligned content increases the
probability that a user subsequently expresses the same stance.
The estimated ATEs are relatively consistent in magnitude:
exposure to “pro-Europe” content is associated with an average
increase of0.218in the probability of stance expression, while
“anti-Europe” and “anti-Russia” exposures yield comparable
effects of0.251and0.253, respectively. The estimated effect

Fig. 8. Individual treatment effect (ITE) of exposure to stance-aligned content on expression of similar stances in subsequent tweets, obtained with ProEmb.
for “pro-Russia” exposure is substantially larger in magnitude
(0.517), exceeding the effects observed for all other stances.
However, this estimate should be interpreted with caution
due to the relatively small number of treated observations in
this category, which limits statistical precision and increases
sensitivity to modeling assumptions.
Fig. 8 further illustrates the heterogeneity at the user level
through the distribution of estimated ITE. Although the major-
ity exhibit modest treatment effects, the distributions are right-
skewed, revealing a subset of users who, when exposed, have
an increased likelihood of stance-aligned posting. This pattern
suggests that peer exposure does not uniformly influence
behavior, but instead disproportionately affects a smaller group
of highly responsive users. The list of hyperparameters and
models used for ProEmb can be found in the Appendix.
VII. DISCUSSION
Across platforms, the conversation is dominated by narra-
tives related to European integration and opposition to Russian
influence, particularly during periods of increased political
interest around the election. This dominance is visible not only
in aggregate volume but also in the structure of interaction,
with these narratives occupying the most central positions
in both retweet-based amplification and semantic alignment
networks. The Moldovan election was organized around a
geopolitical discussion in which EU integration and Russian
influence were central political issues. These asymmetries
instead suggest that the online discourse we observe was not a
balanced contest between equally visible parties. Instead, the
conversation was structured around a dominant pro-European
and anti-Russian frame, with alternative narratives appearing
less visible and less structurally amplified.
Amplification patterns further differentiate how narratives
propagate. Retweet networks exhibit a dense core composed
of highly active accounts repeatedly amplifying a narrow set
of messages, while semantic similarity networks reveal more
selective alignment through near-duplicate framing within an
event-scale temporal window. The observed structural dif-
ferences imply that not all narratives benefit equally from
synchronized amplification, even when coordinated-looking
behavior is present. In particular, “pro-Europe” and “anti-
Russia” narratives appear to benefit from both direct amplifi-
cation of prominent political and media accounts and repeated
semantic framing against Russian influence. At the same time,
because the 1-hour window usually captures organic attention
to trending topics [35], these patterns should not be interpreted
as evidence of inauthentic coordination.
Beyond descriptive patterns, causal analysis provides evi-
dence that exposure to stance-aligned content increases the
likelihood of subsequent stance expression. The ProEmb
framework identifies consistent positive effects for several
stance categories. Prior work has shown that political discourse
on social platforms is highly polarized, with users embed-
ded in ideologically homogeneous communities that resemble
echo chambers [3], [9]–[11]. These studies document strong
assortative mixing and selective exposure in political networks,
but largely stop short of establishing whether exposure itself
causally shapes political expression. Our results complement
these studies by showing that, under the proximal identification
assumptions and using observable exposure through retweet-
based peers, exposure to stance-aligned content has a posi-
tive estimated effect on subsequent stance expression. This
suggests that echo chambers are not only a structural prop-
erty of political networks but also a potential reinforcement
mechanism through which already visible narratives become
repeatedly expressed and amplified over time.
Several limitations should be acknowledged. All causal
estimates rely on observational data and proxy-based adjust-
ment, which cannot fully eliminate bias from unmeasured con-
founders. Moreover, our treatment definition captures observ-
able exposure through retweet-based peer ties, not all content
that users may have encountered through algorithmic feeds,
search, screenshots, external media, or offline communication.
An additional source of risk lies in model misspecification.
Estimating peer influence and contagion effects depends on the
ability of the chosen model to capture the relevant exposure
mechanisms, temporal dependencies, and latent confounding
structure. Misspecified models can yield biased or misleading
effect estimates, including overestimating or underestimating
the contagion effects. These limitations call for cautious inter-
pretation, particularly in politically sensitive contexts.
Overall, this work contributes empirical evidence on the
interaction between political narratives, coordination mecha-
nisms, and peer influence in a geopolitically salient election.
By combining language-based annotation with network and
causal methods, the study demonstrates the value of integrated
analytical frameworks for understanding political communica-
tion in social media public environments.

REFERENCES
[1] P. Barber ´a, “Birds of the same feather tweet together: Bayesian ideal
point estimation using twitter data,”Political analysis, vol. 23, no. 1,
pp. 76–91, 2015.
[2] Y . M. C ¸ etinkaya, V . Ghafouri, G. Suarez-Tangil, J. Such, and T. Elmas,
“Cross-partisan interactions on twitter,” inProceedings of the Interna-
tional AAAI Conference on Web and Social Media, vol. 19, 2025, pp.
324–340.
[3] M. Conover, J. Ratkiewicz, M. Francisco, B. Gonc ¸alves, F. Menczer,
and A. Flammini, “Political polarization on twitter,” inProceedings of
the International AAAI Conference on Web and Social Media, vol. 5,
no. 1, 2011, pp. 89–96.
[4] S. Stier, A. Bleier, H. Lietz, and M. Strohmaier, “Election campaigning
on social media: Politicians, audiences, and the mediation of political
communication on facebook and twitter,” inStudying politics across
media. Routledge, 2020, pp. 50–74.
[5] J. Jiang, X. Ren, and E. Ferrara, “Retweet-bert: political leaning
detection using language features and information diffusion on social
networks,” inProceedings of the international AAAI conference on web
and social media, vol. 17, 2023, pp. 459–469.
[6] S. Stier, S. A. Popa, Y . Theocharis, and B. Boyle, “Online election
campaigning in changing political environments: A comparison of
the 2014 and 2019 european parliament elections,”Party Politics, p.
13540688251317855, 2025.
[7] A. M ¨uller, J. Riedl, and W. Drews, “Real-time stance detection and issue
analysis of the 2021 german federal election campaign on twitter,” in
International Conference on Electronic Government. Springer, 2022,
pp. 125–146.
[8] L. Nizzoli, S. Tardelli, M. Avvenuti, S. Cresci, and M. Tesconi, “Co-
ordinated behavior on social media in 2019 uk general election,” in
Proceedings of the international AAAI conference on web and social
media, vol. 15, 2021, pp. 443–454.
[9] K. Garimella, G. De Francisci Morales, A. Gionis, and M. Mathioudakis,
“Political discourse on social media: Echo chambers, gatekeepers, and
the price of bipartisanship,” inProceedings of the 2018 world wide web
conference, 2018, pp. 913–922.
[10] M. Cinelli, G. De Francisci Morales, A. Galeazzi, W. Quattrociocchi, and
M. Starnini, “The echo chamber effect on social media,”Proceedings
of the national academy of sciences, vol. 118, no. 9, p. e2023301118,
2021.
[11] F. Cinus, M. Minici, C. Monti, and F. Bonchi, “The effect of people
recommenders on echo chambers and polarization,” inProceedings of
the International AAAI Conference on Web and Social Media, vol. 16,
2022, pp. 90–101.
[12] W. J. Brady, J. A. Wills, J. T. Jost, J. A. Tucker, and J. J. Van Bavel,
“Emotion shapes the diffusion of moralized content in social networks,”
Proceedings of the National Academy of Sciences, vol. 114, no. 28, pp.
7313–7318, 2017.
[13] Y . Gao, W. Qin, A. Murali, C. Eckart, X. Zhou, J. D. Beel, Y .-C. Wang,
and D. Yang, “A crisis of civility? modeling incivility and its effects
in political discourse online,” inProceedings of the International AAAI
Conference on Web and Social Media, vol. 18, 2024, pp. 408–421.
[14] K. Burghardt, A. Rao, G. Chochlakis, B. Sabyasachee, S. Guo, Z. He,
A. Rojecki, S. Narayanan, and K. Lerman, “Socio-linguistic charac-
teristics of coordinated inauthentic accounts,” inProceedings of the
international AAAI conference on web and social media, vol. 18, 2024,
pp. 164–176.
[15] Y . Zhu, E.-U. Haq, G. Tyson, L.-H. Lee, Y . Wang, and P. Hui, “A
study of partisan news sharing in the russian invasion of ukraine,” in
Proceedings of the International AAAI Conference on Web and Social
Media, vol. 18, 2024, pp. 1847–1858.
[16] D. Pacheco, P.-M. Hui, C. Torres-Lugo, B. T. Truong, A. Flammini, and
F. Menczer, “Uncovering coordinated networks on social media,”arXiv
preprint arXiv:2001.05658, vol. 16, 2020.
[17] D. Pacheco, A. Flammini, and F. Menczer, “Unveiling coordinated
groups behind white helmets disinformation,” inCompanion Proceed-
ings of the Web Conference 2020. ACM, 2020, pp. 611–616.
[18] I. Augenstein, A. Vlachos, and K. Bontcheva, “Usfd at semeval-2016
task 6: Any-target stance detection on twitter with autoencoders,” in
Proceedings of the 10th international workshop on semantic evaluation
(SemEval-2016), 2016, pp. 389–393.
[19] M. Taranukhin, V . Shwartz, and E. Milios, “Stance reasoner: Zero-shot
stance detection on social media with explicit reasoning,”arXiv preprint
arXiv:2403.14895, 2024.
[20] R. Zhang, N. Xu, H. Yang, Y . Tian, and W. Mao, “Target-oriented
relation alignment for cross-lingual stance detection,” inFindings of
the Association for Computational Linguistics: ACL 2023, 2023, pp.
6391–6404.
[21] F. Bianchi, S. Terragni, D. Hovy, D. Nozza, and E. Fersini, “Cross-
lingual contextualized topic models with zero-shot learning,” inProceed-
ings of the 16th conference of the European chapter of the association
for computational linguistics: Main volume, 2021, pp. 1676–1683.
[22] I. Kloo, I. J. Cruickshank, and K. M. Carley, “A cross-platform topic
analysis of the nazi narrative on twitter and telegram during the 2022
russian invasion of ukraine,” inProceedings of the international AAAI
conference on web and social media, vol. 18, 2024, pp. 839–850.
[23] S. Aral, L. Muchnik, and A. Sundararajan, “Distinguishing influence-
based contagion from homophily-driven diffusion in dynamic networks,”
Proceedings of the National Academy of Sciences, vol. 106, no. 51, pp.
21 544–21 549, 2009.
[24] C. R. Shalizi and A. C. Thomas, “Homophily and contagion are generi-
cally confounded in observational social network studies,”Sociological
methods & research, vol. 40, no. 2, pp. 211–239, 2011.
[25] D. Eckles, B. Karrer, and J. Ugander, “Design and analysis of experi-
ments in networks: Reducing bias from interference,”Journal of Causal
Inference, vol. 5, no. 1, p. 20150021, 2017.
[26] Z. Fatemi, J. Pouget-Abadie, and E. Zheleva, “Cascade-based random-
ization for inferring causal effects under diffusion interference,” in
Proceedings of the International AAAI Conference on Web and Social
Media, vol. 18, 2024, pp. 394–407.
[27] S. Adhikari and E. Zheleva, “Inferring individual direct causal effects
under heterogeneous peer influence,”Machine Learning, vol. 114, no. 4,
p. 113, 2025.
[28] S. Adhikari, S. Medya, and E. Zheleva, “Learning exposure mapping
functions for inferring heterogeneous peer effects,”arXiv preprint
arXiv:2503.01722, 2025.
[29] Z. Fatemi and E. Zheleva, “Contagion effect estimation using proximal
embeddings,” inCausal Learning and Reasoning. PMLR, 2025, pp.
243–259.
[30] N. Reimers and I. Gurevych, “Sentence-bert: Sentence embeddings using
siamese bert-networks,” inProceedings of the 2019 Conference on
Empirical Methods in Natural Language Processing and the 9th Inter-
national Joint Conference on Natural Language Processing (EMNLP-
IJCNLP), 2019, pp. 3982–3992.
[31] M. Grootendorst, “Bertopic: Neural topic modeling with a class-based
tf-idf procedure,”arXiv preprint arXiv:2203.05794, 2022.
[32] R. Egger and J. Yu, “A topic modeling comparison between lda, nmf,
top2vec, and bertopic to demystify twitter posts,”Frontiers in sociology,
vol. 7, p. 886498, 2022.
[33] G. Comanici, E. Bieber, M. Schaekermann, I. Pasupat, N. Sachdeva,
I. Dhillon, M. Blistein, O. Ram, D. Zhang, E. Rosenet al., “Gem-
ini 2.5: Pushing the frontier with advanced reasoning, multimodality,
long context, and next generation agentic capabilities,”arXiv preprint
arXiv:2507.06261, 2025.
[34] P. Sahoo, A. K. Singh, S. Saha, V . Jain, S. Mondal, and A. Chadha,
“A systematic survey of prompt engineering in large language models:
Techniques and applications,”arXiv preprint arXiv:2402.07927, 2024.
[35] B. De Clerck, J. C. F. Toledano, F. Van Utterbeeck, and L. E. Rocha,
“Detecting coordinated and bot-like behavior in twitter: The j ¨urgen
conings case,”EPJ Data Science, vol. 13, no. 1, p. 40, 2024.
[36] L. H. X. Ng and K. M. Carley, “Online coordination: methods and
comparative case studies of coordinated groups across four events in the
united states,” inProceedings of the 14th ACM Web Science Conference
2022, 2022, pp. 12–21.
[37] T. Magelinski, L. Ng, and K. Carley, “A synchronized action framework
for detection of coordination on social media,”Journal of Online Trust
and Safety, vol. 1, no. 2, 2022.
[38] E. J. T. Tchetgen, A. Ying, Y . Cui, X. Shi, and W. Miao, “An introduction
to proximal causal learning,”arXiv preprint arXiv:2009.10982, 2020.
[39] N. Reimers and I. Gurevych, “Sentence-bert: Sentence embeddings
using siamese bert-networks,” inProceedings of the 2019 Conference
on Empirical Methods in Natural Language Processing. Association
for Computational Linguistics, 11 2019. [Online]. Available: http:
//arxiv.org/abs/1908.10084

I. BROADERPERSPECTIVE ANDETHICS
All data used in this study were publicly available and
collected in accordance with the platforms’ terms of service.
To minimize risks to users, all identifiable information was
removed, and analyses were conducted on aggregated data
only. Data were publicly collected in the United States and
did not require user consent, leading us to assess the poten-
tial negative impacts of data use as minimal. This analysis
aims to provide positive societal value by improving the
understanding of information campaign tactics. The findings
may help researchers identify and mitigate similar forms of
coordinated activity in future political contexts. The presence
of measurable stance contagion also raises important ethical
considerations regarding the societal implications of social
influence in online political environments. By demonstrating
that exposure to stance-aligned content can causally affect
subsequent expression, our findings highlight a mechanism
through which political narratives may reinforce themselves
over time. In principle, such dynamics could be exploited in
manipulative or strategic ways, for example, by deliberately
amplifying targeted messages to influence opinion formation,
mobilization, or polarization. It is important to emphasize
that we do not propose, develop, or deploy tools for political
persuasion, targeting, or manipulation. Rather, our objective is
to document and quantify the existence of contagion effects in
real-world electoral discourse, contributing empirical evidence
to ongoing discussions about the role of social influence in
digital political communication. Although focused on the 2024
Moldovan presidential election, we can expect that the insights
from this study can be generalized to other political events.
II. DATAEXTRACTION ANDQUERYSTRATEGY
Election-related social media data were collected via a
commercial third-party social media monitoring provider that
aggregates publicly available content from multiple platforms
under platform Terms of Service and applicable data protection
regulations, including GDPR. The provider supports Boolean
keyword queries, metadata-based filtering, and engagement-
based retrieval, while enforcing platform-specific limits on
data volume, retention, and redistribution. The scripts with
relative keywords are available in the repository.
Query Design.To capture a broad range of election-related
discourse, a set of complementary query templates was em-
ployed, targeting (i) political actors and parties, (ii) election-
and referendum-related keywords, (iii) multilingual variants of
core election terms, and (iv) interaction-based content such
as replies, retweets, and quoted posts involving prominent
Moldovan political accounts. Content unrelated to politics
(e.g., sports or entertainment) was explicitly excluded where
possible. In addition, some queries targeted engagement with
specific high-profile accounts to capture secondary discussion
and amplification dynamics beyond original posts. Table II
summarizes the main categories of queries used during data
collection.
Scope and Limitations.The extraction strategy was designed
to capture as much relevant discourse as possible within
practical and legal constraints. However, platform-specific lim-
itations, uneven data availability, and throttling policies may
have resulted in different coverage across users. Furthermore,
because several queries directly name candidates, parties,
Russia/EU-related actors, and engagement with selected ac-
counts, the retrieval design may affect both stance prevalence
and the apparent centrality of narratives. The authors were
not given the provider’s identity, collection budget, complete
retrieval logic, or platform-specific rate limits. As a result,
findings should be interpreted as reflecting observed discourse
within the collected dataset rather than population-level esti-
mates of all online political activity during the election period.
TABLE II
SUMMARY OF QUERY CATEGORIES USED FOR ELECTION-RELATED DATA
EXTRACTION.
Query cate-
gory
Description
Actor-based Mentions of prominent Moldovan political fig-
ures, candidates, and party leaders, including
multilingual name variants.
Party-based References to major political parties and coali-
tions participating in the election, expressed in
multiple languages.
Election
keywords
Proximity-based queries capturing elections,
voting, referendum-related terms, and electoral
procedures across languages.
Interaction-
based
Posts engaging with or authored by key polit-
ical accounts (e.g., replies, retweets, quotes),
used to capture amplification and discussion
dynamics.
Location-
based
Content associated with Moldova or major
cities (e.g., Chis, in˘au), combined with political
keywords to increase contextual relevance.
Platform-
specific
Queries tailored to platform constraints (e.g.,
site-restricted searches or first-post filters) to
improve coverage consistency.
III. POLITICALSTANCECLASSIFICATION ANDLLM
PROMPTING
Before consensus adjudication, the two annotators agreed on
84.6% of the individual label decisions. Mean label-specific
Cohen’sκwas 0.324. All disagreements were subsequently
reviewed and resolved through discussion to establish the final
reference annotations. For classification, we explored multiple
prompting strategies commonly used for this task to assess
robustness and sensitivity to prompt design. Specifically, we
evaluated zero-shot prompting, in which the model is asked
to infer stance labels solely from natural-language definitions;
few-shot prompting, which supplements these definitions with
a small number of labeled examples; Chain-of-Thought (CoT)
prompting, which encourages the model to reason explicitly
before producing a label [34]; and a combined CoT + few-
shot approach that integrates labeled demonstrations with
step-by-step reasoning instructions. The final prompting setup
used in our analysis frames stance classification as a struc-
tured instruction-following task. For each tweet, the model

Fig. 9. Sensitivity of the retweet-based synchronized amplification network to the temporal threshold∆t. Panels (a)–(c) show how network density, network
size, and retweet coverage change as the threshold increases. Dashed vertical lines mark the representative thresholds of 60 s, 1 hour, and 24 hours.
is required to output a fixed-format JSON array indicating
whether the content has a “pro”, “anti”, or “neutral” stance
in the political context of the 2024 Moldovan presidential
election, along with a truncated tweet snippet, the tweet
ID, and an index (for subsequent merging of the stances in
the database). The prompt enforces a two-step decision pro-
cess—first determining whether Russia (and/or the presidential
candidate Stoianoglo) or Europe (and/or the presidential can-
didate Sandu) is mentioned in a relevant political context, and
then assigning sentiment labels conditionally on that mention,
while allowing for mixed sentiment when explicitly present.
To ensure consistency and machine-readability, the prompt
strictly constrains output formatting and provides illustrative
examples covering positive, negative, neutral, mixed, and
non-relevant cases. Furthermore, for each axis, the classifier
returns four binary indicators: pro, anti, neutral, and non-
relevant. Pro and anti may co-occur when a post contains
mixed framing, and neutral is used only when the target is
politically relevant but neither positive nor negative framing
is present. Using the consensus-adjudicated annotations as
the reference, the LLM classifier achieved pooled precision,
recall, and F1 scores of 0.810. Performance was particularly
strong for identifying content unrelated to Russia and Europe
(F1= 0.932and 0.885, respectively), while the anti-Europe
and anti-Russia categories obtained F1 scores of 0.750 and
0.700. The macro-F1 across all eight labels was 0.620, and
variation across categories partly reflects the limited number
of positive examples available for several comparatively rare
stances.
For readability, the complete prompt text and implementation
details are available in the repository.
IV. ADDITIONALRETWEET-NETWORKANALYSES
Fig. 9 reports the sensitivity of the retweet-based synchro-
nized amplification network to the temporal window∆t[35].
As expected, increasing∆texpands the network and in-
creases the fraction of retweets covered, while decreasing
network density. The 60,s threshold provides the strictest
synchronization signal, but covers only a limited share of
retweet activity and yields a comparatively small network. In
contrast, the 24,hour threshold approaches saturation, covering
nearly all retweets, which makes it more likely to capture
general trending-topic dynamics rather than temporally local-
ized amplification. The 1,hour threshold lies between these
two extremes. It substantially increases retweet coverage and
network size relative to the 60,s window, while remaining
below near-saturation, observed at 24,hours. The in-degree and
edge-weight distributions remain heavy-tailed across the three
representative thresholds, suggesting that the amplification
structure is not driven solely by a few isolated edges.
To contextualize the structure of the rapid-retweet network,
Table III lists selected high-degree accounts from its largest
connected component. The examples include political figures,
news organizations, journalists, activist accounts, and satirical
accounts. The account descriptions are based on publicly
available profile information and observed content.
TABLE III
SELECTED HIGH-DEGREE ACCOUNTS IN THE RAPID RETWEET NETWORK.
DESCRIPTIONS ARE BASED ON PUBLICLY AVAILABLE ACCOUNT
INFORMATION AND OBSERVED CONTENT.
Account Description
@SanduMaiaMD Official account of President
Maia Sandu
@vonderleyen Official account of Ursula von
der Leyen, President of the Eu-
ropean Commission
@JuliaDavisNews Journalist and columnist moni-
toring Russian state media
@wartranslated Account translating and repost-
ing Russo-Ukrainian war footage
@nexta tv Eastern European opposition-
aligned news outlet
@IgorSushko Ukrainian–American political
commentator on Eastern Europe
@IamDenya de President of IPN Press Agency,
Moldovan news outlet
@DarthPutinKGB Satirical account critical of
Vladimir Putin
@YourAnonCentral Anonymous political activists
@visegrad24 International news account fo-
cused on Central-Eastern Europe
V. TRAININGDETAILS ANDCOMPUTATIONALRESOURCES
All experiments were conducted on an internal laboratory
server. The system is equipped with a single AMD EPYC
7662 processor (64 cores, 128 threads) and 256 GB of system
memory. GPU-accelerated workloads were run on an NVIDIA
RTX A5000 GPU with 24 GB of VRAM, using CUDA 12.8.
For topic modeling, we used BERTopic [31]. Sentence
embeddings are generated using a transformer-based multi-
lingual embedding model, followed by dimensionality reduc-

tion with UMAP and clustering within the BERTopic frame-
work. The UMAP configuration usesn_neighbors=15,
n_components=5,min_dist=0.0, cosine distance, and
a fixed random seed for reproducibility. BERTopic is in-
stantiated with an n-gram range of(1,3), a minimum topic
size of 15 documents, and a target of 40 topics. These
hyperparameters were chosen to balance topic coherence
and granularity and were not optimized against downstream
tasks. For causal analyses, we used sentence embeddings gen-
erated with theparaphrase-multilingual-MiniLM
-L12-v2model [39]. This choice enables a shared semantic
representation across languages, which is essential given the
multilingual nature of the dataset. We followed the ProEmb
modeling choices and hyperparameter settings recommended
in the original ProEmb paper, without additional tuning [29].
However, we use gradient-boosted decision trees implemented
with LightGBM as the outcome model and rely on text embed-
dings as covariates instead of bag-of-words representations,
which are less suitable for multilingual data. To quantify
sensitivity to stochastic model fitting, we repeated ProEmb
across ten random seeds and report the mean and between-
seed standard deviation.
VI. TOPICPREVALENCE ANDMACRO-TOPICMAPPING
Figure 10 presents the complete ranked distribution of the
retained election-relevant topics. Topic prevalence is strongly
concentrated: the three most frequent topics account for 64%
of the observed posts, while the eight most frequent topics
account for 82%. The remaining topics form a long tail of
comparatively infrequent themes. This concentration motivates
both the main-text focus on topics representing at least 2%
of posts on one platform and the higher-level macro-topic
aggregation reported below.
Fig. 10. Topic prevalence across election-related posts, ordered by frequency
and shown on a logarithmic scale. The distribution exhibits a pronounced long
tail, with a small number of dominant topics and many low-frequency topics.
To facilitate higher-level analysis and cross-platform com-
parison, we manually aggregate generated topics into four
macro-topics. This aggregation is based on a qualitative in-
spection of each topic, aiming to group semantically coherent
themes while preserving interpretability. Table IV reports the
mapping between topics and the corresponding macro-topic.
Considering the qualitative nature of the aggregation process,
language-by-macro-topic comparisons should be interpreted as
exploratory summaries and not as validated category measure-
ments.
TABLE IV
MANUAL AGGREGATION OFBERTOPIC TOPICS INTO MACRO-TOPICS
BASED ON QUALITATIVE INSPECTION OF TOPIC CONTENT.
Macro-Topic Mapped Topic Descriptions
Geopolitics
& EU
Integration
Ukraine, Russia, NATO, and post-Soviet geopolitics
Eastern European countries and regional cooperation
Referendum results and diaspora turnout
EU accession and political stability
Justice reforms and EU cooperation plans
Putin, Trump, and geopolitical propaganda discourse
Statements on Russian politics
Diplomatic visits and international relations
Domestic
Politics &
Governance
Moldova, EU membership, Russia, and regional
identity
President Maia Sandu and presidential elections
Russian media figures and disinformation narratives
Ilan Shor, oligarchy, and pro-Russian political scan-
dals
Ballots, large-scale voting, and election logistics
Society &
Civic Life
Chisinau infrastructure, traffic, and airport news
Independence Day and national celebrations
Police activity, arrests, and public safety
Border control and customs checks
Gender roles and gender-based violence
LGBT rights and civil society debates
Housing conditions and real estate in Chisinau
Culture,
Religion, &
Conflict
Orthodox Church and religious leadership
Russia–Ukraine war and armed forces
War narratives and historical references
Christian faith, rural life, and traditions
Women, careers, and media narratives
Israel, Lebanon, and foreign affairs
