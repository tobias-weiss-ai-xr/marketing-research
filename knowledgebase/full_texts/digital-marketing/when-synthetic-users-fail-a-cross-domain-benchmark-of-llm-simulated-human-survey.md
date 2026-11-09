---
title: 'When Synthetic Users Fail: A Cross-Domain Benchmark of LLM-Simulated Human Survey Responses'
url: https://arxiv.org/abs/2607.26348
category: digital-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Zihan Chen
- Di Zhu
- Lei Nico Zheng
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.26348
pages: 19
chars: 83034
fetched_at: '2026-11-08T13:21:45+00:00'
kb_version: 1
---

# When Synthetic Users Fail: A Cross-Domain Benchmark of LLM-Simulated Human Survey Responses

WHENSYNTHETICUSERSFAIL: A CROSS-DOMAIN
BENCHMARK OF
LLM-SIMULATEDHUMANSURVEYRESPONSES ∗
Zihan Chen
Stevens Institute of Technology
Hoboken, NJ, USA
zchen61@stevens.edu
Di Zhu
Stevens Institute of Technology
Hoboken, NJ, USA
dzhu1@stevens.edu
Lei Nico Zheng
University of Massachusetts Boston
Boston, MA, USA
lei.zheng@umb.edu
ABSTRACT
Large language models (LLMs) are increasingly used as synthetic users, stand-ins for human re-
spondents whose simulated answers feed product, policy, and market decisions. We ask when this
substitution is valid and when it fails, and package the answer as an evaluation framework for intelli-
gent synthetic-user systems. A single protocol, run across four models spanning two families and an
8B-to-frontier capability range, is applied to two independent domains of real human-response data:
U.S. general social attitudes (General Social Survey) and cross-cultural values (World Values Survey).
Every model is benchmarked against a suite of non-LLM baselines fit on held-out human data. Under
demographic prompting and the survey-simulation protocols we test, two failures replicate across
both domains, all four models, and both families. First, at the individual level no LLM beats even
the strongest baseline; on cross-cultural values every model falls well below it, and the gap survives
distance-aware and proper scoring. Second, models systematicallyover-determinedemographics,
treating identity as far more predictive of attitudes than it is among real people, a distortion present for
nearly every question–group combination and robust to a coding-invariant measure. Neither failure is
remedied by a larger, more capable model. A decision-impact analysis shows why this matters in
practice: on a segment-targeting task the models inflate between-segment gaps two to fourfold, would
direct a team to the wrong segment in half of U.S. and most cross-cultural cases, and manufacture
segment splits that do not exist in real people. We publicly release the cross-domain benchmark and
validation framework, including all code and data, so that teams can determine in advance when
synthetic-user evidence is safe for decision support and when it is not.
Keywordslarge language models · synthetic users · survey simulation · social simulation · evaluation benchmark ·
stereotyping·responsible AI
1 Introduction
Running a human study is slow and expensive, so a fast-growing body of work proposes replacing human participants
with large language models (LLMs) prompted to behave assynthetic users, using them to pilot surveys, pre-test
questionnaire items, estimate opinion distributions, and stand in for study participants. The appeal is obvious: a survey
that takes months and thousands of dollars to field can, in principle, be approximated in minutes at the cost of a few
API calls.
These simulated respondents are increasingly wired intodecision-supportpipelines. Product teams query synthetic
personas to prioritize features, marketers use them to pre-test messaging and estimate segment-level demand through
“silicon samples” [1, 2], and policy and organizational analysts use them to gauge how a population might react before
∗This manuscript is currently under peer review. Code and data are publicly available at: https://github.com/
ZihanChen1995/when-synthetic-users-fail-a-cross-domain-benchmark-of-llm-simulated-human-survey-
responses
arXiv:2607.26348v2  [cs.CL]  4 Oct 2026

committing resources. In each case an intelligent system is asked to manufacture evidence that a human sample
would normally provide, and a downstream decision is made on that evidence. Viewed this way, a synthetic user is an
evidence-producing component of an intelligent decision-support system, and, like any such component, it should be
verified and validated against its intended use before it is trusted [3, 4]. This is precisely the setting where an unnoticed
failure is costly: if the synthetic users are wrong in a structured way, the resulting decisions inherit that error at scale1.
A practical evaluation framework, one that tells a teamin advancewhether synthetic-user evidence is trustworthy for
the decision at hand, is therefore as important as the simulation method itself. Building that framework is the goal of
this paper.
The central unresolved question is not whether LLMs can produce survey-shapedoutput (they trivially can) butwhen
the substitution is valid and when it fails. The evidence so far is conflicting: some studies report encouraging aggregate
alignment [5], while others warn that substitution is unsafe [6, 7]. Prior work has also largely answered the question one
domain at a time (political surveys, or cultural values, or a single national survey), often reporting a single aggregate
similarity number that can look reassuring even when the underlying simulation is poor. Two questions are therefore
under-answered. (i) Is a synthetic user actually more informative than the trivial thing it is supposed to replace, a
lookup of “what do people with these demographics usually answer”? (ii) Do conclusions about validitytransfer across
domains, or is each positive result an artifact of one survey, one model, or one prompt?
We address both with a deliberately unified design. We fix one protocol (the same models, prompts, decoding, sampling,
and metrics) and apply it to two independent domains ofrealhuman-response ground truth:
• U.S. general social attitudes.The General Social Survey (GSS), 2016–2024 waves, 10 attitude questions
spanning wellbeing, social trust, moral/policy positions, gender-role attitudes, and institutional confidence.
• Cross-cultural values.The World Values Survey (WVS) Wave 7, 63 countries, 16 ordinal value questions
spanning economic values, corruption perceptions, immigration attitudes, views of science, religiosity, and
moral justifiability.
Across these domains we evaluate four models from two families across an 8B-to-frontier capability range, under two
prompt formats (a single-answer prompt and a probability-distribution prompt). The design choice that makes our
individual-level results interpretable, and which much prior work omits, is an explicitnaive demographic baseline:
for each question we fit the conditional distribution of human answers given demographics on a held-out portion of
the real data, and score every LLM against it on the same respondents. Without this yardstick, “the model predicts
individuals with X% accuracy” is uninterpretable, because individual survey answers are not a deterministic function
of demographics; there is an irreducible ceiling that a trivial predictor already captures.
Research questionsWe formalize the study as five research questions. The first three ascend the levels of analysis at
which synthetic users are actually deployed, from the individual respondent (RQ1), through the population aggregate
(RQ2), to the demographic structure of opinion (RQ3); the final two then ask whether those answers are stable to
modelling choices (RQ4) and whether they transfer across domains (RQ5).
RQ1 Individual fidelity vs. a trivial baseline.Do LLM synthetic users predict individual human answers more
accurately than a naive demographic-conditional predictor?
RQ2Aggregate fidelity.Do LLM synthetic users reproduce the population-level distribution of human answers?
RQ3 Subgroup structure.Do LLMs represent the demographic structure of attitudes faithfully, or do they distort
how predictive demographics are of answers?
RQ4 Stability and capability.Are these behaviors stable across model family, model capability, and output format?
RQ5Cross-domain transfer.Do the answers to RQ1–RQ4 hold in both domains, or are they domain-specific?
Headline findingsOur central result is that, under demographic prompting and the survey-simulation protocols we
test, LLM synthetic users exhibit two distinct failures that replicate acrossbothdomains,all fourmodels, andboth
families. The first is alack of individual-level advantage.As yardsticks we build a suite of non-LLM predictors, from
a “demographic lookup table” (for any set of demographics, it returns the answer most common among real people with
those demographics) up to learned demographic models (logistic regression, random forest). On GSS (U.S. attitudes)
every LLM, at best, only ties the lookup table and trails the learned baseline; on WVS (cross-cultural values) every
model is11 to 22 percentage points less accuratethan the baseline. The gap is not an artifact of exact-match scoring: it
1“Fail” is scoped throughout todemographic prompting under survey-simulation protocols: the specific elicitation setting we
test. We make no claim about synthetic users produced by other means (e.g. fine-tuning or richer persona construction), which the
protocol is designed to evaluate in turn.
2

