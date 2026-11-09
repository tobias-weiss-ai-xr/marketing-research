---
title: AI-based matching improves refugee employment in a double-blind randomized trial
url: https://arxiv.org/abs/2609.35448
category: digital-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Kirk Bansak
- Jens Hainmueller
- Dominik Hangartner
- Jeremy Ferwerda
- Elisabeth Paulson
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.35448
pages: 58
chars: 121077
fetched_at: '2026-11-08T13:20:23+00:00'
kb_version: 1
---

# AI-based matching improves refugee employment in a double-blind randomized trial

AI-based matching improves refugee employment in a
double-blind randomized trial
Kirk Bansak1,2,*, Jens Hainmueller2,3,*,†, Dominik Hangartner4,5,*,
Jeremy Ferwerda2,6, Elisabeth Paulson2,7, Angie Delevoye2,
Nicholas Adams-Cohen2, Ashwin Ramaswami2, Selina Kurer4,5,
Joelle Pianzola4, and Michael Hotard2
*These authors jointly led this project.
†Corresponding author: jhain@stanford.edu
1Department of Political Science, University of California, Berkeley, Berkeley, CA, USA
2Immigration Policy Lab, Stanford University, Stanford, CA, USA
3Department of Political Science, Stanford University, Stanford, CA, USA
4Immigration Policy Lab, ETH Zurich, Zurich, Switzerland
5Public Policy Group, ETH Zurich, Zurich, Switzerland
6Department of Government, Dartmouth College, Hanover, NH, USA
7Technology and Operations Management Unit, Harvard Business School, Boston, MA, USA
Abstract
Refugee integration is a central policy challenge for host countries, and where governments ini-
tially place refugees shapes their integration trajectories. Yet placement officers often have limited
information about where each case is most likely to succeed. Algorithmic refugee matching uses
administrative data, machine learning, and constrained optimization to recommend employment-
optimized placements in real time as cases arrive, with human placement officers retaining final
authority. Between January 2020 and June 2023, the Swiss State Secretariat for Migration ran-
domly assigned about 2,000 refugee cases to receive a canton recommendation either algorithmically
optimizedforemploymentordrawntoapproximateexistingprocedures, with placementofficersand
refugees blinded to assignment. The two arms used identical but separate canton and origin-group
quotas, so gains reflect better refugee-canton matching rather than reallocation toward stronger
labor markets. The trial began just before the COVID-19 pandemic shifted labor-market condi-
tions. For the pre-registered primary outcome—the share of months employed during the first three
years—the pooled intention-to-treat (ITT) estimate across the 2020–2023 placement cohorts was
+2.2percentage points (≈10%of the 22.3% control mean; 95% CI [+0.05,+4.33]), rising to+3.9
pp (≈17%; [+1.11,+6.68]) for the post-COVID 2022–2023 cohorts. Effects grew over time: at 36
months, the pooled ITT on the employment rate was+5.2pp (≈11%; 95% CI [+1.10,+9.25])—
comparable to the gains from hundreds of hours of intensive language training. Overall, the results
provide rare field evidence that AI-based decision support can improve high-stakes public-sector
allocation, offering a scalable, low-cost way to raise refugee employment.
1
arXiv:2609.35448v1  [econ.GN]  28 Sep 2026

UNHCR projects that 136 million people will be forcibly displaced or stateless worldwide
by the end of 20261. In host countries that grant refugees protection, their labor-market
integration is a central policy challenge. Refugees face many barriers to employment, and
integration is often slow. One study, for instance, showed that across twenty European coun-
tries refugees are about twelve percent less likely to be employed than otherwise comparable
migrants, a gap that persists for ten to fifteen years after arrival2. Low employment is costly
for refugees, who depend on limited amounts of public assistance, as well as for host societies,
which bear welfare costs and forgo the tax revenue employment would generate.
Research consistently identifies the early period after a refugee’s arrival in a host country,
often called the “integration window,” as decisive. Conditions and interventions in the
first months and years after arrival have lasting effects on refugees’ trajectories, making
early action more cost-effective than later remediation3,4. Yet interventions aimed at this
window have yielded inconsistent results5,6. Intensive language training, wage subsidies,
and bundled employment programs can improve employment prospects, but they require
substantial investment7–10. Lighter-touch programs, on the other hand, often have limited
or no lasting effects11,12. Cost-effective and scalable interventions remain elusive.
A separate stream of research highlights the importance of where refugees are settled.
In many destination countries, refugees are assigned to regions or municipalities according
to administrative distribution rules, such as population-based quotas, rather than based
on where they are most likely to succeed. A large body of quasi-experimental evidence
shows that these initial placement decisions can have large and persistent effects on refugees’
employment and earnings13–19. Yet existing allocation systems rarely leverage these place ef-
fects, because placement officers typically have limited information about where each refugee
would fare best while also needing to satisfy complex distribution requirements.
Addingalgorithmicrecommendationstotheplacementprocessoffersthepotentialtocap-
ture these gains within existing admissions policies, quotas, and service constraints. First in-
troduced by Bansak et al.20, outcome-based algorithmic refugee matching combines machine
2

learning with constrained optimization to achieve precisely that goal. Under this frame-
work, predictive models estimate how each refugee would fare across possible locations, and
an optimization step generates recommended matches between refugees and available slots
to maximize predicted aggregate employment while respecting capacity limits and other as-
signment rules. Holding geographic quotas fixed, the approach does not direct more refugees
toward stronger labor markets; instead, it helps placement officers identify better-fitting lo-
cations for individual refugees. Because it relies on routinely collected administrative data
and operates within the existing placement process, it has low marginal costs. The approach
is also advisory by design in that it solves a complex placement problem that officers could
not practically evaluate case by case, recommends a location, and leaves officers with final
authority to incorporate information not captured in the administrative data.
Backtests using historical placement data suggest potential employment gains, and tools
based on this approach have been piloted in Switzerland, the Netherlands, the United States,
and Canada21. Subsequent research has extended these methods with online assignment and
dynamic resource balancing, welfare and fairness constraints, and learning under distribution
shift and across small locations22–29. Yet every published estimate of the approach’s benefits
rests on retrospective backtests, which cannot fully account for implementation frictions,
staff responses, noncompliance, general-equilibrium displacement, or changing conditions
between training and deployment. Whether these estimated gains carry over to real-world
implementation therefore remains a central empirical question.
This study reports, to our knowledge, the first randomized controlled trial of algorithmic
refugee matching, conducted in partnership with the Swiss State Secretariat for Migration
(SEM), the federal authority responsible for Switzerland’s asylum system. The SEM was the
first government agency to adopt these methods in the refugee placement setting, deploying
and testing an early generation of a tool named GeoMatch. More broadly, the trial provides
rare field evidence on whether AI decision-support systems built on predictive models can
improve high-stakes public-sector decisions.
3

Between January 2020 and June 2023, the SEM randomly assigned eligible refugee cases
to receive either an algorithmic recommendation (treatment arm) or a status quo recom-
mendation (control arm) with equal probability. The algorithmic recommendation selected
the canton predicted to maximize aggregate employment across cases, subject to strict na-
tional origin distribution quotas across cantons. The status quo recommendation randomly
selected a canton without using employment predictions, subject to an identical but sepa-
rate copy of the quotas, so that the two arms never competed for the same allocation slots.
Both placement officers and refugees were blinded to treatment status. The algorithm was
trained and trial outcomes were analyzed using SEM administrative register data linked to
employment histories. Treatment effects are estimated at the level of the refugee case, which
may comprise a family or an individual and is the unit of randomization and placement.
The primary outcome is the mean share of months employed among adult case members
during the first three years following placement in their assigned canton. To characterize
how effects evolve within this window, the analysis also examines point-in-time employment
across the follow-up period, including whether any adult in the case is employed 36 months
after placement. Consistent with the target in the pre-analysis plan (PAP)30, the analysis
sample includes the first 2,000 cases with complete three year employment outcomes in order
of assignment; results are nearly identical when all 2,046 complete cases through June 2023
are included (Supplementary Information, Sec. S7).
Attrition was low and balanced: 2.5% of control-arm adults and 2.3% of treatment-
arm adults were no longer observed at three years (Supplementary Information, Sec. S4).
Baseline covariates were balanced across treatment arms (F11,1,999 = 0.49,p= 0.91). The
mirrored quota design also produced balance across arms in both canton placements and the
joint distribution of canton and origin group (χ2 testsp>0.99; Supplementary Information,
Table S3). Thus, in this trial, the treatment contrast isolates gains from improved refugee-
canton matching while holding the aggregate canton and origin-group allocation fixed.
The primary analysis reports intention-to-treat (ITT) effects of assignment to receive a
4

GeoMatch recommendation rather than a status quo recommendation. It also considers lo-
cal average treatment effects (LATE) for placement in the GeoMatch-recommended canton,
taking into account noncompliance with recommendations. The analyses use pre-registered
covariate-adjusted ordinary least squares (OLS) and instrumental variables (IV) regression
specifications (see Methods). Alternative estimators and adjustment sets yield nearly iden-
tical results (Figure 1). Secondary and diagnostic analyses examine alternative employment
measures, secondary migration, placement ranks, and distributional effects.
The trial provides a conservative test, for reasons anticipated in the PAP and detailed
in the Methods. First, the prediction stage of the algorithm used a sparse predictor set
drawn from the government’s administrative register and selected by the SEM for deploy-
ment. The Swiss register data did not include standard human capital variables that are
known to be predictive of employment and are usually available in other contexts, such as
education, occupation, prior work experience, and host-language proficiency. Second, to
preserve implementation fidelity and keep the treatment definition fixed, the model speci-
fication and optimization procedure were not changed as newer matching methods became
available. Third, the placement process was tightly constrained by Switzerland’s cantonal
proportionality key and by origin-group balancing rules. These constraints limited the fea-
sible assignment set and therefore the scope for the algorithm to exploit location-specific
synergies, especially those involving ethnic networks or language region matches17–19. In
addition, the mirrored quota design meant that the algorithm optimized over only about
half of the caseload and its slots, further shrinking the feasible match set relative to a full-
scale deployment. Finally, the trial launched in January 2020, just before the COVID-19
pandemic disrupted cross-border mobility, asylum processing, and labor markets. This cre-
ated a gap between the data available for model training and the conditions in which the
tool was used. Prior scholarship has documented how COVID-19 disruptions led to abrupt
distribution shifts and thereby created challenges for prediction and forecasting across medi-
cal, economic, business, and other domains31–36. These disruptions likely made it harder for
5

models trained on pre-pandemic data to predict employment for the trial’s early cohorts.
Despite these challenges, the trial shows positive pooled gains of roughly 10%, with larger
gains of roughly 17–21% for the post-COVID cohorts whose integration windows unfolded
after the labor market had mostly normalized—a pattern consistent with the algorithm’s
predictions realigning with realized outcomes after the pandemic. Treatment effects also
grow over follow-up. At 36 months after placement, when refugee employment becomes
economically meaningful, algorithmically guided placement raised the share of cases with
any adult employed by roughly 11–12%—an effect comparable to the gains from hundreds
of hours of intensive language training (see Discussion).
Results
Main Treatment Effects
Table 1 reports the ITT and LATE estimates for the pre-registered primary outcome—the
share of months employed over the first three years after placement—aggregated at the case
level as the mean across adult case members. Pooled across all placement cohorts, the case-
level ITT estimate is+2.2percentage points (pp) on a control mean of22.3%of months
employed, a relative increase of≈10%, with a 95% confidence interval from+0.05to+4.33
pp andp= 0.045(N= 2,000cases; Table 1). The case-level LATE is+2.5pp (≈11%,
95% CI[+0.05,+4.93]pp,p= 0.046). The LATE first stage is strong: randomization
increased placement in the GeoMatch-recommended canton by approximately 88 pp (partial
F= 7,107; Supplementary Information, Table S5).
The pooled estimates may, however, mask cohort heterogeneity associated with the
COVID-19 disruption. The analysis therefore reports non-prespecified comparisons across
placementcohorts. GeoMatchwasinitiallytrainedonpre-pandemicadministrativedata, and
the PAP warned that COVID-era labor markets might not reflect the relationships learned
from those data30. The 2020 launch cohort began its integration window during the acute
6

Table 1:Treatment Effects on Three Year Employment.
Sample EstimandNCtrl. mean (%)β(pp) Gain 95% CI (pp)p
All cohorts (2020–2023) ITT 2,000 22.3+2.19 +9.8% [+0.05,+4.33]0.045
LATE 2,000 22.3+2.49 +11.1% [+0.05,+4.93]0.046
Excluding peak COVID (2021–2023) ITT 1,709 22.0+2.71 +12.3% [+0.39,+5.03]0.022
LATE 1,709 22.0+3.11 +14.1% [+0.45,+5.77]0.022
Post-COVID (2022–2023) ITT 1,212 22.3+3.90 +17.5% [+1.11,+6.68]0.006
LATE 1,212 22.3+4.59 +20.6% [+1.35,+7.82]0.006
Notes:Estimates report ITT and LATE effects. The outcome is the mean share of months employed over
the first three years after placement among adult case members. ITT estimates capture access to a
GeoMatch algorithmic recommendation. LATE estimates capture initial placement in the
GeoMatch-recommended canton among compliers, instrumenting placement with randomization. Control
means are shown as percentages, and the effects in the column labeledβare in percentage points. The
column labeled Gain denotes the effect in terms of a percentage increase over the baseline, which is
calculated by dividing the percentage-point effect by the corresponding control mean. The “Excluding peak
COVID” row drops the 2020 launch cohort but retains the 2021 transition cohort and the post-COVID
cohorts. The “Post-COVID” row pools the 2022–2023 post-COVID cohorts.Ncounts the number of cases.
pandemic disruption, and the 2021 cohort remained heavily exposed during early integra-
tion. By contrast, the 2022–2023 cohorts mostly integrated after the disruption had passed
and COVID-related restrictions had been lifted (Supplementary Information, Sec. S3). Ta-
ble 1 accordingly reports estimates excluding the peak-COVID 2020 cohort and estimates
restricted to the post-COVID 2022–2023 cohorts.
Estimates are larger once the peak-COVID launch cohort is excluded: the case-level
ITT rises to+2.7pp (≈12%; 95% CI[+0.4,+5.0]pp,p= 0.022;N= 1,709cases) and
the LATE to+3.1pp (≈14%; 95% CI[+0.4,+5.8]pp,p= 0.022). In the post-COVID
2022–2023 cohorts, the ITT reaches+3.9pp (≈17%; 95% CI[+1.1,+6.7]pp,p= 0.006;
N= 1,212cases) and the LATE+4.6pp (≈21%; 95% CI[+1.4,+7.8]pp,p= 0.006).
In sum, algorithmic recommendations raised employment on the pre-registered primary
outcome, with gains roughly twice as large once labor markets had stabilized. A direct
comparison across eras supports this pattern. Specifically, the estimated treatment effect
is+4.6pp larger in the post-COVID 2022–2023 cohorts than in the COVID-era 2020–
2021 cohorts (treatment-by-era interactionp= 0.039with covariate adjustment,p= 0.070
unadjusted). Cohort-by-cohort estimates show the same progression—effects statistically
7

