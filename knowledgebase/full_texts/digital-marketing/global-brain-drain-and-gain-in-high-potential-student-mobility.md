---
title: Global brain drain and gain in high-potential student mobility
url: https://arxiv.org/abs/2604.16375
category: digital-marketing
subcategory: empirical
date: 2026-03
venue: ''
authors:
- Tabia Tanzin Pramaa
- Christopher M. Danfortha
- Peter Sheridan Dodds
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.16375
pages: 18
chars: 67967
fetched_at: '2026-11-08T13:06:46+00:00'
kb_version: 1
---

# Global brain drain and gain in high-potential student mobility

Global brain drain and gain in high-potential student mobility
Tabia Tanzin Prama, 1,∗ Christopher M. Danforth, 1, 2,† and Peter Sheridan Dodds 1, 3, 4,‡
1Computational Story Lab, Vermont Complex Systems Institute,
Vermont Advanced Computing Center, University of Vermont, Burlington, VT 05405, US.
2Department of Mathematics and Statistics, Burlington, VT 05405, US.
3Department of Computer Science, Burlington, VT 05405, US.
4Santa Fe Institute, 1399 Hyde Park Rd, Santa Fe, NM 87501, US
(Dated: April 21, 2026)
The mobility of high-potential individuals, particularly graduates from elite academic institutions,
serves as a critical driver of global innovation and economic development. Despite its importance,
granular data on the specific trajectories and demographic drivers of these flows remain scarce in
traditional administrative sources. In this study, we leverage anonymized, aggregate-level digital
trace data from the LinkedIn Advertising platform to map the international mobility of graduates
from 1,504 QS-ranked universities across 102 countries. We find that global talent flows are highly
concentrated, with the United States capturing 38.4% of the mobile elite, followed by the United
Kingdom (7.9%) and Canada (6.8%), while regional hubs like the United Arab Emirates (5.2%) have
emerged as significant talent magnets. Our analysis reveals a global Relative Gender Gap (RGG)
of +3.16%, indicating a modest male overrepresentation that varies sharply by destination, from
extreme male skews in Ethiopia (+60.34%) to female overrepresentation in Armenia (−30.77%).
Professional integration is highly structured; while Business Development and Operations are uni-
versal entry channels, technical specialization in Engineering and IT is concentrated in specific
innovation hubs. Destination “pull” is primarily driven by economic capacity, institutional stability,
and educational infrastructure, though female graduates demonstrate significantly higher sensitivity
to the cost of living. These findings provide a high-resolution lens on the global “brain circulation,”
highlighting the destination-specific comparative advantages that govern high-skilled relocation.
I. INTRODUCTION
The mobility of high-skilled professionals has emerged
as an increasingly large and critical component of inter-
national migration [56], with the population of high-
ly educated migrants growing three times faster than
less-educated groups between 1990 and 2010 [26]. By
2020, the majority of immigrants to Organization for
Economic Cooperation and Development (OECD) coun-
tries possessed a tertiary education, as the rate of skilled
emigration continues to exceed overall emigration rates
due to the heightened human and financial capital asso-
ciated with elite mobility [1, 15]. This professional
migration represents a vital labor source for countries
facing advanced skills shortages and shrinking native-
born workforces, directly influencing economic develop-
ment, innovation, and the global circulation of knowledge
[12, 17]. Central to this phenomenon is international stu-
dent mobility, which has nearly tripled over the last two
decades. While the number of mobile tertiary students
reached 2.2 million in 2001 [56], it climbed to over 6.39
million by 2021—defying pandemic-era expectations with
continued growth.[31] This population remains notably
gendered; although the gap has narrowed, male students
still comprise 52% of the global total compared to 47%
for females.[36] Historically, 70% of these students have
∗ tabia.prama@uvm.edu
† chris.danforth@uvm.edu
‡ peter.dodds@uvm.edu
been concentrated in the US, UK, Germany, France, and
Australia, with the US remaining the primary destination
hosting over 833,000 students in 2021 and seeing an addi-
tional 8% growth in the 2023/24 academic year.[37] How-
ever, as the market undergoes a structural shift toward
emerging hubs in Asia and the Middle East, the strategic
need for Western economies to retain international talent
via pathways like Optional Practical Training (OPT) has
intensified.
Despite the wealth of literature on brain drain [11],
brain gain [23] and brain circulation [7, 58], there remains
a critical lack of reliable data regarding the specific tra-
jectories of students from diverse origins [3, 47]. Despite
the increasing scale of these flows, many dynamics relat-
ed to skilled migration remain poorly understood, pri-
marily due to persistent data limitations in administra-
tive sources that lack granular disaggregation by gender
and skill level [13, 27, 30]. High-quality migration and
mobility data are notoriously difficult to obtain [48]; even
widespread harmonization efforts such as the Integrated
Public Use Microdata Series (IPUMS) [4] often reveal
paradoxical records between neighboring nations due to
divergent registration and digitization practices.
Traditionally, researchers have attempted to remedy
these gaps by treating migration as a residual “error
term” calculated from the difference between popula-
tion growth and vital statistics [9]. However, such esti-
mates fail to measure actual migration events and are
prone to significant inaccuracies, particularly regarding
the non-linear, intermediary steps taken by high-skilled
cohorts [14]. To address this scarcity of reliable lon-
gitudinal data, recent studies have turned to digital
Typeset by REVTEX
arXiv:2604.16375v1  [cs.CY]  23 Mar 2026

2
trace data, high-resolution signals generated by social
media and professional networks [10, 29, 60]. Among
these, the LinkedIn Advertising platform emerges as a
uniquely robust source for studying professional migra-
tion, as it captures information on educational back-
grounds, employment changes, and relocation behavior
for over one billion users [24, 46]. Previous research
has successfully leveraged LinkedIn to estimate the spa-
tial distribution of university graduates [18], monitor the
labor market integration of skilled migrants [16], and doc-
ument international “brain circulation” through profes-
sional connectivity [21, 22, 50]. Crucially, it has been
validated the platform’s ability to mirror “ground truth”
gender gaps reported by the International Labour Orga-
nization (ILO) [25].
By leveraging these digital traces from LinkedIn—the
world’s largest professional networking platform with
over 900 million members in over 200 countries,[38] we
access novel data via the Advertising and Recruiter plat-
forms. These sources provide timely, aggregate-level
information about professional migrants at a significantly
richer level of detail than traditional survey data [49].[39]
In this study, we address existing research gaps through
four primary objectives: mapping the mobility of stu-
dents from QS World Ranked universities[40] across 102
countries (RQ1); identifying demographic variances in
“who moves” disaggregated by gender and age (RQ2);
tracking the selectivity and distribution of these migrants
across specific industries (RQ3); and finally, analyzing
the socio-economic and cultural drivers that influence
these global flows (RQ4).
RESUL TS AND DISCUSSION
RQ1: Global topology of student mobility across 102
countries
In this study, we define High-Potential Mobility as
users who attended QS World University Rankings
institutions and subsequently relocated internationally
(LinkedIn’s “current address” measure, interpreted as an
estimate of recently arrived professional migrant stock in
destination countries) [59]. We compile the QS list of
top-ranked universities (QS World University Rankings
2026: 1,504 institutions across 107 locations[41]). Coun-
tries not available in the platform query interface (e.g.,
Russia, Iran, Syria, Northern Cyprus) and universities
from these countries are excluded from the country-level
coverage in our data collection.
Data is collected as anonymous, aggregate-level esti-
mates via the LinkedIn advertising with Campaign Man-
ager platforms[42]. To protect individual identifiers,
the platform provides information only above a thresh-
old of 300 users; targeted queries below this thresh-
old do not return results. There are acknowledged
trade-offs between the level of detail and data sparsi-
ty in aggregate-level data [24], particularly for specific
industry categories and countries with smaller popula-
tion sizes. LinkedIn estimates user age based on profile
information such as years since college graduation and
years in the labor force. We construct three age groups
for our analysis: 18–24; 25–34; 35–55 and 55+ years old.
LinkedIn does not assign a gender to all users; on average,
75 percent of LinkedIn users are labeled as male or female
on the Advertising platform. We analyze the two gender
categories provided by LinkedIn (male and female) but
recognize the need for future research on nonbinary users
if this measure becomes available [28]. Despite these lim-
itations, the data shows patterns consistent with analy-
sis conducted by the World Bank on talent migration
trends and industry composition on LinkedIn [59, 61],
increasing our confidence in the present dataset. Relocat-
ed members are identified based on a country change in
the location of employment between two job titles, which
we interpret as an estimate of the recently arrived pro-
fessional migrant stock in destination countries [21, 57].
The destination preferences of elite graduates reveal a
highly concentrated topology of global talent flows, as
shown in Figure 1, which displays a global density map
(left) and a detailed rank distribution (right). The Unit-
ed States acts as the primary hub, capturing 38.4% of
the mobile elite. This dominance is driven by the 35–54
age bracket (25.11%), suggesting the U.S. is a defini-
tive settlement hub for established professionals. Tra-
ditional OECD nations follow, including the UK (7.9%),
Canada (6.8%), and Australia (4.7%). Notably, these
Western hubs demonstrate robust gender integration; in
the U.S., the female share (19.01%) outpaces the male
share (13.47%), reflecting an ecosystem that successfully
retains high-potential female talent.A shifting landscape
is evidenced by powerful regional magnets diversifying
the network. The UAE has emerged as a major node with
a 5.2% share, followed by Singapore (4.0%), India (3.1%),
and Saudi Arabia (3.0%). As shown in the Rank Distri-
bution in Figure 1, these hubs display unique demograph-
ic profiles; while the UAE and Saudi Arabia show a male
skew (3.15% and 2.04% respectively), Indonesia (4.3%)
attracts a much younger cohort. Its 18–24 (1.44%) and
25–34 (1.51%) groups represent a higher proportion of
intake than Western counterparts, signaling that young
talent is increasingly drawn to high-growth regional pow-
erhouses.The inclusion of Chile (2.5%), Malaysia (2.0%),
and Colombia (1.7%) in the top 20 highlights a tran-
sition toward a multi-polar network. These ”middle-
power” nodes are successfully competing for early-career
professionals, with Chile and Malaysia maintaining sta-
ble captures of the 25–34 age cohort. This trend sug-
gests that historical ”brain drain” is evolving into ”brain
circulation,” where elite graduates navigate a globalized
market where the Global South is becoming increasing-
ly competitive, ultimately reshaping the future of global
human capital distribution.
The interactive visualization enables a granular decom-
position of talent mobility from specific origin country
(See Supplementary File A), revealing distinct migra-

