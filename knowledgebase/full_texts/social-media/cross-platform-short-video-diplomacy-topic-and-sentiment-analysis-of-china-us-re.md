---
title: 'Cross-Platform Short-Video Diplomacy: Topic and Sentiment Analysis of China-US Relations on Douyin
  and TikTok'
url: https://arxiv.org/abs/2510.22415
category: social-media
subcategory: empirical
date: 2025-10
venue: ''
authors:
- Zheng Wei
- Mingchen Li
- Junxiang Liao
- Zeyu Yang
- Xiaoyu Yang
source: arxiv
pdf_url: https://arxiv.org/pdf/2510.22415
pages: 12
chars: 60761
fetched_at: '2026-11-08T13:10:50+00:00'
kb_version: 1
---

# Cross-Platform Short-Video Diplomacy: Topic and Sentiment Analysis of China-US Relations on Douyin and TikTok

Cross-Platform Short-Video Diplomacy: Topic and Sentiment Analysis of
China–US Relations on Douyin and TikTok
Zheng Wei1, Mingchen Li 2, Junxiang Liao 3, Zeyu Yang2, Xiaoyu Yang2, Yixuan Xie2, Pan Hui 2,
Huamin Qu1
1The Hong Kong University of Science and Technology
2The Hong Kong University of Science and Technology (Guangzhou)
3The Hong Kong Polytechnic University
zwei302@connect.ust.hk, mli736@connect.hkust-gz.edu.cn, junxiang.liao@connect.polyu.hk,
zyang979@connect.hkust-gz.edu.cn, xyang058@connect.hkust-gz.edu.cn, yixuanxie@hkust-gz.edu.cn,
panhui@hkust-gz.edu.cn, huamin@cse.ust.hk
Abstract
We examine discussions surrounding China-U.S. relations on
the Chinese and American social media platformsDouyin
andTikTok. Both platforms, owned byByteDance, operate
under different regulatory and cultural environments, provid-
ing a unique perspective for analyzing China-U.S. public dis-
course. This study analyzed 4,040 videos and 338,209 user
comments to assess the public discussions and sentiments on
social media regarding China-U.S. relations. Through topic
clustering and sentiment analysis, we identified key themes,
including economic strength, technological and industrial in-
terdependence, cultural cognition and value pursuits, and re-
sponses to global challenges. There are significant emotional
differences between China and the US on various themes.
Since April 2022, the Chinese government has implemented a
new regulation requiring all social media accounts to disclose
their provincial-level geolocation information. Utilizing this
publicly available data, along with factors such as GDP per
capita, minority index, and internet penetration rate, we in-
vestigate the changes in sentiment towards the U.S. in main-
land China. This study links socioeconomic indicators with
online discussions, deeply analyzing how regional and eco-
nomic factors influence Chinese comments on their views of
the US, providing important insights for China-U.S. relation-
ship research and policy making.
Introduction
The dynamic relationship between China and the United
States has been a focal point in global politics, economics,
and international relations. As these two superpowers navi-
gate the complexities of cooperation and competition, social
media platforms such as the AmericanTikTokand the Chi-
neseDouyinhave introduced new dimensions to their inter-
actions. Although both platforms are owned byByteDance,
they operate under different regulatory frameworks and cul-
tural contexts, which not only shape the user experience but
also serve as channels for public discourse that reflect and in-
fluence mutual perceptions between the two countries. Mil-
lions of users engage in discussions and share content on
these platforms, offering real-time insights into societal atti-
tudes. These interactions provide a rich data source for ana-
Copyright © 2024, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
lyzing how digital dialogues construct and mediate national
identities, stereotypes, and geopolitical narratives. By exam-
ining user comments on short videos related to each other’s
content onTikTokandDouyin, this study aims to uncover the
core themes and emotional trends in public discourse sur-
rounding China-U.S. relations.
Furthermore, we conduct an in-depth analysis of the emo-
tional differences towards the United States across vari-
ous regions in China. By utilizingDouyin’s IP geolocation
mandatory disclosure policy implemented in April 2022, we
associate user comments with their geographic locations to
analyze emotional differences among different provinces.
This not only enhances the comprehensiveness of public
sentiment analysis but also overcomes the sample selec-
tion bias caused by users’ voluntary location disclosure.
By integrating geographical information, we further investi-
gate how regional socioeconomic factors (such as per capita
GDP, minority index, and internet penetration rate) influence
public discussions on these platforms. Additionally, by us-
ing large language models (LLM) for sentiment analysis,
we quantify the emotional tones in the comments, catego-
rizing them into positive (including 1.rational support 2. ex-
treme enthusiasm) and negative (including 1.hate 2.criticism
or complaints), as well as neutral sentiments. This approach
provides a more nuanced understanding of the emotional
trends present in the discussions.
We analyze comments posted byDouyinandTikTokusers
from China and the United States on short videos involv-
ing China-U.S. relations, focusing on: (1) the topics dis-
cussed by users from both countries regarding each other’s
views in the comments; (2) the level of negative sentiment
in the United States towards China; (3) the level of negative
sentiment in comments from different provinces in China
towards the United States; (4) the socioeconomic factors
that can explain the emotional differences in discussions
across different provinces in China. We analyzed data from
338,209 comments on 4,040 short videos displaying content
related to China and the United States to answer the follow-
ing questions:
•RQ1: What are the dominant themes that emerge in
user comments on U.S.TikT okand ChineseDouyin
when discussing mutual perceptions between the two
arXiv:2510.22415v1  [cs.SI]  25 Oct 2025

