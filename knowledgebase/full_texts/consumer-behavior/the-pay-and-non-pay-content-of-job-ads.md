---
title: The Pay and Non-Pay Content of Job Ads
url: https://arxiv.org/abs/2407.13204
category: consumer-behavior
subcategory: empirical
date: 2024-07
venue: ''
authors:
- Richard Audoly
- Manudeep Bhuller
- Tore Adam Reiremo
source: arxiv
pdf_url: https://arxiv.org/pdf/2407.13204
pages: 95
chars: 266759
fetched_at: '2026-11-08T13:08:56+00:00'
kb_version: 1
---

# The Pay and Non-Pay Content of Job Ads

The Pay and Non-Pay Content of Job Ads ∗
Richard Audoly† Manudeep Bhuller‡ Tore Adam Reiremo§
First Version: July 2024
This Version: May 2026
Abstract
How informative are job ads about the actual pay and non-pay attributes offered
by employers? Using a comprehensive database of job ads posted by Norwegian em-
ployers, we develop a methodology to systematically classify the pay and non-pay job
attributes advertised in vacancy texts. About 60% of job ads provide pay-related
information and nearly all ads feature information on non-pay attributes. We link
these advertised attributes to the employers posting the ads and validate this informa-
tion against revealed-preference measures of employer quality, realized attributes, and
choices from a survey experiment. All three strategies confirm that job ads provide
reliable signals of employer quality. We then incorporate the detailed job attributes in
a monopsony framework and quantify their contribution to labor market inequality.
Keywords: amenities, non-pecuniary job attributes, compensating differentials, worker mo-
bility, information frictions, monopsony, job ads, text analysis
JEL: J23, J32, J33, J62, J63
∗Acknowledgements: The views below are those of the authors and do not necessarily reflect the position
of the Federal Reserve Bank of New York or the Federal Reserve System. We thank Statistics Norway and the
Norwegian Public Employment Agency (NA V) for providing us access to their data. For helpful feedback and
suggestions, we are thankful to Christoph Heidrich, Lisa Kahn, Gizem Kosar, Thomas Le Barbanchon, Steve
Machin, Alan Manning, Ryan Michaels, Chris Moser, Suresh Naidu, Barbara Petrongolo, Giorgio Topa, as
well as conference and seminar participants at the F AIR Midway Conference 2022 (Tromsø), the 2023 Nordic
Meeting on Register Data and Economic Modelling (Oslo), the 2023 EEA-ESEM Meetings (Barcelona), the
3rd CRC Labor Workshop (Mannheim), the Federal Reserve System Applied Micro Conference (Chicago), the
2024 CEPR Annual Symposium in Labour Economics (London), the 2024 NBER SI Labor Studies/Personnel
Economics Meeting (Cambridge), the NHH/F AIR CELE Meeting, the 2025 Econometric Society World
Congress (Seoul), and the 2026 ASSA/AEA Annual Meeting (Philadelphia). This project has received
funding from the European Union’s Horizon Europe Research and Innovation Programme under Grant
Agreement No. 101043127 and the Norwegian Research Council under Grant Agreement No. 275123.
†Federal Reserve Bank of New York. E-mail: richard.audoly@ny.frb.org
‡University of Oslo, Statistics Norway, CEPR, IZA, CESifo. E-mail: manudeep.bhuller@econ.uio.no
§Norwegian School of Economics. E-mail: tore.reiremo@nhh.no
arXiv:2407.13204v3  [econ.GN]  26 May 2026

1 Introduction
There is a long tradition in labor economics of seeing jobs as more than pay [e.g.,Brown,
1980, Duncan and Holmlund, 1983, Rosen, 1986]. Phrases such as “compensating differ-
entials,” “amenities,” or “workplace differentiation” all capture the notion that jobs are
multidimensional bundles of attributes that workers trade off against pay when considering
job opportunities with alternative employers (see, e.g.,Mas [2025] for a recent overview).
Such trade-offs can be substantial: recent experimental evidence shows that workers at a US
call center are willing to give up 8% of their salary for the option to work from home [Mas
and Pallais, 2017], while undergraduates at a top US university would accept a 5.1% salary
cut for jobs that offer the possibility to work flexible hours [Wiswall and Zafar, 2018].
What is unclear from this evidence, however, is how workers gather information on the
pay and amenity attributes of a job while exploring their options in the labor market. The
content of job postings represents one important search channel through which workers
can gather information about these attributes.1 But as employers ultimately decide on the
content of publicly advertised job postings, it remains an open question whether such content
reflects the actual pay and amenities associated with different employers.
In this paper, we study in detail the information content of job ads. Our first objective
is to provide a detailed description of the pay and non-pay content advertised by employers
in their vacancies. Our second objective is to analyze how employers of varying quality, as
characterized by several alternative measures, systematically advertise different types of pay
and non-pay attributes in their job ads. Our third and final objective is to separately quan-
tify the contribution of advertised amenities to labor market inequality, providing empirical
content to the amenity index typically featured in structural models of the labor market.
To characterize the distribution of job attributes advertised in job ads, we use the near-
universe of publicly posted vacancies in Norway. A key contribution is to systematically
extract a broad range of pay and non-pay job attributes from these texts. Using natural
language processing tools, we identify nearly fifty commonly advertised pay and non-pay
attributes, such as “competitive pay,” “flexible work hours,” and “nice work environment.”
We build a large collection of unique natural language expressions associated with each
attribute that we make publicly available.2
We find that about 60% of job ads provide pay-related information, with 30% revealing
1Recently, Carrillo-Tudela et al. [2023] provide survey evidence from Germany showing that 55.3% of
firms used job postings in their latest hire, while 88.1% of workers used job postings in their search process.
Notably, however, job postings are not exclusive of other search methods, such as social networks. Carrillo-
Tudela et al. [2023] find that firms and workers use, respectively, 1.9 and 2.3 channels on average.
2The full list is available at: https://zenodo.org/records/14973628.
1

explicit salary information, such as an actual salary figure, a salary bracket, or referring
to a collective bargaining agreement. Nearly all ads also feature non-pay amenities, such
as contract duration, irregular hours, shift work, flexible work hours, workplace attributes,
task-related attributes, or other minor perks. These results indicate that employers advertise
a broad range of pay and non-pay attributes when attracting workers.
Thekeystrengthofourdatasetisthateachadcanbedirectlytracedtotheestablishment
posting the job. Using this feature of the data, we analyze the information that workers can
infer from job ads with three complementary empirical designs. First, we analyze how
advertised job attributes correlate with several revealed-preference measures of employer
quality. Second, we link ads to hires and document the concordance between advertised and
realized attributes, for the subset of attributes with clear counterparts in the register data.
Third, we present evidence from a survey experiment fielded byBhuller et al.[2024] in which
respondents state their preferences over real-world job ads rather than hypothetical jobs.
Across measures of employer quality, we find that high-quality employers are more likely
to advertise attributes typically seen as positive, such as more generous pensions, flexible
working hours, and permanent jobs, while low-quality employers tend to advertise negative
attributes, such as shift-work and temporary jobs. This holds even for less tangible job at-
tributes: high-quality employers also more often advertise a professional environment with
“good colleagues” and work involving “challenging tasks.” Similarly, we show that job ad
attributes meaningfully predict employer quality, with more than 60% of the variation ex-
plained across quality measures. This result holds after removing the variation accounted
for by industry, occupation, and location controls: job ad attributes still explain 15–20%
of the remaining dispersion in employer quality. Finally, using the linked ad-hire data we
construct, we confirm that advertised and realized job attributes generally coincide.
The survey experiment adds further evidence on the reliability of job ads as an informa-
tionchannel. Weestimatetheimpliedwillingness-to-payforthejobattributesextractedfrom
the ads. We find that our estimates have sensible signs and, for the attributes documented
in prior work, plausible magnitudes, indicating that respondents rely on this information in
making their choices. Moreover, based solely on the ad text, respondents are also more likely
to state that they prefer job ads posted by higher-quality employers, as measured with a
revealed-preference approach using information for the population at large.
Having documented that job ads contain useful information about employer quality, we
quantify the contribution of advertised attributes to employer-level inequality in the labor
market. We incorporate these attributes into an otherwise standard static monopsony model
inwhichworkershaveheterogeneouspreferencesoveralternativeemployers[ Cardetal. ,2018,
Lamadon et al., 2022]. With amenity information derived from the ads, we can distinguish
2

between advertised and intrinsic amenities, where the latter capture employer characteristics
that are not explicitly mentioned in job ads but still valued by workers.
Our estimates suggest that the distinction between advertised and intrinsic amenities
is useful for analyzing the employer-level drivers of labor market inequality. We find that
the advertised component of non-pay utility augments pay differentials, while the intrinsic
component represents a compensating differential. Our model simulations show that, all
else equal, wages would decrease by 2.3 log points in the absence of advertised non-pay
attributes and increase by 3.8 log points without intrinsic amenities. Employer-level pay
dispersion increases by 13% when all employers provide the same advertised amenities, and
decreases by 25% when intrinsic amenities are equalized. More broadly, our framework helps
connect findings in the empirical literature focusing on specific non-pay attributes [e.g.,Mas
and Pallais, 2017, Maestas et al., 2023] with the structural labor literature that collapses
amenities into a scalar index [e.g.,Hall and Mueller, 2018, Morchio and Moser, 2024].
We see our approach as the first attempt at quantifying the breadth and quality of
information present in the texts of job ads. We show that job openings contain a broad
range of attributes relevant to workers, and that their content provides reliable signals of
employer quality. These findings have implications for a broad class of job search models,
such as models with a multi-dimensional job ladder [Hwang et al., 1998, Jarosch, 2023]. We
leave it to future research to shed light on employers’ endogenous choices over how much
and what type of content to include in their job ads, and how these choices relate to their
recruitment objectives.
Our results also have implications for the design of policies related to the information
contained in job ads. There is a current policy drive to improve pay transparency within
organizations in many countries, and several US jurisdictions are also implementing policies
to promote pay transparency in job openings [Cullen, 2024].3 Our findings on the prevalence
of pay-related information in job ads, and on which non-pay attributes more attractive
employers choose to advertise, can help inform the design of such policies.
Related literature Several recent studies have used vacancy texts as a source of informa-
tion on the type of jobs advertised by employers. A large portion of this literature focuses on
skill requirements. Marinescu and Wolthoff[2020] study the role of job titles in accounting
for the number of applicants per vacancy.Deming and Kahn[2018], Atalay et al.[2020],
and Deming and Noray[2020] study variation in demand for specific skills across local labor
3In January 2021, Colorado enacted a transparency law requiring online job postings to include informa-
tion about the expected salary, while in November 2022, New York City mandated employers to include a
salary bracket in job ads, followed by Washington State in January 2023 [see Audoly and Xing , 2025].
3

markets and over time.4
We contribute to this literature by considering a broad set of pay and non-pay attributes
advertised by employers in job ads. Several recent contributions focus on a single attribute,
such as flexible work arrangements [Adams-Prassl et al., 2023a], remote work [Hansen et al.,
2023], or on-the-job training [Adams-Prassl et al., 2023b]. Our approach encompasses these
attributes but also captures what employers communicate about compensation and work-
place quality.Sockin [2022] similarly uses text analysis to retrieve amenity information from
employer reviews posted by workers. We see our results as complementary, as vacancy texts
reflect the information advertised by employers rather than worker assessments.5
A large body of work has emphasized that non-pay attributes are important determinants
ofhowmuchworkersvaluealternativeemployers. Onestrandelicitsworkers’preferencesover
specific attributes using quasi-experimental designs [see, e.g.,Le Barbanchon et al., 2021] or
survey experiments [see, e.g.,Maestas et al., 2023].6 The other strand recovers structural
estimates of employers’ composite amenity value by modeling workers’ job choices in markets
with heterogeneous firms. In this approach, amenity values are identified by reconciling
workers’ choices with their pay [Rosen,1986], using employer size in static monopsony models
[e.g., Card et al., 2018, Lamadon et al., 2022] or mobility flows in dynamic search models
[e.g., Sorkin, 2018, Taber and Vejlin, 2020, Morchio and Moser, 2024].
Our paper contributes to both strands of the literature. We quantify the willingness-
to-pay for non-pay attributes mentioned in job ads using a survey experiment, and use
information on advertised attributes in a structural monopsony framework. Further, we
relatesurveyresponsestocommonrevealed-preferencemeasuresofemployerquality, building
on Sorkin [2018] and Bagger and Lentz[2019]. By distinguishing advertised and intrinsic
amenities, we can test which amenities represent augmenting or compensating differentials.
Our framework therefore helps connect these two important strands of the literature.7
We also contribute to the expanding body of work aimed at unpacking search frictions in
the labor market.Jäger et al.[2024] elicit workers’ beliefs about their reemployment wages
4Recent contributions have focused specifically on demand for computer science and AI skills [see, e.g.,
Alekseeva et al. , 2021, Acemoglu et al. , 2022, Braxton and Taska , 2023, Contractor and Taska , 2022].
5In other recent related work, Arold et al. [2025] and Lagos [2024] use text analysis to retrieve information
on workplace amenities from collective bargaining agreement texts, while Caldwell et al. [2025a], Humlum
et al. [2025], Gupta et al. [2025], and Folke and Rickne [2022] design large-scale surveys to collect information
on specific workplace amenities, which these authors are able to link to administrative data.
6Notable examples include workplace flexibility [ Mas and Pallais , 2017, Wiswall and Zafar , 2018, Drake
et al. , 2023], job security [ Datta, 2019], commuting time [ Le Barbanchon et al. , 2021, Bütikofer et al. , 2025],
working from home [ Nagler et al. , 2022, Lewandowski et al., 2022], and shift work [ Desiere and Walter, 2023].
See Mas [2025] for a recent overview.
7Morchio and Moser [2024] also relate their estimates of the amenity values of employers to some of the
workplace characteristics observed in their data, such as “workplace hazards” and “working hours flexibility” .
4

in the event of job loss and compare them to actual outcomes.Horton et al.[2024] andBelot
et al.[2022] design experiments to study how job seekers respond to wage variation in job
vacancies. Our evidence also relates to recent work on how posted wages affect recruitment
outcomes [e.g.,Faberman and Menzio, 2018].8 We add to these studies by focusing on job ad
texts as a source of information on both pay and non-pay attributes, and by relating these
attributes to revealed-preference measures of employer quality.
Finally, our work relates to a broader literature on the role of advertising, which em-
phasizes the distinction between its informational and persuasive functions.9 Isolating these
motives empirically requires either experimental variation [Bertrand et al., 2010] or data on
advertising effort combined with a structural model [Hastings et al., 2017]. While we see our
work as a first step toward linking realized job attributes to those advertised in job ads, we
leave it for future research to devise similar research designs for the labor market.
Outline Section 2 describes our data sources. Section3 explains how we retrieve informa-
tion on the attributes advertised by employers in vacancy texts and provide evidence on their
prevalence in our data. Section4 provides our evidence on the information content of job
ads, where we link the information in job ads to revealed-preference measures of employer
quality, realized attributes in employment contracts, and responses from a survey exper-
iment. Section 5 provides our evidence on the contribution of amenities to labor market
inequality from a monopsony framework with detailed job attributes. Section6 concludes.
2 Data and Institutional Context
2.1 Vacancy Data
Our data include almost 2.15 million job ads covering the near universe of publicly posted
vacancies in Norway between 2015 and 2024.10 These data are maintained by the Norwegian
Public Employment Agency (NAV). The employment agency collects information about
vacancies from several sources, including online job boards and newspapers, as well as direct
job opening reports from employers.11 The share of online postings has increased gradually
over the past two decades, and about 90% of job postings recorded in the agency’s database
8Recent studies have examined the wage elasticity of vacancy duration [ Mueller et al. , 2024], applications
[Azar et al. , 2022, Banfi and Villena-Roldan , 2019], and hires [ Bassier et al. , 2022, Hirsch et al. , 2022].
9See Bagwell [2007] for a review.
10In an earlier version of this paper, we used data on Norwegian job ads going back to 2002.
11In accordance with the Labor Market Act §7, Norwegian employers are required by law to report publicly
posted job openings to the agency, which maintains a comprehensive database of publicly posted vacancy
ads with the stated goal of providing job-seekers with current information on suitable job opportunities.
5

since 2015 were retrieved from various online job boards.12 The remaining job ads were either
(i) scanned or transcribed from newspapers by caseworkers in the employment agency, or
(ii) enclosed in the notifications of job openings sent by employers directly to the agency.
The ability to observe virtually all publicly posted vacancy ads in the economy with full-text
corpora is an important advantage of our setting, which differentiates it from the existing
literatureusingvacancytextsthatoftenreliesoninformationfromselectedonlinejobportals.
In addition to the job title and actual text of each job opening, our data contain the
following structured information about each ad: unique establishment identifiers, the dates
when the ad was registered and filled or removed (i.e., vacancy duration), the number of job
openings per vacancy, and some additional information about job characteristics submitted
by employers. The establishment identifiers are central to our analysis. They allow us to
link job openings to matched employer-employee administrative data and to compare the
information we extract from the text to actual outcomes at the establishment level.13 Each
job ad in our data set has an occupational code based on the 4-digit ISCO classification. This
occupational code is assigned by caseworkers based on the job title and textual information
on job descriptions and skill requirements stated by the employers in the vacancy, and is a
novel feature of our data. Besides the structured information, the text of a typical job ad
contains an average of 310 words. As we describe in Section3, we use tools from the natural
language processing literature to retrieve information on job attributes from these texts.
As in many other contexts [see, e.g.,Card et al., 2024], Norwegian employers are re-
quired to follow anti-discrimination laws (Working Environment Act §3; Equality and Anti-
Discrimination Act §29a), which limit the listing of explicit preferences, e.g., based on gen-
der, age, or ethnicity, in job ads. Moreover, public-sector state employers are subject to the
“qualification principle” (the State Employees Act §3), which requires that the best-qualified
applicant be appointed. This implies that the skill requirements listed in state-sector job ads
have binding implications for how candidates are evaluated. In other respects, Norwegian
employers may design and describe job ads as they see fit. Importantly, there is no general
legal requirement to disclose information on salaries or workplace amenities in job ads.
12Bhuller et al. [2023] study the consequences on labor market matching of increased online job search and
recruitment triggered by a roll-out of broadband internet across Norway during the early 2000s.
13Notably, around 9% of job ads in our data were posted through recruitment or temporary employment
agencies, and we drop these from most of our main analysis, as we are unable to link such ads to the actual
establishment where the job is placed. Further, in around 12% of job ads, the posting employer has for
various reasons decided not to disclose the establishment name in the publicly posted information, but we
do have the corresponding establishment identifier in our data as the agency maintains this information and
could share this with us for research purposes (according to the Labor Market Act §7-4).
6

2.2 Matched Employer-Employee Data
We have access to Norwegian administrative matched employer-employee data covering sev-
eral decades. From January 2015, these data are available as monthly files, where each
record has information on the individual’s employer, as well as their pre-tax earnings, hours
of work, employment start and end date. Individuals can have several recorded spells in any
given month if they receive earnings from more than one employer. This data set has ad-
ditional information on several background characteristics of employees (gender, education)
and employers (location, industry). Notably, our data set also includes information on cer-
tain non-pecuniary job attributes, such as whether the employment spell involves shift work,
and taxable in-kind benefits, which we use in our analysis for comparisons to some of the
attributes retrieved from job ads. Since 2021, the data set has additional job attributes (e.g.,
contract type) for each employment spell that employers must report to Statistics Norway.
We use information from the matched employer-employee data set at several places in
our analysis. First, we infer revealed-preference measures of employer quality in a structural
approach, where we use information on measures of average hourly wages, employment size
and worker flows across employers. For this purpose, we aggregate all employment spells to
the annual level for each worker and retain observations corresponding to the main employer,
defined as the establishment with the largest annual earnings. Using information on annual
earnings and annual contracted hours of work, we calculate the average hourly wage for
each worker in their main job in each year. Second, we use detailed monthly information on
hiring dates for workers in each employment spell to relate posted job ads to potential hires.
Moreover, we draw on information from the matched employer-employee data set to define
comparable worker and employer characteristics for our various analyses.
2.3 Job Postings and Recruitment
An underlying assumption in our analysis is that job postings are an important source
through which employers recruit workers and where workers learn about available jobs. In
order to assess the importance of job postings for recruitment, we use information on (i)
establishment identifiers available both in vacancy and matched employer-employee data
sets, and (ii) the dates of job ad postings and hires. Based on this information, we find that
85.3% of all publicly posted non-staﬀing agency job ads can be associated to at least one new
hire in the establishment within the following six months after the posting date. This applies
to 92.8% for ads posted by public sector state employers, 83.5% of ads by non-state public
sector employers (e.g., local municipalities, public schools, public hospitals), and 84.2% of
ads by private sector employers. Conversely, 48.6% of all hires can be related to a posted
7

ad within the previous six months; this applies to 87.0% of hires by public sector state
employers, 70.4% of hires by non-state public employers, and 39.9% of private sector hires.
Notably, employers may use other recruitment channels, such as social networks, or directly
solicit applications, and thus hire workers without publicly posting a job ad.14 These shares
reported above nonetheless suggest that job ads are an important recruitment channel in the
Norwegian labor market.
To further assess the associations between job postings and recruitment in our data,
we perform a series of descriptive event studies around the month of each job ad posting,
and follow hiring outcomes at the establishment level around such events. This descriptive
evidence can help us evaluate the extent of “excess” hiring associated with job postings,
as opposed to hires that may reflect other recruitment channels. We show in Appendix
Figure A.1 that there is a clear increase in the average number of hires in the six months
following an ad posting, peaking about two to three months after the posting month, while
hiring outcomes are stable prior to the posting month. In total, the number of hired workers
increases by 0.43 workers in the six month period after an ad is posted relative to the months
before. When focusing on hires within narrowly defined 4-digit occupations, i.e., the posted
occupation in the job ad and the occupation associated with the hire are identical, we find an
“excess” hiring of about 0.2 workers in the months following the ad posting. This suggests
that postings and recruitment are closely related, as one may expect.
Further, in some of our analyses, we use micro-level information on workers hired in the
different job postings. While the above suggests there is a tight relationship between postings
and hires, our data sets do not provide direct links between the hired workers and the job
postings at the ad-hire level. In a similar vein as the event study setup described above, we
thus construct a dataset of hires linked to job ads based on probabilistic linkages, within
narrowly defined establishment-occupation cells and posting-hiring periods. We use this
restrictive approach to avoid measurement error in the linking of hires to job ads, with the
downside that we do not capture all hires that could be related to job postings.15 Specifically,
for each job ad we look for hires in the six months after the ad is posted. We restrict links
to establishment-occupation cells with a single hire in the following six months to reduce
14While all employers have an obligation to report the vacancies they publicly post to the Norwegian
employment agency, it is up to them to decide whether or not to post a public vacancy for the purposes of
recruitment. However, recruitment by public-sector state employers is regulated by state legislation, which
requires as a general rule that all job openings are publicly advertised (the State Employees Act §4).
15For instance, the posted occupation in the job ad and the occupation associated with the hire may not
necessarily be identical, even though the worker is clearly hired as a result of the job posting. As noted in
Section 2.1, the occupational code in our job ad data is assigned by caseworkers in the employment agency
based on the job title and other textual information stated by the employers in the vacancy, which may be
different from the occupational code filed by the employer in the administrative records at the time of hiring.
8

the likelihood of linking an ad to a worker hired independently of the posting. We further
exclude ads that were posted on the same date in the same establishment-occupation cell.
We also exclude recall hires having a prior spell with the employer, as they are less likely to
be hired through postings. Finally, we avoid linking a single job spell to multiple vacancies
by removing it if the spell is already linked to a job ad, i.e., we link ads to hires without
replacement. In the following, we refer to the resulting dataset as the ad-hire sample.
2.4 Survey Experiment
Besides information on job ads and matched employer-employee data, we use anonymized
data from a survey experiment performed by Bhuller et al. [2024]. Notably, the survey
used hypothetical choice experiments to elicit willingness to pay (WTPs) for workplace
amenities, and further included components where respondents were asked to rank real job
ads, where the choice sets respondents faced were experimentally designed for the purposes
of identification. The survey experiment was pre-registered with trial numberAEARCTR-
0013426 in the AEA RCT registry. In recent work,Andresen et al.[2026] use data from this
survey to study the role of pay beliefs on job choices, using experimentally designed features
of the survey. We instead use information on respondents’ rankings of real job ads, and
relate these rankings to revealed-preference measures of employer quality, which we estimate
using the matched employer-employee data for the population at large. As inAndresen et al.
[2026], we provide estimates of respondents’ WTPs for specific workplace amenities.
We use data from the survey waves that were targeted at students enrolled at the Uni-
versity of Oslo, which is a large public university in Norway. Around 2,800 students were
invited to participate in the survey, of whom 1,059 gave their informed consent and 1,040
completed one of the relevant modules, which gave a response rate of about 37% (see details
inAndresen et al.[2026]). Each respondent faced up to 40 experimentally designed hypothet-
ical choice scenarios, where the respondents were asked to state their preferred alternative
across the two options that were made available to them in each scenario. Half of the choice
scenarios featured choices between purely hypothetical jobs as inWiswall and Zafar[2018].
Each alternative listed the monthly salary and a set of posted amenities that were randomly
sampled using the methodology developed byDrake et al.[2022], and the respondents were
explicitly told that the alternatives were otherwise identical in all aspects. This approach
facilitates consistent estimation of respondents’ WTPs for randomized workplace amenities.
Importantly, for the purposes of our study, the survey also included experimentally de-
signed components featuring around 1,200 real job ads that were posted by around 500
unique employers in Oslo or the surrounding labor market regions over a six-month period
9

from June to December 2023. These job ads were used in experimentally designed choice
scenarios as part of the survey, where the respondents were asked to rank between two job
ads in each scenario, as illustrated in Appendix FigureA.2. In a given scenario, the job
ads were randomly selected from the relevant pool of posted ads within the same sector and
broad occupation group. The respondents were allowed to read the full texts of each job
posting, and could thus learn about amenities and other job attributes associated with each
option, before stating their preferred alternative. To ease comparisons, all job ads featured
full-time jobs. Notably, none of the job ads used in the survey experiment explicitly stated
the compensation level as part of the actual ad text. These features imply that comparisons
of respondents’ rankings of job ads to revealed-preference measures of employer quality de-
rived from market-level data are informative about what job seekers can potentially learn
about employer quality solely from job ad texts. Using our matched employer-employee data
across all employers in the Norwegian labor market, we are able to construct measures of
employer quality for most of the employers included in the survey for the relevant period.
2.5 Sample Selection
For most of our analysis we focus on the years 2021-2024, which allows us to leverage the
richness of our administrative data and relate our findings to evidence from the survey
experiment that was fielded during the later part of this period. We exclude 2020 from
the analysis as recruitment and hiring were heavily disrupted in Norway at the onset of the
Covid-19 pandemic. From 2021, job postings and unemployment rates had largely returned
to their pre-pandemic levels. We also provide additional results from a longer period covering
the years 2015-2024, using only information from job ads and administrative data sources.
We use different samples at various stages of our analysis. Table1 summarizes these
samples and shows how the number of observations differ across samples used in our baseline
analysis for the 2021-2024 period.16 As shown in the first row, prior to additional sample
restrictions, our initial matched employer-employee data has about 264,000 establishments
covering about 3 million unique workers and 12.2 million worker-year observations. During
this period, we observe about 1 million job ads in the employment agency’s database.17
In our main analysis, we use either data on job ads or job ads combined with admin-
istrative employment data. As shown in the second row of Table1, we retain around 92%
of job ads with non-missing information on establishment and posted occupation, as well as
non-missing vacancy texts with at least one section written in Norwegian. Note, however,
that less than half of the establishments in our initial sample publicly posted at least one job
16Appendix Table A.3 shows the corresponding sample restrictions for the 2015-2024.
17An ad is on average associated with 1.6 job openings, so these ads cover 1.6 million job openings.
10

Table 1: Overview of Sample Selection.
Workers in Included Establishments
Job Ads Establishments Workers Worker-Years
(1) (2) (3) (4)
All Observations 1,031,687 (100%) 264,084 (100%) 3,000,154 (100%) 12,220,469 (100%)
Main Analysis
Text Analysis Sample 943,721 (91.5%) 117,896 (44.6%) 2,792,164 (93.1%) 10,985,594 (89.9%)
Employer Quality Sample 675,832 (65.5%) 70,046 (26.5%) 2,210,151 (73.7%) 8,253,567 (67.5%)
Static Monopsony Sample 390,722 (37.9%) 12,973 (4.9%) 1,688,064 (56.3%) 5,902,421 (48.3%)
Additional Analysis
Linked Ad-Hire Sample 110,913 (10.8%) 47,877 (18.1%) 2,036,676 (67.9%) 6,999,923 (57.3%)
Survey Experiment Sample 1,028 (0.1%) 417 (0.2%) 96,529 (3.2%) 214,123 (1.8%)
Notes: This table documents the sample sizes for different sample restrictions imposed for the 2021-2024
period. The first row shows the total number of observations in our data on job ads (Column 1) and matched
employer-employee data (Columns 2-4), prior to the various sample selection steps. The “Text Analysis
Sample” refers to the set of job ads with non-missing information on establishment identifiers, occupational
codes, and vacancy texts, and with at least one section written in Norwegian. The “Employer Quality
Sample” refers to the sample we retain by restricting the sample to workers aged 20 to 60 (inclusive) and the
strongly connected set of employers used in the estimation of employer values, while removing establishments
registered as recruitment or temporary employment agencies. The “Static Monopsony Sample” refers to a
subset of large employers that have at least 30 stayers and 15 movers during the 2021-2024 period. The
“Linked Ad-Hire Sample” refers to a restricted set of job ads that could be uniquely linked to a new hire at
the establishment-4-digit occupation level within the six-month period since job ad posting, as described in
Section 2.3. The “Survey Experiment Sample” refers to the subset of job ads used in the survey experiment,
as described in Section 2.4, that could be linked to employer quality measures taken from the “Employer
Quality Sample” . Appendix Table A.1 documents the characteristics of employers and workers for each of
these samples, while Appendix Figure A.5 documents the detected job ad attributes for the three “Main
Analysis” samples. Appendix Table A.3 documents the corresponding sample sizes for the 2015-2024 period.
ad in the 2021-2024 period. Meanwhile, the posting establishments tend to be substantially
larger, and for our text analysis of job ads, we still retain establishments covering around 90%
of workers and worker-year observations, as shown in Columns (3)-(4). In Appendix Table
A.1, we provide a comparison of how sample compositions differ across samples. Notably,
employers considered in our text analysis of job ads are quite similar in terms of average
worker characteristics to the initial sample drawn from the matched employer-employee data,
yet these employers are larger in size and more likely to belong in the public sector.
Next, we consider the sample used for estimating revealed-preference measures of em-
ployer quality. In this sample, we include only prime-aged workers, i.e., aged 20–60, and
further, we restrict the estimation to employers that are in the set of strongly connected
establishments, i.e., the set of establishments across which we observe two-way job mobil-
ity flows during the 2021-2024 period. Finally, we also remove establishments registered as
11

