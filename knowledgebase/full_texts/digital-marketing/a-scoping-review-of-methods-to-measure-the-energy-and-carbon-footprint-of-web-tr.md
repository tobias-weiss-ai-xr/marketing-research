---
title: A Scoping Review of Methods to Measure the Energy and Carbon Footprint of Web Tracking and Advertising
url: https://arxiv.org/abs/2608.19495
category: digital-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Nils Bonfils
- Christoph Becker
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.19495
pages: 5
chars: 32569
fetched_at: '2026-11-08T13:00:30+00:00'
kb_version: 1
---

# A Scoping Review of Methods to Measure the Energy and Carbon Footprint of Web Tracking and Advertising

A Scoping Review of Methods to Measure the Energy and Carbon
Footprint of Web Tracking and Advertising
Nils Bonfils
nils.bonfils@mail.utoronto.ca
University of Toronto
Toronto, Ontario, Canada
Christoph Becker
christoph.becker@utoronto.ca
University of Toronto
Toronto, Ontario, Canada
Abstract
The environmental impact of web tracking and advertising is in-
creasingly receiving attention as the ICT sector’s carbon footprint
keeps rising. Yet the scholarship addressing this question remains
scattered across disciplines and inconsistent in its terminology. This
paper presents a scoping review of the literature on methods for
measuring the energy and carbon footprint of web tracking and
advertising. From an initial pool of 46 articles identified through
a structured title-based search on Google Scholar, we arrived at a
final corpus of 15 papers, from which we identified five distinct
methodological approaches: ad blocking, controlled environment,
replaying ads, traffic flow analysis, and literature-derived estima-
tion. This review provides a structured overview of the current
methodological landscape and a foundation for more comprehen-
sive environmental accounting of the ad tech ecosystem.
1 Introduction
Digital advertising is the growing primary source of revenue for
the majority of services offered on the web, including search en-
gines, social media platforms, news outlets, and video stream-
ing platforms [24]. Those services represent the core products of
multibillion-dollar corporations that derive the majority of their
revenue through advertising [1, 15]. To increase the relevance of
digital advertisements, web advertising is often coupled with user
tracking (a.k.a. analytics or behavioral/targeted advertising) form-
ing part of a complex "ad tech" ecosystem [14].
However, tracking and advertising on the web extends far beyond
traditional advertising. They represent the user-facing layer of
a complex ecosystem of software and data transfer engineered
to generate profit from users’ interactions with ostensibly free
web services. Sometimes called surveillance capitalism [30], digital
capitalism [26], or platform capitalism [ 28], this new economic
order is built on the monetization of enormous quantities of user
data. The infrastructures required to capture, store, and process
data at scale consumes substantial energy and carries significant
material consequences. Accurately calculating the environmental
cost of surveillance capitalism practices is therefore a necessary
step toward a fuller picture of its ecological toll, of which web
tracking and advertising is the most visible constituent part.
While generic software tools to measure the carbon footprint
of software and services exist, accurately measuring the energy
and carbon cost of web tracking and advertising poses a distinct
methodological challenge: isolating the computational resources
specifically devoted to displaying advertisements and capturing
user data from the resources required by the regular operation of
LOCO 2026, Lancaster, UK
2026.
the software. Existing research does address the environmental
impact of web tracking and advertising, but it draws on a diver-
sity of approaches without any coherent understanding of what
the state-of-the-art methods are or how they relate to one another.
Addressing that gap is what this paper seeks to accomplish:what
methods have been established to quantify the computational resource
consumption of web tracking and advertising?To that end, we con-
duct a scoping review of the literature on methods to measure the
energy and carbon footprint of web tracking and advertising.
2 Motivation
The impetus for this work stems from the authors’ earlier efforts
to map and assess the environmental impact of surveillance cap-
italism [2, 3]. In that prior work, the authors sought methods to
calculate the environmental impact of processes closely related to
web advertising and analytics, but found no clear answer in the
existing literature. The literature quantifying the carbon and en-
ergy footprint of ad tech does exist but is scattered across different
fields, such as computer science, impact assessment, and industrial
ecology. This disciplinary fragmentation has produced considerable
terminological inconsistency: terms like web analytics, online track-
ing, and user tracking typically denote the same processes, while
words like costs, impacts, and footprint are used interchangeably
across studies. Combined with the relative recency of this phenom-
enon, this terminological disjunction makes it difficult to follow the
latest methodological developments in the field.
Nevertheless, a substantial body of research has recently emerged
addressing these questions. This body of literature is comprised
of studies that draw on a variety of methods involving bespoke
setups for data collection, diverse metrics, and differing statistical
methods. Given the range of studies and the absence of a unified
field or community regrouping the knowledge surrounding it, a
scoping review is an appropriate instrument for providing an initial
overview of the methods used to measure the energy and carbon
footprint of web tracking and advertising.
3 Methods
Our approach started with a base set of ten papers, each highly
relevant to measuring the energy and carbon impact of advertising,
tracking, and surveillance on the web (Appendix A). The ten base
papers were identified through a non-systematic combination of on-
line and database searches, including DuckDuckGo, Google Scholar,
ACM Digital Library, IEEE Xplore, alongside both backward and
forward snowballing. From this set, we extracted terms from the
paper titles to capture both the topic of focus and the type of impact
measured (Appendix B.1), which were then used to craft search
queries.
arXiv:2608.19495v1  [cs.CY]  19 Aug 2026

