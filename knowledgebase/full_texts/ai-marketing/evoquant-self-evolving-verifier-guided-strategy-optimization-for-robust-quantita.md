---
title: 'EVOQUANT: Self-Evolving Verifier-Guided Strategy Optimization for Robust Quantitative Trading'
url: https://arxiv.org/abs/2607.12455
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Jie Mao
- Changlun Li
- Xiang Li
- Qiqi Duan
- Jinhui Yuan
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.12455
pages: 13
chars: 51093
fetched_at: '2026-11-08T13:22:51+00:00'
kb_version: 1
---

# EVOQUANT: Self-Evolving Verifier-Guided Strategy Optimization for Robust Quantitative Trading

EVOQUANT: Self-Evolving Verifier-Guided Strategy Optimization
for Robust Quantitative Trading
Jie Mao1,∗, Changlun Li1,2,∗, Xiang Li1, Qiqi Duan2, Jinhui Yuan1, Xiang Liu1,
Yuyu Luo1,2,Jing Tang 1,Xiaowen Chu 1
1The Hong Kong University of Science and Technology (Guangzhou)
2Paradoox AI Research
∗Equal contribution. Correspondence:research@paradoox.ai
Abstract
Quantitative strategy optimization remains
largely manual, requiring domain experts
to identify weak signals, tune risk-control
rules, and repeatedly validate iterative revi-
sions. Large language models can acceler-
ate this process, but directly relying on them
to rewrite trading strategies often introduces
hallucinated edits, strategy drift, and back-
test overfitting. We proposeEVOQUANT, a
self-EvolvingVerifier-guided framework for
strategyOptimization inQuantitative trading.
Our method utilize LLMs to deeply diagnoses
performance bottlenecks, generates semanti-
cally controlled candidate edits, selects the
best strategy through a multi-stage verifica-
tion pipeline, and distills optimization expe-
rience into reusable knowledge for continual
self-improvement. We evaluate our method us-
ing seven representative strategies: four from
the A-share market and three from the Crypto
market. Experimental results show that our
method significantly improves the Sharpe ra-
tio across all tested strategies: the average test
Sharpe increases from −0.298 to 0.538, and
the best-performing strategy achieves a 199%
relative improvement. Ablation studies and
stress tests under stricter conditions further val-
idate the effectiveness and robustness of the
framework. Overall, this work transforms quan-
titative strategy optimization from costly man-
ual trial-and-error into an automated and veri-
fiable iterative paradigm, offering a new path
for applying large language models to financial
strategy research.
1 Introduction
Quantitative strategy development is fundamentally
an iterative scientific process: researchers propose
a testable market hypothesis, implement a trad-
ing rule, validate its performance through rigor-
ous backtesting, diagnose failure modes, revise
the hypothesis, and repeat this cycle continuously
to adapt to non-stationary market regimes (Noor-
MohammadzadehMaleki et al., 2026; Zhou et al.,
2025; Li et al., 2025a, 2026). As summarized
in Figure 1(a), traditional manual optimization of
quantitative strategies is constrained by scarce do-
main expertise, repetitive labor-intensive analysis,
low iteration efficiency, and performance bottle-
necks that are difficult to overcome (Wang et al.,
2025; Yu et al., 2025).
As shown in Figure 1(b), Modern large lan-
guage model (LLM) agents promise to dramati-
cally accelerate this iterative loop by automating
code generation, hypothesis testing, and strategy
refinement (Luo et al., 2025; Tang et al., 2025a;
Dong et al., 2025). Nevertheless, the direct appli-
cation of general-purpose large language models
(LLMs) to quantitative finance introduces new criti-
cal challenges. Specifically, these models are prone
to generating hallucinatory trading rules, produc-
ing unverifiable and unexecutable strategy modifi-
cations, and failing to provide transparent causal
explanations for their proposed changes (Wu et al.,
2025; Li et al., 2024a). A system that generates
many candidates can look impressive by exploit-
ing noisy validation windows, low trade counts, or
unreported degrees of freedom (White, 2000; Bai-
ley et al., 2017; Harvey et al., 2016). Therefore,
the central problem is not simply to generate
strategies, but to improve strategies under a pro-
tocol that records, verifies, and rejects unsafe
edits.Throughout this process, the LLM acts only
as a bounded edit proposer over the typed strategy
genome; all data-dependent accept or reject deci-
sions are made by deterministic verification and
promotion modules, and the model is never trained
on market data.
Existing LLM-driven quantitative finance stud-
ies focus on autonomous trading strategy construc-
tion and alpha factor mining (Kou et al., 2025; Tang
et al., 2025b; Wang et al., 2026; Li et al., 2025b;
Tian et al., 2025). In contrast, we study a more
practically impactful yet understudied problem: the
arXiv:2607.12455v3  [cs.AI]  10 Sep 2026

Figure 1: Motivation. Compared with manual human optimization and vanilla LLM rewriting,EVOQUANTprovides
a verifier-guided closed loop for controlled and reliable strategy improvement.
systematic improvement of existing deployed quan-
titative strategies. Figure 1(c) illustrates the work-
flow and advantages of our proposed optimization
framework. Our framework takes a user-provided
quantitative strategy as input. Unlike unconstrained
generative search, we formulate automated strategy
optimization as a closed-loop scientific process. In
this process, the system explicitly represents the
underlying hypothesis, diagnoses current failure
modes, guides the LLM to generate controlled op-
timization hypotheses step by step, and adopts a
modification only after it survives a rigorous multi-
stage verification pipeline.
The proposed method implements this design
through four technical principles. (i) It converts
raw strategy logic into a typed strategy genome.
This genome serves as an editable intermediate
representation that supports interventions ranging
from parameter tuning and local structural repair to
logic rewriting. (ii) It builds an LLM-based strat-
egy risk-diagnosis agent. By integrating backtest
evidence across multiple time periods, the agent
analyzes failure modes from the perspectives of
trading behavior, risk exposure, and market com-
patibility, thereby identifying the core weaknesses
of the current strategy. (iii) Candidate generation
is conditioned on the diagnostic results and orga-
nized into a hierarchy of increasingly expressive
edits. Guided by the LLM, the system progresses
from conservative local tuning to structural recon-
struction, strategy-family migration, and hypothe-
sis rewriting. Each candidate is emitted as an ex-
plicit edit plan over the strategy genome, enabling
drift constraints during optimization and post-hoc
provenance auditing. (iv) An out-of-sample-aware
verifier and an adaptive promotion engine jointly
screen candidates through hard admission rules
and robustness penalties. A candidate replaces
the current incumbent only after passing all ver-
ification stages. In addition, a built-in knowledge-
distillation module continuously distills effective
experience from the optimization process into a
reusable strategy knowledge base, enabling contin-
ual self-improvement of the system.
We evaluate whether the proposed iterative pro-
cess improves quantitative strategies across both eq-
uity and cryptocurrency markets while mitigating
single-asset artifacts and optimization overfitting.
Across seven representative strategies, the system
consistently improves test performance, raising the
average Sharpe ratio from −0.298 to 0.538, with
the best-performing strategy achieving a 199% rel-
ative improvement. Ablation and stress-test results
further show that diagnosis, LLM-based candidate
generation, adaptive promotion, and reusable mem-
ory each contribute to robust optimization gains.
Our contributions are:
• Evidence-constrained strategy evolution.We
formulate automated quantitative strategy im-
provement as evidence-constrained program evo-

