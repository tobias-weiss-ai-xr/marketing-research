---
title: 'FACTS-MAS: A Multi-Agent Architecture for Adaptive Forecasting from Heterogeneous Evidence'
url: https://arxiv.org/abs/2610.38225
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Madumita Karthikeyan
- Umang Rajnikant Bid
- Rong Pan
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.38225
pages: 29
chars: 101133
fetched_at: '2026-11-08T13:35:57+00:00'
kb_version: 1
---

# FACTS-MAS: A Multi-Agent Architecture for Adaptive Forecasting from Heterogeneous Evidence

FACTS-MAS: A Multi-Agent Architecture for
Adaptive Forecasting from Heterogeneous Evidence
Madumita Karthikeyan
mkarthi5@asu.edu
Umang Rajnikant Bid
umangraj@asu.edu
Rong Pan
rong.pan@asu.edu
October 30, 2026
Abstract
Real-world forecasting often requires integrating heterogeneous evidence whose predictive value varies
across horizons, operating regimes, and domains. We introduce FACTS-MAS, a domain-agnostic multi-
agent forecasting framework that decomposes evidence into specialized channels for temporal dynam-
ics, exogenous context, seasonality, structural information, and discrete events. Each agent gener-
ates an independently testable forecast through a common interface, while leakage-safe historical val-
idation measures its predictive skill relative to a naive reference. These skill estimates are used to
weight and combine agent forecasts, so that uninformative evidence is either removed or downweighted
rather than forced to participate. A calibration procedure selects domain-specific constant means based
on historical validation folds. We evaluate FACTS-MAS on weekly for-sale housing inventory from
Zillow and weekly unemployment insurance claims from FRED, for 15 U.S. metropolitan areas at
4-, 8-, and 13-week forecasting horizons. Our method outperforms both a naive last-value forecast
method and the TimesFM foundation model. However, a factor-adjusted exponential smoothing model
performs as well as the fused forecast. The evidence therefore supports FACTS-MAS as a system-
atic protocol for testing, calibrating, and recomposing evidence channels, before assembling them to
the strongest single model for a specific application domain. Code, data, and results are available at
https://github.com/Madumita24/FACTS-MAS.
1 Introduction
Forecasting in operational settings almost always draws on more than one kind of information. A target
series may be strongly autoregressive, yet its near-term path can also depend on exogenous conditions,
recurring seasonal cycles, slowly varying attributes of the entity being forecast, and discrete events that do
not arrive as ordinary numerical features. These information sources differ in representation, timing, and,
most importantly, predictive value. A signal that helps at a short horizon or in one regime may add nothing
at a longer horizon or in another domain.
A common approach in forecasting is to fold all available inputs into a single statistical/machine-learning
(ML) model or a single artificial intelligence (AI) reasoning process. This forecasting approach may be
able to capture complex interactions among different information sources, but it binds three tasks into one
object: how each source is encoded, how the forecast is produced, and how credit is assigned to each
source. When the forecast accuracy has changed, it is difficult to identify whether the change came from
temporal dynamics, external context, structure, or events. It also requires dissimilar information sources to
be translated into a single input format, even though time-series dynamics, calendar effects, static covariates,
and unstructured events are not naturally expressed in the same way.
In this paper, we develop a new approach, Forecasting from Adaptive, Calibrated, Testable Sources –
Multi-agent AI System (FACTS-MAS), which is built upon the opposite premise. We define AI agents by
1
arXiv:2610.38225v1  [cs.AI]  28 Oct 2026

theirfunctional evidence roles, not by an application name. Each agent turns the evidence in its channel
into a numerical forecast that satisfies a common output contract. The fusion step then asks a focused
question:does this channel improve on a simple reference forecast in leakage-safe historical validation?
We quantify the relative skill of each agent for the targeted forecasting task as a weight; weak or redundant
channels are downweighted rather than forced to participate. Domain-specific constants like event-impact
scales, event durations, and reversion caps are chosen by the same validation test, and these constants can
be set to zero. This changes the interpretation of negative results. If an agent receives little weight, it is
not necessarily a failed component; instead, it is evidence that the channel it is managing contains little
incremental information for the current domain, or that the present implementation does not extract the
useful information. Likewise, a plausible causal event may in fact have little predictive power in one domain,
but we can keep it and assign it a confidence score for later domains.
We evaluate FACTS-MAS on the forecast of weekly U.S. housing inventory, a setting in which all five
candidate channels can be populated: recent inventory dynamics, national financial conditions, annual listing
seasonality, metropolitan structure, and disaster declarations. The study covers 15 metropolitan statistical
areas (MSAs) at forecast horizons of 4, 8, and 13 weeks. At each forecast origin, defined as the week in
which a prediction is issued, models are trained only on observations dated on or before that week; because
Zillow publishes each week’s value one to two weeks later, we also report every result with a two-week
publication lag. Evaluation uses a six-fold expanding-window backtest, with a 13-week embargo between
the end of training and the start of testing, followed by a single pre-registered holdout on data after February
21, 2026 that was not accessed until the configuration was frozen. On Zillow’s smoothed inventory series,
the frozen configuration reduces MAPE relative to a naive last-value forecast from 4.194% to 2.118% at
the 4-week horizon, from 7.225% to 3.622% at 8 weeks, and from 10.814% to 5.731% at 13 weeks in
the backtest, and from 3.122% to 1.243%, 5.445% to 1.929%, and 8.438% to 3.045% on the holdout. The
reduction is smaller on the unsmoothed series (24% at 4 weeks in the backtest, against 50% on the smoothed
series). The fused forecast is significantly more accurate than the TimesFM foundation model [Das et al.,
2024] in the backtest. On the holdout it has a lower error than a chain-of-thought language-model forecast
built on the NEXUS prompt [Das et al., 2026], but the difference is not statistically significant. It is not
more accurate than a factor-adjusted damped exponential smoothing model, with which it is statistically
equivalent at 8 weeks. We also transfer the method to weekly unemployment insurance claims to assess the
generalizability of the approach.
The contributions of this paper are as follows.
1. We introduce FACTS-MAS, a multi-agent forecasting procedure that assigns heterogeneous evidence
to functional channels—temporal, exogenous, seasonal, structural, and event-based—and requires each
agent to return a numerical forecast under a common output contract.
2. We develop a leakage-safe fusion rule that measures each agent’s improvement over a naive reference,
aggregates that skill by the median, and converts the resulting scores into fusion weights. The weights
may depend on forecast horizon and operating regime when the validation sample is sufficient to sup-
port that conditioning; a regime is used only when it contains at least 13 distinct validation weeks, and
otherwise the pooled weights apply.
3. We specify a calibration procedure for domain-specific constants, including event-impact scales, event
durations, and reversion caps. Candidate values are selected on historical validation folds, and a constant
may be set to zero when validation does not support a nonzero effect.
4. We evaluate the method on weekly for-sale housing inventory for 15 U.S. metropolitan areas at forecast
horizons of 4, 8, and 13 weeks, on both Zillow’s smoothed and unsmoothed series. The analysis com-
pares accuracy with naive, seasonal-naive, and seasonally adjusted naive references, with exponential-
2

smoothing and Theta models, with the TimesFM foundation model, and with a chain-of-thought language-
model forecast, using panel Diebold–Mariano tests and block-bootstrap confidence intervals. It distin-
guishes evidence channels that add incremental skill from channels whose quantitative effect is weak or
unsupported.
5. We report a pre-registered evaluation: the configuration, the hypotheses, and the statistical tests were
fixed and committed before a holdout period of 29 weekly origins was accessed, and every result on that
holdout is reported, including those that do not favor the fused forecast.
The remainder of the paper is organized as follows. Section 2 reviews multi-agent forecasting, the
evolution of forecasting models, forecast combination, and the NEXUS precursor. Section 3 defines the
FACTS-MAS procedure, including the evidence channels, the shared forecast interface, skill-based fusion,
calibration, and attribution. Section 4 states the rolling-origin protocol, the information boundary, the ac-
curacy metrics, and the comparison design, then instantiates the method for U.S. housing inventory and
reports forecast accuracy together with the channel and fusion diagnostics. Section 5 discusses the housing
findings, including the holdout results, and the transfer of the method to weekly unemployment insurance
claims. Section 6 concludes.
2 Related Work
FACTS-MAS draws on four lines of research: multi-agent forecasting, the succession of time-series model
classes, the combination of heterogeneous evidence, and LLM-assisted interpretation of unstructured infor-
mation. This section reviews each line and states how FACTS-MAS differs.
2.1 Multi-Agent and LLM-Assisted Forecasting
Multi-agent systems decompose a complex prediction task into specialized components whose outputs are
orchestrated or aggregated [Chang et al., 2025, Wang et al., 2024]. Large language models have widened this
pattern: agents can interpret text, call tools, plan, and communicate over mixed structured and unstructured
inputs [Yao et al., 2023, Jang et al., 2026]. Recent agentic forecasting systems organize those capabilities
into workflows—planning, tool use, iterative revision, and ensemble generation—rather than a single-pass
map from history to the future [Tao et al., 2026, Pan et al., 2026]. Role-specialized designs give agents
distinct duties and pass intermediate results through conversation or a shared workflow [Park et al., 2023,
Wu et al., 2024, Hong et al., 2024].
However, specialization alone does not establish that every agent adds predictive information. Two
agents may encode the same signal, a plausible feature family may have no out-of-sample benefit, and
usefulness may depend on the forecast horizon or the operating regime. When agents only converse, their
individual numerical contributions cannot be isolated. FACTS-MAS differs by requiring each agent to issue
its own numerical forecast and by measuring that forecast’s skill relative to a simple reference before fusion
assigns it any weight. The skill measurement may depend on the forecast horizon and the operating regime
when the validation sample is sufficient.
2.2 From Statistical Models to Foundation Models
Time-series forecasting has moved through several model classes that remain useful as channel implementa-
tions or as baselines. Exponential smoothing, including the Holt–Winters trend form, forecasts from a local
level and trend [Holt, 2004, Winters, 1960, Hyndman et al., 2002, Pan, 2011]. Additive statistical models of
the same family are widely used in practice [Taylor and Letham, 2018]. Large competitions then compared
3

