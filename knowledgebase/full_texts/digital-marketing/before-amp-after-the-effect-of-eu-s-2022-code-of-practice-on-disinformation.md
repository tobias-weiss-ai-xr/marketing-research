---
title: 'Before &amp; After: The Effect of EU''s 2022 Code of Practice on Disinformation'
url: https://arxiv.org/abs/2410.11369
category: digital-marketing
subcategory: empirical
date: 2024-10
venue: ''
authors:
- Emmanouil Papadogiannakis
- Panagiotis Papadopoulos
- Nicolas Kourtellis
- Evangelos P. Markatos
source: arxiv
pdf_url: https://arxiv.org/pdf/2410.11369
pages: 11
chars: 72949
fetched_at: '2026-11-08T13:16:32+00:00'
kb_version: 1
---

# Before &amp; After: The Effect of EU's 2022 Code of Practice on Disinformation

Before & After: The Effect of EU’s 2022 Code of Practice on
Disinformation
Emmanouil
Papadogiannakis
FORTH & University of Crete
Heraklion, Greece
Panagiotis
Papadopoulos
FORTH
Heraklion, Greece
Nicolas Kourtellis
Telefonica Research
Barcelona, Spain
Evangelos Markatos
FORTH & University of Crete
Heraklion, Greece
Abstract
Over the past few years, the European Commission has made sig-
nificant steps to reduce disinformation in cyberspace. One of those
steps has been the introduction of the 2022 “Strengthened Code of
Practice on Disinformation”. Signed by leading online platforms,
this Strengthened Code of Practice on Disinformation is an attempt
to combat disinformation on the Web. The Code of Practice includes
a variety of measures including the demonetization of disinforma-
tion, urging, for example, advertisers “to avoid the placement of
advertising next to Disinformation content”.
In this work, we set out to explore what was the impact of the
Code of Practice and especially to explore to what extent ad net-
works continue to advertise on dis-/mis-information sites. We per-
form a historical analysis and find that, although at a hasty glance
things may seem to be improving, there is really no significant re-
duction in the amount of advertising relationships among popular
misinformation websites and major ad networks . In fact, we show
that ad networks have withdrawn mostly from unpopular misinfor-
mation websites with very few visitors, but still form relationships
with highly unreliable websites that account for the majority of
misinformation traffic. To make matters worse, we show that ad
networks continue to place advertisements of legitimate companies
next to misinformation content. We show that major ad networks
place ads in almost 400 misinformation websites in our dataset.
CCS Concepts
• Information systems→ World Wide Web; Online advertising.
Keywords
Misinformation; Disinformation; Advertising; Web Monetization;
Code of Practice
ACM Reference Format:
Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Nicolas Kourtellis,
and Evangelos Markatos. 2025. Before & After: The Effect of EU’s 2022 Code
of Practice on Disinformation. In Proceedings of the ACM Web Conference
2025 (WWW ’25), April 28-May 2, 2025, Sydney, NSW, Australia. ACM, New
York, NY, USA, 11 pages. https://doi.org/10.1145/3696410.3714898
1 Introduction
From the US presidential elections in 2016 [6] to the Brexit refer-
endum [35], Covid-19 [47], the war in Ukraine [31] and the recent
This work is licensed under a Creative Commons Attribution 4.0 International License.
WWW ’25, Sydney, NSW, Australia
© 2025 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-1274-6/25/04
https://doi.org/10.1145/3696410.3714898
conflict in the Middle East [ 18], disinformation today is shaping
major global events. It tears apart the fabric that holds our societies
together by destroying people’s faith in traditional news sources
and undermining people’s trust in governments, public institutions,
and democratic processes [39]. Disinformation is usually designed
to appeal to our worst impulses, fears and prejudices – all in an
attempt to shape opinions or divide and conquer a society on the
information battlefield. Over 80% of EU citizens see fake news as
an issue both for their country, and for democracy in general [48].
In an attempt to mitigate this threat, governments, tech firms, and
stakeholders have explored various methods to identify and curtail
the spread of fake news. In 2018, Google launched the Digital News
Innovation Fund that supports over 7000 news partners ($300M in
funding) [29]. In 2022, the United Nations in their report [49] set out
the relevant international legal framework, and discussed measures
that States and technology enterprises reported to have taken to
counter disinformation. A few years earlier, the European Union
issued the 2018 Code of Practice on Disinformation, where repre-
sentatives of online platforms, leading tech companies and players
in the advertising industry (e.g., Facebook, Twitter, Google with
Microsoft and TikTok following) agreed on a self-regulatory Code
of Practice to address the spread of online disinformation [21]. The
Code of Practice is based on 21 commitments in different domains,
including the demonetization of purveyors of disinformation.
A year after its implementation, the Code was already acknowl-
edged globally as a pioneering framework [23]. An assessment of
the Code was published in 2020 [22], showing that (i) the Code did
provide a valuable framework for a structured dialogue between
online platforms, thus, ensuring transparency and accountability
of their policies on disinformation, but also (ii) a set of important
gaps and shortcomings. In June 2022, the Commission issued the
Strengthened Code of Practice on Disinformation (CoP) [19].
In this paper, we set out to explore the impact of the Strength-
ened CoP with regard to one of its most important commitments:
the demonetization of disinformation-spreading websites. We per-
form a historical analysis on misinformation websites in order to
investigate what was the impact of the policy on their ad revenue
by comparing their direct business relationships with ad networks.
The contributions of this work are summarized as follows:
(1) We discover that there is no significant reduction in the
amount of advertising accounts with popular ad networks,
after the Code of Practice on Disinformation came into effect.
Popular ad networks have withdrawn mostly from unpop-
ular disinformation websites, with hardly any visitors. On
the contrary, we find that these ad networks still have con-
nections with popular misinformation websites that account
for the majority of misinformation traffic.
arXiv:2410.11369v2  [cs.CY]  9 Jul 2025

