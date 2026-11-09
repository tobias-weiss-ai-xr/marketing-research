---
title: 'DualCast: A Dual-Path Language Model for Bimodal Financial Time-Series Forecasting'
url: https://arxiv.org/abs/2609.38197
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Wentao Zhao
- Hongqiang Wu
- Shanghang Liu
- Zhaochen Zan
- Yu Zhang
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.38197
pages: 12
chars: 55812
fetched_at: '2026-11-08T13:24:46+00:00'
kb_version: 1
---

# DualCast: A Dual-Path Language Model for Bimodal Financial Time-Series Forecasting

DualCast: A Dual-Path Language Model for Bimodal Financial Time-Series Forecasting
Wentao Zhao‡a,b, Hongqiang Wu‡c,d, Shanghang Liu‡a, Zhaochen Zana, Yu Zhang†c, Biqing Huang†a
aDepartment of Automation, Tsinghua University, Beijing, 100084, China
bSchool of Software, Tsinghua University, Beijing, 100084, China
cSchool of Computer Science, Northwestern Polytechnical University, Xi’an, 710129, China
dInspur Yunzhou Industrial Internet Co. Ltd, Jinan, 250101, China
Abstract
Financial time-series forecasting must capture price dynamics across heterogeneous assets while incorporating news available at
prediction time. We introduce DualCast, a dual-path framework that extends a frozen language model with a discrete financial
vocabulary. Each log-return patch is represented by a learned summary token and three residual shape tokens, preserving local
drift and volatility while allowing shape patterns to be shared across assets. To improve codebook utilization, we develop adaptive
frequency-equalizing residual vector quantization, which rebalances overloaded codewords without compromising reconstruction
accuracy. The fast path trains only the new financial-token embeddings and output heads on a frozen Qwen3-8B backbone. A
toggleable LoRA adapter enables a slow path that conditions on the fast forecast and news available at the forecast origin to
produce a revised prediction. The reviser is initialized by supervised fine-tuning and further optimized with a return-space group
relative policy optimization objective that rewards improvements over the fast forecast. In zero-shot evaluations covering equities
and energy prices at five-minute, daily, and weekly resolutions, the slow path achieves the lowest mean absolute percentage error
among the compared methods in 8 of 12 dataset–horizon settings, including every longest-horizon setting. News ablations indicate
additional gains in most tested settings, although their magnitude varies across markets. DualCast thus combines a fast numerical
forecaster with an optional text-conditioned revision mechanism.
Keywords:time-series forecasting, large language models, financial forecasting, vector quantization, multimodal learning,
reinforcement learning
1. Introduction
Despite recent progress in applying large language models
(LLMs) to time-series forecasting, financial markets remain
particularly challenging. First, financial data are highly hetero-
geneous, exhibit low signal-to-noise ratios, and evolve under
rapidly changing volatility regimes, creating a substantial gap
from conventional forecasting benchmarks and making stable
pattern learning difficult. Second, financial forecasting requires
not only modeling historical price dynamics but also under-
standing and reasoning over external information such as news.
While LLMs excel at language understanding and knowledge
integration, they are not naturally designed for numerical pre-
diction and time-series modeling. Bridging these two require-
ments remains a central challenge for financial foundation mod-
els.
Most modern forecasting models, from patch-based Trans-
formers to large-scale time-series foundation models, are de-
signed for signals that are smooth, strongly periodic, and gov-
erned by relatively stable dynamics, such as electricity load,
traffic, and weather. Financial markets differ fundamentally:
they are noisy, weakly autocorrelated, and characterized by
rapidly changing volatility regimes. Moreover, financial time
1† Corresponding author
2‡ Equal contribution.
series are highly heterogeneous across assets, with volatility
levels often spanning multiple orders of magnitude. As a result,
representations learned under one scale regime frequently fail
to generalize to others, while models trained on high-variance
assets tend to overlook the subtle signals present in lower-
variance markets. Bridging this gap requires a representation
that captures transferable market patterns while remaining ro-
bust to large differences in scale and volatility.
A substantial fraction of price-moving information originates
outside historical price trajectories. Earnings announcements,
policy decisions, macroeconomic releases, and the collective
sentiment reflected in financial news and social media contin-
uously shape market behavior. Consequently, even highly ex-
pressive numerical forecasting models remain structurally blind
to information that has already been disclosed through text.
While recent large language models offer powerful language
understanding and knowledge integration capabilities, they are
not naturally optimized for numerical forecasting. Existing
foundation models therefore tend to specialize in either numer-
ical modeling or language reasoning, but rarely both. Closing
this gap requires a bimodal forecasting framework that jointly
reasons over historical market dynamics and contemporaneous
textual information.
Large language models (LLMs) provide a promising foun-
dation for addressing both challenges simultaneously: they al-
arXiv:2609.38197v1  [cs.LG]  18 Sep 2026

