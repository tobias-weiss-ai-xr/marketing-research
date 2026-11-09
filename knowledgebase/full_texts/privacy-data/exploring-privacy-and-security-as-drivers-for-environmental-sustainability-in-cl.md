---
title: Exploring Privacy and Security as Drivers for Environmental Sustainability in Cloud-Based Office
  Solutions (Extended Abstract)
url: https://arxiv.org/abs/2411.16340
category: privacy-data
subcategory: measurement
date: 2024-11
venue: arXiv (Cornell University)
authors:
- Jason Kayembe
- Iness Ben Guirat
- Jan Tobias Müehlberg
source: arxiv
pdf_url: https://arxiv.org/pdf/2411.16340
pages: 4
chars: 21931
fetched_at: '2026-11-08T12:59:33+00:00'
kb_version: 1
---

# Exploring Privacy and Security as Drivers for Environmental Sustainability in Cloud-Based Office Solutions (Extended Abstract)

arXiv:2411.16340v2  [cs.SE]  26 Nov 2024
Exploring Privacy and Security as Drivers for Environmenta l
Sustainability in Cloud-Based Oﬀice Solutions
(Extended Abstract)
Jason Kayembe
jason.kayembe@ulb.be
Université Libre de Bruxelles
Brussels, Belgium
Iness Ben Guirat
iness.ben.guirat@ulb.be
Université Libre de Bruxelles
Brussels, Belgium
Jan Tobias Mühlberg
jan.tobias.muehlberg@ulb.be
Université Libre de Bruxelles
Brussels, Belgium
ABSTRACT
This paper explores the intersection of privacy, cybersecu rity, and
environmental impacts, speciﬁcally energy consumption an d car-
bon emissions, in cloud-based oﬃce solutions. We hypothesise that
solutions that emphasise privacy and security are typically “greener”
than solutions that are ﬁnanced through data collection and ad-
vertising. To test our hypothesis, we ﬁrst investigate how t he un-
derlying architectures and business models of these servic es, e.g.,
monetisation through (personalised) advertising, contribute to the
services’ environmental impact. We then explore commonly u sed
methodologies and identify tools that facilitate environm ental as-
sessments of software systems. By combining these tools, we de-
velop an approach to systematically assess the environmental foot-
print of the user-side of online services, which we apply to i nvesti-
gate and compare the inﬂuence of service design and ad-block ing
technology on the emissions of common web-mail services. Ou r
measurements of a limited selection of such services does no t yet
conclusively support or falsify our hypothesis regarding p rimary
impacts. However, we are already able to identify the greener web-
mail services on the user-side and continue the investigati on to-
wards conclusive assessment strategies for online oﬃce sol utions.
KEYWORDS
privacy, security, environmental impacts
Reference Format:
Jason Kayembe, Iness Ben Guirat, and Jan Tobias Mühlberg. 2024. Exploring
Privacy and Security as Drivers for Environmental Sustainability in Cloud -
Based Oﬃce Solutions (Extended Abstract). In LOCO ’24: 1st International
Workshop on Low Carbon Computing, December 03, 2024.https://doi.org/10.48550/arXiv.2411.16340
1 INTRODUCTION
Following growing concerns over the environmental impactsof hu-
man activities across all sectors, this paper investigates the inter-
section of privacy, security, and the environmental conseq uences
of ICT services, with a particular focus on web-based email s er-
vices as an example of commonly used oﬃce solutions. We explore
how to deﬁne and evaluate these services, examine the archit ec-
ture and business models they rely on, and envision a framewo rk
Permission to make digital or hard copies of part or all of thi s work for personal or
classroom use is granted without fee provided that copies ar e not made or distributed
for proﬁt or commercial advantage and that copies bear this notice and the full citation
on the ﬁrst page. Copyrights for third-party components of this work must be honored.
For all other uses, contact the owner/author(s).
LOCO ’24, December 03, 2024, Glasgow, UK
© 2024 Copyright held by the owner/author(s).
https://doi.org/10.48550/arXiv.2411.16340
that can measure the energy consumption associated with spe ciﬁc
email services. Our research hypothesis is that online services that
emphasise privacy and security are typically “greener, ” and we take
web mailers as a case study to test this hypothesis.
Sending an email might seem like a trivial task; however the
scale at which large email services operate makes their envi ron-
mental impact signiﬁcant. For instance, according to Stati sta, a
web platform for markets statistics, an estimated 333 billion emails
were sent and received daily worldwide in 2022 [17]. Perhaps even
more important, beyond the data volume, is that the infrastr uc-
ture supporting email services requires many components of the
internet network to remain operational which, in return consumes
energy and requires maintenance continuously. This is illu strated
in [16] where Pärssinen et al. take inventory of common inter -
net network devices to derive the overall environmental imp act of
the online-advertising industry. An important factor inﬂu encing
the environmental impacts of the diﬀerent services is the bu siness
model behind the services. We identify six key models: 1. subscription-
based, 2. transaction-based, 3. freemium, 4. donation-based, 5. advertisement-
based, and 6. monetisation through data collection and rese lling.
Speciﬁcally, services that rely on advertising and data col lection
often deploy additional technologies that go beyond email f unc-
tionalities, leading to increased energy consumption: use r track-
ing, training of personalised models, and further advertis ing tech-
nologies that require large-scale infrastructure for storage and data
processing, thereby compounding their environmental foot print.
Additionally, the sending and rendering of advertisements monop-
olises resources. In a study assessing the environmental co st of
online advertising, Pärssinen et al. [16] describe the mech anism:
when a user visits a web page, it often initiates thousands of con-
nections to data centres on the user’s behalf. Some of these d ata
centres keep the connections open to deliver advertisement s as
long as the user remains on the page, thereby monopolising ne t-
work, data centre, and user device resources. Pearce et al. [12] quan-
tify this waste for user devices in their initiative to estimate the en-
ergy savings achievable through the use of ad-blockers, sho wing
that page load times can decrease by up to 28% with ad-blocker s.
This represents potential energy savings of 13.5 billion kW h per
year for internet users worldwide.
Thus, business models centred on data collection raise not o nly
privacy and security concerns but also exacerbate environm ental
costs. Validating the relationship between business models and en-
ergy consumption can guide the design of more secure, privac y
friendly and also more sustainable online services. This paper com-
pares the environmental burdens of three email service prov iders:
1