WWW ’25, April 28-May 2, 2025, Sydney, NSW, Australia Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Nicolas Kourtellis, Evangelos Markatos
(2) Two years after the CoP was signed, signatories still accept 1
out of 3 misinformation websites as authorized ad inventory
sellers.
(3) We show that ad networks do not substantially differenti-
ate between unreliable and reliable news websites in their
business relations, and that they form business relationships
with both kinds of websites.
(4) We establish that ad networks still serve ads to almost 400
misinformation websites (from our dataset) and facilitate the
monetization of misinformation content.
(5) We find that ads of 23 Fortune 500 companies are served
next to misinformation content, endangering their brand
reputation and consumer trust.
(6) We make our list of approximately 2,500 misinformation
news websites publicly available [41].
2 Background
When users visit a website, an automated programmatic process
matches them with advertisers. Advertisers rely on Demand-Side
Platforms (DSPs) to target the right users, while website publishers
use Supply-Side Platforms (SSPs) to manage their ad inventory.
ads.txt: Due to the complexity of the advertising ecosystem, bad
actors were able to sell ad inventory of websites they did not control.
To eliminate this, the Internet Advertising Bureau (IAB) Technology
Laboratory introduced the ads.txt specification [33] that allows
publishers to explicitly disclose who is authorized to sell the ad
inventory of their website. This information is enclosed within a
text file, publicly available at the root of the domain (snippet in
Figure 1). Each ads.txt file contains comma-separated records,
with each record authorizing an entity to sell the ad inventory
of the website. Each record contains: (i) the domain name of the
advertising system (e.g., SSP), (ii) an identifier for the seller’s ac-
count, (iii) the type of the account, and optionally (iv) a certification
ID for the advertising system. The type of the account represents
the relationship between the account holder and the ad system. A
DIRECT account suggests that the website publisher also controls
the advertising account and has a direct business contract with
the ad system. For a RESELLER account, the website publisher has
authorized a third-party entity to resell their ad inventory.
sellers.json: To increase transparency in the advertising ecosys-
tem, the IAB Tech Lab also introduced the sellers.json stan-
dard [32]. This standard helps discover the identities of the entities
that sell the ad inventory of websites and can help identify all in-
termediaries involved in ad inventory selling. The sellers.json
standard is implemented as a JSON file published by advertising
systems in order to disclose the inventory sellers they have ap-
proved within their ad system. Each approved seller is represented
by a unique identifier inside this file. This is the same identifier that
appears in the ads.txt file and maps to a single entity that is paid
for the ad inventory it sells (example in Figure 1). Additionally, a
seller type describes each identifier. A PUBLISHER seller suggests
that this account directly owns and controls the website whose ad
inventory is sold through the advertising system, and that the ad-
vertising system directly pays this entity. AnINTERMEDIARY record
indicates that it is a reseller of ad inventory. Finally, a seller can be
labelled as BOTH, acting as both a publisher and an intermediary.
3 Methodology
3.1 Sources of Misinformation
Disinformation is the deliberate creation or spread of false infor-
mation, whereas misinformation is false information shared with-
out necessarily intending to deceive. While we study the Code of
Practice on Disinformation, our focus is on how misinformation
websites generate ad revenue. Proving that there is clear intent to
mislead (i.e., disinformation) is not a trivial task and falls outside the
scope of this work. Nonetheless, some websites in our list have been
labeled as disinformation spreaders (e.g., [15, 16]). We acknowledge
the distinction between these two concepts but argue that under-
standing the business model behind false content is crucial, as many
disinformation campaigns rely on the same advertising mechanisms
as misinformation [52, 53]. The ability to profit from misleading
content encourages bad actors to deliberately spread false claims,
blurring the line between misinformation and disinformation.
To assemble a list of misinformation websites and study their
behavior over time, we make use of publicly available datasets pro-
duced by academic publications, as well as by credible and acclaimed
organizations. Our first source is MediaBias/FactCheck (MBFC) [11],
an organization that investigates bias and misinformation in online
sources of information. By using human evaluators and a concrete
and consistent methodology [13], they evaluate the factual accuracy
of various media sources. We visit the MBFC website in October
2023 and extract labels and information about the bias, factual re-
porting, credibility and traffic volume for each evaluated website.
We retain only websites that have a “LOW CREDIBILITY” score
and a factual reporting of “MIXED”, “LOW” or “VERY LOW”, form-
ing a list of 1,677 misinformation websites. We consciously exclude
websites from the “Satire” category from this analysis, since they
deliberately use humor and exaggeration in their published articles
and do not attempt to deceive visitors. Such websites do not fall
under the misinformation umbrella.
Next, we use the publicly available lists of previous academic
works. We extend our dataset with fake news websites assembled
in [45] consisting of 1,044 misinformation websites. Additionally,
we extract 669 more misinformation sites from [55] that classifies
news websites using independent sources (e.g., Politifact, Snopes).
Finally, we make use of the FakeNewsNet tool used in [ 51] and
download all news articles from the collected dataset. We exclude
all data from the GossipCop fact-checking service because it has
been discontinued and is no longer available. We extract 8 mis-
information websites by filtering websites that have published at
least 4 fake news articles (proven by Politifact [30]). We also filter
out Facebook because we argue that it is neither a news publisher
nor a news aggregator. Misinformation posts on a large platform
shouldn’t label the entire network as misinformation.
We merge all the above lists and end up with a dataset of 2,469
distinct misinformation websites. In an attempt to foster academic
research and give back to the academic community, we make our
list of misinformation websites publicly available [41].
3.2 Fetching ads.txt and sellers.json files
Our study revolves around ads.txt and sellers.json, two im-
portant files in digital advertising that help combat ad fraud and
increase transparency in the advertising ecosystem. Previous work

Before & After: The Effect of EU’s 2022 Code of Practice on Disinformation WWW ’25, April 28-May 2, 2025, Sydney, NSW, Australia
Figure 1: Snippets of Tumblr’s ads.txt
file and Google’s sellers.json file on
April 2024. The ID that describes an ad-
vertising account matches in both files.
0 20 40 60 80 100
% of misinformation websites
openx.com
rhythmone.com
pubmatic.com
indexexchange.com
appnexus.com
rubiconproject.com
aps.amazon.com
lijit.com
google.com
25.4%
28.4%
29.9%
30.6%
30.6%
30.8%
74.8%
81.1%
93.9%
0.7%
-5.4%
0.4%
-2.2%
0.7%
-0.9%
-37.7%
-43.4%
-51.4%
January 2022 January 2024
Figure 2: Direct business relationships
of top ad networks with misinformation
websites over the years.
1K 10K 100K 1M 10M 100M 600M
Network Traffic
0.0
0.2
0.4
0.6
0.8
1.0ECDF
Min: 366
Max: 663M
Median: 7.0K
Figure 3: Distribution of number of visits
of selected misinformation websites on
January 2024 (Note:𝑥-axis is in log scale).
has demonstrated that these files can reveal business relationships
among websites and ad networks [4, 45, 55]. We first study the busi-
ness relationships among ad networks and misinformation websites
and how these have changed over the years and especially after
the Code of Practice on Disinformation was signed. To that extent,
we utilize ads.txt files served by misinformation websites, and
the sellers.json files served by popular ad networks. We crawl
the list of approximately 2,500 misinformation websites on January
2024 and download 226,659 ads.txt entries coming from 1,132
misinformation websites (an ads.txt file of a single website can
contain multiple entries for multiple ad networks [42]). We make
use of an open-source crawler [42] to collect and parse the respec-
tive ads.txt files. We find there are ads.txt records representing
relationships with over 1,100 distinct ad networks, suggesting that
ad networks still work with objectionable websites. To get a better
understanding of the actual business relationships, we direct our
analysis to ads.txt entries marked as DIRECT. The ads.txt speci-
fication defines that DIRECT accounts indicate the website owner
(i.e., publisher) directly controls the advertising account, and that
there is a direct business contract between the publisher and the ad
system [33]. Note that a website may provide bogus information in
its ads.txt file. For example, it may claim that a legitimate adver-
tiser sells ads on this website. On the other hand, an ad seller may
also provide a fake sellers.json file claiming that it can put ads
in high-profile websites to attract more customers. Although each
individual file of the above two files may provide fake information,
their intersection provides the truth. Indeed, if website A (in its
ads.txt file) claims that it displays content from ad network B,and
ad network B (in its sellers.json file) claims that it displays ads
in website A, then this is true. We provide an example in Figure 1.
In the rest of this work we take the intersection of these files. That
is, we form a relation between A and B only if we find this relation
both in ads.txt file of A and in sellers.json file of B.
3.3 Ad Collection
In order to study ads that are actually served on misinformation
websites, as well as the ad networks that serve them, we develop a
fully automated system that visits websites, emulates the behavior
of a real user and clicks on ads.
First, we establish different user profiles (i.e., personas) to emu-
late real users and present a compelling profile to ad networks. We
form different personas emulating different real-world users so that
they receive ads from different advertisers, thus revealing a better
picture of the ad ecosystem around misinformation. Additionally,
we emulate users from various geographic locations in order to
(potentially) get ads from both acclaimed companies and brands
known worldwide, as well as local advertisers. We select Nether-
lands, Greece, and USA as the different vantage points. We choose
two EU countries since the CoP is an EU Commission initiative.
Given its self-regulatory nature and potential differences outside
the EU, we also include the US to identify ad servings that may not
be evident in the EU. We use a VPN service to set the location of
our virtual users, and before we begin forming the personas, we
use two different geolocation services to ensure that these virtual
users indeed appear to be in the specified country. In order to build
a persona, we visit a set of specific websites and expect that third
parties will infer the user’s gender and preferences based on the
content they consume. We describe the methodology we follow to
build user profiles in Appendix A.
After we have built each persona, we use this user profile to
visit the list of misinformation websites. We utilize the open-source
crawler presented in [44] and extend it to cover the needs of this
work. The crawler visits both the landing page and a randomly
selected internal page of each website and detects the advertisers
in these. Prior work has demonstrated that internal pages can have
significant differences in both structure and content (including ads
and trackers) [3]. We extend the crawler to also detect online ads
using cosmetic filters, based on Easylist 1 and uBlock Origin 2, two
of the most popular ad-blocking projects. Additionally, to make
the crawler appear as close to an actual user as possible, we use a
headful browser with custom preferences (e.g., dark color scheme,
window size, etc.). Finally, we make use of Consent-O-Matic [38], a
reliable extension, to automatically accept all cookies in consent
banners and ensure that ads are not blocked because the user has
not interacted with the consent banner. We configure the extension
to automatically accept all data processing purposes.
1https://easylist.to/
2https://ublockorigin.com/

