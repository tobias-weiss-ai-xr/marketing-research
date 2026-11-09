---
title: Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
url: https://arxiv.org/abs/2606.25811
category: ai-marketing
subcategory: measurement
date: 2026-06
venue: ''
authors:
- Yoonsik Hong
- Diego Klabjan
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.25811
pages: 26
chars: 92602
fetched_at: '2026-11-08T13:27:14+00:00'
kb_version: 1
---

# Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets

Hierarchical Graph Learning for Calendar Spread Strategies
in Commodity Futures Markets
Yoonsik Hong1,∗, Diego Klabjan1
Abstract
Commodityfuturescanberepresentedhierarchically,withunderlyingassetsattheupperlevel
and individual futures contracts at the lower level. Entities at each level can be connected by
edges reflecting inherent correlations, with cross-level edges capturing contract-to-underlying
asset connections. Building on our observations of these structures, we propose a hierarchical
graph learning approach for calendar spread (CS) strategies in commodity futures markets,
addressing two significant gaps in the machine-learning literature: (i) the absence of learning-
based methods for CS strategies in futures markets, and (ii) the lack of consideration of
maturity-dependentinterrelationshipsacrosscommodityfutures.Wefirstestablishtheefficacy
of CS strategies by analytically showing that CS strategies can possess higher risk-adjusted
returns, measured by the information ratio, and lower risk, measured by variance and delta,
than long-only strategies. We then introduce a method to convert learning-based predictions
into CS positions. Next, we develop a hierarchical graph learning method that predicts futures
pricemovementsbyutilizingthematurity-dependentinterrelationships,therebyyieldingaCS
tradingalgorithm.EmpiricalresultsoncommodityfuturesmarketstradedontheChicagoMer-
cantile Exchange Group demonstrate that our method outperforms benchmark models in both
prediction and trading performance. Wefind that maturity-dependent interrelationships across
commodity futures are instrumental in prediction and that CS trading based on hierarchical
graph learning is effective for statistical arbitrage.
Keywords:Calendar Spread Strategy, Graph Learning, Statistical Arbitrage, Commodity
Futures, Deep Learning
1. Introduction
We address the problem of exploiting statistical arbitrage opportunities in commodity futures markets through a
calendar spread (CS) strategy based on hierarchical graph learning that captures information embedded in maturity-
dependent interrelationships across commodity futures. A futures contract is an agreement between two parties in
which the contract price is fixed at initiation, and at maturity, one party delivers the underlying asset (or settles in
cash), while the other pays the predetermined price (Hull, Treepongkaruna, Colwell, Heaney and Pitt, 2013). If the
underlyingassetisacommodity,thecontractisreferredtoasacommodityfuturescontract.Statisticalarbitragerefers
to cash flows that generate profits by exploiting mispricing under acceptable risk (Lazzarino, Berrill, Šević et al.,
2018),anddeep-learning–basedapproachesforcapturingsuchopportunitieshavebeenactivelystudiedacrossvarious
financialmarkets(e.g.,Guijarro-Ordonez,PelgerandZanotti(2025);HongandKlabjan(2025a)).Toexploitstatistical
arbitrageincommodityfuturesmarkets,weemployaCSstrategythattakeslongandshortpositionsinfuturescontracts
with the same underlying commodity but different times to maturity (TTMs).
No prior learning-based studies address CS trading, despite its widespread use and extensive empirical studies
in futures markets (Clarke, De Silva and Thorley, 2013; Szymanowska, De Roon, Nijman and Van Den Goorbergh,
2014;BoonsandPrado,2019;CMEGroup,n.d.b).Tradingstrategiesinexistinglearning-basedfuturesstudies—such
as single-contract directional trading and top-K selection—are highly likely to be exposed to underlying asset price
risk. Such exposure to volatile underlying price movements, rather than relatively stable cost-of-carry components
(e.g., interest rates and storage costs), can deteriorate risk-adjusted trading performance. Motivated by this limitation,
∗Corresponding author
1Department of Industrial Engineering and Management Sciences, Northwestern University, Evanston, 60208, IL, USA
YoonsikHong2028@u.northwestern.edu(Y. Hong);d-klabjan@northwestern.edu(D. Klabjan)
Y. Hong and D. Klabjan, Preprint, June 25, 20261arXiv:2606.25811v1  [q-fin.TR]  24 Jun 2026

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
we show that CS strategies can mitigate risk and yield superior risk-adjusted returns. We also introduce a method to
convert learning-based predictions into CS positions.
Most existing learning-based studies overlook TTM-dependent interrelationships across commodity futures.
Commodity futures contracts are economically linked (Chng, 2009; Vacha, Janda, Kristoufek and Zilberman, 2013;
Cai, Fang, Chang, Tian and Hamori, 2020; Furlong and Ingenito, 1996; Hammoudeh, Sari and Ewing, 2009; Boakye,
HeimonenandJunttila,2024;Liu,Lu,ZongandXie,2023),butthisstructureisrarelyincorporatedintolearning-based
models.Althoughsomerecentstudies(Hu,Tan,LiuandYin,2025;Tan,Hu,LiuandYin,2024)adoptgraphlearning
tomodelrelationshipsamongcommodityfutures,theydonotdistinguishtheserelationshipsbyTTM.However,these
relationships are inherently TTM-dependent (Brennan, 1976; Gibson and Schwartz, 1990; Schwartz, 1997; Casassus
andCollin-Dufresne,2005).Forexample,gasolineanddieselinventoriesmayremainlowforthreemonthsduetoawar,
but they are expected to recover after six months as supply chains recover. When predicting the price of diesel futures
withasix-monthTTM,thepriceinformationofgasolinefutureswithathree-monthTTMshouldnotbetreatedinthe
same way as that of gasoline futures with a six-month TTM. Ignoring TTM thus limits the ability of graph-learning
modelstocaptureTTM-dependentinformation.Toaddressthisgap,weproposeahierarchicalgraphlearningapproach.
First,weverifytheefficacyofCSstrategiesintermsofriskandrisk-adjustedreturn.Wetheoreticallyestablishtheir
advantages over long-only (LO) strategies. Since any trading position can be expressed as a linear combination of CS
andLOpositions,wecomparethetwostrategies.WeshowthatCSstrategiespossesslowervarianceandriskexposure
than LO strategies under some assumptions. Moreover, we show that if an LO strategy outperforms an uninformed
strategy by a certain threshold, then a CS strategy derived from the LO strategy outperforms the LO strategy in terms
ofrisk-adjustedreturn.Wealsopresentamethodtoassesswhethertheassumptionsarerealistic.Wefurtherintroduce
a method to map learning-based predictions into CS positions.
Next, we develop a hierarchical graph learning approach that captures maturity-dependent relationships across
commodity futures. We construct a bi-level graph in which underlying commodities form upper-level nodes and
individual futures contracts form lower-level nodes, connected via cross-commodity, commodity-contract, and cross-
contract relationships. Since commodities do not share a common contract maturity grid, we introduce a graph
lifting method that constructs TTM-aligned virtual futures nodes for each commodity on a virtual TTM grid shared
across commodities. On this lifted graph, we design a bi-level convolution architecture that alternates between (i)
propagatinginformationacrosscommoditiesthroughvirtualfuturesatthesameTTM(TTM-alignedpropagation)and
(ii) capturing intra-commodity term structure dynamics via message passing over neighboring maturities (different-
TTM propagation). By distinguishing relationships based on TTM through distinct parameterizations and iteratively
integrating information across both dimensions, the proposed method captures interrelationships across commodity
futures while explicitly accounting for maturity dependence.
Our experiments demonstrate that the proposed method generates statistical arbitrage and that both CS strategies
and maturity-dependent interrelationships are effective. We provide evidence that CS strategies can exhibit lower
variance, lower exposure risk, and higher IRs than LO strategies in commodity futures markets. Our hierarchical
graph learning achieves the lowest mean squared error with statistical significance, and its CS trading attains the best
risk-adjusted returns by capturing TTM-dependent interrelationships among commodity futures, compared to other
learning-based methods that either ignore such interrelationships or do not account for their maturity dependence.
This paper makes the following main contributions.
•To the best of our knowledge, this study is the first to propose a hierarchical graph learning approach for
predicting commodity futures price movements while accounting for maturity-dependent interrelationships
across commodity futures.
•We establish the efficacy of calendar spread strategies by presenting propositions showing that they can exhibit
higherinformationratios,lowervariance,andlowerexposureriskthanlong-onlystrategiesincommodityfutures
markets.
•Empirical results show that the hierarchical graph learning method outperforms benchmark methods with
statisticalsignificanceinpredictiontasks.Wefindthatmaturity-dependentinterrelationshipsacrosscommodity
futures are instrumental in predictive performance.
•OurcalendarspreadstrategyattainsdailyinformationandSortinoratiosof0.0846and0.1241,correspondingto
improvementsof 96%and82% overthebenchmarks, and75%and113% overtheS&P 500,respectively.These
Y. Hong and D. Klabjan, Preprint, June 25, 2026 2

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
results indicate that calendar spread trading based on hierarchical graph learning in futures markets is effective
for statistical arbitrage.
2. Related Work
No learning-based studies address CS strategies in futures markets. Existing work applies various learning-based
methods to prediction and trading, including LSTM and GRU models (Li, Li, Liu, Zhu and Wei, 2022; Zhang,
Wang and Wang, 2020; Hung and Chen, 2021), econometric regression (Wang and Zhang, 2024; Angelidis, Sakkas
and Tessaromatis, 2025), reinforcement learning (Gabrielsson and Johansson, 2015; Massahi and Mahootchi, 2024;
Kaur, Sidhu and Bhathal, 2025), clustering-based approaches (Fengqian and Chao, 2020), and AI-agent systems
incorporating vision-language models (Wang, Wu, Zhang, Tan, Chen and Lin, 2025). These studies span agricultural
futures (Li et al., 2022; Liu et al., 2023; Wang et al., 2025; Fengqian and Chao, 2020), energy futures (Zhang et al.,
2020; Sun, Wang, Ni, Cao and Liu, 2019; Hu et al., 2025; Baruník and Malinska, 2016), metal futures (Massahi
and Mahootchi, 2024; Kaur et al., 2025; Fengqian and Chao, 2020; Sun et al., 2019; Tan et al., 2024), equity index
futures (Hung and Chen, 2021; Gabrielsson and Johansson, 2015; Fengqian and Chao, 2020), and broad cross-market
commodity universes (Wang and Zhang, 2024; Angelidis et al., 2025). Many learning-based studies focus solely on
price or return prediction (Li et al., 2022; Zhang et al., 2020; Hung and Chen, 2021), while trading-oriented work
considers single-contract directional trading (Gabrielsson and Johansson, 2015; Fengqian and Chao, 2020; Wang
et al., 2025; Massahi and Mahootchi, 2024; Kaur et al., 2025; Sun et al., 2019), top-K trading (Hu et al., 2025),
cross-commoditylong-shorttrading(WangandZhang,2024;Angelidisetal.,2025),orcross-commoditypairstrading
(Liu et al., 2023). However, none of the prior learning-based work addresses CS strategies. We conjecture that a key
reason is the lack of clear theoretical guarantees on the efficacy of CS strategies, despite their widespread empirical
use in futures markets (Clarke et al., 2013; Szymanowska et al., 2014; Boons and Prado, 2019; CME Group, n.d.b).
Accordingly,weprovidetheoreticaljustificationanddemonstratethatCStradingbasedonhierarchicalgraphlearning
is effective compared with benchmark methods.
Existing learning-based studies largely overlook TTM-dependent interrelationships across commodity futures.
Futures contracts across different commodities are economically interconnected through production chains (Chng,
2009), substitution and complementarity effects (Vacha et al., 2013), and shared macroeconomic drivers (Cai et al.,
2020; Furlong and Ingenito, 1996; Hammoudeh et al., 2009; Boakye et al., 2024; Liu et al., 2023) (e.g., oil and
agricultural markets (Ji and Fan, 2012; Mitchell, 2008; Nazlioglu, 2011)), yet most learning-based approaches treat
contracts in isolation. Although a few recent studies (Hu et al., 2025; Tan et al., 2024) incorporate cross-futures
relationshipsthroughgraphlearning,theytreatcommodityfuturescontractsasgenericnodesandconstructconnections
without conditioning on TTM. However, interrelationships across commodity futures are inherently TTM-dependent,
as contracts with different TTMs exhibit heterogeneous sensitivities to inventory conditions, short-term supply
disruptions, production constraints, and long-run demand and substitution dynamics (Brennan, 1976; Gibson and
Schwartz,1990;Schwartz,1997;CasassusandCollin-Dufresne,2005).IgnoringTTMthusconflatesdistincteconomic
channels and limits the ability of graph architectures to capture TTM-dependent relationships across commodity
futures. Their methods (Hu et al., 2025; Tan et al., 2024) also cannot address node birth and death, as their focus
on high-frequency trading assumes a fixed contract universe. In contrast, we consider daily trading, where node birth
and death arise naturally from contract maturities. Through our hierarchical graph learning method, we highlight the
importanceofTTMdependenceincommodityfuturesinterrelationshipsanddemonstratetheinstrumentalroleofsuch
interrelationships.
3. Notation and Preliminaries
For a finite setand vectors𝐱 𝑖 ∈ℝ 𝑝 for𝑖∈, let[𝐱 𝑖]𝑖∈ ∈ℝ ||×𝑝 denote the row-wise stacked matrix in
lexicographicalorderof.Foranindexset,if𝑥 𝑖∈ℝisdefinedfor𝑖∈ ′⊂andnotdefinedfor𝑖∈⧵ ′,welet
sum(𝑥𝑖;𝑖∈),avg(𝑥 𝑖;𝑖∈)andstd(𝑥 𝑖;𝑖∈)denotethesum,average,andstandarddeviationover ′,respectively.
We denote by𝕀{⋅} the indicator function. For𝑎≤𝑏, let[𝑎∶𝑏],[𝑎∶𝑏),(𝑎∶𝑏], and(𝑎∶𝑏)denote the corresponding
integer intervals. For𝐱= [𝑥𝑖]𝑖∈[1∶𝑛] ∈ℝ 𝑛, we definecdf(𝑥;𝐱) = 1 𝑛 ∑𝑛 𝑖=1 𝕀{𝑥𝑖≤𝑥} and ̂cdf(𝑥;𝐱) = 1 𝑛+𝜖 ∑𝑛 𝑖=1 𝕀{𝑥𝑖≤𝑥}
where𝜖 >0is a small constant. For any random variable𝑋, let ̃𝑋denote a realization and ̂𝑋denote its mean
estimate. Let𝟏denote a vector of ones. For𝑥∈ℝ, define[𝑥]+ = max{0,𝑥}. We let𝑊⋅ and𝐛 ⋅ denote a real-valued
Y. Hong and D. Klabjan, Preprint, June 25, 2026 3

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
learnable parameter matrix and a real-valued learnable bias vector, respectively, where the subscripts indicate their
indices, and let𝜙denote an activation function.
We index trading dates by𝑡∈ℕin chronological order, without skipped integers. Let⊂ℕdenote the index
set of commodities, withmax=||. For each𝑐∈, let 𝑐 ⊂ℕdenote the index set of futures contracts with
underlying commodity𝑐, ordered by increasing maturity, and satisfyingmax𝑐 =| 𝑐|. We denote a futures contract
by(𝑐,𝑑)∈× 𝑐 with maturity𝑇𝑐𝑑. We denote by𝑐 ={𝑇 𝑐𝑑 ∶𝑑∈ 𝑐}the maturity grid of commodity𝑐∈. We
refer to𝑇𝑐𝑑 −𝑡as the TTM of contract(𝑐,𝑑)at time𝑡∈ℕ.
For𝑡∈ℕand𝑐∈, we let𝑆 𝑡𝑐 >0denote the price of commodity𝑐at time𝑡, with return𝑅𝑡𝑐 =𝑆 𝑡𝑐∕𝑆𝑡−1,𝑐−1.
We assume that𝑆𝑡𝑐 is defined for all𝑡∈ℕand𝑐∈. For𝑡∈ℕand(𝑐,𝑑)∈× 𝑐, let𝑉𝑡𝑐𝑑 ≥0denote the trading
volume of futures contract(𝑐,𝑑)at time𝑡, and let𝐹𝑡𝑐𝑑 >0denote its price at time𝑡for all𝑡≤𝑇 𝑐𝑑. Assume that the
margin ratio is one for every position (long or short) across all contracts and time, and that there are no transaction
costs. The return of futures contract(𝑐,𝑑)is then defined as𝑅𝑡𝑐𝑑 =𝐹 𝑡𝑐𝑑∕𝐹𝑡−1,𝑐𝑑 −1when𝑡≤𝑇 𝑐𝑑. We assume that
all𝑆 𝑡𝑐,𝑅 𝑡𝑐,𝑉 𝑡𝑐𝑑,𝐹 𝑡𝑐𝑑, and𝑅𝑡𝑐𝑑 are random variables, and that, for all(𝑐,𝑑)∈×𝑐 and𝑡≤𝑇 𝑐𝑑,
𝔼|𝑅𝑡𝑐𝑑|<∞,𝔼𝑅 2 𝑡𝑐𝑑 <∞,andVar(𝑅 𝑡𝑐𝑑)>0.(1)
We define the history at time𝑡as 𝑡 = {(𝑡′, ̃𝐻𝑡′) ∶𝑡 ′ ∈ [1 ∶𝑡]}, where ̃𝐻𝑡′ = {(𝑐,𝑑, ̃𝑉𝑡′𝑐𝑑, ̃𝐹𝑡′𝑐𝑑) ∶ (𝑐,𝑑) ∈
× 𝑐, ̃𝑉𝑡′𝑐𝑑 >0}is an observable sample at𝑡′.
The price of a futures contract(𝑐,𝑑)∈× 𝑐 at time𝑡is expressed as
𝐹𝑡𝑐𝑑 =𝑆 𝑡𝑐exp(𝑄𝑡𝑐𝑑(𝑇𝑐𝑑 −𝑡))>0(2)
where the random variable𝑄𝑡𝑐𝑑 ∈ℝis the net cost-of-carry rate. Its return is then expressed as
𝑅𝑡𝑐𝑑 =(1+𝑅 𝑡𝑐)exp(𝐴𝑡𝑐𝑑)−1(3)
where𝐴𝑡𝑐𝑑 =𝑄 𝑡𝑐𝑑(𝑇𝑐𝑑−𝑡)−𝑄 𝑡−1,𝑐𝑑(𝑇𝑐𝑑−𝑡+1)representsthechangeinthecarrycostfrom𝑡−1to𝑡.Thespotdelta
of(𝑐,𝑑)is
Δ𝑡𝑐𝑑 = 𝜕𝐹𝑡𝑐𝑑 𝜕𝑆𝑡𝑐 =exp(𝑄 𝑡𝑐𝑑(𝑇𝑐𝑑 −𝑡))>0,(4)
which represents the risk exposure to the underlying commodity price (Hull et al., 2013).
Wedefinethesetofcontractsobservablefrom𝑡−1to𝑡as𝑈 𝑡={(𝑐,𝑑)∈× 𝑐 ∶𝑉 𝑡𝑐𝑑𝑉𝑡−1,𝑐𝑑 >0}with𝑛 𝑡=|𝑈 𝑡|.
Let𝐶𝑡={𝑐∶(𝑐,𝑑)∈𝑈 𝑡}and𝐷 𝑡𝑐 ={𝑑∶(𝑐,𝑑)∈𝑈 𝑡}denote the corresponding sets of commodities and contracts,
respectively, with𝑛𝑡𝑐 =|𝐷 𝑡𝑐|. We denote the realization of𝑈𝑡 by ̃𝑈𝑡 = {(𝑐,𝑑) ∈× 𝑐 ∶ ̃𝑉𝑡𝑐𝑑 ̃𝑉𝑡−1,𝑐𝑑 >0}, and
define ̃𝐶𝑡, ̃𝐷𝑡𝑐,̃ 𝑛𝑡,and̃ 𝑛𝑡𝑐,analogously.Wedenotethetradinguniverseattime𝑡by ̂𝑈𝑡⊂{(𝑐,𝑑)∈× 𝑐 ∶𝑡≤𝑇 𝑐𝑑},
and define ̂𝐶𝑡, ̂𝐷𝑡𝑐, ̂ 𝑛𝑡, and̂ 𝑛𝑡𝑐 analogously. Note that̂𝑈𝑡 is determined at𝑡−2. In the following, we consider a single
investor implementing our method.
4. Proposed Method
To exploit statistical arbitrage in commodity futures markets, we propose a hierarchical graph learning method to
predict futures price movements for CS trading. We first formally define a CS strategy, establish its efficacy through
theoreticalpropositions,andintroduceaprojectionmethodthatmapspredictionsintoCSpositions.Wethenformulate
the prediction problem for CS trading and develop a hierarchical graph learning architecture that captures TTM-
dependent interrelationships among commodity futures.
4.1. Calendar Spread Strategy
For𝑡∈ℕand𝑐∈ ̂𝐶𝑡, we define a CS strategy for𝑐as a trading strategy that yields a position weight vector
𝐰𝑡𝑐 =[𝑤 𝑡𝑐𝑑]𝑑∈ ̂𝐷𝑡𝑐 ∈ℝ ̂ 𝑛𝑡𝑐 such that𝟏⊤𝐰𝑡𝑐 =0and‖𝐰 𝑡𝑐‖1=1. This implies symmetric long and short positions:
∑
𝑑∈ ̂𝐷𝑡𝑐
[𝑤𝑡𝑐𝑑]+= ∑
𝑑∈ ̂𝐷𝑡𝑐
[−𝑤𝑡𝑐𝑑]+= 1 2.(5)
Y. Hong and D. Klabjan, Preprint, June 25, 2026 4

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
We let 𝑡𝑐,CS = {𝐰𝑡𝑐 ∈ℝ ̂ 𝑛𝑡𝑐 ∶𝟏 ⊤𝐰𝑡𝑐 = 0,‖𝐰 𝑡𝑐‖1 = 1}denote the set of CS weights for𝑐at𝑡, and
𝑡𝑐,LO = {𝐰𝑡𝑐 ∈ℝ ̂ 𝑛𝑡𝑐 ∶𝑤 𝑡𝑐𝑑 ≥0,‖𝐰 𝑡𝑐‖1 = 1}denote the set of LO weights for𝑐at𝑡. Since any position can
be expressed as a linear combination of CS and LO positions, we focus on these two classes.
We evaluate both classes of strategies in terms of their risk and risk-adjusted return. For𝑡∈ℕand𝑐∈ ̂𝐶𝑡, a
position weight vector𝐰𝑡𝑐 =[𝑤 𝑡𝑐𝑑]𝑑∈ ̂𝐷𝑡𝑐 ∈ℝ ̂ 𝑛𝑡𝑐 is determined by an investor at𝑡−2, built in markets at𝑡−1. Then, the resulting position is cleared at𝑡, yielding the return given by
Π(𝐰𝑡𝑐)=
∑
𝑑∈ ̂𝐷𝑡𝑐
𝑤𝑡𝑐𝑑𝑅𝑡𝑐𝑑 (6)
Note thatΠ(𝐰𝑡𝑐)depends on𝑅 𝑡𝑐𝑑; for simplicity, we omit this dependence. Moreover, we define the return variance
of𝐰 𝑡𝑐 asVar(Π(𝐰 𝑡𝑐)), the IR of𝐰𝑡𝑐 asIR(Π(𝐰 𝑡𝑐)) =𝔼(Π(𝐰𝑡𝑐))∕
√
Var(Π(𝐰𝑡𝑐))ifVar(Π(𝐰 𝑡𝑐))>0, and the delta of
𝐰𝑡𝑐 as
Δ(𝐰𝑡𝑐)= 𝜕 𝜕𝑆𝑡−1,𝑐 ( ∑
𝑑∈ ̂𝐷𝑡𝑐
𝑤𝑡𝑐𝑑𝐹𝑡−1,𝑐𝑑)=
∑
𝑑∈ ̂𝐷𝑡𝑐
𝑤𝑡𝑐𝑑Δ𝑡−1,𝑐𝑑.(7)
Risk is commonly measured by return variance (Markowitz, 1952) or by delta (Hull et al., 2013), and investment
objectives are often framed as maximizing risk-adjusted return (Sharpe, 1966, 1998). Thus, we analyze LO and CS
strategies under these metrics in Propositions 1 to 3, with proofs in Appendix Section A.
Proposition 1 implies that CS strategies can have lower variance than LO strategies, thereby entailing lower risk.
Since the variance of𝑅𝑡𝑐𝑑 is driven more by the underlying commodity return𝑅𝑡𝑐 than by the cost-of-carry change
𝐴𝑡𝑐𝑑 in Eq. (3) (Gospodinov and Ng, 2013; Maslyuk and Smyth, 2009), returns of contracts with the same underlying
commoditytendtobepositivelycorrelated.Basedonthisproperty,weassumethatsuchcorrelationsadmitnonnegative
lower bounds in Proposition 1. Part (i) shows that an LO position has higher variance than all CS positions when
correlations exceed a threshold depending on the LO position. Part (ii) removes this dependence and shows that all
CS positions have lower variance than all LO positions when correlations exceed a bound determined by the variance
range ratio and the number of contracts.
Proposition 1.Fix𝑡∈ℕand𝑐∈ ̂𝐶𝑡. For𝑑,𝑑 ′ ∈ ̂𝐷𝑡𝑐, let𝜎𝑡𝑐𝑑𝑑′ = Cov(𝑅𝑡𝑐𝑑,𝑅𝑡𝑐𝑑′),𝜌 𝑡𝑐𝑑𝑑′ = Corr(𝑅𝑡𝑐𝑑,𝑅𝑡𝑐𝑑′) =
𝜎𝑡𝑐𝑑𝑑′∕√𝜎𝑡𝑐𝑑𝑑𝜎𝑡𝑐𝑑𝑑′, and𝜅2 𝑡𝑐 =(max 𝑑∈ ̂𝐷𝑡𝑐 𝜎𝑡𝑐𝑑𝑑)∕(min𝑑∈ ̂𝐷𝑡𝑐 𝜎𝑡𝑐𝑑𝑑).
(i)Ifmin 𝑑,𝑑′∈ ̂𝐷𝑡𝑐 𝜌𝑡𝑐𝑑𝑑′ ≥0and𝐰∈ 𝑡𝑐,LO( ̂𝐷𝑡𝑐)satisfies
min
𝑑,𝑑′∈ ̂𝐷𝑡𝑐
𝜌𝑡𝑐𝑑𝑑′ >(𝜅 2 𝑡𝑐−2‖𝐰‖2 2)(3−2‖𝐰‖ 2 2)−1,(8)
then for all𝐰′∈ 𝑡𝑐,CS( ̂𝐷𝑡𝑐),Var(Π(𝐰))>Var(Π(𝐰 ′)).
(ii)Ifmin 𝑑,𝑑′∈ ̂𝐷𝑡𝑐 𝜌𝑡𝑐𝑑𝑑′ ≥0and
min
𝑑,𝑑′∈ ̂𝐷𝑡𝑐
𝜌𝑡𝑐𝑑𝑑′ >(𝜅 2 𝑡𝑐̂ 𝑛𝑡𝑐−2)(3̂ 𝑛𝑡𝑐−2)−1,(9)
then for all(𝐰,𝐰′)∈ 𝑡𝑐,LO( ̂𝐷𝑡𝑐)× 𝑡𝑐,CS( ̂𝐷𝑡𝑐),Var(Π(𝐰))>Var(Π(𝐰 ′)).
Proposition 2 shows that if the expected return of an LO strategy𝐰exceeds that of the uninformed equal-weight
strategy ̄𝐰by a threshold, then the CS strategy̌𝐰derived from𝐰attains a positive IR that exceeds that of the LO
strategy.TheCSweightvector ̌𝐰isobtainedbydemeaningandrescaling𝐰,therebypreservingtherelativeorderingof
weightswhilesatisfyingtheCSconstraints.BecauseVar(Π( ̌𝐰))≥0inpart(ii),thefirstinequalityineachpartensures
thatΠ(𝐰)hasnonzerovariance.Since𝐰≥0,thisnonzero-varianceconditiontypicallyholdswhencontractswiththe
same underlying commodity are positively correlated, as is commonly observed in the market (see Proposition 1).
Moreover,thefirstinequalityinpart(ii)issatisfiedunderProposition1,forinstance.Thesecondinequalityinparts(i)
and (ii) excludes the degenerate case addressed in part (iii). Each part specifies a threshold on𝔼Π(𝐰)−𝔼Π(̄𝐰)under
different conditions: the variance ratio in (i), the position difference in (ii), and zero in (iii). In part (iii),̌𝐰yields a
risk-free arbitrage, which can be viewed as having an infinite IR, and in parts (i) and (ii), the CS strategy achieves a
positiveIRthatexceedsthatoftheLOstrategy.Therefore,ifanLOstrategyexceedstheuninformedbenchmarkbeyond
Y. Hong and D. Klabjan, Preprint, June 25, 2026 5

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
the corresponding threshold, investing in the LO position is inferior to the derived CS position. Since CS positions
aredollar-neutral,theirSharpeandinformationratioscoincide,whereastheSharpebenchmarkforLOpositionsisthe
risk-free rate (Sharpe, 1966, 1998). Thus, Proposition 2 also implies that CS strategies can attain higher Sharpe ratios
than LO strategies.
Proposition 2.Fix𝑡∈ℕand𝑐∈ ̂𝐶𝑡. Let𝐰∈ 𝑡𝑐,LO, ̄𝐰=𝟏∕̂ 𝑛𝑡𝑐 ∈ 𝑡𝑐,LO, anď𝐰=(𝐰− ̄𝐰)∕‖𝐰− ̄𝐰‖1 ∈ 𝑡𝑐,CS
with𝐰≠ ̄𝐰.
(i)IfVar(Π(𝐰))>0,Var(Π(𝐰− ̄𝐰))>0, and
𝔼Π(𝐰)−𝔼Π( ̄𝐰)>[𝔼Π(𝐰)] +√ Var(Π(𝐰− ̄𝐰))∕Var(Π(𝐰)),(10)
thenIR(Π( ̌𝐰))>[IR(Π(𝐰))] +.
(ii)IfVar(Π(𝐰))>Var(Π( ̌𝐰)),Var(Π(𝐰− ̄𝐰))>0, and
𝔼Π(𝐰)−𝔼Π( ̄𝐰)>‖𝐰− ̄𝐰‖1[𝔼Π(𝐰)]+,(11)
thenIR(Π( ̌𝐰))>[IR(Π(𝐰))] +.
(iii)IfVar(Π(𝐰))>0,Var(Π(𝐰− ̄𝐰))=0, and
𝔼Π(𝐰)−𝔼Π( ̄𝐰)>0, (12)
then𝔼Π( ̌𝐰)>0,Var(Π( ̌𝐰))=0andIR(Π(𝐰))<∞.
Proposition 3 implies that CS strategies can have lower risk exposure to the underlying commodity price. Part (i)
gives a condition under which the CS weight vectoř𝐰, obtained by demeaning an LO vector𝐰and scaling, has lower
delta. In particular, if‖𝐰−̄𝐰‖1 ≥1, then ̌𝐰always has lower risk exposure regardless ofΔ(𝐰)andΔ(̄𝐰), as both are
positive by Eq. (4). Under the assumption that the delta range ratio,Δmax 𝑡−1,𝑐∕Δmin 𝑡−1,𝑐, is less than three, part (ii) implies
that, almost surely, every CS strategy is less exposed to the underlying commodity price than every LO strategy.
Proposition 3.Fix𝑡∈ℕand𝑐∈ ̂𝐶.
(i)Let𝐰∈ 𝑡𝑐,LO, ̄𝐰=𝟏∕̂ 𝑛𝑡𝑐 ∈ 𝑡𝑐,LO, and ̌𝐰= (𝐰− ̄𝐰)∕‖𝐰− ̄𝐰‖1 ∈ 𝑡𝑐,CS with𝐰≠ ̄𝐰. IfΔ( ̄𝐰)>
(1−‖𝐰− ̄𝐰‖1)Δ(𝐰), thenΔ(̌𝐰)<Δ(𝐰).
(ii)Assume thatΔ 𝑡−1,𝑐𝑑 is an a.s. finite random variable for every𝑑∈̂𝐷𝑡𝑐. LetΔmin 𝑡−1,𝑐 = min{essinfΔ𝑡−1,𝑐𝑑 ∶𝑑∈
̂𝐷𝑡𝑐}∈ℝandΔ max 𝑡−1,𝑐 =max{esssupΔ 𝑡−1,𝑐𝑑 ∶𝑑∈ ̂𝐷𝑡𝑐}∈ℝ. If3Δ min 𝑡−1,𝑐 >Δ max 𝑡−1,𝑐, then
essinf
𝐰∈𝑡𝑐,LO
Δ(𝐰)>esssup
𝐰∈tc,CS
Δ(𝐰)(13)
We assess the realism of the inequality assumptions in the second parts of Propositions 1 and 3 by estimating the
relevant parameters in the trading universê𝑈𝑡. Sincê𝑈𝑡 is determined based on𝑡−2, as discussed below in Eq. (25),
somecontractsin ̂𝑈𝑡 maynotbeobservableat𝑡−1or𝑡,i.e., ̃𝑉𝑡−1,𝑐𝑑 ̃𝑉𝑡𝑐𝑑 =0.Thus,inthepropositions,wereplace ̂𝐷𝑡𝑐,
̂ 𝑛𝑡𝑐, and̂𝐶𝑡 with ̂𝐷′ 𝑡𝑐 = ̂𝐷𝑡𝑐∩ ̃𝐷𝑡𝑐,̂ 𝑛′ 𝑡𝑐 =| ̂𝐷′ 𝑡𝑐|, and̂𝐶′ 𝑡 ={𝑐∈ ̂𝐶𝑡∩ ̃𝐶𝑡∶̂ 𝑛′ 𝑡𝑐 >1}, respectively. For a CS strategy to be
implemented,atleasttwocontractsonthesameunderlyingassetarerequired;thus,weimposetheconstraint̂ 𝑛 ′ 𝑡𝑐 >1in
̂𝐶′ 𝑡.Foreach𝑡∈ℕ,𝑐∈ ̂𝐶′ 𝑡,and(𝑑,𝑑 ′)∈ ̂𝐷′ 𝑡,𝑐× ̂𝐷′ 𝑡,𝑐,weestimatê 𝜎𝑡𝑐𝑑𝑑′ asthesamplecovarianceof{( ̃𝑅𝑡′𝑐𝑑, ̃𝑅𝑡′𝑐𝑑′)∶
𝑡′∈[𝑡−𝑛 min sam∶𝑡]},assuminĝ 𝜎𝑡𝑐𝑑𝑑′ ≈̂ 𝜎𝑡′𝑐𝑑𝑑′ over𝑡′∈[𝑡−𝑛 min sam∶𝑡).Since ̂𝑈𝑡 and ̃𝑈𝑡 ensurepricedataavailabilityon
[𝑡−𝑛min sam−1∶𝑡−2]—discussedinEq.(28)—and[𝑡−1∶𝑡],respectively,weusereturnsover[𝑡−𝑛 min sam∶𝑡]forestimation.
We then estimatê 𝜌𝑡𝑐𝑑𝑑′ =̂ 𝜎𝑡𝑐𝑑𝑑′∕
√
̂ 𝜎𝑡𝑐𝑑𝑑̂ 𝜎𝑡𝑐𝑑𝑑′,min 𝑑,𝑑′∈ ̂𝐷′ 𝑡𝑐 ̂ 𝜌𝑡𝑐𝑑𝑑′, and̂ 𝜅2 𝑡𝑐 =(max 𝑑∈ ̂𝐷′ 𝑡𝑐 ̂ 𝜎𝑡𝑐𝑑𝑑)∕(min𝑑∈ ̂𝐷′ 𝑡𝑐 ̂ 𝜎𝑡𝑐𝑑𝑑). For
each𝑡∈ℕand𝑐∈ ̂𝐶𝑡, we estimatêΔmax 𝑡−1,𝑐∕̂Δmin 𝑡−1,𝑐 =max{ ̃𝐹𝑡−1,𝑐𝑑∕̃𝐹𝑡−1,𝑐𝑑′ ∶𝑑,𝑑 ′ ∈ ̂𝐷′ 𝑡𝑐}from Eqs. (2) and (4). We
then check the following inequalities for each𝑡and𝑐:
̂ 𝜌𝑡𝑐,min−(̂ 𝜅2̂ 𝑛′ 𝑡𝑐−2)(3̂ 𝑛′ 𝑡𝑐−2)−1>0,(14)
̂ 𝜌𝑡𝑐,min ≥0, (15)
̂Δmax 𝑡𝑐 ∕̂Δmin 𝑡𝑐 <3, (16)
Y. Hong and D. Klabjan, Preprint, June 25, 2026 6

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
where Eqs. (14) and (15) correspond to (ii) in Proposition 1, and Eq. (16) corresponds to3Δmin 𝑡−1,𝑐 >Δ max 𝑡−1,𝑐 in
Proposition 3.
Since CS strategies can exhibit lower risk and higher IR yet remain largely unexplored in the machine-learning
literature, we focus on CS strategies and extend the framework from a single commodity to multiple commodities.
We define a CS strategy for̂𝑈𝑡 as a strategy that yields a position weight vector𝐰𝑡 =[𝑤 𝑡𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡 ∈ℝ ̂ 𝑛𝑡 satisfying ‖𝐰𝑡‖1=1and
𝟏⊤𝐰𝑡𝑐 =0,∀𝑐∈ ̂𝐶𝑡. (17)
Unlike the single-commodity definition, the𝓁1-norm constraint is imposed on𝐰𝑡, rather than on each𝐰𝑡𝑐. A CS
strategy for ̂𝑈𝑡 is a convex combination of the weight vectors of CS strategies, one for each𝑐∈̂𝐶𝑡, after extending
their dimensions toℝ̂ 𝑛𝑡.
Given a prediction vector̂𝐘𝑡 =[ ̂𝑌𝑡𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡 ∈ℝ ̂ 𝑛𝑡, we construct a CS weight vector𝐰𝑡 for ̂𝑈𝑡 using a projection
method adapted from Hong and Klabjan (2025b), wherê𝑌𝑡𝑐𝑑 is discussed below. Specifically, we compute
𝐰𝑡= ̂𝐘◦ 𝑡∕‖̂𝐘◦ 𝑡‖1 (18)
where
̂𝐘◦ 𝑡 =[ ̂𝑌𝑡𝑐𝑑 − ̂𝑌∙ 𝑡𝑐](𝑐,𝑑)∈ ̂𝑈𝑡 ,(19)
̂𝑌∙ 𝑡𝑐 = 1 ̂ 𝑛𝑡𝑐 ∑ 𝑑′∈ ̂𝐷𝑡𝑐 ̂𝑌𝑡𝑐𝑑′. (20)
Thatis,wecenterthepredictionvectorbysubtractingthecommodity-wiseaverage ̂𝑌∙ 𝑡𝑐 inEq.(19),andthenscaleitin
Eq. (18). This computation is equivalent to projectinĝ𝐘𝑡 onto{𝐰 𝑡∶𝟏 ⊤𝐰𝑡𝑐 =0,∀𝑐∈ ̂𝐶𝑡}under the Euclidean norm
and then scaling; see Appendix Section B. Thus,𝐰𝑡 satisfies𝟏 ⊤𝐰𝑡𝑐 = 0,∀𝑐∈ ̂𝐶𝑡 and‖𝐰 𝑡‖1 = 1. Since projection
yields the closest vector satisfying the constraints, the resulting vector from Eqs. (18) to (20) is, up to scaling, the CS
weight vector closest to the prediction vector.
We consider a daily trading scheme with daily predictions and periodic retraining. Given𝑛fit ∈ℕ, we let
{𝑡𝑘 ∶𝑘∈[1∶𝑛 fit]}denote the retraining dates with𝑡𝑘 <𝑡 𝑘+1 and𝑡 𝑛fit+1 =∞. For each𝑘∈[1∶𝑛 fit], a prediction model𝑓 𝑘 is trained on𝑡𝑘 when 𝑡𝑘 becomes available, i.e., after the markets close on𝑡𝑘 and before they open on
𝑡𝑘+1. On each trading date𝑡∈ test 𝑘 = [𝑡𝑘 ∶𝑡 𝑘+1), we predict price movements𝐘𝑡+2 = [𝑌𝑡+2,𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡+2 ∈ℝ ̂ 𝑛𝑡+2
from𝑡+1to𝑡+2as ̂𝐘𝑡+2 = [̂𝑌𝑡+2,𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡+2 =𝑓 𝑘(𝑡) ∈ℝ ̂ 𝑛𝑡+2 where𝑌 𝑡+2,𝑐𝑑 is defined below. Based on these
predictions, CS position vector𝐰𝑡+2 = [𝑤𝑡+2,𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡+2 ∈ℝ ̂ 𝑛𝑡+2 is computed via Eqs. (18) to (20). The prediction
and CS position vectors are generated after the markets close at𝑡(or after training if𝑡=𝑡𝑘) and before they open at
𝑡+1. In the markets, the CS position vector is then established at𝑡+1and liquidated at𝑡+2, with trades executed at
prices𝐹 𝑡+1,𝑐𝑑 and𝐹𝑡+2,𝑐𝑑, respectively. No datum in𝐻𝑡′ with𝑡′ ≥𝑡 𝑘+1is used to train𝑓𝑘, and no datum in𝐻𝑡′ with
𝑡′ ≥𝑡+1is used to produce( ̂𝐘𝑡+2,𝐰𝑡+2), thereby precluding look-ahead bias.
4.2. Prediction Model
Foreach𝑘∈[1∶𝑛 fit],givenhistory 𝑡𝑘,ourpredictionproblemistotrainamodel𝑓 𝑘(𝑡)=[ ̂𝑌𝑡+2,𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡+2 ∈
ℝ̂ 𝑛𝑡+2 that predicts[𝑌𝑡+2,𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡+2 , so as to minimize
∑
𝑡∈test 𝑘
𝔼
[
𝑙𝑝
(
[̂𝑌𝑡+2,𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡+2 ,[𝑌𝑡+2,𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡+2
)]
,(21)
where test 𝑘 = [𝑡𝑘 ∶𝑡 𝑘+1)and𝑙 𝑝 is a loss function. For𝑡∈ℕand(𝑐,𝑑) ∈ ̂𝑈𝑡, the target𝑌𝑡𝑐𝑑 is defined as the normalized, commodity-wise demeaned return
𝑌𝑡𝑐𝑑 =Φ −1(̂cdf(𝑅◦ 𝑡𝑐𝑑;[𝑅◦ 𝑡𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡 ))(22)
Y. Hong and D. Klabjan, Preprint, June 25, 2026 7

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
whereΦ−1 is the standard normal quantile function, and the commodity-wise demeaned return is defined as
𝑅◦ 𝑡𝑐𝑑 =𝑅 𝑡𝑐𝑑 −𝑅∙ 𝑡𝑐 (23)
with𝑅 ∙ 𝑡𝑐 = avg(𝑅𝑡𝑐𝑑;𝑑∈ ̂𝐷𝑡𝑐). By the probability integral transform,̂cdf(𝑅◦ 𝑡𝑐𝑑;[𝑅◦ 𝑡𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡 )is approximately
uniformly distributed on[0,1], andΦ−1 maps it to an approximately standard normal variable. Since the standard-
normaltargetcanstabilizeoptimization(LeCun,Bottou,OrrandMüller,2002;GlorotandBengio,2010;Hong,Kim,
Kim and Choi, 2023), we adopt this prediction target. The motivation for using𝑅◦ 𝑡𝑐𝑑 is discussed below. When addressing a task related toΠ(𝐰𝑡)for a CS strategy, we can predict𝑅◦ 𝑡𝑐𝑑 in lieu of𝑅𝑡𝑐𝑑. For𝐰𝑡∈ 𝑡,CS, its strategy return satisfiesΠ(𝐰𝑡) =∑ 𝑐∈ ̂𝐶𝑡 ∑ 𝑑∈ ̂𝐷𝑡𝑐 𝑤𝑡𝑐𝑑𝑅𝑡𝑐𝑑 = ∑ 𝑐∈ ̂𝐶𝑡 (∑ 𝑑∈ ̂𝐷𝑡𝑐 𝑤𝑡𝑐𝑑𝑅𝑡𝑐𝑑 −𝑅 ∙ 𝑡𝑐 ∑ 𝑑∈ ̂𝐷𝑡𝑐 𝑤𝑡𝑐𝑑) =∑ 𝑐∈ ̂𝐶𝑡∑
𝑑∈ ̂𝐷𝑡𝑐 𝑤𝑡𝑐𝑑(𝑅𝑡𝑐𝑑 −𝑅 ∙ 𝑡𝑐) = ∑ (𝑐,𝑑)∈ ̂𝑈𝑡 𝑅◦ 𝑡𝑐𝑑𝑤𝑡𝑐𝑑 where each equality follows from Eq. (6), Eq. (17), algebraic
manipulation, and Eq. (23), in that order. Thus,𝑅◦ 𝑡𝑐𝑑 can replace𝑅𝑡𝑐𝑑 in Eq. (6) to obtain the return of a CS strategy.
As𝑅◦ 𝑡𝑐𝑑 canbelessexposedtotheunderlyingcommodity,𝑅 ◦ 𝑡𝑐𝑑 canbemorepredictablethan𝑅 𝑡𝑐𝑑.Fix(𝑐,𝑑)∈ ̂𝑈𝑡.
Thequantity𝑅 ◦ 𝑡𝑐𝑑 canbeinterpretedasthereturnofaCSstrategyfor𝑐withapositionvector[𝕀 {𝑑′=𝑑}]𝑑′∈ ̂𝐷𝑡𝑐 − 1 ̂ 𝑛𝑡𝑐 𝟏∈
ℝ̂ 𝑛𝑡𝑐, which becomes a weight vector after scaling. In contrast,𝑅𝑡𝑐𝑑 corresponds to the return of a LO strategy for𝑐
with weight[𝕀{𝑑′=𝑑}]𝑑′∈ ̂𝐷𝑡𝑐 . By Proposition 3 and its experimental evidence in Section 5,𝑅◦ 𝑡𝑐𝑑 has lower exposure to the underlying commodity than𝑅𝑡𝑐𝑑 in a large fraction of cases. In addition, the data for underlying commodities are
intrinsically incomplete.1 Therefore, we predict𝑅◦ 𝑡𝑐𝑑.
Foreach𝑘∈[1∶𝑛 fit],wetrain𝑓 𝑘on{(𝑡,[ ̃𝑌𝑡+2,𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡+2∩̃𝑈𝑡+2 )∶𝑡∈ fit 𝑘 },validateon{( 𝑡,[ ̃𝑌𝑡+2,𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡+2∩̃𝑈𝑡+2 )∶
𝑡∈ val 𝑘 },andevaluateon{( 𝑡,[ ̃𝑌𝑡+2,𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡+2∩̃𝑈𝑡+2 )∶𝑡∈ test 𝑘 },where fit 𝑘 ∩ val 𝑘 =∅, fit 𝑘 ∪ val 𝑘 ⊂[1∶𝑡 𝑘−2],
and test 𝑘 =[𝑡 𝑘∶𝑡 𝑘+1).Since ̂𝑈𝑡+2 isdeterminedat𝑡basedsolelyon 𝑡,somecontractsin ̂𝑈𝑡+2 maynotbeobservable
at𝑡+1or𝑡+2,i.e., ̃𝑉𝑡+1,𝑐𝑑 ̃𝑉𝑡+2,𝑐𝑑 =0;thus,weuse ̂𝑈𝑡+2∩ ̃𝑈𝑡+2 inlieuof ̂𝑈𝑡+2 forthemodeltrainingandevaluation:
̃𝑌𝑡𝑐𝑑 =Φ −1(̂cdf( ̃𝑅◦ 𝑡𝑐𝑑;[ ̃𝑅◦ 𝑡𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡∩̃𝑈𝑡 )), ̃𝑅◦ 𝑡𝑐𝑑 = ̃𝑅𝑡𝑐𝑑 − ̃𝑅∙ 𝑡𝑐, ̃𝑅∙ 𝑡𝑐 =avg( ̃𝑅𝑡𝑐𝑑;𝑑∈ ̂𝐷𝑡𝑐∩ ̃𝐷𝑡𝑐).(24)
Note that the training and validation datasets are constructed solely from𝑡𝑘, which is given for training𝑓𝑘 in the
problem, and do not use any future data, i.e.,𝑡′ for𝑡′>𝑡 𝑘, thereby ensuring no look-ahead bias.2 Additionally, test 𝑘
for𝑘∈[1∶𝑛 fit]partition[𝑡 1∶𝑡 𝑛fit+1), i.e.,⋃ 𝑘∈[1∶𝑛fit]  test 𝑘 =[𝑡 1∶𝑡 𝑛fit+1)with test 𝑘 ∩ test 𝑘′ =∅for𝑘≠𝑘 ′. Architecture Overview. To solve the problem, we propose a bi-level hierarchical graph learning architecture
𝑓𝑘(𝑡)=(𝑓 H 𝑘◦𝑓B 𝑘◦𝑓L 𝑘◦𝑓P 𝑘)(𝑡)=[ ̂𝑌𝑡+2,𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡+2 .Thepreprocessingfunction𝑓 P 𝑘 maps𝑡toabi-levelhierarchical
graph,andthegraphliftingfunction𝑓 L 𝑘 alignsTTMgridsacrosscommoditiesbyextendingthegraphalongtheTTM
dimension. The bi-level convolution function𝑓B 𝑘 then performs TTM-conditioned propagation through the extended
bi-levelgraph,followedbythehead𝑓 H 𝑘 ,whichoutputspredictions[ ̂𝑌𝑡+2,𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡+2 .Throughoutthesefunctions,our
architecturecapturesTTM-dependentinformationembeddedininterrelationshipsamongcommodityfuturescontracts.
The preprocessing function𝑓 P 𝑘(𝑡)outputs a bi-level graph𝐺𝑡 =( ̂𝐶𝑡+2∪ ̂𝑈𝑡+2,𝐸CC+ 𝑡 ∪𝐸 CC− 𝑡 ∪𝐸 CU 𝑡 ∪𝐸 UC 𝑡 ∪
𝐸UU 𝑡 ,𝑋𝑡), illustrated in Figure 1. The commodities in̂𝐶𝑡+2 form the upper-level nodes, and their contracts in̂𝑈𝑡+2
constitutethelower-levelnodes.Theupper-levelnodesareconnectedvia𝐸 CC+ 𝑡 ⊂ ̂𝐶𝑡+2× ̂𝐶𝑡+2and𝐸CC− 𝑡 ⊂ ̂𝐶𝑡+2× ̂𝐶𝑡+2,
whichdenotetheedgesetscorrespondingtopositiveandnegativecorrelationsbetweencommodities,respectively.The
cross-levelconnectionsaregivenby𝐸 CU 𝑡 ⊂ ̂𝐶𝑡+2× ̂𝑈𝑡+2 and𝐸 UC 𝑡 ⊂ ̂𝑈𝑡+2× ̂𝐶𝑡+2,linkingeachunderlyingcommodity
and its contracts. The lower-level nodes are connected via𝐸UU 𝑡 ⊂ ̂𝑈𝑡+2× ̂𝑈𝑡+2, which links each contract to its two
nearest-maturitycontracts(oneshorterandonelonger)withthesameunderlyingcommodity 3,reflectingtheeconomic
insight(Brennan,1976;GibsonandSchwartz,1990;Schwartz,1997;CasassusandCollin-Dufresne,2005)thatfutures
contractswithsimilarTTMssharesimilareconomiccharacteristics.Thematrix𝑋 𝑡∈ℝ ̂ 𝑛𝑡+2×𝑛min sam containsnodefeatures
for ̂𝑈𝑡+2.
1 True spot markets for some underlying commodities do not exist (Gibson and Schwartz, 1990), and thus their spot price data are not directly
observable.
2The pair(𝑡𝑘−2,[ ̃𝑌𝑡𝑘,𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡𝑘∩̃𝑈𝑡𝑘 )is the latest sample that can be used for training or validation. By Eqs. (22) and (23) and the definition
of𝑈 𝑡𝑘, the latest historical data involved in(𝑡𝑘−2,[ ̃𝑌𝑡𝑘,𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡𝑘∩̃𝑈𝑡𝑘 )are 𝑡𝑘, thereby ensuring no look-ahead bias. 3For each commodity, contracts with the smallest or largest maturity have only one edge in𝐸UU 𝑡
Y. Hong and D. Klabjan, Preprint, June 25, 2026 8

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
Figure 1:Bi-Level Hierarchical Graph
To ensure proper backtesting, we define the trading universê𝑈𝑡+2 as
̂𝑈𝑡+2={(𝑐,𝑑)∈ ̂𝑈′ 𝑡+2∶̂ 𝜎𝑥 𝑡𝑐 >0}(25)
where𝜎 𝑥 𝑡𝑐 is defined below, and̂𝑈′ 𝑡+2 is defined as the set of(𝑐,𝑑)∈× 𝑐 such that
𝑡+2≤𝑇 𝑐𝑑, (26)
𝑇𝑐𝑑 −𝑡≤𝜏 max, (27) ∏
𝑡′∈(𝑡−𝑛minsam,𝑡]
̃𝑉𝑡′𝑐𝑑 >0. (28)
Here,𝜏 max∈ℕand𝑛 min sam∈ℕarehyperparameters.TheconstraintinEq.(25)ensures𝑋 𝑡 iswell-defined,asdiscussed
below.Eq.(26)ensuresthatpositionvectordeterminedat𝑡canbeliquidatedat𝑡+2,andEq.(27)excludeslong-TTM
contracts, which tend to be illiquid (Xu and Zhang, 2023). Eq. (28) implies that(𝑐,𝑑)∈̂𝑈′ 𝑡+2 is traded in the market
on all of the most recent𝑛min sam trading dates, thereby ensuring liquidity. Unlike Hu et al. (2025); Tan et al. (2024), our
trading universe evolves over time, allowing node creation and deletion.
To enable neural networks to capture information in𝑡, we define the node feature matrix𝑋𝑡=[𝐱 𝑡𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡+2 ∈
ℝ̂ 𝑛𝑡+2×𝑛min sam where𝐱 𝑡𝑐𝑑 =[𝑥 𝑡𝑐𝑑𝜏]𝜏∈[0∶𝑛minsam)∈ℝ 𝑛min sam and
𝑥𝑡𝑐𝑑𝜏 =Φ −1(̂cdf(𝑥′ 𝑡𝑐𝑑𝜏;[𝑥′ 𝑡𝑐𝑑𝜏′](𝑐,𝑑)∈ ̂𝑈𝑡+2,𝜏′∈[0∶𝑛minsam)))(29)
for𝑡∈ [𝑛 min sam ∶ ∞),(𝑐,𝑑) ∈ ̂𝑈𝑡+2, and𝜏∈ [0 ∶𝑛 min sam). For𝑡∈ [𝑛min sam ∶ ∞),(𝑐,𝑑) ∈ ̂𝑈′ 𝑡+2, and𝜏∈ [0 ∶𝑛 min sam), we define
𝑥′ 𝑡𝑐𝑑𝜏 =𝑥 ′′ 𝑡𝑐𝑑𝜏∕̂ 𝜎𝑥 𝑡𝑐 (30)
where
̂ 𝜎𝑥 𝑡𝑐 =std(𝑥 ′′ 𝑡𝑐𝑑′′𝜏;𝜏∈[0∶𝑛 min sam),(𝑐,𝑑 ′′)∈ ̂𝑈′ 𝑡+2),(31)
𝑥′′ 𝑡𝑐𝑑𝜏 =log( ̃𝐹𝑡−𝜏,𝑐𝑑)−̂ 𝜇𝑥 𝑡𝑐𝑑⋅ −̂ 𝜇𝑥 𝑡𝑐⋅𝜏 +̂ 𝜇𝑥 𝑡𝑐⋅⋅,(32)
̂ 𝜇𝑥 𝑡𝑐𝑑⋅ =avg(log( ̃𝐹𝑡−𝜏′,𝑐𝑑);𝜏′∈[0∶𝑛 min sam)),(33)
Y. Hong and D. Klabjan, Preprint, June 25, 2026 9

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
̂ 𝜇𝑥 𝑡𝑐⋅𝜏 =avg(log( ̃𝐹𝑡−𝜏,𝑐𝑑′′);𝑑′′∈{𝑑 ′∶(𝑐,𝑑 ′)∈ ̂𝑈′ 𝑡+2}),(34)
̂ 𝜇𝑥 𝑡𝑐⋅⋅ =avg(log( ̃𝐹𝑡−𝜏′,𝑐𝑑′′);𝜏′∈[0∶𝑛 min sam),𝑑′′∈{𝑑 ′∶(𝑐,𝑑 ′)∈ ̂𝑈′ 𝑡+2}).(35)
Eqs. (32) to (35) perform two-way ANOVA-style centering of log prices. To account for differing price scales across
commodities,Eq.(30)scalesthecenteredvalueswithineachcommodity.Thus,eachnodefeaturecontainscenteredand
scaledlog-priceinformationoverthemostrecent𝑛 min sam days.Sincestandard-normalfeaturescanstabilizeoptimization
(LeCun et al., 2002; Glorot and Bengio, 2010; Hong et al., 2023), we normalize𝑥′ 𝑡𝑐𝑑𝜏 in Eq. (29).
To capture inter-commodity relationships, we define the inter-commodity edge sets𝐸CC+ 𝑡 = {(𝑐,𝑐′) ∈ ̂𝐶𝑡+2×
̂𝐶𝑡+2 ∶̂ 𝜌𝑡𝑐𝑐′ ≥𝜌 ∗}and𝐸 CC− 𝑡 = {(𝑐,𝑐′) ∈ ̂𝐶𝑡+2 × ̂𝐶𝑡+2 ∶̂ 𝜌𝑡𝑐𝑐′ ≤−𝜌 ∗}. Here,𝜌 ∗ >0is a predefined
threshold, and̂ 𝜌𝑡𝑐𝑐′ is the Pearson correlation computed from the accumulated sample set⋃ 𝑡′∈[1∶𝑡]𝐵𝑡′𝑐𝑐′, provided
that|{𝑡 ′ ∈ [1 ∶𝑡] ∶𝐵 𝑡′𝑐𝑐′ ≠∅}|≥𝑛 min sam. If the minimum number of observation time points is not met,
we set̂ 𝜌𝑡𝑐𝑐′ = 0. A sample batch𝐵𝑡𝑐𝑐′ is defined as the set of maturity-aligned pairs of estimated-and-demeaned
returns:𝐵 𝑡𝑐𝑐′ = {(̂𝑅◦ 𝑡𝑐(𝑇), ̂𝑅◦ 𝑡𝑐′(𝑇)) ∶𝑇∈ ( 𝑐 ∪ 𝑐′)∩dom( ̂𝑅◦ 𝑡𝑐)∩dom( ̂𝑅◦ 𝑡𝑐′),𝑇−𝑡≤𝜏 max}. Here, ̂𝑅◦ 𝑡𝑐(𝑇)is the
demeaned return estimation function with domaindom(̂𝑅◦ 𝑡𝑐). Since maturities are not aligned across commodities—
i.e., a commodity-𝑐futures contract with maturity𝑇, or its return, may not exist—we linearly interpolatê𝑅◦ 𝑡𝑐(𝑇) = ̃𝑅∗ 𝑡𝑐𝑑+−̃𝑅∗ 𝑡𝑐𝑑−
𝑇𝑐𝑑+−𝑇𝑐𝑑− (𝑇−𝑇 𝑐𝑑−)+ ̃𝑅∗ 𝑡𝑐𝑑− where(𝑑 −,𝑑+)minimizes|𝑑 +−𝑑 −|subject to𝑇∈[𝑇 𝑐𝑑−,𝑇𝑐𝑑+]and both ̃𝑅∗ 𝑡𝑐𝑑+ and ̃𝑅∗ 𝑡𝑐𝑑− are well-defined. We define
̃𝑅∗ 𝑡𝑐𝑑 = ̃𝑅𝑡𝑐𝑑 −avg( ̃𝑅𝑡𝑐𝑑′;𝑑′∈𝐷 ′ 𝑡𝑐)(36)
for𝑑∈𝐷 𝑡𝑐 with|𝐷′ 𝑡𝑐|>1,where𝐷 ′ 𝑡𝑐 ={𝑑 ′∈𝐷 𝑡𝑐 ∶𝑇 𝑐𝑑′−𝑡≤𝜏 max}.ConsistentwiththepredictiontargetEq.(22),
which is based on demeaned returns Eq. (23), we use demeaned returns for̂𝑅◦ 𝑡𝑐(𝑇).
The graph lifting function𝑓 L 𝑘(𝐺𝑡)outputs an augmented graph𝐺𝑡0 = (̂𝐶𝑡+2,0∪ ̂𝑈𝑡+2,𝐸CC+ 𝑡0 ∪𝐸 CC− 𝑡0 ∪𝐸 CU 𝑡0 ∪
𝐸UC 𝑡0 ∪𝐸 UU 𝑡 ,𝑍𝑡0). It transformŝ𝐶𝑡+2 into an extended node set̂𝐶𝑡+2,0 = {(𝑐,𝑗) ∶𝑗∈ [0 ∶𝑛bas]}of virtual futures contracts where𝑗indexes a virtual basis TTM𝜏𝑗 =𝑗⋅(𝜏 max∕𝑛bas). This aligns maturity grids𝑐 across commodities
𝑐∈ ̂𝐶𝑡+2 onto a shared virtual TTM grid{𝜏𝑗 ∶𝑗∈ [0 ∶𝑛 bas]}, since commodities generally do not share identical
futures maturities, i.e.,𝑐′ ≠  𝑐′′ for𝑐 ′,𝑐′′ ∈. Accordingly, the edges of𝐺 𝑡 are also extended along the TTM
dimension, yielding𝐸CC+ 𝑡0 ,𝐸CC− 𝑡0 ,𝐸CU 𝑡0 ,𝐸UC 𝑡0 . Specifically,𝐸CC+ 𝑡0 ={((𝑛,𝑗),(𝑛 ′,𝑗))∶(𝑛,𝑛 ′)∈𝐸 CC+ 𝑡 ,𝑗∈[0∶𝑛 bas]},
𝐸CU 𝑡0 = {((𝑛,𝑗),𝑛′) ∶ (𝑛,𝑛′) ∈𝐸CU 𝑡 ,𝑗∈ [0 ∶𝑛bas]}with𝐸 CC− 𝑡0 and𝐸 UC 𝑡0 defined analogously. While preserving the
original topology,𝐸CC+ 𝑡0 ∪𝐸 CC− 𝑡0 connects the virtual nodes with the same virtual TTMs, and𝐸CU 𝑡0 ∪𝐸 UC 𝑡0 connects
virtual nodes and their original futures nodes. Next,𝑓L 𝑘 produces the initial embedding𝑍𝑡0=[𝐳 𝑡,0,𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡+2 where
𝐳𝑡,0,𝑐𝑑 =Dropout(𝜙(𝑊 L,𝑘𝐱𝑡𝑐𝑑 +𝐛L,𝑘))∈ℝ 𝑛hid for(𝑐,𝑑)∈ ̂𝑈𝑡+2. Here,𝑛hid∈ℕis a hyperparameter.
The bi-level convolution function𝑓 B 𝑘(𝐺𝑡0) = (𝑓B 𝑘,𝑙con ◦…◦𝑓 B 𝑘,1)(𝐺𝑡0)with𝑙 con layers outputs𝐺𝑡,𝑙con, where each
layer function𝑓 B 𝑘𝑙 maps𝐺 𝑡,𝑙−1 to𝐺 𝑡𝑙. Each layer output graph𝐺𝑡𝑙 shares the same node and edge sets but differs
in its node embedding matrix𝑍𝑡𝑙 = [𝐳𝑡𝑙𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡+2 ∈ℝ ̂ 𝑛𝑡+2×𝑛hid, so that𝐺𝑡𝑙 = (̂𝐶𝑡+2,0 ∪ ̂𝑈𝑡+2,𝐸CC+ 𝑡0 ∪𝐸 CC− 𝑡0 ∪
𝐸CU 𝑡0 ∪𝐸 UC 𝑡0 ∪𝐸 UU 𝑡 ,𝑍𝑡𝑙). Each convolution layer function𝑓B 𝑘𝑙 consists of four operations, illustrated in Figure 2:
𝑓B 𝑘𝑙 =𝑔 UU 𝑘𝑙 ◦𝑔CU 𝑘𝑙 ◦𝑔CC 𝑘𝑙 ◦𝑔UC 𝑘𝑙 where all the operation outputs share the same node and edge sets but have distinct node
embeddings. First,𝑔UC 𝑘𝑙 elevates embeddings from lower-level contract nodes to TTM-aligned virtual futures nodes
at the upper-level. Next,𝑔CC 𝑘𝑙 propagates information among virtual futures contracts sharing the same TTM. Then,
𝑔CU 𝑘𝑙 transfers the aggregated upper-level information back to lower-level contract nodes. Finally,𝑔UU 𝑘𝑙 propagates information across contracts with the nearest maturities within the same commodities. Throughout these steps, we
distinguish contract relationships based on maturity differences and extract information accordingly via𝑔CC 𝑘𝑙 and𝑔 UU 𝑘𝑙 , in contrast to existing approaches (Hu et al., 2025; Tan et al., 2024) that treat all relationships in the same manner
regardless of maturity. Each step is discussed next.
Theelevatingoperator𝑔 UC 𝑘𝑙 transforms𝑍𝑡,𝑙−1=[𝐳 𝑡,𝑙−1,𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡+2 ∈ℝ ̂ 𝑛𝑡+2×𝑛hid into𝑍UC 𝑡𝑙 =[𝐳 UC 𝑡𝑙𝑐𝑗](𝑐,𝑗)∈ ̂𝐶𝑡+2×[0∶𝑛bas]∈
ℝ̂ 𝑛𝑡+2(𝑛bas+1)×𝑛hid, via linear interpolation
𝐳UC 𝑡𝑙𝑐𝑗 = 𝐳𝑡,𝑙−1,𝑐𝑑+−𝐳𝑡,𝑙−1,𝑐𝑑− 𝑇𝑐𝑑+−𝑇𝑐𝑑− ⋅(𝑡+𝜏 𝑗−𝑇𝑐𝑑−)+𝐳 𝑡,𝑙−1,𝑐𝑑− ∈ℝ 𝑛hid (37)
Y. Hong and D. Klabjan, Preprint, June 25, 2026 10

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
Figure 2:Bi-Level Convolution
for𝑡+𝜏 𝑗 ∈[𝑇 𝑐,min ̂𝐷𝑡+2,𝑐 ,𝑇𝑐,max ̂𝐷𝑡+2,𝑐 ],where𝑑 −,𝑑+∈ ̂𝐷𝑡+2,𝑐 minimize|𝑇𝑐𝑑+−𝑇𝑐𝑑−|subjectto𝑡+𝜏 𝑗 ∈[𝑇 𝑐𝑑−,𝑇𝑐𝑑+].
Since futures contracts with similar TTMs share similar economic characteristics (Brennan, 1976; Gibson and
Schwartz, 1990; Schwartz, 1997; Casassus and Collin-Dufresne, 2005), we use interpolation based on neighboring
maturities. For𝑡+𝜏 𝑗 ∉ [𝑇𝑐,min ̂𝐷𝑡+2,𝑐 ,𝑇𝑐,max ̂𝐷𝑡+2,𝑐 ], we use the end point values for the extrapolation by setting
𝐳UC 𝑡𝑙𝑐𝑗 =𝐳 𝑡,𝑙−1,𝑐𝑑∗ with𝑑 ∗ =𝕀 {𝜏𝑗+𝑡<𝑇𝑐,min ̂𝐷𝑡+2,𝑐}⋅min ̂𝐷𝑡+2,𝑐 +𝕀 {𝜏𝑗+𝑡>𝑇𝑐,max ̂𝐷𝑡+2,𝑐}⋅max ̂𝐷𝑡+2,𝑐. Since both interpolation
and extrapolation are linear, for each𝑐∈̂𝐶𝑡+2, we can write[𝐳UC 𝑡𝑙𝑐𝑗]𝑗∈[0∶𝑛bas] = ∑ 𝑑∈ ̂𝐷𝑡+2,𝑐 𝐩𝑡𝑐𝑑 𝐳⊤ 𝑡,𝑙−1,𝑐𝑑 ∈ℝ (𝑛bas+1)×𝑛hid
for some constant vectors𝐩𝑡𝑐𝑑 ∈ℝ 𝑛bas+1. Note that𝐩𝑡𝑐𝑑 does not depend on𝑙and𝑍 𝑡,𝑙−1 but depends on𝑡,𝜏𝑗,𝑇𝑐𝑑+,
and𝑇𝑐𝑑−. Thus,𝐩𝑡𝑐𝑑 can be precomputed before training and inference, and shares the same values for all layers. As a
result of𝑔UC 𝑘𝑙 , each𝐳UC 𝑡𝑙𝑐𝑗 contains the information of a virtual future contract with TTM𝜏𝑗 for commodity𝑐.
The inter-commodity propagation𝑔CC 𝑘𝑙 transforms𝑍 UC 𝑡𝑙 into
𝑍𝐶𝐶 𝑡𝑙 =𝜙([𝑍 UC 𝑡𝑙 𝑍𝐶𝐶+ 𝑡𝑙 𝑍𝐶𝐶− 𝑡𝑙 ]𝑊CC,𝑘𝑙+𝟏𝐛⊤ CC,𝑘𝑙)∈ℝ ̂ 𝑛𝑡+2(𝑛bas+1)×𝑛hid (38)
where[𝑍 UC 𝑡𝑙 𝑍𝐶𝐶+ 𝑡𝑙 𝑍𝐶𝐶− 𝑡𝑙 ]∈ℝ ̂ 𝑛𝑡+2(𝑛bas+1)×(3𝑛hid),𝑍 𝐶𝐶+ 𝑡𝑙 =𝜙(CONV( ̂𝐶𝑡+2,0,𝐸𝐶𝐶+ 𝑡0 ,𝑍𝑈𝐶 𝑡𝑙 ;𝜃+ 𝐶𝐶,𝑙))∈ℝ ̂ 𝑛𝑡+2(𝑛bas+1)×𝑛hid,
and𝑍 𝐶𝐶− 𝑡𝑙 =𝜙(CONV( ̂𝐶𝑡+2,0,𝐸𝐶𝐶− 𝑡0 ,𝑍𝑈𝐶 𝑡𝑙 ;𝜃− 𝐶𝐶,𝑙)) ∈ℝ ̂ 𝑛𝑡+2(𝑛bas+1)×𝑛hid. Here,CONVdenotes a graph convolution,
and𝜃 + 𝐶𝐶,𝑙 and𝜃 − 𝐶𝐶,𝑙 are distinct learnable parameters. Since𝐸𝐶𝐶+ 𝑡0 and𝐸 𝐶𝐶− 𝑡0 connect nodes with the same virtual
TTM, each node(𝑐,𝑗∗)∈ ̂𝐶𝑡+2,0 aggregates information𝐳UC 𝑡𝑙𝑐′𝑗∗ from other nodes with the same TTM𝑗∗ but different
commodities𝑐 ′, while preserving the original topology of𝐸𝐶𝐶+ 𝑡 and𝐸 𝐶𝐶− 𝑡 . In other words,𝑔CC 𝑘𝑙 propagates TTM-
aligned information[𝐳UC 𝑡𝑙𝑐𝑗]𝑗∈[0∶𝑛bas] across commodities𝑐∈ ̂𝐶𝑡+2.
Theloweringfunction𝑔 CU 𝑘𝑙 converts𝑍𝐶𝐶 𝑡𝑙 =[𝐳 CC 𝑡𝑙𝑐𝑗]𝑐∈ ̂𝐶𝑡+2,𝑗∈[0∶𝑛bas]∈ℝ ̂ 𝑛𝑡+2(𝑛bas+1)×𝑛hid into𝑍𝐶𝑈 𝑡𝑙 =[𝐳 CU 𝑡𝑙𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡+2 ∈
ℝ̂ 𝑛𝑡+2×𝑛hid via linear interpolation
𝐳CU 𝑡𝑙𝑐𝑑 = 𝐳CC 𝑡𝑙𝑐,𝑗−+1−𝐳CC 𝑡𝑙𝑐𝑗− 𝜏𝑗−+1−𝜏𝑗− ⋅(𝑇𝑐𝑑 −𝑡−𝜏 𝑗−)+𝐳 CC 𝑡𝑙𝑐𝑗− ∈ℝ 𝑛hid (39)
where𝑗 −∈[0∶𝑛 bas)satisfies𝑇 𝑐𝑑−𝑡∈[𝜏 𝑗−,𝜏𝑗−+1].Sincetheintervals[𝜏 𝑗−,𝜏𝑗−+1]partitionaninterval[0,𝜏 max],the
minimization used for the indexes in Eq. (37) is not required. Since this interpolation is linear, it can be precomputed,
as discussed in the elevating operator Eq. (37).
Y. Hong and D. Klabjan, Preprint, June 25, 2026 11

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
The intra-commodity propagation𝑔UU 𝑘𝑙 maps𝑍 𝐶𝑈 𝑡𝑙 to𝑍 𝑡𝑙=[𝐳 𝑡𝑙𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡+2 ∈ℝ ̂ 𝑛𝑡+2×𝑛hid where
𝐳𝑡𝑙𝑐𝑑 =𝜙(𝑊 UU,𝑘𝑙[𝐳CU 𝑡𝑙𝑐𝑑;𝐳UU 𝑡𝑙𝑐𝑑]+𝐛 UU,𝑘𝑙)∈ℝ 𝑛hid (40)
with
𝐳UU 𝑡𝑙𝑐𝑑 = ∑
𝑑′∈{𝑑′′∶(𝑑′′,𝑑)∈𝐸UU 𝑡 }
𝐳UU∗ 𝑡𝑙𝑐𝑑𝑑′ ∈ℝ 𝑛hid,(41)
𝐳UU∗ 𝑡𝑙𝑐𝑑𝑑′ =𝜙(𝑊 UU∗,𝑘𝑙⋅LayerNorm(𝐳 CU 𝑡𝑙𝑐𝑑 −𝐳CU 𝑡𝑙𝑐𝑑′)+𝐛 UU∗,𝑘𝑙)∈ℝ 𝑛hid,(42)
InEq.(40),𝐳 𝑡𝑙𝑐𝑑 integratesthetargetcontractembedding𝐳 CU 𝑡𝑙𝑐𝑑 withneighboringinformation𝐳 UU 𝑡𝑙𝑐𝑑.Eq.(41)aggregates
messages𝐳UU∗ 𝑡𝑙𝑐𝑑𝑑′ fromneighboringcontractsin𝐸 UU 𝑡 .Eachmessage𝐳 UU∗ 𝑡𝑙𝑐𝑑𝑑′ iscomputedfromthenormalizeddifference between the target and source embeddings as in Eq. (42) to capture relative deviations along the term structure
withinthesamecommodity.Consequently,𝑔 UU 𝑘𝑙 extractsintra-commodityinformationfromnearest-maturitycontracts of the same underlying commodity, reflecting the economic insight that futures with similar TTMs exhibit similar
characteristics (Brennan, 1976; Gibson and Schwartz, 1990; Schwartz, 1997; Casassus and Collin-Dufresne, 2005).
Throughout the bi-level convolution𝑓B 𝑘 , each futures contract node integrates its information with that of related nodes while explicitly accounting for their TTMs, in contrast to existing approaches (Hu et al., 2025; Tan et al., 2024)
that ignore the maturity dependence of these relationships. In their approaches, interactions between futures contracts
are treated without differentiation by maturity, so information from contracts with similar maturities is processed in
the same manner as that from contracts with dissimilar maturities. In our method, however, each convolution layer
𝑓B 𝑘,𝑙 uses two distinct message passing functions:𝑔CC 𝑘𝑙 , which propagates information across different commodities at
thesameTTM,and𝑔 UU 𝑘𝑙 ,whichpropagatesinformationacrossnearbyTTMswithinthesamecommodity.Bystacking
multiplelayersof𝑓 B 𝑘,𝑙,themodelpropagatesinformationacrosscontractswithlargermaturitygapsthroughsuccessive local interactions, thereby capturing higher-order dependencies over the joint commodity-maturity space. This design
enables maturity-dependent propagation by explicitly distinguishing the relationships based on TTM while capturing
inter-commodity and intra-commodity structures.
The head𝑓 H 𝑘(𝐺𝑡𝑘𝑙con)transformsthefinalnodeembeddingmatrix𝑍 𝑡,𝑙con intoapredictionvector[ ̂𝑌𝑡+2,𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡+2 .
For each(𝑐,𝑑) ∈ ̂𝑈𝑡+2, the head𝑓H 𝑘(𝐺𝑡𝑘𝑙con)outputs ̂𝑌𝑡+2,𝑐𝑑 =𝑊 H,𝑘𝐳𝑡𝑙con𝑐𝑑 +𝐛 H,𝑘 ∈ℝ. During the training, we
minimize the mean squared error between̂𝑌𝑡+2,𝑐𝑑 and𝑌 𝑡+2,𝑐𝑑 for(𝑐,𝑑)∈ ̂𝑈𝑡+2∩ ̃𝑈𝑡+2.
5. Experiments
We conduct experiments to address the following questions.
(Q1)Can CS strategies be more effective than LO strategies for statistical arbitrage in commodity futures markets in
terms of risk and risk-adjusted return?
(Q2)Are TTM-dependent interrelationships among futures contracts instrumental for statistical arbitrage?
(Q3)Are both inter-commodity and intra-commodity relationships instrumental?
Specifically,weverifyEqs.(14)to(16)inthedata,togetherwithtradingexamplesofLObaselines,for(Q1);compare
our method against benchmarks in prediction and trading for(Q2); and conduct ablation studies for(Q3).
Baselines, Benchmarks, and Ablations. We consider the following LO strategy baselines for(Q1).
(B1)𝐰 𝑡= ̂𝐕𝑡∕𝟏⊤̂𝐕𝑡 where ̂𝐕𝑡=[Φ( ̂𝑌𝑡𝑐𝑑)](𝑐,𝑑)∈ ̂𝑈𝑡
(B2)𝐰 𝑡= ̂𝐕𝑡∕𝟏⊤̂𝐕𝑡 where ̂𝐕𝑡=cdf( ̂𝑌𝑡𝑐𝑑;[ ̂𝑌𝑡𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡 )
(B3)𝐰 𝑡= ̂𝐕𝑡∕𝟏⊤̂𝐕𝑡 where ̂𝐕𝑡=[ ̂𝑌𝑡𝑐𝑑 − ̂𝑌𝑡,min](𝑐,𝑑)∈ ̂𝑈𝑡 and ̂𝑌𝑡,min=min{ ̂𝑌𝑡𝑐′𝑑′ ∶(𝑐 ′,𝑑′)∈ ̂𝑈𝑡}
(B4)𝐰 𝑡 = 1 ̂ 𝑛𝑡 𝟏+𝑘𝐰 CS 𝑡 where𝑘= min{ 1 ̂ 𝑛𝑡|𝑤CS 𝑡𝑐𝑑| ∶ (𝑐,𝑑) ∈ ̂𝑈𝑡,𝑤CS 𝑡𝑐𝑑 <0}and𝐰 CS 𝑡 = [𝑤CS 𝑡𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡 is a CS weight
position vector for̂𝑈𝑡
Y. Hong and D. Klabjan, Preprint, June 25, 2026 12

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
The first equations of(B1)to(B4)ensure the unit sum requirement of LO positions, by scaling for(B1)to(B3)
and by using the zero sum property of CS positions for(B4). The where clauses guarantee the nonnegative weight
requirement of LO positions. From Eqs. (22) and (24), the first baseline transformŝ𝑌𝑡𝑐𝑑 into a prediction for
̂cdf( ̃𝑅◦ 𝑡𝑐𝑑;[ ̃𝑅◦ 𝑡𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡∩̃𝑈𝑡 ). The second baseline directly mapŝ𝑌𝑡𝑐𝑑 to its empirical cumulative distribution value
within the cross section[̂𝑌𝑡𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡 . The third baseline subtracts the minimum value of the predictions. The last
baseline is an inverse transformation of̌𝐰in Proposition 2. The four resulting baseline LO positions preserve the
ordering of the prediction or weight values:Φandcdfin the first two baselines are monotonically increasing, and the
translations in the last two do not change the order. Thus,(B1)to(B4)are natural transformations from a prediction
vector to an LO position vector.
The benchmarks for(Q2)include ridge linear regression, LightGBM (Ke, Meng, Finley, Wang, Chen, Ma, Ye
and Liu, 2017), and multi-layered perceptrons (MLP) to assess the importance of the information extracted from
commodity futures interrelationships. These methods take the node features𝐱𝑡𝑐𝑑, whose components are defined in
Eq. (29), as predictor vectors, and use𝑌𝑡+2,𝑐𝑑 defined in Eq. (22) as the prediction target, consistent with our method.
Ridge linear regression is adopted due to its strong theoretical grounding, robustness to multicollinearity, and role
as a canonical linear benchmark. As gradient-boosted tree methods have been shown to outperform neural networks
on numerous tabular datasets (Ke et al., 2017; Grinsztajn, Oyallon and Varoquaux, 2022; Shwartz-Ziv and Armon,
2022; McElfresh, Khandagale, Valverde, Prasad C, Ramakrishnan, Goldblum and White, 2023; Shmuel, Glickman
and Lazebnik, 2024), such as𝐱𝑡𝑐𝑑 in our study, we include LightGBM as a benchmark. We also include MLP as a
fundamental neural network baseline. The MLP consists of𝑙con hidden layers with𝑛hid hidden units, followed by a
final linear output layer. Since these benchmarks are non-graph methods, comparing them with our method shows the
value of incorporating relational information in commodity futures.
We also include graph neural networks (GNNs) as benchmarks for(Q2)to assess whether the TTM-dependence
is instrumental in extracting information from commodity futures relationships. To predict𝑌𝑡+2,𝑐𝑑 given 𝑡, the
GNNs use a graph(̂𝑈𝑡+2,𝐸𝑈𝑈+ 𝑡 ∪𝐸 𝑈𝑈− 𝑡 ,𝑋𝑡), where nodes represent contracts, edges encode positive and negative
correlations, and node features follow Eq. (29). Consistent with our method, we define𝐸𝑈𝑈+ 𝑡 = {((𝑐,𝑑),(𝑐′,𝑑′)) ∈
̂𝑈𝑡+2× ̂𝑈𝑡+2 ∶̂ 𝜌𝑡𝑐𝑑𝑐′𝑑′ ≥𝜌 ∗}and𝐸 𝑈𝑈− 𝑡 = {((𝑐,𝑑),(𝑐′,𝑑′)) ∈ ̂𝑈𝑡+2× ̂𝑈𝑡+2 ∶̂ 𝜌𝑡𝑐𝑑𝑐′𝑑′ ≤−𝜌 ∗}. Here,̂ 𝜌𝑡𝑐𝑑𝑐′𝑑′ is the
Pearson correlation computed from the accumulated pairs of(̃𝑅∗ 𝑡′′𝑐𝑑, ̃𝑅∗ 𝑡′′𝑐′𝑑′)over𝑡 ′′∈[1∶𝑡], using only time points
where both returns are available and at least𝑛min sam observations exist. Since GNNs capture contract relationships but
ignore TTMs, they serve to evaluate the importance of TTM dependence.
The GNN consists of an initial embedding layer,𝑙con interim layers, and a final head. The initial layer embeds𝑋𝑡
as𝑍 𝐺 𝑡,0 =𝜙(𝑋 𝑡𝑊G,𝑘0+𝟏𝐛 ⊤ G,𝑘0) ∈ℝ ̂ 𝑛𝑡×𝑛hid. Each interim layer propagates information over𝐸𝑈𝑈+ 𝑡 and𝐸 𝑈𝑈− 𝑡 : for
𝑙∈[1∶𝑙 con], the𝑙-th interim layer output is
𝑍𝐺 𝑡,𝑙=𝜙 ([ 𝜙(CONV(̂𝑈𝑡+2,𝐸𝑈𝑈+ 𝑡 ,𝑍𝐺 𝑡,𝑙−1;𝜃− 𝐺,𝑙)), 𝜙(CONV(̂𝑈𝑡+2,𝐸𝑈𝑈− 𝑡 ,𝑍𝐺 𝑡,𝑙−1;𝜃+ 𝐺,𝑙)) ] 𝑊𝐺,𝑘𝑙+𝟏𝐛⊤ 𝐺,𝑘𝑙 ) ∈ℝ ̂ 𝑛𝑡×𝑛hid
(43)
whereCONVdenotesagraphconvolution,and𝜃 − 𝐺,𝑙 and𝜃+ 𝐺,𝑙 arelearnableparameters.Afinalheadoutputsaprediction
vector[ ̂𝑌𝑡+2,𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡+2 =𝑍 𝐺 𝑡,𝑙con 𝑊𝐺,𝑘,𝐻 +𝟏𝐛⊤ 𝐺,𝑘,𝐻 ∈ℝ ̂ 𝑛𝑡. We consider the following ablations for(Q3), keeping all other components unchanged:
(A1)Replace𝑓 B 𝑘𝑙=𝑔 UU 𝑘𝑙 ◦𝑔CU 𝑘𝑙 ◦𝑔CC 𝑘𝑙 ◦𝑔UC 𝑘𝑙 with𝑓 B 𝑘𝑙=𝑔 UU 𝑘𝑙 ,
(A2)Replace𝑓 B 𝑘𝑙=𝑔 UU 𝑘𝑙 ◦𝑔CU 𝑘𝑙 ◦𝑔CC 𝑘𝑙 ◦𝑔UC 𝑘𝑙 with𝑓 B 𝑘𝑙=𝑔 CU 𝑘𝑙 ◦𝑔CC 𝑘𝑙 ◦𝑔UC 𝑘𝑙 .
Thesevariantsremoveinter-commodityandintra-commodityinformation,respectively.Comparingthemwiththefull
model verifies the necessity of the two relationships in(Q3).
Experimental settings.WeusedailycommodityfuturespricedatafromLSEGDatastreamaccessedviaWharton
ResearchDataServices. 4ThedataspanfromAug.1977toDec.2025andconsistof, 𝑐 and𝑐 foreach𝑐∈,and 𝑡
forfuturescontractslistedonCME,CBOT,NYMEX,COMEX,andeCBOTandtradedinU.S.dollars.Tradingdates
aredefinedasweekdaysonwhichthenumberoftradedcontracttickersexceeds50%oftheaverageoverthepreceding
4See Appendix Section C for details on data processing.
Y. Hong and D. Klabjan, Preprint, June 25, 2026 13

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
Table 1
Hyperparameter Grids
Method Hyperparameter Grid
Our method, GNN,(A2)CONV∈{GCN, SAGE, GAT},#params∈{10 4,105},𝜌 ∗∈{0.1,0.2,0.3},𝑙 conv∈{1,2,3}
Ridgeregularizer ∈ {10−10+0.1𝑖 ∶𝑖∈[0∶200] }
MLP,(A1)#params∈{10 4,105},𝑙 conv∈{1,2,3}
LightGBMlearning_rate∈ {0.02,0.05,0.1},num_leaves∈ {127,255},
min_child_weight∈ {100,3000},min_child_samples∈ {20,1000},
num_round∈ {100,500,1000},(top_rate,other_rate) ∈ {(0.05,0.05),
(0.05,0.10),(0.10,0.10),(0.15,0.10),(0.15,0.25),(0.20,0.10),(0.25,0.10)}
Figure 3:1-Year Rolling Average Rate of Satisfaction of Conditions (ii) in Propositions 1 and 3
365days.Sincefuturetradingdatesareunavailable,TTMandthedifferenceofmaturitiesareestimatedusingcalendar
dates. To ensure sufficient training samples, we set𝑡1 as the first trading date in 2016, define𝑡𝑘 as the first trading
date of each subsequent year, and set𝑛fit = 10. We conduct stratified sampling forval 𝑘 to mitigate the influence of period-specificmarketeffects,treatingeachmonthasaseparatestratum.Weset𝜏 maxtooneyear,𝑛 bas=52(thenumber
of weeks in a year), and𝑛min sam = 28that ensures 99% of contracts to be traded in the testing period. Statistics of the
tradinguniverseareprovidedinAppendixSectionE.Since ̂𝑈𝑡 cancontainunobservablecontracts,i.e.,contractswith ̃𝑉𝑡−1,𝑐𝑑 ̃𝑉𝑡,𝑐𝑑 =0, ̃𝑅𝑡,𝑐𝑑 is unavailable for such contracts; thus, we compute Eq. (6) aŝΠ(𝐰𝑡𝑐)= ∑ 𝑑∈ ̂𝐷𝑡𝑐∩̃𝐷𝑡𝑐 𝑤𝑡𝑐𝑑 ̃𝑅𝑡𝑐𝑑. Weevaluatetestperformanceusinghyperparametersselectedbyvalidationforeachperiod.Foreach𝑘∈[1∶𝑛 fit]
andeachmethod,wetrainmodelsoveritshyperparametergridon fit 𝑘 ,selectthebestconfigurationbasedonvalidation
performanceon val 𝑘 ,andevaluateon test 𝑘 .ThegridsaregiveninTable1.WeuseGCN(KipfandWelling,2017),GAT (Veličković, Cucurull, Casanova, Romero, Liò and Bengio, 2018), and SAGE (Hamilton, Ying and Leskovec, 2017)
due to their wide usage (Fey and Lenssen, 2019). Although larger models may improve performance, the ranges of
#params,𝑙conv,𝜌∗ areappropriateforthepurposeofthisstudybasedontheselectedconfigurationcountsinAppendix
Section D. For each model,𝑛hid is chosen to achieve the closest match to the target#params. We set𝜙to the SiLU
(Ramachandran,ZophandLe,2017;HendrycksandGimpel,2023),andusedefaultCONVhyperparametersfromthe
original papers. For LightGBM, we use the grid generated from the best configurations reported in its original paper
appendix (Ke et al., 2017), set remaining parameters to defaults in (Microsoft, 2026a,b), and apply early stopping as
in (Ke et al., 2017). In total, 8,790 models are trained across ten periods: 540 each for our method, GNN, and(A2);
2,010 for ridge; 60 each for MLP and(A1); and 5,040 for LightGBM.
Experimental resultsare summarized in Tables 2 to 4 and Figures 3 and 4. HGL denotes our hierarchical graph
learning method, with HGL-GAT/GCN/SAGE specifyingCONV=GAT∕GCN∕SAGE; GNN-GAT/GCN/SAGE are
definedanalogously.HGLandGNNarethebestconvolutionmethodsselectedfromGAT,GCN,andSAGEperperiod
based on validation performance. In Table 2 and Figure 4, the daily CS position vectors are computed via Eqs. (18)
to (20) wherê𝑌𝑡𝑐𝑑 are the corresponding model predictions. In Table 2, the daily LO position vectors (except for the
equal-weight(EW)strategyandS&P500)arecomputedfromthepredictionsorCSweightsofHGL.TheEWstrategy
assigns equal positive weights across contracts. In Table 2, IR and SR measure risk-adjusted return; Vol and MDD
measure risk; Tvr proxies transaction costs; and Cor measures diversification benefits relative to the S&P 500 (lower
Y. Hong and D. Klabjan, Preprint, June 25, 2026 14

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
Figure 4:Cumulative Sum of Profit and Loss, under the trading scheme in which each day half of the portfolio weight is
long and the other half is short. The jumps in 2020 and 2022 may be associated with COVID-19 and the Russo-Ukrainian
war, respectively.
Table 2
Trading Performance Across Methods (IR: information ratio; SR: Sortino ratio; Ret(%): average daily return (%); Vol(%):
daily return volatility (%); Hit: hit ratio; MDD: maximum drawdown (absolute); Tvr: average daily turnover; Cor: correlation
with the S&P 500). Under typical margin ratios, the actual daily returns (except for the S&P 500) can exceed the Ret
values reported below by at least a factor of8.33=1∕0.12. For example, the actual HGL daily return can exceed 0.08634%.
This is because the Ret values below are reported under the unit-margin assumption in Section 3, whereas typical margin
ratios in practice are 3–12% (CME Group, n.d.a) and even lower for spreads (CME Group, n.d.b).
IR SR Ret (%) Vol (%) MDD Hit Tvr Cor
Strategy Method
CS HGL0.08459 0.12409 0.010360.122490.02002 0.539590.55726 -0.01850
Ridge 0.03299 0.04306 0.00517 0.15685 0.05074 0.50696 0.62866 0.04576
MLP 0.03233 0.04963 0.00487 0.15050 0.05609 0.51134 0.51328 0.02198
LGBM 0.04324 0.06834 0.00645 0.14922 0.03893 0.51612 0.65431 0.03262
GNN 0.01492 0.02131 0.00254 0.17031 0.05710 0.50378 0.59353 0.04165
(A1)0.07583 0.11027 0.008270.109040.02367 0.534420.53363 -0.03402
(A2)0.04420 0.06526 0.00609 0.13789 0.03028 0.52129 0.53653 0.01235
LO(B1)0.03266 0.04398 0.02605 0.79765 0.34652 0.53124 0.04710 0.30209
(B2)0.03606 0.04927 0.027850.772390.31870 0.53004 0.27418 0.29924
(B3)0.03825 0.05234 0.02994 0.782790.316910.52845 0.246090.29897
(B4)0.03691 0.05018 0.02944 0.79753 0.33267 0.53084 0.21805 0.30171
EW 0.03224 0.04337 0.02576 0.79910 0.34957 0.531240.039470.30227
S&P 5000.04836 0.05815 0.055251.14240 0.382490.547151.00000
is better).5 HGL achieves the highest risk-adjusted returns, measured by IR and SR, indicating the strongest statistical
arbitrage performance.6 We address each of(Q1)to(Q3)based on these results.
(Q1)We find strong empirical support for the effectiveness of CS strategies over LO strategies for statistical
arbitrage, as the assumptions in Propositions 1 and 3 hold with high probability. Specifically, on average, 81.109%
of(𝑡,𝑐)pairsinourtradinguniversesatisfybothEqs.(14)and(15)associatedwithProposition1,and99.976%satisfy
Eq.(16)forProposition3.InFigure3,theconditionsinPropositions1and3holdforatleast70%and99%,respectively,
indicatingthatCSstrategiesexhibitlowervarianceanddeltainalargefractionofcases.Moreover,byProposition2(ii),
ifanLOstrategyachievessufficientlyhighexpectedreturnsascharacterizedtherein,thenthedemeanedCSstrategycan
outperform the LO strategy, asVar(Π(𝐰))>Var(Π(̌𝐰))holds in a large fraction of cases. Note that these percentages
do not imply CS underperformance otherwise; rather, they indicate that theoretical superiority is not established in
those cases.
5Additionally, yearly metrics are provided in Appendix Section F.
6Investment objectives in finance typically focus on maximizing risk-adjusted returns (Sharpe, 1966, 1998).
Y. Hong and D. Klabjan, Preprint, June 25, 2026 15

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
Table 3
MSEofPredictionModels.ThefirstrowindicatesthemodelselectedfromGAT,GCN,andSAGEbasedonvalidationperformance
for each period.
Model MSE Model MSE
HGL1.125511GNN 1.126562
HGL-GAT 1.125746 GNN-GAT 1.126513
HGL-GCN 1.125513 GNN-GCN 1.126587
HGL-SAGE 1.125342 GNN-SAGE 1.126562
LGBM1.126221Ridge 1.127108
MLP 1.126497
Table 4
P-values from Paired Statistical Tests of MSE Differences between HGL and Benchmark Models. The first two tests assess
the significance of the differences, while the last two columns evaluate the underlying assumptions: the Shapiro–Wilk test
assesses the normality of the paired differences (for the t-test), and the symmetry test (Miao, Gel and Gastwirth, 2006)
examines distributional symmetry (for the Wilcoxon test).
Paired T Wilcoxon Signed Rank Shapiro-Wilk Symmetry
GNN 6.27e-058.14e-057.81e-10 8.74e-01
GNN-GAT1.68e-042.95e-05 1.59e-02 9.99e-01
GNN-GCN 1.96e-054.88e-053.34e-05 9.99e-01
GNN-SAGE 6.27e-058.14e-057.81e-10 8.74e-01
MLP 6.22e-052.29e-056.80e-03 2.13e-01
Ridge8.01e-095.52e-08 1.42e-01 2.43e-01
LGBM2.14e-031.36e-03 1.32e-01 9.13e-01
Furthermore, Table 2 provides an empirical example of the effectiveness of CS trading. HGL achieves more than
twicetheIRandSR,morethansixtimeslowervolatility,andmorethanfifteentimeslowerMDDthantheLObaselines
(B1)to(B4)and the EW strategy. These results are consistent with the propositions, showing that CS strategies can
deliver both lower risk and higher risk-adjusted return than LO strategies. Moreover, HGL outperforms the S&P 500,
with over 75% higher IR, 113% higher SR, nine times lower volatility, and nineteen times lower MDD, indicating
stronginvestmentpotential.Italsoexhibitsnear-zerocorrelationwiththeS&P500,implyingsubstantialdiversification
benefitswheninvestedalongsidetraditionalequities.AttypicalmarginratiosemployedbyCMEGroup(CMEGroup,
n.d.a,n), HGL’s daily return is 188% and 56% higher than those of the LO baselines and the S&P 500, respectively.
(Q2)FromtheoutperformanceofHGLinFigure4andtables2to4,wefindthatTTM-dependentinterrelationships
betweenfuturescontractsareinstrumentalforbothtradingandprediction.ThecumulativesumP&LofHGLisstable
and upward-sloping in Figure 4, compared to the other benchmarks. In Table 2, HGL consistently outperforms the
non-graph CS benchmarks (Ridge, MLP, LGBM, and GNN) across all the key metrics: higher IR, SR, daily return,
and hit ratio; and lower volatility and MDD. These results stem from the better prediction of HGL. All HGL models
achievelowerMSEs(Table3)thanthebenchmarks,withdifferencesstatisticallysignificantatthe0.01level(Table4)
based on paired tests listed in Hong and Klabjan, 2025a using daily MSEs. Since HGL outperforms the non-graph
methods, futures interrelationships are informative; since it also outperforms GNNs, TTM dependence is important
for capturing these relationships.
(Q3)We confirm that both inter- and intra-commodity relationships are instrumental. In Table 2, although(A1)
performs better than(A2), neither achieves IR and SR comparable to HGL, indicating that both types of relationships
are informative. Hence, both are important for extracting information from futures contract relationships.
Future work.Although our method generates statistical arbitrage and demonstrates the effectiveness of CS
strategies and the importance of TTM-dependent futures interrelationships, there remains room for future research.
Due to limited and contract-specific data availability, this study does not account for margin ratios or transaction
costs;incorporatingthesefactorsisanimportantdirection.WhileHGLcapturestheTTM-dependentinterrelationship
information,theexactnatureoftheextractedinformationremainsunclearduetotheblack-boxnatureofdeeplearning
Y. Hong and D. Klabjan, Preprint, June 25, 2026 16

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
methods,motivatingfurtherstudy.AlthoughCSstrategiescanoutperformLOstrategies,theircombinationmayyield
additional gains under certain conditions, which presents an interesting direction for further study.
6. Conclusion
This paper proposes a hierarchical graph learning approach for CS strategies in commodity futures markets,
bridging two key gaps in the machine-learning literature: (i) the absence of learning-based methods for CS strategies
in futures markets, and (ii) the lack of consideration for maturity-dependent interrelationships among commodity
futures. We establish the efficacy of CS strategies by proving that they can exhibit higher risk-adjusted returns
and lower risk than long-only strategies. We also present a method to transform predictions into CS positions.
Next, we develop a hierarchical graph learning method that predicts futures price movements by leveraging TTM-
dependentinterrelationshipsamongfutures,therebyyieldingatradingalgorithm.Theexperimentsdemonstratethatthe
hierarchical graph learning and resulting CS positions outperform benchmarks in prediction and trading, respectively.
We find that maturity-dependent interrelationships across commodity futures are important and that CS trading based
on hierarchical graph learning is effective for statistical arbitrage.
Y. Hong and D. Klabjan, Preprint, June 25, 2026 17

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
Declaration on the Use of Generative AI and AI-Assisted Technologies in Manuscript
Preparation
In preparing this work, the authors used ChatGPT to assist with English-language editing, such as grammar
correction and translation.
References
Angelidis, T., Sakkas, A., Tessaromatis, N., 2025. Predicting commodity returns: Time series vs. cross sectional prediction models. Journal of
Commodity Markets 38, 100475.
Baruník, J., Malinska, B., 2016. Forecasting the term structure of crude oil futures prices with neural networks. Applied Energy 164, 366–379.
Boakye, E.O., Heimonen, K., Junttila, J., 2024. Commodity markets and the global macroeconomy: Evidence from machine learning and GVAR.
Empirical Economics 67, 1919–1965.
Boons, M., Prado, M.P., 2019. Basis-momentum. The Journal of Finance 74, 239–279.
Brennan, M.J., 1976. The supply of storage, in: The Economics of Futures Trading. Springer, pp. 100–107.
Cai, X.J., Fang, Z., Chang, Y., Tian, S., Hamori, S., 2020. Co-movements in commodity markets and implications in diversification benefits.
Empirical Economics 58, 393–425.
Casassus, J., Collin-Dufresne, P., 2005. Stochastic convenience yield implied from commodity futures and interest rates. The Journal of Finance
60, 2283–2331.
Chng, M.T., 2009. Economic linkages across commodity futures: Hedging and trading implications. Journal of Banking & Finance 33, 958–970.
Clarke, R.G., De Silva, H., Thorley, S., 2013. Fundamentals of futures and options. CFA Institute Research Foundation 3.
CME Group, n.d.a. The benefits of futures margins. URL:https://www.cmegroup.com/education/courses/
understanding-the-benefits-of-futures/the-benefits-of-futures-margins. online; accessed 30 March 2026.
CME Group, n.d.b. Understanding futures spreads: futures spread overview. URL:https://www.cmegroup.com/education/courses/
understanding-futures-spreads/futures-spread-overview. online; accessed 30 March 2026.
Fengqian,D.,Chao,L.,2020. Anadaptivefinancialtradingsystemusingdeepreinforcementlearningwithcandlestickdecomposingfeatures. IEEE
Access 8, 63666–63678.
Fey, M., Lenssen, J.E., 2019. Fast graph representation learning with PyTorch Geometric. arXiv preprintarXiv:1903.02428.
Furlong, F., Ingenito, R., 1996. Commodity prices and inflation. Economic Review-Federal Reserve Bank of San Francisco , 27–47.
Gabrielsson,P.,Johansson,U.,2015. High-frequencyequityindexfuturestradingusingrecurrentreinforcementlearningwithcandlesticks,in:2015
IEEE Symposium Series on Computational Intelligence, IEEE. pp. 734–741.
Gibson, R., Schwartz, E.S., 1990. Stochastic convenience yield and the pricing of oil contingent claims. The Journal of Finance 45, 959–976.
Glorot, X., Bengio, Y., 2010. Understanding the difficulty of training deep feedforward neural networks, in: Proceedings of the Thirteenth
International Conference on Artificial Intelligence and Statistics, PMLR. pp. 249–256.
Gospodinov, N., Ng, S., 2013. Commodity prices, convenience yields, and inflation. Review of Economics and Statistics 95, 206–219.
Grinsztajn, L., Oyallon, E., Varoquaux, G., 2022. Why do tree-based models still outperform deep learning on typical tabular data?, in: Advances
in Neural Information Processing Systems, Curran Associates, Inc.. pp. 507–520.
Guijarro-Ordonez, J., Pelger, M., Zanotti, G., 2025. Deep learning statistical arbitrage. Management Science 0.
Hamilton, W., Ying, Z., Leskovec, J., 2017. Inductive representation learning on large graphs, in: Advances in Neural Information Processing
Systems, Curran Associates, Inc.
Hammoudeh, S.,Sari, R., Ewing, B.T.,2009. Relationships amongstrategic commodities andwith financial variables: Anew look. Contemporary
Economic Policy 27, 251–264.
Hendrycks, D., Gimpel, K., 2023. Gaussian error linear units (GELUs). arXiv preprintarXiv:1606.08415.
Hong, Y., Kim, Y., Kim, J., Choi, Y., 2023. Index tracking via learning to predict market sensitivities, in: Proceedings of SAI Intelligent Systems
Conference, Springer. pp. 111–131.
Hong, Y., Klabjan, D., 2025a. Graph learning for foreign exchange rate prediction and statistical arbitrage, in: Proceedings of the 6th ACM
International Conference on AI in Finance, ACM. pp. 692–699.
Hong, Y., Klabjan, D., 2025b. Statistical arbitrage in options markets by graph learning and synthetic long positions. arXiv preprint
arXiv:2508.14762.
Hu, M., Tan, Z., Liu, B., Yin, G., 2025. Graph portfolio: High-frequency factor predictors via heterogeneous continual GNNs. IEEE Transactions
on Knowledge and Data Engineering 37, 4104–4116.
Hull,J.,Treepongkaruna,S.,Colwell,D.,Heaney,R.,Pitt,D.,2013.Fundamentalsoffuturesandoptionsmarkets.8thed.,PearsonHigherEducation
AU.
Hung, C.C., Chen, Y.J., 2021. DPP: Deep predictor for price movement from candlestick charts. Plos One 16, e0252404.
Ji, Q., Fan, Y., 2012. How does oil price volatility affect non-energy commodity markets? Applied Energy 89, 273–280.
Kaur, B., Sidhu, B.K., Bhathal, G.S., 2025. A hybrid deep reinforcement learning approach for algorithmic trading in commodity futures markets.
Applied Computational Intelligence and Soft Computing 2025, 5993683.
Ke, G., Meng, Q., Finley, T., Wang, T., Chen, W., Ma, W., Ye, Q., Liu, T.Y., 2017. LightGBM: A highly efficient gradient boosting decision tree,
in: Advances in Neural Information Processing Systems, Curran Associates, Inc.
Kipf, T.N., Welling, M., 2017. Semi-supervised classification with graph convolutional networks, in: International Conference on Learning
Representations.
Lazzarino, M., Berrill, J., Šević, A., et al., 2018. What is statistical arbitrage? Theoretical Economics Letters 8, 888–908.
LeCun, Y., Bottou, L., Orr, G.B., Müller, K.R., 2002. Efficient backprop, in: Neural networks: Tricks of the Trade. Springer, pp. 9–50.
Y. Hong and D. Klabjan, Preprint, June 25, 2026 18

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
Li,J.,Li,G.,Liu,M.,Zhu,X.,Wei,L.,2022. Anoveltext-basedframeworkforforecastingagriculturalfuturesusingmassiveonlinenewsheadlines.
International Journal of Forecasting 38, 35–50.
Liu,J.,Lu,L.,Zong,X.,Xie,B.,2023. Nonlinearrelationshipsinsoybeancommoditiespairstrading-testbydeepreinforcementlearning. Finance
Research Letters 58, 104477.
Markowitz, H., 1952. Portfolio selection. The Journal of Finance 7, 77–91.
Maslyuk,S.,Smyth,R.,2009. Cointegrationbetweenoilspotandfuturepricesofthesameanddifferentgradesinthepresenceofstructuralchange.
Energy Policy 37, 1687–1693.
Massahi, M., Mahootchi, M., 2024. A deep q-learning based algorithmic trading system for commodity futures markets. Expert Systems with
Applications 237, 121711.
McElfresh, D., Khandagale, S., Valverde, J., Prasad C, V., Ramakrishnan, G., Goldblum, M., White, C., 2023. When do neural nets outperform
boosted trees on tabular data?, in: Advances in Neural Information Processing Systems, Curran Associates, Inc.. pp. 76336–76369.
Miao,W.,Gel,Y.R.,Gastwirth,J.L.,2006. Anewtestofsymmetryaboutanunknownmedian,in:RandomWalk,SequentialAnalysisandRelated
Topics: A Festschrift in Honor of Yuan-Shih Chow. World Scientific, pp. 199–214.
Microsoft,2026a.Lightgbmdocumentation.URL:https://lightgbm.readthedocs.io/en/latest/Python-Intro.html.online;accessed
30 March 2026.
Microsoft, 2026b. Lightgbm python package. URL:https://pypi.org/project/lightgbm/. online; accessed 30 March 2026.
Mitchell, D., 2008. A note on rising food prices. World Bank Policy Research Working Paper .
Nazlioglu, S., 2011. World oil and agricultural commodity prices: Evidence from nonlinear causality. Energy Policy 39, 2935–2943.
Ramachandran, P., Zoph, B., Le, Q.V., 2017. Searching for activation functions. arXiv preprintarXiv:1710.05941.
Schwartz, E.S., 1997. The stochastic behavior of commodity prices: Implications for valuation and hedging. The Journal of Finance 52, 923–973.
Sharpe, W.F., 1966. Mutual fund performance. The Journal of Business 39, 119–138.
Sharpe, W.F., 1998. The Sharpe ratio. Streetwise—the Best of the Journal of Portfolio Management 3, 169–85.
Shmuel, A., Glickman, O., Lazebnik, T., 2024. A comprehensive benchmark of machine and deep learning across diverse tabular datasets. arXiv
preprintarXiv:2408.14817.
Shwartz-Ziv, R., Armon, A., 2022. Tabular data: Deep learning is not all you need. Information Fusion 81, 84–90.
Sun, T., Wang, J., Ni, J., Cao, Y., Liu, B., 2019. Predicting futures market movement using deep neural networks, in: 2019 18th IEEE International
Conference On Machine Learning And Applications (ICMLA), IEEE. pp. 118–125.
Szymanowska,M.,DeRoon,F.,Nijman,T.,VanDenGoorbergh,R.,2014. Ananatomyofcommodityfuturesriskpremia. TheJournalofFinance
69, 453–482.
Tan, Z., Hu, M., Liu, B., Yin, G., 2024. Futures quantitative investment with heterogeneous continual graph neural network, in: 2024 IEEE
International Conference on Data Mining (ICDM), IEEE. pp. 851–856.
Vacha,L.,Janda,K.,Kristoufek,L.,Zilberman,D.,2013. Time-frequencydynamicsofbiofuel-fuel-foodsystem. EnergyEconomics40,233–241.
Veličković,P.,Cucurull,G.,Casanova,A.,Romero,A.,Liò,P.,Bengio,Y.,2018.Graphattentionnetworks,in:InternationalConferenceonLearning
Representations.
Wang, J., Wu, J., Zhang, G., Tan, M., Chen, S., Lin, Z., 2025. Agricultural futures trading decision using AI agent with multiscale candlestick
analysis. IEEE Transactions on Computational Social Systems .
Wang, S., Zhang, T., 2024. Predictability of commodity futures returns with machine learning models. Journal of Futures Markets 44, 302–322.
Xu, X., Zhang, Y., 2023. Neural network predictions of the high-frequency CSI300 first distant futures trading volume. Financial Markets and
Portfolio Management 37, 191–207.
Zhang, L., Wang, J., Wang, B., 2020. Energy market prediction with novel long short-term memory network: Case study of energy futures index
volatility. Energy 211, 118634.
Y. Hong and D. Klabjan, Preprint, June 25, 2026 19

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
A. Proofs of Propositions
A.1. Proof of Proposition 1
Proof.Fix𝑡∈ℕand𝑐∈ ̂𝐶𝑡. We suppress the subscripts(𝑡,𝑐)and write𝑤𝑑 =𝑤 𝑡𝑐𝑑,𝜎 𝑑𝑑′ =𝜎 𝑡𝑐𝑑𝑑′,𝜌 𝑑𝑑′ =𝜌 𝑡𝑐𝑑𝑑′,
̂ 𝑛=̂ 𝑛𝑡𝑐,𝜅=𝜅 𝑡𝑐,𝑅 𝑑 =𝑅 𝑡𝑐𝑑, ̂𝐷= ̂𝐷𝑡𝑐, LO = 𝑡𝑐,LO, andCS = 𝑡𝑐,CS. Let𝜎𝑑 = √𝜎𝑑𝑑,𝜎 min = min𝑑∈ ̂𝐷𝜎𝑑,
𝜎max=max 𝑑∈ ̂𝐷𝜎𝑑, and𝜌∗=min 𝑑,𝑑′∈ ̂𝐷𝜌𝑑𝑑′. Let𝐰=[𝑤 𝑑]𝑑∈ ̂𝐷∈ LO and𝐰′=[𝑤 ′ 𝑑]𝑑∈ ̂𝐷∈ CS be arbitrary.
(i) Assume that𝜌∗ >(𝜅 2−2‖𝐰‖2 2)(3−2‖𝐰‖ 2 2)−1 and𝜌 ∗ ≥0. We obtain Eq. (A.1) from Eq. (6) and Eq. (A.2)
from the definition of𝜌∗. Pulling out𝜌∗∑ 𝑑∈ ̂𝐷𝑤2 𝑑𝜎2 𝑑 from the first term of Eq. (A.2) and adding it to the second term
of Eq. (A.2), we have Eq. (A.3) since𝜌∗∑ 𝑑,𝑑′∈ ̂𝐷𝑤𝑑𝑤𝑑′𝜎𝑑𝜎𝑑′ =𝜌 ∗(∑ 𝑑∈ ̂𝐷𝑤𝑑𝜎𝑑)2. Since𝜎2 𝑑 ≥𝜎 2 min for all𝑑∈ ̂𝐷,
and𝟏 ⊤𝐰=1, we obtain Eq. (A.4).
Var(Π(𝐰))=
∑
𝑑,𝑑′∈ ̂𝐷
𝑤𝑑𝑤𝑑′𝜎𝑑𝑑′ =
∑
𝑑∈ ̂𝐷
𝑤2 𝑑𝜎2 𝑑+ ∑
𝑑,𝑑′∈ ̂𝐷∶𝑑≠𝑑′
𝑤𝑑𝑤𝑑′𝜎𝑑𝜎𝑑′𝜌𝑑𝑑′ (A.1)
≥
∑
𝑑∈ ̂𝐷
𝑤2 𝑑𝜎2 𝑑+𝜌∗ ∑
𝑑,𝑑′∈ ̂𝐷∶𝑑≠𝑑′
𝑤𝑑𝑤𝑑′𝜎𝑑𝜎𝑑′ (A.2)
=(1−𝜌 ∗) ∑
𝑑∈ ̂𝐷
𝑤2 𝑑𝜎2 𝑑+𝜌∗( ∑
𝑑∈ ̂𝐷
𝑤𝑑𝜎𝑑)2 (A.3)
≥𝜎 2 min ((1−𝜌 ∗)‖𝐰‖2 2+𝜌∗) (A.4)
We obtain Eq. (A.5) from Eq. (6). We have Eq. (A.6) since𝑤′ 𝑑 =[𝑤 ′ 𝑑]+−[−𝑤′ 𝑑]+. Since𝜎𝑑𝜎𝑑′𝜌∗ ≤𝜎 𝑑𝜎𝑑′𝜌𝑑𝑑′ = 𝜎𝑑𝑑′ ≤𝜎 𝑑𝜎𝑑′, we obtain Eq. (A.8). Since𝐰′ is a CS position weight vector, we have∑ 𝑑∈ ̂𝐷[𝑤′ 𝑑]+= ∑ 𝑑∈ ̂𝐷[−𝑤′ 𝑑]+=
1∕2from Eq. (5). Then, we have𝜎2 max∕4 =𝜎 2 max(∑ 𝑑∈ ̂𝐷[𝑤′ 𝑑]+)2 ≥( ∑ 𝑑∈ ̂𝐷𝜎𝑑[𝑤′ 𝑑]+)2 since𝜎 𝑑 ≤𝜎 max, which
yields the upper bound of the first term of Eq. (A.9). Analogously, we obtain𝜎2 max∕4≥( ∑ 𝑑∈ ̂𝐷𝜎𝑑[−𝑤′ 𝑑]+)2, which yields the upper bound of the second term of Eq. (A.9). Therefore, we obtain Eq. (A.10) since∑ 𝑑∈ ̂𝐷𝜎𝑑[𝑤′ 𝑑]+ ≥ 𝜎min ∑ 𝑑∈ ̂𝐷[𝑤′ 𝑑]+=𝜎 min∕2and ∑ 𝑑∈ ̂𝐷𝜎𝑑[−𝑤′ 𝑑]+ ≥𝜎 min∕2.
Var(Π(𝐰′))= ∑
𝑑,𝑑′∈ ̂𝐷
𝑤′ 𝑑𝑤′ 𝑑′𝜎𝑑𝑑′ (A.5)
=
∑
𝑑,𝑑′∈ ̂𝐷
𝜎𝑑𝑑′
([𝑤′ 𝑑]+−[−𝑤′ 𝑑]+)([𝑤′ 𝑑′]+−[−𝑤′ 𝑑′]+) (A.6)
=
∑
𝑑,𝑑′∈ ̂𝐷
𝜎𝑑𝑑′[𝑤′ 𝑑]+[𝑤′ 𝑑′]++ ∑
𝑑,𝑑′∈ ̂𝐷
𝜎𝑑𝑑′[−𝑤′ 𝑑]+[−𝑤′ 𝑑′]+−2 ∑
𝑑,𝑑′∈ ̂𝐷
𝜎𝑑𝑑′[𝑤′ 𝑑]+[−𝑤′ 𝑑′]+ (A.7)
≤
∑
𝑑,𝑑′∈ ̂𝐷
𝜎𝑑𝜎𝑑′[𝑤′ 𝑑]+[𝑤′ 𝑑′]++ ∑
𝑑,𝑑′∈ ̂𝐷
𝜎𝑑𝜎𝑑′[−𝑤′ 𝑑]+[−𝑤′ 𝑑′]+−2𝜌∗ ∑
𝑑,𝑑′∈ ̂𝐷
𝜎𝑑𝜎𝑑′[𝑤′ 𝑑]+[−𝑤′ 𝑑′]+
(A.8)
=
(
∑
𝑑∈ ̂𝐷
𝜎𝑑[𝑤′ 𝑑]+
)2
+
(
∑
𝑑∈ ̂𝐷
𝜎𝑑[−𝑤′ 𝑑]+
)2
−2𝜌∗
(
∑
𝑑∈ ̂𝐷
𝜎𝑑[𝑤′ 𝑑]+
)(
∑
𝑑∈ ̂𝐷
𝜎𝑑[−𝑤′ 𝑑]+
)
(A.9)
≤𝜎 2 max(1 4+1 4)−2𝜌 ∗⋅ 𝜎min 2 ⋅ 𝜎min 2 = 1 2(𝜎2 max−𝜌∗𝜎2 min)(A.10)
Since𝟏 ⊤𝐰=1and𝑤 𝑑 ≥0, we have
‖𝐰‖2 2 ≤(𝟏 ⊤𝐰)2=1 (A.11)
and thus3−2‖𝐰‖ 2 2>0. From this, since𝜌∗>(𝜅 2−2‖𝐰‖2 2)(3−2‖𝐰‖ 2 2)−1, we obtain
𝜌∗(3−2‖𝐰‖ 2 2)>𝜅 2−2‖𝐰‖2 2,(A.12)
2(‖𝐰‖2 2+𝜌∗(1−‖𝐰‖ 2 2))>𝜅 2−𝜌∗,(A.13)
Y. Hong and D. Klabjan, Preprint, June 25, 2026 20

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
𝜎2 min ((1−𝜌 ∗)‖𝐰‖2 2+𝜌∗)> 1 2(𝜎2 max−𝜌∗𝜎2 min),(A.14)
wherethelastinequalityfollowsfromthedefinitionof𝜅 2.FromEqs.(A.4),(A.10)and(A.14),weobtainVar(Π(𝐰))>
Var(Π(𝐰′)).
(ii) Assume thatmin𝑑,𝑑′∈ ̂𝐷𝜌𝑡𝑐𝑑𝑑′ ≥0andmin 𝑑,𝑑′∈ ̂𝐷𝜌𝑡𝑐𝑑𝑑′ >(𝜅 2̂ 𝑛− 2)(3̂ 𝑛− 2)−1. We have𝜅2 <3since
(𝜅2̂ 𝑛−2)(3̂ 𝑛−2)−1=1+ (𝜅2−3)̂ 𝑛 3̂ 𝑛−2,̂ 𝑛is natural, and every correlation coefficient does not exceed one. Since𝟏⊤𝐰=1,
by the Cauchy-Schwarz inequality and Eq. (A.11), we obtain1∕̂ 𝑛≤‖𝐰‖2 2 ≤1. We thus have
3−2̂ 𝑛−1 ≥3−2‖𝐰‖ 2 2,(A.15)
(𝜅2̂ 𝑛−2)(3̂ 𝑛−2)−1=1+ 𝜅2−3 3−2̂ 𝑛−1 ≥ 𝜅2−3 3−2‖𝐰‖ 2 2 +1=(𝜅 2−2‖𝐰‖2 2)(3−2‖𝐰‖ 2 2)−1.(A.16)
Fromthisandtheassumption,weobtainmin 𝑑,𝑑′∈ ̂𝐷𝜌𝑡𝑐𝑑𝑑′ >(𝜅 2̂ 𝑛−2)(3̂ 𝑛−2)−1 ≥(𝜅 2−2‖𝐰‖2 2)(3−2‖𝐰‖ 2 2)−1.From (i), we obtainVar(Π(𝐰))>Var(Π(𝐰′)).
A.2. Proof of Proposition 2
Proof.Let𝐰∈ 𝑡𝑐,LO, ̄𝐰=𝟏∕̂ 𝑛𝑡𝑐 ∈ 𝑡𝑐,LO, and ̌𝐰= (𝐰− ̄𝐰)∕‖𝐰− ̄𝐰‖1 ∈ 𝑡𝑐,CS with𝐰≠ ̄𝐰. Since both
expectation and Eq. (6) are linear, we have
𝔼Π(𝐰− ̄𝐰)=𝔼Π(𝐰)−𝔼Π( ̄𝐰),(A.17)
𝔼Π(̌𝐰)= 𝔼Π(𝐰− ̄𝐰) ‖𝐰− ̄𝐰‖1 = 𝔼Π(𝐰)−𝔼Π( ̄𝐰) ‖𝐰− ̄𝐰‖1 .(A.18)
Due to the linearity of Eq. (6) and the property of variance, we have
Var(Π(̌𝐰))=Var
(Π(𝐰− ̄𝐰)
‖𝐰− ̄𝐰‖1
)
= Var(Π(𝐰− ̄𝐰))
‖𝐰− ̄𝐰‖2 1 .(A.19)
From Eqs. (A.18) and (A.19), sinceVar(Π(𝐰−̄𝐰))>0, we have
IR(Π(̌𝐰))= 𝔼Π(̌𝐰)√
Var(Π(̌𝐰))
= 𝔼[Π(𝐰− ̄𝐰)]∕‖𝐰− ̄𝐰‖1√
Var(Π(𝐰− ̄𝐰))∕‖𝐰− ̄𝐰‖2 1
= 𝔼Π(𝐰− ̄𝐰)√
Var(Π(𝐰− ̄𝐰))
=IR(Π(𝐰− ̄𝐰)).(A.20)
(i) Assume that Eq. (10) holds,Var(Π(𝐰−̄𝐰))>0, andVar(Π(𝐰))>0. From Eqs. (10) and (A.17), we obtain
IR(Π(𝐰− ̄𝐰))= 𝔼Π(𝐰−̄𝐰)√
Var(Π(𝐰−̄𝐰)) > [𝔼Π(𝐰)]+ √ Var(Π(𝐰) =[IR(Π(𝐰))] +, yieldingIR(Π(̌𝐰))>[IR(Π(𝐰))] + due to Eq. (A.20).
(ii)AssumethatEq.(11)holds,Var(Π(𝐰− ̄𝐰))>0,andVar(Π(𝐰))>Var(Π( ̌𝐰)).FromEq.(A.20),wehavethefirst
two equalities of Eq. (A.21). By the assumption and Eq. (A.19), we obtainVar(Π(𝐰))>Var(Π(̌𝐰)) =Var(Π(𝐰−̄𝐰)) ‖𝐰−̄𝐰‖2 1 , which yields the inequality between the third and fourth terms in Eq. (A.21) since𝔼[Π(𝐰−̄𝐰)]>0by Eqs. (11)
and (A.17). By Eqs. (11) and (A.17), we have𝔼Π(𝐰−̄𝐰)>‖𝐰− ̄𝐰‖1[𝔼Π(𝐰)]+, yielding the inequality between the
fourth and fifth terms in Eq. (A.21). From the following, we haveIR(Π(̌𝐰))>[IR(Π(𝐰))] +:
IR(Π(̌𝐰))=IR(Π(𝐰− ̄𝐰))= 𝔼[Π(𝐰− ̄𝐰)]√
Var(Π(𝐰− ̄𝐰))
> 𝔼[Π(𝐰− ̄𝐰)]
‖𝐰− ̄𝐰‖1
√
Var(Π(𝐰))
> ‖𝐰− ̄𝐰‖1[𝔼Π(𝐰)]+
‖𝐰− ̄𝐰‖1
√
Var(Π(𝐰))
=[IR(Π(𝐰))] +.
(A.21)
(iii) We assume that Eq. (12) holds,Var(Π(𝐰−̄𝐰)) = 0, andVar(Π(𝐰))>0. We have𝔼Π(̌𝐰)>0by Eqs. (12)
and (A.18) andVar(Π(̌𝐰)) = 0by Eq. (A.19) and the zero-variance assumption. Let𝐰= [𝑤𝑐𝑑]𝑑∈ ̂𝐷𝑡𝑐 . From Eq. (6),
𝔼Π(𝐰)=𝔼 ∑ 𝑑∈ ̂𝐷𝑡𝑐 𝑤𝑐𝑑𝑅𝑡𝑐𝑑 < ∑ 𝑑∈ ̂𝐷𝑡𝑐 𝔼𝑅𝑡𝑐𝑑 <∞, where the first inequality is because‖𝐰‖1=1and𝑤 𝑐𝑑 ≥0, and the last inequality follows from Eq. (1). Thus, we obtainIR(Π(𝐰))<∞sinceVar(Π(𝐰))>0.
Y. Hong and D. Klabjan, Preprint, June 25, 2026 21

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
A.3. Proof of Proposition 3
Proof.Fix𝑡∈ℕand𝑐∈ ̂𝐶𝑡.
(i) Let𝐰∈ 𝑡𝑐,LO, ̄𝐰=𝟏∕̂ 𝑛𝑡𝑐 ∈ 𝑡𝑐,LO, and ̌𝐰= (𝐰− ̄𝐰)∕‖𝐰− ̄𝐰‖1 ∈ 𝑡𝑐,CS with𝐰≠ ̄𝐰. Assume
thatΔ( ̄𝐰)>(1−‖𝐰− ̄𝐰‖1)Δ(𝐰). Then, we haveΔ(𝐰)> Δ(𝐰)−Δ(̄𝐰) ‖𝐰−̄𝐰‖1 . SinceΔ(⋅)is linear by its definition Eq. (7),
Δ(𝐰)−Δ(̄𝐰)
‖𝐰−̄𝐰‖1 =Δ( 𝐰−̄𝐰 ‖𝐰−̄𝐰‖1 )=Δ( ̌𝐰). Thus, we haveΔ(𝐰)>Δ(̌𝐰).
(ii) For each𝑑∈ ̂𝐷𝑡𝑐, we have
Δ𝑡−1,𝑐𝑑 ≥essinfΔ 𝑡−1,𝑐𝑑 ≥Δ min 𝑡−1,𝑐 a.s.,(A.22)
Δ𝑡−1,𝑐𝑑 ≤esssupΔ 𝑡−1,𝑐𝑑 ≤Δ max 𝑡−1,𝑐 a.s. (A.23)
Fix any𝐰=[𝑤 𝑑]𝑑∈ ̂𝐷𝑡𝑐 ∈ 𝑡𝑐,LO. From Eq. (7),Δ(𝐰)=∑ 𝑑∈ ̂𝐷𝑡𝑐 𝑤𝑑Δ𝑡−1,𝑐𝑑 ≥ ∑ 𝑑∈ ̂𝐷𝑡𝑐 𝑤𝑑Δmin 𝑡−1,𝑐 =Δ min 𝑡−1,𝑐 a.s., where the inequality follows from Eq. (A.22), and the last equality is because𝐰∈𝑡𝑐,LO. Therefore, we have
essinf
𝐰∈𝑡𝑐,LO
Δ(𝐰)≥Δ min 𝑡−1,𝑐.(A.24)
Redefine𝐰=[𝑤 𝑑]𝑑∈ ̂𝐷𝑡𝑐 ∈ 𝑡𝑐,CS. From Eq. (7), we obtain
Δ(𝐰)=
∑
𝑑∈ ̂𝐷𝑡𝑐
[𝑤𝑑]+Δ𝑡−1,𝑐𝑑 − ∑
𝑑∈ ̂𝐷𝑡𝑐
[−𝑤𝑑]+Δ𝑡−1,𝑐𝑑
≤
∑
𝑑∈ ̂𝐷𝑡𝑐
[𝑤𝑑]+Δmax 𝑡−1,𝑐− ∑
𝑑∈ ̂𝐷𝑡𝑐
[−𝑤𝑑]+Δmin 𝑡−1,𝑐 a.s.
= 1 2Δmax 𝑡−1,𝑐− 1 2Δmin 𝑡−1,𝑐 a.s.,
wherethefirstequalityisbecause𝑤 𝑑 =[𝑤 𝑑]+−[−𝑤𝑑]+,theinequalityisduetoEqs.(A.22)and(A.23),andthelast
equality is due to Eq. (5). Hence, we have
esssup
𝐰∈tc,CS
Δ(𝐰)≤ 1 2(Δmax 𝑡−1,𝑐−Δmin 𝑡−1,𝑐).(A.25)
If3Δ min 𝑡−1,𝑐 >Δ max 𝑡−1,𝑐, thenΔmin 𝑡−1,𝑐 > 1 2(Δmax 𝑡−1,𝑐−Δmin 𝑡−1,𝑐), yieldingessinf 𝐰∈𝑡𝑐,LOΔ(𝐰)>esssup 𝐰∈𝑡𝑐,CSΔ(𝐰)due to
Eqs. (A.24) and (A.25).
B. CS Weight Projection via Group Demeaning
Given a prediction vector̂𝐘𝑡=[ ̂𝑌𝑡𝑐𝑑](𝑐,𝑑)∈ ̂𝑈𝑡 ∈ℝ ̂ 𝑛𝑡, we obtain a projected CS weight vector𝐰𝑡 by computing:
𝐰𝑡= ̂𝐘◦ 𝑡∕‖̂𝐘◦ 𝑡‖1 (B.1)
where
̂𝐘◦ 𝑡 =[ ̂𝑌𝑡𝑐𝑑 − ̂𝑌∙ 𝑡𝑐](𝑐,𝑑)∈ ̂𝑈𝑡 ,(B.2)
̂𝑌∙ 𝑡𝑐 = 1 ̂ 𝑛𝑡𝑐 ∑ 𝑑′∈ ̂𝐷𝑡𝑐 ̂𝑌𝑡𝑐𝑑′. (B.3)
Eq. (B.1) corresponds to a scaling that enforces‖𝐰𝑡‖1 = 1. From the proof below, Eqs. (B.2) and (B.3) yield the
projection of̂𝐘𝑡 onto{𝐰 𝑡∈ℝ ̂ 𝑛𝑡 ∶𝟏 ⊤𝐰𝑡𝑐 =0,∀𝑐∈ ̂𝐶𝑡}. Therefore,𝐰𝑡 is, up to scaling, the CS weight vector closest
to ̂𝐘𝑡.
We now show that Eqs. (B.2) and (B.3) are the Euclidean projection of̂𝐘𝑡 onto{𝐰 𝑡 ∈ℝ ̂ 𝑛𝑡 ∶𝐸𝑞.(17)}. The
Euclidean projection is given by
̂𝐘′ 𝑡 =(𝐼 ̂ 𝑛𝑡−𝐺⊤ 𝑡 (𝐺𝑡𝐺⊤ 𝑡 )−1𝐺𝑡)̂𝐘𝑡 (B.4)
Y. Hong and D. Klabjan, Preprint, June 25, 2026 22

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
Table C.1
Summary of Maturity Date Replacements (Total Contracts: 26,461). The first row reports the number and ratio of issues
before the replacements. Each subsequent row reports the number of replacements made and the remaining number of
issues.
Replacement Type Replacements Remaining Issues Ratio (%)
Original 0 233 0.88
Replacement 1 78 155 0.59
Replacement 2 8 147 0.56
Replacement 3 147 0 0.00
where𝐼 ̂ 𝑛𝑡 ∈ℝ ̂ 𝑛𝑡×̂ 𝑛𝑡 is the identity matrix,𝐺𝑡 = [𝐠𝑡𝑐]𝑐∈ ̂𝐶𝑡 ∈ℝ | ̂𝐶𝑡|×̂ 𝑛𝑡, and𝐠𝑡𝑐 = [𝕀{𝑐′=𝑐}](𝑐′,𝑑′)∈̂𝑈𝑡 ∈ℝ ̂ 𝑛𝑡, because Eq. (17) is equivalent to𝐺𝑡𝐰𝑡=0. Note that
̂𝑌∙ 𝑡𝑐 = 1 ̂ 𝑛𝑡𝑐 𝐠⊤ 𝑡𝑐 ̂𝐘𝑡. (B.5)
The(𝑐 ′,𝑐′′)element of𝐺 𝑡𝐺⊤ 𝑡 is𝐠 ⊤ 𝑡𝑐′ 𝐠𝑡𝑐′′ =̂ 𝑛𝑡𝑐′ 𝕀{𝑐′=𝑐′′}. From this, we have𝐺𝑡𝐺⊤ 𝑡 =diag 𝑐∈𝐶𝑡(̂ 𝑛𝑡𝑐)and
𝐺⊤ 𝑡 (𝐺𝑡𝐺⊤ 𝑡 )−1𝐺𝑡̂𝐘𝑡 (B.6)
=[𝐠 𝑡𝑐1 𝐠𝑡𝑐2 …]⋅diag 𝑐∈𝐶𝑡(1∕̂ 𝑛𝑡𝑐)⋅[𝐠 ⊤ 𝑡𝑐1 ;𝐠⊤ 𝑡𝑐2 ;…] ̂𝐘𝑡 (B.7)
=
∑
𝑐∈ ̂𝐶𝑡
1
̂ 𝑛𝑡𝑐
𝐠𝑡𝑐𝐠⊤ 𝑡𝑐 ̂𝐘𝑡 (B.8)
=
∑
𝑐∈ ̂𝐶𝑡
̂𝑌∙ 𝑡𝑐𝐠𝑡𝑐 ∈ℝ ̂ 𝑛𝑡 (B.9)
by Eq. (B.5), where𝑐1 < 𝑐2 are the two smallest elements in̂𝐶𝑡. The component of Eq. (B.9) corresponding to(𝑐,𝑑)
is the commodity-wise averagê𝑌∙ 𝑡𝑐 for𝑐. From this and Eq. (B.4), the component of̂𝐘′ 𝑡 = (𝐼̂ 𝑛𝑡 −𝐺 ⊤ 𝑡 (𝐺𝑡𝐺⊤ 𝑡 )−1𝐺𝑡)̂𝐘𝑡
corresponding to(𝑐,𝑑)is ̂𝑌𝑡𝑐𝑑 − ̂𝑌∙ 𝑡𝑐. Hence, we havê𝐘′ 𝑡 = [̂𝑌𝑡𝑐𝑑 − ̂𝑌∙ 𝑡𝑐](𝑐,𝑑)∈ ̂𝑈𝑡 , implying that Eqs. (B.2) and (B.4)
coincide. Therefore, Eqs. (B.2) and (B.3) are the Euclidean projection of̂𝐘𝑡 onto{𝐰 𝑡∈ℝ ̂ 𝑛𝑡 ∶𝟏 ⊤𝐰𝑡𝑐 =0,∀𝑐∈ ̂𝐶𝑡}.
C. Data Processing
The maturity dates of futures contracts are initially estimated using their expiration dates, i.e., theLastTrdDate
field in theDSFutContrInfotable of the LSEG Datastream database provided by WRDS. However, for some
contracts,theestimatedmaturitydatesbasedonLastTrdDatediffersubstantiallyfromtheexpirationmonthrecorded
intheContrDatefieldofthesametable,whichreportsonlytheyearandmonthratherthantheexactdate.Toaddress
this discrepancy, we further refine the estimated maturity dates by applying the following replacements in sequence:
•Replacement 1:a validEndDatefield in theDSFutContrChgtable,
•Replacement 2:a validMaxDate, or
•Replacement 3:AppContrDate.
FollowingLSEG’srecommendation,weusetheEndDatefield.MaxDatedenotesthelatestdateonwhichthecontract
istradedintheprice-volumetableDSFutContrVal.Here,AppContrDatedenotestheapproximatedmaturitydate.It
iscomputedbyaddingthemediandifferencebetweenLastTrdDateandthe15thdayofContrDate,calculatedfrom
contracts with the same underlying commodity, to the 15th day ofContrDate. If the median is unavailable, we use
the 15th day ofContrDate. For a value ofEndDateandMaxDateto be valid, it should not be significantly different
fromAppContrDate. In addition,EndDateshould not be less thanMaxDateto be valid.
We use theDSFutContrValtable for the price-volume data, along with theDSFutContrInfotable. Following
the indication of theCurrUnitCodefield in theDSFutContrInfotable, we convert the unit of the price data.
Y. Hong and D. Klabjan, Preprint, June 25, 2026 23

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
Table D.1
Hyperparameter Selection Counts under Yearly Cross-Validation
HGL(A1) (A2)Individual MLP
#params 10000 3 5 6
100000 10 7 10 5 4
𝑙conv 1 1 7 1
2 3 1 3 4 6
3 7 8 5 4
𝜌∗ 0.1 10 9 4
0.2 1 2
0.3 4
CONV GAT 3 1
GCN 2 10 2
SAGE 5 7 10
Figure E.1:Time-Series Characteristics of the Trading Universe.
However, some contracts whose underlying commodity has other contracts requiring unit conversion, as indicated
byCurrUnitCode, are not indicated for scaling but exhibit substantially different price scales. We therefore rescale
these price data accordingly.
D. Hyperparameter Selection Statistics
EachentryinTableD.1reportsthenumberoftimesahyperparametervalueisselectedacrossthecross-validation
periods.
E. Trading Universe Characteristics
Figure E.1 summarizes the time-series characteristics of the trading universe used in our experiments.
F. Annual Trading Performance Metrics
Tables F.1 and F.2 present annual trading performance metrics.
Y. Hong and D. Klabjan, Preprint, June 25, 2026 24

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
Table F.1
Annual Trading Performance Metrics (IR: information ratio; SR: Sortino ratio; Ret(%): average daily return (%); Vol(%):
daily return volatility (%); Hit: hit ratio; MDD: maximum drawdown (absolute); Tvr: average daily turnover; Cor: correlation
with the S&P 500)
CS LO
HGL Ridge MLP LGBM GNN(A1) (A2) (B1) (B2) (B3) (B4)EW S&P 500
Metric Year
IR 2016 0.0611 0.0110 -0.0245 0.0017 0.0503 0.0547 0.0020 0.0592 0.0625 0.0649 0.0607 0.0587 0.0614
2017 0.1800 -0.0047 0.0536 0.1394 0.0618 0.1413 0.0769 0.0186 0.0229 0.0260 0.0257 0.0181 0.1712
2018 0.1211 -0.0132 0.0567 0.0746 -0.0292 0.1412 0.0514 -0.0394 -0.0343 -0.0341 -0.0326 -0.0398 -0.0324
2019 -0.0174 0.0036 -0.0587 -0.0299 -0.0663 -0.0111 -0.0258 0.0356 0.0372 0.0377 0.0343 0.0354 0.1474
2020 0.1214 0.0448 0.0494 0.1049 0.0797 0.1004 0.0979 0.0343 0.0387 0.0399 0.0419 0.0339 0.0367
2021 0.0185 0.0100 -0.0964 -0.0888 -0.1063 0.0181 -0.0603 0.1468 0.1461 0.1454 0.1489 0.1469 0.1261
2022 0.1123 0.0243 0.0756 0.0525 0.0244 0.0785 0.0566 0.0618 0.0639 0.0700 0.0681 0.0612 -0.0495
2023 0.0478 0.0656 0.0599 0.0482 0.0359 0.0456 0.0763 -0.0605 -0.0612 -0.0575 -0.0586 -0.0607 0.1009
2024 0.0906 0.0605 0.0146 0.0225 -0.0023 0.0982 0.0168 -0.0218 -0.0152 -0.0129 -0.0169 -0.0225 0.1202
2025 0.1435 0.1225 0.1179 0.0997 0.0781 0.1337 0.1228 0.0423 0.0513 0.0546 0.0490 0.0416 0.0541
SR 2016 0.0909 0.0150 -0.0360 0.0024 0.0697 0.0723 0.0028 0.1058 0.1109 0.1161 0.1084 0.1050 0.0804
2017 0.2980 -0.0070 0.0969 0.2430 0.0979 0.2433 0.1216 0.0295 0.0370 0.0420 0.0412 0.0287 0.2296
2018 0.1719 -0.0149 0.0798 0.1149 -0.0352 0.2136 0.0797 -0.0523 -0.0458 -0.0455 -0.0436 -0.0529 -0.0395
2019 -0.0236 0.0066 -0.0778 -0.0414 -0.0824 -0.0124 -0.0334 0.0529 0.0554 0.0563 0.0508 0.0526 0.1871
2020 0.1591 0.0561 0.0715 0.1692 0.1123 0.1412 0.1396 0.0402 0.0462 0.0476 0.0495 0.0397 0.0417
2021 0.0280 0.0154 -0.1471 -0.1299 -0.1421 0.0283 -0.0917 0.1908 0.1920 0.1905 0.1951 0.1908 0.1787
2022 0.2017 0.0303 0.1477 0.0998 0.0434 0.1316 0.0933 0.0822 0.0873 0.0961 0.0921 0.0813 -0.0793
2023 0.0719 0.0963 0.1092 0.0898 0.0605 0.0723 0.1279 -0.0959 -0.0963 -0.0906 -0.0919 -0.0962 0.1665
2024 0.1340 0.0830 0.0241 0.0330 -0.0036 0.1383 0.0244 -0.0353 -0.0248 -0.0210 -0.0274 -0.0363 0.1585
2025 0.2469 0.2250 0.1766 0.1751 0.1406 0.2114 0.2058 0.0589 0.0712 0.0764 0.0691 0.0577 0.0680
Ret (%) 2016 0.0043 0.0012 -0.0019 0.0002 0.0055 0.0037 0.0002 0.0449 0.0459 0.0477 0.0461 0.0446 0.0505
2017 0.0101 -0.0004 0.0046 0.0096 0.0052 0.0076 0.0056 0.0093 0.0112 0.0130 0.0129 0.0090 0.0723
2018 0.0120 -0.0022 0.0071 0.0091 -0.0056 0.0134 0.0063 -0.0217 -0.0187 -0.0188 -0.0180 -0.0220 -0.0351
2019 -0.0013 0.0004 -0.0050 -0.0028 -0.0077 -0.0008 -0.0025 0.0198 0.0201 0.0206 0.0191 0.0197 0.1136
2020 0.0213 0.0091 0.0127 0.0229 0.0212 0.0143 0.0212 0.0343 0.0372 0.0388 0.0421 0.0339 0.0797
2021 0.0023 0.0016 -0.0120 -0.0113 -0.0159 0.0019 -0.0077 0.1228 0.1206 0.1204 0.1238 0.1230 0.1033
2022 0.0231 0.0059 0.0188 0.0129 0.0065 0.0151 0.0125 0.0786 0.0774 0.0860 0.0856 0.0780 -0.0754
2023 0.0048 0.0089 0.0075 0.0070 0.0043 0.0043 0.0093 -0.0463 -0.0448 -0.0428 -0.0448 -0.0465 0.0833
2024 0.0111 0.0093 0.0017 0.0033 -0.0003 0.0096 0.0020 -0.0143 -0.0097 -0.0085 -0.0112 -0.0148 0.0959
2025 0.0160 0.0182 0.0153 0.0138 0.0122 0.0137 0.0141 0.0328 0.0389 0.0426 0.0383 0.0322 0.0640
Vol (%) 2016 0.0708 0.1053 0.0796 0.0917 0.1096 0.0679 0.0776 0.7580 0.7350 0.7362 0.7598 0.7600 0.8211
2017 0.0560 0.0852 0.0860 0.0690 0.0847 0.0536 0.0723 0.4986 0.4913 0.4977 0.5004 0.4988 0.4221
2018 0.0990 0.1682 0.1251 0.1216 0.1901 0.0951 0.1232 0.5518 0.5472 0.5503 0.5512 0.5522 1.0831
2019 0.0755 0.1016 0.0849 0.0931 0.1156 0.0748 0.0956 0.5556 0.5404 0.5455 0.5579 0.5566 0.7711
2020 0.1752 0.2041 0.2567 0.2180 0.2654 0.1420 0.2162 0.9990 0.9597 0.9708 1.0046 1.0016 2.1705
2021 0.1251 0.1583 0.1242 0.1276 0.1496 0.1039 0.1273 0.8360 0.8257 0.8282 0.8320 0.8370 0.8190
2022 0.2057 0.2423 0.2490 0.2451 0.2651 0.1919 0.2211 1.2709 1.2109 1.2292 1.2573 1.2742 1.5232
2023 0.1014 0.1360 0.1245 0.1450 0.1205 0.0947 0.1222 0.7647 0.7316 0.7449 0.7647 0.7667 0.8261
2024 0.1222 0.1530 0.1182 0.1474 0.1373 0.0982 0.1200 0.6548 0.6422 0.6593 0.6639 0.6549 0.7974
2025 0.1112 0.1486 0.1300 0.1386 0.1568 0.1022 0.1148 0.7745 0.7583 0.7797 0.7803 0.7745 1.1835
MDD 2016 0.0126 0.0154 0.0151 0.0144 0.0154 0.0090 0.0145 0.0905 0.0852 0.0825 0.0896 0.0912 0.0820
2017 0.0046 0.0144 0.0103 0.0059 0.0075 0.0066 0.0063 0.0746 0.0673 0.0686 0.0727 0.0751 0.0281
2018 0.0108 0.0300 0.0177 0.0190 0.0346 0.0066 0.0142 0.1186 0.1087 0.1103 0.1115 0.1194 0.2145
2019 0.0084 0.0104 0.0186 0.0144 0.0258 0.0101 0.0126 0.0881 0.0798 0.0783 0.0870 0.0889 0.0699
2020 0.0187 0.0230 0.0319 0.0286 0.0237 0.0144 0.0186 0.2884 0.2724 0.2737 0.2842 0.2896 0.3825
2021 0.0142 0.0216 0.0289 0.0277 0.0414 0.0152 0.0199 0.0668 0.0682 0.0674 0.0668 0.0667 0.0527
2022 0.0200 0.0507 0.0205 0.0267 0.0441 0.0209 0.0267 0.1862 0.1683 0.1677 0.1749 0.1876 0.2562
2023 0.0083 0.0169 0.0100 0.0152 0.0150 0.0089 0.0095 0.1539 0.1440 0.1447 0.1557 0.1547 0.1065
2024 0.0097 0.0152 0.0171 0.0145 0.0204 0.0072 0.0180 0.1362 0.1319 0.1291 0.1325 0.1368 0.0872
2025 0.0077 0.0160 0.0091 0.0094 0.0168 0.0088 0.0075 0.0939 0.0886 0.0893 0.0924 0.0942 0.2041
Hit 2016 0.5397 0.5119 0.5119 0.5159 0.5198 0.5357 0.5000 0.5198 0.5159 0.5238 0.5238 0.5198 0.5238
2017 0.5720 0.4680 0.5080 0.5680 0.5360 0.5600 0.5320 0.5360 0.5480 0.5480 0.5440 0.5360 0.5720
2018 0.5595 0.4960 0.4921 0.5040 0.4802 0.5714 0.5079 0.5040 0.5198 0.5159 0.5040 0.5040 0.5198
2019 0.4841 0.4722 0.5119 0.5040 0.5000 0.5198 0.5437 0.5357 0.5357 0.5278 0.5397 0.5357 0.5952
2020 0.5573 0.5296 0.5336 0.5573 0.5296 0.5375 0.5613 0.5573 0.5613 0.5534 0.5573 0.5573 0.5731
2021 0.5198 0.5278 0.4603 0.4603 0.4405 0.5119 0.4762 0.5833 0.5754 0.5754 0.5754 0.5833 0.5675
2022 0.5179 0.5020 0.4861 0.4861 0.4861 0.5179 0.5020 0.5697 0.5498 0.5578 0.5657 0.5737 0.4303
2023 0.5280 0.5320 0.5160 0.5240 0.5200 0.5280 0.5400 0.4760 0.4720 0.4640 0.4680 0.4760 0.5440
2024 0.5397 0.5278 0.5119 0.5159 0.4960 0.5317 0.5119 0.5159 0.5119 0.5079 0.5119 0.5119 0.5714
2025 0.5783 0.5020 0.5823 0.5261 0.5301 0.5301 0.5382 0.5141 0.5100 0.5100 0.5181 0.5141 0.5743
Y. Hong and D. Klabjan, Preprint, June 25, 2026 25

Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets
Table F.2
Annual Trading Performance Metrics (IR: information ratio; SR: Sortino ratio; Ret(%): average daily return (%); Vol(%):
daily return volatility (%); Hit: hit ratio; MDD: maximum drawdown (absolute); Tvr: average daily turnover; Cor: correlation
with the S&P 500)
CS LO
HGL Ridge MLP LGBM GNN(A1) (A2) (B1) (B2) (B3) (B4)EW S&P 500
Metric Year
Tvr 2016 0.5276 0.6454 0.4692 0.6413 0.5683 0.5884 0.5114 0.0582 0.2663 0.2512 0.2262 0.0547
2017 0.5583 0.6547 0.6300 0.7193 0.6138 0.5790 0.5902 0.0554 0.2882 0.2566 0.2318 0.0520
2018 0.6625 0.6705 0.4946 0.6540 0.7327 0.5235 0.5890 0.0500 0.3197 0.2444 0.2257 0.0431
2019 0.6274 0.4144 0.5628 0.6654 0.6017 0.5541 0.5415 0.0524 0.3078 0.2735 0.2481 0.0469
2020 0.5313 0.6429 0.5680 0.6852 0.5764 0.5615 0.5032 0.0472 0.2592 0.2532 0.2231 0.0430
2021 0.6155 0.6048 0.4857 0.6504 0.5687 0.4720 0.4963 0.0510 0.2984 0.2353 0.2180 0.0467
2022 0.5350 0.7176 0.5349 0.5913 0.5300 0.6061 0.5649 0.0483 0.2646 0.2492 0.2262 0.0466
2023 0.5039 0.8716 0.4988 0.6557 0.5084 0.4757 0.5332 0.0462 0.2595 0.2120 0.1948 0.0433
2024 0.5400 0.4508 0.4357 0.6471 0.6230 0.4480 0.5234 0.0471 0.2696 0.2576 0.2159 0.0426
2025 0.5149 0.6623 0.5022 0.6805 0.6556 0.5749 0.5621 0.0496 0.2667 0.2881 0.2324 0.0462
Cor 2016 0.0300 0.0181 0.1579 0.1066 0.1552 0.0461 0.1137 0.3874 0.3834 0.3816 0.3892 0.3878 1.0000
2017 0.0426 -0.0565 0.0582 0.0358 0.0161 0.0129 0.0352 0.0387 0.0288 0.0319 0.0405 0.0391 1.0000
2018 0.0235 0.1229 0.0838 0.1115 0.0506 0.0588 0.1405 0.3021 0.3035 0.3048 0.3027 0.3017 1.0000
2019 -0.0898 -0.0621 -0.0365 -0.0151 -0.0259 0.0345 -0.0353 0.3595 0.3561 0.3538 0.3554 0.3599 1.0000
2020 0.0267 0.1062 0.0783 0.0943 0.0663 -0.0394 0.0140 0.5252 0.5189 0.5224 0.5257 0.5252 1.0000
2021 -0.0747 -0.0416 -0.0602 -0.1115 -0.0496 -0.1307 -0.0737 0.2850 0.2754 0.2806 0.2833 0.2854 1.0000
2022 -0.0512 0.0293 0.0167 0.0275 0.0216 -0.0444 -0.0025 0.1496 0.1509 0.1492 0.1483 0.1497 1.0000
2023 0.0499 0.0573 0.0062 0.0155 0.0741 0.0283 0.0493 0.2752 0.2799 0.2789 0.2779 0.2748 1.0000
2024 -0.0012 0.0017 0.0170 -0.0009 0.0515 0.0102 0.0144 0.1219 0.1272 0.1261 0.1196 0.1218 1.0000
2025 -0.1068 0.0305 -0.1755 -0.0624 0.0287 -0.1505 -0.0576 0.3426 0.3353 0.3294 0.3340 0.3434 1.0000
Y. Hong and D. Klabjan, Preprint, June 25, 2026 26
