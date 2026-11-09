---
title: 'Synthetic Personalities: How Well Can LLMs Mimic Individual Respondents Using Socio-Economic Microdata?'
url: https://arxiv.org/abs/2606.04592
category: digital-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Leonard Kinzinger
- Jochen Hartmann
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.04592
pages: 41
chars: 80148
fetched_at: '2026-11-08T13:06:02+00:00'
kb_version: 1
---

# Synthetic Personalities: How Well Can LLMs Mimic Individual Respondents Using Socio-Economic Microdata?

Synthetic Personalities: How Well Can LLMs Mimic Individual
Respondents Using Socio-Economic Microdata?
Leonard Kinzingera,∗, Jochen Hartmanna
aTUM School of Management, Technical University of Munich, 80333 Munich, Germany
Abstract
LLM-based digital twins promise to scale and accelerate market research, but most published twins
are either coarse persona bots conditioned on a few demographic questions or detailed individual-
level twins built on purpose-collected surveys and interview transcripts. Neither setup speaks to
the operationally most relevant case for marketing practice: building detailed individual twins
from the pre-existing heterogeneous panel data that firms already accumulate through CRM sys-
tems, loyalty programs, and repeat surveys. We construct detailed individual-level twins from the
German Socio-Economic Panel (SOEP) and evaluate them across a 3×5×2×2 construction-
method grid that covers three open-weights LLMs, five cumulative information depths ranked by
normalized Shannon entropy, two embedding methods, and two reasoning modes, scoring over
2.1 million twin responses on 500 participants and 183 held-out questions. Twin quality rises
with information depth but with diminishing returns past the 75 percent entropy quartile, which
acts as a cost-efficient Pareto point relative to the best-performing 100 percent cells. Switching
the embedding from a narrative persona summary to a raw dialog history of past responses raises
hold-out accuracy in every model-by-reasoning cell at the 100 percent depth, while an explicit
thinking mode raises rank-order correlation without moving accuracy. Best-cell accuracy reaches
78.8 percent and Fisher-zcorrelation reachesr=0.590 on the SOEP held-out evaluation set. The
findings suggest that twin-based market research is no longer gated by data design, but by item
∗Corresponding author
Email address:leonard.kinzinger@tum.de(Leonard Kinzinger)
arXiv:2606.04592v1  [cs.CY]  3 Jun 2026

volume, model selection, and a small set of construction-level decisions that this paper now maps.
Keywords:Large Language Models, Digital Twins, Synthetic Respondents, Survey Microdata,
Market Research
2

1. Introduction
Traditional market research, including large-sample surveys, conjoint experiments, and in-depth
interviews, is invaluable for understanding consumers. But it is also slow, expensive, and es-
pecially difficult for hard-to-reach respondents such as low-incidence demographics and senior
decision-makers (Arora et al., 2025). Large language models (LLMs) as synthetic respondents
promise a step change in cost and speed. Marketing research has shown that LLMs can estimate
within-category willingness-to-pay after fine-tuning on category data (Brand et al., 2023), repro-
duce brand-perception maps that align with revealed-preference data (P. Li et al., 2024), recover
individual-level time preferences (Goli & Singh, 2024), cut the survey data needed for conjoint
estimation by 25 to 80 percent (M. Wang et al., 2026), and calibrate LLM-generated samples to
reduce their distributional disparity from human responses (Leng et al., 2024). Commercial ven-
dors such as simile.ai are forming around these capabilities and now sell on-demand synthetic
respondent panels.1
The synthetic-respondent literature has organized itself around two granularities. Coarse repre-
sentations condition an LLM on a handful of demographic attributes and represent a segment of
people in aggregate (Argyle et al., 2023; Brand et al., 2023; Goli & Singh, 2024; P. Li et al., 2024;
Santurkar et al., 2023; M. Wang et al., 2026). Detailed individual representations, in contrast, con-
dition the model on rich individual-level data and represent one specific real person (J. S. Park et al.,
2026; Peng et al., 2025; Toubia et al., 2025). The latter is strictly more flexible because individual-
level twins can be aggregated post hoc to any segment a researcher cares to define, while coarse
persona bots cannot be decomposed back to individuals. Academic work in the detailed paradigm
has, however, so far been built almost exclusively on datasets collected for the purpose of creat-
ing digital twins. Toubia et al. (2025) build the Twin-2K-500 dataset as a four-wave instrument
1simile.ai closed a USD 100 million funding round in February 2026 to help firms
predict human behavior at scale (see https://www.bloomberg.com/news/articles/2026-02-12/
ai-startup-nabs-100-million-to-help-firms-predict-human-behavio), an indication that synthetic respondents are
moving from research curiosity to a market-relevant product.
3

designed end-to-end for twin construction with more than 500 items per respondent. J. S. Park
et al. (2026) run two-hour AI-conducted semi-structured interviews per respondent. Binz et al.
(2025) and Binz et al. (2026) curate the Psych-101 and Psych-201 trial-by-trial behavioral bat-
teries across more than 60,000 participants and use them to fine-tune and benchmark the Centaur
family of cognition models. This is not the data shape firms hold. Enterprise CRM systems, loyalty
databases, and repeat-survey programs accumulate heterogeneous item banks over years without
a twin-oriented design, with uneven information density per item. Less is known about whether
useful individual-level twins can be built from the kind of panel data that already sits on a firm’s
disk.
A second open question concerns construction methodology: while embedding method, reasoning
mode, and information depth have each been examined anecdotally (J. S. Park et al., 2026; Peng
et al., 2025; Toubia et al., 2025), no study to our knowledge has compared them systematically on
a shared dataset and a shared evaluation set.
We address both gaps. We construct individual-level digital twins from the German Socio-Economic
Panel (SOEP), a 41-year longitudinal panel that interviewed more than 28,000 respondents in 2023
and exposes more than 900 individual-level question-answer pairs per respondent in the 2023 wave
alone (Goebel et al., 2019; Socio-Economic Panel, 2025). The SOEP serves as an academic ana-
logue of the heterogeneous panel data that firms accumulate through CRM systems, loyalty pro-
grams, and repeat surveys. We then evaluate twins across the full 3×5×2×2 construction-method
grid (three open-weights LLMs, five cumulative information depths ranked by normalized Shan-
non entropy, two embedding methods, two reasoning modes), scoring over 2.1 million individual
twin responses on 500 participants and 183 held-out questions against ground truth, using the ac-
curacy, rank-order correlation, and dispersion-ratio framework established by Peng et al. (2025),
Toubia et al. (2025), and J. S. Park et al. (2026). Intuitively, accuracy measures how close each
twin’s answer sits to its human counterpart’s answer on the question’s natural scale (1 for a perfect
match, 0 for the maximum possible miss; for example, a twin who answers 6 to a human’s 5 on
4

a 1-to-7 scale scores 0.833), while rank-order correlation measures whether the twins reproduce
who scores higher than whom across participants on each question, i.e., the individual-level het-
erogeneity that humans display (Peng et al., 2025). We use open-weights models because they
are reproducible end-to-end and remain deployable in license-bound or regulated settings where
third-party APIs cannot be used.
Several patterns emerge from the construction-method grid. Accuracy and rank-order correlation
both rise monotonically with information depth on a concave curve: the 75 percent quartile of
entropy-ranked items captures the bulk of the available signal at a moderate prompt-token cost,
while the 100 percent quartile attains the best cells at substantially higher cost. Switching the
embedding from a narrative persona summary to a raw dialog history of past survey responses
raises accuracy at the 100 percent depth for every one of the three models, in both reasoning
modes, while an explicit thinking mode raises rank-order correlation without moving accuracy.
Across the three open-weights models, Qwen 3 (Qwen Team, 2025) leads on average across all
three metrics, with Gemma 4 (Gemma Team, Google DeepMind, 2025) attaining the single best
accuracy cell at 78.8 percent and Qwen 3 the highest rank-order correlation (r=0.590), both in
the dialog-thinking-100-percent cell. On the SOEP held-out evaluation set, these levels sit at the
same order of magnitude as the leading published twins built on purpose-collected data (J. S. Park
et al., 2026; Peng et al., 2025; Toubia et al., 2025).
Our contribution centers on demonstrating that individual-level twins can be built from pre-existing
heterogeneous panel data of the kind firms already accumulate, opening the digital twin program
beyond the bespoke surveys and interview protocols used to date. The construction-method grid
we deliver on a shared dataset and a shared evaluation set identifies which choice drives which
metric and at what cost, and locates a clear Pareto point at the 75 percent entropy quartile with the
maximum at 100 percent, giving practitioners an actionable rule for context budgeting.
5

2. Background and Related Literature
Our paper draws on three lines of work: LLMs as synthetic survey respondents in marketing,
individual-level digital twins built from rich human data, and the diagnostic literature on their
failure modes.
2.1. LLMs as Synthetic Survey Respondents in Marketing
Marketing research has shown that LLMs can act as synthetic respondents on several aggregate
tasks, and the discipline has been framing this opportunity since at least Peres et al. (2023) and
Arora et al. (2025). Yoo et al. (2025) extend this framing into a field guide that replicates 35
consumer-research articles across all six research stages on ChatGPT-4o. Brand et al. (2023)
show that off-the-shelf GPT estimates of willingness-to-pay are often inaccurate or wrong-signed,
while fine-tuning on category-specific human conjoint data recovers the sign and rough magnitude
of within-category attribute valuations. P. Li et al. (2024) validate off-the-shelf GPT-4 brand-
perception maps against human surveys and revealed-preference car-trade-in data, reaching over
75 percent agreement on car-brand similarity ratings. Both papers report a clear ceiling on de-
mographic heterogeneity: Brand et al. find that GPT cannot meaningfully reflect heterogeneous
preferencesacross demographic groups, and Li et al. find that while LLM-generated brandper-
ceptionsare largely invariant across demographics (mirroring human data), brandpreferencescan
be aligned only when the prompt is explicitly conditioned on individual attributes. M. Wang et
al. (2026) pool LLM-generated and real choice data in a transfer-learning estimator with proved
asymptotic consistency and recover efficiency gains of 25 to 80 percent on two conjoint studies.
Goli and Singh (2024) extend LLM-based prediction to individual-level time preferences. Leng et
al. (2024) propose an optimal sample-calibration scheme that reweights LLM-generated responses
to reduce their distributional disparity from human samples. Adjacent work uses LLMs for feature
extraction in high-stakes hiring contexts (Chakraborty et al., 2025).
6