WWW ’25, April 28-May 2, 2025, Sydney, NSW, Australia Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Nicolas Kourtellis, Evangelos Markatos
0 20 40 60 80 100
% of misinformation websites
openx.com
rhythmone.com
pubmatic.com
indexexchange.com
appnexus.com
rubiconproject.com
aps.amazon.com
lijit.com
google.com
70.5%
64.8%
76.1%
77.3%
77.3%
78.4%
65.9%
76.1%
87.5%
-2.3%
-12.5%
-2.3%
-4.5%
4.5%
0.0%
12.5%
0.0%
-4.5%
Popular Misinformation Websites
January 2022 January 2024
Figure 4: Direct business relationships of
top ad networks with popular misinfor-
mation websites over the span of 2 years.
0 20 40 60 80 100
% of misinformation websites
openx.com
rhythmone.com
pubmatic.com
indexexchange.com
appnexus.com
rubiconproject.com
aps.amazon.com
lijit.com
google.com
14.8%
20.2%
19.4%
19.7%
19.4%
19.7%
77.8%
83.2%
95.7%
1.1%
-4.0%
1.1%
-1.7%
0.0%
-1.1%
-49.9%
-54.1%
-63.5%
UNpopular Misinformation Websites
January 2022 January 2024
Figure 5: Direct business relationships of
top ad networks with unpopular misin-
formation websites after 2 years.
20% 40% 60% 80% 100%
Website Popularity
0
20
40
60
80
100
Decrease in advertisement for Google
between 2021 and 2024
T op 20% most
popular
misinformation
websites
Bottom 20% of
misinformation websites
Figure 6: Difference in misinformation
websites working with Google based on
website network traffic.
4 Regulation Impact
We set out to explore if the Strengthened Code of Practice on Dis-
information has had a meaningful impact on the monetization of
misinformation content. We expect that the ecosystem will be im-
proving because multiple signatories have committed to cutting
the advertising revenue of disinformation spreaders [19]. Inspired
by prior work [45], we study how direct business relationships of
misinformation websites with ad networks have evolved over time.
We utilize the dataset of ads.txt and sellers.json files de-
scribed in Section 3.2, as well as the one collected in [45] for news
websites in December 2021. Arguably, publishers of fake news con-
tent could easily lie in their ads.txt files [42, 55]. To discover the
actual business relationships, we focus on information coming from
both the publishers and the ad systems. That is, we cross-reference
the claims that publishers make in their ads.txt files with those
of trustworthy ad networks in sellers.json files. We argue that
since these are conflicting sides of the same coin, the intersec-
tion of their claims is the ground truth. For each distinct DIRECT
ads.txt entry, we review whether the respective publisher ID is
also disclosed by the respective ad network. For instance, if exam-
plefakenews.com has the entry adnetwork.com, 12345, DIRECT
in its ads.txt file, we confirm thatadnetwork.com also discloses the
identifier 12345 in its sellers.json file. Again, we focus only on
ads.txt records labeled as DIRECT because they indicate a direct
business contract between the misinformation publisher and the
advertising system. First, we study the behavior of the top ad net-
works and how their business relationships with misinformation
websites have evolved over a period of 2 years. We focus on the
intersection of these datasets and find that there exist 461 misinfor-
mation websites with an ads.txt file in both datasets and with at
least one business relationship also disclosed by the respective ad
network. We plot our findings in Figure 2.
At first glance, most ad networks (as of January 2024) still work
with misinformation websites, with only minor reductions. 6 out
of the 9 most popular ad networks (i.e., rubiconproject.com to
openx.com in Figure 2) have only blocked a very small percentage
of misinformation websites (i.e., up to 5.4%). However, some ad sys-
tems, including Google, Lijit, and Amazon, have stopped working
with a significant portion of misinformation sites, dropping 51%,
43%, and 37%, respectively, compared to two years ago. While the
drop in ad network relationships with misinformation websites
aligns with the CoP, these websites represent a small fraction of to-
tal misinformation traffic. To explore this, we use SimilarWeb [34] to
gather traffic data for 95% of the misinformation websites for which
we have collected their ads.txt files, before and after the CoP. In
Figure 3, we plot the distribution of their network traffic (number
of visits on desktop and mobile) in January 2024. The𝑥-axis is in
logarithmic scale, suggesting that there exist a lot of misinformation
websites with low network traffic and a few highly popular that are
able to attract millions of monthly visitors. We split these websites
on the 80th percentile based on the observation that the top 20% are
popular websites, while the rest are unpopular.3 The 80th percentile
corresponds to a network traffic of approximately 290K monthly
visits. Consequently, we find 88 misinformation websites which we
label as “popular”, and 351 labeled as “unpopular”.
We replicate the analysis from Figure 2 to track the evolution
of ad network relationships with popular and unpopular misinfor-
mation sites in Figures 4 and 5, respectively. These figures paint a
clear picture of the ad ecosystem. Even though it seems that some
ad networks no longer work with misinformation websites, they do
so only for the unpopular ones. Some of these websites have hardly
any visitors and their effect on the dissemination of misinformation
is limited, deeming them potentially insignificant. However, for
high-traffic misinformation sites attracting millions of visits, ad
networks continue to partner with them, even a year and half after
the CoP was signed (Figure 4). Some top networks have severed ties
with a small portion of the most popular misinformation websites,
while others, like Amazon and Microsoft (AppNexus), now work
with more popular misinformation websites than two years ago.
To further support our finding, we explore how business rela-
tionships with misinformation websites have been affected based
on their popularity. As a case study, we focus on Google, the most
popular ad network [42]. We group misinformation websites into
equal-sized buckets based on their monthly traffic in January 2024.
To validate these business relationships, we cross-reference them
with Google’s sellers.json accounts, only reporting those that
match. We then compute the difference in misinformation websites
3The split 80-20 could have been made as 85-15, or 75-25. The point here is not to
define an optimal threshold, but to create two categories: the “popular” misinformation
websites and the “unpopular” ones.

