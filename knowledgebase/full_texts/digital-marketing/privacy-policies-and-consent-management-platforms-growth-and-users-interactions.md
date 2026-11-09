---
title: 'Privacy Policies and Consent Management Platforms: Growth and Users'' Interactions over Time'
url: https://arxiv.org/abs/2402.18321
category: digital-marketing
subcategory: empirical
date: 2024-02
venue: ''
authors:
- Nikhil Jha
- Martino Trevisan
- Marco Mellia
- Daniel Fernandez
- Rodrigo Irarrazaval
source: arxiv
pdf_url: https://arxiv.org/pdf/2402.18321
pages: 24
chars: 81509
fetched_at: '2026-11-08T13:16:10+00:00'
kb_version: 1
---

# Privacy Policies and Consent Management Platforms: Growth and Users' Interactions over Time

Privacy Policies and Consent Management Platforms:
Growth and Users’ Interactions over Time
NIKHIL JHA, Politecnico di Torino, Italy
MARTINO TREVISAN, Università degli Studi di Trieste, Italy
MARCO MELLIA, Politecnico di Torino, Italy
DANIEL FERNANDEZ and RODRIGO IRARRAZAVAL,illow.io, United States
In response to growing concerns about user privacy, legislators have introduced new regulations and laws such as the General
Data Protection Regulation (GDPR) and the California Consumer Privacy Act (CCPA) that force websites to obtain user consent
before activating personal data collection, fundamental to providing targeted advertising. The cornerstone of this consent-seeking
process involves the use of Privacy Banners, the technical mechanism to collect users’ approval for data collection practices. Consent
management platforms (CMPs) have emerged as practical solutions to make it easier for website administrators to properly manage
consent in ever-changing scenarios, allowing them to outsource the complexities of managing user consent and activating advertising
features.
This paper presents a detailed and longitudinal analysis of the evolution of CMPs spanning nine years. We take a twofold perspective:
Firstly, thanks to the HTTP Archive dataset, we provide insights into the growth, market share, and geographical spread of CMPs.
Noteworthy observations include the substantial impact of GDPR on the proliferation of CMPs in Europe, where more than 40% of
websites currently adopt a CMP. Secondly, we analyse millions of user interactions with a medium-sized CMP present in thousands of
websites worldwide. We observe how even small changes in the design of Privacy Banners have a critical impact on the user’s giving
or denying their consent to data collection. For instance, over 60% of users do not consent when offered a simple “one-click reject-all”
option. Conversely, when opting out requires more than one click, about 90% of users prefer to simply give their consent. The main
objective is in fact to eliminate the annoying privacy banner rather the make an informed decision. Curiously, we observe iOS users
exhibit a higher tendency to accept cookies compared to Android users, possibly indicating greater confidence in the privacy offered
by Apple devices. We believe the findings of this paper contribute to a deeper understanding of the multifaceted interactions between
privacy regulations, technological solutions and user choices in the evolving Web ecosystem. We also show that the availability of
large open datasets, although not explicitly designed and collected for our goals, is fundamental to exploring different angles of the
internet evolution over time.1.
Additional Key Words and Phrases: cookies, consent management platforms, Web privacy, Web measurements
1 INTRODUCTION
The landscape of Web advertising has been continuously evolving since the Web is more and more intertwined with
people’s lives, and many websites base their revenues on advertisements (ads). To maximize ad effectiveness, Interest-
Based Advertisement (IBA) stems from the fundamental assumption that users will be more interested in ads that relate
to their specific interests. In the Web ecosystem, this fueled the deployment of mechanisms that aim at building specific
per-user profiles to push the IBA to a great level of detail. Third-party cookies have largely been at the center of the
IBA ecosystem. Once installed on the end user’s browser, the so-called profiling cookies cookies enable a third party to
collect information on the visits a user performs on those websites where the third-party is present [19, 34, 35]. This
allows the third party to collect information about the users’ navigation history and derive what they are interested in.
1Part of this work previously appeared at the 2023 Network Traffic Measurement and Analysis Conference (TMA).
Authors’ addresses: Nikhil Jha, nikhil.jha@polito.it, Politecnico di Torino, Italy; Martino Trevisan, martino.trevisan@dia.units.it, Università degli Studi di
Trieste, Italy; Marco Mellia, marco.mellia@polito.it, Politecnico di Torino, Italy; Daniel Fernandez, daniel@illow.io; Rodrigo Irarrazaval, rodrigo@illow.io,
illow.io, United States.
1
arXiv:2402.18321v2  [cs.CY]  29 Feb 2024

2 Jha, et al.
Over the years, the use of cookies raised concerns for the users’ privacy, and legislators started acting to regulate
the abuse of these practices across the Web to increase the users’ awareness of the process. In the European Union,
the first significant step in this direction was the introduction of the “Cookie Law” [ 12] in 2009, which states that
every website using first- or third-party cookies should obtain user’s approval via a Privacy Banner. The measure was
further enforced in 2018 with the General Data Protection Regulation (GDPR) [21], which introduced severe fines to
non-compliant websites and organizations. Similarly, other legislators around the globe started regulating the collection
of personal data, making the presence of Privacy Banners pervasive as we all experience while surfing the Web. Notably,
California’s California Consumer Privacy Act (CCPA) [11] in 2018, the Brazilian General Personal Data Protection Law
(LGPD) [10] and the Canadian Personal Information Protection and Electronic Documents Act (PIPEDA) [39] in 2000
(and currently being reformed [40]).
To avoid the burden of creating, controlling, and checking the compliance of Privacy Banners with existing and
evolving regulations, websites often outsource the banner creation and management to external companies offering
Consent Management Platforms (CMPs). CMPs take care of the technical complexity of implementing Privacy Banners,
offering their customers a simple mechanism to install and manage the user’s consent and data collection at large.
In this paper, we present a longitudinal measurement study that aims to understand how the Consent Management
Platforms landscape has evolved over the years, and how users interact with them. We consider two angles in our
study: the system and the end-user point of view. From the system point of view, we break down the global evolution of
CMPs, observing the growth of different solutions, their market share, their effectiveness in controlling the usage of
third-party cookies and their spread in different geographical regions. For this, we leverage the unique opportunity
offered by the HTTP Archive [3] which includes the history of millions of websites since 2015.
From the end-user perspective, we leverage the preferences expressed by users when interacting with a medium-sized
CMP, observing the impact of different options like the presence (or absence) of a “one-click-choice” option, the position
of the banner, the device they use, the country they are from, etc. To this end, we leverage a unique dataset of the
illow.io2 CMP which spans more than two years of data since its introduction in the CMP market, collecting more than
20 million interactions with the CMP.
Our study unveils the introduction of the GDPR and similar regulations fuelled the explosion of the CMPs which are
now present in 40% of websites in Europe. We also witness an increase in websites that opted to directly remove third-
party tracking technologies, probably balancing the benefit and complexity of managing their presence. Surprisingly,
more than 50% of websites adopting a CMP still install third-party cookies of possible tracking services before the user
accepts their usage. This is in fact due to the complexity of managing third-party content, and the lack of standard
technical solutions to enforce the user’s choice by CMPs. Moreover, a website must nowadays adapt its behavior with
third parties depending on regulations and the country of the user. This, in turn, calls for more analysis and for more
extensive archival projects.
From the user’s point, we observe that more than 60% of users deny the usage of third-party tracking cookies when
offered a simple “one-click reject-all” action. Yet, the large majority of these choices derive from the intent of quickly
removing the intrusive banner from the screen rather than an explicit and conscious decision. In fact, in those countries
where the opt-out choice requires more than one click, about 90% of users accept the usage of cookies via a one-click
accept-all button. Curiously, iOS users tend to accept the usage of cookies more frequently than Android users. This
may be linked to a higher confidence in privacy offered by iOS and Apple devices.
2https://illow.io