ready encode rich semantic knowledge and reasoning capabil-
ities over text, while their autoregressive architecture offers a
natural framework for sequential prediction. Recent efforts
have adapted LLMs to time-series forecasting through three
main paradigms: reprogramming continuous signals into the
embedding space of a frozen LLM [1, 2, 3], converting nu-
merical values into textual representations and leveraging next-
token prediction directly [4], and quantizing time series into
discrete tokens so that forecasting becomes language model-
ing over an extended vocabulary [5, 6]. For financial fore-
casting, we argue that the quantization paradigm is particularly
appealing. By representing market dynamics as discrete to-
kens, it places price trajectories and textual information within
a unified autoregressive sequence over a shared vocabulary, en-
abling joint modeling of historical prices and external news.
More importantly, quantization transforms forecasting into a
discrete prediction problem, producing verifiable targets that
naturally support reinforcement learning with outcome-based
rewards. Recent studies have shown that such verifiable re-
wards are effective for eliciting deliberate reasoning in forecast-
ing tasks [7, 8]. In contrast, continuous reprogramming does
not naturally provide an explicit discrete target space, while
textual stringification may fragment numerical structure and
incur substantial token overhead. These advantages make the
quantize-and-adapt paradigm a natural foundation for building
a bimodal financial forecasting model that integrates both nu-
merical dynamics and textual reasoning.
Committing to the quantize-and-adapt paradigm turns the
two challenges above into three design requirements. (1) Dis-
cretization must preserve scale information. Financial assets
exhibit volatility levels spanning multiple orders of magnitude,
and naive quantization either lets high-volatility assets domi-
nate the codebook or collapses low-volatility series into near-
degenerate representations. While normalization alleviates this
issue, it also removes scale information that is often predictive.
(2) Acquiring numerical forecasting ability must not come at
the expense of textual reasoning. Fine-tuning an entire LLM
on tokenized time series risks shifting model capacity toward
numerical patterns and degrading the language understanding
needed to interpret news and justify forecast revisions. (3) Fast
forecasting and slow reasoning should coexist within a single
model. Most predictions require only a lightweight history-to-
future mapping, while text-conditioned deliberation is mainly
valuable during regime shifts. A practical financial foundation
model should therefore support both efficient forecasting and
optional reasoning without maintaining separate systems or re-
learning the forecasting process.
We present DualCast, a dual-path framework built on a sim-
ple principle: a finite-capacity backbone should acquire nu-
merical forecasting ability without sacrificing the pretrained
linguistic and reasoning competence it later needs to interpret
news. To preserve scale information across heterogeneous as-
sets, thefast modeemploys a decoupled scale–shape tokenizer
that represents normalized price dynamics and market scale as
separate discrete tokens, enabling robust forecasting across di-
verse volatility regimes. These time-series tokens are intro-
duced through a fully frozen Qwen3-8B backbone [9], with
only the newly added token embeddings trained, thereby pre-
serving the model’s native language capabilities by construc-
tion. To support both efficient forecasting and optional deliber-
ation, theslow modeadds a toggleable adapter [10] on the same
frozen backbone. When enabled, it conditions on news and the
fast-mode prediction to produce a revised forecast together with
a reasoning trace, optimized via reinforcement learning in re-
turn space. Because both modes share the same backbone and
forecasting format, reasoning can be invoked only when addi-
tional context is valuable, while retaining the efficiency of the
fast forecasting path.
Figure 1 summarizes the framework. The scale–shape tok-
enizer converts each return patch into one summary token and
three residual shape tokens. Fast mode learns to forecast this
financial-token sequence with a frozen language-model back-
bone, whereas slow mode activates a lightweight adapter that
conditions on causally available text and the fast forecast to
generate a revised path.
Contributions.
•Scale-aware financial tokenization.We represent each
log-return patch with one token from a learned sum-
mary codebook and three residual shape tokens. Adaptive
frequency-equalizing residual vector quantization (AFE-
RVQ) rebalances assignments within the shape codebooks,
reducing codeword usage imbalance while maintaining re-
construction accuracy.
•Parameter-efficient dual-path adaptation.We extend
a frozen Qwen3-8B backbone with financial tokens and
train their embeddings and output heads for the fast fore-
casting path. A toggleable LoRA adapter enables a slow
revision path on the same backbone. Across the two
training stages, 48.9 million parameters, or 0.60% of the
model, are trainable.
•News-conditioned revision with return-space feedback.
The slow path conditions on the fast forecast and news
available at the forecast origin to produce a revised pre-
diction. We initialize the reviser through supervised fine-
tuning and further optimize it with group relative policy
optimization, using return-space rewards for improvement
over the fast forecast and cross-sectional consistency.
2. Related Work
2.1. LLMs for Time-Series Forecasting
Adapting language models to numerical forecasting has pro-
duced three methodological families.Reprogrammingap-
proaches keep the LLM frozen and learn a thin interface that
projects patched series into the model’s embedding space:
Time-LLM [1] aligns patches with text prototypes, GPT4TS [2]
fine-tunes only the normalization and projection layers of a
frozen GPT-2, and TEST [3] contrasts time-series and text
embeddings to activate the LLM. These methods preserve the
backbone but operate on continuous embeddings, which makes
them incompatible with the discrete, RL-optimizable targets we
2

清华大学 | Tsinghua University
AFE-RVQ
S L0 L1  L2
Hierarchical TS Tokens
Slow Mode
Frozen
Transformer
Backbones
Lora

Q V
GRPO
Text Context
Fast Mode
Hybrid Vocabulary
TS tokens Text tokens
Frozen
Transformer
Backbones
S L0 L1 L2
Fast Forecast
S L0 L1 L2
Fast Forecast
Observed Series
Log-return Representation
ReVIN
Summary Multi-scale Patterns
Reasons:
1. Prices may trend downward...Because...
2. The news show that...
3. I decide to refine...
Figure 1: Overview of DualCast. The scale–shape tokenizer separates scale statistics from residual shape patterns and maps both to a hierarchical financial-token
sequence. Fast mode predicts future financial tokens using the shared frozen backbone. Slow mode activates a LoRA adapter and uses causally available text
together with the fast forecast to produce a news-conditioned revision. The adapter is initialized by supervised fine-tuning and subsequently optimized with the
return-space GRPO objective described in Section 3.
require.Stringificationmethods such as LLMTime [4] ren-
der numbers as digit strings and forecast by next-token sam-
pling; they are simple and training-free but waste sequence
length on digits and fracture numerical semantics.Quantiza-
tionmethods discretize the signal into a finite vocabulary and
train a language model over it. Chronos [5] bins scaled val-
ues into a fixed vocabulary, while TOTEM [6] learns a VQ-
V AE codebook of temporal patterns; both demonstrate that
“time series as language” transfers the mature machinery of se-
quence modelling to forecasting. In parallel, a line of domain-
specific foundation models—TimesFM [11], Moirai [12], MO-
MENT [13], Timer [14], Time-MoE [15], and Sundial [16]—
pretrains Transformers from scratch on large numerical cor-
pora. KTD-Fin[17] finds no persistent positive stock-selection
alpha among the LLM trading agents evaluated under leakage-
controlled conditions. These models are strong unimodal fore-
casters but discard the pretrained text and reasoning priors that
bimodal financial forecasting depends on.
Our tokenizer sits in the quantization family but departs from
it in two ways. First, following the patch-wise consensus of
PatchTST [18] and PITS [19] and per-instance normalization
of RevIN [20], we explicitlyfactoreach patch into a normal-
ized shape and a removed scale, then re-quantize the scale
with a learned codebook rather than discarding it or binning
it coarsely. Second, we adopt residual vector quantization from
neural audio coding [21] with the rotation-trick straight-through
estimator [22] and EMA codebooks [23], and add a frequency-
equalization step so the resulting LLM vocabulary is densely
utilized.
2.2. Text–Time-Series Fusion for Financial Forecasting
Combining textual signals with market data has a long his-
tory. StockNet [24] pairs tweets with prices for movement
prediction and remains a standard benchmark; FinBERT [25]
adapts BERT to financial sentiment; and BloombergGPT [26]
and FinGPT [27] build finance-specialized LLMs, though their
temporal modelling is weak. A second thread designs explicit
fusion architectures—attention gating, cross-attention between
text and price, and contrastive alignment—typified by market-
guided transformers such as MASTER [28]. These systems
generally treat text and series as two encoders fused by a be-
spoke module, and the numerical channel is a regression head
rather than a generative sequence. We instead place price to-
kens and news tokens in asingleautoregressive sequence over
a shared vocabulary, so fusion is performed by the backbone’s
native attention and the model can both read news andgenerate
a refined numerical forecast.
2.3. Reasoning and Reinforcement Learning for Time Series
A recent direction reframes forecasting as explicit reason-
ing rather than a one-shot mapping. “Slow-thinking” stud-
ies [7, 29] show that prompting an LLM to deliberate before
predicting can outperform direct prediction, and surveys doc-
ument a rapid shift toward reasoning- and agent-centric time-
series systems [30]; reinforcement learning over discrete token
outputs has emerged as the standard way to elicit such chain-of-
thought via verifiable rewards [8]. We follow this philosophy—
reasoning iselicited by RL with verifiable rewards[31, 32]
rather than distilled from synthetic traces—but our contribution
is orthogonal to how the reasoning trace itself is produced, and
lies instead inwhereandhow cheaplyreasoning is added. First,
we keep the backbone permanently frozen and adapt only a
compact set of new embeddings, so the model’s native text and
reasoning ability is preserved for the refinement stage instead
of being diluted by domain fine-tuning. Second, reasoning is an
optionalsecond pass: a single toggleable adapter recovers the
fast single-forward forecaster when disabled and a slow, text-
conditioned reasoner when enabled. Third, the refinement se-
quence regenerates the forecast in a numerical context, so the
history-to-target attention learned during pretraining is reused
at refinement time rather than relearned. Together these make
the reasoning path inexpensive to add and inexpensive to skip,
3

