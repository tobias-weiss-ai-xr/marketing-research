---
title: When Should Forecasting Agents Reason? Behavioral Stress Tests for Reliability Routing
url: https://arxiv.org/abs/2609.28475
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Yufeng Wang
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.28475
pages: 9
chars: 29939
fetched_at: '2026-11-08T13:20:54+00:00'
kb_version: 1
---

# When Should Forecasting Agents Reason? Behavioral Stress Tests for Reliability Routing

Preprint.
When Should Forecasting Agents Reason?
Behavioral Stress T ests for Reliability Routing
Louis Wang
Abstract
Forecasting agents increasingly combine language-model reasoning, re-
trieval, ensembling, and calibration, but it remains unclear when each
behavior should be trusted. We study this question on ForecastBench-style
binary forecasting tasks, treating the choice to retrieve, reason, defer to a
market prior, or use a historical analog as an observable agent behavior
rather than a hidden implementation detail. Our central finding is that
mechanism choice is source-dependent: structured analogs dominate for
some data-generating processes, while market/crowd-style and conserva-
tive baselines are better for others. We introduce RELIABILITYROUTE, a
structural intervention that steers forecasting-agent behavior using reliabil-
ity features such as historical coverage, market-prior availability, source-
prior sharpness, evidence strength, evidence disagreement, and horizon.
A fixed 2024-fitted rule closely matches a hand taxonomy without hard-
coded source-name decisions, while a walk-forward self-adjusting rule re-
fits thresholds from previously resolved vintages and obtains the best mean
Brier score among our deterministic systems across 16 later LLM vintages.
The gain is modest and historical/search baselines remain highly compet-
itive. The main contribution is therefore a behavioral stress test showing
that more reasoning is not always better; forecasting agents should first
estimate which evidence source deserves control, routing policies should
themselves adapt under auditable constraints, and reproducibility artifacts
are available athttps://github.com/louiswang524/forcastagent.
1 Introduction
Forecasting agents estimate probabilities for future events from heterogeneous evidence
such as time-series histories, public forecasts, market prices, and textual context. This
setting is important because forecasts guide decisions under uncertainty, and benchmarks
such as ForecastBench provide a dynamic way to evaluate probabilistic forecasting systems
without relying on already-resolved static datasets (Karger et al., 2024). Many recent systems
combine retrieval, multiple reasoning roles, supervisor aggregation, and calibration. This
leaves a behavioral design question open: should every forecasting question trigger the
same agentic reasoning behavior, or should the system first decide whether to reason,
retrieve, defer to a prior, or use a structured analog?
The core behavioral challenge is that forecasting evidence is not exchangeable across sources.
A macroeconomic time-series question may be best answered by leakage-checked historical
analogs, a prediction-market question may already contain a strong crowd prior, and an
open-ended news question may require retrieval and textual reasoning. Treating these
settings with one uniform ensemble creates an over-reasoning failure mode: the agent
invokes expensive or brittle reasoning behavior even when a simpler evidence source is
more reliable. Conversely, selecting the best component on a calibration set can overfit the
mixture of sources and horizons in that vintage. The forecasting-agent design problem is
therefore not only how to build better reasoners, but how to steer behavioral mechanism
choice without leaking evaluation labels.
We propose to study forecasting agents as reliability-routed systems. Instead of presenting
another monolithic agent, we build a reproducible harness that decomposes a forecasting
1
arXiv:2609.28475v1  [cs.AI]  9 Jul 2026

