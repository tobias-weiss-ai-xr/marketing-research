---
title: Regime-Aware Portfolio Management via Retrieval-Augmented LLM-Guided Expert Switching
url: https://arxiv.org/abs/2608.28252
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Ahmad Asadi
- Reza Safabakhsh
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.28252
pages: 43
chars: 76991
fetched_at: '2026-11-08T13:19:16+00:00'
kb_version: 1
---

# Regime-Aware Portfolio Management via Retrieval-Augmented LLM-Guided Expert Switching

Regime-Aware Portfolio Management via
Retrieval-Augmented LLM-Guided Expert
Switching
Ahmad Asadi 1 and Reza Safabakhsh 1
1Deep Learning Lab, Computer Engineering Department,
Amirkabur University of Technology, Hafez A venue, Tehran, Iran
August 31, 2026
Abstract
Financial markets are inherently non-stationary, making the effec-
tiveness of individual portfolio-management strategies highly depen-
dent on changing market conditions. This work proposes a retrieval-
augmentedexpert-switchingframeworkthatdynamicallyselectsportfolio-
management experts based on their historical performance under similar
market situations. A dual-stream variational autoencoder represents
asset-level and market-wide information, while a retrieval-based knowl-
edge base stores historical situations and expert performance. During
inference, an instruction-tuned LLM reasons over the retrieved evidence
to identify the most appropriate expert rather than directly generating
portfolio actions. We further establish a monotonicity property showing
that adding a locally superior expert cannot degrade the switching
mechanism’s performance. Experiments across cryptocurrency, stock,
and foreign-exchange markets show that the proposed selector achieves
the highest cumulative return and Sharpe ratio among the evaluated se-
lection strategies in all three markets. In the stock market, for example,
cumulative return increases from 26% for the best fixed expert to 34%,
while the Sharpe ratio improves from 0.74 to 0.96. Ablation results
confirm the importance of both retrieval and LLM reasoning, while
1
arXiv:2608.28252v1  [cs.AI]  28 Aug 2026

experiments with different expert-pool sizes demonstrate the value
of complementary expertise. Overall, the findings support retrieval-
grounded expert switching as an effective approach to adaptive portfolio
management in non-stationary financial environments.
Keywords: Knowledge-based systems, Retrieval-augmented generation,
Large language models, Expert switching, Portfolio management, Financial
markets
1 Introduction
Portfolio management in financial markets, particularly within the context
of high-frequency trading, presents significant challenges due to the inherent
non-stationarity of real-world data, abrupt price fluctuations driven by exoge-
nous shocks and news events, often-irrational trader behavior, and intricate
interdependencies among financial instruments [Cliff and Rollins, 2020]. Con-
ventional approaches typically assume a stationary data-generating process
[Cakmak and Özekici, 2006] and stable factor relationships over time [Jacobs
et al., 2005]. In contrast, modern deep learning-based frameworks seek to
address these complexities by scaling model capacity through a substantial
increase in parameterization. However, training such large-scale models, along
with ensuring their robustness and safety under extreme or anomalous market
conditions, introduces additional practical constraints that hinder deployment.
An alternative formalism for capturing such nonlinear dynamics is through
regime-switching representations, wherein the data-generating process is char-
acterized by distinct latent states. Nevertheless, this paradigm introduces
further methodological challenges, as it requires simultaneous learning of
both the regime identities and the corresponding conditional models, thereby
compounding the overall training complexity [Liu and Garrett, 2023].
Deep learning has attracted attention in financial forecasting, with a
wide range of architectures; including recurrent neural networks [Sharma and
Shekhawat, 2022], convolutional designs [Popa et al., 2020], temporal attention
mechanisms [Asadi and Safabakhsh, 2025], and deep reinforcement learning
frameworks [Taghian et al., 2022], demonstrating varying degrees of success
in predicting asset returns, volatility, and directional trends [Choudhary
et al., 2025]. Among these, reinforcement learning (RL) offers a particularly
compelling paradigm, as it naturally formalizes portfolio optimization as a
2

sequential decision-making process. In particular, policy gradient and actor-
critic methods have proven effective in navigating the intricate trade-offs
between risk and return under evolving market conditions [Wei et al., 2025,
Jiang et al., 2024]. End-to-end deep learning systems are prone to overfitting
the specific market regularities present in their training sets; however, they fail
when confronted with unprecedented shocks or abrupt changes in volatility
regimes.
To address the inherent variability of financial environments, mixture-of-
experts (MoE) architectures have been proposed as a promising alternative to
monolithic models [Wei et al., 2025]. In this framework, a set of specialized
expert networks is maintained, each calibrated to a distinct region of the
input space, thereby enabling adaptive responses to changing market con-
ditions. In financial applications, MoE models typically employ supervised
gating networks [Vats et al., 2024] or meta-learning strategies [Masoudnia
and Ebrahimpour, 2014] to dynamically combine expert outputs. These
approaches have been shown to enhance predictive accuracy, particularly
under controlled experimental settings.
Nevertheless, a critical limitation emerges when the system encounters
market regimes that were not represented during training. Under such condi-
tions, where the test-time distribution deviates substantially from the training
distribution, the gating mechanism becomes unreliable, often assigning dis-
proportionate weights to mismatched experts. This misallocation results
in significant portfolio drawdowns, undermining the robustness that MoE
architectures are designed to achieve. Consequently, the effectiveness of these
models remains contingent upon the representativeness of the training data,
and their generalization capacity to novel or extreme regimes remains an open
and pressing research question.
The growing adoption of Large Language Models (LLMs) in finance has
opened new avenues for integrating structured and unstructured data, such
as news and reports, into trading systems. Their chain-of-thought reasoning
capabilities enable semantically informed decision-making, supporting appli-
cations like sentiment analysis, automated reporting, and strategy generation
[Kong et al., 2024, Feng and Sinchai, 2025]. Recent efforts have further com-
bined LLMs with reinforcement learning or retrieval-augmented frameworks
to incorporate historical context and domain knowledge at inference time [Liu
et al., 2024].
We propose a situation-based expert switching framework, in which expert
selection is framed as a sequential decision problem rather than an inherent
3

property of a single predictive model. At each decision step, the system
evaluates the current market state against a repository of historical situations
and assesses the historical performance of each expert under analogous con-
ditions. To render this selection process evidence-based and risk-aware, we
construct a Statement of Performance (SoP) for each expert during an offline
indexing phase. Each SoP encapsulates risk-adjusted profitability across a
distribution of historical market contexts. During inference, these statements
serve as empirical evidence, enabling the switcher to determine not only the
prevailing market regime, but also which expert has demonstrated historical
effectiveness within that regime.
We formalize this selection mechanism mathematically and establish a
theoretical foundation through a monotonicity property: the introduction of
a new expert that outperforms the existing pool within a given sub-domain
guarantees non-degradation of overall system performance. This property is of
practical significance, as it permits incremental expansion of the expert pool;
enablingtheintegrationofimprovedspecialistswithoutretrainingamonolithic
model from scratch. Importantly, this result distinguishes our approach
from conventional strategies that pursue generalization primarily through
increases in model scale. The switching mechanism is grounded in retrieval-
based reasoning. Market situations are encoded via a dual-stream Variational
Autoencoder, which extracts complementary representations from two sources:
asset-level technical indicators and market-wide macroeconomic features. The
resulting compact embeddings facilitate similarity-based retrieval of historical
episodes characterized by analogous price dynamics. The retrieved evidence,
combined with the expert SoPs, is supplied to the model switcher, which
estimates the most appropriate expert to activate for subsequent portfolio
construction.
Collectively, the proposed framework offers an alternative paradigm for
adaptive portfolio management; one that emphasizes specialization across
experts rather than scaling within a single model. The system begins with
a predefined set of experts, incorporates a retrieval mechanism to ground
expert selection in historical precedent, and integrates risk-aware performance
statements to inform decisions based on realized outcomes. As new experts
become available, they can be seamlessly incorporated into the pool, with the
theoretical monotonicity result ensuring that such additions do not degrade
performance, while the retrieval mechanism ensures their deployment under
relevant conditions. Together, these components constitute a coherent and
extensible framework for portfolio management in non-stationary financial
4

environments.
2 Literature Review
2.1 Adaptive Portfolio Allocation
Mean-variance portfolio optimization relies on assumptions of approximately
Gaussian returns and stable asset correlations. Both assumptions become
problematic in markets characterized by volatility clustering, structural breaks,
and rapidly changing cross-asset dependencies [Nguyen, 2025]. Machine learn-
ing methods relax these assumptions by learning nonlinear relationships from
market observations [Feng and Sinchai, 2025]. Their empirical performance,
however, varies substantially across market conditions, suggesting that the ef-
fectiveness of a portfolio model depends partly on the state of the environment
in which it operates.
A common early strategy combined learned representations with conven-
tional portfolio optimization. Predictive models extracted features from price
observations, after which a separate optimizer determined portfolio weights.
CNN- and recurrent-network-based predictors improved risk-adjusted per-
formance in several such hybrid systems [Nguyen, 2025]. Correlation-aware
CNN-Transformer architectures subsequently incorporated cross-asset depen-
dencies more explicitly and introduced cross-market transfer learning [Feng
and Sinchai, 2025]. The allocation stage remained separate from representa-
tion learning in these models. Consequently, changes in market dynamics were
handled primarily through model retraining or allocation heuristics rather
than through an adaptive policy.
2.2 Regime-Aware Reinforcement Learning
Deep reinforcement learning removes the separate prediction-and-optimization
stages by allowing an agent to map market observations directly to portfolio
decisions. Jiang and Liang [2017] showed that a CNN-based agent trained on
raw price tensors could be applied across equity and cryptocurrency markets.
Later architectures placed greater emphasis on temporal structure. The
encoder-decoder models of Taghian et al. [2022, 2023], for example, separate
long-horizon temporal representation from short-horizon decision making.
Other studies have incorporated behavioral assumptions, such as loss aversion
5

