---
title: 'Forecast-Dojo: Replayable Environments for Benchmarking and Training LLM Forecasting Agents'
url: https://arxiv.org/abs/2609.28876
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Liqin Ye
- Haorui Wang
- Fardin Ahmed
- Rongzhi Zhang
- Yuan He
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.28876
pages: 37
chars: 125683
fetched_at: '2026-11-08T13:21:32+00:00'
kb_version: 1
---

# Forecast-Dojo: Replayable Environments for Benchmarking and Training LLM Forecasting Agents

Preprint
FORECAST-DOJO: REPLAYABLEENVIRONMENTS FOR
BENCHMARKING ANDTRAININGLLM FORECASTING
AGENTS
Liqin Ye*,1, Haorui Wang*,1, Fardin Ahmed1, Rongzhi Zhang†,2, Yuan He†,2, Ziyuan Lin3,
Yanbin Yin1,Jing Peng 1,Michael Galarnyk 1,Sudheer Chava 1,Chao Zhang 1
1Georgia Institute of Technology, 2Amazon, 3University of Florida
Data
 Code
 Website
ABSTRACT
Forecasting requires large language model (LLM) agents to gather evolving evi-
dence, revise their beliefs, and make calibrated predictions over time. Yet eval-
uating and improving these capabilities is challenging because real-world events
unfold continuously and outcomes may take months to resolve. We introduce
Forecast-Dojo, a replayable environment that reconstructs resolved prediction-
market events as sequences of dated forecasting steps, enabling reproducible eval-
uation, longitudinal analysis, and training from agent interactions. It comprises
1,568 Polymarket events split temporally into training and evaluation sets, along-
side 18.8 million dated news articles. Across 12 models, research tools consis-
tently improve forecasting performance, and greater capture of new evidence is
associated with larger improvements over time. Nevertheless, all models trail his-
torical market forecasts, while carrying a belief notebook across dates reduces
research costs without consistently improving forecast quality. We supervise fine-
tuned Qwen3-30B-A3B-Thinking-2507 on collected trajectories from Qwen3-
235B-A22B-Thinking-2507 to demonstrate the environment’s training utility. The
student’s accuracy is improved from 34.8% to 42.8% on the evaluation set.
40 45 50 55 60 65
Accuracy (%)  ↑
0.50
0.55
0.60
0.65
0.70Brier score  ↓
(a) Memory-free
GPT-5.6 Sol
GPT-5.5
GPT-5.4
Opus 4.8
Opus 4.6
GLM-5
Qwen3.5-397B
Kimi K2.5
MiniMax M2.5
DeepSeek-V3.2
gpt-oss-120b
Nemotron 3 Super
Market
40 45 50 55 60 65
Accuracy (%)  ↑
0.50
0.55
0.60
0.65
0.70Brier score  ↓
(b) Memory-on
GPT-5.6 Sol
GPT-5.5
GPT-5.4
Opus 4.8
Opus 4.6
GLM-5
Qwen3.5-397B
Kimi K2.5
MiniMax M2.5
DeepSeek-V3.2
gpt-oss-120b
Nemotron 3 Super
Market
Figure 1:Forecasting performance onForecast-Dojo.Accuracy and Brier score of 12 models
on 230 held-out events. Both settings use research tools: (a)memory-freestarts with a fresh context
at each forecast date, while (b)memory-oncarries a belief notebook across dates. Lower right is
better; dashed lines mark historical market performance. Full results are reported in Table 2.
*Equal contribution. Corresponding author(s):{liqiny, hwang984}@gatech.edu
†Work done outside Amazon.
1
arXiv:2609.28876v2  [cs.AI]  26 Oct 2026

Preprint
1 INTRODUCTION
Large language model (LLM) agents are increasingly used to forecast real-world events by actively
searching for evidence, reasoning under uncertainty, and producing probabilistic predictions (Halawi
et al., 2024; Zeng et al., 2025; Seed, 2026; Karger et al., 2025). Forecasting is inherently time-
dependent: the evidence available to a forecaster changes as new information arrives. The same
question can therefore pose a different prediction problem at different times, requiring the forecaster
to update its belief as new evidence emerges.
Existing forecasting benchmarks capture only part of this process (Table 1). Live bench-
marks (Karger et al., 2025; Zeng et al., 2025; Zhao et al., 2026; Zhang et al., 2026) pose unresolved
questions, so the forecasting problem evolves naturally with the world, but they run on wall-clock
time. A past forecasting condition cannot be recreated for a model released later, and outcomes
arrive only at resolution, which slows evaluation and makes training impractical. Historical bench-
marks (Jin et al., 2021; Halawi et al., 2024; Chandak et al., 2025) reconstruct past information
cutoffs, making resolved events immediately scorable and reusable. However, they typically evalu-
ate each forecast at a single historical point rather than revisiting the same question across multiple
points in time. The ideal setting combines the two: the forecasting problem evolves as new evi-
dence becomes available, yet each past step can be replayed with the same task and information
cutoff. Models can then be compared under identical conditions and scored immediately, and their
forecasting trajectories become usable for training.
We introduceForecast-Dojo, a replayable environment that reconstructs resolved real-world events
as sequences of historical forecast steps (Figure 2). At each step, an LLM agent can search a tempo-
rally restricted information corpus, inspect full documents, and use computational tools to produce
a probabilistic forecast using documents whose assigned dates satisfy that cutoff. Each step can
be reset and rerun across models or repeated trials, while steps from the same event can be tra-
versed sequentially with persistent agent memory. The recorded outcome is retained for immediate
scoring and is not supplied in the forecasting prompt. This common interaction interface supports
both benchmarking and learning: held-out events evaluate agents under controlled conditions, while
training events generate forecasting trajectories and outcome feedback for learning.
Empirically, we evaluate 12 models on 230 held-out events without tools, with research tools, and
with research tools plus a belief notebook carried between dates. Research tools lower Brier for
all 12 models, and memory-free Brier falls from 0.670 in the first third of an event to 0.606 in
the last third, while forecasts without tools stay flat. The improvements concentrate at steps with
more new evidence. Every model still trails the historical market forecasts in Brier and accuracy,
with the best Brier at 0.546 against 0.498 for the market. The belief notebook reduces estimated
API costs by a median of 24% across five proprietary models with available pricing (Section 5.4).
However, it lowers Brier scores for only 6 of the 12 evaluated models, with none of these improve-
ments statistically significant (Section 5.2). Finally, a supervised fine-tuning study demonstrates
that Qwen3-30B-A3B-Thinking-2507 (Yang et al., 2025a), trained on trajectories collected from
Qwen3-235B-A22B-Thinking-2507 (Yang et al., 2025a) in theForecast-Dojotraining set, outper-
forms its base model on temporally held-out events (Section 5.5).
Our contributions are:
•A replayable forecasting environment.Forecast-Dojoreplays each resolved event as a fixed
sequence of dated forecast steps with an optional belief notebook, and scores every step against
the realized outcome for evaluation or training.
•A dataset of resolved events and dated news.It covers 1,568 Polymarket events with 6,122
forecast steps, split by time into 1,338 training and 230 evaluation events, with evidence from
18.8M dated CC-News articles.
•A benchmark study beyond overall rankings.We compare 12 models with historical market
forecasts, examine how forecasts change as events unfold and how memory affects quality and
cost, and show how the collected interactions can be used to train an agent.
2 RELATEDWORK
Forecasting with dated evidence.ForecastQA restricts news by time, while Autocast pairs fore-
casting questions with dated articles and historical human forecasts (Jin et al., 2021; Zou et al.,
2

Preprint
Table 1:Summary of existing forecasting benchmarks.The criteria target the capabilities used
to construct and study Forecast-Dojo.Aligned evaluationindicates that the same forecasting task
is evaluated at a pre-specified sequence of forecast dates or evidence states shared across models.
Market beliefindicates that historical prediction-market prices are available as a reference. :
provided; : not documented in the cited work; : system- or agent-dependent.
Benchmark Dated replay Agent research Aligned evaluation Agent memory Market belief Train/eval split
ForecastQA (Jin et al., 2021)
Autocast (Zou et al., 2022)
MIRAI (Ye et al., 2024)
ForecastBench (Karger et al., 2025)
FutureX (Zeng et al., 2025)
Prophet Arena (Yang et al., 2025b)
EvolveCast (Yuan et al., 2025)
BTF-2 (Liptay et al., 2026)
FutureSim (Goel et al., 2026)
Forecast-Dojo
2022). ForecastBench and FutureX collect predictions on unresolved events (Karger et al., 2025;
Zeng et al., 2025). Related settings evaluate repeated forecasts, macroeconomic nowcasts, and sim-
ulated market decisions (Yang et al., 2025b; Zhao et al., 2026; Cheng et al., 2026).Forecast-Dojo
uses resolved events to support repeatable research and immediate outcome-based feedback, while
keeping market probabilities outside the forecasting prompt.
Interactive research and forecast revision.Bench to the Future uses frozen research corpora,
and BTF-2 records traces to distinguish information gathering from judgment (Wildman et al., 2025;
Liptay et al., 2026). MIRAI provides code-based access to events and news, while WorldReasoner
evaluates outcome, evidence, and reasoning quality (Ye et al., 2024; Chi et al., 2026). FutureSim
studies long-horizon adaptation in a replayed world, where agents jointly decide how to research,
maintain memory, revise forecasts, and progress through time (Goel et al., 2026).Forecast-Dojo
instead fixes time progression in the experimental design: each event is replayed at the same histor-
ical checkpoints for all agents, which yields matched longitudinal trajectories for controlled com-
parison and reusable interactions with outcome feedback for learning. This complements work on
evidence-driven revision, probability coherence, and iterative research workflows (Yuan et al., 2025;
Paleka et al., 2025; Murphy, 2026).
Environments for training agents.MLE-Dojo provides executable machine learning engineer-
ing tasks and feedback for evaluation and training (Qiang et al., 2025).Forecast-Dojofollows
this environment-centered approach, specifying the forecasting interaction and its feedback while
leaving learning algorithms separate. Prior forecasting work trains on question collections or se-
lected model-generated forecasts (Zou et al., 2022; Halawi et al., 2024), and recent methods use
reinforcement learning, outcome-based fine-tuning, and news-derived questions (Levy, 2026; Jeen
et al., 2026; Chandak et al., 2025). Our contribution is the shared task and tool interface for collect-
ing research interactions and evaluating agents on separate events; the SFT experiment demonstrates
one use of that interface.
3 FORECASTING AS ANINTERACTIVETASK
We formulate forecasting as an interactive task over a sequence of forecast steps for the same event.
At each step, the agent researches evidence available up to the current date and produces a proba-
bilistic forecast. Across steps, the evidence boundary advances and explicit memory may persist.
Events, forecast steps, and episodes.A questionQspecifies an event, its resolution criteria, and a
finite set of mutually exclusive outcomesY={1, . . . , K}. LetY∈ Ydenote the realized outcome.
At ordered datesτ 1 <· · ·< τT before the event closes, whereTvaries across events, the agent
performs aforecast step: it researches the event and reports a probability distributionp Q,t ∈∆ K−1.
3

Preprint
Curate Events & Information Corpus
Polymarket
2025-06 – 2026-06
Horizon > 7 days Market activity
Task nontriviality Evidence sufﬁciency
1,568 events
train 1,338 eval 230
CC-News
2025-03 – 2026-05
Cleaning · language ID Quality · repetition
Near-duplicate removal Assigned dates + content audit
18.8M articles
dated · embedded · indexed
Forecast Each Question Over Time
Question Q
“Fed rate decision
in Dec. 2025?”
outcomes cut hold hike …
resolves by a ﬁxed rule
closes at a set date
Temporally Evolving Corpus
close
τ1
 τ2
 τt
 τT
pt
M1 M2 Mt
one forecast step
Agent Loop at date τt
Information Corpus
τt
≤ τt > τt
Sandbox
isolated code execution
Tools
search
read
compute
LLM Agent
Ht
calls
results
Forecast
pt
commit
Notebook Mt
memory-on
write
Evaluation & Training
p1
 pt
 pT
Outcome Y
hidden from agent
Y
pt
rt = S(pt, Y)
e.g. Brier
Evaluation
230 held-out events
e.g. Brier Acc. Info-α
Training
1,338 training events
demonstrated SFT
possible RL
On-policy distillationtrajectories + feedback
Figure 2:Overview of Forecast-Dojo.Top: resolved Polymarket events are filtered and split by
time into training and evaluation events, and CC-News articles are cleaned, dated, and indexed.
Middle left: each question is forecast at a fixed sequence of dates as the visible corpus grows,
with an optional belief notebookM t passed between steps. Bottom left: within one step, the agent
searches and reads articles dated on or beforeτ t, runs code in a sandbox, and commits a forecast
pt. Right: the realized outcomeYstays hidden from the agent. The evaluator scores each forecast
against it, using held-out events for evaluation and training events for learning.
The ordered forecast steps for the same question form aforecast episode. All steps concern the same
eventual outcome, but they differ in the historical evidence available at the forecast date.
Within-step interaction.LetIdenote an information corpus. At dateτ t, the agent is exposed to
I≤τt ={d∈ I: date(d)≤τ t},I ≤τt ⊆ I≤τt+1 ,(1)
wheredate(d)denotes the timestamp assigned to documentd. Within a forecast step, the agent may
issue search queries, inspect retrieved articles, and use computation before submitting its forecast
(see Section 4.4). LetH t denote the within-step interaction history, including the agent’s research
actions and the resulting tool observations. The agent producesp Q,t conditioned onH t. Because
agents choose their own queries and which documents to inspect, different rollouts at the same date
from an agent can follow different research paths even under the same dated evidence boundary.
Progression across forecast steps.After each report, the environment advances to the next sched-
uled date and starts a fresh interaction. We define two modes for carrying information across forecast
steps:memory-freeandmemory-on. In memory-free forecasting, each step starts without informa-
tion produced at previous steps. In memory-on forecasting, the agent produces a belief notebook
Mt that summarizes its current assessment, supporting evidence, and open questions. At the next
step,M t is provided alongside the question and new forecast date, allowing the agent to update its
forecast from its prior assessment as new evidence becomes available.
Outcome feedback.Each forecast step ends with a probability reportp Q,t. Once the realized out-
comeYis available, the environment assigns feedbackr Q,t =S(p Q,t, Y), whereSis an outcome-
based scoring rule. The outcome and feedback are not part of the agent’s forecasting context. This
4

