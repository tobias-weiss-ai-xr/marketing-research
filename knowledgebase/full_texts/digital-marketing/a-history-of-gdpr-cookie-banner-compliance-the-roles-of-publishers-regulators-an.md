---
title: 'A history of GDPR cookie banner compliance: the roles of publishers, regulators and CMPs'
url: https://arxiv.org/abs/2606.31485
category: digital-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Yana Dimova
- Vincent Toubiana
- Tom Van Goethem
- Lieven Desmet
- Wouter Joosen
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.31485
pages: 26
chars: 67580
fetched_at: '2026-11-08T13:10:01+00:00'
kb_version: 1
---

# A history of GDPR cookie banner compliance: the roles of publishers, regulators and CMPs

A history of GDPR cookie banner compliance:
the roles of publishers, regulators and CMPs
Yana Dimova1[0000−0001−6558−2062], Vincent Toubiana2[0009−0004−9968−1447],
Tom Van Goethem1[0000−0001−6846−9081], Lieven Desmet1[0000−0001−5155−7472],
and Wouter Joosen1[0000−0002−7710−5092]
1 DistriNet, KU Leuven, Belgium{firstname.lastname}@kuleuven.be
2 CNIL, Francevtoubiana@cnil.fr
Abstract.Since the introduction of the GDPR in 2018, cookie banners
have become the primary mechanism for users to express preferences
on online tracking and advertising. Consequently, their visual design
and the options they present significantly influence user choice. Over
time, the cookie banner landscape has evolved under the influence of key
players, including publishers (website owners), regulators, and Consent
Management Platforms (CMPs). This paper presents an in-depth anal-
ysis of the roles of these three key actors and an examination of their
impact on cookie banners’ design and implementation within the con-
text of EU law. Our results, based on a historical evaluation of 11,364
websites across 30 countries, indicate a positive evolution in the privacy
landscape, with the compliance rate for websites featuring a “reject all”
button increasing from 2.94% in 2018 to 30.66% in 2024. We analyze
Data Protection Authority (DPA) activity and find a clear correlation
betweenhighercomplianceratesandstrongerregulatoryactionandguid-
ance. Our experiments further show that compliance improvements are
primarily driven by website owners, with CMPs showing little response
to regulatory action or (indirect) influence on compliance rates. Our find-
ings highlight the importance of more uniform collaboration and guid-
ance among EU-level regulators to reduce interpretive divergence and
simplify cookie banner compliance, as well as the need for regulatory
oversight of CMPs, which in turn could significantly enhance privacy for
many websites and users. Our work provides a foundation for academics,
regulators, and industry to develop more effective strategies to motivate
key players and promote greater user privacy.
Keywords:Cookie banners·GDPR compliance·CMPs
1 Introduction
The General Data Protection Regulation (GDPR), which came into effect in
May 2018, established a more formal definition of online consent. This had a
significant impact on the ePrivacy Directive, which requires publishers to obtain
valid consent before placing cookies on users’ devices. Consequently, “Cookie
arXiv:2606.31485v2  [cs.CY]  2 Jul 2026

2 Y. Dimova et al.
Banners” have become the most visible manifestation of this new consent re-
quirement, prompting publishers to adopt them on any website visited by EU
data subjects.
While prior work has studied the positive changes due to the GDPR [12],
it has also highlighted the persistence of non-compliant interfaces [5,6] and
their variation across geographical regions [47,52]. These non-compliant ban-
ners often include manipulative designs, that subtly nudge users toward less
privacy-friendly choices [53,37]. While problematic design of cookie banners has
been studied by prior work, less focus has been put on motivation behind com-
pliance. In fact, DPAs have played a crucial role in addressing such issues of
non-compliance.
Their function is twofold: issuing guidance to clarify legal ambiguities and
executing enforcement actions. For example, in December 2021, the French DPA
(CNIL) sanctioned Google and Meta for failing to provide a “reject” button on
the same layer as the “accept” option [46,45]. Consequently, Google updated its
banner design across the EU [1], with Meta adopting similar changes outside of
France [13].
The CNIL case demonstrates that DPA enforcement exerts a direct extra-
territorial impact. We examine the extent of these “ripple effects” across EU
countries and websites, focusing on longitudinal regulatory influence. Our results
reveal substantial variation in banner implementation, highlighting the pivotal
role of DPA guidance and enforcement in driving compliance, and the need for
technical standardization of consent.
Simultaneously, in response to the consent obligations under the GDPR, a
new industry of specialized actors emerged: CMPs. Many publishers rely on
CMPs to customize and deploy cookie banners on their website [34,31]. There-
fore, CMP design decisions have a broad influence on overall compliance. We
hypothesized that CMPs would respond to regulatory pressure and gradually
converge toward a common set of GDPR-compliant and privacy-friendly cookie
banner interfaces. However, our results show the opposite. An examination of
consent interfaces from 18 CMPs shows substantial divergence, even among web-
sites that only recently adopted a CMP. Among the five most widely used CMPs,
for example, Cookiebot includes a reject button on 55.16% of pages, whereas
Cookies Consent does so on only 13.39%. While prior work focuses mainly on
CMP-provided banners, our comparison of CMP and in-house banners reveals
that CMPs have contributed little to compliance improvements. Instead, most
positivechangesaredrivenbywebsiteownerswhoexplicitlychoosetoimplement
them.
We analyze the historical evolution of cookie banners across 30 countries over
a six-year period (2018–2024). To achieve this, we introduce a novel method for
replaying cookie banners on archived web pages by combining data from two ma-
jor web archives: the Wayback Machine and HTTPArchive. Our findings reveal a
general positive trend toward greater privacy in cookie banner design over time.
We integrate historical and cross-country perspectives, and dive deeper into the
roles of three key actors (publishers, DPAs and CMPs) and their interactions.

A history of GDPR cookie banner compliance 3
With our findings, we provide a better understanding of the motivations
behind compliance and identify which actors have the greatest impact on the
broader landscape. Our work can also help NGOs, plaintiffs, and regulators in
establishing the most effective actions to increase compliance with regulation.
We summarize our main contributions:
–Alongitudinalanalysisdemonstratingageneralpositivetrendtowardgreater
privacy in cookie banners over a six-year period.
–An examination of cross-country developments, highlighting the crucial role
and positive impact of DPA regulatory actions.
–An investigation of cookie banners provided by 18 CMPs, which measures
their limited influence on compliance and reveals that most privacy-positive
changes are initiated by website owners.
2 Related work
2.1 Web Archives
The use of web archives offers significant advantages in research, notably in fa-
cilitating the reproducibility of web measurements. A comprehensive evaluation
by Hantke et al. [28] of 13 public web archives found that the Internet Archive’s
Wayback Machine achieved the best results in both suitability and performance.
Prior work has leveraged web archives to investigate diverse topics, including the
evolution of web tracking [42], changes in privacy policies [12,44,4], the compo-
sition of the web [2], and the development of security features [51,68,63]. While
related work by Jha et al. [34] has examined the historical and geographical
evolution of CMPs, no prior study, to our knowledge, has utilized web archives
to specifically analyze cookie banners.
2.2 Automated detection of cookie banners
Ouranalysisreliesonpreviouslydevelopedmethodsforautomatedcookiebanner
detection, a topic that has been extensively explored in prior work. A variety
of approaches have been employed, including HTML- or CSS-based filtering of
web page elements [71,37,62], sometimes in combination with manual curation
[35]. Other studies have utilized machine learning models on textual and visual
elements [36] or a combination of multiple such methods [26,30,6]. For example,
Bouhoula et al. [6] present a tool that uses a combination of HTML/CSS filtering
and machine learning to detect and interact with cookie banners, and classify
cookies and declared purposes.
Many studies focus primarily on cookie notices provided by popular CMPs
[53,27,31,37,5] or supported by Interactive Advertising Bureau (IAB) Europe’s
Transparency and Consent Framework (TCF). Detection methods for TCF-
enabled CMPs have included using the TCF consent signal [47,62,74,52], public
lists of CSS selectors [34], or methods that inspect HTTP requests [27,31,34] or
page HTML [53,5], or a combination thereof [37].