persists under distance-aware metrics that give partial credit for near-misses on ordinal scales, and under proper scoring
of the distribution outputs, where the model assignslowerprobability to the true human answer than the baseline.
In short, an LLM asked to role-play an individual adds no information beyond what the demographics alone already
imply, and for value questions it is substantially worse. The second failure isdemographic over-determination, or
stereotyping. We measure how strongly a demographic attribute predicts a person’s answer (the share of the variation in
answers that is explained by which group the person is in) and compare that share for real humans versus for the model.
Models consistently exaggerate it. For U.S. political leaning and confidence in banks, for example, a person’s politics
explains only about 1.5% of the variation in real answers, yet the model behaves as though it explains up to roughly
67%. This exaggeration is present, and statistically distinguishable from chance, for nearly every question–group
combination in both domains, and it replicates under a coding-invariant association measure that makes no numeric
assumption about the answer scale. Crucially,neither failure is fixed by using a bigger, more capable model: the
frontier models stereotype at least as strongly as the small 8B model, and often more.
ContributionsTaken together, our contributions are both methodological and practical. On themethodological
and empiricalside we make four. First, we build a compact, reproduciblecross-domain benchmarkfor LLM
synthetic users, spanning U.S. social attitudes and 63-country values under a single protocol and packaged as a reusable,
publicly released evaluation toolkit (data-build, inference, and analysis scripts, with all prompts, parser rules, and
baselines specified in the appendices). Second, we develop abaseline-anchored evaluation: we show that the standard
individual-accuracy number is uninterpretable without non-LLM baselines, and that against a suite of them (question-
marginal, demographic lookup, and learned demographic models) LLMs show no individual-level advantage, a result
we confirm with distance-aware metrics for ordinal scales and proper scoring (log-loss, Brier) for distribution outputs,
with paired-bootstrap confidence intervals throughout. Third, we introduce astereotyping index, a single, bounded
number that compares how predictive a demographic attribute is of the answer in the model versus in real people,
reported with confidence intervals and paired with a coding-invariant companion measure (Cramér’s V) that requires no
numeric coding of answers; it reframes the common worry that “LLMs flatten minorities” into its measurable opposite
for identity-linked attitudes, namely that LLMsover-associatedemographics with answers, treating identity as more
decisive than it really is. Fourth, we provide adecision-impact analysisthat carries the over-determination finding
through to the decision a synthetic user is meant to support: on the canonical segment-targeting task, we quantify how
far the models inflate between-segment gaps (two to fourfold), how often they would send a team to the wrong segment
(50–72% of cases), and how often they manufacture a segment split that does not exist in real people (up to 41% of
cases on cross-cultural values).
On thepractical, applied-intelligent-systemsside, these pieces combine into our main deliverable: avalidation
framework for intelligent synthetic-user systemsused in decision support. It is not merely a benchmark of model
outputs but a verification-and-validation procedure a practitioner runsbeforedeployment, one that reports individual
and aggregate fidelity separately, always against non-LLM baselines; reports subgroup determinism and its decision
impact; reports invalid-output rates; and never assumes a larger model is a safer synthetic user. The framework is the
deliverable; the negative findings are the evidence that a framework of this kind is necessary.
The remainder of the paper reviews related work (Section 2), details the data, protocol, and metrics (Section 3), presents
results by research question (Section 4), and discusses implications and limitations (Sections 5–6).
2 Related Work
Our study sits at the intersection of six literatures. We review each in turn, then state the gap that motivates a
baseline-anchored, cross-domain validation framework.
2.1 LLMs as simulated survey respondents and participants
A fast-growing line of work treats LLMs as programmable populations, prompting them with personas or demographics
to predict opinions and behaviors. The optimistic anchor is Argyle et al.[5], who show that demographically conditioned
prompts can reproduce aggregate patterns in U.S. political survey data, launching the “silicon sample” idea; related
work extends the substitution to behavioral experiments [ 8], economic agents [ 9], and the generation of synthetic
research data in HCI and product settings [10]. A skeptical counter-current quickly followed. Bisbee et al. [6] show that
LLM-generated survey responses can misrepresent population and subgroup variation; Santurkar et al. [11] find that
model “opinions” align more with some demographic groups than others rather than neutrally representing a population;
and Dominguez-Olmedo et al. [12] show that model survey answers are sensitive to ordering and labeling, and so
should not be read as direct measurements of population beliefs. Position pieces in cognitive science and psychology
3

sharpen the caution: replacing human participants risks confusing linguistic plausibility with validity [7, 13, 14]. The
practical problem for this paper is precisely this gap between survey-shaped output and valid evidence.
2.2 Survey-simulation benchmarks and cross-cultural value modeling
A parallel effort builds benchmarks that make survey and cross-cultural value simulation measurable at scale. WorldVal-
uesBench derives a large demographic-context-to-answer benchmark from the World Values Survey [15]; SocioBench
evaluates LLMs as survey-response predictors across countries and sociological domains [ 16]; and distribution-
specialization work fine-tunes models to match country-level response distributions, improving group-level prediction
while still struggling to generalize [17]. One of our two domains reuses the WorldValuesBench question set and scales
for comparability. Our work differs from these benchmarks on three axes that matter for a validity claim. First,reference
point: WorldValuesBench and SocioBench score model accuracy against the human answer, but not against a non-LLM
predictor of that answer, so a reported accuracy cannot be read as evidence that the simulation adds information; our
demographic-lookup and learned baselines supply exactly that missing reference, and against it the individual-level
advantage disappears. Second,level of analysis: these benchmarks (and the distribution-specialization work of Cao
et al. [17], which improves group-level fit through fine-tuning) target aggregate or country-level distributions, which
our RQ2 confirms models reproduce reasonably; we show that aggregate success coexists with individual-level failure
and with a subgroup distortion the aggregate metric cannot see. Third,cross-domain transfer: each benchmark fixes a
single survey instrument, so a positive or negative result could be an artifact of that instrument; by holding one protocol
fixed across a U.S. attitude survey and a 63-country value survey we can separate properties of LLM simulation from
properties of a dataset. In short, we complement calibrated value and persona benchmarks by asking whether simulated
users add individual-level information beyond a demographic baseline, whether the demographic structure of answers is
faithful, and whether the answer transfers across domains.
2.3 Persona prompting, silicon samples, and prompt artifacts
Persona and demographic prompting is the dominant mechanism for constructing synthetic users, and it is used well
beyond political surveys: in marketing and consumer research, where “silicon samples” are proposed as low-cost
respondent pools [1], and in automated perceptual analysis for product decisions [2]. Crucially, persona assignment
is not a neutral conditioning operation. It can amplify toxicity and stereotypes [ 18], the surface architecture of a
prompt can induce methodological artifacts [19], sociodemographic persona formulations materially change model
behavior [20], and persona generation itself carries quality and validity pitfalls [21]. This literature motivates treating
prompt-surface stability and demographic over-determination (our RQ3–RQ4) as first-order validity conditions rather
than minor robustness checks.
2.4 Social simulation and LLM agents
Synthetic survey respondents are one instance of a broader movement to simulate humans with LLMs. Generative
agents endow LLMs with memory, reflection, and planning to produce believable individual and social behavior [22],
building on earlier populated prototypes for social computing systems [23]; recent surveys map the field from individual
agents to whole-society simulation [24] and assess the promise and epistemic risks of LLMs for computational social
science [25]. This work mostly evaluates believability or downstream system behavior; we contribute a quantitative,
human-anchored validity benchmark for one high-stakes class of these simulations.
2.5 Algorithmic stereotyping, fairness, and subgroup validity
Our over-determination finding connects to a long line of work on social bias in learned representations: human-like
biases in embeddings [26, 27], stereotyped associations in generation [28], and representational harms of large mod-
els [29]. The fairness literature further establishes that aggregate performance can mask subgroup harm: intersectional
accuracy disparities [30], group-conditioned error criteria [ 31], hand-built bias benchmarks for constrained-choice
QA [32], and the reminder that fairness must be assessed within the sociotechnical context of use [33]. Our stereotyping
index adapts this subgroup lens but differs in target: rather than asking whether a model attaches a negative label
to a group, we comparehow predictivedemographics are of an answer in the model versus in real humans, turning
stereotyping into a human-comparable validity metric.
2.6 Decision-support validity and expert-system validation
For an applied-AI venue, the decisive framing is that synthetic users are evidence-producing components inside
intelligent decision-support systems, and such components require verification and validation against intended use.
4

Information-systems research treats predictive validity (out-of-sample performance against baselines) as a first-class
evaluation goal distinct from explanatory fit [3]; the decision-support and expert-systems tradition has long emphasized
verification, validation, and evaluation of intelligent artifacts [ 4, 34, 35]. Multi-metric reporting norms from ML
evaluation reinforce the same discipline: holistic evaluation across accuracy, calibration, robustness, and fairness [36],
behavioral testing beyond aggregate accuracy [37], broad capability benchmarks [38], and standardized documentation
of models and datasets [39, 40]. Finally, survey methodology’s total-survey-error framework distinguishes representation
from measurement error [41], which is exactly why individual, aggregate, and subgroup validity are separate questions:
an LLM synthetic user introduces a new error source that can look benign in aggregate while failing at the individual or
subgroup level.
2.7 What is missing
This prior work is strong but fragmented: each study typically fixes one domain, one or two models, and one evaluation
lens, which makes it hard to tell whether a reported failure (or success) is a property of LLM simulation or of the specific
setup. Two gaps matter for practice. First, individual-level results are usually reported withoutnon-LLM baselines, so it
is unclear whether the model beats a demographic lookup, let alone a learned demographic model [3], and whether any
apparent gap is merely an artifact of harsh exact-match scoring on ordinal scales. Second, subgroup analyses typically
ask whether groups are “flattened,” but do not quantify, on a human-comparable scale, how much demographicsshould
explain versus how much the model makes them explain. We close both gaps by anchoring individual fidelity to a
baseline suite scored with distance-aware and proper-scoring metrics, and by quantifying subgroup determinism with
both a variance-based and a coding-invariant association measure. Holding one protocol fixed across two domains and
four models, we then test whether the conclusions transfer.
3 Data, Protocol, and Metrics
3.1 Domains and scope
We use two public human-response datasets and state the scope we actually use; all claims are restricted to that scope.
GSS (U.S. social attitudes).We use the GSS 1972–2024 cumulative file restricted to the2016–2024waves. Recent
waves give large per-subgroup cells and partially mitigate pretraining contamination relative to decades-old waves.
After removing respondents with missing values on any prompt demographic, the in-scope pool is 14,704 respondents
and 85,898 (respondent, question) pairs over 10 questions. Demographics used in the prompt: age, sex, race, highest
degree, region, political views, party identification.
WVS (cross-cultural values).We use WVS Wave 7 (inverted CSV , v6.0). We retain the 16 value questions from
the WorldValuesBench probe set [15] that are present in this release; question wordings and ordinal scales follow
WorldValuesBench for comparability. After demographic filtering the in-scope pool is 91,774 respondents across 63
countries and 1,426,473 (respondent, question) pairs. Demographics: age group, sex, education level, settlement type
(urban/rural), and country.
3.2 Sampling for measurable distributions
Our headline analyses need a reliable estimate of the human answerdistributionwithin each (question, group) cell,
which requires enough people in each cell. We therefore sample by cell rather than drawing respondents at random. For
each domain we draw about 100 respondents per question (GSS: 993 rows; WVS: 1,458 rows), allocated so that the
main grouping is well covered (GSS: degree × race; WVS: country). Importantly, the human answer distributions and
the demographic baseline are always estimated from the full dataset, never from this small sample, so the human side of
every comparison rests on large, stable numbers.
3.3 Models and prompting
We evaluate four chat-style models through a single, common interface: Claude Haiku 4.5 and Claude Sonnet 4.6 (the
closedfamily: proprietary, accessed via an API) and Llama-3.1-8B and Llama-3.3-70B (theopenfamily: open-weight
and publicly downloadable). Together these span two independent model families and a wide capability range, from
a small 8B model to frontier-scale systems. Each sampled respondent is run under two prompt formats and two
independent generation runs (“seeds,” which differ only in the model’s internal randomness, letting us gauge run-to-run
noise):
5