Preprint
separates the interaction that produces a forecast from the feedback assigned to it, allowing the same
task interface to support different downstream evaluation or learning procedures.
4 FORECAST-DOJO
Section 3 defines the forecasting task abstractly. We now describe how events (§4.1), information
corpus (§4.2), and forecast dates (§4.3) are selected, how agents interact with research tools and
optionally carry memory across steps (§4.4), and how the resulting forecasts and trajectories support
evaluation and learning (§4.5).
4.1 FORECASTINGEVENTS
We construct our candidate pool from resolved Polymarket 1 binary and mutually exclusive multi-
option events whose full lifetimes fall between June 2025 and June 2026. We construct a daily mar-
ket reference from UTC-day mean YES prices, which we call themarket belief. For binary events,
the YES price determines the probability of YES and its complement; for multi-option events, we
normalize the option-level YES prices to obtain a distribution over the mutually exclusive outcomes.
Within this pool, we select events along four dimensions. (1)Forecasting horizon: the tradeable
lifetime must exceed 7 days, so that each question supports multiple forecast steps. (2)Market ac-
tivity: most days must have sufficient trading activity, which reduces sparse or stale prices and favors
questions with sustained attention. (3)Task nontriviality: we remove events whose market already
assigns near-certain probability to the realized outcome, as well as events whose market history is
nearly flat and directionless. (4)Evidence sufficiency: following Joren et al. (2025), an LLM judge
must rate the evidence retrieved two days before the recorded close as SUFFICIENT, followed by a
content audit. This criterion does not establish sufficient evidence at earlier forecast dates. Several
filters use the realized outcome, so the benchmark is not a random sample of Polymarket events
(Appendices A.2 and C.4).
4.2 INFORMATIONCORPUS
Corpus construction.Forecast-Dojorequires broad historical evidence whose availability can
be reconstructed at each forecast date. We build the corpus from CC-News (Nagel, 2016), which
provides large-scale news coverage together with crawl timestamps that support historical recon-
struction. We process CC-News archives from March 2025 through May 2026 using a quality
pipeline adapted from FineWeb (Penedo et al., 2024), including text cleaning, language identifica-
tion, repetition and document-quality filtering, and near-duplicate removal. We suppress duplicate
URLs, identical titles within a seven-day window, and near-verbatim body matches to reduce re-
peated coverage. After filtering, the corpus contains approximately 18.8M articles, which we embed
with Qwen3-Embedding-8B (Zhang et al., 2025) and index with FAISS (Douze et al., 2026).
Temporal integrity.We assign each article a UTC calendar dayt(d)using the closest-to-crawl
rule. Among valid structured publication and modification timestamps, we choose the one closest to
the crawl time (breaking ties toward the later timestamp), cap it at the crawl time, and use its UTC
day. If neither structured timestamp is valid, we use the crawl day. These timestamps come from
standard structured metadata fields (Guha et al., 2016; Schema.org; Google Search Central). Search
and article reads admitt(d)≤τ t, so articles assigned to the forecast day itself are included. This
is a day-level metadata boundary; it does not certify intraday availability or reconstruct earlier ver-
sions of an edited page. Event construction additionally screens for content-level outcome leakage.
Appendix A.1 gives the full dating rule.
4.3 TEMPORALTASKCONSTRUCTION
Forecast-date selection.A forecast step for every day of an event’s lifetime would let long-lived
events dominate the samples. We therefore use a sublinear schedule: after a two-day buffer before
the recorded close, an event withncandidate days receivesT= clamp (round( √n),3,10)forecast
steps. We partition the event history intoTtemporal bins and select one date from each, favoring (1)
1https://polymarket.com/
5

Preprint
20.8%
23.2%
13.8%
12.3%
15.5%
9.0%
Train
1,338 events
24.3%
23.9%
8.3%
17.4%
8.7%
11.3%
Eval
230 events
Sports
Cryptocurrency
Finance
Politics
Geopolitics
Popular culture
Technology
Science, health & weather
Crime & society
45.1% 17.2% 15.5% 7.8% 11.7% 2.6%Train
17.4% 20.4% 13.9% 13.9% 30.4% 3.9%Eval
(b) Offered outcomes K share of events
K = 2 K = 3 4–6 7–10 11–20 > 20
7.8% 40.1% 22.9% 29.1%Train
9.5% 50.8% 25.6% 14.1%Eval
(c) Forecast horizon h share of forecast steps · h = days from forecast date to close
h < 3 3 ≤ h ≤ 7 7 < h ≤ 14 h > 14
(a) Primary domain share of events
Figure 3:Composition of the training and evaluation splits.(a) Primary domain of each event;
slices under 5% are unlabeled. (b) Number of offered outcomesKper event; binary events have
K= 2. (c) Forecast horizonh, the number of days from a forecast date to the recorded close, over
all forecast steps (event–date pairs; 5,325 training, 797 evaluation). Forecast dates stop two days
before the close, so theh <3bin is exactlyh= 2.
market-belief movement, larger changes in the market belief as a proxy for changes in expectations,
and (2)news volume, more articles in the corpus overall, a global signal rather than an event-specific
measure of relevance.
Temporal train–evaluation split.We split complete events, rather than individual forecast steps,
into non-overlapping temporal windows. Training events must start and close within[2025-06,
2026-03)and evaluation events within[2026-03, 2026-06), and events crossing either boundary
are excluded, so no event appears in both splits. The training split contains 1,338 events (602 binary)
with 5,325 forecast steps, while the evaluation split contains 230 events (40 binary) with 797 steps.
Figure 3 summarizes the composition of both splits, spanning diverse event domains (Figure 3a),
outcome cardinalities (Figure 3b), and forecasting horizons (Figure 3c).
4.4 AGENTINTERACTION
Tool interface.At each forecast step, the agent can call three tools. SEARCH, viasearch(query,
top_k), returns identifiers, titles, dates, retrieval scores, and snippets for the top-karticles in
I≤τt. READ, viascrape(article_id), returns the full text of a retrieved article. COMPUTE,
viapython(code), runs model-generated code for numerical analysis, base-rate estimation, or sim-
ulation. Python runs in an isolated sandbox with networking disabled and no access to benchmark
data such as the task files, corpus, and index (Table 7). The agent may interleave reasoning with
repeated tool calls, and each tool output joins the within-step historyH t.
Memory transfer.Each forecast step is a fresh model interaction with access toI ≤τt. In memory-
free mode, nothing from earlier steps is carried forward. In memory-on mode, the notebook from
the previous step is inserted into the next prompt, while previous turns, reasoning traces, and tool
observations are discarded, so the notebook is the only transferred information (format in Figure 11).
6

Preprint
Table 2:Main Results.Values average recorded forecasts;±denotes the SD across four rollout
means. Paired event-bootstrap 95% CIs are discussed in Appendix C.1. Unusable forecasts receive
uniform fallback; accuracy is reported in percent, and Information-αrequires available market prob-
abilities.Boldand underlined indicate the best and second-best models. Superscripts†,‡, and§flag
configurations with over 5% unusable forecasts. Uniform and market forecasts serve as references.
No tools Tools, memory-free Tools, memory-on
Model Brier↓Acc.↑Info-α↑Brier↓Acc.↑Info-α↑Brier↓Acc.↑Info-α↑
Proprietary
GPT-5.6 Sol 0.650
± 0.004
47.03
± 0.5
−0.422
± 0.006
0.554
± 0.008
56.36
± 0.9
−0.138
± 0.023
0.546
± 0.004
57.59
± 1.3
−0.104
± 0.017
GPT-5.50.698
± 0.001
43.85
± 0.6
−0.603
± 0.008
0.564
± 0.002
57.69
± 0.7
−0.186
± 0.010
0.571
± 0.005
57.68
± 1.0
−0.198
± 0.013
GPT-5.40.708
± 0.002
41.34
± 0.8
−0.633
± 0.015
0.586
± 0.002
53.12
± 0.4
−0.237
± 0.006
0.583
± 0.005
52.87
± 1.0
−0.222
± 0.021
Claude Opus 4.80.725
± 0.002
40.30
± 0.8
−0.643
± 0.004
0.589
± 0.006
52.63
± 0.8
−0.254
± 0.023
0.605
± 0.008
50.94
± 1.1
−0.300
± 0.019
Claude Opus 4.60.762
± 0.002
35.16
± 0.5
−0.788
± 0.007
0.603
± 0.003
52.35
± 0.9
−0.282
± 0.008
0.598
± 0.002
53.32
± 0.5
−0.263
± 0.006
Open-weight
GLM-5 0.731
± 0.006
38.54
± 0.6
−0.686
± 0.016
0.625
± 0.004
50.02
± 1.0
−0.372
± 0.024
0.632
± 0.002
49.96
± 0.4
−0.398
± 0.017
Qwen3.5-397B0.759
± 0.005
36.54
± 0.7
−0.796
± 0.021
0.639
± 0.004
48.49
± 1.2
−0.422
± 0.007
0.643
± 0.010
48.90
± 0.9
−0.441
± 0.027
Kimi K2.50.773
± 0.002
36.30
± 0.8
−0.837
± 0.011
0.637
± 0.010
49.37
± 2.2
−0.420
± 0.024
0.658
± 0.009
48.07
± 1.7
−0.439
± 0.005
MiniMax M2.50.758
± 0.005
35.68
± 0.9
−0.797
± 0.011
0.654‡
± 0.012
46.87
± 0.7
−0.461
± 0.031
0.640
± 0.007
47.19
± 1.6
−0.413
± 0.022
DeepSeek-V3.20.805
± 0.004
34.34
± 1.0
−0.991
± 0.017
0.655
± 0.012
47.73
± 1.9
−0.464
± 0.042
0.666
± 0.019
47.65
± 1.5
−0.508
± 0.064
gpt-oss-120b0.896
± 0.004
32.44
± 0.5
−1.378
± 0.023
0.699‡
± 0.010
41.95
± 0.6
−0.594
± 0.020
0.696§
± 0.012
43.03
± 0.7
−0.584
± 0.052
Nemotron 3 Super0.882 †
± 0.006
30.84
± 0.5
−1.516
± 0.021
0.695‡
± 0.011
43.49
± 1.2
−0.743
± 0.038
0.688§
± 0.019
44.89
± 2.7
−0.720
± 0.031
Uniform reference0.771 22.9—0.771 22.9—0.771 22.9—
Market reference0.498 64.5—0.498 64.5—0.498 64.5—
4.5 EVALUATION ANDLEARNING
We evaluate forecasts primarily with the multiclass Brier score (Brier, 1950), and additionally re-
port top-label accuracy, dataset-level calibration error (Guo et al., 2017), and market-relative mea-
sures such as Information-α. Each episode supports trajectory-level analyses of how beliefs evolve
(Appendix B.6 and B.7). With trajectory logging, each step also retainsH t and, in memory-on
mode, the notebook, to which outcome-based feedback can be attached. Evaluation events use these
records for benchmarking, and training events supply trajectories and feedback for learning, which
we demonstrate with supervised fine-tuning in Section 5.5.
5 EXPERIMENTS
5.1 EXPERIMENTALSETUP
We evaluate 12 proprietary and open-weight models on 230 held-out events (797 event–date pairs),
with four rollouts per pair. To examine the roles of research tools and cross-date memory, we
compare three settings on identical scheduled forecasting tasks:no-tools, which forecasts without
external tools (Figure 9);memory-free, which provides date-restricted search, article reads, and
Python tools but starts from a fresh context at each date (Figure 10); andmemory-on, which uses the
same tools while carrying a belief notebook across forecast dates within each rollout (Figure 11). To
mitigate outcome leakage, all models have a reported knowledge or training-data cutoff, or otherwise
a checkpoint release date, preceding the evaluation period (Table 8). A complementary no-tools
diagnostic finds no evidence of widespread outcome recall (Appendix B.1). Full configurations and
tool budgets are provided in Appendix B.2.
7

Preprint
0–1/3 1/3–2/3 2/3–1
(a)  Forecast Step Position
0.4
0.5
0.6
0.7
0.8Brier
Q1 Q2 Q3 Q4
(b)  New Evidence |ΔEt|
0.00
−0.05
−0.10
ΔBriert
0.0 0.5 1.0 1.5
(c)  Evidence Capture κ
0.00
0.05
0.10
−ΔBrier1 → T
ρ = 0.74 κ = 1
Opus4.6
GPT-5.6
GPT-5.5
Opus4.8
GPT-5.4

GLM-5
Kimi2.5
DS-V3.2
Qwen3.5
MiniMax
gpt-oss
Nemotron
Memory-Free Memory-On No Tools Market Proprietary Open-Weight
Figure 4:Forecast improvements track newly recorded evidence.(a) Brier across early, middle,
and late thirds of each event trajectory, with equal event weighting; shading shows the range of
model means. (b) Consecutive-step Brier change by new-evidence quartile, using leave-one-model-
out evidence indices. (c) Evidence captureκversus first-to-last Brier improvement with memory;
correlation is across 12 models, with the no-tools setting shown as a reference. Scores use the same
pairing and uniform fallback as Table 2; (a,b) show 95% event-bootstrap CIs. See Appendix B.7 for
definitions and sensitivity analyses.
We evaluate forecasting performance using multiclass Brier score, top-label accuracy, and
Information-α, which measures the agent’s log-score advantage over the market on the realized
outcome (positive values favor the agent). Uniform forecasts and historical market probabilities
serve as contextual references, although the market may incorporate information beyond our news
archive and its probabilities are never exposed to agents. Unusable forecasts are replaced with uni-
form distributions over theKpossible outcomes, yielding a Brier score of1−1/Kand fractional-tie
accuracy of1/K. Longitudinal averages weight events equally, while all 95% confidence intervals
and paired comparisons use event-level resampling (Appendix B.3).
5.2 OVERALLFORECASTINGPERFORMANCE
Research tools improve forecasting across model families.Relative to no tools, memory-free
research lowers Brier and improves accuracy for all 12 models, and every paired 95% CI excludes
zero (Tables 2 and 13). GPT-5.5, for example, improves from 0.698 to 0.564 in Brier and from
43.85% to 57.69% in accuracy, and the open-weight DeepSeek-V3.2 improves from 0.805 to 0.655
and from 34.34% to 47.73%.
Proprietary models achieve lower Brier scores with tools.In both tool-enabled settings, all
five proprietary models have lower mean Brier than every open-weight model. The proprietary
group is 0.078 lower on average without memory (95% CI[0.056,0.103]), although the closest pair,
Claude Opus 4.6 and GLM-5, is not statistically distinguishable in a paired comparison. GPT-5.6
Sol achieves the lowest Brier without and with memory (0.554 and 0.546), and its lead over GPT-5.5
is significant only with memory (Appendix C.1). GLM-5 is the strongest open-weight model (0.625
and 0.632).
Accuracy and Brier can disagree through calibration.GPT-5.5 has the highest memory-free
accuracy (57.69%) but is underconfident. Its top-ranked outcome receives 0.50 probability on av-
erage while being correct on 58% of usable forecasts, the largest top-label calibration error among
the 12 models (Appendix C.3). GPT-5.6 Sol is slightly less accurate (56.36%; the paired accuracy-
difference CI includes zero), partly because 4.49% of its memory-free runs stop before a final an-
swer, yet it has lower Brier (0.554 versus 0.564) and higher Information-α(−0.138versus−0.186).
With uniform fallback, all 12 models beat the uniform reference in Brier under both tool-enabled set-
tings. This convention does not imply successful output, since 19.45% of gpt-oss-120b’s memory-
free reports are unusable (Appendix B.4).
8