Response stability across this work is uneven. Sarstedt et al. (2024) document substantial drift
across model versions and prompt forms, and Brucks and Toubia (2025) show in 5,760 GPT-4
factorial-experiment responses a 63 percent first-position selection rate and a 74 percent rate of
choosing B over C under letter labels, with the first-position bias falling to 54 percent when the
same options carry symbol rather than letter labels. Toubia et al. (2025) reframe the question
by benchmarking twin responses against the underlying human two-week test-retest accuracy on
Twin-2K-500, positioning the human self-consistency ceiling as the natural reference point for
twin stability rather than absolute accuracy. Industry benchmarks point in the same direction, with
LLM accuracy degrading as the target segment narrows (Stromberg et al., 2025).
2.2. Two Paradigms of Synthetic Respondents
Synthetic-respondent work has organized itself around two granularities, which we termcoarse
representationsanddetailed individual representations. Coarse representations condition on a few
demographics (age, gender, race, party) and are most often used to represent a segment of people
(Aher et al., 2023; Argyle et al., 2023; Santurkar et al., 2023; Sarstedt et al., 2024). Its output is
by construction an aggregation, and it is evaluated against aggregate human distributions: opinion-
distribution match (Santurkar et al., 2023; Suh et al., 2025), mean treatment-effect replication
(Aher et al., 2023; Hewitt et al., 2024), and between-group distributional fidelity (Boelaert et
al., 2025). Detailed individual representations condition an LLM on rich individual-level data
and represent one specific real person (J. S. Park et al., 2026; Toubia et al., 2025). The unit of
analysis is finer than a segment, and the same twins can be aggregated, post hoc, to any segment
the researcher cares to define and to alternative segment definitions in parallel. The aggregation
direction is asymmetric: persona bots cannot be decomposed into individuals, but twins can be
summed up to any segment a researcher constructs. Evaluation therefore operates at both levels.
At the individual level, the standard metrics are accuracy and rank-order correlation (J. S. Park et
al., 2026; Peng et al., 2025; Toubia et al., 2025), together with the variance ratio of twin-to-human
response dispersion (Peng et al., 2025), each measured per question across respondents; at the
7

population level, twins inherit the persona-bot metrics above. Anthis et al. (2025) and Kozlowski
and Evans (2025) give higher-level framings of this space. We use the termdigital twinin the
narrow individual sense throughout.
2.3. Building Individual-Level Twins
A digital twin is built from the real responses of one individual, and its task is to answer new
questions as that person would. Inputs vary along several dimensions: the type of question (closed-
scale, free-form, behavioral task), the response modality (typed survey, conversation transcript,
voice file), the level of detail (a handful of demographics versus hundreds of items per person),
and the topics covered. No input set ever fully captures a person, meaning every digital twin is
by design a lossy representation. The goal of a digital twin is not to represent a human to 100%,
but to be close enough that their outputs are realistic (reproducing the human’s specific knowledge,
opinions, and characteristic gaps, including bounded-rationality patterns documented in behavioral
economics) to be useful. This means that the behavior is such that it could have been observed by
a similar person, and that digital twins and real humans are close enough that they share similar
aggregated metrics.
Published twins differ mainly in the type of input data and how it is fed to the model. J. S.
Park et al. (2026) use two-hour AI-conducted semi-structured interview transcripts (about 6,500
words per person), injected directly into the prompt, for a representative US sample of 1,052
respondents. J. S. Park et al. (2026) normalize their accuracy by each participant’s two-week test-
retest consistency: the agent’s prediction accuracy is divided by the participant’s own replication
accuracy on the same items, so a normalized accuracy of 1.0 corresponds to the agent matching
the participant’s own self-consistency two weeks later. They report normalized accuracy of 0.83
(interview-only) and 0.86 (interview-plus-survey) on the General Social Survey, against 0.74 for a
demographics-only baseline, 0.80 on the Big Five inventory, and 0.66 on economic games. Toubia
et al. (2025) take the structured-survey route with the Twin-2K-500 dataset: a four-wave survey
8

of 2,058 US respondents covering 14 demographic items, 19 personality tests (279 questions, 26
constructs), 11 cognitive measures (85 questions), 10 economic-preference tests (34 questions), 21
behavioral-economics paradigms (48 questions), and a 40-question pricing study, with individual-
level accuracy near 0.72 absolute and 0.88 normalized against participant test-retest. Both lines of
work require data collected for the purpose of twin-building.
A parallel research stream fine-tunes models on large collections of human response data rather
than feeding individual histories at prompt time (Kolluri et al., 2025; Orlikowski et al., 2025; Suh
et al., 2025). The most thorough examples are Binz et al. (2025) and Kolluri et al. (2025). Binz
et al. (2025) fine-tune LlaMA-3.1 70B on the Psych-101 dataset with trial-by-trial data from more
than 60,000 participants and 10,000,000 choices across 160 experiments. Their Centaur model not
only improves performance on held-out participants but also generalizes to new tasks and domains.
Binz et al. (2026) extend this line with Psych-201, a behavioral-alignment benchmark used to show
that post-training systematically reduces alignment with human behavior across model families
and that persona-induction on top of an off-the-shelf chat model does not improve individual-level
predictions on that battery. Kolluri et al. (2025) fine-tune LLaMA-3-8B and Qwen-2.5-14B on
2.9 million responses across 210 NSF-TESS social-science experiments and report distributional
alignment with human responses that beats GPT-4o by 12.1 percent (LLaMA) and 13.2 percent
(Qwen) on completely unseen studies. These approaches are complementary to prompt-based
methods but require curated training data and a separate compute budget.
What is currently missing in published work are digital twins, built from pre-existing heteroge-
neous panel datasets, of the kind market research firms already hold or that companies routinely
collect through CRM, loyalty, or repeat-survey programs. Such panels are a strong candidate
substrate for twin construction for at least three reasons. First, they accumulate hundreds of
items per person through repeated surveys across many topics, which is materially more than
the demographics-only personas in published persona-bot work and on par with or larger than
purpose-built twin instruments. Second, the topics covered are commercially relevant (consump-
9

tion, employment, family, household equipment, time use), so twins built on them speak directly to
the questions firms ask in practice. Third, panels run for years, so values, opinions, and behaviors
are observed repeatedly per person and life-course changes are recorded, which gives the model
genuine within-person variation rather than a single cross-sectional snapshot.
2.4. Documented Failure Modes
At the segment level, prior work has shown that persona bots produce opinion distributions that
systematically deviate from human aggregates (Bisbee et al., 2024; Boelaert et al., 2025; Santurkar
et al., 2023) and can carry the political leanings introduced through pretraining and alignment
(Motoki et al., 2024; Rozado, 2024; Santurkar et al., 2023). At the individual level, Peng et al.
(2025) reports that twins inherit these biases and add their own, including shrinkage toward the
base-model prior and over-reliance on demographic shortcuts, and L. Li et al. (2025) finds that bias
is amplified as more LLM-generated persona content is added; P. S. Park et al. (2024) and Gupta
et al. (2024) document related patterns of reduced diversity and persona-assigned reasoning bias.
Because twins aggregate up into segments, individual-level failures propagate to the population
level whenever segments are reconstructed from twin populations.
Peng et al. (2025) report a 19-substudy pre-registered evaluation using the Twin-2K-500 dataset.
Across 164 outcomes, individual-level accuracy is 0.748 for the full persona and 0.746 for a 14-
variable demographics-only persona, statistically indistinguishable at p = 0.37, with an empty
persona reaching 0.734 and a random null 0.629. Per-outcome cross-respondent correlation is r
= 0.197 for the full persona. Twin response variance is lower than human variance in 154 of 164
outcomes (94 percent). The authors consolidate these patterns into five distortions: insufficient in-
dividuation, demographic stereotyping, representation bias, ideological drift, and hyper-rationality.
Companion diagnostic work documents related concerns from adjacent angles, including psycho-
metric invalidity of LLM responses on standardized scales (Petrov et al., 2024), prompt-form and
probe sensitivity (Brucks & Toubia, 2025; Dominguez-Olmedo et al., 2024; X. Wang et al., 2024),
10

alignment-induced ideological drift (Lyman et al., 2025), social-desirability response bias (Salecha
et al., 2024), and contamination risk for survey research at the population level (Gao et al., 2025;
Westwood, 2025). A parallel literature uses LLMs to replicate prior human-subject studies and
treatment effects, with mixed but informative results (Aher et al., 2023; Cui et al., 2025; Hewitt
et al., 2024; Mei et al., 2024).
We use the insights from this literature to interrogate the outputs of our own digital twins, reporting
the individual- and population-level versions of the metrics that this stream has established and
noting where our results align with or diverge from the biases cataloged above.
2.5. The Gap We Fill
Our contribution sits at the intersection of three streams of work that together do not address the
operationally most relevant question for marketing practice. We work in the detailed individual-
representation paradigm rather than the coarse persona-bot paradigm: most LLM market-research
work to date (Brand et al., 2023; Goli & Singh, 2024; P. Li et al., 2024; M. Wang et al., 2026) con-
ditions on a handful of demographic axes and aggregates LLM outputs to population-level targets,
which cannot speak to within-person fidelity, rank-order, or dispersion and cannot be decomposed
back to individuals. The detailed twin literature (Binz et al., 2025; J. S. Park et al., 2026; Toubia et
al., 2025) is individual-aware but bespoke-data-only, requiring data collection designed end-to-end
for twin construction, which is precisely what firms cannot retrofit cheaply. Construction-method
levers such as embedding, reasoning, and information depth have each been examined anecdotally
(J. S. Park et al., 2026; Peng et al., 2025; Snell et al., 2024; Toubia et al., 2025; Wei et al., 2022)
but never systematically on a shared dataset and a shared evaluation set. We fill this intersection by
building detailed individual-level twins from a pre-existing heterogeneous panel dataset (SOEP)
and evaluating them across the full construction-method grid using the accuracy, rank-order corre-
lation, and dispersion-ratio framework inherited from Peng et al. (2025), Toubia et al. (2025), and
J. S. Park et al. (2026).
11

