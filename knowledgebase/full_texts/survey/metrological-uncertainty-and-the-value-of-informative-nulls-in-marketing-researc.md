---
title: Metrological uncertainty and the value of informative nulls in marketing research
url: https://doi.org/10.1057/s41270-026-00465-3
category: survey
subcategory: measurement
date: 2026-03
venue: Journal of Marketing Analytics
authors:
- Marko Sarstedt
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1057/s41270-026-00465-3.pdf
pages: 7
chars: 33500
fetched_at: '2026-11-08T17:56:28+00:00'
kb_version: 1
---

# Metrological uncertainty and the value of informative nulls in marketing research

ORIGINAL ARTICLE
Journal of Marketing Analytics
https://doi.org/10.1057/s41270-026-00465-3
However, this framing risks misdiagnosing the underly -
ing problem. The challenge is not merely that too few null
results are reported, but that empirical findings are routinely
interpreted with unwarranted confidence. Standard inferen -
tial practices assess uncertainty almost exclusively in terms
of random sampling variance, typically through p-values or
confidence intervals defined by a fixed significance thresh -
old (Cohen 1994; Rigdon 2023; Wasserstein et al. 2019).
This narrow treatment of uncertainty can create the appear-
ance of precise and decisive evidence even when the true
uncertainty surrounding an effect is substantially larger.
Moreover, it obscures the distinction between statistical
detectability and practical relevance.
A broader perspective is offered by the concept of met -
rological uncertainty, long established in the physical sci -
ences. Metrological uncertainty refers to the degree of
confidence that can be placed in a measurement of a quan -
tity or effect, taking into account all relevant sources of
imprecision (Bell 2001). In addition to sampling variability,
this includes uncertainty arising from data quality, model
specification, analytic choices, and many more (Sarstedt et
al. 2024). Conventional confidence intervals that do not take
Introduction
Debates about null results in empirical research are typically
framed in terms of scarcity. Studies that fail to detect statis-
tically significant effects are less likely to be published and
disseminated (e.g., Dwan et al. 2013; Fanelli 2012; Brodeur
et al. 2022), a phenomenon widely described as publication
bias (Soliman et al. 2025). This selective visibility contrib-
utes to an overrepresentation of statistically significant,
“novel,” or “surprising” findings in the literature (Rosenthal
1979) and has been argued to distort theoretical develop -
ment and practical inference (Knight 2003).
  Marko Sarstedt
sarstedt@lmu.de
1 Ludwig-Maximilians-University Munich, LMU Munich
School of Management, Ludwigstraße 28 RG/III,
80539 Munich, Germany
2 Faculty of Economics and Business Administration, Babeș-
Bolyai University, Cluj-Napoca, Romania
Abstract
Null results in empirical research are commonly framed as scarce outcomes suppressed by publication bias. This paper
argues that the central problem is not the absence of null findings, but the systematic misinterpretation of uncertain evi -
dence as informative effects due to overly narrow conceptions of uncertainty. Drawing on metrology, the science of mea -
surement in the physical sciences, the paper introduces metrological uncertainty as a broader framework for interpreting
null results that integrates sampling variability with uncertainty arising from measurement imprecision, model dependence,
and contextual factors. From this perspective, many statistically significant findings may overstate evidential strength,
while many nonsignificant results remain genuinely uninformative. The paper develops the concept of informative nulls,
defined not by the inclusion of zero but by the exclusion of substantively meaningful effect sizes. A three-step inferential
framework is proposed—recognize uncertainty, minimize it, and evaluate it against predefined regions of practical equiva -
lence. This approach reframes debates on null results, replicability, and practical relevance, and offers a more transparent
and cumulative foundation for marketing research inference.
Keywords File-drawer problem · Metrological uncertainty · Null effects · Open science · Publication bias · Region of
practical equivalence (ROPE)
Received: 9 February 2026 / Accepted: 10 February 2026
© The Author(s) 2026
Metrological uncertainty and the value of informative nulls in
marketing research
Marko Sarstedt1,2