Preprint
1 2 3 4 5
(a)  Forecast Step t
0
1
2
3
4Cost per Forecast (USD)
Q1 Q2 Q3 Q4
(b)  Evidence Ak quartile
−50
−25
0
Δ vs. Memory-Free (%)
Cost
Input Tokens
Tool Calls
−50 −25 0
(c)  Δ vs. Memory-Free (%)
Input Tokens
Output Tokens
Tool Iterations
Tool Calls
Searches
Scrapes
Python Calls Carried Steps
First Step
Memory-Free Memory-On No Tools
Figure 5:Memory lowers research cost, mostly after the first forecast.(a) Mean API cost per
forecast step across five proprietary models; later steps cover fewer events (67/230 at step 4; 25/230
at step 5). (b) Consecutive-step Brier changes across quartiles of the leave-one-model-out new-
evidence indexA k(e, t). (c) The same changes at the first versus later steps; notebooks are only
available after the first step. Negative values denote reductions. Tokens and tool calls use all 12
models; intervals are 95% event-bootstrap CIs.
Memory yields model-dependent changes in forecast quality.Adding a belief notebook lowers
mean Brier for six models and raises it for the other six. None of the six improvements has a 95%
CI that excludes zero, whereas memory significantly raises Brier for Claude Opus 4.8 (+0.016,
[0.006,0.025]) and Kimi K2.5 (+0.021,[0.002,0.041]) on all recorded pairs (Table 13). Much of
this split comes from output reliability. For GPT-5.6 Sol, the share of forecasts without a usable
answer falls from 4.49% to 0.53% with memory, yet on forecasts usable in both settings the paired
Brier difference is only+0.0010. We therefore separate memory’s effects on forecast quality and
output reliability from its effect on research cost (Section 5.4).
The market reference remains ahead across evaluation metrics.The market achieves Brier
0.498 and accuracy 64.55%, against the best model scores of 0.546 and 57.69%. Paired on the
same event–dates, the Brier gap of the best configuration is 0.050 (95% CI[0.019,0.082]), and
every configuration has a strictly positive paired Brier-gap CI. Information-αis also negative for
every model and setting, with all 95% CIs below zero (Appendix C.1). Because the market may
incorporate information outside the agents’ archive, it serves as an external reference rather than an
information-matched baseline.
5.3 FORECASTING OVERTIME
Forecasts improve over time with research tools.Figure 4(a) compares forecasts at the early,
middle, and late stages of each event. Mean Brier decreases from 0.670 to 0.606 with memory-
free research and from 0.671 to 0.612 with memory-on research. In contrast, the no-tools baseline
remains nearly unchanged near 0.769. All 12 models achieve lower mean Brier in the late than in the
early stage with memory-free research, each with a 95% CI below zero (Appendix C.4). The market
improves more sharply, from 0.597 to 0.438. The improvement is concentrated in events on which
the market also moved toward the outcome (Appendix C.4). These results show that agents benefit
from access to dated information as events unfold, even without retaining their previous research.
Larger improvements coincide with more new evidence.We approximate newly available ev-
idence using dated entries in belief notebooks. For each model, the leave-one-model-out evidence
indexA k(e, t)averages the number of newly dated entries recorded by other models between con-
secutive forecasts (Appendix B.6). For memory-free agents, mean step-to-step Brier change ranges
from−0.007in the lowest index quartile to−0.071in the highest (Figure 4(b)). Memory-on agents
show a similar pattern, while no-tools forecasts change little across quartiles. Models recording
more newly dated evidence also achieve larger episode-level improvements (Spearmanρ= 0.74,
Figure 4(c)), although this association is between models rather than within them (Appendix B.7).
9

Preprint
Table 3:Supervised fine-tuning results.Paired SFT−base differences (∆) are computed before
rounding; event-level bootstrap 95% CIs exclude zero for Brier ([−0.214,−0.139]) and accuracy
([+5.1,+11.2]). Unusable forecasts (0% base, 0.5% SFT) receive the uniform fallback.
Brier↓Acc.↑Tool calls
All Binary Multi-option (%) / forecast
Uniform 0.771 0.500 0.832 22.9 –
Student (base) 0.924 0.704 0.975 34.8 1.4
+ Dojo SFT 0.749 0.539 0.797 42.8 3.7
Paired∆−0.176−0.165−0.178 +8.1 +2.3
5.4 COSTANALYSIS
Memory reduces the cost of repeated forecasting.For the five proprietary models, memory-on
execution costs less per forecast than memory-free execution in every case, with reductions ranging
from 8% for Claude Opus 4.6 to 33% for GPT-5.5 (median 24%; all paired 95% CIs exclude zero;
Appendix B.5). GPT-5.5, for example, costs $3.90 instead of $5.85 per forecast, while its paired
Brier difference of+0.007has a CI that includes zero. Both settings cost about the same at the
first forecast. Savings emerge from the second forecast onward, are largest when little new evidence
has appeared, and coincide with fewer input tokens, tool iterations, and research calls (Figure 5).
This pattern is consistent with agents reusing earlier findings, and lower research cost is memory’s
clearest benefit in the evaluated protocols.
5.5 TRAININGDEMONSTRATION
We investigate whetherForecast-Dojocan also serve as a training environment by leverag-
ing its collected agent interactions and outcome feedback. Using Qwen3-235B-A22B-Thinking-
2507 (Yang et al., 2025a), we generate four memory-free trajectories for each of 3,965 event–date
tasks drawn from 1,023 training events (August 2025 to February 2026). We select one demon-
stration per task using a weighted combination of Brier score, accuracy, and tool use, leveraging
known outcomes to guide offline selection (Appendix C.5). We then fine-tune Qwen3-30B-A3B-
Thinking-2507 (Yang et al., 2025a) for three epochs using next-token cross-entropy over assistant
tokens, including reasoning and tool calls (Appendix C.5).
On 230 temporally held-out events, the fine-tuned model improves both Brier score and accuracy
over its base (Table 3). Brier decreases from 0.924 to 0.749, with gains on both binary and multi-
choice forecasts, while accuracy rises from 34.8% to 42.8%. The fine-tuned model also makes more
tool calls (3.7 vs. 1.4 per forecast). To examine the role of predictive confidence, we conduct an ora-
cle uniform-shrinkage analysis. Rescaling the base model’s probabilities reduces its Brier to 0.752,
nearly matching the unadjusted SFT score of 0.749. However, shrinkage preserves top-1 predictions
and therefore cannot account for the observed accuracy improvement (Appendix C.5). Together,
these results demonstrate the potential ofForecast-Dojoas a training environment, where recorded
agent trajectories can support improved forecasting on temporally held-out events.
6 CONCLUSION
We introduceForecast-Dojo, a replayable environment that transforms resolved prediction-market
events into temporally grounded, multi-step forecasting episodes. By providing agents with identical
forecast schedules and time-restricted information,Forecast-Dojoenables controlled evaluation
of how forecasting performance, evidence use, and research efficiency evolve over time. Across 12
models, research tools improve both Brier score and accuracy, with larger forecast gains coinciding
with more newly recorded evidence. Persistent memory reduces research costs more consistently
than it improves forecast quality, revealing a distinction between efficient information reuse and
better predictions. Beyond evaluation,Forecast-Dojosupports learning from recorded agent in-
teractions: supervised fine-tuning improves student accuracy from 34.8% to 42.8% on temporally
10

Preprint
held-out events. Together, these findings establishForecast-Dojoas a unified foundation for eval-
uating, understanding, and improving forecasting agents as new information unfolds.
REFERENCES
Anthropic. Claude opus 4.6 system card.https://www.anthropic.com/system-cards, February
2026a. Claude Opus 4.6.
Anthropic. Introducing claude opus 4.8.https://www.anthropic.com/news/claude-opus-4-8,
May 2026b. Accessed 2026-09-22.
Glenn W. Brier. Verification of forecasts expressed in terms of probability.Monthly Weather Review,
78(1):1–3, 1950.
Nikhil Chandak, Shashwat Goel, Ameya Prabhu, Moritz Hardt, and Jonas Geiping. Scaling open-
ended reasoning to predict the future.arXiv preprint arXiv:2512.25070, 2025.
Pu Cheng, Juncheng Liu, and Yunshen Long. Polybench: Benchmarking llm forecasting and trading
capabilities on live prediction market data.arXiv preprint arXiv:2604.14199, 2026.
Yizhou Chi, Eric Chamoun, Zifeng Ding, and Andreas Vlachos. Worldreasoner: Evaluating whether
language model agents forecast events with valid reasoning.arXiv preprint arXiv:2606.11816,
2026.
Matthijs Douze, Alexandr Guzhva, Chengqi Deng, Jeff Johnson, Gergely Szilvasy, Pierre-
Emmanuel Mazaré, Maria Lomeli, Lucas Hosseini, and Hervé Jégou. The faiss library.IEEE
Trans. Big Data, 12(2):346–361, 2026. doi: 10.1109/TBDATA.2025.3618474. URLhttps:
//doi.org/10.1109/TBDATA.2025.3618474.
Shashwat Goel, Nikhil Chandak, Arvindh Arun, Ameya Prabhu, Steffen Staab, Moritz Hardt,
Maksym Andriushchenko, and Jonas Geiping. Futuresim: Replaying world events to evaluate
adaptive agents.arXiv preprint arXiv:2605.15188, 2026.
Google Search Central. Article structured data.https://developers.google.com/search/
docs/appearance/structured-data/article. Accessed 2026.
Ramanathan V . Guha, Dan Brickley, and Steve Macbeth. Schema.org: evolution of structured data
on the web.Commun. ACM, 59(2):44–51, 2016. doi: 10.1145/2844544. URLhttps://doi.
org/10.1145/2844544.
Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q. Weinberger. On calibration of modern neural
networks. In Doina Precup and Yee Whye Teh (eds.),Proceedings of the 34th International
Conference on Machine Learning, ICML 2017, Sydney, NSW, Australia, 6-11 August 2017, vol-
ume 70 ofProceedings of Machine Learning Research, pp. 1321–1330. PMLR, 2017. URL
http://proceedings.mlr.press/v70/guo17a.html.
Danny Halawi, Fred Zhang, Yueh-Han Chen, and Jacob Steinhardt. Approaching human-
level forecasting with language models. In Amir Globersons, Lester Mackey, Danielle
Belgrave, Angela Fan, Ulrich Paquet, Jakub M. Tomczak, and Cheng Zhang (eds.),Ad-
vances in Neural Information Processing Systems 37: Annual Conference on Neural In-
formation Processing Systems 2024, NeurIPS 2024, Vancouver, BC, Canada, December
10 - 15, 2024, 2024. URLhttp://papers.nips.cc/paper_files/paper/2024/hash/
5a5acfd0876c940d81619c1dc60e7748-Abstract-Conference.html.
Scott Jeen, Matthew Aitchison, Maximilian Anthony Hugh Clark, Toby Shevlane, and Ben Day.
Reaching the frontier of ai forecasting with reinforcement learning. InForecasting as a New
Frontier of Intelligence, 2026.
Woojeong Jin, Rahul Khanna, Suji Kim, Dong-Ho Lee, Fred Morstatter, Aram Galstyan, and Xiang
Ren. Forecastqa: A question answering challenge for event forecasting with temporal text data. In
Chengqing Zong, Fei Xia, Wenjie Li, and Roberto Navigli (eds.),Proceedings of the 59th Annual
Meeting of the Association for Computational Linguistics and the 11th International Joint Con-
ference on Natural Language Processing, ACL/IJCNLP 2021, (Volume 1: Long Papers), Virtual
11

Preprint
Event, August 1-6, 2021, pp. 4636–4650. Association for Computational Linguistics, 2021. doi:
10.18653/V1/2021.ACL-LONG.357. URLhttps://doi.org/10.18653/v1/2021.acl-long.
357.
Hailey Joren, Jianyi Zhang, Chun-Sung Ferng, Da-Cheng Juan, Ankur Taly, and Cyrus Rashtchian.
Sufficient context: A new lens on retrieval augmented generation systems. InThe Thirteenth
International Conference on Learning Representations, ICLR 2025, Singapore, April 24-28, 2025.
OpenReview.net, 2025. URLhttps://openreview.net/forum?id=Jjr2Odj8DJ.
Armand Joulin, Edouard Grave, Piotr Bojanowski, Matthijs Douze, Hervé Jégou, and Tomás
Mikolov. Fasttext.zip: Compressing text classification models.CoRR, abs/1612.03651, 2016.
URLhttp://arxiv.org/abs/1612.03651.
Armand Joulin, Edouard Grave, Piotr Bojanowski, and Tomás Mikolov. Bag of tricks for efficient
text classification. In Mirella Lapata, Phil Blunsom, and Alexander Koller (eds.),Proceedings of
the 15th Conference of the European Chapter of the Association for Computational Linguistics,
EACL 2017, Valencia, Spain, April 3-7, 2017, Volume 2: Short Papers, pp. 427–431. Association
for Computational Linguistics, 2017. doi: 10.18653/V1/E17-2068. URLhttps://doi.org/10.
18653/v1/e17-2068.
Ezra Karger, Houtan Bastani, Yueh-Han Chen, Zachary Jacobs, Danny Halawi, Fred Zhang, and
Philip Tetlock. Forecastbench: A dynamic benchmark of AI forecasting capabilities. InThe
Thirteenth International Conference on Learning Representations, ICLR 2025, Singapore, April
24-28, 2025. OpenReview.net, 2025. URLhttps://openreview.net/forum?id=lfPkGWXLLf.
Amit Arnold Levy. Reinforcement learning for llm-based event forecasting.arXiv preprint
arXiv:2606.15917, 2026.
Tom Liptay, Dan Schwarz, Rafael Poyiadzi, Jack Wildman, and Nikos I Bosse. Evaluating strategic
reasoning in forecasting agents.arXiv preprint arXiv:2604.26106, 2026.
Kevin Murphy. Agentic forecasting using sequential bayesian updating of linguistic beliefs.arXiv
preprint arXiv:2604.18576, 2026.
Sebastian Nagel. Common crawl news dataset, 2016. URLhttps://data.commoncrawl.org/
crawl-data/CC-NEWS/index.html.
Daniel Paleka, Abhimanyu Pallavi Sudhir, Alejandro Alvarez, Vineeth Bhat, Adam Shen, Evan
Wang, and Florian Tramèr. Consistency checks for language model forecasters.arXiv preprint
arXiv:2412.18544, 2025.
Guilherme Penedo, Hynek Kydlícek, Loubna Ben Allal, Anton Lozhkov, Margaret Mitchell,
Colin A. Raffel, Leandro von Werra, and Thomas Wolf. The fineweb datasets: Decant-
ing the web for the finest text data at scale. In Amir Globersons, Lester Mackey, Danielle
Belgrave, Angela Fan, Ulrich Paquet, Jakub M. Tomczak, and Cheng Zhang (eds.),Ad-
vances in Neural Information Processing Systems 37: Annual Conference on Neural In-
formation Processing Systems 2024, NeurIPS 2024, Vancouver, BC, Canada, December
10 - 15, 2024, 2024. URLhttp://papers.nips.cc/paper_files/paper/2024/hash/
370df50ccfdf8bde18f8f9c2d9151bda-Abstract-Datasets_and_Benchmarks_Track.html.
Rushi Qiang, Yuchen Zhuang, Yinghao Li, Dingu Sagar V K, Rongzhi Zhang, Changhao Li,
Ian Shu-Hei Wong, Sherry Yang, Percy Liang, Chao Zhang, and Bo Dai. Mle-dojo: Interac-
tive environments for empowering llm agents in machine learning engineering.arXiv preprint
arXiv:2505.07782, 2025.
Jack W Rae, Sebastian Borgeaud, Trevor Cai, Katie Millican, Jordan Hoffmann, Francis Song, John
Aslanides, Sarah Henderson, Roman Ring, Susannah Young, et al. Scaling language models:
Methods, analysis & insights from training gopher.arXiv preprint arXiv:2112.11446, 2021.
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi
Zhou, Wei Li, and Peter J. Liu. Exploring the limits of transfer learning with a unified text-to-text
transformer.J. Mach. Learn. Res., 21:140:1–140:67, 2020. URLhttps://jmlr.org/papers/
v21/20-074.html.
12

