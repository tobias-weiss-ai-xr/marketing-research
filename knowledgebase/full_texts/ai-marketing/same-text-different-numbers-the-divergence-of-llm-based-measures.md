---
title: 'Same Text, Different Numbers: The Divergence of LLM-Based Measures'
url: https://arxiv.org/abs/2609.31013
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Hamid Boustanifar
- Sasan Mansouri
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.31013
pages: 86
chars: 249525
fetched_at: '2026-11-08T13:24:14+00:00'
kb_version: 1
---

# Same Text, Different Numbers: The Divergence of LLM-Based Measures

Same Text, Different Numbers: The Divergence of
LLM-Based Measures ∗
Hamid Boustanifar† Sasan Mansouri‡
ABSTRACT
Researchers increasingly use generative large language models (LLMs) to convert corporate
text into empirical variables. We examine the extent to which LLM-based textual measures
are invariant to model choice using thirteen measures, including sentiment, management
clarity, uncertainty, answer specificity, and climate and political risk. Seven LLMs from
different providers score earnings call transcripts of S\&P 500 companies on these constructs.
Cross-model rank correlations average only 0.52, and transcript-level differences common
across providers account for only 34\% of total score variation. Cross-model disagreement
does not predict subsequent analyst or market disagreement, consistent with a substantial
model-specific component rather than common ambiguity in the underlying disclosure. Model
choice significantly affects downstream inference, with coefficient magnitudes, signs, and
statistical significance varying substantially across models. Averaging across providers makes
transcript rankings more stable for most constructs, but score levels remain sensitive to the
models included in the ensemble. LLM-generated variables should therefore be treated as
model-contingent measurements and validated across providers.
Keywords:Large language models; textual analysis; measurement invariance; construct
validity; corporate disclosure; reproducibility.
JEL Classification:C45, G14, G10, G12.
∗\mathrm{W}\mathrm{e} \mathrm{d}\mathrm{e}\mathrm{c}\mathrm{l}\mathrm{a}\mathrm{r}\mathrm{e} \mathrm{t}\mathrm{h}\mathrm{a}\mathrm{t} \mathrm{w}\mathrm{e} \mathrm{h}\mathrm{a}\mathrm{v}\mathrm{e} \mathrm{n}\mathrm{o} \mathrm{r}\mathrm{e}\mathrm{l}\mathrm{e}\mathrm{v}\mathrm{a}\mathrm{n}\mathrm{t} \mathrm{o}\mathrm{r} \mathrm{m}\mathrm{a}\mathrm{t}\mathrm{e}\mathrm{r}\mathrm{i}\mathrm{a}\mathrm{l} fi\mathrm{n}\mathrm{a}\mathrm{n}\mathrm{c}\mathrm{i}\mathrm{a}\mathrm{l} \mathrm{i}\mathrm{n}\mathrm{t}\mathrm{e}\mathrm{r}\mathrm{e}\mathrm{s}\mathrm{t}\mathrm{s} \mathrm{t}\mathrm{h}\mathrm{a}\mathrm{t} \mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{e} \mathrm{t}\mathrm{o} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{r}\mathrm{e}\mathrm{s}\mathrm{e}\mathrm{a}\mathrm{r}\mathrm{c}\mathrm{h} \mathrm{d}\mathrm{e}\mathrm{s}\mathrm{c}\mathrm{r}\mathrm{i}\mathrm{b}\mathrm{e}\mathrm{d}
\mathrm{i}\mathrm{n} \mathrm{t}\mathrm{h}\mathrm{i}\mathrm{s} \mathrm{p}\mathrm{a}\mathrm{p}\mathrm{e}\mathrm{r}. \mathrm{A}\mathrm{l}\mathrm{l} \mathrm{e}\mathrm{r}\mathrm{r}\mathrm{o}\mathrm{r}\mathrm{s} \mathrm{a}\mathrm{r}\mathrm{e} \mathrm{o}\mathrm{u}\mathrm{r} \mathrm{o}\mathrm{w}\mathrm{n}.
†\mathrm{E}\mathrm{D}\mathrm{H}\mathrm{E}\mathrm{C} \mathrm{B}\mathrm{u}\mathrm{s}\mathrm{i}\mathrm{n}\mathrm{e}\mathrm{s}\mathrm{s} \mathrm{S}\mathrm{c}\mathrm{h}\mathrm{o}\mathrm{o}\mathrm{l}, 393 \mathrm{P}\mathrm{r}\mathrm{o}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{a}\mathrm{d}\mathrm{e} \mathrm{d}\mathrm{e}\mathrm{s} \mathrm{A}\mathrm{n}\mathrm{g}\mathrm{l}\mathrm{a}\mathrm{i}\mathrm{s}, 06000 \mathrm{N}\mathrm{i}\mathrm{c}\mathrm{e}, \mathrm{F}\mathrm{r}\mathrm{a}\mathrm{n}\mathrm{c}\mathrm{e}. \mathrm{P}\mathrm{h}\mathrm{o}\mathrm{n}\mathrm{e}: +33 (0)4 93 18 3498.
\mathrm{E}\mathrm{m}\mathrm{a}\mathrm{i}\mathrm{l}:hamid.boustanifar@edhec.edu
‡\mathrm{U}\mathrm{n}\mathrm{i}\mathrm{v}\mathrm{e}\mathrm{r}\mathrm{s}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{o}\mathrm{f} \mathrm{G}\mathrm{r}\mathrm{o}\mathrm{n}\mathrm{i}\mathrm{n}\mathrm{g}\mathrm{e}\mathrm{n}, \mathrm{B}\mathrm{r}\mathrm{o}\mathrm{e}\mathrm{r}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{a}\mathrm{t} 5, 9712 \mathrm{C}\mathrm{P} \mathrm{G}\mathrm{r}\mathrm{o}\mathrm{n}\mathrm{i}\mathrm{n}\mathrm{g}\mathrm{e}\mathrm{n}, \mathrm{N}\mathrm{e}\mathrm{t}\mathrm{h}\mathrm{e}\mathrm{r}\mathrm{l}\mathrm{a}\mathrm{n}\mathrm{d}\mathrm{s}. \mathrm{P}\mathrm{h}\mathrm{o}\mathrm{n}\mathrm{e}: +31 (0) 6 23310677.
\mathrm{E}\mathrm{m}\mathrm{a}\mathrm{i}\mathrm{l}:s.mansouri@rug.nl
arXiv:2609.31013v1  [cs.AI]  25 Sep 2026

1 Introduction
Generative large language models (LLMs) are becoming measurement instruments in empirical
accounting and finance. 1 The attraction is clear: LLMs can perform classification and
evaluation tasks at scale that previously required extensive human coding or were infeasible.
In most applications, however, the output of a single selected model is treated as the empirical
measure, implicitly assuming that the choice of model does not materially affect the resulting
measurement.
We examine the extent to which LLM-based textual measures are invariant to model
choice across thirteen measures commonly used in the literature. Our setting focuses on
measurement rather than predictive applications of LLMs. Predictive applications ask models
to forecast outcomes such as returns, earnings, or price targets (Lopez-Lira and Tang, 2026;
Chen et al., 2023; Cao et al., 2024; Nagel et al., 2026) and therefore raise concerns about
training-data contamination and look-ahead bias (Sarkar and Vafa, 2025; Lopez-Lira et al.,
2025; Levy, 2026). Our tasks instead ask each model to characterize a fixed text using only
the information contained in it; there is no future outcome to forecast. Measurement is
therefore often viewed as a comparatively conservative use of LLMs in empirical research.
Consistent with this view, Cao et al. (2026) recommend mitigating concerns associated with
LLM-based prediction by using LLMs to ``extract or classify information and then plug those
outputs into conventional empirical models for prediction."" Our design examines whether
model choice remains consequential even in this recommended, measurement-focused use
case.
Our setting is the Q\&A section of 1,946 earnings conference calls held by S\&P 500 firms
during 2024. We ask seven models developed by different providers (OpenAI, Anthropic,
Google, Meta, Mistral, DeepSeek, and Alibaba) to evaluate the same transcripts. The
models receive identical construct definitions, numerical scales, and output instructions.
Each model returns a score, a self-reported confidence level, and a written justification.
1\mathrm{S}\mathrm{e}\mathrm{e} \mathrm{S}\mathrm{e}\mathrm{c}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} 2 \mathrm{f}\mathrm{o}\mathrm{r} \mathrm{a} \mathrm{n}\mathrm{o}\mathrm{n}-\mathrm{e}\mathrm{x}\mathrm{h}\mathrm{a}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{i}\mathrm{v}\mathrm{e} \mathrm{l}\mathrm{i}\mathrm{s}\mathrm{t} \mathrm{o}\mathrm{f} \mathrm{r}\mathrm{e}\mathrm{f}\mathrm{e}\mathrm{r}\mathrm{e}\mathrm{n}\mathrm{c}\mathrm{e}\mathrm{s}.
1

We study twelve constructs commonly examined in accounting and finance---sentiment,
uncertainty, management clarity, climate risk, political risk, answer specificity, and corporate
culture together with its five component dimensions---and an additional, explicitly rule-based
implementation of specificity. We select these constructs both because established non-LLM
measures are available, allowing us to assess their alignment with LLM-based measures, and
because their breadth allows us to examine heterogeneity in cross-model agreement across
measurement tasks. The design therefore produces thirteen measures of twelve constructs for
every transcript and model.
One feature of this design deserves emphasis at the outset. Our focus is on measurement
reliability, which is logically prior to validity: before asking whether an LLM-based measure
is correct, one must ask whether different models produce the same measure from the same
text. Cross-model disagreement is therefore informative regardless of which model, if any,
is closest to the ground truth, because it shows that the resulting variable depends on a
consequential but rarely motivated research choice---the choice of LLM.
We find substantial cross-model divergence. Across the thirteen measures, the mean
pairwise rank correlation between providers is only 0.52. Agreement is strongly construct
dependent. Sentiment has the highest mean pairwise correlation, at 0.85, followed by
innovation at 0.76. At the other end of the distribution, integrity has a mean correlation of
0.32, and the rule-based specificity ratio has a mean correlation of only 0.23. Thus, the same
providers that produce similar rankings for one construct can produce very different rankings
for another.
Differences in score levels are also economically large. The average within-call standard
deviation across providers is 0.75 times the overall standard deviation of the corresponding
measure. Hence, for the typical construct, variation across models evaluating the same
transcript is comparable to the cross-sectional variation that the measure is intended to
capture.
To investigate the sources of variation, we conduct a variance-components analysis that
2

separates variation common across providers at the transcript level from stable provider
calibration and provider-specific responses to individual transcripts. On average, the transcript
component accounts for 34.4\% of total score variation, the provider component for 33.4\%,
and the residual provider-by-transcript component for 32.2\%. The composition varies sharply
across constructs: the transcript component is 74\% for sentiment but only 13\% for integrity
and 4\% for the specificity ratio. Thus, on average, only about one-third of score variation
reflects transcript-level differences on which providers agree, with the remainder attributable to
systematic differences across providers or provider-specific responses to individual transcripts;
importantly, the extent of this model dependence varies substantially across constructs.
The rule-based specificity exercise helps distinguish ambiguity in a latent construct from
variation in how models implement an explicit scoring rule. In this exercise, the prompt
defines the relevant categories of specific language and instructs the model to count such
language and scale it by transcript length. Surprisingly, making the scoring rules and their
implementation more explicit leads, if anything, to greater rather than lower disagreement
across LLMs. Thus, cross-model disagreement cannot be attributed solely to ambiguity in
the underlying construct: even explicit scoring rules do not ensure consistent implementation
across models.
Several additional results help characterize the divergence. First, models' self-reported
confidence does not identify observations for which their scores are more dependable. Confi-
dence reports are tightly clustered, and restricting the sample to cases in which both models
report high confidence does not increase cross-model agreement. Second, agreement in
scores need not imply agreement in reasoning. The semantic similarity of providers' written
justifications is relatively low, even for sentiment (0.69), for which their numerical scores
are highly correlated. In some cases, models cite the same textual feature but map it into
opposite assessments of the construct. Third, observable firm and textual characteristics,
justification similarity, and construct, industry, and quarter fixed effects jointly account for
only 20\% of the variation in cross-provider dispersion. Disagreement is greater for larger and
3

higher-growth firms and for calls containing more forward-looking language, but most of the
variation in disagreement remains unexplained by standard observables.
We further ask whether cross-model disagreement reflects ambiguity in the underlying
disclosure that is also perceived by investors and analysts. We relate call-level LLM dispersion
to subsequent analyst forecast dispersion and forecast errors, as well as announcement-window
bid-ask spreads, trading volume, and return variance. LLM disagreement is not significantly
associated with any of these outcomes. Thus, the cross-model dispersion we document
does not appear to proxy for a broader form of disclosure ambiguity that also generates
disagreement among market participants, and is instead consistent with a substantial model-
specific component in LLM-based measurement.
We next compare the ensemble measures with established dictionary-based measures of
the corresponding constructs (Loughran and McDonald, 2011; Hassan et al., 2019; Sautner
et al., 2023; Hope et al., 2016; Li et al., 2021; Barth et al., 2023). The correlations are
positive but generally low, reaching a maximum of approximately 0.55 for corporate culture,
innovation, and specificity, but only about 0.3 for political risk and sentiment. 2 Together
with our earlier evidence of cross-provider disagreement, these results show that LLM-based
measures are neither interchangeable across providers nor simple substitutes for established
non-LLM measures of the same constructs. Moreover, strong agreement across LLMs does
not necessarily imply convergence with an established non-LLM operationalization, as the
sentiment results illustrate.
The preceding evidence raises a natural question: does this measurement dependence
matter for the empirical conclusions researchers draw from these measures? We examine
this question by estimating the relation between announcement returns and each provider's
version of a construct, holding the call sample, controls, and econometric specification fixed.
We find that model dependence can propagate into downstream inference, affecting the sign,
2\mathrm{W}\mathrm{e} \mathrm{n}\mathrm{o}\mathrm{t}\mathrm{e} \mathrm{t}\mathrm{h}\mathrm{a}\mathrm{t} \mathrm{t}\mathrm{r}\mathrm{a}\mathrm{d}\mathrm{i}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{a}\mathrm{l} \mathrm{m}\mathrm{e}\mathrm{a}\mathrm{s}\mathrm{u}\mathrm{r}\mathrm{e}\mathrm{s} \mathrm{a}\mathrm{r}\mathrm{e} \mathrm{a}\mathrm{l}\mathrm{t}\mathrm{e}\mathrm{r}\mathrm{n}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{v}\mathrm{e} \mathrm{o}\mathrm{p}\mathrm{e}\mathrm{r}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{a}\mathrm{l}\mathrm{i}\mathrm{z}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}, \mathrm{n}\mathrm{o}\mathrm{t} \mathrm{g}\mathrm{r}\mathrm{o}\mathrm{u}\mathrm{n}\mathrm{d} \mathrm{t}\mathrm{r}\mathrm{u}\mathrm{t}\mathrm{h}. \mathrm{O}\mathrm{u}\mathrm{r} \mathrm{a}\mathrm{r}\mathrm{g}\mathrm{u}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{t}
\mathrm{l}\mathrm{i}\mathrm{k}\mathrm{e}\mathrm{w}\mathrm{i}\mathrm{s}\mathrm{e} \mathrm{t}\mathrm{r}\mathrm{e}\mathrm{a}\mathrm{t}\mathrm{s} \mathrm{n}\mathrm{o} \mathrm{s}\mathrm{i}\mathrm{n}\mathrm{g}\mathrm{l}\mathrm{e} \mathrm{L}\mathrm{L}\mathrm{M} \mathrm{a}\mathrm{s} \mathrm{g}\mathrm{r}\mathrm{o}\mathrm{u}\mathrm{n}\mathrm{d} \mathrm{t}\mathrm{r}\mathrm{u}\mathrm{t}\mathrm{h}: \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{d}\mathrm{i}\mathrm{v}\mathrm{e}\mathrm{r}\mathrm{g}\mathrm{e}\mathrm{n}\mathrm{c}\mathrm{e} \mathrm{a}\mathrm{c}\mathrm{r}\mathrm{o}\mathrm{s}\mathrm{s} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}\mathrm{s} \mathrm{i}\mathrm{s} \mathrm{a} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{p}\mathrm{e}\mathrm{r}\mathrm{t}\mathrm{y} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{m}\mathrm{e}\mathrm{a}\mathrm{s}\mathrm{u}\mathrm{r}\mathrm{e}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{t}
\mathrm{i}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{t}, \mathrm{e}\mathrm{s}\mathrm{t}\mathrm{a}\mathrm{b}\mathrm{l}\mathrm{i}\mathrm{s}\mathrm{h}\mathrm{e}\mathrm{d} \mathrm{w}\mathrm{i}\mathrm{t}\mathrm{h}\mathrm{o}\mathrm{u}\mathrm{t} \mathrm{t}\mathrm{a}\mathrm{k}\mathrm{i}\mathrm{n}\mathrm{g} \mathrm{a} \mathrm{s}\mathrm{t}\mathrm{a}\mathrm{n}\mathrm{d} \mathrm{o}\mathrm{n} \mathrm{w}\mathrm{h}\mathrm{i}\mathrm{c}\mathrm{h} \mathrm{o}\mathrm{p}\mathrm{e}\mathrm{r}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{a}\mathrm{l}\mathrm{i}\mathrm{z}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{i}\mathrm{s} \mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{c}\mathrm{t}.
4

magnitude, and statistical significance of estimated relations. For sentiment and uncertainty,
the signs and statistical significance of the estimated relations are stable across providers,
although their magnitudes vary by up to 60\%. For other measures, model choice can also
alter the sign and statistical significance of the estimated relation. We also find differences in
the signs, magnitudes, and statistical significance of coefficients estimated using LLM-based
versus traditional measures. Thus, researchers analyzing the same transcripts using the
same regression specification can reach different conclusions depending on the LLM used to
construct the measure and, more broadly, on how the underlying construct is operationalized.
Given these consequences of model dependence, we next ask whether aggregating across
providers can mitigate it. Following generalizability theory (Brennan, 2001), we distinguish
reliability for relative decisions---whether the ensemble consistently ranks transcripts---from
dependability for absolute decisions---whether score levels remain stable when models are
treated as draws from a broader population of possible providers. Using 0.80 as a demanding
conventional benchmark, the seven-provider ensemble meets the relative-reliability threshold
for ten of thirteen measures, but the absolute-dependability threshold for only five. Thus,
averaging across providers substantially improves the stability of relative rankings for most
measures, but is less effective at stabilizing absolute score levels.
Finally, we find that moving to newer, frontier models narrows cross-model disagreement
but does not resolve it---a substantial gap remains, both among LLMs and between LLM-based
and traditional measures.
2 Related Literature
A recent but rapidly growing literature in accounting and finance uses LLMs as measurement
instruments. The underlying research design is increasingly familiar: a researcher provides a
selected model with a fixed body of text and instructions to evaluate a construct and then
treats the model's numerical or categorical response as an empirical variable. Applications
5

differ in the model selected, the text analyzed, and the construct measured. For example,
Shaffer and Wang (2026) use GPT-4o to extract and classify unusual gains and losses from
10-K filings and construct a measure of core earnings. Bernard et al. (2026) use a GPT model
to measure business complexity from 10-K footnotes, while He et al. (2025) use Google's
Gemini to classify the intensity of customer-capital investment from sales and marketing
discussions in Items 1 and 7 of 10-K filings. Using other corporate texts, Li et al. (2026)
employ GPT-4o-mini to identify culture types, tone, and cause--effect relations in analyst
reports, earnings-call transcripts, and employee reviews; Jia et al. (2026) use ChatGPT-4 to
determine whether conference-call discussions describe substantive generative-AI initiatives
rather than merely mention the technology; and Iacoviello and Tong (2026) use GPT-4o-mini
to score the geopolitical-risk intensity of newspaper articles. Other applications use LLMs to
measure managers' anticipated policies (Jha et al., 2025), political speech (Ottonello et al.,
2024), non-answers in earnings conference calls (de Kok, 2025), workplace psychological safety
(Boustanifar and Sheykhi, 2026), central-bank policy stance (Hansen and Kazinnik, 2024),
and information revealed in executives' conference-call answers (Bai et al., 2025).
These studies illustrate a common empirical practice: researchers select an LLM, provide
it with text and a measurement task, and use the resulting output as data. This practice
raises the question at the center of our paper: whether another model given the same text and
instructions would produce an interchangeable empirical measure. The issue is also relevant
when LLMs are used to validate classifications produced by traditional textual methods (e.g.,
Abraham et al., 2024; Andreou et al., 2026; Boustanifar and Schwarz, 2026), because the
apparent validation then depends on the properties of the selected LLM benchmark.
Recent methodological work examines several related dimensions of LLM-based measure-
ment. Asirvatham et al. (2026) treat LLM outputs as noisy measurements of latent constructs
and show that a single model can closely match human coders. We complement this work
by showing that independently developed models often disagree when applied to the same
text. Wang and Wang (2025) study reproducibility across repeated realizations from the
6

same model and show that averaging repeated runs can improve consistency. Ludwig et al.
(2026) develop an econometric framework for using LLM outputs as generated regressors.
They note that theoretically such choices---which model, which prompt---can move parameter
estimates, and propose combining LLM outputs with a small validation sample as the fix; we
instead document this model dependence systematically, across thirteen measures and seven
independent developers in a measurement-only setting, and trace where it originates.
The contemporaneous study most closely related to ours is Cookson et al. (2026), who
conceptualize LLM-generated variables as subject to systematic measurement error arising
from how models transform source text. Although we share a similar setting---direct-
prompt construct ratings of S\&P 500 disclosures---the two studies examine distinct sources of
measurement error: a model can faithfully preserve the information in the source text (their
focus) yet operationalize the same construct differently from another model (ours).
To sum up, our contribution is therefore to identify model choice as a distinct dimension of
LLM-based measurement design. Our study differs from a comparison of alternative prompts
or repeated draws from one model: we hold the transcript, construct definition, prompt,
numerical scale, and inference settings fixed while varying the model used to construct the
variable. Moreover, rather than studying a single measurement task, we examine thirteen
measures spanning a broad set of constructs. This breadth allows us to study whether model
dependence varies systematically across the constructs researchers ask LLMs to measure.
We further examine whether explicit rule-based instructions reduce cross-model variation,
whether aggregation across providers produces measures sufficiently reliable for relative
and absolute empirical uses, and how LLM-based measures relate to established non-LLM
operationalizations. Together, these analyses isolate model choice from other sources of
variation in LLM-based measurement. Importantly, this contribution does not depend on
identifying a ""correct"" model. Our design isolates whether the measure is invariant to model
choice---a reliability property---leaving open the separate validity question of which model
best recovers the construct. The two are complementary: cross-model agreement is necessary
7

but not sufficient for validity, and a validation exercise against human coding would identify
the best provider without overturning our central point that the choice matters.
Our analysis also complements research on model-induced ``non-standard errors"" in AI-
assisted empirical analysis (Gao and Xiao, 2026; Huang et al., 2026). Whereas that work
examines variation generated when AI agents execute broader research tasks, we isolate an
earlier stage of the empirical process: the construction of a variable from fixed source material.
Our setting also differs from studies that deliberately use dispersion in LLM forecasts or
persona-conditioned responses to measure heterogeneous beliefs (Liu et al., 2026; Bhagwat
et al., 2026). In those settings, disagreement is itself informative about the economic object
of interest. In ours, the models are intended to serve as alternative instruments for measuring
the same fixed text. Cross-model disagreement is therefore a property of the measurement
procedure to be diagnosed rather than the economic object the procedure is designed to
recover.
3 Data
3.1 Sample
Our sample is the set of earnings conference calls held by S\&P 500 constituents during 2024.
We obtain call transcripts from S\&P Capital IQ and retain the question-and-answer (Q\&A)
portion of each call, in which analysts question management and management responds
without a prepared script. After requiring firms to be index members on the call date and to
have the financial data described below, the final sample comprises 1,946 calls by 501 firms.
The unit of analysis is the text of management's answers, which average roughly 3,900 words
per call.
8

3.2 LLM-based textual measures
As of November 2025, we select one cost-efficient, API-accessible model from each of seven
independently developed model families: OpenAI's GPT, Anthropic's Claude, Google's
Gemini, Meta's Llama, Mistral, DeepSeek, and Alibaba's Qwen. The selected models include
both proprietary, closed-weight models, such as GPT and Claude, and open-weight models,
such as Llama and DeepSeek. 3
Our focus on cost-efficient models reflects how LLM-based measurement is conducted
at scale. Scoring our sample requires hundreds of thousands of model queries, and applied
research of this scope generally relies on affordable, high-throughput models. Moreover, the
models we use are at least as capable as those employed in the studies cited earlier in the
introduction and literature review sections. Our evidence therefore bears directly on the
existing body of LLM-based measures. We query each model through its API using a fixed
prompt, a temperature of 0, and no external tools, retrieval, or scaffolding. This design
isolates the contribution of the model itself from that of any surrounding system and matches
the API-based pipeline that the literature relies on to construct LLM-derived measures (see
the citations in Section 2).
We use each model to read every transcript and assign scores for twelve constructs
commonly examined in the accounting and finance literature. These constructs are sentiment,
uncertainty, management clarity, climate risk, political risk, answer specificity, and corporate
culture, together with its five underlying dimensions: innovation, integrity, quality, respect,
and teamwork.
Each prompt follows a common structure. It instructs the model to act as an analyst
tasked with quantifying a particular construct, such as sentiment, from a passage of text.
The model is instructed to base its assessment exclusively on the supplied text, without
relying on external knowledge or assumptions. The prompt then provides a definition of the
construct---for example, sentiment captures the overall positivity versus negativity expressed
3\mathrm{D}\mathrm{e}\mathrm{t}\mathrm{a}\mathrm{i}\mathrm{l}\mathrm{s} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{m}\mathrm{o}\mathrm{d}\mathrm{e}\mathrm{l}\mathrm{s} \mathrm{a}\mathrm{r}\mathrm{e} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{d} \mathrm{i}\mathrm{n} \mathrm{A}\mathrm{p}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{d}\mathrm{i}\mathrm{x} \mathrm{E}.
9

in the text---and specifies its numerical scale, such as  - 1 to +1. Finally, it requires a
structured output containing the construct score, the model's confidence in that score, and a
brief justification based on specific language in the text. The complete prompts used for each
construct are provided in Appendix F.
Because specificity has a relatively narrow definition---namely, whether the text contains
any of seven categories of specific information: names of persons, organizations, percentages,
locations, dates, monetary values, and durations (Hope et al., 2016)---we also construct an
alternative measure of specificity. To do so, we directly prompt the LLMs to count the number
of specific words and then compute a specificity ratio, defined as the number of specific words
divided by the total number of words. In other words, this is a precisely defined task for
which we specify both the underlying concept and the rule used to compute the measure. One
would therefore expect this measure to exhibit the highest level of agreement across models,
making it a useful setting in which to analyze model disagreement on a clearly defined task.
We refer to this measure asSpecificity Ratio, whereas the more general specificity measure is
referred to asSpecificity.
Accordingly, we obtain 13 measures across the 12 constructs. Each model receives an
identical prompt for each construct and returns a numerical score, a self-reported confidence
score, and a brief written justification for its assessment. 4 We hold the set of models fixed
across all calls, such that the same seven models evaluate the same texts. Consequently, any
disagreement among them reflects differences across models rather than differences in model
coverage.5
Two further steps precede the analysis. First, as with the financial variables, we winsorize
4\mathrm{T}\mathrm{h}\mathrm{e} \mathrm{a}\mathrm{g}\mathrm{g}\mathrm{r}\mathrm{e}\mathrm{g}\mathrm{a}\mathrm{t}\mathrm{e} \mathrm{c}\mathrm{u}\mathrm{l}\mathrm{t}\mathrm{u}\mathrm{r}\mathrm{e} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{t}\mathrm{h}\mathrm{e} fi\mathrm{v}\mathrm{e} \mathrm{c}\mathrm{u}\mathrm{l}\mathrm{t}\mathrm{u}\mathrm{r}\mathrm{e} \mathrm{d}\mathrm{i}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{s}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s} \mathrm{s}\mathrm{h}\mathrm{a}\mathrm{r}\mathrm{e} \mathrm{o}\mathrm{n}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{n}fi\mathrm{d}\mathrm{e}\mathrm{n}\mathrm{c}\mathrm{e} \mathrm{a}\mathrm{s}\mathrm{s}\mathrm{e}\mathrm{s}\mathrm{s}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{t} \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{o}\mathrm{n}\mathrm{e}
\mathrm{j}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{i}fi\mathrm{c}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{s}\mathrm{i}\mathrm{n}\mathrm{c}\mathrm{e} \mathrm{t}\mathrm{h}\mathrm{e}\mathrm{y} \mathrm{a}\mathrm{r}\mathrm{e} \mathrm{p}\mathrm{a}\mathrm{r}\mathrm{t} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{a}\mathrm{m}\mathrm{e} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{m}\mathrm{p}\mathrm{t}.
5\mathrm{E}\mathrm{v}\mathrm{e}\mathrm{r}\mathrm{y} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l} \mathrm{r}\mathrm{e}\mathrm{c}\mathrm{e}\mathrm{i}\mathrm{v}\mathrm{e}\mathrm{d} \mathrm{a} \mathrm{r}\mathrm{e}\mathrm{s}\mathrm{p}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{e} \mathrm{f}\mathrm{r}\mathrm{o}\mathrm{m} \mathrm{e}\mathrm{v}\mathrm{e}\mathrm{r}\mathrm{y} \mathrm{m}\mathrm{o}\mathrm{d}\mathrm{e}\mathrm{l} \mathrm{f}\mathrm{o}\mathrm{r} \mathrm{e}\mathrm{v}\mathrm{e}\mathrm{r}\mathrm{y} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{m}\mathrm{p}\mathrm{t}. \mathrm{W}\mathrm{e} \mathrm{p}\mathrm{a}\mathrm{r}\mathrm{s}\mathrm{e} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{n}\mathrm{u}\mathrm{m}\mathrm{e}\mathrm{r}\mathrm{i}\mathrm{c}\mathrm{a}\mathrm{l} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}
\mathrm{f}\mathrm{r}\mathrm{o}\mathrm{m} \mathrm{e}\mathrm{a}\mathrm{c}\mathrm{h} \mathrm{r}\mathrm{e}\mathrm{s}\mathrm{p}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{e}. \mathrm{O}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} 177,086 \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}\mathrm{s} \mathrm{r}\mathrm{e}\mathrm{q}\mathrm{u}\mathrm{e}\mathrm{s}\mathrm{t}\mathrm{e}\mathrm{d} (\mathrm{s}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{n} \mathrm{m}\mathrm{o}\mathrm{d}\mathrm{e}\mathrm{l}\mathrm{s}, 13 \mathrm{m}\mathrm{e}\mathrm{a}\mathrm{s}\mathrm{u}\mathrm{r}\mathrm{e}\mathrm{s}, 1,946 \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l}\mathrm{s}), 98 (0.06\%)
\mathrm{c}\mathrm{o}\mathrm{u}\mathrm{l}\mathrm{d} \mathrm{n}\mathrm{o}\mathrm{t} \mathrm{b}\mathrm{e} \mathrm{p}\mathrm{a}\mathrm{r}\mathrm{s}\mathrm{e}\mathrm{d}, \mathrm{n}\mathrm{a}\mathrm{m}\mathrm{e}\mathrm{l}\mathrm{y} 68 \mathrm{L}\mathrm{l}\mathrm{a}\mathrm{m}\mathrm{a} \mathrm{s}\mathrm{p}\mathrm{e}\mathrm{c}\mathrm{i}fi\mathrm{c}\mathrm{i}\mathrm{t}\mathrm{y}-\mathrm{r}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o} \mathrm{r}\mathrm{e}\mathrm{s}\mathrm{p}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{e}\mathrm{s} \mathrm{c}\mathrm{u}\mathrm{t} \mathrm{o}ff \mathrm{a}\mathrm{t} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{o}\mathrm{u}\mathrm{t}\mathrm{p}\mathrm{u}\mathrm{t}-\mathrm{t}\mathrm{o}\mathrm{k}\mathrm{e}\mathrm{n} \mathrm{l}\mathrm{i}\mathrm{m}\mathrm{i}\mathrm{t} \mathrm{a}\mathrm{n}\mathrm{d} 30
\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{p}\mathrm{o}\mathrm{r}\mathrm{a}\mathrm{t}\mathrm{e}-\mathrm{c}\mathrm{u}\mathrm{l}\mathrm{t}\mathrm{u}\mathrm{r}\mathrm{e} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}\mathrm{s} (\mathrm{t}\mathrm{h}\mathrm{e} \mathrm{o}\mathrm{v}\mathrm{e}\mathrm{r}\mathrm{a}\mathrm{l}\mathrm{l} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{o}\mathrm{r} \mathrm{o}\mathrm{n}\mathrm{e} \mathrm{o}\mathrm{f} \mathrm{i}\mathrm{t}\mathrm{s} \mathrm{d}\mathrm{i}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{s}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}) \mathrm{f}\mathrm{r}\mathrm{o}\mathrm{m} \mathrm{M}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{l} \mathrm{r}\mathrm{e}\mathrm{s}\mathrm{p}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{e}\mathrm{s} \mathrm{t}\mathrm{h}\mathrm{a}\mathrm{t} \mathrm{d}\mathrm{e}\mathrm{g}\mathrm{e}\mathrm{n}\mathrm{e}\mathrm{r}\mathrm{a}\mathrm{t}\mathrm{e}\mathrm{d}
\mathrm{i}\mathrm{n}\mathrm{t}\mathrm{o} \mathrm{a} \mathrm{r}\mathrm{e}\mathrm{p}\mathrm{e}\mathrm{t}\mathrm{i}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{l}\mathrm{o}\mathrm{o}\mathrm{p}; \mathrm{t}\mathrm{h}\mathrm{e}\mathrm{s}\mathrm{e} \mathrm{a}\mathrm{r}\mathrm{e} \mathrm{t}\mathrm{r}\mathrm{e}\mathrm{a}\mathrm{t}\mathrm{e}\mathrm{d} \mathrm{a}\mathrm{s} \mathrm{m}\mathrm{i}\mathrm{s}\mathrm{s}\mathrm{i}\mathrm{n}\mathrm{g}. \mathrm{N}\mathrm{o} \mathrm{p}\mathrm{a}\mathrm{r}\mathrm{s}\mathrm{e}\mathrm{d} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{f}\mathrm{a}\mathrm{l}\mathrm{l}\mathrm{s} \mathrm{o}\mathrm{u}\mathrm{t}\mathrm{s}\mathrm{i}\mathrm{d}\mathrm{e} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{a}\mathrm{d}\mathrm{m}\mathrm{i}\mathrm{s}\mathrm{s}\mathrm{i}\mathrm{b}\mathrm{l}\mathrm{e} \mathrm{r}\mathrm{a}\mathrm{n}\mathrm{g}\mathrm{e}. \mathrm{T}\mathrm{h}\mathrm{e}
\mathrm{n}\mathrm{u}\mathrm{m}\mathrm{b}\mathrm{e}\mathrm{r} \mathrm{o}\mathrm{f} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l}\mathrm{s} \mathrm{w}\mathrm{i}\mathrm{t}\mathrm{h} \mathrm{a} \mathrm{v}\mathrm{a}\mathrm{l}\mathrm{i}\mathrm{d} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{f}\mathrm{r}\mathrm{o}\mathrm{m} \mathrm{a}\mathrm{l}\mathrm{l} \mathrm{s}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{n} \mathrm{m}\mathrm{o}\mathrm{d}\mathrm{e}\mathrm{l}\mathrm{s} \mathrm{t}\mathrm{h}\mathrm{e}\mathrm{r}\mathrm{e}\mathrm{f}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{r}\mathrm{a}\mathrm{n}\mathrm{g}\mathrm{e}\mathrm{s} \mathrm{f}\mathrm{r}\mathrm{o}\mathrm{m} 1,878 (\mathrm{s}\mathrm{p}\mathrm{e}\mathrm{c}\mathrm{i}fi\mathrm{c}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{r}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}) \mathrm{t}\mathrm{o}
1,946, \mathrm{a}\mathrm{s} \mathrm{r}\mathrm{e}\mathrm{p}\mathrm{o}\mathrm{r}\mathrm{t}\mathrm{e}\mathrm{d} \mathrm{i}\mathrm{n} \mathrm{t}\mathrm{h}\mathrm{e}N\mathrm{c}\mathrm{o}\mathrm{l}\mathrm{u}\mathrm{m}\mathrm{n} \mathrm{o}\mathrm{f} \mathrm{T}\mathrm{a}\mathrm{b}\mathrm{l}\mathrm{e} 2.
10

