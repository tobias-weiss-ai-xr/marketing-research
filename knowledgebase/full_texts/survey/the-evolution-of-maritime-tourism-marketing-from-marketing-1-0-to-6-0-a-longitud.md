---
title: 'The Evolution of Maritime Tourism Marketing from Marketing 1.0 to 6.0: A Longitudinal Text-Mining
  and Structural Topic Model Analysis'
url: https://doi.org/10.22429/euc2026.jmr.imlc.09
category: survey
subcategory: framework
date: 2026-07
venue: Journal of Maritime Research
authors:
- Mohammed Ali Sharafuddin
source: openalex-oa
pdf_url: https://www.jmr.unican.es/jmr/article/download/1623/1221
pages: 7
chars: 33464
fetched_at: '2026-11-08T19:55:13+00:00'
kb_version: 1
---

# The Evolution of Maritime Tourism Marketing from Marketing 1.0 to 6.0: A Longitudinal Text-Mining and Structural Topic Model Analysis

SPECIAL ISSUE (2026) pp 72–78
ISSN: 1697-4840, www.jmr .unican.es
JOURNAL OF MARITIME RESEARCH
The Evolution of Maritime Tourism Marketing from Marketing 1.0 to 6.0:
A Longitudinal Text-Mining and Structural Topic Model Analysis
Mohammed Ali Sharafuddin1,∗
ARTICLE INFO ABSTRACT
Special Issue:
1st International Maritime and
Logistics Conference;
February 10-11, 2026.
National University of Science &
Technology (NU), Oman
Article history:
Received 15 Feb 2026;
in revised from 24 Feb 2026;
accepted 05 Jun 2026.
Keywords:
Maritime Tourism, Marketing
Evolution, Structural Topic Model,
Bibliometrics, Digital Marketing..
Maritime tourism is among the fastest-growing segments of the blue economy, yet the evolution of
its marketing philosophy has not been examined systematically. This study applies Kotler, Kartajaya
and Setiawan’s Marketing 1.0 to 6.0 framework to a corpus of 17,335 scholarly works on maritime
tourism retrieved from OpenAlex (2000 to 2024). A theory-derived dictionary was operationalised
in the quanteda R package, and a structural topic model (STM, K=8) with publication year as a
prevalence covariate was estimated to recover latent thematic trajectories. The Values era (Marketing
3.0) dominates the corpus throughout, holding 26 to 29 per cent of era-specific vocabulary and reflecting
the sector’s dependence on heritage, authenticity and coastal community. The Consumer era (2.0) rose
from 19.2 to 23.0 per cent and the Digital era (4.0) more than doubled from 8.1 to 17.8 per cent. The
Technology era (5.0) reached only 4.4 per cent and the Immersive era (6.0) just 2.0 per cent by 2024, a
structural lag of roughly one marketing generation behind the broader hospitality literature. The findings
define an urgent eras 5.0 and 6.0 agenda for destination managers, cruise operators and researchers.
©SEECMAR|All rights reserved
1. Introduction.
Maritime tourism covers cruise tourism, coastal leisure travel,
nautical recreation and marine heritage experiences, and to-
gether these activities form one of the fastest-growing parts of
the global blue economy. The European Commission’s Blue
Economy Report put coastal and maritime tourism at roughly
183 billion euros in gross value added and more than 3.2 mil-
lion jobs across the EU (European Commission, 2023), and in-
ternational cruise passenger volumes passed 31 million in 2023,
a full recovery from the pandemic contraction (Cruise Lines In-
ternational Association, 2024). For all that economic weight,
scholarship on how maritime tourism organisations conceptu-
alise marketing, and on how that conceptualisation has changed
over time, remains fragmented.
1Qasim Ibrahim School of Business, Villa College, Malé, Maldives.
∗Corresponding author: Mohammed Ali Sharafuddin. E-mail address:
mohammed.ali@villacollege.edu.mv.
The thematic development of blue tourism research has drawn
growing bibliometric attention; Sharafuddin and Madhavan (2024)
analysed 986 Scopus-indexed articles on coastal, marine and
maritime tourism published between 2000 and 2019 and iden-
tified four developmental stages through a hybrid scientomet-
ric and systematic review. They showed that the field diver-
sified sharply after about 2012, moving from early dominance
by sustainability, community development and heritage authen-
ticity toward digital platforms, visitor experience quality and
blue economy governance. Their framework, however, was de-
scriptive: it mapped what the field studied without asking what
marketing philosophy governed how those topics were framed.
That gap motivates the present study.
The Marketing 1.0 to 6.0 framework, set out by Kotler,
Kartajaya and Setiawan across four books (Kotler et al., 2010,
2017, 2021, 2024), offers a normative periodisation of mar-
keting practice. The eras move from a product-centred logic,
through consumer satisfaction and loyalty, societal values and