these statistical methods with later machine-learning entries on common collections of series [Makridakis
and Hibon, 2000, Makridakis et al., 2020]. The M4 winner combined exponential smoothing with a re-
current network [Smyl, 2020]. Global neural forecasters fit one model to many related series, including
autoregressive recurrent networks [Salinas et al., 2020], residual basis expansions [Oreshkin et al., 2020],
and attention models that also accept covariates [Lim et al., 2021]. Lim and Zohren [2021] survey this
deep-learning line.
Transformer forecasters adapted attention to long horizons [Zhou et al., 2021, Wu et al., 2021, Nie
et al., 2023], and Wen et al. [2023] survey that design family. Subsequent comparisons showed that simple
linear models can match or beat several of those architectures [Zeng et al., 2023]. Pretrained foundation
models now produce zero-shot forecasts across domains, including TimesFM [Das et al., 2024], Chronos
[Ansari et al., 2024], and Moirai [Woo et al., 2024]. Those zero-shot forecasts can still carry variance and
systematic bias. Bootstrap aggregation, regression stacking, and residual correction of a foundation-model
forecast have reduced both on an operational electricity-load series [Modi and Pan, 2025]. A parallel line
asks a language model to forecast, either by reprogramming a frozen model [Jin et al., 2024] or by encoding
the series as text [Gruver et al., 2023]. FACTS-MAS does not replace this sequence of forecasters. A
channel may use a statistical smoother, a regression, or a pretrained model. The housing study uses Holt’s
linear-trend exponential smoothing on the temporal channel at the 4-week horizon and a factor-adjusted
damped-trend model [Gardner and McKenzie, 1985] at 8 and 13 weeks, and it uses TimesFM 2.5, a later
checkpoint of the TimesFM line, as a numerical baseline.
2.3 Heterogeneous Evidence and Forecast Combination
Operational forecasting problems commonly pool evidence with heterogeneous statistical structure: en-
dogenous dynamics, exogenous covariates, calendar effects, slowly varying entity attributes, and discrete
events. Recurrent events can be forecast through the cumulative intensity of the event process, includ-
ing with boosted trees that use both static and dynamic features [Liu and Pan, 2021]. A joint statistical
or machine-learning model maps this collection to a single forecast, so that input encoding, prediction,
and source-level attribution are determined by one fitted mapping. Forecast combination retains a separate
forecast for each source and aggregates those forecasts. Equal-weight aggregation reduces dependence on
any one specification [Clemen, 1989]. Performance-based weights assign greater influence to component
forecasts with lower historical error [Bates and Granger, 1969]. Regression on the component forecasts is
another classical route to those weights [Granger and Ramanathan, 1984, Stock and Watson, 2004]. Static
weights assume that relative accuracy is sufficiently stable to be pooled across time [Newbold and Granger,
1974, Wang et al., 2023]. Timmermann [2006] reviews when such combination improves on the best indi-
vidual forecast. That question is central here: a combination of channels is only useful if it improves on the
strongest single model that could have been selected on the same validation data. A related prediction task
is degradation under a time-varying environment, where an ensemble is trained to follow that change [Wang
et al., 2020].
FACTS-MAS uses rolling weights based on each agent’s skill relative to a simple reference forecast.
The skill score, its median aggregation, and the softmax conversion are defined in Section 3. Whether those
weights should also depend on forecast horizon or operating regime is treated there as a validation choice,
because finer conditioning is estimated from fewer observations.
2.4 Calibration and NEXUS
Plausible numerical assumptions—event-severity maps, effect durations, lags, and thresholds—can degrade
forecast accuracy even when the underlying causal mechanism is plausible. FACTS-MAS selects such
4

constants on historical validation folds and allows a constant to be set to zero when a nonzero effect is
unsupported. The calibration rule is given in Section 3.
The immediate precursor of our MAS approach is NEXUS [Das et al., 2026], which forecasts from
mixed structured and unstructured evidence by passing that evidence through multi-agent language-model
reasoning and then issuing the forecast. Efficiency extensions of that design, such as early-exit gating
and batched reasoning, retain language-model reasoning on the main forecasting path; they are not part of
FACTS-MAS and are not evaluated here. FACTS-MAS assigns the same evidence to specialized channels
and obtains an independent numerical forecast from each channel. The fusion weights are estimated from
the channels’ historical skill relative to a simple reference on a validation window that ends at the training
cutoff, and they are re-estimated whenever the training window is extended. Those weights may also depend
on the forecast horizon and the operating regime when the validation sample is sufficient.
The housing experiments in Section 4.2 compare FACTS-MAS with a chain-of-thought language-model
forecast that uses the NEXUS prompt, with a time-series foundation model, and with strong statistical
references. Those comparisons test the forecasting consequence of this decomposition.
3 FACTS-MAS: Domain-Agnostic Forecasting Architecture
FACTS-MAS separates a reusable forecasting procedure from any one domain’s data and models. The
appropriate raw variables, predictive models, event types, and operating regimes may depend on the domain,
but the forecasting procedure remains the same. Heterogeneous evidence is digested and fed into forecasting
channels; each channel produces an independently evaluable forecast, and these forecasts are combined
adaptively.
Lety t denote the target variable observed up to forecast origint, and letHdenote the requested forecast
horizon. LetI t denote the information available at that origin. For a forecasting domainD, this information
is streamed intoKfunctional evidence channels,
E (D) = n E(D) 1 , E(D) 2 , . . . , E(D) K o .(1)
E(D) k denotes the channel, and each channel is assigned one agent. The assigned agent reads that channel
and maps the available information to a horizon forecast,
fk :I t → ˆyk, k= 1, . . . , K,(2)
where ˆyk is the forecast over the requested horizon. In a named domainD, the agent isA k,
Ak :I (D) t → ˆy(H) k,t ,(3)
where ˆy(H) k,t = [ˆyk,t+1, . . . ,ˆyk,t+H ]is theH-step forecast produced independently by agentk.
These maps determine the forecast. At each forecast origin, domain evidence is assigned to theK
channels, and each agent returns an independent forecast. A validation step scores each agent’s historical
forecasts against a reference, the resulting skill scores set the fusion weights, and adaptive fusion combines
the agent forecasts into ˆyF ACTS. Calibration is a separate, offline step that selects channel constants on
historical validation folds before the test period begins.
Figure 1 shows this procedure at one forecast origin. The following subsections describe the compo-
nents of this process and identify which elements remain invariant across domains and which need to be
reconfigured for specific forecasting tasks.
5

Figure 1: FACTS-MAS at one forecast origin. Each evidence channel returns an independent horizon
forecast. Skill relative to a naive reference, measured on a validation window that ends at the training cutoff,
sets the fusion weights. Calibration acts offline on channel constants and may set a constant to zero.
3.1 Functional Evidence-Channel Decomposition
FACTS-MAS organizes forecasting evidence according to its functional role rather than according to a
particular dataset or application. The current architecture defines five candidate evidence channels:
1.Temporal channel.It models the endogenous dynamics of the target using its historical trajectory.
This channel captures stability, trend, autocorrelation, and other temporal structure that can be estimated
without external information.
2.Exogenous channel.It represents external numerical variables that may influence future changes in the
target. The identity and transmission lag of these variables are domain dependent.
3.Seasonal channel.It represents recurring temporal structure associated with calendar, periodic, or cyclic
behavior.
4.Intrinsic or structural channel.It represents relatively persistent characteristics of the entity being
forecast. These features may distinguish entities even when they share similar recent temporal trajecto-
ries.
5.Event channel.It represents discrete or unstructured information whose forecasting relevance may
require semantic interpretation before it can be converted into a structured signal.
These channels arefunctional abstractions, not fixed feature sets. For example, the exogenous channel
may contain monetary-policy indicators in a housing application, weather and demand drivers in an energy
6

application, or labor-market indicators in an employment application. Similarly, the meaning of a relevant
event depends on the target domain.
This distinction is central to domain transfer. FACTS-MAS does not assumeE (D1) k =E (D2) k . Instead, it
assumes that both domains can expose evidence serving comparable forecasting functions,E (D1) k ∼E (D2) k
with respect to functional role, while allowing their data sources, features, transformations, and agent im-
plementations to differ.
3.2 Shared Agent Interface
To keep evidence-channel implementation separate from downstream fusion, every forecasting agent must
satisfy a common output contract. For a given forecast request, an agent returns
Ok = (ak, d, t, H,ˆyk,c k),(4)
wherea k identifies the agent,didentifies the entity or forecasting unit,tis the forecast origin,His the
requested horizon, ˆyk contains exactlyHforecast values, andc k optionally contains horizon-specific con-
fidence values.
This output contract enforces three important invariants. First, all agents must produce forecasts for
the same entity, origin, and requested horizon before fusion. Second, the output length must exactly match
the requested horizon. Third, target forecasts must satisfy domain-valid output constraints; for the housing
implementation, for example, inventory forecasts are constrained to be non-negative.
The shared contract allows an agent implementation to be replaceable without modifying the fusion
layer. A statistical model, machine-learning model, foundation time-series model, or LLM-assisted seman-
tic embedding model can therefore occupy an evidence channel as long as its output satisfies the same
forecasting interface.
3.3 Leakage-Safe Agent Evaluation
The quality of a forecasting agent is estimated using its historical forecasts generated under the same infor-
mation constraints that would exist during deployment. For each forecast origint, an agent may access only
evidence available on or before that origin after accounting for publication and availability delays.
For an agentkand reference modelb, define the absolute percentage errors at validation pointias
ek,i = |yi −ˆyk,i| |yi| , e b,i = |yi −ˆyb,i| |yi| .(5)
FACTS-MAS measures incremental forecasting skill relative to the reference,s k,i = 1−e k,i/eb,i. Thus,
sk,i



>0,agent improves on the reference,
≈0,agent approximately matches the reference,
<0,agent underperforms the reference.
(6)
Skill is scored against the persistence baseline, so an agent that only reproduces that baseline receives a skill
near zero.
Directly averaging the pointwise skill ratios can be unstable when the reference error is extremely small
at individual validation points. FACTS-MAS therefore aggregates pointwise skill using the median,
˜sk = mediani∈V (sk,i),(7)
whereVdenotes the leakage-safe validation window. The median reduces the influence of isolated points at
which an unusually small reference error would otherwise produce an extreme ratio.
7

3.4 Skill-Based Adaptive Fusion
The validated skill scores are converted into non-negative normalized weights using a temperature-controlled
softmax,
wk = exp(˜sk/τ)PK
j=1 exp(˜sj/τ)
,(8)
whereτ >0controls how strongly differences in historical skill affect the final allocation. In the housing
configurationτ= 0.05. This value was set by hand from the magnitude of validation skill scores, not
selected by a search; a validation-selected temperature was tested and not adopted (Section 5.1.5).
The fused forecast is then
ˆy(H) F ACTS,t=
KX
k=1
w(H) k,t ˆy(H) k,t .(9)
Softmax weighting is useful in this setting because it preserves the complete ranking of agents, including
agents with negative relative skill. No hard threshold is required to assign identical minimum weights
to all underperforming channels. An agent that is slightly worse than the reference can therefore remain
distinguishable from an agent that is substantially worse.
Weights are re-estimated whenever the training window is extended rather than fixed once for the entire
evaluation period. In the backtest, each fold estimates its weights from a 104-week validation window
ending at the training cutoff and holds them fixed over that fold’s test window. Consequently,w(H) k,t1 ̸=w (H) k,t2
is permitted across folds, and within a fold whent 1 andt 2 fall in different regimes.
3.5 Adaptive Context and Regime Conditioning
The relative value of an evidence channel may depend on both forecast horizon and operating context.
FACTS-MAS therefore supports multiple levels of conditioning.
Letr t denote a domain-specific regime observed at forecast origint. The regime variable itself is
not part of the invariant framework. It is a domain-specific configuration satisfying two requirements: it
must represent a meaningful state for the target process, and its value at forecast origintmust be com-
putable without future information. The same historical skill scores can be grouped in four ways. Pooled
weighting,w k, uses the full validation history and assigns each agent one weight at every horizon and in
every regime. Horizon-conditioned weighting,w (H) k , recomputes skill at each forecast horizon. Regime-
conditioned weighting,w (r) k , recomputes skill within each regime. Horizon–regime-conditioned weighting,
w(H,r) k , recomputes skill inside each combination of horizon and regime. FACTS-MAS treats the choice
among these groupings as a validation problem: for each eligible configuration, competing fusion strategies
are evaluated on historical validation data, and the strategy with lower validation error is selected before
entering the test window.
This creates an important distinction betweenadaptivityandgranularity. A more granular rule can rep-
resent more context-specific behavior but is estimated from fewer observations. Rare regimes can therefore
produce insufficient evidence for reliable weight selection. FACTS-MAS allows the level of adaptation to be
constrained by historical support rather than assuming that finer conditioning always improves generaliza-
tion. In the housing configuration, a regime-specific weight vector is used only when the regime contains at
least 13 distinct validation weeks; otherwise the forecast falls back to the pooled weights. An earlier version
of the implementation had no such rule and assigned equal weights to every channel when a regime had no
validation data, which affected 780 test cells and inflated the apparent benefit of regime conditioning.
8