countries?
•RQ2: Do sentiment patterns vary across different
themes related to perceptions of China and the U.S.,
and if so, what are the key differences?
•RQ3: Are there regional variations in the topics and
sentiment attitudes expressed in comments onDouyin
in mainland China when discussing the U.S., and if so,
what are the characteristics of these variations?
•RQ4: What factors contribute to the differences in
negative sentiment levels towards the U.S. across var-
ious topics and provinces in China, and can these fac-
tors be used to explain the observed variations?
We found that sentiments in China towards the U.S. are
relatively complex, with 11.19% of the comments being pos-
itive and 45.55% negative. In contrast, 42.09% of comments
from the U.S. towards China are positive, while 11.36% are
negative. Through topic clustering, we identified key themes
such as economic strength, technological competition and
cooperation, happy life, and addressing global challenges.
Discussions in China comments tend to emphasize power
dynamics and the complexity of interdependence, while
U.S. comments discussions focus more on shaping values
and perceptions. Based on provincial regression data, we
also found that the level of negative sentiment toward China-
U.S. relations varies across different regions in China. By
examining socioeconomic development indicators in several
provinces, including local GDP, minority population indices,
and internet penetration rates, we can explain some of these
regional differences. This study deepens our understanding
of discussions on China-U.S. relations on social media, re-
vealing how these discussions are influenced by regional so-
cioeconomic development and evolve accordingly.
BACKGROUND AND RELA TED WORK
Social media platforms, such as TikTok and Douyin, have
significantly influenced the dynamic development of cross-
cultural perceptions and international relations, providing
unique digital spaces to observe the socioeconomic, polit-
ical, and cultural environments of their respective user bases
(Chu and Choi 2011; Baum and Potter 2019; Bennett 2012;
Wei, Xu, and Hui 2024). China-U.S. relations are a critical
topic in contemporary international affairs, with interactions
between the two nations profoundly affecting the global po-
litical and economic landscape (Chengqiu 2020). A substan-
tial body of research has highlighted the significant role of
public attitudes in shaping bilateral relations, often serving
as references for national foreign policy formulation (Qin
and Ge 2023; Hudson 2005; Holsti 2009). In this context,
numerous studies have focused on the perceptions and atti-
tudes between China and the United States, typically using
opinion polls and social surveys as their primary methodolo-
gies (Swedlow and Wyckoff 2009; King et al. 2004). Specif-
ically, research on Chinese public attitudes toward the U.S.
reveals a spectrum of complex sentiments often influenced
by changes in international relations (Deng 2001). The emo-
tional dynamics between China and the U.S. are shaped by
geopolitical factors and domestic influences in both coun-
tries (Deng 2001). In the United States, anxiety surrounding
China’s rise is a significant concern (Ikenberry 2008), stem-
ming partly from a perceived “mystique” surrounding China
and partly from worries about America’s own developmen-
tal trajectory (Friedberg 2005).
This section reviews research on sentiment trends be-
tween China and the United States on social media. We then
briefly introduce policies related to IP geolocation disclosure
on Chinese social media platforms (Zhou, Wei, and Liao
2024; Wei et al. 2024). Finally, we present the theoretical
model underpinning this study.
Mutual Perceptions on TikTok and Douyin
Social media has emerged as a crucial space for shap-
ing and articulating inter-nation perceptions (Ausat 2023;
Duncombe 2019).TikTokandDouyin, both owned by
ByteDance, share a unified algorithmic architecture and sim-
ilar operational models, providing a consistent foundation
for comparative analysis. This commonality in their tech-
nological and usage frameworks sets the stage for examin-
ing how these platforms diverge when situated within dis-
tinct cultural and regulatory environments, resulting in var-
ied content ecosystems. Such a setup offers a valuable op-
portunity to investigate the impact of localized factors on
platform usage and content generation (Kaye, Chen, and
Zeng 2021; Liu and Yang 2022). Studies have shown that
TikTokusers in the United States engage with a diverse
range of content that contributes to a global youth culture
characterized by viral trends, creative challenges, and meme
sharing (Boffone 2022b,a). In contrast,Douyin(the Chi-
nese version ofTikTok) offers content that is more localized
and closely aligned with Chinese cultural norms, social is-
sues, and adheres to government regulations (Wagner 2023;
Chen, Valdovinos Kaye, and Zeng 2021).Douyinempha-
sizes themes that reinforce Chinese cultural identity and so-
cietal values, resulting in a user experience deeply rooted in
local culture (Chen et al. 2023). Previous studies have ex-
plored how these platforms reflect and shape mutual percep-
tions. Some scholars have analyzed user-generated content
during significant geopolitical events, finding that users of-
ten engage in discourses reinforcing national identities and
stereotypes (Zhang 2019). The algorithmic curation on these
platforms can create echo chambers, reinforcing existing
beliefs and potentially exacerbating misunderstandings be-
tween cultures (Raza and Aslam 2024; Wei, Xu, and Hui
2024; Brady et al. 2023). Additionally, the lack of direct in-
teraction betweenTikTokandDouyinusers due to platform
segregation limits opportunities for cross-cultural engage-
ment.
Sentiment Differences Across Themes
Sentiment analysis on social media has revealed that public
attitudes toward foreign nations vary across different themes
and contexts (Thelwall 2018; Wei et al.). In the context
of China-U.S. relations, sentiments expressed fluctuate de-
pending on topics such as politics, economics, culture, or
technology (Zhang 2020; Guan et al. 2020; Chen and Wang
2022). During the COVID-19 pandemic, conspiracy theo-
ries and misinformation blaming China proliferated on so-
cial media, includingTikTok, fueling xenophobia and anti-

Asian incidents (Shahsavari et al. 2020; Ittefaq et al. 2022;
Roberto, Johnson, and Rauhaus 2020). Moreover, concerns
over data security and privacy tied to Chinese apps have
deepened skepticism and distrust among American users
(Kokas 2018; Liu 2021). Debates surrounding the poten-
tial banning ofTikTokin the U.S. highlighted broader is-
sues of digital security and international rivalry (Ke 2023;
Gray 2021). These examples underscore the critical role that
thematic context plays in shaping public sentiment toward
foreign countries on social media platforms, demonstrating
how different topics can either bridge cultural gaps or exac-
erbate existing tensions.
Regional Sentiment Distribution in China
China’s regional diversity raises questions about whether
users from different provinces prioritize distinct topics or ex-
press varying sentiments on China-U.S. relations. Prior re-
search has shown regional patterns in areas such as public
health, sports, and urban planning based on users’ disclosed
locations (Baucom et al. 2013; Milusheva et al. 2021; Cao
et al. 2018; Kuchler, Russel, and Stroebel 2022). However,
voluntary location sharing can introduce selection bias (Li
et al. 2016; Bao et al. 2015; Backstrom, Sun, and Marlow
2010). To address this, the Chinese government mandated
that social media platforms automatically tag comments
with users’ IP-based provincial locations (or country if in-
ternational), minimizing self-selection concerns (Wei et al.
2024). This policy supports a more comprehensive analysis
of regional sentiment variations in discussions about China-
U.S. relations.
Theoretical Models
We propose a four-dimensional theoretical framework that
integrates power transition theory, complex interdependence
theory, constructivism, and global governance theory to
guide our understanding of the dimensions of topics dis-
cussed between China and the U.S. on social media.
Power Transition TheoryPower transition theory posits
that the international system is characterized by a hierarchy
of states, where global order is contingent upon the distribu-
tion of power among major players (Ross and Feng 2008).
In the context of China-U.S. relations, this framework elu-
cidates the competitive dynamics inherent in their interac-
tions on social media. As China emerges as a formidable
global power, the theoretical lens reveals a struggle for dom-
inance that transcends mere economic competition, encom-
passing value battles over narrative control and legitimacy
(Pan 2012; Ambrosetti 2012). The interactions on social me-
dia can be viewed as a battleground for competing visions
of international order, where both nations seek to assert their
influence and reshape public perceptions, ultimately impact-
ing diplomatic engagement and conflict resolution strategies
(Collins, DeWitt, and LeFebvre 2019).
Complex Interdependence TheoryComplex interde-
pendence theory offers a sophisticated lens through which
to comprehend the multifaceted relationships characteriz-
ing China-U.S. interactions in an increasingly globalized
context (Zhao and Liu 2010). It departs from traditional
state-centric paradigms by emphasizing the importance of
transnational networks, non-state actors, and multiple inter-
action channels—including economic interdependence, cul-
tural exchanges, and technological partnerships (Chengqiu
2020). On social media platforms, this interdependence is
evident through shared narratives and dialogues that high-
light mutual vulnerabilities and interconnected interests
(Schindler et al. 2024). Examining these digital interactions
facilitates a critical exploration of how collective identities
are constructed and negotiated in the online public sphere,
uncovering both opportunities for cooperation and the po-
tential for misperceptions that may exacerbate tensions be-
tween the two nations.
ConstructivismConstructivism posits that state identi-
ties and interests are socially constructed through interac-
tions and shared understandings, rather than being inher-
ently fixed (Badea 2021; Friedberg 2005). This theoretical
perspective emphasizes the significance of social cognition,
cultural values, and collective meanings in shaping inter-
national relations. In the context of social media, construc-
tivism is highly relevant as platforms likeTikTokandDouyin
facilitate the exchange of narratives and cultural expressions
that contribute to the mutual construction of national iden-
tities (Jaworsky and Qiaoan 2021). These discursive prac-
tices influence how nations perceive each other, impacting
public opinion and potentially informing foreign policy de-
cisions (Baum and Potter 2008). By examining the ways in
which users engage with content and with each other online,
we can better understand how cultural perceptions and value
systems shape bilateral attitudes and relationships.
Global Governance TheoryOur final theoretical lens,
global governance theory, explores the mechanisms by
which state and non-state actors collaborate to manage
transnational challenges that transcend national boundaries
(Higgott, Underhill, and Bieler 2000; Green 2018). This per-
spective is particularly salient in the context of social me-
dia, where China and the U.S. interact with and respond
to complex global issues such as climate change, public
health crises, cybersecurity threats, and economic interde-
pendence. By analyzing discussions on platforms likeTikTok
andDouyin, we can discern how each nation articulates its
priorities, frames global challenges, and proposes solutions
within the digital public sphere.
DA TA
Our data was sourced fromDouyinandTikTok.Douyinis
China’s leading short video platform, boasting over 700 mil-
lion daily active users (prudent 2023).TikTok, its global
counterpart, has been downloaded more than 6.7 billion
times (Zheng, Mulligan, and Scott 2021). Short videos on
platforms likeDouyinandTikTokare often tagged with mul-
tiple hashtags, many of which are automatically suggested
by the platform to reflect relevant topics. Our data collec-
tion process was driven by keyword searches, starting with
seed keywords related to topics such as “China” and “United
States,” along with their associated terms, which the plat-
form recommends when performing the search. These seed
keywords were initially selected based on expert knowledge
of China-U.S. studies and were supplemented with platform-
suggested terms that reflect trending topics related to the

