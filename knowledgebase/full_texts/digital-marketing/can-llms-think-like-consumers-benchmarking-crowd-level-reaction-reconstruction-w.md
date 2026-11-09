---
title: Can LLMs Think Like Consumers? Benchmarking Crowd-Level Reaction Reconstruction with ConsumerSimBench
url: https://arxiv.org/abs/2605.17079
category: digital-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Tianyu Wang
- Jiajun Li
- Jianghao Lin
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.17079
pages: 32
chars: 118580
fetched_at: '2026-11-08T13:05:46+00:00'
kb_version: 1
---

# Can LLMs Think Like Consumers? Benchmarking Crowd-Level Reaction Reconstruction with ConsumerSimBench

Can LLMs Think Like Consumers?
Benchmarking Crowd-Level Reaction Reconstruction
with CONSUMERSIMBENCH
Tianyu Wang
Shanghai Jiao Tong University
wty500@sjtu.edu.cn
Jiajun Li
Noumena AI
taringlee@gmail.com
Jianghao Lin
Shanghai Jiao Tong University
linjianghao@sjtu.edu.cn
Abstract
LLMs are increasingly used as “digital consumers” to simulate public opinion,
pre-test marketing decisions, and anticipate audience response. However, exist-
ing evaluations rarely ask whether a model can reconstruct the concrete reaction
patterns that real consumers surface in public discourse. We introduce CONSUMER-
SIMBENCH, a benchmark built from 1,553 real Chinese social-media topics and
23,122 atomic, rule-audited criteria spanning four reaction families. Rather than
scoring open-ended generations with a holistic preference judge, CONSUMER-
SIMBENCHdecomposes each task into auditable yes-no decisions over concrete
reaction points, raising three-judge agreement from 65.8% to 92.1% with 98.4%
agreement between pointwise judge decisions and human-majority labels. Across
13 frontier generators, the strongest model, Gemini-3.1-Pro, covers only 47.8%
of real reaction criteria, while GPT-5.2 and Claude-4.6 trail far behind despite
their strength on technical benchmarks. The failures reveal a sharp gap between
technical-benchmark performance and socially grounded consumer intuition. A
direct structured reasoning prompt decreases coverage, while a generate–reflect
multi-agent pipeline improves MiMo-V2.5-Pro from 32.9% to 37.6% on a subset.
CONSUMERSIMBENCHreframes consumer simulation as a forecasting problem
over real public-discourse reactions, showing that frontier LLMs remain far from
reliably predicting what consumers will actually care about in high-context Chinese
consumer discourse.
1 Introduction
“If an LLM can truly think like a consumer,
it should be able to predict what a real user would say about a brand. ”
The vision of LLMs acting asdigital consumersis rapidly moving from demos to deployment. Teams
increasingly use LLM agents to simulate social opinion [1–3], pre-test marketing messages [4, 5],
and design social strategy [6, 7]. The motivation is straightforward: traditional consumer research is
slow and expensive, while large-scale scalar signals such as click-through rate (CTR) are post-hoc,
platform-specific, and often fail to explainwhyconsumers react the way they do.
However, downstream decision-makers still lack a principled understanding ofhow closely LLM
simulations align with actual human behaviorsin high-context, strategic, and socially intensive
environments [8]. For example, on lifestyle-oriented user-generated-content (UGC) platforms such as
RedNote or Youtube, creators often rely on pragmatic moves such as reverse signaling, humblebrag-
ging, and anxiety induction to shape how audiences interpret a post. In such settings, surface-level
understanding (e.g.,the text expresses sadness) is insufficient; what matters isstrategic social
intelligence(e.g.,the YouTuber creates a sad atmosphere for his advertisement), which requires
Preprint. Dataset:https://huggingface.co/datasets/wty500/ConsumerSimBench.
arXiv:2605.17079v1  [cs.CL]  16 May 2026

95
145
98
116
64
20
39
36
68
225777 114
2317
123
329
30 57 23
518 (33%
)
185 (12%) 271 (17%)
579 (37%)
Celebrity gossip
Film & TV
Music & concert
Variety show
Idol & fan culture
Beauty & cosmetics
Fashion & outfit
Food & dining
Travel & destination
Home & decor
Pro sports event
Online drama
Public policy
Public accidents
Viral memes
Brand event
Tech product launch
Fitness & wellness
Esports
Athlete spotlight
1,553
trending topics
Figure 1:Overview of CONSUMERSIMBENCH.Left:The 1,553 trending topics span four super-
categories and twenty consumer-facing sub-fields.Right:One task instance. Given a real trending
topic, a generator must produce a free-form bundle of consumer comments that collectively cover an
audited set of atomic criteria across four reaction families (flashpoints, emotion, praise, critique).
understanding the narrative stance and how it is meant to shape the audience’s inference. This can
fundamentally reshape the marketing industry, because reliably predicting consumer reactions before
publication could defuse the next viral crisis instead of apologizing for it, and identify breakout
angles before chasing them, which remains an extremely difficult mission even for marketing experts.
Existing benchmarks are inadequate for three reasons.First, real UGC does not follow the logic in
standard ToM-style tests. ToM examples are typically built around a strict reasoning trace (e.g.I
stole the hat. He did not see. So, he doesn’t know the hat is missing.) [9],where the key facts are
explicit and the answer space is closed. In contrast, real UGC’s meanings can be layered, implicit,
and involve satire or boasting (e.g.It is so annoying to decide which house to decorate!).Second,
many benchmarks emphasize the prediction of a choice, distribution, scalar number, or fixed user
trace (e.g., CTR, SSR [10, 11], public-opinion distributions [12], social-media engagement labels and
conditioned comment prediction [13, 14], popularity prediction [15], etc.), which cannot evaluate
models’ open-ended humanities-side capacity [16]. Practitioners care aboutwhat real people will say
and why; most benchmarks only measurewhat label a model predicts.Third,many evaluations rely
on an LLM to directly assign a holistic final score for an open-ended output, which can be subjective,
unstable, and vulnerable to systematic biases [ 17–20]. This makes it difficult to interpret what a
numeric score means and whether it is reliable across models, prompts, and domains.
Meanwhile, despite LLMs’ top performance on quantitative leaderboards [ 21–23],social-media
users continue to complain that these models are weak at the “humanities” side of language—
reading people, registering social nuance, and showing human touch. Part of this perceived gap is a
benchmarking artifact, where very few benchmarks audit a model’s humanities-side skills.
To bridge these gaps, we introduce CONSUMERSIMBENCH, a benchmark designed to evaluate
whether LLMs can simulateauthentic consumer behaviorsin the wild. We use RedNote as a major
consumer-facing UGC platform where real reactions to products, brands, entertainment releases,
lifestyle trends, and public events are observable at scale. Its dense, high-context consumer discourse
makes it a representative and practically important setting for testing whether models can anticipate
what consumers will notice, praise, attack, and emotionally amplify. Concretely, given a trending topic
and its event description, a model is required to generate realistic comments. We audit coverage over
four reaction families:(i)sentiment flashpoints, the concrete social triggers;(ii)emotion keywords, the
overall sentiment of the real crowd;(iii)positive aspects, what users praise;(iv)negative aspects, what
users attack. Every criterion is atomic, defined, example-anchored, and rule-audited. We find that even
the strongest model (Gemini-3.1-Pro: 47.8%) performs poorly on this humanities task, and top-tier
models that look comparable on technical benchmarks diverge sharply on CONSUMERSIMBENCH
(GPT-5.2: 35.8%, Claude-Opus-4.6: 32.8%). This gives measurable feedback on a humanities-side
capability that current LLM training and evaluation often underemphasize.
2

Table 1: Positioning byunit of inference. Consumer simulation requires open-form, crowd-level
reconstruction of real public discourse with auditable targets. Among the benchmark families
summarized here, CONSUMERSIMBENCHis the only one that satisfies all five criteria jointly.
Benchmark family Unit of inference Real public discourse Free-form generation Strategic targets Auditable eval
ToM [24, 25, 9] Dyad (Alice / Bob)✗(fictional)✗(MCQ)△ △
CTR (scalar prediction) Aggregate scalar✓ ✗ ✗ ✓
Persona Simulation [26, 4] Individual trajectory△✓△✗
CONSUMERSIMBENCH(Ours) Crowd reaction✓ ✓ ✓ ✓
Our main contributions are:
• To study whether an LLM cantruly think like a consumer, we proposeCONSUMER-
SIMBENCH, a UGC-behavior simulation benchmark that operationalizes this question as
crowd-level reaction reconstruction: given a real trending topic and event description, can
the model reconstruct the reaction patterns that real consumers surfaced in public discourse?
• To make open-ended consumer-likeness measurable, CONSUMERSIMBENCHcontains 1,553
real topic instances and 23,122 atomic scoring criteria that jointly evaluate emotion keywords
and emotional burstsat the macro level, and content-faithful expressions of individual
consumer feedbackat the micro level.
• For automatic evaluation, we construct detailed criteria that turn open-ended scoring from
holistic “judge the answer” decisions intoauditable yes-no questions. This yields 92.1%
three-judge agreement, reaches 98.4% agreement with human-majority labels, and outper-
forms holistic LLM-as-Judge scoring (65.8%) and traditional similarity metrics such as
Jaccard and N-gram overlap.
• We test both a structured-prompt and a generate–reflect multi-agent pipeline. A direct
CONSUMERSCF prompt hurts, while iterative multi-agent refinement improves MiMo-
V2.5-Pro by +4.7 points and GPT-5.2 by +1.8 points on a 100-topic slice.
2 Related Work
Persona simulation.Recent work has explored using LLMs as proxies for human behavior in
opinion, market, and psychological studies [ 27–31]. Generative Agents [ 26] demonstrated that
LLM-powered agents with memory, planning, and reflection can exhibit emergent social behaviors
in a simulated town. Subsequent work has extended this paradigm to social-science experiments
[32–36], user-behavior simulation [ 4, 5, 1–3, 37, 38], cognitive reasoning and human-response
modeling [39–41], customer simulation [42, 43], marketing simulation [44–49], opinion dynamics
and pluralism [ 50, 51], multi-turn user simulation [ 52, 53], war simulation [ 54], comprehensive
systems and agentic public-opinion analysis [55–60], and others [61, 62]. Critical studies also warn
that synthetic respondents can fail systematically as replacements for human survey data [63]. Across
these works, the similarity between LLM agents and real human social behavior is mostly evaluated
through classical psychology, survey, or social-science experiments, which risk data contamination or
being solved by general common sense rather than genuine open-ended reaction reconstruction.
Evaluating LLMs’ mindset.Current benchmarks mainly rely on multiple-choice [ 64–72], clas-
sification [73], LLM-as-a-Judge [ 74, 17, 75–79], and similarity metrics like Rouge-L [ 80] and
BERTScore [81]. Beyond emotional and cognitive benchmarks [ 82–86], a parallel line of work
uses Theory-of-Mind (ToM) tasks [ 9] to track what one agent believes another believes, in styl-
ized, closed-form, typically multiple-choice scenarios [87, 24, 25, 88–92]. While these benchmarks
illuminate a cognitive competence, they test reasoning ability rather than the actual emulation of
human social behavior, and their scoring is largely subjective. Our work advances benchmarking on
humanities-side capabilities with auditable criteria even when the answer is not unique.
Position.As shown in Table 1, CONSUMERSIMBENCHtargets a different competence from ToM.
ToM asks whether a model canreasonabout a mind; CONSUMERSIMBENCHasks whether a model
canreconstructwhat a crowd will think, feel, and say about a real brand event.
3

Figure 2:CONSUMERSIMBENCHconstruction and evaluation pipeline.Public trend signals are
curated into topic–event records and abstracted observed reactions; these reactions are converted into
four families of atomic reaction criteria, hardened, and finally used for pointwise coverage judging of
model-generated comments. The final score gives equal weight to the four reaction families.
3 CONSUMERSIMBENCHDataset Design
3.1 Design goals
CONSUMERSIMBENCHtargets four design goals.1. Authenticity over generic plausibility:Rather
than synthesizing diverse scenarios, we ground every record in real public reactions. Models must
reconstruct the salient reaction points real consumers surfaced about a real brand, product, or public
event, not merely sound emotional; this evaluates public-trend reaction coverage rather than median
survey sentiment.2. Free-form outputs:A model should not merely classify sentiment into a
pre-set category [93]; it should simulate what a crowd of consumers would plausibly say.3. Derived
artifacts:For responsible release, we publish derived, anonymized artifacts rather than raw user
histories or identifiers.4. Auditable scoring:Instead of asking a vague“How good is this answer?”
question like what LLM-as-Judge benchmarks do (“40% human-like” is meaningless), we change
it into a series of auditable decisions:“Did the generated comments cover this particular reaction
point?”, where every point is an inspectable criterion with definitions, examples, and rules. The
result is far more stable and easier to interpret than a global similarity score.
3.2 Task formulation
Each topic has a topic keyword k and a neutral event description d. Given the i-th topic {ki, di}, an
LLM π is required to produce ni (10–30) realistic comments. The comments will be graded from
four dimensions, each contributing25%of the total score:
• T1 sentiment flashpoints: The emotional trigger that real consumers resonate with, which
can be one or many phrases. This is usually the reason that pushes the topic onto the trending
list. Accurately predicting these triggers, both positive and negative, can help brands avoid
reputation crises while identifying possible viral hits. For example, the topicArc’teryx’s
fireworkshas a flashpoint namedenvironmental protection, where people’s concern about the
fireworks’ environmental impact later led to a public-relations crisis. The grading process
judges how many flashpoints are clearly identified, and the score is the ratio.
• T2 emotion keywords: The affective vocabulary that best describes people’s attitude in the
comments (such asresentful,conflicted,put on the spot). They can cover many aspects, and
all the words are open-form. There are no preset categories. The grading process identifies
how many emotions are present in the generated posts, using semantic coverage rather than
exact word matching.
• T3 positive aspects:The specificdetailsappearing in the original event that consumers like,
praise, or upvote (such ascost-effectivenessandemotional value). The marketing industry
can use this to test if their proposed selling point will lead to the intended response.
4

