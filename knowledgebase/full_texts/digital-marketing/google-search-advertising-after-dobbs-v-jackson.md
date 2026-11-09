---
title: Google Search Advertising after Dobbs v. Jackson
url: https://arxiv.org/abs/2507.06640
category: digital-marketing
subcategory: empirical
date: 2025-07
venue: ''
authors:
- Yelena Mejova
- Ronald E. Robertson
- Catherine A. Gimbrone
- Sarah McKetta
source: arxiv
pdf_url: https://arxiv.org/pdf/2507.06640
pages: 8
chars: 44086
fetched_at: '2026-11-08T13:14:33+00:00'
kb_version: 1
---

# Google Search Advertising after Dobbs v. Jackson

Google Search Advertising after Dobbs v. Jackson
Yelena Mejova
ISI F oundation
Turin, Italy
yelenamejova@acm.org
Ronald E. Robertson
Cyber Policy Center
Stanford University
Stanford, CA, USA
rer@acm.org
Catherine A. Gimbrone
Department of Epidemiology
Columbia University
New York, NY , USA
ag2246@cumc.columbia.edu
Sarah McKetta
Department of Population Medicine
Harvard Medical School and
Harvard Pilgrim Healthcare Institute
Boston, MA, USA
sarahmcketta@fas.harvard.edu
Abstract—Search engines have become the gateway to in-
formation, products, and services, including those concerning
healthcare. Access to reproductive health has been especially
complicated in the wake of the 2022 Dobbs v. Jackson decision
by the Supreme Court of the United States, splintering abortion
regulations among the states. In this study, we performed an
audit of the advertisements shown to Google Search users seeking
information about abortion across the United States during
the year following the Dobbs decision. We found that Crisis
Pregnancy Centers (CPCs)–organizations that target women with
unexpected or “crisis” pregnancies, but do not provide abortions–
accounted for 47% of advertisements, whereas abortion clinics
– for 30%. Advertisements from CPCs were often returned for
queries concerning information and safety. The type of adver-
tisements returned, however, varied widely within each state,
with Arizona returning the most advertisements from abortion
clinics and other pro-choice organizations, and Minnesota the
least. The proportion of pro-choice vs. anti-choice advertisements
returned also varied over time, but estimates from Staggered
Augmented Synthetic Control Methods did not indicate that
changes in advertisement results were attributable to changes
in state abortion laws. Our findings raise questions about the
access to accurate medical information across the U.S. and point
to a need for further examination of search engine advertisement
policies and geographical bias.
Index Terms—abortion, women’s health, public health, search
engine, Google
I. I NTRODUCTION
In June 2022, The United States Supreme Court overturned
a federal right to abortion in its rule for Dobbs v. Jackson [1].
As a result, state-level abortion laws, which already varied
widely prior to the court decision [2],determine who can get
an abortion, when, and under what circumstances [3]. In the
wake of Dobbs v. Jackson, abortion became illegal under any
circumstances (i.e., a total ban) in 13 states [4]. In 4 states,
restrictions were placed on procedures as early as 6 weeks
gestation, amounting to a de facto ban, since the majority of
pregnancies are not detected until 6 weeks or later [5].
Even prior to Dobbs v. Jackson, people seeking abortions
experienced barriers to accessing care. In 2014, 18% of people
seeking abortion traveled over 50 miles each way to obtain
care [6], and since Dobbs v. Jackson, the median travel
distance has increased to 191 miles [7]. In 2023, nearly 1
in 5 abortion patients traveled out of state to access abortion
care [8]. As a result of these barriers, an increasing proportion
of abortion care has moved to telehealth and online delivery of
abortion medication [9], [10] as well as self-managed abortion.
Fig. 1. Example of two advertisements on Google Search.
Therefore, search engines have become critical tools for people
seeking abortion–not only to identify information regarding
local laws and local abortion services, but also to identify
telehealth services and information on self-managed abortion
[11]–[13]. In the wake of the Dobbs v. Jackson decision,
searches related to abortion and contraception increased, par-
ticularly in states with laws limiting abortion access [14].
Crisis pregnancy centers, or CPCs, are organizations that
have played a large patient-facing role in the anti-choice
movement for years. These businesses target patients seeking
abortion, and then often provide misinformation to discourage
abortion procedures [15]. A core part of their strategy is po-
sitioning or advertising themselves as abortion providers [16].
In the past decade, CPCs have contributed to the ”infodemic”
[17] of online misinformation about abortion efficacy, safety,
and availability–in part due to search engine optimization and
online advertising, such that CPCs are heavily represented in
Google searches for terms related to abortion [12], [17].
Advertising is an important source of revenue for Google
(for an example, see Figure 1), and paid Google adver-
tisements (a.k.a. ads) are a cost-effective form of market-
ing for businesses [18]. Buying advertising on Google is a
strategy employed by businesses and websites promulgating
misinformation and fake news [19], including CPCs [20].
Google allows advertisers to tailor their audience, such that
advertisements vary widely based both on search terms and
the location of the user searching [21]. In the context of people
seeking abortion, Google advertisements may play a large
role in paradoxically directing towards legitimate services and
misdirecting towards misinformation. While several states ban
abortion clinics from advertising their services, these bans do
arXiv:2507.06640v1  [cs.CY]  9 Jul 2025

