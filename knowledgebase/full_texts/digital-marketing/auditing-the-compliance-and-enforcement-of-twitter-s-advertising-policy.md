---
title: Auditing the Compliance and Enforcement of Twitter's Advertising Policy
url: https://arxiv.org/abs/2309.12591
category: digital-marketing
subcategory: empirical
date: 2023-09
venue: ''
authors: []
source: arxiv
pdf_url: https://arxiv.org/pdf/2309.12591
pages: 19
chars: 89038
fetched_at: '2026-11-08T13:14:16+00:00'
kb_version: 1
---

# Auditing the Compliance and Enforcement of Twitter's Advertising Policy

Auditing the Compliance and
Enforcement of Twitter’s Advertising
Policy
Social Media + Society
XX(X):1–19
©The Author(s) 2024
Reprints and permission:
sagepub.co.uk/journalsPermissions.nav
DOI: 10.1177/ToBeAssigned
www.sagepub.com/
SAGE
Yash Vekaria1, Zubair Shafiq1 and Savvas Zannettou2
Abstract
Online platforms have enacted various policies to maintain a safe and trustworthy advertising environment. However,
the extent to which these policies are adhered to and enforced remains a subject of interest and concern. In this work,
we present a large-scale audit of adult advertising on Twitter (now X), specifically focusing on compliance with its adult
(sexual) content advertising policy. Twitter is an interesting case study in that it – uniquely from other social media
platforms – allows posting of adult content but prohibits adult content in advertising. We analyze approximately 35
thousand ads on Twitter with respect to their compliance to the adult content ad policy through Perspective API and
manual annotations. Among other things, we find that nearly 38% of ads violate Twitter’s adult content advertising
policy, although the platform eventually removed only about 63% of these non-compliant adult ads. We also find
inconsistencies in the moderation of such ads across languages, highlighting the need for more reliable and consistent
moderation practices across various languages. Overall, our findings highlight blind spots in Twitter’s adult ad policy
enforcement for certain languages and countries. Our work underscores the importance of external audits to monitor
compliance and improve transparency in online advertising.
Keywords
Social media advertising, adult advertising, platform audit, ad moderation, ad policy compliance
Disclaimer: This paper studies adult content in Twitter
ads. Therefore, we warn the readers about uncensored
mentions of sexually explicit content in the manuscript.
1 Introduction
Social media platforms allow advertisers to promote their
products or services to users on the platform (Twitter Adver-
tising, 2023; Meta Advertising, 2023). However, to maintain
a safe and trustworthy advertising environment (Geng, Yang,
Gao, Tan, & Yang, 2021), they impose various policies
that all advertisers must adhere to. For example, social
media platforms prohibit harmful advertisements that pro-
mote scams, phishing schemes, or illegal products and ser-
vices (Meta, 2023; Twitter’s Prohibited Content Policies,
2023). Similarly, social media platforms have strict policies
to prevent sharing or promotion of sexually explicit content
via advertising.
Given the potential of online advertising to reach and
influence many users (Arora, Bansal, Kandpal, Aswani,
& Dwivedi, 2019), there is a great deal of interest in
understanding whether platforms enforce compliance with
their stated advertising policies. Some online platforms, such
as Facebook, have introduced limited transparency by, for
example, making available an archive of the ads that run on
the platform (Meta, 2019). However, not all online platforms
have committed to such transparency, leading to new
regulations around the world (European Commission, 2023;
Congress, 2022). Even when they do, research has shown
that these transparency efforts are far from perfect (Edelson,
Lauinger, & McCoy, 2020). To improve transparency and
compliance, there is a pressing need for external audits that
provide an independent assessment of advertising policy
compliance on online platforms.
1University of California – Davis, USA
2Delft University of Technology, NL
Corresponding author:
Y ash Vekaria
University of California – Davis, USA
One Shields Ave, Davis, CA 95616, USA
This work was partially carried out during the author’s visit to Max Planck
Institute for Informatics, Saarbrucken, Germany
Email: yvekaria@ucdavis.edu
Prepared using sagej.cls [Version: 2017/01/17 v1.20]
arXiv:2309.12591v2  [cs.CY]  20 Feb 2025

2 Social Media + Society XX(X)
In this paper, we conduct the first large-scale audit
of compliance and enforcement of adult sexual content
advertising policy on Twitter (now X). Our time period
of analysis consists data from when the platform was
Twitter as well as from when it was re-branded as X.
However, in this paper, we refer to the platform as
‘Twitter’. More than “another study on Twitter”, through
this work, we aim to emphasize the importance of external
audits of social media platforms to study their risks
and potential online harm. This is becoming extremely
important and relevant as Digital Services Act (DSA)
recently went into effect in the EU, mandating large
online platforms to aid researchers with appropriate data
to assess whether and how their advertising systems are
manipulated. Twitter is an interesting case study since it
allows posting of adult content (Sensitive Media, 2018)
but it prohibits adult content in advertising (T. Business,
2023). Compliance with adult advertising policy is important
to avoid exposure of inappropriate content to minors or
vulnerable populations (Choi, Yoo, Reichert, & Northup,
2022; Thiel, DiResta, & Stamos, 2023). Anecdotal evidence
has also suggested that Twitter is unable to detect and remove
sexual exploitation content (Hutchinson, 2022) and that
13% of Twitter constitutes NSFW content (Press-Reynolds,
2022). Thus, it is crucial to evaluate the existing gaps and
new issues that have emerged in regards to adult advertising
policy compliance and enforcement on Twitter more recently
than ever before.
Our work aims to answer two research questions:
• RQ1: What is the level of moderation for adult sexual
advertisements on Twitter?
• RQ2: What is the level of compliance for the non-
moderated adult advertisements on Twitter with its
adult sexual content advertising policy?
By ‘non-moderated’ we refer to the ads that are supposedly
not detected or removed by Twitter’s moderation systems.
To answer these research questions, we collect a dataset
of nearly 600 million tweets over six months. We then
identify tweets that are advertisements by leveraging the
tweet metadata made available in Twitter’s Streaming
API (Platform, 2022a). We identify nearly 35,000 distinct
advertisements by filtering tweets created via Twitter Ad
Manager (Twitter’s Ad Manager Platform, 2023). To identify
the tweets that are likely removed by Twitter due to non-
compliance, we rehydrate the ads after two weeks. We
then compare removed and existing ads to understand
the effectiveness of Twitter’s ad moderation. To identify
advertisements that have a sexually-explicit nature, we use
Perspective API (Jigsaw, 2017).
Main findings. Our audit yields the following findings:
• We find that 38.64% of all advertisements on Twitter
are sexual in nature and hence violate the adult content
advertising policy. Twitter moderates 62.68% of these
violating ads; however, 37.32% of the remaining
violating ads exist on the platform even 2 weeks after
their creation despite the similarity in their content.
• Most of the moderated ads (81%) are due to a violation
of Twitter’s adult content advertising policy. 75% of
advertiser accounts whose at least one ad was removed
and that were created after the start of our data
collection violates Twitter’s adult content advertising
policy, suggesting spam accounts.
• Twitter moderates more ads in English, followed
by Arabic (24%) and Indonesian (21.3%). Also,
moderation of Japanese ads (2.8%) is extremely low
as compared to these languages, despite Japanese
(31.1%) being way more frequent than Arabic (8.7%)
or Indonesian (2.6%).
• Our analysis of ads that violate Twitter’s advertising
policies reveals that the majority ( ∼64%) of non-
moderated adult ads follow a simple ad template
comprising a period followed by a set of adult
keywords. Advertisers running such ads have a
higher tweets-per-minute ratio than a normal account,
suggesting automation. Some bad actors are also
observed to abuse Twitter ads platform to promote
porn content.
Overall, ad compliance with policies and enforcement on
Twitter remains relatively under-explored, in part because
Twitter does not provide an ad library (except recently
for European countries (Ads Transparency, 2023)). Our
work contributes to the literature by demonstrating how
researchers can perform independent and external audits
of advertisements on Twitter. We anticipate that our
proposed data collection methodology can assist researchers
in studying the compliance of advertisements with other
policies (e.g., political) on Twitter and also motivate similar
external audits on other social media platforms.
2 Related Work
Social media platforms rely on advertising for monetiza-
tion. Given potential negative ramifications, social media
platforms are concerned about the abuse of advertising on
their platforms. Prior research has attempted to understand
Prepared using sagej.cls