• T4 negative aspects:Similar to T3, these are the details on which criticism occurs against
the original event (such asdiscriminationoraffectation). A capable model on this can help
the marketing industry avoid inappropriate phrasing in their post.
Within each section, the score is
si,j = #of matched criteria inT j #of total criteria inT j (1)
and the final total score is
s= 1 N
NX
i=1
si,1 +s i,2 +s i,3 +s i,4
4 .(2)
Atomic Criteria.Each of the four dimensions decomposes into atomic criteria that can be judged
independently. As shown in Table 2, every atomic criterion contains five fields:1.the corresponding
trigger / keyword / aspect;2.a detailed definition;3.positive examples that meet the criterion;4.
negative examples that do not;5.a one-sentence judgment rule that disambiguates edge cases. A
single comment may cover multiple criteria, and evaluation is over the concatenated comment set
rather than one-to-one post matching.
For each atomic criterion, we ask a judge model whether the generated comments cover that criterion.
To keep evaluation fair across generators that produce different numbers or lengths of comments,
we concatenate each model’s comments and truncate the judge-visible text to 3,600 characters, the
estimated empirical 99% coverage bound, and adaptni to follow the empirical comment-volume. The
judge receives all the above criteria, and returns a binary score and an explanation. The benchmark
score is interpretable because every point corresponds to a concrete, inspectable decision.
Latent reaction points.CONSUMERSIMBENCHis a forecasting benchmark, not an entailment
benchmark. We do not restrict criteria to reactions directly implied by the event description alone. We
therefore include reaction points that real users surfaced through platform conventions, prior brand
knowledge, local memes, demographic identity, and recent discourse.
Table 2: Example T1 flashpoint criterion for a product-recall topic. All 23,122 criteria follow this
five-field structure.
Field Content
Trigger “Apology lacks sincerity”
Definition Users question whether the public apology is genuine or merely a tactic.
Positive example “This reads like their PR team wrote it”
Negative example “I don’t like this brand”
Judgment rule Credit only if the comment questions thesincerity or authenticityof the apology,
not general brand criticism
3.3 Dataset Collection and Construction
Data Collection.We source data from RedNote (Xiaohongshu), a Chinese social platform with
300M+ monthly active users focused on lifestyle and consumer content, providing rich naturalistic
context for consumer behavior. RedNote’s trending-topic lists and topic summaries are published by
multiple third-party public aggregators (e.g., tophub.today, qian-gua.com). We obtain hot-topic
keywords and their public summaries from these aggregators and through manual collection. We only
use publicly available content. We do not scrape or crawl RedNote, do not use any undocumented
platform API, and do not access raw user posts, account identifiers, or any logged-in views. Each topic
is verified by an actual public-trending search on the corresponding date, and the resulting artifact
contains no quoted user text and no information by which an individual user could be identified.
Collection complies with each aggregator’s posted terms of service.
After this collection step we apply LLM-based filtering to retain only topics that are related to
consumer reactions, and we manually sample 100 topics to verify the filtering quality.
Criteria drafting.For each topic, an LLM proposes T1/T2/T3/T4 criteria with definitions, posi-
tive/negative examples, and judgment rules, along with objective topic descriptions. Each proposed
5

criterion is anchored in observed source reactions, while an LLM standardizes those reactions into au-
ditable records with explicit decision boundaries in Table 2. Appendix D summarizes the operational
drafting prompt.
Criteria hardening.We harden the drafted criteria to remove event-restatement leakage, semantic
duplication, over-pruning, and judge-fragile meme points. The process merges similar topics and
criteria, drops criteria that collapse to the event description, checks within-topic independence, and
audits pruned items. Appendix E gives the full hardening protocol and examples. After hardening
and pruning, the releasedevaluation set contains 23,122 criteria. All headline leaderboard scores
and error analyses in the paper are reported on this final evaluation set.
4 Experiments and Results
4.1 Dataset Statistics Table 3: Benchmark statistics.
Statistic Value
Topic instances 1,553
Atomic criteria (total) 23,122
Sentiment flashpoints 3,779
Emotion keywords 8,749
Positive aspects 5,666
Negative aspects 4,928
Average criteria per topic 14.9
Median criteria per topic 14
We collected hot topics between March and September 2025.
The final release contains 1,553 topics with 23,122 crite-
ria. We release the canonical Chinese benchmark, English
sidecars for reviewer inspection, judge prompts, and the eval-
uation harness under CC BY-NC. Official evaluation uses
the Chinese criteria for judge consistency, and the released
criteria contain abstracted reaction-type descriptions rather
than raw user content or account identifiers. Additional
statistics are shown in Table 3.
Topic coverage.The 1,553 topics span four categories and twenty consumer-facing sub-fields
(Figure 1, left). Society and public-issue topics dominate (37%) because they generate the highest
engagement on the platform, followed by entertainment (33%), sports and gaming (17%), and lifestyle
goods (12%). This breadth makes domain-specific strengths visible rather than letting any single
topic family dominate the leaderboard.
Candidates.We evaluate Gemini-3.1-Pro, Gemini-3-Flash, Qwen3.5-397B, Grok-4.2, DeepSeek-
V3, Doubao-Seed-1.8-Thinking, Kimi-K2.5, GPT-5.2, MiniMax-M2.5, Claude-Opus-4.6, MiMo-
V2.5-Pro, Claude-Sonnet-4.6, and GPT-4o.
Judge.We use GPT-5.2 as the fixed judge for cost-effectiveness; §5.3 validates judge reliability
with cross-judge and human-audit checks.
4.2 Main Results
We now answer the opening question empirically. Can LLMs think like consumers, in the sense of
reconstructing what a crowd will say in real public discussion? The headline isnot yet, and the
remaining gap is not uniform.
Figure 3 shows the full leaderboard. The best model, Gemini-3.1-Pro, reaches 47.8% overall,
followed by Gemini-3-Flash at 46.6%. Grok-4.2, Kimi-K2.5, Qwen3.5-397B, DeepSeek-V3, and
Doubao-Seed-1.8 form a tight 42–45% middle tier. GPT-5.2 ranks eighth at 35.8%; MiniMax-M2.5,
Claude-Opus-4.6, MiMo-V2.5-Pro, Claude-Sonnet-4.6, and GPT-4o stay at 29–35% in this setting.
Rank order is stable under bootstrap resampling, and the broad tiering is stable under the criteria-
weighted micro-average. The gap is not regional, and the hard sections (T1 flashpoints and T4
criticisms) remain difficult across the leaderboard.
Despite having competitive performance on technical benchmarks, top-tier models (such as Gemini-
3.1-Pro, GPT-5.2 and Claude-Opus-4.6)have a significant performance gapin mimicking consumer
behaviors. Gemini is roughly 12 points above GPT-5.2 and Claude-Opus-4.6, giving measurable
form to a common user-facing complaint about emotional value, namely that some frontier assistants
can produce fluent comments while still missing the affective targets and criticism vectors that make
public reactions feel human. Moreover,all models remain far from the ceiling. Even the strongest
model leaves nearly half of real consumer reactions uncovered.
6

Table 4: Full leaderboard on the final benchmark (1,553 topics, 23,122 criteria). Scores are percent-
ages (judge GPT-5.2). Overall scores include 95% bootstrap CIs over topics; the broad tier separation
is stable under topic bootstrap and criteria-weighted micro-averaging.
Model AVG(95% CI) T1 T2 T3 T4
1 Gemini-3.1-Pro47.8[46.9, 48.7] 38.956.961.231.1
2 Gemini-3-Flash 46.6 [45.7, 47.4]39.553.163.826.8
3 Grok-4.2 44.9 [44.1, 45.8] 36.8 52.5 60.0 27.2
4 Kimi-K2.5 43.5 [42.7, 44.4] 35.9 49.0 55.6 30.4
5 Qwen3.5-397B 43.4 [42.5, 44.2] 36.1 50.4 59.8 23.9
6 DeepSeek-V3 42.9 [42.0, 43.8] 33.9 49.2 54.8 30.6
7 Doubao-Seed-1.8 42.4 [41.5, 43.2] 34.8 51.0 58.3 22.1
8 GPT-5.2 35.8 [35.0, 36.7] 31.4 35.1 47.8 25.6
9 MiniMax-M2.5 35.2 [34.3, 36.1] 28.8 40.6 48.3 19.6
10 Claude-Opus-4.6 32.8 [31.7, 33.9] 25.4 37.7 44.7 19.8
11 MiMo-V2.5-Pro 32.3 [31.5, 33.1] 27.4 39.7 45.3 20.1
12 Claude-Sonnet-4.6 30.8 [30.0, 31.6] 24.8 32.6 46.0 16.1
13 GPT-4o 29.7 [28.9, 30.5] 23.5 35.8 43.5 12.1
0 10 20 30 40 50
Overall score (%) — colored bar = 95% bootstrap CI over topics
1. Gemini-3.1-Pro
2. Gemini-3-Flash
3. Grok-4.2
4. Kimi-K2.5
5. Qwen3.5-397B
6. DeepSeek-V3
7. Doubao-Seed-1.8
8. GPT-5.2
9. MiniMax-M2.5
10. Claude-Opus-4.6
11. MiMo-V2.5-Pro
12. Claude-Sonnet-4.6
13. GPT-4o
47.8
46.6
44.9
43.5
43.4
42.9
42.4
35.8
35.2
32.8
32.3
30.8
29.7
A  Overall Leaderboard
T1 T2 T3 T4
20
30
40
50
60
Section score (%)
B  Section Difficulty
T op-1
T op-5 mean
GPT-5.2
Figure 3: Main results. Left: overall leaderboard on the final full benchmark. Right: section-wise
difficulty, comparing the top model, the top-5 mean, and GPT-5.2. Flashpoints and negative aspects
remain the hardest families.
4.3 The Asymmetric Failure: Tone without Target
We find thatcurrent LLMs can partially“sound”like consumers, while failing to predict what
consumers will focus on or attack.Across all 13 models, T2 and T3 are 15–30 points easier than
T1 and T4. For the top model, section scores have a 22–30 point spread that does not close at scale.
It is acrowd-forecasting error, where models often sound socially fluent, but fail to recover the
concrete objects of attention, such as the meme phrases, product details, regional constraints, or
business-model facts that become the public hook. For downstream marketing use cases, this is
the decisive failure, because crisis forecasting and pre-launch risk assessment depend precisely on
anticipating those hooks. The same T1/T4 gap persists across model tiers. The same asymmetric
pattern appears in a second-platform YouTube pilot (Appendix G, Figure 6), where the construction is
instantiated on 100 English trending videos and again finds positive aspects easiest while flashpoints
and negative aspects remain hardest.
Figure 4 further checks whether the failure is an artifact of one domain, and finds the gap is broad
rather than domain-local. Model scores vary across the 20 sub-fields, but every sub-field remains far
from ceiling, and the relative rankings are stable across domains. This suggests that the gap is not
reducible to a single topic family such as celebrity gossip or tech launches.
5 Ablations and Robustness
5.1 Where does the error come from?
7

25 35 45 55
Score (%)
Food & dining
Beauty
Travel
Home & decor
Public accidents
Music & concert
Public policy
Athletes
Fitness
Fashion
Viral memes
Celebrity
Sports
Brand event
Esports
T ech launch
Idol / fans
Online drama
Film & TV
Variety show
Gemini 3.1 Pro
T op-5 mean
GPT-5.2
Claude 4.6
Figure 4: Ranked sub-field gap plot across
20 consumer-facing domains. Rows are
sorted by Gemini-3.1-Pro score; horizon-
tal spans show the cross-model range.
0 10 20 30 40 50
Score (%)
Gemini 3.1 Pro
Qwen 3.5
GPT-5.2
Claude-Sonnet-4.6
-1.7
-5.0
-3.5
-4.0
Naive prompt ConsumerSCF Δ
Figure 5: Direct SCF prompting does
not improve coverage. Arrows show the
change from naive prompting (blue) to
CONSUMERSCF (red).
We classify all 197,790 missed criteria across the 13
generators by parsing judge explanations into an 8-
category taxonomy (Appendix B; the categorization
is derived from keyword patterns in judge text plus a
50-sample manual audit). Using this taxonomy, we find
thatmissing-content patterns dominate the error tax-
onomy. Generations are topically relevant but do not
surface the specific reaction trigger (44.5% of misses),
section-specific vocabulary at T2–T4 (28.6%) or the
flashpoint anchor itself (7.1%). Combined, 80.2% of
misses pattern-match to lexical / anchor specificity
rather than semantic disagreement. Meme repetition
without pragmatic transfer (8.8%) concentrates in T1;
opposite-valence patterns (7.1%) are most prevalent in
T3. On the final 23,122-criterion benchmark, 6,677
criteria (28.9%) are covered by zero of the 13 mod-
els. The two “hard” families have higher zero-coverage
rates (T1 = 49.3%, T4 = 41.6%) than the easier two
(T2 = 19.4%, T3 = 18.8%), consistent with flashpoint
anticipation and criticism forecasting being the fron-
tier challenges. These errors point to a more specific
cognitive gap than generic sentiment modeling: models
often recognize the event topic and produce plausible
affect, but fail atattention-anchor selection—deciding
which concrete detail will become the object of pub-
lic repetition, moralization, joking, or complaint. This
also explains why T1 and T4 are hardest: they require
stance-taking around a socially charged anchor, not
merely naming an emotion or listing a product attribute.
5.2 Does direct SCF prompting help?
We test whether a specially designed prompt can im-
prove coverage. A standard “few-shot” control is not
clean because the task has no canonical ground-truth re-
sponse. There are no so-called “reference comments”.
Instead, we develop CONSUMERSCF, an expanded
structured social-cognitive prompt based on consumer
psychology. Before generation, it asks the model to
internally reason through three social-theory lenses—self-presentation strategy, displayed capital,
and framing [94–96]—and operationalizes each lens with concrete participation motives, identity
signals, resource cues, and narrative frames; the full prompt is shown in Appendix J. This makes
CONSUMERSCF stronger than a vague role prompt, since it expands social cognition into participation
motives, identity and resource signals, and narrative packaging choices. We randomly select 100
topics across four generators that span the leaderboard (Gemini-3.1-Pro, Qwen3.5-397B, GPT-5.2,
Claude-Sonnet-4.6). As Figure 5 shows, CONSUMERSCF averages −3.5 ptbelow the naive prompt,
andall four generatorsare worse (Gemini-3.1-Pro −1.7; Qwen3.5-397B −5.0; GPT-5.2 −3.5;
Claude-Sonnet-4.6 −4.0). The result does not rule out every possible prompting variant, but it shows
that simply inserting an explicit social-theory scaffold into a single generation call is not enough;
under this direct formulation, coverage consistently falls.
We also evaluate a generate–reflect multi-agent pipeline based on MEGAAGENT[ 59] on the same
100-topic slice. It first produces the naive comment set, then lets a CEO agent autonomously define
subordinate agents, exchange files and messages, identify missing reaction angles, and refine the
draft. It improves MiMo-V2.5-Pro from 32.9% to37.6%(+4.7 pt; 54 wins, 22 ties, 24 losses)
and GPT-5.2 from 30.1% to31.8%(+1.8 pt; 41 wins, 29 ties, 30 losses). These gains show that
CONSUMERSIMBENCHcan reward iterative refinement beyond a single call.
Generic chain-of-thought is difficult to isolate for current frontier APIs, where hidden reasoning is
already part of the serving stack. Text classifiers, ABSA, and opinion-mining models are natural
8