recruitment or temporary employment agencies.18 With these restrictions, we exclude more
than 70% of the establishments in our initial sample, but still retain establishments covering
about 74% (67%) of all workers (worker-year observations). Comparing the average charac-
teristics of employers considered in the text analysis and the employer quality measures in
Appendix TableA.1, we find that the two samples are broadly similar in terms of industry
and worker composition, while employers used in the latter sample are larger.
Further, we consider a more restricted set of large employers that we use to estimate a
static monopsony model of the labor market. This sample includes only large employers that
have at least 30 stayers and 15 movers during the 2021-2024 period. Despite covering only
5% of establishments in our initial sample, this sample nonetheless retains employers that
account for 38% of job ads and around 56% (48%) of all workers (worker-year observations).
Given the sample restrictions, these employers are also substantially larger than the average
employer in our initial sample, having a higher share of college graduates and higher average
hourly wage, and these employers are more likely to belong in the public sector.
To assess how well job attributes advertised in job ads correspond to realized job charac-
teristics observed in administrative data, we further use a restrictive sample of job ads where
we can create unique links between each job ad and a newly hired worker, as described more
closely in Section 2.3. This sample covers 11% of all job ads and 18% of establishments,
which altogether account for 68% (57%) of workers (worker-year observations) in our initial
data. Despite the restrictive nature of the ad-hire links, this sample is fairly similar in terms
of overall worker and establishment characteristics to the sample used in our text analysis,
as shown in Columns (2) and (5) of Appendix TableA.1. Notably, however, the charac-
teristics of newly hired workers differ from the average characteristics of workers in these
establishments. The newly hired workers are younger, more likely to be female, and have
lower wages; see Appendix TableA.2. This reflects that the linking of ads to hire naturally
captures workers overrepresented in labor market flows, as compared to the average worker.
Finally, we use data from the survey experiment performed byBhuller et al.[2024]. For
the purposes of this study, we are able to link measures of employer quality to 1,028 job
ads that were posted by 417 employers. Despite the small number of employers featured
in the survey experiment, as shown in the numbers reported in the final row of Table1,
these employers account for around 3% of workers and 2% of worker-year observations in
our initial sample. This reflects that employers posting job ads in Oslo and the surrounding
labor market regions are larger. As shown in Appendix TableA.1, these employers have a
larger share of female and college graduated workers and pay higher wages, and are more
18Around 90.1% of job ads classified as “staﬀing agency” ads in our data were posted by temporary
employment agencies (e.g., Manpower), while recruitment agencies account for the remaining share.
12

likely to belong in the public sector. Meanwhile, the composition of survey respondents
departs significantly from the average characteristics of workers in our data; see Appendix
Table A.2. As mentioned in Section2.4, the survey targeted university students, and thus
survey respondents are in their early 20s, almost 70% are female, and less than 50% had
completed a college (bachelor’s) degree at the time of interview. Notably, however, nearly
all survey respondents report having at least one prior employment spell, receiving average
hourly wages that are about 20% lower than for the newly hired workers in our linked ad-hire
sample.
3 Pay and Non-Pay Attributes in Vacancy Texts
This section describes how we retrieve the job attributes publicly advertised by employers in
job ads. These attributes are extracted from vacancy texts using tools developed in natural
language processing. To the best of our knowledge, we are among the first to systematically
extract a comprehensive set of pay and amenity attributes from the texts of job ads.
3.1 Extracting Advertised Job Attributes
Consider the sample vacancy text for an IT-consultant position in Figure1. This text con-
tains a variety of information on the type of tasks associated with the position, the required
skills and experience necessary to perform these tasks, and the pay and non-pay attributes
of the job. As this example makes clear, these attributes cover many different aspects of the
position, ranging from the duration of the contract and regular hours (“full time, permanent
position”) to characteristics of the workplace (“good working environment”) and information
about the level of pay (“competitive conditions”). Our goal is to systematically extract this
information from the open text of all vacancies in the database.
The key diﬀiculty with extracting job attributes from the raw texts of job ads is that a
single attribute can be expressed in many distinct ways in natural language. Besides, while
prior research in this area has centered on specific workplace amenities, we do not have a
definitive list of the job attributes advertised by employers in vacancy texts. We therefore
proceed in three broad steps to extract these attributes from all job postings: (i) we pin down
a list of attributes to extract, (ii) we ascribe a set of expressions to each of these attributes,
and (iii) we label the entire corpus of vacancy texts based on these expressions.
Step 1: List of job attributes to include Our choice of which pay and non-pay job
attributes to include in the analysis is based partly on information that is commonly stated
13

Figure 1: Sample Vacancy Text: IT-consultant.
IT-consultant
About the job: Full-time, Permanent position
We are looking for a new team player for our IT department! As an IT consultant,
you will be responsible for our IT environment. It also includes getting to know large
parts of our organization well through having internal user support as well as employee
training. You simply get a varied working day, with different tasks to brush up on. In
the future, you will also assist in larger IT development projects [...]
Tasks:
- IT security.
- SharePoint.
- Data warehouse.
- SOX Compliance.
Required qualifications:
- Likes IT technical challenges.
- Sociable and likes to communicate with people.
- Has relevant education.
- Has experience from similar positions.
We can offer :
- A workplace with many varied tasks and a high focus on quality.
- Training in our key products/services.
- Good working environment with solid professional expertise.
- Flexible working hours.
- Competitive conditions.
[...]
Notes: Translation from Norwegian by the authors. In Appendix Figures A.3-A.4, we provide additional
examples of representative vacancy texts covering a teaching substitute and a civil engineer, respectively.
14

in ads, partly on our knowledge of the particular context of the Norwegian labor market,
and partly on attributes that are considered important in the existing literature.
We identify commonly mentioned attributes in publicly posted vacancies using two dis-
tinct strategies: (i) human recognition on a subset of job ads, and (ii) identifying commonly
used phrases in the “we offer” sections of vacancy texts. We first directed several research
assistants to read through the texts of 1,200 randomly chosen job ads in the vacancy corpus.
The research assistants were asked to make a list of the commonly advertised attributes that
are valuable to workers, to take note of the corresponding expressions associated with these
attributes, and to indicate the presence of these attributes in each job posting.
As a second source of information on commonly advertised attributes, we isolate and
extract common phrases from the “we offer” sections of job ads. We do this in two steps:
First, we identify and extract all structured lists from the vacancy corpus.19 As an example,
in the sample vacancy text in Figure1, we retrieve three distinct lists: “Tasks,” “Required
qualifications,” and “We can offer.” We find that 50% of the vacancy texts in our sample
featureoneormoresuchlists. Second, weisolatethe“weoffer”listsbyapplyingunsupervised
topic modeling [Blei et al., 2003] to the collection of lists retrieved in the previous step.
Further methodological details are provided in AppendixB. The most common expressions
in the “we offer” lists constitute the second source of information on commonly advertised
job attributes that we are able to identify.
Based on the two approaches described above, we are able to identify 47 distinct job
attributes, as well as an initial set of expressions associated with each attribute. For the
purpose of illustration, we summarize the 47 attributes in ten broad categories within classes
of pay and non-pay job attributes, as shown in Table2. Taken together, these attributes
cover a variety of different job characteristics advertised in job ads, such as information on
career opportunities, convenient/inconvenient hours, and the quality of the workplace. The
full list of job attributes with descriptions is provided in Appendix TablesB.3-B.5.
Step 2: Expressions corresponding to each job attribute Each job attribute re-
trieved in Step 1 is associated with an initial set of expressions. For instance, the attribute
“flexible working hours,” is associated with the target expressions “flexible working hours”
and “flexible work time arrangements.”20 In Step 2, we seek to enrich this initial set by
19These lists are found by searching for consecutive sentences starting with a hyphen or bullet point and
by searching for the HTML tags used to generate lists in online vacancies. By design, this approach identifies
attributes that can be organised in structured lists. In the later steps, we search for the common phrases
identified in structured lists across the full corpus of job ads, including ads that were not posted online or
lacked structured lists, as well as search for alternative similar phrases identified using text analysis tools.
20The corresponding expressions in Norwegian are “fleksibel arbeidstid” and “fleksible arbeidstidsord-
ninger,” which denote working hour schemes that offer workers the possibility to choose their own schedule.
15

Table 2: Main Categories of Job Attributes.
Main Category Examples
A. Pay Attributes
– Compensation Scheme Compensation level; Collective agreement pay; Incentive pay
– Financial Attributes Insurance scheme; Pension scheme; Mortgage possibility
– Career Opportunities On-the-job training; Career opportunities
B. Non-Pay Attributes
– Hours of Work Full-time; Part-time; Full-time/part-time choice
– Convenient Hours Regular daytime work; Possibility to work flexible hours
– Inconvenient Hours Shift-work; Weekend/evening/nights; On-call employment
– Contract Duration Permanent job; Temporary job
– Workplace Attributes Social environment; Good colleagues; Remote work
– Task-Related Attributes Interesting tasks; Challenging tasks
– Other Minor Perks Central location; Company vehicle; Company gym
Notes: This table documents broad categories of attributes detected in vacancies, with notable examples
of individual attributes. The full list of job attributes with descriptions is provided in Appendix Tables
B.3-B.5.
including other common ways of referring to the same attributes.
To expand on the set of possible expressions in our analysis, we rely on the Continuous
Bag-of-Words (CBOW) Word2Vec algorithm [Mikolov et al., 2013]21. This approach mea-
sures the degree of similarity between phrases by exploiting that words with similar meanings
tend to occur in similar contexts. As an example, information about flexible working hours
is commonly given with information about whether the spell is full-time or part-time in our
corpus. We train the CBOW model using our collection of job ads, thus associating words
that are similar in the context of job ads but not necessarily in other contexts. We then
loop through the full collection of job ads and use the trained model to store phrases of
one, two, or three consecutive words most similar to the phrases in our original lists from
Step 1. Finally, we remove expressions that are wrongly classified as similar by the model.
An example of a removed phrase is “flexible job adaptation,” which is classified as similar
to “flexible working hours” by the model, but does not imply flexibility in one’s schedule.22
This discussion highlights the main advantage of our approach. We are able to identify a
large number of attributes that can be described by many different expressions, but we still
21See Atalay et al. [2020] for an application of this algorithm to vacancy job titles.
22Notably, as there are two variants of written Norwegian (Bokmål and Nynorsk), we translate all phrases
from Bokmål to Nynorsk, and append phrases that are not already captured by our dictionary.
16

retain control over which specific expressions are included.
In total, our dictionary consists of 1,772 unique expressions, and each of the 47 attributes
is associated with around 39 expressions on average, although some attributes have many
fewer associated expressions than others. We have made this full list of expressions available
in an online repository for other researchers to use.23 Differences in the number of associated
phrases reflect both the number of ways an attribute is presented in vacancy texts and the
specificity of an attribute. For instance, the attribute “inclusive work-life scheme” is usually
discussed using specific terms in Norwegian, which is why the model identifies only a small
number of expressions for this attribute. Conversely, the attribute “shift work” is associated
with many alternative expressions since there are many ways jobs can involve shift work.
Step 3: Apply to all vacancies We use our 1,772 unique expressions to generate job
attribute indicators for all ads in the data. A job ad is defined as advertising a given attribute
if any of the expressions associated with the attribute is found in the ad text.
3.2 Validation
A potential drawback of our approach is that it might fail to detect attributes implied by
more complex phrases. Consider the sentence “we offer flexibility in starting date as well
as in working hours.” As there is some text between “flexibility” and “working hours,” our
dictionaryapproachwouldnotdetect flexibilityin workinghours inthis case. More generally,
wecanexpectthatajobpostingdoesofferaspecificattributewhenourprocedureidentifiesit
(high precision rate), but we can be less certain that a job posting does not contain that same
attribute when it is not identified by our procedure (low sensitivity rate). Another potential
concern is that our approach does not differentiate between aﬀirmations and negations when
searching for specific expressions. In practice, this concern is limited, as negations related
to advertised attributes are rare.24
To check the importance of the above concerns in our setting, we performed an additional
round of manual recognition. We selected another random sample of 400 job ads posted dur-
ing the five-year period from 2015 to 2019, and directed another group of research assistants
to manually classify job attributes in this sample. We deliberately recruited a distinct group
of assistants from the ones who contributed to the initial manual classification (Step 1 of
Section 3.1). We gave each research assistant our full list of 47 attributes and a few sample
23This repository can be accessed at this link: https://zenodo.org/records/14973628.
24We examined the prevalence of negations by searching for 22 negation cues (e.g., “not,” “no,” “absence,”
“never”) within the six words preceding each detected attribute phrase. At most 0.8% of detected attribute
mentions indicated a potential negation.
17

Table 3: Validation of Detected Job Attributes.
All Ads Job Ads in the Validation Sample
Text
Analysis
Text
Analysis
Manual
Recognition
Success
Rate
Precision
Rate
Sensitivity
Rate
(1) (2) (3) (4) (5) (6)
A. Pay Attributes 70.8 79.2 73.2 89.0 89.3 96.6
–– Compensation Scheme 55.9 64.8 61.8 92.5 91.9 96.4
–– Financial Attributes 32.4 37.8 34.2 96.5 90.7 100.0
–– Career Opportunities 43.6 48.8 41.8 79.0 71.3 83.2
B. Non-Pay Attributes 96.5 98.0 97.0 97.5 98.2 99.2
–– Hours of Work 77.0 76.0 71.8 92.2 92.1 97.6
–– Convenient Hours 20.5 15.8 15.8 94.0 81.0 81.0
–– Inconvenient Hours 27.0 28.0 22.8 92.8 77.7 95.6
–– Contract Duration 65.0 67.2 66.8 88.0 90.7 91.4
–– Workplace Attributes 50.7 55.0 51.0 82.0 80.0 86.3
–– Task-Related Attributes 55.9 65.0 46.5 72.0 64.2 89.8
–– Minor Perks 39.8 46.0 18.5 66.5 33.7 83.8
Any Observed Attribute 97.0 98.2 98.0 98.2 99.0 99.2
Average Number of Attributes 6.11 6.64 5.56 – – –
Number of Job Ads 860,467 400 400 400 – –
Notes: This table compares prevalence rates for ten broad categories of job attributes measured using our
text analysis approach and manual recognition. A broad category of job attribute is considered present if
at least one of the underlying distinct job attributes is detected. Column (1) is for the full sample of job
ads with non-missing vacancy text posted 2015–2019, while Columns (2)-(6) consider a random sample of
400 job ads used in the validation. Columns (1)-(3) report prevalence rates, while Columns (4)-(6) provide
summary statistics that compare prevalence rates from text analysis and manual recognition. Success rate is
defined as the share of job ads where the text analysis yields the same result as manual recognition. Precision
is the rate of agreement between the two methods given that an attribute was detected in our text analysis,
while, sensitivity is the rate of agreement given that an attribute was detected in the manual recognition.
Precision is a measure of how many detected attributes are false positives, and sensitivity is a measure of
how good our method is at recovering true attributes. See Appendix Table A.4 for results from validation
exercises for each of the 47 underlying job attributes that contribute to the ten broad categories shown here.
expressions for each attribute, and tasked them to search for each of these attributes in the
full text of each job ad. We could then systematically compare the attributes retrieved with
our automated procedure to those detected in the manual human recognition.
Table 3 shows the results of this comparison for ten broad categories of job attributes.
Column (1) reports the prevalence rates measured based on our text analysis for each of these
categories in the sample of job ads from 2015–2019. Column (2) reports the corresponding
rates for the random sample of 400 job ads, also based on our text analysis procedure, while
Column (3) reports the prevalence rates from manual recognition for this random sample.
18

Finally, Columns (4)-(6) provide rates of success, precision, and sensitivity by comparing
prevalence rates for each category across text analysis and manual recognition.
Across the ten broad categories of job attributes, we find that our procedure performs well
in terms of success, precision, and sensitivity rates. Success and precision rates are above
or around 80% for most categories. The notable exceptions are “task-related attributes”,
where we find a success rate of 72% and precision of 64.2%, and “minor perks”, where we
find a success rate of 66.5% and precision of 33.7%. The former is driven by differences in
detection rates for whether the job “involves leadership responsibilities” and “work involves
travelling,” while the latter is driven by “central location,” which is more frequently detected
in our text analysis.25 Overall, high levels of precision indicate that the attributes recovered
by text analysis reflect the actual content of the attributes well. Sensitivity is always equal
to or larger than precision, above 80% for all attributes.
3.3 The Prevalence of Advertised Job Attributes
We now use the detailed advertised job attributes to highlight several salient descriptive
statistics. Figure 2 reports the share of job ads posted between 2021 and 2024 advertising
each of the 47 attributes, while Appendix FigureA.6 shows the corresponding results for
the 2015-2024 period as a whole. About 60% of job ads provide some compensation-related
information. However, explicit information about the actual level of pay is scarce. Less
than 10% of ads mention a salary number or bracket (“compensation level”) and slightly
more than 25% of ads indicate that pay is set by a collective wage bargaining agreement
(“collective agreement pay”).26 Taken together, we find that 30% of job ads feature explicit
information about the actual pay level or CBAs (e.g., pay scales or floors).
Beyond information on the more tangible attributes of the job, such as pay, hours of work
and contract duration, Figure2 also shows that employers frequently advertise more subjec-
tive aspects of the working environment, such as characteristics of the workplace (“workplace
attributes”) or some appreciation of the type of tasks involved (“task-related attributes”).
Around 35–40% of ads describe these tasks as “challenging” or “interesting.” Similarly, more
than 50% of vacancies feature some language about the quality of the “social environment”
at work and 30% advertise “good colleagues.”
Next, we analyze to what extent differences in advertised attributes are explained by
observable characteristics of the job ad, such as the industry of the posting establishment or
the occupation associated with the job title stated in the job ad. To describe the variation
25See Appendix Table A.4, which shows the results of the same validation exercise for each of the 47
underlying attributes contributing to the ten broad categories in Table 3.
26By comparison, Batra et al. [2023] find that 13% of job ads have salary information in US data.
19

Figure 2: The Prevalence of Job Attributes Advertised in Vacancy Texts.
Compensation Scheme:
  - Compensation Level
  - Competitive Pay
  - Collective Agreement Pay
  - Incentive Pay Scheme
  - Hiring Bonus
  - Good Overtime Pay
  - Any Other Mention of Pay
Financial Attributes:
  - Pension Scheme
  - Insurance Scheme
  - Mortgage Possibility
Career Opportunities:
  - Good Career Paths
  - On-the-Job Training
Hours of Work:
  - Full-time Contract
  - Part-time Contract
  - Full-time/Part-time Choice
Convenient Hours:
  - Possibility to Work Flexible Hours
  - Regular Daytime Work Schedule
  - Exempt from Work Hour Regulations
Inconvenient Hours:
  - Shift Work
  - Weekend/Evening/Night Work
  - On-call Employment
  - Overtime Work Required
Contract Duration:
  - Permanent Job
  - Temporary Job
  - Fixed-term Contract
Workplace Attributes:
  - Social Environment
  - Good Colleagues
  - Possibility for Remote Work
  - Shared Office Space
  - Inclusive Work-life Scheme
Task-Related Attributes:
  - Interesting Tasks
  - Challenging Tasks
  - Variation in Tasks
  - Responsibility in Job
  - Independence in Performing Tasks
  - Involves Leadership Responsibility
  - Work Involves Travelling
Minor Perks:
  - Beautiful Location
  - Central Location
  - Company Gym or Sports Team
  - Parking Space On Premises
  - Company Vehicle
  - Any Welfare Scheme
  - Company Cabin
  - Occupational Health Service
  - Company Canteen
  - Flexible/Extended Holidays
0 .1 .2 .3 .4 .5 .6 .7 .8 .9 1
Notes: This figure documents the prevalence of job attributes detected in job ads posted in Norway between
2021 and 2024 [N=943,721]. The light blue bars show the share of ads detected with each distinct job
attribute. The dark blue bars show the share of ads detected with at least one attribute within ten broad
categories. Appendix Figure A.6 shows the corresponding results for the 2015-2024 period as a whole.
20

Figure 3: Explained Variation in Publicly Advertised Job Attributes.
0 .2 .4 .6 .8 1
Pseudo R
2
  - Number of Attributes
  - Companyname Disclosed
  - Posted Online
  - Number of Words
Other Ad Characteristics:
  - Flexible/Extended Holidays
  - Company Canteen
  - Occupational Health Service
  - Company Cabin
  - Any Welfare Scheme
  - Company Vehicle
  - Parking Space On Premises
  - Company Gym or Sports Team
  - Central Location
  - Beautiful Location
Minor Perks:
  - Work Involves Travelling
  - Involves Leadership Responsibility
  - Independence in Performing Tasks
  - Responsibility in Job
  - Variation in Tasks
  - Challenging Tasks
  - Interesting Tasks
Task-Related Attributes:
  - Inclusive Work-life Scheme
  - Shared Office Space
  - Possibility for Remote Work
  - Good Colleagues
  - Social Environment
Workplace Attributes:
  - Fixed-term Contract
  - Temporary Job
  - Permanent Job
Contract Duration:
  - Overtime Work Required
  - On-call Employment
  - Weekend/Evening/Night Work
  - Shift Work
Inconvenient Hours:
  - Exempt from Work Hour Regulations
  - Regular Daytime Work Schedule
  - Possibility to Work Flexible Hours
Convenient Hours:
  - Full-time/Part-time Choice
  - Part-time Contract
  - Full-time Contract
Hours of Work:
  - On-the-Job Training
  - Good Career Paths
Career Opportunities:
  - Mortgage Possibility
  - Insurance Scheme
  - Pension Scheme
Financial Attributes:
  - Any Other Mention of Pay
  - Good Overtime Pay
  - Hiring Bonus
  - Incentive Pay Scheme
  - Collective Agreement Pay
  - Competitive Pay
  - Compensation Level
Compensation Scheme:
Industry FE + Location FE
+ Occupation FE + Establishment FE
Notes: This figure shows pseudo R2 [McFadden, 1974] from separate logistic regressions of binary job at-
tributes detected in job ads posted in Norway between 2021 and 2024 [N=748,870] on fixed effects denoting
unique combinations of 2-digit industries (88 groups), location indicators (10 groups), 2-digit occupations
(44 groups), and 57,656 establishments. We start by including industry fixed effects, continue by including
industry×location fixed effects, and so on. The last set of regressions controls for 133,964 unique combina-
tions. The regression excludes 194,851 ads with a unique combination of establishment, occupation, location,
and industry indicators, since these observations are perfectly predicted by the last set of regressions by con-
struction. Location indicators group 422 municipalities into 10 groups based on the number of workers, so
municipalities assigned to the same group have a similar number of workers, with a specific indicator for
job postings in Oslo. Appendix Figure A.7 shows the corresponding Shapley Value decomposition, while
Appendix Figure A.8 shows the corresponding results for the 2015-2024 period as a whole.
21

in advertised job attributes that can be explained by these characteristics, we estimate a
series of logistic regressions for the probability that a given attribute is advertised in the
text of a vacancy with several sets of fixed effects: industries, locations, occupations, and
establishments. Figure3 reports the estimated pseudo-R2, a summary measure of goodness
of fit for binary outcomes [McFadden, 1974], from logistic regressions estimated separately
for each attribute.27 This measure therefore captures the variation in the content of job ads
within industries, locations, occupations, and establishments.
A possibility is that the attributes advertised for a given position are largely determined
by its industry or occupation, so the pay and non-pay attributes mentioned in vacancy texts
directly reflect the type of job advertised. For example, it can be expected that working
as a hospital nurse involves shift-work, in which case there is no value-added to mentioning
this information in the corresponding job description. The data instead suggest that there
is variation in advertised job attributes for very similar positions. Figure 3 shows that
industries, occupations, and location fixed-effects explain at most 30–40% of the variation in
theattributesadvertisedbyemployersacrossthe47categoriesweretrieve. Bycontrast, when
we add establishment fixed-effects, we find that the explained variation jumps up to 50–70%
across attributes, which suggests that advertised attributes are in large part correlated across
vacancies for establishments observed with several job ads. These patterns are confirmed in
a Shapley value decomposition (Appendix FigureA.7), and also hold when we extend the
analysis to the years 2015-2024 (Appendix FigureA.8). These patterns are also consistent
with the existence of an “establishment fixed-effect” in advertised attributes, and it justifies
the employer-level analysis we develop in the next sections.
4 The Information Content of Job Ads
In the previous section, we established that employers advertise many pay and non-pay
attributes through job vacancy texts. How much information about the quality of employers
can workers infer from these attributes? We answer this question using three empirical
strategies. In Section4.1, we analyze how advertised job attributes correlate with revealed-
preference measures of employer quality. In Section4.2, we link ads to hires and examine the
concordance between advertised and realized job attributes, for the subset of attributes with
direct counterparts in the register data. In Section4.3, we present evidence from a survey
experiment in which respondents chose among experimentally designed choice sets featuring
27As an alternative, we also estimated linear probability models using OLS with the same set of fixed
effects separately for each attribute (results available upon request). However, as all of our pay and non-
pay attributes are binary, one could be concerned about interpreting standard goodness of fit from such
regressions, which restricts the range of the coeﬀicient of determination R2 [Cox and Wermuth , 1992].
22

real job ads. All three strategies suggest that job ads are a reliable channel through which
workers can gather information about employer quality.
4.1 Evidence from Linked Ad-Establishment Data
We derive alternative composite measures of employer quality from the matched employer-
employee data, as commonly done in revealed-preference approaches. These measures do
not rely on the vacancy data and are obtained from actual labor market outcomes, such as
wages and worker flows across employers. We then link these measures to the advertised
job attributes retrieved in Section3 and ask whether advertised attributes correlate with
employer quality.
4.1.1 Revealed-Preference Measures of Employer Quality
We consider alternative revealed-preference measures previously used in the literature, each
capturing workers’ common valuation of alternative employers. The common theoretical
underpinning of these measures is that labor market imperfections, such as search frictions
or monopsony power, can sustain dispersion in employer quality in equilibrium.
We center our analysis on four measures of employer quality: (i) the employer pay pre-
mium from a standard two-sided wage regression [Abowd et al., 1999], (ii) the overall em-
ployer value in the utility-posting model ofSorkin [2018], (iii) the poaching index ofBagger
and Lentz[2019], and (iv) employer size [Card et al., 2018, Burdett and Mortensen, 1998].28
We select these measures because they capture workers’ revealed preferences within a broad
class of models with heterogeneous employers. For example, in many job search models,
workers have well-defined preferences over employers that are closely linked to employer
size, the poaching index, and pay premiums.29
To estimate measures of employer quality, we focus on employers that are connected by
worker mobility.30 As shown in Table1 (“Employer Quality Sample”), about one-fourth
of establishments satisfy this restriction.31 Since employment is concentrated at larger em-
ployers, however, this sample still covers 74% of workers and 66% of job ads. To precisely
estimate employer-level parameters, we also reduce their number using a clustering algorithm
as a pre-estimation step [Bonhomme et al., 2019], which partitions employers into groups
with similar observable characteristics. The clustering provides a surjective mappingj →g,
28We also report results for the flow utility value in the utility-posting model of Sorkin [2018].
29Notably, the standard Burdett and Mortensen [1998] model with heterogeneous firm productivities yields
an identical ranking of firms based on firm size, pay premiums and the metric underlying the poaching index.
30We compute all measures for the same subset of strongly connected employers, derived from the most
stringent identification restrictions in Sorkin [2018].
31Detailed descriptive statistics on workers and employers are in Table A.1 of Appendix A.
23

where j denotes the employers in the estimation sample andg(j) denotes the employer-
cluster to whichj belongs. This increases the number of movers per group, which underlies
most measures, while preserving substantial employer heterogeneity. The number of clusters
is selected to yield groups with 50 establishments on average, which resulted in1, 422 unique
employer clusters in our baseline.32 Additional details on the clustering algorithm and the
construction and estimation of the employer quality measures are in AppendixC.
These four measures are imperfectly correlated, suggesting that they capture different
aspects of employer quality. Most correlations fall in the 30–50% range: for instance, the
correlation between pay premiums and Sorkin values is 0.369.33 One exception is the strong
correlation between the Sorkin value and the poaching index, which we estimate to be 0.876.
Appendix TableC.1 provides the full set of correlations across all four measures.
4.1.2 What do Good Employers Advertise in Job Postings?
We first investigate whether employers estimated as high- or low-quality advertise different
attributes in their job postings. We estimate
Ak g(j) =αk 0 +αk Q · bQg(j) +εk g(j), (1)
at the employer-cluster level, whereg(j) denotes the mapping from an employerj to a cluster
g, Ak g(j) is the share of job ads from employers in clusterg that advertise attributek, bQg(j)
is their estimated quality (one of the measures described above), andεk g(j) is an error term.
The regression is weighted by the number of worker-years in each cluster.
The key coeﬀicient of interest isαk Q, which measures the association between employer
quality bQg(j) and the propensity to advertise attribute Ak g(j). This descriptive approach
transparently shows whether employers of different quality systematically advertise different
attributes. We standardize bQg(j), soαk Q can be interpreted as the change in the propensity
to advertiseAk g(j) associated with a one standard deviation increase in employer quality.
Figure 4 reports bαk Q for three revealed-preference measures of employer quality (pay
premium, Sorkin value, and poaching index) and all attributes derived from the vacancy
data. In each panel, attributes are ordered bybαk Q from largest to smallest. These coeﬀicients
typically range from −0.1 to 0.1, where 0.1 implies a 10 percentage point change in the
propensity to advertise a given attribute for each standard deviation increase in employer
32We provide robustness using alternative clustering procedures, featuring smaller or larger clusters.
33For the US, the original study [ Sorkin, 2018, Table II] found this correlation to be 0.53. Our setting differs
from that in Sorkin [2018] along many dimensions: time period, institutions, labor market size (thousands vs.
millions of employers), wage measures (yearly vs. hourly wages), and the definition of employer-to-employer
transitions (monthly vs. quarterly job spells).
24