each provider's scores for each construct at the 1st and 99th percentiles (1,324 of the 176,988
parsed scores). The standardized scores used below divide by a provider's own standard
deviation, so on a provider whose scores are tightly clustered a single in-range answer would
otherwise register as an outlier of 20 to 40 standard deviations. Second, the winsorized sample
reveals a form of divergence that precedes any disagreement about levels: two of the seven
models, Anthropic and Qwen, assign a political-risk score of exactly 0.00 to more than 99\%
of the calls, following the prompt's instruction to return 0.00 absent an explicit reference,
whereas the other five find some political-risk exposure in 12\% to 42\% of the same calls.
The two models effectively read the construct as absent from the corpus. Their political-risk
series carry no cross-sectional information, and to be conservative, we exclude them from
all analyses. So political risk is measured with the remaining five providers; every other
construct is measured with all seven.
For each construct, we use the seven series generated by the seven LLMs to construct
measures of LLM dispersion. For example, for sentiment, we have seven sentiment series, one
from each LLM, for the same set of firm-level observations. Because the models use different
scales, we first standardize each model's score series for each construct to have mean zero
and standard deviation one, and defineLLM Dispersion (Z)as the standard deviation across
the seven standardized LLM scores for a given observation and construct. Higher values
indicate greater disagreement across LLMs in assessing the same text for a given construct.
The Online Appendix repeats the main dispersion analysis with the range (maximum minus
minimum) of the standardized scores in place of their standard deviation.
3.3 Traditional textual measures
The constructs we measure are not only economically important, but also commonly measured
in the literature using traditional text-based methods, typically dictionary-based or rule-
based approaches. Including these traditional measures is important because they provide
a benchmark for each construct based on the methods currently used in the literature.
11

Importantly, determining which method captures the ``true"" construct is outside the scope
of our study. Instead, our objective is to examine the extent of agreement or disagreement
across different measurement approaches.
For each construct, we follow the word lists and methods from the original papers to
construct a non-LLM benchmark. Sentiment and uncertainty are based on the word lists of
Loughran and McDonald (2011). Sentiment is measured as the number of positive words
minus the number of negative words, scaled by the total number of words. Uncertainty is
measured as the number of uncertainty-related words divided by the total number of words.
Management clarity follows Barth et al. (2023). We count the number of trigrams that
appear in the evasive-language glossary and scale this count by the total number of words.
We then multiply the measure by (-1), so that higher values correspond to greater clarity.
Climate risk follows Sautner et al. (2023) and is measured as the relative frequency of
climate-related bigrams in the call. Firm-level political risk follows Hassan et al. (2019);
we use their political-exposure measure, computed as the weighted frequency of political
bigrams in the text---each political bigram weighted by its frequency in their political training
library---scaled by the total number of bigrams.
Answer specificity follows Hope et al. (2016). We measure specificity as the number of
specific terms belonging to seven categories---persons, locations, organizations, percentages,
monetary values, dates, and durations---divided by the total number of words. Finally, the
five dimensions of corporate culture, as well as the aggregate culture measure, follow Li et al.
(2021). For each culture dimension, we compute the term frequency of that dimension's word
list divided by the total number of words. The aggregate culture score is the average of the
five dimension-level scores.
As control variables in some regressions, we also use additional textual measures: read-
ability (Li, 2008), linguistic complexity (Loughran and McDonald, 2024), and the intensity of
forward-looking language (Bozanic et al., 2018).
12

3.4 Financial data and outcomes
We match each call to financial and market data through standard identifier links. From
Compustat we construct firm size, book-to-market, and Tobin's Q; from IBES we obtain
analyst earnings-forecast dispersion and coverage and the standardized earnings surprise.
Using CRSP returns, we estimate cumulative abnormal returns (CARs) around each call
from Fama--French three-factor and Carhart four-factor models, and we construct a battery
of post-call market-disagreement measures---abnormal bid-ask spreads, trading volume, and
return variance. The primary outcome variable in the return regressions is the four-factor
announcement CAR over the (0 , 1) window. Table 1 reports summary statistics for the
variables used in the main analyses; per-construct summary statistics of the individual
providers' LLM scores are reported in the Online Appendix (Table OA.B.1).
[Insert Table 1 about here]
4 Empirical analysis
We organize the empirical analysis around three broad objectives. First, we characterize
the extent and nature of disagreement across LLM-based measures. Second, we investigate
the sources and interpretation of that disagreement, including whether it reflects observable
characteristics, disclosure ambiguity perceived by market participants, or differences in model
knowledge cutoffs. Third, we examine its implications for empirical research by comparing
LLM measures with traditional textual measures, evaluating the sensitivity of downstream
inference to model choice, and assessing whether aggregation across providers improves
measurement reliability.
These questions are important because LLMs are increasingly used to transform unstruc-
tured text into quantitative variables, yet researchers often treat model-generated measures as
if they were objective and interchangeable. By studying agreement across models, the sources
of disagreement, and the relation between LLM-based and traditional measures, we provide
13

evidence on whether and to what extent the LLM-generated textual measures are reliable,
whether they are model-dependent, and how they compare with established approaches in
accounting and finance research.
4.1 Agreement across models
We begin by comparing the distribution of scores across providers for each construct and
computing pairwise correlations among the seven models. We also analyze the similarity
of the justifications that LLMs provide for their scores. Finally, we conduct a principal
components analysis to assess the degree of commonality across model-generated score series.
4.1.1 Correlations across LLM scores
Figure 1 presents correlation heatmaps across models for four illustrative constructs: the two
with the highest average pairwise correlation---sentiment and innovation---and the two with
the lowest---integrity and the specificity ratio. The Online Appendix (Appendix A) presents
the full set of heatmaps for all constructs. In each heatmap, the upper triangle reports
Pearson correlations, while the lower triangle reports Spearman correlations. Reporting both
correlations is useful because they capture different forms of agreement: Pearson correlations
measure the extent to which models' scores move together linearly, whereas Spearman
correlations measure whether models produce similar rankings of observations. Thus, the
two measures allow us to distinguish linear agreement in scores from agreement in relative
ordering. To summarize this information compactly, Table 2 reports, for each construct,
the distribution (minimum, mean, median, and maximum) of the 21 pairwise Spearman
correlations among the seven models.
[Insert Figure 1 about here]
The correlations vary substantially across constructs, suggesting that inter-model agree-
ment is construct dependent. Averaged across constructs, the mean pairwise correlation is
14

0.52. Agreement is highest for sentiment, with a mean pairwise correlation of 0.85, making
it the only construct on which the models substantially agree. Agreement is lowest for the
specificity ratio, with a mean pairwise correlation of only 0.23, followed by integrity, with a
mean correlation of 0.32. The Pearson correlations are broadly in line with the Spearman
correlations, suggesting that the main patterns are not driven by nonlinearities or outliers.
[Insert Table 2 about here]
Even when model scores are positively correlated, they can differ substantially in levels.
To quantify this, for each construct we compare the average within-call standard deviation of
the seven raw model scores with the overall standard deviation of that construct's scores,
pooled across calls and providers. Across the thirteen constructs, this ratio averages 0.75:
the typical dispersion across models scoring thesamecall is about three-quarters of the total
variation of the measure across calls. The ratio ranges from 0.42 for political risk, 0.44 for
climate risk, and 0.48 for sentiment to above 0.9 for uncertainty (0.91), integrity (0.95), and
the specificity ratio (0.97), where nearly all of the variation in a score reflects which model
produced it rather than which call was scored. This implies that the choice of LLM provider
can meaningfully affect a firm's measured score, with model-driven variation comparable in
magnitude to economically relevant variation across firms.
The models also report a confidence level with every score, which provides a natural
internal check: if disagreement arose mainly where models are unsure, agreement should be
higher on calls where models are mutually confident. It is not. Self-reported confidence is
tightly clustered (about 30\% of all scores carry a confidence of exactly 0.80), and conditioning
on both models in a pair being confidentlowersrather than raises the average pairwise
correlation---from 0.52 to 0.48 when both models are at or above their own median confidence,
falling monotonically to 0.33 as the definition of high confidence tightens; see Appendix D.
Models' confidence is also essentially uninformative about their own deviation from the
consensus. Thus, LLM disagreement is not concentrated in responses the models themselves
flag as uncertain, no matter where the confidence threshold is drawn.
15

4.1.2 Correlations of LLMs and traditional measures
Another important empirical question is how strongly LLM-based measures correlate with the
traditional measures described in Section 3, which are widely used in the literature. The last
row of Figure 1 reports the correlation between the non-LLM measure and each LLM-based
measure for the selected constructs. The Online Appendix (Appendix A) presents the full set
of heatmaps for all constructs. As shown, the correlations range from very low to moderately
positive and vary substantially across constructs.
To provide more concise summary statistics, we correlate the seven-model average LLM
score with the corresponding non-LLM benchmark. Alignment is highest for corporate
culture (Spearman rank correlation of 0.56), innovation (0.55), specificity (0.55), and climate-
change exposure (0.47). Although these correlations are already relatively low, alignment is
considerably weaker for the remaining constructs. Notably, this pattern extends to sentiment:
the ensemble LLM sentiment score has a correlation of only 0.29 with dictionary-based tone,
even though sentiment is the construct on which the models agree most strongly with one
another. As shown in Figure 1, the correlations between the sentiment scores produced by the
different LLMs and the non-LLM sentiment measure are quite similar, ranging from 0.25 to
0.30. Political risk as measured by LLMs aligns similarly weakly with the measure developed
by Hassan et al. (2019) (0.29), while management clarity exhibits the weakest alignment of
all (0.13). The corresponding Pearson correlations are very similar.
Two implications follow. First, LLM-based and traditional measures are not empirically
interchangeable; substituting one for the other can materially change the resulting empirical
variable. Second, strong inter-model agreement does not imply agreement with the traditional
operationalization of the same construct. Sentiment provides the clearest example, combining
the highest cross-model correlation (0.85) with one of the lowest correlations with its dictionary-
based counterpart.
16

4.1.3 Similarity of justifications
As part of the prompt, we ask each LLM to provide a brief justification for its score for each
construct. This feature allows us to examine whether similarities or differences in numerical
scores are accompanied by similarities or differences in the models' stated rationales. Similar
scores need not imply that models rely on the same aspects of the text, and different
scores need not imply entirely different interpretations. For example, models may focus
on similar textual features but map those features into different numerical scores, or they
may assign similar scores while emphasizing different parts of the text. To assess these
possibilities, we measure the similarity of justifications across models using both cosine
similarity and Jaccard similarity. Cosine similarity captures semantic similarity based on
vector representations, allowing two justifications to be similar even when they use different
words. Jaccard similarity, by contrast, is based on word overlap and therefore captures the
extent to which two justifications rely on the same vocabulary.
Subfigures (b) in the Online Appendix (Appendix A) present the average similarity
in justifications across models, separately for each construct. The similarities between
justifications are generally low under either metric: across constructs, the average cosine
similarity across all models ranges from 0.41 (specificity ratio) to 0.73 (political risk), and
the average Jaccard word overlap from 0.15 to 0.31. Importantly, this pattern holds even
for constructs such as sentiment, for which correlations across model scores are relatively
high. For example, for sentiment, the average cosine similarity across models is only 0.69.
Although this value is not close to zero, it indicates only moderate semantic overlap in model
justifications. This is notable because the justifications are generated for the same text, the
same construct, and the same prompt. Thus, even when models produce relatively similar
numerical scores, their stated rationales exhibit substantial heterogeneity. More broadly,
agreement in LLM-generated scores can mask meaningful heterogeneity in how different
models interpret the same text and which textual features they emphasize.
The reverse pattern---similar reasoning mapped into very different scores---also occurs, and
17

a concrete example illustrates it. In Best Buy's November 2024 earnings call, management
discussed the potential impact of import tariffs. OpenAI assigns a political-risk score of 0.75
and justifies it with precisely this discussion, citing that ``tariffs are very complex"" and that
``higher prices are not helpful."" Qwen assigns a score of 0.00 to the same text while explicitly
acknowledging the same passages: its justification notes that ``the discussion primarily revolves
around supply chain management, tariffs, and promotional strategies,"" yet concludes that
this does not indicate any significant political-risk exposure. The remaining providers span
nearly the full range in between (0.00 to 0.70). The two models at the extremes identify
the same textual feature; they disagree about whether that feature constitutes political risk.
Disagreement of this kind cannot be attributed to one model overlooking information in the
text---it reflects different implicit definitions of the construct itself.
4.1.4 Principal component analysis
We next use principal components analysis to provide a complementary summary of inter-
model agreement. The preceding analyses document that pairwise correlations across LLM
scores are often modest and that the models' stated justifications also exhibit limited similarity.
PCA does not replace these analyses; rather, it asks a related but more aggregate question.
If the seven LLMs are all measuring the same underlying construct, with differences across
providers reflecting mostly idiosyncratic noise, then their scores should contain a strong
common component. In that case, the first principal component should explain a large share
of the cross-model variation and can be interpreted as a consensus measure of the latent
construct. By contrast, if the first component explains only a modest share of the variation,
this suggests that the models are not simply noisy proxies for the same construct, but instead
embed meaningful model-specific differences in how they interpret and operationalize the
text.
For each construct, we run PCA on the seven standardized LLM score series. Standardizing
the scores ensures that the results are not mechanically driven by differences in scale or
18

dispersion across providers. The first principal component captures the dominant common
signal across models, while the remaining components capture variation that is not summarized
by this common factor. Thus, the share of variance explained by the first component provides
a concise measure of how well the seven model-specific series can be represented by a single
LLM consensus component.
Table 3 reports the PCA results, which reinforce the evidence from the correlation and
justification analyses. Across constructs, the first principal component explains an average
of 60\% of the variation. Moreover, on average, five of the seven principal components are
needed to explain 90\% of the total variation. Thus, for most constructs, the seven LLM scores
cannot be reduced to a single consensus measure without losing substantial information.
Consistent with the prior results, sentiment is the only construct with a relatively strong
common component: the first principal component explains 85\% of the variation in sentiment
scores. Consistent with this interpretation, the first-component loadings for sentiment are
nearly identical across the seven providers, ranging from 0.36 to 0.39 (an exactly equal-
weighted component would imply loadings of 0.38), so the first component is effectively an
equal-weighted consensus of the models. For lower-agreement constructs, the loadings remain
positive but become substantially more uneven: for integrity they range from 0.20 to 0.45
across providers, and for the specificity ratio from 0.22 to 0.50, with the heaviest weight on a
single provider (Mistral). Thus, for these constructs the first component does not represent
a uniform consensus across models but instead reflects disproportionate contributions from
particular providers.
[Insert Table 3 about here]
The result for specificity is particularly striking. Ex ante, specificity is the construct for
which one might expect especially high agreement because it is based on a relatively well-
defined counting task: identifying specific textual elements such as named entities, monetary
values, percentages, dates, and durations. In contrast, constructs such as political risk,
integrity, or respect are inherently more interpretive and leave more room for model-specific
19

judgment. Yet the specificity ratio has one of the weakest common components across models.
This suggests that even rule-based, explicitly specified tasks can generate substantial model
dependence when implemented through LLM prompts. Given this surprising outcome, we
proceed to investigate it in more detail.
Because the prompt requires each model to report both the number of specific items
and the specificity ratio, we can trace where the disagreement arises, and every step of
the calculation turns out to fail in a different way. First, models identify very different
numbers of specific items in the same texts: the median count ranges from 12 (OpenAI) to
100 (Gemini). The counts are nonetheless moderately rank-correlated across models (mean
pairwise Spearman correlation of 0.43), so models broadly agree on which texts are more
specific but they come up with very different numbers of specific items (even though the
prompt clearly identifies what categories should be counted as specific items). Second, the
models disagree on the total word count of the text. The totals they report---or that their
reported ratios imply---range from about one-tenth of the true word count (DeepSeek and
Qwen) to more than twice the true count (OpenAI), and they are essentially uncorrelated
across models (mean pairwise Spearman of 0.12); DeepSeek even states in its responses that
it estimates total words by dividing the character count by 4.5.
Therefore, one should not rely on LLM-generated outcomes that depend on word counts,
as the way words are counted is highly model dependent. A simple counterfactual isolates
the role of this fabricated denominator: replacing each model's reported total-word count
with the true word count of the text raises the mean pairwise rank correlation of the ratio
from 0.23 to 0.47. Thus, disagreement in this rule-based task does not primarily reflect
interpretive ambiguity; rather, it reflects differences in implementation, including different
entity-recognition thresholds and highly model-dependent word-count estimates. More
generally, this finding cautions against assuming that a construct is model-invariant simply
because its conceptual definition is precise.
Overall, the PCA results show that inter-model disagreement is not merely a collection
20

of isolated pairwise differences. For many constructs, disagreement reflects the absence of a
dominant common factor across providers. This evidence complements the low similarity in
model justifications and suggests that different LLMs often rely on distinct interpretations
or operational rules when converting the same disclosure into a numerical measure. The
reliability of LLM-based textual measures therefore varies meaningfully across constructs,
and using a single LLM provider may embed provider-specific measurement choices into
empirical variables.
4.2 Variance decomposition of LLM disagreement
To further examine the sources of disagreement across LLMs, we estimate a crossed random-
effects variance-components model using restricted maximum likelihood (REML), separately
for each construct (Patterson and Thompson, 1971; Harville, 1977). Because every provider
scores every call, the design is balanced, and we obtain the variance components from the
analysis-of-variance mean squares of the call-by-provider design (Brennan, 2001), which
coincide with the REML estimates in this setting. This analysis complements the correlation
and PCA results by decomposing the total variation in LLM scores into three components:
variation across calls, systematic differences across providers, and residual model-by-call
variation.
Formally, for constructc, calli, and LLM providerm, we estimate
Score icm =\mu c +\alpha ic +\gamma mc +\varepsilon icm,(1)
where \mu c is the construct-specific grand mean, \alpha ic is a call random effect, \gamma mc is a provider
random effect, and\varepsilon icm is the residual model-by-call component. We assume that
\alpha ic\sim N(0,\sigma 2 \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l},c), \gamma mc\sim N(0,\sigma 2 \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r},c), \varepsilon icm\sim N(0,\sigma 2 \varepsilon ,c).(2)
21

Thus, the total variance in LLM scores for constructcis
\sigma 2 \mathrm{t}\mathrm{o}\mathrm{t}\mathrm{a}\mathrm{l},c =\sigma 2 \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l},c +\sigma 2 \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r},c +\sigma 2 \varepsilon ,c.(3)
The call component, \sigma 2 \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l},c, captures the extent to which scores vary across texts in a
way that is common across models. The provider component, \sigma 2 \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r},c, captures systematic
calibration differences across providers, such as some models assigning consistently higher
or lower scores on average. The residual component, \sigma 2 \varepsilon ,c, captures model-by-call deviations
that remain after accounting for call-level and provider-level effects. This residual component
includes both idiosyncratic noise and systematic differences in how particular models interpret
particular texts. We estimate the model on raw (unstandardized) scores, so that systematic
differences in the level of provider scores are preserved and captured by the provider component
rather than removed by construction.
We report each component as a share of total variance. For example, the call share is
defined as
\widehat \sigma 2 \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l},c
\widehat \sigma 2 \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l},c +\widehat \sigma 2 \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r},c +\widehat \sigma 2 \varepsilon ,c ,(4)
with analogous definitions for the provider and residual shares.
We also report the relative reliability of the seven-model average using the generalizability
coefficient,G, following the logic of generalizability theory (Brennan, 2001):
Gc(7) = \widehat \sigma 2 \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l},c
\widehat \sigma 2 \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l},c +\widehat \sigma 2 \varepsilon ,c/7.(5)
This coefficient measures how reliably the average score across the seven providers captures rel-
ative differences across calls in the common LLM-based component of the measure. Intuitively,
if some calls are consistently scored as high by most providers and others are consistently
scored as low by most providers, then averaging across models can reduce model-specific
deviations and recover a stable consensus measure. However, this is not a mechanical result.
22

Averaging improves reliability only when there is a sufficiently strong common component
across providers and when model-specific deviations partly offset each other. If providers
interpret the same calls in systematically different ways, or if their errors are correlated
rather than idiosyncratic, the seven-model average need not be reliable. Thus, whether an
ensemble LLM measure improves reliability is an empirical question rather than an automatic
consequence of combining multiple models. Because the same seven providers score every
call, stable differences in provider scoring levels cancel out of relative comparisons, and Gc(7)
therefore does not penalize them. To also assess reliability inlevels, we report the absolute
dependability coefficient (Brennan, 2001),
\Phi c(7) = \widehat \sigma 2 \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l},c
\widehat \sigma 2 \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l},c +\widehat \sigma 2 \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r},c/7 +\widehat \sigma 2 \varepsilon ,c/7,(6)
which treats the seven providers as draws from a broader population of possible models and
retains the provider variance in the denominator. \Phi c(7) measures the dependability of the
ensemble's absolute score when providers are treated as draws from the specified universe of
admissible models. It is the relevant reliability concept whenever scores are used in absolute
terms---for example, when comparing magnitudes across studies that rely on different sets of
models or when applying fixed thresholds to the scores.
Table 4 reports the variance-decomposition results. Averaged across constructs, only
34.4\% of the variation in an LLM score is attributable to differences across calls. The
remaining 65.6\% reflects model-related variation: 33.4\% is attributable to systematic provider
differences and 32.2\% to residual model-by-call variation. Sentiment is again the exception:
74\% of the variance is attributable to the call component. In contrast, constructs such as
integrity and the specificity ratio are dominated by model-related variation, with only 13\%
and 4\% of the variance, respectively, attributable to the call component.
[Insert Table 4 about here]
The relative reliability results provide a more encouraging perspective on the use of
23

multiple LLMs. The generalizability coefficient for the seven-model average is 0.84 on average,
and only one of the thirteen constructs---the specificity ratio---falls below 0.70. Sentiment has
the highest reliability, with Gc(7) = 0.97. These results indicate that, although individual
LLM scores contain substantial model-related variation, averaging across providers recovers a
reasonably reliable common signal for most constructs. In other words, the ensemble measure
generally preserves relative differences across calls, even when individual providers differ in
their score levels or in their evaluation of particular calls.
The absolute reliability results are markedly weaker. The dependability coefficient averages
0.72 across constructs; only nine of the thirteen constructs exceed 0.70, and only five exceed
0.80. The gap between Gc(7) and \Phi c(7) is proportional to the provider share of the variance:
sentiment is essentially unaffected (0.97 versus 0.95), while integrity falls from 0.76 to 0.51
and the specificity ratio from 0.49 to 0.22. Uncertainty is a telling intermediate case: the
models rank calls fairly consistently (Gc(7) = 0.90), but they disagree substantially about
levels (\Phi c(7) = 0.65), reflecting the second-largest provider component among all constructs.
Thus, averaging across providers delivers reliable relative rankings for most constructs, but
reliable levels for fewer than half of them.
This distinction is important for interpretation. A relatively high Gc(7) does not imply
that providers are interchangeable in levels, nor does it eliminate the evidence of model
disagreement documented above. Rather, it shows that combining the seven models can
mitigate some forms of model-specific noise and improve the reliability of relative rankings
across calls. At the same time, the large provider component indicates that models differ
substantially in the levels of scores they assign, while the residual component indicates that
models also differ in how they evaluate particular calls. Thus, the variance decomposition
suggests both a caution and a practical implication: relying on a single LLM can embed
provider-specific measurement choices into empirical variables, but averaging across multiple
providers can produce a more reliable measure for many constructs.
Overall, the variance-components analysis shows that LLM disagreement has two distinct
24

implications. First, individual model scores are often substantially affected by provider-specific
calibration and model-by-call variation, which cautions against treating any single LLM as
an objective measure of the underlying construct. Second, the relatively high generalizability
coefficient of the seven-model average indicates that, for most constructs, these disagreements
do not fully eliminate the common signal shared across providers. Thus, the evidence
points to a nuanced conclusion: LLM-based textual measures are often model-dependent at
the individual-provider level, but ensemble measures can recover a more reliable common
component for many constructs. The main exception is the specificity ratio, where averaging
recovers neither a reliable ranking of calls (Gc(7) = 0.49) nor reliable levels (\Phi c(7) = 0.22);
for integrity, averaging restores a usable ranking ( Gc(7) = 0 .76) but not reliable levels
(\Phi c(7) = 0.51).
4.3 Observable determinants of LLM disagreement
The preceding analyses show that LLM disagreement varies substantially across constructs
and is not fully captured by a single common model component. We next ask whether this
disagreement is systematically related to observable firm and call characteristics. This analysis
is descriptive rather than causal: our objective is to understand whether LLM disagreement
is concentrated in particular types of firms, calls, or textual environments.
For each call and construct, we measure LLM disagreement as the standard deviation
of the seven provider-standardized LLM scores. Since we analyze thirteen constructs, each
call contributes thirteen construct-specific disagreement measures. We then pool these
observations and regress LLM disagreement on a set of firm-level and call-level characteristics.
The firm-level variables include size, book-to-market, Tobin's Q, and the earnings surprise
associated with the call. Earnings surprise is included because disagreement may be higher
when the underlying performance news is more salient, ambiguous, or mixed relative to
market expectations. The textual variables include readability, measured using the Fog index;
text length; financial jargon intensity; numerical intensity; and forward-looking language
25

intensity. These variables allow us to examine whether disagreement is higher when calls are
longer, more complex, more quantitative, or more forward-looking.
We also include the average pairwise cosine similarity of the LLM justifications for each
call and construct. In principle, higher justification similarity should be associated with lower
score dispersion if models that emphasize similar textual features also assign more similar
scores. However, this relation is an empirical question, especially given the earlier evidence
that similarity in scores and similarity in justifications do not always move together. All
specifications include construct fixed effects, which absorb average differences in disagreement
across prompts/constructs. In some specifications, we also include industry and quarter fixed
effects to account for persistent differences across industries and time.
Table 5 reports the results. Firm size and Tobin's Q are positively associated with LLM
disagreement, suggesting that disagreement is greater for larger and higher-growth firms.
One interpretation is that these firms tend to have more complex operations and disclosures,
which may leave more room for model-specific interpretation. There is no significant relation
between earnings surprise and the level of LLM disagreement.
[Insert Table 5 about here]
The textual characteristics provide additional insight. Readability, as measured by the
Fog index, is not systematically related to LLM disagreement in the richer specifications. This
suggests that disagreement is not primarily driven by conventional readability constraints:
the models do not appear to disagree simply because the text is syntactically more difficult.
By contrast, calls with a greater share of forward-looking language exhibit significantly higher
disagreement. This pattern is intuitive because forward-looking statements often involve
expectations, risks, and conditional claims, all of which may require more interpretation
than descriptions of realized outcomes. Such language may therefore provide more scope for
different LLMs to emphasize different parts of the same disclosure.
Finally, higher similarity in model justifications is associated with lower LLM disagreement.
This result suggests that the justifications are informative about the scoring process: when
26

models provide more similar rationales, they also tend to assign more similar scores. At
the same time, the relation is not mechanical. Models may use similar language in their
justifications while mapping the text into different numerical scores, or they may assign
similar scores while emphasizing different aspects of the call. Thus, the negative association
between justification similarity and score dispersion provides evidence that stated rationales
are economically meaningful, while also reinforcing the importance of analyzing both scores
and explanations.6
Importantly, the explanatory power of these regressions is quite low. Even after controlling
for firm characteristics, textual characteristics, justification similarity, construct, industry,
and quarter fixed effects, the model explains only 20\% of the variation in LLM disagreement.
This indicates that disagreement across LLMs is not simply a function of observable firm
characteristics, standard textual measures, or broad industry and time patterns. Instead,
much of the disagreement appears to arise from model-specific responses to particular texts.
This conclusion is consistent with the variance-decomposition results: LLM disagreement
reflects not only stable provider-level calibration differences, but also residual model-by-call
variation that is difficult to explain using standard observables.
4.4 Does LLM disagreement predict market and analyst disagree-
ment?
Finally, we ask whether disagreement among LLMs is informative about subsequent dis-
agreement in markets. If cross-model dispersion partly reflects genuine ambiguity in the
disclosure, then calls on which the models disagree should be followed by greater disagreement
among investors and analysts. We regress post-call disagreement outcomes on call-level LLM
dispersion, defined as the average across the thirteen measures of the standard deviation
of the seven provider-standardized scores. We examine five outcomes: next-quarter analyst
6\mathrm{T}\mathrm{a}\mathrm{b}\mathrm{l}\mathrm{e} \mathrm{O}\mathrm{A}.\mathrm{C}.1 \mathrm{i}\mathrm{n} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{O}\mathrm{n}\mathrm{l}\mathrm{i}\mathrm{n}\mathrm{e} \mathrm{A}\mathrm{p}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{d}\mathrm{i}\mathrm{x} \mathrm{r}\mathrm{e}\mathrm{p}\mathrm{o}\mathrm{r}\mathrm{t}\mathrm{s} \mathrm{r}\mathrm{e}\mathrm{s}\mathrm{u}\mathrm{l}\mathrm{t}\mathrm{s} \mathrm{u}\mathrm{s}\mathrm{i}\mathrm{n}\mathrm{g} \mathrm{a} \mathrm{r}\mathrm{a}\mathrm{n}\mathrm{g}\mathrm{e}-\mathrm{b}\mathrm{a}\mathrm{s}\mathrm{e}\mathrm{d} \mathrm{d}\mathrm{i}\mathrm{s}\mathrm{p}\mathrm{e}\mathrm{r}\mathrm{s}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{m}\mathrm{e}\mathrm{a}\mathrm{s}\mathrm{u}\mathrm{r}\mathrm{e}, \mathrm{d}\mathrm{e}fi\mathrm{n}\mathrm{e}\mathrm{d} \mathrm{a}\mathrm{s}
\mathrm{t}\mathrm{h}\mathrm{e} \mathrm{m}\mathrm{a}\mathrm{x}\mathrm{i}\mathrm{m}\mathrm{u}\mathrm{m} \mathrm{m}\mathrm{i}\mathrm{n}\mathrm{u}\mathrm{s} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{m}\mathrm{i}\mathrm{n}\mathrm{i}\mathrm{m}\mathrm{u}\mathrm{m} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}-\mathrm{s}\mathrm{t}\mathrm{a}\mathrm{n}\mathrm{d}\mathrm{a}\mathrm{r}\mathrm{d}\mathrm{i}\mathrm{z}\mathrm{e}\mathrm{d} \mathrm{L}\mathrm{L}\mathrm{M} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}\mathrm{s} \mathrm{f}\mathrm{o}\mathrm{r} \mathrm{e}\mathrm{a}\mathrm{c}\mathrm{h} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l} \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t}. \mathrm{T}\mathrm{h}\mathrm{e}
\mathrm{r}\mathrm{e}\mathrm{s}\mathrm{u}\mathrm{l}\mathrm{t}\mathrm{s} \mathrm{a}\mathrm{r}\mathrm{e} \mathrm{s}\mathrm{i}\mathrm{m}\mathrm{i}\mathrm{l}\mathrm{a}\mathrm{r} \mathrm{t}\mathrm{o} \mathrm{t}\mathrm{h}\mathrm{o}\mathrm{s}\mathrm{e} \mathrm{r}\mathrm{e}\mathrm{p}\mathrm{o}\mathrm{r}\mathrm{t}\mathrm{e}\mathrm{d} \mathrm{a}\mathrm{b}\mathrm{o}\mathrm{v}\mathrm{e} \mathrm{u}\mathrm{s}\mathrm{i}\mathrm{n}\mathrm{g} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{t}\mathrm{a}\mathrm{n}\mathrm{d}\mathrm{a}\mathrm{r}\mathrm{d}-\mathrm{d}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}-\mathrm{b}\mathrm{a}\mathrm{s}\mathrm{e}\mathrm{d} \mathrm{d}\mathrm{i}\mathrm{s}\mathrm{p}\mathrm{e}\mathrm{r}\mathrm{s}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{m}\mathrm{e}\mathrm{a}\mathrm{s}\mathrm{u}\mathrm{r}\mathrm{e}.
27

forecast dispersion, the analyst consensus forecast error (from the I/B/E/S detail file), and
abnormal bid-ask spreads, trading volume, and return variance in the two-day announcement
window. Each column of Table 6 is a call-level regression, controlling for pre-call analyst
coverage and dispersion, size, book-to-market, Tobin's Q, and the earnings surprise, with
industry and quarter fixed effects and standard errors clustered by firm.
As shown, LLM dispersion is not significantly related to any of the five outcomes. That
is, calls on which the models disagree are not associated with greater dispersion or larger
errors in analyst forecasts, nor with wider bid-ask spreads, heavier trading, or higher return
variance.
These results provide no evidence that LLM disagreement captures disclosure ambiguity
that is subsequently reflected in analyst or market disagreement, and are consistent with a
substantial model-specific component in LLM-based measurement.
[Insert Table 6 about here]
4.5 Does model choice affect empirical conclusions?
The preceding results establish that LLM-based measures are model-dependent. Specifically,
the distributions and properties of constructs commonly used in empirical accounting and
finance research vary substantially across LLMs, and LLM-generated measures exhibit low
correlations with commonly used non-LLM measures of the same constructs. In this section,
we examine whether---and to what extent---empirical conclusions would differ depending on
the LLM used to construct earnings-call measures.
To do so, for each construct and each provider separately, we regress announcement
returns on the provider's standardized LLM score, controlling for firm characteristics and
including industry and quarter fixed effects. Each provider-specific coefficient in Table 7
can therefore be interpreted as the finding that a researcher would obtain if they used that
provider's LLM output as the textual measure.
28

Two results stand out. First, for several constructs---including climate risk, management
clarity, specificity, and the specificity ratio---the provider-specific coefficients vary substantially
in magnitude, sign, and statistical significance. For climate risk, for example, the coefficients
in the first column range from - 0.4 to +0.2, and only one of the seven model-specific measures,
Qwen's, is significantly associated with the subsequent market reaction. A similar pattern
emerges for management clarity, where statistical significance is driven by a single provider,
and for the specificity ratio, where the coefficients are significant for Mistral and OpenAI but
not for the other providers. These results illustrate a consequential form of model dependence:
two researchers analyzing the same earnings calls using the same empirical specification, but
choosing different LLM providers, could reach materially different conclusions, with point
estimates differing in magnitude or even sign and statistically significant results under some
providers but not others.
Second, some constructs display more consistent patterns across LLMs. For corporate
culture, sentiment, and uncertainty, the signs and statistical significance of the LLM-based
coefficients are more stable across providers. Even in these cases, however, the estimated
magnitudes vary substantially, especially for sentiment and uncertainty. To assess formally
whether these coefficient differences are statistically meaningful, we estimate, for each
construct, the seven provider-specific return regressions jointly as a stacked regression. In this
specification, the right-hand-side variables are interacted with provider indicators, making
the stacked regression equivalent to estimating the provider-specific regressions separately
while allowing us to test equality of coefficients across providers. We then test the equality
of the seven LLM score coefficients using a Wald test, clustering standard errors by firm.
Equality is rejected at the 1\% level for sentiment ( \chi 2 = 32.8) and uncertainty (\chi 2 = 33.5).
Corporate culture is the clearest case in which the results are relatively consistent across
providers and the Wald test does not reject equality of the provider-specific coefficients.
Finally, the comparison with traditional non-LLM measures further illustrates the impor-
tance of measurement choice. For example, while the LLM-based sentiment coefficients are
29