Privacy Policies and Consent Management Platforms 3
Both the HTTP Archive and the illow.io datasets have not been collected nor been designed specifically for this
work. Yet, their availability allows us to study and present interesting insights in an opportunistic manner. In particular,
HTTP Archive collects its data uniquely from locations in the U.S., which is nowadays limiting, as the web is more and
more customized based on users’ location to adapt to the different privacy regulations. To allow the reproducibility of
part of our results, we publish online the pre-processed HTTP Archive dataset and the code to obtain the figures of this
paper [4].
The remainder of the paper is organized as follows. In Section 2, we introduce the regulation history and discuss
related works. In Section 3, we discuss the methodology and the datasets we use for our analysis. In Section 4 we present
how the pervasiveness of the CMPs in the Web has evolved over time while in Section 5 we focus on users’ interactions
when facing the Privacy Banners of the illow.io CMP. Finally, in Section 6, we summarize the main finding of our work.
2 PRIV ACY REGULATIONS AND RELATED WORKS
Behavioural advertising has always been a pillar of the Web ecosystem and entailed the massive collection of personal
information through web tracking and cookies [7, 19, 20, 34, 35, 38, 41, 43, 46]. The implications of web tracking on
users’ privacy encouraged the legislator to issue privacy-related regulations.
In the European Union, the introduction of the Cookie Law [12] in 2009 and updated in 2013 led to the proliferation
of Privacy Banners [18]. The regulation states that when visiting a website, users have to interact with the Privacy
Banner to explicitly opt-in to the usage of tracking mechanisms. Only after getting explicit users’ consent, the website
(and any third party embedded in the website) are allowed to install cookies and start the data collection. Privacy
Banners, however, do not fully protect users in many cases [48]. Later in 2018, the GDPR profoundly influenced the
Internet user experience [14, 16, 30, 32, 44] for EU-based users by defining severe sanctions for violators.3
Other countries issued similar regulations, with notable examples in the Brazilian Lei Geral de Proteção de Dados
Pessoais (LGPD) [10] (entered into force on September 18th 2020), the PIPEDA [39] (April 13th 2000) and Quebec 25
law [36] (September 22nd 2021) in Canada, and the California Consumer Privacy Act (CCPA) [11] (January 1st 2020)
which spurred other US states to enforce similar regulations. At the high level, these regulations provide individuals
control over the personal data that businesses collect about them. In a nutshell, they mandate that users have to explicitly
opt-in to the collection of personal data, including the usage of cookies and other tracking technologies on the web.
A large number of websites started to rely on Consent Management Platforms, i.e., external companies that provide
technical solutions to manage users’ consent collection by offering customizable and easy-to-deploy Privacy Banners.
Hils et al. [26] provided a first analysis of CMPs’ popularity. By actively crawling popular websites for almost three-years
they provide a detailed picture of the growth in popularity of CMPs, observing websites switching CMPs, and manually
analyzing the privacy policies they publish to check the purpose for data collection indicated. Our work complements
and extends this analysis by offering a longitudinal analysis over a period of 9 years thank to the HTTP Archive, and by
including the users’ perspective on the analysis.
In general, it has been shown that most users tend to ignore privacy-related notices [13, 22, 50], up to getting annoyed
by these. This behavior has gone under the name of “privacy paradox”: Users claim to be concerned about their privacy,
while at the same time taking little actions to protect their data [8]. In fact, given the advertising-based business model,
some websites and CMPs make efforts to increase the cookie acceptance rate. Recent works have shown that banners
often nudge users to acceptance by exploiting dark patterns in the user interface, if not openly disregarding GDPR’s
3U.K. adopted GDPR in the “Data Protection Act” in 2018. In the rest of the paper, we refer to “GDPR countries” as any European country where the
GDPR is in place, including U.K.

4 Jha, et al.
requirements [33], or making it difficult for users to exercise their rights [ 24]. Some hide the content of a website,
which is visible only upon cookie acceptance. These impacts automated internet measurements since the first visit
to a website may not show the actual website content [29]. Nudging includes offering the user a Accept All default
button via intrusive banners [9, 17], which is often the case [25] with websites presenting large pop-ups or wall-style
banners that cover most of the webpage content. Researchers have shown that apparently minor design choices have
a significant effect on inducing the user to accept the cookies [ 31, 37, 42, 45, 47, 49]. For instance, Habib et al. [23]
compared the behaviour of 1 109 volunteers on 12 different banners, showing that the cookie acceptance rate varies by
≈ 25% depending on banner design. Unequal paths (i.e., refuse action more complicated than the accept action) and
blocking banners are the most important factors. Our work complements this by analyzing the behaviour of millions of
users when facing the banner of a popular CMP whose banner assumes various forms across time and country. This
allows us to compare the impact of the banner design including many more factors than those considered by Habib et
al. [23].
The part of the paper focused on the study of user interaction the CMP is an extension and a refinement of a previous
work [28]. In this work, we extend the timeline of our analysis to include more than two years. This allows us to better
appreciate the impact of the banner design on the user choice and to include several new angles, including the impact
of the user’s device, country, etc.
3 METHODOLOGY AND DATASETS
This section describes our datasets and the processing methodology we adopt to carry out our analyses. We rely on
two datasets to study CMP adoption and user behaviour on CMPs that we enrich using external sources. We provide
a high-level overview of our data processing and analysis methodology in Figure 1. The top part refers to the CMP
adoption study which we base on the HTTP Archive. The bottom part refers to the user behaviour study which we
base on the CMP dataset. In both cases, we start from a longitudinal dataset, and integrate it with external information
to observe both the evolution over time of different metrics and the detailed breakdown in the most recent period. In
the appendix, we provide the exact structure of the two datasets. We release the pre-processed HTTP Archive data used
in our analyses along with the code to replicate our results as open-source [4].
3.1 CMP Adoption
3.1.1 Dataset.
To study CMP adoption through the years we use the HTTP Archive open dataset [3]. The curators of this archive visit a
list of worldwide websites using an automated version of the Google Chrome browser. They perform the visits using test
agents from various Google Cloud data centers in the U.S. The test agents use the WebPageTest4 to instrument Google
Chrome and collect several metrics on the web page visit using the HTTP Archive (HAR) format, a JSON-formatted
archive format for logging a web browser’s interaction with a webpage. All websites are visited every 15 days to create
a longitudinal archive. The curators update the list of websites they visit on regular periods. In detail, until June 2018
the website list contains the top-500 k entries of the Alexa rank. In July 2018, they extended the list to include the
top-1M websites taken from the Chrome UX Report, which contains a variable set of entries (≈ 10 M), updated on a
monthly basis.5. The HTTP Archive data is available on Google Cloud from which we downloaded the data into a Spark
cluster for processing.
4https://webpagetest.org/ toolset, Accessed on Friday 1st March, 2024.
5https://developer.chrome.com/docs/crux, Accessed on Friday 1st March, 2024.

Privacy Policies and Consent Management Platforms 5
HTTP Archive
CMP Dataset
CMP Adoption
Tracker Adoption
User Location
User Device
AdGuard &
Wappalyzer
AdGuard & EasyPrivacy &
Whotracksme
Maxmind Geo IP
Python User Agents
Website behavior:
• CMP Use
• Tracker Presence
• CMP market share
User behavior:
• By country
• By device
• By type of banner
Longitudinal
Analysis
Last Snapshot
Longitudinal
Analysis
Stable Snapshot
Fig. 1. Data processing and analysis workflow. The top part refers to the CMP adoption study. The bottom parts to the user behaviour
study.
In this work, we rely on the monthly snapshots offered by HTTP Archive starting from January 2015 until December
2023. For the longitudinal study, we focus on the subset of websites that are present for the whole time. There are
47, 899 websites. We refer to this dataset as HTTP-9Years. To study the impact of the countries the website belongs to,
we use the top-level domain (e.g., .fr ) to associate a website with its main country. 6 We have 11, 819 website whose
top-level domain belongs to a GDPR-regulated countries, and that are present for all the nine yars. We focus most of
our analysis on this set of websites. Table 1 details the breakdown of sites for each country.
To complement the longitudinal study and detail the most recent picture of the CMP adoption, we resort to the last
available snapshot which includes the top-1M websites as visited during December 2023. This dataset includes websites
from all over the world. We refer to this dataset as HTTP-Dec23 (last line in Table 1).
For each visit, the HTTP Archive datasets report several statistics and details on each HTTP transaction carried out
to fetch the webpage’s objects. In detail, for each HTTP request/response pair, the dataset reports the URL, the timings
and various HTTP headers including Cookies, Referrer, etc. This allows us to study the presence of various third-party
elements in a website, including the presence of CMPs or other third-party services. To this end, we examine all HTTP
requests issued during the page loading and extract the domains from the corresponding URL. In case the HTTP request
refers to a third-party server (i.e., the domain is different from the webpage one), we match the domain into the lists
described in the next paragraph to detect whether the website adopts a CMP or embeds a potential web tracker.
3.1.2 Processing Methodology.
CMP Identification. We study the adoption of CMPs by looking for URL requests to the most popular CMPs. For this,
we build a list of CMP domains by combining two sources: the AdGuard [1] list which includes a set of CMP domain
names; And the Wappalyzer [5] list, a profiler tool that is used to identify various characteristics of a website including
the presence of Content Management Platforms and Analytics products. Wappalyzer explicitly lists domain names of
6Although there exist other approaches to link a website to its country (e.g., inspecting the registrar of the DNS domain or location of the server), using
the country-code TLDs represents an accurate yet conservative option, even if we may erroneously exclude websites using global TLDs (.com, .org, etc.).

6 Jha, et al.
Table 1. Breakdown of Websites present in the HTTP Archive Dataset.
Dataset Websites Period
HTTP-9Years
Total 47,899
Jan 2015 - Dec 2023
GDPR 11,819
.de 2,907
.es 603
.fr 1,060
.it 1,060
.co.uk 1,617
EU No-GDPR 1,412
Africa 336
Asia 3,926
North America 777
South America 1,399
Other 28,230
HTTP-Dec23 1,000,000 Dec 2023
CMPs. We merge the two sets of CMP domains, and, given the small number of entries, we manually verify each one. In
total, we obtain 84 CMPs, each identified by one or more domains.
Potential Trackers. To detect the presence of potential third-party trackers in a given website, we merge publicly-
available lists provided by Whotracksme [6] (an anti-tracking-related open-data provider), EasyPrivacy [2] (one of
the lists at the core of AdBlock tracker-blocking strategy) and AdGuard [ 1] (a popular ad-blocking tool). Trackers
are identified by their domain name. For robustness, we merge the three lists and consider as a potential tracker
any third-party domain that appears in at least two lists. In total, we obtain 1,497 domains that we consider tracking
services.7
We record the presence of a tracker during a visit if the webpage embeds an object served by a tracking domain and
the latter installs a persistent cookie. The HTTP archive dataset does not indicate the content and the lifespan of the
cookie, making it impossible to verify if the third-party cookie is actually a Profiling Cookie or not. We thus verify the
potential presence of a Tracker. In fact, such a cookie could be a technical cookie used to store, e.g., consent information,
not violating the privacy policy or the regulations.
3.2 User interaction
3.2.1 Dataset.
To study the users’ interaction patterns when facing a Privacy Banner we use a proprietary dataset of illow.io, a
medium-sized CMP company. The illow.io CMP provides web developers with the ability to include a simple Privacy
Banner to control their preferences about data collection, via cookies or other means. The banner is shown the first
time a user accesses the website as a small overlay window that can be placed in different locations on the screen. The
users can express their preference across four categories of cookies: i) necessary, ii) statistical, iii) preferential, and
iv) marketing cookies. The necessary cookies include those technical cookies that are needed for the site to function,
including the storage of the user’s preference on the usage of cookies, and the user cannot opt out from their usage.
Once the users have expressed their choice, the CMP sets the necessary cookies on the user’s device to store their
7For simplicity, we match the domains using the second-level domain name — i.e., a hostname truncated after the second label. We handle the case of
two-label country-code TLDs such as .co.uk.