quality. As shown in Figure2, the baseline prevalence of many attributes is in the 5–30%
range. However, many estimatedαk Q are not statistically different from zero, indicating no
detectable association between those attributes and employer quality.
Panel (a) shows that high-pay employers are more likely to advertise a generous com-
pensation package (“pension scheme,” “insurance scheme,” “collective agreement pay”) and
training opportunities (“on-the-job training”). As documented in Section3.3, only 30% of
ads mention pay information (less than 10% list an actual salary number or bracket), so pay
premiums and advertised pay information are separate concepts. Several attributes related
to the workplace (“good colleagues,” “social environment”) and tasks (“challenging tasks,”
“interesting tasks”) are also positively associated with employer pay. In sum, high-pay em-
ployers tend to advertise a professional environment with a generous compensation package.
Our estimates also show that attributes related to inconvenient hours (e.g., “shift work”)
are more common among high-pay employers, consistent with compensating differentials for
inconvenient work schedules. On the other end, low-pay employers more often advertise a
“part-time contract” or a “temporary job”.
Panels (b) and (c) of Figure4 show bαk Q for the Sorkin value and the poaching index,
respectively. These two measures are strongly correlated, and the overall patterns of associ-
ation between bQg(j) and Ak g(j) are similar. Although high-quality employers advertise many
of the same attributes as high-pay employers, the positive association with inconvenient work
schedules disappears: “shift work” and “weekend/evening/night work” become attributes of
low-quality employers. Conversely, flexible work arrangements, such as “possibility to work
flexible working hours” and “possibility for remote work,” are positively associated with
high-quality employers. In sum, high-quality employers tend to advertise more generous
compensation and better work schedules.
WepresentresultsforaseriesofalternativespecificationsinAppendixFigures A.10–A.14.
The results are robust to extending the sample period (2015–2024 instead of 2021–2024),
varying cluster size (25 or 100 establishments per cluster on average instead of 50), and
using alternative revealed-preference measures of employer quality (Sorkin flow value and
employment size). We also show results for the flow-based measures of employer quality
while controlling for pay premiums in Appendix FigureA.9. As some attributes, such as
“shift work” and “weekend/evening/night work,” are positively correlated with pay (likely
reflecting compensating differentials), this alternative specification reinforces their negative
correlation with these measures, consistent with these attributes entering worker utility
negatively.
25

Figure 4: Publicly Advertised Job Attributes By Employer Values and Pay Premiums.
(a) Pay Premium
Challenging Tasks ··················
Shift Work ·························
Pension Scheme ·····················
Insurance Scheme ···················
Interesting Tasks ··················
Weekend/Evening/Night Work ·········
Social Environment ·················
On-the-Job Training ················
Good Colleagues ····················
Central Location ···················
Collective Agreement Pay ···········
Permanent Job ······················
Company Gym or Sports Team ·········
Variation in Tasks ·················
Full-time Contract ·················
Any Welfare Scheme ·················
Company Cabin ······················
Competitive Pay ····················
Work Involves Travelling ···········
Possibility to Work Flexible Hours ·
Compensation Level ·················
Inclusive Work-life Scheme ·········
Parking Space On Premises ··········
Occupational Health Service ········
Independence in Performing Tasks ···
Hiring Bonus ·······················
Possibility for Remote Work ········
Incentive Pay Scheme ···············
Mortgage Possibility ···············
Flexible/Extended Holidays ·········
Good Career Paths ··················
Beautiful Location ·················
Good Overtime Pay ··················
Shared Office Space ················
Company Canteen ····················
Regular Daytime Work Schedule ······
Overtime Work Required ·············
Responsibility in Job ··············
Full-time/Part-time Choice ·········
On-call Employment ·················
Exempt from Work Hour Regulations ··
Fixed-term Contract ················
Involves Leadership Responsibility ·
Any Other Mention of Pay ···········
Company Vehicle ····················
Part-time Contract ·················
Temporary Job ······················
-.05 0 .05 .1 (b) Overall Sorkin Value
Full-time Contract ·················
Pension Scheme ·····················
Insurance Scheme ···················
Challenging Tasks ··················
Good Colleagues ····················
Competitive Pay ····················
Possibility to Work Flexible Hours ·
Interesting Tasks ··················
Central Location ···················
Permanent Job ······················
Work Involves Travelling ···········
Company Gym or Sports Team ·········
Involves Leadership Responsibility ·
Possibility for Remote Work ········
Good Career Paths ··················
Compensation Level ·················
Company Cabin ······················
Social Environment ·················
On-the-Job Training ················
Independence in Performing Tasks ···
Any Welfare Scheme ·················
Mortgage Possibility ···············
Good Overtime Pay ··················
Incentive Pay Scheme ···············
Flexible/Extended Holidays ·········
Occupational Health Service ········
Company Canteen ····················
Responsibility in Job ··············
Shared Office Space ················
Fixed-term Contract ················
Parking Space On Premises ··········
Exempt from Work Hour Regulations ··
Regular Daytime Work Schedule ······
Overtime Work Required ·············
Full-time/Part-time Choice ·········
Hiring Bonus ·······················
Beautiful Location ·················
Inclusive Work-life Scheme ·········
Variation in Tasks ·················
Company Vehicle ····················
Any Other Mention of Pay ···········
Collective Agreement Pay ···········
On-call Employment ·················
Shift Work ·························
Temporary Job ······················
Part-time Contract ·················
Weekend/Evening/Night Work ·········
-.15 -.1 -.05 0 .05 .1 (c) Poaching Index
Pension Scheme ·····················
Insurance Scheme ···················
Full-time Contract ·················
Challenging Tasks ··················
Good Colleagues ····················
Central Location ···················
Interesting Tasks ··················
Possibility to Work Flexible Hours ·
Collective Agreement Pay ···········
Social Environment ·················
Work Involves Travelling ···········
Company Gym or Sports Team ·········
Permanent Job ······················
Competitive Pay ····················
On-the-Job Training ················
Involves Leadership Responsibility ·
Compensation Level ·················
Possibility for Remote Work ········
Company Cabin ······················
Inclusive Work-life Scheme ·········
Independence in Performing Tasks ···
Occupational Health Service ········
Mortgage Possibility ···············
Flexible/Extended Holidays ·········
Parking Space On Premises ··········
Variation in Tasks ·················
Any Other Mention of Pay ···········
Good Overtime Pay ··················
Company Canteen ····················
Any Welfare Scheme ·················
Fixed-term Contract ················
Exempt from Work Hour Regulations ··
Hiring Bonus ·······················
Shared Office Space ················
Regular Daytime Work Schedule ······
Overtime Work Required ·············
Beautiful Location ·················
Responsibility in Job ··············
Full-time/Part-time Choice ·········
Company Vehicle ····················
Incentive Pay Scheme ···············
Good Career Paths ··················
Shift Work ·························
On-call Employment ·················
Temporary Job ······················
Part-time Contract ·················
Weekend/Evening/Night Work ·········
-.1 -.05 0 .05 .1 .15
Notes: This figure shows parameter estimates and 90% confidence intervals from separate regressions of the share of each ad attribute on Employer
Pay Premium, Overall Sorkin Value, and Poaching Index, capturing the change in the fraction of ads with each job attribute associated with a
standard deviation increase in employer value. Estimations are done at the employer-cluster level for the period from 2021 to 2024, and are weighted
by the number of worker-years. Appendix Figure A.9 documents regressions on Overall Sorkin Value and Poaching Index while controlling for Pay
Premium, Appendix Figure A.10 documents the corresponding results for the period 2015-2024, while Appendix Figures A.11-A.12 show results using
smaller and larger clusters. Appendix Figures A.13-A.14 documents corresponding results by Sorkin Flow Value and Employment Size.
26

Overall, the correlations in Figure4 suggest that the content of job ads is informative.
Attributes typically seen as positive (financial benefits, flexible schedules, job stability) are
more likely to be advertised by high-quality employers, while low-quality employers more
often advertise attributes seen as negative (constrained schedules, temporary positions).
Advertised information therefore does not appear to be “cheap talk.”
However, advertised attributes need not translate directly into actual job characteristics,
for two reasons. First, employers may not be able to commit to all advertised attributes,
particularly subjective ones such as “social environment” and “good colleagues.” These may
be better interpreted as signals of workplace culture than as concrete commitments. Second,
employers may omit actual job characteristics from the ad: for instance, an employer may
offer a competitive salary without mentioning it explicitly upfront.
4.1.3 Predicting the Quality of Employers from Job Ads
How predictive are advertised job attributes of employer quality? To quantify the predictive
power of the pay and non-pay content of job ads, we estimate
bQg(j) =β0 + X
k
βk ·Ak g(j) +βXXg(j) +εQ g(j), (2)
at the employer-cluster level, whereg(j) maps employerj to clusterg, Ak g(j) is the share of
ads from employers in clusterg featuring attributek, Xg(j) is a vector of industry, location,
and occupation controls capturing other commonly observed job ad characteristics, andεQ g(j)
is an error term. The regression is weighted by the number of worker-years in each cluster.
We use the adjustedR2 of regression (2) as our summary measure of predictive power,
reporting versions with and without the controls inXg.34 Figure 5 shows this measure for
alternative estimates of employer quality bQg(j), decomposed across three broad groups of
attributes: pay attributes (red bars), non-pay attributes (blue bars), and other ad charac-
teristics (black bars).35 Since the contribution of each group of attributes depends on the
order in which they are introduced in (2), we report a Shapley value decomposition.
Figure 5 shows that job ad content meaningfully predicts employer quality across all
measures we consider. Non-pay attributes (blue bars) contribute two to three times as much
34The formula used to calculate predictive power is Adjusted R2 = 1 − (SSres/d fres)/(SStotal/d ftotal)
where SSres is the residual sum of squares, d fres is the number of employer clusters (1,422 in our baseline)
minus the number of explanatory variables, and SStotal and d ftotal are from a regression on a constant only.
The partial R2 is the share of variation unexplained by baseline controls alone but explained when job ad
attributes are added: Partial R2 = (R2 f ull − R2 baseline)/(1 − R2 baseline) where R2 f ull (R2 baseline) is the adjusted
R2 from a regression with (without) job attributes.
35Other ad characteristics include the number of advertised attributes, the number of words in the ad,
and whether the employer name is mentioned.
27

Figure 5: Predictive Power of Publicly Advertised Job Attributes.
Overall Partial Overall Partial Overall Partial Overall Partial Overall Partial
Pay Overall Flow Poaching Employment
Premium Sorkin Value Sorkin Value Index Size
0
.1
.2
.3
.4
.5
.6
.7
.8
.9
1
Adjusted R
2
 (Shapley)

     Pay
 Attributes
  Non-Pay
 Attributes
      Other Ad
 Characteristics
Notes: This figure shows adjusted R2s from regressions of estimated model parameters on pay and non-pay
job attributes and other ad characteristics retrieved in the text analysis, including the number of words in
the ad, indicators for ad posted online, disclosure of company name, and the overall number of attributes
in the ad. We decompose R2s into the contributions of Pay Attributes, Non-Pay Attributes, and Other
Ad Characteristics using the Shapley value decomposition. Estimations are done at the employer-cluster
level for the four-year period from 2021 to 2024, and are weighted by the number of worker-years in each
cluster. Overall R2s are from regressions that include ad attributes and other ad characteristics, while partial
R2s are from regressions that also control for the composition of industry, occupation and location in each
cluster. Industry and occupation controls are defined at the two-digit level. Location indicators split local
municipalities into deciles, with municipalities in the same group having similar number of workers (Oslo as
an own group). The sample corresponds to the “Employer Quality Sample” in Table 1. Appendix Figure
A.15 reports the corresponding results using alternative clustering procedures, while Appendix Figure A.16
provides results for the 2015-2024 period and Appendix Figure A.18 provides results by main industry.
as pay attributes (red bars), with other ad characteristics (black bars) contributing broadly
as much as pay attributes. Based solely on job attributes, without the controls inXg(j), we
explain about 60% of the variation in employer quality. Conditioning onXg(j), job attributes
still explain 15% to 20% of the remaining variation, as shown by the partialR2 in Figure
5. These findings are robust to using smaller or larger employer groups (Appendix Figure
A.15) and to extending the sample period to 2015–2024 (Appendix FigureA.16).
We further explore the adjusted-R2 reported in Figure5 through the following two exer-
cises. First, we decompose the adjusted-R2 by finer attribute categories in Appendix Figure
A.17, reporting the contribution of each of the ten categories from Table2 separately. This
exercise indicates that explanatory power is broadly distributed across attribute categories
28

rather than concentrated in a few, though attributes related to compensation and inconve-
nient hours consistently contribute more, as shown by the Shapley value decompositions in
panels (a) and (b) of Appendix FigureA.17.
In a similar spirit, AppendixE documents that these patterns are robust to focusing
on individual attributes. Specifically, we use Lasso regression in Equation (2) to select the
most predictive individual job attributes for each employer quality measure. This confirms
that attributes related to hours of work, contract duration, pension scheme, and collective
agreement pay are highly predictive of employer quality.
4.2 Evidence from Linked Ad-Hire Data
How well do job attributes advertised in job postings correspond to realized job characteris-
tics observed in administrative data? For a limited set of attributes, we are able to construct
counterparts of advertised attributes in the matched employer–employee data, which allow
us to examine the concordance between advertised and realized job attributes. We perform
this assessment using the linked ad-hire sample discussed in Section2.3.
Wefocusonasubsetofattributes byconstructingbinaryindicatorsfromthe registerdata
that closely match those retrieved from job ad texts. The attributes with the most direct
counterpart in administrative records are “shift work” and contract duration (“permanent
job” or “temporary job”). From reported contractual hours, we also construct indicators for
“full-time contract” (≥30 hours per week) and “part-time contract” (<30 hours per week).
Further, using detailed spell-level information on payroll and in-kind benefits, we construct
three further attributes: bonus pay (“incentive pay scheme”), travel-related reimbursements
(“work involves travelling”), and company car benefits (“company vehicle”). Finally, we
define jobs located in one of the four largest cities in Norway as offering a “central location.”
In most cases, the attributes we extract from administrative records are contractual in
nature and unlikely to be misreported in job ads. Still, some comparisons are ambiguous:
our hours threshold for full-time work may not align with the threshold employers use in
postings, and our classifications of incentive pay and travel involvement depend on arbitrary
cutoffs. Moreover, negotiations between employers and workers during the recruitment pro-
cess may result in final contracts that deviate from what was advertised. Divergence between
posted and realized attributes therefore does not necessarily imply cheap talk. Despite these
limitations, we view this exercise as a novel feature of our setup.
Table 4 compares attribute prevalence in job ads and in administrative records for the
linked ad-hire sample. Columns (1) and (2) show that prevalence lines up closely across the
two sources: attributes we rarely detect in job ads, such as “incentive pay scheme,” “com-
29

pany vehicle,” and “work involves traveling,” are also rare in register data, while common
contractual attributes such as “part-time contract,” “shift work,” and “temporary job,” are
common in both. Column (3) reports the share of linked ads and job spells where the two
sources agree. We find success rates are generally above 90%. The main exceptions are
“temporary job” and “part-time contract,” where match rates are closer to 75%. This could
reflect genuine deviations from the listed attributes, but may also stem from measurement
error either in the attribute definitions or in the construction of the ad-hire sample.
Table 4: Publicly Advertised Job Attributes and Observed Attributes in Register Data.
Cohen’s κ
Attribute Prevalence Relative to Random Matching Within:
Register Job Ads Success Rate All Jobs Occuption Industry Occ. # Ind.
(1) (2) (3) (4) (5) (6) (7)
Incentive Pay Scheme 2.4% 3.5% 95.4% 0.25 0.21 0.18 0.18
Part-time Contract 23.0% 22.4% 78.5% 0.40 0.25 0.41 0.24
Shift Work 13.1% 12.4% 87.9% 0.44 0.19 0.44 0.17
Temporary Job 30.3% 27.2% 75.8% 0.44 0.34 0.42 0.34
Work Involves Travelling 5.0% 5.6% 92.0% 0.28 0.13 0.17 0.11
Central Location 27.1% 23.9% 76.1% 0.43 0.41 0.41 0.39
Company Vehicle 1.0% 2.0% 97.7% 0.18 0.17 0.16 0.16
Notes: This table documents attribute prevalence and the correspondence between linked attributes in
register and job ads data. Columns (1) and (2) document attribute prevalence in register and job ads data.
Column (3) documents how often job ad attributes correspond to the information provided in register data
(success rate). Column (4) compares the success rate to the expected success rate when forming random
links between ads and hires using Cohen’s κ. Hired worker attributes are binary indicators extracted from
matched employer-employee data, and are measured as follows: Incentive Pay Scheme indicates that bonus
pay accounts for > 5% of total pay; Full-time Contract indicates contractual hours > 30 hours a week; Shift
Work and Temporary Job are directly reported by employers; Work Involves Traveling indicates that the
worker had at least two recorded travel expenses; Central Location indicates that the establishment is located
in one of the four largest Norwegian cities; and Company Vehicle indicates company car benefits recorded for
tax purposes. For the purpose of this classification, attributes relating to Full-time Contract and Permanent
Job correspond to the counterpart of Part-time Contract and Temporary Job attributes, respectively, and
are thus left out from this table, although these attributes are also found in the register data. The success
shares and Cohen’s κ for these attributes can be inferred from their respective counterparts. Appendix Table
A.2, Column (2), documents the sample characteristics of individuals that were uniquely linked to a job ad.
Notably, the success rates in Column (3) of Table4 depend not only on the predictive
value of job ads but also on the prevalence rates reported in Columns (1)-(2), i.e., differences
in success rates may simply reflect differences in incidence. To address this, we use Cohen’s
κ-coeﬀicient, which measures agreement between the two sources relative to what would
30

be expected under random matching [Cohen, 1960].36 Columns (4)-(7) of Table4 report
Cohen’s κ estimates across different levels of random matching, consistently showing that
20–40% of the agreement between job ads and register data exceeds what could be expected
purely based on random matching. We take this as evidence that posted job attributes
meaningfully predict the job characteristics observed in employment contracts.
4.3 Evidence from Survey Experiment with Job Ads
We now present evidence from a survey experiment byBhuller et al.[2024], which elicited re-
spondents’ preferences over real job ads using hypothetical choice scenarios. Each respondent
i faced multiple choice scenarioss, each presenting two alternativescis(j,j′) = {cisj,c isj′}, and
stated their preferred alternative. Within each scenario, both ads were randomly drawn from
the same sector and broad occupation, and therefore differences between alternatives reflect
within-sector-occupation differences across employers, notably in posted job attributes. We
use respondents’ choices to evaluate the information content of job ads in two steps.
As a first step, we use the non-pay job attributesAj = (A1 j,...,A K j ) retrieved from
job ad texts, as described in Section 3, together with respondents’ choices, to estimate
how the presence of specific attributes affects choices and to construct willingness-to-pay
(WTP) estimates for workplace amenities. Importantly, respondents could read the job
ad texts associated with each alternative, so their choices may reflect preferences over the
job attributes they could infer from the ads. Using the survey responses, we construct
binary indicatorsDis(j,j′) = 1[cisj ≻cisj′] for respondenti’s preferred alternative in scenario
s(j,j ′). Using the binary indicatorsDis(j,j′), non-pay job attributes(Aj,A j′) and employer
pay premiums(wj,w ′ j), we estimate a conditional logit model. Standard errors are clustered
at the respondent level, as each respondent faced many scenarios.
Table 5 reports the results from the choice model. Column (1) presents the parameter
estimates of the choice model where we used a subset of advertised non-pay attributes and
employer pay premium as explanatory variables. Column (3) provides the implied WTP
estimates γk for these non-pay job attributes, constructed as the ratios of the attribute-
specific choice parameters and the employer pay premium estimate reported in Column (1).
In determining which non-pay attributes to include in the model, we use two criteria. First,
we include attributes that have been emphasized in the literature as salient dimensions of
employer quality, such as inconvenient or convenient hours (e.g., shift work, flexible hours)
36The expected success rate with random matching is pr = sadsjob + (1 − sad)(1 − sjob), where sad is
the share of ads with detected attribute, and sjob is the corresponding share of job spells with the detected
attribute. The Cohen’s κ-coeﬀicient is defined as: Cohen’s κ = ( po − pr)/(1 − pr), where po and pr denote
observed success rates and the expected success rate with random matching, respectively. Cohen’s κ is zero
whenever the observed success rate po equals pr, and is one whenever po is 100%.
31

and fringe benefits (e.g., insurance scheme, mortgage possibility). Second, we focused on
attributes that were estimated as significant in the preceding analysis.37 In Columns (2) and
(4), we provide an additional set of estimates, where we include the remaining job attributes
mentioned in Section3 as additional controls in the choice model. We show that our WTP
estimates for the salient attributes are robust to controlling for additional non-pay attributes.
We use the WTPs reported in Column (4) as part of the structural analysis in Section5.
Table5 shows that respondents place high value on amenities such as “convenient hours”
(e.g., “possibilitytoworkflexiblehours”), andrequiresubstantialcompensationfordisameni-
ties such as a “temporary job” or “inconvenient hours” (e.g., “shift work”). The estimates
all have the expected signs and their magnitudes are in line with prior literature estimating
WTPs from similar hypothetical choice experiments. As noted inAndresen et al. [2026],
although the survey targeted university students, the WTPs for this group closely resemble
estimates found in the literature for broader populations.38 For instance, we estimate a
WTP for remote work at 0.065 in Column (4), which is similar in magnitude to the esti-
mates reported byMas and Pallais[2017] (0.078) andMaestas et al.[2023] (0.041) for the
US. Similarly, the estimates inDatta [2019] imply a WTP of -0.242 for temporary job in the
UK, whileVan Landeghem et al.[2024] find a WTP of 0.192 for flexible hours in Belgium,
very close to the WTPs in Table5, Column (4). For the estimates that are specific to our
setting, we find that the signs and magnitudes of our estimates are empirically plausible.
For instance, jobs advertising good career opportunities have an estimated WTP of around
0.085, while working alongside qualified colleagues has a WTP of 0.094. We interpret this
as evidence that respondents use advertised job attributes to guide their survey choices.
In the second step, we assess how well respondents’ stated choices align with the revealed-
preference measures of employer quality described in Section4.1 by linking their binary
choicesDis(j,j′) to these quality measures.39 Specifically, for each employer quality measure,
we compute the difference in employer quality between the two alternatives,∆ ˆQis(j,j′) =n
ˆQg(j) − ˆQg(j′)
o
is(j,j′) , using the notation in Section4.1. Finally, we estimate (local polyno-
37As described in Section 3, our text analysis extracts 47 distinct attributes from the job ads, while in
Section 4.1 we show that not all of these attributes hold predictive value for the employer quality measures.
38Andresen et al. [2026] provide WTP estimates for a smaller set of workplace amenities that featured
in both hypothetical choices over real ads and purely hypothetical jobs that were experimentally designed,
along with a literature overview. The estimates in Table 5 are similar to those in Andresen et al. [2026],
though they use a more flexible mixed logit model with repeated choices [ Revelt and Train , 1998, 1999].
39In recent related work, Caldwell et al. [2025b] relate survey respondents’ pay expectations across actual
employers to pre-estimated AKM employer pay premiums, where the latter are estimated using data from the
population at large [ Abowd et al. , 1999]. We instead relate respondents’ preferred choices across real-world
job ads to alternative employer quality measures, including pay premiums. Besides these similarities, the
survey designs depart significantly across the two studies. In particular, the survey in Caldwell et al. [2025b]
does not feature job ads, and is targeted at a broader population of workers employed in full-time jobs.
32

Table 5: Survey Experiment: Choice Parameters and Willingness-to-Pay Estimates.
Conditional Logit Willingness to Pay
Choice Parameters Estimates
(1) (2) (3) (4)
Temporary Job -0.239∗∗∗ -0.252∗∗∗ -0.263∗∗∗ -0.254∗∗∗
(0.0217) (0.0226) (0.0458) (0.0433)
Convenient Hours 0.151∗∗∗ 0.188∗∗∗ 0.167∗∗∗ 0.189∗∗∗
(0.0189) (0.0203) (0.0320) (0.0345)
Inconvenient Hours -0.320∗∗∗ -0.280∗∗∗ -0.353∗∗∗ -0.282∗∗∗
(0.0372) (0.0388) (0.0808) (0.0667)
Insurance Scheme 0.0390 0.104 ∗∗∗ 0.0431 0.105 ∗∗∗
(0.0272) (0.0338) (0.0304) (0.0383)
Mortgage Possibility 0.265∗∗∗ 0.116 0.292 ∗∗∗ 0.117
(0.0691) (0.0738) (0.0962) (0.0779)
Career Opportunities 0.0600∗ 0.0839∗∗ 0.0663 0.0845 ∗∗
(0.0336) (0.0382) (0.0406) (0.0425)
Possibility for Remote Work 0.0591 ∗∗∗ 0.0649∗∗∗ 0.0653∗∗∗ 0.0653∗∗∗
(0.0122) (0.0130) (0.00482) (0.00482)
Good Colleagues 0.0713∗∗∗ 0.0935∗∗∗ 0.0788∗∗ 0.0941∗∗∗
(0.0249) (0.0268) (0.0323) (0.0333)
Inclusive Work-life Scheme 0.204∗∗∗ 0.172∗∗ 0.226∗∗ 0.173∗∗
(0.0686) (0.0743) (0.0894) (0.0823)
Company Gym or Sports Team 0.237∗∗∗ 0.232∗∗∗ 0.262∗∗∗ 0.234∗∗∗
(0.0364) (0.0402) (0.0617) (0.0585)
Company Cabin 0.177∗∗∗ 0.270∗∗∗ 0.195∗∗ 0.272∗∗∗
(0.0630) (0.0681) (0.0828) (0.0913)
Employer Pay Premium 0.906∗∗∗ 0.993∗∗∗ – –
(0.174) (0.186)
Controls:
Respondent Fixed Effects ✓ ✓ ✓ ✓
Survey Interview Module ✓ ✓ ✓ ✓
Travel Time to Job ✓ ✓ ✓ ✓
Additional Job Attributes ✓ ✓
Number of Respondents 1,040 1,040 1,040 1,040
Number of Choice Scenarios 37,420 37,420 37,420 37,420
Standard errors in parentheses. ∗ p < 0.10, ∗∗ p < 0.05, ∗∗∗ p < 0.01.
Notes: This table shows parameters estimates from conditional logit choice models of hypothetical job
choices estimated using data collected in a survey experiment featuring real job ads performed by Bhuller
et al. [2024]. Using the text analysis approach in Section 3, we construct indicators for the presence of
each job attribute listed in Figure 2 for every job ad. Using the retrieved job attributes, we estimate choice
models allowing choices to depend on the vector of non-pay job attributes Aj = (A1 j , . . . , AK j ) and employer
pay premiums (as in Section 4.1) associated with each job ad. Columns (1)-(2) provide the estimated choice
parameters, while Columns (3)-(4) provide the implied willingness-to-pay estimates γk, constructed for each
job attribute k as the ratio of the k-attribute choice parameter and the pay premium estimate. All models
include controls for respondent fixed effects interacted with indicators for survey modules, and travel time
between job location and respondent residence. Standard errors are clustered at the respondent level.
33

Figure 6: Survey Experiment: Choice Probability and Employer Quality.
(a) Pay Premium
0.028***
[0.004]
.4
.45
.5
.55
.6
Choice Probability
0
.1
.2
.3
.4
.5
.6Density
−2 −1.5 −1 −.5 0 .5 1 1.5 2
Standarized Difference in Pay Premium
(b) Sorkin Overall Value
0.058***
[0.004]
.35
.4
.45
.5
.55
.6
.65
Choice Probability
0
.2
.4
.6
.8
1
Density
−2 −1.5 −1 −.5 0 .5 1 1.5 2
Standarized Difference in Sorkin Overall Value (c) Poaching Index
0.064***
[0.004]
.35
.4
.45
.5
.55
.6
.65
Choice Probability
0
.1
.2
.3
.4
.5
.6Density
−2 −1.5 −1 −.5 0 .5 1 1.5 2
Standarized Difference in Poaching Index
Notes: This figure shows the relationships between the probability that survey respondents rank a job ad
above the alternative option (right y-axis) and the standardized difference in employer quality across the
job ad options (x-axis), as estimated using data on hypothetical choices of real job ads collected in a survey
experiment performed by Bhuller et al. [2024]. We assign the alternative employer quality measures defined
in Section 4.1 to each job ad, and provide the associations between Employer Pay Premium (panel a), Sorkin
Overall Value (panel b) and Poaching Index (panel c), and respondents’ subjective rankings of job ads
based on their hypothetical choices across two randomly assigned ads in each scenario. The black lines show
estimates from local polynomial regressions of choice probabilities on the standardized difference in employer
quality, estimated separately for each quality measure, along with 95% confidence intervals. Standard errors
are clustered at the respondent level. In each panel, we also report the OLS regression estimates from linear
probability models on each employer quality measure, providing the expected change in choice probability
(reported in percentage points) associated with one standard deviation increase in the employer quality
measure. The associated standard errors are reported in square brackets. We further show the distribution
of standardized differences in employer quality (left y-axis), ranging between -2 and 2 in each panel.
34

mial) regressions ofDis(j,j′) on the standardized quality differences∆ ˆQis(j,j′).
The results are shown in Figure6. Panel (a) shows how respondents’ choice probabili-
ties relate to standardized differences in employer pay premiums. Respondents’ choices are
clearly positively aligned with differences in employer pay premiums: a one standard devi-
ation difference is associated with about three percentage points higher choice probability.
Notably, respondents were not provided explicit pay information in the job ad texts, so we
interpret this as evidence that respondents value high-paying jobs and were able to infer
signals correlated with pay premiums from the ad texts. In Panels (b)-(c), we consider two
alternative measures of employer quality, the Sorkin overall value and the poaching index,
respectively, and similarly show a clear alignment: a one standard deviation difference in
each measure is associated with a six percentage points higher choice probability. We inter-
pret this as evidence that respondents’ stated choices are aligned with revealed-preference
employer quality measures, suggesting that ad texts are informative of employer quality.40
5 Job Attributes and Labor Market Inequality
Having documented that job ad attributes predict employer quality, we now quantify their
contribution to employer-level inequality in the labor market. We incorporate the ad infor-
mation into an otherwise standard static monopsony framework where workers value jobs
at alternative employers differently [Card et al., 2018, Lamadon et al., 2022]. We can then
introduce a distinction between advertised amenities, derived from the ad information, and
intrinsic amenities, which capture employer characteristics unobserved in job ads and valued
by workers. Our goal is to separately estimate their contribution to firm-level inequality.
5.1 A Monopsony Framework with Detailed Job Attributes
Consider a static economy populated by a large number of workers indexed byi and a large
number of employers indexed byj ∈ {1,...,J }. Each employerj posts a wagewj and a job
attribute bundleaj that workers observe at no cost. We assume that workeri with a job at
40While the evidence provided above shows that survey respondents’ stated choices in a controlled setting
align with population-wide employer quality measures, we show in Appendix Table A.5 that these measures
are also clearly associated with the duration of posted vacancies. As described in Section 2, our job ads data
has information on the duration of posted vacancies, measured as the difference between the date when an
ad was posted or registered and when it was either filled or removed. Recent evidence provided by Mueller
et al. [2024] and Bassier et al. [2025], respectively, shows that the employer pay premiums and the posted
pay are negatively related to the duration of posted vacancies, consistent with the notion that high-pay
employers are more attractive in the labor market. In Appendix Table A.5, we find an elasticity of vacancy
duration with respect to the employer pay premium of about −0.15 (similar to Mueller et al. [2024]), while
vacancy durations are around 3-4% shorter for ads with one standard deviation higher employer quality.
35