M. Sarstedt
these sources into account understate the range of plausible
effect sizes supported by the data. From this perspective,
many results that are labeled as statistically “significant”
may in fact be false positives when recognizing that the dis-
tribution of plausible outcomes is much wider than implied
by sampling variability-centered paradigm (Rigdon et al.
2020). The problem, therefore, is not an absence of null
results in published research, but a systematic tendency to
misclassify uncertain evidence as informative effects, often
without regard to the magnitude of effects that would matter
in practice (Lakens et al. 2018).
This paper advances the argument that metrologi -
cal uncertainty constitutes a critical yet underappreciated
source of epistemic bias in marketing research. By explic -
itly recognizing and quantifying uncertainty beyond random
sampling variance, null results and apparent replication dis-
crepancies can be reinterpreted not as failures of detection,
but as informative evidence about the limits of what can be
known given existing measures, data, and models.
Metrological uncertainty
In metrology—the science of measurement in the physical
sciences—each measurement is accompanied by a stated
uncertainty, which characterizes the range of values plau -
sibly consistent with the measurement result, given all rec -
ognized sources of imprecision (JCGM/WG1). Although
metrological accounts often describe this range in relation
to a “true” value of the measurand (i.e., the quantity being
measured), this language reflects epistemic uncertainty
about a target quantity rather than a claim about a directly
observable or perfectly knowable ground truth (Crowder et
al. 2020; Chap. 2).
This conception differs from conventional measurement
frameworks in the behavioral sciences, particularly psycho-
metrics. In classical test theory, a “true value” is defined
operationally as the expected value of a measurement over
repeated samplings. Measurement error is then conceptual -
ized as deviation from this expectation. Formally, this rela -
tionship is expressed as.
X = T + E, where.
T denotes the long-run average score, and E captures ran-
dom and systematic error (Nunnally and Bernstein 1994).
In this framework, T is a statistical expectation defined
relative to a specific measurement process, not an onto -
logically fixed attribute. Distinguishing a model-dependent
expectation from a realist notion of a true value is a crucial
conceptual difference between psychometric error and met-
rological uncertainty (Crowder et al. 2020; Chap. 2). Rather
than describing a specific discrepancy between an observed
value and a presumed true value, metrological uncertainty
quantifies the degree of doubt associated with the measure -
ment result itself, integrating multiple sources of impreci -
sion beyond sampling variability (Fisher and Stenner 2023).
This degree of doubt is typically expressed as an uncertainty
interval, representing the range of plausible values sup -
ported by the data given limitations in measurement, data
quality, and modeling (Milinković and Jovičić 2023).
In marketing research, measurement practices are error-
centric, emphasizing the detection and minimization of
measurement error rather than the explicit characterization
of uncertainty (Rigdon et al. 2020). Yet marketing measure-
ments are subject to substantial uncertainty arising from
multiple sources not captured by the conventional error
framework, including ambiguity in concept definitions
(V oss et al. 2020), imprecision in measurement instruments
(Rossiter 2002), sampling and coverage error (Qian and
Xie 2022), and construct drift as metrics change meaning
over time (Bergkvist and Eisend 2023). By treating preci -
sion as achievable primarily through error reduction, mar -
keting research underrepresents the probabilistic nature of
measurement and conveys unwarranted exactness (Rigdon
and Sarstedt 2022), with adverse consequences for the rep -
licability of empirical findings (Rigdon et al. 2020; Sarstedt
et al. 2024).
Metrological uncertainty intervals provide a more com -
prehensive representation of the limits of inference than
error-centric summaries, but their mere existence does not
by itself determine what substantive conclusions can be
drawn. Acknowledging uncertainty often widens inferential
bounds, increasing epistemic caution but not necessarily
yielding informative conclusions about an effect. Whether
a result is informative depends not only on whether uncer -
tainty is acknowledged, but on whether it is sufficiently
constrained to rule out substantively relevant possibilities.
Specifically, a result is informative when the uncertainty
interval it yields excludes effect sizes that would mean -
ingfully alter theory or practice; it is uninformative when
the interval remains compatible with a wide range of sub -
stantively different outcomes (Hanel and Mehler 2019).
Importantly, informativeness is therefore an interval-level
property, but it concerns which values can be ruled out, not
whether a particular value—such as zero—is included.
Central to this assessment is the specification of a small-
est effect size of interest (SESOI). The SESOI represents the
minimum magnitude of an effect that would be considered
theoretically, managerially, or practically meaningful (Lak-
ens et al. 2018; Riesthuis 2024). Once specified, the SESOI
induces a region of practical equivalence (ROPE) around
zero—typically [−δ, +δ ], where δ  is the SESOI—within
which effects are treated as substantively equivalent to no
effect. An informative null conclusion is warranted only