3. Methodology
Prior work has shown that LLM-based digital twins are sensitive to three independent construction
choices: how persona context is embedded in the prompt (J. S. Park et al., 2026; Toubia et al.,
2025); whether the model is prompted to reason explicitly before responding (Toubia et al., 2025);
and how much individual context the prompt carries (J. S. Park et al., 2026; Peng et al., 2025).
However, to the best of our knowledge, no published study has compared digital-twin construc-
tion methods systematically, which leaves an open question: which combination of construction
choices actually performs best?
The remainder of this section sets out the design of the resulting 3×5×2×2=60-cell construction-
method grid: the SOEP source data and our 500-participant sample (Section 3.1), the three open-
weights LLMs (Section 3.2), the two embedding methods, the two reasoning modes, the five cumu-
lative information depths ranked by Shannon entropy (Section 3.5), and the three evaluation metrics
(Section 3.6). By holding the participant subsample and the held-out evaluation set fixed across all
60 cells, the resulting curves isolate the marginal contribution of each construction-method choice
and let us assess its robustness across models.
3.1. Data and Sample Selection
We build our digital twins on the German Socio-Economic Panel (SOEP), a longitudinal household
panel administered by DIW Berlin since 1984 (Goebel et al., 2019) that provides individual-level
microdata on a representative cross-section of the resident German population. It covers a het-
erogeneous adult population across ten thematic life domains and spans four decades of repeated
measurement; we accessed the microdata under a granted SOEP data contract with DIW Berlin.
As a non-U.S. panel, it also serves as a counter-weight to the U.S.-centric datasets that dominate
published digital twin work (J. S. Park et al., 2026; Toubia et al., 2025). Specifically, we use SOEP-
Core v40 EU Edition (Socio-Economic Panel, 2025), which covers Demographics and Population;
12

Integration, Migration, and Transnationalisation; Health and Care; Employment and Occupation;
Education and Qualification; Family and Social Networks; Attitudes, Values, and Personality;
Housing, Equipment, and Private Household Services; Time Use and Environmental Behaviour;
and Income, Taxes, and Social Security. Table 1 reports the resulting question composition across
these ten domains.
We take a cross-sectional snapshot of the 2023 wave and merge five source datasets:pl(individual
questionnaire),biol(biography),hl(household),ppathl(person meta-data), andpgen(gener-
ated status variables). We retain all migration samples (Brücker et al., 2014) and refugee samples
(Brücker et al., 2026) to preserve the full diversity of the panel.2
Starting from 820,360 individual records in thepldataset, we apply participant-level filters (2023
survey wave, complete Big Five responses on the BFI-S (Schupp & Gerlitz, 2008), biography
coverage within 2019 to 2023, valid household linkage) and a column-level pipeline (versioned-
column deduplication, fill-rate threshold, technical-identifier exclusion, near-duplicate removal,
and LLM-based question reformulation and scale-type assignment) to arrive at 16,055 participants
and 949 usable question-answer pairs per participant across all ten SOEP categories. The 949
questions split into 38 core demographic items that always appear in the persona context, 728
persona-context questions used to build the digital twin, and 183 held-out evaluation questions
reserved exclusively for measuring prediction accuracy. Step-by-step row counts, filter rationales,
and LLM post-processing examples are reported in Web Appendices A.3, A.4, and A.5.
For the construction-method grid we draw a fixed random subsample of 500 participants from the
16,055-participant pool. Five hundred participants is a deliberate sweet spot: it is large enough
to make differences between cells in the 60-cell grid detectable with reasonable statistical power,
small enough to keep the total compute requirement tractable (the grid runs over 2.1 million twin
responses locally, each of which then has to be scored again locally by an LLM-as-judge), and
2Recent SOEP recruitment waves have disproportionately sampled refugees and migrants (particularly from
Ukraine and Syria).
13

Table 1
Dataset overview: distribution of 949 usable datapoints across SOEP thematic categories, data splits, and scale types.
Values show column-wise percentages within each split.
SOEP Category
Demographic
Information
Questions for
Persona Constr .
Questions for
Persona Eval. Total
(n=38) (n=728) (n=183) (N=949)
Employment and Occupation 26.3% 14.3% 14.8% 141
Education and Qualification 21.1% 7.4% 5.5% 72
Demographics and Population 18.4% 7.1% 6.6% 71
Income, Taxes, and Social Security 5.3% 10.3% 12.0% 99
Attitudes, Values, and Personality 0.0% 7.4% 3.8% 61
Family and Social Networks 7.9% 8.7% 7.1% 79
Health and Care 0.0% 6.7% 6.0% 60
Integration, Migration, Transnation. 18.4% 18.8% 22.4% 185
Housing, Equipment, Private HH Services 2.6% 15.1% 16.4% 141
Time Use and Environmental Behaviour 0.0% 4.1% 5.5% 40
Total 38 728 183 949
by scale type:
Nominal 60.5% 48.8% 46.4% 463
Ordinal 15.8% 25.5% 27.3% 242
Metric 23.7% 25.7% 26.2% 244
Note.Demographic Information = core demographic variables included as baseline context in all condi-
tions. Questions for Persona Construction and Questions for Persona Evaluation were drawn randomly
(80/20 split, seed=42) from the pool of 911 standard questions; any differences in distribution between
the two splits occurred by chance. SOEP categories translated from the original German thematic areas
(“Themen”).
14

small enough to avoid a setting in which trivially small construction-method differences become
statistically significant by sheer sample size. Holding this 500-participant subsample fixed across
all 60 cells is what makes the cell-to-cell comparisons interpretable.
Although SOEP is academic microdata, datasets of comparable shape (detailed individual-level
survey histories spanning many life domains) also exist in large market-research firms, in enter-
prises with mature CRM systems and in-house consumer panels, and increasingly in digital-twin
startups such as simile.ai and ListenLabs. Findings on SOEP therefore have direct parallels in the
commercial settings where comparable but proprietary data are available.
3.2. Large Language Model Selection
We evaluate three open-weights models:Qwen3-30B-A3B(Qwen Team, 2025),Gemma-4-26B-
A4B(Gemma Team, Google DeepMind, 2025), andMinistral-3-14B(Liu et al., 2026). In the
Results chapter we refer to them as: Qwen 3, Gemma 4, and Ministral 3. We selected them
because each ships paired reasoning and non-reasoning variants on Hugging Face, and all three
rank among the top open-source models runnable on a single GPU as of May 2026 on LiveBench
(White et al., 2025) and the Artificial Analysis Intelligence Index. 3 We serve all inference locally
on a single NVIDIA H100 via vLLM; closed-source frontier models are excluded by the SOEP
data license. All three models support German natively and we use the original SOEP wording.
Multilingual benchmarks consistently show small accuracy gaps relative to English, attributable
to English-skewed pretraining and tokenizer optimization. Our reported accuracy and correlation
levels can therefore be read as a lower bound for what equivalent twins would achieve on English-
language panels in the US or UK, where the same models have stronger native support.
3https://artificialanalysis.ai/models/open-source/small
15

3.3. Embedding methods
The persona context can be presented to the LLM either as anarrative summarythat compresses
each participant’s survey responses into a dense description of the information, or as adialog input
that preserves the raw question-and-answer pairs as alternating user/assistant chat turns (J. S. Park
et al., 2026; Toubia et al., 2025). We construct the narrative summaries using a Chain-of-Density
summarization approach, adapted from Adams et al. (2023). Full prompts, per-category examples,
and the Chain-of-Density summarization procedure are reported in Web Appendix B.
3.4. Reasoning modes
Each of the three models is queried either innon-reasoningmode, where it provides a direct
response to the question, or inreasoningmode, in which it first produces an internal<think>
block before emitting the visible response. For Qwen 3 and Ministral 3 we use the dedicated
reasoning checkpoints released by the vendors (Qwen3-30B-A3B-Thinking-2507 and Ministral-
3-14B-Reasoning-2512); Gemma 4 does not ship a separate reasoning checkpoint, so we elicit
the reasoning trace from the same Gemma-4-26B-A4B model via the structured-thinking prompt
template in Web Appendix B.3. The non-reasoning variants are Qwen3-30B-A3B-Instruct-2507,
Ministral-3-14B-Instruct-2512, and the same Gemma-4-26B-A4B model with the reasoning in-
struction removed. The design is inspired by chain-of-thought prompting (Wei et al., 2022) and
the broader test-time-compute literature (Snell et al., 2024); the per-model system prompts and an
example reasoning trace are reported in Web Appendix B.3.
3.5. Information Depth
Prior work on individual-level digital twins has typically been built from data collected specifically
for the purpose: the four-wave Twin-2K-500 dataset of∼500 curated questions (Toubia et al.,
2025), and the two-hour American V oices Project interview transcripts (J. S. Park et al., 2026).
Our dataset is different and, we argue, more representative of the conditions under which firms
16