• Style A, the single-answer prompt.The model is shown the demographic profile and question and must
return one answer (an option letter for short-labelled questions, or the scale number for numeric scales).
• Style C, the distribution prompt.The model must return a probability for each answer option, expressed as
JSON.
We use these two names (Style A / single-answer prompt, Style C / distribution prompt) interchangeably throughout.
The model’s internal randomness is held at a fixed setting across models; the two seeds probe run-to-run stability. All
calls use the same output parser, which flags any response it cannot read as a valid answer asinvalid/refused.
3.4 Non-LLM baselines
The individual-accuracy number is only interpretable against what a non-LLM predictor achieves on the same people,
so we build a suite of four non-LLM baselines. All are fit on a held-out 50% split of the in-scope pool (assigned by a
hash of the respondent id) and evaluated on the evaluation-sample rows, which come from the other split, so no baseline
is ever fit and scored on the same respondents. The four baselines, from simplest to most sophisticated, are as follows
(full formulae and hyperparameters are in Appendix E):
• Question marginal.The single most common answer to the question among the fit humans (ignores
demographics entirely).
• Demographic lookup(our primary yardstick). A predictor of the conditional answer distribution given
demographics, which backs off from a fine demographic cell to a coarse cell to the question marginal, so it
always yields a prediction. For WVS the finest cell begins with country; the coarse cell is country alone, which
we also report separately as acountry-onlybaseline.
•Multinomial logistic regressionon the one-hot-encoded prompt demographics, fit per question.
•Random foreston the same features (300 trees), a nonlinear learned baseline.
The demographic lookup and logistic model also emit a full predicteddistributionover answers, which we use as the
reference for the proper-scoring comparison against the model’s distribution outputs (Section 3.5). These baselines are
the yardsticks for RQ1: following the predictive-validity tradition in information systems [3], a synthetic user earns its
place only by beating a simpler predictor on held-out human data.
3.5 Metrics
We use four families of metric, one per research question. Reporting individual, aggregate, and subgroup fidelity
separately mirrors the total-survey-error distinction between measurement and representation error [41] and the multi-
metric evaluation norms now standard for language models [ 36, 37]: a single aggregate number hides exactly the
failures we care about. Each metric is stated in plain terms first, then defined precisely. Every headline comparison
against a baseline carries apaired-bootstrap 95% confidence interval: we resample the evaluation-sample rows 500
times, scoring model and baseline on thesamerows in each resample, and report the interval of the difference, so the
reader can tell a real margin from sampling noise.
Individual fidelity (RQ1): can the model guess one person’s answer?We reportaccuracy(the fraction of individuals
whose exact answer the model predicts correctly) next to each baseline’s accuracy on the same people. For the
distribution prompt (Style C), the model’s single “guess” is the option it assigned the highest probability (the arg-max
of its distribution). Exact-match accuracy is deliberately harsh on long ordinal scales, so for the ordinal questions we
also report twodistance-awaremetrics that give partial credit for being close. Themean absolute error(MAE) is the
average gap, in scale points, between the single predicted answer and the true one. Theearth-mover’s distance(EMD)
uses the whole predicted distribution from the distribution prompt: it is the expected number of scale steps needed to
move the predicted probability mass onto the true answer, and so rewards a distribution that concentrates near the truth
even when its mode is wrong. Both are reported for the model and for the baseline on the same rows.
Aggregate fidelity (RQ2): does the model reproduce the group’s answerspread?Rather than any one person, we
compare the overallshareof people choosing each option (the answer distribution) between the model and real humans.
We summarize the gap between two distributions with theJensen–Shannon (JS) divergence, a standard 0-to-1 measure
of how different two probability distributions are; 0 means identical, and larger means further apart, so lower is better.
Because we sample by cell rather than at random (Section 3.2), the raw pooled model distribution reflects our sampling
design, not the human population. We therefore also report apopulation-reweightedJS, in which each cell’s model
distribution is weighted back to that cell’s share of the real population before comparing to the true (full-table) human
distribution. If the two versions agree, the aggregate-fidelity result is not an artifact of the sampling design.
6

For the distribution prompt (Style C), arg-max accuracy discards most of the predicted distribution, so we additionally
score thewholedistribution with two proper scoring rules evaluated at the true human answer: thelog-loss(negative
log-likelihood the model places on the true answer) and theBrier score(squared error of the predicted distribution
against the one-hot true answer). Lower is better, and both are reported against the baseline’s conditional distribution
on the same rows; a proper score is the right way to ask whether the distribution puts mass where the human actually
answered.
Subgroup determinism (RQ3): does the model treat identity as destiny?Fairness research has long argued that
aggregate performance can hide subgroup harm and must be assessed group by group [ 30, 31]. We adopt that lens
but ask a sharper, human-anchored question: how strongly a demographic attribute (say, political leaning)predicts
the answer, for real people and for the model. The natural measure is the share of the total variation in answers that
is explained by which group a person belongs to. Statisticians call this η2 (“eta-squared”), the ratio of the variation
betweengroups to the total variation (between plus within groups); it runs from 0 (the attribute tells you nothing about
the answer) to 1 (the attribute determines the answer completely). We compute η2 the same way for humans and for the
model. Our headline measure, thestereotyping index, is simply the difference,
∆η2 =η 2 model −η 2 human,
which is positive when the model treats a demographic attribute asmorepredictive of the answer than it actually is
among real people, that is, when the model stereotypes. Because it is a difference of two bounded quantities computed
identically, it is not distorted by which prompt style produced the model’s answers, and it captures the full spread within
each group rather than only the group averages. We attach a 95% confidence interval to each value by resampling
respondents500times (a bootstrap), so we can tell a real effect from sampling noise.
η2 treats the answer codes as numbers, which is natural for the ordinal questions but would be an arbitrary choice
for nominal ones. To guard against the objection that the finding depends on how answers are coded, we add a
coding-invariantcompanion measure that uses no numeric codes at all: Cramér’s V , the standard association strength
between two categorical variables (here, group membership and the chosen answer), computed identically for humans
and for the model from the group×answer contingency table. Its stereotyping analogue is ∆V=V model −V human, again
with a bootstrap 95% CI. Because it is purely nominal, we can report it forallquestions, including the nominal GSS
items that the η2 index omits. If both the numeric ∆η2 and the coding-free ∆V are positive, over-determination is not
an artifact of the answer coding.
Decision impact: what does over-determination cost a decision that acts on it?The stereotyping index measures
the distortion in the model’s world; a decision-support venue needs to know what that distortion does to a decision. We
therefore translate it into the terms of the single most common use of a synthetic user in practice:segment targeting. A
product, marketing, or policy team asks which demographic segment is most extreme on an attitude, and how large the
between-segment gap is, in order to target the top segment, size a niche, or claim “this attitude splits along <segment>.”
For each (question, demographic axis) we compute, identically for the model and for real humans, thesegment share pg
(the fraction of segment g on the high end of the answer scale), and read three quantities a targeting decision keys on:
thebetween-segment gap maxg pg −min g pg; thetarget segment arg maxg pg; and, when the model’s target differs
from the human target, thetargeting cost(the attitude a team forgoes, in real human share, by acting on the model’s
segment instead of the true one). From these we report (i) thegap-inflation factor gapmodel/gaphuman, how much the
model exaggerates the between-segment difference; (ii) thewrong-target rate, the fraction of (question, axis) pairs
where the model would send a team to the wrong segment; and (iii) thespurious-split rate, the fraction where humans
show a negligible gap (≤0.10 ) but the model shows a large one ( ≥0.25 ), a segment split a team would “discover”
and act on that does not exist in real people. Human shares use the full in-scope table; the model gap carries a 95%
bootstrap CI over respondents.
Stability (RQ4): do the conclusions survive irrelevant changes?We report the rate of invalid or refused outputs
(answers the parser cannot read as a valid choice), agreement between two decoding runs, and how results move across
model family, model size, and prompt wording.
3.6 Estimation choices and their robustness
Four choices in the estimation deserve explicit justification, since each is a place a reader might worry the headline
effects are an artifact of the analysis rather than of the models. We resolve each on the data itself and report the checks
in Section 4.5 and Appendix F.
Confidence level.We use 95% intervals throughout. The individual-level deficit (RQ1) and the over-determination effect
(RQ3) are large relative to their uncertainty, so moving from a 90% to a stricter 95% interval leaves every headline
unchanged: on WVS every individual-accuracy margin remains strictly below zero, on GSS every model remains a
7

