---
title: 'Beyond Citations: Comparing Scholarly, Policy, and Patent Impact Across the FT50 Journals'
url: https://arxiv.org/abs/2606.17610
category: digital-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Arash Hajikhani
- Yi Zhang
- Mengjia Wu
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.17610
pages: 28
chars: 60168
fetched_at: '2026-11-08T13:05:53+00:00'
kb_version: 1
---

# Beyond Citations: Comparing Scholarly, Policy, and Patent Impact Across the FT50 Journals

Beyond Citations: Comparing Scholarly, Policy, and
Patent Impact Across the FT50 Journals
Arash Hajikhani1,2,* Yi Zhang3 Mengjia Wu3
1VTT Technical Research Centre of Finland Ltd, Espoo, Finland
2LUT University, Lappeenranta, Finland
3University of Technology Sydney, Sydney, NSW, Australia
*Corresponding author:arash.hajikhani@vtt.fiORCID: 0000-0003-2032-9180
Abstract
The Financial Times 50 (FT50) journal list shapes hiring, promotion, accreditation, and
research evaluation across business schools worldwide. Yet journals on the list are typically
treated as if they represent a homogeneous tier of excellence. We test this assumption by
comparing 53 FT50 and recently removed journals across three distinct impact channels:
scholarly influence (field-weighted citations and visibility), policy uptake, and technological
reach through patent citations. Using a panel of more than 60,000 publications from
2005–2019, we find striking heterogeneity hidden beneath the binary FT50 label. Elite
economics journals dominate policy influence, information systems and marketing journals
lead technological impact, while many highly cited management journals exhibit limited
reach beyond academia. Citation, policy, and patent indicators behave as largely independent
dimensions of impact, with a citation-only ranking correlating only moderately with a
multidimensional ranking. Nearly half of all journals change quartile once policy and
patent indicators are incorporated, demonstrating that assessments based solely on scholarly
citations overlook important dimensions of research influence. While the FT50 remains
widely used as a binary classification of journal quality, our results reveal a substantial
1
arXiv:2606.17610v1  [cs.DL]  16 Jun 2026

within-list impact spectrum and show that journal rankings are highly sensitive to how
impact is defined and measured.
Keywords:FT50; journal evaluation; policy citations; patent citations; field-weighted citation
impact
1 Introduction
The Financial Times 50 list (FT50) is used by deans, accreditation bodies, and tenure committees
as a shorthand for journal quality in business and management research. Its constitution and
effects have been argued over for two decades. The list was last substantially revised in 2016
and has now, in 2026, been adjusted again with three titles removed and three added (Financial
Times, 2026). The literature accumulated around the list raises three questions that motivate
the present analysis. The first concerns selection: does the FT50 identify the journals where the
most consequential research is published, and would alternative bibliometric selections produce
a different ordering (Fassin, 2021; Vidgen et al., 2019; Mingers and Yang, 2017). The second
concerns the metric ecology in which FT50 evaluations are made: citation-based indicators
have been shown to be vulnerable to volume-driven dilution (Zhang, 2021) and to the broader
publication-volume strain documented across academic publishing (Hanson et al., 2024), to
Goodhart-style decay as citation counts have become targets (Fire and Guestrin, 2019), and to
outright manipulation through paper mills and citation-purchasing services (Ibrahim et al., 2025;
Meho, 2025). The third concerns rigour and relevance: critics argue that the kind of scholarship
the list rewards has drifted away from the audiences outside academia that business-school
research is supposed to serve (Steingard et al., 2026; Jack and Dalal, 2024), an argument that
becomes harder to evaluate as long as the available evidence is restricted to a single, citation-
based dimension of impact.
The most useful empirical question to bring to this debate is comparative. If the FT50
certifies a homogeneous tier of high-quality outlets, then on properly normalized per-publication
indicators of citation impact, policy reach, and patent reach the journals on the list should look
similar; if the list bundles incommensurable kinds of scholarship, the indicators will spread
2

apart. Existing FT50-focused analyses tend to treat impact as a single number (Zhang, 2021;
Fassin, 2021) or to focus on one disciplinary slice of the list (Vidgen et al., 2019), and rarely
include policy or patent reach. The comparison is provided here on a single panel of all 53
journals currently on or recently removed from the list, using all three channels in parallel, and
the resulting comparison is tested against a sensitivity analysis over alternative publication-year
windows.
The contribution is descriptive. The aim is not to settle whether the FT50 selects the right
journals, but to characterize the within-list quality spectrum on per-publication terms, to identify
which journals sit at the top of that spectrum on multiple channels and which sit consistently at
the bottom, to test whether the identification is stable across publication-year windows, and to
read the 2026 list update against the resulting picture. The motivating question is the one a user
of any journal list ought to be able to ask: given two journals on the FT50, which has the larger
per-paper reach, and on which kind of impact?
2 Data and methods
2.1 Data sources
Three coupled data sources are used. The bibliographic backbone is Scopus, accessed through
the Elsevier APIs that also underlie SciVal. Baas et al. (2020) document Scopus as a curated
bibliometric source, and Visser et al. (2021) compare it with Web of Science, Dimensions,
Crossref, and Microsoft Academic; for the social and management sciences that fill the FT50,
Scopus is the most complete option for both coverage and citation linking. The indicators built
on top of Scopus are computed in SciVal, and the SciVal indicator definitions are followed
throughout (Elsevier B.V ., 2019a,b).1 The patent-citation stream in SciVal draws on the five
largest patent offices: the European Patent Office, the United States Patent and Trademark
Office, the United Kingdom Intellectual Property Office, the Japan Patent Office, and the
World Intellectual Property Organization. Patent visibility is constrained by an eighteen-month
1The two SciVal guidebooks (Elsevier B.V ., 2019a,b) and the 2026 FT list announcement (Financial Times, 2026)
are cited here as documentary references — vendor methodology documentation and a public list announcement,
respectively — rather than as peer-reviewed sources.
3

publication lag and a multi-year examination window, so the patent indicators are most reliable
for papers published more than three years before the extract date (Elsevier B.V ., 2019b). Public-
policy citations are sourced via Overton, described in detail by Szomszor and Adie (2022), with
the strengths and limitations of Overton for research-impact evaluation discussed by Cristofoletti
et al. (2025). Overton has a coverage skew toward English-language and Anglo-American policy
producers, and the policy series is treated cautiously throughout.
2.2 Indicators
Seven per-publication indicators are used; they are directly comparable across journals once
volume and field are accounted for. Three measure citation-based scholarly impact. The Field-
Weighted Citation Impact (FWCI) is the ratio of citations received by a publication to the world
average for similar publications, controlling for subject field, year of publication, and document
type (Elsevier B.V ., 2019a; Larivière and Sugimoto, 2019); a value of 1.0 corresponds to the
world average. The Top-10% rate is the share of a journal’s papers in the global top decile by
FWCI within their field-year-document-type cell, computed as Output-in-Top-10% divided by
Scholarly Output. The Field-Weighted Views Impact is the same normalization applied to usage
rather than citations. Two measure public-policy reach: policy citations per published paper
(Citing Policy Documents divided by Scholarly Output) and the share of papers ever cited by
at least one policy document (Scholarly Output cited by Policies divided by Scholarly Output).
Two measure industry reach: patent citations per published paper (Patent Citations divided by
Scholarly Output) and the share of papers ever cited by at least one patent (Scholarly Output
cited by Patents divided by Scholarly Output).
Normalizing every count by Scholarly Output is required by the same logic that motivates
FWCI. Aggregate counts of citations, policy mentions, or patent links are mechanical functions
of how many papers a journal has published and how long those papers have had to accumulate
citations. A journal that publishes 1,000 papers per year will accumulate more aggregate citations
than one that publishes 50, regardless of per-paper impact. To compare journals, the relevant
quantity is the rate per published paper. SciVal already applies this adjustment natively in the
patent channel by reporting Patent Citations per Scholarly Output as a denominator-adjusted
4