M.A. Sharafuddin./Journal of Maritime Research SPECIAL ISSUE (2026) 72–7873
authenticity, digital channel integration, technology-enabled per-
sonalisation, and finally an emergent phygital and immersive
paradigm built on co-creation. Each transition marks a shift in
the primary unit of value, the dominant mode of consumer en-
gagement, and the capabilities a firm needs to compete. The
framework has been used to trace marketing evolution in hos-
pitality (Romero Montero et al., 2023) and experiential tourism
(Aarabe et al., 2026), but maritime tourism as a coherent schol-
arly field has not been examined through it. Given the sector’s
distinctive features, its capital-intensive physical infrastructure,
its deep heritage narratives, and a stakeholder ecology span-
ning ports, fishing communities, conservation bodies and cruise
lines, there is no reason to assume its marketing evolution mir-
rors land-based hospitality.
This paper addresses that gap. We analyse 17,335 works on
maritime tourism from OpenAlex (2000 to 2024) with two com-
plementary methods. First, we operationalise the Kotler frame-
work as a quanteda dictionary and compute the share of era-
specific vocabulary per document, aggregated by year. Second,
we estimate a structural topic model (Roberts et al., 2019) with
publication year as a prevalence covariate, recovering eight la-
tent themes and tracking how their prevalence shifts. Three
findings emerge. The Values era (3.0) is persistently dominant,
at 26 to 29 per cent of era vocabulary, which we read as con-
stitutive of maritime tourism rather than a passing trend. The
Consumer era (2.0) and Digital era (4.0) grow steadily. The
Technology era (5.0) and Immersive era (6.0) together account
for only 6.4 per cent of era vocabulary in 2024, a lag of about
one marketing generation behind the broader hospitality litera-
ture.
The contribution is threefold. Empirically, we extend the
scientometric mapping of Sharafuddin and Madhavan (2024)
to a far larger corpus (17,335 versus 986 works) over a longer
window (to 2024), and shift the analytical frame from what the
field studies to what marketing logic it adopts. Methodologi-
cally, we set out a fully open-source and replicable pipeline us-
ing the OpenAlex API, quanteda and stm. Practically, we frame
the eras 5.0 and 6.0 deficit as a concrete agenda and offer differ-
entiated recommendations for destination management organi-
sations, cruise operators and policy makers. The paper reviews
the framework and literature, describes the data and methods,
presents results, discusses implications, and concludes.
2. Literature Review.
2.1. The Marketing 1.0 to 6.0 Framework.
The Marketing 1.0 to 6.0 periodisation has been adopted
widely as a device for reviewing marketing evolution. Each era
corresponds to a dominant logic of value creation and a partic-
ular way of engaging consumers, and the progression is neither
strictly linear nor synchronised across industries. Sectors have
absorbed successive eras at different rates, and that heterogene-
ity makes maritime tourism a useful comparative case.
In theProduct era(1.0), the product is the primary unit of
value, and firms compete on functional attributes, price and dis-
tribution reach (Kotler et al., 2010). In maritime tourism this
shows up in work that foregrounds infrastructure: ship specifi-
cations, port facilities, route networks and timetables, treating
marketing largely as a problem of communicating the quality
of physical assets. TheConsumer era(2.0) shifted attention to
the individual consumer, bringing satisfaction, loyalty, service
quality and experiential value into the core vocabulary. In mar-
itime tourism this paradigm is most visible in the large body of
research on cruise passenger satisfaction, onboard service qual-
ity and revisit intention, and in the spread of structural equa-
tion modelling with SERVQUAL-derived instruments from the
1990s onward.
TheV alues era(3.0) reaches beyond the transactional to-
ward social purpose, cultural meaning and community (Kotler
et al., 2010). In maritime and coastal tourism it appears in re-
search on heritage and authenticity, community-based coastal
development, blue economy governance and the sustainability
discourse that intensified after the adoption of Sustainable De-
velopment Goal 14. That Values-era vocabulary holds 26 to
29 per cent of era-specific terms throughout 2000 to 2024, nei-
ther rising nor falling sharply, suggests this paradigm is em-
bedded in the field rather than fashionable. TheDigital era
(4.0) follows the rise of social media, user-generated content
and online booking, and reframes marketing as a continuous,
multi-directional conversation across channels (Kotler et al.,
2017). In maritime tourism it is represented by research on on-
line destination image, review dynamics, cruise-line social me-
dia and influencer promotion. Sharafuddin et al. (2024) show,
in a coastal tourism setting, that digital marketing effectiveness
shapes perceived service quality and sustainability quality, and
that both mediate satisfaction and behavioural intention; the
appearance of a sustainability-quality pathway alongside ser-
vice quality suggests era 4.0 marketing is already being judged
against criteria more typical of eras 5.0 and 6.0.
TheTechnology era(5.0) is defined by artificial intelligence,
machine learning, the Internet of Things and big-data analyt-
ics enabling personalised experiences at scale (Kotler et al.,
2021). In maritime tourism, engagement with these tools has
been led by the engineering and logistics literature, automatic
identification system analytics, smart-port management, algo-
rithmic demand forecasting, rather than by marketing scholars,
and consumer-facing personalisation research is scarce. The
Immersive era(6.0) describes a phygital paradigm fusing phys-
ical and digital experience through augmented and virtual real-
ity, the metaverse and gamification (Kotler et al., 2024). Appli-
cations in maritime tourism remain largely conceptual: study
of phygital shore excursions, virtual cruise previews or gami-
fied port experiences is, as yet, sparse. The framework there-
fore describes a shift in the locus of value from the product,
to consumer experience, to social meaning, to digital interac-
tion, to data-driven personalisation, and finally to immersive
co-creation, a progression not previously measured longitudi-
nally for maritime tourism.
2.2. Maritime Tourism Marketing.
The closest precedent to this study is the scientometric anal-
ysis of blue tourism by Sharafuddin and Madhavan (2024), which
mapped 986 Scopus articles across 2000 to 2019 and found four

