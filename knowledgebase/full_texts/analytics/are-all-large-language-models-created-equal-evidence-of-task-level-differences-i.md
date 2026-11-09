---
title: Are All Large Language Models Created Equal? Evidence of Task-Level Differences in Generation X
  E-Commerce Marketing Analytics
url: https://doi.org/10.24018/ejece.2026.10.3.70459
category: analytics
subcategory: framework
date: 2026-06
venue: European Journal of Electrical Engineering and Computer Science
authors:
- Kandice Brawley-Walker
- Yanzhen Qu
source: openalex-oa
pdf_url: https://eu-opensci.org/index.php/ejece/article/download/70459/14531
pages: 6
chars: 27657
fetched_at: '2026-11-08T17:34:55+00:00'
kb_version: 1
---

# Are All Large Language Models Created Equal? Evidence of Task-Level Differences in Generation X E-Commerce Marketing Analytics

SA Copyright: © 2026 Brawley-Walker and Qu. This work is under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
European Journal of Electrical Engineering and Computer Science
Vol 10 | Issue 3 | June 2026
ISSN 2736-5751
RESEARCH ARTICLE
Are All Large Language Models Created Equal?
Evidence of Task-Level Differences in Generation
X E-Commerce Marketing Analytics
Kandice Brawley-Walker and Y anzhen Qu*
ABSTRACT
With GPT-4, Claude, and Gemini each commanding premium enterprise
pricing and distinct vendor claims, the question of which large language
model (LLM) best serves marketing analytics practitioners is increasingly
consequential. This article reports findings from a quantitative comparative
study evaluating these three models on five analytical tasks applied to
Generation X e-commerce customer engagement data (n = 385). Across
precision, recall, F1-score, and AUC, no statistically significant aggregate
differences emerged among the three models, supporting retention of the
null hypothesis. Yet task-level distinctions are real and actionable: GPT-4
delivers the highest output stability, Gemini excels in processing speed
and clustering quality, and Claude produces the strongest psychographic
segmentation signal. Cost analysis reveals meaningful API pricing
differences of $10–$120 per million output tokens across these platforms,
making model-task alignment a budget decision as well as a performance
one. The findings offer marketing teams an evidence-based framework for
choosing LLMs by task priority rather than brand reputation.
Keywords: Comparative analysis, generation X, large language models,
marketing analytics.
Submitted: June 01, 2026
Published: June 27, 2026
10.24018/ejece.2026.10.3.70459
Colorado Technical University, United
States.
*Corresponding Author:
e-mail: yqu@coloradotech.edu
1. Introduction
The artificial intelligence marketplace is crowded with
competing claims. OpenAI has positioned GPT-4 as the
gold standard for analytical reasoning. Anthropic markets
Claude based on nuance and safety . Google promotes
Gemini at an enterprise-scale speed. For marketing pro-
fessionals tasked with building data-driven campaigns, this
raises a practical question: Does the choice of platform
materially affect analytical outcomes?
The answer, based on an empirical study using a strat-
ified sample of 385 Generation X e-commerce records,
is simultaneously yes and no, and that distinction carries
real consequences for organizations allocating AI budgets.
Generation X consumers, born between 1965 and 1980,
command an estimated $2.4 trillion in annual U.S. pur-
chasing power [1]. Despite this, brands disproportionately
underinvest in Generation X-targeted digital marketing
relative to their purchasing power [2], [3]. This study aimed
to determine whether LLMs could close this gap and, more
specifically, whether the three leading commercial models
are interchangeable or meaningfully different when applied
to this analytical challenge.
1.1. Related Works
1.1.1. Large Language Models in Marketing Analytics
The deployment of LLMs in marketing has grown sub-
stantially as organizations seek to automate and enhance
customer insight generation. Mahiet al. demonstrated that
LLMs enable more personalized customer engagement
and targeted campaign design, which outpaced conven-
tional rule-based analytics [ 4]. Cherenkov et al .s h o w e d
that LLMs facilitate sentiment analysis and trend pre-
diction, which are essential for crafting better customer
experiences across consumer data domains [ 5]. Sridharan
and Rao demonstrated that machine learning approaches
applied to social media behavioral data produce senti-
ment signals that outperform conventional demographic
segmentation [ 6], while Ugbaja et al . documented how
AI-driven frameworks transform raw customer data
into actionable segmentation strategies with measurable
improvements in campaign-targeting efficiency [ 7].
V ol 10 | Issue 3 | June 2026 26

