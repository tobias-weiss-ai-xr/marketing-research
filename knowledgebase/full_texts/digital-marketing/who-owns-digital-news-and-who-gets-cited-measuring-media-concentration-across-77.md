---
title: 'Who Owns Digital News, and Who Gets Cited: Measuring Media Concentration Across 77 Countries and
  Seven AI Systems'
url: https://arxiv.org/abs/2610.40164
category: digital-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Peter Carragher
- Kathleen M. Carley
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.40164
pages: 12
chars: 71724
fetched_at: '2026-11-08T13:23:45+00:00'
kb_version: 1
---

# Who Owns Digital News, and Who Gets Cited: Measuring Media Concentration Across 77 Countries and Seven AI Systems

Who Owns Digital News, and Who Gets Cited: Measuring Media
Concentration Across 77 Countries and Seven AI Systems
Peter Carragher
Carnegie Mellon University
Pittsburgh, Pennsylvania, USA
pcarragh@andrew.cmu.edu
Kathleen M. Carley
Carnegie Mellon University
Pittsburgh, Pennsylvania, USA
carley@andrew.cmu.edu
Abstract
Digital news outlets compete for audience attention. Search en-
gines equipped with generative AI systems such as Google’s AI
overviews increasingly decide where that attention goes, as well
as the revenue it represents. Yet, the lack of a consistent data col-
lection infrastructure between national-level regulatory bodies has
hindered between-country comparative analysis of media concen-
tration, and with it any assessment of how these intermediaries
reshape digital news markets. To address this issue, we compile
an ownership dataset for 9,761 digital news outlets drawn from
Wikipedia and Wikidata, achieving high agreement with indepen-
dently compiled US and UK news directories. Using this dataset, we
derive traffic-weighted concentration indices for 77 countries. We
find that journalists report more owner pressure in countries with
higher concentration (𝜌=+ 0.318), and that outlet-level measures
understate concentration, with owner-level indices a median 1.30×
higher. Applying concentration measures to AI-mediated news dis-
covery, we find that citation distributions from major AI systems
are up to 2.08× more concentrated than traffic, and that if Google
AI Overviews mediated all organic search, the resulting rise in US
concentration would be several times that associated with highly
regulated media mergers and acquisitions. Finally, our analyses
indicate that AI systems preferentially cite state-controlled media
outlets when prompted in that country’s native language. Together,
these findings raise concerns about the effect AI systems may have
on digital media. We release the dataset to enable the monitoring of
digital news globally, so that the impact of disruptive technologies
on digital media markets can be tracked as they emerge.
CCS Concepts
•Social and professional topics→ Antitrust and competition;
•Information systems → Web searching and information
discovery;•Applied computing→Economics.
Keywords
Web economics, media concentration, news ownership, generative
AI, AI search, platform regulation
Introduction
On October 6, 2026, despite being challenged by twelve state attor-
neys general and the Writers Guild of America, Paramount Sky-
dance acquired Warner Bros. Discovery in a deal worth over $110bn.
By placing CBS News and CNN under a single owner, critics are
concerned the merger will impact external pluralism in US news.
When questions of media concentration invariably arise in such
cases, they are answered anew each time, a process made difficult
by a lack of standardization in how concentration is measured.
Figure 1: Ownership concentration by country, as HHI on
traffic shares by owner. Higher values mean traffic is held by
fewer owners. Unshaded countries have no estimate. Each
country’s state-controlled media are grouped under one state
entity (state-sponsored are not).
National regulators count licenses, circulation, or revenue within
their own borders and on their own definitions. As a result, there
is no readily available dataset that can be used to compare media
concentration between countries. This is a particularly timely issue,
given that the technological changes actively shaping the news
media, such as algorithmic curation and the proliferation of AI
overviews in search engines, are global in nature.
Digital news outlets exist in a market. Outlets compete for audi-
ence attention online, converting referral traffic from search engines
and, increasingly, generative AI systems into revenue. Missing own-
ership data therefore leave a Web economics question open: how
concentrated are national markets for digital news traffic once web-
sites are grouped by owner, and are citations from AI systems more
or less concentrated than that traffic? This places our work, along
with its recommendations regarding competition policy for digital
platforms, within the Web Economics and Digital Society track.
To answer it, we construct an international news ownership
dataset from crowd-sourced data on Wikipedia. We assign own-
ership labels to 9,761 domains and compute traffic-weighted con-
centration indices (Herfindahl Hirschmann (HHI)) for 77 countries,
while the largest prior cross-national study covered 30 [33].
The picture that emerges is one of substantial variation (Figure 1).
Here, HHI is the sum of squared market shares and runs from near
0 when many small owners split the market to 10,000 for a single
owner. Its reciprocal (10,000/HHI) is the effective number of equally
sized owners, and competition regulators use it to assess market
concentration and the effect of mergers [27]. In our measurement,
the number of effective owners per country ranges from more than
ten to fewer than three. Despite this variation, grouping outlets by
arXiv:2610.40164v1  [cs.CY]  29 Oct 2026

Carragher and Carley
owners reveals higher traffic concentration levels, with owner-level
indices being a median factor of 1.30×outlet-level indices.
We validate our concentration indices by comparing against
previously published concentration figures [33], and both an inde-
pendently compiled US ownership directory [23] and a UK news
directory [1]. We further compute agreement between the dataset
and a set of hand-annotated is-news labels, and between each out-
let’s assigned country and where its audience is located [ 2]. Our
indices reveal that media concentration tracks conditions reported
[25] from inside newsrooms: journalists report more owner and
commercial pressure where ownership is concentrated.
That excessive media concentration can result in such harm
is the reason that the FCC regulates traditional mergers and ac-
quisitions. However, existing regulations have blindspots around
emerging technologies, and AI-mediated news discovery is already
redistributing news attention. AI-generated answers have been
shown to substantially reduce click-through to publishers [4], and
publishers are rewriting distribution and search strategy as they
compete to gain AI citations [37]. Collectively called Generative En-
gine Optimization (GEO) after Search Engine Optimization (SEO),
these emerging strategies attempt to increase the rate at which a
domain is cited by generative models [5], such as those deployed
in AI overviews [14].
Whether the distribution of citations from AI systems follows ex-
isting media market structures, and what impact those systems will
have on future concentration levels, are open questions. We apply
our ownership dataset to investigate this, using citation counts from
seven AI systems: in doing so, we find that AI citation distributions
are 1.23×–2.08× more concentrated than traffic distributions at
the outlet-level, and 1.11×–1.79× more concentrated at the owner-
level. In addition, we find that the AI amplification effect (i.e. the
relative increase in concentration in citations over traffic) is most
pronounced in countries with lower traffic concentrations. As such,
if traffic to news outlets shifts to follow citations from AI systems,
the traffic concentrations reported here will increase, with less
concentrated markets being disproportionately affected. However,
given that measuring the impact of AI citations on traffic directly
requires longitudinal data, we leave this to future work.
Underscoring the importance of these findings are a series of
copyright infringement and unfair competition law suits that news
media companies are beginning to bring against AI intermediaries
over the impact of AI systems on declining news outlet traffic and
advertising revenues [45]. Whether regulators should focus their
efforts on these new cases or on those associated with traditional
mergers and acquisitions becomes an issue of policy priority. Does
a merger of two of the largest broadcast news owners move a
country’s media concentration more, or less, than the introduction
of AI overviews in Google Search? We estimate the impact of both
against our indices and return to the comparison in the Discussion.
Related Work
Digital News.Research on digital news covers a broad range of
topics such as local news provision [9], misinformation [11] and
“pink slime” detection [7], revenue modeling for unreliable news
[34], cross-national news diversity measurement [16], and social
media based news exposure [18]. While these works classify and
track digital news outlets in various ways, they do not record who
owns them. The resulting lack of market-structure analysis for
digital news media has been identified as a research gap in a recent
literature review on organizational influences in newsrooms [44].
Media concentration measurement.Increases in U.S. media con-
centration between 1983, when 50% of the US media was owned by
some fifty companies, and 2000, by which time this had fallen to six
companies, motivated a large body of research [8]. Researchers have
developed several measures to quantify concentration, such as the
Noam [32] and Herfindahl Hirschmann (HHI) indices [27]. These
measures have enabled the effects of mergers and acquisitions to be
evaluated, such as by the FCC who adopted HHI in 2005 [27]. Since
then, measures of media concentration have been applied to media
environments around the world in which corporate consolidation
is problematic [30, 33, 42, 46].
Comparative media analysis.Comparative media analysis de-
scribes how various journalistic cultures emerge given differing
political systems [ 24]. We draw on three cross-national survey-
based instruments: the Worlds of Journalism survey (WJS) [ 28],
the Reuters Digital News Reports’ country-level media trust scores
[20], and Reporters Sans Frontières (RSF) measures of press free-
dom [38]. Based on these indices, it has recently been demonstrated
that LLMs exhibit pro-government valences when prompted in the
languages of countries with lower media freedom [51], a finding
we build on in this work.
Search, AI intermediaries and publisher economics.Search engines
and AI overviews act as intermediaries between publishers and their
audiences. AI-generated answers reduce click-through to publishers
[4], generative engines can be optimized for citation [ 5, 14], and
publishers have begun to litigate over lost traffic and advertising
revenue [45]. Search engine audits have frequently measured which
sources results pages and news search surface [29, 39, 47] and how
much traffic search sends to state-linked sites [ 43]. Recent work
extends such measurement to LLM-based search engines whose
source selection can be manipulated [15] when retrieving citations
for new user queries [40].
A parallel line of research develops diversity-aware news aggre-
gation and recommendation algorithms [3, 13, 17] by measuring
external pluralism and incentivizing it through algorithmic inter-
vention [41, 49, 50]. Although we do take advantage of datasets of
AI citations to news outlets [31, 52], to the best of our knowledge,
there are no works that investigate the impact of AI systems on
media concentration. Pierson et al. [36] emphasize that current AI
media policy research has largely ignored structural power issues,
and explicitly list the impact that AI has on trends of “increasing
market concentration and power asymmetries” as a blindspot in
the literature.
Dataset
To compile our dataset of global news sources and their owning
companies, we utilize crowdsourced lists of broadcasting company
assets on Wikipedia. We compiled a list of broadcasting compa-
nies for which a Wikipedia category exists1 and used Wikipedia’s
1e.g., Nexstar’s page: https://en.wikipedia.org/wiki/Category:Nexstar_Media_Group

