---
title: 'Artificial Intelligence in Equity and Crypto Markets: Progress, Profitability Evidence, and the
  Limits of Automated Investing'
url: https://arxiv.org/abs/2609.04917
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Linsen Zhu
- Mengqing Cai
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.04917
pages: 32
chars: 115872
fetched_at: '2026-11-08T13:33:06+00:00'
kb_version: 1
---

# Artificial Intelligence in Equity and Crypto Markets: Progress, Profitability Evidence, and the Limits of Automated Investing

Artificial Intelligence in Equity and Crypto Markets:
Progress, Profitability Evidence, and the Limits of Automated
Investing
Linsen Zhu Mengqing Cai
Literature cutoff: 31 August 2026
Abstract
Artificial intelligence (AI) now supports investment workflows from data and prediction
through research, portfolios, execution, and tool use. Technical capability, however, is not
evidence of investment profitability. This critical state-of-the-art review examines public research
available through 31 August 2026 on listed equities, exchange-traded funds, centralized crypto
spot, perpetual futures, and on-chain markets. We organize evidence with analpha-translation
chain: point-in-time information must yield a stable signal, feasible positions, executable orders,
and risk-adjusted returns after costs. Across machine learning, time-series foundation models,
financial language models, reinforcement learning, and agents, the examined record shows real
but mainly upstream progress in prediction, text processing, portfolio design, and workflow
integration. Evidence is thinner for durable net performance. Temporal contamination, repeated
selection, survivorship, weak benchmarks, implementation costs, venue mechanics, and capacity
can break translation to net alpha. Strong historical results coexist with predictor decay, corrected
look-ahead failures, mixed prospective evidence, and few audited live-capital records. Crypto
adds informative state but requires separate treatment of spot, perpetual, and decentralized cash
flows and execution. Within the public evidence examined here, no general AI architecture is
shown to deliver persistent, cross-regime, capacity-aware net alpha. More credible claims require
point-in-time data and models, decision-aligned objectives, joint portfolio–execution evaluation,
controlled adaptation, prospective tests, and authority-matched governance. These conditions
can improve evidence and implementation; they do not guarantee profit.
Keywords:artificial intelligence; machine learning; asset pricing; algorithmic trading; large
language models; reinforcement learning; portfolio choice; market microstructure; cryptocurrency;
financial agents
1 Introduction
Artificial intelligence (AI) has moved from a specialized forecasting technique to an organizing
layer for investment workflows. A contemporary system may ingest prices, accounting variables,
analyst text, news, social media and blockchain state; generate forecasts or research narratives;
translate them into holdings under risk constraints; and route orders through broker, exchange
or smart-contract tools. The literature mirrors this expansion. Cross-sectional machine learning
(ML) studies estimate nonlinear return functions from hundreds of firm characteristics (Gu et al.,
2020; Chen et al., 2024). Deep policies map state variables directly to portfolio weights (Simon
et al., 2026); cost-aware methods optimize implementable portfolios rather than forecasts (Jensen
et al., 2026); and natural language processing (NLP) turns unstructured disclosure and news into
1
arXiv:2609.04917v1  [cs.AI]  4 Sep 2026

investable signals (Tetlock, 2007; Loughran and McDonald, 2011; Ke et al., 2019). More recently,
large language models (LLMs) and agents have joined retrieval, memory, debate, analysis, order
APIs and feedback loops within a single interface (Yu et al., 2023; Zhang et al., 2024; Yu et al., 2024;
Xiao et al., 2024). These studies document genuine technical progress. They do not, by themselves,
answer the economically decisive question: does the progress produce sustainable net alpha?
That question is harder than asking whether a model predicts labels or whether a backtest
earns a positive return. A forecast is not a portfolio; a portfolio return is not alpha unless the risk
adjustment is stated; gross alpha is not net alpha; and a historical test labelled “out of sample” is
not a prospectively committed trading record. Even a correctly timestamped and cost-adjusted
simulation can overstate attainable performance if it ignores capacity, market impact, borrowing,
execution delay, model-selection multiplicity, or changes caused by other investors adopting the
same signal. Conversely, the observation that many published anomalies decay does not imply
that all predictability is spurious. Large open replication exercises reproduce substantial parts of
the cross-sectional record (Chen and Zimmermann, 2022; Jensen et al., 2023), while institutional
transaction data suggest that some established styles are cheaper and more scalable than pessimistic
trading-cost models imply (Frazzini et al., 2018). The relevant assessment is therefore neither
technological enthusiasm nor blanket market-efficiency scepticism. It is a stage-by-stage audit of
what survives implementation.
This review develops that audit as analpha-translation chain. Information must be available
at the decision time; a learned representation must produce incremental and stable information;
the decision rule must convert it into positions under financing and risk constraints; orders must
receive plausible fills; and realized gains must remain after fees, spreads, price impact, funding, taxes
or protocol-specific extraction. Performance must then persist across regimes, capital scales and
independent or prospective tests. The chain provides a common language for methods that otherwise
resist comparison. A time-series foundation model may be valuable because it transfers forecast
structure, an LLM because it extracts an event, an RL policy because it internalizes sequential costs,
and an agent because it coordinates tools. None receives an exemption from economic validation
simply because its architecture is newer or more general.
The same framework also explains why “financial markets” cannot be treated as one benchmark.
Listed equities and exchange-traded funds (ETFs) operate through scheduled sessions, regulated
disclosure, corporate actions, centralized limit-order books, settlement and established shorting
and market-access rules. Centralized crypto spot markets trade continuously across fragmented
venues, with changing token universes, custody and data-integrity risks. Perpetual futures add
funding payments, mark prices, leverage, margin and discontinuous liquidation. On-chain markets
expose auditable state and composable transactions but introduce gas auctions, smart-contract risk,
automated-market-maker (AMM) inventory loss, transaction reordering and maximal extractable
value (MEV). An equity backtest cannot validate a perpetual strategy by analogy; a directionally
correct on-chain signal can still lose its surplus to ordering and fees. We consequently keep
equities/ETFs, centralized spot, perpetuals and decentralized execution analytically separate, while
asking which modeling principles transfer.
Our central conclusion is deliberately bounded. Within the public record examined through 31
August 2026, evidence supports meaningful advances in representation, prediction, textual informa-
tion processing, portfolio design and operational integration. Selected studies report economically
large historical out-of-sample results, including nonlinear equity models and decision-focused policies.
The same record does not establish that a general AI method, foundation model or agent architecture
delivers persistent, cross-regime and capacity-aware net alpha. The gap is not a semantic technicality.
A look-ahead correction can eliminate a celebrated ML alpha (Zhang et al., 2025); LLMs can recall
pre-training-period financial facts that appear to be forecasts (Lopez-Lira et al., 2026); cost-unaware
2

learners can load on fleeting signals that sit outside the implementable efficient frontier (Jensen
et al., 2026); and prospective AI-managed household portfolios can be concentrated without earning
statistically significant abnormal returns (Carlin et al., 2026). Evidence on AI-labelled hedge funds
further suggests that early relative performance can decay as a technology diffuses (Chen et al.,
2026). These findings do not refute every strategy. They locate where claims become fragile in the
evidence examined.
The financial disciplines used here—point-in-time information, explicit benchmarks, implemen-
tation costs, capacity and prospective validation—are established principles, not inventions of this
review. The contribution is their synthesis and joint application across AI method classes and
market strata. First, we connect return prediction, language models, portfolio choice, execution
and agents along one investment chain. Second, we define a multidimensional evidence profile and
a set of evaluation-design archetypes that distinguish task metrics, historical prediction, portfolio
simulation, prospective evaluation, live-capital operation and external persistence without collapsing
them into one rank. Third, we apply a common validation framework to stocks and crypto while
preserving their different payoff and microstructure equations. Common criteria do not imply equal
evidentiary depth: the AI-specific crypto record examined here is thinner than the equity record.
Fourth, we turn recurring failure modes into a constructive research agenda: point-in-time data
and model checkpoints; economic rather than proxy objectives; joint signal, portfolio and execution
evaluation; regime-aware updating; transparent prospective protocols; and controls proportionate to
trading authority.
The remaining sections proceed from claims to mechanisms and then back to evidence. Section 2
defines the critical-review method and evidentiary boundaries. Section 3 formalizes alpha translation
and the evidence profile. Sections 4–6 assess predictive models, language and agent systems, and
portfolio/RL approaches. Section 7 compares the four market strata and their execution losses.
Section 8 weighs affirmative and contrary profitability evidence. Section 9 develops the research
agenda, and Section 10 states what can and cannot presently be concluded.
2 Scope, Review Method, and Evidentiary Boundaries
2.1 A critical state-of-the-art review, not a systematic review
This article is a critical state-of-the-art review of research and primary official material available by
31 August 2026. Its purpose is conceptual integration and adversarial evaluation of profitability
claims, not exhaustive enumeration or pooled effect estimation. We searched iteratively across
finance, economics, machine learning, NLP and market-microstructure venues; followed backward
and forward citations around influential primary studies; checked publisher or proceedings records
where available; and used first-party documentation for operational interfaces and regulatory controls.
We prioritize peer-reviewed articles and official proceedings, then identifiable working papers or
dated arXiv versions for rapidly changing topics. Official vendor pages establish that a product or
interface existed and what its publisher said it could do; they do not establish return performance.
Surveys are used for orientation, not as substitutes for the underlying evidence.
This method has intentional limits. It does not claim database-complete retrieval, duplicate
independent screening, a registered protocol, or formal risk-of-bias scores for every record. It is
therefore not labelled a systematic review, systematic map or meta-analysis. Quantitative pooling
would in any case be misleading for much of this literature: reported Sharpe ratios differ in sampling
frequency, annualization, universe, leverage, cash rate, benchmark, risk model, transaction-cost
assumptions and model-selection budget. We instead use structured critical comparison. Claims
central to the argument are anchored to primary studies, strong contrary findings are retained, and
3

inference is separated from directly reported results. Two ancillary audit aids included with the
source package—a claim–evidence map and a representative study-level evidence profile—record the
support, contrary evidence and unresolved dimensions behind the main synthesis. They remain
selective aids rather than systematic extraction sheets.
2.2 Inclusion boundaries
The method boundary is broad but economically specific. We include classical ML, deep learning
(DL), time-series foundation models (TSFMs), NLP and LLMs, multimodal models, RL, portfolio
and risk optimization, learned execution, and agentic systems when they bear on investment research,
allocation or trading. We exclude generic financial chatbots, credit underwriting, fraud detection
and corporate forecasting unless a result directly informs traded-asset decisions. “AI” is the umbrella
term, not a synonym for LLMs. A prompted workflow is not called RL without an explicit sequential
learning objective, and tool use is not called autonomy unless the system has documented delegated
authority.
The asset boundary covers listed common stocks and ETFs, centralized crypto spot, crypto
perpetual futures, and on-chain/DEX markets. It includes cross-asset information when used to
trade one of those strata. It does not attempt full treatment of fixed income, foreign exchange,
options, commodities, private assets or market making outside the crypto mechanisms needed
here. ETFs are included because they are both investable portfolios and an execution vehicle for
asset-allocation policies; they are not assumed to be passive. Crypto-linked ETFs remain listed
securities for execution analysis even when their underlying exposure is crypto.
2.3 The unit of evidence
The unit of evidence is a precisely bounded claim, not a paper-level endorsement. A study can
provide strong evidence that a representation predicts returns and weak evidence that the resulting
strategy is deployable. We record at least seven dimensions when interpreting an economic result:
1. T emporality: Were observations, releases, constituent membership and model artifacts available
at the decision timestamp?
2. Selection: How many features, architectures, prompts, assets, periods and hyperparameters
were tried before the reported result?
3. Portfolio mapping: Are leverage, shorting, concentration, turnover and financing feasible and
disclosed?
4. Implementation: Which commissions, spread, price impact, delay, borrow, funding, gas and
failed transactions are included?
5. Risk and benchmark: Is “alpha” measured against an explicit factor model, and are uncertainty
and serial dependence handled?
6. External validity: Does evidence cross assets, venues, regimes, scales or an independently
maintained test?
7. Operational provenance: Is the result a retrospective simulation, a prospectively timestamped
paper portfolio, or contemporaneously documented live capital?
Absence of a reported item is coded conceptually as unknown, not favourable. For example, a
strategy described as “net” is net only of its disclosed cost model. We do not infer zero latency or
4