Preprint.
system into four mechanisms: a reproduced multi-agent forecasting baseline, an evidence-
graph search loop, a leakage-checked historical analog forecaster, and feature-based routing
over these mechanisms. Our key method, RELIABILITYROUTE, fits a small threshold rule
over non-label reliability features rather than choosing per-source winners. We evaluate both
a frozen rule, which tests direct transfer from one calibration vintage, and a self-adjusting
rule, which updates thresholds only from previously resolved vintages in a walk-forward
protocol.
Our experiments produce three findings. First, fixed reliability routing can improve over
the best single deterministic baseline on a later ForecastBench vintage, reducing Brier score
from 0.1876 for HISTORICALANALOGto 0.1846 for RELIABILITYROUTEon the 2025-10-26
evaluation set. Second, fixed thresholds do not uniformly transfer: across 16 LLM vintages,
HISTORICALANALOGand SEARCHLOOPremain highly competitive. Third, walk-forward
self-adjustment closes this gap, reducing mean Brier from 0.1867 for the frozen reliability
router to 0.1839 and beating the frozen rule on 10 of 16 vintages. These results suggest that
a strong forecasting agent should not simply reason more. It should decide which kind of
evidence deserves control, while treating routing policies themselves as adaptive behaviors
that must be stress-tested across vintages.
Our contributions are:
• We introduce a reproducible behavioral stress-test harness for ForecastBench-style
forecasting agents, treating mechanism choice as an observable behavior alongside
probabilistic accuracy.
• We introduce RELIABILITYROUTE, a feature-based reliability router that replaces
hard-coded source-name routing with auditable thresholds over historical coverage,
market availability, prior sharpness, evidence strength, disagreement, and horizon.
• We show that fixed reliability routing can outperform the best single deterministic
baseline on one later vintage, and that walk-forward self-adjustment improves
average multi-vintage performance while preserving an inspectable rule family.
• We provide behavioral route diagnostics, source-slice diagnostics, threshold-
stability analysis, multi-vintage stress tests, oracle-routing headroom, and cali-
bration ablations showing when structured analogs, market/crowd priors, and
agentic reasoning are useful.
2 Method
2.1 Problem Setting
We consider binary forecasting questions. For each questionq, a system outputs a probability
p∈[ 0, 1] that the event resolves true. Once the event resolves with outcome y∈ {0, 1}, we
evaluate forecasts with Brier score (p−y) 2 (Brier, 1950), log score, and calibration error.
Lower Brier and log score are better. Each ForecastBench target also has metadata such as
source family, forecast due date, resolution date, and, when available, a frozen market or
crowd probability.
2.2 Behavioral Mechanisms
Our harness separates forecasting into behavioral mechanisms rather than treating the agent
as a single opaque policy. This decomposition is the main experimental object: it lets us ask
not only whether an agent is accurate, but what kind of behavior produced the forecast.
Historical analog forecaster.For structured sources such as FRED, DBnomics, and YFinance,
we build leakage-checked analog probabilities from observations dated no later than the
forecast due date. For each target, the forecaster computes the resolution horizon in days,
scans historical observations before the cutoff, and records whether the value increased over
matching horizons. A series is used only when at least 20 comparable historical outcomes
are available. The final probability is a clipped blend of the historical increase rate, a
2