indicator (Elsevier B.V ., 2019b); the same logic is applied here to the policy channel and to the
share of papers reaching either channel.
2.3 Sample and time window
All 53 journals tagged FT50 in SciVal as of April 2026 are included. The panel is the union of the
pre-2026 FT50 (the 50 journals on the list before the most recent update) and the three additions in
2026 (Academy of Management Annals,American Sociological Review,Psychological Science),
with the three removed journals (Human Relations,Journal of Business Ethics,Organization
Studies) still present in the panel. Keeping the removed journals in the panel makes the 2026
swap directly observable in the comparative analysis. Three of the listed journals (Academy
of Management Annals,Strategic Entrepreneurship Journal,Review of Finance) were founded
mid-window; they are kept in the panel and earlier years are left missing.
The headline analysis uses publication years 2005–2019. The lower edge is set by the
Overton policy database. Szomszor and Adie (2022) document indexed-document growth and
citation accrual back to 2000–2005, and 2005 is used here as the earliest year for which per-paper
policy reach is reasonably comparable across cohorts; pre-2005 measurements would understate
per-paper policy reach simply because the policy documents that would have cited those earlier
papers are not all in the database.
The upper edge is set by accrual time, and three separate constraints push it down to 2019
even though the SciVal panel itself runs to 2026. The first is citation accrual. The per-publication
citation indicators (Citations per Publication, FWCI, Top-10% rate, Field-Weighted Views
Impact) all need post-publication time for citations and views to accumulate. SciVal’s FWCI
uses a four-year accrual window, so a paper from 2022 has its FWCI computed on citations
received through 2025, which is in principle workable but puts late-window cohorts on a noisier
footing than earlier cohorts. The Top-10% rate is a cumulative-since-publication metric and is
more sensitive still: a 2024 paper has had two years to enter the global top decile, while a 2010
paper has had sixteen. The standard scientometric convention, discussed at length in Larivière
and Sugimoto (2019) in the context of citation-window length, is to allow at least five years of
post-publication accrual when comparing journals on citation-based per-paper rates. Stopping at
5

2019 gives every paper in the panel between five and twenty years of accrual through the April
2026 extract.
The second constraint is the patent channel, which is tighter than the citation channel. Patents
have an eighteen-month publication lag from filing, plus a three- to five-year examination process
for grant, plus the time it takes for a granted patent to surface in patent-to-paper citation indexing.
The Elsevier Patent Metrics Guidebook (Elsevier B.V ., 2019b) notes that patent metrics are most
reliable for publication years that predate extraction by at least three years, which for an April
2026 extract means a cutoff at 2022 or earlier. In practice, papers published in 2023, 2024, or
2025 have had little or no exposure to the granted patents that would cite them, regardless of the
underlying research. Including those years would push the late-cohort patent rates toward zero
mechanically, distorting one of the three channels under measurement.
The third constraint is the policy channel on the right-hand side. Policy uptake of academic
research typically lags by several years: a paper has to be published, become known, then be
cited in a government report, working paper, or NGO brief that itself has to be indexed by
Overton. Cristofoletti et al. (2025) discuss right-censoring of recent policy citations as a known
feature of the database. For papers from 2024 or later, Overton has had little time to index the
policy documents that would cite them.
Cutting at 2019 gives the panel a window that is reliable on all three channels at once. The
15-year span covers 60,705 papers across the 53 journals (median 868 papers per journal, range
170 to 5,170), enough for the per-publication ratios to stabilize even for journals with small
annual output. The choice of upper edge is itself a parameter, and it is tested directly: every
per-journal indicator is replicated under the three alternative windows 2005–2014, 2010–2019,
and 2015–2019, and Kendall τ is reported between the rankings produced under each pair of
windows. The 2015–2019 replication sits closest to the right-censored zone and is the most
exposed to recency noise, so any drop in stability there gives a measurable bound on how much
the upper edge is doing the work.
6

2.4 Sub-discipline grouping
For interpretation the 53 journals are grouped into eleven sub-disciplines, following each journal’s
primary subject area in the All Science Journal Classification used by Scopus to compute FWCI
(Baas et al., 2020), supplemented by the journal-by-journal subfield assignments documented for
FT50 journals by Fassin (2021) and the Information Systems clustering used by Vidgen et al.
(2019). The full mapping with sources is given in Appendix A. The grouping is heuristic at the
boundaries; the channel-share results are stable under several plausible reassignments.
2.5 Why a comparative cross-journal analysis is the right framing
A natural alternative would be to study how impact at the FT50 has changed over time. That
framing was tried first and is reported briefly: the median FWCI across the list declines over
the 2005–2023 window, from approximately 3.45 in 2005 to 2.04 in 2020 (Section 5). Because
citations, policy mentions, and patent links all accumulate over time, much of this aggregate
decline is mechanical: papers published in 2005 have had more time to be discovered than papers
published in 2020. Even FWCI, despite its four-year normalization window, is sensitive to the
time-window choices that set the world baseline. The longitudinal trend is therefore mostly
informative about citation accrual, not about the relative quality of journals on the list. The
substantive question, namely which journals sit at the top of the quality spectrum and which sit
at the bottom, is sharpest when journals are compared to each other under the same window and
after per-publication normalization. That is the framing of the rest of the paper.
2.6 Composite ranking and quality map
For each journal in each window, performance is ranked on each of the seven indicators (1
= best within the FT50, 53 = worst). The composite rank is the mean of the within-FT50
ranks across the seven indicators, then re-ranked. Within-FT50 quartiles of the composite are
used for tier interpretation. To complement the rank-based composite with a magnitude-aware
visualization, each indicator is also z-scored across the 53 journals and averaged within channel
(citation indicators in one composite, policy and patent indicators in another); each journal is then
7

