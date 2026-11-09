---
title: Are LLMs Good Financial User Simulators? Multi-view Investor Logic Alignment (MILA)
url: https://arxiv.org/abs/2609.15727
category: digital-marketing
subcategory: empirical
date: 2026-09
venue: AAAI
authors:
- Jiajie He
- Jiangyuan Hong
- Xintong Chen
- Dongling Ni
- Wenjin Liu
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.15727
pages: 14
chars: 54285
fetched_at: '2026-11-08T13:21:00+00:00'
kb_version: 1
---

# Are LLMs Good Financial User Simulators? Multi-view Investor Logic Alignment (MILA)

Are LLMs Good Financial User Simulators? Multi-view Investor Logic
Alignment (MILA)
Jiajie He1 Yuanhong Jiang1 Xintong Chen3 Dongling Ni1 Wenjin Liu2
1Hithink Research 2Nanyang Technological University 3McMaster University
jiajiehe@myhexin.com, yuanhongjiang@myhexin.com, chen54xt@mcmaster.ca
donglingni@myhexin.com,wenjinliu23@outlook.com
Abstract
Large language models (LLMs) are increas-
ingly used as user simulators, yet it remains
unclear whether their predictions faithfully re-
produce the evolving decisions of individual
users. We investigate this question in a con-
trolled longitudinal paper-trading study with 80
participants, where user interactions, simulated
transactions, virtual portfolio states, and point-
in-time market information are aligned under a
rolling next-day prediction protocol. We evalu-
ate behavioral fidelity hierarchically, from trade
occurrence to action structure, asset selection,
and downstream portfolio consequences.
Across 1,239 aligned user-days, no evaluated
LLM reliably outperforms a simple recent-
activity persistence baseline for predicting
whether a user trades. Fidelity further deterio-
rates at finer levels: models struggle to recover
buy–sell structure and traded assets, and sim-
ilar activity-level predictions can lead to sub-
stantially different portfolio trajectories. Con-
trolled evidence ablations show that recent trad-
ing history strongly governs activity prediction,
whereas asset selection is substantially more
sensitive to the available evidence. An obser-
vational analysis further finds that intensified
ticker-specific research predicts imminent trad-
ing, but diagnostic tests do not support a causal
interpretation. These findings suggest that cur-
rent LLMs capture useful short-term behavioral
regularities without yet recovering a stable in-
dividual decision mechanism.
1 Introduction
Large language models (LLMs) are increas-
ingly used to simulate human behavior in dia-
logue, recommendation, and interactive decision-
making (Chan et al., 2023; Chen et al., 2026; Park
et al., 2023; Ren et al., 2024). Their ability to in-
tegrate heterogeneous contextual information and
generate flexible, context-dependent actions makes
them a natural foundation for user simulation. How-
ever, generating plausible behavior is not necessar-
ily equivalent to faithfully reproducing the behavior
of a particular individual. A simulator may match
aggregate behavioral statistics while acting at the
wrong times, selecting different objects, or respond-
ing to different evidence than the user it is intended
to represent.
This distinction becomes especially important
in longitudinal decision-making. User actions are
not independent observations: each decision is con-
ditioned on prior behavior, the current state of the
environment, and the consequences of earlier ac-
tions. Financial decision-making provides a useful
setting for studying this problem because these de-
pendencies are explicit. Whether an investor trades
may depend on recent activity, while the direction
and asset involved may additionally depend on cur-
rent holdings, asset-specific attention, and chang-
ing market conditions. A prediction can therefore
appear correct at one level while remaining behav-
iorally inconsistent at another.
Existing financial-agent research has primarily
evaluated trading performance, recommendation
quality, or aggregate market behavior (Zhang et al.,
2024a; Y ANG et al., 2025; Wang et al., 2026b). Re-
cent work has also explored LLM-based investor
simulation and evolving financial-user states (Gong
et al., 2026). These studies establish the potential
of LLMs for modeling financial interactions, but
leave a more basic question comparatively under-
explored:when an LLM produces behavior similar
to an individual user, what aspects of that user’s
decision process have actually been reproduced?
We study this question through a controlled
longitudinal paper-trading setting. Eighty partic-
ipants interact with real-time market information
and make simulated investment decisions using
non-redeemable virtual funds. The resulting tra-
jectories contain cross-scenario platform interac-
tions, executed paper trades, virtual portfolio states,
and contemporaneous market information. At each
arXiv:2609.15727v2  [cs.AI]  21 Sep 2026

prediction cutoff, the simulator receives only in-
formation observable before that time and predicts
the participant’s behavior on the next trading day.
This rolling design allows us to evaluate temporally
aligned individual decisions rather than aggregate
behavioral similarity alone.
Our analysis separates behavioral fidelity into in-
creasingly demanding levels. We first ask whether
the simulator predictswhetheran individual trades.
Conditional on trading, we examine whether it re-
covers the structure of the action, including buying,
selling, or both; which assets are involved; and
whether the resulting simulated decisions induce
a similar portfolio trajectory. This decomposition
is important because success at a coarse level need
not imply fidelity at a finer one. A model may re-
produce a user’s overall trading frequency while
trading on different days, correctly identify a trad-
ing day while selecting the wrong assets, or achieve
moderate action agreement while producing a sub-
stantially different economic trajectory.
We further distinguishbehavioral outcome fi-
delityfromdecision-process fidelity. Correct pre-
diction alone does not establish that the simulator
relies on the same information as the user. We
therefore intervene on the simulator’s input by with-
holding recent trading history, portfolio state, re-
cent platform behavior, market context, and long-
horizon profile information. These controlled ab-
lations reveal which evidence sources causally af-
fect the model’s predictions. We complement this
analysis with an observational study of real partici-
pant behavior, examining whether intensified ticker-
specific research precedes subsequent trading. Im-
portantly, we distinguish evidence that changes the
simulator’s prediction from evidence that is asso-
ciated with user behavior, and both from evidence
that can be identified as causally affecting the user’s
decision.
Our results reveal a substantial gap between
coarse behavioral similarity and individual deci-
sion fidelity. For trade occurrence, a simple recent-
activity persistence rule achieves performance com-
petitive with or stronger than the evaluated LLMs,
indicating that apparently strong next-action predic-
tion can largely reflect short-term behavioral mo-
mentum. Fidelity further deteriorates when recover-
ing buy–sell structure and traded assets. Moreover,
similar activity-level predictions do not necessarily
produce similar portfolio trajectories, demonstrat-
ing that agreement onwhethera user trades can
obscure important disagreement aboutwhatthe
user does.
The evidence analysis provides a complemen-
tary explanation. Removing recent trading history
causes a large degradation in trade-occurrence pre-
diction, whereas removing other evidence sources
has comparatively limited effects on the binary
activity decision. Asset predictions, in contrast,
change substantially when almost any evidence
group is withheld, suggesting a less stable asset-
selection mechanism. In the observed participant
trajectories, intensified ticker-specific research is
positively associated with imminent same-ticker
trading, but residual imbalance and placebo tests
prevent a causal interpretation. Together, these re-
sults suggest that current LLM simulators capture
predictive regularities in investor behavior more
reliably than they recover stable, asset-specific, or
causal decision mechanisms.
Contributions.Our contributions are threefold:
• We provide a longitudinal empirical study of
LLM-based financial user simulation under
strict point-in-time evaluation, separating be-
havioral fidelity across trade occurrence, ac-
tion structure, asset selection, and downstream
portfolio consequences.
• We identify a hierarchy of behavioral fidelity:
current LLMs can reproduce aspects of coarse
trading behavior, but agreement progressively
weakens for temporally aligned decisions,
buy–sell structure, asset selection, and in-
duced portfolio trajectories. We further show
that a simple recent-activity persistence rule
remains a strong baseline for trade-occurrence
prediction.
• We distinguish predictive dependence from
behavioral mechanism through controlled evi-
dence interventions and observational analy-
sis. Recent trading history strongly governs
the simulator’s activity prediction, whereas
asset-level predictions depend on a less sta-
ble combination of evidence; meanwhile, pre-
trade research activity predicts subsequent
trading without supporting causal identifica-
tion.
2 Task Formulation
Rolling Simulation Setting: Let i index investors
and t index U.S. equity trading days. For each tar-
get trading day t+1, we define the prediction cutoff