indistinguishable from zero in 2020 and 2021, and then effects that are positive, statistically
significant, andstableacrossthe2022and2023cohorts(SupplementaryInformation, Sec.S6,
Figs.S4andS6; Fig.S5showsthesameprogressionusingdouble/debiasedmachinelearning).
Robustness of the Main Estimates
Figure 1 shows that the estimates are stable across alternative specifications. The PAP-
primary specification adjusts for covariates by interacting treatment with mean-centered
covariates, following Lin37 (see Methods). The alternatives include the unadjusted and post-
double-selection estimators38, inverse-probability-weighted attrition correction, the same
specification without canton indicators, and an additive specification. For the LATE, the
analysis considers three definitions of treatment take-up: initial placement in the GeoMatch-
recommended canton, placement plus at least 18 months of residence in the recommended
canton, and the share of follow-up spent in the recommended canton. For all three analysis
samples, the resulting ITT and LATE estimates are virtually unchanged across specifica-
tions. The full set of estimates is reported in the Supplementary Information (Tables S5
and S6). Additional robustness checks show that the individual-level estimates are close to
the case-level estimates, with similar magnitudes, precision, and cohort patterns (Supple-
mentary Information, Table S7).
Effect Growth over Follow-up
Refugee labor-market integration typically progresses slowly in Switzerland and elsewhere
in Europe2–4, making it important to examine whether the effects of improved placement
grow with time since placement. Figure 2 traces the evolution of employment over follow-up
for the same cohort samples as Table 1. The left panels show the employment rate—the
share of cases with any adult employed—at quarterly intervals since placement, separately
by assignment arm. This point-in-time measure was not specified in the PAP but is built
from the same monthly employment indicators as the primary outcome. It also corresponds
8

Figure 1:Robustness of the Three Year Employment Effects.
All cohorts (2020−2023)
N = 2,000
Excluding peak COVID (2021−2023)
N = 1,709
Post−COVID (2022−2023)
N = 1,212
ITTLATE
0 2 4 6 8 0 2 4 6 8 0 2 4 6 8
xxPAP−primary Lin
xxLin, no canton indicatorsxxxxxx
xxAdditive adjustment
xxPDS LASSO
xxUnadjusted
xxAttrition IPW
Estimators:
xxInitial placement
xxPlaced and stayed 18+ months
xxShare of follow−up spent there
Treatment definitions
(recommended canton):
Treatment effect on 3−year employment (pp)
Primary ITT Primary LATE Supporting ITT Supporting LATE
Notes:The top panel shows ITT estimates for three year employment under alternative estimators. The
bottom panel shows LATE estimates under the alternative definitions of treatment take-up given in the
text. Red and blue points mark the primary ITT and LATE specifications; grey points show supporting
analyses. PDS denotes post-double-selection, and IPW denotes inverse-probability weighting. Columns
correspond to the three samples in Table 1. Points show estimates and bars show 95% confidence intervals.
Full estimates are reported in the Supplementary Information, Tables S5 and S6.
more closely to how employment is conventionally measured in labor economics.
Employment rises steadily from low levels in both arms, the two trajectories track each
other closely through the first year, and the treatment arm then pulls ahead, with the gap
widening through the end of follow-up. The right panels report the corresponding case-
level ITT and LATE estimates at six-month intervals. Across samples, point estimates
become larger at longer horizons. In the pooled sample, the ITT estimate is close to zero
at early horizons but grows to+5.2pp at 36 months (95% CI[+1.1,+9.2];≈11%of the
47.7% control share), with the corresponding LATE at+6.0pp (95% CI[+1.4,+10.6]) and
the post-COVID ITT reaching+5.5pp ([+0.2,+10.8]). A complementary analysis of the
share of months employed over the first one, two, and three years shows the same pattern
of increasing effects at both the case and individual levels (Supplementary Information,
Fig. S7). Overall, the estimated effects grow over follow-up rather than fading, and the
9

Figure 2:Employment Effects Grow Over Follow-up.
Post−COVID (2022−2023)
N = 1,212
Excluding peak COVID (2021−2023)
N = 1,709
All cohorts (2020−2023)
N = 2,000
6 12 18 24 30 36
0
10
20
30
40
50
0
10
20
30
40
50
0
10
20
30
40
50
Months since placement
Employment rate (%)
Treatment Control
Post−COVID (2022−2023)
N = 1,212
Excluding peak COVID (2021−2023)
N = 1,709
All cohorts (2020−2023)
N = 2,000
6 12 18 24 30 36
−5
0
5
10
15
−5
0
5
10
15
−5
0
5
10
15
Months since placement
Treatment effect (pp)
ITT LATE
Notes:Rows correspond to the three samples evaluated in Table 1. Left panels show the case employment
rate, by assignment arm, at quarterly horizons from 3 to 36 months after placement; shaded bands are
pointwise 95% intervals. Right panels report the corresponding case-level ITT and LATE estimates at
six-month intervals. Bars show 95% confidence intervals. Panel headers report the 36-month sample sizes.
The 36-month estimates are reported in the Supplementary Information, Table S9.
pooled estimates are largest at the longest observed horizon.
10

Distributional Analysis
The Supplementary Information presents empirical cumulative distribution functions
(ECDFs) of the primary three year employment outcome by assignment arm for the three
samples considered in Table 1 (Fig. S8). Across all three samples, the treatment ECDF lies
below the control ECDF over almost the entire support, with the largest separation in the
post-COVID sample. Two complementary distributional tests formally assess this pattern
(Supplementary Information, Table S10). First, a test for first-order stochastic dominance
(FOSD), based on the Barrett–Donald supremum statistic, asks whether the treatment
outcome distribution weakly dominates the control distribution, meaning that the treatment
ECDF is nowhere above the control ECDF39. The test fails to reject in all three samples
(allp≥0.81), indicating that the data are statistically consistent with treatment FOSD
over control. Second, a one-sided Kolmogorov–Smirnov test rejects distributional equality
in favor of a treatment-favoring shift in the pooled sample (D+ = 5.41pp,p= 0.035), the
sample excluding 2020 (D+ = 6.47pp,p= 0.018), and the post-COVID sample (D + = 8.76
pp,p= 0.007). Overall, the increasingly pronounced distributional shift mirrors the pattern
in the mean effects. From a social planning perspective, the broad rightward shift indicates
that the treatment regime improves the distribution of employment outcomes across its
range rather than in a narrow segment. Likewise, a refugee choosing behind a veil of
ignorance about their own circumstances would have reason to prefer the treatment regime’s
employment prospects.
Secondary Outcomes
Figure 3 reports results using secondary employment outcomes. The prespecified any-
employment outcome indicates whether any adult in the case worked at any point during
the first three years, even briefly. Additional outcomes not specified in the PAP capture
the speed and stability of employment. Any-employment estimates are positive but fairly
imprecise, with a pooled ITT of+2.26pp (95% CI[−1.61,+6.13]pp,p= 0.253) that rises
11

to+4.78pp in the post-COVID cohorts (95% CI[−0.25,+9.81]pp,p= 0.063).
The evidence is stronger for sustained employment. In the pooled sample, assignment to
the treatment arm raises the probability that any adult has a single job spell of at least six
months by5.57pp in the ITT analysis (95% CI[1.50,9.64]pp,p= 0.007). The ITT rises
to9.56pp in the post-COVID cohorts (95% CI[4.30,14.82]pp,p<0.001). Treatment also
raises the probability that any adult has an open-ended contract at three years by4.45pp in
the pooled sample (95% CI[0.46,8.44]pp,p= 0.029) and7.07pp in the post-COVID cohorts
(95% CI[1.84,12.29]pp,p= 0.008). The first adult obtains employment an estimated0.78
months sooner in the pooled sample (95% CI[−0.15,1.71]months,p= 0.100) and1.45
months sooner in the post-COVID cohorts (95% CI[0.22,2.67]months,p= 0.021). Taken
together, these results suggest that access to algorithmic placement recommendations shifted
cases toward earlier and more sustained employment, particularly in the later cohorts.
Secondary migration out of the initial placement canton within three years is rare in
the control arm (5.4% of cases) and not differentially affected by treatment (+0.35pp,p=
0.71; Supplementary Information, Table S11), consistent with legal restrictions on cantonal
mobility.
12

Figure 3:Effects on Secondary Employment Outcomes.
Ever employed within 3y
Open−ended contract (3y)
Single job spell
>=6 months
0 5 10 15
Effect (pp)
ITT
0 5 10 15
Effect (pp)
LATE
First job in case
−2 −1 0
Effect (months)
−3 −2 −1 0
Effect (months)
All cohorts (2020−2023) Excluding peak COVID (2021−2023) Post−COVID (2022−2023)
Notes:Points show covariate-adjusted case-level ITT and LATE estimates for four outcomes: whether any
adult in the case worked at any point during the first 36 months, whether any adult had a single job spell
covering at least 183 days (six months), whether any adult had an open-ended contract at three years, and
months until the first adult in the case obtained employment, censored at 36 months. Negative estimates
for time to first employment indicate faster employment. Bars show 95% confidence intervals. Outcome
definitions and additional results are reported in Supplementary Information, Sec. S10 and Table S11.
13

Prediction Ranks and Realized Gains
To better understand why the estimated gains are larger in later cohorts, Figure 4 examines
two links required for algorithmic matching to improve employment. First, recommendations
must shift placements toward cantons ranked more highly within each refugee’s predicted-
employment profile. This occurred in both the COVID-era and post-COVID cohorts: treat-
ment cases were disproportionately placed in cantons near the top of their own rankings.
Second, higher assigned-canton ranks must be associated with better realized outcomes.
During the COVID era, the rank-on-rank relationship is essentially flat in the upper half,
where most treatment placements occur, indicating little ability to distinguish among the
cantons most often recommended. In the post-COVID cohorts, by contrast, the relationship
is stronger and increases monotonically. Consistent with these patterns, the model predicts
a positive treatment-control employment difference in both periods, while the realized ITT
gain is substantially larger in the post-COVID cohorts. Taken together, the diagnostics show
that treatment shifted placements toward higher-ranked cantons throughout the trial, but
that these rankings translated into larger realized gains after the pandemic. This pattern is
consistent with COVID-induced distribution shift: labor-market conditions during the early
trial diverged from the algorithm’s pre-pandemic training data, weakening the alignment be-
tween predicted rankings and realized employment. As conditions stabilized, that alignment
strengthened and treatment gains increased.
Discussion
This is, to our knowledge, the first randomized controlled trial of algorithmic refugee match-
ing, an approach that has attracted interest from governments and resettlement agencies
because of its potential to improve employment at low marginal cost. Even when averaged
across a deployment period spanning the COVID-19 disruption, the pooled estimates im-
ply employment gains of roughly 10–11%. Among the post-COVID cohorts, the estimated
14

Figure 4:Placement Ranks, Prediction Fit, and Realized Gains.
Pooled COVID−era 2020−2021 Post−COVID 2022−2023
26 20 15 10 5 1 26 20 15 10 5 1 26 20 15 10 5 1
0%
5%
10%
Assigned−canton predicted−employment rank (26 = worst; 1 = best)
Share of placements within arm
Control Treatment
A. Assigned−canton ranks by treatment arm
slope = 0.16 slope = 0.11 slope = 0.19
Pooled COVID−era 2020−2021 Post−COVID 2022−2023
0.0 0.5 1.0 0.0 0.5 1.0 0.0 0.5 1.0
0.4
0.5
0.6
Assigned−canton predicted−employment percentile (1 = best)
Employment percentile
B. Prediction rank and realized employment
Pooled COVID−era 2020−2021 Post−COVID 2022−2023
Predicted gain Actual ITT Predicted gain Actual ITT Predicted gain Actual ITT
−4
0
4
Treatment effect on
3−year employment (pp)
C. Predicted gains versus realized treatment effects
Notes:Columns report pooled cohorts, COVID-era cohorts (2020–2021), and post-COVID cohorts
(2022–2023). Panel A plots the arm-specific distribution of assigned-canton predicted-employment ranks
(1 =highest predicted employment,26 =lowest). Panel B relates the predicted-employment percentile of
the assigned canton to the realized employment percentile. Panels A and B use adult-level prediction
profiles and orient the horizontal axis so worse-ranked cantons are on the left and better-ranked cantons
are on the right. Panel C aggregates to the case level, comparing the predicted employment gain at
realized placements with the case-level ITT. Intervals are 95% confidence intervals where applicable.
Construction details for all three panels are provided in the Supplementary Information, Sec. S11.
gains rise to roughly 17–21% across the ITT and LATE. The effects also grow over the three
year follow-up, consistent with the gradual pace of refugee labor-market integration. At 36
months, treatment raises the probability that any adult in the case is employed by+5.2to
15