which is essential when a fast estimate already suffices and de-
liberation is warranted only at regime shifts.
3. Method
Overview and Problem Setup
Letp 1:C+H ={p 1,...,p C+H}denote a univariate positive
price series, wherep 1:C is the historical context andp C+1:C+H
is the forecasting target. In the multimodal setting, the forecast
origin is also associated with a timestamped text streamT ≤C,
such as news headlines, filings, or social media posts, whose
timestamps are no later than the forecast origin. The task is to
predict the future price path while respecting this no-leakage
constraint.
DualCastdecomposes the task into a fast numerical path and
a slow text-conditioned refinement path. Stage 1 learns a time-
series language: prices are converted into discrete tokens and
a frozen LLM is trained to autoregressively forecast the next
tokens. Stage 2 keeps the same frozen backbone and Stage 1
time-series vocabulary, attaches a small adapter, and asks the
model to revise the Stage 1 forecast using recent text. This de-
sign separates two capabilities that are both needed in financial
forecasting: robust pattern matching over noisy price histories
and language-based reasoning over exogenous events.
3.1. Shape–Scale Tokenization with AFE-RVQ
A local price segment contains two fundamentally different
types of information: its movement pattern and its scale. The
former describes relative temporal dynamics, such as rallies,
reversals, or consolidation behaviors, while the latter reflects
local drift and volatility. Quantizing both factors within a sin-
gle representation space forces the tokenizer to model heteroge-
neous phenomena simultaneously and reduces token efficiency.
We therefore decompose each patch into ashapecomponent
and ascalecomponent, which are discretized separately and
later combined into a unified token stream.
We represent the price trajectory by log-returns rather than
raw prices,
rt =logp t−logp t−1,(1)
which removes dependence on the absolute price level and
makes the representation invariant to multiplicative rescaling.
The return series is partitioned into non-overlapping patches of
lengthL, and each patch is independently normalized using re-
versible instance normalization (RevIN) [20]. The normalized
patch serves as the shape signal, while the removed normaliza-
tion statistics are retained as patch-level scale information.
To bridge continuous financial signals and discrete language
modeling, we convert each normalized patch into a small set
of discrete shape tokens. An encoder first maps the normalized
patch ˜r(w) into a latent representation, which is then discretized
using residual vector quantization (RVQ) [21]. By representing
each patch as a composition of codewords drawn from multiple
codebooks, RVQ provides a compact yet expressive vocabulary
of recurring return patterns. The resulting code indices form
the shape tokens, allowing numerically different but structurally
similar price movements to share a common symbolic represen-
tation.
Because every RVQ codeword becomes one trainable em-
bedding row in the extended LLM vocabulary, its assignment
frequency directly determines how often that row receives a
gradient. Plain RVQ can concentrate a disproportionate fraction
of assignments on a small number of codewords, producing a
peaked financial-token distribution even when most entries are
active. We therefore introduceAdaptive Frequency-Equalizing
RVQ(AFE-RVQ), a periodic rebalancing operator applied in-
dependently at each residual level during tokenizer training.
LetC={c i}K i=1 be one codebook and leth i denote the number
of latent vectors assigned toc i over a poolZof recent batches.
With the uniform expected load ¯h=|Z|/K, AFE-RVQ identi-
fies overloaded and starved entries as
O={i:h i >τ hi¯h},D={i:h i <τ lo¯h}.(2)
For an overloaded entryi, the latent vectors assigned toc i are
split with a smallk-means problem. One sub-center replaces
ci, while the remaining sub-centers are written into available
entries inD. The exponential-moving-average accumulators
of every relocated entry are reset so that it is not pulled back
toward its previous location, and a small anti-symmetric per-
turbation separates sibling sub-centers that would otherwise re-
merge. In our deployed tokenizer, assignment counts are col-
lected fromP=64 recent batches and rebalancing is applied
every 500 steps withτ lo =0.5 andτ hi =2.0. The opera-
tion adds no parameters and is disabled at inference time. As
shown in Section 4.5, it reduces peak codeword load while pre-
serving reconstruction fidelity; we therefore use it to obtain a
better-balanced vocabulary rather than claim additional repre-
sentational capacity.
Since the normalization used to isolate shape patterns re-
moves local drift and volatility, the discarded scale information
is represented separately using a discrete summary token.
The retained statistics (µw,σ w) are discretized using a learned
summary vocabulary constructed from observed (µ w,logσ w)
pairs in the training set. Each summary token corresponds to
a frequently occurring local market regime characterized by a
particular combination of drift and volatility. Unlike manually
designed discretization grids, the learned vocabulary allocates
capacity according to the empirical distribution of market states
and therefore uses tokens more efficiently.
Each patch is ultimately represented by one summary token
Sfollowed by three residual shape tokens,
[S,L 0,L 1,L 2].(3)
Placing the summary token first allows subsequent shape to-
kens to be interpreted under the corresponding local market
regime. The resulting token sequence forms a discrete financial
language that can be modeled directly by a standard autoregres-
sive LLM.
3.2. Fast Mode: Financial Language Modeling
Fast mode treats the tokenized price sequence as a discrete
financial language and trains a frozen LLM to autoregressively
4