LOCO ’24, December 03, 2024 Kayembe et al.
Microsoft Outlook and Gmail, both of which rely heavily on adver-
tising and tracking technologies, and Proton Mail, which op erates
on a privacy-preserving and end-to-end secure freemium mod el
without the use of advertisements or trackers.
2 METHODOLOGY
We propose an approach that builds upon, and extends the work of
Pesari et al. [13] who examine the power usage of a computer vi s-
iting global news websites when using ad-blockers. Our appr oach
is designed to assess the energy consumption of a web service by
breaking it down into distinct, measurable functional unit s. Our
framework aims to (i) facilitate the comparison of similar s ervices
based on their energy consumption and (ii) highlight the con nec-
tion between data collection, processing, and the associat ed envi-
ronmental costs. We identify three key components in the ass ess-
ment: (1) user side, (2) network and server side, and (3) embo died
and end-of-life (EoL) emissions.
2.1 User-Side Assessment
To evaluate the emissions released by a user device when accessing
the service, and to identify the attributable share for trac king and
advertising, our framework involves six steps:
(1) Select Comparable Services: The framework is designed t o
compare diﬀerent implementations of online services. Dif-
ferent implementations may reveal diﬀerences in consump-
tion proﬁles, which could be attributed to various factors
distinguishing the implementations. However, in our case,
the aim is not to identify the greener solution, rather to
assess the impact of advertising mechanisms on device en-
ergy consumption. Hence we run the same service multiple
times, both with and without the ad-blocker activated. Ad-
ditionally we conﬁgure the browser to allow the blocking
of cookies and the restriction of certain website tracking
capabilities in order to account for the impact of tracking
mechanisms.
(2) Deﬁne Functional Units: We identify the common scenario s
that users typically engage in when using the service such
as logging into the account, reading three emails, replying
to, and logging out.
(3) Automate the identiﬁed scenarios for repeated executio n
without manual intervention.
(4) Monitor the Scenarios: This step involves executing the scripts
developed in the previous step and monitoring (i) machine
power or energy consumption (in Watts or Joules) and (ii)
data traﬃc on the network (in Bytes). This is achieved using
metric tool APIs relying on modern computers’ embedded
sensors to track their components power consumption.
(5) Convert Energy to Greenhouse Gas (GHG) Emissions: This
is typically done using an average grid energy mix, which
translates to the environmental cost of electricity produc -
tion (expressed in kgCO2-equivalent per kWh).
(6) Assess the User Side Use-Phase Emissions: Perform tasks 1
to 6 for both services and compute the diﬀerences in their
GHG emissions. Additionally, compute the diﬀerences in
the network data traﬃc they generated.
2.2 Network and Server-Side Assessment
Estimating server-side emissions is challenging due to the lack of
transparency from companies regarding environmental impa cts
and data processing and storage. This is highlighted, for ex ample,
by the European Data Protection Supervisor (EDPS) who found
that the European Commission’s use of Microsoft 365 does not
comply with EU data protection regulations due to unclarity re-
garding the collection, purpose, and processing location o f per-
sonal data [1]. Therefore, previous studies assessing the e nviron-
mental impact of the ICT sector [3, 10] often rely on global ma rket
and industry statistics for estimates. This leads to signiﬁcant uncer-
tainty across diﬀerent studies. In particular, the impact o f training
and maintaining advertising models is assumed to have high i m-
pacts that are hard to assess: training AI models is not only k nown
to be a computationally intensive task but also often requir es ex-
tra hardware accumulating thereby more embodied emissions . As
underlined in a review on diﬀerent estimates of ICT climate i m-
pact [3], the rising trend in AI and data science can be regard ed
as a threat to the future of the ICT climate impact as it drives a
steep growth in data storage and processing. Additionally, mod-
els are eventually used to target ads more eﬀectively, lever aging
the relationship, studied in [4], between perceived consum ption-
promoting online content and consumption levels. Both kind of
impact, i.e., direct and indirect, make it diﬃcult to derive precise
estimates of server-side energy consumption for any speciﬁ c ser-
vice. Nevertheless, we include this step to emphasise the im por-
tance of recognising and maintaining awareness of the subst antial
energy consumption and associated GHG emissions linked to d ata
processing:
(1) Collect Data from ICT Sector: We rely on the estimations
provided in [10], as it contains the most recent data avail-
able. Speciﬁcally, we use the study’s estimates of network
and server-side emissions per GB of data handled.
(2) Estimate Network and Server-Side Emissions: Multiply t he
diﬀerence in data traﬃc (calculated in step 6) by the respec-
tive ratios identiﬁed in the previous step to estimate the
share of attributable network and server emissions.
2.3 Embodied and End-of-Life Assessment
Similarly to the previous evaluation, this step involves ga thering
data from prior studies that assess the ICT sector [10]. Spec iﬁcally,
we need the ratios of the estimated embodied and End-of-Life(EoL)
emissions for the network and server sides per GB of data hand led.
3 EXPERIMENTAL RESULTS
We present a ﬁrst application of our framework to estimate an d
compare the environmental footprint of three major email providers:
Microsoft Outlook [11], Gmail [6], and Proton Mail [15]. We aim to
compare these services and assess the impact of browsing with and
without an ad-blocker, thus currently focusing on the user s ide.
We ﬁrst created diﬀerent email accounts with each provider.Six
fundamental functional units were deﬁned: Idle, Login, Logout,
No attachment , Attachment, Reply, and Delete. The idea is to
estimate consumption for more complex functional units by a g-
gregating the performance of basic ones.
2

