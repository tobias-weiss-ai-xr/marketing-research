---
title: 'The direct democracy paradox: Microtargeting and issue ownership in Swiss online political ads'
url: https://arxiv.org/abs/2512.14564
category: digital-marketing
subcategory: empirical
date: 2025-12
venue: ''
authors:
- Arthur Capozzi
source: arxiv
pdf_url: https://arxiv.org/pdf/2512.14564
pages: 17
chars: 67766
fetched_at: '2026-11-08T13:18:04+00:00'
kb_version: 1
---

# The direct democracy paradox: Microtargeting and issue ownership in Swiss online political ads

THE DIRECT DEMOCRACY PARADOX: MICROTARGETING AND
ISSUE OWNERSHIP INSWISS ONLINE POLITICAL ADS
Arthur Capozzi
Computational Social Science
ETH Zürich
Stampfenbachstrasse 48,8006,Zürich,
Switzerland
ABSTRACT
Political advertising on social media has fundamentally reshaped democratic deliberation, play-
ing a central role in electoral campaigns and propaganda. However, its systemic impact remains
largely theoretical or unexplored, raising critical concerns about institutional fairness and algorithmic
transparency. This paper provides the first data-driven analysis of the relationship between direct
democracy and political advertising on social media, leveraging a novel dataset of 40,000 political ads
published on Meta in Switzerland between 2021 and 2025. Switzerland’s system of direct democracy,
characterized by frequent referenda, provides an ideal context for examining this relationship beyond
standard electoral cycles. The results reveal the sheer scale of digital campaigning, with 560 million
impressions targeting 5.6 million voters, and suggest that greater exposure to “pro-Yes” advertising
significantly correlates with referendum approval outcomes. Demographic microtargeting analysis
suggests partisan strategies: Centrist and right-wing parties predominantly target older men, whereas
left-wing parties focus on young women. Regarding textual content, a clear pattern of “talking past
each other” is identified; in line with the issue ownership theory, parties avoid debating shared issues,
preferring to promote exclusively owned topics. Furthermore, the parties’ strategies are so distinctive
that a machine learning model trained only on audience and topic features can accurately predict the
author of an advertisement. This article highlights how demographic microtargeting, issue divergence,
and tailored messages could undermine democratic deliberation, exposing a paradox: Referenda are
designed to be the ultimate expression of the popular will, yet they are highly susceptible to invisible
algorithmic persuasion.
Keywordspolitical advertising, microtargeting, elections, Facebook, Instagram
1 Introduction
Online political advertising has long been considered controversial and potentially capable of undermining democratic
processes, primarily due to its effectiveness in manipulating voters, fueling cynicism, and polarizing the electorate [1].
This reality stands in stark contrast to the principles of active democracy, which is founded on the idea that citizens are
well-informed and capable of debating and deciding on complex policy issues as part of shared public deliberation [2].
The threat to this public sphere is significantly amplified by the advent of microtargeting, which uses vast datasets
to tailor persuasive messages to narrow, psychologically profiled segments of the electorate [ 3]. In fact, multiple
studies have found that such personalized political ads are more effective at persuading than generic, non-personalized
messages [4, 5], while new generative AI technologies promise to render these microtargeting campaigns even more
effective [4]. Although the impact of these technologies on candidate elections is well documented [6, 7], their systemic
impact on policy-making and direct legislation remains largely unexplored. Does algorithmic microtargeting simply
encourage voter participation, or does it fundamentally fragment the debate on key issues? This gap is critical because
the risks are amplified in direct democratic systems. Here, a dangerous paradox emerges: citizens operate under the
impression that they are making sovereign decisions, yet their preferences may actually be steered by opaque, tailored
arXiv:2512.14564v2  [cs.SI]  20 Jan 2026

Capozzi A.
messaging. If the electorate feels empowered to decide but is unknowingly steered by algorithms, is the “will of the
people” still authentic?
To answer this question, Switzerland offers a unique laboratory. Firstly, direct democracy is not just a feature, but
a central pillar of the nation’s identity. Swiss citizens vote on national issues approximately four times per year,
participating in far more referendums and initiatives than citizens of any other country [8]. Secondly, Switzerland is a
robust setting for testing the generalizability of cross-cultural findings. Switzerland is a multicultural nation of 9 million
people with four official languages, where 41% of permanent residents have a migration background as of 2024.
This article presents a longitudinal, data-driven analysis of a novel dataset of 40,000 political ads published on Facebook
and Instagram in Switzerland from 2021 to 2025. Through a combined study of demographic microtargeting and textual
content, this research assesses the scale, scope, and normative impact of opaque online political advertising, while
isolating differences and similarities among major political parties and linguistic regions. Beyond the specific case
study, the article describes a reproducible research pipeline that can be applied to other contexts and democracies, and
provides researchers and policymakers with a toolbox to make the digital public sphere more transparent.
2 Background
2.1 Online political advertising
The real impact of social media platforms on political opinion formation and voting behavior remains a topic of debate
in the scientific literature. For instance, large-scale experiments have demonstrated that algorithmically delivered social
messages can measurably increase voter turnout [9]. Other experiments have shown that curated search rankings can also
potentially shift the preferences of undecided voters [10]. The impact of online communication on politically sensitive
topics has also been examined. For example, Papakyriakopoulos et al. [11] investigated the role of demagoguery in
civic engagement on Reddit, while Lee and Hsieh [ 12] examined participation in online activism, or “slacktivism”,
in donation campaigns. Memes and other new forms of communication have also been studied as a mean of political
propaganda on social media [13, 14, 15].
This online political context intersects with the underlying business model of social media platforms, which is
predominantly based on advertising [16]. The economic logic incentivizes the continuous algorithmic optimization of
content delivery systems to maximize user engagement and, consequently, advertising revenue [17, 18]. The exploitation
of these highly optimized, profit-driven systems for the dissemination of political messages is, on the one hand, a source
of contemporary public debate and academic research [19, 20]. On the other hand, the effectiveness of recommendation
systems has also made online ads much more effective [21] and, as a result, led to a significant increase in their use [22].
In this context, Meta’s platforms, Facebook and Instagram, are among the most effective at influencing public
opinion [23] and accurately identifying users’ demographic information [ 24]. Madrigal [ 25] argues that although
Facebook’s potential impact on elections had been evident for years, it reached its peak during the 2016 presidential
election, with $1.4 billion spent on online ads during the campaign. However, hundreds of millions of dollars of dark
ads paid for by foreign governments to influence elections should be added to this number [ 25]. In this regard, it
has been proven that Russia attempted to manipulate the 2016 U.S. presidential election by running political ads on
Facebook [26, 27]. Matias et al. [ 28] designed a software-supported approach for auditing, which uses coordinated
volunteers to analyze political advertising policies enacted by Facebook and Google during the 2018 midterm U.S.
election.
During the 2021 German federal elections, a positive correlation was identified between social media advertising and
successful election outcomes for candidates [7]. In addition, Bär et al. [ 29] found that Meta’s algorithm prioritized
advertisements from populist parties during the same election campaign. Other studies on Facebook political ads include
anti-vaccination ads during COVID-19 [30], populist advertising for the European Parliamentary election in 2019 [6],
Italian political propaganda on the migration issue [31, 32], far-right misinformation spread by the populist Spanish
party VOX [33]. Many studies examined the spread and impact of political ads in Switzerland, with the earliest focusing
on traditional newspapers [34, 35]. Other studies have focused on referendum campaigns shifting from newspapers to
social media [36], or politicians’ use of social media [37].
2.2 Switzerland and direct democracy
Even before the advent of social media, the efficacy of direct democracy was questioned in academic literature, with
some analyzes finding it to be ineffective or even counterproductive in practice. Critics often highlight the potential for
a “tyranny of the majority”, the influence of wealthy special interest groups, and the risk posed by citizen incompetence
regarding complex policy issues [38, 39]. However, Switzerland is often cited as an exception to this criticism, with
2