Brawley-Walker and Qu Are All Large Language Models Created Equal? Evidence
GPT-4 offers enhanced logical reasoning and nuanced
outputs with documented strengths in iterative, multi-
step analytical tasks [ 8]. Claude is distinguished by its
extended context window and strong performance on
sophisticated reasoning tasks involving complex datasets
[8]. Gemini features a multimodal architecture optimized
for the simultaneous processing of diverse data types,
with demonstrated advantages in speed and scalability [ 8].
Despite growing practitioner interest, Aghaei et al . called
for systematic, evidence-based frameworks to guide LLM
adoption [9], and Aghaei et al.[ 9] noted that most existing
evaluations focus on natural language generation quality
rather than quantitative analytical accuracy . Bolgovaet al.
confirmed that performance differences among leading
LLMs tend to be task-specific rather than globally consis-
tent, directly motivating the multi-task evaluation design
of this study [ 10].
1.1.2. Generation X as a Marketing Analytics Target
Generation X occupies a structurally underserved posi-
tion in the digital marketing analytics research. Despite
commanding $2.4 trillion in annual U.S. purchasing power
and comprising approximately 23% of the U.S. population
[1], this cohort receives disproportionately less analyt-
ical attention than Millennials or Baby Boomers [ 2],
[3]. Choudhary et al .[ 3] established that Generation X
customer journeys involve complex, multi-channel engage-
ment patterns that resist simplification using traditional
demographic proxies [3]. Choudhary et al.[ 3] identified e-
mail engagement as the most reliable behavioral activation
channel for Generation X, with direct implications for
how analysts should weigh engagement variables when
constructing LLM prompts [9]. Y adavet al. confirmed that
Generation X exhibits a preference for authenticity and
quality over novelty, which shapes how segmentation vari-
ables perform predictively [ 2], while Pongwe and Churk
(2024) demonstrated that targeted campaigns based on
segment-specific messaging can maximize ROI by allocat-
ing resources efficiently [ 11].
1.1.3. Machine Learning Approached to Customer
Segmentation
The methodological foundation for this study draws
on established machine learning techniques, including
logistic regression, random forest classification, Pearson
correlation, K-means clustering, and ANOV A, applied
through LLM interfaces rather than direct coding envi-
ronments. Hamid and Abdulazeez reviewed machine
learning applications for sentiment and behavioral clas-
sification, confirming that ensemble methods, such as
random forests, produce robust performance on imbal-
anced customer datasets when appropriate preprocessing
steps are applied [ 12]. Their review specifically flagged
class imbalance as a primary source of classification col-
lapse, a finding directly relevant to the random forest
results reported in this study .
K-means clustering has been widely validated for
behavioral segmentation tasks in e-commerce contexts. Sil-
houette score analysis, as employed in this study, provides
a model-agnostic quality metric for cluster cohesion that
enables a direct cross-model comparison [ 7], [13].
1.2. Problem. Purpose, Research Question and Hypot-
heses
Marketing analytics practitioners lack empirical evi-
dence for selecting GPT-4, Claude, or Gemini for
Generation X e-commerce applications. Vendor claims are
not grounded in independently verifiable comparative per-
formance data, and existing LLM benchmarks focus on
general reasoning rather than domain-specific marketing
analytics tasks.
1.2.1. Problem Statement
Organizations face financial and operational risks when
committing to premium LLM subscriptions for marketing
analytics without a task performance basis for selec-
tion because independently verified and domain-specific
comparative performance data for large language models
in marketing analytics, particularly for Generation X e-
commerce applications, are lacking.
1.2.2. Purpose Statement
This quantitative, comparative study aimed to evaluate
the analytical accuracy of three large language models,
GPT 4, Claude, and Gemini, in performing marketing
analytics tasks on e-commerce customer engagement data
for Generation X segments, as measured by precision,
recall, F1 score, and area under the curve.
1.2.3. Research Question
Do GPT 4, Claude, and Gemini produce statisti-
cally equivalent analytical accuracy on a standardized
Generation X e-commerce dataset across defined mar-
keting analytics tasks, and if equivalence is observed at
the aggregate level, what task-level differences inform
evidence-based LLM selection?
1.2.4. Hypotheses
H0: No statistically significant differences in analytical
accuracy (precision, recall, F1-score, AUC) exist among
GPT-4, Claude, and Gemini when applied to Generation
X e-commerce customer engagement data under standard-
ized analytical conditions.
H1: Statistically significant differences in analytical
accuracy exist among GPT-4, Claude, and Gemini when
applied to Generation X e-commerce customer engage-
ment data under standardized analytical conditions.
2. Methodology
2.1. Method
This study employed a quantitative comparative design
to evaluate the analytical performance of GPT-4, Claude,
and Gemini across five standardized marketing analyt-
ics tasks. All three LLMs processed an identical dataset
through identical standardized prompts, eliminating con-
founding variables. Each model operated under equivalent
conditions with no task-specific fine-tuning. Five analyti-
cal tasks were evaluated: (1) logistic regression for repeat
customer classification, (2) random forest classification
for premium membership prediction, (3) Pearson corre-
lation analysis, (4) K-Means behavioral clustering, and
V ol 10 | Issue 3 | June 2026 27