LOCO 2026, September 10–11, 2026, Lancaster, UK Nils Bonfils and Christoph Becker
For this review, we selected Google Scholar as our search data-
base. We restricted our searches to paper titles by using the "allinti-
tle:" operator, and excluded a small number of terms to filter out
unrelated papers. It is worth noting that Google Scholar’s query
syntax is both limited and not well-documented. Throughout our
searches, we discovered a 340 character ceiling beyond which query
terms are silently dropped while still appearing in the search box.
In order to circumvent that limitation, we divided our search into
multiple queries that are detailed in Appendix B.2. This process
ended up yielding a pool of 46 articles.
We then filtered this pool based on the title, abstract, and a brief
review of the methods section, retaining only papers that attempted
to measure the energy or carbon footprint of web tracking, adver-
tising, or associated network traffic. This filtered set contained 18
articles, from which we excluded three: 1) a thesis [9], 2) an online
news article [17], and 3) a conference paper that we were unable to
access [29]. This left a final corpus of 15 papers (Table 1).
4 Findings
During our analysis of the articles, we found it useful to consider
several of the dimensions outlined by Pärssinen et al. [18]. The first
dimension concerns how contributions to the carbon impact of the
ICT sector are allocated, based on either the use time or by the
volume of data traffic. The second dimension is the fundamental
internet subsystem addressed by the paper. It can be one of: 1) the
end-user devices:client-side, 2) the infrastructure connecting users
to applications:connectivity, 3) the applications themselves:server-
side, or 4) the traffic flowing across other sub-systems:secondary
traffic. The third dimension concerns the approach used to estimate
the power usage or carbon footprint of a system, typically one of:
1) top-down, 2) bottom-up, 3) model based, or 4) unified method.
Finally, we identified five distinct methods across all the articles in
our final corpus listed in Table 1.
4.1 Method 1: Ad Blocking
The most common approach to measuring the carbon and energy
footprint of advertising and analytics in our selected scholarship
involves browsing websites that contains ads, with and without
some form of ad blocking. Ad blocking most commonly takes the
form of a web browser extension, such as uBlock Origin, Adblock
Plus, or AdGuard. However, ad blocking can also be implemented
as a built-in feature of web browsers (i.e. Brave, Opera, Vivaldi)[12],
filtered through an HTTP proxy [27], or even blocked at the DNS
request level[20].
For clarity, we deconstruct this approach into three essential
steps:
(1) Define a navigation or web browsing strategy
(2) Select ad blocking configurations
(3) Instrument the measurement setup
Step 1: Navigation Strategy.The first step of the ad blocking
approach involves defining which websites will be browsed and
how. Most studies select a sample from online lists of popular
websites (e.g. Digg, Tranco, or 4imn.com), some (such as Khan et
al.) simply use an arbitrary list of websites [10–13]. Methodological
transparency is achieved by clearly documenting the initial source
list, the inclusion and exclusion criteria, and the motivation behind
those choices.
Once the list of websites to be browsed is finalized, a browsing
approach must be devised. Some studies instrument a web browser
to automate browsing using tools, such as Puppeteer [20] or Auto-
Browse, a bespoke solution built specifically by Simons and Pras
for their study [27]. The browsing behavior can range from simply
loading a page, to automating mouse movement [21], to emulating
realistic user behavior [20].
Step 2: Ad Blocking Configuration.The ad blocking configuration
plays an important role, as most studies demonstrated a significant
variation in the power measured depending on the combination
of web browser, type of ad blocking (browser extension, built-in,
proxy, or DNS), OS, and hardware. Configurations are therefore
always disclosed, with Khan et al. going as far as to organize their
works around specific categories of configurations [10–13].
Step 3: Measurement Setup.The measurement setup can take
several different forms. Simons and Pras opted for direct measure-
ments with a voltmeter to record hardware power usage [27]. Pearce
recorded differences in page load time to infer how much time was
"lost" to advertisement delivery and tracking [19]. Most other stud-
ies use a software-based approach that draws on CPU or battery
information to infer power consumption – common tools for this
include Powerstat, HWiNFO, and Batterystat.
4.2 Method 2: Controlled Environment
Another approach, similar in essence to ad blocking but different in
execution, is what we term the "controlled environment" method.
Rather than blocking ads after the fact, this method involves cre-
ating or recreating websites in lab settings in order to control the
delivery side of ads and trackers. The two studies that employed
this method implemented it in notably different ways.
Petalotis et al. followed a similar approach to the ad blocking
method, selecting a list of nine websites containing both ads and
analytics and automating web browsing on Android using Mon-
keyRunner. However, rather than configuring ad blocking, they
downloaded the selected websites and produced three versions of
each: 1) the original, unchanged; 2) with ads removed; and 3) with
analytics and trackers removed. These versions were then served
locally in a controlled environment, where measurements were
carried out [22].
Puhtila et al. implemented this approach differently, building
a website from scratch and instrumenting a varying number of
analytical tools (0, 1, 5 and 10) on that website. Their navigation
strategy used an automated setup with Selenium to perform actions
on the website, including page navigation, scrolling on a page, and
form submission, while power consumption was measured directly
via voltmeter [23].
4.3 Method 3: Replaying Ads
This approach is used by a single paper [8]. González-Cabañas et
al. first created a dataset by automatically crawling a thousand
popular websites and saving the ads encountered, gathering around
25,000 ads. In parallel, they manually collected around 500 ads from
humans browsing the web. They then built an automated setup to