Capozzi A.
its political system considered a model of success [40]. The Swiss model is not a simple and universally applicable
template; rather, it has developed within a specific and unique historical and institutional setting. It evolved “bottom-up”
from cantonal traditions, not being imposed by a central authority [ 41]. This high degree of direct democracy and
participation is argued to have numerous positive social and economic effects, including empowering citizens, making
procedures more appealing, and imposing fiscal discipline on public spending [ 40, 42]. Further research connects
direct democratic rights directly to improved economic performance [43] and higher levels of subjective well-being, or
happiness, among citizens [44].
Even within the Swiss context, the positive portrayal of direct democracy has its detractors. Some scholars have
highlighted problematic aspects, including “voting fatigue” caused by the large number of decisions, the complexity of
certain ballot measures, and the system’s ability to impede social and political reforms [2]. Furthermore, the “double
majority” rule, which requires a majority of both citizens and cantons, has been criticized for giving disproportionate
power to small, rural cantons. This rule enables controversial initiatives to pass despite lacking broad popular support in
major population centers [45].
In order to understand the deep cultural roots of direct democracy in Swiss institutions and society, it is necessary to
start with the very foundations of the Swiss Confederation. The modern federal state was established in 1848 as a direct
result of a brief civil war, known as the Sonderbund War. The new state faced the challenges of integrating minorities
and managing the country’s deep “cross-cutting cleavages” [41]. Switzerland was and remains a mosaic:
Linguistic.Since unification, there have been four national languages: German, French, Italian, and Romansh. In 2023,
61.4% of the population is native German speaker; 22.6% are native French speakers; 7.7% are native Italian speakers;
and 0.5% are native Romansh speakers [46].
Religious.According to the Swiss National Survey [ 47], 35.6% of the population was religiously unaffiliated in 2023.
The remaining population was divided as follows: 30.7% Catholic, 19.5% Swiss Protestant, 5.8% other Christian
denominations, and 6% Muslim.
Geographic.Although rural municipalities cover 57% of the country’s total area, in 2025 they are home to only 35% of
the population. In contrast, urban areas account for just 17% of the total area but are home to 65% of the population and
76% of the workforce [48].
Economic.Cantons with major urban centers, such as Zurich and Basel-Stadt, have an exceptionally high economic
output compared to other cantons. For instance, the nominal GDP per capita in Basel-Stadt was about CHF 210,000
in 2022, compared to the Swiss national average of around CHF 90,000 and the canton of Uri’s average of CHF
58,000 [49].
The federal state’s guarantee of municipal and cantonal autonomy with regard to taxation, education, and infrastructure
has played an important role in preserving cohesion [50]. Alongside this federal structure, the system of direct democracy
has been the most important political compromise made to maintain cohesion in diversity since the unification in
1848. For this reason, Swiss direct democracy has often been interpreted by scholars as a mechanism for minority
protection and power-sharing, specifically designed to integrate the country’s diverse segments [ 41, 51]. The legal
instruments available to citizens and enshrined in the Swiss Federal Constitution include the compulsory referendum,
non-compulsory (facultative) referendum, and the popular initiative [52, 45].
Swiss direct democracy operates within a historically highly fragmented, multipolar party system that reflects the
nation’s underlying divisions. In 2025, the Federal Assembly remains highly multipolar, with no single party holding
a majority. Following the 2023 federal elections, the national-conservative SVP (Swiss People’s Party) affirmed its
position as the largest party with 27.9% of the vote. The center-left SP (Social Democratic Party) followed at 18.3%. The
political center is split between the liberal, center-right FDP (FDP.The Liberals) at 14.3% and the Christian democratic
Die Mitte (The Center) at 14.1%. The environmentalist bloc, which saw historic gains in 2019, is divided between the
left-leaning GRÜNE (Green Party) at 9.8% and the centrist GLP (Green Liberal Party) at 7.6% [53]. Finally, it should
be mentioned that, out of a population of approximately 9.1 million in 2025, only about 5.6 million people are eligible
to vote.
3 Results
The findings presented in this section are divided into three subsections: demographic microtargeting (RQ1), impact on
direct democratic votes (RQ2), and strategic ownership of issues during federal elections (RQ3). The research questions
are the following:
3

Capozzi A.
RQ1 Demographic microtargeting
a: Do parties target specific users based on demographics?
b: Are there regional-specific demographics?
RQ2 Referenda
a: Are ads used intensively during popular referenda?
b: To what extent can ads influence the outcome of a referendum?
RQ3 Federal elections
a: Which issues do the parties promote the most, and how?
b: Are the content and the microtargeting of an ad reliable predictors of its author?
3.1 Microtargeting
Figure 1 compares each party’s audience demographics to the “party complementary” profile, which consists of all
advertisements not associated with that party. SinceRQ1.adoes not concern regional differences, ads from all languages
are combined for this analysis.
Overall, centrist and right-wing parties are more oriented towards a male audience, particularly the SVP (+36%). On
the other hand, the GRÜNE and the SP are more female-oriented, with the GRÜNE at+27%and the SP at+13%. In
terms of age reach, the SVP and, to a lesser extent, Die Mitte tend to attract an older audience, whereas the GRÜNE and
the GLP primarily attract people in the 25–34 age group. Furthermore, the GRÜNE is the only party that extensively
reaches the 18–24 age group, yet it underrepresents the over-45 age group more than any other party.
To answerRQ1.band evaluate the cantonal differences, the demographic distributions can be stratified by language.
Figure 3 shows the male-to-female odds ratio within each party’s audience by language. Each cell (party/language)
of the heatmap is computed with bootstrapping. For each of the 100 iterations, the OR is computed on a sample of
the party’s ads and the complement’s ads with replacement. The mean and 95% confidence interval are computed at
the end of the process from the bootstrap distribution. While center- and right-leaning parties attract male-dominated
audiences in all language regions, the SVP’s audience in Ticino, the only predominantly Italian-speaking canton,
is the most male-oriented. Other significant regional differences exist. For instance, the GLP and Die Mitte are
gender-balanced in the French-speaking cantons and slightly male-oriented in the German-speaking cantons (+15%
and +20%, respectively). However, they are much more male-oriented in Ticino ( +40% and +28%, respectively).
Further to the left on the political spectrum, the situation changes dramatically. For the SP, Ticino is again the least
gender-balanced canton, but this time it favors a more female audience (+32%). In German-speaking cantons, the SP
reaches a more female audience (+13%), while in French-speaking cantons, the audience is gender balanced. On the
other hand the GLP is more gender unbalanced in French-speaking cantons (+34%women).
Figure 2 shows the age distribution of the audience reached by the parties, compared to the party complementaries,
broken down by language group. The shaded area represents the standard deviation of the audience reached for each
age group. The distribution is build using a bootstrapping procedure similar to that described for Figure 3. Significant
differences between parties within the same canton can be observed, as well as regional variations within parties. While
the SVP focuses on an audience over 45, especially in Ticino, Die Mitte focuses on an older audience in French-speaking
cantons only. The SP, in German-speaking cantons, has a WD of almost 0 (no differences with the complementary
party’s audience), while in French-speaking cantons, it targets a much more over-45 audience. In Ticino, however, it
does the opposite, underrepresenting the over-35 audience and focusing on the 18-24 age range. The GLP, on the other
hand, focuses heavily on the 25-34 age range in French-speaking cantons, while in Ticino, the reach is broader (25-45).
With the exception of the GRÜNE and the SVP, all parties in the German-speaking cantons show fewer differences
compared to their counterparts. In summary, parties differ in their demographic reach (RQ1.a), with evident internal
variations emerging across different linguistic regions (RQ1.b).
3.2 Referenda
Figure 4 shows the seven-day moving average of total political ad views. The gray vertical lines represent referendums,
and the inset shows the total number of views per language in the 30 days before the federal elections of October 22,
2023. Clearly, this event caused the most significant increase in views. At first glance, it is instead difficult to answer
RQ2.aand determine whether advertising activity increases before the 14 referendum dates. As preliminary step, a
Wilcoxon signed-rank test is applied to compare ad views and spending in the 30 days before and after each referendum.
For completeness, this analysis is conducted separately for German, French, and Italian ads. The results of all the
tests (shown in S4 Table) confirm a significant increase in ad views and spending in the 30 days before a referendum
(p <0.001in all cases).
4