seed keywords. For example, when “China” was used as
the seed keyword, the platform might recommend hashtags
such as “Chinese Society,” “Chinese Culture,” or “Life in
China.” Therefore, our keyword search method was primar-
ily guided by the platform’s algorithmic suggestions. This
approach is consistent with previous research that gathered
topic-related short videos on Douyin using a similar method
(Wei et al. 2024). We also tested alternative methods, such as
using cosine similarity to identify words related to the seed
keywords, but found the platform’s algorithmic recommen-
dations to be more effective. We began our data crawling
with an initial set of ten seed keywords and expanded the list
when the number of comments collected was insufficient.
The final set of keywords included 40 terms, which provided
a diverse range of videos and comments. These keywords
include terms such as “Chinese Society,” “Chinese Culture,”
and “American Life,” as specified in Appendix Table 6.
All video content featuring at least one of these keywords
was collected. Between August 31 and September 19, 2024,
we developed a customized web crawler utilizing the open-
source toolMediaCrawlerand conducted data collection for
20 hours each day 1. When collecting data from China, to
minimize content discrepancies caused by the platform’s
recommendation algorithms based on IP geolocation, we
employed IP proxy services fromchinapptp. This allowed us
to simulate IP addresses from multiple regions within China.
When handling comments from the United States, given that
TikTok’s user base is global, we restricted our data collection
to English and Chinese comments posted under videos con-
taining the relevant search terms. Furthermore, we filtered
these comments to include only those from accounts regis-
tered in the United States, thereby ensuring that the com-
menters are predominantly U.S. users.
Our keyword searches yielded 1,546 short videos and
539,443 associated comments from China, alongside 3,571
short videos and 298,920 comments from the U.S., cov-
ering the period from May 2019 to September 2024. The
preprocessing of comment data involved several systematic
steps. Initially, four researchers assessed the videos to ver-
ify their relevance to China-U.S. relations issues. We then
removed duplicate comments and those consisting solely of
punctuation, emojis, or @usernames, resulting in an initial
refined dataset of 338,209 comments. This included 1,158
videos and 211,090 comments from China, and 2,882 videos
and 127,117 comments from the U.S. These comments were
subsequently analyzed thematically. Each comment was cat-
egorized into multiple themes based on its content (refer
to the “Topic Analysis” section below). In addition, when
analyzing regional differences within mainland China, we
excluded comments without IP addresses (i.e., comments
posted before the mandatory IP address disclosure policy)
and comments with IP addresses not from mainland China.
Ultimately, 330,670 comments from 4,024 videos were in-
cluded in the analysis (China: 1,142 videos, 203,553 com-
ments; U.S.: 2,882 videos, 127,117 comments).
1https://github.com/NanmiCoder/MediaCrawler
METHOD
Topic Analysis
We identified the key themes arising from online discussions
through a mixed analytical strategy that combines both in-
ductive and deductive methods, following the principles of
Grounded Theory (Corbin and Strauss 2014). This approach
categorizes comment texts into clusters of words, subse-
quently synthesizing them into broader themes and theoret-
ical dimensions, as illustrated in the thematic analyses con-
ducted by Boyd-Graber et al. and Baumer et al. (Baumer
et al. 2017; Boyd-Graber et al. 2017). Next, we applied the
BERTopicalgorithm (Grootendorst 2022) to organize a sub-
stantial dataset of unstructured user comments. The algo-
rithm clustered 539,443 Chinese comments into 301 the-
matic categories and 298,920 U.S. comments into 300 the-
matic categories.
Subsequently, we narrowed the investigation to specific
clusters directly related to China-U.S. relations. To accom-
plish this, three researchers manually verified the common
keywords within each cluster. We removed 52 clusters from
the Chinese comments that were unrelated to the themes,
leaving 249 clusters corresponding to 1,158 short videos and
211,090 comments. Similarly, we deleted 69 clusters from
the U.S. comments that were unrelated to the themes, result-
ing in 231 clusters corresponding to 2,882 short videos and
127,117 comments. This constituted the final analysis sam-
ple.
Three researchers manually reviewed each cluster to en-
sure consistency of keywords and accuracy of the identi-
fied themes. We conducted qualitative analyses on the 249
Chinese clusters and 231 U.S. clusters. Using an iterative,
consensus-based coding procedure, three researchers inde-
pendently inspected the keyword lists for every cluster,
manually merged clusters with synonymous or conceptu-
ally overlapping terms, and—after two rounds of discussion
to reconcile differences—consolidated them into 21 higher-
order themes; for instance, clusters 37 and 102, which shared
>80 % tariff-related trade keywords, were combined as
“Sino-US Trade & Economic Frictions. Finally, we mapped
the themes onto a four-dimensional theoretical framework
encompassing power transition theory, complex interdepen-
dence theory, constructivism, and global governance theory.
Independent theme grouping was followed by collaborative
discussions to resolve discrepancies and achieve consensus.
Table 1 presents the final classification results.
Table 1: The classification of 21 thematic clusters into four
theoretical dimensions
Power
Transition
Theory
Complex
Interdependence
Theory
Constructivism
Global
Governance
Theory
1.Economic Strength
2.Great Power Rivalry
3.Power Dismantlement
4.Values Dialogue
5.War and Conflict
6.Political Party Rivalry
7.Racial Conflict
1.Technological
Competition
and Cooperation
2.Financial
Interdependence
3.Industrial Synergy
4.Talent Exchange
and Interaction
1.Happy Life
2.Culture and
Education
3.Immigration
4.Public Safety
5.Gender/Racial
Equality
1.Invasive species
2.Food security
3.Public health
4.Environmental
protection
5.Multipolarity