Measuring Media Concentration Across 77 Countries and Seven AI Systems
Figure 2: The ownership dataset has a long tail of owners that
own many news outlets (blue, left axis) and account for large
proportions of total traffic (orange, right axis; monthly visits
in millions). Both follow power laws (dashed lines; 𝛼≈ 2.2
for outlets, 𝛼≈ 2.4for traffic). The axis starts at 1, which
hides the 63% of owners with fewer than 1M monthly visits;
probabilities are computed over all owners.
Petscan service to retrieve the Wiki-pages of the news outlets each
company owns. News sources can be newspapers, TV stations, and
radio stations. To restrict to outlets with an official website, we
query Wikidata via SPARQL for each outlet’s official domain (2,684
outlets) and fall back to the website link in the outlet’s Wikipedia
Infobox. This yields 25,631 news domains across 211 countries.
We combine these ownership records with SimilarWeb traffic
estimates and site categories. Previous research has validated Sim-
ilarWeb traffic estimates against estimates from both Ahrefs and
computations of PageRank over the CommonCrawl webgraph [12].
While the definition of what counts as news is subject to extensive
research [26], we simply use SimilarWeb site categories to filter
out non-news websites from the dataset. Specifically, to the list
of 25,631 news domains, we remove domains that: are missing a
country code, have a traffic estimate of zero, have a SimilarWeb
site category unrelated to news (removes platforms, commerce and
streaming sites), or are news aggregators (via a Wikidata entity-type
rule). Of the remaining 22,928 domains, we filter out any that do not
have an ownership record. The resulting dataset has 9,761 domains.
We annotated a sample of 𝑛= 200of the remaining domains. 75%
are news, accounting for 82.6% of traffic in the sample. Counting
magazines and sports outlets increases this to 89% news, account-
ing for 95% of traffic. The appendix details coverage, filtering, and
annotation.
Owner sizes follow power laws, with a small number of large
groups sitting on a long tail of smaller news organizations (Figure 2).
Of the 3,540 owners in the dataset, 76.9% hold exactly one outlet and
87.5% hold one or two. Together the single-outlet owners account
for 27.5% of labeled news traffic, and within the median ranked
country they are 80.1% of the owners and 47.8% of the traffic.
Concentration Estimates
For a given country with 𝑛 media companies, let 𝑠𝑖 represent the
market share, in percent, of the𝑖𝑡ℎ largest company. We compute the
largest-owner share (𝑠1), CR4 (˝4 𝑖=1 𝑠𝑖), the Herfindahl–Hirschman
Index (˝𝑛 𝑖=1 𝑠2 𝑖 ), and the Noam index (HHI/√𝑛). A domain with 𝑘
co-owners contributes traffic/𝑘 to each co-owner. While estimates
are computed for 211 countries, we report results for the set of 77
countries that have at least five identified owners. For countries
that have less than five owners identified in Wikidata, coverage
was insufficient to produce reliable estimates. We compare concen-
tration estimates for two variants of the dataset, the 77 country
dataset described above (Figure 1), and a smaller 42 country variant
that filters out any country with less than 20 owner-labeled news
domains or whose domains account for less than 25% of the traffic
going to that country’s news domains.
Across the 42 reliable countries the median HHI is 1,715, or about
5.8 effective owners, with a median largest-owner share of 29% and
a median top-four share of 72%. The median well-covered national
news market therefore resolves to roughly six effective owners: one
organization holds about a quarter of news attention and the largest
four hold >50%. Across the wider set of 77 ranked countries the
median falls to 4.5 effective owners and CR4 rises to 80%, because
countries that fall outside the reliable set are smaller and thinner.
The least concentrated markets resolve to tens of effective owners,
the most concentrated to fewer than three.
Concentration indices provide information beyond simply the
number of owners. The UK has 215 identified owners and an HHI
of 1,877, because the BBC alone holds 40% of labeled news traf-
fic; Türkiye, by contrast, has 26 owners and alowerHHI of 1,360.
The BBC is just one example of a public service broadcasters that
accounts for significant traffic in a highly concentrated market.
Among the 47 countries for which we identify a largest owner, that
owner is a public or state entity in 2 of them. Outside these four,
public broadcasters often act as a counterweight to an otherwise
highly concentrated commercial sector.
State-Sponsored Media Labels
We use the state-media classification from the State Media Mon-
itor (SMM), a hand-compiled census of state-administered news
media maintained by the Media and Journalism Research Center
[19]. SMM grades outlets on ownership and governance, source of
funding, and editorial autonomy. In total, of the domains in our
dataset, 298 are classified as state-controlled by SMM labels, with
coverage spanning 80 countries. In our analyses, we treat all state-
controlled news outlets as being owned by a single entity (i.e. the
state), as treating them as independent entities would artificially
inflate market competition metrics. Wikidata supports a similar
classification with high precision but low recall against SMM, so
we rely on SMM and describe the Wikidata derived labels for state
sponsorship in the appendix.
Dataset Validation
We validate the dataset by evaluating agreement with published
concentration figures, independent ownership directories, and hu-
man annotations. The appendix reports further validation, such
as a high level of agreement between our country labels and the