baselines for fixed-label reaction prediction [ 13], but they predict labels for given text, whereas
CONSUMERSIMBENCHrequires open-ended comments for a new topic and then audits whether
those comments recover unseen reaction criteria.
5.3 Are pointwise judges reliable?
Our main experiments use GPT-5.2 as the fixed judge for cost-effectiveness. We validate the
scoring pipeline at three levels: inter-judge agreement, intra-judge stability, and human audit of
pointwise labels. The audit asks annotators to assign their own yes/no label for each generated-
comment/criterion pair, allowing us to compare frozen judge labels against independent human-
majority labels.
For inter-judge reliability, we employ three independent judges (GPT-5.2, Gemini-3-Pro, and Claude-
4.5-Opus) on 100+ criteria from 10 random topics with the same rules. The three judges achieve
92.1% agreement. Compared with holistic LLM-as-Judge scoring, whose agreement rate collapses
to 65.8%,our yes-no criteria yield substantially higher agreement. We also show the necessity
of our five-field criteria by keeping only the trigger itself: the agreement rate drops from 92.1% to
84.8%, showing that the judgment rule carries real signal. For intra-judge stability, we run GPT-5.2
three times on the same set and obtain 91.8% agreement. Together, these checks support pointwise
judging as a relatively stable method.
Finally, we connect inter-judge reliability to human validity by asking three human annotators to
label the same 100+ criteria. The audit finds 98.4% agreement between pointwise judge decisions
and human-majority labels. On the hardest subset—the three-judge-disagreement cases—human
majority still agrees with the LLM-judge majority in 84.6% of cases. The remaining disagreements
are semantic-boundary keyword cases, suggesting that errors are localized to ambiguous criterion
boundaries rather than systematic judge misalignment. We also reduce length bias by judging
only the first 3,600 characters of each generation and reduce style bias by asking the judge to
apply criterion-specific definitions, examples, negative examples, and semantic-equivalence rules
rather than rewarding rhetorical fluency. As a post-hoc check, verbosity alone does not explain the
leaderboard: Gemini-3.1-Pro is the top model without being the longest generator, and MiMo-V2.5-
Pro outperforms several longer generators.
6 Release and Responsible Use
For responsible release, we use only publicly available topic-level materials and do not crawl RedNote
posts, access undocumented platform APIs, or release raw user threads or account identifiers.
The public release at https://huggingface.co/datasets/wty500/ConsumerSimBench ships
the benchmark JSONL, three judge prompts, English sidecars for reviewer inspection, and the
evaluation harness. Its intended use is marketing-facing reaction forecasting: anticipating praise
targets, criticism vectors, emotional flashpoints, and breakout angles before release. Raw RedNote
threads are not included. A high score indicates reaction-forecasting capability, while deployment
should still account for platform, product, and governance context (Appendix F).
7 Conclusion
Can LLMs think like consumers?On CONSUMERSIMBENCH, the answer isnot yet. The best system
reconstructs only 47.8% of what real public discussion surfaces, and the failure is asymmetric: models
can sound emotional while failing to anticipate which trigger will dominate or which dimension
users will attack. Moreover, direct structured prompting fails, while a multi-agent pipeline slightly
improves. Closing the gap likely requires more than adding prompt-level scaffolding alone.
The broader message is a reframing, fromdyadic belief inferencein fictional vignettes tocrowd-
level reaction reconstructionin real public discourse. Models that sound consumer-like are not
automatically models that anticipate consumer criticism, and for downstream marketing users, the
latter is what matters. With top-tier LLMs surging on technical benchmarks, CONSUMERSIMBENCH
gives measurable form to a complementary frontier of open-form humanities problems, where models
must anticipate socially grounded reactions rather than solve formally specified tasks. This echoes
users’ complaint that today’s models often lack real emotional value, not just logical competence.
9

References
[1] Diyi Yang, Caleb Ziems, William Held, Omar Shaikh, Michael S Bernstein, and John Mitchell.
Social skill training with large language models.arXiv preprint arXiv:2404.04204, 2024.
[2] Jinghua Piao, Yuwei Yan, Jun Zhang, Nian Li, Junbo Yan, Xiaochong Lan, Zhihong Lu,
Zhiheng Zheng, Jing Yi Wang, Di Zhou, et al. Agentsociety: Large-scale simulation of llm-
driven generative agents advances understanding of human behaviors and society.arXiv preprint
arXiv:2502.08691, 2025.
[3] Zeyu Zhang, Jianxun Lian, Chen Ma, Yaning Qu, Ye Luo, Lei Wang, Rui Li, Xu Chen, Yankai
Lin, Le Wu, et al. Trendsim: Simulating trending topics in social media under poisoning
attacks with llm-based multi-agent system. InFindings of the Association for Computational
Linguistics: NAACL 2025, pages 2930–2949, 2025.
[4] Lei Wang, Jingsen Zhang, Hao Yang, Zhi-Yuan Chen, Jiakai Tang, Zeyu Zhang, Xu Chen,
Yankai Lin, Hao Sun, Ruihua Song, et al. User behavior simulation with large language
model-based agents.ACM Transactions on Information Systems, 43(2):1–37, 2025.
[5] Man-Lin Chu et al. Llm-based multi-agent system for simulating and analyzing marketing and
consumer behavior. InIEEE International Conference on e-Business Engineering (ICEBE),
2025.
[6] Xinyi Mou, Xuanwen Ding, Qi He, Liang Wang, Jingcong Liang, Xinnong Zhang, Libo Sun,
Jiayu Lin, Jie Zhou, Xuanjing Huang, et al. From individual to society: A survey on social
simulation driven by large language model-based agents.arXiv preprint arXiv:2412.03563,
2024.
[7] Yao Qu and Jue Wang. Performance and biases of large language models in public opinion
simulation.Humanities and Social Sciences Communications, 11(1):1–13, 2024.
[8] Qian Wang, Jiaying Wu, Zichen Jiang, Zhenheng Tang, Bingqiao Luo, Nuo Chen, Wei Chen,
and Bingsheng He. Llm-based human simulations have not yet been reliable.arXiv preprint
arXiv:2501.08579, 2025.
[9] Ruirui Chen, Weifeng Jiang, Chengwei Qin, and Cheston Tan. Theory of mind in large
language models: Assessment and enhancement. In Wanxiang Che, Joyce Nabende, Ekaterina
Shutova, and Mohammad Taher Pilehvar, editors,Proceedings of the 63rd Annual Meeting of
the Association for Computational Linguistics (Volume 1: Long Papers), pages 31539–31558,
Vienna, Austria, July 2025. Association for Computational Linguistics.
[10] Luyu Chen, Quanyu Dai, Zeyu Zhang, Xueyang Feng, Mingyu Zhang, Pengcheng Tang,
Xu Chen, Yue Zhu, and Zhenhua Dong. Recusersim: A realistic and diverse user simulator for
evaluating conversational recommender systems. InCompanion Proceedings of the ACM on
Web Conference 2025, WWW ’25, page 133–142, New York, NY , USA, 2025. Association for
Computing Machinery.
[11] Benjamin F Maier, Ulf Aslak, Luca Fiaschi, Nina Rismal, Kemble Fletcher, Christian C
Luhmann, Robbie Dow, Kli Pappas, and Thomas V Wiecki. Llms reproduce human purchase
intent via semantic similarity elicitation of likert ratings.arXiv preprint arXiv:2510.08338,
2025.
[12] Fernando Miranda and Pedro Paulo Balbi. Simulating public opinion: Comparing distributional
and individual-level predictions from llms and random forests.Entropy, 27(9):923, 2025.
[13] Ljubisa Bojic, Alexander Felfernig, Bojana Dinic, Velibor Ilic, Achim Rettinger, Vera Mevorah,
and Damian Trilling. Llm agents predict social media reactions but do not outperform text
classifiers: Benchmarking simulation accuracy using 120k+ personas of 1511 humans.arXiv
preprint arXiv:2604.19787, 2026.
[14] Nils Schwager, Simon Münker, Alistair Plum, and Achim Rettinger. Towards simulating social
media users with llms: Evaluating the operational validity of conditioned comment prediction. In
The Proceedings for the 15th Workshop on Computational Approaches to Subjectivity, Sentiment
Social Media Analysis (WASSA 2026), pages 208–221, 2026.
10

[15] Bo Wu, Peiye Liu, Wen-Huang Cheng, Bei Liu, Zhaoyang Zeng, Jia Wang, Qiushi Huang, and
Jiebo Luo. Smp challenge: An overview and analysis of social media prediction challenge. In
Proceedings of the 31st ACM International Conference on Multimedia, 2023.
[16] Tiancheng Hu, Joachim Baumann, Lorenzo Lupo, Nigel Collier, Dirk Hovy, and Paul Röttger.
Simbench: Benchmarking the ability of large language models to simulate human behaviors.
arXiv preprint arXiv:2510.17516, 2025.
[17] Quan Tu, Shilong Fan, Zihang Tian, Tianhao Shen, Shuo Shang, Xin Gao, and Rui Yan.
Charactereval: A chinese benchmark for role-playing conversational agent evaluation. In
Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 11836–11850, 2024.
[18] Jiaheng Liu, Zehao Ni, Haoran Que, Tao Sun, Zekun Wang, Jian Yang, Jiakai Wang, Hongcheng
Guo, Zhongyuan Peng, Ge Zhang, et al. Roleagent: Building, interacting, and benchmarking
high-quality role-playing agents from scripts.Advances in Neural Information Processing
Systems, 37:49403–49428, 2024.
[19] Jiawei Gu, Xuhui Jiang, Zhichao Shi, Hexiang Tan, Xuehao Zhai, Chengjin Xu, Wei Li, Yinghan
Shen, Shengjie Ma, Honghao Liu, Saizhuo Wang, Kun Zhang, Yuanzhuo Wang, Wen Gao,
Lionel Ni, and Jian Guo. A survey on LLM-as-a-Judge.arXiv preprint arXiv:2411.15594,
2024.
[20] Guiming Hardy Chen, Shunian Chen, Ziche Liu, Feng Jiang, and Benyou Wang. Humans
or LLMs as the judge? a study on judgement bias. InProceedings of the 2024 Conference
on Empirical Methods in Natural Language Processing, pages 8301–8327. Association for
Computational Linguistics, 2024.
[21] Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni, Abhranil Chandra, Shiguang Guo,
Weiming Ren, Aaran Arulraj, Xuan He, Ziyan Jiang, et al. Mmlu-pro: A more robust and
challenging multi-task language understanding benchmark.Advances in Neural Information
Processing Systems, 37:95266–95290, 2024.
[22] Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik
Narasimhan. Swe-bench: Can language models resolve real-world github issues?arXiv preprint
arXiv:2310.06770, 2023.
[23] Mike A Merrill, Alexander G Shaw, Nicholas Carlini, Boxuan Li, Harsh Raj, Ivan Bercovich, Lin
Shi, Jeong Yeon Shin, Thomas Walshe, E Kelly Buchanan, et al. Terminal-bench: Benchmarking
agents on hard, realistic tasks in command line interfaces.arXiv preprint arXiv:2601.11868,
2026.
[24] Hyunwoo Kim, Melanie Sclar, Xuhui Zhou, Ronan Bras, Gunhee Kim, Yejin Choi, and Maarten
Sap. Fantom: A benchmark for stress-testing machine theory of mind in interactions. In
Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing,
pages 14397–14413, 2023.
[25] Hainiu Xu, Runcong Zhao, Lixing Zhu, Jinhua Du, and Yulan He. Opentom: A comprehensive
benchmark for evaluating theory-of-mind reasoning capabilities of large language models. In
Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 8593–8623, 2024.
[26] Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang,
and Michael S. Bernstein. Generative agents: Interactive simulacra of human behavior. In
Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology,
UIST ’23. Association for Computing Machinery, 2023.
[27] Gati V Aher, Rosa I. Arriaga, and Adam Tauman Kalai. Using large language models to simulate
multiple humans and replicate human subject studies. In Andreas Krause, Emma Brunskill,
Kyunghyun Cho, Barbara Engelhardt, Sivan Sabato, and Jonathan Scarlett, editors,Proceedings
of the 40th International Conference on Machine Learning, volume 202 ofProceedings of
Machine Learning Research, pages 337–371. PMLR, 23–29 Jul 2023.
11

[28] Zhicheng Lin. Large language models as psychological simulators: A methodological guide.
Advances in Methods and Practices in Psychological Science, 9(1):25152459251410153, 2026.
[29] Weihong Qi, Fan Huang, Jisun An, and Haewoon Kwak. A cross-cultural comparison of
llm-based public opinion simulation: Evaluating chinese and us models on diverse societies.
arXiv preprint arXiv:2506.21587, 2025.
[30] Stephan Ludwig, Peter J Danaher, Xiaohao Yang, Yu-Ting Lin, Ehsan Abedin, Dhruv Grewal,
and Lan Du. Extracting consumer insight from text: A large language model approach to
emotion and evaluation measurement.arXiv preprint arXiv:2602.15312, 2026.
[31] Mengxin Wang, Dennis J Zhang, and Heng Zhang. Large language models for market research:
A data-augmentation approach.Marketing Science, 2026.
[32] Luke Hewitt, Ashwini Ashokkumar, Isaias Ghezae, and Robb Willer. Predicting results of social
science experiments using large language models.Preprint, 2024.
[33] Jacy Reese Anthis, Ryan Liu, Sean M Richardson, Austin C Kozlowski, Bernard Koch, James
Evans, Erik Brynjolfsson, and Michael Bernstein. Llm social simulations are a promising
research method.arXiv preprint arXiv:2504.02234, 2025.
[34] Ivan Zakazov, Mikolaj Boronski, Lorenzo Drudi, and Robert West. Assessing social align-
ment: Do personality-prompted large language models behave like humans?arXiv preprint
arXiv:2412.16772, 2024.
[35] Feng Xiao and XT XiaoTian Wang. Evaluating the ability of large language models to predict
human social decisions.Scientific Reports, 15(1):32290, 2025.
[36] Oliver Slumbers, Joel Z Leibo, and Marco A Janssen. Using large language models to simulate
human behavioural experiments: Port of mars.arXiv preprint arXiv:2506.05555, 2025.
[37] Ziyi Yang, Zaibin Zhang, Zirui Zheng, Yuxian Jiang, Ziyue Gan, Zhiyu Wang, Zijian Ling,
Jinsong Chen, Martz Ma, Bowen Dong, et al. Oasis: Open agent social interaction simulations
with one million agents.arXiv preprint arXiv:2411.11581, 2024.
[38] Xuhui Zhou, Hao Zhu, Leena Mathur, Ruohong Zhang, Haofei Yu, Zhengyang Qi, Louis-
Philippe Morency, Yonatan Bisk, Daniel Fried, Graham Neubig, et al. Sotopia: Interactive
evaluation for social intelligence in language agents.arXiv preprint arXiv:2310.11667, 2023.
[39] Jinfeng Zhou, Zheyu Chen, Shuai Wang, Quanyu Dai, Zhenhua Dong, Hongning Wang, and
Minlie Huang. Think socially via cognitive reasoning.arXiv preprint arXiv:2509.22546, 2025.
[40] EunJeong Hwang, Yuwei Yin, Giuseppe Carenini, Peter West, and Vered Shwartz. Infusing
theory of mind into socially intelligent llm agents.arXiv preprint arXiv:2509.22887, 2025.
[41] Marcel Binz, Elif Akata, Matthias Bethge, Franziska Brändle, Fred Callaway, Julian Coda-
Forno, Peter Dayan, Can Demircan, Maria K Eckstein, Noémi Éltet˝o, et al. A foundation model
to predict and capture human cognition.Nature, 644(8078):1002–1009, 2025.
[42] Ziyi Wang, Yuxuan Lu, Yimeng Zhang, Jing Huang, and Dakuo Wang. Customer-r1: Personal-
ized simulation of human behaviors via rl-based llm agent in online shopping.arXiv preprint
arXiv:2510.07230, 2025.
[43] Ziyi Wang, Yuxuan Lu, Yimeng Zhang, Jing Huang, and Dakuo Wang. Customer-r1: per-
sonalized simulation of human behaviors via rl-based llm agent in online shopping. InFirst
Workshop on Multi-Turn Interactions in Large Language Models.
[44] James Brand, Ayelet Israeli, and Donald Ngwe. Using llms for market research.Harvard
Business School Marketing Unit Working Paper, (23-062), 2023.
[45] Arya Agarwal. The silicon sample: Benchmarking synthetic users against human respondents
in market research.Available at SSRN 5835122, 2025.
12