Capozzi A.
Male Female0.0
0.1
0.2
0.3
0.4
0.5Gender Distribution
OR: 0.87
.48 .51.52 .47
SP
Male Female
OR: 0.73
.44
.54.52
.47
GRÜNE
Male Female
OR: 1.12
.53
.46
.50 .49
GLP
Male Female
OR: 1.18
.54
.45
.50 .49
Die Mitte
Male Female
OR: 1.15
.53
.45
.50 .49
FDP
Male Female
OR: 1.36.57
.42
.49 .50
SVP
13-1718-2425-3435-4445-5455-6465+
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35Age Distribution
WD: 0.74
13-1718-2425-3435-4445-5455-6465+
WD: 3.52
13-1718-2425-3435-4445-5455-6465+
WD: 0.98
13-1718-2425-3435-4445-5455-6465+
WD: 1.56
13-1718-2425-3435-4445-5455-6465+
WD: 0.21
13-1718-2425-3435-4445-5455-6465+
WD: 2.43
Party Complementary WD = Wasserstein distance OR = Odds ratio
Figure 1:Comparison of demographic reach by age and gender.Each party’s audience is compared against the
distribution of all other ads (Party Complementary). Gender bias is measured using the male-to-female Odds Ratio
(OR), and age distribution shifts are measured using the Wasserstein Distance (WD).
0.0
0.1
0.2
0.3
0.4DE
WD: 0.41
SP
WD: 3.08
GRÜNE
WD: 0.56
GLP
WD: 1.04
Die Mitte
WD: 0.67
FDP
WD: 2.50
SVP
0.0
0.1
0.2
0.3
0.4FR
WD: 2.59
 WD: 4.87
 WD: 2.97
 WD: 3.80
 WD: 0.95
 WD: 2.41
13-1718-2425-3435-4445-5455-64 65+
age
0.0
0.1
0.2
0.3
0.4IT
WD: 2.18
13-1718-2425-3435-4445-5455-64 65+
age
WD: 1.62
13-1718-2425-3435-4445-5455-64 65+
age
WD: 2.44
13-1718-2425-3435-4445-5455-64 65+
age
WD: 1.07
13-1718-2425-3435-4445-5455-64 65+
age
WD: 1.02
13-1718-2425-3435-4445-5455-64 65+
age
WD: 4.23
Party Complementary WD = Wasserstein Distance
Figure 2:Language-specific age distributions by party.Distribution of audience age for each party compared to all
other ads (Party Complementary) across German, French, and Italian cantons. Shaded areas represent the standard
deviation derived from bootstrapping. Differences in distributions are reported as the Wasserstein Distance (WD).
Although the Wilcoxon signed-rank test confirms a difference, it does not account for confounding factors, such as
seasonality or other temporal patterns. The true impact of the referenda can be isolated by fitting a GAM to predict
the daily spending and impressions. Figure 5 shows the partial effects of the proximity of the referendum on the
log-transformed expenditure and impressions. The results are consistent across all language groups and suggest a
significant increase in ad spending and impressions 30 days before the vote. The 95% confidence intervals remain
entirely above the baseline during this pre-referendum period, and then collapse immediately after the vote at t= 0.
These results confirm that ads are used intensively during the referendum campaign period.
5

Capozzi A.
SP GRÜNE GLP Die Mitte FDP SVP
DE
FR
IT
0.86* 0.76* 1.14* 1.20* 1.06 1.35*
0.97 0.66* 1.01 1.07* 1.33* 1.23*
0.67* 0.82* 1.39* 1.29* 1.36* 1.57* 0.8
1.0
1.2
1.4
Male-to-Female Odds Ratio
Figure 3:Male-to-female targeting bias across linguistic regions.Odds ratios comparing the gender distribution of
each party’s ads against the complementary set. Values are bootstrapped means, with 1.0 representing gender balance,
while a value greater than 1.0 indicates a shift toward a more male audience. Significant results, where the 95%
confidence interval does not include the baseline of 1.0, are indicated by an asterisk (*).
2021-Jan 2022-Jan 2023-Jan 2024-Jan 2025-Jan
Date
0
2M
4M
6MImpressions 22-Sep 02-Oct 12-Oct 22-Oct
0
4M
8M
Total Impressions (7-Day Avg)
Referendum
Federal Election
French
German
Italian
Figure 4:Seven-day rolling average of ad impressions.The inset provides a daily view, disaggregated by language,
for the 30-day period preceding the federal election.
These findings lead to the next research question (RQ2.b): Given the increase in ad activity before referenda, is it
possible to explore and measure the influence of referendum ads on the outcome of the vote? Figure 6 shows the
distribution of all ad impressions supporting or opposing the referenda in relation to their outcomes. This figure suggests
that there is a relationship between the number of impressions per side and referendum outcomes. When a referendum
is rejected, the number of views of ads opposing the referendum looks to be higher. In contrast, if the outcome of
a referendum is positive, the number of views of ads supporting it tends to be higher. Correlation analysis shows
a moderate positive association between the ratio of Yes to No ad impressions and referendum approval outcome
(Spearman ρ= 0.39, p= 0.043). This indicates that referendums with relatively more Yes-side advertising tended to
be approved more often. Then, a Mann-Whitney U non-parametric test is used to independently compare the “Yes”
and “No” impression volumes. The results suggest that approved referenda have a significantly higher volume of “Yes”
impressions compared to rejected referenda (U= 146.0 , p= 0.0135). In contrast, the volume of “No” impressions
is not a statistically significant predictor of a referendum rejection (U= 117.0 , p= 0.1906). In other words, greater
exposure to pro-Yes advertising is associated with a higher probability of referendum approval, whereas exposure to
pro-No advertising does not show a systematic link to rejection outcomes. It is important to note that this is a correlation
and does not prove causation. In addition, popularity can act as a confounding factor: popular referendums are more
likely to attract higher ad spending for the “Yes” side and are also more likely to pass. This is because “Yes” campaigns
inherently face an uphill battle against the well-documented “status quo bias”, in which uncertain voters tend to vote
“No” to avoid uncertainty [54]. A “Yes” campaign must first have strong latent public support to overcome this bias and
succeed. Thus, ad volume may indicate a well-funded campaign with this support rather than being an independent
driver of the outcome [55].
6

Capozzi A.
4
2
0
2
4
Partial Effect
Italian German
3015015
30
Days to Nearest Referendum
4
2
0
2
4
Partial Effect
French
3015015
30
Days to Nearest Referendum
All Languages
Expenditure Impressions Referendum Day (t=0) Baseline
Figure 5:Temporal dynamics of advertising intensity.Partial effects of the “days to referendum” variable on
log-transformed Expenditure (blue curve) and Impressions (orange curve). The vertical dotted line att= 0marks the
day of the vote. The analysis isolates the referendum effect from seasonal trends and is presented for each linguistic
region and the national aggregate. Shaded areas represent 95% confidence intervals.
3.3 Federal elections
The third research question focuses on the federal elections in October 2023 and the issues promoted in ad campaigns.
As described in the Federal Election Subsection, each ad published in the month before the federal elections is labeled
with a relevance flag and with up to 3 keywords related to the topics discussed in the ad. Thanks to this data-processing
procedure, it is possible to investigate whether parties discuss different issues during federal elections or promote
different views on the same issues (RQ3.a).
Figure 7 shows the share of impressions by party for the top ten topics by impressions. Most issues are promoted
exclusively by one party or by a few parties that are close to each other on the political spectrum. For example, the
issues of “Business & Regulation” and “Taxation & Public Finance” are almost only represented by the SVP, the FDP,
and Die Mitte. Most of the impressions on the issue of “Civil Liberties & Rights” (which includes topics such as
abortion, drugs liberalization, and freedom of speech) are shared by the SVP and the FDP; on the other hand, most of
the impressions on the issue “Agriculture & Food Security” are shared by the SVP and Die Mitte. Instead, issues related
to “Pensions & Retirement”, “Climate & Environment”, “Energy & Policy”, and “Foreign Relations” (which covers
topics such as EU relations, NATO, or the war in Ukraine) are shared almost exclusively by the SP and the GRÜNE.
They also focus heavily on “Family & Youth Policy”, “Gender & LGBTQ+ Rights”, “Social Justice & Equality”, and
“Political Spectrum” (including topics such as progressive policies and liberalism). However, other issues transcend
traditional political divides, receiving support from parties that would otherwise be considered ideologically distant.
These include “Education System” (shared by the SVP, the FDP, and the SP), “Infrastructure & Mobility” (shared by the
GRÜNE and the SVP), Housing & Rent” (shared by the SP, the GRÜNE and the FDP), “Healthcare System” (shared by
the SP, the GRÜNE and Die Mitte), and “Economy & labour” (shared by all parties except the GLP and Die Mitte).
7