Carragher and Carley
country from which the majority of the news domain’s audience
originates, as derived from SimilarWeb data, and shows that our
analyses are invariant under different inclusion criteria.
Published figures.Against Noam’sWho Owns the World’s Media?
[33], our index reproduces his four-firm newspaper concentration
ratio at 𝜌=+ 0.465( 𝑝= 0.011, 𝑛= 29). His newspaper-press
HHI ranking is also reproduced ( 𝜌=+ 0.407, 𝑝= 0.025, 𝑛= 30).
Noam’s figures are for 30 countries in 2008–2013 and mostly mea-
sure the print press (online news is covered for only 20 countries),
so moderate correlations are expected. The comparison spans more
than a decade and a change of medium from newspapers to digital
news. As such, our index reads systematically less concentrated
than Noam’s print series, which is likely related to the inclusion of
a long tail of small news outlets. The rank agreement is nonetheless
evidence that it tracks national ownership concentration.
Owner directory.A total of 𝑛= 638news domains in our dataset
overlap with the Medill Local News Initiative directory of US news-
papers [22, 23]. Against the Medill dataset, our ownership labels
achieve a 73.5% agreement rate. When weighted by traffic, the do-
mains with matching owners account for 91.9% of the traffic that
the overlapping domains receive, revealing that agreement rates
are higher for news domains that receive more traffic.
Where Medill disagrees with our dataset, we validate by man-
ually annotating the disagreeing domains. We find that Medill is
typically correct, with errors on Wikipedia being caused by the
crowdsourced ownership attributes being out of date. Infoboxes of-
ten lag recent acquisitions, such as CherryRoad Media’s acquisition
of several Gannett newspapers [10].
Medill data also contains historical data on acquisitions. Using
this, we find that our Wikipedia ownership dataset reaches an agree-
ment rate of 93.6% on overlapping domains with the Medill dataset,
if we consider either the current or last owner — thus accounting
for the Wikipedia data being out of date by a single recent acquisi-
tion. Domains matched under this condition account for 98.8% of
overlapping traffic. While this level of agreement is already very
high, any error that might be induced by inaccuracies is minimized
by the fact that acquisitions typically serve to increase media con-
centration. As such, country-level concentration measures derived
from these labels would be biased in the same direction, and could
be considered lower-bounds.
Annotations.On 200 hand-annotated domains the primary filter
has precision 0.744, recall 0.970 and traffic-weighted precision 0.831,
retaining 84.0% of the list. The unfiltered list is only 66.0% news by
human judgement, and the non-news it contains (platforms, news
aggregators, etc.) dominate traffic distributions. As such, removal
of non-news websites can have a large impact on HHI measures.
For example, US HHI falls by a factor of four once large platforms
are removed. Finally, we annotate a subset of US news domains (𝑛=
321) with ownership labels and find that the Wikidata ownership
labels agree with our annotations (95.8%).
Results
We first relate our concentration indices to reports of ownership
pressure [28], then compare traffic with AI citation data from Ahrefs
[6] and AI Search Arena [31], and finally ask whether AI systems
Figure 3: WJS indicators show that ownership concentration
(HHI(traffic)) correlates with reports of owner and manager
influences by journalists [28]. The same indicators often have
opposing correlations with media trust [ 20]. Filled markers
show significance.
show preference toward state media [19] and how amplification
relates to media trust [20].
Reported Ownership Pressure
Table 1 shows that WJS ownership pressure ratings correlate with
concentration indices, in particular the largest-owner share (+0.359).
Since WJS country aggregates are produced by surveying journal-
ists, correlations between the WJS aggregates and traffic-weighted
concentration indices (Figure 3) represent a relation between the
media market structure and the experiences of journalists in the
newsroom. We also find that this relationship is not explained by
developmental indicators. Adding controls for GDP per capita, in-
ternet penetration, and population to a regression model predicting
WJS ownership pressure leaves the association intact (𝛽=+ 0.302
on log HHI,𝑝=0.029,𝑅 2 =0.478,𝑛=54).
AI Citations
This section asks whether the citations from AI systems follow
the existing structure of media ownership. We collect Ahrefs AI-
response counts showing how often each domain is cited by one of
five AI systems, ChatGPT, Copilot, Gemini, Google AI Overviews
(‘Google’) and Grok. Ahrefs counts AI citations based on the re-
sponses each system gives to queries drawn from Google’s “People

Measuring Media Concentration Across 77 Countries and Seven AI Systems
Measure Owners Managers Org
Largest-owner share +0.359** +0.401** +0.403**
HHI +0.318* +0.365** +0.359**
Noam index +0.242 +0.290* +0.257
Top-4 owner share +0.164 +0.189 +0.193
Table 1: Spearman correlations across 55 countries between
each measure of ownership concentration (rows) and each
WJS rating of ownership pressure [ 28]: the influence jour-
nalists report from the owners of their news organisation,
from its business managers, and the organizational-influence
index ("Org"). Ratings run 1–5 with 5 most influential, so a
positive value means journalists in more concentrated mar-
kets report more pressure.
Also Ask” corpus 2. The AI citation data covers 4,584 news domains
across 199 countries. We filter out one country for which there are
fewer than 10 domains receiving AI citations, and report results
on the overlap with the 77 countries for which we have reliable
concentration measures. Where mean and median measures are
presented over multiple AI systems, the measure is first computed
separately per system, and then aggregated. Otherwise, summing
two citation distributions gives an HHI that underestimates the
average of their separate HHIs. 3
Related to our research questions on the impact of AI systems
on media concentration, we test four hypotheses:
H1AI citations are more concentrated than traffic.
H2 AI citations are more concentrated than traffic after group-
ing outlets by owner.
H3AI concentration tracks ownership concentration.
H4 When prompted in the relevant native language, AI sys-
tems cite state media sources more than expected based on
traffic levels.
Because the Ahrefs collection method may carry its own biases,
we also compute citation counts for our news domains in the AI
Search Arena dataset [ 31]. Its coverage of our dataset is lower,
so only Ahrefs data is used for H1–H3, but Arena adds a second
measurement of Gemini, search-enabled Perplexity and GPT 4.0,
and non-English prompts.
H1. Citations are more concentrated than traffic. For each country
and each AI system, we compare the HHI of citations with the HHI
of traffic over the same outlets. A positive difference (amplification)
means AI answers draw on a narrower set of outlets than audiences
do. Using a Wilcoxon signed-rank test, all 5 systems reject the null
at 𝑝< 10−6, supporting H1, that HHI(AI)>HHI(traffic) . Table 2
shows that AI systems cite a narrower set of outlets than audiences
visit in 67%–86% of countries.
We also check whether AI citations are allocated across outlets
differently from traffic. We correlate outlets’ traffic ranks with their
citation ranks, and check whether the most-cited outlets are also
the most-visited. While median within-country rank correlation
between traffic share and citation share indicates agreement (𝜌=
2https://ahrefs.com/blog/brand-radar-methodology/
3This fact follows from applying Jensen’s inequality to HHI.
Figure 4: AI owner amplification rates are higher in countries
with lower media concentration (𝜌=−0.32*).
0.63), this does not necessarily mean that AI citations and traffic
favor the same set of outlets.
We test whether the citation ranking of two AI systems agree
with each other more than their agreement with traffic estimates
would predict. The median rank correlation between each individual
system and traffic is 0.51, with a mean correlation of 0.49. If each
system cited outlets independently, their correlation with traffic
would account for the entire correlation between the two AI system
rankings leading to an expected correlation of0 .51× 0.51≈ 0.26.
However, the median rank correlation between two systems is 0.65.
The most-cited outlet is the most-visited in only 21 of 76 countries.
So, while there is substantial overlap between the outlets cited by
AI and those that attract the most traffic, there are also systematic
differences as exemplified by higher inter AI system agreement.
H2. H1 holds after grouping outlets by owner.Figure 4 demon-
strates AI amplification at the owner-level, with most countries
having an amplification rate > 1. After summing traffic and cita-
tions across each owner’s outlets, we repeat the same test as for
H1. Owner-level HHI(AI) and HHI(traffic) are strongly correlated
across countries ( 𝜌= 0.78***). Averaged over the 5 systems the
owner-level amplification is+600HHI (1.38×); at the outlet level
it is+445(1.57×). Although the effect is smaller than at the outlet
level, the result holds for 54 of countries and under every variant
of the dataset we test (see the appendix). Hence, H2 is supported.
H3. AI concentration tracks ownership concentration. Across coun-
tries, we correlate AI concentration and amplification with own-
ership HHI. Because countries with fewer owners score high on
both by construction, we control for the number of owners and
for traffic concentration. Owner-level AI concentration correlates
with ownership HHI at 𝜌=+ 0.766,+0.496after controlling for the
number of owners in the country (𝑝= 1.4× 10−4), and+0.35after
controlling for both number of owners and traffic concentration.
This result holds under all 5 owner-set variants tested (see the ap-
pendix). As such, among countries with comparable numbers of