Privacy Policies and Consent Management Platforms 7
preferences. When the user accesses again the website, no banner is shown and preferences can be updated via a
dedicated page.
The Privacy Banner is served directly by the illow.io servers in the form of a small set of Java Scripts. When users
interact with the Privacy Banner (i.e., provide their choice, or change their consent), the illow.io servers log the event.
The collection happens only when users submit their preferences (as detailed in the privacy notice). No data is collected
if the user does not perform any action on the banner. The logged information includes the time of the visit, a random ID
of the entry, an anonymized ID for the website, the type and position of the banner, which cookies the user accepted, the
User Agent header value as set by the browser, and the client IPv4 /24 subnet. We use the client’s subnet to map a user
to country and state via the MaxMind GeoIP8 database.9 This information is necessary to implement the functionalities
of the platform (i.e., record user’s preferences for the next visits to the website), and it is useful to customize the
information provided to users (e.g., show the banner in different language, decide what version of the banner to show
to the user — more details in Section 3.2.2), and to collect statistics about the usage of the platform, including the billing
of the website deploying the CMP. All these pieces of information, including the description of the collected data and
the purpose of the collection, are documented in the privacy policy the CMP offers to users.
Users submitting (or changing) their preference generate an entry in the log, which we call an interaction in the
following. As previously stated, each entry is associated with a random ID, and, thus it is impossible to re-identify or
track a user across different websites, guaranteeing users’ privacy. To further protect the CMP customers, in the data
used for this study, the website name is also anonymized by replacing the domain name with a random identifier.
We classify each interaction according to the combination of cookie categories accepted by the user. Specifically, we
classify interactions as:
• Accepted-All: if all cookie categories are accepted, either with a single click on the Accept All button, by
individually accepting all the cookies after clicking on Custom Permissions button, or by clicking on the Don’t
sell my data link;
• Rejected-All: if only the necessary cookies are accepted, either by clicking Reject All button (or equivalent
action) if present, or by manually deactivating all the cookies after clicking on Custom Permissions (recall
that necessary cookies cannot be excluded);
• Custom: if at least one among the statistical, preferential and marketing cookies is accepted through the Custom
Permissions screen.
In the following, we compare the Rejected-All rate against different factors, such as banner layout and position, user’s
country and type of device. This offers us precious insight into understanding which banner layout is the most effective
in allowing the users to exercise their right to refusal.
The dataset contains interactions spanning from July 1st, 2022 to August 22nd, 2023. In this period, the CMP collected
≈ 25𝑀 interactions from more than 6,000 websites. We report the breakdown of interactions per user’s regions in
Table 2. Also for this dataset, we consider the whole data when focusing on the evolution over time, while we consider
the period from July 5th 2023 until the end to consider a stable period and minimize the effect of the transients.
Banner Layouts. The illow.io CMP complies with the privacy regulations of different countries and follows the best
practices recommended by the privacy regulation bodies. The different regulations specify how online companies
should collect data of the visitors (from areas under their jurisdiction) and indicate how the user’s consent should be
8https://www.maxmind.com/, Accessed on Friday 1st March, 2024.
9We do not consider IPv6, as it generates negligible traffic.

8 Jha, et al.
Table 2. Number of users’ interactions per geographical region - illow.io dataset.
Region Total July-August ’23
South America 11,953,295 (48.20%) 3,415,701 (43.79%)
GDPR-regulated 9,417,253 (37.97%) 3,124,085 (40.06%)
North America 2,448,467 (9.87%) 849,008 (10.89%)
Asia 377,853 (1.52%) 184,390 (2.36%)
Rest of Europe 367,107 (1.48%) 140,969 (1.81%)
Africa 149,905 (0.60%) 45,925 (0.59%)
Oceania 87,685 (0.35%) 38,757 (0.50%)
(a) General banner.
 (b) GDPR-compliant banner.
 (c) CCPA-compliant banner.
Fig. 2. The available banners introduced since July 2023 in the illow.io CMP. Figures showcase the pop-up style banners.
obtained. When a new user visits a website, the CMP serves the correct type of banner according to the country and
region the customer visit comes from.
Over the years, the illow.io CMP updated several times the design and actions offered by the banner to enable new
functionalities or to adapt to evolving regulations. In our longitudinal study, we show the impact of such changes. The
description below refers to the most recent configuration of the CMP which has been in place since July 5th 2023. The
illow.io CMP supports three different types of banners that comply with different regulations:
• The General banner (Figure 2a) presents two buttons, the Accept All and the Custom Permissions . The first
button gives the permission to install any type of cookie – i.e., represent the opt-in choice. The second button
brings to a selection window, where the user can fine-select the categories of cookies to accept. This is the
default banner shown to users who connect from areas that are not covered by any particular regulation.
• The GDPR-compliant banner (Figure 2b) presents three buttons. The Accept All gives the permission to install
any type of cookie. The Reject All only forbids all but necessary cookies. Finally, the Custom Permissions
prompts to the selection window as in the General banner. The banner also features a close-window button
in the form of an “X”. The CMP offers this banner to users connecting from GDPR-regulated countries and
from countries with similar regulations – i.e., Canada (due to the PIPEDA and Quebec 25 laws) and Brazil (due
to the LGPD). This banner was introduced in August 2022, while, before, users in these countries faced the
General banner. Moreover, the operation of the “X” close button changed from “accept-all” to “reject-all” action
in December 2022. We will explore these changes in Section 5.
• The CCPA-compliant banner (Figure 2c) notifies the user that cookies are being used. Two links appear: the first
brings to the website privacy policy; The second, named “Don’t sell my data”, brings the user to the selection
window where the user can fine-select the active cookies. This banner is served by default to visitors coming
from California and Utah, under the regulation of the CCPA and the Utah Consumer Privacy Act (UCPA),
respectively. The banner offers a close-window button in the form of an “X” that closes the banner without

Privacy Policies and Consent Management Platforms 9
requiring further action from the user, which implicitly accepts the use of cookies. Notice that the operation of
this banner is different from the previous two: The user must explicitly opt out of cookies, which are enabled
by default.
3.2.2 Processing Methodology. The dataset is securely stored on a big data cluster located in our institution. We process
it using Python code to extract various metrics and statistics. Given that an imbalance exists in the website audience,
we want to prevent popular websites from biasing the results. For this, we opt to show results using a website-wise
macro-average of the metrics under study. In other words, we compute the desired metric average for each website,
separately. Then we compute the average over the websites. In such a way, each website weights one, regardless of the
number of interactions it generates. We consider a per-website average valid if we observe at least 10 interactions from
it, in at least 50 websites.
Formally, given a target metric𝑀 (e.g., Rejected-All), a set of websites𝑤∈W , each with a population of interactions
I𝑤, an indicator function 1 𝑀(𝑖) which return 1 if 𝑖 refers to 𝑀, 0 otherwise (e.g., whether interaction 𝑖 records a
Rejected-All choice or not), we define as 𝑀(I) the website-wise macro-average of 𝑀 computed over the samples
belonging to the subsetI = — 𝑤∈𝑊 :|𝐼𝑊|≥ 10I𝑤. Formally:
𝑀(I𝑤) = 1 |I𝑤| ∑︁ 𝑖∈I𝑤 (1 𝑀(𝑖)), given|𝐼𝑊|≥ 10, (1)
𝑀(I) = 1 |W| ∑︁ 𝑤∈W 𝑀(I𝑤), given|W|≥ 50, (2)
Equation(1) computes the per website average. Equation(2) computes the overall macro average.
In addition, we also evaluate the confidence interval of the macro average. Hence, each estimate is presented as:
𝑀(I)± 𝑐· 𝑆(I) |𝑊| ,
where𝑐 corresponds to the quantile of a Student’s 𝑡-distribution with|𝑊|− 1 degrees of freedom, and𝑆(I) is the
sample standard deviation of each website-wise average. In this work, we consider a confidence interval of 90% and
report the confidence interval as an error bar. As our main target metric, we consider the Rejected-All rate.
4 TEMPORAL EVOLUTION OF CMP ADOPTION
In this section, we study the adoption of CMPs on websites during the last 9 years. To this end, we rely on the two
HTTP Archive datasets (HTTP-9Years and HTTP-Dec23) as described in Section 3.
4.1 Overall trend
We start our analysis with Figure 3 where we show the fraction of websites with and without a CMP on the 11,819
European-based websites where GDPR is in force. We further break down the statistics to consider sites that embed or
not a potential tracker. Observe how the CMP adoption (indicated by the black curve) was negligible before the GDPR
(entered into force in May 2018, indicated with a black vertical line in the Figure): At that time, only≈ 5% of websites
adopted a CMP. Recall that some form of Privacy Banners was already implemented to comply with the previous
“Cookie Law” European directive. Yet, CMPs were not a common solution. Notice that between 2015 and 2018, at least 3
out of 4 websites used to embed at least a potential tracker even if the user did not accept their usage. This is in line
with our previous finding [48]. In fact, this figure is a lower bound for the popularity of tracking services because we