Metrological uncertainty and the value of informative nulls in marketing research
when the uncertainty interval lies entirely within this region,
thereby excluding effects large enough to matter.
Figure 1 contrasts two hypothetical cases with different
confidence and uncertainty intervals, highlighting when
uncertainty is sufficiently constrained to support a substan -
tive conclusion. Panel A illustrates a case in which uncer -
tainty is fully recognized but remains too large to support an
informative conclusion. Under a conventional error-centric
analysis that considers sampling variability alone, the con -
fidence interval [1; 7] excludes zero and would typically be
interpreted as evidence of a statistically significant effect.
Once additional sources of uncertainty are incorporated
such as measurement imprecision or model dependence,
the resulting uncertainty interval widens to [-6; 8], thereby
including zero. However, crucially, the expanded interval
also extends beyond the ROPE of [-5; 5], meaning that
effects large enough to be practically important remain plau-
sible (in both directions). In other words, the data remain
compatible with a range of possibilities, including effects
that would be practically important (i.e., they fall outside
the ROPE). The result is best described as uninformative:
uncertainty has been recognized, but meaningful effects
cannot yet be ruled out.
Panel B depicts a contrasting case in which uncertainty is
both recognized and sufficiently reduced. Here, the uncer -
tainty interval of [-3; 4] includes zero but lies entirely within
the ROPE of [-5; 5]. In this situation, all effect sizes that
remain plausible given the data are smaller than the thresh -
old of practical importance. Although the analysis does not
establish that the effect is exactly zero, it supports the stron-
ger and more relevant conclusion that any effect present is
unlikely to matter in substantive terms. This is what consti-
tutes an informative null: not the mere inclusion of zero, but
the exclusion of effects that would meaningfully alter theory
or practice.
Together, the two panels illustrate why informative nulls
require more than statistical nonsignificance. Recognizing
uncertainty may initially widen inferential bounds and ren -
der conclusions more tentative, as in Panel (A). Only when
uncertainty is sufficiently constrained relative to a clearly
defined ROPE, does a null result become informative, as
in Panel (B). This distinction underscores the importance
of specifying practical significance thresholds in advance
and evaluating results in terms of exclusion rather than
inclusion.
Table 1 summarizes the discussion by highlighting
key conceptual differences between psychometrics and
metrology.
Towards informative nulls
Informative nulls arise not simply from nonsignificant
results, but from a structured inferential process that makes
uncertainty explicit, constrains it, and evaluates it against
standards of practical relevance. A nonsignificant effect
is not informative merely because its uncertainty interval
includes zero; it becomes informative only when uncertainty
has been sufficiently reduced to exclude effects that would
matter theoretically or managerially. In this sense, infor -
mativeness depends on exclusion rather than inclusion, a
logic formalized by equivalence testing and minimal-effect
frameworks (Anvari and Lakens 2021). Together, these
considerations motivate a three-step procedure: recognize
uncertainty, minimize it, and establish practical equivalence
thresholds.
Fig. 1 ROPE and intervals