4 Y. Dimova et al.
Unlike studies limited to manual analysis or popular CMPs, our research
examines banners from 18 different CMPs alongside custom, in-house solutions.
This broader scope provides a more comprehensive view of the cookie banner
landscape.
2.3 The impact of regulation on cookie banners
Research onconsentbanners oftenaddresses theirinterdisciplinaryaspects.War-
berg et al. [72] examined the evolution of cookie banners on 911 news and media
websites in the EU and US, observing an increase in reject options and a de-
crease in nudging strategies following GDPR enforcement. Similarly, Nouwens et
al. [52] performed a cross-country analysis of the top 10,000 websites and found
that only 15% of consent interfaces were minimally GDPR compliant, with some
country-specificdifferences.OtherstudieshavefocusedontheevolutionofCMPs
[34,31].
Manystudieshavemeasuredcomplianceratesacrossdifferentcountrieswithin
the EU [52,34,12,70,71,35,43], or compared EU and US perspectives [72,64,
71], and even considered an inter-continental scope [62,21]. Most studies offer
only a static, single-point-in-time snapshot. Our work distinguishes itself by pro-
viding a historical, longitudinal analysis over a period of six years, focusing on
the long-term impact of the GDPR.
Thelawfulnessofcookiebannershasalsobeenamajorresearchfocus.Studies
have addressed issues such as implicit consent [38,12,64,48,53,5,70,47,74,62,
66,41,39,3,73,43,6] and the presence of dark patterns [72,53,27,37,66,39,67,
3,6], including pre-checked options [52,48,53,47,74,37,66] and cookie walls [37,
66,41,3]. Large-scale measurement studies have exposed the widespread non-
compliance on cookie banners, finding that 72.2% of websites violated at least
one GDPR requirement [6].
3 Historical evolution of cookie banners
This section examines the historical evolution of cookie banners. We first out-
line our methodology for replaying archived webpage snapshots to automatically
identify GDPR violations. We then analyze trends in banner prevalence and the
evolution of user options over time.
3.1 Methodology
Our study examines the evolution of cookie banners across the EU from 2018
to 2024. Unlike prior research dependent on web crawling, we leverage two of
the largest web archives to retrospectively and automatically analyze historical
snapshots.

A history of GDPR cookie banner compliance 5
Web ArchivesThe HTTPArchive [32] is a valuable open-source dataset that
hasbeentrackingthecompositionofthewebsince2012.Eachmonth,itperforms
crawls of millions of web pages (12 million URLs in the latest period). The result-
ing data is stored in HAR (HTTPArchive) format, a JSON-formatted file that
logsawebbrowser’sinteractionswithawebsite.SinceJuly2018,HTTPArchive’s
crawls have been based on the Chrome User Experience Report (CrUX) [7], a list
of the most visited websites globally. The data, captured from US-based agents,
includes all requests and responses for each web page and is stored on BigQuery.
To the best of our knowledge, no historical web archives of comparable scale or
completeness exist from an EU perspective.
To ensure comprehensive capture of dynamic cookie banners, we supple-
mented HTTPArchive snapshots with data from the Wayback Machine [33]. This
dual-archive approach is essential because HTTPArchive occasionally misses dy-
namic request chains required to load CMP banners. By using the Wayback
Machine’s API to retrieve missing resources, we can accurately replay historical
banners in their entirety.
ReplayingwebpagesWeuseamulti-tieredapproachcombiningHTTPArchive
andtheWaybackMachine.First,weextractrelevantsnapshotsfromHTTPArchive
and store them locally, then preprocess the data to address missing or incom-
plete response bodies, which are common due to HTTPArchive’s cutoff limits.
For each resource, we check for missing bodies and, if found, attempt retrieval
via the Wayback Machine’s API, ignoring images and fonts as they are unnec-
essary for banner layouts and omitted by HTTPArchive by default. This step is
crucial for managing the Wayback Machine’s rate limit of 60 requests per minute
[15]. Without this pre-emptive approach, attempting to retrieve all missing re-
sources on the fly would significantly slow down our crawler, with each page
taking several minutes to replay.
To replay pre-completed snapshots, we instruct the browser to visit selected
URLs through an HTTP proxy that intercepts traffic and redirects requests
to archived snapshots. If a resource is missing, we fetch it from the Wayback
Machine. If the resource is not available in both archives, we return an empty
response.Thisensuresallinteractionsremainofflineandpreventsanyconnection
to the live web.
Website selectionWhile past studies have looked at the immediate effects of
the GDPR in May 2018, our work examined its long-term impact on websites in
all 30 EEA countries (27 EU countries, Norway, Liechtenstein and Iceland).
To select our sample, we filtered the CrUX list by country code top-level
domain (ccTLD) (e.g.,.frfor France). From this set, we identified websites with
available snapshots spanning the entire analysis period. Finally, we randomly
selected 500 websites per country. Because some countries had fewer than 500
websites available in CRuX (see Table 1), our final dataset consists of 11,364
websites.

6 Y. Dimova et al.
Total
Austria
Belgium
Bulgaria
Croatia
Cyprus
Czech
Denmark
Estonia
Finland
France
Germany
Greece
Hungary
Ireland
Italy
Latvia
Lithuania
Luxembourg
Malta
Netherlands
Poland
Portugal
Romania
Slovakia
Slovenia
Spain
Sweden
Iceland
Liechtenstein
Norway
Number of
websites 11364 500 500 377 320 30 500 500 190 500 500 500 500 500 500 500 182 316 65 19 500 500 500 500 500 247 500 500 109 9 500
Max detected
banners 4060 155 178 128 131 9 194 112 73 151 137 172 176 220 190 154 95 138 16 9 149 217 166 205 212 116 196 184 37 1 139
Detected
banners 2479 99 100 85 94 4 103 66 24 52 81 92 111 157 114 106 50 92 8 7 93 163 111 131 124 96 148 109 20 1 38
T able 1.The first row of this table shows the number of websites crawled for each
country. The second row shows the maximum number of cookie banners detected (in
September 2024). The third row shows the number of websites which include a cookie
banner throughout the whole analysis period.
We select country-code top-level domains (ccTLDs) for two reasons. First,
this ensures the dataset represents popular websites within each target country.
Second, although snapshots are captured via US-based IP addresses, ccTLDs
target European audiences, as confirmed in thePammer and Alpenhofcase [17,
18]. Therefore, these websites fall within the territorial scope of GDPR Article
3 [60].
We performed several analyses to confirm this latter claim. First, we lever-
aged the country-specific CrUX popularity information, and compared the pop-
ularity of sites with an EEA ccTLD to its global popularity. We find that the
vast majority (over 99%) of sites in our dataset are much more popular in the
EEA than globally, clearly indicating that these target European citizens. We
excluded a few exceptions, such as vanity domains (e.g.,linktr.ee) or compro-
mised websites. Second, we confirmed that none of the 11,364 websites in our
dataset redirect from an EU ccTLD to a global, non-EU domain (e.g.,youtu.be
toyoutube.com), which would potentially complicate their GDPR obligations.
Finally, our assessment of the impact of US-based access (detailed in Section 3.2)
shows that 91.6% of cookie banners are captured consistently regardless of the
access location. Our methodology aligns with prior work that adopts a similar
ccTLD-based approach [34].
Cookie banners analysisTo detect and analyze cookie banners, we extended
the automated tool developed by Bouhoula et al. [6]. Built on the OpenWPM
framework, this tool identifies and interacts with banners to report GDPR vio-
lations for both CMP and in-house solutions. We added support for the primary
languages of all 30 target countries by integrating the Google Cloud Translate
API to translate banner text before processing.
The framework locates candidate banners through HTML filtering and z-
index inspection. It then validates these candidates using a language model to
identify cookie-related terms, achieving 100% precision and 86.9% recall. A ma-
chine learning model classifies banner options (e.g., accept, reject, settings) and
links them to specific cookie sets. Finally, cookies are categorized as either 1)
analytics and advertising or 2) essential and session based on their purpose. For
detecting missing “Reject” buttons, the tool yields 91.5% precision and 65.2%