10 Jha, et al.
2015/012016/012017/012018/012019/012020/012021/012022/012023/012024/01
0
20
40
60
80
100Websites [%]
Websites with CMP
GDPR enters
into force
No CMP & No Tracker Cookie
No CMP & Tracker Cookie
CMP & No Tracker Cookie
CMP & Tracker Cookie
Fig. 3. Fraction of websites with/without a CMP and contacting
potential trackers. HTTP-9Years Dataset of 11,819 websites that
are present during the whole period in GDPR-regulated countries.
Table 3. Fraction of websites with/without a CMP and con-
tacting potential trackers. HTTP-Dec23 Dataset with top-1M
website worldwide.
Tracker No Tracker Overall
CMP 9.9% (75.6%) 3.2% (24.4%) 13.1%
No CMP 40.2% (46.2%) 46.7% (58.8%) 86.9%
Overall 50.1% 49.9%
Table 4. Potential tracker and Third Party prevalence on websites adopting different CMPs. HTTP-Dec23 Dataset with top-1M
website worldwide.
CMP Websites With Trackers [%] Average Trackers Websites
Usercentrics 32.94 2.14 16,077
Iubenda 56.30 3.05 13,378
OneTrust 61.33 9.23 46,144
CookieScript 63.55 4.78 2,093
Cookiebot 75.85 4.99 12,415
Didomi 82.14 20.29 5,202
Funding Choices 97.85 16.30 26,921
HubSpot 99.20 9.07 20,871
expect more trackers would be contacted upon the user’s consent (recall that the HTTP Archive test agents perform
always a “first-visit” to all websites and do not interact in any form with any banner).
Starting from May 2018, the CMP adoption quickly increases, reaching 30% at the beginning of 2021 and 42% in late
2023. As expected, the CMP adoption erodes primarily the fraction of websites with no CMP and potential tracker (light
red area) which shrinks from≈70% (May 2019) to≈20% (Dec. 2023). This indicates that the introduction of the GDPR
created a new need for those websites using ads and tracking services to adopt solid privacy management solutions (i.e.,
a CMP).
It is interesting to notice that the fraction of websites without a CMPand without potential trackers (light green area)
increases as well, growing from 20% (May 2019) to 35% of websites (Dec. 2023). We argue this is due to two phenomenon:
first, some large and popular websites started implementing proprietary consent management solutions (which we
cannot detect). Second, smaller web services started balancing the benefit of including third-party ad services with the
burden of correctly managing their presence, opting out from including trackers and deploying a CMP.
Focus now on the fraction of websites with CMPs (bottom solid red and green areas). Unexpectedly, more than
60% of websites that adopt a CMP still lets the user’s browser install cookies from potential trackers before collecting
any user’s consent (bottom dark red area). We argue this is due to the complexity of managing advertisement and
tracking platforms, coupled with the burden of installing and operating a CMP and the lack of a standard mechanism
for CMPs to control third-party services. In a nutshell, as previously found [48], the presence of a consent banner does

Privacy Policies and Consent Management Platforms 11
2015/012016/012017/012018/012019/012020/012021/012022/012023/012024/01
0
10
20
30
40
50
60
70Websites with CMP [%]
Italy implements
Cookie Law
Germany mandates
Opt In
.de .es .fr .it .co.uk
Fig. 4. Fraction of websites with a CMP for 5 European TLDs.
HTTP-9Years Dataset of 11,819 websites that are present
during the whole period, in GDPR-regulated countries.
2015/012016/012017/012018/012019/012020/012021/012022/012023/012024/01
0
10
20
30
40
50Websites with CMP [%]
Europe (GDPR)
Europe (Non-GDPR)
North America
South America
Asia
Fig. 5. Fraction of websites with a CMP for different con-
tinents. HTTP-9Years Dataset of websites that are present
during the whole period, in not GDPR-regulated countries.
not guarantee the correct management of data collection policies. Recall that we cannot claim those websites violate
the GPDR: first, the HTTP Archive visits websites from the U.S. and a website/CMP might differentiate their behaviour
when the user visit comes from a non-GDPR country. Second, a tracking service can legitimately install a technical
cookie before the user’s consent. As previously said, we cannot distinguish this case from the installation of an actual
profiling cookie due to limitations of the HTTP Archive data.
We complement our analysis by looking at the most recent snapshot which contains the top 1 million ranked websites.
Here, we broad the picture to include websites from all over the world, regardless of their country and of being present
in the past snapshots. In Table 3 we show the CMP adoption and potential tracker share. Globally. Only 13.1% of
websites adopts a CMP, while 50.1% of them include potential trackers. As noticed before, most websites adopting a
CMP embed potential trackers (9.8% of the total, corresponding to 75% of sites with CMP).
We investigate in more detail the surprisingly large fraction of websites with CMP that include a potential tracker. For
the top-10 most popular CMPs (see later), in Table 4, we report the percentage of websites that embed a potential tracker
(sorted from lowest to highest), their average number and the number of websites they are present in. Results are very
heterogeneous, with some CMPs able to prevent the browser from contacting potential trackers more efficiently than
others. For instance, 32.9% of websites adopting Usercentric still contact two potential trackers on average. Conversely,
58.8% of sites adopting the Sourcepoint CMP still allow the visitors to contact more than 33 potential trackers. Again,
due to the limitations of the HTTP Archive, we cannot confirm the cookies installed by potential trackers are profiling
cookies. Recalling that the HTTP Archive visits come from the USA, we manually verified 10 websites adopting the
Usercentric and 10 the Sourcepoint CMP, visiting them from Italy. In all cases, we observe both CMPs correctly permit
the browser to contact trackers only after accepting the site privacy policy. This call for further investigations and
automated means to provide an extensive evaluation of the eventual violation of the privacy policies as this would
depend on multiple factors such as client country location, language, device type, etc. as presented in our previous
work [29]. We leave this as future work.
4.2 Country-wise and region-wise diversity
Different countries and regions of the world have adopted different regulations at different times. To observe how this
impacts the evolution of CMPs, in Figure 4 we break down the CMP adoption for GDPR countries. Here, we focus on
websites belonging to five country code top-level domains, namely: .de, .es, .fr, it and .co.uk, i.e., websites based

12 Jha, et al.
in Germany, Spain, France, Italy and the United Kingdom, respectively. Before GDPR (represented by the black vertical
line), CMP adoption was negligible in all countries except for Italy, where approximately 10% of websites already
adopted a CMP starting from mid-2015. This is due to the implementation of the old European Directive called Cookie
Law [12], which entered into force in June 2015 in Italy. Indeed, the Italian Data Protection Authority “Garante per
la protezione dei dati personali” mandated the correct implementation of a Privacy Banner [27] by June 2, 2015. As a
consequence, Italian websites resorted to CMPs to solve the issue. The Italian CMP Iubenda grabbed a market share of
90.3% in Italy by the end of 2017. In the last part of this section, we analyse in detail the market share of popular CMPs.
Following the entering into force of the GPDR (May 2018), the CMP adoption started increasing gradually until 2023,
even if at a different pace. Italian websites (purple line) grow quicker, remaining those with the highest rate until the
most recent snapshot. Conversely, the German websites (red line) have the lowest CMP adoption rate reaching just≈ 10%
in mid-2020. From June 2020, they exhibit a very rapid increase, reaching 35% by the end of the year. This acceleration
is due to the decision of the German Federal Court [15] that in May 2020 modified the GDPR in a more restrictive sense.
The judgement underlined the need for explicit user consent before installing marketing or nonessential cookies and
specified that an opt-out mechanism is invalid. We speculate this led to the massive adoption of CMPs in Germany,
causing their sudden growth to 40% by mid-2021. Spain, France, and the UK exhibit a more gradual increase. The CMP
adoption was below 10% in May 2019 and increased to 40-50% by the end of the observation period.
Interestingly, we observe that, in all countries but the UK, CMP adoption is no longer increasing in 2023, and we
even notice a moderate yet measurable decrease in Italy and Germany.
For the sake of comparison, in Figure 5 we dissect CMP adoption for different regions of the world. The red solid line
refers to GDPR countries (i.e., it is equivalent to the back curve of Figure 3). In these countries, CMP adoption tops 42%,
while we observe a moderately decreasing trend in the second semester of 2023. In the remaining European countries
(those not implementing the GDPR, blue line), the CMP adoption rate stands at significantly lower values, and even
with an increasing trend, it has not yet reached 20%. We observe similar numbers for North America and Asia – green
and cyan curves, respectively. Interestingly, in South America, the CMP adoption rate is consistently higher over time,
exceeding 20% since mid-2023. This is mostly due to Brazilian (.br) websites, which represent 59% of the 1,399 South
American websites in the HTTP-9Years dataset. Recall that in Brazil the LGPD entered into force in September 2020,
imposing a regulation similar to the GDPR. We consequently observe an average CMP adoption rate in South America
of 26% by the end of 2023.
In short, we clearly observe that the entrace into force and important changes to the regulations stimulate the need
for valid technical solutions, creating a new market need that CMPs satisfy.
4.3 The CMP market ecosystem
We now study this new CMP market, discussing the pace at which they are born and how their market share evolves
over time. We focus on the GDPR-based websites present in the HTTP-9Years dataset. We first study when new CMPs
enter this market over the years. In Figure 6, the𝑥-axis represents time; On the𝑦-axis, we sort the CMPs by the time of
their first appearance. A dot in the figure indicates that the i-th CMP was found on at least 10 different websites in that
month. In fact, out of 84 CMPs present in our list, 76 have actually been adopted by more than 10 websites (we expect
some to be active uniquely in countries other than GDPR). Figure 6 shows that, before the GDPR, less than 20 CMPs
were active on the market. The GDPR fostered the born of new solutions, and, by the end of 2019, 35 CMPs were active.
In 2020 we observe a second increase in the number of CMPs, with the adoption of 30 new platforms, a symptom of a
more vast, yet competitive market for privacy-management solutions. In 2021, 2022 and 2023 we testify only less than