ct as the market close on day t. The simulator is
restricted to point-in-time information observable
at or beforec t:
Ii,t = (ui,t,h i,≤t−7,r i,t−6:t,p i,t,m t),(1)
where ui,t denotes the investor profile con-
structed from expanding historical records; hi,≤t−7
denotes long-term executed trading history pre-
ceding the recent window; ri,t−6:t denotes cross-
scenario behavior during the most recent seven trad-
ing days; pi,t denotes the portfolio state at the cut-
off; and mt denotes market information observable
through day t. Recent behavior includes transac-
tions, stock and portfolio views, news consumption,
and other in-platform interactions that may indicate
emerging investment intent.
Given this information, the simulator predicts
the investor’s structured action on the next trading
day:
ˆai,t+1 =f θ (Ii,t).(2)
All time-varying inputs are reconstructed inde-
pendently at each cutoff to ensure point-in-time
validity and prevent future information leakage.
During evidence-ablation experiments, derived rep-
resentations, including the investor profile, are re-
computed after the relevant source is removed to
prevent information from leaking across evidence
groups. Figure 1 illustrates the complete rolling
simulation framework.
3 Task Evaluation
We formulate personalized investor simulation as
a rolling-origin, hierarchical prediction problem.
At each prediction cutoff t, the simulator observes
only information available before t and predicts a
structured sequence of investor decisions: whether
the investor will trade, the trade direction, the assets
involved, the position-level changes, and the trans-
action scale. These decisions jointly determine the
predicted portfolio transition.
Our objective isbehavioral fidelityrather than
portfolio optimization. Unlike trading agents,
which are commonly evaluated by realized returns
or recommendation quality, a personalized investor
simulator should reproduce the decisions of the
particular investor it represents—including the de-
cision to abstain from trading—even when those
decisions are not financially optimal.
We evaluate fidelity along two complementary
dimensions. First,behavioral outcome fidelitymea-
sures how accurately the simulator predicts the in-
vestor’s realized actions under strictly temporal
evaluation. Second,decision-process fidelityexam-
ines whether the simulator recovers an investor-
specific decision policy rather than relying pri-
marily on population-level trading frequencies or
market regularities. We operationalize decision-
process fidelity by testing whether predictions re-
spond to investor-specific evidence, including his-
torical behavior, portfolio state, research activity,
and market context, and whether these sensitivi-
ties are consistent with the conditional patterns ob-
served in the investor’s actual decisions. We assess
such sensitivity through controlled input ablations
and counterfactual interventions rather than relying
on the model’s self-generated explanations.
3.1 Hierarchical prediction of investor
actions.
We formulate action simulation as a five-stage hier-
archical prediction task. Let the realized executions
on dayt+ 1be
Li,t+1 ={(j k, σk, nk)}Ki,t+1 k=1 ,(3)
where jk is the traded asset, σk ∈ {+1,−1}
indicates a buy or sell, and nk is the executed no-
tional. First, the simulator predicts whether the
investor trades:
ytrade i,t+1 =I[K i,t+1 >0].(4)
Conditional on trading, it predicts the day-level
action composition:
ydir i,t+1 ∈ {BUY,SELL,BUY&SELL}.(5)
TheBUY&SELLlabel represents portfolio re-
balancing in which both buy and sell transactions
occur on the same day. The simulator then ranks
the eligible assets and returns the top-k assets most
likely to be traded. For each selected asset, it pre-
dicts the corresponding position transition:
ypos i,t+1,j ∈ {START,ADD,TRIM,EXIT}.(6)
Here,STARTinitiates a new position,ADDin-
creases an existing position,TRIMreduces but re-
tains a position, andEXITcloses it. Finally, the sim-
ulator predicts the normalized signed trade scale