Before & After: The Effect of EU’s 2022 Code of Practice on Disinformation WWW ’25, April 28-May 2, 2025, Sydney, NSW, Australia
google.comlijit.com appnexus.compubmatic.comaps.amazon.com
Ad Networks
0
10
20
30
40
50
60Number of misinformation websites
50
58
36 38
22 20 19 18 18 22
January 2022
January 2024
Figure 7: Evolution of popular misin-
formation websites explicitly stated in
sellers.json files of popular ad net-
works.
0 25 50 75 100 125 150 175 200
Number of directly related Ad Networks
0.0
0.2
0.4
0.6
0.8
1.0ECDF
Min: 1
Max: 196
Median: 1.0 Mean: 10.48
Figure 8: Distribution of the number of
direct business relationships between
a misinformation website and ad net-
works.
0 200 400 600
Number of websites
smartadserver.com
onetag.com
sonobi.com
conversantmedia.com
video.unrulymedia.com
amxrtb.com
openx.com
indexexchange.com
rubiconproject.com
appnexus.com
pubmatic.com
aps.amazon.com
lijit.com
google.com
udmserve.net
175
175
176
180
186
190
205
214
227
234
235
270
279
408
603
Signatory
Non Signatory
0 20 40 60
% of websites
16.9%
16.9%
17.0%
17.3%
17.9%
18.3%
19.7%
20.6%
21.9%
22.5%
22.6%
26.0%
26.9%
39.3%
58.1%
Figure 9: Direct business contracts with
misinformation websites on July 2024
based on ads.txt and sellers.json. Red
bars represent CoP signatories [20].
Ad Network Websites Spearman p-value Minimal
google.com 502 0.64 5.021135e-57 -72.62%
lijit.com 429 0.63 1.333227e-47 -73.57%
aps.amazon.com 415 0.64 8.267313e-48 -75.28%
Table 1: Correlation between misinformation websites traffic
and progress of direct ad networks business contracts. The
last column shows the percentage of low-traffic websites that
no longer have business relationships after 2 years.
working with Google between December 2021 and January 2024.
We express this difference as a percentage decrease𝐷 = 𝐵−𝐴 |𝐵| · 100,
where𝐴 (i.e., After) is the number of misinformation websites hav-
ing a direct business relationship with Google on 2024/01, and𝐵
(i.e., Before) is for 2022/01. Our findings, shown in Figure 6, reveal
a significant drop in verified accounts for less popular websites
(left-most bar of the plot), with 96% of websites ranked in the bot-
tom 20% based on traffic, no longer having a contract with Google.
On the other hand, we observe almost no difference for popular
misinformation websites (i.e., right-most bar of the plot). Thus, we
observe a discrepancy on how popular misinformation websites
are treated, compared to unpopular ones.
Building on Figure 6, we examine the correlation between a mis-
information website’s network traffic and whether an ad network
stops working with it. We make use of the traffic labels that MBFC
assigns to news websites (“Minimal”, “Low”, “Medium” or “High”).
MBFC estimates traffic data through the SimilarWeb platform, but
also takes into consideration the number of subscribers for print
media and market size for TV/Radio entities [13]. We focus on the
ad networks of Figure 2 that showed the greatest decrease in mis-
information websites. We find a correlation between the network
traffic of a misinformation website and if it declares a business con-
tract with an ad network after two years. We present our findings
in Table 1, with a Spearman correlation coefficient of∼0.6 and a
𝑝-value close to zero. Over 70% of misinformation websites with
minimal network traffic no longer have a business relationship with
these ad networks after two years. We study how the popularity of
misinformation websites has changed over time in Appendix B.
Recent work has demonstrated that misinformation websites
often use dark pooling in order to pool their ad inventory with
that of lawful and acceptable websites [42, 55, 56]. In an attempt
to prove explicit relationships between popular misinformation
websites and popular ad networks, we study their sellers.json
files. In Figure 7, we plot the number of misinformation websites
from our list of∼2,500 misinformation websites that are explicitly
stated inside sellers.json files of popular ad systems. This is a
definitive proof that ad networks still fund misinformation websites
because they explicitly name them as verified ad inventory sellers.
We observe that the number of misinformation websites explic-
itly disclosed in the sellers.json files of the most prestigious
and popular ad networks is somewhat stable. It is evident that the
behavior of the top ad networks has not changed significantly over
the last two years, even after the Code of Practice on Disinformation
was signed. In fact, studying the standard deviation of the number
of popular misinformation websites in sellers.json files (less
than 2.5) shows that almost all networks have not stopped doing
business with the misinformation websites. We provide examples
of such relationships in Appendix C.
Finding 1: Major ad networks still accept business relationships
with misinformation websites, which account for the majority
of the misinformation traffic. After the CoP, these ad networks
have ceased their collaboration mainly with the unpopular mis-
information websites.
5 Financial Incentives
The analysis of Section 4 suggests that misinformation websites
still rely on popular ad networks to monetize their content. We
cross-reference the accounts declared in ads.txt files with those
found in sellers.json ad networks, just like in Section 4 and find
that there exist 985 (87%) misinformation websites with at least one
substantiated business relationship with an ad network. That is,
for 985 misinformation websites, there exists an ad network that
confirms the publisher account exists within its network and that
it indeed belongs to a publisher. This demonstrates that misinfor-
mation websites are still able to get approved by ad networks and
monetize their content through ad revenue.
5.1 Direct Business Relationships
We set out to explore what is the state of the advertising ecosystem
two years after the Strengthened CoP was signed. We collect the

WWW ’25, April 28-May 2, 2025, Sydney, NSW, Australia Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Nicolas Kourtellis, Evangelos Markatos
0 500 1000 1500
Number of websites
adyoulike.com
teads.tv
video.unrulymedia.com
onetag.com
triplelift.com
smartadserver.com
openx.com
udmserve.net
indexexchange.com
pubmatic.com
appnexus.com
rubiconproject.com
lijit.com
aps.amazon.com
google.com
503
554
566
604
627
634
688
694
710
790
791
809
813
825
1478
Non Signatory
Signatory
0 20 40 60
% of websites
22.1%
24.4%
24.9%
26.6%
27.6%
27.9%
30.3%
30.6%
31.3%
34.8%
34.8%
35.6%
35.8%
36.3%
65.1%
Figure 10: Direct business relationships with the most un-
reliable websites in July 2024 based on both ads.txt and
sellers.json files.
Least reliable
Generally unreliableLimited reliabilityGenerally reliable Most reliable
0
20
40
60
80
100
% of misinformation websites
with direct business contracts
88.9
45.4
73.4
88.1 88.7
42.1
28.9
59.3
75.0 74.3
19.0
10.2
23.1
28.4 25.5
google.com appnexus.com xandr.com
Figure 11: Business relationships among signatories of the CoP
and news websites of various credibility ratings.
ads.txt files of misinformation websites and the sellers.json
files of ad networks on July 2024. We plot in Figure 8 the number
of direct business relationships among misinformation websites
and ad networks. These relationships are extracted based on the
ad accounts that both publishers and ad networks agree are valid
through ads.txt and sellers.json files, respectively. We observe
that the majority of misinformation websites have a direct contract
with only a handful of ad networks. However, there exist misin-
formation websites that form business contracts with tens or even
hundreds of ad networks. One such example is the website wha-
treallyhappened.com. This website serves an ads.txt file of over
8500 lines that contains verified DIRECT entries for 196 distinct
ad networks. In fact, the identifiers in this file are organized and
labeled accordingly, indicating the presence of (dark) pools [42, 55].
Next, we plot in Figure 9 the direct business relationships of top
ad networks with misinformation websites. We observe that for
most ad networks, the behavior is similar; they have a DIRECT
business relationship with about 16.9%-58.1% of misinformation
websites whose ads.txt files we were able to obtain. Even though
these values might seem small, the underlying implications are
significant. They indicate that the most popular ad networks have a
direct business contract with a large percentage of misinformation
websites, and that they facilitate the proliferation of misinformation
content through ad revenue. In fact, event the smallest value in
Figure 9 suggests that ad networks have authorized at least 1 out
of 5 misinformation websites that serve an ads.txt file. The two
ad systems that stand out are Google, and Underdog Media that
controls udmserve.net. These ad networks directly partner with
400+ misinformation websites according to their sellers.json
files. Even though their own guidelines prohibit monetizing false
content [26, 36], they fail to filter out all such websites. Altogether,
there are hundreds of misinformation websites that still have direct
business relationships with legitimate and popular ad networks and
are able to generate revenue from dis-/mis-information content.
The accounts used to sell the ad inventory of these websites are
recognized by popular ad networks.
Finding 2: To this day, the most popular ad networks still
have documented business relationships with over 500 distinct
misinformation websites. Ad networks that have signed the
CoP have approved as ad inventory sellers more than 1 out of 3
misinformation websites that serve an ads.txt file.
5.2 News Websites Credibility
To further support our finding that ad networks still work with
misinformation websites to a large extent, we utilize the Science
Feedback dataset on news websites credibility [25]. The researchers
behind this dataset have accumulated a list of over 20K news web-
sites from more than 100 countries. For each news website they
assign a score reflecting its credibility, aggregating pre-existing
and publicly available evaluations from trustworthy entities (i.e.,
academic researchers, fact-checking organizations, expert raters).
We access the original list and successfully fetch the ads.txt
files of∼7K news websites in July 2024. We perform a similar anal-
ysis as described earlier, but here, we make use of the list’s original
classification system and focus on websites labeled as “Generally
unreliable” and “Least reliable”. We are able to extract 2,459 un-
reliable news websites with at least one DIRECT record in their
ads.txt files and present our findings in Figure 10. We discover a
similar behavior with our previous findings. Popular and legitimate
ad networks have a direct business contract with hundreds of unre-
liable news websites, and this relationship is recognized by both
the websites and ad networks. Finally, in Figure 11 we focus on the
signatories of the Code of Practice on Disinformation and explore
their direct business relationships with news websites of various
credibility scores. We find that these ad networks work with all
news websites and do not seem to have a distinctively different
policy for unreliable news websites. In the case of Google, we find
that it works with almost as many of the least reliable websites
(percentage wise) as with the most reliable.
Finding 3: Two years after the Strengthened Code of Practice on
Disinformation was signed, even the ad networks that signed
the CoP do not considerably distinguish between unreliable
and reliable news sources, allowing publishers to generate ad
revenue from false claims.