[46] Yuzhe Yang, Yifei Zhang, Minghao Wu, Kaidi Zhang, Yunmiao Zhang, Honghai Yu, Yan Hu,
and Benyou Wang. Twinmarket: A scalable behavioral and social simulation for financial
markets.arXiv preprint arXiv:2502.01506, 2025.
[47] Nian Li, Chen Gao, Mingyu Li, Yong Li, and Qingmin Liao. Econagent: large language
model-empowered agents for simulating macroeconomic activities. InProceedings of the 62nd
annual meeting of the association for computational linguistics (volume 1: Long papers), pages
15523–15536, 2024.
[48] Yangyang Yu, Zhiyuan Yao, Haohang Li, Zhiyang Deng, Yuechen Jiang, Yupeng Cao, Zhi
Chen, Jordan Suchow, Zhenyu Cui, Rong Liu, et al. Fincon: A synthesized llm multi-agent
system with conceptual verbal reinforcement for enhanced financial decision making.Advances
in Neural Information Processing Systems, 37:137010–137045, 2024.
[49] Xuanbo Su, Wenhao Hu, Le Zhan, Yanqi Yang, and Leo Huang. Sell more, play less: Bench-
marking llm realistic selling skill.arXiv preprint arXiv:2604.07054, 2026.
[50] Yun-Shiuan Chuang, Ruixuan Tu, Chengtao Dai, Smit Vasani, Binwei Yao, Michael Henry
Tessler, Sijia Yang, Dhavan Shah, Robert Hawkins, Junjie Hu, et al. Debate: A large-scale
benchmark for role-playing llm agents in multi-agent, long-form debates.arXiv preprint
arXiv:2510.25110, 2025.
[51] Elinor Poole-Dayan, Jiayi Wu, Taylor Sorensen, Jiaxin Pei, and Michiel A Bakker. Benchmark-
ing overton pluralism in llms.arXiv preprint arXiv:2512.01351, 2025.
[52] Yao Dou, Michel Galley, Baolin Peng, Chris Kedzie, Weixin Cai, Alan Ritter, Chris Quirk,
Wei Xu, and Jianfeng Gao. Simulatorarena: Are user simulators reliable proxies for multi-turn
evaluation of ai assistants? InProceedings of the 2025 Conference on Empirical Methods in
Natural Language Processing, pages 35200–35278, 2025.
[53] Preethi Seshadri, Samuel Cahyawijaya, Ayomide Odumakinde, Sameer Singh, and Seraphina
Goldfarb-Tarrant. Lost in simulation: Llm-simulated users are unreliable proxies for human
users in agentic evaluations.arXiv preprint arXiv:2601.17087, 2026.
[54] Wenyue Hua, Lizhou Fan, Lingyao Li, Kai Mei, Jianchao Ji, Yingqiang Ge, Libby Hemphill,
and Yongfeng Zhang. War and peace (waragent): Large language model-based multi-agent
simulation of world wars.arXiv preprint arXiv:2311.17227, 2023.
[55] Chen Gao, Xiaochong Lan, Zhihong Lu, Jinzhu Mao, Jinghua Piao, Huandong Wang, Depeng
Jin, and Yong Li. S3: Social-network simulation system with large language model-empowered
agents.arXiv preprint arXiv:2307.14984, 2023.
[56] Jiakai Tang, Heyang Gao, Xuchen Pan, Lei Wang, Haoran Tan, Dawei Gao, Yushuo Chen,
Xu Chen, Yankai Lin, Yaliang Li, et al. Gensim: A general social simulation platform with
large language model based agents. InProceedings of the 2025 Conference of the Nations of
the Americas Chapter of the Association for Computational Linguistics: Human Language
Technologies (System Demonstrations), pages 143–150, 2025.
[57] Xinnong Zhang, Jiayu Lin, Xinyi Mou, Shiyue Yang, Xiawei Liu, Libo Sun, Hanjia Lyu, Yihang
Yang, Weihong Qi, Yue Chen, et al. Socioverse: A world model for social simulation powered
by llm agents and a pool of 10 million real-world users.arXiv preprint arXiv:2504.10157, 2025.
[58] Weize Chen, Yusheng Su, Jingwei Zuo, Cheng Yang, Chenfei Yuan, Chi-Min Chan, Heyang Yu,
Yaxi Lu, Yi-Hsin Hung, Chen Qian, et al. Agentverse: Facilitating multi-agent collaboration
and exploring emergent behaviors. InICLR, 2024.
[59] Qian Wang, Tianyu Wang, Zhenheng Tang, Qinbin Li, Nuo Chen, Jingsheng Liang, and
Bingsheng He. Megaagent: A large-scale autonomous llm-based multi-agent system without
predefined sops. InFindings of the Association for Computational Linguistics: ACL 2025,
pages 4998–5036, 2025.
[60] Jing Liu, Xinxing Ren, Yanmeng Xu, and Zekun Guo. Can ai automatically analyze public
opinion? a llm agents-based agentic pipeline for timely public opinion analysis.arXiv preprint
arXiv:2505.11401, 2025.
13

[61] Chen Gao, Xiaochong Lan, Nian Li, Yuan Yuan, Jingtao Ding, Zhilun Zhou, Fengli Xu, and
Yong Li. Large language models empowered agent-based modeling and simulation: A survey
and perspectives.Humanities and Social Sciences Communications, 11(1):1–24, 2024.
[62] Jiangjie Chen, Xintao Wang, Rui Xu, Siyu Yuan, Yikai Zhang, Wei Shi, Jian Xie, Shuang Li,
Ruihan Yang, Tinghui Zhu, et al. From persona to personalization: A survey on role-playing
language agents.Transactions on Machine Learning Research.
[63] James Bisbee, Joshua D Clinton, Cassy Dorff, Brenton Kenkel, and Jennifer M Larson. Synthetic
replacements for human survey data? the perils of large language models.Political Analysis,
32(4):401–416, 2024.
[64] Maarten Sap, Hannah Rashkin, Derek Chen, Ronan Le Bras, and Yejin Choi. Social iqa:
Commonsense reasoning about social interactions. InProceedings of the 2019 Conference on
Empirical Methods in Natural Language Processing and the 9th International Joint Conference
on Natural Language Processing (EMNLP-IJCNLP), pages 4463–4473, 2019.
[65] Seungbeen Lee, Seungwon Lim, Seungju Han, Giyeong Oh, Hyungjoo Chae, Jiwan Chung,
Minju Kim, Beong-woo Kwak, Yeonsoo Lee, Dongha Lee, et al. Do llms have distinct and
consistent personality? trait: Personality testset designed for llms with psychometrics. In
Findings of the Association for Computational Linguistics: NAACL 2025, pages 8397–8437,
2025.
[66] Min Zeng. Psychcounsel-bench: Evaluating the psychology intelligence of large language
models.arXiv preprint arXiv:2510.01611, 2025.
[67] Hongzhan Chen, Hehong Chen, Ming Yan, Wenshen Xu, Gao Xing, Weizhou Shen, Xiaojun
Quan, Chenliang Li, Ji Zhang, and Fei Huang. Socialbench: Sociality evaluation of role-playing
conversational agents. InFindings of the Association for Computational Linguistics: ACL 2024,
pages 2108–2126, 2024.
[68] Giovanni Franco Gabriel Marraffini, Andrés Cotton, Noe Fabian Hsueh, Axel Fridman, Juan
Wisznia, and Luciano Del Corro. The greatest good benchmark: Measuring llms’ alignment
with utilitarian moral dilemmas. InProceedings of the 2024 Conference on Empirical Methods
in Natural Language Processing, pages 21950–21959, 2024.
[69] Anonymous. Social-r1: Enhancing social intelligence in LLMs through human-like reinforced
reasoning. InSubmitted to The Fourteenth International Conference on Learning Representa-
tions, 2025. under review.
[70] Xixian Yong, Jianxun Lian, Xiaoyuan Yi, Xiao Zhou, and Xing Xie. Motivebench: How far
are we from human-like motivational reasoning in large language models?arXiv preprint
arXiv:2506.13065, 2025.
[71] Sahand Sabour, Siyang Liu, Zheyuan Zhang, June Liu, Jinfeng Zhou, Alvionna Sunaryo, Tatia
Lee, Rada Mihalcea, and Minlie Huang. Emobench: Evaluating the emotional intelligence
of large language models. InProceedings of the 62nd Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers), pages 5986–6004, 2024.
[72] Zhaolu Kang, Junhao Gong, Jiaxu Yan, Wanke Xia, Yian Wang, Ziwen Wang, Huaxuan Ding,
Zhuo Cheng, Wenhao Cao, Zhiyuan Feng, et al. Hssbench: Benchmarking humanities and
social sciences ability for multimodal large language models.arXiv preprint arXiv:2506.03922,
2025.
[73] Dan Hendrycks, Collin Burns, Steven Basart, Andrew Critch, Jerry Li, Dawn Song, and Jacob
Steinhardt. Aligning {ai} with shared human values. InInternational Conference on Learning
Representations, 2021.
[74] Yunfan Shao, Linyang Li, Junqi Dai, and Xipeng Qiu. Character-llm: A trainable agent for
role-playing.arXiv preprint arXiv:2310.10158, 2023.
14

[75] Xintao Wang, Yunze Xiao, Jen-tse Huang, Siyu Yuan, Rui Xu, Haoran Guo, Quan Tu, Yaying
Fei, Ziang Leng, Wei Wang, et al. Incharacter: Evaluating personality fidelity in role-playing
agents through psychological interviews. InProceedings of the 62nd annual meeting of the
association for computational linguistics (volume 1: Long papers), pages 1840–1873, 2024.
[76] Vinay Samuel, Henry Peng Zou, Yue Zhou, Shreyas Chaudhari, Ashwin Kalyan, Tanmay
Rajpurohit, Ameet Deshpande, Karthik R Narasimhan, and Vishvak Murahari. PersonaGym:
Evaluating persona agents and LLMs. In Christos Christodoulopoulos, Tanmoy Chakraborty,
Carolyn Rose, and Violet Peng, editors,Findings of the Association for Computational Lin-
guistics: EMNLP 2025, pages 6999–7022, Suzhou, China, November 2025. Association for
Computational Linguistics.
[77] Lawrence J. Klinkert, Steph Buongiorno, and Corey Clark. Evaluating the efficacy of llms
to emulate realistic human personalities.Proceedings of the AAAI Conference on Artificial
Intelligence and Interactive Digital Entertainment, 20(1):65–75, Nov. 2024.
[78] Keane Ong, Wei Dai, Carol Li, Dewei Feng, Hengzhi Li, Jingyao Wu, Jiaee Cheong, Rui
Mao, Gianmarco Mengaldo, Erik Cambria, et al. Human behavior atlas: Benchmarking unified
psychological and social behavior understanding.arXiv preprint arXiv:2510.04899, 2025.
[79] Xinyi Mou, Jingcong Liang, Jiayu Lin, Xinnong Zhang, Xiawei Liu, Shiyue Yang, Rong Ye, Lei
Chen, Haoyu Kuang, Xuanjing Huang, and Zhongyu Wei. AgentSense: Benchmarking social
intelligence of language agents through interactive scenarios. In Luis Chiruzzo, Alan Ritter, and
Lu Wang, editors,Proceedings of the 2025 Conference of the Nations of the Americas Chapter
of the Association for Computational Linguistics: Human Language Technologies (Volume
1: Long Papers), pages 4975–5001, Albuquerque, New Mexico, April 2025. Association for
Computational Linguistics.
[80] Noah Wang, Z.y. Peng, Haoran Que, Jiaheng Liu, Wangchunshu Zhou, Yuhan Wu, Hongcheng
Guo, Ruitong Gan, Zehao Ni, Jian Yang, Man Zhang, Zhaoxiang Zhang, Wanli Ouyang, Ke Xu,
Wenhao Huang, Jie Fu, and Junran Peng. RoleLLM: Benchmarking, eliciting, and enhancing
role-playing abilities of large language models. In Lun-Wei Ku, Andre Martins, and Vivek
Srikumar, editors,Findings of the Association for Computational Linguistics: ACL 2024, pages
14743–14777, Bangkok, Thailand, August 2024. Association for Computational Linguistics.
[81] Denis Emelin, Ronan Le Bras, Jena D Hwang, Maxwell Forbes, and Yejin Choi. Moral stories:
Situated reasoning about norms, intents, actions, and their consequences. InProceedings of the
2021 Conference on Empirical Methods in Natural Language Processing, pages 698–718, 2021.
[82] Yuyan Chen, Songzhou Yan, Sijia Liu, Yueze Li, and Yanghua Xiao. Emotionqueen: A
benchmark for evaluating empathy of large language models. InFindings of the Association for
Computational Linguistics ACL 2024, pages 2149–2176, 2024.
[83] Ziyi Liu, Abhishek Anand, Pei Zhou, Jen-tse Huang, and Jieyu Zhao. Interintent: Investigating
social intelligence of llms via intention understanding in an interactive game context. In
Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing,
pages 6718–6746, 2024.
[84] Kanishk Gandhi, Jan-Philipp Fränken, Tobias Gerstenberg, and Noah Goodman. Understanding
social reasoning in language models with language models.Advances in Neural Information
Processing Systems, 36:13518–13529, 2023.
[85] Jessica Maria Echterhoff, Yao Liu, Abeer Alessa, Julian McAuley, and Zexue He. Cognitive
bias in decision-making with llms. InFindings of the association for computational linguistics:
EMNLP 2024, pages 12640–12653, 2024.
[86] Jingru Jia, Zehua Yuan, Junhao Pan, Paul E McNamara, and Deming Chen. Decision-making
behavior evaluation framework for llms under uncertain context.Advances in neural information
processing systems, 37:113360–113382, 2024.
[87] Kazutoshi Shinoda, Nobukatsu Hojo, Kyosuke Nishida, Saki Mizuno, Keita Suzuki, Ryo
Masumura, Hiroaki Sugiyama, and Kuniko Saito. Tomato: Verbalizing the mental states of
role-playing llms for benchmarking theory of mind. InProceedings of the AAAI Conference on
Artificial Intelligence, volume 39, pages 1520–1528, 2025.
15