and overconfidence, into actor-critic policies [Charkhestani and Esfahanipour,
2026], while Alidousti et al. [2025] used a double-DQN formulation to reduce
overestimation bias. Transformer-based reinforcement learning extends this
line of work by modeling longer temporal dependencies than conventional
recurrent architectures [Ren et al., 2025].
The main difficulty for a single DRL policy is its dependence on patterns
that were useful during training. When the underlying market dynamics
change, the same policy can continue to exploit relationships that are no
longer present [Rezaei and Nezamabadi-Pour, 2025]. Several studies therefore
introduce multiple policies or explicitly model market regimes. Choudhary et
al. [Choudhary et al., 2025] use multi-agent PPO with differentiated objectives
based on log-return, Sharpe ratio [Sharpe, 2005], and drawdown, producing
more stable allocations than a single-agent formulation. Regime-switching sys-
tems instead associate different DRL agents with detected market conditions
and report improvements in Sharpe and Sortino ratios for commodity and
futures markets [Wang and Liu, 2025, Sortino and Price, 1994]. Zhang et al.
[2025] follow a related strategy by defining volatility regimes and combining
regime-specific ensemble forecasts with adaptive mean-variance allocation.
These studies differ mainly in how regime information reaches the trading
policy. Some methods infer the regime implicitly through the learned state
representation, whereas others introduce an explicit controller that determines
whichpolicyshouldbeactive. Explicitswitchingprovidesanaturalmechanism
for handling heterogeneous market conditions, but it also makes the quality of
the switching signal critical. A regime classifier that reacts slowly can retain
an inappropriate policy after a structural change; one that reacts too quickly
can cause unnecessary switching between experts.
2.3 Mixture-of-Experts and Expert Routing
Mixture-of-experts (MoE) architectures address policy heterogeneity by main-
taining several specialists and learning a routing mechanism that determines
which specialist receives each state. In portfolio applications, Transformer-
based spatio-temporal representations have been combined with learned gating
networks to select among DRL experts, with improvements reported in cu-
mulative and risk-adjusted returns [Wei et al., 2025]. Other systems use
hypernetworks to modify expert parameters according to detected regime
information, improving regime identification and predictive performance [Sun
et al., 2025]. Gu et al. [2025] likewise use an MoE formulation to account for
6

non-stationarity and stochastic volatility.
Therouting mechanismis thekey distinctionamongthese models. Learned
gatesgenerallyinferexpertsuitabilityfromthecurrentrepresentation, whereas
performance-basedmechanismscanuserecentoutcomesasanindirectmeasure
of suitability. Recent performance is attractive because it is inexpensive and
directly related to the trading objective, but it is also noisy. A short sequence
of favorable or unfavorable returns may reflect transient randomness rather
than a persistent change in regime. During abrupt transitions, a router based
primarily on recent performance can therefore favor an expert whose historical
behavior is poorly matched to the newly emerging conditions.
Historical comparison offers a different basis for routing. Instead of asking
which expert has performed best most recently, the router can ask which
previously observed market states resemble the current state and examine
expert behavior in those states. Such a mechanism shifts the routing problem
from short-horizon performance estimation toward retrieval of comparable
market episodes. The distinction is particularly relevant when the current
regime has not appeared frequently in the recent training window but has
recognizable historical counterparts.
2.4 LLMs for Financial Decision Support
Large language models have primarily entered financial systems through the
processing of information that is difficult to represent directly in numerical
market features. Huang et al. [2025] combine ChatGPT-based stock selection
with portfolio optimization, while Yin and Guo [2026] investigate chain-of-
thought prompting with ChatGPT 4.0 for financial forecasting and portfolio
optimization. Other studies incorporate LLM-derived sentiment, macroeco-
nomic information, and textual summaries into DRL state representations,
reporting improvements relative to quantitative baselines [Liu et al., 2024,
Unnikrishnan, 2024]. Formulaic signals and textual descriptions generated by
LLMs have similarly been investigated as higher-level features for prediction
and interpretation.
A separate line of research assigns the LLM a coordination role. TradEx-
pert uses several specialized LLM experts with different knowledge domains
and combines their outputs through a general expert for prediction or ranking
[Ding et al., 2024]. Liu and Lo [2025] replace conventional neural routing
with an LLM-based selector, using contextual reasoning and broader financial
knowledge to distinguish among experts. TradingAgents extends the multi-
7

agent formulation by assigning separate agents to analysis, risk management,
and trading before synthesizing their outputs [Xiao et al.]. Similar multi-agent
designs have also been explored for cryptocurrency portfolio management.
The empirical evidence places an important constraint on these uses of
LLMs. Large-scale benchmarks show that LLM-based trading agents do not
consistently outperform buy-and-hold strategies over multi-month evaluation
periods [Chen et al., 2025]. The result suggests that language-based reasoning
alone is insufficient for reliable portfolio control. LLMs appear more suitable
for tasks involving information synthesis, contextual interpretation, and
coordination than for generating precise portfolio actions at every decision
step. For a portfolio system with quantitative experts, this distinction makes
the LLM’s role narrower but also easier to evaluate: the language model can
contribute contextual information or assess relationships among retrieved
market episodes without being responsible for the final portfolio weights.
2.5 Research Gaps and Proposed Contributions
The literature leaves three related issues unresolved. First, DRL and MoE
systems commonly learn expert selection from the current state representation,
a learned gate, or recent performance. These signals do not necessarily indicate
whether an expert has previously succeeded under market conditions similar
to those observed at the current decision point. Second, explicit regime-
aware systems depend on regime definitions or classifiers whose errors can
directly affect policy selection. Third, LLM-based financial systems have
demonstrated value in information processing and coordination, but their use
as direct trading agents remains inconsistent.
The proposed method places these three observations in a single routing
mechanism. For a current market state, historical observations are retrieved
according to their similarity to the present state. Expert performance in the
retrieved episodes then provides the basis for selecting the portfolio policy.
The retrieved episodes also provide an empirical reference for assessing how
well the candidate experts behaved under comparable conditions. The LLM
operates on this contextual information instead of producing portfolio weights
directly; its role is to encode semantic information and assist with reasoning
about regime similarity.
The resulting design treats expert selection as a historical matching
problem. The central question is not simply which expert has performed well
recently, but which expert has demonstrated suitable behavior in market states
8

resembling the one currently observed. This distinction connects regime-aware
reinforcement learning with MoE routing while giving the LLM a bounded
decision-support role. It also provides a direct basis for evaluating expert
selection through the retrieved historical episodes rather than relying solely
on the internal state of a learned gating network.
3 Proposed Method
3.1 Overview
The proposed system maintains a pool of specialized portfolio experts and
selects among them at inference time using historical market states as refer-
ence points. The procedure has an offline and an online component. During
offline processing, historical market windows are converted into latent state
representations, each expert is evaluated over a fixed forward horizon, and
the resulting state–performance pairs are stored in a vector database. Dur-
ing inference, the current market window is embedded in the same latent
space, similar historical windows are retrieved, and the corresponding expert
outcomes are used to rank the available policies.
The design separates the expensive construction of the historical perfor-
mance index from the online selection step. Expert evaluation and indexing
are performed once for each historical window. Online inference then requires
only state encoding, nearest-neighbor retrieval, and expert scoring. The
retrieved observations also provide an explicit record of why a particular
expert is favored: its selection can be traced to the behavior of that expert
under historically similar market conditions.
3.2 System Architecture and Data Flow
Figure 1 shows the complete data flow. The lower pipeline constructs the
historical index, whereas the upper pipeline processes the current market
state and selects an expert.
The market state is represented through two feature streams. The first
contains asset-level technical information, including returns, momentum,
volatility, and volume characteristics for each asset. The second describes
market-wide conditions through aggregate trend, volatility, and liquidity mea-
sures. Separate encoders transform these streams into latent representations,
9

which are subsequently combined into a single vectorht. Using two streams
preserves information about individual assets while retaining conditions that
affect the market as a whole.
The offline pipeline associates each historical representation with the real-
ized performance of every expert over a fixed forward horizon. The resulting
records contain both numerical performance measures and a Statement of
Performance (SoP), which summarizes the corresponding market episode and
the observed behavior of each expert. These records form the evidence base
used during online routing.
At time t, the current state is processed by the same encoders and repre-
sented by ht. Approximate nearest-neighbor search identifies historical states
close to ht. The performance records attached to these neighbors provide
estimates of how the experts have behaved under comparable conditions. The
LLM receives these retrieved records together with the current market de-
scription and is used for contextual assessment and uncertainty calibration. It
does not generate portfolio weights. The selected expert remains responsible
for producing the portfolio allocation.
3.3 Theoretical Framework: Expert Switching with His-
torical Risk Evaluation
The switching problem can be formulated over a distribution of latent market
states. Let S denote the space of possible market states andP a probability
measure over S. A state may represent a combination of macroeconomic con-
ditions, volatility characteristics, liquidity conditions, and structural market
changes. The latent state is not directly observed at decision time; instead,
the system constructs an observable representation from recent market data
and uses historical observations to identify similar states.
Let the available experts beEN = E1, . . . , EN . Each expert Ei maps an
observed market representation to a portfolio weight vector. Its realized risk-
adjusted utility in states is denoted byUi(s). This quantity is unknown when
the portfolio decision is made and is estimated from historical observations.
The value of a switching policyπN : S →1, . . . , Nis
V (πN ) =
Z
S
UπN (s)(s), dP(s). (1)
The purpose of adding a new specialist is therefore not simply to increase
the number of available policies. The additional expert is useful only when
10