Y ash Vekaria et al. 3
problematic advertising on the open Web (Braun & Eklund,
2019; Kim, Barasz, & John, 2019; Knoll, 2016; Vekaria,
Nithyanand, & Shafiq, 2024; Zeng, Kohno, & Roesner, 2021;
Zeng, Wei, Gregersen, Kohno, & Roesner, 2021) as well as
social media platforms.
2.1 Ad Transparency on Social Media
To promote transparency in advertising on their platforms
and to comply with the regulations, social media plat-
forms have made efforts to make advertising-related infor-
mation publicly available. In 2019, Facebook started Ad
Library (Meta, 2019) – an archive of all the ads that
run on their platform. Prior work has studied different
issues pertaining to advertising on Facebook using this
ad archive (Abuhashesh, Alshurideh, Ahmed, Sumadi, &
Masa’deh, 2021; Chiu, 2022; Edelson et al., 2020; Marino
et al., 2019; Youn & Kim, 2019). Various studies have
explored different types of problematic advertising on Face-
book such as discriminatory ad delivery (Ali et al., 2019),
exploitation of sensitive data for ads (Caba ˜nas, Cuevas, &
Cuevas, 2018), Russia-linked targeting of socially divisive
ads (Ribeiro et al., 2019) and aggravating ads (Vargo &
Hopp, 2020), COVID-19 (Mejova & Kalimeri, 2020) or
vaccine-related (Jamison et al., 2020) advertising, dispar-
ity of harmful ads (Ali, Goetzen, Mislove, Redmiles, &
Sapiezynski, 2022), etc.
Unlike Facebook, Twitter does not allow direct access
to all the ads that run on its platform, hindering at-scale
analysis of its advertising ecosystem. Twitter also does not
have clear guidelines on how to identify ads nor it exposes
clear identification suggesting if an ad was paid for or not
in their platform data crawled using the API access. Due
to these limitations, little to no research has focused on
studying advertising on Twitter on a large scale. Most of the
Twitter-specific studies focus on understanding ad-targeting
from the marketing perspective on either a limited scale,
specific category, or a small set of advertisers (Arora et al.,
2019; Bradley & James, 2019; Clark et al., 2016; Hayes,
Golan, Britt, & Applequist, 2020; Janson, 2022; MR Ara ´ujo
et al., 2022; Noh, Kim, Kim, & Cheong, 2021; Wei et al.,
2020; Wells et al., 2020). Some of these works leverage
the tweets available on an advertiser’s Twitter timeline as
a representative sample for the tweets advertised by them.
However, this is inaccurate because an advertiser may not
always create a tweet for advertising purposes. It could also
create and share non-ad tweets (i.e., tweets that are not
advertised or sponsored), just like a normal Twitter user.
In contrast to these studies, we propose a novel
methodology to effectively detect actual ads from the Twitter
metadata as described later in Section 3.2. As a result,
tweets that we detect as ads are truly created from Twitter’s
advertising platform accessible via an advertiser account,
helping us study accurate advertising trends prevalent on
Twitter. Moreover, our data collection is not advertiser-
specific and involves a continuous collection of ads from
random 1% worldwide tweets over a period of 6 months,
aiding us to analyze ads on a large scale, as opposed to
previous works.
2.2 Adult Advertising on Social Media
Past research has studied adult advertising on the Web
focused on the promotion of adult services via advertise-
ments by sex traffickers (Keskin, Bott, & Freeman, 2021)
and sex workers (Skidmore, Garner, Desroches, & Saggu,
2018). Advertising related to adult content is concerning due
to the potential exposure of inappropriate content to minors
or vulnerable populations. For instance, as of 2023, 6.6%
of Twitter’s population comprises users in the age range of
13-17 (Statista, 2022). Exposure to adult ads due to poor
ad moderation can have adverse consequences on children.
Some studies have analyzed normal tweets related to illicit
adult content (Burbano & Hern ´andez-Alvarez, 2018) and
escort services posted by OnlyFans users on Twitter (Arenas,
Nair, Rabbany, & Farnadi, 2023) by treating them as adver-
tisements. This clearly shows a lack of understanding in the
research community regarding the identification of ads. To
this end, we propose and explain the novel methodology in
Section 3.2. Thus, no work has really studied adult adver-
tising on Twitter, however, research has attempted to detect
abusive Twitter accounts (Abozinadah & Jones Jr, 2017;
Cheng, Xing, Liu, & Lv, 2014), malicious activity (Founta
et al., 2018; Ilias & Roussaki, 2021; Singh, Bansal, & Sofat,
2016), and spread of adult content in general on Twit-
ter (Alshehri, El Moatez Billah Nagoudi, & Abdul-Mageed,
2018; Dhaka, Kakar, & Mehrotra, 2022; Mubarak, Hassan,
& Abdelali, 2021). To prevent the distribution of such
problematic content, extensive research has been conducted
in the past to understand content moderation strategies on
Twitter (Alizadeh et al., 2022; De Keulenaar, Magalh ˜aes, &
Ganesh, 2022; Gorwa, Binns, & Katzenbach, 2020; Haim-
son, Delmonaco, Nie, & Wegner, 2021; Jhaver, Boylston,
Yang, & Bruckman, 2021; Jim ´enez Dur ´an, 2022; Keller &
Leerssen, 2020; Morrow, Swire-Thompson, Polny, Kopec,
& Wihbey, 2022; Myers West, 2018; Papakyriakopoulos,
Serrano, & Hegelich, 2020). Although Twitter allows sharing
normal tweets with adult content, it prohibits the promotion
of adult content globally. This includes:
Prepared using sagej.cls

4 Social Media + Society XX(X)
pornography, escort services and prostitution,
full and partial nudity, penis enlargement
products & services and breast enhancement
services, modeled clothing that is sexual in
nature, dating sites which focus on facilitating
sexual encounters or infidelity, dating sites in
which money, goods or services are exchanged
in return for a date, mail order bride
services, sex toys, and host and hostess clubs
(Kyabakura).
This is referred to as adult (sexual) content advertising
policy (T. Business, 2023). Like Twitter, other social media
platforms (including Facebook) also strictly disallows any
advertising related to adult content with an exception that
allows its inclusion in promotion of art such as paintings or
sculptures (M. T. Center, 2023).
3 Dataset & Methodology
This section presents our dataset and research methodology
as depicted in Figure 1. First, we collect a random 1%
sample of real-time worldwide tweets (Section 3.1). Next, we
identify ads observed in the 1% tweet sample (Section 3.2).
Then, we describe how we identify and study adult ads
(Section 3.3). Also, we describe how we study potentially
malicious URLs embedded in adult ads on Twitter in
Section 3.4. Finally, we discuss the ethical considerations
when collecting and processing our dataset (Section 3.5).
Data related to our research is made available on the OSF
repository ( https://osf.io/sk8r2/?view only=
17bb5d6cc75343d38c2ece7f24c1ae90)
3.1 Data collection
We use Twitter’s Streaming API endpoint (Platform,
2022a), which returns a random sample of 1% of all
the tweets made at each given point of time during the
day anywhere in the world. To gather metadata related
to each tweet, we append all available query parameters
to the endpoint URL, particularly, tweet.fields,
user.fields, place.fields, and media.fields.
We run our data collection from July 2022 to December
2022, collecting a set of 597,889,636 tweets. Then, we
identify the tweets that are ads. To do this, we leverage
the source attribute as discussed in Section 3.2 and
select all tweets with a source in our ad sources, obtaining
a set of 34,606 ad tweets. Each ad or tweet undergoes
Twitter moderation, and if Twitter deems some tweets
unsafe, then the account may be temporarily restricted or
permanently suspended, making their tweets inaccessible.
A tweet creator could also delete the tweet if it receives
a warning from Twitter. To retain ads that are not
removed from Twitter, we rehydrate (or refresh) ad tweets
after two weeks from their initial fetch date using the
Tweet Lookup API (Platform, 2022b) endpoint: https://
api.twitter.com/2/tweets as done by Pochat et
al. (Le Pochat et al., 2022). Rehydration yielded only 24,530
ads, corresponding to a drop of about 30% ad tweets.1
3.2 Identifying Ads on Twitter
An inherent challenge that exists when studying online
advertising is obtaining data from social media platforms.
Unlike Facebook, Twitter does not provide an ad archive.
To overcome this challenge, in this work, we devise a novel
methodology that uses the source attribute on Twitter to
identify whether a tweet is an ad or not. The source
attribute is a metadata field that indicates the application that
was used for the posting of the tweet. For instance, if a user
posts a tweet using Twitter’s Web interface, the source will be
set to Twitter Web App, or if they posted via their iPhone, the
source will be set to Twitter for iPhone. Similarly, the source
attribute can be used to identify tweets created via Twitter’s
Ads Manager (Twitter’s Ad Manager Platform, 2023), which
assists our purpose of identifying ads.
To advertise on Twitter, an advertiser needs to create
a Twitter advertising account, which gives them access to
the Twitter Ads Manager to create and manage their ad
campaigns. A new ad tweet can be created through the
advertiser’s approved ad account using either the Twitter’s
Ads API (Twitter Ads source) or using one of the two
options from Twitter Ads Manager page - Tweet Composer
(under Creatives) and Create Campaign (under Campaign).
All ads created through Tweet Composer are assigned the
source Twitter for Advertisers or Twitter for Advertisers
(legacy) label. Ads created from theCreate Campaign option
can be either a Simple Campaign ( simpleads-ui source)
or Advanced Campaign ( advertiser-interface source). We
use the following sources for identifying ad tweets: Twitter
Ads, Twitter for Advertisers, Twitter for Advertisers (legacy),
simpleads-ui, and advertiser-interface. We refer to these as
our ad sources.
Limitations. Our methodology for identifying ad tweets
has some limitations that are worth mentioning. First, an
advertiser can in theory, use a custom source to create and
promote their tweets; hence, such tweets will not be captured
by our methodology. Second, a Twitter user can create tweets
via Twitter Ads Manager and post them as regular tweets
(unpaid) instead of paid ad tweets. Based on our experience
with Twitter advertising, we expect this phenomenon to
Prepared using sagej.cls

Y ash Vekaria et al. 5
Real-time Stream of
Worldwide Tweets
Twitter
Streaming API
1% Tweets Ad Tweets
source-based
Filtering
Perspective API
sexually_explicit
>= 0.3
Violating
Sexual
Ads
Figure 1. Overview of our methodology.
0.000.050.100.150.200.250.300.350.400.450.500.550.600.650.700.750.800.850.900.951.00
Perspective API thresholds for sexually explicit attribute
0
10
20
30
40
50Number of sexual tweets within 0.1 ranges
Selected threshold = 0.3
# Sexual tweets
0.0
0.2
0.4
0.6
0.8
1.0
Performance metric
Accuracy
F1-scores
Figure 2. Threshold selection for Perspective API’s
sexually explicit attribute to identify adult ads.
be extremely infrequent. Finally, Twitter has recently made
changes to its API (Tiers of X API Access, 2023) such that
only paid (Pro and Enterprise) versions allow access to the
Streaming API. Our data collection stopped when we lost
access to the Streaming API via our academic account. That
said, our methodology is still applicable – albeit needing paid
API access – to study advertising on Twitter.
3.3 Identifying Adult Ads
To identify adult sexual content in Twitter ads, we use
Google’s Perspective API (Jigsaw, 2017). Perspective API
uses machine learning models to identify different types of
abusive comments and the perceived impact of a comment
in the conversation. It provides scores for toxicity, insult,
identity attack , threat, profanity, and sexually explicit
attributes, ranging between 0 to 1 for each attribute. This
score can be interpreted as the probability of the text
being of a specific abusive nature. We focused only on
sexually explicit attribute, which captures “ references to
sexual acts, body parts, or other lewd content ” as broadly
scoped by Twitter’s definition of adult sexual content.
The textual content of each ad tweet is first translated to
English (if necessary2) using Google’s Translate API (PyPi,
2022) as popularly used in the literature (De Vries,
Schoonvelde, & Schumacher, 2018; Miftari, Gandolfi, &
Muvdi, 2020; Van Vliet, T ¨ornberg, & Uitermark, 2020)
and then passed to the Perspective API to obtain the
sexually explicit attribute score between 0 and 1. To decide
a suitable threshold for the sexually explicit attribute, we
extract a random sample of 500 ads (50 ad tweets from each
0.1 range of the score from 0 to 1 motivated from Hoseini,
Melo, Benevenuto, Feldmann, and Zannettou (2023)). A
sample of 200/500 ads (20/50 ad tweets from each 0.1 range)
is selected to evaluate inter-annotator agreement. Each ad
in this sample is independently annotated to be sexually
explicit or not by four researchers (one internal and three
external) by referring to the policy documentation. We find
a 90.5% inter-annotator agreement and Fleiss’ Kappa score
of 0.884, which suggests an almost perfect agreement. Next,
to evaluate the classification performance, we calculate f1-
scores for each 0.1 score range using the full sample of 500
ads. We select the threshold as 0.3 – for which we observe the
highest f1-score (f1-score = 0.92) and the greatest difference
in identified adult ads as depicted in Figure 2. False negatives
constitute of ads that contain “double meaning” text, which
makes the ML model behind the perspective API classify
it with a low sexually explicit score whereas it actually
implies sexual references when read by a human. All the ads
with sexually explicit score ≥ 0.3 are classified as adult
ads. We obtain a total of 13,374 sexually explicit ads from
a total of 34,606 ads in our dataset. For further validation,
we manually verify that these 13,374 ads indeed include
or refer to sexually explicit content and are in violation of
Twitter’s adult sexual content advertising policy; we observe
only 314 ( ∼2.35%) false positive ads. This suggests that
only 314 ads are falsely classified as sexually explicit, when
they are actually not, showing the effectiveness of using
a threshold of 0.3. These 314 ads are discarded to obtain
13,060 sexually explicit ads further studied in Section 4.
Prepared using sagej.cls