not impact online advertisements (i.e., via Google or other
search engines) [22].
Several studies documented an increase in Google searches
related to sexual health and abortion access resulting from
the Dobbs decision. For example, analyses of Google search
trends demonstrated between a 25-62% increase in searches
using terms related to abortion or abortion medication after the
Dobbs decision was made public [14], [23]. This increase was
patterned by state abortion policy–as states became more re-
strictive, the number of searches increased in an apparent dose-
response manner [23]. Searches for vasectomy also spiked in
an apparent dose-response manner [24], [25].
Not only did people respond to the Dobbs decision by
using Google to search for information related to abortion
and sexual health, but the results and content that Google
made available to users also adapted to the changing policy
environment. Google consistently updates its algorithm to
tailor its search results; in fact, in 2019, in response to public
pressure, Google updated its advertising policy to require that
all advertisers disclose whether they offered abortion services
(to distinguish abortion providers from CPCs) [26], [27].
After this change, advertisements for abortion services were
more likely to facilitate access to abortion, though a third of
advertisements still led users to businesses that would hinder
abortion access [27].
In our prior work examining how the content of Google
search results varies by state, we used 10 abortion-related
search queries to conduct Google searches from 467 different
locations in the United States and examined the distribution of
abortion clinics and CPCs resulting from those searches [12].
We found that locations with a higher proportion of abortion
clinics yielded more search results for abortion clinics, and
that locations with fewer abortion clinics yielded more results
for CPCs. Users searching for abortion content were less likely
to encounter a result including an abortion clinic if they were
searching from a state with restrictive legislation. Overall, the
searches yielded relatively accurate information and directed
users to abortion clinics 79% of the time, and CPCs only 7% of
the time. Critically, this research did not examine the content
of advertisements, nor did it include searches after the Dobbs
v. Jackson case.
While prior research has demonstrated the use of Google
searches to identify information related to abortion services,
[11], [14] as well as the proliferation of CPC website promot-
ing misinformation in Google results, [12], [17] no research to
date has examined the content of Google advertisements that
appear in searches related to abortions, nor to what extent this
advertising content varies by US state or state abortion policy
climate.
In the present study, we use best practices in algorithm
auditing [28] to examine the content of advertisements that
would have been shown to people searching for abortion-
related content on Google after Dobbs v. Jackson. Our study
follows prior work by conducting a focused set of abortion-
related queries from a wide array of locations across the
US [12], and advances on that work by collecting a more
temporally dense dataset of searches (daily instead of weekly)
for a year following Dobbs v. Jackson. Given the dynamic
nature of the web and the constant updates that Google Search
undergoes, our dataset captures a distinct set of search results
from prior work, and does so in the wake of a historic event
impacting abortion care in the US.
II. D ATA COLLECTION AND METHODS
Queries. To collect our search data, we first obtained a set
of queries that might be used by people who are looking for
abortion-related services or information on Google Search.
Specifically, we used the set of queries developed in past
work [12], which began with the query “abortion”, and used
Google’s autocomplete search suggestions, People Also Ask,
and Related Searches features to find other possible wordings
or related queries. Our final set of 20 queries can be grouped
as follows:
1) General: abortion, abortion clinic, abortion clinic near
me, abortion clinic (localized), abortion center , abortion
center near me, abortion center (localized), pregnancy
termination
2) Informational: kinds of abortion, types of abortion, how
does abortion work
3) Safety: is abortion dangerous, is abortion safe
4) Cost: abortion cost, free abortion, does insurance cover
abortion
5) Legality: is abortion illegal in my state, is abortion legal
in my state, is abortion illegal, is abortion legal
The search queries containing “(localized)” were localized
by adding the name of the location from which the search was
going to be conducted.
Locations. We conducted the searches with our set of
queries on a daily schedule using an open source python
library called WebSearcher [29]. This library allowed us to
specify the location from which the search was conducted
(e.g., a particular US congressional voting district), which
allowed us to compare the search results returned for the exact
same query from different locations at roughly the same time.
Distinct from prior work, which used 467 counties that were
selected via stratified random sampling [12], here we used
the 435 US congressional districts as our set of locations to
search from. After combining our query and location sets,
we collected the search results for each query-location pair
every day between 2022-06-27 and 2023-06-16. In total, we
collected 1 387 550search engine result pages (SERPs) and
used the WebSearcher library to parse them and extract the
returned advertisements (if any exist on the page).
Advertisements. We extracted the advertisements from
each collected SERP, which contain the results for a particular
query, ran on a particular day, localized in a particular district.
For each ad, we obtained its text and the URL it links to, as
well as subtext (if any) and its position on the page (whether
it is shown first, second, etc.). An example of two ads can
be seen in Figure 1. Note that, because the querying was
performed in various locations and over several days, the