employerj derives indirect utility
uij = lnwj + lnaj +ξij =uj +ξij, (3)
whereuj = lnwj + lnaj denotes the indirect utility of working for employerj common to all
workers, andξij is a worker-specific taste shock for employerj.
We impose standard restrictions on the idiosyncratic utility shifters{ξij} to obtain a
closed-form expression for the labor supply curve specific to each employerj. The taste
shocks {ξij} are assumed to be workers’ private information, independent across (i,j) pairs,
and distributed according to a Gumbel distribution with scale parameterσ. Under these
assumptions, as is well-known, the probability that workeri chooses employerj posting wage
wj and amenity bundleaj is given by
Pr

j = arg maxj′∈{1,...,J}{uij′}  = (wjaj)σU −1, (4)
where we introduce the notationU := PJ k=1(wkak)σ. Letting ¯ℓ denote the workforce in the
economy, we arrive at the labor supply curve faced by employerj,
ℓj(wj) = ¯ℓaσ jU −1wσ j, (5)
where, in line with prior work, we assume that employers are atomistic and ignore the effect
of adjusting its own wage rate on the indexU. As a result, the parameterσ, which scales the
worker-specific utility shifter, can be interpreted as the labor supply elasticity in Equation
(5), and we exploit this interpretation in the model estimation.
Weincorporatethenon-payjobattributeinformationretrievedfromjobadsbyspecifying
the amenity bundle offered by employerj as
lnaj =γAj + ln ˜aj. (6)
The utility derived from the non-pay amenity bundlelnaj is made up of two components.
The first component is a vectorAj = (A1 j,...,A K j ) of advertised non-pay attributes whose
elements directly map to the ad attributes described in Section3. More specifically, for some
job attributek at employerj, the elementAk j ofAj is defined as the share of job ads posted
by that employer featuring attributek, similarly to the definitions used in Section4.1. With
this definition, the coeﬀicientγk can be interpreted as the WTP for job attributek.41 We
41If all jobs listed by employer j feature attribute k, then Ak j = 1 and, since the indirect utility specified
in Equation ( 3) is in log-wage units, γk is approximately the percentage wage change required to make the
worker indifferent between a job with and without the attribute all else equal.
36

refer toγAj as the advertised component of non-pay utility .42
The second component of the non-pay amenity bundle, ln ˜aj, is left unrestricted. It
captures unobserved employer characteristics that enter workers’ utility but are explicitly not
listed in job ads, such as perceptions about company brand (positive) or stressful working
conditions (negative). The termln ˜aj is therefore the net effect on workers’ utility of these
unobserved attributes, and we refer to it as theintrinsic component of non-pay utility .
An attractive feature of the framework described by Equations (3)-(6) is that it does
not restrict the relationship between the three components of workers’ indirect utility:lnwj,
γAj, and ln ˜aj. Notably, for a given value of the labor supply elasticityσ, the advertised
and intrinsic components of non-pay utility can reflect either compensating or augmenting
differentials, and we test for the nature of each component in our estimation.
5.2 Estimation Procedure and Parameter Estimates
We combine annual matched employer-employee data and job ad data from the datasets
described in Section 2. We use establishments as the empirical counterpart to employers
in the model. We restrict the sample to larger establishments for which we can credibly
estimate the employer-specific components. Specifically, we only retain employers with at
least30stayersand15moversovertheperiod, wherestayersareworkersobservedatthesame
employer in the following period, and movers are workers observed at a different employer.
As shown in Table1, these restrictions leave us with a sample of 12,973 establishments.
Details on the composition of this sample can be found in Appendix TableA.1.
The model is estimated in four broad steps. First, we reduce the number of parameters to
be estimated by clustering employers paying similar wages.43 Second, we use well-identified
pre-estimated parameters for the labor supply elasticity (σ) and the WTP vector (γ). For
the labor supply elasticity, we use the pass-through estimates for Norway reported inBhuller
et al. [2025, Table 2] using firm-level demand shocks. Their central pass-through estimate
implies a labor supply elasticity estimatebσ of 3.29.44 For the WTP parameters, we use the
estimates derived from the survey experiment featuring real job ads described in Section
42To the extent employers provide additional signals about workplace amenities in job ads that are not
captured by our text analysis or enter into γAj, we may interpret this component as providing a lower bound.
43The clustering provides a surjective mapping j → g, where j denotes the employers in the estimation
sample and g the employer group to which j belongs. The parameters we recover are therefore cluster-level
estimates. As an example, we derive estimates for dln ˜ag(j). For brevity, we use the notation dln ˜aj for dln ˜ag(j).
44This estimate falls within the range of elasticities typically found in the literature (see Azar and Marinescu
[2024] and Kline [2025] for overviews), and is close to estimates from recent studies using credible designs.
For instance, Dube et al. [2025] find firm-level labor supply elasticities ranging between 1.7 and 2.6, while
Kroft et al. [2025] report elasticities ranging from 3.5 to 4.1 and Bassier et al. [2022] find an elasticity of 4.2.
37

4.3. In particular, we use the WTP estimatesbγ from Column (4) of Table5.45 Since the
survey experiment is restricted to full-time job ads, we construct a WTP estimate for jobs
that offer part-time contracts based on recent evidence on employer-level hours constraints
in Dube et al.[2022] andLachowska et al.[2025].46 Third, we estimate a standard two-sided
wage regression with worker and employer fixed effects and set the pay premiumslnwj to
the estimated employer effects. Finally, we recover the remaining parameters by maximum
likelihood using Equation (4) conditional on the pre-estimated parametersbσ, bγ, and dlnwj.
Appendix D provides details on these steps.
Table 6 reports summary statistics on the dispersion of the estimated components of
workers’ indirect utility. Panel A analyzes the variance of these components, usingVar(dlnwj)
as a benchmark. A key statistic of interest is the dispersion of employer utilitybuj relative
to employer pay premiums dlnwj, which we estimate at 2.2. This represents a significant
departure from compensating differentials, which would imply a relative dispersion close to
zero. Our estimate of Var(buj)/Var(dlnwj) is close to Taber and Vejlin[2020], lower than
Hall and Mueller[2018], and larger thanMaestas et al.[2023]. As the prior work reporting
similar statistics differs along many dimensions (e.g., data source, modeling assumptions), we
are cautious about making direct comparisons, but our estimate reassuringly falls within the
broad range reported in the literature. Details on this comparison, including the construction
of the relevant dispersion statistics in each study, are provided in AppendixD.
The remaining components of workers’ indirect utility in Table6 are specific to our
framework, in which we can distinguish between the listed component of amenitiesbγAj and
the intrinsic componentdln ˜aj. Panel A shows that the relative dispersion of the advertised
component, Var(bγAj)/Var(dlnwj) = 0 .704, is nearly as large as pay dispersion. The rel-
ative dispersion of the intrinsic component is even larger, withVar(dln ˜aj) exceeding both
other components by a factor of three. Panel B shows how each amenity component co-
moves with the pay component. The advertised component augments pay differentials
(Corr(bγAj, dlnwj) > 0), while the intrinsic component acts as a compensating differential
(Corr(dln ˜aj, dlnwj)< 0). Taken together, the total amenity component implies compensating
differentials (Corr(bγAj + dln ˜aj, dlnwj) < 0), as the intrinsic component quantitatively domi-
nates the advertised component. However, sinceCorr(bγAj + dln ˜aj, dlnwj)> −1, we still find
that our model estimates imply substantial utility dispersion across employers.
These results suggest that isolating advertised amenities is helpful for understanding the
employer-level drivers of labor market inequality. Quantitatively, advertised amenities are
45Although these parameters could in principle be estimated within the model, we use the well-identified
estimates from Section 4.3 to reduce the number of parameters that we need to estimate numerically.
46We assign a WTP of -0.0785 for jobs that offer part-time hours, which is one minus the average WTP
estimate for jobs offering full-time hours reported in Dube et al. [2022] and Lachowska et al. [2025].
38

Table 6: Monopsony Framework: Dispersion of Utility Components.
Measure Value
Panel A. Ratio of Variance to Variance of Pay Premiums (lnwj)
Employer Utility Value (uj) 2.200
Advertised Amenity (γAj) 0.704
Intrinsic Amenity (ln ˜aj) 3.075
Total Amenity (γAj + ln ˜aj) 1.926
Panel B. Correlations of Components of Utility (uj)
Corr(lnwj,γA j) 0.547
Corr(lnwj, ln ˜aj) -0.469
Corr(γAj, ln ˜aj) -0.630
Corr(lnwj,γA j + ln ˜aj) -0.262
Notes: The table shows summary statistics of the three employer-level components of workers’ indirect utility
estimated based on the model described in Equations ( 3)-(6): pay premiums, advertised non-pay amenities,
and intrinsic non-pay amenities. All employer-level statistics are weighted by employment size.
a substantial source of utility dispersion and tend to reinforce pay differences. However,
they only partly account for workers’ preferences over employers: the intrinsic component
is even more dispersed relative to pay and tends to attenuate employer pay differences. As
the advertised amenitiesbγAj and the intrinsic amenitiesdln ˜aj are negatively correlated, the
variance of total amenities (bγAj + dln ˜aj) is lower than the sum of variances of its components.
More broadly, our framework helps bridge the gap between the empirical labor literature
analyzing specific attributes [e.g.,Maestas et al., 2023], analogous toγAj and its components
in isolation, and the structural labor literature that collapses amenities into a scalar index
[e.g., Morchio and Moser, 2024], analogous tolnaj =γAj + ln ˜aj in our framework.
5.3 Contribution of Amenities to Labor Market Inequality
To further characterize the employer-side determinants of labor market inequality, we con-
sider counterfactual scenarios in which non-pay amenities are equalized across employers.
We report results for three counterfactual scenarios, switching off in turn: advertised job at-
tributes (Aj = 0), intrinsic job attributes (ln ˜aj = 0), and both components simultaneously.
In each scenario, we recompute workers’ choices and simulate a counterfactual distribution of
employmentsizeforeachemployerfromEquations( 3)–(6), holdingallotherparametersfixed
at their estimated values. These counterfactuals should therefore be interpreted as partial
39

equilibrium responses to changes in the components of non-pay utility. For instance, the “ad-
vertised amenities turned off” counterfactual corresponds to a policy imposing that all jobs
have the baseline attributes implied byAj = 0, so that workers maximizelnwj + ln ˜aj +ξij
over the set of employers{1,...,J }.
Table 7: Monopsony Framework: Counterfactual Analyses.
Counterfactual Scenarios
Advertised Intrinsic All
Amenities Amenities Amenities
Turned Off Turned Off Turned Off
(1) (2) (3)
Panel A. Employer Pay Premium
Average Relative to Baseline -0.023 0.038 0.015
Variance Relative to Baseline 1.132 0.747 0.772
Panel B. Employer Utility Value
Average Relative to Baseline 0.048 -0.001 -0.047
Variance Relative to Baseline 1.150 1.077 0.351
Variance of Utility / Variance of Pay 2.237 3.170 1.000
Panel C. Employer Size
Average Relative to Baseline -0.035 0.031 0.147
Variance Relative to Baseline 1.060 1.021 0.452
Notes: The table reports summary statistics for the three counterfactual scenarios: Column (1) shows the
outcomes when the advertised amenities are turned off ( Aj = 0 ), while Column (2) considers the scenario
when the intrinsic amenities are turned off ( ln ˜aj = 0 ), and Column (3) considers the scenario when all
amenities are turned off (both Aj = 0 and ln ˜aj = 0). A verage relative to baseline is defined as the difference
between the counterfactual mean and the baseline mean. Variance relative to baseline is defined as the ratio
of the counterfactual variance to the baseline variance. Employer size is measured in logs in Panel C. Kernel
density estimates of the corresponding counterfactual distributions are provided in Appendix Figure D.1.
Table 7 reports summary measures from the baseline and counterfactual distributions
for three objects of interest: employer pay premiums, employer utility differentials, and em-
ployment size.47 Panel A summarizes the distribution of employer pay premiums, weighted
by employment size. Switching off advertised amenities decreases average pay by 2.3 log
points, while switching off intrinsic amenities increases it by 3.8 log points. These results
complement the correlations in Table6 by quantifying, in terms of pay, the extent to which
47Kernel density estimates of the corresponding distributions are in Appendix Figure D.1.
40

advertised and intrinsic amenities are, respectively, augmenting and compensating differen-
tials on average. Intuitively, when advertised amenities are switched off, some workers are
more likely to enter lower paying jobs as higher paying jobs are now less attractive (augment-
ing differentials are removed). Analogously, when intrinsic amenities are switched off, some
workers are more likely to enter higher paying jobs as lower paying jobs are now less attrac-
tive (compensating differentials are removed). Equalizing advertised and intrinsic amenities
also has opposite effects on the dispersion of employer pay premiums. The variance of pay
increases by 13% when all employers provide the same advertised amenities, and decreases
by 25% when intrinsic amenities are equalized. This result is consistent with the estimated
joint distribution of the different utility components that enter in Equation (3).48
The remaining panels of Table7 confirm the contribution of non-pay amenities to utility
and size dispersions across employers. Panel B shows that the variance of utility goes up in
both scenarios, by 15% and 7%, respectively.49 Panel C shows that non-pay utility differ-
entials are a key factor behind the distribution of employment size across employers: in the
scenario where both components are equalized, the variance of log employer size decreases
by more than half. This result cannot be attributed to a specific amenity component, as
separately equalizing advertised and intrinsic amenities has comparatively smaller effects.
6 Conclusion
In this paper, we study the pay and non-pay content of job ads. Our first set of results
follows from extracting a comprehensive set of pay and non-pay attributes from vacancy
texts. Nearly every job ad mentions at least one such attribute, with an average of seven
attributesperad. Byconsideringabroadrangeofadvertisedattributes, ouranalysisexpands
on prior work focusing on specific job attributes, such as pay information [Batra et al., 2023],
remote work [Hansen et al.,2023], or flexible work arrangements [Adams-Prassl et al.,2023a].
Our second set of results follows from linking these advertised attributes to the employer
posting the ad. We use a revealed-preference approach to derive measures of employer quality
and find that high-quality employers tend to advertise good attributes, such as more generous
pensions, flexible working hours, and permanent and full-time jobs. Ad attributes also
meaningfully predict employer quality, even controlling for detailed observable characteristics
48The kernel density estimates in Appendix Figure D.1 show that many employers offer a combination of
low pay, low advertised amenities, and high intrinsic amenities, which accounts for the dispersion results.
49Appendix Figure D.1, Panel (c), shows the underlying employment distribution in each scenario. In the
“advertised amenities off” scenario, the results are mainly driven by the bottom of the utility distribution
gaining employment from the middle, while the top remains unchanged. In the “intrinsic amenities off”
scenario, employment shifts from the bottom to the middle of the distribution, while the top shrinks markedly.
41

such as industry and occupation. In the survey experiment featuring real-work job ads,
respondents are significantly more likely to state that they prefer job ads posted by higher-
quality employers. Taken together, these results indicate that job ads provide reliable signals
of employer quality for workers assessing their options in the labor market.
Our last set of results follows from introducing these advertised attributes in a standard
monopsony model where workers value jobs at alternative employers differently. We distin-
guish between advertised and intrinsic job attributes, where intrinsic attributes are those
not explicitly mentioned in the ad but valued by workers, and find that the advertised com-
ponent of non-pay worker utility augments pay differentials, while the intrinsic component
represents a compensating differential. Our analysis therefore connects the survey-based em-
pirical literature focusing on specific non-pay attributes [e.g.,Mas and Pallais, 2017, Maestas
et al., 2023] with the structural labor literature that collapses amenities into a scalar index
[e.g., Hall and Mueller, 2018, Morchio and Moser, 2024].
Our approach based on extracting a comprehensive set of job attributes from vacancy
texts points to several directions for future work. First, the pay and non-pay content of job
postings can be expected to differ across labor markets. As one example, health insurance
is largely absent from job ads in Norway, where healthcare is universal, but is likely to be
an important job attribute wherever employer-provided health insurance is common, such
as in France or in the US. Second, there might be a cyclical element to the content of job
ads, with recruiters potentially advertising different attributes when they compete for fewer
job seekers. Third, while prior experimental work has focused on the salary component of
vacancies [Belot et al., 2022], our results show that there is scope to vary a much broader
range of job attributes and further unpack workers’ search behavior.
Finally, our results have implications for the design of policies regulating the information
provided in job ads. Several jurisdictions have passed laws mandating employers to disclose
a salary range in their job openings. Our analysis suggests that there is scope to extend
such transparency laws beyond pay to other job characteristics, such as working arrange-
ments. Similarly, our results can be useful for the design of online job platforms by providing
guidance on the attributes employers should be encouraged to include in their postings.
References
J. M. Abowd, F. Kramarz, and D. N. Margolis. High wage workers and high wage firms.
Econometrica, 67(2):251–333, 1999.
D. Acemoglu, D. Autor, J. Hazell, and P. Restrepo. Artificial intelligence and jobs: evidence
42

from online vacancies.Journal of Labor Economics , 40(S1):S293–S340, 2022.
A. Adams-Prassl, M. Balgova, M. Qian, and T. Waters. Firm concentration & job design:
The case of schedule flexible work arrangements. IFS Working Paper 23/14, Institute for
Fiscal Studies, 2023a.
A. Adams-Prassl, T. Le Barbanchon, and A. Marcato. On-the-job training and labor market
concentration. Technical report, Unpublished working paper, 2023b. Available at SSRN
4477642.
L. Alekseeva, J. Azar, M. Gine, S. Samila, and B. Taska. The demand for ai skills in the
labor market. Labour economics, 71:102002, 2021.
M. E. Andresen, M. Bhuller, and A. Løvgren. Pay Beliefs and the Amenity-Pay Tradeoff.
Unpublished working paper, 2026.
B. W. Arold, E. Ash, W. B. MacLeod, and S. Naidu. Worker Rights in Collective Bargaining.
Working Paper 33605, National Bureau of Economic Research, 2025. Previously circulated
as “Do Words Matter? The Value of Collective Bargaining Agreements”.
E. Atalay, P. Phongthiengtham, S. Sotelo, and D. Tannenbaum. The evolution of work in
the united states. American Economic Journal: Applied Economics , 12(2):1–34, 2020.
R. Audoly and R. Xing. Do employers comply with pay transparency requirements in job
postings? Liberty Street Economics, https://doi. org/10.59576/lse , 20251002, 2025.
J. Azar and I. Marinescu. Monopsony power in the labor market. volume 5 ofHandbook of
Labor Economics, pages 761–827. Elsevier, 2024.
J. Azar, I. Marinescu, and M. Steinbaum. Labor market concentration.Journal of Human
Resources, 57:S167–S199, 2022.
J. Bagger and R. Lentz. An empirical model of wage dispersion with sorting.Review of
Economic Studies, 86(1):153–190, 2019.
K. Bagwell. The economic analysis of advertising.Handbook of Industrial Organization , 3:
1701–1844, 2007.
S. Banfi and B. Villena-Roldan. Do high-wage jobs attract more applicants? Directed search
evidence from the online labor market.Journal of Labor Economics , 37:715–746, 2019.
I. Bassier, A. Dube, and S. Naidu. Monopsony in Movers The Elasticity of Labor Supply to
Firm Wage Policies.Journal of Human Resources , 57:S50–S86, 2022.
43

I. Bassier, A. Manning, and B. Petrongolo. Vacancy Duration and Wages.Review of Eco-
nomics and Statistics , 2025. Forthcoming.
H. Batra, A. Michaud, and S. Mongey. Online job posts contain very little wage information.
Working Paper 31984, National Bureau of Economic Research, 2023.
M. Belot, P. Kircher, and P. Muller. How wage announcements affect job search—a field
experiment. American Economic Journal: Macroeconomics, 14(4):1–67, 2022.
M. Bertrand, D. Karlan, S. Mullainathan, E. Shafir, and J. Zinman. What’s advertising con-
tent worth? evidence from a consumer credit marketing field experiment.The Quarterly
Journal of Economics , 125(1):263–306, 2010.
M. Bhuller, D. Ferraro, A. R. Kostøl, and T. C. Vigtel. The Internet, Search Frictions and
Aggregate Unemployment. Technical report, NBER Working Paper 30911, 2023.
M. Bhuller, M. E. Andresen, and A. Løvgren. Eliciting Preferences for Workplace Charac-
teristics. AEA RCT Registry , AEARCTR-0013426, 2024. URL https://doi.org/10.
1257/rct.13426-1.1.
M. Bhuller, L. Delgado-Prieto, S. Hermo, and L. Lorentzen. Wage-Setting Constraints and
Firm Responses to Demand Shocks.arXiv preprint arXiv:2512.19622 , 2025.
D. M. Blei, A. Y. Ng, and M. I. Jordan. Latent dirichlet allocation.Journal of machine
Learning research, 3(Jan):993–1022, 2003.
S. Bonhomme, T. Lamadon, and E. Manresa. A distributional framework for matched
employer employee data.Econometrica, 87(3):699–739, 2019.
S. Bonhomme, K. Holzheu, T. Lamadon, E. Manresa, M. Mogstad, and B. Setzler. How
much should we trust estimates of firm effects and worker sorting? Journal of Labor
Economics, 41(2):291–322, 2023.
J.C.Braxton andB. Taska. Technologicalchangeandtheconsequences ofjob loss. American
Economic Review, 113(2):279–316, 2023.
C. Brown. Equalizing differences in the labor market.Quarterly Journal of Economics , 94
(1):113–134, 1980.
K. Burdett and D. T. Mortensen. Wage differentials, employer size, and unemployment.
International Economic Review, 39(2):257–273, 1998.
44

A. Bütikofer, R. Karadakic, and A. Willén. Parenthood and the gender gap in commuting.
Journal of Public Economics , 248:105371, 2025.
S. Caldwell, I. Haegele, and J. Heining. Bargaining and Inequality in the Labor Market.
Quarterly Journal of Economics , 141(1):315–371, 10 2025a.
S. Caldwell, I. Haegele, and J. Heining. Why Workers Stay: Pay, Beliefs, and Attachment.
Working paper, 2025b.
D. Card, J. Heining, and P. Kline. Workplace heterogeneity and the rise of west german
wage inequality. Quarterly journal of economics , 128(3):967–1015, 2013.
D. Card, A. R. Cardoso, J. Heining, and P. Kline. Firms and labor market inequality:
Evidence and some theory.Journal of Labor Economics , 36(S1):S13–S70, 2018.
D. Card, F. Colella, and R. Lalive. Gender Preferences in Job Vacancies and Workplace
Gender Diversity. The Review of Economic Studies , 92(4):2437–2471, 08 2024.
C. Carrillo-Tudela, L. Kaas, and B. Lochner. Matching through search channels. Working
paper, CESifo, 2023.
J. Cohen. A Coeﬀicient of Agreement for Nominal Scales. Educational and Psychological
Measurement, 20(1):37–46, 1960.
Z. Contractor and B. Taska. The effect of software adoption on skill demand. Technical
report, Unpublished working paper, 2022.
D. R. Cox and N. Wermuth. A comment on the coeﬀicient of determination for binary
responses. The American Statistician, 46(1):1–4, 1992.
Z. Cullen. Is pay transparency good? Journal of Economic Perspectives , 38(1):153–180,
2024.
N. Datta. Willing to pay for security: a discrete choice experiment to analyse labour supply
preferences. Working Paper, 2019.
D. Deming and L. B. Kahn. Skill requirements across firms and labor markets: Evidence
from job postings for professionals.Journal of Labor Economics, 36(S1):S337–S369, 2018.
D. J. Deming and K. Noray. Earnings dynamics, changing job skills, and stem careers.
Quarterly Journal of Economics , 135(4):1965–2005, 2020.
45

S. Desiere and C. Walter. The Shift Premium: Evidence from a Discrete Choice Experiment.
Technical report, Unpublished working paper, 2023.
M. Drake, F. Payró, N. Thakral, and L. T. Tô. Bayesian adaptive choice experiments.
Technical report, Unpublished working paper, 2022.
M. Drake, N. Thakral, and L. T. To. Wage Differentials and the Price of Workplace Flexi-
bility. Technical report, Unpublished working paper, 2023.
A.Dube, S.Naidu, andA.D.Reich. Poweranddignityinthelow-wagelabormarket: Theory
and evidence from wal-mart workers. Technical report, National Bureau of Economic
Research, 2022.
A. Dube, A. Manning, and S. Naidu. Monopsony and Employer Misoptimization Explain
Why Wages Bunch at Round Numbers.American Economic Review, 115(8):2689–2721,
August 2025.
G. J. Duncan and B. Holmlund. Was adam smith right after all? another test of the theory
of compensating wage differentials.Journal of Labor Economics , 1(4):366–379, 1983.
J. Faberman and G. Menzio. Evidence on the Relationship between Recruiting and the
Starting Wage. Labour Economics, 50:67–79, 2018.
O. Folke and J. Rickne. Sexual Harassment and Gender Inequality in the Labor Market.
Quarterly Journal of Economics , 137(4):2163–2212, 05 2022.
N. D. Gupta, Y. Gallen, K. S. Hedeager, and K. Holzheu. Workplace Amenities and the
Gender Pay Gap.Unpublished working paper, 2025.
A. Gyetvai, P. Arcidiacono, A. Maurel, and E. Jardim. Identification and estimation of
continuous-time job search models with preference shocks. Technical report, Unpublished
working paper, 2022.
R. E. Hall and A. I. Mueller. Wage dispersion and search behavior: The importance of
nonwage job values.Journal of Political Economy , 126(4):1594–1637, 2018.
S. Hansen, P. J. Lambert, N. Bloom, S. J. Davis, and B. Taska. Remote work across jobs,
companies, and space. Technical report, Unpublished working paper, 2023.
J. Hastings, A. Hortaçsu, and C. Syverson. Sales force and competition in financial product
markets: The case of mexico’s social security privatization. Econometrica, 85(6):1723–
1761, 2017.
46

B.Hirsch, E.J.Jahn, A.Manning, andM.Oberfichtner. TheWageElasticityofRecruitment.
Discussion Paper 1883, Centre for Economic Performance, LSE, 2022.
J. J. Horton, R. Johari, and P. Kircher. Sorting through cheap talk: Theory and evidence
from a labor market. Working Paper 11163, CESifo, 2024.
A. Humlum, M. Rasmussen, and E. K. Rose. Firm Premia and Match Effects in Pay vs.
Amenities. Working Paper 33884, National Bureau of Economic Research, May 2025.
H.-s. Hwang, D. T. Mortensen, and W. R. Reed. Hedonic wages and labor market search.
Journal of Labor Economics , 16(4):815–847, 1998.
M. O. Jackson. Social and Economic Networks . Princeton University Press, paperback
edition, 11 2010. ISBN 978-0691148205.
S. Jäger, C. Roth, N. Roussille, and B. Schoefer. Worker beliefs about outside options.
Quarterly Journal of Economics , 139(23):1505–1556, 2024.
G. Jarosch. Searching for job security and the consequences of job loss.Econometrica, 91
(3):903–942, 2023.
G. Jolivet, F. Postel-Vinay, and J.-M. Robin. The empirical content of the job search model:
Labor mobility and wage distributions in europe and the us.Contributions to Economic
Analysis, 275:269–308, 2006.
P. Kline. Labor Market Monopsony: Fundamentals and Frontiers. In C. Dustmann and
T. Lemieux, editors,Handbook of Labor Economics, volume 6 ofHandbook of Labor Eco-
nomics, chapter 8, pages 655–728. Elsevier, 2025.
K. Kroft, Y. Luo, M. Mogstad, and B. Setzler. Imperfect competition and rents in labor and
product markets: The case of the construction industry.American Economic Review, 115
(9):2926–69, September 2025.
M. Lachowska, A. Mas, R. Saggio, and S. A. Woodbury. Work hours mismatch.Economet-
rica, 2025. Forthcoming.
L. Lagos. Union Bargaining Power and the Amenity-Wage Tradeoff. Technical report,
Unpublished working paper, 2024.
T. Lamadon, M. Mogstad, and B. Setzler. Imperfect competition, compensating differentials,
andrentsharingintheuslabormarket. American Economic Review, 112(1):169–212, 2022.
47