A history of GDPR cookie banner compliance 7
recall, meaning false positives are rare, though some non-compliant banners are
missed. While our findings represent a lower-bound estimate, they remain suit-
able for identifying long-term trends.
Detecting GDPR violationsA multitude of factors dictate compliance with
data protection laws, ranging from the adequacy of user information to the de-
ployment of pre-selected choices and the installation of tracking cookies without
explicit consent. While comprehensive compliance involves complex, qualitative
dimensions, this study focuses on the foundational and objective parameters of
lawful consent. To mitigate inconsistencies arising from divergent national inter-
pretations, such as varying regulations on “cookie walls” [50], we deliberately ex-
clude metrics that require subjective legal judgment. By restricting our analysis
to automatically detectable and consistently interpreted infractions, we ensure
an unbiased assessment that facilitates reliable cross-country and longitudinal
comparisons.
Within this methodological framework, we evaluate cookie banners that de-
ploy tracking cookies and are thus legally mandated to provide an equally ac-
cessible rejection mechanism. The absence of a clear “reject” option violates the
GDPR requirement for freely given consent, which dictates that declining con-
sent must be as effortless as accepting it, a principle firmly upheld by the CNIL
[46] and the EDPB taskforce [20]. Consequently, we utilize this specific consent
requirement as a primary proxy for broader GDPR compliance.
Furthermore, initializing tracking cookies without offering an immediate re-
jectionmechanismviolatestheePrivacyDirective(Art.5.3)[59,19],whichstrictly
requiresprior consentfornon-essentialcookies.Because ourdatacollection simu-
lated access from outside the EU, we cannot definitively confirm actual ePrivacy
violations within our dataset. Therefore, our findings should be interpreted as
potential ePrivacy violations. This extrapolation remains highly robust, given
that our comparative analysis between US and EU vantage points revealed no
significant divergence in website behavior (detailed in Section 3.2).
CrawlsIn the final step, we crawled 11,364 websites across 25 time periods
and 30 countries using an automated detection tool interfaced with archived
snapshots via a proxy. The primary bottleneck was live requests to the Wayback
Machine API, which extended each crawl of 500 websites to approximately 36
hours. The process was deployed on a university cloud network using machines
with 16 GB RAM and 4 CPUs. Out of a total of 284,100 websites (25 time
points multiplied by 11,364 websites), we successfully crawled 277,440 (97.66%)
of them.
3.2 Web Archives: Benefits and Constraints
Webarchivesprovidetemporalstabilitybyeliminatingsomeofthedisadvantages
of live web crawls. However, they present limitations such as browser compati-
bility issues [29] and incomplete resource retrieval [42]. Because some dynamic

8 Y. Dimova et al.
content may be replayed incorrectly, our cookie banner detection rates represent
a lower-bound estimate. We quantify this potential bias through a three-fold
validation.
CMP Detection ComparisonBy matching HTTP requests to known CMP do-
mains (Section 5.1), we found that a substantial share of banners remains uncap-
tured, increasing from 41.49% in 2018 to 49.59% in 2024. However, these missed
banners are distributed across various providers (e.g., Cookiebot, OneTrust),
suggesting our longitudinal trends remain representative of the broader ecosys-
tem.
Manual AnalysisWe manually analyzed 500 websites to assess crawler errors,
archive limitations, and geographical bias. Our automated methodology success-
fully captured 53.2% of banners found manually.
To test IP location bias, we crawled 500 websites with a EU IP address and a
US IP address and compared the results. EU crawls detected 73.72% of banners,
whileUScrawlsdetected64.96%.This8.4%disparityisrelativelylowbecausewe
focused on country-code TLDs (ccTLDs), which, as Van Eijk et al. [71] noted,
often influence compliance more than the visitor’s location, particularly when
compared to generic.comdomains.
Comparison with Prior WorkOur September 2024 detection rate was 35.73%.
While Bouhoula et al. [6] reported 57.16% using the same crawler on live sites,
our lower rate is expected given the archive and geolocation constraints. Our
results align with the broad range found in existing literature, where automated
detection rates vary from 24% [37] to 67% [52]. We conclude that our findings re-
main representative of the broader cookies banners landscape and their evolution
of time, despite the acknowledged limitations.
3.3 Results
We crawled 11,364 websites and detected a cookie banner on 4,060 (35.73%) of
them. The number of cookie banners detected increased continually throughout
the measurement period, as shows in Figure 1. The detection rate varied across
EU countries, from 22.4% in Denmark to 52.2% in Latvia. A detailed country
breakdown is shown in Table 1. Our historical analysis over six years (September
2018–September 2024) shows a steady increase in cookie banner adoption. At
the start, 2,479 (21.81%) websites consistently included a banner. By Septem-
ber 2024, this number rose to 4,060 (35.73%), a 63.78% increase. This growth
aligns with the post-GDPR regulatory landscape. Following GDPR’s introduc-
tion, website owners likely became more aware of their legal obligations to obtain
userconsentfornon-essentialthird-partyservices,suchasanalyticsandtracking,
prompting gradual adoption of cookie banners.

A history of GDPR cookie banner compliance 9
Sep 2018Dec 2018Mar 2019Jun 2019Sep 2019Dec 2019Mar 2020Jun 2020Sep 2020Dec 2020Mar 2021Jun 2021Sep 2021Dec 2021Mar 2022Jun 2022Sep 2022Dec 2022Mar 2023Jun 2023Sep 2023Dec 2023Mar 2024Jun 2024Sep 2024
2400
2600
2800
3000
3200
3400
3600
3800
4000# websites with cookie banners
2479
+ 9.08%
+ 3.18%
+ 2.69%
+ 2.27%
+ 2.42%
+ 2.17%
+ 1.86%
+ 1.92%
+ 1.98%
+ 1.82%
+ 2.33%+ 1.18%
+ 1.61%
+ 2.85%
+ 1.29%+ 1.05%+ 1.01%+ 1.05%
+ 1.1%+ 0.82%
+ 1.18%
+ 2.26%
+ 1.88%
4060
Fig. 1.Number of detected cookie banners throughout time
Cookie banners optionsNext, we examine the evolution of consent options
on cookie banners, focusing on websites that consistently displayed a banner
throughout the analysis period. We categorize these into four types: 1) banners
offering both “accept” and “reject” options, 2) banners with only an ”accept“
option, 3) banners with only a “reject” option, and 4) banners providing no
choice at all.
As shown in Figure 2, which illustrates the evolution of these four types, we
observe several positive trends. First, banners offering both accept and reject
options increased steadily over time, from 73 (2.94%) websites in September
2018 to 760 (30.66%) in September 2024. This reflects a positive shift toward
providing users with more choice.
Second, we note a short-term rise in banners featuring only an “Accept” but-
ton between September 2018 and March 2019. This likely occurred as many
websites initially implemented passive banners following the GDPR’s introduc-
tion. Subsequent regulatory guidance likely prompted website owners to recog-
nize the unlawfulness of this practice, leading them to adapt banners to include
active consent options. Following this period, the number of accept-only banners
declined steadily in favor of banners that include a reject option.
Periods with most changeTo identify during which period cookie banners
became more privacy-focused, we calculated the growth rate of banners offering
both “accept” and “reject” options relative to those that lacked them. These
trends are detailed in Figure 3.

10 Y. Dimova et al.
73
1275
9
997
82
1343
9
1018
86
1358
9
1011
91
1361
8
1009
100
1346
9
1018
113
1360
10
990
127
1352
11
984
151
1347
11
966
164
1348
17
946
184
1353
18
921
229
1324
16
907
247
1337
13
879
273
1327
13
864
306
1296
17
858
380
1272
16
809
416
1257
17
787
443
1220
17
798
480
1191
23
784
507
1185
24
762
540
1159
27
752
584
1124
27
743
625
1085
24
744
683
1039
31
725
731
992
31
725
Accept and reject
Accept only
Reject only
No options
2019 2020 2021 2022 2023 2024
760
978
710
31
Fig. 2.Number of cookie banners over time with “Reject” options, only “Accept” op-
tions, and no options.
We observed two major shifts. The first peak occurred between January and
December 2022, when 7.5% more websites began displaying reject buttons on
their banners. The second period took place toward the end of our analysis,
between December 2023 and September 2024, with an 8.82% increase in banners
offering a reject option.
Itappearsthatasignificantshiftinthecomplianceofcookiebannerinterfaces
occurred in 2022, followed by an even more impactful shift that began in early
2024 and continued until the end of our analysis period. While the main driver
for this positive evolution is not yet clear, it is possible that this behavior will
continue to propagate into late 2024 and 2025.
The changes in cookie banner features can be attributed to numerous factors.
These include country-specific developments, such as regulatory actions, as well
as EU-wide ripple effects (e.g., from cases of the European Court of Justice).
Additionally,websiteownersoftenemployCMPstomanagetheircookiebanners,
which can significantly influence how banners are displayed. We explore these
considerations in Sections 5 and 6.