would actually deploy twins. SOEP accumulates hundreds of items per person through repeated
surveys across many commercially relevant life domains (consumption, employment, family, time
use, housing, attitudes). It was never designed for twin construction, the topical coverage is uneven,
and the information density per item varies widely. This is also the data shape held by firms with
mature CRM, loyalty, and repeat-survey programs, and it raises three substantial questions for
prompt construction: (1) Should all available information be included, or does additional context
eventually hurt rather than help? (2) What is the marginal gain of each additional unit of context,
and at what point do returns diminish? (3) On what principle should items be ranked when only a
subset of data is selected?
We address all three by structuring the persona context by information density, using normalized
Shannon entropy (Cover & Thomas, 2006; Shannon, 1948) as a measure of how strongly each sur-
vey question differentiates between individuals. For each of the 728 persona-context questions we
compute the normalized Shannon entropy of the empirical response distribution across all 16,055
participants in the pre-filtered pool, treating this value as a proxy for the question’s differentiating
power. For a discrete random variableXwithkpossible outcomes and probability massp(x i),
we compute the normalized Shannon entropy as the raw entropy divided by the maximum entropy
attainable for the question’s scale:
Hnorm(X) =− ∑k i=1 p(xi)log 2 p(xi) log2 k ∈[0,1].(1)
By construction,H norm =0 when all respondents give the same answer (no differentiating power)
andH norm =1 when responses are uniformly distributed across categories (maximum differentiat-
ing power). Intuitively, a question where 99% of respondents answer “Yes” tells us almost nothing
about how to distinguish a specific person, while a question whose responses are evenly distributed
across five categories provides substantial differentiating information.
We use these normalized entropy scores to rank the 728 persona-context questions in descending
17

order and split at the quartile boundaries into four equal-sized buckets of 182 questions each. We
then define fivecumulativeinformation depth levels: (1) Basic demographic information, (2) De-
mographics + 25% Quartile, (3) Demographics + 50% Quartile, (4) Demographics + 75% Quartile,
(5) All available persona-context data. The depth levels are cumulative, meaning digital twins at
depth level 3 see all demographic, first quartile and second quartile questions, sorted by normalized
Shannon entropy. This cumulative ordering isolates the marginal effect of each successive quartile
on prediction accuracy.
Demo: +5.1%
Q1: +39.1%
Q2: +28.9%
Q3: +17.8%
Q4: +9.1%
0
25
50
75
100
0 100 200 300 400 500 600 700
Number of Questions (sorted descending)
Cumulative % of Total
Cumulative %
Perfect equality
Figure 1.Cumulative distribution of normalized Shannon entropy across the 728 persona-context questions, sorted by
descending entropy. Dashed vertical lines mark the boundaries of the four cumulative information depth levels. The
dashed diagonal represents perfect equality (uniform entropy contribution).
The distribution of normalized entropy across the 728 persona-context questions is non-uniform
(see cumulative distribution in Figure 1). The first entropy quartile alone captures 39.1% of the
total Shannon entropy across all persona-context questions, while the last entropy quartile con-
tributes only 9.1%. Our systematic comparison of construction methods reveals whether the ac-
curacy of digital twins follows the same diminishing-returns shape. Web Appendix D.6 reports a
random-question-selection ablation on a subsample of 500 participants, in which the four cumula-
tive quartiles are replaced with cumulative random quartiles of matching size.
18

3.6. Evaluation Metrics
We evaluate twins on three complementary metrics, following Peng et al. (2025). The first is an
accuracy score that captures how close each twin’s answer is to the human’s. For each (question,
participant) cell we adapt the score from Toubia et al. (2025) and extend it with partial credit for
ordinal items:
S=



1 if prediction = ground truth (nominal)
0 if prediction̸=ground truth (nominal)
1− |pos(GT)−pos(Pred)| noptions −1 (ordinal)
1− |GT−Pred| Range (metric)
(2)
where pos(·)is the position of an ordinal option and Range is the natural range of a metric outcome;
S∈[0,1]with 1 a perfect prediction. Predicted responses are normalized via an LLM-as-judge pass
before scoring (see Web Appendix B.7).
The second is a correlation metric that captures whether twins additionallyrank-orderparticipants
the same way humans do, a property accuracy is blind to whenever twins sit close to the human
mean on every question. For each questionqwe compute the Pearson correlationr q between the
vectors of human and twin responses across participants, restricted to ordinal and metric items
where option order is meaningful. We aggregate ther q across questions via a Fisherztransform
(mean of atanh(rq), back-transformed) to obtain the cell-level ¯r.
The third is a dispersion-fidelity metric that captures whether twins reproduce thespreadof human
responses across participants, the failure mode Peng et al. (2025) describes as “insufficient individ-
uation.” For each questionqwe compute the ratioσ (q) twin/σ (q) human of digital twin to human standard
deviations across participants, on the same ordinal+metric items used for correlation, and report
two summaries per cell: the mean ratio across questions (with a bootstrap CI) and, mirroring Peng’s
19

binary framing, the share of questions withσ (q) twin <σ (q) human. This variance ratio complements the
other two metrics and tells us if the distribution of digital twins is too narrow or too wide. It is also
essential to spot model-collapse and metric-scale blow-out failures.
For all three metrics we aggregateper question first, then average across questions, matching the
convention of Peng et al. (2025) and weighting every question equally regardless of participant
coverage. Implementation details, edge-case conventions (zero-variance, twin-collapse, metric-
scale winsorization), and the per-question coverage threshold are reported in Web Appendix C.
4. Results
We evaluated the 60-cell construction-method grid (3 models×5 information depths×2 embed-
ding methods×2 reasoning modes; Section 3) on a held-out evaluation set of 183 questions (89
nominal, 94 ordinal/metric; per-cell coveragen q ≈89 after NA drops). 98.01 % of the 2,104,164
expected responses yielded valid scores; the remaining 1.99 % split into ambiguous ground truths
(1.65 %), unparseable LLM outputs (0.32 %), and upstream pipeline errors (0.02 %). A per-model
breakdown of data quality is provided in Web Appendix D.1. Sections 4.1–4.4 and Web Appendix
D report the detailed findings; Table 2 gives the joint per-cell accuracy and correlation grid.
20

Table 2
Accuracy and correlation by construction method and model (n=500 participants).
Persona Description Dialog Input
Information DepthNon-Thinking Thinking Non-Thinking Thinking
acc↑/ corr↑acc↑/ corr↑acc↑/ corr↑acc↑/ corr↑
Qwen3-30B
Basic Demographic 0.708 / 0.253 0.683 / 0.272 0.706 / 0.2650.717/0.299
25% Quartile0.721 / 0.369 0.698 /0.4030.706 / 0.248 0.707 / 0.359
50% Quartile0.741/ 0.456 0.723 /0.490 0.732 / 0.351 0.735 / 0.468
75% Quartile 0.750 / 0.514 0.737 /0.579 0.754/ 0.434 0.753 / 0.565
100% Quartile 0.759 / 0.489 0.743 / 0.582 0.762 / 0.5040.767/0.590
Gemma-4-26B
Basic Demographic 0.679 / 0.329 0.645 / 0.278 0.722 / 0.3270.748 /0.362
25% Quartile 0.670 / 0.368 0.667 /0.418 0.714/ 0.290 0.705 / 0.337
50% Quartile 0.686 / 0.405 0.680 /0.4590.739 / 0.3900.755 / 0.454
75% Quartile 0.710 / 0.486 0.695 / 0.515 0.762 / 0.5120.772 /0.542
100% Quartile 0.725 / 0.446 0.703 /0.5320.773 / 0.4910.788 / 0.502
Ministral-14B
Basic Demographic 0.613 / 0.250 0.651 /0.286 0.687/ 0.277 0.684 / 0.265
25% Quartile 0.604 / 0.354 0.656 /0.3580.690 / 0.2680.690/ 0.242
50% Quartile 0.635 /0.4370.666 / 0.3850.726/ 0.404 0.721 / 0.349
75% Quartile 0.646 /0.5040.671 / 0.4300.746/ 0.476 0.745 / 0.458
100% Quartile 0.657 / 0.484 0.678 /0.5060.755 / 0.4700.756/ 0.491
Note.Boldmarks the best value within each (model, depth) row; underline marks the best value across
all models within each depth. Both are applied independently for accuracy and correlation.
21

4.1. Effects of the Information Depth
The marginal effect of cumulatively adding more persona context is summarized in Figure 2, which
plots accuracy and Fisher-zcorrelation by depth. Both metrics increase monotonically across con-
dition cells. Accuracy gained an average of 5.2 pp from Basic Demographic to the 100 % Quartile,
with per-model lifts of+5.6,+5.1, and+6.8 pp on the three Dialog Non-Thinking cells for Qwen
3, Gemma 4, and Ministral 3 respectively. Fisher-zcorrelation gained an average of 21.9 pp over
the same range, a factor of four larger; Qwen 3 Dialog Non-Thinking moved fromr=0.265 to
0.504 (∆= +23.9 pp), and its Thinking sibling reached the cross-grid maximumr=0.590 at the
100 % Quartile (∆= +29.1 pp; Table 2). Correlation responded to persona content more sensi-
tively than accuracy on every model that responded monotonically to depth, replicating the pattern
that Peng et al. (2025) report on the Twin-2K-500 dataset (Toubia et al., 2025), namely that rank-
order correlation responds more strongly to added persona context than mean accuracy does, but
at three to five times larger magnitude on our open-weights stack.
0.64
0.68
0.72
0.76
Basic Demographic
25% Quartile 50% Quartile 75% Quartile 100% Quartile
Information Depth
Mean accuracy
Qwen3−30B
Ministral−14B
Gemma−4−26B
0.3
0.4
0.5
Basic Demographic
25% Quartile 50% Quartile 75% Quartile 100% Quartile
Information Depth
Fisher−z−averaged Pearson r
Qwen3−30B
Ministral−14B
Gemma−4−26B
Figure 2.Accuracy (left) and Fisher-zcorrelation (right) by information depth, with±1 standard-error bands per
model computed across the four construction cells (embedding×reasoning) at each depth.
Across the cells, the bulk of the gain landed in the two middle transitions (25→50 % and 50→
75 %): together they accounted for+4.3 of the+5.2 pp accuracy lift and+16.7 of the+21.9 pp
correlation lift. The opening transition (Basic→25 %) was effectively flat on accuracy (−0.1 pp),
and the closing transition (75→100 %) added only+0.6 pp of correlation. The biggest single-
cell accuracy jumps landed in the 25 %→50 % transition (Gemma 4 Dialog Thinking+5.0 pp;
Ministral 3 Dialog Non-Thinking+3.6 pp). The 75 %→100 % transition delivered less corre-
22