placed on a two-dimensional plane defined by the citation z-composite (x-axis) and the societal
z-composite (y-axis). This visualization is referred to as the FT50 quality map throughout the
paper.
3 Results
3.1 Per-publication impact varies by orders of magnitude across the FT50
Even after per-publication normalization, the journals on the list span very large ranges on every
channel. In the 2005–2019 window, theQuarterly Journal of Economicsrecords 88.3 policy
citations per published paper whileContemporary Accounting Researchrecords 0.36, a span of
roughly 250-fold. On patent citations per paper,MIS Quarterlyrecords 0.116 and theAcademy
of Management Reviewrecords essentially zero. On FWCI the span is narrower but still wide:
Academy of Management Annalsat approximately 8.4,Operations Researchat approximately
1.16, a factor of seven. On the share of papers ever reaching policy, the elite economics journals
lead (American Economic Reviewat 90%,Quarterly Journal of Economicsat 98%); practitioner
outlets and several accounting and management journals trail at single-digit percentages. These
ranges hold across all three replication windows.
The map in Figure 1 plots each journal in (per-publication policy reach, per-publication
patent reach) space, with bubble size proportional to mean FWCI in the window. The picture is
a three-region structure. The lower-right quadrant is the policy channel, occupied by the elite
economics journals (Quarterly Journal of Economics,Journal of Political Economy,American
Economic Review,Econometrica), theJournal of Finance, and a handful of journals that achieve
genuine policy reach despite different home disciplines (American Sociological Review,Research
Policy). The upper-left quadrant is the patent channel, occupied by the IS journals (MIS Quarterly,
Information Systems Research), the marketing science journals (Marketing Science,Journal of
Marketing,Journal of Marketing Research), the practitioner outlets (Harvard Business Review,
MIT Sloan Management Review), and a small set of operations research journals. The lower-left
corner contains journals whose per-paper reach is low on both societal channels: a sizeable share
of the management, accounting, and organizational-behaviour outlets. The upper-right corner is
8

empty. No FT50 journal achieves both high per-paper policy reach and high per-paper patent
reach.
10 1
 100 101 102
Policy citations per published paper (log scale; +0.01)
10 3
10 2
10 1
Patent citations per published paper (log scale; +0.0005)
American Economic Review
Quarterly J. Economics
J. Political Economy
Econometrica
J. Finance
Research Policy
Management Science
Operations Research
Marketing Science
J. Marketing
Harvard Business Review MIS Quarterly
Information Systems Research
AoM Review
AoM Annals
Administrative Science Quarterly
Psychological Science
American Sociological Review
Contemporary Accounting Research
MIT Sloan Management Review
Per-publication policy vs.\ patent reach, 2005 2019
(bubble size proportional to mean FWCI in window)
Sub-discipline
Economics
Finance
Accounting
Management
Marketing
OR / Operations
Information Systems
Psychology / OB
Sociology
Practitioner
Innovation Studies
Figure 1: Per-publication policy reach (x-axis, log) versus per-publication patent reach (y-
axis, log) for the 53 FT50 journals in the 2005–2019 publication-year window. Bubble size is
proportional to mean FWCI in the window; colour indicates sub-discipline. The three populated
regions correspond to the policy channel (lower right), the patent channel (upper left), and a
low-reach corner (lower left).
3.2 The FT50 quality map: where each journal sits on a single 2D plane
Figure 2 places every FT50 journal on a single quality map. The horizontal axis is the journal’s
average z-score on the three citation-impact indicators (FWCI, Top-10% rate, Field-Weighted
Views Impact). The vertical axis is the average z-score on the four societal-impact indicators
(policy citations per pub, share reaching policy, patent citations per pub, share reaching patents).
Both axes are standardized across the 53 FT50 journals, so a value of 0 is the FT50 average;
positive means above average, negative means below average. Bubble size is proportional to
the overall z-score across all seven indicators, so the larger the bubble the higher the journal’s
all-channel quality.
The four quadrants of the map carry distinct meanings. Q1 (upper right, n = 9) contains
9

2
 1
 0 1 2
Citation impact composite
(mean z-score of FWCI, T op-10% rate, FW Views Impact)
1.0
0.5
0.0
0.5
1.0
1.5
2.0
Societal impact composite
(mean z-score of policy/pub, %-reach-policy, patent/pub, %-reach-patents)
FT50 quality map, 2005-2019: where each journal sits on citation impact vs. societal reach
(bubble size proportional to overall composite z-score across all seven indicators)
Sub-discipline
Economics
Finance
Accounting
Management
Marketing
OR / Operations
Information Systems
Psychology / OB
Sociology
Practitioner
Innovation Studies
Q1 - high citation
+ high societal reach
Q2 - strong societal reach,
below-avg citation impact
Q3 - strong citation impact,
below-avg societal reach
Q4 - below-avg on both
channels (low spectrum)
Figure 2: FT50 quality map, 2005–2019. Horizontal axis: citation-impact composite (mean
z-score of FWCI, Top-10% rate, FW Views Impact). Vertical axis: societal-impact composite
(mean z-score of policy citations per pub, share reaching policy, patent citations per pub, share
reaching patents). Bubble size is proportional to the overall z-score across all seven indicators.
Colour indicates sub-discipline. Quadrant lines fall at zero on each axis.
journals above the FT50 average on both citation impact and societal reach: theQuarterly
Journal of Economicsis the standout (cit z = +1.07, soc z = +1.88), followed byMIS Quarterly,
Journal of Marketing,Journal of Finance,Journal of Political Economy,American Sociological
Review,Information Systems Research,Journal of Financial Economics, andResearch Policy.
These nine sit at the top of the spectrum across every channel. Q2 (upper left, n = 11) contains
journals strong on societal reach but below the within-FT50 citation average. TheAmerican
Economic Review,Econometrica, andReview of Economic Studiesall sit here, not because their
citation impact is low in absolute terms but because the FT50 is a list of high-citation journals
to begin with: a journal can rank in the world’s top decile of business research and still fall
below the FT50’s internal average. Q3 (lower right, n = 15) is the citation-prestige cluster, with
Academy of Management Annalsas the rightmost outlier (cit z = +2.19) and the rest of the
10

cluster dominated by management journals with strong field-normalized citation impact and
weak external reach. Q4 (lower left, n = 18) contains journals below the FT50 average on both
channels.
3.3 The quality spectrum: a stable identification of top and bottom tiers
Translating the map into a single ordering, each journal is ranked on each of the seven indicators
and the mean rank is taken as a composite score (Section 2.2). The ordering, presented as a
heatmap of within-FT50 ranks, is shown in Figure 3.
The top quartile of the FT50 contains thirteen journals:Quarterly Journal of Economics
(composite rank 1),Journal of Finance,MIS Quarterly,Journal of Marketing,Journal of Business
Venturing,Journal of Financial Economics,Administrative Science Quarterly,Research Policy,
American Sociological ReviewandJournal of Operations Management(tied at 9),Academy of
Management Journal,Academy of Management Review, andEconometrica. No journal in this
group leads on every channel; what unites the thirteen is that each sits in the upper half of the list
on at least four of the seven indicators. They span seven of the eleven sub-disciplines: economics,
finance, information systems, management, marketing, sociology, and innovation studies. Two of
the three 2026 additions (Academy of Management AnnalsandAmerican Sociological Review)
sit in the top half of the list, and the third (Psychological Science) in the third quartile.
The bottom quartile contains thirteen journals:Manufacturing and Service Operations
Management,Accounting Review,Organizational Behavior and Human Decision Processes,
Journal of Business Ethics,Production and Operations Management,Operations Research,
Human Relations,MIT Sloan Management Review,Journal of Consumer Psychology,Human
Resource Management,Review of Accounting Studies,Organization Studies, andContemporary
Accounting Research. Each sits in the lower half of the list on at least four of the seven indicators.
The composition leans heavily on accounting (five of the six FT50 accounting journals are here),
on operations (three of the five operations journals), and on the practitionerSloan Management
Review. All three of the 2026-removed journals (Organization Studies,Human Relations,Journal
of Business Ethics) are in this bottom quartile.
The contrast between the top and bottom quartiles is large in absolute as well as ordinal
11

