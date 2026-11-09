---
title: 'Inconsistencies in Classification of Online News Articles: A Call for Common Standards in Brand
  Safety Services'
url: https://arxiv.org/abs/2601.01303
category: digital-marketing
subcategory: empirical
date: 2026-01
venue: ''
authors:
- Michael Smith
- Riley Grossman
- Antonio Torres-Aguero
- Pritam Sen
- Cristian Borcea
source: arxiv
pdf_url: https://arxiv.org/pdf/2601.01303
pages: 17
chars: 85460
fetched_at: '2026-11-08T13:16:40+00:00'
kb_version: 1
---

# Inconsistencies in Classification of Online News Articles: A Call for Common Standards in Brand Safety Services

Inconsistencies in Classification of Online News Articles:
A Call for Common Standards in Brand Safety Services
Michael Smith1, Riley Grossman1, Antonio Torres-Ag¨uero2, Pritam Sen1, Cristian Borcea1,
Yi Chen1
1New Jersey Institute of Technology, Newark, New Jersey, USA
2DeepSee.io, Los Angeles, California, USA
{mes6, rag24, ps37, borcea, yi.chen}@njit.edu, antonio@deepsee.io
Abstract
This study examines inconsistencies in the brand safety clas-
sifications of online news articles by analyzing ratings from
three leading brand safety providers, DoubleVerify, Integral
Ad Science, and Oracle. We focus on news content because of
its central role in public discourse and the significant financial
consequences of unsafe classifications in a sector that is al-
ready underserved by digital ad spending. By collecting data
from 4,352 news articles on 51 domains, our analysis shows
that brand safety services often produce conflicting classi-
fications, with significant discrepancies between providers.
These inconsistencies can have harmful consequences for
both advertisers and publishers, leading to misplaced adver-
tising spending and revenue losses. This research provides
critical insights into the shortcomings of the current brand
safety landscape. We argue for a standardized and transpar-
ent brand safety system to mitigate the harmful effects of the
current system on the digital advertising ecosystem.
1 Introduction
Brand safety services are essential for advertisers to ensure
that their ads do not appear alongside harmful or inappro-
priate content. Their value is best demonstrated in a recent
paper that surveyed over 200 decision makers from compa-
nies spending more than $10 million annually on advertis-
ing, finding that more than 80% were concerned with brand
safety. These same participants indicated that they would
pay a nearly 50% premium to guarantee that their adver-
tisements would only appear alongside safe content (John-
son, V oorhees, and Khodakarami 2023), thus highlighting
the need for brand safety classification tools.
Our study focuses on DoubleVerify (DV), Integral Ad Sci-
ence (IAS) and Oracle, because they are three of the most
widely used state-of-the-art providers of brand safety tech-
nology in the industry (Elmore 2024; Business Insider 2024;
Barwick 2024). Each brand safety provider offers a differ-
ent, proprietary classification system to assess the safety of
online content. But all claim to leverage AI, natural lan-
guage processing (NLP) and machine learning (ML) tech-
nologies to evaluate whether a webpage’s content is safe
for advertising based on predefined safety categories (e.g.,
violence, adult, alcohol) (Vargo, Hopp, and Agarwal 2024;
Griffin 2023).
Correct classification of brand safety is critical for both
advertisers and publishers, and yet, remains a huge chal-
lenge. On one hand, an article with safe content may be
misclassified as unsafe. For example, an article discussing
recent advances in breast cancer research can be classi-
fied as unsafe due to the presence of the keyword “breast”.
In such cases, advertisers lose opportunities and publish-
ers face reduced revenues. On the other hand, an article
with potentially unsafe content may be misclassified as safe,
which results in advertisers wasting their budget and also
risking their brand’s reputation. One well-known example
is YouTube’s “Adpocalypse”. Despite YouTube’s keyword-
based brand safety controls, major brands like AT&T, Pepsi,
and Verizon pulled their ads from the platform after discov-
ering their ads were placed alongside extremist or inappro-
priate content (Reed 2017). This highlights how misclassi-
fication can lead to financial and reputational damage for
advertisers and publishers.
While professional editorial review reduces the likelihood
of toxic language compared to user-generated platforms, it
does not eliminate risk. News outlets regularly cover vio-
lence, pandemics, political extremism, and other sensitive
topics that can trigger brand safety systems. In these cases,
the underlying content is not ‘unsafe’ in the sense of misin-
formation or hate speech, but it is nevertheless subject to
unsafe ratings due to its subject matter. Thus, news con-
tent presents a unique challenge: the coexistence of edito-
rial standards with recurring coverage of high-risk topics.
Misclassifying safe digital news content as unsafe will harm
the struggling news publishers. Despite generating $12 bil-
lion in digital advertising revenue in 2019, an industry re-
port estimated that news publishers across the United States
failed to generate an additional $2.8 billion because of erro-
neous, or overly cautious, keyword-blocking practices that
prevented safe content from being monetized (CHEQ 2020).
News publishers are increasingly reliant on digital ad-
vertising as print revenues decline (CHEQ 2020). However,
even digital income is under strain: AI-driven search features
have reduced referral traffic, with one 2025 report showing
a 7% drop in visits from Google year over year (Kint 2025).
This makes accurate brand safety classification vital, since
mislabeling legitimate content as unsafe directly undermines
publishers’ ability to monetize their limited traffic.
It is noteworthy that the aforementioned examples were
the result of keyword-based brand safety tools. At the time,
there was hope that newer AI and contextual-based brand
arXiv:2601.01303v1  [cs.CY]  3 Jan 2026

Bid Request
Advertiser
Article on forbes.com
Bid Response
Brand Safety Providers
Demand Side Platform Sell Side Platform
12
Figure 1: Three brand safety providers each classify an
article at Forbes.com
safety tools would do more accurate classifications (CHEQ
2020). Today, AI-based brand safety classification is preva-
lent. Our paper investigates whether this technological ad-
vancement is satisfactory.
The objective of this study is to analyze the effectiveness
and consistency of the major brand safety providers: DV ,
IAS, and Oracle, to determine if they adequately protect the
reputation of the advertisers’ brand without losing advertis-
ing opportunities, and at the same time, prevent publishers’
safe content from becoming demonetized.
Our study shows that different providers may give differ-
ent classifications for the same article. Figure 1 shows how
DV , IAS and Oracle categorize an article on Forbes’ web-
site. The article discusses crime, a topic that can be deemed
unsafe. While Oracle classifies the content as unsafe and re-
lated to crime, IAS deems it unsafe with a low risk of vio-
lence, and DV classifies the article as safe. This illustrates
the significant variation in the way brand safety tools inter-
pret and classify the same content. If safety classifications
are inconsistent, publishers would be confused about how to
avoid demonetization, and advertisers do not know what fil-
ters to set to avoid placement alongside undesirable content.
Few studies have evaluated the effectiveness of brand
safety tools. One evaluated brand safety classifications on
Reddit (Vargo, Hopp, and Agarwal 2024), and another eval-
uated the brand safety classification of social media influ-
encers’ content (Bishop 2021). Our research differs from
these works in several aspects. First, instead of studying
user-generated content on social media platforms, we study
the brand safety classification of news articles on reputable
websites. News content was selected because it is a major
concern for advertisers, and digital advertising revenue is
a key profit source for publishers. Since news content en-
compasses a broad range of topics and styles, our findings
are generalizable. Second, we evaluate multiple third-party
brand safety providers, which are widely used in the online
advertising industry. Furthermore, we study many dimen-
sions of brand safety (e.g., violence, crime, alcohol) instead
of just considering general toxicity, as in prior literature.
Inspired by the Forbes Ad Inspector 1, we built a data
collection tool and collected brand safety data from 4,352
articles from popular news websites (e.g., nytimes.com,
cnn.com, economist.com).
1https://forbes.github.io/ad-inspector/
This study presents several major findings from our anal-
ysis of these 4,352 articles. First, brand safety is a preva-
lent issue for the news media that the public may not be
aware of. Our research indicates that brand safety providers
have a significant impact on the advertising ecosystem and
the news media publishers. Of the articles with brand safety
data, 43.99% were classified as “unsafe” by at least one of
the three brand safety providers (Section 4.1). This impact is
felt most by publishers that focus on breaking/general news,
as we find that articles from these domains are more likely
to be classified as unsafe (52.14% of articles).
Second, we identified significant inconsistencies in the
overall article classifications (i.e., whether the content is
unsafe for any reason) among the brand safety providers.
Disagreement in an article’s brand safety rating occurs in
22.98% of the cases where two providers rate the same ar-
ticle, and in 41.57% of cases where all three providers give
ratings. Furthermore, we evaluate interrater reliability with
Krippendorff’s alpha, which adjusts for agreement that may
occur by chance. The interrater reliability between all three
providers, and each pair of providers, falls well below the
conventional thresholds, indicating unreliable ratings (Sec-
tion 4.1).
Third, an article may be unsafe for different categories,
such as violence, adult content, hate speech, or drugs.
Providers disagree not only on the assessment of an arti-
cle’s overall brand safety, but also on brand safety cate-
gories (see Table 1 for all categories). Different providers
adopt different safety categories and different risk levels.
Even when two providers consider the same safety category,
their assessment of an article may be different. Disagree-
ments between two and three providers occurred in 62.40%
and 70.0% of cases, respectively, when at least one provider
rated the article as unsafe for the category. Furthermore, the
discrepancies vary significantly between different safety cat-
egories. The hate speech safety category, for example, was
inconsistent 87% of the time; while the death/injury cate-
gory was inconsistent 57% of the time (Section 4.2).
Furthermore, our study shows that the current brand
safety classification is not reliable even within the ratings
assigned by the same provider. For instance, IAS rates one
article as unsafe regarding “Illegal and Recreational Drugs”,
but safe regarding “Drugs” (Section 4.2).
The absence of a common standard may contribute
to inconsistencies in brand safety classifications between
providers. The Global Alliance for Responsible Media
(GARM) previously provided a framework that defined a
set of brand safety categories and risk levels to inform
decision-making across platforms, advertisers, publishers,
and brand safety providers. However, GARM was discon-
tinued on August 9th, 2024 after a lawsuit from X (formerly
Twitter) (Gollasch 2024).
The Media Ratings Council (MRC) performs audits on
several brand safety tools based on guidelines co-developed
with the Interactive Advertising Bureau (IAB). However,
these guidelines are not a comprehensive framework for
brand safety and do not include specific definitions or exam-
ples of what constitutes safe or unsafe content (MRC 2018).
The need for a unified and transparent framework is under-