lution, where user-provided strategies are repre-
sented as structured trading genomes that support
localized, executable, and provenance-preserving
edits.
• LLM-enabled verifier-guided optimization
protocol.We develop a verifier-guided optimiza-
tion framework that uses LLMs for failure-mode
diagnosis and hierarchical candidate synthesis,
while integrating out-of-sample-aware verifica-
tion, adaptive promotion, and memory-based ex-
perience reuse into a unified auditable loop.
• Long-horizon cross-market evaluation.We
provide a long-horizon empirical evaluation
across A-share and Bitcoin strategies, including
before–after performance comparisons, compo-
nent ablations, transaction-cost stress tests, and
walk-forward validation.
2 Related Work
Backtest overfitting and data snooping.Finan-
cial machine learning has long recognized that re-
peated strategy search can inflate apparent perfor-
mance through data snooping and backtest over-
fitting (White, 2000; Bailey et al., 2017). Prac-
tical treatments emphasize leakage-aware valida-
tion (López de Prado, 2018), and recent theory
quantifies in-sample to out-of-sample Sharpe de-
cay (Jacquier et al., 2025). Our work addresses this
concern by logging rejected candidates, exposing
low-trade failures, tracking validation–test behav-
ior, and reporting non-degradation rather than only
the best discovered strategy.
LLM agents and iterative refinement.LLM
agents can reason, act, and revise outputs through
feedback loops (Yao et al., 2023; Shinn et al.,
2023; Madaan et al., 2023), and recent finance
agents extend this pattern to market analysis, fac-
tor mining, and tool-augmented trading (Zhang
et al., 2024; Li et al., 2024b; Zhang et al., 2025).
Newer benchmarks and critiques highlight instabil-
ity and weak deployment evidence in LLM trading
agents (Zhang et al., 2026; Ye et al., 2026).EVO-
QUANTdiffers by grounding each strategy edit
in chronological backtests, trade-coverage checks,
cost assumptions, and risk-sensitive promotion.
Programmatic strategy search.Programmatic
strategy search has moved from evolutionary and
symbolic alpha discovery (Kakushadze, 2016; Cui
et al., 2021) toward automated formulaic-alpha
mining with reinforcement learning, LLM agents,
structure-aware search, and dedicated evaluation
protocols (Shi et al., 2025; Zhao et al., 2025; Tang
et al., 2025b; Ding et al., 2026; Chen et al., 2026;
Yang et al., 2026; Wang et al., 2026). These ap-
proaches scale candidate generation and assess-
ment, but broad search spaces can blur whether
a gain reflects principled refinement of an initial
market hypothesis or selection among many de-
grees of freedom.EVOQUANTinstead treats op-
timization as constrained program evolution from
a user-provided strategy, with typed genome edits,
diagnosis-conditioned generation, out-of-sample-
aware promotion gates, and an explicit audit trail.
3 Methodology
EVOQUANTcasts quantitative strategy optimiza-
tion asverifier-guided program evolution. As
shown in Figure 2, the system contains four mod-
ules: strategy ingestion and representation, base-
line evidence construction, a diagnostic–generative
optimization loop, and final strategy refinemen-
t/output. The core design of our framework empha-
sizes practical execution over pure generation. The
large language model proposes strategy revisions
within controllable scopes, and components includ-
ing the backtester and verifier jointly determine
whether such revisions are admissible.
At round t, the incumbent genome gt is evalu-
ated into an evidence pack Et. The optimization
loop diagnoses the current bottleneck, generates
candidates Ct, and promotes only a verified candi-
date:
gt+1 =
(
c⋆ t ,ifc ⋆ t is accepted byΠ,
gt,otherwise.
where c⋆ t is the best verified candidate selected from
Ct, and Π denotes the promotion rule later speci-
fied in Module 3. The loop adopts a conservative
design: failed candidates are stored with rejection
reasons and later used to avoid repeating unproduc-
tive edits.
3.1 Module 1: Strategy Ingestion and
Representation
EVOQUANTfirst normalizes the user strategy into
a typed intermediate representation called astrat-
egy genome. This module performs four steps.
First, it parses raw code or rule text into an ab-
stract syntax tree. Second, it tags trading semantics

Figure 2:EVOQUANTworkflow organized into four modules. Module 1 normalizes raw strategy code or logic into
a typed strategy genome. Module 2 constructs chronological baseline evidence. Module 3 performs the iterative
diagnostic–generative loop, including bottleneck diagnosis, controlled candidate editing, verification, and promotion
with memory update. Module 4 outputs the best verified strategy, optimization trajectory, and report.
such as signals, entry conditions, risk rules, posi-
tion sizing, and exits. Third, it factors the strat-
egy into editable layers. Finally, it recompiles the
genome to ensure that the representation remains
executable. Formally, the parser Φ maps a strategy
sto
Φ(s) =g=

gsig, grisk, gpos, gentry, gexit, ξ  ,
where ξ stores provenance, strategy family, parent
identifiers, and mutation history. The output of
this module is not merely a parsed program, but an
editable research object. Later edits must specify
the target layer, satisfy non-anticipativity and ex-
posure constraints, and compile back to executable
strategy semanticsg.
3.2 Module 2: Baseline Evaluation and
Evidence Construction
EVOQUANTnext measures the original strategy be-
fore attempting to improve it. The evaluator loads
real market data, constructs chronological splits,
and runs the incumbent genome under the same
execution assumptions used for all future candi-
dates. It records both scalar metrics and behavioral
profiles, producing
E(g) =
n
MX , Ptrade X , Pregime X
o
X∈{train,val,test}
∪ {δoos, Cconc, Hrisk}.
Here, MX comprises performance metrics such as
return, Sharpe ratio, maximum drawdown, trade
count, win rate, and related statistics. P trade X char-
acterizes trading behaviors including trade sparsity,
holding period distributions, and return concentra-
tion, while P regime X quantifies the strategy’s sensi-
tivity to different market regimes. The metric δoos
reflects the degradation from validation to out-of-
sample (OOS) performance, and Hrisk documents
abnormal risk phenomena, such as excessive stop-
loss triggering or truncated upside returns. This
module provides comprehensive evidence for the
downstream diagnostic loop, enabling the system to
assess not only whether a strategy underperforms,
but also to elucidate the specific failure modes un-
derlying any observed weaknesses.
3.3 Module 3: Strategy Optimization Pipeline
Bottleneck Diagnosis and Search Planning.It
starts by turning Evidence pack statistics into a

bottleneck diagnosis and a concrete search plan.
zt =B(E t,M t),
pt = (ot, ℓt,O t,F t, Kt).
The diagnosis is implemented by large language
models through rule-based evidence verification
and in-depth analysis. It identifies failure modes
such as risk-rule alpha truncation, regime mis-
match, validation decay and so on. The search
plan then specifies the round objective ot, search
level ℓt, allowed operators Ot, forbidden shortcuts
Ft, and candidate budgetK t.
The diagnosis constrains the generator’s action
space. For example, If the bottleneck is validation–
OOS decay, the plan favors simplification, ro-
bustness repair, and parameter smoothing rather
than adding more regime-specific conditions. The
search level progresses fromrepairtobridge,re-
design, and finallyfamily migration. This keeps
the adaptivity of AutoML and LLM-as-optimizer
loops (Hutter et al., 2011; Akiba et al., 2019; Yang
et al., 2024; Guo et al., 2024), but makes each
search step accountable to a financial failure mode.
Candidate Generation and Controlled Edit-
ing.Given the search plan,EVOQUANTbuilds
a candidate-generation prompt from four artifacts:
the current genome, a compressed EvidencePack,
the bottleneck diagnosis, and retrieved memory
cases. The LLM must return a controlled edit plan
with fields for target layer, operation, patch content,
mechanism rationale, expected metric movement,
and safety constraints. A candidate is accepted for
testing only if it satisfies the typed edit contract:
ct,i = ∆t,i(gt),
∆t,i ∈ T(pt,M t),
dG(gt, ct,i)≤ϵ ℓt,I(c t,i) = 1.
Here ∆t,i is an edit operator,dG measures semantic
drift from the incumbent, and I checks executable
and financial invariants. In practice, parameter re-
pair adjusts lookback windows, thresholds, stop
widths, and position caps; bridge edits modify entry
filters, exit rules, or signal combinations; redesign
rewrites the strategy graph around a coherent mar-
ket mechanism. Family migration, the highest-tier
modification, shifts to a nearby strategy family after
repeated local failures. Before evaluation, candi-
dates are compiled, deduplicated by genome hash,
and diversified so that one round does not spend all
budget on near-identical edits.
OOS-Aware Verification, Promotion, and Mem-
ory.The verifier evaluates candidates in parallel
under the same data split and execution assump-
tions as the incumbent. It first applies hard gates
that are intentionally simple and difficult to game:
G(c) = 1⇐ ⇒Nval(c)≥n min, Noos(c)≥n min,
MDDoos(c)≤ ¯d,
dG(gt, c)≤ϵ ℓt,I(c) = 1.
These gates remove non-executable, zero-trade,
overly drifting, and high-drawdown candidates be-
fore any soft scoring. Gated candidates are then
ranked with a compact score:
Q(c) =w v∆Sval +w o∆Soos +w r∆Roos
−λ dPdd −λ gPgap −λ sPstress.
Here S denotes Sharpe, R denotes return, P
denotes the penalty and all deltas are candidate-
minus-incumbent. The penalties capture OOS (out-
of-sample) drawdown expansion, validation–OOS
discrepancy, and lightweight stress probes such
as fee/slippage perturbation, one-bar delay, and
parameter jitter. The score deliberately separates
validation improvement from out-of-sample audit
behavior, so a fluent rewrite that wins only on vali-
dation is not automatically promotable.
The promotion engine assigns each candidate to
ADOPT,INCUBATE, orREJECT. ADOPTreplaces
the incumbent only when the candidate passes hard
gates and exceeds an adaptive score threshold. IN-
CUBATEstores candidates that show a plausible
mechanism but insufficient evidence, whileREJECT
records failure reasons such as zero trades, OOS
collapse, excessive drift, or abnormal drawdown.
After the decision, Memory module stores the di-
agnosis, search plan, edit summary, candidate evi-
dence, decision, and failure reason. This memory is
first distilled and persisted in the strategy repository,
serving dual purposes in subsequent iterations: re-
trieving proven optimization paradigms and black-
listing recurrent failure mechanisms, thereby en-
abling continuous self-improvement of the system.
3.4 Module 4: Iterative Refinement and Final
Strategy Output
The final module manages convergence and output.
It tracks the best verified genome observed across
the trajectory,
g⋆ t = arg max g∈Ht Qaudit(g),

where Ht contains adopted and incubated candi-
dates observed so far. If local repairs fail repeatedly,
the controller escalates to bridge edits, redesign,
and finally family migration. The loop stops when
the round budget is exhausted, the audit score con-
verges, or no admissible search level passes veri-
fication. The final output includes the optimized
strategy code g⋆, a pre/post backtest report, and
the full optimization trajectory with diagnoses, edit
plans, promotion decisions, and memory records.
4 Experimental Protocol
Data and LLM Backend.All experimental data
are obtained from the AKShare database1. We use
daily historical data for both the A-share market
and Bitcoin from 1/1/2020 to 31/12/2025. For all
components that require large language model in-
ference, we use the DeepSeek-R1 model (Guo et al.,
2025). Each optimization run lasts 20 iterations.
A-share Main Task.We evaluate four representa-
tive A-share quantitative strategies: an EMA-RSI
trend-continuation strategy, a Bollinger Band-RSI
mean-reversion strategy, a volume-breakout strat-
egy, and a low-volatility quality-stock strategy. We
randomly sample 30 stocks as the experimental
universe and independently optimize each strategy–
stock pair. For each strategy family, the final perfor-
mance is computed as an equal-weighted portfolio
over the 30 optimized stock-level strategies. All
core empirical conclusions for the A-share market
are based on these portfolio-level backtest results.
Bitcoin Main Task.We further evaluate three Bit-
coin trading strategies: a MACD-RSI-Bollinger
Band strategy, an ATR trend-breakout strategy, and
an oversold-reversal strategy. This experiment ex-
amines whether the proposed optimization frame-
work can adapt to an alternative asset class with
substantially different volatility and trend character-
istics, while still improving strategy performance.
Ablation Studies.To isolate where the optimiza-
tion gains come from, we organize the ablation
study into two groups. The first group,setting
variations, changes the search or selection con-
figuration while keeping the overall pipeline in-
tact:Simple thresholdreplaces adaptive promo-
tion with a fixed threshold rule,Parameter only
restricts candidate generation to parameter-level
tuning,Random mutation onlyreplaces diagnosis-
1https://akshare.akfamily.xyz/
conditioned generation with random edits, and
Bayesian Opt parameter-onlytunes numeric param-
eters with Bayesian optimization under the same
verifier protocol but cannot rewrite strategy logic.
The second group,pipeline variations, removes
major functional modules from the full system:
w/o promotion enginedisables adaptive candidate
adoption,w/o rule diagnosisremoves rule-based
failure-mode diagnosis, andw/o memorydisables
both retrieval from and writing to historical opti-
mization experience. All ablations are conducted
on the A-share volume-breakout task (See Table 2).
Robustness and Walk-Forward Tests.We per-
form robustness and walk-forward tests on the A-
share volume-breakout strategy. For robustness,
we double the transaction cost and slippage as-
sumptions, and change the “train/validation/test”
split points. For walk-forward tests, we use two
distinct rolling windows (2020-2023, 2021-latest)
compared to the original (2020-2025).
5 Results
5.1 Main A-Share Results
Table 1 reports the comparative results of the four
quantitative strategies on the test set before and af-
ter optimization.We mainly report the performance
of the strategy on the test set before and after opti-
mization, because the test set is an important indi-
cator for evaluating whether the optimized strategy
has generalization ability. Figure 3(a, b) present
the comparison of the main quantitative strategies
across all time periods. The remaining figures can
be found in the appendix. All four strategy-family
portfolios improve Sharpe after optimization, with
Sharpe uplifts from −0.298 to 0.538 and an aver-
age uplift of 0.829. Annual return also improves
for all four strategies, with an average return uplift
of 13.38 percentage points. Drawdown behavior
is more divergent: EMA-RSI and low-volatility
quality reduce MDD, while Bollinger reversion and
volume breakout trade higher return for larger draw-
down. The overall result shows thatEVOQUANT
improves risk-adjusted performance broadly, but
does not trivially optimize by only suppressing risk.
5.2 Main Bitcoin Results
Table 1 and Figure 3(c) report the Bitcoin re-
sults. All three original Bitcoin strategies start with
negative test Sharpe. Optimization improves all
three: MACD-RSI-Bollinger improves by 1.383

Market Strategy family Sharpe↑Return (%)↑MDD (%)↓
Base Opt.∆Base Opt.∆Base Opt.∆
A-share
Bollinger Reversion 0.351 0.966 0.615 4.89 9.02 4.13 5.01 6.71 1.70
EMA-RSI Trend -0.465 0.367 0.832 1.64 16.83 15.19 14.36 10.41 -3.95
Low-V ol Quality -0.500 0.386 0.885 1.58 17.86 16.28 9.30 8.26 -1.04
V olume Breakout -0.493 0.489 0.982 -2.21 15.74 17.95 4.81 6.62 1.81
Crypto
MACD-RSI Bollinger -1.118 0.265 1.383 -13.27 5.42 18.69 18.22 8.54 -9.68
ATR Trend Breakout -1.536 -1.050 0.486 -14.48 -9.67 4.81 14.06 12.01 -2.05
Oversold Reversal -0.838 0.679 1.516 -8.37 11.56 19.93 16.53 12.17 -4.36
Table 1: Main results across A-share and cryptocurrency strategy families. ∆ is computed as Opt.(optimized) minus
Base (original). Arrows indicate the preferred direction for each metric. Positive ∆ is desirable for Sharpe and
Return, while negative∆is desirable for MDD.
train val testOriginal Optimized
60
40
 20
0
20

40
2020-01-01 2025-12-31
Trading Date
(c)  Bitcoin Oversold Reversal
40
20
10
0
10
2020-01-02 2025-12-30
Trading Date
(a)  A-share Volume Breakout
30
20
10
0
10
2020-01-02 2025-12-30
(b)  A-share Low-Vol Quality
Trading Date
Return (%) Return (%) Return (%)
30
Figure 3: Return curves of the original and optimized strategies on three representative tasks from 2020 to 2025: (a)
A-share V olume Breakout, (b) A-share Low-V ol Quality, and (c) Bitcoin Oversold Reversal. Shaded regions denote
the train, validation, and test periods.
V olume Breakout Sharpe∆Return∆MDD∆
EVOQUANTFully loaded 0.982 17.95 1.81
Setting variations
Simple threshold 0.053 3.39 3.34
Parameter only 0.274 6.59 -0.21
Random mutation only 0.645 13.05 2.34
Bayesian Opt. parameter-only 0.739 11.11 1.14
Pipeline variations
w/o promotion engine 0.128 4.32 2.72
w/o rule diagnosis 0.693 9.99 -2.76
w/o memory 0.782 15.95 -2.19
Table 2: Ablations on the A-share volume-breakout task.
Returns and MDD are annualized percentage values.
Sharpe points and becomes positive-Sharpe, over-
sold reversal improves by 1.516 and also becomes
positive-Sharpe, while ATR trend breakout remains
negative but improves by 0.486. Unlike the A-share
portfolios, all three Bitcoin strategies reduce MDD,
by 2.05 to 9.68 percentage points, suggesting that
the verified edits improve both payoff quality and
downside control in this market.
5.3 Ablation Study
Table 2 isolates the main mechanisms on the fixed
30-stock A-share volume-breakout task. The full
system achieves Sharpe uplift 0.982. Removing the
promotion engine reduces Sharpe uplift to 0.128,
while simple-threshold promotion reaches only
0.053. These results demonstrate that adaptive
promotion serves as a core enabler. Simply ex-
panding candidate pools cannot yield performance
gains, since the non-promotion configuration in-
volves more edits on average yet achieves markedly
inferior results.
Candidate generation also plays an important
role, although its effect is more nuanced. Restrict-
ing the search to parameter-only edits improves
the Sharpe ratio by 0.274, indicating that local tun-
ing alone cannot explain the full performance gain.
The random-mutation baseline achieves an aver-
age improvement of 0.645. While this baseline
remains competitive, it still underperforms the full
system and is more prone to severe strategy drift
and weak interpretability. The Bayesian Optimiza-
tion parameter-only baseline reaches an uplift of
0.739: even principled parameter search within
the original strategy logic under the same verifier
protocol cannot close the gap to the full system,
confirming that the larger gain stems from verifier-
constrained structural rewriting. Removing the
rule-diagnosis module reduces the improvement
to 0.693, and removing the shared-memory mech-

Protocol Strategy Sharpe↑Return (%)↑MDD (%)↓
Base Opt.∆Base Opt.∆Base Opt.∆
Robustness testing
2x fee/slip
Bollinger Reversion 0.647 1.025 0.378 8.71 11.40 2.69 2.62 2.25 -0.37
MA-RSI Trend -0.855 -0.202 0.653 -5.33 7.13 12.46 10.22 7.51 -2.71
Low-V ol Quality -0.633 0.504 1.136 -2.79 13.98 16.77 5.95 5.53 -0.42
V olume Breakout -0.384 0.133 0.517 -1.07 9.04 10.11 1.19 3.10 1.91
Split shift
Bollinger Reversion 0.596 0.848 0.252 5.92 8.54 2.62 3.72 2.77 -0.95
EMA-RSI Trend -0.391 0.263 0.653 -4.77 7.95 12.72 18.24 12.74 -5.50
Low-V ol Quality -0.100 0.359 0.459 6.05 12.32 6.27 10.99 7.98 -3.01
V olume Breakout -0.048 -0.001 0.047 4.94 4.86 -0.08 5.95 9.25 3.30
Walk-forward
2020–2023
Bollinger Reversion 0.099 0.355 0.256 1.09 5.51 4.42 1.00 1.44 0.44
EMA-RSI Trend -0.408 0.440 0.848 4.26 21.03 16.77 5.38 4.76 -0.62
Low-V ol Quality -0.156 0.306 0.462 8.00 11.13 3.13 4.02 4.19 0.17
V olume Breakout 0.159 0.196 0.038 1.15 1.43 0.28 0.00 0.03 0.03
2021–latest
Bollinger Reversion 0.334 0.602 0.269 6.14 7.39 1.25 2.76 3.22 0.46
EMA-RSI Trend -1.014 -0.063 0.951 -8.81 11.30 20.11 10.27 7.87 -2.40
Low-V ol Quality -0.563 0.136 0.699 -2.19 16.29 18.48 3.18 5.31 2.13
V olume Breakout 0.113 0.486 0.373 1.15 15.34 14.19 0.20 2.75 2.55
Table 3: Robustness and rolling walk-forward portfolio results on the controlled slice. Returns and MDD are
annualized percentage values.
anism further changes the improvement to 0.782.
These results confirm that both diagnosis-guided
search and memory-based experience reuse con-
tribute materially to the overall system.
5.4 Robustness and Walk-Forward
Table 3 reports stress and rolling evaluations.
Under doubled fee/slippage assumptions, mean
Sharpe uplift remains 0.700 , indicating that the
gains are not purely a friction artifact. Under an
alternative chronological split, the uplift falls to
0.368 but remains positive improvement. Rolling
walk-forward evaluation also remains positive: the
2020–2023 window yields 0.370 uplift and the
later-start window yields 0.545 uplift. The reduced
magnitude under split shifts and rolling windows is
expected; the important result is that performance
weakens without collapsing.
6 Discussion
Capability across strategies and markets.The
results suggest thatEVOQUANTcan optimize mul-
tiple strategy families rather than a single hand-
picked rule. In the A-share market, the method
improves diverse equity strategies after aggregat-
ing stock-level optimizations into portfolio-level
results. In the cryptocurrency market, it also im-
proves Bitcoin strategies with different volatility
and trend characteristics, indicating broader appli-
cability across market settings.
Improvement is not just random edits.The abla-
tion study indicates that the main benefit does not
come from blindly perturbing strategy parameters
or rules. Random mutation can occasionally find
useful changes, but it lacks the failure-mode di-
agnosis, mechanism-aware hypothesis generation,
and rejection feedback needed for reliable optimiza-
tion. In contrast, LLM-guided strategy optimiza-
tion contributes by turning backtest evidence into
targeted edit hypotheses, explaining why an edit
should help, and embedding those hypotheses in
an evidence-aware promotion protocol.
Verification is central to the contribution.The
gains should be interpreted as risk-adjusted im-
provements under explicit evidence gates, not as
universal drawdown reduction. Some A-share
strategies accept higher drawdown in exchange
for larger return and Sharpe, while the robustness
tests show that the effect weakens under stricter
settings without disappearing. This positions LLM-
enabled strategy optimization as a verification prob-
lem as much as a generation problem: fluent edits
are easy to produce, but trustworthy evidence re-
quires chronological validation, provenance track-

ing, adaptive promotion, and visible rejection logs.
Methodological boundaries. EVOQUANT
claims relative improvement under a controlled his-
torical backtesting protocol, not live-trading readi-
ness or absolute guarantees under novel market
regimes. Daily-bar backtests omit liquidity, bor-
row, and market-impact frictions, which bounds
the absolute interpretation of the results while leav-
ing the paired comparisons largely unaffected.
7 Conclusion and Future Work
This paper studied automated quantitative strat-
egy optimization as a verifier-guided program-
evolution problem. Across A-share and Bitcoin
strategies,EVOQUANTimproves risk-adjusted
performance while keeping the optimization pro-
cess auditable through explicit evidence gates and
recorded edit decisions.
Future work can extend the evaluation to more
realistic execution assumptions, larger investable
universes, and stronger verifiers that combine statis-
tical robustness tests with domain-specific financial
constraints. These extensions would further clarify
the boundary between useful automated strategy
improvement and overfitting-driven search. We
also plan to integrate statistical overfitting tests
such as the deflated Sharpe ratio into promotion,
and to explore broader strategy discovery from
typed hypothesis templates under the same verifier-
guided constraint layer.
Limitations
This study is a research prototype, not an invest-
ment recommendation. The backtests use local
daily data and simplified execution assumptions.
Although we stress fees and slippage, real trad-
ing introduces liquidity, market impact, survivor-
ship, corporate action, borrow, and operational
constraints. To mitigate survivorship bias, we re-
validated the A-share evaluation on a Wind point-
in-time, delisting-inclusive universe (100 randomly
sampled stocks for two strategy families); the im-
provement over the human-written baselines per-
sists. The LLM comparison is also limited by local
model/API configuration and budget. Since orig-
inal and optimized strategies share the same data,
splits, and execution assumptions, simplified daily-
bar execution affects absolute interpretation more
than the paired comparisons; richer execution mod-
eling remains future work. These limitations do not
invalidate the system contribution, but they bound
the financial interpretation of the results.
Ethical Considerations
This work studies automated strategy optimization
for quantitative trading. The methods are evalu-
ated exclusively on historical backtests and do not
constitute financial advice or a live trading system.
No personally identifiable information, proprietary
data, or confidential market data were used. All
equity and cryptocurrency price data used in experi-
ments are publicly available daily OHLCV records.
Any third-party models, APIs, datasets, or market
data sources used by the artifact remain subject to
their original licenses and terms of use.
The paper does not claim that the presented sys-
tem is safe for deployment in real financial markets.
As discussed in the Limitations section, the evalua-
tion relies on simplified execution assumptions that
do not account for liquidity, market impact, or sur-
vivorship bias. Practitioners who build on this work
bear full responsibility for compliance with appli-
cable financial regulations and risk management
requirements.
References
Takuya Akiba, Shotaro Sano, Toshihiko Yanase, Takeru
Ohta, and Masanori Koyama. 2019. Optuna: A next-
generation hyperparameter optimization framework.
InProceedings of the 25th ACM SIGKDD Interna-
tional Conference on Knowledge Discovery & Data
Mining, pages 2623–2631. ACM.
David H. Bailey, Jonathan M. Borwein, Marcos López
de Prado, and Qiji Jim Zhu. 2017. The probability of
backtest overfitting.The Journal of Computational
Finance, 20(4):39–69.
Binqi Chen, Hongjun Ding, Ning Shen, Taian Guo,
Jinsheng Huang, Luchen Liu, and Ming Zhang.
2026. AlphaSAGE: Structure-aware alpha mining
via GFlowNets for robust exploration. InThe Four-
teenth International Conference on Learning Repre-
sentations, pages 2955–2982.
Can Cui, Wei Wang, Meihui Zhang, Gang Chen, Zhao-
jing Luo, and Beng Chin Ooi. 2021. AlphaEvolve:
A learning framework to discover novel alphas in
quantitative investment. InProceedings of the 2021
International Conference on Management of Data,
pages 2208–2216. ACM.
Hongjun Ding, Binqi Chen, Jinsheng Huang, Taian Guo,
Zhengyang Mao, Guoyi Shao, Lutong Zou, Luchen
Liu, and Ming Zhang. 2026. AlphaEval: A com-
prehensive and efficient evaluation framework for
formula alpha mining. InProceedings of the 32nd

ACM SIGKDD Conference on Knowledge Discovery
and Data Mining V .2, pages 897–908. ACM.
Yihong Dong, Xue Jiang, Jiaru Qian, Tian Wang, Kechi
Zhang, Zhi Jin, and Ge Li. 2025. A survey on code
generation with LLM-based agents.arXiv preprint
arXiv:2508.00083.
Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song,
Peiyi Wang, Qihao Zhu, Runxin Xu, Ruoyu Zhang,
Shirong Ma, Xiao Bi, Xiaokang Zhang, Xingkai
Yu, Yu Wu, Z. F. Wu, Zhibin Gou, Zhihong Shao,
Zhuoshu Li, Ziyi Gao, Aixin Liu, and 175 oth-
ers. 2025. DeepSeek-R1 incentivizes reasoning
in LLMs through reinforcement learning.Nature,
645(8081):633–638.
Qingyan Guo, Rui Wang, Junliang Guo, Bei Li, Kaitao
Song, Xu Tan, Guoqing Liu, Jiang Bian, and Yujiu
Yang. 2024. Connecting large language models with
evolutionary algorithms yields powerful prompt opti-
mizers. InThe Twelfth International Conference on
Learning Representations, pages 34133–34156.
Campbell R. Harvey, Yan Liu, and Heqing Zhu. 2016.
. . . and the cross-section of expected returns.Review
of Financial Studies, 29(1):5–68.
Frank Hutter, Holger H. Hoos, and Kevin Leyton-Brown.
2011. Sequential model-based optimization for gen-
eral algorithm configuration. InLearning and Intelli-
gent Optimization, volume 6683 ofLecture Notes in
Computer Science, pages 507–523. Springer Berlin
Heidelberg.
Antoine Jacquier, Johannes Muhle-Karbe, and Joseph
Mulligan. 2025. In-sample and out-of-sample Sharpe
ratios for linear predictive models.arXiv preprint
arXiv:2501.03938.
Zura Kakushadze. 2016. 101 formulaic alphas.Wilmott,
2016(84):72–81.
Zhizhuo Kou, Holam Yu, Junyu Luo, Jingshu Peng, Xu-
jia Li, Chengzhong Liu, Juntao Dai, Lei Chen, Sirui
Han, and Yike Guo. 2025. Automate strategy finding
with LLM in quant investment. InFindings of the
Association for Computational Linguistics: EMNLP
2025, pages 18517–18533. Association for Computa-
tional Linguistics.
Changlun Li, Yao Shi, Chen Wang, Qiqi Duan, Runke
Ruan, Weijie Huang, Haonan Long, Lijun Huang,
Nan Tang, and Yuyu Luo. 2025a. Time travel is cheat-
ing: Going live with DeepFund for real-time fund
investment benchmarking. InAdvances in Neural
Information Processing Systems, volume 38, pages
184676–184704. Neural Information Processing Sys-
tems Foundation, Inc. (NeurIPS).
Junyi Li, Jie Chen, Ruiyang Ren, Xiaoxue Cheng, Xin
Zhao, Jian-Yun Nie, and Ji-Rong Wen. 2024a. The
dawn after the dark: An empirical study on factuality
hallucination in large language models. InProceed-
ings of the 62nd Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Pa-
pers), pages 10879–10899. Association for Compu-
tational Linguistics.
Xiang Li, Penglei Sun, Wanyun Zhou, Zikai Wei,
Yongqi Zhang, and Xiaowen Chu. 2026. FinKario:
Event-enhanced automated construction of financial
knowledge graph. InProceedings of the 64th Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 9826–9845.
Association for Computational Linguistics.
Yuante Li, Xu Yang, Xiao Yang, Xisen Wang, Weiqing
Liu, and Jiang Bian. 2025b. R&D-Agent-Quant: A
multi-agent framework for data-centric factors and
model joint optimization. InAdvances in Neural
Information Processing Systems, volume 38, pages
131781–131830. Neural Information Processing Sys-
tems Foundation, Inc. (NeurIPS).
Zhiwei Li, Ran Song, Caihong Sun, Wei Xu, Zhengtao
Yu, and Ji-Rong Wen. 2024b. Can large language
models mine interpretable financial factors more ef-
fectively? a neural-symbolic factor mining agent
model. InFindings of the Association for Compu-
tational Linguistics: ACL 2024, pages 3891–3902.
Association for Computational Linguistics.
Marcos López de Prado. 2018.Advances in Financial
Machine Learning. John Wiley & Sons.
Junyu Luo, Weizhi Zhang, Ye Yuan, Yusheng Zhao,
Junwei Yang, Yiyang Gu, Bohan Wu, Binqi Chen,
Ziyue Qiao, Qingqing Long, Rongcheng Tu, Xiao
Luo, Wei Ju, Zhiping Xiao, Yifan Wang, Meng Xiao,
Chenwu Liu, Jingyang Yuan, Shichang Zhang, and 7
others. 2025. Large language model agent: A survey
on methodology, applications and challenges.arXiv
preprint arXiv:2503.21460.
Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler
Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon,
Nouha Dziri, Shrimai Prabhumoye, Yiming Yang,
Shashank Gupta, Bodhisattwa Prasad Majumder,
Katherine Hermann, Sean Welleck, Amir Yazdan-
bakhsh, and Peter Clark. 2023. Self-Refine: Itera-
tive refinement with self-feedback. InAdvances in
Neural Information Processing Systems, volume 36,
pages 46534–46594. Neural Information Processing
Systems Foundation, Inc. (NeurIPS).
Deniz NoorMohammadzadehMaleki, Sina Abbaskhani,
Amirfarhad Farhadi, and Azadeh Zamanifar. 2026.
Artificial intelligence methods for financial market
prediction: A systematic review.Computers and
Electrical Engineering, 134:111110.
Hao Shi, Weili Song, Xinting Zhang, Jiahe Shi, Cuicui
Luo, Xiang Ao, Hamid Arian, and Luis Angel Seco.
2025. AlphaForge: A framework to mine and dynam-
ically combine formulaic alpha factors.Proceedings
of the AAAI Conference on Artificial Intelligence,
39(12):12524–12532.

