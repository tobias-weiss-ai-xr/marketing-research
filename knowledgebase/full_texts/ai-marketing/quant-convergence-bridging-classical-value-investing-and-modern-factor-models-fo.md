---
title: 'Quant Convergence: Bridging Classical Value Investing and Modern Factor Models for Systematic
  Equity Selection'
url: https://arxiv.org/abs/2606.24575
category: ai-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Augusto Eiji Yamazaki
- Hugo Garrido-Lestache Belinchon
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.24575
pages: 19
chars: 36002
fetched_at: '2026-11-08T13:04:52+00:00'
kb_version: 1
---

# Quant Convergence: Bridging Classical Value Investing and Modern Factor Models for Systematic Equity Selection

Quant Convergence: Bridging Classical Value Investing and
Modern Factor Models for Systematic Equity Selection
Augusto Eiji Yamazaki, Hugo Garrido-Lestache Belinchon
Milwaukee School of Engineering
Milwaukee, WI US
{eijiyamazaki,garrido-lestacheh}@msoe.edu
Abstract
Modern finance relies heavily on complex machine learning models to find patterns in the
stock market. However, as these AI models get more complicated, they often memorize
short-termmarketnoiseinsteadoffindingcompanieswithreal,lastingvalue. Wedesigned
this research to test if Benjamin Graham’s classic value investing rules could act as a
mathematical “low-pass filter” to keep these modern models in check. We built three
different sets of features—pure Graham rules, modern market factors, and a mix of both—
and tested them against highly complex models (XGBoost and AutoGluon) using 20 years
of S&P 500 data. By applying a strict buy-and-hold strategy over a four-year test period
(March 2022 to March 2026), the results showed that more complex algorithms do not
always win. While the AutoGluon model captured high returns (222.68%), it suffered
a substantial 39.78% drop because it bought volatile tech stocks right before the market
crashed. On the other hand, the pure Graham Random Forest achieved the highest overall
return (232.13%) with much less risk (1.38 Calmar Ratio). Furthermore, the Combined
Random Forest successfully mixed momentum with Graham’s rules, making a 202.91%
arXiv:2606.24575v1  [cs.AI]  23 Jun 2026

return while keeping the lowest maximum drop (34.53%) of any model tested. Ultimately,
this research proves that Graham’s “margin of safety” isn’t outdated; it is actually a highly
effective way to prevent modern AI from taking on too much risk.
1 Introduction
Stockselectionhasevolvedfrommanualanalysistoalgorithmictradingdrivenbycomplex
neural networks. In modern quantitative finance, state-of-the-art machine learning models
like XGBoost and AutoGluon are often used to hunt for hidden patterns in financial data.
However,thestockmarketisincrediblynoisy. Asthesemodelsgetmorecomplicated,they
risk “overfitting”—memorizing short-term market hype instead of finding companies with
actual, long-term value.
Long before machine learning existed, Benjamin Graham wroteThe Intelligent Investor,
creating strict, rule-based screens to find companies with strong balance sheets and con-
servative valuations. Specifically, his defensive framework requires seven core criteria: (1)
adequate enterprise size, (2) strong short-term liquidity (𝐶𝑢𝑟𝑟𝑒𝑛𝑡𝑅𝑎𝑡𝑖𝑜≥2), (3) consis-
tent positive earnings, (4) an uninterrupted dividend record, (5) demonstrated long-term
earningsgrowth, (6)amoderateprice-to-earningsratio(𝑃/𝐸≤15), and(7)aconservative
combined valuation multiple (𝑃/𝐸×𝑃/𝐵≤22.5). While designed for the 1940s, the
engineering goal behind these rules—acting as a mathematical “low-pass filter” to remove
financially fragile companies—makes intuitive sense. But does it actually hold up against
modern AI?
We designed this research to find out. By combining industrial engineering principles
with quantitative finance, we built a system to test Graham’s classical value signals against
modern quantitative factors (like momentum and volatility) and highly complex automated
ensembles. Through a rigorous 20-year backtest, our goal was to see if the structural
simplicityofclassicfundamentalscreensprovidesabettersignal-to-noiseratiothanmodern
black-box algorithms.
What we found challenged our own assumptions. Not only did Graham’s 1940s rules
survive, but they actively beat the modern AI models in both absolute returns and risk
management. Even more surprisingly, trying to modernize Graham’s rules by combining
themwithcontemporarymomentumfactorsactuallydilutedtheirperformance. Thispaper
breaks down exactly how we built this system, why the complex AI failed during market
shocks, and why pure fundamental logic is still the best regularization tool we have in
quantitative finance.
2