statistical tie-or-worse against the baseline, and the stereotyping index remains significant for the large majority of
question–group pairs (Table 1).
Multiple comparisons.The stereotyping index is tested over many (question, axis) pairs, so a per-pair interval does not
control the false-discovery rate. We therefore also apply a Benjamini–Hochberg FDR correction at q= 0.05 across all
pairs within a model and prompt style. Because the effects are large, correction barely changes the count of significant
pairs (e.g. Sonnet single-answer: 32/32→32/32 on WVS, 10/12→10/12 on GSS; Appendix F), so “significant for
the majority of pairs” is not an artifact of uncorrected multiplicity.
Respondent clustering.A minority of respondents answer more than one question ( 7.6% on GSS, 1.8% on WVS), so
rows are not fully independent. We recompute the RQ1 margin with aclusterbootstrap that resamples respondents
rather than rows; the 95% intervals are essentially unchanged and every WVS deficit still excludes zero (Appendix F).
Survey weights.GSS and WVS ship official design/population weights ( wtssps, W_WEIGHT). We estimate human
targets unweighted, and justify that choice by recomputing, with and without weights on the full in-scope table, the two
human-side quantities the claims rest on: the population answer distribution (the RQ2 target) and the humanη2 (the RQ3
baseline that the stereotyping index subtracts). Weighting moves the human distribution by a mean Jensen–Shannon
divergence of ≤0.0003 and the human η2 by at most 0.007, both one to three orders of magnitude smaller than the
effects we report (JS gaps of 0.04–0.38; stereotyping indices of +0.05 to +0.7). Weighting therefore cannot account
for either failure, so we report the simpler unweighted analysis and document the check in Appendix F.
4 Results
Table 1 reports the full cross-model, cross-domain results, and Table 2 the RQ1 robustness checks (stronger baselines,
distance-aware and proper scoring). The individual-fidelity result is shown in Figures 1 and 2 (the latter adding
paired-bootstrap confidence intervals on the accuracy margin over the baseline), and the over-determination result in
Figures 3 and 4 (the latter resolving it to the individual-question level).
Table 1: Cross-domain, cross-model results. ∆base = individual accuracy minus the demographic-lookup baseline
(negative = worse than the baseline); paired-bootstrap 95% CIs for this margin are shown per model in Figure 2,
and the stronger baselines, distance-aware, and proper-scoring comparisons in Table 2. JS = mean Jensen–Shannon
divergence (lower is better; population-reweighted values agree, see Section 4.2). ∆η2 = median stereotyping index
(positive = over-determination); “sig” = number of question–group pairs whose 95% CI excludes zero, out of the total
(a coding-invariant Cramér’s V replication is in Section 4.3). Style A=single answer, Style C=distribution.
Domain Model Sty Acc Base∆base JS ∆η2 (sig)
GSS Haiku 4.5 A 0.587 0.589−0.0030.090+0.048(5/8)
GSS Haiku 4.5 C 0.583 0.589−0.0060.011+0.059(9/12)
GSS Sonnet 4.6 A 0.563 0.589−0.0260.082+0.081(10/12)
GSS Sonnet 4.6 C 0.589 0.589−0.0010.017+0.104(9/12)
GSS Llama 8B A 0.496 0.589−0.0930.056+0.026(7/12)
GSS Llama 8B C 0.509 0.586−0.0770.023+0.026(3/7) †
GSS Llama 70B A 0.569 0.589−0.0210.072+0.051(6/8)
GSS Llama 70B C 0.582 0.589−0.0080.016+0.031(5/8)
WVS Haiku 4.5 A 0.170 0.388−0.2180.382+0.087(30/32)
WVS Haiku 4.5 C 0.269 0.404−0.1350.046+0.056(21/24) †
WVS Sonnet 4.6 A 0.236 0.388−0.1520.274+0.107(31/32)
WVS Sonnet 4.6 C 0.277 0.388−0.1110.037+0.103(26/28)
WVS Llama 8B A 0.179 0.388−0.2090.232+0.030(22/32)
WVS Llama 8B C 0.182 0.400−0.2180.130+0.376(1/1) †
WVS Llama 70B A 0.249 0.388−0.1390.293+0.136(31/32)
WVS Llama 70B C 0.267 0.388−0.1210.046+0.054(27/30)
† Style-C cells with elevated invalid rates (Section 4.5); interpret with caution. Llama-8B Style-C on WVS is effectively unusable
(85% invalid,n= 440).
4.1 RQ1: LLMs do not beat, and on values fall well below, any non-LLM baseline
On GSS, the individual accuracy of every model is at or below the demographic lookup baseline ( 0.589). The best
margin any model achieves is −0.001 (Sonnet, Style C), a paired-bootstrap tie (CI [−0.028,0.022] ); Llama-8B is 9
8

points worse (0.496 vs. 0.589, CI [−0.120,−0.067] ). The lookup is not a weak straw man: a learnedlogisticbaseline
reaches 0.622 and a random forest 0.583 (Table 2), so the best LLM also trails the strongest non-LLM predictor. On
WVS the gap is far larger and uniformly negative: under the single-answer prompt every model is13.9 to 21.8 accuracy
points belowthe demographic baseline (e.g. Haiku Style A: 0.170 vs. 0.388), and every model under either prompt is
below the learned baselines as well. On WVS every one of these margins has a 95% CI that lies strictly below zero; on
GSS no margin is positive, with the deficits for Llama-8B (both prompts) and Sonnet’s single-answer prompt clearing
95% significance and the remaining cells statistical ties at or below the baseline. So for predicting an individual’s
response, and especially a cross-cultural value response, a simple demographic predictor beats all four LLMs.
Two robustness checks close the obvious escape routes. First, the deficit is not an artifact of harsh exact-match scoring:
on the ordinal questions the model’sdistance-awareerror is also worse than the baseline’s. On GSS the model’s MAE
is 0.56–0.72 versus 0.54 for the baseline; on WVS’s long scales it is1.83–2.27 versus 1.74 (Table 2). The distributional
EMD, which credits a distribution for placing mass near the truth even when its mode is wrong, tells the same story
(0.76–0.83 vs. 0.73 on GSS; 1.94–2.30 vs. 1.67–2.02 on WVS). Giving partial credit for near-misses does not rescue
the model. Second, scoring thewholeStyle C distribution with proper scoring rules tells the same story: the model
assignslowerprobability to the true human answer than the baseline does. On GSS the model’s log-loss is 0.84–1.03
versus 0.81 for the baseline (Brier 0.52–0.62 vs. 0.50); on WVS 1.76–2.26 versus 1.70 (Brier 0.80–0.89 vs. 0.71). This
directly answers RQ1: synthetic users providenoindividual-level advantage over a demographic baseline under any of
these scorings, and on values they are actively worse.
Figure 1: Individual accuracy vs. the naive demographic baseline (dashed line), GSS (left) and WVS (right). No model
exceeds the baseline on GSS; every model falls well below it on WVS. The individual-level failure (RQ1) holds in both
domains and is more severe for cross-cultural values.
Figure 2: Individual-accuracy margin over the demographic baseline (∆base) with paired-bootstrap 95% confidence
intervals, GSS (left) and WVS (right). Negative means worse than the baseline. Every interval lies below zero except
the two GSS ties, and the WVS deficits are large and tight.
4.2 RQ2: Aggregate distributions are reproduced reasonably, especially under Style C
Reproducing the group’s overall answerspreadis much easier for the models than guessing individuals, and asking
the model directly for a distribution (Style C) does this markedly better than asking for a single answer (Style A).
Recall that the JS divergence runs from 0 (distributions identical to humans’) upward, so smaller is better. On GSS,
9