same ad could be returned in many SERPs. Thus, the dataset
contains a total of 3 646 559search result ads, out of which
298 662are unique (considering the ad’s URL, title, and text
snippet). We further processed the URLs to extract the top-
level domain name (such as plannedparenthood.org) in order
to aggregate the ads.
Domain Annotation. In order to characterize the organiza-
tions linked to these ads, we extracted the domain name (e.g,
plannedparenthood.org) from each ad’s URL and manually
annotated them, expanding on domain labels from prior work
[12]. Two independent experts specializing in reproductive
health policy labeled each domain (K = 0.85, indicating al-
most perfect agreement) [30], cross-checking with the Internet
Archive in cases of dead links and with a database of crisis
pregnancy centers as needed [31]. Conflicts were resolved by
consensus between the two coders, and the final set of domain
labels was:
• Abortion clinic (AC)
• Pro-choice advocacy group or research
• Pro-choice link to care
• Crisis Pregnancy Center (CPC)
• Anti-choice advocacy group or research
• Anti-choice link to care
• Other non-profit organization
• Adoption resource
• Governmental resource
• General clinic / medical services
• News & blogs
• Religious organization
• Dead link
State Abortion Laws. In order to contextualize the time
period in which we collected our searches, we compiled a list
of state-level laws active during the study period. To account
for the rapidly-changing policy environment, we iteratively
tracked these legal developments using a combination of news
coverage and databases from policy watchdogs [32], [33],
specifically noting the gestation limit (in weeks) until which
abortion could be lawfully performed in each state. In some
states, instead of restrictions based on gestation, the law speci-
fied “fetal viability,” which can range in interpretation from the
late 2nd to 3rd trimester [34]. Because the definition of fetal
viability is generally at the discretion of a medical provider,
these laws were considered to be minimally restrictive with
respect to gestational limit. The laws were categorized as a
total ban (most restrictive), 1st trimester (0-12 weeks), 2nd
trimester (13-26), or 3rd trimester/fetal viability (27-40 weeks,
least restrictive). We have made this information available to
the research community. 1
Statistical Methods. We employed Staggered Augmented
Synthetic Control Methods (SASCM) to estimate the average
treatment effect on the treated (ATT) of state-level abortion
policy changes on ad content [35]. This method attempts to
address causal inference challenges when policies are adopted
1https://tinyurl.com/AbortionLawsByStateAfterDobbs
0.0 0.2 0.4 0.6 0.8 1.0
proportion of ad kind
is abortion legal in my state [L]
is abortion legal [L]
is abortion illegal in my state [L]
is abortion illegal [L]
does insurance cover abortion [C]
free abortion [C]
abortion cost [C]
is abortion safe [S]
is abortion dangerous [S]
how does abortion work [I]
types of abortion [I]
kinds of abortion [I]
pregnancy termination [G]
abortion clinic (localized) [G]
abortion clinic near me [G]
abortion clinic [G]
abortion center (localized) [G]
abortion center near me [G]
abortion center [G]
abortion [G]
abortion clinic
pro-choice advocacy/research
pro-choice link to care
crisis pregnancy center
anti-choice advocacy/research
anti-choice link to care
adoption resource
general medical clinic
other non-profit
news or blog
government resource
religious organization
broken link
0 1 2 3 4
average # ads in SERP
Fig. 2. Proportion of ad results that are of a particular type (bars; bottom
y-axis) and average number of ad results in a SERP (diamonds; top y-axis),
by query (type in brackets; General, Informational, Safety, Cost, Legality).
by different units at different times. For these analyses, we
chose to dichotomize policies as ban (including 6-week gesta-
tional limits, given they amount to a de facto abortion ban [5])
or no ban. We chose this more parsimonious approach, rather
than the categorical approach to coding policies, both in order
to examine the differences across the most extreme restrictions
and to provide a sufficient number of both treatment and
control states. Ads were dichotomized as proportion pro-
choice or anti-choice ad content. Both policies and ad content
were further aggregated to the weekly level, with weekly
policies coded based on whichever policy was in effect for
the majority of days within that week. We tested two models
based on policy adoption: (1) treatment states that restricted
policies from no ban to ban (Idaho, West Virginia) and (2)
treatment states that relaxed policies from ban to no ban (South
Carolina, Ohio) during the study period. Control states were
selected so that they matched the pre-study period policies in
treatment states and did not change policy categories during
the study period.
III. R ESULTS
A. Categories of Ads Returned
Overall, the most frequent category of domains in our
data was CPCs at 46.8%, followed by abortion clinics (AC,
29.9%), pro-choice advocacy or research (16.4%), and anti-
choice advocacy or research (2.4%). Aggregating over the
study period and across locations, we grouped the results
by query type and found substantial variance in the number

