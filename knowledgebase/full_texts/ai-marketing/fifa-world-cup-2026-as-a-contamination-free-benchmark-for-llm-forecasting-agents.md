---
title: 'FIFA World Cup 2026 as a Contamination-Free Benchmark for LLM Forecasting Agents: Four Models,
  a Bookmaker, and 104 Matches'
url: https://arxiv.org/abs/2607.17765
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Jiacheng Ding
- Cong Guo
- Jason Xu
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.17765
pages: 9
chars: 39404
fetched_at: '2026-11-08T13:04:20+00:00'
kb_version: 1
---

# FIFA World Cup 2026 as a Contamination-Free Benchmark for LLM Forecasting Agents: Four Models, a Bookmaker, and 104 Matches

FIFA World Cup 2026 as a Contamination-Free Benchmark for
LLM Forecasting Agents: Four Models, a Bookmaker, and 104
Matches
Jiacheng Ding∗
University of Memphis
Memphis, Tennessee, USA
jding2@memphis.edu
Cong Guo∗
University of Memphis
Memphis, Tennessee, USA
cguo@memphis.edu
Jason Xu
QuantaInsight
Seattle, Washington, USA
jasonx@quantainsight.info
Abstract
We introduceWC2026-Agents, a benchmark and dataset for eval-
uating large language models (LLMs) asautonomous forecasting
agentson real, future events. For every one of the 104 matches of the
2026 FIFA World Cup, four frontier models — Claude Opus 4.8, Chat-
GPT (GPT-5.5, high reasoning), Gemini 3.1 Pro, and Grok (Expert
Mode) — ran an identical search–act–reflect loop: gather evidence
with a web tool, commit to a 1X2 (team-A win / draw / team-B win)
probability distribution and a virtual $100 bet, and, after the match,
reflect given only the final score. Because every match kicked off
after the models’ training cutoffs, the benchmark iscontamination-
freeby construction. Crucially, we pair the four agents with a fifth
competitor drawn from the same information environment — the
pre-match betting market — collected as per-match 1X2 odds, giv-
ing an economically grounded human baseline and letting us score
not just what an agent predicts but what itdoes with money. The
release contains 416 forecasts and 414 reflections with verbatim
reasoning, ground truth (including penalty shootouts), odds, and
a reproducible evaluation suite. A reference evaluation surfaces
findings that raw accuracy hides: the four agents issue an identi-
cal top pick in 92% of matches and none beats the market’s Brier
score, yet they diverge sharply as decision-makers — betting return-
on-investment ranges from−18%to +10%, fading the market is
unprofitable for all four, the share of forecasts that cite the market
ranges from 12% to 100%, and self-reported error rates on wrong
picks range from 36% to 86%. The benchmark thus measures calibra-
tion, decision quality, and self-knowledge — axes on which frontier
models differ even when their predictions do not. Data and code:
https://github.com/graphuofm/FIFA2026LLM.
CCS Concepts
•Computing methodologies → Artificial intelligence;•In-
formation systems→Data mining.
Keywords
large language models, LLM agents, forecasting, calibration, pre-
diction markets, sports analytics, benchmark dataset, data contami-
nation
1 Introduction
Large language models are moving from answering questions to
acting: retrieving evidence, reasoning, committing to decisions,
and reflecting on outcomes [ 22, 34, 36]. Evaluating this agentic
behaviour is hard for three reasons. First, most benchmarks are
∗These authors contributed equally to this research.
static and increasinglycontaminated— test items leak into training
data [8, 17]. Second, they score a single answer and ignore what an
agent woulddowith a belief. Third, they lack a strong, economically
meaningful human baseline.
Real-world forecasting offutureevents dissolves all three prob-
lems at once. A scheduled sporting tournament provides a stream of
questions whose answers (i) do not exist at query time, so contami-
nation is impossible; (ii) arrive on a known date with unambiguous
ground truth; (iii) are continuously priced by a liquid betting mar-
ket that aggregates human and algorithmic beliefs into calibrated
probabilities [28, 31]. The 2026 FIFA World Cup — 104 matches over
five weeks, every one after current models’ training cutoffs — is
close to an ideal such stream.
We use it to buildWC2026-Agents, a benchmark that treats
four frontier LLMs as forecasting agents and the betting market as
a fifth competitor. For each match, each agent runs a fixedsearch–
act–reflectloop: it searches the web for team news and prices,
acts by returning calibrated 1X2 (team-A win / draw / team-B
win) probabilities together with a virtual $100 staking decision,
and — once the score is known — reflects on its own forecast. We
settle every bet at real 1X2 odds, so the benchmark scores three
distinct capabilities that usually travel together but here come apart:
predictive calibration(are the probabilities right?),decision quality
(does the agent profit against a real price?), andself-knowledge(does
it know when it was wrong?).
A reference evaluation of the four 2026 models illustrates why
these axes matter. Onwhat will happen, the agents are nearly in-
terchangeable: they choose the same most-likely outcome in 92%
of matches, their accuracies fall in a three-point band, and none
beats the market’s Brier score — an efficient-market result that a
single-answer benchmark would report as a null. Onwhat to do
about it, they diverge sharply: betting ROI spans −18%to +10%;
fading the market loses money for every agent; the fraction of fore-
casts that even mention the market spans 12% to 100%; and, on their
own wrong picks, self-reported error rates span 36% to 86%. These
behavioural axes, not accuracy, are where frontier models differ.
Contributions.
• A contamination-free agentic-forecasting benchmarkover
all 104 matches of a future World Cup: 416 forecasts and 414
reflections from four frontier LLMs, with verbatim reasoning,
paired pre-/post-match structure, and a reproducible evaluation
suite (§4, §5).
• A market baseline as a fifth competitor.We release per-
match 1X2 odds and the settlement machinery so any forecaster
arXiv:2607.17765v1  [cs.LG]  20 Jul 2026

