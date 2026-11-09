---
title: 'StakeBench: Evaluating Language Understanding Grounded in Market Commitment'
url: https://arxiv.org/abs/2605.26074
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Yunhua Pei
- Jingyu Hu
- Yiwei Shi
- Hongnan Ma
- Weiru Liu
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.26074
pages: 21
chars: 71781
fetched_at: '2026-11-08T12:58:47+00:00'
kb_version: 1
---

# StakeBench: Evaluating Language Understanding Grounded in Market Commitment

StakeBench: Evaluating Language Understanding
Grounded in Market Commitment
Yunhua Pei∗ Jingyu Hu Yiwei Shi Hongnan Ma Weiru Liu John Cartlidge
University of Bristol, Bristol, UK
{ge22472,jingyu.hu,yiwei.shi}@bristol.ac.uk
{hongnan.ma,weiru.liu,john.cartlidge}@bristol.ac.uk
Abstract
Existing financial NLP benchmarks often rely on labels supplied by outside ob-
servers, measuring how language is perceived rather than what speakers have
committed to in the market. We introduceStakeBench, an evaluation framework
for language understanding grounded in market commitment. StakeBench links
560,876 comments from 2,261 resolved markets to verified position, action, and
market-odds records across Polymarket and Manifold. Supervision is derived from
observable market behavior. Position sides, post-comment trading actions, and
market-odds trajectories replace human annotation. Four diagnostic tasks test
whether models detect market commitment, identify the revealed side, anticipate
future action, and perform collective odds projection. Three commitment-aware
metrics measure alignment with revealed preferences rather than perceived sen-
timent. Validity audits and explicit interpretation boundaries help distinguish
observable commitment signals from latent belief and causal market-odds impact.
Across 15 LLMs and 18 topics and platform settings, models partially recover
position-side signals, with Directed Accuracy from 0.506 to 0.599, but show struc-
tural failures on later tasks. Ten of the fifteen models collapse to one or two action
labels in future action anticipation, and no model consistently improves on the
naive odds-direction baseline in collective odds projection. Model scale is not
correlated with performance, finance-domain tuning does not improve revealed-
side identification, and platform incentives strongly shape higher-order results.
StakeBench is packaged with evaluation code and dataset under CC-BY 4.0.
1 Introduction
Large language models (LLMs) have shown strong potential for financial text analysis, forecasting,
and decision-making [28, 26]. However, language in financial markets is not merely descriptive. Mar-
ket participants often communicate while holding positions, facing reputational costs, or attempting
to influence others’ beliefs. This makes financial language intrinsically strategic: the same statement
can carry different implications depending on what the speaker has at stake. For example, online
discussions were tightly associated with the GameStop short squeeze in 2021, while social-platform
coordination has been linked to rapid pump-and-dump movements in cryptocurrency markets [3, 15].
These cases suggest a central challenge for financial NLP: understanding market language requires
reasoning not only about what is said, but also about what the speaker has observably committed to.
Existing financial NLP resources cover text-level tasks from sentiment analysis and stance detection
to question answering and outcome forecasting [28, 26, 25, 29, 16], yet their supervision is defined
by task labels, benchmark annotations, or downstream outcomes rather than speaker commitment.
FinBen [26] and PIXIU [25] together cover broad financial NLP task suites, and Zhang et al. [29]
∗Corresponding author:ge22472@bristol.ac.uk
Preprint.
arXiv:2605.26074v1  [cs.CL]  25 May 2026

Pei et al. StakeBench: Evaluating Market-Grounded Language Understanding
Figure 1: StakeBench overview. Comments from Polymarket and Manifold are linked to position,
action, and market-odds records for four grounding tasks: market commitment detection, revealed-
side identification, future action anticipation, and collective odds projection.
extend sentiment evaluation across 26 datasets, but these targets still describe how text is classified
rather than what the speaker demonstrably chose in the market. SemEval-2016 Task 6 [16] defines
tweet-target stance classification with three labels (FA VOR/AGAINST/NEITHER), where systems
infer whether a tweet supports or opposes a specified target. This label structure is closest to
StakeBench, but the data consists of crowdsourced tweets rather than comments linked to verifiable
financial positions. Social-media analyses of investment communities [6, 3] analyze Reddit sentiment
and investment advice without linking individual posts to their authors’ actual market positions or
subsequent trading actions. On the prediction-market side, Autocast [ 30], Halawi et al. [11], and
ForecastBench [14] benchmark LLM forecasting calibration on resolved outcomes, targeting event
resolution rather than the commitment signals embedded in individual comments, while Turtel et al.
[24] use prediction-market-style forecasting data for model self-improvement but do not evaluate
comment text. No benchmark jointly connects a speaker’s language to their verified financial position,
subsequent trading behavior, and the collective market-odds signals their speech may anticipate.
To bridge this gap, we introduceStakeBench, an evaluation framework for commitment-grounded
language understanding in prediction markets. The key idea is to replace perception-based supervision
with revealed-preference signals derived from observable market commitments [ 20]. Prediction
markets provide a natural testbed because comments, positions, trading actions, resolutions, and
market-odds trajectories can be jointly observed. StakeBench contains 560,876 comments from 2,261
resolved markets across Polymarket and Manifold platforms. This dual-platform design captures
complementary incentive regimes: Polymarket offers stronger monetary commitment signals, while
Manifold provides broader position coverage and direct resolution metadata. Because these targets
are behavioral proxies, StakeBench evaluates whether models recover observable commitments rather
than private beliefs or causal effects of language on market odds. Full related works, see Appendix A.
StakeBench is organized as a progressive diagnostic suite with four grounding tasks, denoted G1–G4.
The four tasks pair technical names with plain-language questions: G1: Market Commitment
Detection (Who Holds a Position?)asks whether a given comment is written by a user who holds
any observable position in the corresponding market. G2: Revealed-Side Identification (Which
Side Is Revealed?)asks which market side the commenter’s revealed position supports. G3: Future
Action Anticipation (What Action Follows?)asks how the user will update the position after
commenting. G4: Collective Odds Projection (Where Do Aggregate Odds Move?)moves to
the collective level, testing whether aggregated commitment-aware comment signals project the
next-window market odds direction. The four tasks form an increasingly demanding hierarchy:
detecting whether a comment reflects market commitment, identifying the revealed side, anticipating
the user’s subsequent action, and projecting whether collective committed speech leads future odds
movement.
In summary, our main contributions are: 1) We introduceStakeBench, a dual-platform prediction-
market evaluation framework with 560,876 comments from 2,261 resolved markets, linking language
to speaker positions, later actions, and market-odds histories. 2) We derive task targets from public
position records, post-comment trading behavior, market resolutions, and market-odds trajectories,
replacing perception-based labels with observable commitment signals. 3) We define four progressive
diagnostic tasks covering market commitment detection, revealed-side identification, future action
2

Pei et al. StakeBench: Evaluating Market-Grounded Language Understanding
anticipation, and collective odds projection, enabling evaluation beyond text-only sentiment or
stance classification. 4) We provide commitment-aware metrics, validity audits, and documented
interpretation boundaries that support reusable evaluation of current and future models.
2 StakeBench
The aim of StakeBench is to link prediction-market comments to each author’s verified position
record across resolved markets, creating four annotation-free evaluation tasks spanning the language-
position-action-odds chain. Specifically, StakeBench contains a total of 560,876 comments across
2,261 resolved-market records with 18 topic–platform combinations collected from two public
prediction-market platforms:Polymarket 2, a real-money market whose comments provide monetary
commitment signals, andManifold 3, a virtual-Mana market with denser position coverage and
direct resolved-outcome metadata. For Polymarket, we retrieve comment threads via the Gamma
application programming interface (API) and reconstruct each commenter’s position at comment
time by replaying their trade history against the activity API to compute position_side (YES/NO)
and position_size. For Manifold, positions are reconstructed from per-user bet records. G3
additionally uses 862,540 Polymarket and 387,263 Manifold timestamped position-change records.
Markets and comments pass quality thresholds. All data are retrieved from public APIs without
authentication. Table 1 summarizes key statistics. Full API endpoints, collection funnel, and filtering
parameters appear in Appendix E. The details of topics can be found in Appendix E. Ethics and
licensing are in Appendix H. The resulting labels are deterministic reconstructions from public
records, but they remain behavioral proxies. G1 uses on-chain and API position records to assign
a binary label indicating whether the commenter held a financial stake at comment time. This
is the most directly verifiable label, as it requires no inference beyond record presence. G2 uses
revealed position side as the target, not an unobserved mental state. G3 depends on linking comments
to subsequent position changes, which is cleaner on Manifold than on Polymarket. G4 evaluates
incremental collective odds-direction signal above a commitment-weighted baseline, not a causal
effect of comments on market odds.
Table 1: Platform statistics for the two prediction-market sources used in StakeBench.
Corpus Comment activity Commitment labels Market-level signal
Platform Cleaned comments Markets Users Date range Median length Median comments / market Position coverage G1/G2 instances G3 instances G4 windows Resolution source
Polymarket514,314 2,070 24,909 May 2024– Mar 2026 44 70 27.2% 139,848 73,893 603 Price-inferred ≥0.90
Manifold46,562 191 3,250 Jan 2022– Mar 2026 107 163 80.5% 37,430 27,116 789 Direct API field
Label reconstruction and interpretation boundary.The key design choice in StakeBench is to
keep supervision tied to observable market records rather than to post-hoc text annotation. For
Polymarket, we reconstruct position side by replaying public activity records around each comment
time; for Manifold, we aggregate per-user bet histories from the public API. These labels should be
read as revealed commitment signals, not as direct measurements of private belief: G2 asks whether
language reveals the side a user had taken, G3 asks whether later observable position changes can
be anticipated, and G4 tests residual odds-direction signal beyond a commitment-weighted baseline
rather than causal price impact.
2.1 Notation
Table 2 summarizes the variables used by the four tasks. We use i for a comment instance. qi is the
corresponding market question and xi is the comment text. For G1, yi ∈ {0,1}indicates whether the
comment author has any reconstructed position at comment time, with 1 mapped to YES and 0 to NO.
For G2, zi ∈ {YES,NO}is the revealed side of that position for positioned comments. si ≥0 is the
reconstructed stake magnitude of the position, measured in USD for Polymarket and platform Mana
2https://polymarket.com
3https://manifold.markets
3