+6.0pp (≈11–12%across the ITT and LATE), a particularly policy-relevant margin. In
sum, the results indicate that algorithmically guided placement raised refugee employment
on the order of 10–20% in a real-world deployment.
Several features make the trial a demanding and deliberately constrained test. First, the
trial spanned the COVID-19 disruption, and the COVID-era cohorts weigh down the pooled
estimates. Indeed, the post-COVID cohorts show gains roughly twice as large. Second, the
trial evaluated a tightly constrained deployment, with a sparse predictor set, a low-base-rate
outcome measured over a long horizon, stringent balancing constraints that precluded many
potentially beneficial matches, and mirrored quotas that limited the optimizer to about half
of the caseload and its slots. The estimates therefore capture a restricted version of the ap-
proach. The Methods section describes these issues in greater detail, and the Supplementary
Information compares the trial estimates with the original retrospective backtest predictions
(Sec. S13).
Cost-benefit calculations, which use the fiscal benchmark detailed in the Supplementary
Information, Sec. S12, suggest that these employment gains are large relative to implementa-
tion costs. The central benchmark values each additional employment-month at CHF 1,950
(all monetary amounts are in Swiss francs; CHF 1≈USD 1.2 at September 2026 exchange
rates), combining reduced public support payments with social security contributions and
source taxes. Implementation costs are assumed at CHF 50 per treated adult, covering the
additional operating expenditure of layering the tool onto the existing placement workflow.
This allowance includes placement-officer time, computing, software maintenance, and rou-
tine monitoring. One-time development and integration costs are excluded from this figure
because they amortize at scale. On this basis, the individual-level pooled ITT estimate of
about 1.95 percentage points—equivalent to 0.70 additional employment-months per adult
over three years—translates into roughly CHF 1,300 in fiscal benefits per adult net of im-
plementation costs. The resulting benefit-cost ratio, calculated using gross fiscal benefits,
is approximately 27:1. At a scale of 1,000 treated adults, the pooled ITT corresponds to
16

about CHF 1.30 million in net fiscal benefits. These calculations are deliberately narrow,
in that they capture only fiscal returns to the government—reduced support payments plus
the payroll contributions and source taxes collected on refugees’ earnings—and do not count
the earnings that refugees retain or other welfare gains that accrue to refugees themselves.
Even under this narrow accounting, the estimated fiscal benefits substantially exceed imple-
mentation costs.
These gains are comparable to those of substantially more resource-intensive refugee
labor-market interventions, but are achieved at far lower marginal cost. In the most compa-
rable metric, the trial’s individual-level ITT on being employed three years after placement
is+4.6percentage points (LATE+5.4pp) on a control mean of 44.8% (Supplementary In-
formation, Table S9). Denmark’s 1999 reform, which added roughly 430 hours of language
training, increased full-time-equivalent employment by 4.2 percentage points on average over
18 years7, while Germany’s 600-hour integration courses increased employment by roughly 5
percentage points after one year8. Randomized trials of labor-intensive programs—including
a Swedish package combining language instruction, work practice, and job search assistance9,
as well as an Italian program providing job mentoring and subsidized internships10—reported
gains of 15 and 10 percentage points, respectively. These programs cost roughly CHF 2,400
and CHF 3,000 per participant and require substantial staffing and delivery capacity, making
them resource-intensive to scale. Meanwhile, lighter-touch interventions often yield limited
or no lasting effects11,12. To date, no other causally evaluated refugee-integration interven-
tion has combined employment gains of the order observed in the trial with such low marginal
cost. This cost advantage arises because algorithmic matching improves a placement decision
the government makes anyway rather than adding a costly new program. This comparison
should not be interpreted as evidence that algorithmic matching can substitute for intensive
language courses.
Beyondrefugeeplacement, thetrialprovidesrarerandomizedfieldevidenceonprediction-
based AI decision support in public administration, complementing randomized evidence
17

on statistical support systems for caseworkers in employment offices40 and on algorithmic
risk assessments provided to judges in criminal justice41. Its timing also illustrates the
vulnerability of such systems to distribution shift: the largest gains occur among cohorts
that integrated after labor-market conditions normalized, and prediction diagnostics show
closer alignment between predicted and realized gains in those cohorts. These findings
underscore the importance of monitoring predictive fit, detecting distribution shift, and
retraining as conditions change27,28. More broadly, they show that predictive tools can
improve consequential public decisions42 when used to support, rather than replace, human
decision-makers and when operating within explicit policy constraints.
Future randomized evaluations should test upgraded systems in other institutional set-
tings and under different allocation constraints. Priorities include richer predictor sets,
shorter-horizon proxy outcomes that permit faster updating, dynamic and multi-objective
optimization, and methods designed explicitly for distribution shift. That the highly con-
strained implementation increased employment during a period of substantial disruption and
at low marginal cost suggests that updated and less constrained systems could generate even
larger gains.
Methods
Trial Eligibility
The cases in the trial entered the SEM’s normal asylum process as asylum seekers. Eligible
cases were assigned by the SEM to the fast-track procedure (beschleunigtes Verfahren) and,
before cantonal placement, had obtained either subsidiary protection (permit F) or recog-
nized refugee status (permit B). They were also “free” cases not subject to legally required
placement in a specific canton and had at least one adult member.
18

Algorithmic Recommendation System
The intervention evaluated in this trial was an early generation version of GeoMatch, an
outcome-based refugee-matching system based on the methodology in Bansak et al.20. The
system recommended one of Switzerland’s 26 cantons for each eligible case. A case is the
placement unit, consisting of one or more refugees (typically a household or family) who
are placed together. For each canton, a separate stochastic gradient-boosted tree model
predicted a working age refugee’s three year employment proportion from a small set of
baseline characteristics selected by the SEM for deployment: gender, age at arrival, marital
status, case size, arrival year and month, nationality, and native language.
The models were trained on administrative data from past arrivals and tuned by cross-
validation20,30. During the trial, the models were retrained roughly quarterly using the
newest available administrative data. This scheduled retraining is part of the GeoMatch
design, throughwhichthedeployedsystemlearnsfromaccumulatingdata. Thepredictorset,
model class, optimization target, and constraint structure remained fixed. The optimization
target, chosen by the SEM, was the cumulative share of months employed over the first three
years after placement.
Becauseeachcaseisplacedasasingleunit, therefugee-levelpredictionswithinacasewere
combined into one case-level metric. For the employment-share outcome optimized in the
trial, thetoolfollowedtheSEM’srequestedaggregationruleandaveragedtheadultmembers’
predicted employment proportions within each case. A constrained optimization procedure
then recommended a canton for each case to maximize aggregate predicted employment,
subject to the system’s capacity constraints.
The SEM imposed two stringent optimization constraints, reflecting rules that govern its
regular cantonal allocation process43. First, every placement had to respect Switzerland’s
cantonal proportionality key, which allocates asylum cases across the 26 cantons roughly
in proportion to canton population. Second, the key is crossed with nationality quotas
requiring several national-origin groups to remain separately balanced across cantons in the
19

same proportions30. In addition, placements were made online and case by case: cases
arrived sequentially and had to be placed before later arrivals were known. To handle this
online problem, the early generation system used a minimum-discord allocation rule26. The
rule simulates the expected future caseload and recommends the feasible canton that least
disrupts the allocation of slots anticipated for future arrivals, thereby preserving scarce slots
for later cases likely to need them while respecting capacity constraints.
GeoMatch ran as a standalone, human-in-the-loop decision support tool built with input
from placement officers to fit their existing workflow. For each eligible case, the placement
officers received a recommended canton that could be accepted or overridden, retaining final
placement authority.
Experimental Design
The trial was authorized by the SEM Board and designed in consultation with the cantons
represented in the tripartite working group AGNA (Arbeitsgruppe zur Neustrukturierung des
Asylbereichs). Before the trial began, it was reviewed and approved by the Stanford Univer-
sity Institutional Review Board (protocol 46216), and the ETH Zurich Ethics Commission
accepted the Stanford approval as sufficient for ETH-based investigators. The Commit-
tee for the Protection of Human Subjects at Dartmouth College also approved the study
(STUDY00031234). The Stanford University Institutional Review Board waived the require-
ment for informed consent because the intervention was embedded in routine administrative
placement and the analysis used administrative records. The trial was a single-intervention,
double-blind randomized controlled trial with one treatment arm and one control arm. The
PAP specified a target of 2,000 cases, with 1,000 cases per arm, and the case was the unit of
randomization. This sample-size target was agreed with the SEM rather than derived from
a formal power calculation, and it was fixed before any outcome data were received.
Each eligible case was randomized independently, with probability 0.5, to receive ei-
ther an algorithmic recommendation (treatment) or a status quo recommendation (control).
20

Placement officers screened cases for trial eligibility and entered them into the placement
tool, where assignment was executed by a computer-generated random draw. Allocation
was therefore determined centrally and automatically after eligibility had been established:
a case’s assignment did not exist at the time of screening and was never revealed afterward,
ruling out selective enrollment based on expected treatment status. The tool’s interface was
identical in both arms; only the recommended canton differed. Eligibility criteria, the ran-
domization procedure, and the mirrored quota design remained unchanged from the January
2020 launch through June 30, 2023.
The treatment recommendation selected the canton predicted to maximize aggregate
employment across cases, subject to the quota and balancing constraints described above.
The control recommendation was designed to approximate the status quo procedure for free
cases. Under regular Swiss dispersal policy, the SEM assigns asylum cases to cantons ac-
cording to the cantonal proportionality key and national-origin balancing rules, using records
from ZEMIS (the SEM’s Central Migration Information System) and without personal in-
teraction with applicants. Refugee preferences are not considered except for narrow legal
exceptions, such as close family ties, health needs, or the accommodation of unaccompanied
minors. The control arm therefore approximated the status quo for free cases by randomly
selecting among feasible canton slots under the same quota structure, without using employ-
ment predictions.
Two design features protected the integrity of the treatment contrast. First, the design
prevented interference through separate, mirrored quotas. The trial quota was split into
identical treatment and control quotas, so each case drew only on slots reserved for its own
arm. This ruled out interference through slot competition and kept the aggregate canton
and origin-group allocation the same across arms. As a result, any treatment effect cannot
come from assigning more treated cases to stronger labor markets, but only from changing
which cases are recommended for a particular canton within the same distribution of slots.
Second, the trial was double-blind. For each trial case, placement officers received either
21

the GeoMatch recommendation or the control recommendation in the same format and
workflow, but were not told which procedure generated the recommendation. Refugees
were likewise unaware of treatment status. Thus, officers could respond to the displayed
recommendation but not to its source. Outcomes came from independently collected register
records and were not subject to assessor discretion based on treatment status.
Pre-Analysis Plan
The trial’s PAP was registered on the OSF Registries on March 9, 2023, after the trial
launched in January 2020 but before linked employment outcome data were received30. The
PAP defines the primary outcome as the three year employment proportion, the employment
measure optimized by the tool. The primary estimand is the intention-to-treat (ITT) effect
of assignment to the treatment arm rather than the control arm. The primary estimator is
ordinary least squares (OLS) regression with the prespecified covariate adjustment from the
Lin specification37 that interacts the demeaned covariates with the treatment indicator.
The PAP also specifies local average treatment effect (LATE) analyses for placement
in the GeoMatch-recommended canton, allowing for noncompliance with recommendations.
For each case, the GeoMatch-recommended canton is defined as the canton the algorithm
recommended in the treatment arm or would have recommended had the case been as-
signed to treatment. An indicator then records whether the case was initially placed in
that GeoMatch-recommended canton. The LATE instruments this placement indicator with
random assignment to the treatment arm. Noncompliance arises when officers do not follow
the displayed recommendation (“nonadherence”) or, more commonly, when the control and
GeoMatch procedures recommend the same canton. Officer adherence to the displayed rec-
ommendation was 97%. Section S5 of the Supplementary Information details these channels
and the identifying assumptions. The PAP specifies two additional pre-registered LATE def-
initions: initial placement in the GeoMatch-recommended canton combined with residence
for at least half of the three year follow-up, and the fraction of the follow-up period spent in
22

that canton. Because secondary migration is rare, these residence-based definitions produce
very similar estimates.
The PAP also pre-registers secondary outcomes and analyses, including any employment
during the three year follow-up, emigration, secondary migration, and alternative estimators.
The PAP anticipated that the COVID-19 disruption could weaken the performance of models
trained on pre-pandemic data. Analyses by placement cohort and follow-up horizon provide
a natural way to examine this concern, although they were not explicitly prespecified.
A Conservative Test
Several features of the Swiss deployment make the trial a conservative test of algorithmic
refugee matching, as the PAP anticipated.1
The trial evaluated an early generation version of the matching system. Since launch, the
methodology has advanced, including richer predictive models, online assignment with dy-
namic resource balancing, methods for learning under distribution shift, and multi-objective
trade-off methods23,24,26–28. To preserve implementation fidelity and keep the treatment
definition fixed, the deployed model specification and optimization procedure remained un-
changed as these methods became available. Periodic retraining updated the fitted models
withnewlyavailabledatabutdid notaltertheunderlyingmethod. The informationavailable
to the deployed algorithm was also sparse. The ZEMIS register does not currently record
standard human capital variables that are known to be predictive of employment, such as
education, occupational skills, prior work history, and host-language proficiency. Predictive
accuracy, and therefore the scope for finding person-place synergies, was bounded by the
information the algorithm was allowed to use. The three year employment outcome itself
was difficult to optimize as well, as refugee employment in this window is low, with a control-
arm mean of about 22% of months employed over three years. Small relative movements are
1The PAP described the recommendations as a “highly constrained version of the GeoMatch algorithm”
whose observed gains would be a “lower bound for gains that may be realized in less constrained versions”;
conversely, “if no gains are observed, this does not imply that no gains could be realized with less constrained
versions” 30.
23

therefore hard to detect.
The placement geography was also coarse. Recommendations were made across Switzer-
land’s 26 cantons rather than across municipalities or local labor markets, and the propor-
tionality key’s uneven distribution left several small cantons with less than 1% of placements
(Supplementary Information, Table S1).
The quota constraints described in the experimental design further restricted the opti-
mization problem. The cantonal proportionality key was crossed with nationality-balance
rules43. Thus, the algorithm had to recommend cases within a fixed canton-by-origin-group
distribution rather than shifting more members of a given origin group to cantons where that
group tends to fare better, for example because of co-ethnic networks or language region
matches. This constraint cuts against a well-documented finding in the refugee integration
literature that networks and language matches matter for employment. The importance
of these constraints is demonstrated by prior research in Switzerland, which showed that
assignment to a canton with a 10% larger co-national network raises the probability of em-
ployment three years after arrival by about 0.3 percentage points (roughly 2% relative)19,
while placement on the linguistically matching side of the German–French language border
more than doubles employment over the first five years after arrival17,18. The trial therefore
measures the value of matching within a heavily constrained quota structure, not the gains
possible under less constrained allocation.
The mirrored quota design imposed one further restriction on the optimizer. To keep
the arms free of interference, the available canton-by-origin-group capacity was divided into
separate treatment and control pools, so the algorithm optimized assignments over only
about half of the eligible caseload and its slots—a restriction no practical deployment would
impose. Because matching gains grow with the size of the joint pool, particularly where
small cantons hold only a handful of slots, a system-wide deployment optimizing the full
caseload would face a richer set of feasible matches than the trial allowed.
Two further features added noise and distribution shift. First, the tool applied only
24