Ding, Guo, and Xu
can be scored not only for calibration but for realized betting
profit against a real price (§4.5).
• A curated, documented dataset.Fixtures, team orientation,
scores (including penalty shootouts and who advanced) were
hand-resolved from four heterogeneous transcripts and cross-
checked four ways (§4.4).
• A reference evaluationspanning calibration, betting/decision
quality, reasoning content, and reflection honesty, with the find-
ings above and a distillation of the agents’ recurring blind spots
into candidate features (§6).
2 Related Work
LLMs as forecasters.Retrieval-augmented LLMs can approach
human crowd accuracy on judgemental questions [11], and LLM
ensembles rival human crowds [23], echoing the human superfore-
caster literature [ 26]. Dynamic forecasting benchmarks such as
ForecastBench[ 15] and early neural event forecasting [37] score
probabilistic accuracy. We add three elements those lack: a fixed
agentic loop, a betting-baseddecisionscore against a real market,
and paired self-reflection.
LLM agents, reasoning, and reflection.Agentic scaffolds in-
terleave reasoning and tool use [30, 36] and let models critique and
revise their own outputs [18, 24], though unaided self-correction is
fragile [13]. Surveys chart the space [29, 34]. Our reflection prompt
is a minimal, standardized probe of self-knowledge at tournament
scale.
Calibration and uncertainty.Modern networks are often mis-
calibrated [10]; LLM confidence can be elicited but is imperfectly cal-
ibrated [14, 27, 35]. We measure calibration with reliability curves
and expected calibration error [ 20], and full-distribution quality
with the Brier score [4] and log-loss.
Betting and prediction markets.Bookmaker odds are strong,
hard-to-beat probability estimates [1, 28, 32], consistent with mar-
ket efficiency [7] and exhibiting known regularities such as the
favorite–longshot bias [16, 25]. Machine-learning football models
are a long line of work [3, 5]. We use the market both as a baseline
and as the price an agent may follow or fade.
Benchmarks and contamination.Static benchmarks [ 12, 17]
face contamination as models train on ever more of the web [ 8].
Forecasting strictly future events is contamination-free by con-
struction, a property we exploit. Finally, algorithm aversion [6] and
overconfidence [19] frame our behavioural analysis.
3 Task Formulation
A match 𝑥 has an outcome 𝑜(𝑥) ∈ Y=
{team_a_win,draw,team_b_win} , where team A is the first-
listed side. A forecasting agent 𝑔 observes 𝑥 and its public
information environment and returns a distribution 𝑝𝑔(𝑥)∈Δ(Y)
and a decision 𝑑𝑔(𝑥)=(pick,stake) with stake∈[ 0, 100]. After
the match it returns a reflection 𝑟𝑔(𝑥) . The market 𝑚 supplies an
implied distribution 𝑝𝑚(𝑥) obtained by removing the vigorish
from published 1X2 odds; it makes no bets and files no reflection,
serving as a fifth forecaster and as the price at which agent bets
settle. Knockout ties that finish level go to a shootout; because a
1X2 bet settles on the 90-minute result, we take 𝑜(𝑥) to be that
result (adrawfor such ties) and separately record the shootout
winner (§4.4).
4 The WC2026-Agents Benchmark
4.1 Agent protocol
Each match generates two turns in a single per-model conversa-
tion. Thepre-matchturn ( 𝑇− 24h) instructs the agent that it is in
a research study (virtual money; do not refuse), names the fixture,
tells it to use web search, and requires a strict JSON reply:
{"probabilities": {"team_a_win", "draw",
"team_b_win"},
"bet": {"pick", "stake_usd"},
"reasoning": ..., "key_sources": [urls]}
Thepost-matchturn provides only the final score and asks —
without web access — for a reflection: anoutcome_vs_prediction
label (correct/partially_correct/incorrect), a calibration self-
judgement, a luck attribution, onekey_factor_i_missed, one
key_factor_i_overweighted, a counterfactual, a would-bet-
differently verdict, and a confidence. The prompt text is byte-
identical across agents; only the model changes.
4.2 Models
We evaluate four frontier assistants queried through their con-
sumer interfaces with web tools enabled and held fixed across the
tournament: Claude Opus 4.8 [2], ChatGPT (GPT-5.5 “Thinking”,
high reasoning effort) [21], Gemini 3.1 Pro [9], and Grok in Expert
Mode [33]. Using production assistants (rather than raw API base
models) is deliberate: it captures the retrieval-and-reasonagenta
user actually deploys, which is the object of study.
4.3 Data collection
Between 11 June and 19 July 2026, each agent was run on all 104
fixtures (𝑚01–𝑚72group, 𝑚73–𝑚104knockout), producing a pre-
match forecast∼24h before kickoff and a post-match reflection after
the result. Raw transcripts are archived read-only. The pre-match
window strictly precedes each outcome, so no target could appear
in any model’s training data.
4.4 Curation and quality control
Group-stage transcripts follow a regular structure and were parsed
with a string-aware JSON extractor. The knockout transcripts are
not regex-parseable: they use four different header renderings,
some Round-of-16 fixtures were pasted with bracket placehold-
ers (“W74 vs W77”) whose numbering does not match reality,
and final scores appear in a dozen phrasings (penalty shootouts,
lower-cased names, occasionally reversed team order). We there-
forehand-resolvedfixtures, team orientation, and ground truth for
all 32 knockout matches from the transcripts, encoding them in a
verified table. As an automatic guard, the human-pasted score line
in each of the four agents’ transcripts is compared to that table; the
four-way check flagged zero disagreements across all 128 knockout
cells. Ground truth records the 90-minute result, the shootout result
where applicable, and which side advanced. Every deviation from
the JSON schema (recovered braces, duplicated pastes, two missing
Gemini reflections) is logged rather than dropped.