3
FIG. 1: Global Topology and Demographic Composition of High-Potential Mobility. The map illustrates the global
distribution of internationally mobile graduates from QS-ranked universities, with destination countries colored by
total student mobility counts. The accompanying Rank Distribution (right) highlights the top 20 destination
countries by global share. Each bar in the rank distribution is disaggregated by Age Distribution (left-facing: 18–24,
25–34, 35–54, and 55+ cohorts) and Gender Distribution (right-facing: platform-inferred male and female shares),
revealing a mobility pool predominantly concentrated in prime working ages (25–54) and showing varying degrees of
gender balance across major destination hubs (see interactive dashboard).
tory “fingerprints.” Outward mobility from the United
States shows a pivot toward emerging markets (See Fig-
ure 7): Indonesia captures 16.7% of the U.S. top-20 des-
tination share and is strongly youth-skewed, with the
18–24 and 25–34 cohorts together accounting for 10.79%,
far exceeding the 55+ share (0.67%). In contrast, flows
to Chile (12.2%) are more senior-heavy, with the 35–54
and 55+ cohorts comprising over half of Chile’s share,
while other prominent U.S.-origin destinations such as
Cyprus (7.4%) and Brunei Darussalam (6.0%) emphasize
mid-career movers. Similarly, United Kingdom reveals
a structure shaped by historical and economic ties (See
Figure 8): the United States is the dominant recipient
of UK-based elite talent, capturing 28.9% of the UK
top-20 distribution, with an overwhelmingly profession-
al profile (a combined 18.52% aged 35+), while the UK
also serves as a feeder to Commonwealth and regional
markets including India (7.5%), Australia (6.8%), and
Singapore (6.1%). Although flows to Australia remain
relatively gender-balanced, mobility to the United Arab
Emirates (6.4%) is distinctly male-skewed (3.56% male
vs. 1.81% female), consistent with broader regional pat-
terns. Overall, the country-by-country breakdown high-
lights increasingly complex “brain circulation” dynamics:
for UK-origin mobility, Hong Kong (5.0%) and China
(3.9% emerge as key nodes for the 25–34 cohort, while
Malaysia (5.0%) and Nigeria (2.9% point to strengthen-
ing North–South corridors, illustrating how destinations
compete for specific segments of the global elite workforce
by age, gender, and career stage.
Demographic composition results (Supplementary Fig-
ure 9) indicate strong imbalances by both gender and
age. The gender distribution shows a small observed
male share (2.55%) in the platform-inferred aggregate
(Supplementary Figure 9). The age profile is concen-
trated in prime working ages: the 35–54 group comprises
the largest share (23.10%), followed by 25–34 (16.71%)
and 18–24 (2.45%), while 55+ is consistently the smallest
category (Supplementary Figure 9). The region-level bar
plot shows that total emigrant shares are unevenly dis-
tributed across regions and highlights stepwise gaps in
ordered regional shares—most notably Oceania (↑16.68
percentage points), Asia (↑11.41), and Europe (↑9.37)
(Supplementary Figure: Region-wise percent of total
emigrants). Taken together, these composition patterns
motivate examining where high-potential migrants relo-
cate across the global system. To interpret the direc-
tionality of high-potential mobility, Figure 2 summarizes
directed inter-regional flows in percentage terms, where
each ribbon represents the share of an origin region’s total
outflow that relocates to a given destination (outgoing
shares sum to 100% within each origin). The resulting
topology reveals clear destination preferences and asym-
metric exchange patterns across regions. Asia’s outward
trajectory is the most concentrated: 64.3% of Asia’s out-
flow is directed to the Americas, followed by Europe

4
0
5
10
0
5
10
15
2025 30
35
0
5
10
15
20
25
30
0
5
10 15
20
25
30
0
5
10
Africa
Americas
Asia
Europe
Oceania
FIG. 2: Directed Inter-Regional Flows of internationally
mobile graduates from QS-ranked universities across
five world regions. Each ribbon represents a directed
flow, and its width at the origin indicates the share of
an origin region’s total outflow that relocates to a given
destination region.
(24.2%) and Oceania (8.0%), with a smaller share to
Africa (3.5%). European circulation exhibits a dual pull,
with graduates splitting primarily between the Americas
(48.3%) and Asia (39.3%), and smaller shares flowing to
Africa (6.6%) and Oceania (5.9%). The Americas show a
comparatively balanced pattern, sending most outflow to
Asia (45.8%) and Europe (41.4%), with smaller fractions
to Africa (9.8%) and Oceania (3.0%). Africa’s outflow
is directed predominantly toward Asia (49.5%), followed
by the Americas (26.9%), Europe (17.9%), and Oceania
(5.8%). Finally, Oceania sends over half of its outflow
to Asia (52.3%), with additional flows to the Americas
(29.5%), Europe (15.9%), and Africa (2.3%), reinforcing
Asia’s central role as a destination region across multiple
origin-specific distributions.
RQ2:Gender Heterogeneity in Student Mobility
We quantify gender imbalance in high-potential
mobility using a Relative Gender Gap (RGG) score,
where positive values indicate male overrepresentation
and negative values indicate female overrepresentation
among internationally mobile graduates from QS-ranked
universities.[43] At the global level, we estimate RGG =
+3.16%, indicating a modest overall male advantage in
international relocation among graduates of top-ranked
universities[54, 55]. Despite near-parity globally, region-
al aggregates reveal pronounced divergence, consistent
with variation in labor-market structure and institutional
context. Destinations in Africa (RGG = +27.10%) and
Asia (RGG = +23.10%) exhibit the largest male over-
representation, indicating strongly male-skewed mobili-
ty into these regions. This pattern is consistent with
broader evidence that migrant stocks in parts of the Mid-
dle East and North Africa (MENA) are heavily male—
roughly two-thirds of international migrants in the region
are male (2015), with especially high male shares in sev-
eral Gulf states (e.g., 66% male in Kuwait and 84%
male in Qatar) [20]. while women comprise at least
half of emigrants in other settings (e.g., the Occupied
Palestinian Territories, Lebanon, and Jordan), under-
scoring how destination-specific labor markets and stu-
dent mobility regimes shape gender composition. In con-
trast, the Americas display the most female-skewed pro-
file (RGG =−10.35%), implying female overrepresenta-
tion among internationally mobile QS graduates. Europe
(RGG = +1.10%) and Oceania (RGG = +4.40%) are
closest to parity, with only modest male overrepresenta-
tion.
Consistent with these regional differences, Figure 3
shows wide dispersion in gender balance across the 102
destination countries analyzed. The most male-skewed
destinations include Ethiopia (+60.34%), Saudi Arabia
(+54.91%), Pakistan (+54.13%), Libya (+52.41%), and
Kyrgyzstan (+48.24%); for example, RGG = +60.34%
indicates an extremely male-dominated mobility pool.
Such extreme male skews are plausibly shaped by a com-
bination of (i) gendered constraints on education and
later mobility and (ii) sectoral labor demand that dis-
proportionately recruits men. Evidence from Ethiopia,
for example, documents persistent gender disadvantages
for girls and young women—linked to entrenched gen-
der norms and life-course constraints—which can reduce
women’s ability to translate education into cross-border
mobility relative to men.[32] Libya provides a clear illus-
tration of how destination labor markets can generate
male-heavy migrant pools: the IOM Displacement Track-
ing Matrix (DTM) reports that around 80% of migrants
in Libya are male, and that employed male migrants are
concentrated in sectors including construction (report-
ed as the largest category), alongside manufacturing and
agricultural labor. For Kyrgyzstan, external evidence
suggests an additional mechanism relevant to platform-
based measurement: the World Bank reports that many
female migrants from the Kyrgyz Republic are engaged
in low-skilled domestic work abroad [45], which may
reduce visibility in professional online platforms even
when migrants have substantial human capital. This
type of occupational downgrading or “skills mismatch”
can plausibly contribute to male-skewed professional-
platform mobility signals even when women migrate in
large numbers.
At the same time, a substantial subset of coun-
tries cluster near parity, including Viet Nam (−0.02%),
South Korea (−0.11%), Canada (+0.22%), Puerto Rico

5
FIG. 3: Global Relative Gender Gap (RGG) in High-Potential Mobility to show the gender imbalances among
internationally mobile graduates from elite universities across 102 countries. The RGG score identifies destinations
with male overrepresentation (blue, e.g., Ethiopia at +60.34%) versus female overrepresentation (pink, e.g., Armenia
at−30.77%), while white areas signify near-parity (e.g., Canada at +0.22%). (see interactive dashboard)
(+0.25%), and Romania (−0.50%), with only modest
skews in settings such as China (Mainland) (+0.73%),
the Netherlands (+1.55%), and Hungary (+1.64%). This
near-zero cluster indicates that large gender gaps are
not inevitable; many destinations appear to operate
as approximately gender-neutral endpoints for high-
potential movers.
At the female-skewed end of the distribution, the low-
est RGG values are observed in Armenia (−30.77%),
Norway (−17.48%), and the United States (−16.28%),
indicating substantial female overrepresentation among
high-potential migrants in these destinations. In the
United States, this is consistent with the broader demo-
graphic context in which immigrant women constitute
a slight majority of the foreign-born population (51.3%
in 2021) [6], which can support female-majority cohorts
depending on the education-to-work pathways captured
by platform measures. Armenia’s strong female skew
is consistent with documented male labor outmigration
(often to Russia) that leaves women disproportionately
represented in some rural communities, creating gender-
selective mobility systems [2, 8]. Norway’s female skew
similarly aligns with official statistics showing a large and
growing female immigrant population; Statistics Norway
reports 428,100 immigrant women at the beginning of
2023, corresponding to 16% of all resident women [51].
Taken together, these results indicate that while the
global gender gap in high-potential mobility is small,
gendered selectivity is strongly destination-specific.
Extreme male overrepresentation is concentrated in a
subset of destinations and is consistent with contexts
where education-to-mobility pipelines are more gender-
stratified and where labor demand is concentrated in
male-dominated sectors (as seen in MENA aggregate
patterns and in Libya’s DTM profile). Conversely,
female-skewed destinations may reflect a combination
of baseline immigrant composition (e.g., the United
States), gendered mobility systems (e.g., male labor
outmigration from Armenia), and destination contexts
where female immigrant populations are growing (e.g.,
Norway). Importantly, the large cluster of near-parity
destinations underscores that gender imbalance is not a
universal feature of high-potential mobility but varies
systematically across destinations and the pathways
that connect education to international relocation.
RQ2: Age Heterogeneity in Student Mobili-
tyWe evaluate the demographic composition of high-

6
potential mobility using the Age Dissimilarity Score
(Dc), which quantifies how strongly a destination coun-
try’s migrant age distribution deviates from the global
benchmark age shares. Values near zero indicate a com-
paratively “standardized” age structure dominated by
prime working ages, whereas higher values indicate age-
selective inflows concentrated in specific cohorts (e.g.,
student-heavy or older-skewed profiles). Across all des-
tinations, the mean global dissimilarity isD c = 0.1663,
indicating moderate but meaningful age-structure het-
erogeneity across the global mobility system. Region-
al aggregates show clear differences in demographic sta-
bility and, by implication, in labor-market integration
potential. Europe exhibits the lowest regional dissimi-
larity (Dc = 0.0772), consistent with an age profile that
closely tracks the global benchmark and reflects a pre-
dominantly working-age inflow across multiple corridors.
The Americas show a higher deviation (D c = 0.1286)
but remain strongly concentrated in active ages; in the
United States, 77.1% of the foreign-born population is of
working age (16–64), compared with 60.9% among the
U.S.-born population, implying a lower dependency bur-
den among migrants and a greater potential fiscal con-
tribution through labor-force participation and tax rev-
enue [5]. Asia (D c = 0.1307) and Oceania (D c = 0.1200)
show similar levels of deviation, consistent with corridor-
specific selection that emphasizes younger working-age
movers; in Oceania, mobility is often concentrated in
early-career cohorts (median age 37) [52], consistent with
recruitment and post-study pathways that disproportion-
ately attract younger adults [19]. Africa (D c = 0.1198)
also departs from the benchmark, reflecting a compara-
tively youthful mobility profile; the median age of inter-
national migrants in Africa was 31 in 2017 [53], consistent
with migration systems shaped by younger cohorts and
substantial intra-continental movement.
Figure 4 shows the cross-country differences inD c,
revealing outlier destinations where mobility is strong-
ly cohort-concentrated, plausibly reflecting distinctive
migration histories, labor demand, and crisis dynam-
ics. Indonesia (D c = 0.507) and Slovenia (D c = 0.505)
rank among the highest-discrepancy destinations, indi-
cating pronounced deviation from the global bench-
mark. In Indonesia, age structure varies sharply by
destination corridor: migrants residing in the Nether-
lands are substantially older, consistent with long-run
historical and family-linked settlement channels, whereas
migrants in Korea and Japan are heavily concentrated in
younger cohorts, consistent with labor-market selection
and contract-based recruitment that draws early-career
movers [44]. Slovenia shows similarly strong age selec-
tivity consistent with labor-linked entry, with migrants
arriving at a relatively young average age (27 at immi-
gration). Cuba (D c = 0.402) represents another high-
discrepancy case, consistent with crisis-driven, working-
age–concentrated exits (“brain drain”): 77–80% of emi-
grants fall between ages 15 and 59, a composition that
plausibly accelerates demographic aging in the origin
population by disproportionately removing economical-
ly active cohorts.
In contrast, several destinations exhibit low dissimilar-
ity scores, indicating age distributions that closely resem-
ble the global benchmark and reflect comparatively stan-
dardized working-age inflows. Romania (D c = 0.042),
Ireland (D c = 0.047), and Slovakia (D c = 0.049) fall in
this low-imbalance range. In Ireland, 52% of immigrants
are aged 25–44, consistent with broad inflows centered
on prime labor-market ages rather than a narrow cohort
channel. In Slovakia, foreign residents are concentrat-
ed in the 30–34 range and show relatively high educa-
tional attainment (26.3% holding university degrees ver-
sus 17.9% among the native population), consistent with
selective inflows dominated by early- to mid-career pro-
fessionals rather than student-only or older-skewed path-
ways.
Overall, age-structure variation indicates that high-
potential mobility is shaped by corridor-specific selection
mechanisms rather than a single global demographic
profile. Europe’s lowD c suggests relatively benchmark-
aligned inflows across multiple corridors, while the
United States illustrates how a working-age–heavy
migrant profile can reduce dependency burdens and
support fiscal contributions. By contrast, Indonesia and
Slovenia highlight how historically embedded corridors
and labor recruitment regimes can generate strongly
cohort-selective inflows, and Cuba illustrates how crisis
dynamics can concentrate mobility into prime work-
ing ages with potential downstream consequences for
origin-country aging. Because pathway composition can
shift both age and gender distributions through sectoral
sorting and mobility constraints, demographic patterns
are most informative when interpreted jointly acrossD c,
RGG, and directed flow topology.
RQ3: Professional Distribution of High-Skilled
Migrant Graduates
The professional integration of internationally mobile
graduates exhibits a highly structured, domain-specific
pattern across all 50 host economies, indicating that
cross-border mobility is shaped less by uniform “global”
demand than by destination-specific comparative advan-
tage.
Figure 5 shows across nearly every country, Business
Development and Operations function as the dominant
entry channels for high-skilled talent, forming a commer-
cial–operational engine that is particularly pronounced
in service-scaling destinations such as the United Arab
Emirates (14.6% Business Development, 13.0% Oper-
ations), Oman (16.9% Business Development), and
Thailand (16.4% Business Development), and remains
central even in secondary European markets like Austria
(15.8% Business Development), Greece (15.7%), and
Italy (14.1%), where migrant absorption primarily
reinforces commercial growth rather than deep technical
specialization. In contrast, the pull for Engineering
and Information Technology is sharply concentrated in

7
FIG. 4: Global Age Imbalance (D c Score) of High-Potential Migrants to visualizes the Age Dissimilarity Score (D c)
across 102 destination countries, quantifying how strongly a nation’s migrant age distribution deviates from the
global benchmark. Destinations with low dissimilarity (yellow-green, e.g., Romania atD c = 0.042) reflect
standardized working-age inflows, while high dissimilarity (dark teal/purple, e.g., Indonesia atD c = 0.507 and
Slovenia atD c = 0.505) indicates age-selective mobility concentrated in specific cohorts due to labor recruitment
regimes or historical corridors. (see interactive dashboard)
innovation hubs that selectively absorb graduates into
technical roles, including the United States (9.4% Engi-
neering, 5.5% IT), Germany (7.8% Engineering), Canada
(8.9% IT, 7.7% Engineering), Israel (8.4% Engineering,
5.6% IT), as well as Japan (8.4% Engineering) and Sin-
gapore (5.8% Engineering), reflecting targeted demand
tied to R&D ecosystems and high-tech industry capacity.
High-value knowledge-economy functions—especially
Finance and Research—are concentrated in a smaller
set of global nodes, most notably Hong Kong SAR
(Finance 8.0%), Switzerland (Finance 5.0%, Research
6.4%), and the United Kingdom (Research 3.4%), while
Education emerges as a major pathway in several Latin
American and Asian destinations, including Jordan
(14.2%), Brazil (11.0%), Argentina (11.0%), Chile
(10.9%), China (Mainland) (8.9%), and South Korea
(8.6%). Finally, the distributions reveal distinct niche
outliers and emerging footprints, such as Cyprus as a
strong anomaly with a concentrated focus on Human
Resources (20.9%), Poland as a secondary European
technical magnet (IT 5.8%), and developing host mar-
kets like Nigeria (Engineering 4.0%, Education 2.3%)
and Uganda (Business Development 11.2%, Education
7.1%) where professional integration is still consolidating
around foundational commercial and education sectors.
Taken together, the results shows that the occupational
composition of high-skilled graduate mobility is an
adaptive response to destination-specific labor-market
demand, with countries selectively integrating migrant
talent into functions that mirror their national economic
specialization.
RQ4: Influencing F actors of Global Student
Mobility
To investigate the socioeconomic and demographic
drivers of international student mobility, we estimated
a multivariate Ordinary Least Squares (OLS) regression
using destination-country predictors capturing econom-
ic capacity (GDP per capita, poverty, cost of living,
economic freedom, remittances, unemployment), human
capital and public services (education, life expectancy,
healthcare expenditure), governance and social structure
(democracy, gender gap, social welfare spending), and
risk and stability (global peace, climate performance,
women peace and security), alongside baseline geography
and demography (area, population density). Across 102

8
FIG. 5: Professional Distribution of High-Skilled
Migrant Graduates of the percentage of mobile
graduates across 10 domains in 50 destination countries.
Business Development and Operations are universal
entry channels (e.g., Oman, Thailand>15%), while
Engineering and IT are concentrated in innovation hubs
like the U.S. (9.4% Eng) and Canada (8.9% IT).
destination countries using data from World Population
Review [33] , the model explains 33.6% of the variance
in global student mobility (R 2 = 0.336; See Appendix D
for details).
Figure 6 shows student mobility is significantly
positively associated with larger destination area, higher
GDP per capita, more democratic governance, greater
economic freedom, higher remittance intensity, stronger
education conditions, and higher societal peace, con-
sistent with a destination pull mechanism combining
capacity and stability. In contrast, population density
and unemployment exhibit statistically significant
negative associations, indicating that congestion and
weaker labor-market conditions reduce destination
attractiveness. After conditioning on core economic
and institutional factors, the gender gap index and
healthcare expenditure show small but statistically
significant negative associations, plausibly reflecting
overlap among development indicators rather than
direct deterrent effects. Several predictors, including
social welfare spending, poverty, cost of living, life
expectancy, climate performance, and women peace and
security, do not reach conventional significance in this
specification, suggesting limited marginal explanatory
power beyond the core capacity and stability measures.
1
 0 1 2 3 4
Coefficient (Effect Size)
Density
Unemployment Rate
Gender Equality Gap
Healthcare Spending
Poverty Rate
Social Welfare Spending
Women in Peace and Security
Climate Change Performance
Cost of Living
Economic Freedom
Education Quality
Remittances
Democracy
Global Peace
GDP per Capita
Area
***
*
*
*
*
*
***
***
***
***
***
Stronger Pull Factors
 Stronger Push Factors
FIG. 6: Drivers of Global High-Potential Mobility.
Coefficient plot from a multivariate OLS regression
(R2 = 0.336) estimating factors associated with
destination choices of internationally mobile elite
graduates. Point size is proportional to the absolute
t-statistic, indicating the strength of statistical evidence
for each predictor, and the horizontal axis reports
coefficient estimates (effect sizes). Blue points denote
positive associations (pull factors), such as geographic
AreaandGDP per Capita, while red points denote
negative associations (deterrents), led byPopulation
DensityandUnemployment Rate. Significance levels:
∗∗∗p <0.001, ∗p <0.05.
To further examine heterogeneity in destination “pull”
factors, we disaggregated mobility flows by gender and
estimated models for male and female cohorts across
102 destination countries. Model performance is simi-
lar for both groups (male:R 2 = 0.252; female:R 2 =
0.240), indicating that the same macro-structural pre-
dictors explain comparable shares of variation in gender-
specific mobility (See Appendix E). Figure 10 summa-
rizes coefficient concordance by plotting male against
female estimates for each predictor. Most covariates clus-
ter near the identity line, implying broadly symmetric
associations across genders. In particular, destination
area, GDP per capita, and democratic governance exhib-
it consistently positive associations, reflecting a shared
preference for destinations with greater economic capac-
ity and stronger institutions. Likewise, population den-
sity and unemployment are negatively associated with
both male and female mobility, suggesting that structural
crowding and weaker labor-market conditions reduce des-

9
tination attractiveness for both groups.
Departures from the identity line reveal gender-
differentiated sensitivities. Female mobility is more
strongly associated with cost of living and education con-
ditions, and shows a significant negative association with
poverty, indicating greater selectivity with respect to des-
tination socioeconomic context. In contrast, male mobil-
ity aligns more closely with economic freedom and glob-
al peace, consistent with a stronger response to market
openness and broad stability signals in the male model.
Taken together, the gender-disaggregated results suggest
that destination choice is governed by a common “capac-
ity and stability” mechanism, but the relative salience
of specific socioeconomic constraints differs by gender
in ways consistent with gendered opportunity structures
and differential exposure to destination risk and resource
environments.
LIMIT A TIONS AND FUTURE DIRECTIONS
While our approach leverages aggregated audience esti-
mates to study high-skilled mobility at scale, several
limitations warrant caution. The data are subject to
self-selection, since LinkedIn users are not representa-
tive of national populations and skew toward highly edu-
cated, urban, and digitally connected groups. Mea-
sures also rely on self-reported profile attributes (e.g.,
schools attended, location), which may be incomplete or
inconsistently reported across countries and demograph-
ic groups. In addition, audience counts and demograph-
ic labels are generated by proprietary, evolving platform
systems, so definitions and taxonomies may shift over
time in ways that complicate comparability and repli-
cation; relatedly, changes to the platform interface or
endpoints can disrupt reproducibility. Finally, although
we use only anonymized, aggregate outputs subject to
a minimum audience threshold (300 users), ethical risks
remain, including the possibility of group-level harms if
aggregate statistics are misinterpreted or misused.
These constraints motivate several directions for future
work. Substantively, we plan to examine gendered occu-
pational sorting by linking gender-disaggregated mobility
to destination professional profiles to identify where gaps
are largest (e.g., Engineering vs. Education) and how
these patterns vary by region and institutional context.
We also aim to extend the analysis by degree level (bach-
elor’s, master’s, PhD) to test whether destination “pull”
factors differ across stages of human-capital accumula-
tion. Methodologically, future work should triangulate
platform-based estimates with administrative and survey
benchmarks where available, develop sensitivity analy-
ses for platform penetration and measurement error, and
document collection procedures to improve transparency
and reproducibility.
MA TERIALS AND METHODS
Data collection
We construct a bilateral student-mobility dataset from
aggregate audience estimates provided by LinkedIn’s
Campaign Manager (Advertising) platform. Although
LinkedIn does not allow targeting users by “countries
previously lived in,” it supports targeting byMember
school, enabling queries for members who studied at a
specific higher-education institution and currently reside
in a specified country. We use this feature to approx-
imate education-based origins: for each origin country,
we compiled the 2026 QS-ranked universities[34] and
mapped each institution to its LinkedIn School entity
(e.g.,urn:li:school:<ID>) via the platform’s school
search endpoint. Using these school identifiers, we
queried audience counts for members who (i) studied
at a QS-ranked institution in origin countryXand (ii)
currently live in destination countryY, generating an
origin–destination mobility matrix over 102 destination
countries (each origin paired with the other 101 possible
destinations). While the QS rankings cover 107 coun-
tries, LinkedIn location targeting was not available for
Russia, Iran, Syria, and Northern Cyprus, limiting our
destination coverage to 102 countries (see Appendix for
the list C). All outputs are anonymous, aggregate esti-
mates; LinkedIn suppresses audiences below a privacy
threshold of 300 users, so some small flows are censored.
In addition to total flows, we collected stratified audi-
ence counts by gender (male/female) and age (18–24, 25–
34, 35–54, 55+), and we extracted destination-specific
occupational composition using LinkedIn’s job-function
taxonomy. For each destination, occupational categories
are reported as shares of the migrant stock (e.g., Busi-
ness Development, Operations, Engineering, Information
Technology, Education, Finance), allowing us to char-
acterize how host labor markets absorb internationally
mobile graduates.
Relative Gender Gap (RGG)
We quantify gender imbalance in high-potential mobil-
ity using aRelative Gender Gap(RGG) score. For each
uniti(e.g., destination country or destination region), let
Mi andF i denote the total number of male and female
migrants, obtained by summing gender-disaggregated
LinkedIn audience estimates across all relevant origin–
destination pairs. We define
RGGi = 100× Mi −F i Mi +F i ,(1)
where RGGi >0 indicates percentage of male overrepre-
sentation, RGGi <0 indicates percentage of female over-
representation, and RGG i = 0 indicates parity. Region-
level scores are computed by first aggregating countries

10
within regionr,M r = P j∈r Mj andF r = P j∈r Fj, and
then applying Eq. 1. The global RGG is computed anal-
ogously using totalsM= P i Mi andF= P i Fi.
Age dissimilarity score
We quantify how strongly a destination’s age composi-
tion of internationally mobile graduates deviates using an
Age Dissimilarityscore. Letg k denote the global share of
migrants in age groupk∈ {18–24,25–34,35–54,55+},
computed as
gk =
P
i NikP
i Ti
,(2)
whereN ik is the number of migrants in age groupkfor
unitiandT i = P k Nik is total migrants ini. For each
uniti, we compute within-unit age sharess ik =N ik/Ti
and define
Di =
s
1
3
X
k
(sik −g k)2
gk
.(3)
LargerD i values indicate greater deviation from the
global age profile. We compute region-level scores by
first aggregating age counts within each region and then
applying the same equation 3.
Estimating destination-level professional profiles
We estimate destination-level professional profiles by
combining LinkedIn audience counts with job-function
shares. For each origin–destination pair, LinkedIn pro-
vides the total migrant audienceN od and the percentage
distribution across function categoriesp odk (e.g., Engi-
neering, Education, Finance). We convert these percent-
ages into implied category counts,
Nodk =N od × podk 100 ,(4)
and then aggregate across origins to obtain destination
totalsN dk = P o Nodk. Finally, we report each destina-
tion’s professional composition as shares of its migrant
stock,
sdk = 100× NdkP
k Ndk
.(5)
DA T A A V AILABILITY
All student-mobility datasets and destination-country
demographic indicators used in this study are provided
in CSV format in thedata/folder of the repository[35].
All analysis code, including preprocessing pipelines,
professional-profile construction, and the regression mod-
els reported in the paper, is available in thecode/folder.
ACKNOWLEDGMENTS
The authors express their gratitude for helpful conver-
sations with Julia Witte Zimmerman, Ashley Fehr, Calla
Beauregard, Alejandro Javier Ruiz Iglesias, Mikaela Irene
Fudolig. The authors acknowledge financial support
from the National Science Foundation under Award Nos.
2242829 (VT EPSCoR SOCKS) and 2419830 (SaTC),
and the Vermont Advanced Computing Core (V ACC) for
computational support.

11
[1] Global migration, gender, and health professional creden-
tials. 2022.
[2] Gayane Abrahamyan and Justyna Mielnikiewicz. Arme-
nia: A Woman’s World in One Mountain Village.
Eurasianet, March 7 2011. Accessed: 2026-03-23.
[3] Aliakbar Akbaritabar, Tom Theile, and Emilio Zagheni.
Global flows and rates of international migration of schol-
ars. 2023.
[4] Monica J. Alexander, Kivan Polimis, and Emilio Zagheni.
Combining social media and survey data to nowcast
migrant stocks in the united states.Population Research
and Policy Review, 41:1 – 28, 2020.
[5] American Immigration Council. Immigrants in the Unit-
ed States, 2021. Accessed: 2026-03-23.
[6] American Immigration Council. A snapshot of immigrant
women in the united states, 2021. Accessed: 2026-03-23.
[7] Silvia Appelt, Brigitte van Beuzekom, Fernando Galindo-
Rueda, Roberto de, and Pinho. Which factors influence
the international mobility of research scientists. 2015.
[8] Aoife Barry. Women left behind as 98% of men leave
Armenian village. The Journal, March 18 2011.
[9] Vladimir Canudas-Romo, Tianyu Shen, and Collin F.
Payne. The components of change in population growth
rates.Demography, 2022.
[10] C. Coimbra Vieira, M. Fatehkia, K. Garimella, I. G.
Weber, and E. Zagheni. Using facebook and linkedin
data to study international mobility. In A. A. Salah,
E. E. Korkmaz, and T. Bircan, editors,Data Science
for Migration and Mobility, volume 251 ofProceedings of
the British Academy, pages 141–158. Oxford University
Press, Oxford, 2022.
[11] Fr´ ed´ eric Docquier, Olivier Lohest, and Abdeslam Mar-
fouk. Brain drain in developing countries.The World
Bank Economic Review, 21:193–218, 2007.
[12] Fr´ ed´ eric Docquier and Hillel Rapoport. Globalization,
brain drain, and development.Journal of Economic Lit-
erature, 50(3):681–730, 2012.
[13] Katharine M. Donato, Bhumika Piya, and Anna W.
Jacobs. The double disadvantage reconsidered: Gender,
immigration, marital status, and global labor force par-
ticipation in the 21st century 1.International Migration
Review, 48:335 – 376, 2014.
[14] Lucas G. Drouhot, Emanuel Deutschmann, Caroli-
na Viviana Zuccotti, and Emilio Zagheni. Computa-
tional approaches to migration and integration research:
promises and challenges.Journal of Ethnic and Migra-
tion Studies, 49:389 – 407, 2022.
[15] Rohen d’Aiglepierre, Anda Mariana David, Charlotte
Levionnois, Gilles Spielvogel, Michele Tuccio, and Erik R.
Vickstrom. A global profile of emigrants to oecd coun-
tries. 2020.
[16] Ina Ganguli, Shulamit Kahn, and Megan J. MacGarvie.
The roles of immigrants and foreign students in us sci-
ence, innovation, and entrepreneurship. 2020.
[17] Tel´ esforo Ram ´ ırez Garc ´ ıa. Rese˜ na: High-skilled migra-
tion. drivers and policies.Revista Latinoamericana de
Poblaci´ on, 13:162–165, 2019.
[18] Nayoung Heo, Hsin-Chieh Chang, and Guy J. Abel.
Investigating the distribution of university alumni pop-
ulations within south korea and taiwan based on data
from the linkedin advertising platform.Cities, 2023.
[19] International Organization for Migration (IOM). Age
and sex breakdown of international migrants. Asia-
Pacific Migration Data Hub, 2026. Accessed: 2026-03-23.
[20] International Organization for Migration (IOM), Region-
al Office for the Middle East and North Africa. Migration
to, from and in the middle east and north africa: Data
snapshot. Report, April 2016. Prepared by IOM Regional
Office for the Middle East and North Africa.
[21] Elizabeth M. Jacobs, Tom Theile, Daniela Perrotta,
Xinyi Zhao, Athina Anastasiadou, and Emilio Zagheni.
Global gender gaps in the international migration of
professionals on linkedin.Population and Development
Review, 51, 2024.
[22] Ghazal Kalhor, Hannah Gardner, Ingmar Weber, and
Ridhi Kashyap. Gender gaps in online social connectivity,
promotion and relocation reports on linkedin.ArXiv,
abs/2308.13296, 2023.
[23] Devesh Kapur. Give us your best and brightest: The
global hunt for talent and its impact on the developing
world. 2005.
[24] Ridhi Kashyap. Has demography witnessed a data revo-
lution? promises and pitfalls of a changing data ecosys-
tem.Population Studies, 75:47 – 75, 2021.
[25] Ridhi Kashyap and Florianne C. J. Verkroost. Analysing
global professional gender gaps using linkedin advertising
data.EPJ Data Science, 10, 2021.
[26] Sari Pekkala Kerr, William R. Kerr, Caglar Ozden, and
Christopher Parsons. Global talent flows.International
Trade eJournal, 2016.
[27] Eleonore Kofman. Towards a gendered evaluation of
(highly) skilled immigration policies in europe.Inter-
national Migration, 52:116–128, 2014.
[28] Danya Lagos. Has there been a transgender tipping
point? gender identification differences in u.s. cohorts
born between 1935 and 2001.American Journal of Soci-
ology, 128:94 – 143, 2022.
[29] Bruno Latour. Beware, your imagination leaves digital
traces.Times Higher Literary Supplement, April 2007.
application/pdf.
[30] Wolfgang Lutz, William P. Butz, and Samir Kc. World
population and human capital in the twenty-first century.
2014.
[31] International Organization for Migration (IOM),
World Migration Report 2024, Chapter 2:
International Students. Available at:https:
//worldmigrationreport.iom.int/what-we-do/
world-migration-report-2024-chapter-2/
international-students. Accessed 8 February 2026.
[32] Bekele Tefera and Paola Pereznieto, with Guday
Emirie,Transforming the lives of girls and young
women: Case study: Ethiopia(London: Overseas
Development Institute, August 2013). Available at:
https://odi.cdn.ngo/media/documents/8820.pdf.
[33] World Population Review, accessed 1 February 2026:
https://worldpopulationreview.com/.
[34] QS World University Rankings, accessed 2 Febru-
ary 2026:https://www.topuniversities.com/
world-university-rankings.
[35] https://github.com/TabiaTanzin/migration-dashboard.
[36] In 2001, there were around 1 million internationally
mobile female students (45% of the total) and 1.2 million

12
male students (54%). While this gap has narrowed over
the last 20 years, the number of internationally mobile
female students remains lower than that of male students;
in 2021, around 3 million students were female (47%)
and males comprised around 3.4 million (52%). Source:
UNESCO Institute for Statistics. Accessed 8 February
2026.
[37] International student totals grew by 8% in the
2023/24 academic year, building on 12% growth in
2022/23 and 4% in 2021/22. This includes a 7%
increase in graduate enrollment and a 17% surge
in students pursuing employment via Optional Prac-
tical Training (OPT). See IIE (2023)Fall 2023
Snapshot on International Student EnrollmentAvail-
able at:https://www.iie.org/wp-content/uploads/
2023/11/Fall-2023-Snapshot.pdf. Accessed 8 Febru-
ary 2026.
[38] https://learning.linkedin.com/content/dam/me/business/en-
us/amp/learning-solutions/images/wlr-2024/LinkedIn-
Workplace-Learning-Report-2024.pdf, Accessed: 8
February, 2026.
[39] LinkedIn, “Statistics & Facts,”https://www.statista.
com/topics/951/linkedin/(accessed February 9, 2026).
[40]https://www.topuniversities.com/
university-rankings, Accessed: 8 February 2026.
[41] QS Quacquarelli Symonds (QS), “QS World University
Rankings 2026: Top global universities,”Top Universi-
ties, accessed[DATE],https://www.topuniversities.
com/world-university-rankings. The 2026 rankings
include over 1,500 universities across more than 100 loca-
tions worldwide.
[42] https://www.linkedin.com/campaignmanager ,
Accessed: 9 Feb 2026.
[43] An RGG of +X% indicates that men are overrepresented
byXpercentage points relative to women in the observed
mobility pool, whereas an RGG of−X% indicates that
women are overrepresented byXpercentage points.
[44] OECD. A review of indonesian emigrants, 2022.
[45] Nurzhamal Parpieva. Transformation of employment in
the agricultural sector of kyrgyzstan: Challenges and
prospects.Bulletin of the Kyrgyz National Agrarian Uni-
versity, 2025.
[46] Daniela Perrotta, Sarah C. Johnson, Tom Theile, Andr´ e
Grow, Helga de Valk, and Emilio Zagheni. Openness to
migrate internationally for a job: Evidence from linkedin
data in europe. InInternational Conference on Web and
Social Media, 2022.
[47] Ebru Sanliturk, Emilio Zagheni, Maciej Jan Da´ nko, Tom
Theile, and Aliakbar Akbaritabar. Global patterns of
migration of scholars with economic development.Pro-
ceedings of the National Academy of Sciences of the Unit-
ed States of America, 120, 2023.
[48] Ronald Skeldon. Interlinkages between internal and inter-
national migration and development in the asian region.
Population Space and Place, 12:15–30, 2006.
[49] Stephanie A. Smith and Brandi A. Watkins. Millenni-
als’ uses and gratifications on linkedin: Implications for
recruitment and retention.International Journal of Busi-
ness Communication, 60:560 – 586, 2020.
[50] Bogdan State, Mario Rodr ´ ıguez, Dirk Helbing, and
Emilio Zagheni. Migration of professionals to the u.s. -
evidence from linkedin data. InSocial Informatics, 2014.
[51] Statistics Norway (SSB). Immigrant women and their
Norwegian-born daughters: Demography, education,
labour and income. Technical report, Statistisk sentral-
byr ˚ a, February 19 2024. Accessed: 2026-03-23.
[52] United Nations. International Migration 2013: Age and
Sex Distribution. Technical Report 2015/4, Department
of Economic and Social Affairs, Population Division,
2015.
[53] United Nations. International Migration Report 2017:
Highlights. Technical report, Department of Economic
and Social Affairs, Population Division, New York, 2017.
[54] United Nations, Department of Economic and Social
Affairs, Population Division. Trends in internation-
al migrant stock: The 2015 revision. United Nations
database, 2015. POP/DB/MIG/Stock/Rev.2015.
[55] United Nations, Department of Economic and Social
Affairs, Population Division. World population
prospects: The 2015 revision. DVD Edition, 2015.
[56] Line Verbik and Veronica Lasanowski. International stu-
dent mobility: Patterns and trends. 2007.
[57] Carolina Coimbra Vieira, Ebru Sanliturk, and Emilio
Zagheni. Forced migration and information-seeking
behavior on wikipedia: Insights from the ukrainian
refugee crisis.ArXiv, abs/2512.01692, 2025.
[58] Torsten N. Wiesel. Fellowships: Turning brain drain into
brain circulation.Nature, 510:213 – 214, 2014.
[59] World Bank Group and LinkedIn. World bank group–
linkedin data insights: Jobs, skills, and migration
trends—methodology and validation results, 2018.
[60] Emilio Zagheni, Ingmar Weber, and Krishna P. Gumma-
di. Leveraging facebook’s advertising platform to monitor
stocks of migrants.Population and Development Review,
43:721–734, 2017.
[61] Tingting Zhu, Alan Fritzler, and Jan Alexander Kaz-
imierz Orlowski. Data insights : Jobs, skills and migra-
tion trends methodology and validation results. 2018.

13
Appendix A: Student Mobility by Origin Country
The interactive mobility map shows origin-specific stu-
dent mobility patterns for each country included in the
dataset. For every origin country, we identify the top 20
destination countries based on relative student mobility
share and decompose these flows by age cohort (18–24,
25–34, 35–54, 55+) and gender (platform-inferred male
and female). The total share for each destination rep-
resents its proportion within the origin country’s top 20
outward mobility distribution.
Appendix B: Composition of High-Potential
Mobility
Figure 9 summarizes the demographic and region-
al composition of high-potential mobility (QS-ranked
alumni who recently relocated internationally, measured
as anonymous aggregate audiences from the LinkedIn
Advertising platform). Figure 9a reports the gender com-
position of the observed emigrant population. Figure
9b reports the age composition, showing that mobility
is concentrated in prime working ages, with the 35–54
group representing the largest share and the 55+ group
the smallest. Figure 9c reports the regional distribution
of total emigrants and visualizes stepwise gaps between
ordered regional shares, highlighting pronounced differ-
ences across regions.
Appendix C: List of Countries
The analysis covers 102 destination countries for which
LinkedIn Campaign Manager locations were available.
To avoid layout overflow in the two-column PNAS tem-
plate, we report the full country list as a wrapped para-
graph inside a full-width table (Table I).
Appendix D: Influencing F actors Regressor
Outcome (dependent variable).We model student
mobility volume as a log-transformed count to reduce
skewness while retaining zero flows:
log total mobility= log(1 +total mobility),
wheretotal student mobilityis the observed origin-
to-destination mobility count. Predictors were scaled to
a common range prior to estimation (see Methods) so
coefficients reflect associations per unit change on the
standardized scale.
Predictors used in the OLS specification.Table II
defines each destination-country covariate, explains what
it measures, and clarifies whether higher values are gen-
erally interpreted as better or worse and Table III shows
the results of regressor model for student mobility.
TABLE I: List of 102 destination countries included in
the analysis.
Country list.
Argentina Guatemala Panama
Armenia Honduras Paraguay
Australia Hong Kong SAR, Chi-
na
Peru
Austria Hungary Philippines
Azerbaijan Iceland Poland
Bahrain India Portugal
Bangladesh Indonesia Puerto Rico
Belarus Iraq Qatar
Belgium Ireland Romania
Bosnia & Herzegovina Israel Saudi Arabia
Brazil Italy Serbia
Brunei Darussalam Japan Singapore
Bulgaria Jordan Slovakia
Canada Kazakhstan Slovenia
Chile Kenya South Africa
China (Mainland) Kuwait South Korea
Colombia Kyrgyzstan Spain
Costa Rica Latvia Sri Lanka
Croatia Lebanon Sudan
Cuba Libya Sweden
Cyprus Lithuania Switzerland
Czechia Luxembourg Taiwan
Denmark Macao SAR, China Thailand
Dominican Republic Malaysia Tunisia
Ecuador Malta T¨ urkiye
Egypt Mexico Uganda
Estonia Morocco Ukraine
Ethiopia Netherlands United Arab Emirates
Finland New Zealand United Kingdom
France Nigeria United States of Amer-
ica
Georgia Norway Uruguay
Germany Oman Uzbekistan
Ghana Pakistan Venezuela
Greece Palestine Viet Nam
Appendix E: Multivariate Regression Analysis of
Gender-Disaggregated Mobility
To further elucidate the drivers of high-skilled mobility,
we present the detailed results of our multivariate Ordi-
nary Least Squares (OLS) regression models for male and
female migrant flows. To stabilize variance while retain-
ing zero-flow observations, the dependent variables were
transformed using the natural logarithm as follows:
log male mobility= log(1 +male mobility),
log female mobility= log(1 +female mobility).
These models assess the impact of 17 socioeconomic
and demographic predictors across 10,403 observations.
The results, summarized in Table IV, demonstrate that
while structural drivers such as destination Area, GDP

14
FIG. 7: United States-Origin Topology and Demographic Composition of High-Potential Mobility. The map
illustrates the global distribution of internationally mobile graduates from QS-ranked universities originating from
the United States, with destination countries colored by total student mobility counts. The accompanying Rank
Distribution (right) highlights the top 20 destination countries receiving U.S.-origin talent by relative share. Each
bar in the rank distribution is disaggregated by Age Distribution (left-facing: 18–24, 25–34, 35–54, and 55+ cohorts)
and Gender Distribution (right-facing: platform-inferred male and female shares), revealing outward mobility
patterns that vary by destination but remain largely concentrated in prime working ages (25–54), with differing
levels of gender balance across regional and global hubs.
per Capita, Democracy, and Remittances remain signif-
icant positive ”pull” factors for both cohorts, their rel-
ative influence varies. Notably, female mobility exhibits
a statistically significant and stronger sensitivity to the
Cost of Living (β= 1.05) compared to male mobility
(β= 0.62,p= 0.06), while Economic Freedom serves as
a marginally significant driver for males only.

15
FIG. 8: United Kingdom-Origin Topology and Demographic Composition of High-Potential Mobility. The map
illustrates the global distribution of internationally mobile graduates from QS-ranked universities originating from
the United Kingdom, with destination countries colored by total student mobility counts. The accompanying Rank
Distribution (right) highlights the top 20 destination countries receiving UK-origin talent by relative share. Each
bar in the rank distribution is disaggregated by Age Distribution (left-facing: 18–24, 25–34, 35–54, and 55+ cohorts)
and Gender Distribution (right-facing: platform-inferred male and female shares), revealing outward mobility
patterns that vary across destinations but remain predominantly concentrated in prime working ages (25–54), with
observable variation in gender balance across transatlantic, Commonwealth, and regional hubs.
Female Male0
10
20
30
40
50Percent of total emigrants (%)
 2.55%
(a) Gender composition of total
emigrants (platform-inferred
aggregates).
55+ 18 24
 25 34
 35 54
0
10
20
30
40
50Percent of total emigrants (%)
 2.45%
 23.10%
 16.71%
(b) Age composition of total emigrants.
Mobility is concentrated in prime
working ages, with comparatively low
representation in the 55+ group.
Africa Oceania Europe Asia Americas0
10
20
30
40
50Percent of total emigrants(%) 0.08%
 16.68%
 9.37%
 11.41%
(c) Regional distribution of total
emigrants (percent of global total),
ordered by share; arrows indicate
percentage-point gaps to the next
region.
FIG. 9:Figure S1. Composition of high-potential mobility .Panels report gender, age, and regional
distributions of emigrants in the LinkedIn aggregate dataset used in this study.

16
TABLE II: Definitions of destination-country predictors used in the regression.
V ariable Definition and interpretation (destination-country)
areaTotal geographic area of the destination country; a proxy for physical scale and spatial
capacity. Higher values indicate larger geographic scale.
densityPopulation density (population per unit area), capturing crowding and pressure on
infrastructure and services. Higher values typically indicate more congestion and
strain.
GDP per CapitaGross domestic product per person, reflecting average economic resources and nation-
al capacity. Higher values indicate stronger economic capacity.
DemocracyDemocracy Index (EIU), an aggregate score across electoral process and pluralism,
functioning of government, political participation, political culture, and civil liberties.
Higher values indicate more democratic institutions.
Global Gender GapGlobal Gender Gap Index (WEF), summarizing gender equality across economic par-
ticipation, educational attainment, health and survival, and political empowerment;
ranges from 0 (least equal) to 1 (most equal). Higher values indicate greater gender
equality.
Social Welfare SpendingSocial assistance expenditure (benefits plus administrative costs) aggregated across
programs and expressed as a share of GDP (most recent available year within a multi-
year window). Higher values indicate greater social support effort.
PovertyPoverty prevalence measure (share of population below a poverty threshold, or a
multidimensional poverty proxy where applicable). Higher values indicate greater
poverty prevalence.
Cost of LivingCost of living index reflecting relative prices of goods, services, and housing. Higher
values indicate higher living costs and lower affordability.
Economic FreedomEconomic freedom index capturing market openness and regulatory constraints, typi-
cally incorporating elements of rule of law, government size, regulatory efficiency, and
open markets. Higher values indicate greater economic freedom.
RemittancesRemittances received, defined as non-commercial transfers from workers abroad to
households with family ties, representing a key channel of international capital flows
and diaspora ties. Higher values indicate stronger remittance inflows.
Unemployment RateUnemployment rate, capturing the share of the labor force without work but actively
seeking employment (estimates may vary by source and methodology). Higher values
indicate weaker labor-market conditions.
EducationEducation environment proxy capturing educational attainment and access (index-
style measure drawn from global development reporting), reflecting the strength of
the local education ecosystem. Higher values indicate stronger education conditions.
Life ExpectancyLife expectancy at birth (years), a summary indicator of population health and overall
living conditions. Higher values indicate better health outcomes.
Healthcare ExpenditureHealthcare spending indicator reflecting national investment in health services; inter-
pretation may vary because higher spending can reflect greater investment or higher
system costs. Higher values indicate more healthcare spending.
Climate Change PerformanceClimate Change Performance Index style composite summarizing greenhouse gas
emissions, energy use, renewable energy transition, and climate policy strength. High-
er values indicate stronger climate performance.
Women Peace and SecurityWomen, peace, and security index capturing women’s inclusion, justice, and security.
Higher values indicate better women’s security and inclusion.
Global PeacePeace and safety composite capturing societal peacefulness and stability. Higher
values indicate more peace and stability.

17
TABLE III: OLS Regression Results for Log Total Student Mobility
V ariable Coefficient Std. Errort-statisticP>|t|
Density -1.6285 0.330 -4.934 0.000
Area 4.1479 0.179 23.153 0.000
GDP per Capita 1.8706 0.348 5.373 0.000
Democracy 1.1055 0.210 5.261 0.000
Global Gender Gap -0.6090 0.303 -2.008 0.045
Social Welfare Spending -0.2520 0.303 -0.832 0.406
Poverty -0.2979 0.225 -1.324 0.185
Cost of Living 0.6038 0.392 1.539 0.124
Economic Freedom 0.6388 0.248 2.577 0.010
Remittances 1.0732 0.206 5.198 0.000
Unemployment Rate -0.6846 0.276 -2.477 0.013
Education 0.9474 0.375 2.523 0.012
Life Expectancy -0.4806 0.307 -1.566 0.117
Healthcare Expenditure -0.5430 0.227 -2.390 0.017
Climate Change Performance 0.0674 0.203 0.332 0.740
Women, Peace, and Security -0.1046 0.384 -0.272 0.785
Global Peace 1.1536 0.246 4.685 0.000
Model Diagnostics
Observations 10,403R 2 (uncentered) 0.336
F-statistic (17, 10386) 308.9 Adj.R 2 (uncentered) 0.335
Prob (F-statistic) 0.000 Log-Likelihood -26,786
AIC 5.361e+04 BIC 5.373e+04
TABLE IV: Comparative Regression Results for Male and Female Migrants
Male Migrants F emale Migrants
V ariable Coefficient P>|t|Coefficient P>|t|
Density -0.9720 0.000 -0.6586 0.013
Area 3.4478 0.000 3.2007 0.000
GDP per Capita 1.4233 0.000 0.8960 0.001
Democracy 0.8340 0.000 0.7983 0.000
Global Gender Gap -0.7275 0.004 -0.6439 0.008
Social Welfare Spending -0.1658 0.516 -0.0262 0.914
Poverty -0.1474 0.437 -0.4357 0.016
Cost of Living 0.6211 0.060 1.0491 0.001
Economic Freedom 0.3974 0.057 0.1922 0.334
Remittances 0.9323 0.000 0.8132 0.000
Unemployment Rate -0.6749 0.004 -0.6777 0.002
Education 0.7847 0.013 0.8954 0.003
Life Expectancy -0.0761 0.769 -0.2246 0.361
Healthcare Expenditure -0.1834 0.338 0.3216 0.078
Climate Change Performance -0.0102 0.952 -0.0713 0.661
Women, Peace, and Security -0.6315 0.051 -0.4809 0.118
Global Peace 0.6911 0.001 0.3579 0.070
Diagnostics
Observations 10,403 10,403
R2 (uncentered) 0.252 0.240
F-statistic 205.9 193.2
Log-Likelihood -25,011 -24,487

18
1
 0 1 2 3 4
Male student mobility coefficient
1
0
1
2
3
4
Female student mobility Coefficient
Significant for Both
Significant for Male Only
Significant for Female Only
Not Significant
Density
Area
Gdp Per Capita
Democracy
Global Gender Gap
Social Welfare Spending
Poverty
Cost Of Living
Economic Freedom
Remittances
Unemployment Rate
Education
Life Expectancy
Healthcare Expenditure
Climate Change Performance
Women, Peace And Security
Global Peace
FIG. 10:Comparative drivers of male versus female high-potential mobility .Scatterplot of OLS coefficient
estimates from gender-disaggregated models across 102 destination countries (male:R 2 = 0.252; female:
R2 = 0.240), with male coefficients on the horizontal axis and female coefficients on the vertical axis. Points are
colored by significance atp <0.05 (significant for both models; male only; female only; not significant). The dashed
line (y=x) denotes equal associations for men and women, and the vertical/horizontal reference lines mark zero
effects.