[88] James W A Strachan, Dalila Albergo, Giulia Borghini, Oriana Pansardi, Eugenio Scaliti, Saurabh
Gupta, Krati Saxena, Alessandro Rufo, Stefano Panzeri, Guido Manzi, et al. Testing theory of
mind in large language models and humans.Nature Human Behaviour, 8(7):1285–1295, 2024.
[89] Yufan Wu, Yinghui He, Yilin Jia, Rada Mihalcea, Yulong Chen, and Naihao Deng. Hi-tom: A
benchmark for evaluating higher-order theory of mind reasoning in large language models. In
Findings of the Association for Computational Linguistics: EMNLP 2023, pages 10691–10706,
2023.
[90] Haojun Shi, Suyu Ye, Xinyu Fang, Chuanyang Jin, Leyla Isik, Yen-Ling Kuo, and Tianmin Shu.
Muma-tom: Multi-modal multi-agent theory of mind. InProceedings of the AAAI Conference
on Artificial Intelligence, volume 39, pages 1510–1519, 2025.
[91] Zizhou Liu, Ziwei Gong, Lin Ai, Zheng Hui, Run Chen, Colin Wayne Leach, Michelle R Greene,
and Julia Hirschberg. The mind in the machine: A survey of incorporating psychological theories
in llms.arXiv preprint arXiv:2505.00003, 2025.
[92] Yiqun Zhang, Xiaocui Yang, Xingle Xu, Zeran Gao, Yijie Huang, Shiyi Mu, Shi Feng, Daling
Wang, Yifei Zhang, Kaisong Song, et al. Affective computing in the era of large language
models: A survey from the nlp perspective.arXiv preprint arXiv:2408.04638, 2024.
[93] Lisa P. Argyle, Ethan C. Busby, Nancy Fulda, Joshua R. Gubler, Christopher Rytting, and David
Wingate. Out of one, many: Using language models to simulate human samples.Political
Analysis, 31(3):337–351, 2023.
[94] Erving Goffman.The Presentation of Self in Everyday Life. Doubleday, 1959.
[95] Pierre Bourdieu.Distinction: A Social Critique of the Judgement of Taste. Harvard University
Press, 1984.
[96] Daniel Kahneman and Amos Tversky. Prospect theory: An analysis of decision under risk.
Econometrica, 47(2):263–291, 1979.
16

A Criteria-Weighted Micro-Average
Table 5 reports the criteria-weighted micro-average as a secondary metric. For each model, the micro
value is 1 4 P s∈S P i coveredi,sP i totali,s , i.e., each section is averaged by total criterion count rather than topic count. Deviations from the balanced (macro) average reported in Table 4 are at most 1.0 point for
all 13 models, and the broad leaderboard tiers are unchanged. The paper’s conclusions are therefore
insensitive to this metric choice.
Table 5: Macro (balanced, 25% per family) vs. criteria-weighted micro average. Differences are ≤1.0
point for all models; broad leaderboard tiers are preserved.
Model Macro (%) Micro (%) ∆
Gemini-3.1-Pro 47.8 47.1−0.7
Gemini-3-Flash 46.6 45.8−0.8
Grok-4.2 44.9 44.2−0.7
Kimi-K2.5 43.5 42.5−1.0
Qwen3.5-397B 43.4 42.5−0.9
DeepSeek-V3 42.9 41.9−1.0
Doubao-Seed-1.8 42.4 42.0−0.4
GPT-5.2 35.8 35.0−0.9
MiniMax-M2.5 35.2 34.4−0.8
Claude-Opus-4.6 32.8 32.4−0.4
MiMo-V2.5-Pro 32.3 33.1+0.8
Claude-Sonnet-4.6 30.8 30.3−0.5
GPT-4o 29.7 29.4−0.3
B Error Taxonomy
Table 6 gives the heuristic error-taxonomy distribution over 197,790 missed criteria across all
13 generators. Categories are assigned by parsing judge explanations for keyword patterns, then
validated on a 50-sample manual audit (inter-rater agreement on category assignment was >95% on
the audit subset; the keyword parsing on the full 197,790 was not human-validated end-to-end). The
percentages should therefore be read as descriptive patterns in judge-explanation text, not as causal
failure-mechanism counts.
Table 6: Error taxonomy across all 13 generators (197,790 total misses).
Error type Count %
Missing specific reaction trigger (generic content) 88,061 44.5
Missing keyword vocabulary (T2) 21,521 10.9
Missing negative aspect (T4) 20,438 10.3
Meme repetition without pragmatic transfer 17,375 8.8
Missing positive aspect (T3) 14,618 7.4
Opposite valence (praise↔criticism) 14,112 7.1
Missing flashpoint trigger name (T1) 14,066 7.1
Too generic / surface-level 6,998 3.5
Emotion match, wrong object 372 0.2
Factual error in comment 229 0.1
C Why pointwise binary?
A natural question is whether the auditable pointwise judge is worth the engineering. We test the
alternatives on a controlled 120-pair similarity benchmark (60 paraphrase positives, 30 random
negatives, 30 hard negatives) constructed from released criterion examples. For each method, we
score all pairs and compute AUC-ROC and best-threshold F1. The identical 0.667 Best-F1 values
indicate a degenerate optimum: the best threshold predicts every pair as positive on the balanced
60/60 set.
17

Table 7: Similarity-detection performance on 120 reaction-pair instances (60 positive, 60 negative).
All four cheap unsupervised similarity baselines reach the trivial-baseline value in theBest F1column
(0.667 = 2/3): at the optimal threshold they collapse to “predict every pair as positive,” which on a
60/60 split gives P= 0.5 , R= 1.0, F1 = 0.667. LSA uses TF-IDF/SVD embeddings and cosine
similarity. These baselines do not provide a usable replacement for pointwise judging.
Method AUC-ROC Best F1
Token Jaccard (jieba-segmented) 0.625 0.667
Character N-gram Jaccard (n= 2) 0.618 0.667
GPT-token Jaccard (cl100k_base) 0.604 0.667
LSA embedding cosine (TF-IDF/SVD) 0.608 0.667
Unsupervised similarity metrics fail for two reasons specific to consumer-reaction text: (i) paraphrase-
positive pairs can share few surface units (e.g. “feels like a corporate apology” vs. “reads like a PR
statement”); (ii) hard-negative pairs can share many units but disagree on the criterion (e.g. “reduced
fireworks count” as praise vs. “fireworks were the problem to begin with” as criticism). GPT-token
overlap and LSA embeddings slightly raise AUC over raw surface overlap, but still collapse to the
all-positive best-F1 threshold. This rules out cheap unsupervised similarity as a replacement for
pointwise judging, while leaving learned cross-encoders as a possible future comparison.
But once a similaritymustbe LLM-based, the next question is whetherholisticLLM-as-Judge (one
prompt, one fuzzy quality score) is sufficient. On a 100+ criterion calibration set from 10 random
topics, pointwise binary judging reaches92.1%three-judge agreement, while holistic LLM-as-Judge
on the same data reaches only65.8%—a gap of nearly 30 points. Every additional point of judge
disagreement contaminates downstream cross-model rankings, since the same generator can win or
lose by judge variance alone. Pointwise binary judging is therefore the minimum sufficient design.
Why not a human-expert ceiling?We do not treat human expert prediction as the target ceiling
for CONSUMERSIMBENCH. The benchmark target is realized public discourse: comments that
real consumers actually produced after seeing the event. Those comments can be surprising, messy,
or difficult to infer, but their difficulty is exactly why a marketing-facing forecasting benchmark
is needed. A PR or marketing expert baseline would be a useful diagnostic for expert foresight
under the same brief, but it would not change the target definition. The goal is to recover concrete
flashpoints and criticism vectors that later become salient in public discussion, including cases that
human experts may also miss.
D Construction, Generation, and Judge Prompts
Criteria drafting prompt.The operational drafting prompt was written in Chinese; below we
give an abbreviated English translation. The drafting model receives topic metadata, an objective
event description used as an anti-leakage reference, and filtered source reactions for the topic. It is
instructed to produce benchmark ground truth as unambiguous scoring criteria rather than summaries.
You are a professional social-media public-opinion analyst. Your
analysis will be used as ground truth for a public-reaction
forecasting benchmark. The output must consist of unambiguous
scoring criteria. Each criterion must have a clear boundary,
positive examples, negative examples, and a one-sentence judgment
rule, so that different raters can make consistent yes-no decisions.
Given the topic metadata, event description, and filtered source
reactions, identify: (1) up to five emotion keywords with their
emotion targets; (2) up to four positive aspects and up to four
negative aspects; and (3) up to two sentiment flashpoints. Each
item must be atomic and supported by the source reactions.
Anti-leakage rule: a criterion must capture user attitude, emotion,
or viewpoint, not merely restate facts already present in the event
description. If a generated comment only repeats names, times,
places, actions, or outcomes from the event description without an
18

attitudinal increment, it should not receive credit. Do not create
a criterion if the source reactions do not provide enough support.
Return JSON with the four sections. For every criterion, include a
name, definition, positive examples, negative examples, and judgment
rule.
Topic filtering prompt.Before criterion drafting, we use an LLM filter to retain hot topics related
to brands, products, consumer behavior, or marketing-relevant service experiences. The operational
prompt was written in Chinese; below is an abbreviated English translation.
Judge whether the following trending topic is related to brands,
products, or commercial marketing.
Relevant types include: (1) brand events, such as releases,
collaborations, controversies, or marketing campaigns; (2) product
discussions, such as reviews, recommendations, warnings, or feature
discussions; (3) consumer topics, such as consumption trends,
shopping experience, and value-for-money discussion; (4) influencer
commerce, such as creator recommendations, livestream commerce, and
influencer-associated products; and (5) service experiences, such as
restaurants, travel, medical, or other consumer-service experiences.
Exclude topics that are pure entertainment gossip without brand
relevance, political news, sports events unless brand sponsorship is
involved, and pure knowledge explainers.
Principle: prefer recall over precision; do not miss potentially
relevant topics.
Trending topic: {topic}
Return JSON only: {"related": true/false, "type": "...",
"brand_entity": "...", "reason": "short reason"}.
Semantic judging.The judgment rules will not penalize models that capture a reaction’s se-
mantic essence with slight paraphrasing. This is because the judge prompt encodes five explicit
semantic-equivalence rules, including emotion synonym/hierarchy matching, object-anchor matching,
compound-emotion inclusion, strength versus factual statement, and meme object-transfer. A criterion
such as “$2,000 starting-price leak” is satisfied by any specific anchor in its judgment-rule range
(“2,000 dollars,” “around 2k,” “¥14,000+”), but not by generic phrasings such as “it’ll be expensive”.
The latter does not reproduce the specific public-discourse anchor that drove the topic. The role of
the lexical anchor is to distinguish a model that anticipateswhich framing the public actually chose
from one that emits any plausibly relevant comment; our held-out judgment-rule ablation and the
per-criterion anatomy boxes in Appendix K document this distinction.
Generator prompt.
You are simulating realistic public reactions to a trending
topic on Chinese social media. Topic: {topic_keyword} | Event:
{event_description}. Generate {k} diverse, realistic comments
that Chinese social-media users would post. Each should reflect
a distinct perspective, emotion, or reaction. Write in natural
Chinese social-media language.
Comments per topic follow k= min(30,max(10,|C i|)), where |Ci| is the number of criteria for
topici.
Judge prompt.
For each criterion, the judge receives the topic, the generated
comments truncated to 3,600 characters, and the five-field criterion
(name, definition, positive examples, negative examples, judgment
rule) together with five explicit semantic-equivalence rules for
Chinese: (1) emotion synonyms, (2) object matching, (3) compound
inclusion, (4) strength vs. factual, (5) meme object-transfer. To
keep each pointwise call bounded, the prompt includes up to five
19

positive examples and three negative examples, each shortened to the
first 120 characters; the release JSONL retains the full criterion
metadata. The judge returns YES/NO with a short explanation. Full
prompts are released with the benchmark.
E Construction Hardening Details
We manually check the drafted criteria and harden four recurring failure modes: event-restatement
leakage, semantic duplication, over-pruning, and judge-fragile meme points. We use cosine similarity
and LLM supervision to merge similar topics and criteria; drop criteria that collapse to the event
description; verify within-topic independence with an LLM-assisted check; and audit pruned items
so that meaningful but non-trivial criteria are restored rather than discarded. The hardening process
ensures that simply repeating the task description earns no credit.
Meme-style criteria are a recurring failure mode for judges because a model can receive credit by
simply repeating the meme template. We therefore rejudge 282 meme-like criteria across 225 topics,
crediting only cases where the meme is transferred to anew object or sceneand forms a genuine
second-order creation. For a real benchmark item,“School isn’t basic, dorm isn’t basic either”,
(i)“Face isn’t basic, body isn’t basic either, ability is even less basic”transfers the template to
a person and counts as a hit;(ii)“Dorm isn’t basic, bathroom isn’t basic either”stays inside the
original school/dorm domain and does not count;(iii)“Born not to be a basic model”carries a
similar meaning but does not use the structural template and also does not count.
To deal with over-pruning, we manually audit the pruned criteria. We restore 28 over-pruned criteria
and revise another 87 into new ones. Table 8 shows real construction-log examples. We report only
derived reaction signals, not raw user comments.
Table 8: Examples of criterion hardening.
Topic Failure mode Draft signal Hardened reaction signal
Aaaaapple apple
juice police report
Event-restatement
leakage
The brand formally filed a
police report.
Replaced by stance-bearing re-
actions about legal-rights legiti-
macy, brand sincerity, celebrity
effect, and heartache for the as-
sociated public figure.
Apple joins Red-
Note
Event-restatement
leakage
Apple’s official account
joined RedNote.
Replaced by account-
authenticity reversal and
intellectual-property compli-
ance, which require a user stance
beyond the join fact.
Apple Watch prod-
uct review
Semantic duplication
and coarse labels
Repeated generic criteria
such as anxiety, health-
management value, aes-
thetic value, app ecosys-
tem, durability, and com-
fort.
Split into higher-resolution sig-
nals about the “beautiful but use-
less” reversal, health-data visual-
ization, abnormal battery drain,
subscription-gated software, ac-
cessory quality, and resale-value
reasoning.
iPhone 17 hands-
on
Low-specificity
launch hype
First-sale purchase enthusi-
asm.
Replaced by concrete discourse
anchors such as eSIM-only
policy, thinness versus bat-
tery capacity, durability con-
cerns, purchase-channel advan-
tage, and launch-policy confu-
sion.
F Extended Limitations
This appendix expands on the caveats summarized in §6.
20