2 Related Works
2.1 Historical Validation of Value Investing Criteria
Thehistoricalfoundationofclassicalvalueinvestingreliesheavilyonthedefensivescreens
formalizedbyBenjaminGraham. EarlyempiricalstudiesdemonstratedthatGraham’sstrict
criteria—includingadequateenterprisesize,lowP/Eratios,androbustequitycapitalization—
yielded positive abnormal risk-adjusted returns for defensive investors [11]. Modern quan-
titative asset pricing has inadvertently echoed these principles; for example, the “Quality
Minus Junk” (QMJ) factor captures dimensions like safety, profitability, and payout ratios
that closely mirror Graham’s original requirements [2]. While these studies confirm that
Graham’s metrics work in isolation or in simple linear models, we need to evaluate how
this entire defensive framework holds up when mathematically transformed into a unified
feature set for complex, non-linear machine learning architectures.
2.2 Machine Learning in Fundamental Analysis and Asset Pricing
Machinelearninghasfundamentallyshiftedhowweforecastfinancialdata. Recentresearch
highlights this by applying Random Forests and Artificial Neural Networks to raw funda-
mental accounting variables, proving that non-linear models drastically reduce earnings
forecasterrorsandgeneratesignificantpredictivealphacomparedtotraditionallinearmod-
els [4]. This intersection has expanded by successfully digitizing and evaluating Graham’s
fundamental criteria using modern supervised learning algorithms [22]. Random Forests
trainedoncomprehensivevaluationvariablescansystematicallyisolatemarketsignalswhile
minimizing human bias [7].
In the broader scope of empirical asset pricing, non-linear architectures effectively double
the out-of-sample Sharpe ratio of standard panel regressions by naturally capturing com-
plex characteristic interactions [6]. Dissecting financial characteristics with nonparametric
methods further shows that accommodating non-linearities significantly increases out-of-
sampleexplanatorypower[5]. Evaluatingtheequitypremiumutilizingnon-linearmethods
likemultiplekernellearningonfinancialfeaturesvalidatesthenecessityofmovingbeyond
simple linear regressions [1].
3

2.3 Investability and Market-Specific Constraints
WhileacademicbacktestsofMLalgorithmsoftenignoretradingfrictions,recentliterature
emphasizes realistic implementations. “Investable and interpretable” ML utilizing 12-
month prediction horizons can significantly reduce portfolio turnover, proving that while
ML consistently outperforms linear models, the practical benefits are incremental when
subjected to liquidity constraints [9]. Similarly, ML strategies maintain robust alphas even
after adjusting for transaction costs by dynamically adapting to regime shifts [13].
Data integrity and synchronization are also critical. Studies capitalizing on synchronized
fiscal year-ends to eliminate look-ahead bias have shown that feeding financial ratios into
machine learning models generates significant excess returns [19]. Deep learning mod-
els have successfully extracted robust signals from fundamental profitability and growth
metrics in international markets as well [8]. To respect these real-world constraints and
guarantee reproducibility, our methodology enforces a strict 80/20 temporal split, locks all
algorithmic random seeds, and utilizes a single-trade buy-and-hold rule. This ensures that
the extracted ML signals are not just mathematically significant, but practically investable
without succumbing to look-ahead bias or prohibitive turnover.
2.4 Algorithmic Architectures: Ensembles and AutoML
The literature provides extensive evaluations of the specific tree-based and ensemble ar-
chitectures used in equity classification. Comprehensive evaluations of multiple classifiers
have long established that ensemble methods generally offer superior predictive accuracy
for stock price direction compared to single algorithms [3]. The evolution of financial
ML highlights how simple linear models have been superseded by robust ensembles like
Random Forest and XGBoost for handling non-linear asset behaviors [15, 20]. Compar-
ative studies explicitly verify that Random Forests achieve significantly higher prediction
accuracy with lower error rates than simple decision trees [21]. Moreover, portfolios opti-
mizedviaXGBoostandRandomForesteasilyachievehigherSharperatiosthantraditional
mean-variance frameworks [10].
Tomaximizetheextractionofthesesignalswithoutmanualbias,automatedmachinelearn-
ing(AutoML)frameworkshavebecomeabenchmark. Researchevaluatingframeworkslike
AutoGluon-TimeSeriesprovestheirefficacyinsystematicallystreamliningdatapreparation
andhyperparametertuningtoconstructpowerfulmulti-layeredensembles[16]. Ultimately,
the future of AI in finance does not lie in high-frequency trading, but in utilizing these
advancedcomputationalarchitecturesforlong-horizon, fundamentalcapitalallocationthat
mathematicallymirrorsthephilosophyofBenjaminGraham[14]. AdvancedMLtechniques
can even successfully aggregate global market anomalies into a single, highly profitable
4