FWCI
T op-10% rate
FW Views ImpactPolicy cit. per pubShare reach. policyPatent cit. per pubShare reach. patents
Quarterly Journal of Economics  [Econ]
Journal of Finance  [Fin]
MIS Quarterly: Management Information Systems  [IS]
Journal of Marketing  [Mkt]
Journal of Business Venturing  [Mgmt]
Journal of Financial Economics  [Fin]
Administrative Science Quarterly  [Mgmt]
Research Policy  [Innov]
American Sociological Review  [Soc]
Journal of Operations Management  [OR/Ops]
Academy of Management Journal  [Mgmt]
Academy of Management Review  [Mgmt]
Econometrica  [Econ]
Journal of Political Economy  [Econ]
Review of Economic Studies  [Econ]
Information Systems Research  [IS]
Journal of Accounting and Economics  [Acct]
Academy of Management Annals  [Mgmt]
Review of Financial Studies  [Fin]
Journal of International Business Studies  [Mgmt]
Strategic Management Journal  [Mgmt]
Journal of Management  [Mgmt]
Journal of Marketing Research  [Mkt]
American Economic Review  [Econ]
Journal of Accounting Research  [Acct]
Organization Science  [Mgmt]
Journal of the Academy of Marketing Science  [Mkt]
Entrepreneurship Theory and Practice  [Mgmt]
Journal of Applied Psychology  [Psych/OB]
Management Science  [OR/Ops]
Harvard Business Review  [Pract]
Journal of Management Information Systems  [IS]
Journal of Consumer Research  [Mkt]
Psychological Science  [Psych/OB]
Marketing Science  [Mkt]
Journal of Management Studies  [Mgmt]
Journal of Financial and Quantitative Analysis  [Fin]
Review of Finance  [Fin]
Strategic Entrepreneurship Journal  [Mgmt]
Accounting, Organizations and Society  [Acct]
Manufacturing and Service Operations Managemen  [OR/Ops]
Accounting Review  [Acct]
Organizational Behavior and Human Decision Pro  [Psych/OB]
Journal of Business Ethics  [Mgmt]
Operations Research  [OR/Ops]
Production and Operations Management  [OR/Ops]
Human Relations  [Mgmt]
MIT Sloan Management Review  [Pract]
Journal of Consumer Psychology  [Mkt]
Human Resource Management  [Mgmt]
Review of Accounting Studies  [Acct]
Organization Studies  [Mgmt]
Contemporary Accounting Research  [Acct]
4 4 29 1 1 20 13
14 11 21 6 2 14 15
5 10 3 33 32 5 5
10 8 19 31 37 3 4
8 5 5 14 11 37 39
20 18 24 8 6 29 21
13 9 15 11 16 34 29
23 20 13 10 9 25 28
6 6 27 7 10 35 40
11 13 1 40 35 15 16
3 2 25 20 21 30 34
1 3 7 15 25 45 43
24 22 45 3 8 19 20
19 17 38 2 4 26 38
29 31 51 4 3 10 17
21 23 10 37 43 12 7
25 26 12 18 14 36 22
2 1 4 48 28 39 35
27 25 36 9 7 28 30
12 7 9 17 15 53 53
17 16 17 19 17 40 41
7 12 2 27 23 50 50
30 29 39 28 33 6 6
28 30 50 5 5 23 31
38 39 16 22 18 18 27
22 21 35 21 24 31 26
15 24 18 41 47 17 18
9 14 11 30 22 48 48
35 28 28 23 19 27 23
41 44 49 16 20 9 9
16 41 6 53 53 8 12
32 37 20 39 46 7 8
26 19 30 32 42 22 19
31 27 41 29 39 13 11
43 43 43 35 36 4 1
18 15 26 24 26 49 49
48 46 48 13 13 32 33
50 50 53 12 12 24 32
34 33 23 43 27 41 36
33 32 14 42 44 38 37
52 51 32 51 51 1 3
35 38 22 38 29 43 42
44 42 44 25 34 33 25
37 34 8 47 38 44 45
53 53 52 49 49 2 2
46 47 46 50 50 11 10
40 35 31 26 30 51 51
42 48 40 52 52 16 14
51 52 42 45 48 21 24
49 49 37 34 31 42 44
45 40 34 44 40 46 46
39 36 47 36 41 52 52
47 45 33 46 45 47 47
TOP
QUARTILE2nd3rdBOTTOM QUARTILE
Quality spectrum across the FT50, 2005-2019
rows ordered by composite rank across the seven indicators
10
20
30
40
50
Within-FT50 rank (lower = better)
Figure 3: Within-FT50 rank of each journal on each of the seven per-publication indicators in
the 2005–2019 window. Rows are sorted by composite rank. Cell colour and number indicate
the journal’s rank from 1 (best, dark green) to 53 (worst, dark red). Horizontal lines mark the
boundaries between within-FT50 quartiles.
12

terms (Figure 4). The multiplicative gap is largest on the policy channel: the top-quartile mean is
roughly nineteen times the bottom-quartile mean on policy citations per pub. On FWCI, Top-10%
rate, and share-reaching-policy, the gap is roughly 2.5-fold. On patent reach the gap is smaller
(between 1.5 and 2-fold), reflecting the broader cross-disciplinary distribution of industry uptake.
FWCI
T op-10% rate
FW Views Impact Policy cit. per pub
Share reaching policyPatent cit. per pub Share reaching patents
0.0
0.2
0.4
0.6
0.8
1.0
Mean indicator value
(normalized to within-FT50 maximum)
x2.6
x2.6
x1.5
x22.9
x2.6
x1.1 x1.0
Profile of top-quartile vs. bottom-quartile FT50 journals (2005-2019)
T op quartile (n=13)
Bottom quartile (n=13)
Figure 4: Mean indicator value of the top and bottom within-FT50 quartiles, normalized to the
within-FT50 maximum, with the multiplicative ratio between top and bottom annotated above
each pair. The largest gap is on policy citations per published paper.
3.4 The identification is stable across publication-year windows
The composite ranking might depend on the specific 2005–2019 window. To check this, the
per-journal indicator computation is replicated under three alternative windows (2005–2014,
2010–2019, and 2015–2019) and journals are ranked on each indicator in each window separately.
Figure 5 plots each journal’s composite rank in the earliest and latest replication windows. Points
cluster tightly along the diagonal: most journals occupy almost the same position in 2005–2014
as in 2015–2019.
The Kendall τ between the headline ranking and each of the three sensitivity windows is 0.89
(versus 2005–2014), 0.86 (versus 2010–2019), and 0.78 (versus 2015–2019). The τ between the
most distant pair of sensitivity windows is 0.69 (2005–2014 versus 2015–2019). All four values
13