M.A. Sharafuddin./Journal of Maritime Research SPECIAL ISSUE (2026) 72–7874
developmental stages: a thin preliminary phase, two transversal
stages of broadening, and a growth stage from 2016 in which
smart destination management and blue economy governance
emerged as new fronts. We build on that work in three ways:
we extend the window to 2024, capturing the post-pandemic
acceleration of digital and technology adoption; we expand the
corpus from 986 Scopus articles to 17,335 OpenAlex works,
taking in open-access and non-English literature; and we im-
pose a normative frame, the Kotler periodisation, to read the
marketing philosophy the field implicitly endorses.
The maritime and coastal tourism marketing literature falls
into five streams. The most extensive is consumer satisfaction
and loyalty (era 2.0), examining cruise passenger satisfaction,
onboard service quality and destination loyalty, typically with
SEM and SERVQUAL. Sharafuddin et al. (2022) extend this
tradition with an integrated model of island destination service
quality that introduces co-creation of destination e-image as a
mediator, positioning the consumer as an active participant in
constructing the destination’s digital identity and so bridging
eras 2.0 and 4.0. A second stream, community-based devel-
opment and geotourism (era 3.0), is strong in the Southeast
Asian context and frames rural coastal communities, geoparks
and marine ecotourism through sustainable development and
empowerment. A third, also era 3.0, addresses cultural her-
itage and maritime identity, including historic port cities, fish-
ing heritage and museum interpretation in destination branding;
this stream has declined in relative prevalence since about 2010
in our model, possibly as the sustainability discourse absorbed
heritage into a broader values vocabulary.
A fourth stream, blue economy and coastal governance, cov-
ers fisheries, climate adaptation, marine protected areas and
the institutional governance of coastal tourism resources. It
is philosophically aligned with era 3.0 but operates at the pol-
icy level rather than at consumer engagement, and its vocabu-
lary sits at the boundary of tourism, environmental science and
political economy. The fifth and fastest-growing stream, dig-
ital innovation and smart technology (eras 4.0 and 5.0), spans
maritime digitalisation reviews, algorithmic demand forecast-
ing and emerging-technology surveys; it is the most steeply
positive topic in our model. What is notably absent is any estab-
lished literature on Marketing 6.0 in maritime tourism: era 6.0
vocabulary accounts for only 2.0 per cent of era-specific terms
in the 2024 corpus, confirming that phygital and immersive ex-
perience design remains conceptually emergent rather than em-
pirically studied. This lag is the central puzzle the present study
documents and explains.
3. Methods.
3.1. Data Source.
Bibliometric data were retrieved from OpenAlex (Priem et al.,
2022) using the openalexR package in R (Aria, 2023). Ope-
nAlex was preferred over Scopus or Web of Science for three
reasons: it is fully open-access and requires no subscription; it
indexes more than 250 million works, giving broader coverage
of open-access and non-English literature; and it exposes struc-
tured metadata, titles, abstracts, authorship, venue and citations,
through a documented API. openalexR reconstructs abstracts
from the OpenAlex inverted index, giving effectively complete
abstract coverage without additional scraping.
The search targeted works containing at least one of “mar-
itime tourism,” “coastal tourism,” “cruise tourism,” “marine tour-
ism,” “port tourism,” “nautical tourism,” “island tourism” or
“beach tourism” in the title or abstract. We deliberately did not
intersect the query with “marketing”: restricting to works that
self-identify as marketing studies would exclude a large body
of research that implicitly adopts marketing logic, for example
studies of service quality, visitor experience or destination im-
age. Works were limited to journal articles published between
1990 and 2024. After deduplication by OpenAlex identifier the
corpus comprised 17,335 documents in more than 800 jour-
nals, withSustainability(n=1,185),GeoJournal of Tourism
and Geosites(n=171),Frontiers in Marine Science(n=143)
andIEEE Access(n=134) most frequent. The open-access
share was 89.8 per cent. The corpus retains some non-English
abstracts; quanteda’s lowercasing and stopword removal handle
but do not eliminate them, and an English-only check is flagged
as a robustness extension.
3.2. Marketing Era Dictionary.
A six-era dictionary was built from the definitional vocab-
ulary in Kotler, Kartajaya and Setiawan (Kotler et al., 2010,
2017, 2021) and adapted to maritime tourism. Each era is a
closed list of unigrams and bigrams capturing its core logic.
The dictionary was applied in quanteda (Benoit et al., 2018) us-
ingdfm_lookup()on a document-feature matrix pre-processed
by lowercasing, removing punctuation, symbols and English
stopwords, and suppressing a set of ubiquitous domain terms
(tourism, tourist, coastal, maritime, marine, destination) that
would otherwise dilute the signal. The era score for a docu-
ment is the share of dictionary-matched tokens among its non-
stopword tokens, which standardises for length, and scores are
averaged by year and decade.
In summary, the Product era (1.0) is captured by infras-
tructure terms (facility, fleet, harbour, berth, terminal, route,
timetable); the Consumer era (2.0) by experience and relation-
ship terms (satisfaction, loyalty, expectation, perception, mo-
tivation, attitude); the Values era (3.0) by ethics and commu-
nity terms (authenticity, heritage, identity, social responsibil-
ity, stakeholder, wellbeing, co-creation); the Digital era (4.0) by
platform terms (social media, mobile, e-tourism, user-generated
content, e-commerce, ICT); the Technology era (5.0) by data
and AI terms (analytics, personalisation, machine learning, arti-
ficial intelligence, algorithm, IoT, blockchain, chatbot); and the
Immersive era (6.0) by phygital terms (immersive, metaverse,
augmented reality, virtual reality, gamification, co-design, em-
bodied, multisensory). The full term lists are in the replication
repository.
3.3. Structural Topic Model
To recover the latent thematic structure and trace how themes
shift over time we estimated a structural topic model (Roberts
et al., 2019) with the stm package. The STM extends latent