scored by the news in October 2024 that the US government
is interested in investigating brand safety scandals (Barwick
2024), signaling broader concerns about systemic issues in
the industry.
The contributions of our study are threefold. First, to the
best of our knowledge, this is the first work that assesses
widely used brand safety tools in news articles. Second,
our comprehensive analysis shows the prevalence of brand
safety usage in the industry and, at the same time, the incon-
sistency of the brand safety classification system for news
articles. Furthermore, our findings call for action on stan-
dardizing guidelines in the space of brand safety. Specif-
ically, a unified framework of brand safety categories be-
tween providers is needed. Reliable brand safety tools that
are not self-contradicting are required, and greater consis-
tency among different brand safety tools should be expected.
A more standardized and transparent system, with explain-
able classifications, would reduce risks for advertisers, en-
sure fairness for publishers, and promote trust within the
digital advertising ecosystem.
2 Related Work
Brand safety has become a central concern for advertisers,
as ensuring that ads do not appear next to harmful or in-
appropriate content is crucial to protecting a brand’s rep-
utation (Johnson, V oorhees, and Khodakarami 2023; Lee,
Kim, and Lim 2021; Marvin and Meisel 2018; Griffin 2023;
Hemmings 2021). Early approaches to brand safety relied
largely on keyword-based filtering systems, which flagged
content based on the presence of specific terms without ac-
counting for context. Later, advanced methods that incorpo-
rate natural language processing (NLP) and machine learn-
ing (ML) were introduced to more effectively analyze the
content (Vargo, Hopp, and Agarwal 2024; Griffin 2023).
Two works are related to ours in that they also evaluate
brand safety tools, but in different contexts. The most rele-
vant one examines Reddit’s brand safety classifications and
compares them with toxicity scores calculated by the Per-
spective API2. The authors find evidence of misclassifica-
tions, particularly on high-traffic forums, where potential ad
revenues may influence safety classifications (Vargo, Hopp,
and Agarwal 2024). The second most relevant work stud-
ies influencer management tools, which help pair advertis-
ers with social media influencers and rate the brand safety
of social media influencers’ content. This study found that
one such tool used a list of keywords to calculate a “fam-
ily friendly rating” and was systematically biased against
LGBTQ creators due to words like “queer” and “gay” falling
on the keyword list (Bishop 2021).
Our study differs in several important aspects. We focus
on ratings of news articles from multiple reputable websites
(instead of user-generated content) and analyze how multi-
ple brand safety providers classify the content (instead of a
single provider). Unlike previous work, we examine classi-
fication variation across numerous brand safety dimensions
(e.g., violence, crime, sexual content).
2https://www.perspectiveapi.com/
In the larger literature on brand safety, several articles try
to address how placement alongside unsafe content can af-
fect advertising effectiveness or brand reputation. One paper
finds that it does not decrease effectiveness in the case of ad-
vertisements shown before “unsafe” Youtube videos (Bell-
man et al. 2018). Others have found that the advertisement’s
effectiveness and brand’s reputation are negatively affected
when advertisements are placed next to offensive or unsafe
content (Johnson, V oorhees, and Khodakarami 2023; Lee,
Kim, and Lim 2021). These studies are orthogonal to ours,
but show the importance of brand safety for advertisers.
Several works are devoted to the development of image-
based classifiers to classify images and videos as unsafe with
respect to adult content (V o, Cao, and Ton-That 2020; Wang
et al. 2018; Jin, Wang, and Tan 2019; Ou et al. 2017), and ad-
ditional sensitive safety categories such as gambling, guns,
and gore (V o, Cao, and Ton-That 2020). These works are
also orthogonal to ours in that they attempt to build new
classification systems for image and video content, while we
audit existing systems that focus primarily on text content.
Our work relates to the broader literature on the shortcom-
ings of algorithmic content moderation. Content moderation
differs from brand safety classification in that it is applied
to user-generated content instead of reputable news articles,
and the goal is to protect users from toxic content (e.g., pro-
fanity or slurs) instead of advertisers from negative or in-
appropriate topics (e.g., violence). However, there are some
similarities as the ultimate goal is to classify content based
on its safety. One study finds that automated content moder-
ation tools struggle to replicate nuanced human moderation
decisions in Reddit (Samory 2021). Another study finds that
LLMs can improve content moderation performance over
traditional NLP tools (e.g., Perspective API), but that perfor-
mance varies significantly between different LLMs (Kumar,
AbuHashem, and Durumeric 2024). This finding echoes the
inconsistencies we observe across brand safety providers.
Prior research has also found that misclassifications result-
ing from algorithmic content moderation are unequally dis-
tributed across demographic groups (Gomez et al. 2024). For
example, the Perspective API tool was shown to unfairly
penalize the content of LGBTQ influencers (Oliva, Anto-
nialli, and Gomes 2021). Similarly, unfair decisions against
the LGBTQ, black, and blind communities have been found
on platforms such as YouTube, TikTok, and Twitter (Kings-
ley et al. 2022; Ball-Burack et al. 2021; Lyu et al. 2024;
Harris et al. 2023; Vaccaro et al. 2021).
Related literature has increasingly advocated for stan-
dardized, transparent, and contestable content moderation
frameworks. Many researchers recognize that content mod-
eration policy changes often happen silently, and advocate
for greater transparency and clearer definitions of what is
and is not allowed (Pisharody et al. 2025; Harris et al. 2023;
Gomez et al. 2024). Several papers further propose explain-
able algorithms for content moderation so users get detailed
answers for why their content was targeted (Kingsley et al.
2022; Gomez et al. 2024). (Vaccaro et al. 2021) propose
mechanisms for making decisions contestable by affected
users. Our paper supports this growing consensus and calls
for standardization, transparency, explainability, and mech-

anisms that allow for appealing incorrect decisions in brand
safety classification protocols .
3 Method
This section presents the methodology used to collect and
analyze data for this study. First, Section 3.1 provides a
brief overview of how brand safety tools work. Then, we de-
scribe our system, illustrated in Figure 2, in Section 3.2 (data
collection) and Section 3.3 (data processing). Data collec-
tion involves two specialized web crawlers to collect brand
safety data in popular online news domains. Data process-
ing involves several data cleaning steps to extract provider-
specific brand safety details, which are then used in the anal-
ysis presented in Section 4. The Github repository with the
processed dataset and complete code for both crawlers will
be made available after the review process.
3.1 How Brand Safety Tools Work
Brand safety providers collect page text and metadata (e.g.,
title) for each article, and use proprietary AI and natural
language processing (NLP) models, as well as rule-based
heuristics to assign risk levels across predefined safety cat-
egories. These classifications are stored on the provider’s
servers and are used to protect advertisers from placing their
ads next to unsafe content.
There are two primary ways for advertisers to obtain
ad inventory: through real-time bidding (RTB) auctions, or
through direct deals with publishers (e.g., guaranteed deals).
Publishers often manage their ad inventory using Google Ad
Manager (GAM), which helps publishers decide whether to
show an ad from an advertiser who has a guaranteed deal, or
to show the winning ad from an RTB auction. In an RTB auc-
tion, safety classifications are shared with the demand side
platform (DSP), who represents the advertiser. The DSP will
not bid on behalf of an advertiser if the impression does not
meet the advertiser’s predefined brand-safety requirements.
Because this exchange happens server-side, these classifica-
tions are not visible to external observers.
In cases where publishers integrate brand safety tools di-
rectly with GAM via Google Publisher Tags (GPT), the pro-
cess occurs on the client side, allowing us to observe the
classifications. In this setup, the publisher’s code issues an
HTTP request to the brand safety provider when an article is
loaded. The provider either retrieves a pre-computed rating
Page-level
targeting
Ad slot-level
targeting
Store data as key-value pairs
Article
Check GPT Tag
OnLoad
Overall
Classification
Specific
Classifications
Extract Brand Safety
Company Specific Tags
Top domains
from Alexa &
Tranco List
Collaborating
Online
Publisher
Crawl Google
News
Filter out
irrelevant URLs
Domain Selection
Pre-defined list
URL Selection
News Articles
Collected Data
Report
Data Collection Data Processing and Analysis
Figure 2: System Design
from its database or performs the classification in real time
and returns the result. These results are then appended to the
HTTP request sent to GAM via the GPT tag, where they can
influence the ad decision logic. The GPT integration thus en-
ables both publishers (and researchers) to access page-level
brand safety scores during article rendering.
3.2 Data Collection Phase
The first phase of our system focuses on 1) collecting the
URLs of articles from various news domains, and 2) collect-
ing the GPT data for the articles.
Domain SelectionWe start with a list of 5,397 popular
news domains developed by von Hohenberg et al. (2021),
that was the union of Alexa’s 1,000 top domains, domains
frequently tweeted by US politicians, domains for local
newspapers and television stations, and domains frequently
visited by survey participants. This initial list does not rank
the domains. We use the Tranco rankings (Le Pochat et al.
2019), which are widely adopted in academic research as
an objective listing of web domain popularity, to rank the
initial list of news domains by popularity.
We then visit the top 250 news domains . We only visit
the top 250, so our analysis uncovers brand safety data pat-
terns across the most influential online news sources. For
each domain, we visit it using the Forbes Ad-Inspector tool,
implemented as a bookmarklet. This tool displays all of the
Google Publisher Tag (GPT) data related to the ads on the
page. We use the tool to determine whether brand safety data
is available on each website.
If the publisher chooses to use the brand safety providers
tags’ with its Google Ad Manager ad server (see Sec-
tion 3.1), the brand safety data will be visible to us in the
GPT data. Based on this filtering, we identified 55 top news
domains that we could capture brand safety data from. In
addition, our collaborating online publisher (who requested
to be anonymous) provides data for four of their domains.
Thus, we have a total of 59 target domains for analysis. No-
tably, websites choosing not to collect brand safety data does
not affect whether advertisers can see this data. It only means
that we can not access brand safety ratings on articles from
these websites.
URL SelectionNext, we collect webpages of news ar-
ticles from the 59 target domains. The collaborating pub-
lisher provided a list of around 150 URLs for each of their
four domains. For each of the remaining 55 target domains,
we crawl 100news articles(i.e., not other content such as
home pages or author pages) using Google News. Specifi-
cally, we queried Google News with only the publisher’s
domain name (e.g., cnn.com) and selected the first 100
articles returned. Note that Google News links are click-
through URLs, meaning they redirect to the actual article
pages. The crawler follows these links and extracts the arti-
cle URLs. For this purpose, we develop a JavaScript-based
web crawler using the Playwright automation framework 3
to crawl Google News and retrieve URLs for recent news
3https://github.com/microsoft/playwright