A history of GDPR cookie banner compliance 11
Fig. 3.This figure shows the growth of “Reject” options relative to banners previously
lacking this feature. We compare the growth in one year starting from the given period,
with the year before. E.g., between September 2019 and June 2020 1.69% more websites
adopted cookie banners with accept and reject options as compared to Sep 2018-Jun
2019.
4 Cross-country analysis
In this section, we shift the perspective from EU-wide trends to country-specific
developments, exploring which countries have experienced the most significant
increase in cookie banner compliance over time.
4.1 Methodology
For the analysis, we rely on the same dataset, described in section 3.1. To assess
how a website’s territorial scope influences its banner, we compare GDPR com-
pliance across countries by focusing on banners without reject options (at any
layer).
ActivitylevelofDPAsOuranalysisfocusesontwodefiningactivitiesforDPA
involvement: the imposition of sanctions and fines for GDPR infringements and
the publication of regulatory guidance (e.g., guidelines, recommendations).
We extracted this information from noyb’s GDPRhub [58], an open-source
wiki summarizing over 2,000 national cases. We identified a total of 287 relevant
cases by searching for the keyword “cookie” in their summaries. This allowed us
to compile the number of cases and total fine amounts in euros for each country.

12 Y. Dimova et al.
Furthermore, we referenced noyb’s “Consent Banner Report” [57] for an overview
of all pertinent EU and national guidelines on cookie banners.
Correlation testTo investigate the relationship between DPA activity and
compliance, we performed a Pearson correlation test. We tested the correlation
between 1) compliance rates and the presence of regulatory guidance (as a binary
parameter), and 2) compliance and enforcement (as measured by the number of
cases).
4.2 Results
Country A vg. banners with Reject(%) Latest banners with Reject (%) # of Cases T otal Fines (EUR) Guidelines Published
Denmark 35.15 60.61 15 — 2020
France 23.51 41.98 43 645 250 000 2020
Austria 20.08 44.44 19 — 2023
Germany 19.61 38.04 25 — 2022
Finland 18.69 44.23 5 1 100 000 2022
Ireland 18.24 40.35 4 225 000 000 2020
Italy 17.66 37.74 21 51 732 546 2021
Netherlands 16.43 25.81 14 1 165 500 2019
Belgium 16.08 31.00 34 604 140 2023
Slovakia 15.36 42.74 — — —
Spain 14.78 43.24 74 37 021 6002019, 2020, 2023
Latvia 14.40 30.00 2 — 2022
Czech Rep. 13.44 39.81 2 14 160 363 unknown
Croatia 13.32 27.66 5 133 000 —
Portugal 12.40 33.33 1 — —
Slovenia 11.38 17.71 — — —
Greece 9.95 20.72 4 440 000 2020
Sweden 9.91 26.61 9 6 955 136 —
Hungary 8.66 20.38 3 25 000 —
Romania 8.18 19.08 5 55 000 —
Bulgaria 6.73 14.12 — — —
Poland 5.89 20.25 2 40 000 —
Lithuania 4.74 14.13 — — —
A verage 14.55 31.91 12.5
T able 2.Compliance rates differences across countries represented by the presence of
“Reject” options. The second column shows the average compliance rate throughout the
whole time period, while the third column refers to the compliance rate in September
2024. DPA activity is represented by the number of cases on cookies, total amount of
fines and the publication of guidelines on cookie banners.

A history of GDPR cookie banner compliance 13
Cross-countrydifferencesCookiebannercompliancevariedsignificantlyacross
countries. Denmark maintained the highest average compliance (35.15%), fol-
lowed by France (23.51%) and Austria (20.08%). By 2024, the top performers
were Denmark (60.61%), Austria (44.44%), and Finland (44.23%).
While Spain (43.24%) and Slovakia (42.74%) reached the top five in 2024,
their lower historical averages suggest a very recent surge in compliance. Con-
versely, Lithuania (4.74%), Poland (5.89%), and Bulgaria (6.73%) consistently
exhibited the lowest compliance rates.
The impact of regulatory actionDPA engagement varies significantly across
the EEA. For instance, the Spanish DPA has processed the most cookie-related
enforcement cases (74), totaling€37,021,600 in fines. Meanwhile, the French
CNIL has levied the highest aggregate fines, totaling€645,250,000 across 43
cases.
Our findings suggest that DPA activity measurably impacts compliance. We
identified a moderate positive correlation between compliance and regulatory
action(r=0.42,p=0.046)and a strong positive correlation with the publica-
tion of regulatory guidance(r=0.62,p=0.002). While other factors, such as a
country’s general privacy stance, reputational risk, and economic considerations,
likely influence compliance, a full evaluation of these multidisciplinary aspects
remains outside this study’s scope.
Case study: FranceIn France, we observe a consistently high compliance rate
throughout the analysis period. The CNIL case likely caused a significant in-
crease in the number of reject buttons after January 2022. As shown in Figure
4, we observe that in March 2022, 16.08% more websites were compliant. The
compliance rate continued to increase, with an additional 21.69% of websites be-
coming compliant by September 2022. This phased increase could be attributed
to some websites making changes immediately after the CNIL ruled Google’s
cookie banner non-compliant (on December 31st, 2021), while others only made
changes months later, after Google announced its intent to redesign its banner
according to CNIL’s guidelines [1] (on April 21, 2022).
The case against Meta and Google appears to have had a significant impact
in France. However, we did not observe a similar increase in compliance after the
CNIL published a recommendation on the use of cookies [9] (in January 2020)
or after the grace period for companies to comply with these guidelines ended
(in March 2021) [8]. France is one of three countries where the evolution of the
compliance rate mimics the global trend, peaking around 2022 and 2024 (the
others being the Czech Republic and Slovakia).
5 Cross-CMP analysis
Website owners frequently rely on CMPs for cookie banner configuration. While
CMPs offer default settings, owners often customize these by adding “reject”

14 Y. Dimova et al.
Fig. 4.Increase in number of banners with reject buttons over time in France
buttons, implementing dark patterns, or modifying button text. Consequently,
CMPs directly shape banner design and user controls, significantly influencing
the overall privacy-friendliness of a site. This section explores the evolving role
of CMPs and their banner implementations over time.
5.1 Methodology
CMP detectionTo identify CMPs on visited websites, we utilized Easylist
Cookie [14], manually filtering the most frequent URL and CSS rules as estab-
lished by Bouhoula et al. [6].
We verified CMP ownership by cross-referencing matched domains with of-
ficial service websites or GitHub implementation documentation. This process
identified 18 distinct CMPs.
CMP typesUsing this method, we detected a total of 18 CMPs. Consistent
with prior research [52,40], we categorize these CMPs into three distinct types.
Twelve companies fall under the category ofComprehensive CMPs, as they offer
a range of services beyond basic consent management, such as website scan-
ning and data insights (e.g., OneTrust, Cookiebot). Two companies are classi-
fied asPlugin CMPs. These are advertised as lightweight solutions that prioritize
easy integration with web applications and frameworks (e.g., Consent Manager,
CookieYes). Finally, four companies belong toOpen-source CMPs, which are de-
signed to be lightweight, freely accessible, and open-source (e.g., Cookie Consent,
Cookie Notice).