positive and statistically significant across providers, and the LLM-based uncertainty coeffi-
cients are negative and statistically significant across providers, the corresponding traditional
measures are very different in magnitude and not statistically significant. This pattern shows
that even when LLMs agree with one another, their measures can differ meaningfully from
traditional text-based measures.
[Insert Table 7 about here]
4.6 Is the disagreement an artifact of differing knowledge cutoffs?
A natural concern is that the cross-model disagreement we document reflects the models'
differing training-dataknowledge cutoffsrather than genuine differences in how they read
the same text. Because a language model is trained on data only up to some date, it
may have ingested news coverage, analyst commentary, and the realized market reaction
surrounding an earnings call that predates its cutoff. A model scoring such a call could then
be guided by the realized outcome rather than by the transcript alone---the look-ahead bias
and outcome memorization documented for LLM-based financial prediction (Glasserman and
Lin, 2023; Didisheim et al., 2025; Kong et al., 2026). If two models with different cutoffs bring
systematically different outside knowledge to the same call, part of their disagreement would
be an artifact of training vintage rather than of interpretation. This concern is sharpest for
sentiment: Glasserman and Lin (2023) show that an LLM's prior knowledge of the firms
involved materially shapes its sentiment scores, which makes sentiment both the construct
most exposed to training-corpus leakage and the natural place to look for a cutoff effect.
Separating a cutoff effect from model identity is difficult because, across providers, a
model's cutoff is almost perfectly collinear with the model itself. The cutoffs of our seven
models fall on either side of the 2024 sample: four are in 2023 (Anthropic in August, OpenAI
and Mistral in October, and Meta's Llama in December), one is in early 2025 (Google), and
two---Qwen, at June 2024, and DeepSeek, at July 2024---fall inside the window (Table 8). The
direction of potential contamination is important to fix at the outset. For a given model, a
30

call datedbeforeits cutoff is one the model could have ingested together with the call's market
outcome, and is thus potentially contaminated; a call datedafterthe cutoff cannot have been
seen and is clean. Under this logic the early-2025 model could in principle have memorized
outcomes for every call in our 2024 sample, the four 2023 models could have memorized none,
and two models straddle: DeepSeek, with 1,242 pre-cutoff (potentially contaminated) and 704
post-cutoff (clean) calls, and Qwen, with 970 and 976. We therefore treat DeepSeek and Qwen
as within-model probes and the remaining five models, whose contamination status does
not change within 2024, as a calendar control in a difference-in-differences design. Because
both post-cutoff periods fall in the second half of 2024, any raw pre-to-post change in their
behavior must be purged of the common calendar trend before it can be read as a cutoff
effect. The evidence points consistently away from a cutoff explanation.
We begin by asking whether disagreement tracks differences in training vintage. If it did,
model pairs with more distant cutoffs should agree less. Across the 21 provider pairs, however,
the rank correlation between the gap in cutoff dates (in months) and pairwise agreement (the
mean across constructs of the two models' Spearman correlation) is essentially zero ( \rho = 0.00,
p = 0.99), whereas a cutoff story predicts a negative relation. The most telling version of
this test uses the one pair of models that shares an identical cutoff (OpenAI and Mistral,
October 2023): its agreement (\rho = 0.62) is no higher than that of the same two models paired
with Google, whose cutoff is fifteen months later (0 .62 on average). Nor is Google, the only
model whose cutoff postdates the entire sample and hence the one with potential access to
every realized 2024 outcome, an outlier: its average agreement with the other six models
(0.56) matches that of OpenAI (0 .56) and Mistral (0.56). Models with the same training
vintage do not converge, and the model with the most potential access to outcomes does not
diverge, which is difficult to reconcile with the idea that shared training vintage manufactures
shared scores.
We next examine whether the straddling models' disagreement with the consensus shifts
as each crosses its own cutoff. DeepSeek's raw absolute deviation from the leave-one-out
31

seven-model consensus rises from 0.457 before its cutoff to 0.485 after, an increase of about
six percent, while Qwen's is unchanged (0 .849 and 0.851); but because both post periods
fall late in 2024, a raw change conflates the cutoff with any common calendar drift. A
difference-in-differences that removes the common monthly pattern (provider and month
fixed effects, standard errors clustered by firm) leaves a smaller DeepSeek-specific increase
of +0.020 (t = 2.9), against a mean deviation of 0 .46, and no change for Qwen (  - 0.005,
t = - 0.6). Two features of DeepSeek's residual argue against a contamination reading. First,
its construct signature is the opposite of what outcome leakage would produce. The increase is
concentrated in the most subjective constructs---corporate culture (+0.075), quality (+0.067),
and management clarity (+0.057), each significant---none of which has a realized-outcome
referent that a model could memorize, whereas the constructs where leakage is most plausible
show nothing: the interaction is an insignificant  - 0.003 (t = - 0.2) for sentiment, is flat for
integrity and the specificity ratio, and is, if anything, negative for political risk (  - 0.027,
t = - 1.2) (Table 9). Qwen, whose overall deviation does not change, shows the same
for sentiment ( - 0.014, t = - 1.0), and its few significant construct-level changes run in
both directions. Memorization of realized outcomes should surface in the news-grounded
constructs, not in perceptions of ``respect"" or ``teamwork."" Second, the effect is economically
negligible---roughly four percent of the average deviation---and, as we show next, is absent in
the one construct where outcome leakage can be tested directly.
That direct test concerns sentiment. If a straddling model's pre-cutoff sentiment scores
were contaminated by the realized outcome, their correlation with the announcement CAR
should fall once the model crosses its cutoff and can no longer have observed that outcome.
It does not, for either model: the correlation is 0 .17 before DeepSeek's cutoff and 0.27 after,
an increase that mirrors the common movement across the five control models over the
same months (from 0.17 to 0.27); Qwen's moves from 0.16 to 0.18 around its cutoff, against
0.20 to 0.22 for the controls. The cross-model comparison tells the same story. The one
always-pre-cutoff model, Google, exhibits a sentiment--CAR correlation of 0 .24, against 0.20
32

for the four always-post-cutoff models pooled and 0 .20--0.23 for them individually; access to
realized outcomes, where it exists, does not visibly sharpen the sentiment--return link. A final
check looks at the dispersion of the scores themselves: if outside knowledge had anchored
the straddling models' pre-cutoff scores, they should become noticeably noisier once that
knowledge is unavailable. They do not---the post-to-pre within-firm variance ratio is 1 .05 for
DeepSeek and 0.94 for Qwen, against 1.01 and 1.02 for the five control models.
Taken together, the construct most exposed to training-corpus leakage---sentiment--- is
among the least affected by cutoff crossing, and the one direct look-ahead test we can run
shows no sign of the predicted decline. Therefore, we find little evidence that differences in
knowledge cutoffs account for the cross-model disagreement we document.
[Insert Table 8 about here]
[Insert Table 9 about here]
5 Do Newer Models Converge?
The seven models we study were, at the time of our analysis, among those most widely used
in academic applications and were comparable in capability to the models employed in the
studies reviewed in Section 2. Nevertheless, the rapidly evolving model landscape limits the
generalizability of any such snapshot. The pace of new releases makes continuous updating
infeasible: pipelines built around particular models can quickly become outdated, while
re-scoring a large corpus after every release is impractical. Moreover, applying frontier models
to samples of the size common in this literature can be prohibitively costly, particularly when
researchers seek to conduct the cross-provider validation that our findings recommend.
To assess whether our conclusions extend to more recent models, we conduct a supplemen-
tary analysis using a random subsample of 250 calls covering 204 firms. We re-score these calls
using the September 2026 successors from two of the seven model families in our main analysis,
selected from the providers most widely used in academic research: OpenAI ( gpt-5.6-terra)
33

and Google ( gemini-3.8-flash). We hold the transcripts, prompts, scoring scales, and
inference settings fixed relative to the main analysis. We examine three measures commonly
used in the accounting disclosure literature---sentiment (Loughran and McDonald, 2011),
management clarity (Barth et al., 2023), and answer specificity (Hope et al., 2016). These
measures span the range of cross-model agreement observed in our main analysis: agreement
is highest for sentiment, lowest for specificity ratio, and intermediate for management clarity.
This design therefore allows us to assess whether the pattern persists across the upper, middle,
and lower portions of the agreement distribution.
Forsentiment---already the most reliable construct---little changes. The OpenAI and
Google models agreed strongly in our baseline setup (Spearman correlation of 0 .91) and
agree marginally more once upgraded (0.92). Their correlation with the Loughran--McDonald
dictionary is essentially flat, and low, in both vintages (OpenAI 0 .36 \rightarrow 0.33; Gemini
0.32\rightarrow 0.32). The dictionary, however, is one operationalization of tone, not ground truth, so
this stability is unremarkable: it says only that LLM-based and dictionary-based sentiment
remain distinct measures at the frontier, not that either is closer to correct.
Formanagement clarity---the middle case---cross-provider agreement rises modestly, from
0.68 to 0.73. Yet neither model moves toward the traditional evasive-language benchmark:
the correlation stays near 0.10 and is, if anything, slightly lower for the newer models (OpenAI
0.08\rightarrow 0.06; Gemini 0.14\rightarrow 0.11). As with sentiment, the benchmark is an alternative
operationalization rather than a criterion of truth, so its persistent low correlation cannot be
read as an LLM failure; but it does show that greater agreement between the frontier models
does not reconcile them with the established measure.
For thespecificity ratio---the least reliable construct in the main analysis---the frontier
delivers the largest change on both margins. Cross-provider agreement rises sharply, from 0.37
to 0.61, and, unlike the other two measures, each model also movescloserto the traditional
benchmark (OpenAI 0 .52\rightarrow 0.57; Gemini 0 .44\rightarrow 0.65). This measure is the one case
in which the traditional benchmark can be treated as an approximate ground truth: the
34

specificity ratio is defined by an explicit counting rule, and the non-LLM version simply
implements that rule directly, whereas the dictionary tone and evasive-language measures are
only proxies for the constructs they name. Rising alignment with the counting rule therefore
indicates that the newer models compute the ratio morecorrectly, not merely more alike.
The mechanics confirm this: the two 2026 models count specific items far more consistently
(item-count correlation of 0.75, versus 0.43 in the original case). The newer models also count
transcript length much more accurately (within roughly half to one times the true count,
versus one-tenth to three times before), correcting the faulty denominator that drove the
divergence. Even so, cross-provider agreement reaches only 0.61.
Taken together, upgrading to frontier models moves cross-provider agreement in the right
direction but does not eliminate the disagreement. Whether ``the right direction""---higher
agreement---also means greater accuracy is, in general, outside the scope of our design, which
measures whether models agree rather than whether they are correct. The specificity ratio is
a partial exception: because it is defined by an explicit counting rule that the traditional
benchmark implements directly, higher agreement on this measure can plausibly be read as
movement toward the true value. Even there, however, substantial disagreement remains---the
two frontier models correlate only 0.61---and, with the sole exception of sentiment, which
already exhibited high agreement, cross-provider disagreement persists at the frontier. This
is a demanding setting in which to find such disagreement. As noted earlier, we deliberately
study measurement rather than prediction---a far more challenging task that would invite still
greater cross-model disagreement and additional problems such as look-ahead bias---and we
do so using constructs that are conceptually well defined. That substantial model dependence
survives even under these favorable conditions suggests that researchers should be cautious
in using a single model for measurement: another model, including a newer one, may yield
materially different results.
35

6 Conclusion
We ask a simple question with broad consequences for empirical research in accounting and
finance: when a generative LLM converts text into a number, is that number a property of
the text or of the model? Using the question-and-answer portions of 1,946 S\&P 500 earnings
calls in 2024, we have seven LLMs from seven independent developers score each call on
thirteen measures that the literature routinely extracts from corporate disclosure. The design
is deliberately conservative---every construct is contained in a fixed transcript, and no model
is asked to forecast a future metric---so that any disagreement can be read as noise in the
measurement instrument rather than informative disagreement about an unknown future.
We nonetheless find substantial divergence. The average pairwise correlation across models
is 0.52, only about a third of the variation in a typical score is attributable to the text
rather than the model, and for several constructs the model matters far more than the firm.
Disagreement is not confined to soft constructs: it is among the largest for an explicitly
specified implementation task (Specificity ratio).
These results carry a direct lesson for empirical research. Accounting and finance have
increasingly treated LLM output as measurement-ready data, often substituting a single
model's scores for the dictionary- and rule-based measures that preceded them. Our evidence
shows that this substitution is not innocuous: LLM measures are neither interchangeable with
one another nor with the traditional measures they replace---the ensemble sentiment score
correlates only 0.29 with dictionary tone---so a construct's empirical content now depends on
the measurement technology chosen. Most consequentially, the choice of model is a researcher
degree of freedom that can change conclusions. Estimating the same announcement-return
regression on the same calls, three researchers who differ only in their choice of provider could
report a positive effect, a negative effect, and no effect for the very same construct. Because
this choice is currently neither disclosed nor justified in most applications, two studies that
claim to measure the ""same"" construct may be measuring materially different things.
These findings do not imply that LLM-based measurement should be abandoned. Aver-
36

aging across providers behaves as generalizability theory predicts: it cancels model-specific
noise and recovers a reliable ranking of calls for most measures, even though the individual
models disagree. But aggregation is a partial remedy, not a panacea. It restores reliable
relative rankings without restoring reliable levels.
We also provide direct, if limited, evidence on whether newer models help. In a smaller
exercise, we re-score a random subsample of calls with the September 2026 successors of two
providers, OpenAI and Google. Upgrading to these frontier models moves cross-provider
agreement in the right direction but does not eliminate it: agreement rises most for the
constructs on which the earlier models diverged most, yet meaningful disagreement remains
for every measure except sentiment, which was already highly reliable. Greater agreement
between the newer models also does not, in general, bring them closer to the established
benchmarks; the exception is the specificity ratio---a rule-based measure for which higher
agreement plausibly reflects movement toward the true value, and even there the two frontier
models correlate only 0 .61. Continued model improvement therefore does not by itself
eliminate the need to assess measurement invariance empirically.
Two features of our design bound the interpretation of these results. We query each
model through its API with a fixed prompt and without external tools, retrieval, or extended-
reasoning scaffolding. This isolates the model's own contribution---its weights and align-
ment---and matches the pipelines through which research measures are actually constructed,
which for reasons of cost, reproducibility, and structured output rely on API calls rather
than on the consumer chat applications. Our estimates therefore need not carry over to
measurement performed through those full products or through agentic systems that add
system prompts, tool use, web retrieval, and multi-step reasoning. Such scaffolding could raise
agreement, by grounding models in common external sources, or lower it, by multiplying the
idiosyncratic paths a model can follow, and each such choice is itself a further undocumented
researcher degree of freedom layered on top of the model choice we study.
We close with three practical recommendations for the research community. First, model
37

choice should be reported as a first-order design decision: studies should disclose---and
ideally justify---the specific model and version used, just as they disclose a sample period
or a variable definition, particularly since the model snapshots underlying a measure are
versioned and periodically deprecated. Second, cross-provider validation should become
routine; a second model is a cheap diagnostic, and material sensitivity to it is itself a finding
worth reporting. Third, where feasible, researchers should prefer ensemble measures across
providers to any single model's output. More broadly, the field would benefit from shared
benchmarks and validation standards for LLM-based measurement, from routine reporting of
the sensitivity of results to model, version, and prompt, and from external validation against
human-coded or otherwise anchored ground truth. As LLMs move from measurement toward
more autonomous, agentic roles in the research pipeline, the model-induced variation we
document at the measurement stage is likely to compound rather than cancel---making a
discipline of measurement reliability a prerequisite, not an afterthought, for credible research.
38

References
Abraham, J., Olbert, M., and Vasvari, F. (2024). ESG disclosures in the private equity
industry.Journal of Accounting Research, 62(5):1611--1660.
Andreou, P. C., Lambertides, N., Magidou, M., and Maruska, A. E. (2026). Measuring R\&D
activity through 10-K narrative disclosures.Research Policy, 55(3):105409.
Asirvatham, H., Mokski, E., and Shleifer, A. (2026). GPT as a measurement tool. Working
Paper 34834, National Bureau of Economic Research.
Bai, J. J., Boyson, N. M., Cao, Y., Liu, M., and Wan, C. (2025). Executives vs. chatbots:
Unmasking insights through human--AI differences in earnings conference Q\&A.SSRN
Working Paper.
Barth, A., Mansouri, S., and Woebbeking, F. (2023). ``let me get back to you"": A machine
learning approach to measuring nonanswers.Management Science, 69(10):6333--6348.
Bernard, D., Blankespoor, E., de Kok, T., and Toynbee, S. (2026). Using gpt to measure
business complexity.The Accounting Review, 101(3):67--102.
Bhagwat, V., Cookson, J. A., Dim, C., and Niessner, M. (2026). The market's mirror:
Revealing investor disagreement with LLMs. Working Paper.
Boustanifar, H. and Schwarz, P. (2026). Measuring business social irresponsibility: The case
of sin stocks. SSRN Working Paper.
Boustanifar, H. and Sheykhi, S. (2026). The Fearless Premium: Workplace Psychological
Safety and Stock Returns. SSRN Working Paper.
Bozanic, Z., Roulstone, D. T., and Van Buskirk, A. (2018). Management earnings forecasts
and other forward-looking statements.Journal of Accounting and Economics, 65(1):1--20.
Brennan, R. L. (2001).Generalizability Theory. Springer, New York.
39

Cao, S., Jiang, W., Wang, J., and Yang, B. (2024). From Man vs. Machine to Man + Machine:
The art and AI of stock analyses.Journal of Financial Economics, 160:103910.
Cao, S. S., Chen, W. X., Ma, G., and Srinivasan, S. (2026). Generative AI in capital markets:
Information production, dissemination, and processing.Journal of Accounting Research,
64(3):1427--1450.
Chen, J., Tang, G., Zhou, G., and Zhu, W. (2023). ChatGPT and Deepseek: Can they
predict the stock market and macroeconomy? Working Paper.
Cookson, J. A., Fathollahi, M., Grieser, W., and Venugopal, B. (2026). LLMs and systematic
measurement error. Available at SSRN.
de Kok, T. (2025). ChatGPT for textual analysis? how to use generative LLMs in accounting
research.Management Science, 71(9):7888--7906.
Didisheim, A., Fraschini, M., and Somoza, L. (2025). AI's predictable memory in financial
analysis.Economics Letters.
Gao, R. and Xiao, S. C. (2026). Nonstandard errors in AI agents. Working Paper.
Glasserman, P. and Lin, C. (2023). Assessing look-ahead bias in stock return predictions
generated by GPT sentiment analysis. Working paper.
Hansen, A. L. and Kazinnik, S. (2024). Can ChatGPT decipher fedspeak? Working Paper.
Harville, D. A. (1977). Maximum likelihood approaches to variance component estimation
and to related problems.Journal of the American Statistical Association, 72(358):320--338.
Hassan, T. A., Hollander, S., Van Lent, L., and Tahoun, A. (2019). Firm-level political risk:
Measurement and effects.The Quarterly Journal of Economics, 134(4):2135--2202.
He, B., Mostrom, L. I., and Sufi, A. (2025). Investing in customer capital. Working Paper
33171, National Bureau of Economic Research.
40

Hope, O.-K., Hu, D., and Lu, H. (2016). The benefits of specific risk-factor disclosures.
Review of Accounting Studies, 21(4):1005--1045.
Huang, W., Menkveld, A. J., and Yu, S. (2026). AI ``errors"". Available at SSRN.
Iacoviello, M. and Tong, J. (2026). The AI-GPR index: Measuring geopolitical risk using
artificial intelligence. Working Paper.
Jha, M., Qian, J., Weber, M., and Yang, B. (2025). ChatGPT and corporate policies. Working
Paper.
Jia, N., Li, N., Ma, G., and Xu, D. (2026). Corporate responses to generative AI: Early
evidence from conference calls.Review of Accounting Studies, 31(2):649--703.
Kong, Y., Lee, H., Hwang, Y., Lopez-Lira, A., Levy, B., Mehta, D., Wen, Q., Choi, C., Lee,
Y., and Zohren, S. (2026). Evaluating LLMs in finance requires explicit bias consideration.
Working paper.
Levy, B. (2026). Caution ahead: Numerical reasoning and look-ahead bias in AI models.
Journal of Accounting Research, 64(3):1139--1188.
Li, F. (2008). Annual report readability, current earnings, and earnings persistence.Journal
of Accounting and Economics, 45(2--3):221--247.
Li, K., Mai, F., Shen, R., and Yan, X. (2021). Measuring corporate culture using machine
learning.The Review of Financial Studies, 34(7):3265--3315.
Li, K., Mai, F., Shen, R., Yang, C., and Zhang, T. (2026). Dissecting corporate culture using
generative AI: Insights from analyst reports.Review of Financial Studies, 39(1):253--296.
Liu, Y., Liu, J., and Wang, T. (2026). Large language model disagreement. Working Paper,
version of June 2026 (first version August 2025).
41

Lopez-Lira, A. and Tang, Y. (2026). Can ChatGPT forecast stock price movements? return
predictability and large language models.Journal of Financial Economics. Forthcoming.
Lopez-Lira, A., Tang, Y., and Zhu, M. (2025). The memorization problem: Can we trust
LLMs' economic forecasts?
Loughran, T. and McDonald, B. (2011). When Is a Liability Not a Liability? Textual
Analysis, Dictionaries, and 10-Ks.Journal of Finance, 66(1):35 -- 65.
Loughran, T. and McDonald, B. (2024). Measuring firm complexity.Journal of Financial
and Quantitative Analysis, 59(6):2487--2514.
Ludwig, J., Mullainathan, S., and Rambachan, A. (2026). Large language models: An applied
econometric framework.Annual Review of Economics, 18:283--316.
Matsumoto, D., Pronk, M., and Roelofsen, E. (2011). What makes conference calls useful?
the information content of managers' presentations and analysts' discussion sessions.The
Accounting Review, 86(4):1383--1414.
Nagel, S., Tseng, C., and Xiu, D. (2026). Completions, not convictions: Can llm probabilities
proxy for human beliefs? Available at SSRN:https://ssrn.com/abstract=7265538.
Ottonello, P., Song, W., and Sotelo, S. (2024). An anatomy of firms' political speech. Working
Paper 32923, National Bureau of Economic Research. Available at SSRN.
Patterson, H. D. and Thompson, R. (1971). Recovery of inter-block information when block
sizes are unequal.Biometrika, 58(3):545--554.
Sarkar, S. and Vafa, K. (2025). Lookahead bias in pretrained language models. Working
Paper.
Sautner, Z., Van Lent, L., Vilkov, G., and Zhang, R. (2023). Firm-level climate change
exposure.The Journal of Finance, 78(3):1449--1498.
42

Shaffer, M. and Wang, C. C. Y. (2026). Harnessing large language models for core earnings
measurement.SSRN Working Paper.
Wang, J. J. and Wang, V. X. (2025). Assessing consistency and reproducibility in the outputs
of large language models: Evidence across diverse finance and accounting tasks. Working
paper.
43

Exhibits and Tables
Figure 1:\mathrm{I}\mathrm{n}\mathrm{t}\mathrm{e}\mathrm{r}-\mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}: \mathrm{h}\mathrm{i}\mathrm{g}\mathrm{h}\mathrm{e}\mathrm{s}\mathrm{t}- \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{l}\mathrm{o}\mathrm{w}\mathrm{e}\mathrm{s}\mathrm{t}-\mathrm{a}\mathrm{g}\mathrm{r}\mathrm{e}\mathrm{e}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{t} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t}\mathrm{s}. \mathrm{P}\mathrm{a}\mathrm{i}\mathrm{r}\mathrm{w}\mathrm{i}\mathrm{s}\mathrm{e}
\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s} \mathrm{b}\mathrm{e}\mathrm{t}\mathrm{w}\mathrm{e}\mathrm{e}\mathrm{n} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{n} \mathrm{L}\mathrm{L}\mathrm{M} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}\mathrm{s}' \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}\mathrm{s} (\mathrm{u}\mathrm{p}\mathrm{p}\mathrm{e}\mathrm{r} \mathrm{t}\mathrm{r}\mathrm{i}\mathrm{a}\mathrm{n}\mathrm{g}\mathrm{l}\mathrm{e}: \mathrm{P}\mathrm{e}\mathrm{a}\mathrm{r}\mathrm{s}\mathrm{o}\mathrm{n}; \mathrm{l}\mathrm{o}\mathrm{w}\mathrm{e}\mathrm{r} \mathrm{t}\mathrm{r}\mathrm{i}\mathrm{a}\mathrm{n}\mathrm{g}\mathrm{l}\mathrm{e}:
\mathrm{S}\mathrm{p}\mathrm{e}\mathrm{a}\mathrm{r}\mathrm{m}\mathrm{a}\mathrm{n}) \mathrm{f}\mathrm{o}\mathrm{r} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{t}\mathrm{w}\mathrm{o} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t}\mathrm{s} \mathrm{w}\mathrm{i}\mathrm{t}\mathrm{h} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{h}\mathrm{i}\mathrm{g}\mathrm{h}\mathrm{e}\mathrm{s}\mathrm{t} \mathrm{m}\mathrm{e}\mathrm{a}\mathrm{n} \mathrm{p}\mathrm{a}\mathrm{i}\mathrm{r}\mathrm{w}\mathrm{i}\mathrm{s}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}---\mathrm{s}\mathrm{e}\mathrm{n}\mathrm{t}\mathrm{i}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{t} \mathrm{a}\mathrm{n}\mathrm{d}
\mathrm{i}\mathrm{n}\mathrm{n}\mathrm{o}\mathrm{v}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}---\mathrm{a}\mathrm{n}\mathrm{d} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{t}\mathrm{w}\mathrm{o} \mathrm{w}\mathrm{i}\mathrm{t}\mathrm{h} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{l}\mathrm{o}\mathrm{w}\mathrm{e}\mathrm{s}\mathrm{t}---\mathrm{i}\mathrm{n}\mathrm{t}\mathrm{e}\mathrm{g}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{p}\mathrm{e}\mathrm{c}\mathrm{i}fi\mathrm{c}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{r}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}. \mathrm{T}\mathrm{h}\mathrm{e} \mathrm{l}\mathrm{a}\mathrm{s}\mathrm{t} \mathrm{r}\mathrm{o}\mathrm{w} \mathrm{a}\mathrm{n}\mathrm{d}
\mathrm{c}\mathrm{o}\mathrm{l}\mathrm{u}\mathrm{m}\mathrm{n} \mathrm{r}\mathrm{e}\mathrm{p}\mathrm{o}\mathrm{r}\mathrm{t} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{o}\mathrm{f} \mathrm{e}\mathrm{a}\mathrm{c}\mathrm{h} \mathrm{L}\mathrm{L}\mathrm{M} \mathrm{m}\mathrm{e}\mathrm{a}\mathrm{s}\mathrm{u}\mathrm{r}\mathrm{e} \mathrm{w}\mathrm{i}\mathrm{t}\mathrm{h} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{s}\mathrm{p}\mathrm{o}\mathrm{n}\mathrm{d}\mathrm{i}\mathrm{n}\mathrm{g} \mathrm{t}\mathrm{r}\mathrm{a}\mathrm{d}\mathrm{i}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{a}\mathrm{l}, \mathrm{n}\mathrm{o}\mathrm{n}-\mathrm{L}\mathrm{L}\mathrm{M}
\mathrm{b}\mathrm{e}\mathrm{n}\mathrm{c}\mathrm{h}\mathrm{m}\mathrm{a}\mathrm{r}\mathrm{k} \mathrm{f}\mathrm{o}\mathrm{r} \mathrm{t}\mathrm{h}\mathrm{a}\mathrm{t} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t}. \mathrm{T}\mathrm{h}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{l}\mathrm{o}\mathrm{u}\mathrm{r} \mathrm{s}\mathrm{c}\mathrm{a}\mathrm{l}\mathrm{e} \mathrm{i}\mathrm{s} \mathrm{i}\mathrm{d}\mathrm{e}\mathrm{n}\mathrm{t}\mathrm{i}\mathrm{c}\mathrm{a}\mathrm{l} \mathrm{t}\mathrm{o} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{h}\mathrm{e}\mathrm{a}\mathrm{t}\mathrm{m}\mathrm{a}\mathrm{p}\mathrm{s} \mathrm{f}\mathrm{o}\mathrm{r} \mathrm{a}\mathrm{l}\mathrm{l}
\mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t}\mathrm{s} \mathrm{r}\mathrm{e}\mathrm{p}\mathrm{o}\mathrm{r}\mathrm{t}\mathrm{e}\mathrm{d} \mathrm{i}\mathrm{n} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{O}\mathrm{n}\mathrm{l}\mathrm{i}\mathrm{n}\mathrm{e} \mathrm{A}\mathrm{p}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{d}\mathrm{i}\mathrm{x} (\mathrm{A}\mathrm{p}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{d}\mathrm{i}\mathrm{x} \mathrm{A}).
44

Table 1:\mathrm{S}\mathrm{u}\mathrm{m}\mathrm{m}\mathrm{a}\mathrm{r}\mathrm{y} \mathrm{S}\mathrm{t}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{i}\mathrm{c}\mathrm{s}
\mathrm{N} \mathrm{M}\mathrm{e}\mathrm{a}\mathrm{n} \mathrm{S}\mathrm{t}\mathrm{d} \mathrm{M}\mathrm{i}\mathrm{n} \mathrm{P}25 \mathrm{M}\mathrm{e}\mathrm{d}\mathrm{i}\mathrm{a}\mathrm{n} \mathrm{P}75 \mathrm{M}\mathrm{a}\mathrm{x}
LLM-related variables (call\times construct level)
\mathrm{L}\mathrm{L}\mathrm{M} \mathrm{D}\mathrm{i}\mathrm{s}\mathrm{p}\mathrm{e}\mathrm{r}\mathrm{s}\mathrm{i}\mathrm{o}\mathrm{n} (\mathrm{Z}) 25,298 0.618 0.315 0.067 0.415 0.583 0.784 2.787
\mathrm{J}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{i}\mathrm{f}. \mathrm{C}\mathrm{o}\mathrm{s}\mathrm{i}\mathrm{n}\mathrm{e} \mathrm{S}\mathrm{i}\mathrm{m} 25,298 0.618 0.102 0.204 0.564 0.624 0.682 0.931
\mathrm{J}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{i}\mathrm{f}. \mathrm{J}\mathrm{a}\mathrm{c}\mathrm{c}\mathrm{a}\mathrm{r}\mathrm{d} \mathrm{S}\mathrm{i}\mathrm{m} 25,298 0.183 0.061 0.010 0.150 0.169 0.193 0.584
Firm-level variables (call level)
\mathrm{l}\mathrm{n}(\mathrm{A}\mathrm{s}\mathrm{s}\mathrm{e}\mathrm{t}\mathrm{s}) 1,945 10.348 1.281 7.288 9.498 10.246 11.102 15.253
\mathrm{B}\mathrm{o}\mathrm{o}\mathrm{k}-\mathrm{t}\mathrm{o}-\mathrm{M}\mathrm{a}\mathrm{r}\mathrm{k}\mathrm{e}\mathrm{t} 1,942 0.328 0.308 -0.638 0.114 0.257 0.483 2.380
\mathrm{T}\mathrm{o}\mathrm{b}\mathrm{i}\mathrm{n}'\mathrm{s} \mathrm{Q} 1,942 2.892 2.713 0.760 1.346 1.961 3.386 34.202
\mathrm{S}\mathrm{U}\mathrm{E} 1,898 2.107 3.177 -5.769 0.279 1.634 3.300 14.696
\mathrm{C}\mathrm{A}\mathrm{R}(0,1) 1,935 0.020 6.542 -20.733 -3.921 -0.106 4.066 17.321
\mathrm{A}\mathrm{n}\mathrm{a}\mathrm{l}\mathrm{y}\mathrm{s}\mathrm{t} \mathrm{D}\mathrm{i}\mathrm{s}\mathrm{p}. (\mathrm{Q}1) 1,935 0.070 0.103 0.003 0.019 0.037 0.076 0.693
\mathrm{A}\mathrm{n}\mathrm{a}\mathrm{l}\mathrm{y}\mathrm{s}\mathrm{t} \mathrm{C}\mathrm{o}\mathrm{u}\mathrm{n}\mathrm{t} (\mathrm{Q}1) 1,937 15.126 6.579 3.000 11.000 15.000 19.000 36.000
\mathrm{P}\mathrm{r}\mathrm{e}-\mathrm{C}\mathrm{a}\mathrm{l}\mathrm{l} \mathrm{A}\mathrm{n}\mathrm{a}\mathrm{l}\mathrm{y}\mathrm{s}\mathrm{t} \mathrm{D}\mathrm{i}\mathrm{s}\mathrm{p}. 1,933 0.071 0.111 0.003 0.019 0.037 0.074 0.799
\mathrm{P}\mathrm{r}\mathrm{e}-\mathrm{C}\mathrm{a}\mathrm{l}\mathrm{l} \mathrm{A}\mathrm{n}\mathrm{a}\mathrm{l}\mathrm{y}\mathrm{s}\mathrm{t} \mathrm{C}\mathrm{o}\mathrm{u}\mathrm{n}\mathrm{t} 1,934 15.989 6.421 4.000 11.000 16.000 20.000 38.000
Textual variables (call level)
\mathrm{F}\mathrm{o}\mathrm{g} \mathrm{I}\mathrm{n}\mathrm{d}\mathrm{e}\mathrm{x} 1,946 7.381 0.836 5.112 6.809 7.301 7.868 11.633
\mathrm{l}\mathrm{n}(\mathrm{W}\mathrm{o}\mathrm{r}\mathrm{d} \mathrm{C}\mathrm{o}\mathrm{u}\mathrm{n}\mathrm{t}) 1,946 8.243 0.352 4.682 8.067 8.278 8.461 9.091
\mathrm{F}\mathrm{i}\mathrm{n}\mathrm{a}\mathrm{n}\mathrm{c}\mathrm{i}\mathrm{a}\mathrm{l} \mathrm{J}\mathrm{a}\mathrm{r}\mathrm{g}\mathrm{o}\mathrm{n} 1,946 0.063 0.011 0.032 0.056 0.063 0.070 0.110
\mathrm{N}\mathrm{u}\mathrm{m}\mathrm{b}\mathrm{e}\mathrm{r}\mathrm{s} 1,946 0.012 0.005 0.000 0.008 0.011 0.015 0.036
\mathrm{F}\mathrm{o}\mathrm{r}\mathrm{w}\mathrm{a}\mathrm{r}\mathrm{d}-\mathrm{L}\mathrm{o}\mathrm{o}\mathrm{k}\mathrm{i}\mathrm{n}\mathrm{g} 1,946 0.057 0.012 0.023 0.049 0.056 0.064 0.187
\mathrm{S}\mathrm{p}\mathrm{e}\mathrm{c}\mathrm{i}fi\mathrm{c}\mathrm{i}\mathrm{t}\mathrm{y} 1,946 0.013 0.004 0.004 0.011 0.013 0.016 0.040
Notes:\mathrm{T}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{a}\mathrm{m}\mathrm{p}\mathrm{l}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{s} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{q}\mathrm{u}\mathrm{e}\mathrm{s}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}-\mathrm{a}\mathrm{n}\mathrm{d}-\mathrm{a}\mathrm{n}\mathrm{s}\mathrm{w}\mathrm{e}\mathrm{r} \mathrm{s}\mathrm{e}\mathrm{c}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s} \mathrm{o}\mathrm{f} 1,946 \mathrm{e}\mathrm{a}\mathrm{r}\mathrm{n}\mathrm{i}\mathrm{n}\mathrm{g}\mathrm{s} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l}\mathrm{s} \mathrm{h}\mathrm{e}\mathrm{l}\mathrm{d} \mathrm{b}\mathrm{y} \mathrm{S}\&\mathrm{P} 500
fi\mathrm{r}\mathrm{m}\mathrm{s} \mathrm{i}\mathrm{n} 2024, \mathrm{e}\mathrm{a}\mathrm{c}\mathrm{h} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}\mathrm{d} \mathrm{o}\mathrm{n} 13 \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t}\mathrm{s} \mathrm{b}\mathrm{y} 7 \mathrm{L}\mathrm{L}\mathrm{M} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}\mathrm{s}. \mathrm{L}\mathrm{L}\mathrm{M}-\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{e}\mathrm{d} \mathrm{v}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{a}\mathrm{b}\mathrm{l}\mathrm{e}\mathrm{s} \mathrm{a}\mathrm{r}\mathrm{e} \mathrm{m}\mathrm{e}\mathrm{a}\mathrm{s}\mathrm{u}\mathrm{r}\mathrm{e}\mathrm{d} \mathrm{a}\mathrm{t}
\mathrm{t}\mathrm{h}\mathrm{e} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l}\times \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} \mathrm{l}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{l}; fi\mathrm{r}\mathrm{m}-\mathrm{l}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{l} \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{t}\mathrm{e}\mathrm{x}\mathrm{t}\mathrm{u}\mathrm{a}\mathrm{l} \mathrm{v}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{a}\mathrm{b}\mathrm{l}\mathrm{e}\mathrm{s} \mathrm{a}\mathrm{r}\mathrm{e} \mathrm{m}\mathrm{e}\mathrm{a}\mathrm{s}\mathrm{u}\mathrm{r}\mathrm{e}\mathrm{d} \mathrm{o}\mathrm{n}\mathrm{c}\mathrm{e} \mathrm{p}\mathrm{e}\mathrm{r} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l}, \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{t}\mathrm{h}\mathrm{e}\mathrm{i}\mathrm{r} \mathrm{s}\mathrm{t}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{i}\mathrm{c}\mathrm{s} \mathrm{a}\mathrm{r}\mathrm{e}
\mathrm{c}\mathrm{o}\mathrm{m}\mathrm{p}\mathrm{u}\mathrm{t}\mathrm{e}\mathrm{d} \mathrm{o}\mathrm{n} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l}-\mathrm{l}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{l} \mathrm{p}\mathrm{a}\mathrm{n}\mathrm{e}\mathrm{l}. \mathrm{V}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{a}\mathrm{b}\mathrm{l}\mathrm{e} \mathrm{d}\mathrm{e}fi\mathrm{n}\mathrm{i}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s} \mathrm{a}\mathrm{p}\mathrm{p}\mathrm{e}\mathrm{a}\mathrm{r} \mathrm{i}\mathrm{n} \mathrm{T}\mathrm{a}\mathrm{b}\mathrm{l}\mathrm{e} \mathrm{A}1. \mathrm{P}\mathrm{e}\mathrm{r}-\mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} \mathrm{s}\mathrm{u}\mathrm{m}\mathrm{m}\mathrm{a}\mathrm{r}\mathrm{y} \mathrm{s}\mathrm{t}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{i}\mathrm{c}\mathrm{s}
\mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{i}\mathrm{n}\mathrm{d}\mathrm{i}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{u}\mathrm{a}\mathrm{l} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}\mathrm{s}' \mathrm{z}-\mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}\mathrm{d} \mathrm{L}\mathrm{L}\mathrm{M} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}\mathrm{s} \mathrm{a}\mathrm{r}\mathrm{e} \mathrm{r}\mathrm{e}\mathrm{p}\mathrm{o}\mathrm{r}\mathrm{t}\mathrm{e}\mathrm{d} \mathrm{i}\mathrm{n} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{O}\mathrm{n}\mathrm{l}\mathrm{i}\mathrm{n}\mathrm{e} \mathrm{A}\mathrm{p}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{d}\mathrm{i}\mathrm{x} (\mathrm{T}\mathrm{a}\mathrm{b}\mathrm{l}\mathrm{e} \mathrm{O}\mathrm{A}.\mathrm{B}.1).
45