6 Social Media + Society XX(X)
Limitations. It is impossible to fully account for multiple
cultures and customs when analyzing multiple languages.
We acknowledge that the annotation is carried out by non-
culture experts – who may not be able to incorporate cultural
differences in their annotations.
3.4 URL Extraction and Classification
URLs are often used in ads by advertisers to promote
their products or websites. Malicious links embedded in
the ads can negatively affect many people interacting with
them and have largely been observed in tweets with adult
content (Szurdi, Luo, Kondracki, Nikiforakis, & Christin,
2021). Advances in cybersecurity have automated the
detection of such URLs for large-scale applications. Hence,
it is the responsibility of the platform to also moderate
and appropriately handle ads from advertisers that embed
and spread malicious URLs. While annotating adult ads,
we came across several such malicious links. Hence, we
study the security of URL usage in Twitter ads in context
of the adult ads to understand if Twitter is able to reliably
detect and remove ads containing such malicious URLs to
enforce their link embedding policy (T. H. Center, 2022).
We extract embedded links from the tweet metadata obtained
from the API response. Often, the embedded URLs in the
tweet are shortened URLs (e.g., t.co, bit.ly, etc.) and do
not actually represent the final landing page that is actually
embedded. Hence, we visit each of the embedded URL in
a fresh browser window programmatically and wait for all
the intermediate redirects to complete before extracting the
final landing page. We check the landing page URL against
VirusTotal (VirusTotal, 2022) using their API endpoint to
obtain counts for the number of anti-virus services that
classify the URL asmalicious and/or suspicious. To compare
URL usage against non-advertised tweets, we extract a
random sample of non-ad tweets that have at least one
embedded URL from the 1% dump of size equal to the total
number of ads in our dataset.
3.5 Ethical Considerations
Our work relies solely on analyzing publicly available
datasets obtained via Twitter API; hence, we do not deal
with sensitive data that is private. Due to this, no additional
privacy concerns arise from our work beyond those that
are also applicable to the vast research work that analyzes
large-scale datasets obtained via the Twitter API (Jhaver
et al., 2021; Qayyum et al., 2023). In this work, we
performed manual annotations to label advertisements and
assess whether they were related to sexually explicit content.
Out of the four annotators, one was internal (one of the
authors), and three were external (two undergrads and one
PhD student). We acknowledge that this manual work might
expose the annotators to sensitive and disturbing content.
As a result, an informed consent was taken from each
annotator by explaining the details of the annotation work
and the fact that they might be exposed to such content.
We elected only three external annotators to minimize the
exposure to potentially disturbing content to only a few
annotators, but also sufficient to establish credibility in our
annotations. On a separate note, when extracting embedded
URLs from ads and visiting them independently to extract
landing pages, we do not remove campaign details or user
identifiers (like ‘?uid=XX&etc’) (if any). Since extraction
was done from Tweet metadata with one of the author’s
API keys, we expect these identifiers to be either absent or
associated with the author. Moreover, we intentionally do not
perform stripping of these identifiers because, in dynamic
campaigns, the resultant landing pages could be selected
dynamically. These identifiers are essential to accurately
replicate the actual behavior of a real user click. The crawls
were carried out in a containerized environment, and hence,
the researchers weren’t exposed to any harmful results from
clicking malicious URLs.
4 Results
From our dataset of 34,606 advertisements over a time
period of 6 months, 10,306 were removed by Twitter within
two weeks of their creation. We first discuss the general
characteristics of the ads that Twitter is successfully able
to detect and remove and contextualize it with respect to
adult ad policy violation in Section 4.1. We then investigate
the compliance of non-moderated ads with Twitter’s adult
content advertising policy in Section 4.2.
4.1 RQ1: (In)effectiveness of Twitter’s
Enforcement
We first analyze the ad content that Twitter is likely to
remove due to violations of its platform policies. Figure 3
depicts the distribution of ads per day – before and after
the rehydration during the period of our data collection. We
observe that 15%-55% (∼28% on an average) of daily ads on
Twitter are removed by either the platform or the advertiser.
The total number of ads in Twitter’s 1% data has gradually
increased beginning October 2022 post-Twitter’s acquisition,
along with an increase in ad removals up to 75% ( ∼44% on
an average) daily ads since mid-November 2022.
The analysis yields that these ad removals appear
to mostly occur from ads campaigned by less popular
advertisers — 50% of all advertisers with less than 100
Prepared using sagej.cls

Y ash Vekaria et al. 7
Jul 06
Jul 08
Jul 10
Jul 12
Jul 14
Jul 16
Jul 18
Jul 20
Jul 22
Jul 24
Jul 26
Aug 01
Aug 03
Aug 05
Aug 07
Aug 09
Aug 11
Aug 13
Aug 15
Aug 17
Aug 19
Aug 21
Aug 23
Aug 25
Aug 27
Aug 29
Aug 31
Sep 02
Sep 04
Sep 06
Sep 08
Sep 10
Sep 12
Sep 14
Sep 16
Sep 18
Sep 20
Sep 22
Sep 24
Sep 26
Sep 28
Sep 30
Oct 02
Oct 04
Oct 06
Oct 08
Oct 10
Oct 12
Oct 14
Oct 16
Oct 18
Oct 20
Oct 22
Oct 24
Oct 26
Oct 28
Oct 30
Nov 01
Nov 03
Nov 05
Nov 07
Nov 09
Nov 11
Nov 13
Nov 15
Nov 17
Nov 19
Nov 21
Nov 23
Nov 25
Nov 27
Nov 29
Dec 01
Dec 03
Dec 05
Dec 07
Dec 10
Dec 12
Dec 14
Dec 16
Dec 18
Dec 20
Ad Date
0
100
200
300
400# of Ads
Average Monthly Ads (Before Rehydration)
Average Monthly Ads (After Rehydration)
Total Ads (Before Rehydration)
Total Ads (After Rehydration)
Figure 3. Distribution of ads on Twitter over the period of data collection before and after the rehydration (or refresh).
Jan 2007
Jan 2008
Jan 2009
Jan 2010
Jan 2011
Jan 2012
Jan 2013
Jan 2014
Jan 2015
Jan 2016
Jan 2017
Jan 2018
Jan 2019
Jan 2020
Jan 2021
Jan 2022
Jan 2023
Account Creation Date
0
500
1000
1500
2000
2500Number of Accounts Created
Removed Ads
Rehydrated Ads
Start of Data Collection
0.0
0.2
0.4
0.6
0.8
1.0
CDF
Figure 4. Distribution of account creation dates of advertisers
whose ads are removed with respect to not removed by Twitter
moderation. Solid lines correspond to number of accounts
created while dashed line corresponds to its cumulative
distribution function (CDF).
followers ( ∼80% with less than 10K followers) have at
least one advertised tweet removed by Twitter. Some of
these advertisers also resemble the characteristics of a spam
account with very low follower-to-following ratios. One
could argue that accounts demonstrating bot-based activity
and posting violating ads could have been created after the
start of our data collection. To rule out this possibility, we
analyze the creation of accounts of advertisers associated
with advertising on Twitter. Figure 4 shows the distribution
of account creation dates of all advertisers in our data – the
ones whose at least one ad was removed post-rehydration as
well as the ones whose ads were not removed. Overall, out of
10,221 distinct advertisers in our data, ∼80% accounts were
created before the start of our data collection. In contrast,
∼44% (i.e., 915 out of 2089) advertiser accounts whose ads
were removed by Twitter were created after the start of our
data collection. Moreover, 75% of 915 advertising accounts
promoted at least one ad that violated Twitter’s adult content
advertising policy. We do not perform analysis of all tweets
from each of these accounts as it is out-of-scope for our
research. However, this suggests that a majority of ads that
are removed from the accounts created after the start of our
data collection are due to their violation of Twitter’s adult
content advertising policy.
Having looked at the general characteristics of ad
removals, we analyze the content of the removed ads to
identify violations pertaining to adult content as described
in Section 3.3. Out of 10306 removed ads, 8383 ads
(i.e., ∼81%) have sexually explicit attribute score ≥0.3 and
hence were likely removed due to violation of Twitter’s
adult content advertising policy. Surprisingly, these ads also
mostly follow a similar content pattern as non-moderated
adult ads as described later in Section 4.2. Hence, we perform
an in-depth analysis of the content in that section. However,
this shows that Twitter is able to detect and remove some
adult ads within two weeks of their posting while not others,
despite their content being extremely similar.
To understand language-specific differences in ad moder-
ation of sexually explicit content, we look at the distribu-
tion of language detected in adult ads that are moderated
and removed by Twitter. We observed that out of 8383 ad
removals due to violation of adult content advertising policy,
cases where an ad contains textual content in English are
the highest (8001; 95.4% of all removed adult ads) followed
by Arabic (250; 2.9% of all removed adult ads), Indonesian
(136; 1.6% of all removed adult ads) and then Japanese (5;
0.06% of all removed adult ads) (see Figure 5). The second
most prominent language of ads in our entire dataset of 34K
ads is Japanese (4533; 13.1% of all ads), followed by Arabic
(3010; 8.7% of all ads) and Indonesian (908; 2.6% of all ads)
at sixth as observed in Figure 10. However, interestingly,
we detect a higher number of ad removals in Arabic and
Indonesian as compared to Japanese. To further corroborate
this claim, we compare the distribution of ad removals with
policy violations of adult content ad policy in non-moderated
ads for these two languages. We observe 171 violating
Japanese adult ads, 504 violating Indonesian adult ads, and
789 violating Arabic adult ads that are not moderated by
Twitter. If we compute the percentage of violating ads that
are moderated per language, it turns out to be 2.8% for
Japanese, 21.25% for Indonesian, and 24% for Arabic. This
shows that moderation in Japanese is poorer ( δ=21%) as
compared to Indonesian or Arabic ads, suggesting language-
specific differences in Twitter’s ad moderation.
Prepared using sagej.cls