3.6 Calibration of Domain-Specific Parameters
Some evidence channels require domain-specific constants or mappings. Examples include event-effect
duration, numerical impact scales, classification thresholds, lag lengths, or transformation parameters. As-
signing such values from intuition alone can introduce an unmeasured source of forecasting error.
FACTS-MAS therefore separates parameter calibration from held-out evaluation. For a domain-specific
parameterθand candidate setΘ ={θ 1, . . . , θm}, each candidate is evaluated on historical validation data
for validation foldf,
Lf (θ) = MAPE (yf , ˆyf (θ)).(10)
A candidate is not promoted solely because it achieves the lowest pooled error. The framework addition-
ally checks whether the direction of improvement is sufficiently consistent across folds. This discourages
parameter changes whose apparent benefit is driven by a small subset of historical periods. Most impor-
tantly, calibration is permitted to return a null quantitative effect. Ifθ ∗ = 0provides the best and most
consistent validation performance, the framework interprets this as evidence that the corresponding magni-
tude adjustment is unsupported. Other outputs from the same channel, such as classification, confidence, or
attribution information, can remain available even when its direct numerical adjustment is removed.
In the housing study, each constant was selected once using the validation windows of all six folds, with
a candidate promoted only if it improved validation loss in at least five of the six folds. Because later folds’
validation windows postdate earlier folds’ test windows, this selection is not fully nested in time. The only
adopted calibration result, a zero event-impact scale, changes test accuracy by at most 0.002 percentage
points.
3.7 Factor Attribution
Because every agent produces an independent forecast and every fusion weight is derived from historical
predictive skill, FACTS-MAS exposes a direct forecast-level attribution mechanism.
For forecast origint, the contribution of agentkto the forecasted change from the last observed value is
C(H) k,t =w (H) k,t  ˆy(H) k,t −y t1  ,(11)
so that P k C(H) k,t = ˆy(H) F ACTS,t−yt1. A level-based sharew (H) k,t ˆy(H) k,t would credit an agent that merely repeats
the last observed value with a share of the forecast level even though it contributes nothing to the forecasted
change; the change-based form assigns such an agent a contribution of zero. The set
n
w(H) 1,t , . . . , w(H) K,t o
provides an interpretable summary of which evidence channels were historically most useful under the
validation conditions governing that forecast.
These weights should not be interpreted as causal effect estimates. They are empirical measures of
relative predictive contribution under the selected forecasting and validation procedure. The distinction is
important: an agent can receive low weight because its evidence is redundant with another channel, because
its implementation fails to extract the available signal, or because the evidence itself has little predictive
value.
3.8 Domain Adaptation
The domain-agnostic claim of FACTS-MAS concerns the forecasting procedure, not the invariance of every
fitted component. Moving from source domainD 1 to target domainD 2 therefore involves a controlled
reconfiguration. Table 1 separates the framework into invariant and domain-specific components.
Under this formulation, adapting FACTS-MAS to a new domain consists of four steps:
9

Table 1: Invariant and domain-specific components of FACTS-MAS.
Invariant framework components Domain-specific components
Evidence-channel decomposition Raw data sources and feature definitions
Shared agent output contract Model selected within each evidence channel
Forecast-origin information boundary Relevant exogenous variables and lags
Leakage-safe validation Seasonal period or temporal structure
Skill-relative agent evaluation Structural/entity-level variables
Adaptive fusion mechanism Event ontology and event sources
Calibration protocol Calibrated parameters
Factor-attribution procedure Operating-regime definition
1.Map available evidence to functional channels.Identify which historical, exogenous, seasonal, struc-
tural, and event information is meaningful for the new forecasting target.
2.Instantiate the channel models.Select or fit an appropriate forecasting implementation for each avail-
able evidence channel while preserving the shared output contract.
3.Calibrate domain-specific assumptions.Estimate lags, scales, thresholds, or other configurable quan-
tities using historical validation data without accessing the held-out evaluation period.
4.Re-estimate attribution.Compute agent skill and adaptive fusion weights from the target domain’s own
historical performance rather than transferring weights learned in another domain.
Consequently, FACTS-MAS does not requirew (D1) k =w (D2) k . Indeed, different weight distributions
are expected if the importance of evidence channels differs between domains. Cross-domain transfer is
successful when the common decomposition, validation, calibration, and fusion procedure can be applied
without redesigning the overall architecture, while the system learns a domain-appropriate configuration
from the available evidence.
To summarize, at each forecast origin, available information is streamed into the functional evidence
channels, and each assigned agent returns an independent horizon forecast. A validation step scores these
forecasts against a reference, a calibration step sets the domain-specific constants, and the resulting skill
scores are converted into fusion weights. Adaptive fusion then combines the channel forecasts into the
FACTS-MAS forecast and records each channel’s estimated contribution.
4 Case Studies
Two cases—weekly U.S. housing inventory and weekly unemployment insurance claims—are analyzed by
FACTS-MAS, and a third, energy demand, is specified as a planned configuration only. They are used to
answer the following questions: First, does the fused forecast improve on simple and competitive references?
Second, which evidence channels add incremental skill, and does that skill change with horizon or regime?
Third, can the same decomposition and fusion procedure be re-instantiated when the target and the raw
evidence change? The housing study answers the first two questions, and unemployment claims are used
for the third; the energy configuration is reported as a channel map without results. All experiments follow
one rolling-origin protocol. Data and channel models may change by domain; the information boundary,
agent-level scoring, weight estimation, and held-out testing rules do not.
10

4.1 Data Preparation and Agent Setups
Observations are ordered asT={t 1, . . . , tN }. Each foldfsplits this history into training, validation, an
optional embargo, and a test region,T=T (f) train ∪ T(f) val ∪ T(f) embargo ∪ T(f) test. The split is a rolling-origin
evaluation: training expands, forecasts are issued at successive origins, and accuracy is judged on held-out
periods rather than on a single origin [Tashman, 2000]. Randomly mixing times into training and test folds
can leak future observations in an autoregressive series [Bergmeir et al., 2018], so model fitting, fusion
weights, and the choice of weighting rule use only pre-test information. Two exceptions in the development
of the housing configuration are disclosed and corrected. The seasonal smoothing window was originally
chosen on the test window of the last fold, including targets in January and February 2026; it was re-selected
on validation data alone, nested by fold, and the reported results use the re-selected window. The calibrated
constants were selected across all folds’ validation windows (Section 3.6). Forecasts are issued at every
eligible origin in the test window, and every method is scored on that full set. An inputxmay enter a
forecast at origintonly when its availability date satisfiest available(x)≤t, after any publication lag. The
embargo period takes at least the longest horizon,Hmax = max{H1, . . . , Hq}; for weekly housing data it is
13 weeks. Validation forecasts used to estimate fusion weights are restricted to targets dated on or before the
training cutoff, so that no validation target falls inside the embargo. Test targets dated on or after January 1,
2026, the start of the reserved period, are excluded from the backtest; that period is used only for the holdout
in Section 4.2.3.
Accuracy is reported at each horizon inH={H 1, . . . , Hq}. Within a domain every agent uses the same
set. The reference forecast, which is also the denominator of the skill scores k,i = 1−e k,i/eb,i, is the last
observed value,ˆynaive t+h =y t. Fornpairs the primary metrics are mean absolute percentage error and root
mean squared error [Hyndman and Koehler, 2006],
MAPE = 100 n nX i=1

 yi −ˆyi yi

 ,RMSE = vuut 1 n nX i=1 (yi −ˆyi)2.(12)
Accuracy differences are tested on the weekly cross-section of losses. For each pair of methods, the
panel Diebold–Mariano test of equal average accuracy [Diebold and Mariano, 1995, Qu et al., 2024] uses
a Newey–West variance with lagH−1[Newey and West, 1987]; per-MSA tests use the small-sample
correction of Harvey et al. [1997] with the Benjamini–Hochberg adjustment across the 15 MSAs [Benjamini
and Hochberg, 1995]. Confidence intervals come from a moving block bootstrap over whole weeks [Künsch,
1989] with 5,000 replications and a block length of 13 weeks. Two methods are called equivalent when the
90% confidence interval of their MAPE difference lies within±2%of the reference method’s MAPE. The
model confidence set [Hansen et al., 2011] summarizes the comparison among all methods.
Each agent is also scored alone byL(A k, H), a horizon-specific accuracy loss for agentA k, and
by skill against the reference. Removing channelkfrom the fused forecast changes loss by∆ (H) k =
L(F ACTS−k, H)−L(F ACTS, H). A positive value means that the channel contributes inside the combi-
nation. Removing a channel renormalizes the remaining weights in each cell without re-estimating them.
Removing adaptive weighting replaces every cell’s weights with the fold’s pooled weights, which removes
both horizon and regime conditioning, so this ablation alone cannot separate the two. Domain-specific
constants such as event-impact scales, event durations, and reversion caps are selected by the calibration
procedure on historical validation folds, before the test interval begins. For a candidateθ j,∆ f (θj) =
Lf (θj)−L f (θcurrent)is the change in fold-fvalidation loss; a negative value is an improvement, and pro-
motion requires that improvement across folds. A null candidate is included when it is meaningful, so an
unsupported adjustment can be set to zero.
Two weighting rules are compared on the same forecasts: one pooled weight vector per fold, and sep-
arate weights for each combination of regime and horizon. For each fold and horizon, the rule with lower
11

validation error is selected,g ∗ = arg ming Lval(g), and fixed before the test interval. The regime is com-
puted at the forecast origin, and test error is also reported by horizon and regime. To check whether regime
labels carry information, the same pipeline is rerun with regime labels permuted in blocks and with horizon-
only weights that ignore the regime.
Every compared method is scored at the same forecast origins and against the same realized targets. The
references are the last observed value, a seasonal-naive forecast, and the seasonally adjusted naive forecast
of the M4 competition [Makridakis et al., 2020]. The statistical baselines are Holt’s linear-trend model,
its damped form, factor-adjusted exponential smoothing with and without damping, and a factor-adjusted
Theta model [Assimakopoulos and Nikolopoulos, 2000]. The strongest single model chosen on validation
data is also reported, together with equal-weight combinations of all channels and of the temporal and
seasonal channels. The learned baselines are the TimesFM 2.5 foundation model and a chain-of-thought
language-model forecast. The primary success check is that the fused FACTS-MAS forecast improves
on the last-observed-value reference over the full test window; the stricter check is whether it improves
on the strongest single model. Design choices that used test data during development are listed in the
protocol paragraph above, and the final configuration, hypotheses, and tests were fixed before the holdout
was accessed. Cross-domain transfer keeps the same architecture and learns a new evidence mapping for
each domain (Section 5.4).
4.2 U.S. Housing Inventory Forecasting
The weekly for-sale housing inventory time series from Zillow is the first complete instantiation of FACTS-
MAS. It can populate all five channels in Section 3.1: recent inventory dynamics, national financial condi-
tions, annual listing seasonality, metropolitan structure, and disaster declarations. Two of these channels, the
intrinsic and event channels, calibrate to a null quantitative effect and are retired from the final housing fore-
cast; they are reported as tested channels. The task is to forecast weekly inventory for 15 U.S. metropolitan
statistical areas at 4-, 8-, and 13-week horizons. What follows specifies the housing configuration, reports
forecast accuracy, and then diagnoses which channels earned influence. This case study is one applied con-
figuration of FACTS-MAS, not a definition of the framework: the same procedure can be reused with a
different target and a different evidence map.
4.2.1 Domain Instantiation
The target variable is weekly for-sale housing inventory obtained from Zillow Research. The study includes
the following 15 metropolitan areas:
New York Los Angeles Chicago
Dallas Houston Washington, DC
Miami Philadelphia Atlanta
Phoenix Boston San Francisco
Riverside Detroit Seattle
Zillow reports this series as a four-week trailing average; the unsmoothed weekly series is used as a
robustness check. The panel begins on February 3, 2018. The backtest uses observations through February
21, 2026. The holdout uses a fresh download taken on October 20, 2026 with observations through October
10, 2026 (454 weekly observations per metropolitan statistical area (MSA) and 6,810 MSA–week observa-
tions); every value dated on or before February 21, 2026 in that download equals the earlier vintage, so no
revision affects the results.
Nine target observations were missing in Zillow’s source series: four in Chicago, two in Los Angeles,
two in Miami, and one in Atlanta. These gaps were filled independently within each MSA using the most
12