Noah Shinn, Federico Cassano, Ashwin Gopinath,
Karthik Narasimhan, and Shunyu Yao. 2023. Re-
flexion: language agents with verbal reinforcement
learning. InAdvances in Neural Information Pro-
cessing Systems, volume 36, pages 8634–8652. Neu-
ral Information Processing Systems Foundation, Inc.
(NeurIPS).
Wang Tang, Heng Wei Zhang, Jianuo Huang, Shaowen
Wang, Feifan Yu, Hui Yang, and Yu Wang. 2025a.
AgentBuilder: Automating agent creation via large
language model-driven systems.Neurocomputing,
646:130476.
Ziyi Tang, Zechuan Chen, Jiarui Yang, Jiayao Mai,
Yongsen Zheng, Keze Wang, Jinrui Chen, and Liang
Lin. 2025b. AlphaAgent: LLM-driven alpha min-
ing with regularized exploration to counteract alpha
decay. InProceedings of the 31st ACM SIGKDD
Conference on Knowledge Discovery and Data Min-
ing V .2, pages 2813–2822. ACM.
Qiushi Tian, Churong Liang, Kairan Hong, and Run-
nan Li. 2025. Agent-based genetic algorithm for
crypto trading strategy optimization.arXiv preprint
arXiv:2510.07943.
Saizhuo Wang, Hang Yuan, Leon Zhou, Lionel Ni,
Heung-Yeung Shum, and Jian Guo. 2025. Alpha-
GPT: Human-AI interactive alpha mining for quanti-
tative investment. InProceedings of the 2025 Con-
ference on Empirical Methods in Natural Language
Processing: System Demonstrations, pages 196–206.
Association for Computational Linguistics.
Yanlong Wang, Jian Xu, Hongkang Zhang, Shao-Lun
Huang, Danny Dongning Sun, and Xiao-Ping Zhang.
2026. FactorMiner: A self-evolving agent with skills
and experience memory for financial alpha discovery.
InProceedings of the 32nd ACM SIGKDD Confer-
ence on Knowledge Discovery and Data Mining V .2,
pages 12327–12338. ACM.
Halbert White. 2000. A reality check for data snooping.
Econometrica, 68(5):1097–1126.
Yilin Wu, Han Yuan, Li Zhang, and Zheng Ma. 2025.
Natural language inference as a judge: Detecting
factuality and causality issues in language model self-
reasoning for financial analysis. InProceedings of
The 10th Workshop on Financial Technology and
Natural Language Processing, pages 210–220. Asso-
ciation for Computational Linguistics.
Chengrun Yang, Xuezhi Wang, Yifeng Lu, Hanxiao
Liu, Quoc V Le, Denny Zhou, and Xinyun Chen.
2024. Large language models as optimizers. In
The Twelfth International Conference on Learning
Representations, pages 12028–12068.
Han Yang, Dong Hao, Zhuohan Wang, Qi Shi,
and Xingtong Li. 2026. Alpha discovery via
grammar-guided learning and search.arXiv preprint
arXiv:2601.22119.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
Shafran, Karthik Narasimhan, and Yuan Cao. 2023.
ReAct: Synergizing reasoning and acting in language
models. InThe Eleventh International Conference
on Learning Representations.
Yuxuan Ye, Jun Han, Ao Hu, Juncheng Bu, Yiyi Chen,
Liangjian Wen, Danilo Mandic, Danny Dongning
Sun, Xu Yinghui, and Zenglin Xu. 2026. The alpha
illusion: Reported alpha from LLM trading agents
should not be treated as deployment evidence.arXiv
preprint arXiv:2605.16895.
Yangyang Yu, Haohang Li, Zhi Chen, Yuechen Jiang,
Yang Li, Jordan W. Suchow, Denghui Zhang,
and Khaldoun Khashanah. 2025. FinMem: A
performance-enhanced LLM trading agent with lay-
ered memory and character design.IEEE Transac-
tions on Big Data, 11(6):3443–3459.
Junjie Zhang, Shuoling Liu, Tongzhe Zhang, and
Yuchen Shi. 2025. A survey on large language
model-based alpha mining.Frontiers of Information
Technology & Electronic Engineering, 26(10):1809–
1821.
Wentao Zhang, Lingxuan Zhao, Haochong Xia, Shuo
Sun, Jiaze Sun, Molei Qin, Xinyi Li, Yuqing Zhao,
Yilei Zhao, Xinyu Cai, Longtao Zheng, Xinrun Wang,
and Bo An. 2024. A multimodal foundation agent
for financial trading: Tool-augmented, diversified,
and generalist. InProceedings of the 30th ACM
SIGKDD Conference on Knowledge Discovery and
Data Mining, pages 4314–4325. ACM.
Wentao Zhang, Mingxuan Zhao, Jincheng Gao, Jieshun
You, Huaiyu Jia, Yilei Zhao, Bo An, and Shuo Sun.
2026. AlphaForgeBench: Benchmarking end-to-end
trading strategy design with large language models.
arXiv preprint arXiv:2602.18481.
Junjie Zhao, Chengxi Zhang, Min Qin, and Peng Yang.
2025. QuantFactor REINFORCE: Mining steady
formulaic alpha factors with variance-bounded RE-
INFORCE.IEEE Transactions on Signal Processing,
73:2448–2463.
Wanyun Zhou, Saizhuo Wang, Mihai Cucuringu, Zi-
hao Zhang, Xiang Li, Jian Guo, Chao Zhang, and
Xiaowen Chu. 2025. DeltaLag: Learning dynamic
lead-lag patterns in financial markets. InProceedings
of the 6th ACM International Conference on AI in
Finance, pages 422–430. ACM.
A Prompt Templates
This appendix lists the prompt templates used by
EVOQUANTfor LLM-enabled candidate genera-
tion and diagnosis. All prompts were used verbatim
in the frontier LLM experiments reported in Sec-
tion 5.4.