of ads returned and the proportion of ad types (Figure 2).
First, the number of ads (the black diamonds, top x axis)
ranged from just above 1 (in response to “does insurance cover
abortion”) to around 3.5 (in response to the informational
queries). Second, queries associated with information seeking
(“types/kinds of abortion”, “how does abortion work”) and its
potential dangers (“is abortion dangerous/safe”) returned the
largest proportion of CPC and anti-choice ads (colored bars,
bottom x axis). Third, queries about the legality of abortion,
returned the largest proportions of pro-choice advocacy ads.
Fourth, general queries about abortion (including those related
to abortion centers or clinics) returned a notable proportion of
CPC ads (ranging from: 19% to 40%).
Next, we examined SERPs returned for queries executed
from each state (aggregated over all queries, times, and loca-
tions within each state). Similar to Figure 2, Figure 3 shows
the percentage of each domain type and the average number
of ads in a SERP, now grouped by state instead of query
type. States are sorted by the percentage of ads that were
labeled as AC, pro-choice advocacy/research, or pro-choice
link to care. We found that states with the largest proportion of
advertising for either ACs or pro-choice resources (and lower
proportions of ads for CPCs and anti-choice websites) were
Arizona, Massachusetts, Utah, New Hampshire, Washington,
and Arkansas. Conversely, states with the smallest proportion
of such ads (and proportionally more CPCs and anti-choice
websites) included Minnesota, Kansas, Wisconsin, followed by
Delaware, Ohio, Alabama, and Hawaii. Upon visual inspection
of these results, no apparent state pattern emerged with regard
to notable state features – i.e., geographical region, population
density, or state conservatism, though we did not formally test
associations with state characteristics.
The overall number of ads shown to users in different
states varied from approximately 2 to 3.5 per SERP. Further,
the average number of ads per state was associated with the
distribution of ad content per state. That is, states with more
ads generally returned fewer pro-choice resources (Pearson
correlation r = -0.49, p = 0.0003) and more anti-choice
resources (r = 0.48, p = 0.0004).
Figure 4 shows the type of ads returned each day in our
study period by count (top) and as percentages (bottom). We
found wide variation in the total number of ads returned across
all searches from one day to another, peaking in February 2023
at over 15,000. Although there was some heterogeneity in the
proportion of anti-choice ads versus pro-choice ads over time,
the balance between the two remained largely similar across
time, with ACs and pro-choice resources making up 47.7% of
daily ads (std=0.054), and anti-choice ads comprising 49.9%
(std=0.053).
B. Top Advertisers
Table I shows the top 30 domains, out of a total of 7,969
unique domains across the full dataset, the proportion of ads
that led to those domains, and their respective domain type
labels. Overall, no individual domain dominated the share of
ad content, with plannedparenthood.org (an American
0.00 0.25 0.50 0.75 1.00
proportion of ad kind
Minnesota
Kansas
Wisconsin
Delaware
Ohio
Alabama
Hawaii
Iowa
Michigan
Florida
Nebraska
Alaska
North Dakota
Indiana
Illinois
North Carolina
Oregon
Maryland
Missouri
Kentucky
Wyoming
Pennsylvania
West Virginia
Mississippi
California
New Jersey
Nevada
Virginia
New Mexico
South Carolina
Montana
Oklahoma
Louisiana
Colorado
Idaho
T exas
Vermont
T ennessee
Connecticut
South Dakota
Maine
Georgia
Rhode Island
New York
Arkansas
Washington
New Hampshire
Utah
Massachusetts
Arizona
abortion clinic
pro-choice advocacy/research
pro-choice link to care
crisis pregnancy center
anti-choice advocacy/research
anti-choice link to care
adoption resource
general medical clinic
other non-profit
news or blog
government resource
religious organization
broken link
0 1 2 3 4
average # ads in SERP
Fig. 3. Proportion of ad results that are of a particular type (bars; bottom
x-axis) and average number of ad results in a SERP (diamonds; top x-axis),
by state. The states are ordered by the total proportion of abortion clinic and
pro-choice advocacy/research or link to care ads.
nonprofit that provides reproductive and sexual healthcare
and sexual education in the U.S. and globally) exhibiting a
frequency (0.161%), more than double that of the second
most popular domain ( lifechoicesinc.org; 0.063%).
The remaining top advertisers included 15 CPCs, 5 ACs, 6
pro-choice related sites, and 2 anti-choice related sites.
Whereas the top advertising AC provider ( planned-
parenthood.org) is an organization spanning the whole
country, the CPCs at the top of this list are often specific
to a single location. For instance, lifechoicesinc.org