Pei et al. StakeBench: Evaluating Market-Grounded Language Understanding
for Manifold; it is supplied toG3 and used by Commitment-Calibrated Accuracy (CCA), Costly Signal
Delta (CSD), and the G4 stake-weighted baseline. For G3, ai ∈ {flip,increase,decrease,hold}is
the first net position action observed within the 48-hour post-comment window: flip switches to
the opposite side, increase grows exposure on the current side, decrease shrinks exposure on the
current side, and hold means no qualifying update is observed. For G4, w∈ Windexes an evaluated
aggregation window for a single market question after the horizon and near-tie filters. Iw is the set
of positioned comment instances in that window. p0 w is the mean YES price for the same market
during the comment window; the superscript0marks this pre-horizon reference window.hdenotes
the prediction horizon, and ph w is the mean YES price in the subsequent price window at horizon h.
The target direction is dw = dir(ph w −p 0 w)∈ {UP,DOWN}, with near-zero moves filtered out as
described in Section 4. Let b(YES) = +1 and b(NO) =−1 . The stake-weighted baseline direction
is ˜dw = dir P i∈Iw sib(zi)  , and ˜d={ ˜dw}w∈W denotes the corresponding baseline sequence.
Model predictions use hats on the corresponding targets: ˆyi, ˆzi, ˆai, and ˆdw; for G4, ˆd={ ˆdw}w∈W
is the model’s prediction sequence. For tasks with an abstention option, ⊥ denotes the NEUTRAL
output in Table 2. Metric notation in the table is as follows: Acc and F1 are standard accuracy and F1;
Accstrict is strict G2 accuracy; DA is Directed Accuracy; CCA and CSD are the commitment-aware
G2 metrics defined in Section 3.1; Accact, Accf , and Accd are the G3 four-class and binary-slice
accuracies; PLA is G4 direction accuracy, ∆PLA is its advantage over ˜d, and n+ counts evaluated
splits with ∆PLA >0 ; and Commitment Gap (CG), Mean Commitment Gap (MCG), and the
cross-task Agg score are defined in Section 3 and Section 4. In the protocol column, “binomial
sig.” denotes one-sided binomial significance testing against the task’s chance baseline, “baseline ˜d”
denotes the G4 stake-weighted odds-direction reference sequence, and “descriptive” indicates that G4
Probability-Lead Accuracy (PLA) andn + are reported without a per-split significance threshold.
Table 2: Task definitions and metric families.
Task setup Metrics
Task Specific task Input Prediction Target Target resolution Direct score Protocol
G1
Who Holds
a Position? qi, xi ˆyi yi
0/NO: no position
1/YES: position exists Acc, F1 binomial sig.
G2
Which Side
Is Revealed? qi, xi ˆzi zi
YES/NO: target side
NEUTRAL: abstain output
Accstrict, DA
CCA, CSD
binomial sig.
CG/MCG
G3
What Action
Follows? qi, xi, zi, si ˆai ai
flip, increase,
decrease, hold
post-comment action
Accact,
Accf ,Acc d
binomial sig.
CG/MCG
G4
Where Do
Aggregate
Odds Move?
p0 w,I w ˆdw dw
UP/DOWN: target move
NEUTRAL: abstain output
near-ties filtered
PLA,
∆PLA,n +
baseline ˜d
CG/MCG
descriptive
2.2 Task Definitions
G1: Market Commitment Detection.This task tests whether a model can recognize financially
committed speech before downstream inference conditions on position.
G2: Revealed-Side Identification.This task tests whether a model can infer the side supported
by a positioned commenter’s revealed market commitment. Revealed side is a behavioral proxy,
not a direct observation of private belief. Strict accuracy counts abstention as incorrect on position-
labeled examples, while DA conditions on non-abstaining predictions. Here 1[·] denotes the indicator
function: DA =
P
i:ˆzi ̸=⊥ 1[ˆzi=zi]
|{i:ˆzi̸=⊥}| . If a model produces no directional prediction for a split, DA is
undefined for that split and the split is excluded from the corresponding macro average.
G3: Future Action Anticipation.This task tests whether a model can anticipate how a positioned
commenter will change their exposure after speaking. It uses the action labels defined in Section 2.1.
Thus G3 uses a per-comment action window, while G4 uses market-level aggregation and price
windows. Accact is the four-class action accuracy. The two binary slices are Accf for flip-vs-hold
and Accd for decrease-vs-hold; each slice is evaluated on examples whose true action belongs to the
named pair.
G4: Collective Odds Projection.This task tests whether aggregated comment signals add odds-
direction signal beyond the revealed position distribution. Using the window notation from
4

Pei et al. StakeBench: Evaluating Market-Grounded Language Understanding
Section 2.1, we score the target odds move against the model’s predicted direction. The base-
line asks whether a model adds signal beyond the revealed position distribution already present
in the market. We use PLA and its advantage over the baseline as the evaluation metrics:
PLA( ˆd) = 1 |W| P w∈W 1[ ˆdw=dw],∆ PLA = PLA( ˆd)−PLA( ˜d).
3 Evaluation Protocol
StakeBench defines a three-layer evaluation protocol: (i) a progressive task suite linking language to
position, action, and odds, (ii) commitment-aware metrics separating surface sentiment from revealed
position side, and (iii) validity audits testing the assumption that financial commitment changes
language in measurable ways. All targets are derived from public records without human annotation.
Table 2 gives the task-family overview before the detailed definitions.Supported claims.StakeBench
supports claims about commitment-based supervision, relative task difficulty, and transfer across
platform incentive regimes. It does not by itself identify causal effects of comments on market odds or
fully separate model failure from market efficiency. We therefore report validity audits and limitations
alongside benchmark scores.Reference points.StakeBench uses null baselines for classification
tasks, revealed-preference reference scores for commitment gaps, and the commitment-weighted
odds-direction baseline for G4. These reference points calibrate the strength of the observed signal
and prevent small score differences from being overread as model orderings.
3.1 Commitment-Aware Metrics
CCA and CSD.For a model M, CCA is the stake-weighted version of DA for G2, using log(1 +s i)
to limit the influence of extreme positions. CSD compares DA between the highest and lowest stake
quartiles. Let DA(k) denote DA in the k-th stake-magnitude quartile (k=1 lowest stake, k=4 highest
stake). If the set {i: ˆzi ̸=⊥} is empty or the CCA denominator is zero, CCA is undefined for
that split and excluded from macro averaging. Positive CSD is the costly-signaling prediction for
committed speech.
CCA(M) =
P
i:ˆzi̸=⊥ log(1 +s i)1[ˆzi=zi]P
i:ˆzi̸=⊥ log(1 +s i) ,CSD(M) = DA (4) −DA (1). (1)
CG and MCG.For a model M, let Oj be the task-specific revealed-preference reference score: the
score obtained from the observed market commitment baseline for task j, rather than from a text-only
model prediction. Concretely, O2 uses the stake-weighted market-majority reference, O3 uses the
realized post-comment action, and O4 uses the stake-weighted odds-direction baseline ˜d. S(M, j)is
corresponding model score for task j∈ {2,3,4} (S(M,2)=DA , S(M,3)=Acc act, S(M,4)=PLA ,
with PLA evaluated on modelM’s ˆd). G1 is excluded because it lacks a revealed-preference reference
score.
CG(M, j) =Oj −S(M, j),MCG(M) = 1 3
4X
j=2
CG(M, j).(2)
CG is signed: positive values indicate a shortfall from the revealed-preference reference score,
negative values indicate that the model exceeds it, and values closer to zero indicate closer alignment.
ForG 2, CG compares analogous but not identical targets; Appendix G defines the reference scores.
3.2 Commitment Validity Audits
G2 performance might reflect smart-money effects, self-selection, or outcome prediction rather
than language shaped by commitment. We therefore run three falsification audits alongside the
benchmark scores. These audits test specific alternative explanations rather than certifying that every
reconstructed label is noise-free. Full results in Appendix C.Wrong-Bettor Test.Letr i denote the
resolved market side for comment i. We isolate comments where zi ̸=r i (the trader held the losing
side). A model exploiting market truth predicts ri. A model reading commitment language predicts zi.
We test H0 : Pr(ˆzi=zi)=0.5 (one-sided binomial) on directional (non-abstaining) predictions only,
requiring nd≥20 per topic–platform split, where nd denotes the number of directional predictions
for the model–split pair.Position-Size Dose Response.We partition directional G2 examples
into stake-magnitude quartiles and test whether CSD is positive via one-sided Mann–Whitney with
5