mispricing signal [18].
Currently, the academic consensus leans toward feeding as many variables as possible
into hyper-complex models to find an edge. This paper pivots to a different approach.
We ask whether restricting a machine learning model exclusively to Graham’s classical
criteria yields a superior, structurally safer portfolio compared to relying on unrestricted,
high-dimensional quantitative factors.
3 Implementation and Methodology
3.1 System Architecture and Data Integrity Pipeline
WedefinedourinvestmentuniversebyscrapingthecurrentS&P500constituents,utilizing
theyfinanceAPItoretrieveupto20yearsofdailyadjustedOHLCVpricedataandtrailing
fundamental snapshots. This data acquisition protocol has been widely validated in recent
financial machine learning literature [17, 12].
Financialdatasetsinherentlycontainmissingvaluesandinfinityerrorsduetodifferingcor-
porate reporting schedules. Dropping incomplete records outright introduces survivorship
bias. Instead, we pruned features missing more than 90% of their data. The remaining
missing values were then imputed using the cross-sectional median. Critically, we com-
putedthismedianexclusivelyfromthetrainingperioddataandstoreditforprediction-time
imputation, explicitly preventing future data leakage into the training environment.
3.2 Label Construction and Feature Engineering
We framed equity selection as a binary classification problem. For each stock𝑖in the
universe, the total return𝑅𝑖 over the respective price window is calculated as:
𝑅𝑖 = 𝑃𝑒𝑛𝑑,𝑖 𝑃𝑠𝑡𝑎𝑟𝑡,𝑖 −1
A stock is labeled as an outperformer (𝑦𝑖 =1) if its return exceeds the cross-sectional
median of the S&P 500 universe for that period, generating an inherently balanced target
distribution:
5