are at levels read in the scientometrics literature as substantial agreement. Per-indicator stability
(Figure 6) is highest for the policy measures, with τ above 0.91 against any sensitivity window.
FWCI, the Top-10% rate, and Field-Weighted Views Impact sit in the middle, withτ between
0.74 and 0.91. The patent indicators are the noisiest, with τ between 0.68 and 0.87, because
patent reach is the sparsest signal in the panel. Within these bounds the tier assignment is stable:
of the thirteen journals in the bottom quartile of the 2005–2019 ranking, eleven or more are also
in the bottom quartile of every sensitivity window, and the corresponding numbers for the top
quartile are at least eleven of thirteen.
The journals whose ranks move most across windows are themselves informative.Journal of
Accounting Researchmoves twelve ranks between the earliest and latest sensitivity windows;
Journal of Political Economymoves ten;Organization Sciencemoves nine. These movements
do not weaken the comparison framework. They show that some journals are genuinely shifting
their indicator profile over the past two decades, and a longitudinal extension that models
within-journal change is a natural follow-up.
3.5 Channel orthogonality holds at the per-publication level
The cross-journal comparison demonstrates that citation, policy, and patent reach behave as nearly
orthogonal channels across the FT50 on per-publication terms, consistent with the cross-channel
decoupling discussed in the Overton literature (Szomszor and Adie, 2022). In the 2005–2019
window, the Spearman rank correlation across the 53 journals between FWCI and policy citations
per pub is 0.27, between FWCI and patent citations per pub is −0.12, and between policy
citations per pub and patent citations per pub is 0.08. The Top-10% rate correlates more strongly
with policy reach (ρ= 0.63) but only weakly with patent reach (ρ= 0.24). A journal’s rank on
one channel does not predict its rank on the others, even after per-publication adjustment. The
empty upper-right quadrant of Figure 1 is the geometric expression of this point: no FT50 journal
in the 2005–2019 window achieves above-median per-paper policy reach and above-median
per-paper patent reach simultaneously.
The disciplinary composition of the channels matches the decoupling. Five economics jour-
nals account for 65% of all FT50 policy-citation footprint over the window. Operations Research
14

and Operations Management journals account for 33% of the patent footprint; Marketing journals
account for another 20%. Management journals dominate raw citation count and views (32.7%
and 34.3% respectively) but contribute less than 8% to either of the societal channels.
3.6 How distinct are the policy and patent measures from citation-based
measures?
A reasonable objection to the seven-indicator composite is that the policy and patent measures
may simply track the citation measures. If they do, the composite is a citation ranking in disguise,
and the two societal channels add nothing. The question is whether the four societal indicators
(policy citations per pub, share of papers reaching policy, patent citations per pub, share of
papers reaching patents) carry information that the three citation indicators (FWCI, Top-10%
rate, Field-Weighted Views Impact) do not. The data answer it directly.
The strongest correlation between any societal indicator and any citation indicator is 0.49,
between the share of papers reaching policy and the Top-10% rate (Figure 7b). That is the
maximum; it corresponds to 24% shared variance, so even the most citation-aligned societal
measure leaves three-quarters of its variance unexplained by the closest citation measure. The
mean absolute correlation between a societal indicator and a citation indicator is 0.25. The two
policy measures are weakly-to-moderately positive with FWCI and the Top-10% rate (0.37 to
0.49) and near zero with Field-Weighted Views Impact; the two patent measures are weakly
negative with all three citation measures (−0.11 to −0.25). On the patent side, a journal that
scores well on citations tends, if anything, to score slightly worse on patent reach. Policy and
patent reach are not citations under another name.
The full picture is shown in Figure 7a. The seven-indicator correlation matrix has a clear block
structure: indicators within a channel are strongly collinear, which is the intended behaviour,
because each pair measures one construct from two angles. The three citation indicators carry
a mean pairwise correlation of 0.83, the two policy indicators correlate at 0.93, and the two
patent indicators at 0.96. Across channels the mean correlation is −0.02. A principal component
analysis confirms the dimensionality: three components are needed to account for 91% of the
variance in the seven indicators (43%, 26%, and 22% respectively), and the loadings separate the
15

channels rather than blending them. A single “quality” factor does not exist in these data; the
FT50 occupies a three-dimensional impact space.
The practical consequence is that the choice of indicator set changes the ranking. A citation-
only composite, built from the three citation indicators alone, correlates with the full seven-
indicator composite at a Kendall τ of only 0.54. Sorting the 53 journals into within-FT50
quartiles under each indicator set, 25 of the 53 move at least one quartile when the policy and
patent channels are added, and only 28 stay put (Figure 8). The largest single-journal moves run
in both directions: the elite economics and finance journals rise (Review of Economic Studies
by 24 rank positions,Econometricaby 18,Management Scienceby 16,Review of Finance
by 15), while management journals whose strength is concentrated in the citation channel fall
(Entrepreneurship Theory and Practiceby 19,Journal of Business Ethicsby 18,Academy of
Management Annalsby 17,Journal of Managementby 17). The citation channel and the societal
channels reward different journals. A ranking that includes only citations has made an implicit
and consequential choice.
3.7 Trajectories and near-term outlook
The cross-sectional ranking describes where journals sit over 2005–2019 as a whole. A separate
question is where they are heading. To address it, the seven-indicator composite ranking is
recomputed on seventeen overlapping five-year windows, from 2005–2009 through 2021–2025,
stepped one year at a time. Because each window is ranked internally, the common citation-
accrual shift that affects all journals in a given window cancels out, and the resulting series
of composite ranks is comparable across windows. Two journals founded mid-window, the
Academy of Management Annalsand theStrategic Entrepreneurship Journal, do not have a
complete seventeen-window series and are excluded from the trajectory analysis, leaving 51
journals. The windows that include 2020 onward carry more accrual noise, particularly on the
patent indicators, where citations to papers published after about 2022 are not yet observable; the
within-window ranking absorbs the common component, and the composite is carried mainly by
the citation and policy channels in those windows.
The trend line for each journal is computed by ordinary least squares: the journal’s composite
16

