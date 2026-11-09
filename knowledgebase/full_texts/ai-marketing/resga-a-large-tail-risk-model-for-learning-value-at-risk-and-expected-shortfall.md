---
title: 'ReSGA: A Large Tail Risk Model for Learning Value-at-Risk and Expected Shortfall'
url: https://arxiv.org/abs/2606.04576
category: ai-marketing
subcategory: measurement
date: 2026-06
venue: ''
authors:
- Yichi Zhang
- Ke Zhu
- Zhoufan Zhu
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.04576
pages: 74
chars: 143728
fetched_at: '2026-11-08T13:27:56+00:00'
kb_version: 1
---

# ReSGA: A Large Tail Risk Model for Learning Value-at-Risk and Expected Shortfall

ReSGA: A Large Tail Risk Model for Learning
Value-at-Risk and Expected Shortfall
Yichi Zhang 1, Ke Zhu 1 and Zhoufan Zhu 2,3†
1Department of Statistics and Actuarial Science, The University of Hong Kong, Hong Kong
2Wang Yanan Institute for Studies in Economics, Xiamen University, China
3Department of Finance, School of Economics, Xiamen University, China
Learning Value-at-Risk (VaR) and Expected Shortfall (ES) is important for man-
aging financial risks effectively. Existing approaches with limited parameters are vul-
nerable to model misspecification in the era of big data. To address this limitation,
we propose a large tail risk model, the retrieval-enhanced self-grouping autoencoder
(ReSGA), which is designed with millions of parameters to exploit the rich cross-
sectional dependence and long-term temporal dynamics of assets using their charac-
teristics. Applied to monthly US equity returns from 1926 to 2023 with 153 firm char-
acteristics, ReSGA outperforms twelve econometric and machine learning competitors
in terms of out-of-sample loss and statistical backtesting. In addition, its forecast ad-
vantages can translate into significant economic gains from long-short decile portfolios
that are constructed by a new size-enhanced left-side momentum strategy. To clarify
the role of complexity, we further conduct a systematic scaling analysis and demon-
strate that improvements in joint VaR-ES forecasting are primarily driven by data
complexity rather than model complexity. Finally, our analyses of group-importance
and transfer-learning exhibit the interpretability and cross-market generalizability of
ReSGA.
∗A user-oriented companion website for this paper, including stock-level tail risk forecasts, documentation,
and links to the data and source code, is available athttps://tailrisk-resga.github.io.
†Correspondence to Zhoufan Zhu (Email: tylerzzf@xmu.edu.cn)
Keywords:AI for Finance, Expected Shortfall, Large Tail Risk Model, Value-at-Risk, Virtue of Complexity
1
arXiv:2606.04576v1  [stat.ML]  3 Jun 2026

2
1. Introduction.Value-at-Risk (VaR) and Expected Shortfall (ES) are central measures
of financial tail risk in both academic research and regulatory practice. Considering the loss
of a portfolio or investment, VaR characterizes only a quantile of the distribution of this
loss, while ES summarizes expected losses beyond that quantile and therefore captures the
severity of extreme downside outcomes. Moreover, ES is a coherent risk measure, satisfying
properties like subadditivity, monotonicity, positive homogeneity, and translation invariance
(Artzner et al., 1999). In contrast, VaR is generally not subadditive, implying that portfolio
risk measured by VaR may exceed the sum of individual risks. These advantages make ES more
consistent with the diversification principles of portfolio theory and capture the tail risk in a
more comprehensive manner, explaining its growing role in modern risk management (Basel
Committee on Banking Supervision, 2019) 1.
Although conceptually attractive, ES remains challenging to forecast in practice. A funda-
mental obstacle is that ES on its own is not elicitable, whereas VaR is (Gneiting, 2011). In
other words, there exists no loss function for which ES is the unique minimizer of expected loss.
This lack of direct elicitability partly explains why the development of ES forecasting methods
has lagged behind that of VaR. A major breakthrough is provided by Fissler and Ziegel (2016),
which introduce a class of consistent scoring rules, known as Fissler-Ziegel (FZ) loss functions,
to utilize the joint elicitability of VaR and ES. This breakthrough leads to a growing litera-
ture on joint VaR-ES forecasting. For example, Patton, Ziegel and Chen (2019) employ FZ
loss functions in semi-parametric settings based on the generalized autoregressive score (GAS)
model and the generalized autoregressive conditional heteroskedasticity (GARCH) model; Tay-
lor (2019) exploits the link between the asymmetric Laplace likelihood and the FZ loss for joint
VaR-ES estimation; Merlo, Petrella and Raponi (2021) further extend the Laplace-based ap-
proach to multivariate regression settings. Until now, most existing work on joint VaR-ES
forecasting remains confined to parametric or semi-parametric models. In such frameworks,
the number of parameters is kept modest to ensure interpretability, and each asset is often
1For more studies on VaR and ES, one can refer to Acerbi and Tasche (2002), Rockafellar and Uryasev (2002),
Acerbi and Szekely (2014), Du and Escanciano (2017), Li and Wang (2023), and Chronopoulos, Raftapostolos
and Kapetanios (2024).

3
modeled separately with its own set of parameters. While tractable, their performance de-
pends critically on correct model specification, where the true data-generating process for tail
risks may be far more complex than a GARCH or GAS model can capture.
Fortunately, the era of big data brings new opportunities for tail risk modeling. Risk fore-
casters now have access to decades of financial data, covering tens of thousands of assets,
along with hundreds of firm characteristics. This abundance of information naturally raises
a key question: Can we develop a large tail risk model, analogous to large language models
(e.g., ChatGPT, Gemini, and Claude) in natural language processing, that learns from rich
and diverse data to predict VaR and ES more accurately? In other words,instead of relying
on asset-specific (semi-)parametric models, could a single high-capacity universal model trained
on massive data serve as a general engine for joint VaR-ES forecasting?
To shed light on large tail risk models, we first develop a unified learning framework for
joint VaR-ES forecasting. This framework assumes a universal function indexed by unknown
parameters, mapping from predictors (e.g., firm characteristics) to two latent but unconstrained
risk scores. Then, it transforms these two risk scores into valid VaR and ES forecasts through
a fixed one-to-one mapping. This data-driven framework enables linear regression models,
machine learning methods, and deep learning architectures to be treated in the same manner,
with parameters estimated by minimizing the FZ loss.
Under this framework, we propose a new large tail risk model, theretrieval-enhanced self-
grouping autoencoder(ReSGA), designed to fully exploit complex financial information for
joint VaR-ES forecasting. ReSGA first learns latent group structures across assets, allowing
tail-risk information to be shared among assets with similar financial behavior. It then incor-
porates a retrieval mechanism that enables each asset to draw on relevant long-term historical
“experiences” from both its own past and other assets within the same group, thereby enriching
usable temporal information. By leveraging cross-sectional dependence and long-term tempo-
ral dynamics in a flexible data-driven manner, ReSGA exploits spatial-temporal information
more effectively than existing approaches.
Empirically, we study the monthly VaR and ES of United States (US) equity returns using
a comprehensive dataset provided by Jensen, Kelly and Pedersen (2023), covering more than

4
40,000 stocks from January 1926 to December 2023. Each stock-month observation is associated
with 153 firm characteristics that are widely used in the asset pricing literature. We evaluate
the out-of-sample VaR and ES forecasting performance of ReSGA and its 12 competing models
through the average loss. From this analysis, we find that ReSGA consistently attains the lowest
out-of-sample average loss across all stock universes considered. Besides the loss analysis, we
further assess the statistical performance of all models via several statistical hypothesis tests,
including the Diebold–Mariano (DM; Diebold and Mariano, 1995) test, the model confidence
set (MCS; Hansen, Lunde and Nason, 2011) test, the conditional coverage (CC; Christoffersen,
1998) test, and the auxiliary expected shortfall regression (AESR; Bayer and Dimitriadis, 2022)
test. The out-of-sample testing results also provide consistent evidence in favor of ReSGA.
Beyond statistical assessments, we are interested in whether the tail risk forecasts generated
by ReSGA can lead to economically meaningful gains. Following Atilgan et al. (2020), we con-
struct a left-side momentum strategy by sorting stocks into deciles based on the predicted VaR
or ES. The resulting VaR- and ES-sorted portfolios exhibit sharp nonlinearities concentrated
in the extreme deciles: Stocks with the highest predicted tail risk (i.e., the lowest VaR or ES)
deliver substantially lower returns and markedly worse downside risk, while a long-short strat-
egy that buys the lowest-risk decile and sells the highest-risk decile, yields economically sizable
Sharpe ratios. These patterns indicate that ReSGA’s tail risk forecasts capture cross-sectional
variation in downside risk, which is also priced in the cross-section. Building on this insight, we
propose a new size-enhanced left-side momentum signal that combines predicted ES with firm
size. This signal is motivated by the “too big to fail” phenomenon in the US market: Tail risk
in large firms is more likely to reflect compensated systematic risk, whereas similar tail risk in
small firms often stems from idiosyncratic fragility. Based on this signal, we propose long-short
portfolios for each considered model and find that all proposed non-econometric portfolios
exhibit significant alphas relative to the Fama–French five-factor model. Hence, it indicates
that our size-enhanced left-side momentum signal could broaden the mean-variance frontier.
More importantly, our portfolio performances confirm that ReSGA delivers the best economic
performance among all competing models, with the highest Sharpe ratio for the long-short
decile portfolio and a clear monotonic return pattern across deciles. All of the above findings

5
show that the forecasting advantage from ReSGA is not only statistically relevant but also
economically meaningful.
Taken together, our statistical and economic findings above highlight that models can deliver
better tail risk forecasts by exploiting richer information in the input. We view the informative-
ness of model input as one aspect of data complexity. This phenomenon connects to a broader
debate on the virtue of complexity. In artificial intelligence, a growing body of evidence shows
that the out-of-sample predictive performance of models often improves systematically with
increases in either data complexity (with respect toin-sample data availability) or model com-
plexity (with respect tomodel parameter size); see, for example, Kaplan et al. (2020). This
empirical regularity, known as the scaling law, underpins the success of large language models
in the last five years. In finance, there has been an increasing focus on the investigation of model
complexity, while the examination of data complexity remains very rare. Kelly, Malamud and
Zhou (2024) provide early theoretical and empirical support for the virtue of model complexity
in asset pricing, demonstrating that simple models with few parameters can severely under-
state return predictability relative to more complex alternatives. See more empirical evidence
for this view in Didisheim et al. (2024) and Kelly et al. (2025). However, at the same time,
other studies also question whether such gains from model complexity are economically mean-
ingful or robust in asset pricing applications (Berk, 2023; Nagel, 2025; Buncic, 2025; Cartea,
Jin and Shi, 2025). In terms of risk forecasting, evidence on the role of model complexity is
far more limited; Li and Tang (2025) show that machine learning models outperform linear
models in realized volatility forecasting by capturing nonlinear temporal dynamics. However,
to date, the role of model complexity and data complexity in tail risk forecasting remains
largely unexplored.
To fill the gap, we further investigate the scaling performance of ReSGA and its competitors
by varying model parameter size or in-sample data size to assess the role of model complexity
or data complexity, respectively. First, our experiment results show that, holding the in-sample
data fixed, simply increasing parameter size alone does not yield consistent performance im-
provements: Larger models do not reliably outperform smaller ones, and the best results in
terms of out-of-sample average loss and portfolio Sharpe ratio typically occur at intermedi-

6
ate scales (around or below the in-sample sample size). In particular, models that exploit
spatial–temporal inputs, such as ReSGA, benefit more from additional parameters and consis-
tently outperform simpler architectures once sufficient parameters are available. Second, our
complementary experiments vary the available in-sample data size while keeping the model
architectures fixed. The corresponding results demonstrate that, in terms of out-of-sample
average loss and portfolio Sharpe ratio, the performance of each model exhibits a clear im-
provement trend with the size of the in-sample data used. Together, the aforementioned scaling
results indicate that our out-of-sample performance gains are primarily driven by richer data
rather than by parameter growth alone. Hence, they provide limited support for a general
virtue of model complexity, instead emphasizing the central role of data complexity in tail risk
forecasting.
Lastly, we illustrate the usefulness of ReSGA through a group-importance analysis and
a transfer-learning analysis. In the group-importance analysis, we explore economic model
interpretability by investigating which types of firm characteristics drive tail risk predictability
in the ReSGA model. It turns out that the predictive power for VaR and ES is concentrated
in a small set of economic themes (or groups): Value, Low Risk, Momentum, Quality, and
Short-Term Reversal. Additionally, the importance of these groups varies systematically across
firm size and over time, reflecting shifts in the underlying economic sources of tail risk. In the
transfer-learning analysis, we deploy the ReSGA model trained only on US equity data, without
any re-estimation or fine-tuning, to five major international equity markets: China, Japan, the
United Kingdom (UK), Australia and Canada. Despite substantial cross-market heterogeneity,
ReSGA consistently presents reliable out-of-sample VaR-ES forecasting performance in every
market, indicating that its predictive advantage is not US-specific and remains robust under
market shifts. Hence, ReSGA, as a universal large tail risk model, has great generalizability in
learning VaR and ES. At the portfolio level, however, return patterns differ substantially across
countries. In China and Japan, higher size-enhanced left-side momentum is associated with
higher returns, while in the UK, Australia, and Canada, large return dispersion concentrates
in the extreme deciles. These findings suggest that tail-risk pricing varies across markets, likely
reflecting differences in market structure, investor behavior, and risk premia.

7
The remaining paper proceeds as follows. Section 2 introduces a unified VaR-ES learning
framework and the ReSGA model. Section 3 presents the empirical results for the US equity
market, while Section 4 examines the transferability of the ReSGA model trained on US data
to other markets. Section 5 concludes. Technical details are provided in Appendix A and other
appendices in the supplementary materials.
2. Methodology.Letr i,t denote the return of assetiat timet, wheret= 1, . . . , Tand
i= 1, . . . , Nt, withN t representing the number of available assets at timet. The variables of
interest in this paper are the conditionalτ-th VaR and ES ofr i,t, defined respectively as
VaRi,t =F −1 i,t (τ) and ES i,t =E(r i,t |r i,t ≤VaR i,t,F t−1),
whereτ∈(0,1) is the quantile level,F i,t(·) is the conditional distribution ofr i,t givenF t−1,
andF t−1 is the information set containing all available information up to timet−1.
In the following subsections, Section 2.1 introduces a unified learning framework for VaR i,t
and ESi,t. Section 2.2 presents our new ReSGA model. Section 2.3 describes a set of represen-
tative benchmark tail risk models that are used for comparison in our empirical study.
2.1.A Unified Learning Framework.Following the seminal work of Koenker and Bassett
(1978), a common way to learn VaR is based on the check loss function. However, as shown in
Gneiting (2011), ES alone is not elicitable, meaning that it cannot be the unique minimizer of
an expected loss function. Fissler and Ziegel (2016) solve this issue by showing that VaR and
ES are jointly elicitable: (VaR,ES) is the unique minimizer of the general FZ loss function.
Specifically, to jointly learn the VaR and ES of a univariate random variableY, Fissler and
Ziegel (2016) define the general FZ loss function (also termed as the scoring rule) as follows:
ℓ(Y,(v, e)) =

1{Y≤v} −τ

g1(v)−1{Y≤v}g 1(Y)
+g 2(e)

e−v+ 1 τ 1{Y≤v}(v−Y)  −˜g2(e), (1)
whereτ∈(0,1) is the quantile level,1{·}is the indicator function, andg 1, g2 :R→Rare
two pre-determined functions, withg 2 being strictly increasing and convex, and ˜g 2 being its

8
primitive. In particular, wheng 1(x) = 0 andg 2(x) =−1/x, the general FZ loss function in (1)
becomes the commonly used degree-0 FZ loss function:
ℓFZ0(Y,(v, e)) =− 1 τ e1{Y≤v}(v−Y) + v e + log(−e)−1,(2)
where (v, e)∈Γ for an admissible region Γ ={(v, e) :e < v <0}. Using the degree-0 FZ loss
function, a joint learning of VaR and ES can be achieved by noting
(VaR ofY,ES ofY) = argmin
(v,e)∈Γ
E[ℓ FZ0(Y,(v, e))].(3)
As shown in (3), the learning of VaR i,t and ESi,t underℓ FZ0 needs to meet a key admissible
condition: ESi,t <VaR i,t <0. To achieve this goal, we propose a new unified learning framework
for VaRi,t and ES i,t. Specifically, lety i,t = (y i,t,1, yi,t,2)′ ∈R 2 represent a vector of two latent
risk scoresy i,t,1 andy i,t,2. Then, we define a Softplus-based one-to-one mappingp:y i,t →
(VaRi,t,ES i,t), satisfying
VaRi,t =−Softplus(y i,t,1),
ESi,t =−

Softplus(yi,t,1) + Softplus(yi,t,2)

,
(4)
where Softplus(·) is a function (Dugas et al., 2000) defined as
Softplus(x) = log(1 +e x)∈R +,forx∈R.
Since both Softplus(yi,t,1) and Softplus(yi,t,2) are strictly positive, the mapping in (4) guarantees
that ES i,t <VaR i,t <0, regardless of the values ofy i,t,1 andy i,t,2. Consequently, we are able
to learn VaRi,t and ESi,t through a model fory i,t, the form of which can be specified without
imposing restrictions ony i,t,1 andy i,t,2.
Following the above idea, our learning framework only needs to specify a model fory i,t
indexed by unknown parametersθ. Therefore, unless otherwise stated, all tail risk models in
this paper are designed fory i,t. By writingy i,t ≡y i,t(θ), we have (VaR i,t,ES i,t) =p(y i,t(θ))
according to (4), so we can make use of result (3) to estimateθby minimizing the empirical
degree-0 FZ loss:
bθ= argmin
θ
TX
t=1
NtX
i=1
ℓFZ0

ri,t,

VaRi,t,ES i,t

= argmin
θ
TX
t=1
NtX
i=1
ℓFZ0

ri,t, p(yi,t(θ))

.(5)