unlimited borrow because a paper is silent. Likewise, a platform that exposes an order endpoint
demonstrates connectivity, not safe operation or investment skill.
2.4 Reading positive and negative evidence symmetrically
Financial ML debates are especially vulnerable to asymmetric standards. A large backtest cannot
prove permanence, but one failed replication cannot prove universal impossibility. Multiple-testing
corrections show why discovery thresholds must rise as researchers search more strategies (Harvey
et al., 2016; White, 2000; Bailey et al., 2017); large replication projects then disagree about how
much of the published cross section survives. Hou et al. (2020) report that a majority of 452
anomalies fail conventional significance in their reconstruction and that an even larger share fails
a higher, multiple-testing-aware threshold. In contrast, Chen and Zimmermann (2022) reproduce
almost all of 319 published characteristics under a transparent common code base, and Jensen
et al. (2023) find broad international evidence for many return predictors. The difference reflects
definitions, implementations, samples and thresholds as well as genuine empirical disagreement. We
preserve it rather than selecting the conclusion that best fits a technological narrative.
The same symmetry applies to trading costs. Novy-Marx and Velikov (2016) show that costs
disproportionately erode high-turnover strategies and that trading rules can change implementability.
Using a large proprietary record of institutional trades, Frazzini et al. (2018) report costs lower and
capacity higher than several pessimistic estimates for some styles. Neither result licenses a universal
cost assumption. A credible AI study should present sensitivity to investor size, participation,
urgency and venue, because the cost function is conditional on precisely those variables.
2.5 What this review means by sustainable net alpha
We reservealphafor abnormal return relative to a stated risk model, andnet returnfor return after
explicitly modeled implementation costs.Sustainable net alphais a higher evidentiary standard:
positive risk-adjusted performance must survive time-valid external or prospective evaluation across
materially different regimes and remain positive at a stated scale. “Sustainable” does not mean
eternal; it requires a defensible horizon, capacity and monitoring rule. This definition intentionally
sets a higher bar than most individual papers attempt. Our conclusion that the public evidence
examined here is insufficient at this bar is therefore not the claim that no AI strategy has ever
earned money, that proprietary systems cannot work, or that markets are perfectly efficient. It
means the examined public record does not support a general, portable promise.
Finally, profitability is not the only legitimate output. AI can reduce research time, standardize
evidence retrieval, detect operational exceptions, improve scenario analysis or make a decision trail
auditable. Those benefits may be economically important even when incremental alpha is zero.
The review nevertheless keeps productivity and investment performance separate: saved analyst
hours are not silently added to a Sharpe ratio, and a coherent generated report is not scored as a
profitable trade.
3 From Model Output to Sustainable Net Alpha
3.1 The alpha-translation chain
The core analytical object is not a model but a conversion process. LetIt denote the point-in-time
information set, including the historical version of data and the model available at timet. A
representationzt =fθ(It)may support a forecast ˆrt+1, a ranking, an event label or a distribution.
5

Point-in-time
information
Representation
and signal
Decision,
portfolio
and risk
Orders, fills
and costs
Net alpha,
capacity
and per-
sistence
revision, sur-
vivorship, model-
memory leakage
overfit, weak
labels, unsta-
ble regimes
turnover,
leverage, concen-
tration, borrow
spread, impact,
latency, funding,
gas, MEV
selection,
crowding,
scale, gover-
nance failure
Prospective monitoring
controlled updating
Figure 1: The alpha-translation chain. Technical improvement at one stage is economically valuable
only to the extent that information survives all downstream transformations. Red labels identify
representative failure channels, not an exhaustive list.
A policyπ converts the representation and current state into target holdingsw∗ t =π(zt, ~wt−1,ct)
under constraintsct, where ~wt−1 denotes realized post-fill holdings from the preceding decision. An
execution rule convertsw∗ t− ~wt−1 into orders; realized fills then determine the post-fill holdings~wt.
For a generic portfolio, one-period realized net return can be written schematically as
Rnet p,t+1 = ~w⊤ t rt+1−C fee t −C spread t −C impact t −C delay t −C fin t −C venue t ,(1)
where everyCt term is a return-normalized deduction for the same measurement period—or,
equivalently, a currency cost divided by beginning net asset value—and may depend on submitted
orders, realized fills and holdings. Financing includes borrow and leverage costs, and venue-specific
losses may include perpetual funding, liquidation, gas, failed transactions or MEV. Taxes are
material to many investors but are rarely modeled consistently and are therefore kept explicit
rather than presumed. Alpha is the intercept from a stated risk model fitted toRnet p,t, not another
name for the left-hand side. Sustainable net alpha additionally requires persistence outside the
researcher-selected environment and at a stated capital scale.
Figure 1 shows why evidence can weaken even while components improve. Each arrow is a possible
loss of validity. Revised fundamentals, delisted firms or pretraining memories can contaminate the
information set. A high-R2 forecast can be concentrated in low-capacity securities. A ranker can
induce excessive turnover. A target portfolio can require unavailable borrow. A correct order can
be filled after its signal decays. A profitable simulation can disappear when many investors deploy
it, or it can be operationally unacceptable because no one can reconstruct the source, model version
or authorization path. The last box feeds back to earlier stages because performance and controls
must be monitored rather than frozen after deployment.
3.2 A multidimensional evidence profile, not a leaderboard
Evidence quality is a profile rather than a scalar tier. For each economic claim, we assess the
seven dimensions introduced in Section 2: temporality (T), selection control (S), portfolio mapping
(P), implementation realism (I), risk and benchmark specification (R), external validity (X), and
operational provenance (O). The profile is
E= (T,S,P,I,R,X,O).(2)
6

Table 1: Evaluation-design archetypes within a multidimensional profitability-evidence profile. Rows
are common study designs, not a total ordering; each must be assessed on all seven dimensions in
Equation 2.
Code Evidence object Primary support Dimensions unresolved unless reported
CAP Architecture or ven-
dor capability
Feasibility of representation, tool use or
order connectivity
Prediction, portfolio mapping and return
TASK Task metric Classification, extraction, reasoning or
forecast accuracy on a defined benchmark
Feasible positions, implementation and
economic value
OOS Time-valid statistical
test
Incremental prediction after a declared
historical split
Portfolio value, costs and capacity
GROSS Gross portfolio simu-
lation
Historical decision value under stated
weights and constraints
Implementable net performance
NET Net, risk-adjusted
simulation
Simulated alpha under disclosed cost,
financing and execution models
Prospective robustness and unmodeled costs
PROSP Precommitted paper
or shadow portfolio
Resistance to hindsight and changing model
selection
Real fills, operational loss and live-capital
behavior
LIVE Audited live-capital
record
Orders, fills, costs and controls for the
observed size and period
Causality, future persistence and larger
capacity
EXT Independent cross-
regime/capacity
study
A bounded sustainability claim for specified
settings
A guarantee under future competition or
structural change
These dimensions are not interchangeable. A live record can have strong operational provenance
but weak selection control; a carefully designed historical study can isolate a mechanism while
saying little about capacity or future persistence. Table 1 therefore lists recurring evaluation-design
archetypes, not ranked levels. The codes identify the dominant evidence object and do not imply a
total ordering. A task benchmark becomes evidence about net, prospective or live profitability only
when the corresponding dimensions are separately documented.
Three distinctions deserve emphasis. First, “out of sample” is not synonymous with point-in-time.
A test observation can be held out while the input database contains later revisions, the universe
contains future survivors, or the pretrained LLM remembers events from its corpus. The appropriate
condition is
It∩Ft+1 =∅,(3)
whereFt+1 denotes information observable only after the decision. This must hold for feature
values, timestamps, membership, preprocessing estimates, prompt examples and model parameters.
The correction documented by Zhang et al. (2025) illustrates the stakes: a reported ML return
advantage can vanish when predictors are aligned to their actual availability.
Second, a cost deduction is a model, not a stamp of realism. Linear costs may approximate
commissions and spread at small size; impact is nonlinear and depends on volatility, liquidity,
urgency and participation. If target holdings areqt and the strategy trades∆qt, then writing
Ct =k|∆qt| silently assumes away much of the capacity problem. Jensen et al. (2026) show that
cost-unaware return predictors can favor fleeting, low-scale opportunities and produce unattractive
implementable frontiers, whereas learning the portfolio with trading costs inside the objective
changes which information is valuable. The result is more than “subtract a higher fee.” Economic
constraints alter the optimal representation and decision rule.
Third, a statistically significant alpha is not necessarily decision-relevant. Investors care about
expected utility, drawdown, tail exposure, funding stability and the covariance of a strategy with
the rest of their wealth. Mean–variance choice remains a useful abstraction (Markowitz, 1952),
but estimated means are noisy and optimized portfolios are unstable. The long-standing difficulty
of beating simple1/N diversification out of sample (DeMiguel et al., 2009) is a warning against
7

adding an elaborate optimization layer without measuring estimation error. AI can reduce some
approximation error while increasing selection error and opacity.
3.3 A decomposition of the central verdict
The central verdict follows from a mismatch between the location of progress and the location
of decisive evidence in the reviewed record. Most documented public advances are upstream:
representation learning, scalable prediction, text extraction, workflow integration and historical
policy optimization. The most demanding profitability claims are downstream: timestamped
commitment, real execution, complete costs, meaningful risk adjustment, capacity and persistence.
This is why the review can affirm material changes in the investment practices examined while
concluding that the reviewed public evidence does not establish a general profit engine.
The verdict is also conditional on disclosure. Proprietary firms may possess better data,
engineering and live evidence than they publish. Public insufficiency is not evidence of private
absence. But unpublished performance cannot validate public architectural claims, and selective
disclosure creates its own inference problem. A scientific claim must be supported by inspectable
evidence at the level claimed. The practical response is not to demand that every study operate a
fund. It is to report the full evidence profile and design the next evaluation around the dimensions
that remain unresolved.
4 Prediction and Representation: Real Progress, Conditional Eco-
nomic Value
4.1 From linear characteristics to nonlinear cross-sectional models
The strongest case that ML has changed empirical investing comes from large, structured equity
panels. Traditional predictive regressions impose a small set of linear effects because expected returns
are noisy and the number of candidate interactions grows rapidly. Regularization, trees, boosting
and neural networks relax this restriction while controlling complexity. In a broad US sample, Gu
et al. (2020) compare multiple ML methods using firm characteristics and macroeconomic variables.
Trees and neural networks improve out-of-sample prediction and portfolio performance relative to
standard linear benchmarks; the result also shows that relatively shallow architectures can be better
suited to financial data’s low signal-to-noise ratio than indiscriminately deeper networks. Chen
et al. (2024) use a deep stochastic-discount-factor framework that joins no-arbitrage restrictions,
macroeconomic state and firm characteristics. Here, economic structure is not decoration after
prediction: it shapes the learning problem.
These studies establish that nonlinearities and high-dimensional interactions contain information
under their protocols. They do not establish universal alpha. Their historical universes, rebalancing
rules and institutional assumptions define a particular opportunity set. Cross-sectional predictability
may compensate investors for risk, reflect mispricing, or combine both, and a factor-model intercept
depends on which risks the model recognizes. Moreover, portfolio sorts amplify small statistical
differences and can concentrate exposure in illiquid stocks. In the profile of Table 1, their support is
strongest on time-valid historical prediction and disclosed portfolio simulations; prospective, capacity
and live-operation dimensions remain open.
Replication evidence further resists a simple story. The multiple-testing analysis of Harvey et al.
(2016) implies that conventional significance thresholds are too permissive when researchers search
hundreds of candidate factors. Hou et al. (2020) find that many published anomalies fail to replicate
under their procedures. Yet Chen and Zimmermann (2022) reproduce most signals in a transparent,
8