8 Social Media + Society XX(X)
0 1000 2000 3000
Number of Sexual Ads
German
Bengali
Korean
Portuguese
Spanish
Turkish
Japanese
Indonesian
Arabic
English
Lanuage
Figure 5. Language distribution of the violating adult ads
Takeaways. The key takeaways from our analyses of ads
removed by Twitter are as follows:
• On average, Twitter observes a removal of ∼28% of
daily ads due to policy violations that increase to
∼44% post-Twitter’s acquisition.
• 75% of advertiser accounts whose at least one ad
was removed and that were created after the start
of our data collection violates Twitter’s adult content
advertising policy, suggesting spam accounts.
• ∼81% of the removed ads (i.e., 8383 ads) violate
Twitter’s adult content ad policy. This suggests that
Twitter’s ad moderation is effective in detecting policy
violations related to the platform’s adult content
advertising policy.
• We find some blindspots of Twitter’s enforcement
– Twitter is (in)effective at removing non-compliant
ads in specific languages – we observe Twitter to
moderate more ads in English, followed by Arabic
and Indonesian. Also, moderation in Japanese is
extremely low compared to these languages, even
though Japanese is way more frequent than Arabic or
Indonesian among all ads.
4.2 RQ2: Compliance of Non-Moderated Ads
with Twitter’s Adult Advertising Policies
To better understand the blindspots of Twitter’s enforcement,
we now analyze the compliance of non-moderated ads
with Twitter’s adult content advertising policy. By ‘non-
moderated,’ we refer to these ad tweets that are supposedly
not detected or removed by Twitter’s moderation systems.
Using the methodology described in Section 3.3, we
identify 4,991 ( ∼20.35%) ads out of 24,530 rehydrated
ads that have a sexually explicit score of 0.3 or above and
manually remove 118 false positive ads to obtain 4,873
sexually explicit ads. We find more than 75% of ads in our
data have sexually explicit score of 0.05 or less, while∼10%
of ads have scores as high as >0.9 (Figure 12). Out of
0 1000 2000 3000 4000
Noisy data points (out of 4783)
0
50
100
150
200
250
300Number of Resultant Clusters
 0.15
0.20
0.25
0.30
0.35
0.40
0.45
DBCV Score
Figure 6. Scatter plot showing number of clusters and noisy
data points obtained for different hyperparameter combinations
(with DBCV score >= 0.1) from HDBSCAN for clustering of
violating adult ads. Red star represents the selected optimal
combination.
34,606 ads in the entire dataset, 13,256 sexually explicit ads
were obtained – 63.24% of which are already moderated
and removed by the platform, as discussed in the previous
section. We analyze the remaining 4873 (36.76%) ads here.
Content Analysis. To characterize the content of the adult
ads, we follow a textual clustering approach employed
by Hoseini et al. (Hoseini et al., 2023). We use
a pre-trained multilingual BERT model (distiluse-base-
multilingual-cased-v2) (Reimers & Gurevych, 2019) to
generate 512-dimensional embedding for each violating ad.
We selected this specific model primarily because it supports
50+ languages and has been shown to perform well in
standard semantic similarity tasks. Next, embeddings are
reduced to 128-dimensional space using UMAP (McInnes,
Healy, & Melville, 2018) for effective density-based
clustering. We use HDBSCAN to perform clustering of these
embeddings. We experiment with different combinations
of 4 hyperparemeters – min cluster size, min samples,
cluster selection method, and metric and compute
DBCV (Density-based Clustering Validation) score for each
combination to evaluate quality of resultant clusters. DBCV
score signifies relative density connection between pairs of
points and ranges from -1 to 1, where a higher value suggests
better clusters. We discard combinations with DBCV <
0.1 as we observe poor clustering results for these cases.
Figure 6 depicts the rest of the 1748 combinations. We select
the combination ( min cluster size=7, min samples=2,
metric=euclidean, cluster selection method=eom) that
produces the highest number of clusters (188) with least
noise (1663 points). We validate the effectiveness of our
0.1 threshold by selecting two random samples of 100 ad
tweets each from the resultant clusters (such that there is
at least one ad tweet from each cluster) – one with DBCV
Prepared using sagej.cls

Y ash Vekaria et al. 9
≥ 0.1 and one with < 0.1, respectively. Next, the primary
researcher on the project assign a cluster label to each ad
tweet given an ad’s textual content and list of cluster labels.
Model assigned cluster labels are hidden from the annotator
during the annotation to avoid bias. Annotation result shows
that 60/100 ads with DBCV≥ 0.1 are accurately assigned the
correct cluster label as output by BERT, while only 19/100
ads with cosine < 0.1 are correctly assigned, establishing
confidence in our threshold.
Figure 7 represents the output clusters along with the
detected Louvain communities. Qualitative analysis of ads
corresponding to different clusters clearly reveals grouping
of ads based on distinct adult content-specific categories –
for example, the light purple community in the bottom right
represents all the ads that promote indo-porn content. Upon
manually evaluating the ads in the violating clusters, we
observe that there are 2 main types of content structures
followed by the advertisers: First, the textual content of
the ad begins with a period (i.e., “.”) followed by different
space-separated adult content-related words. Maddocks et
al. (Maddocks, 2020) observed this type of bot-based text
pattern in normal tweets. However, it is surprising to
see this pattern in Twitter ads, as it suggests a lack of
effective ad moderation. The majority of ads with this
structure only contain textual content and do not have
any embedded links or images. 3,122 out of 4,873 (i.e.,
∼64%) unmoderated adult ads belonged to this category.
Upon analyzing the usernames of the advertiser accounts
in this sub-type, they all followed the same naming
pattern – some hypothetical first name followed by last
name without any spaces and first letter of both first and
last names capitalized, for instance MilliexChanax. Upon
mapping different advertisers’ author id to their username,
we observed a pattern wherein to avoid detection, an
advertiser account (i.e., a given author id) kept changing
their username in variable amounts of time. We observed
as high as 49 usernames mapped to a single author id. It is
important to note that the characteristics of non-moderated
sexual ad content described above are also followed by
the moderated adult ads discussed in Section 4.1. However,
despite that, Twitter is ineffective in moderating all ads that
follow the same content pattern. The remaining ads contain
some textual content describing the scenario displayed in the
linked porn video, and the catchy text is aimed to entice
the viewer’s attention using clickbaity adult language. This
sub-category of ads involved scenarios where the advertisers
used dark patterns and embedded unsafe links in violation
of Twitter’s quality policy (Policy, 2020) for advertising, as
explained later in this section. A standard embedded video
within a tweet should always be playable on Twitter itself
when clicked on the play button as per Twitter’s policy.
However, we observed that some advertisers embed a link
in the ad with a preview containing an image with a play
button to deceive the viewers into thinking it is a normal
playable video so that when they click on the play button, it
redirects them to the embedded link. Twitter moderates even
the videos. So, to evade detection, some advertisers were
found to embed an adversarial playable porn video which
was edited so as to have a static foreground overlaid on the
video such that humans could perceive the video contents.
However, the moderation framework could falsely classify
it as negative. These tactics are strictly against Twitter’s
quality policy. However, specific behavioral insights of non-
compliance discussed here can help platform X in improving
its ad moderation and compliance framework, as ads with
these deceptive or evasion techniques were never moderated
by Twitter. Moreover, Twitter allows posting of adult content
but limits its spread on the platform. However, such porn-
disguised-as-ad can potentially be promoted like a normal
ad to reach a much larger audience, increasing the harm to
vulnerable users.
URL Analysis. Out of 24,530 non-moderated ads, 20,362
ads had at least one URL embedded within the tweet.
We observed a common usage of URL shortening services
to shorten the original URL before embedding it. Besides
the benign functionality of reducing the length of URLs,
advertisers could also use it to hide malicious URLs in their
ads. As a result, we analyze the security of embedded as
well as the final landing URLs resulting from clicking on
an embedded link. Using the VirusTotal-based classification
of each URL, we calculate a score as follows:
Score = max(male + suse, mall + susl) (1)
Here, male and mall are the counts of VirusTotal services
that respectively classified the embedded and landing URL of
the current tweet as malicious. Similarly, suse and susl are
the respective counts of VirusTotal services that respectively
classified the embedded and landing URL of the current
tweet as suspicious. Then, we treat a tweet as problematic
if the above score is greater or equal to 3 for at least
one URL embedded in it. We experimented with different
values for this threshold – with a threshold value of 2, many
benign links were also getting classified as problematic; with
higher thresholds above 3, there was up to 11% decrease in
problematic tweets with an increase in the threshold from 3
to 7. As a result, we chose the score threshold as 3 to avoid
false negatives. Figure 8 depicts the number of ad tweets with
Prepared using sagej.cls