Capozzi A.
Rejected Accepted
Referendum Outcome
0
1M
2M
3M
4MTotal Impressions
Campaign Side
Supporting
Opposing
Figure 6:Distribution of ad impressions for pro-Yes and pro-No campaigns, grouped by referendum outcome.
Business &Regulation
Economy & LaborHousing & Rent
Pensions & Retirement
Taxation &
Public Finance
Agriculture &
Food Security
Climate & Environment
Energy & Policy
Infrastructure & Mobility
Urban & RegionalDevelopment Democratic ProcessForeign RelationsNational SecurityPolitical Spectrum Civil Liberties & Rights Culture Society Education System Family & Youth Policy
Gender &
LGBTQ+ RightsHealthcare System
Immigration & Asylum
Social Justice& Equality
Media & Information
SVP
FDP
Die Mitte
GLP
GRÜNE
SP
0.33 0.14 0.05 0.01 0.27 0.66 0.09 0.06 0.34 0.06 0.19 0.03 0.78 0.18 0.53 0.31 0.33 0.07 0.02 0.02 0.80 0.02 0.02
0.24 0.14 0.31 0.05 0.50 0.07 0.00 0.05 0.00 0.06 0.14 0.02 0.04 0.04 0.30 0.02 0.21 0.04 0.10 0.08 0.01 0.02 0.96
0.33 0.04 0.01 0.01 0.15 0.16 0.00 0.06 0.01 0.08 0.02 0.01 0.08 0.04 0.03 0.26 0.06 0.01 0.00 0.19 0.00 0.05 0.00
0.07 0.03 0.02 0.00 0.01 0.00 0.02 0.00 0.01 0.02 0.03 0.04 0.02 0.02 0.02 0.13 0.01 0.03 0.00 0.03 0.01 0.03 0.00
0.02 0.27 0.17 0.36 0.00 0.11 0.71 0.57 0.56 0.05 0.36 0.29 0.00 0.39 0.03 0.14 0.10 0.32 0.35 0.20 0.02 0.49 0.00
0.00 0.34 0.43 0.56 0.05 0.00 0.17 0.26 0.07 0.74 0.27 0.43 0.08 0.33 0.01 0.02 0.29 0.45 0.51 0.46 0.15 0.38 0.00
Economy Environment Governance Society Technology
Figure 7:Share of impressions per topic by party.Only the top ten topics for each party are represented.
Finally, some issues are pushed by a single party. For instance, “National Security” and “Immigration & Asylum”
are cornerstones of the SVP’s agenda but are not promoted by other parties. The issue of “Media & Information”
(which includes topics such as cancel culture, disinformation, and woke culture) is almost exclusively promoted by the
center-right FDP party. The issue of “Urban & Regional Development” is addressed almost exclusively by the SP. It is
also worth mentioning that the more centrist parties, GLP and Die Mitte, have the lowest share values. It is reasonable
to hypothesize that this is because they address a wide range of issues instead of focusing on a few specific topics. In
summary, of the two hypotheses presented at the beginning of this subsection, the most accurate is that parties tend to
have different agendas and rarely promote or debate the same topics.
To further investigate similarities and differences between parties, a machine learning model is built to try to predict
the party author of an ad (RQ3.b). For this multi-class classification task, a multinomial logistic regression model is
trained on the ads relevant to the 2023 federal elections. For completeness, three different feature combinations are
tested: (1)Demographic, representing the percentage of impressions per age and gender bucket; (2)Topic, which are
one-hot encoded topic categories; and (3) a combination ofDemographic + Topics.
Table 1: AUC ROC score for each feature combination/party
Demographic Topics Demographic + Topics
SVP 0.748 0.804 0.869
GRÜNE 0.728 0.775 0.857
SP 0.661 0.776 0.816
GLP 0.653 0.736 0.795
FDP 0.685 0.710 0.792
Die Mitte 0.632 0.722 0.759
8

Capozzi A.
In general, the model achieves strong discriminative power across all classes and feature combinations, as shown by
Table 1 where is reported the One-vs-Rest goodness of fit measured as the area under the ROC curve.Demographic
features alone are sufficient to distinguish the parties with good performance. However,Topicfeatures appear to be
stronger predictors, and the best-performing model uses the combined set of all features. In the combined model, all
parties achieve an AUC ROC score above 0.75, with top-performing classes like SVP and GRÜNE exceeding 0.85.
The recall-normalized confusion matrix (Figure 8.a) highlights a more complex situation than the model’s high
discriminative power might suggest.
SP GRÜNE GLP Die Mitte FDP SVP
Predicted Party
SP GRÜNE GLP Die Mitte FDP SVP
Actual Party
0.48 0.26 0.04 0.02 0.07 0.12
0.13 0.69 0.04 0.01 0.04 0.10
0.18 0.18 0.28 0.01 0.14 0.20
0.18 0.13 0.04 0.08 0.24 0.32
0.12 0.10 0.04 0.03 0.36 0.35
0.05 0.06 0.02 0.00 0.10 0.78
(a)
SP GRÜNE GLP Die Mitte FDP SVP
Predicted Party
SP GRÜNE GLP Die Mitte FDP SVP
Actual Party
0.50 0.19 0.14 0.17 0.10 0.07
0.16 0.59 0.14 0.12 0.06 0.07
0.10 0.07 0.47 0.05 0.10 0.06
0.10 0.05 0.07 0.41 0.19 0.11
0.09 0.05 0.11 0.20 0.39 0.16
0.05 0.05 0.07 0.05 0.16 0.53 (b)
Figure 8:Recall-normalized (a) and Precision-normalized (b) confusion matrices.The metrics refer to the
Demographic + Topicsmodel. The diagonal shows the per-class recall (a) or precision (b).
While recall is high for parties at the poles of the political spectrum, such as the SVP (0.78), it is notably low for the
centrist parties Die Mitte and the GLP. This is particularly evident for Die Mitte, which achieves a recall of only 0.08.
The confusion matrix shows that Die Mitte ads are most frequently misclassified as SVP (32%) and FDP (24%). This
Economy& Labor
Housing Rent
Climate &
EnvironmentEnergy Policy DemocraticProcessGovernance& Politics
Political
Spectrum Civil Liberties& Rights Culture &Society EducationSystemHealthcareSystemImmigration& AsylumSocial Justice& Equality
0.3
0.2
0.1
0.0
0.1
0.2
0.3
0.4
Marginal Effect
Economy Environment Governance Society
SP GRÜNE GLP Die Mitte FDP SVP
Figure 9:Marginal effects of the model with the best feature combination (demographic + topics).Positive values
indicate a higher likelihood of an ad belonging to a specific party when that topic is present. Only statistically significant
coefficients (p <0.05) are displayed.
result suggests that while the model can reliably distinguish Die Mitte from non-Die Mitte ads (as shown by its high
AUC of 0.76), it fails to classify them as the top choice, probably because of a strong feature overlap with other parties.
In line with the analyses conducted for RQ1.a and RQ1.b, the difficulty of predicting centrist parties reinforces the
observation that they rely less on microtargeting strategies and avoid focusing on specific issues.
9

