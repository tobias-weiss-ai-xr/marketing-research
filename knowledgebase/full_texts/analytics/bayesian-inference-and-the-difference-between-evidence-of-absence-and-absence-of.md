---
title: Bayesian inference and the difference between evidence of absence and absence of evidence
url: https://doi.org/10.1057/s41270-026-00514-x
category: analytics
subcategory: theory
date: 2026-08
venue: Journal of Marketing Analytics
authors:
- Matteo Fina
- Charles F. Hofacker
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1057/s41270-026-00514-x.pdf
pages: 17
chars: 59974
fetched_at: '2026-11-08T17:51:23+00:00'
kb_version: 1
---

# Bayesian inference and the difference between evidence of absence and absence of evidence

ORIGINAL ARTICLE
Journal of Marketing Analytics
https://doi.org/10.1057/s41270-026-00514-x
 Charles Hofacker
chofack@wertheim.fsu.edu
Matteo Fina
matteo.fina@its.uni-frankfurt.de
1 Goethe University, Frankfurt, Frankfurt Am Main, Germany
2 Florida State University, Tallahassee, USA
Abstract
Null results are central to accumulating knowledge in marketing, yet conventional null hypothesis significance testing
(NHST) renders such results ambiguous. A nonsignificant p-value does not distinguish between data insufficiency and
data that meaningfully support the absence of an effect. In this brief note we argue that Bayesian inference provides a
useful framework for interpreting null findings in marketing analytics. By allowing probability distributions on unknown
parameters and then comparing the predictive adequacy of null and alternative models, Bayesian methods allow research -
ers to distinguish between the evidence of absence and the absence of evidence. This note outlines how Bayes factors,
posterior intervals, and interval null hypotheses can make null findings more informative whether those findings derive
from laboratory experiments, field experiments or secondary data studies. We note that publication bias in favor of sig -
nificant results is not just an issue for editors but is rather a problem across the full field of marketing since it impedes
accumulation of knowledge. In fact, when null results are analyzed and reported in ways that quantify evidential strength,
they become easier to interpret, easier to compare across studies, and more useful to both academic theory and manage -
rial decision-making.
Keywords Bayesian inference · Null hypothesis significance testing · Bayes factor · Null results
Received: 2 May 2026 / Accepted: 6 July 2026
© The Author(s) 2026
Bayesian inference and the difference between evidence of absence
and absence of evidence
Matteo Fina1 · Charles Hofacker2
Like almost all social science fields the traditional mar -
keting review process rewards statistically significant
findings more than it rewards carefully estimated null or
near-null results (McShane et al. 2024; Bultez and Her -
rmann 2025). A history of how this incentive structure came
to be is delightfully presented by Rigdon (in press) 2026,
but for now we simply point out that it is less than helpful
because many questions in marketing are not about whether
an effect differs from zero in a purely mathematical sense,
but whether the effect is large enough to matter for theory,
prediction, or managerial decision-making. When field data
show that personalization moves click-through rates by a
trivial amount, or an experiment shows that a popular new
framing of the offering changes consumer self-report by less
than a 10th of a Likert scale point, in such circumstances, a
conclusion that an effect is negligible can be just as useful
as evidence that it is not.
A central difficulty is that the dominant language of
empirical analysis remains frequentist NHST (Bialek,
Misiak and Dziekan 2023). By “frequentist” we mean the
commonly taught definition that asserts that probability is
an objective fact about the world, rather than a mathematical
Introduction
Recently, Petrescu and Krishen (2025) have argued that null
results have been marginalized for too long in marketing
analytics. They pointed out the negative consequences to
academic progress, and to practitioners and most tellingly
they noted that null results are not synonymous with “no
effect”. In this work, we have two goals. First, we wish to
express our agreement with Petrescu and Krishen ( 2025)
and to reinforce and embellish the points made by those
authors. Second, we wish to advocate for a simple, pre-
existing approach that allows the researcher to distinguish
between “null results” and “no effect”. That approach is
called Bayesian inference.

M. Fina, C. Hofacker
convenience useful for making beneficial decisions over the
long run. In routine practice, researchers often move from a
frequentist p-value greater than 0.05 to the conclusion that
there is no effect, even though this is not what the test estab-
lishes. Nevertheless the study ends up in the file drawer. In
fact the result is ambiguous: is the study telling us that the
effect is absent, or only that the sampled data points were
too noisy or too few in number to discriminate between
competing explanations?
This brief note suggests that part of the problem with
respect to null results in marketing is based on the infer -
ential techniques traditionally employed by researchers.
We propose Bayesian analysis as an alternative. Of course
Bayesian methods cannot by themselves eliminate publica -
tion bias, but such methods can make null findings more
interpretable by allowing researchers to quantify support
for negligible effects, for any alternatives, or for data insuf-
ficiency. Having said all this, our main claim is modest:
frequentist methods will remain a helpful tool for many
researchers but when the research question is whether the
evidence favors the notion that an effect is practically unim-
portant, Bayesian inference can offer a more natural and
informative answer.
What counts as a null result?
It is useful to separate three claims that are often conflated,
by necessity under frequentist NHST, in marketing and con-
sumer research articles. First, a study may report statistical
nonsignificance meaning that the p-value exceeds a chosen
threshold, generally 0.05. Second, the study may claim prac-
tical equivalence meaning that plausible effect is too small
to matter. Third, the study may claim support for a null or
interval-null hypothesis relative to an alternative motivated
by theory. These are not the same conclusions.
Under NHST, a large p-value generally means that the
observed data are not especially incompatible with the null
hypothesis being tested. The large p-value does not, by
itself, indicate that the null hypothesis is probably true, nor
does it distinguish weak evidence from evidence favoring no
meaningful effect. This distinction is especially important in
marketing because sample sizes are becoming increasingly
large, experiments are often inexpensive to run, and mana -
gerial application will rarely be driven by whether an effect
is exactly zero.
For those reasons the most useful null result in many
marketing applications is not the claim that the population
effect is exactly zero. Rather, it is the claim that the effect
lies within a range of practical irrelevance. An ad cam -
paign lift below a certain return-on-investment threshold, a
treatment effect too small to alter current positioning, or a
measurement difference too trivial to threaten comparability
may all count as “effectively null” even when they are not
mathematically zero.
Why frequentist NHST leaves nulls
ambiguous
The attraction of NHST is easy to describe: it provides a
comfortable operational procedure passed down from advi-
sor to student (Bialek, Misiak and Dziekan 2023); it has
been implemented on thousands of software platforms;
and it can be summarized, ready for an all-or-nothing deci -
sion by the researcher, by a single quantity, the ever present
p-value (Perezgonzalez 2015). Unfortunately, its interpreta-
tion is not well aligned with the questions researchers want
to answer (Feinberg 2024). The p-value is a statement about
the extremity or “weirdness” of the observed data under the
assumption of the null hypothesis. As such it is not a direct
statement about the plausibility of any hypothesis. This has
the implication that a nonsignificant finding leaves inves -
tigators with the weak conclusion that they have failed to
reject the null.
This creates two related problems. The first is asymme -
try. NHST can provide a basis for rejecting a null, but it does
not provide a comparable basis for concluding that a null or
negligible-effect hypothesis is supported. The second is that
studies with low precision and studies with strong evidence
for a near-zero effect both end up “nonsignificant”.
The problem manifests one way or the other whether sam-
ple sizes are small or large. With small samples, researchers
may report null findings that are simply uninformative. With
very large samples, trivially small departures from zero can
become statistically significant and then get framed as theo-
retically meaningful. In both cases, the significance thresh -
old obscures the inferential question that matters most: what
do the data say about the sign, the size and the practical
importance of the effect?
What Bayesian inference adds
Bayesian inference changes the status of null results because
it allows researchers to make probability statements about
unknown quantities (Wedel et al. 2024) and therefore com-
pare competing hypotheses directly. In Bayesian inference
the uncertainty surrounding unknown parameters—such as
a beta coefficient that captures the linear impact of an inde -
pendent variable on the dependent variable—is represented
as a probability distribution. This is not possible under a
“frequency” interpretation of probability since, after all,
the frequency with which, out in the world, the unknown