Are All Large Language Models Created Equal? Evidence Brawley-Walker and Qu
Fig. 1. Conceptual framework.
(5) repeated-measures ANOV A across five marketing seg-
mentation variables. Bootstrap confidence intervals were
computed from 1,000 iterations for all primary metrics.
Hypothesis-testing metrics were precision, recall, F1-score,
and AUC.
The conceptual framework is presented in Fig. 1.I t
begins with a dataset that includes customer demo-
graphic variables, engagement indicators, and transaction
attributes. This dataset was then used to drive each large
language model in the analysis. The model outputs were
subsequently evaluated across four dimensions: predictive
performance, clustering quality, statistical significance,
and interpretability . This allows the framework to connect
technical AI capabilities directly to measurable marketing
results.
2.2. Population and Sample
The study population comprised Generation X e-
commerce consumers (born between 1965 and 1980). The
dataset was drawn from a publicly available 10,000-record
Kaggle e-commerce customer engagement dataset, filtered
to 2,255 Generation X records, and stratified random-
sampled into 385 records. The analytical sample yielded
a mean customer age of 52.6 years and a mean customer
lifetime value (CL V) of $157.23. Email engagement (mean
= 0.42) outpaced social media engagement (mean = 0.35),
consistent with the prior literature [ 3]. The random forest
task introduced a class imbalance condition, with premium
membership holders representing 40.5% of the sample size.
2.3. Data Analysis
All three LLMs received identical prompts and data
inputs for the five analytical tasks. The outputs were eval-
uated against standardized reference metrics computed
using Python (scikit-learn). For the classification tasks,
precision, recall, weighted F1-score, and AUC were the
primary metrics. For the clustering task, the silhouette
score served as a quality measure. For the correlation
task, Pearson’s r coefficients were compared across mod-
els and against a reference calculation. For the ANOV A
task, F-statistics and p-values were evaluated for the five
marketing segmentation variables. Bootstrap resampling
(1,000 iterations) was applied to assess the output stability .
Statistical significance was evaluated at α = 0.05.
3. Application and Results
3.1. Results
No statistically significant differences in aggregate ana-
lytical accuracy were detected among GPT-4, Claude, and
Gemini under standardized conditions. The null hypothe-
sis is retained. All three models achieved AUC scores near
0.86 on the logistic regression task, weighted F1-scores
between 0.751 and 0.765, and produced identical Pearson
correlation coefficients for the two highest-signal variable
pairs (r = 0.705 and r = 0.693). However, aggregate equiv-
alence is not the same as identical performance. The study
surfaces four task-level distinctions with real practical
consequences. Fig. 2 illustrates the Logistic Regression for
repeat customer classification. Precision Recall and AUC
are equivalent across the 3 LLMs.
3.1.1. GPT-4: Output Stability Champion
GPT-4 produced the narrowest bootstrap confidence
interval across 1,000 resampling iterations (0.787–0.819),
indicating the most consistent and reproducible output
among the three models. For organizations running iter-
ative analytical workflows, monthly resegmentation, and
campaign-cycle recalibration, this stability advantage is
operationally significant. GPT-4 did, however, produce
a discrepant Pearson correlation estimate for the T otal
Purchases ↔ Repeat Customer variable pair (approxi-
mately 0.45–0.55 vs. the reference value of 0.355 reported
by Claude and Gemini), a localized hallucination in
quantitative reporting that underscores why multimodel
0.763 0.765
0.861
0.751 0.754
0.858
0.765 0.762
0.863
Precision Recall AUC
GPT-4 Claude Gemini
Fig. 2. Logistic regression performance repeat customer
classification (n = 385). Note: W eighted metrics were computed
across 1,000 bootstrap iterations. A UC= area under the ROC
curve.
V ol 10 | Issue 3 | June 2026 28