M. Sarstedt
regarding the individual contributors to measurement uncer-
tainty—often based on individual experience or scientific
judgment (Tal 2011). After assigning values to these com -
ponents, the aggregate uncertainty is derived using the
conventional approach for combining standard deviations
(i.e., compute the square root of the sum of squared stan -
dard deviations, accounting for potential covariances). The
resulting composite uncertainty is subsequently scaled by a
coverage factor—selected to correspond to a specified con-
fidence level—to produce the uncertainty interval (V osk and
Emery 2015; Chap. 7).
Recognizing uncertainty may initially appear to make
findings weaker—it enlarges confidence intervals and ren -
ders effects “less significant”—as Rigdon et al. (2020) show
in an illustrative example of a between-group attitude mea -
surement. Yet this act of intellectual honesty is foundational
to credible inference. By showing the true range of plausible
outcomes, researchers make room for nulls that are not fail-
ures but well-calibrated reflections of limited information.
Widening the bounds directly counteracts the file-drawer
problem. Nulls that are properly contextualized within
quantified uncertainty become more interpretable, reducing
the temptation to suppress them. Recognized uncertainty
turns ambiguity into evidence.
Step two: minimize uncertainty
Once uncertainty is recognized, the next step is to minimize
it through methodological refinement. Minimization does
not mean artificially reducing variance through data clean -
ing or post-hoc adjustment that would turn the statistical
analysis into a fishing expedition (Stefan and Schönbrodt
2023). Instead, this step involves systematically improving
measurement quality. Researchers can achieve this through
calibration of measurement instruments (e.g., Bach 2024;
Bach et al. 2020, 2025), consistent operationalization of
constructs (Gilliam and V oss 2013), replication across con-
texts (e.g., Ebersole et al. 2016; Klein et al. 2014, 2018,
2022), and integration of multiple analytical approaches
that cross-validate one another (Sarstedt et al. 2024). These
steps narrow the bounds around estimates, transforming
previously ambiguous nulls into confident statements about
the absence (or presence) of effects (Sarstedt and Moisescu
2024).
Recognition without minimization leaves us aware of
uncertainty but powerless to improve it, while minimiza -
tion without recognition risks false precision. The two steps
must proceed in sequence and in dialogue. When both are
achieved, results reflect metrological transparency that sup-
ports cumulative knowledge.
Step one: recognize uncertainty
The first and most neglected step in improving inference is
to recognize uncertainty explicitly. Recognition does not
mean resignation; it means widening our statistical bounds
to match the true precision of our data, measurement, and
theory. This involves identifying all material sources of
uncertainty and incorporating them into statistical models
so that confidence intervals reflect both error and measure -
ment uncertainty.
In metrological terms, these sources of uncertainty can be
classified as Type A and Type B (Bell 2001). Type A uncer-
tainties arise from statistical variation such as sampling
error, response variability, or repeated measures in experi -
ments, quantified through empirical data analysis. Type B
uncertainties, by contrast, stem from nonstatistical sources,
including instrument calibration drift, respondent bias, or
imperfect construct validity, and are often estimated from
expert judgment (Rigdon et al. 2020). In marketing research,
acknowledging both types ensures that reported findings
reflect not only the randomness of data collection but also
the systematic limitations of the tools and constructs used
to measure consumer perceptions, attitudes, and intentions.
Recognizing uncertainty also requires quantifying it.
To do so, researchers establish an uncertainty budget,
which systematically consolidates all pertinent information
Table 1 Conceptual differences between psychometrics and metrology
Dimension Psychometrics Metrology
Primary goal Model observed scores
and their reliability across
measurements
Characterize measure-
ment results and their
limits of inference
Meaning of
“true value”
Expected value of scores
over repeated, equivalent
measurements
Fixed but unknow-
able property of the
measurand
Ontological
stance
Operational: “true” is
model-dependent and
expectation-based
Realist: target
quantity is assumed
to exist
Treatment of
error
Deviation from expected
score, often decomposed
into random and systematic
components
Integrated into
uncertainty as
multiple sources of
imprecision
Core quantity
reported
Observed score with reli-
ability and error variance
Measurement with
associated uncertainty
Expression of
imprecision
Error variance or standard
error around the expected
value
Uncertainty interval
reflecting plausible
values
Scope of
uncertainty
Primarily random and sys-
tematic measurement error
Sampling variability,
measurement error,
model uncertainty,
contextual effects
Implica-
tion for null
results and
replicability
Null or divergent find-
ings are often interpreted
as failures of detection or
replication
Null or divergent
findings may be
compatible outcomes
within a shared uncer-
tainty range