Before & After: The Effect of EU’s 2022 Code of Practice on Disinformation WWW ’25, April 28-May 2, 2025, Sydney, NSW, Australia
Entity % misinformation # misinformation
websites websites
Google LLC 69.39% 272
RevContent, LLC 20.66% 81
AdRoll, Inc. 12.50% 49
RTB House S.A. 12.50% 49
Microsoft Corporation 8.93% 35
Criteo SA 7.91% 31
MGID Inc 7.14% 28
Taboola, Inc. 6.12% 24
Zeta Global 5.87% 23
Outbrain 5.61% 22
Table 2: Ad network operators serving programmatic ads to
misinformation websites. Even though Google and Microsoft
have signed the CoP, they still deliver ads, and therefore
revenue, to misinformation websites.
6 Served Advertisements
In previous sections, we demonstrate that the most popular ad
networks still have business relationships with misinformation
websites, and that the CoP did not have a substantial impact on the
monetization of misinformation. To validate our observations, we
study ads that are actually served on misinformation websites. Our
goal is to explore to what extent ad networks still monetize misin-
formation content and if reputable advertisers might end up next
to misinformation content. This analysis follows the methodology
described in Section 3.3. Since misinformation websites are short-
lived [10], we focus only on active ones, detailed in Appendix D.
6.1 Ad Networks
Using data coming from 6 distinct user profiles (2 genders and 3
countries) and one clean user profile, we detect ads from 2,480 adver-
tisers in 392 misinformation websites. We attribute the large number
of distinct advertisers to the use of different vantage points (i.e., 3
geographic locations), thus being served ads from local brands.
First, we study the ad networks that deliver ads to misinforma-
tion websites. We achieve this by studying the ad URLs the crawler
detected. We analyze these ad URLs and extract the domain from
them, grouping them on the eTLD+1 level. For example, ads served
by adclick.g.doubleclick.net and googleads.g.doubleclick.net are all
grouped under the doubleclick.net domain. To uncover the actual
entities serving ads, we group domains based on the companies
that own these domains. For example, ads served by doubleclick.net
and googleadservices.com are all attributed to Google LLC. To iden-
tify entities that operate each domain, we utilize the DuckDuckGo
Tracker Radar dataset [24]. We recognize that ad inventory (re)sales
may involve intermediaries, but this is beyond the scope of this
work. We summarize our findings in Table 2.
We find that there are a lot of legitimate and popular ad networks
that still deliver ads to misinformation websites. Google is the most
prominent ad facilitator of misinformation websites, serving ads to
69% of the misinformation websites that contained ads. The second
most popular ad network that serves ads to misinformation web-
sites is RevContent, known to be popular among misinformation
websites [27, 45]. Unfortunately, we find that ads are served on
misinformation websites even by entities that have signed the Code
of Practice on Disinformation (e.g., Google and Microsoft) [ 20],
suggesting that there is still work to be done.
It is important to mention that these findings highlight the issue
described in previous sections with the analysis of ads.txt and
sellers.json files. Ad networks may claim they once allowed
misinformation websites (i.e., findings of previous sections) but
later blocked them. Our analysis proves some still partner with
misinformation publishers, serving ads and funding them.
To make matters worse, we discover ad networks serving misin-
formation ads. For example, when our USA-based female persona
visited the website theconservativebried.com, Google served an ad
for goop.com, a website linked to pseudoscience and failed fact-
check [12]. We observe similar behavior with Outbrain, RevContent
and Yandex LLC. Evidently, ad networks do not properly review
the content they promote, thus disseminating misinformation. The
CoP explicitly states that signatories (such as Google) should work
towards stopping ads that contain false claims (Commitment 2:
“TACKLING ADVERTISING CONTAINING DISINFORMATION”).
All the above suggest that even though the CoP is a step towards the
right direction, more effort is required to tackle the monetization
and propagation of online misinformation.
Finding 4: We discover that the most popular ad networks do
not closely examine their ad placements. They still serve ads,
and thus ad revenue, to almost 400 misinformation websites.
Google and Microsoft, signatories of the CoP, place ads in 70%
and 9% (resp.) of misinformation websites in our dataset.
6.2 Brand Safety of Advertisers
Next, we analyze the actual advertisers that appear within the mis-
information context. We utilize the dataset of the previous section,
but now focus on the landing pages users arrive when they click
on ads displayed on misinformation websites. We find that there
exist a lot of advertisers whose ads are placed in dozens of different
misinformation websites. This behavior is consistent for various
types of ads and for all personas. For example, using the USA-based
female persona, we find thatjjshouse.com, a popular online store for
wedding dresses, was advertised in 80 distinct misinformation web-
sites. Similarly, the Greece-based male persona was served ads from
Temu in 86 distinct misinformation websites (22%) while ads from
overnightglasses.com were served to the male US-based user in 59
distinct misinformation websites. We should note that this finding
is not a finger pointing exercise for these advertisers and does not
indicate that these advertisers choose to appear in misinformation
websites. Most likely, these ads are placed next to misinformation
because of the ad network believing they are of interest to the vir-
tual user. However, we should note that this can have a big impact
on advertisers (i.e., brand safety) if visitors associate misinformation
content with specific services or products.
Finally, we analyze the significance of the advertisers found in
misinformation websites. To our surprise, we find ads from very
reputable companies appearing in misinformation websites. We
provide screenshots of examples [41]. We find 23 Fortune 500 com-
panies advertising in misinformation websites, threatening their
reputation and consumer trust due to negative brand associations.
Finding 5: Ads from very popular and renowned brands (even
from 23 of the largest companies in the world) are served in
misinformation websites. Users can see an ad of a specific brand
in up to 86 distinct misinformation websites.

WWW ’25, April 28-May 2, 2025, Sydney, NSW, Australia Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Nicolas Kourtellis, Evangelos Markatos
7 Related Work
The monetization of misinformation content through online ads has
been thoroughly studied. In fact, in [54], authors performed a cost-
based analysis on fake news interventions and proposed a model
that can help combat the proliferation of misinformation websites.
In [7], authors studied fake news and low-quality news websites
and found that fake news publishers monetize their content using
reliable ad servers. Similarly, in [9], authors studied the monetiza-
tion schemes of misinformation websites, focusing on anti-vaccine
pages, demonstrating they mainly rely on ads. In [ 10], authors
found that some popular third-party services have higher presence
in fake news sites compared to real news. In [27], expanded upon
this finding and found that misinformation websites rely on pop-
ular Web services such as Cloudflare, Google and RevContent to
host and monetize their content. This behavior is leveraged by [46],
where authors proposed a content-agnostic fake news detection
service using network and structural characteristics (including re-
quests towards third-party advertising services), and [28], authors
utilized non-perceptual features (e.g., domain name, DNS config)
to train a multi-class model that detects disinformation websites.
Regarding the ads.txt and sellers.json standards that are
the foundation of our methodology, in [ 4], authors performed a
longitudinal study of ads.txt files and their adoption. In [ 55],
authors also measured the compliance of the ad ecosystem with
ad standards and explored how publishers use ads.txt files to
form dark pools, a way to circumvent restrictions and monetize
misinformation content. Similarly, in [42], authors further explored
dark pooling along with hidden intermediaries and highlighted the
importance of limiting the ad revenue generated by misinformation
publishers. In [56], authors demonstrated that dark pooling can be
diminished by notifying stakeholders and ad networks. In this work,
we expand the methodology and make use of the dataset presented
in [45], where authors processed ads.txt and sellers.json files
to study the business relationships between fake news websites
and ad networks. They discovered that fake news websites rely on
popular and credible ad networks to generate revenue.
Previous work has examined the content of ads served on misin-
formation websites, finding that nearly half of the ads were prob-
lematic [57] and that some advertisers tolerate fake news websites
due to lower costs [8]. In this work, we mainly focus on the ad net-
works responsible for serving ads on misinformation websites and
only briefly examine the advertisers to discuss brand safety. Brand
safety has been more extensively studied in [ 2], where authors
demonstrated that ads largely finance misinformation websites and
that can have a great effect on advertisers’ brand safety. Previous
work has also studied how questionable content affects the brand
of pre-roll advertisers [5] and advertisers that utilize programmatic
advertising [50], and how reputable brands can appear next to illicit
content, unbeknownst to them [43].
8 Discussion & Conclusion
8.1 Discussion
The Strengthened Code of Practice on Disinformation is a step
towards the right direction, but more work is needed. This study
doesn’t aim to discredit the CoP but to stress the need for bet-
ter scrutiny of ad placements and more misinformation websites
marked ineligible for monetization. We believe ad networks must
ensure misinformation is no longer profitable, preventing even pop-
ular websites from surviving on ad revenue. Reducing financial
incentives for misinformation can improve information quality and
trust in factual reporting. Although the self-regulatory nature of
the CoP is promising, its adoption is limited, with only 44 signa-
tories as of July 2024. It is evident that current signatories have
been laying the foundation, but we hope new signatories from the
online ad ecosystem (i.e., ad networks) will take initiative for more
substantial actions.
It is customary in such studies to have a control group, that is, a
set of non-disinformation websites and study what is the change
in advertisements in these websites as well. Such a control group
enables researchers to argue whether a change they see in misinfor-
mation websites is due to the CoP. However, this is not needed for
this work. Indeed, we are not interested in attributing any changes
we see to the CoP (or not). The goal of this work is to discover if
the change that the CoP expected (i.e., that disinformation websites
will not have ads) happened and to what extent.
Finally, we acknowledge the argument that some ad networks
might still work with misinformation websites because they classify
these websites as serving “low credibility content” rather than
deliberate disinformation. Classifying a website as misinformation
or not falls outside the scope of this work. We rely on external
sources (e.g., MBFC, ScienceFeedback) that work on this exact topic
and the academic community has already reviewed their reliability.
8.2 Conclusion
The Strengthened Code of Practice on Disinformation was signed in
June 2022, in an attempt to fight disinformation in a self-regulatory
manner. The first commitment of the CoP is that entities involved
in ad placements demonetize dissemination of disinformation. The
expectation is that since the CoP was signed by leading industry
players (e.g., Google and Microsoft), two years after the introduc-
tion of the strengthened CoP, things will have improved. In this
work, we perform a historical analysis and demonstrate that this
is not the case. In fact, misinformation websites are still able to
retain business contracts with popular ad networks and monetize
their content. We show that the adoption of the Code of Practice
for Disinformation has not made a significant impact on the misin-
formation ecosystem, and that ad networks stopped working with
only insignificant misinformation websites that do not have a lot
of visitors. Finally, we perform a dynamic analysis of ads served
on misinformation websites. We establish that not only popular ad
networks still facilitate the monetization of the majority of misin-
formation websites, but that they also serve ads of respectable and
popular brands next to misinformation content.
Acknowledgments
Funded by the European Union. Views and opinions expressed
are however those of the author(s) only and do not necessarily
reflect those of the European Union or European Research Execu-
tive Agency (REA). Neither the European Union nor the granting
authority can be held responsible for them.