standardized library, while Jensen et al. (2023) document a broad global cross section. The lesson
for AI is not that characteristics are either “real” or “dead.” Feature definition, accounting lag,
microcap treatment, weighting, exchanges, sample end and statistical threshold are part of the
model. A neural network trained on a disputed panel can fit the disagreement rather than resolve it.
The time dimension adds another challenge. Welch and Goyal (2008) show how equity-premium
predictors that fit in sample can fail out of sample, and Goyal et al. (2024) document substantial
deterioration in a long update of predictive variables. McLean and Pontiff (2016) report lower
returns after sample end and especially after academic publication, consistent with both statistical
overfit and trading that attenuates mispricing. Thus a predictive relationship can be genuine
in the discovery sample and still be a poor forecast of future strategy profitability. AI expands
the hypothesis space and accelerates discovery, which increases both the chance of finding useful
nonlinear structure and the burden of controlling selection.
4.2 Deep learning and economically structured policies
DL contributes in three different ways that should not be conflated. Representation models compress
high-dimensional prices, characteristics or text; prediction models estimate conditional returns, risks
or state transitions; decision models output positions or execution actions. Most reported gains
occur in one of these roles, and the downstream evidence depends on the others.
The promise of deep representation is greatest where interactions are numerous and economically
constrained data are sufficiently broad. Asset-pricing networks can enforce a pricing equation,
attend across firms or learn latent states instead of treating observations as independent rows. But
financial depth has a different meaning from depth in computer vision: samples are correlated,
regimes change, and an additional decade provides only a small number of independent crises. Model
size is not an adequate proxy for effective sample size. Large parameter counts can be defensible
when pretraining transfers stable structure or when cross-sectional breadth is informative; they can
also create a large, weakly observed search space.
Decision-focused work addresses a more consequential limitation: minimizing forecast error need
not maximize investor welfare. Simon et al. (2026) estimate parametric portfolio policies that map
characteristics to holdings under an investor objective, reporting higher historical out-of-sample
certainty-equivalent returns than linear policies across their setting and robustness exercises. Jensen
et al. (2026) formulate ML around the implementable efficient frontier. Their comparison is revealing:
standard prediction-oriented ML extracts signals that can appear valuable gross but trade poorly
after costs, particularly when opportunities are fleeting and low scale; directly cost-aware learning
changes both portfolio composition and the attainable frontier. These results support a design
principle—train for the decision actually made—rather than a claim that one neural architecture
dominates all markets.
Direct objectives introduce their own specification risk. A policy trained to maximize an
estimated Sharpe ratio can exploit volatility estimates, boundary constraints or leverage conventions.
A drawdown penalty encodes a horizon and path dependence that may not match investor liabilities.
Transaction costs calibrated from a representative account can be wrong for another scale. Economic
training therefore moves assumptions inside the loss function; it does not eliminate them. Robust
evaluation must perturb risk aversion, financing, cost curves, turnover limits, short availability and
execution delay, and it should report which performance survives rather than selecting the most
favourable preference.
9

4.3 Time-series foundation models
TSFMs extend pretraining and zero-shot transfer to numerical sequences. TimesFM is pretrained on
a large time-series corpus and reports competitive zero-shot forecasting across general benchmarks
(Das et al., 2024). Moirai is trained on the LOTSA collection, spanning many domains, frequencies
and variable dimensions, and is evaluated as a universal forecaster (Woo et al., 2024). Chronos
tokenizes numerical values and uses language-model-style training for probabilistic forecasting
(Ansari et al., 2024). Time-MoE scales a mixture-of-experts time-series model and reports strong
general forecasting performance (Shi et al., 2025). These are substantial engineering and statistical
advances: a common pretrained model can provide usable forecasts without fitting a separate
architecture from scratch for every dataset.
Their direct profitability evidence is much weaker. General time-series benchmarks are designed
around forecasting loss, not tradable excess return. Asset prices are close to nonstationary, economic
value often lies in a small conditional mean relative to volatility, and a lower mean absolute error
can result from better level or seasonal prediction without improving the sign, timing or capacity
of a trade. A universal model can forecast realized volatility well and still require a separate
risk-allocation thesis. Conversely, it may be economically useful even when directional-return
accuracy is unchanged, because better uncertainty or covariance forecasts can improve sizing. The
model’s role must be stated before its benchmark metric is interpreted.
Two finance-specific preprints available by the cutoff sharpen this mixed result without turning
forecast accuracy into trading profit. In rolling-origin tests on five liquid US equities, Alonso and
Franklin (2026) find that pretrained TSFMs take eight of ten task-level wins, yet improvements
over a random-walk benchmark are small and sparse, with statistically significant gains in only
two model–asset comparisons. FinVerse broadens the measurement substrate to 116,897 financial
series and compares 43 public foundation models across domain-aligned metrics; its authors find
that strong generic forecasting ranks need not translate into useful financial forecasts (Lee et al.,
2026). Both are author-run preprints. Neither supplies a portfolio with execution costs, capacity, or
live-capital returns.
There is also a caution against assuming that a large pretrained language backbone is intrinsically
useful for numerical forecasting. Tan et al. (2024) systematically ablate several LLM-based time-
series methods and find that removing or replacing the LLM component can preserve or improve
performance, while claimed few-shot benefits do not reliably appear in their tests. This is not a
refutation of time-series pretraining: TimesFM, Moirai and Chronos are trained around numerical
sequences rather than relying on semantic language knowledge. It is evidence that transfer must
be demonstrated against smaller, time-series-specific and non-pretrained baselines under equal
information and tuning budgets.
Financial application raises a further point-in-time issue. A generic TSFM may have been trained
on historical series extending into the intended test period. Unlike a text model that can sometimes
disclose a corpus date, numerical pretraining sets may contain transformed or duplicated benchmark
sequences whose provenance is difficult to audit. A defensible investment experiment needs a model
checkpoint whose entire training data ends before the trading period, or a contamination test strong
enough to bound the overlap. Fine-tuning only on a pre-cutoff slice does not remove information
already encoded in the base model.
4.4 What predictive metrics reveal—and conceal
Table 2 summarizes the main method families by their demonstrated contribution and their
characteristic translation failure. It is not a ranking: studies inside each family vary widely, and the
10

Table 2: Method families viewed through the alpha-translation chain. “Progress” denotes an
evidence-backed technical contribution, not a general profitability finding.
Family Demonstrated progress Principal economic
opportunity
Characteristic evidence gap
Regularized
ML, trees,
boosting
Nonlinear and
high-dimensional return
prediction in large panels
Ranking and interaction
discovery
Multiple testing, unstable
features, liquidity
concentration
Deep asset-
pricing models
Joint representation and
economic restrictions
Latent states, nonlinear
stochastic discount factors
Effective sample size,
interpretation, historical
dependence
TSFMs Zero-shot and cross-domain
forecast transfer
Fast adaptation, risk and
covariance inputs
Generic loss is not alpha;
pretraining contamination
Financial
NLP/LLMs
Scalable extraction and
semantic event processing
Timely news, filing and
expectation signals
Memorization,
timestamping, prompt
selection, source provenance
RL and direct
policies
Sequential or
decision-aligned objectives
Turnover, constraints and
dynamic risk inside learning
Simulator error, reward
hacking, fragile policy
transfer
LLM agents Integration of retrieval,
memory, reasoning and tools
End-to-end research and
operational coordination
Component attribution,
reproducibility, cost and live
validation
table records the strongest defensible generalization rather than the largest reported return.
PredictiveR2, classification accuracy and information coefficients are useful diagnostic quantities.
They reveal whether a model adds conditional information and where. They conceal the portfolio’s
nonlinear exposure to tails, the covariance among simultaneous signals, trading required to realize a
forecast, and the value of abstention. A small, stable rank correlation in liquid securities can be
more valuable than high accuracy in rare or untradeable cases. An apparent directional hit rate can
be produced by market drift. Calibration matters when position size depends on confidence; ranking
may matter when only a fixed long–short book is feasible. No single predictive metric dominates
without an explicit decision problem.
The best reading of this literature is therefore two-sided. It is no longer credible to claim that
only linear models can extract useful information from financial data. It is equally unsupported
to infer from upstream benchmark gains that general pretrained models have solved investing.
Prediction is a valuable and increasingly transferable component. Its economic value is conditional
on temporal provenance, stable incremental information and a downstream policy that survives risk
and execution.
5 Text, Multimodality, and Agents as an Integration Layer
5.1 Text can contain return-relevant information
Financial text is an unusually plausible domain for AI because prices respond to information that is
not naturally represented as a fixed numerical panel. Early work established both the opportunity
and the domain problem. Tetlock (2007) links pessimistic media content to market activity and
subsequent return dynamics. Loughran and McDonald (2011) shows that general-purpose sentiment
dictionaries misclassify financially meaningful language, motivating domain-specific vocabularies.
Supervised methods can learn a return-predictive text representation rather than treating sentiment
11

as a universal label; Ke et al. (2019), for example, construct a text-based signal aligned with
return prediction. These studies precede generative LLMs but remain conceptually important: the
economic label, release time and audience expectation matter more than fluent language generation.
Modern financial language models expand scale and task coverage. BloombergGPT demonstrates
finance-intensive pretraining across financial and general corpora (Wu et al., 2023); FinGPT proposes
an open-source ecosystem for adapting language models to financial data and tasks (Yang et al.,
2023). Fine-tuned models classify news, extract entities and relations, summarize filings, answer
questions and generate research. Multimodal systems can add price patterns, tables, charts or audio
transcripts. These capabilities lower the cost of converting heterogeneous disclosure into structured
features. They can also improve analyst productivity without making any trade, a benefit that
should be measured through time saved, coverage, error rates and decision quality rather than recast
as alpha.
The strongest recent profitability-related LLM evidence comes from designs that respect event
time. Using news headlines after the model’s training-data cutoff, Lopez-Lira and Tang (2026) find
that GPT classifications are informative about subsequent stock-price movements, especially around
smaller firms and negative news. The design helps separate semantic processing from historical
recall, and the paper documents that predictability weakens as use of the technology spreads. The
interpretation requires care: classifying the market’s immediate reaction is not a trade available
before that reaction, whereas subsequent drift is potentially actionable subject to release timestamps,
latency, costs and capacity. The result is evidence that an LLM can extract economically relevant
event information, not that an off-the-shelf chat interface supplies a permanent strategy.
Two lines of work clarify temporal validity. Lopez-Lira et al. (2026) show that LLMs can recall
financial values and events from their pretraining period, and that masking obvious identifiers is not
a sufficient defence. An apparently prescient historical narrative can therefore be retrieval from
parameters. Kelly et al. (2026) train a sequence of point-in-time language-model checkpoints with
information cutoffs, enabling historical tests without using a model trained on later text. Their
evidence suggests that point-in-time representations retain useful financial information and can
approach the apparent performance of contaminated alternatives in selected tests. The broader
lesson is constructive: contamination is not a reason to abandon LLM research, but a reason
to version the base model, retrieval corpus, prompt, tool data and evaluation period as a single
time-indexed object.
5.2 Why multimodality helps and complicates identification
An investor rarely observes one modality in isolation. Earnings news is interpreted relative to
prior guidance, estimates, prices, options and macro conditions; an on-chain transfer may mean
something different depending on exchange flows and perpetual positioning. Multimodal models
can represent these interactions without forcing every source into a handcrafted scalar. FinAgent
combines textual and market information with tools in a generalist trading agent (Zhang et al.,
2024); CryptoTrade combines on-chain and off-chain evidence with reflection for cryptocurrency
decisions (Li et al., 2024). Such systems illustrate a useful direction: information fusion is aligned
with the actual analyst problem.
Yet adding modalities increases the number of timestamps, revisions and missingness mechanisms
that must be correct. A news database may record ingestion rather than first public release.
Fundamental values may be backfilled. A chart image can encode future axes or annotations.
Blockchain state is timestamped but may not be final at the moment a transaction is signed. If a
multimodal ablation removes an entire feed, it may reveal that the feed matters but not whether
the model fused it intelligently; a simpler late-fusion baseline or decision rule may capture the
12

same value. Comparisons should hold the information set, latency and search budget fixed before
attributing performance to architectural integration.
5.3 Agentic systems: architectural closure before evidentiary closure
LLM agents shift the unit of design from a single prediction to a repeated workflow. A typical system
retrieves news and fundamentals, maintains episodic or hierarchical memory, assigns specialized
analyst roles, debates opposing theses, calls quantitative tools, generates a position and revisits the
decision after outcomes. FinMem emphasizes layered memory and character design (Yu et al., 2023);
FinCon uses multiple agents and verbal reinforcement (Yu et al., 2024); TradingAgents organizes
analyst, researcher, trader, risk and portfolio roles in a multi-agent framework (Xiao et al., 2024);
and FinAgent combines multimodal observations and tool use (Zhang et al., 2024). These projects
are important because they make the research-to-action boundary explicit. They are also difficult
to evaluate: an end-to-end return mixes information sources, base-model knowledge, prompts, role
decomposition, tools, risk rules and random generation.
An agent is therefore an integration layer, not a new asset-pricing law. Debate can reduce
one-sided reasoning, but correlated agents using the same base model may create verbose agreement
rather than independent evidence. Memory can preserve a thesis, but can also anchor the system
to a past regime. Reflection can update behavior, but evaluating on the same outcomes used for
reflection converts the test into training. Tool use can improve arithmetic and access fresh data;
it can also enlarge the prompt-injection, credential and erroneous-order surface. The appropriate
baselines include a single agent with the same model and tools, deterministic rules using the same
signals, equal token and data budgets, and ablations that preserve timestamps.
Benchmark design is beginning to strengthen the temporality and operational-provenance
dimensions of the evidence profile. StockBench emphasizes real-world stock trading evaluation
across a temporally structured setting (Chen et al., 2025); Agent Trading Arena studies numerical
understanding and trading behavior in a controlled arena (Ma et al., 2025); DeepFund commits
fund recommendations in real time to prevent retrospective “time travel” (Li et al., 2025); and
Agent Market Arena evaluates agents in a live, multi-market setting (Qian et al., 2026). These
efforts improve prospective validity and comparability. A live feed or paper arena still differs from
audited live-capital execution, however, and short evaluation windows can be dominated by market
beta, style exposures or a few events. The research frontier is less about adding roles than about
longer timestamped evaluation, complete holdings and fill logs, predeclared model updates, and
uncertainty that reflects both market and agent stochasticity.
A contemporaneous agentic-quantitative-trading survey reaches a compatible diagnosis: cur-
rent systems remain concentrated on signal discovery, while complete integration with portfolio
construction, execution and risk control is uncommon (Hua et al., 2026). A separate audit-oriented
preprint maps 77 studies but identifies only 19 with both action output and closed-loop evaluation;
within that subset it reports two time-consistent splits, one explicit transaction-cost model, one
documented universe or survivorship treatment, and no fully replayable R3 record (Xia et al., 2026).
These author-coded counts diagnose protocol and reporting gaps, not the profitability of every
agentic system. Our broader market-wide synthesis uses both surveys as context rather than as
return evidence.
Table 3 locates representative systems and official interfaces by what they demonstrate. Academic
papers are evidence for their reported experiment; official product documentation is evidence that a
capability is offered. Neither category is silently upgraded to durable profitability evidence.
13