articles on each target domain. To refine our dataset, we ex-
cluded redirects to subscription pages (6 domains that al-
ways redirect to a subscription page were removed) and non-
English websites (2 domains were removed). Thus, 51 of
the original 59 target domains remain, reflecting the filter-
ing steps that were necessary to ensure the availability of
brand safety data on news articles written in English. With
roughly 100 URLs for each of the 47 domains we crawled
and 150 URLs for each of the four domains from our collab-
orating publisher, we have a total of 5,241 article URLs (not
including those that redirect to subscription pages) from 51
domains.
Collecting GPT dataWith the URL data set finalized, we
proceed to the second phase, where we extract theadver-
tising dataembedded on each article’s web page. For this
purpose, we develop a second crawler that visits each arti-
cle’s URL and calls on the Forbes Ad Inspector to collect the
GPT data related to the ads on the web page. Brand safety
data can be stored at different levels: ad-level or page-level.
We collect brand safety data from both levels because differ-
ent providers and publishers choose to store the data differ-
ently. The extracted data are stored locally for further analy-
sis. Due to technical constraints, such as metered paywalls,
CAPTCHAs, broken links, and anti-crawling measures, we
are unable to extract data from every article. As a result, we
successfully retrieve GPT data from 4,352 of the 5,241 arti-
cles that we attempted to visit.
3.3 Data Processing
After data collection, we process the data collected from
4,352 articles to extract brand safety data whenever avail-
able. Brand safety classifications are successfully retrieved
from 3,219 articles. This subset of 3,219 articles from 51
top news domains, constitutes our final dataset for analysis.
All brand safety data are stored in key-value pairs. We
show examples of the collected (Figure 7) and processed
(Figure 8) data in Appendix A. We collaborated with a De-
mand Side Platform (DSP) to get information on how brand
safety data is stored and coded. This allows us to interpret
brand safety data from the three brand safety providers: Or-
acle, IAS, and DV . Now we discuss the process of extracting
brand safety data from each provider.
OracleThe extraction of Oracle brand safety data is the
simplest. There is an overall binary rating for the article (that
is, “safe” or “unsafe”) stored under a key calledm safety.
Oracle also has a list of flags indicating which specific safety
categories (e.g., crime) the article is unsafe for. This list of
flags is stored under a key calledm categories. The ten spe-
cific safety categories considered by Oracle are listed in the
first row of Table 1 under the “Oracle” column. We extract
the overall rating and the list of categories and store them in
two separate variables. If the overall Oracle safety rating ex-
ists, we count the article as having Oracle brand safety data.
In our data collection, there are 74 articles where the Oracle
tag did not load properly and the value is “waiting”. We do
not count these articles in our analysis, leaving us with 1,053
articles that have Oracle brand safety data.
Integral Ad Science (IAS)There are several components
for collecting IAS brand safety data. In total there are 29
safety categories. The 11 safety categories in the first row
of the “IAS” column in Table 1 are binary flags only indi-
cating the presence of the category. These 11 categories are
stored under theias-kwkey. The other 18 safety categories
can take on risk levels. The seven safety categories in the
middle row of the “IAS” column in Table 1 are stored un-
der separate keys. They can take on values of “veryLow”,
“low”, “medium”, or “’high”. The “veryLow” value is the
default value and means the article is safe with respect to
the specific category, and the other values represent varying
levels of risk with regard to the unsafeness of the article. We
extract these seven safety categories and store each as their
own variable. The remaining 11 safety categories (shown in
the last row of the column “IAS” in Table 1) are also stored
under theias-kwkey. These 11 safety categories have risk
levels of low, medium, or high. However, they are different
from the safety categories in the middle row of the “IAS”
column in Table 1 as they have an additional classification
that specifies whether the unsafe content is related to news,
entertainment or video games.
All brand safety values under theias-kwkey are coded
as a 7-digit number with ‘ PG’ appended. We decode these
numbers using our DSP access. Some values stored under
ias-kware just codes for keywords or contextual targeting
categories that do not relate to brand safety, and thus, are re-
moved. We store the list of decoded brand safety categories
for each article in a variable calledias-kw-decoded.
IAS typically does not provide an overall safety rating for
the article. Advertisers need to choose the safety categories
they want to avoid (e.g. terrorism and politics), and check
the safety rating with respect to those categories. For the
purpose of comparison with Oracle and DV , we construct
an overall binary safety rating for each article: if theias-
kw-decodedis empty and all seven of the separately stored
category ratings take on a “veryLow” value, we consider
the article to be rated safe by IAS, otherwise it is rated un-
safe. For one domain (theglobeandmail.com), IAS instead
stores values under theias admantskey. For this publisher,
IAS does not consider specific safety category ratings, but
rates its overall safety (through the presence/absence of a
“brand unsafe” string).
As long as any of the IAS key-value pairs exist, we con-
sider the article to have IAS brand safety data. This results in
1,666 articles with IAS brand safety data. For most articles,
both theias-kwand seven variables in row two of Table 1
are scored. However, 80 articles only haveias-kwdata and
232 articles have theias-kwunscored.
DoubleVerify (DV)The DV brand safety data is stored as
a list of 8-digit codes under theBSCorbsckey. We use our
DSP access to decode these 8-digit codes. We only retain
the codes that are brand safety categories, and we store the
list of decoded categories in the “bsc-decoded” variable. DV
provides both specific category ratings and an overall article
safety rating. If any brand safety category is present, there is
an additional code for the “Any moderate content” category.
There is also a code for “Any severe content”, but we see

Levels Oracle IAS DV
Binary Drugs, Death/Injury, Crime,
Military, Adult, Arms, Terror-
ism, Hate speech, Tobacco,
Obscenity
Politics (negative), Pop
Culture (negative), Animal
Cruelty, Discrimination
Avoidance, Conspiracy The-
ories, Infectious Diseases,
Protests, Misinformation,
Pollution, Smoking, Natural
Disasters
Any Moderate Content, Any
Severe Content, Occult, Gam-
bling, Pharmaceutical (neg-
ative), Financial (negative),
Celebrity Gossip
Low, Medium, High - Adult, Alcohol, Illegal Down-
loadable Material, Drugs,
Hate speech, Offensive Lan-
guage, Violence
Violence, Death/Injury, Drug
Abuse, Crime, Adult/Sex-
ual, Human–made Disaster,
Terrorism, Hate speech/Cy-
berbullying, Alcohol, Natural
Disasters, Vehicle Disasters,
Profanity
Low, Medium, High,
Medium - News,
Medium - Entertainment,
Medium - Video Games
- Death/Injury/Military, Crime,
Sensitive Social Issues, Ter-
rorism, Incitement of Hatred,
Sexual Content, Arms/Ammu-
nition, Cyber Security, Ille-
gal/Recreational Drugs, On-
line Piracy, Obscenities
-
Table 1: Brand Safety Categories for each Provider
this only twice in our dataset. If the “Any moderate content”
code is present, we consider the article to be rated as unsafe.
DV considers 17 safety categories. As shown in the first row
of the “DV” column in Table 1, there are five categories that
are only recorded for presence, and do not have an associ-
ated risk level. The second row lists the remaining 12 safety
categories, where risk ratings are low, medium, or high. As
long as the “BSC” or “bsc” key is not empty, we consider
the article to have been rated by DV for brand safety. This
results in 1,261 articles.
4 Results
Our data allows us to explore brand safety ratings from two
perspectives: overall classifications and specific classifica-
tions by safety categories. Overall classifications categorize
an article as “safe” or “unsafe” on a holistic level. Exploring
brand safety at this level is important because some adver-
tisers choose not to advertise on a web page where content
is rated “unsafe” according to any category. However, it is
also important to analyze brand safety ratings for specific
safety categories (e.g., crime or hate speech) because dif-
ferent brand safety providers consider different categories
to define overall brand safety, and thus their overall brand
safety ratings may not be directly comparable. Next, we
present the results and insights for the overall and specific
category classifications of the 3,219 articles obtained after
processing the data as described in Section 3.3.
4.1 Overall Classifications
The analysis of brand safety ratings for the overall classi-
fication relies on the definitions of safe and unsafe that we
derived for each provider, as discussed in Section 3.3. We
find that 1,416 of the 3,219 articles in our sample (43.99%)
had an unsafe rating from at least one of the brand safety
providers. This indicates that brand safety is having a large
impact on the digital advertising industry. Our findings show
that articles on domains publishing general/breaking news
stories are more likely to be classified as unsafe compared
with domains on specific news topics (52.14% vs. 32.67%).
We also found that some brand safety providers are more
stringent than others and, most importantly, that classifica-
tions are highly inconsistent between providers.
OracleThe 1,053 articles with Oracle brand safety data
are from 16 domains (see Section 3.3). Oracle rates 234
(22.22%) of these articles as unsafe. The breakdown of these
safe and unsafe ratings by domain is shown in Figure 3. We
categorize domains into different categories, such as general,
breaking news, or a specific topic such as business, laws,
politics, etc. The details of labeling a domain into news cat-
egories can be found in Table 3 in Appendix C. There is a big
difference in the percentage of articles rated as “safe” for do-
mains that focus on a special topic (e.g., business/finance or
law) versus general/breaking news. Articles on domains that
focus on a specific topic are rated as safe by Oracle 84.37%
of the time. One domain (realclearpolitics.com) has all safe
ratings, and another four domains, all focusing on a specific
topic, have over 90% safe ratings. On the other hand, only
67.32% of articles on domains in the general/breaking news