Pei et al. StakeBench: Evaluating Market-Grounded Language Understanding
nd≥40 directional predictions and non-constant stake magnitudes. Here, nd is defined as above.
Within-User Difference-in-Differences (DiD).We compare the same user’s comments before and
after their first position in the same market. The DiD statistic is defined as DiD = DA+ r −DA − r . It is
post-position DA minus pre-position DA, both scored against resolution ri, where superscripts + and
− denote post-position and pre-position comments, and the subscript r indicates scoring against ri.
We treat negative DiD (language drifting away from market truth after position-taking) as a signature
of commitment bias.
4 Experimental Setup
The benchmark evaluation covers 15 large language models spanning three categories: three
closed-source models include GPT-5.5 [17], Gemini-2.5-Flash [5], and Claude-Haiku-4.5 [1]; eight
general-purpose open-weight models include Qwen3-32B, Qwen3-14B, Qwen3-30B-A3B, and
Qwen3-8B [27], Gemma2-9B [23], DeepSeek-R1-Distill-Llama-8B [10], Llama-3.2-3B-Instruct [9],
and Mistral-7B-Instruct-v0.3 [13]; The four finance-domain models include Fino1-14B (based on
Qwen2.5-14B) and Fino1-8B (based on Llama-3.1-8B) [18], Finance-Chat-7B (based on Llama-2-
7B-Chat) [4], and FinMA-30B (based on Llama-2-30B) [25]. All models are evaluated under a fixed
prompting protocol with greedy decoding (temperature 0, seed 42). Macro scores average uniformly
over the 18 topic–platform splits rather than pooling comments, preventing high-volume markets
from dominating the benchmark. G4 uses adaptive horizons in the 1–30 day range and removes
near-tie odds moves with |ph w −p 0 w| ≤0.005. Classification tasks are evaluated with one-sided
binomial tests against task-specific chance baselines, while G4 is reported descriptively relative to the
stake-weighted odds-direction baseline. Other settings are in Appendix B.
5 Results
Table 3: Main benchmark results with macro-averaged scores. Red/blue mark the best/second-best
model values.
Model G1 G2 G3 G4 Agg
Acc F1 Accstrict DA CCA CSD Accact Accf Accd PLA ∆PLA n+
Closed-source LLMs
GPT-5.5 .689 .598 .448.599 .678.048 .279.564.514.521 -.052 5 .204
Gemini-2.5-Flash .711 .666 .384 .587 .623 -.056 .278 .538 .500 .392 -.181 3 .175
Claude-Haiku-4.5 .697 .616 .381.594 .655.057 .257 .522 .510 .363 -.210 1 .138
General open-weight LLMs
Qwen3-32B.747 .711.430 .578 .606 .030 .256 .481.524.402 -.1654 .176
Qwen3-30B .670 .562 .344 .548 .609.092 .294 .575.512 .209 -.373 1 .140
Qwen3-14B.740 .703.423 .567 .621 .022 .274 .554 .493 .345 -.222 2 .173
Gemma2-9B .718 .673 .397 .578 .622 -.038 .166 .381 .513 .310 -.257 3 .152
DeepSeek-R1-8B .721 .696 .345 .514 .534 .054 .230 .434 .418 .326 -.256 2 .116
Qwen3-8B .692 .612 .325 .564 .607 .038 .168 .474 .377 .186 -.381 0 .103
Mistral-7B .534 .169 .335 .523 .552 -.050 .169 .382 .397 .267 -.300 2 .045
Llama-3.2-3B .567 .322.534.534 .535 -.008.401.395.665.159 -.408 1 .092
Finance-domain open-weight LLMs
FinMA-30B .503 .668 .476 .506 .519 .031 .164 .342 .413 .130 -.437 0 .003
Fino1-14B .648 .498 .363 .565 .608 .078 .190 .457 .415 .275 -.307 1 .096
Fino1-8B .601 .414.524.524 .573.094.162 .366 .404.560 -.0222 .072
Fin-Chat-7B .531 .169 .445 .514 .552 .003 .167 .472 .519 .433 -.1345.073
Results are organized around the claims StakeBench can support. We first report the full benchmark
scores, then analyze the position-side, action, and odds layers that reveal where current models fail.
We emphasize robust patterns, class collapse, transfer behavior, and baseline-relative signal rather
than treating small score differences as final model rankings.
Table 3 reports macro-averaged results for all 15 models. Models cover all 18 topic–platform
combinations unless explicitly noted. The reference scores are O2=0.552 for G2 (stake-weighted
market majority predicting resolution, see Appendix G), O3=1.0 for G3, and O4 Table 3 reports
G4 through PLA, ∆PLA and n+; the corresponding O4 values are reported with commitment gaps
6

Pei et al. StakeBench: Evaluating Market-Grounded Language Understanding
in Table 20. MCG spans 0.242 (GPT-5.5, lowest MCG) to 0.440 (FinMA-30B, highest MCG),
with mean MCG 0.278 for closed-source models and 0.360 for finance-domain models (Table 20).
Finance-domain models trail on speaker-level tasks, and paired open-weight comparisons show little
benefit from finance tuning (Table 13).
Figure 2: Task-chain correlations, model-family means, and scale effects. Asterisks markp<0.05.
5.1G 1: Market Commitment Detection
Eleven of fifteen models exceed G1 accuracy 0.65, with Qwen3-32B leading at 0.747 (F1 0.711).
FinMA-30B (0.503) and Mistral-7B (0.534) fall near chance, although their F1 scores differ sub-
stantially. The Polymarket–Manifold gap is negligible (δ=0.016,p=0.73; Appendix Table 12), and
cross-platform rankings are nearly identical (ρ=0.975). This indicates that committed speech carries
recognizable discourse-level markers that are stable across both platforms’ writing styles. This
near-perfect rank transfer stands in sharp contrast to G2 and G3, where platform effects are large,
marking market commitment detection as the most transferable layer of the task hierarchy.
5.2G 2: Revealed-Side Identification
G2 DA spans 0.506 to 0.599, with closed-source models averaging 0.593 and finance-domain models
0.527. The ceiling near 0.60 indicates that many position sides are not directly recoverable from
surface sentiment. GPT-5.5’s CCA = 0.678 exceeds its DA = 0.599, showing stronger signals in
higher-stake comments. Finance-domain models instead show outcome-oriented behavior: FinMA-
30B scores 0.506 against commenter side but 0.538 against market resolution, while most general
models show the opposite pattern (Table 9). G2 is also platform-sensitive (ρ=0.286 across shared-
topic platform rankings). Together, these patterns suggest that StakeBench is not merely measuring
generic financial optimism. Models must distinguish the speaker’s committed side from the market
outcome, and this distinction is where finance-domain tuning appears least reliable.
5.3G 3: Future Action Anticipation
G3 exposes a class-coverage collapse that aggregate scores conceal. Ten of fifteen models show usable
recall on only one or two action classes: some models favorflip, while others favordecrease(Table 4).
Meanholdrecall is 22.9%, even thoughholdis the largest true class (47.6%), suggesting that models
over-predict behavioral change. G3 is easier on Manifold (δ=−0.076 for Accact and δ=−0.129
forAcc f ), but this gap partly reflects a Polymarket data limitation: Polymarket’s comment API and
its position-activity API use different market identifiers, so only 14.1% of positioned comments can
be matched to a subsequent position-change record (versus 86.0% on Manifold). The Polymarket G3
pairs are therefore a non-random subset, likely biased toward high-frequency traders whose records
appear in both APIs. The platform comparison is in Appendix Table 12. Scores are stable across
6h–72h action windows (Table 7), so we retain 48h as the default horizon. This failure mode is
central to StakeBench. A model can identify a position or even infer its side while still failing to
reason about whether the speaker will flip, increase, decrease, or hold that exposure. The gap between
7