Table 3: Representative agentic integration systems and interfaces. The table describes the principal
evidenced contribution, not a performance ranking.
System/source Market em-
phasis
Integration contribution Profitability boundary
FinMem (Yu
et al., 2023)
Equities Layered memory and reflective trading
workflow
Retrospective experiments; memory benefit
is conditional on protocol
FinAgent (Zhang
et al., 2024)
Equities Multimodal observations, tools and
generalist agent
Historical evaluation, not independent
live-capital persistence
FinCon (Yu
et al., 2024)
Equities/
other tasks
Multi-agent roles and conceptual verbal
reinforcement
Reported backtests do not isolate a general
alpha mechanism
TradingAgents
(Xiao et al.,
2024)
Selected US
equities
Analyst debate, trader and risk/portfolio
roles
Short historical test on selected stocks;
architecture is not durable-alpha proof
StockBench
(Chen et al.,
2025)
Equities Time-structured benchmark for LLM-agent
trading
Benchmark outcome remains model-,
window- and cost-specific
Agent Trad-
ing/Market
Arenas (Ma
et al., 2025; Qian
et al., 2026)
Controlled
and multi-
market
Comparative numerical behavior and
live-market evaluation
Prospective arenas improve validity but
need longer, fill-aware, risk-adjusted records
CryptoTrade (Li
et al., 2024)
Crypto spot On-chain/off-chain fusion and reflection Beats selected learned baselines; does not
establish superiority to all traditional signals
DSA (Zhu and
Shi, 2026)
Multi-
market
stocks
Evidence-aware research orchestration and
report support
Research/report generation; conformance
evidence only, with no report-quality,
forecast, return, or execution result
Robinhood, Al-
paca, Coinbase
(Robinhood Mar-
kets, 2026a; Al-
paca, 2026; Coin-
base Developer
Platform, 2024)
Brokerage
and crypto
execution
Agent-facing research, account and
order/wallet tools with stated controls
First-party capability claims; no
independent evidence of alpha
5.4 Brokerage and on-chain tools change the risk boundary
The release of agent-facing trading interfaces makes the distinction between reasoning and authority
operationally urgent. Robinhood’s official material distinguishes the earlier Cortex research product
from an Agentic Trading account whose documented interface can expose account data and order
placement under account-specific permissions (Robinhood Markets, 2025, 2026a,c). In a July 2026
SEC exhibit, Robinhood reported nearly 100,000 opened Agentic Trading accounts and more than
USD 100 million in assets under custody (Robinhood Markets, 2026b). Those are company-reported
adoption figures, not counts of active or profitable accounts, evidence of safe use, or an independent
audit. Alpaca’s official Model Context Protocol server exposes market and account operations,
including order-related endpoints; its documentation recommends paper testing and warns of
unintended orders, slippage and limits (Alpaca, 2025, 2026). Coinbase AgentKit provides wallet
and blockchain actions for agents (Coinbase Developer Platform, 2024). These products lower
integration cost. They do not show that an agent selects good trades.
Tool access, delegated authority and investment skill are separate variables. A read-only research
agent may create reputational or confidentiality risk but cannot place an order. An order-capable
agent can create immediate market and credit exposure even when its forecast is unchanged. Controls
should therefore be attached to authority: allow-listed instruments and venues, maximum notional
and leverage, price collars, stale-data rejection, rate limits, transaction simulation, human approval
above thresholds, independent position reconciliation and a kill switch outside the model’s control.
Smart-contract calls additionally require chain, contract and token allow-lists, allowance limits, gas
14

bounds and protection against malicious tool output. The successful demonstration of a buy order
is CAP-type operational evidence and a governance event, not a profitability experiment.
Agents may ultimately be most valuable as disciplined coordinators: they can keep evidence and
counterarguments visible, call deterministic calculators, enforce a checklist, and document why a
decision changed. That value is credible only if provenance survives generation. Every consequential
statement should link to a dated source or computed object; each tool result should carry a
timestamp; and the final action should be reproducible from logged inputs, versions and policy
constraints. Fluent rationales generated after an action are not provenance. The frontier is thus an
auditable hybrid: learned components for extraction and adaptation, deterministic components for
accounting and limits, and explicit human or institutional responsibility for delegated risk.
6 Portfolio Learning, Reinforcement Learning, and Risk
6.1 The portfolio is where weak assumptions become positions
Prediction papers often postpone the portfolio problem by forming equal-weighted quantiles. That
convention is transparent, but a deployed investor must choose exposure, covariance risk, turnover,
financing and abstention jointly. Mean–variance optimization formalizes the trade-off between
expected return and variance (Markowitz, 1952); in practice, expected returns are estimated so
imprecisely that unconstrained optimized weights can be extreme. The out-of-sample strength of
simple diversification documented by DeMiguel et al. (2009) remains a relevant baseline for AI. A
complicated allocator should be compared not only with another learned model but with equal
weight, volatility scaling, a market portfolio, a low-turnover characteristic strategy and a no-trade
policy.
End-to-end portfolio learning attempts to optimize what investors value rather than the error of
an intermediate forecast. Direct policies can learn nonlinear mappings from features to weights, and
risk aversion can regularize those mappings economically (Simon et al., 2026). AlphaPortfolio uses
a deep RL formulation for dynamic portfolio optimization and reports large historical out-of-sample
risk-adjusted performance under its protocol (Cong et al., 2026). Such results are affirmative
evidence that economic losses and sequential decisions can change the frontier. They remain
historical evidence: the strategy’s attainable return depends on the chosen asset universe, action
interval, transaction-cost curve, state variables and constraints, as well as whether the research
search that produced the architecture is counted in uncertainty.
Cost-aware portfolio learning is especially important because signal value depends on how slowly
it decays. A small persistent signal can support a large, patient position; a stronger one-step forecast
may be consumed by spread and impact. Jensen et al. (2026) make this interaction explicit by
learning the implementable efficient frontier rather than attaching costs to a preselected forecast.
Related portfolio-combination work shows that combining predictors can cancel offsetting trades
and improve implementability (DeMiguel et al., 2020). The general principle is that turnover is not
merely an evaluation statistic. It is a state variable and design constraint.
6.2 What RL adds
RL is appropriate when current actions change future states or opportunities: inventory affects later
execution, trading changes transaction costs and tax lots, leverage changes liquidation risk, and
an order can reveal information. A policyπ(at|s t)is trained to maximize expected discounted or
finite-horizon reward,
15

J(π) =E π
[ T∑
t=0
γtu ( Rnet p,t,xt )] ,(4)
where xt may include drawdown, inventory or funding state. Early recurrent reinforcement
learning directly optimized a risk-adjusted trading objective (Moody and Saffell, 2001). Later
work applies deep RL to allocation and execution; FinRL-Meta and TradeMaster package datasets,
environments, baselines and evaluation tools intended to improve reproducibility (Liu et al., 2022a;
Sun et al., 2023). These infrastructures are meaningful progress because inconsistent data preparation
and environments can dominate algorithm comparisons.
RL also magnifies the simulation problem. Historical markets do not reveal the counterfactual
prices and queues that would have followed a different large action. A backtest environment
commonly assumes that the agent is a price taker, fills at the next bar, and observes a Markov state
assembled from historical variables. Under those assumptions an algorithm can learn simulator
shortcuts: trading at a bar price unavailable in real time, exploiting a reward normalization fitted
with future data, or using turnover patterns that would alter impact. A policy’s repeated interaction
with a fixed historical tape is not interactive market evidence.
Crypto provides instructive negative as well as positive results. The recurrent RL crypto agent
of Borrageiro et al. (2022) reports a systematic framework for crypto trading, whereas a PPO
study of BTC/USDT minute data reports failure to outperform buy-and-hold under its experiment
(Mahayana et al., 2022). The contrast is healthier than a leaderboard: performance depends
on period, benchmark, action space, reward and cost model. Buy-and-hold is itself a high-beta,
regime-dependent comparator, so beating or failing to beat it does not identify alpha. Crypto RL
should additionally compare volatility-matched exposure, cash, momentum or carry baselines and
state whether funding and liquidation are modeled.
6.3 Risk is not a penalty appended at the end
Many AI systems represent risk as one scalar penalty. Real portfolio risk is multidimensional:
market and factor exposure, concentration, correlation, drawdown, liquidity, short squeeze, borrow
recall, counterparty, custody, stablecoin, smart-contract and operational risk. A variance penalty
treats upside and downside symmetrically and can miss liquidation discontinuities. A drawdown
constraint is path-dependent. Value-at-risk or expected shortfall depends on tail estimation precisely
where data are sparse and regimes change. Risk models should therefore be stress-tested as models,
not treated as ground truth.
Risk also determines whether a return is interpretable. A long-only agent evaluated during a
bull market can earn positive return through beta while adding no security-selection value. A crypto
policy can earn a high nominal return by loading on market direction, small tokens or short-volatility
carry. Appropriate reporting includes gross and net return, volatility, drawdown, turnover, leverage,
average and peak concentration, beta and factor alpha where meaningful, tail loss, and exposure
to the venue-specific cash flows discussed in Section 7. Confidence intervals should respect time
dependence; repeated runs are required when generated decisions or RL training are stochastic.
Distribution shift is not one generic robustness test. A policy can face covariate shift in features,
label shift in return distribution, a new market mechanism, missing vendors, a changed fee tier, an
asset delisting or an adversarial text source. Training with historical perturbations may improve
resilience but can also create false comfort if stress scenarios omit the actual discontinuity. A robust
deployment separates monitored assumptions from learned flexibility: hard limits remain outside
the policy; state drift and performance attribution trigger review; model updates are staged through
shadow operation; and rollback does not require the failing model to cooperate.
16

6.4 Execution as a sequential decision problem
Executionisonedomainwheresequentiallearninghasanaturaltarget: buyorsellarequiredquantity
while balancing price risk and market impact. Classical optimal execution already formalizes this
trade-off (Almgren and Chriss, 2001), and market-impact theory explains why private information
and order flow affect prices (Kyle, 1985). RL can adapt order placement to book state and partial
fills; Nevmyvaka et al. (2006) provide an early empirical application to optimized trade execution.
The relevant benchmark is an execution schedule with the same parent order and information, not
the portfolio return created by the upstream signal.
Execution evaluation should report implementation shortfall against a predeclared arrival
or decision price, fill probability, adverse selection, latency, rejected orders and tail outcomes.
Training and testing on messages from one venue can overfit queue priority and fee rules. A policy
that improves average shortfall but occasionally fails to complete a risk-reducing order may be
unacceptable. Thus even in a domain where RL’s sequential advantage is credible, optimization
requires hard completion, credit and price controls.
The synthesis is that portfolio and RL methods address real weaknesses of forecast-first investing.
They can internalize constraints, dynamic costs and risk, and strong historical results justify further
research. They also relocate model risk into the objective, simulator and constraint set. A decision-
aligned loss is better than a proxy only when the decision environment is time-valid and economically
faithful.
7 Market Structure and the Meaning of Profitable Prediction
7.1 Listed equities and ETFs
Equities provide the deepest public record for ML asset pricing: long return histories, standardized
accounting variables, regulated corporate disclosures and established factor benchmarks. They also
contain traps that a model can exploit. Delisted firms and delisting returns must be represented to
avoid survivorship bias (Shumway, 1997); accounting and index data must be lagged to publication;
corporate actions alter prices and shares; and historical constituents cannot be reconstructed from
today’s membership. Intraday execution occurs in fragmented, scheduled markets with auctions,
halts, tick sizes and venue routing. Short positions require locate and borrow, while an ETF adds
fund-specific spreads, premiums/discounts and creation/redemption mechanics.
Equity capacity is highly cross-sectional. A strategy whose predictive power is concentrated in
microcaps can show strong equal-weighted returns while supporting little capital. Value-weighting
is not a complete solution because it changes the question; it can conceal whether a model has
incremental information away from mega-cap beta. Studies should report performance by liquidity
and market-cap segment, participation-rate sensitivity and the contribution of the smallest securities.
Trading-cost evidence should be read conditionally: high turnover can destroy anomaly profits
(Novy-Marx and Velikov, 2016), yet actual institutional records show that some systematic styles
remain scalable at meaningful size (Frazzini et al., 2018). The cost model must match the strategy
and investor.
ETFs can reduce the security-selection and execution burden for macro or allocation agents. They
offer liquid, diversified exposures and can make a generated sector or asset-class view implementable
without hundreds of individual orders. But they also make benchmark discipline essential. Rotating
among equity ETFs may largely time market beta, duration, size or geography; risk-adjusted value
should be measured against a feasible static or volatility-managed allocation. Leveraged and inverse
ETFs have path-dependent daily objectives, so a model that treats their ticker return as a scaled
17