Table 2: RQ1 robustness: the individual-level deficit survives stronger baselines, distance-aware scoring, and proper
scoring.Top:pooled individual accuracy of the four non-LLM baselines (the best LLM is shown for reference).Bottom:
per-model distance-aware error on ordinal questions and proper scores, each next to the baseline on the same rows (all
lower is better): MAE = mean absolute error of the single-answer prediction; EMD = earth-mover’s distance of the full
predicted distribution (Style C) from the true answer, in scale steps; log-loss and Brier are evaluated on the distribution
prompt at the true answer. Each cell shows model / baseline (m/b) on the same rows. In every cell the model is at best
tied and usually worse than the baseline.
Marginal Dem. lookup Logistic Random forest Best LLM
GSS accuracy 0.568 0.5890.6220.583 0.589
WVS accuracy 0.348 0.3880.3930.366 0.277
MAE EMD log-loss Brier
Domain Model (m/b) (m/b) (m/b) (m/b)
GSS Haiku 4.5 0.57 / 0.54 0.78 / 0.73 0.84 / 0.81 0.52 / 0.50
GSS Sonnet 4.6 0.60 / 0.54 0.78 / 0.73 0.84 / 0.81 0.52 / 0.50
GSS Llama 8B 0.68 / 0.54 0.83 / 0.74 1.03 / 0.80 0.62 / 0.50
GSS Llama 70B 0.59 / 0.54 0.76 / 0.73 0.86 / 0.81 0.53 / 0.50
WVS Haiku 4.5 1.86 / 1.74 1.94 / 1.67 1.76 / 1.70 0.80 / 0.71
WVS Sonnet 4.6 1.84 / 1.74 2.22 / 2.02 1.88 / 1.85 0.81 / 0.74
WVS Llama 8B 2.05 / 1.74 2.30 / 1.87 2.26 / 1.85 0.89 / 0.73
WVS Llama 70B 1.83 / 1.74 2.27 / 2.02 1.94 / 1.85 0.82 / 0.74
Style C reaches 0.011–0.023 (essentially the human distribution), versus 0.056–0.090 for Style A. WVS shows the
same ordering (Style C ≈0.037 –0.046 for the models that produce valid output, versus 0.23–0.38 for Style A). This
confirms, across both domains, the familiar pattern that a model can mimic “the average group” far better than any
individual within it. This aggregate result is not an artifact of the cell-based sampling: reweighting each cell back to its
human population share leaves the JS divergence essentially unchanged (e.g. Haiku GSS Style C 0.0108→0.0109 ;
Sonnet WVS Style C 0.0371→0.0373 ), so the model is being compared against the true population distribution, not
against our sampling design.
4.3 RQ3: LLMs over-determine demographics (stereotyping), not flatten them
A common worry is that LLMsflattengroups, washing out the differences between them. For identity-linked attitudes
we find the opposite. The stereotyping index ispositivefor essentially every model and prompt style in both domains,
and its confidence interval excludes zero for the large majority of question–group combinations (Table 1): models treat
demographics asmoredecisive of the answer than they are among real people. The effect is dramatic for politically-
and identity-linked questions. On GSS, a person’s political views explain about 10% of the real variation in gender-role
attitudes, but in the models they appear to explain 60–69%; for confidence in banks, political views explain only about
1.5% of the real variation yet up to about 67% in the model, roughly a forty-fold exaggeration. On WVS, taking country
as the grouping, nearly all 32 question–country combinations are significantly over-determined for the two Claude
models and the larger Llama. The simulated population is therefore not a blurred copy of the real one; it is acaricature,
in which who you are dictates what you think far more tightly than it does in reality.
This does not depend on how we code the answers. The coding-invariant measure, Cramér’s V , which uses no numeric
codes and treats every answer as an unordered category, tells the same story onallquestions, including the nominal
GSS items the η2 index omits. The median ∆V is positive for both Claude models in both domains (GSS Sonnet
Style A +0.152, Haiku +0.108; WVS Sonnet Style A +0.160, Llama-70B +0.166), and its bootstrap CI excludes zero
for a majority of question–group pairs (e.g. 22 of 40 for Sonnet on GSS, 23 of 32 on WVS). Over-determination is thus
a property of the model’s behavior, not of the numeric coding of the scale.
4.4 Decision impact: over-determination produces wrong and spurious segment decisions
Over-determination is not just a statistical curiosity; it changes what a team would decide. Reading segment structure
off the synthetic users rather than off real humans distorts the targeting decision in three concrete ways (Figure 5). First,
the modelinflates the between-segment gapa decision keys on: for the frontier model (Sonnet, single-answer) the
median gap is 2.3× the true human gap on GSS and 2.5× on WVS, and every model inflates it (medians 1.3–4.1×
on GSS, 2.0–4.7× on WVS). A team sizing a segment difference off synthetic users over-estimates it roughly two
10

Figure 3: Stereotyping index (η2 model −η 2 human) by model and prompt style, GSS (left) and WVS (right); higher means
the model treats demographics as more decisive of the answer than they are among real people. All reliable bars are
positive in both domains: every model over-determines demographics (RQ3), and the larger, more capable models do
not reduce the effect (RQ4). Distribution-prompt bars with high invalid-output rates are omitted and marked “output
unreliable” (see Section 4.5).
Figure 4: Question-level over-determination for the frontier model (Sonnet 4.6, single-answer prompt) with bootstrap
95% CIs, along the primary grouping axis (GSS: political views; WVS: country). Over-determination is not a model-
average artifact: it holds question by question, with confidence intervals well above zero for the strongest items.
to fourfold. Second, the model oftentargets the wrong segment: its arg max segment differs from the true human
arg max for 50% of GSS (question, axis) pairs and 72% of WVS pairs (Sonnet single-answer), so a team choosing
which segment to prioritize would, more often than not on values, pick a segment that is not actually the most extreme.
Third, and most damaging, the modelmanufactures segment splits that do not exist: on WVS, 28% of pairs (Sonnet
single-answer; up to 41% for Haiku and Llama-70B) fall in the spurious-split regime: humans differ across segments
by ≤10 points while the model differs by ≥25 . Concrete cases make the failure vivid. Among U.S. respondents,
confidence in banks barely varies with political leaning (a “great deal” of confidence ranges only 13–24% across the
seven political categories), yet the model treats politics as roughly 67% determinative of the answer; a team reading
the simulation would conclude, wrongly, that trust in banks is sharply polarized. On WVS, attitudes to government
responsibility (Q108) differ across education levels by under 5 points among real people but by 74 points in the model
(16×; CI [0.60,0.86] ), a segment split with no basis in the human data. Because these errors arestructured, always in
the direction of exaggerated group difference, they do not average out across a portfolio of decisions; they systematically
push a team toward over-segmenting a population and over-targeting the segment the model has caricatured.
4.5 RQ4: Capability does not fix it; outputs are unstable to format and prompt surface
Three stability results stand out. First,capability does not remedy either failure. Within the closed family, the
frontier model (Sonnet 4.6) stereotypesmorethan the smaller Haiku 4.5 (median ∆η2 +0.104 vs. +0.059 on GSS
Style C; +0.103 vs. +0.056 on WVS Style C), and does not beat the baseline on individuals. Within the open family,
Llama-70B has the highest stereotyping index on WVS (+0.136). Larger, more capable models are therefore not safer
synthetic users on these axes. Second,format stability is a real failure mode for smaller models. The distribution
prompt (Style C) over long numeric scales produced high invalid-output rates: Llama-8B reached 85% invalid on
WVS (rendering its Style-C numbers unusable, n= 440 ) and 57% on GSS; Haiku reached 40% on WVS. Sonnet and
11

Figure 5: Decision impact of over-determination for the frontier model (Sonnet 4.6, single-answer prompt): the
between-segment gap a targeting decision reads off the model (vertical axis, with 95% bootstrap CI) against the true
human gap (horizontal axis), one point per (question, demographic axis), GSS (left) and WVS (right). The dashed line
is faithful reading (model = human); points above it are gaps the model exaggerates. Shaded: thespurious-splitzone
(human gap ≤0.10 but model gap ≥0.25), the segment differences a team would act on that do not exist in real people.
Almost every point lies above the faithful line.
Llama-70B remained at 0% invalid. This is itself a practical result: a researcher relying on distribution prompts from a
small model may silently lose most of their sample.
The accuracy numbers elsewhere in the paper areconditional on valid output, which flatters the high-invalid cells
because invalid responses may not be missing at random. We therefore report both bounds. Where invalid rates are
near zero (all Claude and Llama-70B cells), the two coincide, so those results are unaffected. Where they are high,
treating each invalid output as a failed prediction, the appropriate accounting when a synthetic user must return a usable
answer, widens the deficit sharply: Llama-8B’s Style-C accuracy falls from 0.51 to 0.22 on GSS and from 0.18 to 0.03
on WVS, and Haiku’s WVS Style-C from 0.27 to 0.16. Because the non-LLM baselines never emit invalid output,
penalizing invalids can only widen the LLM’s gap to the baseline, never close it; the individual-level conclusion is
robust to either accounting.
Third,predictions are unstable to prompt-surface choices that should be irrelevant. Prior work shows that
survey-style LLM answers are sensitive to option ordering and labeling [12] and that prompt architecture and persona
formulation can themselves induce artifacts [19, 20]; we quantify this for our setting. On the two clean closed models
we measured theprediction-flip rate(the fraction of single-answer predictions that change) under two perturbations that
leave the actual question and answer set unchanged: reversing the display order of the answer options, and reframing
the identical demographics as a natural-language persona sentence rather than a bulleted profile. We benchmark these
against a decoding-noise floor: the flip rate between two decoding seeds of thesameprompt. On GSS, merely reversing
option order flips 9.8% (Sonnet) to 10.8% (Haiku) of predictions, and the persona reframing flips a further ∼9% ,
both roughly 4–10× the seed-noise floor (1.1% and 2.6% respectively). An option-order spot-check on WVS shows
the same effect more strongly (14.3% flips for Sonnet, 22.6% for Haiku). Option order also moves aggregate fidelity
(e.g. Haiku GSS accuracy 0.587→0.606 ), so a study’s conclusions can depend on an arbitrary presentation choice.
Together with the capability and format results, this means synthetic-user validity is not only a model property but a
prompt/interface property.
4.6 RQ5: Both failures transfer across domains
The two headline failures (no individual-level advantage over the demographic baseline, and positive stereotyping)
appear inboththe U.S. social-attitude domain and the 63-country values domain, forall fourmodels andbothfamilies.
The individual-level failure is in factstrongerin the cross-cultural domain (an 11–22 point deficit vs. a rough tie). This
12