category are rated as safe. This may be due to the fact that
breaking news publishers are more likely to publish articles
about inherently unsafe content (e.g., natural disasters, ter-
rorist attacks, or wars). Of the 16 domains with ratings from
Oracle, there is only one domain (telegraph.co.uk, a gen-
eral news website) where safe ratings are in the minority
(46.03%).
Integral Ad Science (IAS)The 1,666 collected articles
with IAS brand safety data are from 31 domains (see Sec-
tion 3.3). IAS rates 895 (53.72%) of these articles as unsafe.
0 20 40 60 80 100
Count
economist.com
euronews.com
msnbc.com
newyorker.com
telegraph.co.uk
theglobeandmail.com
bizjournals.com (B/F)
bloomberg.com (B/F)
cnbc.com (B/F)
forbes.com (B/F)
ft.com (B/F)
law.com (L)
marketwatch.com (B/F)
realclearpolitics.com (P)
vanityfair.com (F)
wired.com (T)
Domain
73
6
67
60
29
39
82
13
17
70
6
80
67
84
56
70
23
4
21
32
34
19
6
6
1
22
1
2
4
37
22
Safe
Unsafe
Figure 3: Oracle ratings by domain
Note: Navy=Breaking/General News, Green=Specific Topic,
B/F=Business/Finance, L=Law, P=Politics, T=Technology,
F=Fashion
0 20 40 60 80
Count
azcentral.com
cnn.com
dailymail.co.uk
dailytelegraph.com.au
desmoinesregister.com
detroitnews.com
dispatch.com
jsonline.com
metro.co.uk
news.com.au
newyorker.com
reuters.com
theglobeandmail.com
theguardian.com
theroot.com
thesun.co.uk
theweek.com
usatoday.com
washingtonpost.com
barrons.com (B/F)
forbes.com (B/F)
hollywoodreporter.com (E)
investors.com (B/F)
jalopnik.com (C)
kotaku.com (E)
marketwatch.com (B/F)
mashable.com (E)
qz.com (B/F)
vanityfair.com (F)
variety.com (E)
wired.com (T)
Domain
5
24
9
8
2
2
6
5
39
42
10
49
24
12
46
45
2
16
16
54
30
41
42
19
16
32
51
37
37
50
5
63
76
1
6
10
6
4
26
49
49
32
41
33
18
34
36
9
60
14
41
33
12
12
5
60
11
55
51
43
Safe
Unsafe
Figure 4: IAS ratings by domain
Note: Navy = Breaking/General News, Green = Specific Topic,
B/F = Business/Finance, E = Entertainment, C = Cars,
T = Technology, F = Fashion
The breakdown of these safe and unsafe ratings by domain is
shown in Figure 4. It is very different from Oracle’s ratings
(see Figure 3) in that there are 16 domains with more arti-
cles rated unsafe than safe by IAS. There is one domain with
only safe ratings (investors.com), but there is also a domain
with only unsafe ratings (dailymail.co.uk). The trend that ar-
ticles from general/breaking news publishers are more likely
to be rated unsafe still holds true for IAS. Articles on spe-
cific news topics domains are rated safe 55.77% of the time,
while articles on general/breaking news domains are rated
safe only 38.27% of the time.
DoubleVerify (DV)The 1,261 articles collected with DV
brand safety data are from 16 domains (see Section 3.3).
DV rated 448 of these articles (35.27%) as unsafe. There
are two domains with over 90% of the articles rated as safe,
both of which specialize in business/finance news. There are
five domains where the majority of articles are rated unsafe,
and four of them are general news domains; the other is
vulture.com, which focuses on entertainment. The domains
that focus on a specific topic have articles classified as safe
77.9% of the time, while the general/breaking news domains
have articles classified as safe only 57.95% of the time.
Comparison between brand safety providersWe find
that in general IAS is most stringent, with the highest per-
centage of articles classified as unsafe, with DV second
highest, and Oracle lowest. This may be due to IAS con-
sidering 29 brand safety categories, while DV and Oracle
consider only 17 and 10, respectively (see Table 1).
Next, we analyze the 672 articles that have multi-
ple providers’ brand safety ratings and compare different
providers’ ratings. There are 329 articles rated by just Or-
acle and IAS, 249 articles rated by just Oracle and DV , 5
articles rated by just IAS and DV , and 89 articles (all on
forbes.com) rated by all three providers. In Figure 6, we use
an UpSet style plot (Lex et al. 2014) to show how each of
these 672 articles is rated for overall safety by the different
providers. The vertical dotted lines separate which providers
are being compared in each section (e.g., the first section
compares Oracle and IAS). Blue bars indicate agreement be-
0 20 40 60 80 100
Count
buzzfeed.com
economist.com
euronews.com
huffpost.com
nymag.com
nytimes.com
telegraph.co.uk
theatlantic.com
thedailybeast.com
time.com
vox.com
bizjournals.com (B/F)
bloomberg.com (B/F)
businessinsider.com (B/F)
forbes.com (B/F)
vulture.com (E)
Domain
53
77
2
55
58
47
21
39
50
47
43
89
64
57
69
42
32
18
1
35
23
49
24
42
42
37
54
1
3
16
28
43
Safe
Unsafe
Figure 5: DV ratings by domain
Note: Navy = Breaking/General News, Green = Specific Topic,
B/F = Business/Finance, E = Entertainment

tween providers, while red bars indicate disagreement. In to-
tal there is disagreement in 22.98% of the 583 articles with
ratings from only two providers. There is even higher dis-
agreement when all three providers generate ratings: 41.57%
of the 89 articles.
The first four bars in Figure 6 break down (dis)agreements
between Oracle and IAS on 329 articles rated by just these
two providers. Disagreement is high (29.79%). Such dis-
agreements are not just due to different levels of tolerance
for “unsafe” content. Across the entire dataset, IAS rates ar-
ticles as unsafe at the highest rate, and Oracle at the lowest
rate. However, there are 21 articles rated safe by IAS and un-
safe by Oracle (including 1 article rated unsafe by all three
providers). Furthermore, we calculated Krippendorff’s alpha
(α) to demonstrate the poor agreement between providers.
Calculating interrater reliability is a more accurate measure
of inconsistency than raw percentages because it accounts
for agreement by chance. This is particularly important in
our dataset where safe classifications are more likely than
unsafe classifications. IAS and Oracle had an interrater reli-
ability of only 0.42, far below the recommended threshold
of 0.8, and even below the absolute minimum acceptable
threshold of 0.67 for ratings that are only used for tentative
conclusions (Krippendorff 2004).
The second set of four bars in Figure 6 break down the
(dis)agreements on 249 articles rated by just Oracle and DV .
Disagreement is lower (14.06%), but this is partially due to
both providers rating the majority of articles as safe. This
indicates potential agreement by chance. The interrater re-
liability is higher than any other pairing of brand safety
providers (α= 0.53), but is still far below the recommended
and minimum thresholds of 0.8 and 0.67, respectively.
The third section of bars in Figure 6 break down the
(dis)agreements on the five articles rated by just IAS and
DV . There are so few articles because IAS and DV are only
both present on 94 forbes.com articles in our sample and
MOAT also rates 89 of these articles (shown in the final sec-
tion of bars in Figure 6). Across all 94 articles rated by IAS
and DV , the disagreement is high (37.23%) and the interrater
reliability is very low (α= 0.19).
Classifications of the 89 articles rated by all three
providers is shown in the final section of Figure 6. Disagree-
ment between the three providers is high (41.57%), and the
interrater reliability is low (α= 0.35).
Oracle Safe
DV Safe
IAS Safe
IAS Unsafe
Oracle Unsafe
DV Unsafe
0250
476
270
217
206
191
73
0
50
100
150Frequency
143
88 78
20
177
37
26
9 2 2 1 0
41
11 15 10 0 3 1 8
Figure 6: Brand Safety Disagreements
4.2 Specific Classifications
The results from Section 4.1 show the inconsistency of brand
safety tools in assessing the overall safety of an article. How-
ever, this inconsistency can be partially explained by varia-
tion in the number and nature of safety categories assessed
by each provider. Additionally, some advertisers may only
block a few specific brand safety categories, and do not care
about the overall safety rating. For example, a beer com-
pany may care specifically about not advertising on news ar-
ticles about alcoholism, alcohol abuse, drug abuse, or drunk
driving accidents, and set up brand safety filters accordingly.
Thus, in this section, we examine the inconsistency in brand
safety classifications with respect to a particular safety cat-
egory. A descriptive analysis of which safety categories are
most frequently occurring under each provider in our dataset
is presented in Appendix B.
Comparison between brand safety providersEach
provider considers different safety categories and different
risk levels (see Table 1). To compare the providers, we iden-
tify several brand safety categories that exist in the list of
at least two brand safety providers (regardless of risk level).
We make these pairings conservatively, and only pair cate-
gories from different providers when the category is not am-
biguous. For example, we donotpair the “Drugs” category
for IAS with the “Drug Abuse” category from DV because
drug abuse content is more severe than drug-related con-
tent. We do, however, allow for combining two categories
under one brand safety provider to make a match. For ex-
ample, IAS has a “Death, Injury or Military Conflict” cate-
gory. While Oracle does not have this exact category, it does
have “Military” and “Death & Injury” categories. We com-
bine these two categories for Oracle to allow comparison
with IAS. The full list of pairings is displayed in Table 2.
For each safety category listed, we can tell which providers
are compared from the “Oracle”, “IAS”, and “DV” columns.
The “T” values indicate which provider is being compared
for the specific category.
After identifying the set of safety categories supported by
all brand safety providers, we compare their respective clas-
sification outcomes for each shared category. For each cate-
gory, we locate all articles with ratings from both providers
and compute interrater reliability using Krippendorff’s alpha
(see “α” in Table 2). For interpretability, we also compute
the inconsistency as a percentage. The majority of articles
are not related to any given category and thus providers are
in agreement by default. Therefore, we only consider articles
with at least one unsafe rating when reporting disagreement
as a percentage.
Since there is no risk level provided for many safety cat-
egories, we consider two providers to agree when they both
rate the article as unsafe for the target category, irrespective
of risk level (e.g., if one provider rates unsafe with low risk
and the other rates unsafe with high risk, we consider them
in agreement). Thus, we are making a conservative estimate
of the inconsistency between brand safety tools. While this
analysis does not always enable us to reveal the provider that
misclassified the article, manual evaluation of some articles
shows that all providers are inaccurate in some cases.