Carragher and Carley
By outlet By owner
Data Model AI÷traffic HHI𝑛 AI>traffic AI÷traffic HHI𝑛 AI>traffic
Ahrefs Gemini 2.08×*** [1.65, 2.56] 65 / 76 1.79×*** [1.49, 2.00] 47 / 53
Copilot 1.60×*** [1.38, 1.86] 59 / 76 1.33×*** [1.13, 1.57] 42 / 54
Google 1.57×*** [1.36, 1.73] 60 / 76 1.34×** [1.14, 1.46] 39 / 54
ChatGPT 1.35×*** [1.22, 1.63] 61 / 76 1.33×*** [1.16, 1.58] 41 / 54
Grok 1.23×** [1.09, 1.38] 51 / 76 1.11×* [1.02, 1.31] 35 / 54
Arena Perplexity 1.76×*** [1.47, 1.95] 23 / 31 1.19×* [0.99, 1.53] 20 / 31
Gemini 1.70×[1.02, 2.70] 13 / 17 1.28×[0.99, 1.67] 12 / 16
GPT 4.0 1.60×* [1.23, 6.05] 10 / 13 1.47×* [1.09, 1.73] 10 / 13
Table 2: AI citation concentration against attention concentration, for each system, with outlets grouped by owner in the
right-hand pair. Values are medians across countries; 𝑛AI>traffic counts the countries in which the system’s citations are more
concentrated than attention. Stars are a two-sided Wilcoxon signed-rank test of AI against traffic HHI across countries,
uncorrected; Benjamini–Hochberg adjustment across the five systems leaves every star unchanged. ‘Google’ is Google AI
Overviews. ‘Sonar’ is the Sonar-Reasoning-Pro perplexity model. Note that results on the Arena dataset [ 31] are underpowered,
with wide confidence intervals. *𝑝<0.05, **𝑝<0.01, ***𝑝<0.001.
owners and levels of traffic concentration, the ones whose owner-
ship is more concentrated also see AI citations more concentrated
by owner.
While H3 is supported, analysis reveals an interesting relation-
ship (𝜌=− 0.32*) between AI amplification and owner-level traffic
HHI (Figure 4). Amplification ratios are higher where ownership
is less concentrated, suggesting that AI systems may cause more
media concentration to occur in markets with lower levels of media
concentration. As such, AI concentration is higher in absolute terms
where ownership is concentrated, while the multiple by which it
exceeds traffic concentration is larger where ownership is dispersed.
Ahrefs vs. Arena.Table 2 compares the amplification rates mea-
sured for a series of AI systems across the two datasets. We note
that results on the arena dataset are underpowered, as coverage
over our news domains is poor. However, on the3, 964overlapping
domains, logged citation counts are well correlated ( 𝜌= 0.536).
Similar to Ahrefs data, citation counts from Arena are significantly
more concentrated at the outlet-level than traffic. We again see that
amplification effects persist at the owner-level, but owner-level am-
plification is weaker compared to outlet-level across both datasets.
While both datasets are subject to biases induced by data collection
methodologies, corroboration between the two datasets reveals that
the AI amplification of media concentration that we measure is not
a product of these biases.
State Media
We demonstrate that state media ownership plays an important role
in shaping journalism cultures by comparing to measures of press
freedom. Then, we answer the question of whether AI citations
show a preference toward state media.
Press freedom indices.We collect RSF indices on press freedom.
Table 4 shows that the proportion of news traffic that a country’s
state-sponsored media accounts for correlates negatively with RSF
indices of press freedom [38]. Counter to this, the proportion of
traffic accounted for by public service broadcasting correlates posi-
tively with press freedom.
AI citation rates.For each country, system, and class (state-controlled
or public-service), we calculate an AI amplification rate (citations
/ traffic) and test the log ratio across countries with a Wilcoxon
signed-rank test. On Ahrefs data, 𝑝> 0.05for every system and
class, and confidence intervals around the state-controlled ratios
include 1 for every system (Table 3). At first glance, this finding is
in contrast to recent research on the influence of state media on
LLMs. It has been shown that, when a country has lower media
freedom, LLMs tend to exhibit greater pro-government valence
in that country’s language[ 51]. As such, we should not expect a
preference to be visible in Ahrefs data, which is compiled using
English prompts. The Arena dataset, however, is not subject to the
same limitation.
H4. AI systems cite state media sources more than expected based
on traffic levels when prompted in the relevant native language.In
the Arena dataset, 40% of prompts are not in English. Restricting to
users in a country, prompting in its national language, and citing
that country’s own outlets, state-controlled media are cited 1.65×
[1.46, 1.87] more often than commercial outlets matched to the same
traffic share: state-controlled outlets are cited at 1.01× their traffic
share, against 0.61× for the matched commercial bloc, across 2,961
citations in 16 countries. Asked in a country’s own language rather
than in English, the same outlets’ citations go to state-controlled
media 16.7% of the time against 6.0% (difference 10.7% [8.4%, 12.9%]).
This is caused primarily by Russia and China. There are 2.5× as
many citations to Chinese state-controlled outlets in responses
to Mandarin prompts as there are for English prompts. Likewise,
Russian prompts provoke 5.3× more citations to Russian state media
than English prompts do (Table 8).
Media trust and AI amplification
Here we ask whether the AI citations amplification effect is stronger
in countries with lower media trust. In countries where media trust
is lower, if AI systems depend more heavily on smaller sets of outlets
(for example, those that are well-known), a negative correlation
between media trust and the AI amplification rates would follow.

Measuring Media Concentration Across 77 Countries and Seven AI Systems
Class Data source System countries cite : traffic 95% CI amplified suppressed p
public-service Ahrefs (English panel) ChatGPT 15 0.51×[0.26, 1.53] 6 9 .208
Copilot 15 0.22×[0.12, 0.77] 3 12.008
Gemini 15 0.01×[0.00, 1.63] 5 10.015
Google 15 0.57×[0.01, 1.50] 5 10 .095
Grok 15 0.69×[0.13, 1.36] 7 8 .277
Arena (native language) All systems 3 0.82×[0.01, 1.01] 1 2 –
state-captured Ahrefs (English panel) ChatGPT 26 0.92×[0.36, 2.25] 13 13 .708
Copilot 26 0.50×[0.25, 1.10] 9 17.027
Gemini 26 0.74×[0.00, 1.70] 9 17 .053
Google 26 0.92×[0.55, 2.12] 12 14 .727
Grok 26 0.99×[0.54, 1.86] 13 13 .671
Arena (native language) All systems 102.71×[0.14, 9.87] 7 3 .492
Perplexity 92.67×[0.01, 30.86] 6 3 .652
Gemini 51.61×[0.01, 21.06] 3 2 1.000
GPT-4o 41.15×[0.01, 4.40] 2 2 1.000
Table 3: Is state media amplified or suppressed, per class, data source and AI system? For each country we take the class’s share
of a system’s citations over its share of that country’s news traffic; we report the median of that ratio across countries, how
many countries fall on each side of parity, and a two-sided Wilcoxon signed-rank test of the log ratio against zero. Ahrefs
rows come from answers to an English keyword panel; Arena rows are restricted to prompts in the country’s own language,
following previous work [51]. Arena reaches too few countries to test public service broadcasting.
Class countries with sector𝜌
state-captured 122 38−0.279**
independent public 122 20 +0.282**
pooled 122 52−0.056
Table 4: Correlates between each country’s Reporters With-
out Borders (RSF) press freedom indicator and both the share
of traffic received by that country’s public service broadcast-
ing and state-captured outlets.
For this, we use country level media trust scores from the Reuters
Digital News Reports media trust survey instruments [ 20], and
we find a significant negative correlation ( 𝜌=− 0.467**, 𝑛= 40).
Higher-trust countries see less owner-level AI amplification. Fur-
thermore, we find that media concentration does not explain the re-
lationship between trust and AI amplification. While concentration
correlates with amplification (𝜌=− 0.429**), media concentration
and media trust are themselves unrelated ( 𝜌=+ 0.013), and so
controlling for media concentration leaves the association between
amplification and trust intact (𝜌=− 0.496***). So, the relationship
between media trust and AI amplification persists independently of
media concentration, suggesting that differences in media trust may
be associated with how AI systems distribute citations across news
outlets. While this is one possible explanation, we refrain from
making any claims that AI systems do in fact distribute citations
according to media trust, and leave this for future work.
Discussion
This work provides current and cross-national answers to questions
around the number of organizations that operate in a country’s
media system and how much online traffic is concentrated among
them. We motivate this work by showing how increased media con-
centration is associated with journalists’ reports of organizational
influence on editorial decisions (Figure 3). Our dataset provides
a comparative baseline for the types of merger cases this paper
opened with. Take the Paramount–Warner Bros. Discovery litiga-
tion, for example. Combining the two groups’ outlets under one
owner raises our traffic-based estimate of US media concentration
by+9.9%. Now take the current market as the baseline, in which
we assume that AI overviews mediate a negligible share of news
traffic, and consider the case where all organic search traffic passes
through Google AI Overviews. In this scenario, with attention redis-
tributed in proportion to Google AI Overview’s citations, US media
concentration rises by+33.3%, roughly 3.4 times the Paramount
merger’s effect. Furthermore, the effects are felt internationally,
with the median country’s owner-level HHI increasing by+26.3%
(in 49 of 67 countries). Although we cannot yet conclude that traffic
will come to follow citations, which requires longitudinal analysis,
this scenario is indicative that platform and AI policy may now be
more important than regulating mergers and acquisitions.
The strongest AI system amplifies concentration threefold more
than the weakest, and consulting several systems exposes a reader to
meaningfully more diversity than consulting one — differences that
dwarf most of the cross-country variation in the market baseline.
This inverts where policy levers sit. The instruments of pluralism
policy are national and aimed at owners: licence caps, merger re-
view, cross-ownership rules. The variation that now matters most is
between platforms, is set by citation behavior rather than by owner-
ship transactions, and is global in reach. As such, FCC interventions
in mergers and acquisitions between media conglomerates such
as Paramount and Warner Bros. Discovery represent a national
remedy applied to the ownership layer, while AI systems may have
a more severe effect and are held accountable by no media reg-
ulator. Exemplifying this issue is the fact that, according to our