A history of GDPR cookie banner compliance 15
5.2 Results
CMP popularityWe observed a significant increase in CMP adoption over
time. The number of websites utilizing CMP banners rose from 1,318 (11.60%)
in 2018 to 4,578 (40.29%) in 2024. Figure 5 illustrates the yearly evolution of
the top 10 most widely used CMPs.
Fig. 5.Number of websites which use the top 10 CMPs over time.
We observe a decline in popularity ofpluginandopen-source CMPs. Many
were widely used immediately after the GDPR’s introduction in 2018. For in-
stance, 53.19% of websites with a CMP employed theCookies Consentframe-
work [49], but this figure dropped to just 5.94% by September 2024. The pop-
ularity of all plugin and open-source CMPs has decreased significantly over the
last few years.
Conversely, the use of more comprehensive CMPs has grown steadily since
2018.Cookiebot[11] saw its prevalence increase from 136 (10.32%) websites in
2018 to 1090 (23.81%) in 2024, potentially because of its merger withUser-
centrics[10]. Similarly, the second-largest comprehensive CMP,OneTrust[61],
has also seen rapid adoption, increasing from 11 websites (0.83%) in 2018 to 917
(20.03%) in 2024.

16 Y. Dimova et al.
Google Funding Choices was introduced in 2018 to manage visits from users
with ad blockers [23]. In 2020, a CMP functionality was added [25], and it is now
integrated with Google’s advertising platforms [24]. In 2024, 727 (15.88%) web-
sites included resources from Google Funding Choices domains. However, this
number represents an upper bound, as it is not possible to distinguish whether
these websites are using the CMP functionality or only the anti-adblocking fea-
ture without having an actual screenshot of the page.
Overall, our findings suggest a consolidation in the market, with smaller play-
ers losing ground to larger, comprehensive CMPs. This indicates that website
owners are increasingly willing to invest in more elaborate, and often more ex-
pensive, CMP solutions, reflecting a greater concern for (apparent) compliance.
Cookie banners across CMPsTo understand how CMPs influence compli-
ance and interface design, we focus on websites utilizing detected CMP-provided
banners. We again employ the presence of a reject option at any layer as a proxy
forcompliance.Inpractice,bannerdeploymentisacollaborationbetweenCMPs,
which provide a default interface, and website owners, which can modify it at any
time. This flexibility makes it difficult to distinguish whether compliance trends
stem from the CMP’s default settings or the owner’s custom adjustments. To
better understand this dynamic between CMPs and publishers, we conduct a
series of experiments.
What do CMP banners look like?In this section, we analyze how CMP-specific
banner designs change over time to evaluate whether CMPs influence the preva-
lence of banners lacking a “reject” button. As shown in Figure 6, there are signifi-
cant differences in compliance rates among various CMPs. For instance, in 2024,
Cookiebot demonstrates a compliance rate of 55.16% and OneTrust 49.19%,
while the rate for Cookies Consent is only 13.39%. This suggests a varying rela-
tionship between the choice of a CMP and the likelihood of having a compliant
banner.ItseemsthatthecookiebannersofsomeCMPsaremoreprivacy-friendly
than in-house banners, as shown by a 2024 compliance rate of only 26.69% for
non-CMP banners.
TheevolutionofspecificCMPsprovidesfurtherinsight.Cookiebothassteadily
evolved toward higher compliance, becoming one of the most widely-used CMPs
by 2024. Its most significant shift toward including more reject buttons occurred
between June 2020 and December 2021, a period that predates the major global
evolution observed in 2022.
In May 2021, noyb filed complaints against 500 OneTrust-using websites
for GDPR violations [54]. By August 2021, 42% of these sites had remediated
their issues [55]. This campaign had a measurable effect in our data: the com-
pliance rate for OneTrust banners rose from 33.33% in March 2021 to 47.47%
in December 2022, following a second wave of enforcement [56]. Because noyb
contacted website owners directly before filing formal complaints, these improve-
ments likely resulted from publishers responding to legal pressure rather than
the CMP proactively driving compliance.

A history of GDPR cookie banner compliance 17
What drives positive changes?When focusing on the evolution of positive change
over time, we observe a similar trend for both CMP and non-CMP banners. This
indicates that major regulatory events, such as the CNIL case in March 2022,
spurred a significant jump in compliance rates across both groups. This shared,
responsive behavior suggests that website publishers actively made changes, in-
stead of CMPs pushing for them.
Furthermore, we compare existing customers (i.e., websites that were already
using the CMP in the previous period) and new CMP customers (i.e., websites
that either switched from one CMP to another or did not include a CMP in the
previous period). We hypothesize that CMPs would actively encourage compli-
ance in both new and existing customers as a result of the CNIL case. For new
customers, this motivation could manifest as updated, more compliant default
settings or clearer information about illegal practices. For existing customers,
CMPs could either notify them of non-compliant banners or, in more extreme
cases, force a change by no longer supporting non-compliant interfaces. However,
our data does not support this hypothesis. As shown in Figure 6, at no point
have all interfaces from major CMPs become compliant. If CMPs were indeed a
primary driver of compliance, we would expect to see a widespread change, such
as 90% of all websites adopting “reject” buttons.

2019

2020

2021

2022

2023

2024

0
50
100# of websites
OneTrust
no options
accept only
reject only
accept and reject

2019

2020

2021

2022

2023

2024

0
50
100
150# of websites
Cookies Consent

2019

2020

2021

2022

2023

2024

0
100
200# of websites
Cookiebot

2019

2020

2021

2022

2023

2024

0
500
1000
1500
2000# of websites
Unknown/No CMP
Fig. 6.Number of cookie banners with “Reject”, “Accept”-only and no options for top
3 CMPs and websites with no CMP

18 Y. Dimova et al.
Consequently, we conclude that CMPs have had a limited impact on this
upward trend in compliance, and show little response to regulatory action.
6 Discussion
Between2018and2024,compliancewithprivacyregulationsamongwebsiteown-
ers has increased, likely due to a combination of factors: the threat of fines and
regulatory action, concerns over reputational damage, and a general increase in
privacy awareness. Although the specific motivator for changes in cookie banner
design is difficult to pinpoint, this paper explores the cross-country impact of
major actors influencing these banners: website owners, regulators and CMPs.
6.1 Historical evolution of cookie banners
Our findings indicate improvements in specific aspects of GDPR compliance. In
2018, only 2.94% of websites offered both accept and reject options. By 2024,
this figure had risen to 30.66%. This improvement was most significant during
two distinct periods. The first major shift occurred in 2022, likely due to a
combination of factors, including a wave of complaints filed by noyb with DPAs
and the CNIL fine targeting the lack of a reject button on the first layer of the
cookie banner.
A second substantial compliance surge occurred in 2024. While difficult to
attribute to a single cause, this shift potentially follows the EDPB’s October
2023 guidelines clarifying the ePrivacy Directive. Increased DPA enforcement
and rising privacy awareness also likely played key roles. Given this momentum,
the trend toward higher compliance will likely persist into 2025 and beyond,
providing a significant area for future study.
We acknowledge that our findings should be interpreted as being lower-
bound, given that the use of web archives proved to result in a variety of
cookie banners being missed by our analysis. Nonetheless, we argue that the
methodology allows us to observe GDPR compliance trends over time. Overall,
our findings show a positive evolution in cookie banner compliance, driven in
part by regulatory action (e.g., case law) and guidance (e.g., EDPB guidelines).
While this progress is positive, new privacy issues, such as manipulation and
user choices not being respected, are still prevalent.
6.2 The role of DPAs
Our results show considerable differences in compliance rates across EU coun-
tries. Denmark, France, and Austria have consistently been part of the top coun-
tries with the greatest compliance, with Spain, Finland, and Slovakia catching
up in 2024. Conversely, Lithuania, Bulgaria, and Slovenia remain at the lower
end of the compliance spectrum.
Higher compliance rates correlate with active DPAs, yet other factors sig-
nificantly influence banner design. Beyond regulators, NGOs like noyb drive