Table 2: FACTS-MAS evidence-channel instantiation for housing inventory.
Channel Housing evidence Implementation
Temporal Historical weekly inventory 4 weeks: ETS with additive trend and
no seasonal component; 8 and 13 weeks:
damped-trend ETS on seasonally adjusted
inventory (factor-adjusted)
Exogenous Mortgage rate, federal funds rate,
CPI, unemployment
Lagged ridge-regression modifier with
pre-specified lags
Seasonal Week-of-year inventory pattern Ratio-to-moving-average seasonal factors
(seasonally adjusted naive form)
Intrinsic Population, income, housing
stock, density, hazard exposure
Scaled ridge regression with structural
mean reversion; retired (calibrated rever-
sion cap is zero)
Event FEMA disaster declarations LLM-assisted event interpretation with
confidence gating; retired (calibrated im-
pact scale is zero)
recent previously observed value. No information from a future observation or another MSA was used
during imputation, and the affected rows were retained in a separate audit log. The unsmoothed series has
20 missing observations, filled the same way. No missing observation falls in a test or holdout target. Table 2
maps the domain-independent FACTS-MAS evidence roles to their housing-specific implementations. The
initial decomposition is deliberately non-overlapping: the 4-week temporal agent does not model seasonality
internally because seasonality is represented by a separate evidence channel, which makes the incremental
value of each component easier to evaluate. At 8 and 13 weeks, however, the temporal agent that survived
validation is a factor-adjusted model that reuses the seasonal channel’s factors (see the temporal channel
below), so the two channels are not independent at those horizons.
Temporal channelThe temporal channel models the endogenous trajectory of each MSA’s inventory se-
ries independently. At the 4-week horizon it uses exponential smoothing with an additive trend and no sea-
sonal component [Holt, 2004, Winters, 1960, Hyndman et al., 2002, Pan, 2011], ˆyAR = ETS(y1:t;trend=
add,seasonal=∅). At 8 and 13 weeks it uses a factor-adjusted damped-trend model: the series is divided
by the seasonal factors of the seasonal channel, a damped additive trend [Gardner and McKenzie, 1985] is
fitted to the adjusted series, and the forecast is multiplied by the factors of the target weeks. This variant was
promoted by a rule fixed before the comparison was run: it had to improve validation error and improve test
error in at least five of the six folds; it met the rule at 8 and 13 weeks but not at 4 weeks. Because this rule
consults test-fold accuracy, the holdout in Section 4.2.3 provides the clean test of the resulting configuration.
Damping was chosen over an undamped trend on validation data in every fold. Both models are fitted sepa-
rately for each MSA and forecast origin using only the available historical target, and negative extrapolated
values are clipped at zero. A last-value persistence forecast,ˆy naive t+h =y t, serves as the minimum baseline.
Over all test origins, the undamped trend model has MAPE 2.368%, 5.430%, and 10.225% at 4, 8, and 13
weeks, against 4.194%, 7.225%, and 10.814% for the naive forecast, and it improves on the naive forecast
in 15, 14, and 11 of the 15 MSAs. Its advantage therefore narrows sharply with horizon, and at 13 weeks
it is worse than the naive forecast in four of the six folds. The factor-adjusted damped model has MAPE
1.974%, 3.608%, and 5.664%.
13

Exogenous channelThe exogenous channel uses four national macroeconomic series from Federal Re-
serve Economic Data (FRED): the 30-year fixed mortgage rate, the effective federal funds rate, the Con-
sumer Price Index, and the unemployment rate. The weekly macroeconomic panel begins in January 2018.
Because several FRED series are indexed by their reference month rather than their actual publication date,
the housing pipeline shifts monthly observations forward by approximate publication delays before they
become eligible for forecasting: 32 days for the federal funds series, 35 days for unemployment, and 42
days for CPI. Weekly mortgage rates require no corresponding monthly-release adjustment. The macro and
Zillow series retain their native Monday and Saturday conventions, respectively. Macro observations are
attached to each Zillow week using a backward-only as-of join, ensuring that a housing observation never
receives a macroeconomic value dated after that week. The Macro agent (exogenous channel) fits a ridge
regression of inventory percentage change on lagged macroeconomic features [Hoerl and Kennard, 1970].
The lags are pre-specified from the literature rather than fitted: 6 weeks for the mortgage rate, 10 weeks for
the federal funds rate, 10 weeks for CPI, and 5 weeks for unemployment. Importantly, subsequent validation
did not produce convincing evidence that this magnitude channel adds incremental predictive information.
Three increasingly restrictive analyses were performed: direct forecast-signal correlation, lag-sensitive re-
gression analysis, and a two-way fixed-effects panel regression with MSA-clustered standard errors. The
final panel specification contained 5,850 observations. Mortgage rate, the theoretically most direct housing-
finance variable, was statistically indistinguishable from zero (p= 0.575); unemployment was also null
(p= 0.548), and CPI was borderline (p= 0.085). The federal funds rate hadp= 0.042, but this does
not survive a Holm adjustment across the four variables (p= 0.170), a wild cluster bootstrap (p= 0.073),
or Driscoll–Kraay standard errors that allow for the fact that all MSAs share the same national regressor
[Driscoll and Kraay, 1998] (p= 0.71). Used as a forecast on its own, the channel is no more accurate
than the naive forecast (MAPE 4.258%, 7.297%, and 10.919%). Because this pattern did not constitute
robust evidence of incremental forecasting value, we treat the macro magnitude channel as a documented
negative result rather than continuing to tune the specification until a positive result appears. This behavior
illustrates a central FACTS-MAS principle: candidate evidence channels are evaluated empirically and are
not guaranteed positive influence merely because they are economically plausible.
Seasonal channelThe seasonal channel is deterministic and learns a separate annual inventory profile for
each MSA. For observationt, letm t denote a 52-week centered moving average. A raw seasonal ratio is
rt =y t/mt. For ISO weekw∈ {1, . . . ,53}, the seasonal factorqw is the median historical ratio observed
for that week. The week-of-year profile is smoothed with a seven-week circular moving average, so that
the transition between week 53 and week 1 is treated as adjacent rather than as a boundary. Factors are
then normalized to have mean one. The window was selected on validation data, nested by fold, from
{1,3,5,7}; the value seven was chosen in every fold. An earlier window of five had been chosen on the test
window of the last fold and is not used. Near the forecast origin the centered average is computed from the
available half-window only, so no factor uses data after the origin. Ifq wt denotes the seasonal factor at the
forecast origin andq wt+h the factor for future weekt+h, the seasonal forecast isˆy season t+h =y tqwt+h/qwt.
This forecast is the seasonally adjusted naive method of the M4 competition [Makridakis et al., 2020] with
leakage-safe factors. On its own it has MAPE 2.890%, 4.774%, and 6.945% at 4, 8, and 13 weeks.
Intrinsic channelThe intrinsic channel represents persistent differences between metropolitan areas. The
five static features are population, median income, housing units, density, and a hazard index. Popula-
tion, income, and housing stock are derived from Census American Community Survey data. Population
density combines Census population with CBSA land-area information. Hazard exposure is represented
using county-level NOAA Storm Events records aggregated to each MSA. An initial tree-based imple-
mentation strongly overfit the small cross-section of 15 metropolitan areas. The current implementation
14

Table 3: Housing Event Agent impact-scale calibration: mean validation MAPE. Validation targets are
restricted to dates on or before each fold’s training cutoff; an earlier version of this sweep allowed targets to
extend up to 13 weeks past it, which changed the values by 1–2% but not the ordering.
Scale 0 .01 .02 .03 .05 .075 .10
MAPE5.7045.869 6.112 6.413 7.110 8.121 9.234
therefore uses a standardized ridge regression to estimate a structurally implied average inventory level,
µd =β 0 +β ⊤˜xd. The model is regularized and evaluated using held-out MSAs so that structural relation-
ships must generalize across metropolitan areas rather than memorize MSA identity. The current implemen-
tation replaced an earlier Gradient-Boosting model that achieved very low training error but approximately
48–52% leave-one-MSA-out error. Rather than immediately forecasting the structural level itself, the agent
gradually moves the most recent inventory towardµ d. For horizonHand steph,ρ h =ρ max(h/H) 2 and
ˆyintrinsic t+h =y t +ρ h(µd −y t), withρ max = 0.30in the original housing configuration. The cap was then
calibrated on validation folds over{0,0.10,0.20,0.30,0.45,0.60,0.80}, and zero was preferred in all six
folds (validation MAPE 7.923% at zero against 10.259% at 0.30). Atρ max = 0the agent reproduces the
naive forecast, so the channel is retired from the housing forecast. The quadratic schedule is also not con-
sistent across horizons: the forecast for weekt+ 4closes 0.30 of the gap whenH= 4but 0.028 of it when
H= 13. Because the channel is retired, this is documented rather than corrected. The static features use the
2024 Census vintage and 2016–2025 storm records for every fold; replacing the channel’s output with the
naive forecast changes fused accuracy by at most 0.011 percentage points, so this vintage has no material
effect.
Event channelDiscrete events are represented using FEMA disaster declarations. OpenFEMA provides
stable declaration metadata, which is mapped from affected counties to the 15 target MSAs. The Event
Agent is the only housing component that uses an LLM (gpt-4o-mini). Its role is not to directly generate
an inventory forecast from free-form text. Instead, the model converts event metadata into a structured
representation containing event type, impact magnitude, confidence, and reasoning. The event ontology
includes disaster, zoning change, major employer shift, and housing initiative categories. Event confidence
is explicitly gated: interpretations with confidence less than or equal to 0.60 receive zero quantitative effect.
Both the original magnitude and gated result are retained for auditability. Prompt development revealed an
important failure mode. Without an explicit causal definition of the magnitude sign, small prompt changes
caused event impacts to reverse direction. The final interpretation procedure therefore requires the model
to identify the mechanism connecting an event to for-sale inventory before assigning the sign of the impact.
FEMA’s available metadata nevertheless supported only coarse severity differentiation. In practice, the
LLM largely behaved as an ordinal severity classifier rather than a genuinely continuous impact estimator.
The resulting event-magnitude mapping was therefore subjected to the calibration procedure in Sections 3.6
and 4.1. Two event assumptions were explicitly calibrated: the duration for which a declaration should
influence the forecast and the scale converting event severity into a numerical inventory adjustment. For the
active-event duration, progressively shorter windows produced lower validation error in all six folds. Once
the impact scale is set to zero (below), the duration no longer affects the forecast. A separate sweep of the
event impact scale considered the values0,0.01,0.02,0.03,0.05,0.075, and0.10. Mean validation MAPE
increased monotonically as the event magnitude scale increased (Table 3). The scale of zero was preferred
in 6 of 6 folds. With a zero scale, the agent’s forecast equals the last observed value at every origin, so the
event channel reproduces the naive reference and is retired from the final housing forecast. Consequently, the
production Event Agent does not directly perturb forecast magnitude from the LLM severity score. Event
15