Preprint.
ForecastBench
question
source family
and evidence type
historical analog
availabilitybehavior router
structured
analog
market/crowd
baseline
search/graph
fallback
probability forecast
Figure 1: RELIABILITYROUTEroutes each forecasting target to a mechanism based on
reliability features rather than fitting per-source winners on the evaluation distribution.
neutral prior, and a small mean-reversion adjustment based on the frozen value’s historical
percentile. If no historical analog is available, the forecaster falls back to the source prior
embedded in the question metadata.
Search and evidence-graph forecaster.The search loop plans four specialist queries: base
rate, recent evidence, resolution criteria, and counterevidence. The local search provider
retrieves only frozen benchmark evidence and leakage-checked historical analog documents;
it does not call live web search in the reported deterministic experiments. A deterministic
reasoner then updates a logit prior from retrieved document weights, historical-analog
probabilities, and market/crowd probabilities, and aggregates role forecasts by confidence-
weighted averaging in logit space. This module approximates the structure of LLM search
agents while keeping the ablation deterministic and inexpensive.
Reproduced multi-agent baseline.We implement an AIA-style reproduced baseline for
comparison (Alur et al., 2025): five focused agents forecast from different evidence groups,
a supervisor aggregates their probabilities using a median, and a fixed extremization slope
of 1.15 is applied in logit space. This baseline is not meant to be a claim about the original
system’s exact performance; it is a reproducible comparator that captures the broad motifs
of role-specialized forecasting, supervisor aggregation, and extremization.
2.3 Reliability Routing
We compare four behavioral routing policies. These are internal baselines and diagnostics,
not public named systems.Analog gatinguses a pure historical analog probability whenever
the search provider retrieves one; otherwise, it uses search/graph fallback.FITTEDROUTE
is a label-fit diagnostic: for each source family, it chooses the mechanism with the best Brier
score on the 2024 calibration vintage, then freezes that source-to-mechanism mapping for
evaluation. It is included to test whether direct empirical source fitting transfers, not as
a deployable method.TAXONOMYROUTEis a hand-written diagnostic router that maps
broad source families to mechanisms using source semantics: structured historical sources
are routed to historical analogs, market/crowd sources to the reproduced multi-agent
baseline, and unsupported cases to search/graph fallback. It provides an interpretable
reference point for how much of routing can be explained by obvious source taxonomy. Our
proposed method,RELIABILITYROUTE, removes source-name decisions and fits a small
reliability rule over non-label features. Figure 1 summarizes this routing view.
The distinction between FITTEDROUTEand RELIABILITYROUTEis deliberate. A fitted source
router can exploit calibration labels but may learn source-vintage artifacts. A reliability
router is less flexible: it can only use historical coverage, market/crowd prior availability,
prior sharpness, evidence strength, evidence disagreement, and horizon. We instantiate
3

Preprint.
Table 1: Initial RELIABILITYROUTEfeature rule fitted on the 2024 calibration vintage. In the
walk-forward variant, the same threshold family is refit from previously resolved vintages
before each later evaluation vintage.
Feature or threshold Role in routing
Historical coverage ≥
0.5
Allows historical analog routing when the target has an
analog and the source has broad analog coverage
Market sharpness ≥ 0.05 Routes to AIA-REPROwhen a non-neutral market/crowd
prior is available
Source prior sharpness
≥0.18
Routes to HISTORICALANALOGfallback when source pri-
ors are informative even without explicit analogs
Evidence strength
≥ 0.30 for historical
sources
Treats high-strength structured evidence as noisy and
routes to conservative AIA-REPRO
Horizon≤400 days Prevents long-horizon analogs from controlling when the
historical comparison is weak
Search strength ≥ 0.50
and disagreement
≤0.35
Allows search fallback only when retrieved evidence is
strong and not internally conflicted
this rule family in two ways. The fixed router selects thresholds on the 2024 calibration
vintage and freezes them. The self-adjusting router augments the semantic threshold
grid with quantiles from the available calibration feature distribution and, in the multi-
vintage protocol, refits thresholds before each evaluation vintage using only the original
calibration set and earlier resolved vintages. The feature set, rule order, candidate-threshold
construction, and component forecasters are fixed before walk-forward scoring begins;
resolved feedback can only choose threshold values within this pre-specified family. This
constraint turns routing into a behavioral intervention: it changes when the agent reasons,
retrieves, or defers, while keeping the intervention inspectable.
3 Experimental Setup
Benchmark.We use public ForecastBench dataset releases (Karger et al., 2024). Our
primary transfer protocol calibrates design choices on the 2024-07-21 human-written vintage
and evaluates without retuning on the 2025-10-26 LLM-written vintage. We also run a multi-
vintage stress test on 16 later LLM-written ForecastBench question sets from 2025-03-02
through 2025-12-07, excluding combination questions that do not match our binary single-
question protocol. For the self-adjusting router, each vintage is scored in chronological order
after refitting thresholds on only previously resolved vintages. This tests whether a design
rule survives changes in question provenance, source mixture, and resolution progress
without using current-vintage labels.
Baselines.We compare RELIABILITYROUTEagainst TAXONOMYROUTE, HISTORICALANA-
LOG, historical-evidence blending, SEARCHLOOP, FITTEDROUTE, AIA-REPRO, an evidence-
graph baseline, and a market-only baseline where applicable. TAXONOMYROUTEand
FITTEDROUTEare diagnostic routers introduced in this paper: TAXONOMYROUTEuses
human-written source-family rules, while FITTEDROUTEuses calibration-label performance
to choose one mechanism per source. AIA-REPROis our deterministic reproduction of the
main architectural pattern in AIA Forecaster (Alur et al., 2025); because the original system’s
full prompts, model choices, search stack, and calibration details are not all available in our
harness, we use it as a baseline for comparison rather than as a leaderboard claim about the
external system. We also include two diagnostic upper bounds: an oracle source router that
chooses the best mechanism per source using 2025 labels, and an oracle question router that
chooses the best mechanism per question using 2025 labels. These oracle systems are not
deployable; they measure remaining routing headroom.
4