T. Le Barbanchon, R. Rathelot, and A. Roulet. Gender differences in job search: Trading
off commute against wage.Quarterly Journal of Economics , 136(1):381–426, 2021.
P. Lewandowski, K. Lipowska, and M. Smoter. Working from Home during a Pandemic -
A Discrete Choice Experiment in Poland. Technical report, Unpublished working paper,
2022.
N. Maestas, K. J. Mullen, D. Powell, T. Von Wachter, and J. B. Wenger. The value of
working conditions in the united states and the implications for the structure of wages.
American Economic Review, 113(7):2007–2047, 2023.
I. Marinescu and R. Wolthoff. Opening the black box of the matching function: The power
of words. Journal of Labor Economics , 38(2):535–568, 2020.
A. Mas. Non-wage amenities. In C. Dustmann and T. Lemieux, editors,Handbook of Labor
Economics, volume 6, pages 373–446. Elsevier, 2025.
A. Mas and A. Pallais. Valuing alternative work arrangements.American Economic Review,
107(12):3722–3759, 2017.
D. McFadden. Conditional logit analysis of qualitative choice behavior. In P. Zarembka,
editor, Frontiers in Econometrics, pages 105–139. New York [u.a.] : Academic Press, 1974.
T. Mikolov, K. Chen, G. Corrado, and J. Dean. Eﬀicient estimation of word representations
in vector space. 2013. doi: 10.48550/ARXIV.1301.3781.
I. Morchio and C. Moser. The gender pay gap: Micro sources and macro consequences.
Working Paper 32408, National Bureau of Economic Research, 2024.
A. I. Mueller, D. Osterwalder, J. Zweimuller, and A. Kettemann. Vacancy durations and
entry wages: Evidence from linked vacancy–employer–employee data.Review of Economic
Studies, 91(3):1808–1841, 2024.
M. Nagler, J. Rincke, and E. Winkler. How Much Do Workers Actually Value Working from
Home? Technical report, Unpublished working paper, 2022.
D. Revelt and K. Train. Mixed Logit with Repeated Choices: Households’ Choices of Ap-
pliance Eﬀiciency Level.Review of Economics and Statistics , 80(4):647–657, 1998.
D. Revelt and K. Train. Customer-Specific Taste Parameters and Mixed Logit: House-
holds’ Choice of Electricity Supplier. Technical report, University of California, Berkeley,
Department of Economics, 1999.
48

S. Rosen. The theory of equalizing differences. Handbook of labor economics , 1:641–692,
1986.
J. Sockin. Show me the amenity: Are higher-paying firms better all around? Working Paper
9842, CESifo, 2022.
I. Sorkin. Ranking firms using revealed preference.Quarterly Journal of Economics , 133(3):
1331–1393, 2018.
C. Taber and R. Vejlin. Estimation of a roy/search/compensating differential model of the
labor market. Econometrica, 88(3):1031–1069, 2020.
B. Van Landeghem, T. Dohmen, A. R. Hole, and A. Künn-Nelen. The value of commuting
time, flexibility, and job security: Evidence from current and recent jobseekers in flanders.
Labour Economics, 91:102631, 2024. ISSN 0927-5371.
M. Wiswall and B. Zafar. Preference for the workplace, investment in human capital, and
gender. Quarterly Journal of Economics , 133(1):457–507, 2018.
49

Appendix
A Additional Tables and Figures
Table A.1: Overview of Sample Composition.
Main Analysis Additional Analysis
All
Observations
Text
Analysis
Sample
Employer
Quality
Sample
Static
Monopsony
Sample
Linked
Ad-Hire
Sample
Survey
Experiment
Sample
(1) (2) (3) (4) (5) (6)
Worker Characteristics:
Age 42.0 41.8 39.9 42.3 42.2 42.2
Immigrant 16.4% 16.3% 17.4% 15.8% 15.4% 18.9%
Women 46.3% 47.9% 50.5% 50.5% 52.3% 43.8%
College 49.7% 51.2% 56.0% 60.8% 55.4% 66.8%
Hourly Wage $27.57 $27.77 $28.55 $30.46 $28.00 $31.32
Number of Workers 3,000,154 2,792,164 2,210,151 1,688,064 2,036,676 96,529
Number of Worker-Years 12,220,469 10,985,594 8,253,567 5,902,421 6,999,923 214,123
Establishment Characteristics:
Size 14.9 26.4 36.8 119.4 39.1 137,9
Public Sector 13.4% 22.5% 27.1% 54.5% 29.2% 15.5%
Industry Composition
Agriculture, Forestry and Fishing 2.9% 1.6% 1.2% 0.8% 0.8% 0.0%
Mining and Quarrying 0.4% 0.4% 0.5% 1.5% 0.3% 0.0%
Manufacturing 4.6% 5.2% 4.9% 5.9% 5.2% 6.7%
Energy Supply 0.4% 0.5% 0.4% 0.6% 0.5% 1.2%
Water Supply 0.5% 0.7% 0.7% 0.6% 0.6% 0.4%
Construction 12.9% 8.6% 7.8% 4.7% 6.5% 5.0%
Wholesale and Retail Trade 19.4% 23.5% 22.1% 5.8% 26.3% 13.2%
Transportation and Storage 4.6% 3.9% 4.1% 3.6% 3.0% 4.3%
Accommodation and Food Service 5.2% 6.5% 6.5% 3.4% 4.9% 1.3%
Information and Communication 4.3% 3.4% 3.8% 5.5% 2.5% 7.0%
Financial and Insurance 1.1% 1.1% 1.2% 1.9% 1.2% 3.5%
Real Estate 4.1% 1.7% 1.3% 0.3% 1.2% 1.6%
Professional, Scientific and Technical 10.2% 6.6% 6.3% 5.7% 5.1% 14.1%
Administrative and Support Service 4.5% 4.6% 3.4% 3.0% 3.0% 14.2%
Public Administration and Defense 2.0% 3.4% 3.3% 7.6% 3.9% 6.3%
Education 3.3% 4.7% 6.2% 13.4% 7.0% 3.3%
Health and Social Work 12.3% 17.3% 21.6% 33.4% 22.7% 14.5%
Arts, Entertainment and Recreation 2.7% 2.5% 2.3% 1.3% 1.9% 0.7%
Other Service Activities 4.5% 3.7% 2.7% 1.1% 3.3% 2.6%
Households as Employers 0.1% 0.0% 0.0% 0.0% 0.0% 0.0%
Number of Establishments 264,084 117,896 70,046 12,973 47,877 416
Notes: This table documents the compositions of workers and employers between 2021 and 2024 across the
different samples we use, as listed in Table 1. “Worker Characteristics” (“Establishment Characteristics”)
shows averages over worker-years (establishment-years), meaning that workers (employers) that are present
in all years are implicitly weighted more than workers (employers) that are present in fewer years. Column
(1) provides sample averages for the initial sample prior to the various sample selection steps, while the
remaining columns provides sample averages for the other analysis samples we use, cf. Table 1. Industry
composition is based on the Classification of Economic Activities in the European Community (NACE).
[Appendix-1]

Table A.2: Characteristics of Workers Linked to Ads and Survey Respondents.
All Observations Linked to Ads Survey Respondents
(1) (2) (3)
Age 42.1 34.3 21.8
Immigrant 16.4% 17.7% 10.2%
Women 46.3% 59.3% 69.6%
College 49.7% 55.1% 46.7%
Hourly Wage $27.57 $23.36 $18.54
Observations 3,000,154 110,932 1,040
Notes: This table shows the average characteristics of (i) all workers in our initial sample, (ii) hired workers
that were linked to a job ad in the linked ad-hire sample used in Section 4.2, and (iii) survey respondents in
the survey experiment sample used in Section 4.3, respectively. In Column (1), we provide average worker
characteristics for the initial sample prior to the various sample selection steps described in Table 1, and
the numbers reported here are identical to the worker-year averages reported in the first panel of Appendix
Table A.1, Column (1). In Column (2), we report average worker characteristics recorded in administrative
data records for the hired workers linked to job ads in the linked ad-hire sample, corresponding to Appendix
Table A.1, Column (4). In Column (3), we report average self-reported background characteristics reported
by respondents participating in the survey experiment, corresponding to Appendix Table A.1, Column (5).
Table A.3: Overview of Sample Selection: 2015-2024.
Workers in Included Establishments
Job Ads Establishments Workers Worker-Years
(1) (2) (3) (4)
All Observations 2,151,994 (100%) 359,789 (100%) 3,479,076 (100%) 29,789,720 (100%)
Main Analysis
Text Analysis Sample 1,998,745 (92.9%) 196,231 (54.5%) 3,383,123 (97.2%) 28,328,064 (95.1%)
Employer Quality Sample 1,660,028 (77.1%) 162,346 (45.1%) 2,956,702 (85.0%) 23,470,708 (78.8%)
Notes: This table documents the sample sizes for different sample restrictions imposed for the 2015-2024
period. The first row shows the total number of observations in our data on job ads (Column 1) and
matched employer-employee data (Columns 2-4), prior to the various sample selection steps. The “Text
Analysis Sample” refers to the set of job ads with non-missing vacancy text and at least one section written
in Norwegian. The “Employer Quality Sample” refers to the sample we retain by restricting the sample
to workers aged 20 to 60 (inclusive) and the strongly connected set of employers used in the estimation of
employer values, while removing establishments registered as recruitment or temporary employment agencies.
[Appendix-2]

Table A.4: Validation of Detected Pay and Non-Pay Job Attributes.
All Ads Job Ads in the Validation Sample
Text
Analysis
Text
Analysis
Manual
Recognition
Success
Rate
Precision
Rate
Sensitivity
Rate
(1) (2) (3) (4) (5) (6)
Compensation Scheme
–– Competitive Pay 15.8 17.5 19.2 94.2 88.6 80.5
–– Collective Agreement Pay 24.3 30.8 33.8 87.0 83.7 76.3
–– Incentive Pay Scheme 2.7 2.0 1.5 98.5 50.0 66.7
–– Hiring Bonus 0.2 0.0 0.0 100.0 – –
–– Good Overtime Pay 0.4 0.2 0.8 99.5 100.0 33.3
–– Any Other Mention of Pay 14.5 14.5 8.8 86.2 32.8 54.3
Financial Attributes
–– Pension Scheme 30.4 34.8 32.8 98.0 94.2 100.0
–– Insurance Scheme 19.1 23.8 21.5 96.2 87.4 96.5
–– Mortgage Possibility 1.4 2.0 3.8 98.2 100.0 53.3
Career Opportunities
–– Good Career Paths 12.6 16.8 6.2 85.0 23.9 64.0
–– On-the-Job Training 41.6 46.8 39.2 78.0 68.4 81.5
Hours of Work
–– Full-time Contract 59.3 55.8 53.2 95.0 93.3 97.7
–– Part-time Contract 30.9 34.0 28.2 91.2 78.7 94.7
–– Full-time/Part-time Choice 4.1 3.0 3.0 94.0 0.0 0.0
Convenient Hours
–– Possibility to Work Flexible Hours 6.5 6.8 7.5 98.2 92.6 83.3
–– Regular Daytime Work Schedule 14.0 8.8 8.8 97.0 82.9 82.9
–– Exempt from Work Hour Regulations 0.5 1.2 0.2 98.5 0.0 0.0
Inconvenient Hours
–– Shift Work 15.4 15.0 11.8 95.8 75.0 95.7
–– Weekend/Evening/Night Work 18.4 21.8 17.0 94.8 77.0 98.5
–– On-call Employment 3.4 3.8 2.2 98.0 53.3 88.9
–– Overtime Work Required 0.2 0.0 0.2 99.8 – 0.0
Contract Duration
–– Permanent Job 40.6 38.8 40.8 93.0 93.5 89.0
–– Temporary Job 29.6 32.2 29.2 91.0 81.4 89.7
–– Fixed-term Contract 0.4 0.8 0.8 100.0 100.0 100.0
Workplace Attributes
–– Social Environment 41.4 44.0 40.8 80.8 74.4 80.4
–– Good Colleagues 21.7 26.0 28.2 77.2 60.6 55.8
–– Possibility for Remote Work 0.4 0.5 0.5 100.0 100.0 100.0
–– Shared Oﬀice Space 0.2 0.0 0.0 100.0 – –
–– Inclusive Work-life Scheme 7.1 7.2 6.0 98.2 79.3 95.8
Task-Related Attributes
–– Interesting Tasks 34.5 38.2 22.2 82.5 56.2 96.6
–– Challenging Tasks 28.6 32.0 19.0 85.0 56.2 94.7
–– Variation in Tasks 10.9 10.2 15.8 87.5 65.9 42.9
–– Responsibility in Job 1.6 1.8 10.2 90.5 71.4 12.2
–– Independence in Performing Tasks 2.5 2.8 5.0 95.8 63.6 35.0
–– Involves Leadership Responsibility 11.8 13.5 9.0 87.0 35.2 52.8
–– Work Involves Travelling 8.2 10.2 3.5 93.2 34.1 100.0
Minor Perks
–– Beautiful Location 0.8 2.2 4.8 96.5 77.8 36.8
–– Central Location 33.0 37.5 5.2 65.8 11.3 81.0
–– Company Gym or Sports Team 3.7 5.0 6.5 95.5 70.0 53.8
–– Parking Space On Premises 0.5 0.5 0.2 99.8 50.0 100.0
–– Company Vehicle 1.2 1.5 1.0 99.5 66.7 100.0
–– Any Welfare Scheme 4.2 4.8 2.5 97.2 47.4 90.0
–– Company Cabin 1.9 2.0 3.2 98.8 100.0 61.5
–– Occupational Health Service 1.4 1.2 1.2 100.0 100.0 100.0
–– Company Canteen 0.3 0.8 0.8 99.0 33.3 33.3
–– Flexible/Extended Holidays 0.5 0.0 0.0 100.0 – –
Number of Job Ads 860,467 400 400 400 – –
Notes: See details in the notes to Table 3. [Appendix-3]

Table A.5: Association Between Employer Quality and Vacancy Duration.
Outcome: Log Vacancy Duration
(1) (2)
Pay Premium -0.150∗∗∗ -0.164∗∗
(0.036) (0.055)
Overall Sorkin Value -0.028 ∗∗∗ -0.040∗∗∗
(0.004) (0.008)
Poaching Index -0.029∗∗∗ -0.033∗∗∗
(0.004) (0.007)
Occupation FE ✓
Industry FE ✓
Location FE ✓
Number of Job Ads 1,587,634 1,587,634
Standard errors in parentheses
∗ p < 0.10, ∗∗ p < 0.05, ∗∗∗ p < 0.01
Notes: This table documents associations between employer quality measures and vacancy duration. Each
column reports point estimates from three separate regressions of alternative revealed-preference employer
quality measures defined in Section 4.1, namely Employer Pay Premium, the Overall Sorkin Value, and the
Poaching Index, on Log Vacancy Duration. Vacancy Duration is the number of days between the dates when
the ad is posted and unlisted, right censored at 90 days to avoid outliers. For this analysis, we drop a small
share of ads with zero or negative durations. Pay Premium is measured in logs, so the estimated coeﬀicient
on this measure can be interpreted as an elasticity, while Overall Sorkin Value and Poaching Index are scaled
by their standard deviation, so the estimated coeﬀicient for each of these represents a standard deviation
increase in employer quality. Estimations are done at the ad level for the period between 2015 and 2024. In
Column (2), we control for occupation and industry using two-digit occupation and two-digit industry fixed
effects and location based on deciles of the number of workers in the municipality of the firm (Oslo as an
own group), using separate categories for missing occupation, industry, and locations.
[Appendix-4]

Figure A.1: Event Study: Hires and Job Postings.
(a) Hires All Occupations
-0.05
0.00
0.05
0.10
Hires
-9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9
Month Relative to Ad Posting Month
(b) Within 1-digit Occupation
-0.05
0.00
0.05
0.10
Hires
-9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9
Month Relative to Ad Posting Month (c) Within 2-digit Occupation
-0.05
0.00
0.05
0.10
Hires
-9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9
Month Relative to Ad Posting Month
(d) Within 3-digit Occupation
-0.05
0.00
0.05
0.10
Hires
-9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9
Month Relative to Ad Posting Month (e) Within 4-digit Occupation
-0.05
0.00
0.05
0.10
Hires
-9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9
Month Relative to Ad Posting Month
Notes: This figure shows the number of hires around the month of job ad posting within establishments
and occupations, constructed using subsets of the text analysis sample as listed in Table 1 from 2021 to
2024. We start by identifying establishment-occupation cells with posted ads and merge in the number of
hired workers in surrounding months. The number of hired workers is constructed by counting workers with
a reported starting date in each month at the establishment and occupation. We estimate an event study
regression controlling for year–month fixed effects to account for seasonality in ad posting and hiring:
hiresjom =
X
k̸=−1
βk1(m − me = k) + γm + εjom,
where hires jom is the number of hires in month m in establishment j and occupation o, k indicates month
relative to the month of ad posting ( me), and γm are year-month fixed effects. The sum of point estimates
to the right of the vertical lines relative to the left of the vertical lines implies an increase of about 0.43 hires
at the establishment level (Panel (a)), and 0.22 hires at the establishment-occupation level (Panel (e)).
[Appendix-5]

Figure A.2: Survey Experiment: Job Choice Scenario with Real Ads.
Notes: This figure shows an example of a choice scenario with job ads that respondents faced in the survey experiment performed by Bhuller et al.
[2024]. This is simplified version of the choice scenarios shown in Andresen et al. [2026], who introduce additional experimental features.
[Appendix-6]

Figure A.3: Sample Vacancy Text: Teacher Substitute.
Substitute in a professional position:
One year of temporary work in a 100% position from 01.08.2016 - 31.07.2017.
The position entails travel activities in the region and the applicant must have
their own car.
We are looking for an employee with:
- Special needs teacher with competence at the Master’s or Bachelor’s level.
- Professional experience from kindergarten/school and relevant skills.
- Good collaboration skills, flexibility, and personal suitability.
The following applies to the position:
- Challenging tasks.
- Good working environment in an interdisciplinary team.
- Appointment and working conditions according to current agreements and
regulations.
- Wages in accordance with the agreement.
- Compulsory membership in KLP (public sector occupational pension
scheme).
[...]
Notes: Translation from Norwegian by the authors.
[Appendix-7]

Figure A.4: Sample Vacancy Text: Civil Engineer.
[...]
We need to increase capacity within water- and environmental engineering, and
are therefore looking for a civil engineer/engineer with experience within water
supply, sewage and urban drainage systems.
The position involves exciting and challenging tasks in an interdisciplinary envi-
ronment.
The work will include planning, engineering, and follow-up of private and munic-
ipal urban drainage-, water-, and sewage systems.
Desired competence:
- Engineer / civil engineer
- Relevant experience
- Good ability to work with colleagues, partners, and clients
- Good knowledge of written and spoken Norwegian
- New graduates with good results may also be relevant
Preferred abilities:
- Ability to work independently as well as in a team
- Solution-oriented and accurate
- Resourceful
- Positive and persistent
We offer:
- An independent position in a solid company in growth and development
- Professionally inspiring with talented colleagues
- A pleasant and orderly workplace with bright and open premises in central
Oslo
- Competitive conditions
[...]
Notes: Translation from Norwegian by the authors.
[Appendix-8]

Figure A.5: The Prevalence of Job Attributes Advertised in Vacancy Texts Across Samples.
Compensation Scheme:
  - Compensation Level
  - Competitive Pay
  - Collective Agreement Pay
  - Incentive Pay Scheme
  - Hiring Bonus
  - Good Overtime Pay
  - Any Other Mention of Pay
Financial Attributes:
  - Pension Scheme
  - Insurance Scheme
  - Mortgage Possibility
Career Opportunities:
  - Good Career Paths
  - On-the-Job Training
Hours of Work:
  - Full-time Contract
  - Part-time Contract
  - Full-time/Part-time Choice
Convenient Hours:
  - Possibility to Work Flexible Hours
  - Regular Daytime Work Schedule
  - Exempt from Work Hour Regulations
Inconvenient Hours:
  - Shift Work
  - Weekend/Evening/Night Work
  - On-call Employment
  - Overtime Work Required
Contract Duration:
  - Permanent Job
  - Temporary Job
  - Fixed-term Contract
Workplace Attributes:
  - Social Environment
  - Good Colleagues
  - Possibility for Remote Work
  - Shared Office Space
  - Inclusive Work-life Scheme
Task-Related Attributes:
  - Interesting Tasks
  - Challenging Tasks
  - Variation in Tasks
  - Responsibility in Job
  - Independence in Performing Tasks
  - Involves Leadership Responsibility
  - Work Involves Travelling
Minor Perks:
  - Beautiful Location
  - Central Location
  - Company Gym or Sports Team
  - Parking Space On Premises
  - Company Vehicle
  - Any Welfare Scheme
  - Company Cabin
  - Occupational Health Service
  - Company Canteen
  - Flexible/Extended Holidays
0 .1 .2 .3 .4 .5 .6 .7 .8 .9 1
Text Analysis Sample
Employer Quality Sample
Static Monopsony Sample
Notes: This figure documents the prevalence of job attributes detected in job ads posted in Norway between
2021 and 2024, separately for the three main analysis samples. The light bars show the share of ads detected
with each distinct job attribute, while dark bars show the share of ads detected with at least one attribute
within ten broad categories. Sample sizes are reported in Table 1.
[Appendix-9]

Figure A.6: The Prevalence of Job Attributes Advertised in Vacancy Texts: 2015-2024.
Compensation Scheme:
  - Compensation Level
  - Competitive Pay
  - Collective Agreement Pay
  - Incentive Pay Scheme
  - Hiring Bonus
  - Good Overtime Pay
  - Any Other Mention of Pay
Financial Attributes:
  - Pension Scheme
  - Insurance Scheme
  - Mortgage Possibility
Career Opportunities:
  - Good Career Paths
  - On-the-Job Training
Hours of Work:
  - Full-time Contract
  - Part-time Contract
  - Full-time/Part-time Choice
Convenient Hours:
  - Possibility to Work Flexible Hours
  - Regular Daytime Work Schedule
  - Exempt from Work Hour Regulations
Inconvenient Hours:
  - Shift Work
  - Weekend/Evening/Night Work
  - On-call Employment
  - Overtime Work Required
Contract Duration:
  - Permanent Job
  - Temporary Job
  - Fixed-term Contract
Workplace Attributes:
  - Social Environment
  - Good Colleagues
  - Possibility for Remote Work
  - Shared Office Space
  - Inclusive Work-life Scheme
Task-Related Attributes:
  - Interesting Tasks
  - Challenging Tasks
  - Variation in Tasks
  - Responsibility in Job
  - Independence in Performing Tasks
  - Involves Leadership Responsibility
  - Work Involves Travelling
Minor Perks:
  - Beautiful Location
  - Central Location
  - Company Gym or Sports Team
  - Parking Space On Premises
  - Company Vehicle
  - Any Welfare Scheme
  - Company Cabin
  - Occupational Health Service
  - Company Canteen
  - Flexible/Extended Holidays
0 .1 .2 .3 .4 .5 .6 .7 .8 .9 1
Notes: This figure documents the prevalence of job attributes detected in job ads posted in Norway between
2015 and 2024 [N=1,998,745]. The light blue bars show the share of ads detected having each of the distinct
job attributes. The dark blue bars show the share of ads detected with at least one attribute within ten
broad categories. Figure 2 shows the corresponding results for the 2021-2024 period.
[Appendix-10]

Figure A.7: Explained Variation in Publicly Advertised Job Attributes: Shapley Values.
0 .2 .4 .6 .8 1
Pseudo R
2
  - Number of Attributes
  - Companyname Disclosed
  - Posted Online
  - Number of Words
Other Ad Characteristics:
  - Flexible/Extended Holidays
  - Company Canteen
  - Occupational Health Service
  - Company Cabin
  - Any Welfare Scheme
  - Company Vehicle
  - Parking Space On Premises
  - Company Gym or Sports Team
  - Central Location
  - Beautiful Location
Minor Perks:
  - Work Involves Travelling
  - Involves Leadership Responsibility
  - Independence in Performing Tasks
  - Responsibility in Job
  - Variation in Tasks
  - Challenging Tasks
  - Interesting Tasks
Task-Related Attributes:
  - Inclusive Work-life Scheme
  - Shared Office Space
  - Possibility for Remote Work
  - Good Colleagues
  - Social Environment
Workplace Attributes:
  - Fixed-term Contract
  - Temporary Job
  - Permanent Job
Contract Duration:
  - Overtime Work Required
  - On-call Employment
  - Weekend/Evening/Night Work
  - Shift Work
Inconvenient Hours:
  - Exempt from Work Hour Regulations
  - Regular Daytime Work Schedule
  - Possibility to Work Flexible Hours
Convenient Hours:
  - Full-time/Part-time Choice
  - Part-time Contract
  - Full-time Contract
Hours of Work:
  - On-the-Job Training
  - Good Career Paths
Career Opportunities:
  - Mortgage Possibility
  - Insurance Scheme
  - Pension Scheme
Financial Attributes:
  - Any Other Mention of Pay
  - Good Overtime Pay
  - Hiring Bonus
  - Incentive Pay Scheme
  - Collective Agreement Pay
  - Competitive Pay
  - Compensation Level
Compensation Scheme:
Industry FE Location FE
Occupation FE Establishment FE
Notes: This figure shows the Shapley Value Decomposition of the pseudo R2 [McFadden, 1974] from logistic
regressions of binary job attributes detected in job ads posted in Norway between 2021 and 2024 [N=748,870]
on fixed effects denoting unique combinations of 2-digit industries (88 groups), location indicators (10 groups),
2-digit occupations (44 groups), and 57,656 establishments. Every regression considered by the Shapley Value
Decomposition consists of a single categorical variable indicating unique combinations of included industries,
location categories, occupations, and establishments. The fully interacted regression with all four categories
controls for 133,964 unique combinations. The regression excludes 194,851 ads with a unique combination of
establishment, occupation, location, and industry indicators, since these observations are perfectly predicted
by the last set of regressions by construction. Location indicators group 422 municipalities into 10 groups
based on the number of workers, so municipalities assigned to the same group have a similar number of
workers, with a specific indicator for job postings in Oslo. Figure 3 shows the corresponding results for
sequentially adding industry, location, occupation, and establishment FE.
[Appendix-11]

Figure A.8: Explained Variation in Publicly Advertised Job Attributes: 2015-2024.
0 .2 .4 .6 .8 1
Pseudo R
2
  - Number of Attributes
  - Companyname Disclosed
  - Posted Online
  - Number of Words
Other Ad Characteristics:
  - Flexible/Extended Holidays
  - Company Canteen
  - Occupational Health Service
  - Company Cabin
  - Any Welfare Scheme
  - Company Vehicle
  - Parking Space On Premises
  - Company Gym or Sports Team
  - Central Location
  - Beautiful Location
Minor Perks:
  - Work Involves Travelling
  - Involves Leadership Responsibility
  - Independence in Performing Tasks
  - Responsibility in Job
  - Variation in Tasks
  - Challenging Tasks
  - Interesting Tasks
Task-Related Attributes:
  - Inclusive Work-life Scheme
  - Shared Office Space
  - Possibility for Remote Work
  - Good Colleagues
  - Social Environment
Workplace Attributes:
  - Fixed-term Contract
  - Temporary Job
  - Permanent Job
Contract Duration:
  - Overtime Work Required
  - On-call Employment
  - Weekend/Evening/Night Work
  - Shift Work
Inconvenient Hours:
  - Exempt from Work Hour Regulations
  - Regular Daytime Work Schedule
  - Possibility to Work Flexible Hours
Convenient Hours:
  - Full-time/Part-time Choice
  - Part-time Contract
  - Full-time Contract
Hours of Work:
  - On-the-Job Training
  - Good Career Paths
Career Opportunities:
  - Mortgage Possibility
  - Insurance Scheme
  - Pension Scheme
Financial Attributes:
  - Any Other Mention of Pay
  - Good Overtime Pay
  - Hiring Bonus
  - Incentive Pay Scheme
  - Collective Agreement Pay
  - Competitive Pay
  - Compensation Level
Compensation Scheme:
Industry FE + Location FE
+ Occupation FE + Establishment FE
Notes: This figure shows pseudo R2 [McFadden, 1974] from separate logistic regressions of binary job at-
tributes detected in job ads posted in Norway between 2015 and 2024 [N=1,677,211], on fixed effects denoting
unique combinations of 2-digit industries (88 groups), location indicators (10 groups), 2-digit occupations
(44 groups), and 88,887 establishments. We start by including industry fixed effects, continue by including
industry×location fixed effects, and so on. The regression excludes 321,534 ads with a unique combination
of establishment, occupation, location, and industry indicators, as these observations are precisely predicted
by the last set of regressions by construction. The last set of regressions controls for 260,241 unique combi-
nations. Location indicators group 422 municipalities into ten groups based on the number of workers, such
that municipalities assigned to the same group have a similar number of workers, with a specific indicator
for job postings in Oslo. Figure 3 shows the corresponding results for the 2021-2024 period.
[Appendix-12]