Table 4: Housing backtest folds and holdout. Test start and end are the first and last forecast origins.
Fold Train start Train end Test start Test end
1 2019-02-02 2021-01-23 2021-05-01 2021-11-13
2 2019-02-02 2021-11-13 2022-02-19 2022-09-03
3 2019-02-02 2022-09-03 2022-12-10 2023-06-24
4 2019-02-02 2023-06-24 2023-09-30 2024-04-13
5 2019-02-02 2024-04-13 2024-07-20 2025-02-01
6 2019-02-02 2025-02-01 2025-05-10 2025-11-22
Holdout 2019-02-02 2026-02-21 2026-02-28 2026-09-12
classification and confidence remain available, but the unsupported cardinal interpretation of the severity
score is removed. This result should not be interpreted as evidence that real-world events are irrelevant to
housing. It shows that the particular mapping from available FEMA metadata to a continuous point-forecast
adjustment did not demonstrate incremental predictive value.
The housing experiment uses six expanding-window folds and reserves data from January 2026 onward.
In an earlier version of the experiment, 8- and 13-week forecasts issued near the end of the sixth test window
had targets in January and February 2026 (165 MSA–origin–horizon cells); these cells are excluded from
every backtest result reported here. The fold schedule is shown in Table 4, together with the holdout de-
scribed in Section 4.2.3. Every fold contains at least a 13-week separation between the final eligible training
date and the test period, matching the longest housing forecast horizon. Forecasts are evaluated at every
eligible weekly origin within each test window rather than at one forecast date per fold.
To evaluate whether agent usefulness changes with financial conditions, housing forecast origins are
divided into three monetary-policy regimes using the 13-week change in the federal funds rate,∆13FFRt =
FFRt −FFR t−13. The origin is hiking when that change exceeds0.25percentage points, cutting when it is
below−0.25, and stable otherwise. The regime is evaluated at the forecast origin rather than the target date,
ensuring that it represents information available when the prediction is made. Because the federal funds
rate is national, all 15 MSAs share the same regime at every date, and the sample contains one substantive
hiking episode (June 2022 to September 2023) and three cutting episodes, so regime conditioning is close
to conditioning on a small number of historical periods.
Two fusion configurations are compared: pooled fold-level weighting, and adaptive selection, for each
horizon, between pooled weights and weights conditioned on regime and horizon. The production config-
uration uses adaptive selection with the 13-week data-sufficiency rule of Section 3.5. A finer, cell-level
selection was also explored during development, but that choice was informed by test-window results and is
not reported. Section 5.1.5 tests whether the regime labels carry information.
4.2.2 Forecasting Results
Table 5 reports test accuracy over the six backtest folds for FACTS-MAS, its references, and the statistical
baselines, on both Zillow series. FACTS-MAS outperforms the persistence reference at all three horizons:
the panel Diebold–Mariano statistic is−6.9,−6.3, and−5.7at 4, 8, and 13 weeks (p <10 −4), the difference
is significant in all 15 MSAs at every horizon, and the 95% confidence intervals of the MAPE difference are
[−2.66,−1.42],[−4.72,−2.52], and[−7.11,−3.53]. The relative reduction is 49.5%, 49.9%, and 47.0%
on the smoothed series and 23.9%, 34.5%, and 37.1% on the unsmoothed series. The strongest single
model, factor-adjusted damped exponential smoothing (FA-ETS-d), is at least as accurate as FACTS-MAS
at every horizon. FACTS-MAS is statistically equivalent to it at 8 weeks (90% interval of the difference
[−0.001,0.030], within the±0.072margin), less accurate at 4 weeks by 0.144 (90% interval[0.022,0.261];
16

Table 5: Backtest MAPE (%) over six folds, all test origins, targets before January 1, 2026. FA-ETS-d:
factor-adjusted damped ETS. Lower is better; bold marks the lowest value in each column.
Smoothed series Unsmoothed series
Method4 wk 8 wk 13 wk 4 wk 8 wk 13 wk
Naive (last value) 4.194 7.225 10.814 4.785 7.882 11.438
Seasonal naive 20.771 20.513 20.597 – – –
Seasonally adjusted naive 2.890 4.774 6.945 3.626 5.408 7.489
Holt (temporal channel) 2.368 5.430 10.225 4.317 7.901 13.022
Theta (factor-adjusted) 2.933 4.842 7.047 – – –
FA-ETS-d1.974 3.608 5.664 3.402 5.105 7.164
FACTS-MAS 2.118 3.622 5.731 3.642 5.159 7.189
Table 6: Backtest MAPE (%) over six folds against the TimesFM 2.5 foundation model, smoothed series.
Method4 weeks 8 weeks 13 weeks
Naive 4.194 7.225 10.814
TimesFM 2.5 2.361 4.860 8.269
FA-ETS-d1.974 3.608 5.664
FACTS-MAS 2.118 3.622 5.731
Diebold–Marianop= 0.12), and marginally less accurate at 13 weeks by 0.067 (95% interval[0.001,0.152];
p= 0.09). At 8 weeks the 90% model confidence set contains only FA-ETS-d, FACTS-MAS, and the
five-channel variant of FACTS-MAS; at 13 weeks it excludes only the naive forecast. The fused forecast
therefore improves strongly on the references but does not improve on the best single model.
Table 6 compares FACTS-MAS with Google’s TimesFM 2.5 time-series foundation model [Das et al.,
2024], run zero-shot with a 52-week context at every test origin of all six folds. TimesFM improves on the
naive reference at every horizon (p <10 −4), but FACTS-MAS is more accurate than TimesFM at every
horizon, by 0.243, 1.239, and 2.539 percentage points (Diebold–Marianop= 0.006,0.0001, and0.0004;
significant in 7, 10, and 10 of the 15 MSAs). FA-ETS-d is likewise more accurate than TimesFM at every
horizon. The chain-of-thought language-model forecast is evaluated on the holdout only (Section 4.2.3),
because the backtest period falls inside the training data of the language models available for the comparison.
Errors stratified by monetary-policy regime show no regime in which the final forecast fails. At the
13-week horizon,
Regime Naive FA-ETS-d FACTS-MAS
hiking 8.059 5.530 5.552
cutting 13.043 6.091 6.090
stable 11.628 5.666 5.759
so FACTS-MAS improves on the naive reference in every regime, and FA-ETS-d, which uses no regime
information, is equally accurate in every regime. An earlier version of the system appeared to lose to the
naive reference in the hiking and cutting regimes and to be repaired by regime-aware weighting; that pattern
came from an older seasonal channel and, in the cutting regime, from the equal-weight fallback described
in Section 3.5, and it does not appear in the current configuration.
17

Table 7: Holdout MAPE (%), forecast origins February 28 to September 12, 2026, no publication lag. 13-
week values are descriptive. CoT: chain-of-thought forecast (gpt-5.6-luna), run on the smoothed series only.
Smoothed series Unsmoothed series
Method4 wk 8 wk 13 wk 4 wk 8 wk 13 wk
Naive (last value) 3.122 5.445 8.438 3.355 5.306 7.925
Seasonal naive 8.534 8.534 8.550 8.593 8.601 8.622
Seasonally adjusted naive 1.492 2.377 3.393 2.053 2.6773.564
TimesFM 2.5 1.410 2.602 4.457 2.464 3.689 5.355
CoT (gpt-5.6-luna) 1.259 2.225 3.268 – – –
FA-ETS-d1.1381.936 3.0802.0282.709 3.736
FACTS-MAS 1.2431.929 3.0452.0532.6713.644
4.2.3 Holdout Evaluation
After the configuration was frozen, it was evaluated once on data that had not been accessed during devel-
opment: forecast origins from February 28 to September 12, 2026 (29, 25, and 20 weekly origins at 4, 8,
and 13 weeks for each of the 15 MSAs). The fusion weights were estimated from the 104-week validation
window ending on February 21, 2026. Four hypotheses, the tests, and the reporting rules were committed
before the holdout data were downloaded: FACTS-MAS improves on the naive reference at every horizon
(H1); FA-ETS-d does too (H2); FACTS-MAS and FA-ETS-d are equivalent at 8 and 13 weeks (H3); and
FA-ETS-d is at least as accurate as FACTS-MAS at 4 weeks (H4). With 20 origins the 13-week results are
reported as descriptive only. The bootstrap block length equals the horizon, and at 13 weeks it is capped
at half the number of weeks. The chain-of-thought baseline uses the NEXUS prompt with gpt-5.6-luna
(reasoning effort low), whose documented knowledge cutoff, February 16, 2026, precedes the first holdout
target; the model’s own answer to a cutoff question was June 2024. The prompt itself states a January 2025
cutoff, a wording inherited from the NEXUS template.
Table 7 reports the holdout accuracy and Table 8 the hypothesis tests. All four hypotheses are supported.
FACTS-MAS reduces MAPE relative to the naive forecast by 60%, 65%, and 64% on the smoothed series
and by 39%, 50%, and 54% on the unsmoothed series. It is equivalent to FA-ETS-d at 8 weeks and less ac-
curate than FA-ETS-d at 4 weeks by 0.105 percentage points. The chain-of-thought forecast is competitive:
its MAPE is higher than that of FA-ETS-d and of FACTS-MAS at every horizon, but neither difference is
statistically significant (against FA-ETS-d,p= 0.38,0.43, and0.60; against FACTS-MAS, in a compar-
ison added after the results were seen,p= 0.90,0.43, and0.54). TimesFM is significantly less accurate
than FA-ETS-d at 4 and 8 weeks (p= 0.016andp <10 −4). On the unsmoothed series FACTS-MAS at
4 weeks coincides with the seasonally adjusted naive forecast, and at 8 weeks it is slightly more accurate
than FA-ETS-d (−0.038,p= 0.031); because the seasonally adjusted naive forecast is equally accurate
there, this does not indicate a benefit of fusion over a single model. With a two-week publication lag, every
method’s error rises (FACTS-MAS 2.270%, 2.944%, and 4.000%; naive 5.474%, 7.953%, and 11.110%),
and no conclusion changes. In the lag-two run, 27 of 1,110 chain-of-thought forecasts (2.4%) were lost to
a network interruption; the tests for that run were computed with and without the chain-of-thought forecast.
The holdout period was easier for every method than the backtest, so absolute errors should be compared
within a period, not across periods.
Several limits are inherited from the housing data. FRED publication adjustments use approximate
fixed delays rather than true vintages: 32 days for federal funds, 35 for unemployment, and 42 for CPI. That
removes the most obvious lookahead but does not reconstruct the exact information set on every historical
date. The target is Zillow’s smoothed series, a four-week trailing average, which makes every method look
18