Preprint.
Table 2: Single-vintage transfer result on 2025-10-26. The fixed row uses only the 2024
calibration vintage; the self-adjusting row uses the walk-forward rule available by this
vintage. Lower is better for all metrics.
System Brier↓Log score↓Cal. error↓
TAXONOMYROUTE0.1846 0.53930.0650
RELIABILITYROUTEfixed0.1846 0.53940.0649
HISTORICALANALOG0.1876 0.5460 0.0240
RELIABILITYROUTEself-adjusting 0.1876 0.5461 0.0232
Historical-evidence blend 0.1886 0.55050.0231
SEARCHLOOP0.1888 0.5524 0.0271
Analog-gated search 0.1888 0.5524 0.0271
FITTEDROUTE0.1949 0.5651 0.0797
AIA-REPRO0.2009 0.5808 0.1200
Evidence graph 0.2048 0.5858 0.1134
Market only 0.2296 0.6406 0.1180
Behavioral and outcome metrics.We report Brier score, log score, calibration error, and
routing behavior. Brier and log score are strictly proper scoring rules for probabilistic
forecasts (Gneiting & Raftery, 2007). Calibration error is computed by binning predictions
and comparing average predicted probability to empirical frequency. Routing behavior is
measured by the mechanism selected for each target: historical analog use, conservative
market/crowd-style baseline use, search-loop use, or graph-reasoning use. For paired
comparisons, we bootstrap question IDs with replacement using 2000 samples and report
95% percentile intervals for routed-system differences. For behavioral robustness, we
perturb each fitted reliability threshold and measure both route-change rate and change in
Brier score; for self-adjustment, we additionally log the active rule before every vintage.
Calibration ablation.To test whether the routed system merely needs post-hoc calibration,
we fit Platt-style transformations on the 2024 calibration vintage. A global calibration fits
one slope and intercept in logit space. A source-conditional calibration fits source-specific
slopes and intercepts when at least 20 calibration targets are available and otherwise falls
back to the global fit. Both transformations are frozen before scoring the 2025 evaluation set.
4 Results
Tables 2–3 and Table 4 answer different questions. The first two tables evaluate direct
transfer on one diagnostic vintage, including the frozen rule fitted only on 2024 data; the
multi-vintage table evaluates chronological adaptation across 16 later vintages, where the
self-adjusting rule may use only feedback from already resolved earlier vintages.
4.1 No-Retune T ransfer
Table 2 shows that the fixed RELIABILITYROUTErule matches the best Brier score among our
deterministic non-oracle systems while using feature thresholds rather than source-name
routing. It improves Brier by 0.0030 over the strongest single baseline, HISTORICALANALOG,
and by 0.0042 over the search loop. The gain is modest in absolute terms; paired-bootstrap
intervals are [−0.0062, 0.0005] against HISTORICALANALOGand [−0.0078, −0.0006] against
SEARCHLOOP. The self-adjusting rule is not better on this individual vintage, but it is much
better calibrated and becomes stronger in the 16-vintage walk-forward test below. This
distinction is important: fixed transfer asks whether one vintage’s thresholds generalize,
while walk-forward adaptation asks whether the routing behavior can improve as resolved
feedback accumulates.
5