A.1 Diagnosis Prompt
The diagnosis prompt receives the evidence pack
(returns, Sharpe, drawdown, trade counts, recent
rejection reasons) and produces a structured bottle-
neck report.
Promotion Explanation Prompt Template
You are a quantitative strategy analyst.
Given the following backtest evidence pack for
strategy {strategy_name}:
Train Sharpe : {train_sharpe:.3f}
Val Sharpe : {val_sharpe:.3f}
Test Sharpe : {test_sharpe:.3f}
Max Drawdown : {max_dd:.2%}
Trade Count : {n_trades}
Recent rejections: {rejection_summary}
Identify the top-2 bottlenecks from:
[sparse_entry, delayed_exit, excessive_drawdown,
low_trend_filter, overfit_validation,
parameter_sensitivity]
Return a JSON object:
{
"bottlenecks": ["<bottleneck_1>", "<bottleneck_2>"],
"rationale": "<one sentence per bottleneck>"
}
A.2 LLM Candidate Generation Prompt
The candidate generation prompt receives the cur-
rent genome and the diagnosed bottlenecks, and
proposes a single edited genome as a JSON diff.
Promotion Explanation Prompt Template
You are a quantitative strategy engineer.
Current genome (JSON):
{genome_json}
Diagnosed bottlenecks: {bottlenecks}
Propose ONE targeted edit to address the primary bottleneck.
Constraints:
- Do NOT change the core hypothesis of the strategy.
- Only modify parameters or add/remove a single indicator.
- Keep trade count above 20 per year.
Return ONLY a JSON patch in the format:
{
"layer": "<signal|risk|position|exit>",
"field": "<field_name>",
"old_value": <old>,
"new_value": <new>,
"rationale": "<one sentence>"
}
A.3 Promotion Explanation Prompt
When a candidate is promoted,EVOQUANTop-
tionally queries the LLM for a human-readable
explanation of the change, which is stored in the
audit trail.
Promotion Explanation Prompt Template
The following genome edit was accepted by the verifier:
Layer : {layer}
Field : {field}
Old value: {old_value}
New value: {new_value}
Val Sharpe before: {val_before:.3f}
Val Sharpe after : {val_after:.3f}
Summarize in one sentence why this edit is likely beneficial,
referencing the strategy hypothesis.
B Additional Experimental Results
This appendix provides supplementary experimen-
tal results that support the claims in the main paper
but were omitted from the main text due to space
constraints.
B.1 Main A-Share and Bitcoin Results
Figure 4 shows that the optimized strategies gener-
ally achieve stronger return trajectories than their
original counterparts across both A-share and Bit-
coin tasks. For the A-share EMA-RSI Trend and
Bollinger Reversion strategies, optimization leads
to higher cumulative returns throughout the valida-
tion and test periods, with especially clear gains in
the later test window. For Bitcoin strategies, the
effect is more divergent: the optimized MACD-RSI
Bollinger strategy improves substantially and ends
with a higher return, whereas the optimized ATR
Trend Breakout strategy underperforms the orig-
inal strategy in the test period despite remaining
profitable.
B.2 Per-Symbol Sharpe Uplift Distribution
Figure 5 shows the full distribution of per-symbol
test Sharpe uplift across all 120 A-share tasks (i.e.,
task counted by the multiplication of 30 A-share
stocks and 4 typical strategies) in the canonical
seed-42 run. The distribution is right-skewed, with
a long tail of large improvements and a small mass
of degradations, consistent with the 115/120 non-
degradation rate reported in the main text. The
mean test Sharpe uplift is positive in every case,
indicating that the gains are not driven by a single
strategy type. The improvement is strongest for
the V olume Breakout family, followed by Low-V ol
Quality and EMA-RSI Trend, while Bollinger Re-
version shows a smaller but still clear uplift. Over-
all, these results suggest that the verifier-guided op-
timization process can generalize across different
A-share strategy families rather than only benefit-
ing one specific signal design.