Capozzi A.
As a final step, the marginal effects of the model trained only onTopicfeatures are studied to better understand the
predictive interaction between topics and parties. The topic-share plot in Figure 7 represents the raw association between
a topic and a party, meaning it also includes the effects of all other topics. In contrast, marginal effects isolate the
predictive effect of adding a single topic while holding all others constant, thereby highlighting the influence of each
topic. Figure 9 presents the marginal effects that are statistically significant ( p <0.005), revealing several patterns.
For example, environmental and social issues sharply divide the parties. In particular, topics related to “Climate &
Environment” are negatively associated with the SVP, the FDP, and Die Mitte, while “Energy Policy” topics are a
positive predictor only for Die Mitte. In contrast, “Social Justice & Equality” issues are strong positive predictors of
the SP and the GRÜNE. Other policy areas also show distinct alignments. “Healthcare System” topics are positively
associated with the SP and Die Mitte, and “Education System” issues appear as relevant predictive topics for the FDP
and Die Mitte. Moreover, “Immigration & Asylum” issues are a significant, strong, positive predictor exclusively for
the right-wing party SVP.
4 Discussion
The 2024 European Parliament Youth Survey [56] reports that 42% of European youth (ages 16–30) rely primarily on
social media platforms such as TikTok, Instagram, and YouTube for political and social news. Consequently, the paid
advertising and algorithmic mechanisms that govern visibility on these platforms now have a disproportionate influence
on the democratic process. Switzerland’s system of direct democracy, characterized by frequent popular referendums, is
particularly vulnerable to these shifts in democratic deliberation. It is little wonder that online political advertising has
shifted from a peripheral tool to a central mechanism for influencing both elections and policy outcomes.
Against this backdrop, this article provides a comprehensive analysis of 40,000 political advertisements (560 million
impressions) published on Meta from 2021 to 2025. A critical finding is the strong correlation between the volume of
“pro-Yes” advertising and referendum approval. Unlike elections, where voters rely on party heuristics, referendums
often involve complex technical issues in which the availability of information plays a decisive role. The correlation
between higher ad exposure and favorable outcomes raises normative concerns. If visibility, purchased through an
algorithmic auction, can influence policy decisions, then the “marketplace of ideas” could become a “marketplace
of budgets”. Although our data reveals a correlation rather than a direct causal relationship, it suggests that well-
funded interest groups may use algorithmic reach to circumvent traditional deliberation, especially in “low-salience”
referendums where voters have fewer preconceived notions. Furthermore, evidence of demographic microtargeting
confirms that political parties are actively segmenting the electorate, rather than merely broadcasting messages. Their
adaptation of strategies to Switzerland’s linguistic and regional divisions demonstrates the sophistication of these
campaigns. As previous studies have shown, Swiss heterogeneity is a primary driver of political divisions [ 57, 58]
and voting behavior [59, 60]. Our results suggest that algorithms are effectively automating the exploitation of these
societal fault lines. By delivering different narratives to young urban women than to older rural men, microtargeting
reinforces existing socioeconomic and cultural divisions, which could lead to the polarization seen in other multicultural
democracies.
The content analysis reveals a distinct pattern of divergent issues, where political actors “talk past each other”. Rather
than engaging in a shared debate, parties retreat into safe topics, effectively creating parallel public spheres. This
behavior aligns with the theory of issue ownership [ 61], in which parties emphasize topics on which they have a
reputational advantage [62]. By selectively focusing on “their” issues, parties avoid competing on unfavorable ground
and instead attempt to make their own issue priorities the most important for voters [63, 64]. Social media algorithms
likely amplify this effect beyond what is possible in traditional media. In a television broadcast, viewers are exposed
to the opposition’s arguments, even if they disagree with them. In the algorithmic environment observed, parties can
target their “owned” issues exclusively to sympathetic demographics, insulating their base from counterarguments. This
suggests that digital microtargeting transforms issue ownership from a campaign tactic into a mechanism of epistemic
closure.
These conclusions should be interpreted in light of the limitations imposed by the Meta Ad Library API. The current
transparency tools only reveal basic targeting parameters, such as age, gender, and location, and omit the vast array of
behavioral and interest-based attributes used for profiling [65, 66]. Additionally, the data cannot distinguish between
targeting decisions made by campaign managers and those optimized automatically by Meta’s delivery algorithms.
This “black box” is a significant barrier to accountability. Without access to the precise logic of audience selection,
researchers cannot determine whether elections are being manipulated by malicious actors or merely optimized by
profit-driven algorithms.
This study contributes to the ongoing debate on the governance of the digital public sphere by providing a novel,
data-driven analysis of the impact of political advertising on social media on direct democracy. Although censoring
10

Capozzi A.
political ads entirely may be undesirable, maintaining the current level of secrecy is not an option. Empowering
users and researchers requires shifting from voluntary transparency to comprehensive data access. Citizens can only
move from being passive recipients of tailored messaging to active participants in a shared democratic process by
understanding how they are being targeted.
5 Materials and methods
This study relies on data from two main sources: the Swiss Federal Statistical Office1 and the Meta Ad Library API2.
The Federal Statistical Office provides detailed statistics related to referenda, including results by canton, participation
percentages, and full descriptions of referendum questions.
5.1 Meta Ad Library
The Meta Ad Library API discloses advertisements about social issues, election, or politics that were delivered on
Facebook or Instagram during the past seven years. Although the API allows for specifying search parameters, such as
limiting results to a specific country, all queries must contain keywords or author names. The following information
can be extracted for each advertisement: the publication date; the end time of the campaign; the textual content; and
the number of impressions (provided as an interval). The term “impressions” refers to non-unique visualizations. It
is also possible to access the campaign expenditure (again presented as an interval) and the audience’s demographic
profile, specifically their gender (male, female, or unknown) and age (categorized into seven buckets). In line with
existing literature [31], the midpoint of the interval’s boundaries is computed for values presented as ranges (expenditure
and impressions). For unbounded ranges, only the defined boundary is used. To quantify the extent of demographic
microtargeting, two statistical measures are employed. First, gender disparities are analyzed using the odds ratio (OR).
This metric measures the likelihood of an advertisement being shown to a male user versus a female user. An OR of 1.0
indicates a perfectly balanced gender distribution; values greater than 1.0 indicate a bias toward a male audience, while
values less than1.0indicate a bias toward a female audience. Second, differences in age targeting are evaluated using
the Wasserstein distance (WD), often referred to as the Earth Mover’s Distance. Unlike comparing simple averages, the
WD accounts for the entire shape of the probability distributions. It quantifies the minimum amount of “work” required
to transform one distribution into another. In the context of this study, the WD effectively represents the mean absolute
difference in years between the age profile of a specific party’s audience and that of the comparison group (e.g., the rest
of the dataset).
The collection is initiated using a broad set of election-related keywords (see Table 2) in German, French, and Italian
due to the API’s requirement for keyword- or author-based searches. This process yielded an initial corpus of 40,044
ads (22,494 from German keywords, 10,794 from French, and 6,756 from Italian) published between January 1, 2021,
and September 30, 2025. The API’s country filter includes advertisements displayed in Switzerland, even if they are
intended for a different audience. To create a Swiss-centric dataset, ads are further filtered to include only those for
which more than 50% of impressions come from users based in Switzerland. This reduces the dataset to 34,559 ads
from 2,246 unique pages, which received an estimated 560 million impressions and cost over CHF 4.5 million.
Although the API provides a page name (username) for each ad, this identifier is frequently ambiguous or does not
directly correspond to a particular political party, even when the content of the page clearly promotes a party’s agenda.
As shown in Figure 4, the 2023 federal elections represent the most significant activity peak in the dataset. For this
reason, the 1,224 pages that published at least one ad in the 30 days preceding the federal election are manually labeled
to establish whether they are related to a specific party. This process identified 943 pages that could be directly attributed
to a political party, while the remaining 281 pages belong to entities such as media organizations (newspapers and daily
newspapers), NGOs, neighborhood committees, and non-partisan referendum groups. Of the 943 political pages, 17
major parties and smaller entities (e.g., municipal parties and civic lists) are identified. However, only six parties —
SVP, SP, FDP, Die Mitte, GRÜNE, and GLP — play a dominant role in the advertising landscape, accounting for 95%
of all impressions. Collectively, these parties also secured 91.84% of the votes in the 2023 federal elections. Tables 3, 4,
and 5 provide detailed statistics on impressions, volume, and ad expenditure broken down by party and language.
5.2 Content Annotation
The filtered dataset of 34,559 ads is cleaned to remove entries with blank or duplicate textual content, resulting in
13,324 unique ads. The paper presents two analyses of the textual content: one focused on referenda, and the other on
the 2023 federal elections.
1https://abstimmungen.admin.ch/en/overview
2https://www.facebook.com/ads/library/api/
11