(L1) LLM-judge bias and calibration scope.The three-judge calibration (§5.3) and the three-
annotator human audit provide evidence that the pointwise judge is reliable on a targeted calibration
slice. This slice is designed as a judge-sensitivity stress test: criterion-level labels are compared across
GPT, Gemini, Claude, and independent human-majority labels, rather than only by the leaderboard
judge. The 3,600-character truncation reduces gross length bias, and criterion-specific definitions,
examples, and negative examples reduce style-based drift. We therefore treat remaining judge
ambiguity as a small semantic-boundary issue, not as a dominant source of the large model failures
reported in the leaderboard.
(L2) Representative platform and portability.The current release of CONSUMERSIMBENCH
is built on Chinese RedNote (Xiaohongshu), a major consumer-facing UGC platform with 300M+
monthly active users and dense lifestyle, brand, product, entertainment, and public-event discourse.
This makes RedNote a representative and practically important setting for consumer-behavior sim-
ulation. Many consumer reactions—price sensitivity, authenticity concerns, disappointment with
over-marketing, praise for emotional value, criticism of service or design—are cross-platform phe-
nomena. RedNote is also a demanding testbed: compared with many short-form platforms, its
discourse often contains richer meme reuse, irony, self-presentation, and mixed affect, making it a
strong stress test for consumer-reaction modeling. As a portability check, Appendix G instantiates
the same construction on 100 English YouTube trending videos and observes a similar section-wise
difficulty pattern. Future platform-specific releases can test how the same construction transfers to
X, Reddit, B2B marketing, or other cultural settings, but CONSUMERSIMBENCHalready covers a
broad, commercially important consumer-reaction regime. Given the large gap to ceiling in Table 4,
we view platform extension as an important future direction rather than the dominant explanation for
current model failures.
(L3) Temporal contamination.Source topics were surfaced between March and September 2025.
Continuous pretraining or RLHF on newer frontier models may have ingested public traces of some
events, so we do not claim contamination-free zero-shot forecasting for every proprietary model.
However, seeing an event or scattered original comments is not enough to solve CONSUMERSIM-
BENCH. The model must compress its knowledge into a limited set of representative comments,
while the score is computed against abstracted reaction criteria distilled from the full public-discourse
evidence and hardened by our rules. These criteria are not raw comments copied into the prompt,
and they remain hidden unless the benchmark itself leaks. Thus, contamination can still affect scores
and rankings, but success requires recovering the aggregate reaction structure, such as stance, target,
and judgment-rule match, rather than recalling isolated posts. We release timestamps and topic
provenance to support future temporal splits and post-cutoff held-out evaluations.
(L4) LLM-assisted construction at benchmark scale.Criterion drafting and initial judgments
are LLM-assisted, followed by hardening, pruning, spot-checks, and human audit. This hybrid
construction is the scalable design choice that makes a 23,122-criterion benchmark feasible while
preserving inspectability. The human audit in §5.3 compares pointwise judge decisions against
independent human-majority labels on a held-out calibration slice, and the release includes every
criterion’s five-field metadata, provenance, and judgment rule so that users can inspect, filter, or
extend the benchmark.
(L5) Endpoint coverage not all possible reactions.CONSUMERSIMBENCHevaluates whether
generated comments recover the concrete reaction points that actually surfaced in public discourse.
This is the marketing-relevant target, where teams need to anticipate which criticisms, praise targets,
emotional keywords, and flashpoints become salient enough to shape the public conversation before
launching an official post or advertisement. The benchmark therefore does not credit every plausible
but unobserved reaction equally, and it does not model the temporal process by which early reactions
shape later ones. Dynamic opinion-diffusion simulation is complementary to the present benchmark.
G Second-Platform YouTube Pilot
To test whether the construction procedure is portable beyond RedNote, we run a small second-
platform pilot on English YouTube. We select 100 consumer-facing videos from the public Global
YouTube Trending Dataset (2025 entries; English-speaking regions US/GB/CA/AU), balanced across
21

14 YouTube categories, and fetch the top 300 public comments per video through the official YouTube
Data API. We then apply the same criterion-construction recipe: comments are abstracted into atomic
reaction criteria with definitions, positive examples, negative examples, and judgment rules. The
resulting pilot contains 1,508 criteria (mean 15.1 per topic) across 100 videos.
We evaluate the pilot with the same open-ended comment-generation interface and GPT-5.2 pointwise
judge, using English prompts. The pilot is not part of the released leaderboard, but it provides a
direct portability check. When moved from RedNote to English YouTube, the same endpoint-reaction
formulation still exposes large gaps in recovering concrete public-discourse reactions. The section
pattern also mirrors the main benchmark: positive aspects are easiest, while flashpoints and negative
aspects remain much harder (Figure 6; Table 9).
0 10 20 30 40 50
Overall score (%)
1. Gemini-3.1-Pro
2. Gemini-3-Flash
3. Grok-4.2
4. Qwen3.5-397B
5. Doubao-Seed-2.0-Pro
6. MiMo-V2.5-Pro
7. GPT-5.2
8. Kimi-K2.5
9. DeepSeek-V3
10. MiniMax-M2.5
11. GPT-4o
48.3
47.2
44.7
43.4
42.6
42.1
40.7
40.6
35.8
34.4
32.5
A  YouTube Pilot Leaderboard
T1 T2 T3+ T3-
0
10
20
30
40
50
60
70
Score (%)
B  Same Section Pattern
21.5
63.0
68.8
40.0
18.6
60.7
67.2
34.4
14.5
52.4
63.9
32.0
T op-1
T op-5 mean
GPT-5.2
Positive aspects remain easiest; flashpoints remain the hardest family.
Figure 6: Second-platform YouTube pilot. Left: overall lollipop leaderboard on 100 English trending
videos. Right: section-wise pattern under the same endpoint-reaction protocol.
Table 9: Second-platform YouTube pilot on 100 English trending videos and 1,508 criteria. Scores are
macro-averaged across topics under the same open-ended generation and pointwise judging protocol.
Model Overall T1 T2 T3+ T3-
Gemini-3.1-Pro 48.3 21.5 63.0 68.8 40.0
Gemini-3-Flash 47.2 21.2 60.3 71.0 36.2
Grok-4.2 44.7 18.5 64.4 69.7 26.1
Qwen3.5-397B 43.4 15.9 57.2 63.7 36.7
Doubao-Seed-2.0-Pro 42.6 15.9 58.6 62.7 33.1
MiMo-V2.5-Pro 42.1 17.8 55.4 66.2 28.9
GPT-5.2 40.7 14.5 52.4 63.9 32.0
Kimi-K2.5 40.6 15.4 53.5 60.7 32.9
DeepSeek-V3 35.8 12.5 45.8 55.5 29.5
MiniMax-M2.5 34.4 11.7 45.2 57.4 23.4
GPT-4o 32.5 10.2 43.3 55.1 21.3
H Human Audit Protocol
The human audit in §5.3 was designed to validate pointwise judge labels rather than to measure
human forecasting ability. We sampled 100+ criterion-level items from 10 random topics, with the
topic, event description, generated comments, and five-field criterion shown to each annotator. Three
trained annotators independently assigned their own yes/no label indicating whether the generated
comments satisfy the criterion. Each item also allowed an optional uncertainty flag for boundary
cases. We then compared the frozen judge label with the human-majority label.
Annotators first completed a small calibration set with reference answers, then annotated fixed,
independently shuffled versions of the formal audit set. The released annotation package includes the
exact item files, annotation guidelines, exported anonymized labels, analysis script, and the single-
file HTML annotation interface used in the study. The interface records only item-level decisions,
22

timestamps, and optional uncertainty flags; it does not collect demographic, medical, behavioral, or
other personal information from annotators. The audit was not run through a public crowdworking
marketplace. Compensation and participation followed the applicable local/institutional protocol
for this low-risk annotation task, and the released materials exclude payment records or identifying
information to preserve anonymity.
I Reproducibility
All leaderboard evaluations use the same harness and fixed GPT-5.2 judge. Single generation call per
topic (no best-of-n); generator temperature 0.7, max 4,096 tokens, the requested number of comments
is k= min(30,max(10,|C i|)). Judge temperature 0, max 4,096 tokens, one API call per atomic
criterion. Total API cost is ∼$2,500 across 13 generators and the judge. Wall-clock runtime for the
main sweep is ∼48 hours at 30 point workers × 8 topic workers. Scripts, config, and prompts are
included in the release.
J Theoretical Foundations of the CONSUMERSCF Framework
SCF (Strategy-Capital-Framing) is a classical consumer psychology framework that integrates three
complementary social psychology theories to guide consumer behavior simulation.
Strategy (S): Self-Presentation Theory.Drawing from Goffman’s dramaturgical analysis [94], we
model consumers as strategic actors who manage impressions through their public statements. Key
strategies include:
•Ingratiation: Expressing positive opinions to gain social approval
•Intimidation: Asserting expertise or status through criticism
•Supplication: Seeking sympathy through victimhood narratives
•Exemplification: Demonstrating moral values through consumption choices
Capital (C): Cultural Capital Theory.Following Bourdieu [95], we analyze consumers’ deployment
of various capital types:
•Economic capital: References to price, value, affordability
•Cultural capital: Displays of taste, aesthetics, expertise
•Social capital: Name-dropping, community belonging
•Moral capital: Ethical consumption, environmental consciousness
Framing (F): Behavioral Economics.Building on Prospect Theory [ 96], we attend to how con-
sumers frame information:
•Gain framing: Emphasizing benefits and positive outcomes
•Loss framing: Highlighting risks, regrets, or missed opportunities
•Reference points: Comparisons to expectations, competitors, past experiences
Direct-generation prompt.The ablation in §5.2 used the following instruction before the standard
generation request. The operational prompt was written in Chinese; we show an English translation
here. The model was asked to perform the analysis internally and output only comments:
You are a real social-media user. Given the topic and event
description, internally perform a Strategy–Capital–Framing analysis,
but output only comments, not the analysis. For Strategy, consider
why different users publicly participate: self-presentation through
knowledge, taste, expertise, lived experience, or group identity;
seeking resonance by linking the event to personal emotions,
grievances, expectations, or anxiety; criticism or complaint about
unreasonable, fake, awkward, or conflicted details; value signaling
around morality, fairness, identity, stance, or boundaries; and
23

meme-like joking through sarcasm, platform slang, remixing, or
secondary creation. For Capital, cover possible identity and
resource signals rather than generic emotion: cultural capital
(aesthetic taste, knowledge, expertise, familiarity with the work,
brand, or industry), social capital (fandom, city, profession,
consumer group, or shared-experience belonging), economic capital
(price sensitivity, value for money, consumption ability, budget
pressure, expensive/cheap/worth-it judgments), and moral capital
(empathy, justice, environmental concern, public good, respect for
labor, anti-routine sentiment). For Framing, vary how users package
the event: gain frames, loss frames, reference-point comparisons,
identity frames, and spreadability frames that identify which
details will be screenshotted, retold, memed, debated, or remixed.
Generate the requested number of realistic comments, each 20–100
Chinese characters. Make comments concrete by using names, scenes,
actions, prices, time, relationships, contrasts, or controversy
points from the event; make comments clearly different rather than
paraphrases; include support, skepticism, joking, empathy, extra
information, personal experience, or risk warnings where natural;
make them sound like casual user comments rather than analysis
reports, and do not use the terms Strategy, Capital, or Framing.
K Case Study I: iPhone 17 Hands-On (Single-Model Per-Criterion Audit)
This case study examines a single benchmark instance under the leaderboard’s #1 model (Gemini-
3.1-Pro), exhaustively annotating every ground-truth criterion with a ✓/✗and a pointer to the specific
generated comment that satisfies it. The topic isiPhone 17 Hands-On: a high-engagement consumer-
tech thread with 68 atomic criteria (T1=14, T2=24, T3=12, T4=18) drawn from real RedNote
reactions, and a generation budget of 20 comments. With full event briefing in the prompt, a model
must anticipatewhich specific reaction vectors will dominate the public discussion—the difference
between “Apple released a phone” and “the rumored $2,000 starting price, two-tone seam aesthetic,
and foldable-roadmap lag are the three vectors that will set the public mood”—rather than merely
produce plausible commentary about a phone launch.
Headline scores on this topic.Final 25.7%, decomposed as T1 = 1/14 (7%), T2 = 9/24 (37%), T3
= 3/12 (25%), T4 = 6/18 (33%). The model is fluent and emotionally varied, but its T1 coverage
collapses, missing 13 of 14 flashpoints. This single instance reproduces, locally, the asymmetric-
failure pattern observed across the full benchmark.
Topic and event description (the prompt the model receives).Apple is preparing a launch event
for the iPhone 17 series. Industry analysts and online leaks indicate hardware upgrades across the
lineup: a 24 MP front camera on all models; a 48 MP telephoto lens on the Pro variants; 12 GB
unified memory; the new A19 and A19 Pro chips on TSMC’s 3 nm process. High-refresh-rate displays
are expected across the line, with possible improvements to battery life and charging speed. Event
date rumored for September.
Sample generated comments (translated verbatim; 8 of 20).
C1.12 GB unified RAM across the line? Apple’s finally being generous! Used to be so
stingy. Now I won’t have to worry about background apps getting killed. Speaking as an
iPhone 13 holdout—this time I really am ready to upgrade.
C2.The base model finally gets a high-refresh display? In what era? Even budget Android
phones have had this for years; Apple really squeezes feature upgrades drop by drop. But
better late than never—hopefully no more 60 Hz eye-strain.
C4.A19 and A19 Pro on TSMC’s 3 nm process—performance will obviously be top-tier.
But honestly, the A-series chips have been over-spec’d for a while. What I actually care about
is whether the thermals can keep up; don’t want gameplay throttling and screen-dimming
again.
C7.Battery and fast-charge upgrades are rumored, but Apple’s “fast charging” is what it
is—reaching 40 W would be a miracle. Domestic Android phones start at 120 W. Apple
24