Carragher and Carley
analysis, which assistant a reader uses may matter more for traffic
concentration than which country they live in.
For the economics of digital news, AI systems impact media con-
centration through two mechanisms at once. The first is citation
allocation, measured here: citations concentrate by owner beyond
what attention concentration predicts. The second is in traffic gen-
eration and click-through rates, where AI citations typically fail
to deliver readers. According to recent estimates, roughly one AI
citation link in twenty is clicked, well below click-through in con-
ventional search [4]. As AI-mediated discovery displaces organic
search, that ratio becomes a downwards pressure on referral traffic
as a whole, and therefore on revenue. In an industry defined by
high fixed costs and low marginal costs [ 33], declining revenues
will necessitate greater levels of efficiency on the production side.
Hence, the economies of scale that govern the organizational forms
that media environments take on will strengthen, making media
markets yet more concentrated in equilibrium. Symptomatic of
these efficiencies are the waves of persistent layoffs and reduced ed-
itorial output reported across the sector [35]. The concern this work
raises is that, through increasing traffic concentration (and decreas-
ing traffic overall), AI systems as they exist today will indirectly
exacerbate these issues.
We extend three lines of existing work. We reproduce Noam’s
four-firm ranking [33], while at the same time translating his media
concentration program from national press and broadcast censuses
to attention-weighted measurement of digital news. We show that,
once ownership labels are attached, traffic concentration tracks
ownership pressure reported by journalists. As such, monitors work-
ing from audience data alone (i.e., without ownership labels) may
miss harms of media concentration. Finally, we extend the study of
algorithmic curation and source diversity [3, 13, 17] from search and
social feeds to generative systems, including their native-language
preference for state-controlled media [ 51]. Underlying all three
is our ownership dataset. The lack of a consistent, cross-national
news ownership dataset has been the chief obstacle to compara-
tive analysis of media concentration, and we release the dataset 4
and code so that concentration in new information systems can be
monitored.
Limitations
The ownership labels are derived from Wikipedia categories, Wiki-
data ownership fields and website links, and Wikipedia infoboxes.
As a result, underlying issues in these systems will carry forward
into our dataset. For example, editor attention may vary across coun-
tries and language editions, and acquisitions may go unrecorded.
Furthermore, our validation against the Medill dataset [23] covers
the United States only, where Wikipedia coverage is known to be
stronger. Where available, the integration of official data sources
such as registries and regulator filings would extend that validation
to countries where the data are weakest. We note that, while our
findings do reproduce on subsets of countries with better label
coverage, coverage is also negatively related to measured concen-
tration (𝜌=− 0.347, 𝑝= 0.002, 𝑛= 77). Our labels cover 28.8%
of domains and 70.1% of traffic, so poorly covered countries may
appear more concentrated than they are.
4https://doi.org/10.5281/zenodo.22782826
However, even given complete labels, the index uses traffic es-
timates and citations rather than editorial influence, advertising
revenue or political power. This restricts the production-economics
argument in the Discussion. However, since it is known that in-
forming voters is a critical information need served by news media
[48], election polling routinely asks which outlets shape voting de-
cisions [21], and as a result, data to compute measures of editorial
influence may be available. Reproducing our findings on influence
based indices would strengthen the case for causal modeling of
media concentration and its impacts.
These limitations have important implications for the AI citation
analysis. Ahrefs data is from a commercial panel whose prompt set
is proprietary and English- and United States-weighted. We there-
fore replicate on the AI Search Arena dataset [31], whose prompts
are organic user questions and roughly 40% of them not in English.
Agreement across two panels makes an artefact of either collection
process less likely, though both remain snapshots. Moreover, AI
systems cite few sources by construction, so some elevation of con-
centration relative to traffic may be unavoidable, and our analysis
does not account for the order or ranking of sources that get cited.
Finally, owner-level analysis of AI citations rests on a smaller set
of 54 countries, because only 1,653 of 4,584 AI-cited news domains
carry an ownership label. This issue is particularly acute for the
Arena data, upon which any statistical claims are difficult to defend.
The AI findings are accordingly best read as generating hypotheses
that longitudinal data can test.
Conclusion
We release a cross-national news ownership dataset and use it to re-
veal that media concentrations across 77 countries are higher than
the corresponding outlet-level concentrations. Our concentration
indices correlate with the degree of commercial pressure reported
by journalists, and after incorporating state media labels into the
dataset, the indices reproduce external indicators of press freedom.
AI citation behavior then acts on that structure. AI citations are
more concentrated than attention at the outlet level, and again once
outlets are grouped by owner. Asked in a country’s own language,
these systems cite state-controlled outlets 1.65× more than com-
mercial outlets of the same size. AI systems now allocate digital
news attention at a scale comparable to the mergers regulators
review, and we argue that traditional antitrust regulations should
be extended to cover new AI systems. Without this, global trends of
increasing media concentration are likely to accelerate. The dataset,
the labels and the full analysis pipeline are released so that this
work can be expanded upon.
Acknowledgements
We thank Dr. Zachary Metzger at the Medill Institute for providing
ownership data for print outlets. This work was supported in part
by the Office of Naval Research grant (N000142412568) and the
Knight Foundation. The views and conclusions in this document
are those of the authors and should not be interpreted as represent-
ing the official policies, either expressed or implied, of the Knight
Foundation, Office of Naval Research, or the U.S. Government.