A history of GDPR cookie banner compliance 19
compliance through strategic complaints. Furthermore, a “spillover effect” can
boost compliance in countries with inactive DPAs, such as Slovakia, while oth-
ers like Slovenia remain stagnant due to limited enforcement resources. EU-wide
EDPB guidelines also exert varying degrees of influence across member states,
making it difficult to isolate a single motivation for compliance. Cross-country
divergence complicates compliance further with contradictory regulatory guide-
lines. For example, some DPAs disagree on whether “accept” and “reject” buttons
must be on the same interface level, with the Italian DPA specifically discou-
riging an equal path for both: “the affirmative action the user is empowered to
perform when first accessing a website must in any case be aimed at giving his
or her consent (so-called “opt-in”) and may never consist in refusing such consent
(so-called “opt-out”).” [22].
Our findings document the effect of enforcement on compliance and highlight
the critical importance of DPA collaboration. Many DPAs lack the resources
to counter the behavioral advertising industry’s evolving manipulative tactics,
such as the recentpay-or-consentmodel. Even with adequate resources, the
enforcement process can be challenging and span years, especially when well-
resourced parties are involved. Additionally, the average website often uses third-
party services that operate across multiple EU countries, further complicating
enforcement.
We argue that greater EU-wide uniformity is needed for two primary rea-
sons: first, to foster collaboration, enhancing enforcement and support for web-
site owners; and second, to standardize cookie banner implementations. Such
uniformity could be realized through Article 88b of the Digital Omnibus pro-
posal [16]. Legally mandating a technically supported consent signal (e.g., via
browser vendors) would grant users more control, minimize banner divergence,
streamline regulatory oversight, and ultimately increase compliance.
6.3 The role of CMPs
Market shareOur findings show the growing significance of CMPs as part of
the adtech ecosystem. Their adoption has become increasingly popular, rising
from 11.6% of websites in 2018 to 40.29% in 2024, though this number is likely
higher, as smaller CMPs may have been missed by our methodology. We observe
a market trend where website owners are opting for more comprehensive and
costly privacy solutions. This shift indicates a greater concern for compliance and
a willingness to spend more money on privacy solutions. Consequently, the CMP
market is converging around a few popular players, with OneTrust, Cookiebot,
and Google Funding Choices holding a combined 61.85% market share in 2024.
This dominant position of CMPs has been scrutinized by prior work [52,34]
given their presence on popular websites [31].
How do CMPs influence cookie banners’ design?We found significant
differences in compliance rates among CMPs. For example, in 2024, 55.16% of
websites using Cookiebot included a reject button, compared to only 13.39% of

20 Y. Dimova et al.
sites using Cookies Consent. This contrasts with the 26.69% rate for websites
using their own banner, indicating that the choice of CMP can strongly influence
compliance.Thesecross-CMPvariationsstemfromseveralfactors.Insomecoun-
tries, locally developed CMPs are more common, which helps explain some of
the cross-country differences we’ve observed. Furthermore, certain CMPs might
use manipulative designs during installation, steering website owners toward less
privacy-friendly interfaces [69].
In theory, the evolution of cookie banners on CMP-using websites reflects
both updates made by CMPs and configuration choices made by website owners.
In practice, our results indicate that website owners are the primary drivers
of change. First, regulatory actions are typically directed at website owners,
not the CMPs they use. Regulations may impact CMPs indirectly (as seen in
noyb’s complaints against OneTrust), but it is the website owners who are the
ultimate agents of change. Second, we see a similar rise in compliance over time
onwebsitesthatdon’tuseaCMP,whichsuggestsabroaderincreaseinawareness
among owners. Third, CMPs show little response to regulatory actions and do
not incentivize customers to adopt more compliant configurations.
We conclude that the increased compliance is predominantly due to website
owners intentionally configuring their banners to meet GDPR standards. This
shift is likely fueled by a growing awareness of GDPR violations, driven by
significant enforcement actions (e.g., noyb complaints, the CNIL case) and a
general rise in public concern over privacy and reputational risk.
Responsibility and complianceOur study reveals a positive trend in cookie
banner compliance over time. However, persistent issues like manipulative de-
signs and disregarded user choices raise a fundamental question: who is respon-
sible for compliance? By examining various stakeholders, our results show that
most improvements stem from website owners actively updating their banners.
In contrast, despite their significant market share and close ties to the adtech
ecosystem, CMPs exert limited effort to improve compliance. Because they po-
sition themselves as expert solutions, they effectively set the de facto standard
for cookie banners, leading developers to rely heavily on their default configura-
tions. Furthermore, prior work shows that many website owners are unaware of
the various technologies on their pages and rely on tools such as cookie scans for
compliance [40]. This issue is compounded by the fact that some CMPs include
manipulative designs in their configuration process for new customers [69] and
offer tools like “consent optimization” and A/B testing of interface configurations
that may not serve users’ best interests. CMPs are likely to have more incentive
to maximize user consent, as it might give them a competitive edge with rela-
tion to other market players and help to retain clients. At the very least, this
behavior is misleading to the publishers who rely on their services.
At the same time, website owners retain their own responsibilities. One could
argue that CMPs merely provide the tools, and website owners must still con-
figure them correctly to meet GDPR requirements. Some CMPs might be more

A history of GDPR cookie banner compliance 21
inclined to meet those criteria bu default, in order to guarantee safety from
enforcement actions for their customers.
In practice, we argue that GDPR compliance for cookie banners is a shared
responsibility between CMPs and publishers. There is a clear need for greater
legal accountability for CMPs. Revisiting questions around joint controllership
could help determine when CMPs should be held responsible under the GDPR
[65]. At present, CMPs have little incentive to push for higher compliance and
show minimal response to regulatory actions. Stronger incentives could help
reduce manipulative designs and lead to more efficient improvements in com-
pliance. Additionally, standardizing how users communicate consent would con-
strain CMPs, leaving less room for non-compliant banner interfaces such as those
that lack a clear “Reject” option.
Ultimately, increased regulatory oversight of CMPs would more effectively
scale privacy protections across the web. Based on our findings, we encourage
website owners to be cautious when relying on CMPs’ interfaces and instead,
ensure privacy-friendly cookie banners which align with users’ choices regarding
their privacy on the web.
7 Conclusion
Our findings reveal a complex, evolving landscape of cookie banner compliance
under the GDPR. Compliance rose from 2.94% in 2018 to 30.66% in 2024, driven
by the interplay between publishers, CMPs, and DPAs. A strong correlation
between DPA activity and higher compliance, particularly in France and Spain,
underscores the necessity of consistent enforcement. Conversely, countries with
limited regulatory activity, such as Lithuania, Poland, and Bulgaria, maintain
notably low compliance.
CMPsofferwidelyvaryinginterfaces;forinstance,“reject” optionsrangefrom
55.16% on Cookiebot to only 13.39% on Cookies Consent. Despite their preva-
lence, CMPs have shown little response to regulatory pressure. Instead, com-
pliance improvements appear driven primarily by publishers opting for more
privacy-respecting designs. By analyzing these stakeholders, this study clari-
fies the forces shaping GDPR compliance and the gradual shift toward privacy-
friendly interfaces.
Acknowledgments
This research is partially funded by the Internal Funds KU Leuven, and by the
Cybersecurity Research Program Flanders.
References
1. Adhyae, S.: New cookie choices in europe. https://blog.google/around-the-
globe/google-europe/new-cookie-choices-in-europe/ (2022), last accessed on 30-08-
2025