Figure 1: Overview of the rolling investor-simulation framework. At each cutoff ct, the simulator constructs a
point-in-time investor representation from the expanding profile, long-term trading history, recent seven-trading-day
behavior, current portfolio state, and contemporaneous market context. It then predicts the investor’s structured
action on the next trading day t+ 1 . All inputs are reconstructed using only information observable at or before the
cutoff.
ωi,t+1,j =
P
k σknkI[jk =j]
Vi,t
,(7)
where Vi,t is the portfolio value at the cutoff.
These predictions jointly determine the simulated
transaction-induced portfolio transition. The hier-
archical prediction process is summarized as
ytrade →y dir → S →ypos →ω.(8)
Here, the stages correspond to trade occurrence,
trade direction, asset selection, position transition,
and trade scale, respectively. Portfolio transition
is treated as an end-to-end outcome derived from
these five components rather than as an additional
prediction stage.
Evaluation.We evaluate trade occurrence, trade
direction, and position transition using accuracy
and macro-F1(Takahashi et al., 2022). Asset selec-
tion is evaluated using Hit@5(He et al., 2017, 2025)
and NDCG@5(Järvelin and Kekäläinen, 2002). We
report both stage-wise results, using ground-truth
outputs from preceding stages, and end-to-end re-
sults based entirely on the simulator’s predictions.
Asset selection is performed over a point-in-time
candidate set Ci,t containing current holdings, pre-
viously attended assets, and market-matched dis-
tractors. Target-day assets are not added based on
information observed after cutoffc t.
3.2 Evaluating investor-specific decision
policies.
Correctly predicting an action does not necessar-
ily imply that the simulator has recovered the in-
vestor’s decision policy. It may instead exploit
population-level trading frequencies, asset popular-
ity, or aggregate market regularities. We therefore
evaluate whether predictions depend on investor-
specific and decision-relevant evidence.
We organize the model input into five evidence
groups: investor profile, long-term trading history,
recent behavior, portfolio state, and market con-
text. For each group g, we compare the original
prediction with a controlled leave-one-group-out
prediction:
∆g =D

fθ(Ii,t), fθ(I (−g) i,t )  ,(9)
where I (−g) i,t removes evidence group g and
D(·,·) measures changes in predicted probabilities,
ranked assets, or discrete actions. We report proba-
bility shifts, action-flip rates, ranking changes, and
performance degradation under each intervention.
These experiments identify which evidence af-
fects the simulator’s outputs. They do not, how-
ever, establish that the same evidence causally de-
termines the real investor’s behavior. We therefore
refer to them asevidence-sensitivity probesrather
than causal identification.

Evaluation.For each prediction, the simulator
generates a structured natural-language explanation
that links the predicted action to evidence available
before the cutoff. The Sample is shown in the
Appendix??. We evaluate explanations from two
complementary perspectives. First, human annota-
tors assess(DeYoung et al., 2020):
1. Evidence grounding: whether the cited evi-
dence is present in the pre-cutoff record;
2. Investor specificity: whether the explanation
reflects the focal investor rather than generic
financial reasoning;
3. Decision consistency: whether the evidence
coherently supports the predicted action;
4. Historical plausibility: whether the explana-
tion is compatible with the investor’s previ-
ously observed decisions.
Second, we evaluate whether the model actually
relies on the evidence cited in its explanation. For
a cited evidence group g and predicted action ˆa, we
define interventional faithfulness as
Fg =s θ (ˆa| Ii,t)−s θ

ˆa| I(−g) i,t  ,(10)
where sθ is the model score assigned to ˆa. If
calibrated scores are unavailable, we instead report
whether removing the cited evidence changes the
predicted action or asset ranking. Human evalua-
tion measures whether an explanation is grounded,
specific, and plausible, whereas interventional faith-
fulness measures whether the prediction actually
depends on the cited evidence. Neither alone
demonstrates access to the investor’s unobserved
psychological process.
4 Experiments
We treat the current study as a pilot evaluation
aimed at characterizing the feasibility and fail-
ure modes of LLM-based financial user simula-
tion rather than establishing population-level per-
formance. Experimental details are provided in
Appendix A.
4.1 RQ1: How Faithful Are LLMs as
Financial User Simulators?
We evaluate simulator fidelity hierarchically. A
faithful financial user simulator must reproduce not
onlywhethera user trades, but also the structure
of the action, the assets involved, and ultimately
the economic consequences of those decisions. We
therefore organize the evaluation as
trade occurrence→side structure→asset selection→economic consequence
This decomposition is important because agree-
ment at an earlier layer does not necessarily imply
fidelity at the next.
LLMs capture trading propensity, but a sim-
ple persistence rule remains competitive.Across
1,239 confirmed user-days, 307 contain an ob-
served trade and 932 contain no trade, correspond-
ing to a real-user trade rate of 24.78%. The sim-
ulators exhibit markedly different activity biases.
Gemini-3-Flash-preview trades much more fre-
quently than the observed users, whereas GPT-5.6-
Sol is substantially more conservative. GPT-5.6-
Luna nearly reproduces the aggregate trade rate,
but aggregate agreement does not imply that the
model trades on the correct dates.
This distinction is reflected in Table 1. GPT-5.6-
Sol achieves the highest LLM accuracy, but does
so with low recall of actual trade days. Gemini-
3-Flash-preview shows the opposite behavior, re-
covering many more real trades at the cost of sub-
stantially more false positives. More importantly,
the recent-activity persistence baseline—which pre-
dicts a trade when the preceding trading day con-
tains an execution—achieves 79.82% accuracy and
0.714 macro-F1, exceeding all LLM point esti-
mates. Participant-level bootstrap comparisons do
not establish a reliable improvement of any LLM
over this simple behavioral rule.
The result suggests that a substantial component
of next-day trading behavior can already be ex-
plained by short-term activity persistence. A simu-
lator may therefore obtain apparently strong activ-
ity accuracy without recovering a richer model of
the user’s investment decision process.
Matching aggregate trading frequency does
not imply temporal fidelity.Figure 2(a,c) makes
the distinction visible. Some simulators system-
atically overpredict user activity, while others un-
derpredict it. GPT-5.6-Luna is particularly infor-
mative: its overall predicted trade rate is close to
the real-user rate, yet it still disagrees with the ob-
served action on many aligned dates. Consequently,
matching total activity can arise even when individ-
ual decisions occur at the wrong times.
The cumulative curves reinforce the same point.
Deviations compound in different directions across