Sentiment Analysis
To ensure the accuracy and consistency of sentiment anno-
tation, we developed comprehensive annotation guidelines
and published them on GitHub 2 to ensure all participants
followed standardized procedures. We randomly selected
1,000 comments each from China and the United States
for manual annotation, establishing a benchmark and eval-
uating the performance of theQwen-PlusLLM 3 andGPT-
4o miniLLM 4. After experiments with prompt optimiza-
tion and fine-tuning using manually annotated sentiment
analysis of 100 comments from both China and the U.S.,
the LLM’s sentiment analysis ability was significantly im-
proved. We selected the best-performing configuration from
all of our experiments and tested it on a total of 2,000 re-
views. the results showed that this configuration achieved
near-human level accuracy, and the accuracy of sentiment
analysis reached 88.4% for China and 85.9% for the U.S.,
as shown in Table 2.
Table 2: Sentiment distribution for China and the U.S. was
evaluated with 1,000 samples each, comparing manual la-
bels with GPT-4o mini and Qwen-Plus. Where FT stands
for fine-tuning, PO stands for prompt optimization. When
calling the API of the LLM, the parameters are set as top p
= 0.1, presence penalty = -2.0, with other parameters using
default values. During fine-tuning of the LLM, the settings
are epochs = 3, batch size = 1, LR multiplier = 1.8, and seed
= 1925383673. The data used for prompt optimization and
fine-tuning are not included in the test data.
Method Country Negative Neutral Positive Censored Accuracy
Manual
labels
China 40.1 48.7 11.2 / /
U.S. 10.3 52.4 37.3 / /
Qwen-Plus China 34.7 53.2 10.6 1.5 70.3% U.S. 15.9 62.6 18.9 2.6 63.9%
GPT-4o mini China 45.5 39.3 10.3 0 79.0% U.S. 17.7 47.3 35.0 0 72.6%
Qwen-Plus
(PO)
China 50.1 38.9 11 0 71.5%
U.S. 9.3 69.3 21.2 0.2 70.7%
GPT-4o mini
(PO)
China 45.6 43.5 10.9 088.4%
U.S. 11.7 47.6 40.7 085.9%
GPT-4o mini
(FT)
China 40.3 53.8 5.9 0 76.3%
U.S. 9.1 67.3 23.6 0 75.0%
GPT-4o mini
(FT + PO)
China 42.5 51.5 6.0 0 78.3%
U.S. 9.2 66.4 24.4 0 73.9%
Based on these findings, we developed detailed opera-
tional guidelines for the LLM to ensure consistency and
accuracy in classification. Ultimately, we comprehensively
annotated 330,670 comments using the updated guidelines.
Table 3 presents the results of the sentiment analysis of com-
ments exchanged between Chinese and U.S. users regarding
each other’s countries. We categorized sentiments based on
three labels: negative, Neutral, and positive.
Regression Analysis
Since 2022, China’sDouyinplatform has mandated the dis-
closure of users’ provincial location information alongside
2https://anonymous.4open.science/r/DDPP-China-US-26A2
3https://cn.aliyun.com/product/bailian?from alibabacloud=
4https://platform.openai.com/docs/models/gpt-4o-mini
Table 3: Sentiment distribution of China and U.S.
Negative Neutral Positive Total
China 96,150 (45.55%) 91,322 (43.26%) 23,618 (11.19%) 211,090
U.S. 14,439 (11.36%) 59,170 (46.55%) 53,508 (42.09%) 127,117
their comments, providing us with detailed data for analyz-
ing regional emotional attitudes in China toward the United
States. We linked the themes and sentiments of comments
to their provincial IP addresses to study regional differences
and explore the factors influencing these variations. To eval-
uate the likelihood of observing negative comments, we used
a ordered logistic regression model (DeMaris 1995), where
the dependent variable is the comment sentiment catego-
rized into three levels: 1 representing negative, 2 represent-
ing neutral, and 3 representing positive. The provincial-level
explanatory factors are sourced from China’s Seventh Na-
tional Population Census. For further details, please refer to
the results section. Our study focuses exclusively on data
from China’s 31 provincial regions. Additionally, we applied
a fixed effects design at the short video level to control for
specific characteristics associated with each video. This ap-
proach allows for a more accurate analysis of the relation-
ship between predictor variables and outcomes within video
comments, minimizing the influence of content distribution
algorithms on variations in exposure.
RESULT
Topic Themes
Figure 4 (1)-(2) present the word cloud distributions in both
China and the U.S., based on the words’ higher weighted log
odds (Monroe, Colaresi, and Quinn 2008). The word cloud
of the four dimensions, as shown in appendix . Table 4 shows
that Chinese video comments mainly focus on Power Transi-
tion Theory (30.32%) and Complex Interdependence Theory
(29.18%), while U.S. comments emphasize Constructivism
(48.79%), reflecting differing concerns: China focuses on
power dynamics and interdependence, while the U.S. high-
lights the role of ideas and perceptions in China-U.S. rela-
tions.
Figure 1: Word cloud map of (we translated the Chinese into
English for display) (1) China; (2) U.S..
Power Transition Theory: Economic Strength and Val-
ues DialogueThe topic of “Power Transition Theory” is
related to seven phrases: 1. Economic Strength, 2. Great