Brawley-Walker and Qu Are All Large Language Models Created Equal? Evidence
TABLE I: K-Means Clustering Quality and Win-Back Priority
Segment
Model Silhouette
GPT-4 0.1158
Claude 0.1160
Gemini ⋆ 0.1415
Note: Silhouette scores reflect the intra-cluster cohesion, with higher
values indicating superior cluster separation. ⋆ = highest silhouette
score. All three models unanimously identified the Lapsed/One-Time
Buyer cohort as the highest-priority win-back target .
verification protocols remain essential. Table I summa-
rizes the K-Means clustering quality metrics and win-back
priority segments across all three models.
3.1.2. Gemini: Speed and Segmentation Quality
Gemini completed logistic regression training in 0.010 s,
over 56 times faster than Claude at 0.560 s. On K-means
clustering, Gemini produced the highest silhouette score
(0.1415 vs. 0.1158 for GPT-4 and 0.1160 for Claude), indi-
cating superior intra-cluster cohesion. For teams running
high-volume, real-time customer segmentation at scale,
Gemini’s speed and clustering quality represent significant
operational advantages. The same efficiency advantage
appeared in random forest tasks, where Gemini trained in
0.649 s versus 3.191 s for GPT-4 and 3.450 s for Claude.
3.1.3. Claude: Psychographic Segmentation Edge
ANOV A testing across five marketing segmentation
variables found that satisfaction by gender was the
only variable that produced statistically significant results
across all three models. Claude detected this signal most
strongly (p= 0.0202), followed by GPT-4 (p= 0.0265) and
Gemini (p = 0.0317). Critically, conventional demographic
proxies’ income level, geographic region, and mobile app
usage yielded no statistically significant group differen-
tiation across any of the models. This finding means
psychographic variables such as gender-linked satisfaction
are more powerful marketing levers than demographics for
Generation X. Claude’s sensitivity to this dimension makes
it the preferred choice for satisfaction-centered, gender-
responsive campaign design. A heatmap of the ANOV A
p-values by LLM is shown in Fig. 3.
3.1.4. A Universal Warning: Class Imbalance Collapses
All Three Models
The random forest classification task predicting
premium membership status produced a striking and
unambiguous result: All three LLMs experienced complete
classification collapse in the minority class. Class 1
precision, recall, and F1 registered at zero across GPT-
4, Claude, and Gemini, with AUC values near 0.50. This
was not a model-specific failure; it was a data structure
problem. With premium members representing only 40.5%
of the sample, the random forest algorithms defaulted
to majority-class prediction without corrective interven-
tions. The implication is clear: robust preprocessing for
class imbalance through techniques such as SMOTE,
ADASYN, or cost-sensitive learning is mandatory before
any LLM-assisted classification task on imbalanced
datasets, regardless of the platform.
3.2. Interpretation and Application
The aggregate equivalence finding has a direct practical
implication: organizations that have been paying premium
prices for one model on the assumption of analytical
superiority may be doing so without empirical justifica-
tion. When mapped against pricing data ( Table II), the
performance findings become strategically actionable. The
combination of the lowest API cost tier, fastest processing
speed, and highest clustering quality makes Gemini the
strongest value proposition for teams running large-scale
automated segmentation workflows. Claude’s API cost
is mid-range, but its superiority in psychographic signal
detection justifies investment in campaigns where targeting
precision outweighs volume throughput. GPT-4’s higher
API cost is defensible only when output reproducibility
and stability are mission-critical, such as in regulated
industries or audit-sensitive workflows.Table IIIshows the
LLM pricing comparison across individual and API tiers
as of mid-2025.
Beyond the LLM comparison, the study’s descriptive
findings offer an actionable profile of Generation X for
marketers. Email engagement (mean = 0.42) outpaced
social media engagement (mean = 0.35), confirming that
email remains the more reliable activation channel for
this demographic despite industry investment in social
Fig. 3. Heatmap of ANOV A p-values by model and segmentation variable. Note: Dark teal = statistically significant (p < 0.05). Borderline =
p between 0.05 and 0.10. Light = not significant (p > 0.10). Satisfaction by gender was the only variable that achieved significance across all
three models.
V ol 10 | Issue 3 | June 2026 29