10 Social Media + Society XX(X)
sex-teen-hentai
pornhub-lesbian-onlyfans
porno-teen-porn
adult-slut-pornhub
hooker-porn-hentai
teen-fetish-porn
lover-beautiful-breasts
mmm-sex-jk
fetish-hentai-porn
slut-pornhub-lesbian
porn-fetish-hentai
porn-slut-hentai
porn-fetish-cam
blowjob-porno-fetish
fetish-blowjob-porn
bro-indo-porn
mario-kart-tracks
porno-teen-slut
bbw-porn-fetish
porn-slut-hentai
pussy-porno-lesbian
orgasm-teen-fetish
want-sex-need
viral-porn-indo
porno-pornhub-lesbian
arabicsex-saudi-sex
pussy-webcam-blowjob
live-love-sex
porn-bokep-indo
teenleaks-lesbian-nsfwtwt
porn-fetish-cam
money-indo-sex
viral-porn-indo
hooker-fetish-pornhub
ass-incest-stepmother
knowing-sister-sex
squeezes-tits-indo
pornhub-slut-porn
leave-arabicsex-sexy
blowjob-cum-arabicsex
slut-porn-pornhub
sex-beautiful-girl
orgy-porn-hentai
pornhub-blowjob-teen
hooker-lesbian-hentai
lesbian-pornhub-pussy
cam-hentai-porn
lesbian-blowjob-porn
blowjob-anal-pornhub
lingerie-porno-sex
indo-viral-porn
porn-blowjob-lesbian
adult-hooker-hentai
bra-makes-look
hooker-pussy-hentai
porn-indo-high
lesbian-blowjob-porn
porn-teen-hentai
cam-teen-sex
porn-teen-hentai
porn-indo-viral
sexy-big-boobs
bx-saturday
immoral-egyptian-snoring
friend-sex-wife
sex-movies-come
japanese-sex-fuck
blowjob-pornhub-lesbian
adult-pornhub-blowjob
fetish-sex-porn
breasted-arab-wife
orgasm-girl-vibrator
gaming-adult-lesbian
sex-beautiful-girl
pornhub-teen-lesbian
indo-perverted-brother
sex-porn-lesbian
sexfilms-fuckings-incest
exclusive-arab-incest
porn-cam-fetish
sex-porn-teen
pornhub-teen-hentai
fucking-cuckold-husband
pornhub-fetish-hentai
wife-husband-wife
kardashian-pm-new
teen-hentai-porn
feeling-fulfillment-intimacy
perverted-son-takes
breasted-wife-husband
pussy-pornhub-hentai
kink-fun-porn
hentai-porn-slut
hooker-porn-lesbian
slut-teen-porn
hooker-porno-porn
video-arab-couple
hentai-adult-pornhub
blowjob-cam-lesbian
slut-bbw-porn
wife-movie-happiness
pornhub-slut-blowjob
blowjob-porn-bbw
porn-bokep-indo
ass-wife-husband
teens-mesum-pornviral
porn-orgasm-hentai
boob-neighbor-mistress
blowjob-sex-pornhub
body-amiami-pantyhose
wife-happy-wife
hentai-orgasm-slut
sex-onlyfans-lesbian
love-romantic-couple
know-weakness-married
hands-rubbing-breasts
wife-couch-erotic
cam-girl-slut orgasm-lesbian-pornhub
porn-blowjob-lesbian
pornhub-onlyfans-lesbian
fetish-teen-porn
boobs-wife-couple
orgasm-porn-hentai
veiled-outside-bastard
pornhub-hooker-blowjob
blowjob-hentai-porn
hot-pervert-sunday
horny-latina-teen
love-love-body
teens-mesum-pornviral
big-tits-chick
fetish-teen-sex
skandal-bokep-indo
porn-hooker-hentai
anal-pornhub-porn
pulsing-feel-warmth
lesbian-fetish-blowjob
sex-bokepindo-pornviral
fetish-pussy-porn
porn-orgasm-hentai
cam-teen-pornhub
indo-porn-abg
porn-onlyfans-slut
boss-bokepviral-pornindomilf-hentai-porn
hentai-sex-bbw
pornhub-hentai-porn
lesbian-orgasm-pornhub
sex-milf-pornhub
fetish-porn-bbw
slut-teen-porn
joy-arab-porn
porn-blowjob-lesbian
teen-porn-lesbian
nude-nude-nude
hooked-jump-read
tiktok-indo-porn
orgasm-bbw-porn
porn-pornhub-teen
sex-onlyfans-pornhub
big-breasts-arab
teen-porno-pornhub
pussy-swollen-grinding
boyfriend-enjoying-video
slut-porn-orgasm
porn-teen-lesbian
pussy-pornhub-porn
slut-onlyfans-porn
pornhub-porno-fetish
making-love-couple
world-desperate-cornea
hentai-porn-slut
hentai-teen-pornhooker-porn-hentai
vibrator-scarf-sexy
perverted-viral-memek
hentai-bbw-porn
milf-porn-pornhub
hentai-blowjob-fetish
indo-abg-porn
breasts-arab-girlfriend
sex-orgasm-pornhub
menstrual-pain-comes
movie-wife-butt
tits-screaming-hotel
porno-slut-hentai
porn-teen-onlyfans
Figure 7. Clustering of sexually explicit ads in violation of Twitter’s adult content advertising policy.
Jul 10
Jul 20
Aug 03
Aug 13
Aug 23
Sep 02
Sep 12
Sep 22
Oct 02
Oct 12
Oct 22
Nov 01
Nov 11
Nov 21
Dec 01
Dec 12
Ad Date
0
100
200
300# of Ads
Total Ads
Ads w/ Problematic URLs
Figure 8. Distribution of the problematic ads with respect to all
the ads run on each day on Twitter. Here, problematic refers to
classifying either the embedded or the landing URLs of an ad as
malicious or suspicious or both by 3 or more VirusTotal services.
problematic URLs with respect to the daily total ads after the
rehydration3. We observe an increase in ads with problematic
URLs from December 2022 onwards. This is likely due to the
fact that amnesty was granted by Elon Musk to all the past
suspended Twitter accounts – such as that of the former US
president Donald Trump, for instance – by restoring them.
Another benign yet worrisome reason could be that Twitter
is unable to detect ads malicious URLs in two weeks, and
moderation of such ads requires longer. This explanation can
be deduced based on the temporal distribution of URLs in
Figure 8.
It is important to understand how different URL usage is
for violating adult ads compared to other ads. As a result,
we plot a scatter chart between the sum of (malicious +
suspicious) VirusTotal services and sexually explicit scores
of embedded URLs and Landing URLs in Figure 9. Let’s first
look at the non-adult ads (i.e., sexual explicit < 0.3) – for
both embedded and landing URLs, we obtain 103 ads where
its URL is problematic. For adult ads (i.e., sexual explicit
>= 0.3), in the case of embedded URLs, only 3 ads contain
a problematic embedded link, while on the other hand, 345
Prepared using sagej.cls

Y ash Vekaria et al. 11
0
5
10 threshold = 0.3Embedded URLs
0.0 0.2 0.4 0.6 0.8 1.0
Sexually Explicit Score of Ads (Perspective API)
0
10# of (Mal. + Susp.) VT Services
threshold = 0.3Landing URLs
Figure 9. Scatter diagram of (malicious + suspicious) counts of
VirusTotal (VT) services for embedded URLs and landing URLs
partitioned with respect to the threshold of sexually explicit
score (i.e., 0.3) of the ad tweet containing those URLs.
ads contain benign embedded URLs, which lead to unsafe
landing pages.
Upon closely analyzing different kinds of landing URLs,
we observed a variety of potentially harmful scenarios.
First, the landing URL sometimes results after a number
of redirects. Moreover, Twitter only expands the embedded
URLs, which are converted by Twitter’s link service, and
warns its viewers about any harmful page by checking it
against a list of potentially dangerous sites it maintains
before proceeding (T. H. Center, 2022). However, it does
not check the landing URLs currently. Landing URL pages
comprise – normal porn sites, fake reCAPTCHA and
consent options, system-infected warning screens, anti-virus
download prompts, online game sites (including interactive
adult games), sex-baity sites, YouTube channel promotions,
Forex market trading publisher websites, betting websites
(like bet365 offers and registration), etc.
Takeaways. We summarize the takeaways from our audit of
Twitter’s adult content advertising policies with respect to
non-moderated ad content:
• We observe ∼37% of all sexually explicit ads in
our dataset to bypass Twitter’s moderation. They
constitute 20% of all the rehydrated ads and are in
violation of Twitter’s adult sexual content advertising
policy.
• Majority ( ∼64%) of non-moderated adult ads follow a
simple ad template comprising of a ‘period’ followed
by a set of adult words. Advertisers running such ads
are suspected to have a higher tweets-per-minute ratio
than a normal account, suggesting automation. Despite
similar characteristics, Twitter is able to moderate such
ads only partially.
• Adult ads with videos and embedded links are
observed either using dark patterns to engage users
or using problematic links. A non-negligible fraction
(∼2.75%) of daily ads on an average are detected to
contain problematic URLs (as per VirusTotal) – most
of which embed benign shortened URLs that actually
lead to malicious landing pages. This pattern is more
common in adult ads than in other ads.
5 Discussion
In this work, we performed a large-scale audit of Twitter
compliance and enforcement of Twitter’s adult content
advertising policy. We selected Twitter because it is
understudied in terms of compliance and enforcement, and
unlike most social media platforms that strictly prohibit both
posting and promoting adult content, Twitter permits posting
but prohibits promotion of such material. We collected a total
of 35K advertisements on Twitter and analyzed them to shed
light on how Twitter moderates ads containing adult content
and the degree of compliance with the platform’s adult
content advertising policy. Among other things, our study
finds that a large percentage of advertisements on Twitter are
sexual in nature (∼38%) and that 37% of them are likely not
effectively moderated by Twitter. Also, we find moderation
discrepancies and significant differences in content across
various languages; Twitter is more effective in moderating
adult advertisements in English when compared to adult
ads in Japanese. At the same time, we find inconsistencies
in Twitter’s moderation practices; adult ads that follow a
simple template (period followed by a list of sexual words)
are not consistently moderated and removed by Twitter.
Overall, our work and findings have several important
implications for stakeholders interested in online advertising
and content moderation. Below, we discuss the implications
of our work related to data access, content moderation of
online advertising, harms that may arise from exposure to
advertisements that have a sexual nature, and platform’s
moderation workflow and affordances.
5.1 Data Access
Our work relied on access to the Twitter API – we
leveraged the source attribute that was made available
via the API to identify ads and the application used to
share or promote tweets. Unfortunately, during our data
collection, our free academic access to the Twitter API and
the availability of the source attribute were cut off, mainly
due to changes made on the Twitter platform after Elon
Musk’s acquisition (Community, 2022). These changes to
Prepared using sagej.cls

12 Social Media + Society XX(X)
data access have detrimental effects on scientific research
efforts that aim to understand and mitigate harmful online
phenomena and harm transparency efforts.
Twitter introduced access tiers (Developer, 2024) on
February 9th, 2023, under which with a basic tier, researchers
get access to only 15K tweets per month at $200. Before
that, anyone could access up to two million tweets from the
past seven days for free every month. Moreover, research
institutions could obtain unlimited amounts from the entire
archive for free. This magnitude of data allowed researchers
to rigorously study online communities and analyze platform
harms such as bot activities, spread of misinformation, hate
speech, political propaganda, etc. at a macroscopic as well
as fine-grained level. But that is no longer possible. As
of August 14, 2024, even Meta decommissioned its public
insights tool – CrowdTangle (M. T. Center, 2024). Without
access to data, there is little scrutiny over the platform’s
practices. There is need for a regulatory change that requires
platforms to provide data access to researchers.
We argue that, as a research community, we need to work
closely with policymakers to ensure that the platforms are
accountable for harms arising from their services and must
provide the necessary means for researchers to audit their
services. Indeed, recently, Digital Services Act (European
Commission, 2023) introduced by the EU Commission went
into effect, which calls for such audits on social media
platforms to understand if and how their advertising systems
are manipulated in the EU. We believe this is an essential step
in the right direction. At the same time, we believe there is
still a long way to go about finding ways to incentivize online
platforms to be more transparent and to give data access to
researchers.
5.2 Content Moderation
With his acquisition of Twitter, Elon Musk vocalized
his stance against moderating content that is not strictly
illegal (Guardian, 2024). This view empowers free speech
but also opens door to hate speech and other types of
malicious activities that may cause more harm than good to
the end users.
Our empirical analysis demonstrates the blind spots,
inconsistencies, and ineffectiveness of Twitter’s moderation
practices to prevent the publication of harmful advertise-
ments, in this case, ads promoting adult content. Our find-
ings are in line with previous characterizations of Twitter’s
moderation practices on non-ad content and their inability to
effectively and consistently moderate and prevent the sharing
of harmful content (Paudel, Blackburn, De Cristofaro, Zan-
nettou, & Stringhini, 2023; Zannettou, 2021).
Post acquisition, on November 4th, 2022, Elon Musk fired
50% of Twitter employees (Reuters, 2022) – this constituted
15% of its moderation team (News, 2022). This was followed
by two additional lay-offs on November 15th and 19th,
which worsened the platform’s content moderation as per
its policies at the time. We observe this in our data based
on the increase in the net volume of tweets as well as the
volume of removed content around this time in Figure 3.
Figure 13 also depicts the increase in volume of adult ads
during this time. The situation further aggravated when
amnesty was granted on December 1st, 2022 to all the
users who were either banned or suspended under Twitter’s
regime (Milmo, 2022). Twitter also revised its adult content
advertising policy to allow promotion of certain products
that were previously disallowed *. This included dating
and/or marriage brokerage services, sexual Merchandise (for
example sex toys, sexualized clothing), condoms, lubricants
and other non-prescription contraceptives (X. Business,
2024). This shows that already poor compliance and
moderation got worse with laxed enforcement of policies and
lack appropriate moderation staff.
Overall, our findings emphasize the need for effective
and consistent content moderation, especially in the context
of online advertising. Even for online platforms, this is
important because ineffective and inconsistent moderation
of advertisement content can have negative consequences.
For example, advertisers can choose not to advertise on the
platform due to brand-safety concerns (Aisha & Nakano,
2023) or users loosing trust in the platform’s ability to
diminish the propagation of harmful content and migrate to
other platforms (O’Flaherty, 2024). Due to this millions of
users have migrated to newly emerged platforms – Mastodon
and BlueSky – for better moderation (Boran, 2024)
Twitter’s adult content advertising policy prohibits
promotion of adult content globally. Specifically, policy
clearly prevents promoting “sexually suggestive text, images,
videos, audio, gestures, poses and movements etc. ” Our
results show that not only videos with adult content go
undetected from advertising but also that the platform is
unable to moderate simple ad tweet text with a bunch of
sexual words that is promoted. This is different from all other
social media platforms that generally disallows both sharing
as well as promoting adult content on their platform. One of
the other important distinction is that Twitter also provides a
capability of advertising any post that was originally created
as a normal tweet for a brief period of time. This is crucial
due to the unique adult content advertising policy under
∗These changes were observed from Oct 2024 as per the Wayback archive.
Prepared using sagej.cls