Measuring Media Concentration Across 77 Countries and Seven AI Systems
References
[1] 2019. Public Interest News Foundation. https://www.publicinterestnews.org.
uk/. https://www.publicinterestnews.org.uk/ Registered Charity No. 1191397;
Company No. 12320800.
[2] 2026. SimilarWeb. (2026). https://www.similarweb.com/corp/ourdata/
[3] Himan Abdollahpouri, Edward C. Malthouse, Joseph A. Konstan, Bamshad
Mobasher, and Jeremy Gilbert. 2021. Toward the Next Generation of News
Recommender Systems. InCompanion Proceedings of the Web Conference 2021
(New York, NY, USA, 2021-06-03)(WWW ’21). Association for Computing Ma-
chinery, 402–406. doi:10.1145/3442442.3452327
[4] Saharsh Agarwal and Ananya Sen. 2026. The Impact of Google AI Overviews
on Publisher Traffic and User Experience: Evidence from a Field Experiment.
(2026).
[5] Pranjal Aggarwal, Vishvak Murahari, Tanmay Rajpurohit, Ashwin Kalyan,
Karthik Narasimhan, and Ameet Deshpande. 2024. GEO: Generative engine
optimization. InProceedings of the 30th ACM SIGKDD conference on knowledge
discovery and data mining. 5–16.
[6] Ahrefs. 2023. SEO tools & resources to grow your traffic. (2023). https://ahrefs.
com/
[7] Abdullah Aljebreen, Weiyi Meng, and Eduard C. Dragut. 2024. Analysis and
Detection of “Pink Slime” Websites in Social Media Posts. InProceedings of the
ACM Web Conference 2024 (WWW ’24). ACM, 2572–2581. doi:10.1145/3589334.
3645588
[8] Ben H Bagdikian. 2004. The new media monopoly: A completely revised and
updated edition with seven new chapters. Beacon Press.
[9] Simona Bisiani, Agnes Gulyas, John Wihbey, and Bahareh Heravi. 2025. Uk-
twitnewscor: A dataset of online local news articles for the study of local news
provision. InProceedings of the International AAAI Conference on Web and Social
Media, Vol. 19. 2371–2384.
[10] Mark Caro. 2025. Paving the CherryRoad. https://localnewsinitiative.
northwestern.edu/posts/2025/05/12/jeremy-gulban-cherryroad-q-and-
a/index.html. Accessed: 2026-01-XX.
[11] Peter Carragher, Evan M Williams, and Kathleen M Carley. 2024. Detection and
discovery of misinformation sources using attributed webgraphs. InProceedings
of the International AAAI Conference on Web and Social Media, Vol. 18. 214–226.
[12] Peter Carragher, Evan M Williams, and Kathleen M Carley. 2025. Misinformation
resilient search rankings with webgraph-based interventions.ACM Transactions
on Intelligent Systems and Technology16, 1 (2025), 1–27.
[13] Abhijnan Chakraborty, Mohammad Luqman, Sidhartha Satapathy, and Niloy
Ganguly. 2018. Editorial Algorithms: Optimizing Recency, Relevance and Diver-
sity for Automated News Curation. InCompanion Proceedings of the The Web
Conference 2018(Republic and Canton of Geneva, CHE, 2018-04-23)(WWW
’18). International World Wide Web Conferences Steering Committee, 77–78.
doi:10.1145/3184558.3186937
[14] Mahe Chen, Xiaoxuan Wang, Kaiwen Chen, and Nick Koudas. 2025. Generative
engine optimization: How to dominate AI search.arXiv preprint arXiv:2509.08919
(2025).
[15] Pei Chen, Geng Hong, Xinyi Wu, Mengying Wu, Zixuan Zhu, Mingxuan Liu,
Baojun Liu, Mi Zhang, and Min Yang. 2026. Unveiling the Resilience of LLM-
Enhanced Search Engines against Black-Hat SEO Manipulation. InProceedings
of the ACM Web Conference 2026 (WWW ’26). ACM, 2962–2973. doi:10.1145/
3774904.3792399
[16] Xi Chen, Scott A. Hale, David Jurgens, Mattia Samory, Ethan Zuckerman, and
Przemyslaw A. Grabowicz. 2024. Global News Synchrony and Diversity During
the Start of the COVID-19 Pandemic. InProceedings of the ACM Web Conference
2024 (WWW ’24). ACM, 2639–2650. doi:10.1145/3589334.3645645
[17] Seonghwan Choi, Hyeondey Kim, and Manjun Gim. 2022. Do Not Read the
Same News! Enhancing Diversity and Personalization of News Recommendation.
InCompanion Proceedings of the Web Conference 2022(New York, NY, USA,
2022-08-16)(WWW ’22). Association for Computing Machinery, 1211–1215.
doi:10.1145/3487553.3524936
[18] Salim Chouaki, Abhijnan Chakraborty, Oana Goga, and Savvas Zannettou. 2024.
What News Do People Get on Social Media? Analyzing Exposure and Consump-
tion of News through Data Donations. InProceedings of the ACM Web Conference
2024 (WWW ’24). ACM, 2371–2382. doi:10.1145/3589334.3645399
[19] Marius Dragomir and Astrid Söderström. 2022. The state of state media.A Global
Analysis of the Editorial Independence of State Media Based on the State Media
Matrix(2022).
[20] J Egan, CT Robertson, A Ross Arguedas, N Newman, RK Nielsen, M Mukherjee,
and R Fletcher. 2026. Reuters Institute digital news report 2026. (2026). doi:10.
60625/risj-4vgf-s811
[21] Richard Fletcher, Nic Newman, and Anne Schulz. 2020.A Mile Wide, an Inch
Deep: Online News and Media Use in the 2019 UK General Election. Technical
Report. Reuters Institute for the Study of Journalism. doi:10.60625/risj-205t-c448
[22] Tim Franklin. 2024. The State of Local News 2024: Expanding Deserts, Shifts
in Ownership, and Expanded Digital Coverage. Online report, Northwestern
University. https://localnewsinitiative.northwestern.edu/projects/state-of-local-
news/2024/ Accessed January 2026.
[23] Tim Franklin. 2025. The State of Local News 2025. Online report, Northwestern
University. https://localnewsinitiative.northwestern.edu/projects/state-of-local-
news/2025/ Accessed January 2026.
[24] Daniel C Hallin and Paolo Mancini. 2004.Comparing media systems: Three models
of media and politics. Cambridge university press.
[25] Thomas Hanitzsch, Folker Hanusch, Jyotika Ramaprasad, and Arnold S. de
Beer (Eds.). 2019.Worlds of Journalism: Journalistic Cultures Around the Globe.
Columbia University Press, New York.
[26] Tony Harcup and Deirdre O’neill. 2017. What is news? News values revisited
(again).Journalism studies18, 12 (2017), 1470–1488.
[27] Brian C Hill. 2006. Measuring media market diversity: Concentration, importance,
and pluralism.Fed. Comm. LJ58 (2006), 169.
[28] Corinna Lauerer, Mia Grünewald, Thomas Hanitzsch, Jonila Godole, Rrapo Zguri,
Besmir Godole, Adriana Amado, Maximiliano Bongiovanni, Nicolás Rotelli, Fa-
cundo Luque, et al. 2025. Worlds of Journalism Study Wave 3 (2021-2025) Con-
solidated Dataset [Data set]. (2025). doi:10.5281/zenodo.15280738
[29] Huyen Le, Raven Maragh, Brian Ekdale, Andrew High, Timothy Havens, and
Zubair Shafiq. 2019. Measuring Political Personalization of Google News Search.
InThe World Wide Web Conference (WWW ’19). ACM, 2957–2963. doi:10.1145/
3308558.3313682
[30] Johan Lidberg. 2019. The distortion of the Australian public sphere: Media
ownership concentration in Australia.AQ-Australian Quarterly90, 1 (2019),
12–20.
[31] Mihran Miroyan, Tsung-Han Wu, Logan King, Tianle Li, Jiayi Pan, Xinyan Hu,
Wei-Lin Chiang, Anastasios Angelopoulos, Narges Norouzi, Joseph E Gonzalez,
et al. 2026. Search arena: Analyzing search-augmented llms. InInternational
Conference on Learning Representations, Vol. 2026. 41109–41146.
[32] Eli Noam. 2009.Media ownership and concentration in America. Oxford University
Press.
[33] Eli M Noam. 2016.Who owns the world’s media?: media concentration and
ownership around the world. Oxford University Press.
[34] Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Evangelos P. Markatos,
and Nicolas Kourtellis. 2023. Who Funds Misinformation? A Systematic Analysis
of the Ad-related Profit Routines of Fake News Sites. InProceedings of the ACM
Web Conference 2023 (WWW ’23). ACM, 2765–2776. doi:10.1145/3543507.3583443
[35] Erik Peterson and Johanna Dunaway. 2023. The New News Barons: Invest-
ment Ownership Reduces Newspaper Reporting Capacity.The ANNALS of
the American Academy of Political and Social Science707, 1 (May 2023), 74–89.
doi:10.1177/00027162231211426
[36] Jo Pierson, Aphra Kerr, Stephen Cory Robinson, Rosanna Fanni, Valerie Eveline
Steinkogler, Stefania Milan, and Giulia Zampedri. 2023. Governing Artificial
Intelligence in the Media and Communications Sector.Internet Policy Review12,
1 (2023). doi:10.14763/2023.1.1683
[37] Dominic Ponsford. 2026.Which journalists and news outlets are most cited by
AI answer engines?https://pressgazette.co.uk/news/journalists-cited-ai/ Press
Gazette. Updated May 18, 2026.
[38] Reporters sans frontières. 2026. World Press Freedom Index. https://rsf.org/en/
index
[39] Ronald E. Robertson, David Lazer, and Christo Wilson. 2018. Auditing the
Personalization and Composition of Politically-Related Search Engine Results
Pages. InProceedings of the 2018 World Wide Web Conference (WWW ’18). ACM,
955–965. doi:10.1145/3178876.3186143
[40] Abdur-Rahman Ibrahim Sayyid-Ali, Daanish Uddin Khan, and Naveed Anwar
Bhatti. 2026. Are LLM Web Search Engines Sustainable? A Web-Measurement
Study of Real-Time Fetching. InProceedings of the ACM Web Conference 2026
(WWW ’26). ACM, 2083–2093. doi:10.1145/3774904.3792278
[41] Marco Scalvini. 2023. Making Sense of Responsibility: A Semio-Ethic Perspective
on TikTok’s Algorithmic Pluralism.Social Media + Society9, 2 (2023). doi:10.
1177/20563051231180625
[42] Helle Sjøvaag and Jonas Ohlsson. 2019. Media Ownership and Journal-
ism. InOxford Research Encyclopedia of Communication. doi:10.1093/acrefore/
9780190228613.013.839
[43] Alexander Spangher, Gireeja Ranade, Besmira Nushi, Adam Fourney, and Eric
Horvitz. 2020. Characterizing Search-Engine Traffic to Internet Research Agency
Web Properties. InProceedings of The Web Conference 2020 (WWW ’20). ACM,
2253–2263. doi:10.1145/3366423.3380290
[44] Hendrik Theine, Julia Bartsch, and Mandy Troeger. 2025. Does media ownership
matter for journalistic content? A systematic scoping review of empirical studies.
International Journal of Communication19 (2025), 865–887.
[45] Charlotte Tobitt. 2026. Who’s suing AI and who’s signing: Encyclopedia Bri-
tannica and Merriam-Webster sue OpenAI following Perplexity lawsuit.Press
Gazette(24 March 2026). https://pressgazette.co.uk/platforms/news-publisher-
ai-deals-lawsuits-openai-google/ Updated April 7, 2026.
[46] Josef Trappel and Werner A. Meier. 2022. Soaring media ownership concentration:
Comparing the effects of digitalisation on media pluralism and diversity. (2022).
doi:10.48335/9789188855589-7 Publisher: Nordicom, University of Gothenburg.