Table 1: Trade-occurrence prediction (%) on 307 confirmed trade days and 932 confirmed no-trade days. The
recent-activity persistence baseline predicts a trade when the preceding trading day contains a recorded execution.
No LLM reliably improves over this simple behavioral baseline.
Model Accuracy Macro-F1 Trade recall No-trade recall Trade precision
Gemini-3-Flash 68.60 65.34 76.55 65.99 42.57
Gemini-3.5-Flash 75.06 68.94 61.89 79.40 49.74
GPT-4o-mini 76.11 69.32 58.63 81.87 51.58
GPT-5.6-Luna 78.05 71.23 59.28 84.23 55.32
GPT-5.6-Sol 79.18 66.24 34.85 93.78 64.85
Always no-trade 75.22 42.93 0.00 100.00 –
Recent-activity persistence 79.82 71.45 51.79 89.06 60.92
simulators, but even a curve that tracks the ob-
served total does not establish that the same days
were predicted correctly. Aggregate turnover agree-
ment is therefore a weak proxy for temporal behav-
ioral fidelity.
Trade detection does not imply recovery of
the action structure.Real trading behavior is also
more complex than a binary buy-versus-sell de-
cision. Among the 307 confirmed trading days,
109 are buy-only, 71 are sell-only, and 127 con-
tain both purchases and sales. Thus, simultaneous
buying and selling accounts for 41.4% of observed
trading days and is a substantial behavioral mode
rather than an edge case. We consequently treat
buy_and_sellas a distinct side class.
Recovering this structure remains difficult. The
strongest simulator correctly predicts the three-way
side on 129 of the 307 trading days (42.02%), only
slightly above the 41.37% majority baseline ob-
tained by always predicting buy_and_sell. Its
remaining errors arise through two different paths:
some trades are missed entirely at the activity stage,
while others are detected but assigned the wrong
side composition (Figure 2(b)).
The errors are also asymmetric across action
types. Sell-only days are particularly difficult to
recover, with end-to-end recall between 4.23% and
8.45% across the five models, whereas recall for
buy_and_sell ranges from 41.73% to 67.72%.
For the joint class, Gemini-3.5-Flash achieves the
strongest F1 (0.647), while GPT-5.6-Sol attains
higher precision but substantially lower recall. This
contrast indicates that models differ not only in
overall side accuracy, but also in how readily they
infer multi-action trading days.
Recognizing the action structure does not im-
ply recovering its assets.We next evaluate asset
selection conditionally on the observed side. A
trading day is counted once in side classification,
Table 2: Conditional ticker retrieval after restricting
model outputs to the candidate pool. Joint buy-and-sell
days contribute to both side-specific evaluation sets.
Model
Buy
Hit@5
Buy
NDCG@5
Sell
Hit@5
Sell
NDCG@5
Gemini-3-Flash40.70.25942.9 0.272
Gemini-3.5-Flash 39.00.260 42.90.265
GPT-4o-mini 37.7 0.247 27.8 0.164
GPT-5.6-Luna 35.2 0.22342.90.257
GPT-5.6-Sol 22.9 0.150 32.3 0.219
whereas a buy_and_sell day contributes to both
the buy-ticker and sell-ticker retrieval tasks. The
resulting evaluation sets contain 236 gold buying
days and 198 gold selling days, with the overlap
induced by the 127 joint buy-and-sell days.
Because the simulator contract returns at
most five tickers per side, we report Hit@5
and NDCG@5 in the main text. Table 2 re-
ports candidate-restricted rankings, keeping the
scored predictions consistent with the candidate-
generation contract.
Ticker recovery is substantially harder than de-
tecting that a user will trade. Even the strongest
Hit@5 values remain around 40–43%, meaning
that a model can correctly infer the occurrence or
structure of a trade while failing to recover the
assets that constitute the decision. The 127 joint
buy-and-sell days make this separation especially
clear: recognizing that a user will both buy and sell
is a different problem from reconstructing the two
corresponding ticker sets.
Candidate reachability is a separate bottle-
neck from asset selection.Ticker-level perfor-
mance also depends on whether the relevant asset
is available to the simulator in the first place. At
least one true bought ticker appears in the candidate
pool on only 73.31% of buying days, compared
with 91.92% of selling days. Moreover, 116 of the
236 buying days contain at least one gold ticker

Figure 2: Structural mismatch between real and simulated financial decisions. Simulators exhibit distinct activity
biases, and errors propagate from missed trades to incorrect side composition. Matching cumulative trading
frequency does not imply matching the timing or structure of the underlying decisions.
that is absent from the candidate pool.
Consequently, a ticker miss can arise before the
ranking stage: the correct asset may never have
been reachable. At the same time, imperfect can-
didate coverage does not explain the entire gap.
Candidate-restricted performance remains far be-
low the corresponding candidate oracle, indicating
substantial residual error even when useful assets
are available. The end-to-end ticker metric there-
fore reflects at least two distinct failure modes: can-
didate generation and downstream asset selection.
This distinction is important for interpreting sim-
ulator fidelity. A low ticker score does not neces-
sarily imply that the model ignored an available
asset, but a high candidate recall would also not
guarantee that the simulator could select the correct
asset once exposed to it.
Behavioral agreement does not guarantee eco-
nomic fidelity.The previous analyses evaluate dis-
crete behavioral decisions. We finally ask whether
behavioral similarity translates into similar portfo-
lio trajectories. We select three high-fidelity users
with sufficient observation coverage, trading activ-
ity, and end-of-day holdings changes to support a
meaningful comparison.
For each user, the simulated portfolio is initial-
ized as an exact copy of the real portfolio at the
first prediction cutoff. The simulated portfolio is
then updated using only the simulator’s predicted
buy and sell tickers. Trade sizes are calibrated from
that user’s historical behavior, and both real and
simulated portfolios are marked using the same
adjusted close prices. We therefore interpret the
resulting curves asdecision-attribution trajectories,
rather than realized P&L: they isolate the economic
consequences of different simulated decision paths
under a common accounting rule.
Figure 3 reveals that activity-level fidelity and
economic fidelity can diverge sharply. For Users
A and B, relatively strong behavioral agreement is
accompanied by similar terminal returns: the simu-
lated portfolios end within 0.82 and 1.86 percent-
age points of their corresponding real portfolios.
These cases show that the simulator can sometimes
recover a decision path with similar economic con-
sequences.
User C provides the more informative counterex-
ample. Despite an activity macro-F1 of 0.627,
the real portfolio returns +11.0% while the simu-
lated portfolio returns −8.37%, producing a 19.37
percentage-point gap. Thus, moderate agreement
onwhethera user trades can coexist with a qual-
itatively different economic trajectory when the
simulator does not recover the correct assets, direc-
tion, or position scale.
RQ1 takeaway.The results expose a hierarchy
of financial-simulator fidelity. LLMs can approxi-
mate broad user-level trading propensity, but appar-
ent agreement progressively weakens as the evalua-
tion moves fromwhethera user trades tohowthe
action is structured,which assetsare selected, and
what economic trajectorythose decisions induce.
In particular, strong activity accuracy can largely
reflect short-term behavioral persistence; matching
aggregate trading frequency does not imply correct
timing; recognizing a joint buy-and-sell action does
not imply recovering the corresponding assets; and
activity-level agreement can still produce substan-
tially different portfolio outcomes. Financial user
simulation should therefore be evaluated as a hier-
archy of behavioral decisions rather than as a single
next-action prediction problem.