Table 2:\mathrm{I}\mathrm{n}\mathrm{t}\mathrm{e}\mathrm{r}-\mathrm{P}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r} \mathrm{A}\mathrm{g}\mathrm{r}\mathrm{e}\mathrm{e}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{t} \mathrm{b}\mathrm{y} \mathrm{C}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t}: \mathrm{D}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{i}\mathrm{b}\mathrm{u}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}
\mathrm{o}\mathrm{f} \mathrm{P}\mathrm{a}\mathrm{i}\mathrm{r}\mathrm{w}\mathrm{i}\mathrm{s}\mathrm{e} \mathrm{S}\mathrm{p}\mathrm{e}\mathrm{a}\mathrm{r}\mathrm{m}\mathrm{a}\mathrm{n} \mathrm{C}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
\mathrm{C}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t}N\mathrm{M}\mathrm{i}\mathrm{n} \mathrm{M}\mathrm{e}\mathrm{a}\mathrm{n} \mathrm{M}\mathrm{e}\mathrm{d}\mathrm{i}\mathrm{a}\mathrm{n} \mathrm{M}\mathrm{a}\mathrm{x}
Sentiment 1,946 0.77 0.85 0.86 0.90
\mathrm{I}\mathrm{n}\mathrm{n}\mathrm{o}\mathrm{v}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} 1,946 0.59 0.76 0.75 0.87
\mathrm{U}\mathrm{n}\mathrm{c}\mathrm{e}\mathrm{r}\mathrm{t}\mathrm{a}\mathrm{i}\mathrm{n}\mathrm{t}\mathrm{y} 1,946 0.54 0.64 0.62 0.75
\mathrm{C}\mathrm{l}\mathrm{i}\mathrm{m}\mathrm{a}\mathrm{t}\mathrm{e} \mathrm{R}\mathrm{i}\mathrm{s}\mathrm{k} 1,946 0.36 0.58 0.53 0.79
\mathrm{S}\mathrm{p}\mathrm{e}\mathrm{c}\mathrm{i}fi\mathrm{c}\mathrm{i}\mathrm{t}\mathrm{y} 1,946 0.34 0.54 0.51 0.70
\mathrm{M}\mathrm{a}\mathrm{n}\mathrm{a}\mathrm{g}\mathrm{e}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{t} \mathrm{C}\mathrm{l}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} 1,946 0.38 0.53 0.51 0.66
\mathrm{P}\mathrm{o}\mathrm{l}\mathrm{i}\mathrm{t}\mathrm{i}\mathrm{c}\mathrm{a}\mathrm{l} \mathrm{R}\mathrm{i}\mathrm{s}\mathrm{k} 1,946 0.30 0.52 0.53 0.64
\mathrm{C}\mathrm{o}\mathrm{r}\mathrm{p}\mathrm{o}\mathrm{r}\mathrm{a}\mathrm{t}\mathrm{e} \mathrm{C}\mathrm{u}\mathrm{l}\mathrm{t}\mathrm{u}\mathrm{r}\mathrm{e} 1,938 0.33 0.49 0.48 0.66
\mathrm{T}\mathrm{e}\mathrm{a}\mathrm{m}\mathrm{w}\mathrm{o}\mathrm{r}\mathrm{k} 1,939 0.37 0.49 0.49 0.62
\mathrm{Q}\mathrm{u}\mathrm{a}\mathrm{l}\mathrm{i}\mathrm{t}\mathrm{y} 1,942 0.27 0.44 0.41 0.62
\mathrm{R}\mathrm{e}\mathrm{s}\mathrm{p}\mathrm{e}\mathrm{c}\mathrm{t} 1,939 0.27 0.41 0.34 0.58
\mathrm{I}\mathrm{n}\mathrm{t}\mathrm{e}\mathrm{g}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} 1,942 0.14 0.32 0.29 0.54
Specificity Ratio 1,878 0.10 0.23 0.23 0.43
\mathrm{M}\mathrm{e}\mathrm{a}\mathrm{n} 0.37 0.52 0.50 0.67
\mathrm{M}\mathrm{e}\mathrm{d}\mathrm{i}\mathrm{a}\mathrm{n} 0.34 0.52 0.51 0.66
Notes:\mathrm{F}\mathrm{o}\mathrm{r} \mathrm{e}\mathrm{a}\mathrm{c}\mathrm{h} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} \mathrm{w}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{m}\mathrm{p}\mathrm{u}\mathrm{t}\mathrm{e} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{S}\mathrm{p}\mathrm{e}\mathrm{a}\mathrm{r}\mathrm{m}\mathrm{a}\mathrm{n} \mathrm{r}\mathrm{a}\mathrm{n}\mathrm{k} \mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}
\mathrm{b}\mathrm{e}\mathrm{t}\mathrm{w}\mathrm{e}\mathrm{e}\mathrm{n} \mathrm{e}\mathrm{v}\mathrm{e}\mathrm{r}\mathrm{y} \mathrm{p}\mathrm{a}\mathrm{i}\mathrm{r} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{L}\mathrm{L}\mathrm{M} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}\mathrm{s} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{i}\mathrm{n}\mathrm{g} \mathrm{i}\mathrm{t} (\mathrm{t}\mathrm{h}\mathrm{e} \mathrm{n}\mathrm{o}\mathrm{n}-\mathrm{L}\mathrm{L}\mathrm{M}
\mathrm{b}\mathrm{e}\mathrm{n}\mathrm{c}\mathrm{h}\mathrm{m}\mathrm{a}\mathrm{r}\mathrm{k} \mathrm{i}\mathrm{s} \mathrm{e}\mathrm{x}\mathrm{c}\mathrm{l}\mathrm{u}\mathrm{d}\mathrm{e}\mathrm{d}) \mathrm{a}\mathrm{c}\mathrm{r}\mathrm{o}\mathrm{s}\mathrm{s} \mathrm{a}\mathrm{l}\mathrm{l} \mathrm{t}\mathrm{r}\mathrm{a}\mathrm{n}\mathrm{s}\mathrm{c}\mathrm{r}\mathrm{i}\mathrm{p}\mathrm{t}\mathrm{s}, \mathrm{t}\mathrm{h}\mathrm{e}\mathrm{n} \mathrm{s}\mathrm{u}\mathrm{m}\mathrm{m}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{z}\mathrm{e} \mathrm{t}\mathrm{h}\mathrm{e}
\mathrm{r}\mathrm{e}\mathrm{s}\mathrm{u}\mathrm{l}\mathrm{t}\mathrm{i}\mathrm{n}\mathrm{g} \mathrm{p}\mathrm{a}\mathrm{i}\mathrm{r}\mathrm{w}\mathrm{i}\mathrm{s}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}. N \mathrm{i}\mathrm{s} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{n}\mathrm{u}\mathrm{m}\mathrm{b}\mathrm{e}\mathrm{r} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{r}\mathrm{a}\mathrm{n}\mathrm{s}\mathrm{c}\mathrm{r}\mathrm{i}\mathrm{p}\mathrm{t}\mathrm{s} \mathrm{f}\mathrm{o}\mathrm{r} \mathrm{w}\mathrm{h}\mathrm{i}\mathrm{c}\mathrm{h}
\mathrm{a}\mathrm{l}\mathrm{l} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}\mathrm{s} \mathrm{h}\mathrm{a}\mathrm{v}\mathrm{e} \mathrm{a} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}. \mathrm{C}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t}\mathrm{s} \mathrm{a}\mathrm{r}\mathrm{e} \mathrm{o}\mathrm{r}\mathrm{d}\mathrm{e}\mathrm{r}\mathrm{e}\mathrm{d} \mathrm{b}\mathrm{y} \mathrm{m}\mathrm{e}\mathrm{a}\mathrm{n} \mathrm{p}\mathrm{a}\mathrm{i}\mathrm{r}\mathrm{w}\mathrm{i}\mathrm{s}\mathrm{e}
\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}; \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{m}\mathrm{o}\mathrm{s}\mathrm{t} (\mathrm{l}\mathrm{e}\mathrm{a}\mathrm{s}\mathrm{t}) \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{e}\mathrm{n}\mathrm{t} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} \mathrm{i}\mathrm{s} \mathrm{s}\mathrm{h}\mathrm{o}\mathrm{w}\mathrm{n} \mathrm{i}\mathrm{n}bold
(italics).
46

Table 3:\mathrm{C}\mathrm{r}\mathrm{o}\mathrm{s}\mathrm{s}-\mathrm{M}\mathrm{o}\mathrm{d}\mathrm{e}\mathrm{l} \mathrm{C}\mathrm{o}\mathrm{m}\mathrm{m}\mathrm{o}\mathrm{n}\mathrm{a}\mathrm{l}\mathrm{i}\mathrm{t}\mathrm{y}: \mathrm{P}\mathrm{C}\mathrm{A} \mathrm{S}\mathrm{u}\mathrm{m}\mathrm{m}\mathrm{a}\mathrm{r}\mathrm{y}
\mathrm{C}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} \mathrm{P}\mathrm{C}1 \mathrm{V}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{a}\mathrm{n}\mathrm{c}\mathrm{e} \mathrm{E}\mathrm{x}\mathrm{p}\mathrm{l}\mathrm{a}\mathrm{i}\mathrm{n}\mathrm{e}\mathrm{d} (\%) \# \mathrm{P}\mathrm{C}\mathrm{s} \mathrm{f}\mathrm{o}\mathrm{r} 90\%
Sentiment 84.95 3
\mathrm{C}\mathrm{l}\mathrm{i}\mathrm{m}\mathrm{a}\mathrm{t}\mathrm{e} \mathrm{R}\mathrm{i}\mathrm{s}\mathrm{k} 75.71 3
\mathrm{I}\mathrm{n}\mathrm{n}\mathrm{o}\mathrm{v}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} 74.28 4
\mathrm{U}\mathrm{n}\mathrm{c}\mathrm{e}\mathrm{r}\mathrm{t}\mathrm{a}\mathrm{i}\mathrm{n}\mathrm{t}\mathrm{y} 65.28 5
\mathrm{P}\mathrm{o}\mathrm{l}\mathrm{i}\mathrm{t}\mathrm{i}\mathrm{c}\mathrm{a}\mathrm{l} \mathrm{R}\mathrm{i}\mathrm{s}\mathrm{k} 64.24 4
\mathrm{S}\mathrm{p}\mathrm{e}\mathrm{c}\mathrm{i}fi\mathrm{c}\mathrm{i}\mathrm{t}\mathrm{y} 58.89 5
\mathrm{C}\mathrm{o}\mathrm{r}\mathrm{p}\mathrm{o}\mathrm{r}\mathrm{a}\mathrm{t}\mathrm{e} \mathrm{C}\mathrm{u}\mathrm{l}\mathrm{t}\mathrm{u}\mathrm{r}\mathrm{e} 57.05 5
\mathrm{T}\mathrm{e}\mathrm{a}\mathrm{m}\mathrm{w}\mathrm{o}\mathrm{r}\mathrm{k} 56.85 6
\mathrm{M}\mathrm{a}\mathrm{n}\mathrm{a}\mathrm{g}\mathrm{e}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{t} \mathrm{C}\mathrm{l}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} 55.45 5
\mathrm{Q}\mathrm{u}\mathrm{a}\mathrm{l}\mathrm{i}\mathrm{t}\mathrm{y} 52.67 6
\mathrm{R}\mathrm{e}\mathrm{s}\mathrm{p}\mathrm{e}\mathrm{c}\mathrm{t} 51.87 6
\mathrm{I}\mathrm{n}\mathrm{t}\mathrm{e}\mathrm{g}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} 45.99 6
Specificity Ratio 32.49 6
\mathrm{M}\mathrm{e}\mathrm{a}\mathrm{n} 59.67 4.9
\mathrm{M}\mathrm{e}\mathrm{d}\mathrm{i}\mathrm{a}\mathrm{n} 57.05 5.0
Notes:\mathrm{P}\mathrm{C}\mathrm{A} \mathrm{o}\mathrm{n} \mathrm{z}-\mathrm{s}\mathrm{t}\mathrm{a}\mathrm{n}\mathrm{d}\mathrm{a}\mathrm{r}\mathrm{d}\mathrm{i}\mathrm{z}\mathrm{e}\mathrm{d} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}\mathrm{s} \mathrm{f}\mathrm{r}\mathrm{o}\mathrm{m} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{L}\mathrm{L}\mathrm{M}\mathrm{s} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{i}\mathrm{n}\mathrm{g} \mathrm{e}\mathrm{a}\mathrm{c}\mathrm{h} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t}.
\mathrm{P}\mathrm{C}1 \mathrm{v}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{a}\mathrm{n}\mathrm{c}\mathrm{e} = \mathrm{c}\mathrm{r}\mathrm{o}\mathrm{s}\mathrm{s}-\mathrm{m}\mathrm{o}\mathrm{d}\mathrm{e}\mathrm{l} \mathrm{a}\mathrm{g}\mathrm{r}\mathrm{e}\mathrm{e}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{t}; \mathrm{h}\mathrm{i}\mathrm{g}\mathrm{h}\mathrm{e}\mathrm{r} \mathrm{i}\mathrm{s} \mathrm{s}\mathrm{t}\mathrm{r}\mathrm{o}\mathrm{n}\mathrm{g}\mathrm{e}\mathrm{r} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{v}\mathrm{e}\mathrm{r}\mathrm{g}\mathrm{e}\mathrm{n}\mathrm{t} \mathrm{v}\mathrm{a}\mathrm{l}\mathrm{i}\mathrm{d}\mathrm{i}\mathrm{t}\mathrm{y}.
47

Table 4:\mathrm{V}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{a}\mathrm{n}\mathrm{c}\mathrm{e} \mathrm{D}\mathrm{e}\mathrm{c}\mathrm{o}\mathrm{m}\mathrm{p}\mathrm{o}\mathrm{s}\mathrm{i}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{o}\mathrm{f} \mathrm{L}\mathrm{L}\mathrm{M} \mathrm{S}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}\mathrm{s}: \mathrm{P}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r} \mathrm{C}\mathrm{a}\mathrm{l}\mathrm{i}\mathrm{b}\mathrm{r}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{v}\mathrm{s}. \mathrm{T}\mathrm{r}\mathrm{a}\mathrm{n}\mathrm{s}\mathrm{c}\mathrm{r}\mathrm{i}\mathrm{p}\mathrm{t}
\mathrm{A}\mathrm{m}\mathrm{b}\mathrm{i}\mathrm{g}\mathrm{u}\mathrm{i}\mathrm{t}\mathrm{y}
\mathrm{C}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} \mathrm{T}\mathrm{r}\mathrm{a}\mathrm{n}\mathrm{s}\mathrm{c}\mathrm{r}\mathrm{i}\mathrm{p}\mathrm{t} \mathrm{P}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r} \mathrm{R}\mathrm{e}\mathrm{s}\mathrm{i}\mathrm{d}\mathrm{u}\mathrm{a}\mathrm{l}G\Phi N
(\% \mathrm{o}\mathrm{f} \mathrm{T}\mathrm{o}\mathrm{t}\mathrm{a}\mathrm{l}) (\% \mathrm{o}\mathrm{f} \mathrm{T}\mathrm{o}\mathrm{t}\mathrm{a}\mathrm{l}) (\% \mathrm{o}\mathrm{f} \mathrm{T}\mathrm{o}\mathrm{t}\mathrm{a}\mathrm{l})
\mathrm{S}\mathrm{e}\mathrm{n}\mathrm{t}\mathrm{i}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{t} 74.0\% 9.9\% 16.1\% 0.970 0.952 13,622
\mathrm{I}\mathrm{n}\mathrm{n}\mathrm{o}\mathrm{v}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} 52.0\% 24.6\% 23.4\% 0.940 0.884 13,622
\mathrm{C}\mathrm{l}\mathrm{i}\mathrm{m}\mathrm{a}\mathrm{t}\mathrm{e} \mathrm{R}\mathrm{i}\mathrm{s}\mathrm{k} 58.5\% 10.1\% 31.4\% 0.929 0.908 13,622
\mathrm{U}\mathrm{n}\mathrm{c}\mathrm{e}\mathrm{r}\mathrm{t}\mathrm{a}\mathrm{i}\mathrm{n}\mathrm{t}\mathrm{y} 20.9\% 62.3\% 16.9\% 0.896 0.648 13,622
\mathrm{S}\mathrm{p}\mathrm{e}\mathrm{c}\mathrm{i}fi\mathrm{c}\mathrm{i}\mathrm{t}\mathrm{y} 42.4\% 15.0\% 42.6\% 0.875 0.838 13,622
\mathrm{C}\mathrm{o}\mathrm{r}\mathrm{p}\mathrm{o}\mathrm{r}\mathrm{a}\mathrm{t}\mathrm{e} \mathrm{C}\mathrm{u}\mathrm{l}\mathrm{t}\mathrm{u}\mathrm{r}\mathrm{e} 30.2\% 36.3\% 33.5\% 0.863 0.752 13,566
\mathrm{T}\mathrm{e}\mathrm{a}\mathrm{m}\mathrm{w}\mathrm{o}\mathrm{r}\mathrm{k} 30.1\% 36.2\% 33.7\% 0.862 0.751 13,573
\mathrm{P}\mathrm{o}\mathrm{l}\mathrm{i}\mathrm{t}\mathrm{i}\mathrm{c}\mathrm{a}\mathrm{l} \mathrm{R}\mathrm{i}\mathrm{s}\mathrm{k} 47.9\% 4.9\% 47.2\% 0.835 0.821 9,730
\mathrm{Q}\mathrm{u}\mathrm{a}\mathrm{l}\mathrm{i}\mathrm{t}\mathrm{y} 28.4\% 32.3\% 39.3\% 0.835 0.735 13,594
\mathrm{R}\mathrm{e}\mathrm{s}\mathrm{p}\mathrm{e}\mathrm{c}\mathrm{t} 20.6\% 45.9\% 33.4\% 0.812 0.645 13,573
\mathrm{M}\mathrm{a}\mathrm{n}\mathrm{a}\mathrm{g}\mathrm{e}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{t} \mathrm{C}\mathrm{l}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} 25.5\% 29.1\% 45.4\% 0.797 0.706 13,622
\mathrm{I}\mathrm{n}\mathrm{t}\mathrm{e}\mathrm{g}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} 12.8\% 58.8\% 28.4\% 0.760 0.508 13,594
\mathrm{S}\mathrm{p}\mathrm{e}\mathrm{c}\mathrm{i}fi\mathrm{c}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{R}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o} 3.9\% 68.3\% 27.9\% 0.492 0.219 13,146
Average34.4\% 33.4\% 32.2\% 0.836 0.720 13,269
Notes:\mathrm{V}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{a}\mathrm{n}\mathrm{c}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{m}\mathrm{p}\mathrm{o}\mathrm{n}\mathrm{e}\mathrm{n}\mathrm{t}\mathrm{s} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{c}\mathrm{r}\mathrm{o}\mathrm{s}\mathrm{s}\mathrm{e}\mathrm{d} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l} \times \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r} \mathrm{r}\mathrm{a}\mathrm{n}\mathrm{d}\mathrm{o}\mathrm{m}-\mathrm{e}ff\mathrm{e}\mathrm{c}\mathrm{t}\mathrm{s} \mathrm{m}\mathrm{o}\mathrm{d}\mathrm{e}\mathrm{l}, \mathrm{e}\mathrm{s}\mathrm{t}\mathrm{i}\mathrm{m}\mathrm{a}\mathrm{t}\mathrm{e}\mathrm{d} \mathrm{p}\mathrm{e}\mathrm{r}
\mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} \mathrm{f}\mathrm{r}\mathrm{o}\mathrm{m} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{t}\mathrm{w}\mathrm{o}-\mathrm{w}\mathrm{a}\mathrm{y} \mathrm{a}\mathrm{n}\mathrm{a}\mathrm{l}\mathrm{y}\mathrm{s}\mathrm{i}\mathrm{s}-\mathrm{o}\mathrm{f}-\mathrm{v}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{a}\mathrm{n}\mathrm{c}\mathrm{e} \mathrm{m}\mathrm{e}\mathrm{a}\mathrm{n} \mathrm{s}\mathrm{q}\mathrm{u}\mathrm{a}\mathrm{r}\mathrm{e}\mathrm{s} \mathrm{o}\mathrm{n} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l}\mathrm{s} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}\mathrm{d} \mathrm{b}\mathrm{y} \mathrm{e}\mathrm{v}\mathrm{e}\mathrm{r}\mathrm{y} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}
(\^\sigma 2 r = MS r, \^\sigma 2 t = (MS t - MS r)/k, \^\sigma 2 p = (MS p - MS r)/nt; \mathrm{n}\mathrm{e}\mathrm{g}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{v}\mathrm{e} \mathrm{e}\mathrm{s}\mathrm{t}\mathrm{i}\mathrm{m}\mathrm{a}\mathrm{t}\mathrm{e}\mathrm{s} \mathrm{s}\mathrm{e}\mathrm{t} \mathrm{t}\mathrm{o} \mathrm{z}\mathrm{e}\mathrm{r}\mathrm{o}); \mathrm{f}\mathrm{o}\mathrm{r}
\mathrm{t}\mathrm{h}\mathrm{i}\mathrm{s} \mathrm{b}\mathrm{a}\mathrm{l}\mathrm{a}\mathrm{n}\mathrm{c}\mathrm{e}\mathrm{d} \mathrm{d}\mathrm{e}\mathrm{s}\mathrm{i}\mathrm{g}\mathrm{n} \mathrm{t}\mathrm{h}\mathrm{e}\mathrm{s}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{i}\mathrm{n}\mathrm{c}\mathrm{i}\mathrm{d}\mathrm{e} \mathrm{w}\mathrm{i}\mathrm{t}\mathrm{h} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{R}\mathrm{E}\mathrm{M}\mathrm{L} \mathrm{e}\mathrm{s}\mathrm{t}\mathrm{i}\mathrm{m}\mathrm{a}\mathrm{t}\mathrm{e}\mathrm{s}. G =\sigma 2 t/(\sigma 2 t +\sigma 2 r/k) \mathrm{i}\mathrm{s} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{v}\mathrm{e}
\mathrm{g}\mathrm{e}\mathrm{n}\mathrm{e}\mathrm{r}\mathrm{a}\mathrm{l}\mathrm{i}\mathrm{z}\mathrm{a}\mathrm{b}\mathrm{i}\mathrm{l}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{c}\mathrm{o}\mathrm{e}ffi\mathrm{c}\mathrm{i}\mathrm{e}\mathrm{n}\mathrm{t} \mathrm{a}\mathrm{n}\mathrm{d} \Phi = \sigma 2 t/(\sigma 2 t +\sigma 2 p/k +\sigma 2 r/k) \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{a}\mathrm{b}\mathrm{s}\mathrm{o}\mathrm{l}\mathrm{u}\mathrm{t}\mathrm{e} \mathrm{d}\mathrm{e}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{d}\mathrm{a}\mathrm{b}\mathrm{i}\mathrm{l}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{c}\mathrm{o}\mathrm{e}ffi\mathrm{c}\mathrm{i}\mathrm{e}\mathrm{n}\mathrm{t} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e}
k-\mathrm{m}\mathrm{o}\mathrm{d}\mathrm{e}\mathrm{l} \mathrm{a}\mathrm{v}\mathrm{e}\mathrm{r}\mathrm{a}\mathrm{g}\mathrm{e}, \mathrm{w}\mathrm{i}\mathrm{t}\mathrm{h} k \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{n}\mathrm{u}\mathrm{m}\mathrm{b}\mathrm{e}\mathrm{r} \mathrm{o}\mathrm{f} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}\mathrm{s} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{i}\mathrm{n}\mathrm{g} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t}. \mathrm{N}\mathrm{o}\mathrm{t}\mathrm{e} \mathrm{t}\mathrm{h}\mathrm{a}\mathrm{t} k \mathrm{i}\mathrm{s} \mathrm{e}\mathrm{q}\mathrm{u}\mathrm{a}\mathrm{l} \mathrm{t}\mathrm{o} fi\mathrm{v}\mathrm{e}
\mathrm{f}\mathrm{o}\mathrm{r} \mathrm{p}\mathrm{o}\mathrm{l}\mathrm{i}\mathrm{t}\mathrm{i}\mathrm{c}\mathrm{a}\mathrm{l} \mathrm{r}\mathrm{i}\mathrm{s}\mathrm{k}. \Phi \mathrm{a}\mathrm{d}\mathrm{d}\mathrm{i}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{a}\mathrm{l}\mathrm{l}\mathrm{y} \mathrm{p}\mathrm{e}\mathrm{n}\mathrm{a}\mathrm{l}\mathrm{i}\mathrm{z}\mathrm{e}\mathrm{s} \mathrm{s}\mathrm{t}\mathrm{a}\mathrm{b}\mathrm{l}\mathrm{e} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}-\mathrm{l}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{l} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{i}\mathrm{b}\mathrm{r}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{d}\mathrm{i}ff\mathrm{e}\mathrm{r}\mathrm{e}\mathrm{n}\mathrm{c}\mathrm{e}\mathrm{s}, \mathrm{s}\mathrm{o} \mathrm{i}\mathrm{t} \mathrm{m}\mathrm{e}\mathrm{a}\mathrm{s}\mathrm{u}\mathrm{r}\mathrm{e}\mathrm{s}
\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{i}\mathrm{a}\mathrm{b}\mathrm{i}\mathrm{l}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{o}\mathrm{f} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{l}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{l}\mathrm{s} \mathrm{r}\mathrm{a}\mathrm{t}\mathrm{h}\mathrm{e}\mathrm{r} \mathrm{t}\mathrm{h}\mathrm{a}\mathrm{n} \mathrm{o}\mathrm{f} \mathrm{r}\mathrm{a}\mathrm{n}\mathrm{k}\mathrm{i}\mathrm{n}\mathrm{g}\mathrm{s}.N\mathrm{i}\mathrm{s} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l}\mathrm{s}\times \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}\mathrm{s}.
48