Original Optimized
800
600
400
200
0
2020-01-01 2025-12-31
Trading Date
(d)  Bitcoin ATR Trend Breakout
100
80
60
40
20
0
20

2020-01-01 2025-12-31
Trading Date
(c)  Bitcoin MACD-RSI Bollinger
60
40
20
0
20
2020-01-02 2025-12-30
(a)  A-share EMA-RSI Trend
30
25
20
15

10

5
0
2020-01-02 2025-12-30
(b)  A-share Bollinger Reversion
train val test
40
Figure 4: Return curves of the original and optimized strategies on four representative tasks from 2020 to 2025: (a)
A-share EMA-RSI Trend, (b) A-share Bollinger Reversion, (c) Bitcoin MACD-RSI Bollinger, and (d) Bitcoin ATR
Trend Breakout. Shaded regions denote the train, validation, and test periods.
bollinger
reversion
ema
rsi
trend
low
vol
quality
volume
breakout
0.0
0.2
0.4
0.6
0.8
1.0Mean test Sharpe uplift
Risk-adjusted improvement by A-share strategy family
Figure 5: Distribution of per-symbol test Sharpe uplift
(seed 42, all 120 A-share tasks).
B.3 Rejection Reasons
We further analyzed the rejection reasons across
all experiments to characterize the optimizer’s fail-
ure modes and the verifier’s screening behavior.
The rejection analysis (see Figure 6) reveals how
the verifier filters unsafe or unreliable candidate
strategies. The most frequent rejection reason is
sparse trade coverage across OOS splits, indicating
that many candidates do not generate enough out-
of-sample trades to support reliable evaluation. A
smaller number of candidates are rejected because
their risk-adjusted quality falls below the target or
because their performance is unstable across mar-
ket regimes. Only a few candidates are rejected
solely because current-window gains fail to trans-
fer OOS.
0 200 400 600 800 1000 1200 1400
Count
trade coverage is too sparse across OOS sp
risk-adjusted quality is below target
strategy is unstable across regimes and ne
current gains are not transferring OOS and
Rejected / non-adopted iteration reason proxies
Figure 6: Distribution of rejection reasons for non-
adopted candidate strategies. Rejected candidates fail
because: trade coverage is too sparse, below-target risk-
adjusted quality, instability across regimes, or current
gains that do not transfer out of sample.