Before & After: The Effect of EU’s 2022 Code of Practice on Disinformation WWW ’25, April 28-May 2, 2025, Sydney, NSW, Australia
References
[1] Pushkal Agarwal, Sagar Joglekar, Panagiotis Papadopoulos, Nishanth Sastry, and
Nicolas Kourtellis. 2020. Stop Tracking Me Bro! Differential Tracking of User
Demographics on Hyper-Partisan Websites. InProceedings of The Web Conference
2020 (Taipei, Taiwan) (WWW ’20). Association for Computing Machinery, New
York, NY, USA, 1479–1490. https://doi .org/10.1145/3366423.3380221
[2] Wajeeha Ahmad, Ananya Sen, Charles Eesley, and Erik Brynjolfsson. 2024. Com-
panies inadvertently fund online misinformation despite consumer backlash.
Nature 630, 8015 (2024), 123–131.
[3] Waqar Aqeel, Balakrishnan Chandrasekaran, Anja Feldmann, and Bruce M.
Maggs. 2020. On Landing and Internal Web Pages: The Strange Case of Jekyll
and Hyde in Web Performance Measurement. In Proceedings of the ACM In-
ternet Measurement Conference (Virtual Event, USA) (IMC ’20). Association for
Computing Machinery, New York, NY, USA, 680–695. https://doi .org/10.1145/
3419394.3423626
[4] Muhammad Ahmad Bashir, Sajjad Arshad, Engin Kirda, William Robertson,
and Christo Wilson. 2019. A Longitudinal Analysis of the ads.txt Standard. In
Proceedings of the Internet Measurement Conference (Amsterdam, Netherlands)
(IMC ’19). Association for Computing Machinery, New York, NY, USA, 294–307.
https://doi.org/10.1145/3355369.3355603
[5] Steven Bellman, Ziad HS Abdelmoety, Jamie Murphy, Shruthi Arismendez, and
Duane Varan. 2018. Brand safety: the effects of controversial video content on
pre-roll advertising. Heliyon 4, 12 (2018), e01041.
[6] Alexandre Bovet and Hernán A Makse. 2019. Influence of fake news in Twitter
during the 2016 US presidential election. Nature communications 10, 1 (2019), 7.
[7] Lia Bozarth and Ceren Budak. 2021. Market Forces: Quantifying the Role of Top
Credible Ad Servers in the Fake News Ecosystem. Proceedings of the International
AAAI Conference on Web and Social Media 15, 83–94. https://doi .org/10.1609/
icwsm.v15i1.18043
[8] Joshua A Braun and Jessica L Eklund. 2019. Fake news, real money: Ad tech
platforms, profit-driven hoaxes, and the business of journalism.Digital Journalism
7, 1 (2019), 1–21.
[9] David A. Broniatowski, Kevin T. Greene, Nilima Pisharody, Daniel J. Rogers, and
Jacob N. Shapiro. 2023. Measuring the monetization strategies of websites with
application to pro- and anti-vaccine communities. Scientific Reports 13, 1 (Sept.
2023). https://doi .org/10.1038/s41598-023-43061-6
[10] Manolis Chalkiadakis, Alexandros Kornilakis, Panagiotis Papadopoulos, Evange-
los Markatos, and Nicolas Kourtellis. 2021. The Rise and Fall of Fake News Sites: A
Traffic Analysis. In Proceedings of the 13th ACM Web Science Conference 2021 (Vir-
tual Event, United Kingdom) (WebSci ’21). Association for Computing Machinery,
New York, NY, USA, 168–177. https://doi .org/10.1145/3447535.3462510
[11] Media Bias/Fact Check. 2023. Search and Learn the Bias of News Media. https:
//mediabiasfactcheck.com/.
[12] Media Bias/Fact Check. 2024. Goop – Bias and Credibility. https://
mediabiasfactcheck.com/goop/.
[13] Media Bias/Fact Check. 2024. Methodology. https://mediabiasfactcheck .com/
methodology/.
[14] Media Bias/Fact Check. 2024. One America News Network – Bias and Credibility.
https://mediabiasfactcheck.com/one-america-news-network/.
[15] Media Bias/Fact Check. 2024. Trending Politics – Bias and Credibility. https:
//mediabiasfactcheck.com/trending-politics/.
[16] Media Bias/Fact Check. 2024. War Room (Steve Bannon) – Bias and Credibility.
https://mediabiasfactcheck.com/war-room-steve-bannon-bias/.
[17] Media Bias/Fact Check. 2024. World Lifestyle – Bias and Credibility. https:
//mediabiasfactcheck.com/world-lifestyle-bias/.
[18] Yong CHIM, Stéphanie CHEVAL, Sonia BARITELLO, Catalina Marchant de Abreu,
and Nadia MASSIH. 2023. Israel-Hamas, the media war: How to verify informa-
tion? https://www.france24.com/en/tv-shows/middle-east-matters/20231018-
israel-hamas-the-media-war-how-to-verify-information.
[19] European Comission. 2022. The 2022 Code of Practice on Disinformation. https:
//digital-strategy.ec.europa.eu/en/policies/code-practice-disinformation.
[20] European Comission. 2022. Signatories of the 2022 Strengthened Code of Practice
on Disinformation. https://digital-strategy.ec.europa.eu/en/library/signatories-
2022-strengthened-code-practice-disinformation.
[21] European Commission. 2018. 2018 Code of Practice on Disinformation. https:
//digital-strategy.ec.europa.eu/en/library/2018-code-practice-disinformation.
[22] European Commission. 2020. Assessment of the Code of Practice on
Disinformation – Achievements and areas for further improvement.
https://digital-strategy.ec.europa.eu/en/library/assessment-code-practice-
disinformation-achievements-and-areas-further-improvement.
[23] European Commission. 2020. Disinformation: EU assesses the Code of
Practice and publishes platform reports on coronavirus related disinforma-
tion. https://digital-strategy.ec.europa.eu/en/news/disinformation-eu-assesses-
code-practice-and-publishes-platform-reports-coronavirus-related.
[24] DuckDuckGo. 2024. Tracker Radar. https://github .com/duckduckgo/tracker-
radar.
[25] Science Feedback. 2023. Consensus Credibility Scores: A Comprehensive Dataset
of Web Domains’ Credibility. https://science.feedback.org/consensus-credibility-
scores-comprehensive-dataset-web-domains-credibility/.
[26] Google. 2024. Publisher Policies. https://support.google.com/adsense/answer/
10502938.
[27] Catherine Han, Deepak Kumar, and Zakir Durumeric. 2022. On the Infrastructure
Providers That Support Misinformation Websites.Proceedings of the International
AAAI Conference on Web and Social Media 16, 287–298. https://doi .org/10.1609/
icwsm.v16i1.19292
[28] Austin Hounsel, Jordan Holland, Ben Kaiser, Kevin Borgolte, Nick Feamster, and
Jonathan Mayer. 2020. Identifying disinformation websites using infrastructure
features. In 10th USENIX Workshop on Free and Open Communications on the
Internet (FOCI).
[29] Google News Initiative. 2022. Digital News Innovation Fund Impact Report.
https://newsinitiative.withgoogle.com/en-gb/impact/.
[30] Poynter Institute. 2023. PolitiFact: a fact-checking website that rates the ac-
curacy of claims by elected officials and others on its Truth-O-Meter. https:
//www.politifact.com/.
[31] Irina Khaldarova and Mervi Pantti. 2020. Fake news: The narrative battle over the
Ukrainian conflict. In The Future of Journalism: Risks, Threats and Opportunities .
Routledge, 228–238.
[32] IAB Technology Laboratory. 2019. sellers.json Specification. https://
iabtechlab.com/wp-content/uploads/2019/07/Sellers.json_Final.pdf.
[33] IAB Technology Laboratory. 2022. ads.txt Specification Version 1.1. https://
iabtechlab.com/wp-content/uploads/2022/04/Ads.txt-1.1.pdf.
[34] Similarweb LTD. 2023. Website Traffic - Check and Analyze Any Website. https:
//www.similarweb.com/.
[35] Hannah Marshall and Alena Drieschova. 2018. Post-truth politics in the UK’s
Brexit referendum. New Perspectives 26, 3 (2018), 89–105.
[36] Underdog Media. 2024. Publisher Guidelines. https://underdogmedia .com/
signup/.
[37] Microsoft. 2024. Playwright. https://playwright .dev/.
[38] Midas Nouwens, Rolf Bagge, Janus Bager Kristensen, and Clemens Nylandsted
Klokmose. 2022. Consent-O-Matic: Automatically Answering Consent Pop-
ups Using Adversarial Interoperability. In Extended Abstracts of the 2022 CHI
Conference on Human Factors in Computing Systems (New Orleans, LA, USA)(CHI
EA ’22). Association for Computing Machinery, New York, NY, USA, Article 238,
7 pages. https://doi .org/10.1145/3491101.3519683
[39] Katherine Ognyanova, David Lazer, Ronald E Robertson, and Christo Wilson.
2020. Misinformation in action: Fake news exposure is linked to lower trust in
media, higher trust in government when your side is in power. Harvard Kennedy
School Misinformation Review (2020).
[40] Michalis Pachilakis, Panagiotis Papadopoulos, Nikolaos Laoutaris, Evangelos P.
Markatos, and Nicolas Kourtellis. 2022. YourAdvalue: Measuring Advertising
Price Dynamics without Bankrupting User Privacy. In Abstract Proceedings of the
2022 ACM SIGMETRICS/IFIP PERFORMANCE Joint International Conference on
Measurement and Modeling of Computer Systems (Mumbai, India) (SIGMETRIC-
S/PERFORMANCE ’22). Association for Computing Machinery, New York, NY,
USA, 41–42. https://doi .org/10.1145/3489048.3522629
[41] Emmanouil Papadogiannakis. 2024. Open-source Data. https://gitlab .com/
papamano/before-after-data.
[42] Emmanouil Papadogiannakis, Nicolas Kourtellis, Panagiotis Papadopoulos, and
Evangelos Markatos. 2025. Welcome to the Dark Side: Analyzing the Revenue
Flows of Fraud in the Online Ad Ecosystem. (2025). https://doi .org/10.1145/
3696410.3714899
[43] Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Evangelos P. Markatos,
and Nicolas Kourtellis. 2024. Ad Laundering: How Websites Deceive Advertisers
into Rendering Ads Next to Illicit Content. In Companion Proceedings of the
ACM Web Conference 2024 (Singapore, Singapore) (WWW ’24). Association for
Computing Machinery, New York, NY, USA, 782–785. https://doi .org/10.1145/
3589335.3651466
[44] Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Evangelos P. Markatos,
and Nicolas Kourtellis. 2022. Leveraging Google’s Publisher-Specific IDs to Detect
Website Administration. In Proceedings of the ACM Web Conference 2022 (Virtual
Event, Lyon, France) (WWW ’22). Association for Computing Machinery, New
York, NY, USA, 2522–2531. https://doi .org/10.1145/3485447.3512124
[45] Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Evangelos P. Markatos,
and Nicolas Kourtellis. 2023. Who Funds Misinformation? A Systematic Analy-
sis of the Ad-Related Profit Routines of Fake News Sites. In Proceedings of the
ACM Web Conference 2023 (Austin, TX, USA) (WWW ’23). Association for Com-
puting Machinery, New York, NY, USA, 2765–2776. https://doi .org/10.1145/
3543507.3583443
[46] Panagiotis Papadopoulos, Dimitris Spythouris, Evangelos P Markatos, and Nicolas
Kourtellis. 2023. FNDaaS: Content-agnostic Detection of Websites Distributing
Fake News. In 2023 IEEE International Conference on Big Data (BigData) . IEEE,
1438–1449.
[47] Yasmim Mendes Rocha, Gabriel Acácio de Moura, Gabriel Alves Desidério, Car-
los Henrique de Oliveira, Francisco Dantas Lourenço, and Larissa Deadame de