cross-domain consistency is the basis for treating these as properties of current LLM synthetic-user methods rather than
artifacts of a single survey, model, or prompt.
5 Discussion
The two failures discussed in this paper stem from the same underlying cause: current LLMs, prompted with demo-
graphics, appear to answer by mapping a profile to a stereotyped “typical” response for that profile. This is consistent
with evidence that language models encode social associations [26, 29] and that persona conditioning steers models
toward stereotyped abstractions rather than nuanced individuals [18]. That mapping is too coarse to beat a demographic
lookup at the individual level, and it is worse than the lookup when the answer space is large, as in the 10-point WVS
scales. Yet it is also too tight: it treats demographics as more predictive of attitudes than they truly are. The practical
corollary is that a synthetic-user study can look successful on an aggregate-distribution metric, even one improved
by distribution-specialized training [ 17], while being invalid for any individual- or subgroup-level use, and while
systematically exaggerating the demographic structure of opinion. Because the aggregate metric is the one most often
reported, this is a live risk for the field.
Implications for decision supportThese two failures map directly onto how synthetic users are used to support
decisions. A team that only checks aggregate fidelity, the common practice, can be misled in two ways at once.
Any decision keyed toindividuals or narrow segments(personalizing an offer, sizing a niche, or predicting how a
specific demographic will react) rests on individual-level fidelity the models do not have; a demographic lookup
would serve at least as well and often better, at a fraction of the cost. And any decision that reads thestructureof
opinion off the simulation (“this attitude splits sharply along political lines,” “this segment is monolithic”) inherits the
models’ over-determination, which manufactures group differences that are far larger than they are in real people. Our
decision-impact analysis (Section 4.4) puts numbers on this second failure: on the segment-targeting task the models
inflate between-segment gaps two to fourfold, would send a team to the wrong segment in half of GSS and most WVS
cases, and manufacture a nonexistent segment split in up to 41% of value questions. The danger is not random noise,
which averages out, but thisstructurederror, which propagates into the decision. The framework we propose is meant
to catch exactly this before the evidence is trusted: it turns “did the aggregate look right?” into a set of checks a team
can run against held-out human data to decide, for their specific question, whether synthetic-user evidence is safe.
A validation protocolFrom these results we distill a checklist for researchers considering LLM synthetic users: (1)
report individual-level and aggregate-level fidelityseparately; (2) always benchmark individual fidelity against non-LLM
baselines computed on real held-out data (at least a demographic lookup, ideally a learned demographic model) using
distance-aware or proper-scoring metrics on ordinal scales; an LLM that does not beat them adds no individual-level
information; (3) report subgroup determinism (e.g. ∆η2, or a coding-invariant association measure), not just group
means, to detect stereotyping; (4) before acting on any segment-level read, check the decision-impact quantities (gap
inflation, wrong-target rate, and spurious-split rate) against held-out human data, since a distortion invisible in an
aggregate metric can still flip a targeting decision; (5) report invalid/refusal rates, especially for distribution prompts
and smaller models; (6) do not assume a larger or more capable model is a safer synthetic user; and (7) restrict validity
claims to the population, domain, and level of analysis actually tested.
LimitationsOur claims are scoped to the data we used: GSS respondents 2016–2024 and WVS Wave 7 across 63
countries, on the specific questions listed, with two prompt formats and two seeds, and to demographic prompting under
survey-simulation protocols, not to every elicitation strategy. The LLM-evaluated sample is about 100 respondents per
question, but the individual-fidelity claims pool all rows in a domain (n≈2,000 on GSS, n≈2,900 on WVS) and
every headline comparison carries a paired-bootstrap 95% interval, so the conclusions rest on those intervals rather
than on any single question’s cell. We do not claim these numbers characterize every model, prompt, or elicitation
strategy; richer persona construction [21], few-shot conditioning, or fine-tuning could shift the individual-fidelity and
stereotyping numbers, and testing that is exactly the value of a fixed, reusable protocol. We estimate human targets
without survey weights; because applying the official GSS and WVS weights moves those targets by amounts one
to three orders of magnitude smaller than the effects we report (Appendix F), this choice does not affect any claim.
Older public surveys such as these may appear in model pretraining data; we mitigate this by scoping GSS to recent
waves and by noting that memorization would, if anything,helpaggregate fidelity while leaving the individual-level
and over-determination failures intact. Finally, survey answers are stated opinions, not behavior; extending the protocol
to behavioral tasks and to interactive multi-agent simulations [22, 24] is future work.
13

6 Conclusion
Across two independent domains, four models, and two model families, and under the demographic-prompting protocols
we test, LLM synthetic users show two robust failures: they do not beat, and on cross-cultural values fall well below,
non-LLM baselines at the individual level, and they systematically over-determine demographics, treating identity as
far more predictive of attitudes than it is among real people. The individual-level deficit survives distance-aware and
proper scoring, and the over-determination survives a coding-invariant association measure; model capability does not
fix either failure.
The contribution, however, is not merely the negative result that these systems fail. It is a reusable evaluation framework
for intelligent synthetic-user systems: the cross-domain benchmark, the suite of non-LLM baselines scored with distance-
aware and proper-scoring metrics, the stereotyping index and its coding-invariant companion, and the validation protocol
that ties them together, designed to be run before synthetic-user evidence is deployed in a decision-support workflow.
Rather than trusting an aggregate similarity number, a team can use this framework to determine, for their specific
question, population, and level of analysis, whether an LLM synthetic user is fit for purpose or whether a trivial
demographic predictor would serve at least as well. As LLMs are increasingly wired into product, policy, and market
decisions, that up-front check is what turns a cautionary finding into an actionable safeguard.
A Model call settings
All four models (Claude Haiku 4.5, Claude Sonnet 4.6, Llama-3.1-8B-Instruct, and Llama-3.3-70B-Instruct) are called
through a single common chat-completion interface. Decoding uses temperature 1.0 (the model’s default sampling;
where a model rejects an explicit temperature field it is omitted and the provider default applies) and a token cap of 100.
Each (model, prompt format, respondent, question) cell is generated under two independent runs (“seeds” 0 and 1);
these differ only in sampling randomness and are used to estimate the run-to-run noise floor in RQ4.
B Exact questions and answer scales
Tables 3 and 4 give every question verbatim, with its answer options and integer coding, whether it is treated as ordinal
or nominal, and which metrics it enters. GSS wordings and value labels are the standard GSS codebook text; WVS
wordings and ordinal scales follow WorldValuesBench for comparability. An item is ordinal when a mean answer is
meaningful; only ordinal items enter the η2 stereotyping index and the distance-aware metrics (MAE/EMD), while all
items enter accuracy, JS divergence, and the coding-invariant Cramér’s V (V ). GSS prompt demographics are age, sex,
race, highest degree, region, political views, and party identification (subgroup axes: sex, race, degree, region, political
views); WVS prompt demographics are age group, sex, education level, settlement type, and country (subgroup axes:
country, education, age group, sex).
Table 3: GSS questions: wording, answer options (code=label), type, and metrics
entered. “all”=acc, JS, MAE/EMD, log-loss/Brier,η 2,V.
Var Question wording Options (code=label) Type Metrics
happy Taken all together, how would you say
things are these days – would you say
that you are very happy, pretty happy,
or not too happy?
1=very happy; 2=pretty
happy; 3=not too happy
ordinal all
trust Generally speaking, would you say
that most people can be trusted or that
you can’t be too careful in dealing
with people?
1=most people can be trusted;
2=can’t be too careful; 3=de-
pends
nominal acc, JS,V
fair Do you think most people would try
to take advantage of you if they got a
chance, or would they try to be fair?
1=would take advantage of
you; 2=would try to be fair;
3=depends
nominal acc, JS,V
helpful Would you say that most of the time
people try to be helpful, or that they
are mostly just looking out for them-
selves?
1=try to be helpful; 2=look-
ing out for themselves; 3=de-
pends
nominal acc, JS,V
cappun Do you favor or oppose the death
penalty for persons convicted of mur-
der?
1=favor; 2=oppose nominal acc, JS,V
14