9
In practice, due to the massive data volume, we use the adaptive moment estimation (Adam)
algorithm in Kingma and Ba (2015) to solve optimization problem (5). Given bθ, VaRi,t and
ESi,t are then learned by dVaRi,t and cESi,t, respectively, where ( dVaRi,t, cESi,t) =p(y i,t( bθ)).
2.2.The ReSGA Model.LetY t ∈R Nt×2 denote the matrix of cross-sectional risk scores at
timet, where itsi-th row isy ′ i,t. Under the learning framework in Section 2.1, we design a new
ReSGA model forY t, which aims to capture the nonlinear relationships between asset charac-
teristics and risk scores, while simultaneously accounting for spatial and temporal dependencies
of assets. To facilitate the construction of ReSGA, we letX i,t−1 ∈R S×P be the feature matrix
of assetiup to timet−1, with itss-th rowx ′ i,t−1−S+s, wherex i,t = (x i,t,1, . . . , xi,t,P )′ ∈R P
containsPcharacteristics of this asset at timet. Here,Pis the number of characteristics and
Sis the number of time lags. Collecting all individual feature matrices, we obtain the tensor
of asset characteristicsX t−1 = [X1,t−1, . . . ,XNt,t−1]∈R Nt×S×P .
UsingX t−1 as the input, ReSGA, parameterized byθ= (ϕ ′,ψ ′)′, learnsY t through three
core modules,encoder,retriever, anddecoder, which are defined as follows:
(Ht,M t) = Encoder(Xt−1;ϕ),
Zt = Retriever(Ht;M t),
Yt = Decoder (Ht,Z t;M t,ψ),
(6)
where Encoder(·;ϕ), Retriever(·;M t), and Decoder(·,·;M t,ψ) denote the functional forms of
encoder, retriever, and decoder, respectively (see their detailed architectures in Sections A.1–
A.3). Generally speaking,
•Encoder(·;ϕ), parameterized byϕ, extracts a temporal featureH t ∈R Nt×S×D for all
assets across lags in an autoregressive manner, along with a setM t that captures latent
group structures among assets according to their similarities in characteristics, where the
dimensionDserves as a user-specific hyperparameter controlling model complexity;
•Retriever(·;M t) leverages the learned group structureM t to retrieve long-term historical
information not only from each asset’s own temporal history but also from other assets
within the same group, yielding the retrieval featureZ t ∈R Nt×D;

10
•Decoder(·,·;M t,ψ), parameterized byψ, hierarchically aggregates the group-, retrieval-,
and asset-level information to generate the risk scoreY t.
It is worth noting thatM t depends on the specific choice ofX t−1 and loss function. In this
study, under the degree-0 FZ loss in (5),M t reveals the dynamic topological relationships
among assets for tail risk analysis, guided by the similarities in asset characteristics. When
ReSGA is applied to other studies, different inputs and loss functions can lead to different
interpretations forM t.
2.3.Competing Models.To assess the performance of ReSGA, we consider its 12 com-
peting models. These competitors are classified into four categories:Point-wise,Temporal,
Spatial–temporalandEconometricmodels, depending on whether they exploit temporal or
cross-sectional information and whether they employ firm characteristics. Models in the first
three categories are based on our learning framework in Section 2.1, while models in the last
category learn VaR and ES using existing econometric approaches. For more details about
these 12 competing models, one can refer to Appendix B in the supplementary materials.
Point-wise Models.The point-wise models aim to capture the relationship between asset
characteristics and tail risks, but ignore both temporal and cross-sectional dependencies. They
directly map the most recent asset characteristics to risk scores as follows:
yi,t =f(x i,t−1;θ),(7)
wherex i,t−1 ∈R P is the vector ofPcharacteristics for assetiat timet−1, andf(·;θ) is a
parametric function indexed byθ. Particularly, we focus on two models in (7): (i) the classical
linear regression model, labeled as “Linear”; (ii) a three-hidden-layer neural network model
proposed by Gu, Kelly and Xiu (2020), labeled as “NN”.
Temporal Models.Unlike point-wise models, the temporal models explicitly account for the
dynamic evolution of asset characteristics over time by assuming
yi,t =g(X i,t−1;θ),(8)

11
whereX i,t−1 ∈R S×P is the feature matrix of assetiat timet−1, andg(·;θ) is a parametric
function indexed byθ. Note that the hyperparameterSspecifies the look-back time period of
characteristics. WhenS= 1,X ′ i,t−1 reduces tox i,t−1, which is the vector of the most recent
characteristics (i.e., the input to point-wise models in (7)). Compared with point-wise models,
the temporal models in (8) exploit not only the predictive power of the latest characteristics,
but also the historical evolution of characteristics, allowing them to capture dynamic patterns
that may enhance predictive performance.
The temporal models require specific designs to effectively capture temporal dynamics. In
this paper, we employ several representative temporal deep learning models in (8), including:
(i) two extended models: a lag-augmented neural network model that flattensX i,t−1 into a
vector as input (labeled as “LANN”), and a decomposition-based neural network model
proposed by Zeng et al. (2023) that separately builds trend and seasonal components
(labeled as “DLinear”);
(ii) two recurrent neural network models: long short-term memory network model from
Hochreiter and Schmidhuber (1997) (labeled as “LSTM”) and gated recurrent unit net-
work model from Chung et al. (2014) (labeled as “GRU”);
(iii) three transformer-type neural network models: the “Informer” model proposed by Zhou
et al. (2021), which leverages an attention-based encoder and decoder to capture tem-
poral dependencies, along with its encoder-only and decoder-only variants (labeled as
“EInformer” and “DInformer”, respectively).
Spatial-temporal Models.For the spatial-temporal models, they simultaneously capture both
the temporal evolution of asset characteristics and the cross-sectional interactions among assets
using advanced deep learning architectures. Specifically, they are defined as
Yt =m(X t−1;θ),(9)
whereX t−1 ∈R Nt×S×P is the tensor of asset characteristics, andm(·;θ) is a parametric func-
tion indexed byθ. Compared to the temporal models, which handle assets separately, the
spatial–temporal models allow each asset’s risk scores to depend not only on its own historical
information but also on that of other assets. By explicitly modeling these inter-asset dependen-

12
cies, the spatial–temporal models are capable of capturing common shocks, contagion effects,
and network spillovers, which are particularly relevant in financial markets. This spatial infor-
mation sharing is expected to lead to improved robustness and predictive accuracy, especially
during periods of heightened market co-movement or systemic stress.
Given the rich information contained inX t−1, the spatial–temporal models must be care-
fully designed to efficiently exploit both temporal and cross-sectional dependencies. Besides the
proposed ReSGA model, we consider another spatial–temporal model in (9): the self-grouping
autoencoder model from Zhu and Zhu (2025) (labeled as “SGA”). In short, the SGA model can
be viewed as a simplified version of ReSGA. Both models share a common encoder–decoder
architecture that learns time-varying group structures across assets. However, SGA removes
all retrieval-related components and focuses solely on contemporaneous spatial dependencies.
As a result, it could perform well when the temporal lengthSis relatively short. In contrast,
ReSGA extends this framework by incorporating a retrieval mechanism to capture long-term
spatial–temporal interactions, making it suitable for longer sequences and more complex sys-
temic risk patterns.
Econometric Models.In the econometrics literature, Patton, Ziegel and Chen (2019) apply
two widely used semi-parametric models, GAS and GARCH, to study the dynamics of VaR
and ES. These models do not rely on machine learning or deep learning techniques to utilize
the information of asset characteristics, yet they need to impose the constraint of ES i,t <
VaRi,t <0 when implementing optimization in model estimation. Including them allows us to
assess whether more complex models deliver meaningful improvements over well-established
econometric approaches. Notably, unlike the aforementioned non-econometric models, which
employ a unified learning framework with a single parameter set shared across assets, the GAS
and GARCH models are estimated separately for each asset to learn VaR and ES directly.
Table 1 summarizes the features of all considered tail risk models, such as nonlinearity from
deep learning, temporal dynamics from lagged characteristics, and spatial information sharing
within cross-sectional input. In addition, it also distinguishes models by whether they support
long-history inputs (i.e., capturing long memory effect). By clarifying the incremental modeling

13
capabilities across point-wise, temporal, spatial–temporal, and econometric models, this table
clearly illustrates how ReSGA integrates all these features within a single model to exploit
available information efficiently.
Table 1
Summary of model features.
Model Universal Nonlinear Temporal Spatial Long Memory
Linear✓– – – –
NN✓ ✓– – –
LANN✓ ✓ ✓–✓
DLinear✓ ✓ ✓–✓
LSTM✓ ✓ ✓– –
GRU✓ ✓ ✓– –
Informer✓ ✓ ✓–✓
EInformer✓ ✓ ✓–✓
DInformer✓ ✓ ✓–✓
SGA✓ ✓ ✓ ✓–
ReSGA✓ ✓ ✓ ✓ ✓
GARCH – –✓– –
GAS – –✓– –
Notes.“Universal” indicates that the model is applied to all assets. “Nonlinear” showcases that the model
is nonlinear. “Temporal” means that the model processes sequential information from multiple time lags.
“Spatial” signifies that the model makes use of information shared across assets. “Long Memory” expresses
that the model is able to utilize long-term historical information.
3. Empirical Study of US Equity.
3.1.Data.This section analyzes a comprehensive US equity dataset compiled by Jensen,
Kelly and Pedersen (2023). This dataset covers more than 40,000 stocks, providing a broad and
representative cross-section of the US equity market for large-scale risk forecasting. Meanwhile,
it spans the period from January 1926 to December 2023 at a monthly frequency, offering nearly
a century of observations across different market regimes, including economic expansions and

14
major crisis episodes. In this dataset, each stock in every month is associated with 153 firm
characteristics2. As in Gu, Kelly and Xiu (2020), we rank-normalize all characteristics cross-
sectionally to mitigate the impact of outliers, and then impute missing characteristic values
using contemporaneous cross-sectional medians. After this preprocessing treatment, we letr i,t
denote the excess return of stockiin montht, and construct the characteristics tensorX t−1
from all 153 characteristics.
Throughout the analysis, we apply the ReSGA model to learn VaRi,t and ESi,t at the quantile
levelτ= 0.05, with a comparison to the 12 competing models outlined in Section 2.3. To
evaluate out-of-sample forecasting performance for all models, we follow Gu, Kelly and Xiu
(2020) to adopt an expanding-window process, with the last ten years of the sample (2014–
2023) reserved for out-of-sample evaluation. Specifically, each model is trained on data from
1926 to 1995, validated on data from 1996 to 2013, and tested on data from 2014; this process
then shifts forward by one year (trained on 1926–1996, validated on 1997–2014, and tested
on 2015), and it is repeated until reaching the end of the out-of-sample period 3. For the
detailed implementation of the above training, validation, and testing process, one can refer
to Section D.
3.2.Statistical Performance Evaluation.We first evaluate the out-of-sample forecasting
performance of ReSGA and its 12 competitors from a statistical perspective. As in Patton,
Ziegel and Chen (2019), we consider the following out-of-sample average loss as a natural
assessment criterion:
ℓoos = 1P
t∈oos |St|
X
t∈oos
X
i∈St
ℓFZ0

ri,t,

dVaRi,t, cESi,t

,(10)
where “oos” denotes the out-of-sample period,S t denotes a group of stocks at timet, with|S t|
being its cardinality,ℓ FZ0 is the degree-0 FZ loss function defined in (2), and dVaRi,t and cESi,t
are forecasts of VaR i,t and ESi,t from each learned model.
2Seehttps://jkpfactors.s3.amazonaws.com/documents/Documentation.pdffor more details.
3As an exception, two econometric models, GAS and GARCH, have no need for validation, so they are
estimated using all training and validation data.

15
Table 2
Out-of-sample average lossℓ oos across different models and stock groups.
All Mega Large Small Micro Nano
Point-wise models
Linear 3.3442 2.8431 3.0908 3.3305 3.4642 3.7616
NN 3.3322 2.8770 3.0958 3.3055 3.4380 3.7561
Temporal models
LANN 3.3440 2.8797 3.0944 3.3055 3.4679 3.8151
DLinear 3.3166 2.8385 3.0703 3.2919 3.4508 3.7404
LSTM 3.3063 2.8368 3.0670 3.2838 3.4368 3.7184
GRU 3.3022 2.8326 3.0601 3.2807 3.4357 3.7082
Informer 3.2985 2.8217 3.0532 3.2779 3.4334 3.7098
EInformer 3.3276 2.8387 3.0732 3.3148 3.4648 3.7395
DInformer 3.3134 2.8258 3.0578 3.2925 3.4535 3.7346
Spatial-temporal models
SGA 3.2868 2.8215 3.0527 3.2647 3.4118 3.7017
ReSGA 3.2793 3.27933.2793 2.8081 2.80812.8081 3.0417 3.04173.0417 3.2635 3.26353.2635 3.4036 3.40363.4036 3.6932 3.69323.6932
Econometric models
GAS 4.3461 3.0214 3.1899 3.7713 5.5837 5.0057
GARCH 4.7122 2.9189 3.2377 3.8226 6.6247 5.0849
Notes.This table reports out-of-sample average lossℓ oos for six stock groups, withS t formed by all
stocks and five size-based subgroups (mega, large, small, micro, and nano) of stocks. These subgroups
are defined by the percentiles of firms’ market capitalization among all stocks at the end of each month:
Mega stocks are above the 80th percentile, large stocks are between the 50th and 80th percentiles, small
stocks are between the 20th and 50th percentiles, micro stocks are between the 1st and 20th percentiles,
and nano stocks fall below the 1st percentile. The lowest value for each column is highlighted in boldface.
Table 2 reports the results ofℓ oos across models and different stock groups. From this table,
we can draw the following interesting findings:

16
•ReSGA achieves the lowest loss across the full stock group, as well as within five size-
based stock groups: mega, large, small, micro, and nano. This consistent dominance in-
dicates that ReSGA provides a broadly effective engine for VaR and ES forecasting, with
its combination of learned cross-sectional group structure and retrieval-based temporal
augmentation.
•Two spatial-temporal models tend to outperform seven temporal models, which in turn
generally outperform two point-wise models. A notable exception is LANN, which per-
forms worse than NN in most cases despite having richer inputs. By flattening theS×P
characteristics matrix into a single vector, LANN discards temporal ordering and there-
fore fails to model sequential dependence directly. As a result, it fails to capture dynamic
patterns such as persistence or volatility clustering, illustrating that exploiting tempo-
ral information requires appropriate model architecture. Nevertheless, the overall ranking
among all eleven universal models provides strong empirical support for the virtue of data
complexity: Improvements from point-wise to temporal models reflect the value of in-
corporating temporal information, while further gains from temporal to spatial-temporal
models highlight the importance of cross-sectional information.
•All eleven universal models substantially outperform two econometric models: GAS and
GARCH. A natural explanation is that GAS and GARCH are primarily designed to
capture return dynamics and largely overlook rich firm-level information, which is crucial
for VaR and ES forecasting. Note that GAS and GARCH are estimated separately for
each asset, whereas all universal models are trained on the pooled samples across assets.
Hence, the above advantage of universal models over econometric models also points to
a clear data scaling effect, highlighting the advantage of larger effective sample sizes and
richer information content.
•Within the universal model family, moving beyond linear specifications yields clear gains,
since nonlinear models (e.g., NN, LSTM, SGA, and ReSGA) deliver lower losses than
the linear model in most cases. This finding suggests that nonlinearities and interaction
effects among firm characteristics play an important role in tail risk forecasting.
•In terms of size-based stock groups, a clear monotonic pattern emerges: Larger firms

17
systematically exhibit lower losses. This pattern is expected, as larger firms have greater
liquidity, more standard published financial statements, and more stable trading envi-
ronments, all of which contribute to their better predictability of tail risk.
In addition to the out-of-sample average loss, we further evaluate the out-of-sample perfor-
mance of all models using four statistical hypothesis tests: the DM in Diebold and Mariano
(1995), MCS in Hansen, Lunde and Nason (2011), CC in Christoffersen (1998), and AESR in
Bayer and Dimitriadis (2022). See their detailed descriptions in Section E of the supplementary
materials. In terms of the values ofℓ oos withS t being the full stock group, the DM test aims
to compare the prediction performance of any two models, and the MCS test searches for a
batch of models that perform significantly better than the others. The CC and AESR tests
provide statistical evidence of the validity of VaR and ES forecasts, respectively. Notably, we
do not adopt the e-backtesting approach of Wang, Wang and Ziegel (2025) to examine the
validity of ES forecasts, since that framework is mainly designed for sequential monitoring and
non-fixed-sample sizes, whereas our empirical exercise is based on fixed-sample out-of-sample
evaluation.
Table 3 reports the pairwise DM test statistics for all considered models. From this table,
we have two clear findings. First, except for SGA, ReSGA dominates all other models with
significantly lower values ofℓ oos. Second, all universal models deliver statistically significant
improvements over econometric models.
Next, starting from the full set of models, our MCS test iteratively eliminates inferior models
at the 90% confidence level, until only those statistically indistinguishable models remain to
form the final model set. It turns out that only SGA and ReSGA are retained in the final
model set. This outcome indicates that no other forecasting models perform as well as SGA
and ReSGA in a statistical sense, underscoring the importance of spatial-temporal modeling
for tail risk forecasting.
Moreover, we apply the CC and AESR tests to check the validity of VaR and ES forecasts
for each stock at the significance levelα∈ {0.01,0.05,0.10}, respectively, and then denote the
proportion of stocks having valid VaR and ES forecasts as the pass rate. Table 4 reports pass
rates with respect to VaR and ES forecasts across all models. From this table, we find that,