Metrological uncertainty and the value of informative nulls in marketing research
Informative inference requires a three-step process that
builds on metrological principles: Recognizing uncertainty,
minimizing it, and establishing benchmarks of practical
equivalence. Recognition ensures that uncertainty reflects
all material sources of imprecision, not merely sampling
variability. Minimization improves the precision of esti -
mates through better measurement and design. Crucially,
establishing practical relevance—operationalized through
regions of practical equivalence—provides the criterion for
determining whether remaining uncertainty is substantively
meaningful.
This perspective clarifies the role of null results. A non -
significant finding becomes informative only when uncer -
tainty has been sufficiently constrained to rule out effects
that would matter theoretically or managerially. In this sense,
informativeness is an interval-level property grounded in
exclusion rather than inclusion. The importance of explic -
itly defining smallest effect sizes of interest, as emphasized
in anchor-based and equivalence-testing frameworks, is
therefore not ancillary but central to valid inference (Anvari
and Lakens 2021).
More broadly, this framework reframes debates about
replicability and null results. Apparent inconsistencies
across studies may reflect shared uncertainty rather than
conflicting evidence, particularly when confidence inter -
vals are narrow, but uncertainty intervals remain wide. By
shifting attention from binary significance decisions toward
uncertainty-aware and relevance-driven inference, the
approach outlined here offers a path toward more cumula -
tive, transparent, and decision-relevant research.
Funding Open Access funding enabled and organized by Projekt
DEAL.
Declarations
Conflict of interest The author declares no conflict of interest.
Open Access   This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format,
as long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate
if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless
indicated otherwise in a credit line to the material. If material is not
included in the article’s Creative Commons licence and your intended
use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright
holder. To view a copy of this licence, visit  h t t p  : / /  c r e a  t i  v e c  o m m o  n s .  o
r g  / l i c e n s e s / b y / 4 . 0 /.
Step three: establish practical equivalence
benchmarks
Recognizing and minimizing uncertainty improves the
fidelity of measurement, but they do not, on their own,
determine what conclusions are substantively meaning -
ful. In a final step, researchers need to establish the ROPE
against which an effect can be interpreted. This step is not
a statistical exercise but a substantive one (Riesthuis et
al. 2018). It requires researchers to articulate, in advance,
what magnitude of effect would warrant attention, invest -
ment, or theoretical revision. In marketing research, such
benchmarks may be grounded in economic considerations
(e.g., minimum changes in revenue, conversion rates, or
customer lifetime value), theoretical relevance (e.g., effect
sizes large enough to distinguish competing explanations),
or institutional constraints (e.g., costs of implementation
or intervention). Importantly, the ROPE should be justi -
fied independently of the observed data to avoid post hoc
rationalization.
This step makes explicit what is often left implicit in
empirical research. Without a ROPE, uncertainty can be
reduced indefinitely without yielding decision-relevant
conclusions, and null results remain ambiguous regardless
of precision. By contrast, specifying a ROPE establishes a
stopping rule for inference: it clarifies how much uncertainty
reduction is sufficient and what kinds of effects the study is
designed to rule out. In doing so, it transforms uncertainty
from a descriptive feature of the data into a criterion for
substantive judgment.
Establishing the ROPE completes the recognition–
minimization sequence. Recognition identifies the sources
and magnitude of uncertainty, minimization reduces their
impact, and practical equivalence benchmarks define the
standards against which remaining uncertainty is evaluated.
Together, these steps anchor marketing inference in trans -
parent measurement practices and explicitly connect statis -
tical evidence to the consequences that matter.
Conclusion
A persistent problem in empirical research is that null
results are often treated as uninformative, while statistically
significant findings are interpreted as inherently meaningful
(Gelman and Stern 2006). This paper argues that this asym-
metry is misplaced. The central issue is not the presence
or absence of statistical significance, but whether empirical
results are interpreted against a realistic representation of
uncertainty and clear standards of practical relevance. With-
out these elements, both significant and null findings risk
being misclassified as informative.