M.A. Sharafuddin./Journal of Maritime Research SPECIAL ISSUE (2026) 72–7875
Dirichlet allocation by letting document metadata inform topic
prevalence, and we specified publication year as a linear preva-
lence covariate; an approximately linear trend in the dictio-
nary proportions made a spline unnecessary. The matrix was
trimmed to terms appearing at least five times overall and in at
least three documents, giving a 17,335 by 18,738 matrix, and
was converted to STM input with quanteda’sconvert()pre-
serving document metadata. The number of topics K was set to
8 after inspecting semantic coherence and held-out likelihood
across K in {6, 8, 10}. Estimation used spectral initialisation
with seed 2024 and converged at iteration 93. Year trends were
estimated withestimateEffect()using global uncertainty,
giving a year coefficient and standard error per topic.
3.4. V alidity Checks
Three checks were run. Face validity was assessed by in-
specting the most-cited works per dominant-era category, which
showed that a few high-citation works from outside tourism
enter each era list through shared vocabulary, so the era lists
need manual curation. Robustness to K was assessed by re-
estimating at K=6 and K=10: the main trends were stable,
with consumer-behaviour topics positive and significant at K=
6 (β= +0.007) and K=10 (β= +0.005), digital topics positive
at both, and heritage and product topics negative at all three
values. Temporal face validity was checked by comparing the
dictionary trajectories against known milestones, the rise of so-
cial media research after 2008 and of blockchain applications
after 2017, both clearly visible in the era 4.0 and 5.0 series.
4. Results
4.1. Corpus Description
The corpus spans 1990 to 2024, with only 244 works (1.4
per cent) before 2000, reflecting the youth of the field. Annual
output grew from 79 works in 2000 to 598 in 2015 and peaked
at 2,140 in 2023; the lower 2024 figure is an indexing artefact,
since OpenAlex had not yet captured all 2024 work at retrieval.
As Figure 1 shows, the 2020s already hold the largest decade-
level share (8,809 works), ahead of the 2010s (6,796), with the
2000s contributing 1,486 and the 1990s 174. The open-access
share is 89.8 per cent.
The journal profile is itself a finding. The prominence of
SustainabilityandFrontiers in Marine Sciencereflects the cor-
pus’s Values-era orientation, whileIEEE Accesssignals a grow-
ing engineering-technology stream tied to eras 5.0 and 6.0. The
dominant-era distribution confirms this: of the 17,265 docu-
ments with an identifiable dominant era, 4,796 (27.8 per cent)
fall under the Values era (3.0), 4,330 (25.1 per cent) under the
Consumer era (2.0), 2,761 (16.0 per cent) under the Product
era (1.0) and 1,843 (10.7 per cent) under the Digital era (4.0).
Technology-era documents number only 403 (2.3 per cent) and
Immersive-era documents 128 (0.7 per cent).
  174