model its dynamics. Given a sequence of summary and shape
tokens produced by AFE-RVQ, the model predicts future to-
kens using only historical price information. This mode serves
as the efficient forecasting path of DualCastand provides the
baseline prediction that is later refined by the slow mode.
We extend the Qwen3-8B vocabulary with the financial to-
kens introduced in Section 3.1, including one summary vocab-
ulary and three shape vocabularies. Rather than random ini-
tialization, the newly added embeddings inherit the geometry
of the learned tokenizers, preserving similarity relationships
among both market regimes and local price patterns. Through-
out fast-mode training, the pretrained LLM backbone remains
frozen. The resulting token stream follows a deterministic
grammar that uniquely determines the type of the next token
from its position, enabling a factorized prediction objective in
which the softmax is restricted to the valid token subset associ-
ated with the next token type rather than competing over the en-
tire vocabulary. This design eliminates interference from irrele-
vant text tokens and better aligns optimization with the structure
of the discrete financial language.
The overall training objective is
Lfast =λ sumLCE sum +
2X
k=0
λLkLCE Lk .(4)
where later residual levels receive smaller weights due to their
higher entropy and lower predictability. The first patch of each
sequence is used only as context, while all subsequent tokens
contribute autoregressive prediction losses.
Fast mode learns an interface between the discrete finan-
cial language and the pretrained LLM. Only the newly intro-
duced financial-token embeddings and prediction heads are op-
timized, while all original Qwen parameters remain fixed. This
design allows the model to acquire forecasting ability without
altering its native language and reasoning capabilities, enabling
the same backbone to be reused by both the fast and slow modes
of DualCast.
3.3. Slow Mode: Text-Conditioned Forecast Revision
While the fast mode captures numerical regularities from his-
torical prices, it is intentionally blind to textual information.
The slow mode therefore formulates multimodal forecasting as
aforecast revisionproblem, refining a strong fast-mode base-
line using news and recent market context rather than generat-
ing a forecast from scratch. Such a revision-based formulation
mirrors how investors typically reason about markets: they first
extrapolate from observed trends and then revise their expecta-
tions in response to newly arriving information.
Formally, given historical pricesp 1:C, related newsT≤C, and
a fast-mode forecasty fast, the slow mode produces a refined
forecasty slow by conditioning on all three sources of informa-
tion.
To realize this revision process, we express each example in
the native chat format of the base language model. The prompt
contains three explicitly separated information sources: histor-
ical prices, related news, and the fast-mode forecast, while the
model is instructed to generate a refined forecast for the target
horizon together with a reasoning trace.
The slow mode is first initialized through supervised fine-
tuning on automatically constructed revision examples. For
each price–news pair, the base model is prompted to analyze
the potential market implications of the news and produce a
rationale followed by a refined forecast. To better align textual
reasoning with the newly introduced time-series vocabulary, we
augment a subset of training examples with an explicit trend de-
scription derived from recent price movements at the beginning
of the reasoning trace. This lightweight grounding procedure
encourages the model to associate time-series tokens with se-
mantic concepts such as upward, downward, or sideways mar-
ket behavior.
Supervision is applied primarily to the refined forecast to-
kens, while prompt tokens are masked. The trend-grounding
examples serve only as an auxiliary alignment signal and do not
alter the forecasting target. As a result, the model learns both
the revision behavior and the structured output format without
requiring manually annotated financial reasoning traces.
3.4. Slow Mode: Utility Optimization via Revision Feedback
While supervised fine-tuning enables the model to imitate
revision behavior from automatically constructed examples, it
primarily optimizes token-level likelihood and does not directly
reflect forecasting utility. In particular, it does not explicitly en-
courage the model to improve upon the fast-mode baseline in
a decision-relevant manner. As a result, the model may pro-
duce plausible revisions without consistently improving predic-
tive performance.
To address this limitation, we optimize the slow mode using
group-relative policy optimization (GRPO), directly operating
in the forecast (return) space. The training objective is defined
as a composite reward:
R=w impRimp +w ICRIC +w fmtRfmt,(5)
whereR imp measures improvement over the fast-mode baseline,
RIC captures cross-sectional directional consistency, andR fmt
enforces valid structured output.
Letρ(x) denote the cumulative return implied by forecastx,
and letρ ⋆ denote the realized cumulative return. We define a
volatility-normalized error:
e(x)= |ρ(x)−ρ ⋆| s ,s=2σ C √ H,(6)
whereσ C is estimated from the historical context andHis the
forecast horizon. The improvement reward is then defined as:
Rimp =clip
 e(yfast)−e(y slow)
max(e(yfast),∆) ,−1,1
!
.(7)
This formulation ensures that the slow mode is rewarded only
when it strictly improves upon the fast-mode forecast, explicitly
aligning optimization with the goal of forecast revision rather
than standalone prediction.
WhileR imp measures absolute improvement, financial deci-
sions are often driven by correct cross-sectional ranking rather
5

than point-wise accuracy. We therefore introduce a rank-based
directional reward computed over a rollout batch.
For each sampleiin a batch, we compute volatility-
normalized returns:
zi = ρ(yi) 2σi √Hi ,z ⋆ i = ρ⋆ i 2σi √Hi .(8)
We define a normalized rank operatorR(·) that maps values
within a batch to [0,1] with tie averaging:
˜zi =R(z i),˜z ⋆ i =R(z ⋆ i ).(9)
We define a cross-sectional rank-consistency reward using
the normalized within-batch ranks of the predicted and realized
volatility-normalized returns:
RIC,i =4