FIFA World Cup 2026 as a Contamination-Free Benchmark for LLM Forecasting Agents: Four Models, a Bookmaker, and 104 Matches
Table 1: Dataset coverage. Two Gemini group reflections are
absent in the source and flagged, not imputed.
Stage Matches Agents Forecasts Reflections Bets placed
Group 72 4 288 286 232
Knockout 32 4 128 128 103
Total 104 4 416 414 335
4.5 Market odds
We release pre-match 1X2 odds for all 104 matches with a source
URL each, oriented to team A and vig-removed to implied probabil-
ities (mean overround1 .05). Knockout odds are opening lines from
public sportsbook previews; we validated them against the market
probabilities the agents themselves cited in their reasoning (e.g. our
de-vigged Brazil–Japan line, 55/25/20, matches a cited “56/25/19”),
and corrected one line whose implied hold was economically im-
possible. The market is thus both an independent baseline and the
settlement price for agent bets.
4.6 Schema, statistics, accessibility
The release is one row per (agent, match): fixture and stage; ground
truth with penalty and advancement fields; the pre-match proba-
bilities, pick, stake, verbatim reasoning and cited URLs; the eight
reflection fields; and parse-issue flags. A tidy 104-match table joins
all agents and the market for analysis. Table 1 summarizes coverage.
All data (CC BY 4.0) and code (MIT), including the one-command
pipeline that regenerates every table and figure, are public; the
dataset requires no access request.
An illustrative record.For match 𝑚92(Brazil vs. Norway, Round
of 16), one agent returned the pre-match forecast {team_a_win:
0.55, draw:0 .25, team_b_win:0 .20}, a $40 stake on Brazil, and the
reasoning “Brazil enters as heavy favorites with superior squad
depth . . . Norway’s Haaland–Ødegaard threat and historical edge
make an upset possible. ” Norway won2–1. The paired reflection
then labelled the outcomeincorrect, named the missed factor as
“Norway’s historical dominance and counter-attacking effectiveness
. . . amplified by Haaland, ” and the over-weighted factor as “Brazil’s
overall squad depth and pedigree. ” Every record has this pre/post
structure, letting a user trace a belief, a decision, a result, and a
self-assessment for the same event.
5 Benchmark Tasks and Metrics
The suite scores three capabilities.
(T1) Calibrated prediction.Accuracy (arg max𝑝 𝑔 =𝑜); multi-
class Brier ˝ 𝑖(𝑝𝑔,𝑖−⊮[𝑜=𝑖]) 2; log-loss−log𝑝 𝑔,𝑜; and, for the top
pick, a reliability curve and expected calibration error (ECE) [20]
over ten confidence bins.Convergence— the fraction of matches on
which all agents share an arg max — quantifies how much accuracy
can separate them.
(T2) Decision quality.Each agent’s own pick/stake settles at
the match’s decimal odds on the 90-minute result: profit =stake×
(dec− 1) on a win, else−stake. We report bankroll, ROI, hit-rate,
and acontrariansplit: a bet is contrarian if its pick differs from
the market’s most-likely outcome, isolating the value of fading the
Table 2: Task T1 — calibrated prediction over all 104 matches.
Best in bold;↑/↓ = higher/lower better. The market attains
the best Brier score.
Acc.↑Brier↓LogLoss↓ECE↓Draw mass
Claude .664 .4705 .806 .116 .234
ChatGPT.683.4729 .814 .111 .235
Gemini .654 .4828 .820.068.238
Grok.683.4706.803.097 .227
Market.683 .4688.807 — .229
Table 3: Task T2 — betting/decision quality over all 104
matches. Each agent settles its own picks at real 1X2 odds.
“Contr. ” = contrarian (against-market) bets.
#Bets Staked Net $ ROI % Hit Contr. share/ROI
Claude 73 1519−275−18.1.329 .58 /−24%
ChatGPT 55 1471+118+8.0.509 .36 /−14%
Gemini 103 8660+322+3.7.631 .14 /−12%
Grok 104 6305+650+10.3.673 .05 /+33%
price. The market’s implied probabilities are scored under T1 as a
fifth forecaster.
(T3) Behavioural transparency.Everyreasoningand reflec-
tion field is coded into 13 factor categories with a published keyword
lexicon (no model in the loop), giving each agent’s information diet
and itsself-knowledge: on the matches its arg max got wrong, how
often does its reflection label itselfincorrect?
6 Reference Evaluation
We evaluate the four 2026 agents and the market. Tables 2 and 3
give the headline numbers; figures expand each result.
6.1 The agents converge; accuracy cannot
separate them
The four agents issue an identical top pick in92%of matches (91.7%
group, 93.8% knockout; Fig. 1). Pairwise agreement reaches 100%
(ChatGPT–Grok) and never falls below 92%. Accuracy therefore
spans only three points (Table 2), i.e. three matches. Figure 2 shows
the mechanism: each agent’s team-A probability tracks the market’s
almost perfectly (𝑟= 0.97–0.99), so the agents are, to first order,
reading and lightly re-expressing the same price. On the eight
matches where they are not unanimous, the split is always 3–1 (a
single agent dissents), and the dissenter is usually Gemini (six of
eight) — consistent with it being the least market-anchored agent
(Fig. 5). All eight are near-coin-flips where the market itself is
close to even, so a shade more weight on one side tips the arg max.
Disagreement thus appears exactly where the signal is weakest, not
where an agent has found private information.
6.2 No agent beats the market
Scored as a forecaster, the market attains the best Brier score of
all five competitors (0.469 vs. 0.471 for the best agent) and ties the