Y ash Vekaria et al. 13
which a malicious advertiser can create a normal adult
content tweet and then later on promote it. Our approach
cannot detect such cases as the data obtained using Twitter’s
API doesn’t provide any information that suggests if the
tweet was ever promoted in its lifetime or not.
Additionally, our results highlight significant differences
in the moderation of advertisements across languages, which
demonstrates the need to improve content moderation in
lower resource languages (when compared to English). That
is, content shared in non-English languages is more likely
to bypass content moderation, which emphasizes that online
harm can be more prevalent on content that is not shared
in English. These findings have important implications and
emphasize the pressing need to improve content moderation
and moderators’ workforce that is able to effectively deal
with content shared in languages other than English. We
discuss more about the platform’s moderation workflows in
the Section 5.4.
5.3 Potential Harms
Trust and safety are crucial to evaluate and then appropriately
mitigate harms arising from services offered by social media
platforms. Our study shows that there is a non-negligible
amount of adult ads on Twitter. This also includes porn
promoted as an ad by bad actors. Its presence on platforms
could potentially harm curious youths’ image and perception
regarding sexual relations and sexuality (Paasonen, Jarrett,
& Light, 2024). According to a study, one in five youth
between the ages of 9 and 17 would view unwanted sexual
material online (The Conversation, 2018). Also, nearly 25%
of youth presented with adult content experience intense
fear or anxiety (Madigan et al., 2018). Such inappropriate
content reduces trust in digital platforms. When platforms
like Twitter fail to adequately moderate adult ads, it
sends conflicting signals to users regarding the platform’s
commitment to user safety. This can also disproportionately
harm marginalized groups, such as women and LGBTQ+
youth, who are more likely to encounter stigmatizing or
exploitative depictions of sexuality online (Powell & Henry,
2020). A study found that increasing the intensity of sexual
humor in advertisement improves its effectiveness amongst
men but leads to significantly more negative attitudes toward
the advertisement and brand amongst women (Freeman,
Marder, Gorton, & Angell, 2023). Stanford researchers
showed an increase in CSAM content on the platform
in 2023 (Observatory, 2023) where illicit adult content
was distributed by a network of accounts operated by
minors. Moreover, Participants of a user study focused at
understanding user perspectives on content of an ad, have
expressed disgust against the presence of sexual content in
ads (Zeng, Kohno, & Roesner, 2021).
Besides increasing risk of its exposure to vulnerable
platform users, advertising adult content could also result
in the potential exploitation and trafficking of vulnerable
individuals through poorly moderated ad spaces. Studies
have highlighted that online platforms, including social
media, have been exploited by traffickers to advertise
exploitative services, often under the guise of adult content or
escort ads (Latonero, 2011). When platforms like Twitter fail
to regulate such ads, they risk becoming unwitting enablers
of trafficking networks, where victims of exploitation
are marketed and sold to large audiences with minimal
accountability (Williams, 2019). Furthermore, the global
reach of social media platforms exacerbate the scale of this
harm, making it harder for authorities to track and intervene.
Overall, there is a pressing need to improve platform
affordances and moderation workflows so that these potential
harms are effectively mitigated from online platforms like
Twitter.
5.4 Moderation Workflows
To better understand ineffective moderation, it is important
to look into Twitter’s moderation workflow (Sircar, 2024).
Twitter adopts a two-fold approach in its ad moderation
constituting of automated systems and human moderators. In
the first phase, Twitter’s automated systems perform a large-
scale review of platform-wide posted content, including ads
using AI-based approaches designed to detect violations
such as hate speech, violence, inappropriate content, etc.
If these automated systems flag an ad to be problematic,
appropriate human moderators review the ad content to reach
a decision about whether to moderate the content or not. A
label is assigned to an ad to provide context and additional
information to the users. (X. H. Center, 2024b). Then, on a
case-by-case basis, it maybe either restricted or the account
maybe suspended/terminated.
Our research shows that the adult ads are disparately
moderated across different languages, suggesting that
sufficient number of language-specific human moderators
are not available. This further worsened when the platform
fired a portion of its moderation team (Elliott & Stokel-
Walker, 2022), leaving with no option but to heavily rely
on automated AI systems, lowering platform’s moderation
accuracy. Recruiting expert human moderators in proportion
to the volume of tweets in different languages can help.
We argue that if we can determine that a significant portion
of the non-compliant content goes unmoderated using
Perspective API, then Twitter has a lot more resources and
Prepared using sagej.cls

14 Social Media + Society XX(X)
is more capable (than us) to determine whether problematic
content is being shared on the platform. A recent study
showed that state-of-the-art generative AI models perform
better harmful content labeling than crowd workers (Jo,
Wesołowska, & Wojcieszak, 2024). Given that Twitter
recently updated its platform policies to allow the user posted
content to be accessed and utilized to train its generative AI
model – Grok (X. H. Center, 2024a), it can be used to detect
and moderate problematic content such as adult content on
the platform.
We finally conclude with recommendations to improve
these moderation workflows. Existing moderation workflow
is able to moderate some ads with a given pattern but not
all. Lookalike-based moderation models can help moderate
these basic non-compliant ads at the very least in a timely
manner. Additionally, most of the false negatives (although
small in number) comprises of an ad with textual content that
can be interpreted differently – sometimes benign appearing
text were observed to be associated with additional modality
of content that is in violation of adult content policy. To
effectively handle such cases, context-aware multi-modal
models could prove to be useful to incorporate broader
context, such as cultural norms, regional variations, etc.
Local moderators can help moderate flagged content more
effectively than a generic moderator. Lastly, integrating ad
policy checks directly when an advertiser creates an ad can
prove to be a low-cost and effective way to early-detect
violating ads preventing them from running as part of the
campaign. This also ensures that advertisers understand and
comply with platform advertising policies strictly.
Notes
1. We observe that only a small fraction ( <5%) of ads are removed
by Twitter even after the 2-week rehydration period.
2. ∼50% of the ads are not in English.
3. Moderated ads are no longer accessible, we could not perform
this analysis on removed ads.
References
Abozinadah, E. A., & Jones Jr, J. H. (2017). A statistical
learning approach to detect abusive twitter accounts.
In Iccda (pp. 6–13).
Abuhashesh, M. Y ., Alshurideh, M. T., Ahmed, A., Sumadi,
M., & Masa’deh, R. (2021). The effect of culture
on customers’ attitudes toward facebook advertising:
the moderating role of gender. Review of International
Business and Strategy, 31(3), 416–437.
Advertising, T. (2023). How x advertisements work?
https://business.twitter.com/en/
help/troubleshooting/how-twitter-ads
-work.html.
Aisha, C., & Nakano, E. (2023). Twitter’s
hate content problem is driving advertisers
away. https://time.com/6295711/
twitters-hate-content-advertisers/.
Ali, M., Goetzen, A., Mislove, A., Redmiles, E., &
Sapiezynski, P. (2022). All things unequal: Measuring
disparity of potentially harmful ads on facebook. In
Conpro.
Ali, M., Sapiezynski, P., Bogen, M., Korolova, A., Mislove,
A., & Rieke, A. (2019). Discrimination through
optimization: How facebook’s ad delivery can lead to
biased outcomes. CSCW, 3.
Alizadeh, M., Gilardi, F., Hoes, E., Kl ¨user, K. J., Kubli,
M., & Marchal, N. (2022). Content moderation as
a political issue: The twitter discourse around trump’s
ban. JQD: DM, 2.
Alshehri, A., El Moatez Billah Nagoudi, H. A., & Abdul-
Mageed, M. (2018). Think before your click: Data
and models for adult content in arabic twitter. In Ta-
cos (V ol. 15).
Arenas, M., Nair, P., Rabbany, R., & Farnadi, G. (2023).
Social media as a vector for escort ads: A study on
onlyfans advertisements on twitter. InAcm websci (pp.
260–270).
Arora, A., Bansal, S., Kandpal, C., Aswani, R., & Dwivedi,
Y . (2019). Measuring social media influencer index-
insights from facebook, twitter and instagram.Journal
of retailing and consumer services, 49, 86–101.
Boran, M. (2024). How top twitter rivals fared since elon
musk exodus. https://www.newsweek.com/
how-top-twitter-rivals-fared-since
-elon-musk-exodus-1984404.
Bradley, A., & James, R. J. (2019). How are major gambling
brands using twitter? International Gambling Studies,
19(3), 451–470.
Braun, J. A., & Eklund, J. L. (2019). Fake news, real
money: Ad tech platforms, profit-driven hoaxes, and
the business of journalism. Digital Journalism, 7(1),
1–21.
Burbano, D., & Hern ´andez-Alvarez, M. (2018). Illicit,
hidden advertisements on twitter. In Icedeg (pp. 317–
321).
Business, T. (2023). Twitter’s adult sexual content
advertising policy. https://business.x.com/
en/help/ads-policies/ads-content
Prepared using sagej.cls