Pei et al. StakeBench: Evaluating Market-Grounded Language Understanding
Table 4: Per-class recall profile for G3. Model rows report recall by true action class; the Ground
truth row reports the true action distribution.
Type Model Flip% Increase% Decrease% Hold%
Non-degenerate
GPT-5.5 11.0 41.4 21.8 35.6
Gemini-2.5-Flash 7.0 21.1 27.1 54.6
Claude-Haiku-4.5 7.6 27.1 34.4 32.5
Qwen3-32B 24.8 22.0 11.8 36.1
Qwen3-14B 8.4 9.0 19.9 47.5
Partially degenerate
Qwen3-30B 23.9 3.4 28.9 42.1
DeepSeek-R1-8B 60.5 11.5 20.6 15.8
Llama-3.2-3B 26.9 4.6 0.0 70.8
Degenerate
FinMA-30B 1.1 0.0 97.0 0.0
Fino1-14B 5.8 4.9 84.4 5.3
Gemma2-9B 7.1 0.3 92.0 0.1
Qwen3-8B 44.3 3.2 42.7 3.3
Fino1-8B 79.1 0.0 18.4 0.0
Mistral-7B 90.2 0.0 11.2 0.0
Fin-Chat-7B 100.0 0.0 0.0 0.0
Cross-model mean 33.2 9.9 34.0 22.9
Ground truth 6.0 19.9 26.5 47.6
language interpretation and later action is therefore not a small degradation, but a change in the kind
of reasoning required.
5.4G 4: Collective Odds Projection
No model consistently exceeds the naive baseline ˜d in aggregate. All ∆PLA values are negative
(−0.022 to −0.437), showing that LLMs do not add collective odds-direction signal beyond the
commitment-weighted majority. This is a baseline-relative result, not evidence that comments lack
market-odds information. Positive gains concentrate on Manifold (27 of 32 model–split instances,
Table 14), consistent with more residual signal on the play-money platform. G4 is uncorrelated
with G1–G3 (|ρ|≤0.39), showing that speaker-level tasks and crowd-level odds projection measure
different abilities. Figure 2(a) places this separation in the task chain: G1–G2 (ρ=0.625, p=0.013)
and G2–G3-Accf (ρ=0.621, p=0.013) are significant, but the chain breaks at G4. Figure 2(c) further
shows that model size is not significantly correlated with any task score across the 3B–32B open-
weight range; we report |ρ| because the largest absolute association is small (|ρ|≤0.43, p>0.16 across
12 models). The G4 result also clarifies the role of the naive baseline. The benchmark does not ask
whether comments are correlated with future odds in isolation. It asks whether a language model can
add value after the market’s revealed position distribution has already been observed.
Table 5: Representative case studies forG 1–G4.
Task Market Comment cue Prediction Target resolution 15-model summary Insight
G1 Russia×Ukraine
ceasefire in March?
Polymarket
“I boughtwith the rules . . . illegitimate and
fraudulent. ”
GPT, Gemini, Claude:
YES
Mistral, Qwen-30B:
NO
Position exists
YES stake: $159
Target:YES/ True
8YES/ 7NO
Acc. 53.3%
First-person ownership is
masked by complaint
tone and third-person
“yes holders” framing.
G2 US recession before
end-2024?
Manifold
“10y2y treasury yield spread: it just
disinverted. ”
GPT:YES
Gemini, Claude,
FinMA:NO
Revealed side
YES stake: $1,364
Target:YES
7YES/ 7NO
1NEU
Acc. 46.7%
Correct reading needs
macro timing knowledge,
not only finance
vocabulary.
G3 Will Manifold solve
my puzzle? (Round
2)
Manifold
“Ispent 2500 mana on Noshares. ” Mistral, Qwen-30B:
flip
GPT-5.5:inc.
Claude, Gemini:
hold
48h action
NO $2,501→YES
Target:flip
5flip/ 5hold
3dec./ 2inc.
Acc. 33.3%
Past position disclosure
does not reveal whether
exposure will grow,
shrink, hold, or reverse.
G4 MicroStrategy BTC
purchase Jul. 1–7?
Polymarket
“100% will be another buy”;“99% for him
to buy more”;“buy more NO . . . free
money”.
“not gonna smash ATM”;“pump and Dump
by whales”.
DeepSeek, Claude,
Gemini:DOWN
GPT-5.5, FinMA:
NEU
Most others:UP
YES odds
0.810→0.452
stat_3c:UP
Target:DOWN
3DOWN/ 9UP
3NEU
Acc. 20.0%
The crowd sounds bullish,
but minority bearish cues
better anticipate the next
odds move.
8

Pei et al. StakeBench: Evaluating Market-Grounded Language Understanding
5.5 Diagnostic Case Studies and Platform Effects
Table 5 presents four representative task cases. The examples show that discourse context can
obscure commitment cues, domain timing can determine revealed side, position disclosure need
not imply later action, and bullish aggregate language can precede a lower next-window price.
These cases clarify the diagnostic role of StakeBench. The relevant signal is often not the surface
polarity of the comment, but its relation to an observable commitment, later action, or price-window
outcome. The same heterogeneity appears at the model-family and platform levels. Model-family
means are shown in Figure 2(b), and cross-platform breakdowns appear in Table 12 (Appendix D).
Finance-domain models trail on speaker-level metrics (mean G3-Accact 0.171 vs. 0.271 for closed-
source) despite a marginal G4 PLA advantage, suggesting that financial pretraining is associated with
outcome-oriented rather than position-side reasoning.G 1 transfers fully across platforms (δ=0.016,
ρ=0.975). G2 aggregate performance is stable but model orderings diverge (ρ=0.286). G3 transfers
at neither level (ρ≤0.207, p≤0.001). G4 model orderings are consistent (ρ=0.771). This hierarchy
(G1 generalizes, G2 partially, G3 not at all, G4 distinct) confirms that StakeBench’s dual-platform
design adds diagnostic coverage rather than redundant replication.
6 Conclusion
We present StakeBench, an evaluation framework for commitment-grounded language understanding
that links 560,876 comments from 2,261 resolved markets across Polymarket and Manifold to each
author’s verified position record, supporting four progressive diagnostic tasks and three commitment-
aware metrics grounded in revealed preferences rather than perceived sentiment. Its contribution is
an auditable evaluation protocol with explicit behavioral targets, not a new model or a final model
ranking. Our evaluation of 15 LLMs across 18 topic–platform combinations shows that models
partially recover individual commitment signals, with G2 Directed Accuracy spanning 0.506 to 0.599,
but fail on future action and collective odds tasks. G3 collapses to one or two action labels in 10 of 15
models, and no model consistently exceeds the stake-weighted majority baseline on G4. Financial
pretraining is associated with weaker speaker-level reasoning than comparable general models, model
scale is uncorrelated with performance, and most positive G4 gains occur on the play-money platform.
Validity audits test whether committed speech differs from non-committed speech in language [22, 8]
and whether models exploit commitment cues or merely outcome-prediction cues. These results
should be read as evidence about observable commitment proxies under the StakeBench protocol, not
as claims about private beliefs or causal market-odds formation. Together, these findings show that
commitment-grounded language understanding remains an open challenge for LLMs across speaker
positions, behavioral consistency, and collective odds signals, suggesting that training objectives
using position context may be more productive than domain-specific financial pretraining.
Limitations.CSD and DiD audits are underpowered on some topics. Polymarket G3 label coverage
is lower than Manifold (14.1% vs. 86.0%) because Polymarket’s comment API and position-activity
API assign different hex identifiers to the same market, preventing a direct join in 85.9% of cases.
The benchmark uses fixed prompts and LLM probes rather than trainable reference models, so it
measures evaluation behavior rather than best achievable performance. Public comments may enter
future pretraining corpora, platform incentives differ, G4 may reflect market efficiency as well as
model limits, and all data are in English.
Ethics and broader impact.All data are sourced from public APIs. User identifiers are platform
pseudonyms (proxy_wallet on Polymarket, user_id on Manifold), and no real names, IP ad-
dresses, or private messages are included. Position-holding commenters differ from non-holders on
observable dimensions with effect sizes below d=0.3 (Cohen’s d), indicating modest but non-zero
selection bias in G2 and G3 evaluation sets. The benchmark dataset, evaluation code, model outputs,
and scripts are packaged under CC-BY 4.0 to support review and reproduction. The underlying
platform data are used under Polymarket’s Terms of Use and Manifold’s Terms of Service, both
of which permit non-commercial research use. Open-weight model weights follow their respective
licenses (Meta Llama 3 Community License for Llama 3 and Apache 2.0 for Qwen3).
9