WWW ’25, April 28-May 2, 2025, Sydney, NSW, Australia Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Nicolas Kourtellis, Evangelos Markatos
Figueiredo Nicolete. 2021. The impact of fake news on social media and its influ-
ence on health during the COVID-19 pandemic: A systematic review. Journal of
Public Health (2021), 1–10.
[48] Alasdair Sandford. 2018. 80% of people believe fake news ‘a problem for democ-
racy’ — EU study. https://www.euronews.com/2018/03/13/80-of-people-believe-
fake-news-a-problem-for-democracy-eu-study.
[49] Secretary-General of the United Nations. 2022. Countering disinformation for
the promotion and protection of human rights and fundamental freedoms. https:
//undocs.org/en/A/77/287.
[50] Edlira Shehu, Nadia Abou Nabout, and Michel Clement. 2021. The risk of pro-
grammatic advertising: Effects of website quality on advertising effectiveness.
International Journal of Research in Marketing 38, 3 (2021), 663–677.
[51] Kai Shu, Deepak Mahudeswaran, Suhang Wang, Dongwon Lee, and Huan Liu.
2020. Fakenewsnet: A data repository with news content, social context, and
spatiotemporal information for studying fake news on social media. Big data 8,
3 (2020), 171–188.
[52] Craig Silverman, Ruth Talbot, Jeff Kao, and Anna Klühspies. 2022.
How Google’s Ad Business Funds Disinformation Around the World.
https://www.propublica.org/article/google-alphabet-ads-fund-disinformation-
covid-elections.
[53] Matt Skibinski. 2021. Top brands are sending $2.6 billion to misinformation
websites each year. https://www.newsguardtech.com/special-reports/brands-
send-billions-to-misinformation-websites-newsguard-comscore-report/.
[54] Saravanan Thirumuruganathan, Michael Simpson, and Laks V.S. Lakshmanan.
2021. To Intervene or Not To Intervene: Cost based Intervention for Combating
Fake News. In Proceedings of the 2021 International Conference on Management of
Data (Virtual Event, China) (SIGMOD ’21). Association for Computing Machinery,
New York, NY, USA, 2300–2309. https://doi .org/10.1145/3448016.3452778
[55] Yash Vekaria, Rishab Nithyanand, and Zubair Shafiq. 2024. The Inventory is
Dark and Full of Misinformation: Understanding Ad Inventory Pooling in the
Ad-Tech Supply Chain. In 2024 IEEE Symposium on Security and Privacy (SP) .
IEEE Computer Society.
[56] Yash Vekaria, Rishab Nithyanand, and Zubair Shafiq. 2024. Turning the Tide
on Dark Pools? Towards Multi-Stakeholder Vulnerability Notifications in the
Ad-Tech Supply Chain. arXiv preprint arXiv:2406.06958 (2024).
[57] Eric Zeng, Tadayoshi Kohno, and Franziska Roesner. 2020. Bad news: Click-
bait and deceptive ads on news and misinformation websites. In Workshop on
Technology and Consumer Protection. 1–11.
A User Profiles
We form browser profiles to emulate real and distinct Web users.
Our methodology revolves around the idea that user profiles can
be formed based on websites that are representative of the user’s
gender [1]. For example, if websites a.com, b.com and c.com are
mainly visited by female users from the Netherlands, and we visit
these websites with a Dutch IP address using a clean user profile,
third parties will deduce that the profile belongs to a female user
from the Netherlands.
To form a list of websites that are associated with a gender of a
specific country, we utilize the SimilarWeb analytics platform [34].
Specifically, we visit SimilarWeb and extract the 5 most popular
websites in each category and each country of our experiment.
SimilarWeb uses a taxonomy system with 210 distinct website cate-
gories (including subcategories). For each website, we extract its
demographic data (if available). SimilarWeb uses two gender groups
(i.e., female and male) to classify visitors of websites. Next, we sort
websites based on their audience’s gender representation and en-
sure that all websites have a representation of at least 55% for that
gender. We set an upper threshold of 200 websites and a lower
threshold of 100 websites to train each persona. The lower thresh-
old is more than enough, since previous work has demonstrated
that a persona is stable after visiting the top 10 websites associated
with users of that demographic [1]. This process leads to 6 (combi-
nation of 2 genders and 3 countries) lists of websites that represent
the interests of the specific persona.
We utilize Playwright [37], a browser automation framework
and set up legitimate browser profiles, retaining cookies and local
storage. To build the user profiles, we try to emulate the behavior
of a real user that visits some websites to consume online con-
tent. We try to make the behavior of our automated crawler as
non-deterministic as possible to appear as a legitimate user. The be-
havior we are emulating is that of a user that visits a website, reads
its content, and then navigates through the website after quickly
inspecting the content of each page. For each website in our target
list, we (i) visit the landing page, (ii) wait for a random number
of seconds in range [2, 5], and (iii) explore 5 subpages. In order
to explore a subpage, our crawler clicks on a randomly selected
internal URL and navigates to this subpage, waits for a random
number of seconds to emulate a user consuming content, scrolls
for a random number of seconds and then waits for an additional
random number of seconds. The websites of the list are visited in
a random order and after all websites have been visited, the user
profile is stored for further use.
B Popularity Evolution
We find that popular ad networks no longer work with websites
with low traffic. The classification of a website’s popularity is based
on traffic data from 2024. We study if their popularity was simi-
lar when the ad networks made their decisions. We compare the
popularity rank of the 461 misinformation websites of Figure 2. We
make use of the Tranco list and compare their ranks during June
2021 and June 2023 (i.e., one year before and one year after the CoP
was signed). We find that for the websites in both lists, their rank
distribution is somewhat similar. In fact, the mean rank decreased
by -9% (i.e., more popular) during this 2-year period, while the
median rank increased 42%.
Next, we perform a 2-sample KS test for the ranks of misinforma-
tion websites in June 2021 and June 2023 and find that the p-value
is large enough (i.e., 0.16) so we cannot reject the hypothesis that
the two distributions are the same. In addition to this, we argue that
the difference in the median rank might be credited to some extent
the variance the Tranco list exhibits from one version to the other.
We perform exactly the same experiment for the same time period
for the real news websites published in [45]. We find that for real
news websites, the median rank increased by 35%, a comparable
magnitude. Altogether, we demonstrate that the popularity of the
misinformation websites we studied has not changed significantly
before and after the CoP was signed, thus our argument that ad
networks have dropped only unpopular misinformation websites
still holds. We selectively compare the rank of misinformation web-
sites in June 2023 and not January 2024 (just like we do in Figure 2)
because Tranco has since changed the ground truth datasets they
utilize to compute the aggregated ranks.
C Popular Misinformation Websites
To our surprise, we find that even today, there are a lot of ad net-
works working with certain misinformation websites that one can
hardly argue they are legitimate. For example, we find that there
are at least 10 of the most popular ad networks (including Google,
Amazon, AppNexus and Pubmatic) that have an explicit and direct
business relationship with worldlifestyle.com. According to Media-
Bias/FactCheck, WordLifestyle is “a strong pseudoscience website
based on the promotion of false or misleading claims regarding