Table 5:\mathrm{D}\mathrm{e}\mathrm{t}\mathrm{e}\mathrm{r}\mathrm{m}\mathrm{i}\mathrm{n}\mathrm{a}\mathrm{n}\mathrm{t}\mathrm{s} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{e}\mathrm{x}\mathrm{t}\mathrm{u}\mathrm{a}\mathrm{l} \mathrm{m}\mathrm{e}\mathrm{a}\mathrm{s}\mathrm{u}\mathrm{r}\mathrm{e} \mathrm{d}\mathrm{i}\mathrm{s}\mathrm{p}\mathrm{e}\mathrm{r}\mathrm{s}\mathrm{i}\mathrm{o}\mathrm{n} (\mathrm{s}\mathrm{t}\mathrm{a}\mathrm{n}\mathrm{d}\mathrm{a}\mathrm{r}\mathrm{d} \mathrm{d}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}).
\mathrm{T}\mathrm{e}\mathrm{x}\mathrm{t}\mathrm{u}\mathrm{a}\mathrm{l} \mathrm{M}\mathrm{e}\mathrm{a}\mathrm{s}\mathrm{u}\mathrm{r}\mathrm{e} \mathrm{D}\mathrm{i}\mathrm{s}\mathrm{p}\mathrm{e}\mathrm{r}\mathrm{s}\mathrm{i}\mathrm{o}\mathrm{n} (\mathrm{S}\mathrm{t}\mathrm{d}. \mathrm{D}\mathrm{e}\mathrm{v}.)
(1) (2) (3) (4)
Panel A: Firm Controls
\mathrm{l}\mathrm{n}(\mathrm{A}\mathrm{s}\mathrm{s}\mathrm{e}\mathrm{t}\mathrm{s}) 0.0067 \ast \ast \ast 0.0029 0.0030 0.0046 \ast \ast
(2.85) (1.22) (1.24) (2.01)
\mathrm{B}\mathrm{o}\mathrm{o}\mathrm{k}-\mathrm{t}\mathrm{o}-\mathrm{M}\mathrm{a}\mathrm{r}\mathrm{k}\mathrm{e}\mathrm{t} 0.0028 -0.0050 -0.0051 -0.0092
(0.27) (-0.43) (-0.44) (-0.94)
\mathrm{T}\mathrm{o}\mathrm{b}\mathrm{i}\mathrm{n}'\mathrm{s}Q0.0019 \ast 0.0031\ast \ast \ast 0.0030\ast \ast \ast 0.0043\ast \ast \ast
(1.91) (3.16) (3.09) (4.51)
\mathrm{S}\mathrm{U}\mathrm{E} -0.0012 -0.0004 -0.0004 0.0004
(-1.60) (-0.52) (-0.51) (0.56)
Panel B: Textual Controls
\mathrm{F}\mathrm{o}\mathrm{g} \mathrm{I}\mathrm{n}\mathrm{d}\mathrm{e}\mathrm{x} -0.0032 0.0010
(-0.97) (0.28)
\mathrm{l}\mathrm{n}(\mathrm{W}\mathrm{o}\mathrm{r}\mathrm{d} \mathrm{C}\mathrm{o}\mathrm{u}\mathrm{n}\mathrm{t}) -0.0303 \ast \ast \ast
(-3.34)
\mathrm{F}\mathrm{i}\mathrm{n}\mathrm{a}\mathrm{n}\mathrm{c}\mathrm{i}\mathrm{a}\mathrm{l} \mathrm{J}\mathrm{a}\mathrm{r}\mathrm{g}\mathrm{o}\mathrm{n} -0.3115
(-1.12)
\mathrm{N}\mathrm{u}\mathrm{m}\mathrm{b}\mathrm{e}\mathrm{r}\mathrm{s} 0.6018
(1.31)
\mathrm{F}\mathrm{o}\mathrm{r}\mathrm{w}\mathrm{a}\mathrm{r}\mathrm{d}-\mathrm{L}\mathrm{o}\mathrm{o}\mathrm{k}\mathrm{i}\mathrm{n}\mathrm{g} \mathrm{L}\mathrm{a}\mathrm{n}\mathrm{g}\mathrm{u}\mathrm{a}\mathrm{g}\mathrm{e} 0.7468 \ast \ast \ast
(3.14)
\mathrm{J}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{i}fi\mathrm{c}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{S}\mathrm{i}\mathrm{m}\mathrm{i}\mathrm{l}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} -0.7405 \ast \ast \ast
(-16.92)
\mathrm{F}\mathrm{E} -- \mathrm{I}\mathrm{n}\mathrm{d}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{y} \mathrm{I}\mathrm{n}\mathrm{d}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{y} \mathrm{I}\mathrm{n}\mathrm{d}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{y}
\mathrm{Q}\mathrm{u}\mathrm{a}\mathrm{r}\mathrm{t}\mathrm{e}\mathrm{r} \mathrm{F}\mathrm{E} \mathrm{N}\mathrm{o} \mathrm{Y}\mathrm{e}\mathrm{s} \mathrm{Y}\mathrm{e}\mathrm{s} \mathrm{Y}\mathrm{e}\mathrm{s}
\mathrm{C}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} \mathrm{F}\mathrm{E} \mathrm{Y}\mathrm{e}\mathrm{s} \mathrm{Y}\mathrm{e}\mathrm{s} \mathrm{Y}\mathrm{e}\mathrm{s} \mathrm{Y}\mathrm{e}\mathrm{s}
\mathrm{O}\mathrm{b}\mathrm{s}\mathrm{e}\mathrm{r}\mathrm{v}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s} 24,622 24,622 24,622 24,622
\mathrm{A}\mathrm{d}\mathrm{j}.R 2 0.176 0.180 0.180 0.205
Notes:\mathrm{E}\mathrm{a}\mathrm{c}\mathrm{h} \mathrm{c}\mathrm{o}\mathrm{l}\mathrm{u}\mathrm{m}\mathrm{n} \mathrm{i}\mathrm{s} \mathrm{a}\mathrm{n} \mathrm{O}\mathrm{L}\mathrm{S} \mathrm{r}\mathrm{e}\mathrm{g}\mathrm{r}\mathrm{e}\mathrm{s}\mathrm{s}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{a}\mathrm{t} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l}--\mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} \mathrm{l}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{l} (1,894 \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l}\mathrm{s} \mathrm{w}\mathrm{i}\mathrm{t}\mathrm{h} \mathrm{n}\mathrm{o}\mathrm{n}-\mathrm{m}\mathrm{i}\mathrm{s}\mathrm{s}\mathrm{i}\mathrm{n}\mathrm{g} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{t}\mathrm{r}\mathrm{o}\mathrm{l}\mathrm{s} \times
13 \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t}\mathrm{s}). \mathrm{T}\mathrm{h}\mathrm{e} \mathrm{d}\mathrm{e}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{d}\mathrm{e}\mathrm{n}\mathrm{t} \mathrm{v}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{a}\mathrm{b}\mathrm{l}\mathrm{e} \mathrm{i}\mathrm{s} \mathrm{L}\mathrm{L}\mathrm{M} \mathrm{d}\mathrm{i}\mathrm{s}\mathrm{p}\mathrm{e}\mathrm{r}\mathrm{s}\mathrm{i}\mathrm{o}\mathrm{n}: \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{t}\mathrm{a}\mathrm{n}\mathrm{d}\mathrm{a}\mathrm{r}\mathrm{d} \mathrm{d}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{a}\mathrm{c}\mathrm{r}\mathrm{o}\mathrm{s}\mathrm{s} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}\mathrm{s} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e}
\mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}-\mathrm{s}\mathrm{t}\mathrm{a}\mathrm{n}\mathrm{d}\mathrm{a}\mathrm{r}\mathrm{d}\mathrm{i}\mathrm{z}\mathrm{e}\mathrm{d} \mathrm{L}\mathrm{L}\mathrm{M} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{f}\mathrm{o}\mathrm{r} \mathrm{t}\mathrm{h}\mathrm{a}\mathrm{t} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l} \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} (\mathrm{o}\mathrm{v}\mathrm{e}\mathrm{r} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}\mathrm{s} \mathrm{w}\mathrm{i}\mathrm{t}\mathrm{h} \mathrm{a} \mathrm{v}\mathrm{a}\mathrm{l}\mathrm{i}\mathrm{d} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{f}\mathrm{o}\mathrm{r} \mathrm{t}\mathrm{h}\mathrm{a}\mathrm{t}
\mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l} \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t}). \mathrm{C}\mathrm{o}\mathrm{n}\mathrm{t}\mathrm{r}\mathrm{o}\mathrm{l}\mathrm{s}: \mathrm{l}\mathrm{n}(\mathrm{A}\mathrm{s}\mathrm{s}\mathrm{e}\mathrm{t}\mathrm{s}), \mathrm{b}\mathrm{o}\mathrm{o}\mathrm{k}-\mathrm{t}\mathrm{o}-\mathrm{m}\mathrm{a}\mathrm{r}\mathrm{k}\mathrm{e}\mathrm{t}, \mathrm{T}\mathrm{o}\mathrm{b}\mathrm{i}\mathrm{n}'\mathrm{s} \mathrm{Q}, \mathrm{S}\mathrm{U}\mathrm{E} (\mathrm{w}\mathrm{i}\mathrm{n}\mathrm{s}\mathrm{o}\mathrm{r}\mathrm{i}\mathrm{z}\mathrm{e}\mathrm{d} \mathrm{a}\mathrm{t} 1/99\%), \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{F}\mathrm{o}\mathrm{g}
\mathrm{i}\mathrm{n}\mathrm{d}\mathrm{e}\mathrm{x}, \mathrm{l}\mathrm{n}(\mathrm{W}\mathrm{o}\mathrm{r}\mathrm{d} \mathrm{C}\mathrm{o}\mathrm{u}\mathrm{n}\mathrm{t}), \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{t}\mathrm{h}\mathrm{e} fi\mathrm{n}\mathrm{a}\mathrm{n}\mathrm{c}\mathrm{i}\mathrm{a}\mathrm{l} \mathrm{j}\mathrm{a}\mathrm{r}\mathrm{g}\mathrm{o}\mathrm{n}, \mathrm{n}\mathrm{u}\mathrm{m}\mathrm{b}\mathrm{e}\mathrm{r}\mathrm{s} \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{f}\mathrm{o}\mathrm{r}\mathrm{w}\mathrm{a}\mathrm{r}\mathrm{d}-\mathrm{l}\mathrm{o}\mathrm{o}\mathrm{k}\mathrm{i}\mathrm{n}\mathrm{g} \mathrm{l}\mathrm{a}\mathrm{n}\mathrm{g}\mathrm{u}\mathrm{a}\mathrm{g}\mathrm{e} \mathrm{s}\mathrm{h}\mathrm{a}\mathrm{r}\mathrm{e}\mathrm{s} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{Q}\&\mathrm{A}
\mathrm{t}\mathrm{e}\mathrm{x}\mathrm{t}, \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{a}\mathrm{v}\mathrm{e}\mathrm{r}\mathrm{a}\mathrm{g}\mathrm{e} \mathrm{p}\mathrm{a}\mathrm{i}\mathrm{r}\mathrm{w}\mathrm{i}\mathrm{s}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{s}\mathrm{i}\mathrm{n}\mathrm{e} \mathrm{s}\mathrm{i}\mathrm{m}\mathrm{i}\mathrm{l}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{n} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}\mathrm{s}' \mathrm{j}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{i}fi\mathrm{c}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}. \mathrm{A}\mathrm{l}\mathrm{l} \mathrm{c}\mathrm{o}\mathrm{l}\mathrm{u}\mathrm{m}\mathrm{n}\mathrm{s} \mathrm{i}\mathrm{n}\mathrm{c}\mathrm{l}\mathrm{u}\mathrm{d}\mathrm{e}
\mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} fi\mathrm{x}\mathrm{e}\mathrm{d} \mathrm{e}ff\mathrm{e}\mathrm{c}\mathrm{t}\mathrm{s}; \mathrm{c}\mathrm{o}\mathrm{l}\mathrm{u}\mathrm{m}\mathrm{n}\mathrm{s} (2)--(4) \mathrm{a}\mathrm{d}\mathrm{d} \mathrm{i}\mathrm{n}\mathrm{d}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{y} (\mathrm{o}\mathrm{n}\mathrm{e}-\mathrm{d}\mathrm{i}\mathrm{g}\mathrm{i}\mathrm{t} \mathrm{S}\mathrm{I}\mathrm{C} \mathrm{d}\mathrm{i}\mathrm{v}\mathrm{i}\mathrm{s}\mathrm{i}\mathrm{o}\mathrm{n}, \mathrm{n}\mathrm{i}\mathrm{n}\mathrm{e} \mathrm{g}\mathrm{r}\mathrm{o}\mathrm{u}\mathrm{p}\mathrm{s}) \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{q}\mathrm{u}\mathrm{a}\mathrm{r}\mathrm{t}\mathrm{e}\mathrm{r} fi\mathrm{x}\mathrm{e}\mathrm{d}
\mathrm{e}ff\mathrm{e}\mathrm{c}\mathrm{t}\mathrm{s}.t-\mathrm{s}\mathrm{t}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{i}\mathrm{c}\mathrm{s} \mathrm{i}\mathrm{n} \mathrm{p}\mathrm{a}\mathrm{r}\mathrm{e}\mathrm{n}\mathrm{t}\mathrm{h}\mathrm{e}\mathrm{s}\mathrm{e}\mathrm{s}, \mathrm{S}\mathrm{E} \mathrm{c}\mathrm{l}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{e}\mathrm{r}\mathrm{e}\mathrm{d} \mathrm{b}\mathrm{y} fi\mathrm{r}\mathrm{m}. \ast p<0.10; \ast \ast p<0.05; \ast \ast \ast p<0.01.
49

Table 6:\mathrm{L}\mathrm{L}\mathrm{M} \mathrm{D}\mathrm{i}\mathrm{s}\mathrm{a}\mathrm{g}\mathrm{r}\mathrm{e}\mathrm{e}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{t} \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{P}\mathrm{o}\mathrm{s}\mathrm{t}-\mathrm{C}\mathrm{a}\mathrm{l}\mathrm{l} \mathrm{M}\mathrm{a}\mathrm{r}\mathrm{k}\mathrm{e}\mathrm{t} \& \mathrm{A}\mathrm{n}\mathrm{a}\mathrm{l}\mathrm{y}\mathrm{s}\mathrm{t} \mathrm{D}\mathrm{i}\mathrm{s}\mathrm{a}\mathrm{g}\mathrm{r}\mathrm{e}\mathrm{e}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{t}
\mathrm{A}\mathrm{n}\mathrm{a}\mathrm{l}\mathrm{y}\mathrm{s}\mathrm{t} \mathrm{D}\mathrm{i}\mathrm{s}\mathrm{p}. \mathrm{F}\mathrm{o}\mathrm{r}\mathrm{e}\mathrm{c}. \mathrm{E}\mathrm{r}\mathrm{r}\mathrm{o}\mathrm{r} \mathrm{B}\mathrm{i}\mathrm{d}--\mathrm{A}\mathrm{s}\mathrm{k} \mathrm{A}\mathrm{b}\mathrm{n}. \mathrm{V}\mathrm{o}\mathrm{l}\mathrm{u}\mathrm{m}\mathrm{e} \mathrm{A}\mathrm{b}\mathrm{n}. \mathrm{R}\mathrm{e}\mathrm{t}. \mathrm{V}\mathrm{a}\mathrm{r}.
(1) (2) (3) (4) (5)
\mathrm{L}\mathrm{L}\mathrm{M} \mathrm{D}\mathrm{i}\mathrm{s}\mathrm{p}\mathrm{e}\mathrm{r}\mathrm{s}\mathrm{i}\mathrm{o}\mathrm{n} (\mathrm{Z}-\mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}) -0.0019 -0.0041 -0.0000 0.0099 0.4880
(-1.23) (-0.63) (-1.03) (0.12) (0.69)
Controls
\mathrm{P}\mathrm{r}\mathrm{e}-\mathrm{C}\mathrm{a}\mathrm{l}\mathrm{l} \mathrm{A}\mathrm{n}\mathrm{a}\mathrm{l}\mathrm{y}\mathrm{s}\mathrm{t} \mathrm{C}\mathrm{o}\mathrm{u}\mathrm{n}\mathrm{t} 0.0003 0.0005 0.0000 \ast \ast 0.0621\ast \ast \ast 0.2044
(0.78) (0.35) (2.33) (3.36) (1.43)
\mathrm{P}\mathrm{r}\mathrm{e}-\mathrm{C}\mathrm{a}\mathrm{l}\mathrm{l} \mathrm{A}\mathrm{n}\mathrm{a}\mathrm{l}\mathrm{y}\mathrm{s}\mathrm{t} \mathrm{D}\mathrm{i}\mathrm{s}\mathrm{p}. 0.5763 \ast \ast \ast 0.7262\ast \ast \ast 0.0002\ast -0.4429 -15.8447 \ast \ast \ast
(9.63) (5.70) (1.90) (-0.51) (-3.18)
\mathrm{l}\mathrm{n}(\mathrm{A}\mathrm{s}\mathrm{s}\mathrm{e}\mathrm{t}\mathrm{s}) -0.0051 \ast \ast 0.0084 -0.0000 \ast \ast \ast -0.4003\ast \ast \ast -2.0895\ast \ast \ast
(-2.05) (0.98) (-4.48) (-4.35) (-3.04)
\mathrm{B}\mathrm{o}\mathrm{o}\mathrm{k}-\mathrm{t}\mathrm{o}-\mathrm{M}\mathrm{a}\mathrm{r}\mathrm{k}\mathrm{e}\mathrm{t} 0.0437 \ast \ast 0.1955\ast \ast \ast -0.0001\ast \ast 0.1491 -2.8404
(2.56) (2.70) (-2.55) (0.41) (-1.43)
\mathrm{T}\mathrm{o}\mathrm{b}\mathrm{i}\mathrm{n}'\mathrm{s}Q-0.0012 \ast -0.0060\ast \ast 0.0000 -0.0817 \ast -0.5260\ast \ast
(-1.65) (-1.99) (0.07) (-1.96) (-2.24)
\mathrm{S}\mathrm{U}\mathrm{E} -0.0005 0.0018 0.0000 -0.0492 -0.1616
(-0.67) (0.97) (0.68) (-1.47) (-0.49)
\mathrm{O}\mathrm{b}\mathrm{s}\mathrm{e}\mathrm{r}\mathrm{v}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s} 1,889 1,826 1,890 1,890 1,890
\mathrm{A}\mathrm{d}\mathrm{j}.R 2 0.467 0.197 0.055 0.069 0.045
\mathrm{I}\mathrm{n}\mathrm{d}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{y} \mathrm{F}\mathrm{E}, \mathrm{Q}\mathrm{u}\mathrm{a}\mathrm{r}\mathrm{t}\mathrm{e}\mathrm{r} \mathrm{F}\mathrm{E} \mathrm{Y}\mathrm{e}\mathrm{s} \mathrm{Y}\mathrm{e}\mathrm{s} \mathrm{Y}\mathrm{e}\mathrm{s} \mathrm{Y}\mathrm{e}\mathrm{s} \mathrm{Y}\mathrm{e}\mathrm{s}
Notes:\mathrm{E}\mathrm{a}\mathrm{c}\mathrm{h} \mathrm{c}\mathrm{o}\mathrm{l}\mathrm{u}\mathrm{m}\mathrm{n} \mathrm{i}\mathrm{s} \mathrm{a} \mathrm{s}\mathrm{e}\mathrm{p}\mathrm{a}\mathrm{r}\mathrm{a}\mathrm{t}\mathrm{e} \mathrm{O}\mathrm{L}\mathrm{S} \mathrm{o}\mathrm{f} \mathrm{a} \mathrm{p}\mathrm{o}\mathrm{s}\mathrm{t}-\mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l} \mathrm{d}\mathrm{i}\mathrm{s}\mathrm{a}\mathrm{g}\mathrm{r}\mathrm{e}\mathrm{e}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{t} \mathrm{o}\mathrm{u}\mathrm{t}\mathrm{c}\mathrm{o}\mathrm{m}\mathrm{e} \mathrm{a}\mathrm{t} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l} \mathrm{l}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{l} (\mathrm{o}\mathrm{n}\mathrm{e} \mathrm{o}\mathrm{b}\mathrm{s}\mathrm{e}\mathrm{r}\mathrm{v}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{p}\mathrm{e}\mathrm{r} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l})
\mathrm{o}\mathrm{n} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l}-\mathrm{l}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{l} \mathrm{L}\mathrm{L}\mathrm{M} \mathrm{d}\mathrm{i}\mathrm{s}\mathrm{p}\mathrm{e}\mathrm{r}\mathrm{s}\mathrm{i}\mathrm{o}\mathrm{n} (\mathrm{t}\mathrm{h}\mathrm{e} \mathrm{a}\mathrm{v}\mathrm{e}\mathrm{r}\mathrm{a}\mathrm{g}\mathrm{e} \mathrm{a}\mathrm{c}\mathrm{r}\mathrm{o}\mathrm{s}\mathrm{s} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{t}\mathrm{h}\mathrm{i}\mathrm{r}\mathrm{t}\mathrm{e}\mathrm{e}\mathrm{n} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t}\mathrm{s} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{t}\mathrm{a}\mathrm{n}\mathrm{d}\mathrm{a}\mathrm{r}\mathrm{d} \mathrm{d}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{n}
\mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}-\mathrm{s}\mathrm{t}\mathrm{a}\mathrm{n}\mathrm{d}\mathrm{a}\mathrm{r}\mathrm{d}\mathrm{i}\mathrm{z}\mathrm{e}\mathrm{d} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}\mathrm{s}, \mathrm{s}\mathrm{t}\mathrm{a}\mathrm{n}\mathrm{d}\mathrm{a}\mathrm{r}\mathrm{d}\mathrm{i}\mathrm{z}\mathrm{e}\mathrm{d}). \mathrm{O}\mathrm{u}\mathrm{t}\mathrm{c}\mathrm{o}\mathrm{m}\mathrm{e}\mathrm{s}: \mathrm{l}\mathrm{o}\mathrm{g} \mathrm{a}\mathrm{n}\mathrm{a}\mathrm{l}\mathrm{y}\mathrm{s}\mathrm{t} \mathrm{f}\mathrm{o}\mathrm{r}\mathrm{e}\mathrm{c}\mathrm{a}\mathrm{s}\mathrm{t} \mathrm{d}\mathrm{i}\mathrm{s}\mathrm{p}\mathrm{e}\mathrm{r}\mathrm{s}\mathrm{i}\mathrm{o}\mathrm{n}; \mathrm{f}\mathrm{o}\mathrm{r}\mathrm{e}\mathrm{c}\mathrm{a}\mathrm{s}\mathrm{t} \mathrm{e}\mathrm{r}\mathrm{r}\mathrm{o}\mathrm{r} ( | \mathrm{p}\mathrm{o}\mathrm{s}\mathrm{t}-\mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l}
\mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{e}\mathrm{n}\mathrm{s}\mathrm{u}\mathrm{s} - \mathrm{a}\mathrm{c}\mathrm{t}\mathrm{u}\mathrm{a}\mathrm{l}| /\mathrm{p}\mathrm{r}\mathrm{i}\mathrm{c}\mathrm{e}\times 100, \mathrm{f}\mathrm{r}\mathrm{o}\mathrm{m} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{I}/\mathrm{B}/\mathrm{E}/\mathrm{S} \mathrm{d}\mathrm{e}\mathrm{t}\mathrm{a}\mathrm{i}\mathrm{l} fi\mathrm{l}\mathrm{e}); \mathrm{a}\mathrm{b}\mathrm{n}\mathrm{o}\mathrm{r}\mathrm{m}\mathrm{a}\mathrm{l} \mathrm{q}\mathrm{u}\mathrm{o}\mathrm{t}\mathrm{e}\mathrm{d} \mathrm{b}\mathrm{i}\mathrm{d}--\mathrm{a}\mathrm{s}\mathrm{k} \mathrm{s}\mathrm{p}\mathrm{r}\mathrm{e}\mathrm{a}\mathrm{d}; \mathrm{a}\mathrm{b}\mathrm{n}\mathrm{o}\mathrm{r}\mathrm{m}\mathrm{a}\mathrm{l} \mathrm{v}\mathrm{o}\mathrm{l}\mathrm{u}\mathrm{m}\mathrm{e};
\mathrm{a}\mathrm{b}\mathrm{n}\mathrm{o}\mathrm{r}\mathrm{m}\mathrm{a}\mathrm{l} \mathrm{r}\mathrm{e}\mathrm{t}\mathrm{u}\mathrm{r}\mathrm{n} \mathrm{v}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{a}\mathrm{n}\mathrm{c}\mathrm{e} (\mathrm{e}\mathrm{a}\mathrm{c}\mathrm{h} \mathrm{s}\mathrm{u}\mathrm{m}\mathrm{m}\mathrm{e}\mathrm{d} \mathrm{o}\mathrm{v}\mathrm{e}\mathrm{r} \mathrm{t}\mathrm{h}\mathrm{e} (0, 1) \mathrm{w}\mathrm{i}\mathrm{n}\mathrm{d}\mathrm{o}\mathrm{w} \mathrm{i}\mathrm{n} \mathrm{e}\mathrm{x}\mathrm{c}\mathrm{e}\mathrm{s}\mathrm{s} \mathrm{o}\mathrm{f} \mathrm{i}\mathrm{t}\mathrm{s} \mathrm{e}\mathrm{s}\mathrm{t}\mathrm{i}\mathrm{m}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}-\mathrm{w}\mathrm{i}\mathrm{n}\mathrm{d}\mathrm{o}\mathrm{w} \mathrm{m}\mathrm{e}\mathrm{a}\mathrm{n}). \mathrm{C}\mathrm{o}\mathrm{n}\mathrm{t}\mathrm{r}\mathrm{o}\mathrm{l}\mathrm{s}:
\mathrm{p}\mathrm{r}\mathrm{e}-\mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l} \mathrm{a}\mathrm{n}\mathrm{a}\mathrm{l}\mathrm{y}\mathrm{s}\mathrm{t} \mathrm{c}\mathrm{o}\mathrm{u}\mathrm{n}\mathrm{t} \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{d}\mathrm{i}\mathrm{s}\mathrm{p}\mathrm{e}\mathrm{r}\mathrm{s}\mathrm{i}\mathrm{o}\mathrm{n}, \mathrm{l}\mathrm{n}(\mathrm{A}\mathrm{s}\mathrm{s}\mathrm{e}\mathrm{t}\mathrm{s}), \mathrm{b}\mathrm{o}\mathrm{o}\mathrm{k}-\mathrm{t}\mathrm{o}-\mathrm{m}\mathrm{a}\mathrm{r}\mathrm{k}\mathrm{e}\mathrm{t}, \mathrm{T}\mathrm{o}\mathrm{b}\mathrm{i}\mathrm{n}'\mathrm{s} \mathrm{Q}, \mathrm{S}\mathrm{U}\mathrm{E}. \mathrm{T}\mathrm{h}\mathrm{e} \mathrm{d}\mathrm{e}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{d}\mathrm{e}\mathrm{n}\mathrm{t} \mathrm{v}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{a}\mathrm{b}\mathrm{l}\mathrm{e}\mathrm{s}, \mathrm{S}\mathrm{U}\mathrm{E}
\mathrm{a}\mathrm{n}\mathrm{d} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{a}\mathrm{n}\mathrm{a}\mathrm{l}\mathrm{y}\mathrm{s}\mathrm{t} \mathrm{v}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{a}\mathrm{b}\mathrm{l}\mathrm{e}\mathrm{s} \mathrm{a}\mathrm{r}\mathrm{e} \mathrm{w}\mathrm{i}\mathrm{n}\mathrm{s}\mathrm{o}\mathrm{r}\mathrm{i}\mathrm{z}\mathrm{e}\mathrm{d} \mathrm{a}\mathrm{t} 1/99\%. t-\mathrm{s}\mathrm{t}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{i}\mathrm{c}\mathrm{s} \mathrm{i}\mathrm{n} \mathrm{p}\mathrm{a}\mathrm{r}\mathrm{e}\mathrm{n}\mathrm{t}\mathrm{h}\mathrm{e}\mathrm{s}\mathrm{e}\mathrm{s}, \mathrm{S}\mathrm{E} \mathrm{c}\mathrm{l}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{e}\mathrm{r}\mathrm{e}\mathrm{d} \mathrm{b}\mathrm{y} fi\mathrm{r}\mathrm{m}. \ast p <0.10;
\ast \ast p<0.05; \ast \ast \ast p<0.01.
50

Table 7:\mathrm{R}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{B}\mathrm{e}\mathrm{t}\mathrm{w}\mathrm{e}\mathrm{e}\mathrm{n} \mathrm{L}\mathrm{L}\mathrm{M} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}\mathrm{s} \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{M}\mathrm{a}\mathrm{r}\mathrm{k}\mathrm{e}\mathrm{t} \mathrm{R}\mathrm{e}\mathrm{a}\mathrm{c}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}
Climate Risk
Corporate Culture
Innovation
Integrity
Management Clarity
Political Risk
Quality
Respect
Sentiment
Specificity
Specificity Ratio
Teamwork
Uncertainty
\mathrm{M}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{l} 0.2 0.4 \ast \ast \ast 0.2 0.3 \ast \ast 0.2 -0.1 0.3 \ast \ast 0.4\ast \ast 1.3\ast \ast \ast 0.1 0.4 \ast \ast \ast 0.3\ast \ast -0.5\ast \ast \ast
(1.27) (2.66) (1.25) (2.05) (1.01) (-0.84) (2.17) (2.46) (7.60) (0.95) (2.92) (2.13) (-2.92)
\mathrm{G}\mathrm{e}\mathrm{m}\mathrm{i}\mathrm{n}\mathrm{i} 0.0 0.5 \ast \ast \ast 0.3\ast 0.3\ast 0.2 -0.0 0.3 \ast 0.6\ast \ast \ast 1.4\ast \ast \ast 0.1 0.2 0.6 \ast \ast \ast -0.4\ast \ast \ast
(0.22) (2.68) (1.83) (1.76) (0.99) (-0.29) (1.73) (3.79) (8.61) (0.72) (1.33) (3.62) (-2.85)
\mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{A}\mathrm{I} -0.1 0.5 \ast \ast \ast 0.3\ast 0.4\ast \ast 0.1 0.2 0.4 \ast \ast 0.4\ast \ast \ast 1.1\ast \ast \ast 0.1 0.4 \ast \ast \ast 0.4\ast \ast \ast -0.5\ast \ast \ast
(-0.46) (3.11) (1.80) (2.55) (0.82) (0.96) (2.46) (2.67) (7.07) (0.87) (3.12) (2.71) (-3.80)
\mathrm{Q}\mathrm{w}\mathrm{e}\mathrm{n} -0.4 \ast \ast \ast 0.2 0.1 0.1 -0.1 --- 0.1 0.2 0.9 \ast \ast \ast -0.1 -0.1 0.2 -0.6 \ast \ast \ast
(-2.77) (1.21) (0.67) (0.92) (-0.92) (0.50) (1.08) (5.60) (-0.95) (-0.59) (1.63) (-3.84)
\mathrm{L}\mathrm{l}\mathrm{a}\mathrm{m}\mathrm{a} -0.0 0.4 \ast \ast \ast 0.1 0.3 \ast \ast 0.3\ast \ast -0.0 0.3 \ast 0.3\ast \ast 1.3\ast \ast \ast -0.0 0.1 0.4 \ast \ast \ast -0.5\ast \ast \ast
(-0.26) (2.75) (0.81) (2.01) (2.52) (-0.30) (1.72) (2.22) (7.54) (-0.18) (0.36) (2.81) (-2.99)
\mathrm{D}\mathrm{e}\mathrm{e}\mathrm{p}\mathrm{S}\mathrm{e}\mathrm{e}\mathrm{k} 0.1 0.4 \ast \ast \ast 0.4\ast \ast 0.4\ast \ast -0.1 0.0 0.4 \ast \ast \ast 0.4\ast \ast 1.2\ast \ast \ast 0.0 0.1 0.4 \ast \ast -0.4\ast \ast \ast
(0.87) (2.68) (2.02) (2.31) (-0.49) (0.11) (2.70) (2.48) (7.17) (0.25) (0.93) (2.45) (-3.00)
\mathrm{A}\mathrm{n}\mathrm{t}\mathrm{h}\mathrm{r}\mathrm{o}\mathrm{p}\mathrm{i}\mathrm{c} 0.0 0.4 \ast \ast 0.1 0.3 \ast \ast 0.2 --- 0.3 \ast \ast 0.3\ast \ast 1.2\ast \ast \ast 0.1 0.0 0.4 \ast \ast -1.1\ast \ast \ast
(0.16) (2.45) (0.85) (2.40) (1.26) (2.13) (1.98) (7.13) (0.88) (0.03) (2.46) (-6.97)
\mathrm{N}\mathrm{o}\mathrm{n}-\mathrm{L}\mathrm{L}\mathrm{M} 0.2 0.4 \ast \ast 0.2 0.2 0.1 0.2 \ast 0.1 0.2 0.3 0.2 \ast 0.2\ast 0.4\ast \ast \ast 0.1
(1.33) (2.33) (1.03) (1.63) (0.47) (1.72) (0.78) (1.33) (1.63) (1.91) (1.91) (3.17) (0.33)
Notes:\mathrm{E}\mathrm{a}\mathrm{c}\mathrm{h} \mathrm{c}\mathrm{e}\mathrm{l}\mathrm{l} \mathrm{i}\mathrm{s} \mathrm{a} \mathrm{s}\mathrm{e}\mathrm{p}\mathrm{a}\mathrm{r}\mathrm{a}\mathrm{t}\mathrm{e} \mathrm{O}\mathrm{L}\mathrm{S} \mathrm{r}\mathrm{e}\mathrm{g}\mathrm{r}\mathrm{e}\mathrm{s}\mathrm{s}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{o}\mathrm{f} \mathrm{C}\mathrm{a}\mathrm{r}\mathrm{h}\mathrm{a}\mathrm{r}\mathrm{t} 4-\mathrm{F}\mathrm{a}\mathrm{c}\mathrm{t}\mathrm{o}\mathrm{r} \mathrm{C}\mathrm{A}\mathrm{R}(0,1) \mathrm{o}\mathrm{n} \mathrm{o}\mathrm{n}\mathrm{e} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}'\mathrm{s} \mathrm{z}-\mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}\mathrm{d} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}
\mathrm{f}\mathrm{o}\mathrm{r} \mathrm{o}\mathrm{n}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t}, \mathrm{w}\mathrm{i}\mathrm{t}\mathrm{h} fi\mathrm{r}\mathrm{m} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{t}\mathrm{r}\mathrm{o}\mathrm{l}\mathrm{s} (\mathrm{l}\mathrm{n}(\mathrm{A}\mathrm{s}\mathrm{s}\mathrm{e}\mathrm{t}\mathrm{s}), \mathrm{b}\mathrm{o}\mathrm{o}\mathrm{k}-\mathrm{t}\mathrm{o}-\mathrm{m}\mathrm{a}\mathrm{r}\mathrm{k}\mathrm{e}\mathrm{t}, \mathrm{T}\mathrm{o}\mathrm{b}\mathrm{i}\mathrm{n}'\mathrm{s} \mathrm{Q}, \mathrm{S}\mathrm{U}\mathrm{E}) \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{i}\mathrm{n}\mathrm{d}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{y} (\mathrm{o}\mathrm{n}\mathrm{e}-\mathrm{d}\mathrm{i}\mathrm{g}\mathrm{i}\mathrm{t}
\mathrm{S}\mathrm{I}\mathrm{C} \mathrm{d}\mathrm{i}\mathrm{v}\mathrm{i}\mathrm{s}\mathrm{i}\mathrm{o}\mathrm{n}, \mathrm{n}\mathrm{i}\mathrm{n}\mathrm{e} \mathrm{g}\mathrm{r}\mathrm{o}\mathrm{u}\mathrm{p}\mathrm{s}) \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{q}\mathrm{u}\mathrm{a}\mathrm{r}\mathrm{t}\mathrm{e}\mathrm{r} fi\mathrm{x}\mathrm{e}\mathrm{d} \mathrm{e}ff\mathrm{e}\mathrm{c}\mathrm{t}\mathrm{s}, \mathrm{o}\mathrm{n} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l}\mathrm{s} \mathrm{w}\mathrm{i}\mathrm{t}\mathrm{h} \mathrm{a} \mathrm{v}\mathrm{a}\mathrm{l}\mathrm{i}\mathrm{d} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{f}\mathrm{r}\mathrm{o}\mathrm{m} \mathrm{t}\mathrm{h}\mathrm{a}\mathrm{t} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r} \mathrm{a}\mathrm{n}\mathrm{d}
\mathrm{n}\mathrm{o}\mathrm{n}-\mathrm{m}\mathrm{i}\mathrm{s}\mathrm{s}\mathrm{i}\mathrm{n}\mathrm{g} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{t}\mathrm{r}\mathrm{o}\mathrm{l}\mathrm{s}. \mathrm{T}\mathrm{h}\mathrm{e} \mathrm{N}\mathrm{o}\mathrm{n}-\mathrm{L}\mathrm{L}\mathrm{M} \mathrm{m}\mathrm{e}\mathrm{a}\mathrm{s}\mathrm{u}\mathrm{r}\mathrm{e}\mathrm{s} \mathrm{a}\mathrm{r}\mathrm{e} \mathrm{a}\mathrm{l}\mathrm{s}\mathrm{o} \mathrm{s}\mathrm{t}\mathrm{a}\mathrm{n}\mathrm{d}\mathrm{a}\mathrm{r}\mathrm{d}\mathrm{i}\mathrm{z}\mathrm{e}\mathrm{d} \mathrm{s}\mathrm{o} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{e}ffi\mathrm{c}\mathrm{i}\mathrm{e}\mathrm{n}\mathrm{t}\mathrm{s} \mathrm{a}\mathrm{r}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{m}\mathrm{p}\mathrm{a}\mathrm{r}\mathrm{a}\mathrm{b}\mathrm{l}\mathrm{e} \mathrm{w}\mathrm{i}\mathrm{t}\mathrm{h}\mathrm{i}\mathrm{n}
\mathrm{e}\mathrm{a}\mathrm{c}\mathrm{h} \mathrm{c}\mathrm{o}\mathrm{l}\mathrm{u}\mathrm{m}\mathrm{n}. \mathrm{T}\mathrm{h}\mathrm{e} \mathrm{t}\mathrm{w}\mathrm{o} \mathrm{b}\mathrm{l}\mathrm{a}\mathrm{n}\mathrm{k} \mathrm{c}\mathrm{e}\mathrm{l}\mathrm{l}\mathrm{s} (\mathrm{m}\mathrm{a}\mathrm{r}\mathrm{k}\mathrm{e}\mathrm{d} ---) \mathrm{a}\mathrm{r}\mathrm{e} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}--\mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} \mathrm{s}\mathrm{e}\mathrm{r}\mathrm{i}\mathrm{e}\mathrm{s} \mathrm{e}\mathrm{x}\mathrm{c}\mathrm{l}\mathrm{u}\mathrm{d}\mathrm{e}\mathrm{d} \mathrm{f}\mathrm{r}\mathrm{o}\mathrm{m} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{a}\mathrm{m}\mathrm{p}\mathrm{l}\mathrm{e} \mathrm{d}\mathrm{u}\mathrm{e} \mathrm{t}\mathrm{o}
\mathrm{l}\mathrm{a}\mathrm{c}\mathrm{k} \mathrm{o}\mathrm{f} \mathrm{v}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} (\mathrm{s}\mathrm{e}\mathrm{e} \mathrm{S}\mathrm{e}\mathrm{c}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} 3.2). \mathrm{C}\mathrm{A}\mathrm{R} \mathrm{i}\mathrm{s} \mathrm{i}\mathrm{n} \mathrm{p}\mathrm{e}\mathrm{r}\mathrm{c}\mathrm{e}\mathrm{n}\mathrm{t}\mathrm{a}\mathrm{g}\mathrm{e} \mathrm{p}\mathrm{o}\mathrm{i}\mathrm{n}\mathrm{t}\mathrm{s}, \mathrm{s}\mathrm{o} \mathrm{e}\mathrm{a}\mathrm{c}\mathrm{h} \mathrm{c}\mathrm{o}\mathrm{e}ffi\mathrm{c}\mathrm{i}\mathrm{e}\mathrm{n}\mathrm{t} \mathrm{i}\mathrm{s} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{c}\mathrm{h}\mathrm{a}\mathrm{n}\mathrm{g}\mathrm{e} \mathrm{i}\mathrm{n} \mathrm{C}\mathrm{A}\mathrm{R}
\mathrm{a}\mathrm{s}\mathrm{s}\mathrm{o}\mathrm{c}\mathrm{i}\mathrm{a}\mathrm{t}\mathrm{e}\mathrm{d} \mathrm{w}\mathrm{i}\mathrm{t}\mathrm{h} \mathrm{a} \mathrm{o}\mathrm{n}\mathrm{e}-\mathrm{s}\mathrm{t}\mathrm{a}\mathrm{n}\mathrm{d}\mathrm{a}\mathrm{r}\mathrm{d}-\mathrm{d}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{i}\mathrm{n}\mathrm{c}\mathrm{r}\mathrm{e}\mathrm{a}\mathrm{s}\mathrm{e} \mathrm{i}\mathrm{n} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}'\mathrm{s} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}. t-\mathrm{s}\mathrm{t}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{i}\mathrm{c}\mathrm{s} \mathrm{i}\mathrm{n} \mathrm{p}\mathrm{a}\mathrm{r}\mathrm{e}\mathrm{n}\mathrm{t}\mathrm{h}\mathrm{e}\mathrm{s}\mathrm{e}\mathrm{s}, \mathrm{S}\mathrm{E}
\mathrm{c}\mathrm{l}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{e}\mathrm{r}\mathrm{e}\mathrm{d} \mathrm{b}\mathrm{y} fi\mathrm{r}\mathrm{m}. \ast p<0.10; \ast \ast p<0.05; \ast \ast \ast p<0.01.
51