1,486
6,796
8,809
0
2500
5000
7500
10000
1990s 2000s 2010s 2020s
Number of works
Figure 1:Maritime tourism works by decade, OpenAlex corpus.
Source: Authors.
4.2. Marketing Era Prevalence over Time
The dictionary analysis shows a coherent pattern of evo-
lution (Figure 2). The Values era (3.0) is dominant in every
year from 2000 to 2024, holding 26 to 29 per cent through-
out. This stability is itself substantive: unlike the other eras the
Values paradigm neither grows nor declines but holds a struc-
turally elevated share, which suggests it is constitutive of mar-
itime tourism discourse. The Consumer era (2.0) rose from 19.2
per cent in 2000 to 23.0 per cent in 2024, most of the growth af-
ter 2010 and consistent with the spread of SEM-based satisfac-
tion research. The Digital era (4.0) shows the sharpest propor-
tional rise, more than doubling from 8.1 to 17.8 per cent, with
acceleration after 2015 as social media and online reputation
management matured as research priorities. The Technology
era (5.0) grew from effectively zero to 4.4 per cent, with visi-
ble momentum after 2018, and the Immersive era (6.0) reached
only 2.0 per cent, growth beginning around 2020. Both confirm
that these paradigms are emergent rather than established in the
field.
4.3. Topic Analysis
Table 1 summarises the eight STM topics, their top FREX
words, the marketing era to which each maps, and their year co-
efficients; Figure 3 orders the topics by that coefficient. Topic 8
(Digital Innovation and Sustainability) has the steepest positive
year trend, followed by Topic 2 (Consumer Behaviour). Topics
4 (Cultural Heritage) and 3 (Market Economics) decline most.
The pattern matches a field-level shift away from static product
and heritage framings toward consumer engagement and digital
innovation.
Topic 7 warrants a note. Its top FREX words include non-
English tokens (de, el) and marine-biology terms (whale, bal-
last, invasive), so the cluster captures a mixture of non-English
documents and ecological science rather than a coherent mar-
keting stream. It should be read as a corpus-quality artefact,
and an English-only re-run is an appropriate extension. The
dominant-era counts reinforce the picture: Values-era docu-
ments lead (4,796), then Consumer (4,330) and Product (2,761),
with Digital (1,843) growing and Technology (403) and Immer-
sive (128) still a small minority.