A Scoping Review of Methods to Measure the Energy and Carbon Footprint of Web Tracking and Advertising LOCO 2026, September 10–11, 2026, Lancaster, UK
Table 1: The final set of 15 papers. Each work uses either a time-based or network traffic-based metric. Each work focus on
different part of the ecosystem of ad and tracking. Each work makes use of one of the five methods discussed in the findings.
Paper Metric Focus Method
(Simons and Pras, 2010)[27] Time-based Client-side Ad Blocking
(Pärssinen et al., 2018)[18] Network Traffic Holistic Literature-Derived Estimation
(Pearce, 2020)[19] Time-based Client-side Ad Blocking
(Cuccietti et al., 2022)[4] Network Traffic Holistic Traffic Flow Analysis
(González-Cabañas et al., 2023)[8] Time-based Client-side Replaying Ads
(Pesari et al., 2023)[21] Time-based Client-side Ad Blocking
(Khan et al., 2024a)[13] Time-based Client-side Ad Blocking
(Khan et al., 2024b)[11] Time-based Client-side Ad Blocking
(Khan et al., 2024c)[12] Time-based Client-side Ad Blocking
(Petalotis et al., 2024)[22] Time-based Client-side Controlled Environment
(Puhtila et al., 2024)[23] Time-based Client-side Controlled Environment
(Khan et al., 2025)[10] Time-based Client-side Ad Blocking
(Duprat, 2026)[5] Network Traffic Client and Server Literature-Derived Estimation
(Pélissier et al., 2026)[20] Time-based Client-side Ad Blocking
(Bonfils et al., 2026)[3] Network Traffic Connectivity Traffic Flow Analysis
render and display each collected ad individually. The measurement
process ran in two steps: first, opening and closing a blank page of
the browser to establish a "baseline" measurement; second, opening
the ad in the web browser and recording its energy usage. Subtract-
ing the baseline from the second measurement yielded the energy
cost of rendering a single ad. To generalize those findings, they
trained a machine learning model on the pairing of ads with their
normalized energy usage, demonstrating how statistical models
can extend the reach of such a method.
4.4 Method 4: Traffic Flow Analysis
This method consists in analyzing the network traffic generated
by advertisement and tracking processes. Cuccietti et al. [4] used
OpenWPM, a tool that extends and optimizes Selenium for crawling
large number of websites [6], to crawl the top one million websites
according to the Tranco List and capture the network traffic for
each page load. They used cookies as the differentiator between
tracking and non-tracking traffic, enabling them to leverage the
network traffic data collected to sum the amount of bytes used by
cookies, and estimated the total data transferred for cookie-based
tracking. As appealing as deriving energy and carbon footprint
estimates from this figure by applying the appropriate energy and
carbon intensity coefficients may be, it is important to note that
such an approach is flawed and will likely results in misleading fig-
ures. Current work is underway attempting to attribute the energy
consumption associated with data traffic [25].
The authors’ most recent work is a pilot study quantifying the
environmental footprint of user tracking and other processes related
to surveillance capitalism [3]. The approach compares the network
traffic usage on two distinct platforms: a corporate platform whose
business model requires the use of ads and analytics (i.e. X/Twitter)
and a non-commercial free and open-source counterpart free of
those incentives (i.e. Mastodon). The network traffic was measured
by instrumenting a web browser to emulate realistic user behavior
(i.e. scrolling on the feed and making posts).
4.5 Method 5: Literature-Derived Estimation
The final method is the only approach that requires no primary
data collection and no dedicated measurement setup. Instead, it
derives energy and carbon footprint estimates by drawing on coef-
ficients and figures reported in existing literature, applying them
relevant metrics to produce macro-level consumption estimates.
Duprat, offers a lightweight application of this method: estimating
the proportion of computational resources used by advertisements
and applying carbon intensity coefficients to calculate energy and
carbon footprint estimates [5]. This approach is accessible but its
validity rests on the relevance of the coefficients it borrows.
Pärssinen et al. are considerably more thorough [18]. Drawing
on an extensive body of literature, they contribute a framework
for assessing the environmental impact of any internet service.
The least transparent element of their analysis is their estimate of
the share of network traffic dedicated to online advertising, which
could not be grounded in prior literature as it was non-existent at
the time. Nevertheless, their approach demonstrated clearly how
to handle uncertainty in figures derived from the literature.
4.6 Presentation of Results
It is worth noting that none of the works directly measure CO2
emissions. Instead, they translate their chosen metric into energy
(typically in kWh), if power was not measured directly, and then
convert that energy figure to a CO2-equivalent quantity by multiply-
ing it with a recent local or global grid carbon intensity coefficient.
Some works contribute a figure representing the relative power
consumption of web tracking or advertising without attempting to
extrapolate their results to scale. For instance, Khan et al. report that
using a web browser with a built-in ad blocker can reduce power
consumption by up to 44% compared to traditional web browser
setups [12]. Conversely, other works, such as Pearce, go as far as to
estimate the financial savings and the number of lives that could
be saved from coal-based pollution if all the internet users in the
United States used an ad blocker [19].