to trial-eligible cases intended to be placeable in any canton. In the historical data used
for training, however, the available free-case indicator only imperfectly approximated this
eligibility rule. This mismatch between the training indicator and the trial population likely
diluted performance. Second, the trial began in January 2020, just before the start of the
COVID-19 pandemic. The Swiss Federal Council declared an “extraordinary situation” on
March 16, 2020, closing shops, restaurants, and leisure venues, and lifted many measures
only in February 202244.
The pandemic shock affected labor markets and the relationship between employment
and geographic placement through several channels44–47. Border controls and entry restric-
tions disrupted mobility. The SEM temporarily modified asylum interviews and procedural
rules, and working hours were cut through short-time work schemes that prioritized pro-
tecting incumbent jobs over hiring new labor-market entrants. Vacancy data show that job
advertisements regained pre-pandemic levels only in the third quarter of 2021, with hospi-
tality hiring especially depressed until the summer reopening. The asylum employment spell
records provide corresponding evidence: among employed cases in the 2019–2023 arrival
cohorts, the main jobs were concentrated in hospitality (restaurants and hotels) and other
face-to-face service work, with sizable shares also in cleaning and construction-related work.
These entry jobs were plausibly among those most exposed to closures, capacity restrictions,
reduced customer demand, and short-time work during the early pandemic.
Since integration is front-loaded, the first one to two years after placement are when
refugees typically enter language and integration programs, build local networks, search for
first jobs, and establish early work histories3,4. Cohorts placed in 2020 and 2021 therefore
experienced pandemic disruptions during the period when placement quality was most likely
to matter. By contrast, the 2022 and 2023 cohorts began this early integration window after
the most severe mortality waves and broadest labor-market and institutional disruptions had
largely passed (Supplementary Information, Fig. S2).
The models available to the early trial cohorts were trained on pre-pandemic data. They
25

were therefore extrapolating person-place employment relationships from an economy that
no longer closely resembled the one those cohorts entered. The system also could not learn
from COVID-era three year employment outcomes in real time, because those outcomes were
observed only years after placement and the deployed algorithm did not use short-horizon
proxy outcomes for updating. Later cohorts integrated under conditions closer to those in
the training data.
Data and Sample
The data come from the SEM’s ZEMIS administrative register, which tracks asylum appli-
cants from arrival through the asylum process. Its case-processing and placement records
are linked to basic demographic characteristics and employer-reported employment histories.
The three year window is the 36 calendar months following the month of canton assignment;
the partial assignment month is excluded. A month counts as employed if it falls within
an employer-reported employment spell recorded in ZEMIS. Following the PAP sample-size
target, the analytic sample consists of the first 2,000 eligible cases with complete three year
employment outcomes, ordered by the date and time of assignment. The source extract cov-
ers assignments between January 2020 and June 30, 2023 and contains 2,096 eligible cases
comprising 2,256 adults present at initial assignment (Supplementary Information, Fig. S1).
Adults are case members whose age at arrival is at least 18. Of these cases, 2,046 have com-
plete three year outcomes. Retaining the first 2,000 (1,001 treatment and 999 control cases)
yields an analytic sample of 2,156 adults, with the final selected case assigned on June 13,
2023. A sensitivity analysis including all 2,046 complete cases yields nearly identical results
(Supplementary Information, Sec. S7, Table S8).
Attrition and inverse-probability-weighting diagnostics use a broader recruitment frame
containing all eligible cases randomized through the June 13 selection boundary, regard-
less of three year outcome completeness. This frame contains 2,050 cases comprising 2,209
adults. Employment is observed only while an individual has an active administrative record;
26

individuals no longer active at three years are likely to have left Switzerland.
In the analytic sample, mean age at arrival is 27.9 years; 16% are female; and the largest
origin groups are Afghanistan (54%), Turkey (26%), and Syria (9%). The mean arrival-to-
placement gap is 2.8 months (capped at its 95th percentile). In the control arm, the share
of months employed is 7% in the first year, 14% over the first two years, and 22% over the
first three years. Among control-arm refugees, 57% hold any job at some point within the
first three years.
Design Checks
Placement officer adherence to the displayed recommendation was high and similar across
arms. Specifically, eventual placement matched the displayed canton in roughly 97% of cases
in each arm (97.3% in control and 96.5% in treatment; difference=−0.8pp,p= 0.37).
At the case level, the mirrored quotas produced nearly identical canton distributions
across treatment and control arms (χ2 test of independencep >0.99in the PAP analysis
sample). The same balance holds within each placement cohort (2020–2023;χ2 testp>0.92
for all cohorts). The joint distribution of canton and origin group (Afghanistan, Turkey, and
Other) was likewise balanced (χ2 testp >0.99; Supplementary Information, Table S3 and
Fig. S3).
In the pooled sample, baseline covariate means are nearly identical across arms (Supple-
mentary Information, Table S2), and an omnibus regression of treatment assignment on the
listed baseline covariates does not reject joint balance (F11,1,999 = 0.49,p= 0.91). Finally,
three year outcome observability is balanced. The percentage unobserved at three years
is 2.5% in control and 2.3% in treatment, with an adjusted treatment-control difference of
−0.27pp (p= 0.67; Supplementary Information, Sec. S4, Table S4).
27

Analysis
The ITT captures deployment of the GeoMatch recommendation with the observed level of
officer take-up, including any overrides. The LATE captures the effect of placement in the
GeoMatch-recommended canton among compliers48.
The main analysis uses the refugee case as the unit of analysis, matching the unit of
randomization and placement and the objective optimized by the algorithm: the mean three
year employment proportion among adult members of the placed case. The individual-level
analog is reported in the Supplementary Information (Table S7) and yields similar results.
The ITT estimator is an OLS regression of this case-level outcome on treatment assign-
ment and covariates, entered with interactions via the Lin specification37, as registered in
the PAP. An instrumental variables (IV) specification with additive covariate adjustment
estimates the LATE. All specifications use robust standard errors clustered by case. Unless
otherwise noted, reported confidence intervals andp-values are two-sided. The covariate set
follows the PAP’s primary specification and includes year- and month-of-placement fixed
effects, age-bin indicators, gender, case-size indicators (top-coded at four or more mem-
bers), marital-status indicators, nationality group indicators (top three nationalities plus
other), language group indicators (top three languages plus other), time from arrival or en-
try to placement, and canton fixed effects. Case-level covariates use the earliest-arriving
adult; when multiple adults tie on the earliest arrival date, their covariate values are aver-
aged. Additional specifications—including the unadjusted difference in means, the primary
Lin specification omitting canton fixed effects, additive covariate adjustment, post-double-
selection LASSO38, and inverse-probability-weighted attrition correction—are reported in
the Supplementary Information and yield results that are virtually identical to the primary
Lin specification (Table S6). Details of AI-assisted manuscript preparation are provided in
the Supplementary Information (Sec. S14).
28

Acknowledgements
We thank the Swiss State Secretariat for Migration (SEM) for providing the administrative
data and, above all, for implementing the pilot within the agency’s core placement processes.
We are grateful to the SEM placement officers and staff who carried out the randomized
recommendations in their daily work. We thank Duncan Lawrence for useful comments,
George Wood for research assistance, and Michael Maurer for assistance with the GeoMatch
interface.
Funding
The tool development and evaluation were supported by Stanford University’s Institute
for Human-Centered Artificial Intelligence, Schmidt Futures, Google.org, Rockefeller Foun-
dation, Stanford Impact Labs, Charles Koch Foundation, and Open Society Foundations.
D.H.acknowledgesfundingfromtheEuropeanResearchCouncilundertheEuropeanUnion’s
Horizon 2020 research and innovation programme (grant 804307). The funders had no role in
study design, data collection or analysis, the decision to publish, or manuscript preparation.
Author Contributions
K.B., J.H., and D.H. jointly led the project and are designated as lead authors. K.B., J.H.,
D.H., and J.F. conceptualized and designed the study. K.B. and J.H. developed the core
GeoMatch algorithm, and K.B. and E.P. developed the minimum-discord online assignment
rule. K.B., N.A.-C., and A.R. developed the software interface. K.B., J.H., D.H., J.F., S.K.,
J.P., and M.H. coordinated and implemented the trial. K.B., J.H., D.H., A.D., N.A.-C., and
M.H. acquired and curated the data. K.B., J.H., and D.H. conducted the statistical analysis
and prepared the visualizations. K.B., J.H., D.H., J.F., E.P., A.D., and M.H. interpreted the
results. J.H. and D.H. supervised the project and acquired funding. J.H. wrote the original
29

draft. All authors reviewed and revised the manuscript and approved the final version.
Competing Interests
The authors declare no competing interests. The research team received no payments from
SEM or other Swiss government entities for developing or operating the tool.
Data Availability
Thesensitiveindividual-leveladministrativedataarerestrictedunderthedata-useagreement
with the Swiss State Secretariat for Migration (SEM). Researchers may apply directly to
SEM, subject to legal, privacy, and institutional approval.
Code Availability
The code used to produce all analyses, tables, and figures will be archived in a public
repository upon publication.
Additional Information
Supplementary Information is appended to this preprint. The pre-analysis plan is avail-
able on the OSF Registries30. Correspondence should be addressed to Jens Hainmueller
(jhain@stanford.edu).
References
[1] UNHCR (United Nations High Commissioner for Refugees). Global appeal 2026. UN-
HCR, Geneva (2026).
30

[2] Fasani, F., Frattini, T. & Minale, L. (The Struggle for) refugee integration into the
labour market: evidence from Europe.Journal of Economic Geography22, 351–393
(2022).
[3] Hainmueller, J., Hangartner, D. & Lawrence, D. When lives are put on hold: Lengthy
asylum processes decrease employment among refugees.Science Advances2, e1600432
(2016).
[4] Marbach, M., Hainmueller, J. & Hangartner, D. The long-term impact of employment
bans on the economic integration of refugees.Science Advances4, eaap9519 (2018).
[5] Bahar, D., Brough, R. J. & Peri, G. Refugees’ economic integration.Journal of Eco-
nomic Literature64, 950–983 (2026).
[6] Ferwerda, J. & Finseraas, H. Do integration courses influence refugees’ integration
trajectories? Evidence from Norway.The Journal of Politics87, 1319–1334 (2025).
[7] Foged, M., Hasager, L., Peri, G., Arendt, J. N. & Bolvig, I. Language training and
refugees’ integration.The Review of Economics and Statistics106, 1157–1166 (2024).
[8] Marbach, M., Vallizadeh, E., Harder, N., Hangartner, D. & Hainmueller, J. Does ad
hoc language training improve the economic integration of refugees? Evidence from
Germany’s response to the Syrian refugee crisis.Journal of the Royal Statistical Society
Series A: Statistics in Society188, 1168–1183 (2025).
[9] Dahlberg, M., Egebark, J., Vikman, U. & Özcan, G. Labor market integration of
refugees: RCT evidence from an early intervention program in Sweden.Journal of
Economic Behavior and Organization217, 614–630 (2024).
[10] Abbiati, G., Battistin, E., Monti, P. & Pinotti, P. Fast-tracked jobs help asylum seekers
integrate faster. Discussion Paper 17859, IZA (2025).
31

[11] Emeriau, M., Hainmueller, J., Hangartner, D. & Laitin, D. D. “Welcome to France.”
Can mandatory integration contracts foster immigrant integration?American Journal
of Political Science70, 425–440 (2026).
[12] Battisti, M., Giesing, Y. & Laurentsyeva, N. Can job search assistance improve the
labour market integration of refugees? Evidence from a field experiment.Labour Eco-
nomics61, 101745 (2019).
[13] Åslund, O.&Rooth, D.-O. Dowhenandwherematter? Initiallabourmarketconditions
and immigrant earnings.The Economic Journal117, 422–448 (2007).
[14] Damm, A. P. & Rosholm, M. Employment effects of spatial dispersal of refugees.Review
of Economics of the Household8, 105–146 (2010).
[15] Azlor, L., Damm, A. P. & Schultz-Nielsen, M. L. Local labour demand and immigrant
employment.Labour Economics63, 101808 (2020).
[16] Godøy, A. Local labor markets and earnings of refugee immigrants.Empirical Eco-
nomics52, 31–58 (2017).
[17] Auer, D. Language roulette – the effect of random placement on refugees’ labour market
integration.Journal of Ethnic and Migration Studies44, 341–362 (2018).
[18] Schmid, L. The impact of host language proficiency on migrants’ employment outcomes.
American Economic Review: Insights5, 477–493 (2023).
[19] Martén, L., Hainmueller, J. & Hangartner, D. Ethnic networks can foster the economic
integration of refugees.Proceedings of the National Academy of Sciences116, 16280–
16285 (2019).
[20] Bansak, K.et al.Improving refugee integration through data-driven algorithmic assign-
ment.Science359, 325–329 (2018).
32

[21] Bansak, K.et al.Robustness of refugee-matching gains to off-policy evaluation choices.
arXiv preprint arXiv:2605.06686 (2026).
[22] Ahani, N., Andersson, T., Martinello, A., Teytelboym, A. & Trapp, A. C. Placement
optimization in refugee resettlement.Operations Research69, 1468–1486 (2021).
[23] Acharya, A., Bansak, K. & Hainmueller, J. Combining outcome-based and preference-
based matching: A constrained priority mechanism.Political Analysis30, 89–112
(2022).
[24] Freund, D., Lykouris, T., Paulson, E., Sturt, B. & Weng, W. Group fairness in dynamic
refugee assignment. arXiv preprint arXiv:2301.10642 (2023).
[25] Ahani, N., Gölz, P., Procaccia, A. D., Teytelboym, A. & Trapp, A. C. Dynamic place-
ment in refugee resettlement.Operations Research72, 1087–1104 (2024).
[26] Bansak, K. & Paulson, E. Outcome-driven dynamic refugee assignment with allocation
balancing.Operations Research72, 2375–2390 (2024).
[27] Bansak, K., Paulson, E. & Rothenhäusler, D. Learning under random distributional
shifts. InInternational Conference on Artificial Intelligence and Statistics, 3943–3951
(PMLR, 2024).
[28] Jain, G., Rothenhäusler, D., Bansak, K. & Paulson, E. CTRL your shift: Clustered
transfer residual learning for many small datasets. arXiv preprint arXiv:2508.11144
(2025).
[29] Bansak, K., Lee, S., Manshadi, V., Niazadeh, R. & Paulson, E. Dynamic matching with
post-allocation service and its application to refugee resettlement.Management Science
(2026).
[30] Bansak, K.et al.Pre-analysis plan for the Swiss Pilot RCT (2023). URLhttps:
//osf.io/pu23k. Registered on the OSF Registries, March 9, 2023.
33