Category Oracle IAS DV Inconsistencies α
Arms/Ammunitions T T F 6/9 (66.67%) 0.49
Drugs T T F 8/9 (88.9%) 0.19
Adult T T F 14/23 (60.87%) 0.54
Adult/Sexual* F T T 6/9 (66.7%) 0.47
Natural Disasters F T T 1/1 (100%) 0.0
Terrorism T T T 2/3 (66.67%) 0.66
Terrorism T T F 12/18 (66.67%) 0.48
Terrorism T F T 5/12 (41.67%) 0.73
Terrorism F T T 2/3 (66.67%) 0.49
Crime T T T 5/7 (71.43%) 0.56
Crime T T F 37/61 (60.66%) 0.50
Crime T F T 22/41 (53.66%) 0.6
Crime F T T 3/7 (42.86%) 0.7
Death/Injury T F T 24/42 (57.14%) 0.56
Death/Injury/Military* T T F 35/63 (55.56%) 0.55
Hate speech T T F 27/31 (87.10%) 0.19
Violence F T T 19/26 (73.08%) 0.31
Alcohol F T T 1/2 (50%) 0.66
Obscenities T T F 2/2 (100%) 0.00
Total - - - 231/369 (62.60%) -
- T T F 141/216 (65.28%) 0.37
- T F T 51/95 (53.68%) 0.63
- F T T 32/48 (66.67%) 0.44
- T T T 7/10 (70%) 0.61
Table 2: Comparing Brand Safety Ratings for Specific
Categories
Note: * means two categories were combined
In total, there are 231 inconsistencies on 369 instances
(62.60%). There is an inconsistency on 7 of the 10 instances
with a rating from all three providers. The average inter-
rater reliability across all comparable categories for the three
providers (α=0.53) and each pair of providers is always be-
low the minimum threshold of 0.67. The highest average
agreement (α=0.63) is between Oracle and DV , which can
be compared for three categories. The lowest average inter-
rater reliability (α=0.37) is between IAS and Oracle, which
can be compared across eight categories.
Digging in deeper, Table 2 shows 141 disagreements be-
tween IAS and Oracle, 65.28% of all 216 instances where
IAS and Oracle can be compared. There were 75 times
where only Oracle flagged the category as unsafe, and 66
times only IAS flagged a category unsafe, with 39 times be-
ing low risk, 26 times being medium risk, and once being
high risk. In the most egregious example, where IAS rated
an article as high risk for drug content while Oracle rated it
as safe, it appears IAS is at fault because the article covers an
update to the Samsung Galaxy phones. Our manual inspec-
tion of this article revealed no reason for this. As an example
where Oracle is at fault, an article inThe New Yorkerabout
“Black Identity” is labeled by Oracle as being unsafe and
related to crime.
Table 2 shows 51 instances of an inconsistency between
Oracle and DV ratings, 53.68% of the 95 instances that Or-
acle and DV can be compared. Most disagreements are due
to Oracle being more stringent, flagging a category as un-
safe when DV rates it as safe (41 times). As an example,
an article about the Hezbollah pager explosions cites 9 dead
and 2,750 injured, yet DV does not rate the article unsafe for
“Death & Injury”.
Finally, there are 32 cases of disagreement between IAS
and DV , 66.67% of the 48 instances that can be compared.
IAS is a more stringent provider, flagging 26 out of the 32 in-
stances as unsafe with a risk level of low 13 different times,
medium 11 times, and high twice. For the other 6 disagree-
ments (where DV rates the article as unsafe and IAS does
not), DV rates the risk level as low once and medium five
times.
We can also look at the two safety categories (Terror-
ism and Crime) in Table 2 where all three brand safety
providers can be compared. For “Terrorism”, there are only
three articles for comparison and two are disagreements. For
“Crime”, there are seven articles for comparison, and five
have a disagreement. In three of the disagreements only Or-
acle rates the content as unsafe.
Comparison among safety categoriesWe further ana-
lyze the inconsistencies across different safety categories, as
shown in Table 2. The interrater reliability for all specific
categories falls below the recommended reliability threshold
of 0.8, but there are two instances (IAS and DV rating crime,
and Oracle and DV rating terrorism) where the interrater re-
liability exceeds the minimum acceptable threshold of 0.67.
The remaining 17 categories have interrater reliability scores
that signal unreliable ratings, which may indicate that the
corresponding safety category is harder to classify. Under
this assumption, our results illustrate which safety categories
need more concrete definitions in an updated framework
of brand safety. Brand safety providers should also priori-
tize improving classification accuracy within the safety cat-
egories with a higher level of inconsistency.
Comparisons within brand safety providersWe also ex-
amine the consistency of behavior within a brand safety
provider. For IAS, sometimes the category ratings are in con-
flict with each other. For example, there are separate “Adult”
and “Sexual Content”safety categories, and we expect these
two categories to have similar ratings. There are 179 arti-
cles where both categories are considered and at least one of
them has a low, medium, or high risk rating. Of those 179
articles, there are:
• 12 articles where both categories are rated unsafe with
the same risk level.
• 12 articles where both categories are rated as unsafe, but
with different risk levels.
• 155 articles where one category is safe and one is unsafe.
We consider some of these inconsistencies to be extreme.
For example there are 36 articles where one category is rated
as safe and the other is unsafe with a risk level higher than
low (35 with medium risk and 1 with high risk). Looking
into these 36 articles, we find that 12 of them discuss sexual
assault, sex trafficking, or rape, and yet have a safe rating
for either “Adult” or “Sexual content”. In contrast, there is
also an article about the construction plans for a highway in
Arizona classified as medium risk for adult content.
There is a similar trend occurring for the “Drugs” and “Il-
legal and Recreational Drugs” categories. There are 46 arti-
cles where both safety categories are considered and at least