Preprint.
Table 3: Observable routing behavior on the 2025 evaluation vintage. Fixed RELIABILITY-
ROUTEavoids the fitted router’s overuse of graph/search behavior; the self-adjusting rule
is more conservative on this vintage and shifts most targets to historical analog behavior.
Router Historical AIA-repro Search Graph
RELIABILITYROUTEfixed 589 488 0 0
RELIABILITYROUTEself-adjusting 1004 73 0 0
TAXONOMYROUTE588 489 0 0
FITTEDROUTE196 11 288 582
Table 4: Mean Brier score across 16 later LLM-written ForecastBench vintages. The self-
adjusting reliability router refits thresholds in walk-forward order using only previously
resolved vintages. Lower is better.
System Mean Brier↓Vintage wins Median rank
RELIABILITYROUTEself-adjusting0.18397/16 2.0
HISTORICALANALOG0.1841 2/16 3.0
SEARCHLOOP0.1848 1/16 4.0
TAXONOMYROUTE0.1863 4/16 3.5
RELIABILITYROUTEfixed 0.1867 1/16 4.0
FITTEDROUTE0.1940 1/16 6.0
AIA-REPRO0.2054 0/16 7.0
4.2 Behavioral Route Diagnostics
Table 3 reports the behavioral intervention directly. The fixed RELIABILITYROUTErule
routes 589 of 1077 targets to historical analog behavior and 488 to conservative reproduced-
baseline behavior, nearly matching the hand taxonomy without source-name rules. The
self-adjusting rule, after seeing earlier 2025 vintages, routes 1004 targets to historical analog
behavior and only 73 to the conservative baseline on this vintage; this explains why it is
better calibrated but not better in Brier on Table 2. By contrast, the fitted router routes
870 targets to graph/search behavior and performs worse. This supports the behavioral
interpretation of the main result: the failure mode is not simply poor probability calibration,
but unstable behavioral mechanism choice under transfer.
4.3 Multi-Vintage Stress T est
Table 4 extends the evaluation to 16 LLM-written vintages from 2025-03-02 through 2025-12-
07. This broader test changes the interpretation of RELIABILITYROUTE: fixed thresholds are
useful but brittle, while walk-forward self-adjustment yields the best mean Brier among our
deterministic systems. The self-adjusting router improves mean Brier from 0.1867 for the
frozen rule to 0.1839, wins 7 of 16 vintages, and beats the frozen rule on 10 of 16 vintages. A
vintage-level paired bootstrap gives a mean Brier difference of −0.0029 against the frozen
rule with 95% interval [−0.0056, −0.0006]. The gain remains modest: HISTORICALANALOG
is close at 0.1841, and the bootstrap interval against HISTORICALANALOGoverlaps zero.
This supports a behavioral rather than leaderboard-style interpretation: routing helps when
it adapts under constraints, but many targets are already well served by simple structured
analogs or deterministic search evidence.
Threshold and route traces explain what self-adjustment changes behaviorally. After early
vintages, the rule becomes stricter about source-level historical coverage, raises market-
prior sharpness thresholds, and mostly disables search fallback when prior vintages do not
support it; the full per-vintage rule trace is included in the reproducibility artifacts. Across
vintages, single-threshold perturbations change 4.3% of routes on average and change Brier
by 0.0007 on average, although the most disruptive perturbations can change up to 21% of
routes on some vintages. The intervention is therefore not merely changing probabilities; it
6