Table 8:\mathrm{K}\mathrm{n}\mathrm{o}\mathrm{w}\mathrm{l}\mathrm{e}\mathrm{d}\mathrm{g}\mathrm{e}-\mathrm{C}\mathrm{u}\mathrm{t}\mathrm{o}ff \mathrm{R}\mathrm{o}\mathrm{b}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{n}\mathrm{e}\mathrm{s}\mathrm{s}: \mathrm{M}\mathrm{o}\mathrm{d}\mathrm{e}\mathrm{l} \mathrm{C}\mathrm{u}\mathrm{t}\mathrm{o}ff\mathrm{s} \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{C}\mathrm{a}\mathrm{l}\mathrm{l}\mathrm{s} \mathrm{B}\mathrm{e}\mathrm{f}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{A}\mathrm{f}\mathrm{t}\mathrm{e}\mathrm{r} \mathrm{E}\mathrm{a}\mathrm{c}\mathrm{h} \mathrm{C}\mathrm{u}\mathrm{t}\mathrm{o}ff
\mathrm{P}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r} \mathrm{K}\mathrm{n}\mathrm{o}\mathrm{w}\mathrm{l}\mathrm{e}\mathrm{d}\mathrm{g}\mathrm{e} \mathrm{c}\mathrm{u}\mathrm{t}\mathrm{o}ff \mathrm{C}\mathrm{a}\mathrm{l}\mathrm{l}\mathrm{s} \mathrm{p}\mathrm{r}\mathrm{e} \mathrm{C}\mathrm{a}\mathrm{l}\mathrm{l}\mathrm{s} \mathrm{p}\mathrm{o}\mathrm{s}\mathrm{t} \mathrm{S}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{d}\mathrm{d}\mathrm{l}\mathrm{e}\mathrm{s}?
\mathrm{A}\mathrm{n}\mathrm{t}\mathrm{h}\mathrm{r}\mathrm{o}\mathrm{p}\mathrm{i}\mathrm{c} 2023-08 0 1,946 \mathrm{N}\mathrm{o}
\mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{A}\mathrm{I} 2023-10 0 1,946 \mathrm{N}\mathrm{o}
\mathrm{M}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{l} 2023-10 0 1,946 \mathrm{N}\mathrm{o}
\mathrm{M}\mathrm{e}\mathrm{t}\mathrm{a} (\mathrm{L}\mathrm{l}\mathrm{a}\mathrm{m}\mathrm{a}) 2023-12 0 1,946 \mathrm{N}\mathrm{o}
Qwen 2024-06 970 976 Yes
DeepSeek 2024-07 1,242 704 Yes
\mathrm{G}\mathrm{o}\mathrm{o}\mathrm{g}\mathrm{l}\mathrm{e} (\mathrm{G}\mathrm{e}\mathrm{m}\mathrm{i}\mathrm{n}\mathrm{i}) 2025-01 1,946 0 \mathrm{N}\mathrm{o}
Notes:\mathrm{S}\mathrm{a}\mathrm{m}\mathrm{p}\mathrm{l}\mathrm{e} = 1,946 \mathrm{S}\&\mathrm{P} 500 \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l}\mathrm{s} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}\mathrm{d} \mathrm{i}\mathrm{n} 2024 (2024-01-04 \mathrm{t}\mathrm{o} 2024-12-20); \mathrm{c}\mathrm{u}\mathrm{t}\mathrm{o}ff\mathrm{s} \mathrm{f}\mathrm{r}\mathrm{o}\mathrm{m} \mathrm{o}ffi\mathrm{c}\mathrm{i}\mathrm{a}\mathrm{l}
\mathrm{d}\mathrm{o}\mathrm{c}\mathrm{u}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{t}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{w}\mathrm{h}\mathrm{e}\mathrm{r}\mathrm{e} \mathrm{a}\mathrm{v}\mathrm{a}\mathrm{i}\mathrm{l}\mathrm{a}\mathrm{b}\mathrm{l}\mathrm{e}, \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{o}\mathrm{t}\mathrm{h}\mathrm{e}\mathrm{r}\mathrm{w}\mathrm{i}\mathrm{s}\mathrm{e} \mathrm{f}\mathrm{r}\mathrm{o}\mathrm{m} \mathrm{d}\mathrm{a}\mathrm{t}\mathrm{e}\mathrm{d} \mathrm{d}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{l}\mathrm{o}\mathrm{p}\mathrm{e}\mathrm{r} \mathrm{s}\mathrm{t}\mathrm{a}\mathrm{t}\mathrm{e}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{t}\mathrm{s} \mathrm{o}\mathrm{r} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{m}\mathrm{o}\mathrm{d}\mathrm{e}\mathrm{l} \mathrm{c}\mathrm{a}\mathrm{t}\mathrm{a}\mathrm{l}\mathrm{o}\mathrm{g}\mathrm{u}\mathrm{e} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e}
\mathrm{A}\mathrm{P}\mathrm{I} \mathrm{g}\mathrm{a}\mathrm{t}\mathrm{e}\mathrm{w}\mathrm{a}\mathrm{y} \mathrm{t}\mathrm{h}\mathrm{r}\mathrm{o}\mathrm{u}\mathrm{g}\mathrm{h} \mathrm{w}\mathrm{h}\mathrm{i}\mathrm{c}\mathrm{h} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{m}\mathrm{o}\mathrm{d}\mathrm{e}\mathrm{l} \mathrm{w}\mathrm{a}\mathrm{s} \mathrm{q}\mathrm{u}\mathrm{e}\mathrm{r}\mathrm{i}\mathrm{e}\mathrm{d}. \mathrm{A} \mathrm{c}\mathrm{u}\mathrm{t}\mathrm{o}ff \mathrm{m}\mathrm{o}\mathrm{n}\mathrm{t}\mathrm{h} \mathrm{i}\mathrm{s} \mathrm{r}\mathrm{e}\mathrm{a}\mathrm{d} \mathrm{a}\mathrm{s} \mathrm{k}\mathrm{n}\mathrm{o}\mathrm{w}\mathrm{l}\mathrm{e}\mathrm{d}\mathrm{g}\mathrm{e} \mathrm{t}\mathrm{h}\mathrm{r}\mathrm{o}\mathrm{u}\mathrm{g}\mathrm{h} \mathrm{i}\mathrm{t}\mathrm{s} \mathrm{l}\mathrm{a}\mathrm{s}\mathrm{t} \mathrm{d}\mathrm{a}\mathrm{y},
\mathrm{s}\mathrm{o} \mathrm{a} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l} \mathrm{i}\mathrm{s} \mathrm{p}\mathrm{o}\mathrm{s}\mathrm{t}-\mathrm{c}\mathrm{u}\mathrm{t}\mathrm{o}ff \mathrm{f}\mathrm{r}\mathrm{o}\mathrm{m} \mathrm{t}\mathrm{h}\mathrm{e} fi\mathrm{r}\mathrm{s}\mathrm{t} \mathrm{d}\mathrm{a}\mathrm{y} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{f}\mathrm{o}\mathrm{l}\mathrm{l}\mathrm{o}\mathrm{w}\mathrm{i}\mathrm{n}\mathrm{g} \mathrm{m}\mathrm{o}\mathrm{n}\mathrm{t}\mathrm{h}. \mathrm{A} \mathrm{m}\mathrm{o}\mathrm{d}\mathrm{e}\mathrm{l} ``\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{d}\mathrm{d}\mathrm{l}\mathrm{e}\mathrm{s}"" \mathrm{i}\mathrm{f} \mathrm{i}\mathrm{t} \mathrm{h}\mathrm{a}\mathrm{s} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l}\mathrm{s} \mathrm{b}\mathrm{o}\mathrm{t}\mathrm{h} \mathrm{b}\mathrm{e}\mathrm{f}\mathrm{o}\mathrm{r}\mathrm{e}
\mathrm{a}\mathrm{n}\mathrm{d} \mathrm{a}\mathrm{f}\mathrm{t}\mathrm{e}\mathrm{r} \mathrm{i}\mathrm{t}\mathrm{s} \mathrm{c}\mathrm{u}\mathrm{t}\mathrm{o}ff \mathrm{i}\mathrm{n}\mathrm{s}\mathrm{i}\mathrm{d}\mathrm{e} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{a}\mathrm{m}\mathrm{p}\mathrm{l}\mathrm{e}; \mathrm{Q}\mathrm{w}\mathrm{e}\mathrm{n} (2024-06) \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{D}\mathrm{e}\mathrm{e}\mathrm{p}\mathrm{S}\mathrm{e}\mathrm{e}\mathrm{k} (2024-07) \mathrm{d}\mathrm{o}, \mathrm{s}\mathrm{o} \mathrm{t}\mathrm{h}\mathrm{e} ``\mathrm{p}\mathrm{o}\mathrm{s}\mathrm{t}"" \mathrm{w}\mathrm{i}\mathrm{n}\mathrm{d}\mathrm{o}\mathrm{w}\mathrm{s}
\mathrm{f}\mathrm{a}\mathrm{l}\mathrm{l} \mathrm{i}\mathrm{n} 2024 (\mathrm{Q}\mathrm{w}\mathrm{e}\mathrm{n}, \mathrm{J}\mathrm{u}\mathrm{l}\mathrm{y}--\mathrm{D}\mathrm{e}\mathrm{c}\mathrm{e}\mathrm{m}\mathrm{b}\mathrm{e}\mathrm{r} 2024; \mathrm{D}\mathrm{e}\mathrm{e}\mathrm{p}\mathrm{S}\mathrm{e}\mathrm{e}\mathrm{k}, \mathrm{A}\mathrm{u}\mathrm{g}\mathrm{u}\mathrm{s}\mathrm{t}--\mathrm{D}\mathrm{e}\mathrm{c}\mathrm{e}\mathrm{m}\mathrm{b}\mathrm{e}\mathrm{r} 2024). \mathrm{T}\mathrm{h}\mathrm{e} \mathrm{d}\mathrm{i}ff\mathrm{e}\mathrm{r}\mathrm{e}\mathrm{n}\mathrm{c}\mathrm{e}-\mathrm{i}\mathrm{n}-\mathrm{d}\mathrm{i}ff\mathrm{e}\mathrm{r}\mathrm{e}\mathrm{n}\mathrm{c}\mathrm{e}\mathrm{s}
\mathrm{e}\mathrm{s}\mathrm{t}\mathrm{i}\mathrm{m}\mathrm{a}\mathrm{t}\mathrm{e}\mathrm{s} \mathrm{b}\mathrm{y} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} \mathrm{a}\mathrm{r}\mathrm{e} \mathrm{i}\mathrm{n} \mathrm{T}\mathrm{a}\mathrm{b}\mathrm{l}\mathrm{e} 9.
52

Table 9:\mathrm{K}\mathrm{n}\mathrm{o}\mathrm{w}\mathrm{l}\mathrm{e}\mathrm{d}\mathrm{g}\mathrm{e}-\mathrm{C}\mathrm{u}\mathrm{t}\mathrm{o}ff \mathrm{R}\mathrm{o}\mathrm{b}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{n}\mathrm{e}\mathrm{s}\mathrm{s}: \mathrm{P}\mathrm{e}\mathrm{r}-\mathrm{C}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} \mathrm{D}\mathrm{i}ff\mathrm{e}\mathrm{r}\mathrm{e}\mathrm{n}\mathrm{c}\mathrm{e}-\mathrm{i}\mathrm{n}-\mathrm{D}\mathrm{i}ff\mathrm{e}\mathrm{r}\mathrm{e}\mathrm{n}\mathrm{c}\mathrm{e}\mathrm{s} \mathrm{o}\mathrm{n} \mathrm{D}\mathrm{i}\mathrm{s}\mathrm{a}\mathrm{g}\mathrm{r}\mathrm{e}\mathrm{e}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{t}
\mathrm{C}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} \mathrm{D}\mathrm{e}\mathrm{e}\mathrm{p}\mathrm{S}\mathrm{e}\mathrm{e}\mathrm{k}\times \mathrm{p}\mathrm{o}\mathrm{s}\mathrm{t} \mathrm{Q}\mathrm{w}\mathrm{e}\mathrm{n}\times \mathrm{p}\mathrm{o}\mathrm{s}\mathrm{t}
\mathrm{C}\mathrm{o}\mathrm{r}\mathrm{p}. \mathrm{c}\mathrm{u}\mathrm{l}\mathrm{t}\mathrm{u}\mathrm{r}\mathrm{e} 0.0748 \ast \ast \ast -0.0402
(3.35) (-1.54)
\mathrm{Q}\mathrm{u}\mathrm{a}\mathrm{l}\mathrm{i}\mathrm{t}\mathrm{y} 0.0668 \ast \ast \ast -0.0220
(2.88) (-0.82)
\mathrm{M}\mathrm{g}\mathrm{m}\mathrm{t} \mathrm{c}\mathrm{l}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} 0.0573 \ast \ast \ast 0.0847\ast \ast \ast
(2.65) (3.36)
\mathrm{T}\mathrm{e}\mathrm{a}\mathrm{m}\mathrm{w}\mathrm{o}\mathrm{r}\mathrm{k} 0.0536 \ast \ast -0.0411\ast
(2.33) (-1.65)
\mathrm{R}\mathrm{e}\mathrm{s}\mathrm{p}\mathrm{e}\mathrm{c}\mathrm{t} 0.0408 \ast -0.0402
(1.72) (-1.60)
\mathrm{I}\mathrm{n}\mathrm{n}\mathrm{o}\mathrm{v}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} 0.0335 \ast \ast -0.0059
(2.33) (-0.29)
\mathrm{S}\mathrm{p}\mathrm{e}\mathrm{c}\mathrm{i}fi\mathrm{c}\mathrm{i}\mathrm{t}\mathrm{y} 0.0196 -0.0098
(1.00) (-0.38)
\mathrm{I}\mathrm{n}\mathrm{t}\mathrm{e}\mathrm{g}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} 0.0184 -0.0979 \ast \ast \ast
(0.75) (-3.56)
\mathrm{C}\mathrm{l}\mathrm{i}\mathrm{m}\mathrm{a}\mathrm{t}\mathrm{e} \mathrm{r}\mathrm{i}\mathrm{s}\mathrm{k} -0.0013 -0.0633 \ast \ast \ast
(-0.09) (-2.74)
Sentiment -0.0030 -0.0138
(-0.25) (-0.97)
\mathrm{U}\mathrm{n}\mathrm{c}\mathrm{e}\mathrm{r}\mathrm{t}\mathrm{a}\mathrm{i}\mathrm{n}\mathrm{t}\mathrm{y} -0.0202 -0.0253
(-1.06) (-1.28)
\mathrm{S}\mathrm{p}\mathrm{e}\mathrm{c}\mathrm{i}fi\mathrm{c}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{r}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o} -0.0205 0.0026
(-0.70) (0.09)
\mathrm{P}\mathrm{o}\mathrm{l}\mathrm{i}\mathrm{t}\mathrm{i}\mathrm{c}\mathrm{a}\mathrm{l} \mathrm{r}\mathrm{i}\mathrm{s}\mathrm{k} -0.0266 ---
(-1.24)
Notes:\mathrm{E}\mathrm{a}\mathrm{c}\mathrm{h} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} \mathrm{i}\mathrm{s} \mathrm{a} \mathrm{s}\mathrm{e}\mathrm{p}\mathrm{a}\mathrm{r}\mathrm{a}\mathrm{t}\mathrm{e} \mathrm{O}\mathrm{L}\mathrm{S} | \mathrm{d}\mathrm{e}\mathrm{v}| ij = \sum s\beta s (\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{d}\mathrm{d}\mathrm{l}\mathrm{e}\mathrm{r}s,i\times \mathrm{p}\mathrm{o}\mathrm{s}\mathrm{t} s,t)+ \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r} \mathrm{F}\mathrm{E}+\mathrm{m}\mathrm{o}\mathrm{n}\mathrm{t}\mathrm{h} \mathrm{F}\mathrm{E}+\varepsilon ,
\mathrm{w}\mathrm{h}\mathrm{e}\mathrm{r}\mathrm{e}| \mathrm{d}\mathrm{e}\mathrm{v}| \mathrm{i}\mathrm{s} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{a}\mathrm{b}\mathrm{s}\mathrm{o}\mathrm{l}\mathrm{u}\mathrm{t}\mathrm{e} \mathrm{d}\mathrm{e}\mathrm{v}\mathrm{i}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{f}\mathrm{r}\mathrm{o}\mathrm{m} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{l}\mathrm{e}\mathrm{a}\mathrm{v}\mathrm{e}-\mathrm{o}\mathrm{n}\mathrm{e}-\mathrm{o}\mathrm{u}\mathrm{t} 7-\mathrm{m}\mathrm{o}\mathrm{d}\mathrm{e}\mathrm{l} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{e}\mathrm{n}\mathrm{s}\mathrm{u}\mathrm{s} \mathrm{o}\mathrm{n} z-\mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}\mathrm{s} \mathrm{t}\mathrm{a}\mathrm{k}\mathrm{e}\mathrm{n} \mathrm{w}\mathrm{i}\mathrm{t}\mathrm{h}\mathrm{i}\mathrm{n}
\mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}\times \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} (\mathrm{s}\mathrm{o} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{i}\mathrm{b}\mathrm{r}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{i}\mathrm{s} \mathrm{n}\mathrm{e}\mathrm{t}\mathrm{t}\mathrm{e}\mathrm{d} \mathrm{o}\mathrm{u}\mathrm{t}) \mathrm{a}\mathrm{n}\mathrm{d} ``\mathrm{p}\mathrm{o}\mathrm{s}\mathrm{t}"" = \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l} \mathrm{a}\mathrm{f}\mathrm{t}\mathrm{e}\mathrm{r} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{d}\mathrm{d}\mathrm{l}\mathrm{e}\mathrm{r}'\mathrm{s} \mathrm{o}\mathrm{w}\mathrm{n} \mathrm{c}\mathrm{u}\mathrm{t}\mathrm{o}ff
\mathrm{m}\mathrm{o}\mathrm{n}\mathrm{t}\mathrm{h} (\mathrm{D}\mathrm{e}\mathrm{e}\mathrm{p}\mathrm{S}\mathrm{e}\mathrm{e}\mathrm{k}: \mathrm{f}\mathrm{r}\mathrm{o}\mathrm{m} \mathrm{A}\mathrm{u}\mathrm{g}\mathrm{u}\mathrm{s}\mathrm{t} 2024; \mathrm{Q}\mathrm{w}\mathrm{e}\mathrm{n}: \mathrm{f}\mathrm{r}\mathrm{o}\mathrm{m} \mathrm{J}\mathrm{u}\mathrm{l}\mathrm{y} 2024). \mathrm{E}\mathrm{a}\mathrm{c}\mathrm{h} \beta s \mathrm{i}\mathrm{s} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{e}\mathrm{x}\mathrm{t}\mathrm{r}\mathrm{a} \mathrm{c}\mathrm{h}\mathrm{a}\mathrm{n}\mathrm{g}\mathrm{e} \mathrm{i}\mathrm{n} \mathrm{t}\mathrm{h}\mathrm{a}\mathrm{t} \mathrm{m}\mathrm{o}\mathrm{d}\mathrm{e}\mathrm{l}'\mathrm{s}
\mathrm{d}\mathrm{i}\mathrm{s}\mathrm{a}\mathrm{g}\mathrm{r}\mathrm{e}\mathrm{e}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{t} \mathrm{a}\mathrm{t} \mathrm{i}\mathrm{t}\mathrm{s} \mathrm{o}\mathrm{w}\mathrm{n} \mathrm{c}\mathrm{u}\mathrm{t}\mathrm{o}ff \mathrm{b}\mathrm{e}\mathrm{y}\mathrm{o}\mathrm{n}\mathrm{d} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{m}\mathrm{m}\mathrm{o}\mathrm{n} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{e}\mathrm{n}\mathrm{d}\mathrm{a}\mathrm{r} \mathrm{t}\mathrm{r}\mathrm{e}\mathrm{n}\mathrm{d}; \mathrm{b}\mathrm{e}\mathrm{c}\mathrm{a}\mathrm{u}\mathrm{s}\mathrm{e} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{t}\mathrm{w}\mathrm{o} \mathrm{c}\mathrm{u}\mathrm{t}\mathrm{o}ff\mathrm{s} \mathrm{d}\mathrm{i}ff\mathrm{e}\mathrm{r} \mathrm{b}\mathrm{y} \mathrm{a}
\mathrm{m}\mathrm{o}\mathrm{n}\mathrm{t}\mathrm{h}, \mathrm{J}\mathrm{u}\mathrm{l}\mathrm{y} 2024 \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l}\mathrm{s} \mathrm{a}\mathrm{r}\mathrm{e} \mathrm{p}\mathrm{o}\mathrm{s}\mathrm{t}-\mathrm{c}\mathrm{u}\mathrm{t}\mathrm{o}ff \mathrm{f}\mathrm{o}\mathrm{r} \mathrm{o}\mathrm{n}\mathrm{e} \mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{d}\mathrm{d}\mathrm{l}\mathrm{e}\mathrm{r} \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{p}\mathrm{r}\mathrm{e}-\mathrm{c}\mathrm{u}\mathrm{t}\mathrm{o}ff \mathrm{f}\mathrm{o}\mathrm{r} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{o}\mathrm{t}\mathrm{h}\mathrm{e}\mathrm{r}. \mathrm{C}\mathrm{e}\mathrm{l}\mathrm{l}\mathrm{s} \mathrm{m}\mathrm{a}\mathrm{r}\mathrm{k}\mathrm{e}\mathrm{d} --- \mathrm{a}\mathrm{r}\mathrm{e}
\mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}--\mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} \mathrm{s}\mathrm{e}\mathrm{r}\mathrm{i}\mathrm{e}\mathrm{s} \mathrm{e}\mathrm{x}\mathrm{c}\mathrm{l}\mathrm{u}\mathrm{d}\mathrm{e}\mathrm{d} \mathrm{f}\mathrm{r}\mathrm{o}\mathrm{m} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{a}\mathrm{m}\mathrm{p}\mathrm{l}\mathrm{e} (\mathrm{S}\mathrm{e}\mathrm{c}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} 3.2). \mathrm{A} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{t}\mathrm{a}\mathrm{m}\mathrm{i}\mathrm{n}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}/\mathrm{l}\mathrm{o}\mathrm{o}\mathrm{k}-\mathrm{a}\mathrm{h}\mathrm{e}\mathrm{a}\mathrm{d} \mathrm{s}\mathrm{t}\mathrm{o}\mathrm{r}\mathrm{y} \mathrm{p}\mathrm{r}\mathrm{e}\mathrm{d}\mathrm{i}\mathrm{c}\mathrm{t}\mathrm{s}
\mathrm{t}\mathrm{h}\mathrm{e} \mathrm{n}\mathrm{e}\mathrm{w}\mathrm{s}-\mathrm{g}\mathrm{r}\mathrm{o}\mathrm{u}\mathrm{n}\mathrm{d}\mathrm{e}\mathrm{d}sentiment\mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} \mathrm{s}\mathrm{h}\mathrm{o}\mathrm{u}\mathrm{l}\mathrm{d} \mathrm{m}\mathrm{o}\mathrm{v}\mathrm{e} \mathrm{m}\mathrm{o}\mathrm{s}\mathrm{t}; \mathrm{i}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{e}\mathrm{a}\mathrm{d} \mathrm{i}\mathrm{t} \mathrm{i}\mathrm{s} \mathrm{a}\mathrm{m}\mathrm{o}\mathrm{n}\mathrm{g} \mathrm{t}\mathrm{h}\mathrm{e}least\mathrm{a}ff\mathrm{e}\mathrm{c}\mathrm{t}\mathrm{e}\mathrm{d} \mathrm{f}\mathrm{o}\mathrm{r} \mathrm{b}\mathrm{o}\mathrm{t}\mathrm{h}
\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{d}\mathrm{d}\mathrm{l}\mathrm{e}\mathrm{r}\mathrm{s}.t-\mathrm{s}\mathrm{t}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{i}\mathrm{c}\mathrm{s} \mathrm{i}\mathrm{n} \mathrm{p}\mathrm{a}\mathrm{r}\mathrm{e}\mathrm{n}\mathrm{t}\mathrm{h}\mathrm{e}\mathrm{s}\mathrm{e}\mathrm{s}, \mathrm{S}\mathrm{E} \mathrm{c}\mathrm{l}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{e}\mathrm{r}\mathrm{e}\mathrm{d} \mathrm{b}\mathrm{y} fi\mathrm{r}\mathrm{m}. \ast p<0.10; \ast \ast p<0.05; \ast \ast \ast p<0.01.
53

Appendix Table
Table A1: Definition of variables
Variable Definition
LLM-based variables
LLM Score
the score assigned by an LLM provider to the Q\&A text of a
call for a given construct, on the scale requested in the prompt
(0--1 for all constructs except sentiment, which is scored from
 - 1 to +1; the specificity ratio is defined as specific words over
total words). The full prompts are reported in the Appendix.
Scores are winsorized at the 1st and 99th percentiles within
construct and provider, and z-standardized within construct
and provider where indicated
LLM Confidence the self-reported confidence (0--1) that each provider returns together with its score
LLM Dispersion (Z)
the standard deviation of the seven providers' scores for the
same call and construct, computed after z-standardizing each
provider's scores within construct
Justif. Cosine Sim
the average pairwise cosine similarity of sentence embeddings
of the seven providers' written justifications for the same call
and construct
Justif. Jaccard Sim
the average pairwise word-overlap (Jaccard) similarity of the
seven providers' written justifications for the same call and
construct
Firm-level variables
ln(Assets) the natural logarithm of total assets (from Compustat)
BTM book-to-market ratio; total common/ordinary equity divided by the market value of equity (from Compustat)
Q
Tobin's Q; the book value of assets minus book value of common
equity plus the market value of common equity, divided by the
total book value of assets (from Compustat)
SUE standardized unexpected earnings, from the I/B/E/S surprise history file, matched to the call's earnings announcement date
CAR(0,1)
the cumulative abnormal return over trading days (0 , +1)
around the call, from a Carhart four-factor model estimated
on CRSP daily returns
Analyst Disp. (Q1)
the natural logarithm of one plus the coefficient of variation
(standard deviation over the absolute mean) of I/B/E/S an-
alyst EPS forecasts for the next fiscal quarter, from the first
consensus published within 60 days after the call
54

Analyst Count (Q1) the number of analyst estimates in that first post-call consensus
Pre-Call Analyst Disp. /
Count
the same dispersion and count measures, from the last consen-
sus published within 60 days before the call
Forecast Error
the absolute difference between the post-call consensus (the
mean of analysts' latest I/B/E/S detail-file forecasts issued
within 30 days after the call, requiring at least three analysts)
and the realized EPS for that quarter, scaled by the pre-call
share price and multiplied by 100
Abn. Bid-Ask / Volume /
Ret. Var.
abnormal bid-ask spread, trading volume, and return variance
over the (0, +1) announcement window, each relative to the
firm's estimation-window baseline (from CRSP)
Textual variables (management answers in the Q\&A)
Fog Index the Gunning fog readability index of the answers
ln(Word Count) the natural logarithm of the total number of words in the answers
Financial Jargon the ratio of finance-jargon terms to total words
Numbers the ratio of numeric tokens to total words
Forward-Looking
the ratio of forward-looking terms to total words; forward-
looking terms from Matsumoto et al. (2011) and Bozanic et al.
(2018)
Specificity
the ratio of specific tokens---named entities, numeric values,
monetary amounts, dates, and durations (Stanza named-entity
recognition plus rule-based matching)---to total words; this is
the non-LLM benchmark of the LLM specificity ratio
55

Online Appendix
Same Text, Different Numbers: The Divergence of
LLM-Based Measures
Hamid Boustanifar Sasan Mansouri

A Correlation Heatmaps
(a)\mathrm{S}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
 (b)\mathrm{T}\mathrm{e}\mathrm{x}\mathrm{t}\mathrm{u}\mathrm{a}\mathrm{l} \mathrm{s}\mathrm{i}\mathrm{m}\mathrm{i}\mathrm{l}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{j}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{i}fi\mathrm{c}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
Figure OA.A.1:\mathrm{S}\mathrm{e}\mathrm{n}\mathrm{t}\mathrm{i}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{t}
(a)\mathrm{S}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
 (b)\mathrm{T}\mathrm{e}\mathrm{x}\mathrm{t}\mathrm{u}\mathrm{a}\mathrm{l} \mathrm{s}\mathrm{i}\mathrm{m}\mathrm{i}\mathrm{l}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{j}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{i}fi\mathrm{c}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
Figure OA.A.2:\mathrm{U}\mathrm{n}\mathrm{c}\mathrm{e}\mathrm{r}\mathrm{t}\mathrm{a}\mathrm{i}\mathrm{n}\mathrm{t}\mathrm{y}
2

(a)\mathrm{S}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
 (b)\mathrm{T}\mathrm{e}\mathrm{x}\mathrm{t}\mathrm{u}\mathrm{a}\mathrm{l} \mathrm{s}\mathrm{i}\mathrm{m}\mathrm{i}\mathrm{l}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{j}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{i}fi\mathrm{c}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
Figure OA.A.3:\mathrm{S}\mathrm{p}\mathrm{e}\mathrm{c}\mathrm{i}fi\mathrm{c}\mathrm{i}\mathrm{t}\mathrm{y}
(a)\mathrm{S}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
 (b)\mathrm{T}\mathrm{e}\mathrm{x}\mathrm{t}\mathrm{u}\mathrm{a}\mathrm{l} \mathrm{s}\mathrm{i}\mathrm{m}\mathrm{i}\mathrm{l}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{j}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{i}fi\mathrm{c}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
Figure OA.A.4:\mathrm{S}\mathrm{p}\mathrm{e}\mathrm{c}\mathrm{i}fi\mathrm{c}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{R}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}
3

(a)\mathrm{S}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
 (b)\mathrm{T}\mathrm{e}\mathrm{x}\mathrm{t}\mathrm{u}\mathrm{a}\mathrm{l} \mathrm{s}\mathrm{i}\mathrm{m}\mathrm{i}\mathrm{l}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{j}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{i}fi\mathrm{c}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
Figure OA.A.5:\mathrm{I}\mathrm{n}\mathrm{n}\mathrm{o}\mathrm{v}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{S}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}
(a)\mathrm{S}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
 (b)\mathrm{T}\mathrm{e}\mathrm{x}\mathrm{t}\mathrm{u}\mathrm{a}\mathrm{l} \mathrm{s}\mathrm{i}\mathrm{m}\mathrm{i}\mathrm{l}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{j}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{i}fi\mathrm{c}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
Figure OA.A.6:\mathrm{C}\mathrm{l}\mathrm{i}\mathrm{m}\mathrm{a}\mathrm{t}\mathrm{e} \mathrm{R}\mathrm{i}\mathrm{s}\mathrm{k}
4

(a)\mathrm{S}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
 (b)\mathrm{T}\mathrm{e}\mathrm{x}\mathrm{t}\mathrm{u}\mathrm{a}\mathrm{l} \mathrm{s}\mathrm{i}\mathrm{m}\mathrm{i}\mathrm{l}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{j}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{i}fi\mathrm{c}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
Figure OA.A.7:\mathrm{P}\mathrm{o}\mathrm{l}\mathrm{i}\mathrm{t}\mathrm{i}\mathrm{c}\mathrm{a}\mathrm{l} \mathrm{R}\mathrm{i}\mathrm{s}\mathrm{k}
(a)\mathrm{S}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
 (b)\mathrm{T}\mathrm{e}\mathrm{x}\mathrm{t}\mathrm{u}\mathrm{a}\mathrm{l} \mathrm{s}\mathrm{i}\mathrm{m}\mathrm{i}\mathrm{l}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{j}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{i}fi\mathrm{c}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
Figure OA.A.8:\mathrm{C}\mathrm{o}\mathrm{r}\mathrm{p}\mathrm{o}\mathrm{r}\mathrm{a}\mathrm{t}\mathrm{e} \mathrm{C}\mathrm{u}\mathrm{l}\mathrm{t}\mathrm{u}\mathrm{r}\mathrm{e}
5

(a)\mathrm{S}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
 (b)\mathrm{T}\mathrm{e}\mathrm{x}\mathrm{t}\mathrm{u}\mathrm{a}\mathrm{l} \mathrm{s}\mathrm{i}\mathrm{m}\mathrm{i}\mathrm{l}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{j}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{i}fi\mathrm{c}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
Figure OA.A.9:\mathrm{M}\mathrm{a}\mathrm{n}\mathrm{a}\mathrm{g}\mathrm{e}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{t} \mathrm{C}\mathrm{l}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y}
(a)\mathrm{S}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
 (b)\mathrm{T}\mathrm{e}\mathrm{x}\mathrm{t}\mathrm{u}\mathrm{a}\mathrm{l} \mathrm{s}\mathrm{i}\mathrm{m}\mathrm{i}\mathrm{l}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{j}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{i}fi\mathrm{c}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
Figure OA.A.10:\mathrm{T}\mathrm{e}\mathrm{a}\mathrm{m}\mathrm{w}\mathrm{o}\mathrm{r}\mathrm{k} \mathrm{S}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}
6

(a)\mathrm{S}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
 (b)\mathrm{T}\mathrm{e}\mathrm{x}\mathrm{t}\mathrm{u}\mathrm{a}\mathrm{l} \mathrm{s}\mathrm{i}\mathrm{m}\mathrm{i}\mathrm{l}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{j}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{i}fi\mathrm{c}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
Figure OA.A.11:\mathrm{Q}\mathrm{u}\mathrm{a}\mathrm{l}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{S}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}
(a)\mathrm{S}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
 (b)\mathrm{T}\mathrm{e}\mathrm{x}\mathrm{t}\mathrm{u}\mathrm{a}\mathrm{l} \mathrm{s}\mathrm{i}\mathrm{m}\mathrm{i}\mathrm{l}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{j}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{i}fi\mathrm{c}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
Figure OA.A.12:\mathrm{R}\mathrm{e}\mathrm{s}\mathrm{p}\mathrm{e}\mathrm{c}\mathrm{t} \mathrm{S}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}
7

(a)\mathrm{S}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
 (b)\mathrm{T}\mathrm{e}\mathrm{x}\mathrm{t}\mathrm{u}\mathrm{a}\mathrm{l} \mathrm{s}\mathrm{i}\mathrm{m}\mathrm{i}\mathrm{l}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{j}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{i}fi\mathrm{c}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}
Figure OA.A.13:\mathrm{I}\mathrm{n}\mathrm{t}\mathrm{e}\mathrm{g}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{S}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}
8