Privacy Policies and Consent Management Platforms 13
2015/012016/012017/012018/012019/012020/012021/012022/012023/012024/01
0
10
20
30
40
50
60
70
80CMP
Fig. 6. Presence of the considered CMPs in the observation period. HTTP-9Years Dataset of 11,819 websites that are present during
the whole period, in GDPR-regulated countries.
2015/012016/012017/012018/012019/012020/012021/012022/012023/012024/01
0
20
40
60
80
100Market Share [%]
0.5% 1.6% 1.8% 2.8% 8.5% 13.5% 29.7% 38.1% 41.7%
CMP Adoption Rate
Other
HubSpot
Iubenda
Sourcepoint
Funding Choices
Didomi
Usercentrics
Cookiebot
OneTrust
Fig. 7. Market share of the top-8 CMPs. HTTP-9Years
Dataset of 11,819 websites that are present during the whole
period in GDPR-regulated countries.
OneTrust
Funding Choices
HubSpotUsercentrics IubendaCookiebotDidomi CookieScript AxeptioCookieYes Other
0
5
10
15
20
25
30Websites [%]
Fig. 8. Market share of the top-10 CMPs on the last snapshot.
HTTP-Dec23 Dataset with top-1M website worldwide.
10 newcomers, hinting the European market is rather saturated. Finally, we notice that a non-negligible fraction of
CMP (18 out of 76) has apparently shut down or has been acquired by other companies (i.e., is no longer present as
testified by the missing dots).
We now focus on CMP market share. For each CMP, we compute its market share as the ratio between the number
of websites adopting it and the number of websites using any CMP. In Figure 7 we report the market share evolution in
the GDPR countries of the top-8 CMPs (as measured in the last time step of the dataset). The grey area represents the
remaining CMPs. For reference, the top-𝑥-axis reports the overall CMP adoption rate (recall it increases over time).
Before the GDPR came into force, Iubenda dominated the market: it was the choice for more than 40% of (mostly Italian)
websites resorting to a CMP. The main competitor of Iubenda was Hubspot, even if with moderate penetration. After
GDPR, the leading position of Iubenda is quickly eroded by new competitors: Cookiebot and OneTrust entered the
market, the former reaching a market share of 16.1% by the end of 2020. Since then Cookiebot maintained its market
share of about 25-28%. OneTrust, a company offering various marketing and analytics solutions, exhibits a significant
growth that reaches 29% at the end of 2023. This is also thanks to the acquisition of the CookieLaw and CookiePro
competitors. The youngest notable player is Funding Choices, a CMP operated by Google, which appeared in 2020 and
currently with a market share of around 7.4%.

14 Jha, et al.
2022-07 2022-09 2022-11 2023-01 2023-03 2023-05 2023-07
0
500
1000
1500
2000
2500# of sites
Fig. 9. Evolution of the number of sites with at least 1 daily recorded interaction in the illow.io dataset.
We complete the analysis by providing the most recent snapshot of the worldwide CMP market share. We rely on the
top-ranked 1 million websites as of December 2023 in the HTTP-Dec23 dataset, where 13.1% of them adopts a CMP (see
Table 3). Figure 8 details the market share of the top 10 CMPs worldwide. We find most of the CMP already presented in
Figure 7, even if with a different rank and share due to the different website bases. The leader is again OneTrust (27.6%
of market share). Funding Choices by Google comes second with 16.1% of market share among the top-1M worldwide
websites. Interestingly, its market share is only 7.4% of European websites existing in all 9 years. This suggests Funding
Choices CMP is especially adopted in non-GDPR countries. Conversely, CookieBot has a market share of 14.7% on the
HTTP-9Years (GDPR) and only 7.3% on HTTP-Dec23, suggesting it is more popular among GDPR countries.
To summarize, CMPs are products born as a result of European privacy regulations. Different countries show
different patterns caused by their internal dynamics and specific implementations of the European directives and
privacy regulations at large. While the market was initially dominated by a few players, nowadays different companies
compete. The availability of longitudinal data as those provided by the HTTP Archive is fundamental for this type of
analysis.
5 USER INTERACTION
In this section, we focus on users’ interaction patterns when facing a Privacy Banner. To this end, we use the proprietary
dataset of the illow.io CMP described in Section 3.2.
In total, illow.io serves more than 6,000 websites all over the world, collecting hundreds of thousands of interactions
daily. In detail, in Figure 9, we show the daily number of websites for which we observe at least one interaction. The
weekly periodicity is due to Sundays which record the least amount of traffic. We first observe that the number of the
CMP’s customer websites grows over time, with a significant increase starting in December 2022 and a second one in
June 2023. Since then, more than 2,000 websites have been active daily. Not shown for brevity, the number of daily
interactions grows proportionally, surpassing 180,000 daily interactions in the last period.
5.1 Longitudinal analysis
We first focus on the evolution of the fraction ofRejected-All interactions. Figure 10 reports the daily averageRejected-All
rate for users connecting from different areas of the world, separately for the GDPR area (Figure 10a) and other notable
countries (Figure 10b). On the contrary to what we define in Section 3.2.2, we remove the 50-websites constraint — so

Privacy Policies and Consent Management Platforms 15
2022-07 2022-09 2022-11 2023-01 2023-03 2023-05 2023-07 2023-09
0
20
40
60
80Rate [%]
A
B C D E
(a) GDPR-regulated countries.
2022-07 2022-09 2022-11 2023-01 2023-03 2023-05 2023-07 2023-09
0
20
40
60
80Rate [%]
Canada
USA (CA, UT)
USA (Other)
Brazil
(b) Other areas.
Fig. 10. The Rejected-All rate in a 14-months period by macro areas.
that we have enough data for most of the days in out 14-months span. Figure 10 thus shows the average among all the
websites with at least ten daily interactions.
Starting from the GDPR area, observe how the curve follows a complicated shape. Each change is a consequence of
changes in the banner design at illow.io. We highlight and describe the five main changes:
• A – Add Reject All button: In August 2022, the CMP changed the banner shown to the GDPR users from
the General – two-buttons banner – to the GDPR-compliant – three-buttons banner. The new banner includes
the Reject All button, allowing users to refuse the usage of non-mandatory cookies with a simple one-click
action. This addition is a consequence of the fine imposed by CNIL (the French data protection authority) on
Google and Facebook in January 202210. This suddenly increases the Rejected-All rate to≈ 20% (we already
observed this behaviour in our previous work [28]).
• B – Add “X” button, activate blurring, top position : In December 2022, the CMP introduced the “Close
banner” “X” button. Clicks on this button are equivalent to aRejected-All choice. Following again the suggestions
10https://www.cnil.fr/sites/cnil/files/atoms/files/deliberation_of_the_restricted_committee_no._san-2021-023_of_31_december_2021_concerning_
google_llc_and_google_ireland_limited.pdf, Accessed on Friday 1 st March, 2024.