LOCO 2026, September 10–11, 2026, Lancaster, UK Nils Bonfils and Christoph Becker
5 Discussion
This scoping review identified five distinct methodological ap-
proaches across the 15 studies of our final corpus. Of these, the ad
blocking method is adopted by the greatest number of different
authors (despite the bias towards Khan et al.), offering a practical
and reproducible means of isolating the energy cost of ads and
trackers on the client side. The controlled environment and indi-
vidual ad replay methods offer greater experimental control at the
cost of validity, while traffic flow analysis and literature review
represent approaches better suited to macro-level estimation. No
single method has emerged as a standard, and the field has yet to
converge on shared metrics, terminology, and evaluations.
Our corpus suggests that the interest for this area of inquiry is
rather young and growing with 12 out of the 15 studies (80% of
the corpus) published in the last five years. This recent increase
in attention is understandable, particularly in light of the global
environmental crisis and the growing environmental impact attrib-
utable to the ICT sector [ 7]. The urgency of this topic is further
compounded by the critiques of surveillance capitalism, which
demonstrate how the economical and political incentives under-
pinning ad tech are harmful for democratic societies [30]. The link
between the concrete environmental impacts of ad tech and the
critiques of surveillance is a novel angle that we, the authors, are
seeking to explore.
Despite its small size, the corpus revealed a breadth of method-
ological approaches that also reflects fragmentation in the field. The
studies engage with shared questions without meaningfully build-
ing on or responding to each other’s findings. For instance, when
González-Cabañas et al. discovered that the transfer size (i.e. the
amount of data transferred necessary to receive the ad) is irrelevant
to estimate the energy necessary to render individual ads [8], they
did not situate this finding in relation to the work of Pärssinen et al.
whose analysis relies on allocating energy consumption based on
network traffic [18]. The implication is significant: if transfer size is
not a reliable proxy for the energy consumed by client-side ad ren-
dering, then Pärssinen et al’s estimate of the energy consumption
of online advertising on user devices may be invalid.
Several directions emerge as priorities for future work. Most im-
mediately, the near-complete absence of server-side and secondary
traffic measurements are highlighting the need to develop methods
to instrument the measurement of ad delivery and user data pro-
cessing within data center infrastructure. However, the systemic
opacity of corporate infrastructure undermines the feasibly of such
undertakings. Thus, the controlled environment approach (Section
4.2) offers an imperfect but accessible approach that warrants fur-
ther development as a methodology capable of addressing that gap,
given its potential to model the full stack. There is also a need for
shared terminology and methods across the disciplines for coher-
ent dialogue between studies. This could be achieved through a
systematic literature review that extends the queries used in this
review, and includes terms such as "telemetry" as a synonym for
analytics and "efficiency" as a synonym for consumption, as well
as emphasizing the need to capture literature on the server-side.
Finally, longitudinal studies tracking the environmental cost of ad
tech over time are lacking and are essential to track the evolution
and trends of the environmental impact of this industry.
It is important to underscore that while this paper is a scoping
review, it is not systematic [16]. We deliberately limited our search
to terms in the title of papers and did not employ complementary
methods, such as backward or forward snowballing. Therefore, the
five methods presented here should not be considered exhaustive
and are instead representative. We also note that this work only
engages with literature measuring the footprint of web tracking
and advertising. We recognize that a wider scope of would surface
more approaches capable of quantifying the energy and carbon
footprint of software and web services (e.g. CO2.js1).
6 Conclusion
This scoping review maps existing methods to measure the energy
and carbon footprint of web tracking and advertising, a question
that sits at the intersection of the environmental crisis and the
growing critique of surveillance capitalism. Through a structured
literature search and filtering process, we identified 15 relevant
studies and surfaced five distinct methodological approaches: ad
blocking, controlled environment, replaying ads, traffic flow analy-
sis, and literature-derived estimation. The field itself seems to be
gaining momentum with 80% of the papers in our corpus published
within the last five years. This growing interest combined with a
variety of existing methods suggests the importance and potential
of quantifying the environmental costs of the ad tech ecosystem,
while the methodological groundwork for doing so is already taking
shape.
References
[1] Alphabet Inc. 2026.Alphabet Investor Relations - Investors. https://abc.xyz/
investor/
[2] Nils Bonfils. 2025. An Empirical Inquiry into Surveillance Capitalism: Web
Tracking. In11th Workshop on Computing within Limits. doi:10.48550/arXiv.2508.
07454
[3] Nils Bonfils and Christoph Becker. 2026. The Environmental Costs of Surveillance
Capitalism: A Case Study of Social Media Platforms. InAccepted at the 12th
International Conference on ICT for Sustainability. Bern, Switzerland. doi:10.
48550/arXiv.2605.26314
[4] Fernando Cucchietti, Joana Moll, Marta Esteban, Patricio Reyes, and Carlos Garcia
Calatrava. 2022. Carbolytics: An Analysis of the Carbon Costs of Online Tracking.
https://carbolytics.org/report.html.
[5] Charles Duprat. 2026. The Thermodynamic Efficiency Inversion: A Comparative
Energy Lifecycle Assessment of Generative AI Inference versus Ad-Supported
Web Search Sessions. social science research network:6287918 doi:10.2139/ssrn.
6287918
[6] Steven Englehardt and Arvind Narayanan. 2016. Online Tracking: A 1-Million-
Site Measurement and Analysis. InProceedings of the 2016 ACM SIGSAC Confer-
ence on Computer and Communications Security. ACM, Vienna Austria, 1388–1401.
doi:10.1145/2976749.2978313
[7] Charlotte Freitag, Mike Berners-Lee, Kelly Widdicks, Bran Knowles, Gordon S.
Blair, and Adrian Friday. 2021. The Real Climate and Transformative Im-
pact of ICT: A Critique of Estimates, Trends, and Regulations. 2, 9 (2021).
pubmed:34553177 doi:10.1016/j.patter.2021.100340
[8] José González-Cabañas, Patricia Callejo, Rubén Cuevas, Steffen Svartberg, Tommy
Torjesen, Ángel Cuevas, Antonio Pastor, and Mikko Kotila. 2023. CarbonTag:
A Browser-Based Method for Approximating Energy Consumption of Online
Ads.IEEE Transactions on Sustainable Computing8, 4 (Oct. 2023), 739–750.
doi:10.1109/TSUSC.2023.3286916
[9] Khan Awais Khan. 2025.Impact of Ad Blockers on Computer Power Consumption:
A Comparative Analysis of Browser Ad on and Built-in Browsers Feature. Master’s
thesis. Memorial University of Newfoundland.
[10] Khan Awais Khan, Mohammad Tariq Iqbal, and Mohsin Iqbal. 2025. Computer
Power Consumption While Using Ad-Blocker on a System with AI Accelerators.
European Journal of Information Technologies and Computer Science5, 1 (Jan.
2025), 11–20. doi:10.24018/compute.2025.5.1.144
1https://www.thegreenwebfoundation.org/co2-js/