lation gain on average (+0.6 pp, with Gemma 4 Dialog Thinking actually losing−4.0 pp). This
means that the context-length increase from the 75 % to the 100 % information depth did not pay
off consistently on rank-ordering. The 75 % Quartile (≈584 of the 728 train items) captured most
of the available accuracy signal and the bulk of the correlation signal.
The per-model accuracy curves (Figure 3) show this concave pattern, with some model-specific
heterogeneity across the construction methods.
Dialog Non−Thinking Dialog Thinking
Summary Non−Thinking Summary Thinking
Basic Demographic
25% Quartile50% Quartile75% Quartile100% Quartile
Basic Demographic
25% Quartile50% Quartile75% Quartile100% Quartile
0.60
0.65
0.70
0.75
0.80
0.60
0.65
0.70
0.75
0.80
Information Depth
Accuracy
Model Qwen3−30B Ministral−14B Gemma−4−26B
Figure 3.Per-model accuracy by information depth, with all four construction methods overlaid.
To bound how much of the accuracy and correlation levels came from persona content rather than
from instruction-following, we ran an empty-persona ablation where Qwen 3 Dialog Non-Thinking
was re-evaluated at all five depths with the persona content replaced by an empty block (Figure 4,
23

Web Appendix D.5). Empty-persona accuracy was flat, as expected, across information depths4 at
0.65–0.66, while personalized accuracy climbed from 0.706 to 0.762, so the personalization delta
widened from+4.2 pp at Basic Demographic to+10.8 pp at the 100 % Quartile, an order of mag-
nitude larger than Peng’s+1.4 pp on Twin-2K-500. Empty-persona correlation was structurally
pinned atr=0 at every depth (zero twin variance implies Pearson is coded as 0 per the Peng
et al. (2025) convention), so the entire personalized correlation curve was attributable to persona
content. The empty-persona correlation panel is reproduced in Web Appendix D.5.
0.65
0.70
0.75
Basic Demographic
25% Quartile 50% Quartile 75% Quartile 100% Quartile
Information Depth
Accuracy
Personalized
Empty persona
Figure 4.Empty-persona ablation. Personalized versus empty-persona accuracy by information depth on Qwen 3
Dialog Non-Thinking (n=500 participants, 183 held-out questions). Empty-persona accuracy is depth-flat at 0.65–
0.66; the personalization delta widens from+4.2 pp at Basic Demographic to+10.8 pp at the 100 % Quartile.
We also found that the entropy-based ranking of persona-context questions had less effect than
hypothesized. Cumulative random quartiles of equal size produced curves statistically indistin-
guishable from entropy-ranked quartiles at every depth on both metrics (paired-question sign test,
p>0.10 at every depth; aggregated paired test across the four ablation depths,p≈0.32; Web
Appendix D.6). The increase in accuracy and correlation with depth was driven primarily by cu-
mulatively adding more information, not by the within-pool prioritization of high-entropy items.
4This behavior is expected, since the model answered the same evaluation questions using the same context across
all information depths. The variance is caused by the non-deterministic behavior of the model at a temperature level
greater than 0.
24

Entropy is also not the only meaningful selection signal: per-item relevance to the evaluation ques-
tion and per-question covariance structure are both plausible alternatives that we did not test here,
and either could outperform random selection without being captured by raw response entropy.
0.5
0.6
0.7
0.8
0.9
Basic Demographic
25% Quartile 50% Quartile 75% Quartile 100% Quartile
Information Depth
Mean accuracy
Hard
Medium
Easy
Figure 5.Personalized accuracy by information depth (Qwen 3 Dialog Non-Thinking,n=500 participants, 183 held-
out items), split by difficulty tercile with 95 % confidence bands. Difficulty is defined by empty-persona accuracy at
the 100 % Quartile. The hard tercile (red) absorbed 3.9×the lift of the easy tercile (blue) over the depth range.
To better understand which questions drive the increase in accuracy and correlation, we split the
held-out items into three difficulty terciles using empty-persona accuracy at the 100 % Quartile
(cut-points 0.578 and 0.820; 59 hard / 58 medium / 58 easy items) and replotted the depth-accuracy
curve within each tercile on the same Qwen 3 Dialog Non-Thinking run (Figure 5). Interestingly,
the depth gain concentrated on the hard tercile, with the easy tercile near-saturated at every depth
(88.4 %–90.6 % across all five depths). The corresponding deltas table is in Web Appendix D.10.
Accuracy increased by+8.6 pp on hard items,+6.1 pp on medium items, and+2.2 pp on easy
items. More information depth, in other words, helps most on items where the most common
population response (the modal answer) is not the same as the participant’s actual response, and
barely helps on items where the modal response already coincides with the participant’s answer.
Variance ratio shows a similar pattern to accuracy and correlation under cumulative information
depth. Across all available construction cells the mean variance ratio rose from 0.98 at Basic
25

Demographic to 1.09 at the 100 % Quartile (+0.11, a+10.7% relative increase).
4.2. Effects of the Model Selection
The three models separated cleanly when each construction cell’s metric values were averaged
into a per-model summary. The fingerprint matrix (Figure 6, Table 3) condenses each model
into a 1×3 z-score row across the three metrics, averaged across the 20 construction cells per
model. Qwen 3, on average, led every metric: accuracy (0.730), Fisher-zcorrelation (0.431), and
dispersion closeness (σtwin/σhuman =0.99), with composite row mean+0.84. Gemma 4 came in
close on accuracy and correlation (0.717 and 0.426) but is slightly under-dispersed (mean ratio
0.88, composite−0.09). Ministral 3 trailed on accuracy (0.684) and correlation (0.388) and was
mildly over-dispersed (mean ratio 1.07, composite−0.76). The model ranking is not the same
across embedding methods: on Persona Summary cells Qwen 3 leads at every information depth
from the 25 % Quartile upward, while on Dialog cells Gemma 4 takes the cross-model top accuracy
at all depths beyond the basic-demographic baseline, including the cross-grid maximum at 100 %
Quartile Dialog Thinking (0.788). Ministral 3 trails on Persona at every depth and closes the gap
to Gemma only on Dialog.
Table 3
Per-model summary statistics and z-scored composite fingerprint, pooled across the 20 construction cells per model
(n=500 participants; correlation and variance ratio restricted to ordinal/metric items). The z-score columns
benchmark each model against the three-model panel; variance-ratio z-scores are computed on−|σ twin/σhuman −1|
so that higher z = closer to human dispersion.
Model Acc. Corr .σ twin/σhuman z(Acc) z(Corr) z(VR-close) z(row mean)
Qwen3-30B 0.730 0.431 0.990 +0.83 +0.69 +1.01+0.84
Gemma-4-26B 0.717 0.426 0.881 +0.28 +0.45 -0.99-0.09
Ministral-14B 0.684 0.388 1.066 -1.11 -1.15 -0.02-0.76
Across the construction grid (Table 2), every model scored its best accuracy in the Dialog×Think-
ing×100 % Quartile cell, giving a consistent recipe for the accuracy-best configuration. Gemma
4’s Dialog Thinking 100 % cell achieved the cross-grid maximum accuracy (0.788), Qwen 3’s
Dialog Thinking 100 % cell achieved the cross-grid maximum correlation (r=0.590), and Minis-
26

tral 3 benefited disproportionately from the Dialog embedding (+9.8 pp at 100 % Quartile Non-
Thinking, the largest single-cell embedding effect in the grid; see Section 4.3).
+0.83 +0.69 +1.01
+0.28 +0.45 −0.99
−1.11 −1.15 −0.02Ministral−14B
Gemma−4−26B
Qwen3−30B
Accuracy Correlation Var−ratio
closeness
Z−score
(higher
is better)
−1
0
1
Cross−model fingerprint (z−scored, n = 4 models)
Figure 6.Z-scored composite fingerprint for the three models across the three twin-quality metrics. Each cell is
the across-model z-score of the model’s per-cell-averaged metric value (accuracy / Fisher-zcorrelation / closeness to
human variance, encoded as−|σ twin/σhuman −1|so higher = closer to parity = better). Higher and greener = better on
all three columns.
The per-question variance-ratio distributions (Figure 7) are well-shaped for all three models, with
per-model medians close to 1 (Qwen≈0.99, Ministral≈1.07) or modestly below (Gemma≈0.88)
and a reasonable spread.
4.3. Effects of the Embedding Method
We compared the two embedding strategies, the Chain-of-Density (CoD) Persona summary and
the Dialog input, on the same construction grid. Figure 8 reports the marginal effect of switching
from Persona to Dialog, pooled across reasoning modes and information depths, on each of the
three twin-quality metrics.
Accuracy increased for all three models when switching from Persona to Dialog. The mean gain
across construction cells was+6.2 percentage points for Gemma 4 (pairedt-testp=8.3×10 −6)
27