M.A. Sharafuddin./Journal of Maritime Research SPECIAL ISSUE (2026) 72–7876
19.2
27.0
8.1
0.2 0.0
23.0
27.0
17.8
4.4
2.0
0
10
20
30
2.0 Consumer 3.0 Values 4.0 Digital 5.0 Technology 6.0 Immersive
Era vocabulary share (%)
2000 2024
Figure 2:Marketing-era vocabulary share in the maritime tourism corpus, 2000 versus 2024. The Values era (3.0) holds a stable 26 to 29 per
cent across the period and is shown at its representative level.
Source: Authors.
T4 Cultural heritage
T3 Market economics
T7 Marine ecology (mixed)
T5 Blue economy
T6 Smart technology
T1 Community/geotourism
T2 Consumer behaviour
T8 Digital innovation
−0.004 0.000 0.004
Y ear prevalence coefficient (per year)
Declining Increasing
Figure 3:STM topic prevalence trends over time (year coefficient per
topic).
Source: Authors.
4.4. Synthesis
The two analyses converge on three conclusions. First, mar-
itime tourism scholarship is structurally anchored in Marketing
3.0 values-era thinking, which neither the dictionary propor-
tions nor the topic trajectories contradict. Second, the Con-
sumer and Digital eras (2.0 and 4.0) are growing robustly, so
the field is actively assimilating these paradigms rather than
paying them lip service. Third, the Technology and Immersive
eras (5.0 and 6.0) together account for only 6.4 per cent of era
vocabulary in 2024, well below what tracking the broader hos-
pitality literature would imply (Romero Montero et al., 2023).
5. Discussion
5.1. Why Maritime Tourism Lags in Eras 5.0 and 6.0
Capital intensity offers the most structural explanation. Cruise
ships and port infrastructure run on 20 to 30-year investment
cycles, and marketing innovation in asset-heavy sectors tracks
technology adoption more slowly than in service-light ones, be-
cause the physical product cannot be reconfigured quickly. Re-
searchers study what practitioners do, and practitioners are con-
strained by assets that predate the era 5.0 paradigm. The reg-
ulatory environment reinforces this conservatism: safety reg-
ulation, port-authority protocols and customs and immigration
requirements limit the room for the kind of experiential innova-
tion era 6.0 envisages. Audience demographics add a third fac-
tor, since cruise tourism has historically drawn an older traveller
profile whose demand for immersive and metaverse experiences
may be weaker than in urban experiential hospitality, and weak
demand signals leave marketing scholars less to study. A fourth,
disciplinary explanation is that maritime tourism researchers
are concentrated in nautical science, marine geography and en-
vironmental management, where the priorities lean toward re-
source management and sustainability governance rather than
marketing philosophy.
5.2. Why the V alues Era Is Persistently Dominant
The persistence of era 3.0 vocabulary is the most distinc-
tive feature of the corpus. Unlike land-based hospitality, where
the values era was a time-bounded shift in the 2000s, maritime
tourism appears to have made values-era language a permanent
feature of its discourse. Three overlapping reasons are plau-
sible. Maritime and coastal settings are inherently meaning-
laden: the sea, fishing communities, historic ports and marine