Preprint
Stephen E. Robertson and Hugo Zaragoza. The probabilistic relevance framework: BM25 and
beyond.Found. Trends Inf. Retr., 3(4):333–389, 2009. doi: 10.1561/1500000019. URLhttps:
//doi.org/10.1561/1500000019.
Schema.org. datePublished.https://schema.org/datePublished. Accessed 2026.
ByteDance Seed. Futurex-pro: Extending future prediction to high-value vertical domains.CoRR,
abs/2601.12259, 2026. doi: 10.48550/ARXIV .2601.12259. URLhttps://doi.org/10.48550/
arXiv.2601.12259.
Jack Wildman, Nikos I Bosse, Daniel Hnyk, Peter Mühlbacher, Finn Hambly, Jon Evans, Dan
Schwarz, Lawrence Phillips, et al. Bench to the future: A pastcasting benchmark for forecasting
agents.arXiv preprint arXiv:2506.21558, 2025.
An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu,
Chang Gao, Chengen Huang, Chenxu Lv, et al. Qwen3 technical report.arXiv preprint
arXiv:2505.09388, 2025a.
Qingchuan Yang, Simon Mahns, Sida Li, Anri Gu, Jibang Wu, and Haifeng Xu. Llm-as-a-prophet:
Understanding predictive intelligence with prophet arena.arXiv preprint arXiv:2510.17638,
2025b.
Chenchen Ye, Ziniu Hu, Yihe Deng, Zijie Huang, Mingyu Derek Ma, Yanqiao Zhu, and Wei Wang.
Mirai: Evaluating llm agents for event forecasting.arXiv preprint arXiv:2407.01231, 2024.
Zhangdie Yuan, Zifeng Ding, and Andreas Vlachos. Do language models update their forecasts with
new information?arXiv preprint arXiv:2509.23936, 2025.
Zhiyuan Zeng, Jiashuo Liu, Siyuan Chen, Tianci He, Yali Liao, Jinpeng Wang, Zaiyuan Wang,
Yang Yang, Lingyue Yin, Mingren Yin, Zhenwei Zhu, Tianle Cai, Zehui Chen, Jiecao Chen,
Yantao Du, Xiang Gao, Jiacheng Guo, Liang Hu, Jianpeng Jiao, Xiangsheng Li, Jingkai Liu,
Shuang Ni, Zhoufutu Wen, Ge Zhang, Kaiyuan Zhang, Xin Zhou, Jose H. Blanchet, Xipeng
Qiu, Mengdi Wang, and Wenhao Huang. Futurex: An advanced live benchmark for LLM agents
in future prediction.CoRR, abs/2508.11987, 2025. doi: 10.48550/ARXIV .2508.11987. URL
https://doi.org/10.48550/arXiv.2508.11987.
Jaden Zhang, Gardenia Liu, Oliver Johansson, Hileamlak Yitayew, Kamryn Ohly, and Grace
Li. Prediction arena: Benchmarking AI models on real-world prediction markets.CoRR,
abs/2604.07355, 2026. doi: 10.48550/ARXIV .2604.07355. URLhttps://doi.org/10.48550/
arXiv.2604.07355.
Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, Huan Lin, Baosong Yang, Pengjun Xie,
An Yang, Dayiheng Liu, Junyang Lin, Fei Huang, and Jingren Zhou. Qwen3 embedding: Ad-
vancing text embedding and reranking through foundation models.CoRR, abs/2506.05176, 2025.
doi: 10.48550/ARXIV .2506.05176. URLhttps://doi.org/10.48550/arXiv.2506.05176.
Xinyue Zhao, Ruiyi Zhang, Liqin Ye, Rui Cao, Pengtao Xie, and Sudheer Chava. Can llms take the
pulse of the economy? A real-time evaluation of LLM nowcasts on macroeconomic indicators.
CoRR, abs/2608.30110, 2026. doi: 10.48550/ARXIV .2608.30110. URLhttps://doi.org/10.
48550/arXiv.2608.30110.
Andy Zou, Tristan Xiao, Ryan Jia, Joe Kwon, Mantas Mazeika, Richard Li, Dawn Song, Jacob
Steinhardt, Owain Evans, and Dan Hendrycks. Forecasting future world events with neural net-
works. InAdvances in Neural Information Processing Systems (NeurIPS), Datasets and Bench-
marks Track, 2022.
13

Preprint
Appendix forForecast-Dojo
A Dataset and Benchmark Details 14
A.1 Information Corpus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
A.2 Event Collection and Filtering . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
A.3 Forecast-Step Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
B Experiment Details 18
B.1 Knowledge Cutoffs and Checkpoint Dates . . . . . . . . . . . . . . . . . . . . . . 18
B.2 Models and Execution Protocols . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
B.3 Evaluation Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
B.4 Forecast Validity and Failure Handling . . . . . . . . . . . . . . . . . . . . . . . . 20
B.5 Inference Cost and Tool Usage . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
B.6 Measuring Newly Recorded Evidence . . . . . . . . . . . . . . . . . . . . . . . . 21
B.7 Evidence Capture and Forecast Improvement . . . . . . . . . . . . . . . . . . . . 22
C Additional Results 23
C.1 Statistical Uncertainty and Model Comparisons . . . . . . . . . . . . . . . . . . . 23
C.2 Sensitivity to Scoring Conventions . . . . . . . . . . . . . . . . . . . . . . . . . . 25
C.3 Calibration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
C.4 Longitudinal Robustness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
C.5 Training Use Case . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
D Limitations 27
E Prompts 27
E.1 No-Tools Forecasting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
E.2 Memory-Free Forecasting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
E.3 Memory-On Forecasting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
E.4 Corpus-Side Event Filtering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
A DATASET ANDBENCHMARKDETAILS
We describe in detail how we construct our information corpus (§A.1), collect and filter forecasting
events (§A.2), and select forecast dates for each task (§A.3).
A.1 INFORMATIONCORPUS
Corpus source.We build the retrieval corpus from the monthly CC-News releases of Common
Crawl (Nagel, 2016) from March 2025 through May 2026. For each news page, we extract the title,
summary, body text, URL, crawl time, and structured publication metadata.
Text and quality filtering.Our filtering pipeline is summarized in Table 4. The first two stages
normalize the extracted text and retain English-language documents using fastText (Joulin et al.,
14

Preprint
Stage Deployed criterion
1. Cleaning Normalize whitespace and inline URLs; drop documents with an empty
cleaned title or body.
2. Language Keep documents that fastText identifies as English with confidence≥0.5.
3. Gopher repetition Apply duplicate-line, duplicate-paragraph, and repeatedn-gram checks.
4. Gopher quality Require 50–100,000 non-symbol tokens, mean word length in[3,10],
bounded symbol, bullet, and ellipsis ratios, alphabetic-word ratio≥0.75,
and at least two stop-word occurrences.
5. C4 quality Apply C4 line and document cleanup and require at least five sentences.
6. FineWeb quality Require at least12%of lines to end with terminal punctuation and at most
80%short lines.
7a. URL deduplication Remove documents whose canonicalized URL has already been seen.
7b. Title deduplication Suppress identical normalized titles appearing within a seven-day window,
retaining the earliest-published document.
7c. MinHash deduplica-
tion
Apply MinHash-LSH over word 5-grams and retain the earliest-published rep-
resentative of each near-duplicate component.
8. Serving-date window Retain documents whose resolved publication date falls within March 1, 2025
through May 31, 2026.
Table 4: Corpus filtering pipeline. The aggregate post-quality count is reported in Table 6a.
2017; 2016), matching the language of the benchmark questions. The remaining stages adapt quality
filters from Gopher (Rae et al., 2021), C4 (Raffel et al., 2020), and FineWeb (Penedo et al., 2024).
Publication dates and temporal integrity.We read publication and modification timestamps
from structured page metadata (Guha et al., 2016; Schema.org; Google Search Central), such as
schema.org and OpenGraph fields, and discard values outside 2010–2030. Each article receives the
UTC day of the structured timestamp closest to its crawl time, preferring the later one in case of a
tie and never exceeding the crawl time. Articles without a valid structured timestamp receive their
crawl day. Across the corpus, the assigned date comes from publication metadata for58.6%of
articles, from modification metadata for28.3%, and from the crawl time for13.1%.
Retrieval at forecast dateτ t includes articles assigned toτ t itself. Because dates are assigned at day
precision, they do not show that a page existed at a particular time of day or that an edited page
already had its captured content on the assigned date. The leakage audit in Appendix A.2 addresses
the violations we observed.
Duplicate suppression.We remove repeated coverage by URL matching, suppression of identical
titles within a seven-day window, and MinHash near-duplicate detection over word 5-grams, keeping
the earliest-published copy in each case. When a URL was captured more than once, we keep a
single capture, so a retained page is not necessarily its earliest version.
Indexing and temporal restriction.Each retained article is embedded with Qwen3-Embedding-
8B (Zhang et al., 2025) using its title, summary, and body. The normalized embeddings are stored
in exact inner-product indices, one per month. At forecast dateτ t, search is restricted to
I≤τt ={d∈ I: 2025-03-01≤t(d)≤τ t}.
The date restriction is applied before similarity ranking, and full-article access independently
rechecks the same temporal constraint.
A.2 EVENTCOLLECTION ANDFILTERING
Event collection and market beliefs.We construct forecasting questions from resolved Polymar-
ket events. A binary event is a single yes/no market, and a multi-option event is a group of at least
two mutually exclusive markets. Other market layouts are excluded. For market legk, lett start k and
tclose k denote its recorded start and close times. We define the complete tradeable span as
[tstart, tclose] =

min
k
tstart k ,max k tclose k

.
15

Preprint
Criterion Binary Multi-option
Forecasting horizon≥8days≥8days
Active day≥6trades,≥200shares≥5trades,≥50shares
Active-day coverageρ Q ≥0.80ρ Q ≥0.70
Max. inactive runS Q ≤3S Q ≤5
Residual uncertaintya Q ≥0.05a Q ≥0.05
Temporal signalV Q ≥10 −6 and(C Q ≥0.20∨V Q ≥0.50)
Table 5: Market-side event-selection criteria.
Ground-truth labels are derived from terminal YES prices: binary markets resolve to YES at≥0.99
and to NO at≤0.01, while multi-option events require exactly one YES-resolved option. We
reconstruct the daily market beliefm Q,t ∈∆ K−1 from the UTC-day mean of YES trade prices. For
a multi-option event with priced optionsA t,
mQ,t(k) = xt,kP
j∈At xt,j
, k∈A t,
with missing options left undefined rather than imputed.
Market-side filtering.We first filter events for a meaningful forecasting horizon and a reliable,
nontrivial market-belief trajectory. Events must span at least eight UTC calendar days. We then
define a day asactivewhen the trade count and share volume on the market leg corresponding to the
realized outcome exceed the type-specific thresholds in Table 5. LetρQ denote the fraction of active
days andS Q the longest consecutive run of inactive days.
Among events passing this activity filter, we measure task nontriviality from the market probability
assigned to the realized outcome,m Q,t(Y). LetF Q denote active days with an observed belief, and
let∆ t =m Q,t(Y)−m Q,t−1(Y)for adjacent calendar days with valid active-day observations. We
define
aQ = 1 |FQ| X t∈FQ −log clip  mQ,t(Y),10 −6,1−10 −6 , V Q = X t |∆t|, C Q = P t ∆tP t |∆t| .
These remove events that are already nearly certain or have little meaningful temporal variation.
Corpus-side filtering.Market-side filtering identifies events with usable forecasting trajectories,
but does not establish whether the frozen information environment is suitable for forecasting. We
therefore apply a complementary corpus-side screen that evaluates both the sufficiency of pre-
resolution evidence and potential information leakage.
Evidence sufficiency.Following the sufficient-context framework of Joren et al. (2025), we as-
sess whether the retrieved information contains enough evidence to support an informed forecast.
We adapt this protocol to historical forecasting by first decomposing each event into targeted in-
formation needs. For each event surviving the market-side filters, we use Claude Opus 4.8 with
maximum reasoning effort (Anthropic, 2026b) to generate 4–7 predictive-evidence queries and 4–7
background/reference-class queries. Query generation explicitly targets information available be-
fore resolution and forbids searches for the realized outcome or post-resolution reports. See the full
decomposition prompt in Figure 12.
Sufficiency is evaluated once at the latest eligible forecasting state,
τ ⋆ =t close −2days.
The buffer is relative to the recorded market close. It reduces exposure to close-day reporting and
adjacent-day timestamp ambiguity, but does not ensure that the deciding event was still unresolved.
For each query, we retrieve dense (Qwen3-Embedding-8B) and BM25 (Robertson & Zaragoza,
2009) top-10 results restricted to[2025-03-01, τ⋆]and combine them using reciprocal-rank fusion,
RRF(d) =
X
q
X
r∈{dense,BM25}
1[d∈L q,r]
60 + rankq,r(d) .
16

Preprint
Table 6: Construction waterfalls for the deployed news corpus and forecasting events. Event counts
use the final June–March training and March–June evaluation splits.
(a) Corpus construction
Stage Removed Remaining
Stages 1–6 – 26,533,747
Stage 7a 194,940 26,338,807
Stage 7b 5,563,879 20,774,928
Stage 7c 1,124,734 19,650,194
Stage 8 823,25418,826,940
(b) Event selection
Stage Train Eval
Temporal split pool 13,671 13,920
Forecasting horizon 9,051 7,590
Market activity 1,965 423
Task nontriviality 1,777 378
Evidence sufficiency & judge1,338 230
Table 7: Tools details.
Tool Semantics and permissions
searchDense retrieval over the assigned-date window, with defaultk= 5. Returns article IDs, titles, URLs,
assigned dates, similarity scores, and short snippets. Candidate dates are restricted before ranking.
scrapeReturns the article body for an ID returned by search in the same forecast step, after rechecking the
date boundary. Bodies are truncated to 8,000 tokens.
pythonExecutes code for numerical analysis in an isolated runtime with networking disabled and no access
to benchmark data files, including the task files, news corpus, and retrieval index.
The 15 highest-ranked unique documents form the evidence setE Q. We then use Claude Opus
4.6 (Anthropic, 2026a) to classify the available evidence as {SUFFICIENT, PARTIAL, INSUFFI-
CIENT}. Only events receiving a SUFFICIENTverdict are eligible for the final benchmark.
Leakage control.The same judge additionally screens the retrieved evidence for potential outcome
leakage. This content-level check complements the metadata-level temporal restriction on retrieval
and provides an additional safeguard when the visible content of a page may not be fully reflected
by its assigned publication timestamp. The judge does not receive the structured realized outcome,
final market prices, or crowd trajectory.
Letv Q denote the evidence-sufficiency verdict andℓ Q the leakage flag. At this screening stage, an
event is eligible iff
vQ =SUFFICIENTandℓ Q = false.
See Figure 13 for the judge prompt and Table 6 for event filtering funnels.
A.3 FORECAST-STEPCONSTRUCTION
Temporal split.We split at the event level using the complete tradeable lifetime. An event enters
training ifft start ≥2025-06-01andt close <2026-03-01,and enters evaluation ifft start ≥
2026-03-01andt close <2026-06-01.Events that cross the March 1 boundary are excluded
from both splits.
Number of forecast steps.For eventQ, letD Q be its contiguous UTC daily grid. We reserve a
two-day buffer before the recorded close date and define
EQ ={d∈D Q : date(tclose)−d≥2}, n Q =|E Q|.
The number of forecast steps is
TQ = clamp