index return across longer horizons is misspecified.
7.2 Centralized crypto spot
Centralized crypto spot markets operate continuously across venues and quote currencies. They
offer rapid data generation, public blockchain covariates and a large natural experiment in market
fragmentation. Return studies find that momentum and investor attention predict cryptocurrency
returns (Liu and Tsyvinski, 2021), and a factor structure involving market, size and momentum
explains a substantial part of the cross section (Liu et al., 2022b). Persistent cross-exchange
price differences documented by Makarov and Schoar (2020) show that limits to arbitrage can be
economically important. These findings support the existence of structured signals and frictions;
they do not imply riskless machine-extractable profit.
Crypto data are abundant but not automatically clean. Token histories are short and universes
change through listings, delistings, forks, migrations and failures. A dataset assembled from surviving
API symbols can omit precisely the assets that went to zero. Reported volume may be strategic
rather than organic. Cong et al. (2023) find extensive wash trading across less regulated exchanges,
and Aloosh and Li (2024) provide direct evidence of wash trading in Bitcoin markets. A model
trained on volume, order flow or social attention can learn venue manipulation as if it were investor
demand. This may remain locally predictive, but it changes both interpretation and the risk that
the behavior disappears after enforcement or venue redesign.
Centralized custody and counterparty exposure are part of net performance. An apparent
arbitragecanrequireprefundedbalancesonseveralvenues, exposingcapitaltodefaultandwithdrawal
risk. Settlement delays and transfer limits prevent instantaneous convergence. Stablecoin quote
assets introduce issuer and peg exposure. AI does not diversify these risks simply by monitoring
more feeds; a portfolio layer must constrain venue and settlement concentration, and performance
should charge capital tied up to make execution possible.
7.3 Perpetual futures are not spot with leverage
Perpetual futures have no fixed expiry and use funding or analogous transfers to keep the contract
near an index. For positionqt, a simplified holding-period P&L is
PnLt,t+1 =q t(Pt+1−Pt)−q tPtft−Ct−LiqLosst,t+1,(5)
whereft is the funding rate paid by a long when positive,Ct covers trading costs, and liquidation
loss is discontinuous rather than a small linear fee. Venue rules use index and mark prices,
maintenance margin, insurance funds and auto-deleveraging mechanisms. A backtest based only on
last-traded prices can therefore report a path that the margined account could not survive.
Crypto carry can be large precisely because it is not a free yield. Schmeling et al. (2026)
document substantial variation in crypto futures carry and connect high carry to scarce arbitrage
capital, leverage constraints and crash risk. Earlier work on Bitcoin derivatives similarly highlights
venue-specific pricing and microstructure (Alexander et al., 2020). A strategy that earns funding
by taking the other side of leveraged demand is exposed to basis moves, margin, exchange and
tail risk; a directional agent that ignores funding can be right about spot direction and wrong
about contract P&L. Evaluation needs contract-level funding timestamps, mark-price liquidation
simulation, collateral currency, leverage, margin mode, fee tier and downtime.
Perpetual datasets also create subtle leakage. A current contract specification may be applied
to an earlier period with different funding intervals or limits. Continuous series can cross listing
changes. The set of tradable tokens can be reconstructed using future liquidity. Liquidation labels
18

Table 4: Market strata require different P&L and validity fields. Items in the final column are
minimum additions to ordinary return reporting.
Stratum Distinct information/data risk Distinct implementation loss Minimum economic validation
Listed equi-
ties/ETFs
Publication lags, revisions,
constituent and delisting bias,
corporate actions
Spread, impact, commission,
borrow, auction/halts; ETF
premium and path dependence
Liquidity/capacity slices, borrow
and turnover, factor alpha,
corporate-action-correct universe
Centralized
crypto spot
Changing token/venue universe,
wash volume, forks, quote-asset
and API revisions
Fragmented fills, custody,
prefunding, withdrawal and
stablecoin risk
Venue-level executable prices,
survival-free universe,
custody/capital charge,
manipulation sensitivity
Perpetual fu-
tures
Historical contract specifications,
index/mark construction,
changing funding rules
Funding, leverage, margin,
liquidation,
insurance/auto-deleveraging
Contract-level funding and
mark-price path, collateral and
margin rules, tail liquidation tests
On-chain/DEX State at signing versus inclusion,
address labels, reorg/finality,
adversarial activity
Gas/priority fees, slippage, failed
calls, MEV, LVR, smart-contract
loss
Ordered transaction simulation,
all failed/successful gas,
rebalancing benchmark,
contract/allowance controls
derived from later-reported data can leak the event. A point-in-time contract master is as necessary
as point-in-time fundamentals in equities.
7.4 On-chain markets: transparent state, endogenous extraction
Blockchain settlement makes balances, contract calls and transaction ordering visible, enabling
features that centralized markets cannot expose. An agent can observe liquidity-pool state, flows
between addresses, protocol positions and composable prices. The same transparency creates a
competitive execution game. Pending or public transactions can be reordered or surrounded; users
bid gas or priority fees; failed transactions consume resources; and contract state can change between
simulation and inclusion. MEV is therefore not an operational footnote but a claimant on gross
surplus.
AMMs replace or complement limit-order books with programmed liquidity. Liquidity providers
earn fees while bearing inventory and adverse-selection losses. Loss-versus-rebalancing (LVR)
formalizes the loss relative to an appropriate rebalancing benchmark (Milionis et al., 2022). Empirical
work finds that arbitrage-related losses can exceed fee income in many large Uniswap pools (Fritsch
and Canidio, 2024). Capponi and Jia (2025) show how arbitrage competition can transfer much
of the surplus into gas and infrastructure expenditure, while Capponi et al. (2026) link fees and
ordering behavior to price discovery. A model that predicts the next pool price can therefore be
statistically excellent while failing to capture any surplus after priority competition.
For a swap of intended sizex, executable output is a function of reserves at inclusion, fee tier,
price impact and ordering, not simply the contemporaneous mid-price. For liquidity provision, the
benchmark is not token buy-and-hold alone; fee income must be compared with rebalancing, hedging,
gas and adverse selection. Smart-contract risk, oracle failure, bridge exposure and governance
changes are additional state transitions. Backtests need block-level ordering assumptions, gas and
failed-call accounting, realistic slippage bounds and a policy for reorg or finality. “On-chain” means
observable after settlement, not necessarily known before a decision.
7.5 A market-specific evaluation matrix
Table 4 prevents a common category error: applying one return equation and one cost scalar to
all markets. Shared requirements include point-in-time universes, executable benchmarks, risk
adjustment and capacity. The marginal cash flows and failure events differ.
19

The matrix also explains why crypto warrants explicit treatment within a common validation
framework rather than peripheral mention. It is not merely a volatile additional asset class on which
to rerun an equity model. Its continuous trading and public state make it a valuable laboratory
for adaptation and execution, while leverage, venue quality and programmable ordering expose
failure modes more sharply. Evidence can transfer at the level of method—point-in-time data,
cost-aware objectives, uncertainty and controls—but profitability numbers should remain stratified.
The AI-specific crypto evidence examined here is thinner than the equity evidence; common criteria
must not be mistaken for equal evidentiary depth.
8 Does the Evidence Establish Sustainable Excess Returns?
8.1 What the affirmative record establishes
Within the reviewed record, credible affirmative evidence exists in several designs. Large-panel
equity studies show that nonlinear ML can improve historical out-of-sample return prediction and
portfolio outcomes (Gu et al., 2020; Chen et al., 2024). Direct portfolio methods report economically
meaningful utility or risk-adjusted gains relative to linear and forecast-first baselines (Simon et al.,
2026; Cong et al., 2026; Jensen et al., 2026). Text models extract return-relevant information from
news under post-training-cutoff designs (Lopez-Lira and Tang, 2026), and point-in-time language
models produce economically meaningful signals without knowingly using later corpora (Kelly et al.,
2026). Within those settings, the results contradict two categorical positions: that flexible models
add no information, or that every favourable AI backtest is necessarily leakage.
One recent design also reports improvement on a selected upstream economic benchmark. Koijen
and Levy (2026) construct a real-time out-of-sample task around earnings announcements and report
that optimized agentic systems raise explained contemporaneous return variation from a standard
benchmark near 8% to close to 20%. This is evidence, within that protocol, that agents can structure
text into interpretable mechanisms. It is not a trading return: contemporaneous explanation around
an announcement includes price adjustment that may occur before an executable position can be
established. Its scientific value is strongest as a time-valid asset-pricing and information-processing
benchmark.
The reviewed crypto studies likewise document structured opportunities rather than pure noise.
Momentum, attention and cross-sectional factors appear in spot returns (Liu and Tsyvinski, 2021;
Liu et al., 2022b); persistent international price segmentation reveals limits to arbitrage (Makarov
and Schoar, 2020); and futures carry is economically large in some states (Schmeling et al., 2026).
AI may improve the speed or conditionality with which such states are recognized. But these premia
and mispricings can compensate exposure to crashes, constrained capital, custody and liquidation.
Their existence is an input to an AI strategy, not evidence that the model captures the return net
of competition.
8.2 Why the examined record does not establish general profitability
The evidence thins for four cumulative reasons. First, time validity is often incomplete. Historical
LLM queries are especially unreliable when the base model has seen the outcome (Lopez-Lira et al.,
2026). More traditional ML is not immune: Zhang et al. (2025) trace a reported monthly alpha to
look-ahead alignment and find that removing it erases the alpha; the journal subsequently issued an
expression of concern regarding the original article (The Review of Financial Studies, 2026). These
are not minor reproducibility details. They show that a plausible model can turn a data timestamp
error into an economically large story.
20

Table 5: Representative evidence and the maximum inference it supports. Numerical results are not
compared across rows because universes, horizons, objectives and costs differ.
Evidence Evaluation mode Affirmative inference Binding qualification
Gu et al.; Deep SDF Historical equity
OOS
Nonlinear characteristic structure
improves selected forecasts/portfolios
Historical, universe- and
implementation-specific
Deep policies; Alpha-
Portfolio
Historical decision
OOS
Economic objectives and sequence
modeling can improve selected
portfolios
Preference, search, constraint and
cost-model dependence
Implementable frontier Historical cost-
aware OOS
Joint cost-aware learning dominates
cost-agnostic construction in the
study
Simulated costs and capacity; not live
capital
Post-cutoff news LLM Post-training-
cutoff event test
LLM semantics can identify
return-relevant news and later drift
Latency, adoption decay and portfolio
implementation
Point-in-time LMs Chronological
model checkpoints
Useful text signals need not rely on
future-trained models
Historical portfolio construction
remains model-specific
Prospective household
portfolios
Daily precommit-
ted recommenda-
tions
Direct evidence of LLM style,
concentration and behavior
No significant adjusted abnormal
return; preliminary period
AI hedge-fund field
data
Observed fund
classifications and
returns
Early AI adopters show potential;
strategies are not simply homogeneous
Relative outperformance declines; AI
classification is observational
Live/real-time agent
benchmarks
Prospective paper
or contemporane-
ous tasks
Reduce hindsight and test changing
models
Generally short, small-scale, not
audited live-capital alpha
Second, repeated search and publication selection inflate the observed maximum. Reality-check
and backtest-overfitting methods formalize the problem (White, 2000; Bailey et al., 2017). In an
LLM or agent experiment the search space includes prompts, role descriptions, memory lengths,
retrieval sources, model versions, random seeds, assets and windows. Reporting only the best
trajectory understates uncertainty even if the final period is technically held out. A complete record
should identify the frozen specification and distinguish exploratory validation from confirmatory
testing.
Third, implementation and equilibrium erode signals. Costs are endogenous to turnover, urgency,
liquidity and capital; cost-agnostic ML can select precisely the least scalable opportunities (Jensen
et al., 2026). After publication, anomaly returns decline in ways consistent with both initial overfit
and investor learning (McLean and Pontiff, 2016). An AI strategy may accelerate its own decay:
faster extraction makes the early price response more efficient, while common models and data
reduce uniqueness. The falling strength of the headline signal as ChatGPT use diffuses in Lopez-Lira
and Tang (2026) is consistent with this reflexive mechanism, although it does not identify all causes.
Fourth, emerging prospective and field evidence is more restrained than selected backtests.
Carlin et al. (2026) collect daily LLM stock recommendations prospectively. They find concentrated
tilts toward large, growth and momentum stocks and media attention, while buy-and-hold and
active AI portfolios do not earn statistically significant abnormal returns under their characteristic
adjustment. The study is preliminary and its prompts, retail framing and period do not cover
all professional systems; its importance is that it observes choices before outcomes and separates
raw returns from style-adjusted skill. Using regulatory disclosures, labor-market information and
strategy descriptions, Chen et al. (2026) find that AI hedge funds outperformed non-AI peers
early, but that this advantage declined over time even among early adopters. They also find lower,
not higher, return comovement among AI funds, qualifying the simple claim that AI necessarily
homogenizes all strategies. Together these studies support potential and diffusion limits, not a
zero-effect verdict.
21