Ding, Guo, and Xu
ClaudeChatGPTGeminiGrok Market
Claude
ChatGPT
Gemini
Grok
Market
1.00 0.98 0.92 0.98 0.98
0.98 1.00 0.94 1.00 1.00
0.92 0.94 1.00 0.94 0.94
0.98 1.00 0.94 1.00 1.00
0.98 1.00 0.94 1.00 1.00
Pairwise same-pick rate (agents + market)
Group (72) Knockout (32)
0
20
40
60Matches
43
24
split 5
22
8
split 2
Rarely split; unanimous ≈ 2× more right than wrong
unanimous · correct
unanimous · wrong
models split
Agreement of the four agents' top pick
Figure 1: Convergence. Left: pairwise same-pick rate. Right: match counts by consensus; genuine disagreement is rare and
unanimous picks are right about twice as often as wrong.
0.0 0.5 1.0
Market P
0.0
0.5
1.0Model P(team A win)
r=0.99
Claude
0.0 0.5 1.0
Market P
r=0.99
ChatGPT
0.0 0.5 1.0
Market P
r=0.97
Gemini
0.0 0.5 1.0
Market P
r=0.98
Grok
pick correct
pick wrong
Agent vs. market-implied probability (team-A win), 104 matches per agent
Figure 2: Each agent’s probability for a team-A win against the market-implied probability, all 104 matches. Points hug the
diagonal (𝑟shown); Gemini is the loosest, consistent with it rarely citing the market (Fig. 5).
best accuracy (Table 2; per-stage in Table 4). It also identifies the
advancing side in 24 of 32 knockout ties (75%), equal to the agents.
This is the expected efficient-market outcome [28]: web-enabled
agents recover the market’s information but do not systematically
exceed it. The tournament was mildly favorite-friendly, which the
released odds let users control for: binning matches by the market’s
implied probability for its favored side, that side won 62% of the
time when priced near 48% and 78% when priced near 62%, while
heavy favorites (∼81%) were well-calibrated. In a cup with slightly
fewer upsets than priced, every forecaster that respected the market
— agents and market alike — looks under-confident in hindsight
(§6.3), a difficulty profile the benchmark exposes rather than hides.
6.3 Calibration does separate them
All four agents lieabovethe reliability diagonal: they areunder-
confidenton their top pick, which wins more often than its stated
probability (Fig. 8). Gemini is best calibrated (ECE 0.068), then
Grok (0.097), ChatGPT (0.111), Claude (0.116). Calibration and full
distribution can disagree: Gemini has the best top-pick ECE but the
worst Brier, because it spreads probability mass more aggressively
and stakes larger (Table 3); the per-agent reliability curves are in
App. B (Fig. 8).
6.4 Decision quality diverges where accuracy
does not
Settling each agent’s own picks at real odds, betting ROI spans
−18.1%(Claude) to +10.3%(Grok), with net results of −$275to