Figure 3: Behavioral agreement does not necessarily translate into economic fidelity. Similar activity predictions
can produce similar portfolio paths (Users A and B), but can also mask substantial economic divergence when
asset-level decisions differ from the real ones (User C).
4.2 RQ2: Does the Simulator Recover User
Investment Logic?
We investigate whether an LLM-based user simu-
lator recovers the logic underlying a user’s invest-
ment decisions. We separate two questions that are
easily conflated. First, which behavioral evidence
actually governs the simulator’s next-action predic-
tion? Second, can an observable pre-trade behavior
be identified as a causal trigger of the user’s real
trading decision? The first concerns the decision
logic learned by the simulator, whereas the second
concerns the behavioral mechanism of the user. An
input may causally change the simulator’s predic-
tion without being a cause of the user’s behavior.
Recent trading history dominates the sim-
ulator’s activity decision.We first intervene
directly on the simulator’s information envi-
ronment through paired prompt ablations with
gpt-5.6-luna. For each user–date pair, we hold
the model, target date, prompt template, and de-
coding configuration fixed, while replacing one
evidence block with an explicitwithheldmarker.
We separately remove recent trade records, hold-
ings and portfolio changes, seven-day app behavior,
market context, and the long-horizon profile.
The resulting dependence is strongly asymmet-
ric. Removing recent trade records reduces ac-
tivity accuracy by 23.49 percentage points (95%
CI: [−33.00,−13.65] ), while no other evidence
block produces a reliable loss in activity accuracy.
This suggests that the simulator’s trade/no-trade
decision is anchored primarily inbehavioral per-
sistence: recent trading activity provides a strong
prior that the user will remain active. Holdings,
app interactions, market conditions, and the long-
horizon profile contribute comparatively little to
the binary decision of whether a trade occurs.
The simulator is more stable about when to
trade than what to trade.A different pattern
emerges at the asset level. Withholding any ev-
idence block changes more than half of the pre-
dicted ticker lists on gold-observed trade days, even
when the model’s trade/no-trade accuracy remains
nearly unchanged. The simulator can therefore
preserve its belief that a user will trade while sub-
stantially revising which asset the user is expected
to select.
This separation suggests that activity timing and
asset selection rely on different forms of inferred
user logic. The former is dominated by a relatively
stable short-term activity prior, whereas the latter
appears to be assembled from several partially re-
dundant signals. The simulator therefore captures
short-term behavioral momentum more robustly
than asset-specific investment logic. We do not
interpret the ablation effects additively, since the
evidence blocks overlap: portfolio changes may
partially reveal recent trading, and holdings and
market context contain related portfolio informa-
tion.
Research escalation marks an approaching
trade, but is not identified as its cause.We next

Table 3: Paired evidence ablation for simulator decisions. Removing recent trade records uniquely produces a
reliable loss in activity accuracy, whereas asset-level predictions remain sensitive to nearly every evidence source.
Negative∆accuracy indicates worse activity prediction relative to the paired full-information control.
Withheld evidence
∆accuracy
(pp) 95% CI
Activity
flip
Side
flip
Ticker-list
flip
Confidence
decrease
Recent trade records-23.49 [-33.00, -13.65] 36.5% 27.9% 76.6% 57.0%
Holdings and portfolio changes -1.40 [-3.98, 1.15] 7.0% 16.2% 58.6% 8.8%
7-day app behavior -0.23 [-2.16, 1.41] 4.4% 9.9% 56.8% 8.1%
Market context -1.16 [-3.20, 0.74] 4.0% 9.9% 57.7% 10.2%
Long-horizon profile -0.23 [-2.88, 2.14] 6.7% 12.6% 60.4% 8.4%
Figure 4: Evidence dependence of simulator decisions.
Recent trade history is uniquely important for deter-
mining whether a user will trade, whereas predicted
ticker lists remain sensitive to nearly every evidence
source. The contrast suggests that the simulator cap-
tures short-term activity momentum more reliably than
asset-specific investment logic.
move from the simulator’s internal dependence to
the user’s observed behavior. We ask whether a
concrete pre-trade action—an escalation in ticker-
specific research—can be interpreted as a trigger
of subsequent trading. We pre-specify an observa-
tional target-trial emulation at the user–ticker–date
level. Treatment is defined as a one-day escalation
into research following prior quote attention and
two no-research baseline sessions, and the outcome
is an executed same-ticker trade on the next trading
day.
The opportunity set is fixed before treatment and
contains held, viewed, or recently traded tickers.
We adjust for user, ticker, and date fixed effects
together with pre-treatment holdings, trading his-
tory, attention, portfolio state, and available market
features using IPW/MSM and AIPW estimators.
The primary risk set contains 15,125 opportunities,
including 395 treated opportunities from 80 users
over 21 dates.
Research escalation is positively associated with
imminent trading. The adjusted probability of a
next-day same-ticker trade increases by 3.94 per-
centage points, with similar positive associations
for both buys and sells. This makes intensified
ticker-specific research a useful behavioral marker
of an approaching investment decision.
The identification diagnostics, however, rule
out a causal interpretation. Although common
support is largely retained, post-weighting covari-
ate balance remains inadequate, with a maximum
weighted standardized mean difference of 0.324
relative to the pre-specified 0.10 threshold. More
importantly, the future-behavior placebo remains
positive (+5.12 pp; 95% CI: [1.58,10.07] ). These
failures are consistent with residual time-varying
confounding.
A plausible explanation is that an unobserved
increase in ticker-specific investment intent jointly
produces both additional research and the subse-
quent trade. Under this mechanism,
latent investment intent− →
 research escalation,
subsequent trade.
The observed temporal sequence of research fol-
lowed by trading therefore does not establish
research escalation− →trade.
Instead, research activity may be an observable
manifestation of a decision process that is already
underway. We consequently treat research escala-
tion as a temporally proximal behavioral marker
rather than an identified causal trigger.
The simulator recovers predictive logic, not
a complete causal decision mechanism.Taken
together, the two experiments expose different lev-
els of investment logic. The prompt intervention
shows that recent trading history causally governs
the simulator’s activity prediction, providing ev-
idence that the model has learned a meaningful
short-term behavioral dependency. However, its
ticker-level predictions are substantially more frag-
ile, suggesting that the model does not recover an
equally stable asset-selection mechanism.