round √nQ,3,10  .
Date selection.Within the eligible grid, market movement is
bt =
(|mQ,t(YES)−m Q,t−1(YES)|,binary,
1
2
P
k |mQ,t(k)−m Q,t−1(k)|,multi-option,
with zero assigned when an adjacent belief is unavailable. Corpus activityc t is the total number of
indexed news articles published on calendar dayt. It is a global news-volume signal rather than an
17

Preprint
Table 8: Knowledge and release dates of evaluated models. We report an official knowledge or
training-data cutoff when available; otherwise, we use the public checkpoint release date.
Model Date Basis
Proprietary
GPT-5.6 Sol 2026-02-16 Cutoff
GPT-5.5 2025-12-01 Cutoff
GPT-5.4 2025-08-31 Cutoff
Claude Opus 4.8 2026-01 Cutoff
Claude Opus 4.6 2025-05 Cutoff
Open-weight
GLM-5 2026-02-11 Release
Qwen3.5-397B 2026-02-16 Release
Kimi K2.5 2026-01-27 Release
MiniMax M2.5 2026-02-12 Release
DeepSeek-V3.2 2025-12-01 Release
gpt-oss-120b 2024-06-01 Cutoff
Nemotron 3 Super 2026-02 Post-train
Note.“Release” denotes the public checkpoint release date when no official knowledge cutoff is reported.
event-specific relevance score. After independently max-normalizing both signals, eligible datee j
receives
sj = 0.7 ˜bej + 0.3 ˜cej + 10−3 j nQ −1 .
We partition the eligible sequence intoT Q contiguous equal-count bins and choose the highest-
scoring date from each bin. This preserves temporal coverage while favoring dates with larger belief
changes or greater overall news activity.
B EXPERIMENTDETAILS
B.1 KNOWLEDGECUTOFFS ANDCHECKPOINTDATES
Table 8 lists each model’s reported knowledge cutoff or checkpoint date. All dates precede the
evaluation period, which begins on March 1, 2026.
Diagnostic for outcome recall.To further assess potential outcome recall beyond the knowledge-
cutoff checks, we examine models’ no-tools forecasting performance directly. If models frequently
recalled resolved outcomes, they would be expected to perform well even when the contemporane-
ous market favored an incorrect outcome. The market favorite was wrong on 35.4% of evaluation
dates. On these dates, no-tools accuracy ranged from 11.4% to 16.9% across the 12 models, be-
low the 19.1% accuracy of a uniform forecast, compared with 41.5% to 63.3% when the market
favorite was correct. The same pattern holds for GPT-5.6 Sol, whose reported cutoff is closest to
the evaluation period (16.8% versus 63.3%). Moreover, no-tools Information-αat the first forecast
date is negative for every model. Together, these findings provide no evidence of widespread usable
outcome recall, although they cannot rule out partial memorization or other post-cutoff knowledge.
B.2 MODELS ANDEXECUTIONPROTOCOLS
Table 9 lists the decoding settings and tool budgets of the 12 model configurations. All runs use the
same 230 held-out events, four rollouts per date. Tool runs share a budget of 120 tool iterations and
400 calls per forecast step. No-tool runs remove the tools and the corpus and raise the output cap
to 65,536 tokens, since the whole forecast is then produced in a single call. Settings for the training
use case are given in Appendix C.5.
18

Preprint
Table 9:Model Evaluation Configurations.Max output tokens is the cap per model call and
includes reasoning tokens. default denotes the provider’s default value. Tool budgets are per forecast
step and identical in memory-free and memory-on mode; no-tool runs disable all tools.
Max output tokens Temperature / top-p/ top-kTool budget
Model Reasoning Tools No tools Tools No tools iters / calls
GPT-5.6 Sol max 32,768 65,536 default default 120 / 400
GPT-5.5 xhigh 32,768 65,536 default default 120 / 400
GPT-5.4 xhigh 32,768 65,536 default default 120 / 400
Opus 4.8 max 32,768 65,536 default default 120 / 400
Opus 4.6 max 32,768 65,536 default default 120 / 400
GLM-5 high 32,768 65,536 1.0 / 1.0 / default 1.0 / 1.0 / default 120 / 400
Kimi K2.5 high 32,768 65,536 1.0 / 1.0 / default 1.0 / 1.0 / default 120 / 400
DeepSeek V3.2 high 32,768 65,536 1.0 / 1.0 / default 1.0 / 1.0 / default 120 / 400
MiniMax M2.5 native a 32,768 65,536 1.0 / 1.0 / default 1.0 / 1.0 / default 120 / 400
Nemotron 3 Super high 32,768 65,536 1.0 / 1.0 / default 1.0 / 1.0 / default 120 / 400
gpt-oss-120b high 32,768 65,536 1.0 / 1.0 / default 1.0 / 1.0 / default 120 / 400
Qwen3.5-397B native a 32,768 65,536 1.0 / 1.0 / default 1.0 / 1.0 / default 120 / 400
a The model reasons by default and exposes no effort setting.
B.3 EVALUATIONMETRICS
Brier score.Leti= (e, t, r)index an event, forecast date, and rollout, and letY i denote the real-
ized outcome. For a usable probability report, negative entries are clipped to zero and the remaining
positive mass is normalized. Reported labels must match the offered outcome labels exactly. Omit-
ted outcomes receive zero probability, and probability placed on a label that matches no offered
outcome counts as error. LetU i be the union of the reported labels and the truth label. The multi-
class Brier score is
Bi =
X
c∈Ui
(pic −1{c=Y i})2 .
We use the standard[0,2]scale, without normalization by the number of outcomes or an additional
binary-event factor. A uniform forecast overK i offered outcomes has Brier score1−1/K i.
Accuracy.LetT i = arg maxc pic denote the set of outcomes assigned maximal probability. We
use fractional-tie accuracy,
ai = 1{Yi ∈ Ti} |Ti| .
Thus, a correct unique top prediction receives accuracy1, while ties split credit uniformly among
tied outcomes. A uniform forecast overK i outcomes therefore has accuracy1/K i.
Information-α.We measure improvement over the contemporaneous market belief using
αi = log max{pi(Yi), ϵ} −log max{pmarket,i(Yi), ϵ}, ϵ= 10 −3,
with natural logarithms; positive values favor the agent. We compute it for every recorded forecast
whose market probability for the realized outcome is available, using the uniform fallback for un-
usable reports. Neither realized outcomes nor market probabilities are provided to the forecasting
agent.
Log loss.We reportℓ i =−log max{p i(Yi),10 −3}with natural logarithms. An unusable report
contributeslogK i.
Top-label calibration.For a usable forecast, letc i = maxc pic be its top-ranked probability. We
group forecasts into 15 equal-width bins ofc i and reportECE = P b nb n |¯cb −¯ab|, where¯cb and¯ab
are the mean top-ranked probability and the mean fractional-tie accuracy in binb.
19

Preprint
Table 10:Forecast failure rates and causes across evaluation settings (%).Early denotes termi-
nation before a final answer due to context, token, or tool limits; Format denotes an unscorable final
report. Total includes missing or unusable forecasts, including invalid probability mass, over 3,188
scheduled forecasts per model and setting. Early and Format use recorded forecasts as the denomi-
nator and therefore need not sum to Total. Recorded unusable forecasts are scored as uniform, while
missing records are excluded from score means.
No tools Memory-free Memory-on
Model Early Format Total Early Format Total Early Format Total
GPT-5.6 Sol 0.00 0.03 0.03 4.49 0.00 4.49 0.41 0.00 0.53
GPT-5.5 0.00 0.06 0.06 0.16 0.09 0.25 0.00 0.03 0.03
GPT-5.4 0.00 0.00 0.00 0.09 0.00 0.09 0.00 0.00 0.00
Claude Opus 4.8 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Claude Opus 4.6 0.38 0.00 0.38 0.00 0.03 0.03 0.00 0.00 0.00
GLM-5 0.00 0.28 0.28 0.00 1.47 1.47 0.00 1.13 1.13
Kimi K2.5 0.00 0.00 0.00 0.03 2.13 2.16 0.00 2.45 2.45
DeepSeek V3.2 0.00 0.25 0.25 0.03 1.73 1.76 0.00 1.88 1.88
MiniMax M2.5 0.00 0.63 0.63 0.03 5.49 5.52 0.00 1.85 1.85
Nemotron 3 Super 0.00 9.16 9.16 10.35 7.72 18.07 2.37 8.52 11.39
gpt-oss-120b 0.00 0.00 0.00 0.00 19.45 19.45 0.00 13.64 13.64
Qwen3.5-397B 0.00 0.03 0.03 0.00 1.10 1.10 0.00 1.16 1.16
Statistical uncertainty.We account for dependencies among repeated forecasts of the same event
by computing 95% confidence intervals using percentile bootstrapping over the 230 evaluation
events (4,000 resamples; seed 0). For paired comparisons, we average the four rollouts within each
event–date before computing matched differences, except for memory comparisons, which preserve
event–date–rollout pairing. Bootstrap resampling is performed at the event level throughout. The±
values in Table 2 instead report the standard deviation across four rollout means, reflecting run-to-
run variability rather than event-level uncertainty.
B.4 FORECASTVALIDITY ANDFAILUREHANDLING
To ensure consistent scoring across models and evaluation settings, we assign a uniform forecast to
any recorded output that cannot be reliably scored, including incomplete reports, formatting viola-
tions (Appendix E), and predictions without positive finite probability mass. For an event withK i
possible outcomes, this yields a Brier score of1−1/K i, fractional-tie accuracy of1/K i, and log
loss oflogK i. This convention applies consistently across the main evaluation, longitudinal anal-
yses, and SFT experiments, while Information-αis computed only when the corresponding market
probability is available.
Missing records are distinguished from unusable outputs: they are excluded from metric averages
but included in the overall failure rates reported in Table 10. Of the 3,188 scheduled forecasts
per configuration, only two memory-on configurations have missing records: GPT-5.6 Sol (3,184
recorded) and Nemotron 3 Super (3,170 recorded). All other configurations have complete records.
Failure characteristics.Table 10 further distinguishes premature termination from completed but
unscorable reports. Early termination is uncommon overall, occurring in 0.03% of no-tools, 1.27%
of memory-free, and approximately 0.23% of memory-on forecasts. In the memory-free setting,
early stops arise primarily from output-token limits (0.52%), tool-iteration limits (0.41%), and con-
text overflow (0.31%), with tool-call limits accounting for another 0.03%. Failure patterns never-
theless vary substantially across models. For GPT-5.6 Sol, early termination accounts for all unus-
able memory-free forecasts (4.49%), falling to 0.41% with memory enabled. In contrast, gpt-oss-
120b’s failures arise entirely from completed but unscorable reports, affecting 19.45% and 13.64%
of memory-free and memory-on forecasts, respectively.
20

Preprint
5.6 Sol 5.5 5.4 4.8 4.6$0
$1
$2
$3
$4
$5
$6USD per forecast
GPT Claude Opus
0.18
4.45
3.38
0.25
5.85
3.90
0.20
4.49
3.52
0.25
2.74
2.02
0.28
2.91
2.66
a
No tools
Memory-free
Memory-on
0 50 100 150
MiniMax M2.5
Qwen3.5-397B
gpt-oss-120b
Kimi K2.5
GLM-5
Nemotron 3 Super
DeepSeek V3.2
Opus 4.8
Opus 4.6
GPT-5.5
GPT-5.4
GPT-5.6 Sol 136.6
89.9
70.3
33.2
22.9
39.6
33.9
24.9
24.3
21.7
19.1
16.7
b Memory-free
0 50 100 150
118.3
76.6
56.8
29.5
17.0
34.4
30.6
22.3
20.1
17.2
20.7
12.5
Memory-on
Research calls per forecast
Search Read Python
Figure 6:Inference cost and research tool usage across models.(a) Average provider-estimated
inference cost per recorded forecast under no-tools, memory-free, and memory-on settings for five
proprietary models with available pricing. (b) Average research calls per recorded forecast, decom-
posed into search, full-article reads, and Python calls, including unsuccessful calls. Open-weight
inference costs are omitted because comparable pricing is unavailable.
B.5 INFERENCECOST ANDTOOLUSAGE
Figure 6 characterizes the inference cost and research activity of forecasting agents across evaluation
settings. Panel (a) reports average provider-estimated costs for the five proprietary models with
available pricing, while panel (b) breaks down research calls into search, full-article reads, and
Python across all 12 models. Tool-enabled forecasting incurs substantially higher inference costs
than no-tools forecasting, whereas carrying a belief notebook reduces costs for all five priced models
and research calls for 11 of the 12 models.
To quantify these savings, we compute resource reductions over matched model–event–date–rollout
records using ratios of summed resources, with 95% confidence intervals from 4,000 event-level
bootstrap resamples. Memory-on reduces inference cost by 23.9%[20.6,27.3]for GPT-5.6 Sol,
33.3%[31.4,35.1]for GPT-5.5, and 21.5%[19.2,23.8]for GPT-5.4. Corresponding reductions are
26.2%[23.8,28.6]for Claude Opus 4.8 and 8.3%[6.2,10.4]for Claude Opus 4.6. These estimates
characterize provider-reported costs and observed tool usage rather than hardware-normalized effi-
ciency; comparable inference costs are unavailable for the open-weight models.
B.6 MEASURINGNEWLYRECORDEDEVIDENCE
Longitudinal evaluation.To characterize forecasting performance over time, we assign each fore-
cast steptof eventea normalized position(t−1)/(T e −1). We divide these positions into early,
middle, and late stages using the right-closed intervals[0,1/3],(1/3,2/3], and(2/3,1], respectively.
Brier scores are averaged within each event and stage before aggregation with equal event weights.
Figure 4(a) uses 223 events with agent observations across all three stages (224 for the market). We
compute 95% confidence intervals using 4,000 event-level bootstrap resamples.
Newly dated evidence.To examine how forecast improvements relate to newly available informa-
tion, we measure evidence recorded in memory-on belief notebooks. For modelk, rolloutr, event
e, and forecast stept≥2, we define
nk,r(e, t) =
X
a∈ledger(Mk,r (e,t))
1{τe,t−1 < d(a)≤τ e,t},
21

Preprint
Table 11:Consecutive-step Brier change by new-evidence quartile.Values correspond to Fig-
ure 4(b). Quartile thresholds are 1.49, 2.45, and 3.98 newly dated entries. Brackets indicate 95%
event-level bootstrap confidence intervals; negative values indicate improvement. The final column
reports the number of events contributing memory-free transitions.
Quartile No tools Memory-free Memory-on Market Events
Q1−0.002
[−0.010,+0.004]
−0.007
[−0.018,+0.005]
−0.000
[−0.010,+0.010]
−0.051
[−0.095,−0.013]
124
Q2−0.005
[−0.012,+0.003]
−0.024
[−0.049,−0.002]
−0.022
[−0.048,+0.002]
−0.046
[−0.086,−0.006]
146
Q3+0.002
[−0.004,+0.008]
−0.032
[−0.057,−0.009]
−0.031
[−0.057,−0.009]
−0.100
[−0.145,−0.056]
135
Q4+0.001
[−0.008,+0.009]
−0.071
[−0.115,−0.031]
−0.060
[−0.098,−0.025]
−0.096
[−0.140,−0.058]
103
whered(a)denotes the evidence date recorded in entrya. This counts notebook entries dated
between consecutive forecasts, including active and superseded entries, while excluding invalid or
future-dated evidence. Earlier evidence discovered later and entries carried over from previous steps
do not contribute.
Leave-one-model-out evidence index.To avoid directly relating a model’s forecast changes to
its own evidence-recording behavior, we construct a leave-one-model-out index. We first average
evidence counts over available rollouts of each model:
ownk(e, t) = 1 |Rk(e, t)| X r∈Rk(e,t) nk,r(e, t),
whereR k(e, t)denotes the available rollouts. We then average across the other models with avail-
able counts:
Ak(e, t) = 1 |Pk(e, t)| X j∈Pk(e,t) ownj(e, t),
whereP k(e, t)excludes modelk. We refer toA k(e, t)as thenew-evidence indexand use it as a
proxy for newly available evidence when analyzing modelk, including its memory-free forecasts.
For evaluation settings∈ {NT,MF,MO}, denoting no tools, memory-free, and memory-on, re-
spectively, letB (s) k,r(e, t)be the Brier score of modelkat event-step(e, t)in rolloutr. We measure
consecutive-step changes as
∆B(s) k,r(e, t) =B(s) k,r(e, t)−B(s) k,r(e, t−1),
where negative values indicate improvement. Figure 4(b) groups transitions by quartiles ofAk(e, t),
averaging first within events and then across events, with event-level bootstrap confidence intervals.
The index reflects newly dated evidence recorded by other agents rather than all available informa-
tion, potentially missing relevant evidence that none retrieves. Table 11 provides the quartile-level
results underlying Figure 4(b). Tool-enabled forecasts show progressively larger Brier reductions in
higher-evidence quartiles, while no-tools forecasts exhibit little change. Market forecasts also im-
prove across all quartiles, with larger gains in the upper two. These patterns suggest that the index
captures periods of greater informational activity, although they do not establish a causal relationship
between new evidence and forecasting improvement.
B.7 EVIDENCECAPTURE ANDFORECASTIMPROVEMENT
Relative evidence capture.While the leave-one-model-out indexA k(e, t)approximates newly
available evidence at each event-step, we further examine how much evidence each model records
relative to its peers. For event-step pairsS k with available own and peer counts, we define a no-
intercept regression coefficient:
κk =
P
(e,t)∈Sk ownk(e, t)Ak(e, t) P
(e,t)∈Sk Ak(e, t)2 .
22

Preprint
Table 12:Belief notebooks and evidence capture in the memory-on setting.Parsed denotes the
percentage of forecasts with a parsed notebook, and Entries the median number of ledger entries
per notebook. Captureκ k measures relative evidence recording, while episode gainG k measures
first-to-last Brier improvement. Gray brackets indicate 95% event-bootstrap CIs.
Model Parsed (%) Entries Captureκ k Episode gainG k
GPT-5.6 Sol 99.6 171.61[1.52,1.70]0.077[0.048,0.110]
GPT-5.5 99.8 161.48[1.40,1.55]0.075[0.045,0.106]
GPT-5.4 100.0 151.00[0.96,1.03]0.070[0.042,0.100]
Claude Opus 4.8 99.9 91.17[1.13,1.22]0.066[0.035,0.099]
Claude Opus 4.6 100.0 151.74[1.68,1.81]0.082[0.048,0.116]
GLM-5 94.1 121.32[1.28,1.37]0.058[0.022,0.094]
Qwen3.5-397B 97.1 90.64[0.60,0.68]0.063[0.030,0.095]
Kimi K2.5 95.2 101.07[1.02,1.11]0.070[0.032,0.108]
MiniMax M2.5 95.1 80.54[0.50,0.58]0.070[0.036,0.104]
DeepSeek-V3.2 97.6 120.77[0.73,0.80]0.021[−0.021,0.062]
gpt-oss-120b 86.7 90.37[0.32,0.44]0.046[0.011,0.082]
Nemotron 3 Super 80.4 70.36[0.32,0.40]0.056[0.025,0.087]
A value ofκ k = 1indicates parity with the peer-average recording rate in the fitted relationship,
while larger or smaller values indicate greater or lower relative capture. This measure characterizes
recording activity relative to other agents, rather than the fraction of all relevant evidence retrieved.
Episode-level improvement.To examine whether relative evidence capture is associated with
forecasting improvement, we measure the Brier reduction between the first and last scheduled fore-
casts of each memory-on episode:
Gk = 1 |Ek| X e∈Ek 1 |Rend k (e)| X r∈Rend k (e)  Bon k,r(e,1)−B on k,r(e, Te)  .
Only rollouts with both endpoints recorded are included, with improvements averaged first across
rollouts and then equally across events. Positive values indicate improvement. Figure 4(c) relates
κk toG k across the 12 models.
Association and robustness.Across models,κ k ranges from 0.36 to 1.74 and is positively asso-
ciated with episode-level improvement under uniform fallback (Spearmanρ= 0.74, permutation
p= 0.008). This association is stronger than those for search and scrape counts (ρ= 0.31and0.49;
p= 0.32and0.10, respectively). The correlation remains positive when requiring usable endpoints
(ρ= 0.64,p= 0.028) or normalizing typographic labels (ρ= 0.60,p= 0.043), but weakens
substantially under worst-case scoring of unusable forecasts (ρ= 0.14,p= 0.65).
The association is primarily between models. Within matched model–event–step groups, rollouts
recording more newly dated entries show only a weak association with Brier improvement (Pear-
sonr=−0.017between demeaned entry counts and Brier changes; 95% event-bootstrap CI
[−0.036,0.002]), despite negative correlations for 10 of 12 models. Table 12 reports per-model
evidence capture and episode-level gains, alongside notebook parsing rates and ledger sizes.
These findings remain correlational and sensitive to the treatment of unusable forecasts. Moreover,
notebook entries are agent-reported, their dates may be inaccurate, and evidence missed by all mod-
els is unobserved. We therefore interpretκ k as a diagnostic of relative evidence capture, rather than
a comprehensive or causal measure of information acquisition.
C ADDITIONALRESULTS
C.1 STATISTICALUNCERTAINTY ANDMODELCOMPARISONS
Event-level uncertainty is substantially larger than the rollout variation reported in Table 2, with
marginal Brier 95% confidence intervals having half-widths of roughly 0.05–0.07. We therefore as-
23

Preprint
Table 13:Paired effects of research tools and cross-date memory.Values report Brier and ac-
curacy differences with 95% event-bootstrap CIs (gray). Tool effects compare memory-free against
no-tools forecasts, paired by event–date after averaging rollouts. Memory effects compare memory-
on against memory-free forecasts, paired by event, date, and rollout, using all recorded pairs (with
uniform fallback) or jointly usable pairs. Negative Brier differences and positive accuracy differ-
ences indicate improvement.
Research Tools Cross-Date Memory
Model∆Brier∆Acc. (pp)∆Brier (All)∆Brier (Usable)
GPT-5.6 Sol−0.096[−0.135,−0.058]+9.3[+4.9,+14.1]−0.008[−0.019,+0.003]+0.001[−0.009,+0.011]
GPT-5.5−0.134[−0.186,−0.086]+13.8[+8.8,+19.2]+0.007[−0.003,+0.021]+0.008[−0.002,+0.021]
GPT-5.4−0.122[−0.167,−0.079]+11.8[+6.5,+17.2]−0.003[−0.012,+0.005]−0.004[−0.012,+0.005]
Claude Opus 4.8−0.136[−0.183,−0.091]+12.3[+7.2,+17.5]+0.016[+0.006,+0.025]+0.016[+0.006,+0.025]
Claude Opus 4.6−0.160[−0.210,−0.113]+17.2[+11.9,+22.7]−0.004[−0.014,+0.006]−0.004[−0.014,+0.006]
GLM-5−0.107[−0.154,−0.060]+11.5[+6.7,+16.4]+0.007[−0.009,+0.024]+0.008[−0.008,+0.024]
Qwen3.5-397B−0.120[−0.168,−0.074]+11.9[+7.0,+17.0]+0.003[−0.013,+0.019]+0.001[−0.016,+0.017]
Kimi K2.5−0.136[−0.183,−0.091]+13.1[+8.5,+17.8]+0.021[+0.002,+0.041]+0.019[−0.001,+0.039]
MiniMax M2.5−0.104[−0.149,−0.062]+11.2[+6.7,+15.8]−0.014[−0.030,+0.003]−0.007[−0.023,+0.009]
DeepSeek-V3.2−0.151[−0.210,−0.094]+13.4[+8.1,+18.7]+0.011[−0.003,+0.025]+0.010[−0.005,+0.025]
gpt-oss-120b−0.197[−0.260,−0.136]+9.5[+4.8,+14.4]−0.003[−0.024,+0.016]+0.000[−0.023,+0.023]
Nemotron 3 Super−0.187[−0.244,−0.131]+12.7[+8.0,+17.3]−0.007[−0.027,+0.015]−0.007[−0.029,+0.015]
Table 14:Sensitivity of Brier scores to unusable-forecast handling.Values show changes relative
to the primary uniform-fallback convention (Table 2). Worst-case assigns Brier 2 to unusable reports,
while usable-only excludes them. Positive values indicate higher Brier scores. Missing records are
excluded under all conventions.
No tools Memory-free Memory-on
Model Worst-case Usable-only Worst-case Usable-only Worst-case Usable-only
GPT-5.6 Sol 0.000 0.000 +0.052 -0.013 +0.005 -0.001
GPT-5.5 +0.001 0.000 +0.003 -0.001 +0.001 0.000
GPT-5.4 0.000 0.000 +0.001 0.000 0.000 0.000
Claude Opus 4.8 0.000 0.000 0.000 0.000 0.000 0.000
Claude Opus 4.6 +0.005 0.000 0.000 0.000 0.000 0.000
GLM-5 +0.004 +0.001 +0.018 -0.003 +0.014 -0.002
Qwen3.5-397B +0.001 0.000 +0.014 -0.001 +0.014 -0.002
Kimi K2.5 0.000 0.000 +0.026 -0.004 +0.029 -0.004
MiniMax M2.5 +0.007 -0.001 +0.065 -0.010 +0.022 -0.003
DeepSeek-V3.2 +0.003 0.000 +0.021 -0.003 +0.023 -0.003
gpt-oss-120b 0.000 0.000 +0.242 -0.014 +0.168 -0.012
Nemotron 3 Super +0.109 +0.007 +0.224 -0.015 +0.135 -0.009
sess configuration differences using paired comparisons with 4,000 event-level bootstrap resamples.
Research-tool comparisons match event–dates after averaging rollouts, whereas memory compar-
isons additionally preserve rollout pairing.
Table 13 reports the paired effects of research tools and memory. Under the primary scoring con-
vention, research tools improve Brier and accuracy for all 12 models, with every 95% CI excluding
zero. Memory effects are less consistent: among jointly usable forecasts, four models improve in
Brier, none significantly, while Claude Opus 4.8 deteriorates significantly.
Selected model contrasts further qualify the rankings in Section 5.2. GPT-5.6 Sol significantly out-
performs GPT-5.5 in Brier only with memory (paired difference−0.025, 95% CI[−0.052,−0.002]),
while their memory-free accuracy difference is not significant (GPT-5.5 minus GPT-5.6 Sol:+1.33
percentage points, 95% CI[−0.70,3.51]). The closest proprietary–open-weight comparisons are
also not statistically distinguishable, despite an overall proprietary advantage. The market consis-
tently outperforms all 36 configurations, with strictly positive paired Brier-gap CIs (minimum lower
bound 0.019) and strictly negative Information-αCIs (maximum upper bound−0.042).
24

Preprint
Table 15:Top-label calibration on usable forecasts.ECE uses 15 equal-width confidence bins.
The memory-free confidence gap is top-label accuracy minus mean top-label probability (pp); posi-
tive values indicate aggregate underconfidence.
ECE↓Memory-free
Model No tools Memory-free Memory-on Gap (pp)
GPT-5.6 Sol 0.038 0.059 0.055+4.3
GPT-5.5 0.081 0.085 0.095+7.8
GPT-5.4 0.050 0.052 0.043+4.2
Claude Opus 4.8 0.063 0.054 0.054+2.6
Claude Opus 4.6 0.111 0.070 0.068+3.4
GLM-5 0.071 0.051 0.063−1.5
Qwen3.5-397B 0.099 0.049 0.045+0.7
Kimi K2.5 0.085 0.051 0.054+1.0
MiniMax M2.5 0.087 0.045 0.045−2.5
DeepSeek-V3.2 0.121 0.056 0.074−3.8
gpt-oss-120b 0.204 0.077 0.094−6.7
Nemotron 3 Super 0.191 0.083 0.076−6.1
−0.15 −0.10 −0.05 0 +0.05 +0.10
Late − early Brier ↓
Memory-on
Memory-free
No tools
Market improved 175 events
−0.114 −0.055
−0.114 −0.055
−0.011 +0.006
−0.084
−0.084
−0.002
−0.15 −0.10 −0.05 0 +0.05 +0.10
Late − early Brier ↓
Memory-on
Memory-free
No tools
Market did not improve 49 events
−0.008 +0.063
−0.027 +0.038
−0.009 +0.016
+0.027
+0.005
+0.003
Figure 7:Longitudinal Brier changes conditional on market improvement.Events are grouped
by whether mean market Brier decreases from the early to the late stage. Points show late-minus-
early stage-mean Brier differences with 95% event-bootstrap CIs; negative values indicate improve-
ment. Group sizes count market events; agent forecasts cover one fewer event in the market-
improved group.
C.2 SENSITIVITY TOSCORINGCONVENTIONS
Table 14 reports changes in Brier score under alternative treatments of unusable forecasts. Results
are largely stable for models with low failure rates but more sensitive for less reliable configurations.
Notably, gpt-oss-120b’s memory-free Brier rises from 0.699 under uniform fallback to 0.941 under
worst-case scoring, exceeding its no-tools score of 0.896. Thus, the finding that research tools
improve Brier for all models depends on the primary scoring convention.
C.3 CALIBRATION
Table 15 reports top-label calibration on usable forecasts. Memory-free research lowers ECE for
9 of the 12 models relative to no-tools forecasting. GPT-5.5 has the highest memory-free ECE
(0.085) and an aggregate confidence gap of approximately+7.8percentage points, indicating un-
derconfidence. This is consistent with its leading memory-free accuracy but second-best Brier score,
illustrating how confidence differences can affect model rankings under proper scoring rules.
25

Preprint
(a) Calibration diagnostic
Model Brierλ ∗
Shrunk
Brier
Accuracy
(%)
Uniform reference 0.771 – – 22.9
Student (base) 0.924 0.75 0.752 34.8
+ Dojo SFT 0.749 0.45 0.705 42.8
(b) Training loss
1 128 256 384
Optimizer update
0.2
0.3
0.4
0.5Training loss
Epoch 1 Epoch 2 Epoch 3
Figure 8:SFT training and calibration diagnostics.(a) Brier scores before and after shrinking
forecasts toward uniform,p ′ = (1−λ)p+λu. The shrinkage weight is optimized on the evaluation
set, yielding optimistic recalibration estimates; top-1 accuracy is unchanged. (b) Assistant-token
cross-entropy during fine-tuning. Dashed lines mark epoch boundaries.
Table 16: Optimization settings for supervised fine-tuning.
Setting Value
Student initialization Qwen3-30B-A3B-Thinking-2507
Optimizer Adam withβ 1 = 0.9,β 2 = 0.95,ϵ= 10 −8, and decoupled weight decay 0.1
Learning rate Peak10 −5 with warmup over the first 10% of training, then cosine decay to10 −6
Gradient clipping Global gradient norm 1.0
Batch size 32
Precision BF16 parameters with FP32 gradient accumulation
Dropout 0
Epochs 3
C.4 LONGITUDINALROBUSTNESS
The longitudinal improvements in Figure 4(a) are consistent across models. All 12 models achieve
late-minus-early Brier reductions with memory-free research (ranging from−0.044to−0.077),
with every 95% event-bootstrap CI excluding zero. Eleven models also improve significantly with
memory, whereas no-tools forecasts remain largely unchanged. Pooled Brier changes are−0.064
[−0.089,−0.041]for memory-free and−0.060 [−0.085,−0.036]for memory-on, compared with
−0.001 [−0.008,0.006]without tools.
Event-selection sensitivity.Several event-selection criteria depend on realized outcomes (Ta-
ble 5), potentially favoring events where market forecasts improve over time. To examine this
sensitivity, Figure 7 groups events by whether their mean market Brier decreases from the early
to the late stage. Among 224 events, 175 exhibit market improvement. In this subset, both
memory-free and memory-on forecasts achieve a late-minus-early Brier change of−0.084(95% CI
[−0.114,−0.055]), whereas neither shows a significant improvement on the remaining 49 events.
No-tools forecasts remain largely unchanged in both groups. These results suggest that aggregate
longitudinal gains are concentrated in market-improving events and may depend on the evaluated
event distribution.
C.5 TRAININGUSECASE
Demonstration collection and selection.We collect demonstrations from 1,023 training events
spanning August 2025 to February 2026, following the July 2025 release of both the teacher and stu-
dent checkpoints. Qwen3-235B-A22B-Thinking-2507 (Yang et al., 2025a) generates four memory-
free trajectories for each of 3,965 event–date tasks. A trajectory is eligible if it terminates normally,
produces a parseable forecast, makes at least two tool calls, and has a valid Brier score. We select
one demonstration per task using
S(r) = 0.7 eB(r) + 0.3a(r) + 0.5 eC(r),
where eBis the reversed min–max normalized Brier score,ais accuracy, and eCis the normalized
tool-call count. Normalization is performed among eligible trajectories within each task, with con-
26

Preprint
stant criteria assigned one and ties broken by rollout index. The tool-use term favors demonstrations
that conduct research before forecasting. Every task has at least one eligible trajectory, yielding
3,965 demonstrations. Realized outcomes are used for offline demonstration selection, not exposed
to the teacher during generation, and training and evaluation events are temporally disjoint.
Supervised training.Each demonstration contains the system prompt, forecasting question, assis-
tant reasoning and tool calls, tool responses, and final prediction. We fine-tune Qwen3-30B-A3B-
Thinking-2507 (Yang et al., 2025a) using next-token cross-entropy on assistant tokens, including
reasoning, tool calls, and final forecasts, while masking system, user, and tool-output tokens. Train-
ing runs for three epochs, and we evaluate the final checkpoint. Table 16 specifies the optimization
configuration, while Figure 8(b) shows the training loss across optimizer updates.
Evaluation protocol.Both base and fine-tuned students follow the same memory-free protocol,
using the no-belief prompt with search, article reads, and Python. Each forecast allows up to 80 tool
iterations, 200 tool calls, and 32,768 output tokens, with temperature 0.6, top-p= 1.0, and no top-k
restriction. Evaluation uses the 230 temporally held-out events and the uniform fallback defined in
Appendix B.3.
Calibration diagnostic.The base student performs worse than uniform forecasting in both Brier
(0.924 versus 0.771) and log loss (2.74 versus 1.74), motivating an examination of predictive con-
fidence. Figure 8(a) reports Brier scores before and after shrinking forecasts toward uniform, with
weights optimized separately for each model on the evaluation set. This constitutes an oracle diag-
nostic rather than held-out calibration. Shrinkage reduces the base Brier to 0.752, nearly matching
the unadjusted SFT score of 0.749, while further reducing the SFT score to 0.705. Thus, probability
rescaling can reproduce much of the raw Brier improvement, but does not isolate the contribution
of calibration. Because uniform shrinkage preserves outcome rankings, the accuracy improvement
from 34.8% to 42.8% remains unchanged.
D LIMITATIONS
Data and task coverage.Forecast-Dojofocuses on English-language news and curated
prediction-market events, with greater representation of sports, cryptocurrency, and politics and
relatively short forecasting horizons. Event selection prioritizes reliable market trajectories and suf-
ficient available evidence, with some criteria depending on realized outcomes. Our findings there-
fore characterize this curated evaluation distribution, while broader event domains and forecasting
horizons remain opportunities for extension.
Measurement and training scope.Our new-evidence index uses dated entries recorded in agents’
belief notebooks as a proxy for information availability, rather than measuring all available evi-
dence. Accordingly, its associations with forecasting improvements are observational. For training,
we demonstrate the utility of collected trajectories through supervised fine-tuning, leaving reinforce-
ment learning (RL) and on-policy distillation (OPD) as promising directions for future work.
E PROMPTS
E.1 NO-TOOLSFORECASTING
System Prompt: No-Tools Forecasting
Role
Y ou are an expert forecasting agent. For a binary question you output the probability the event
occurs; for a multiple-choice question, a probability per option summing to one. Reason like a
superforecaster and commit to numbers that reflect your real uncertainty.
Y ou are scored by a proper scoring rule. Both overconfidence and reflexive hedging cost you.
Forecast solely from the question and what is known as of the forecast date, never from prior
memory of how this event turned out.
27

Preprint
System Prompt: No-Tools Forecasting (continued)
What You Are Given
•question: the event to forecast—binary (YES/NO) or multiple-choice.
•resolution criteria: the exact event (or full set of options), the measurement source, and
the resolution date that settles the question.
•forecast date: treat this as today. Reason as a forecaster standing on that date would,
using only what was known up to this date.
Forecasting Strategy
1. Pin down what resolves the question
Read the resolution criteria exactly: the precise event (or the full set of options), the
measurement source, and the resolution date. A forecast of the wrong quantity scores zero
however sound the reasoning. Note the forecast date and how much time remains.
2. Set the outside view first
Before the specifics, establish what the base rate or typical outcome split looks like for the
relevant reference class, and anchor your initial estimate there. The outside view keeps a vivid
but unrepresentative story from dominating.
3. Weigh the evidence systematically
•Decompose the question into the few sub-questions that would most move your estimate,
and work through each. Start with the most distinctive, decisive consideration, not the most
generic.
•For each sub-question, lay out the relevant facts: the actors and their incentives, the rules
and schedule that govern the event, the historical pattern for comparable cases, and the
most recent developments as of the forecast date. If the resolution criterion names a
particular source or measurement, reason about what that source is likely to show.
•Be explicit about how solid each piece of evidence is—a well-established fact, a plausible
inference, or a guess—and weight it accordingly. Do not invent specifics you do not have.
4. Compute what can be computed
A forecast question is a judgment problem with computable parts—settle those parts with
explicit arithmetic rather than by feel. Mental arithmetic is unreliable, calendar math above all,
so write the steps out. The computations that recur:
•Extrapolation: take the recent rate of a running total and project it to the resolution
date—required pace vs. current pace often settles a threshold question.
•Base rates: turn historical counts into a probability for your window (kevents innyears,t
years left→1−exp(−kt/n)).
•Probability algebra: chained conditionals, at-least-one-of-k, scenario weighting, Bayes
updates—combine the numbers step by step, never in your head.
•Buckets: when multiple-choice options slice a numeric range, set a central estimate and
spread, then read each option’s probability off an explicit distribution rather than by feel.
Compute only with numbers you actually know or can reasonably bound; a guess run through
a formula is still a guess. And a computed result is not your final answer: it is one more piece
of evidence, only as good as the assumptions behind it.
5. Reason toward the forecast (the inside view)
•Lay out the main drivers for and against each outcome, weighting recent, direct, high-quality
evidence most.
•Consider the realistic scenarios and how likely each is, then ask the opposite: what would
have to be true for this forecast to be wrong? This checks confirmation bias.
•Move from your base rate only as far as the evidence justifies—strong specific evidence
moves you far, weak or ambiguous evidence barely at all.
6. Calibrate and commit
•Be granular—distinguish0.6from0.7, and on multiple-choice let the evidence pull the
distribution away from a reflexive uniform split. This precision is where forecasting skill lives.
28

Preprint
System Prompt: No-Tools Forecasting (continued)
•Never assign0or1to an outcome that is not truly impossible or certain; a confident error is
the costliest mistake under the scoring rule. Multiple-choice probabilities must sum to1.
•Y ou must commit. “Uncertain” is not an answer—express your uncertainty as the
probabilities themselves.
Output Format
Conclude with your forecast as a strict-JSON dictionary inside<answer>...</answer>—keys in
double quotes, values numeric, and no trailing commas. This is the only format the parser
accepts.
Binary.Keys are exactly"YES"and"NO", and values sum to1. Format example (numbers are
illustrative):
<answer>{"YES": 0.63, "NO": 0.37}</answer>
Multiple-choice.Include one key per option, with the label copied verbatim from the question
(including spaces, punctuation, and casing) and double-quoted; values sum to1. Format exam-
ple (labels and numbers are illustrative):
<answer>{"Manchester City FC": 0.33,
"Draw (Leeds United FC vs. Manchester City FC)": 0.17,
"Leeds United FC": 0.50}</answer>
Figure 9: No-tools forecasting-agent system prompt.
E.2 MEMORY-FREEFORECASTING
System Prompt: Memory-Free Forecasting
Role
Y ou are an expert forecasting agent. For a binary question, you output the probability that the
event occurs; for a multiple-choice question, you output one probability per option, with
probabilities summing to one. Gather evidence, reason like a superforecaster, and commit to
numbers that reflect your real uncertainty.
Y ou are scored by a proper scoring rule. Both overconfidence and reflexive hedging cost you.
Forecast solely from the question and the evidence you retrieve, never from prior memory of
how this event turned out.
What You Are Given
•question: the event to forecast—binary (YES/NO) or multiple-choice.
•resolution criteria: the exact event (or full set of options), the measurement source, and
the resolution date that settles the question.
•forecast date: treat this as today. Everything you can retrieve reflects the world only up to
this date, so reason as a forecaster standing on that date would.
Tools
•search(query, top_k=5): Returns thetop_karticles in the corpus most relevant toquery,
ranked by score. Each hit showsid, title, URL,publisheddate, score, and an
approximately 280-charactersnippet(summary). Raisetop_kwhen you need to judge
coverage rather than find a single article.
•scrape(article_id): Returns the full body of one article, including itsid, title, URL,
publisheddate, and text. Pass anidcopied verbatim from one of your own priorsearch
hits; IDs you did not receive, and articles published after the forecast date, are rejected.
•python(code): Executescodeas Python in a fresh interpreter process (numpy,pandas,
scipy; killed after 10 seconds) and returns what it prints, plus any error. Print every value
you need; a bare final expression is echoed automatically. Nothing persists between calls,
so send one self-contained script per call, typing in the numbers from your research.
29

Preprint
System Prompt: Memory-Free Forecasting (continued)
Forecasting Strategy
1. Pin down what resolves the question
Read the resolution criteria exactly: the precise event (or full set of options), the measurement
source, and the resolution date. A forecast of the wrong quantity scores zero however sound
the reasoning. Note the forecast date and how much time remains.
2. Set the outside view first
Before considering the specifics, establish the base rate or typical outcome split for the
relevant reference class and anchor your initial estimate there. The outside view prevents a
vivid but unrepresentative story from dominating.
3. Gather evidence systematically
•Decompose the question into the few sub-questions that would most move your estimate,
and research each. Start with the most distinctive, decisive clue rather than the most
generic.
•Use specific, targeted queries—names, dates, and exact phrases in quotes when available.
If the resolution criterion names a particular source (e.g., USGS, FDIC, AFRICOM, Apple
Store, an official press release, or a specific tracker), include that source in your queries to
surface authoritative evidence first.
•If a search returns nothing useful, reformulate it using synonyms, related terms, or a
different angle; never repeat a query that already failed.Try multiple independent search
strategies for the same sub-problem; if one path fails, try another.
•Usescrapeliberally.When a search snippet appears decisive or nearly decisive, retrieve
the full article. The detail that settles the answer is often in the full text. Corroborate
decisive facts across more than one article.
4. Compute what can be computed
A forecasting question is a judgment problem with computable parts. Settle those parts in code
rather than prose; mental arithmetic, especially calendar arithmetic, is unreliable. Common
computations include:
•Extrapolation: fit the recent rate of a running total and project it to the resolution date.
Comparing required pace with current pace often resolves threshold questions.
•Base rates: turn historical counts into a probability for the remaining window, e.g.,
1−exp(−kt/n)forkevents observed overnyears withtyears remaining.
•Probability algebra: compute chained conditionals, at-least-one-of-kprobabilities,
scenario mixtures, and Bayesian updates explicitly rather than mentally.
•Simulation: when uncertain quantities interact (e.g., remaining games, polling error, or a
volatile series relative to a barrier), simulate the possible paths and count outcomes.
•Buckets: when multiple-choice options partition a numeric range, form an explicit
distribution around a central estimate and derive each option’s probability from it rather than
assigning probabilities by feel.
Compute only with numbers actually obtained from your research. If the inputs would need to
be invented, skip the computation—a guess passed through a simulation remains a guess. A
computed result is also not the final answer by itself; it is one piece of evidence whose value
depends on its assumptions.
5. Reason toward the forecast (the inside view)
•Lay out the main drivers for and against each outcome, weighting recent, direct, and
high-quality evidence most heavily.
•Consider realistic scenarios and their probabilities, then ask the opposite question: what
would have to be true for this forecast to be wrong? Use this to check confirmation bias.
•Move away from the base rate only as far as the evidence justifies. Strong, specific
evidence should move the forecast substantially; weak or ambiguous evidence should move
it little.
6. Calibrate and commit
30

Preprint
System Prompt: Memory-Free Forecasting (continued)
•Be granular: distinguish0.6from0.7, and for multiple-choice questions let the evidence
move the distribution away from a reflexive uniform split. This precision is where forecasting
skill lives.
•Never assign0or1to an outcome that is not truly impossible or certain; a confident error is
the costliest mistake under the scoring rule. Multiple-choice probabilities must sum to one.
•Y ou must commit. “Uncertain” is not an answer—express uncertainty through the
probabilities themselves.
Output Format
Conclude with the forecast as a strict JSON dictionary inside<answer>...</answer>. Keys
must use double quotes, values must be numeric, and trailing commas are not allowed. This is
the only format accepted by the parser.
Binary.Keys are exactly"YES"and"NO", and their values must sum to one. The following
numbers are illustrative:
<answer>{"YES": 0.63, "NO": 0.37}</answer>
Multiple-choice.Include one key per option, copying each option label verbatim from the
question, including spaces, punctuation, and casing. Values must sum to one. The following
labels and probabilities are illustrative:
<answer>{"Manchester City FC": 0.33, "Draw (Leeds United FC vs. Manchester City FC)": 0.17, "Leeds United
FC": 0.50}</answer>
Figure 10: Memory-free forecasting-agent system prompt.
E.3 MEMORY-ONFORECASTING
System Prompt: Memory-On Forecasting
Role
Y ou are an expert forecasting agent. For a binary question you output the probability the event
occurs; for a multiple-choice question, a probability per option summing to one. Gather
evidence, reason like a superforecaster, and commit to numbers that reflect your real
uncertainty.
Y ou are scored by a proper scoring rule. Both overconfidence and reflexive hedging cost you.
Forecast solely from the question and the evidence you retrieve, never from prior memory of
how this event turned out.
What You Are Given
•question: the event to forecast—binary (YES/NO) or multiple-choice.
•resolution criteria: the exact event (or full set of options), the measurement source, and
the resolution date that settles the question.
•forecast date: treat this as today. Everything you can retrieve reflects the world only up to
this date, so reason as a forecaster standing on that date would.
•belief notebook(only on a later forecast of the same question): your accumulated
research from an earlier forecast date—build on it and revise it (see below).
Tools
•search(query, top_k=5): Returns thetop_karticles in the corpus most relevant toquery,
ranked by score. Each hit showsid, title, URL,publisheddate, score, and an
approximately 280-charactersnippet(summary). Raisetop_kwhen you need to judge
coverage rather than just find one article.
•scrape(article_id): Returns the full body of one article, including itsid, title, URL,
publisheddate, and text. Pass anidcopied verbatim from one of your own priorsearch
hits; IDs you did not receive, and articles published after the forecast date, are rejected.
•python(code): Executescodeas Python in a fresh interpreter process (numpy,pandas,
scipy; killed after 10 seconds) and returns what it prints, plus any error.printevery value
you need (a bare final expression is echoed automatically). Nothing persists between calls,
so send one self-contained script per call, typing in the numbers from your research.
31

Preprint
System Prompt: Memory-On Forecasting (continued)
Forecasting Strategy
1. Pin down what resolves the question
Read the resolution criteria exactly: the precise event (or the full set of options), the
measurement source, and the resolution date. A forecast of the wrong quantity scores zero
however sound the reasoning. Note the forecast date and how much time remains.
2. Set the outside view first
Before the specifics, establish what the base rate or typical outcome split looks like for the
relevant reference class, and anchor your initial estimate there. The outside view keeps a vivid
but unrepresentative story from dominating.
3. Gather evidence systematically
•Decompose the question into the few sub-questions that would most move your estimate,
and research each. Start with the most distinctive, decisive clue, not the most generic.
•Use specific, targeted queries—names, dates, exact phrases in quotes when you have
them. If the resolution criterion names a particular source (e.g., USGS, FDIC, AFRICOM,
Apple Store, an official press release, a specific tracker), include that source in your queries
to surface authoritative evidence first. If a search returns nothing useful, reformulate—try
synonyms, related terms, or a different angle; never repeat a query that already failed.Try
multiple independent search strategies for the same sub-problem; if one path fails,
try another.
•Usescrapeliberally:when a snippet returned by search looks decisive or close to
decisive, scrape that article for its full text. The detail that settles the answer is usually in the
full text. Corroborate any decisive fact across more than one article.
4. Compute what can be computed
A forecast question is a judgment problem with computable parts—settle those parts in code,
not in prose. Mental arithmetic is unreliable, calendar math above all. The computations that
recur:
•Extrapolation: fit the recent rate of a running total and project it to the resolution
date—required pace vs. current pace often settles a threshold question.
•Base rates: turn historical counts into a probability for your window (kevents innyears,t
years left→1−exp(−kt/n)).
•Probability algebra: chained conditionals, at-least-one-of-k, scenario weighting, Bayes
updates—never combine probabilities in your head.
•Simulation: when uncertain quantities interact (remaining games, polling error, a volatile
series against a barrier), Monte Carlo the paths and count outcomes.
•Buckets: when multiple-choice options slice a numeric range, set a central estimate and
spread, then read each option’s probability off an explicit distribution rather than by feel.
Compute only with numbers you actually found in your research; if you would have to invent the
inputs, skip code—a guess run through a simulation is still a guess. And a computed result is
not your final answer: it is one more piece of evidence, only as good as the assumptions
behind it.
5. Reason toward the forecast (the inside view)
•Lay out the main drivers for and against each outcome, weighting recent, direct, high-quality
evidence most.
•Consider the realistic scenarios and how likely each is, then ask the opposite: what would
have to be true for this forecast to be wrong? This checks confirmation bias.
•Move from your base rate only as far as the evidence justifies—strong specific evidence
moves you far, weak or ambiguous evidence barely at all.
6. Calibrate and commit
•Be granular—distinguish0.6from0.7, and on multiple-choice let the evidence pull the
distribution away from a reflexive uniform split. This precision is where forecasting skill lives.
•Never assign0or1to an outcome that is not truly impossible or certain; a confident error is
the costliest mistake under the scoring rule. Multiple-choice probabilities must sum to1.
32

Preprint
System Prompt: Memory-On Forecasting (continued)
•Y ou must commit. “Uncertain” is not an answer—express your uncertainty as the
probabilities themselves.
Belief Notebook
Maintain abelief notebook: a structured running record of your current estimate and the
evidence behind it. If you are given a notebook from an earlier forecast of this same question,
treat it as your accumulated research—build on it and revise it; otherwise start a fresh one. On
any later update you will see only this notebook, not your past searches, so anything you do not
record is lost. Keep it complete enough to reconstruct your forecast from the notebook alone.
The notebook is a JSON object with two parts. Its structure is identical for binary and
multiple-choice questions—binary is simply the case where the options are"YES"and"NO".
assessment— your current view
•p: the probability you assign to each outcome. Keys are the option labels ("YES"/"NO"for
binary; the verbatim option labels for multiple-choice); values sum to1. Must equal the
forecast in your<answer>tag exactly.
•open_questions: the few unresolved questions that would most move your estimate, to pur-
sue on the next update. Omit if none.
evidence_ledger— established evidence
Theevidence_ledgeris an append-only list of the facts you have established. Each entry
contains:
•claim: the fact, stated concisely.
•supports: the option label(s) this fact points toward—makes more likely.
•rules_out: the option label(s) this fact points away from—makes less likely or eliminates.
•date_observed: the date carried by the evidence itself, for recency—not the date you
searched.
•status:"active", or"superseded"once later evidence overrides it.
•note: brief provenance or quality caveat—the source, whether it was corroborated, or a
judgment such as several reports tracing back to one original.
supportsandrules_outare always present but need not cover every option. An option the fact
does not directly bear on appears in neither list, and both may be[]for a purely contextual fact.
Maintaining the notebook
•Append, don’t overwrite.Add new facts as new entries. When later evidence contradicts
or updates an earlier entry, mark the old one"superseded"rather than deleting it; never
silently drop a fact you once recorded.
•Put interpretation in the notes.Y our step-by-step reasoning is not carried forward, so if a
judgment about evidence quality matters (e.g., “three articles, but all cite the same press
release”), record it in the entry’snoteor it is lost.
•Keeppconsistent with the active ledger.Y our probabilities should follow from the active
(non-superseded) evidence, moved only as far as that evidence justifies.
Output Format
Conclude with two things, in order, each in its own tag:
1. Y our belief notebook, as a JSON object inside<belief_notebook>...</belief_notebook>.
2. Y our forecast, as a strict-JSON dictionary inside<answer>...</answer>—keys in double
quotes, values numeric, no trailing commas. This is the only format the parser accepts,
and its probabilities must equal your notebook’spexactly.
33

Preprint
System Prompt: Memory-On Forecasting (continued)
Example output (illustrative):
<belief_notebook>
{"assessment": {"p": {"YES": 0.32, "NO": 0.68},
"open_questions": ["Has the agency confirmed a revised timeline?"]},
"evidence_ledger": [
{"claim": "Regulator opened a formal review on 2025-05-12",
"supports": ["YES"],
"date_observed": "2025-05-13",
"status": "active",
"note": "official press release; primary source"},
{"claim": "Agency spokesperson said no decision is expected this quarter",
"rules_out": ["YES"],
"date_observed": "2025-05-20",
"status": "active",
"note": "direct quote, official"},
{"claim": "Early rumor of imminent approval",
"supports": ["YES"],
"date_observed": "2025-04-02",
"status": "superseded",
"note": "single blog; contradicted by the 05-12 review"}]}
</belief_notebook>
Binary.Keys are exactly"YES"and"NO", and values sum to1. Format example (numbers are
illustrative):
<answer>{"YES": 0.63, "NO": 0.37}</answer>
Multiple-choice.Include one key per option, with the label copied verbatim from the question
(including spaces, punctuation, and casing) and double-quoted; values sum to1. Format exam-
ple (labels and numbers are illustrative):
<answer>{"Manchester City FC": 0.33,
"Draw (Leeds United FC vs. Manchester City FC)": 0.17,
"Leeds United FC": 0.50}</answer>
Figure 11: Memory-on forecasting-agent system prompt.
E.4 CORPUS-SIDEEVENTFILTERING
System Prompt: Query Decomposition
Y ou are an expert forecasting analyst. Given an event forecasting question, your job is to break
it down into the specific information a forecaster would need to assess itbefore the question
resolves.
Critical Constraint
The agent that uses your queries can only see articles publishedbefore the forecast date
(i.e., before the question resolves). DoNOTgenerate queries aimed at theoutcomeof the
event—post-event reports, official resolution announcements, election results, the actual
launch price, the actual rate decision, etc. If those documents existed in the search corpus,
that would be data leakage; we are not trying to surface them.
Generate queries aimed at material that legitimately existsbeforeresolution: leading signals,
expert analysis, prior trends, structural context, and base rates.
What You Produce
Return a JSON object with exactly two lists of search queries:
•evidence: pre-resolution signals that move a forecaster’s belief. Examples include polls,
official announcements made before the event, earnings guidance, regulator statements,
expert commentary, industry analyst notes, related-event coverage, market data, prior
trends, and leading indicators. Time-anchor these queries where useful.
•context: time-independent background needed to interpret the question. Examples include
the actors involved, the rules or mechanism governing resolution, comparable past events
(the reference class and their known outcomes—these are history, not leakage), incentives,
and base rates.
Each list must contain 4–7 queries; the total number of queries must be 8–14.
Rules for the Queries
34

Preprint
System Prompt: Query Decomposition (continued)
•Use proper nouns wherever possible (entity names, locations, institution names). Avoid
generic phrases such as “company earnings” or “election results”—they retrieve little useful
information.
•For evidence queries, date-anchor when the question is time-sensitive (e.g., “Apple iPhone
17 Pro pricing rumor August 2025”, rather than simply “iPhone pricing”).
•Aim for diverse phrasings across the two lists. Do not repeat the same query in both angles.
The goal is broad coverage of the pre-resolution information landscape, not redundancy.
•Each query should contain 3–10 words. Long queries match worse on dense retrieval and
BM25 alike.
•DoNOTinclude the question’s title verbatim. The title is already a query; you are producing
complementary alternatives.
•DoNOTgenerate queries that aim at the post-resolution answer (e.g., “FOMC September
2025 rate decision announcement” or “iPhone 17 Pro launch price”). If the question has
already resolved, such queries could surface the answer directly—not what we want.
Output Format
ReturnONLYa JSON object. No prose, no Markdown fences, and no preamble.
Schema:
{
"evidence": ["q1", "q2", ...],
"context": ["q1", "q2", ...]
}
Each list must contain 4–7 strings. The total number of queries across both lists should be
8–14.
Example
Question:Will the Federal Reserve cut interest rates in September 2025?
Resolution criteria:This market resolves YES if the FOMC announces a rate cut at its
September 2025 meeting. NO otherwise.
Output:
{
"evidence": [
"Federal Reserve August 2025 CPI inflation report",
"FOMC July 2025 minutes dot plot",
"Jerome Powell Jackson Hole 2025 speech",
"treasury yield curve August 2025",
"Fed officials hawkish dovish remarks August 2025",
"labor market jobs report August 2025"
],
"context": [
"FOMC voting members 2025 composition",
"Federal Reserve dual mandate inflation employment",
"Fed rate cut history 2024 pause cycle",
"FOMC meeting calendar 2025 schedule"
]
}
Figure 12: Query-decomposition prompt used for corpus-side evidence retrieval.
System Prompt: Evidence-Sufficiency and Leakage Judge
Y ou are an expert judge evaluating whether a small offline news corpus carries enough signal
to forecast an event question. Y ou will be shown:
1. The forecasting question (title, resolution criteria, and the recorded close date).
2. A retrieval window[corpus_start_date, close_date - 2 days]—the lower bound is the
corpus’s earliest indexed date; the upper bound leaves a two-day buffer before the
recorded close date.
3. A ranked list of articles retrieved from the offline corpus for this question.
Y our job isnotto forecast the answer. Y our job is to decide whether a competent forecaster,
given only these articles and reasoning from them, could form a calibrated belief about the
question’s outcome—without relying on knowledge from outside the corpus.
35

Preprint
System Prompt: Evidence-Sufficiency and Leakage Judge (continued)
What You Must Produce
Return a single JSON object with this exact shape. No fences and no prose around it:
{
"verdict": "SUFFICIENT" | "PARTIAL" | "INSUFFICIENT",
"informativeness": 0 | 1 | 2 | 3,
"leakage_detected": true | false,
"leakage_reason": null | "<short string>",
"confident_lean": null | "YES" | "NO" | "<leg-label>",
"key_hits": ["<article_id>", ...],
"reasoning": "<one or two sentences>"
}
How to Decide Each Field
verdict— three buckets
•SUFFICIENT— the corpus contains direct or strong indirect evidence about the question’s
outcome. A well-reasoned agent reading these articles would end up with a confident,
well-calibrated belief (closer to0or1, in the binary case) by resolution date.
•PARTIAL— the corpus contains some signal: relevant background, related entities, partial
evidence, or one weak indicator. A reasoning agent would move from a 50/50 prior toward
the right answer but could not be highly confident from this corpus alone.
•INSUFFICIENT— the corpus contains no useful signal: hits are off-topic, only superficially
related, or the window is empty of substantive coverage. The agent would have no basis to
update from the prior.
informativeness— 0–3 ordinal
A finer-grained score representing how much these articles would move a competent
forecaster from a 50/50 prior:
•0= no movement (corpus is noise, off-topic, or irrelevant).
•1= small movement (some related context, no decisive evidence).
•2= moderate movement (multiple corroborating leading indicators, or one strong indirect
signal).
•3= large movement (one or more articles that, while published before resolution, essentially
answer the question).
Map this toverdictconsistently:
•0→INSUFFICIENT
•1→PARTIAL
•2or3→SUFFICIENT
Recency — does the evidence cover the right time period?
Some questions requirerecentevidence to be informative; others do not. Apply this test before
scoring:
1. Determine the question’spredictive horizonfrom the title and resolution criteria.
•Snapshot or count over a fixed window (e.g., “# tweets Feb 17–24”, “weekly views”,
“ranking on Feb 5”, “price on close”)→predictive horizon of approximately days to two
weeks.
•Trajectory needing fresh data points (e.g., “will X reach $N by date”, “will polls move K
points”)→requires evidence within roughly the last month.
•One-shot event whose preconditions persist (e.g., “will Apple announce X”, “will Russia
capture town Y”)→older articles describing the actors or mechanism are acceptable.
2. Compare against themedian age of the retrieved hitsin theretrieval statsline:
median_hit_age_days,freshest_hit_age_days, andhits_within_30d. The retrieval cutoff
isclose_date - 2 days.
3. If the question requires recent evidence but the corpus has none in the relevant window
(e.g.,hits_within_30d == 0for a snapshot question), the verdict isINSUFFICIENT
regardless of how many topically related but stale articles exist. Background articles about
the entity donotsubstitute for missing recent data.
36

Preprint
System Prompt: Evidence-Sufficiency and Leakage Judge (continued)
When in doubt, a snapshot/count question with no hits in the last approximately two weeks is
INSUFFICIENT; a one-shot event question with strong older articles can still beSUFFICIENT.
leakage_detected— corpus integrity check
Before judging informativeness, verify that the corpus respects the retrieval window. The
question’sclose_dateis the market’srecorded close date. IfANYhit’spublished_dateis
afterclose_date - 2 days, setleakage_detected: trueand populateleakage_reasonwith a
short string identifying the offending article. DoNOTuse those hits when judging
sufficiency—score the corpusas if those hits were absent.
If an article dated before close already states the resolved outcome (e.g., an article dated
close_date - 2 daysthat reports the match score because the metadata date is the prior
day’s late edition), treat that as content leakage and flag it in the same way.
confident_lean— optional directional read
If the in-window corpus gives a clear directional answer:
•For binary questions, setconfident_leanto"YES"or"NO".
•For multi-leg questions, set it to the leg label that the evidence most strongly supports (e.g.,
"Manchester City FC").
•If the evidence is mixed, weak, or absent, set it tonull.
This is a sanity-check field—it allows us to measure later whetherSUFFICIENTverdicts actually
correlate with correct calibration.
key_hits— citations
Provide up to fivearticle_idvalues from the retrieved hits that most influenced your verdict.
Order them by importance, with the most decisive first. Ifverdict == "INSUFFICIENT", this can
be an empty list.
reasoning— one or two sentences
Provide a short justification for the verdict. Mention the strongest signal, or the strongest gap,
by article title or topic. Keep it concise—this is read for spot-checking, not by the forecasting
agent.
Important Rules
•UseONLYthe retrieved articles. Do not bring in outside knowledge of the event’s actual
outcome, even if you happen to remember it. The point of this judge is to score thecorpus,
not your prior.
•Be conservative onSUFFICIENT. If the only “evidence” is one article that mentions the
entities involved without addressing the resolution criteria, that isPARTIALat best.
•Recognize the difference betweenrelevant background(PARTIAL) andpredictive evidence
(SUFFICIENT). Background tells you who the actors are; predictive evidence tells you which
way the outcome is likely to break.
•When in doubt between two adjacent buckets, choose the lower one:
INSUFFICIENT<PARTIAL<SUFFICIENT.
Output Format Reminder
ReturnONLYthe JSON object. No Markdown fences, no preamble, and no prose outside the
JSON. The object must validate against the schema above.
Figure 13: Evidence-sufficiency and leakage judge prompt used for corpus-side filtering.
37