Exploring Privacy and Security as Drivers for Environmenta l Sustainability in Cloud-Based Oﬀice Solutions LOCO ’24, D ecember 03, 2024
We then developed a simulation tool using Selenium [2] in or-
der to automate scenarios such as mouse clicks, user interac tions,
logging in, etc. This tool is available [9]. For our evaluati on we use
the Green Metric Tool (GMT) [7] which is speciﬁcally designe d
to monitor the power consumption of software. To achieve thi s it
uses containers which are small, lightweight virtual environments
that contain the necessary dependencies for programs to run . By
isolating the program in a container, the GMT creates a contr olled
environment that accurately evaluate the speciﬁc energy consump-
tion and data transfer attributable to the container. As an i ndica-
tor, the tool automatically converts the data traﬃc exchang ed by
the program on the network into the corresponding shares of t he
network’s and server’s emissions, which corresponds to the net-
work and server-side assessment[2.2] in our framework. Fin ally,
it can also accept relevant parameters describing the machi ne on
which it runs to estimate the monitored program’s share of em -
bodied emissions. This allows an assessment of the user side em-
bodied emissions. We conducted ﬁve runs for each functional unit,
collecting data on CPU energy, memory energy, machine energ y,
and network I/O. While no signiﬁcant diﬀerences were found, sug-
gesting that ad-blockers did not notably aﬀect energy consu mp-
tion, comparison among providers showed some diﬀerences, w ith
Gmail being slightly more energy-eﬃcient and Proton consum ing
more energy, particularly in memory usage. We then provide e s-
timates for emissions based on energy consumption. An objec tive
is to extend these measurements and contribute to the Energy ID
project [8] consisting in developing impact-based score ca rds for
diﬀerent software services.
3.1 Limitations and Future Directions
The primary limitation of this work, as previously mentione d, is
the lack of data transparency from companies handling user i nfor-
mation. While monitoring network exchanges can provide an e sti-
mate of the data collected by these platforms, there is no rel iable
way to assess the environmental impact of the data processing hap-
pening behind the scenes—simply because we don’t know what
is that processing. Enhancing our framework could involve l isting
the various data storage and processing technologies we are aware
of, along with approximate estimates of their carbon cost pe r giga-
byte. This might help us gauge how far a given provider’s practices
deviate from our current estimates. However, such insights would
remain indicative at best and could not serve as a basis for di rect
comparison. Our view is that, without regulations requirin g stake-
holders in this industry to disclose much more detailed info rma-
tion about their activities, it will remain challenging to a chieve a
comprehensive and accurate estimate.
In terms of network consumption, we believe our estimates ar e
closer to reality. However, as Freitag et al. discuss in thei r compar-
ative analysis of ICT climate impact estimates [3], there is ongoing
debate in the ﬁeld regarding this issue. We recognise that ne twork
consumption is not elastic, which challenges the validity o f our
emission allocation. Networks are designed to handle peak activity,
consuming a constant amount of energy regardless of data tra ﬃc
levels. It is only when growing data demand requires infrast ruc-
ture expansion that emissions increase. Nevertheless, sin ce higher
data transfer eventually results in higher emissions, we ma intain
that allocating responsibility for network emissions is ne cessary,
with the volume of data exchanged serving as a suitable crite rion.
On the user side, for which we have the most reliable estimate s,
several limitations need to be addressed. First, our tool cu rrently
does not account for the impact of the ad-blocker itself. Thi s lim-
itation could potentially be addressed by incorporating an exter-
nal ad-blocker such as Pi-hole [14] which blocks ads at the ne t-
work level by supplying non-routable DNS entries for ad serv ers.
Additionally, to ensure a fair comparison among providers, func-
tional units have been standardised to operate for the same d ura-
tion across diﬀerent providers using wait statements. Whil e this
approach helps maintain consistency, it reduces the click r ate and
may hide the time savings achieved by the ad-blocker, as high -
lighted by Pearce et al. [12]. To cross-validate our ﬁndings , we
could re-run the tests without these wait statements and pla ce
greater focus on the time savings aspect. Another reason for not
observing signiﬁcant diﬀerences between runs with and with out
ad-blockers could be that web-mail services typically display fewer
ads, relying instead on data collection and reselling as the ir busi-
ness model. Ad-blockers are less eﬀective against such mechanisms
as most processing happens server-side. This could explainthe lack
of variation in our current results. We are also critically a ware of
projections claiming that between 50% and 90% of all email tr aﬃc
is spam [5, 18], the management of which might have a measur-
able impact on sustainability metrics of a mail service. We l eave
assessment and evaluation of these aspects for future work.
4 CONCLUSIONS
Our work oﬀers insights into the environmental impact of onl ine
services. We proposed an approach and framework for the impa ct
assessment of software systems and partially apply this to e val-
uate services such as web mailers. Our approach not only faci li-
tates comparison between similar services based on energy c on-
sumption, but also highlights the connection between data c ollec-
tion, processing, and their environmental costs. Ongoing r esearch
focuses on expanding sample sizes, incorporating more dive rse
scenarios for functional units, and including server-side data for
greater accuracy, and to make the results more accessible to deci-
sion makers.
ACKNOWLEDGMENTS
We gratefully acknowledge the Brussels-Capital Region - Innoviris
for ﬁnancial support under grant numbers 2024-RPF-2 and 202 4-
RPF-4, and the CyberExcellence programme of the Walloon Re-
gion, Belgium (grant 2110186).
REFERENCES
[1] 2024. European Commission’s use of Microsoft 365 infrin ges data protec-
tion law for EU institutions and bodies | European Data Prote ction Supervisor.
https://www.edps.europa.eu/press-publications/press-news/press-releases/2024/european-commissions-
[2] Software Freedom Conservancy. 2024. Selenium. https:/ /www.selenium.dev
Accessed: 2024-10-02.
[3] Charlotte Freitag, Mike Berners-Lee, Kelly Widdicks, B ran Knowles, Gordon S.
Blair, and Adrian Friday. 2021. The real climate and transfo rmative impact of
ICT: A critique of estimates, trends, and regulations. Patterns 2, 9 (Sept. 2021),
100340. https://doi.org/10.1016/j.patter.2021.100340
[4] Vivian Frick, Ellen Matthies, John Thøgersen, and Tilma n Santarius. 2021. Do
online environments promote suﬃciency or overconsumption ? Online adver-
tisement and social media eﬀects on clothing, digital devic es, and air travel
3