Preprint.
Table 5: Source-level Brier score on the 2025 evaluation vintage. Parentheses show the
number of targets. The best mechanism depends strongly on source family, and fixed versus
self-adjusting routing make different source-level tradeoffs.
Source RELIABILITYROUTEfixed RELIABILITYROUTEself-adj. TAXONOMYROUTEHISTORICALANALOGAIA-REPRO
ACLED (200)0.1112 0.1112 0.1112 0.11120.1543
DBnomics (190)0.23300.24700.23300.24700.2330
FRED (196)0.2292 0.2292 0.2292 0.22920.2564
Infer (5)0.03910.05480.03910.05480.0391
Manifold (21)0.03470.03700.03470.03770.0347
Metaculus (11) 0.2321 0.2111 0.23210.20720.2321
Polymarket (70) 0.0170 0.02050.01670.02090.0167
Wikipedia (192)0.1821 0.1821 0.1821 0.18210.2006
YFinance (192)0.24890.25080.24890.25080.2489
Table 6: Routing and calibration ablations on the 2025 evaluation vintage. Oracle rows use
2025 labels and are diagnostic upper bounds rather than deployable systems. Lower is
better for all metrics.
System Brier↓Log score↓Cal. error↓
Oracle question router0.1196 0.38220.2369
Oracle source router0.1844 0.53770.0634
TAXONOMYROUTE0.1846 0.53930.0650
RELIABILITYROUTEfixed0.1846 0.53940.0649
HISTORICALANALOG0.1876 0.54600.0240
RELIABILITYROUTEself-adjusting 0.1876 0.54610.0232
TAXONOMYROUTE+ global calibration 0.1882 0.5531 0.0670
FITTEDROUTE0.1949 0.5651 0.0797
TAXONOMYROUTE+ source calibration 0.2004 0.5798 0.1025
AIA-REPRO0.2009 0.5808 0.1200
is changing which behavioral mechanism is allowed to control the forecast, while leaving a
visible audit trail of rule drift.
4.4 Source-Slice Diagnostics
Table 5 explains why routing helps and why the two RELIABILITYROUTEvariants differ.
Historical analogs dominate for ACLED, FRED, and Wikipedia. The reproduced multi-agent
baseline is stronger for DBnomics, YFinance, and several market-family sources. Fixed
RELIABILITYROUTErecovers almost the same slice behavior as TAXONOMYROUTEfrom
reliability features rather than source names. Self-adjusting RELIABILITYROUTEimproves
some small market-like slices by using historical behavior more often, but loses on DBnomics
and YFinance on this vintage by over-shifting toward historical analogs. This is the single-
vintage cost of the adaptation that improves average multi-vintage performance.
4.5 Ablations and Negative Results
FITTEDROUTEdirectly fits the best mechanism per source on the 2024 vintage, so it is
intentionally more label-dependent than TAXONOMYROUTEor RELIABILITYROUTE. This
diagnostic performs worse than using the source taxonomy. It selects evidence graph for
DBnomics and YFinance because those choices win on the calibration vintage, but the same
choices fail on the 2025 vintage. This yields Brier 0.1949, worse than HISTORICALANALOG
and SEARCHLOOP. The result shows that behavioral routing is useful only when the routing
rule is constrained by reliability structure or validated across vintages.
Table 6 shows two additional negative results. First, post-hoc Platt-style calibration fitted on
the 2024 vintage does not repair the routed system: global calibration worsens Brier from
0.1846 to 0.1882, and source-conditional calibration worsens it to 0.2004. This suggests that
the calibration mismatch is not a single global slope/intercept problem and that source-
level calibration overfits when each slice is small. Second, the oracle source router reaches
7