Bayesian inference and the difference between evidence of absence and absence of evidence
is equal to what it is equal to is 1, and the frequency with
which the unknown is equal to all of the values it is not
equal to is 0 (Hofacker et al. 2024). Rather than asking only
whether the observed data would be unusual under the null
hypothesis, Bayesian analysis asks how the data update
rational belief (probability) about the value of unknown
parameters and models (Blozis 2022). The core updating
rule is Bayes’ theorem:
p (θ|y)= p (y|θ) p (θ) p (y)
where y denotes the observed data, θ the unknown param -
eter or vector of parameters, p (θ) the prior distribution
for the parameter(s), p(y|θ) the likelihood of the data, and
p(θ|y) the posterior distribution for the parameters. The
denominator,
p (y)=
ˆ
θ
p (y|θ) p (θ) dθ
is the marginal likelihood, which serves to ensure that the
posterior distribution sums (more technically integrates) to
1 and is therefore proper and provides a prediction for the
observed data y as we will see later when we discuss the
Bayes factor. In the equation immediately above we wish
to understand the distribution of the data despite our lack of
certainty about the value of the unknown parameter(s) θ. In
that case we average out (integrate over) θ.
Ignoring p (y) for now, Bayes theorem expresses our
beliefs about the model unknowns θ given the observed
data (the posterior) and states that these updated, poste -
rior beliefs should be proportional to our beliefs about the
unknowns excluding the data (the prior), multiplied by the
likelihood of the data:
p (θ|y) ∝ p (y|θ) p (θ) .
Note that the posterior distribution, sitting there on the
left-hand side, is a function of θ. We are thus treating the
uncertainty about unknown parameters as a legitimate
application of probability, which allows us to divide, multi-
ply and integrate over our uncertain beliefs, as we did when
we wanted to predict p (y) above, or to conclude when two
sets of beliefs have equal or proportional strength. In the
frequentist paradigm, probability calculations are strictly
reserved for physical and objective randomness such as
occurs during sampling. Bayesians, on the other hand, grant
themselves the mathematical right to describe the uncer -
tainty surrounding a fixed but unknown quantity, like the
value of a causal effect as captured by a regression slope, as
a probability distribution. One might think of this distribu -
tion as a cloud of possible values for the fixed quantity. This
makes it simple to ask direct questions about the probability
of any possible parameter value or set of values, null or oth-
erwise. One can calculate the probability that the treatment
effect is positive, the probability that said effect is negligible
as defined by a given range, or the probability that the data
are too weak or noisy to support either conclusion.
The posterior distribution then is the fundamental basis
used for distinguishing among these possibilities (Kruschke
2021). This distribution describes the uncertainty that
remains about some unknown effect after we have updated
prior information, if any, with observed data. For example,
if δ = θA − θB denotes the treatment effect in a two-group
comparison, Bayesian inference allows us (or our preferred
software) to calculate p(δ> 0|y) or p (|δ|⟨ ε| y) where ε is a
substantively chosen threshold for practical meaningfulness.
The first quantity captures the probability that the effect is
positive assuming we have observed the data that we have
observed. It is often referred to as a Bayesian p-value (by
Wedel and Dong 2020, among others). The second quan -
tity analogously captures the posterior probability that the
effect β lies inside a region of practical meaninglessness.
The region created by ε is known as the region of practi -
cal equivalence or ROPE (Kruschke 2010), and this will be
discussed further below. In our view these sorts of questions
are what marketing researchers and marketing managers
care about, as opposed to how unusual the data would be
if δ =0 .
In addition to the Bayesian p-value and the ROPE, we
can use the posterior distribution to create a credible inter-
val. A 100 (1 − α)%  credible intervals is an interval [a, b]
such that
p(a ≤ δ ≤ b|y)=1 − α.
Unlike the classical confidence interval, a credible interval
is directly interpretable as a probability statement about the
parameter (given the observed data). In the present con -
text, posterior intervals are especially useful because they
reveal whether the credible values of the effect are concen -
trated near zero, spread widely across positive and negative
values, or centered on a value that would be managerially
meaningful.
The Bayes factor  (Allenby 1990; Keysers et al. 2020)
represents a different approach that uses p (y) to calculate
the odds in favor of one hypothesis as compared to another.
This leads to a comparison of the two competing hypotheses
in predicting y. If H0 denotes a null or practically null model
(belief that the true parameter value is within the ROPE)
and H1 is any alternative model of interest, the Bayes factor
in favor of H0 over H1 is