median = 0.88
share < 1: 63%
median = 0.82
share < 1: 72%
median = 0.96
share < 1: 57%
Gemma−4−26B
Qwen3−30B Ministral−14B
0.05 0.1 0.25 0.5 1 2 5
0.05 0.1 0.25 0.5 1 2 5
0
2
4
6
0
2
4
6
Variance ratio between human and twin responses
% of questions
Qwen3−30B
Ministral−14B
Gemma−4−26B
Figure 7.Per-question variance-ratio distributionσ twin/σhuman by model on a logx-axis. Each per-(model, question)
value is the mean across the 20 construction cells per model of the per-cell winsorised SD ratio on that question;
per-cell ratios are capped at 5 before averaging. Restricted to ordinal- and metric-scale items. Dashed grey line at
ratio=1; solid black line at the per-model median.
and+7.2 percentage points for Ministral 3 (p=6.1×10 −6); Qwen 3’s gain was much smaller at
+0.8 percentage points (p=0.14). Fisher-zcorrelation barely moved for any model (all|∆r| ≤
0.03,p≥0.07). The variance ratio stayed close to parity for Ministral 3 (1.09→1.05,p=
0.08) and Qwen 3 (1.02→0.96,p=0.22); for Gemma 4 the ratio moved further from parity
(0.91→0.85,p=0.026). Per-cell numbers underlying these aggregates are in Web Appendix D.2
(accuracy), Web Appendix D.3 (correlation), and Web Appendix D.4 (variance ratio).
Restricting attention to the 100 % Quartile cells, switching from Persona to Dialog raised accuracy
in every (model×reasoning) cell (Web Appendix D.2). The largest single-cell improvements were
28

0.64
0.68
0.72
0.76
Summary Dialog
Embedding Method
Mean accuracy
Qwen3−30B
Ministral−14B
Gemma−4−26B
0.36
0.40
0.44
0.48
Summary Dialog
Embedding Method
Fisher−z−averaged Pearson r
Qwen3−30B
Ministral−14B
Gemma−4−26B
0.9
1.0
1.1
Summary Dialog
Embedding Method
Mean SD ratio   σtwin σhuman
Qwen3−30B
Ministral−14B
Gemma−4−26B
Figure 8.Persona summary (left endpoint) versus Dialog input (right endpoint) per model, pooled across reasoning
modes and information depths. Left: accuracy. Center: Fisher-zcorrelation. Right: variance ratio.
Ministral 3 Non-Thinking (+9.8 pp), Gemma 4 Thinking (+8.5 pp), and Ministral 3 Thinking
(+7.8 pp); Qwen 3, by contrast, picked up at most+2.4 pp from the Dialog embedding at 100 %
depth.
The accuracy gain comes at a measurable token cost. At the 100 % Quartile, the Persona sum-
mary averages 2,761 words / 5,354 tokens per participant; the Dialog input averages 7,074 words
/ 14,863 tokens, roughly 2.6×the words and 2.8×the tokens (sampledn=100 participants;
tiktoken cl100k_base). The CoD summary’s token efficiency comes from paraphrasing scale
items into integrated prose, but that compression collapses information, like Likert labels, into ap-
proximate descriptions. A participant’s response of “Does not apply at all” (lowest of six points) to
the question “How much do you agree with the statement that you react annoyed when others take
your attention away?” (translated from German) is rendered in the CoD summary as “She does not
react annoyed when others take her attention away.” (translated from German). Dialog preserves
the exact information, while persona summaries collapse it to a binary negation.
The trade-off is therefore one of lossy compression: the Dialog input keeps every response from
past surveys exactly as stated in context, while the Persona summary saves roughly 60% of the
token cost (and a proportional share of latency and prompt-cache footprint) at the price of precision.
29

4.4. Effects of the Reasoning Mode
We compared Non-Thinking and Thinking by pairing the matched (embedding×information
depth) cells within each model. Figure 9 reports the marginal accuracy and correlation effect; the
matched variance-ratio dumbbell is in Web Appendix D.8.
0.675
0.700
0.725
Non−Thinking Thinking
Reasoning Mode
Mean accuracy
Qwen3−30B
Ministral−14B
Gemma−4−26B
0.35
0.40
0.45
0.50
Non−Thinking Thinking
Reasoning Mode
Fisher−z−averaged Pearson r
Qwen3−30B
Ministral−14B
Gemma−4−26B
Figure 9.Non-Thinking (left endpoint) versus Thinking (right endpoint) per model, pooled across embedding methods
and information depths. Left: accuracy. Right: Fisher-zcorrelation.
Accuracy barely moved between reasoning modes for any model (all|∆ acc| ≤2 percentage points
across cells; only Ministral 3’s+1.6 percentage-point shift reached a paired-t p-value below 0.05).
Fisher-zcorrelation rose under Thinking for Qwen 3 (∆r= +0.073, pairedt-testp=3×10 −4)
and Gemma 4 (∆r= +0.036,p=0.014), while Ministral 3 was effectively flat (∆r=−0.015,
p=0.22). The variance ratio moved toward parity under Thinking, most visibly on Gemma 4
(0.83→0.93,p=0.004).
Restricting attention to the 100 % Quartile cells, every (model×embedding) cell showed a di-
rectional correlation increase under Thinking, with Qwen 3’s Dialog 100 % Thinking cell taking
the cross-grid maximum atr=0.590 (up from 0.504 under Non-Thinking). Thinking helped most
where the base configuration was already well-aligned. The largest∆rat the 100 % Quartile landed
on Qwen 3 Summary (+0.094), Qwen 3 Dialog (+0.086), and Gemma 4 Summary (+0.086);
Ministral 3’s gains were an order of magnitude smaller (Summary+0.022, Dialog+0.021).
30

The correlation gain came at a substantial cost in inference time. Thinking inference was substan-
tially slower per prediction than Non-Thinking on our hardware, with per-model ratios spanning
roughly an order of magnitude: Qwen 3 21×, Gemma 4 5×, and Ministral 3 3×. The cost re-
flects both the additional reasoning-trace tokens and the wider generation budget configured for
Thinking runs.
5. Discussion and Conclusion
Four patterns emerge from the 60-cell construction grid. Accuracy and rank-order correlation both
rise with information depth, with diminishing returns past the 75 percent entropy quartile. The 100
percent quartile contains the best-performing cells overall and represents the achievable ceiling on
the panel data we have. The 75 percent quartile, in contrast, captures the bulk of that gain at a mod-
erate data-acquisition and prompt-token cost, and is therefore the cost-efficient Pareto point firms
should target when item volume is a constraint. The depth gain is also non-uniform across items:
hard items, defined by low empty-persona accuracy, gain+8.6 percentage points on accuracy from
basic demographics to the 100 percent quartile, while easy items gain only+2.2 percentage points.
More persona context, in other words, helps most where the most common population response
does not match the participant’s actual answer. Switching the embedding from a Chain-of-Density
persona summary to a raw dialog history of past survey responses raises accuracy in every model-
by-reasoning cell at the 100 percent depth, while an explicit thinking mode lifts Fisher-zcorrelation
by an average of+0.038 across models while leaving accuracy roughly unchanged. A plausible in-
terpretation is that thinking allocates extra inference compute to weighing competing persona cues
against each other, which sharpens between-respondent contrasts without meaningfully improving
mean accuracy across the population.
Within the open-weights stack, Qwen 3 leads on average across all three metrics (accuracy 0.730,
Fisher-zcorrelation 0.431, dispersion ratio 0.99), Gemma 4 attains the single best accuracy cell
at 0.788, and Qwen 3 attains the highest rank-order correlation atr=0.590, both in the dialog-
31

thinking-100 percent cell.
Our headline accuracy and rank-order correlation sit at the same order of magnitude as recent
findings in the digital-twin literature, despite our reliance on a pre-existing panel rather than a
purpose-built instrument. Best-cell accuracy of 0.788 on the SOEP held-out evaluation set sits
above the 0.748 full-persona accuracy reported by Peng et al. (2025) on Twin-2K-500 and above
the 0.72 absolute reported by Toubia et al. (2025), while the 0.83 to 0.86 reported by J. S. Park
et al. (2026) is on a normalized scale that benchmarks twin agreement against participants’ own
two-week test-retest consistency and is therefore comparable in interpretation rather than in level.
Best-cell rank-order correlation ofr=0.590 is roughly three times the per-outcomer=0.197 that
Peng et al. (2025) report on the same construct. The most plausible reading of the rank-order gap is
that SOEP carries more individuating signal per added item than the Twin-2K-500 battery, whose
personality and cognitive items tend to shrink toward base-model priors (Peng et al., 2025).
The empty-persona ablation tells the same story: the personalization delta widens with depth to
roughly an order of magnitude larger than the+1.4 percentage-point delta reported by Peng et
al. (2025), consistent with the SOEP panel carrying more usable personalization signal than the
Twin-2K-500 dataset. A random-quartile ablation produced curves indistinguishable from entropy-
ranked quartiles (aggregated paired testp≈0.32), so it is the total volume of items in the prompt
that drives twin quality, not the within-pool rule by which items are selected.
The distortion family cataloged by Peng et al. (2025) does not reproduce uniformly. Insufficient
individuation shows up only on Gemma 4, whose mean variance ratio of 0.88 sits below human dis-
persion and which thinking mode partially corrects (0.83 to 0.93). Qwen 3 has a near-parity mean
variance ratio of 0.99, and Ministral 3 is mildly over-dispersed at 1.07. The depth-by-difficulty split
likewise indicates that easy items are saturated by demographics alone, so demographic shortcut-
ting is concentrated on a specific subset of items rather than being a universal property of the
twins.
32