Are All Large Language Models Created Equal? Evidence Brawley-Walker and Qu
TABLE II: LLM Pricing Comparison Individual and API Tiers (Mid-2025)
Platform Individual/mo Team/user/mo API (per 1M tokens)
GPT-4 (ChatGPT Plus/Team) $20 $30 ∼$60–$120
Claude (Pro/Team) $20 $30 ∼$15–$75
Gemini advanced (Google One AI) $19.99 $24–$30 ∼$10–$35
Note: Pricing is based on publicly available rates as of Q2 2025. API costs reflect standard model tiers, whereas actual costs depend on usage volume
and the selected variant. Enterprise pricing is negotiated through contracts.
TABLE III: LLM Selection Framework by Task Priority
User priority LLM Evidence-based rationale
High-volume real-time segmentation Gemini Fastest speed, best clustering quality, lowest API cost tier
Psychographic/gender-responsive campaigns Claude Strongest satisfaction-by-gender signal (p = 0.0202)
Reproducible, auditable iterative analytics GPT-4 Narrowest bootstrap CI; most stable output across iterations
platforms [ 3]. The K-means clustering analysis adds an
immediately actionable insight: all three models unan-
imously identified four behavioral segments, with the
Lapsed/One-Time Buyer cohort (n = 309, 0% repeat rate,
CL V = $157.32) as the highest-priority win-back tar-
get, a recoverable audience whose average CL V can be
recaptured through targeted campaigns informed by the
satisfaction and engagement patterns the LLM analysis
surfaces.
Regardless of the platform, this study established two
universal requirements. First, multi-model verification
should be a standard governance practice: the GPT-4
Pearson correlation discrepancy demonstrates that no sin-
gle LLM output should be treated as authoritative in
high-stakes workflows. Second, class-imbalance correc-
tion must be implemented as a mandatory preprocessing
step before any LLM-assisted classification task on imbal-
anced datasets.
3.3. Limitations
This study has several limitations that warrant trans-
parency and directly inform future research directions.
First, the analysis relied on secondary data from a pub-
licly available Kaggle dataset. While this approach enabled
controlled, reproducible comparisons under standardized
conditions, the dataset does not carry verified provenance
documentation, and the analytical outputs are bounded by
the distributional characteristics of that specific dataset.
The generalizability of these findings to other e-commerce
contexts, industries, or demographic cohorts has not been
established.
Second, the random forest classification task revealed
the consequences of class imbalance without fully resolv-
ing them. This study documents the collapse rather than
testing corrective interventions such as SMOTE or cost-
sensitive learning. Future research should apply these
techniques and evaluate whether LLM-assisted classifica-
tion recovers under-corrected class distributions.
Third, the generalizability of the findings is constrained
by the specific prompt structure, dataset, and model ver-
sions evaluated. The behavior of LLMs is sensitive to
prompt variation, and model updates by vendors may
alter comparative performance over time. The pricing data,
accurate as of Q2 2025, are subject to vendor revision.
Replication studies across different prompting strategies
and updated model versions would strengthen the general-
izability of these findings.
Fourth, this study evaluated five specific analytical tasks.
Marketing analytics encompasses a broader range of appli-
cations, such as predictive lead scoring, natural language
customer review analysis, time-series forecasting, and mul-
tivariate attribution modeling, for which the comparative
findings reported here may not apply directly .
4. Conclusion
The answer to the question posed in this article’s title
depends on the specific analytical requirements of the
practitioners. At the aggregate level, GPT-4, Claude, and
Gemini demonstrated statistically equivalent analytical
accuracy for Generation X e-commerce marketing analyt-
ics under standardized conditions. As a result, premium
pricing for one platform over another cannot be justified
based on claims of overall analytical superiority, a finding
with direct budgetary implications for organizations cur-
rently paying differential subscription rates to access the
software.
However, task-level distinctions are evident and are
operationally meaningful. Gemini demonstrates advan-
tages in processing speed and clustering quality for
high-volume analytical pipelines. Claude exhibits stronger
performance in psychographic segmentation tasks. GPT-
4 offers the highest reproducibility, making it well-suited
for iterative and audit-sensitive workflows. Across all three
models, the consistent identification of the Lapsed or
One-Time Buyer cohort as the highest-priority win-back
segment provides a concrete, data-driven starting point for
organizations targeting Generation X, a demographic rep-
resenting approximately $2.4 trillion in annual purchasing
power.
These findings indicate that the selection of language
models should not be guided by vendor reputation alone.
Instead, organizations should adopt an evidence-based
approach that aligns model selection with task require-
ments, cost structures and governance considerations.
Such alignment enables more efficient resource allocation
and the more effective deployment of artificial intelligence
in marketing analytics.
V ol 10 | Issue 3 | June 2026 30