rank in each of the seventeen windows is regressed on the window’s midpoint year. The fitted
slope is the journal’s trajectory, in rank positions per year; a negative slope means the journal
is improving, because a lower rank number is better. The fitted line extended three years past
the last window gives the projection. With the last window centred on 2023, the projection
reaches a window midpoint of 2026, that is, a notional 2024–2028 window. It is a naive linear
extrapolation, offered as an indication of direction rather than a forecast.
Two groups are of interest. The first is journals not currently in the top quartile but with
an improving trajectory (negative slope); the seven steepest are theJournal of Business Ethics
(−1.89 rank positions per year),Human Resource Management( −1.52),Human Relations
(−1.47), theReview of Finance( −0.86), theReview of Accounting Studies( −0.85), theJournal
of Political Economy( −0.71), and theReview of Financial Studies( −0.28). TheJournal
of Political Economy, currently at rank 27, has the most consequential improving trajectory,
projecting toward the top quartile by 2026. The second group is journals currently in the top
three quartiles but with a declining trajectory (positive slope); the seven steepest are theJournal
of Operations Management( +2.11 per year),MIS Quarterly( +2.05),Organization Science
(+1.62),Econometrica( +1.26), theStrategic Management Journal( +1.23), theJournal of
Business Venturing( +0.88), and theAcademy of Management Journal( +0.83). Figure 9 plots
both groups, with the linear projection extended three years past the last window.
The trajectory result is distinct from the ranking-shift result of the previous subsection and
should not be conflated with it. The ranking shift is cross-sectional: it asks which journals gain
when the indicator set is broadened. The trajectory is temporal: it asks which journals are moving
up or down over time on the fixed seven-indicator composite.Econometrica, for instance, gains
18 rank positions when the societal channels are added to the indicator set, yet its rolling-window
trajectory is declining. Both statements describe the same journal without contradiction. The
projections in Figure 9 assume that the recent linear trend continues, which it need not; they are
best read as a structured way of flagging journals whose recent direction is worth watching, not
as a model of future performance.
17

4 Discussion: the 2026 list update against the comparative
quality spectrum
The Financial Times announced a revision of the list in 2026, the first substantial change since
the 2016 reshuffling discussed in detail by Fassin (2021). Three journals were removed (Human
Relations,Journal of Business Ethics, andOrganization Studies, all in the Management cluster)
and three were added (Academy of Management Annalsin Management,American Sociological
Reviewin Sociology, andPsychological Sciencein Psychology). All three of the removed
journals sit in the bottom quartile of the 2005–2019 composite ranking:Organization Studies
at rank 52 of 53,Human Relationsat rank 47, andJournal of Business Ethicsat rank 44. On
the quality map,Organization StudiesandHuman Relationssit in the lower-left Q4.Journal of
Business Ethicssits just inside Q3 with citation impact at the FT50 average and societal reach
below it. Two of the three additions sit in the top half of the ranking:American Sociological
Reviewenters in the top quartile and the Q1 high-citation high-societal quadrant, andAcademy
of Management Annalsenters in the second quartile with an exceptional within-FT50 citation
profile and below-average societal reach (Q3).Psychological Scienceenters in the third quartile,
with below-average citation impact and slightly above-average societal reach (Q2).
The swap tracks the comparative quality picture closely. The peer-perception judgement
implicit in the FT’s dean polls and editorial review is converging with the bibliometric picture
the framework recovers, and the convergence is itself a useful empirical finding. The form of the
swap, however, mostly tightens the bottom of the list and broadens the top. The citation channel
strengthens through the addition ofAnnals, a top-FWCI journal. The policy channel strengthens
marginally through the addition ofAmerican Sociological Review. The patent channel picks
up a modest non-OR contribution throughPsychological Science. None of the three additions
occupies the empty upper-right region of the quality map (Figure 2), where a journal would reach
both policy and industry at scale at the same time. If the policy and patent dimensions of impact
are part of what FT50 inclusion is meant to certify, the 2026 swap refines the existing impact
profile of the list rather than broadening it.
A more fundamental implication concerns the structure of the list. The analysis identifies a
18

within-FT50 quality spectrum that the binary in-or-out structure obscures. A channel-aware or
multi-tier presentation of the list would communicate this heterogeneity to deans, accreditation
bodies, and hiring committees without changing the list’s role in research evaluation. The 2026
update is consistent with this reading: the FT appears to be making implicit channel-aware
judgements when it removes bottom-quartile management journals and adds an exceptional
citation-prestige journal alongside one policy-strong and one patent-strong addition.
5 Caveats
Five caveats apply. First, the analysis is within-FT50. Without a control set of comparable
elite non-FT50 journals (the natural candidate is the ABS-AJG 4* set) it is not possible to say
whether the FT50 itself is moving relative to the wider business-research journal population.
The aggregate trends observed (median FWCI of 3.45 in 2005 falling to 2.04 in 2020; total
annual output growing 51% over the same period) fit the citation-metric ecology that Hanson
et al. (2024) and Fire and Guestrin (2019) describe at the level of all of academic publishing, and
are not necessarily features of the FT50 specifically.
Second, the SciVal extracts include self-citations by default. Self-citations have not been
stripped from any of the indicators, and a self-citation-stripped variant would shift the rankings,
particularly in fields with unusually high self-citation rates (Larivière and Sugimoto, 2019;
Ibrahim et al., 2025). This is the cleanest methodological extension of the present analysis.
Third, the policy-citation infrastructure is itself growing. Overton has been adding coverage
and depth across the windows used in the analysis (Szomszor and Adie, 2022; Cristofoletti et al.,
2025), and a small share of the cross-journal heterogeneity in policy reach probably reflects
uneven indexing across policy producers and source languages. The headline window starts in
2005 to mitigate the issue, but it is not eliminated.
Fourth, FT50 list membership is itself a moving target. The panel uses the current list,
including the 2026 additions; all six swap journals are present because the SciVal extraction
predates the FT’s operationalization of the change. The longitudinal stability claim concerns the
trajectory of journals that are or were recently on the list, not the trajectory of FT50-membership-
as-a-set.
19

Fifth, the sub-discipline grouping is heuristic at the boundaries. The channel-share results
are stable under alternative groupings (placingJournal of International Business Studiesin
Economics rather than Management, and placingResearch Policyin Management rather than
Innovation Studies). The full mapping is in Appendix A.
6 Conclusion
When the FT50 is examined on per-publication, properly normalized terms, the heterogeneity it
bundles is directly visible. The leading economics journals attract policy citations at a per-paper
rate two orders of magnitude greater than the lowest journals on the list. The leading information-
systems, marketing, and operations journals attract industry citations at a per-paper rate two to
three orders of magnitude greater than the academic-management or accounting cluster. The
composite ranking built from seven per-publication indicators identifies a top quartile of thirteen
journals and a bottom quartile of thirteen journals whose membership is stable across alternative
publication-year windows, with Kendall τ between rankings in the range 0.78 to 0.89 and the
worst pair of sensitivity windows still at 0.69. The three impact channels are nearly orthogonal
across the list: a journal’s strength on one does not predict its strength on the others, and no
journal achieves above-average per-paper policy reach and above-average per-paper patent reach
simultaneously.
FT50 membership is not meaningless. The elite economics, finance, information-systems,
and a small number of management and marketing journals do outperform across multiple
channels. The substantive implication is that the in-or-out structure conceals a quality spectrum,
and that a channel-aware presentation of the list (a small number of tiers based on which channel
a journal leads) would communicate this heterogeneity directly. The 2026 update is consistent
with this reading: it tightens the composite ranking at the top and the bottom while leaving the
channel orthogonality of the list undisturbed.
20