one of the two drug-related categories has a low, medium,
or high risk rating. There are only two articles where both
categories have an unsafe rating, and the risk levels for the
two categories are not the same in either case. For the other
44 articles, there are 33 times where “Illegal and Recre-
ational Drugs” is rated as safe and “Drugs” is not (30 low
risk, 2 medium risk, 1 high risk). There are 11 articles
where “Drugs” is rated as safe and “Illegal and Recreational
Drugs” is not (all medium risk). Looking at the 14 articles
with medium or high risk we again find that some of these ar-
ticles are not ambiguous. Three of the articles mention hard
drugs such as ketamine or ecstasy, and one of the articles
is the aforementioned article about Samsung Galaxy phones
that is rated high risk for drug content.
For DV , the aggregate category for severe content is
present each time that there is high risk for alcohol or pro-
fanity (one of their occurrences is on the same article). How-
ever, DV does not classify the seven articles with high risk
for “Adult & Sexual” content as “severe content”. It is un-
clear why being rated as unsafe with high risk for some cate-
gories and not for others would classify an article as “severe
content”.
5 Discussion
Issues in Current Digital Advertising Ecosystem.Each
provider approaches brand safety with a different propri-
etary algorithm and set of brand safety categories. Com-
bined with a lack of standardization and regulation, incon-
sistencies occur as expected. These problems are not limited
to breaking news media. Our data show that inconsistency
extends across many different categories such as entertain-
ment, health, and finance. Inconsistent ratings are especially
harmful to publishers as they can not reliably figure out how
to prevent unsafe classifications, nor the resulting decline in
advertising revenue. Advertisers can mitigate some of the
harms of inconsistent ratings by relying on a single provider
(publishers do not have this choice); however, we also find
inconsistency within the ratings of a single provider.
We also manually identified instances of clearly incorrect
brand safety ratings. These misclassifications carry serious
consequences: advertisers risk damaging their brand when
their ads are served next to harmful content misclassified
as safe, and publishers lose revenue when valuable, con-
textually appropriate content is mislabeled as unsafe. The
consequences of misclassification in content moderation are
complex, and prior research has shown that such misclassi-
fications typically harm marginalized groups disproportion-
ately (Kingsley et al. 2022; Oliva, Antonialli, and Gomes
2021; Gomez et al. 2024; Harris et al. 2023). This makes the
fact that an article about “Black Identity” was labeled as un-
safe and related to crime in our dataset unsettling. Although
we did not have enough relevant articles to draw concrete
conclusions, future research should investigate this potential
problem more thoroughly.
Call for Industry Standardization and Academic Re-
search.While our findings point to serious flaws in the
current digital advertising landscape, advertisers still value
safely-aligned ad placements, and publishers need moneti-
zation tools that protect brand integrity without sacrificing
legitimate content.
Our findings call for a standardized, transparent frame-
work for brand safety classification, which is essential for
ensuring consistency, accuracy, and trust for a sustainable
digital advertising ecosystem on the open web. This frame-
work should include:
• Clear definitions of safety categories, with concrete ex-
amples of what constitutes risks at different levels,
• Auditable classification processes, where providers agree
to regular third-party evaluations in exchange for indus-
try accreditation,
• An appeal mechanism for publishers to contest misclas-
sifications,
• A public benchmark dataset, grounded in human-labeled
brand safety ratings, to evaluate accuracy and bias across
tools,
• Explainable classifications (i.e., a rationale for why con-
tent was rated safe/unsafe should be provided).
While brand safety providers may initially resist such
measures, advertisers and publishers, who ultimately fund
these tools, hold the leverage. If they collectively demand
compliance with a standardized framework, non-compliant
brand safety providers may be pushed out of the market.
Importantly, such a system would still allow differentiation:
providers could offer better classification quality and addi-
tional features such as specialized categories, fine-grained
risk levels, or dynamic pricing models.
Our study advances academic and technical discourse on
content classification and calls for deeper engagement from
the Web, natural language processing, and machine learning
communities to build culturally sensitive, explainable brand
safety models, an urgent need amid increasing regulatory
scrutiny (Barwick 2024).
Limitations of the Study.While our study presents valu-
able findings of inconsistencies in brand safety classification
among leading providers, several methodological and con-
ceptual limitations should be noted.
Although our analysis is limited to English-language
news articles, the brand safety systems we evaluate are
not confined to this domain. These tools are widely de-
ployed across international markets and are applied to vari-
ous formats, including video, podcasts, and user-generated
content. Consequently, the methodological concerns we
identify—classification inconsistency and the absence of
ground-truth benchmarking—are likely to extend beyond
our dataset and may affect brand safety assessments across
languages, formats, and cultural contexts. Investigating how
classification systems perform across these diverse types of
media would provide a more comprehensive understanding
of brand safety practices in the digital ecosystem.
Second, our primary analytical focus is on classifica-
tion inconsistencies between brand safety providers rather
than classification accuracy. This is due to the absence of
a ground-truth dataset of brand safety labels against which
we could benchmark provider’s output. Without indepen-
dent, human-verified assessments of content safety, we can-

not definitively determine whether any given provider’s clas-
sification is correct or incorrect. We call for future research
to develop such a benchmark using human expert annota-
tion. Developing a human-annotated benchmark to evalu-
ate the accuracy of brand safety classifications remains an
important avenue for future work, and we are actively ex-
ploring best practices for designing such a dataset in con-
sultation with industry providers. Recent work indicates that
carefully calibrated moderation interventions can steer users
away from extremist movements (Russo et al. 2025), high-
lighting the broader social implications of reliable classifi-
cation of safe content.
Third, our dataset only includes webpages for which their
publishers choose to collect brand safety data from the
providers. This introduces a potential selection bias. Con-
sequently, our findings on the proportion of articles labeled
unsafe may be influenced by publishers’ self-selection, po-
tentially skewing our understanding of the overall coverage
of brand safety. Our analysis assumes that the publisher’s
decision to collect brand safety data is independent of the
safety classification provided by a brand safety provider, a
conceptual constraint that we acknowledge and plan to test
in future research.
6 Conclusions and Future Work
This paper presented an empirical analysis of brand safety
classifications from three industry leading providers, Dou-
bleVerify (DV), Integral Ad Science (IAS), and Oracle. Our
findings show that brand safety has a large effect on the dig-
ital advertising industry as there was an unsafe rating from
at least one provider on 43.99% of the articles in our dataset
(including 52.14% of general/breaking news articles). The
frequency of unsafe ratings is not a problem in itself, but
the lack of standardization and consistency in the ratings is.
We found inconsistent classifications between two providers
in both overall safety assessments (22.98%) and individual
risk categories (62.40% of the time where at least one un-
safe rating is present). Low interrater reliabilities, as mea-
sured by Krippendorff’s alpha, indicate that both the overall
safety, as well as the specific category-level, ratings from
brand safety providers are unreliable. These inconsistencies
are not isolated anomalies, but indicate deeper issues stem-
ming from inherent technical challenges, proprietary algo-
rithms and varying interpretations of what constitutes “un-
safe” content. Finally, we showed that IAS sometimes pro-
duces internally inconsistent ratings. For instance, there are
46 articles where IAS rated as safe for the ‘Drugs’ category
but as unsafe for the ‘Illegal and Recreational Drugs’ cate-
gory, or vice versa.
Such inconsistencies carry serious consequences and un-
dermine the trust in brand safety technologies that are central
to the operation of the digital advertising ecosystem. If pub-
lishers and advertisers cannot correctly identify unsafe con-
tent, publishers cannot mitigate the revenue losses associ-
ated with content that is classified as unsafe, and advertisers
may reduce their digital advertising budget to protect their
brand’s reputation. Furthermore, some inconsistencies are
due to blatant misclassifications, which directly harm pub-
lishers’ revenues when safe content is incorrectly flagged
as unsafe, and advertisers’ reputations when their ads are
shown next to unsafe content that is misclassified.
Although our dataset is primarily made up of English-
language web articles, the issues that we have identified
of inconsistent classification of safe content both within
and between providers are fundamental to inherent techni-
cal challenges in classification and lack of standardization.
Therefore, we believe that our results are broadly generaliz-
able across different content, geographies and media types.
To address these issues, we advocate for the implemen-
tation of a standardized, transparent, explainable, and au-
ditable brand safety framework. Such a framework would
include clearly defined safety categories, routine third-party
audits, explainable classifications, and an appeal process for
misclassified content. By adopting a shared protocol, the in-
dustry can move toward more reliable and fair evaluations
that serve the interests of advertisers and publishers.
Our findings also raise important areas for future research.
Content safety classification poses inherent technical chal-
lenges to natural language understanding. The necessity of
evaluating words in their context (e.g., “shoot” has differ-
ent meanings in a sports article versus a breaking news story
about a violent criminal) lends itself well to large language
models. However, open research questions remain about
how to effectively handle hierarchical classification (e.g.,
assigning low, medium, or high risk levels to certain cate-
gories), mitigate potential biases against specific dialects or
writing styles, and generate explanations for each classifica-
tion that are both faithful and plausible.
Acknowledgements
This work was supported by the NSF under Grants No. CNS
2237328 and DGE 2043104, as well as by the Martin Tuch-
man’62 Chair Endowment and the Leir Foundation. Chat-
GPT and Writefull were utilized to refine some sentences
for clarity, grammar, spelling, and punctuation.
References
Ball-Burack, A.; Lee, M. S. A.; Cobbe, J.; and Singh, J.
2021. Differential Tweetment: Mitigating Racial Dialect
Bias in Harmful Tweet Detection. InProceedings of the
2021 ACM Conference on Fairness, Accountability, and
Transparency.
Barwick, R. 2024. DOJ, NCIS ask ad executives
about brand-safety companies.Marketing Brew.
https://www.marketingbrew.com/stories/2024/10/11/doj-
ncis-brand-safety-google-integral-ad-science-doubleverify.
Bellman, S.; Abdelmoety, Z. H. S.; Murphy, J.; Arismendez,
S.; and Varan, D. 2018. Brand Safety: The Effects of Con-
troversial Video Content on Pre-Roll Advertising.Heliyon,
4(12).
Bishop, S. 2021. Influencer Management Tools: Algorith-
mic Cultures, Brand Safety, and Bias.Social Media + Soci-
ety, 7(1): 1–13.
Business Insider. 2024. DoubleVerify and Integral Ad
Science face fresh scrutiny from brand safety watchdogs.
https://www.businessinsider.com/doubleverify-integral-ad-
science-face-fresh-brand-safety-scrutiny-2024-6.