Pei et al. StakeBench: Evaluating Market-Grounded Language Understanding
Acknowledgements
This work was funded by UKRI EPSRC (grant No. EP/Y028392/1): AI for Collective Intelligence
(AI4CI).
References
[1] Anthropic. Claude Haiku 4.5 System Card. https://www-cdn.anthropic.com/
7aad69bf12627d42234e01ee7c36305dc2f6a970.pdf, 2025. Accessed: 2026-05-04.
[2] Yoav Benjamini and Yosef Hochberg. Controlling the false discovery rate: a practical and
powerful approach to multiple testing.Journal of the Royal statistical society: series B
(Methodological), 57(1):289–300, 1995.
[3] Tolga Buz and Gerard de Melo. Wallstreetbets: assessing the collective intelligence of reddit
for investment advice.ACM Transactions on Social Computing, 7(1-4):1–23, 2024.
[4] Daixuan Cheng, Shaohan Huang, and Furu Wei. Adapting large language models to domains
via reading comprehension.arXiv preprint arXiv:2309.09530, 2023.
[5] Gheorghe Comanici, Eric Bieber, Mike Schaekermann, Ice Pasupat, Noveen Sachdeva, Inderjit
Dhillon, Marcel Blistein, Ori Ram, Dan Zhang, Evan Rosen, et al. Gemini 2.5: Pushing the
frontier with advanced reasoning, multimodality, long context, and next generation agentic
capabilities.arXiv preprint arXiv:2507.06261, 2025.
[6] Xiang Deng, Vasilisa Bashlovkina, Feng Han, Simon Baumgartner, and Michael Bendersky.
Llms to the moon? reddit market sentiment analysis with large language models. InCompanion
Proceedings of the ACM Web Conference 2023, pages 1014–1019, 2023.
[7] Bradley Efron. Bootstrap methods: another look at the jackknife. InBreakthroughs in statistics:
Methodology and distribution, pages 569–593. Springer, 1992.
[8] Andrea Galeotti, Christian Ghiglino, and Francesco Squintani. Strategic information transmis-
sion networks.Journal of Economic Theory, 148(5):1751–1769, 2013.
[9] Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian,
Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. The llama
3 herd of models.arXiv preprint arXiv:2407.21783, 2024.
[10] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Peiyi Wang, Qihao Zhu, Runxin Xu,
Ruoyu Zhang, Shirong Ma, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in
llms via reinforcement learning.arXiv preprint arXiv:2501.12948, 2025.
[11] Danny Halawi, Fred Zhang, Chen Yueh-Han, and Jacob Steinhardt. Approaching human-level
forecasting with language models.Advances in Neural Information Processing Systems, 37:
50426–50468, 2024.
[12] Clayton Hutto and Eric Gilbert. Vader: A parsimonious rule-based model for sentiment analysis
of social media text. InProceedings of the international AAAI conference on web and social
media, volume 8, pages 216–225, 2014.
[13] Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh
Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile
Saulnier, Lélio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut
Lavril, Thomas Wang, Timothée Lacroix, and William El Sayed. Mistral 7b, 2023. URL
https://arxiv.org/abs/2310.06825.
[14] Ezra Karger, Houtan Bastani, Chen Yueh-Han, Zachary Jacobs, Danny Halawi, Fred Zhang, and
Philip E Tetlock. Forecastbench: A dynamic benchmark of ai forecasting capabilities.arXiv
preprint arXiv:2409.19839, 2024.
[15] Massimo La Morgia, Alessandro Mei, Francesco Sassi, and Julinda Stefa. The doge of wall
street: Analysis and detection of pump and dump cryptocurrency manipulations.ACM Transac-
tions on Internet Technology, 23(1):1–28, 2023.
10

Pei et al. StakeBench: Evaluating Market-Grounded Language Understanding
[16] Saif Mohammad, Svetlana Kiritchenko, Parinaz Sobhani, Xiaodan Zhu, and Colin Cherry.
Semeval-2016 task 6: Detecting stance in tweets. InProceedings of the 10th international
workshop on semantic evaluation (SemEval-2016), pages 31–41, 2016.
[17] OpenAI. GPT-5.5 System Card. https://openai.com/index/gpt-5-5-system-card/ ,
2026. Accessed: 2026-05-04.
[18] Lingfei Qian, Weipeng Zhou, Yan Wang, Xueqing Peng, Han Yi, Yilun Zhao, Jimin Huang,
Qianqian Xie, and Jian-yun Nie. Fino1: On the transferability of reasoning-enhanced llms and
reinforcement learning to finance.arXiv preprint arXiv:2502.08127, 2025.
[19] Hannah Rashkin, Maarten Sap, Emily Allaway, Noah A Smith, and Yejin Choi. Event2mind:
Commonsense inference on events, intents, and reactions. InProceedings of the 56th Annual
Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages
463–473, 2018.
[20] Paul A Samuelson. Consumption theory in terms of revealed preference.Economica, 15(60):
243–253, 1948.
[21] Maarten Sap, Hannah Rashkin, Derek Chen, Ronan Le Bras, and Yejin Choi. Social iqa:
Commonsense reasoning about social interactions. InProceedings of the 2019 conference on
empirical methods in natural language processing and the 9th international joint conference on
natural language processing (EMNLP-IJCNLP), pages 4463–4473, 2019.
[22] Michael Spence. Job market signaling. InUncertainty in economics, pages 281–306. Elsevier,
1978.
[23] Gemma Team, Morgane Riviere, Shreya Pathak, Pier Giuseppe Sessa, Cassidy Hardin,
Surya Bhupatiraju, Léonard Hussenot, Thomas Mesnard, Bobak Shahriari, Alexandre Ramé,
et al. Gemma 2: Improving open language models at a practical size.arXiv preprint
arXiv:2408.00118, 2024.
[24] Benjamin Turtel, Danny Franklin, and Philipp Schoenegger. Llms can teach themselves to
better predict the future.arXiv preprint arXiv:2502.05253, 2025.
[25] Qianqian Xie, Weiguang Han, Xiao Zhang, Yanzhao Lai, Min Peng, Alejandro Lopez-Lira, and
Jimin Huang. Pixiu: A comprehensive benchmark, instruction dataset and large language model
for finance.Advances in Neural Information Processing Systems, 36:33469–33484, 2023.
[26] Qianqian Xie, Weiguang Han, Zhengyu Chen, Ruoyu Xiang, Xiao Zhang, Yueru He, Mengxi
Xiao, Dong Li, Yongfu Dai, Duanyu Feng, et al. Finben: A holistic financial benchmark for
large language models.Advances in Neural Information Processing Systems, 37:95716–95743,
2024.
[27] An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu,
Chang Gao, Chengen Huang, Chenxu Lv, et al. Qwen3 technical report.arXiv preprint
arXiv:2505.09388, 2025.
[28] Yi Yang, Mark Christopher Siy Uy, and Allen Huang. Finbert: A pretrained language model for
financial communications.arXiv preprint arXiv:2006.08097, 2020.
[29] Wenxuan Zhang, Yue Deng, Bing Liu, Sinno Pan, and Lidong Bing. Sentiment analysis in the
era of large language models: A reality check. InFindings of the Association for Computational
Linguistics: NAACL 2024, pages 3881–3906, 2024.
[30] Andy Zou, Tristan Xiao, Ryan Jia, Joe Kwon, Mantas Mazeika, Richard Li, Dawn Song, Jacob
Steinhardt, Owain Evans, and Dan Hendrycks. Forecasting future world events with neural
networks.Advances in Neural Information Processing Systems, 35:27293–27305, 2022.
11

Pei et al. StakeBench: Evaluating Market-Grounded Language Understanding
A Related Work
Forecasting and prediction-market benchmarks.Recent forecasting benchmarks evaluate whether
models can assign calibrated probabilities to future events. Autocast [30] introduced large-scale event
forecasting from textual evidence, Halawi et al.[11] evaluate LLM calibration on resolved forecasting
questions, and ForecastBench [14] maintains a dynamic leaderboard for AI forecasting capabilities.
Turtel et al. [24] further use prediction-market-style forecasting data for model self-improvement.
These works ask whether models predict event outcomes. StakeBench instead asks whether models
understand what a speaker’s market comment reveals about their verified position, later action, and
collective odds-direction signal.
Financial NLP, sentiment, and stance.Financial NLP has largely focused on document- or sentence-
level labels. FinBERT [ 28] adapts language modeling to financial communications, PIXIU [ 25]
combines a benchmark, instruction dataset, and financial LLM, and FinBen [26] broadens evaluation
across financial tasks. General sentiment and stance resources, including V ADER [12], SemEval-
2016 Task 6 [16], and the multi-dataset LLM sentiment audit of Zhang et al. [29], evaluate how
text is classified by external labels. SemEval’s YES/NO/NONE formulation is structurally close to
StakeBench G2, but its labels are crowdsourced tweet stances rather than positions that speakers paid
to hold. StakeBench replaces perception-based labels with revealed-preference targets [20].
Market discourse and social-media finance.Work on retail-investor communities studies how
online language relates to market behavior. Deng et al. [6] analyze Reddit market sentiment with
LLMs, Buz and de Melo [3] study WallStreetBets investment advice, and La Morgia et al. [15]
analyze pump-and-dump manipulation in cryptocurrency communities. These studies connect public
discussion to market phenomena, but they typically operate at the post, forum, or aggregate level.
StakeBench links each comment to the author’s own contemporaneous position and post-comment
trading record, enabling instance-level tests of commitment language rather than only community-
level sentiment analysis.
Grounded intent, action, and strategic communication.NLP benchmarks for social reasoning,
such as Event2Mind [19] and Social IQa [21], test whether models can infer intents, reactions, and
likely social consequences from text, but their targets are human-authored annotations. StakeBench
G3 extends grounded intent prediction to observed post-comment market actions. The benchmark
is also connected to economic accounts of costly signaling and strategic communication: Spence’s
signaling model [22] explains why costly actions can reveal private information, while Crawford and
Sobel’s cheap-talk framework [8] shows why unsupported messages can be strategically distorted.
Prediction-market positions provide the missing costly action, allowing StakeBench to test whether
models distinguish committed speech from unsupported market talk.
B Detailed settings
Models.The model suite is used as a set of probes for the benchmark rather than as the main
contribution. The goal is to expose capability boundaries under a fixed prompting protocol, not to
exhaust model-specific prompt tuning or establish a final model ranking. All 15 models use greedy
decoding (temperature = 0, seed = 42). Three closed-source models are queried via the OpenRouter
API: GPT-5.5 [17], Gemini-2.5-Flash [5], and Claude-Haiku-4.5 [ 1]. Eight general open-weight
models are loaded from Hugging Face in float16: Qwen3-32B, Qwen3-14B, Qwen3-30B-A3B
(mixture-of-experts, MoE), and Qwen3-8B [ 27], Gemma2-9B [23], DeepSeek-R1-Distill-Llama-
8B [10], Llama-3.2-3B-Instruct [9], and Mistral-7B-Instruct-v0.3 [13]. Four finance-domain models
complete the suite: Fino1-14B (Qwen2.5-14B base) and Fino1-8B (Llama-3.1-8B base) [18], Finance-
Chat-7B (Llama-2-7B-Chat base) [4], and FinMA-30B (Llama-2-30B base) [25]. Qwen3 models
prepend the <nothink> token to suppress chain-of-thought generation and are capped at 32 output
tokens. DeepSeek-R1-8B retains its full reasoning chain (512 output tokens). All other open-weight
models are capped at 24–48 output tokens. All 15 models are evaluated on the same 18 topic–platform
splits.
Computational environment.Open-weight models are evaluated on a SLURM-managed high-
performance-computing (HPC) cluster equipped with NVIDIA GH200 GPUs (95 GB HBM3e per
device), using the Hugging Face Transformers library (Python 3.11.7, PyTorch 2.5.1, float16 preci-
sion). Most models fit on a single GH200. Qwen3-30B-A3B (MoE, ≈60 GB fp16) and FinMA-30B
12