22 Y. Dimova et al.
2. Agarwal, V., Sastry, N.: “way back then”: A data-driven view of 25+ years of web
evolution. In: Proceedings of the ACM Web Conference 2022. pp. 3471–3479 (2022)
3. Alharbi, J.A., Albesher, A.S., Wahsheh, H.A.: An empirical analysis of e-
governments’ cookie interfaces in 50 countries. Sustainability15(2), 1231 (2023)
4. Amos, R., Acar, G., Lucherini, E., Kshirsagar, M., Narayanan, A., Mayer, J.: Pri-
vacy policies over time: Curation and analysis of a million-document dataset. In:
Proceedings of the Web Conference 2021. pp. 2165–2176 (2021)
5. Bollinger, D., Kubicek, K., Cotrini, C., Basin, D.: Automating cookie consent and
gdpr violation detection. In: 31st USENIX Security Symposium (USENIX Security
22). pp. 2893–2910 (2022)
6. Bouhoula, A., Kubicek, K., Zac, A., Cotrini, C., Basin, D.: Automated large-
scale analysis of cookie notice compliance. In: 33rd USENIX Security Symposium
(USENIX Security 24). pp. 1723–1739 (2024)
7. Chrome UX report: Overview of crux. https://developer.chrome.com/docs/crux
(2024), last accessed on 30-08-2025
8. CNIL: Cookies et autres traceurs : la cnil publie des lignes directrices mod-
ificatives et sa recommandation. https://www.cnil.fr/fr/cookies-et-autres-
traceurs/regles/cookies/lignes-directrices-modificatives-et-recommandation, last
accessed on 13-01-2026
9. CNIL: Délibération n°2020-092 du 17 septembre 2020 portant adop-
tion d’une recommandation proposant des modalités pratiques de mise
en conformité en cas de recours aux “cookies et autres traceurs”.
https://www.cnil.fr/sites/default/files/atoms/files/recommandation-cookies-
et-autres-traceurs.pdf, last accessed on 12-01-2026
10. Cookiebot by Usercentrics: Usercentrics and cookiebot join forces.
https://www.cookiebot.com/en/usercentrics-cookiebot-cmp/ (2022), last ac-
cessed on 30-08-2025
11. Cookiebot by Usercentrics: Automate consent signaling and drive results on top
ad platforms. https://www.cookiebot.com/ (2026), last accessed on 13-01-2026
12. Degeling, M., Utz, C., Lentzsch, C., Hosseini, H., Schaub, F., Holz, T.: We value
your privacy... now take some cookies: Measuring the gdpr’s impact on web privacy.
arXiv preprint arXiv:1808.05096 (2018)
13. Dimova, Y., Franken, G., Le Pochat, V., Joosen, W., Desmet, L.: Tracking the evo-
lution of cookie-based tracking on facebook. In: Proceedings of the 21st Workshop
on Privacy in the Electronic Society. pp. 181–196 (2022)
14. easylist: easylist cookie github repository. https://github.com/easylist/easylist,
last accessed on 30-08-2025
15. edgi-govdata-archiving/wayback:search_calls_per_secondneeds to be dialed
down. https://github.com/edgi-govdata-archiving/wayback/issues/137, last ac-
cessed on 12-01-2026
16. European Comission: Proposal for a regulation of the european parliament
and of the council amending regulations (eu) 2016/679, (eu) 2018/1724, (eu)
2018/1725, (eu) 2023/2854 and directives 2002/58/ec, (eu) 2022/2555 and
(eu) 2022/2557 as regards the simplification of the digital legislative frame-
work, and repealing regulations (eu) 2018/1807, (eu) 2019/1150, (eu) 2022/868,
and directive (eu) 2019/1024 (digital omnibus). https://eur-lex.europa.eu/legal-
content/EN/TXT/?uri=CELEX:52025PC0837 (2026), last accessed on 12-06-2026
17. European Court of Justice: Peter pammer v reederei karl schlüter gmbh & co.
kg (c-585/08) and hotel alpenhof gesmbh v oliver heller (c-144/09). https://eur-
lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:62008CJ0585 (2010),
last accessed on 22-04-2026

A history of GDPR cookie banner compliance 23
18. European Data Protection Board: Guidelines 3/2018 on the territo-
rial scope of the gdpr (article 3). https://www.edpb.europa.eu/our-work-
tools/our-documents/guidelines/guidelines-32018-territorial-scope-gdpr-article-3-
version_en (2019), last accessed on 22-04-2026
19. European Data Protection Board: Adopted 1 guidelines 2/2023 on technical
scope of art. 5(3) of eprivacy directive. https://www.edpb.europa.eu/our-work-
tools/our-documents/guidelines/guidelines-22023-technical-scope-art-53-eprivacy-
directive_en (2023), last accessed on 07-01-2026
20. European Data Protection Board: Report of the work undertaken by
the cookie banner taskforce. https://www.edpb.europa.eu/system/files/2023-
01/edpb_20230118_report_cookie_banner_taskforce_en.pdf (2023), last ac-
cessed on 8-01-2026
21. Fruchter, N., Miao, H., Stevenson, S., Balebako, R.: Variations in tracking in rela-
tion to geographic location. arXiv preprint arXiv:1506.04103 (2015)
22. Garante per la protezione dei dati personali: Linee guida cookie e altri stru-
menti di tracciamento. https://www.garanteprivacy.it/web/guest/home/docweb/-
/docweb-display/docweb/9677876 (2021), last accessed on 30-08-2025
23. Google: Helping publishers recover lost revenue from ad blocking.
https://blog.google/technology/ads/helping-publishers-recover-lost-revenue-
ad-blocking/ (2018), last accessed on 30-01-2025
24. Google: Funding choices has moved. https://support.google.com/fundingchoices
/answer/9010669 (2024), last accessed on 30-01-2025
25. Google Ad Manager: Helping publishers manage consent with funding choices.
https://blog.google/products/admanager/helping-publishers-manage-consent-
funding-choices/ (2024), last accessed on 30-01-2025
26. Gundelach, R., Herrmann, D.: Cookiescanner: An automated tool for detecting
and evaluating gdpr consent notices on websites. In: Proceedings of the 18th In-
ternational Conference on Availability, Reliability and Security. pp. 1–8 (2023)
27. Habib, H., Li, M., Young, E., Cranor, L.: “okay, whatever”: An evaluation of cookie
consent interfaces. In: Proceedings of the 2022 CHI conference on human factors
in computing systems. pp. 1–27 (2022)
28. Hantke, F., Calzavara, S., Wilhelm, M., Rabitti, A., Stock, B.: You call this ar-
chaeology? evaluating web archives for reproducible web security measurements.
In: Proceedings of the 2023 ACM SIGSAC Conference on Computer and Commu-
nications Security. pp. 3168–3182 (2023)
29. Hantke, F., Snyder, P., Haddadi, H., Stock, B.: Web execution bundles:
Reproducible, accurate, and archivable web measurements. arXiv preprint
arXiv:2501.15911 (2025)
30. Hausner, P., Gertz, M.: Dark patterns in the interaction with cookie banners.
position paper at the workshop" what can chi do about dark patterns?" at the chi
conference on human factors in computing systems (chi’21)., 5 pages (2021)
31. Hils, M., Woods, D.W., Böhme, R.: Measuring the emergence of consent manage-
ment on the web. In: Proceedings of the ACM Internet Measurement Conference.
pp. 317–332 (2020)
32. HTTPArchive: Httparchive. https://httparchive.org/ (2025), last accessed on 05-
01-2026
33. Internet Archive: Wayback machine. https://web.archive.org/ (2026), last accessed
on 9-01-2026
34. Jha, N., Trevisan, M., Mellia, M., Fernandez, D., Irarrazaval, R.: Privacy policies
and consent management platforms: Growth and users’ interactions over time.
ACM Transactions on the Web19(3), 1–25 (2025)