B Summary Statistics --- Full Detail
Table OA.B.1:\mathrm{S}\mathrm{u}\mathrm{m}\mathrm{m}\mathrm{a}\mathrm{r}\mathrm{y} \mathrm{S}\mathrm{t}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{i}\mathrm{c}\mathrm{s} --- \mathrm{F}\mathrm{u}\mathrm{l}\mathrm{l} \mathrm{D}\mathrm{e}\mathrm{t}\mathrm{a}\mathrm{i}\mathrm{l} (\mathrm{i}\mathrm{n}\mathrm{c}\mathrm{l}. \mathrm{p}\mathrm{e}\mathrm{r}-\mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} \mathrm{L}\mathrm{L}\mathrm{M} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}\mathrm{s})
\mathrm{N} \mathrm{M}\mathrm{e}\mathrm{a}\mathrm{n} \mathrm{S}\mathrm{t}\mathrm{d} \mathrm{M}\mathrm{i}\mathrm{n} \mathrm{P}25 \mathrm{M}\mathrm{e}\mathrm{d}\mathrm{i}\mathrm{a}\mathrm{n} \mathrm{P}75 \mathrm{M}\mathrm{a}\mathrm{x}
LLM-related variables (call\times construct level)
\mathrm{L}\mathrm{L}\mathrm{M} \mathrm{D}\mathrm{i}\mathrm{s}\mathrm{p}\mathrm{e}\mathrm{r}\mathrm{s}\mathrm{i}\mathrm{o}\mathrm{n} (\mathrm{Z}) 25,298 0.618 0.315 0.067 0.415 0.583 0.784 2.787
\mathrm{J}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{i}\mathrm{f}. \mathrm{C}\mathrm{o}\mathrm{s}\mathrm{i}\mathrm{n}\mathrm{e} \mathrm{S}\mathrm{i}\mathrm{m} 25,298 0.618 0.102 0.204 0.564 0.624 0.682 0.931
\mathrm{J}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{i}\mathrm{f}. \mathrm{J}\mathrm{a}\mathrm{c}\mathrm{c}\mathrm{a}\mathrm{r}\mathrm{d} \mathrm{S}\mathrm{i}\mathrm{m} 25,298 0.183 0.061 0.010 0.150 0.169 0.193 0.584
Firm-level variables (call level)
\mathrm{l}\mathrm{n}(\mathrm{A}\mathrm{s}\mathrm{s}\mathrm{e}\mathrm{t}\mathrm{s}) 25,285 10.348 1.281 7.288 9.498 10.246 11.102 15.253
\mathrm{B}\mathrm{o}\mathrm{o}\mathrm{k}-\mathrm{t}\mathrm{o}-\mathrm{M}\mathrm{a}\mathrm{r}\mathrm{k}\mathrm{e}\mathrm{t} 25,246 0.328 0.308 -0.638 0.113 0.257 0.483 2.380
\mathrm{T}\mathrm{o}\mathrm{b}\mathrm{i}\mathrm{n}'\mathrm{s} \mathrm{Q} 25,246 2.892 2.712 0.760 1.345 1.961 3.386 34.202
\mathrm{S}\mathrm{U}\mathrm{E} 24,674 2.107 3.176 -5.769 0.279 1.634 3.300 14.696
\mathrm{C}\mathrm{A}\mathrm{R}(0,1) 25,155 0.020 6.540 -20.733 -3.922 -0.106 4.069 17.321
\mathrm{A}\mathrm{n}\mathrm{a}\mathrm{l}\mathrm{y}\mathrm{s}\mathrm{t} \mathrm{D}\mathrm{i}\mathrm{s}\mathrm{p}. (\mathrm{Q}1) 25,155 0.070 0.103 0.003 0.019 0.037 0.076 0.693
\mathrm{A}\mathrm{n}\mathrm{a}\mathrm{l}\mathrm{y}\mathrm{s}\mathrm{t} \mathrm{C}\mathrm{o}\mathrm{u}\mathrm{n}\mathrm{t} (\mathrm{Q}1) 25,181 15.126 6.578 3.000 11.000 15.000 19.000 36.000
\mathrm{P}\mathrm{r}\mathrm{e}-\mathrm{C}\mathrm{a}\mathrm{l}\mathrm{l} \mathrm{A}\mathrm{n}\mathrm{a}\mathrm{l}\mathrm{y}\mathrm{s}\mathrm{t} \mathrm{D}\mathrm{i}\mathrm{s}\mathrm{p}. 25,129 0.071 0.111 0.003 0.019 0.037 0.074 0.799
\mathrm{P}\mathrm{r}\mathrm{e}-\mathrm{C}\mathrm{a}\mathrm{l}\mathrm{l} \mathrm{A}\mathrm{n}\mathrm{a}\mathrm{l}\mathrm{y}\mathrm{s}\mathrm{t} \mathrm{C}\mathrm{o}\mathrm{u}\mathrm{n}\mathrm{t} 25,142 15.989 6.420 4.000 11.000 16.000 20.000 38.000
Textual variables (call level)
\mathrm{F}\mathrm{o}\mathrm{g} \mathrm{I}\mathrm{n}\mathrm{d}\mathrm{e}\mathrm{x} 25,298 7.381 0.835 5.112 6.809 7.301 7.868 11.633
\mathrm{l}\mathrm{n}(\mathrm{W}\mathrm{o}\mathrm{r}\mathrm{d} \mathrm{C}\mathrm{o}\mathrm{u}\mathrm{n}\mathrm{t}) 25,298 8.243 0.352 4.682 8.067 8.278 8.461 9.091
\mathrm{F}\mathrm{i}\mathrm{n}\mathrm{a}\mathrm{n}\mathrm{c}\mathrm{i}\mathrm{a}\mathrm{l} \mathrm{J}\mathrm{a}\mathrm{r}\mathrm{g}\mathrm{o}\mathrm{n} 25,298 0.063 0.011 0.032 0.056 0.063 0.070 0.110
\mathrm{N}\mathrm{u}\mathrm{m}\mathrm{b}\mathrm{e}\mathrm{r}\mathrm{s} 25,298 0.012 0.005 0.000 0.008 0.011 0.015 0.036
\mathrm{F}\mathrm{o}\mathrm{r}\mathrm{w}\mathrm{a}\mathrm{r}\mathrm{d}-\mathrm{L}\mathrm{o}\mathrm{o}\mathrm{k}\mathrm{i}\mathrm{n}\mathrm{g} 25,298 0.057 0.012 0.023 0.049 0.056 0.064 0.187
\mathrm{S}\mathrm{p}\mathrm{e}\mathrm{c}\mathrm{i}fi\mathrm{c}\mathrm{i}\mathrm{t}\mathrm{y} 25,298 0.013 0.004 0.004 0.011 0.013 0.016 0.040
continued on next page
9

(Table OA.B.1 continued)
\mathrm{N} \mathrm{M}\mathrm{e}\mathrm{a}\mathrm{n} \mathrm{S}\mathrm{t}\mathrm{d} \mathrm{M}\mathrm{i}\mathrm{n} \mathrm{P}25 \mathrm{M}\mathrm{e}\mathrm{d}\mathrm{i}\mathrm{a}\mathrm{n} \mathrm{P}75 \mathrm{M}\mathrm{a}\mathrm{x}
LLM scores (z-scored, by task)
Climate Risk
\mathrm{M}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{l} 1,946 -0.000 1.000 -0.511 -0.511 -0.511 0.582 3.863
\mathrm{G}\mathrm{e}\mathrm{m}\mathrm{i}\mathrm{n}\mathrm{i} 1,946 -0.000 1.000 -0.751 -0.751 -0.056 -0.056 4.118
\mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{A}\mathrm{I} 1,946 -0.000 1.000 -0.633 -0.633 -0.633 0.634 4.117
\mathrm{Q}\mathrm{w}\mathrm{e}\mathrm{n} 1,946 0.000 1.000 -0.501 -0.501 -0.501 0.499 4.497
\mathrm{L}\mathrm{l}\mathrm{a}\mathrm{m}\mathrm{a} 1,946 0.000 1.000 -0.339 -0.339 -0.339 -0.339 5.121
\mathrm{D}\mathrm{e}\mathrm{e}\mathrm{p}\mathrm{S}\mathrm{e}\mathrm{e}\mathrm{k} 1,946 0.000 1.000 -0.594 -0.594 -0.594 0.383 5.048
\mathrm{A}\mathrm{n}\mathrm{t}\mathrm{h}\mathrm{r}\mathrm{o}\mathrm{p}\mathrm{i}\mathrm{c} 1,946 -0.000 1.000 -0.233 -0.233 -0.233 -0.233 4.292
Corporate Culture
\mathrm{M}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{l} 1,938 0.000 1.000 -2.057 -0.774 0.152 0.650 1.933
\mathrm{G}\mathrm{e}\mathrm{m}\mathrm{i}\mathrm{n}\mathrm{i} 1,946 -0.000 1.000 -2.064 -0.681 -0.012 0.635 2.662
\mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{A}\mathrm{I} 1,946 0.000 1.000 -2.994 -0.461 0.298 0.636 1.565
\mathrm{Q}\mathrm{w}\mathrm{e}\mathrm{n} 1,946 -0.000 1.000 -2.457 -0.704 0.173 0.757 2.101
\mathrm{L}\mathrm{l}\mathrm{a}\mathrm{m}\mathrm{a} 1,946 -0.000 1.000 -2.189 -0.760 0.097 0.669 2.170
\mathrm{D}\mathrm{e}\mathrm{e}\mathrm{p}\mathrm{S}\mathrm{e}\mathrm{e}\mathrm{k} 1,946 0.000 1.000 -1.801 -0.849 0.035 0.715 2.143
\mathrm{A}\mathrm{n}\mathrm{t}\mathrm{h}\mathrm{r}\mathrm{o}\mathrm{p}\mathrm{i}\mathrm{c} 1,946 -0.000 1.000 -3.011 -0.942 0.207 0.590 1.816
Innovation
\mathrm{M}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{l} 1,946 -0.000 1.000 -1.725 -1.327 0.263 1.059 1.456
\mathrm{G}\mathrm{e}\mathrm{m}\mathrm{i}\mathrm{n}\mathrm{i} 1,946 0.000 1.000 -1.782 -1.004 -0.226 0.942 1.720
\mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{A}\mathrm{I} 1,946 -0.000 1.000 -2.392 -0.243 0.294 0.563 1.368
\mathrm{Q}\mathrm{w}\mathrm{e}\mathrm{n} 1,946 -0.000 1.000 -1.615 -0.245 -0.245 0.441 3.868
\mathrm{L}\mathrm{l}\mathrm{a}\mathrm{m}\mathrm{a} 1,946 0.000 1.000 -1.589 -0.816 -0.816 0.730 1.503
continued on next page
10

(Table OA.B.1 continued)
\mathrm{N} \mathrm{M}\mathrm{e}\mathrm{a}\mathrm{n} \mathrm{S}\mathrm{t}\mathrm{d} \mathrm{M}\mathrm{i}\mathrm{n} \mathrm{P}25 \mathrm{M}\mathrm{e}\mathrm{d}\mathrm{i}\mathrm{a}\mathrm{n} \mathrm{P}75 \mathrm{M}\mathrm{a}\mathrm{x}
\mathrm{D}\mathrm{e}\mathrm{e}\mathrm{p}\mathrm{S}\mathrm{e}\mathrm{e}\mathrm{k} 1,946 0.000 1.000 -1.604 -0.756 -0.120 0.940 1.788
\mathrm{A}\mathrm{n}\mathrm{t}\mathrm{h}\mathrm{r}\mathrm{o}\mathrm{p}\mathrm{i}\mathrm{c} 1,946 -0.000 1.000 -2.791 -0.085 -0.085 0.998 1.539
Integrity
\mathrm{M}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{l} 1,942 -0.000 1.000 -1.664 -0.433 -0.433 0.798 2.644
\mathrm{G}\mathrm{e}\mathrm{m}\mathrm{i}\mathrm{n}\mathrm{i} 1,946 0.000 1.000 -0.664 -0.664 -0.664 0.236 4.739
\mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{A}\mathrm{I} 1,946 0.000 1.000 -2.608 -0.232 -0.232 0.560 2.144
\mathrm{Q}\mathrm{w}\mathrm{e}\mathrm{n} 1,946 0.000 1.000 -2.371 -0.880 0.115 0.612 1.855
\mathrm{L}\mathrm{l}\mathrm{a}\mathrm{m}\mathrm{a} 1,946 -0.000 1.000 -1.246 -0.609 0.028 0.028 3.848
\mathrm{D}\mathrm{e}\mathrm{e}\mathrm{p}\mathrm{S}\mathrm{e}\mathrm{e}\mathrm{k} 1,946 -0.000 1.000 -0.999 -0.999 -0.379 0.241 3.030
\mathrm{A}\mathrm{n}\mathrm{t}\mathrm{h}\mathrm{r}\mathrm{o}\mathrm{p}\mathrm{i}\mathrm{c} 1,946 0.000 1.000 -3.323 -0.468 -0.468 0.959 1.245
Management Clarity
\mathrm{M}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{l} 1,946 -0.000 1.000 -1.688 0.118 0.118 0.118 1.924
\mathrm{G}\mathrm{e}\mathrm{m}\mathrm{i}\mathrm{n}\mathrm{i} 1,946 -0.000 1.000 -2.797 -0.051 -0.051 1.048 1.048
\mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{A}\mathrm{I} 1,946 -0.000 1.000 -2.738 -0.100 -0.100 1.219 1.219
\mathrm{Q}\mathrm{w}\mathrm{e}\mathrm{n} 1,946 -0.000 1.000 -2.328 -0.777 0.774 0.774 0.774
\mathrm{L}\mathrm{l}\mathrm{a}\mathrm{m}\mathrm{a} 1,946 -0.000 1.000 -4.846 0.021 0.021 0.697 0.899
\mathrm{D}\mathrm{e}\mathrm{e}\mathrm{p}\mathrm{S}\mathrm{e}\mathrm{e}\mathrm{k} 1,946 -0.000 1.000 -2.712 -0.526 0.567 0.567 1.660
\mathrm{A}\mathrm{n}\mathrm{t}\mathrm{h}\mathrm{r}\mathrm{o}\mathrm{p}\mathrm{i}\mathrm{c} 1,946 0.000 1.000 -2.360 -0.542 -0.542 1.276 2.185
Political Risk
\mathrm{M}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{l} 1,946 -0.000 1.000 -0.394 -0.394 -0.394 -0.394 2.880
\mathrm{G}\mathrm{e}\mathrm{m}\mathrm{i}\mathrm{n}\mathrm{i} 1,946 0.000 1.000 -0.656 -0.656 -0.656 0.127 4.041
\mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{A}\mathrm{I} 1,946 0.000 1.000 -0.294 -0.294 -0.294 -0.294 5.757
\mathrm{L}\mathrm{l}\mathrm{a}\mathrm{m}\mathrm{a} 1,946 0.000 1.000 -0.394 -0.394 -0.394 -0.394 5.077
continued on next page
11

(Table OA.B.1 continued)
\mathrm{N} \mathrm{M}\mathrm{e}\mathrm{a}\mathrm{n} \mathrm{S}\mathrm{t}\mathrm{d} \mathrm{M}\mathrm{i}\mathrm{n} \mathrm{P}25 \mathrm{M}\mathrm{e}\mathrm{d}\mathrm{i}\mathrm{a}\mathrm{n} \mathrm{P}75 \mathrm{M}\mathrm{a}\mathrm{x}
\mathrm{D}\mathrm{e}\mathrm{e}\mathrm{p}\mathrm{S}\mathrm{e}\mathrm{e}\mathrm{k} 1,946 -0.000 1.000 -0.435 -0.435 -0.435 -0.435 4.351
Quality
\mathrm{M}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{l} 1,942 -0.000 1.000 -2.468 -0.633 -0.021 0.591 2.426
\mathrm{G}\mathrm{e}\mathrm{m}\mathrm{i}\mathrm{n}\mathrm{i} 1,946 -0.000 1.000 -2.014 -0.963 0.088 0.614 2.190
\mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{A}\mathrm{I} 1,946 0.000 1.000 -2.446 -0.556 0.389 0.862 1.807
\mathrm{Q}\mathrm{w}\mathrm{e}\mathrm{n} 1,946 -0.000 1.000 -1.873 -0.869 0.134 0.636 2.141
\mathrm{L}\mathrm{l}\mathrm{a}\mathrm{m}\mathrm{a} 1,946 0.000 1.000 -2.277 -0.784 -0.287 0.709 1.704
\mathrm{D}\mathrm{e}\mathrm{e}\mathrm{p}\mathrm{S}\mathrm{e}\mathrm{e}\mathrm{k} 1,946 -0.000 1.000 -2.021 -0.646 -0.095 1.006 1.831
\mathrm{A}\mathrm{n}\mathrm{t}\mathrm{h}\mathrm{r}\mathrm{o}\mathrm{p}\mathrm{i}\mathrm{c} 1,946 -0.000 1.000 -2.921 -1.180 0.562 0.562 0.910
Respect
\mathrm{M}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{l} 1,939 0.000 1.000 -2.101 -0.741 -0.060 0.620 2.660
\mathrm{G}\mathrm{e}\mathrm{m}\mathrm{i}\mathrm{n}\mathrm{i} 1,946 -0.000 1.000 -0.884 -0.884 0.232 0.232 3.583
\mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{A}\mathrm{I} 1,946 0.000 1.000 -2.289 -0.888 0.162 0.862 1.913
\mathrm{Q}\mathrm{w}\mathrm{e}\mathrm{n} 1,946 -0.000 1.000 -2.005 -0.652 0.250 0.701 1.828
\mathrm{L}\mathrm{l}\mathrm{a}\mathrm{m}\mathrm{a} 1,946 0.000 1.000 -1.432 -0.846 -0.259 0.914 3.261
\mathrm{D}\mathrm{e}\mathrm{e}\mathrm{p}\mathrm{S}\mathrm{e}\mathrm{e}\mathrm{k} 1,946 -0.000 1.000 -1.223 -0.883 -0.033 0.817 2.856
\mathrm{A}\mathrm{n}\mathrm{t}\mathrm{h}\mathrm{r}\mathrm{o}\mathrm{p}\mathrm{i}\mathrm{c} 1,946 0.000 1.000 -2.392 -0.876 0.639 0.639 2.155
Sentiment
\mathrm{M}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{l} 1,946 -0.000 1.000 -3.385 -0.779 0.524 0.524 1.393
\mathrm{G}\mathrm{e}\mathrm{m}\mathrm{i}\mathrm{n}\mathrm{i} 1,946 -0.000 1.000 -2.878 -0.856 0.431 0.983 1.351
\mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{A}\mathrm{I} 1,946 -0.000 1.000 -2.571 -0.581 0.215 1.011 1.807
\mathrm{Q}\mathrm{w}\mathrm{e}\mathrm{n} 1,946 -0.000 1.000 -3.447 -0.836 0.469 0.469 1.340
\mathrm{L}\mathrm{l}\mathrm{a}\mathrm{m}\mathrm{a} 1,946 0.000 1.000 -3.454 0.081 0.081 0.912 1.120
continued on next page
12

(Table OA.B.1 continued)
\mathrm{N} \mathrm{M}\mathrm{e}\mathrm{a}\mathrm{n} \mathrm{S}\mathrm{t}\mathrm{d} \mathrm{M}\mathrm{i}\mathrm{n} \mathrm{P}25 \mathrm{M}\mathrm{e}\mathrm{d}\mathrm{i}\mathrm{a}\mathrm{n} \mathrm{P}75 \mathrm{M}\mathrm{a}\mathrm{x}
\mathrm{D}\mathrm{e}\mathrm{e}\mathrm{p}\mathrm{S}\mathrm{e}\mathrm{e}\mathrm{k} 1,946 -0.000 1.000 -3.206 -0.781 0.432 0.836 1.240
\mathrm{A}\mathrm{n}\mathrm{t}\mathrm{h}\mathrm{r}\mathrm{o}\mathrm{p}\mathrm{i}\mathrm{c} 1,946 0.000 1.000 -2.683 -0.545 0.168 0.643 1.831
Specificity
\mathrm{M}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{l} 1,946 -0.000 1.000 -2.039 -0.671 0.356 0.698 1.383
\mathrm{G}\mathrm{e}\mathrm{m}\mathrm{i}\mathrm{n}\mathrm{i} 1,946 -0.000 1.000 -2.943 -0.497 0.318 0.318 1.541
\mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{A}\mathrm{I} 1,946 -0.000 1.000 -2.831 -0.149 -0.149 0.745 1.639
\mathrm{Q}\mathrm{w}\mathrm{e}\mathrm{n} 1,946 0.000 1.000 -2.619 -0.198 0.609 0.609 1.416
\mathrm{L}\mathrm{l}\mathrm{a}\mathrm{m}\mathrm{a} 1,946 -0.000 1.000 -4.594 -0.345 0.409 0.409 1.232
\mathrm{D}\mathrm{e}\mathrm{e}\mathrm{p}\mathrm{S}\mathrm{e}\mathrm{e}\mathrm{k} 1,946 -0.000 1.000 -2.141 -0.290 0.081 0.821 1.562
\mathrm{A}\mathrm{n}\mathrm{t}\mathrm{h}\mathrm{r}\mathrm{o}\mathrm{p}\mathrm{i}\mathrm{c} 1,946 -0.000 1.000 -2.915 -0.501 -0.501 1.108 1.108
Specificity Ratio
\mathrm{M}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{l} 1,946 -0.000 1.000 -1.811 -0.459 -0.213 0.771 2.123
\mathrm{G}\mathrm{e}\mathrm{m}\mathrm{i}\mathrm{n}\mathrm{i} 1,946 0.000 1.000 -2.191 -0.338 -0.232 0.912 2.004
\mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{A}\mathrm{I} 1,946 -0.000 1.000 -0.783 -0.369 -0.231 -0.002 5.514
\mathrm{Q}\mathrm{w}\mathrm{e}\mathrm{n} 1,946 -0.000 1.000 -1.228 -0.503 -0.503 0.223 3.687
\mathrm{L}\mathrm{l}\mathrm{a}\mathrm{m}\mathrm{a} 1,878 0.000 1.000 -1.337 -0.764 -0.286 0.442 3.013
\mathrm{D}\mathrm{e}\mathrm{e}\mathrm{p}\mathrm{S}\mathrm{e}\mathrm{e}\mathrm{k} 1,946 -0.000 1.000 -1.750 -0.395 -0.395 0.535 2.395
\mathrm{A}\mathrm{n}\mathrm{t}\mathrm{h}\mathrm{r}\mathrm{o}\mathrm{p}\mathrm{i}\mathrm{c} 1,946 -0.000 1.000 -1.210 -0.441 -0.441 1.096 2.633
Teamwork
\mathrm{M}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{l} 1,939 0.000 1.000 -2.530 -0.875 0.228 0.779 1.883
\mathrm{G}\mathrm{e}\mathrm{m}\mathrm{i}\mathrm{n}\mathrm{i} 1,946 -0.000 1.000 -1.576 -0.822 -0.069 0.684 2.944
\mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{A}\mathrm{I} 1,946 -0.000 1.000 -2.581 -0.685 0.073 0.832 1.590
\mathrm{Q}\mathrm{w}\mathrm{e}\mathrm{n} 1,946 0.000 1.000 -1.855 -0.857 0.141 0.640 2.137
continued on next page
13

(Table OA.B.1 continued)
\mathrm{N} \mathrm{M}\mathrm{e}\mathrm{a}\mathrm{n} \mathrm{S}\mathrm{t}\mathrm{d} \mathrm{M}\mathrm{i}\mathrm{n} \mathrm{P}25 \mathrm{M}\mathrm{e}\mathrm{d}\mathrm{i}\mathrm{a}\mathrm{n} \mathrm{P}75 \mathrm{M}\mathrm{a}\mathrm{x}
\mathrm{L}\mathrm{l}\mathrm{a}\mathrm{m}\mathrm{a} 1,946 -0.000 1.000 -1.996 -0.926 0.145 0.680 2.285
\mathrm{D}\mathrm{e}\mathrm{e}\mathrm{p}\mathrm{S}\mathrm{e}\mathrm{e}\mathrm{k} 1,946 -0.000 1.000 -1.885 -0.991 -0.098 0.497 2.284
\mathrm{A}\mathrm{n}\mathrm{t}\mathrm{h}\mathrm{r}\mathrm{o}\mathrm{p}\mathrm{i}\mathrm{c} 1,946 0.000 1.000 -2.422 -1.056 0.310 0.310 1.676
Uncertainty
\mathrm{M}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{l} 1,946 -0.000 1.000 -3.382 -0.160 -0.160 -0.160 1.451
\mathrm{G}\mathrm{e}\mathrm{m}\mathrm{i}\mathrm{n}\mathrm{i} 1,946 -0.000 1.000 -3.774 -0.433 0.680 0.680 1.794
\mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{A}\mathrm{I} 1,946 -0.000 1.000 -2.172 -1.246 0.608 0.608 1.534
\mathrm{Q}\mathrm{w}\mathrm{e}\mathrm{n} 1,946 0.000 1.000 -1.902 -0.947 0.008 0.962 3.827
\mathrm{L}\mathrm{l}\mathrm{a}\mathrm{m}\mathrm{a} 1,946 0.000 1.000 -3.956 -1.006 0.398 0.609 1.505
\mathrm{D}\mathrm{e}\mathrm{e}\mathrm{p}\mathrm{S}\mathrm{e}\mathrm{e}\mathrm{k} 1,946 0.000 1.000 -2.034 -0.712 0.611 0.611 1.273
\mathrm{A}\mathrm{n}\mathrm{t}\mathrm{h}\mathrm{r}\mathrm{o}\mathrm{p}\mathrm{i}\mathrm{c} 1,946 0.000 1.000 -1.198 -0.844 -0.135 1.282 2.345
Notes:\mathrm{S}\mathrm{u}\mathrm{m}\mathrm{m}\mathrm{a}\mathrm{r}\mathrm{y} \mathrm{s}\mathrm{t}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{i}\mathrm{c}\mathrm{s} \mathrm{f}\mathrm{o}\mathrm{r} \mathrm{v}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{a}\mathrm{b}\mathrm{l}\mathrm{e}\mathrm{s} \mathrm{i}\mathrm{n} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{m}\mathrm{a}\mathrm{i}\mathrm{n} \mathrm{a}\mathrm{n}\mathrm{a}\mathrm{l}\mathrm{y}\mathrm{s}\mathrm{e}\mathrm{s}. \mathrm{V}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{a}\mathrm{b}\mathrm{l}\mathrm{e} \mathrm{d}\mathrm{e}fi\mathrm{n}\mathrm{i}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s} \mathrm{a}\mathrm{p}\mathrm{p}\mathrm{e}\mathrm{a}\mathrm{r} \mathrm{i}\mathrm{n} \mathrm{T}\mathrm{a}\mathrm{b}\mathrm{l}\mathrm{e} \mathrm{A}1. \mathrm{L}\mathrm{L}\mathrm{M}
\mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}\mathrm{s} \mathrm{a}\mathrm{r}\mathrm{e} \mathrm{z}-\mathrm{s}\mathrm{t}\mathrm{a}\mathrm{n}\mathrm{d}\mathrm{a}\mathrm{r}\mathrm{d}\mathrm{i}\mathrm{z}\mathrm{e}\mathrm{d} \mathrm{w}\mathrm{i}\mathrm{t}\mathrm{h}\mathrm{i}\mathrm{n} \mathrm{t}\mathrm{a}\mathrm{s}\mathrm{k}. \mathrm{F}\mathrm{i}\mathrm{r}\mathrm{m}-\mathrm{l}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{l} \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{t}\mathrm{e}\mathrm{x}\mathrm{t}\mathrm{u}\mathrm{a}\mathrm{l} \mathrm{v}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{a}\mathrm{b}\mathrm{l}\mathrm{e}\mathrm{s} \mathrm{r}\mathrm{e}\mathrm{p}\mathrm{e}\mathrm{a}\mathrm{t} \mathrm{a}\mathrm{c}\mathrm{r}\mathrm{o}\mathrm{s}\mathrm{s} \mathrm{t}\mathrm{h}\mathrm{e} 13 \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t}\mathrm{s} \mathrm{i}\mathrm{n} \mathrm{t}\mathrm{h}\mathrm{i}\mathrm{s}
\mathrm{p}\mathrm{o}\mathrm{o}\mathrm{l}\mathrm{e}\mathrm{d} \mathrm{p}\mathrm{a}\mathrm{n}\mathrm{e}\mathrm{l}; \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l}-\mathrm{l}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{l} \mathrm{s}\mathrm{t}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{i}\mathrm{c}\mathrm{s} \mathrm{a}\mathrm{r}\mathrm{e} \mathrm{i}\mathrm{n} \mathrm{T}\mathrm{a}\mathrm{b}\mathrm{l}\mathrm{e} 1.
14

C Dispersion Regression Tables
Table OA.C.1:\mathrm{D}\mathrm{e}\mathrm{t}\mathrm{e}\mathrm{r}\mathrm{m}\mathrm{i}\mathrm{n}\mathrm{a}\mathrm{n}\mathrm{t}\mathrm{s} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{e}\mathrm{x}\mathrm{t}\mathrm{u}\mathrm{a}\mathrm{l} \mathrm{m}\mathrm{e}\mathrm{a}\mathrm{s}\mathrm{u}\mathrm{r}\mathrm{e} \mathrm{d}\mathrm{i}\mathrm{s}\mathrm{p}\mathrm{e}\mathrm{r}\mathrm{s}\mathrm{i}\mathrm{o}\mathrm{n} (\mathrm{r}\mathrm{a}\mathrm{n}\mathrm{g}\mathrm{e}-\mathrm{b}\mathrm{a}\mathrm{s}\mathrm{e}\mathrm{d}).
\mathrm{T}\mathrm{e}\mathrm{x}\mathrm{t}\mathrm{u}\mathrm{a}\mathrm{l} \mathrm{M}\mathrm{e}\mathrm{a}\mathrm{s}\mathrm{u}\mathrm{r}\mathrm{e} \mathrm{D}\mathrm{i}\mathrm{s}\mathrm{p}\mathrm{e}\mathrm{r}\mathrm{s}\mathrm{i}\mathrm{o}\mathrm{n} (\mathrm{R}\mathrm{a}\mathrm{n}\mathrm{g}\mathrm{e})
(1) (2) (3) (4)
Panel A: Firm Controls
\mathrm{l}\mathrm{n}(\mathrm{A}\mathrm{s}\mathrm{s}\mathrm{e}\mathrm{t}\mathrm{s}) 0.0169 \ast \ast \ast 0.0069 0.0070 0.0112 \ast
(2.63) (1.04) (1.06) (1.76)
\mathrm{B}\mathrm{o}\mathrm{o}\mathrm{k}-\mathrm{t}\mathrm{o}-\mathrm{M}\mathrm{a}\mathrm{r}\mathrm{k}\mathrm{e}\mathrm{t} 0.0108 -0.0090 -0.0092 -0.0191
(0.38) (-0.29) (-0.29) (-0.70)
\mathrm{T}\mathrm{o}\mathrm{b}\mathrm{i}\mathrm{n}'\mathrm{s}Q0.0065 \ast \ast 0.0094\ast \ast \ast 0.0092\ast \ast \ast 0.0123\ast \ast \ast
(2.38) (3.52) (3.46) (4.65)
\mathrm{S}\mathrm{U}\mathrm{E} -0.0032 -0.0011 -0.0011 0.0008
(-1.57) (-0.54) (-0.53) (0.39)
Panel B: Textual Controls
\mathrm{F}\mathrm{o}\mathrm{g} \mathrm{I}\mathrm{n}\mathrm{d}\mathrm{e}\mathrm{x} -0.0074 0.0038
(-0.78) (0.39)
\mathrm{l}\mathrm{n}(\mathrm{W}\mathrm{o}\mathrm{r}\mathrm{d} \mathrm{C}\mathrm{o}\mathrm{u}\mathrm{n}\mathrm{t}) -0.0828 \ast \ast \ast
(-3.17)
\mathrm{F}\mathrm{i}\mathrm{n}\mathrm{a}\mathrm{n}\mathrm{c}\mathrm{i}\mathrm{a}\mathrm{l} \mathrm{J}\mathrm{a}\mathrm{r}\mathrm{g}\mathrm{o}\mathrm{n} -1.0921
(-1.37)
\mathrm{N}\mathrm{u}\mathrm{m}\mathrm{b}\mathrm{e}\mathrm{r}\mathrm{s} 1.8590
(1.42)
\mathrm{F}\mathrm{o}\mathrm{r}\mathrm{w}\mathrm{a}\mathrm{r}\mathrm{d}-\mathrm{L}\mathrm{o}\mathrm{o}\mathrm{k}\mathrm{i}\mathrm{n}\mathrm{g} \mathrm{L}\mathrm{a}\mathrm{n}\mathrm{g}\mathrm{u}\mathrm{a}\mathrm{g}\mathrm{e} 1.9736 \ast \ast \ast
(2.94)
\mathrm{J}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{i}fi\mathrm{c}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{S}\mathrm{i}\mathrm{m}\mathrm{i}\mathrm{l}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} -1.7357 \ast \ast \ast
(-14.77)
\mathrm{F}\mathrm{E} -- \mathrm{I}\mathrm{n}\mathrm{d}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{y} \mathrm{I}\mathrm{n}\mathrm{d}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{y} \mathrm{I}\mathrm{n}\mathrm{d}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{y}
\mathrm{Q}\mathrm{u}\mathrm{a}\mathrm{r}\mathrm{t}\mathrm{e}\mathrm{r} \mathrm{F}\mathrm{E} \mathrm{N}\mathrm{o} \mathrm{Y}\mathrm{e}\mathrm{s} \mathrm{Y}\mathrm{e}\mathrm{s} \mathrm{Y}\mathrm{e}\mathrm{s}
\mathrm{C}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} \mathrm{F}\mathrm{E} \mathrm{Y}\mathrm{e}\mathrm{s} \mathrm{Y}\mathrm{e}\mathrm{s} \mathrm{Y}\mathrm{e}\mathrm{s} \mathrm{Y}\mathrm{e}\mathrm{s}
\mathrm{O}\mathrm{b}\mathrm{s}\mathrm{e}\mathrm{r}\mathrm{v}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s} 24,622 24,622 24,622 24,622
\mathrm{A}\mathrm{d}\mathrm{j}.R 2 0.196 0.199 0.199 0.217
Notes:\mathrm{E}\mathrm{a}\mathrm{c}\mathrm{h} \mathrm{c}\mathrm{o}\mathrm{l}\mathrm{u}\mathrm{m}\mathrm{n} \mathrm{i}\mathrm{s} \mathrm{a}\mathrm{n} \mathrm{O}\mathrm{L}\mathrm{S} \mathrm{r}\mathrm{e}\mathrm{g}\mathrm{r}\mathrm{e}\mathrm{s}\mathrm{s}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{a}\mathrm{t} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l}--\mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} \mathrm{l}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{l} (1,894 \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l}\mathrm{s} \mathrm{w}\mathrm{i}\mathrm{t}\mathrm{h} \mathrm{n}\mathrm{o}\mathrm{n}-\mathrm{m}\mathrm{i}\mathrm{s}\mathrm{s}\mathrm{i}\mathrm{n}\mathrm{g} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{t}\mathrm{r}\mathrm{o}\mathrm{l}\mathrm{s} \times
13 \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t}\mathrm{s}). \mathrm{T}\mathrm{h}\mathrm{e} \mathrm{d}\mathrm{e}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{d}\mathrm{e}\mathrm{n}\mathrm{t} \mathrm{v}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{a}\mathrm{b}\mathrm{l}\mathrm{e} \mathrm{i}\mathrm{s} \mathrm{L}\mathrm{L}\mathrm{M} \mathrm{d}\mathrm{i}\mathrm{s}\mathrm{p}\mathrm{e}\mathrm{r}\mathrm{s}\mathrm{i}\mathrm{o}\mathrm{n}: \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{r}\mathrm{a}\mathrm{n}\mathrm{g}\mathrm{e} (\mathrm{m}\mathrm{a}\mathrm{x}\mathrm{i}\mathrm{m}\mathrm{u}\mathrm{m} \mathrm{m}\mathrm{i}\mathrm{n}\mathrm{u}\mathrm{s} \mathrm{m}\mathrm{i}\mathrm{n}\mathrm{i}\mathrm{m}\mathrm{u}\mathrm{m}) \mathrm{a}\mathrm{c}\mathrm{r}\mathrm{o}\mathrm{s}\mathrm{s}
\mathrm{t}\mathrm{h}\mathrm{e} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}\mathrm{s} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}-\mathrm{s}\mathrm{t}\mathrm{a}\mathrm{n}\mathrm{d}\mathrm{a}\mathrm{r}\mathrm{d}\mathrm{i}\mathrm{z}\mathrm{e}\mathrm{d} \mathrm{L}\mathrm{L}\mathrm{M} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{f}\mathrm{o}\mathrm{r} \mathrm{t}\mathrm{h}\mathrm{a}\mathrm{t} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l} \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} (\mathrm{o}\mathrm{v}\mathrm{e}\mathrm{r} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}\mathrm{s} \mathrm{w}\mathrm{i}\mathrm{t}\mathrm{h} \mathrm{a}
\mathrm{v}\mathrm{a}\mathrm{l}\mathrm{i}\mathrm{d} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{f}\mathrm{o}\mathrm{r} \mathrm{t}\mathrm{h}\mathrm{a}\mathrm{t} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l} \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t}). \mathrm{C}\mathrm{o}\mathrm{n}\mathrm{t}\mathrm{r}\mathrm{o}\mathrm{l}\mathrm{s}: \mathrm{l}\mathrm{n}(\mathrm{A}\mathrm{s}\mathrm{s}\mathrm{e}\mathrm{t}\mathrm{s}), \mathrm{b}\mathrm{o}\mathrm{o}\mathrm{k}-\mathrm{t}\mathrm{o}-\mathrm{m}\mathrm{a}\mathrm{r}\mathrm{k}\mathrm{e}\mathrm{t}, \mathrm{T}\mathrm{o}\mathrm{b}\mathrm{i}\mathrm{n}'\mathrm{s} \mathrm{Q}, \mathrm{S}\mathrm{U}\mathrm{E} (\mathrm{w}\mathrm{i}\mathrm{n}\mathrm{s}\mathrm{o}\mathrm{r}\mathrm{i}\mathrm{z}\mathrm{e}\mathrm{d} \mathrm{a}\mathrm{t}
1/99\%), \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{F}\mathrm{o}\mathrm{g} \mathrm{i}\mathrm{n}\mathrm{d}\mathrm{e}\mathrm{x}, \mathrm{l}\mathrm{n}(\mathrm{W}\mathrm{o}\mathrm{r}\mathrm{d} \mathrm{C}\mathrm{o}\mathrm{u}\mathrm{n}\mathrm{t}), \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{t}\mathrm{h}\mathrm{e} fi\mathrm{n}\mathrm{a}\mathrm{n}\mathrm{c}\mathrm{i}\mathrm{a}\mathrm{l} \mathrm{j}\mathrm{a}\mathrm{r}\mathrm{g}\mathrm{o}\mathrm{n}, \mathrm{n}\mathrm{u}\mathrm{m}\mathrm{b}\mathrm{e}\mathrm{r}\mathrm{s} \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{f}\mathrm{o}\mathrm{r}\mathrm{w}\mathrm{a}\mathrm{r}\mathrm{d}-\mathrm{l}\mathrm{o}\mathrm{o}\mathrm{k}\mathrm{i}\mathrm{n}\mathrm{g} \mathrm{l}\mathrm{a}\mathrm{n}\mathrm{g}\mathrm{u}\mathrm{a}\mathrm{g}\mathrm{e}
\mathrm{s}\mathrm{h}\mathrm{a}\mathrm{r}\mathrm{e}\mathrm{s} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{Q}\&\mathrm{A} \mathrm{t}\mathrm{e}\mathrm{x}\mathrm{t}, \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{a}\mathrm{v}\mathrm{e}\mathrm{r}\mathrm{a}\mathrm{g}\mathrm{e} \mathrm{p}\mathrm{a}\mathrm{i}\mathrm{r}\mathrm{w}\mathrm{i}\mathrm{s}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{s}\mathrm{i}\mathrm{n}\mathrm{e} \mathrm{s}\mathrm{i}\mathrm{m}\mathrm{i}\mathrm{l}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{y} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{n} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}\mathrm{s}' \mathrm{j}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{i}fi\mathrm{c}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s}. \mathrm{A}\mathrm{l}\mathrm{l}
\mathrm{c}\mathrm{o}\mathrm{l}\mathrm{u}\mathrm{m}\mathrm{n}\mathrm{s} \mathrm{i}\mathrm{n}\mathrm{c}\mathrm{l}\mathrm{u}\mathrm{d}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} fi\mathrm{x}\mathrm{e}\mathrm{d} \mathrm{e}ff\mathrm{e}\mathrm{c}\mathrm{t}\mathrm{s}; \mathrm{c}\mathrm{o}\mathrm{l}\mathrm{u}\mathrm{m}\mathrm{n}\mathrm{s} (2)--(4) \mathrm{a}\mathrm{d}\mathrm{d} \mathrm{i}\mathrm{n}\mathrm{d}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{y} (\mathrm{o}\mathrm{n}\mathrm{e}-\mathrm{d}\mathrm{i}\mathrm{g}\mathrm{i}\mathrm{t} \mathrm{S}\mathrm{I}\mathrm{C} \mathrm{d}\mathrm{i}\mathrm{v}\mathrm{i}\mathrm{s}\mathrm{i}\mathrm{o}\mathrm{n}, \mathrm{n}\mathrm{i}\mathrm{n}\mathrm{e} \mathrm{g}\mathrm{r}\mathrm{o}\mathrm{u}\mathrm{p}\mathrm{s})
\mathrm{a}\mathrm{n}\mathrm{d} \mathrm{q}\mathrm{u}\mathrm{a}\mathrm{r}\mathrm{t}\mathrm{e}\mathrm{r} fi\mathrm{x}\mathrm{e}\mathrm{d} \mathrm{e}ff\mathrm{e}\mathrm{c}\mathrm{t}\mathrm{s}. t-\mathrm{s}\mathrm{t}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{i}\mathrm{c}\mathrm{s} \mathrm{i}\mathrm{n} \mathrm{p}\mathrm{a}\mathrm{r}\mathrm{e}\mathrm{n}\mathrm{t}\mathrm{h}\mathrm{e}\mathrm{s}\mathrm{e}\mathrm{s}, \mathrm{S}\mathrm{E} \mathrm{c}\mathrm{l}\mathrm{u}\mathrm{s}\mathrm{t}\mathrm{e}\mathrm{r}\mathrm{e}\mathrm{d} \mathrm{b}\mathrm{y} fi\mathrm{r}\mathrm{m} (497 fi\mathrm{r}\mathrm{m}\mathrm{s}). \ast p< 0.10; \ast \ast p< 0.05;
\ast \ast \ast p<0.01.
15