Table 4: Distribution of the four theoretical perspectives in
the comments on China-U.S. relations
Total
Power
Transition
Theory
Complex
Interdependence
Theory
Constructivism
Global
Governance
Theory
China 211,090 64,004 (30.32%) 61,591 (29.18%) 49,744 (23.57%) 35,751 (16.93%)
U.S. 127,117 33,646 (26.47%) 11,240 (8.84%) 62,023 (48.79%) 20,208 (15.90%)
Power Rivalry, 3. Power Dismantlement, 4. Values Dia-
logue, 5. War and Conflict, 6. Political Party Rivalry, 7.
Racial Conflict. Among the U.S. and China, “Economic
Strength” is the most frequently discussed, and comments
typically reflect personal opinions. Chinese comments often
express personal views through phrases like “The Fed’s rate
cut benefits China” and “The U.S. government’s debt prob-
lem is severe.” U.S. comments include phrases like “China’s
rise is threatening the U.S. economy” These comments high-
light the global focus on the power transition between China
and the U.S., centered on economic strength.
Complex Interdependence Theory: Mutual Dependence
in Technology and IndustryThe theme of “Complex In-
terdependence Theory” includes four phrases: 1. Technolog-
ical Competition and Cooperation, 2. Financial Interdepen-
dence, 3. Industrial Synergy, and 4. Talent Exchange and
Interaction. In China, “Technological Competition and Co-
operation” is the most common, typically revolving around
discussions such as “If iPhone stops supporting updates for
WeChat (a Chinese social media app), I won’t use iPhone
anymore” and “Huawei phones are far ahead.” In the U.S.,
“Industrial Synergy” is more prevalent. Common phrases in-
clude “Made in China is essential for U.S. manufacturing”
These comments highlight the mutual dependence between
China and the U.S. in the fields of technology and eco-
nomics. China emphasizes technological competition and
cooperation across markets, while the U.S. focuses on in-
dustrial synergy, reflecting its reliance on Chinese products.
Constructivism: Cultural Perceptions and Value Pur-
suitsFrom a Constructivist perspective, the key themes
include: 1. Happy Life, 2. Culture and Education, 3. Im-
migration, 4. Public Safety, and 5. Gender/Racial Equality.
Chinese discourse predominantly centers on the aspiration
for a “Happy Life,” with emphasis on family well-being and
future generations, as seen in comments like “I really envy
your life.” In contrast, U.S. discussions are dominated by
“Culture and Education,” showcasing an appreciation and
interest in Chinese cultural elements, such as “I’m working
hard to learn Chinese,” and “This Chinese song has a beauti-
ful melody.” These differing focuses highlight how cultural
perceptions shape international relations. China prioritizes
social welfare and prosperity, while the U.S. focuses on cul-
tural exchange and education, reflecting constructivism’s in-
fluence on bilateral relations and international dynamics.
Global Governance Theory: Managing Global Chal-
lengesIncludes five themes: 1. Invasive Species, 2. Food
Security, 3. Public Health, 4. Environmental Protection, and
5. Multipolarity. In China, the primary focus is on manag-
ing invasive species, with discussions centered on the eco-
logical impacts and control strategies, such as “There are so
many carp in the U.S., Chinese fishermen should help them”
and “Using biological control to manage mosquitoes”. Con-
versely, U.S. discourse emphasizes “Food Security,” ad-
dressing sustainable food production and healthy eating
choices with comments like “This meat is lab-grown, very
eco-friendly” and “I only eat organic food.” These differing
priorities reflect China and U.S. unique environmental and
economic contexts within global governance.
Sentiment in China and U.S.
We analyzed these figures according to theoretical dimen-
sion types. Figure 2 illustrates the distribution of comments
expressing negative, positive, and neutral sentiments across
four theoretical dimensions in China (1) and the U.S. (2). As
shown in Figures 3 (1)-(3), in the Chinese sample, 45.55%
(96,150 comments) were categorized as “negative sentiment
towards the U.S.,” including 3.82% hate (8,068 comments)
and 41.73% criticism or complaints (88,082 comments). In
contrast, in the U.S. sample, 11.36% (14,439 comments)
were categorized as “negative sentiment towards China,” in-
cluding 2.63% hate (3,340 comments) and 8.73% criticism
or complaints (11,099 comments), as shown in Figures 3 (4)-
(6).
Figure 2: China-U.S. comments by sentiment (negative,
positive, neutral) within four theoretical frameworks: (1)
China’s comments on the U.S. (2) U.S. Comments on China.
Figure 3: The levels of negative sentiment expressed by
China and the U.S. towards each other are as follows: (1)
China’s overall negative sentiment, (2) China’s hate senti-
ment, (3) China’s criticism or complaints, (4) U.S. overall
negative sentiment, (5) U.S. hate sentiment, and (6) U.S.
criticism or complaints.

Figure 4 (1) (2) (3) display the levels of negative, posi-
tive, and neutral sentiment towards the U.S. across different
provinces in China. As shown in Figure 4 (2), the lowest
levels of negative sentiment towards the U.S. were found
in Shaanxi (42.13%), followed by Chongqing (42.34%) and
Shanxi (42.51%). In contrast, Hunan and Hainan exhibited
the highest levels of negative sentiment towards the U.S., at
51.01% and 48.38%, respectively.
Figure 4: The levels of negative, positive, and neutral senti-
ment towards the U.S. across different provinces in China:
(1) Negative. (2) Positive. (3) Neutral.
Levels of Negative Sentiment: A Regression
Analysis in China
We use regression analysis to examine variations in hate
sentiment across four theoretical dimensions and identify
thematic topics within short videos that attract higher lev-
els of hate sentiment. Additionally, we explore how regional
economic and cultural factors contribute to these sentiment
differences, focusing on three key factors: (1) provincial
GDP per capita (economic development), (2) the propor-
tion of ethnic minorities, and (3) internet penetration rate.
Control variables include the number of religious temples,
the foreign population, and Starbucks stores, which reflect
the influence of religious values (Halman and De Moor
1994), multicultural interaction (Lebedeva, Tatarko, and
Berry 2016), and openness to global influences, respec-
tively. Our regression results, shown in Table 5, indicate that
Global Governance Theory is linked to significantly higher
levels of negative sentiment compared to the other dimen-
sions. This may be due to the complex and contentious na-
ture of global governance issues, which often provoke emo-
tional responses in social media discussions. Furthermore,
Our results show that higher levels of economic develop-
ment and internet penetration are associated with lower odds
of comments being classified into more negative sentiment
categories. In economically developed regions, globaliza-
tion and exposure to diverse perspectives are more com-
mon. With increased international economic and cultural ex-
changes, users in these regions are more likely to adopt tol-
erant and open attitudes toward other countries and cultures.
Furthermore, ethnic diversity is significantly associated with
sentiment levels; regions with higher ethnic diversity exhibit
lower odds of more negative sentiment. Frequent interac-
tions with diverse cultural backgrounds and values may pro-
mote openness and inclusivity, encouraging users to respond
with understanding and respect when encountering different
cultural or value systems, rather than expressing hostility or
negativity.
Table 5: Ordered Logistic Regression Model Predicting the
Odds of “Negative” Comments
Variables Coefficient
ComplexInterdependence vs GlobalGovernance -0.324***
(0.021)
Constructivism vs GlobalGovernance -0.254***
(0.021)
PowerTransition vs GlobalGovernance -0.246***
(0.021)
GDP: middle vs bottom 0.001
(0.014)
GDPP: top vs bottom -0.042**
(0.020)
Internet penetration rate -0.282**
(0.138)
Ethnic minority middle vs lowest 0.009
(0.014)
Ethnic minority high vs lowest -0.047***
(0.015)
Religion -0.002
(0.005)
Foreign people 0.000
(0.000)
Starbucks -0.000
(0.001)
Video Fixed Effect YES
R2 0.1551
Number of Videos 1,142
Number of Comments 203,553
Data:Douyin.
standard errors in parentheses.
p<0.1, ** p<0.05, *** p<0.01
Discussion
China-U.S. Sentiment DivergenceOur analysis reveals a
significant emotional asymmetry in the responses from Chi-
nese and U.S. commenters when discussing each other’s
countries. Chinese comments largely express negative sen-
timents toward the U.S., focusing on perceived injustices,
competitive threats, and issues of national pride. These
views align with the realist perspective in international re-
lations (Gries 2004). In contrast, U.S. comments tend to
focus more on cultural perceptions and value differences,
rather than geopolitical competition. This reflects construc-
tivist theory, which stresses that international relations are
deeply shaped by ideas, identities, and social norms (Adler
1997). This divergence highlights the distinct ways in which
each country’s public sentiment is framed. For China, neg-
ative views toward the U.S. are driven by fears of national
security and concerns about global power rivalry. U.S. per-
spectives, on the other hand, tend to focus more on cultural
and ideological divides. This suggests that improving bilat-
eral relations will require addressing each nation’s unique
emotional and ideological concerns. For China, policies ac-
knowledging national pride and addressing security issues
could ease negative sentiments. In the U.S., fostering deeper
cultural understanding and challenging stereotypes about
China could bridge the perceptual gap.
Regional Variations in China’s PerceptionsOur study
reveals regional variations in emotional responses toward
the U.S. within China. Provinces with lower GDP, fewer
ethnic minorities, and limited internet access tend to ex-
press stronger negative emotions. This is due to limited me-