Table 8: Pre-registered holdout hypotheses, smoothed series, no publication lag. Differences are in MAPE
percentage points with 95% block-bootstrap intervals (90% intervals for the equivalence test, H3).
Hypothesis Horizon Difference Interval Result
H1: FACTS-MAS<naive 4 wk−1.879 [−3.031,−0.897]supported
8 wk−3.516 [−5.681,−1.705]supported
13 wk−5.393 [−7.681,−3.071]supported
H2: FA-ETS-d<naive 4 wk−1.984 [−3.081,−1.031]supported
8 wk−3.509 [−5.693,−1.680]supported
13 wk−5.358 [−7.642,−3.028]supported
H3: equivalent to FA-ETS-d 8 wk−0.007 [−0.029,0.014]equivalent (±0.039)
13 wk−0.035 [−0.048,−0.035]equivalent (±0.062)
H4: FA-ETS-d≤FACTS-MAS 4 wk+0.105 [−0.007,0.182]supported
Table 9: FACTS-MAS evidence-channel mapping for unemployment insurance claims. The temporal, ex-
ogenous, and seasonal channels are implemented; the intrinsic and event channels are not.
Channel Unemployment-domain interpretation
Temporal Historical unemployment level, rate, or claims trajectory
Exogenous Macroeconomic, labor-market, financial, or activity indicators
Seasonal Recurring calendar structure in employment or claims
Intrinsic Persistent regional labor-force, demographic, or industrial composition
Event Major layoffs, employer expansions or closures, policy changes, disasters,
or other labor-market shocks
more accurate than on the unsmoothed series; both are reported. The hazard index is a partial structural
proxy: NOAA Storm Events can be coded by county or by forecast zone, and the present aggregation uses
county-coded events, so some hazards are undercounted. The Intrinsic Agent learns mainly from differences
across metropolitan areas, and only 15 MSAs are available. That small cross-section limits how much
structural signal can be estimated. Replacing an overfit tree with ridge regression reduces memorization
of those few areas, but it does not increase the number of metropolitan areas available for learning. Nine
Zillow observations were forward-filled, including a four-week Chicago gap. The fill is lookahead-safe, yet
it inserts an artificial flat stretch.
The Event Agent currently depends on FEMA declarations. The event ontology used by this agent
includes four categories—disaster, zoning change, major employer shift, and housing initiative—and there-
fore contemplates local shocks such as employer moves, mass layoffs, zoning actions, and housing-policy
changes. FEMA covers only disasters, not the full set. Some FEMA records also fit the ontology poorly;
a presidential-inauguration declaration is the example encountered in validation. Confidence gating zeroed
its quantitative effect, but the gap remains. Two design choices made during development used test-window
evidence (the original seasonal smoothing window and a cell-level fusion rule); both were replaced or re-
moved, and the holdout was evaluated only after the configuration was frozen.
4.3 Unemployment Forecasting
Unemployment forecasting emphasizes labor-market dynamics, policy and employer shocks, and recurring
calendar structure in employment or claims. The channel map for this domain is Table 9.
The target is weekly initial unemployment insurance claims, not seasonally adjusted, for 15 U.S. states
19

Table 10: Unemployment insurance claims: test MAPE (%) over six folds, pandemic window excluded.
The undamped FA-ETS row was added after the other results were seen and is descriptive.
Method4 weeks 8 weeks 13 weeks
Naive 18.816 21.963 24.716
Seasonally adjusted naive 17.836 19.294 20.613
FA-ETS-d (damped) 17.868 19.411 20.791
FA-ETS (undamped)17.71 19.18 20.55
FACTS-MAS (frozen recipe) 17.863 19.233 20.578
from January 2013, obtained from FRED. The temporal and seasonal channels use the housing implemen-
tations unchanged, including the seven-week seasonal window, and the exogenous channel uses the federal
funds rate and CPI with the housing lags. The housing recipe is applied without re-tuning: the same six
folds, embargo, validation window, data-sufficiency rule, temperature, and promotion outcome. The win-
dow of pandemic-era claims, from March 14, 2020 to September 4, 2021 (the start of the national surge
to the expiry of the federal pandemic programs), is excluded from skill estimation and scoring but kept for
model fitting. This window, and the rest of the protocol, were fixed from policy dates and written down
before any result of this evaluation was computed.
Table 10 reports the results. The fused forecast improves on the naive reference at every horizon
(p= 0.002,0.0004, and0.0004) and on damped FA-ETS at 8 and 13 weeks (p= 0.0009and0.005),
but validation selected the undamped trend in every fold, and the undamped factor-adjusted model alone is
slightly more accurate than the fused forecast at every horizon. In unemployment claims, the frozen recipe
beats naive and the damped FA-ETS reference, but not undamped FA-ETS, which is the better reference for
that series. In neither domain is there evidence that fusion beats the best single model. The channel weights
differ from housing, as the transfer hypothesis expects: with the temporal channel that ignores seasonality,
the seasonal channel receives about three quarters of the weight at every horizon, and the exchange of weight
between the temporal and seasonal channels seen across horizons in housing does not appear. Including the
pandemic window raises every method’s MAPE by 0.7 to 2.2 points. Because an earlier pilot evaluation
scored claims data through August 2026, a clean holdout for this domain is not available.
4.4 Energy Forecasting
Energy demand forecasting emphasizes short and medium cycles, weather sensitivity, and abrupt regime
changes driven by temperature extremes, outages, and price shocks. The intended channel map for this
domain is Table 11. No energy experiments are reported in this paper; the mapping below records the
planned configuration.
The configuration isC (energy) = (E (energy),A (energy),Θ (energy),H (energy),R (energy)). Completed
energy runs should report target, frequency, regions, coverage, horizons, leakage controls, channel models,
calibrated parameters, baselines, and any regime definition, together with learned weightsw (energy) =
[wtemporal,w exogenous,w seasonal,w intrinsic,w event], or the subset of channels actually implemented. In this
domain, seasonal and exogenous channels are expected candidates for substantial weight when validation
supports that attribution.
5 Discussion
The housing inventory case study shows that FACTS-MAS can decompose mixed evidence into testable
channels, tell those channels apart, calibrate domain assumptions, and adapt their influence. It also clarifies
20

Table 11: Planned FACTS-MAS evidence-channel mapping for the energy domain.
Channel Energy-domain interpretation
Temporal Historical energy-demand or load trajectory
Exogenous Weather, temperature, economic activity, price, or other external demand
drivers available at the forecast origin
Seasonal Recurring daily, weekly, and/or annual demand structure
Intrinsic Persistent characteristics of the forecasting region, grid, customer base, or
system capacity
Event Discrete weather, outage, policy, infrastructure, or other domain-relevant
events
what “domain-agnostic” does and does not mean. The framework is not a pretrained model whose fitted
weights are expected to carry over unchanged to a new domain; instead, it carries over a procedure: mapping
evidence to functional channels and scoring each channel against a reference, so as to calibrate, attribute,
and fuse.
5.1 Channel Diagnostics and Fusion Analysis
This section examines standalone channel value, domain-specific calibration, and adaptive fusion: whether
FACTS-MAS can distinguish useful evidence from weak, redundant, or context-dependent evidence and
adjust the fused forecast accordingly.
5.1.1 Evidence Channels as Testable Hypotheses
Each FACTS-MAS agent is a forecasting hypothesis:H k asserts thatE k contains incremental information
about futurey. Including an agent does not acceptH k; historical validation decides whether the channel
beats the reference. Unlike a joint feature model, FACTS-MAS produces independent agent forecasts before
fusion, so weak evidence can be diagnosed without removing or retraining unrelated channels. The housing
experiments show that pattern clearly. The temporal channel improves on persistence at 4 weeks but its
advantage narrows with horizon unless seasonality is removed first; seasonality helps at every horizon;
the tested macroeconomic magnitude channel adds little robust incremental value; the intrinsic reversion
calibrates to zero; and the initial event-severity magnitude mapping is harmful before calibration. Agents
are therefore candidate hypotheses, not mandatory contributors.
5.1.2 Macro Channel: A Well-Earned Null
The Macro agent (exogenous channel) is driven by mortgage rates, monetary policy, inflation, and unem-
ployment. These are plausible housing drivers, but plausibility does not establish short-horizon incremental
forecast value. Three diagnostics were used.
Direct forecast-signal validation.The agent’s predicted modifier was compared with realized inventory
changes across the six backtest folds. The correlations were weak:
Horizon 4wk8wk13wk
r 0.011−0.025−0.177
p 0.920 0.814 0.095
(13)
providing no clear predictive signal.
21

Table 12: Final housing Macro agent signal validation:p-values for the original panel (MSA and year–
quarter fixed effects, MSA-clustered errors), with a Holm adjustment across the four variables, a wild cluster
bootstrap (Webb weights, 9,999 draws), and Driscoll–Kraay errors with MSA fixed effects.n= 5,850.
Variable Lag Coef. Clustered Holm Wild bootstrap Driscoll–Kraay
Mortgage rate 6 weeks 0.0075 0.575 1.000 0.611 0.973
Federal funds 10 weeks -0.0129 0.042 0.170 0.073 0.712
CPI 10 weeks -0.0047 0.085 0.254 0.086 0.463
Unemployment 5 weeks -0.0015 0.548 1.000 0.577 0.264
Lag-sensitive analysis.A search over plausible transmission lags yielded apparently strong correlations
for several raw macroeconomic levels. Those correlations are misleading: national macro values are identi-
cal across MSAs on a given date, so MSA–date pairs pseudo-replicate one national signal and overstate the
effective sample size. Strong trends in both macro levels and inventory also make simple level correlations
vulnerable to spurious association.
Panel validation.The final diagnostic used a two-way fixed-effects panel with MSA and year–quarter
fixed effects, MSA-clustered standard errors, 5,850 observations, and the pre-specified midpoint lags rather
than data-mined best lags (Table 12).
Only federal funds crosses the conventional 5% threshold under clustered errors, and it does not survive
the multiple-testing adjustment, the wild bootstrap, or errors that allow for the common national regressor;
mortgage rates, the most direct theoretical housing-finance channel, are null under every specification. We
treat this as awell-earned null: the Macro agent was not retuned until a positive result appeared, and its
weak incremental skill is allowed to reduce its fusion weight. FACTS-MAS can reject a plausible channel
without redesigning the architecture.
5.1.3 Event Channel: Semantic Evidence and a Null Scale
The Event Agent fails differently. FEMA metadata contain useful semantic information that an LLM can
classify, but a qualitative severity score is not automatically a valid continuous forecast adjustment. The
original agent returned an impact in[−1,1]. Prompt development showed that FEMA metadata support only
coarse severity tiers: similar assistance-program configurations repeatedly mapped to the same severity, so
the output behaved more like an ordinal classifier than a continuous impact model. FACTS-MAS therefore
tested whether those magnitudes should modify the numerical forecast at all.
Impact-scale calibration.Letm t be the signed severity score andλthe scale that maps it into a fore-
cast adjustment. Instead of assumingλ >0, calibration testedλ∈ {0,0.01,0.02,0.03,0.05,0.075,0.10}
(Table 3).
The ordering is monotonic: larger magnitude adjustments worsen validation MAPE, andλ= 0is
preferred in all six folds. With the scale at zero, the declaration-active window no longer affects the forecast,
and the event channel’s output equals the naive reference. The production Event Agent therefore keeps
semantic classification and confidence but removes the unsupported point-forecast magnitude adjustment.
Useful semantic information need not imply a validated numerical effect.
22