Figure A.9: Job Attributes and Employer Quality: Controlling for Pay Premiums.
(a) Overall Sorkin Value
Full-time Contract ·················
Pension Scheme ·····················
Insurance Scheme ···················
Challenging Tasks ··················
Good Colleagues ····················
Competitive Pay ····················
Possibility to Work Flexible Hours ·
Interesting Tasks ··················
Central Location ···················
Permanent Job ······················
Work Involves Travelling ···········
Company Gym or Sports Team ·········
Involves Leadership Responsibility ·
Possibility for Remote Work ········
Good Career Paths ··················
Compensation Level ·················
Company Cabin ······················
Social Environment ·················
On-the-Job Training ················
Independence in Performing Tasks ···
Any Welfare Scheme ·················
Mortgage Possibility ···············
Good Overtime Pay ··················
Flexible/Extended Holidays ·········
Incentive Pay Scheme ···············
Occupational Health Service ········
Company Canteen ····················
Responsibility in Job ··············
Shared Office Space ················
Fixed-term Contract ················
Exempt from Work Hour Regulations ··
Parking Space On Premises ··········
Regular Daytime Work Schedule ······
Overtime Work Required ·············
Full-time/Part-time Choice ·········
Hiring Bonus ·······················
Beautiful Location ·················
Inclusive Work-life Scheme ·········
Variation in Tasks ·················
Company Vehicle ····················
Any Other Mention of Pay ···········
Collective Agreement Pay ···········
On-call Employment ·················
Shift Work ·························
Temporary Job ······················
Part-time Contract ·················
Weekend/Evening/Night Work ·········
-.15 -.1 -.05 0 .05 .1
Without Controls
Pay Premium Control (b) Poaching Index
Pension Scheme ·····················
Insurance Scheme ···················
Full-time Contract ·················
Challenging Tasks ··················
Good Colleagues ····················
Central Location ···················
Interesting Tasks ··················
Possibility to Work Flexible Hours ·
Collective Agreement Pay ···········
Social Environment ·················
Work Involves Travelling ···········
Company Gym or Sports Team ·········
Permanent Job ······················
Competitive Pay ····················
On-the-Job Training ················
Involves Leadership Responsibility ·
Compensation Level ·················
Possibility for Remote Work ········
Company Cabin ······················
Inclusive Work-life Scheme ·········
Independence in Performing Tasks ···
Occupational Health Service ········
Mortgage Possibility ···············
Flexible/Extended Holidays ·········
Parking Space On Premises ··········
Any Other Mention of Pay ···········
Variation in Tasks ·················
Good Overtime Pay ··················
Company Canteen ····················
Any Welfare Scheme ·················
Fixed-term Contract ················
Exempt from Work Hour Regulations ··
Hiring Bonus ·······················
Shared Office Space ················
Regular Daytime Work Schedule ······
Overtime Work Required ·············
Beautiful Location ·················
Responsibility in Job ··············
Full-time/Part-time Choice ·········
Company Vehicle ····················
Incentive Pay Scheme ···············
Shift Work ·························
Good Career Paths ··················
On-call Employment ·················
Temporary Job ······················
Part-time Contract ·················
Weekend/Evening/Night Work ·········
-.15 -.1 -.05 0 .05 .1
Without Controls
Pay Premium Control
Notes: This figure shows parameter estimates and 90% confidence intervals from separate regressions of the
share of each ad attribute on Overall Sorkin Value and Poaching Index while controlling for Pay Premium,
capturing the change in the fraction of ads with each job attribute associated with a residualized standard
deviation increase in employer value. Estimations are done at the employer-cluster level for the period from
2021 to 2024, and are weighted by the number of worker-years.
[Appendix-13]

Figure A.10: Publicly Advertised Job Attributes By Employer Quality Measures: 2015-2024.
(a) Pay Premium
Challenging Tasks ··················
Pension Scheme ·····················
Central Location ···················
Interesting Tasks ··················
Insurance Scheme ···················
Shift Work ·························
Good Colleagues ····················
Social Environment ·················
On-the-Job Training ················
Work Involves Travelling ···········
Competitive Pay ····················
Collective Agreement Pay ···········
Full-time Contract ·················
Permanent Job ······················
Variation in Tasks ·················
Company Gym or Sports Team ·········
Weekend/Evening/Night Work ·········
Any Welfare Scheme ·················
Possibility to Work Flexible Hours ·
Company Cabin ······················
Compensation Level ·················
Inclusive Work-life Scheme ·········
Occupational Health Service ········
Good Career Paths ··················
Independence in Performing Tasks ···
Parking Space On Premises ··········
Involves Leadership Responsibility ·
Possibility for Remote Work ········
Mortgage Possibility ···············
Flexible/Extended Holidays ·········
Hiring Bonus ·······················
Good Overtime Pay ··················
Company Canteen ····················
Shared Office Space ················
Responsibility in Job ··············
Beautiful Location ·················
Overtime Work Required ·············
Incentive Pay Scheme ···············
Exempt from Work Hour Regulations ··
Fixed-term Contract ················
Any Other Mention of Pay ···········
Company Vehicle ····················
On-call Employment ·················
Full-time/Part-time Choice ·········
Temporary Job ······················
Regular Daytime Work Schedule ······
Part-time Contract ·················
-.05 0 .05 .1 (b) Overall Sorkin Value
Pension Scheme ·····················
Insurance Scheme ···················
Interesting Tasks ··················
Challenging Tasks ··················
Good Colleagues ····················
Full-time Contract ·················
Central Location ···················
Possibility to Work Flexible Hours ·
Competitive Pay ····················
Work Involves Travelling ···········
Involves Leadership Responsibility ·
Social Environment ·················
Company Gym or Sports Team ·········
Compensation Level ·················
On-the-Job Training ················
Permanent Job ······················
Collective Agreement Pay ···········
Company Cabin ······················
Possibility for Remote Work ········
Good Career Paths ··················
Inclusive Work-life Scheme ·········
Occupational Health Service ········
Any Welfare Scheme ·················
Mortgage Possibility ···············
Any Other Mention of Pay ···········
Good Overtime Pay ··················
Independence in Performing Tasks ···
Flexible/Extended Holidays ·········
Responsibility in Job ··············
Company Canteen ····················
Parking Space On Premises ··········
Shared Office Space ················
Variation in Tasks ·················
Fixed-term Contract ················
Overtime Work Required ·············
Exempt from Work Hour Regulations ··
Hiring Bonus ·······················
Beautiful Location ·················
Company Vehicle ····················
Incentive Pay Scheme ···············
Full-time/Part-time Choice ·········
Regular Daytime Work Schedule ······
On-call Employment ·················
Temporary Job ······················
Shift Work ·························
Part-time Contract ·················
Weekend/Evening/Night Work ·········
-.1 -.05 0 .05 .1 (c) Poaching Index
Pension Scheme ·····················
Insurance Scheme ···················
Challenging Tasks ··················
Good Colleagues ····················
Interesting Tasks ··················
Central Location ···················
Full-time Contract ·················
Social Environment ·················
Collective Agreement Pay ···········
Possibility to Work Flexible Hours ·
On-the-Job Training ················
Work Involves Travelling ···········
Competitive Pay ····················
Involves Leadership Responsibility ·
Compensation Level ·················
Permanent Job ······················
Company Gym or Sports Team ·········
Inclusive Work-life Scheme ·········
Company Cabin ······················
Any Other Mention of Pay ···········
Possibility for Remote Work ········
Variation in Tasks ·················
Occupational Health Service ········
Mortgage Possibility ···············
Good Overtime Pay ··················
Independence in Performing Tasks ···
Flexible/Extended Holidays ·········
Parking Space On Premises ··········
Company Canteen ····················
Responsibility in Job ··············
Any Welfare Scheme ·················
Hiring Bonus ·······················
Shared Office Space ················
Beautiful Location ·················
Fixed-term Contract ················
Exempt from Work Hour Regulations ··
Overtime Work Required ·············
Company Vehicle ····················
Good Career Paths ··················
Incentive Pay Scheme ···············
Shift Work ·························
Temporary Job ······················
Full-time/Part-time Choice ·········
On-call Employment ·················
Regular Daytime Work Schedule ······
Weekend/Evening/Night Work ·········
Part-time Contract ·················
-.1 -.05 0 .05 .1 .15
Notes: This figure shows parameter estimates and 90% confidence intervals from separate regressions of the share of each ad attribute on Employer
Pay Premium, Employer Overall Sorkin Value, and Employer Poaching Index, capturing the change in the fraction of ads with each job attribute
associated with a standard deviation increase in employer value. Estimations are done at the employer-cluster level for the period from 2015 to 2024,
and are weighted by the number of worker-years.
[Appendix-14]

Figure A.11: Publicly Advertised Job Attributes By Employer Quality Measures: Smaller Clusters.
(a) Pay Premium
Shift Work ·························
Challenging Tasks ··················
Pension Scheme ·····················
Weekend/Evening/Night Work ·········
Interesting Tasks ··················
Insurance Scheme ···················
On-the-Job Training ················
Social Environment ·················
Good Colleagues ····················
Central Location ···················
Collective Agreement Pay ···········
Permanent Job ······················
Company Gym or Sports Team ·········
Variation in Tasks ·················
Any Welfare Scheme ·················
Full-time Contract ·················
Company Cabin ······················
Competitive Pay ····················
Work Involves Travelling ···········
Compensation Level ·················
Inclusive Work-life Scheme ·········
Parking Space On Premises ··········
Possibility to Work Flexible Hours ·
Occupational Health Service ········
Incentive Pay Scheme ···············
Hiring Bonus ·······················
Independence in Performing Tasks ···
Possibility for Remote Work ········
Mortgage Possibility ···············
Flexible/Extended Holidays ·········
Good Career Paths ··················
Beautiful Location ·················
Good Overtime Pay ··················
Company Canteen ····················
Regular Daytime Work Schedule ······
Shared Office Space ················
Overtime Work Required ·············
On-call Employment ·················
Responsibility in Job ··············
Full-time/Part-time Choice ·········
Exempt from Work Hour Regulations ··
Fixed-term Contract ················
Involves Leadership Responsibility ·
Any Other Mention of Pay ···········
Company Vehicle ····················
Part-time Contract ·················
Temporary Job ······················
-.05 0 .05 .1 (b) Overall Sorkin Value
Full-time Contract ·················
Pension Scheme ·····················
Insurance Scheme ···················
Challenging Tasks ··················
Competitive Pay ····················
Good Colleagues ····················
Possibility to Work Flexible Hours ·
Interesting Tasks ··················
Central Location ···················
Permanent Job ······················
Work Involves Travelling ···········
Company Gym or Sports Team ·········
Involves Leadership Responsibility ·
Good Career Paths ··················
Possibility for Remote Work ········
Compensation Level ·················
Company Cabin ······················
On-the-Job Training ················
Incentive Pay Scheme ···············
Mortgage Possibility ···············
Independence in Performing Tasks ···
Occupational Health Service ········
Social Environment ·················
Flexible/Extended Holidays ·········
Any Welfare Scheme ·················
Good Overtime Pay ··················
Company Canteen ····················
Parking Space On Premises ··········
Responsibility in Job ··············
Shared Office Space ················
Fixed-term Contract ················
Regular Daytime Work Schedule ······
Exempt from Work Hour Regulations ··
Overtime Work Required ·············
Full-time/Part-time Choice ·········
Hiring Bonus ·······················
Beautiful Location ·················
Inclusive Work-life Scheme ·········
Company Vehicle ····················
Any Other Mention of Pay ···········
Variation in Tasks ·················
Collective Agreement Pay ···········
On-call Employment ·················
Temporary Job ······················
Shift Work ·························
Part-time Contract ·················
Weekend/Evening/Night Work ·········
-.1 -.05 0 .05 .1 (c) Poaching Index
Pension Scheme ·····················
Insurance Scheme ···················
Full-time Contract ·················
Challenging Tasks ··················
Good Colleagues ····················
Central Location ···················
Interesting Tasks ··················
Possibility to Work Flexible Hours ·
Collective Agreement Pay ···········
Social Environment ·················
Work Involves Travelling ···········
Company Gym or Sports Team ·········
Permanent Job ······················
Competitive Pay ····················
On-the-Job Training ················
Involves Leadership Responsibility ·
Compensation Level ·················
Possibility for Remote Work ········
Company Cabin ······················
Inclusive Work-life Scheme ·········
Independence in Performing Tasks ···
Occupational Health Service ········
Mortgage Possibility ···············
Flexible/Extended Holidays ·········
Parking Space On Premises ··········
Variation in Tasks ·················
Any Other Mention of Pay ···········
Good Overtime Pay ··················
Company Canteen ····················
Any Welfare Scheme ·················
Fixed-term Contract ················
Exempt from Work Hour Regulations ··
Hiring Bonus ·······················
Shared Office Space ················
Regular Daytime Work Schedule ······
Overtime Work Required ·············
Beautiful Location ·················
Responsibility in Job ··············
Full-time/Part-time Choice ·········
Company Vehicle ····················
Incentive Pay Scheme ···············
Good Career Paths ··················
Shift Work ·························
On-call Employment ·················
Temporary Job ······················
Part-time Contract ·················
Weekend/Evening/Night Work ·········
-.1 -.05 0 .05 .1 .15
Notes: This figure shows parameter estimates and 90% confidence intervals from separate regressions of the share of each ad attribute on Employer
Pay Premium, Employer Overall Sorkin Value, and Employer Poaching Index, capturing the change in the fraction of ads with each job attribute
associated with a standard deviation increase in employer value. Estimations are done at the employer-cluster level for the period from 2021 to 2024,
and are weighted by the number of worker-years. On average, each cluster has 25 establishments, i.e., G =round(J/25) = 2 , 843 unique employer
clusters, while Figure 4 shows the corresponding results in our baseline with G =round(J/50) = 1 , 422 unique employer clusters.
[Appendix-15]

Figure A.12: Publicly Advertised Job Attributes By Employer Quality Measures: Larger Clusters.
(a) Pay Premium
Challenging Tasks ··················
Shift Work ·························
Pension Scheme ·····················
Insurance Scheme ···················
Interesting Tasks ··················
Social Environment ·················
Weekend/Evening/Night Work ·········
Good Colleagues ····················
On-the-Job Training ················
Central Location ···················
Collective Agreement Pay ···········
Variation in Tasks ·················
Permanent Job ······················
Full-time Contract ·················
Company Gym or Sports Team ·········
Any Welfare Scheme ·················
Possibility to Work Flexible Hours ·
Competitive Pay ····················
Work Involves Travelling ···········
Company Cabin ······················
Inclusive Work-life Scheme ·········
Compensation Level ·················
Parking Space On Premises ··········
Independence in Performing Tasks ···
Occupational Health Service ········
Hiring Bonus ·······················
Possibility for Remote Work ········
Flexible/Extended Holidays ·········
Mortgage Possibility ···············
Beautiful Location ·················
Good Overtime Pay ··················
Shared Office Space ················
Company Canteen ····················
Incentive Pay Scheme ···············
Regular Daytime Work Schedule ······
Overtime Work Required ·············
Responsibility in Job ··············
Full-time/Part-time Choice ·········
Exempt from Work Hour Regulations ··
Fixed-term Contract ················
On-call Employment ·················
Good Career Paths ··················
Any Other Mention of Pay ···········
Involves Leadership Responsibility ·
Company Vehicle ····················
Part-time Contract ·················
Temporary Job ······················
-.05 0 .05 .1 (b) Overall Sorkin Value
Full-time Contract ·················
Pension Scheme ·····················
Insurance Scheme ···················
Competitive Pay ····················
Interesting Tasks ··················
Good Colleagues ····················
Challenging Tasks ··················
Possibility to Work Flexible Hours ·
Central Location ···················
Permanent Job ······················
Work Involves Travelling ···········
Company Gym or Sports Team ·········
Involves Leadership Responsibility ·
Possibility for Remote Work ········
Compensation Level ·················
Company Cabin ······················
Social Environment ·················
Good Career Paths ··················
Independence in Performing Tasks ···
Mortgage Possibility ···············
Any Welfare Scheme ·················
Occupational Health Service ········
Flexible/Extended Holidays ·········
Good Overtime Pay ··················
Company Canteen ····················
On-the-Job Training ················
Shared Office Space ················
Parking Space On Premises ··········
Fixed-term Contract ················
Responsibility in Job ··············
Regular Daytime Work Schedule ······
Exempt from Work Hour Regulations ··
Overtime Work Required ·············
Incentive Pay Scheme ···············
Variation in Tasks ·················
Hiring Bonus ·······················
Full-time/Part-time Choice ·········
Beautiful Location ·················
Inclusive Work-life Scheme ·········
Any Other Mention of Pay ···········
Company Vehicle ····················
Collective Agreement Pay ···········
On-call Employment ·················
Temporary Job ······················
Shift Work ·························
Part-time Contract ·················
Weekend/Evening/Night Work ·········
-.15 -.1 -.05 0 .05 .1 (c) Poaching Index
Pension Scheme ·····················
Insurance Scheme ···················
Full-time Contract ·················
Challenging Tasks ··················
Good Colleagues ····················
Central Location ···················
Interesting Tasks ··················
Possibility to Work Flexible Hours ·
Collective Agreement Pay ···········
Social Environment ·················
Work Involves Travelling ···········
Company Gym or Sports Team ·········
Permanent Job ······················
Competitive Pay ····················
On-the-Job Training ················
Involves Leadership Responsibility ·
Compensation Level ·················
Possibility for Remote Work ········
Company Cabin ······················
Inclusive Work-life Scheme ·········
Independence in Performing Tasks ···
Occupational Health Service ········
Mortgage Possibility ···············
Flexible/Extended Holidays ·········
Parking Space On Premises ··········
Variation in Tasks ·················
Any Other Mention of Pay ···········
Good Overtime Pay ··················
Company Canteen ····················
Any Welfare Scheme ·················
Fixed-term Contract ················
Exempt from Work Hour Regulations ··
Hiring Bonus ·······················
Shared Office Space ················
Regular Daytime Work Schedule ······
Overtime Work Required ·············
Beautiful Location ·················
Responsibility in Job ··············
Full-time/Part-time Choice ·········
Company Vehicle ····················
Incentive Pay Scheme ···············
Good Career Paths ··················
Shift Work ·························
On-call Employment ·················
Temporary Job ······················
Part-time Contract ·················
Weekend/Evening/Night Work ·········
-.1 -.05 0 .05 .1 .15
Notes: This figure shows parameter estimates and 90% confidence intervals from separate regressions of the share of each ad attribute on Employer
Pay Premium, Employer Overall Sorkin Value, and Employer Poaching Index, capturing the change in the fraction of ads with each job attribute
associated with a standard deviation increase in employer value. Estimations are done at the employer-cluster level for the period from 2021 to 2024,
and are weighted by the number of worker-years. On average, each cluster has 100 establishments, i.e., G =round(J/100) = 711 unique employer
clusters, while Figure 4 shows the corresponding results in our baseline with G =round(J/50) = 1 , 422 unique employer clusters.
[Appendix-16]

Figure A.13: Publicly Advertised Job Attributes By Sorkin Flow Value.
(a) Baseline
Full-time Contract ·················
Pension Scheme ·····················
Insurance Scheme ···················
Competitive Pay ····················
Good Colleagues ····················
Challenging Tasks ··················
Possibility to Work Flexible Hours ·
Interesting Tasks ··················
Permanent Job ······················
Central Location ···················
Work Involves Travelling ···········
Company Gym or Sports Team ·········
Involves Leadership Responsibility ·
Good Career Paths ··················
Possibility for Remote Work ········
Compensation Level ·················
Company Cabin ······················
Independence in Performing Tasks ···
Good Overtime Pay ··················
Mortgage Possibility ···············
Flexible/Extended Holidays ·········
Incentive Pay Scheme ···············
Occupational Health Service ········
Social Environment ·················
Any Welfare Scheme ·················
Company Canteen ····················
On-the-Job Training ················
Responsibility in Job ··············
Shared Office Space ················
Regular Daytime Work Schedule ······
Fixed-term Contract ················
Exempt from Work Hour Regulations ··
Overtime Work Required ·············
Parking Space On Premises ··········
Full-time/Part-time Choice ·········
Hiring Bonus ·······················
Company Vehicle ····················
Beautiful Location ·················
Variation in Tasks ·················
Inclusive Work-life Scheme ·········
Any Other Mention of Pay ···········
Collective Agreement Pay ···········
On-call Employment ·················
Temporary Job ······················
Shift Work ·························
Part-time Contract ·················
Weekend/Evening/Night Work ·········
-.15 -.1 -.05 0 .05 .1 (b) Smaller Clusters
Full-time Contract ·················
Pension Scheme ·····················
Insurance Scheme ···················
Competitive Pay ····················
Challenging Tasks ··················
Good Colleagues ····················
Possibility to Work Flexible Hours ·
Interesting Tasks ··················
Permanent Job ······················
Central Location ···················
Work Involves Travelling ···········
Company Gym or Sports Team ·········
Involves Leadership Responsibility ·
Good Career Paths ··················
Possibility for Remote Work ········
Compensation Level ·················
Company Cabin ······················
Incentive Pay Scheme ···············
Independence in Performing Tasks ···
Mortgage Possibility ···············
Flexible/Extended Holidays ·········
Occupational Health Service ········
Good Overtime Pay ··················
On-the-Job Training ················
Social Environment ·················
Company Canteen ····················
Any Welfare Scheme ·················
Responsibility in Job ··············
Regular Daytime Work Schedule ······
Shared Office Space ················
Parking Space On Premises ··········
Overtime Work Required ·············
Fixed-term Contract ················
Exempt from Work Hour Regulations ··
Full-time/Part-time Choice ·········
Hiring Bonus ·······················
Company Vehicle ····················
Beautiful Location ·················
Any Other Mention of Pay ···········
Variation in Tasks ·················
Inclusive Work-life Scheme ·········
On-call Employment ·················
Collective Agreement Pay ···········
Temporary Job ······················
Shift Work ·························
Part-time Contract ·················
Weekend/Evening/Night Work ·········
-.15 -.1 -.05 0 .05 .1 (c) Larger Clusters
Full-time Contract ·················
Pension Scheme ·····················
Insurance Scheme ···················
Competitive Pay ····················
Challenging Tasks ··················
Good Colleagues ····················
Possibility to Work Flexible Hours ·
Interesting Tasks ··················
Permanent Job ······················
Central Location ···················
Work Involves Travelling ···········
Company Gym or Sports Team ·········
Involves Leadership Responsibility ·
Good Career Paths ··················
Possibility for Remote Work ········
Compensation Level ·················
Company Cabin ······················
Incentive Pay Scheme ···············
Independence in Performing Tasks ···
Mortgage Possibility ···············
Flexible/Extended Holidays ·········
Occupational Health Service ········
Good Overtime Pay ··················
On-the-Job Training ················
Social Environment ·················
Company Canteen ····················
Any Welfare Scheme ·················
Responsibility in Job ··············
Regular Daytime Work Schedule ······
Shared Office Space ················
Parking Space On Premises ··········
Overtime Work Required ·············
Fixed-term Contract ················
Exempt from Work Hour Regulations ··
Full-time/Part-time Choice ·········
Hiring Bonus ·······················
Company Vehicle ····················
Beautiful Location ·················
Any Other Mention of Pay ···········
Variation in Tasks ·················
Inclusive Work-life Scheme ·········
On-call Employment ·················
Collective Agreement Pay ···········
Temporary Job ······················
Shift Work ·························
Part-time Contract ·················
Weekend/Evening/Night Work ·········
-.15 -.1 -.05 0 .05 .1
Notes: This figure shows parameter estimates and 90% confidence intervals from separate regressions of the share of each ad attribute on Employer
Sorkin Flow Value, capturing the change in the fraction of ads with each job attribute associated with a standard deviation increase in employer
value. Estimations are done at the employer-cluster level for the period from 2021 to 2024, and are weighted by the number of worker-years.
The baseline model in panel (a) features G = round(J/50) = 1 , 422 unique employer clusters, while panel (b) shows results using smaller clusters
(G = round(J/25) = 2 , 843 unique employer clusters) and panel (c) shows results using larger clusters ( G = round(J/100) = 711 unique employer
clusters).
[Appendix-17]

Figure A.14: Publicly Advertised Job Attributes By Employment Size.
(a) Baseline
Central Location ···················
Pension Scheme ·····················
Challenging Tasks ··················
Company Gym or Sports Team ·········
Compensation Level ·················
Collective Agreement Pay ···········
Full-time Contract ·················
Any Welfare Scheme ·················
Possibility to Work Flexible Hours ·
On-the-Job Training ················
Interesting Tasks ··················
Good Colleagues ····················
Shift Work ·························
Insurance Scheme ···················
Involves Leadership Responsibility ·
Work Involves Travelling ···········
Social Environment ·················
Occupational Health Service ········
Permanent Job ······················
Company Cabin ······················
Mortgage Possibility ···············
Possibility for Remote Work ········
Fixed-term Contract ················
Inclusive Work-life Scheme ·········
Parking Space On Premises ··········
Exempt from Work Hour Regulations ··
Good Overtime Pay ··················
Flexible/Extended Holidays ·········
Regular Daytime Work Schedule ······
Shared Office Space ················
Company Canteen ····················
Hiring Bonus ·······················
Overtime Work Required ·············
Full-time/Part-time Choice ·········
Beautiful Location ·················
Responsibility in Job ··············
Variation in Tasks ·················
Incentive Pay Scheme ···············
Independence in Performing Tasks ···
Good Career Paths ··················
Temporary Job ······················
Any Other Mention of Pay ···········
Competitive Pay ····················
On-call Employment ·················
Company Vehicle ····················
Weekend/Evening/Night Work ·········
Part-time Contract ·················
-.05 0 .05 .1 .15 (b) Smaller Clusters
Central Location ···················
Challenging Tasks ··················
Pension Scheme ·····················
Company Gym or Sports Team ·········
Compensation Level ·················
Collective Agreement Pay ···········
Any Welfare Scheme ·················
Full-time Contract ·················
Possibility to Work Flexible Hours ·
On-the-Job Training ················
Interesting Tasks ··················
Shift Work ·························
Good Colleagues ····················
Insurance Scheme ···················
Involves Leadership Responsibility ·
Work Involves Travelling ···········
Social Environment ·················
Occupational Health Service ········
Permanent Job ······················
Company Cabin ······················
Mortgage Possibility ···············
Inclusive Work-life Scheme ·········
Possibility for Remote Work ········
Fixed-term Contract ················
Parking Space On Premises ··········
Exempt from Work Hour Regulations ··
Good Overtime Pay ··················
Flexible/Extended Holidays ·········
Regular Daytime Work Schedule ······
Shared Office Space ················
Company Canteen ····················
Hiring Bonus ·······················
Overtime Work Required ·············
Full-time/Part-time Choice ·········
Responsibility in Job ··············
Incentive Pay Scheme ···············
Beautiful Location ·················
Variation in Tasks ·················
Independence in Performing Tasks ···
Good Career Paths ··················
Temporary Job ······················
Competitive Pay ····················
Any Other Mention of Pay ···········
On-call Employment ·················
Company Vehicle ····················
Weekend/Evening/Night Work ·········
Part-time Contract ·················
-.05 0 .05 .1 .15 (c) Larger Clusters
Central Location ···················
Pension Scheme ·····················
Challenging Tasks ··················
Company Gym or Sports Team ·········
Compensation Level ·················
Collective Agreement Pay ···········
Possibility to Work Flexible Hours ·
Any Welfare Scheme ·················
Full-time Contract ·················
Interesting Tasks ··················
On-the-Job Training ················
Insurance Scheme ···················
Good Colleagues ····················
Shift Work ·························
Involves Leadership Responsibility ·
Social Environment ·················
Work Involves Travelling ···········
Occupational Health Service ········
Permanent Job ······················
Company Cabin ······················
Mortgage Possibility ···············
Possibility for Remote Work ········
Inclusive Work-life Scheme ·········
Parking Space On Premises ··········
Fixed-term Contract ················
Exempt from Work Hour Regulations ··
Good Overtime Pay ··················
Regular Daytime Work Schedule ······
Variation in Tasks ·················
Flexible/Extended Holidays ·········
Shared Office Space ················
Hiring Bonus ·······················
Company Canteen ····················
Overtime Work Required ·············
Full-time/Part-time Choice ·········
Beautiful Location ·················
Responsibility in Job ··············
Independence in Performing Tasks ···
Competitive Pay ····················
Incentive Pay Scheme ···············
Any Other Mention of Pay ···········
Company Vehicle ····················
On-call Employment ·················
Temporary Job ······················
Good Career Paths ··················
Weekend/Evening/Night Work ·········
Part-time Contract ·················
-.1 -.05 0 .05 .1 .15
Notes: This figure shows parameter estimates and 90% confidence intervals from separate regressions of the share of each ad attribute on Employer
Size (in logs), capturing the change in the fraction of ads with each job attribute associated with a standard deviation increase in size. Estimations
are done at the employer-cluster level for the period from 2021 to 2024, and are weighted by the number of worker-years. The baseline model in
panel (a) features G = round(J/50) = 1 , 422 unique employer clusters, while panel (b) shows results using smaller clusters ( G = round(J/25) = 2 , 843
unique employer clusters) and panel (c) shows results using larger clusters ( G = round(J/100) = 711 unique employer clusters).
[Appendix-18]

Figure A.15: Predictive Power of Publicly Advertised Job Attributes: By Cluster Size.
(a) Baseline Model: G = round(J/50)
Overall Partial Overall Partial Overall Partial Overall Partial Overall Partial
Pay Overall Flow Poaching Employment
Premium Sorkin Value Sorkin Value Index Size
0
.1
.2
.3
.4
.5
.6
.7
.8
.9
1
Adjusted R
2
 (Shapley)

     Pay
 Attributes
  Non-Pay
 Attributes
      Other Ad
 Characteristics
(b) Smaller Clusters: G = round(J/25)
Overall Partial Overall Partial Overall Partial Overall Partial Overall Partial
Pay Overall Flow Poaching Employment
Premium Sorkin Value Sorkin Value Index Size
0
.1
.2
.3
.4
.5
.6
.7
.8
.9
1
Adjusted R
2
 (Shapley)

     Pay
 Attributes
  Non-Pay
 Attributes
      Other Ad
 Characteristics (c) Larger Clusters: G = round(J/100)