Preprint.
0.1844 on the 2025-10-26 vintage, only 0.0002 Brier better than the fixed RELIABILITYROUTE
rule on that diagnostic split. Thus, much of the single-vintage source-level headroom is
already captured by reliability routing, while the multi-vintage results show that threshold
adaptation matters for transfer. The much stronger oracle question router shows that fine-
grained per-question routing could matter, but using evaluation labels makes this only an
upper bound.
5 Related Work
Forecasting has a long tradition of evaluating probabilistic predictions with proper scoring
rules (Brier, 1950; Gneiting & Raftery, 2007). Human forecasting research shows that
expert forecasters can be systematically trained and evaluated (Tetlock & Gardner, 2015),
while prediction markets aggregate dispersed information through market prices (Hanson,
2003). ForecastBench provides a dynamic benchmark for comparing AI, public, and expert
forecasts on future-resolving questions (Karger et al., 2024). AIA Forecaster is a closely
related LLM forecasting system that combines agentic search, supervisor aggregation, and
calibration (Alur et al., 2025); we use an AIA-style reproduced baseline as one comparator
in our harness. Our work focuses on a different axis: isolating mechanism choice and
evaluating it as an observable agent behavior. This connects forecasting accuracy to a
behavioral question: when should an agent retrieve, reason, defer to an external prior, or
rely on structured historical evidence?
6 Limitations
Our study is intentionally component-level. Our AIA-style reproduced baseline does not
use the same search stack, prompts, models, or calibration procedure as the reported AIA
Forecaster system, so it should be read as a baseline for comparison rather than a reproduc-
tion claim. The main single-vintage gain is modest, and the paired bootstrap interval against
the strongest single baseline slightly overlaps zero. The multi-vintage self-adjusting gain
is also narrow: RELIABILITYROUTEhas the best mean Brier in our deterministic harness,
but HISTORICALANALOGis close and several vintages are still won by simple baselines
or the hand taxonomy. RELIABILITYROUTEreplaces source-name routing with feature
thresholds, but those thresholds are selected from a human-designed rule family; future
work should validate the same adaptation procedure with nested development splits and ex-
ternal forecasting datasets. Our behavioral analysis also observes only mechanism selection
and route-level features, not richer interaction behavior such as search-query refinement,
tool-use trajectories, or multi-agent disagreement dynamics. Finally, RELIABILITYROUTE
improves Brier and log score on some vintages but often worsens calibration error, and
our train-fitted global and source-conditional calibration attempts both fail to transfer.
Downstream users who require calibrated probabilities should therefore treat conditional
calibration as an unsolved component rather than a solved add-on.
7 Conclusion
Forecasting agents should not reason uniformly across all questions. In our ForecastBench
transfer study, historical analogs, market/crowd-style baselines, and search/graph rea-
soning have different source-dependent error profiles. A feature-based reliability router
can improve on individual vintages, and walk-forward self-adjustment improves mean
multi-vintage Brier while remaining more constrained than directly fitting per-source win-
ners. The practical lesson is therefore not that routing alone solves forecasting. It is that
behavior choice is itself an object of evaluation: before adding more reasoning, a forecasting
agent should estimate which evidence source deserves control, update that estimate only
from resolved evidence, and spend future complexity on within-source forecasting, richer
behavioral traces, and robust conditional calibration.
8

Preprint.
Reproducibility Statement
We provide an reproducibility artifact at https://github.com/louiswang524/forcastagent.
The artifact includes the deterministic forecasting-agent harness, cached public Forecast-
Bench inputs, smoke tests, and scripts for rerunning the fixed-transfer, calibration, source-
slice, threshold-stability, and walk-forward self-adjustment experiments reported in this
paper. No API key is required for the deterministic results.
Ethics Statement
This work studies probabilistic forecasting systems. Such systems can support better
decision-making, but overconfident or poorly calibrated forecasts may cause harm if used
without human oversight. We therefore report calibration error, negative transfer results,
and limitations alongside accuracy metrics.
References
Rohan Alur, Bradly C. Stadie, Daniel Kang, Ryan Chen, Matt McManus, Michael Rickert,
Tyler Lee, Michael Federici, Richard Zhu, Dennis Fogerty, Hayley Williamson, Nina
Lozinski, Aaron Linsky, and Jasjeet S. Sekhon. Aia forecaster: Technical report.arXiv
preprint arXiv:2511.07678, 2025.
Glenn W. Brier. Verification of forecasts expressed in terms of probability.Monthly Weather
Review, 78(1):1–3, 1950.
Tilmann Gneiting and Adrian E. Raftery. Strictly proper scoring rules, prediction, and
estimation.Journal of the American Statistical Association, 102(477):359–378, 2007.
Robin Hanson. Combinatorial information market design.Information Systems Frontiers, 5
(1):107–119, 2003.
Ezra Karger, Houtan Bastani, Yueh-Han Chen, Zachary Jacobs, Danny Halawi, Fred Zhang,
and Philip E. Tetlock. Forecastbench: A dynamic benchmark of ai forecasting capabilities.
arXiv preprint arXiv:2409.19839, 2024.
Philip E. Tetlock and Dan Gardner.Superforecasting: The Art and Science of Prediction. Crown,
2015.
9