Figure 5: Research escalation is positively associated with next-day same-ticker trading, but the identification
diagnostics do not support a causal interpretation. Residual covariate imbalance and a positive future-behavior
placebo indicate that intensified research is better viewed as a marker of an emerging trading decision than as an
identified trigger of that decision.
The observational analysis reveals a complemen-
tary limitation on interpreting the user’s behavior.
Ticker-specific research contains information about
imminent trading, but the available data do not es-
tablish that research itself causes the decision. We
therefore distinguish three increasingly demand-
ing notions of behavioral understanding:predictive
dependence, where an evidence source changes
the simulator’s prediction;behavioral association,
where an observable behavior precedes and predicts
real trading; andcausal mechanism, where inter-
vening on that behavior would change the user’s
decision. Our results provide evidence for the first
two, but not the third.
Thus, the simulator demonstrates partial under-
standing of investment logic: it captureswhenre-
cent behavioral momentum makes trading more
likely, but it is less reliable in recoveringwhatthe
user will trade, and the observational data are in-
sufficient to establishwhythe user ultimately acts.
5 Related Work
5.1 LLM as Human Simulator
Advances in large language models (LLMs) have
enabled increasingly realistic simulation of human
cognition and interaction across diverse domains,
including dialogue (Chan et al., 2023), recom-
mendation (Chen et al., 2026; Wang et al., 2025;
Zhang et al., 2024b), and autonomous driving (Jin
et al., 2024). Seminal works such as Generative
Agents (Park et al., 2023) and BASES (Ren et al.,
2024) further extend this paradigm to long-horizon
social behavior and web search. However, most ex-
isting user simulators are evaluated in controlled en-
vironments, synthetic sandboxes, or relatively sta-
ble interaction settings, leaving their effectiveness
in financial decision making largely unexplored. In
particular, prior work does not examine whether
LLM-based simulators can infer an investor’s la-
tent decision process and subsequent trading action
from heterogeneous behavioral signals under dy-
namically evolving market conditions. This gap
motivates benchmarks grounded in longitudinal
platform behavior and point-in-time market infor-
mation. To this end, we introduce a pilot financial
benchmark that jointly captures long-horizon paper-
trading behavior and market dynamics, enabling an
initial evaluation of LLM-based simulators in mod-
eling investor decision processes and predicting
next-step investment actions.
5.2 Financial Agent Application
Financial user simulation has evolved from rule-
based dialogue models to LLM-based investor
agents. Early work introduced user simulators
for personalized dialogue management in financial
product recommendation (den Hengst et al., 2019).
More recent studies, such as StockAgent (Zhang
et al., 2024a) and TwinMarket (Y ANG et al., 2025),
employ LLM-based agents to simulate investor
trading behavior under dynamic market conditions,
with TwinMarket further examining how individ-
ual trading decisions give rise to collective market
dynamics. Conv-FinRe (Wang et al., 2026b) con-
structs longitudinal financial recommendation sce-
narios from real market data and human decision
trajectories, highlighting the potential discrepancy
between observed investor behavior and underlying
utility. More recently, ShiJianBench (Gong et al.,

2026) introduces investor simulators with evolving
internal states to study how financial recommenda-
tions influence users’ subsequent investment deci-
sions over long horizons. However, existing studies
have not systematically investigated whether user
simulators reproduce individual, heterogeneous be-
havior across scenarios and over extended time
horizons.
6 Conclusion
We conducted a longitudinal empirical study
of LLMs as financial user simulators, examin-
ing whether apparent behavioral similarity re-
flects faithful reproduction of individual decision-
making. Our evaluation separates fidelity across
trade occurrence, action structure, asset selection,
and downstream portfolio consequences, and fur-
ther distinguishes predictive performance from the
evidence dependence underlying model decisions.
The results reveal a consistent hierarchy of be-
havioral fidelity. Current LLMs can capture aspects
of coarse trading propensity, but a simple recent-
activity persistence rule remains a strong baseline
for predicting whether an individual trades. Agree-
ment deteriorates further when recovering buy–sell
structure and traded assets, and similar activity-
level predictions can produce substantially differ-
ent portfolio trajectories. These findings show that
aggregate or coarse action agreement can substan-
tially overstate individual-level simulation fidelity.
Our evidence analysis further suggests that cur-
rent simulators recover predictive regularities more
reliably than stable decision mechanisms. Recent
trading history strongly influences activity predic-
tion, whereas asset selection is substantially more
sensitive to changes in the available evidence. Al-
though intensified ticker-specific research is associ-
ated with imminent trading in the observed partici-
pant trajectories, the available data do not support
interpreting this relationship causally.
Taken together, these results suggest that evalu-
ating LLM user simulators requires more than mea-
suring whether their outputs resemble observed ac-
tions. Behavioral fidelity should be assessed across
temporal alignment, decision structure, object-level
choices, and downstream consequences, while pre-
dictive dependence should be distinguished from
evidence about the causal mechanisms underlying
human behavior.
References
Chi-Min Chan, Weize Chen, Yusheng Su, Jianxuan Yu,
Wei Xue, Shanghang Zhang, Jie Fu, and Zhiyuan
Liu. 2023. Chateval: Towards better llm-based
evaluators through multi-agent debate.Preprint,
arXiv:2308.07201.
Jiawei Chen, Ruoxi Xu, Boxi Cao, Ruotong Pan, Yun-
fei Zhang, Yifei Hu, Yong Du, Tingting Gao, Yaojie
Lu, Yingfei Sun, Xianpei Han, Le Sun, Xiangyu Wu,
and Hongyu Lin. 2026. Towards real-world human
behavior simulation: Benchmarking large language
models on long-horizon, cross-scenario, heteroge-
neous behavior traces.Preprint, arXiv:2604.08362.
DeepSeek-AI, Anyi Xu, Bangcai Lin, Bing Xue, Bingx-
uan Wang, Bingzheng Xu, Bochao Wu, Bowei Zhang,
Chaofan Lin, Chen Dong, Chenchen Ling, Chengda
Lu, Chenggang Zhao, Chengqi Deng, Chengyu Hou,
Chenhao Xu, Chenze Shao, Chong Ruan, Conner
Sun, and 300 others. 2026. Deepseek-v4: Towards
highly efficient million-token context intelligence.
Preprint, arXiv:2606.19348.
Floris den Hengst, Mark Hoogendoorn, Frank van
Harmelen, and Joost Bosman. 2019. Reinforcement
learning for personalized dialogue management. In
IEEE/WIC/ACM International Conference on Web
Intelligence, WI ’19, page 59–67, New York, NY ,
USA. Association for Computing Machinery.
Jay DeYoung, Sarthak Jain, Nazneen Fatema Rajani,
Eric Lehman, Caiming Xiong, Richard Socher, and
Byron C. Wallace. 2020. ERASER: A benchmark to
evaluate rationalized NLP models. InProceedings
of the 58th Annual Meeting of the Association for
Computational Linguistics, pages 4443–4458, Online.
Association for Computational Linguistics.
Jie Gong, Maowei Jiang, Zhiwei Liu, Yang Qiao, Wenxi
Wu, Mengxi Xiao, Enze Zhang, Ziyan Kuang, Yankai
Chen, Caishuang Huang, Meng Zhou, Xiku Du, Xue
Liu, Guojun Xiong, Min Peng, Qianqian Xie, and
Sophia Ananiadou. 2026. Shijianbench: From di-
alogue to decision for long-horizon evaluation of
investment advisors.Preprint, arXiv:2608.01204.
Google DeepMind. 2025. Gemini 3 flash: Frontier
intelligence built for speed. Accessed: 2026-09-22.
Google DeepMind. 2026. Gemini 3.5 flash model card.
Accessed: 2026-09-22.
Jiajie He, Yuechun Gu, and Keke Chen. 2025. Recps:
Privacy risk scoring for recommender systems. In
Proceedings of the Nineteenth ACM Conference on
Recommender Systems, RecSys ’25, page 432–440,
New York, NY , USA. Association for Computing
Machinery.
Xiangnan He, Lizi Liao, Hanwang Zhang, Liqiang Nie,
Xia Hu, and Tat-Seng Chua. 2017. Neural collabo-
rative filtering. InProceedings of the 26th Interna-
tional Conference on World Wide Web, WWW ’17,
page 173–182, Republic and Canton of Geneva, CHE.