Capozzi A.
5.2.1 Referenda
The first step is to identify which advertisements relate to one of the 42 referenda held between January 2021 and
October 2025. The process begins by filtering the ads to include only those containing at least 10 words and published
within 30 days of the referendum. This procedure results in 9,118 ads. The second step involves prompting GPT-4o
with the text of the ad campaign to establish whether it is related to a referendum and, if so, what stance the campaign is
taking. In addition, the model is provided with the official title and description of each referendum, as published by the
Federal Statistical Office. The model checkpoint is “gpt-4o-2024-08-06”, and the API queries are executed on October
8, 2025. The task is structured as a few-shot query, and the output for each ad is a Boolean parameter indicating whether
the ad is relevant to the referendum. If an ad is deemed relevant, the output includes also the referendum’s title and
the ad’s stance (Yes, No, or Neutral). Manual label verification is performed on a random sample of 100 ads, and this
verification revealed an accuracy rate of 100%.
To evaluate the intensity of advertising activity, a Wilcoxon signed-rank test is employed to determine if there is
a significant increase in the number of ads and expenditure in the period preceding a referendum. The Wilcoxon
signed-rank test is a non-parametric statistical hypothesis test used to compare two related samples, matched samples,
or repeated measurements on a single sample to assess whether their population mean ranks differ. In this study, it is
used to compare the 30-day “pre-referendum” window against the 30-day “post-referendum” window for each vote.
This test is particularly suitable because it does not assume a normal distribution of the data, which is necessary given
the highly skewed nature of advertising impressions and expenditure.
However, the Wilcoxon test only identifies a difference between two time blocks and does not account for external
confounding factors such as seasonality, day-of-the-week effects, or long-term growth trends in the dataset. To isolate
the specific impact of referendum proximity, a Generalized Additive Model (GAM) is deployed. A GAM is a flexible
regression technique that extends Generalized Linear Models by allowing the linear predictor to depend on unknown
smooth functions of some predictor variables. By using smoothers for the “days until referendum”, the day of the
year, and the general trend, the model can separate the temporary spike caused by a political campaign from recurring
temporal patterns.
5.2.2 Federal Election
The second analysis focuses on the 2023 federal elections. Unlike a referendum, which addresses one or a few political
issues, federal elections involve political parties promoting broader agendas. Therefore, it is necessary to not only
identify election-relevant ads but also determine the specific topic(s) they cover. Consistent with the previous task, only
ads with at least 10 words published within 30 days before the federal election are selected. The model checkpoint and
the API query date are the same of the previous task. The model’s output includes a Boolean parameter identifying
whether the ad is relevant to the federal election, as well as up to three English keywords related to the ad’s topic. This
initial extraction process yielded a large set of 739 unique keywords, which require consolidation into fewer categories.
To this end, each keyword is encoded into a semantic vector using OpenAI’s state-of-the-art text-embedding-3-large
model. These vectors are then clustered into 25 topics using the K-Means clustering algorithm [67]. This unsupervised
method partitions the semantic vectors into K= 25 distinct clusters by iteratively assigning each data point to the
nearest centroid, thereby minimizing the within-cluster variance. To ensure reliability, qualitative validation is performed
on a random subset of 100 ads. In this review, human annotation agreed with model-generated keywords in 96% of the
cases.
To addressRQ3.b, a multinomial logistic regression model is employed to predict the political party responsible for a
given ad. This method generalizes binary logistic regression to multi-class classification problems by using the softmax
function to model the probability distribution overK possible outcomes (parties). For a given input vector x (containing
demographic or topic features), the probability that the ad belongs to partykis given by:
P(y=k|x) = ewT k x PK
j=1 ewT j x (1)
where wk is the weight vector associated with class k. Ads are weighted according to their total number of impressions
to ensure that ads with a larger reach have a proportionally larger impact on the model’s parameters.
A multinomial logistic regression model provides interpretable coefficients that reveal the relationship between specific
features (e.g., a specific topic) and the likelihood of an ad originating from a specific party. An ablation study is
conducted to evaluate feature importance using three configurations: only demographic features, only topic features,
and a combination of the two.
The model’s performance is evaluated using the Area Under the Receiver Operating Characteristic curve (AUC ROC).
The ROC curve plots the true positive rate (sensitivity) against the false positive rate (1-specificity) at various threshold
12

Capozzi A.
settings. The AUC represents the probability that the model ranks a randomly chosen positive instance higher than a
randomly chosen negative instance. Since this is a multi-class problem, the AUC is calculated using a One-vs-Rest
strategy, where the performance for each party is evaluated against all other parties combined. An AUC score of 0.5
corresponds to random guessing, indicating a lack of discriminative ability. In contrast, a score of 1.0 signifies perfect
classification. To better understand the model’s specific strengths and weaknesses, the recall and precision confusion
matrices are also analyzed. Recall quantifies the model’s ability to correctly identify all ads belonging to a specific
party (True Positive Rate). Precision, on the other hand, measures the accuracy of the model’s positive predictions for a
given party (Positive Predictive Value).
A multinomial logistic regression model provides interpretable coefficients that reveal the relationship between specific
features (e.g., a specific topic) and the likelihood of an ad originating from a specific party. An ablation study is
conducted to evaluate feature importance using three configurations: only demographic features, only topic features,
and a combination of the two.
The model’s performance is evaluated using the Area Under the Receiver Operating Characteristic curve (AUC ROC).
The ROC curve plots the true positive rate (sensitivity) against the false positive rate (1-specificity) at various threshold
settings. The AUC represents the probability that the model ranks a randomly chosen positive instance higher than a
randomly chosen negative instance. Since this is a multi-class problem, the AUC is calculated using a One-vs-Rest
strategy, where the performance for each party is evaluated against all other parties combined. An AUC score of 0.5
corresponds to random guessing, indicating a lack of discriminative ability. In contrast, a score of 1.0 signifies perfect
classification. To better understand the model’s specific strengths and weaknesses, the recall and precision confusion
matrices are also analyzed. Recall quantifies the model’s ability to correctly identify all ads belonging to a specific
party (True Positive Rate). Precision, on the other hand, measures the accuracy of the model’s positive predictions for a
given party (Positive Predictive Value).
6 Acknowledgments
I thank Dr. Dirk Helbing for fruitful discussions.
Data Availability
Data and code are available in the Zenodo repository athttps://doi.org/10.5281/zenodo.18256330.
7 Supplementary Material
Table 2: Thematic Keyword Groups for Data Collection
English Theme German Keywords Italian Keywords French Keywords
To vote / To elect “wählen”, “wähle”, “wählen wir” “votare”, “vota”, “votiamo”, “voter”, “vote”, “votons”,
“eleggere”, “eleggi”, “eleggiamo” “élire”, “élis”, “élisons”
Election(s) / V ote(s) “Wahl”, “Wahlen” “elezione”, “elezioni”, “élection”, “élections”,
“votazioni”, “voto” “votes”, “vote”
Poll / Ballot “Abstimmungen”, “Abstimmung”(n/a) (n/a)
Referendum “Referendum” “referendum” “référendum”
Electoral Campaign “Wahlkampf”, “Wahlkampagne” “campagna elettorale” “campagne électorale”
Electoral Round “Wahlgang” “turno elettorale” “tour électoral”
Counting / Tally “Auszählung” “scrutinio” “scrutin”
References
[1] Kathleen Hall Jamieson.Dirty Politics. Oxford University Press, 09 1992.
[2] JEAN BLONDEL. The politics of switzerland: Continuity and change in a consensus democracy – by h. kriesi
and a. trexsel.JCMS: Journal of Common Market Studies, 47(4):931–932, 2009.
13