5.1.4 From Raw Error to Softmax Weights
Why raw accuracy is insufficient.An earlier fusion rule weighted agents by inverse validation MAPE.
The Macro agent, despite its null signal, sometimes received weight comparable to stronger agents. A
weakly fitted regularized model can stay close to persistence; because persistence is competitive at short
horizons, absolute error can look good without adding new information. Absolute error therefore confounds
useful signal with naive imitation. FACTS-MAS uses skill relative to naive,s k,i = 1−e k,i/enaive,i, so an
agent that only reproduces the naive forecast receives approximately zero skill even when its MAPE looks
competitive.
Robust skill aggregation.Averaging pointwise relative-skill ratios is unstable whene naive,i →0: the ratio
ek,i/enaive,i can explode. In one diagnostic, the temporal agent had median pointwise skill about+0.227
but mean skill about−0.407, with isolated ratios near−32. Fusion therefore uses˜s k = mediani(sk,i). The
median protects relative-skill aggregation whenever the reference occasionally has near-zero error.
Why softmax replaced hard skill floors.Transforming skill bymax(s k, ϵ)p avoided zero weights but
collapsed every negative-skill agent to the same floor, sos=−0.01ands=−0.50became indistinguish-
able. Softmax,w k = exp(˜sk/τ)/ P j exp(˜sj/τ), preserves the full ranking, including among negative-skill
agents. The fusion rule therefore evolved from raw MAPE, to relative skill, to robust relative skill with
softmax, each step answering an observed failure of the previous rule.
5.1.5 Adaptive Fusion and Its Limits
Does regime conditioning carry information?Adaptive weighting chooses, for each fold and horizon,
between pooled weights and weights conditioned on regime and horizon. Its apparent 13-week benefit was
tested in three ways on the five-channel configuration, before the temporal channel was replaced. First,
with regime labels permuted in blocks, 46% of 200 permutations at 8 weeks and 27% at 13 weeks were at
least as accurate as the true labels. Second, weights conditioned on horizon alone, with no regime, matched
the regime-conditioned weights at 8 weeks (4.468% against 4.468%) and were more accurate at 13 weeks
(6.826% against 6.987%). Third, 60–75% of the 13-week benefit came from a single fold, in the stable
regime. We therefore find no evidence that the regime labels carry predictive information beyond horizon
conditioning; with a national regime variable and one substantive hiking episode in the sample, the regime
partition is close to a partition by historical period.
Data sufficiency.Context-aware adaptation should depend on both estimated performance and evidence
volume. Letn (f) H,r be the number of distinct validation weeks for horizonH, regimer, and foldf. The
production rule uses regime-conditioned weights only ifn (f) H,r ≥13and otherwise falls back to the pooled
weights. An earlier implementation had no such rule: when a regime was absent from a validation window,
every channel, including the channels that reproduce the naive forecast, received a weight of 0.2. That
fallback affected 780 test cells, accounted for about one fifth of the apparent 13-week benefit of regime
weighting, and produced the apparent repair of the cutting regime reported in an earlier version of this work.
Fusion versus the strongest single model.Once the temporal channel is seasonally adjusted, validation
gives it 0.97 of the weight at 8 weeks and 0.92 at 13 weeks, the seasonal channel receives most of the re-
mainder, and the exogenous channel receives almost none. The fused forecast is then statistically equivalent
to the factor-adjusted model alone at 8 weeks in the backtest and on the holdout, and slightly less accurate
at 4 and 13 weeks, in the backtest and on the holdout. Three further candidates, each registered before it
23

was run, did not change this: a listing-flow channel built from Zillow new listings, newly pending sales, and
price-cut shares; fusion of deviations from the naive forecast; and a validation-selected temperature with
shrinkage toward equal weights. None met the promotion rule, and the best was 0.002 percentage points
behind FA-ETS-d at 4 weeks (p= 0.42). In the housing domain, the value of the fusion step is therefore
that it selects and recomposes the useful channels, not that it combines them into a forecast more accurate
than the best of them.
5.1.6 Predictive versus Causal Attribution
Fusion weights measure predictive importance, not causation. For agentk,w k is the influence assigned to
its forecast given historical validation skill; it does not claim that the underlying evidence caused the same
share of the target change. A low weight can mean little forecasting signal, redundancy with another chan-
nel, a weak implementation, rare-regime dependence, or insufficient validation history. Accordingly,factor
attributionmeans predictive attribution within the forecasting architecture, not structural causal identifica-
tion.
5.2 Why Full-Window Evaluation Matters
The baseline experiments also exposed a significant evaluation artifact. An earlier diagnostic evaluated one
forecast origin per fold and horizon, and its comparison of the temporal channel with the naive forecast
scored horizons that fell inside the embargo. Under that design the 13-week forecast appeared to lose to
naive in most MSAs. A single forecast date is a poor estimator of general forecasting performance, so
every result reported here uses all eligible forecast origins in each test window: 2,610 MSA–origin pairs per
horizon in the backtest and 29 weekly origins per MSA in the holdout.
5.3 What the Housing Results Imply
FACTS-MAS improves on persistence at every evaluated horizon, on both Zillow series, in the backtest and
on the holdout, and it is more accurate than the TimesFM foundation model. On the holdout a chain-of-
thought language-model forecast comes close to it, with no statistically significant difference. It is not more
accurate than the strongest single model, factor-adjusted damped exponential smoothing, which it matches
at 8 weeks. The more important architectural point is that the final forecast is the product of tests that each
channel had to pass. Temporal dynamics and seasonality carry skill; the tested macro magnitude specifica-
tion is largely null; the intrinsic reversion and the event-magnitude map calibrate to zero. That pattern is
intentional. Available evidence is not the same as validated predictive evidence: the first determines which
agents can be proposed, and the second determines how strongly they may move the forecast. A less disci-
plined process could keep searching lags and prompts until a favorable statistic appears; FACTS-MAS treats
a null channel as an admissible outcome.
The Event Agent (event channel) and Macro Agent (exogenous channel) illustrate two different limits of
that distinction. An LLM can turn disaster metadata into structured categories, explanations, and confidence,
but that does not imply a calibrated continuous effect; usefulness can stop at interpretation, classification,
ordinal severity, or only at a cardinal forecast effect. The Macro agent fails for another reason: not semantic
ambiguity, but too little independent variation. National macro series are repeated across MSAs, so naive
correlations overstate the sample, and a panel with thousands of entity–time rows can still contain only a
modest number of macro shocks.
Fusion weights should be read in the same spirit. For agentk,w k is a predictive attribution, not a
causal contribution: a large temporal weight does not mean that temporal dynamics caused the same share
of the observed movement, and a small macro weight does not mean that monetary conditions are causally
24

irrelevant. Low weight can also mean redundancy, a weak implementation, rare-regime dependence, or
insufficient validation history. Regime analysis shows why apparent context effects need a placebo. An
earlier version of the system seemed to fail in the hiking and cutting regimes and to be repaired by regime-
aware weighting, but the failure disappeared once the seasonal channel was estimated properly, the repair
was partly an artifact of an equal-weight fallback, and randomly permuted regime labels did as well as the
true ones. Context-specific weighting reduces the observations behind each decision, and the rare regimes
where adaptation looks most attractive often have the least support. The tradeoff is context specificity
versus estimation reliability. Energy or unemployment applications will meet the same constraint whenever
extreme weather or recessions are uncommon in the validation sample.
5.4 Toward Cross-Domain Transfer
Housing shows that the procedure works inside one heterogeneous problem. It does not, by itself, show that
the procedure is domain agnostic. Transfer in FACTS-MAS is reconfiguration of evidence, not identity of
fitted parts.
For source domainD 1 and target domainD 2, we do not requireE (D1) =E (D2), norw (D1) =w (D2).
Identical weights across unlike targets would be a warning that fusion is insensitive to domain structure.
What should be preserved is the procedure: decompose the evidence, forecast from each channel, validate,
calibrate, attribute, and fuse. Formally, each domain supplies a configurationC (D) = (E (D),A (D),Θ (D),
H(D),R (D)), whereEis the evidence map,Athe channel models,Θthe calibrated parameters,Hthe
horizons, andRoptional regimes. The invariant pieces remain the shared interface, origin-time information
boundary, leakage-safe rolling evaluation, reference-relative skill, calibration, adaptive fusion, and predic-
tive attribution. Weights are re-estimated in the target domain:w (D1) ̸=w (D2) is expected rather than
treated as failed transfer. The transfer hypotheses are therefore architectural, not parametric.
T1: Architectural transfer.A new problem can be written in the same functional channels and contracts
without a new orchestrator.
T2: Adaptive predictive value.Channel importance changes across domains and is learned from each
domain’s own validation history.
T3: Forecasting benefit.After that reconfiguration, adaptive fusion should remain competitive with the
new domain’s simple reference and strong standalone models.
The unemployment-claims study (Section 4.3) supports T1: the claims series was written in the same
channels and contracts, and the housing code ran unchanged. It supports T2: the learned weights differ
from housing, with the seasonal channel carrying most of the weight. It supports T3 only in part: the
fused forecast beats the naive reference and the damped factor-adjusted model, but not the undamped factor-
adjusted model, which validation selected and which is the better single model for that series. The energy
configuration in Section 4.4 is planned and untested.
6 Conclusion
This paper introduced FACTS-MAS, a multi-agent forecasting framework that treats heterogeneous evi-
dence as a set of testable hypotheses rather than as a single pooled feature list. Each functional channel
produces an independent forecast; leakage-safe validation measures incremental skill against a reference;
calibration is allowed to return a null effect; adaptive fusion converts that evidence into weights that can
depend on horizon and regime when the sample can support the dependence.
25

On weekly U.S. housing inventory across 15 metropolitan areas, the frozen configuration attains backtest
MAPE of 2.118%, 3.622%, and 5.731% at 4, 8, and 13 weeks on Zillow’s smoothed series, against 4.194%,
7.225%, and 10.814% for last-value persistence, and 1.243%, 1.929%, and 3.045% on a pre-registered
holdout, against 3.122%, 5.445%, and 8.438%. The gains are smaller but still significant on the unsmoothed
series. FACTS-MAS is more accurate than the TimesFM 2.5 foundation model; on the holdout its error is
lower than that of a chain-of-thought language-model forecast built on the NEXUS prompt, but not signifi-
cantly so. It is not more accurate than a factor-adjusted damped exponential smoothing model, with which
it is equivalent at 8 weeks. Those results coexist with null and rejected channels: the tested macro magni-
tude specification adds little short-horizon skill, validation removes the intrinsic reversion and the cardinal
event-severity adjustment, and regime-aware weighting shows no benefit beyond horizon conditioning once
a placebo is applied. The contribution of FACTS-MAS is therefore the protocol itself: every channel is tested
against a reference, calibration may return a null, the final forecast is recomposed from the channels that
survive, and the result is checked on data held out until the configuration is frozen. Transferring the method
to a different domain requires a new evidence map, new channel models where needed, and new validation-
based calibration and weights, but the FACTS-MAS architecture, the shared interface, leakage-safe scoring,
and adaptive fusion procedure remain the same.
References
Abdul Fatir Ansari, Lorenzo Stella, Caner Turkmen, Xiyuan Zhang, Pedro Mercado, Huibin Shen, Olek-
sandr Shchur, Syama Sundar Rangapuram, Sebastian Pineda Arango, Shubham Kapoor, Jasper Zschieg-
ner, Danielle C. Maddix, Hao Wang, Michael W. Mahoney, Kari Torkkola, Andrew Gordon Wilson,
Michael Bohlke-Schneider, and Yuyang Wang. Chronos: Learning the language of time series.Transac-
tions on Machine Learning Research, 2024.
V . Assimakopoulos and K. Nikolopoulos. The theta model: A decomposition approach to forecasting.
International Journal of Forecasting, 16(4):521–530, 2000.
J. M. Bates and C. W. J. Granger. The combination of forecasts.Operational Research Quarterly, 20(4):
451–468, 1969.
Yoav Benjamini and Yosef Hochberg. Controlling the false discovery rate: A practical and powerful ap-
proach to multiple testing.Journal of the Royal Statistical Society: Series B, 57(1):289–300, 1995.
Christoph Bergmeir, Rob J. Hyndman, and Bonsoo Koo. A note on the validity of cross-validation for
evaluating autoregressive time series prediction.Computational Statistics & Data Analysis, 120:70–83,
2018.
C. Chang, Y . Shi, D. Cao, W. Yang, J. Hwang, H. Wang, J. Pang, W. Wang, Y . Liu, W.-C. Peng, and T.-F.
Chen. A survey of reasoning and agentic systems in time series with large language models, 2025. arXiv
preprint arXiv:2509.11575. Accepted toTransactions on Machine Learning Research.
Robert T. Clemen. Combining forecasts: A review and annotated bibliography.International Journal of
Forecasting, 5(4):559–583, 1989.
Abhimanyu Das, Weihao Kong, Rajat Sen, and Yichen Zhou. A decoder-only foundation model for time-
series forecasting. InProceedings of the 41st International Conference on Machine Learning, volume
235 ofProceedings of Machine Learning Research, pages 10148–10167, 2024.
S. S. S. Das, P. Goyal, M. Parmar, N. Peng, V . Tirumalashetty, C.-L. Li, R. Zhang, J. Yoon, and T. Pfister.
Nexus: An agentic framework for time series forecasting, 2026. arXiv preprint arXiv:2605.14389.
26