CHEQ. 2020. The Economic Cost of Keyword Blacklists
for Online Publishers. Technical report, University of Balti-
more.
Elmore, J. 2024. Who are DoubleVerify Competitors: A
Closer Look at the Top Contenders.TheTechyLife. https:
//thetechylife.com/who-are-doubleverify-competitors/.
Gollasch, G. 2024. WFA makes ‘difficult decision’
to discontinue GARM following X lawsuit.Market-
ing Week. https://www.marketingweek.com/wfa-suspend-
garm-x-lawsuit/.
Gomez, J. F.; Machado, C.; Paes, L. M.; and Calmon, F.
2024. Algorithmic Arbitrariness in Content Moderation. In
The 2024 ACM Conference on Fairness, Accountability, and
Transparency.
Griffin, R. 2023. From Brand Safety to Suitability: Advertis-
ers in Platform Governance.Internet Policy Review, 12(3).
Harris, C.; Johnson, A. G.; Palmer, S.; Yang, D.; and Bruck-
man, A. 2023. ‘Honestly, I Think TikTok Has a Vendetta
Against Black Creators’: Understanding Black Content Cre-
ator Experiences on TikTok. InProceedings of the ACM
Human-Computer Interaction.
Hemmings, M. 2021. Ethical Online Advertising: Choosing
the Right Tools for Online Brand Safety.Journal of Brand
Strategy, 10(2): 109–120.
Jin, X.; Wang, Y .; and Tan, X. 2019. Pornographic Image
Recognition via Weighted Multiple Instance Learning.IEEE
Transactions on Cybernetics, 49(12): 4412–4420.
Johnson, R. W.; V oorhees, C.; and Khodakarami, F. 2023.
Is Your Brand Protected? Assessing Brand Safety Risks in
Digital Campaigns.Journal of Advertising Research, 63(3):
205–221.
Kingsley, S.; Sinha, P.; Wang, C.; Eslami, M.; and Hong, J. I.
2022. “Give Everybody [..] a Little Bit More Equity”: Con-
tent Creator Perspectives and Responses to the Algorithmic
Demonetization of Content Associated with Disadvantaged
Groups.Proceedings of the ACM on Human-Computer In-
teraction, 6: 1–37.
Kint, J. 2025. Facts: Google’s push to AI hurts publisher
traffic. InDigital Content Next.
Krippendorff, K. 2004. Reliability in content analysis: Some
common misconceptions and recommendations.Human
communication research, 30(3): 411–433.
Kumar, D.; AbuHashem, Y .; and Durumeric, Z. 2024. Watch
Your Language: Investigating Content Moderation with
Large Language Models.Proceedings of the 18th Interna-
tional AAAI Conference on Web and Social Media.
Le Pochat, V .; Van Goethem, T.; Tajalizadehkhoob, M.,
Samaneh Korczy ´nski; and Joosen, W. 2019. Tranco: A
Research-Oriented Top Sites Ranking Hardened Against
Manipulation. InProceedings of the 26th Annual Network
and Distributed System Security Symposium, NDSS 2019.
Lee, C.; Kim, J.; and Lim, J. S. 2021. Spillover Effects of
Brand Safety Violations in Social Media.Journal of Current
Issues & Research in Advertising, 42(4): 354–371.
Lex, A.; Gehlenborg, N.; Strobelt, H.; Vuillemot, R.; and
Pfister, H. 2014. UpSet: visualization of intersecting sets.
IEEE transactions on visualization and computer graphics,
20(12): 1983–1992.
Lyu, Y .; Cai, J.; Callis, A.; Cotter, K.; and Carroll, J. M.
2024. ‘I Got Flagged for Supposed Bullying, Even Though
It Was in Response to Someone Harassing Me About My
Disability.’: A Study of Blind TikTokers’ Content Modera-
tion Experiences. InProceedings of the CHI Conference on
Human Factors in Computing Systems.
Marvin, G.; and Meisel, S. 2018. Protecting the brand in the
era of fake news: Why brands need advertisement verifica-
tion tools.Journal of Digital & Social Media Marketing,
5(4): 322–331.
MRC. 2018. MRC Supplement to IAB Guide-
lines for the Conduct of Ad Verification: En-
hanced Content Level Context and Brand Safety.
https://www.mediaratingcouncil.org/sites/default/files/
Standards/MRC%20Ad%20Verification%20Supplement-
%20Enhanced%20Content%20Level%20Context%
20and%20Brand%20Safety%20%28Final%29.pdf.
Oliva, T. D.; Antonialli, D. M.; and Gomes, A. 2021. Fight-
ing Hate Speech, Silencing Drag Queens? Artificial Intelli-
gence in Content Moderation and Risks to LGBTQ V oices
Online.Sexuality & Culture.
Ou, X.; Ling, H.; Yu, H.; Li, P.; Zou, F.; and Liu, S. 2017.
Adult Image and Video Recognition by a Deep Multicontext
Network and Fine-to-Coarse Strategy.ACM Transactions on
Intelligent Systems and Technology, 8(5): 1–25.
Pisharody, N.; Norton, S.; Greene, K.; and Shapiro, J. 2025.
Changes in YouTube’s Content Moderation Policy Had Lit-
tle Detectable Impact on Election Denial Content.Proceed-
ings of the 19th International AAAI Conference on Web and
Social Media.
Reed, B. 2017. Google’s bad week: YouTube loses
millions as advertising row reaches US.The Guardian.
https://www.theguardian.com/technology/2017/mar/25/
google-youtube-advertising-extremist-content-att-verizon.
Russo, G.; Styczen, M.; Horta Ribeiro, M.; and West, R.
2025. Does Content Moderation Lead Users Away from
Fringe Movements? Evidence from a Recovery Commu-
nity. InProceedings of the International AAAI Conference
on Web and Social Media, volume 19, 1719–1734.
Samory, M. 2021. On Positive Moderation Decisions. In
Proceedings of the International AAAI Conference on Web
and Social Media, volume 15, 585–596.
Vaccaro, K.; Xiao, Z.; Hamilton, K.; and Karahalios, K.
2021. Contestability for Content Moderation. InProceed-
ings of the ACM on Human-Computer Interaction.
Vargo, C. J.; Hopp, T.; and Agarwal, P. 2024. Balancing
Brand Safety and User Engagement in a Two-Sided Market:
An Analysis of Content Monetization on Reddit.Journal of
Current Issues & Research in Advertising, 45(2), 242–256.
V o, Q. M.; Cao, N. T.; and Ton-That, A. H. 2020. Unsafe Im-
age Classification Using Convolutional Neural Network for
Brand Safety. InProceedings of the Asia-Pacific Conference
on Computer Science and Data Engineering. IEEE.

von Hohenberg, C.; Menchen-Trevino, B.; Casas, E.; and
Wojcieszak, M. 2021. A list of over 5000 US news do-
mains and their social media accounts. https://doi.org/10.
5281/zenodo.5681483.
Wang, X.; Cheng, F.; Sun, H.; Liu, G.; and Zhou, C. 2018.
Adult Image Classification by a Local-Context Aware Net-
work. InProceedings of the 2018 25th IEEE International
Conference on Image Processing (ICIP). IEEE.
Appendix
A Examples of Collected and Processed Data
Figures 6 and 7 provide illustrative examples of the brand
safety datasets referenced in our study. Figure 6 displays the
original GPT-generated classifications for IAS, while Figure
7 shows the corresponding processed format prepared for
analysis.
Figure 7: Example of Collected GPT Brand Safety Data for
IAS
B Frequency of Specific Brand Safety
Categories
Given we could not find any previous works that collected
brand safety data for news articles, we feel there is some
benefit in presenting descriptive results. For example, we
showed that articles on breaking/general news websites are
more likely to be rated as unsafe than articles from domains
which focus on a specific topic (e.g., business). For this same
reason, we want to present the specific content categories
which are most likely to be rated as unsafe on news articles.
These results are not important to our main analysis, thus we
present them here in the Appendix.
B.1 Oracle
Oracle has the simplest specific classifications system of the
three providers. There are only 10 categories, as shown in
Table 1. Classification into each category is only binary,
and there are no risk levels. The frequency with which each
of these 10 categories is found in the 234 articles classified
as unsafe by Oracle are visualized in Figure 9. The “Crime”
and “Death & Injury” columns are by far the most common,
with 120 and 118 occurrences, respectively.
Adult Crime
Terrorism
Death & Injury
Drugs
Obscenity
Hate speech
Arms
Military Tobacco
Category
0
20
40
60
80
100
120Frequency
22
120
26
118
6 3 9
35
44
2
Figure 9: Oracle Specific Classifications
100 101 102
Count
Animal Cruelty
Conspiracy Theories
Discrimination Avoidance
Infectious Diseases & Outbreaks
Misinformation
Natural Disasters
Politics
Pollution
Pop Culture
Protests & Demonstrations
Smoking
Adult
Alcohol
Drugs
Hate Speech
Illegal Downloads
Offensive Language
Violence
Arms and Ammunition
Crime
Cyber Security
Death, Injury or Military Conflict
Illegal and Recreational Drugs
Incitement of Hatred
Obscenities
Online Piracy
Sensitive Social Issues
Sexual Content
Terrorism
Category
2
7
19
21
6
34
186
5
51
17
1
135
48
5
31
2
3
38
2
3
108
22
4
153
12
314
119
53
1
11
2
4
127
4
6
6
13
198
14
33
10
1
1
1
76
3
2
21
9
6
39
Risk Group
High Risk
Medium Risk
Low Risk
Present
Figure 10: IAS Specific Classifications