Author contributions (CRediT)
Arash Hajikhani:Conceptualization, Data curation, Formal analysis, Funding acquisition, In-
vestigation, Methodology, Project administration, Resources, Software, Supervision, Validation,
Visualization, Writing – original draft, Writing – review & editing.Yi Zhang:Investigation,
Methodology, Resources, Software, Supervision, Validation, Writing – original draft, Writing –
review & editing.Mengjia Wu:Investigation, Methodology, Validation, Visualization, Writing –
review & editing.
Data availability statement
The reshaped journal-year-metric panel (ft50_panel.csv, 39,432 rows), the per-window
per-journal indicator tables (2005–2019 headline, 2005–2014, 2010–2019, and 2015–2019
sensitivity replications), the composite-ranking and Kendall-τ stability tables, and all code used
for the analysis and figures will be archived at Zenodo with a DOI on acceptance. The raw SciVal
CSV exports cannot be shared openly because they are derived from a proprietary database
(Scopus and SciVal); the indicator-extraction parameters and the 53-journal Scopus source-id list
documented in the supplementary code allow exact replication for any user with SciVal access.
Overton-derived policy citations are similarly proprietary in their full granularity; the aggregated
per-journal indicators are computed and shared in the per-window indicator tables.
References
Baas, J., Schotten, M., Plume, A., Côté, G., and Karimi, R. (2020). Scopus as a curated,
high-quality bibliometric data source for academic research in quantitative science studies.
Quantitative Science Studies, 1(1):377–386.
Cristofoletti, E. C., Salles-Filho, S., Juk, Y ., Cabral, B., Pinto, K. E. F., Hollanda, S., Graziani,
C., and Pereira, C. A. (2025). A long and winding road: Research impact evaluation over
public policies.Quantitative Science Studies, 6:194–215.
Elsevier B.V . (2019a). Research metrics guidebook. Research Intelligence, Elsevier.
21

Elsevier B.V . (2019b). SciVal usage and patent metrics guidebook. Research Intelligence,
Elsevier.
Fassin, Y . (2021). Does the Financial Times FT50 journal list select the best management and
economics journals?Scientometrics, 126:5911–5943.
Financial Times (2026). FT’s 50 journals used in Business School Research Rank (2026 update).
ft.com. Three titles removed (Human Relations, Journal of Business Ethics, Organization
Studies); three added (Academy of Management Annals, American Sociological Review,
Psychological Science).
Fire, M. and Guestrin, C. (2019). Over-optimization of academic publishing metrics: Observing
Goodhart’s law in action.GigaScience, 8(6):giz053.
Hanson, M. A., Gómez Barreiro, P., Crosetto, P., and Brockington, D. (2024). The strain on
scientific publishing.Quantitative Science Studies, 5(4):823–843.
Ibrahim, H., Liu, F., Zaki, Y ., and Rahwan, T. (2025). Citation manipulation through citation
mills and pre-print servers.Scientific Reports, 15:5480.
Jack, A. and Dalal, A. (2024). Business school and the pursuit of rigour, resonance and relevance.
Financial Times. Published 2024-11-08.
Larivière, V . and Sugimoto, C. R. (2019). The journal impact factor: A brief history, critique,
and discussion of adverse effects. In Glänzel, W., Moed, H. F., Schmoch, U., and Thelwall,
M., editors,Springer Handbook of Science and Technology Indicators, pages 3–24. Springer.
Meho, L. I. (2025). Gaming the metrics? bibliometric anomalies and the integrity crisis in global
university rankings.bioRxiv preprint.
Mingers, J. and Yang, L. (2017). Evaluating journal quality: A review of journal citation
indicators and ranking in business and management.European Journal of Operational
Research, 257(1):323–337.
22

Steingard, D., Linacre, S., Reibstein, D., Flynn, D., and Springer, C. (2026). Revolutionizing
societal impact in business school research: can the FT50 lead the change?Society and
Business Review, 21(2):316–333.
Szomszor, M. and Adie, E. (2022). Overton: A bibliometric database of policy document
citations.Quantitative Science Studies, 3(3):624–650.
Vidgen, R., Mortenson, M., and Powell, P. (2019). Invited viewpoint: How well does the
information systems discipline fare in the Financial Times’ top 50 journal list?Journal of
Strategic Information Systems, 28(4):101577.
Visser, M., van Eck, N. J., and Waltman, L. (2021). Large-scale comparison of bibliographic
data sources: Scopus, Web of Science, Dimensions, Crossref, and Microsoft Academic.
Quantitative Science Studies, 2(1):20–41.
Zhang, T. (2021). Will the increase in publication volumes “dilute” prestigious journals’ impact
factors? A trend analysis of the FT50 journals.Scientometrics, 126:863–869.
A Sub-discipline assignment of FT50 journals
The grouping below is anchored in each journal’s primary subject area in the Scopus All Science
Journal Classification, which is the classification SciVal uses to compute FWCI (Baas et al., 2020;
Elsevier B.V ., 2019a). For journals that span multiple ASJC categories the subfield assignments
documented for FT50 journals by Fassin (2021) and the Information Systems clustering used
by Vidgen et al. (2019) are followed. Practitioner outlets and Innovation Studies are treated as
separate categories because their indicator profiles differ systematically from the academic and
the broader social-science groups respectively.
23

01020304050
Composite rank in 2005 2014 window
0
10
20
30
40
50 Composite rank in 2015 2019 window
J. Finance
MIS Quarterly: Management In
Quarterly J. Economics
J. Marketing
J. Operations Management
Contemporary Accounting Rese
Review of Accounting Studies
Human Resource Management
Organization Studies
J. Consumer Psychology
J. Accounting Research
J. Political Economy
Organization Science
AoM Review
Administrative Science Quart
American Economic Review
J. the Academy of Marketing
Strategic Entrepreneurship J
J. Accounting and Economics
Composite rank stability across alternative windows
(Kendall  = 0.69 between most distant windows)
Sub-discipline
Economics
Finance
Accounting
Management
Marketing
OR / Operations
Information Systems
Psychology / OB
Sociology
Practitioner
Innovation Studies
Figure 5: Composite within-FT50 rank in the 2005–2014 window (x-axis) versus the 2015–2019
window (y-axis), with axes inverted so that rank 1 sits in the upper right. Points cluster tightly
along the diagonal, indicating that the ranking is largely stable across the decade-long shift in
window. A small number of journals (Journal of Accounting Research, Organization Science,
Journal of Political Economy) move appreciably, suggesting genuine relative shifts in their
indicator profiles.
24