FIFA World Cup 2026 as a Contamination-Free Benchmark for LLM Forecasting Agents: Four Models, a Bookmaker, and 104 Matches
+$650(Table 3, Fig. 3). The spread is not driven by who they pick
— they pick alike — but byhow much they stake and whether they
respect the price. Gemini stakes most aggressively ($8,660 across 103
bets); Claude stakes least and most often on draws and underdogs.
As a reference, a naive baseline that stakes a flat $100 on the market
favourite every match returns+$1,041(grey line, Fig. 3), out-earning
all four agents in absolute terms at comparable ROI — a betting
counterpart of the result that no agent beats the market. (Favorites
over-performed their price this cup, §6.3; the released odds let users
hold this difficulty fixed.)
6.5 Fading the market is unprofitable for every
agent
Decomposing bets by their relationship to the price explains the
P&L (Fig. 4). Contrarian (against-market) bets hit 21–40% and return
−24%to+33%(the lone positive being Grok’s five such bets), while
market-conforming bets are the source of all profit. The ordering is
monotone: the more an agent fades the market, the worse it does.
Claude cites the market in every forecast yet bets against it 58% of
the time — itseesthe price and overrides it — and is the only agent
with a net loss.
6.6 Staking discipline is a distinct axis
Beyondwhichside to back, agents differ in how theysizea bet. We
correlate each agent’s stake with the edge it believed it held (its
probability minus the market’s for the picked side) and with its
confidence. Grok’s stake tracks its confidence most tightly (Pear-
son 𝑟=0.85) and its claimed edge positively (𝑟=0.13) — Kelly-like
behaviour that concentrates money on its strongest reads. Gemini
and ChatGPT also stake up with confidence (𝑟=0.54and0 .53), but
Gemini’s mean stake ($84 of a $100 budget) is a near-max-bet habit
that inflates variance — its bankroll in Fig. 3 is the most volatile
of the four. Claude is the reverse: its stake isnegativelyrelated to
confidence (𝑟=− 0.20), because it sizes up precisely on the low-
confidence, against-market “value” plays that tend to lose. Staking
discipline is therefore a separate, measurable axis, only loosely cou-
pled to whether a pick is correct, and the released stakes let others
re-score the agents under any fixed staking policy.
6.7 Information diets differ while picks
converge
Coding the reasoning reveals sharply different information diets
that nonetheless yield the same picks (Fig. 5). The share of forecasts
that cite the betting market or odds ranges from100% (Claude) and
92% (ChatGPT) to 12% (Gemini); Gemini reasons almost entirely
from football (attacking threat, defensive organisation, form) while
barely referencing the price. This is the behavioural counterpart
of Fig. 2: Gemini is market-blind in itsstated reasoningyet still
lands near the market, and consequently fades it in only 14% of its
bets. Grok most often invokes “paper strength” (squad depth 88%,
form 76%, FIFA ranking 61%); Claude most often invokes knockout
variance (53%).
6.8 Reflection is a behavioural fingerprint
Given only the final score, the agents reflect very differently on
their own mistakes (Fig. 7). On the picks each got wrong, the rate
of admitting “incorrect” ranges from86% (Gemini) to 36% (Chat-
GPT), which softens 55% of its errors to “partially correct”; Claude
(49%) and Grok (61%) sit between. When they were right, the rate
of claiming “correct” ranges from 68% (Claude) to 94% (Grok). Re-
flection style is thus a stable per-agent trait, orthogonal to accuracy
— relevant wherever a model’s self-report gates a downstream ac-
tion [13, 24].
6.9 Shared blind spots and candidate features
Eight matches were mispredicted byall fouragents (Fig. 6); in every
case they backed the favourite. Four were penalty ties in which
a heavy favourite (Germany, 75% consensus) failed to win in 90
minutes; the rest were regulation upsets (e.g. Norway over Brazil,
Belgium 4–1 over the USA, Spain over France). The agents’ own
post-mortems are strikingly consistent: across all wrong picks, the
factor most often named asmissedis underdog defensive organisa-
tion (62%), then knockout/penalty variance (32%); the factor most
often named asover-weightedis the favourite’s squad quality (40%)
and attacking firepower (38%). These yield concrete, minable priors
for future systems: down-weight a favourite’s paper talent against
a disciplined low block, and explicitly price the draw→shootout
path in knockout ties.
7 Discussion and Impact
The benchmark separates three capabilities that a single-answer
score conflates. On prediction the 2026 agents are interchange-
able and no better than the market; ondecisionandself-knowledge
they differ by large, stable margins. For practitioners the lesson is
that selecting an LLM for a consequential forecasting-and-acting
pipeline should weigh calibration, staking discipline, and honest
self-assessment, not headline accuracy. Because the protocol is
a thin wrapper around a consumer assistant, WC2026-Agents is
a template: the same search–act–reflect loop and market settle-
ment apply to any scheduled, market-priced event stream (other
tournaments, elections, product launches), enabling live, rolling,
contamination-free evaluation and longitudinal tracking of model
releases. We release the loop, lexicon, and settlement code to that
end.
Two results deserve emphasis for benchmark design. First, the
convergence of four independently built models cautions against
reading a single leaderboard number as a capability signal: when
models share a retrieval surface they also share errors, so an en-
semble inherits rather than cancels the common bias — a limit on
the “wisdom of the silicon crowd” [23] when the crowd reads the
same web. Second, that no agent beats a vig-bearing market is the
sharpest available null for an over-eager “LLMs can predict the
future” narrative: the market is not a weak baseline but a near-
efficient [7, 28] aggregator that the agents match but do not exceed,
so a benchmark that omits it would mistake market-level perfor-
mance for super-human forecasting. Surfacing such failure modes
is precisely the role of a datasets-and-benchmarks contribution.

