---
title: 'Mapping Consumer Sentiment and Network Dynamics of Perfume Co-Branding Discourse on X/Twitter:
  A Computational Social Network Analysis Approach'
url: https://doi.org/10.58905/apollo.v4i3.691
category: brand
subcategory: case-study
date: 2026-07
venue: Apollo Journal of Tourism and Business
authors:
- Fida Adzkiyatunnida
- Vanessa Gaffar
- Asep Miftahuddin
source: openalex-oa
pdf_url: https://journal.mediadigitalpublikasi.com/index.php/apollo/article/download/691/399
pages: 19
chars: 54037
fetched_at: '2026-11-08T19:32:19+00:00'
kb_version: 1
---

# Mapping Consumer Sentiment and Network Dynamics of Perfume Co-Branding Discourse on X/Twitter: A Computational Social Network Analysis Approach

Mapping Consumer Sentiment and Network Dynamics of
Perfume Co-Branding Discourse on X/Twitter: A
Computational Social Network Analysis Approach
Fida Adzkiyatunnida*, Vanessa Gaffar, Asep Miftahuddin
Faculty of Economics and Business Education, Universitas Pendidikan Indonesia, Bandung,
Indonesia
*Corresponding Email: fidaadzkiya@upi.edu
Abstract. The rapid growth of the global fragrance industry has driven brands
to adopt co-branding strategies to strengthen brand equity and expand market
reach, yet consumer responses to these collaborations in digital spaces remain
fragmented and difficult to predict. This study analyzes the distribution of con-
sumer sentiment, identifies key actors in interaction networks, and explores the
extent to which Twitter -based data can complement the evaluation of fragrance
co-branding strategy. Using an exploratory social media analytics approach
grounded in Digital Public Sphere theory and Social Network Theory, this
study integrates Social Network Analysis with six computational modules,
wordcloud analysis, sentiment analysis, text network analysis, emotion analysis,
trend analysis, and zero-shot classification, applied to 300 public tweets collect-
ed via the SocialX platform during 1–12 January 2026 using fragrance and
brand collaboration keywords. Results show that public discourse was lexically
dominated by neutral sentiment (88%), while zero-shot classification of the
same corpus yielded a positive -leaning distribution (82.33%); these are inter-
preted as two distinct constructs, evaluative polarity versus semantic stance,
alongside a Sentiment Index of +0.28 and a dominant happy-emotion classifica-
tion (92%). Network analysis identified a small number of actors occupying
central or bridging positions in information dissemination, and trend analysis
detected two major activity peaks on January 1 –2, 2026, coinciding with the
New Year transition. These findings offer theoretical implications for applying
Digital Public Sphere and Social Network Theory jointly to fragrance co -
branding discourse, and practical implications for brand managers seeking to
monitor how collaboration discourse is expressed and circulates online.
Keywords: Co-branding, Social Network Analysis, Sentiment Analysis, Digital
Marketing, Consumer Sentiment, Social Media Analytics
1 Introduction
In the past few decades, the global fragrance market has grown to a considerable ex-
tent and by 2030 it is expected to reach a market value of more than USD 70 billion
Apollo: Journal of Tourism and Business
Vol 4, Issue 3, September 2026, Page 864-882
ISSN: 2985-5810 (Media Online)
DOI: https://doi.org/10.58905/apollo.v4i3.691
864

[1]. In such extensive competition, fragrance companies are not only competing in
terms of product quality but also by constructing of identity and management of con-
sumer's perception [2]. Co-branding is a marketing technique that has come into focus
in today's marketing world. Co -branding is business joint venture between two or
more brands to develop a product or campaign which allows the development of
complementary brand equity [3]. Although brand collaborations can generate synergy
for the brand that are felt by consumers, there is a disconnect between that ideal sce-
nario and what happens in the market in response to fragrance co- branding, as the
market is unpredictable and responses are often fragmented. Some brand collabora-
tions bring in confusing brand values into consumer's brain [4]. Yet, it is urgent to
create knowledge on the creation and growth of a consumer's sentiment in the fra-
grance segment towards co-branding in a digital environment.
The previous research has laid the foundations of key concepts such as understand-
ing of co-branding dynamics and consumer behaviour in the digital world. The results
of the Washburn et al. study, which revealed that brand alliances can improve con-
sumers' product evaluations, especially when the brand alliances are well aligned
between the brands of the partnership, is conceptually consistent with recent research
on brand fit and brand alliance effects [5]. In the digital environment, social media
has become an important platform for marketing and consumer engagement and
brands have gained more visibility and reach through the use of influencers, and run-
ning campaigns online [6]. For instance, several studies have identified the potentials
of X/Twitter to be used in public discussion where it facilitates real -time sharing and
interaction. Because of the dynamic nature of Twitter's networks, the most central and
most engaged users with respect to topic networks tend to be the ones who can sustain
and facilitate the flow of information, and the more peripheral, more relevant to topic
users are more sensitive to topic relevance and serve to spread the information more
widely [7]. Many studies also show that the elements of retweeting, commenting and
hashtag use of Twitter can be used to convey complex public opinion [8] . The emo-
tional bond also applies to the sense of authenticity and a way of expression, as luxury
brands are also becoming a part of sustainability and contemporary consumer values,
enriching the symbolic fabric luxury fragrances present to consumers [9] . This im-
plies that symbolic and emotional attributes will shift in cultural and generational
change, and consequently, it is a significant marketing approach of luxury perfumery
[10]. A number of other models are related to SNA which have already been success-
fully applied to the problem of information dissemination in complex online social
hypernetworks, such as those proposed in [11].
There are a number of gaps in knowledge, however, that are not being addressed.
First, while some of the co -branding studies have been carried out on general product
categories (electronic products, food and beverages), the fragrance industry, which is
characterized by a symbolic complexity, has not been sufficiently studied as an object
of digital co -branding research [12]. Second, research integrating SNA and Twitter
sentiment analysis to assess brand collaboration is still quite limited, and the under-
standing of how sentiment flows among actors of the social network is limited. Sen-
timent analysis of Indonesian -language social media text is further complicated by
code-mixing and code -switching patterns common in informal online discourse [13].
Apollo: Journal of Tourism and Business
Vol 4, Issue 3, September 2026, Page 864-882
ISSN: 2985-5810 (Media Online)
DOI: https://doi.org/10.58905/apollo.v4i3.691
865