dia exposure, where official narratives often frame interna-
tional relations as competitive, fueling nationalist sentiment
(Gries et al. 2011). In contrast, more developed regions with
higher internet access and greater ethnic diversity encounter
diverse perspectives, leading to more nuanced views of the
U.S. Economic development and cultural diversity in these
areas reduce sensitivity to global competition, mitigating
negative sentiment. As China’s global role grows, address-
ing these regional differences is essential. Promoting media
literacy, cross-cultural communication, and inclusive narra-
tives could help reduce negative perceptions and foster more
balanced public sentiment.
SuggestionsDouyinandTikTokare important platforms
for public discussion. The role these platforms play in con-
tent management means they have a significant influence in
shaping mainstream narratives, which has sparked extensive
discussions about content management and the formation of
public opinion. RegardingDouyinandTikTok, the existing
algorithms may to some extent impact the diversity of dis-
course and could promote the prominence of certain senti-
ment and narratives. This algorithm-based content distribu-
tion method may pose challenges for cross-cultural under-
standing, foster the formation of echo chambers, potentially
exacerbate existing biases, and limit opportunities for peo-
ple to encounter diverse viewpoints (Wei et al. 2024; Harris
et al. 2023). AsDouyinandTikTokshape public opinion and
national identity, policymakers must understand the digital
ecosystems guiding user cognition. Effective diplomacy re-
lies on grasping regional socioeconomic contexts and algo-
rithmic forces. Encouraging cross-cultural communication
on these platforms can help reduce fragmentation and pro-
mote balanced dialogue.
CONCLUSIONS
China and the United States on social media platforms
prompted us to investigate the discourses surrounding
China-U.S. relations onDouyinandTikTok. Our study found
that comments predominantly focused on themes such as
“Economic Strength,” “Technological Competition and Co-
operation,” “Happy Life,” and “Invasive Species.” Sentiment
analysis showed that Chinese comments are more negative
than U.S. ones. In China, higher GDP, greater ethnic di-
versity, and higher internet penetration are associated with
more negative sentiments across regions. Overall, comments
from areas with lower economic development, less ethnic
diversity, and lower internet penetration tended to display
more negative sentiments. We call for further research to
delve into the underlying mechanisms and for strategies to
enhance mutual understanding and reduce negative percep-
tions on social media.
Limitations
This study has several limitations, primarily stemming from
the use of social media data fromDouyinandTikTok. First,
Douyin’s geographic data is restricted to China’s provincial-
level regions, which may obscure important local socio-
economic factors and regional disparities relevant to dis-
cussions on China-U.S. relations. Additionally,Douyin’s
location-based recommendation algorithms could bias the
dataset towards localized content, limiting the diversity of
viewpoints. To enhance data representativeness, we em-
ployed IP proxies from multiple provinces. Secondly, the
analysis ofTikTokis limited to accounts registered in the
United States and English and Chinese language comments.
Although some users may have relocated overseas, since the
account registration remains in the U.S., we consider their
comments to still reflect the attitudes of U.S. users toward
China. We believe that the scale of our dataset helps to mit-
igate the potential interference caused by this minority sce-
nario.
Moreover, excluding non-English and non-chinese com-
ments (such as those in Spanish) means the study primarily
captures the perspectives of English-speaking and chinese-
speakingTikTokusers in the U.S., potentially overlooking
viewpoints from other linguistic communities within the
country. The number of Chinese comments on tiktok is very
small (less than 1%), but we have retained the Chinese
comments. Despite the large dataset size, it only includes
users who actively participate in public comment sections,
which may not accurately represent the broader user base
(Inara Rodis 2021). Previous research indicates that male
users are more likely than female users to engage in online
commentary, potentially leading to a gender bias in the per-
spectives analyzed (K ¨uchler et al. 2023). While LLMs of-
fer more nuanced labels that capture complex sentiments,
their variable outputs can hinder replication (Gilardi, Al-
izadeh, and Kubli 2023). However, human annotators face
similar challenges (Garcia-Molina et al. 2016), and in our
study, the LLM maintained reasonably stable performance.
Finally, the findings are specific toDouyinandTikTokusers
and should be cautiously generalized to the broader popula-
tions of China or the U.S. Online discussions on these plat-
forms may not fully capture offline perceptions or broader
social attitudes, as they are influenced by the distinct social
and values environments of the two countries.
We chose the number of temples as a measurable indicator
of religious influence due to data availability, acknowledg-
ing its limitations in fully capturing the impact of religion
and moral values. In the absence of comprehensive micro-
level religious survey data in China, we used the number
of religious institutions as a proxy, reflecting the extent of
religious practice through their activities and memberships.
Since most religious activities in China are organized by
these institutions, their quantity provides a reasonable mea-
sure of religious influence in different regions (Wang and
Lin 2014).
ETHICAL STA TEMENTOur data is sourced from
publicly available internet sources. We prioritize user pri-
vacy and security, especially when handling sensitive geo-
location data. For comments from China, provincial geo-
location information is used, but with each province hous-
ing over one million people, individual identification is un-
likely. We do not infer user mobility or misuse the data; in-
stead, we associate it with comments for analysis. The aim
of our research is to understand public discussions on China-
U.S. relations, not to stereotype or stigmatize any individual
or country. We ensure that all data is anonymized, and only