0
5000
10000
15000# of ads
2022-07 2022-09 2022-11 2023-01 2023-03 2023-05 2023-07
0
50
100% of ads
Fig. 4. V olume of ads returned (top) and percentage of ads (bottom) by kind.
Colors are the same as those used in Figure 2: shades of green correspond to
abortion clinics and pro-choice resources while shades of red correspond to
CPCs and anti-choice resources.
TABLE I
TOP 30 DOMAINS IN THE DATASET
Domain Kind % ads
plannedparenthood.org ac 0.161
lifechoicesinc.org cpc 0.063
states.guttmacher.org pro-choice advocacy 0.063
anchorofhopewi.org cpc 0.047
lifeclinic.org cpc 0.040
reproductiverights.org pro-choice advocacy 0.038
prestonwoodpregnancy.org cpc 0.031
noisefornow.org pro-choice advocacy 0.023
guttmacher.org pro-choice advocacy 0.020
alphacentermychoice.org cpc 0.019
fpawomenshealth.com ac 0.017
info.carafem.org ac 0.016
hesperian.org pro-choice advocacy 0.014
womenscarecenter.org cpc 0.013
nyc.gov government resource 0.013
wholewomanshealth.com ac 0.012
abortionclinicservicesatlantaga.com ac 0.011
care.wholewomanshealth.com ac 0.010
abortiontestimonials.com anti-choice advocacy 0.010
freeabortionalternatives.com cpc 0.010
lifeforwardcincy.org cpc 0.009
scprc.com cpc 0.009
lifechoicesmemphis.org cpc 0.009
carenetfrederick.org cpc 0.009
arkadelphiapregnancy.com cpc 0.009
alternativespc.org cpc 0.008
womenonweb.org pro-choice link to care 0.008
youroptions.com anti-choice advocacy 0.007
go.fcws.org cpc 0.007
go.option1.org cpc 0.007
lists its location in Conway, AR, anchorofhopewi.org in
Sheboygan, WI and lifeclinic.org lists 3 locations in
Michigan state.
C. Relation to Laws
Next, we examined the search results with respect to each
state’s abortion policy environment. In Figure 5 we compare
the distribution of different ad types separately for each policy
environment, separated into ban, or limit at first, second,
or third trimester. We examined the four most prevalent
categories of ads in our dataset: ACs, CPCs, pro-choice, and
anti-choice advocacy/research. On average, the number of AC
ads was highest in states with first trimester ban, whereas
ban tri_1 tri_2 tri_3
0
2
4
6
0.83 1.05 0.68 0.80
ac
ban tri_1 tri_2 tri_3
1.03 1.11 1.36 1.29
cpc
ban tri_1 tri_2 tri_3
0
2
4
6
0.37 0.34 0.48 0.45
pro-choice advocacy
ban tri_1 tri_2 tri_3
0.09 0.04 0.05 0.06
anti-choice advocacy
number of ads in SERP
abortion limit
Fig. 5. Distribution of ad counts per SERP (y-axis) for four of the main
domain type labels (see plot titles) in states with different abortion limits (x-
axis). The mean of each distribution is shown below each x-axis tick label.
the number CPC ads generally grew with increasing trimester
limits. Given the large corpus of data, tests of difference
were all highly significant ( p < 0.01), but the magnitudes
of differences were fairly modest. The distribution for each
ad type was similar across policy environments, regardless of
gestational limits. Notably, and not visible in this plot, we
found that states with total bans had a higher proportion of
AC and pro-choice advocacy advertisements than states with
first trimester gestational limits.
We then explored the relationship between the types of
ads returned for our abortion-related queries and the states in
which the searches were executed. Figure 6 shows the total and
proportional volume for the four treatment states used in the
SASCM: Idaho, West Virginia, South Carolina, and Ohio. Note
that the raw number of results (bottom panels) depends on the
number of voting districts in each state, and thus these are
not comparable between states. Instead, we direct the reader
to examine the trends in the proportion of advertisement types
within each state (top panels). Plots for all states can be viewed
in the online supplementary material. 2 In these plots, we also
indicate the time at which a new policy takes effect (vertical
blue lines, along with text specifying the new abortion term
limit).
Clear patterns in changes of ad prevalence in response
to policy changes were not visibly evident. Of note, Idaho
experienced a marked increase in the relative proportion of
CPC ads toward the end of the study period, however this was
not precipitated by an abortion policy change. Findings from
SASCM models using binarized ad and policy variables ag-
gregated to the weekly-level further confirmed these findings,
with small effect sizes that did not reach statistical significance
for the proportion of pro-choice ads (overall ATT for restrictive
model = −0.01 [SE = 0.06], overall ATT for relaxed model
2https://tinyurl.com/AbortionAdsByState

0
50
100
% of ads
ban
Idaho (starts at fetal viability)
2022-07 2022-09 2022-11 2023-01 2023-03 2023-05 2023-07
0
100
# of ads
0
50
100
% of ads
ban
West Virginia (starts at 22w)
2022-07 2022-09 2022-11 2023-01 2023-03 2023-05 2023-07
0
100
# of ads
0
50
100
% of ads
6w 22w 6w, 22w
South Carolina (starts at 22w)
2022-07 2022-09 2022-11 2023-01 2023-03 2023-05 2023-07
0
250
# of ads
0
50
100
% of ads
22w
Ohio (starts at 6w)
2022-07 2022-09 2022-11 2023-01 2023-03 2023-05 2023-07
0
500
# of ads
Fig. 6. V olume of ads returned (bottom) and proportion of ads (top) by kind
for select states. Colors as in previous figures. Changes in laws indicated by
vertical blue lines and text indicates the new abortion term limit.
= −0.06 [SE = 0.14]). Figure 7 shows plots of weekly ATT
estimates for each of these models.
IV. D ISCUSSION
This study assessed trends in ads returned by Google Search
for abortion-related queries during the year following the
Dobbs v. Jackson decision in the US. Our analysis revealed
several key patterns in advertisement content. First, ad content
was sensitive to query type, with informational and safety-
related queries about abortion returning the highest propor-
tion of ads related to CPCs and anti-choice organizations.
Conversely, queries about abortion legality returned a higher
proportion of content related to pro-choice organizations.
Second, we found a relatively consistent balance between pro-
choice and anti-choice advertising content across all queries
over time. Third, state-level analyses revealed geographic
variation in ad content, however, we have not attempted to link
it to particular demographic or sociopolitical characteristics.
Notably, states with total abortion bans had a higher proportion
of AC ads. Further the average number of AC ads was
highest for states with first trimester gestational limits and
Fig. 7. SASCM models measuring effect of law change on the proportion
of pro-choice ads. Top: Relaxed model with SC and OH as treatment states.
Bottom: Restricted model with WV and ID as treatment states.Note that the
weekly aggregation of policies eliminated two brief policy changes in South
Carolina that lasted less than the majority of the week. Vertical dashed lines
indicate the policy change. Solid black lines represent weekly average ATT
estimates over time, with 95% confidence intervals in grey. Solid grey lines
represent weekly ATT estimates over time per treatment state. An ATT of 0
is a null effect.
the average number of CPC ads was positively correlated
with increasing gestational limits, suggesting possible reactive
advertising strategies. Despite these patterns, our statistical
analyses found no significant relationship between state policy
changes and shifts in ad content over time.
The dominance of CPC ads in response to informational
and safety-related abortion queries raises concern about access
to accurate medical information among those seeking care.
Users seeking basic information about abortion procedures,
who may be most vulnerable to misinformation, would be
disproportionately exposed to ads from organizations that do
not provide abortion services and often actively discourage
them [36]. Access to accurate medical information varies
significantly based on query type and location, potentially
limiting access to time-sensitive care when users need it most
[14]. Moreover, the increased presence of CPC ads in areas
with higher gestational limits suggests a targeting of regions
where abortion services are more legally accessible, potentially
aiming to intercept care-seeking individuals [37].
These findings also highlight the role of digital advertising
policies in shaping access to information seeking around
abortion. Despite Google’s patchy efforts to label abortion
providers, which were rolled out in June 2022 [38], CPCs
maintain a strong ad presence on the platform. The consistent
presence of CPC ads alongside ads for medical services,
particularly in response to searches about abortion information
and safety, therefore may exacerbate confusion among users
seeking medical information [36].
Examination of state-level data revealed unexpected patterns
in abortion-related ad content. Further, despite shifts in state