Third, past research tends to focus on a single platform (for instance, Instagram), and
is platform-centric in nature rather than considering the utility of public conversation
on X/Twitter as a way to complement and augment our understanding of the effec-
tiveness of marketing campaigns. The following methodological limitations provide
an incomplete picture of consumer perception landscape in the context of co-branding
fragrance in 2.0 social media age.
The novelty of this study lies in combining two analytical lenses that have typically
been applied in isolation: Natural Language Processing (NLP) -based sentiment and
affect analysis, and Social Network Analysis (SNA), integrated under the Digital
Public Sphere framework and Social Network Theory (Granovetter, 1973) that ground
this research throughout. Brand equity considerations inform the interpretive framing
of results, particularly in explaining why symbolic and sensory associations with fra-
grance brands may register as affectively positive even when explicit sentiment re-
mains neutral, but they are treated as a supporting lens rather than a third co -equal
theoretical pillar. The current study thus makes two contributions: theoretical (extend-
ing the joint application of Digital Public Sphere theory and Social Network Theory
to the fragrance co-branding domain) and practical (a data-informed framework brand
managers can use to monitor how collaboration discourse is expressed and circulates
online).
Based on the foregoing, this research aims to: (1) examine the distribution and
temporal trends of consumer sentiment toward perfume co -branding discourse on
X/Twitter; (2) identify key actors and interaction patterns within the Twitter social
network and their relationship to sentiment propagation; and (3) explore the extent to
which Twitter-based sentiment patterns and network structures can complement, ra-
ther than substitute for, the evaluation of perfume co-branding strategy.
2 Methods

Fig. 1. Research Methodology Framework. Source: Compiled by the author (2026).
This study uses exploratory social media analytics design and de -scriptive-
quantitative orientation along with seven computer modules of analysis. This method
was chosen because of its ability to capture the interactions between citizens in the
Apollo: Journal of Tourism and Business
Vol 4, Issue 3, September 2026, Page 864-882
ISSN: 2985-5810 (Media Online)
DOI: https://doi.org/10.58905/apollo.v4i3.691
866