˜zi− 1 2 ! ˜z⋆ i − 1 2 ! ,(10)
Here, (˜zi) and (˜z⋆ i ) denote the predicted and realized ranks, re-
spectively. The reward is positive when the two ranks fall on
the same side of the rank midpoint and negative when they fall
on opposite sides. Aggregated over a rollout batch, it encour-
ages agreement in the relative ordering of returns across assets.
Because it depends only on ranks, this reward does not directly
measure the sign or numerical magnitude of an individual pre-
dicted return; forecast accuracy is addressed separately by the
return-space improvement reward.
We include a lightweight format rewardRfmt to enforce valid
structured generation, including separation between reasoning
traces and forecast tokens. It additionally penalizes language
collapse in the reasoning trace, discouraging degenerate repe-
tition and the leakage of time-series tokens into the textual ra-
tionale. This term primarily acts as a constraint and contributes
little gradient once training stabilizes.
The reinforcement learning objective aligns the slow mode
with the goal of forecast revision: improving upon a strong
numerical baseline while remaining sensitive to cross-sectional
market structure. This ensures that optimization is driven by
forecasting utility rather than language modeling likelihood.
4. Experiments
We evaluate DualCaston financial forecasting across mul-
tiple markets, sampling frequencies, and modalities to assess
both its forecasting accuracy and its ability to generalize be-
yond the distributions seen during pretraining. We first compare
DualCastagainst strong time-series foundation models, mul-
timodal forecasters, and general-purpose LLMs under a strict
zero-shot protocol. We then investigate its ability to transfer
across heterogeneous assets and unseen temporal resolutions,
and finally analyze the contribution of the proposed scale–shape
tokenizer and deliberative revision mechanism.
4.1. Experimental Setup
Table 1: Evaluation datasets, covering markets, sampling frequencies, and input
modalities. All datasets are evaluated zero-shot at horizonsH∈{16,32,64}.
Dataset Market/freq. Modality
MTBench-short [33] US eq., 5-min price only
SP500 [34] US eq., daily price+news
HS300 [34] CN eq., daily price+news
Energy [35] US gas, weekly price+news
Table 2: Parameter-efficient training footprint of DualCast. The 8.2B back-
bone remains frozen; 48.9M parameters (0.60%) are trained across the two
stages.
Component Params Trained
Qwen3-8B backbone 8.19 B frozen
+Financial tokens (4,097; embed+head) 33.6 M Stage 1
+LoRA adapter (q,v;r=32) 15.3 M Stage 2
Total trainable 48.9 M0.60%
We evaluate on three benchmark sources covering two fi-
nancial markets, three temporal resolutions, and both price-
only and multimodal forecasting settings. Together, they as-
sess generalization across markets, sampling frequencies, and
input modalities.MTBench-short[33] provides event-aligned
five-minute U.S. equity windows.FinMultiTime[34] provides
daily OHLC price series paired with timestamped financial
news for U.S. equities (SP500) and Chinese equities (HS300).
We use only text available at the forecast origin, ensuring strict
temporal causality. Table 1 summarizes the evaluation datasets,
markets, temporal resolutions, and input modalities.Time-
MMD (Energy)[35] consists of weekly U.S. gasoline retail
prices paired with textual market reports, extending evaluation
beyond equity markets to commodity price forecasting.
All settings use a lookback ofC=96 observations and hori-
zonsH∈{16,32,64}. We construct the evaluation origins using
the maximum horizonH max=64 and then reuse exactly the same
origins for the shorter horizons by truncating the target to its
first 16 or 32 observations. All baselines follow the same con-
struction. Table 2 summarizes the parameter-efficient training
footprint of DualCast; the backbone remains frozen through-
out both training stages.
We compare against three families: (1)time-series founda-
tion models, in their latest released versions, Chronos-2 [36],
TimesFM-2.5 [11], Timer [14], and Time-MoE [15], and
Moirai-2.0 [12]; (2)dedicated multimodal forecastersthat na-
tively consume text, ChatTime [37] and Aurora [38]; and (3) an
LLM-prompting baseline that feeds the same recent prices and
news to a general-purpose Qwen3-8B [9] as text and parses its
numeric forecast. All baselines run in their released zero-shot
configurations on the same windows and horizons.
6

Table 3: Forecasting MAPE (%,↓) across markets and frequencies. MTBench-short is five-minute and evaluated with price only; SP500/HS300 are daily, and
Energy is weekly. DualCastuses no dataset-specific fine-tuning. Best per column inbold.
MTBench (5-min) SP500 HS300 Energy
Model 16 32 64 16 32 64 16 32 64 16 32 64
Chronos-2 1.51 1.77 2.07 4.98 6.82 11.125.84 7.139.50 7.11 10.47 13.56
TimesFM-2.5 1.47 1.73 2.04 5.03 7.01 11.25 6.10 7.21 9.747.0910.43 13.65
Timer 1.59 1.90 2.25 7.04 9.61 15.17 6.38 7.77 10.63 7.76 10.70 13.91
Time-MoE 1.57 1.90 2.31 6.55 9.05 14.23 6.06 8.25 11.09 7.45 10.62 14.05
Moirai-2.0 1.46 1.72 2.03 5.03 7.09 11.29 6.17 7.20 9.49 7.1310.2013.59
ChatTime 2.10 2.41 2.72 5.68 7.43 11.39 6.82 7.91 10.14 15.55 16.49 17.60
Aurora 3.34 3.47 3.60 12.68 14.20 18.20 8.86 9.78 12.52 13.59 14.79 16.72
Qwen3 4.50 4.75 5.60 25.80 25.66 31.15 15.64 17.37 22.51 94.46 57.06 40.87
DualCast(Slow)1.45 1.68 1.96 4.81 6.45 9.807.08 7.589.197.38 10.3313.30
Because financial series span several orders of magnitude in
scale and absolute errors are not comparable across assets, we
report mean absolute percentage error (MAPE, %) at horizons
H∈{16,32,64}. For DualCastwe report the fast forecaster
(Fast), the SFT reviser (SFT), and the RL-tuned slow reviser
(Slow); Slowis the default.
4.2. Main Results
DualCast (Slow) achieves the lowest MAPE in 8 of 12
dataset–horizon settings as Table 3 shows, including H=64 on
all four evaluation subsets. On five-minute MTBench, whose
resolution is entirely unseen during pretraining, Slowobtains
the best results across all horizons. This demonstrates that the
scale–shape tokenizer is able to extract market patterns that
are agnostic to sampling frequency. Despite keeping the entire
backbone frozen, our method achieves competitive or superior
performance compared with cutting-edge time-series founda-
tion models, including Chronos-2, TimesFM-2.5, and Moirai-
2.0, especially at long forecasting horizons critical for real-
world financial analysis. Consistent with baseline protocols,
DualCast follows the same price-only pretraining paradigm and
only updates merely 0.6% of the total parameters. DualCast
clearly outperforms ChatTime and Aurora; feeding long news
text into ChatTime eveninflatesits error on Energy (≥15%),
as serializing text disrupts its numeric scale anchoring, whereas
our method keeps the model anchored to the price dynamics.
Figures 4 and 2 visualize stable forecasts across markets and
the Fast–SFT–Slow progression on identical windows, respec-
tively.
4.3. Refinement: Fast vs. Slow
DualCastprovides three forecasting modes based on the
same frozen backbone: the fast numerical forecaster (Fast),
a supervised fine-tuned reviser (SFT), and a reviser further
optimized by reinforcement learning (Slow). Table 4 com-
pares these modes on identical evaluation windows. MAPE
decreases or remains unchanged from Fast to SFT to Slow in
every dataset–horizon setting; SFT and Slow tie on MTBench-
short at H=16 and H=64. At H=64, MAPE decreases from
Table 4: Ablation of the three DualCastmodes on identical windows. MAPE
(%,↓); best per row group inbold. MTBench-short is five-minute and price-
only; SP500/HS300 are daily, and Energy is weekly.
Dataset ModeH=16 32 64
MTBench
Fast 1.49 1.76 2.05
SFT1.451.691.96
Slow1.45 1.68 1.96
SP500
Fast 6.23 9.03 15.26
SFT 5.68 7.87 14.03
Slow4.81 6.45 9.80
HS300
Fast 8.75 11.61 18.06
SFT 7.56 8.79 12.43
Slow7.08 7.58 9.19
Energy
Fast 9.73 15.02 24.48
SFT 7.73 11.08 14.24
Slow7.38 10.33 13.30
18.06% to 12.43% and then 9.19% on HS300, and from 15.26%
to 14.03% and then 9.80% on SP500. These comparisons show
that revision improves the fast forecast across the evaluated set-
tings, with larger gains at longer horizons. Figure 2 illustrates
this progression on representative windows.
Table 3 also shows that directly prompting Qwen3-8B with
recent prices and news as text yields substantially higher MAPE
than DualCast(Slow) on the daily equity subsets. On SP500,
Qwen3-8B records MAPE of 25.66–31.15% across the three
horizons, compared with 4.81–9.80% for DualCast(Slow).
On HS300, the corresponding ranges are 15.64–22.51% and
7.08–9.19%. Thus, direct text prompting is a weaker baseline
in these evaluations.
Table 6 quantifies the price of reasoning on SP500 (single
H800, batch 1, greedy decoding). The fast path emits only the
16 forecast tokens and completes in 0.37 s per window, whereas
the slow path autoregressively generates a∼167-token reason-
ing trace before regenerating the forecast, costing 5.85 s—about
16×more. Because the adapter is toggleable and both modes
share the frozen backbone, disabling deliberation recovers the
fast forecaster exactly, with no separate model to maintain. The
reasoning pass is therefore something to spend only when text is
7