random samples are published. We ensured that all data was
anonymized, and we only revealed a 10% random sample
with three variables: comments, topic labels, and sentiment
labels. This project has been approved by our Institutional
Review Board (IRB anonymous).
References
Adler, E. 1997. Seizing the middle ground: Constructivism
in world politics.European journal of international rela-
tions, 3(3): 319–363.
Ambrosetti, M. 2012.Power and Influence: Ideational and
Material Factors in the International Posture of China Ris-
ing as a Great Power. Ph.D. thesis, Georgetown University.
Ausat, A. M. A. 2023. The role of social media in shap-
ing public opinion and its influence on economic decisions.
Technology and Society Perspectives (TACIT), 1(1): 35–44.
Backstrom, L.; Sun, E.; and Marlow, C. 2010. Find me if
you can: improving geographical prediction with social and
spatial proximity. InProceedings of the 19th international
conference on World wide web, 61–70.
Badea, C. 2021. US–CHINA RELATIONS THROUGH
THE PERSPECTIVE OF SOCIAL-CONSTRUCTIVISM.
Studia Universitatis Babes-Bolyai-Studia Europaea, 66(2):
363–390.
Bao, J.; Zheng, Y .; Wilkie, D.; and Mokbel, M. 2015. Rec-
ommendations in location-based social networks: a survey.
GeoInformatica, 19: 525–565.
Baucom, E.; Sanjari, A.; Liu, X.; and Chen, M. 2013. Mir-
roring the real world in social media: Twitter, geolocation,
and sentiment analysis. InProceedings of the 2013 inter-
national workshop on Mining unstructured big data using
natural language processing, 61–68.
Baum, M. A.; and Potter, P. B. 2008. The relationships be-
tween mass media, public opinion, and foreign policy: To-
ward a theoretical synthesis.Annu. Rev. Polit. Sci., 11(1):
39–65.
Baum, M. A.; and Potter, P. B. 2019. Media, public opinion,
and foreign policy in the age of social media.The Journal
of Politics, 81(2): 747–756.
Baumer, E. P.; Mimno, D.; Guha, S.; Quan, E.; and Gay,
G. K. 2017. Comparing grounded theory and topic model-
ing: Extreme divergence or unlikely convergence?Journal
of the Association for Information Science and Technology,
68(6): 1397–1410.
Bennett, W. L. 2012. The personalization of politics: Polit-
ical identity, social media, and changing patterns of partici-
pation.The annals of the American academy of political and
social science, 644(1): 20–39.
Boffone, T. 2022a. Introduction: The rise of TikTok in US
culture. InTikTok cultures in the United States, 1–13. Rout-
ledge.
Boffone, T. 2022b.TikTok cultures in the United States.
Routledge.
Boyd-Graber, J.; Hu, Y .; Mimno, D.; et al. 2017. Applica-
tions of topic models.Foundations and Trends® in Informa-
tion Retrieval, 11(2-3): 143–296.
Brady, W. J.; Jackson, J. C.; Lindstr¨om, B.; and Crockett, M.
2023. Algorithm-mediated social learning in online social
networks.Trends in Cognitive Sciences.
Cao, X.; MacNaughton, P.; Deng, Z.; Yin, J.; Zhang, X.; and
Allen, J. G. 2018. Using twitter to better understand the
spatiotemporal patterns of public sentiment: A case study in
Massachusetts, USA.International journal of environmen-
tal research and public health, 15(2): 250.
Chen, F.; and Wang, G. 2022. A war or merely friction? Ex-
amining news reports on the current Sino-US trade dispute
in The New York Times and China Daily.Critical Discourse
Studies, 19(1): 1–18.
Chen, S.; Chen, X.; Lu, Z.; and Huang, Y . 2023. ” My
Culture, My People, My Hometown”: Chinese Ethnic Mi-
norities Seeking Cultural Sustainability by Video Blogging.
Proceedings of the ACM on Human-Computer Interaction,
7(CSCW1): 1–30.
Chen, X.; Valdovinos Kaye, D. B.; and Zeng, J. 2021. # Pos-
itiveEnergy Douyin: Constructing “playful patriotism” in a
Chinese short-video application.Chinese Journal of Com-
munication, 14(1): 97–117.
Chengqiu, W. 2020. Ideational differences, perception gaps,
and the emerging Sino–US rivalry.The Chinese Journal of
International Politics, 13(1): 27–68.
Chu, S.-C.; and Choi, S. M. 2011. Electronic word-of-
mouth in social networking sites: A cross-cultural study of
the United States and China.Journal of Global Marketing,
24(3): 263–281.
Collins, S. D.; DeWitt, J. R.; and LeFebvre, R. K. 2019.
Hashtag diplomacy: twitter as a tool for engaging in public
diplomacy and promoting US foreign policy.Place brand-
ing and public diplomacy, 15: 78–96.
Corbin, J.; and Strauss, A. 2014.Basics of qualitative re-
search: Techniques and procedures for developing grounded
theory. Sage publications.
DeMaris, A. 1995. A tutorial in logistic regression.Journal
of Marriage and the Family, 956–968.
Deng, Y . 2001. Hegemon on the offensive: Chinese per-
spectives on US global strategy.Political Science Quarterly,
116(3): 343–365.
Duncombe, C. 2019. The politics of Twitter: emotions and
the power of social media.International Political Sociology,
13(4): 409–429.
Friedberg, A. L. 2005. The future of US-China relations: Is
conflict inevitable?International security, 30(2): 7–45.
Garcia-Molina, H.; Joglekar, M.; Marcus, A.;
Parameswaran, A.; and Verroios, V . 2016. Challenges
in data crowdsourcing.IEEE Transactions on Knowledge
and Data Engineering, 28(4): 901–911.
Gilardi, F.; Alizadeh, M.; and Kubli, M. 2023. ChatGPT
outperforms crowd workers for text-annotation tasks.Pro-
ceedings of the National Academy of Sciences, 120(30):
e2305016120.
Gray, J. E. 2021. The geopolitics of” platforms”: The TikTok
challenge.Internet policy review, 10(2): 1–26.