18
except for ES at the levelα= 0.01, the two spatial-temporal models, SGA and ReSGA have
the largest values of pass rates. In particular, ReSGA shows a substantially larger pass rate
than SGA for the prediction of ES at the levelα= 0.05 or 0.10.
Overall, the above statistical performance evaluations consistently demonstrate the state-
of-the-art performance of ReSGA in tail risk forecasting, which in turn implies the virtue of
data complexity.
3.3.Economic Performance Evaluation.To explore the economic implications of the VaR
and ES, it is important to evaluate all tail risk models from an economic perspective. Following
Atilgan et al. (2020), we first assess economic gains using decile portfolios sorted on the pre-
dicted VaR or ES. This trading strategy is referred to as “left-side momentum”. It guides us to
monthly rebalance ten decile portfolios (P1–P10), after sorting all stocks in descending order
according to their predicted VaR or ES at the end of each month. Note that our predicted
VaR and ES are negative in this paper, so P1 corresponds to the lowest-risk portfolio and P10
represents the highest-risk portfolio.
To keep the presentation concise, Table 5 reports portfolio results only for ReSGA, as the
performance for other models is qualitatively similar. As shown in this table, under VaR-based
sorting, average portfolio returns remain relatively stable up to P8 (1.090%), but drop sharply
to 0.619% in P9 and turn negative in P10 (−0.284%), while the Sharpe ratio falls to−0.085 in
P10. This decline in returns is accompanied by a marked increase in downside risk: Maximum
drawdown worsens from 0.499 in P8 to 0.730 in P9 and 0.807 in P10. A similar pattern appears
under ES-based sorting, with average returns decreasing from 1.196% in P8 to 0.512% in P9
and−0.024% in P10, and maximum drawdown deepening to 0.710 in P9 and 0.810 in P10.
The above findings indicate P9 and P10, which include stocks with high predicted tail risk,
exhibit a substantially worse performance in terms of return, Sharpe ratio, and drawdown.
Atilgan et al. (2020) attribute this pattern to behavioral underreaction to bad news and the
persistence of left-tail risks, which concentrate losses in the most risk-exposed portfolios. Our
findings mirror this stylized fact under both VaR- and ES-based sorting, supporting the view
that tail-risk forecasts from the ReSGA can capture economically meaningful variation in
downside risk across the cross-section.

19
Table 3: Pairwise DM test statistics.
GAS GARCH Linear NN LANN DLinear LSTM GRU Informer EInformer DInformer SGA ReSGA
GAS –
GARCH 1.04 –
Linear -3.35 ∗∗∗ -2.39∗∗ –
NN -3.39 ∗∗∗ -2.41∗∗ -0.85 –
LANN -3.30 ∗∗∗ -2.34∗∗ 1.02 8.37 ∗∗∗ –
DLinear -3.42 ∗∗∗ -2.39∗∗ -1.73∗ -0.11 -2.86 ∗∗∗ –
LSTM -3.43 ∗∗∗ -2.40∗∗ -2.21∗∗ -1.32 -5.24 ∗∗∗ -2.11∗∗ –
GRU -3.45 ∗∗∗ -2.41∗∗ -2.46∗∗ -1.80∗ -5.65∗∗∗ -2.89∗∗∗ -2.23∗∗ –
Informer -3.44 ∗∗∗ -2.41∗∗ -3.80∗∗∗ -1.62 -4.46 ∗∗∗ -3.13∗∗∗ -1.31 -0.56 –
EInformer -3.36 ∗∗∗ -2.37∗∗ -0.23 0.42 -0.81 0.76 1.22 1.45 2.27 ∗∗ –
DInformer -3.41 ∗∗∗ -2.39∗∗ -2.66∗∗∗ -0.21 -1.83 ∗ -0.32 0.58 0.91 1.62 -1.39 –
SGA -3.51 ∗∗∗ -2.43∗∗ -4.62∗∗∗ -3.56∗∗∗ -8.01∗∗∗ -4.40∗∗∗ -3.05∗∗∗ -2.17∗∗ -1.40 -2.25 ∗∗ -2.13∗∗ –
ReSGA -3.51 ∗∗∗ -2.44∗∗ -4.69∗∗∗ -4.49∗∗∗ -7.63∗∗∗ -4.82∗∗∗ -4.13∗∗∗ -3.26∗∗∗ -2.33∗∗ -2.60∗∗∗ -2.51∗∗ -1.12 –
Notes.A lower-triangular matrix that reports the pairwise DM test statistic. Each entry shows the value of DM statistic by
comparing the model in the row against the one in the column. Its negative (positive) value indicates that the row model yields
lower (higher) loss, where the symbols∗ ∗ ∗,∗∗, and∗denote the rejection of the null hypothesis of equal prediction performance
at the 1%, 5%, and 10% levels, respectively.

20
Table 4
Pass rates of stocks with valid VaR (or ES) predictions across different models.
VaR ES
0.01 0.05 0.10 0.01 0.05 0.10
Point-wise Models
Linear 95.14 87.52 82.02 78.90 70.13 64.73
NN 95.92 88.65 83.47 67.92 60.04 54.75
Temporal Models
LANN 95.08 87.17 82.26 56.14 49.59 44.89
DLinear 96.41 89.95 84.88 85.28 78.07 73.18
LSTM 97.28 91.54 86.53 83.65 76.82 71.90
GRU 97.39 91.85 86.96 83.93 77.66 72.56
Informer 97.04 90.89 86.04 87.12 81.02 76.91
EInformer 96.23 89.43 84.24 88.75 82.27 77.13
DInformer 96.20 89.70 84.72 86.81 80.42 76.41
Spatial-temporal Models
SGA 98.07 98.0798.07 92.82 88.27 87.63 80.48 75.56
ReSGA 97.86 92.84 92.8492.84 88.33 88.3388.33 88.63 82.86 82.8682.86 79.17 79.1779.17
Econometric Models
GAS 93.59 87.71 82.76 88.84 88.8488.84 82.81 78.03
GARCH 92.42 84.43 79.77 79.72 71.99 66.86
Notes.Pass rate is the proportion of stocks that have valid VaR (or ES) predictions, assessed using the CC (or
AESR) test at the significance levelα∈ {0.01,0.05,0.10}. For each column, the largest pass rate is highlighted
in boldface.
Beyond the above left-side momentum, we further design a new size-enhanced left-side mo-
mentum strategy, which utilizes the trading signal motivated by the “too big to fail” phe-
nomenon in the US stock market. Our key trading idea is to exploit the different economic

21
Table 5
Out-of-sample performances of decile portfolios using the signal of VaR or ES.
Signal Metric P1 P2 P3 P4 P5 P6 P7 P8 P9 P10 H–L
VaR
Avg 0.947 0.956 0.991 0.829 0.961 1.324 1.013 1.090 0.619 -0.284 1.231
MDD 0.199 0.209 0.253 0.292 0.260 0.321 0.582 0.499 0.730 0.807 0.681
SR 0.909 0.788 0.708 0.570 0.585 0.724 0.431 0.431 0.217 -0.085 0.412
ES
Avg 0.900 1.001 0.940 0.813 1.031 1.297 0.895 1.196 0.512 -0.024 0.924
MDD 0.207 0.201 0.235 0.303 0.268 0.400 0.561 0.515 0.710 0.810 0.769
SR 0.826 0.818 0.697 0.515 0.663 0.694 0.389 0.487 0.185 -0.007 0.298
Notes.This table reports the performance of value-weighted decile portfolios constructed by predicted VaR
and ES from the ReSGA model as sorting signal. At each month, stocks are sorted in descending order of the
corresponding risk signal and assigned to ten portfolios (P1–P10). Portfolio P1 (High) contains stocks with
the lowest tail risk, while P10 (Low) contains those with the highest tail risk. All portfolios are value-weighted
using market equity and rebalanced monthly. Avg denotes the average portfolio return in percentage, MDD
denotes the maximum drawdown, and SR denotes the annualized Sharpe ratio. H–L (i.e., High–Low) is a
long-short portfolio that buys P1 and sells P10.
implications of tail risk across firms of different sizes. Specifically, we assign strong buying
signal to large-cap stocks with small values of ES, reflecting that downside risk in large firms
often attracts market attention, policy support, or investor demand, and it thus can limit
extreme losses and help preserve long-term value. In contrast, we assign strong selling signal
to small-cap stocks with significantly negative ES, which often reflects idiosyncratic fragility,
limited liquidity, or elevated default risk, rather than priced systematic risk.
Motivated by this idea, we construct the following trading signal:
αi,t =

Capi,t−1 − Capt−1

×

1−exp( cESi,t)  ,(11)
where Cap i,t−1 denotes the log market capitalization of assetiat timet−1, and Capt−1 is
the corresponding cross-sectional mean. Here, the term [1−exp( cESi,t)] lies between 0 and 1,
with its value decreasing as cESi,t increases, serving as a proxy for tail-loss severity; the term
(Capi,t−1 − Capt−1) tends to be positive for large-cap stocks and negative for small-cap stocks,
acting as a classifier for firm size. Combining these two terms, the signalα i,t in (11) assigns

22
high values to large-cap stocks with severe predicted tail risk, and low values to small-cap
stocks with similar tail risk.
To assess the economic performance of our size-enhanced left-side momentum strategy, we
adopt the signalα i,t to propose monthly rebalanced decile portfolios as before, with cESi,t
computed from different models. Moreover, we regress the monthly returns of the resulting
H–L portfolios on the Fama–French five factors (Fama and French, 2015) to examine whether
there is an abnormal return (alpha) unexplained by standard factors. Table 6 reports the
results of this analysis, and it delivers the following findings:
•The ReSGA-based strategy delivers the highest value of monthly average return, annual-
ized Sharpe ratio and alpha for the H–L portfolio, outperforming all competing strategies.
This result indicates that the best ES forecasting accuracy from ReSGA can translate
into the strongest economic gains when combined with firm size information.
•Regardless of the choice of models, decile portfolios exhibit a clear and robust monotonic
pattern: Moving from P1 to P10, average portfolio returns and annualized Sharpe ratios
decline steadily and become strongly negative in the lowest deciles (P9 and P10). This
pattern confirms that the signalα i,t can effectively rank stocks that have economically
meaningful size-enhanced tail risk exposure.
•For all strategies based on the universal models, thep-values of the estimated alphas
are below 0.05, whereas the correspondingp-values for the GAS- and GARCH-based
strategies are 0.051 and 0.128, respectively. This contrast indicates that the economet-
ric models exhibit relatively weak predictive power, highlighting the advantage of our
proposed unified learning framework.
Taken together, Tables 5 and 6 show that the superior advantage of ReSGA in learning tail
risks can translate into economically meaningful gains.
3.4.Scaling Performance Evaluation.To examine whether there is virtue of model com-
plexity in learning VaR and ES, we begin by evaluating scaling performance with respect to
parameter size for all considered machine-learning-based models (i.e., all universal models ex-
cluding Linear). Specifically, we adopt a within-architecture scaling strategy: For each model,

23
Table 6
Out-of-sample performance of decile portfolios using the signal ofα i,t across different models.
Metric P1 P2 P3 P4 P5 P6 P7 P8 P9 P10 H–L Alpha
Point-wise Models
Linear Avg 0.931 0.804 0.761 0.830 0.534 0.587 0.469 0.461 -0.193 -0.887 1.818 1.477 SR 0.732 0.597 0.500 0.510 0.306 0.328 0.264 0.217 -0.076 -0.274 0.673 (0.030)
NN Avg 0.926 0.764 0.741 0.820 0.535 0.538 0.651 0.314 -0.223 -0.901 1.827 1.510 SR 0.720 0.582 0.491 0.494 0.307 0.307 0.357 0.148 -0.087 -0.272 0.659 (0.035)
Temporal Models
LANN Avg 0.934 0.809 0.825 0.821 0.657 0.646 0.575 0.427 -0.174 -1.039 1.973 1.625 SR 0.731 0.612 0.551 0.500 0.380 0.356 0.307 0.196 -0.066 -0.317 0.723 (0.019)
DLinear Avg 0.928 0.767 0.785 0.827 0.646 0.643 0.591 0.503 -0.234 -0.947 1.876 1.516 SR 0.725 0.590 0.527 0.513 0.372 0.355 0.314 0.231 -0.088 -0.292 0.691 (0.032)
LSTM Avg 0.926 0.830 0.807 0.843 0.623 0.645 0.640 0.380 -0.146 -1.108 2.034 1.720 SR 0.722 0.643 0.552 0.525 0.362 0.354 0.343 0.175 -0.055 -0.338 0.744 (0.010)
GRU Avg 0.916 0.855 0.836 0.831 0.679 0.656 0.586 0.447 -0.212 -0.944 1.860 1.536 SR 0.713 0.658 0.575 0.519 0.393 0.362 0.312 0.205 -0.082 -0.286 0.671 (0.030)
Informer Avg 0.908 0.816 0.796 0.835 0.609 0.632 0.615 0.464 -0.133 -1.095 2.002 1.680 SR 0.709 0.623 0.531 0.510 0.355 0.349 0.328 0.212 -0.050 -0.329 0.719 (0.013)
EInformer Avg 0.938 0.758 0.815 0.801 0.643 0.632 0.605 0.434 -0.146 -0.911 1.850 1.501 SR 0.737 0.582 0.555 0.494 0.373 0.350 0.321 0.199 -0.055 -0.279 0.678 (0.029)
DInformer Avg 0.913 0.807 0.776 0.841 0.625 0.646 0.548 0.512 -0.149 -0.949 1.862 1.519 SR 0.714 0.604 0.509 0.508 0.363 0.356 0.292 0.236 -0.056 -0.294 0.689 (0.023)
Spatial-temporal Models
SGA Avg 0.918 0.800 0.830 0.797 0.693 0.679 0.554 0.346 -0.049 -1.251 2.169 1.812 SR 0.719 0.612 0.566 0.500 0.403 0.380 0.290 0.160 -0.018 -0.378 0.780 (0.013)
ReSGA Avg 0.905 0.806 0.868 0.819 0.697 0.702 0.552 0.336 -0.069 -1.308 2.213 2.2132.213 1.8421.8421.842 SR 0.710 0.613 0.585 0.510 0.401 0.391 0.291 0.153 -0.026 -0.392 0.787 0.7870.787 (0.013)
Econometric Models
GAS Avg 0.917 0.831 0.767 0.785 0.678 0.636 0.693 0.513 0.097 -0.705 1.621 1.217 SR 0.703 0.655 0.587 0.519 0.394 0.348 0.357 0.238 0.038 -0.237 0.672 (0.051)
GARCH Avg 0.899 0.809 0.837 0.806 0.714 0.712 0.556 0.539 0.037 -0.496 1.395 1.012 SR 0.695 0.630 0.629 0.546 0.418 0.387 0.285 0.252 0.015 -0.161 0.562 (0.128)
Notes.This table reports the performance of value-weighted decile portfolios constructed usingα i,t in (11) as
sorting signal, where cESi,t is computed from each model. The column “Alpha” reports the estimated alpha
(intercept) and the correspondingp-value of thet-statistic (in parentheses) in the Fama–French five-factor
regression. For the H–L portfolios, the largest values of Avg, SR, and Alpha are highlighted in boldface. Other
descriptions are consistent with those in Table 5.

24
we vary the number of model parameters by adjusting width/depth-related hyperparameters,
while keeping all other mechanisms unchanged 4. This approach produces multiple variants of
each model with substantially different numbers of learnable parameters. The connection be-
tween hyperparameter choices and parameter size for each model is reported in Table D15 of
the supplementary materials.
Table 7 details the out-of-sample average loss of different models when their parameter size
varies over several orders of magnitude. It includes exact loss values, while its accompanying
figure visualizes the corresponding scaling patterns 5. Combining both pieces of evidence, we
obtain three main interesting findings:
•ReSGA consistently outperforms all competitors once the parameter size reaches 10 5 or
above, with SGA ranking second, whereas Informer achieves the lowest loss at smaller
scales. This pattern is evident from the bold entries in the table and the crossing behavior
in the figure: ReSGA and SGA improve sharply from small to intermediate scales, while
Informer deteriorates once its parameter size becomes large. These findings indicate that
models with richer spatial-temporal inputs, such as SGA and ReSGA, need sufficient
capacity in parameters to exploit useful information from inputs, while temporal models
can perform well with relatively few parameters. In contrast, the point-wise model of NN
benefits little from expanded capacity, likely because its input information is inherently
limited.
•There is no systematic evidence for a general virtue of model complexity. Except for
LSTM, the parameter-richest specification (around 10 7 parameters) does not deliver the
best performance within each model family. The figure makes this non-monotonicity
especially visible: Most loss curves flatten or turn upward after intermediate scales. Even
for LSTM, where loss performance improves with scale, the gains are modest. Meanwhile,
LSTM with around 107 parameters still underperforms ReSGA with 105 parameters. This
4For example, in the NN model, parameter size is controlled by the hidden-state dimension and the number
of hidden layers. See Section B.1.2 for more details.
5For each model, we fit a polynomial function linking loss to log parameter size, with the polynomial order
selected by the Akaike information criterion (Akaike, 1974).

25
absence of monotonic and substantial improvement suggests that simply increasing model
size alone does not guarantee better tail-risk forecasts.
•As shown by Kaplan et al. (2020), in natural language processing, optimal performance
is often achieved when model size is of the same order as the in-sample data size. This
principle is only partially supported in our financial task. To be specific, ReSGA and SGA
achieve their lowest out-of-sample losses at around 10 6 parameters, which is comparable
to the effective training sample size (approximately 2×10 6); however, this alignment is
not universal, since other models show no clear match between optimal parameter size
and sample size. These observations point to the heterogeneity in the virtue of data com-
plexity: Spatial-temporal models could exploit richer inputs, allowing for more capacity
in parameters to be used effectively, whereas temporal and point-wise models rely on less
information and consequently obtain fewer benefits from increased parameterization.
Meanwhile, Table 8 reports the out-of-sample Sharpe ratios of H–L portfolios as parameter
size varies, with an accompanying figure to visualize the trend of Sharpe ratio across parameter
scales. From Table 8, we find that Sharpe ratio fails to exhibit a clear monotonic pattern as the
parameter size increases. First, the best-performing parameter size differs across models: Most
models peak at intermediate scales, while LSTM and Informer attain their highest Sharpe ratios
at the largest scale. Second, the leading model also changes across parameter scales. These
mixed patterns indicate that increasing model complexity alone does not reliably improve
portfolio-level gains.
To further examine the virtue of data complexity in learning VaR and ES, we next evaluate
scaling performance with respect to in-sample data size. Specifically, we hold each model fixed
and vary the fraction of available in-sample data used for training and validation, from 1% to
100% of the full in-sample dataset. For each fraction, we draw the in-sample data uniformly at
random from the full in-sample dataset, and keep the hyperparameter configuration fixed at
the values selected using the full in-sample dataset. This design holds model complexity fixed,
and it isolates the role of in-sample data size that is one key dimension of data complexity.
Table 9 reports the out-of-sample average loss across different in-sample data sizes, while
its accompanying figure visualizes how these losses evolve as more in-sample data become