A Scoping Review of Methods to Measure the Energy and Carbon Footprint of Web Tracking and Advertising LOCO 2026, September 10–11, 2026, Lancaster, UK
[11] Khan Awais Khan, Mohammad Tariq Iqbal, and Mohsin Jamil. 2024. Impact of Ad
Blockers on Computer Power Consumption While Web Browsing: A Comparative
Analysis.European Journal of Electrical Engineering and Computer Science8, 5
(Oct. 2024), 18–24. doi:10.24018/ejece.2024.8.5.650
[12] Khan Awais Khan, Mohammad Tariq Iqbal, and Mohsin Jamil. 2024. The Impact
of Built-in Ad-Blockers in Web Browsers on Computer Power Consumption.
European Journal of Information Technologies and Computer Science4, 5 (Nov.
2024), 1–10. doi:10.24018/compute.2024.4.5.137
[13] Khan Awais Khan, Mohammad Tariq Iqbal, and Mohsin Jamil. 2024. Power
Consumption While Using Ad-Blockers on ARM-Based CPU. InThe 33rd Annual
Newfoundland Electrical and Computer Engineering Conference.
[14] Stine Lomborg, Rasmus Helles, and Signe Sophus Lai. 2023. Digital Tracking and
Infrastructural Power. InHandbook of Critical Studies of Artificial Intelligence.
Edward Elgar Publishing, Chapter Handbook of Critical Studies of Artificial
Intelligence, 354–366.
[15] Meta Platforms, Inc. 2026.Meta - Financials. https://investor.atmeta.com/
financials/
[16] Zachary Munn, Micah D. J. Peters, Cindy Stern, Catalin Tufanaru, Alexa
McArthur, and Edoardo Aromataris. 2018. Systematic Review or Scoping Re-
view? Guidance for Authors When Choosing between a Systematic or Scoping
Review Approach.BMC Medical Research Methodology18, 1 (Nov. 2018), 143.
doi:10.1186/s12874-018-0611-x
[17] Omar Oakes. 2021. Carbon Footprint of Digital Ads Laid Bare by Good-Loop
Tool.
[18] M. Pärssinen, M. Kotila, R. Cuevas, A. Phansalkar, and J. Manner. 2018. Envi-
ronmental Impact Assessment of Online Advertising.Environmental Impact
Assessment Review73 (Nov. 2018), 177–200. doi:10.1016/j.eiar.2018.08.004
[19] Joshua M. Pearce. 2020. Energy Conservation with Open Source Ad Blockers.
Technologies8, 2 (June 2020), 18. doi:10.3390/technologies8020018
[20] Samuel Pélissier, Naif Mehanna, Sterenn Roux, Quentin Perez, Walter
Rudametkin, Johann Bourcier, and Pierre Laperdrix. 2026. Users Pay Twice:
The Hidden Energy Cost of Web Advertising. InProceedings of the ACM Web
Conference 2026 (WWW ’26). Association for Computing Machinery, New York,
NY, USA, 1629–1639. doi:10.1145/3774904.3792414
[21] Fabio Pesari, Giovanni Lagioia, and Annarita Paiano. 2023. Client-Side Energy
and GHGs Assessment of Advertising and Tracking in the News Websites.Journal
of Industrial Ecology27, 2 (2023), 548–561. doi:10.1111/jiec.13376
[22] Christos Petalotis, Luka Krumpak, Maximilian Stefan Floroiu, Laréb Fatima Ah-
mad, Shashank Athreya, and Ivano Malavolta. 2024. An Empirical Study on
the Performance and Energy Costs of Ads and Analytics in Mobile Web Apps.
Information and Software Technology166 (Feb. 2024), 107370. doi:10.1016/j.infsof.
2023.107370
[23] Panu Puhtila, Lauri Kivimäki, Timi Heino, Jari-Matti Mäkelä, Sampsa Rauti, and
Tuomas Mäkilä. 2024. The Effect of Analytics Tools on Energy Consumption of
Websites. In2024 10th International Conference on ICT for Sustainability (ICT4S).
335–345. doi:10.1109/ICT4S64576.2024.00041
[24] PwC. 2026.IAB Internet Advertising Revenue Report - Full-year 2025 Results.
Technical Report. PwC.
[25] Daniel Schien, Paul Shabajee, Louise Krug, Greg McSorley, and Chris Preist. 2025.
Causal Allocation of Fixed Impacts in Product Systems: Assessing the Effect of
Data Demand on Network Energy Consumption.Journal of Industrial Ecology
29, 5 (2025), 1618–1631. doi:10.1111/jiec.70057
[26] Daniel Schiller. 2000.Digital Capitalism: Networking the Global Market System.
MIT Press, Cambridge, MA, USA.
[27] R. J. G. Simons and Aiko Pras. 2010. The Hidden Energy Cost of Web Advertising.
(June 2010).
[28] Nick Srnicek. 2017.Platform Capitalism. John Wiley & Sons.
[29] A. Visser. 2016. The Effect of Ad Blockers on the Energy Consumption of Mobile
Web Browsing.
[30] Shoshana Zuboff. 2019.The Age of Surveillance Capitalism: The Fight for a Human
Future at the New Frontier of Power. PublicAffairs.
A Initial Paper Titles
The list of ten paper titles used to extract query terms from.
• An empirical study on the performance and energy costs of
ads and analytics in mobile web apps
• Carbolytics: An Analysis of the Carbon Costs of Online
Tracking
• Client-side energy and GHGs assessment of advertising and
tracking in the news websites
•Energy Conservation with Open Source Ad Blockers
•Environmental impact assessment of online advertising
• Impact of Ad Blockers on Computer Power Consumption
while Web Browsing: A Comparative Analysis
• The Effect of Analytics Tools on Energy Consumption of
Websites
• The Environmental Costs of Surveillance Capitalism: A Case
Study of Social Media Platforms
•The Hidden Energy Cost of Web Advertising
• Users Pay Twice: The Hidden Energy Cost of Web Advertis-
ing
B Search Queries
Google Scholar search syntax: ’|’ means OR, a space means AND,
parentheses means grouping, and double quotes are use for exact
match.
B.1 Query Terms
Type of Impact.
• (ecological | environmental) (cost | costs | impact | impacts |
footprint | sustainability)
• (energy | carbon) (cost | costs | consumption | conservation |
impact | impacts | footprint | assessment)
•power (consumption | assessment)
Topic of Focus.
• (online | web | website | websites | digital) (ad | ads | analytics
| advertising | advertisement | tracking | surveillance)
• ("ad blocker" | "ad blockers" | "traffic flows" | "surveillance
capitalism")
Excluded Terms
.-road -urban -cities -gas
B.2 Final Queries
• allintitle: (ecological | environmental) (cost | costs | impact
| impacts | footprint | sustainability) (online | web | website
| websites | digital) (ad | ads | analytics | advertising | adver-
tisement | tracking | surveillance) -road -urban -cities -gas
•allintitle: (ecological | environmental) (cost | costs | impact |
impacts | footprint | sustainability) ("ad blocker" | "ad block-
ers" | "traffic flows" | "surveillance capitalism") -road -urban
-cities -gas
• allintitle: (energy | carbon) (cost | costs | consumption | con-
servation | impact | impacts | footprint | assessment) (online |
web | website | websites | digital) (ad | ads | analytics | adver-
tising | advertisement | tracking | surveillance) -road -urban
-cities -gas
• allintitle: (energy | carbon) (cost | costs | consumption | con-
servation | impact | impacts | footprint | assessment) ("ad
blocker" | "ad blockers" | "traffic flows" | "surveillance capi-
talism") -road -urban -cities -gas
• allintitle: power (consumption | assessment) (online | web |
website | websites | digital) (ad | ads | analytics | advertising |
advertisement | tracking | surveillance) -road -urban -cities
-gas
• allintitle: power (consumption | assessment) ("ad blocker" |
"ad blockers" | "traffic flows" | "surveillance capitalism") -road
-urban -cities -gas