[31] Kagerbauer, S. M.et al.Susceptibility of AutoML mortality prediction algorithms to
model drift caused by the COVID pandemic.BMC Medical Informatics and Decision
Making24, 34 (2024).
[32] Andonov, D. I.et al.Impact of the Covid-19 pandemic on the performance of machine
learning algorithms for predicting perioperative mortality.BMC Medical Informatics
and Decision Making23, 67 (2023).
[33] Yin, J., Han, B. & Wong, H. Y. COVID-19 and credit risk: A long memory perspective.
Insurance: Mathematics and Economics104, 15–34 (2022).
[34] Papík, M. & Papíková, L. Impacts of crisis on SME bankruptcy prediction models’
performance.Expert Systems with Applications214, 119072 (2023).
[35] Castle, J. L., Doornik, J. A. & Hendry, D. F. The value of robust statistical forecasts
in the Covid-19 pandemic.National Institute Economic Review256, 19–43 (2021).
[36] O’Trakoun, J. Business forecasting during the pandemic.Business Economics57,
95–110 (2022).
[37] Lin, W. Agnostic notes on regression adjustments to experimental data: Reexamining
Freedman’s critique.The Annals of Applied Statistics7, 295–318 (2013).
[38] Belloni, A., Chernozhukov, V. & Hansen, C. High-dimensional methods and inference
on structural and treatment effects.Journal of Economic Perspectives28, 29–50 (2014).
[39] Barrett, G. F. & Donald, S. G. Consistent tests for stochastic dominance.Econometrica
71, 71–104 (2003).
[40] Behncke, S., Frölich, M. & Lechner, M. Targeting labour market programmes: Results
from a randomized experiment.Swiss Journal of Economics and Statistics145, 221–268
(2009).
34

[41] Imai, K., Jiang, Z., Greiner, D. J., Halen, R. & Shin, S. Experimental evaluation
of algorithm-assisted human decision-making: Application to pretrial public safety as-
sessment.Journal of the Royal Statistical Society Series A: Statistics in Society186,
167–189 (2023).
[42] Kleinberg, J., Ludwig, J., Mullainathan, S.&Obermeyer, Z. Predictionpolicyproblems.
American Economic Review105, 491–495 (2015).
[43] Schweizerischer Bundesrat. Asylverordnung 1 vom 11. August 1999 über Verfahrensfra-
gen (Asylverordnung 1, AsylV 1). Systematische Rechtssammlung, SR 142.311 (1999).
URLhttps://www.fedlex.admin.ch/eli/cc/1999/359/de. Accessed 25 June 2026.
[44] Swiss Federal Council. Coronavirus (COVID-19): Federal Council measures (media
releases). admin.ch (2022). “Extraordinary situation” declared 16 March 2020; most
measures lifted February 2022; available athttps://www.admin.ch/en/nsb?id=78454
andhttps://www.admin.ch/en/nsb?id=87216.
[45] Swiss State Secretariat for Migration (SEM). Verordnung über Massnahmen im
Asylbereich im Zusammenhang mit dem Coronavirus (Covid-19-Verordnung Asyl).
sem.admin.ch (2020). COVID-19 asylum-procedure ordinance and protective measures;
available athttps://www.sem.admin.ch/sem/de/home/sem/rechtsetzung/archiv/
covid-19-vo-asyl.html.
[46] KOF Swiss Economic Institute. The situation in the labour market remains chal-
lenging. KOF Bulletin (2021). Reports large sectoral employment losses, reduced
working hours, and extensive short-time work during the COVID-19 crisis; avail-
able athttps://kof.ethz.ch/en/news-and-events/kof-bulletin/kof-bulletin/
2021/04/The-situation-in-the-labour-market-remains-challenging.html.
[47] Adecco Group Switzerland and Swiss Job Market Monitor. Swiss job market: Job
advertisements reach pre-coronavirus level. Adecco Group Swiss Job Market Index, Q3
35

2021 (2021). Survey developed with the Swiss Job Market Monitor at the University of
Zurich; available from Adecco Group.
[48] Angrist, J. D., Imbens, G. W. & Rubin, D. B. Identification of causal effects using
instrumental variables.Journal of the American Statistical Association91, 444–455
(1996).
36

Supplementary Information for
AI-based matching improves refugee employment in a double-blind randomized trial
Kirk Bansak1,2, Jens Hainmueller 2,3, Dominik Hangartner 4,5,
Jeremy Ferwerda2,6, Elisabeth Paulson 2,7, Angie Delevoye 2,
Nicholas Adams-Cohen2, Ashwin Ramaswami 2, Selina Kurer 4,5,
Joelle Pianzola4, and Michael Hotard 2
1Department of Political Science, University of California, Berkeley, Berkeley, CA, USA
2Immigration Policy Lab, Stanford University, Stanford, CA, USA
3Department of Political Science, Stanford University, Stanford, CA, USA
4Immigration Policy Lab, ETH Zurich, Zurich, Switzerland
5Public Policy Group, ETH Zurich, Zurich, Switzerland
6Department of Government, Dartmouth College, Hanover, NH, USA
7Technology and Operations Management Unit, Harvard Business School, Boston, MA, USA
Contents
S1 Trial profile 2
S2 Cantonal distribution key 2
S3 COVID disruption 3
S4 Descriptive statistics and balance checks 5
S5 Local average treatment effects 8
S6 Effects by placement cohort 9
S7 Robustness checks 12
S8 Effects over follow-up 14
S9 Distributional analysis 15
S10 Secondary outcomes 16
S11 Placement ranks and predicted gains 19
S12 Fiscal benchmark 20
S13 Comparison with backtest 20
S14 AI-assisted preparation 21
1

S1 Trial profile
Figure S1 reports the trial profile. Placement officers screened free cases for trial eligibility as cases
reached the placement stage and entered eligible cases into the placement tool, where each case was
randomized at the moment it was entered; cases screened out before this step are not recorded in
the trial extract, so the profile begins at randomization. Eligible cases were randomized between
January 13, 2020 and June 30, 2023, at placement processing, which typically occurred a few months
after arrival in Switzerland (Table S2). The analytic sample comprises the first 2,000 cases with
complete three year outcomes in assignment order, per the PAP’s target sample size. Attrition
diagnostics use the broader recruitment frame of all eligible cases randomized up to the assignment
of the 2,000th complete case on June 13, 2023, regardless of outcome completeness (Sec. S4.3).
Figure S1:Trial profile.
Eligible free cases, randomized 1:1
January 13, 2020 – June 30, 2023
2,096 cases (1,051 treatment, 1,045 control)
2,256 adults
Complete three year outcomes
2,046 cases (1,027 treatment, 1,019 control)
Analytic sample: first 2,000 com-
plete cases in assignment order
2,000 cases (1,001 treatment, 999 control)
2,156 adults (1,083 treatment, 1,073 control)
Without complete three year out-
comes:
50 cases (24 treatment, 26 control)
Assigned after the 2,000th complete
case, beyond the prespecified target
sample size:
46 cases (26 treatment, 20 control)
Notes: Counts are refugee cases, the unit of randomization, with adult counts shown where a stage’s analyses use
adults. A case lacks complete three year outcomes when no adult member has an observed three year employment
history. The selection rule retains the first 2,000 complete cases in assignment order, per the PAP’s target sample
size. Attrition and observability diagnostics (Sec. S4.3) use the recruitment frame of all 2,050 eligible cases
randomized up to the assignment of the 2,000th complete case on June 13, 2023 (1,025 per arm; 2,209 adults).
S2 Cantonal distribution key
The Swiss proportionality key allocates asylum seekers to cantons according to cantonal population.
Table S1 reports the distribution set out in Asylum Ordinance 1.1 Because the shares are uneven,
1Swiss Federal Council,Asylum Ordinance 1 on Procedural Matters (AsylV 1), SR 142.311, art. 21 para. 3 and
annex 3, annex version effective January 1, 2026:https://www.fedlex.admin.ch/eli/cc/1999/359/de. The key
only varies slightly across years.
2