Francis X. Diebold and Roberto S. Mariano. Comparing predictive accuracy.Journal of Business & Eco-
nomic Statistics, 13(3):253–263, 1995.
John C. Driscoll and Aart C. Kraay. Consistent covariance matrix estimation with spatially dependent panel
data.Review of Economics and Statistics, 80(4):549–560, 1998.
Everette S. Gardner and Ed McKenzie. Forecasting trends in time series.Management Science, 31(10):
1237–1246, 1985.
C. W. J. Granger and Ramu Ramanathan. Improved methods of combining forecasts.Journal of Forecasting,
3(2):197–204, 1984.
Nate Gruver, Marc Finzi, Shikai Qiu, and Andrew Gordon Wilson. Large language models are zero-shot
time series forecasters. InAdvances in Neural Information Processing Systems, volume 36, 2023.
Peter R. Hansen, Asger Lunde, and James M. Nason. The model confidence set.Econometrica, 79(2):
453–497, 2011.
David Harvey, Stephen Leybourne, and Paul Newbold. Testing the equality of prediction mean squared
errors.International Journal of Forecasting, 13(2):281–291, 1997.
Arthur E. Hoerl and Robert W. Kennard. Ridge regression: Biased estimation for nonorthogonal problems.
Technometrics, 12(1):55–67, 1970.
Charles C. Holt. Forecasting seasonals and trends by exponentially weighted moving averages.International
Journal of Forecasting, 20(1):5–10, 2004. Reprint of the 1957 Office of Naval Research memorandum.
Sirui Hong, Mingchen Zhuge, Jonathan Chen, Xiawu Zheng, Yuheng Cheng, Jinlin Wang, Ceyao Zhang,
Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu,
and Jürgen Schmidhuber. MetaGPT: Meta programming for a multi-agent collaborative framework. In
International Conference on Learning Representations, 2024.
Rob J. Hyndman and Anne B. Koehler. Another look at measures of forecast accuracy.International Journal
of Forecasting, 22(4):679–688, 2006.
Rob J. Hyndman, Anne B. Koehler, Ralph D. Snyder, and Simone Grose. A state space framework for
automatic forecasting using exponential smoothing methods.International Journal of Forecasting, 18(3):
439–454, 2002.
J. Jang, H. Jin, H. Park, K. Chae, and T. Kim. What if TSF: A benchmark for reframing forecasting as
scenario-guided multimodal forecasting, 2026. arXiv preprint arXiv:2601.08509.
Ming Jin, Shiyu Wang, Lintao Ma, Zhixuan Chu, James Y . Zhang, Xiaoming Shi, Pin-Yu Chen, Yuxuan
Liang, Yuan-Fang Li, Shirui Pan, and Qingsong Wen. Time-LLM: Time series forecasting by reprogram-
ming large language models. InInternational Conference on Learning Representations, 2024.
Hans R. Künsch. The jackknife and the bootstrap for general stationary observations.The Annals of Statis-
tics, 17(3):1217–1241, 1989.
Bryan Lim and Stefan Zohren. Time-series forecasting with deep learning: A survey.Philosophical Trans-
actions of the Royal Society A, 379(2194):20200209, 2021.
Bryan Lim, Sercan Ö. Arık, Nicolas Loeff, and Tomas Pfister. Temporal fusion transformers for interpretable
multi-horizon time series forecasting.International Journal of Forecasting, 37(4):1748–1764, 2021.
27

Xiao Liu and Rong Pan. Boost-R: Gradient boosted trees for recurrence data.Journal of Quality Technology,
53(5):545–565, 2021.
Spyros Makridakis and Michèle Hibon. The M3-competition: Results, conclusions and implications.Inter-
national Journal of Forecasting, 16(4):451–476, 2000.
Spyros Makridakis, Evangelos Spiliotis, and Vassilios Assimakopoulos. The M4 competition: 100,000 time
series and 61 forecasting methods.International Journal of Forecasting, 36(1):54–74, 2020.
Dhruv D. Modi and Rong Pan. Enhancing transformer-based foundation models for time series forecasting
via bagging, boosting and statistical ensembles, 2025. arXiv preprint arXiv:2508.16641.
Paul Newbold and C. W. J. Granger. Experience with forecasting univariate time series and the combination
of forecasts.Journal of the Royal Statistical Society: Series A, 137(2):131–165, 1974.
Whitney K. Newey and Kenneth D. West. A simple, positive semi-definite, heteroskedasticity and autocor-
relation consistent covariance matrix.Econometrica, 55(3):703–708, 1987.
Yuqi Nie, Nam H. Nguyen, Phanwadee Sinthong, and Jayant Kalagnanam. A time series is worth 64
words: Long-term forecasting with transformers. InInternational Conference on Learning Representa-
tions, 2023.
Boris N. Oreshkin, Dmitri Carpov, Nicolas Chapados, and Yoshua Bengio. N-BEATS: Neural basis expan-
sion analysis for interpretable time series forecasting. InInternational Conference on Learning Repre-
sentations, 2020.
B. Pan, M. Cheng, Z. Liu, S. Yu, X. Tao, Y . Wu, Q. Liu, D. Lian, and E. Chen. CastFlow: Learning
role-specialized agentic workflows for time series forecasting, 2026. arXiv preprint arXiv:2604.27840.
Rong Pan. Holt–Winters exponential smoothing. InWiley Encyclopedia of Operations Research and Man-
agement Science. Wiley, 2011.
Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, and Michael S.
Bernstein. Generative agents: Interactive simulacra of human behavior. InProceedings of the 36th Annual
ACM Symposium on User Interface Software and Technology, 2023.
Ritong Qu, Allan Timmermann, and Yinchu Zhu. Comparing forecasting performance with panel data.
International Journal of Forecasting, 40(3):918–941, 2024.
David Salinas, Valentin Flunkert, Jan Gasthaus, and Tim Januschowski. DeepAR: Probabilistic forecasting
with autoregressive recurrent networks.International Journal of Forecasting, 36(3):1181–1191, 2020.
Slawek Smyl. A hybrid method of exponential smoothing and recurrent neural networks for time series
forecasting.International Journal of Forecasting, 36(1):75–85, 2020.
James H. Stock and Mark W. Watson. Combination forecasts of output growth in a seven-country data set.
Journal of Business & Economic Statistics, 22(4):405–422, 2004.
X. Tao, M. Cheng, C. Jiang, T. Gao, H. Zhang, and Y . Liu. Cast-R1: Learning tool-augmented sequential
decision policies for time series forecasting, 2026. arXiv preprint arXiv:2602.13802.
Leonard J. Tashman. Out-of-sample tests of forecasting accuracy: An analysis and review.International
Journal of Forecasting, 16(4):437–450, 2000.
28

Sean J. Taylor and Benjamin Letham. Forecasting at scale.The American Statistician, 72(1):37–45, 2018.
Allan Timmermann. Forecast combinations. In Graham Elliott, C. W. J. Granger, and Allan Timmermann,
editors,Handbook of Economic Forecasting, volume 1, pages 135–196. Elsevier, 2006.
Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang,
Xu Chen, Yankai Lin, Wayne Xin Zhao, Zhewei Wei, and Jirong Wen. A survey on large language model
based autonomous agents.Frontiers of Computer Science, 18:186345, 2024.
Lizhi Wang, Dawei Lu, Xiaohong Wang, Rong Pan, and Zhuo Wang. Ensemble learning for predicting
degradation under time-varying environment.Quality and Reliability Engineering International, 36(4):
1205–1223, 2020.
Xiaoqian Wang, Rob J. Hyndman, Feng Li, and Yanfei Kang. Forecast combinations: An over 50-year
review.International Journal of Forecasting, 39(4):1518–1547, 2023.
Qingsong Wen, Tian Zhou, Chaoli Zhang, Weiqi Chen, Ziqing Ma, Junchi Yan, and Liang Sun. Trans-
formers in time series: A survey. InProceedings of the 32nd International Joint Conference on Artificial
Intelligence, pages 6778–6786, 2023.
Peter R. Winters. Forecasting sales by exponentially weighted moving averages.Management Science, 6
(3):324–342, 1960.
Gerald Woo, Chenghao Liu, Akshat Kumar, Caiming Xiong, Silvio Savarese, and Doyen Sahoo. Uni-
fied training of universal time series forecasting transformers. InProceedings of the 41st International
Conference on Machine Learning, volume 235 ofProceedings of Machine Learning Research, pages
53140–53164, 2024.
Haixu Wu, Jiehui Xu, Jianmin Wang, and Mingsheng Long. Autoformer: Decomposition transformers with
auto-correlation for long-term series forecasting. InAdvances in Neural Information Processing Systems,
volume 34, 2021.
Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun Zhang,
Shaokun Zhang, Jiale Liu, Ahmed Awadallah, Ryen W. White, Doug Burger, and Chi Wang. AutoGen:
Enabling next-gen LLM applications via multi-agent conversation. InConference on Language Modeling,
2024.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. Re-
Act: Synergizing reasoning and acting in language models. InInternational Conference on Learning
Representations, 2023.
Ailing Zeng, Muxi Chen, Lei Zhang, and Qiang Xu. Are transformers effective for time series forecasting?
InProceedings of the AAAI Conference on Artificial Intelligence, volume 37(9), pages 11121–11128,
2023.
Haoyi Zhou, Shanghang Zhang, Jieqi Peng, Shuai Zhang, Jianxin Li, Hui Xiong, and Wancai Zhang. In-
former: Beyond efficient transformer for long sequence time-series forecasting. InProceedings of the
AAAI Conference on Artificial Intelligence, volume 35(12), pages 11106–11115, 2021.
29