Figure 1: Overall architecture of the proposed retrieval-augmented adaptive
portfolio management framework. The lower pipeline constructs the historical
index by encoding market states and evaluating expert performance. The
upper pipeline retrieves comparable historical states, combines their perfor-
mance records with contextual information, and selects the expert used for
portfolio allocation.
its inclusion creates states in which the switching rule can identify a policy
with at least as much utility as the best existing expert.
3.3.1 Historical Evidence and Switching Rule
For a current states, let Ht(s) denote the historical episodes retrieved as
similar to that state. The quantitative component of the router derives
an expert-specific estimate from the outcomes observed in these episodes.
The LLM receives the same evidence and produces a contextual risk/return
assessment:
ρi(s) = M (Ht(s), Ei) . (2)
11

Here, ρi(s) represents the assessment used by the switching procedure; it
should not be interpreted as a direct observation of the unobservable quantity
Ui(s). The historical performance records provide the numerical basis for the
estimate, while the LLM interprets the retrieved context and contributes to
its calibration.
The active expert is selected according to the resulting scores. When
a new specialist EN +1 is introduced, the corresponding policyπN +1 either
retains the incumbent expert or activates the new specialist according to the
switching margin specified below.
3.3.2 Conditions for Non-Decreasing Performance
The monotonicity result relies on three assumptions concerning estimation
error, switching conservatism, and specialist behavior.
Axiom 1(Bounded Estimation Error / Empirical Alignment). The assess-
ment ρi(s) is uniformly close to the true utility. There existsϵ > 0 such
that
sup
s∈S
|ρi(s) − Ui(s)| ≤ϵ, ∀i ∈ 1, . . . , N+ 1. (3)
The practical implementation approximates this condition by grounding as-
sessments in observed historical returns, drawdowns, and related performance
measures rather than allowing unrestricted extrapolation.
Axiom 2(Conservative Switching Logic). At state s, the switcher evaluates
all experts in the poolEN = E1, . . . , EN. Let the incumbent expert beπN (s)
and let
e∗(s) = arg max
i∈1,...,N
ρi(s) (4)
denote the expert with the highest estimated utility. The switcher activatese∗(s)
only when its estimated advantage over the incumbent exceeds the switching
threshold τ ≥ 2ϵ:
πN (s) =
(
e∗(s), ρ e∗(s)(s) − ρπN (s)(s) > τ,
πN (s) otherwise. (5)
The threshold prevents the switcher from replacing the incumbent when the es-
timated advantage of the best available expert is within the expected estimation
error.
12

Axiom 3(Specialist Dominance and Tail Protection). The new expertEN +1
is intended for a subsetSR ⊂ Swith P(SR) > 0. Within this region, the
specialist has a utility advantage of at leastδ, where δ > τ+ 2ϵ. Thus,
UN +1(s) ≥ UπN (s)(s) + δ, s ∈ SR. (6)
Outside the specialist region, its utility is assumed unlimited.
3.3.3 Operational Interpretation of the Conditions
The three conditions translate into concrete constraints on the routing proce-
dure. Empirical alignment limits the range of values supplied to the LLM;
conservative switching requires a candidate expert to demonstrate a suffi-
ciently large advantage before replacing the incumbent; and tail protection
requires explicit examination of periods in which the specialist is expected to
provide its main benefit.
Table 1 summarizes this correspondence. The prompt instructions are not
themselves proofs of the mathematical assumptions. They are implementation
heuristics intended to make the LLM’s behavior more consistent with those
assumptions. The prompt was refined using a validation set, as described in
Section 3.4.
Table 1: Mapping of the switching assumptions to LLM evaluation constraints.
Condition Mathematical
requirement
Operational constraint
Axiom 1 sups |ρi − Ui| ≤
ϵ
Restrict quantitative assessments to the
empirical range of retrieved return and
drawdown observations. Missing regimes
are handled using historical baseline statis-
tics.
Axiom 2 τ ≥ 2ϵ Require a candidate expert to exceed the
incumbent by a margin larger than the es-
timated uncertainty before recommending
a switch.
Axiom 3 δ > τ+ 2ϵ Evaluate specialist performance in extreme
conditions.
13

3.3.4 Monotonicity Result
Theorem 1 (Monotonic Expert-Pool Performance). Under Axioms 1–3,
adding a specialist EN +1 to the expert pool does not decrease the expected
utility: V (πN +1) ≥ V (πN ). Furthermore, the specialist produces a strict utility
improvement on its target regionSR. If specialists are subsequently added so
that their target regions cover the relevant state space, the resulting sequence
of policy values is non-decreasing and converges to a limiting value bounded
above by the optimal achievable utility.
Proof. Consider first a state s /∈ SR. If the switching condition is not
satisfied, the incumbent remains active andπN +1(s) = πN (s), so the utility is
unchanged.
If the switch occurs, then
ρN +1(s) − ρπN (s)(s) > τ.
By Axiom 1,
UN +1(s) ≥ ρN +1(s) − ϵ, (7)
UπN (s)(s) ≤ ρπN (s)(s) + ϵ. (8)
Consequently,
UN +1(s) − UπN (s)(s) > τ− 2ϵ. (9)
Since τ ≥ 2ϵ, the utility difference is non-negative. A switch outside the
specialist’s target region therefore cannot reduce utility under the stated error
bound.
Now consider s ∈ SR. Axiom 3 gives
UN +1(s) − UπN (s)(s) ≥ δ.
Using Axiom 1,
ρN +1(s) − ρπN (s)(s) ≥ δ − 2ϵ. (10)
Because δ > τ+ 2ϵ, it follows that
δ − 2ϵ > τ.
The specialist therefore satisfies the switching condition throughoutSR. Its
contribution to the expected utility is at least
∆V ≥
Z
SR
δ dP(s) = δP(SR) > 0. (11)
14

Combining the two regions gives
V (πN +1) ≥ V (πN ).
For a sequence of specialist additions, the same argument gives
V (π1) ≤ V (π2) ≤ · · · ≤V (πK).
The sequence is bounded above by the best achievable utility
V ∗ =
Z
S
sup
E
UE(s) dP(s),
and therefore has a limit. If the added specialists cover the relevant state space
and satisfy the stated dominance conditions, this limiting value approaches
V ∗.
3.4 Prompt Design and Uncertainty Calibration
The practical implementation was designed around the limitations observed
during validation. Early prompt versions permitted the LLM to infer returns
outside the range represented in the retrieved historical records. These re-
sponses were frequently overconfident. The final prompt constrains numerical
assessments to empirical observations and requires the model to fall back to
historical baseline statistics when the retrieved evidence is sparse.
Five prompt iterations were evaluated on a validation set. The mean
absolute estimation error decreased from approximately18% in the earlier
versions to 11% after the empirical-range constraints were introduced. The
final prompt implements three specific restrictions:
• Empirical grounding: risk and return assessments are derived from
the historical MDD, realized information ratios, and other performance
observations supplied in the retrieved context.
• Conservative margining:a newly introduced expert receives a risk
penalty before comparison with the incumbent, and the candidate is
not preferred unless its estimated advantage exceeds the specified noise
margin.
15

• Tail-event analysis: the evaluator examines extreme drawdowns,
liquidity squeezes, and regime transitions separately from ordinary
observations. A specialist’s advantage must be localized to its intended
regime without creating a severe deterioration elsewhere.
The resulting system prompt is shown in Prompt Specification 3.4 . Its
output is restricted to a structured JSON representation so that the LLM
assessment can be incorporated into the numerical routing procedure without
requiring free-form text parsing.
System prompt used by the LLM risk evaluator. The instructions
constrain numerical assessments to retrieved empirical evidence
and require explicit treatment of switching margins and tail
conditions.
ROLE. You are a financial risk analyzer operating within a dynamic Mixture-
of-Experts (MoE) portfolio system.
EMPIRICAL ALIGNMENT.
• Base risk-adjusted assessments on the observed historical Maximum Draw-
down (MDD) and realized Information Ratios provided in the context.
• Do not extrapolate returns beyond the empirical observations.
• If evidence for a regime is sparse, use the historical baseline mean.
CONSER V A TIVE MARGINING.
• When evaluating a new candidate expertE(N +1), apply the specified risk
penalty buffer τ.
• Do not prefer the candidate unless its estimated advantage over the
incumbent exceeds the estimated noise level by the required margin.
T AIL-EVENT SEP ARA TION.
• Examine extreme drawdowns, liquidity squeezes, and regime shifts.
• If a candidate is a specialist, identify the regime in which its advantage
is observed.
• Verify that performance outside this regime does not fall below the weakest
baseline expert.
16

OUTPUT FORMA T.The evaluator must return a structured record:
{
"expert_id": "E_N+1",
"calculated_rho": <float>,
"confidence_bound_epsilon": <float>,
"regime_separation_margin_tau": <float>,
"tail_optimal_flag": <boolean>
}
3.5 Market State Decomposition and Feature Modeling
At each time stept, the market state is represented by two rolling-window
feature tensorsof lengthL. Thefirst describesasset-specific technicalbehavior:
Stech t ∈ RL×A×F1, where A is the number of assets andF1 is the number of
asset-level features. The feature set includes log-returns, RSI, MACD, ATR,
realized volatility, and volume changes.
The second representation describes market-wide conditions: Smkt t ∈
RL×F2. It contains aggregate trend indicators, volatility-regime measures, and
liquidity variables.
The two representations retain different types of information. Asset-level
features describe relative behavior among individual instruments, whereas
market-wide features describe conditions shared across the portfolio. Keeping
the streams separate before encoding avoids forcing both types of information
into a single input representation. The resulting latent representation is used
for historical state matching, where preserving both sources of information is
important for identifying comparable episodes [Bali and Weigert, 2024, Asadi
and Safabakhsh, 2025].
All features are standardized using rolling z-score normalization. The
rolling procedure limits the effect of scale changes and reduces the influence
of heteroskedasticity on the state representation.
3.6 Dual-Stream Transformer-VAE Embedding
Each feature stream is encoded with a pretrained Transformer-VAE from
Asadi and Safabakhsh [2025]. Forx ∈ tech, mkt, the encoder mapsSx t to the
Gaussian posterior
17

qϕx(zx | Sx t ) = N (µx(Sx t ), Σx(Sx t )) , (12)
where the mean and diagonal covariance are generated by the temporal
Transformer encoder. A latent representation is sampled using
zx = µx + ϵ ⊙ σx, ϵ ∼ N(0, I). (13)
During pretraining, the sampled representation is passed through the
decoder to reconstruct the input. After pretraining, the decoder is removed
and the encoder is retained for market-state representation.
The two latent vectors are concatenated:
ht = [ztech t | zmkt t ] ∈ RD. (14)
The same representation function is used in both phases of the system.
Historical states are indexed usinghτ, and the current state is represented by
ht before nearest-neighbor retrieval. Using the same encoder in both cases
ensures that the distance used during retrieval is defined in a common latent
space.
3.7 Offline Indexing
Algorithm 1 describes the construction of the historical index. For each
historical time stepτ, the system constructs the two market-state represen-
tations and computes hτ. Every expert is then evaluated from that state
over the forward horizonH. The resulting record contains cumulative return,
Sharpe ratio, and maximum drawdown. A Statement of Performance (SoP)
is generated from the same episode and records the market context, observed
expert behavior, and relevant uncertainty factors.
An index entry is therefore represented as
Dτ = (hτ , Re τ , SoPe τ ) , e ∈ 1, . . . , E. (15)
3.8 Online Retrieval and Portfolio Decision
Algorithm 2 summarizes the online procedure. The current market window
is first transformed intoStech t and Smkt t and encoded asht. The system then
retrieves the K historical states closest toht:
18

Algorithm 1Offline Regime Indexing and Expert Performance Grounding
Require: Historical market data, expert setE = E(e) ∗ e = 1E, horizon H
1: for each historical time stepτ do
2: Construct S ∗ τ tech, Smkt τ
3: Compute embedding hτ using the dual-stream T-VAE
4: for each expert E(e) do
5: Execute expert policy fromSτ
6: Evaluate realized performanceR(e) τ over horizon H
7: end for
8: Generate Statement of PerformanceSoP ∗ τ
9: Store (h ∗ τ, R(e) τ , SoP(e) τ )
10: end for
Nt = KNN (ht, hτ , K) . (16)
The performance of each expert is estimated from the retrieved episodes.
Let sim(ht, hτ ) denote the similarity between the current and retrieved states.
The normalized retrieval weight is
wτ = sim(ht, hτ )P
j∈Nt sim(ht, hj) , (17)
and the similarity-weighted performance estimate for experte is
ˆR(e) t = X
τ ∈N ∗t
w ∗ τ R(e) τ . (18)
The retrieved SoPs, performance summaries, and current market descrip-
tion are also supplied to the LLM. The model decides on selecting the best
expert model among the existing ones based on the current market situation
and the risk-return behavior profile of the experts embedded into retrieved
SoPs.
4 Experimental Results
We evaluate the proposed retrieval-augmented expert-switching framework
independently on three financial market classes: cryptocurrency, stocks,
19

Algorithm 2Online Retrieval and Portfolio Decision-Making
Require: Current market data, vector database, expert setE(e)
1: Construct Stech t , Smkt t
2: Compute embedding ht using the dual-stream T-VAE
3: Retrieve K nearest historical regimesNt
4: for each expert E(e) do
5: Compute similarity-weighted performance ˆR(e) t
6: Compute weighted uncertaintyσ(e) t
7: Query the LLM using retrieved SoPs and market context to gete∗
8: end for
9: Generate portfolio weightswt using E(e∗)
10: return wt
and foreign exchange. The effect of important components in the proposed
framework are investigated and the performance of the proposed model is
compared with the baseline portfolio management methods.
Each experiment is conducted once for each market using the complete
30-symbol panel of that market. Consequently, the reported values are point
estimates for a single experimental run rather than averages over multiple
random seeds. This design makes the market-level comparison explicit and
avoids conflating differences between market classes with differences between
repeated runs.
4.1 Experimental Setup
Dataset We construct a multi-market daily OHLCV dataset covering three
market classes: cryptocurrencies, stocks, and foreign-exchange pairs. For
each market, top 30 assets regarding their liquidity are selected along with
the data for the market indices. Since, the cryptocurrencies market has no
standard market index, we computed two indices to illustrate overall market
situation.
The cryptocurrency panel contains the assets listed in Table 2. The
stock panel and foreign-exchange panel are summarized in Tables 3 and 4,
respectively. Individual availability windows differ because the instruments
were listed or became available at different dates. The resulting panels
therefore contain unequal numbers of historical observations per symbol.
All experiments use a rolling input window ofL = 22 trading days and a
20

holding horizon ofH = 5 days. The same input and decision horizons are
used across all three markets so that the switching mechanism is evaluated
under a common experimental protocol rather than being separately tuned
to each market.
Market-level visualizations Figure 2 illustrates the OHLC price histories
of all 30 cryptocurrency symbols. The corresponding visualizations for stocks
and foreign exchange are shown in Figures 3 and 4. These plots are included
to make the cross-market heterogeneity explicit and to document the different
price scales, trend structures, and volatility regimes encountered by the feature
extractor and retrieval mechanism.
(1) ADA
 (2) APT
 (3) ARB
 (4) ATOM
 (5) AVAX
 (6) BCH
(7) BNB
 (8) BTC
 (9) DOGE
 (10) DOT
 (11) EGLD
 (12) ETC
(13) ETH
 (14) FIL
 (15) HBAR
 (16) ICP
 (17) LINK
 (18) LTC
(19) MATIC
 (20) MKR
 (21) NEAR
 (22) RNDR
 (23) SHIB
 (24) SOL
(25) TON
 (26) TRX
 (27) UNI
 (28) VET
 (29) XLM
 (30) XRP
Figure 2: Daily OHLC price histories for the 30 cryptocurrency symbols used
in the experiments.
21

Table 2: Crypto market data summary.
Market Symbol Range Samples
Crypto VET_USD 2018-08-03-2026-05-31 2859
Crypto BCH_USD 2017-11-09-2026-05-31 3126
Crypto ETC_USD 2017-11-09-2026-05-31 3126
Crypto UNI_USD 2019-10-21-2025-04-17 2006
Crypto SHIB_USD 2020-08-01-2026-05-31 2089
Crypto LTC_USD 2014-09-17-2026-05-31 4275
Crypto ICP_USD 2021-05-10-2026-05-31 1848
Crypto ARB_USD 2017-11-09-2026-05-31 3108
Crypto ADA_USD 2017-11-09-2026-05-31 3126
Crypto SOL_USD 2020-04-10-2026-05-31 2243
Crypto FIL_USD 2017-12-13-2026-05-31 3092
Crypto BTC_USD 2014-09-17-2026-05-31 4275
Crypto TON_USD 2020-08-29-2026-05-31 2102
Crypto EGLD_USD 2020-09-04-2026-05-31 2096
Crypto MATIC_USD 2019-04-28-2025-03-24 2158
Crypto DOT_USD 2020-08-20-2026-05-31 2111
Crypto XLM_USD 2017-11-09-2026-05-31 3126
Crypto ETH_USD 2017-11-09-2026-05-31 3126
Crypto RNDR_USD 2020-06-11-2024-07-21 1502
Crypto MKR_USD 2017-11-20-2026-05-31 3115
Crypto HBAR_USD 2019-09-17-2026-05-31 2449
Crypto AVAX_USD 2020-07-13-2026-05-31 2080
Crypto ATOM_USD 2019-03-14-2026-05-31 2636
Crypto DOGE_USD 2017-11-09-2026-05-31 3126
Crypto LINK_USD 2017-11-09-2026-05-31 3126
Crypto TRX_USD 2017-11-09-2026-05-31 3126
Crypto NEAR_USD 2020-10-14-2026-05-31 2056
Crypto APT_USD 2021-11-20-2025-06-24 1311
Crypto XRP_USD 2017-11-09-2026-05-31 3126
Crypto BNB_USD 2017-11-09-2026-05-31 3126
22

Table 3: Stock market data summary.
Market Symbol Range Samples
Stock TMO 2000-01-03-2026-05-29 6641
Stock MCD 2000-01-03-2026-05-29 6641
Stock NVDA 2000-01-03-2026-05-29 6641
Stock DIS 2000-01-03-2026-05-29 6641
Stock TSLA 2010-06-29-2026-05-29 4004
Stock CVX 2000-01-03-2026-05-29 6641
Stock XOM 2000-01-03-2026-05-29 6641
Stock ACN 2001-07-19-2026-05-29 6252
Stock V 2008-03-19-2026-05-29 4578
Stock WMT 2000-01-03-2026-05-29 6641
Stock KO 2000-01-03-2026-05-29 6641
Stock LIN 2000-01-03-2026-05-29 6641
Stock HD 2000-01-03-2026-05-29 6641
Stock GOOGL 2004-08-19-2026-05-29 5479
Stock CRM 2004-06-23-2026-05-29 5519
Stock UNH 2000-01-03-2026-05-29 6641
Stock BAC 2000-01-03-2026-05-29 6641
Stock COST 2000-01-03-2026-05-29 6641
Stock MA 2006-05-25-2026-05-29 5034
Stock PG 2000-01-03-2026-05-29 6641
Stock AAPL 2000-01-03-2026-05-29 6641
Stock JPM 2000-01-03-2026-05-29 6641
Stock JNJ 2000-01-03-2026-05-29 6641
Stock MSFT 2000-01-03-2026-05-29 6641
Stock MRK 2000-01-03-2026-05-29 6641
Stock META 2012-05-18-2026-05-29 3527
Stock AMZN 2000-01-03-2026-05-29 6641
Stock ABBV 2013-01-02-2026-05-29 3372
Stock BRK-B 2000-01-03-2026-05-29 6641
Stock PEP 2000-01-03-2026-05-29 6641
23

Table 4: Foreign-exchange market data summary.
Market Symbol Range Samples
Forex USDCAD 2003-09-17-2026-05-29 5904
Forex EURAUD 2003-12-01-2026-05-29 5853
Forex EURCHF 2003-01-23-2026-05-29 6059
Forex GBPCHF 2003-10-01-2026-05-29 5894
Forex CHFJPY 2003-12-01-2026-05-29 5854
Forex NZDCHF 2003-12-01-2026-05-29 5825
Forex AUDCAD 2003-12-01-2026-05-29 5856
Forex NZDCAD 2003-12-01-2026-05-29 5852
Forex GBPUSD 2003-12-01-2026-05-29 5848
Forex AUDUSD 2006-05-16-2026-05-29 5212
Forex GBPAUD 2003-06-03-2026-05-29 5982
Forex USDJPY 2000-01-03-2026-05-29 6856
Forex GBPJPY 2003-12-01-2026-05-29 5852
Forex NZDJPY 2003-12-01-2026-05-29 5852
Forex AUDNZD 2003-12-01-2026-05-29 5855
Forex EURGBP 2000-01-03-2026-05-29 6876
Forex USDCHF 2003-09-17-2026-05-29 5902
Forex EURCAD 2003-12-01-2026-05-29 5839
Forex AUDJPY 2003-12-01-2026-05-29 5855
Forex GBPCAD 2003-12-01-2026-05-29 5853
Forex USDTRY 2005-01-03-2026-05-29 5565
Forex AUDCHF 2003-12-01-2026-05-29 5827
Forex EURTRY 2005-01-03-2026-05-29 5567
Forex EURSEK 2000-01-03-2026-05-29 6853
Forex GBPNZD 2003-06-03-2026-05-29 5981
Forex EURUSD 2003-12-01-2026-05-29 5836
Forex NZDUSD 2003-12-01-2026-05-29 5837
Forex EURJPY 2003-01-23-2026-05-29 6061
Forex EURNZD 2003-12-01-2026-05-29 5853
Forex CADJPY 2004-08-20-2026-05-29 5665
24

(1) TMO
 (2) MCD
 (3) NVDA
 (4) DIS
 (5) TSLA
 (6) CVX
(7) XOM
 (8) ACN
 (9) V
 (10) WMT
 (11) KO
 (12) LIN
(13) HD
 (14) GOOGL
 (15) CRM
 (16) UNH
 (17) BAC
 (18) COST
(19) MA
 (20) PG
 (21) AAPL
 (22) JPM
 (23) JNJ
 (24) MSFT
(25) MRK
 (26) META
 (27) AMZN
 (28) ABBV
 (29) BRK-B
 (30) PEP
Figure 3: Daily OHLC price histories for the 30 stock symbols used in the
experiments.
Market indices To provide a market-level reference, we report the mar-
ket index series associated with each experiment in Figure 5 and Figure 6.
Because the cryptocurrency market has no single standard benchmark, the
cryptocurrency panel uses the two synthetic indices defined in the experi-
mental protocol: an equal-weighted (unweighted) cumulative-return index
and a volume-weighted cumulative-return index. As shown in Figure 5, the
volume-weighted index grows gradually from 2020 onward and traces the
characteristic cycle of the market, with a 2021 bull run, a 2022 drawdown,
and a strong 2024–2025 rally followed by a partial reversal. The unweighted
index instead remains close to its initial level until late 2024, after which it
25

(1) USD-
CAD
(2) EU-
RAUD
 (3) EURCHF
(4)
GBPCHF
 (5) CHFJPY
(6) NZDCHF
(7) AUD-
CAD
(8) NZD-
CAD
 (9) GBPUSD
(10)
AUDUSD
(11) GB-
PAUD
(12) USD-
JPY
(13)
GBPJPY
(14) NZD-
JPY
(15)
AUDNZD
(16) EU-
RGBP
(17) USD-
CHF
(18) EUR-
CAD
(19) AUD-
JPY
(20) GBP-
CAD
(21) US-
DTRY
(22) AUD-
CHF
(23) EU-
RTRY
(24)
EURSEK
(25)
GBPNZD
(26) EU-
RUSD
(27) NZ-
DUSD
(28) EUR-
JPY
(29) EU-
RNZD
(30) CAD-
JPY
Figure 4: Daily OHLC price histories for the 30 foreign-exchange symbols
used in the experiments.
26

exhibits an extreme surge and a subsequent sharp correction, indicating that
equal-weighted aggregation over raw prices is dominated by a small number of
extreme constituents and motivating the use of the volume-weighted variant
as the primary market-level descriptor. For the stock-market experiments,
we report three broad United States equity references, namely the S&P 500,
the NASDAQ Composite, and the Dow Jones Industrial Average. All three
indices trend upward over 2016–2026 and share the same major episodes,
including the March 2020 pandemic crash, the 2022 bear market, and the
post-2023 recovery, while the technology-heavy NASDAQ Composite displays
the largest swing amplitude. No comparable composite series is reported
for foreign exchange, as no standard broad-market index exists for the set
of currency pairs under study; market-wide conditions in that market are
instead captured by the aggregate feature stream of the state encoder.
(1) Equal-weighted (unweighted) index.
 (2) Volume-weighted index.
Figure 5: Market-level cryptocurrency indices.
Expert pool We construct a pool of five heterogeneous experts. The
purpose of the pool is to expose the switching mechanism to strategies with
different inductive biases rather than to create a collection of near-identical
predictors. The pool contains policy-gradient, actor-critic, distributional,
and off-policy reinforcement-learning strategies, providing complementary
behaviors for the adaptive selector.
1. A2C (Advantage Actor-Critic).A synchronous actor-critic policy-
gradient method that provides a relatively simple policy-learning base-
line.
27

(1) S&P 500.
 (2) NASDAQ Composite.
 (3) Dow Jones Average.
Figure 6: Market-level United States equity reference indices for the stock-
market experiments.
2. DDPG (Deep Deterministic Policy Gradient). An off-policy
actor-critic method designed for continuous action spaces.
3. PPO (Proximal Policy Optimization).A policy-gradient method
that constrains policy updates to improve training stability.
4. TQC (Truncated Quantile Critics).A distributional reinforcement-
learning method that models the reward distribution through quantile
critics and provides a risk-sensitive candidate policy.
5. CrossQ. An off-policy reinforcement-learning expert included to in-
crease behavioral diversity within the candidate pool.
Metrics We report cumulative return, annualized return, annualized volatil-
ity, Sharpe ratio, Sortino ratio, and maximum drawdown (MDD). Sharpe ratio
measures return relative to total variability, whereas Sortino ratio focuses on
downside variability and is therefore particularly informative when downside
risk is of primary interest. MDD measures the largest peak-to-trough decline
and is used to assess robustness under adverse market regimes. Because the
three markets exhibit different statistical properties and volatility scales, the
discussion emphasizes risk-adjusted measures together with cumulative return
rather than interpreting any single metric in isolation.
Implementation details The retrieval mechanism usesK = 3 nearest
neighbors based on cosine similarity between VAE embeddings of dimension
d = 64. The LLM component uses the model specified in the corresponding
LLM-sensitivity experiment, with temperature 0.1 and at most one LLM
28

call per decision step. The retrieval database is constructed chronologically:
for each training timestampt, the embeddingzt, realized returnRt, and a
summary of the subsequentH = 5 days are stored. At test time, retrieval is
restricted to observationsτ < t, preventing future information from entering
the decision process. All experiments are run on a single NVIDIA H100 GPU.
4.2 Baseline Expert Performance
We first evaluate the standalone experts independently in each market. This
experiment establishes whether the adaptive selector is operating in an en-
vironment with genuinely heterogeneous expert behavior. A useful expert
pool should contain strategies whose relative strengths vary across market
regimes; otherwise, switching has little opportunity to improve over the
globally strongest fixed strategy. In addition, this experiment validates our
assumption that each expert in the pool is dominant in a sub-domain of the
problem over the other experts.
Table 5 shows clear differences in expert behavior across the three markets.
In cryptocurrency, TQC achieves the highest cumulative return (76.16%),
while DDPG obtains the highest Sharpe (1.74) and Sortino (2.73); A2C has
the smallest MDD (−25%) and the highest dominance frequency (34.5%). In
the stock market, CrossQ achieves the highest cumulative return (38.21%)
and the highest dominance frequency (36.4%), whereas PPO provides the
highest Sharpe (0.96), Sortino (1.46), and the smallest MDD (−22%). In
foreign exchange, A2C achieves the highest cumulative return (4.27%), PPO
ties for the highest Sharpe and Sortino (0.88 and 1.20), and PPO has the
smallest MDD (−2.00%), while TQC is dominant most frequently (48.9%).
Thus, no single expert simultaneously provides the strongest return, risk-
adjusted performance, drawdown, and dominance frequency across all markets.
Figure 7 further illustrates this market-dependent dominance pattern and
supports the use of an adaptive selection mechanism.
4.3 Similarity-Driven Expert Selection
The central empirical claim is that selecting experts using historical similarity
can outperform both static expert selection and selection based only on recent
realized performance. We compare four strategies:
1. Best Fixed Expert: the best-performing single expert is selected and
29

A2C TQC CrossQ DDPG PPO
0
10
20
30
40
34.5 32.7
16.4
10.9
5.5
Dominance Frequency
(1) Experts dominance in Crypto mar-
ket.
A2C TQC CrossQ DDPG PPO
0
20
40
60
6.8
48.9
20.5
13.6 10.2
Dominance Frequency
(2) Experts dominance in Forex mar-
ket.
A2C TQC CrossQ DDPG PPO
0
10
20
30
40
19.3
14.8
36.4
5.7
23.9
Dominance Frequency
(3) Experts dominance in the stock mar-
ket.
Figure 7: Illustrative expert-selection frequencies for the proposed switcher
in the three markets.
30

Table 5: Standalone performance of the five expert models in each market.
Market Expert Cum. Return Sharpe Sortino MDD Weeks Dominant
Crypto A2C 63.00 % 1.61 2.44 -25 % 19 (34.5%)
Crypto DDPG 71.26 % 1.74 2.73 -26 % 06 (10.9%)
Crypto PPO 60.49 % 1.57 2.38 -27 % 03 (05.5%)
Crypto CrossQ 53.66 % 1.44 2.24 -28 % 09 (16.4%)
Crypto TQC 76.16 % 1.71 2.63 -29 % 18 (32.7%)
Stock A2C 32.16 % 0.90 1.35 -23 % 17 (19.3%)
Stock DDPG 28.89 % 0.85 1.26 -24 % 05 (05.7%)
Stock PPO 33.38 % 0.96 1.46 -22 % 21 (23.9%)
Stock CrossQ 38.21 % 0.95 1.42 -27 % 32 (36.4%)
Stock TQC 32.09 % 0.86 1.28 -26 % 13 (14.8%)
Forex A2C 4.27 % 0.88 1.20 -2.18 % 06 (06.8%)
Forex DDPG 1.80 % 0.36 0.46 -2.85 % 12 (13.6%)
Forex PPO 4.07 % 0.88 1.20 -2.00 % 09 (10.2%)
Forex CrossQ 2.62 % 0.53 0.69 -2.68 % 18 (20.5%)
Forex TQC 2.26 % 0.48 0.60 -2.18 % 43 (48.9%)
retained throughout the evaluation.
2. Recent-Performance Gating: the expert with the strongest recent
performance over a rolling five-day window is selected.
3. Proposed RAG: the proposed retrieval-based expert-selection frame-
work.
Table 6: Effect of expert-selection strategy in each market.
Market Method Cum. Return Ann. Return Ann. Vol. Sharpe Sortino MDD
Crypto Best Fixed 68 % 62 % 0.32 1.64 2.54 -27 %
Crypto Recent Gating 69 % 62 % 0.32 1.66 2.57 -27 %
Crypto Proposed RAG 71 % 64 % 0.31 1.73 2.72 -26 %
Stock Best Fixed 26 % 14 % 0.21 0.74 1.11 -26 %
Stock Recent Gating 33 % 17 % 0.20 0.91 1.37 -24 %
Stock Proposed RAG 34 % 18 % 0.19 0.96 1.45 -26 %
Forex Best Fixed 3.2 % 1.8 % 0.026 0.71 0.92 - 1.9 %
Forex Recent Gating -0.4 % -0.2 % 0.029 -0.062 -0.08 - 2.6 %
Forex Proposed RAG 4.3 % 2.4 % 0.028 0.88 1.20 -2.2 %
Across all three markets, the proposed selector improves the risk-return
profile relative to the two reference selection strategies. In cryptocurrency,
the proposed method increases cumulative return from 68% for the best fixed
31

expert to 71%, while Sharpe improves from 1.64 to 1.73 and MDD improves
from −27% to −26%. In the stock market, cumulative return increases from
26% to 34%, annualized return from 14% to 18%, and Sharpe from 0.74
to 0.96, while annualized volatility decreases from 0.21 to 0.19. In foreign
exchange, the proposed method achieves 4.3% cumulative return and a Sharpe
ratio of 0.88, compared with 3.2% and 0.71 for the best fixed expert and
−0.4% and −0.062 for recent-performance gating. These results show that
the advantage of retrieval-based selection is not confined to one market class.
The comparison with recent-performance gating is particularly informa-
tive. Recent realized performance is a local criterion and can therefore react
strongly to transient noise. In contrast, retrieval provides historical context
by identifying previous states with similar latent representations. The ex-
pected advantage is consequently largest when the current regime resembles
a previously observed regime in which different experts exhibited different
conditional strengths.
4.4 Ablation: Number of Expert Models
We next investigate whether the benefit of the proposed switcher is merely
a consequence of having access to more candidate models. Nested pools are
constructed by progressively increasing the number of experts. For each pool,
the proposed switcher is compared with the best fixed expert available within
the same pool.
To keep the comparison compact, Table 7 reports Sharpe improvements
and the corresponding fixed-expert Sortino values rather than reproducing
the complete set of portfolio metrics.
With one expert, switching is necessarily identical to fixed selection, pro-
viding an important sanity check. The reported Sharpe improvement remains
small when moving from one to two experts, but increases substantially for
three- and four-expert pools. The four-expert pool produces the largest
reported improvement in every market: 19.8% in cryptocurrency, 22.0% in
stocks, and 27.5% in foreign exchange. Thus, the relevant design variable is
not the number of models alone but the amount of complementary expertise
represented in the pool.
32

Table 7: Effect of expert-pool size on the proposed switcher. Fixed Sharpe
values are consistent with the reported RAG Sharpe values and percentage
improvements.
Market # Experts Fixed Sharpe RAG Sharpe ∆ Sharpe (%) Fixed Sortino
Crypto 1 0.81 0.81 0.0 1.11
Crypto 2 0.84 0.85 1.2 1.16
Crypto 3 0.89 0.98 10.1 1.22
Crypto 4 0.96 1.15 19.8 1.34
Stock 1 0.43 0.43 0.0 0.58
Stock 2 0.51 0.52 2.0 0.68
Stock 3 0.55 0.63 14.5 0.73
Stock 4 0.59 0.72 22.0 0.79
Forex 1 0.35 0.35 0.0 0.49
Forex 2 0.43 0.44 2.3 0.59
Forex 3 0.46 0.55 19.6 0.63
Forex 4 0.51 0.65 27.5 0.70
4.5 Component Ablation
We next isolate the contributions of retrieval, LLM reasoning, and uncertainty-
aware decision making. The ablation is performed independently in each
market using the same expert pool and evaluation protocol.
Table 8: Component ablation across the three markets.
Market Configuration Cum. Return Sharpe MDD
Crypto NR (No Retrieval) +64.8% 1.622 -26.7%
Crypto R −LLM (No LLM) +69.1% 1.661 -27.1%
Crypto F ull (R+L+U) 71 % 1.73 -26 %
Stock NR (No Retrieval) +33.1% 0.911 -24.4%
Stock R −LLM (No LLM) +25.5% 0.735 -26.5%
Stock F ull (R+L+U) 34 % 0.96 -26 %
Forex NR (No Retrieval) +3.2% 0.710 -1.9%
Forex R −LLM (No LLM) -0.2% -0.025 -2.4%
Forex F ull (R+L+U) 4.3 % 0.88 -2.2 %
The component ablation shows that both retrieval and LLM-based reason-
ing contribute to the final performance, although their relative importance
differs across markets. In cryptocurrency, removing retrieval reduces cu-
mulative return from 71% to 64.8% and Sharpe from 1.73 to 1.622, while
removing the LLM reduces them to 69.1% and 1.661, respectively. In the
stock market, the no-retrieval configuration remains relatively close to the
33

full model (33.1% versus 34% cumulative return), whereas removing the LLM
causes a substantially larger reduction to 25.5% and lowers Sharpe from 0.96
to 0.735. In foreign exchange, retrieval is again important, with cumulative
return decreasing from 4.3% to 3.2% without retrieval; the largest degradation
occurs when the LLM is removed, producing a negative cumulative return
of −0.2% and a negative Sharpe ratio of−0.025. The MDD results also
show that the full configuration does not uniformly minimize drawdown in
every market: the no-retrieval variant has a smaller MDD in stocks and
foreign exchange, whereas the full configuration has the smallest MDD in
cryptocurrency.
Importantly, the reported ablation contains no configuration that removes
only the uncertainty component. Therefore, the present results support
conclusions about retrieval and LLM reasoning, but they do not provide an
isolated empirical estimate of the contribution of uncertainty-aware decision
making. As with the other experiments, comparisons should be made within
each market because the markets have different return distributions and
volatility scales.
4.6 LLM Sensitivity: Model Used for Indexing
The retrieval database contains structured historical information that must be
indexed into a representation usable by the retrieval and reasoning pipeline.
We therefore evaluate the sensitivity of the framework to the LLM used during
indexing while keeping the inference-time LLM fixed. Specifically, we compare
three candidate indexing models: Google/Gemma4-E4B, Google/Gemma4-
31B-it, and AliBaba/Qwen3.6-27B-it.
The indexing experiment isolates the effect of the representation supplied
to the retrieval stage. Differences between indexing models can arise from
their ability to preserve financially relevant information when constructing
historical summaries or metadata. To quantify this, we measure each model’s
success rate in following the indexing instructions and producing the expected
output format. Gemma4-E4B achieved this for only 28% of cases, Gemma4-
31B-it for 96%, while Qwen3.6-27B-it succeeded in all instances. Table 9
summarises the success and failure proportions for each model, highlighting
the marked performance disparity across the three candidates. A relatively
stable ranking across markets would indicate that the framework is robust to
the choice of indexing model, whereas large differences, such as the pronounced
gap observed here, would indicate that corpus construction is itself a critical
34

component of the system.
Table 9: Success and failure rates for each indexing LLM.
Model Success Failure
Google/Gemma4-E4B 28% 72%
Google/Gemma4-31B-it 96% 4%
AliBaba/Qwen3.6-27B-it 100% 0%
4.7 LLM Sensitivity: Model Used for Inference
We further investigate the sensitivity of the proposed framework to the LLM
responsible for processing the retrieved historical evidence and producing
the inference-time decision. Unlike the indexing experiment, which examines
how the choice of LLM affects the construction of the historical retrieval
corpus, this experiment focuses on the reasoning stage after retrieval. The
indexed corpus and T-VAE representation are kept unchanged across all
configurations, while only the inference LLM is varied. This setup allows
us to determine whether the effectiveness of the proposed expert-selection
mechanism is preserved when the reasoning capability of the downstream
LLM changes.
Table 10: Sensitivity to the LLM used for inference.
Market Inference LLM Cum. Return Ann. Return Ann. Vol. Sharpe Sortino MDD
Crypto Google/Gemma4-31B-it 68.3 % 61.7 % 0.32 1.65 2.55 -27 %
Crypto Google/Gemma4-E4B 63.5 % 57.4 % 0.32 1.57 2.42 - 28 %
Crypto AliBaba/Qwen3.6-27B-it 71 % 64 % 0.31 1.73 2.72 -26 %
Stock Google/Gemma4-31B-it 25.1 % 13.7 % 0.21 0.73 1.09 -26.5 %
Stock Google/Gemma4-E4B 24.5 % 13.5 % 0.21 0.71 1.06 -27 %
Stock AliBaba/Qwen3.6-27B-it 34 % 18 % 0.19 0.96 1.45 -26 %
Forex Google/Gemma4-31B-it -0.3 % -0.2 % 0.03 -0.05 -0.06 -2.5 %
Forex Google/Gemma4-E4B -5.4 % -3.1 % 0.03 -1.07 -1.37 -5.6 %
Forex AliBaba/Qwen3.6-27B-it 4.3 % 2.4 % 0.028 0.88 1.20 -2.2 %
The inference sensitivity experiment shows a stable ranking across all three
markets. Google/Gemma4-E4Bproducestheweakestresults, Google/Gemma4-
31B-it provides an intermediate level of performance, and AliBaba/Qwen3.6-
27B-it achieves the strongest results. The advantage of Qwen3.6-27B-it is
35

particularly pronounced in foreign exchange, where it changes cumulative
return from −5.4% with Gemma4-E4B and−0.3% with Gemma4-31B-it to
4.3%, while Sharpe increases from −1.07 and −0.05 to 0.88. Similar but
smaller improvements are observed in cryptocurrency and the stock market.
These results indicate that the quality of inference-time reasoning materially
affects how the retrieved evidence is converted into an expert-selection deci-
sion. They also show that the retrieval mechanism alone does not guarantee
robust performance: the downstream reasoning model remains an important
component of the complete framework.
4.8 Comparison with State-of-the-Art Methods
Finally, we compare the proposed framework with representative state-
of-the-art portfolio-management, adaptive-trading, and LLM-based finan-
cial decision-making methods. The comparison is performed separately in
cryptocurrency, stocks, and foreign exchange using the same data splits,
transaction-cost assumptions, portfolio constraints, and evaluation horizon
wherever the competing implementations permit a controlled comparison.
The state-of-the-art models the proposed model compared with are:
1. AlphaMixRL [Sun, 2024]. A hierarchical reinforcement-learning
approach that combines ensemble learning with adaptive expert routing
for portfolio management.
2. TAC (Trend-Aware Controller) [Asadi and Safabakhsh, 2025].
A strategy that formulates portfolio management as dynamic expert se-
lection using Transformer-VAE representations and trend-aware decision
making.
3. LLM-MAS [Luo et al., 2025].A large-language-model-based multi-
agent system for cryptocurrency portfolio management. The framework
employs multiple specialized LLM agents and hierarchical skill configu-
rations to analyze market information and generate portfolio decisions,
providing an LLM-driven alternative to conventional reinforcement-
learning portfolio managers.
4. Multi-LLMBlack–Litterman[MantshimuliandMutebaMwamba,
2025]. A portfolio-optimization framework that aggregates investment
views generated by multiple LLMs from financial sentiment information
36

and incorporates them into the classical Black–Litterman model. The
approach is evaluated on an S&P 500 equity portfolio and represents
an LLM-enhanced probabilistic portfolio-allocation strategy.
5. Fine-tuned LLaMA [Ballinari and Maly, 2025].A fine-tuned
LLaMA-based approach for foreign-exchange trading that adapts a
pretrained LLM to financial-news sentiment analysis and uses the re-
sulting signals for trading decisions. The method investigates whether
domain-specific fine-tuning improves the effectiveness of LLM-generated
sentiment signals for FX portfolio management.
Table 11 shows that the proposed framework achieves the strongest overall
risk-adjusted performance among the compared methods in each of the three
markets. In cryptocurrency, the proposed method obtains the highest cu-
mulative return (71%) and annualized return (64%), substantially exceeding
LLM-MAS (33% and 30%), TAC (24% and 21.6%), and AlphaMixRL (22%
and 19.8%). It also achieves the highest Sharpe ratio (1.73), while its annu-
alized volatility (0.31) and MDD (−26%) are both substantially lower than
those of the competing methods. Thus, the return advantage is accompanied
by a materially improved risk profile.
The stock-market comparison leads to the same conclusion. The proposed
framework achieves 34% cumulative return and 18% annualized return, com-
pared with 10.4% and 5.6% for TAC, 11.8% and 6.3% for AlphaMixRL, and
31% and 16.4% for Multi-LLM Black–Litterman. The proposed method also
records the highest Sharpe ratio (0.96), the lowest annualized volatility (0.19),
and the smallest MDD (−26%) among the reported methods. The result is
therefore not explained solely by higher raw return; the proposed framework
also provides a stronger risk-adjusted profile under the evaluated setting.
In foreign exchange, the absolute return levels are lower, but the ranking
remains favorable. The proposed method achieves 4.3% cumulative return
and 2.4% annualized return, compared with 3.3% and 1.9% for the fine-
tuned LLaMA approach, 0.8% and 0.45% for AlphaMixRL, and 0.7% and
0.4% for TAC. It also obtains the highest Sharpe ratio (0.88), the lowest
annualized volatility (0.03), and the smallest MDD (−2.2%). Overall, the
SOTA comparison indicates that the proposed framework generalizes its
advantage across cryptocurrency, stocks, and foreign exchange rather than
relying on a single favorable market.
37

Table 11: Comparison with representative state-of-the-art methods in each
market.
Market Method Cum. Return Ann. Return Ann. Vol. Sharpe MDD
Crypto TAC [Asadi and Safabakhsh, 2025] 24 % 21.6 % 0.94 1.29 -31 %
Crypto AlphaMixRL [Sun, 2024] 22 % 19.8 % 1.00 1.38 -29 %
Crypto LLM-MAS [Luo et al., 2025] 33 % 30 % 0.96 1.50 -28 %
Crypto Proposed 71 % 64 % 0.31 1.73 -26 %
Stock TAC [Asadi and Safabakhsh, 2025] 10.4 % 5.6 % 0.25 0.74 -28 %
Stock AlphaMixRL [Sun, 2024] 11.8 % 6.3 % 0.31 0.82 -27 %
Stock Multi-LLM [Mantshimuli and Muteba Mwamba, 2025] 31 % 16.4 % 0.28 0.91 -29 %
Stock Proposed 34 % 18 % 0.19 0.96 -26 %
Forex TAC [Asadi and Safabakhsh, 2025] 0.7 % 0.4 % 0.45 0.61 -5.1 %
Forex AlphaMixRL [Sun, 2024] 0.8 % 0.45 % 0.50 0.68 -4.6 %
Forex Fine-tuned LLaMA [Ballinari and Maly, 2025] 3.3 % 1.9 % 0.08 0.76 -3.1 %
Forex Proposed 4.3 % 2.4 % 0.03 0.88 -2.2 %
5 Conclusion
The experiments demonstrate that no single expert consistently dominates
across all markets and evaluation metrics, supporting the need for adaptive
expert selection. The proposed RAG-based selector achieves the strongest
overall performance, obtaining the highest cumulative return and Sharpe
ratio across cryptocurrency, the stock market, and foreign exchange, with
particularly notable improvements in the stock and foreign-exchange markets.
The expert-pool experiments further show that performance improves as com-
plementary experts are introduced, highlighting the importance of diversity
within the candidate pool. The ablation results confirm that both retrieval
and LLM reasoning contribute substantially to the framework’s effectiveness,
while the current experiments do not isolate the independent contribution of
uncertainty-aware decision making.
The LLM sensitivity experiments indicate that both indexing quality and
inference capability affect the overall pipeline, with Qwen3.6-27B-it providing
the strongest portfolio results. The SOTA comparison further suggests that
the proposed framework achieves strong risk-adjusted performance across all
three markets, particularly in terms of Sharpe ratio and annualized volatility.
Nevertheless, these findings should be interpreted with appropriate caution
because each market was evaluated using a single experimental run, and
the competing methods were not always implemented under identical ex-
perimental protocols. Future work should therefore evaluate the framework
38

across multiple random seeds, market periods, transaction-cost scenarios, and
statistically tested repeated experiments.
References
Mahshad Alidousti, Morteza Khakzar Bafruei, and Amir Hosein Afshar Sedigh.
A novel data-efficient double deep q-network framework for intelligent
financial portfolio management. Engineering Applications of Artificial
Intelligence, 162:112436, 2025.
Ahmad Asadi and Reza Safabakhsh. Transformer-based actor-critic for
adaptive cryptocurrency portfolio rebalancing.Applied Soft Computing,
185:113697, 2025.
Turan G. Bali and Florian Weigert. Hedge funds and the positive idiosyncratic
volatility effect.Review of Finance, 28(5):1611–1661, 2024.
Daniele Ballinari and Jessica Maly. Fx sentiment analysis with large language
models. Swiss National Bank Working Paper, 11:1–41, 2025.
Ulas Cakmak and Süleyman Özekici. Portfolio optimization in stochastic
markets. Mathematical Methods of Operations Research, 63(1):151–168,
2006.
Atefe Charkhestani and Akbar Esfahanipour. Behaviorally informed deep
reinforcement learning for portfolio optimization with loss aversion and
overconfidence: A. charkhestani, a. esfahanipour.Scientific Reports, 16(1):
6443, 2026.
Yanxu Chen, Zijun Yao, Yantao Liu, Jin Ye, Jianing Yu, Lei Hou, and
Juanzi Li. Stockbench: Can llm agents trade stocks profitably in real-world
markets? arXiv preprint arXiv:2510.02209, 2025.
Himanshu Choudhary, Arishi Orra, Kartik Sahoo, and Manoj Thakur. Risk-
adjusted deep reinforcement learning for portfolio optimization: A multi-
reward approach. International Journal of Computational Intelligence
Systems, 18:126, 2025.
Dave Cliff and Michael Rollins. Methods matter: A trading agent with
no intelligence routinely outperforms ai-based traders. In 2020 IEEE
39

Symposium Series on Computational Intelligence (SSCI), pages 392–399.
IEEE, 2020.
Qianggang Ding, Haochen Shi, Jiadong Guo, and Bang Liu. Tradexpert:
Revolutionizing trading with mixture of expert llms. arXiv preprint
arXiv:2411.00782, 2024.
Ling Feng and Ananta Sinchai. Deep context-attentive transformer transfer
learning for financial forecasting.PeerJ Computer Science, 11:e2983, 2025.
Fengchen Gu, Huijia Wang, Zhengyong Jiang, Angel F García-Fernández,
Jionglong Su, and Huakang Li. Mixture-of-experts liquid financial mamba
framework for portfolio management based on deep reinforcement learning.
In 2025 IEEE International Conference on Big Data (BigData), pages
5756–5764. IEEE, 2025.
Zhendai Huang, Bolin Liao, Cheng Hua, Xinwei Cao, and Shuai Li. Leveraging
chatgpt for enhanced stock selection and portfolio optimization.Neural
Computing and Applications, 37(8):6163–6179, 2025.
Bruce I Jacobs, Kenneth N Levy, and Harry M Markowitz. Portfolio opti-
mization with factors, scenarios, and realistic short positions.Operations
Research, 53(4):586–599, 2005.
Yifu Jiang, Jose Olmo, and Majed Atwi. Deep reinforcement learning for
portfolio selection. Global Finance Journal, 62:101016, 2024.
Zhengyao Jiang and Jinjun Liang. Cryptocurrency portfolio management
with deep reinforcement learning. In2017 Intelligent systems conference
(IntelliSys), pages 905–913. IEEE, 2017.
Yaxuan Kong, Yuqi Nie, Xiaowen Dong, John M Mulvey, H Vincent Poor,
Qingsong Wen, and Stefan Zohren. Large language models for financial
and investment management: Applications and benchmarks.Journal of
Portfolio Management, 51(2), 2024.
Kuan-Ming Liu and Ming-Chih Lo. Llm-based routing in mixture of experts:
A novel framework for trading.arXiv preprint arXiv:2501.09636, 2025.
Wei Liu and Ian Garrett. Regime-dependent effects of macroeconomic uncer-
tainty on realized volatility in the us stock market.Economic Modelling,
128:106483, 2023.
40

Yuchen Liu, Daniil Mikriukov, Owen C. Tjahyadi, Gangmin Li, Terry R.
Payne, Yong Yue, Kamran Siddique, and Ka Lok Man. Revolutionising
financial portfolio management: The non-stationary transformer’s fusion of
macroeconomic indicators and sentiment analysis in a deep reinforcement
learning framework. Applied Sciences, 14(1):274, 2024.
Yichen Luo, Yebo Feng, Jiahua Xu, Paolo Tasca, and Yang Liu. Llm-powered
multi-agent system for automated crypto portfolio management.arXiv
preprint arXiv:2501.00826, 2025.
Lamu Mantshimuli and John Weirstrass Muteba Mwamba. Enhancing port-
folio optimization with multi-llm sentiment aggregation: A black-litterman
integration approach.Available at SSRN 5394743, 2025.
Saeed Masoudnia and Reza Ebrahimpour. Mixture of experts: a literature
survey. Artificial Intelligence Review, 42(2):275–293, 2014.
Minh Duc Nguyen. Advanced investing with deep learning for risk-aligned
portfolio optimization. PLOS ONE, 20(8):e0330547, 2025.
Alin-Bogdan Popa, Iulia Maria Florea, and Răzvan Rughiniş. Convolutional
neural network portfolio management system with heterogeneous input. In
2020 19th RoEduNet Conference: Networking in Education and Research
(RoEduNet), pages 1–4. IEEE, 2020.
Xiaotian Ren, Ruoyu Sun, Zhengyong Jiang, Angelos Stefanidis, Hongbin
Liu, and Jionglong Su. Time series is not enough: Financial transformer
reinforcement learning for portfolio management.Neurocomputing, 647:
130451, 2025.
Mohadese Rezaei and Hossein Nezamabadi-Pour. A taxonomy of literature
reviews and experimental study of deepreinforcement learning in portfolio
management. Artificial Intelligence Review, 58(3):94, 2025.
Meeta Sharma and Hardayal Singh Shekhawat. Portfolio optimization and
return prediction by integrating modified deep belief network and recurrent
neural network.Knowledge-Based Systems, 250:109024, 2022.
William F. Sharpe. Insights from a pioneer in portfolio theory and practice:
A talk with nobel laureate william f. sharpe, phd.Journal of Investment
Consulting, 7(2):10–20, 2005.
41

Frank A Sortino and Lee N Price. Performance measurement in a downside
risk framework. the Journal of Investing, 3(3):59–64, 1994.
Shuo Sun. Reinforcement Learning for Financial Trading: Algorithms, Eval-
uations and Platforms. Phd thesis, Nanyang Technological University,
2024.
Yinuo Sun, Zhaoen Qu, Tingwei Zhang, and Xiangyu Li. Adaptive ensemble
learning for financial time-series forecasting: A hypernetwork-enhanced
reservoir computing framework with multi-scale temporal modeling.Axioms,
14(8):597, 2025.
M Taghian, A Asadi, and R Safabakhsh. A reinforcement learning-based
encoder-decoder framework for learning stock trading rules.Journal of AI
and Data Mining, 11(1):103–118, 2023.
Mehran Taghian, Ahmad Asadi, and Reza Safabakhsh. Learning financial
asset-specific trading rules via deep reinforcement learning.Expert Systems
with Applications, 195:116523, 2022.
Ananya Unnikrishnan. Financial news-driven llm reinforcement learning for
portfolio management. arXiv preprint arXiv:2411.11059, 2024.
Arpita Vats, Rahul Raja, Vinija Jain, and Aman Chadha. The evolution of
moe: A survey from basics to breakthroughs.Journal of IEEE Transactions
on Artificial Intelligence, 2024.
Xinyao Wang and Lili Liu. Risk-sensitive deep reinforcement learning for
portfolio optimization. Journal of Risk and Financial Management, 18(7):
347, 2025.
Ziqiang Wei, Deng Chen, Yanduo Zhang, Dawei Wen, Xin Nie, and Liang Xie.
Deep reinforcement learning portfolio model based on mixture of experts.
Applied Intelligence, 55(5):347, 2025.
Yijia Xiao, Edward Sun, Di Luo, and Wei Wang. Tradingagents: Multi-agents
llm financial trading framework. InThe First MARW: Multi-Agent AI in
the Real World Workshop at AAAI 2025.
Meiqun Yin and Mengzhu Guo. Complex forecasting and investment strategy
optimization via chain-of-thought of large language models.Expert Systems
with Applications, 298:129913, 2026.
42

Yiyao Zhang, Diksha Goel, Hussain Ahmad, and Claudia Szabo. Regimefolio:
A regime aware ml system for sectoral portfolio optimization in dynamic
markets. IEEE Access, 13:184722–184744, 2025.
43