Capozzi A.
Table 3: Impressions by party and language
SP GRÜNE GLP Die Mitte FDP SVP
All 90.0M 55.9M 20.3M 20.3M 49.9M 45.4M
DE 59.4M 37.1M 13.8M 14.7M 27.6M 34.8M
FR 18.0M 15.6M 5.5M 3.8M 19.2M 6.6M
IT 12.6M 3.2M 1.0M 1.8M 3.1M 4.0M
Table 4: Number of ads by party and language
SP GRÜNE GLP Die Mitte FDP SVP
All 3.2K 2.6K 1.4K 1.4K 3.0K 2.5K
DE 2.1K 1.7K 1.1K 1.0K 2.0K 2.1K
FR 0.7K 0.7K 0.2K 0.3K 0.9K 0.2K
IT 0.4K 0.1K 0.1K 0.1K 0.1K 0.2K
Table 5: Expenditure on ads by party and language
SP GRÜNE GLP Die Mitte FDP SVP
All 758.4K 353.1K 157.6K 188.5K 372.7K 353.0K
DE 484.2K 229.1K 113.9K 138.7K 226.1K 286.9K
FR 149.5K 103.5K 37.9K 39.4K 132.2K 39.4K
IT 124.7K 20.5K 5.8K 10.3K 14.4K 26.6K
Table 6: Wilcoxon signed-rank test of ad views 30 days pre- and post-referendum (p <0.001for all tests).
Impressions Expenditure
All 69456 68337
DE 62227 64002
FR 61751 58278
IT 35867 33361
[3] Frederik J. Zuiderveen Borgesius, Judith Moller, Sanne Kruikemeier, Ronan Fathaigh, Kristina Irion, Tom Dobber,
Balazs Bodo, and Claes de Vreese. Online political microtargeting: Promises and threats for democracy.Utrecht
Law Review, 14(1):82–96, fe 2018.
[4] Almog Simchon, Matthew Edwards, and Stephan Lewandowsky. The persuasive effects of political microtargeting
in the age of generative artificial intelligence.PNAS Nexus, 3(2):pgae035, 01 2024.
[5] Ben M. Tappin, Chloe Wittenberg, Luke B. Hewitt, Adam J. Berinsky, and David G. Rand. Quantifying the
potential persuasive returns to political microtargeting.Proceedings of the National Academy of Sciences,
120(25):e2216261120, 2023.
[6] Arthur Capozzi, Gianmarco De Francisci Morales, Yelena Mejova, Corrado Monti, and André Panisson. The
thin ideology of populist advertising on facebook during the 2019 eu elections. InProceedings of the ACM
Web Conference 2023, WWW ’23, page 2852–2862, New York, NY , USA, 2023. Association for Computing
Machinery.
[7] Dominik Bär, Nicolas Pröllochs, and Stefan Feuerriegel. The role of social media ads for election outcomes:
Evidence from the 2021 german election.PNAS Nexus, 4(3):pgaf073, 03 2025.
[8] Uwe Serdült.Referendums in Switzerland. Palgrave Macmillan UK, London, 2014.
[9] Robert M Bond, Christopher J Fariss, Jason J Jones, Adam DI Kramer, Cameron Marlow, Jaime E Settle,
and James H Fowler. A 61-million-person experiment in social influence and political mobilization.Nature,
489(7415):295–298, 2012.
[10] Robert Epstein and Ronald E. Robertson. The search engine manipulation effect (seme) and its possible impact on
the outcomes of elections.Proceedings of the National Academy of Sciences, 112(33):E4512–E4521, 2015.
14

Capozzi A.
[11] Orestis Papakyriakopoulos, Severin Engelmann, and Amy Winecoff. Upvotes? downvotes? no votes? understand-
ing the relationship between reaction mechanisms and political discourse on reddit. InProceedings of the 2023
CHI Conference on Human Factors in Computing Systems, CHI ’23, New York, NY , USA, 2023. Association for
Computing Machinery.
[12] Yu-Hao Lee and Gary Hsieh. Does slacktivism hurt activism? the effects of moral balancing and consistency in
online activism. InProceedings of the SIGCHI Conference on Human Factors in Computing Systems, CHI ’13,
page 811–820, New York, NY , USA, 2013. Association for Computing Machinery.
[13] Kelly Williams Nagel. Make america meme again: The rhetoric of the alt-right.Quarterly Journal of Speech,
106(2):216–219, 2020.
[14] Yelena Mejova, Arthur Capozzi, Corrado Monti, and Gianmarco De Francisci Morales. Narratives of war:
Ukrainian memetic warfare on twitter.Proc. ACM Hum.-Comput. Interact., 9(2), 2025.
[15] Faye Margarette G. De Leon and Rachelle Ballesteros-Lintao. The rise of meme culture: Internet political memes
as tools for analysing philippine propaganda.Journal of Critical Studies in Language and Literature, 2(4):1–13,
May 2021.
[16] Simon P. Anderson and Bruno Jullien. Chapter 2 - the advertising-financed business model in two-sided media
markets. In Simon P. Anderson, Joel Waldfogel, and David Strömberg, editors,Handbook of Media Economics,
volume 1 ofHandbook of Media Economics, pages 41–90. North-Holland, 2015.
[17] Tim O’Reilly, Ilan Strauss, and Mariana Mazzucato. Algorithmic attention rents: A theory of digital platform
market power.Data & Policy, 6:e6, 2024.
[18] Dezhi Ran, Weiqiang Zheng, Yunqi Li, Kaigui Bian, Jie Zhang, and Xiaotie Deng. Revenue and user traffic
maximization in mobile short-video advertising. AAMAS ’22, page 1092–1100, Richland, SC, 2022. International
Foundation for Autonomous Agents and Multiagent Systems.
[19] Katharine Dommett and Sam Power. The political economy of facebook advertising: Election spending, regulation
and targeting online.The Political Quarterly, 90(2):257–265, 2019.
[20] Muhammad Ali, Piotr Sapiezynski, Aleksandra Korolova, Alan Mislove, and Aaron Rieke. Ad delivery algorithms:
The hidden arbiters of political messaging. InProceedings of the 14th ACM International Conference on Web
Search and Data Mining, WSDM ’21, page 13–21, New York, NY , USA, 2021. Association for Computing
Machinery.
[21] Xiaotong Chu, Rens Vliegenthart, Lukas Otto, Sophie Lecheler, Claes de Vreese, and Sanne Kruikemeier. Do
online ads sway voters? understanding the persuasiveness of online political ads.Political Communication,
41(2):290–314, 2024.
[22] Vera Sosnovik and Oana Goga. Understanding the complexity of detecting political ads. WWW ’21, page
2002–2013, New York, NY , USA, 2021. Association for Computing Machinery.
[23] David Karpf.Analytic Activism: Digital Listening and the New Political Strategy. Oxford University Press, 01
2017.
[24] André Grow, Daniela Perrotta, Emanuele Del Fava, Jorge Cimentada, Francesco Rampazzo, Sofia Gil-Clavel,
Emilio Zagheni, René D. Flores, Ilana Ventura, and Ingmar Weber. Is facebook’s advertising data accurate enough
for use in social science research? insights from a cross-national online survey.Journal of the Royal Statistical
Society: Series A (Statistics in Society), 185(S2):S343–S363, 2022.
[25] Alexis C Madrigal. What facebook did to american democracy.The Atlantic, 2017.
[26] Adam Entous, Craig Timberg, and Elizabeth Dwoskin. Russian operatives used facebook ads to exploit america’s
racial and religious divisions.Washington Post, 25, 2017.
[27] Ritam Dutt, Ashok Deb, and Emilio Ferrara. “senator, we sell ads”: Analysis of the 2016 russian facebook ads
campaign. InAdvances in Data Science, pages 151–168, Singapore, 2019. Springer Singapore.
[28] J. Nathan Matias, Austin Hounsel, and Nick Feamster. Software-supported audits of decision-making systems:
Testing google and facebook’s political advertising policies.Proc. ACM Hum.-Comput. Interact., 6(CSCW1),
2022.
[29] Dominik Bär, Francesco Pierri, Gianmarco De Francisci Morales, and Stefan Feuerriegel. Systematic discrepancies
in the delivery of political ads on facebook and instagram.PNAS Nexus, 3(7):pgae247, 06 2024.
[30] Yelena Mejova and Kyriaki Kalimeri. Covid-19 on facebook ads: Competing agendas around a public health
crisis. InProceedings of the 3rd ACM SIGCAS Conference on Computing and Sustainable Societies, COMPASS
’20, page 22–31, New York, NY , USA, 2020. Association for Computing Machinery.
15