Detailed individual-level digital twins, as we, Peng et al. (2025), and J. S. Park et al. (2026) build
them, have a structural advantage over the coarse persona-bot approach used by most marketing
twin work (Brand et al., 2023; Goli & Singh, 2024; P. Li et al., 2024; M. Wang et al., 2026): they
can be aggregated post hoc to any segment a researcher cares to define, including segments not an-
ticipated at construction time, while a persona-bot designed to represent a particular demographic
segment cannot be decomposed back into individuals. Combined with our results, where best-cell
accuracy is comparable to bespoke-data twins and rank-order correlation is roughly three times the
reported per-outcome level on Twin-2K-500, this means that post-hoc segmentation and segment-
versus-segment comparisons built on these twins should reproduce both group-level means and
within-group heterogeneity better than aggregations built from coarse persona bots.
For firms that hold heterogeneous panel data, a panel of roughly 1,000 question-answer pairs per
customer is sufficient material to build twins that reach the same order of magnitude on accuracy as
twins built on purpose-collected interviews or surveys. The construction grid maps a usable cost-
quality frontier. For accuracy-first applications, the dialog-thinking-100 percent cell on Gemma 4
is the recommended recipe. For cost-first applications with acceptable accuracy, a persona-non-
thinking-75 percent cell captures the bulk of the available accuracy gain at substantially lower
compute. On input tokens, the Chain-of-Density persona summary at the 100 percent quartile
uses roughly 36 percent of the dialog-condition input budget (5,354 versus 14,863 tokens per par-
ticipant), so switching from Dialog to Persona saves about two-thirds of the prompt-token bill.
On output tokens, the non-thinking mode avoids the reasoning-trace generation that lifts thinking-
mode inference time by roughly 3×(Ministral 3), 5×(Gemma 4), and 21×(Qwen 3) over direct
prompting. For applications that prize rank-ordering of respondents, such as segmentation or scor-
ing, the dialog-thinking-100 percent cell on Qwen 3 is preferred.
The depth-flat empty-persona baseline of 0.65 to 0.66 has an instructive interpretation rather than
being a nuisance. Without any persona content, the LLM still answers a large share of test items
correctly because many SOEP items have a modal answer that the model can reach by giving the
33

socially desirable response, the most common response in the population, or the response a base
model has internalized from pretraining. The baseline is therefore the right yardstick for sepa-
rating instruction-following accuracy from the marginal value of individual persona content, and
empty-persona depth ablations should become standard hygiene in twin papers, since otherwise
the contribution of individual context to reported accuracy is uninterpretable.
5.1. Limitations and Future Research
Several limitations bound the present results and motivate clear extensions. The SOEP is a Ger-
man general-population panel, and brand and choice items typical of consumer marketing are not
directly comparable. Future research should explore whether our findings can be reproduced us-
ing a US- or UK-panel on commercially relevant items. We evaluate three open-weights models
that dominate the single-GPU open-source frontier in May 2026, but we do not benchmark against
closed-source frontier models because of data-license constraints. Finally, we cover insufficient in-
dividuation, demographic shortcutting, and contamination via empty persona, but not ideological
drift (Lyman et al., 2025; Motoki et al., 2024; Rozado, 2024) or persona-induced reasoning bias
and diversity collapse (Gupta et al., 2024; P. S. Park et al., 2024), all of which warrant dedicated
follow-up work.
5.2. Conclusion
Detailed individual-level digital twins do not require bespoke conditioning data. The pre-existing
heterogeneous panel data that firms already accumulate through CRM systems, loyalty programs,
and repeat surveys is sufficient material to build twins that reach the same order of magnitude
on accuracy and rank-order correlation as published twins built on purpose-collected interviews
or surveys. Within that data, the construction-method search space collapses into a small set of
usable trade-offs: the dialog-thinking-100 percent recipe yields the strongest twins we observed,
the persona-non-thinking-75 percent recipe yields a cost-efficient near-substitute, and the choice
34

of model depends on whether the use case prizes accuracy, rank-order correlation, or dispersion
fidelity. Combined, these findings move the question from “can large firms with bespoke survey
budgets build twins?” to “can any firm with a heterogeneous panel of customer responses build
twins?”. The latter is now answered in the affirmative, and the path toward democratising consumer
insights through LLM-based digital twin research is open.
References
Adams, G., Fabbri, A., Ladhak, F., Lehman, E., & Elhadad, N. (2023). From sparse to dense: Gpt-4
summarization with chain of density prompting. https://doi.org/10.48550/arXiv.2309.042
69
Aher, G. V ., Arriaga, R. I., & Kalai, A. T. (2023). Using large language models to simulate multiple
humans and replicate human subject studies.Proceedings of the International Conference
on Machine Learning, 337–371.
Anthis, J. R., Liu, R., Richardson, S. M., Kozlowski, A. C., Koch, B., Brynjolfsson, E., Evans, J., &
Bernstein, M. S. (2025). Position: Llm social simulations are a promising research method.
Proceedings of the 42nd International Conference on Machine Learning.
Argyle, L. P., Busby, E. C., Fulda, N., Gubler, J. R., Rytting, C., & Wingate, D. (2023). Out of
one, many: Using language models to simulate human samples.Political Analysis,31(3),
337–351. https://doi.org/10.1017/pan.2023.2
Arora, N., Chakraborty, I., & Nishimura, Y . (2025). AI–Human hybrids for marketing research:
Leveraging large language models (LLMs) as collaborators.Journal of Marketing,89(2),
43–70. https://doi.org/10.1177/00222429241276529
Binz, M., Akata, E., Almaatouq, A., Alsobay, M., Ariasov, O., Brändle, F., Broska, D., Burton,
J. W., Busch, N., Callaway, F., Cheung, V ., Christian, B., Coda-Forno, J., Demircan, C.,
Dentella, V ., Eckstein, M. K., Éltet˝o, N., Franke, M., Griffiths, T. L., . . . Schulz, E. (2026).
35

Post-training makes large language models less human-like. https://doi.org/10.48550/arXi
v.2605.07632
Binz, M., Akata, E., Bethge, M., Brändle, F., Callaway, F., Coda-Forno, J., Dayan, P., Demircan, C.,
Eckstein, M. K., Éltet˝o, N., et al. (2025). A foundation model to predict and capture human
cognition.Nature,644(8078), 1002–1009. https://doi.org/10.1038/s41586-025-09215-4
Bisbee, J., Clinton, J. D., Dorff, C., Kenkel, B., & Larson, J. M. (2024). Synthetic replacements for
human survey data? the perils of large language models.Political Analysis,32(4), 401–416.
https://doi.org/10.1017/pan.2024.5
Boelaert, J., Coavoux, S., Ollion, É., Petev, I., & Präg, P. (2025). Machine bias: How do generative
language models answer opinion polls?Sociological Methods & Research,54(3), 1156–
1196. https://doi.org/10.1177/00491241251330582
Brand, J., Israeli, A., & Ngwe, D. (2023). Using LLMs for market research.Harvard Business
School Marketing Unit Working Paper, (23-062). https://doi.org/10.2139/ssrn.4395751
Brücker, H., Kosyakova, Y ., Rother, N., Zinn, S., Liebau, E., Gider, W., Schwanhäuser, S., &
Siegert, M. (2026). Exploring integration and migration dynamics: The research potentials
of a large-scale longitudinal household study of refugees in germany.European Sociologi-
cal Review,42(1), 146–163. https://doi.org/10.1093/esr/jcaf032
Brücker, H., Kroh, M., Bartsch, S., Goebel, J., Kühne, S., Liebau, E., Trübswetter, P., Tucci, I., &
Schupp, J. (2014).The new IAB-SOEP migration sample: An introduction into the method-
ology and the contents(Series C No. 216). SOEP Survey Papers.
Brucks, M., & Toubia, O. (2025). Prompt architecture induces methodological artifacts in large
language models.PLOS ONE,20(4), e0319159. https://doi.org/10.1371/journal.pone.031
9159
Chakraborty, I., Chiong, K., Dover, H., & Sudhir, K. (2025). Can AI and AI-Hybrids detect per-
suasion skills? salesforce hiring with conversational video interviews.Marketing Science,
44(1), 30–53. https://doi.org/10.1287/mksc.2023.0149
36