M. Fina, C. Hofacker
BF01 = p(y|H0) p(y|H1) .
If the analyst wishes to calculate instead the Bayes factor in
favor of H1 over H0, he or she need only take the reciprocal
of BF01. Here p(y|Hj) is the marginal likelihood of the data
under model Hj, obtained by integrating over the parameter
values allowed by that model,
p (y|Hj)=
ˆ
θ∈Hj
p (y|θ, Hj) p (θ|Hj) dθ.
Here we average out (integrate over) all possible values for
θ that are allowed under model or hypothesis Hj. The aver-
aging is weighted by the joint distribution of y and θ under
Hj,
p (y, θ|Hj)= p (y|θ, Hj) p (θ|Hj) .
The Bayes factor updates prior model odds, converting
those into posterior model odds, according to
p(H0|y)
p(H1|y) = BF01 · p (H0) p (H1) .
Now we have arrived at one of the most important concep -
tual differences between Bayesian thinking and the tradi -
tional NHST. A large p-value does not provide evidence
for the null. It merely indicates that the data are not highly
inconsistent with it. Conversely, a small p-value suggests
that the data are inconsistent with H0. In contrast, a Bayes
factor provides evidence in favor of the null when it is large,
in favor of the alternative when it is small, and the odds
remain near a value of one when the data are insufficiently
informative (Rouder et al. 2009). This is exactly the distinc-
tion needed to separate evidence of absence from absence of
evidence (Gallistel 2009).
Returning to the notion of the ROPE, Bayesian analysis
enables researchers to define null results in substantively
meaningful terms. In many marketing applications, the rel -
evant benchmark is not whether an effect is exactly zero,
but whether it is too small to matter for theory or manage -
rial action. This naturally leads to the idea of an interval-
null formulation. Let δ again denote the treatment effect and
let ε> 0 denote the smallest effect size of interest. Then
one may define the ROPE as H0: |δ| <ε  and further set
up H1: |δ|≥ ε. This reframes the mathematical question
of whether the effect is precisely zero to the decision-rel -
evant question about whether any plausible effect is large
enough to matter. In a marketing context, ε might represent
the smallest main effect that would make changing a current
marketing practice worthwhile, or the smallest change in a
moderation effect that would make that moderator manage-
rially significant, or the smallest slope for the mediator-to-
outcome path that would justify management attention to the
mediator. Such practical considerations could be attached to
various aspects of marketing including matters of privacy
perception (Gorostiza-Esquerdeiro, Buján-Carballal and
Oyarbide-Zubillaga, 2026), issues surrounding sustainabil -
ity (Brüggemann et al. 2025) or topics pertaining to influ -
encers (Campbell et al. 2026). In summary, the technique
would be applicable to any managerially relevant combina-
tion of independent, moderating, mediating and dependent
variables.
In general, Bayesian methods connect seamlessly to
managerial or academic decision-making because Bayes -
ian methods rigorously separate uncertainty about the world
from the value (utility) of acting in the world (Hofacker
et al. 2024). Once the posterior distribution for an effect
is available, decision makers can combine it with a payoff
or loss function to evaluate the expected consequences of
alternative actions. In a marketing setting, for example, a
manager may compare the expected profit from rolling out
a new campaign, running another experiment, or maintain -
ing the status quo, where each option depends not only on
the most likely treatment effect but also on the uncertainty
surrounding it and the costs of implementation. Formally, if
a denotes an action and U (a, θ) the utility associated with
that action when the true state of the unknown parameter or
parameters is θ, Bayesian decision theory suggests choosing
the action that maximizes expected posterior utility,
ˆ
θ
U (a, θ) p (y|θ) p (θ) dθ.
This approach is especially useful when effects are small,
uncertain, or asymmetric in their consequences, because the
relevant managerial question is often not whether an effect
is “significant,” but whether acting on the current evidence
would pay off. We humbly suggest that authors in marketing
should carefully think through the potential gains or losses
that would correspond to implementing the recommenda -
tions made in the managerial implications section.
To wrap up this section we note that Bayesian inference
is an axiomatically grounded theory of learning from data
(Gilbride et al. 2008). Prior beliefs are updated via the like-
lihood, and then the posterior distribution becomes the basis
for estimation, interval statements, model comparison, prob-
abilities and prediction. The coherence of Bayesian infer -
ence matters especially for null results. The posterior grants
us a common probabilistic language for quantifying the
odds for three separate possibilities. With the Bayes factor

Bayesian inference and the difference between evidence of absence and absence of evidence
we can quantify evidence for a meaningful effect (how large
is the ratio), evidence for a practically negligible effect (how
small is the ratio), or for the insensitivity of the data with
respect to distinguishing between the two (how close to 1 is
the ratio). These three continuous possibilities end up fused
into a single ambiguous binary statement under NHST. That
Bayes can distinguish among these three possibilities makes
it highly useful, and usefulness is of course why scientists
choose to describe the world using math in the first place.
Bayesian methods connect naturally to decision-making
because they separate uncertainty about the world from the
consequences of acting in the world. Once a posterior dis -
tribution for an effect is available, managers can combine
it with a payoff or loss function to evaluate the expected
consequences of alternative actions. In a marketing setting,
for example, a decision maker may compare the expected
value of rolling out a campaign, collecting more data, or
keeping the status quo, where each option depends not only
on the most likely treatment effect but also on the uncer -
tainty surrounding it and the costs of implementation.
When a is a potential (researcher or managerial) action and
U (a, θ) is the utility associated with that action when the
true state is θ, Bayesian decision theory recommends choos-
ing the action that maximizes expected posterior utility,
∫
θ
U (a, θ) p (θ|y) dθ. This is useful in the null-results con -
text because the relevant question is often not whether an
effect is significant in the NHST sense, but whether acting
on the available evidence is worthwhile.
We now turn to some simple simulations so as to make
the discussion more concrete.
Simulation: a stylized main effect testing
exercise
To make the discussion less theoretical, we simulate a
stylized two group test with a binary outcome like repa -
tronage or picking the healthier food option. Each repli -
cation compares a control group and a treatment group,
and that which we care about is the treatment lift, defined
as the difference in the binary outcome between the
treatment and control groups. This setup is intentionally
simple. The goal is not to mimic every feature of mar -
keting research, but to study how competing inferential
frameworks behave in a familiar and practically relevant
setting.
Four data-generating processes are considered. The
first is a true-null case in which the treatment leaves the
conversion rate unchanged. The second is a small posi -
tive-effect case in which the treatment effect is positive
but close to the boundary of practical relevance. The third
is a positive-effect case in which the treatment produces
a clearly meaningful increase in conversion. The fourth
is a negative-effect case in which the treatment lowers
conversion. Together, these scenarios allow the analy -
sis to study not only evidence accumulation under null
and positive effects, but also the symmetric treatment of
potentially harmful interventions.
Design calibration and justification
The baseline control conversion rate is set to 10 percent.
This value is not intended as a universal benchmark, but
it places the exercise in a realistic order of magnitude for
many digital marketing outcomes such as click-through,
low-friction conversion, or campaign response. The sample-
size grid spans small pilot experiments, moderate field tests,
and large-scale digital experiments. This range is chosen to
show how evidence changes as information accumulates
rather than to calibrate the design to one narrow empirical
application.
The baseline Bayesian prior is weakly informative.
The simulation uses Beta priors for the treatment and
control conversion probabilities because these priors are
transparent, easy to interpret, and analytically convenient
in the binomial setting. This provides a neutral starting
point for a paper whose purpose is conceptual rather than
domain-specific forecasting. At the same time, the paper
does not treat the prior as fixed by nature. Because prior
assumptions are part of the inferential question, the simu -
lation also reports sensitivity analyses under alternative
prior specifications.
The same logic applies to the region of practical equiva -
lence. The ROPE is intended to capture effects that are too
small to matter for a managerial decision, not effects that are
mathematically equal to zero. In the baseline specification,
the ROPE is defined as a narrow interval around zero cor -
responding to effects that are substantively negligible in the
A/B-testing (two-group) context. Because that benchmark is
partly contextual, the analysis also considers narrower and
wider ROPE values. This makes explicit that practical-null
conclusions depend on the substantive standard of relevance
rather than on statistical convention alone.
Finally, the baseline evidence threshold for Bayes fac -
tors is set at a conventional moderate-evidence level,
and the paper also evaluates more permissive and more
demanding thresholds. This is important because evi -
dential cutoffs, like significance thresholds, are partly
conventional. The purpose of the sensitivity analysis is
therefore not to eliminate dependence on assumptions,
but to show whether the main qualitative conclusions
remain intact under plausible alternatives.