16 Jha, et al.
of European privacy-regulation bodies, The CMP also changed the Reject All button to have the same colour
as the Accept All button. The banner is shown by blurring the background and placed in a central position on
the page. This forces the users to interact with the banner to access the website content. Users quickly click on
the “X” or Reject All buttons. In a nutshell, they are more interested in discarding the banner rather than
making an informed decision. The reject rate tops 70% (and 30% explicitly accepting cookies).
• C – Remove blurring; D – central position : In January and March 2023, the CMP took some minor measures
to reduce the Rejected-All rate: they disabled the blurring effect (C), and moved the banner in the bottom position
by default (D). These changes allow the user to see the website content without getting rid of the banner, which
causes a reduction in the Rejected-All rate. The Rejected-All rate drops to 55%. We link this drop to users ignoring
the banner (for which we have no records), rather than intentionally selecting to accept cookies.
• E –lack of data : In May 2023, the data collection was suspended for a short amount of time for technical
reasons.
The same events, although differently combined and at different times, explain the shape that we observe in other
regions in Figure 10b. Focus on Canada (red curve) and Brazil (black curve): The CMP introduced a GDPR-compliant
banner for Brazilians in February 2023 with a configuration similar to A+B (i.e., with the Reject All and “X” buttons).
The presence of the intrusive banner suddenly makes the users close the banner by clicking on the “X” which is
equivalent to selecting Rejected-All. In April 2023, the CMP defaults to C+D, reducing the Rejected-All rate by users. The
same happens in Canada where users start interacting with the GPDR-compliant banner in July 2023.
For other countries, the CMP shows the General banner with neither the “X” nor the Reject All button (see
Figure 2a). The Rejected-All rate is far lower and barely reaches 10%. In this case, a user who would like to disable the
usage of profiling and tracking cookies has to perform multiple clicks. This burden makes the user prefer to either
ignore the banner or quickly select the Accept All button to dismiss the banner.
In a nutshell, users aim to quickly close the banner. Less than 10% of them go through the burden of manually
disabling the data collection when more than one click is needed. When the Reject All button is present, users select
it in 20% of cases. When the “X” button is present (and equivalent to the Reject All action), users just click on it to
quickly close the privacy banner.
For completeness, the curves in Figure 10 include the per-region average Rejected-All rate if at least 10 interactions
are collected for the given samples (i.e., at least 10 interactions on a website by users from the given region). This causes
the curves to be noisy and possibly lack some points, especially in the early months when the number of interactions is
low – see Figure 9.
5.2 Stationary analysis
We now focus on the last two months of illow.io data (from July 5th to the end of August ’23, highlighted in grey in
previous plots). By doing so, we ensure that the CMP operation is not changing, allowing us to drill down the analysis.
In Figure 11 we break down the Rejected-All rate based on users’ country. To only show the most represented
countries, we show countries with at least 50 websites recording 50 visits in the observation period — rather than
only 10 visits. The main differences are ascribable to the different versions of the banner the users are shown. The
Rejected-All rate varies between 45% and 65% for countries with a GDPR-compliant banner (which include Brazil and
Canada). Conversely, countries with default banners do not exceed the 10%Rejected-All rate. We attribute the differences

Privacy Policies and Consent Management Platforms 17
PolandItalyFrancePortugalRomaniaGermanySpain Netherlands SwedenAustria UKIrelandBelgiumBrazilMexicoArgentinaColombiaCanada USA (Other)USA (CA, UT)
0
20
40
60
80Rate [%]
GDPR-regulated South America North America
Fig. 11. The Rejected-All rate per country. illow.io dataset from July 3rd, 2023.
Firefox Android
Firefox PC
Chrome MobileSamsung Internet
Edge PCSafari PCChrome PCFacebookInstagramMobile Safari
Chrome Mobile iOS
Google
0
20
40
60
80
100Rate [%]
Mobile browsers PC browsers App browsers
Fig. 12. Average Rejected-All rate by browsers. illow.io dataset from July 1st, 2023.
among countries with the same banner to different cultural habits, as differences are consistent across all of our dataset
dimensions. As an example, we compare the Rejected-All rate for Italy and UK in Appendix B.
Peculiar is the case of California and Utah, where users face the CCPA-compliant banner (as in Figure 2c). The
Rejected-All rate for these two states (6.6%) is only moderately lower than in the remaining states of the U.S. (8.8%),
where users are offered the General banner (as in Figure 2a. These numbers are interesting if we focus on how the two
types of banners operate. The CCPA-compliant banner is based on the opt-out mechanism – i.e., if the user ignores or
closes the banner, the consent is presumed. Conversely, with, the General banner, the user must explicitly opt in to
cookies, although opting in is faster and easier than opting out (which requires accessing the selection windows). The
opt-in mechanism is considered more respectful of users’ privacy, but our results show that, when the banner design
encourages users to opt in, the practical effect is almost comparable to an opt-out banner.
We now focus on other aspects and study how the user’s browser and device impact the behaviour with privacy
banners. In Figure 12, we compare the Rejected-All rate for users using different browsers to surf the Internet. We focus
on users facing a GDPR-compliant banner, and we group the browsers into three categories for ease of visualization.

18 Jha, et al.
0 20 40 60 80
Android rate [%]
0
20
40
60
80iOS rate [%]
GDPR
General
CCPA
Fig. 13. Android vs iOS: Average Rejected-All rate for users in each country, since July 3rd, 2023. The dotted lines represent a±5%
difference.
• Mobile browsers – red pattern : full browsers operating on a mobile device, such as a smartphone or a tablet.
Among them, we include Chrome Mobile, Samsung Internet, and Firefox Mobile on Android devices, and the
Mobile Safari and Chrome Mobile for iOS on iOS and iPadOS devices.
• PC browsers – green pattern : full browsers operating on a laptop or desktop computer. We include Google
Chrome, Safari, Edge, and Firefox.
• App browsers – blue pattern : in-app browsers offered by popular applications on smartphones and tablets.
These apps let the user browse websites in the app when they click a link. We observe a significant usage of
Facebook, Instagram, and Google Search apps directly requesting and showing webpages to users.
Interestingly, Firefox stands first among both Android and PC browsers. Although we cannot prove any hypothesis
on this outcome, we argue Firefox users are careful about their privacy and tend to refuse the use of cookies more
often than other users. At the opposite edge, users navigating app browsers tend to refuse less. This behaviour might
have multiple causes: for example, users inside a third-party app’s environment might be less encouraged to make an
informed choice about cookies, given the unusual surfing context they are in. Or the more occasional browsing makes
them quickly return to the app without spending time on the webpage content.
We now draw attention to mobile, comparing the behaviour of Android and iOS users, for which we find notable
differences. In general, we find that Android users have high Rejected-All rates (see for example Firefox Android in
Figure 12): this may be caused by the large relative banner area which covers a large fraction of the screen. Users
quickly dismiss the banner by clicking on the “X” more frequently on a mobile than on a desktop browser (we will
investigate this later). However, for iOS users, the picture is different – for instance, Mobile Safari and Chrome Mobile
iOS stand in the last positions in Figure 12. We explore the remarkable differences between Android and iOS users more
in-depth in Figure 13. For every country, we plot the Rejected-All rate for users using Android versus iOS operating
system. We consider countries with at least 10 websites with 50 interactions each. The diagonal dashed lines represent a
±5% difference. Interestingly enough, in every country we observe iOS users present a significantly smaller Rejected-All
rate than Android users. Our data cannot offer us any insight into the reason for this difference. We hypothesize this

Privacy Policies and Consent Management Platforms 19
Firefox Android
Firefox PCEdge PCSafari PCChrome PC
Chrome MobileSamsung Internet
InstagramFacebookMobile Safari
Chrome Mobile iOS
Google
0
20
40
60
80Rate [%]
Bo/t_tom Squared Le/f_t
Fig. 14. Average Rejected-All rate by browsers, divided by banner position. illow.io dataset since July 3rd, 2023.
could be due to iOS users being more confident about their privacy than their Android counterparts because of the
feeling of privacy-friendly solutions offered by the Apple ecosystem.
At last, we differentiate the outcome with respect to the Privacy Banner position on the screen. We consider the two
most popular banner options: Bottom, i.e., the banner appears on the lower part of the screen - covering a portion of
the bottom area with an overlay window; Squared Left, i.e., the banner appears as a pop-up in the bottom-left corner
of the screen (see Figure 2), resulting more visible. In Figure 14, we observe that the position of the banner makes a
significant difference only on Desktop browsers. In fact, the banners overlayed on the bottom of the page register a
lower Rejected-All rate than the Squared Left pop-up style banner. This hints at users being annoyed by the pop-up
banner window, nudging more people to dismiss it via the “X” button to freely access the page. In Mobile and App
browsers on smartphones and tablets, there is no significant difference in the Rejected-All rate between the two types of
banners. This is because there is practically no difference between the layout of the Bottom and of the Squared Left
banners - both covering a large fraction of the mobile device screen.
5.3 Other findings
Here we report some additional findings regarding users’ interaction with the illow.io Privacy Banner.
• Access to Cookie Policy and the Privacy Policy: from August 2022 to April 2023, the illow.io dataset reports
clicks on the Cookie Policy and the Privacy Policy links offered by the banner. Only 0.22% of users explore this
possibility and click on at least one of the two policies. It stands clear that common website visitors are not
interested in spending time reading long and detailed policy text.
• Fine-grained consent: few users choose to fine-tune the categories of cookies they are willing to accept. In
the whole illow.io dataset, we only count 8,297 interactions which offered a partial acceptance over almost 25
million interactions. The statistics category is the most accepted one (62.77± 1.04%), followed by preferences
(52.95± 1.07%). The marketing category (arguably the one most associated with the feeling of privacy lack)
is the least accepted one (19.63± 0.85%). All confidence intervals are computed with a 95% probability on a
per-website grouping.

20 Jha, et al.
6 CONCLUSION
In this paper we discussed different aspects related to Consent Management Platforms, considering both their penetration
into the web ecosystem and the way users interact with them.
Thanks to the long-lasting effort of the HTTP Archive, we showed the significant growth of CMP adoption on
the web to ease the management of different and evolving privacy regulations. We witnessed that the CMP adoption
significantly varies according to their region and when the privacy regulations entered into force. Thanks to the GDPR,
Europe leads the CMP adoption, with other regions of the world growing quickly when regulation enters into force,
generating new opportunities for the CMP market.
Our results also suggest that some websites and CMPs still allow the browser to contact tracking systems and let
them install persistent cookies before the user accepts their use. However, the limitations of the HTTP Archive call
for further investigations to verify whether this corresponds to an actual violation of privacy legislation. At large,
this shows the need to extend the availability of archiving platforms like HTTP Archive due to the intertwining of
the regulations, user location, device type, language, etc. In fact, the customisation of content websites serve to users
includes the way CMPs show the privacy banners and their actions.
Considering users’ interactions with CMPs, our results showed that, when offered a viable option to refuse data
collection, users tend to do so. Even more clearly, we showed that a large percentage of users tend to dismiss the
Privacy Banner without actively interacting with it, but simply clicking on the close button if present, without making
any explicit decision about their privacy. Such behaviour challenges the concept that offering users fine-grained
options about their privacy empowers them to make the best decision. For instance, when bugged with more intrusive
banners, the reject rate increases inflated by the need to close the banner. Conversely, when refusing data collection is
cumbersome and requires more than one click, users tend not to take the opportunity. Interestingly, with an opt-out
banner, where, by default, consent is presumed, the rejection rate is similar.
Finally, our results showed that users operating on mobile devices are apparently the most keen to refuse the use of
data collection – in fact they just to counterbalance the intrusiveness of the banner on mobile device screens. Curiously,
iOS users tend to refuse at a lower rate than Android ones. Although we formulate some hypotheses about it, this
observation poses the ground for interesting future work.
ACKNOWLEDGMENTS
This work was partially supported by project SERICS (PE00000014) under the MUR National Recovery and Resilience
Plan funded by the European Union - NextGenerationEU and the project "National Center for HPC, Big Data and
Quantum Computing", CN00000013 (Bando M42C – Investimento 1.4 – Avviso Centri Nazionali” – D.D. n. 3138 of
16.12.2021, funded with MUR Decree n. 1031 of 17.06.2022).
REFERENCES
[1] 2024. AdGuard. https://adguard.com/, Accessed on Friday 1 st March, 2024..
[2] 2024. EasyPrivacy. https://easylist.to/easylist/easyprivacy.txt, Accessed on Friday 1 st March, 2024..
[3] 2024. HTTP Archive. https://httparchive.org/, Accessed on Friday 1 st March, 2024..
[4] 2024. HTTP Archive open dataset used for CMP analysis. https://smartdata.polito.it/consent-management-platforms-growth-and-users-interactions-
over-time/, Accessed on Friday 1st March, 2024..
[5] 2024. Wappalyzer. https://www.wappalyzer.com/, Accessed on Friday 1 st March, 2024.).
[6] 2024. WhoTracks.me. https://whotracks.me/, Accessed on Friday 1 st March, 2024..
[7] Gunes Acar, Christian Eubank, Steven Englehardt, Marc Juarez, Arvind Narayanan, and Claudia Diaz. 2014. The web never forgets: Persistent
tracking mechanisms in the wild. In Proceedings of the 2014 ACM SIGSAC Conference on Computer and Communications Security . 674–689.