Cover, T. M., & Thomas, J. A. (2006).Elements of information theory(2nd ed.). Wiley-Interscience.
https://doi.org/10.1002/047174882X
Cui, Z., Li, N., & Zhou, H. (2025). A large-scale replication of scenario-based experiments in
psychology and management using large language models.Nature Computational Science,
5(8), 627–634. https://doi.org/10.1038/s43588-025-00840-7
Dominguez-Olmedo, R., Hardt, M., & Mendler-Dünner, C. (2024). Questioning the survey re-
sponses of large language models. In A. Globerson, L. Mackey, D. Belgrave, A. Fan, U.
Paquet, J. Tomczak, & C. Zhang (Eds.),Advances in neural information processing systems
(pp. 45850–45878, V ol. 37). Curran Associates, Inc. https://doi.org/10.52202/079017-1458
Gao, Y ., Lee, D., Burtch, G., & Fazelpour, S. (2025). Take caution in using LLMs as human
surrogates.Proceedings of the National Academy of Sciences,122(24), e2501660122. http
s://doi.org/10.1073/pnas.2501660122
Gemma Team, Google DeepMind. (2025). Gemma-4-26b-a4b model card [Hugging Face mirror:
https://huggingface.co/google/gemma-4-26B-A4B].
Goebel, J., Grabka, M. M., Liebig, S., Kroh, M., Richter, D., Schröder, C., & Schupp, J. (2019).
The German Socio-Economic Panel (SOEP).Jahrbücher für Nationalökonomie und Statis-
tik,239(2), 345–360. https://doi.org/10.1515/jbnst-2018-0022
Goli, A., & Singh, A. (2024). Frontiers: Can large language models capture human preferences?
Marketing Science,43(4), 709–722. https://doi.org/10.1287/mksc.2023.0306
Gupta, S., Shrivastava, V ., Deshpande, A., Kalyan, A., Clark, P., Sabharwal, A., & Khot, T. (2024).
Bias runs deep: Implicit reasoning biases in persona-assigned llms.International Confer-
ence on Learning Representations.
Hewitt, L., Ashokkumar, A., Ghezae, I., & Willer, R. (2024). Predicting results of social science
experiments using large language models.Preprint.
Kolluri, A., Wu, S., Park, J. S., & Bernstein, M. S. (2025, November). Finetuning LLMs for
human behavior prediction in social science experiments. In C. Christodoulopoulos, T.
Chakraborty, C. Rose, & V . Peng (Eds.),Proceedings of the 2025 conference on empir-
37

ical methods in natural language processing(pp. 30096–30111). Association for Compu-
tational Linguistics. https://doi.org/10.18653/v1/2025.emnlp-main.1530
Kozlowski, A. C., & Evans, J. (2025). Simulating subjects: The promise and peril of artificial
intelligence stand-ins for social agents and interactions.Sociological Methods & Research,
54(3), 1017–1073. https://doi.org/10.1177/00491241251337316
Leng, Y ., Sang, Y ., & Agarwal, A. (2024). Reducing disparity between llms and humans: Optimal
llm sample calibration.Available at SSRN 4802019. https://doi.org/10.2139/ssrn.4802019
Li, L., Chen, H., Namkoong, H., & Peng, T. (2025). Llm generated persona is a promise with a
catch. In D. Belgrave, C. Zhang, H. Lin, R. Pascanu, P. Koniusz, M. Ghassemi, & N. Chen
(Eds.),Advances in neural information processing systems(V ol. 38). Curran Associates,
Inc. https://proceedings.neurips.cc/paper_files/paper/2025/file/5fc150b75e8b509735564d
e16bc3527b-Paper-Position_Paper_Track.pdf
Li, P., Castelo, N., Katona, Z., & Sarvary, M. (2024). Frontiers: Determining the validity of large
language models for automated perceptual analysis.Marketing Science,43(2), 254–266.
https://doi.org/10.1287/mksc.2023.0454
Liu, A. H., Khandelwal, K., Subramanian, S., Jouault, V ., Rastogi, A., Sadé, A., Jeffares, A., Jiang,
A., Cahill, A., Gavaudan, A., et al. (2026). Ministral 3.arXiv preprint arXiv:2601.08584.
https://doi.org/10.48550/arXiv.2601.08584
Lyman, A., Hepner, B., Argyle, L. P., Busby, E. C., Gubler, J. R., & Wingate, D. (2025). Balancing
large language model alignment and algorithmic fidelity in social science research.Socio-
logical Methods and Research,54(3), 1110–1155. https://doi.org/10.1177/004912412513
42008
Mei, Q., Xie, Y ., Yuan, W., & Jackson, M. O. (2024). A Turing test of whether AI chatbots are
behaviorally similar to humans.Proceedings of the National Academy of Sciences,121(9),
e2313925121. https://doi.org/10.1073/pnas.2313925121
Motoki, F., Pinho Neto, V ., & Rodrigues, V . (2024). More human than human: Measuring ChatGPT
political bias.Public Choice,198(1), 3–23. https://doi.org/10.1007/s11127-023-01097-2
38

Orlikowski, M., Pei, J., Röttger, P., Cimiano, P., Jurgens, D., & Hovy, D. (2025, July). Beyond
demographics: Fine-tuning large language models to predict individuals’ subjective text
perceptions. In W. Che, J. Nabende, E. Shutova, & M. T. Pilehvar (Eds.),Proceedings of
the 63rd annual meeting of the association for computational linguistics (volume 1: Long
papers)(pp. 2092–2111). Association for Computational Linguistics. https://doi.org/10.18
653/v1/2025.acl-long.104
Park, J. S., Zou, C. Q., Kamphorst, J., Egan, N., Shaw, A., Hill, B. M., Cai, C., Morris, M. R.,
Liang, P., Willer, R., & Bernstein, M. S. (2026). Llm agents grounded in self-reports enable
general-purpose simulation of individuals. https://arxiv.org/abs/2411.10109
Park, P. S., Schoenegger, P., & Zhu, C. (2024). Diminished diversity-of-thought in a standard large
language model.Behavior Research Methods,56(6), 5754–5770. https://doi.org/10.3758/s
13428-023-02307-x
Peng, T., Gui, G., Brucks, M., Merlau, D. J., Fan, G. J., Sliman, M. B., Johnson, E. J., Althenayyan,
A., Bellezza, S., Donati, D., Fong, H., Friedman, E., Guevara, A., Hussein, M., Jerath, K.,
Kogut, B., Kumar, A., Lane, K., Li, H., . . . Toubia, O. (2025). Digital twins as funhouse
mirrors: Five key distortions. https://doi.org/10.48550/arXiv.2509.19088
Peres, R., Schreier, M., Schweidel, D., & Sorescu, A. (2023). On ChatGPT and beyond: How
generative artificial intelligence may affect research, teaching, and practice.International
Journal of Research in Marketing,40(2), 269–275. https://doi.org/10.1016/j.ijresmar.2023
.03.001
Petrov, N. B., Serapio-García, G., & Rentfrow, J. (2024). Limited ability of llms to simulate human
psychological behaviours: A psychometric analysis. https://doi.org/10.48550/arXiv.2405
.07248
Qwen Team. (2025). Qwen3 technical report. https://doi.org/10.48550/arXiv.2505.09388
Rozado, D. (2024). The political preferences of LLMs.PLOS ONE,19(7), e0306621. https://doi.o
rg/10.1371/journal.pone.0306621
39

Salecha, A., Ireland, M. E., Subrahmanya, S., Sedoc, J., Ungar, L. H., & Eichstaedt, J. C. (2024).
Large language models display human-like social desirability biases in Big Five personality
surveys.PNAS Nexus,3(12), pgae533. https://doi.org/10.1093/pnasnexus/pgae533
Santurkar, S., Durmus, E., Ladhak, F., Lee, C., Liang, P., & Hashimoto, T. (2023). Whose opin-
ions do language models reflect?Proceedings of the International Conference on Machine
Learning, 29971–30004.
Sarstedt, M., Adler, S. J., Rau, L., & Schmitt, B. (2024). Using large language models to generate
silicon samples in consumer and marketing research: Challenges, opportunities, and guide-
lines.Psychology & Marketing,41(6), 1254–1270. https://doi.org/10.1002/mar.21982
Schupp, J., & Gerlitz, J.-Y . (2008). Big five inventory-soep (bfi-s). https://doi.org/10.6102/zis54
Shannon, C. E. (1948). A mathematical theory of communication.The Bell System Technical Jour-
nal,27(3), 379–423. https://doi.org/10.1002/j.1538-7305.1948.tb01338.x
Snell, C., Lee, J., Xu, K., & Kumar, A. (2024). Scaling llm test-time compute optimally can be
more effective than scaling model parameters.arXiv preprint arXiv:2408.03314. https://do
i.org/10.48550/arXiv.2408.03314
Socio-Economic Panel. (2025). Socio-economic panel (SOEP), data for years 1984–2023, SOEP-
core v40, EU edition. https://doi.org/10.5684/soep.core.v40eu
Stromberg, M., Moe, W. W., Reutterer, T., & Schweidel, D. A. (2025). Blind spots in broad strokes:
Caveats for the use of llms in marketing research.Available at SSRN. https://doi.org/10.21
39/ssrn.5145114
Suh, J., Jahanparast, E., Moon, S., Kang, M., & Chang, S. (2025). Language model fine-tuning on
scaled survey data for predicting distributions of public opinions.Proceedings of the 63rd
Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
21147–21170. https://doi.org/10.18653/v1/2025.acl-long.1028
Toubia, O., Gui, G. Z., Peng, T., Merlau, D. J., Li, A., & Chen, H. (2025). Database report: Twin-
2k-500: A data set for building digital twins of over 2,000 people based on their answers to
40

over 500 questions.Marketing Science,44(6), 1446–1455. https://doi.org/10.1287/mksc.2
025.0262
Wang, M., Zhang, D. J., & Zhang, H. (2026). Large language models for market research: A data-
augmentation approach.Marketing Science. https://doi.org/10.1287/mksc.2025.0009
Wang, X., Ma, B., Hu, C., Weber-Genzel, L., Röttger, P., Kreuter, F., Hovy, D., & Plank, B. (2024).
“My Answer is C”: First-token probabilities do not match text answers in instruction-tuned
language models.Findings of the Association for Computational Linguistics: ACL 2024,
7407–7416. https://doi.org/10.18653/v1/2024.findings-acl.441
Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E. H., Le, Q. V ., & Zhou, D.
(2022). Chain-of-thought prompting elicits reasoning in large language models.Proceed-
ings of the 36th International Conference on Neural Information Processing Systems.
Westwood, S. J. (2025). The potential existential threat of large language models to online survey
research.Proceedings of the National Academy of Sciences,122(47), e2518075122. https:
//doi.org/10.1073/pnas.2518075122
White, C., Dooley, S., Roberts, M., Pal, A., Feuer, B., Jain, S., Shwartz-Ziv, R., Jain, N., Saifullah,
K., Dey, S., et al. (2025). Livebench: A challenging, contamination-limited llm benchmark.
International Conference on Learning Representations,2025, 91595–91631.
Yoo, K., Haenlein, M., & Hewett, K. (2025). A whole new world, a new fantastic point of view:
Charting unexplored territories in consumer research with generative artificial intelligence.
Journal of the Academy of Marketing Science,53(3), 723–759. https://doi.org/10.1007/s1
1747-025-01097-2
41