M. Fina, C. Hofacker
Analysis strategy and symmetric Bayesian
classification
Each simulated dataset is analyzed in two ways. The fre -
quentist analysis uses a difference-in-proportions test and
classifies the outcome as a positive effect, a negative effect,
or non-significant. The Bayesian analysis uses a Beta-Bino-
mial model for the treatment and control conversion prob -
abilities and then studies the posterior distribution of the
treatment effect, δ = θT − θC . Classification on the Bayes-
ian side is fully symmetric and distinguishes four outcomes:
evidence for a negative effect, evidence for a practical null,
evidence for a positive effect, and inconclusive data.
Formally, let ε> 0 denote the smallest effect size of
interest. The Bayesian classification partitions the posterior
distribution into three substantively meaningful regions:
δ ≤− ε, |δ| <ε , and δ ≥ ε. Posterior probabilities for these
three regions are then combined with the evidential thresh -
old to determine whether the data support a harmful effect,
a practically negligible effect, a beneficial effect, or whether
the remaining uncertainty is too large for any of these con -
clusions. This symmetry is important because many applied
marketing interventions can fail in either direction: a treat -
ment can help, do nothing, or make outcomes worse.
Evidence accumulation in single cumulative paths
The simulation first presents cumulative paths that show
how evidence evolves within a single experiment as more
observations are added. These figures are useful because
they reveal how the inferential language changes as infor -
mation accumulates. Under a true-null path, the p-value
may remain above the conventional significance threshold
for much of the sequence, but that fact alone does not distin-
guish between practical absence and weak information. The
Bayesian summaries add that distinction by tracking the pos-
terior probability of the practical-null region and the Bayes
factor comparing the practical null with its complement.
Under the positive-effect and negative-effect paths, the
cumulative figures illustrate directional learning. As the
sample grows, posterior mass should move toward the rel -
evant directional region if the effect is sufficiently large
relative to the ROPE. The small positive-effect path is par -
ticularly informative because it shows the setting in which
practical relevance and statistical detectability are most
likely to diverge. In that scenario, the Bayesian classification
may remain conservative at moderate sample sizes, which is
substantively meaningful rather than merely inconvenient:
it indicates that the evidence is not yet strong enough to
conclude that the effect exceeds the smallest threshold of
managerial relevance.
Figure 1 reports the cumulative evidence paths for the
four data-generating processes. The figure should be dis -
cussed as an illustration of how the frequentist p-value,
the Bayes factor, and the posterior probability of the
practical-null region evolve as n increases within a single
experiment.
Classification results across repeated samples
The main simulation results are based on repeated replica -
tions at each sample size. On the frequentist side, the clas -
sification plots summarize how often NHST detects positive
or negative effects and how often it remains in the non-
significant category. These figures provide a useful bench -
mark for rejection behavior and directional detection. In the
positive-effect and negative-effect scenarios, the probability
of directional detection should rise with sample size. In the
true-null case, most replications should remain non-signifi -
cant, with a small fraction of false directional findings.
The limitation of the frequentist framework remains
interpretive. The non-significant category combines sub -
stantively different situations: a genuine practical null, weak
evidence, and small effects that do not yet yield rejection.
By construction, it does not distinguish among these pos -
sibilities. The Bayesian classification plots add that dis -
tinction. Under a true null, the simulation can accumulate
explicit evidence for the practical-null region. Under clearly
positive or clearly negative effects, the simulation can move
toward the corresponding directional conclusion. Under
small effects, the classification may remain mixed, which
reveals that the answer depends on both the available infor-
mation and the substantive threshold of relevance.
Figure 2 reports the frequentist classification rates across
sample sizes and scenarios. Figure 3 reports the correspond-
ing Bayesian classification rates. These two figures should
be read together: the frequentist plots summarize rejection
behavior, whereas the Bayesian plots summarize evidential
allocation across harmful, negligible, beneficial, and incon-
clusive outcomes.
Detailed numerical summaries for the baseline specifica-
tion are reported in Appendix Table 2 through Table 5.
Sensitivity analysis
Because Bayesian classifications are expected to depend
on priors, practical thresholds, and evidential thresholds,
the paper reports one-factor-at-a-time sensitivity analyses

Bayesian inference and the difference between evidence of absence and absence of evidence
for each of these ingredients. The prior sensitivity analy -
sis compares the baseline weakly informative prior with
alternative specifications such as Jeffreys-type and mildly
informative priors. The ROPE sensitivity analysis evaluates
narrower and wider practical-null regions. The evidence-
threshold sensitivity analysis examines how classifications
change under more permissive and more demanding Bayes-
factor cutoffs.
(a) Negative effect (b) Positive effect
(c) Small positive effect (d) True null
Fig. 1 Cumulative evidence paths for the true-null, small positive-effect, positive-effect, and negative-effect scenarios

M. Fina, C. Hofacker
The purpose of these analyses is not to show invariance
under every conceivable assumption. Rather, the goal is
to determine whether the main qualitative conclusions are
stable across plausible alternatives. If the same broad pat -
tern holds across a reasonable range of priors and thresh -
olds, confidence in the substantive interpretation increases.
If conclusions shift materially, that is also informative,
because it indicates that the result is close to the boundary
of practical relevance or evidential sufficiency. In that sense,
sensitivity analysis is not an auxiliary robustness ritual but it
is part of the inferential content of the exercise itself.
Figures 4 through 6 summarize the sensitivity analy -
ses for the ROPE, the prior, and the Bayes-factor thresh -
old. These figures should be used to show both stability
and dependence. Under the true-null scenario, evidence
for practical absence should remain comparatively robust
across many specifications. Under the small positive-effect
scenario, however, classifications may shift across assump-
tions in predictable ways. That pattern is substantively
valuable because it shows how managerial notions of rel -
evance shape the interpretation of near-null findings (Figs.
5, 6).
Detailed numerical summaries for the sensitivity analy -
ses are reported in Appendix Table 6 through Table 8.
Interpretation
This simulation connects directly to the larger argument
of the paper. If the field continues to rely mainly on p-val -
ues and dichotomous significance thresholds, then many
null findings will continue to be rhetorically weak even
while they are empirically informative. A study with a
large p-value can always be dismissed as underpowered,
and a study with a tiny but statistically significant effect
can always be overstated as theoretically important. The
inferential vocabulary of NHST itself encourages these
distortions. The present simulation shows that once the
analysis is allowed to distinguish directional effects,
(a) Negative effect (b) Positive effect
(c) Small positive effect (d) True null
Fig. 2 Frequentist classification rates by sample size and data-generating process. The absence of lines for a given sample size indicates a flat,
zero proportion