Table 3 continued
Var Question wording Options (code=label) Type Metrics
grass Do you think the use of marijuana
should be made legal or not?
1=should be legal; 2=should
not be legal
nominal acc, JS,V
abany Please tell me whether or not you
think it should be possible for a preg-
nant woman to obtain a legal abortion
if the woman wants it for any reason.
1=yes; 2=no nominal acc, JS,V
gunlaw Would you favor or oppose a law
which would require a person to obtain
a police permit before he or she could
buy a gun?
1=favor; 2=oppose nominal acc, JS,V
fefam Do you agree or disagree with this
statement: It is much better for every-
one involved if the man is the achiever
outside the home and the woman takes
care of the home and family?
1=strongly agree; 2=agree;
3=disagree; 4=strongly dis-
agree
ordinal all
confinan How much confidence do you have in
the people running banks and financial
institutions – a great deal, only some,
or hardly any?
1=a great deal; 2=only some;
3=hardly any
ordinal all
Table 4: WVS questions (WorldValuesBench probe set): wording, scale, type, and
metrics entered. All are ordinal integer scales.
Var Question wording Scale Type Metrics
Q48 On a scale of 1 to 10, 1 meaning ‘None at all’ and 10 meaning ‘A great deal’,
how much freedom of choice and control over your life do you feel you have?
1–10 ord. all
Q106 On a scale of 1 to 10, 1 meaning ‘Incomes should be made more equal’ and
10 meaning ‘There should be greater incentives for individual effort’, where
would you place your view?
1–10 ord. all
Q107 On a scale of 1 to 10, 1 meaning ‘Private ownership of business should be
increased’ and 10 meaning ‘Government ownership of business should be
increased’, where would you place your view?
1–10 ord. all
Q108 On a scale of 1 to 10, 1 meaning ‘The government should take more responsi-
bility to ensure that everyone is provided for’ and 10 meaning ‘People should
take more responsibility to provide for themselves’, where would you place
your view?
1–10 ord. all
Q112 On a scale of 1 to 10, 1 meaning ‘No corruption at all’ and 10 meaning ‘Abun-
dant corruption’, how much corruption do you think there is in your country?
1–10 ord. all
Q113 On a scale of 1 to 4, 1 meaning ‘None of them’ and 4 meaning ‘All of them’,
how many state authorities do you think are involved in corruption?
1–4 ord. all
Q114 On a scale of 1 to 4, 1 meaning ‘None of them’ and 4 meaning ‘All of them’,
how many business executives do you think are involved in corruption?
1–4 ord. all
Q121 On a scale of 1 to 5, 1 meaning ‘Very bad’ and 5 meaning ‘Very good’, what
impact do you think immigrants have on the development of your country?
1–5 ord. all
Q122 On a scale of 0 to 2, 0 meaning ‘Disagree’ and 2 meaning ‘Agree’, do you
agree that immigration fills useful jobs in the labour market?
0–2 ord. all
Q123 On a scale of 0 to 2, 0 meaning ‘Disagree’ and 2 meaning ‘Agree’, do you
agree that immigration increases the crime rate?
0–2 ord. all
Q158 On a scale of 1 to 10, 1 meaning ‘Completely disagree’ and 10 meaning
‘Completely agree’, how much do you agree that science and technology
make our lives healthier, easier, and more comfortable?
1–10 ord. all
Q159 On a scale of 1 to 10, 1 meaning ‘Completely disagree’ and 10 meaning
‘Completely agree’, how much do you agree that because of science and
technology there will be more opportunities for the next generation?
1–10 ord. all
Q160 On a scale of 1 to 10, 1 meaning ‘Completely disagree’ and 10 meaning
‘Completely agree’, how much do you agree that we depend too much on
science and not enough on faith?
1–10 ord. all
Q164 On a scale of 1 to 10, 1 meaning ‘Not at all important’ and 10 meaning ‘Very
important’, how important is God in your life?
1–10 ord. all
15

Table 4 continued
Var Question wording Scale Type Metrics
Q177 On a scale of 1 to 10, 1 meaning ‘Never justifiable’ and 10 meaning ‘Always
justifiable’, how justifiable do you think it is to claim government benefits to
which you are not entitled?
1–10 ord. all
Q178 On a scale of 1 to 10, 1 meaning ‘Never justifiable’ and 10 meaning ‘Always
justifiable’, how justifiable do you think it is to avoid paying a fare on public
transport?
1–10 ord. all
Here “all” denotes accuracy, JS, MAE/EMD, log-loss/Brier,η 2, andV, since every WVS item is ordinal.
C Prompt templates and demographic formatting
Demographics are rendered as a bulleted profile, one line per attribute, using human-readable value labels (e.g. “ -
Political views (liberal–conservative): conservative ”); for the persona perturbation (RQ4) the same
attributes are rewritten as a single natural-language sentence (“a person with . . .”). The two prompt formats share this
demographic block and differ only in the response instruction:
Single-answer prompt (Style A).
You are simulating a single {respondent noun} with the following demographic
profile:
{demographics}
Based only on this profile, predict how this specific person would answer the
following survey question.
Question:
{question text}
Answer options:
{options}
Respond with only the single {option letter|number} (e.g. A). No explanation.
Distribution prompt (Style C).
Consider a {respondent noun} with the following demographic profile:
{demographics}
Estimate the probability that this respondent would choose each answer option for
the question below. Probabilities must sum to 1.
Question:
{question text}
Answer options:
{options}
Return only valid JSON mapping each answer {key} to a probability, using exactly
these keys: {keys}. No other text.
Answer options use short letters (A, B, . . . ) when the options have text labels (GSS), and the scale number itself when
options are numeric points on an ordinal scale (WVS), which avoids the eight-letter limit on the longest scales. In every
case the prompt carries an explicit key→answer-code mapping that the parser uses to recover the underlying code.
D Parser rules and invalid-output handling
Outputs are parsed deterministically. For the single-answer prompt with letter keys, the parser takes the first standalone
capital letter that is a valid option key; with numeric keys it takes the first integer token that is a valid key, matching
multi-digit tokens so that “10” is not read as “1”. For the distribution prompt, the parser extracts the first balanced
JSON object, reads a probability for each declared key (absent keys default to 0), and normalizes to sum to one; any
response that is empty, contains no valid key, fails JSON parsing, or yields a non-positive total is flaggedinvalid/refused.
Invalid outputs are excluded from the accuracy and distribution metrics (a conditional-on-valid accounting) and counted
in the invalid-rate stability metric (RQ4). Because invalids may not be missing at random, Section 4.5 also reports the
opposite bound (each invalid counted as a failed prediction), and the two accountings coincide wherever the invalid rate
is near zero. Prose-wrapped answers are tolerated as long as a valid key is recoverable.
16

E Baseline construction and back-off
All baselines are fit on the 50% “fit” fold (respondents with an even hash of their id) and evaluated on the evaluation-
sample rows, which are drawn from the “eval” fold, so no respondent is used for both. Thequestion-marginalbaseline
predicts the single most frequent fit-fold answer for the question. Thedemographic-lookupbaseline estimates a
conditional answer distribution for each demographic cell and predicts its mode, backing off when a cell has fewer
than 20 fit-fold respondents: for GSS the back-off is {degree, race, sex, political views} → {degree, race} → question
marginal; for WVS it is {country, education, age group}→ {country} → question marginal, and we report the {country}
level separately as a country-only baseline. Thelogisticbaseline is a multinomial logistic regression on the one-hot-
encoded prompt demographics, fit per question (≤2000 iterations); therandom-forestbaseline uses 300 trees on the
same features. The lookup and logistic baselines also emit a full predicted distribution, used as the reference for the
log-loss and Brier comparisons.
F Estimation robustness
This appendix records the four estimation checks summarized in Section 3.6; all are computed on the same cached
outputs as the main results, with no additional model calls.
Multiple comparisons (FDR).For each (question, axis) pair entering the η2 stereotyping index we compute a one-sided
bootstrap p-value for H0 : ∆η2 ≤0 and apply a Benjamini–Hochberg correction at q= 0.05 across all pairs within a
model and prompt style. The number of significant, positively-signed pairs is nearly identical before and after correction,
because the effects are large: for the single-answer prompt, Sonnet is 32/32 (WVS) and 10/12 (GSS) both before
and after correction; Haiku 31/32→31/32 (WVS); Llama-70B 31/32→31/32 (WVS) and 7/8→7/8 (GSS).
Over-determination is therefore not an artifact of uncorrected multiple testing.
Respondent-clustered bootstrap.The individual-fidelity sample contains a small share of respondents who answer
more than one question ( 7.6% on GSS, 1.8% on WVS). Recomputing the RQ1 accuracy margin over the baseline
with a cluster bootstrap (resampling respondents, then taking all of their rows) leaves the 95% intervals essentially
unchanged from the row-level intervals: on WVS every margin still excludes zero (e.g. Sonnet single-answer−0.152,
[−0.180,−0.121] ; Haiku −0.218, [−0.248,−0.187] ), and on GSS the Llama-8B deficits remain significant while the
Claude cells remain ties, exactly as in the row-level analysis. Within-respondent correlation does not drive the result.
Survey-weight robustness.GSS and WVS provide official weights ( wtssps, coverage 100%; W_WEIGHT, coverage
100% on the in-scope pool). Applying them to the two human-side quantities the claims depend on changes them
negligibly: the human population answer distribution moves by a mean Jensen–Shannon divergence of 0.0001 (GSS)
and <0.0001 (WVS), with a maximum over questions of 0.0003; the human η2 that the stereotyping index subtracts
moves by a mean absolute 0.0016 (GSS) and 0.0012 (WVS), with a maximum of 0.0065. These are one to three orders
of magnitude below the effects we report, so the unweighted analysis is adequate for every claim in the paper.
Sample adequacy.Individual-fidelity margins pool all evaluation rows per domain ( n= 1,986 scored (respondent,
question) pairs on GSS, n= 2,916 on WVS for the clean cells) rather than the≈100 respondents of any single question,
and every headline comparison carries a paired-bootstrap 95% interval computed on those rows; the intervals, not a
nominal per-question count, are what license the claims.
References
[1] Marko Sarstedt, Susanne J Adler, Lea Rau, and Bernd Schmitt. Using large language models to generate silicon
samples in consumer and marketing research: Challenges, opportunities, and guidelines.Psychology & Marketing,
41(6):1254–1270, 2024.
[2] Peiyao Li, Noah Castelo, Zsolt Katona, and Miklos Sarvary. Frontiers: Determining the validity of large language
models for automated perceptual analysis.Marketing Science, 43(2):254–266, 2024.
[3] Galit Shmueli and Otto R Koppius. Predictive analytics in information systems research1.MIS quarterly, 35(3):
553–572, 2011.
[4] Robert M O’Keefe and Daniel E O’Leary. Expert system verification and validation: a survey and tutorial.
Artificial intelligence review, 7(1):3–42, 1993.
[5] Lisa P Argyle, Ethan C Busby, Nancy Fulda, Joshua R Gubler, Christopher Rytting, and David Wingate. Out of
one, many: Using language models to simulate human samples.Political Analysis, 31(3):337–351, 2023.
[6] James Bisbee, Joshua D Clinton, Cassy Dorff, Brenton Kenkel, and Jennifer M Larson. Synthetic replacements
for human survey data? the perils of large language models.Political Analysis, 32(4):401–416, 2024.
17