Privacy Policies and Consent Management Platforms 21
[8] Susanne Barth and Menno D.T. de Jong. 2017. The privacy paradox – Investigating discrepancies between expressed privacy concerns and actual
online behavior – A systematic literature review. Telematics and Informatics 34, 7 (2017), 1038–1058. https://doi.org/10.1016/j.tele.2017.04.013
[9] Jan M Bauer, Regitze Bergstrøm, and Rune Foss-Madsen. 2021. Are you sure, you want a cookie?–The effects of choice architecture on users’
decisions about sharing private online data. Computers in Human Behavior 120 (2021), 106729.
[10] Brazilian President of the Republic. 2018. Lei Geral de Proteção de Dados Pessoais. http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/
L13709compilado.htm, Accessed on Friday 1st March, 2024..
[11] California State Legislature. 2018. California Consumer Privacy Act of 2018. https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=
201720180AB375, Accessed on Friday 1st March, 2024..
[12] Council of European Union. 2009. Directive 2009/136/EC amending Directive 2002/22/EC on universal service and users’ rights relating to electronic
communications networks and services, Directive 2002/58/EC concerning the processing of personal data and the protection of privacy in the
electronic communications sector and Regulation (EC) No 2006/2004 on cooperation between national authorities responsible for the enforcement
of consumer protection laws. http://eur-lex.europa.eu/legal-content/en/TXT/?uri=CELEX:32009L0136, Accessed on Friday 1 st March, 2024..
[13] Lynne M Coventry, Debora Jeske, John M Blythe, James Turland, and Pam Briggs. 2016. Personality and social framing in privacy decision-making:
A study on cookie acceptance. Frontiers in psychology 7 (2016), 1341.
[14] Adrian Dabrowski, Georg Merzdovnik, Johanna Ullrich, Gerald Sendera, and Edgar Weippl. 2019. Measuring Cookies and Web Privacy in a
Post-GDPR World. In Passive and Active Measurement , David Choffnes and Marinho Barcellos (Eds.). Springer International Publishing, Cham,
258–270.
[15] Data Protection Authorities of Germany. 2024. Orientierungshilfe der Konferenz der unabhängigen Datenschutzaufsichtsbehörden des Bundes und
der Länder vom 20. Dezember 2021 . https://www.datenschutzkonferenz-online.de/media/oh/20211220_oh_telemedien.pdf, Accessed on Friday 1 st
March, 2024..
[16] Martin Degeling, Christine Utz, Christopher Lentzsch, Henry Hosseini, Florian Schaub, and Thorsten Holz. 2019. We Value Your Privacy... Now
Take Some Cookies. Informatik Spektrum 42, 5 (2019), 345–346.
[17] Deloitte. 2020. Cookie Benchmark Study. https://www2.deloitte.com/content/dam/Deloitte/nl/Documents/risk/deloitte-nl-risk-cookie-benchmark-
study.pdf, Accessed on Friday 1st March, 2024..
[18] Rob van Eijk, Hadi Asghari, Philipp Winter, and Arvind Narayanan. 2019. The impact of user location on cookie notices (inside and outside of the
European union). In Workshop on Technology and Consumer Protection (ConPro’19) .
[19] Steven Englehardt and Arvind Narayanan. 2016. Online tracking: A 1-million-site measurement and analysis. In Proceedings of the 2016 ACM
SIGSAC conference on computer and communications security . 1388–1401.
[20] José Estrada-Jiménez, Javier Parra-Arnau, Ana Rodríguez-Hoyos, and Jordi Forné. 2017. Online advertising: Analysis of privacy threats and
protection approaches. Computer Communications 100 (2017), 32–51.
[21] European Parliament and Council of European Union. 2016. Directive 95/46/EC. General Data Protection Regulation.
http://data.consilium.europa.eu/doc/document/ST-5419-2016-INIT/en/pdf, Accessed on Friday 1 st March, 2024..
[22] Jens Grossklags and Nathan Good. 2007. Empirical studies on software notices to inform policy makers and usability designers. In International
Conference on Financial Cryptography and Data Security . Springer, 341–355.
[23] Hana Habib, Megan Li, Ellie Young, and Lorrie Cranor. 2022. “Okay, whatever”’: An Evaluation of Cookie Consent Interfaces. In Proceedings of the
2022 CHI Conference on Human Factors in Computing Systems . 1–27.
[24] Hana Habib, Sarah Pearman, Jiamin Wang, Yixin Zou, Alessandro Acquisti, Lorrie Faith Cranor, Norman Sadeh, and Florian Schaub. 2020. "It’s
a scavenger hunt": Usability of Websites’ Opt-Out and Data Deletion Choices. In Proceedings of the 2020 CHI Conference on Human Factors in
Computing Systems (<conf-loc>, <city>Honolulu</city>, <state>HI</state>, <country>USA</country>, </conf-loc>) (CHI ’20). Association for
Computing Machinery, New York, NY, USA, 1–12. https://doi.org/10.1145/3313831.3376511
[25] Philip Hausner and Michael Gertz. 2021. Dark Patterns in the Interaction with Cookie Banners. arXiv preprint arXiv:2103.14956 (2021).
[26] Maximilian Hils, Daniel W. Woods, and Rainer Böhme. 2020. Measuring the Emergence of Consent Management on the Web. InProceedings of
the ACM Internet Measurement Conference (Virtual Event, USA) (IMC ’20). Association for Computing Machinery, New York, NY, USA, 317–332.
https://doi.org/10.1145/3419394.3423647
[27] Italian Data Protection Authority. 2024. Chiarimenti in merito all’attuazione della normativa in materia di cookie. https://www.garanteprivacy.it/
web/guest/home/docweb/-/docweb-display/docweb/4006878, Accessed on Friday 1 st March, 2024..
[28] Nikhil Jha, Martino Trevisan, Marco Mellia, Rodrigo Irarrazaval, and Daniel Fernandez. 2023. I Refuse if You Let Me: Studying User Behavior with
Privacy Banners at Scale. In 2023 7th Network Traffic Measurement and Analysis Conference (TMA) . 1–9. https://doi.org/10.23919/TMA58422.2023.
10198936
[29] Nikhil Jha, Martino Trevisan, Luca Vassio, and Marco Mellia. 2022. The Internet with privacy policies: Measuring the Web upon consent. ACM
Transactions on the Web (TWEB) 16, 3 (2022), 1–24.
[30] Michael Kretschmer, Jan Pennekamp, and Klaus Wehrle. 2021. Cookie Banners and Privacy Policies: Measuring the Impact of the GDPR on the Web.
ACM Trans. Web 15, 4, Article 20 (jul 2021), 42 pages. https://doi.org/10.1145/3466722
[31] Oksana Kulyk, Willard Rafnsson, Ida Marie Borberg, and Rene Hougard Pedersen. 2022. “So I Sold My Soul”: Effects of Dark Patterns in Cookie
Notices on End-User Behavior and Perceptions. In Proceedings of 2022 Symposium on Usable Security and Privacy . Internet society.