Green, J. F. 2018. Transnational delegation in global en-
vironmental governance: When do non-state actors govern?
Regulation & Governance, 12(2): 263–276.
Gries, P. H. 2004.China’s new nationalism: Pride, politics,
and diplomacy. Univ of California Press.
Gries, P. H.; Zhang, Q.; Crowson, H. M.; and Cai, H. 2011.
Patriotism, nationalism and China’s US policy: Structures
and consequences of Chinese national identity.The China
Quarterly, 205: 1–17.
Grootendorst, M. 2022. BERTopic: Neural topic model-
ing with a class-based TF-IDF procedure.arXiv preprint
arXiv:2203.05794.
Guan, Y .; Tingley, D.; Romney, D.; Jamal, A.; and Keohane,
R. 2020. Chinese views of the United States: evidence from
Weibo.International Relations of the Asia-Pacific, 20(1):
1–30.
Halman, L.; and De Moor, R. 1994. Religion, churches and
moral values. InThe individualizing society, 37–65. Brill.
Harris, C.; Johnson, A. G.; Palmer, S.; Yang, D.; and Bruck-
man, A. 2023. ” Honestly, I Think TikTok has a Vendetta
Against Black Creators”: Understanding Black Content Cre-
ator Experiences on TikTok.Proceedings of the ACM on
Human-Computer Interaction, 7(CSCW2): 1–31.
Higgott, R. A.; Underhill, G. R.; and Bieler, A. 2000. Non-
state actors and authority in the global system.
Holsti, O. R. 2009.Public opinion and American foreign
policy. University of Michigan Press.
Hudson, V . M. 2005. Foreign policy analysis: Actor-specific
theory and the ground of international relations.Foreign
policy analysis, 1–30.
Ikenberry, G. J. 2008. The rise of China and the future of the
West-Can the liberal system survive.Foreign Aff., 87: 23.
Inara Rodis, P. d. C. 2021. Let’s (re) tweet about racism
and sexism: responses to cyber aggression toward Black
and Asian women.Information, Communication & Society,
24(14): 2153–2173.
Ittefaq, M.; Abwao, M.; Baines, A.; Belmas, G.; Kamboh,
S. A.; and Figueroa, E. J. 2022. A pandemic of hate: So-
cial representations of COVID-19 in the media.Analyses of
Social Issues and Public Policy, 22(1): 225–252.
Jaworsky, B. N.; and Qiaoan, R. 2021. The politics of blam-
ing: The narrative battle between China and the US over
COVID-19.Journal of Chinese political science, 26(2):
295–315.
Kaye, D. B. V .; Chen, X.; and Zeng, J. 2021. The co-
evolution of two Chinese mobile short video apps: Parallel
platformization of Douyin and TikTok.Mobile Media &
Communication, 9(2): 229–253.
Ke, W. 2023. Unraveling the TikTok Paradox: Western Con-
cerns, Economic Implications, and Prospects.Highlights in
Business, Economics and Management, 20: 489–495.
King, G.; Murray, C. J.; Salomon, J. A.; and Tandon, A.
2004. Enhancing the validity and cross-cultural comparabil-
ity of measurement in survey research.American political
science review, 98(1): 191–207.
Kokas, A. 2018. Platform patrol: China, the United States,
and the global battle for data security.The Journal of Asian
Studies, 77(4): 923–933.
K¨uchler, C.; Stoll, A.; Ziegele, M.; and Naab, T. K. 2023.
Gender-related differences in online comment sections: find-
ings from a large-scale content analysis of commenting be-
havior.Social Science Computer Review, 41(3): 728–747.
Kuchler, T.; Russel, D.; and Stroebel, J. 2022. JUE In-
sight: The geographic spread of COVID-19 correlates with
the structure of social networks as measured by Facebook.
Journal of urban economics, 127: 103314.
Lebedeva, N.; Tatarko, A.; and Berry, J. W. 2016. Intercul-
tural relations among migrants from Caucasus and Russians
in Moscow.International Journal of Intercultural Relations,
52: 27–38.
Li, H.; Zhu, H.; Du, S.; Liang, X.; and Shen, X. 2016. Pri-
vacy leakage of location sharing in mobile social networks:
Attacks and defense.IEEE Transactions on Dependable and
Secure Computing, 15(4): 646–660.
Liu, J.; and Yang, L. 2022. “Dual-Track” platform gover-
nance on content: A comparative study between China and
United States.Policy & Internet, 14(2): 304–323.
Liu, L. 2021. The rise of data politics: digital China and the
world.Studies in Comparative International Development,
56(1): 45–67.
Milusheva, S.; Marty, R.; Bedoya, G.; Williams, S.; Re-
sor, E.; and Legovini, A. 2021. Applying machine learn-
ing and geolocation techniques to social media data (Twitter)
to develop a resource for urban planning.PloS one, 16(2):
e0244317.
Monroe, B. L.; Colaresi, M. P.; and Quinn, K. M. 2008.
Fightin’words: Lexical feature selection and evaluation for
identifying the content of political conflict.Political Analy-
sis, 16(4): 372–403.
Pan, C. 2012.Knowledge, desire and power in global poli-
tics: Western representations of China’s rise. Edward Elgar
Publishing.
prudent, F. 2023. Douyin vs. Douyin: Dreams, Rampage,
Paradox and Reconciliation.
Qin, B.; and Ge, X. 2023. Did the popularization of the Inter-
net impact Chinese citizens’ attitude towards foreign coun-
tries? An empirical study based on two surveys.Plos one,
18(9): e0291091.
Raza, A.; and Aslam, M. W. 2024. Algorithmic Curation in
Facebook: An Investigation into the role of AI in Forming
Political Polarization and Misinformation in Pakistan.An-
nals of Human and Social Sciences, 5(2): 219–232.
Roberto, K. J.; Johnson, A. F.; and Rauhaus, B. M. 2020.
Stigmatization and prejudice during the COVID-19 pan-
demic.Administrative Theory & Praxis, 42(3): 364–378.
Ross, R. S.; and Feng, Z. 2008.China’s ascent: power, se-
curity, and the future of international politics. Cornell Uni-
versity Press.
Schindler, S.; Alami, I.; DiCarlo, J.; Jepson, N.; Rolf, S.;
Bayırba˘g, M. K.; Cyuzuzo, L.; DeBoom, M.; Farahani,
A. F.; Liu, I. T.; et al. 2024. The second cold war: US-China

competition for centrality in infrastructure, digital, produc-
tion, and finance networks.Geopolitics, 29(4): 1083–1120.
Shahsavari, S.; Holur, P.; Wang, T.; Tangherlini, T. R.; and
Roychowdhury, V . 2020. Conspiracy in the time of corona:
automatic detection of emerging COVID-19 conspiracy the-
ories in social media and the news.Journal of computational
social science, 3(2): 279–317.
Swedlow, B.; and Wyckoff, M. L. 2009. Value preferences
and ideological structuring of attitudes in American public
opinion.American Politics Research, 37(6): 1048–1087.
Thelwall, M. 2018. Social media analytics for YouTube
comments: Potential and limitations.International Journal
of Social Research Methodology, 21(3): 303–316.
Wagner, K. B. 2023. TikTok and its mediatic split: the
promotion of ecumenical user-generated content alongside
Sinocentric media globalization.Media, Culture & Society,
45(2): 323–337.
Wang, Q.; and Lin, X. 2014. Does religious beliefs af-
fect economic growth? Evidence from provincial-level panel
data in China.China Economic Review, 31: 277–287.
Wei, Z.; Li, M.; Zhang, P.; Liu, X.; Qu, H.; and Hui, P.
???? ContextAware: A Multi-Agent Framework for Detect-
ing Harmful Image-Based Comments on Social Media.
Wei, Z.; Xie, Y .; Xiao, D.; Zhang, S.; Hui, P.; and Zhou,
M. 2024. Social media discourses on interracial intimacy:
Tracking racism and sexism through chinese geo-located so-
cial media data. InProceedings of the ACM Web Conference
2024, 2337–2346.
Wei, Z.; Xu, X.; and Hui, P. 2024. Digital democracy
at crossroads: A meta-analysis of web and ai influence on
global elections. InCompanion Proceedings of the ACM
Web Conference 2024, 1126–1129.
Zhang, B. 2020. Understanding changes in Sino-US re-
lations from a historical perspective.China International
Strategy Review, 2(1): 1–13.
Zhang, C. 2019. Right-wing populist discourse on Chinese
social media: Identity, otherness, and global imaginaries.
Les Cahiers du Cevipol, 19(3): 2–31.
Zhao, Q.; and Liu, G. 2010. Managing the challenges of
complex interdependence: China and the United States in
the era of globalization.Asian Politics & Policy, 2(1): 1–23.
Zheng, D. X.; Mulligan, K. M.; and Scott, J. F. 2021. TikTok
and dermatology: an opportunity for public health engage-
ment.Journal of the American Academy of Dermatology,
85(1): e25–e26.
Zhou, M.; Wei, Z.; and Liao, J. 2024. How Can the Uni-
versal Disclosure of Provincial-level IP Geolocation Change
the Landscape of Social Media Analysis.ACM SIGWEB
Newsletter, 2024(Autumn): 1–9.

APPENDIX
40 Keywords for Search and Extraction
Table 6:Keyword search and extraction between China
and the United States
Type China (Douyin) U.S. (TikTok)
USA China
American Chinese
American Dream Chinese Dream
American Society Chinese Society
American Economy Chinese Economy
American Development Chinese Development
American Election Chinese Politics
American Culture Chinese Culture
American Travel China Travel
US Interest Rate Cuts China Finance
American Immigration Learn Chinese
American Bankruptcy The Chinese Threat
American Government Chinese Government
Washington Beijing
American Life China Life
American Food Chinese Food
Los Angeles Shanghai
New York Guangzhou
American Streets China Streets
American Decline China Decline
Word cloud map of four theoretical dimensions
Figure 5: Word cloud map of (we translated the Chinese into
English for display) (1) Power Transition Theory - 7 words
in China; (2) Complex Interdependence Theory - 4 words
in China; (3) Constructivism - 5 words in China; (4) Global
Governance Theory - 5 words in China; (5) Power Transi-
tion Theory - 7 words in U.S.; (6) Complex Interdependence
Theory - 4 words in U.S.; (7) Constructivism - 5 words in
U.S.; (8) Global Governance Theory - 5 words in U.S..