abortion policies, we did not find significant reciprocal changes
in the proportion pro-choice advertisements over time. How-
ever, some variations emerged when analyzing ad composition
relative to different policy environments. Notably, states with
total abortion bans showed a higher prevalence of AC ads,
while states with later-term abortion limits saw a greater
average number of CPC ads. This suggests that advertising
strategies may be shaped more by market conditions than by
immediate policy changes. This may also indicate strategic
advertising plans, such that pro-choice organizations prioritize
outreach in restrictive environments to maintain awareness
of services that may be available in neighboring states [39].
Ultimately, we found that access to accurate reproductive
health information via search engines is unevenly distributed
across the US, potentially reinforcing existing disparities in
abortion access [12].
This study has many methodological strengths. First, it
provides a unique analysis of abortion-related ad patterns
across the US during the year following the Dobbs v. Jackson
decision, spanning 435 congressional districts and including
over 3.6 million ads. Second, our systematic data collection
process captured daily advertising patterns across multiple
query types, from general searches to specific questions about
legality, safety, and cost. Third, our domain classification
approach achieved high inter-rater reliability and expanded
upon previous labeling schemes to capture nuanced distinc-
tions between different types of abortion-related resources.
Fourth, our year-long data collection period, combined with
daily tracking of state policy changes, enabled analysis of
advertising patterns across varying regulatory environments.
Several limitations should also be acknowledged when
interpreting these results. Our data collection was confined to
Google search results and did not account for information dis-
semination through other digital platforms, indicating a need
for research examining advertising patterns across broader
online spaces. Our query set, though systematically developed
through Google’s search features, may not have captured the
variance in real users’ queries. Furthermore, the requirements
of SASCM models, specifically the need for adequate pre-
treatment periods and comparable control states, limited our
analysis of policy effects to a subset of states experiencing
policy changes during the study period.
Future work should evaluate the effectiveness of current
advertisement labeling practices and their impact on informa-
tion access. Studies incorporating real-world search patterns
and user-focused investigations could provide insight into
individual-level engagement with abortion-related advertising
under ecologically-valid conditions [40]–[42]. Additional sta-
tistical approaches could examine associations between ad-
vertising patterns and state characteristics, including demo-
graphic, political, and healthcare access variables. Finally,
while our analysis covered a substantial period following
Dobbs, continued monitoring of online information ecosys-
tems is needed to understand long-term shifts in abortion-
related advertising strategies [43], [44].
Our findings demonstrate that Google search advertising
patterns for abortion-related queries vary systematically by
query type and location, with CPC advertisements appearing
prominently in response to several queries. This observed
prominence of CPC advertisements in search results may
create barriers for users seeking time-sensitive abortion-related
information and services and highlights the critical role that
digital advertising policies play in shaping access to abortion
care. These advertising patterns raise questions about user ac-
cess to accurate abortion-related information on Google Search
and suggest a need for further examination of search engine
advertising policies, specifically regarding the placement of
advertisements from organizations that do not provide medical
services.
V. A CKNOWLEDGMENTS
We would like to acknowledge Kara E. Rudolph, PhD,
Columbia University, for her consultation on statistical meth-
ods, and Andrew Schwartz for his assistance in putting to-
gether the database of abortion-related policy changes follow-
ing Dobbs v. Jackson. The search data used in this study
were collected using machines at Northeastern University
that are administered by the authors’ collaborators, with their
permission. Northeastern University was given permission to
query Google Search automatically for research purposes.
Google did not review our research design, nor had any review
rights with respect to the manuscript. Jeffrey Hancock was the
faculty director of this work at Stanford.
REFERENCES
[1] T. Dobbs, “Dobbs v. jackson women’s health organization,” Supreme
Court of the United States , vol. 597, 2022.
[2] A. Llamas, L. Borkowski, and S. F. Wood, “Public health impacts of
state-level abortion restrictions,” Overview of Research and Policy in the
United States , pp. 1–38, 2018.
[3] M. F. Davis, “The state of abortion rights in the us,” International
Journal of Gynecology & Obstetrics , vol. 159, no. 1, pp. 324–329, 2022.
[4] A. McCann and A. Walker, “Tracking abortion bans across the
country,” The New York Times , 2025. [Online]. Available: https:
//www.nytimes.com/interactive/2024/us/abortion-laws-roe-v-wade.html
[5] K. Watson and C. Angelotta, “The frequency of pregnancy recognition
across the gestational spectrum and its consequences in the united
states,” Perspectives on Sexual and Reproductive Health , vol. 54, no. 2,
p. 32, 2022.
[6] L. Fuentes and J. Jerman, “Distance traveled to obtain clinical abortion
care in the united states and reasons for clinic choice,” Journal of
Women’s Health, vol. 28, no. 12, pp. 1623–1631, 2019.
[7] L. McGuinn, M. Quasebarth, M. Daniel, L. Hasselbacher, and K. Rivlin,
“Changes in distance traveled among chicago abortion fund callers from
2020-2023,” Contraception, vol. 139, p. 110609, 2024.
[8] F. Sheets, “The high toll of us abortion bans: Nearly one in five patients
now traveling out of state for abortion care,” Policy Analysis, 2023.
[9] L. R. Koenig, A. Becker, J. Ko, and U. D. Upadhyay, “The role of
telehealth in promoting equitable abortion access in the united states:
spatial analysis,” JMIR Public Health and Surveillance , vol. 9, p.
e45671, 2023.
[10] C. Brown, C. E. Neerland, E. V . Weinfurter, and M. A. Saftner, “The
provision of abortion care via telehealth in the united states: A rapid
review,” Journal of Midwifery & Women’s Health , vol. 68, no. 6, pp.
744–758, 2023.
[11] L. Flores, Z. Kelani, C. Chandwani, and S. D. Young, “Internet searches
for self-managed abortion after roe v wade overturned,” JAMA surgery,
vol. 158, no. 9, pp. 976–977, 2023.