Pei et al. StakeBench: Evaluating Market-Grounded Language Understanding
(≈60 GB fp16) use tensor parallelism (device_map="auto") across two GPUs. Per-model infer-
ence batch sizes are calibrated to the available key–value (KV) cache budget on one GH200 at a
1,500-token context. Batch sizes range from 32 prompts for Qwen3-32B (64 GB weights, ≈12 GB
KV headroom) to 384 for Llama-3.2-3B (6.4 GB weights, ≈63 GB KV headroom). Closed-source
responses are logged and parsed by the same label-extraction pipeline used for open-weight models.
Task windows and filters. G3 uses the post-comment action window defined in Section 2.1. G4 uses
an adaptive per-window horizon h∈[1,30] days. Topic–platform splits with fewer than 12 instances
are excluded, andG 4 excludes near-zero odds moves with|p h w −p 0 w| ≤0.005.
Scoring and significance.For platform comparisons, δ denotes the paired Polymarket-minus-
Manifold mean score difference over shared topics, and ρ denotes the corresponding Spearman rank
correlation of model rankings across platforms. Cross-platform breakdowns are reported in Appendix
Table 12. Macro averages weight all 18 topic–platform splits equally. Significance uses one-sided
binomial tests (α= 0.05 ) with null baselines 0.5 for G1, G2-DA, and the binary G3 slices Accf and
Accd, and 0.25 for G3-Accact. G4 PLA and n+ are reported descriptively without a significance
threshold. The aggregate score Agg rescales G1-Acc, G2-DA, and G3-Accact from their chance
baselines (0.5,0.5,0.25) toward 1, rescales n+ from 0 toward 18, clips each component below at 0,
and averages the four components equally. Plain p denotes a statistical test p-value. Spearman ρ is a
signed rank correlation, while |ρ| reports only its magnitude when the claim concerns the absence of
association regardless of direction. Bootstrap confidence interval widths [7] and Benjamini-Hochberg
false discovery rate retention [2] are reported in Appendix C.
Prompting. G1 uses a one-shot prompt requesting YES or NO. G2 requests one label from the
prediction set in Table 2 and instructs the model to infer the commenter’s revealed position side rather
than the market outcome or surface sentiment. G3 provides zi and si, then requests the four-class
action label or a binary subtask label. G4 provides p0 w, concatenates window comments, and requests
one direction label from Table 2. Full prompt templates are in Appendix F.
C Statistical Reliability and Validity Audit Details
Table 6: Statistical reliability checks. N pool + is the pooled G4 positive count, distinct from the
per-modeln + in Table 3; Ret. is the fraction of raw discoveries retained after BH-FDR correction.
Metric 95% CI Raw sig. BH-FDR Ret.
G1 Acc .033 166 154 92.8%
G2 DA .050 114 72 63.2%
G3 Accact .057 17 7 41.2%
G3 Accf .096 23 7 30.4%
G4 PLA .116 N pool + = 32/270 (∆ PLA>0)
Reliability declines as tasks move from market commitment detection to behavioral anticipation. G1
and G2 retain most discoveries after BH-FDR correction, while G3 has wider uncertainty and fewer
robust topic-level wins. Then + column in Table 3 is per-model rather than pooled.
Table 7: Action-window sensitivity. Sig. splits are model–split tests above the chance baseline.
Horizon True hold Pred. hold Mean Accact Sig. splits
6h 45.3% 22.1% .233 21
12h 45.3% 22.1% .231 18
24h 45.2% 22.6% .229 18
48h 45.1% 22.5% .231 21
72h 45.1% 22.4% .228 15
Mean accuracy varies by less than one percentage point across horizons, and the ground-truth hold
rate is nearly unchanged. The final column counts model–split tests above the chance baseline.
Full audit findings.In the Wrong-Bettor test, 25 of 116 eligible model–split pairs reach p<0.05.
OnPOLY/POLITICS_INTL, Pr(ˆzi=zi |z i̸=ri) reaches 0.71–0.81 across four models, showing
13

Pei et al. StakeBench: Evaluating Market-Grounded Language Understanding
that models track commitment language rather than market truth. In the stake-magnitude dose-
response audit, 12 of 154 eligible pairs are significant, with five concentrated onMANI/ECONOMICS
(CSD≈0.26–0.37). Evidence outside this topic is limited. The formal DiD statistic (DA+ r −DA − r ,
both scored against ri) has macro mean 0.026. As a complementary comparison, DA+ z (post-position
scored against zi) reaches 0.621 versus DA− r =0.508, indicating stronger commitment-side signal
after position-taking.
Tables 8, 10, and 11 give the full per-model breakdowns for the three audits on all 12 open-weight
models (116 eligible and 25 significant pairs for the Wrong-Bettor test; 3 significant dose-response
cases).
Table 8: Wrong-Bettor test summary. Elig. counts eligible topic–model pairs, Sig. counts significant
tests, and Mac. pct is the macro commitment-following rate.
Model Elig. Sig. >0.5 Mac. pct
Qwen3-8B 8 4 5 .584
Qwen3-32B 10 3 6 .552
Qwen3-14B 10 3 5 .535
DeepSeek-R1-8B 9 1 6 .533
Fin-Chat-7B 10 1 5 .526
Fino1-14B 8 2 4 .505
Gemma2-9B 9 3 5 .504
Mistral-7B 11 1 5 .474
Qwen3-30B 8 2 5 .472
Fino1-8B 11 3 5 .462
Llama-3.2-3B 11 0 4 .432
FinMA-30B 11 2 4 .384
Total 116 25 59 .493
In Table 8, >0.5 counts eligible model–topic pairs whose commitment-following rate is above
chance. The strongest effects come from a small set of topics rather than a uniform global shift.
Table 9: Outcome-scored side audit. Gap is resolution-scored DA minus side-scored DA.
Type Model Topics Side DA Res. DA Gap
general DeepSeek-R1-8B 18 .514 .497 −.018
general Gemma2-9B 18 .578 .567−.011
general Llama-3.2-3B 18 .534 .550+.015
general Mistral-7B 18 .523 .521−.003
general Qwen3-14B 18 .567 .531−.036
general Qwen3-30B 18 .548 .543−.004
general Qwen3-32B 18 .578 .547−.031
general Qwen3-8B 18 .564 .530−.035
finance Fin-Chat-7B 18 .514 .510 −.004
finance Fino1-14B 18 .565 .556−.009
finance Fino1-8B 18 .524 .522−.002
finance FinMA-30B 18 .506 .538+.032
FinMA-30B is the only model with a clear positive gap, suggesting that its side predictions lean
toward market outcomes rather than commenter-side language.
Table 10: Stake-magnitude dose response.
Model Topic nd CSD p DA(1) DA(2) DA(3) DA(4)
FinMA-30B mani/economics 116 .321 .017 .300 .429 .759 .621
Qwen3-30B mani/economics 75 .368 .026 .158 .579 .722 .526
Qwen3-8B mani/economics 70 .333 .044 .333 .706 .765 .667
All significant dose-response cases occur on Manifold economics. The repeated pattern suggests
that stake size can sharpen commitment language, but the evidence is topic-concentrated rather than
14