Bayesian inference and the difference between evidence of absence and absence of evidence
practical nulls, and inconclusive evidence, many findings
that would otherwise be grouped together under non-sig -
nificance become more interpretable.
The simulation also shows how Bayesian analysis
changes that vocabulary. Once the researcher defines a
substantively meaningful null interval, the output can
distinguish practical absence from mere non-rejection,
and it can also distinguish genuinely promising effects
from experiments that are still too imprecise to be deci -
sive. This does not eliminate the editorial norms or career
incentives that contribute to publication bias, but it does
reduce one important source of the problem: the tendency
to treat all nonsignificant results as second-class evi -
dence. In particular, the symmetric classification adopted
here makes clear that the relevant alternatives are not
limited to a beneficial effect versus no effect: a negative
effect can also be identified explicitly rather than being
absorbed into a residual category.
Taken together, the simulation supports the paper’s cen -
tral claim in a more refined way. The frequentist proce -
dure remains useful for describing rejection behavior and
directional detection, and it performs well when the true
effect is sufficiently large and the sample is allowed to grow.
At the same time, under a true null it still mostly produces
only non-significance. The Bayesian procedure adds a sub -
stantively important category that NHST lacks: evidence for
the practical null. In that sense, the Bayesian analysis does
not merely replace one threshold with another. It changes
what the researcher is allowed to say. A null result can
become informative evidence that the treatment effect is too
small to matter, rather than a weak statement that the null
was not rejected.
At the same time, the simulation also shows something
more nuanced and important for the note’s credibility.
Bayesian evidence is not magically pro-null or always
more permissive. Under the chosen ROPE, prior, and
evidence threshold, the Bayesian classification is conser -
vative when the true effect is small, and the sensitivity
analyses show that this conservatism changes in pre -
dictable ways when those assumptions are varied. This
should be understood as a feature rather than a defect,
because near-null findings are meaningful only relative
(a) Negative effect (b) Positive effect
(c) Small positive effect (d) True null
Fig. 3 Bayesian classification rates by sample size and data-generating process. The absence of lines for a given sample size indicates a flat, zero
proportion

M. Fina, C. Hofacker
to a substantive standard of relevance. For that reason,
the simulation supports practical reporting recommenda -
tions as well as a conceptual claim: researchers should
justify their statistical workflow (Schad et al. 2023;
Gallistel 2009), including their ROPE, report prior and
threshold sensitivity checks, and distinguish carefully
among practical-null evidence, directional evidence, and
inconclusive evidence. The practical reporting checklist
appears as Table 1.
Implications for publication and reporting
If null findings are to contribute to cumulative marketing
knowledge, they must be reported in ways that preserve
their evidential content and reveal the assumptions under
which that content is assessed. A useful starting point is
to define the smallest effect size of interest before analy -
sis and to explain that benchmark in substantive terms.
In a marketing context, this benchmark might correspond
to the minimum conversion lift worth implementing, the
minimum revenue gain worth the cost of personalization,
or the smallest performance decline that would justify
abandoning a treatment.
A second implication is that Bayesian analyses should be
reported symmetrically whenever the substantive problem
is symmetric. If a treatment can help, do nothing, or harm
Table 1 Practical reporting checklist
Element What to specify Why it helps
Substantive null Define the smallest
effect size of interest or
interval null
Prevents no effect from
being confused with no
detectable effect
Prior
specification
State priors and give a
short rationale
Makes assumptions
visible and cumulative
Posterior
summary
Report posterior mean
or median and a credible
interval
Shows the range of
effect sizes still sup-
ported by the data
Model
comparison
Report a Bayes factor
when comparing null
and alternative accounts
Distinguishes evidence
for absence from data
insensitivity
Sensitivity
check
Show whether conclu-
sions change under plau-
sible alternative priors
Improves robust-
ness and reviewer
confidence
Fig.  4 Sensitivity of Bayesian classifications to alternative ROPE values. The absence of lines for a given sample size indicates a flat, zero
proportion

Bayesian inference and the difference between evidence of absence and absence of evidence
performance, the inferential framework should preserve
that structure. Reporting only beneficial and null outcomes
while absorbing harmful effects into a residual category
obscures information that matters for theory and decision-
making. In near-null settings, especially, symmetric report-
ing clarifies whether the data support a beneficial effect, a
harmful effect, a practically negligible effect, or whether
the evidence remains too weak to discriminate among these
possibilities.
A third implication is that sensitivity analysis should
be routine rather than exceptional. Because Bayesian
classifications may depend materially on the prior, the
ROPE, or the evidential threshold, those inputs should be
justified and varied transparently. This does not weaken
the method. On the contrary, it makes explicit what is
often left implicit in applied research: many evidential
judgments depend on assumptions about relevance and
acceptable uncertainty.
Taken together, these points suggest a stronger report -
ing standard for null and near-null findings in marketing.
Researchers should distinguish clearly among four out -
comes whenever the design permits: evidence for a positive
effect, evidence for a negative effect, evidence for a practi -
cal null, and inconclusive evidence. They should report the
assumptions under which these classifications are obtained
and show whether those classifications remain stable under
plausible alternatives. In this way, null findings become
cumulative contributions rather than discarded residuals of
non-significant testing 7.
Fig. 5 Sensitivity of Bayesian classifications to alternative prior specifications. The absence of lines for a given sample size indicates a flat, zero
proportion

M. Fina, C. Hofacker
Conclusion
Bayesian methods do not make difficult decisions disappear,
they rather force those decisions into the open. Priors, ROPE
values, and evidential thresholds all require judgment, but
that judgment is closely aligned with the actual questions that
researchers and managers face when interpreting null and near-
null findings. In that sense, the main contribution of the Bayes-
ian perspective is not only technical. It is also conceptual: it
provides a language in which the absence of a meaningful effect
can become evidence rather than merely a failure to reject.
Null results should not be treated as failed outcomes in
marketing research. Many of the most important scientific and
managerial conclusions concern stability, invariance, boundary
conditions, and effects too small to justify attention (Rouder et
al. 2009; Gallistel 2009). The difficulty is that application of
NHST leaves such findings rhetorically and inferentially under-
specified. A nonsignificant result is too often reported as either
failure or absence, even though it may be neither.
A Bayesian perspective offers a useful complement here. By
expressing uncertainty directly over unknown quantities and
by comparing the predictive performance of null and alterna-
tive accounts, Bayesian methods can distinguish evidence for
negligible effects from simple lack of information. Used in that
way, Bayesian inference does not end debates over publication
bias, but it can reduce one important source of the problem:
the tendency to treat all nonsignificant findings as interpretively
thin. For a field that increasingly values cumulative evidence
and managerial relevance, that is not a small contribution.
Appendix
See Tables 2, 3, 4, 5, 6, 7 and 8.
Table 2 Baseline simulation design choices
Component Baseline specification
Outcome Binary conversion in a two-arm A/B test
Baseline control rate 10%
True-effect scenarios True null: 0 pp; Small positive: + 1 pp; Posi-
tive: + 2 pp; Negative: -2 pp
Sample sizes per arm 250, 500, 1000, 2500, 5000, 10,000
Baseline prior Uniform Beta(1,1) for treatment and control
conversion rates
ROPE  ± 0.50 percentage points
Bayes-factor threshold 3
Replications 1,000 experiments per scenario and sample size
Bayesian regions Negative: Δ ≤ − ε; Practical null: |Δ|< ε; Posi-
tive: Δ ≥ ε; otherwise inconclusive
Fig. 6 Sensitivity of Bayesian classifications to alternative Bayes-factor thresholds. The absence of lines for a given sample size indicates a flat,
zero proportion