M. Sarstedt
JCGM/WG1. 2008. Joint Committee for Guides in Metrology/Work -
ing Group on the Expression of Uncertainty in Measurement
(JCGM/WG1): Evaluation of measurement data—Guide to the
expression of uncertainty in measurement. Retrieved from  h t t p
s : /  / w w w  . b  i p m  . o r g  / u t  i l s  / c o  m m o  n / d o  c u  m e n  t s / j  c g m  / J C  G M _ 1 0 0 _ 2
0 0 8 _ E . p d f
Klein, R. A., K. A. Ratliff, M. Vianello, R. B. Adams, Š. Bahník, M. J.
Bernstein, K. Bocian, M. J. Brandt, B. Brooks, C. C. Brumbaugh,
Z. Cemalcilar, J. Chandler, W. Cheong, W. E. Davis, T. Devos, M.
Eisner, N. Frankowska, D. Furrow, and E. M. Galliani. 2014. and
B.A. Nosek. Investigating variation in replicability. Social Psy-
chology, 45(3), 142–152.
Klein, R. A., M. Vianello, F. Hasselman, B. G. Adams, R. B. Adams, S.
Alper, M. Aveyard, J. R. Axt, M. T. Babalola, Š. Bahník, R. Batra,
M. Berkics, M. J. Bernstein, D. R. Berry, O. Bialobrzeska, E. D.
Binan, K. Bocian, M. J. Brandt, R. Busching, and B. A. Nosek.
2018. Many Labs 2: Investigating variation in replicability across
samples and settings. Advances in Methods and Practices in Psy-
chological Science, 1(4), 443–490.
Klein, R. A., C. L. Cook, C. R. Ebersole, C. Vitiello, B. A. Nosek,
J. Hilgard, P. H. Ahn, A. J. Brady, C. R. Chartier, C. D. Chris -
topherson, S. Clay, B. Collisson, J. T. Crawford, R. Cromar, G.
Gardiner, C. L. Gosnell, J. Grahe, C. Hall, I. Howard, and K. A.
Ratliff. 2022. Many labs 4: Failure to replicate mortality salience
effect with and without original author involvement. Collabra:
Psychology 8(1):35271.
Knight, J. 2003. Null and void. Nature 422:554–555.
Kübler, R., J. S. Adler, L. Welke, M. Sarstedt, and R. Pauwels. 2025.
Mining consumer mindset metrics with user generated content.
Schmalenbach Business Review 77(3):497–525.
Lakens, D., A. M. Scheel, and P. M. Isager. 2018. Equivalence testing
for psychological research. Advances in Methods and Practices in
Psychological Science 1(2):259–269.
Milinković, N., and S. Jovičić. 2023. Measurement uncertainty. In
Advances in clinical chemistry , ed. G. S. Makowski. vol. 116
277–317. Cambridge, MA: Academic.
Nunnally, J. C., and I. H. Bernstein. 1994. Psychometric theory .
Columbus, OH: McGraw-Hill.
Qian, Y ., and H. Xie. 2022. Simplifying bias correction for selective
sampling: A unified distribution-free approach to handling endog-
enously selected samples. Marketing Science 41(2):211–432.
Riesthuis, P. 2024. Simulation-based power analyses for the smallest
effect size of interest: A confidence-interval approach for mini -
mum-effect and equivalence testing. Advances in Methods and
Practices in Psychological Science 7(2):1–14.
Riesthuis, P., I. Mangiulli, N. Broers, and H. Otgaar. 2018. Expert
opinions on the smallest effect size of interest in false memory
research. Applied Cognitive Psychology 36(1):203–215.
Rigdon, E. E. 2023. How improper dichotomization and the misrepre-
sentation of uncertainty undermine social science research. Jour-
nal of Business Research 165:114086.
Rigdon, E. E., and M. Sarstedt. 2022. Accounting for uncertainty in the
measurement of unobservable marketing phenomena. In Review
of marketing research, ed. H. Baumgartner, and B. Weijters. vol.
19 53–73. Bingley: Emerald.
Rigdon, E. E., M. Sarstedt, and J.-M. Becker. 2020. Quantify
uncertainty in behavioral research. Nature Human Behaviour
4(4):329–331.
Rosenthal, R. 1979. The file drawer problem and tolerance for null
results. Psychological Bulletin 86(3):638–641.
Rossiter, J. R. 2002. The C-OAR-SE procedure for scale development
in marketing. International Journal of Research in Marketing
19(4):305–335.
Sarstedt, M., and O.-I. Moisescu. 2024. Quantifying uncertainty in
PLS-SEM-based mediation analyses. Journal of Marketing Ana-
lytics 12(1):87–96.
References
Anvari, F., and D. Lakens. 2021. Using anchor-based methods to deter-
mine the smallest effect size of interest. Journal of Experimental
Social Psychology 96:104159.
Bach, D. R. 2024. Psychometrics in experimental psychology: A case
for calibration. Psychonomic Bulletin & Review 31(4):1461–1470.
Bach, D. R., F. Melinscak, S. M. Fleming, and M. C. V oelkle. 2020.
Calibrating the experimental measurement of psychological attri-
butes. Nature Human Behaviour 4:1229–1235.
Bach, D. R., E. E. Rigdon, and M. Sarstedt. 2025. Calibration experi -
ments: An alternative to multi-method approaches for mea -
surement validation in consumer research. Journal of Business
Research 193(April):115352.
Bell, S. 2001. Measurement good practice guide no. 11 (issue 2): A
beginner’ s guide to uncertainty of measurement . Teddington:
National Physical Laboratory.
Bergkvist, L., and M. Eisend. 2023. Changes in definitions and opera-
tionalizations in advertising research – justified or not? Journal of
Advertising 52(3):468–476.
Brodeur, A., N. Cook, and A. Heyes. 2022. We need to talk about
Mechanical Turk: What 22,989 hypothesis tests tell us about pub-
lication bias and p-hacking in online experiments. IZA Discussion
Paper No. 15478. Available online:  h t t p  s : /  / p a p  e r  s . s  s r n .  c o m  / s o  l 3 /
p a p  e r s .  c f  m ? a  b s t r  a c t  _ i d  = 4 1 8 8 2 8 9
Cohen, J. 1994. The Earth is round (p<.05). American Psychologist
49(12):997–1003.
Crowder, S., C. Delker, E. Forrest, and N. Martin. 2020. Introduction
to statistics in metrology. Cham: Springer.
Deer, L., S. J. Adler, H. Datta, N. Mizik, and M. Sarstedt. 2025.
Toward open science in marketing research. International Jour-
nal of Research in Marketing 42(1):212–233.
Dwan, K., C. Gamble, P. R. Williamson, J. J. Kirkham, and the Report-
ing Bias Group. 2013. Systematic review of the empirical evi -
dence of study publication bias and outcome reporting bias — An
updated review. Plos One, 8(7), e66844.
Ebersole, C. R., O. E. Atherton, A. L. Belanger, H. M. Skulborstad, J.
M. Allen, J. B. Banks, E. Baranski, M. J. Bernstein, D. B. Bon -
figlio, L. Boucher, E. R. Brown, N. I. Budiman, A. H. Cairo, C.
A. Capaldi, C. R. Chartier, J. M. Chung, D. C. Cicero, J. A. Cole-
man, and J. G. Conway. 2016. and B.A… Nosek. Many Labs 3:
evaluating participant pool quality across the academic semester
via replication. Journal of Experimental Social Psychology , 67,
68–82.
Fanelli, D. 2012. Negative results are disappearing from most disci -
plines and countries. Scientometrics 90:891–904.
Fisher, W. P., and A. J. Stenner. 2023. Towards an alignment of engi-
neering and psychometric approaches to uncertainty in measure -
ment: Consequences for the future. In Explanatory models, unit
standards, and personalized learning in educational measure -
ment, ed. W. P. Fisher, and P. J. Massengill. 295–306. Singapore:
Springer.
Gelman, A., and H. Stern. 2006. The difference between significant
and not significant is not itself statistically significant. The Ameri-
can Statistician 60(4):328–331.
Gilliam, D. A., and K. V oss. 2013. A proposed procedure for con -
struct definition in marketing. European Journal of Marketing
47(1/2):5–26.
Hanel, P. H. P., and D. M. A. Mehler. 2019. Beyond reporting statisti-
cal significance: Identifying informative effect sizes to improve
scientific communication. Public Understanding of Science
28(4):468–485.
Hubbard, R., and S. Armstrong. 1992. Are null results becoming an
endangered species in marketing? Marketing Letters 3:127–136.