International World Wide Web Conferences Steering
Committee.
Kalervo Järvelin and Jaana Kekäläinen. 2002. Cumu-
lated gain-based evaluation of ir techniques.ACM
Trans. Inf. Syst., 20(4):422–446.
Ye Jin, Ruoxuan Yang, Zhijie Yi, Xiaoxi Shen, Huil-
ing Peng, Xiaoan Liu, Jingli Qin, Jiayang Li, Jintao
Xie, Peizhong Gao, Guyue Zhou, and Jiangtao Gong.
2024. Surrealdriver: Designing llm-powered genera-
tive driver agent framework based on human drivers’
driving-thinking data.Preprint, arXiv:2309.13193.
OpenAI. 2024. GPT-4o mini: advancing cost-efficient
intelligence. Accessed: 2026-09-22.
OpenAI. 2026. Gpt-5.6: Frontier intelligence that scales
with your ambition.
Georgios Th. Papadopoulos, Asterios Leonidis,
Margherita Antona, and Constantine Stephanidis.
2022. User profile-driven large-scale multi-agent
learning from demonstration in federated human-
robot collaborative environments. InHuman-
Computer Interaction. Technological Innovation,
pages 548–563, Cham. Springer International Pub-
lishing.
Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Mered-
ith Ringel Morris, Percy Liang, and Michael S. Bern-
stein. 2023. Generative agents: Interactive simulacra
of human behavior. InProceedings of the 36th An-
nual ACM Symposium on User Interface Software
and Technology, UIST ’23, New York, NY , USA.
Association for Computing Machinery.
Ruiyang Ren, Peng Qiu, Yingqi Qu, Jing Liu,
Wayne Xin Zhao, Hua Wu, Ji-Rong Wen, and
Haifeng Wang. 2024. BASES: Large-scale web
search user simulation with large language model
based agents. InFindings of the Association for Com-
putational Linguistics: EMNLP 2024, pages 902–
917, Miami, Florida, USA. Association for Compu-
tational Linguistics.
Kanae Takahashi, Kouji Yamamoto, Aya Kuchiba, and
Tatsuki Koyama. 2022. Confidence interval for
micro-averaged F1 and macro-averaged F1 scores.
Applied Intelligence, 52(5):4961–4972.
Haoting Wang, Haokai Lu, Zheyun Feng, Jenny Huang,
Yifat Amir, Gregory Hinkson, Ben Most, Zelong
Zhao, Yixin Kelly Cui, Rein Zhang, Fabio Soldo,
Yu Xia, Nihar Bhupalam, Minmin Chen, Konstantina
Christakopoulou, Lichan Hong, and Ed H. Chi.
2026a. Llm-based user personas for recommenda-
tions at scale.Preprint, arXiv:2606.12198.
Lei Wang, Jingsen Zhang, Hao Yang, Zhi-Yuan Chen,
Jiakai Tang, Zeyu Zhang, Xu Chen, Yankai Lin, Hao
Sun, Ruihua Song, Xin Zhao, Jun Xu, Zhicheng Dou,
Jun Wang, and Ji-Rong Wen. 2025. User behavior
simulation with large language model-based agents.
ACM Trans. Inf. Syst., 43(2).
Yan Wang, Yi Han, Lingfei Qian, Yueru He, Xueqing
Peng, Dongji Feng, Zhuohan Xie, Vincent Jim Zhang,
Yuqing Guo, Fengran Mo, Jimin Huang, Yankai
Chen, and Jian-Yun Nie. 2026b. Conv-finre: A con-
versational and longitudinal benchmark for utility-
grounded financial recommendation. InProceedings
of the 49th International ACM SIGIR Conference on
Research and Development in Information Retrieval,
SIGIR ’26, page 3448–3455, New York, NY , USA.
Association for Computing Machinery.
Yuzhe Y ANG, Yifei Zhang, Minghao Wu, Kaidi Zhang,
Yunmiao Zhang, Honghai Yu, Yan Hu, and Benyou
Wang. 2025. Twinmarket: A scalable behavioral and
social simulation for financial markets. InAdvances
in Neural Information Processing Systems, volume
38, Main Conference, pages 63469–63519. Curran
Associates, Inc.
Chong Zhang, Xinyi Liu, Zhongmou Zhang, Mingyu
Jin, Lingyao Li, Zhenting Wang, Wenyue Hua, Dong
Shu, Suiyuan Zhu, Xiaobo Jin, Sujian Li, Mengnan
Du, and Yongfeng Zhang. 2024a. When ai meets
finance (stockagent): Large language model-based
stock trading in simulated real-world environments.
Papers 2407.18957, arXiv.org.
Junjie Zhang, Yupeng Hou, Ruobing Xie, Wenqi Sun,
Julian McAuley, Wayne Xin Zhao, Leyu Lin, and Ji-
Rong Wen. 2024b. Agentcf: Collaborative learning
with autonomous language agents for recommender
systems. InProceedings of the ACM Web Conference
2024, WWW ’24, page 3679–3689, New York, NY ,
USA. Association for Computing Machinery.
A Experimental Setting
A.1 Baselines
We evaluate a diverse set of representative LLMs,
including both proprietary and open-weight models.
The proprietary models the GPT series (GPT-5.6
Sol(OpenAI, 2026), GPT-5.6 luna (OpenAI, 2026)
and GPT-5.4o-mini(OpenAI, 2024)), and the Gei-
mini series (Geimini-3-Flash(Google DeepMind,
2025) and Geimini-3.5-Flash(Google DeepMind,
2026))
A.2 DataSet
Data SourceUsing real brokerage records for re-
search can raise substantial privacy, regulatory,
and data-governance concerns. We therefore con-
structed a controlled paper-trading environment
and did not access participants’ real brokerage ac-
counts, money holdings, credentials, or transaction
records.
We recruited 80 volunteer participants. Partic-
ipants could buy, sell, rebalance, or remain inac-
tive at their discretion under real-time market con-
ditions. Orders were simulated exclusively with