Pei et al. StakeBench: Evaluating Market-Grounded Language Understanding
universal. Here nd is the number of directional examples used in the quartile test (consistent with the
notation in Section 3).
Table 11: Within-user DiD summary. Neg./total counts topics with negative DiD.
Model Macro DiD Neg./total Pre vs.r i Post vs.z i
Fin-Chat-7B+0.075 3/12 .453 .548
FinMA-30B+0.066 4/12 .495 .547
Qwen3-30B+0.052 3/12 .470 .639
Llama-3.2-3B+0.046 5/12 .497 .560
Gemma2-9B+0.034 4/12 .523 .689
Qwen3-8B+0.020 5/12 .509 .677
Mistral-7B+0.016 6/12 .541 .675
DeepSeek-R1-8B+0.008 6/12 .495 .543
Qwen3-32B−0.030 6/12 .556 .656
Qwen3-14B−0.029 7/12 .542 .678
Mean +0.026 4.9/12 .508 .621
Macro DiD is the macro-averaged formal resolution-scored statistic ( DA+ r −DA − r ). The final
two columns show the complementary comparison DA− r and DA+ z , confirming that post-position
language aligns more strongly with the user’s own side than pre-position language aligns with the
final market outcome.
D Platform Comparison Details
In this appendix, δ denotes the Polymarket-minus-Manifold mean score difference and ρ denotes
cross-platform Spearman rank correlation.
Table 12: Cross-platform comparison.
Task δ Test stat. p Cross-rankρ
G1 +0.016 0.37 .729.975 ∗
G2-DA+0.015 0.44 .680.286
G3-Accact −0.076−7.06.001 ∗ .207
G3-Accf −0.129−7.02.001 ∗ .032
G4 (∆PLA)−0.110−1.04 .346.771 ∗
Table 12 reports δ, the paired test statistic, the test p-value, and ρ. The main platform effect is
concentrated inG 3, whileG 1 rankings transfer almost perfectly.
Table 13: Paired finance-domain comparisons.
Pair Comparison G1 G2-DA G3-Accact G3-Accf G4-PLA
14B Fino1-14B minus Qwen3-14B−.092−.002−.084−.097−.070
30B FinMA-30B minus Qwen3-32B−.245−.072−.092−.139−.272
7B Fin-Chat-7B minus Mistral-7B−.004−.009−.002+.090+.167
Entries are finance-model scores minus matched general-model scores. The paired comparisons show
that finance tuning does not improve speaker-level commitment tasks, even when model sizes are
similar.
Positive counts model–split instances where the model exceeds the naive odds-direction baseline.
Positive gains are rare on both platforms, but they are more frequent on Manifold. This supports
treating G4 as a baseline-relative test of residual signal rather than a claim that comments alone
forecast market odds.
15

Pei et al. StakeBench: Evaluating Market-Grounded Language Understanding
Table 14:G 4 platform split.
Platform Splits Positive Share PLA ∆PLA
Manifold 180 27 15.0% .312−.220
Polymarket 90 5 5.6% .352−.300
Total 270 32 11.9% .325 −.247
E Dataset Details
E.1 Data Sources and Collection Funnel
The collection design separates breadth from label density. Polymarket provides large-scale real-
money discussion, while Manifold provides cleaner binary resolution fields and much denser position
coverage. We therefore use both platforms rather than treating either as an interchangeable source.
Table 15: Data sources and collection funnel.
Panel A: public APIs
Platform Data Endpoint
Polymarket Markets / tagsgamma-api.polymarket.com/markets
Polymarket Comments + positionsgamma-api.polymarket.com/comments
Polymarket Position activitydata-api.polymarket.com/activity
Polymarket Price historyclob.polymarket.com/prices-history
Manifold Marketsapi.manifold.markets/v0/search-markets
Manifold Commentsapi.manifold.markets/v0/comments
Manifold Bets (positions)api.manifold.markets/v0/bets
Panel B: collection funnel
Stage Polymarket markets Manifold markets
Comment-crawl input 2,469 6,083
With collected comments 2,070 2,926
After comment-depth filter 2,070 191
Final 2,070 191
Panel B reports the comment-collection funnel rather than the full raw API universe. Polymarket
keeps markets with at least 10 valid comments after collection, while Manifold keeps markets with
at least 100 valid comments after cleaning. This asymmetric threshold preserves Polymarket scale
while enforcing Manifold discussion depth. It also explains why platform comparisons are reported
on shared topics rather than by pooling all markets.
E.2 Descriptive Statistics
Two dataset differences are central to StakeBench. Manifold comments are longer and more position-
covered, which makes it useful for side and action labels. Polymarket positions are real-money and
heavy-tailed, which makes it better suited for costly-signal analyses where stake magnitude matters.
E.3 Topic Difficulty
Topic difficulty is not a simple platform effect. The hardest topics include small Manifold slices and
U.S. politics on Polymarket, while several Manifold community topics are easier because comments
more directly reveal the speaker’s side. This spread motivates macro-averaging by topic–platform
split.
E.4 Filtering Criteria
Market level.Polymarket: closed markets with total volume ≥$10,000 and ≥10 valid comments
after collection. Manifold: resolved binary markets with volume ≥M$10,000, ≥50 unique bettors,
16

Pei et al. StakeBench: Evaluating Market-Grounded Language Understanding
Table 16: Dataset statistics.
Panel A: comment length (characters)
Platform p10 p25 p50 p75 p90 max
Polymarket≈1022 44 85≈1601,492
Manifold≈1849 107 230≈4709,132
Panel B: Polymarket stake-size tiers
Tier Range (USD) Count % of positioned
Retail<$10052,259 37.4%
Small $100–500 35,042 25.1%
Medium $500–1,000 14,162 10.1%
Large $1,000–5,000 23,865 17.1%
XLarge $5,000–10,000 6,315 4.5%
Whale $10,000–50,000 6,732 4.8%
Mega>$50,0001,473 1.1%
Panel C: Manifold stake-size tiers
Tier Range (M$) Count % of positioned
Retail<100 8,621 23.0%
Small 100–500 7,191 19.2%
Medium 500–1,000 3,480 9.3%
Large 1,000–5,000 7,981 21.3%
XLarge 5,000–10,000 3,008 8.0%
Whale 10,000–50,000 4,944 13.2%
Mega>50,000 2,205 5.9%
Table 17: Per-topicG 2 difficulty.
Rank Platform / Topic Mean DA Std Min Max
1 Manifold / politics_intl .419 .077 .286 .560
2 Manifold / science .464 .105 .257 .657
3 Manifold / sports_other .473 .147 .231 .722
4 Polymarket / politics_us .528 .041 .472 .654
5 Polymarket / tech_other .536 .056 .398 .615
6 Polymarket / other .544 .064 .425 .656
7 Manifold / politics_us .545 .054 .470 .653
8 Manifold / crypto .550 .091 .269 .646
9 Manifold / economics .555 .054 .467 .635
10 Polymarket / crypto .558 .092 .410 .726
11 Manifold / tech_other .560 .058 .460 .658
12 Manifold / culture .576 .059 .448 .675
13 Polymarket / economics .583 .032 .529 .632
14 Manifold / meta .588 .094 .394 .719
15 Polymarket / politics_intl .593 .047 .524 .674
16 Manifold / other .621 .045 .534 .682
17 Manifold / social .628 .050 .514 .712
18 Manifold / tech_ai .635 .047 .571 .706
and ≥100 comments after cleaning.Comment level.Length ≥30 characters after URL stripping,
English-only (ASCII ratio ≥85% with basic function-word check), and alphabetic ratio ≥30%.
Topic filtering.A keyword blacklist removes puzzle and game markets (“wordle”, “nyt crossword”,
“spelling bee”) mis-tagged under the crypto category on Manifold. All filters apply uniformly across
all tasks.
17

Pei et al. StakeBench: Evaluating Market-Grounded Language Understanding
E.5 Position Reconstruction
Position labels are reconstructed from timestamped trading records at comment time. Neither the
Polymarket nor the Manifold comment API supplies them directly.
Polymarket.For each comment author identified by proxy_wallet, we query the Polymarket
activity API ( data-api.polymarket.com/activity?user={proxy_wallet}) and replay the
full transaction sequence up to the comment timestamp. position_side isYESif net YES shares
exceed zero andNOif net NO shares exceed zero. position_size (USD) is computed as total
BUY amount minus total SELL amount over all trades in the target market prior to the comment.
A negative value indicates a realized-profit state (the user sold shares above cost but remains net
long). Weighting formulas use the nonnegative magnitude of the reconstructed stake. Requests are
parallelized with eight threads per market and use exponential backoff on HTTP 429/5xx responses.
Total wall-clock time for 2,070 markets was approximately 9.7 hours. The Polymarket comment API
returns parent_entity_type as Event (37.2% of rows) or Series (62.8%). Series markets share
comment threads across multiple related markets, creating duplicate comment_id values that must
be deduplicated before unique-comment analyses.
Manifold.For each commenter ( userId) in each market, we query
api.manifold.markets/v0/bets?contractId={id}&userId={uid} and aggregate bets
placed before the comment timestamp. position_mana (net Mana M$) is the sum of amounts
on the dominant side. The side with the higher net Mana determines position_side. Each bet
record includes a probAfter field, which is interpolated to produce prob_at_comment (market
probability at comment time, 87.9% coverage). Resolution outcomes (YES/NO) are read directly
from the market metadata API, enabling the Wrong-Bettor and reference-score analyses that require
ri (Appendices C and G). Position coverage reaches 80.5% on Manifold versus 27.2% on Polymarket,
reflecting the behavioral difference: Manifold users typically bet before or during commenting, while
many Polymarket users comment without an open position. G3 action labels additionally use 862,540
Polymarket and 387,263 Manifold timestamped position-change records to identify each user’s first
net position update in the 48-hour post-comment window.
E.6 Temporal and Category Distribution
Table 18 summarizes comment volumes over time. Polymarket activity is concentrated in late 2024
and 2025, peaking in June 2025 (123,040 comments) driven by Iran-nuclear-crisis markets. Manifold
shows a longer growth arc from 2022 onward, with peak monthly volumes of roughly 3,000 comments
in 2023. Table 19 shows the keyword-classified category breakdown. On Polymarket, 67.1% of raw
rows fall outside the five defined keyword categories (NaN/other). The deduplicated share drops to
51.6% because NaN comments are disproportionately from Series markets whose comment threads
span multiple market IDs. Politics is the largest named category on both platforms. Reply and
engagement statistics reflect the difference in platform culture: 50.4% of Polymarket comments are
replies (maximum 152 replies per thread) versus 70.9% on Manifold (maximum 78), and average
reaction counts are 1.06 versus 1.72, respectively.
Table 18: Monthly comment volumes.
Polymarket Manifold
Month Comments Period Comments/mo
2024-11 25,143 2022-01–10<500
2024-12 48,980 2023-01–12 1,350–3,089
2025-01 46,020 2024-07 2,603
2025-04 43,632 2024-11 1,456
2025-06 123,0402025-05 1,575
2025-07 53,050
The category distribution is highly skewed, especially on Polymarket where Series-level comment
pools inflate broad residual categories. Topic-level evaluation avoids letting high-volume political or
Series markets dominate the benchmark.
18