Brawley-Walker and Qu Are All Large Language Models Created Equal? Evidence
Conflict of Interest
The authors declare no conflicts of interest regarding the
publication of this paper. This study was conducted in the
absence of any commercial or financial relationships that
could be construed as potential conflicts of interest.
AI Assistance Statement
This manuscript was developed with the assistance of
artificial intelligence tools, including Microsoft Copilot to
support language refinement, formatting, and clarity . All
technical content, analyses, and interpretations were devel-
oped and validated by the authors. The authors take full
responsibility for the integrity and originality of this work.
References
[1] U.S. Census Bureau. Data [Internet]. Washington (DC): U.S. Cen-
sus Bureau. 2024 [cited 2024]. A vailable from: https://www .census.
gov/data.html.
[2] Y adav A, Singh S, Dash MK. Digital marketing and consumer
behavior: analyzing purchase intentions of generation X and Y
in the FMCG sector. J Adv Manage Stud . 2025;2(1):29–41. doi:
10.36676/jams.v2.i1.31.
[3] Choudhary R, Shaik Y A, Y adav P, Rashid A. Generational
differences in technology behavior: a systematic literature
review. J Infrastruct Policy Dev . 2024;8(9):6755. doi:
10.24294/jipd.v8i9.6755.
[4] Mahi R, Alam F, Hasan M. Exploring the confluence of big data,
artificial intelligence, and digital marketing analytics: a compre-
hensive review. J Innov Eng Educ Technol . 2024;3(3):1–12. doi:
10.62304/jieet.v3i3.159.
[5] Cherenkov E, Benga V, Lee M, Nandwani N, Raguin K, Sueur
MC, et al. From machine learning algorithms to superior customer
experience: business implications of machine learning-driven data
analytics in the hospitality industry . J Smart Tour. 2024;4(2):5–14.
doi: 10.52255/smarttourism.2024.4.2.2.
[6] Sridharan G, Rao P. Enhancing user experience and undertaking
sentiment analysis with machine learning in social media Twitter
(X). Int Sci J Eng Manage . 2025;04(09):1–9. doi: 10.55041/is-
jem05050.
[7] Ugbaja US, Nwabekee US, Owobu WO, Abieba OA. Revolution-
izing sales strategies through AI-driven customer insights, market
intelligence, and automated engagement tools. Int J Soc Sci Except
Res. 2023;2(1):193–210. doi: 10.54660/IJSSER.2023.2.1.193-210.
[8] Aksoy I, Arslan MK. Comparison of performance of artificial
intelligence tools in answering emergency medicine question pool:
ChatGPT 4. 0, Google Gemini and Microsoft Copilot. Pak J Med
Sci. 2025;41(4):968–72. doi: 10.12669/pjms.41.4.11178.
[9] Aghaei R, Kiaei AA, Boush M, Vahidi J, Zavvar M, Barzegar
Z, et al. Harnessing the potential of large language models in
modern marketing management: applications, future directions,
and strategic recommendations. arXiv [Preprint]. 2025 [cited 2025].
doi: 10.48550/ARXIV .2501.10685.
[10] Bolgova O, Ganguly P, Mavrych V. Comparative analysis of
LLMs performance in medical embryology: a cross-platform
study of ChatGPT , Claude, Gemini, and Copilot. Anat Sci Educ .
2025;18(7):718–26. doi: 10.1002/ase.70044.
[11] Pongwe LJ, Churk J. Social media marketing platforms and sales
revenue in Tanzania Telecommunication Company Limited.Int Rev
Manage Mark. 2024;14(1):31–8. doi: 10.32479/irmm.15294.
[12] Hamid AI, Abdulazeez AM. Sentiment analysis based on machine
learning techniques: a comprehensive review.Indones J Comput Sci.
2024;13(3):4079–97. doi: 10.33022/ijcs.v13i3.4049.
[13] Berman R, Israeli A. The value of descriptive analytics: evi-
dence from online retailers. Mark Sci . 2022;41(6):1074–96. doi:
10.1287/mksc.2022.1352.
V ol 10 | Issue 3 | June 2026 31