Overall Partial Overall Partial Overall Partial Overall Partial Overall Partial
Pay Overall Flow Poaching Employment
Premium Sorkin Value Sorkin Value Index Size
0
.1
.2
.3
.4
.5
.6
.7
.8
.9
1
Adjusted R
2
 (Shapley)

     Pay
 Attributes
  Non-Pay
 Attributes
      Other Ad
 Characteristics
0WFSBMM 1BSUJBM
5PUBM7BMVF
7K
0WFSBMM 1BSUJBM
1BZ
ψK
0WFSBMM 1BSUJBM
/PO1BZ
BK
0WFSBMM 1BSUJBM
+PC4FDVSJUZ
TK











"EKVTUFE3

1BZ
"UUSJCVUFT

/PO1BZ
"UUSJCVUFT


0UIFS
"E
"UUSJCVUFT
Notes: This figure documents adjusted R2 from regressions of cluster-size specific estimated model parameters
on ad attributes and characteristics in the text analysis as in Figure 5. Estimations are done at the employer-
cluster level for the 2021-2024 sample and are weighted by the total number of worker-years in each cluster
and period. Overall R2s are from regressions that include ad attributes and other ad characteristics, while
partial R2s are from regressions that also control for the composition of industry, occupation and location in
each cluster. Industry and occupation controls are defined at the two-digit level. Location indicators split
local municipalities into deciles, with municipalities in the same group having similar number of workers
(Oslo as an own group). The baseline model in panel (a) features G = round(J/50) = 1 , 422 unique
employer clusters, while panel (b) shows results using smaller clusters ( G = round(J/25) = 2 , 843) and panel
(c) shows results using larger clusters ( G = round(J/100) = 711 ).
[Appendix-19]

Figure A.16: Predictive Power of Publicly Advertised Job Attributes, 2015-2024.
(a) Baseline Sample: 2021-2024
Overall Partial Overall Partial Overall Partial Overall Partial Overall Partial
Pay Overall Flow Poaching Employment
Premium Sorkin Value Sorkin Value Index Size
0
.1
.2
.3
.4
.5
.6
.7
.8
.9
1
Adjusted R
2
 (Shapley)

     Pay
 Attributes
  Non-Pay
 Attributes
      Other Ad
 Characteristics
(b) Extended Sample: 2015-2024
Overall Partial Overall Partial Overall Partial Overall Partial Overall Partial
Pay Overall Flow Poaching Employment
Premium Sorkin Value Sorkin Value Index Size
0
.1
.2
.3
.4
.5
.6
.7
.8
.9
1
Adjusted R
2
 (Shapley)

     Pay
 Attributes
  Non-Pay
 Attributes
      Other Ad
 Characteristics
0WFSBMM 1BSUJBM
5PUBM7BMVF
7K
0WFSBMM 1BSUJBM
1BZ
ψK
0WFSBMM 1BSUJBM
/PO1BZ
BK
0WFSBMM 1BSUJBM
+PC4FDVSJUZ
TK











"EKVTUFE3

1BZ
"UUSJCVUFT

/PO1BZ
"UUSJCVUFT


0UIFS
"E
"UUSJCVUFT
Notes: This figure documents adjusted R2 from regressions of estimated population group-specific model
parameters on ad attributes and characteristics in the text analysis as in Figure 5. Estimations are done
at the employer-cluster level for the baseline sample period from 2021 to 2024 (Panel a) and from 2015 to
2024 (Panel b), and are weighted by the total number of worker-years in each cluster and period. Overall
R2s are from regressions that include ad attributes and other ad characteristics, while partial R2s are from
regressions that also control for the composition of industry, occupation and location in each cluster. Industry
and occupation controls are defined at the two digit level. Location indicators split local municipalities into
deciles, with municipalities in the same group having similar number of workers (Oslo as an own group).
[Appendix-20]

Figure A.17: Decomposing the Predictive Power of Publicly Advertised Job Attributes.
(a) Pay Premium
0
.1
.2
.3
.4
.5
.6
.7
.8
.9
1
Adjusted R
2
 (Shapley)

(b) Overall Sorkin Value
0
.1
.2
.3
.4
.5
.6
.7
.8
.9
1
Adjusted R
2
 (Shapley)
 (c) Poaching Index
0
.1
.2
.3
.4
.5
.6
.7
.8
.9
1
Adjusted R
2
 (Shapley)

(d) Flow Sorkin Value
0
.1
.2
.3
.4
.5
.6
.7
.8
.9
1
Adjusted R
2
 (Shapley)
 (e) Employment Size
0
.1
.2
.3
.4
.5
.6
.7
.8
.9
1
Adjusted R
2
 (Shapley)

0
.1
.2
.3
.4
.5
.6
.7
.8
.9
1Adjusted R
2
 (Shapley)

Career Opportunities Minor Perks Company Name Disclosed
Financial Attributes Task-Related Attributes Number of Attributes
Compensation Scheme Workplace Attributes Number of Words
Contract Duration
Inconvenient Hours
Convenient Hours
Hours of Work
Notes: This figure documents adjusted R2s from regressions of estimated employer values on pay and non-
pay job attributes and other ad characteristics detected in the text analysis as in Figure 5, decomposing
the overall adjusted R2s into ten broad categories of pay and non-pay attributes using the Shapley Value
Decomposition. Estimations are done at the employer-cluster level for the period from 2021 to 2024, and
are weighted by the number of worker-years in each cluster.
[Appendix-21]

Figure A.18: Predictive Power of Publicly Advertised Job Attributes: By Industry.
(a) Pay Premium
0 .1 .2 .3 .4 .5 .6 .7 .8 .9 1
Adjusted R
2
Health and Social Services
Natural Resource Extraction and Supply
Public Administration
Manufacturing
Construction
Other
Financial Services and Real Estate
Retail and Services
Professional and Support Service Activities
Education
(b) Overall Sorkin Value
0 .1 .2 .3 .4 .5 .6 .7 .8 .9 1
Adjusted R
2
Retail and Services
Other
Health and Social Services
Natural Resource Extraction and Supply
Construction
Manufacturing
Financial Services and Real Estate
Professional and Support Service Activities
Education
Public Administration (c) Poaching Index
0 .1 .2 .3 .4 .5 .6 .7 .8 .9 1
Adjusted R
2
Financial Services and Real Estate
Retail and Services
Manufacturing
Construction
Public Administration
Professional and Support Service Activities
Other
Natural Resource Extraction and Supply
Health and Social Services
Education
(d) Flow Sorkin Value
0 .1 .2 .3 .4 .5 .6 .7 .8 .9 1
Adjusted R
2
Retail and Services
Health and Social Services
Other
Natural Resource Extraction and Supply
Manufacturing
Construction
Professional and Support Service Activities
Education
Public Administration
Financial Services and Real Estate (e) Employment Size
0 .1 .2 .3 .4 .5 .6 .7 .8 .9 1
Adjusted R
2
Public Administration
Natural Resource Extraction and Supply
Other
Retail and Services
Health and Social Services
Manufacturing
Education
Financial Services and Real Estate
Construction
Professional and Support Service Activities
Notes: This figure documents adjusted R2s from regressions of estimated employer values on pay and non-
pay job attributes and other ad characteristics detected in the text analysis as in Figure 5. Estimations are
done separately for the ten main industry groups at the employer-cluster level for the period from 2021 to
2024, and are weighted by the number of worker-years in each cluster. We assign an industry to each cluster
g based on the modal industry among the establishments in the cluster.
[Appendix-22]

B Details on the Text Analysis
Section B.1 documents how we clean the text of job ads before detecting job attributes.
Section B.2 describes one of the processes we use to generate the complete lists of attributes
we search for in vacancy texts. SectionB.3 provides descriptions of detailed attributes and
displays some of the phrases used to detect these attributes.
B.1 Text Cleaning of Job Ads
Before extracting attributes from job ads, we apply some simple text cleaning. We first
search for and remove HTML tags, which always take the form “<...>”, to avoid treating
HTML code as potential job attributes and to reduce the number of words processed by the
phrase-generation model. We keep a record of which ads contain such tags.
We replace numbers in ads with flags indicating their range and whether they are followed
by a percentage sign. This allows us to group similar phrases that differ only in their specific
numbers. For example, “50%” and “40%” both commonly indicate part-time jobs, so we
group all phrases of the form {number below 100}% under a single flag rather than searching
for each value individually. Specifically, we flag numbers below 100 (and 100 itself) followed
by a percentage sign or the word “percentage”. We then assign separate flags to each integer
from one to four, remaining numbers in(0, 100), the number 100, and numbers greater than
100.
Before storing the ads, we split each ad into sentences and each sentence into words.
We do this because the language model we use to expand the dictionary of target phrases
expects input in this form. Splitting into sentences also prevents words at the end of one
sentence from being conflated with words at the beginning of the next. We use the Python
package nltk for this, with a tokenization model trained on a Norwegian corpus. The model
correctly handles periods that do not mark sentence boundaries, such as those appearing in
common abbreviations.
B.2 Extracting Common Attributes from “We Offer” Lists
Our choice of pay and non-pay attributes to include in the text analysis is partly informed by
attributes commonly advertised in “we offer” sections of job ads. We document our approach
here, and show that social environment, on-the-job training, tasks, pension schemes, and
insurance schemes are among the most commonly advertised attributes in such sections.
Our approach has four steps: (i) we extract lists from the corpus of job ads; (ii) we sort
these lists into four topics using a latent Dirichlet allocation (LDA) topic model; (iii) we
[Appendix-23]

identify the topic corresponding to “we offer” sections by inspecting the words and lists
most closely associated with it; and (iv) we extract common phrases from the lists assigned
to this topic. We then assign phrases to attribute categories and add these categories to the
set of attributes we search for in the ads.
Extracting lists from vacancies To identify “we offer” sections, we start by extracting
lists from the full corpus of job ads. Lists are commonly used in job ads to group related
information, such as skill requirements, tasks, and pay and non-pay attributes. We extract
lists by identifying sequences of the HTML tag<li>, which denotes list elements in web
pages, or plain-text lines beginning with a centered dot (·), hyphen (-), or star (*). We
combine each such sequence with the preceding sentence, which typically serves as the list
header, into a single observation. This process allows us to extract sections of ads that
are likely to focus on a single topic. We extract close to 1.5 million lists from around 50%
of the ads, though the approach may omit some lists that do not follow these formatting
conventions.
Sorting lists into different topics To distinguish “we offer” lists from lists covering
other topics, we apply Latent Dirichlet Allocation (LDA) to the collection of lists [Blei et al.,
2003]. LDA is commonly used in natural language processing to partition a collection of texts
into topics. It assigns texts toK categories such that words frequently occurring in topick
are unlikely to occur in other topics. The model performs well when topics are associated
with distinctive vocabulary, but it ignores word order, which can make individual words less
informative. For example, “good” commonly appears in descriptions of workplace amenities
or pay, but carries little information about the specific attribute without its context. Addi-
tionally, some lists combine “we offer” content with other topics, such as skill requirements,
so we expect to lose some “we offer” content that the model assigns to other topics.
LDA models each word as drawn from a mixture ofK topic-specific word distributions.
Each text is associated with its own mixture over theK topics, so the probability that a
word is drawn from topick varies across texts. That is, the probability that wordi in text
j (wij) equals “offer” is
Pr(wij = “offer”) =
KX
k=1
Pr(wij = “offer”|topicij =k) Pr(topicij =k)
We set the number of topics toK = 4 and estimate the model by maximum likelihood using
the Python packagegensim.
[Appendix-24]

Labelling topics After estimating the model, we label the four topics by inspecting the
word distributions and the list-specific topic mixtures. Table B.1 reports the ten words
most strongly associated with each topic, i.e., those with the highest probability of being
drawn from that topic. Words in topics 1–3 are associated with (1) pay and non-pay job
attributes, (2) skill requirements, and (3) task descriptions, while topic 4 contains a mixture
of requirements (e.g., education and police certificate), additional information (e.g., contact
details), and ambiguous words (numbers and “work”). We label topics 1–3 accordingly, and
topic 4 as a “Residual Category”.
The pay and non-pay attributes topic contains words commonly used to indicate a good
socialenvironment, informationaboutpay, andtask-relatedattributesthatmaybeattractive
to workers (e.g., challenging tasks). We label this topic “We Offer”. We note that some words
in this topic are ambiguous outside their original context; for example, “development” can
refer to personal development or to project-based work tasks.
We validate these labels by inspecting the lists most strongly associated with each topic,
shown in FiguresB.1–B.4. Unlike the word distributions, these lists preserve the original
phrasing and context, addressing the bag-of-words limitation of LDA. The lists largely con-
firm the assigned labels. The list most strongly associated with the “We Offer” topic begins
with the header “we offer:” and contains information about various non-pay amenities. The
list most strongly associated with the “Residual Category” contains miscellaneous job infor-
mation, such as details about the hiring process and pay. Overall, lists in the “We Offer”
category appear to contain dense information about amenities, though we are likely to lose
some pay and non-pay content that the model assigns to other categories.
Extracting common phrases from “We Offer” sections To identify specific job at-
tributes commonly advertised in vacancies, we focus on common phrases in lists assigned
to the “We Offer” topic. We assign each list to the topic with the highest probability in
its topic distribution, and extract approximately 260,000 lists under the “We Offer” label,
representing 17% of all lists.
We then extract and inspect the 200 most common unigrams, bigrams, and trigrams,
excluding phrases that include stopwords (e.g., “and”). We add phrases indicating pay or
non-pay attributes to our dictionary, and create new attribute categories for any attribute
not currently included.
Table B.2 reports the 10 most common unigrams, bigrams, and trigrams in “We Offer”
lists, excluding phrases without a clear reference to a specific job attribute. The table
shows that these lists commonly refer to the social environment, pay, pension and insurance
schemes, and on-the-job training. The procedure uncovers relatively few attributes related
[Appendix-25]

to hours of work, which are likely described in other sections of the ads, such as the practical
information found in lists assigned to the “Residual Category.”
Table B.1: Words Used to Separate Lists Into Topics
Topic 1: We-Offer Topic 2: Skill Requirements Topic 3: Tasks Topic 4: Residual Category
Word Probability Word Probability Word Probability Word Probability
(1) (2) (3) (4) (5) (6) (7) (8)
“offer” 0.037 “experience” 0.038 “tasks” 0.025 Number > 99 0.044
“good (plural)” 0.032 “good (plural)” 0.027 “responsibility” 0.011 Number in [5-99] 0.024
“workplace environment” 0.029 “good” 0.024 “to follow up” 0.010 “have to” 0.016
“good (alternative form)” 0.026 “qualifications” 0.021 “contribute” 0.009 “Field of education” 0.009
“pay” 0.019 “ability” 0.016 “cooperation” 0.009 “police certificate” 0.008
“professional” 0.017 “Norwegian” 0.014 “other” 0.008 “contact information” 0.007
“exciting” 0.015 “relevant” 0.014 “tasks” 0.007 “level of education” 0.007
“tasks” 0.014 “written” 0.014 “participate” 0.007 “The position” 0.007
“developement” 0.014 “oral” 0.013 “customers” 0.006 “work” 0.006
“challenging” 0.010 “traits” 0.013 “developement” 0.005 “two” 0.006
Notes: This table documents the words that are most strongly associated with the topics identified by
applying Latent Dirichlet Allocation to our collection of lists. Columns (2), (4), (6), and (8) contain estimated
probabilities of drawing the corresponding word given that the word is drawn from the distribution associated
with that topic. The table shows the words with the 10 largest probabilities for each topic. “Number > 99”
and “Number in [5-99]” are flags that we have inserted into the vacancy in the cleaning step to group numbers
by range. Translation from Norwegian by the authors. Each entry is a single Norwegian word, although
the English translations sometimes require more than one word. Clarifications in parentheses are added
whenever multiple distinct Norwegian words have identical English translations. The table is constructed
using the period from 2002 to 2021.
[Appendix-26]

Figure B.1: Sample List Assigned to Topic “We Offer”.
We offer:
- a unique opportunity to set foot in Norway’s leading exercise company.
- an incredibly exciting job that offers some real challenges that provide a lot of
development as a person.
- very competitive conditions.
- we offer the industry’s best training program and very good career opportunities
for the right person.
Notes: This figure shows the list that the model most strongly associates with the “we offer” topic. This
means that the model assigns a probability of almost 1 for words in this list to be drawn from the distribution
associated with “we offer. ” Translation from Norwegian by the authors.
Figure B.2: Sample List Assigned to Topic “Skill Requirements”.
We are looking for someone who:
- has relevant education in economics, marketing and/or technical subjects.
- has good knowledge of the Norwegian retail.
- has ability to motivate and inspire others.
- communicates effectively and well, written and oral.
[...]
Notes: This figure shows the list that the model most strongly associates with the “skill requirement” topic.
This means that the model assigns a probability of almost 1 for words in this list to be drawn from the
distribution associated with “skill requirement. ” Translation from Norwegian by the authors.
[Appendix-27]

Figure B.3: Sample List Assigned to Topic “Tasks”.
Tasks:
- personnel responsibility for all resources associated with the section.
- financial management and responsibility for results within the area.
- coordination with other sections and departments.
- be the driving force behind the company’s proactive approach to security and
risk.
[...]
Notes: This figure shows the list that the model most strongly associates with the topic “tasks” . This means
that the model assigns a probability of almost 1 for words in this list to be drawn from the distribution
associated with the topic “tasks. ” Translation from Norwegian by the authors.
Figure B.4: Sample List Assigned to Topic “Residual Category”.
Start date, salary placement, and general information about the position:
- the position is a temporary position with a duration until March and is available
for immediate entry.
- the position of chief police oﬀicer is placed in salary plan [number> 100] to
[number> 100].
- our personnel policy is to have a employees from different backgrounds. We
therefore encourage women and people with minority background to apply.
- the statutory pension premium is deducted from the salary
- spotless conduct is required. A certificate from the police will be obtained.
- applicants may be called to an interview.
[...]
Notes: This figure shows the list that the model most strongly associates with the residual category. This
means that the model assigns a probability of almost 1 for words in this list to be drawn from the distribution
associated with the residual category. Translation from Norwegian by the authors.
[Appendix-28]

Table B.2: Most Frequent Phrases in “We-Offer” Lists.
Rank Phrases English Translation Occurrences Assigned Attribute Category
(1) (2) (3) (4) (5)
Panel A: Unigrams
3 “arbeidsmiljø” “workplace environment” 138,459 Social Environment
5 “lønn” “pay” 91,477 Any Other Mention of Pay
6 “spennende” “exciting” 88,695 Interesting Tasks
12 “utfordrende” “challenging” 59,382 Challenging Tasks
21 “opplæring” “training” 37,351 On-the-Job Training
24 “pensjons” “pension” 32,520 Pension Scheme
25 “pensjonsordning” “pension scheme” 32,434 Pension Scheme
26 “utviklingsmuligheter” “opportunities for development” 31,724 Good Career Paths
28 “forsikringsordninger” “insurance schemes” 30,366 Insurance Scheme
36 “oslo” “oslo” 23,336 Central Location
Panel B: Bigrams
1 “godt arbeidsmiljø” “good workplace environment” 65,143 Social Environment
2 “konkurransedyktige betingelser” “competitive conditions” 38,016 Competitive Pay
3 “gode pensjons” “good pension” 22,344 Pension Scheme
4 “faglig utvikling” “professional development” 18,415 On-the-Job Traning
5 “varierte arbeidsoppgaver” “varying tasks” 18,085 Variation in Tasks
7 “utfordrende arbeidsoppgaver” “challenging tasks” 17,777 Challenging Tasks
8 “fleksibel arbeidstid” “flexible work hours” 16,700 Possibility to Work Flexible Hours
10 “personlig utvikling” “personal development” 15,617 On-the-Job Traning
11 “trivelig arbeidsmiljø” “pleasant working environment” 14,591 Social Environment
12 “god pensjonsordning” “good pension scheme” 12,854 Pension Scheme
Panel C: Trigrams
1 “høyt faglig nivå” “high professional level” 6,021 Good Colleagues
2 “god pensjonsordning gjennom” “good pension scheme through ” 3,716 Pension Scheme
7 “godt faglig miljø” “good professional environment” 2,134 Good Colleagues
8 “pensjonsordning gjennom klp” “pension scheme through klp” 2,009 Pension Scheme
9 “godt sosialt miljø” “good social environment” 1,905 Social Environment
10 “gjennom statens pensjonskasse” “public pension fund” 1,805 Pension Scheme
17 “faglig dyktige kollegaer” “professionaly skilles colleagues ” 1,195 Good Colleagues
18 “pensjonsordning gjennom statens” “pension scheme through public” 1,183 Pension Scheme
19 “ulykkesforsikring samt fritidsulykkeforsikring” “sport and general accident insurance” 1,159 Insurance Scheme
20 “svært godt arbeidsmiljø” “very good social environment” 1,129 Social Environment
Notes: This table documents the words occurring most frequently in the “we offer” lists extracted from the
vacancies. Column 3 shows which attribute category we have assigned the word to. These categories are
added to the list of attributes we search for in the vacancies. Not every word is assigned to an attribute
category. The translations are provided by the authors. Every phrase is originally one word in Norwegian.
The table is constructed using the period from 2002 to 2021.
B.3 Description of Detailed Pay and Non-Pay Attributes
Tables B.3 to B.5 describe each attribute we search for in job ads and provide examples of
the phrases used to detect them. In our final dataset, we record each attribute as a binary
indicator equal to one whenever the text of the associated job ad contains any of the phrases
[Appendix-29]

associated with that attribute.50
Table B.3: Description of Pay Related Attributes.
Attribute Description Example Phrases (translated) Example Phrases (Norwegian)
Compensation Scheme:
– Compensation Level Indication of pay, pay level, or pay range (e.g.,
steps in collective bargaining agreements).
wage step, wage range, wage rate lønnstrinn, lønnsspenn, lønnssats
– Competitive Pay Indication of good or competative salary. good pay conditions, competitive
wage, favorable pay conditions
gode lønnsbetingelser,
konkurransedyktig lønn, gunstige
lønnsbetingelser
– Collective Agreement Pay Explicit reference to a collective bargaining
agreement between trade unions and employers’
associations.
wage step, tariff agreement, the main
tariff agreement [public sector]
lønnstrinn, tariffavtale,
hovedtariffavtalen
– Incentive Pay Scheme Pay scheme dependents on an individual worker’s
or company’s performance.
commission, bonus scheme, sales
bonus
provisjon, bonusordning, salgsbonus
– Hiring Bonus One time bonus at time of hiring, usually to
encourage applicants.
recruitment supplement,
establishment supplement
rekrutteringstillegg,
rekrutteringstilskudd
– Good Overtime Pay Reference to the level of overtime pay. overtime pay, paid overtime overtidsbetalt, betalt overtid
– Any Other Mention of Pay Any other reference to pay, excluding any of the
attributes listed above.
pay, income, fixed salary lønn, inntekt, fastlønn
Financial Attributes:
– Pension Scheme Position covered by a pension scheme. Includes
reference to mandatory and additional pension
schemes.
pension scheme, occupational pension
scheme, contribusion based pension
savings
pensionsordning,
tjenestepensjonsordning,
inskuddspensjon
– Insurance Scheme Employer-sponsored insurance. Includes
mandatory and additional insurance schemes,
and coverage of proparty damage, various health
insurances and similar.
insurance scheme, group life insurance,
life insurance scheme, disability
insurance, health insurance
forsikriningsordning,
gruppelivsforsikring, livsforsikring,
uføreforsikring, helseforsikring
– Mortgage Possibility Employer provides access to mortgage schemes
with favorable conditions.
mortgage scheme, favorable mortgage boliglånsordning, gunstig lånetilbud
Career Opportunities:
– Good Career Paths Suggests that the position is a good step in
advancing a career, or that there are good
opportunities to advance within the employer.
career opportunities, promotions,
internal career
karrieremuligheter, forfremmelse,
intern karriere
– On-the-Job Training The position includes a training program or
internship or opportunities to learn new skills.
training program, professional
developement, internship
etterutdaningsmuligheter, faglig
utvikling, praksisplass
Notes: This table describes each of the pay-related attributes detected in vacancies and documents some of
the phrases used to detect these attributes. The phrases in Norwegian are used in the analysis, and the
translations to English are for illustration. Comments to individual phrases are displayed in brackets.
50The exception is the attribute “Any Other Mention of Pay”, which we construct by searching for generic
pay-related words and flagging the attribute as detected, but then setting the indicator to zero if any other
attribute listed under “Compensation Scheme” was already detected by the same set of words.
[Appendix-30]

Table B.4: Description of Non-Pay Related Attributes (Part 1).
Attribute Description Example Phrases (translated) Example Phrases (Norwegian)
Hours of Work:
– Full-time Contract Full time position, usually 37.5 hours per week. full-time position, full-time employee,
100%
fulltidsstilling, fulltidsansatt, 100%
– Part-time Contract Part-time position. part time, part-time position, 50%
[includes all numbers less than 100]
deltidsstilling, deltidsjobb, 50%
– Full-time/Part-time Choice Employer open for both full-time and part-time
hires.
full-time or part-time,
full-time/part-time
heltid eller deltid, fulltid/deltid
Convenient Hours:
– Possibility to Work Flexible Hours Flexible work hours, commonly reflecting
workers’ discretion to choose when to start or
stop work during a shift.
flexible working hours, flexible hours
scheme
fleksibel arbeidstid, fleksibel
arbeidstidsordning
– Regular Daytime Work Schedule Regular, day-time work hours, i.e. working on
evenings, nights or weekends is not required.
regular working hours normal arbeidsdag
– Exempt from Work Hour Regulations The job is exempt from the work hours regulation
covering most workers, usually leaders, academic
staff or similar.
exempt from the working environment
act, leader position [legal term],
doctoral fellow [always exempted]
untatt arbeidsmiljøloven, ledende
stilling, doktorgradsstilling
Inconvenient Hours:
– Shift Work Position requires shift work where employees
usually switch between working day, evening, and
night shifts.
shift work, rotation scheme, night shift skiftarbeid, turnusordning, natturnus
– Weekend/Evening/Night Work Position requires shift work involving either
working on weekends, evening, and/or night.
night shift, evening work,late night
shift
nattursnus, kveldsarbeid, senvakt
– On-call Employment Positions where the employer needs additional
on-call employees, often hired temporarily.
on-call help, on-call substitute, calling
help [norwegian expression],
ekstrahjelp, tilkallingsvikar, ringevikar
– Overtime Work Required Indication that some overtime work is required in
the position.
overtime work, some overtime
expected, overtime in periods
overtidsarbeid, påregnes noe overtid,
overtid i perioder
Contract Duration:
– Permanent Job Permanent job. permanent position, permanent
employment
fast stilling, fast ansettelse
– Temporary Job Temporary job, including substitute positions. temporary job, substitute position,
one year substitute
midlertidig stilling, vikariat,
ettårsvikariat
– Fixed-term Contract This position is restricted to a fixed period, and
is exempted from Norwegian restriction of the
length of temporary spells.
fixed-term contract [legel term] åremål
Workplace Attributes:
– Social Environment Indication of good social environment. good social environment, good
working community, great colleagues
godt arbeidsmiljø, godt
arbeidsfellessakap, flotte kolleger
– Good Colleagues Professional, knowledgable, helpful, or in other
ways good colleagues.
skilled colleagues, good colleagues,
knowledgeable colleagues, helpful
colleagues
dyktige kolleger, gode kolleger,
kunnskapsrike kolleger, hjelpsomme
kolleger
– Possibility for Remote Work Possibility to work remotely. home oﬀice, home oﬀice scheme, work
from home
hjemmekontor, hjemmekontorløsning,
arbeide hjemmefra
– Shared Oﬀice Space Shared oﬀice space. shared oﬀice space, open oﬀice space kontorlandskap, åpent landskap
– Inclusive Work-life Scheme Indication that the employer provides an
inclusive work-life scheme, which is a formal
work-life scheme that provides more generous
sick-leave arrangements.
inclusive work-life scheme, IA
[abbrevation]
inkluderende arbeidsliv, IA
Notes: This table and the next describe each of the non-pay-related attributes detected in vacancies and
document some of the phrases used to detect these attributes. The phrases in Norwegian are used in the
analysis, and the translations to English are for illustration. Comments to individual phrases are displayed
in brackets.
[Appendix-31]