Pei et al. StakeBench: Evaluating Market-Grounded Language Understanding
Table 19: Keyword-based topic categories.
Polymarket Manifold
Category Count % Category Count %
Politics 99,858 19.4 Other 30,875 66.3
Crypto 50,508 9.8 Politics 6,252 13.4
Economics 13,486 2.6 Technology 3,759 8.1
Sports 5,500 1.1 Crypto 3,758 8.1
NaN/other 345,062 67.1 Sports 1,174 2.5
Economics 744 1.6
F Prompt Templates
Allowed output labels follow Table 2; the templates below use “allowed label” where the label
semantics are already specified in the task table.
F.1G 1: Market Commitment Detection (1-shot)
You are analyzing a prediction market comment.
Market question: "{question}"
Example:
Comment: "I’m holding YES here, confident given recent polls."
Answer: YES
Now analyze:
Comment: "{text}"
Does this comment suggest that the commenter has a financial position
in this market? Reply with exactly ONE word: YES or NO.
F.2G 2: Revealed-Side Identification
You are analyzing a prediction market comment to infer the commenter’s
revealed position side.
Market question: "{question}"
Topic: {topic}
Comment: "{text}"
Does the commenter’s language indicate a YES-side or NO-side revealed position?
- YES: bullish / pro-YES view.
- NO: bearish / pro-NO view.
- The abstention output: ambiguous or purely informational.
For crypto/financial topics:
1. Price increase = YES. Price decrease = NO.
2. "To the moon" / "mooning" = YES. "dump" / "crash" = NO.
3. Hedging language ("maybe", "could go either way") uses the abstention label.
4. Pure information without directional opinion uses the abstention label.
Reply with exactly ONE allowed label.
F.3G 3: Future Action Anticipation
You are predicting how a prediction market trader will adjust their
position after making a comment.
Market question: "{question}"
Comment: "{text}"
19

Pei et al. StakeBench: Evaluating Market-Grounded Language Understanding
Current position: {position_side} (size: ${position_size:.0f})
Predict what the trader will do within 48 hours:
- flip: switch to the opposite side
- increase: add to current position
- decrease: reduce current position
- hold: no significant change
Reply with exactly ONE word: flip, increase, decrease, or hold.
F.4G 4: Collective Odds Projection
You are analyzing prediction market comments to forecast the next-window
direction of the YES price.
Market question: "{question}"
Current YES price: {current_price:.2f}
Comments from the current window:
{comments_text}
Based on the collective committed speech in these comments, what is the
next-window direction of the YES price?
Reply with exactly ONE allowed label.
G Theoretical Framework: Commitment Gap
Spence’s job-market signaling model [22] formalizes how agents can reveal private information by
choosing a costly action. In prediction markets, holding a financial position serves as that costly
action. Samuelson’s revealed preference framework [20] treats choices, rather than statements, as
behavioral evidence of preferences. StakeBench targets exploit both properties: position_side is a
preference the trader paid to hold, making it more directly grounded than any post-hoc annotation.
Extending the task and baseline notation from Section 2.1, let µ denote a market, Iµ its set of
positioned comments (distinct from the window-level setIw used in G4), and rµ its resolved outcome
(equal to ri for all comments i∈ Iµ). Let M be the set of evaluable markets within a topic–platform
split after excluding tied stake-weighted commitment sums. The inverse mapping b−1 satisfies
b−1(+1) = YES and b−1(−1) = NO. sign(u) returns +1 for u>0, −1 for u<0, and 0 otherwise.
The reference scoresO 2, O3, O4 correspond toG 2,G 3, andG 4, as defined in Eq. 3:
O2 = 1 |M| X µ∈M 1

b−1

sign

 X
i∈Iµ
sib(zi)



 =r µ

 ,
O3 = 1.0(the reference uses the actual post-comment action),
O4 = 1 |W| X w∈W 1 h ˜dw = dir(ph w −p 0 w) i .
(3)
Empirical reference values.On the evaluated StakeBench splits, O2=0.552 (macro average over 18
topic–platform splits, ranging from 0.250 to 1.000 per split) and O3=1.000. For G4, O4=PLA( ˜d) is
computed on each model’s evaluatedG4 window set and reported in Table 20 (≈0.570 macro); values
can differ across models when their evaluated G4 window sets differ. For G4, CG(4)=O4 −PLA , so
CG(4)=−∆ PLA.
Coverage is the number of evaluated topic–platform splits; O4 is computed on the model-specific
evaluated G4 window set. MCG is dominated by G3, so models with strong G2 scores can still remain
far from the G3 reference score. Seven models have negative CG(2) (GPT-5.5, Gemini, Claude,
Qwen3-32B, Qwen3-14B, Gemma2-9B, Qwen3-8B): their G2 DA exceeds O2=0.552 because DA
scores position-side prediction while O2 measures stake-weighted market-outcome accuracy, which
is a different prediction target. The CG(3) column dominates MCG for most models because G3 is
far harder thanG 2 orG 4.
20

Pei et al. StakeBench: Evaluating Market-Grounded Language Understanding
Table 20: Commitment Gap scores with theG 4 referenceO 4.
Type Model Coverage CG(2) CG(3) O4 CG(4) MCG
closed GPT-5.5 18/18 −0.047 0.721 .573 0.052 0.242
closed Gemini-2.5-Flash 18/18−0.035 0.722 .573 0.181 0.289
closed Claude-Haiku-4.5 18/18−0.042 0.743 .573 0.210 0.304
general Qwen3-32B 18/18 −0.026 0.744 .567 0.165 0.294
general Qwen3-30B 18/18 0.004 0.706 .582 0.373 0.361
general Qwen3-14B 18/18−0.015 0.726 .567 0.222 0.311
general Gemma2-9B 18/18−0.026 0.834 .567 0.257 0.355
general DeepSeek-R1-8B 18/18 0.038 0.770 .582 0.256 0.355
general Qwen3-8B 18/18−0.012 0.832 .567 0.381 0.400
general Mistral-7B 18/18 0.029 0.831 .567 0.300 0.387
general Llama-3.2-3B 18/18 0.018 0.599 .567 0.408 0.342
finance FinMA-30B 18/18 0.046 0.836 .567 0.437 0.440
finance Fino1-14B 18/18−0.013 0.810 .582 0.307 0.368
finance Fino1-8B 18/18 0.028 0.838 .582 0.022 0.296
finance Fin-Chat-7B 18/18 0.038 0.833 .567 0.134 0.335
H Ethics, Bias, and Licensing
Coverage bias.We test whether position-holding commenters differ from non-holders on five
dimensions using two-sided Mann-Whitney U tests with Cohen’s d: comment length (d=0.12), user
activity (d=0.18), market volume (d=0.09), time-to-resolution (d=0.07), and topic distribution (χ2
test, p=0.31). Effect sizes are below d=0.3 in all continuous dimensions, indicating modest but
non-zero selection bias.
Privacy.All data are from public APIs. User identifiers are platform pseudonyms ( proxy_wallet
on Polymarket and user_id on Manifold). On-chain wallet addresses are public by blockchain
design. No IP addresses, real names, or private messages are included.
Licensing.Dataset: CC-BY 4.0. Data derived from Polymarket (Terms of Use: https:
//polymarket.com/terms-of-use ) and Manifold (Terms of Service: https://manifold.
markets/terms), both permitting non-commercial research use of public data. Llama 3 weights:
Meta Llama 3 Community License. Qwen3 weights: Apache 2.0.
21