[7] Yuan Gao, Dokyun Lee, Gordon Burtch, and Sina Fazelpour. Take caution in using llms as human surrogates.
Proceedings of the National Academy of Sciences, 122(24):e2501660122, 2025.
[8] Gati V Aher, Rosa I Arriaga, and Adam Tauman Kalai. Using large language models to simulate multiple humans
and replicate human subject studies. InInternational conference on machine learning, pages 337–371. PMLR,
2023.
[9] John J Horton, Apostolos Filippas, and Benjamin S Manning. Large language models as simulated economic
agents: What can we learn from homo silicus? Technical report, National Bureau of Economic Research, 2023.
[10] Perttu Hämäläinen, Mikke Tavast, and Anton Kunnari. Evaluating large language models in generating synthetic
hci research data: a case study. InProceedings of the 2023 CHI conference on human factors in computing
systems, pages 1–19, 2023.
[11] Shibani Santurkar, Esin Durmus, Faisal Ladhak, Cinoo Lee, Percy Liang, and Tatsunori Hashimoto. Whose
opinions do language models reflect? InInternational conference on machine learning, pages 29971–30004.
PMLR, 2023.
[12] Ricardo Dominguez-Olmedo, Moritz Hardt, and Celestine Mendler-Dünner. Questioning the survey responses of
large language models.Advances in Neural Information Processing Systems, 37:45850–45878, 2024.
[13] Danica Dillion, Niket Tandon, Yuling Gu, and Kurt Gray. Can ai language models replace human participants?
Trends in Cognitive Sciences, 27(7):597–600, 2023.
[14] Zhicheng Lin. Six fallacies in substituting large language models for human participants.Advances in Methods
and Practices in Psychological Science, 8(3):25152459251357566, 2025.
[15] Wenlong Zhao, Debanjan Mondal, Niket Tandon, Danica Dillion, Kurt Gray, and Yuling Gu. Worldvaluesbench:
A large-scale benchmark dataset for multi-cultural value awareness of language models. InProceedings of
the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation
(LREC-COLING 2024), pages 17696–17706, 2024.
[16] Jia Wang, Ziyu Zhao, Tingjuntao Ni, and Zhongyu Wei. Sociobench: Modeling human behavior in sociological
surveys with large language models. InProceedings of the 2025 Conference on Empirical Methods in Natural
Language Processing, pages 26268–26300, 2025.
[17] Yong Cao, Haijiang Liu, Arnav Arora, Isabelle Augenstein, Paul Röttger, and Daniel Hershcovich. Specializing
large language models to simulate survey response distributions for global populations. InProceedings of the 2025
Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human
Language Technologies (Volume 1: Long Papers), pages 3141–3154, 2025.
[18] Ameet Deshpande, Vishvak Murahari, Tanmay Rajpurohit, Ashwin Kalyan, and Karthik Narasimhan. Toxicity
in chatgpt: Analyzing persona-assigned language models. InFindings of the association for computational
linguistics: EMNLP 2023, pages 1236–1270, 2023.
[19] Melanie Brucks and Olivier Toubia. Prompt architecture induces methodological artifacts in large language
models.PloS one, 20(4):e0319159, 2025.
[20] Marlene Lutz, Indira Sen, Georg Ahnert, Elisa Rogers, and Markus Strohmaier. The prompt makes the person
(a): A systematic evaluation of sociodemographic persona prompting for large language models.arXiv preprint
arXiv:2507.16076, 2025.
[21] Leon Li, Haozhe Chen, Hongseok Namkoong, and Tianyi Peng. Llm generated persona is a promise with a catch.
Advances in Neural Information Processing Systems, 38, 2026.
[22] Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and Michael S Bernstein.
Generative agents: Interactive simulacra of human behavior. InProceedings of the 36th annual acm symposium
on user interface software and technology, pages 1–22, 2023.
[23] Joon Sung Park, Lindsay Popowski, Carrie Cai, Meredith Ringel Morris, Percy Liang, and Michael S Bernstein.
Social simulacra: Creating populated prototypes for social computing systems. InProceedings of the 35th annual
ACM symposium on user interface software and technology, pages 1–18, 2022.
[24] Xinyi Mou, Xuanwen Ding, Qi He, Liang Wang, Jingcong Liang, Xinnong Zhang, Libo Sun, Jiayu Lin, Jie
Zhou, Huang Xuanjing, et al. From individual to society: A survey on social simulation driven by large language
model-based agents.ACM Computing Surveys, 58(11):1–41, 2026.
[25] Caleb Ziems, William Held, Omar Shaikh, Jiaao Chen, Zhehao Zhang, and Diyi Yang. Can large language models
transform computational social science?Computational Linguistics, 50(1):237–291, 2024.
[26] Aylin Caliskan, Joanna J Bryson, and Arvind Narayanan. Semantics derived automatically from language corpora
contain human-like biases.Science, 356(6334):183–186, 2017.
18

[27] Tolga Bolukbasi, Kai-Wei Chang, James Y Zou, Venkatesh Saligrama, and Adam T Kalai. Man is to computer
programmer as woman is to homemaker? debiasing word embeddings.Advances in neural information processing
systems, 29, 2016.
[28] Emily Sheng, Kai-Wei Chang, Prem Natarajan, and Nanyun Peng. The woman worked as a babysitter: On
biases in language generation. InProceedings of the 2019 conference on empirical methods in natural language
processing and the 9th international joint conference on natural language processing (EMNLP-IJCNLP), pages
3407–3412, 2019.
[29] Emily M Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell. On the dangers of
stochastic parrots: Can language models be too big? InProceedings of the 2021 ACM conference on fairness,
accountability, and transparency, pages 610–623, 2021.
[30] Joy Buolamwini and Timnit Gebru. Gender shades: Intersectional accuracy disparities in commercial gender
classification. InConference on fairness, accountability and transparency, pages 77–91. PMLR, 2018.
[31] Moritz Hardt, Eric Price, and Nati Srebro. Equality of opportunity in supervised learning.Advances in neural
information processing systems, 29, 2016.
[32] Alicia Parrish, Angelica Chen, Nikita Nangia, Vishakh Padmakumar, Jason Phang, Jana Thompson, Phu Mon
Htut, and Samuel R Bowman. Bbq: A hand-built bias benchmark for question answering. InFindings of the
Association for Computational Linguistics: ACL 2022, pages 2086–2105, 2022.
[33] Andrew D Selbst, Danah Boyd, Sorelle A Friedler, Suresh Venkatasubramanian, and Janet Vertesi. Fairness
and abstraction in sociotechnical systems. InProceedings of the conference on fairness, accountability, and
transparency, pages 59–68, 2019.
[34] David Arnott and Graham Pervan. A critical analysis of decision support systems research.Journal of information
technology, 20(2):67–87, 2005.
[35] Aurora Saibene, Michela Assale, and Marta Giltri. Expert systems: Definitions, advantages and issues in medical
field applications.Expert Systems with Applications, 177:114900, 2021.
[36] Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang,
Deepak Narayanan, Yuhuai Wu, Ananya Kumar, et al. Holistic evaluation of language models.Transactions on
Machine Learning Research, 2023, 2023.
[37] Marco Tulio Ribeiro, Tongshuang Wu, Carlos Guestrin, and Sameer Singh. Beyond accuracy: Behavioral testing
of nlp models with checklist. InProceedings of the 58th annual meeting of the association for computational
linguistics, pages 4902–4912, 2020.
[38] Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao, Abu Awal Md Shoeb, Abubakar Abid, Adam Fisch, Adam R
Brown, Adam Santoro, Aditya Gupta, Adrià Garriga-Alonso, et al. Beyond the imitation game: Quantifying and
extrapolating the capabilities of language models.Transactions on machine learning research, 2023.
[39] Margaret Mitchell, Simone Wu, Andrew Zaldivar, Parker Barnes, Lucy Vasserman, Ben Hutchinson, Elena Spitzer,
Inioluwa Deborah Raji, and Timnit Gebru. Model cards for model reporting. InProceedings of the conference on
fairness, accountability, and transparency, pages 220–229, 2019.
[40] Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna Wallach, Hal Daumé Iii,
and Kate Crawford. Datasheets for datasets.Communications of the ACM, 64(12):86–92, 2021.
[41] Robert M Groves and Lars Lyberg. Total survey error: Past, present, and future.Public opinion quarterly, 74(5):
849–879, 2010.
19