D Self-Reported Confidence
Each model reports a confidence level (0--1) with every score. Panel (a) shows the pooled
distribution: confidence is tightly clustered---about 30\% of all scores carry a confidence of
exactly 0.80, more than four-fifths lie between 0.70 and 0.95, and provider medians range
from 0.80 to 0.90---so the field carries limited cross-sectional information. Panel (b) compares
inter-provider agreement on all calls with agreement on the subset of calls wherebothmodels
in a pair report confidence at or above their own median for that construct---a loose, provider-
relative cut. Even this mild form of confidence screening does not improve agreement: across
the eleven constructs for which the conditional correlations are computable, the mean pairwise
Spearman correlation falls from 0.52 to 0.48, and no construct improves meaningfully. For
climate risk and political risk the high-confidence subsample is degenerate---models are most
confident precisely on calls where they assign the construct a score of zero---so almost no
provider pair retains any score variation. The decline is monotone in the strictness of the
cut: a fixed threshold of 0.8, under which all thirteen constructs remain computable, yields a
mean of 0.46; requiring confidence strictly above each provider's own median yields 0.35; and
a top-quartile cut yields 0.33 over the six constructs that remain computable. Consistent
with this, a model's confidence is essentially uninformative about its own deviation from the
seven-model consensus (mean Spearman correlation of  - 0.08 across provider--construct cells).
Self-reported confidence therefore does not identify a subset of calls on which LLM-based
measures can be trusted to agree, no matter where the threshold is drawn.
16

Figure OA.D.1:\mathrm{S}\mathrm{e}\mathrm{l}\mathrm{f}-\mathrm{r}\mathrm{e}\mathrm{p}\mathrm{o}\mathrm{r}\mathrm{t}\mathrm{e}\mathrm{d} \mathrm{c}\mathrm{o}\mathrm{n}fi\mathrm{d}\mathrm{e}\mathrm{n}\mathrm{c}\mathrm{e}: \mathrm{d}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{i}\mathrm{b}\mathrm{u}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{d}\mathrm{i}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{a}\mathrm{l} \mathrm{a}\mathrm{g}\mathrm{r}\mathrm{e}\mathrm{e}\mathrm{m}\mathrm{e}\mathrm{n}\mathrm{t}. \mathrm{P}\mathrm{a}\mathrm{n}\mathrm{e}\mathrm{l} (\mathrm{a}):
\mathrm{p}\mathrm{o}\mathrm{o}\mathrm{l}\mathrm{e}\mathrm{d} \mathrm{d}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{i}\mathrm{b}\mathrm{u}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n} \mathrm{o}\mathrm{f} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{n}fi\mathrm{d}\mathrm{e}\mathrm{n}\mathrm{c}\mathrm{e} fi\mathrm{e}\mathrm{l}\mathrm{d} \mathrm{a}\mathrm{c}\mathrm{r}\mathrm{o}\mathrm{s}\mathrm{s} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{n} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}\mathrm{s} \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{t}\mathrm{h}\mathrm{i}\mathrm{r}\mathrm{t}\mathrm{e}\mathrm{e}\mathrm{n} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t}\mathrm{s} (\mathrm{a} \mathrm{s}\mathrm{i}\mathrm{n}\mathrm{g}\mathrm{l}\mathrm{e}
\mathrm{i}\mathrm{n}\mathrm{v}\mathrm{a}\mathrm{l}\mathrm{i}\mathrm{d} \mathrm{r}\mathrm{e}\mathrm{s}\mathrm{p}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{e} \mathrm{w}\mathrm{i}\mathrm{t}\mathrm{h} \mathrm{c}\mathrm{o}\mathrm{n}fi\mathrm{d}\mathrm{e}\mathrm{n}\mathrm{c}\mathrm{e} > 1 \mathrm{i}\mathrm{s} \mathrm{e}\mathrm{x}\mathrm{c}\mathrm{l}\mathrm{u}\mathrm{d}\mathrm{e}\mathrm{d}). \mathrm{P}\mathrm{a}\mathrm{n}\mathrm{e}\mathrm{l} (\mathrm{b}): \mathrm{m}\mathrm{e}\mathrm{a}\mathrm{n} \mathrm{p}\mathrm{a}\mathrm{i}\mathrm{r}\mathrm{w}\mathrm{i}\mathrm{s}\mathrm{e} \mathrm{S}\mathrm{p}\mathrm{e}\mathrm{a}\mathrm{r}\mathrm{m}\mathrm{a}\mathrm{n} \mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}
\mathrm{o}\mathrm{f} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e}\mathrm{s} \mathrm{p}\mathrm{e}\mathrm{r} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t}, \mathrm{u}\mathrm{s}\mathrm{i}\mathrm{n}\mathrm{g} \mathrm{a}\mathrm{l}\mathrm{l} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l}\mathrm{s} (\mathrm{g}\mathrm{r}\mathrm{a}\mathrm{y}) \mathrm{v}\mathrm{e}\mathrm{r}\mathrm{s}\mathrm{u}\mathrm{s} \mathrm{o}\mathrm{n}\mathrm{l}\mathrm{y} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l}\mathrm{s} \mathrm{w}\mathrm{h}\mathrm{e}\mathrm{r}\mathrm{e} \mathrm{b}\mathrm{o}\mathrm{t}\mathrm{h} \mathrm{m}\mathrm{o}\mathrm{d}\mathrm{e}\mathrm{l}\mathrm{s} \mathrm{o}\mathrm{f} \mathrm{a} \mathrm{p}\mathrm{a}\mathrm{i}\mathrm{r} \mathrm{r}\mathrm{e}\mathrm{p}\mathrm{o}\mathrm{r}\mathrm{t}
\mathrm{c}\mathrm{o}\mathrm{n}fi\mathrm{d}\mathrm{e}\mathrm{n}\mathrm{c}\mathrm{e} \mathrm{a}\mathrm{t} \mathrm{o}\mathrm{r} \mathrm{a}\mathrm{b}\mathrm{o}\mathrm{v}\mathrm{e} \mathrm{t}\mathrm{h}\mathrm{e}\mathrm{i}\mathrm{r} \mathrm{o}\mathrm{w}\mathrm{n} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}--\mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t} \mathrm{m}\mathrm{e}\mathrm{d}\mathrm{i}\mathrm{a}\mathrm{n} (\mathrm{r}\mathrm{e}\mathrm{d}); ``\mathrm{d}\mathrm{e}\mathrm{g}\mathrm{e}\mathrm{n}\mathrm{e}\mathrm{r}\mathrm{a}\mathrm{t}\mathrm{e}"" \mathrm{m}\mathrm{a}\mathrm{r}\mathrm{k}\mathrm{s} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t}\mathrm{s}
\mathrm{w}\mathrm{h}\mathrm{e}\mathrm{r}\mathrm{e} \mathrm{n}\mathrm{e}\mathrm{a}\mathrm{r}\mathrm{l}\mathrm{y} \mathrm{a}\mathrm{l}\mathrm{l} \mathrm{h}\mathrm{i}\mathrm{g}\mathrm{h}-\mathrm{c}\mathrm{o}\mathrm{n}fi\mathrm{d}\mathrm{e}\mathrm{n}\mathrm{c}\mathrm{e} \mathrm{p}\mathrm{a}\mathrm{i}\mathrm{r}\mathrm{s} \mathrm{l}\mathrm{a}\mathrm{c}\mathrm{k} \mathrm{s}\mathrm{c}\mathrm{o}\mathrm{r}\mathrm{e} \mathrm{v}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}. \mathrm{S}\mathrm{t}\mathrm{r}\mathrm{i}\mathrm{c}\mathrm{t}\mathrm{e}\mathrm{r} \mathrm{d}\mathrm{e}fi\mathrm{n}\mathrm{i}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s} \mathrm{o}\mathrm{f} \mathrm{h}\mathrm{i}\mathrm{g}\mathrm{h} \mathrm{c}\mathrm{o}\mathrm{n}fi\mathrm{d}\mathrm{e}\mathrm{n}\mathrm{c}\mathrm{e}
\mathrm{l}\mathrm{o}\mathrm{w}\mathrm{e}\mathrm{r} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{d}\mathrm{i}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{a}\mathrm{l} \mathrm{c}\mathrm{o}\mathrm{r}\mathrm{r}\mathrm{e}\mathrm{l}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{o}\mathrm{n}\mathrm{s} \mathrm{f}\mathrm{u}\mathrm{r}\mathrm{t}\mathrm{h}\mathrm{e}\mathrm{r}.
17

E LLM Models
Table OA.E.1 lists the seven large language models used to score every earnings-call text,
together with the exact model identifier and the route through which each model was queried.
The set is held fixed across all calls and all constructs, so any disagreement among the models
reflects the models themselves rather than differences in coverage. Six of the seven models are
accessed through the OpenRouter gateway using an OpenAI-compatible interface; OpenAI's
GPT is queried directly through the native OpenAI API. All models are prompted identically
(see Appendix F) with the same decoding settings.
Table OA.E.1:\mathrm{L}\mathrm{a}\mathrm{r}\mathrm{g}\mathrm{e} \mathrm{l}\mathrm{a}\mathrm{n}\mathrm{g}\mathrm{u}\mathrm{a}\mathrm{g}\mathrm{e} \mathrm{m}\mathrm{o}\mathrm{d}\mathrm{e}\mathrm{l}\mathrm{s} \mathrm{u}\mathrm{s}\mathrm{e}\mathrm{d} \mathrm{i}\mathrm{n} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{a}\mathrm{n}\mathrm{a}\mathrm{l}\mathrm{y}\mathrm{s}\mathrm{i}\mathrm{s}.
\mathrm{P}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r} \mathrm{D}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{l}\mathrm{o}\mathrm{p}\mathrm{e}\mathrm{r} \mathrm{F}\mathrm{a}\mathrm{m}\mathrm{i}\mathrm{l}\mathrm{y} \mathrm{M}\mathrm{o}\mathrm{d}\mathrm{e}\mathrm{l} \mathrm{i}\mathrm{d}\mathrm{e}\mathrm{n}\mathrm{t}\mathrm{i}fi\mathrm{e}\mathrm{r} \mathrm{A}\mathrm{c}\mathrm{c}\mathrm{e}\mathrm{s}\mathrm{s} \mathrm{r}\mathrm{o}\mathrm{u}\mathrm{t}\mathrm{e}
\mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{A}\mathrm{I} \mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{A}\mathrm{I} \mathrm{G}\mathrm{P}\mathrm{T}gpt-4o-mini\mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{A}\mathrm{I} \mathrm{A}\mathrm{P}\mathrm{I} (\mathrm{n}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{v}\mathrm{e} \mathrm{S}\mathrm{D}\mathrm{K})
\mathrm{A}\mathrm{n}\mathrm{t}\mathrm{h}\mathrm{r}\mathrm{o}\mathrm{p}\mathrm{i}\mathrm{c} \mathrm{A}\mathrm{n}\mathrm{t}\mathrm{h}\mathrm{r}\mathrm{o}\mathrm{p}\mathrm{i}\mathrm{c} \mathrm{C}\mathrm{l}\mathrm{a}\mathrm{u}\mathrm{d}\mathrm{e}anthropic/claude-3-haiku\mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{R}\mathrm{o}\mathrm{u}\mathrm{t}\mathrm{e}\mathrm{r}
\mathrm{G}\mathrm{e}\mathrm{m}\mathrm{i}\mathrm{n}\mathrm{i} \mathrm{G}\mathrm{o}\mathrm{o}\mathrm{g}\mathrm{l}\mathrm{e} \mathrm{G}\mathrm{e}\mathrm{m}\mathrm{i}\mathrm{n}\mathrm{i}google/gemini-2.5-flash-lite\mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{R}\mathrm{o}\mathrm{u}\mathrm{t}\mathrm{e}\mathrm{r}
\mathrm{L}\mathrm{l}\mathrm{a}\mathrm{m}\mathrm{a} \mathrm{M}\mathrm{e}\mathrm{t}\mathrm{a} \mathrm{L}\mathrm{l}\mathrm{a}\mathrm{m}\mathrm{a}meta-llama/llama-3.3-70b-instruct\mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{R}\mathrm{o}\mathrm{u}\mathrm{t}\mathrm{e}\mathrm{r}
\mathrm{M}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{l} \mathrm{M}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{l} \mathrm{M}\mathrm{i}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{a}\mathrm{l}mistralai/mistral-small-24b-instruct-2501\mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{R}\mathrm{o}\mathrm{u}\mathrm{t}\mathrm{e}\mathrm{r}
\mathrm{D}\mathrm{e}\mathrm{e}\mathrm{p}\mathrm{S}\mathrm{e}\mathrm{e}\mathrm{k} \mathrm{D}\mathrm{e}\mathrm{e}\mathrm{p}\mathrm{S}\mathrm{e}\mathrm{e}\mathrm{k} \mathrm{D}\mathrm{e}\mathrm{e}\mathrm{p}\mathrm{S}\mathrm{e}\mathrm{e}\mathrm{k}deepseek/deepseek-chat\mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{R}\mathrm{o}\mathrm{u}\mathrm{t}\mathrm{e}\mathrm{r}
\mathrm{Q}\mathrm{w}\mathrm{e}\mathrm{n} \mathrm{A}\mathrm{l}\mathrm{i}\mathrm{b}\mathrm{a}\mathrm{b}\mathrm{a} \mathrm{Q}\mathrm{w}\mathrm{e}\mathrm{n}qwen/qwen-2.5-7b-instruct\mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{R}\mathrm{o}\mathrm{u}\mathrm{t}\mathrm{e}\mathrm{r}
Notes.``\mathrm{P}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}"" \mathrm{i}\mathrm{s} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{h}\mathrm{o}\mathrm{r}\mathrm{t} \mathrm{l}\mathrm{a}\mathrm{b}\mathrm{e}\mathrm{l} \mathrm{u}\mathrm{s}\mathrm{e}\mathrm{d} \mathrm{t}\mathrm{o} \mathrm{i}\mathrm{d}\mathrm{e}\mathrm{n}\mathrm{t}\mathrm{i}\mathrm{f}\mathrm{y} \mathrm{e}\mathrm{a}\mathrm{c}\mathrm{h} \mathrm{m}\mathrm{o}\mathrm{d}\mathrm{e}\mathrm{l} \mathrm{t}\mathrm{h}\mathrm{r}\mathrm{o}\mathrm{u}\mathrm{g}\mathrm{h}\mathrm{o}\mathrm{u}\mathrm{t} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{t}\mathrm{a}\mathrm{b}\mathrm{l}\mathrm{e}\mathrm{s} \mathrm{a}\mathrm{n}\mathrm{d} fi\mathrm{g}\mathrm{u}\mathrm{r}\mathrm{e}\mathrm{s}.
``\mathrm{M}\mathrm{o}\mathrm{d}\mathrm{e}\mathrm{l} \mathrm{i}\mathrm{d}\mathrm{e}\mathrm{n}\mathrm{t}\mathrm{i}fi\mathrm{e}\mathrm{r}"" \mathrm{i}\mathrm{s} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{e}\mathrm{x}\mathrm{a}\mathrm{c}\mathrm{t} \mathrm{s}\mathrm{t}\mathrm{r}\mathrm{i}\mathrm{n}\mathrm{g} \mathrm{p}\mathrm{a}\mathrm{s}\mathrm{s}\mathrm{e}\mathrm{d} \mathrm{t}\mathrm{o} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{A}\mathrm{P}\mathrm{I}. \mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{R}\mathrm{o}\mathrm{u}\mathrm{t}\mathrm{e}\mathrm{r} ( openrouter.ai) \mathrm{i}\mathrm{s} \mathrm{a}\mathrm{n} \mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{A}\mathrm{I}-
\mathrm{c}\mathrm{o}\mathrm{m}\mathrm{p}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{b}\mathrm{l}\mathrm{e} \mathrm{g}\mathrm{a}\mathrm{t}\mathrm{e}\mathrm{w}\mathrm{a}\mathrm{y} \mathrm{t}\mathrm{h}\mathrm{a}\mathrm{t} \mathrm{r}\mathrm{o}\mathrm{u}\mathrm{t}\mathrm{e}\mathrm{s} \mathrm{r}\mathrm{e}\mathrm{q}\mathrm{u}\mathrm{e}\mathrm{s}\mathrm{t}\mathrm{s} \mathrm{t}\mathrm{o} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{u}\mathrm{n}\mathrm{d}\mathrm{e}\mathrm{r}\mathrm{l}\mathrm{y}\mathrm{i}\mathrm{n}\mathrm{g} \mathrm{m}\mathrm{o}\mathrm{d}\mathrm{e}\mathrm{l} \mathrm{p}\mathrm{r}\mathrm{o}\mathrm{v}\mathrm{i}\mathrm{d}\mathrm{e}\mathrm{r}; \mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{A}\mathrm{I}'\mathrm{s} \mathrm{G}\mathrm{P}\mathrm{T} \mathrm{i}\mathrm{s} \mathrm{q}\mathrm{u}\mathrm{e}\mathrm{r}\mathrm{i}\mathrm{e}\mathrm{d}
\mathrm{d}\mathrm{i}\mathrm{r}\mathrm{e}\mathrm{c}\mathrm{t}\mathrm{l}\mathrm{y} \mathrm{t}\mathrm{h}\mathrm{r}\mathrm{o}\mathrm{u}\mathrm{g}\mathrm{h} \mathrm{t}\mathrm{h}\mathrm{e} \mathrm{n}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{v}\mathrm{e} \mathrm{O}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{A}\mathrm{I} \mathrm{S}\mathrm{D}\mathrm{K}. \mathrm{T}\mathrm{h}\mathrm{e} \mathrm{s}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{n} \mathrm{m}\mathrm{o}\mathrm{d}\mathrm{e}\mathrm{l}\mathrm{s} \mathrm{c}\mathrm{o}\mathrm{m}\mathrm{e} \mathrm{f}\mathrm{r}\mathrm{o}\mathrm{m} \mathrm{s}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{n} \mathrm{i}\mathrm{n}\mathrm{d}\mathrm{e}\mathrm{p}\mathrm{e}\mathrm{n}\mathrm{d}\mathrm{e}\mathrm{n}\mathrm{t} \mathrm{d}\mathrm{e}\mathrm{v}\mathrm{e}\mathrm{l}\mathrm{o}\mathrm{p}\mathrm{e}\mathrm{r}\mathrm{s}
\mathrm{a}\mathrm{n}\mathrm{d} \mathrm{a}\mathrm{r}\mathrm{e} \mathrm{h}\mathrm{e}\mathrm{l}\mathrm{d} fi\mathrm{x}\mathrm{e}\mathrm{d} \mathrm{a}\mathrm{c}\mathrm{r}\mathrm{o}\mathrm{s}\mathrm{s} \mathrm{e}\mathrm{v}\mathrm{e}\mathrm{r}\mathrm{y} \mathrm{e}\mathrm{a}\mathrm{r}\mathrm{n}\mathrm{i}\mathrm{n}\mathrm{g}\mathrm{s} \mathrm{c}\mathrm{a}\mathrm{l}\mathrm{l} \mathrm{a}\mathrm{n}\mathrm{d} \mathrm{e}\mathrm{v}\mathrm{e}\mathrm{r}\mathrm{y} \mathrm{t}\mathrm{e}\mathrm{x}\mathrm{t}\mathrm{u}\mathrm{a}\mathrm{l} \mathrm{c}\mathrm{o}\mathrm{n}\mathrm{s}\mathrm{t}\mathrm{r}\mathrm{u}\mathrm{c}\mathrm{t}.
18

F Prompt Templates
The following templates were used verbatim for all LLM providers. The placeholder \{ text\}
is replaced with the earnings-call transcript segment at inference time.
F.1 Sentiment
You are an analyst tasked with quantifying sentiment from a passage of text.
Important constraints:
- Base your assessment exclusively on the text provided below.
- Do not use any external knowledge, background information, or assumptions
about the firm, industry, economy, or time period.
- Do not infer intent beyond what is explicitly stated in the text.
Sentiment Definition:
- Sentiment captures the overall positivity vs. negativity expressed in the
text regarding firm performance, prospects, or conditions.
Sentiment Scale:
- Sentiment Score: -1.00 (very negative) to +1.00 (very positive),
where 0.00 is neutral.
Confidence definition:
- Confidence reflects how certain you are that the numeric sentiment score
accurately captures the overall positivity versus negativity expressed in
the provided text.
- Confidence is not about how extreme the sentiment is, only about the
certainty of the measurement given the text.
19

JSON Output format (strict):
- Sentiment Score: !`number?`
- Confidence: !`number between 0 and 1?`
- Justification: !`1-2 sentences citing specific wording from the text?`
Text to analyze:
--text\H
F.2 Uncertainty
You are an analyst tasked with quantifying uncertainty about the firmfls
future outlook from a passage of text.
Important constraints:
- Use only the text provided below.
- Do not incorporate any external data, historical outcomes, or industry
knowledge.
Uncertainty Score Definition (critical):
- Uncertainty reflects the degree of ambiguity, lack of precision, hedging,
conditional language, or unresolved outcomes regarding the firmfls future.
- This is NOT about whether expectations and the outlook are positive or
negative.
Uncertainty Score Scale:
- 0.00 (very certain / precise outlook) to 1.00
(very uncertain / ambiguous outlook).
20

Confidence definition:
- Confidence reflects how certain you are that the numeric uncertainty score
accurately captures the degree of uncertainty about the firmfls future
outlook as expressed in the provided text.
- Confidence is not about whether expectations are positive or negative,
only about the certainty of measuring uncertainty given the text.
JSON Output format (strict):
- Uncertainty Score: !`number?`
- Confidence: !`number between 0 and 1?`
- Justification: !`1-2 sentences citing specific wording from the text?`
Text to analyze:
--text\H
F.3 Climate Risk
You are an analyst tasked with quantifying climate risk exposure as expressed
in a passage of text.
Important constraints:
- Rely only on the text provided below.
- Do not use external information about climate change, regulation,
geography, or the firm.
Climate risk exposure Definition:
- Climate risk exposure captures the extent to which the text indicates
21

exposure to climate-related risks, including physical risks (e.g., extreme
weather), transition risks (e.g., regulation, carbon costs), or
climate-related operational disruptions.
- The measure reflects presence and salience in the text, not whether the
firm is managing the risk well.
Climate risk exposure Scale:
- Climate Risk Exposure Score: 0.00 (no climate risk mentioned) to 1.00
(climate risk is a major, explicit concern).
Confidence definition:
- Confidence reflects how certain you are that the numeric score accurately
captures climate risk exposure as expressed in the provided text.
- Confidence is not about how large or severe the climate risk is, only
about the certainty of the measurement given the text.
JSON Output format (strict):
- Climate Risk Exposure Score: !`number?`
- Confidence: !`number between 0 and 1?`
- Justification: !`1-2 sentences citing specific wording from the text?`
Text to analyze:
--text\H
F.4 Management Clarity
You are an analyst tasked with quantifying management clarity in responses
from a passage of text.
22

Important constraints:
- Base your judgment only on the provided text.
- Do not infer intent or competence beyond what is observable in the wording.
- Do not use external benchmarks or expectations.
Management clarity Definition:
- Management clarity reflects how clear, direct, specific, and internally
consistent the responses are.
- High clarity: concrete answers, specific explanations, minimal hedging,
clear structure.
- Low clarity: vague language, evasive answers, excessive qualifiers, or
failure to directly address issues.
Management clarity Scale:
- 0.00 (very unclear / evasive) to 1.00 (very clear and direct).
Confidence definition:
- Confidence reflects how certain you are that the numeric score accurately
captures management clarity as expressed in the provided text.
- Confidence is not about how extreme the clarity/lack of clarity is, only
about the certainty of the measurement given the text.
JSON Output format (strict):
- Management Clarity Score: !`number?`
- Confidence: !`number between 0 and 1?`
- Justification: !`1-2 sentences citing specific wording from the text?`
Text to analyze:
23

--text\H
F.5 Political Risk
You are an analyst tasked with quantifying political risk exposure as
expressed in a passage of text.
Important constraints:
- Rely only on the text provided below.
- Do not use external knowledge about politics, countries, regulations, or
current events.
- If the text contains no explicit reference to political risk (e.g.,
elections, sanctions, tariffs, trade restrictions, government instability,
policy uncertainty, geopolitical conflict, nationalization, government
shutdowns), assign a score of exactly 0.00.
Political risk exposure Definition:
- Political risk exposure captures the extent to which the text indicates
exposure to political or geopolitical forces that could affect the firmfls
performance or outlook.
- The measure reflects presence and salience in the text, not whether the
risk is managed well.
Political risk exposure Scale:
- Political Risk Exposure Score: 0.00 (no political risk mentioned) to 1.00
(political risk is a major, explicit concern).
Confidence definition:
24

- Confidence reflects how certain you are that the numeric score accurately
captures political risk exposure as expressed in the provided text.
Output format (strict):
- Political Risk Exposure Score: !`number?`
- Confidence: !`number between 0 and 1?`
- Justification: !`1-2 sentences citing specific wording from the text?`
Text to analyze:
--text\H
F.6 Corporate Culture
You are an analyst tasked with quantifying corporate culture signals from
a passage of text.
Important constraints:
- Use only the text provided below.
- Do not use external knowledge about the firm or industry.
- Score only what is explicitly signaled in the wording (values, norms,
behaviors, incentives).
Corporate culture Definition:
- Corporate culture reflects the norms and values signaled by managementfls
language about how the organization behaves and what it prioritizes.
Dimensions (each scored 0.00 to 1.00):
- Innovation: emphasis on experimentation, learning, R\&D, speed,
25

new products/processes.
- Integrity: emphasis on ethics, compliance, transparency, doing the
right thing.
- Quality: emphasis on reliability, craftsmanship, excellence, safety,
customer outcomes.
- Respect: emphasis on people, inclusion, wellbeing, fair treatment,
listening.
- Teamwork: emphasis on collaboration, shared ownership, cross-functional
alignment.
Overall Culture Score:
- Overall Corporate Culture Score (0.00 to 1.00) summarizes the strength
and clarity of culture signals across dimensions.
Confidence definition:
- Confidence reflects how certain you are that the scores accurately reflect
culture signals in the text (not whether the culture is ""good"").
Output format (strict):
- Innovation Score: !`number?`
- Integrity Score: !`number?`
- Quality Score: !`number?`
- Respect Score: !`number?`
- Teamwork Score: !`number?`
- Overall Corporate Culture Score: !`number?`
- Confidence: !`number between 0 and 1?`
- Justification: !`2-3 sentences citing specific wording from the text?`
Text to analyze:
26

--text\H
F.7 Specificity Ratio
You are an analyst tasked with measuring the specificity of a passage of
text.
Important constraints:
- Base your assessment exclusively on the text provided below.
- Do not use any external knowledge or assumptions.
Definition of Specificity:
- Specificity refers to the extent to which the text contains concrete,
verifiable, and precise information, as opposed to general or vague
statements.
- In this task, ""specific words"" are words or phrases that belong to one
of the following seven categories:
1. Person names
2. Geographic locations
3. Organizations (including companies)
4. Percentages
5. Monetary values
6. Dates
7. Times or durations
Counting rules:
- Count as ""specific"" only those words or phrases that clearly fall into
one of the seven categories listed above.
- Count each named entity as one unit, regardless of the number of words
(e.g., ""Apple Inc."" = 1).
27

- Count each numeric expression as one unit (e.g., ""5\%"", ""\$10 million"",
""2024"", ""three years"" = 1 each).
- Count only instances explicitly present in the text.
Definitions for calculation:
- Number of Specific Words = total number of words or expressions belonging
to the seven categories above.
- Total Words = total number of words in the text.
Specificity Score:
- Specificity Score is a number between 0.00 and 1.00, defined as:
- Specificity Score = (Number of Specific Words) / (Total Words)
Confidence definition:
- Confidence reflects how certain you are that the numeric scores accurately
capture the specificity of the provided text.
- Confidence is not about whether specificity is high or low, but about how
certain you are in applying the rules consistently.
Output format (strict):
- Number of Specific Words: !`integer?`
- Specificity Score: !`number between 0 and 1?`
- Confidence: !`number between 0 and 1?`
- Justification: !`list all instances of specific content you counted,
separated by commas; if none, write ""None""?`
Text to analyze:
28

--text\H
F.8 Specificity
You are an analyst tasked with assessing the specificity of a passage of
text.
Important constraints:
- Base your assessment exclusively on the text provided below.
- Do not use any external knowledge or assumptions.
Definition of Specificity:
- Specificity refers to the extent to which the text contains concrete,
verifiable, and precise information, as opposed to general or vague
statements.
- In this context, specificity is driven by the presence of:
- Person names
- Geographic locations
- Organizations (including companies)
- Percentages
- Monetary values
- Dates
- Times or durations
Guidance:
- Texts with many such elements should receive higher specificity scores.
- Texts that are general, abstract, or lack concrete details should receive
lower scores.
- Base your assessment on the overall prevalence of these elements in the
text.
29

Specificity Score Scale:
- Specificity Score: 0.00 (very vague / no concrete details) to 1.00
(highly specific / dense with concrete details).
Confidence definition:
- Confidence reflects how certain you are that the numeric score accurately
captures the specificity of the provided text.
- Confidence is not about whether specificity is high or low, but about how
certain you are in judging the prevalence of specific elements from the
text alone.
Output format (strict):
- Specificity Score: !`number between 0 and 1?`
- Confidence: !`number between 0 and 1?`
- Justification: !`1-2 sentences explaining what types of specific elements
were present or missing?`
Text to analyze:
--text\H
30