Ding, Guo, and Xu
20 40 60 80 100 120
Match number (m01 → m104)
−500
−250
0
250
500
750
1000
1250
Cumulative net profit (virtual $)
  knockout →
Market (flat-fav)  $+1041
Claude  $-275  (-18.1%)
ChatGPT  $+118  (+8.0%)
Gemini  $+322  (+3.7%)
Grok  $+650  (+10.3%)
group stage
Cumulative virtual profit at real 1X2 odds (agents' own stakes; market = flat stake on its favourite)
Figure 3: Cumulative virtual profit over the 104-match tournament, each agent settling its own stakes at real 1X2 odds.
Trajectories diverge despite nearly identical point predictions.
0 20% 40% 60%
Share of bets that fade the market
Claude
ChatGPT
Gemini
Grok
57%
36%
14%
5%
−200 0 200 400 600
Net profit (virtual $)
Claude
ChatGPT
Gemini
Grok
-108
-167
+156
-38
+433
-112
+586
+64
with market
against market
Fading the market loses for every agent
Figure 4: Against-the-market analysis. Top: share of each
agent’s bets that fade the market favourite. Bottom: net profit
from market-conforming vs. contrarian bets. Fading the mar-
ket loses money for all four agents.
0 25% 50% 75% 100%
Share of pre-match forecasts citing the factor
fatigue · rest
head-to-head
home · altitude
experience · motivation
variance · penalties
FIFA ranking
injuries · susp.
star player
form · momentum
squad depth · quality
defensive organisation
attacking threat
market / odds
Gemini barely cites the
market (12%); Claude
always does (100%)
Factor citation rate in pre-match reasoning
Claude
ChatGPT
Gemini
Grok
Figure 5: Share of pre-match forecasts citing each factor, per
agent (dumbbell: one marker per agent). Market/odds citation
ranges from 12% to 100%.
8 Using WC2026-Agents
The release supports several lines of work out of the box, each
a single join on the tidy 104-match table.(i) Calibration and
uncertainty.416 forecasts with confidences and outcomes, plus
a market reference, form a contamination-free testbed for LLM
(mis)calibration and confidence elicitation [ 27, 35].(ii) Agentic
decision-making.Paired probabilities, stakes, and real odds let
researchers score arbitrary staking policies (flat, Kelly, learned)
and quantify the value of following versus fading a price — a de-
cision layer absent from prediction-only benchmarks [ 15].(iii)
Self-knowledge.414 paired reflections let one test whether mod-
els know when they were wrong [13, 14] and whether self-reports

FIFA World Cup 2026 as a Contamination-Free Benchmark for LLM Forecasting Agents: Four Models, a Bookmaker, and 104 Matches
40% 50% 60% 70% 80%
Mean consensus probability on the favorite (all 4 models)
Australia 1–1 Egypt
USA 1–4 Belgium
Switzerland 0–0 Colombia
France 0–2 Spain
Netherlands 1–1 Morocco
France 4–6 England
Brazil 1–2 Norway
Germany 1–1 Paraguay
37% on Egypt
38% on USA
42% on Colombia
42% on France
48% on Netherlands
48% on France
53% on Brazil
75% on Germany
coin flip
Matches mispredicted by all four agents
lost on penalties (90' draw)
lost in regulation
Figure 6: The eight matches mispredicted by all four agents. Every agent backed the favourite; four ties were lost on penalties
after a 90-minute draw.
0 25% 50% 75% 100%
Share of the model's own wrong picks
Claude
ChatGPT
Gemini
Grok
49% 6%
36% 9%
86% 11%
61% 3%
Self-assessment on the agent's own wrong picks
owns it ("incorrect") "partially correct" denies ("correct")
Figure 7: Self-assessment on each agent’s own wrong picks.
Owning error (“incorrect”) ranges from 36% to 86% across
agents.
predict error, using ouroutcome_vs_predictionlabels against re-
alized correctness.(iv) Reasoning and evidence use.Verbatim
reasoning with cited URLs supports factor-attribution and source-
use studies via the released lexicon.(v) Temporal robustness and
longitudinal tracking.Because every target post-dates training,
the data probes genuine forecasting rather than recall; the thin
search–act–reflect protocol re-runs on any future tournament, en-
abling live, rolling evaluation of successive model releases against
a moving, uncontaminated target.
9 Ethics
All betting in this study is virtual; the dataset is a measurement
instrument, not gambling advice, and we report profit only to score
decision quality. No human subjects or personal data are involved:
the records are model outputs and public fixtures, scores, and odds.
Odds come from public preview articles with source URLs; we take
no book’s proprietary feed. A foreseeable misuse — treating any
agent’s edge as an actionable betting strategy — is unsupported
by our data, which show no agent beats the market. We disclose
that generative AI assisted the parsing and drafting of this work;
all findings were verified against the released data by the authors.
10 Limitations
This is a single tournament (104 matches); per-agent differences
have wide intervals and we stress patterns over precise rank-
ings. Agents were queried through consumer interfaces with tools
enabled, so retrieval and decoding are not fully controlled and
providers may update models mid-window — we hold the user-
visible model fixed and record it. Odds are opening lines from
mostly one book, not closing consensus. Reflections are the model’s
own free text, coded by a transparent but lexical scheme. These
are the natural costs of measuring deployed agents on real, un-
repeatable events, and the released pipeline makes every choice
auditable.
11 Conclusion
WC2026-Agents turns a future World Cup into a contamination-free
benchmark of LLMs as forecasting agents, paired with the betting
market as a fifth, economically grounded competitor. Its reference
evaluation shows that frontier agents predict alike and cannot beat
the market, yet diverge sharply in calibration, betting discipline,
and the honesty of their self-reflection — the axes on which they
actually differ. We release the data, odds, and evaluation suite to
support live, rolling evaluation of agentic forecasting.
References
[1] Giovanni Angelini and Luca De Angelis. 2019. Efficiency of online football
betting markets.International Journal of Forecasting35, 2 (2019), 712–721.

Ding, Guo, and Xu
[2] Anthropic. 2026. Claude Opus 4.8. https://www.anthropic.com/claude.
[3] Rahul Baboota and Harleen Kaur. 2019. Predictive analysis and modelling football
results using machine learning approach for English Premier League.Interna-
tional Journal of Forecasting35, 2 (2019), 741–755.
[4] Glenn W. Brier. 1950. Verification of forecasts expressed in terms of probability.
Monthly Weather Review78, 1 (1950), 1–3.
[5] Anthony C. Constantinou, Norman E. Fenton, and Martin Neil. 2012. pi-football:
A Bayesian network model for forecasting Association Football match outcomes.
Knowledge-Based Systems36 (2012), 322–339.
[6] Berkeley J. Dietvorst, Joseph P. Simmons, and Cade Massey. 2015. Algorithm
aversion: People erroneously avoid algorithms after seeing them err.Journal of
Experimental Psychology: General144, 1 (2015), 114–126.
[7] Eugene F. Fama. 1970. Efficient capital markets: A review of theory and empirical
work.The Journal of Finance25, 2 (1970), 383–417.
[8] Shahriar Golchin and Mihai Surdeanu. 2024. Time travel in LLMs: Tracing data
contamination in large language models. InInternational Conference on Learning
Representations (ICLR).
[9] Google DeepMind. 2026. Gemini 3.1 Pro model card. https://deepmind.google/
models/model-cards/gemini-3-1-pro/.
[10] Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q. Weinberger. 2017. On calibration
of modern neural networks. InInternational Conference on Machine Learning
(ICML). 1321–1330.
[11] Danny Halawi, Fred Zhang, Chen Yueh-Han, and Jacob Steinhardt. 2024. Ap-
proaching human-level forecasting with language models.arXiv preprint
arXiv:2402.18563(2024).
[12] Dan Hendrycks, Collin Burns, Steven Basart, et al . 2021. Measuring massive
multitask language understanding. InInternational Conference on Learning Rep-
resentations (ICLR).
[13] Jie Huang, Xinyun Chen, Swaroop Mishra, et al . 2024. Large language mod-
els cannot self-correct reasoning yet. InInternational Conference on Learning
Representations (ICLR).
[14] Saurav Kadavath, Tom Conerly, Amanda Askell, et al. 2022. Language models
(mostly) know what they know.arXiv preprint arXiv:2207.05221(2022).
[15] Ezra Karger, Houtan Bastani, Chen Yueh-Han, et al . 2024. ForecastBench: A
dynamic benchmark of AI forecasting capabilities.arXiv preprint arXiv:2409.19839
(2024).
[16] Steven D. Levitt. 2004. Why are gambling markets organised so differently from
financial markets?The Economic Journal114, 495 (2004), 223–246.
[17] Percy Liang, Rishi Bommasani, Tony Lee, et al . 2023. Holistic evaluation of
language models.Transactions on Machine Learning Research (TMLR)(2023).
[18] Aman Madaan, Niket Tandon, Prakhar Gupta, et al. 2023. Self-Refine: Iterative
refinement with self-feedback. InAdvances in Neural Information Processing
Systems (NeurIPS).
[19] Don A. Moore and Paul J. Healy. 2008. The trouble with overconfidence.Psycho-
logical Review115, 2 (2008), 502–517.
[20] Mahdi Pakdaman Naeini, Gregory F. Cooper, and Milos Hauskrecht. 2015. Ob-
taining well calibrated probabilities using Bayesian binning. InAAAI Conference
on Artificial Intelligence.
[21] OpenAI. 2026. GPT-5.5. https://openai.com/index/gpt-5-5-instant/.
[22] Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, et al. 2023. Generative agents:
Interactive simulacra of human behavior. InACM Symposium on User Interface
Software and Technology (UIST).
[23] Philipp Schoenegger, Indre Tuminauskaite, Peter S. Park, and Philip E. Tetlock.
2024. Wisdom of the silicon crowd: LLM ensemble prediction capabilities rival
human crowd accuracy.Science Advances10, 45 (2024).
[24] Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and
Shunyu Yao. 2023. Reflexion: Language agents with verbal reinforcement learn-
ing. InAdvances in Neural Information Processing Systems (NeurIPS).
[25] Erik Snowberg and Justin Wolfers. 2010. Explaining the favorite–long shot bias:
Is it risk-love or misperceptions?Journal of Political Economy118, 4 (2010),
723–746.
[26] Philip E. Tetlock and Dan Gardner. 2015.Superforecasting: The Art and Science of
Prediction. Crown.
[27] Katherine Tian, Eric Mitchell, Allan Zhou, et al. 2023. Just ask for calibration:
Strategies for eliciting calibrated confidence scores from language models. In
Empirical Methods in Natural Language Processing (EMNLP).
[28] Erik Štrumbelj. 2014. On determining probability forecasts from betting odds.
International Journal of Forecasting30, 4 (2014), 934–943.
[29] Lei Wang, Chen Ma, Xueyang Feng, et al . 2024. A survey on large language
model based autonomous agents.Frontiers of Computer Science18, 6 (2024).
[30] Jason Wei, Xuezhi Wang, Dale Schuurmans, et al. 2022. Chain-of-thought prompt-
ing elicits reasoning in large language models. InAdvances in Neural Information
Processing Systems (NeurIPS).
[31] Justin Wolfers and Eric Zitzewitz. 2004. Prediction markets.Journal of Economic
Perspectives18, 2 (2004), 107–126.
[32] Fabian Wunderlich and Daniel Memmert. 2018. The betting odds rating system:
Using soccer forecasts to forecast soccer.PLOS ONE13, 6 (2018), e0198668.
[33] xAI. 2026. Grok Expert Mode. https://x.ai.
[34] Zhiheng Xi, Wenxiang Chen, Xin Guo, et al. 2023. The rise and potential of large
language model based agents: A survey.arXiv preprint arXiv:2309.07864(2023).
[35] Miao Xiong, Zhiyuan Hu, Xinyang Lu, et al . 2024. Can LLMs express their
uncertainty? An empirical evaluation of confidence elicitation. InInternational
Conference on Learning Representations (ICLR).
[36] Shunyu Yao, Jeffrey Zhao, Dian Yu, et al. 2023. ReAct: Synergizing reasoning and
acting in language models. InInternational Conference on Learning Representations
(ICLR).
[37] Andy Zou, Tristan Xiao, Ryan Jia, et al. 2022. Forecasting future world events
with neural networks. InAdvances in Neural Information Processing Systems
(NeurIPS).
A Reproducibility
One command (python src/run_all.py ) rebuilds every processed
table, analysis CSV, and figure from the raw transcripts and odds;
the paper’s numbers are read directly from those outputs. The repos-
itory documents the schema, the 13-category reasoning lexicon,
per-match ground truth with penalty and advancement fields, and
all parse-issue flags. Randomness is not used in evaluation. The
four-way score cross-check and the odds/citation validation are
part of the build and re-run on every invocation.
B Per-stage metrics and calibration curves
0.4 0.6 0.8 1.0
0.4
0.6
0.8
1.0Empirical accuracy
Claude
ECE=0.116
0.4 0.6 0.8 1.0
0.4
0.6
0.8
1.0
ChatGPT
ECE=0.111
0.4 0.6 0.8 1.0
Mean predicted confidence
0.4
0.6
0.8
1.0Empirical accuracy
Gemini
ECE=0.068
0.4 0.6 0.8 1.0
Mean predicted confidence
0.4
0.6
0.8
1.0
Grok
ECE=0.097
Reliability of the top pick — colour = agent, grey = market (all under-confident)
Figure 8: Reliability of each agent’s top pick (App.). All lie
in the shaded (under-confident) region; marker area ∝ bin
count. ECE values also appear in Table 2.
Table 4 breaks T1 down by phase. Knockout matches are markedly
more predictable for every competitor (accuracy .719vs. ∼. 65;
lower Brier), because seeding concentrates mismatches; the four
agents are again indistinguishable within each phase, and the mar-
ket again leads on Brier. The full 13×4 factor table, the reliabil-
ity bins behind Fig. 8, the contrarian breakdown behind Fig. 4,

FIFA World Cup 2026 as a Contamination-Free Benchmark for LLM Forecasting Agents: Four Models, a Bookmaker, and 104 Matches
and the match-level upset details are released as CSVs under
data/analysis/and regenerated bysrc/run_all.py.
Table 4: Task T1 by phase (accuracy / Brier / log-loss). Group
(𝑛=72) and knockout (𝑛=32).
Group Knockout
Acc Brier LogL Acc Brier LogL
Claude .639 .489 .828 .719 .428 .756
ChatGPT .667 .493 .838 .719 .429 .759
Gemini .625 .485 .820 .719 .477 .822
Grok .667 .491 .826 .719 .425 .752
Market .667 .486 .827 .719 .431 .761