22 Jha, et al.
[32] Thomas Linden, Rishabh Khandelwal, Hamza Harkous, and Kassem Fawaz. 2020. The Privacy Policy Landscape After the GDPR. Proceedings on
Privacy Enhancing Technologies 2020, 1 (2020), 47–64.
[33] Célestin Matte, Nataliia Bielova, and Cristiana Santos. 2020. Do Cookie Banners Respect my Choice? : Measuring Legal Compliance of Banners
from IAB Europe’s Transparency and Consent Framework. In 2020 IEEE Symposium on Security and Privacy (SP) . 791–809. https://doi.org/10.1109/
SP40000.2020.00076
[34] Jonathan R Mayer and John C Mitchell. 2012. Third-party web tracking: Policy and technology. In 2012 IEEE symposium on security and privacy .
IEEE, 413–427.
[35] Hassan Metwalley, Stefano Traverso, Marco Mellia, Stanislav Miskovic, and Mario Baldi. 2015. The online tracking horde: a view from passive
measurements. In International Workshop on Traffic Monitoring and Analysis . Springer, 111–125.
[36] National Assembly of Québec. 2021. An Act to modernize legislative provisions as regards the protection of personal information. https:
//www.publicationsduquebec.gouv.qc.ca/fileadmin/Fichiers_client/lois_et_reglements/LoisAnnuelles/en/2021/2021C25A.PDF, Accessed on Friday
1st March, 2024..
[37] Midas Nouwens, Ilaria Liccardi, Michael Veale, David Karger, and Lalana Kagal. 2020. Dark Patterns after the GDPR: Scraping Consent Pop-Ups and
Demonstrating Their Influence. In Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems (Honolulu, HI, USA) (CHI ’20).
Association for Computing Machinery, New York, NY, USA, 1–13. https://doi.org/10.1145/3313831.3376321
[38] Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Nicolas Kourtellis, and Evangelos P. Markatos. 2021. User Tracking in the Post-Cookie Era:
How Websites Bypass GDPR Consent to Track Users . Association for Computing Machinery, New York, NY, USA, 2130–2141.
[39] Parliament of Canada. 2000. Personal Information Protection and Electronic Documents Act . https://laws-lois.justice.gc.ca/eng/acts/p-8.6/, Accessed
on Friday 1st March, 2024..
[40] Parliament of Canada. 2023. An Act to enact the Consumer Privacy Protection Act, the Personal Information and Data Protection Tribunal Act and the
Artificial Intelligence and Data Act and to make consequential and related amendments to other Acts. https://www.parl.ca/legisinfo/en/bill/44-1/c-27,
Accessed on Friday 1st March, 2024..
[41] Enric Pujol, Oliver Hohlfeld, and Anja Feldmann. 2015. Annoyed users: Ads and ad-block usage in the wild. In Proceedings of the 2015 Internet
Measurement Conference. 93–106.
[42] Van Bavel R and Rodriguez Priego N. 2016. Testing the Effect of the Cookie Banners on Behaviour. LF-NA-28287-EN-N (2016). https://doi.org/10.
2791/22197
[43] Valentino Rizzo, Stefano Traverso, and Marco Mellia. 2021. Unveiling web fingerprinting in the wild via code mining and machine learning.
Proceedings on Privacy Enhancing Technologies 2021, 1 (2021), 43–63.
[44] Iskander Sanchez-Rola, Matteo Dell’Amico, Platon Kotzias, Davide Balzarotti, Leyla Bilge, Pierre-Antoine Vervier, and Igor Santos. 2019. Can I
Opt Out Yet? GDPR and the Global Illusion of Cookie Control. In Proceedings of the 2019 ACM Asia Conference on Computer and Communications
Security (Auckland, New Zealand) (Asia CCS ’19). Association for Computing Machinery, New York, NY, USA, 340–351. https://doi.org/10.1145/
3321705.3329806
[45] Ashutosh Kumar Singh, Nisarg Upadhyaya, Arka Seth, Xuehui Hu, Nishanth Sastry, and Mainack Mondal. 2022. What Cookie Consent Notices Do
Users Prefer: A Study In The Wild. In Proceedings of the 2022 European Symposium on Usable Security . 28–39.
[46] Janice C Sipior, Burke T Ward, and Ruben A Mendoza. 2011. Online privacy concerns associated with cookies, flash cookies, and web beacons.
Journal of internet commerce 10, 1 (2011), 1–16.
[47] Than Htut Soe, Oda Elise Nordberg, Frode Guribye, and Marija Slavkovik. 2020. Circumvention by Design - Dark Patterns in Cookie Consent for
Online News Outlets. In Proceedings of the 11th Nordic Conference on Human-Computer Interaction: Shaping Experiences, Shaping Society (Tallinn,
Estonia) (NordiCHI ’20). Association for Computing Machinery, New York, NY, USA, Article 19, 12 pages. https://doi.org/10.1145/3419249.3420132
[48] Martino Trevisan, Stefano Traverso, Eleonora Bassi, and Marco Mellia. 2019. 4 Years of EU Cookie Law: Results and Lessons Learned. Proc. Priv.
Enhancing Technol. 2019, 2 (2019), 126–145.
[49] Christine Utz, Martin Degeling, Sascha Fahl, Florian Schaub, and Thorsten Holz. 2019. (Un)Informed Consent: Studying GDPR Consent Notices
in the Field. In Proceedings of the 2019 ACM SIGSAC Conference on Computer and Communications Security (London, United Kingdom) (CCS ’19).
Association for Computing Machinery, New York, NY, USA, 973–990. https://doi.org/10.1145/3319535.3354212
[50] Tony Vila, Rachel Greenstadt, and David Molnar. 2003. Why we can’t be bothered to read privacy policies models of privacy economics as a lemons
market. In Proceedings of the 5th international conference on Electronic commerce . 403–407.
A DATASET STRUCTURES
In this Appendix, we provide the exact structure of our two datasets. Both datasets are in tabular format, and, in the
following paragraphs, we report the columns relevant to our analysis (we omit other columns, useless for our purposes).

Privacy Policies and Consent Management Platforms 23
A.1 HTTP Archive
We use the public data offered by the HTTP-Archive to build the HTTP-9Years and HTTP-Dec23 datasets. The pre-
processed data and the code to obtain the figures of this paper are available online [4]. In particular, we downloaded via
Google Cloud Storage the tables called Summary Pages and Summary Requests, containing details on the visited pages
and all issued HTTP requests, respectively. We downloaded the tables for the 9 years of interest. Relevant columns are:
• Summary Pages:
– Numerical identifier of the visit
– URL of the visited website
– Time of the visit
• Summary Requests:
– Identifier of the corresponding visit
– URL requested by the browser in the HTTP request
– Presence of the Set-Cookie header. The dataset does not include the content of the Cookie.
A.2 illow.io CMP dataset
This dataset is contained in a single data table, where each entry corresponds to an interaction. The columns relevant to
our analysis are:
• Time of the interaction
• Anonymous identifier of the interaction
• Anonymous identifier of the website
• Client’s/24 IPv4 subnet
• Client’s User-Agent as set by the browser in the HTTP requests
• Consents Provided among the following Cookie categories:
– Necessary (always present)
– Statistical
– Preferential
– Marketing
B ITALY VS UK
Here, we compare the Rejected-All rate of Italy and the UK to show that consistent differences exist across all of the
dimensions of our dataset. We presume that the differences in rates between the two countries (as shown in Figure 11)
only depend on users’ cultural habits.
In Figure 15, we compare the Rejected-All rate by Italian and British users. The distance between the two countries
has been sizeable and stable since the beginning of 2023. We can thus exclude that any variation in the CMP operation
has biased the measurement.
In Figure 16, we partition the dataset across the most popular browsers. The Rejected-All rate for Italy is always
higher than for the UK, regardless of the considered browser (although for some of them, the distance is minimal –
e.g., Firefox PC). We can also rule out that the difference between the two countries is due to the different browser
popularity. With the information at our disposal, we thus assume the difference is attributable to different cultural
habits among the populations.

24 Jha, et al.
2022-07 2022-09 2022-11 2023-01 2023-03 2023-05 2023-07 2023-09
0
20
40
60
80Rate [%]
Italy
UK
Fig. 15. The Rejected-All rate of Italy and UK.
Firefox PC
Chrome Mobile
Chrome PCEdge PCSafari PC
Samsung Internet
Mobile Safari
Chrome Mobile iOS
InstagramFacebook Google
0
20
40
60
80Rate [%]
Italy UK
Fig. 16. The Rejected-All rate of Italy and UK.