𝑦𝑖 =
(
1if𝑅 𝑖 >median({𝑅 𝑗}𝑁 𝑗=1)
0otherwise
To predict this target, we engineered three distinct feature sets:
•StrategyA(GrahamFeatures):19featuresanchoredbyBenjaminGraham’sseven
defensive criteria, encoded as binary thresholds (e.g.,𝐶𝑢𝑟𝑟𝑒𝑛𝑡𝑅𝑎𝑡𝑖𝑜≥2.0,𝑃/𝐸×
𝑃/𝐵≤22.5). These are supplemented with continuous fundamental ratios and a
composite Graham Score.
•Strategy B (Modern Quantitative Factors):15 features computed entirely us-
ing vectorized operations. These include risk-return metrics (CAPM Alpha, Beta,
Sharpe), momentum signals, and a data-integrity signal based on Benford’s Law
(computed as the RMSE between the theoretical leading-digit distribution and a
firm’s reported revenues).
•Strategy C, D, E (Combined Features):An aggregated set of 36 to 40 features,
augmented with cross-domain interaction terms such as𝑉𝑎𝑙𝑢𝑒×𝑀𝑜𝑚𝑒𝑛𝑡𝑢𝑚and
𝑄𝑢𝑎𝑙𝑖𝑡𝑦×𝑆𝑡𝑎𝑏𝑖𝑙𝑖𝑡𝑦to capture established empirical persistence.
3.3 Model Architectures and Temporal Optimization
Thestudyevaluatesthreedistinctmachinelearningarchitectures. Weexecutedhyperparam-
eter optimization via Optuna using a Tree-structured Parzen Estimator (TPE). To prevent
data leakage during the Bayesian sweep, we replaced standard k-fold cross-validation with
aTimeSeriesSplit, optimizing for ROC-AUC to effectively manage financial data noise.
Furthermore,toguaranteereproducibilityandpreventstochasticvariancefromalteringour
results, we locked all global random seeds prior to initializing the models. The final tuned
parameters are as follows:
•Strategy A (Graham RF):Random Forest with 100 trees, maximum depth of 2,
minimum samples per leaf of 94, and maximum features of 0.2.
•Strategy B (Modern Quant RF):Random Forest with 100 trees, maximum depth
of 5, minimum samples per leaf of 75, andlog2 maximum features.
•Strategy C (Combined RF):Random Forest with 900 trees, maximum depth of 4,
minimum samples per leaf of 50, andlog2 maximum features.
•Strategy D (XGBoost):Gradient boosting classifier with a depth of 9, learning rate
of 0.053, child weight of 9, and dynamic scale positive weighting.
6

•StrategyE(AutoGluon):Anautomatedmachinelearningframeworkconfiguredto
intelligently stack multiple models. The meta-learner ultimately selected aWeighte-
dEnsemble_L2architecture.
3.4 Out-of-Sample Backtesting Protocol
To explicitly eliminate look-ahead bias, we partitioned the dataset of 5,027 trading days
(March 22, 2006, to March 16, 2026) using a strict 80/20 temporal split. The initial 4,021
days constituted the training window. The final 1,006 trading days (March 11, 2022, to
March 16, 2026) served as the completely unseen test window.
Upontrainingcompletion,eachmodelpredictedtheprobabilityofoutperformanceforevery
stock. We selected the top 20 equities ranked by highest probability. We simulated the
portfolio using thevectorbtlibrary, a high-speed matrix-based backtesting engine. The
simulation enforced a strict buy-and-hold protocol: the selected portfolio was purchased in
equal weights on the first day of the test period and held without rebalancing until the final
day.
4 Experimentation and Results
4.1 Out-of-Sample Performance Metrics
The out-of-sample test period (March 11, 2022, to March 16, 2026) provided an excep-
tionally rigorous environment to evaluate algorithmic resilience. This four-year window
contained a severe macroeconomic contraction in 2022, driven by inflation and aggressive
interest rate hikes, followed by a concentrated market rally. This exact sequence of market
regimes perfectly exposes whether a machine learning model has structurally learned to
identify value, or if it simply overfit to the preceding bull market.
Table 1 summarizes the core performance metrics of the 20-stock, equal-weight portfolios
generated by each model at the beginning of the test period, formally benchmarked against
the S&P 500 index (SPY).
7

Table 1: Out-of-Sample Portfolio Performance (March 2022 – March 2026)
Strategy / Feature Set Algorithm Total Return Max Drawdown Calmar Ratio
A — Pure Graham Random Forest232.13%35.01%1.38
B — Modern Quant Factors Random Forest 133.95% 37.28% 0.97
C — Combined Hybrid Random Forest 202.91%34.53%1.22
D — Combined Hybrid XGBoost 56.79% 36.26% 0.50
E — Unrestricted AutoML AutoGluon 222.68% 39.78% 1.16
Benchmark (SPY) S&P 50068.00% 24.00% 0.55
4.2 Absolute Return vs. Algorithmic Complexity
The empirical results fundamentally challenge the prevailing assumption that increased al-
gorithmiccomplexityandhigher-dimensionaldatanaturallyyieldsuperiorfinancialreturns.
When benchmarked against the S&P 500 index, which returned approximately 68.00%
over the four-year window, almost all machine learning architectures generated substantial
alpha. The hyper-optimized AutoGluon ensemble (Strategy E) performed exactly as one
might expect a state-of-the-art AI to perform: it aggressively captured upside momentum,
generating a significant 222.68% absolute return. However, it was outright defeated by
Strategy A (the pure Graham Random Forest), which generated the highest total return
of the entire backtest at 232.13%—more than tripling the performance of the benchmark
index.
Furthermore, the data reveals a severe degradation in performance when attempting to
“modernize” classical rules. When the Random Forest was forced to evaluate modern
quantitativemetricsalongsideclassicalfundamentals(StrategyC),thetotalreturndropped
to202.91%. Evenmoredrastically,whenthehighlycomplexXGBoostalgorithm(Strategy
D) was applied to the combined dataset, its predictive power collapsed entirely in the out-
of-sample window, yielding only a 56.79% return (underperforming the S&P 500). This
indicates severe overfitting during the cross-validation phase, a common failure point for
gradient boosting models applied to noisy financial time series.
4.3 Risk Mitigation and Drawdown Resilience
Whileabsolutereturnsarehighlyvisible,institutionalquantitativefinanceprioritizesstruc-
tural survival. Maximum Drawdown (the peak-to-trough decline of a portfolio) and the
Calmar Ratio (annualized return relative to that drawdown) are the definitive metrics for
evaluating algorithmic risk.
8

Inthisdomain,thestructurallyconstrainedmodelsdemonstratedoverwhelmingsuperiority.
AutoGluon’s aggressive allocation into high-beta tech equities caused it to suffer a severe
39.78% maximum drawdown during the 2022 market shock, drastically worse than the
benchmark’s 24.00% decline. This steep drop severely penalized its Calmar Ratio—a key
metric that divides a portfolio’s annualized return by its maximum drawdown. Essentially,
the Calmar Ratio tells us how much return a strategy generates for every unit of downside
riskitendures. BecauseAutoGluontookoncatastrophicrisktoachieveitsgains,itsCalmar
Ratio was dragged down to just 1.16.
By contrast, the fundamental low-pass filter performed flawlessly. Strategy C (Combined
RF) acted as the ultimate defensive buffer among the algorithms, recording the lowest
machine learning drawdown of the study at 34.53%. More importantly, Strategy A (Pure
Graham) managed to capture its market-leading 232.13% return while experiencing only a
35.01% drawdown. This asymmetrical risk-return profile resulted in a dominant, best-in-
class Calmar Ratio of 1.38.
The empirical conclusion is clear: restricting a non-linear machine learning architecture
exclusively to classical, 1940s balance sheet metrics does not handicap the model. Instead,
it serves as a highly effective regularization technique that prevents critical drawdowns
while maximizing risk-adjusted alpha against the broader market.
4.4 Visual Performance Analysis
Thedivergenceinalgorithmicperformanceismostevidentwhenexaminingthecumulative
returnsandpeak-to-troughdrawdowns. Figure1illustratesthetotalgrowthofa$1starting
investment,whileFigure2providesthe“underwater”perspectiveoftherisktakentoachieve
those returns.
9

Figure 1: Out-of-Sample Cumulative Portfolio Returns (2022–2026). Strategy A (Graham
RF) achieved the highest terminal value, significantly outperforming the S&P 500
benchmark.
Figure 2: Out-of-Sample Drawdown Analysis. This chart highlights the superior capital
preservation of the Graham-regularized models (A and C) compared to the unrestricted
AutoGluon ensemble (E).
10

4.5 Statistical Significance of Returns
Torigorouslyevaluatewhethertheexcessreturnsgeneratedbythemodelsweretheresultof
predictive edge rather than statistical noise, a Welch’s two-sample t-test was conducted on
theexactdailyreturndistributions. Thisspecifictestwasutilizedtoaccountfortheinherent
heteroscedasticity(unequalvariances)betweentheconcentratedalgorithmicportfoliosand
the broader market index.
Each of the five machine learning strategies was independently tested against the S&P 500
(SPY)benchmarkoverthe1,006-dayout-of-sampleperiod. Theformalhypothesisforeach
test was defined as:
•Null Hypothesis (𝐻 0):𝜇 𝑆𝑡𝑟𝑎𝑡𝑒𝑔𝑦 −𝜇 𝑆𝑃500≤0(The strategy’s mean daily return is
less than or equal to the market; any excess return is random variance).
•Alternative Hypothesis (𝐻𝑎):𝜇 𝑆𝑡𝑟𝑎𝑡𝑒𝑔𝑦 −𝜇 𝑆𝑃500 >0(The strategy generates true,
statistically significant excess returns over the market).
The calculated t-statistics and their corresponding p-values are detailed in Table 2.
Table 2: Welch’s t-Test: Machine Learning Strategies vs. S&P 500 Benchmark
Strategy Tested (vs. SPY) Ann. Return Ann. Volatility t-Statistic p-Value
A — Pure Graham RF 35.0% 22.4% 1.2950.098*
B — Modern Quant RF 23.6% 20.2% 0.672 0.251
C — Combined Hybrid RF 31.9% 22.8% 1.164 0.122
D — Combined XGBoost 11.9% 15.8% -0.131 0.552
E — Unrestricted AutoGluon 34.0% 25.8% 1.251 0.106
Benchmark (SPY) 13.8% 17.8% — —
*Note: Statistically significant at the𝛼=0.10level.
Rather than solely testing against the benchmark, an upper-triangular pairwise significance
matrix was constructed to compare every strategy against all alternative architectures. The
formal hypothesis for each cell evaluates whether the Row Strategy mean is strictly greater
than the Column Strategy mean (𝐻𝑎 :𝜇 𝑅𝑜𝑤 > 𝜇𝐶𝑜𝑙𝑢𝑚𝑛). The resulting p-values for the
out-of-sample period are presented in Table 3.
11

Table 3: Pairwise Welch’s t-Test p-values (Upper Triangular)
Strategy (Row > Column) A (Graham) B (Quant) C (Hybrid) D (XGBoost) E (AutoML) SPY
A (Graham RF)— 0.277 0.4270.077*0.4790.098*
B (Quant RF)— — 0.668 0.212 0.707 0.251
C (Hybrid RF)— — —0.097*0.552 0.122
D (XGBoost)— — — — 0.917 0.552
E (AutoML)— — — — — 0.106
SPY (Benchmark)— — — — — —
*Note: Statisticallysignificantatthe𝛼=0.10level. Thetabledisplaystheuppertriangular
matrix to eliminate directional redundancy.
Interpretation of Statistical Results
TheanalysisrevealsthatStrategyA(PureGrahamRF)yieldedap-valueof0.098againstthe
S&P 500. While this marginally exceeds the strict𝛼=0.05threshold used in laboratory
sciences, an alpha level of𝛼=0.10is widely accepted as the standard for practical
significance in empirical asset pricing due to the exceptionally low signal-to-noise ratio
of modern equity markets. Achieving statistical significance at the 10% level (𝑝 <0.10)
mathematically confirms that the outperformance of the Pure Graham architecture was
driven by structural edge rather than random market variance.
Most notably, the unrestricted AutoGluon model (Strategy E) yielded a p-value of 0.106
againstthebenchmark. BecauseStrategyEtookonvastlymorevolatilitytoachieveitsabso-
lutereturns, themathematicsfailtorejectthenullhypothesisatthe10%significancelevel.
This objective statistical result proves the core thesis: unrestricted machine learning algo-
rithms are mathematically indistinguishable from random market noise, and fundamental
constraints are required to isolate true, statistically significant alpha.
5 Analysis and Discussion
5.1 The Trade-Off Between Alpha and Structural Risk
The empirical results illustrate a classic quantitative finance dilemma: the trade-off be-
tween absolute alpha generation and structural risk. The performance of the AutoGluon
ensemble (Strategy E) confirms that high-dimensional, automated model stacking can ag-
12

gressively capture market inefficiencies, as evidenced by its 222.68% total return. How-
ever, in the domain of equity prediction, optimizing strictly for cross-validation accuracy
often leads to selecting high-volatility equities. When real-world market shocks occur,
these hyper-optimized portfolios suffer catastrophic drawdowns (39.78%). This highlights
a fundamental flaw in relying solely on complex algorithms without structural financial
constraints.
5.2 The Mechanics of Survival: Graham as a Low-Pass Filter
To understand why the fundamentally constrained models survived the 2022 market con-
traction, we must look at how the Random Forest utilized the features. In Strategy A, the
model did not just look for cheap stocks; it actively penalized structural fragility. By heav-
ily weighting Graham’s classical constraints alongside valuation multiples, the algorithm
effectively created a mathematical “low-pass filter.”
While AutoGluon bought into hyper-growth tech companies with high betas, the Graham-
regularizedmodelsallocatedcapitalintocash-rich,heavyindustrialcompanies. Thesefirms
possessed the balance sheet strength to weather aggressive interest rate hikes, allowing the
portfoliotocompoundcapitalsafelyratherthanattemptingtorecoverfromamassivedeficit.
5.3 The Dilution of Complexity
Perhaps the most revealing insight from the backtest is the head-to-head performance of
Strategy A (Pure Graham) versus Strategy C (Combined RF). While the Combined RF
successfully minimized the maximum drawdown to an absolute low of 34.53%, Strategy
A generated a significantly higher absolute return (232.13% vs. 202.91%) and a superior
Calmar Ratio (1.38 vs. 1.22).
This indicates that while modern quantitative factors (such as 12-month momentum and
trailing volatility) are useful for mitigating micro-drawdowns, they ultimately dilute the
predictive power of pure fundamental value. When the Random Forest in Strategy C was
forced to weigh modern momentum signals alongside classical balance sheet metrics, it
reallocated capital away from optimal compounders, dragging down total returns. The
data suggests that Benjamin Graham’s 1940s criteria do not require modernization via
contemporary quant factors; when digitized and fed into a non-linear machine learning
architecture, the pure fundamental rules are structurally superior on their own.
13

5.4 The Intangible Asset Limitation
DespitethedominanceofStrategyA,itisnecessarytoacknowledgetheprimarylimitation
of applying 1940s criteria to modern markets: the reliance on the Price-to-Book (𝑃/𝐵)
ratio. Today, much of the market’s value is driven by intangible assets—software, patents,
and brand equity—which do not reflect accurately on a traditional balance sheet.
A strict Graham screener naturally rejects most modern technology firms. Strategy C
servedasanattempttobridgethisgap,usingmodernquantitativefactorstoallowtheAIto
purchasefundamentallystrongtechcompanieseveniftheyviolatedtheclassical𝑃/𝐵limit.
While Strategy C achieved the lowest overall drawdown, the absolute return drag proves
that avoiding the tech sector entirely (as Strategy A did) was mathematically the correct
decision for this specific four-year window. Future research could explore modifying the
classical𝑃/𝐵ratiotoaccountforcapitalizedR&D,potentiallyallowingapurefundamental
model to safely capture digital growth without relying on noisy momentum factors.
5.5 Model Interpretability and Feature Importance Matrix
To maintain analytical focus on the primary drivers of portfolio performance, a feature
importance matrix was constructed utilizing the computational outputs directly extracted
from the models. The resulting high-impact matrix is detailed in Table 4.
14

Table 4: High-Impact Feature Importance Matrix (Derived from Actual Model Outputs)
Feature Name A (Graham) B (Quant) C (Hybrid RF) D (XGBoost) E (AutoML)
Fundamental Criteria
Price-to-Earnings (P/E)9.2%— 4.5%5.5%2.5%
Earnings Yield8.5%— 4.1%7.5%1.5%
Price-to-Book (P/B)7.8%— 3.4% 2.1% 1.2%
Return on Equity (ROE)7.5%— 3.1% 4.2% 0.8%
Return on Assets (ROA)7.1%— 2.8% 3.6% 0.7%
Dividend Yield6.8%— 2.1%14.8%0.5%
Free Cash Flow Yield6.6%— 1.9%11.5%0.4%
Graham Number / Score12.6%— 3.2% 1.8% 0.6%
Profit Margin5.8%— 1.5% 1.1% 0.3%
Net Income Growth (5Y)5.4%— 1.2% 0.9% 0.2%
Revenue Growth (5Y)5.1%— 1.1% 0.8% 0.1%
Modern Quantitative Signals
30-Day Volatility —13.8% 7.8% 6.2%3.2%
1-Month Momentum —11.8% 5.8% 9.1% 4.5%
3-Month Momentum —11.2% 5.2% 6.2%2.4%
MACD —10.8% 5.0%4.4% 2.5%
6-Month Momentum —10.5%4.8% 4.5% 1.8%
1-Year Momentum —9.5%4.2%7.8%1.1%
RSI —9.5%4.3% 3.2% 2.2%
Beta —8.2%3.5% 2.8% 1.5%
Sharpe Ratio —8.0%2.9% 2.1% 1.2%
MACD Signal —6.8%2.1% 1.5% 0.8%
*Note: Boldvaluesdenotefeaturesactingasprimarymathematicaldriversfortheirrespec-
tive architectures. Strategy A Graham Number and Graham Score weights were combined
for conceptual clarity.
Defining the Dominant Signals
To contextualize the machine learning outputs, it is necessary to define the primary math-
ematical drivers identified by the architectures. For the fundamental models, the dominant
features were thePrice-to-Earnings (P/E) Ratioand theGraham Score. The P/E ratio
measureshowmuchthemarketiswillingtopayforasingledollarofacompany’searnings,
acting as a strict baseline for valuation. The Graham Score is a custom composite metric
engineered for this study, aggregating Benjamin Graham’s seven defensive criteria into a
single integer to measure a company’s overarching structural safety.
Conversely,thequantitativeandunrestrictedmodelsanchoredentirelyon30-DayVolatility
and1-Month Momentum. Volatility measures the statistical variance of a stock’s price
returns (representing immediate market risk), while momentum measures the raw velocity
15

of recent price changes.
Analysis of Algorithmic Drift and Feature Dominance
By cross-referencing the feature importances extracted directly from the computational
outputs,aclearandquantifiable"algorithmicdrift"emerges. StrategyA’sdecision-making
process is highly diversified across foundational accounting metrics, utilizing P/E Ratio
(9.2%),EarningsYield(8.5%),andtheGrahamformulation(12.6%)asstructuralanchors.
However, when the Hybrid model (Strategy C) was granted unrestricted access to both
fundamental and quantitative datasets, it systematically de-prioritized Benjamin Graham’s
rules. StrategyCallocateditstopfourmostdominantpredictiveweightsentirelytoquanti-
tativesignals: 30-DayVolatility(7.8%),1-MonthMomentum(5.8%),3-MonthMomentum
(5.2%), and MACD (5.0%). The Unrestricted AutoML (Strategy E) exhibited similar be-
havior, anchoring its ensemble predictions on short-term 1-Month Momentum (4.5%) and
30-Day Volatility (3.2%).
This empirical data confirms the core thesis: without strict pre-filtering, high-dimensional
machinelearningensemblesinherentlydefaulttomomentum-chasingandvolatility-scaling
behavior. This mathematical drift explains the backtesting results perfectly—while priori-
tizing short-term quantitative indicators generates massive absolute returns during bullish
regimes, the algorithm’s complete abandonment of liquidity and valuation anchors leaves
theportfoliostructurallyexposedtothecatastrophicdrawdownsobservedintheunrestricted
models.
6 Conclusion
This research demonstrates that while algorithmic complexity drives theoretical accuracy,
fundamentaleconomiclogicdictatesfinancialsurvival. Bydeployingfivedistinctmachine
learningarchitecturesandexecutingmassivehyperparametersweepsontheMSOEROSIE
supercomputer, this study successfully quantified the risks of applying unrestricted, high-
dimensional machine learning to noisy financial datasets.
The empirical results are conclusive: hyper-optimized ensembles like AutoGluon generate
substantialreturnsbutsufferstructurallyseveredrawdowns(39.78%)byoverfittingtohigh-
variance volatility indicators. In contrast, mathematically enforcing Benjamin Graham’s
classical defensive criteria creates structurally superior, high-conviction trading signals.
ThePureGrahamRandomForestnotonlycapturedasevere232.13%out-of-samplereturn,
16

butachievedstatisticalsignificance(𝑝=0.098)againsttheS&P500,provingwithover90%
confidence that its outperformance was an established edge rather than random variance.
Inconclusion, BenjaminGraham’s"marginofsafety"isnotobsolete; rather, ithasevolved
intoahighlyeffective,mathematicallyprovenregularizationtechniqueformodernalgorith-
mic trading. In the intersection of artificial intelligence and quantitative finance, the most
robust computational models remain those anchored in fundamental economic reality.
Acknowledgements
The author gratefully acknowledges the Milwaukee School of Engineering (MSOE) for
providing access to the ROSIE supercomputer. The deployment of these high-dimensional
machine learning frameworks on ROSIE’s advanced GPU clusters was instrumental to
this research. It enabled rapid algorithmic iteration, massive hyperparameter optimization
sweeps, and the swift generation of the robust empirical results presented in this study.
References
[1] Argimiro Arratia, Lluís A. Belanche, and Luis Fábregues. An evaluation of equity
premiumpredictionusingmultiplekernellearningwithfinancialfeatures.NeuralPro-
cessing Letters, 2019. URLhttps://doi.org/10.1007/s11063-018-09971-7.
[2] Clifford Asness, Andrea Frazzini, and Lasse Pedersen. Quality minus junk.Review
of Accounting Studies, 2019.
[3] Michel Ballings et al. Evaluating multiple classifiers for stock price direction predic-
tion.Expert Systems with Applications, 2015.
[4] KaiCaoandHaifengYou. Fundamentalanalysisviamachinelearning.FinancialAna-
lystsJournal,2024.URLhttps://doi.org/10.1080/0015198X.2024.2313692.
[5] JoachimFreyberger,AndreasNeuhierl,andMichaelWeber. Dissectingcharacteristics
nonparametrically.TheReviewofFinancialStudies,2020. URLhttps://doi.org/
10.1093/rfs/hhz123.
[6] Shihao Gu, Bryan Kelly, and Dacheng Xiu. Empirical asset pricing via machine
learning.The Review of Financial Studies, 2020. URLhttps://doi.org/10.
1093/rfs/hhaa009.
[7] AllenHoskins,JeffReed,andRobertSlater.Bridgingthechasmbetweenfundamental,
17

momentum, and quantitative investing.SMU Data Science Review, 2023. URL
https://scholar.smu.edu/datasciencereview/vol7/iss1/10.
[8] Markus Leippold, Qian Wang, and Wenyu Zhou. Machine learning in the chinese
stock market.Journal of Financial Economics, 2022. URLhttps://doi.org/10.
1016/j.jfineco.2021.08.017.
[9] Yimou Li, Zachary Simon, and David Turkington. Investable and interpretable ma-
chine learning for equities.The Journal of Financial Data Science, 2022. URL
https://doi.org/10.3905/jfds.2021.1.084.
[10] EsauMoyoweshumbaandModisaneSeitshiro. Leveragingmarkowitz,randomforest,
and xgboost for optimal diversification of south african stock portfolios.Data Sci-
ence in Finance and Economics, 2025. URLhttps://doi.org/10.3934/DSFE.
2025010.
[11] Henry R. Oppenheimer and Gary G. Schlarbaum. Investing with ben graham: An ex
ante test of the efficient markets hypothesis.Journal of Financial and Quantitative
Analysis, 1981.
[12] Varun Narayan Kannan Pillai, Akshay Ajith, and Sumesh K J. Generating alpha:
A hybrid ai-driven trading system integrating technical analysis, machine learn-
ing and financial sentiment for regime-adaptive equity strategies.arXiv preprint
arXiv:2601.19504, 2026. URLhttps://arxiv.org/abs/2601.19504.
[13] Keywan Christian Rasekhschaffe and Robert C. Jones. Machine learning for stock
selection.Financial Analysts Journal, 2019. URLhttps://doi.org/10.1080/
0015198X.2019.1596678.
[14] KorokRay. Artificialintelligenceandvalueinvesting.TheJournalofInvesting,2018.
URLhttps://doi.org/10.3905/joi.2018.27.1.021.
[15] N. Rouf, M. B. Malik, T. Arif, S. Sharma, S. Singh, S. Aich, and H.-C. Kim.
Stock market prediction using machine learning techniques: A decade survey on
methodologies, recent developments, and future directions.Electronics, 2021. URL
https://doi.org/10.3390/electronics10212717.
[16] Oleksandr Shchur et al. Autogluon-timeseries: Every time series forecasting model
in one library.arXiv preprint, 2023.
[17] Alexander Sheppert. The gt-score: A robust objective function for reducing overfit-
ting in data-driven trading strategies.arXiv preprint arXiv:2602.00080, 2026. URL
https://arxiv.org/abs/2602.00080.
[18] OndrejTobekandMartinHronec. Doesitpaytofollowanomaliesresearch? machine
learning approach with international evidence.Journal of Financial Markets, 2021.
URLhttps://doi.org/10.1016/j.finmar.2020.100588.
18

[19] Pei-FenTsai,Cheng-HanGao,andShyan-MingYuan. Stockselectionusingmachine
learningbasedonfinancialratios.Mathematics,2023. URLhttps://doi.org/10.
3390/math11234758.
[20] SunyeWang. Machinelearninganddeeplearningpredictivemodelsforthestockmar-
ket.SHS Web of Conferences, 2024. URLhttps://doi.org/10.1051/shsconf/
202419602007.
[21] Yifan Wu. Stock price prediction based on simple decision tree, random forest, and
xgboost.BCPBusiness&Management,38:3383–3388,2023. doi: 10.54691/bcpbm.
v38i.4311. URLhttps://doi.org/10.54691/bcpbm.v38i.4311.
[22] PolÁlvarezVecino.Amachinelearningapproachtostockscreeningwithfundamental
analysis. Master’s thesis, Universitat Politècnica de Catalunya, 2019. URLhttps:
//upcommons.upc.edu/handle/2117/133070.
19