26
Table 7
Out-of-sample average loss across different parameter sizes.
Model≈10 3 ≈10 4 ≈10 5 ≈10 6 ≈10 7
NN 3.3322 3.3128 3.3236 3.3568 3.6057
LANN – 3.3440 3.3923 3.4627 3.7543
DLinear 3.3180 3.3166 3.3153 3.3174 3.3153
LSTM 3.3184 3.3063 3.3083 3.3088 3.3024
GRU 3.3067 3.3065 3.3022 3.2997 3.3003
Informer 3.2999 3.29993.2999 3.2985 3.29853.2985 3.3361 3.3812 3.4128
EInformer 3.3136 3.3163 3.3187 3.3276 3.3806
DInformer 3.3134 3.3097 3.3276 3.3310 3.3428
SGA 3.3319 3.3234 3.2934 3.2868 3.2965
ReSGA 3.3417 3.3250 3.2915 3.29153.2915 3.2793 3.27933.2793 3.28793.28793.2879
Notes.The table (upper panel) reports out-of-sample average lossℓ oos for different models with varying
parameter sizes (approximately 103 to 107 parameters), withS t formed by all stocks. Underlined entries
indicate the lowest loss in each row, and the lowest loss in each column is highlighted in boldface. “–”
indicates no feasible hyperparameters for constructing such parameter size. The accompanying figure
(bottom panel) visualizes the corresponding scaling behavior of average loss across different parameter
scales. Here, the dotted line stands for the best loss (= 3.2793).
available. From this table and its accompanying figure, we can reach the following findings:

27
Table 8
Out-of-sample H–L portfolio Sharpe ratios across different parameter sizes.
Model≈10 3 ≈10 4 ≈10 5 ≈10 6 ≈10 7
NN 0.659 0.659 0.660 0.736 0.718
LANN – 0.723 0.794 0.7940.794 0.703 0.695
DLinear 0.666 0.691 0.666 0.648 0.650
LSTM 0.670 0.744 0.7440.744 0.671 0.710 0.756 0.7560.756
GRU 0.714 0.700 0.671 0.740 0.697
Informer 0.717 0.7170.717 0.719 0.702 0.725 0.729
EInformer 0.639 0.694 0.713 0.678 0.712
DInformer 0.689 0.711 0.647 0.686 0.658
SGA 0.633 0.658 0.710 0.780 0.755
ReSGA 0.622 0.673 0.765 0.787 0.7870.787 0.749
Notes.The table (upper panel) reports the annualized Sharpe ratio (SR) of H–L portfolios under different
parameter scales. Underlined entries indicate the highest SR in each row, and the highest SR in each column
is highlighted in boldface. “–” indicates that the corresponding result is unavailable. The accompanying
figure (bottom panel) plots SRs to visualize the scaling pattern across different parameter scales from the
economic perspective. Here, the dotted line stands for the best SR (= 0.794).
•All models benefit from more in-sample data (from 1% to 100%). With the exception of
EInformer, each model attains its best performance when the full in-sample dataset is

28
available. Meanwhile, the loss curves in the figure mostly present monotonic pattern and
decline as the sample fraction increases.
•The best-performing model changes with the amount of in-sample data. When in-sample
data are scarce (only 1%, 5%, or 10%), temporal models such as GRU and Informer
outperform the other models. Once the fraction of used in-sample data reaches 25%
or above, the spatial-temporal models (SGA and especially ReSGA) become dominant,
indicating that these models require sufficient data to fully exploit cross-sectional sharing
and long-term temporal dependencies.
•Point-wise model, NN, exhibits the largest improvement as the amount of in-sample data
grows, consistent with its reliance on pooled cross-sectional information to compensate
for weaker inductive structure. Nevertheless, even with the full in-sample dataset, NN
remains clearly outperformed by the best temporal and spatial-temporal models. Thus,
more data help broadly, with the greatest statistical gains when the model can use the
richest in-sample information effectively.
Beyond evaluation from loss, Table 10 reports the out-of-sample Sharpe ratios of H–L port-
folios when the in-sample data size varies, while its accompanying figure visualizes the scaling
patterns of Sharpe ratio. Being broadly consistent with the loss results in Table 9, this table
delivers the following notable results from the economic perspective:
•ReSGA delivers the highest Sharpe ratio across different models once the in-sample data
size reaches at least 25% of the full dataset.
•The fitted curves show that portfolio performance generally improves as more in-sample
data become available, although the pattern is not strictly monotonic for every model.
Taken together, the above results show that a larger in-sample dataset can lead to stronger
economic performance, especially for models that can effectively exploit rich information.
Overall, our analysis results provide little support for the virtue of model complexity. Instead,
they highlight the importance of data complexity: Performance gains arise mainly from models
that can exploit richer information with the use of a larger in-sample data size, rather than a
larger parameter size alone. While the available sample size is always limited in finance, this

29
Table 9
Out-of-sample average loss across different in-sample data sizes.
Model 1% 5% 10% 25% 50% 100%
NN 4.4749 4.4075 4.3214 3.6949 3.3621 3.3322
LANN 4.4241 4.3898 4.3771 4.0613 3.4774 3.3440
DLinear 3.3679 3.3363 3.3248 3.3201 3.3175 3.3166
LSTM 3.3506 3.3227 3.3147 3.3102 3.3090 3.3063
GRU 3.3387 3.33873.3387 3.3172 3.31723.3172 3.3117 3.3093 3.3068 3.3022
Informer 3.3585 3.3262 3.3094 3.30943.3094 3.2996 3.2995 3.2985
EInformer 3.3470 3.3363 3.3350 3.3329 3.3269 3.3276
DInformer 3.6000 3.3531 3.3259 3.3184 3.3164 3.3134
SGA 3.4851 3.3680 3.3246 3.2995 3.2907 3.29073.2907 3.2868
ReSGA 3.4938 3.3734 3.3378 3.2933 3.29333.2933 3.2936 3.2793 3.27933.2793
Notes.The table (upper panel) reports the out-of-sample average loss of each model, as the in-sample
data size varies across{1%,5%,10%,25%,50%,100%}of the full in-sample dataset. The accompanying
figure (bottom panel) visualizes the corresponding scaling behavior of average loss across different in-
sample data sizes. Other descriptions are consistent with those in Table 7.
motivates the next scaling dimension: expanding the effective information content of the input
with appropriate model specification and enough parameters, which appears to be a more
effective path to improving tail risk forecasting accuracy than simply increasing model size.

30
Table 10
Out-of-sample H–L portfolio Sharpe ratios across different in-sample sizes.
Model 1% 5% 10% 25% 50% 100%
NN 0.324 0.404 0.525 0.676 0.732 0.659
LANN 0.328 0.320 0.346 0.494 0.666 0.723
DLinear 0.588 0.653 0.630 0.655 0.677 0.691
LSTM 0.608 0.666 0.666 0.662 0.712 0.744
GRU 0.607 0.692 0.6920.692 0.670 0.661 0.664 0.671
Informer 0.656 0.6560.656 0.665 0.675 0.6750.675 0.690 0.687 0.719
EInformer 0.640 0.624 0.615 0.652 0.685 0.678
DInformer 0.523 0.659 0.665 0.683 0.673 0.689
SGA 0.617 0.629 0.628 0.685 0.763 0.780
ReSGA 0.618 0.632 0.663 0.705 0.7050.705 0.782 0.7820.782 0.787 0.7870.787
Notes.The table (upper panel) reports the annualized Sharpe ratio (SR) of H–L portfolios under
different in-sample data sizes. The accompanying figure (bottom panel) plots SRs to visualize the
scaling pattern across different in-sample data sizes from the economic perspective. Other descrip-
tions are consistent with those in Table 8.
3.5.Group Importance.A further empirical question concerns which firm characteristics
are most important for forecasting tail risk. Due to the superior performance of ReSGA from
both statistical and economic perspectives, we utilize this model to tackle the above question.

31
Assessing importance at the level of individual characteristics, however, is challenging due
to the well-known dilution problem: When many characteristics are highly correlated, their
marginal contributions become spread across related variables, obscuring the true economic
drivers of predictive performance (Li and Tang, 2025). To address this issue, we assess impor-
tance at the group level rather than at the level of individual characteristics. Specifically, we
adopt the 13-category taxonomy of Jensen, Kelly and Pedersen (2023), which organizes the 153
firm characteristics into economically interpretable groups, including Low Risk, Value, Quality,
Low Leverage, Momentum, Size, Profit Growth, Short-Term Reversal, Seasonality, Investment,
Profitability, Debt Issuance, and Accruals. As argued by Li and Tang (2025), grouping char-
acteristics reduces redundancy among highly correlated signals and provides a clearer decom-
position of predictive content. This approach allows us to evaluate the incremental value of
entire economic themes, rather than attributing importance to individual characteristics that
may proxy for similar information.
We quantify group importance via a drop-group procedure. To be specific, for each group
(denoted asG), we follow Gu, Kelly and Xiu (2020) to construct perturbed testing samples in
which all characteristics in groupGare set to zero, while all remaining characteristics are left
unchanged. By passing these perturbed samples through the trained model to generate new
forecasts, we recompute the out-of-sample average loss in (10) on these new forecasts, with
the setS t containing all examined stocks. Then, we measure the importance of groupGby
the increase in loss of perturbed samples relative to that obtained using the original testing
samples. After computing importance for all 13 groups, we set negative values to zero to avoid
spurious attribution and normalize the remaining values to sum to one.
Figure 1 exhibits the ten most important groups from ReSGA over the out-of-sample period
(2014.01–2023.12). From this figure, two clear and economically intuitive patterns emerge.
•The top five groups (Value, Low Risk, Momentum, Quality, and Short-Term Reversal)
together account for more than 90% of importance for the full dataset. This concentration
indicates that tail risk predictability is driven by a small set of groups rather than
being evenly distributed across all characteristics. Similar findings can be found in the
asset pricing literature (Gu, Kelly and Xiu, 2020, 2021; Yang et al., 2024). Note that

32
Fig 1: Group importance from ReSGA during the out-of-sample period.
the concentration is even stronger for mega- and large-cap stocks, with top five groups
receiving over 99% importance, whereas the top five groups in small-, micro-, and nano-
stocks contribute 91%, 89%, and 94%, respectively.
•The ranking of the leading groups shows both stability and systematic variation across
different levels of market capitalization. Generally speaking, Low Risk and Momentum
are consistently important regardless of the level of market capitalization. This is in-
tuitive, as volatility- and beta-related characteristics in Low Risk are closely linked to
tail risk, while Momentum captures persistent return dynamics that affect tail outcomes.
Apart from these two common drivers, for mega- and large-cap stocks, Quality and
Low Leverage are more influential, suggesting that tail risk variation among large firms
is closely tied to balance-sheet strength and financial stability; in contrast, for small-,
micro-, and nano-cap stocks, Value and Short-Term Reversal become more crucial, where
valuation performance and short-horizon price reversals are expected to closely relate to
distress risk, illiquidity, and left-tail outcomes of those stocks.

33
Moreover, Figure 2 traces the month-by-month evolution of group importance for ReSGA,
where we compute group importance using the increase of loss from each month. Its heatmap
reinforces that Low Risk remains important almost throughout the entire out-of-sample period,
consistent with its role documented from Figure 1. As one may expect, the importance of Low
Risk was especially pronounced from April to September 2020, since the COVID-19 shock had
severely disrupted global financial markets. In contrast, Value and Quality display a visible
“complementary” pattern over time, where the elevated period of Quality importance often
coincides with muted Value, and vice versa. This finding suggests that the dominant predictors
of tail risk shift between valuation-driven repricing forces and balance-sheet resilience/financial
strength. Additionally, Quality and Low Leverage exhibit similar dynamics in certain months,
a similarity that is expected due to their overlapping economic content related to profitability,
safety, and leverage constraints.
Fig 2: Group importance from ReSGA across months during the out-of-sample period.
4. Transfer Learning.Fundamentally, our universal models are driven by a principle
that tail risk is governed by a mapping structure from asset characteristics to risk scores. As

34
long as relevant asset characteristics are available, the model, by construction, can be applied
to different assets without re-estimation. This contrasts sharply with econometric models, such
as GARCH and GAS, which are inherently asset-specific. Hence, it raises a natural question:
Can a universal model, trained on the largest and most information-rich US equity market,
generalize to other equity markets without re-estimation?
To address this question, we conduct a transfer learning exercise. To be specific, we train each
universal model exclusively on US equity dataset as in Section 3 and then apply it, without
any re-training or fine-tuning, to five major international equity markets: China, Japan, UK,
Australia, and Canada. This exercise allows us to assess whether the universal models capture
fundamental relationships between firm characteristics and future tail risk across different
institutional, regulatory, and liquidity environments.
Table 11 reports the out-of-sample average loss across universal models and international
equity markets. From this table, we have the following noteworthy findings:
•Despite substantial cross-market heterogeneity, ReSGA delivers the lowest out-of-sample
loss in Japan, UK, and Australia, and remains highly competitive in China (ranked
fourth) and Canada (ranked second). This strong and stable performance indicates that
the predictive structure learned by ReSGA from US data generalizes well across inter-
national equity markets, even without re-estimation.
•In contrast, SGA performs poorly in most non-US markets, except for Canada. In par-
ticular, it is often dominated by simpler temporal models. This pattern suggests that
cross-sectional dependence learned in the source market does not necessarily transfer
well to other markets, potentially diluting asset-level tail-risk signals and introducing
noise. The relatively strong performance of SGA in Canada is plausibly attributable to
the close economic integration and high similarity between the US and Canadian equity
markets, which makes cross-sectional structures learned from US data more transferable
in this case. Note that ReSGA mitigates the above limitation of SGA by augmenting
cross-sectional grouping with a retrieval mechanism that extends the effective temporal
memory. The ability to exploit long historical information appears to compensate for po-
tential misspecification in the cross-sectional structure, resulting in more robust transfer

35
performance across markets.
•Temporal models, such as GRU, LSTM, and DLinear, also exhibit relatively stable out-
of-sample performance across markets and often rank among the top predictors. This
robustness further supports the view that temporal dynamics constitute a more transfer-
able source of predictive power than cross-sectional dependence when models are deployed
across markets without re-estimation.
Table 11
Out-of-sample average loss across different universal models and equity markets.
China Japan UK Australia Canada
Point-wise Models
Linear 3.3011 3.0623 3.4380 3.7542 3.5735
NN 3.3285 3.0274 3.4260 3.6783 3.4846
Temporal Models
LANN 3.2924 2.9953 3.4582 3.7393 3.5002
DLinear 3.2652 2.9796 3.4470 3.7843 3.5455
LSTM 3.2677 2.9521 3.4262 3.6733 3.5375
GRU 3.2547 3.25473.2547 2.9408 3.4352 3.6962 3.5364
Informer 3.2943 2.9587 3.4267 3.7586 3.5118
EInformer 3.3146 2.9810 3.4680 3.8530 3.5785
DInformer 3.2661 2.9799 3.4394 3.7640 3.5347
Spatial-temporal Models
SGA 3.6346 3.1192 3.5729 3.8702 3.4071 3.40713.4071
ReSGA 3.2666 2.8884 2.88842.8884 3.3992 3.39923.3992 3.6333 3.63333.6333 3.4100
Notes.This table reports out-of-sample average loss, which is obtained by applying each universal model
trained exclusively on the US equity market to other five global markets. Lower values indicate better tail
risk forecasting performance, with the lowest value for each market being highlighted in boldface.
Besides the loss analysis, Table 12 further displays the models in the final model set from
the MCS test for the transfer learning across markets. For reference, we also include the earlier

36
results for the US market, where only SGA and ReSGA remain in the final model set. The
cross-market evidence from Table 12 delivers a clear message: ReSGA is the only model selected
in all final model sets. This result indicates that the advantage of ReSGA is not confined to the
US market, but generalizes robustly across international equity universes. Moreover, the CC
and AESR testing results in Table 13 provide further evidence of the effectiveness of ReSGA
in transfer learning: Across the five target markets, ReSGA delivers consistently strong pass
rates for both VaR and ES forecasts and ranks among the top performers in nearly all cases.
Table 12
Selected models in the final model set constructed by the MCS test across markets.
Model US China Japan UK Australia Canada
Linear –✓– – – –
NN – – – – – –
LANN – – – – – –
DLinear –✓– – – –
LSTM –✓–✓– –
GRU –✓ ✓– – –
Informer – – – – – –
EInformer – – – – – –
DInformer –✓– – – –
SGA✓– – – –✓
ReSGA✓ ✓ ✓ ✓ ✓ ✓
Notes.A model with check mark (✓) remains in the final model set, which is constructed by the MCS test at
the 90% confidence level for the corresponding market.
Lastly, we examine the economic gains of ReSGA in the transfer learning exercise. Table 14
reports cross-market portfolio performance based on the ES-driven trading signal defined in
(11). Its results show that portfolio return patterns differ substantially between US and non-
US markets. In China and Japan, the decile portfolios exhibit a reversed pattern, with higher
predicted signal associated with higher returns, leading to negative H–L portfolio performance.
In the UK, Australia, and Canada, the results are more heterogeneous. Although monotonicity

37
Table 13
Pass rates of stocks with valid VaR (or ES) predictions across different models and markets.
VaR ES
China Japan UK Australia Canada China Japan UK Australia Canada
Point-wise Models
Linear 92.65 61.40 81.55 48.85 55.55 75.37 20.88 82.71 91.90 85.51
NN 94.90 67.98 86.65 63.98 69.52 50.59 23.74 66.25 78.03 74.80
Temporal Models
LANN 95.60 75.44 84.46 62.11 71.41 37.31 24.68 58.78 66.67 66.62
DLinear 93.77 71.68 84.17 57.56 67.80 81.42 40.69 85.77 89.25 82.51
LSTM 95.38 85.22 89.20 75.07 74.01 75.36 54.28 85.58 89.25 77.04
GRU 95.38 87.35 85.87 67.65 72.71 77.19 72.61 88.72 91.18 81.71
Informer 93.55 77.46 86.56 61.52 70.11 82.47 48.53 88.17 91.27 83.44
EInformer 94.13 73.34 81.78 51.94 65.34 79.52 41.01 87.52 88.08 85.45
DInformer 93.16 70.27 85.49 58.03 68.59 82.98 82.9882.98 39.21 88.45 91.10 84.38
Spatial-temporal Models
SGA 51.65 69.26 75.42 50.61 88.59 88.5988.59 75.98 87.62 87.6287.62 91.4091.4091.40 90.85 86.92
ReSGA 95.6295.6295.62 89.9789.9789.97 91.6391.6391.63 75.4275.4275.42 88.45 67.39 70.55 87.99 95.05 95.0595.05 89.7289.7289.72
Notes.This table reports pass rate of stocks in each market with valid VaR (or ES) predictions, assessed
using the CC (or AESR) test at the significance levelα= 0.05. For each column, the largest pass rate is
highlighted in boldface.
is weaker, the extreme deciles display substantial return dispersion, especially in the lowest-
signal portfolios, which drive large negative H–L returns. These findings suggest that the pricing
of tail risk varies across markets, likely reflecting differences in market structure, investor
behavior, and risk premia.
Taken together, the transfer learning results reinforce our central conclusions: ReSGA func-
tions as a general engine for tail risk forecasting.