8.3 The bounded verdict
Within the evidence examined here, the right conclusion is a gradient across profile dimensions.
For representation, extraction and selected historical forecasts, evidence of progress is strong. For
historical economic value under a disclosed portfolio and cost model, evidence is meaningful but
heterogeneous. For prospective paper decisions, the reviewed record is growing and mixed. For
independently audited live-capital performance that persists across regimes and capital scales, that
public record is sparse. It therefore does not support a claim that a foundation-model, RL or agent
family generally generates sustainable net alpha.
“Insufficient” is not “negative.” A proprietary strategy may possess unique point-in-time data,
careful execution and a record that cannot be published without destroying its edge. Nor would a
universal public algorithm be economically stable if inexpensive replication immediately crowded it.
The bounded claim is epistemic: the academic and public product evidence examined here cannot
carry a stronger conclusion than its designs permit. For researchers, the implication is to strengthen
each material evidence-profile dimension and use prospective or live designs when the claim requires
them. For users, it is to ask which part of a return comes from market exposure, known styles,
leverage, omitted cost and selected timing before attributing the residual to AI.
9 A Research Agenda for More Credible and More Durable Net
Returns
The reviewed evidence does not justify a recipe for alpha, but it identifies where research effort
may improve durable economic value. The agenda is joint: better data cannot rescue a cost-blind
objective, and a realistic simulator cannot rescue a contaminated model. Six linked directions follow
from the alpha-translation chain.
9.1 Make information and models point-in-time by construction
Every observation should carry both an event time and an availability time. Fundamental databases
need original vintages and restatements; universes need listings, delistings and membership at
each date; news needs first-public timestamps and corrections; crypto needs historical symbol,
contract and venue specifications; on-chain decisions need the state observable when a transaction
was formed, not only after inclusion. Data lineage should connect each feature to its source and
transformation. A compact “information bill of materials” can list providers, fields, lags, revisions,
timezone, missing-value policy and universe rules.
The model itself belongs in that bill. Historical LLM evaluation should use point-in-time base
checkpoints, not merely retrieval restricted to old documents. The checkpoint sequence of Kelly
et al. (2026) demonstrates that such infrastructure is feasible at useful scale. When chronological
pretraining is unavailable, researchers should prefer truly post-cutoff prospective tests and explicitly
limit the inference, supplemented by memorization probes (Lopez-Lira et al., 2026). Prompts,
system instructions, tool schemas, embedding models and external search indices must be versioned
because any can encode later information.
This standard will initially reduce headline performance and sample length. That is a feature:
it converts hidden bias into visible uncertainty. Shared, versioned point-in-time testbeds across
equities and each crypto stratum would create more cumulative knowledge than another untraceable
leaderboard.
22

9.2 Train for economic decisions, including abstention
Targets should reflect the action and horizon. Next-period squared error is useful when the output
genuinely feeds a mean forecast; it is poorly aligned with ranking, event surprise, tail risk or execution.
Decision-focused objectives can include risk, turnover and costs directly, as the implementable-
frontier and deep-policy evidence illustrates (Jensen et al., 2026; Simon et al., 2026). Distributional
forecasts are preferable when position size depends on uncertainty, and calibrated abstention should
be an explicit action. A model that declines low-quality trades may create more value than one
forced to issue a daily buy/sell label.
Economic objectives must be evaluated for specification gaming. Researchers should show which
holdings and market states produce gains; perturb risk aversion, cost and financing; and compare
against simple policies using the same information. Multi-objective reporting is safer than optimizing
one reported Sharpe ratio. At minimum, return, risk, turnover, concentration, capacity and tail loss
should remain visible rather than collapsed into a score whose weights were selected after the test.
9.3 Co-design signal, portfolio, and execution
The usual modular pipeline freezes a forecast before learning whether it is tradable. A better
design passes cost and capacity information upstream. Slow signals may be aggregated and netted;
fast signals may justify trading only in liquid names or at sufficiently high confidence; execution
uncertainty may reduce target positions. Portfolio combinations can cancel trades rather than
simply average forecasts (DeMiguel et al., 2020). Execution policies should optimize a fixed parent
decision and be measured by implementation shortfall, keeping signal quality separate from fill
quality.
Capacity curves should be first-class results. Report net performance over capital, participation
rate and latency, with spread, nonlinear impact, borrow/funding and venue-specific losses varied
independently. For crypto, use separate engines for spot, perpetual and on-chain P&L. An agent
that chooses a perpetual must receive the funding and liquidation state; one that calls a DEX
needs transaction-order and failed-gas simulation. Cross-venue arbitrage requires a capital and
counterparty model, not instantaneous transfer at displayed prices.
Market impact creates a further research opportunity: train policies on endogenous response
rather than a fixed tape. Historical limit-order-book replay can support small-action evaluation,
while calibrated agent-based or structural simulators can explore counterfactual larger actions.
Because simulator misspecification is inevitable, policies should be stress-tested across several
plausible response models and graduate through paper, shadow and limited live stages. Robustness
to a family of simulators is more informative than mastery of one.
9.4 Treat adaptation as a controlled experiment
Financial relationships decay through macro change, regulation, venue redesign, competition and the
model’s own adoption. Adaptation is therefore necessary, but unconstrained online updating makes
evaluation and governance ambiguous. A deployable system needs predeclared triggers, candidate
generation, shadow comparison, approval, rollback and an immutable record of the active version.
Performance monitoring should attribute changes to beta, style, volatility, liquidity, costs, model
output and execution rather than watching cumulative return alone.
Research can distinguish several adaptation mechanisms: rolling or expanding retraining; state-
conditioned mixtures; change-point detection; meta-learning; memory retrieval; and human revision.
They should be compared under the same information and compute budget. A memory-equipped
LLM may appear adaptive because it reads recent outcomes, while a simple volatility-conditioned
23

rule may explain the gain. Tests should include structural breaks not used to tune the detector,
source outages, asset entry and exit, fee-rule changes and adversarial news.
Crowding should also enter evaluation. Post-publication decay (McLean and Pontiff, 2016) and
declining AI-fund relative performance (Chen et al., 2026) imply that a static historical edge is not
a stable resource. A useful model estimates how return and capacity change as similar capital grows.
Research consortia can test this indirectly through signal overlap, trade correlation and response to
public release, while recognizing that exact proprietary positions will remain unavailable.
9.5 Replace retrospective showcases with prospective evidence
The next generation of benchmarks should require a precommitted decision artifact before the
outcome. A public append-only ledger can record model and data versions, eligible universe,
prompt/policy hash, target holdings, order timestamp and subsequent correction policy. Paper
portfolios should use executable bid/ask or documented fill models and preserve rejected or missing
decisions. Model updates should start a new cohort rather than rewriting the prior record. Prospec-
tive household recommendations (Carlin et al., 2026), real-time earnings benchmarks (Koijen and
Levy, 2026) and live-market agent arenas (Qian et al., 2026) show complementary ways to reduce
hindsight.
Prospective evaluation does not require immediate unrestricted capital. A safe sequence is offline
frozen test, historical event replay, forward shadow decisions, broker paper orders, small-capital
controlled deployment and only then scaled authority. Each stage answers a different question. A
study can be valuable if it stops at paper trading, provided it does not describe simulated fills as
live trading. Independent replication should reproduce the decision log and metric calculation, not
merely rerun open code on a newly downloaded and potentially revised dataset.
Statistical protocols must count search. Pre-registering one final specification is ideal but not
always compatible with systems research. An alternative is a transparent model-development ledger,
a sequestered confirmatory period and family-wise or false-discovery control across material variants
(Harvey et al., 2016; White, 2000). Uncertainty should reflect serial dependence and stochastic
model runs. A table of all attempted configurations is often more scientifically informative than an
additional best-case chart.
9.6 Engineer governance in proportion to authority
Governance is part of attainable performance because operational loss can overwhelm a statistical
edge. The NIST AI Risk Management Framework provides general functions for governing, mapping,
measuring and managing AI risk (Tabassi, 2023); IOSCO documents capital-market AI use cases and
risks from a securities-regulatory perspective (International Organization of Securities Commissions,
2025). Existing market-access controls also supply a concrete principle: systems with order authority
require pre-trade financial and regulatory limits, controlled access, monitoring and review (U.S.
Securities and Exchange Commission, 2011). These sources do not certify a particular trading agent,
nor do they substitute for jurisdiction-specific legal analysis. They anchor a control architecture.
A practical separation has four planes. Theinformation planeretrieves untrusted external
content and must defend against prompt injection, stale data and malicious files. Thedecision
planeestimates signals and target positions but cannot alter limits. Theexecution planevalidates
identity, price, notional, leverage, venue, instrument and freshness through deterministic controls.
Theassurance planeindependently records inputs, approvals, orders, fills, reconciliations, incidents
and model versions. Credentials are scoped to the minimum action, stored outside prompts, rotated
and revocable. Natural-language confirmation is not a substitute for structured order validation.
24

For LLM agents, reproducibility and semantic risk are linked. Generated rationales can cite
nonexistent evidence, confuse units or change a ticker through an ambiguous name. Retrieval should
return source identifiers and timestamps; numerical quantities should be parsed into typed schemas
and checked by deterministic code; conflicting sources should remain visible; and the system should
fail closed when instrument identity or unit conversion is uncertain. Human oversight must be
defined by an actual decision right and response window, not the statement that a human is “in the
loop.”
The Federal Reserve’s revised model-risk guidance illustrates the importance of reading gover-
nance scope precisely: its 2026 supervisory letter revises expectations for models used by banking
organizations and states that generative and agentic AI fall outside the guidance’s defined model
scope, even though broader risk-management obligations may still apply (Board of Governors
of the Federal Reserve System, 2026). It would therefore be wrong to cite that letter as direct
approval or a complete rulebook for trading agents. The general lesson is to map each system to the
rules governing its institution, activity, data and market access rather than invoke “AI compliance”
abstractly.
9.7 A falsifiable program, not an optimism premium
These directions should be evaluated as hypotheses. Point-in-time pretraining may reduce apparent
performance without finding a replacement edge. Cost-aware objectives may overfit a cost curve.
Joint execution learning may add complexity without improving fills. Governance may reduce
speed while preventing rare losses. The appropriate outcome is a set of measured trade-offs. A
credible research program should publish negative results, document where the alpha-translation
chain breaks and distinguish failure of a signal from failure of its implementation.
The most promising competitive advantage may be less visible than a new model name: cleaner
proprietary timestamps, a unique but lawful information source, faster error correction, lower
turnover, better risk aggregation, patient execution and disciplined decision rights. Foundation
models and agents can amplify these capabilities, but they can also commoditize public analysis.
The synthesis developed here suggests that sustainable net alpha, where it exists, is more plausibly
a property of the complete socio-technical investment process than of one architecture alone.
10 Conclusion
The reviewed evidence documents material technical progress at several points in the investment
chain. Nonlinear models extract structure from broad equity panels; deep and reinforcement-
learning policies place economic objectives inside portfolio construction; time-series models transfer
representations; language models process news and disclosure at scale; and agents combine retrieval,
memory, analysis, tools and execution interfaces. Crypto markets extend the opportunity set through
continuous data and observable blockchain state while exposing funding, liquidation, manipulation,
custody, gas, MEV and smart-contract risks that cannot be represented by an equity-style cost
scalar.
The public profitability record examined here is narrower than this technical record. Strong
historical out-of-sample findings coexist with anomaly decay, multiple-testing risk, timestamp
corrections that erase returns, LLM memorization, cost- and capacity-sensitive frontiers, prospective
portfolios without significant abnormal returns, and limited independently audited live-capital
evidence. The resulting conclusion is not that AI cannot earn excess returns. It is that the evidence
examined through 31 August 2026 does not establish a general AI architecture that produces
persistent, cross-regime, capacity-aware net alpha.
25