[12] Y . Mejova, T. Gracyk, and R. E. Robertson, “Googling for abortion:
Search engine mediation of abortion accessibility in the united states,”
Journal of Quantitative Description: Digital Media , vol. 2, 2022.
[Online]. Available: https://journalqd.org/article/view/2752
[13] J. Jerman, T. Onda, and R. K. Jones, “What are people looking for
when they google “self-abortion”?” Contraception, vol. 97, no. 6, pp.
510–514, 2018.
[14] S. Gupta, B. Perry, and K. Simon, “Trends in abortion-and contraception-
related internet searches after the us supreme court overturned consti-
tutional abortion rights: how much do state laws matter?” in JAMA
health forum , vol. 4, no. 4. American Medical Association, 2023,
pp. e230 518–e230 518.
[15] C. Thomsen, Z. Levitt, C. Gernon, and P. Spencer, “Presence and
absence: Crisis pregnancy centers and abortion facilities in the con-
temporary reproductive justice landscape,” Human Geography , vol. 16,
no. 1, pp. 64–74, 2023.
[16] J. Arthur, A. Downey, A. Katelieva, O. Jensen, K. Mitchell, N. Teale,
and T. Phelps Bondaroff, “Examining the websites of anti-choice crisis
pregnancy centres,” 2023.
[17] S. L. Pagoto, L. Palmer, and N. Horwitz-Willis, “The next infodemic:
abortion misinformation,” Journal of Medical Internet Research , vol. 25,
p. e42582, 2023.
[18] R. Almestarihi, A. Ahmad, R. Frangieh, I. Abu-AlSondos, K. Nser, and
A. Ziani, “Measuring the roi of paid advertising campaigns in digital
marketing and its effect on business profitability,” Uncertain Supply
Chain Management , vol. 12, no. 2, pp. 1275–1284, 2024.
[19] E. Papadogiannakis, P. Papadopoulos, E. P. Markatos, and N. Kourtellis,
“Who funds misinformation? a systematic analysis of the ad-related
profit routines of fake news sites,” in Proceedings of the ACM Web
Conference 2023, 2023, pp. 2765–2776.
[20] J. J. Swartz, C. Rowe, T. Truong, A. G. Bryant, J. E. Morse, and G. S.
Stuart, “Comparing website identification for crisis pregnancy centers
and abortion clinics,” Women’s Health Issues , vol. 31, no. 5, pp. 432–
439, 2021.
[21] I. Ahmadi, N. Abou Nabout, B. Skiera, E. Maleki, and J. Fladen-
hofer, “Overwhelming targeting options: Selecting audience segments
for online advertising,” International Journal of Research in Marketing ,
vol. 41, no. 1, pp. 24–40, 2024.
[22] Temple University Center for Public Health Law Research, “Abortion
advertising restrictions,” LawAtlas.org, 2022. [Online]. Available:
https://lawatlas.org/datasets/abortion-advertising-restrictions?.com=null
[23] A. Poliak, N. Satybaldiyeva, S. A. Strathdee, E. C. Leas, R. Rao,
D. Smith, and J. W. Ayers, “Internet searches for abortion medications
following the leaked supreme court of the united states draft ruling,”
JAMA internal medicine , vol. 182, no. 9, pp. 1002–1004, 2022.
[24] R. D. Patel, J. Loloi, K. Labagnara, and K. L. Watts, “Search trends
signal increased vasectomy interest in states with sparsity of urologists
after overrule of roe vs. wade,” pp. 759–761, 2022.
[25] N. Sellke, K. Tay, H. H. Sun, A. Tatem, A. Loeb, and N. Thirumavalavan,
“The unprecedented increase in google searches for “vasectomy” after
the reversal of roe vs. wade,” Fertility and Sterility , vol. 118, no. 6, pp.
1186–1188, 2022.
[26] L. E. Dodge, S. J. Phillips, D. T. Neo, S. Nippita, M. E. Paul, and
M. R. Hacker, “Quality of information available online for abortion self-
referral,” Obstetrics and gynecology , vol. 132, no. 6, p. 1443, 2018.
[27] L. E. Dodge, R. Aguayo, C. Dutton, and M. R. Hacker, “The influence
of advertising policy on information available online for abortion self-
referral,” Contraception, vol. 114, pp. 61–66, 2022.
[28] D. Metaxa, J. S. Park, R. E. Robertson, K. Karahalios, C. Wilson,
J. Hancock, and C. Sandvig, “Auditing Algorithms: Understanding
Algorithmic Systems from the Outside In,” F oundations and Trends®
in Human–Computer Interaction , vol. 14, no. 4, pp. 272–344, 2021.
[29] R. E. Robertson and C. Wilson, “WebSearcher: Tools for Auditing Web
Search,” in Proceedings of Computation + Journalism Symposium (C+J
’20), 2020, p. 4.
[30] J. R. Landis and G. G. Koch, “The measurement of observer agreement
for categorical data,” biometrics, pp. 159–174, 1977.
[31] S. A and L. D, “Crisis pregnancy center map.” [Online]. Available:
https://www.cpcmap.com
[32] KFF, “The independent source for health policy research, polling, and
news.” https://www.kff.org/, 2025.
[33] NARAL, “Reproductive freedom for al.”
https://reproductivefreedomforall.org/, 2025.
[34] L. Han, M. I. Rodriguez, and A. B. Caughey, “Blurred lines: disentan-
gling the concept of fetal viability from abortion law,” Women’s Health
Issues, vol. 28, no. 4, pp. 287–288, 2018.
[35] E. Ben-Michael, A. Feller, and J. Rothstein, “Synthetic controls with
staggered adoption,” Journal of the Royal Statistical Society Series B:
Statistical Methodology , vol. 84, no. 2, pp. 351–381, 2022.
[36] M. N. Montoya, C. Judge-Golden, and J. J. Swartz, “The problems with
crisis pregnancy centers: reviewing the literature and identifying new
directions for future research,” International Journal of Women’s Health,
pp. 757–763, 2022.
[37] C. Polcyn, S. Swiezy, L. Genn, P. Wickramage, N. Siddiqui, C. Johnson,
P. Nair, C. Bernard, and V . Miller, “Truth and transparency in crisis
pregnancy centers,” Women’s Health Reports , vol. 1, no. 1, pp. 224–
226, 2020.
[38] J. Love and D. Alba, “Google search is failing to label ads from anti-
abortion crisis pregnancy centers,” Bloomberg Technology + Equality ,
2022. [Online]. Available: https://www.bloomberg.com/graphics/
2022-google-search-abortion-clinic-crisis-pregnancy-center-ads/
[39] B. Dahlberg, “The role of independent funds to
help people access abortion is growing,” NPR,
2022, accessed: 2025-02-14. [Online]. Available:
https://www.npr.org/sections/health-shots/2022/07/25/1112938261/
the-role-of-independent-funds-to-help-people-access-abortion-is-growing
[40] A. Feal, J. Gleason, P. Goel, J. Radford, K.-C. Yang, J. Basl, M. Meyer,
D. Choffnes, C. Wilson, and D. Lazer, “Introduction to National Internet
Observatory,” in Workshop Proceedings of the 18th International AAAI
Conference on Web and Social Media , 2024.
[41] K. T. Greene, N. Pisharody, L. A. Meyer, M. Pereira, R. Dodhia, J. L.
Ferres, and J. N. Shapiro, “Current engagement with unreliable sites
from web search driven by navigational search,” Science Advances ,
vol. 10, no. 44, p. eadn3750, 2024.
[42] R. E. Robertson, J. Green, D. J. Ruck, K. Ognyanova, C. Wilson, and
D. Lazer, “Users choose to engage with more partisan news than they
are exposed to on Google Search,” Nature, vol. 618, pp. 342–348, 2023.
[43] K. Munger, “The limited value of non-replicable field experiments in
contexts with low temporal validity,” Social Media + Society , vol. 5,
no. 3, Apr. 2019.
[44] ——, “Temporal validity as meta-science,” Research & Politics, vol. 10,
no. 3, p. 20531680231187271, 2023.