Carragher and Carley
[47] Aleksandra Urman, Mykola Makhortykh, and Roberto Ulloa. 2021. Auditing
Source Diversity Bias in Video Search Results Using Virtual Agents. InCompanion
Proceedings of the Web Conference 2021 (WWW ’21 Companion). ACM, 232–236.
doi:10.1145/3442442.3452306
[48] Nikki Usher, Joshua P Darr, Philip M Napoli, and Michael L Miller. 2023. Media
policy for an informed citizenry: Revisiting the information needs of communities
for democracy in crisis.The ANNALS of the American Academy of Political and
Social Science707, 1 (2023), 8–20.
[49] Sanne Vrijenhoek, Gabriel Bénédict, Mateo Gutierrez Granada, Daan Odijk, and
Maarten de Rijke. 2022. RADio—Rank-Aware Divergence Metrics to Measure Nor-
mative Diversity in News Recommendations. InProceedings of the 16th ACM Con-
ference on Recommender Systems. ACM, 208–219. doi:10.1145/3523227.3546780
[50] Sanne Vrijenhoek, Mesut Kaya, Nadia Metoui, Judith Möller, Daan Odijk, and
Natali Helberger. 2021. Recommenders with a Mission: Assessing Diversity
in News Recommendations. InProceedings of the 2021 ACM SIGIR Conference
on Human Information Interaction and Retrieval. ACM, 173–183. doi:10.1145/
3406522.3446019
[51] Hannah Waight, Eddie Yang, Yin Yuan, Solomon Messing, Margaret E Roberts,
Brandon M Stewart, and Joshua A Tucker. 2026. State media control influences
large language models.Nature(2026), 1–9.
[52] Kai-Cheng Yang. 2025. News source citing patterns in ai search systems.arXiv
preprint arXiv:2507.05301(2025).
Validation, continued
United Kingdom.Using the same methodology, we gathered UK
datasets and validated the coverage of UK news outlets on Wikidata
with those that are listed in curated datasets maintained by the UK
Public Interest News Foundation (PINF) [1]. Of the 1,438 Wikidata
UK news domains we discover, 29% are in the PINF dataset (or 482
news outlets). Coverage varies by media type, with digital outlets
best represented: our UK dataset covers 53.5% of outlets which
exist both in Print & Online, 27.2% of online-only outlets, 9.1%
of print-only titles, community radio 3.7%, and local TV 2.9%. In
terms of ownership type, our dataset is biased toward corporate
owned news outlets, covering 54% of corporate titles, and only 9%
of independent outlets, which may partly reflect the large number
of community radio stations PINF lists.
Country Assignment.The country a domain is assigned to matches
the top audience country SimilarWeb reports for 88.0% of 22,212
domains, and is somewhere in that domain’s top five for 93.2%. The
dataset’s country assignments are built from Wikipedia category
trees, ccTLDs and infobox locations. SimilarWeb’s per-country au-
dience shares are read by nothing in that pipeline, so they are a
genuinely held-out test rather than a consistency check. US traffic
is inflated: a large share of measured web traffic originates in the
United States whatever an outlet’s market, so “the top audience
country is the US” is weak evidence of a US outlet. In cases where
the US is marked as the top audience country by SimilarWeb, we
count our country label as a match if it is either the US or the next
highest country by traffic share.
Label Coverage and Inclusion Criteria.Our inclusion criteria filter
out a large number of domains pulled from Wikipedia. As deter-
mined via SimilarWeb traffic estimates, 70.1% of the total traffic
volume received by the news domains in our frame is accounted
for by a domain that carries an ownership label. Across the 77
ranked countries, coverage and measured concentration correlate
at 𝜌=− 0.347( 𝑝= 0.002), suggesting that inclusion criteria do
impact the analysis. Thin coverage biases the index upward, be-
cause unlabeled traffic is dropped from the denominator. However,
changing the inclusion criteria and naming specifications does not
move the concentration indices (see Specification Stability below).
As such, the analyses are not invalidated by reporting results on
a subset of the traffic data observed (i.e. the subset for which we
have ownership labels).
Wikidata State-Sponsored Labels
The state-media classification used in the main text is the State
Media Monitor’s [19]. We also derive state labels from Wikidata,
which readers can reproduce from the released dataset.
Method.A domain enters the pool on any evidence of public
or state ownership: its own Wikidata entity, or an owner entity
reached through the ownership properties (P127, P749, P123, P137),
is typed as a public or state broadcaster; owner keys are propagated
to every domain sharing the owner string; generic public or state
naming patterns on the owner string (e.g., CBC, SRG SSR, TVNZ);
and a small hand list. The pool is then partitioned by precedence
into government non-media (keyed on .gov, .mil or .edu hosts
and official gazettes), state-sponsored (positive evidence of state
or ruling-party direction, optionally moderated by an RSF press-
freedom gate), party press, and public-service as the remainder.
Analysis.Table 6 gives the class counts. The RSF gate is the
consequential choice, and the reason these labels are not used for
any result relating state media to press freedom: a label that reads
RSF cannot be used to test RSF. Without the gate, state-sponsored
loses 70% of its members and public-service grows by 46%.
Table 7 scores the labels against SMM’s hand-compiled census.
They are precise and incomplete: they rarely call an outlet state-
controlled that SMM does not, but they reach under half of what
SMM lists. Dropping the RSF gate costs recall without buying preci-
sion. This is why the main text reads SMM directly and these labels
are reported only here.
Language Subsets
The Ahrefs citation counts are drawn per domain from a corpus
of observed AI answers, with no country or language parameter,
and that corpus is built on a predominantly English keyword base.
The imbalance is visible in the frame: english-facing outlets are
26.8% of domains but take 61.9% of citations, against 40.1% of traffic.
An outlet is english-facing if its Wikipedia infobox names English
as a publication language (available for 41% of the frame), or its
country’s press works substantially in English, or the domain is
an explicit English edition ( en.*, english.*). The country rule
over-includes, so the restriction is a weak upper bound and the
results below are correspondingly conservative.
Table 9 gives both frames. At the outlet level the median coun-
try’s AI ecosystem is+424HHI points more concentrated than its
attention, against+537on the full frame, and 14 of 16 countries
amplify. At the owner level the restriction changes nothing at all:
1.38×on both frames, with 14 of 16 countries amplifying.
Restricting to native-language outlets does not recover a state-
media preference. Repeating the state-media test on non-english-
facing outlets only, state-controlled media are cited below their
traffic share by every system (median ratios 0.08–0.68× across 20
countries), two systems reach 𝑝<. 05uncorrected, and none sur-
vives Benjamini–Hochberg correction across the ten tests (lowest
𝑞=. 094). What does recover a preference is changing the language