Progress should therefore be judged by the weakest link between information and realized net
performance. Point-in-time data and model versions, decision-aligned objectives, joint portfolio–
execution design, explicit market-specific P&L, controlled adaptation, prospective records and
authority-matched governance can make future claims more credible and may improve economic
outcomes. None guarantees profit. Their value is that they convert an attractive backtest into a
sequence of falsifiable claims—and make failure visible before it becomes uncontrolled capital loss.
Declaration of Generative AI Use
Generative AI tools assisted with literature discovery, drafting, language editing, and LaTeX
preparation; the authors verified the sources, interpretations, and final text and take full responsibility
for the manuscript.
References
Carol Alexander, Jaehyuk Choi, Heungju Park, and Sungbin Sohn. BitMEX bitcoin derivatives:
Price discovery, informational efficiency, and hedging effectiveness.Journal of Futures Markets,
40(1):23–43, 2020. doi: 10.1002/fut.22050.
Robert Almgren and Neil Chriss. Optimal execution of portfolio transactions.Journal of Risk, 3(2):
5–39, 2001. doi: 10.21314/JOR.2001.041.
Miquel Noguer I Alonso and Rodolfo Pereira Franklin. Pretrained time-series foundation models for
financial return forecasting.arXiv preprint arXiv:2606.27100, 2026. doi: 10.48550/arXiv.2606.27
100. URL https://arxiv.org/abs/2606.27100v1. Version 1 submitted 25 June 2026.
Arash Aloosh and Jiasun Li. Direct evidence of bitcoin wash trading.Management Science, 70(12):
8875–8921, 2024. doi: 10.1287/mnsc.2021.01448.
Alpaca. Introducing alpaca’s official MCP server: Enabling multi-market trading with AI interfaces,
November 2025. URL https://alpaca.markets/blog/introducing-official-mcp-server-enabling-mul
ti-market-trading-with-ai-interfaces/. First-party product announcement, 20 November 2025;
capability evidence only.
Alpaca. Alpaca launches MCP server V2, April 2026. URL https://alpaca.markets/blog/alpa
ca-launches-mcp-server-v2/. First-party product announcement, 9 April 2026; capability and
risk-warning evidence only.
Abdul Fatir Ansari, Lorenzo Stella, Caner Turkmen, Xiyuan Zhang, Pedro Mercado, Huibin Shen,
Oleksandr Shchur, Syama Sundar Rangapuram, Sebastian Pineda Arango, Shubham Kapoor,
et al. Chronos: Learning the language of time series.Transactions on Machine Learning Research,
2024. doi: 10.48550/arXiv.2403.07815. URL https://arxiv.org/abs/2403.07815. arXiv:2403.07815.
David H. Bailey, Jonathan M. Borwein, Marcos López de Prado, and Qiji Jim Zhu. The probability
of backtest overfitting.Journal of Computational Finance, 20(4):39–69, 2017. doi: 10.21314/JCF
.2016.322.
Board of Governors of the Federal Reserve System. Revised supervisory guidance on model risk
management, April 2026. URL https://www.federalreserve.gov/supervisionreg/srletters/SR2602
.htm. Supervision and Regulation Letter SR 26-2, 17 April 2026.
26

Gabriel Borrageiro, Nick Firoozye, and Paolo Barucca. The recurrent reinforcement learning crypto
agent.IEEE Access, 10:38590–38599, 2022. doi: 10.1109/ACCESS.2022.3166599.
Agostino Capponi and Ruizhe Jia. Liquidity provision on blockchain-based decentralized exchanges.
The Review of Financial Studies, 38(10):3040–3085, 2025. doi: 10.1093/rfs/hhaf046.
Agostino Capponi, Ruizhe Jia, and Shihao Yu. Price discovery on decentralized exchanges.The
Review of Financial Studies, page hhag002, 2026. doi: 10.1093/rfs/hhag002. Corrected proof,
published 19 January 2026.
Bruce I. Carlin, Ryan D. Israelsen, and Christopher F. Wazzan. AI managed household portfolios:
A preliminary report. Technical Report 35153, National Bureau of Economic Research, April
2026. URL https://www.nber.org/papers/w35153.
Andrew Y. Chen and Tom Zimmermann. Open source cross-sectional asset pricing.Critical Finance
Review, 11(2):207–264, 2022. doi: 10.1561/104.00000112. URL https://www.openassetpricing.c
om/.
Luyang Chen, Markus Pelger, and Jason Zhu. Deep learning in asset pricing.Management Science,
70(2):714–750, 2024. doi: 10.1287/mnsc.2023.4695.
Shuang Chen, Clemens Sialm, and David X. Xu. The growth and performance of artificial intelligence
in asset management. Technical Report 35273, National Bureau of Economic Research, May 2026.
URL https://www.nber.org/papers/w35273.
Yanxu Chen, Zijun Yao, Yantao Liu, Amy Xin, Jin Ye, Jianing Yu, Lei Hou, and Juanzi Li.
StockBench: Can LLM agents trade stocks profitably in real-world markets?arXiv preprint
arXiv:2510.02209, 2025. URL https://arxiv.org/abs/2510.02209v2. arXiv:2510.02209v2, revised 2
March 2026.
Coinbase Developer Platform. Introducing AgentKit, November 2024. URL https://www.coin
base.com/developer-platform/discover/launches/introducing-agentkit. First-party product
announcement, 8 November 2024; capability evidence only.
Lin William Cong, Xi Li, Ke Tang, and Yang Yang. Crypto wash trading.Management Science, 69
(11):6427–6454, 2023. doi: 10.1287/mnsc.2021.02709.
Lin William Cong, Ke Tang, and Jingyuan Wang. AlphaPortfolio: Goal-oriented investment
management through deep reinforcement learning. Technical Report 35195, National Bureau of
Economic Research, May 2026. URL https://www.nber.org/papers/w35195.
Abhimanyu Das, Weihao Kong, Rajat Sen, and Yichen Zhou. A decoder-only foundation model for
time-series forecasting. InProceedings of the 41st International Conference on Machine Learning,
volume 235 ofProceedings of Machine Learning Research, pages 10148–10167. PMLR, 2024. URL
https://proceedings.mlr.press/v235/das24c.html.
Victor DeMiguel, Lorenzo Garlappi, and Raman Uppal. Optimal versus naive diversification: How
inefficient is the 1/n portfolio strategy?The Review of Financial Studies, 22(5):1915–1953, 2009.
doi: 10.1093/rfs/hhm075.
Victor DeMiguel, Alberto Martín-Utrera, Francisco J. Nogales, and Raman Uppal. A transaction-
cost perspective on the multitude of firm characteristics.The Review of Financial Studies, 33(5):
2180–2222, 2020. doi: 10.1093/rfs/hhz085.
27

Andrea Frazzini, Ronen Israel, and Tobias J. Moskowitz. Trading costs. Technical Report 3229719,
SSRN, 2018. Working paper; evidence from live institutional trades.
Robin Fritsch and Andrea Canidio. Measuring arbitrage losses and profitability of AMM liquidity.
InCompanion Proceedings of the ACM Web Conference 2024, pages 1761–1767, 2024. doi:
10.1145/3589335.3651961.
Amit Goyal, Ivo Welch, and Athanasse Zafirov. A comprehensive 2022 look at the empirical
performance of equity premium prediction.The Review of Financial Studies, 37(11):3490–3557,
2024. doi: 10.1093/rfs/hhae044.
Shihao Gu, Bryan Kelly, and Dacheng Xiu. Empirical asset pricing via machine learning.The
Review of Financial Studies, 33(5):2223–2273, 2020. doi: 10.1093/rfs/hhaa009.
Campbell R. Harvey, Yan Liu, and Heqing Zhu. ...and the cross-section of expected returns.The
Review of Financial Studies, 29(1):5–68, 2016. doi: 10.1093/rfs/hhv059.
Kewei Hou, Chen Xue, and Lu Zhang. Replicating anomalies.The Review of Financial Studies, 33
(5):2019–2133, 2020. doi: 10.1093/rfs/hhy131.
Fengrui Hua, Hengyi Yang, Xinlei Hao, Haohan Zhang, Bokai Cao, Yiyan Qi, Jia Li, and Jian Guo.
Agentic quantitative trading: A survey of workflows, systems, and evaluation.arXiv preprint
arXiv:2608.31041, 2026. doi: 10.48550/arXiv.2608.31041. URL https://arxiv.org/abs/2608.31041
v1. Version 1 submitted 31 August 2026.
International Organization of Securities Commissions. Artificial intelligence in capital markets: Use
cases, risks, and challenges. Technical report, IOSCO, 2025. URL https://www.iosco.org/library/
pubdocs/pdf/IOSCOPD788.pdf.
Theis Ingerslev Jensen, Bryan Kelly, and Lasse Heje Pedersen. Is there a replication crisis in finance?
The Journal of Finance, 78(5):2465–2518, 2023. doi: 10.1111/jofi.13249.
Theis Ingerslev Jensen, Bryan Kelly, Semyon Malamud, and Lasse Heje Pedersen. Machine learning
and the implementable efficient frontier.The Review of Financial Studies, page hhag022, 2026.
doi: 10.1093/rfs/hhag022. Corrected proof, published 15 March 2026.
Zheng Ke, Bryan T. Kelly, and Dacheng Xiu. Predicting returns with text data. Technical Report
26186, National Bureau of Economic Research, 2019. URL https://www.nber.org/papers/w26186.
Bryan T. Kelly, Semyon Malamud, Johannes Schwab, and Teng Andrea Xu. Scaling point-in-time
language models. Technical Report 35247, National Bureau of Economic Research, May 2026.
URL https://www.nber.org/papers/w35247.
Ralph S. J. Koijen and Bradford Levy. Assessing the benefits of optimized agentic AI systems for
asset pricing. Technical Report 35431, National Bureau of Economic Research, July 2026. URL
https://www.nber.org/papers/w35431.
Albert S. Kyle. Continuous auctions and insider trading.Econometrica, 53(6):1315–1335, 1985. doi:
10.2307/1913210.
Jaehoon Lee, Jun Seo, Seunghan Lee, Tae Yoon Lim, Dongwan Kang, Hwanil Choi, Minjae Kim,
Sungdong Yoo, Junhyeok Kang, Sangjun Han, Soonyoung Lee, and Wonbin Ahn. FinVerse:
Financial time-series benchmark.arXiv preprint arXiv:2608.03259, 2026. doi: 10.48550/arXiv.2
608.03259. URL https://arxiv.org/abs/2608.03259v2. Version 2, 20 August 2026.
28