non-redeemable virtual funds and had no effect on
participants’ real assets, brokerage accounts, or fi-
nancial positions. We recorded the resulting paper-
trading trajectories over a three-month observation
period.
Privacy ProtectionAlthough the platform did
not collect real brokerage data, the resulting in-
teraction logs constitute participant-generated be-
havioral data. We therefore de-identify all data
used for analysis and release. A locally deployed
DeepSeek-V4-Flash model (DeepSeek-AI et al.,
2026) assists in detecting personally identifiable
information in any free-text or account-associated
fields. Detected identifiers are replaced with stan-
dardized placeholders (e.g., [NAME] and [AGE]).
We then conduct manual quality assurance before
releasing the processed dataset. No raw identifiers,
real account credentials, money positions, and bro-
kerage transactions are included in the released
data.
Construction PipelineWe collected data from
80 volunteers using thePaper Tradingplatform,
comprising 230K+ interactions. The data span
multiple financial scenarios, including market-
information and news browsing, stock/ETF view-
ing, simulated trading activity, virtual portfolio
states, and interactions with the platform chatbot.
Data ProcessingWe clean duplicated, incom-
plete, and noisy records and organize all interac-
tions into unified chronological behavior sequences.
For each user, earlier historical behaviors are fur-
ther used to construct a financial profile capturing
relatively stable characteristics such as investment
preferences, trading patterns, and portfolio charac-
teristics. For viewed financial news, we clean the
original text and useDeepSeek-V4(DeepSeek-AI
et al., 2026) to generate concise summaries, which
are inserted into the corresponding positions of the
behavior sequence.
User Diversity.To preserve behavioral hetero-
geneity, our dataset includes both active and inac-
tive participants with diverse paper-trading styles,
including high-risk trading and long-term invest-
ing. Participants also vary in financial experience,
ranging from experienced market participants to
non-professional retail investors.
B User Profile Construction
We construct a cutoff-safe user profile with a
staged multi-agent pipeline(Wang et al., 2026a; Pa-
padopoulos et al., 2022). The profile is intended
Figure 6: Cutoff-safe multi-agent user-profile construc-
tion. Raw pre-cutoff records are normalized and con-
verted into deterministic features, analyzed by role-
specific agents, checked for conflicts, and synthesized
into a versioned base profile.
to represent a participant’sobservable behavioral
history, rather than unobserved psychological traits
or ground-truth investment preferences. Figure 6
summarizes the construction process.
Evidence collection and normalization.For
each participant and prediction cutoff ci,t, a
data-structuring agent collects and normalizes all
records available before the cutoff. The evidence
streams include interaction events (e.g., viewing,
checking, reading, searching, and switching views),
executed trades, portfolio snapshots, daily account
states, and conversation records. Records are
aligned by participant and timestamp, and target-
day or post-cutoff information is excluded before
any downstream agent is called.
Deterministic feature computation.A feature-
aggregation module converts the normalized
records into auditable behavioral statistics. These
include the number of events, active days, interac-
tion frequencies, executed-trade counts, buy and
sell amounts, observed net direction, asset con-
centration, portfolio changes, and holding-related
summaries. These quantities are computed directly
from the underlying records and are not generated
by an LLM.
Specialized analysis agents.The structured ev-
idence is then routed to role-specific agents with
restricted evidence views. A risk-analysis agent
examines observable risk-related behavior, includ-
ing transaction intensity, trade scale, asset concen-
tration, drawdown, and portfolio volatility. An
investment-logic agent integrates cross-source sig-
nals from behavior, trades, holdings, assets, and
interactions to characterize the participant’s appar-

ent investment logic. Additional agents analyze
investment goals, short-term trading behavior, and
long-term holding patterns. Each agent produces
evidence-linked conclusions together with uncer-
tainty or missing-evidence indicators.
Validation and profile synthesis.A conflict-
checking agent compares the outputs of the special-
ized agents and flags inconsistent, unsupported, or
overconfident statements. A profile-writing agent
then synthesizes the validated outputs into a struc-
tured profile containing (i) a concise overview,
(ii) dimension-level summaries, (iii) evidence-
grounded highlights, and (iv) explicit caveats.
Missing observations remain unknown and are not
converted into negative behavioral claims.
Temporal versioning and model-facing repre-
sentation.The profile is versioned by participant
and cutoff. As the observation history expands, a
new profile snapshot is generated using only evi-
dence available at the new cutoff. The simulator
receives the versioned profile together with sepa-
rate short-horizon behavior, portfolio, and market-
context blocks. Thus, the long-horizon profile cap-
tures persistent observable patterns, whereas the
rolling short-horizon blocks capture recent condi-
tions relevant to the next decision.