Capozzi A.
[31] Arthur Capozzi, Gianmarco De Francisci Morales, Yelena Mejova, Corrado Monti, André Panisson, and Daniela
Paolotti. Clandestino or rifugiato?anti-immigration facebook ad targeting in italy. InProceedings of the 2021
CHI Conference on Human Factors in Computing Systems, CHI ’21, New York, NY , USA, 2021. Association for
Computing Machinery.
[32] Arthur Capozzi, Gianmarco de Francisci Morales, Yelena Mejova, Corrado Monti, André Panisson, and Daniela
Paolotti. Facebook ads: politics of migration in italy. InInternational Conference on Social Informatics, pages
43–57. Springer, 2020.
[33] Lorena Cano-Orón, Dafne Calvo, Guillermo López García, and Tomás Baviera. Disinformation in facebook ads
in the 2019 spanish general election campaigns.Media and Communication, 9(1):217–228, 2021.
[34] Marlène Gerber and Marc Bühlmann. Do ads add up? the impact of parties’ advertisements on the stability of
vote choice at the swiss national elections 2011.Swiss Political Science Review, 20(4):632–650, 2014.
[35] Guillaume Zumofen and Marlène Gerber. Effects of issue-specific political advertisements in the 2015 parliamen-
tary elections of switzerland.Swiss Political Science Review, 24(4):442–463, 2018.
[36] Michaela Fischer. From newspapers to social media? changing dynamics in swiss direct democratic campaigns.
Swiss Political Science Review, 29(4):465–478, 2023.
[37] Maud Reveilhac and Davide Morselli. The impact of social media use for elected parliamentarians: Evidence from
politicians’ use of twitter during the last two swiss legislatures.Swiss Political Science Review, 29(1):96–119,
2023.
[38] Daniel M Warner. Direct democracy: The right of the people to make fools of themselves; the use and abuse of
initiative and referendum, a local government perspective.Seattle UL Rev., 19:47, 1995.
[39] Elisabeth R. Gerber.The Populist Paradox: Interest Group Influence and the Promise of Direct Legislation.
Princeton University Press, 1999.
[40] Bruno S. Frey. Direct democracy: Politico-economic lessons from swiss experience.The American Economic
Review, 84(2):338–342, 1994.
[41] Wolf Linder and Sean Mueller.Swiss democracy: Possible solutions to conflict in multicultural societies. Springer
Nature, 2021.
[42] Alois Stutzer and Bruno S Frey. Political participation and procedural utility: An empirical study.European
Journal of Political Research, 45(3):391–418, 2006.
[43] Lars P. Feld and Marcel R. Savioz. Direct democracy matters for economic performance: An empirical investiga-
tion.Kyklos, 50(4):507–538, 1997.
[44] Bruno S. Frey and Alois Stutzer. Happiness, economy and institutions.The Economic Journal, 110(466):918–938,
2000.
[45] Yannis Papadopoulos. How does direct democracy matter? the impact of referendum votes on politics and
policy-making.West European Politics, 24(2):35–58, 2001.
[46] Bundesamt für Statistik (BFS). Main languages, 1970-2023. Web, Feb 2023.
[47] Bundesamt für Statistik (BFS). Evolution of religious landscape. Web, Jan 2025.
[48] Bundesamt für Statistik (BFS). Three new agglomerations and 10 more towns than 10 years ago: urbanisation
continues in switzerland. Web, Mar 2024.
[49] BFS.PIL in aumento in tutti i Cantoni nel 2022. Number 30665780. Bundesamt für Statistik (BFS), Neuchâtel,
Mar 2024.
[50] F Sager and C Zollinger.The Swiss political system in comparative perspective, page 27–42. Number 7272 in
Routledge Advances in European Politics. Routledge, 2011.
[51] Abraham Diskin, André Eschet-Schwarz, and Dan S. Felsenthal. Homogeneity, heterogeneity and direct democ-
racy: The case of swiss referenda.Canadian Journal of Political Science, 40(2):317–342, 2007.
[52] Hanspeter Kriesi. Direct democracy: the swiss experience. InEvaluating Democratic Innovations, pages 39–55.
Routledge, 2012.
[53] Swiss Federal Statistical Office (FSO). National council elections 2023: Party strength, number of seats, and voter
share, 2023. Data table, identifier: je-e-01.02.01.01.
[54] Shaun Bowler and Todd Donovan.Demanding Choices: Opinion, Voting, and Direct Democracy. University of
Michigan Press, 1998.
16

Capozzi A.
[55] Elisabeth R. Gerber. Pressuring legislatures through the use of initiatives: Two forms of indirect influence. In
Shaun Bowler, Todd Donovan, and Caroline J. Tolbert, editors,Citizens as Legislators: Direct Democracy in the
United States. Ohio State University Press, 1998.
[56] European Parliament. Youth and democracy in the european union: Eurobarometer survey. Flash Eurobarometer
545, European Union, May 2024. Accessed: 2025-06-17.
[57] Daniel Oesch and Line Rennwald. The class basis of switzerland’s cleavage between the new left and the populist
right.Swiss Political Science Review, 16(3):343–371, 2010.
[58] Daniele Mantegazzi. The geography of political ideologies in switzerland over time.Spatial Economic Analysis,
16(3):378–396, 2021.
[59] Marco R. Steenbergen. Decomposing the vote: Individual, communal, and cantonal sources of voting behavior in
switzerland.Swiss Political Science Review, 16(3):403–424, 2010.
[60] Stefano Camatarri, Adrian Favero, Marta Gallina, and Lewis Luartz. The electoral behaviour of voters with
migration backgrounds and natives at the 2015 and 2019 swiss national elections. two completely different stories?
Swiss Political Science Review, 28(2):319–337, 2022.
[61] John R. Petrocik. Issue ownership in presidential elections, with a 1980 case study.American Journal of Political
Science, 40(3):825–850, 1996.
[62] Ian Budge and Dennis J Farlie.Explaining and predicting elections: Issue effects and party strategies in
twenty-three democracies. Taylor & Francis, 2025.
[63] Pablo Amorós and M Socorro Puy. Issue convergence or issue divergence in a political campaign?Public Choice,
155(3):355–371, 2013.
[64] Éric Bélanger and Bonnie M. Meguid. Issue salience, issue ownership, and issue-based vote choice.Electoral
Studies, 27(3):477–491, 2008.
[65] Emilio Zagheni, Ingmar Weber, and Krishna Gummadi. Leveraging facebook’s advertising platform to monitor
stocks of migrants.Population and Development Review, 43(4):721–734, 2017.
[66] Matheus Araujo, Yelena Mejova, Ingmar Weber, and Fabricio Benevenuto. Using facebook ads audiences for
global lifestyle disease surveillance: Promises and limitations. WebSci ’17, page 253–257, New York, NY , USA,
2017. Association for Computing Machinery.
[67] James B McQueen. Some methods of classification and analysis of multivariate observations. InProc. of 5th
Berkeley Symposium on Math. Stat. and Prob., pages 281–297, 1967.
17