public sphere around co- branding perfume, both structurally, through the social net-
work (X/Twitter), and semantically, through the attitudes of the consumers. However,
exploratory design is most appropriate for studies that seek to discover emergent pat-
terns in large-scale, unstructured social media data without categorical constraints and
because visualization plays a critical role in illustrating more complex human mobili-
ty patterns or sentiment trends that might arise from large social media datasets, it can
reveal salient structures and relationships that would otherwise remain less obvious
[14]. From a theoretical perspective, the current research is grounded in two main
theoretical frameworks: The Digital Public Sphere that posits that digital public dis-
course is considered as a rational space of collective perception construction [15]; and
the Social Network Theory that states that social network structures affect inter-action
patterns, information flows and inter-actor influence. By combining these two theoret-
ical lenses, the processes of both expression and dissemination through digital social
structures can be explored simultaneously, a duality that was not possible when look-
ing at either lens alone in previous single-method studies [16].
Data was collected using SocialX AI -Powered Data Min -ing platform
(https://www.socialx.id/) which is a social media analytics tool that can systematically
and quickly crawl and extract public data from X/Twitter with high accuracy and
reproducibility. A dedicated data mining platform guarantees the extraction of struc-
tured data, reducing the risk of manual extraction errors and improving the replicabil-
ity of the process [17], [18]. Data gathered for this period were from 1 -12 January
2026 with the following keyword combinations: "Parfum" OR "Fragrance" OR "Per-
fume Collab" OR "Body Mist" OR "EDP" OR "EDT" OR "Parfum Kolaborasi". Fol-
lowing the common practice in social media keyword- based sampling, the keywords
used were created using Boolean OR which is expected to increase the re -call of the
discourse in both Indonesian and English that are related to fragrance. No language
barriers were imposed on data collection (all languages) to allow for cross -cultural
data inclusivity and to capture the multilingual nature of the discourse on fragrance on
Twitter, as previously reported as a topic community of the global scale [19] . The
main corpus of the tweets was successfully retrieved from the X/Twitter platform and
totalled 300 tweets. This 12- day window was selected as an exploratory snapshot of
early-year fragrance discourse rather than as a basis for long -term generalization; the
implications of this choice for interpreting the findings are discussed in the Limita-
tions section.
All the data was first automatically pre-processed by the SocialX system, including
the removal of URLs with no semantic value, the removal of emojis and non -standard
characters that may affect text classification processes, the removal of duplicate en-
tries, especially if it is identical retweets which could lead to frequency bias, and to-
kenization and the lowercasing of the text; as part of text normalization, in order to
standardize the lexical forms [20]. These are the typical pre- processing steps that are
followed in text mining from social media, as discussed in various best practices in
text mining [21]. Before computational linguistic analysis, this pre -processed data set
was then checked for completeness, and all 300 data were found to be analytically
valid data to be used.
Apollo: Journal of Tourism and Business
Vol 4, Issue 3, September 2026, Page 864-882
ISSN: 2985-5810 (Media Online)
DOI: https://doi.org/10.58905/apollo.v4i3.691
867

The analysis of the data was performed using 7 integrated computational modules
of the SocialX platform. To get a first impression of the thematic landscape of the
tweets, the most dominant words in the tweet corpus was determined using the Term
Frequency (TF) via Wordcloud Analysis [22]. Second, Sentiment Analysis was per-
formed using SocialX's built-in sentiment classification module, which classifies each
tweet into positive, neutral, or negative polarity categories. This module was used as
provided by the platform; its underlying model architecture is not independently doc-
umented by SocialX and is therefore not specified here beyond the classification out-
put it returns. Third, Text Network Analysis was used to construct a word co -
occurrence graph (G = V, E), in which nodes represent individual words and edges
represent their co -occurrence within the same tweet, enabling the identification of
semantic clusters and conceptual linkages within the fragrance co -branding discourse
[23],[24]. Fourth, Emotion Analysis was applied to classify tweet content into five
discrete emotional categories there’s happy, sadness, anger, fear, and love to provid-
ing a more granular understanding of the affective dimensions of consumer responses
beyond binary sentiment polarity [25]. No independent human- coded validation sub-
sample was used to verify emotion classifications, particularly for non -Indonesian
content; this is addressed further in the Limitations section.
Fifth, Social Network Analysis (SNA) was conducted by modeling Twitter interac-
tion data as a directed graph G = (V, E), where nodes (V) represent individual users
and edges (E) represent directional interactions including mentions, replies, and re-
tweets. Key network metrics computed included degree centrality, betweenness cen-
trality, closeness centrality, network density, and community modularity, following
standard SNA methodological conventions as established by Wasserman and Faust
[26],[27]. Within this study, degree centrality was used to identify highly connected
actors who received a disproportionate share of mentions, replies, and retweets, while
betweenness centrality was used to identify bridge actors whose position between
community clusters allowed them to facilitate information flow across otherwise sep-
arate groups. Node size and cluster position in the SocialX visualization were used as
a visual proxy for these two centrality measures rather than as independently reported
numerical scores; this operational basis for identifying "influential" actors is treated as
indicative of relative position within the observed network, not as a validated or ex-
ternally calibrated measure of real- world influence [28] . Sixth, Trend Analysis was
used to visualize the temporal distribution of tweet volumes across the observation
period and to detect spike events defined as statistically significant deviations from
the seven-day moving average baseline that indicate moments of heightened public
attention toward specific co-branding discourse topics [29]. Seventh, Zero-Shot Clas-
sification based on Large Language Models (LLMs) was applied to assess the seman-
tic tendencies of tweets without requiring labeled training data, enabling flexible the-
matic categorization that adapts to the specific contextual dimensions of fragrance co-
branding discourse as they organically emerge from the data [30].
All analytical outputs were visualized through the SocialX interactive dashboard,
encompassing wordcloud representations, sentiment distributions, network graphs,
emotion distributions, key actor metrics, temporal trends, and semantic tendencies.
From a research ethics standpoint, all data constitute content published openly by
Apollo: Journal of Tourism and Business
Vol 4, Issue 3, September 2026, Page 864-882
ISSN: 2985-5810 (Media Online)
DOI: https://doi.org/10.58905/apollo.v4i3.691
868

users on X/Twitter, collected solely for academic purposes and consistent with the
platform's publicly available data usage policies, with no personally sensitive infor-
mation retained beyond public usernames.
3 Results and Discussion
3.1 Data Overview

Fig. 2. Tweet Activity Heatmap: Hour vs. Date Distribution (January 1-12, 2026).  Source:
X/Twitter data processed via SocialX (2026).
The total number of the tweets used in this study was 300 which were collected by
data mining process via the platform of SocialX. The data was collected from
X/Twitter platform, and the time span of observation was 1-12 January 2026, which is
related to the discourse of perfume and co -branding strategies. The data includes so-
cial media metadata, like the timestamp of each tweet; user metadata, including who
is talking and who is talking to whom; and social interactions, including retweets,
mentions and replies. For context on users' engagement, the number of likes, reposts,
and quotes are also included. Figure 2 shows a summary of the dataset
The share of tweet activity was highly uneven across time during the study. The
most of conversational activity was observed on the first two days of the observation
(on January 2, 2026 the number of tweets was about 95, and on January 1, 2026 was
about 90). Combined, these two dates made up over 61.7% of all the data, indicating
that the dataset is strongly event -sensitive rather than reflective of steady- state dis-
course. The observed patterns are therefore best read as a response to a specific tem-
poral trigger, the New Year transition, rather than as a stable baseline for everyday
perfume co-branding conversation. The high intensity in the first part of January sug-
gests a powerful digital push, either as a result of New Year promotions or the intro-
duction of special edition perfume offers, or perhaps co- branding promotions. After
this, the number of tweets significantly decreased from January 3 to 5 ( -240 tweets),
increased slightly on January 8 (+30 tweets) and then returned to low levels between
January 10 and 12 (6-11 tweets).
Apollo: Journal of Tourism and Business
Vol 4, Issue 3, September 2026, Page 864-882
ISSN: 2985-5810 (Media Online)
DOI: https://doi.org/10.58905/apollo.v4i3.691
869

A Tweet Activity Heatmap (Hour vs. Date) was used to see how the tweets were
distributed by hour and observation date. The heat map (Figure 2) shows that the most
active conversation was around 12:00- 18:00 WIB (Western Indonesian Time), with
darker-coloured cells in the midday- to-afternoon time slots. The peak of the activity
occurred at 18:00 WIB on January 1 with 11 tweets per hour, and at 11:00 WIB on
January 2 with 9 tweets per hour. This pattern reveals that Twitter's users who partici-
pate in per -fume and co -branding conversations are more active during times of
greater digital connectivity.
3.2 Wordcloud Analysis

Fig. 3. Wordcloud Analysis: Word Frequency Distribution in Fragrance Discourse
(January 1-12, 2026). Source: SocialX (2026).
To find the words that occurred most frequently in the whole set of 300 tweets,
Wordcloud Analysis was performed (see Figure 3). Analysis results indicate that the
most common words are "parfum", "edp" (Eau de Parfum), "perfume", "fra- grance",
"body" and "mist". Because those terms of the technical nature of perfumeries show
that the discussions on X/Twitter during the observation period were related to sub -
stance, to discussions of perfumes and not to social conversation in general.
The wordcloud also contained in- dividual brand terminology like "sauvage," "bur-
berry," "dior" and the name "ralph" (as in Ralph Lauren) and "elysees." These brand-
identifiable terms each appeared at frequencies of roughly 6 –8% of the corpus
("ralph"/"lauren" and "burberry" at 5.81 –8.14%, "dior" at 8.14%, "sauvage" at
6.98%), confirming that specific brand references are present in the discourse but at a
frequency too low for reliable brand- by-brand comparison without a larger or brand -
stratified sample. This study reports discourse patterns at the aggregate category level
and does not compare the relative performance of individual brand collaborations; the
frequencies above are reported descriptively to characterize the corpus, not as a basis
for ranking brand success. These results indicate that most public discussion was not
only of perfume in a categorical sense, but also in reference to the well -known brands
which are typically large players in the premium perfume co -branding market. The
Apollo: Journal of Tourism and Business
Vol 4, Issue 3, September 2026, Page 864-882
ISSN: 2985-5810 (Media Online)
DOI: https://doi.org/10.58905/apollo.v4i3.691
870

words “collection” and “new” are big, indicating consumer excitement towards new
releases or collections at the beginning of 2026.
Words such as "vanilla," "fruity," "sweet," "mint," "scent" and "wangi" also pro-
vide sensory experience dimension. This indicates that con -sumer conversation on
X/Twitter was shifting beyond transactional and information -based to expressing and
sensory. Consumers were vividly describing the aroma attributes of the product they
discussed. This discovery con-firms that there is an affective di -mension in consumer
digital discourse with per-fume products.
3.3 Text Network Analysis

Fig. 4. Text Network Analysis: Word Co-Occurrence Map in Fragrance Discourse.
 Source: SocialX (2026).
Developed using the 300 tweets, the graph is a Text Network Analysis (TNA)
which shows the co- occurrence relationships between words (Figure 4). The analysis
results show that the nodes with highest size that reflect the highest centrality in the
word network are "edt" (Eau de Toilette), "edp" (Eau de Parfum), "parfum", "per -
fume", "fragrance", "body", and "mist". These terms represent the main discourse
nodes, on which most of the conversations in the network are based, and indicate that
Apollo: Journal of Tourism and Business
Vol 4, Issue 3, September 2026, Page 864-882
ISSN: 2985-5810 (Media Online)
DOI: https://doi.org/10.58905/apollo.v4i3.691
871

the perfume products' type and format is the main topic that connects many sub -
discourses.
A graph visualization was used to extract four different clusters of meaning. The
green cluster is found in the bottom right of the graph and includes words like "body,"
“mist,” “wanginya,” “fruity,” “sweet,” “scent,” “lotion,” and other words that repre-
sent a sub-discourse on body mist, sensory experience. The left side of the cluster, by
contrast, has a red cluster of words such as “fragrance,” “parfum,” “oud,” “mas -
culine,” and “ralph,” related to men's fragrance and high quality men's “per-fume.”
The middle portion of the graph shows that the two technical terms “edt” and
“edp” have a very dense network of connections to nearly all other clusters in the
graph, indicating that these two technical terms are semantic bridges which link vari-
ous sub-topics of the conversations about perfume. The conversations throughout the
observation period are dominated by a discourse of new product launches at the start
of the year, as signaled by other words that were highly associated with each other,
such as "new", "january", "collection", "pour", and "eau". The results of the text net-
work analysis confirm the multi- dimensionality of the co- branding discourse in the
Twitter space, and the presence of those dimensions: the technical aspects of the per-
fume, the brand identity, the senso-rial aspects, and the temporal aspects of perfumes.
3.4 Sentiment Analysis

Fig. 5. Sentiment Analysis Distribution of the 300-Tweet Corpus. Source: SocialX (2026).
All 300 tweets included in the research corpus were analyzed using SocialX's built-
in sentiment classification module. The classification results indicated that neutral
tweets (264, 88%) were the most common, negative tweets (27, 9%), and positive
tweets (9, 3%) were the least common (Figure 5). The dominance of neutral sentiment
indicates that most tweets did not contain explicit evaluative expressions of approval
or rejection. In the context of perfume co -branding discourse, this suggests that users
primarily used X/Twitter to share information, mention products, describe fragrance
attributes, or refer to new collections rather than to express direct positive or negative
judgments. At the lexical sentiment level, consumer perception cannot therefore be
described as predominantly positive; the discourse is better characterized as largely
informational and neutral, with limited explicit positive sentiment.
Apollo: Journal of Tourism and Business
Vol 4, Issue 3, September 2026, Page 864-882
ISSN: 2985-5810 (Media Online)
DOI: https://doi.org/10.58905/apollo.v4i3.691
872

This overall sentiment, neutral (88%) needs to be put into context of the type of
conversation that is happening on Twitter, as this is often used for the dissemination
of information, product recommendations and the dissemination of education related
content about perfumes, including snippets of product reviews, price and new collec-
tions announcements. In spite of the small number of negative sentiment (9% or 27
tweets), it is analytically significant, as it could be the voice of consumers and indi-
cate some dissatisfaction about prices or criticism of specific co -branding strategies
that did not seem to resonate with consumers' perceptions. The other side to that is
that the proportion of positive sentiment is quite small (3%, 9 tweets) making that the
sentiment of "explicit and semantically confirmed expressions of appreciation or en-
thusiasm" was relatively uncommon in this discourse.
This sentiment distribution pat- tern is very important in the perfume co- branding
study. Overall, the results show high neutral sentiment levels, suggesting that the
brands engaging in collaborative strategies have not yet been able to direct consumer
conversations towards a more positive and emotion- arousing sentiment, which is a
paradox to the goal of co-branding as a strategy to enhance the brands' equity through
emotional connections (Keller, 2013). The sentiment analysis layer gives the interpre-
tive understanding that is used in the emotion analysis and zero- shot classification
layers explained in the following sections.
3.5 Emotion Analysis

Fig. 6. Emotion Analysis Distribution of the 300-Tweet Corpus. Source: SocialX (2026).
To gain a closer look into the affective aspects of perfume co -branding discourse,
Emotion Analysis was carried out. Within the five emotion categories, the classifica-
tion re-sults showed a very high number of Happy emotion tweets (276 tweets which
is 92% of the total number of tweets). Sadness ranked second with 14 tweets (4.67%),
followed by Anger with 7 tweets (2.33%), Fear with 2 tweets (0.67%), and Love with
1 tweet (0.33%). A radar diagram is used to see this distribution visually, and to con-
firm the absolute dominance of the happy emotion dimension in the conversational
network (Figure 6).
Apollo: Journal of Tourism and Business
Vol 4, Issue 3, September 2026, Page 864-882
ISSN: 2985-5810 (Media Online)
DOI: https://doi.org/10.58905/apollo.v4i3.691
873

The sentiment analysis results showed that 88% of the tweets were neutral in na-
ture, while at 92% the happy emotion dominated, this seems contradictory. The ap-
parent contradiction can be understood by the methodo- logical differences between
the two analyses: sentiment analysis is about the evaluative polarity of the entire con-
tent, whereas emotion analysis is concerned with the latent affective tone of content
that may be lexically neutral but emotionally positive. In other words, lots of tweets
that were neutral regarding the sentiment were discovered to have a tone of happiness
or enthusiasm which does not always map into explicit evaluative language.
The overall ratio of the negative emotions, anger (2.33%), fear (0.67%) and sad-
ness (4.67%), is very low and suggests that during the observation period, the affec-
tive ecosystem of the discourse on perfume co -branding on Twitter leaned toward
positive and stable affective expression. A distribution this concentrated in a single
emotion category is nonetheless higher than what is typically reported for open social
media discourse, and part of this concentration likely reflects classifier behavior on a
corpus that, as noted in the Limitations section, includes non- Indonesian tweets out-
side the platform's primary processing strengths; without a manually annotated valida-
tion subsample, the exact share attributable to genuine affective positivity versus
model bias toward a default majority class cannot be precisely disentangled. With that
caveat in mind, this discovery is still informative from the Digital Public Sphere point
of view (Habermas, 2022), as the digital space functions as an arena in which a col-
lective perception of perfume products and brand collaboration activities is formed,
and the observed skew toward happiness is a signal, rather than a confirmed measure,
of a more favorable reception climate for co-branding strategies.
4 Social Network Analysis

Fig. 7.  Fig. 8. Social Network Analysis: Mention Interaction Network in Fragrance Discourse.
Source: SocialX (2026).
A social network analysis (SNA) of 300 tweets over January 1 to 12, 2026 created
a directed graph of the interaction patterns of users of X/Twitter when they are talking
about co-branding in perfumes. The three biggest actors with the largest node sizes
are @LluisMolin89719, @MnicaRebullCome, and @maneltec located in the red clus-
Apollo: Journal of Tourism and Business
Vol 4, Issue 3, September 2026, Page 864-882
ISSN: 2985-5810 (Media Online)
DOI: https://doi.org/10.58905/apollo.v4i3.691
874

ter in the middle of the graph. Their high degree centrality scores indicate that these
accounts had a large node size so they are most likely to be reached by mentions,
replies, and retweets. The complex and multi -layered interactions between them sug-
gest deep and active cross -references between the three nodes and confirm the idea
that they are not just part of the stream of information but are active amplifiers of
perfume co-branding content.
The visualization also provides a few community clusters that differ in structure
and are different discursive sub -communities outside the dominant red cluster. The
blue cluster appears to have a more linear interaction pattern and is led by
@wayne010263 as a local hub, the green cluster includes @Trencasostres2 and
@ParisCat1960 and has more linear interaction patterns with the main cluster while
the yellow and purple clusters have few connections with the main clusters. Such
cluster diversity is evidence of high community modularity, which means that users
are closer to each other in their communities than between communities.
Betweenness centrality indicates that both @maneltec and @Trencasostres2 are
bridge actors between the red and green clusters, and play an important role in the
flow of information in and out of these communities. Other peripheral nodes, howev-
er, are not as effective as amplifying nodes, such as @SummerMelodyRec, @dv_7M,
and @MiranyMaker. The patterns that emerge are consistent with the Social Network
Theory (Granovetter, 1973) that proposes that network strength is not represented by
the number of members in the network, but by the strategic position of some actors in
the network that controls the in -formation flow inside the digital discourse system.
These centrality-based distinctions were derived from relative node size and cluster
position within the SocialX visualization rather than from independently reported
numerical thresholds or a validation procedure; the identification of "influential" or
"bridge" actors here should therefore be read as indicative of their position within this
specific observed network, not as a precisely calibrated or externally validated meas-
ure of influence.
4.1 Trend Analysis

Fig. 9. Trend Analysis: Daily Tweet Volume and 7-Day Moving Average
(January 1–12, 2026). Source: SocialX (2026).
Apollo: Journal of Tourism and Business
Vol 4, Issue 3, September 2026, Page 864-882
ISSN: 2985-5810 (Media Online)
DOI: https://doi.org/10.58905/apollo.v4i3.691
875

First, a temporal trend analysis was undertaken to identify temporal patterns in the
distribution of the number of tweets over the time period under observation (from the
1st to the 12th January 2026) in order to single out periods of conversation activity,
known as spike events. A line graph was used to visualize the number of tweets per
day and the 7 -day moving average, and it was determined that there were two major
spike events, one at January 1 2026 with ±90 tweets and the other at January 2 2026
with ±95 tweets. These two dates also coincided with the start of a new year, so that
the "New Year moment" was an important impetus for an increase of public discourse
on per-fume and co-branding on X/Twitter.
The graph indicates that the peak activity was on January 1-2, followed by a steady
downward trend after that day with the number of tweets per day rapidly dropping to
approximately 17-20 tweets per day on January 6. There was a slight uptick on Janu-
ary 8 (+/- 30 tweets) and then another drops off to very low levels on January 10 -12
(6-11 tweets). The 7 -day moving average is slightly flat, decreasing from about 54
tweets on day one of the trend to 11 on day 7 of the trend. The pattern seems to be
cyclic, meaning that public awareness towards the topic of co -branding perfume on
Twitter is strongly related to specific moments and not to constant moments.
The data from the hourly tweet activity heatmap (WIB) allows the trend analysis to
be given an intra-day temporal dimension. The heatmap indicates that the high activi-
ty of tweets was observed in the period of 12:00 – 18:00 WIB (western Indonesia
time) as the main peak hours for the observation period. The most active hour during
1st January was 18:00 - 19:00 WIB (with 11 tweets) while on 2nd January, the high-
est hourly activity was at 11:00 WIB (11 tweets). Based on the results, the most opti-
mal period of time for the co -branding campaign in perfumes using social media is
the midday to afternoon in the Western Indonesian Time zone, and the best time using
celebratory moments or seasonality and year end transition as a trigger for public
conversation is the midday to afternoon period in the Western Indonesian Time zone.
Because both spike events coincide with the New Year transition, the observed rise in
tweet volume is better read as a response to seasonal and calendar -driven attention
rather than as direct evidence of co-branding campaign effectiveness.
4.2 Zero-Shot Classification

Fig. 10. Zero-Shot Classification Distribution of the 300-Tweet Corpus
(January 1–12, 2026). Source: SocialX (2026).
Apollo: Journal of Tourism and Business
Vol 4, Issue 3, September 2026, Page 864-882
ISSN: 2985-5810 (Media Online)
DOI: https://doi.org/10.58905/apollo.v4i3.691
876

To enable flexible thematic categorization of specific aspects within perfume co -
branding discourse, a zero-shot classification based on a LLM (Large Language Mod-
el) was applied to classify 300 tweets without the need to have labelled training data.
The classification results showed an extremely skewed distribution with 82.33% (247
data points) classified as Positive, 14% (42 data points) classified as Negative and
3.67% (11 data points) as Neutral. The result of the distribution is very much skewed
from the sentiment analysis results, which showed a majority at 88% of neutral senti-
ment. Any differences between the zero- shot classification and the sentiment analysis
are not contradictory, but rather indicate a conceptually different measure. The plat-
form's sentiment classification module identifies sentiment polarity lexically and
evaluatively on the basis of explicit opinion expressions in the text, while LLM -based
zero-shot classification can identify more subtle semantic sentiment tendencies, such
as implicit tone, contextual framing, and layered meaning that may not surface as
explicit polarity.
In sum, these zero -shot classification results offer another analytical layer on the
tendencies of public discourse about perfume co- branding on Twitter. Rather than
resolving the discrepancy with the sentiment analysis finding, this layer indicates that
the corpus carries an implicit positive -leaning stance beneath its predominantly neu-
tral surface phrasing. The two findings are treated in this study as complementary
constructs rather than a single settled verdict on consumer sentiment: the platform's
sentiment classification module describes how consumers state things, while zero -
shot classification describes the direction the content leans toward when read for
stance. The 82.33% figure is therefore reported as a semantic- stance indicator, not as
a correction of or replacement for the neutral-dominant sentiment finding.
4.3 Sentiment Index Analysis

Fig. 11. Sentiment Index Analysis: Daily Sentiment Fluctuation Timeline
(January 1–12, 2026). Source: SocialX (2026).
Sentiment Index Analysis was also conducted to determine the overall direction of
the discourse of the co -branding perfume in aggregate during the observation period
(1 January-12 January 2026) on the X/Twitter platform. The overall Sentiment Index
value was in the Positive range and registered at +0.28 on the SocialX dashboard,
Apollo: Journal of Tourism and Business
Vol 4, Issue 3, September 2026, Page 864-882
ISSN: 2985-5810 (Media Online)
DOI: https://doi.org/10.58905/apollo.v4i3.691
877

based on the results shown. This index value was derived by adding together the sen-
timent weights of all 300 tweets observed over the time period and aggregating them
together, with a positive value indicating that the overall sentiment of public discourse
on Twitter about perfume co -branding was positive, or favourable, towards the per-
fume brands. The value of +0.28 is in the moderate positive region but not the maxi-
mum value of +1. This is a significant finding because it represents that there was no
dominant negative sentiment within the digital discourse ecosystem that was threaten-
ing the brand during this time.
The Sentiment Index Timeline visualization shows the fluctuations in value of the
index on a day -to-day basis, and also shows a wave -like pattern, which indicates the
change in quality of sentiment over time. The peak of positive sentiment was on the
9th of January 2026, when the index reached +0.55. The minimum index value that
ever moved into the negative region was on January 11, 2026 at the index value of -
0.10, the lowest in terms of sentiment quality. The day with the highest data volume
was recorded as January 2, 2026, with 94 tweets, but an index value of only about
+0.38, indicating that, while high volume of conversation does not necessarily equate
to high sentiment quality, it can. The pattern is suggesting a dissociation between the
number and the sentiment of the discourse, with the highest numbers of tweets not
necessarily coinciding with the highest positive sentiment.
Overall, the Sentiment Index Timeline curve appears to oscillate with three posi-
tive peaks (January 2 (+0.38), January 6 (+0.32), and January 9 (+0.55)) and three
troughs, or valleys, touching or near zero (January 3-5, and January 7-8). This oscilla-
tion suggests that public sentiment about co- branding discourse was never constant,
but was subject to certain external factors, such as viral content and product an-
nouncements, or celebratory moments, which periodically pushed sentiment quality
up and then down again. This discovery supports the view that the co -branding of
perfumes on social media is not a one -off, but must be supported by a series of care-
fully planned and timed content stimuli to help maintain positive sentiment momen-
tum over time within the perfume consumer community, on Twitter, in particular.
5 Conclusion
This study finds that public discourse on perfume products and co -branding activity
on X/Twitter during 1 –12 January 2026 was predominantly neutral in explicit lexical
sentiment (88%), alongside a positive -leaning semantic and affective tendency indi-
cated by zero -shot classification (82.33%), emotion analysis (92% happy), and the
Sentiment Index (+0.28). These findings should not be read as evidence that consum-
er perception was uniformly positive; rather, the discourse was largely informational
and descriptive on the surface, while carrying favorable associations related to fra-
grance, sensory experience, and new product collections. Because the observation
window coincided with the New Year transition and spans only twelve days, these
patterns are best interpreted as a snapshot of a specific and atypical calendar moment
rather than a stable baseline for perfume co-branding sentiment.
Apollo: Journal of Tourism and Business
Vol 4, Issue 3, September 2026, Page 864-882
ISSN: 2985-5810 (Media Online)
DOI: https://doi.org/10.58905/apollo.v4i3.691
878

Read together through the Digital Public Sphere and Social Network Theory
frameworks that ground this study, the seven analytical modules describe a single
underlying process rather than seven separate outputs: sentiment, emotion, zero- shot
classification, and the Sentiment Index jointly characterize what is being said and how
positively or neutrally it is framed, while wordcloud, text network, and social network
analysis show how that framing circulates and through which actors it is amplified or
bridged across community clusters, with trend analysis marking the temporal mo-
ments at which these two processes intensify together.
Social Network Analysis further shows that a small number of accounts occupied
central or bridging positions within the observed interaction network, based on rela-
tive node position rather than independently validated centrality scores (see Methods).
These actors likely contributed to the circulation of co- branding discourse within and
across community clusters; their influence should be understood as visibility within
this specific dataset, not as demonstrated influence on purchasing behavior or broader
market perception.
Overall, this study demonstrates that Twitter -based data can complement, rather
than substitute for, the evaluation of fragrance co -branding strategy. It is important to
note that this study did not measure sales performance, purchase intention, brand
awareness, or customer loyalty, and the discourse patterns identified here should not
be read as direct evidence of commercial effectiveness; they are better understood as
evidence of digital discourse resonance during a specific observation period.
6 Limitations and Recommendations for Further Research
While this study has yielded valuable insights, several limitations should be acknowl-
edged. First, only 300 tweets from a 12 -day period (1 –12 January 2026) were ana-
lyzed, and this period coincided with the New Year transition; the observed tweet
volume, sentiment pattern, and emotion distribution may reflect seasonal and celebra-
tory online behavior rather than steady- state discourse, so the findings cannot be gen-
eralized to long-term consumer sentiment toward perfume co-branding.
Second, this study focused on a single platform, X/Twitter, which has unique de-
mographic and communication characteristics not necessarily shared with Instagram,
TikTok, or YouTube. Relatedly, X/Twitter users who post publicly about perfume
represent a self-selected and demographically narrow subset of consumers who skew
toward more digitally active and vocal users; this subset does not necessarily corre-
spond to the broader population of actual perfume buyers. The findings should there-
fore be read as characteristics of public digital conversation, not as a proxy for con-
sumer perception or purchasing populations at large.
Third, because tweets were collected via keyword -based scraping rather than lan-
guage-filtered collection, the corpus is inherently multilingual, and this is not a mar-
ginal artefact: several French function words (e.g., "que," "pas," "pour," "les," "des")
each appear in 8 –17% of the corpus, alongside Portuguese and English content. The
sentiment and emotion classifications used in this study were generated by SocialX's
built-in analytical modules, and no manual validation subsample was used to verify
Apollo: Journal of Tourism and Business
Vol 4, Issue 3, September 2026, Page 864-882
ISSN: 2985-5810 (Media Online)
DOI: https://doi.org/10.58905/apollo.v4i3.691
879

classification accuracy on non-Indonesian tweets specifically. The reported sentiment
and emotion distributions should therefore be read as descriptive of the corpus as
processed by the platform, not as a validated measure of true public sentiment across
all languages present in the data.
Fourth, this study did not conduct a brand -level breakdown of co-branding conver-
sations; this is a genuine analytical gap rather than a data limitation, since brand -
identifiable terms (e.g., "ralph"/"lauren," "burberry," "dior," "sauvage") did surface in
the wordcloud and text -network analyses at frequencies of roughly 6 –8% of the cor-
pus. The aggregate -level results reported here cannot distinguish between more and
less successful individual brand collaborations.
Future work is suggested to be conducted for a longer observation period, with at
least 3-6 months beyond the festive seasons; to incorporate other platforms data like
Instagram or TikTok; or to use multilingual sentiment analysis model like XLM-
RoBERTa to enhance the accuracy of the cross -language content classification. The
precise identification of co- branding brands as units of analysis, coupled with the
inclusion of qualitative approaches through in- depth interviews, would further con-
tribute to the understanding of the motivations behind the identified sentiment pat-
terns, and at the same time, would give a more precise contribution to the develop-
ment of perfume co-branding marketing strategies in the digital era.
References
1. R. Alhindawi, Y. Abu Nahleh, and A. Kumar, “Navigating Sustainable Supply Chain
Management in the Perfume Industry: Challenges and Solutions,” Sustain., vol. 17, no. 2,
pp. 1–29, 2025, doi: 10.3390/su17020723.
2. J. Cai, K. L. Shi, and J. Wu, “Research on the Marketing Strategies of Chinese Fragrance
Brands,” Adv. Econ. Manag. Polit. Sci. , vol. 69, no. 1, pp. 105–112, 2024, doi:
10.54254/2754-1169/69/20231297.
3. Makhtibekov Abdulbasyr, “Strategies for Building Partnerships Between Brands:
Analysis of Factors Influencing the Success of Co-Branding Initiatives,” EPRA Int. J.
Econ. Bus. Manag. Stud., no. August, pp. 13–16, 2025, doi: 10.36713/epra23518.
4. C. Ekebas, “The Magic Formula: Scent and Brand" -The Influence of Olfactory Sensory
Co-Branding on Consumer Evaluations and Experiences,” Old Dom. Univ. , 2015, doi:
10.25777/3w6j-3806.
5. K. M. Kim, B. Nobi, S. Lee, and C. Milewicz, “International higher education brand
alliance: the role of brand fit and world-mindedness,” 2022. doi: 10.1108/APJML-06-
2020-0399.
6. P. Wang and Q. Huang, “Digital influencers, social power and consumer engagement
in social commerce,” Internet Res. , vol. 33, no. 1, pp. 178–207, 2023, doi:
10.1108/INTR-08-2020-0467.
7. X. Zhu, G. Yu, Y. Zhang, and N. Ma, “Dissemination characteristics and influencing
factors of topic circles in multi- layer public opinion dissemination,” Front. Public Heal. ,
vol. 13, 2025, doi: 10.3389/fpubh.2025.1566746.
8. G. Kusniawati, “Analysis Of The Use Of Hashtags As A Social Movement In
Apollo: Journal of Tourism and Business
Vol 4, Issue 3, September 2026, Page 864-882
ISSN: 2985-5810 (Media Online)
DOI: https://doi.org/10.58905/apollo.v4i3.691
880

Determining Public Opinion On Social Media ‘Twitter’ (Study On Hastag
#Sahkanruupks),” Tabayyun, vol. 4, no. 2, pp. 357–371, 2023, doi:
10.19109/tabayyun.v4i2.19248.
9. M. Díaz-Bustamante, S. Carcelén, and M. Puelles, “Image of Luxury Brands: A Question
of Style and Personality,” SAGE Open , vol. 6, no. 2, 2016, doi:
10.1177/2158244016644946.
10. C. Krishnan, N. Agarwal, and S. Gupta, “Factors Influencing Consumer Purchase
Intention of Luxury Branded Perfumes,” Mark. Manag. Innov., vol. 13, no. 3, pp. 190–
199, 2022, doi: 10.21272/mmi.2022.3-17.
11. Y. C. Gong, M. Wang, W. Liang, F. Hu, and Z. K. Zhang, “UHIR: An effective
information dissemination model of online social hypernetworks based on user and
information attributes,” Inf. Sci. (Ny). , vol. 644, no. October 2022, p. 119284, 2023, doi:
10.1016/j.ins.2023.119284.
12. R. Basiya, M. Marlien, K. Kasmari, B. Sutejo, and B. Sudiyatno, “The influence of co -
branding strategies on repurchase intention: Empirical evidence on cosmetics and herbal
medicine collaboration product in Indonesia,” Innov. Mark. , vol. 20, no. 2, pp. 89–99,
2024, doi: 10.21511/im.20(2).2024.08.
13. C. Tho, Y. Heryadi, L. Lukas, and A. Wibowo, “Code -mixed sentiment analysis of
Indonesian language and Javanese language using Lexicon based approach,” J. Phys.
Conf. Ser., vol. 1869, no. 1, 2021, doi: 10.1088/1742-6596/1869/1/012084.
14. Z. Ebrahimpour, W. Wan, J. L. V. García, O. Cervantes, and L. Hou, “Analyzing social -
geographic human mobility patterns using large -scale social media data,” ISPRS Int. J.
Geo-Information, vol. 9, no. 2, 2020, doi: 10.3390/ijgi9020125.
15. M. Eisenegger and M. S. Schäfer, “Editorial: Reconceptualizing public sphere(s) in the
digital age? On the role and future of public sphere theory,” Commun. Theory , vol. 33,
no. 2–3, pp. 61–69, 2023, doi: 10.1093/ct/qtad011.
16. K. Lewis, “Digital networks: Elements of a theoretical framework,” Soc. Networks , vol.
77, no. December 2021, pp. 31–42, 2024, doi: 10.1016/j.socnet.2021.12.002.
17. F. A. Ghanem, M. C. Padma, H. M. Abdulwahab, and R. Alkhatib, “Novel Genetic
Optimization Techniques for Accurate Social Media Data Summarization and
Classification Using Deep Learning Models,” Technologies , vol. 12, no. 10, 2024, doi:
10.3390/technologies12100199.
18. N. S. Jonnala et al., “Leveraging hybrid model for accurate sentiment analysis of Twitter
data,” Sci. Rep., vol. 15, no. 1, pp. 1–10, 2025, doi: 10.1038/s41598-025-09794-2.
19. S. Chereni, R. V. Sliuzas, and J. Flacke, “An extended briefing and debriefing technique
to enhance data quality in cross-national/language mixed- method research,” Int. J. Soc.
Res. Methodol., vol. 23, no. 6, pp. 661–675, 2020, doi: 10.1080/13645579.2020.1731992.
20. A. R. Lubis and M. K. M. Nasution, “Twitter Data Analysis and Text Normalization in
Collecting Standard Word,” J. Appl. Eng. Technol. Sci. , vol. 4, no. 2, pp. 855–863, 2023,
doi: 10.37385/jaets.v4i2.1991.
21. M. A. Palomino and F. Aider, “Evaluating the Effectiveness of Text Pre -Processing in
Sentiment Analysis,” Appl. Sci., vol. 12, no. 17, 2022, doi: 10.3390/app12178765.
22. G. Yadav, M. Joshi, and R. Sasikala, “Twitter data analysis: Temporal and term
frequency analysis with real-time event,” IOP Conf. Ser. Mater. Sci. Eng., vol. 263, no. 4,
2017, doi: 10.1088/1757-899X/263/4/042081.
Apollo: Journal of Tourism and Business
Vol 4, Issue 3, September 2026, Page 864-882
ISSN: 2985-5810 (Media Online)
DOI: https://doi.org/10.58905/apollo.v4i3.691
881

23. M. I. Fudolig, T. Alshaabi, M. V. Arnold, C. M. Danforth, and P. S. Dodds, “Sentiment
and structure in word co-occurrence networks on Twitter,” Appl. Netw. Sci., vol. 7, no. 1,
2022, doi: 10.1007/s41109-022-00446-2.
24. G. Casalino, C. Castiello, N. Del Buono, and C. Mencar, “A framework for intelligent
Twitter data analysis with non -negative matrix factorization,” Int. J. Web Inf. Syst. , vol.
14, no. 3, pp. 334–356, 2018, doi: 10.1108/IJWIS-11-2017-0081.
25. S. Chawla and M. Mehrotra, “Impact of emotions in social media content diffusion,”
Inform., vol. 45, no. 6, pp. 11–28, 2021, doi: 10.31449/INF.V45I6.3575.
26. D. J. Lemay, R. B. Basnet, T. Doleck, and P. Bazelais, “Social network analysis of twitter
use during the AERA 2017 annual conference,” Educ. Inf. Technol. , vol. 24, no. 1, pp.
459–470, 2019, doi: 10.1007/s10639-018-9787-2.
27. C. H. Ellis, J. B. Moore, P. Ho, W. Ahmed, and C. E. L. Evans, “Social network and
linguistic analysis of the #nutrition discourse on the social network platform X, formerly
known as Twitter,” Soc. Netw. Anal. Min. , vol. 14, no. 1, pp. 1–11, 2024, doi:
10.1007/s13278-024-01404-9.
28. C. Munro, “Brand Influence Online : Cross -Platform Social Network Analysis on the
Enablement of Effective Brand Communities,” p. 79, 2015, [Online]. Available:
http://digital.library.ryerson.ca/islandora/object/RULA%3A4440/
29. L. S. Drescher, C. Grebitus, and J. Roosen, “Exploring Food Consumption Trends on
Twitter with Social Media Analytics: The Example of #Veganuary,” EuroChoices , vol.
22, no. 2, pp. 45–52, 2023, doi: 10.1111/1746-692X.12403.
30. W. Tafesse and A. Wien, “A framework for categorizing social media posts,” Cogent
Bus. Manag., vol. 4, no. 1, 2017, doi: 10.1080/23311975.2017.1284390.

Apollo: Journal of Tourism and Business
Vol 4, Issue 3, September 2026, Page 864-882
ISSN: 2985-5810 (Media Online)
DOI: https://doi.org/10.58905/apollo.v4i3.691
882