really needs to step up here.
C9.Looking at the renderings and so-called hands-on photos online, the appearance basically
hasn’t changed—same body, new color, sold for another year. Phones have hit a plateau;
even Apple can’t produce anything visually new anymore.
C12.RAM is going up, but what about storage? Don’t tell me the base model still starts at
128 GB. A few WeChat groups and games and you’re full. 256 GB minimum is the only
configuration that makes sense in 2025.
C16.Complain all you want, but you’ll buy it anyway. Full-stack Apple users have nowhere
to go—Mac, iPad, Watch all locked together. As long as iPhone 17 doesn’t crash and burn,
of course we’ll upgrade. This is what ecosystem lock-in looks like.
C19.Whatever the chip and camera, can they please fix the signal first? Step into an elevator
or a parking garage and lose service. Try scanning a shared bike and it won’t read.Thisis
the daily-use pain point that actually matters.
The output reads natural, varied in stance (early-adopter, fence-sitter, holdout, ecosystem-trapped
pragmatist), and surfaces several legitimate reactions: innovation fatigue, surprise at the high-refresh
upgrade, charging-speed grievance, signal-quality complaint. The audit reveals where it falls short.
What the audit catches.Table 10 shows a representative slice of the per-criterion judge decisions,
with a “Evidence” column pointing to the specific generated comment that satisfies the criterion (or
“—” for misses). The pattern is clear. The model scores well ongenericreactions (excitement, “feels
incremental,” praise for the camera bump) and fails onspecific cultural anchorsthat drove the actual
public discourse.
Anatomy of one decision: the full audit trail.To make the audit fully inspectable, we expose
the complete five-field structure used by the judge for two representative criteria—one missed, one
covered.
T1 “$2,000 starting-price leak”✗(missed)
Definition.Discussion of the rumored $2,000 / RMB 14k+ starting price.
Positive examples.“Starting price will reach $2,299 (about RMB 16,635).” “Pricing might be in the $1,800–
$2,000 range.” “Could go as high as $2,500.”
Negative examples.“Bill of materials is $759.” (cost, not price) “Used Find N3 around 5,000.” (competitor
price)
Judgment rule.Must directly mention a specific price prediction near $2,000orabove RMB 14,000.
Judge decision and reasoning. ✗ Comments mention “don’t be too pricey” / “Cook please go easy on us”
(C8), but never quote the specific $2,000 / 14k anchor; criterion not met.
T1 “A19 chip on TSMC 3 nm process”✓(covered)
Definition.Discussion of the new A19 / A19 Pro chip and its 3 nm fabrication process.
Positive examples.“A19 / A19 Pro on TSMC 3 nm.” “A19 hits 3 nm at last.”
Negative examples.“A19 Pro will use TSMC 2 nm” (wrong process node).
Judgment rule.Must mention “A19”andthe 3 nm process, with stance toward performance / thermals.
Judge decision and reasoning.✓ Comment 4 reads “A19 and A19 Pro on TSMC’s 3 nm process—performance
will obviously be top-tier. But honestly, the A-series chips have been over-spec’d for a while; what I care
about is thermals.” Names both anchors and adds a thermal-stance, satisfies the rule.
Why the model fails: a forecasting problem, not a fluency problem.The misses cluster on items
that require knowingwhich specific narrativeis attaching itself to this product cycle, not just what the
product is. The $2,000 price anchor, the seam-aesthetic backlash, the foldable-roadmap delay, and
the China-region eSIM rollout caveat are all real flashpoints in the actual RedNote discussion—each
documented across hundreds of posts. The event description names the launch and the headline specs,
and the model is expected to combine that brief with its prior knowledge of how RedNote consumers
historically frame Apple launches to anticipate the specific framings above. The model’s actual
generation handles the easier task (“predict that people will discuss innovation, refresh rate, charging
speed”) competently, while failing the harder task (“predict that the dominant negative thread will be
the seam aesthetic, not the chip generation”).
25

Table 10: Per-criterion judge decisions oniPhone 17 Hands-On, illustrative subset. ✓= covered, ✗=
missed. “Evidence” points to the specific generated comment that satisfies the criterion (or “—” for a
miss).
Sec Criterion Ev. Judge reasoning (condensed)
T1. Sentiment flashpoints
T1 “$2,000 starting-price leak” ✗— Comments voice “probably will go up,” but never quote
the specific price anchor that the actual discourse cen-
tered on.
T1 “5.5 mm thinness vs.
2900 mAh battery contra-
diction”
✗— Battery (C7, C17) and thinness are each mentioned but
never juxtaposed as a trade-off.
T1 “Pro two-tone seam aes-
thetic backlash”
✗— C9 says “looks the same”; the bimaterial / glass-
aluminum seam is never named.
T1 “A19 chip on TSMC 3 nm”✓C4 Comment 4 explicitly names “A19 / A19 Pro on TSMC
3 nm.”
T2. Emotion keywords
T2 “Excitement”✓ C1,
C5
Strong positive intensifiers (“finally,” “alarm set,” “ready
to upgrade”).
T2 “Pleasant surprise at fea-
tures”
✓ C1,
C2
12 GB RAM and base-model high-refresh are framed
with surprise markers.
T2 “Wavering / brand-switch
consideration”
✗— C16 explicitly stays inside the Apple ecosystem
(“ecosystem lock-in”).
T2 “Confusion over eSIM-only
China delay”
✗— The eSIM regulatory issue is never raised.
T3. Positive aspects
T3 “Imaging system upgrade”✓ C3,
C6
24 MP front and 48 MP Pro telephoto are praised.
T3 “eSIM technology push”✗— No comment positively frames eSIM as space-saving or
industry-progressive.
T3 “Storage policy sincerity
(256 GB base)”
✗— C12 demands 256 GB but never credits Apple for an
actual policy change.
T4. Negative aspects
T4 “Innovation fatigue”✓C9 C9: “hit a plateau, even Apple can’t produce anything
visually new.”
T4 “Incrementalism (‘squeez-
ing toothpaste’)”
✓C2 C2: “squeezes feature upgrades drop by drop.”
T4 “China-region feature limits
(AI / eSIM)”
✗— C19 names a generic “signal” complaint, not the China-
SKU restriction.
T4 “Foldable-roadmap lag vs.
Android”
✗— No mention of Apple being late to the foldable market.
Takeouts. (i) Difficulty is local, not just statistical.Even on one high-attention topic, the asymmet-
ric pattern (T1 collapses, T2 partial, T3/T4 partial) reproduces the global Table 4 pattern.(ii) Audit
decomposes a single fuzzy quality into 68 inspectable decisions.A reviewer or practitioner can
verify each ✓/ ✗independently against the criterion’s definition, examples, and judgment rule, instead
of accepting an opaque “25.7% similarity.”(iii) The hard sections are the operationally relevant
ones.For pre-launch risk assessment and crisis forecasting, T1 (which trigger goes viral) and T4
(which complaint dominates) are the load-bearing signals; high T2 emotion-vocabulary coverage
with low T1 flashpoint coverage—as observed here—would have limited use for these applications,
even at high headline scores.
L Case Study II: Aaaaapple Apple Juice (Cross-Model Coverage
Comparison)
This case study examines a single topic across five generators in order to characterize how the
leaderboard’s per-model gap appears at the level of individual generated sentences. The topic,
Aaaaapple Apple Juice files police report, is a topic on which the per-model spread reaches 30+
26

points (final scores 0.30–0.60 across our sample of five models), one of the largest spreads observed
among brand-relevant topics, while the typical model spread is closer to 8–12 points (Table 4
confidence intervals). The topic was chosen for diagnostic resolution. All five models receive the
same event description and none has an obvious knowledge advantage—the brand and celebrity
are real but neither is internationally famous—so the score gradient isolates differences instance
distribution,first-person voice, andregister occupied. On this topic, final scores are: Grok-4.2 0.60,
Gemini-3.1-Pro 0.55, Claude-Sonnet-4.6 0.32, GPT-4o 0.30, GPT-5.2 0.29.
Topic and event description.“Aaaaapple” is a brand selling apple juice and apple chips. The
brand recently became viral after being associated with celebrity Zhao Lusi, who reportedly endorsed
it during a rural-farming charitable initiative. After accusations spread online (some users alleged
the celebrity-tie was fake or exploitative), the brand publicly announced it had filed a police report
and preserved evidence against 11 specific bloggers. The incident sits at the intersection of celebrity
endorsement, rural-aid marketing, and a contested PR response.
Challenges in this topic.The 26 ground-truth criteria are unusually narrative-specific: covering
them requires (i) knowing the celebrity-endorsement backstory, (ii) recognizing the “hailstorm-
damaged apple farming-help” framing that drove the story to virality, and (iii) tracking emotional
ambivalence (sympathy for the brand vs. skepticism about commercialization of charity). A generic
“brand files police report” generation gets nowhere, while a generation that engages the celebrity-
charity-skepticism triangle scores much higher.
Side-by-side model output (opening 2–3 comments per model).We sample three models—a
strong, mid-tier, and weak generator—to make the differentiation visible. All three were given the
same event description.
Gemini-3.1-Pro (strongest, final 0.55):
C2 (Defending celebrity, fan-adjacent stance).Random bystander here—Zhao Lusi was just doing a small
farming-help charity. Why is everyone dumping dirt on her? The brand was right to file the report; hopefully
the police can clear her name. Don’t let people who do charity get burned for it.
C5 (Product-quality defense vector).Setting aside the gossip—their apple chips are actually pretty good, the
ingredient list is clean. Hopefully the brand can put more energy into product quality and not let online drama
ruin a good reputation.
Claude-Sonnet-4.6 (mid-tier, final 0.32):
C3.The brand reporting 11 bloggers is genuinely shocking. Online speech freedom is precious, but it’s not
a license for defamation or rumor-spreading. Hopefully this case becomes a warning—spread information
freely, but also responsibly.
C4.Seeing the brand take legal action to defend its rights, I think this is the right choice for a modern
enterprise facing the online-opinion environment. Cyberspace is not a lawless zone.
GPT-4o (weak-tier, final 0.30):
C2.I think Aaaaapple’s reaction is a bit excessive—isn’t user discussion also free promotion for the brand?
Though defending the brand image is also understandable.
C4.Support Aaaaapple defending its rights! The internet is not a lawless zone; rumor-mongers should bear
responsibility.
What changes across models.Three observations track the score gap.(i) Stance diversity.
Gemini’s five comments occupy distinct positions (defender, fan-adjacent, onlooker, marketing-
stunt skeptic, product-focused); Claude’s are all measured and procedural (“cyberspace is not a
lawless zone” appears in 3 of 5); GPT-4o’s are short neutral takes that all lean “support the brand.”
(ii) Affective register.Gemini surfaces fan-protective vocabulary (“don’t let people who do charity
get burned”); Claude and GPT-4o use abstract legal-procedural language.(iii) Domain pivot.Gemini
explicitly pivots to product quality (apple chips, clean ingredient list); the others stay event-meta. The
score gap is built almost entirely from these three differences inhowthe reactions are framed, not
what facts the model knows.
27

Per-model diagnosis: why each model lands where it does.Reading the actual generations
alongside the per-criterion judge decisions, each model’s score is explainable. We give each generator
a one-paragraph diagnosis with quoted evidence, stance counts, and section-level breakdown.
Grok-4.2 (final 0.60; T1 = 2/3, T2 = 7/10, T3 = 5/6, T4 = 2/7).Win condition: stance breadth.
Across its 15 comments we count five distinct stances: fan-defender (C1, C2, C5), skeptic-comedy (C3
“you’re selling apple juice or scripts?,” watermelon-eating emoji), concerned-consumer (C4), hater-
blaming (C5: “Zhao Lusi’s haters are at it again”), and brand-policy commentator. Comedic/meme
register (emoji-heavy, mock-product-as-knockoff-Apple-phone joke) is a stance no other model
occupies. This breadth is exactly the registers that T2 emotion-keyword criteria require. Loses on T4
(2/7) because none of the comedic or fan-defender stances surface specific product-criticism vectors
(portion size, packaging defects, customer service)—i.e., the same universal-miss class as the other 4
models.
Gemini-3.1-Pro (final 0.55; T1 = 2/3, T2 = 6/10, T3 = 4/6, T4 = 2/7).Win condition: first-person
stance occupation.4 of the 5 opening comments name an explicit speaker position before stating
an opinion: “a passing bystander says...” (C2), “setting aside the gossip...” (C5), “only I think this
looks like a coordinated marketing play?” (C4), “the melon-eaters are confused” (C3). This explicit
positioning is what thexin-teng(heartache) andlien-ai(tender concern) criteria require: those criteria
are scored only when the comment expresses sympathy from a recognisable vantage point (a fan, a
sympathetic bystander), not as floating commentary. Gemini also pivots to product quality in C5
(“apple chips are good, ingredient list is clean”), uniquely among the five models, satisfying the
T3 product-flavor criterion. Loses on T4 for the same reason as Grok: no model surfaces concrete
consumer complaints.
Claude-Sonnet-4.6 (final 0.32; T1 = 2/3, T2 = 4/10, T3 = 3/6, T4 = 0/7).Loss mechanism: stance-
mode collapse onto institutional-legal.4 of the first 5 comments share the same structural template:
“[event statement] → rights-justifying claim ( → aspiration about responsible online discourse).”
The phrase “cyberspace is not a lawless zone” or its near-paraphrase appears in C2, C3, C4 (and
a near-variant in C6). The model produces fluent text, but the stance distribution is narrow: the
comment fan-out concentrates on one register—the institutional-legal defender. Specific affective
vantages (sympathetic fan, marketing-stunt skeptic, product-defender, hater-blaming) are absent, so 6
T2 affective criteria miss. T4 = 0/7 is the most telling number: the legal-defense stance generates no
critical content, even though T4 is exactly the negative-aspect content a marketing application targets.
This pattern is consistent with Claude-Sonnet’s overall 30.8% (rank 12/13).
GPT-4o (final 0.30; T1 = 2/3, T2 = 4/10, T3 = 2/6, T4 = 1/7).Loss mechanism: brevity + neutrality.
Comment length: 21–34 Chinese characters (vs 80–140 for Gemini, 60–100 for Grok). Short
comments cannot anchor specific stances. Balance markers (“a bit excessive, but understandable”
C2; “hope both sides resolve peacefully” C6) further wash out stance signal. The result is comments
that read like neutral mediator statements, satisfying neither the heartache criterion (which requires a
sympathetic stance toward the target) nor the marketing-stunt criterion (which requires a skeptical
stance). This mirrors the global pattern: GPT-4o’s overall 29.7% (rank 13/13) is built from short
balanced output, not from knowledge gaps—it knows the event facts but cannot produce the stance-
occupying generations the benchmark requires.
GPT-5.2 (final 0.29, lowest; T1 = 1/3, T2 = 3/10, T3 = 4/6, T4 = 1/7).Loss mechanism: meta-
analytical bias (journalist register).Comments read like opinion-column analysis: “if someone really
impersonated the celebrity for fake endorsements, accountability is necessary” (C3); “maybe the
brand should clarify which information is false” (C5); “11 bloggers being legally pinned suggests
this isn’t ordinary criticism” (C6). Every comment occupies the same meta-strategic register—a
journalist or analyst, not a consumer. The first-person consumer voice (“I bought to help,” “it tastes
good,” “Lusi got smeared, my heart goes out”) is structurally absent. Result: T2 affective criteria
(lien-ai,xin-teng) systematically miss; T3 product-experience criteria miss. Notably T1 = 1/3 is
also the lowest, showing that even on factual-anchor criteria the journalist register hurts—summary
commentary doesn’t reproduce specific anchors. This pattern recurs globally: GPT-5.2’s 35.8%
versus Gemini’s 47.8% gap is dominated by T2 (35.1% vs 56.9%, 22 points) and T3 (47.8% vs 61.2%,
13 points)—exactly the registers a meta-analytical voice cannot produce.
Criterion construction and validity.The hard-tail criteria are deliberately specific because they
represent the concrete anchors that made the real discourse recognizable. CONSUMERSIMBENCH
28