24 Y. Dimova et al.
35. Kampanos, G., Shahandashti, S.F.: Accept all: The landscape of cookie banners
in greece and the uk. In: IFIP International Conference on ICT Systems Security
and Privacy Protection. pp. 213–227. Springer (2021)
36. Khandelwal, R., Nayak, A., Harkous, H., Fawaz, K.: Cookieenforcer: Automated
cookie notice analysis and enforcement. arXiv preprint arXiv:2204.04221 (2022)
37. Kirkman, D., Vaniea, K., Woods, D.W.: Darkdialogs: Automated detection of 10
dark patterns on cookie dialogs. In: 2023 IEEE 8th European Symposium on Se-
curity and Privacy (EuroS&P). pp. 847–867. IEEE (2023)
38. Kretschmer, M., Pennekamp, J., Wehrle, K.: Cookie banners and privacy policies:
Measuring the impact of the gdpr on the web. ACM Transactions on the Web
(TWEB)15(4), 1–42 (2021)
39. Krisam, C., Dietmann, H., Volkamer, M., Kulyk, O.: Dark patterns in the wild:
Review of cookie disclaimer designs on top 500 german websites. In: Proceedings
of the 2021 European Symposium on Usable Security. pp. 1–8 (2021)
40. Kusk, K., Nouwens, M.: How website owners use consent management platforms:
An interview study. In: Proceedings of the Extended Abstracts of the CHI Confer-
ence on Human Factors in Computing Systems. pp. 1–7 (2025)
41. Leenes, R., Kosta, E.: Taming the cookie monster with dutch law–a tale of regu-
latory failure. computer law & security review 31 (03 2015) (2015)
42. Lerner, A., Simpson, A.K., Kohno, T., Roesner, F.: Internet jones and the raiders
of the lost trackers: An archaeological study of web tracking from 1996 to 2016.
In: 25th USENIX Security Symposium (USENIX Security 16) (2016)
43. Libert, T., Graves, L., Nielsen, R.: Changes in third-party content on european
news websites after gdpr. Tech. rep., University of Oxford (2018)
44. Linden, T., Khandelwal, R., Harkous, H., Fawaz, K.: The privacy policy landscape
after the gdpr. arXiv preprint arXiv:1809.08396 (2018)
45. Légifrance: Délibération de la formation restreinte n°san-2021-
023 du 31 décembre 2021 concernant les sociétés x et y.
https://www.legifrance.gouv.fr/cnil/id/CNILTEXT000044840062 (2021), last
accessed on 09-01-2026
46. Légifrance: Délibération de la formation restreinte n°san-
2021-024 du 31décembre 2021 concernant la société x.
https://www.legifrance.gouv.fr/cnil/id/CNILTEXT000044840532?isSuggest=true
(2021), last accessed on 09-01-2026
47. Matte, C., Bielova, N., Santos, C.: Do cookie banners respect my choice?: Mea-
suring legal compliance of banners from iab europe’s transparency and consent
framework. In: 2020 IEEE Symposium on Security and Privacy (SP). pp. 791–809.
IEEE (2020)
48. Mehrnezhad, M.: A cross-platform evaluation of privacy notices and tracking prac-
tices. In: 2020 IEEE European Symposium on Security and Privacy Workshops
(EuroS&PW). pp. 97–106. IEEE (2020)
49. metamorfosilab: Cookies-consent github repository.
https://github.com/MetamorfosiLab/cookies-consent?tab=readme-ov-file, last
accessed on 30-08-2025
50. Morel, V., Santos, C., Lintao, Y., Human, S.: Your consent is worth 75 euros a
year-measurement and lawfulness of cookie paywalls. In: Proceedings of the 21st
Workshop on Privacy in the Electronic Society. pp. 213–218 (2022)
51. Nikiforakis, N., Invernizzi, L., Kapravelos, A., Van Acker, S., Joosen, W., Kruegel,
C., Piessens, F., Vigna, G.: You are what you include: large-scale evaluation of
remote javascript inclusions. In: Proceedings of the 2012 ACM conference on Com-
puter and communications security. pp. 736–747 (2012)

A history of GDPR cookie banner compliance 25
52. Nouwens, M., Kristensen, J.B., Maalt, K., Bagge, R.: A cross-country analysis of
gdpr cookie banners and flexible methods for scraping them. In: Proceedings of the
2025 CHI Conference on Human Factors in Computing Systems. pp. 1–28 (2025)
53. Nouwens, M., Liccardi, I., Veale, M., Karger, D., Kagal, L.: Dark patterns after the
gdpr: Scraping consent pop-ups and demonstrating their influence. In: Proceedings
ofthe2020CHIconferenceonhumanfactorsincomputingsystems.pp.1–13(2020)
54. noyb: noyb aims to end “cookie banner terror” and issues more than 500 gdpr com-
plaints. https://noyb.eu/en/noyb-aims-end-cookie-banner-terror-and-issues-more-
500-gdpr-complaints (2021), last accessed on 31-08-2025
55. noyb: noyb files 422 formal gdpr complaints on nerve-wrecking “cookie ban-
ners”. https://noyb.eu/en/noyb-files-422-formal-gdpr-complaints-nerve-wrecking-
cookie-banners (2021), last accessed on 30-08-2025
56. noyb: 226 complaints lodged against deceptive cookie banners.
https://noyb.eu/en/226-complaints-lodged-against-deceptive-cookie-banners
(2022), last accessed on 30-08-2025
57. noyb: Consent banner report. https://noyb.eu/sites/default/files/2024-
07/noyb_Cookie_Report_2024.pdf (2023), last accessed on 30-08-2025
58. noyb: Gdpr decision database. https://gdprhub.eu/ (2025), last accessed on 09-01-
2026
59. Offical Journal of the European Union: Directive 2002/58/ec of the euro-
pean parliament and of the council of 12 july 2002 concerning the processing
of personal data and the protection of privacy in the electronic communica-
tions sector (directive on privacy and electronic communications). https://eur-
lex.europa.eu/eli/dir/2002/58/oj/eng (2002), last accessed on 9-01-2026
60. Offical Journal of the European Union: Regulation (eu) 2016/679 of the
european parliament and of the council of 27 april 2016 on the pro-
tection of natural persons with regard to the processing of personal
data and on the free movement of such data, and repealing directive
95/46/ec (general data protection regulation). https://eur-lex.europa.eu/legal-
content/EN/TXT/PDF/?uri=CELEX:32016R0679 (2016), last accessed on 9-01-
2026
61. OneTrust: Onetrust solutions. https://www.onetrust.com/, last accessed on 30-08-
2025
62. Rasaii, A., Singh, S., Gosain, D., Gasser, O.: Exploring the cookieverse: A multi-
perspective analysis of web cookies. In: International Conference on Passive and
Active Network Measurement. pp. 623–651. Springer (2023)
63. Roth, S., Barron, T., Calzavara, S., Nikiforakis, N., Stock, B.: Complex security
policy?alongitudinalanalysisofdeployedcontentsecuritypolicies.In:Proceedings
of the 27th Network and Distributed System Security Symposium (NDSS) (2020)
64. Sanchez-Rola, I., Dell’Amico, M., Kotzias, P., Balzarotti, D., Bilge, L., Vervier,
P.A., Santos, I.: Can i opt out yet? gdpr and the global illusion of cookie control.
In:Proceedingsofthe2019ACMAsiaconferenceoncomputerandcommunications
security. pp. 340–351 (2019)
65. Santos, C., Nouwens, M., Toth, M., Bielova, N., Roca, V.: Consent management
platforms under the gdpr: processors and/or controllers? In: Annual Privacy Fo-
rum. pp. 47–69. Springer (2021)
66. Sheil, A., Malone, D.: Fianán, cuacha: Irish cookie banners. In: 2022 33rd Irish
Signals and Systems Conference (ISSC). pp. 1–8. IEEE (2022)
67. Soe, T.H., Nordberg, O.E., Guribye, F., Slavkovik, M.: Circumvention by design-
dark patterns in cookie consent for online news outlets. In: Proceedings of the 11th

26 Y. Dimova et al.
nordic conference on human-computer interaction: Shaping experiences, shaping
society. pp. 1–12 (2020)
68. Stock, B., Johns, M., Steffens, M., Backes, M.: How the web tangled itself: Un-
covering the history of client-side web (in) security. In: 26th USENIX Security
Symposium (USENIX Security 17). pp. 971–987 (2017)
69. Toth, M., Bielova, N., Roca, V.: On dark patterns and manipulation of website
publishers by cmps. Proceedings on Privacy Enhancing Technologies2022(3), 478–
497 (2022)
70. Trevisan, M., Traverso, S., Bassi, E., Mellia, M., et al.: 4 years of eu cookie law: Re-
sultsand lessonslearned.ProceedingsonPrivacyEnhancingTechnologies2019(2),
126–145 (2019)
71. Van Eijk, R., Asghari, H., Winter, P., Narayanan, A.: The impact of user loca-
tion on cookie notices (inside and outside of the european union). arXiv preprint
arXiv:2110.09832 (2021)
72. Warberg, L., Lefrere, V., Cheyre, C., Acquisti, A.: Trends in privacy dialog design
after the gdpr: The impact of industry and government actions. In: Proceedings of
the 22nd Workshop on Privacy in the Electronic Society. pp. 107–121 (2023)
73. Wesselkamp, V., Fouad, I., Santos, C., Boussad, Y., Bielova, N., Legout, A.: In-
depth technical and legal analysis of tracking on health related websites with ernie
extension. In: Proceedings of the 20th Workshop on Workshop on Privacy in the
Electronic Society. pp. 151–166 (2021)
74. Zhang, M., Meng, W., Zhou, Y., Ren, K.: Cschecker: Revisiting gdpr and ccpa
compliance of cookie banners on the web. In: Proceedings of the IEEE/ACM 46th
International Conference on Software Engineering. pp. 1–12 (2024)