38
Table 14
Cross-market decile portfolio performance from ReSGA.
Market Metric P1 P2 P3 P4 P5 P6 P7 P8 P9 P10 H–L
US Avg 0.905 0.806 0.868 0.819 0.697 0.702 0.552 0.336 -0.069 -1.308 2.213 SR 0.710 0.613 0.585 0.510 0.401 0.391 0.291 0.153 -0.026 -0.392 0.787
China Avg 0.431 0.526 0.576 0.607 0.729 0.769 1.022 1.225 1.360 1.848 -1.417 SR 0.216 0.250 0.265 0.264 0.296 0.315 0.401 0.465 0.523 0.654 -0.619
Japan Avg 0.451 0.380 0.527 0.527 0.615 0.525 0.563 0.644 0.620 1.146 -0.696 SR 0.403 0.358 0.478 0.468 0.525 0.443 0.438 0.462 0.384 0.610 -0.543
UK Avg 0.240 0.325 0.367 0.328 0.046 -0.005 -0.296 -0.568 -0.196 7.021 -6.781 SR 0.175 0.199 0.221 0.204 0.029 -0.003 -0.171 -0.292 -0.081 0.602 -0.586
Australia Avg 0.545 0.528 0.501 0.299 0.210 0.537 0.531 1.541 1.676 5.324 -4.778 SR 0.319 0.295 0.265 0.160 0.096 0.227 0.196 0.454 0.524 1.406 -1.553
Canada Avg 0.547 0.531 0.610 0.749 0.564 0.690 0.654 0.569 2.135 3.795 -3.248 SR 0.367 0.388 0.382 0.405 0.299 0.329 0.312 0.248 0.652 1.111 -1.191
Notes.This table reports the performance of value-weighted decile portfolios (across markets), constructed
usingα i,t in (11) as sorting signal, where cESi,t is computed from ReSGA. Here, ReSGA is only trained on
the US data and applied to other markets without re-estimation. At each month, stocks in every market
are sorted in descending order ofα i,t and assigned to ten portfolios (P1–P10). Other descriptions are
consistent with those in Table 5.
5. Conclusion.This paper studies tail risk forecasting, with a particular focus on VaR
and ES, in the era of big data. Methodologically, we develop a unified joint VaR-ES learning
framework supervised by the FZ loss. Based on this framework, we propose a large tail risk
model, ReSGA, which captures the nonlinear relationships between asset characteristics and
VaR-ES by accounting for spatial and temporal dependencies among assets. Empirically, using
nearly a century of US equity data covering over 40,000 stocks and 153 firm characteristics, we
find that ReSGA consistently delivers the best out-of-sample forecasting performance among a
broad set of competing models. These forecasting gains are economically meaningful: Trading
strategies based on ReSGA forecasts exhibit pronounced left-tail momentum and deliver su-
perior long-short decile portfolio performances using a newly proposed size-enhanced left-side
momentum signal.
Moreover, we provide systematic evidence on the scaling behavior of ReSGA and other
machine-learning-based universal models. Our results offer little support for a general virtue
of model complexity measured by parameter size alone. Instead, they favor the virtue of data

39
complexity in learning tail risk, as improvements in forecasting VaR and ES can be achieved
through larger in-sample datasets or more informative model inputs. In other words, the success
of ReSGA is not only due to its access to rich available information but also to its ability to
effectively extract, share, and utilize this information. Finally, we conduct group-importance
analysis and transfer-learning experiments to illustrate the interpretability and cross-market
generalizability of ReSGA.
References.
Acerbi, C.andSzekely, B.(2014). Back-testing Expected Shortfall.Risk2776–81.
Acerbi, C.andTasche, D.(2002). On the Coherence of Expected Shortfall.Journal of Banking & Finance
261487–1503.
Akaike, H.(1974). A New Look at the Statistical Model Identification.IEEE Transactions on Automatic
Control19716–723.
Artzner, P.,Delbaen, F.,Eber, J.-M.andHeath, D.(1999). Coherent Measures of Risk.Mathematical
Finance9203–228.
Atilgan, Y.,Bali, T. G.,Demirtas, K. O.andGunaydin, A. D.(2020). Left-Tail Momentum: Underre-
action to Bad News, Costly Arbitrage and Equity Returns.Journal of Financial Economics135725–753.
Bayer, S.andDimitriadis, T.(2022). Regression-Based Expected Shortfall Backtesting.Journal of Financial
Econometrics20437–471.
Berk, J. B.(2023). Comment on “The Virtue of Complexity in Return Prediction” SSRN Working Paper
No. 4410125, SSRN.
Buncic, D.(2025). Simplified: A Closer Look at the Virtue of Complexity in Return Prediction SSRN Working
Paper No. 5239006, SSRN.
Cartea, ´A.,Jin, Q.andShi, Y.(2025). The Limited Virtue of Complexity in a Noisy World SSRN Working
Paper No. 5202064, SSRN.
Christoffersen, P. F.(1998). Evaluating Interval Forecasts.International Economic Review39841–862.
Chronopoulos, I.,Raftapostolos, A.andKapetanios, G.(2024). Forecasting Value-at-Risk Using Deep
Neural Network Quantile Regression.Journal of Financial Econometrics22636–669.
Chung, J.,Gulcehre, C.,Cho, K.andBengio, Y.(2014). Empirical Evaluation of Gated Recurrent
Neural Networks on Sequence Modeling.ArXiv preprint “arXiv:1412.3555”.
Das, A.,Kong, W.,Sen, R.andZhou, Y.(2024). A Decoder-Only Foundation Model for Time-Series
Forecasting. InProceedings of the 41st International Conference on Machine Learning23510148–10167.
Didisheim, A.,Ke, S. B.,Kelly, B.andMalamud, S.(2024). APT or “AIPT”? The Surprising Dominance
of Large Factor Models Working Paper No. 33012, National Bureau of Economic Research.

40
Diebold, F. X.andMariano, R. S.(1995). Comparing Predictive Accuracy.Journal of Business & Eco-
nomic Statistics13253–263.
Dong, L.,Xu, S.andXu, B.(2018). Speech-Transformer: A No-Recurrence Sequence-to-Sequence Model
for Speech Recognition. In2018 IEEE International Conference on Acoustics, Speech and Signal Processing
(ICASSP)5884–5888.
Dosovitskiy, A.,Beyer, L.,Kolesnikov, A.,Weissenborn, D.,Zhai, X.,Unterthiner, T.,De-
hghani, M.,Minderer, M.,Heigold, G.,Gelly, S.,Uszkoreit, J.andHoulsby, N.(2021). An
Image is Worth 16x16 Words: Transformers for Image Recognition at Scale. InInternational Conference on
Learning Representations.
Du, Z.andEscanciano, J. C.(2017). Backtesting Expected Shortfall: Accounting for Tail Risk.Management
Science63940–958.
Dugas, C.,Bengio, Y.,B ´elisle, F.,Nadeau, C.andGarcia, R.(2000). Incorporating Second-Order
Functional Knowledge for Better Option Pricing. InAdvances in Neural Information Processing Systems13
472–478.
F ama, E. F.andFrench, K. R.(2015). A Five-Factor Asset Pricing Model.Journal of Financial Economics
1161–22.
Feng, C.,Huang, L.andKrompass, D.(2024). General Time Transformer: An Encoder-Only Foundation
Model for Zero-Shot Multivariate Time Series Forecasting. InProceedings of the 33rd ACM International
Conference on Information and Knowledge Management3757–3761.
Fissler, T.andZiegel, J. F.(2016). Higher Order Elicitability and Osband’s Principle.The Annals of
Statistics441680–1707.
Gneiting, T.(2011). Making and Evaluating Point Forecasts.Journal of the American Statistical Association
106746–762.
Goodfellow, I.,Bengio, Y.andCourville, A.(2016).Deep Learning. MIT press.
Gu, S.,Kelly, B.andXiu, D.(2020). Empirical Asset Pricing via Machine Learning.The Review of Financial
Studies332223–2273.
Gu, S.,Kelly, B.andXiu, D.(2021). Autoencoder Asset Pricing Models.Journal of Econometrics222
429–450.
Hansen, P. R.,Lunde, A.andNason, J. M.(2011). The Model Confidence Set.Econometrica79453–497.
Hochreiter, S.andSchmidhuber, J.(1997). Long Short-Term Memory.Neural Computation91735–1780.
Ioffe, S.andSzegedy, C.(2015). Batch Normalization: Accelerating Deep Network Training by Reducing
Internal Covariate Shift. InProceedings of the 32nd International Conference on Machine Learning37448–
456.
Jensen, T. I.,Kelly, B.andPedersen, L. H.(2023). Is There a Replication Crisis in Finance?The Journal
of Finance782465–2518.