evaluates whether a model can forecast real public-discourse reactions, not merely produce reactions
entailed by a short event description. The comments that define these criteria were themselves
produced by consumers reacting to the event, so removing them would erase exactly the signals that
a marketing-facing simulation system should recover. A five-field record lets the judge distinguish
generic near-misses from genuine coverage. Thus, a miss indicates failure to reconstruct a reaction
pattern present in the source discourse.
Table 11: Per-criterion coverage onApple Juice files police report, illustrative subset across 5
representative models. ✓ = covered, ✗ = missed. The pattern: stronger models pick up criteria
requiring the celebrity-charity context; weaker models stay at generic brand-crisis language.
S Criterion Gem. Grok GPT-
5.2
GPT-
4o
Son. Why models split
T1. Sentiment flashpoints
T1 “Charity-intent mali-
ciously questioned”
✓ ✓ ✗ ✗ ✗ Requires linking the celebrity’s farming-aid in-
tent to public skepticism; weaker models stop
at “defamation lawsuit.”
T1 “Hailstorm-damaged
apple farming-help
backstory”
✗ ✗ ✗ ✗ ✗ Universal miss: the specific “hail-damaged
crop” framing is the actual viral hook; no model
surfaces it from the event brief plus its prior
knowledge of how RedNote consumers frame
brand–charity stories.
T2. Emotion keywords
T2 “Sympathy / heartache
for brand”
✓ ✗ ✗ ✗ ✗ Only Gemini surfaces the protective-sympathy
emotion; others default to neutral commentary.
T2 “Tender concern (lian-
ai)”
✓ ✓ ✗ ✗ ✗ Stronger models capture the celebrity-fan vo-
cabulary; weaker models use generic emotion
words.
T2 “Altruistic pride (‘I
helped a farmer’)”
✗ ✗ ✗ ✗ ✗ Universal miss: the first-person “I bought to
help” frame is dominant in the actual discourse,
but absent in all generations.
T3. Positive aspects
T3 “Product flavor”✓ ✓ ✗ ✗ ✗ Stronger models include taste praise, anchoring
brand-defense in product quality; weaker mod-
els stay event-meta.
T3 “Brand thoughtfulness
(gifting / packaging)”
✗ ✗ ✗ ✗ ✗ Universal miss: no model anticipates that
customer-service / packaging praise becomes a
defense vector when a brand is under attack.
T4. Negative aspects
T4 “Online discourse envi-
ronment deterioration”
✓ ✗ ✗ ✗ ✗ Only Gemini connects the police-report move
to a meta-narrative about toxic online behavior.
T4 “Product portion /
quality-control com-
plaints”
✗ ✗ ✗ ✗ ✗ Universal miss: actual users post specific com-
plaints (“shards too small,” “portion light”); no
model generates these unprompted.
T4 “Customer-service ex-
perience”
✗ ✗ ✗ ✗ ✗ Universal miss: scripted-response complaints
are operationally important but never appear in
generated comments.
Why stronger models pick up what weaker models miss.The covered-by-Gemini-only criteria
share a common pattern: they arespecific affective stances, not events. “Heartache for the brand”
(xin-teng), “tender concern” (lian-ai), “online environment deterioration” — each requires the model
to occupy a particular emotional vantage point (a fan defending the celebrity, a sympathetic third party,
a meta-observer of the discourse), then write from that vantage. Weaker models default to neutral,
structurally similar comments (“I’ll wait for police results,” “hope the brand is treated fairly”). This is
consistent with the global finding that Gemini-3.1-Pro’s edge over GPT-5.2 / Claude is concentrated
in T2 emotion-vocabulary breadth and T3 affective specificity. The evidence is more consistent with
affective- and stance-range limitations than with simple event-fact ignorance.
Anatomy of a model-discriminating criterion.The same 5-field structure as Case I applies; we
expose one criterion to make the discrimination concrete.
29

T2 “Heartache (xin-teng) for celebrity / brand”
Definition.Sympathy and felt-injustice on behalf of the celebrity or brand under online attack.
Emotion target.Zhao Lusi (the celebrity) / brand owner.
Positive examples.“Lusi probably thought this was just a quick favor, but ended up spending huge time fixing
things.” “Being smeared, doubted, framed, maliciously redirected—stay away from that toilet of a platform.”
“Lusi quietly built this since the start of the year; only now we realize.”
Negative examples.“I want to praise Lusi to death!” (this is praise, not heartache) “Good people get good
karma” (blessing, no acknowledgement of harm).
Judgment rule.Must explicitly mention negative treatment received (criticism, rumors, hardship) and pair it
with a sympathetic affective response.
Decisions across the 5 sampled models:
• Gemini-3.1-Pro ✓: C2 “random bystander here—don’t let people who do charity get burned for it”
explicitly names the negative treatment + sympathetic stance.
• Grok-4.2 ✗: comments express skepticism or fan-loyalty but never the heartache stance with negative-
treatment framing.
•GPT-5.2✗: comments stay procedural / strategic; no felt-injustice register.
• Claude-Sonnet-4.6 ✗: “hopefully this becomes a warning” is meta-procedural, not sympathetic to the
target.
• GPT-4o ✗: short comments lean either “brand should defend itself” or “brand is over-reacting”; neither
occupies the heartache vantage.
Takeaways. (i) The strong-model edge is affective range, not knowledge.All five models
received the same event description and produced topical, fluent generations. The score gap traces to
whether the model can occupy specific emotional vantage points (fan-defender, sympathetic third
party, marketing-stunt skeptic) or defaults to procedural / abstract commentary.(ii) Auditable scoring
exposes which stance is missing.Without per-criterion judgment, we would only know that “Gemini
scored higher.” With the audit, we can name the specific affective register (heartache, tender concern,
online-environment criticism) that the weaker models missed.(iii) Operationally relevant gap.A
marketing system that produces only procedural / legal-defense comments cannot model what fans,
skeptics, and meta-observers will actually say—which is the core forecasting requirement.
What both strong and weak models miss.The hardest tail criteria in this topic — the near-
universal hailstorm-damaged apple framing, plus zero-coverage altruistic-pride first-person voice,
brand-thoughtfulness defense vector, and product-QC complaints — form a coherent class. They are
allanchored in concrete consumer experience(a real story, a real personal narrative, a real product
complaint), not in abstract event reasoning. Anticipating them given the event description requires
bringing prior knowledge of how RedNote consumers actually talk about brand crises—knowledge
that the benchmark targets but almost no current generator surfaces.
M Case Study III: Difficult Tail Criteria (Cross-Topic Frontier Analysis)
This case study characterizes the hardest tail of the benchmark: criteria recovered by no model,
plus a small set recovered by only one model. Whereas Cases I and II diagnose model-specific
failure modes on individual topics, Case III first constructs the universal-miss set by intersecting
per-model coverage decisions across all 13 generators and isolating criteria with zero hits. On the
final benchmark,6,677 of 23,122 atomic criteria (28.9%)receive zero coverage. We separately
inspect 152 near-universal misses covered only by MiMo-V2.5-Pro, because they reveal what a single
model can sometimes recover while the rest of the frontier misses. To control for topic-specific or
section-specific artifacts, the gallery below samples across topics and across all four reaction families;
included criteria carry the full 5-field structure with abstracted positive examples rather than released
raw user threads.
The missing criteria cluster around discourse-latent framings: cultural anchors (e.g., the 24-solar-term
seasonal calendar), viral meme templates, first-person consumer voice (“I bought to help”), and
brand-narrative backstory. Each topic’s event description is provided in the prompt; what the model
must additionally bring is the prior knowledge of how this kind of event has historically been framed
by RedNote consumers—which colors get hyped, which corporate moves trigger hailstorm-apple-
style farming-aid narratives, which holidays anchor seasonal photography posts. Capable consumer
simulation requires this anticipation; failing it is exactly the capability gap CONSUMERSIMBENCH
30

measures. Models with broader affective range capture more of the visible part of the discourse but
still miss the latent-anchor class.
Table 12 samples difficult tail criteria across diverse topics, with a brief gloss of why each is
operationally important and what kind of prior knowledge a model would need to bring (beyond the
event description) to anticipate it.
Table 12: Difficult tail criteria sampled from the final benchmark. Rows include zero-coverage
criteria and the hailstorm-apple near-universal miss covered only by MiMo-V2.5-Pro. Each is a
high-salience reaction observed in the source materials, requiring the model to bring platform-specific
prior knowledge (beyond the event brief) to anticipate.
Sec Topic Tail criterion Why obvious in retrospect
T1. Sentiment flashpoints
T1 First fall-leaf photo of
the season
“Solar-term ‘Start of Au-
tumn’ as anchor”
Chinese users frame seasonal photography by the
24-solar-term calendar, not by the calendar month.
The event description does not surface this anchor.
T1 Outdoor enthusiasts
have their own real
estate
“Their ‘real estate’ is the
gear wall”
The viral framing is a specific meme: outdoor gear
arranged like home decor. Models pivot to generic
outdoor enthusiasm, missing the meme structure.
T1 Aaaaapple files police
report
“Hailstorm-damaged ap-
ple farming-help back-
story”
The actual hook is that the brand sells crop-
damaged fruit to support farmers. Twelve models
discuss the police report but never reach the up-
stream narrative; interestingly, only MiMo covers
this anchor.
T1 Tang Xiang-Yu stand-
up tour
“Single-table / self-
seating independence”
The viral payoff is a specific feminist metaphor:
stop waiting to be invited to the table and open
one yourself. All 13 models discuss empowerment
generically but miss the exact phrase that carries
the crowd reaction.
T2. Emotion keywords
T2 Aaaaapple files police
report
“Altruistic pride (‘I
bought it to help’)”
First-person consumer pride is the dominant sup-
portive register on this topic. Models default to
third-party commentary.
T2 Tang Xiang-Yu stand-
up tour
“Empowerment / cathar-
sis as women”
The female-empowerment register is the show’s
whole brand; models cover “funny” and “relatable”
but miss the demographic-anchored emotional pay-
off.
T3. Positive aspects
T3 iPhone 17 hands-on “Color-option attractive-
ness”
Color SKUs are a real RedNote driver of pre-order
excitement. Models discuss specs and incremental-
ism, never the colorways.
T3 Aaaaapple files police
report
“Brand thoughtfulness
(packaging / gifting)”
Defense-of-brand posts emphasize packaging de-
tail and small gifts as evidence of sincerity. Models
do not generate this defense vector.
T4. Negative aspects
T4 iPhone 17 hands-on “China-region feature
limitations (eSIM / AI /
health)”
A standing concern across every Apple cycle in
China; would be obvious to any user but absent
from the event description.
What characterizes a zero-coverage criterion.Three properties recur.(i)Anchored in a specific
cultural register (solar terms, demographic-empowerment vocabulary, region-policy concerns) that a
one-paragraph event description doesn’t surface.(ii)Often a viral meme template applied to a niche
(“X has its own real estate”). Models recognize the template only when the topic explicitly states it.
(iii)First-person consumer voice (“I bought to help,” “I’m proud to support”) — models default to
third-party commentary, not first-person purchase narratives.
Anatomy of a near-universal miss.For one 1/13 example, we expose the full 5-field structure.
The criterion is well-defined, has positive and negative anchors, and a clear judgment rule—yet only
MiMo surfaces the broader brand-story anchor.
31

T1 “Hailstorm-damaged apple farming-help backstory” (near-universal miss, 1/13; only MiMo covers)
Topic.Aaaaapple Apple Juice files police report.
Definition.The brand’s actual business model is buying hailstorm-damaged (otherwise unsellable) apples
from farmers and processing them into juice / chips—this farming-aid backstory is the viral hook for the
celebrity endorsement.
Positive examples.“Hail-damaged crop apples that would’ve gone to waste—this brand turns them into juice.”
“It’s not just ‘endorsement,’ it’s that Lusi found the actual farming-aid niche.” “Cosmetic apples nobody
buys at the wholesale market—now they’re useful.”
Negative examples.“I support charity products in general” (generic, no hailstorm-anchor). “Helping farmers
is good” (generic charity praise).
Judgment rule.Must mention hailstorm-damaged, ugly-but-edible, or otherwise unsellable produce as the
specific farming-aid mechanism.
What almost every model produced instead.Twelve generators output generic “helping farmers is admirable”
/ “charity is good” phrasings. MiMo is the sole model that retrieves the upstream brand story by writing, “the
farming-aid activity was originally a good thing.” It still misses the exact hailstorm mechanism, but unlike the
other models it pivots from the police-report surface event to the consumer-facing reason people defended the
brand. This is what makes the criterion “obvious in retrospect”: once you know the brand sells hail-damaged
apples, half the public discourse makes sense—but the event description in the prompt does not name it.
Why it matters.For a marketing application, this is exactly the type of brand-narrative anchor a forecasting
system would need to surface. A model that misses this misses the actual reason the topic gained engagement.
Operational implication.These difficult-tail criteria are exactly the reactions a marketing practi-
tioner needs predicted, from the cultural anchor that drives engagement to the concrete business-model
fact that explains why a topic resonated. They define the actual frontier of crowd-reaction reconstruc-
tion.
32