Metrological uncertainty and the value of informative nulls in marketing research
Wasserstein, R. L., A. L. Schirm, and N. A. Lazar. 2019. Moving to a
world beyond p < 0.05. The American Statistician 73(sup1):1–19.
Publisher’s note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional affiliations.
Marko Sarstedt  Marko Sarstedt is a Chaired Professor of Market -
ing at the Ludwig-Maximilians-University Munich (Germany) and an
adjunct research professor at Babeș-Bolyai-University Cluj-Napoca
(Romania). His main research interest is the advancement of research
methods to further the understanding of consumer behavior. His
research has been published in Nature Human Behaviour, Journal of
Marketing Research, Journal of the Academy of Marketing Science,
Multivariate Behavioral Research, Organizational Research Meth -
ods, MIS Quarterly, and Psychometrika, among others. Since 2018,
Marko has been named member of Clarivate Analytics’ Highly Cited
Researchers List, which includes the “world’s most impactful scien -
tific researchers.” More information about Dr. Sarstedt:  h t t p s :   /  / l i n k t   r
. e   e / m  a r k  o s a  r s t e d t.
Sarstedt, M., S. J. Adler, C. M. Ringle, G. Cho, A. Diamantopoulos,
H. Hwang, and B. D. Liengaard. 2024. Same model, same data,
but different outcomes: Evaluating the impact of method choice
in structural equation modeling. Journal of Product Innovation
Management 41(6):1100–1117.
Soliman, M., M. Sarstedt, S. J. Adler, D. Siegfried, O. Genschow,
and M. Imschloss. 2025. A tale of open science: Emergence
of a new normal. Schmalenbach Journal of Business Research
77(4):763–792.
Stefan, A., and F. D. Schönbrodt. 2023. Big little les: A compendium
and simulation of p-hacking strategies. Royal Society Open Sci -
ence 10:220346.
Tal, E. 2011. How accurate is the standard second? Philosophy of Sci-
ence 78(5):1082–1096.
V osk, T., and A. F. Emery. 2015. Forensic metrology: Scientific mea-
surement and inference for lawyers, judges and criminalists .
Boca Raton, FL: CRC.
V oss, K. E., A. R. Zablah, Y .-S- Huang, and G. Chakraborty. 2020.
Conjunctionits: A call for clarity in construct definitions. Euro-
pean Journal of Marketing 54(4):1147–1159.