Bayesian inference and the difference between evidence of absence and absence of evidence
Table 3 Baseline specification: summary classification rates across scenarios and sample sizes
Scenario n per arm Freq: Negative Freq: Non-significant Freq: Positive Bayes:
Negative
Bayes: Positive Bayes:
Practi-
cal null
Negative effect 250 0.133 0.864 0.003 0.308 0.015 0.677
Negative effect 500 0.206 0.793 0.001 0.353 0.003 0.644
Negative effect 1000 0.333 0.666 0.001 0.460 0.001 0.539
Negative effect 2500 0.701 0.299 0.000 0.709 0.000 0.291
Negative effect 5000 0.922 0.078 0.000 0.880 0.000 0.120
Negative effect 10,000 0.999 0.001 0.000 0.998 0.000 0.002
Positive effect 250 0.002 0.893 0.105 0.023 0.277 0.700
Positive effect 500 0.002 0.838 0.160 0.007 0.306 0.687
Positive effect 1000 0.000 0.700 0.300 0.003 0.426 0.571
Positive effect 2500 0.000 0.380 0.620 0.000 0.657 0.343
Positive effect 5000 0.000 0.098 0.902 0.000 0.868 0.132
Positive effect 10,000 0.000 0.001 0.999 0.000 0.980 0.020
Small positive effect 250 0.011 0.925 0.064 0.048 0.175 0.777
Small positive effect 500 0.006 0.917 0.077 0.020 0.188 0.792
Small positive effect 1000 0.003 0.892 0.105 0.011 0.175 0.814
Small positive effect 2500 0.002 0.764 0.234 0.003 0.253 0.744
Small positive effect 5000 0.000 0.621 0.379 0.000 0.323 0.677
Small positive effect 10,000 0.000 0.364 0.636 0.000 0.444 0.556
True null 250 0.028 0.935 0.037 0.089 0.104 0.807
True null 500 0.018 0.961 0.021 0.064 0.069 0.867
True null 1000 0.027 0.946 0.027 0.052 0.049 0.899
True null 2500 0.031 0.947 0.022 0.034 0.026 0.940
True null 5000 0.026 0.949 0.025 0.020 0.015 0.965
True null 10,000 0.027 0.953 0.020 0.008 0.003 0.989
Table 4 Baseline specification: aggregate numeric summaries across scenarios and sample sizes
Scenario n per arm Mean
p-value
Mean
diff_hat
Post prob
negative
Post prob
null
Post prob
positive
BF negative BF null BF positive
Negative effect 250 0.406 − 0.021 0.666 0.094 0.240 1025.673 10.787 0.794
Negative effect 500 0.336 − 0.021 0.732 0.114 0.154 3143.095 13.916 0.336
Negative effect 1000 0.224 − 0.020 0.800 0.119 0.082 10,238.512 15.045 0.152
Negative effect 2500 0.082 − 0.020 0.902 0.083 0.015 39,153.317 11.379 0.018
Negative effect 5000 0.016 − 0.020 0.963 0.036 0.001 152,987.464 4.716 0.001
Negative effect 10,000 0.000 − 0.020 0.996 0.004 0.000 547,246.426 0.417 0.000
Positive effect 250 0.428 0.019 0.271 0.090 0.639 0.921 10.314 2090.771
Positive effect 500 0.387 0.018 0.202 0.116 0.682 1.528 13.983 1053.659
Positive effect 1000 0.263 0.020 0.103 0.120 0.777 0.208 15.439 12,370.333
Positive effect 2500 0.112 0.020 0.026 0.095 0.880 0.033 13.186 43,887.105
Positive effect 5000 0.020 0.020 0.002 0.039 0.959 0.002 5.099 109,828.665
Positive effect 10,000 0.001 0.020 0.000 0.007 0.993 0.000 0.754 400,090.372
Small positive effect 250 0.482 0.011 0.343 0.100 0.557 2.285 11.373 11.407
Small positive effect 500 0.449 0.011 0.272 0.134 0.594 1.155 16.206 1044.271
Small positive effect 1000 0.440 0.010 0.224 0.183 0.592 0.718 24.071 18.242
Small positive effect 2500 0.319 0.010 0.105 0.225 0.670 0.241 34.519 1038.926
Small positive effect 5000 0.221 0.010 0.045 0.239 0.716 0.064 42.335 4070.166
Small positive effect 10,000 0.095 0.010 0.007 0.196 0.796 0.009 39.333 10,230.787
True null 250 0.486 0.000 0.454 0.104 0.442 6.013 12.074 12.311
True null 500 0.506 − 0.000 0.430 0.150 0.420 2.929 18.535 1035.192
True null 1000 0.503 − 0.001 0.408 0.208 0.383 2.737 28.093 2.999
True null 2500 0.494 − 0.000 0.339 0.321 0.340 2.134 52.083 1.536
True null 5000 0.482 − 0.000 0.287 0.437 0.277 1.409 89.367 1.399
True null 10,000 0.504 − 0.000 0.219 0.597 0.184 0.727 191.052 0.452

M. Fina, C. Hofacker
Table 5 Single cumulative example paths under the four scenarios
Scenario n per
arm
diff_hat p-value Post prob
negative
Post
prob
null
Post prob
positive
BF
negative
BF null BF positive Frequentist class Bayesian class
Negative
effect
250 − 0.044 0.079 0.941 0.034 0.025 16.461 3.940 0.026 Non-significant Evidence for
negative effect
Negative
effect
500 − 0.012 0.512 0.655 0.172 0.173 1.935 22.372 0.213 Non-significant Evidence for
practical null
Negative
effect
1000 − 0.010 0.446 0.640 0.227 0.133 1.822 32.298 0.156 Non-significant Evidence for
practical null
Negative
effect
2500 − 0.004 0.589 0.466 0.411 0.124 0.913 70.389 0.140 Non-significant Evidence for
practical null
Negative
effect
5000 − 0.019 0.001 0.993 0.007 0.000 136.190 0.624 0.000 Negative effect
detected
Evidence for
negative effect
Negative
effect
10,000 − 0.019 0.000 1.000 0.000 0.000 2594.763 0.035 0.000 Negative effect
detected
Evidence for
negative effect
Positive
effect
250 − 0.020 0.482 0.713 0.109 0.178 2.578 11.871 0.217 Non-significant Evidence for
practical null
Positive
effect
500 − 0.034 0.102 0.916 0.054 0.030 11.259 6.236 0.031 Non-significant Evidence for
negative effect
Positive
effect
1000 − 0.013 0.358 0.723 0.177 0.100 2.623 21.262 0.115 Non-significant Evidence for
practical null
Positive
effect
2500 − 0.001 0.927 0.314 0.439 0.247 0.488 86.235 0.319 Non-significant Evidence for
practical null
Positive
effect
5000 0.019 0.003 0.000 0.013 0.987 0.000 1.292 75.960 Positive effect
detected
Evidence for
positive effect
Positive
effect
10,000 0.021 0.000 0.000 0.000 1.000 0.000 0.000 995,210.497 Positive effect
detected
Evidence for
positive effect
Small posi-
tive effect
250 0.020 0.488 0.196 0.111 0.693 0.258 13.131 2.221 Non-significant Evidence for
practical null
Small posi-
tive effect
500 0.004 0.836 0.328 0.192 0.480 0.504 29.427 0.924 Non-significant Evidence for
practical null
Small posi-
tive effect
1000 0.014 0.319 0.086 0.175 0.739 0.094 20.942 2.956 Non-significant Evidence for
practical null
Small posi-
tive effect
2500 0.015 0.085 0.010 0.116 0.873 0.010 16.757 7.522 Non-significant Evidence for
practical null
Small posi-
tive effect
5000 0.017 0.005 0.000 0.021 0.979 0.000 2.061 48.248 Positive effect
detected
Evidence for
positive effect
Small posi-
tive effect
10,000 0.014 0.002 0.000 0.020 0.980 0.000 1.980 50.796 Positive effect
detected
Evidence for
positive effect
True null 250 − 0.024 0.395 0.752 0.097 0.151 3.203 13.320 0.174 Non-significant Evidence for
practical null
True null 500 − 0.024 0.225 0.829 0.101 0.070 5.199 10.486 0.073 Non-significant Evidence for
practical null
True null 1000 0.004 0.772 0.266 0.273 0.462 0.358 41.307 0.897 Non-significant Evidence for
practical null
True null 2500 − 0.008 0.381 0.623 0.306 0.071 1.709 38.200 0.077 Non-significant Evidence for
practical null
True null 5000 0.000 1.000 0.200 0.594 0.206 0.270 144.722 0.251 Non-significant Evidence for
practical null
True null 10,000 0.002 0.708 0.062 0.719 0.219 0.068 218.020 0.286 Non-significant Evidence for
practical null
Table 6 Sensitivity-analysis settings
Sensitivity dimension Settings
Prior Uniform Beta(1,1); Jeffreys
Beta(0.5,0.5); Mild informa-
tive Beta(2,18)
ROPE  ± 0.25 pp; ± 0.50 pp; ± 1.00 pp
Bayes-factor threshold 2; 3; 10