Measuring Media Concentration Across 77 Countries and Seven AI Systems
Our measure vs Noam series n𝜌p𝜌SE (Fisher)𝜌SE (bootstrap)
HHI vs newspaper HHI 30+0.407 0.0250.192 0.168
HHI vs newspaper HHI (chapter alternative) 30+0.414 0.0230.192 0.154
HHI vs online-news HHI 20 +0.125 0.600 0.243 0.228
Noam index vs Noam index 24 +0.404 0.050 0.218 0.193
CR1 vs top-company share 30 +0.325 0.080 0.192 0.168
CR4 vs newspaper C4 29+0.465 0.0110.196 0.171
owners≥1% vs N of voices >1% 27+0.408 0.0350.204 0.172
Table 5: Our index against each published Noam series.
Class shipped rebuilt without RSF
state-sponsored 285 85
public-service 305 444
party press 16 77
government non-media 54 54
Table 6: A breakdown of Wikidata-derived labels for state
media control.
Variant precision recall F1
shipped (structural + RSF) 0.969 0.461 0.625
structural only 0.947 0.176 0.298
rebuilt without RSF 0.862 0.123 0.215
Table 7: Wikidata-derived state-sponsored labels against the
SMM labels, on overlapping domains.
of thepromptrather than the language of the outlet (Table 8), which
is what H4 tests and what Waight et al. [51] report.
Owner Layer versus Outlet Layer
On the same 55 countries, the ownership-pressure composite tracks
owner-level concentration (largest-owner share 𝜌=+ 0.359, 𝑝=
0.007) and doesnottrack outlet-level concentration, the HHI over
news outlets computed without using any ownership information
at all (𝜌=+ 0.144, 𝑝= 0.295). Table 10 gives the association under
each way of drawing the owner set.
The preceding checks establish that the index is measured prop-
erly. This establishes that it measures something the outlet-level
alternative does not, against an external report of conditions inside
newsrooms. Entered together against media trust, neither layer
carries an association, which is consistent with the null reported in
the credibility and trust section below.
Specification Stability
Every analytic specification agrees with the primary country rank-
ing at 𝜌≥ 0.940: raw owner names 0.992, first-owner rather than
fractional attribution 0.955, a stricter blocklist 0.973, a news-only
allowlist 0.940, and traffic floors higher still. The single choice that
moves the ranking is declining to filter non-news at all (0.889),
which is the point of the filter: it reorders countries rather than
rescaling them, and the median country HHI barely moves (2,115 to
2,247). Of the 47 countries where we identify a largest owner, only
2 corporate groups top more than one national market. Per-country
estimates are released with the dataset.
External Validation
The comparison in the main text rests on Noam [33]’s four-firm
concentration ratio, the more robust of his two series and the
one that survives every specification we test. Two further results
bound it. The like-for-like online-news comparison is inconclu-
sive ( 𝜌=+ 0.125, 𝑛= 20), and his own two series agree with
each other at only 𝜌=+ 0.149( 𝑛= 20) on the countries where
both exist. Agreement with either is therefore evidence that our
index measures national ownership concentration; agreement with
both would not be available to any measure. On a log scale, our
index and his newspaper-press HHI correlate at Pearson𝑟=+ 0.614
(𝑝=3.0×10 −4). The full set of comparisons is in Table 5.
AI Analysis
The panel is 4,584 news domains across 199 countries. A country
enters the analysis with at least ten labeled domains, rather than
being cut to a fixed top-𝑁 : the owner-count gate already makes mar-
kets comparable, and a fixed cut cost eight ranked countries while
inflating the amplification ratios it was meant to guard. Portals are
excluded, as elsewhere. AI concentration and traffic concentration
are computed over the same outlets, so a difference reflects how
citations spread rather than which outlets were sampled.
Sensitivity.The amplification result holds under all three is-news
filter settings and at every top-𝑁 cut from 10 to 30, though the effect
shrinks as 𝑁 grows — adding smaller outlets adds units that AI
rarely cites, which raises the traffic baseline faster than the citation
index. The association between AI concentration and ownership
concentration strengthens with 𝑁 rather than weakening, so nei-
ther result is an artefact of the cut.
The AI hypothesis family.H1–H3 are corrected together within
each level of analysis. Two tests are deliberately outside the family:
the traffic-versus-ownership correlation, which checks that the data
behave as expected rather than testing a hypothesis, and the trust
tests, which address a separate question.
State and Public-Service Media
Non-commercial ownership is split into four classes rather than
treated as one, because a public-service broadcaster, a state-sponsored
outlet, a government non-media site and a party organ are different

Carragher and Carley
Country Language RSF state traffic share citations state state O/E commercial O/E
RU Russian 25 0.287 1037 233 0.78 0.64
CN Chinese 15 0.168 689 158 1.37 0.59
VN Vietnamese 20 0.007 625 16 3.46 0.57
BR Portuguese 64 0.000 258 0 0.00 0.62
TR Turkish 29 0.013 74 2 2.13 0.90
RO Romanian 66 0.002 69 4 25.64 0.38
CZ Czech 84 0.035 55 11 5.69 0.17
HU Hungarian 63 0.035 55 0 0.00 1.51
UA Ukrainian 64 0.000 45 1 87.43 0.00
IR Persian 16 0.009 28 1 3.80 1.14
pooled – – – 2961 – 1.01 0.61
Table 8: Do AI systems favour state media when asked in the country’s own language? Each row is one country: citations to its
own news outlets in answers to prompts in its national language, from the Search Arena dataset. ‘state O/E’ is the observed
number of citations to state-captured outlets over the number their share of the country’s news traffic predicts; ‘commercial
O/E’ is the same for a bloc of commercial outlets matched to the state bloc’s traffic share, which controls for AI under-citing
large outlets in general. RSF is the Reporters Without Borders press-freedom score.
Level Frame𝑛median amplification𝑝
outlet full 70+537HHI (1.68×)8.3×10 −9
english-facing 16+424HHI (1.51×)0.003
owner full 70+713HHI (1.38×)1.4×10 −6
english-facing 16+689HHI (1.38×)0.016
Table 9: AI citation concentration against attention concen-
tration, on the full frame and on english-facing outlets only.
Each figure is the mean of the five per-model HHIs.
owner set largest-owner share vs
pressure
n
full dataset (primary)+0.359(p = 0.007) 55
top-20 owners per country+0.350(p = 0.009) 55
top-10 owners per country+0.340(p = 0.011) 55
owner traffic≥5M or≥3 outlets +0.293 (p = 0.087) 35
owner traffic≥10M or≥3 outlets +0.220 (p = 0.261) 28
outlet-level fragmentation (any vari-
ant)
+0.144 (p = 0.295) 55
Table 10: The pressure association under each way of drawing
the owner set. Outlet-level fragmentation, which uses no
owner label, is the contrast.
objects and only the first is a plurality institution in the regulatory
sense.
On the Ahrefs panel, AI systems do not preferentially cite state-
controlled or public-service outlets, at either level of analysis and
under the citation-traffic elasticity control, and treating the state
as a single owner does not concentrate citations more than traffic.
Those nulls are read as a size effect rather than a state effect, because
a size-matched commercial bloc ismoresuppressed than the state
bloc: what looks like under-citation of state media is under-citation
of outlets of that size. They are also underpowered, and the native-
language result reported in the main text shows they are a property
of an English-prompted instrument.
Credibility and Trust
Two further questions were asked of these data and are reported
here because the analyses exist and should not be repeated. Neither
supports an argument in the paper.
Credibility and consumption.Concentration is positively asso-
ciated with the share of a country’s news consumption going to
outlets of lowor mixedcredibility ( 𝜌=+ 0.356by outlet count,
+0.386by visits; 𝑝BH = 0.006and0 .004, 𝑛= 77), and that asso-
ciation is robust to weighting and to frame. It does not survive
a control for GDP per capita: correcting for the 24 tests run in
each frame,noneof the GDP-controlled partials is significant, the
strongest being+0.243( 𝑝BH = 0.173). Richer countries are both less
concentrated and consume less low-credibility news, and that is
enough to account for the raw association. There is no association at
all for clearly low-credibility outlets as distinct from low-or-mixed
(𝜌=+0.017,𝑝=0.883).
Media trust.We tested whether concentration relates to public
trust in news. It is not supported: there is no association across
the full 47-country panel (𝜌=− 0.061, 𝑝= 0.682), and the positive
association inside the canonical Hallin and Mancini eighteen is
specification-dependent and not significant on the specification this
paper adopts. It survives neither development controls, nor four
constructions of the public-ownership set, nor a between/within
decomposition by media system.
Both are limited by trust-survey coverage (48 countries) and by
a single wave, and both need better-identified designs than we can
bring to them. Concentration in these data is consequential for the
people producing the news and, on this evidence, not measurably
so for what audiences consume or believe.