the key substantially narrows the effective canton-level choice set.2 Several cantons receive less
than 1% of placements, or fewer than ten cases per 1,000 placements, even before the additional
origin-group constraints are imposed.3
Table S1:Cantonal distribution key under Asylum Ordinance 1.
Canton Key Per 1,000 Canton Key Per 1,000
ZH 17.9% 179 GR 2.3% 23
BE 11.8% 118 BS 2.2% 22
VD 9.5% 95 NE 2.0% 20
AG 8.1% 81 SZ 1.9% 19
SG 6.0% 60 ZG 1.5% 15
GE 5.9% 59 SH 1.0% 10
LU 4.8% 48 JU 0.8% 8
VS 4.1% 41 AR 0.6% 6
TI 4.0% 40 NW 0.5% 5
FR 3.8% 38 GL 0.5% 5
BL 3.3% 33 OW 0.4% 4
TG 3.3% 33 UR 0.4% 4
SO 3.2% 32 AI 0.2% 2
Notes: Per 1,000 converts the key into the expected number of placements per 1,000 placed cases.
During the study period, free cases—cases the SEM could allocate without placement constraints
such as medical needs, family reunification, or resettlement—accounted for approximately 33% of
cantonal allocations among adults processed under the fast-track procedure (beschleunigtes Ver-
fahren). This calculation uses the SEM allocation registers and excludes persons under temporary
protection status S (mostly from Ukraine), consistent with the trial’s eligibility criteria.
S3 COVID disruption
The trial launched in January 2020, weeks before the COVID-19 pandemic reached Switzerland, so
the earliest placement cohorts began their integration under acutely disrupted conditions. Figure S2
documents this exposure by combining monthly COVID-19 deaths (Panel A)4 with each cohort’s
exposure to the broad disruption period from March 2020 through February 2022 (Panel B). These
bounds correspond to major Federal Council decisions: Switzerland declared an “extraordinary
situation” under the Epidemics Act on March 16, 2020, and lifted most remaining restrictions on
February 17, 2022.5
In the complete three year analysis sample, the disruption period covered an average of 81%
of the first two post-placement years for the 2020 cohort and 28% for the 2021 cohort, compared
with less than 1% for the 2022 and 2023 cohorts. During the first post-placement year alone, the
2Cantons are identified by their official two-letter abbreviations, used in Table S1 and Figure S3: AG Aargau, AI
Appenzell Innerrhoden, AR Appenzell Ausserrhoden, BE Bern, BL Basel-Landschaft, BS Basel-Stadt, FR Fribourg,
GE Geneva, GL Glarus, GR Graubünden, JU Jura, LU Lucerne, NE Neuchâtel, NW Nidwalden, OW Obwalden, SG
St. Gallen, SH Schaffhausen, SO Solothurn, SZ Schwyz, TG Thurgau, TI Ticino, UR Uri, VD Vaud, VS Valais, ZG
Zug, ZH Zurich.
3See Asylum Ordinance 1 (AsylV 1), SR 142.311, art. 22 para. 1.
4Deaths are from the official FOPH/BAG dashboard’s weekly series, aggregated to calendar months by ISO week
start date. The archived source file isCOVID19Death_geoRegion_w.csv (source date 28 November 2023, data version
20231206-0sxi4s4a; documentation athttps://www.covid19.admin.ch/api/data/context), using the Switzerland-
only CH series through 2022 and the combined Switzerland–LiechtensteinCHFL series for 2023.
5Federal Council press releases: https://www.admin.ch/en/nsb?id=78454 and https://www.admin.ch/en/nsb?
id=87216.
3

corresponding shares were 99%, 56%, 1%, and 0%. Thus, the 2020–2021 cohorts spent much of
their early integration in the disrupted environment, whereas the 2022 and 2023 cohorts largely did
not. The PAP anticipated that COVID-related distribution shift could weaken models trained on
pre-pandemic data, and analyses by placement cohort and follow-up horizon examine this concern.
Figure S2:COVID mortality and disrupted integration time by placement cohort.
Peak: 3,050
0
1,000
2,000
3,000
Jul
2020
Jan
2021
Jul
2021
Jan
2022
Jul
2022
Jan
2023
Jul
2023
Monthly COVID−19 deaths
A. COVID mortality shock in Switzerland
99%
62%
56%
1% 1%0%
25%
50%
75%
100%
2020
N=291
2021
N=497
2022
N=696
2023
N=516
Placement cohort
Share of months in disruption window
Y ear 1 Y ear 2
B. Disrupted integration time by placement cohort
Notes: Panel A plots monthly COVID-19 deaths; the shaded area marks the disruption period. Panel B calculates,
for each case in the complete three year analysis sample, the shares of the first and second post-placement years
falling within the disruption period, and averages them by placement year.
4

S4 Descriptive statistics and balance checks
S4.1 Covariate balance
Table S2 reports descriptive statistics and covariate balance for the complete three year analysis
sample. Baseline means are nearly identical across arms, and no individual covariate difference is
significant at the 10% level. An omnibus Wald test that the 11 nonredundant covariate coefficients
are jointly zero in a linear probability model of treatment assignment likewise shows no evidence of
joint imbalance (F11,1,999 = 0.49, p = 0.91).
Table S2:Descriptive statistics and covariate balance.
Overall Control Treatment Diff. p
Female 0.163 0.161 0.165 +0.004 0.78
Age at arrival (yrs) 27.93 27.71 28.15 +0.45 0.27
Case size 1.34 1.33 1.34 +0.01 0.76
Single 0.603 0.618 0.588 −0.030 0.20
Married 0.364 0.355 0.373 +0.018 0.43
Origin group: Afghanistan 0.537 0.544 0.530 −0.014 0.54
Origin group: Turkey 0.257 0.256 0.259 +0.002 0.91
Origin group: Other 0.205 0.199 0.211 +0.012 0.52
Language: Dari 0.305 0.309 0.300 −0.009 0.66
Language: Turkish 0.177 0.174 0.180 +0.006 0.75
Language: Kurmanji 0.147 0.141 0.152 +0.012 0.48
Months arrival→placement 2.75 2.75 2.75 −0.00 1.00
Notes: The sample contains 2,156 adults in 2,000 cases (control= 1,073, treatment = 1,083 individuals).
Differences are treatment minus control. Row-specificp-values come from OLS regressions of each covariate on
treatment assignment, with standard errors clustered by case. Months from arrival to placement are capped at the
95th percentile.
S4.2 Design balance
Figure S3 shows the geographic balance produced by the mirrored quota design. Overall canton
shares are nearly identical across arms. The treatment and control distributions also remain similar
within origin groups, although these panels are noisier because of their smaller cell counts.
5

Figure S3:Canton balance overall and by origin group.
Other
Turkey
Afghanistan
All cases
ZH
BE
VD
AG
SG
GE
LU
TI
VS
FR
BL
TG
SO
GR
BS
NE
SZ
ZG
SH
JU
AR
NW
GL
OW
UR
AI
0%
5%
10%
15%
20%
0%
5%
10%
15%
20%
0%
5%
10%
15%
20%
0%
5%
10%
15%
20%
Canton
Share of cases within panel and arm
Control Treatment
Notes: Bars show, within each panel and experimental arm, the share of cases placed in each canton. Within each
panel, canton shares sum to 100% separately by arm. The largest canton-share difference is 0.76 percentage points
in the overall canton panel and 2.20 percentage points across the origin-group panels. The broadly similar
treatment and control patterns reflect the mirrored quota design.
Table S3 reports formal case-level checks of the mirrored quota design. Adherence to the dis-
played recommendation is similar across arms (p = 0.37). Neither the overall canton distribution
nor the joint canton-by-origin-group distribution differs detectably between arms (bothp >0.99).
The same geographic balance holds within placement cohorts and pooled eras.
6

Table S3:Balance checks for the mirrored quota design.
Check Sample Test p Max. diff. (pp)
Adherence to displayed recom-
mendation
2,000 cases difference in proportions 0.37 0.8
Canton distribution 2,000 cases Pearson χ2, Monte Carlop > 0.99 0.8
2020 cohort 291 cases 0.93 5.0
2021 cohort 497 cases > 0.99 2.4
2022 cohort 696 cases > 0.99 2.2
2023 cohort 516 cases > 0.99 2.0
COVID-era 2020–2021 788 cases > 0.99 1.0
Post-COVID 2022–2023 1,212 cases > 0.99 1.2
Canton-by-origin-group distri-
bution
2,000 cases Pearson χ2, Monte Carlop > 0.99 0.6
Notes: Adherence is defined as placement in the canton displayed to the placement officer. The adherence check
compares the share of adherent cases across assignment arms using the two-sample test for equality of proportions
with continuity correction (Pearsonχ2). For the canton and canton-by-origin-group checks,p-values are based on
100,000 Monte Carlo draws from the null distribution of the Pearsonχ2 statistic, holding the observed margins
fixed. The canton-by-origin-group check uses Afghanistan, Turkey, and Other—the groups balanced by the
assignment design—and expresses each cell as a share of all cases in the corresponding assignment arm. The
indented rows apply the canton-distribution check within placement cohorts and pooled eras. Max. diff. is the
largest absolute treatment-control difference for the row’s check, in percentage points: the adherent-case share for
the adherence row, canton shares for the canton-distribution rows, and canton-by-origin-group cell shares for the
origin-group row.
S4.3 Attrition checks
Attrition checks use all eligible cases randomized through the main sample’s June 13, 2023 selection
boundary, including cases without complete outcomes (2,209 adults in 2,050 cases). Because ZEMIS
does not record departure directly, loss to follow-up is proxied by the absence of an active ZEMIS
record at three years. This generally indicates that an individual left Switzerland, although it
may also capture people who remain but no longer interact with Swiss authorities or renew their
residence permits.
The proxy rate is nearly identical across arms: 2.5% in control and 2.3% in treatment. Covariate
adjustment and tests across predicted attrition risk and baseline characteristics likewise provide no
evidence of differential three year outcome observability by treatment (Table S4).
7

Table S4:Attrition checks: treatment and three year outcome observability.
Check Estimate/test p
Unadjusted treatment-control difference −0.29 pp 0.68
Covariate-adjusted treatment-control difference −0.27 pp 0.67
Treatment × predicted attrition risk +0.28 pp per SD 0.86
Omnibus treatment × covariate interactions χ2(56) = 37.62 0.97
High predicted-risk tercile, treatment-control difference +0.79 pp 0.67
Notes: Estimates are treatment-control differences in the lost-to-follow-up indicator from individual-level linear
probability models; the covariate-adjusted difference controls for the main-specification baseline covariates.
Predicted attrition risk is the fitted value from a linear probability model of the lost-to-follow-up indicator on the
main-specification baseline covariates, estimated on the pooled sample and standardized to one standard deviation.
Risk terciles are defined by the empirical terciles of this score. The omnibus check is a joint Wald test of the
treatment-by-covariate interactions. Standard errors are clustered by case.
S5 Local average treatment effects
The pre-analysis plan specifies instrumental-variable analyses in which random assignment to treat-
ment instruments placement in the GeoMatch-recommended canton. For treated cases, this is the
recommendation displayed to SEM placement officers. For control cases, it is the counterfactual
recommendation GeoMatch would have generated under treatment.
The PAP defines three instrumented placement measures. D1, the primary measure used in
the main text, indicates initial placement in the GeoMatch-recommended canton.D2 additionally
requires residence in that canton for at least half of the three year follow-up, whileD3 measures the
fraction of follow-up spent there. Both residence-based measures are constructed from administra-
tive address snapshots. These histories are nearly complete: among adults with nonmissingD1–D3,
the mean number of observed residence months is 35.9 out of 36.
Each measure is instrumented with random assignment. The coefficients for the binaryD1 and
D2 measures are local average treatment effects (LATEs). BecauseD3 is continuous, its coefficient
is an average causal response over cases whose treatment intensity is shifted by the instrument [1].
The first stage is below one for two reasons. First, placement officers occasionally overrode the
displayed recommendation. Second, the status quo procedure sometimes recommended the same
canton that GeoMatch would have recommended, placing some control cases in the GeoMatch-
recommended canton.
Interpreting the instrumental-variable estimates causally requires a strong first stage, the ex-
clusion restriction, and monotonicity. Monotonicity requires treatment assignment not to reduce
a case’s exposure to the GeoMatch-recommended canton. The exclusion restriction requires ran-
dom assignment to affect employment only through the instrumented placement measure. This is
not automatic becauseD1 collapses placement into the GeoMatch-recommended canton versus any
other canton. For example, suppose GeoMatch recommends canton A, but a treatment-arm officer
overrides that recommendation and assigns the case to canton B, while the status quo procedure
assigns the same case to canton C under control. Both assignments yieldD1 = 0, yet assignment
changes the case’s actual canton and could therefore affect employment. The same general concern
applies to D2 and D3.
The scope for such violations is very limited. Officer overrides affected only about 3% of cases,
and open-text explanations indicate that many reflected family ties, family-reunification rules, or
medical needs requiring placement in a particular canton. These placements were therefore likely to
8

be invariant to assignment. This evidence greatly reduces, but cannot eliminate, the potential for
exclusion-restriction violations. The prespecified ITT consequently remains the primary estimand.
Table S5 reports the instrumental-variable estimates and partial first-stageF-statistics. The
first stage is very strong: random assignment increasesD1 by about 88 percentage points in the
pooled sample. Estimates based on D2 and D3 are very similar to those based onD1, consistent
with the limited secondary migration in this setting.
Table S5:Full LATE estimates.
Indicator Sample N Mean D (C, %) Mean D (T, %) First stage F LATE p
D1 All cohorts (2020–2023) 2,000 8.5 96.5 88.2 7,107 +2.49 0.046
D1 Excluding peak COVID (2021–2023) 1,709 8.7 96.1 87.8 5,853 +3.11 0.022
D1 Post-COVID (2022–2023) 1,212 8.6 95.6 87.4 3,921 +4.59 0.006
D2 All cohorts (2020–2023) 2,000 8.2 93.1 85.1 5,368 +2.58 0.046
D2 Excluding peak COVID (2021–2023) 1,709 8.3 93.0 85.1 4,599 +3.21 0.022
D2 Post-COVID (2022–2023) 1,212 8.3 93.1 85.3 3,255 +4.70 0.006
D3 All cohorts (2020–2023) 2,000 8.4 94.4 86.2 6,331 +2.55 0.046
D3 Excluding peak COVID (2021–2023) 1,709 8.5 94.6 86.3 5,463 +3.16 0.022
D3 Post-COVID (2022–2023) 1,212 8.3 94.5 86.6 3,867 +4.63 0.006
Notes: D1 denotes initial placement in the GeoMatch-recommended canton;D2, initial placement in that canton
and remaining there for at least half of the three year follow-up period; andD3, the fraction of the three year
follow-up period spent in that canton. BecauseD3 is continuous, its coefficient is an average causal response
(ACR); for brevity, LATE is used as the umbrella label for all three estimands. MeanD columns are percentages;
first stage and LATE estimates are in percentage points. The first stage is the coefficient from a regression of each
placement measure on treatment assignment and the pre-registered covariates;F is the corresponding partial
first-stage F-statistic, and p is the p-value of the LATE estimate. The employment outcome is the case mean of
adult members’ three year employment;N counts cases.
S6 Effects by placement cohort
Figure S4 reports case-level ITT and LATE estimates separately by placement cohort. Estimates
are noisy and indistinguishable from zero in 2020 and 2021, but positive, statistically significant,
and similar in magnitude in 2022 and 2023.
9

Figure S4:Three year employment effects by placement cohort.
N=291 N=497 N=696 N=516
−10
−5
0
5
10
Treatment effect on 3−year employment (pp)
COVID−19
suspension
COVID−19 restrictions
lifted
PAP target
reached June 2023
0
50
100
2020 2021 2022 2023
Placement cohort
Cases placed
per month
ITT LATE
Notes: Points report case-level ITT and LATE estimates for the primary three year employment outcome,
estimated separately within each placement cohort. Models include the same pre-registered covariates as the main
analysis, entered additively. Case-level outcomes are the mean adult employment proportion within each placed
case. Bars show 95% confidence intervals. The top-panelN labels report observed cases; the bottom panel shows
their monthly placement volume. The bottom-panel annotation marks April–May 2020, when no trial placements
occurred during the initial COVID-19 lockdown.
Figure S5 provides a complementary robustness check using double/debiased machine learning
(DML) to estimate ITT group average treatment effects (GATEs) for the four placement cohorts.
The estimator uses cross-fitted orthogonal scores, regularized nuisance models, and the same ad-
justment covariates as the main analysis, except the placement-year indicators, which serve as the
moderator.6 The estimation sample is the complete three year analysis sample, and confidence in-
tervals use heteroskedasticity-robust standard errors. The DML estimates show the same temporal
progression: muted effects for the 2020 and 2021 cohorts and positive effects for the 2022 and 2023
cohorts. The pointwise confidence interval excludes zero for 2023.
6Implemented withinterflex’s dml option (gate = TRUE ), lasso-type nuisance models for the outcome and treat-
ment equations, five cross-fitting folds, and a fixed random seed for fold assignment.
10

Figure S5:DML effects by placement cohort.
N=291 N=497 N=696 N=516
−10
−5
0
5
10
2020 2021 2022 2023
Placement cohort
DML GATE on 3−year employment (pp)
Notes: Points report DML estimates of ITT GATEs for access to GeoMatch recommendations, with placement
cohort as a discrete moderator. The analysis uses the primary case-level outcome and regularized outcome and
treatment models with cross-fitting. Bars show 95% pointwise confidence intervals.
Figure S6 examines whether the cohort pattern depends on aggregating outcomes at the case
level. The individual-level ITT and LATE estimates show the same progression, with muted effects
in 2020 and 2021 and positive effects in 2022 and 2023.
11

Figure S6:Individual-level effects by placement cohort.
N=319 N=537 N=750 N=550
−10
−5
0
5
10
2020 2021 2022 2023
Placement cohort
Treatment effect on 3−year employment (pp)
ITT LATE
Notes: Points report individual-level ITT and LATE estimates for the three year employment outcome, estimated
separately within each placement cohort. Models use additive adjustment for the same pre-registered covariates as
the main analysis. Bars show 95% confidence intervals based on standard errors clustered by case.
S7 Robustness checks
Table S6 compares the PAP-primary Lin specification with five alternatives: additive adjustment,
post-double-selection LASSO, the Lin specification without canton indicators, the unadjusted differ-
ence, and inverse-probability-weighted attrition correction. Across all three samples, the estimates
are similar in magnitude and precision.
The specification without canton indicators addresses conditioning on realized placement canton,
which is determined after randomization. The mirrored quotas target the same marginal canton
distribution in both arms, and realized shares are nearly identical (the largest difference is 0.76
percentage points; Figure S3). Under exactly equal shares, the overall ITT equals a common-
canton-share-weighted average of the within-canton treatment–control contrasts. Estimates with
and without canton indicators are nearly unchanged in the pooled, excluding-peak-COVID, and
post-COVID samples (+2.19 versus +2.32 pp, +2.71 versus +2.92 pp, and +3.90 versus +4.10 pp,
respectively). The pre-registered specification remains primary, while the close agreement shows
that the results do not depend on conditioning on realized canton.
12

Table S6:Additional case-level three year employment specifications.
Sample Specification N Effect (pp) 95% CI (pp) p
All cohorts (2020–2023) PAP-primary Lin 2,000 +2.19 [+0 .05, +4.33] 0.045
Lin, no canton indicators 2,000 +2.32 [+0 .14, +4.51] 0.037
Additive adjustment 2,000 +2.19 [+0 .05, +4.34] 0.046
PDS LASSO 2,000 +2.32 [+0 .13, +4.51] 0.038
Unadjusted 2,000 +2.41 [+0 .03, +4.79] 0.048
Attrition IPW 2,000 +2.16 [+0 .01, +4.31] 0.049
Excluding peak COVID (2021–2023) PAP-primary Lin 1,709 +2.71 [+0 .39, +5.03] 0.022
Lin, no canton indicators 1,709 +2.92 [+0 .56, +5.29] 0.016
Additive adjustment 1,709 +2.73 [+0 .39, +5.06] 0.022
PDS LASSO 1,709 +2.86 [+0 .49, +5.23] 0.018
Unadjusted 1,709 +3.15 [+0 .57, +5.74] 0.017
Attrition IPW 1,709 +2.65 [+0 .32, +4.98] 0.026
Post-COVID (2022–2023) PAP-primary Lin 1,212 +3.90 [+1 .11, +6.68] 0.006
Lin, no canton indicators 1,212 +4.10 [+1 .23, +6.96] 0.005
Additive adjustment 1,212 +4.01 [+1 .18, +6.83] 0.006
PDS LASSO 1,212 +4.08 [+1 .20, +6.96] 0.006
Unadjusted 1,212 +4.17 [+1 .06, +7.28] 0.009
Attrition IPW 1,212 +3.87 [+1 .05, +6.69] 0.007
Notes: All rows report case-level ITT estimates on the three year employment proportion, with standard errors
clustered by case. The unadjusted, PDS LASSO, and attrition-IPW specifications were prespecified; the additive
and no-canton Lin specifications are additional checks. PDS is the pre-registered post-double-selection LASSO
estimator [2], implemented with the plug-in penalty and post-LASSO refit inhdm (rlasso). Controls selected in the
outcome and treatment equations are combined, and the treatment effect is re-estimated by OLS with standard
errors clustered by case. IPW denotes inverse-probability weighting for three year outcome observability.N counts
cases.
Individual-level estimates. Table S7 shows the same analysis as main-text Table 1 but com-
puted at the individual rather than the case level, with similar results.
Table S7:Individual-level three year employment estimates.
Sample Estimand N Ctrl. mean (%) β (pp) Gain 95% CI (pp) p
All cohorts (2020–2023) ITT 2,156 21.4 +1.95 +9 .1% [ −0.10, +4.01] 0.063
LATE 2,156 21.4 +2.23 +10 .4% [ −0.11, +4.57] 0.062
Excluding peak COVID (2021–2023) ITT 1,837 21.1 +2.44 +11 .6% [+0 .22, +4.66] 0.032
LATE 1,837 21.1 +2.82 +13 .3% [+0 .26, +5.38] 0.031
Post-COVID (2022–2023) ITT 1,300 21.4 +3.46 +16 .2% [+0 .80, +6.13] 0.011
LATE 1,300 21.4 +4.14 +19 .4% [+1 .01, +7.27] 0.010
Notes: ITT and LATE effects on the three year employment proportion, estimated as in main-text Table 1 but at
the individual rather than the case level.N counts individuals.
Table S8 tests sensitivity to the deterministic sample-selection rule by including all 2,046 com-
plete cases assigned through June 30, 2023, rather than the first 2,000 in assignment order. The
ITT and LATE estimates are nearly identical to those in main-text Table 1.
13

Table S8:Sample-definition sensitivity: all complete cases through June 2023.
Sample Estimand N Ctrl. mean (%) β (pp) 95% CI (pp) p
All cohorts (2020–2023) ITT 2,046 22.3 +2.14 [+0 .02, +4.25] 0.048
LATE 2,046 22.3 +2.41 [+0 .01, +4.82] 0.049
Excluding peak COVID (2021–2023) ITT 1,755 22.0 +2.63 [+0 .34, +4.92] 0.025
LATE 1,755 22.0 +2.99 [+0 .37, +5.61] 0.026
Post-COVID (2022–2023) ITT 1,258 22.2 +3.75 [+1 .01, +6.48] 0.007
LATE 1,258 22.2 +4.37 [+1 .22, +7.53] 0.007
Notes: ITT and LATE effects on the three year employment proportion, estimated as in main-text Table 1 using all
2,046 complete cases assigned through June 30, 2023 rather than the first 2,000 in assignment order.N counts cases.
S8 Effects over follow-up
Table S9 reports the point-in-time employment outcome shown in main-text Figure 2, measured in
the 36th month after placement. Case- and individual-level estimates are similar, with positive ITT
and LATE effects of comparable magnitude across the three samples.
Table S9:Point-in-time employment effects 36 months after placement.
Sample Unit Estimand N Ctrl. mean (%) β (pp) Gain 95% CI (pp) p
All cohorts (2020–2023) Case ITT 2,000 47.7 +5.17 +10 .8% [+1 .10, +9.25] 0.013
Case LATE 2,000 47.7 +5.96 +12 .5% [+1 .35, +10.57] 0.011
Individual ITT 2,156 44.8 +4.64 +10 .4% [+0 .78, +8.50] 0.019
Individual LATE 2,156 44.8 +5.40 +12 .0% [+1 .01, +9.79] 0.016
Excluding peak COVID (2021–2023) Case ITT 1,709 47.4 +5.19 +11 .0% [+0 .80, +9.58] 0.021
Case LATE 1,709 47.4 +6.04 +12 .8% [+1 .05, +11.03] 0.018
Individual ITT 1,837 44.4 +4.58 +10 .3% [+0 .43, +8.72] 0.031
Individual LATE 1,837 44.4 +5.34 +12 .0% [+0 .59, +10.09] 0.028
Post-COVID (2022–2023) Case ITT 1,212 48.4 +5.48 +11 .3% [+0 .19, +10.77] 0.043
Case LATE 1,212 48.4 +6.55 +13 .5% [+0 .53, +12.57] 0.033
Individual ITT 1,300 45.8 +4.46 +9 .7% [ −0.58, +9.50] 0.083
Individual LATE 1,300 45.8 +5.45 +11 .9% [ −0.34, +11.25] 0.065
Notes: The outcome is employment in the 36th month after placement: the adult’s own employment for
individual-level rows, and whether any adult in the case is employed for case-level rows. It was not specified in the
PAP. ITT and LATE estimates use the same specifications as main-text Table 1. The outcome is observed for units
active in the registry in month 36.
Figure S7 complements this point-in-time measure by reporting effects on the share of months
employed over the first one, two, and three years. Each panel uses the same complete three year
sample at every horizon, ensuring that changes across horizons do not reflect changes in sample
composition. Effects generally increase over follow-up for both units and estimands, with the largest
three year estimates in the post-COVID cohorts.
14

Figure S7:Employment effects by follow-up horizon, unit, and estimand.
All cohorts
2020−2023
Excluding peak COVID
2021−2023
Post−COVID
2022−2023
IndividualCase
1y 2y 3y 1y 2y 3y 1y 2y 3y
0
2
4
6
8
0
2
4
6
8
Employment follow−up horizon
Treatment effect on employment (pp)
Estimand ITT LATE
Notes: Points report individual- and case-level ITT and LATE estimates for the share of months employed over the
first one, two, and three years. The three samples match those in main-text Table 1. ITT estimates use the
PAP-primary Lin specification; LATE estimates instrument initial placement in the GeoMatch-recommended
canton with treatment assignment. Standard errors are clustered by case. Bars show 95% confidence intervals. The
case-level three year estimates correspond to main-text Table 1.
S9 Distributional analysis
Figure S8 plots empirical cumulative distribution functions (ECDFs) of the case-level primary out-
come by assignment arm. Across all three samples, the treatment ECDF lies below the control
ECDF over almost all of the support, with the clearest separation after COVID. In that sample, the
share with zero employment over three years is 34.4% versus 39.0% in the treatment and control
arms, respectively. Table S10 reports formal permutation tests for first-order stochastic dominance
and a treatment-favoring shift. These comparisons describe marginal outcome distributions, not
individual-level gains or losses, which are not identified without additional assumptions.
15

Table S10:Distributional effects on three year employment.
FOSD test Shift-right test
Sample D− (pp) p D + (pp) p
All cohorts (2020–2023) 0.72 0.82 5.41 0.035
Excluding peak COVID (2021–2023) 0.26 0.93 6.47 0.018
Post-COVID (2022–2023) 0.36 0.91 8.76 0.007
Notes: The FOSD test uses the Barrett–Donald supremum statistic [3],D− = supy{FT (y) − FC (y)}, where FT and
FC are the treatment- and control-arm empirical distribution functions of the case-level primary outcome, under
H0 : FT (y) ≤ FC (y) for all y; larger p-values are consistent with treatment first-order stochastic dominance. The
shift-right test usesD+ = supy{FC (y) − FT (y)} as a one-sided KS statistic under distributional equality.p-values
are from randomization inference—5,000 permutations of assignment labels, including the observed
assignment—which calibrates both tests at distributional equality, the least-favorable configuration of the
dominance null; the FOSD test is therefore conservative for the composite null. Statistics are in percentage points.
Figure S8:Distributions of three year employment by assignment arm.
Zero employment: C 39%, T 37% Zero employment: C 40%, T 37% Zero employment: C 39%, T 34%
All cohorts
(2020−2023)
Excluding peak COVID
(2021−2023)
Post−COVID
(2022−2023)
0 50 100 0 50 100 0 50 100
0
25
50
75
100
Realized 3−year employment proportion (%)
Cumulative share of cases (%)
Control Treatment
Notes: Panels plot ECDFs of realized three year employment proportions for the samples used in main-text Table 1.
A treatment curve below the control curve indicates fewer treatment cases at or below that employment level.
Labels report the share with zero employment during follow-up.
S10 Secondary outcomes
Table S11 collects the case-level secondary-outcome estimates using the main covariate adjustment.
Panel A reports three pre-registered outcomes: any employment during the three year period, the
lost-to-follow-up proxy, and secondary migration. The ITT for any employment is+2.26 pp in the
pooled sample (p = 0.253) and +4.78 pp in the post-COVID cohorts (p = 0.063). This outcome
indicateswhetheranyadultworkedatanypointduringthe36-monthfollow-up, evenbriefly, whereas
the primary outcome captures the share of months employed.
The lost-to-follow-up measure indicates whether any adult lacks an active ZEMIS record at three
years, using the same emigration proxy as the attrition checks (Sec. S4.3). The ITT is−0.07 pp in
16

the pooled sample (p = 0.915) and −0.21 pp in the post-COVID cohorts (p = 0.808). Secondary
migration indicates whether any case member resided outside the initial placement canton during
follow-up. Its ITT is+0.35 pp in the pooled sample (p = 0.714) and −1.71 pp in the post-COVID
cohorts (p = 0.171). Neither outcome differs detectably by treatment.
Panels B and C report additional timing and stability outcomes not specified in the PAP. For
time to first job (Panel B), the ITT implies that the first adult in the case obtains employment0.78
months sooner in the pooled sample (p = 0.100) and1.45 months sooner in the post-COVID cohorts
(p = 0.021). This measure counts months until any adult first obtains employment, censored at 36
months.
Treatment also improves sustained employment. The ITT for having a single job spell of at least
six months is 5.57 pp in the pooled sample (p = 0.007) and 9.56 pp in the post-COVID cohorts
(p <0.001). A six-month spell requires at least 183 covered days in one job within follow-up months
1–36, excluding the partial assignment month and counting both spell endpoints.
The ITT for having an open-ended contract at three years is4.45 pp in the pooled sample
(p = 0.029) and 7.07 pp in the post-COVID cohorts (p = 0.008). This measure approximates
whether any adult held an open-ended contract at three years, counting only jobs that began
during follow-up months 1–36.
Panel C reports the longest single job spell in days, taking the maximum across adults using
the same duration construction. The ITT is14.53 days in the pooled sample (p = 0.168) and 33.12
days in the post-COVID cohorts (p = 0.017).
Monthly-resolution robustness checks yield a similar pattern while allowing consecutive em-
ployment months to span different jobs. The ITT for at least six consecutive months with any
employment is +4.82 pp in the pooled sample (p = 0.020) and +8.82 pp in the post-COVID co-
horts (p <0.001), compared with +5.57 and +9.56 pp for a single job spell of at least 183 days.
The corresponding effects on the longest run of employment months are+0.57 months (p = 0.135)
and +1.24 months (p = 0.013), respectively, mirroring the larger post-COVID gains in single-job
duration.
17

Table S11:Case-level secondary outcomes and three year employment margins.
Panel A. Pre-registered secondary outcomes
Outcome Sample Estimand Scale Control Effect 95% CI p N
Ever employed within 3y All ITT pp 60.86 +2.26 [ −1.61, +6.13] 0.253 2,000
Ever employed within 3y All LATE pp 60.86 +2.71 [ −1.69, +7.12] 0.228 2,000
Ever employed within 3y Excl. peak COVID ITT pp 60.26 +2.78 [ −1.41, +6.96] 0.194 1,709
Ever employed within 3y Excl. peak COVID LATE pp 60.26 +3.36 [ −1.44, +8.15] 0.170 1,709
Ever employed within 3y Post-COVID ITT pp 60.99 +4.78 [ −0.25, +9.81] 0.063 1,212
Ever employed within 3y Post-COVID LATE pp 60.99 +5.84 [+0 .06, +11.62] 0.048 1,212
Any adult left CH / not observed at 3y (proxy) All ITT pp 2.54 −0.07 [ −1.39, +1.25] 0.915 2,050
Any adult left CH / not observed at 3y (proxy) All LATE pp 2.54 −0.12 [ −1.60, +1.37] 0.878 2,050
Any adult left CH / not observed at 3y (proxy) Excl. peak COVID ITT pp 2.51 −0.00 [ −1.43, +1.42] 0.998 1,753
Any adult left CH / not observed at 3y (proxy) Excl. peak COVID LATE pp 2.51 −0.01 [ −1.62, +1.61] 0.995 1,753
Any adult left CH / not observed at 3y (proxy) Post-COVID ITT pp 2.73 −0.21 [ −1.94, +1.51] 0.808 1,246
Any adult left CH / not observed at 3y (proxy) Post-COVID LATE pp 2.73 −0.15 [ −2.14, +1.83] 0.879 1,246
Any case member outside initial canton, 3y All ITT pp 5.41 +0.35 [ −1.54, +2.25] 0.714 2,000
Any case member outside initial canton, 3y All LATE pp 5.41 +0.43 [ −1.72, +2.58] 0.694 2,000
Any case member outside initial canton, 3y Excl. peak COVID ITT pp 5.51 −0.29 [ −2.31, +1.73] 0.777 1,709
Any case member outside initial canton, 3y Excl. peak COVID LATE pp 5.51 −0.34 [ −2.64, +1.96] 0.774 1,709
Any case member outside initial canton, 3y Post-COVID ITT pp 6.12 −1.71 [ −4.16, +0.74] 0.171 1,212
Any case member outside initial canton, 3y Post-COVID LATE pp 6.12 −2.01 [ −4.78, +0.77] 0.157 1,212
Panel B. Employment timing and stability outcomes
Outcome Sample Estimand Scale Control Effect 95% CI p N
First job in case, censored at 36m All ITT months 25.34 −0.78 [ −1.71, +0.15] 0.100 2,000
First job in case, censored at 36m All LATE months 25.34 −0.89 [ −1.95, +0.17] 0.100 2,000
First job in case, censored at 36m Excl. peak COVID ITT months 25.46 −1.05 [ −2.06, −0.04] 0.043 1,709
First job in case, censored at 36m Excl. peak COVID LATE months 25.46 −1.20 [ −2.36, −0.04] 0.042 1,709
First job in case, censored at 36m Post-COVID ITT months 25.22 −1.45 [ −2.67, −0.22] 0.021 1,212
First job in case, censored at 36m Post-COVID LATE months 25.22 −1.72 [ −3.14, −0.30] 0.018 1,212
Single job spell of at least 183 days All ITT pp 40.24 +5.57 [+1 .50, +9.64] 0.007 2,000
Single job spell of at least 183 days All LATE pp 40.24 +6.39 [+1 .78, +11.00] 0.007 2,000
Single job spell of at least 183 days Excl. peak COVID ITT pp 39.39 +6.65 [+2 .25, +11.06] 0.003 1,709
Single job spell of at least 183 days Excl. peak COVID LATE pp 39.39 +7.72 [+2 .70, +12.74] 0.003 1,709
Single job spell of at least 183 days Post-COVID ITT pp 40.00 +9.56 [+4 .30, +14.82] < 0.001 1,212
Single job spell of at least 183 days Post-COVID LATE pp 40.00 +11.19 [+5 .16, +17.21] < 0.001 1,212
Open-ended contract (3y) All ITT pp 34.73 +4.45 [+0 .46, +8.44] 0.029 2,000
Open-ended contract (3y) All LATE pp 34.73 +5.17 [+0 .63, +9.71] 0.026 2,000
Open-ended contract (3y) Excl. peak COVID ITT pp 34.82 +5.41 [+1 .10, +9.73] 0.014 1,709
Open-ended contract (3y) Excl. peak COVID LATE pp 34.82 +6.27 [+1 .33, +11.20] 0.013 1,709
Open-ended contract (3y) Post-COVID ITT pp 36.20 +7.07 [+1 .84, +12.29] 0.008 1,212
Open-ended contract (3y) Post-COVID LATE pp 36.20 +8.33 [+2 .34, +14.31] 0.006 1,212
Notes: Panel A reports ITT and LATE estimates for the three pre-registered secondary outcomes across the three
analysis samples, using the PAP-primary Lin covariate set. Sample abbreviations follow main-text Table 1: All
cohorts (2020–2023), Excluding peak COVID (2021–2023), and Post-COVID (2022–2023). LATE estimates
instrument initial placement in the GeoMatch-recommended canton with treatment assignment. Panel B reports
the additional employment timing and stability outcomes shown in main-text Figure 3; the any-employment
estimates plotted there are reported in Panel A. The Scale column gives the units for the Effect, 95% CI, and
Control columns: percentage-point rows use percentage points for effects and percentages for control means; month
rows use months.N counts cases.
18

Table S11:Case-level secondary outcomes and three year employment margins (continued).
Panel C. Job duration and monthly-resolution robustness checks
Outcome Sample Estimand Scale Control Effect 95% CI p N
Longest single job spell All ITT days 200.73 +14.53 [ −6.11, +35.17] 0.168 2,000
Longest single job spell All LATE days 200.73 +16.86 [ −6.61, +40.34] 0.159 2,000
Longest single job spell Excl. peak COVID ITT days 198.97 +19.58 [ −2.99, +42.14] 0.089 1,709
Longest single job spell Excl. peak COVID LATE days 198.97 +22.79 [ −3.06, +48.65] 0.084 1,709
Longest single job spell Post-COVID ITT days 199.23 +33.12 [+5 .84, +60.40] 0.017 1,212
Longest single job spell Post-COVID LATE days 199.23 +39.34 [+7 .64, +71.05] 0.015 1,212
6+ consecutive employment months All ITT pp 44.74 +4.82 [+0 .76, +8.88] 0.020 2,000
6+ consecutive employment months All LATE pp 44.74 +5.56 [+0 .94, +10.18] 0.018 2,000
6+ consecutive employment months Excl. peak COVID ITT pp 44.08 +5.87 [+1 .47, +10.28] 0.009 1,709
6+ consecutive employment months Excl. peak COVID LATE pp 44.08 +6.78 [+1 .75, +11.82] 0.008 1,709
6+ consecutive employment months Post-COVID ITT pp 44.46 +8.82 [+3 .59, +14.06] < 0.001 1,212
6+ consecutive employment months Post-COVID LATE pp 44.46 +10.40 [+4 .40, +16.41] < 0.001 1,212
Longest run of employment months All ITT months 7.56 +0.57 [ −0.18, +1.32] 0.135 2,000
Longest run of employment months All LATE months 7.56 +0.66 [ −0.20, +1.51] 0.132 2,000
Longest run of employment months Excl. peak COVID ITT months 7.46 +0.76 [ −0.05, +1.58] 0.067 1,709
Longest run of employment months Excl. peak COVID LATE months 7.46 +0.88 [ −0.06, +1.82] 0.065 1,709
Longest run of employment months Post-COVID ITT months 7.45 +1.24 [+0 .26, +2.21] 0.013 1,212
Longest run of employment months Post-COVID LATE months 7.45 +1.46 [+0 .33, +2.59] 0.012 1,212
Notes: Panel C uses the same case-level estimators and samples as Panels A–B. The longest single job is measured
in covered days; monthly measures can include consecutive employment in different jobs.
S11 Placement ranks and predicted gains
Main-text Figure 4 combines three diagnostics of how the recommendation system changed place-
ments and how its predictions aligned with realized outcomes. All panels use the pooled, COVID-era
(2020–2021), and post-COVID (2022–2023) samples.
Placement ranks (Panel A). For each adult, the deployed model predicts three year employ-
ment in each of the 26 cantons. The assigned canton is ranked within this profile from 1 (highest
predicted employment) to 26 (lowest); ties receive the best rank in the tied set. Panel A plots
the within-arm distribution of these ranks for each sample. Curves are fit using LOESS smoothing
(span 0.35, degree 2), evaluated on a fine grid and truncated at zero. The horizontal axis is reversed
so that better ranks appear on the right.
Rank-on-rank relationship (Panel B). To place predicted ranks and realized outcomes on
a common scale, the assigned-canton rank score,(26 − rank)/25, and the realized three year em-
ployment outcome are converted to percentiles within each sample. Percentiles use ranks scaled to
[0, 1], with ties assigned their average rank. Adults are grouped into quintiles of the placement-rank
percentile, and Panel B plots the mean realized-outcome percentile in each bin with 95% intervals
based on the within-bin standard error. The dashed line is the 45-degree line; the slope printed in
each panel is the coefficient from an adult-level regression of the realized-outcome percentile on the
placement-rank percentile.
Predicted versus realized gains (Panel C). Predicted employment at the assigned canton
is taken from the same 26-canton profile and averaged across adults within each case. For each
sample, the predicted gain is 100 times the treatment coefficient from an OLS regression of the
case mean prediction on treatment assignment, with HC2 standard errors. The realized gain is the
19

corresponding case-level ITT estimate from the main analysis. Panel C reports both quantities for
each sample, with 95% intervals.
S12 Fiscal benchmark
The main-text cost-benefit calculation converts the individual-level ITT estimates into additional
employment-months per adult. Each additional employment-month is valued at CHF 1,950 in the
central scenario (all monetary amounts are in Swiss francs; CHF 1≈ USD 1.2 at September 2026
exchange rates). This benchmark combines reduced federal support to cantons with employment-
related social-security contributions and source taxes, with CHF 1,500 and CHF 2,500 as lower and
upper sensitivity values.
The largest component is federal support for unemployed refugees. In 2026, the SEM’s national
lump sum for recognized and provisionally admitted refugees was approximately CHF 1,500 per
person per month.7
Because ZEMIS does not include wages, the earnings benchmark comes from an SEM analysis
linkingZEMISrecordsto2023pensioncontributions. Amongemployedasylumseekersandrefugees,
mean gross earnings were CHF 2,932 per month. Months without earnings are excluded [4]. At
this level, combined employer and employee AHV/IV/EO/ALV contributions equal 12.8%, or about
CHF 375 per month.8 Source-tax rates vary by canton, and the benchmark uses Zurich’s rate for a
single taxpayer without children or church tax. At monthly earnings of CHF 2,932, the applicable
rate is 2.56%, or approximately CHF 75.9
Together, the CHF 1,500 support benchmark, CHF 375 in social-security contributions, and
CHF 75 in source taxes yield approximately CHF 1,950 per additional employment-month per
adult. The CHF 1,500–2,500 sensitivity range accommodates uncertainty about actual transfers,
exceptions to the federal payment rule, canton-level variation in taxes and benefits, and household
size. Implementation costs are set at CHF 50 per treated adult, covering the marginal operating
costs. The main text details what this figure includes and why one-time development and integration
costs are excluded.
S13 Comparison with backtest
The original Swiss backtest by Bansak et al. [5] evaluated employment at the end of the third
calendar year after arrival among working-age asylum seekers granted subsidiary protection. Using
1999–2013registerdataandthe2013arrivalcohortasthetestset, itpredictedthatoptimizedcanton
assignment would raise employment from 15% to 26%, an 11 percentage-point or 73% relative gain.
The closest trial comparison is individual employment in the 36th month after placement. In
the pooled trial sample, control-arm employment at that horizon is 44.8%, and the individual-level
7For refugees aged 25 or older, employment paying more than CHF 600 per month generally ends
this payment; it continues for younger refugees and for adults earning CHF 600 or less. Sources:
SEM, “Neues Finanzierungssystem Asyl und Bundesabgeltungen,” December 2022, available at https:
//www.sem.admin.ch/dam/sem/de/data/asyl/sozialhilfe/factsheet-neues-finanzierungssystem.pdf.
download.pdf/factsheet-neues-finanzierungssystem-d.pdf; SEM, “Anhang 3 zu Weisung III / 7: Anpassung der
Pauschalansätze ab 1. Januar 2026,” available athttps://www.sem.admin.ch/dam/sem/de/data/rechtsgrundlagen/
weisungen/asyl/sozial-_und_nothilfe/anh3-ansaetze-2026.pdf.download.pdf/anh3-ansaetze-2026-d.pdf .
8Informationsstelle AHV/IV, “Lohnbeiträge an die AHV, die IV und die EO,” available athttps://www.ahv-iv.
ch/p/2.01.d; Informationsstelle AHV/IV, “Beiträge an die Arbeitslosenversicherung,” available at https://www.
ahv-iv.ch/p/2.08.d.
9Kantonales Steueramt Zürich, “Quellensteuer-Tarife: Ausgabe 2026, Kanton Zürich,” available athttps://www.
zh.ch/de/steuern-finanzen/steuern/quellensteuer/quellensteuer-tarife.html.
20

ITT estimate is +4.6 pp (95% CI [+0.8, +8.5]). The corresponding case-level ITT is+5.2 pp on
a control mean of 47.7% (Table S9). Because officer adherence was high, adjusting the ITT for
treatment-arm nonadherence while retaining chance control matches would increase it only slightly.
The trial therefore achieved roughly half of the original 11 pp backtest prediction.
The larger difference in relative terms (73% in the backtest versus roughly 10% for the trial ITT)
mainly reflects different control means: 15% in the 2013 backtest population and approximately 45%
in the trial. Even an identical percentage-point gain would represent a much smaller proportional
increase in the trial.
The deployed policy also faced constraints absent from the backtest. Most importantly, the
backtest imposed no origin-group quotas and could exploit origin-by-canton complementarities,
including co-ethnic networks and language-region matches [6, 7, 8]. The trial held origin-group
shares fixed across cantons, largely removing this channel. The backtest also optimized a complete
cohort ex post, whereas the trial assigned cases sequentially. Finally, the deployed model used fewer
predictors and initially relied on pre-pandemic training data.
Diagnostics for the policy actually deployed provide a more direct comparison. In the post-
COVID cohorts, the backtest-style predicted gain for the deployed policy (3.0 pp) is close to the
realized case-level ITT (3.9 pp) shown in main-text Figure 4. The original backtest remains a
useful benchmark rather than a directly comparable estimand: it uses fitted predictions under a
counterfactual cohort-wide reallocation, whereas the trial uses realized outcomes to estimate effects
under prospective deployment.
S14 AI-assisted preparation
Generative AI tools (OpenAI ChatGPT/Codex, GPT-5; Anthropic Claude) were used to assist with
manuscript editing, LATEX formatting, and code review and implementation. The authors reviewed
and verified all analyses, outputs, interpretations, and final text, and take full responsibility for the
content of the article.
References
[1] Angrist, J. D. & Imbens, G. W. Two-stage least squares estimation of average causal effects in
models with variable treatment intensity.Journal of the American Statistical Association 90,
431–442 (1995).
[2] Belloni, A., Chernozhukov, V. & Hansen, C. High-dimensional methods and inference on struc-
tural and treatment effects.Journal of Economic Perspectives 28, 29–50 (2014).
[3] Barrett, G. F. & Donald, S. G. Consistent tests for stochastic dominance.Econometrica 71,
71–104 (2003).
[4] Staatssekretariat für Migration (SEM). Bericht Statistische Auswertung der AHV-Bruttolöhne
2023 von Personen aus dem Asyl- und Flüchtlingsbereich: Datenmaterial der Zentralen Ausgle-
ichsstelle(ZAS). Tech.Rep.252.62-771/3/20/2/1, StaatssekretariatfürMigration, Bern-Wabern
(2025).
[5] Bansak, K. et al. Improving refugee integration through data-driven algorithmic assignment.
Science 359, 325–329 (2018).
21

[6] Martén, L., Hainmueller, J. & Hangartner, D. Ethnic networks can foster the economic integra-
tion of refugees. Proceedings of the National Academy of Sciences 116, 16280–16285 (2019).
[7] Auer, D. Language roulette – the effect of random placement on refugees’ labour market inte-
gration. Journal of Ethnic and Migration Studies 44, 341–362 (2018).
[8] Schmid, L. The impact of host language proficiency on migrants’ employment outcomes.Amer-
ican Economic Review: Insights 5, 477–493 (2023).
22