Y ash Vekaria et al. 15
-policies/adult-or-sexual-products
-and-services.html.
Business, X. (2024). Revised ads content policies:
Adult or sexual products and services. https://
business.x.com/en/help/ads-policies/
ads-content-policies/adult-or-sexual
-products-and-services.
Caba˜nas, J. G., Cuevas, ´A., & Cuevas, R. (2018). Unveiling
and quantifying facebook exploitation of sensitive
personal data for advertising purposes. In Usenix
security (pp. 479–495).
Center, M. T. (2023). Facebook’s adult content advertising
policy: Adult content. https://transparency
.fb.com/policies/ad-standards/
objectionable-content/adult-content.
Center, M. T. (2023). Introduction to the advertising
standards on facebook. https://transparency
.fb.com/policies/ad-standards.
Center, M. T. (2024). Crowdtangle. https://
transparency.meta.com/researchtools/
other-datasets/crowdtangle.
Center, T. H. (2022). How to post links in
a tweet. https://help.twitter.com/en/
using-twitter/how-to-tweet-a-link.
Center, X. H. (2024a). About grok, your humorous
ai assistant on x. https://help.x.com/en/
using-x/about-grok.
Center, X. H. (2024b). Enforcement options. https://
help.x.com/en/rules-and-policies/
enforcement-options.
Cheng, H., Xing, X., Liu, X., & Lv, Q. (2014). Isc:
An iterative social based classifier for adult account
detection on twitter. IEEE Transactions on Knowledge
and Data Engineering, 27(4).
Chiu, Y.-P. (2022). An elaboration likelihood model
of facebook advertising effectiveness: Self-monitoring
as a moderator. Journal of Electronic Commerce
Research, 23(1), 33–44.
Choi, H., Yoo, K., Reichert, T., & Northup, T. (2022). Sexual
ad appeals in social media: Effects and influences of
cultural difference and sexual self-schema. IJA, 41(5),
910–929.
Clark, E. M., Jones, C. A., Williams, J. R., Kurti, A. N.,
Norotsky, M. C., Danforth, C. M., & Dodds, P. S.
(2016). Vaporous marketing: uncovering pervasive
electronic cigarette advertisements on twitter. PloS
one, 11(7), e0157304.
Community, X. D. (2022). Twitter v2 api: Missing source
field again. https://devcommunity.x.com/
t/twitter-v2-api-missing-source
-field-again/181895.
De Keulenaar, E., Magalh ˜aes, J. C., & Ganesh, B. (2022).
Modulating moderation: A history of objectionability
in twitter moderation practices.
Developer, X. (2024). Developer portal. https://
developer.x.com/en.
De Vries, E., Schoonvelde, M., & Schumacher, G. (2018).
No longer lost in translation: Evidence that google
translate works for comparative bag-of-words text
applications. Political Analysis.
Dhaka, D., Kakar, S., & Mehrotra, M. (2022). Detection
of spammers disseminating obscene content on twitter.
International Journal of Business Intelligence and
Data Mining, 21(3), 265–289.
Edelson, L., Lauinger, T., & McCoy, D. (2020). A security
analysis of the facebook ad library. In 2020 ieee s&p
(pp. 661–678).
Elliott, V ., & Stokel-Walker, C. (2022).Twitter’s moderation
system is in tatters. https://www.wired.com/
story/twitters-moderation-system-is
-in-tatters/.
European Commission. (2023). The digital
services act package. https://digital
-strategy.ec.europa.eu/en/policies/
digital-services-act-package.
for Business, T. (2023). Twitter’s ad manager platform.
https://ads.twitter.com/.
for Business, T. (2023). X ads transparency.
https://business.twitter.com/en/
help/ads-policies/product-policies/
ads-transparency.html.
Founta, A., Djouvas, C., Chatzakou, D., Leontiadis, I.,
Blackburn, J., Stringhini, G., . . . Kourtellis, N. (2018).
Large scale crowdsourcing and characterization of
twitter abusive behavior. In Icwsm (V ol. 12).
Freeman, R., Marder, B., Gorton, M., & Angell, R. (2023).
Would you share that? how the intensity of violent
and sexual humor, gender and audience diversity
affect sharing intentions for online advertisements.
Information Technology & People, 36(6), 2312–2337.
Geng, S., Yang, P., Gao, Y ., Tan, Y ., & Yang, C. (2021).
The effects of ad social and personal relevance
on consumer ad engagement on social media: The
moderating role of platform trust. Computers in
human behavior, 122, 106834.
Gorwa, R., Binns, R., & Katzenbach, C. (2020). Algorithmic
content moderation: Technical and political challenges
in the automation of platform governance. Big Data &
Prepared using sagej.cls

16 Social Media + Society XX(X)
Society, 7(1).
Guardian, T. (2024). Elon musk defends stance on
diversity and free speech in interview. https://
www.theguardian.com/technology/2024/
mar/18/elon-musk-defends-stance
-diversity-free-speech-interview
-don-lemon.
Haimson, O. L., Delmonaco, D., Nie, P., & Wegner, A.
(2021). Disproportionate removals and differing con-
tent moderation experiences for conservative, trans-
gender, and black social media users: Marginalization
and moderation gray areas. CSCW, 5, 1–35.
Hayes, J. L., Golan, G., Britt, B., & Applequist, J.
(2020). How advertising relevance and consumer–
brand relationship strength limit disclosure effects of
native ads on twitter. IJA, 39(1), 131–165.
Hoseini, M., Melo, P., Benevenuto, F., Feldmann, A., &
Zannettou, S. (2023). On the globalization of the
qanon conspiracy theory through telegram. In Acm
websci (pp. 75–85).
H.R.6796 - Digital Services Oversight and Safety Act of
2022. (2022). https://www.congress.gov/
bill/117th-congress/house-bill/6796/
text.
Hutchinson, A. (2022). New revelations suggest
that twitter is unable to detect and remove
child sexual exploitation content. https://
www.socialmediatoday.com/news/
new-revelations-suggest-that-twitter
-is-unable-to-detect-and-remove
-child-s/630866/.
Ilias, L., & Roussaki, I. (2021). Detecting malicious activity
in twitter using deep learning techniques. Applied Soft
Computing.
Jamison, A. M., Broniatowski, D. A., Dredze, M., Wood-
Doughty, Z., Khan, D., & Quinn, S. C. (2020).
Vaccine-related advertising in the facebook ad archive.
Vaccine, 38(3), 512–520.
Janson, S. (2022). Pandemic-era advertising: A study of
the twitter advertising of four online food delivery
companies during the 2020 pandemic.
Jhaver, S., Boylston, C., Yang, D., & Bruckman, A. (2021).
Evaluating the effectiveness of deplatforming as a
moderation strategy on twitter. CSCW, 5, 1–30.
Jigsaw. (2017). Google perspective api. https://
perspectiveapi.com.
Jim´enez Dur ´an, R. (2022). The economics of content
moderation: Theory and experimental evidence from
hate speech on twitter. Available at SSRN.
Jo, C. W., Wesołowska, M., & Wojcieszak, M. (2024).
Harmful youtube video detection: A taxonomy of
online harm and mllms as alternative annotators.arXiv
preprint arXiv:2411.05854.
Keller, D., & Leerssen, P. (2020). Facts and where to find
them: Empirical research on internet platforms and
content moderation. Social media and democracy: The
state of the field and prospects for reform, 220, 224.
Keskin, B. B., Bott, G. J., & Freeman, N. K. (2021).
Cracking sex trafficking: Data analysis, pattern
recognition, and path prediction. Production and
Operations Management, 30(4), 1110–1135.
Kim, T., Barasz, K., & John, L. K. (2019). Why am i
seeing this ad? the effect of ad transparency on ad
effectiveness. Journal of Consumer Research , 45(5),
906–932.
Knoll, J. (2016). Advertising in social media: a review of
empirical evidence. IJA, 35(2), 266–300.
Latonero, M. (2011). Human trafficking online:
The role of social networking sites and online
classifieds. Research Series . Retrieved from
https://communicationleadership.usc
.edu/files/2011/08/humantrafficking
online 2011.pdf
Le Pochat, V ., Edelson, L., Van Goethem, T., Joosen, W.,
McCoy, D., & Lauinger, T. (2022). An audit of
facebook’s political ad policy enforcement. In Usenix
security (pp. 607–624).
Maddocks, S. (2020). ‘a deepfake porn plot intended
to silence me’: exploring continuities between
pornographic and ‘political’deep fakes. Porn Studies,
7(4), 415–423.
Madigan, S., & Dimitropoulos, G. (2018). One in five
youth see unwanted sexual content online, says new
research.
Madigan, S., Villani, V ., Azzopardi, C., Laut, D., Smith, T.,
Temple, J. R., . . . Dimitropoulos, G. (2018). The
prevalence of unwanted online sexual exposure and
solicitation among youth: A meta-analysis. Journal
of Adolescent Health, 63(2), 133–141.
Marino, C., Caselli, G., Lenzi, M., Monaci, M. G., Vieno,
A., Nik ˇcevi´c, A. V ., & Spada, M. M. (2019).
Emotion regulation and desire thinking as predictors
of problematic facebook use. Psychiatric Quarterly,
90, 405–411.
McInnes, L., Healy, J., & Melville, J. (2018).
Umap: Uniform manifold approximation and pro-
jection for dimension reduction. arXiv preprint
arXiv:1802.03426.
Prepared using sagej.cls