M.A. Sharafuddin./Journal of Maritime Research SPECIAL ISSUE (2026) 72–7877
Table 1: Structural topic model: topics, top FREX words, assigned marketing era and year coefficient.
Topic Label Top FREX words Eraβ(year)
1 Community-based and geotourism ecotourism, regency, geotourism, rural, vil-
lage
3.0 Values+0.0018*
2 Consumer behaviour and satisfaction satisfaction, intention, loyalty, revisit, per-
ceived
2.0 Consumer+0.0061*
3 Market economics and demand halal, exports, sales, fdi, pandemic 1.0 Product−0.0036*
4 Cultural heritage and identity film, museums, identities, archaeological,
colonial
3.0 Values−0.0058*
5 Blue economy and coastal governance adaptation, livelihoods, fishers, blue, gover-
nance
3.0 Values−0.0033*
6 Smart technology and maritime logistics algorithm, machine, iot, ais, containers 5.0 Technology+0.0015*
7 Marine ecology (non-English) whale, invasive, ballast, de, el Mixed−0.0036*
8 Digital innovation and sustainability bibliometric, digital, blockchain, circular,
systematic
4.0 Digital+0.0069*
*p<0.05 for the year coefficient.
Source: Authors.
heritage carry cultural weight that airport and business hotels
do not, so marketing here has always had to engage authentic-
ity, heritage and community, the very resources the sector sells.
The blue economy policy discourse reinforces this, as SDG 14
and the EU blue economy strategy have generated a large insti-
tutional literature on sustainability governance that shares era
3.0 vocabulary. And the community-based tourism tradition,
strong in the Global South coastal literature, deploys values-
era language as a normative development frame and has grown
steadily over the period.
5.3. Implications for Practitioners
Destination management organisations in port cities face a
distinctive opportunity: the values proposition is already strong,
so what is needed is a digital and technology layer rather than
a wholesale shift. Investing in AI-driven personalisation of her-
itage experiences (era 5.0) is likely to be more effective than try-
ing to leap to phygital immersion (era 6.0), for which the con-
sumer demand infrastructure does not yet exist at scale. Cruise
operators are better placed to experiment with era 6.0 given
their captive passenger environment and existing onboard enter-
tainment technology; for them the move from loyalty-programme
marketing (era 2.0) toward predictive personalisation (era 5.0)
is already under way and is the most urgent near-term agenda.
For heritage ports and historic coastal destinations the impli-
cation is more nuanced: the decline in cultural-heritage schol-
arship (Topic 4,β=−0.0058) suggests the traditional heritage
frame is losing ground even within a values-dominated corpus,
so these destinations may need to reframe heritage as a platform
for digital and experiential innovation rather than as a static as-
set.
5.4. Limitations
Four limitations apply. OpenAlex’s coverage of older jour-
nals is uneven, so the pre-2000 series and the era 1.0 and 2.0
estimates are lower bounds on their true historical prevalence.
The dictionary captures co-occurrence of era vocabulary, not
adoption of marketing practice: a high era 4.0 share means dig-
ital phenomena are central to the research question, not that
the organisation studied has gone digital. Non-English content
introduces lexical noise only partly controlled by the current
pipeline, as Topic 7 shows. And a single search strategy risks
omitting work that discusses maritime tourism marketing under
other terminology. Each points to a clear extension: English-
language filtering, an expert-validated dictionary, and a cross-
sectoral comparison with land-based hospitality.
6. Conclusion
This study mapped the evolution of marketing philosophy in
maritime tourism scholarship using the Kotler 1.0 to 6.0 frame-
work. Drawing on 17,335 OpenAlex works from 2000 to 2024,
and combining a theory-derived dictionary with a structural topic
model, we established three findings. The Values era (3.0) dom-
inates structurally and persistently, reflecting the sector’s re-
liance on heritage, authenticity and coastal community; unlike
in land-based hospitality this paradigm has not been displaced
but absorbed into the field’s foundational vocabulary. The Con-
sumer era (2.0) and Digital era (4.0) are growing robustly, and
the rise of digital vocabulary from 8.1 to 17.8 per cent is the
single most dramatic shift in the corpus. The Technology era
(5.0) and Immersive era (6.0) remain structurally underdevel-
oped, together at 6.4 per cent in 2024, a lag of about one market-
ing generation behind the broader hospitality literature, driven
by capital intensity, regulation, demographics and disciplinary
positioning.
These findings extend the scientometric mapping of Shara-
fuddin and Madhavan (2024) by imposing a normative market-
ing frame on a larger and longer corpus, and they give destina-
tion managers and researchers a data-grounded picture of where
the field stands relative to where the marketing paradigm has
arrived. The replication pipeline, built entirely in open-source
tools using the OpenAlex API, quanteda and stm, accompanies
the article. Future work should add English-language filtering,
an expert-validated dictionary expansion, and a cross-sectoral
comparison that places maritime tourism’s marketing evolution
in explicit relation to land-based hospitality and coastal recre-
ation scholarship.