Before & After: The Effect of EU’s 2022 Code of Practice on Disinformation WWW ’25, April 28-May 2, 2025, Sydney, NSW, Australia
science and health” and it has a low factual reporting score “due
to a lack of sourcing and blatant clickbait abuse to generate adver-
tising revenue” [17]. Even such websites that are known to take
advantage of the ad ecosystem in order to monetize misinformation
still have direct business contracts with popular ad networks. In
fact, by manually visiting this website, we find that Google indeed
serves ads to visitors.
In addition to this, we find that the website of “One America
News Network” (OANN) is an approved ad inventory seller within
the most popular ad networks (including Google and AppNexus,
signatories of the Strengthened Code of Practice on Disinforma-
tion). OANN is considered a far-right biased news website that
promotes propaganda, conspiracy theories and has over 10 failed
fact checks [14]. According to SimilarWeb, this website achieves
over 2.5M monthly visits, and in conjunction with the fact that al-
most 95% of the visitors come from the United States, an advertising
valuable country, it can generate substantial ad revenue.
D Active Misinformation Websites
Inspired by previous findings that misinformation websites might
have a short longevity [10], we aim to refine our list by accumulat-
ing only misinformation websites which are still active. Towards
this extent, we perform a manual analysis using independent re-
viewers. We start from the extended list of 2,469 misinformation
websites and using an automated crawler we take screenshots of
the entire landing page of each website. Our crawler was able to
successfully access 2,049 websites and capture screenshots. Next,
two independent reviewers coming from a computer science back-
ground (not the authors of this work) evaluate which websites are
still active based on the content of the landing pages. Reviewers
are allowed to classify each website as either “Active” or “Inactive”.
Moreover, reviewers are allowed to manually visit a website and
navigate through its pages if they are not certain which label to
assign simply based on the screenshot of the landing page. The two
reviewers are independent of each other and completed the task in
a different environment, without influencing one another.
While manually rating websites, the reviewers noticed that some
domains were active in the sense of responding to requests, but
no longer served news content. This was mainly because these
websites were up for sale (i.e., parked domains) or because they
served empty content. In both of these cases, reviewers classified
such websites as inactive. Domains that did not respond to HTTP(S)
requests, domains that were non-existent (i.e., DNS NXDOMAIN ) and
domains that timed-out when accessed were all labeled as inactive.
Both reviewers evaluated the entire list of 2,469 misinformation
websites and agreed to include 1,889 websites, agreed to exclude
568 websites and disagreed on 11 websites. The reviewers agreed
in 99.55% of websites and had a Cohen Kappa score of 0.99. Note
that a high inter-rater agreement score is expected in this context
because deciding if a website is active is an easy task for a human
evaluator. We decide to only accept websites that both raters agree
are active and end up with a list of 1,889 active misinformation web-
sites. We make this list of active misinformation websites publicly
available [41].
E Ethical Considerations
In this work, we make concentrated effort to not affect the perfor-
mance of any Web service in any way. To downloadads.txt and
sellers.json files, we utilize existing crawlers and reach each
domain only once to download the specific file. This behavior is far
less intrusive compared to the automated processes that DSPs and
SSPs use daily to verify programmatic advertising. Additionally,
our data was collected once and all of our analysis is performed
offline. Regarding the collection of ads, we ensure that we click on
each ad URL only once, similarly to methodologies presented in
previous work [45, 56]. Since previous work has demonstrated that
the cost per thousand ad impressions is only a few dollars [40], we
argue that our study’s influence on the advertising ecosystem is
negligible. Finally, following the GDPR and ePrivacy regulations,
we do not collect or process any personal information of real users.