Y ash Vekaria et al. 17
Mejova, Y ., & Kalimeri, K. (2020). Covid-19 on facebook
ads: competing agendas around a public health crisis.
In Acm sigcas compass (pp. 22–31).
Meta. (2019). Ad library. https://www.facebook
.com/ads/library/.
Meta Platforms, I. (2023). Meta advertising. https://
www.facebook.com/business/ads.
Miftari, D., Gandolfi, F., & Muvdi, Y . (2020). An analysis
of politicians’ tweets: A multilingual approach.
Milmo, D. (2022). Elon musk offers general amnesty
to suspended twitter accounts. https://
www.theguardian.com/technology/
2022/nov/24/elon-musk-offers-general
-amnesty-to-suspended-twitter
-accounts.
Morrow, G., Swire-Thompson, B., Polny, J. M., Kopec, M.,
& Wihbey, J. P. (2022). The emerging science
of content labeling: Contextualizing social media
content moderation. Journal of the Association for
Information Science and Technology, 1365–1386.
MR Ara ´ujo, M., Guimar ˜aes, S., Silva, M., Caetano, J.,
Santos, J., CS Reis, J., . . . M. Almeida, J. (2022).
Earlyad: A system for real-time surveillance of
brazilian early electoral ads on twitter. In Hypertext
(pp. 225–227).
Mubarak, H., Hassan, S., & Abdelali, A. (2021). Adult
content detection on arabic twitter: Analysis and
experiments. In Proceedings of the sixth arabic nlp
workshop (pp. 136–144).
Myers West, S. (2018). Censored, suspended, shadow-
banned: User interpretations of content moderation on
social media platforms. New Media & Society, 20(11),
4366–4383.
News, C. (2022). Elon musk twitter layoffs
include outsourced content moderators.
https://www.cbsnews.com/news/
elon-musk-twitter-layoffs-outsourced
-content-moderators/.
Noh, Y ., Kim, H., Kim, K., & Cheong, Y . (2021).
The relationship between consumer engagements with
super bowl ad tweets and the advertisers’ official
twitter accounts: a panel data analysis of 2019 super
bowl advertisers. IJA, 40(6), 852–869.
Observatory, S. I. (2023). Addressing the distribution
of illicit sexual content of minors online.
https://cyber.fsi.stanford.edu/
news/addressing-distribution-illicit
-sexual-content-minors-online.
O’Flaherty, K. (2024). Delete x: Millions of users just got a
new reason to quit today. https://www.forbes
.com/sites/kateoflahertyuk/2024/11/
15/delete-x-millions-of-users-just
-got-a-new-reason-to-quit-today/.
Paasonen, S., Jarrett, K., & Light, B. (2024). Nsfw: Sex,
humor, and risk in social media. Mit Press.
Papakyriakopoulos, O., Serrano, J. C. M., & Hegelich,
S. (2020). The spread of covid-19 conspiracy
theories on social media and the effect of content
moderation. Harvard Kennedy School Misinformation
Review, 1(3).
Paudel, P., Blackburn, J., De Cristofaro, E., Zannettou, S., &
Stringhini, G. (2023). Lambretta: learning to rank for
twitter soft moderation. In Ieee s&p (pp. 311–326).
Peters, J. (2022). Twitter cut 15 percent of its trust and
safety staff but says it won’t impact moderation.
https://www.theverge.com/2022/11/4/
23441404/twitter-trust-safety-staff
-layoffs-content-moderation.
Platform, T. D. (2022a). Twitter’s streaming api - volume
streams. https://developer.twitter.com/
en/docs/twitter-api/tweets/volume
-streams/introduction.
Platform, T. D. (2022b). Twitter’s tweet lookup api.
https://developer.twitter.com/en/
docs/twitter-api/tweets/lookup/
api-reference/get-tweets.
Platform, T. D. (2023). Tiers of x api access.
https://developer.twitter.com/en/
docs/twitter-api/getting-started/
about-twitter-api.
Policies, T. P. C. (2023). Prohibited content policies.
https://business.twitter.com/
en/help/ads-policies/ads-content
-policies.html.
Policy, T. Q. (2020). Twitter’s quality policy. https://
business.twitter.com/en/help/
ads-policies/ads-content-policies/
quality-policy.html.
Powell, A., & Henry, N. (2020). Image-based sexual abuse:
Victims and perpetrators. Oxford: Oxford University
Press. doi: 10.1093/oso/9780190872013.001.0001
Press-Reynolds, K. (2022). A total of 13% of twitter is nsfw.
https://www.businessinsider.com/nsfw
-not-safe-for-work-explicit-content
-twitter-growing-internal-2022-10.
PyPi. (2022). Google translate. https://pypi.org/
project/googletrans/.
Prepared using sagej.cls

18 Social Media + Society XX(X)
Qayyum, H., Zi Hao Zhao, B., Wood, I., Ikram, M.,
Kourtellis, N., & Ali Kaafar, M. (2023). A longitudinal
study of the top 1% toxic twitter profiles. In Acm
websci (pp. 292–303).
Reimers, N., & Gurevych, I. (2019, 11). Sentence-bert:
Sentence embeddings using siamese bert-networks.
In Emnlp. ACL. Retrieved from http://arxiv
.org/abs/1908.10084
Reuters. (2022). Twitter to start layoffs friday morning:
Internal email. https://www.reuters.com/
technology/twitter-start-layoffs
-friday-morning-internal-email-2022
-11-04/.
Ribeiro, F. N., Saha, K., Babaei, M., Henrique, L., Messias,
J., Benevenuto, F., . . . Redmiles, E. M. (2019). On
microtargeting socially divisive ads: A case study of
russia-linked ad campaigns on facebook. In Facct (pp.
140–149).
Singh, M., Bansal, D., & Sofat, S. (2016). Behavioral
analysis and classification of spammers distributing
pornographic content in social media. Social Network
Analysis and Mining, 6, 1–18.
Sircar, A. (2024). X’s latest content findings reveal troubling
trends in ai moderation. https://www.forbes
.com/sites/anishasircar/2024/10/18/
xs-latest-content-findings-reveal
-troubling-trends-in-ai-moderation/.
Skidmore, M., Garner, S., Desroches, C., & Saggu, N.
(2018). The threat of exploitation in the adult
sex market: A pilot study of online sex worker
advertisements. Policing: A Journal of Policy and
Practice, 12(2), 210–218.
Statista. (2022). Distribution of twitter users
worldwide as of april 2021, by age group.
https://www.statista.com/statistics/
283119/age-distribution-of-global
-twitter-users/.
Szurdi, J., Luo, M., Kondracki, B., Nikiforakis, N., &
Christin, N. (2021). Where are you taking me?
understanding abusive traffic distribution systems. In
Web conference 2021(p. 3613–3624).
Thiel, D., DiResta, R., & Stamos, A. (2023). Cross-
platform dynamics of self-generated csam. Stanford
Internet Observatory, Freeman Spogli Institute for
International Studies.
Twitter Incorporation. (2018). Sensitive media pol-
icy. https://help.twitter.com/en/rules
-and-policies/media-policy.
Van Vliet, L., T ¨ornberg, P., & Uitermark, J. (2020). The
twitter parliamentarian database: Analyzing twitter
politics across 26 countries. PLoS one , 15(9),
e0237073.
Vargo, C. J., & Hopp, T. (2020). Fear, anger, and
political advertisement engagement: A computational
case study of russian-linked facebook and instagram
content. Journalism & Mass Communication
Quarterly, 97(3), 743–761.
Vekaria, Y ., Nithyanand, R., & Shafiq, Z. (2024, may).
The inventory is dark and full of misinformation:
Understanding ad inventory pooling in the ad-tech
supply chain. In Ieee s&p (p. 3-3).
VirusTotal. (2022). Virustotal api. https://www
.virustotal.com/.
Wei, M., Stamos, M., Veys, S., Reitinger, N., Goodman, J.,
Herman, M., . . . Ur, B. (2020). What twitter knows:
characterizing ad targeting practices, user perceptions,
and ad explanations through users’ own twitter data.
In Usenix security (pp. 145–162).
Wells, C., Shah, D., Lukito, J., Pelled, A., Pevehouse, J. C.,
& Yang, J. (2020). Trump, twitter, and news media
responsiveness: A media systems approach. New
media & society, 22(4), 659–682.
Williams, M. (2019). Trafficking and technology: The role of
digital platforms in facilitating and combating human
trafficking. Journal of Human Trafficking, 5(2), 124–
138. doi: 10.1080/23322705.2019.1567701
Youn, S., & Kim, S. (2019). Newsfeed native advertising on
facebook: young millennials’ knowledge, pet peeves,
reactance and ad avoidance. IJA, 38(5), 651–683.
Zannettou, S. (2021). “I Won the Election!”: an empirical
analysis of soft moderation interventions on Twitter.
In Icwsm (pp. 865–876).
Zeng, E., Kohno, T., & Roesner, F. (2021). What makes
a “bad” ad? user perceptions of problematic online
advertising. In Chi.
Zeng, E., Wei, M., Gregersen, T., Kohno, T., & Roesner, F.
(2021). Polls, clickbait, and commemorative $2 bills:
problematic political advertising on news and media
websites around the 2020 us elections. In Acm imc
(pp. 507–525).
Prepared using sagej.cls

Y ash Vekaria et al. 19
Supplemental material
Anonymized data: https://osf.io/sk8r2/?view only=
17bb5d6cc75343d38c2ece7f24c1ae90
Language distribution of our dataset
Our dataset comprises of ads in 57 different languages across
the globe. Figure 10 depicts the distribution of the top most used
languages in the textual content of the ads retained after the 14-
day rehydration period. We also compare this distribution with
the prevalence of the same languages in the random 1% data and
Twitter ads before the rehydration. We observe a strongly co-related
language distribution maintained in the 1% data and the ads data for
some top languages, namely, Japanese, Spanish, and Turkish.
English (en)Japanese (ja)Arabic (ar)Spanish (es)Turkish (tr) Indonesian (in) French (fr)German (de)Portuguese (pt) Korean (ko)
Top 10 Ad Languages After Rehydration
0
20
40
60% of Data Category
1% Data
Ads Before Rehydration
Ads After Rehydration
Figure 10. Distribution of languages in 1% data as well as in
Twitter ads obtained from 1% data.
Weekly advertising trend of Twitter advertisers
We try to understand if advertising on Twitter follows a diurnal
trend (i.e., advertising is more prevalent on some specific days of
the week than others). This could be because advertisers, based on
their past experiences, have observed receiving higher engagements
on their ads if they were shown on some specific day of the week.
To look into this diurnal pattern, we plot the average number of
total ads and the average number of distinct advertisers advertising
on each weekday in Figure 11. We observe that Twitter advertising
decreases over the weekends and then kejpg increasing from
Monday onwards until its peak on Friday.
Mon Tue Wed Thu Fri Sat Sun
Weekday
80
100
120
140
160Average Counts
Average Total Ads
Average Distinct Advertisers
Figure 11. Diurnal trend of Twitter advertising over week.
Temporal distribution of ad policy violation
0.00 0.25 0.50 0.75
Sexually Explicit Score from Perspective API
0.00
0.25
0.50
0.75
1.00
Density
Sexually Explicit Score
Figure 12. CDF distribution of the Perspective API scores of
24,530 rehydrated ads in our data for sexually explicit attribute.
Jul 10
Jul 20
Aug 03
Aug 13
Aug 23
Sep 02
Sep 12
Sep 22
Oct 02
Oct 12
Oct 22
Nov 01
Nov 11
Nov 21
Dec 01
Dec 12
Tweet Date
0
50
100
150# of Violating Sexual Ads
Total Sexual Ads
Figure 13. Daily Distribution of the ads violating Twitter’sadult
content ad policy.
Now, we show the temporal distribution of violations related
adult content advertising policies. Figure 12 shows CDF of
sexually explicit score of perspective API of all refreshed
ads in our dataset with positive scores. Figure 13 shows the number
of violations for adult ads per day in our dataset. We can observe
that from late Oct 2023, the number of violating adult ads have
significantly increased. One of the plausible reasons could be the
layoff of 50% Twitter employees post Musk’s Twitter acquisition
in multiple rounds, which included a lay-off of 15% of moderation
staff on Nov 4, 2023 (Peters (2022)). Or it could be simplify due
to a general increase Twitter advertising post Musk’s takeover as he
relaxed platform policies to allow free speech.
Prepared using sagej.cls