M.A. Sharafuddin./Journal of Maritime Research SPECIAL ISSUE (2026) 72–7878
Acknowledgements
The author thanks colleagues who commented on the dic-
tionary design. The study used only open data and open-source
software.
References
Aarabe, M., Bouizgar, M., Ben Khizzou, N., Alla, L., Benjelloun, A., 2026.
Experiential marketing in tourism: a systematic review of paradigms, mech-
anisms and experiential outcomes. Cogent Business & Management.
Aria, M., 2023. openalexR: Getting Bibliographic Records from OpenAlex. R
package.
Benoit, K., Watanabe, K., Wang, H., Nulty, P., Obeng, A., Müller, S., Matsuo,
A., 2018. quanteda: an R package for the quantitative analysis of textual
data. Journal of Open Source Software 3 (30), 774.
Cruise Lines International Association, 2024. State of the Cruise Industry Re-
port 2024. CLIA.
European Commission, 2023. The EU Blue Economy Report 2023. Publica-
tions Office of the European Union.
Kotler, P., Kartajaya, H., Setiawan, I., 2010. Marketing 3.0: From Products to
Customers to the Human Spirit. Wiley.
Kotler, P., Kartajaya, H., Setiawan, I., 2017. Marketing 4.0: Moving from Tra-
ditional to Digital. Wiley.
Kotler, P., Kartajaya, H., Setiawan, I., 2021. Marketing 5.0: Technology for
Humanity. Wiley.
Kotler, P., Kartajaya, H., Setiawan, I., 2024. Marketing 6.0: The Future Is Im-
mersive. Wiley.
Priem, J., Piwowar, H., Orr, R., 2022. Openalex: a fully-open index of
scholarly works, authors, venues, institutions, and concepts. arXiv preprint
arXiv:2205.01833.
Roberts, M. E., Stewart, B. M., Tingley, D., 2019. stm: an R package for struc-
tural topic models. Journal of Statistical Software 91 (2), 1–40.
Romero Montero, A., Cely Álvarez, A., Sellers Rubio, R., 2023. Inbound mar-
keting in the hospitality industry: a systematic review in the last 12 years.
Enlightening Tourism: A Pathmaking Journal 13 (1), 86–125.
Sharafuddin, M. A., Madhavan, M., 2024. Thematic evolution of blue tourism:
a scientometric analysis and systematic review. Global Business Review
25 (2), 533–554.
Sharafuddin, M. A., Madhavan, M., Wangtueai, S., 2022. Assessing island des-
tination service quality: an integrated model through co-creation of destina-
tion e-image. Global Business Review.
Sharafuddin, M. A., Madhavan, M., Wangtueai, S., 2024. Assessing the ef-
fectiveness of digital marketing in enhancing tourist experiences and sat-
isfaction: a study of Thailand’s tourism services. Administrative Sciences
14 (11), 273.