Table B.5: Description of Non-Pay Related Attributes (Part 2).
Attribute Description Example Phrases (translated) Example Phrases (Norwegian)
Task-Related Attributes:
– Interesting Tasks Indicates interesting, exciting, or meaningful
tasks. Includes description of company, sector, or
industry.
interesting, exciting, meaningful interessante, spennende, meninsfylt
– Challenging Tasks Indicates challenging tasks. challenging, demanding utfordrende, krevende
– Variation in Tasks Varying, nonmonotonous tasks. varied tasks, versatile tasks varierte arbeidsoppgaver, allsidige
oppgaver
– Responsibility in Job Involves responsibilities. Includes responsibility
as leader or project manager.
full responsibility, a lot of
responsibilities, leadership
responsibilities
totalansvar, mye ansvar, lederansvar
– Independence in Performing Tasks Freedom to choose how to approach and solve
tasks.
manage the working day, influence
your own, shape your own
styre arbeidsdagen, påvirke egen,
utforme egen
– Involves Leadership Responsibility The job involves leadership responsibility. looking for CEO, leadership role,
communications director
søker daglig leder, lederrolle,
kommunikasjonsdirektør
– Work Involves Travelling The job requires traveling. business trips, travel days, travel
activity
arbeidsreiser, reisedøgn, reiseaktivitet
Minor Perks:
– Beautiful Location Describes the job location’s environment as
beautiful.
beautiful nature, magnificent nature,
great tracking environment
flott natur, praktfull natur, flott
turterreng
– Central Location Central location, including mentions of major
cities.
oslo [capial], centrally located, close to
the city center
oslo, sentral beliggenhet,
sentrumsnært
– Company Gym or Sports Team The company offers the opportunity for paid
exercise during work hours, access to fitness
center/equipment, and/or has a sports team or
the like.
company sports team, exercise during
work-hours, fitness room, fitness
center membership
bedriftsidrettslag, trening i
arbeidstiden, treningsrom,
treningsavtale
– Parking Space On Premises Available/free parking spaces on premises. parking facilities, free parking parkeringsmuligheter, gratis parkering
– Company Vehicle Access to company vehicle during work hours,
sometimes involves company vehicle available
full-time.
company vehicle, company vechicle
scheme, leasing vechicle
firmabil, bilordning, leasingbil
– Any Welfare Scheme Generic description of company welfare scheme. welfare schemes, personnel schemes,
employee benefits
velferdsordninger, personalordninger,
personalgoder
– Company Cabin The company has access to a cabin usable for
employees. These cabins can be accessable for
company arrangements or for employees’ access
during holidays or vacations.
company cabins, personnell cabin,
vacation apartments
firmahytte, personalhytte,
ferieleiligheter
– Occupational Health Service Access to health professionals and doctors.
Involves preventions and treatment of
injuries/sickness.
occupational health service, company
doctor
bedriftshelsetjeneste, bedriftslege
– Company Canteen Access to canteen. canteen scheme, personnell canteen kantineordning, personalkantine
– Flexible/Extended Holidays Description of the total length of vacation, or of
extended length compared to mandatory
vacation.
x week vacation [where x is a number],
extra vacation
x ukers ferie, ekstra feie
Notes: This table and the previous describe each of the non-pay-related attributes detected in vacancies and
document some of the phrases used to detect these attributes. The phrases in Norwegian are used in the
analysis, and the translations to English are for illustration. Comments to individual phrases are displayed
in brackets.
[Appendix-32]

C Details on Employer Quality Measures
C.1 Alternative Measures of Employer Quality
Employer Pay Premium We recover the pay premium from a standard two-sided unob-
served heterogeneity wage regression with worker and firm effects [Abowd et al., 1999]. We
estimate the regression
lnwit =X ′ itβ +αi +ψj(i,t) +eit, (C.1)
where wit are hourly wages,Xit are exogenous worker characteristics,αi is the unobserved
worker effect,ψj(i,t) is the unobserved firm effect of workeri’s employerj in periodt, and
eit is an idiosyncratic shock. As is standard in the literature, the vectorXit includes a set
of year-by-education fixed effects and a separate cubic age polynomial by education level
restricted to be flat at age 40 [Card et al., 2013].
Employer Value from the Utility-Posting Model We use the employer valueVj and
flow valueuj from the utility-posting model ofSorkin [2018], estimated from the full model
with employer-specific destruction and reallocation shocks, as described in Section V of the
original paper.51 For completeness, we summarize this model in Appendix SectionC.2.
Employer Poaching Index We use the poaching index defined inBagger and Lentz
[2019]. The index is constructed as
Poaching Indexj =
P
k,t EEkj,t P
k,t EEkj,t + NEj,t
. (C.2)
In Equation (C.2), EEkj,t denotes job-to-job flows from employerk to employerj, and NEj,t
denotes flows from non-employment to employerj.
Employment Size We define employment size as the number of worker-year observations
at each employer over the sample period.
C.2 Summary of the Utility-Posting Model
Environment Consider an economy in discrete time populated by a fixed measure of
infinitely-lived workers and a fixed discrete numberJ of employers. Workers have discount
51The literature is often ambiguous about which version of the model is reported. The model is sometimes
described as PageRank, which corresponds to a different normalization of the worker mobility transition
matrix. Many contributions also do not clarify whether they use all worker flows, only job-to-job flows, or
the full utility-posting model.
[Appendix-33]

factor β ∈ (0, 1) and can be either employed at one of theJ employers or non-employed.
Let j ∈ J = {1,...,J } denote employers andVj the value to a worker of being currently
employed at employerj. Let N denote non-employment andVN the value to a worker of
being currently non-employed. Both employed and non-employed workers search for better
employers. Search is random. When searching, workers make contact with one of thej ∈ J
employers with probabilityfj, wheref captures the relative weight of employers in workers’
search. We maintain the wage-posting (here “utility-posting”) assumption fromBurdett and
Mortensen [1998]. The value of working atj is summarized byVj and is not renegotiated
even in the event of a change in the workers’ outside option.
Worker flows between employers LetMjk denote the measure of workers making a job-
to-job move from employerj to employerk. Mjk is assumed to be the sum of involuntary
relocation flowsM R jk and voluntary flowsM V jk. Relocation job-to-job flows are given by
M R jk =Lj ·ρj ·fk, (C.3)
where Lj is employment atj, ρj is the probability that workers employed atj are forced to
reallocate to another employer, andfk is the probability that they find a job at employer
k.52 In Equation (C.3), workers do not make a choice and are forced to relocate to employer
k. This is in contrast with voluntary job-to-job flows, which are given by
M V jk =Lj · (1 −ρj −δj) ·λ1 ·fk ·Pr(k ≻j). (C.4)
Voluntary worker flows fromj to k are given by the measure of workers employed atj
(Lj), who are neither forced to reallocate (with probabilityρj) nor forced to move to non-
employment (with probabilityδj), search for an alternative employer (with probabilityλ1),
and get an offer from employerk with probabilityfk.53 In Equation (C.4), workers choose
whether to remain with employerj or move tok, which occurs with probability Pr(k ≻j).
This is the sense in which these flows are voluntary and reveal workers’ preferences over
the set of employersJ. We follow Sorkin [2018] and assume there are i.i.d. taste shocks
{εi}i∈{J ,N } that make the value of working at employerj and of non-employment worker-
specific in each period. We further assume that these shocks are drawn from a Gumbel
distribution with location parameter normalized to zero and scale parameterσ−1.54 With
52There are no such relocation shocks in Burdett and Mortensen [1998], but they are a common feature in
random search models with on-the-job search (see, e.g., Jolivet et al. [2006] and Bagger and Lentz [2019]).
53The probabilities ρj and δj are assumed to be mutually exclusive.
54Normalizing the location parameter to zero is without loss of generality because it shifts the value of
working at each employer j and of being in non-employment by the same amount.
[Appendix-34]

this assumption, the acceptance probability for a worker with a job offer from employerk
currently working atj is given by
Pr(k ≻j) = Pr(Vk +εk ≥Vj +εj) = exp(σVj) exp(σVj) + exp(σVk).
Worker flows to non-employment The flow measure of workers from employerj to
non-employment N is the sum of a relocation partM R jN and a voluntary partM V jN. The
relocation flow to non-employment is simply the fraction of employment at firmj hit by an
exogenous separation shockδj
M R jN =Lj ·δj. (C.5)
The voluntary flow to non-employment is given by the fraction of workers who decide to
leave employerj
M V jN =Lj · (1 −δj −ρj) · (1 −λ1) ·Pr(N ≻j), (C.6)
where 1 −δj −ρj is the fraction of workers who are not forced to reallocate and1 −λ1 is the
fraction of workers who do not have an alternative offer in the current period. Similarly to
the case of voluntary flows between employers (C.4), the probability that a worker employed
at j moves to non-employment is
Pr(N ≻j) = Pr(VN +εN ≥Vj +εj) = exp(VN ) exp(Vj) + exp(VN ), (C.7)
given the maintained assumption of i.i.d. idiosyncratic taste shocks(εj,ε N ) from an Extreme
Value Type I distribution.
Worker flows from non-employment All transitions from non-employmentN to em-
ployer j are voluntary. The decision to accept a job opportunity is again subject to i.i.d.
taste shocks(εN,ε j). The flow measure of workers moving from non-employment to employer
j is given by
MN j =LN ·λ0 ·fj · exp(Vj) exp(VN ) + exp(Vj). (C.8)
In Equation (C.8), LN is the measure of workers in non-employment,λ0 is the probability
that a non-employed worker gets an offer, andfj is the probability that the offer is from
employer j. For the identification result, it is required that the offer distributionf is the
[Appendix-35]

same for employed and non-employed workers, which we assume.
Value of employment The sequence of events described by the relocation and voluntary
worker flows in Equations (C.3)-(C.4) implies the following expression for the valueVj of
working at employerj. Let uj denote the flow utility of working atj. Vj can be expressed
as
Vj =uj +βδjE

VN +εN

+βρj
X
k∈J
fkE

Vk +εk

+β(1 −δj −ρj)λ1
X
k∈J
fkE

max

Vj +εj,V k +εk
	
+β(1 −δj −ρj)(1 −λ1)E

max

VN +εN,V j +εj
	
.
(C.9)
In Equation (C.9), the continuation value is made of the four following terms. With proba-
bility δj, the worker transitions to non-employment, an exogenous shock. With probability
ρj, the worker is hit by a relocation shock and is forced to move to an alternative employer by
drawing from the offer distributionf, an exogenous shock. With probability(1 −δj −ρj)λ1,
the worker gets an offer from a potential alternative employer by drawing from the offer
distributionf and decides whether to stay or move, an endogenous choice. With probability
(1 −δj −ρj)(1 −λ1), the worker decides whether to stay with their current employer or to
move to non-employment, also an endogenous choice. All expectationsE[.] are taken over
the i.i.d. taste shocks(εk,ε N ).
Value of non-employment With the notation introduced in Equation (C.8), the value
function of non-employment follows directly as
VN =uN +β
(
λ0
X
k
fkE

max

Vk +εk,V N +εN
	
+ (1 −λ0)E

VN +εN

)
, (C.10)
where uN is the flow value of non-employment andβ the discount factor. The continuation
value is made of two terms. With probabilityλ0, non-employed workers get a draw from the
offer distributionf, which they decide to accept or reject given their draw of taste shocks.
With probability 1 −λ0, they remain in non-employment. All expectationsE[.] are taken
over the i.i.d. taste shocks(εk,ε N ).
Identification The model has several employer-level parameters, such as workers’ valu-
ations of alternative employers{Vj}j∈J, and aggregate-level parameters, such as the offer
[Appendix-36]

arrival rate for employed workersλ1. These parameters are identified using the matched
employer-employee data described in Section2, which contain the relevant information on
worker flows (transitions in and out of non-employment and between employers).
The employer-level parameters{σVj,L j,f j,ρ j,δ j}j∈J and the transition parametersλ0
and λ1 are identified from (i) the realized mobility flows between employersMjk, and (ii)
which employers are shrinking or growing [seeSorkin, 2018, Section V.B]. The notationσVj
emphasizes that worker flows pin down the value of working at employerj up to the scale
of the idiosyncratic taste shocks.
The main source of identification for σVj is the aggregation of the realized mobility
flows Mjk. An estimate for Lj is obtained directly from the data as the share of worker-
year observations at employerj. fj is identified from the share of non-employment flows
to employerj. The separation shocksδj and ρj are identified from the separation flows at
shrinking firms, which give information on involuntary worker flows. Finally, the transition
parameters λ0 and λ1 are pinned down by accounting for the aggregate transition flows,
respectively from non-employment to employment and between employers.
Two sample restrictions are required for identification at this step. First, the aggregation
of mobility flows only identifiesVj within the strongly connected sets of employers.55 Second,
each employer must hire at least one worker from non-employment for its sampling weight
fj to be well-defined.
Given {σVj,L j,f j,ρ j,δ j}j∈J and the aggregate transition rateλ1, σuj can be recovered
directly from Equation (C.9), again up to the scale of the i.i.d. taste shocks. This calculation
is straightforward since, given that {σεi}i∈{J ,N } are i.i.d. draws from a Type 1 Extreme
Value distribution with scale one, all expectations in Equation (C.9) admit the following
closed-form solutions
σE

Vj +εj

=σVj +γ,
σE

max

Vj +εj,V k +εk
	
= ln

exp(σVj) + exp(σVk)

+γ,
(C.11)
where γ denotes Euler’s constant.56 This step further requires us to assume a value for the
discount factorβ, which we set in line with a 5% annual discount rate.
As in the original paper, the scale of the taste shocksσ is not separately identified, so
the model is identified up to scale. We setσ = 1.
55Within a strongly connected set of employers, each employer has at least one worker moving in and one
worker moving out. This condition is required for the fixed-point associated with the appropriately scaled
matrix of worker flows to exist. See, e.g., Jackson [2010] for details on social network definitions.
56Gyetvai et al. [2022] make a related point in the context of a continuous time random search model.
[Appendix-37]

Solution algorithm The model is solved using a fixed-point iteration algorithm. The
algorithm is described in Online Appendix G ofSorkin [2018].
C.3 Sample Selection
The model is estimated on the Norwegian matched employer-employee data described in
Section 2. We use establishments as the empirical counterpart to employers (“j”) in the
model. We follow the employer-employee fixed-effect literature and assign each individual
one main employer in each year by selecting the establishment with their largest annual
earnings. Our data feature the exact start date and end date of each employment spell
with an employer in each year, so we can make a precise distinction between employer-
to-employer moves and moves with a non-employment spell in-between. Moves between
two main employers that include an intervening spell with another employer also qualify as
employer-to-employer moves.57
We restrict the sample to the period 2021-2024 and retain workers aged 20 to 60 (inclu-
sive). We compute all measures for the same subset of employers, derived from the most
stringent identification restrictions inSorkin [2018]. Specifically, we restrict the sample to
the largest strongly connected set of establishments and impose that each of these establish-
ments hires at least one individual from non-employment.58 These last two restrictions are
interdependent, and they are imposed recursively until the set of establishments converges.
As shown in Table1, around a quarter of employers satisfy identification restrictions in
Sorkin [2018]. Since employment is concentrated at larger employers, this sample covers
the majority of workers (74% of unique workers) and job ads (68% of posted job ads). See
Appendix TableA.1 for additional descriptive statistics on workers and firms.
C.4 Clustering
To precisely estimate employer parameters, we reduce their number using ak-means clus-
tering algorithm as a pre-estimation step [Bonhomme et al., 2019], which partitions theJ
employers in each sample intoGgroups with similar observable characteristics, increasing the
number of movers per group and improving estimation precision. The algorithm requires two
inputs: (i) a vector of establishment-level variables on which to classify employers, and (ii) a
number of groupsG ≤J. Our clustering variables capture three characteristics of establish-
ments: wages (the empirical cumulative density function of wages evaluated at deciles of the
57We define employer-to-employer flows as consecutive employment spells with a gap of at most 31 days.
58Focusing on the largest connected set is common in the literature. See, among others, Card et al. [2013]
and Bonhomme et al. [2023] in the context of the two-sided unobserved heterogeneity regression model ( C.1)
and Sorkin [2018] and Morchio and Moser [2024] in the context of the utility-posting model.
[Appendix-38]

sample-wide wage distribution), worker flows (job creation and destruction rates, distinguish-
ing direct employer-to-employer transitions from transitions through non-employment), and
industry, occupation, and location composition.59 We setG = round(J/50) in our baseline to
balanceheterogeneityagainstprecision. Asaresult, ourbaselinemodelfeatures 1, 422unique
employer clusters. We provide robustness checks using smaller (G = round(J/25) = 2, 843)
and larger (G = round(J/100) = 711) clusters.
C.5 Correlations
TableC.1 shows the correlations between the five employer quality measures. Panel A is for
the baseline sample (2021-2024,G = round(J/50)). Panels B-D show the same correlations
for several alternative samples: 2015-2024 (Panel B), smaller clusters (Panel C), and larger
clusters (Panel D). Across samples, we find that the measures of employer quality are im-
perfectly correlated, with most correlation coeﬀicients falling in the 30–50% range. There is
stronger agreement between the flow-based measures. The correlation between the poaching
index and the measures derived from the utility-posting model are consistently above 80%.
Table C.1: Correlations between Employer Quality Measures.
Pay Premium Sorkin Overall Value Poaching Index Sorkin Flow Value Employment Size
Panel A. Baseline Sample
Pay Premium 1.000
Sorkin Overall Value 0.369 1.000
Poaching Index 0.434 0.876 1.000
Sorkin Flow Value 0.329 0.981 0.849 1.000
Employment Size 0.535 0.412 0.414 0.334 1.000
Panel B. 2015–2024
Pay Premium 1.000
Sorkin Overall Value 0.485 1.000
Poaching Index 0.531 0.898 1.000
Sorkin Flow Value 0.407 0.965 0.848 1.000
Employment Size 0.540 0.336 0.357 0.191 1.000
Panel C. Smaller Clusters:G = round(J/25)
Pay Premium 1.000
Sorkin Overall Value 0.334 1.000
Poaching Index 0.389 0.849 1.000
Sorkin Flow Value 0.291 0.976 0.817 1.000
Employment Size 0.504 0.372 0.378 0.285 1.000
Panel D. Larger Clusters:G = round(J/100)
Pay Premium 1.000
Sorkin Overall Value 0.394 1.000
Poaching Index 0.461 0.897 1.000
Sorkin Flow Value 0.348 0.985 0.874 1.000
Employment Size 0.568 0.437 0.438 0.364 1.000
Notes: This table shows the correlation coeﬀicients for the five employer quality measures described in
Appendix C. Panel A: 2021-2024, G = round(J/50). Panel B: 2015-2024, G = round(J/50). Panel C:
2021-2024, G = round(J/25). Panel D: 2021-2024, G = round(J/100). All correlations are weighted by
worker-years.
59For location, we cut the distribution of municipality employment into deciles and construct indicators for
the establishment’s municipality. For example, Oslo accounts for more than 10% of Norwegian employment,
so there is a specific indicator for establishments in Oslo.
[Appendix-39]

D Details on the Monopsony Model
D.1 Estimation Procedure
Step 1: Sample selection We restrict the sample to larger employers for which we
can credibly estimate employer-specific components implied by Equations (3)-(6). We use
establishments as the empirical counterpart to employers (“j”) in the model. Specifically,
we only retain establishments with at least 30 stayers and 15 movers over the period, where
stayers are workers observed at the same employer in the following period, and movers are
workers observed at a different employer. As we subsequently recover employer fixed effects
from a standard two-sided unobserved heterogeneity wage regression [Abowd et al., 1999],
we must restrict the sample to the largest connected set of employers, which is required for
identification. This restriction leaves us with 12,973 establishments. Additional details on
the composition of this sample can be found in Appendix TableA.1.
Step 2: Clustering We reduce the number of parameters to be estimated by grouping
employers paying similar wages. Specifically, we use ak-means clustering algorithm and
input the establishment-level empirical cumulative distribution function (CDF) of hourly
wages as the clustering variable [Bonhomme et al., 2019]. The establishment-level empirical
CDF is computed at the deciles of the distribution of hourly wages in the whole sample.
Establishments are weighted by their number of worker-year observations over the sample
period. We choose the number of employer clustersG with the formulaG = round(J/50),
where J is the number of establishments in the estimation sample.
Step 3: Pre-estimated parameters Some of the parameters in the monopsony model
are pre-estimated, as described in the main text. The labor supply elasticity (σ) is derived
from the central pass-through estimate for Norway reported inBhuller et al.[2025, Table
2], which implies bσ = 3.29. The WTP estimates bγk are taken from Column (4) of Table
5. Since the survey experiment is restricted to full-time job ads, we construct an estimated
WTP for part-time hours from recent evidence byDube et al.[2022] andLachowska et al.
[2025].60 These parameters are listed in Appendix TableD.1.
Step 4: Employer pay premiums We recover the employer fixed effects in a standard
two-sided unobserved heterogeneity wage regression with worker and employer effects. We
60We assign a WTP of -0.0785 for jobs that offer part-time hours, which is one minus the average WTP
estimate for jobs offering full-time hours reported in Dube et al. [2022] and Lachowska et al. [2025].
[Appendix-40]

Table D.1: Monopsony Model: Pre-Estimated Parameters.
Parameter Value
σ: Labor Supply Elasticity from the Literature 3.290
γk: Willingness-to-Pay from the Survey Experiment
Temporary Job -0.254
Convenient Hours 0.189
Inconvenient Hours -0.282
Insurance Scheme 0.105
Mortgage Possibility 0.117
Career Opportunities 0.085
Possibility for Remote Work 0.065
Good Colleagues 0.094
Inclusive Work-life Scheme 0.173
Company Gym or Sports Team 0.234
Company Cabin 0.272
γk: Willingness-to-Pay from the Literature
Part-time Contract -0.079
Notes: The table shows the pre-estimated parameters used in the model. The labor supply elasticity ( bσ) is
implied by the pass-through estimates in Bhuller et al. [2025, Column (4) of Table 2]. The willingness-to-pay
(WTP) parameters ( bγk) for the advertised non-pay attributes are taken from Table 5, Column (4), and
estimated using the survey experiment described in Section 4.3. The WTP for jobs with part-time contract
is one minus the average WTP for full-time hours reported in Dube et al. [2022] and Lachowska et al. [2025].
use the wage regression model in Equation (C.1). The estimated employer fixed effectsbψg(j)
are our estimates of employers’ pay premiumslnwj in Equation (3).
Step 5: Intrinsic amenity value The intrinsic amenity parametersln ˜aj are estimated
by maximum likelihood using Equation (4), conditional on the pre-estimated parameters
from Step 3 and the employer pay premiums from Step 4. Since the number of parameters
to be estimated is large, we rely on standard quasi-Newton methods for optimization.
D.2 Comparison of Utility Dispersion
Appendix TableD.2 compares the estimated dispersion of utility to the dispersion of log-
wages for several recent papers. We rely on the references discussed in Section 8.5 of the
[Appendix-41]

review paper by Mas [2025]. For each of the four studies considered in Appendix Table
D.2, we construct a relative dispersion statistic from the most directly comparable results.
Although the underlying studies differ across many dimensions—they all use different models
and data—we harmonize these results to make them comparable to our estimates. For
example, utility is in wage units in the model introduced byMorchio and Moser[2024], so
we report relative dispersion as the variance of log-utility over the variance of log-wages to
make it comparable to the other studies, where utility is in log-wage units.
Table D.2: Relative Dispersion of Utility in Selected Studies.
Source Reported dispersion statistic Value
Panel A. Published Studies
Taber and Vejlin[2020, Tables VI-VII] Var(Utility) / Var(Log-Wages) 0.234/0.104 = 2.250
Hall and Mueller[2018, Table 2] SD(Job Value) / SD(Offered Log-Wages) 0.38/0.24 = 1.583
Morchio and Moser[2024, Table 10] Var(Log-Utility) / Var(Log-Wages) [men,women] [0.044, 0.036]
Maestas et al.[2023, Table 5] IDR(Log-Compensation) / IDR(Log-Wages) 1.769/1.664 = 1.063
Panel B. Model Estimates
— Var(uj) / Var(lnwj) 2.200
— SD(uj) / SD(lnwj) 1.483
— IDR(uj) / IDR(lnwj) 1.914
Notes: This table compares the relative dispersion of workers’ indirect utility ( uj in our framework) derived
from working at employer j relative to the dispersion of employer log-wages ( ln wj in our framework) in the
selected studies listed in the first column. We include the studies discussed in the review paper by Mas [2025,
Section 8.5]. For each study, we construct one relative dispersion statistic from the most relevant reported
results. “Var”: Variance. “SD”: standard deviation. “IDR”: inter-decile range.
We find that our estimates broadly align with the numbers reported inTaber and Vejlin
[2020] (variance ratio: 2.200 vs 2.250) andHall and Mueller[2018] (standard deviation ratio:
1.483 vs 1.583). Our estimates also imply a larger inter-decile range ratio than that reported
in Maestas et al.[2023] (1.914 vs 1.063), possibly because their analysis is restricted to a
subset of non-pay amenities related to working conditions. Finally, the model developed in
Morchio and Moser[2024] implies a much smaller variance ratio than ours (0.040 vs 2.250),
most likely because of differences in the model environment.
We see two main takeaways from the comparison of utility dispersion estimates in Table
D.2. First, we provide a range of published estimates for this summary statistic, suggesting
that both modeling choices and data sources matter. Second, we confirm that the relative
dispersion of employer utility implied by our estimates is reasonable within that range.
[Appendix-42]

D.3 Distributions in Counterfactual Scenarios
We complement the summary statistics on the distribution of employer pay, employer util-
ity, and employment size in each scenario by showing kernel density estimates in Figure
D.1. Panel (a) shows the distribution of employer pay premiums in each scenario, weighted
by employment. Panel (b) shows the distribution of employer utility differentials in each
scenario, also weighted by employment. Panel (c) shows the distribution of employment size
across employers in each scenario. This last figure is constructed under the assumption that
the number of employers is constant in each scenario (i.e., no entry or exit).
Figure D.1: Relative Contribution of Job Attributes in Counterfactual Scenarios.
(a) Employer Pay Premiums: ln wj
(b) Employer Utility Differentials: uj
 (c) Employment Size
Notes: This figure shows kernel density estimates for the distribution of the employer pay premiums (panel
a), the employer utility differentials (panel b), and the employment size across employers (panel c) in the
baseline and each counterfactual scenario. Panels ( a) and ( b) are weighted by employment size. The density
estimates in Panel ( c) are constructed by computing average employer size in each cluster, taking logs, and
weighting each cluster by the corresponding number of establishments. The blue lines show the baseline
distributions. The red lines shows the counterfactual distributions when the advertised amenities are turned
off ( Aj = 0 , “advertised off”), while the green lines reflect the scenario when intrinsic amenities are turned
off ( ln ˜aj = 0, “intrinsic off”), and the orange lines reflect the scenario when all amenities are turned off.
[Appendix-43]

E Predictive Power of Publicly Posted Job Attributes
Which job attributes are most predictive of employer quality? In Section4.1, we decompose
the overallR2 by adding groups of attributes, which abstracts away from the 47individual
attributes. This Appendix focuses on the predictive power of individual attributes directly.
Table E.1: Lasso Regressions – The Most Predictive Publicly Advertised Job Attributes.
Pay Premium Overall Sorkin Value Flow Sorkin Value Poaching Index Employment Size
(1) (2) (3) (4) (5)
Panel A: Lasso Attributes 1-5
– Full-time Contract – Pension Scheme – Part-time Contract – Collective Agreement Pay – Collective Agreement Pay
– Part-time Contract – On-the-Job Training – Pension Scheme – Pension Scheme – On-the-Job Training
– Shift Work – Full-time Contract – Possibility to Work Flexible Hours – On-the-Job Training – Full-time Contract
– Temporary Job – Permanent Job – Social Environment – Full-time Contract – Challenging Tasks
– Challenging Tasks – Social Environment – Good Colleagues – Social Environment – Central Location
Panel B: Lasso Attributes 6-10
– Any Other Mention of Pay – Collective Agreement Pay – Challenging Tasks – Compensation Level – Shift Work
– Pension Scheme – Part-time Contract – Compensation Level – Insurance Scheme – Weekend/Evening/Night Work
– Insurance Scheme – Possibility to Work Flexible Hours – On-the-Job Training – Part-time Contract – Permanent Job
– Good Colleagues – Shift Work – Work Involves Travelling – Weekend/Evening/Night Work – Company Gym or Sports Team
– Central Location – Weekend/Evening/Night Work – Company Vehicle – Permanent Job – Any Welfare Scheme
Panel C: Lasso Attributes 11-15
– Compensation Level – Good Colleagues – Any Welfare Scheme – Good Colleagues – Compensation Level
– Company Gym or Sports Team – Challenging Tasks – Collective Agreement Pay – Challenging Tasks – Any Other Mention of Pay
– Company Vehicle – Compensation Level – Incentive Pay Scheme – Involves Leadership Responsibility – Insurance Scheme
– Any Welfare Scheme – Competitive Pay – Any Other Mention of Pay – Work Involves Traveling – Temporary Job
– Company Cabin – Incentive Pay Scheme – Shift Work – Central Location – Company Vehicle
Notes: This table shows the variables included in Lasso regressions with penalty parameter set so that the
model includes 5, 10, or 15 attributes. Columns (1)-(5) show the first variables selected for each revealed-
preference employer quality measure. All regressions include a constant term and other ad characteristics
without penalization, including the number of words, the total number of attributes, an indicator for online
publication, and an indicator for whether the establishment name was disclosed. As in Section 4.1, we
define Ak g(j) is the share of ads from employers in cluster g featuring attribute k. The sample corresponds
to “Employer Quality Sample” in Table 1.
We use the Least Absolute Shrinkage and Selection Operator (Lasso) to select subsets of
individual attributes for each employer quality measure. Lasso minimizes residual squared
error with an additional penalty on the absolute value of coeﬀicients.61 For each measure,
we start with a penalty high enough to exclude all attributes and reduce it until the Lasso
retains 5, 10, or 15 attributes.62 Rather than emphasizing the exact order of entry, which
61Specifically, Lasso minimizes
X
g
(
bQg(j) − X
k
n
βkAk g(j)
o)2
+ ϕ
X
k
|βk|,
where the first term is the sum of squared errors and the second is the penalty over K penalized parameters.
The penalty parameter ϕ determines the number of excluded regressors (i.e., variables k with βk = 0).
62All regressions include a constant and additional ad characteristics (number of words, total number of at-
tributes, an indicator for online posting, and an indicator for employer name disclosure) without penalization,
so the selection criteria reflect variation in advertised job attributes rather than general ad characteristics.
[Appendix-44]

may be sensitive when attributes are correlated, we report the sets of attributes selected at
each threshold. This provides a parsimonious summary of the attributes with the strongest
predictive power for each employer quality measure.
Appendix TableE.1 reports the attributes selected by Lasso for various thresholds. At-
tributes related to hours of work are important predictors for all quality measures, as found
in Section4.1. For the pay premium (Column 1), the five most predictive attributes relate to
hours of work, inconvenient schedules, contract duration, and tasks. For the broader quality
measures (Columns 2-4), pension scheme, hours of work, contract duration, convenient or
inconvenient hours, collective agreement pay, and social environment are consistently among
the most predictive. For employment size (Column 5), collective agreement pay, on-the-job
training, and central location are highly predictive. Overall, the attributes flagged as salient
in Section4.1 remain highly predictive when we focus on individual attributes directly.
[Appendix-45]