Table 5: News ablation: point error (MAPE, %,↓) and directional accuracy (↑) of the Slowreviser with real news vs. with news removed, on identical date-aligned
windows. Better of the two conditions per column inbold.
MAPE (%,↓) Directional acc. (↑)
Dataset NewsH=16 32 64H=16 32 64
Energy removed7.3010.37 13.48 0.49 0.42 0.45 real 7.3110.32 13.27 0.55 0.54 0.51
SP500 removed 5.67 7.55 10.64 0.51 0.52 0.48 real5.63 7.49 10.56 0.53 0.55 0.50
HS300 removed 6.41 7.91 10.040.53 0.570.54 real6.25 7.68 9.770.48 0.550.55
(a) MTBench (5-minute)
 (b) SPIP, SP500 (daily)
Figure 2: Representative Fast–SFT–Slow forecasts on identical windows. Gray denotes the observed history, black the realized future, blue the fast Stage-1 forecast,
green the SFT reviser, and orange the RL-tuned slow reviser. The MTBench example shows a small refinement when the fast estimate is already reasonable;
the SP500 example shows the two refinement stages correcting a larger fast-mode deviation. These cases are illustrative; aggregate improvements are reported in
Table 4.
Table 6: Cost of deliberation: per-forecast latency (median) and number of
generated tokens on SP500 (single H800, batch 1, greedy decoding). The fast
path decodes only the forecast tokens; the slow path additionally generates a
reasoning trace and regenerates the forecast.
Mode Latency (s) Avg Generated tokens
Fast0.37 16
Slow5.85 199
likely to matter, while the large majority of forecasts are served
by the cheap fast path.
4.4. Does Text Help? A News Ablation
The revision-based slow mode is designed to fold textual in-
formation into a numerical forecast, but MAPE alone cannot
reveal whether the text is actually used: a lower error may sim-
ply reflect the RL stage sharpening the numerical baseline. To
isolate the contribution of text, we re-run the Slowreviser on
strictly date-aligned windows under two conditions–with the
real news at the forecast origin, and with the news removed–
holding everything else fixed. To assess whether news affects
forecast direction as well as point accuracy, we also report di-
rectional accuracy.
Table 5 shows that the text channel is useful, and we evaluate
performance via two complementary metrics: point-prediction
MAPE and directional accuracy. Forpoint error, real news
lowers MAPE in eight of the nine dataset–horizon comparisons.
The gains are largest and most consistent on HS300 (−0.16/−
0.23/−0.27), remain positive on SP500 (−0.04/−0.06/−0.08),
and appear at the longer Energy horizons (−0.05/−0.21 for
H=32/64); the only exception is a negligible+0.01 increase on
Energy atH=16. Fordirection, Energy improves at every hori-
zon (+0.06/+0.12/+0.06), and SP500 shows smaller consistent
gains (+0.02/+0.03/+0.02). HS300 is mixed: news improves
point accuracy at all horizons but directional accuracy only at
H=64. These ablations indicate that real news improves point
accuracy in most tested settings, while its effect varies across
datasets, horizons, and metrics. They also show that news con-
ditioning is not uniformly beneficial for every metric and hori-
zon, motivating selective activation of the slow path rather than
unconditional deliberation.
4.5. Tokenizer Analysis
Two design choices underlie the scale–shape tokenizer. First,
each RVQ codeword maps to one embedding row in the ex-
tended vocabulary, so highly imbalanced assignments produce
correspondingly imbalanced training of the added vocabulary.
Our Adaptive Frequency-Equalizing RVQ (AFE-RVQ) peri-
odically splits overloaded latent clusters and relocates their
sub-centers into starved slots.
Under the controlled 3×1024 setting, AFE-RVQ preserves
reconstruction performance (0.0783→0.0781), while achiev-
ing a modest improvement in finite-budget active-code fraction
(0.839→0.854).
8

(a) HPE,H=32
 (b) BMRN,H=64
Figure 3: Additional SP500 revision examples. The slow path (orange) conditions on the fast forecast (blue) and causally available text. In both examples it removes
a substantial portion of the fast path’s scale or local-trajectory error, although it does not reproduce every short-term fluctuation in the realized path (black). These
examples complement the paired aggregate news ablation in Table 5.
(a) MTBench (5-minute)
 (b) SP500 (daily)
(c) HS300 (daily)
Figure 4: Representative slow-path forecasts (orange dashed) against the realized future (black) following the observed history (gray); the dotted vertical line marks
the forecast origin. The three examples cover five-minute MTBench and daily SP500 and HS300 data.
The primary benefit of AFE-RVQ lies in mitigating skewed
codeword usage. Peak load — the maximum assignment count
relative to uniform expectation — drops drastically across all
residual layers. ForL 0, the worst-case codeword load falls
from 7.9×to 3.9×; forL 1 from 5.0×to 2.6×; forL 2 from
3.4×to 2.1×. Extreme peak load means a small subset of code-
words dominate training updates, harming embedding learning
for under-utilized entries.
4.6. Qualitative Analysis
Figure 4 shows stable slow-path forecasts across five-minute
MTBench and daily U.S. and Chinese equities. Figure 2 sepa-
rately visualizes the progression from Fast to SFT and RL. Fig-
ure 3 adds two SP500 windows in which slow revision reduces
a substantial fast-path error. Figure 5 presents two directional
correction cases with accompanying news and model-generated
chain-of-thought rationales. These examples illustrate individ-
ual revisions; aggregate effects on forecast accuracy and direc-
tion are reported in Tables 4 and 5.
5. Limitations
This work has two main limitations. First, the beneficial ef-
fect of textual news is heterogeneous across different market do-
mains and forecasting settings. While news information effec-
tively improves forecasting performance in most scenarios, the
magnitude of its contribution varies across asset types and pre-
diction horizons, leading to marginal or mixed improvements
under certain conditions.
Second, the high-performance slow deliberation mode suf-
fers from limited inference speed and increased computational
overhead. Compared with the efficient fast forecasting path,
9