Bayesian inference and the difference between evidence of absence and absence of evidence
Table 7 Sensitivity-analysis classification summary at n = 250 per arm
Sensitivity type Setting Scenario Bayes: Negative Bayes: Practical null Bayes: Positive Inconclusive
Prior Jeffreys Beta(0.5,0.5) Negative effect 0.350 0.627 0.022 0.000
Prior Jeffreys Beta(0.5,0.5) Positive effect 0.010 0.642 0.347 0.000
Prior Jeffreys Beta(0.5,0.5) Small positive effect 0.058 0.713 0.230 0.000
Prior Jeffreys Beta(0.5,0.5) True null 0.122 0.752 0.125 0.000
Prior Mild informative Beta(2,18) Negative effect 0.450 0.357 0.055 0.138
Prior Mild informative Beta(2,18) Positive effect 0.072 0.260 0.468 0.200
Prior Mild informative Beta(2,18) Small positive effect 0.145 0.330 0.260 0.265
Prior Mild informative Beta(2,18) True null 0.230 0.315 0.245 0.210
Prior Uniform Beta(1,1) Negative effect 0.247 0.728 0.025 0.000
Prior Uniform Beta(1,1) Positive effect 0.025 0.685 0.290 0.000
Prior Uniform Beta(1,1) Small positive effect 0.055 0.787 0.158 0.000
Prior Uniform Beta(1,1) True null 0.128 0.787 0.085 0.000
ROPE ROPE ± 0.25 pp Negative effect 0.315 0.665 0.020 0.000
ROPE ROPE ± 0.25 pp Positive effect 0.030 0.652 0.318 0.000
ROPE ROPE ± 0.25 pp Small positive effect 0.045 0.748 0.207 0.000
ROPE ROPE ± 0.25 pp True null 0.115 0.765 0.120 0.000
ROPE ROPE ± 0.50 pp Negative effect 0.255 0.733 0.013 0.000
ROPE ROPE ± 0.50 pp Positive effect 0.022 0.677 0.300 0.000
ROPE ROPE ± 0.50 pp Small positive effect 0.037 0.787 0.175 0.000
ROPE ROPE ± 0.50 pp True null 0.068 0.845 0.087 0.000
ROPE ROPE ± 1.00 pp Negative effect 0.217 0.772 0.010 0.000
ROPE ROPE ± 1.00 pp Positive effect 0.010 0.718 0.273 0.000
ROPE ROPE ± 1.00 pp Small positive effect 0.037 0.818 0.145 0.000
ROPE ROPE ± 1.00 pp True null 0.090 0.830 0.080 0.000
Evidence threshold BF threshold = 10 Negative effect 0.268 0.545 0.007 0.180
Evidence threshold BF threshold = 10 Positive effect 0.010 0.525 0.225 0.240
Evidence threshold BF threshold = 10 Small positive effect 0.030 0.603 0.100 0.268
Evidence threshold BF threshold = 10 True null 0.072 0.662 0.068 0.198
Evidence threshold BF threshold = 2 Negative effect 0.260 0.715 0.025 0.000
Evidence threshold BF threshold = 2 Positive effect 0.022 0.690 0.287 0.000
Evidence threshold BF threshold = 2 Small positive effect 0.048 0.787 0.165 0.000
Evidence threshold BF threshold = 2 True null 0.083 0.812 0.105 0.000
Evidence threshold BF threshold = 3 Negative effect 0.328 0.652 0.020 0.000
Evidence threshold BF threshold = 3 Positive effect 0.035 0.675 0.290 0.000
Evidence threshold BF threshold = 3 Small positive effect 0.062 0.812 0.125 0.000
Evidence threshold BF threshold = 3 True null 0.090 0.802 0.107 0.000