Changlun Li, Yao Shi, Chen Wang, Qiqi Duan, Runke Ruan, Weijie Huang, Haonan Long, Lijun
Huang, Nan Tang, and Yuyu Luo. Time travel is cheating: Going live with DeepFund for real-time
fund investment benchmarking. InAdvances in Neural Information Processing Systems, volume 38,
2025. doi: 10.52202/085713-5554. URL https://papers.nips.cc/paper_files/paper/2025/hash/f37
b0e09b90e9a6833aacf5768362b54-Abstract-Datasets_and_Benchmarks_Track.html.
Yuan Li, Bingqiao Luo, Qian Wang, Nuo Chen, Xu Liu, and Bingsheng He. CryptoTrade: A
reflective LLM-based agent to guide zero-shot cryptocurrency trading. InProceedings of the 2024
Conference on Empirical Methods in Natural Language Processing, pages 1094–1106, 2024. doi:
10.18653/v1/2024.emnlp-main.63. URL https://aclanthology.org/2024.emnlp-main.63/.
Xiao-Yang Liu, Ziyi Xia, Jingyang Rui, Jiechao Gao, Hongyang Yang, Ming Zhu, Christina Wang,
Zhaoran Wang, and Jian Guo. FinRL-Meta: Market environments and benchmarks for data-
driven financial reinforcement learning. InAdvances in Neural Information Processing Systems,
volume 35, pages 1835–1849, 2022a. doi: 10.52202/068431-0134. URL https://proceedings.neurip
s.cc/paper_files/paper/2022/hash/0bf54b80686d2c4dc0808c2e98d430f7-Abstract.html.
Yukun Liu and Aleh Tsyvinski. Risks and returns of cryptocurrency.The Review of Financial
Studies, 34(6):2689–2727, 2021. doi: 10.1093/rfs/hhaa113.
Yukun Liu, Aleh Tsyvinski, and Xi Wu. Common risk factors in cryptocurrency.The Journal of
Finance, 77(2):1133–1177, 2022b. doi: 10.1111/jofi.13119.
Alejandro Lopez-Lira and Yuehua Tang. Can ChatGPT forecast stock price movements? return
predictability and large language models.Journal of Financial Economics, 2026. doi: 10.1016/j.
jfineco.2026.104335. Published online before 31 August 2026; earlier version arXiv:2304.07619.
Alejandro Lopez-Lira, Yuehua Tang, and Mingyin Zhu. The memorization problem: Can we trust
LLMs’ economic forecasts?arXiv preprint arXiv:2504.14765, 2026. doi: 10.48550/arXiv.2504.14
765. URL https://arxiv.org/abs/2504.14765. Version dated 22 March 2026.
Tim Loughran and Bill McDonald. When is a liability not a liability? textual analysis, dictionaries,
and 10-Ks.The Journal of Finance, 66(1):35–65, 2011. doi: 10.1111/j.1540-6261.2010.01625.x.
Tianmi Ma, Jiawei Du, Wenxin Huang, Wenjie Wang, Liang Xie, Xian Zhong, and Joey Tianyi Zhou.
Agent trading arena: A study on numerical understanding in LLM-based agents. InFindings
of the Association for Computational Linguistics: EMNLP 2025, pages 5496–5514, 2025. doi:
10.18653/v1/2025.findings-emnlp.294. URL https://aclanthology.org/2025.findings-emnlp.294/.
Dimitri Mahayana, Elbert Shan, and Muhammad Fadhl’Abbas. Deep reinforcement learning to
automate cryptocurrency trading. In2022 12th International Conference on System Engineering
and Technology, pages 36–41. IEEE, 2022. doi: 10.1109/ICSET57543.2022.10010940. URL
https://ieeexplore.ieee.org/document/10010940/.
Igor Makarov and Antoinette Schoar. Trading and arbitrage in cryptocurrency markets.Journal of
Financial Economics, 135(2):293–319, 2020. doi: 10.1016/j.jfineco.2019.07.001.
Harry Markowitz. Portfolio selection.The Journal of Finance, 7(1):77–91, 1952. doi: 10.1111/j.15
40-6261.1952.tb01525.x.
R. David McLean and Jeffrey Pontiff. Does academic research destroy stock return predictability?
The Journal of Finance, 71(1):5–32, 2016. doi: 10.1111/jofi.12365.
29

Jason Milionis, Ciamac C. Moallemi, Tim Roughgarden, and Anthony Lee Zhang. Automated
market making and loss-versus-rebalancing.arXiv preprint arXiv:2208.06046, 2022. doi: 10.485
50/arXiv.2208.06046. URL https://arxiv.org/abs/2208.06046.
John Moody and Matthew Saffell. Learning to trade via direct reinforcement.IEEE Transactions
on Neural Networks, 12(4):875–889, 2001. doi: 10.1109/72.935097.
Yuriy Nevmyvaka, Yi Feng, and Michael J. Kearns. Reinforcement learning for optimized trade
execution. InProceedings of the 23rd International Conference on Machine Learning, pages
673–680, 2006. doi: 10.1145/1143844.1143929.
Robert Novy-Marx and Mihail Velikov. A taxonomy of anomalies and their trading costs.The
Review of Financial Studies, 29(1):104–147, 2016. doi: 10.1093/rfs/hhv063.
Lingfei Qian, Xueqing Peng, Hanley Smith, Yi Han, Yueru He, Haohang Li, Yupeng Cao, Yangyang
Yu, Guojun Xiong, Peng Lu, Yan Wang, Vincent Jim Zhang, Huan He, Alejandro Lopez-Lira,
Jimin Huang, Jian-Yun Nie, and Sophia Ananiadou. When agents trade: Live multi-market
trading arena for LLM agents. InProceedings of the ACM Web Conference 2026, pages 7833–7844,
2026. doi: 10.1145/3774904.3792821. URL https://doi.org/10.1145/3774904.3792821.
Robinhood Markets. Introducing robinhood strategies, banking, and cortex, March 2025. URL
https://robinhood.com/us/en/newsroom/introducing-strategies-banking-and-cortex/. First-party
product announcement, 27 March 2025.
Robinhood Markets. Robinhood accelerates global expansion: Robinhood chain mainnet, stock
tokens, and agentic trading, July 2026a. URL https://robinhood.com/us/en/newsroom/robin
hood-accelerates-global-expansion-robinhood-chain-mainnet-stock-tokens-agentic-trading/.
First-party product announcement, 1 July 2026; capability evidence only.
Robinhood Markets. Robinhood reports second quarter 2026 results. Exhibit 99.1 furnished to
the U.S. Securities and Exchange Commission, July 2026b. URL https://www.sec.gov/Arch
ives/edgar/data/1783879/000178387926000113/q22026robinhoodexhibit991.htm. First-party
product-uptake figures; not performance or safety evidence.
Robinhood Markets. Agentic trading overview. Official support documentation, 2026c. URL
https://robinhood.com/us/en/support/articles/agentic-trading-overview/. Mutable first-party
capability and permission documentation; accessed 31 August 2026.
Maik Schmeling, Andreas Schrimpf, and Karamfil Todorov. Crypto carry.Management Science,
2026. doi: 10.1287/mnsc.2024.05069. Published online 6 May 2026.
Xiaoming Shi, Shiyu Wang, Yuqi Nie, Dianqi Li, Zhou Ye, Qingsong Wen, and Ming Jin. Time-
MoE: Billion-scale time series foundation models with mixture of experts. InThe Thirteenth
International Conference on Learning Representations, 2025. URL https://proceedings.iclr.cc/pa
per_files/paper/2025/hash/558d48c1f08675daa636e09bfe94a89e-Abstract-Conference.html.
Tyler Shumway. The delisting bias in CRSP data.The Journal of Finance, 52(1):327–340, 1997.
doi: 10.1111/j.1540-6261.1997.tb03818.x.
Frederik Simon, Sebastian Weibels, and Tom Zimmermann. Deep parametric portfolio policies.
Management Science, 2026. doi: 10.1287/mnsc.2025.00721. URL https://doi.org/10.1287/mnsc.2
025.00721. Published online 3 June 2026.
30

Shuo Sun, Molei Qin, Wentao Zhang, Haochong Xia, Chuqiao Zong, Jie Ying, Yonggang Xie,
Lingxuan Zhao, Xinrun Wang, and Bo An. TradeMaster: A holistic quantitative trading platform
empowered by reinforcement learning. InAdvances in Neural Information Processing Systems,
volume 36, 2023. doi: 10.52202/075280-2576. URL https://proceedings.neurips.cc/paper_files/p
aper/2023/hash/b8f6f7f2ba4137124ac976286eacb611-Abstract.html.
Elham Tabassi. Artificial intelligence risk management framework (AI RMF 1.0). Technical
Report NIST AI 100-1, National Institute of Standards and Technology, 2023. URL https:
//doi.org/10.6028/NIST.AI.100-1.
Mingtian Tan, Mike A. Merrill, Vinayak Gupta, Tim Althoff, and Thomas Hartvigsen. Are language
models actually useful for time series forecasting? InAdvances in Neural Information Processing
Systems, volume 37, 2024. doi: 10.52202/079017-1922. URL https://proceedings.neurips.cc/pap
er_files/paper/2024/hash/6ed5bf446f59e2c6646d23058c86424b-Abstract-Conference.html.
Paul C. Tetlock. Giving content to investor sentiment: The role of media in the stock market.The
Journal of Finance, 62(3):1139–1168, 2007. doi: 10.1111/j.1540-6261.2007.01232.x.
The Review of Financial Studies. Expression of concern: Man versus machine learning: The term
structure of earnings expectations and conditional biases.The Review of Financial Studies, 39(5):
1555, 2026. doi: 10.1093/rfs/hhag017.
U.S. Securities and Exchange Commission. Risk management controls for brokers or dealers with
market access, 2011. URL https://www.sec.gov/rules-regulations/2011/06/risk-management-con
trols-brokers-or-dealers-market-access. Rule 15c3-5 and official compliance material.
Ivo Welch and Amit Goyal. A comprehensive look at the empirical performance of equity premium
prediction.The Review of Financial Studies, 21(4):1455–1508, 2008. doi: 10.1093/rfs/hhm014.
Halbert White. A reality check for data snooping.Econometrica, 68(5):1097–1126, 2000. doi:
10.1111/1468-0262.00152.
Gerald Woo, Chenghao Liu, Akshat Kumar, Caiming Xiong, Silvio Savarese, and Doyen Sahoo.
Unified training of universal time series forecasting transformers. InProceedings of the 41st
International Conference on Machine Learning, volume 235 ofProceedings of Machine Learning
Research, pages 53140–53164. PMLR, 2024. URL https://proceedings.mlr.press/v235/woo24a.ht
ml.
Shijie Wu, Ozan Irsoy, Steven Lu, Vadim Dabravolski, Mark Dredze, Sebastian Gehrmann, Prabhan-
jan Kambadur, David Rosenberg, and Gideon Mann. BloombergGPT: A large language model
for finance.arXiv preprint arXiv:2303.17564, 2023. doi: 10.48550/arXiv.2303.17564. URL
https://arxiv.org/abs/2303.17564.
Yihan Xia, Panpan You, Taotao Wang, Fang Liu, Han Qi, Xiaoxiao Wu, and Shengli Zhang. Agentic
trading: When LLM agents meet financial markets.arXiv preprint arXiv:2605.19337, 2026. doi:
10.48550/arXiv.2605.19337. URL https://arxiv.org/abs/2605.19337v1. Version 1 submitted 19
May 2026; audit-oriented preprint.
Yijia Xiao, Edward Sun, Di Luo, and Wei Wang. TradingAgents: Multi-agents LLM financial trading
framework.arXiv preprint arXiv:2412.20138, 2024. URL https://arxiv.org/abs/2412.20138v7.
arXiv:2412.20138v7, revised 3 June 2025.
31

Hongyang Yang, Xiao-Yang Liu, and Christina Dan Wang. FinGPT: Open-source financial large
language models.arXiv preprint arXiv:2306.06031, 2023. URL https://arxiv.org/abs/2306.06031.
Yangyang Yu, Haohang Li, Zhi Chen, Yuechen Jiang, Yang Li, Denghui Zhang, Rong Liu, Jordan W.
Suchow, and Khaldoun Khashanah. FinMem: A performance-enhanced LLM trading agent
with layered memory and character design.arXiv preprint arXiv:2311.13743, 2023. URL
https://arxiv.org/abs/2311.13743v2. arXiv:2311.13743v2.
Yangyang Yu, Zhiyuan Yao, Haohang Li, Zhiyang Deng, Yuechen Jiang, Yupeng Cao, Zhi Chen,
Jordan W. Suchow, Zhenyu Cui, Rong Liu, Zhaozhuo Xu, Denghui Zhang, K. P. Subbalakshmi,
Guojun Xiong, Yueru He, Jimin Huang, Dong Li, and Qianqian Xie. FinCon: A synthesized LLM
multi-agent system with conceptual verbal reinforcement for enhanced financial decision making. In
Advances in Neural Information Processing Systems, volume 37, 2024. doi: 10.52202/079017-4354.
URL https://papers.nips.cc/paper_files/paper/2024/hash/f7ae4fe91d96f50abc2211f09b6a7e4
9-Abstract-Conference.html.
Wentao Zhang, Lingxuan Zhao, Haochong Xia, Shuo Sun, Jiaze Sun, Molei Qin, Xinyi Li, Yuqing
Zhao, Yilei Zhao, Xinyu Cai, Longtao Zheng, Xinrun Wang, and Bo An. A multimodal foundation
agent for financial trading: Tool-augmented, diversified, and generalist. InProceedings of
the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, 2024. doi:
10.1145/3637528.3671801. URL https://doi.org/10.1145/3637528.3671801.
Yingguang Zhang, Yandi Zhu, and Juhani T. Linnainmaa. Man versus machine learning revisited.
The Review of Financial Studies, 38(12):3768–3790, 2025. doi: 10.1093/rfs/hhaf066.
Linsen Zhu and Yi Shi. DSA: Evidence-aware LLM-agent orchestration for multi-market stock
research.arXiv preprint arXiv:2608.26990, 2026. doi: 10.48550/arXiv.2608.26990. URL
https://arxiv.org/abs/2608.26990v1. arXiv:2608.26990v1.
32