LOCO ’24, December 03, 2024 Kayembe et al.
consumption. Journal of Consumer Behaviour 20, 2 (March 2021), 288–308.
https://doi.org/10.1002/cb.1855
[5] JuiHsi Fu, PoChing Lin, and SingLing Lee. 2014. Detectin g spamming activi-
ties in a campus network using incremental learning. Journal of network and
computer applications 43 (2014), 56–65.
[6] Google. 2024. Gmail. https://www.google.com/gmail/a bout/ Accessed: 2024-
10-02.
[7] Green Coding Project. 2024. Philosophy and Methodology of Green Cod-
ing. https://docs.green-coding.io/docs/prologue/phil osophy-methodology/ Ac-
cessed: 2024-10-02.
[8] Green Coding Project. 2024. Philosophy and Methodology of Green Coding.
https://www.green-coding.io/projects/energy-id/ Acce ssed: 2024-10-02.
[9] Jason Kayembe. 2024. Artifact: Exploring Privacy and Se curity as Dri-
vers for Environmental Sustainability in Cloud-Based Oﬃce Solutions.
https://github.com/jkayembe/thesis
[10] Jens Malmodin, Nina Lövehagen, Pernilla Bergmark, and Dag Lundén. 2024. ICT
sector electricity consumption and greenhouse gas emissio ns–2020 outcome.
Telecommunications Policy 48, 3 (2024), 102701.
[11] Microsoft. 2024. Microsoft Outlook. https://outlook .live.com/mail/ Accessed:
2024-10-02.
[12] Joshua M Pearce. 2020. Energy conservation with open so urce ad blockers. Tech-
nologies 8, 2 (2020), 18.
[13] Fabio Pesari, Giovanni Lagioia, and Annarita Paiano. 2 023. Client-side energy
and GHGs assessment of advertising and tracking in the news w ebsites. Journal
of Industrial Ecology 27, 2 (2023), 548–561.
[14] PiHole. 2024. Overview of Pi-hole - Pi-hole documentat ion.
https://docs.pi-hole.net/
[15] Proton. 2024. Proton Mail. https://proton.me/mail Ac cessed: 2024-10-02.
[16] M. Pärssinen, M. Kotila, R. Cuevas, A. Phansalkar, and J . Manner. 2018. Environ-
mental impact assessment of online advertising. Environmental Impact Assess-
ment Review 73 (Nov. 2018), 177–200. https://doi.org/10.1016/j.eiar .2018.08.004
[17] Statista. 2024. Daily Number of Emails Worldwide from 2 017 to 2025.
https://www.statista.com/statistics/456500/daily-number-of-e-mails-worldwide/
Accessed: 2024-10-02.
[18] Statista. 2024. Global spam volume as percent-
age of total e-mail traﬃc from 2011 to 2023.
https://www.statista.com/statistics/420400/spam-ema il-traﬃc-share-annual/
Accessed: 2024-10-02.
4