COPX (Copper Miners ETF)•U.S. market•bullish (H=64)
Fast−3.3%−→Slow+5.9%−→Real+5.2%
News.An approximately $131.4M weekly inflow into the Copper Miners
ETF (COPX)—a 4.9% increase in outstanding units—while several under-
lying miners are slightly lower on the day.
Reasoning. (1) The large ETF inflow signals rising institutional interest in
copper miners, despite mixed short-term moves in individual constituents.
(2) Net inflows indicate positive sentiment; if demand fundamentals hold,
gradual upward pressure should continue. (3) I expect COPX to rise mod-
erately over the next 64 trading days, roughly+5% to+10%.
Outcome.Fastwrongly predicts a slight decline; the news-grounded revi-
sion flips the forecast upward and nearly matches the realized+5.2%.
Kuang-Chi Technologies (002625.SZ)•Chinese market•bearish
(H=64)
Fast+27.6%−→Slow−3.0%−→Real−6.4%
News.The controlling shareholder and its concert parties announce a plan
to reduce their stake by up to 2% of shares outstanding.
Reasoning. (1) A controlling-shareholder sell-down raises concerns about
valuation and outlook; with the price already in decline, it can intensify
selling pressure. (2) Share reductions are generally read as a negative sig-
nal, driving near-term outflows and weaker sentiment. (3) Over the next 64
trading days I expect continued downward pressure, about−5% to−7%.
Outcome.Fastconfidently predicts a large rise; reading the insider sell-
down as bearish, the revision corrects the sign and tracks the realized
−6.4%.
Figure 5: Interpretable revisions: two representative cases where the Slowreviser reads the news, reasons explicitly, and corrects the direction (and sign) of the Fast
forecast while approximately matching the realized magnitude. Such directional corrections are illustrative rather than universal; consistent with the news ablation
(Table 5), text helps where it carries information beyond the price path.
the slow path requires additional reasoning token generation,
which substantially increases inference latency. This limits the
deployment efficiency of the slow mode in time-sensitive real-
world scenarios. Optimizing the reasoning efficiency of the de-
liberative forecasting pipeline remains a promising direction for
future work.
6. Conclusion
We introduced DualCast, a dual-path language-model
framework for financial time-series forecasting. The frame-
work represents each return patch via disentangled summary
and residual shape tokens, and leverages AFE-RVQ to bal-
ance codeword usage while maintaining high reconstruction fi-
delity. Based on a frozen Qwen3-8B backbone, DualCast sup-
ports two complementary inference modes: a fast financial to-
ken decoder for efficient numerical forecasting, and a LoRA-
enhanced slow revision module that incorporates causal news
information and refines fast predictions. The slow path is ini-
tialized via supervised fine-tuning and further optimized with
return-space GRPO to improve revision quality. Extensive ex-
periments across minute-level U.S. equities, daily U.S. and Chi-
nese equities, and weekly energy markets demonstrate that the
slow revision mode achieves superior performance, especially
over long forecasting horizons. Ablation studies validate the ef-
fectiveness of news-guided revision and reinforcement learning
optimization. News inputs consistently reduce point prediction
errors across most dataset-horizon settings and deliver promi-
nent directional improvements on energy assets.
Empirical results verify our core design paradigm: multi-
modal financial forecasting can be effectively formulated as
an optional news-based revision upon strong numerical base
predictions. Future work will explore uncertainty-aware eval-
uation, generalized market adaptation, and learnable routing
strategies to further balance prediction accuracy and inference
efficiency.
7. Acknowledgement
This work was supported by the Science and Technology
Program of Qingdao Municipality under Grant 25-1-1-gjgg-32-
gx.
References
[1] M. Jin, S. Wang, L. Ma, Z. Chu, J. Zhang, X. Shi, P.-Y .
Chen, Y . Liang, Y .-F. Li, S. Pan, et al., Time-llm: Time
series forecasting by reprogramming large language mod-
els, in: International conference on learning representa-
tions, V ol. 2024, 2024, pp. 23857–23880.
[2] T. Zhou, P. Niu, L. Sun, R. Jin, et al., One fits all: Power
general time series analysis by pretrained lm, Advances in
neural information processing systems 36 (2023) 43322–
43355.
[3] C. Sun, H. Li, Y . Li, S. Hong, Test: Text prototype aligned
embedding to activate llm’s ability for time series, in: In-
ternational Conference on Learning Representations, V ol.
2024, 2024, pp. 37854–37881.
[4] N. Gruver, M. Finzi, S. Qiu, A. G. Wilson, Large language
models are zero-shot time series forecasters, Advances in
neural information processing systems 36 (2023) 19622–
19635.
[5] A. F. Ansari, L. Stella, C. Turkmen, X. Zhang, P. Mercado,
H. Shen, O. Shchur, S. S. Rangapuram, S. P. Arango,
S. Kapoor, et al., Chronos: Learning the language of time
series, arXiv preprint arXiv:2403.07815 (2024).
[6] S. Talukder, Y . Yue, G. Gkioxari, Totem: Tokenized time
series embeddings for general time series analysis, arXiv
preprint arXiv:2402.16412 (2024).
10