M. Fina, C. Hofacker
Data Availability All code used in the simulations is available from
the authors.
Declarations
Conflict of interest The authors assert there are no conflicts of interest.
All code used in the simulations is available from the authors.
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
holder. To view a copy of this licence, visit  h t    t p : / / c r e  a  t  i v e  c  o  m m o n s . o
r g / l i c e n s e s / b y / 4 . 0 /     .
References
Allenby, Greg M. 1990. Hypothesis testing with scanner data: The
advantage of bayesian methods. Journal of Marketing Research
27 (4): 379–389.
Białek, Michał, Michal Misiak, and Martyna Dziekan. 2023. The
vicious cycle that stalls statistical revolution. Nature Human
Behaviour 7:161–163.
Blozis, Shelley A. 2022. Bayesian two-part multilevel model for lon -
gitudinal media use data. Journal of Marketing Analytics 10 (4):
311–328.
Brüggemann, Philipp, Luis F. Martinez, and Francisco J. Martínez-
López. 2025. The future of analytics in digital marketing and
electronic commerce: How digitalization and sustainability affect
consumers, firms, and policymakers. Journal of Marketing Ana -
lytics 13 (3): 571–573.
Table 8 Sensitivity-analysis classification summary at n = 10,000 per arm
Sensitivity type Setting Scenario Bayes: Negative Bayes: Practical null Bayes: Positive Inconclusive
Prior Jeffreys Beta(0.5,0.5) Negative effect 0.995 0.005 0.000 0.000
Prior Jeffreys Beta(0.5,0.5) Positive effect 0.000 0.022 0.978 0.000
Prior Jeffreys Beta(0.5,0.5) Small positive effect 0.000 0.540 0.460 0.000
Prior Jeffreys Beta(0.5,0.5) True null 0.010 0.978 0.013 0.000
Prior Mild informative Beta(2,18) Negative effect 1.000 0.000 0.000 0.000
Prior Mild informative Beta(2,18) Positive effect 0.000 0.005 0.995 0.000
Prior Mild informative Beta(2,18) Small positive effect 0.000 0.403 0.598 0.000
Prior Mild informative Beta(2,18) True null 0.020 0.963 0.018 0.000
Prior Uniform Beta(1,1) Negative effect 0.993 0.007 0.000 0.000
Prior Uniform Beta(1,1) Positive effect 0.000 0.013 0.988 0.000
Prior Uniform Beta(1,1) Small positive effect 0.000 0.613 0.388 0.000
Prior Uniform Beta(1,1) True null 0.010 0.980 0.010 0.000
ROPE ROPE ± 0.25 pp Negative effect 1.000 0.000 0.000 0.000
ROPE ROPE ± 0.25 pp Positive effect 0.000 0.003 0.998 0.000
ROPE ROPE ± 0.25 pp Small positive effect 0.000 0.405 0.595 0.000
ROPE ROPE ± 0.25 pp True null 0.022 0.968 0.010 0.000
ROPE ROPE ± 0.50 pp Negative effect 0.995 0.005 0.000 0.000
ROPE ROPE ± 0.50 pp Positive effect 0.000 0.010 0.990 0.000
ROPE ROPE ± 0.50 pp Small positive effect 0.000 0.585 0.415 0.000
ROPE ROPE ± 0.50 pp True null 0.003 0.988 0.010 0.000
ROPE ROPE ± 1.00 pp Negative effect 0.887 0.113 0.000 0.000
ROPE ROPE ± 1.00 pp Positive effect 0.000 0.160 0.840 0.000
ROPE ROPE ± 1.00 pp Small positive effect 0.000 0.853 0.147 0.000
ROPE ROPE ± 1.00 pp True null 0.000 1.000 0.000 0.000
Evidence threshold BF threshold = 10 Negative effect 0.995 0.000 0.000 0.005
Evidence threshold BF threshold = 10 Positive effect 0.000 0.022 0.978 0.000
Evidence threshold BF threshold = 10 Small positive effect 0.000 0.583 0.407 0.010
Evidence threshold BF threshold = 10 True null 0.005 0.988 0.007 0.000
Evidence threshold BF threshold = 2 Negative effect 0.993 0.007 0.000 0.000
Evidence threshold BF threshold = 2 Positive effect 0.000 0.015 0.985 0.000
Evidence threshold BF threshold = 2 Small positive effect 0.000 0.595 0.405 0.000
Evidence threshold BF threshold = 2 True null 0.020 0.973 0.007 0.000
Evidence threshold BF threshold = 3 Negative effect 0.995 0.005 0.000 0.000
Evidence threshold BF threshold = 3 Positive effect 0.000 0.015 0.985 0.000
Evidence threshold BF threshold = 3 Small positive effect 0.000 0.585 0.415 0.000
Evidence threshold BF threshold = 3 True null 0.003 0.990 0.007 0.000

Bayesian inference and the difference between evidence of absence and absence of evidence
Bultez, Alain, and Jean-Luc. Herrmann. 2025. Value added to market-
ing research diagnoses by add-ons to P-Values. Journal of Mar-
keting Analytics 13 (2): 445–466.
Campbell, Colin, Jeffrey M. Girard, Daniel McDuff, and Sara Rosen -
gren. 2026. How influencers grow: An empirical study and
future research agenda. Journal of Interactive Marketing  61 (2):
117–136.
Feinberg, Fred. 2024. P-values as qwerty: Curating evidence in the
computational era. Journal of Marketing 88 (3): 20–28.
Gallistel, C. R. 2009. The importance of proving the null. Psychologi-
cal Review 116 (2): 439.
Gary, Joston, Jiang Lu, Yan Feng, Zihan Wang, Yang Gu, Soo-Cheng
Chuah, Simão Sil and António Carrizo Moreira. 2025. The subtle
power of nudging: Consumer choice in ethical and sustainable
retailing (in press). Journal of Marketing Analytics 1–27.
Gilbride, Timothy J., Peter J. Lenk, and Jeff D. Brazell. 2008. Market
share constraints and the loss function in choice-based conjoint
analysis. Marketing Science 27 (6): 995–1011.
Gorostiza-Esquerdeiro, Ignacio, David Buján-Carballa and Aitor
Oyarbide-Zubillaga 2026. MWIN (Measure What Is Needed): A
strategic framework for privacy-first, AI-ready, and data-driven
marketing analytics. Journal of Marketing Analytics 14(1).
Hofacker, Charles F., Huong N. L. Nguyen, and Matteo Fina. 2024.
Bayesian inference and consumer behavioral theory. Psychology
& Marketing 41 (12): 3144–3156.
Keysers, C., V . Gazzola, and E.-J. Wagenmakers. 2020. Using Bayes
factor hypothesis testing in neuroscience to establish evidence of
absence. Nature Neuroscience 23:788–799.
Kruschke, John K. 2010. Bayesian data analysis. Wires Cognitive Sci-
ence 1 (5): 658–676.
Kruschke, John K. 2021. Bayesian reporting guidelines. Nature
Human Behavior 5:1282–1291.
McShane, Blakeley B., Eric T. Bradlow, John G. Lynch, and Robert J.
Meyer. 2024. “Statistical significance” and statistical reporting:
Moving beyond binary. Journal of Marketing 88 (3): 1–19.
Perezgonzalez, Jose D. 2015. Fisher, Neyman-Pearson or NHST? A
tutorial for teaching data testing. Frontiers in Psychology 6 : 223.
Petrescu, Maria, and Anjala S. Krishen. 2025. The significance of
nothing: A call to discussion. Journal of Marketing Analytics 13
(4): 1033–1034.
Rigdon, Edward E. 2026. Statistical Stockholm Syndrome: The Sta -
tistical Significance Myth Is the Problem (in press). Journal of
Marketing Analytics.
Rouder, J. N., P. L. Speckman, D. Sun, R. D. Morey, and G. Iverson.
2009. Bayesian t tests for accepting and rejecting the null hypoth-
esis. Psychonomic Bulletin & Review 16 (2): 225–237.
Schad, Daniel J., Bruno Nicenboim, Paul-Christian. Bürkner, Michael
Betancourt, and Shravan Vasishth. 2023. Workflow techniques
for the robust use of bayes factors. Psychological Methods 28 (6):
1404–1426.
Wedel, Michel, and Chen Dong. 2020. BANOV A: Bayesian analysis
of experiments in consumer psychology. Journal of Consumer
Psychology 30 (1): 3–23.
Wedel, Michel, Chen Dong, and Anna Kopyakova. 2024. Bayesian
analysis of experimental and observational data: A review and
illustration of the BANOV A R package. Journal of Marketing
Analytics 12 (3): 735–742.
Publisher's Note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional affiliations.
Matteo Fina is a doctoral student at the Graduate School of Econom-
ics, Finance and Management at Goethe University Frankfurt.
Charles Hofacker  is Persis Rockwood Professor of Marketing at
Florida State University’s Wertheim College of Business.