0.0 0.2 0.4 0.6 0.8 1.0
Kendall  (1.0 = identical ranking)
Patent cit. per pub
Share reach. patents
FW Views Impact
FWCI
T op-10% rate
Share reach. policy
Policy cit. per pub
Per-indicator rank stability of headline window vs. alternative windows
2005-2019 vs 2005-2014 2005-2019 vs 2010-2019 2005-2019 vs 2015-2019
Figure 6: Kendall τ between rankings produced under different publication-year windows, by
indicator. The dotted vertical line marks τ= 0.7 . Policy-related indicators are the most stable;
patent-related indicators are the least stable, reflecting their sparser distribution.
FWCI
T op-10% rate
FW Views ImpactPolicy cit. / pub
Share reaching policy
Patent cit. / pub
Share reaching patents
FWCI
T op-10% rate
FW Views Impact
Policy cit. / pub
Share reaching policy
Patent cit. / pub
Share reaching patents
1.00 0.95 0.68 0.37 0.39 -0.13 -0.11
0.95 1.00 0.61 0.46 0.49 -0.23 -0.19
0.68 0.61 1.00 -0.14 -0.01 -0.25 -0.20
0.37 0.46 -0.14 1.00 0.93 -0.10 -0.14
0.39 0.49 -0.01 0.93 1.00 -0.21 -0.25
-0.13 -0.23 -0.25 -0.10 -0.21 1.00 0.96
-0.11 -0.19 -0.20 -0.14 -0.25 0.96 1.00
(a) All seven indicators: tight blocks on the diagonal,
near-zero elsewhere
Policy cit. / pub Share reaching
policy
Patent cit. / pub Share reaching
patents
0.6
0.4
0.2
0.0
0.2
0.4
0.6
Spearman correlation with citation indicator
|r| = 0.5
(b) Distinguishing power: the four societal indicators
vs the three citation indicators (max |r| = 0.49)
vs FWCI
vs T op-10% rate
vs FW Views Impact
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
Figure 7: Distinguishing power of the societal indicators. (a) Spearman correlation among
all seven per-publication indicators, with channel blocks outlined; within-channel correlations
average 0.83, across-channel correlations average −0.02. (b) Each of the four societal indicators
against each of the three citation indicators; no pair exceeds |r|= 0.49 , and the patent measures
are weakly negative with all three citation measures.
25

Q1
(13)
Q1
(13)
Q2
(14)
Q2
(14)
Q3
(13)
Q3
(13)
Q4
(13)
Q4
(13)
9
3
1
3
6
4
1
1
5
4
34
9
Citation-only
ranking
Full ranking
(+ policy + patent)
Quartile transitions when policy and patent channels are added to the FT50 ranking
28 of 53 journals (53%) keep their quartile; 25 move at least one quartile; three journals jump two quartiles (annotated)
Econometrica
(Q3  Q1)
Entrepreneurship Theory and Practice
(Q1  Q3)
Journal of Business Ethics
(Q2  Q4)
Figure 8: Quartile transitions of the 53 FT50 journals between the citation-only ranking (left) and
the full seven-indicator ranking (right). Ribbon width is proportional to the number of journals
making each transition; the number on each ribbon is that count. Twenty-eight journals keep
their quartile; twenty-five move at least one quartile.
26

2008 2011 2014 2017 2020 2023 2026
Rolling 5-year window (midpoint year)
0
10
20
30
40
50 Within-FT50 composite rank
top quartile
3-year
projection
(a) Top 7 rising journals
below top quartile now, improving trajectory
J. Political Economy  ( 9)
Rev. of Financial Studies  ( 13)
J. Business Ethics  ( 14)
Human Relations  ( 20)
Human Resource Management  ( 26)
Review of Finance  ( 30)
Rev. of Accounting Studies  ( 38)
2008 2011 2014 2017 2020 2023 2026
Rolling 5-year window (midpoint year)
top quartile
3-year
projection
(b) Top 7 falling journals
top three quartiles now, declining trajectory
J. Business Venturing  ( 19)
AoM Journal  ( 23)
MIS Quarterly  ( 33)
Econometrica  ( 36)
Strategic Management Journal  ( 36)
J. Operations Management  ( 43)
Organization Science  ( 50)
Composite-rank trajectories on rolling 5-year windows, 2005--09 to 2021--25, with a naive 3-year linear projection to a 2026 window midpoint
each journal has a distinct colour and marker; the solid line is the OLS fit, the dashed line is its 3-year extension; label shows projected 2026 rank
Figure 9: Composite-rank trajectories on rolling five-year windows, 2005–2009 to 2021–2025,
with a naive three-year linear projection (dashed) reaching a 2026 window midpoint. The trend
line for each journal is an ordinary-least-squares fit of composite rank on window midpoint year.
(a) The seven journals with the steepest improving trajectory that are not in the top quartile; their
lines move up toward rank 1. (b) The seven journals with the steepest declining trajectory that
are currently in the top three quartiles; their lines move down. Each label shows the journal and
its projected 2026 rank in brackets, with a leader line to its trend-line endpoint. The shaded band
marks the within-FT50 top quartile. Windows that include 2020–2025 carry more accrual noise,
especially on the patent channel.
27

Table 1: Sub-discipline assignment of the 53 FT50 journals.
Sub-discipline Journals
Economics (5) American Economic Review; Quarterly Journal of Eco-
nomics; Journal of Political Economy; Econometrica;
Review of Economic Studies
Finance (5) Journal of Finance; Journal of Financial Economics;
Review of Financial Studies; Review of Finance; Journal
of Financial and Quantitative Analysis
Accounting (6) Accounting Review; Journal of Accounting Research;
Journal of Accounting and Economics; Accounting, Or-
ganizations and Society; Contemporary Accounting Re-
search; Review of Accounting Studies
Management (16) Academy of Management Journal; Academy of Man-
agement Review; Academy of Management Annals; Ad-
ministrative Science Quarterly; Strategic Management
Journal; Journal of Management; Journal of Manage-
ment Studies; Organization Science; Organization Stud-
ies; Human Relations; Human Resource Management;
Strategic Entrepreneurship Journal; Entrepreneurship
Theory and Practice; Journal of Business Venturing;
Journal of Business Ethics; Journal of International Busi-
ness Studies
Marketing (6) Journal of Marketing; Journal of Marketing Research;
Marketing Science; Journal of Consumer Research; Jour-
nal of Consumer Psychology; Journal of the Academy
of Marketing Science
OR / Operations (5) Management Science; Operations Research; Manufac-
turing and Service Operations Management; Produc-
tion and Operations Management; Journal of Operations
Management
Information Systems (3) MIS Quarterly: Management Information Systems; In-
formation Systems Research; Journal of Management
Information Systems
Psychology / OB (3) Journal of Applied Psychology; Psychological Science;
Organizational Behavior and Human Decision Processes
Sociology (1) American Sociological Review
Practitioner (2) Harvard Business Review; MIT Sloan Management Re-
view
Innovation Studies (1) Research Policy
28