[7] Y . Zhou, Y . Luo, M. Cheng, Q. Liu, J. Wang, D. Wang,
E. Chen, Time series forecasting as reasoning: A slow-
thinking approach with reinforced llms, arXiv preprint
arXiv:2506.10630 (2025).
[8] F. Parker, N. Chan, C. Zhang, K. Ghobadi, Eliciting chain-
of-thought reasoning for time series analysis using re-
inforcement learning, arXiv preprint arXiv:2510.01116
(2025).
[9] A. Yang, A. Li, B. Yang, B. Zhang, B. Hui, B. Zheng,
B. Yu, C. Gao, C. Huang, C. Lv, et al., Qwen3 technical
report, arXiv preprint arXiv:2505.09388 (2025).
[10] E. J. Hu, Y . Shen, P. Wallis, Z. Allen-Zhu, Y . Li, S. Wang,
L. Wang, W. Chen, Lora: Low-rank adaptation of
large language models, arXiv preprint arXiv:2106.09685
(2021).
[11] A. Das, W. Kong, R. Sen, Y . Zhou, A decoder-only foun-
dation model for time-series forecasting, arXiv preprint
arXiv:2310.10688 (2023).
[12] G. Woo, C. Liu, A. Kumar, C. Xiong, S. Savarese, D. Sa-
hoo, Unified training of universal time series forecasting
transformers, arXiv preprint arXiv:2402.02592 (2024).
[13] M. Goswami, K. Szafer, A. Choudhry, Y . Cai, S. Li,
A. Dubrawski, Moment: A family of open time-series
foundation models, arXiv preprint arXiv:2402.03885
(2024).
[14] Y . Liu, H. Zhang, C. Li, X. Huang, J. Wang, M. Long,
Timer: Generative pre-trained transformers are large time
series models, arXiv preprint arXiv:2402.02368 (2024).
[15] X. Shi, S. Wang, Y . Nie, D. Li, Z. Ye, Q. Wen, M. Jin,
Time-MoE: Billion-scale time series foundation models
with mixture of experts, arXiv preprint arXiv:2409.16040
(2024).
[16] Y . Liu, G. Qin, Z. Shi, Z. Chen, C. Yang, X. Huang,
J. Wang, M. Long, Sundial: A family of highly ca-
pable time series foundation models, arXiv preprint
arXiv:2502.00816 (2025).
[17] T. Zhu, W. Zhao, R. Sun, B. Luan, J. Lu, S. Wang, J. Li,
D. Jiang, Y . He, Z. Bai, From knowing to doing: A
memory-controlled benchmark for llm trading agents on
stock markets, arXiv preprint arXiv:2605.28359 (2026).
[18] Y . Nie, N. H. Nguyen, P. Sinthong, J. Kalagnanam, A
time series is worth 64 words: Long-term forecasting with
transformers, arXiv preprint arXiv:2211.14730 (2022).
[19] S. Lee, T. Park, K. Lee, Learning to embed time series
patches independently, in: International Conference on
Learning Representations, V ol. 2024, 2024, pp. 27599–
27620.
[20] T. Kim, J. Kim, Y . Tae, C. Park, J.-H. Choi, J. Choo, Re-
versible instance normalization for accurate time-series
forecasting against distribution shift, in: International
conference on learning representations, 2021.
[21] N. Zeghidour, A. Luebs, A. Omran, J. Skoglund,
M. Tagliasacchi, Soundstream: An end-to-end neural au-
dio codec, IEEE/ACM Transactions on Audio, Speech,
and Language Processing 30 (2021) 495–507.
[22] C. Fifty, R. Junkins, D. Duan, A. Iyengar, J. Liu, E. Amid,
S. Thrun, C. Ré, Restructuring vector quantization with
the rotation trick, in: International Conference on Learn-
ing Representations, V ol. 2025, 2025, pp. 19153–19188.
[23] A. Van Den Oord, O. Vinyals, et al., Neural discrete rep-
resentation learning, Advances in neural information pro-
cessing systems 30 (2017).
[24] Y . Xu, S. B. Cohen, Stock movement prediction from
tweets and historical prices, in: Proceedings of the 56th
Annual Meeting of the Association for Computational
Linguistics (V olume 1: Long Papers), 2018, pp. 1970–
1979.
[25] D. Araci, Finbert: Financial sentiment analysis
with pre-trained language models, arXiv preprint
arXiv:1908.10063 (2019).
[26] S. Wu, O. Irsoy, S. Lu, V . Dabravolski, M. Dredze,
S. Gehrmann, P. Kambadur, D. Rosenberg, G. Mann,
Bloomberggpt: A large language model for finance, arXiv
preprint arXiv:2303.17564 (2023).
[27] H. Yang, X.-Y . Liu, C. D. Wang, Fingpt: Open-
source financial large language models, arXiv preprint
arXiv:2306.06031 (2023).
[28] T. Li, Z. Liu, Y . Shen, X. Wang, H. Chen, S. Huang, Mas-
ter: Market-guided stock transformer for stock price fore-
casting, in: Proceedings of the AAAI conference on arti-
ficial intelligence, V ol. 38, 2024, pp. 162–170.
[29] M. Cheng, J. Wang, D. Wang, X. Tao, Q. Liu, E. Chen,
Can slow-thinking llms reason over time? empirical stud-
ies in time series forecasting, in: Proceedings of the Nine-
teenth ACM International Conference on Web Search and
Data Mining, 2026, pp. 99–110.
[30] Y . Kong, Y . Yang, S. Wang, C. Liu, Y . Liang, M. Jin,
S. Zohren, D. Pei, Y . Liu, Q. Wen, Achieving time series
reasoning requires rethinking model design, tasks formu-
lation, and evaluation, arXiv preprint arXiv:2502.01477
(2025).
[31] Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, X. Bi, H. Zhang,
M. Zhang, Y . Li, Y . Wu, et al., Deepseekmath: Pushing the
limits of mathematical reasoning in open language mod-
els, arXiv preprint arXiv:2402.03300 (2024).
11

[32] Q. Yu, Z. Zhang, R. Zhu, Y . Yuan, X. Zuo, Y . Yue, W. Dai,
T. Fan, G. Liu, L. Liu, et al., Dapo: An open-source llm
reinforcement learning system at scale, Advances in Neu-
ral Information Processing Systems 38 (2026) 113222–
113244.
[33] J. Chen, A. Feng, Z. Zhao, J. Garza, G. Nurbek, C. Qin,
A. Maatouk, L. Tassiulas, Y . Gao, R. Ying, Mtbench: A
multimodal time series benchmark for temporal reasoning
and question answering, arXiv preprint arXiv:2503.16858
(2025).
[34] W. Xu, D. Xiang, Y . Liu, X. Wang, Y . Ma, L. Zhang,
S. Hu, C. Xu, J. Zhang, Finmultitime: A four-modal
bilingual dataset for financial time-series analysis, arXiv
preprint arXiv:2506.05019 (2025).
[35] H. Liu, S. Xu, Z. Zhao, L. Kong, H. Kamarthi, A. B. Sasa-
nur, M. Sharma, J. Cui, Q. Wen, C. Zhang, et al., Time-
mmd: Multi-domain multimodal dataset for time series
analysis, Advances in Neural Information Processing Sys-
tems 37 (2024) 77888–77933.
[36] A. F. Ansari, O. Shchur, J. Küken, A. Auer, B. Han,
P. Mercado, S. S. Rangapuram, H. Shen, L. Stella,
X. Zhang, et al., Chronos-2: From univariate to univer-
sal forecasting, arXiv preprint arXiv:2510.15821 (2025).
[37] C. Wang, Q. Qi, J. Wang, H. Sun, Z. Zhuang, J. Wu,
L. Zhang, J. Liao, Chattime: A unified multimodal time
series foundation model bridging numerical and textual
data, in: Proceedings of the AAAI Conference on Artifi-
cial Intelligence, V ol. 39, 2025, pp. 12694–12702.
[38] X. Wu, J. Jin, W. Qiu, P. Chen, Y . Shu, B. Yang, G. Guo,
Aurora: Towards universal generative multimodal time se-
ries forecasting, in: International Conference on Learning
Representations, V ol. 2026, 2026, pp. 103239–103277.
12