41
Kaplan, J.,McCandlish, S.,Henighan, T.,Brown, T. B.,Chess, B.,Child, R.,Gray, S.,Rad-
ford, A.,Wu, J.andAmodei, D.(2020). Scaling Laws for Neural Language Models.ArXiv preprint
“arXiv:2001.08361”.
Kelly, B.,Malamud, S.andZhou, K.(2024). The Virtue of Complexity in Return Prediction.The Journal
of Finance79459–503.
Kelly, B.,Kuznetsov, B.,Malamud, S.andXu, T. A.(2025). Artificial Intelligence Asset Pricing Models
Working Paper No. 33351, National Bureau of Economic Research.
Kingma, D. P.andBa, J.(2015). Adam: A Method for Stochastic Optimization. InInternational Conference
on Learning Representations.
Koenker, R.andBassett, G.(1978). Regression Quantiles.Econometrica4633–50.
Li, S. Z.andTang, Y.(2025). Automated Volatility Forecasting.Management Science716248–6274.
Li, H.andW ang, R.(2023). PEL VE: Probability Equivalent Level of VaR and ES.Journal of Econometrics
234353–370.
Masters, T.(1993).Practical Neural Network Recipes in C++. Academic Press.
Merlo, L.,Petrella, L.andRaponi, V.(2021). Forecasting VaR and ES Using a Joint Quantile Regression
and Its Implications in Portfolio Allocation.Journal of Banking & Finance133106248.
Nagel, S.(2025). Seemingly Virtuous Complexity in Return Prediction Working Paper No. 34104, National
Bureau of Economic Research.
Newey, W. K.andWest, K. D.(1987). A Simple, Positive Semi-Definite, Heteroskedasticity and Autocor-
relation Consistent Covariance Matrix.Econometrica55703–708.
Basel Committee on Banking Supervision(2019). Minimum Capital Requirements for Market Risk Basel
Committee on Banking Supervision Publication, Bank for International Settlements.
Oreshkin, B. N.,Carpov, D.,Chapados, N.andBengio, Y.(2020). N-BEATS: Neural Basis Expansion
Analysis for Interpretable Time Series Forecasting. InInternational Conference on Learning Representa-
tions.
Patton, A. J.,Ziegel, J. F.andChen, R.(2019). Dynamic Semiparametric Models for Expected Shortfall
(and Value-at-Risk).Journal of Econometrics211388–413.
Rockafellar, R. T.andUryasev, S.(2002). Conditional Value-at-Risk for General Loss Distributions.
Journal of Banking & Finance261443–1471.
Taylor, J. W.(2019). Forecasting Value at Risk and Expected Shortfall Using a Semiparametric Approach
Based on the Asymmetric Laplace Distribution.Journal of Business & Economic Statistics37121–133.
V aswani, A.,Shazeer, N.,Parmar, N.,Uszkoreit, J.,Jones, L.,Gomez, A. N.,Kaiser,  L.and
Polosukhin, I.(2017). Attention is All you Need. InAdvances in Neural Information Processing Systems
305998–6008.
Veliˇckovi´c, P.,Cucurull, G.,Casanova, A.,Romero, A.,Li `o, P.andBengio, Y.(2018). Graph

42
Attention Networks. InInternational Conference on Learning Representations.
W ang, Q.,W ang, R.andZiegel, J.(2025). E-Backtesting.forthcoming in Management Science.
Yang, X.,Zhu, Z.,Li, D.andZhu, K.(2024). Asset Pricing via the Conditional Quantile Variational
Autoencoder.Journal of Business & Economic Statistics42681–694.
Yao, Q.,Yang, C.-H. H.,Jiang, R.,Liang, Y.,Jin, M.andPan, S.(2025). Towards Neural Scaling Laws
for Time Series Foundation Models. InInternational Conference on Learning Representations.
Zeng, A.,Chen, M.,Zhang, L.andXu, Q.(2023). Are Transformers Effective for Time Series Forecasting?
InProceedings of the AAAI Conference on Artificial Intelligence3711121–11128.
Zhou, H.,Zhang, S.,Peng, J.,Zhang, S.,Li, J.,Xiong, H.andZhang, W.(2021). Informer: Beyond
Efficient Transformer for Long Sequence Time-Series Forecasting. InProceedings of the AAAI Conference
on Artificial Intelligence3511106–11115.
Zhu, Z.,Zhang, N.andZhu, K.(2024). Big Portfolio Selection by Graph-Based Conditional Moments
Method.Journal of Empirical Finance78101533.
Zhu, Z.andZhu, K.(2025). Machine Learning Vast Dynamic Conditional Covariance Matrices: the Spirit of
“Divide and Conquer”.Minor revision for Management Science.
APPENDIX A: THE ARCHITECTURE OF RESGA
A.1. Encoder.The encoder of ReSGA first applies the widely used recurrent neural net-
work, GRU (Chung et al., 2014), to extract the temporal featureH t. The GRU is designed
to capture temporal dynamics among asset characteristics through its recurrent hidden states.
Letx s i,t−1 =x i,t−1−S+s denote the input characteristic vector of assetiat time lags. Then,
the updates within the GRU are formulated as
(update gate)z s i,t = sigmoid  Wzxs i,t−1 +U zhs−1 i,t +b z  ,
(reset gate)r s i,t = sigmoid  Wrxs i,t−1 +U rhs−1 i,t +b r  ,
(candidate hidden state) ˜hs i,t = tanh  Whxs i,t−1 +U h  rs i,t ⊙h s−1 i,t  +b h  ,
(hidden state)h s i,t =z s i,t ⊙h s−1 i,t +  1−z s i,t  ⊙ ˜hs i,t,
(A1)
whereW ∗ ∈R D×P ,U ∗ ∈R D×D, andb ∗ ∈R D for∗ ∈ {z, r, h}are weight matrices and bias
vectors shared across time lags. The hidden-state dimensionDis a tunable hyperparameter
that controls model complexity, and⊙denotes element-wise multiplication. The element-wise
activation functions sigmoid and tanh are defined as sigmoid(x) = 1 1+e−x and tanh(x) = ex−e−x ex+e−x
forx∈R.

43
In (A1), the hidden stateh s i,t ∈R D serves as the key feature, summarizing the accumulated
temporal information up to lags, while ˜hs i,t represents the candidate hidden state, used to
store newly inputted informationx s i,t−1 at lags. The update gatez s i,t ∈(0,1) D controls how
much of the past information fromh s−1 i,t should be kept, whereas the reset gater s i,t ∈(0,1) D
determines the degree to which the previous hidden stateh s−1 i,t contributes to the candidate
state ˜hs i,t ∈(−1,1) D. Together, these gating mechanisms enable the GRU to adaptively balance
memory retention and new information integration, effectively capturing complex temporal
dependencies in an autoregressive manner.
For each asseti= 1, . . . , Nt and lags= 1, . . . , S, we obtain the hidden states{h1 i,t, . . . ,hS i,t}
from the GRU, and then we stack them into the temporal feature across all assets and lags to
construct
Ht = [H1,t, . . . ,HNt,t]∈R Nt×S×D withH i,t = [h1 i,t, . . . ,hS i,t]∈R S×D.(A2)
In addition toH t, the encoder of ReSGA uses the most recent hidden states{h S 1,t, . . . ,hS Nt,t}
to infer the latent group structure among assets. Specifically, it constructs a setM t that
captures inter-asset relationships based on the similarity of temporal features. To fulfill this,
we first treat each asset as a potential group center, with its node feature defined as
uk,t =h S k,t,fork= 1, . . . , Nt.
Then, we measure the similarity between assetiand centerkby the cosine similarity:
γi,k,t = Cosine

uk,t,h S i,t  = u′ k,thS i,t ∥uk,t∥ ∥hS i,t∥,fori, k= 1, . . . , Nt,
where∥ · ∥denotes theL2 norm. To mitigate the impact of weak or noisy similarities, we retain
only theK ∗ strongest connections for each asseti:
γ∗ i,k,t =



1,ifk=i,
γi,k,t,if|γ i,k,t|>Top(A i,t, K∗),
0,otherwise,
(A3)

44
whereK ∗ is a hyperparameter controlling the number of retained connections,A i,t ={|γ i,k,t|:
k̸=i}, and Top(A, b) denotes theb-th largest value in the setA.
After thresholding, we form each groupM k,t ={i:γ ∗ i,k,t ̸= 0}by gathering all assets con-
nected to centerk. Meanwhile, we discard those groups containing only their own center, as
single-member groups carry no sharing information. Consequently, we reach the group struc-
ture:
Mt ={M k,t :k=k 1, . . . , kKt},(A4)
wherek 1, . . . , kKt denote the indices of all identified group centers.
Our data-driven way to discover group structureM t matches many empirical practices. In
financial markets, assets such as stocks naturally form groups based on their shared charac-
teristics and economic linkages. Typically, stocks within the same groupM k,t tend to co-move
due to common factors such as industrial background, financial statement, or ownership back-
ground. For instance, technology companies like NVIDIA, Apple, Microsoft, and AMD tend
to cluster into the same group, as their prices are jointly affected by factors such as semicon-
ductor supply chains, innovation cycles, and market sentiment toward the tech sector. These
co-movements underscore the importance of modeling group-specific relationships to capture
heterogeneity across different groups. For more empirical elaborations on the group structures
in stock return forecasting, one can refer to Zhu, Zhang and Zhu (2024) and references therein.
Combining (A2) and (A4), we can equivalently write the workflow of encoder in a brief form
(Ht,M t) = Encoder(Xt−1;ϕ),(A5)
whereϕincludes all trainable parameters in (A1).
A.2. Retriever.Although the temporal featureh s i,t in (A1) summarizes the accumulated
temporal information up to lags(i.e. timet−S+s), it inevitably “forgets” long-term depen-
dencies due to the effects of the update and reset gates. Moreover, our encoder only extracts
the temporal feature for each asset independently, without incorporating useful temporal in-
formation from other related assets. For instance, during the 2022 technology sell-off, the price

45
movement of NVIDIA exhibited a pattern strikingly similar to that of Apple during the 2008
financial crisis: Both experienced rapid growth followed by sharp corrections driven by macroe-
conomic tightening. Retrieving such long-ago but structurally similar patterns across assets can
provide valuable insights that purely temporal models may overlook.
To address these limitations, we introduce the retriever of ReSGA, which captures struc-
turally similar patterns from the historical trajectories of related assets. Specifically, we parti-
tion theSlags intoL ∗ non-overlapping segments, forming
Hi,t = [h1 i,t, . . . ,hS/L∗ i,t , . . . ,h2S/L∗ i,t , . . . ,h(L∗−1)S/L∗ i,t , . . . ,hS i,t],
whereh lS/L∗ i,t forl= 1, . . . , L∗ represents the historical context up to timelS/L ∗, andL ∗ is a
user-specific hyperparameter satisfying thatSis divisible byL ∗. The temporal features from
theL ∗ segments thus act as reference checkpoints, each summarizing distinct stages of past
information for subsequent retrieval and comparison.
Next, we retrieve information from its related assets defined by the group structureM t. For
each asseti, the related assets are collected into a set
Ni,t ={k:i∈M k,t},(A6)
whereM k,t is the group centered at assetk. By construction,N i,t contains theK ∗ most similar
assets toiidentified by the encoder, indicating which assets’ historical trajectories should be
searched in the retrieval stage.
We now define the retrieval feature for assetiat timetby aggregating information from a
set of related assets. For each related assetj∈N i,t, its contribution to the retrieval feature of
assetiis given by
zi,j,t =
L∗−1X
l=1
αi,j,l,t h(lS/L∗)+1 j,t ∈R D,(A7)
whereα i,j,l,t is the normalized attention weight defined as
αi,j,l,t = exp(βi,j,l,t)PL∗−1
ℓ=1 exp(βi,j,ℓ,t)
,withβ i,j,l,t = Cosine

hS i,t,h lS/L∗ j,t  .(A8)

46
Here, the attention weightα i,j,l,t quantifies the similarity between the current temporal
feature of asseti,h S i,t, and the checkpoint feature of assetj,h lS/L∗ j,t . This similarity measures
how much the present feature of assetiresembles the past feature of assetjat segmentl.
Importantly, while the attention weights are based on these checkpoint features,z i,j,t uses the
subsequent featureh (lS/L∗)+1 j,t that immediately follows each checkpoint6. The rationale is that
if asseti’s current feature mirrors assetj’s historical feature at timelS/L ∗, then assetj’s next
state after that point provides valuable predictive information for asseti’s future evolution.
In this way, the retriever aligns historical features across assets and integrates their forward
states, allowing the model to infer potential future behavior from similar past behaviors.
Subsequently, we aggregate the contributions from all related assets to form the retrieval
feature. To fulfill this, we compute the average similarity between each related assetjand the
target assetiacross all checkpoints:
¯βi,j,t = 1 L∗ −1
L∗−1X
l=1
βi,j,l,t,
which captures the overall relevance of assetjto asseti. Then, following (A7) and (A8),
we calculate the relative contribution of each related asset and aggregate it into the retrieval
feature for each asseti:
zi,t =
X
j∈Ni,t
ωi,j,tzi,j,t ∈R D,withω i,j,t = exp( ¯βi,j,t)P
m∈Ni,t exp( ¯βi,m,t) .
Finally, we stack allz i,t across assets to obtain the retrieval feature:
Zt = Retriever(Ht;M t) = [z1,t, . . . ,zNt,t]∈R Nt×D.(A9)
By design,Z t aggregates information through a two-stage attention mechanism. In the first
stage, the model adaptively selects the most informative temporal segments from the history
of each related asset, focusing on those that resemble the current behavior of asseti. In the
second stage, it re-weights the related assets based on their overall relevance, emphasizing
6This is why only the firstL ∗ −1 checkpoints are used, ash S+1 j,t is not available at timet.

47
those whose past dynamics are most predictive for asseti. This retrieval structure allows the
retriever to recall and integrate inter-asset temporal patterns that are similar to the present
behavior of the target asset, thereby improving its ability to capture and forecast risk dynamics
at timet. See Figure A1 for the entire process of retriever.
Fig A1: Retriever component of ReSGA.
Notes.This figure presents the retriever component used in ReSGA. The retriever operates conditionally on
the group structureM t andH t obtained by the encoder, and compute the retrieval featureZ t, which is further
fed into the decoder.

48
A.3. Decoder.The decoder integrates the temporal featuresH t, group structureM t, and
retrieval featuresZ t to forecast the risk scoresy t. Specifically, it adopts a residual connecting
framework (Oreshkin et al., 2020), including four layers: (i) a group layer capturing shared
group-level co-behavior, (ii) a retrieval layer utilizing the retrieval features, (iii) an individual
layer modeling stock-specific behavior, and (iv) a fully connected layer producing the final risk
score forecasts.
Group Layer.As the retriever captures spatial–temporal dependencies for each asset by link-
ing its current temporal feature to the historical features of related assets, the group layer in-
stead focuses on modeling contemporaneous interactions among assets within the same group.
In other words, while the retriever aligns the present state of assetiwith the past trajectories
of its peers to recover long-term temporal relations, the group layer exploits the most recent
temporal features across assets to capture shared short-term co-movements.
Specifically, the group layer aims to capture common influences within each group based
on the most recent temporal feature{h S 1,t, . . . ,hS Nt,t}and group structureM t. For each group
Mk,t inM t, we first design a group-level feature by aggregating member features:
Gk,t = LeakyReLU

W1

 X
i∈Mk,t
γ∗ i,k,thS i,t

 +b 1

 ∈R D,
whereh S i,t is the temporal feature of assetifrom (A1),W 1 ∈R D×D andb 1 ∈R D are learnable
parameters, and LeakyReLU(·) is an element-wise activation defined as
LeakyReLU(x) =



x, x >0,
0.01x, x≤0.
This aggregation producesG k,t as a concise summary of the short-term shared dynamics within
groupM k,t.
Next, we propagate the group-level effects to individual assets through a graph attention
mechanism (Veliˇ ckovi´ c et al., 2018):
gi,t =
X
k∈Ni,t
α∗ i,k,tGk,t,withα ∗ i,k,t = exp(β∗ i,k,t)P
m∈Ni,t exp(β∗ i,m,t) , β ∗ i,k,t = Cosine(hS i,t,G k,t),

49
whereN i,t in (A6) denotes the set of group centers containing asseti. Here,β ∗ i,k,t measures
the similarity between the current temporal feature of assetiand the group-level feature of
groupk, whileα ∗ i,k,t provides normalized attention weights to indicate the relative importance
of each group to asseti.
In the final step of the graph layer, we feed the group featureg i,t into a two-headed fully
connected network to produce the forward and backward components:
egi,t = LeakyReLU(W2gi,t +b 2),
hG i,t = LeakyReLU(W3egi,t +b 3),
oG i,t = LeakyReLU(W4egi,t +b 4),
(A10)
whereW 2,W 3,W 4 ∈R D×D andb 2,b 3,b 4 ∈R D are learnable parameters. Here,o G i,t captures
the group-level information directly used for forecastingy i,t, whileh G i,t represents the portion
ofh S i,t already explained by group co-behavior. This residual design separates the group effect
from subsequent retrieval and individual layers, enhancing both model interpretability and
learning efficiency (Oreshkin et al., 2020).
Retrieval Layer.After the graph layer, the retrieval layer employs the retrieval featureZ t
defined in (A9), which captures long-term spatial–temporal dependencies through a two-stage
attention mechanism. To be specific, this retrieval layer passesZ t through a two-headed fully
connected network, mirroring the structure used in the group layer:
ezi,t = LeakyReLU(W5zi,t +b 5),
hR i,t = LeakyReLU(W6 ezi,t +b 6),
oR i,t = LeakyReLU(W7 ezi,t +b 7),
(A11)
wherez i,t is the retrieval feature of asseti(i.e.,i-th row ofZ t), andW 5,W 6,W 7 ∈R D×D
andb 5,b 6,b 7 ∈R D are learnable parameters. Here,h R i,t serves as the backward component of
retrieval layer, representing the portion ofh i,t explained by retrieved information, whileo R i,t
denotes the forward component of retrieval layer that contributes directly to forecastingy i,t.
The parameter sets (W 5,W 6,W 7) and (b 5,b 6,b 7) play analogous roles to (W 2,W 3,W 4) and
(b2,b 3,b 4) in the group layer, respectively.

50
Individual Layer.The individual layer models the idiosyncratic part of each asset after ac-
counting for the effects already captured by the group and retrieval layers. Specifically, we
define:
oI i,t = LeakyReLU(W8hI i,t +b 8),withh I i,t =h S i,t −h G i,t −h R i,t,(A12)
whereW 8 ∈R D×D andb 8 ∈R D are learnable parameters. The output (or the forward compo-
nent of individual layer)o I i,t captures asset-specific behavior unique to asseti, ensuring that the
residual temporal information unexplained by group or retrieval effects is explicitly modeled.
Fully Connected Layer.Finally, the decoder aggregates the outputs from the group, retrieval,
and individual layers through additive composition to generate the final forecasts:
Yt = [y1,t, . . . ,yNt,t] = Decoder(Ht,Z t;M t,ψ)∈R Nt×2,(A13)
where each individual forecast is given byy i,t =W 9

oG i,t +o R i,t +o I i,t  +b 9, withW 9 ∈R 2×D
andb 9 ∈R 2 as learnable parameters. The collectionψ={(W j,b j)}9 j=1 represents all trainable
parameters within the decoder.
Intuitively, this hierarchical design in (A13) allows the decoder to jointly capture group-
level co-behavior, long-term spatial-temporal dependencies, and idiosyncratic behavior within
a unified learning framework.
A.4. Summary.Accompanied with Encoder(·;ϕ) in (A5), Retriever(·;M t) in (A9), and
Decoder(·,·;M t,ψ) in (A13), we get the specification of ReSGA in (6). See Fig A2 for its entire
network architecture.
APPENDIX B: MODEL ARCHITECTURES
In this appendix, we present the details of all competing models considered in Section 2.3.
B.1. Point-Wise Models.We consider two point-wise models in (7): Linear and NN.
B.1.1.Linear.The Linear model assumesfin (7) satisfies
yi,t =f(x i,t−1;θ) =α+β ′xi,t−1,(B1)

51
Fig A2: Overall architecture of ReSGA.
Notes.This figure summarizes the end-to-end workflow of ReSGA, consisting of an encoder constructing cross-
sectional groups, a retriever modeling long-term temporal dependencies, and a decoder combining group, re-
trieval, and individual information via a residual learning framework to produce tail-risk forecasts. For illus-
tration, we setN t = 4 andK ∗ = 2. The internal mechanics of the Retriever block are detailed in Fig A1.

52
whereα∈R 2 andβ∈R P×2 are the vectors of intercepts and regression coefficients, respec-
tively. Here,θincludes all parameters inαandβ. To mitigate the potential high-dimensional
issue, we applyℓ 1-penalization onθduring training, promoting sparsity in the learned param-
eters.
B.1.2.NN.Following Gu, Kelly and Xiu (2020), the NN model applies a multi-layer fully
connected neural network as the functionfin (7):
x(l) i,t−1 = ReLU  W (l)x(l−1) i,t−1 +b (l)  ∈R D(l) ,forl= 1, . . . , L,(B2)
yi,t =f(x i,t−1;θ) =W (L+1)x(L) i,t−1 +b (L+1) ∈R 2,(B3)
wherex (l) i,t−1 denotes the output from thel-th hidden layer, withx (0) i,t−1 =x i,t−1, andD (l) is its
dimension. Here,Lis the number of hidden layers, the activation function ReLU is defined as
ReLU(z) = max(0, z),forz∈R,
the weight matrixW (l) ∈R D(l)×D(l−1) and bias vectorb (l) ∈R D(l) , forl= 1, . . . , L+ 1, are
network parameters, withD (0) =PandD (L+1) = 2, andθcontains all the parameters in
{W (l),b (l) :l= 1, . . . , L+ 1}.
From (B2), we can see that the hidden layers recursively apply linear transformations and
nonlinear activation to extract predictive features from the raw characteristics, while the final
linear projection in (B3) is almost the same as the linear model in (B1). In particular, the
dimensionalities{D (l) :l= 1, . . . , L}control the “width” of NN, while the number of hidden
layersLcontrols the “depth” of NN. Needless to say, they are crucial for the complexity of
NN (i.e., the dimensionality ofθ).
According to the geometric pyramid rule proposed by Masters (1993), an exponentially
decaying sequence of network widths helps balance computational efficiency and nonlinear
approximation capability. Specifically, this rule suggests
D(l) =  γl−1D  ,forl= 1, . . . , L,
where⌊·⌋is the floor operator, andγis a user-defined hyperparameter. Gu, Kelly and Xiu
(2020) employL= 3,D= 32, andγ= 0.5 forP= 94. Following this setup, we also fixL= 3

53
andγ= 0.5, but varyDto investigate the virtue of model complexity in tail risk forecasting.
Additionally, as in Gu, Kelly and Xiu (2020), we also apply the batch normalization technique
(Ioffe and Szegedy, 2015) to control the variability of network inputs across mini-batches. For
more technical details on fully connected neural networks, one can refer to Goodfellow, Bengio
and Courville (2016).
B.2. Temporal Models.We consider seven temporal models in (8): LANN, DLinear,
LSTM, GRU, Informer, EInformer, and DInformer.
B.2.1.LANN.The LANN model extends the NN model in Section B.1.2 by incorporating
temporal information through lagged firm characteristics. Architecturally, LANN is identical
to the NN, and is defined as
x(l) i,t−1 = ReLU  W (l)x(l−1) i,t−1 +b (l)  ∈R D(l) , l= 1, . . . , L,
yi,t =f(x i,t−1;θ) =W (L+1)x(L) i,t−1 +b (L+1) ∈R 2,
where the inputx (0) i,t−1 = vec(X i,t−1)∈R SP flattens the matrixX i,t−1 into a vector. As a
result, the input dimension of the first layer increases fromD (0) =PtoD (0) =SP, and
the corresponding weight matrices and bias vectors adjust accordingly. All remaining network
architecture and notation follow the NN model in Section B.1.2.
Intuitively, the LANN model treats all lagged characteristics as “static” covariates. It does
not model temporal dynamics explicitly and therefore ignores potential temporal dependence
structures across lags.
B.2.2.DLinear.The DLinear model first decomposes the matrixX i,t−1 into a trend com-
ponentT i,t−1 ∈R S×P and a seasonal componentS i,t−1 ∈R S×P . For the trend component, the
s-th row ofT i,t−1 is defined as
T s i,t−1 = 1 |NK(s)| X j∈NK (s) xj i,t−1 ∈R P ,fors= 1, . . . , S,(B4)
whereN K(s) ={j∈ {1, . . . , S}:|j−s| ≤ ⌊K/2⌋}is the local index set for indexs, and
xj i,t−1 ≡x i,t−1−S+j ∈R P denotes thej-th row ofX i,t−1, which also corresponds to thej-

54
th lagged characteristics in the sequence input. Then, for the seasonal component, we have
Si,t−1 =X i,t−1 −T i,t−1 ∈R S×P .(B5)
In (B4) and (B5),T i,t−1 aims to capture the slow-moving and persistent temporal patterns,
whileS i,t−1, as the residual, retains short-term fluctuations and high-frequency variations.
After decomposingX i,t−1 into interpretable trend and seasonal components, the DLinear
model aggregates these components and projects them into a vector of risk scores:
zi,t =W SSi,t−1 +W T Ti,t−1 ∈R P ,
ezi,t = ReLU (Whidzi,t +b hid)∈R D,
yi,t =g(X i,t−1;θ) =W out ezi,t +b out,
(B6)
whereW T ∈R 1×S andW S ∈R 1×S are the weight vectors that aggregate the trend and seasonal
components along the temporal dimension, respectively, the weight matricesWhid ∈R D×P and
Wout ∈R 2×D, together with the bias vectorsbhid ∈R D andb out ∈R 2, define a one-hidden-layer
neural network from the aggregated components to the vector of risk scores.
From (B4)–(B6), we can see that the DLinear model captures the dynamics of characteristics
through trend–seasonal decomposition and then applies a one-hidden-layer neural network to
exploit these components in forecasting.
B.2.3.LSTM.In the LSTM model, the temporal dynamics of the features are captured
through a hidden state vectorh s i,t ∈R D in an autoregressive manner:
zs i,t = tanh(Wzxs i,t−1 +U zhs−1 i,t +b z),
is i,t = sigmoid(Wixs i,t−1 +U ihs−1 i,t +b i),
f s i,t = sigmoid(Wf xs i,t−1 +U f hs−1 i,t +b f ),
cs i,t =f s i,t ⊙c s−1 i,t +i s i,t ⊙z s i,t,
os i,t = sigmoid(Woxs i,t−1 +U ohs−1 i,t +b o),
hs i,t =o s i,t ⊙tanh(c s i,t),
(B7)

55
fors= 1, . . . , S, wherexs i,t−1 =x i, t−1−S+s∈R P is thes-th row ofX i,t−1,W ∗ ∈R D×P ,U ∗ ∈
RD×D, andb ∗ ∈R D for∗ ∈ {z, i, f, o}are the weight matrices and bias vectors, respectively.
Here, the operator⊙denotes element-wise multiplication, while tanh(·) and sigmoid(·) are
element-wise activation functions. Following Hochreiter and Schmidhuber (1997), the initial
statesh 0 i, t−1andc 0 i, t−1are set toD-dimensional zero vectors.
In (B7), the hidden stateh s i,t serves as the key representation, summarizing the accumulated
information up to steps. The cell statec s i,t models the internal long-term memory by carrying
information across steps. Through the sigmoid function, the forget gatef s i,t ∈(0,1) D, input
gatei s i,t ∈(0,1) D, and output gateo s i,t ∈(0,1) D regulate how much past information is
discarded, how much new information is stored, and how much information is revealed to the
hidden stateh s i,t, respectively.
After the recursive extraction in (B7), the final hidden stateh S i,t is passed through a linear
transformation to obtain the risk scores:
yi,t =g(X i,t−1;θ) =W LhS i,t +b L,(B8)
whereW L ∈R 2×D andb L ∈R 2 are weight matrix and bias vector, andθcollects all parameters
within the weight matrices and bias vectors in (B7) and (B8).
B.2.4.GRU.As another widely used recurrent neural network, the GRU model simplifies
the LSTM model by decreasing the number of gates. Its autoregressive update for the hidden
state is given in (A1). Although the ReSGA model uses the full cross-sectional inputX t−1, the
GRU component itself operates independently on each asset’s temporal informationX i,t−1.
This makes the GRU, when used alone, a purely temporal model.
Then, as in the LSTM model, the GRU model passes the final hidden stateh S i,t through a
linear transformation to compute the risk scores:
yi,t =g(X i,t−1;θ) =W GhS i,t +b G,(B9)
whereW G ∈R 2×D andb G ∈R 2 are the output weight matrix and bias vector, respectively,
andθincludes all parameters within weight matrices and bias vectors in (A1) and (B9).

56
B.2.5.Informer.While the vanilla Transformer model (Vaswani et al., 2017) has achieved
remarkable success in natural language processing through the attention mechanism, several
variants have been developed for different tasks, such as the Vision Transformer (Dosovitskiy
et al., 2021) for computer vision and the Speech Transformer (Dong, Xu and Xu, 2018) for
audio recognition. In time-series forecasting, a milestone Transformer-type architecture is the
Informer model (Zhou et al., 2021), which follows the Transformer’s encoder–decoder frame-
work but replaces the standard attention mechanism with a probabilistic sparse self-attention
mechanism to handle long sequences more efficiently, making it particularly suitable for time-
series modeling.
LetX ∗ i,t−1 = [x i,t−S∗,x i,t−2, . . . ,xi,t−1]∈R S∗×P be a truncated version ofX i,t−1 withS ∗
being a constant smaller thanS. The general architecture of Informer model is defined as:
yi,t =g(X i,t−1;θ) = InfDecoder(X ∗ i,t−1,H i,t;ψ)∈R 2
withH i,t = InfEncoder(Xi,t−1;ϕ)∈R S×D, (B10)
where InfEncoder(·;ϕ) :R S×P →R S×D represents the encoder parameterized byϕ, and
InfDecoder(·,·;ψ) :R S∗×P ×R S×D →R 2 denotes the decoder that depends on the encoder
outputH i,t and its parametersψ. Here, the encoder extracts the past-aware featureH i,t
from the full historical inputX i,t−1, summarizing the underlying dynamics from the global
viewpoint; afterwards, the decoder then leverages both the learned featureH i,t and the shorter
inputX ∗ i,t−1 to predict the target vectory i,t.
Specifically, the encoder first applies an embedding layer to extract embeddings fromX i,t−1,
which are then combined as the input for subsequent layers:
H (0) i,t =E val i,t−1 +E pos i,t−1 +E temp i,t−1
= VE(Xi,t−1;ζ) + PE(X i,t−1) + TE(Xi,t−1)∈R S×D, (B11)
whereE val i,t−1,E pos i,t−1 andE temp i,t−1 are threeS×Dmatrices, referred to as the value, positional
and temporal embeddings, respectively. Meanwhile, VE(·;ζ) :R S×P →R S×D, indexed by
parametersζ, applies a one-dimensional temporal convolution to produce the value embedding,
while PE(·) :R S×P →R S×D and TE(·) :R S×P →R S×D are two parameter-free mappings to

57
provide the positional and temporal embeddings 7.
GivenH (0) i,t , a multi-layer self-attention block is employed to further capture complex tem-
poral patterns:
H (l) i,t = FFN  SelfAttn  H (l−1) i,t ;ω (l) ;δ (l) ∈R S×D,forl= 1, . . . , L,(B12)
whereLis the number of self-attention layers, andH (l) i,t denotes the output from thel-th layer.
Here, two operators are involved: SelfAttn and FFN. Particularly, SelfAttn(·;ω) :R S×D →
RS×D is the self-attention operator based on the probabilistic sparse technique 8, indexed by
parametersω (l); meanwhile, FFN(·;δ) :R S×D →R S×D denotes a row-wise feed-forward net-
work, that is, a one-hidden-layer fully connected network applied independently to each row
of the input 9, parameterized byδ.
After the recursive extraction, the output of encoder is defined as
Hi,t ≡H (L) i,t = InfEncoder(Xi,t−1;ϕ),
whereϕencompass all parameters in (B11)–(B12). The matrixH i,t is referred to as the past-
aware feature in our paper, as it summarizes the general information contained inX i,t−1.
So far, we have illustrated the architecture of encoder. Compared to the encoder, the decoder
also first applies an embedding layer to mapX ∗ i,t−1 into an aggregated feature:
F (0) i,t = VE(X ∗ i,t−1;ζ ∗) + PE(X∗ i,t−1) + TE(X∗ i,t−1)∈R S∗×D,(B13)
where VE, PE, and TE operators are consistent with those in (B11),ζ ∗ denotes the parameters
of the decoder’s embedding layer, andF (0) i,t is the resulting aggregated feature.
Next, a multi-layer cross-attention block is applied to compute the hidden states within the
decoder:
F (l) i,t = FFN  CrossAttn  F (l) i,t ,H i,t;γ (l) ;δ (l+L) ∈R S∗×D
with F
(l)
i,t = CausalAttn

F (l−1) i,t ;ω (l+L) ∈R S∗×D, l= 1, . . . , L, (B14)
7For clarity, their precise definitions are deferred to Section C.1.
8See Section C.2 for its details.
9See Section B.1.2 for its details.

58
whereF (l) i,t denotes the output from thel-th layer. Compared to the self-attention block in
(B12) for the encoder, the cross-attention block has the same depth and applies the same FFN
operator, but introduces two additional operators: CausalAttn and CrossAttn.
Specifically, CausalAttn(·;ω) :R S∗×D →R S∗×D is the causal attention operator, which is
identical to SelfAttn except that it imposes a no-forward-looking constraint, forcing the decoder
to follow a strictly autoregressive structure10. Meanwhile, CrossAttn(·,·;γ) :R S∗×D ×R S×D →
RS∗×D denotes the cross-attention operator, which functions similarly to self-attention but
also attends to the past-aware featureH i,t (i.e., the encoder’s output) rather than only its own
input. This mechanism allows the decoder to selectively integrate information from the full
historical context, aligning its input with the temporal dependencies captured by the encoder.
Lastly, to obtain the risk scores, the most up-to-date information extracted by the decoder
is fed into a linear transformation:
yi,t = InfDecoder(X ∗ i,t−1,H i,t;ψ) =W infi,t +b in,(B15)
wheref i,t ∈R D denotes the last row ofF (L) i,t , representing the latest information available for
timet,W in ∈R 2×D andb in ∈R 2 are the weight matrix and bias vector, respectively, andψ
includes all parameters involved in (B13)–(B14). Clearly, the Informer model can be regarded
as a special case of the general temporal model, withθencompassing all parameters withinϕ
andψ.
B.2.6.EInformer and DInformer.As the vanilla Informer follows the encoder–decoder
framework, recent studies have highlighted the potential of encoder-only and decoder-only
variants in time-series forecasting (Das et al., 2024; Feng, Huang and Krompass, 2024; Yao
et al., 2025). Motivated by these works, we implement two variants, the encoder-only Informer
(EInformer) and the decoder-only Informer (DInformer), for VaR and ES forecasting.
Specifically, the EInformer model consists solely of the encoder but modifies the original
10The autoregressive structure means that the feature for timesrelies only on information available up
to times, for anys= 1, . . . , S. In contrast, the encoder operates in a non-autoregressive manner, where the
feature at timescan also depend on information from future stepss+ 1, . . . , S.

59
inputX i,t−1 by appending an additional row of learnable parameters at the end:
X i,t−1 = [Xi,t−1,ν]∈R (S+1)×P ,(B16)
where X i,t−1 is the augmented input, andν∈R P is a vector of learnable parameters. This
additional vectorν, referred to as the predictive token, serves as a placeholder representing
the characteristics at next (yet unseen) time step. It allows the model to generate a forecast
without explicitly relying on a decoder. During training, the predictive token interacts with
the historical information through the self-attention mechanism, enabling the encoder to learn
how the future prediction depends on the past characteristic. In this sense, the predictive token
acts as a query that asks, “given the past, what comes next”?
Next, the augmented input X i,t−1 is passed through the encoder as in (B11)–(B12), and the
last row of the encoder output, corresponding to the predictive token, is used to compute the
risk scores:
yi,t =g(X i,t−1;θ) =W ehi,t +b e ∈R 2,(B17)
whereW e ∈R 2×D andb e ∈R 2 are the output weight matrix and bias vector, respectively.
Here, hi,t ∈R D denotes the last row of the encoder output
H i,t = [hi,t−S, . . . ,hi,t] = InfEncoder(X i,t−1;ϕ)∈R (S+1)×D ,
andθincludes all parameters inν,W e,b e, andϕ.
In contrast, the DInformer model relies solely on the decoder and is defined as
yi,t =g(X i,t−1;θ) = InfDecoder(X i,t−1;ψ)∈R 2.(B18)
Compared with the decoder in the vanilla Informer model, the DInformer usesX i,t−1 rather
thanX ∗ i,t−1 as input. Moreover, since the past-aware representationH i,t from the encoder is
absent, the cross-attention operator in (B14) is omitted.
B.3. Spatial-Temporal Models.Besides our proposed ReSGA, we consider another
spatial-temporal model in (9): SGA. The SGA model can be viewed as a simplified version of

60
the ReSGA model. It has exactly the same encoder as that in the ReSGA model, but omits
the retriever component and hence removes the retrieval layer in the decoder of ReSGA. All
remaining components, especially the mechanism for learning and utilizing dynamic group
structures, are retained. Therefore, comparing ReSGA with SGA isolates the role of the re-
trieval mechanism and highlights the additional value of incorporating long-term cross-asset
information beyond only considering contemporaneous group effects.
B.4. Econometric Models.As econometric benchmarks, we consider two univariate
models that are estimated separately for each asset using only its own historical returns. Let
ri,t denote the excess return of assetiat timet, and letv i,t ande i,t denote the corresponding
conditional VaR and ES at levelτ.
B.4.1.GAS.Following Patton, Ziegel and Chen (2019), we adopt the one-factor GAS model
by assuming that both VaR and ES are driven by a single latent factorκ i,t:
vi,t =a i exp(κi,t), e i,t =b i exp(κi,t), b i < ai <0,(B19)
with dynamics
κi,t =ω i +β iκi,t−1 + γi
bi exp(κi,t−1)
 1
τ 1{ri,t−1 ≤a i exp(κi,t−1)}r i,t−1 −b i exp(κi,t−1)

.(B20)
where (ω i, ai, bi, βi, γi) is a parameter vector. We setω i = 0 as in Patton, Ziegel and Chen
(2019) for identification, and estimate the remaining parameters by minimizing the FZ loss.
The one-factor GAS specification assumes that the time variation in VaR and ES is governed
by a common latent factorκ i,t, so that the two risk measures move proportionally over time.
The recursion forκ i,t is score-driven: Under the one-factor parameterization, the updating term
is obtained from the derivative of the FZ loss with respect toκ i,t. The parameterβ i controls
the persistence of the latent factor, while the parameterγ i determines the sensitivity of tail
risk forecasts to new return realizations. The parametersa i andb i scale the latent factor into
the corresponding VaR and ES forecasts.

61
B.4.2.GARCH.Patton, Ziegel and Chen (2019) also consider a GARCH(1,1) specification
estimated by FZ loss minimization. This model is defined as
(B21)
ri,t =σ i,tηi,t, η i,t ∼i.i.d.F η,i(0,1),
σ2 i,t =ω i +β iσ2 i,t−1 +γ ir2 i,t−1.
Under this location-scale structure,
(B22)
vi,t =a iσi,t, a i =F −1 η,i (τ),
ei,t =b iσi,t, b i =E(η i,t |η i,t ≤a i),
where (ωi, ai, bi, βi, γi) is a parameter vector,σ i,t is the conditional volatility of assetiat time
t, andη i,t is an i.i.d. innovation with distributionF η,i(0,1). As in Patton, Ziegel and Chen
(2019), we setω i = 1.
Under this GARCH specification, both VaR and ES are proportional to the conditional
volatilityσ i,t. Therefore, their time variation is fully determined by the GARCH recursion for
σi,t. The parameterβ i captures the persistence of conditional volatility, whereas the parameter
γi measures the impact of lagged squared returns on current risk. The parametersa i andb i
correspond to theτ-quantile and the associated lower-tail conditional mean of the standardized
innovationη i,t, respectively. In Patton, Ziegel and Chen (2019), this model is estimated by
minimizing the FZ loss, so that the GARCH dynamics are fitted to the joint forecasting
problem for VaR and ES rather than to the full conditional distribution of returns.
APPENDIX C: DETAILS OF OPERATORS IN THE INFORMER MODEL
C.1. Embedding Layer.As described in (B11) and (B13), the inputs to the encoder and
decoder,X i,t−1 andX ∗ i,t−1, are first processed by the embedding layer that consists of three
embedding operators, VE, PE, and TE, which generate the value, positional, and temporal
embeddings, respectively. For notational simplicity, we assume a generic input matrixX∈
RS×P , which containsPdifferent characteristics observed overSconsecutive time steps. Based
on this formulation, the details of each embedding operator are described below.

62
C.1.1.Value Embedding Operator.The value embedding operator VE applies a simple one-
dimensional convolution to the input matrixX, mapping it into an output matrixEval ∈R S×D.
The convolution employsDlearnable filters (also referred to as kernels), whereDcorresponds
to the dimensionality of the hidden state in the Informer model. Each filter is a smaller matrix
of sizeW×Pthat scans the input along the row axis. Specifically, each filter slides over the
input, computes the dot product between its weights and the corresponding input sub-vectors,
and aggregates the results to produce the convolution output.
The resulting matrixE val effectively forms a weighted average of the input among nearby
Wtime points with data-driven weights and bias. The learnable parameters of these filters
are collected inζ. Figure C3 provides a visual illustration of this one-dimensional convolution
process.
Fig C3: Illustration of the 1D convolution used for value embedding.
C.1.2.Positional Embedding Operator.The positional embedding operator PE is an essen-
tial component in Transformer-type models, as the attention mechanism itself treats the inputs
as an unordered set of numbers rather than an ordered matrix. In other words, the attention

63
mechanism does not inherently recognize that one element corresponds to a specific position
or another position, unless positional information is explicitly injected 11.
Following Vaswani et al. (2017), a fixed sinusoidal mapping is adopted to construct the
positional embedding representation, which encodes the positional information of each element
of inputX:
Epos = PE(X)∈R S×D,
where the (i, j)-th element ofE pos is defined as
epos i,j =



sin
 i−1
10000
j−1
2D

,ifjis odd,
cos
 i−1
10000
j−2
2D

,ifjis even.
By definition, the operator PE contains no learnable parameters; it depends solely on the shape
ofXand provides deterministic positional representation that helps the attention mechanism
preserve the sequential structure of the input.
C.1.3.Temporal Embedding Operator.Motivated by the positional embedding operator,
Zhou et al. (2021) introduce the temporal embedding operator TE, which transforms absolute
time stamps into representations that capture potential seasonality and tendency. To construct
the temporal embedding, we associate each row ofXwith a time stamp consisting of its month,
day, and corresponding weekday. Each of these calendar components can be represented by an
integer: For example, months are encoded from 0 (January) to 11 (December), days from 0 (1st)
to 30 (31st), and weekdays from 0 (Monday) to 6 (Sunday). Consequently, each time stamp
is represented as a three-dimensional integer vector encoding its month, day, and weekday
information.
LetM∈R S×3 denote the matrix containing these integer-encoded time stamps for allS
observations. GivenM, the temporal embedding representation is defined as
Etemp = TE(X)∈R S×D,
11See Section C.2 for a detailed discussion on this property of the attention mechanism.

64
where the (i, j)-th element ofE temp is given by
etemp i,j =



3X
k=1
sin

10mi,k exp
 4(j−1)
D

,ifjis odd,
3X
k=1
cos

10mi,k exp
 4(j−2)
D

,ifjis even,
wherem i,k denotes the (i, k)-th element ofM.
Similar to PE, TE contains no learnable parameters. It deterministically maps absolute time
stamps into continuous temporal representations, allowing the attention mechanism to better
capture seasonal patterns and potential trends inherent in the data.
C.2. Probabilistic Sparse Attention.As discussed in Section B.2.5, the Informer model
employs three types of attention operators: SelfAttn, CausalAttn, and CrossAttn. To efficiently
handle long time input, these operators are further equipped with a probabilistic sparse (Prob-
Sparse) technique, resulting in the so-called probabilistic sparse attention (Zhou et al., 2021).
The details of each attention operator are introduced below, while we assume a generic matrix
inputX∈R S×D for these attention operators for notational simplicity.
C.2.1.Self-Attention Operator.First, the inputXis linearly projected into three matrices:
the queryQ, the keyK, and the valueV, defined as
Q=XW Q ∈R S×D,K=XW K ∈R S×D,V=XW V ∈R S×D,(C1)
whereW Q,W K,W V ∈R D×D are learnable weight matrices. In the multi-head attention set-
ting withMheads, these matrices are further projected into head-specific low-dimensional
subspaces:
Q(m) =QW (m) Q ∈R S×D,K (m) =KW (m) K ∈R S×D,V (m) =V W(m) V ∈R S×D,(C2)
form= 1, . . . , M, whereW(m) Q ,W (m) K ,W (m) V ∈R D×D are the head-specific weight matrices,
andD =D/Mdenotes the dimensionality of each head-specific subspace.
Next, the ProbSparse technique is then applied independently within each head. Different
from the standard Transformer attention where each query attends to all keys, the ProbSparse

65
technique reduces complexity by sampling a subset of keys for each query and computing a
sparsity score to identify the most informative queries.
Specifically, fori= 1, . . . , S, letq(m) i ,k (m) i , andv (m) i denote thei-th rows ofQ (m),K (m),
andV (m), respectively. Moreover, letS i be a uniformly random sampled subset of{1, . . . , S}
with|S i|=⌊clogS⌋, wherecis a hyperparameter that balances computational efficiency and
approximation accuracy. The sparsity score is then defined as
γ(m) i = max j∈Si β(m) i,j − 1 |Si| X j∈Si β(m) i,j ,(C3)
whereβ (m) i,j , referred to as the attention coefficient, measures the similarity between the query
vectorq (m) i and the key vectork (m) j through their scaled inner product:
β(m) i,j = q(m)′ i k(m) j√D .
Intuitively, the sparsity scoreγ (m) i quantifies how much the maximum of similarity between
the query vectorq (m) i and its sampled key vectors{k (m) j :j∈ S i}deviates from its mean.
A larger sparsity score indicates that the query vector has a few highly similar key vectors,
implying that these key–value pairs are more informative and thus require full attention com-
putation. Conversely, a smaller sparsity score suggests that the query and key vectors exhibit
more uniform similarity, allowing the corresponding attention computation to be pruned to
reduce complexity.
To implement this idea, letI (m) denote the set of indices corresponding to the largest
⌊clogS⌋values among{γ (m) i :i= 1, . . . , S}. The output of them-th attention head is then
defined asC (m) ∈R S×D with itsi-th row satisfying
c(m) i =



SX
j=1
α(m) i,j v(m) j ,ifi∈ I (m),
1
S
SX
j=1
v(m) j ,otherwise,
(C4)

66
whereα (m) i,j denotes the normalized attention weight, defined as
α(m) i,j = SoftMax  β(m) i,j  = exp(β(m) i,j ) PS
k=1 exp

β(m) i,k
 .
Notably, by employing the sparsity score defined in (C3), only⌊clogS⌋head-specific outputs
c(m) i require full attention computation involving{α (m) i,j :j= 1, . . . , S}, while the remaining
ones are approximated by the average of all value vectors. Consequently, the computational
complexity is reduced fromO(S 2) in the standard self-attention mechanism toO(SlogS) in
the ProbSparse self-attention, providing a significant efficiency advantage for handling long
input sequences (i.e., large value ofS) in the Informer model.
Finally, the outputs from all attention heads are concatenated and linearly projected to
obtain the final self-attention outputY:
Y= SelfAttn(X;ω) =CW O ∈R S×D,withC=  C (1),C (2), . . . ,C(M)  ∈R S×D,(C5)
whereW O ∈R D×D is a learnable output projection matrix. The parameter setωincludes all
learnable weights involved in (C1), (C2), and (C5).
C.2.2.Causal Attention Operator.The causal-attention operator CausalAttn extends the
self-attention operator by imposing a no-forward-looking constraint. This restriction enforces
a strictly autoregressive structure within the attention computation. Specifically, following the
same procedure in (C1)–(C3), we obtain

q(m) i ,k (m) i ,v (m) i 	 and compute the sparsity score
γ(m) i in CausalAttn as
γ(m) i = max j∈Si β(m) i,j − 1 |Si| X j∈Si β(m) i,j ,(C6)
where the attention coefficientβ i,j is defined as before, but the sampling setS i is drawn from
{1, . . . , i}instead of{1, . . . , S}, with size⌊clogS⌋.
Similarly, let I
(m)
denote the indices of the largest⌊clogS⌋values among{ γ(m) i :i=

67
1, . . . , S}. The head-specific outputC
(m)
is then obtained row-wisely as
c(m) i =



iX
j=1
α(m) i,j v(m) j ,ifi∈ I (m) ,
1
i
iX
j=1
v(m) j ,otherwise,
(C7)
where the normalized attention weight α(m) i,j is given by
α(m) i,j = SoftMax  β(m) i,j  = exp(β(m) i,j ) Pi
k=1 exp(β(m) i,k ) .
The outputs from all attention heads are concatenated and linearly projected to produce
the causal-attention outputY:
Y= CausalAttn(X;ω) = CW O ∈R S×D,
with C=
h
C
(1)
, C
(2)
, . . . ,C
(M) i ∈R S×D, (C8)
whereW O is defined in (C5), andωincludes all learnable weights involved in (C1), (C2),
and (C8). The causal constraint guarantees that the model respects temporal order, making
it suitable for autoregressive sequence modeling.
C.2.3.Cross-Attention Operator.The cross-attention operator CrossAttn is similar to the
self-attention operator, but it requires two generic inputs,X∈R S×D andZ∈R S∗×D, where
S∗ is another constant and can be different fromS. The key distinction lies in that the key
and value matrices,KandV, are computed from the external inputZrather than from
X. This design enables the model to align and integrate information between two different
representations (e.g., between the encoder’s outputH i,t and the decoder’s hidden stateF i,t in
the Informer architecture).
Specifically, the queryQ, keyK, and valueVfor CrossAttn are defined as
Q=XW Q ∈R S×D,K=ZW K ∈R S∗×D,andV=ZW V ∈R S∗×D.

68
GivenQ,K, andV, following the same computation steps as in (C2)–(C5), the output of the
cross-attention operator is obtained as
Y= CrossAttn(X,Z) =CW O ∈R S×D.
Through this mechanism, the cross-attention operator allows the model to selectively attend
to the most relevant parts ofZwhile processingX, effectively establishing an information
bridge between different representation spaces.
APPENDIX D: IMPLEMENTATION DETAILS
D.1. Additional Missing-Value Preprocessing.As described in Section 3.1, firm char-
acteristics are rank-normalized cross-sectionally each month to reduce the influence of outliers,
and missing characteristic values are imputed using contemporaneous cross-sectional medians.
For the models under the unified learning framework, we drop stock-month observations when
their relatedr i,t are missing. For the econometric models, GAS and GARCH, which are esti-
mated separately for each asset using return histories, we remove missingr i,t observations and
concatenate the remaining non-missing observations into a valid return series.
D.2. Regularization Learning.As discussed in Section 2.3, we apply a range of deep
learning models to VaR and ES forecasting. While the deep learning models offer strong ca-
pacity and flexibility in extracting nonlinear relationship from data, they are also prone to
overfitting. In addition, their complex architectures and high-dimensional parameter spaces
may lead to unstable estimates due to sensitivity to initialization and convergence to local
optima. To address the above issues, we adopt two regularization techniques for these models.
First, a standard approach to mitigate overfitting is to partition the data into three disjoint
parts: training, validation, and testing samples, while preserving the temporal ordering. The
training sample is used for parameter estimation, the validation sample for hyperparameter
tuning and early stopping, and the testing sample exclusively for evaluating out-of-sample
performance. In this study, we apply this split within each expanding window in chronological
order. Details of the window construction are provided in Section 3.1.

69
Second, following Gu, Kelly and Xiu (2020), we adopt an ensemble learning strategy for
regularization. Model parametersθare estimated by solving the optimization problem in (5)
using the Adam algorithm (Kingma and Ba, 2015). Due to the nonlinearity of the models and
the sensitivity of Adam to initial values, the resulting parameter estimates may vary across
different initializations. To mitigate the impact of initialization, we repeat the optimization
from multiple random initializations. For each run, we estimate the parameters and obtain
forecasts dVaRi,t and cESi,t. The final forecasts are then computed as the average across these
runs (five in our implementation). This ensemble procedure reduces stochasticity caused by
random initialization and improves the stability of the predictions.
D.3. Hyperparameters.As with any deep learning model, performance depends on the
choice of hyperparameters, for which optimal selection is generally infeasible in theory. We
therefore adopt standard settings commonly used in the literature for the learning rate, batch
size, and other non-structural hyperparameters. Our main focus is on structural hyperpa-
rameters that govern model capacity, primarily the hidden-state dimensionD, the depthL
(number of layers), and, for the Informer family, the number of attention headsM. To reduce
computational costs, hyperparameters are tuned only in the first rolling window, and based on
performance on the validation sample, ensuring that no look-ahead bias is introduced. Then,
they are held fixed across subsequent windows, reflecting a realistic forecasting setting in which
frequent re-tuning is impractical and time-consuming.
Moreover, these hyperparameters are also varied to study the virtue of model complexity
discussed in Section 3.4. See Table D15 for a summary of the corresponding hyperparameter
settings for each parameter-scale tier.
APPENDIX E: STATISTICAL TESTING
In this appendix, we introduce the details of four tests used in Section 3.
E.1. DM Test.The DM test evaluates whether two competing models exhibit statistically
different predictive accuracy under a chosen loss function. Suppose we compare two forecasting
models, denotedaandb, for their ability to predict VaR i,t and ESi,t. Let

dVaR (a) i,t , cES (a) i,t  and

70
Table D15
Hyperparameter settings for different parameter sizes.
Model≈10 3 ≈10 4 ≈10 5 ≈10 6 ≈10 7
NNL= 3, D= 16L= 3, D= 64L= 3, D= 512L= 3, D= 1024L= 3, D= 5120
LANN –L= 3, D= 8L= 3, D= 64L= 3, D= 512L= 3, D= 2560
DLinearD= 16D= 64D= 1024D= 5120D= 64000
LSTML= 1, D= 4L= 1, D= 32L= 1, D= 128L= 3, D= 256L= 3, D= 800
GRUL= 1, D= 4L= 1, D= 32L= 1, D= 128L= 3, D= 256L= 3, D= 800
Informer L= 1, L= 1, L= 1, L= 1, L= 3,
D= 4, M= 2D= 8, M= 2D= 64, M= 4D= 256, M= 8D= 384, M= 8
EInformer L= 1, L= 1, L= 1, L= 1, L= 3,
D= 8, M= 2D= 16, M= 2D= 128, M= 4D= 512, M= 8D= 768, M= 8
DInformer L= 1, L= 1, L= 1, L= 1, L= 3,
D= 8, M= 2D= 16, M= 2D= 128, M= 4D= 512, M= 8D= 768, M= 8
SGAL= 1, D= 8L= 1, D= 16L= 1, D= 128L= 1, D= 512L= 2, D= 1024
ReSGAL= 1, D= 8L= 1, D= 16L= 1, D= 128L= 1, D= 512L= 2, D= 1024
Notes.Each entity reports the hyperparameter configuration used to attain the corresponding parameter-
scale tier. For the Informer family,Ldenotes the shared number of encoder and decoder layers, andMis
the number of attention heads. For SGA and ReSGA,Lrefers to the number of GRU layers in the encoder
block.

dVaR (b) i,t , cES (b) i,t  be the forecasts of (VaR i,t,ES i,t) given by modelsaandb, respectively. The
loss differential between modelsaandbat timetis defined as
dt(a, b) = 1 Nt
NtX
i=1
di,t(a, b),
withd i,t(a, b) =ℓFZ0

ri,t,

dVaR (a) i,t , cES (a) i,t  −ℓ FZ0  ri,t,  dVaR (b) i,t , cES (b) i,t  ,
whereℓ FZ0(·) is the FZ loss function defined in (2).
Since the loss differential measures the difference of predictive powers of modelsaandb,
the DM test can examine the following null hypothesisH 0 to check whether two competing

71
models exhibit statistically different predictive accuracy:
H0 :E[d t(a, b)] = 0.(E9)
To detectH 0, the DM test statistic is defined as
DM =
¯d(a, b)
bσ(a, b),
where ¯d(a, b) andbσ(a, b) are the mean and Newey–West standard error (Newey and West,
1987) ofd t(a, b) over the testing sample.
Notably, a significantly positive (or negative) DM statistic indicates that modelaperforms
worse (or better) than modelbunder the FZ loss. Under some mild conditions, the critical
value for the DM test statistic is the (1−α/2)-th quantile of standard normal distribution,
whereαis the confidence level.
E.2. MCS Test.The DM test compares models pairwise, whereas the Model Confidence
Set (MCS) test of Hansen, Lunde and Nason (2011) evaluates a collection of competing models
jointly. Starting from the full model set, the MCS procedure sequentially removes models that
are significantly dominated under the chosen loss function and returns a set of models that
cannot be statistically distinguished from the best-performing model(s).
LetM 0 denote the initial set of competing models. We use the FZ loss differentiald i,t(a, b)
defined in the DM test section to compare any two modelsa, b∈M 0. We aggregate over the
evaluation panel and define
¯d(a, b) = 1 |P| X (i,t)∈P di,t(a, b),
wherePis the set of stock-month observations in the test sample. LetD(a, b) =E[d i,t(a, b)].
Since lower loss indicates better predictive performance, the population superior set is
M∗ =  a∈M 0 :D(a, b)≤0 for allb∈M 0	 .
For any candidate setM⊆M 0, the MCS test considers the null hypothesis
H0,M :D(a, b) = 0,for alla, b∈M.

72
We use the range statistic
TM = max a,b∈M |t(a, b)|, t(a, b) =
¯d(a, b)
bσ(a, b),
wherebσ(a, b) denotes the bootstrap standard error of ¯d(a, b).
The critical value is obtained from a panel block bootstrap as in Yang et al. (2024). In
each bootstrap replication, we resample stocks with replacement and resample months using
contiguous time blocks, so that both cross-sectional heterogeneity and serial dependence in the
loss differentials are accounted for. Denote by ¯d(s)(a, b) the average loss differential computed
from thes-th bootstrap sample,s= 1, . . . , B. We estimate the bootstrap standard error by
bσ(a, b) =
"
1
B
BX
s=1
 ¯d(s)(a, b)− ¯d(a, b) 	2
#1/2
.
The bootstrap distribution of
T (s) M = max a,b∈M

 ¯d(s)(a, b)− ¯d(a, b) bσ(a, b)

is used to obtain the critical valueCV α,M.
IfT M ≤CV α,M, the null is not rejected and the current setMis retained. Otherwise, the
model with the largest standardized average loss relative to the remaining models is removed.
Specifically, the eliminated model is selected according to
eM = argmax
a∈M
¯da,·
bσa,·
, ¯da,· = 1 |M| −1 X b∈M
b̸=a
¯d(a, b),
wherebσa,· is the bootstrap standard error of ¯da,·. The procedure is repeated onM\ {eM}until
the null of equal predictive ability is no longer rejected. The final set is reported as the model
confidence set.
E.3. CC Test.The CC test aims to evaluate the validity of VaR forecasts. LetI i,t =
1

ri,t ≤ dVaRi,t

, where1(·) denotes the indicator function. Under correct specification, the

73
violation indicators{I i,t}should form an i.i.d. Bernoulli sequence with success probabilityτ.
Based on this fact, we examine the validity of VaR forecasts by checking the null hypothesis
H(v) 0,i :{I i,t}is an i.i.d. Bernoulli sequence.
Following Christoffersen (1998), letTjk denote the number of observations for whichIi,t−1 =j
andI i,t =k, withj, k∈ {0,1}. Define
T1 =T 01 +T 11, T 0 =T 00 +T 10,ˆπ 0 = T01
T00 +T 01
,ˆπ 1 = T11
T10 +T 11
,ˆπ= T01 +T 11
T ∗ ,
whereT ∗ is the total number of observations in the evaluation period. Then, the CC test jointly
assesses unconditional coverage and independence by combining the corresponding likelihood
ratio statistics:
LRcc = LRuc + LRind,
where
LRind =−2 log
 (1−ˆπ)T00+T10 ˆπT01+T11
(1−ˆπ0)T00 ˆπT01 0 (1−ˆπ1)T10 ˆπT11 1

and
LRuc =−2 log
 (1−τ) T0τ T1
(1−ˆπ)T0 ˆπT1

,
Under the null hypothesisH (v) 0,i , LR cc is asymptotically distributed asχ 2(2). Therefore, we
rejectH (v) 0,i when the value of LR cc is larger than theα-th upper quantile ofχ 2(2).
E.4. AESR test.Following Bayer and Dimitriadis (2022), we assess the validity of ES
forecasts via the AESR test, which is based on two regressions, linking observed returns to the
corresponding VaR and ES forecasts. Specifically, these regressions are defined as
ri,t =β i,1 +β i,2 dVaRi,t +u (q) i,t , r i,t =γ i,1 +γ i,2 cESi,t +u (e) i,t ,
whereβ i,1, βi,2, γi,1, andγ i,2 are unknown coefficients, andu (q) i,t andu (e) i,t are model errors. The
AESR test makes use of the fact that, conditional on the information setF t−1, theτ-th
conditional VaR ofu (q) i,t and theτ-th conditional ES ofu (e) i,t are equal to zero almost surely.

74
Consequently, for each asseti, the AESR test assesses the adequacy of cESi,t by testing the
null hypotheses:
H(e) i,0 : (γi,1, γi,2)′ = (0,1) ′.
Intuitively, underH (e) i,0 , the ES forecasts are correctly specified in the sense that cESi,t behaves
close to the conditional ES ofr i,t given the information set. Hence, for each model, rejection
ofH (e) i,0 at the significance levelαindicates that the corresponding ES forecasts fail to capture
the tail distribution of returns, suggesting deficiencies in the model’s calibration.
Notably, because ES is not elicitable on its own,γ i,1 andγ i,2 cannot be estimated separately.
Instead, the coefficients (βi,1, βi,2, γi,1, γi,2) are estimated jointly by minimizing the FZ loss. Let
bγi = (bγi,1,bγi,2)′ denote the resulting estimates, and let bΣγ,i be a consistent estimator of the
asymptotic covariance matrix of bγi. Then, we can define a Wald-type test statistic:
W (e) i = bγi −(0,1) ′⊤ bΣ−1 γ,i bγi −(0,1) ′ ,
which asymptotically follows aχ 2(2) distribution underH (e) i,0 . The null hypothesis is rejected
whenW (e) i exceeds the corresponding critical value. Like CC test, the AESR test is applied to
each assetiseparately.