Article ID Domain URL m_safety m_categories adt alc dlm drg hat off vio ias-kw ias_admants BSC
1 bloomberg.com unsafe
['gv_death_injury'
, 'moat_unsafe',
'gv_military']
['84132004',
'80000200’, …]
2 forbes.com safe [‘moat_safe’] veryLow veryLow low high veryLow veryLow veryLow [‘IAS_3006647_PG’, ‘IAS_3005123_PG’, ….] ['84122001', '80023001’, ….]
3 cnn.com medium veryLow veryLow veryLow low veryLow low
['IAS_13149_KW’,
'IAS_1509973_PG’, …]
4. theglobeandmail.com unsafe
['gv_arms',
'moat_unsafe',
'gv_death_injury']
['S_9345',
'S_6900’,…..]
Figure 8: Example of Processed Brand Safety Data
B.2 Integral Ad Science (IAS)
The IAS specific content category classification system is
the most complex of the three providers as described in Sec-
tion 3.3. We show the frequency of all 29 IAS categories in
the 895 articles rated as unsafe by IAS in Figure 10. Note
that we do not consider the additional “News”, “Entertain-
ment”, or “Video Gaming” tags and just plot each category
according to risk level. We do separately show the frequency
of the additional “News”, “Entertainment”, or “Video Gam-
ing” tags in Figure 11.
Of the binary categories which are only measured for
presence, Figure 10 shows that “Politics” is by far the most
common with 186 occurrences. For the categories allowing a
risk level to be assigned, categories with over 100 total clas-
sifications include “Adult”, “Hate speech”, “Offensive Lan-
guage”, “Violence”, “Crime”, and “Death, Injury, or Mili-
tary Conflict”. There are some similarities to Oracle, where
“Crime” and “Death & Injury” were the two most common
categories. However, “Adult” and “Hate Speech” were not
very common in the Oracle classifications. Of the 18 cate-
gories with a risk level assigned, we find that “High Risk”
is rarely used. The one exception is that 53 articles are rated
as high risk with respect to the “Violence” category. There
are only 30 high risk ratings among the other 17 categories
combined.
B.3 DoubleVerify (DV)
We collected data on 19 specific categories as described in
Section 3.3. We chart the frequency of all 19 categories in
Figure 12. Similar to Oracle, the “Crime” and “Death &
Injury” are among the most common categories, with over
100 occurrences each. Similar to IAS, the “Violence” cate-
gory is very common with 178 occurrences. The only other
category with over 100 total occurrences is the “Celebrity
Gossip” category (which does not exist under the other clas-
sification systems). DV rarely rates content as unsafe with
“High Risk” as it only occurs 10 times in total (7 for “Adult
& Sexual”, 2 for “Profanity” and, 1 for “Alcohol”). Oddly,
the “Low Risk” level is also not found frequently. It is only
used 90 times, which is quite low when considering that
the “Medium Risk” level is found 662 times across all cate-
100 101 102
Count
Arms and Ammunition
Crime
Cyber Security
Death, Injury or Military Conflict
Illegal and Recreational Drugs
Incitement of Hatred
Obscenities
Online Piracy
Sensitive Social Issues
Sexual Content
Terrorism
Category
13
12
2
2
131
105
22
5
6
5
1
198
149
22
1
14
7
3
33
26
5
11
7
5
1
1
1
79
70
4
3
30
22
14
9
39
38
1
Risk Group
Total
News
Entertainment
Video Games
Figure 11: IAS Specific Classifications with News,
Entertainment, and Video Gaming Tags
gories.
C Appendix: Categorization of Domains
We classify each domain in our sample into a category of
news so we can see if patterns exist in the classifications of
similar domains. We take a simple approach to classifying
each domain. We search for the website on Google and then
record the blurb that is generated to describe the website. For
each domain, we have copied that text (or a portion of that
text) into the “Description” column of Table 3. For a few
domains, there is no generated blurb. For these domains, we
visit the about page on the website and copy the description
from there. These domains are marked with an asterisk in
Table 3.

100 101 102
Count
All Moderate Content
All Severe Content
Celebrity Gossip
Gambling
Negative News: Financial
Negative News: Pharmaceutical
Occult
Adult & Sexual
Alcohol
Crime
Death & Injuries
Drug Abuse
Hate Speech & Cyberbullying
Human-made Disasters
Natural Disasters
Profanity
Terrorism
Vehicle Disasters
Violence
Category
448
2
125
2
19
3
3
12
53
7
10
10
1
17
176
21
97
3
14
2
26
4
49
3
18
1
11
2
2
36
3
6
12
166
Risk Group
High Risk
Medium Risk
Low Risk
Present
Figure 12: DV Specific Classifications
Once obtaining the descriptions, we can easily clas-
sify each domain. Any description that contains the words
“breaking... news” is classified into the “Breaking News”
category. If the description states it is the online format for
a newspaper (e.g., azcentral.com) or if the descriptions state
their focus as news for a specific global or local market (e.g.,
cnn.com or jsonline.com), then we classify them as “General
News”. Any domain that has a description with a long list
of unrelated topics covered (e.g., theatlantic.com or usato-
day.com) is also classified as “General News”. In the main
results section we combine domains which are classified as
“Breaking News” or “General News” into one category be-
cause we see that the content on these domains is very simi-
lar. Domains with a description that clearly states their focus
is in one area (e.g., wired.com and jalopnik.com) are classi-
fied into a category that is named to align with that focus
(e.g., “Technology” and “Cars”). For most of these domains
which focus on a specific area, they are in a category of
their own. The exceptions are the ten domains in the “Fi-
nance/Business” category and the five domains in the “En-
tertainment” category. We merge the business and finance
focused domains because there are several which would
fall under both categories anyway (e.g., bloomberg.com and
cnbc.com). The domains classified as “Entertainment” ei-
ther explicitly state that they focus on entertainment news
(e.g. variety.com), or we consider their focus to be purely
for entertainment (e.g. kotaku.com focuses on video gaming
news).

Domain Description Categorization
azcentral.com The digital home of The Arizona Republic newspaper, with breaking news and
in-depth coverage of sports, things to do, travel and opinions
Breaking News
barrons.com Barron’s is a leading source of financial news Finance/Business
bizjournals.com The Business Journals features local business news from 40-plus cities across
the nation
Finance/Business
bloomberg.com Bloomberg delivers business and markets news, data, analysis, and video to the
world
Finance/Business
businessinsider.com Business Insider tells the global tech, finance, stock market, media, economy,
lifestyle, real estate, AI and innovative stories you want to know
Finance/Business
buzzfeed.com BuzzFeed has breaking news, vital journalism, quizzes, videos, celeb news,
Tasty food videos, recipes, DIY hacks, and all the trending buzz
Breaking News
cnbc.com CNBC is the world leader in business news and real-time financial market cov-
erage
Finance/Business
cnn.com CNN is the world leader in news and information and seeks to inform, engage
and empower the world.
General News
dailymail.co.uk Get the latest breaking news, showbiz & celebrity photos, sport news & rumours,
viral videos and top stories
Breaking News
dailytelegraph.com.au News and Breaking News Headlines Online including Latest News from Aus-
tralia and the World.
Breaking News
desmoinesregister.com The Des Moines Register is the number one source for Des Moines and Iowa
breaking, politics, business, agriculture, Iowa sports and entertainment news.
Breaking News
detroitnews.com Your first source for breaking news, local in-depth reporting, and analysis of
events important to Detroit and Michigan
Breaking News
dispatch.com The Columbus Dispatch is the number one source for Columbus and Ohio break-
ing politics, business, obituaries, Ohio sports and entertainment news.
Breaking News
economist.com Get in-depth global news and analysis. Our coverage spans world politics, busi-
ness, tech, culture and more
General News
euronews.com European and international latest breaking news, economic news, business news
and more.
Breaking News
forbes.com Forbes is a global media company, focusing on business, investing, technology,
entrepreneurship, leadership, and lifestyle.
Finance/Business
ft.com News, analysis and opinion from the Financial Times on the latest in markets,
economics and politics.
Finance/Business
hollywoodreporter.com Movie news, TV news, awards news, lifestyle news, business news and more Entertainment
huffpost.com Read the latest headlines, news stories, and opinion from Politics, Entertainment,
Life, Perspectives, and more.
General News
investors.com Perform stock investment research with our IBD research tools to help invest-
ment strategies.
Finance/Business
jalopnik.com* Jalopnik is a news and opinion website about cars Cars
jsonline.com Milwaukee and Wisconsin news, sports, business, opinion, entertainment,
lifestyle and investigative reporting
General News
kotaku.com Gaming Reviews, News, Tips and More. Entertainment
law.com The premier global source for trusted and timely legal news, analysis and data. Legal News
marketwatch.com MarketWatch provides the latest stock market, financial and business news Finance/Business
mashable.com Mashable is a global, multi-platform media and entertainment company. Entertainment
metro.co.uk Metro.co.uk: News, Sport, Showbiz, Celebrities from Metro. General News
msnbc.com MSNBC breaking news and the latest news for today Breaking News
news.com.au The Latest on the news that matters to you - sport, entertainment, finance and
politics.
General News
newyorker.com The New Yorker is an American magazine featuring journalism, commentary,
criticism, essays, fiction, satire, cartoons, and poetry.
General News
nymag.com New York Magazine obsessively chronicles the ideas, people, and cultural events
that are forever reshaping our world.
General News
nytimes.com Live news, investigations, opinion, photos and video by the journalists of The
New York Times from more than 150 countries around the world.
General News

Domain Description Categorization
qz.com Quartz is a guide to the new global economy for people who are excited by
change. We cover business, finance, economics
Finance/Business
realclearpolitics.com RealClearPolitics (RCP) is an independent, non-partisan media company that is
the trusted source for the best news, analysis and commentary.
Political News
reuters.com Find latest news from every corner of the globe at Reuters.com, your online
source for breaking international news coverage.
Breaking News
telegraph.co.uk A British daily broadsheet newspaper General News
theatlantic.com The Atlantic covers news, politics, culture, technology, health, and more,
through its articles, podcasts, videos, and flagship magazine.
General News
thedailybeast.com* The Daily Beast delivers award-winning original reporting, fact-informed analy-
sis, and sharp opinion in the arena of politics, pop-culture, and power and reaches
more than 1 million readers a day.
General News
theglobeandmail.com The Globe and Mail offers the most authoritative news in Canada, featuring
national and international news.
General News
theguardian.com Latest US news, world news, sports, business, opinion, analysis and reviews
from the Guardian, the world’s leading liberal voice.
General News
theroot.com* Black News and Black Views with a Whole Lotta Attitude General News
thesun.co.uk Breaking headlines and latest news from the UK and the World General News
theweek.com Concise, twice-daily news digests curated by our editors. Distilled from dozens
of the world’s most trusted news sources
General News
time.com Breaking news and analysis from TIME.com. Politics, world news, photos,
video, tech reviews, health, science and entertainment news.
Breaking News
usatoday.com Current national and local news, sports, entertainment, finance, technology, and
more
General News
vanityfair.com Vanity Fair is an American monthly magazine of popular culture, fashion, and
current affairs
Fashion
variety.com Entertainment news, film reviews, awards, film festivals, box office, entertain-
ment industry conferences.
Entertainment
vox.com V ox is a general interest news site for the 21st century. General News
vulture.com Vulture is a New York Magazine site providing continuous entertainment news
covering TV , movies, music, art, books, theater, comedy, podcasts, celebrities,
Entertainment
washingtonpost.com Breaking news, live coverage, investigations, analysis, video, photos and opin-
ions
Breaking News
wired.com Focuses on how emerging technologies affect culture, the economy, and politics Technology
Table 3: Categorization of Domains
Note: * means no Google blurb was available, so description is from the website itself
