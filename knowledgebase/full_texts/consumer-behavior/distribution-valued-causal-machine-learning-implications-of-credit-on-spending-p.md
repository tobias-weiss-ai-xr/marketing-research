---
title: 'Distribution-valued Causal Machine Learning: Implications of Credit on Spending Patterns'
url: https://arxiv.org/abs/2509.03063
category: consumer-behavior
subcategory: empirical
date: 2025-09
venue: ''
authors:
- Cheuk Hang Leung
- Yijun Li
- Qi Wu
source: arxiv
pdf_url: https://arxiv.org/pdf/2509.03063
pages: 64
chars: 118533
fetched_at: '2026-11-08T13:09:19+00:00'
kb_version: 1
---

# Distribution-valued Causal Machine Learning: Implications of Credit on Spending Patterns

Distribution-valued Causal Machine Learning: Implications of
Credit on Spending Patterns
Cheuk Hang LEUNGa, Yijun LIa, Qi WUa
aDepartment of Data Science, City University of Hong Kong
This version: August 18, 2025
Abstract
Fintech lending has become a central mechanism through which digital platforms stimulate con-
sumption, offering dynamic, personalized credit limits that directly shape the purchasing power of
consumers. Although prior research shows that higher limits increase average spending, scalar-
based outcomes obscure the heterogeneous distributional nature of consumer responses. This
paper addresses this gap by proposing a new causal inference framework that estimates how con-
tinuous changes in the credit limit a ffect the entire distribution of consumer spending. We for-
malize distributional causal effects within the Wasserstein space and introduce a robust Distribu-
tional Double Machine Learning estimator, supported by asymptotic theory to ensure consistency
and validity. To implement this estimator, we design a deep learning architecture comprising
two components: a Neural Functional Regression Net to capture complex, nonlinear relation-
ships between treatments, covariates, and distributional outcomes, and a Conditional Normalizing
Flow Net to estimate generalized propensity scores under continuous treatment. Numerical ex-
periments demonstrate that the proposed estimator accurately recovers distributional e ffects in a
range of data-generating scenarios. Applying our framework to transaction-level data from a major
BigTech platform, we find that increased credit limits primarily shift consumers towards higher-
value purchases rather than uniformly increasing spending, offering new insights for personalized
marketing strategies and digital consumer finance.
Keywords: consumer credit, spending distributions, causal inference, double machine learning,
deep learning.
arXiv:2509.03063v1  [econ.GN]  3 Sep 2025

1. Introduction
In recent years, fintech credit has emerged as a core component of leading digital retail ecosys-
tems such as Amazon, Alibaba, and JD Digit. These BigTech firms weave short-term, revolving
credit products directly into the checkout process, providing consumers with immediate access to
liquidity that traditionally required engagement with external financial institutions. By collapsing
the boundary between payment and borrowing, embedded credit effectively expands the effective
budgets of consumers while o ffering retailers a powerful tool to simulate real-time demand (Li
et al., 2021). As of 2020, BigTech lenders had extended more than $700 billion in credit world-
wide (Cornelli et al., 2023), underscoring their increasing influence over both retail consumption
and global credit markets.
At the core of credit services is the assignment of credit limits - a mechanism that directly
controls the liquidity available to consumers at purchase. These limits are dynamically personal-
ized using proprietary scoring algorithms that leverage demographic, historical transactional and
financial data collected across the platform. Rather than serving merely as a passive financing
constraint, the credit limit functions as an active instrument that shapes consumption behavior
at the point of decision and directly influences not only the likelihood of purchase, but also the
magnitude and composition of spending (Li et al., 2024).
Understanding how variations in assigned credit limits influence consumer spending behaviors
is fundamentally important, as platforms can identify optimal credit levels that stimulate consump-
tion without inducing excessive risk. This insight enables BigTech firms to strategically allocate
credit to maximize transaction volume and revenue. However, determining these optimal credit
levels involves inherently counterfactual scenarios, as the outcome of an alternative credit limit for
a given consumer is always unobservable. This challenge is further compounded by the presence
of confounding factors that simultaneously influence credit assignment decisions and consumer
spending behaviors, thus obscuring the underlying causal relationship and complicating efforts to
isolate the true effect of credit variation (Spirtes, 2010).
A growing body of empirical research has established that increases in credit availability—whether
through higher card limits, relaxed lending terms, or digital financing options—tend to elevate ag-
2

gregate consumer spending (Gross and Souleles, 2002, Soman and Cheema, 2002, Agarwal et al.,
2007, Wilcox et al., 2011, Aydin, 2022). These studies provide solid evidence that many con-
sumers are limited by liquidity and respond to expanded credit access with elevated consumption.
However, these studies have largely focused only on average treatment effects (ATE), such as total
or mean expenditures, and offer limited insight into how consumers reallocate their spending and
reshape their behaviors in response to incremental credit. The fundamental reason lies in the fact
that these studies rely on classical causal inference frameworks that treat the outcome variable as
a scalar quantity. In this paradigm, spending is typically aggregated by summing or averaging the
monetary value of all transaction orders, thereby reducing complex behavioral profiles to single
summary statistics. Although this approach simplifies identification and estimation, it inherently
obscures heterogeneity in how credit is allocated across transactions.
To illustrate, consider two consumers, A and B in Figure 1. Suppose that both start with iden-
tical credit limits of $500 and exhibit similar average spending levels around $30. Consumer A
makes moderately priced purchases—$33, $28, $29—and upon receiving a higher credit limit of
$1,000, they uniformly increase spending to $53, $48, and $49. In contrast, Consumer B initially
spends $33, $28, $29, and after the limit increase, allocates the additional credit almost entirely
to high-end items, spending $33, $28, $89. Although both groups exhibit the same post-treatment
average of $50, their behavioral responses are markedly di fferent: the spending distribution of
consumer A shows a shift to the right, while the spending distribution of consumer B exhibits a
heavier right tail and an increase in skewness. Scalar-based approaches fail to capture such dis-
tributional dynamics, thus limiting their capacity to inform strategic credit design and behavioral
targeting in practice.
To address this methodological gap, this paper introduces a distribution-valued causal infer-
ence framework for settings where the outcome of interest is a distribution rather than a scalar.
Specifically, unlike scalar-based causal inference that operates in Euclidean space, we estimate
the distributional average treatment effects in the Wasserstein space (Panaretos and Zemel, 2020),
which enables robust aggregation and comparison of distributions taking into account the geomet-
ric structure (Verdinelli and Wasserman, 2019, Panaretos and Zemel, 2019). Within this frame-
work, we define two causal quantities: the Distributional Average Potential Outcome (Dist-APO)
3

Consumer
A
Consumer
B
Credit Limits = $500
30 50
30 50
After increasing credit
After increasing credit
𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆
𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆
𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆
𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆30
30
Credit Limits = $1,000
Fig. 1. An illustration example of the shift of spending distribution due to the treatment effect. Each point represents
the expenditure of an individual order, and all the spending collectively constitutes a spending distribution for a
consumer.
and the Distributional Average Treatment Effect (Dist-ATE), which serve as distributional analogs
of the classical potential outcome and the average treatment e ffect. To estimate the Dist-APO,
we develop a Distributional Double Machine Learning (Dist-DML) estimator grounded in (Cher-
nozhukov et al., 2018). To implement our estimators and estimate key nuisance parameters, we
design a unified deep learning architecture comprising two core components. The Neural Func-
tional Regression Net (NFR Net) generalizes classical functional regression to capture nonlinear
mappings from covariates and treatment levels to outcome distributions. In parallel, the Condi-
tional Normalizing Flow Net (CNF Net) extends normalizing flow models to estimate generalized
propensity scores under a continuous treatment regime.
We validate our methodology through extensive simulation studies and a real-world applica-
tion using proprietary data from a major E-commerce platform. In simulations, the Dist-DML
estimator consistently outperforms benchmark methods, including Distributional Direct Regres-
sion (Dist-DR) and Distributional Inverse Propensity Weighting (Dist-IPW), by achieving lower
bias and variance in recovering the true Dist-APO. Empirically, we validate our approach using
data from a major digital retail platform, exploring how incremental adjustments in fintech credit
influence consumer spending distributions. We find that increases in credit limits not only raise
total spending, but also significantly reshape the distribution of expenditures, especially at higher
quantiles, confirming that consumers tend to allocate additional fintech credit towards more expen-
4

sive, discretionary purchases. These insights have strategic implications for online retail platforms
and regulators in optimizing credit offerings, improving risk management strategies, and designing
marketing strategies.
This study makes three contributions that advance both the causal inference methodology and
the credit management practice of a platform:
• We introduce a new formalization of causal e ffects where the outcome is extended from a
scalar to a distributional quantity, and the treatment variable is generalized from discrete to
continuous. To capture the effects of such treatment variation, we define Dist-APO and Dist-
ATE under the Wasserstein metric, which preserves the underlying geometry of outcome
distributions. We further develop a robust and consistent estimator, Dist-DML, and establish
its large-sample properties, providing a rigorous foundation for counterfactual analysis.
• We develop an end-to-end implementation centered on the proposed estimator to address
high-dimensional confounding and continuous treatment spaces. The architecture combines
a NFR Net, which maps covariates and treatment levels to full outcome distributions, with a
CNF Net to estimate the generalized propensity score. This integrated design enables flexi-
ble and consistent estimation of distributional treatment e ffects in complex data-generating
processes.
• We apply the proposed framework to a real-world transaction-level dataset collected from
a major digital platform to uncover how changes in credit limits causally alter the shape of
consumer spending distributions. Our results reveal that expanded credit access not only
increases overall spending but disproportionately a ffects upper expenditure quantiles, sug-
gesting that additional liquidity primarily induces consumers to shift toward higher-value
purchases. These findings provide new operational insights for personalized credit alloca-
tion, targeted promotions, and platform-level financial decision making.
5

2. Literature Review
2.1. Credit Availability and Consumer Spending
Classical consumption theory, grounded in the life cycle and permanent income hypotheses,
posits that rational consumers smooth consumption over time by allocating resources in accor-
dance with expected lifetime income (Modigliani and Brumberg, 1954, Hall, 1978). Within this
framework, credit services merely facilitate intertemporal reallocation, allowing consumers to bor-
row against future income during low-income periods and repay during high-income periods, with-
out affecting aggregate lifetime consumption. Consequently, temporary changes in credit access
should not influence total spending, unless they reflect changes in lifetime resources.
However, a substantial body of empirical evidence challenges this neutrality by demonstrating
that consumption is often excessively sensitive to credit conditions (Bacchetta and Gerlach, 1997,
Breza and Kinnan, 2021). These findings suggest that many consumers face binding liquidity
constraints or behavioral deviations from complete rationality. For example, financial deregulation
and expansions of the credit market have been linked to substantial consumption booms across
countries (Jappelli and Pagano, 1989), while credit contractions have been observed to suppress
consumption even when income remains unchanged. These patterns indicate that many people
rely on credit not only for intertemporal smoothing but also as a binding component of current
spending capacity.
A key mechanism through which credit a ffects spending is the mode of payment. Traditional
theory implies that, conditional on budget constraints, the mode of payment should not alter spend-
ing. However, behavioral economics has shown that credit cards tend to increase spending by
attenuating the psychological salience of payment. The foundational experiments conducted by
Feinberg (1986) and the supporting studies given in (Hirschman, 1979, Prelec and Simester, 2001,
Raghubir and Srivastava, 2008) demonstrate that consumers spend more when using credit cards
instead of cash, since the intangible nature of card-based payment weakens the “pain of pay-
ing”. This decoupling of payment from consumption reduces transaction aversion and inflates
willingness-to-pay.
Beyond the payment medium, credit limits serve as another channel to influence consumer
6

behavior. Empirical studies have discovered that increasing credit limits tends to increase spend-
ing, especially for consumers who were close to their borrowing restrictions (Gross and Souleles,
2002). Similarly, Aydin (2022) provides experimental evidence that newly available credit leads
to sharp and sustained increases in expenditure. One possible explanation, o ffered by Soman and
Cheema (2002), is that assigned credit ceilings act as implicit endorsements of financial stand-
ing, serving as psychological signals that justify greater consumption. This e ffect is particularly
salient for financially inexperienced individuals who may interpret a generous limit as a reflection
of future income potential.
Underlying the empirical insights above is an emphasis on credible identification strategies
to recover causal e ffects. Since credit assignment and usage are often endogenous, researchers
have sought exogenous variation to isolate the impact of credit access. Field experiments and
Randomized Controlled Trials (RCTs) are always the gold standard for identifying causal e ffects
in this domain (Aydin, 2022, Banerjee et al., 2015). When experiments are infeasible, scholars
have leveraged natural experiments, di fference-in-differences designs (Breza and Kinnan, 2021,
Gross and Souleles, 2002), and instrumental variables (Agarwal et al., 2020, Li et al., 2021).
Although effective, these strategies often face constraints related to data access, implementation
costs, and ethical considerations. As a result, there is growing interest in methods that enable
causal inference using observational data, particularly in complex and high-dimensional treatment
settings.
2.2. Causal Machine Learning
Credible causal inference from observational data is challenging because each subject reveals
only the outcome under the treatment actually received. The potential outcomes of alternative
treatments remain unobserved. In addition, treatment assignment is usually correlated with ob-
served and unobserved covariates, generating a confounding that biases naive comparisons of
outcomes between various treatment levels (Hernán and Robins, 2010).
In response to the challenges inherent in deriving causal inferences from observational data,
a variety of methodologies have been developed. One such approach involves constructing the
estimators for the target causal quantities while harnessing the capabilities of advanced machine
7

learning techniques to estimate the nuisance parameters within these estimators. The simplest
method, called the Direct Regression (DR) approach, regresses outcomes with treatments and
covariates, but inherits bias when treatment assignment is endogenous. The inverse propensity
weighting (IPW) method corrects this bias by constructing a pseudo-population and re-weighting
observations with inverse generalized propensity scores (Rosenbaum and Rubin, 1983, Hirano
et al., 2003). However, using estimated propensity scores, especially when they are extreme, can
lead to estimates with high variances. Double machine learning (DML) estimators mitigate bias
and variance by orthogonalizing the estimating equations with respect to nuisance parameter error
and using sample splitting to prevent overfitting (Chernozhukov et al., 2018, Farrell, 2015). Subse-
quent work has extended DML to discrete treatments (Huang et al., 2021), continuous treatments
(Su et al., 2019), dynamic treatments (Bodory et al., 2022), and combined treatments (Ye et al.,
2025), making it a versatile tool for high-dimensional causal analysis.
Despite this progress, most existing approaches for causal inference typically concentrate on
estimating the causal quantities, such as average treatment effect or quantile treatment effect. Their
key assumption is that, given the treatment, the realization of the outcome variables for each in-
dividual is a scalar point drawing from the same potential outcome distribution. Recent works by
Kennedy et al. (2023) and Martinez-Taboada and Kennedy (2024) have shifted the focus toward
directly estimating potential outcome distributions, rather than solely concentrating on counter-
factual scalar values like means or specific quantiles. However, their approaches are also based
on the assumption that all individuals share an identical distribution of potential outcomes when
subjected to the same treatment.
In many real-world applications, the outcome for each individual is not a single realization but
a distribution formed from multiple observations, such as the distribution of transaction amounts
for a given consumer. This naturally connects to ideas from functional data analysis (Cai et al.,
2022, Chen et al., 2016), where the outcome is treated as a continuous object rather than a scalar.
Although early approaches have attempted to model such distributional responses in Euclidean
space (Ecker et al., 2024), it is now understood that Euclidean geometry may distort probabilistic
properties when applied to distributional data (Panaretos and Zemel, 2019, Verdinelli and Wasser-
man, 2019). Alternative formulations that embed outcomes in non-Euclidean spaces, such as the
8

Wasserstein space, provide a more principled way to capture variability across distributions. How-
ever, much of the existing work in this area has focused on discrete or binary treatments, limiting
its relevance to applications involving continuous policy variables, such as credit limits in fintech
platforms.
In numerous real-world scenarios, the outcome of an individual can be observed multiple
times, collectively forming a unique distribution, such as the distribution of transaction amounts
for a given consumer. This naturally connects to ideas from functional data analysis, which delves
into data that continuously vary in a domain (Cai et al., 2022, Chen et al., 2016). Based on this
concept, Ecker et al. (2024) proposed a causal framework to analyze the impact of treatment on
functional outcomes. However, their approaches are grounded in Euclidean space, in which the
random structure of the distributional outcome can be destroyed (Verdinelli and Wasserman, 2019,
Panaretos and Zemel, 2019, Lin et al., 2023).
3. Preliminary Backgrounds
3.1. Notations
We denote the treatment variable byA, a deterministic scalar variable taking continuous values
in a subsetA of R; the outcome variable by Y such that the realization for each individual is a
distribution function; and the confounding variable /confounder by X = [X1,··· , Xd]∈X⊆ Rd
that exerts influence on both treatment A and outcome Y simultaneously. We assume that there
exist N independent units (Xi, Ai, Yi)N i=1. For each unit, the realizations of X and A, together with
a collection of observed values that can be characterized as the distributional outcome under the
realized treatment, are observed. We also denoteY(a) as the potential outcome variable associated
with the specific treatment level a. When a unit actually receives the treatment a, Y equals Y(a),
and we call Y(a) the factual outcome; otherwise, Y(a) is termed the counterfactual outcome and
remains unobserved. Finally, we adopt a hat symbol to denote estimators (e.g., ˆ γ represents an
estimator of the quantityγ).
9

3.2. Causal Assumptions
Rooted in the potential outcome framework Rubin (1978, 2005), our study is based on four
key assumptions to identify causal quantities from observed data.
Assumption 1 (SUTV A). It contains two parts:
1. The potential outcome of a individual is not influenced by the treatment assignment to other
individuals .
2. For each unit, there are no different forms of treatment levels that lead to different potential
outcomes.
Assumption 2 (Consistency). If A = a, then Y = Y(a).
Assumption 3 (Ignorability). A⊥ ⊥Y(a)| X for any a∈ R.
Assumption 4 (Overlap). Denote p (a|x) as the density of A = a conditioning on X = x and
p(a, x) as the joint density function of the variables (A, X) at (a, x). There exists c > 0 such that
inf
a
ess inf
x
p(a|x)≥ c. Furthermore, we assume that p(a, x) is a three-times differentiable function
w.r.t. a with all three derivatives uniformly bounded over the sample space.
We further explain the essentialness of the four assumptions in Appendix Appendix A.
3.3. Wasserstein Space
We define the vector spaceWp(I) ( p≥ 1) that comprises cumulative distribution functions
(CDFs) defined onI that satisfy the condition:
Wp(I) =

λ is a CDF onI⊂ R|
Z
I
tpdλ(t)<∞  .
To quantify the distance between two CDFs, a straightforward option for this purpose is the Eu-
clidean p-measure. Under this measure, the distance between two CDFs λ1 andλ2 is calculated
as the point-wise di fferences of the two CDFs in the domain I. Mathematically, the Euclidean
p-measure is defined as follows:
Z
I
|λ1(t)−λ2(t)|pdt  1 p .
10

Fig. 2. The Euclidean mean and Wasserstein mean (Barycenter) of 5 distributions.
However, the Euclidean p-measure, while simple, is not ideally suited to characterize the distance
between two CDFs. One of its primary limitations is the manner in which it aggregates the values
of various distributions. Using the Euclidean metric involves averaging the values of the distribu-
tions point by point. This process can potentially disrupt the structural properties of the resultant
distribution, leading to a distortion or loss of its essential characteristics. To illustrate, consider
the five normal distributions in the top figure of Figure 2. A Euclidean average of these curves
produces the green density in the bottom figure of Figure 2 where the result is multimodal and no
longer Gaussian.
To overcome the limitations of Euclidean p-measure, we turn to the p-Wasserstein metric
(Villani, 2021, Panaretos and Zemel, 2019, Feyeux et al., 2018), which is formally defined as
Definition 1. Given two random variables V 1 and V2, let the marginal CDFs of V 1 and V2 beλ1
andλ2 that are defined inI. In addition, let Λ be the set that contains all the joint densities of V1
and V2. Suppose that the cost functionγ(·,·) : R× R→ R adheres to the standard metric axioms:
positivity, symmetry, and triangle inequality. The p-Wasserstein metric is given asDp(λ1,λ 2) such
that
Dp(λ1,λ 2) =

inf
˜λ∈Λ
Z
I×I
γ(s, t)pd ˜λ(s, t)  1 p . (1)
11

Here, γ(·,·) represents the cost associated with transporting a point mass from position s in the
distributionλ1 to position t in the distributionλ2. Thus, the integral
R
I×Iγ(s, t)pd ˜λ(s, t) quantifies
the total cost incurred in transporting the mass from λ1 to λ2. Consequently, Dp(λ1,λ 2) is inter-
preted as the minimum total cost achievable among all possible joint distributions of (λ1,λ 2). We
present a detailed illustration in the Appendix Appendix B to further distinguish the Wasserstein
and Euclidean measures.
The vector spaceWp(I) equipped with the metric Dp(·,·) forms the p-Wasserstein space (for-
mally represented as (Wp(I), Dp(·,·))). Since the function γ(s, t) in Definition 1 adheres to the
metric axioms, the distance measure Dp(·,·) also satisfies the metric axioms, confirming that the
p-Wasserstein space is a metric space. In the sequel, we specifically focus on the case wherep = 2
andγ(s, t) =|s− t|. This choice preserves the intrinsic geometry of the probability distributions
and, therefore, produces a barycenter that retains the Gaussian shape of the original samples, as
illustrated by the red curve in Figure 2.
4. Distributional Outcome Causal Inference Framework
4.1. Dist-APO and Dist-ATE
In scenarios where the outcome is a scalar, given the treatment A = a, the realization of the
outcome variables for each individual is a scalar point drawn from the same potential outcome dis-
tribution. For example, as shown in the top figure of Figure 3, the blue and green points represent
the realizations of the ith ( jth) unit, respectively. Under this assumption, various causal quantities
have been developed and explored. For example, the ATE between treatment a and a′ (a , a′),
denoted as θ(aa′), measures the di fference between the mean of the potential outcome Y( a) and
the mean of the potential outcome Y(a′). Mathematically,θ(aa′) is defined with
θ(aa′) = EPa[Y(a)]− EPa′ [Y(a′)]. (2)
Here, EPa[Y(a)] is the expectation of Y(a) in the probability measure Pa, representing the average
potential outcome when all individuals receive treatment a. Similarly to ATE, but designed for
the distributional outcomes Y(a) and Y(a′) of different treatments, we focus on a quantity termed
Dist-ATE, which captures the causal e ffects across all quantiles of the distributional outcomes
12

QTE
ℚℙ𝑎𝑎′ [𝛼𝛼, 𝑌𝑌(𝐴𝐴 = 𝑎𝑎′)]
𝑗𝑗th unit𝑖𝑖th unit
𝑝𝑝𝑌𝑌(𝑎𝑎′)(�)
𝔼𝔼ℙ𝑎𝑎′ 𝑌𝑌(𝐴𝐴 = 𝑎𝑎′)
𝒫𝒫𝒴𝒴 𝑎𝑎′ (�)
ℚℙ𝑎𝑎 [𝛼𝛼, 𝑌𝑌 𝐴𝐴 = 𝑎𝑎 ]
𝑖𝑖th unit 𝑗𝑗th unit
𝑝𝑝𝑌𝑌(𝑎𝑎)(�)
𝔼𝔼ℙ𝑎𝑎 [𝑌𝑌(𝐴𝐴 = 𝑎𝑎)]
𝒫𝒫𝒴𝒴 𝑎𝑎 (�)
Distributional Average Treatment Effect:
Θ(𝑎𝑎) � − Θ(𝑎𝑎′) � , Θ(𝑎𝑎) � = ∫−∞ 𝑥𝑥 𝜙𝜙𝑎𝑎 𝑢𝑢 𝑑𝑑𝑢𝑢
ATE
𝜙𝜙𝑎𝑎′ (𝑥𝑥)
𝜙𝜙𝑎𝑎(𝑥𝑥)
𝛼𝛼
𝛼𝛼
Average Treatment Effect (ATE):
𝔼𝔼ℙ𝑎𝑎 𝑌𝑌(𝐴𝐴 = 𝑎𝑎) − 𝔼𝔼ℙ𝑎𝑎′ 𝑌𝑌 𝐴𝐴 = 𝑎𝑎′
Quantile Treatment Effect (QTE):
ℚℙ𝑎𝑎 [𝛼𝛼, 𝑌𝑌 𝐴𝐴 = 𝑎𝑎 ] − ℚℙ𝑎𝑎′ [𝛼𝛼, 𝑌𝑌 𝐴𝐴 = 𝑎𝑎′ ]
Fig. 3. Comparisons of ATE, QTE, and the Dist-ATE.
due to di fferent treatments, providing a comprehensive understanding of the treatment-outcome
relationships. We require the definition of the distributional average potential outcome (Dist-APO)
given in Definition 2.
Definition 2. The distributional average potential outcome is denoted asΘ(a)(·), where Θ(a)(·) =
¯Y−1(a)(·) and
¯Y(a)(·) := arg min
v∈W2(I)
EPa
D2(Y(a), v)2. (3)
Unlike scalar outcomes, the realization of Y(a) in the context of distributional outcomes con-
sists of CDFs that are represented as points within the Wasserstein spaceW2(I). This space (see
Figure 4) forms the basis of the probability space ( W2(I),FW2(I),Pa), whereW2(I) serves as
the outcome space,FW2(I) is the associated σ-algebra, and the probability measurePa integrates
to one over this space. The expectation EPa[·] is taken over the distributions rather than over the
standard real-valued variables and calculates the averaged squared Wasserstein distance between
every possible distribution ofY(a) (e.g., y1(a),··· , y10(a) in Figure 4) and an arbitrary distribution
and an arbitrary distribution v inW2(I). Consequently, ¯Y(a)(·) is specifically a CDF located in a
position withinW2(I) that minimizes this average squared distance. ¯Y(a)(·) is also known as the
13

𝓎𝓎1(𝑎𝑎)
𝓎𝓎2(𝑎𝑎)
𝓎𝓎3(𝑎𝑎)
𝓎𝓎4(𝑎𝑎)
𝓎𝓎5(𝑎𝑎)
𝓎𝓎6(𝑎𝑎)
𝓎𝓎7(𝑎𝑎)
𝓎𝓎8(𝑎𝑎)
𝓎𝓎9(𝑎𝑎)
𝓎𝓎10(𝑎𝑎)
�𝒴𝒴 (𝑎𝑎)
Fig. 4. The illustration of Wasserstein mean in W2(I) space. Each cross is a realization of Y(a). ¯Y(a) is the
Wasserstein mean that minimizes the averaged squared distance to every realized distribution ofY(a).
Wasserstein mean or the Wasserstein barycenter, and its inverse, denoted ¯Y−1(a)(·) (or Θ(a)(·)),
serves as the quantile function of ¯Y(a)(·). In the sequel, we will omit (·) for simplicity, and thus
¯Y(a)(·), Θ(a)(·) will be ¯Y(a), Θ(a).
To provide further clarity on the expected valueEPa[D2(Y(a), v)2], consider a specific example
in which the treatment level a is set to 1 2, and the random variable Y(a) or Y( 1 2) is defined such
that each of its realizations is a normal distribution N(u, 1), where the mean u is drawn from
a uniform distribution U([ 1 2, 3 2]). In this setting, individual realizations of Y( 1 2) might be, for
example,N(˜u1 = 3 4, 1) orN(˜u2 = 6 5, 1), where ˜u1 and ˜u2 are numbers randomly chosen from
U([ 1 2, 3 2]). As a result, given v∈W 2(I), then
EPa[D2(Y(a), v)2]|a= 1 2 =
Z 3
2
1
2
D2
Z x
−∞
1√
2π
e− (z−u)2 2 dz, v(x)2du.
With the definition of Dist-APO, we can define the Dist-ATE between two treatments in Defi-
nition 3.
Definition 3. The distributional average treatment e ffect between treatments a and a ′, denoted
Θ(aa′), is defined as the difference between Θ(a) and Θ(a′). Mathematically, we have
Θ(aa′) B Θ(a)− Θ(a′). (4)
To improve clarity, we summarize the comparison notations and definitions between the distribu-
tional outcome and the scalar outcome frameworks in Table 1 and provide a detailed comparison
in Appendix Appendix C.
14

Table 1 Comparisons between framework of distributional outcome and scalar outcome.
Distributional Outcome Scalar Outcome
Treatment/Covariates variable (with realization) A/X (a/x) A/X (a/x)
Outcome/Potential outcome variable (with realization) Y/Y(a) (y/y(a)) Y /Y(a) (y/y(a))
Ambient space of outcome variable (Ω) W2(I) R
Probability measure P(ω),Pa(ω), whereω∈ Ω P(ω), Pa(ω), whereω∈ Ω
Metric Wasserstein Euclidean
Realization of outcome variable distribution scalar
Average Potential Outcome Θ(a)∈W 2 θ(a)∈ R
Average Treatment Effect Θ(aa′) = Θ(a)− Θ(a′)∈W 2 θ(aa′) =θ(a)−θ(a′)∈ R
4.2. Dist-DML form
As established in the previous section, the calculation of ¯Y(a) poses a significant challenge,
as it requires solving an optimization problem within the Wasserstein space, that is, ¯Y(a) =
arg min
v∈W2(I)
EPa
D2(Y(a), v)2. This process can be particularly demanding in terms of computa-
tional resources, especially when dealing with high-dimensional datasets or large sample sizes. To
enhance the efficiency of the calculation process, it is imperative to circumvent the direct optimiza-
tion step. This goal is achieved through Proposition 1 that o ffers a methodological advancement
by simplifying the computation of Θ(a).
Proposition 1. The quantity Θ(a) can be reduced as EPa
Y(a)−1.
The detailed proof of Proposition 1 is deferred to Appendix Appendix F.1. This proposition
elucidates that the Dist-APO Θ(a) can be conceptualized as the average of all quantile functions
corresponding to the population entirely subjected to treatment a. However, directly estimating
this quantity from the observed data poses another significant challenge. This di fficulty arises
because, for each individual unit, we can only observe and characterize the distribution of out-
comes under a specific treatment that the individual actually received. It remains infeasible to
directly characterize the distributions of the outcomes that would have occurred under alternative
treatments.
To overcome this limitation, we concentrate on exploring alternative forms ofΘ(a) that facili-
tate the practical estimation of Dist-APO using the observed data. Consequently, we introduce the
Dist-DML form for this purpose (apart from the Dist-DML form, there are two other forms: the
Dist-DR form and the Dist-IPW form. These two forms are treated as the benchmark approaches
15

and are deferred to the Appendix Appendix D). The Dist-DML form is developed from the Double
Machine Learning Theorem as depicted in Chernozhukov et al. (2018). The theorem provides a
powerful framework that combines the benefits of both the Dist-DR form and the Dist-IPW form.
The specific expression of EPa[Y(a)−1] based on the DML approach is summarized in Proposition
2.
Proposition 2. Suppose Assumptions 1 - 4 hold, we have
Θ(a) = E(P(A),P(X),P)

m(a; X) + δ(A− a) p(a|X) [Y−1− m(a; X)]  . (5)
The proof is elaborated in the Appendix Appendix F.3. Here, m(a; X) = EP|P(X)[Y−1|A = a, X]
can be obtained from the observed data using an appropriate regression model. δ(·) is known as
the Delta Dirac function such that (1)
R
Rδ(x)dx = 1; and (2)∀ f∈ Ω with 0∈ Ω,
R
Ω f (x)δ(x)dx =
f (0).
In both the Dist-DR form and the Dist-IPW form, the unbiased estimation of the Dist-APO
Θ(a) is critically dependent on the accurate estimation of specific nuisance parameters. For the
Dist-DR form, this parameter is functional regression m(a; X) and for the Dist-IPW form, it is the
generalized propensity score p(a|X). Ideally, these estimations should align with the true nuisance
parameters to ensure unbiased results. However, achieving such accuracy in real-world applica-
tions is often a significant challenge. However, the Dist-DML form o ffers a unique advantage in
this context. It ensures the unbiasedness of Θ(a) even if either m(a; X) or p(a|X), but not both, are
estimated with a certain inaccuracy. This doubly robust property provides a significant safeguard
against potential modeling inaccuracies, ensuring that the estimation remains reliable as long as
one of the two components is correctly specified.
4.3. Dist-DML Estimator
The construction of estimators based on the Dist-DML form, as described in Eqn. (5), presents
a unique challenge due to the inclusion of the Delta Dirac function δ(·), which is a theoretical
construction that cannot be implementable in practice. To overcome this problem, an approxima-
tion approach is utilized in which the Delta Dirac function is replaced with a sequence of kernel
functions. The kernel sequence allows for the practical implementation of the concept embodied
by the Delta Dirac function in statistical estimations.
16

Definition 4 (Kernel function).
1. Given that K (·) : R→ R is a symmetric function (i.e., K (v) = K(−v)∀v∈ R). We say that
K(·) is a kernel function if it satisfies
R
R K(v)dv = 1.
2. A kernel function K (·) is said to have order ν (ν is an even number) if
R
R v jK(v) dv = 0
∀ 1≤ j≤ν− 1 and
R
R vνK(v) dv<∞.
In this paper, we focus specifically on second-order kernel functions (ν = 2), which are frequently
utilized in statistical estimations. A list of commonly used second-order kernel functions, along
with their properties, can be found in Table E.4 in Appendix Appendix E. For any given kernel
function K(x), we define its scaled kernel with a bandwidthh, denoted as Kh(x). The scaled kernel
is defined as:
Kh(x) := 1 h K  x h  and lim h→0 Kh(x) =δ(x).
Given that lim
h→0
Kh(x) =δ(x), we can replaceδ(A− a) in Eqn. (5) with Kh(A− a) for our estimation
purposes. Consequently, the estimator for the Dist-APO using the Dist-DML form, denoted as
ˆΘDML(a), is formulated using sample averaging:
ˆΘDML (a) = 1 N NX i=1  m(a; Xi) + Kh(Ai− a) p(a|Xi) (Y−1 i − m(a; Xi))  . (6)
In practice, to avoid the overfitting problem that often occurs when Dist-DML estimators are
used directly on the entire dataset, we implement the cross-fitting technique (Chernozhukov et al.,
2018). Specifically, we first partition the total N individuals intoK disjoint groups. Each group,
denoted asDk (k ={1,..., K}), contains Nk individuals. The complementary data for each group,
D−k, is formed by combining all other groups, i.e., D−k =∪K r=1,r,kDr. Then, we use D−k to learn
the estimated functions ˆmk(a;·) and the estimated generalized propensity score ˆpk(a|·). Finally, we
utilizeDk to compute ˆΘDML,k(a) using
ˆΘDML,k(a) = 1 Nk X i∈Dk  ˆmk(a; Xi) + Kh(Ai− a) ˆpk(a|Xi) (Y−1 i − ˆmk(a; Xi))  . (7)
Consequently, we can obtain the cross-fitted estimators ˆΘDML(a) by averaging these individual
estimates across allK groups:
ˆΘDML(a) =
KX
k=1
Nk
N
ˆΘDML,k(a). (8)
To end this section, we outline the above computation process in Algorithm 1.
17

Algorithm 1 Computations of ˆΘDML(a)
Require: Realizations of (Ai, Xi, Yi)N i=1. Determine the kernel function K(·).
1: Estimate ˆY−1 i for each unit i∈{ 1,··· , N}.
2: Split (Ai, Xi, ˆYi)N i=1 toK disjoint unitsDk where k∈{ 1,··· ,K} and formulateD−k. The size
ofDk is Nk.
3: for k← 1 toK do
4: Estimate ˆpk(a|·) based onD−k.
5: Estimate ˆmk(a;·) based onD−k.
6: Compute ˆΘDML,k(a) based onDk according to Eqns. (7).
7: end for
8: Compute ˆΘDML(a) according to Eqn. (8).
5. Theory
We investigate the asymptotic properties of the proposed estimator ˆΘDML(a). To facilitate
a clear and rigorous analysis, we begin by introducing several notations pertinent to our study.
Consider X as a random variable with a distribution function denoted by FX(x). In our analysis,
we consider three types of spaces, namely (1)L2(X; FX), (2)L2([0, 1];λ) whereλ is the Lebesgue
measure, and (3)L2(X× [0, 1]; FX×λ). Each space contains different forms of function:
1. L2(X; FX) contains f such that f :X→ R;
2. L2([0, 1];λ) contains g such that g : [0, 1]→ R;
3. L2(X× [0, 1]; FX×λ) contains Γ such that Γ :X× [0, 1]→ R.
Each of the defined spaces above is associated with the following norm:
1. ∥ f (X)∥2 2 = R X| f (x)|2dFX(x) = EP(X)[| f (X)|2];
2. ∥g∥2 = R [0,1] g(t)2dt;
3. |||Γ(X, t)|||2 = R X×[0,1] Γ2(x, t) dFX(x)dt = R X∥Γ(x, t)∥2dFX(x).
18

In addition, we can define an inner product ⟨·,·⟩ forL2([0, 1];λ): Given g, ˜g∈L 2([0, 1];λ), we
have
⟨g, ˜g⟩ =
Z
[0,1]
g(t)˜g(t)dt, where
Z
[0,1]
|g(t)|2dt,
Z
[0,1]
|˜g(t)|2dt <∞.
Let PN be the empirical average operator defined as PNO = 1 N PN s=1Os. We also denote the
learned estimates of m(a;·) from datasetD−k as ˜mk(a;·) and ˆmk(a;·) for the true outcome distribu-
tion Y and empirical outcome distribution ˆY, respectively. To quantify the estimation error, we
define
ρ4 m = sup
a∈A
{~ ˜mk(a)− m(a)~4} = sup
a∈A
{[
Z
X
∥ ˜mk(a; x)− m(a; x)∥2dFX(x)]2}
for 1≤ k≤K . Similarly, we define
ρ4 p = sup
a∈A
EP(X)[| ˆpk(a|X)− p(a|X)|4].
With these notations and definitions in place, we proceed to present the convergence assumptions
necessary to study the asymptotic properties of the proposed estimators.
Convergence Assumption 1. ˆY1,··· , ˆYN are estimates of Y1,··· , YN that are independent of
each other under the probability measure ˆP. Furthermore, there are two sequences of constants
αN = o(N− 1 2 ) andνN = o(N− 1 2 ) (which are thus o(1) automatically) such that
sup
1≤i≤N
sup
v∈W2(I)
E ˆP[D2 2( ˆYi, Yi)|Yi = v] = O(α2 N) and sup 1≤i≤N sup v∈W2(I) V ˆP[D2 2( ˆYi, Yi)|Yi = v] = O(ν4 N).
Here, V means the variance and V ˆP[D2 2( ˆYi, Yi)|Yi = v] is the variance of D2 2( ˆYi, Yi) conditioning
on Yi = v where v∈W 2(I).
Convergence Assumption 2.∀ a∈A and∀ 1≤ k≤K , we have
1. sup
x∈X
∥ ˜mk(a; x)− m(a; x)∥ = oP(1);
2. sup
x∈X
∥ ˆpk(a|x)− p(a|x)∥ = oP(1).
Convergence Assumption 3.∀ a∈A and 1≤ k≤K , we have
~ ˆmk(a;·)− ˜mk(a;·)~ = OP(N−1 +α2 N +ν2 N).
19

Convergence Assumption 4. There exist constants c1 and c2 such that 0 < c1≤ Nk N ≤ c2 < 1 for
all N and 1≤ k≤K .
The corresponding results for the asymptotic properties of ˆΘDML(a) are given in Theorem 1.
Theorem 1. Let h → 0, Nh → ∞, and Nh 5 → C ∈ [0,∞). Suppose that p (a|x) ∈ C3 on
A such that the derivatives (including the derivative of 0 order) are uniformly bounded in the
sample space for any x. Furthermore, we assume that EP|P(X)
Y−1|A = a, X∈C 3 in [0, 1]×A
and EP|P(X)
∥Y−1∥|A = a, X∈C 3 inA are uniformly bounded in the sample spaces. Under the
convergence assumptions, we have
√
Nh ˆΘDML (a)− Θ(a) = √ Nh  PN{φ(A, X, Y)}− Θ(a)  + oP(1), (9)
whereφ(A, X, Y) := φ(A, X, Y)(t) = Kh(A−a){Y−1(t)−m(a;X)(t)} p(a|X) + m(a; X)(t) andρmρp = o(N− 1 2 ),ρm =
o(1),ρp = o(1). Additionally, we have
√
Nh{ ˆΘDML(a)− Θ(a)− h2Ba} (10a)
converges weakly to a centred Gaussian process inL2([0, 1];λ) such that
Ba =
R
u2K(u)du
2 ×

EP(X)

∂2 aam(a; X) + 2∂am(a; X)∂ap(a|X) p(a|X)  .
The proofs for Theorem 1 are provided in Appendix Appendix F.4. This theorem underscores a
key advantage of the Dist-DML estimator. When estimators are constructed on the basis of the
Dist-DML form, the requirement for accuracy in estimating nuisance parameters can be relaxed.
Specifically, we only require the product ofρmρp equals o((Nh)− 1 2 ). This means, for instance, that
both ρm and ρp could be o((Nh)− 1 4 ), which is less strict than what is needed for the Dist-DR or
Dist-IPW estimators. In the case of the latter two estimators, both ρm andρp must individually be
o((Nh)− 1 2 ) to ensure accurate estimation.
We also give the covariance function of the central Gaussian process of Eqn. (10a).
Ψ(s) = E(P(A),P(X),P)[φ(A, X, Y)(s)], Ψ(s, t) = E(P(A),P(X),P)[φ(A, X, Y)(s)φ(A, X, Y)(t)].
The covariance function is C(s, t) such that
C(s, t) =hΨ(s, t)− hΨ(s)Ψ(t).
20

The leading term of C(s, t) is given by
Clea(s, t) = Z K2(u)duEP(X)  CV(s, t; a, X) p(a|X)  ,
where CV(s, t; a, X) = EP(X)[(Y−1(s)− m(a; X)(s))(Y−1(t)− m(a; X)(t))|A = a, X]. The asymptotic
quantity
E(P(A),P(X),P)[( ˆΘDML(a)(s)− ΘDML(a)(s))( ˆΘDML(a)(t)− ΘDML(a)(t))]
equals h4Ba(s)Ba(t) + Clea(s,t) Nh , and it allows us to choose a suitable h for the estimators ˆΘw(a). For
example, we can choose h such that
Z
[0,1]

h4Ba(s)Ba(t) + Clea(s, t) Nh 

s=t dt
is minimized. To compute the target quantity, we have to obtain ˆBa(t) and ˆC(s, t) which are esti-
mates of Ba(t) and Clea(s, t). ˆBa(t) and ˆC(s, t) are obtained as follows: denote ˆΘDML;β(a)(t) as the
computation of ˆΘDML(a)(t) using the bandwidth h =β. Then ˆBa(t) is given as
ˆBa(t) = ˆΘDML;β(a)(t)− ˆΘDML;ηβ(a)(t) β2(1−η2) , a∈ (0, 1)
followed by Powell and Stoker (1996). In the sequel, we chooseη = 0.5 andβ = 2h. On the other
hand, define
ˆΨh Nk(s) = 1 Nk X i∈Dk ˆφh k(Ai, Xi, Yi)(s), ˆΨh Nk(s, t) = 1 Nk X i∈Dk ˆφh k(Ai, Xi, Yi)(s) ˆφh k(Ai, Xi, Yi)(t),
where ˆφh k(Ai, Xi, Yi)(s) = Kh(Ai−a)( ˆY−1 i − ˆmk(a;Xi))(s) ˆpk(a|Xi) + ˆmk(a; Xi)(s). Then ˆC(s, t) is given as follows:
ˆC(s, t) = h K KX k=1 { ˆΨh Nk(s, t)− ˆΨh Nk(s) ˆΨh Nk(t)},
As such, we may find h∗ such that h∗ = arg min
h
R
[0,1]
h4 ˆBa(t)2 + ˆC(t,t) Nh dt	.
Finally, we can give an estimated range of values which includes the target quantityˆΘDML(a)(t)
for each a∈A and t∈ [0, 1]. Recall that ˆΘDML(a) = ˆΘDML(a)(·). The estimated range can be
obtained based on the result given in Theorem 1. For example, given a fixed h, if we want to
have a range with confidence level 1 −α for each a∈A and t∈ [0, 1], then we have Θ(a)∈
21


ˆΘDML(a)− Bah2− qα 2√ Nh, ˆΘDML(a)− Bah2 + qα 2√ Nh  where qα 2 satisfies P{ sup t∈[0,1] | √ Nh{ ˆΘDML(a)(t)−Θ(a)(t)−
Ba(t)h2}|≤ qα 2} = 1−α. To obtain an estimated range from the observed data, it remains to compute
the quantities Ba and qα 2 empirically. Previously, we demonstrated how to approximate Ba with
ˆBa. We now discuss how to estimate qα 2 . To start, suppose that we draw N samples (G1,··· , GN)
from the centered Gaussian process with covariance ˆC(s, t) (see Appendix Appendix H). For each
Gi, we compute gi = sup
t∈[0,1]
|Gi(t)|. We then obtain an estimate of qα 2 , denoted as ˆqα 2 , empirically
by finding the quantile at the quantile level 1− α 2 of g1,··· , gN. As a result, the estimated range is
empirically equal to

ˆΘDML (a)− ˆBah2− ˆqα 2√ Nh, ˆΘDML (a)− ˆBah2 + ˆqα 2√ Nh  .
6. Models
As Eqn. (7), it becomes essential to accurately estimate Y−1, p(a|X), and m(a; X) based on
the observed dataset. Estimation of Y−1, denoted as ˆY−1, is relatively straightforward. We can
estimate Y empirically and then invert it to obtain the corresponding quantile function ˆY−1. Esti-
mation of nuisance parametersm(a;·) and p(a|·) presents complex challenges due to the non-linear
relationship between outcome distribution and covariates, as well as the high-order dependencies
among covariates and treatment. To address the issue, we develop a comprehensive framework of
deep learning. This framework consists of two distinct components: (1) NFR Net and (2) CNF
Net. Each component is designed to effectively estimate different aspects of our model. The NFR
Net is specifically designed to estimate m(a; X), which aims to capture the functional relationship
between the covariatesX, treatment A, and the outcome distributionY−1. The CNF Net focuses on
estimating the propensity score p(a|X), estimating the conditional density of receiving a specific
treatment given covariatesX. A visual representation of our proposed model is provided in Figure
5. In this illustration, the NFR Net is shown on the left-hand side, and the CNF Net is depicted on
the right-hand side.
6.1. NFR Net
In cases where the outcome for each individual is scalar, neural networks, such as feed-forward
neural networks, have demonstrated their ability to capture complex patterns between the outcome,
22

𝐿𝑜𝑠𝑠ሺ𝜑ሻ ൌ׬ 𝒴ିଵሺ𝑡ሻ െ 𝒴෠ିଵሺ𝑡; 𝜑ሻ ଶ 𝑑𝑡
𝜑∗ ൌa r g m i n
ఝ
𝐿𝑜𝑠𝑠ሺ𝜑ሻ
NFR net
𝑿, 𝑨
Numerical Layers Continuous Layers
𝒇 𝑿, 𝑨; 𝝋 ሺ⋅ሻ ൌ 𝓨෡ ି𝟏ሺ⋅; 𝝋ሻ
Base distribution ( , ) Real distribution
𝜇௔ ൌ𝜇 ሺ 𝑿 ሻ
𝑿
𝑿, 𝑨 ൌ 𝒂
𝑠=𝑠ଵ 𝑠=𝑠଴
𝜎௔ ൌΣ ሺ 𝑿 ሻ
CNF net
𝐿𝑜𝑠𝑠ሺ𝜃ሻ ൌ׬
డ௚ሺ𝐳 ୱ, ୱ , 𝐗 ; ఏ ሻ
డ𝐳 ୱ 𝑑𝑠
௦బ
௦భ ൅l o g𝑝𝒛଴ 𝐗 ,
𝜃∗ ൌa r g m a x
ఏ
𝐿𝑜𝑠𝑠ሺ𝜃ሻ,  where
𝒛଴=d+׬ 𝑔ሺ𝐳 s, s , 𝐗 ; 𝜃 ሻ  𝑑 𝑠
௦బ
௦భ
𝒑 𝑨ൌ𝒂 | 𝑿 ;  𝜽
𝜙ଵሺ𝑡ሻ
𝜙ଶሺ𝑡ሻ
𝜙௟ିଵሺ𝑡ሻ
𝜙௟ሺ𝑡ሻ
Fig. 5. A visualization of our proposed model. The L.H.S. is the NFR Net which is designed to learn the quantity
m(a;·), while the R.H.S. is the CNF Net which aims to estimate the quantity p(a|X) when X = x.
treatment, and covariates. However, when the outcome for each individual is a distribution, as in
our context, the application of these conventional models is not straightforward.
To address this challenge, we turn to functional-on-scalar regression, a method well suited for
analyzing distributional outcomes (Ramsay and Silverman, 2005). This approach utilizes a finite
series of predetermined basis functions to approximate the regression equation. Mathematically,
given a set of basis functions {ϕ1,··· ,ϕ v} (e.g., B-spline basis), the linear functional regression
model (Chen et al., 2016) can be expressed as follows:
˜Y−1(t) = A
vX
k=1
α0kϕk(t) +
dX
j=1
β jX j +ϵ(t), β j =
vX
k=1
α jkϕk(t). (11)
Here, ˜Y−1(t) is the estimated outcome function, ( A, X) = [A, X1,··· , X j,··· , Xd] are predictors,
α jk (0≤ j≤ d and 1≤ k≤ v) are the regression parameters andϵ(t) is the noise term.
Eqn. (11) is a valuable approach that assumes an additive relationship between ˜Y−1(t) and the
predictors (A, X). However, in many cases, this relationship is inherently non-linear and involves
high-order dependencies. To address this complexity, we have designed the NFR Net, which is
a deep learning architecture tailored to capture these intricate patterns. The NFR Net comprises
two integral parts: (1) the numerical layers and (2) the continuous layer (see Figure 5). In our
framework and settings, the numerical layers focus on learning a representationF (A, X;η), which
23

is a u-dimensional vector such that
F (A, X;η) = [F1(A, X;η),··· ,Fu(A, X;η)],
whereFi(A, X;η) represents thei-th linear component that contributes to the formation of the target
distribution.F (A, X;η) is then processed by a continuous layer to output the estimated function
˜Y−1(t) with
˜Y−1  t;η,α i j  = uX
i=1
Fi(A, X;η)
vX
j=1
αi jϕ j(t),
whereαi j are the training parameters.
To train our model effectively, we define a loss metricL (such asL1/L2 loss) that measures the
difference between the empirical estimates ˆY−1(t) and the estimates of the functional regression
model ˜Y−1(t), and focus on min
η,αi j
L(η,α i j), where
L(η,α i j) B
Z 1
0
L( ˜Y−1  t;η,α i j  , ˆY−1(t))dt.
In practice, we can approximate the integral using the trapezoidal rule or Simpson’s rule by taking
a number of discrete quantile points t.
6.2. CNF Net
Estimating the density function from observed data is a pivotal task in various fields. Tra-
ditional approaches to this problem assumed specific forms for the target density (Varanasi and
Aazhang, 1989, Efromovich, 2010), or employed kernel-based methods (Nadaraya, 1964, Watson,
1964, Silverman, 2018). However, each of these methods presents certain limitations. For exam-
ple, assuming specific forms for the target density lacks prior knowledge about the true form of
the target density, leading models not flexible enough to accurately capture the underlying distri-
bution, especially in complex datasets. Furthermore, kernel-based methods, while more flexible,
heavily depend on the choice of the appropriate bandwidth.
Beyond traditional methods, we turn our focus to the use of normalizing flows (Dinh et al.,
2015), an advanced generative approach, to estimate density functions. Normalizing flows lever-
age the concept of transforming a base distribution Z (e.g., standard normal distribution) into a
target distribution Y through a learnable, di fferentiable, and bijective function G, i.e., y = G(z).
24

The relationship between the densities of the base distribution pZ(z) and the target distribution
pY(y) is governed by the change of variables formula:
pY(y) = pZ

G−1(y) 

det∂G(z) ∂z

 −1
⇒ log pY(y) = log pZ

G−1(y)  − log

det∂G(z) ∂z

.
Typically, the transformation function G is parameterized using a sequence of neural networks,
i.e., G = G1◦···◦ GM. A key consideration in designing these neural networks, particularly the
weight matrices of G j, for j = 1,··· , M, is to ensure that they are triangular, which facilitates
efficient computation of the determinant of the Jacobian (Dinh et al., 2017, Kingma and Dhariwal,
2018). However, a notable challenge with this design is the high computational cost, especially
when dealing with large-scale data (Chen et al., 2018). To mitigate this issue, we apply the contin-
uous normalizing flow (Grathwohl et al., 2019) which converts the discrete transformation process
into continuous dynamics, so that it achieves state-of-the-art results without the need for a trian-
gular design. Such a continuous transformation is always governed by neural ordinary differential
equations (Neural ODEs) that can be described by the following integral equation:
"
z(τ0)
log pY(y)− log pZ(τ0)(z(τ0))
#
=
"
y
0
#
+
Z τ0
τ1
" g(z(τ),τ )
Tr∂g(z(τ),τ) ∂z(τ) 
#
dτ. (12)
Here,τ0 andτ1 represent the initial and final flow times, respectively, withz(τ0) = z and z(τ1) = y
being realizations of the base distribution Z and the target distribution Y. The function g is bijec-
tive, Lipschitz continuous in z and continuous in τ, and Tr denotes the trace operator. This trans-
formation process characterizes how a realized individual point of the base distribution ‘flows’
through the ODEs to reach its counterpart in the target distribution.
Although continuous normalizing flows have been introduced primiarily to estimate uncon-
ditional density functions, we extend it to CNF Net (see Figure 5) to estimate the conditional
density function, focusing on the propensity score p(a|X). Specifically, we consider an augmented
state z(τ) = [z(τ), X(τ)]⊤ where z(τ) characterizes a flow from a base variable (initially at z(τ0)
when τ = τ0) to the treatment variable (ultimately at z(τ1) = a when τ = τ1), while X(τ) = X,
∀τ0≤τ≤τ1. Consequently, the transformation form of the first equation in Eqn. (12) becomes
"
z(τ0)
X(τ0)
#
=
"
a
X
#
+
Z τ0
τ1
"
g(z(τ), X,τ )
0
#
dτ. (13)
25

Additionally, we establish a relationship between the logarithmic densities log p(z(τ0), X) and
log p(a, X) based on the second equation of Eqn. (12), as formally stated in Proposition 3.
Proposition 3. Let z(τ) = [z(τ), X]⊤ be a finite continuous random variable, and the probability
density function of z(τ) is p(z(τ)) = p(z(τ), X) which depends on timeτ, whereτ0≤τ≤τ1. Given
the governing equation of z(τ) in Eqn. (13) and g is Lipschitz continuous in z and continuous inτ
for any X, we have
log p(a, X) = log p(z(τ0), X) +
Z τ0
τ1
 ∂g(z(τ), X,τ )
∂z(τ)
!
dτ. (14)
The formal proofs are deferred to the Appendix Appendix F.5. Then, by subtracting both sides of
Eqn. (14) by log p(X), we have
log p(a|X) = log p(z(τ0)|X) +
Z τ0
τ1
 ∂g(z(τ), X,τ )
∂z(τ)
!
dτ. (15)
This formulation indicates that the densityp(a|X) is dependent on the conditional base distribution
p(z(τ0)|X). To model this base distribution, we assume that z(τ0)|X follows a conditional normal
distributionN(µ(X),σ 2(X)). Here, µ(·) and σ(·) are two functions parametrized by feed-forward
neural networks that represent the mean and standard deviation of the conditional normal distribu-
tion, respectively. In the final step of implementing our CNF Net framework, the training process
revolves around maximizing the log-likelihood function, specifically log p(a|X).
7. Numerical Experiment
7.1. Experiment Setting
To verify our theories and models, we perform a numerical experiment in which the treatment
takes continuous values, and the outcome for each sample is a specific distribution function. The
data generation process (DGP) for our numerical experiment is designed to simulate the intricate
dynamics often encountered in real-world datasets, aiming to assess the capability of our models
in handling non-linear interactions and complex causal relationships. The DGP is formulated as
26

0.0 0.2 0.4 0.6 0.8 1.0
Quantiles
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4Y 1
instance 2584
instance 4338
instance 4556
instance 3438
instance 737
Fig. 6. The inverse CDF of 5 simulated samples
follows:
Y−1 i (·) = c + (1− c)(E[γ⊤Xi] + exp (Ai))×
n
2X
j=1
w jB−1  α j,β j  +ϵi,
w j =
exp

X2 j−1 i X2 j i 
n
2P
k=1
exp

X2k−1 i X2k i ,
Ai∼N (γ⊤Xi, log(1 + exp(ξ⊤Xi)),
(16)
where Y−1 i is the quantile function of the individuali, which is a complex function of the treatment
Ai and the covariates Xi. Ai follows a Gaussian distribution whose mean and variance are con-
trolled by the covariates Xi. n is an even number that indicates the number of covariates.B−1(α,β )
is the inverse CDF (quantile function) of the Beta distribution with the shapes’ parameters α and
β. We choose Beta distributions because they vary widely given different parameters. c is the con-
stant that controls the strength of the causal relationship between Ai and Y−1 i . ϵi is the noise that
followsN(0, 0.05). In the experiment, we configure the number of covariates ( n) to be 10, where
X1, X2∼N (−2, 1), X3, X4∼N (−1, 1), X5, X6∼N (0, 1), X7, X8∼N (1, 1), and X9, X10∼N (2, 1).
To add complexity to the outcome distributions, we utilize five inverse Beta CDFs, each set with
distinct parameters. For each individual in our dataset, we generate 100 observations in accor-
dance with our data generation process (Eqn. (16)) using the inverse transform sampling method.
In total, 50,000 individuals are generated. Figure 6 summarizes 5 simulated individuals, where the
27

curve represents the true inverse CDF and the points indicate the corresponding observations for
each unit. This visualization highlights the variability in the inverse CDFs between different treat-
ments. The primary objective of the experiment is to estimate the potential outcome distributions
for all individuals when treated with specific treatment values: −0.5, 0.0, and 0.5 (i.e., A =−0.5,
0.0, 0.5).
Two components, the NFR Net and CNF Net, are trained separately during an experiment
to estimate the functional outcome Y−1 and the conditional density p(a|X). To optimize perfor-
mance, the hyperparameters of NFR Net and CNF Net are tuned using the random search approach
(Bergstra and Bengio, 2012), and the finalized training parameters include a learning rate of 0.003,
a batch size of 128, and a weight decay of 0.001. The Adam algorithm (Kingma and Ba, 2015) is
set as the default optimizer. To ensure e fficient convergence and prevent overfitting, an adaptive
learning rate strategy is used, wherein if the validation loss does not decrease over 10 epochs, the
learning rate would be reduced by half. The model that performs best during the training phase is
preserved and subsequently used to compute counterfactual distributional outcomes.
We implement a two-fold cross-fitting technique for training. Half of the individuals (25,000)
are utilized for training purposes, while the remaining half are used to obtain the Dist-DML es-
timator and two benchmark Dist-DR and Dist-IPW estimators. To assess the performance of our
estimators, we discretize both the ground truth outcome distribution Θ(a) and the estimated Dist-
APO ˆΘ(a), comparing them across 9 quantiles, ranging from 0.1 to 0.9. The Mean Absolute Error
(MAE) between these discretized outcomes serves as our primary metric of performance. To en-
sure the robustness of our results, the entire experiment is repeated 100 times. This repetition
allows us to report both the mean and the standard deviation of the MAE, providing a comprehen-
sive view of the performance and reliability of our estimators under varying conditions.
7.2. Comparison between Dist-DR, Dist-IPW, Dist-DML Estimators
Table 2 presents the results of the numerical experiment, showing the e fficacy of di fferent
estimators in recovering the distributions of potential outcomes at three treatment levels A =
−0.5, 0.0, 0.5. The ground truth for the outcome distribution, derived from the DGP as speci-
fied in Eqn. (16), is presented in the first row for each treatment level. The performance of the
28

Table 2 The numerical experiment results of DR, IPW, and DML estimators on treatment A =−0.5, 0.0, 0.5
Q=0.1 Q =0.2 Q =0.3 Q =0.4 Q =0.5 Q =0.6 Q =0.7 Q =0.8 Q =0.9 Avg.
A =−0.5
Ground 0.0068 0.0279 0.0654 0.1374 0.3053 0.4731 0.5452 0.5826 0.6038
Dist-DR 0.0007 (0.0022) 0.0225 (0.0013) 0.0928 (0.0018) 0.1948 (0.0034) 0.3118 (0.0055) 0.4274 (0.0076) 0.5265 (0.0093) 0.5943 (0.0104) 0.6160 (0.0106)
Dist-DR (MAE) 0.0061 0.0054 0.0274 0.0573 0.0065 0.0457 0.0187 0.0117 0.0123 0.0212
Dist-IPW -0.0028 (0.0001) 0.0400 (0.0012) 0.0889 (0.0026) 0.1679 (0.0047) 0.3171 (0.0086) 0.4581 (0.0123) 0.5321 (0.0143) 0.5791 (0.0156) 0.6220 (0.0168)
Dist-IPW (MAE) 0.0096 0.0120 0.0235 0.0305 0.0118 0.0150 0.0131 0.0035 0.0182 0.0153
Dist-DML -0.0026 (0.0001) 0.0405 (0.0005) 0.0900 (0.0002) 0.1697 (0.0007) 0.3195 (0.0005) 0.4612 (0.0010) 0.5357 (0.0007) 0.5833 (0.0009) 0.6267 (0.0008)
Dist-DML (MAE) 0.0094 0.0126 0.0246 0.0322 0.0142 0.0120 0.0094 0.0007 0.0229 0.0153
A = 0.0
Ground 0.0112 0.0459 0.1075 0.2260 0.5020 0.7780 0.8965 0.9581 0.9929
Dist-DR 0.0103 (0.0034) 0.0311 (0.0021) 0.1406 (0.0033) 0.3080 (0.0059) 0.5028 (0.0092) 0.6948 (0.0128) 0.8560 (0.0160) 0.9590 (0.0180) 0.9762 (0.0185)
Dist-DR (MAE) 0.0009 0.0148 0.0330 0.0820 0.0008 0.0832 0.0405 0.0008 0.0167 0.0303
Dist-IPW 0.0078 (0.0003) 0.0608 (0.0014) 0.1321 (0.0031) 0.2618 (0.0060) 0.5108 (0.0115) 0.7489 (0.0169) 0.8693 (0.0197) 0.9377 (0.0212) 0.9900 (0.0224)
Dist-IPW (MAE) 0.0034 0.0149 0.0246 0.0358 0.0088 0.0291 0.0272 0.0204 0.0029 0.0185
Dist-DML 0.0080 (0.0002) 0.0615 (0.0007) 0.1346 (0.0003) 0.2672 (0.0011) 0.5195 (0.0005) 0.7610 (0.0015) 0.8841 (0.0008) 0.9543 (0.0008) 1.0070 (0.0009)
Dist-DML (MAE) 0.0031 0.0155 0.0271 0.0412 0.0175 0.0171 0.0124 0.0038 0.0141 0.0169
A = 0.5
Dist-Ground 0.0184 0.0756 0.1770 0.3720 0.8264 1.2807 1.4758 1.5772 1.6344
Dist-DR 0.0233 (0.0058) 0.0443 (0.0034) 0.2184 (0.0066) 0.4924 (0.0130) 0.8129 (0.0211) 1.1276 (0.0297) 1.3879 (0.0374) 1.5461 (0.0428) 1.5543 (0.0448)
Dist-DR (MAE) 0.0050 0.0313 0.0414 0.1203 0.0135 0.1531 0.0878 0.0311 0.0801 0.0626
Dist-IPW 0.0205 (0.0025) 0.0929 (0.0115) 0.2031 (0.0253) 0.4190 (0.0528) 0.8284 (0.1047) 1.2173 (0.1547) 1.4135 (0.1794) 1.5183 (0.1925) 1.5879 (0.2011)
Dist-IPW (MAE) 0.0021 0.0174 0.0261 0.0469 0.0020 0.0634 0.0622 0.0589 0.0465 0.0362
DML 0.0212 (0.0010) 0.0949 (0.0065) 0.2088 (0.0019) 0.4302 (0.0083) 0.8459 (0.0060) 1.2411 (0.0168) 1.4427 (0.0115) 1.5511 (0.0091) 1.6219 (0.0120)
Dist-DML (MAE) 0.0029 0.0193 0.0318 0.0582 0.0195 0.0396 0.0331 0.0260 0.0125 0.0270
Dist-DR, Dist-IPW, and Dist-DML estimators in approximating this ground truth is then detailed,
with the mean, standard deviation of the estimates, and the corresponding MAE provided. The re-
sults reveal that while all estimators demonstrate the ability to approximate the potential outcome
distribution, the Dist-DML estimator stands out in terms of performance. Across all treatment
levels, the Dist-DML estimator consistently achieves the lowest MAE, underscoring its robustness
and precision. This superior performance aligns with theoretical expectations, as the Dist-DML
estimator is designed to capitalize on the strengths of both the Dist-DR and Dist-IPW estimators,
thereby enhancing its reliability and accuracy.
Figure 7 complements this analysis by visually representing the ground truth, the estimated
function, and the 95% confidence interval, estimated over 100 experimental runs, when the treat-
29

Fig. 7. The ground and estimated quantile function when A =0.0 based on Dist-DR (left), Dist-IPW (middle), and
Dist-DML (right) Estimators
ment equals 0.0. This graphical depiction illustrates that the Dist-DR estimator tends to show a
smaller variance but a larger bias, while the Dist-IPW estimator exhibits a larger variance but a
smaller bias. The Dist-DML estimator, on the other hand, adeptly balances these aspects, mani-
festing both lower bias and lower variance.
7.3. Sensitivity Analysis
In our theoretical exploration, it became apparent that the sample size and the bandwidth of
the kernel function play a pivotal role in the convergence behavior of the Dist-DML estimator. In
particular, an increase in the sample size tends to enhance the convergence speed of the estimator,
suggesting that larger datasets can lead to more accurate and stable estimates. Meanwhile, a small
bandwidth of the kernel function allows for a closer approximation to the Delta Dirac function,
thereby potentially improving the precision of the estimator in capturing the true causal e ffect.
Building on these theoretical insights, we further investigate the practical implications through
simulation experiments.
7.3.1. The Impact of Sample Size
In this experiment, we fix the bandwidth to an optimal value and then adjust the sample size
using the same data generation process, testing a range of 1000 to 100,000. Each experiment is
conducted 100 times to ensure the reliability of the results. The results of these experiments are
30

Fig. 8. The estimated MAE w.r.t various sample size for Dist-DML estimator.
depicted in Figure 8, which illustrates the estimated MAE with respect to di fferent sample sizes
for the Dist-DML estimator at three di fferent treatment levels (A =−0.5, A = 0.0, and A = 0.5).
Within each sub-plot, the blue line represents the mean MAE computed from the 100 repetitions,
and the shaded area around the line indicates the standard deviation of the MAE across these
repetitions. Each of the three plots corresponds to a specific treatment level and shows a blue
line that represents the mean MAE derived from 100 repeated experiments, while the shaded
area indicates the standard deviation of the MAE across these experiments. The plots reveal that
when the sample size is small (e.g., 1,000 or 5,000), the MAE is relatively larger, implying a less
accurate estimation at all three treatment levels. However, as the sample size increases, there is a
clear downward trend in the MAE, which suggests enhanced accuracy of the Dist-DML estimator.
In addition, the reduction in the shaded area as the sample size grows indicates a decrease in the
variance of the estimator, thus reflecting more robust and consistent results.
7.3.2. The Impact of Bandwidth
In this experiment, we maintain a constant sample size while varying the bandwidth of the
kernel function. As stated in section 5, the optimal bandwidth, denoted as h∗, is determined for
the Dist-DML estimator by minimizing
R
[0,1]
h4 ˆBa(t)2 + ˆC(t,t) Nh dt. This selection process is detailed
in the Appendix Appendix G. We test a range of bandwidths that are multiples of h∗: specifically
h∗
6 , h∗ 4 , h∗ 2 , h∗, 2h∗, 4h∗, and 6h∗.
The results, displayed in Figure 9, illustrate the estimated MAE in relation to the varying band-
31

Fig. 9. The estimated MAE w.r.t the different bandwidth for Dist-DML estimator.
widths for the Dist-DML estimator. As the bandwidth narrows, the MAE decreases, suggesting
increased precision in the estimations at the three treatment levels (A =−0.5, A = 0.0 and A = 0.5).
This trend indicates that a more focused kernel function more accurately approximates the Delta
Dirac function, leading to a more precise estimation of the Dist-ATE. The experiment also reveals
that the smallest standard deviation in the estimated MAE occurs at the optimal bandwidth h∗,
since it is selected when the covariance function is at its minimum.
8. Empirical Application
In recent times, the rapid advancement of financial technology (FinTech) has facilitated the
proliferation of electronic platforms within the credit market, notably through the introduction
of online consumer credit systems (Balyuk, 2023). These E-platforms, such as Taobao.com and
JD.com, offer online marketplace services that enable consumers to make credit-based purchases
without an immediate payment requirement. Simultaneously, by harnessing a comprehensive array
of consumer data, including browsing, transaction, and credit records, these platforms leverage
advanced machine learning algorithms to customize credit limits for individual users.
The capacity of E-commerce platforms to set di fferentiated credit limits for individual users
raises a critical research question: how does adjustment in credit limits influence consumer spend-
ing behaviors? To investigate this problem, we employ our approach by using data collected from
a leading and large E-commerce platform in China. The platform assigns unique credit limits to
32

consumers based on a variety of factors, including their income, ages, genders, and historical be-
haviors such as shopping and credit records. The platform also o ffers a one-month interest-free
loan for purchases, with the stipulation that the total loan amount must not exceed the user’s credit
limit. Our primary objective in this section is to analyze how alterations in credit limits influence
the distribution of consumer spending, thereby contributing to a deeper understanding of consumer
behavior in the context of the E-commerce platform.
We randomly collect data from 10,220 consumers on the platform, spanning a 12-month period
from January to December 2019, which encompasses a wide range of information, including de-
mographic details such as gender, age, and geographic location, alongside comprehensive records
of shopping and financial behavior. The shopping records include measures such as the total
number of orders, pricing, discounts availed, payments for each order, etc. The financial records
encompass the credit limits for each consumer, the credit status, and the borrowings, repayments,
and refunds for each loan. Data from the first half of the year (January to June 2019) are used to
construct the covariates. Subsequently, the impact of credit limits on spending distribution is ana-
lyzed using data from the latter half (July to December 2019). The spending distribution for each
consumer is represented by all payments in individual orders during this period. Figure (10a) dis-
plays the spending distributions of ten randomly selected consumers, suggesting that the spending
distribution varies greatly between consumers. Furthermore, Figure (10b) presents the distribu-
tion of credit limits assigned to all users on the platform, revealing that the majority of users
are assigned credit limits of around 8,000, while a small proportion of users are assigned higher
credit limits, resulting in a skewed long-tailed distribution. For a detailed understanding of these
variables and their distribution, Table 3 provides a statistical summary for some key variables.
Specifically, the demographic profile of users on the E-commerce platform is relatively young,
with an average age of 33.23 years, and is predominantly male, comprising 64% of the consumer
population. These individuals show strong loyalty and engagement, as evidenced by an average
duration of platform use of nearly 2,375 days and an average involvement with credit services
of approximately 1,246 days. Regarding purchasing behavior, consumers place an average of
54.35 orders comprising 106.9 products in the first half of the year. The average order value is
399.5, typically before applying an average discount of 111.73. From a financial perspective,
33

(a) The spending distributions of 10 consumers.
 (b) The credit limit distribution of all consumers.
Fig. 10. The spending distribution and credit limit distribution.
Table 3 The statistical description for important variables.
Category Variables mean std 25% 50% 75%
age 33.23 6.86 28 32 37
gender 0.64 0.48 0 1 1
platform usage days 2375.69 460.11 2094.75 2291 2499
credit usage days 1246.96 325.53 1003 1147 1466
num of orders 54.35 28.96 37 46 61
num of products 106.90 66.26 65 89 127
Covariates averaged order price 399.53 336.27 235.36 338.50 482.13
averaged discount price 111.73 158.36 62.43 91.49 134.03
num of credit usage 21.94 26.59 4 14 32
amount of credit usage 428.16 785.81 114.35 211.00 414.80
num of credit repayment 5.25 3.79 3 5 6
amount of credit repayment 887.00 1023.90 243.80 588.29 1168.93
Treatment credit limit 8042.93 3184.64 6161.63 8000 9800
spending (Q=0.1) 29.84 22.35 12.98 28.70 41.79
spending (Q=0.3) 62.15 37.15 35.9 59.9 88.98
Outcome spending (Q =0.5) 104.1 57.54 68.99 100.97 130.00
spending (Q=0.7) 180.94 109.74 109.90 163.69 221.98
spending (Q=0.9) 487.08 401.06 244 377.56 599.08
the utilization of credit services is frequent among consumers, averaging 21.9 borrows with an
average loan amount of 428.16. In addition, consumers often repay multiple loans concurrently,
reflecting from the observations that the average number of credit repayments per consumer is
34

Fig. 11. The potential spending distribution outcome across credit limits from 0 to 20,000
5.25, leading to an average total repayment amount of 887. The distribution of credit limits,
with an average of 8,042 and a standard deviation of 3,184, reveals a considerable range in the
credit capacity allocated to di fferent consumers. The spending behavior of each consumer, as
the outcome variable, is conceptualized as a distribution. We focus on the quantiles of these
distributions, providing a detailed representation of spending patterns. Specifically, the average
expenditures at the quantiles of 0.1, 0.3, 0.5, 0.7, and 0.9 are observed to be 29.84, 62.15, 104.1,
180.94, and 487.08, respectively.
In line with our numerical experiment, we approximate the integral loss by discretizing it
across 9 quantiles, ranging from 0.1 to 0.9. In this study, we explore potential shifts in spending
35

distributions in response to a range of credit limits, extending from 0 to 20,000, incremented in
steps of 1,000 (i.e., 0, 1,000, 2,000, ··· , 20,000). To ensure the reliability and robustness of our
findings, we undertake multiple iterations of model training, repeating the process 100 times with
both the NFR Net and the CNF Net. The results of our empirical experiments are visualized
in Figure 11. In these figures, each subfigure delineates the average potential spending at each
quantile level (from Q = 0.1 to Q = 0.9) and its corresponding 95% confidence interval across
various credit limits. Generally, lower quantiles (e.g.,Q = 0.1) typically represent smaller amounts
of expenditure, often associated with essential daily purchases like necessities. In contrast, the
higher quantiles (e.g., Q = 0.9) reflect larger spending amounts, usually indicative of discretionary
purchases such as luxury items or services.
In line with previous studies, our results demonstrate a positive correlation between credit lim-
its and consumer spending, underscoring the role of credit as a catalyst for consumption (Aydin,
2022). Our analysis reveals a heterogeneous e ffect across different spending quantiles. In partic-
ular, as credit limits increase, we observe a substantial increase in spending at higher quantiles.
For example, at the 0.9 quantile, spending increases from 375.1 to 897.9 with an increase in the
credit line from 0 to 20,000, marking a growth of approximately 139%. In contrast, spending
at lower quantiles shows relatively modest growth. Specifically, at the 0.1 quantile, spending in-
creases from 28.1 to 37.2 over the same range of increase in credit lines, reflecting growth of only
32%. This trend suggests that consumers tend to disproportionately allocate additional credit to-
ward the purchase of higher-priced items or services rather than distributing the credit uniformly
across various spending categories. This discovery has practical implications for platforms con-
sidering increases in consumer credit limits. Specifically, by recommending higher-end products
in conjunction with increased credit limits, platforms might tap into a market segment previously
unexplored by consumers due to budget constraints.
9. Conclusion
In this paper, we tackle a significant challenge in the realm of causal inference: how to ef-
fectively estimate treatment-outcome relationships when the outcome of each individual is repre-
sented as distributions and the treatments are continuous. Our proposed causal inference frame-
36

work utilizes the Wasserstein space that captures the underlying geometry of distributional out-
comes, offering a more detailed understanding of complex behavioral patterns.
We introduce two novel causal quantities, the Dist-APO and the Dist-ATE, designed specifi-
cally for the complexities inherent in distributional data. To accurately estimate these quantities,
we have developed a machine learning-based robust estimator: the Dist-IPW estimator. Its statisti-
cal asymptotic properties have been rigorously established, laying a strong theoretical foundation
for application.
To ensure a precise estimation of the necessary nuisance parameters in these estimators, we
have developed a deep learning model comprising two main components: the NFR Net and the
CNF Net. The NFR Net is highly e ffective in modeling complex, non-linear relationships, while
the CNF Net excels in accurately estimating generalized propensity scores. Their combination
provides a robust tool for handling high-dimensional data and intricate interactions among vari-
ables.
Through comprehensive numerical studies, we have demonstrated the effectiveness of our pro-
posed Dist-DML estimator. In applying our approach to real-world data, we explored the causal
effects of credit limit adjustments on consumer spending distributions. Our findings provide crit-
ical insights into consumer behavior, revealing a tendency to allocate increased credit towards
purchasing more expensive items rather than uniformly increasing spending across all items. This
behavior offers essential perspectives on consumer spending in response to changes in credit pol-
icy, contributing valuable knowledge to the financial and marketing sectors.
References
Agarwal, S., Chomsisengphet, S., Meier, S., and Zou, X. (2020). In the mood to consume: Effect of sunshine on credit
card spending. Journal of Banking & Finance, 121:105960.
Agarwal, S., Liu, C., and Souleles, N. S. (2007). The reaction of consumer spending and debt to tax rebates—evidence
from consumer credit data. Journal of political Economy, 115(6):986–1019.
Aydin, D. (2022). Consumption response to credit expansions: Evidence from experimental assignment of 45,307
credit lines. American Economic Review, 112(1):1–40.
Bacchetta, P. and Gerlach, S. (1997). Consumption and credit constraints: International evidence.Journal of Monetary
Economics, 40(2):207–238.
37

Balyuk, T. (2023). Fintech lending and bank credit access for consumers. Management Science, 69(1):555–575.
Banerjee, A., Karlan, D., and Zinman, J. (2015). Six randomized evaluations of microcredit: Introduction and further
steps. American Economic Journal: Applied Economics, 7(1):1–21.
Bergstra, J. and Bengio, Y . (2012). Random search for hyper-parameter optimization. Journal of Machine Learning
Research, 13(2):281–305.
Bodory, H., Huber, M., and Lafférs, L. (2022). Evaluating (weighted) dynamic treatment e ffects by double machine
learning. The Econometrics Journal, 25(3):628–648.
Breza, E. and Kinnan, C. (2021). Measuring the equilibrium impacts of credit: Evidence from the indian microfinance
crisis. The Quarterly Journal of Economics, 136(3):1447–1497.
Cai, X., Xue, L., Cao, J., and Initiative, A. D. N. (2022). Robust estimation and variable selection for function-on-
scalar regression. Canadian Journal of Statistics, 50(1):162–179.
Chen, R. T. Q., Rubanova, Y ., Bettencourt, J., and Duvenaud, D. K. (2018). Neural ordinary differential equations. In
Advances in Neural Information Processing Systems, volume 31.
Chen, Y ., Goldsmith, J., and Ogden, R. T. (2016). Variable selection in function-on-scalar regression. Stat, 5(1):88–
101.
Chernozhukov, V ., Chetverikov, D., Demirer, M., Duflo, E., Hansen, C., Newey, W., and Robins, J. (2018). Dou-
ble/debiased machine learning for treatment and structural parameters. The Econometrics Journal, 21(1):C1–C68.
Cornelli, G., Frost, J., Gambacorta, L., Rau, P. R., Wardrop, R., and Ziegler, T. (2023). Fintech and big tech credit:
Drivers of the growth of digital lending. Journal of Banking & Finance, 148:106742.
Dinh, L., Krueger, D., and Bengio, Y . (2015). Nice: Non-linear independent components estimation. InInternational
Conference on Learning Representations, volume 31.
Dinh, L., Sohl-Dickstein, J., and Bengio, S. (2017). Density estimation using real nvp. In International Conference
on Learning Representations, volume 31.
Ecker, K., de Luna, X., and Schelin, L. (2024). Causal inference with a functional outcome. Journal of the Royal
Statistical Society Series C: Applied Statistics, 73(1):221–240.
Efromovich, S. (2010). Orthogonal series density estimation. Wiley Interdisciplinary Reviews: Computational Statis-
tics, 2(4):467–476.
Farrell, M. H. (2015). Robust inference on average treatment effects with possibly more covariates than observations.
Journal of Econometrics, 189(1):1–23.
Feinberg, R. A. (1986). Credit cards as spending facilitating stimuli: A conditioning interpretation. Journal of
Consumer Research, 13(3):348–356.
Feyeux, N., Vidard, A., and Nodet, M. (2018). Optimal transport for variational data assimilation.Nonlinear Processes
in Geophysics, 25(1):55–66.
Grathwohl, W., Chen, R. T. Q., Bettencourt, J., Sutskever, I., and Duvenaud, D. (2019). FFJORD: free-form continu-
38

ous dynamics for scalable reversible generative models. InInternational Conference on Learning Representations.
Gross, D. B. and Souleles, N. S. (2002). Do liquidity constraints and interest rates matter for consumer behavior?
evidence from credit card data. The Quarterly journal of economics, 117(1):149–185.
Hall, R. E. (1978). Stochastic implications of the life cycle-permanent income hypothesis: theory and evidence.
Journal of political economy, 86(6):971–987.
Hernán, M. A. and Robins, J. M. (2010). Causal inference.
Hirano, K., Imbens, G. W., and Ridder, G. (2003). Efficient estimation of average treatment effects using the estimated
propensity score. Econometrica, 71(4):1161–1189.
Hirschman, E. C. (1979). Di fferences in consumer purchase behavior by credit card payment system. Journal of
Consumer Research, 6(1):58–66.
Horvitz, D. G. and Thompson, D. J. (1952). A generalization of sampling without replacement from a finite universe.
Journal of the American Statistical Association, 47(260):663–685.
Huang, Y ., Leung, C. H., Yan, X., Wu, Q., Peng, N., Wang, D., and Huang, Z. (2021). The causal learning of retail
delinquency. Proceedings of the AAAI Conference on Artificial Intelligence, 35(1):204–212.
Jappelli, T. and Pagano, M. (1989). Consumption and capital market imperfections: An international comparison.
The American Economic Review, pages 1088–1105.
Kennedy, E. H., Balakrishnan, S., and Wasserman, L. (2023). Semiparametric counterfactual density estimation.
Biometrika, 110(4):875–896.
Kingma, D. P. and Ba, J. (2015). Adam: A method for stochastic optimization. In International Conference on
Learning Representations.
Kingma, D. P. and Dhariwal, P. (2018). Glow: Generative flow with invertible 1x1 convolutions. In Advances in
Neural Information Processing Systems, volume 31.
Li, J., Song, Q., Wu, Y ., and Huang, B. (2021). The effects of online consumer credit on household consumption level
and structure: Evidence from china. Journal of Consumer Affairs, 55(4):1614–1632.
Li, Y ., Leung, C. H., Sun, X., Wang, C., Huang, Y ., Yan, X., Wu, Q., Wang, D., and Huang, Z. (2024). The causal
impact of credit lines on spending distributions. Proceedings of the AAAI Conference on Artificial Intelligence ,
38(1):180–187.
Lin, Z., Kong, D., and Wang, L. (2023). Causal inference on distribution functions. Journal of the Royal Statistical
Society Series B: Statistical Methodology, 85(2):378–398.
Martinez-Taboada, D. and Kennedy, E. (2024). Counterfactual density estimation using kernel stein discrepancies. In
International Conference on Learning Representations.
Modigliani, F. and Brumberg, R. (1954). Utility analysis and the consumption function: An interpretation of cross-
section data. Franco Modigliani, 1(1):388–436.
Nadaraya, E. A. (1964). On estimating regression. Theory of Probability & Its Applications, 9(1):141–142.
39

Overton, W. S. and Stehman, S. V . (1995). The horvitz-thompson theorem as a unifying perspective for probability
sampling: with examples from natural resource sampling. The American Statistician, 49(3):261–268.
Panaretos, V . M. and Zemel, Y . (2019). Statistical aspects of wasserstein distances. Annual Review of Statistics and
Its Application, 6:405–431.
Panaretos, V . M. and Zemel, Y . (2020).An invitation to statistics in Wasserstein space. Springer Nature.
Powell, J. L. and Stoker, T. M. (1996). Optimal bandwidth choice for density-weighted averages. Journal of Econo-
metrics, 75(2):291–316.
Prelec, D. and Simester, D. (2001). Always leave home without it: A further investigation of the credit-card effect on
willingness to pay. Marketing letters, 12:5–12.
Raghubir, P. and Srivastava, J. (2008). Monopoly money: the e ffect of payment coupling and form on spending
behavior. Journal of experimental psychology: Applied, 14(3):213.
Ramsay, J. O. and Silverman, B. W. (2005). Fitting differential equations to functional data: Principal di fferential
analysis. Springer.
Rosenbaum, P. R. and Rubin, D. B. (1983). The central role of the propensity score in observational studies for causal
effects. Biometrika, 70(1):41–55.
Rubin, D. B. (1978). Bayesian inference for causal effects: The role of randomization. The Annals of Statistics, pages
34–58.
Rubin, D. B. (2005). Causal inference using potential outcomes: Design, modeling, decisions. Journal of the Ameri-
can Statistical Association, 100(469):322–331.
Silverman, B. W. (2018). Density estimation for statistics and data analysis. Routledge.
Soman, D. and Cheema, A. (2002). The e ffect of credit on spending decisions: The role of the credit limit and
credibility. Marketing Science, 21(1):32–53.
Spirtes, P. (2010). Introduction to causal inference. Journal of Machine Learning Research, 11(5).
Su, L., Ura, T., and Zhang, Y . (2019). Non-separable models with high-dimensional data. Journal of Econometrics,
212(2):646–677.
Varanasi, M. K. and Aazhang, B. (1989). Parametric generalized gaussian density estimation. The Journal of the
Acoustical Society of America, 86(4):1404–1415.
Verdinelli, I. and Wasserman, L. (2019). Hybrid wasserstein distance and fast distribution clustering. Electronic
Journal of Statistics, 13:5088–5119.
Villani, C. (2021). Topics in optimal transportation, volume 58. American Mathematical Soc.
Watson, G. S. (1964). Smooth regression analysis. Sankhy¯a: The Indian Journal of Statistics, Series A , pages 359–
372.
Wilcox, K., Block, L. G., and Eisenstein, E. M. (2011). Leave home without it? the e ffects of credit card debt and
available credit on spending. Journal of Marketing Research, 48(SPL):S78–S90.
40

Ye, Z., Zhang, Z., Zhang, D., Zhang, H., and Zhang, R. P. (2025). Deep-learning-based causal inference for large-scale
combinatorial experiments: Theory and empirical evidence. Management Science.
41

Appendix A. Causal assumptions
SUTV AAssumption 1.1 assures that the potential outcome of an individual is due to the level of
treatment the individual receives, but not the assignment of treatment to other individuals.
Assumption 1.2 ensures that each treatment level should be clearly characterized. Consider
the case in which we are interested in the effects of taking Aspirin. If the treatment variable
is binary (taking Aspirin or not), then every patient who takes Aspirin should take the same
dose and the same type of Aspirin.
Consistency It assures that the observed outcome is due to the assigned intervention that allows
us to examine the target quantities from the observable data.
Ignorability/Unconfoundness It has two meanings. First, if two individuals have the same X,
then the joint distributions Y(a) conditioning on the covariates X and the treatment assign-
ment of the two individuals are the same. Second, if two individuals have the same X, then
the treatment assignment mechanism should be the same.
Overlap/Positivity It assures that every available combination of treatment and covariate levels
has a positive density.
Appendix B. Di fferences between the Wasserstein Mean and Euclidean Mean
To further illustrate the superiority of the Wasserstein space in preserving the structural prop-
erties of distributions during operations, we present two examples in this section. Specifically, we
examine the averaging of finite samples of probability distributions in the following contexts: (1)
Gaussian samples; and (2) Exponential samples.
Example 1: Gaussian samples: Consider the case in which Y is a random variable such that
each realization is a normal distributionN(λ, 1), whereλ follows a uniform distributionU(a, 1+a).
Denote fλ(u) as the density function ofλ.
The Euclidean mean is the point-wise average of all the distributions, which is equivalent to
42

averaging all the probability density functions. We therefore have
1
1 + a− a
Z 1+a
a
1√
2π
e− (x−u)2 2 fλ(u)du
=
Z 1+a−x
−∞
1√
2π
e− y2 2 dy− Z a−x
−∞
1√
2π
e− y2 2 du
= Φ(1 + a− x)− Φ(a− x),
where Φ(x) =
R x
−∞
1√
2πe− y2 2 dy and Φ(1 + a− x)− Φ(a− x) is a density function.
The Wasserstein mean is a distribution ¯Y = arg min
v∈W2(I)
EP[D2(Y∥v)2]. In the given example, the
distribution that makes EP[D2(Y∥v)2] the smallest is the Gaussian distributionNa + 1 2, 1 which
has the probability density function 1√ 2πe−
(x−a− 1 2 )2
2 .
Example 2: Exponential samples : Consider the case in which Y is a random variable such
that each realization is an exponential distribution Exp(λ), where λ is a random variable that fol-
lows a uniform distributionU(a, 1 + a) and a> 0.
The point-wise average of all the distributions is a density function
1
1 + a− a
Z 1+a
a
ue−ux fλ(u)du
=−1 x  (1 + a)e−(1+a)x− ae−ax  − 1 x2 e−ux

 1+a a
= (1 + ax)e−ax− (1 + (1 + a)x)e−(1+a)x
x2 .
The distribution that minimizes EP[D2(Y∥v)2] is the exponential distribution with rateµ, such that
the mean of this distribution, 1 µ, should equal the mean of all exponential distributions Exp( λ)
(λ∼U (a, 1 + a)) which equals
R 1+a
a
1
λdλ = ln 1+a a . Thus, we have 1 µ = ln  1+a a  , implying thatµ =
1
ln( 1+a a ). Therefore, the probability density function of the Wasserstein mean is 1 ln  1+a a  exp  − x ln  1+a a   .
Appendix C. Di fferences between Distributional/Scalar Outcome Framework
The distributional outcome causal framework represents a significant advancement in the field
of causal inference, particularly by addressing scenarios where the outcome for each individual is
a distribution, as opposed to a scalar value. This distinction is crucial because it allows for a more
comprehensive analysis of causal effects in complex data.
43

We perform a comprehensive comparison between the scalar outcome framework and the dis-
tributional outcome framework in Table 1 and Figure C.12. To distinguish the di fferences when
the implementation of the outcome variable is a scalar, we use Y, Y(a), P(·) and Pa(·) to represent
the outcome, the outcome when treatmentA = a, the probability measure of Y, and the probability
measure of Y(a), respectively. Specifically, the main differences can be summarized as three main
points.
• Outcome/Potential outcome variable . In scalar outcome frameworks, the potential out-
come variable Y(a) for a given treatment A = a is represented as a single scalar value. A
scalar value (or a realization of Y( a)) is drawn from a potential outcome distribution Pa(·).
For example, if we consider Pa(·) to follow a normal distributionN(0, 1), then any realiza-
tion of Y( a) would be a single point sampled from this normal distribution. On the other
hand, the distributional outcome framework considers the potential outcome variable Y(a)
as a distribution in itself, rather than a single scalar value. This distribution is sampled from a
high-dimensional potential outcome distributionPa(·). In this context, a realization of Y(a)
is an entire normal distribution, sayN(µ,σ 2). The parameters of this distribution, (µ, logσ)
in this case, might be drawn from a distribution, sayN(0, 1). Consequently, a single sample
in our framework is not just a point but a collection of points. For example, an instance
may obtain a collection of points drawn from N(0.5, 0.25) where (µ, logσ) is drawn from
N(0, 1) and equals (0.5, log 0.5), while another instance may obtain a collection of points
drawn fromN(0.3, 0.16) where (µ, logσ) is drawn from N(0, 1) and equals (0.3, log 0.4).
This conceptual shift is visually depicted in Figure C.12.
• Ambient space of outcome variable (Ω). In the scalar outcome framework, the outcomes
are typically scalar values located within the ambient space of the Euclidean space, denoted
as R. However, our proposed framework considers the responses as distributions rather than
scalar values. In this context, the ambient space for these outcomes is not the Euclidean
space, but rather the Wasserstein space of distributions over a setI, symbolized asW2(I).
• Target quantity. In the scalar outcome framework, the essential components are EPa[Y(a)]
or QPa[α, Y(a)], representing the expected value or the α-quantile value of the response
44

𝑖𝑖th sample 𝑗𝑗th sample
pdf of 𝒴𝒴(𝑎𝑎)pdf of Y(a)
𝑗𝑗th sample𝑖𝑖th sample
Observed
dataset
𝑖𝑖th sample
𝑗𝑗th sample
𝑖𝑖th sample
𝑗𝑗th sample
Classical Causal Framework Proposed Causal Framework
Fig. C.12. Comparisons between the scalar outcome framework and distributional outcome framework. When the
outcome is a scalar, the observed dataset contains a finite number of points. Each point represents a realization of one
unit. When the outcome is a distribution, the observed dataset contains a finite number of collections. Each collection
contains finitely many points, and each collection is a realization of one unit.
when all individuals in a population receive a specific treatment a respectively. The differ-
ence between EPa[Y(a)] and EPa′ [Y(a′)] (or QPa[α, Y(a)] and QPa′[α, Y(a′)]), where a′ rep-
resents an alternative treatment, is often used to quantify ATE and QTE in the population. In
contrast, in the distributional outcome, the outcome of each individual is characterized as a
distribution. The key component in this framework is Θ(a), which represents the Dist-APO
(i.e., quantile function of the barycenter) in the Wasserstein space W2(I) when assuming
that all individuals receive treatment A = a. Furthermore, the di fference between Θ(a) and
Θ(a′), denoted asΘ(aa′), is referred to as the quantile differences of Dist-ATE. This measure
captures the variation in treatment effects in different quantiles of the outcome distribution,
providing a detailed understanding of how treatment e ffects vary across the spectrum of
potential outcome distributions.
Appendix D. Dist-DR and Dist-IPW estimator
Appendix D.1. Dist-DR
The core concept of the Dist-DR form involves treating the distributional outcome variable as
a functional response and modeling a functional relationship among the outcome, the treatment,
45

and the covariates. Based on Assumptions 2 and 3, the Dist-DR form can be derived as follows
Θ(a) = EPa[Y(a)−1] = EP(X)[EPa|P(X)[Y(a)−1|X]]
∗
= EP(X)[EPa|P(X)[Y(a)−1|A = a, X]]
⋆
= EP(X)[EP|P(X)[Y−1|A = a, X]] B EP(X)[m(a; X)]. (D.1)
Here,⋆ follows from Assumption 2, while∗ follows from Assumption 3. This form only requires
estimating m(a; X) = EP|P(X)[Y−1|A = a, X] from the observed data using an appropriate regression
model. We can then construct the Dist-DR estimator, termed ˆΘDR(a), according to the Dist-DR
form given in Eqn. (D.1). This estimator is derived by averaging all N individuals, depending on
the regression of the distributional outcome Y−1 on the treatment and covariate variables ( A, X).
The explicit formulation of the Dist-DR estimator is encapsulated in the following equation:
ˆΘDR(a) = 1 N NX i=1 m(a; Xi). (D.2)
However, a potential limitation of the Dist-DR form is that it overlooks the potential influence
of the covariates X on the treatment variable A. Thus, the corresponding estimator is highly
dependent on the accurate estimation of the regression function. The results could be biased if
the functional relationship between variables is misspecified. As such, we consider to express
EPa[Y−1(a)] in other forms.
Appendix D.2. Dist-IPW
The Dist-IPW form is an alternative approach to estimate the Dist-APO Θ(a) according to
the Horvitz–Thompson Theorem (Horvitz and Thompson, 1952, Overton and Stehman, 1995).
The essence of the Dist-IPW form lies in the creation of a pseudo-population from the observed
dataset by assigning specific weights to each unit. These weights are strategically designed to
balance the representation of various groups within the dataset, mirroring the conditions of an
RCT. In this pseudo-population, groups with a smaller portion in the observed dataset are assigned
larger weights, while groups with a larger portion receive smaller weights. The calculation of
these weights involves the use of (generalized) propensity scores that quantify the likelihood that
an individual will receive a particular treatment based on its covariates. The formulation of the
Dist-IPW form is presented in Proposition 4.
46

Proposition 4. Given that Assumptions 1 - 4 hold,
Θ(a) = E(P(A),P(X),P)
δ(A− a)
p(a|X) Y−1

. (D.3)
The detailed proof of the Dist-IPW form is provided in Appendix Appendix F.2. A primary
advantage of Dist-IPW is that it does not require modeling the distributional outcome as a function
of treatment and covariates. Instead, it focuses on modeling the process of treatment assignment,
which can offer greater robustness against model misspecification compared to the Dist-DR form.
However, the Dist-IPW form can be susceptible to issues of high variance. This situation typically
arises in instances where certain subjects in the study have exceptionally low or high propensity
scores. Such extremities in propensity scores result in the assignment of extreme weights to these
subjects in the pseudo-population. The consequence of these extreme weights is an increased
variance in the estimates derived from the Dist-IPW form.
The construction of estimators based on the Dist-IPW form (i.e., Eqn. (D.3)), denoted as
ˆΘIPW (a), is thus formulated by sample averaging:
ˆΘIPW (a) = 1 N NX i=1 Kh(Ai− a) p(a|Xi) Y−1 i . (D.4)
Appendix E. Kernel Functions
Table E.4 summarizes the common kernel functions of order 2 that exist in the literature.
Appendix F. Proofs of Theorems, Propositions, and Corollaries
Appendix F .1. Proofs of Proposition 1
The proof requires Theorem 2.18 of Villani (2021). We state the theorem here:
Theorem 2. Let λ1(·) and λ2(·) be two cumulative distribution functions defined on I ⊆R of
variables V1 and V2 respectively. Let ¯λ be the joint cumulative distribution function such that
¯λ(s, t) = min{λ1(s),λ 2(t)}, (s, t)∈I×I .
47

Table E.4 Some common kernel functions of order 2 that exist in the literature
Kernel Function K(u) Support
Uniform K(u) = 1 2 |u|≤ 1
Triangular K(u) = (1−| u|) |u|≤ 1
Epanechnikov K(u) = 3 4(1− u2) |u|≤ 1
Quartic K(u) = 15 16(1− u2)2 |u|≤ 1
Triweight K(u) = 35 32(1− u2)3 |u|≤ 1
Tricube K(u) = 70 81(1−| u|3)3 |u|≤ 1
Gaussian K(u) = 1√ 2πe− u2 2 u∈ R
Cosine K(u) = π 4 cosπ 2u |u|≤ 1
Logistic K(u) = 1 eu+2+e−u u∈ R
Sigmoid K(u) = 2 π 1 eu+e−u u∈ R
Then ¯λ∈ Λ(λ1,λ 2) (Λ(λ1,λ 2) is the set containing all the joint distributions which haveλ1 andλ2
as the marginal distributions) and
inf
˜λ∈Λ
Z
I×I
|s− t|2d ˜λ(s, t) =
Z
I×I
|s− t|2d ¯λ(s, t).
Furthermore, we have
Z
I×I
|s− t|2d ¯λ(s, t) =
Z 1
0
|λ−1 1 (t)−λ−1 2 (t)|2dt
For the detailed proof, please refer to Villani (2021).
Proof 1. Proof of Assertion 1: Our goal is proving EPa
Y(a)−1 = ¯Y−1(a). Let Q be the set
containing all the left-continuous non-decreasing functions on (0, 1). If we viewQ as a subspace
ofL2([0, 1];λ) whereλ represents the Lebesgue measure, then it is isometric toW2(I) (e.g., see
Panaretos and Zemel (2020)). Indeed,µa = arg min
ν∈W2(I)
EPa
D2(Y(a),ν )2 • = arg min
ν∈Q
EPa
R 1
0|Y(a)−1(t)−
ν−1(t)|2dt. Here, • = follows from Theorem 2.18 of Villani (2021). Since we can interchange the
48

integral sign
R
and EPa, we notice that
EPa
Z 1
0
|Y(a)−1(t)−ν−1(t)|2dt
=
Z 1
0
EPa
|Y(a)−1(t)−ν−1(t)|2dt
=
Z 1
0
EPa
|Y(a)−1(t)− EPa Y(a)−1(t) + EPa Y(a)−1(t)−ν−1(t)|2dt
=
Z 1
0
(EPa
Y(a)−1(t)−ν−1(t))2dt
+ 2
Z 1
0
(EPa[(EPa
Y(a)−1(t)− Y(a)−1(t))])× (EPa Y(a)−1(t)−ν−1(t))dt
+
Z 1
0
EPa[(EPa
Y(a)−1(t)− Y(a)−1(t))2]dt
‡
=
Z 1
0
(EPa
Y(a)−1(t)−ν−1(t))2dt + Z 1
0
EPa[(EPa
Y(a)−1(t)− Y(a)−1(t))2]dt.
‡ follows since
EPa[(EPa
Y(a)−1(t)− Y(a)−1(t))] = EPa Y(a)−1(t)− EPa[Y(a)−1(t)] = 0.
Thus, EPa
R 1
0|Y(a)−1(t)−ν−1(t)|2dt attains its minimum when R 1 0 (EPa Y(a)−1(t)−ν−1(t))2dt at-
tains its minimum. Equivalently, we must have
R 1
0 (EPa
Y(a)−1(t)−ν−1(t))2dt = 0, implying that
ν−1(t) = EPa Y(a)−1(t). We can conclude that ¯Y(a) = EPa Y(a)−1−1 ⇒ Θ(a) = ¯Y(a)−1 =
EPa
Y(a)−1.
Appendix F .2. Proofs of Proposition 4
Proof 2. The derivations are as follows:
E(P(A),P(X),P)
δ(A− a)
p(a|X) Y−1

= EP(X)
 1
p(a|X) E(P(A),P)|P(X)[δ(A− a)Y−1|X] 
=EP(X)
 1
p(a|X) EPa|P(X)[Y−1|A = a, X]p(a|X)  = EP(X)[EPa|P(X)[Y−1|A = a, X]]
⋆
=EP(X)[EPa|P(X)[Y(a)−1|A = a, X]] ∗ = EP(X)[EPa|P(X)[Y(a)−1|X]] = EPa[Y(a)−1] = Θ(a).
Again,⋆ is due to Assumption 2 and∗ is due to Assumption 3.
49

Appendix F .3. Proofs of Proposition 2
Proof 3. We have proven that EP(X)[m(a; X)] = Θ (a) in Eqn. (D.1) under given Assumptions.
Additionally, we have proven that E(P(A),P(X),P)

δ(A−a)
p(a|X) Y−1

= Θ(a) in Proposition 4. It su ffices to
prove that E(P(A),P(X),P)

δ(A−a)
p(a|X) m(a; X)

= Θ(a). Indeed, we have
E(P(A),P(X))
δ(A− a)
p(a|X) m(a; X)

= EP(X)
m(a; X)
p(a|X) EP(A)|P(X)[δ(A− a)|X]

=EP(X)
m(a; X)
p(a|X)
Z
¯a∈A
δa(¯a)p(¯a|X)d¯a

= EP(X)
m(a; X)
p(a|X) p(a|X)

= EP(X)[m(a; X)] = Θ(a).
Appendix F .4. Proof of Theorem 1
Before presenting the proofs of Theorem 1, we present two lemmas that are useful in proofing
Theorem 1.
Lemma 1. For G1, G2 ∈ W2(I), G−1 1 , G−1 2 can be treated as elements in L2([0, 1];λ) where
λ here represents the Lebesgue measure. Hence, we can calculate D2(G1, G2) inW2(I) and
∥G−1 1 − G−1 2∥ inL2([0, 1];λ), and conclude that D2(G1, G2) =L2([0, 1];λ).
Lemma 2. Given that ( ˆYi)N i=1 are estimates of(Yi)N i=1. Suppose that ( ˆYi)N i=1 are independent of each
other and the Convergence Assumption 1 holds. Then ( ˆYi)N i=1 and (Yi)N i=1 are inL2([0, 1];λ) and
we have 1 N NP i=1 ∥ ˆY−1 i − Y−1 i ∥2 = OP(α2 N +ν2 N).
Before presenting the proofs of Theorem 1. We restate it here. In addition, the results given in
Theorem 1 focus on ˆΘDML(a), the restated version also incorporates the results related to ˆΘIPW (a).
Theorem 3. Let h → 0, Nh → ∞, and Nh 5 → C ∈ [0,∞). Suppose that p (a|x) ∈ C3 on
A such that the derivatives (including the derivative of 0 order) are uniformly bounded in the
sample space for any x. Furthermore, we assume that EP|P(X)
Y−1|A = a, X∈C 3 in [0, 1]×A
and EP|P(X)
∥Y−1∥|A = a, X∈C 3 inA are uniformly bounded in the sample spaces. For any
w∈{ IPW, DML}, under the convergence assumptions, we have
√
Nh ˆΘw(a)− Θ(a) = √ Nh  PN{φ(A, X, Y)}− Θ(a)  + oP(1), (F.1)
1. whereφ(A, X, Y) :=φ(A, X, Y)(t) = Kh(A=a)Y−1(t) p(a|X) if w = IPW and ρp = o(N− 1 2 );
50

2. where φ(A, X, Y) : = φ(A, X, Y)(t) = Kh(A−a){Y−1(t)−m(a;X)(t)} p(a|X) + m(a; X)(t) if w = DML and
ρmρp = o(N− 1 2 ),ρm = o(1),ρp = o(1).
Additionally, we have that
√
Nh{ ˆΘw(a)− Θ(a)− h2Ba} (F.2a)
converges weakly to a centred Gaussian process inL2([0, 1];λ) such that when w = IPW, we have
Ba =
R
u2K(u)du
2 ×

EP(X)

∂2 aam(a; X) + m(a; X)∂2 aap(a|X) p(a|X) + 2∂am(a; X)∂ap(a|X) p(a|X)  .
On the other hand, when w = DML, we have
Ba =
R
u2K(u)du
2 ×

EP(X)

∂2 aam(a; X) + 2∂am(a; X)∂ap(a|X) p(a|X)  .
Proof 4. [Proof of Theorem 3] We are going to prove the case when the estimators are chosen as
ˆΘw(a), where w∈{ IPW, DML}. We present the proofs for the estimator ˆΘDML(a).
We consider the case whenK = 2 for simplicity; the general case can be proven in a similar
fashion. In the sequel, given that W is a random function of (A, X, Y), we denote PNW = 1 N NP i=1 Wi
and ENW = 1 N NP i=1 E(P(A),P(X),P)[Wi]. Let Z = LY and ˆZ = L ˆY, where LY = Y−1. Write Ri = ˆZi−Zi
and Dk a(x) = ˆmk(a; x)− ˜mk(a; x). Define
ψa = E(P(A),P(X),P)
 Kh(A− a)Z
p(a|X)

− E(P(A),P(X),P)
 Kh(A− a)
p(a|X) − 1	m(a; X)  , (F.3)
ˆψa,k = PNk
 Kh(A− a) ˆZ
ˆpk(a|X)

− PNk
 Kh(A− a)
ˆpk(a|X) − 1	 ˆmk(a; X)  . (F.4)
Hence, we have
ˆΘDML (a) = 1 N (N1 ˆψa,1 + N2 ˆψa,2).
Moreover, since h → 0, W.L.O.G., we assume that h < 1. Hence, we have 0 <
√
h < 1 and
0<
√
Nh
N <
√
N
N = 1√ N . Note that from Eqn. (F.3), we have
ψa = E(P(A),P(X),P)
 Kh(A− a)(Z− m(a; X))
p(a|X)

+ Θ(a).
51

As a result, we have
√
Nh ˆΘDML(a)− Θ(a)
=
√
Nh 1 N (N1 ˆψa,1 + N2 ˆψa,2)−ψa  + √ NhE(P(A),P(X),P)  Kh(A− a)(Z− m(a; X)) p(a|X)  .
We can then decompose
√
Nh 1 N (N1 ˆψa,1 + N2 ˆψa,2)−ψa  into the sum of five terms as follows:
√
Nh 1 N (N1 ˆψa,1 + N2 ˆψa,2)−ψa 
=
√
N
X
k=1,2
Nk
N I +
√
N
X
k=1,2
Nk
N II +
√
N
X
k=1,2
Nk
N III +
√
N
X
k=1,2
Nk
N IV +
√
N
X
k=1,2
Nk
N V,
where
I =
√
h(PNk− ENk)
 Kh(A− a)(Z− ˜mk(a; X))
ˆpk(a|X) − Kh(A− a)(Z− m(a; X)) p(a|X) + ˜mk(a; X)− m(a; X)  ,
II =
√
h(PNk− ENk)

m(a; X) + Kh(A− a)(Z− m(a; X)) p(a|X) 
=
√
h(PNk− ENk)φ(A, X, Y),
III =
√
hENk

Kh(A− a)(Z− m(a; X))× (p(a|X)− ˆpk(a|X)) ˆpk(a|X)p(a|X) 
+
√
hENk

{ ˜mk(a; X)− m(a; X)}× { ˆpk(a|X)− Kh(A− a)} ˆpk(a|X)  ,
IV =
√
hPNk
1− Kh(A− a) ˆpk(a|X) 	{Dk a(X)}  ,
V =
√
hPNk
 Kh(A− a)R
ˆpk(a|X)

.
Define three quantities H 1(A, X, Z), H2(A, X, Z), and H 3(A, X, Z) such that we have H1(A, X, Z) =
Kh(A−a)Z{p(a|X)− ˆpk(a|X)}
ˆpk(a|X)p(a|X) , H2(A, X, Z) = Kh(A− a){ ˆpk(a|X)m(a;X)−p(a|X) ˜mk(a;X)} ˆpk(a|X)p(a|X) , and H3(A, X, Z) = ˜mk(a; X)−
m(a; X). Also, we write H (A, X, Z) = H1(A, X, Z) + H2(A, X, Z) + H3(A, X, Z). It su ffices to show
that I, III, IV, and V are oP(1).
Consider term I. Note that
Kh(A− a)(Z− ˜mk(a; X))
ˆpk(a|X) + ˜mk(a; X)− Kh(A− a)(Z− m(a; X)) p(a|X) − m(a; X)
=H1(A, X, Z) + H2(A, X, Z) + H3(A, X, Z) = H(A, X, Z).
We computeE(P(A),P(X),P)[∥I∥2]. Indeed, it is equal toE(P(A),P(X),P)[∥ √ h(PNk−E(P(A),P(X),P))H∥2]. Now,
52

we can decompose it into the sum of I1 and I2 where
I1 = h N2 k X i∈Dk E(P(A),P(X),P) ∥H(Ai, Xi, Zi)− E(P(A),P(X),P) H(Ai, Xi, Zi)∥2
and
I2 = h N2 k X i, j∈Dk
i, j
E(P(A),P(X),P)
⟨H(Ai, Xi, Zi)− E(P(A),P(X),P) H(Ai, Xi, Zi),
H(A j, X j, Z j)− E(P(A),P(X),P)
H(A j, X j, Z j)⟩.
We first bound I1. Note that, since H−E(P(A),P(X),P)[H] = H1−E(P(A),P(X),P)[H1]+H2−E(P(A),P(X),P)[H2]+
H3− E(P(A),P(X),P)[H3], we have
I1 ≲ h N2 k
3X
p=1
X
i∈Dk
E(P(A),P(X),P)
∥Hp(Ai, Xi, Zi)− E(P(A),P(X),P) Hp(Ai, Xi, Zi)∥2
≲I1−1 + I1−2 + I1−3.
Here, I1− j = h N2 k P i∈Dk E(P(A),P(X),P) ∥H j(Ai, Xi, Zi)∥2 such that j = 1, 2, 3.
We first consider hE(P(A),P(X),P)[∥H1(A, X, Z)∥2]. Note that it is equal to hE(P(A),P(X),P)

Kh(A−a)2
 Z{p(a|X)− ˆpk(a|X)} ˆpk(a|X)p(a|X)  2  .
Our next objective is showing that the quantity is bounded above by chEP(X)[

p(a|x)− ˆpk(a|X)

 2 EP(A),P|P(X))[Kh(A−
a)2∥Z∥2|X]] for some constant c. Although Z = Y−1 is a function, ∥Z∥ is a scalar. Hence,
EP|P(X)[∥Z∥2|A = a, X] can be treated as a function of a. Hence, we may express
EP|P(X)
∥Z∥2| A = a + uh, X
=EP|P(X)
∥Z∥2| A = a, X +∂aEP|P(X) ∥Z∥2| A = a, Xuh + ∂2 aaEP|P(X) ∥Z∥2| A = a, Xu2h2 2 + OP(h3).
Further, since
p(a + uh|X) = p(a|X) +∂ap(a|X)uh + ∂2 aap(a|X)u2h2 2 + OP(h3),
53

we have
EP(A),P|P(X)[Kh(A− a)2∥Z∥2|X]
=
Z
EP|P(X)[Kh(A− a)2∥Z∥2|A = s, X]p(s|X)ds
= 1 h Z K(u)2du  EP|P(X) ∥Z∥2|A = a, Xp(a|X)
+ h2
h
Z
K(u)2u2 du  ×

EP|P(X)
∥Z∥2|A = a, X∂2 aap(a|X) 2 +∂aEP|P(X) ∥Z∥2|A = a, X∂ap(a|X)
+ ∂2 aaEP|P(X) ∥Z∥2|A = a, X 2 p(a|X)  +OP(h2).
Hence, we have
hE(P(A),P(X),P)
∥H1(A, X, Z)∥2 
≲hEP(X)


p(a|X)− ˆpk(a|X)

2 × EP(A),P|P(X) Kh(A− a)2∥Z∥2|X
=
Z
K(u)2du× I1−1a + h2(
Z
K(u)2u2 du)(I1−1b + I1−1c + I1−1d) + O(h3).
where
I1−1a =EP(X)


p(a|X)− ˆpk(a|X)

2 × EP|P(X) ∥Z∥2|A = a, Xp(a|X)  ,
I1−1b =EP(X)


p(a|x)− ˆpk(a|X)

2 × EP|P(X) ∥Z∥2|A = a, X∂2 aap(a|X) 2  ,
I1−1c =EP(X)


p(a|x)− ˆpk(a|X)

2 ×∂aEP|P(X) ∥Z∥2|A = a, X∂ap(a|X)  ,
I1−1d =EP(X)


p(a|x)− ˆpk(a|X)

2 × ∂2 aaEP|P(X) ∥Z∥2|A = a, X 2 p(a|X)  .
We find the bounds of I1−1a, I1−1b, I1−1c, and I1−1d. Note that, according to the given conditions,
we have
I1−1a, I1−1b, I1−1c, I1−1d
≲ EP(X)[|p(a|X)− ˆpk(a|X)|2]≤ (EP(X)[|p(a|X)− ˆpk(a|X)|4]) 1 2≤ρ2 p.
As a result, we conclude that
I1−1 ≲ EP(X)[|p(a|X)− ˆpk(a|X)|2] + O(h3)≤ (1 + h2)ρ2 p + O(h3)).
54

We therefore have
I1−1 = O
 1
Nk
ρ2 p + h2 Nk ρ2 p + h3  .
We bound I1−2. To start with, we consider hE(P(A),P(X),P)
∥H2(A, X, Z)∥2 , and we have
hE(P(A),P(X),P)
∥H2(A, X, Z)∥2 
=hE(P(A),P(X))

Kh(A− a)2×
 ˆpk(a|X)m(a; X)− p(a|X) ˜mk(a; X) ˆpk(a|X)p(a|X)  2 
≤chEP(X)
 ˆpk(a|X)m(a; X)− p(a|X)m(a; X) 2 × EP(A)|P(X)[Kh(A− a)2|X]
+ chEP(X)
p(a|X)m(a; X)− p(a|X) ˜mk(a; X) 2 × EP(A)|P(X)[Kh(A− a)2|X].
Standard algebraic derivations also give thatEP(A)|P(X)[Kh(A−a)2|X] =
R
K(u)2du  p(a|X)
h +
R
u2K(u)2du  ∂2 aa p(a|X)h
2 +
OP(h2). Thus, we have
hE(P(A),P(X),P)
∥H2(A, X, Z)∥2 
≤ cEP(X)
 ˆpk(a|X)m(a; X)− p(a|X)m(a; X) 2 × Z K(u)2du  p(a|X) 
+ ch2EP(X)

∥ ˆpk(a|X)m(a; X)− p(a|X)m(a; X)∥2×
R
u2K(u)2du

∂2 aap(a|X)
2

+ cEP(X)

∥p(a|X)m(a; X)− p(a|X) ˜mk(a; X)∥2× Z K(u)2du  p(a|X) 
+ ch2EP(X)
p(a|X)m(a; X)− p(a|X) ˜mk(a; X) 2 ×
R
u2K(u)2du

∂2 aap(a|X)
2

+ O(h3).
Therefore, we have
I1−2 ≲ 1 + h2 Nk EP(X) | ˆpk(a|X)− p(a|X)|2 + 1 + h2 Nk EP(X)[∥m(a; X)− ˜mk(a; X)∥2] + O(h3)
≤ 1 + h2
Nk
(EP(X)
| ˆpk(a|X)− p(a|X)|4) 1 2 + 1 + h2
Nk
(EP(X)[∥m(a; X)− ˜mk(a; X)∥4]) 1 2 + O(h3).
Thus, we have
I1−2 = O
1 + h2
Nk
ρ2 p + 1 + h2 Nk ρ2 m + h3  .
We now bound I1−3. Note that
hE(P(A),P(X),P)
∥H3(A, X, Z)∥2 ≲ hE∥ ˜mk(a; X)− m(a; X)∥2,
55

we therefore have
I1−3 ≲ h Nk EP(X)  ˜mk(a; X)− m(a; X) 2 ≤ h Nk ρ2 m.
Thus, we have I1−3 = O

h
Nk ρ2 m

.
Next, we bound I2. Define
G(A, X, Z) := Kh(A− a){Z− ˜mk(a; X)} ˆpk(a|X) + ˜mk(a; X)− m(a; X)
F(A, X, Z) :=− Kh(A− a){Z− m(a; X)} p(a|X) .
We notice that H(A, X, Z) = G(A, X, Z) + F(A, X, Z). In addition, we denote
γw = E(P(A),P(X),P)[w(A, X, Z)],
γw k = E(P(A),P(X),P)[w(Ak, Xk, Zk)],
wk = w(Ak, Xk, Zk)
for w∈{ G, F, H}. As a result, we have

E(P(A),P(X),P)⟨Hi−γH i , H j−γH j⟩

≤

E(P(A),P(X),P)⟨Gi, G j⟩−⟨ γG i ,γ G j⟩

 +

E(P(A),P(X),P)⟨Gi, F j⟩−⟨ γG i ,γ F j⟩

+

E(P(A),P(X),P)⟨G j, Fi⟩−⟨ γG j,γ F i⟩

 +

E(P(A),P(X),P)⟨Fi, F j⟩−⟨ γF i ,γ F j⟩

.
Consider|E(P(A),P(X),P)⟨Gi, G j⟩−⟨ γG i ,γ G j⟩|. We have

E(P(A),P(X),P)⟨Gi, G j⟩−⟨ γG i ,γ G j⟩

≤|E(P(A),P(X),P)⟨Gi, G j⟩| +|⟨γG i ,γ G j⟩| ⋄ ≤∥γG i∥∥γG j∥ +∥γG i∥∥γG j∥ = 2∥γG∥2.
⋄
= holds by using the Cauchy Schwartz inequality and the fact that (Ai, Xi, Zi) and (A j, X j, Z j) are
independent of each other. Similarly, we have

E(P(A),P(X),P)⟨Gi, F j⟩−⟨ γG i ,γ F j⟩

≤ 2∥γG∥∥γF∥,

E(P(A),P(X),P)⟨Fi, G j⟩−⟨ γF i ,γ G j⟩

≤ 2∥γF∥∥γG∥,
and

E(P(A),P(X),P)⟨Fi, F j⟩−⟨ γF i ,γ F j⟩

≤ 2∥γF∥2.
56

Thus, we have

E(P(A),P(X),P)⟨Hi−γH i , H j−γH j⟩

≤ 2∥γG∥2 + 2∥γF∥2 + 4∥γF∥∥γG∥ = 2∥γG∥ +∥γF∥2 ≲∥γG∥2 +∥γF∥2.
Note that
∥E(P(A),P(X),P)[G(A, X, Z)]∥
=∥EP(X)[EP(A),P|P(X)[G(A, X, Z)|X]]∥≤ EP(X)[∥EP(A),P|P(X)[G(A, X, Z)|X]∥],
we have
∥E(P(A),P(X),P)[G(A, X, Z)]∥2
≤ (EP(X)[∥EP(A),P|P(X)[G(A, X, Z)|X]∥])2≤ EP(X)[∥EP(A),P|P(X)[G(A, X, Z)|X]∥2].
It remains to consider∥EP(A),P|P(X)
G(A, X, Z)|X∥ and∥EP(A),P|P(X) F(A, X, Z)|X∥. Now, from the def-
inition of G(A, X, Z), we have
EP(A),P|P(X)
G(A, X, Z)|X
= (m(a; X)− ˜mk(a; X))(p(a|X)− ˆpk(a|X)) ˆpk(a|X)
+ (
Z
u2K(u)du)×
(m(a; X)− ˜mk(a; X))∂2 aap(a|X)h2
2 ˆpk(a|X) + ∂aEP|P(X)[Z|A = a, X]∂ap(a|X)h2 ˆpk(a|X)
+ p(a|x)∂2 aaEP|P(X)[Z|A = a, X]h2
2 ˆpk(a|X)

+OP(h3).
Thus, we have
∥EP(A),P|P(X)
G(A, X, Z)|X∥
≲∥(m(a; X)− ˜mk(a; X))∥|(p(a|X)− ˆpk(a|X))| +∥m(a; X)− ˜mk(a; X)∥|∂2 aap(a|X)|h2
+∥∂aEP|P(X)[Z|A = a, X]∥|∂ap(a|X)|h2 +|p(a|X)|∥∂2 aaEP|P(X)[Z|A = a, X]∥h2 + OP(h3).
Similarly, we have
EP(A),P|P(X)
F(A, X, Z)|X
= (
Z
u2K(u)du)×

− ∂aEP|P(X)[Z|A = a, X]∂ap(a|X)h2
p(a|X) − p(a|X)∂2 aaEP|P(X)[Z|A = a, X]h2 2p(a|X)  + OP(h3)
57

and
∥EP(A),P|P(X)
F(A, X, Z)|X∥
≲∥∂aEP|P(X)[Z|A = a, X]∥|∂ap(a|X)|h2 +|p(a|X)|∥∂2 aaEP|P(X)[Z|A = a, X]∥h2 + OP(h3).
We bound EP(X)[∥EP(A),P|P(X)
G(A, X, Z)|X∥2] and EP(X)[∥EP(A),P|P(X) F(A, X, Z)|X∥2]. Note that
EP(X)[∥EP(A),P|P(X)
G(A, X, Z)|X∥2]
≲ EP(X)[∥(m(a; X)− ˜mk(a; X))∥4] 1 2× EP(X)[|p(a|X)− ˆpk(a|X)|4] 1 2 + O(h4)
and
EP(X)[∥EP(A),P|P(X)
F(A, X, Z)|X∥2] ≲ O(h4).
Hence, we conclude that I 2 = O(hρ2 pρ2 m + h5). Combining all the results, we can conclude that √
N P
k=1,2
Nk
N I = oP(1). Consider∥III∥. We have
∥III∥≤
ENk { ˜mk a(X)− m(a; X)} ˆpk(a|X) × ENk[{ ˆpk(a|X)− Kh(A− a)}|X] 
+
 √ hENk  Kh(A− a)(Z− m(a; X))× (p(a|X)− ˆpk(a|X)) ˆpk(a|X)p(a|X) 
≲
√
h
ENk  { ˜mk(a; X)− m(a; X)}{ ˆpk(a|X)− p(a|X)− h2 2 ∂2 aap(a|X) Z u2K(u)du + OP(h3)}  + h 5 2ρp + O(h 7 2 )
≲
√
hENk
{ ˜mk(a; X)− m(a; X)} ×|{ ˆpk(a|X)− p(a|X)}| 
+
√
hENk
h2
2
{ ˜mk(a; X)− m(a; X)}× ∂2 aap(a|X) Z u2K(u)du   + O(h 7 2 ) + h 5 2ρp
≲
√
h

ENk
 ˜mk(a; X)− m(a; X) 2  1 2 ×  ENk | ˆpk(a|X)− p(a|X)|2  1 2
+
√
h
h2
R
u2K(u)du

2 ×

ENk
 ˜mk(a; X)− m(a; X) 2  1 2 ×  ENk |∂2 aap(a|X)|2 1 2 + O(h 7 2 ) + h 5 2ρp.
We therefore conclude that
III = O(h
5
2ρp + h
1
2ρpρm + h
5
2ρm + h
7
2 ),
and hence
√
N P
k=1,2
Nk
N III = oP(1).
58

Consider the term IV . Note that
∥IV∥2 = IV1 + IV2,
where
IV1 = 1 N2 k X i∈Dk
 1− Kh(Ai− a) ˆpk(a|Xi) 	{Dk a(Xi)}  2
IV2 = 1 N2 k X i, j∈Dk
i, j
⟨1− Kh(Ai− a) ˆpk(a|Xi) 	{Dk a(Xi)},1− Kh(A j− a) ˆpk(a|X j) 	{Dk a(X j)}⟩.
It can be shown that IV1 ≲ 1 Nk P i∈Dk Dk a(Xi)  2 . Besides, we can show that
~ ˆmk(a;·)− ˜mk(a;·)~2 = 1 Nk EP(X) X i∈Dk Dk a(Xi) 2 .
Now, for anyξ >0, using Markov inequality gives
P
 1
Nk
X
i∈Dk
Dk a(Xi) 2 ≥ξ−1~ ˆmk(a;·)− ˜mk(a;·)~2 
≤ξ
1
Nk EP(X)
 P
i∈Dk
Dk a(Xi) 2 
~ ˆmk(a;·)− ˜mk(a;·)~2 =ξ.
Under the Convergence Assumptions, we have
IV1 = OP(~ ˆmk(a;·)− ˜mk(a;·)~2)
= OP(N−2 + N−1ν2 N + N−1α2 N).
For the quantity IV2, we notice that
IV2≤ 1 N2 k X i, j∈Dk
i, j
  1− Kh(Ai− a) ˆpk(a|Xi)  {Dk a(Xi)} ×   1− Kh(A j− a) ˆpk(a|X j)  {Dk a(X j)} 
≤ Nk− 1 Nk 1 Nk X i∈Dk   1− Kh(Ai− a) ˆpk(a|Xi)  {Dk a(Xi)}  2
≤ 1 Nk X i∈Dk   1− Kh(Ai− a) ˆpk(a|Xi)  {Dk a(Xi)}  2 .
59

Similarly, we can show that IV 2 = OP(N−2 + N−1ν2 N + N−1α2 N). Hence, IV = OP(N−1 + N− 1 2νN +
N− 1 2αN) which implies that √ N P
k=1,2
Nk
N IV = oP(1).
Consider the term V . Note that
PNk
 Kh(A− a)R
ˆpk(a|X)

= PNk
 Kh(A− a)R
p(a|X)

+ PNk
 Kh(A− a)R
ˆpk(a|X) − Kh(A− a)R p(a|X)  .
The second term is dominated by the first term since the second term involves the di fference be-
tween the estimated density function ˆpk(a|X) and the true density function p (a|X). Now, we con-
sider the first term and we have
E(P(A),P(X),P)
 1
Nk
NkX
i=1
 Kh(Ai− a)Ri p(a|Xi)  
≤ c Nk NkX i=1 EP(X),P[EP(A)|P(X)[Kh(Ai− a)|Xi]∥Ri∥]
=O(h3) + c  1 Nk NkX i=1 EP(X),P[p(a|Xi)∥Ri∥] + h2 R u2K(u)du 2 1 Nk NkX i=1 EP(X),P[∂2 aap(a|Xi)∥Ri∥] 
≲(1 + h2)  EP  1 Nk NkX i=1 ∥Ri∥2  1 2 + O(h3).
Using Lemma 2 and assumptions on αN andνN, we have V = OP((1 + h2)(α2 N +ν2 N)× √ h +
h3× √ h) which implies that √ N P
k=1,2
Nk
N V = oP(1). As a result, we have
√
Nh ˆΘDML (a)− Θ(a)
=
√
Nh
(
(PN− EN){φ(A, X, Y)} + EN
 Kh(A− a)(LY− m(a; X))
p(a|X)
)
+oP(1).
Thus, we can rewrite the above equality as follows:
√
Nh

ˆΘDML (a)− Θ(a)− E(P(A),P(X),P)
 Kh(A− a)(Y−1− m(a; X))
p(a|X)

=
√
Nh

(PN− E(P(A),P(X),P))φ(A, X, Y)

+ oP(1).
Now, note that
E(P(A),P(X),P)
 Kh(A− a)(Y−1− m(a; X))
p(a|X)

= EP(X)
 1
p(a|X)× EP(A),P|P(X)[Kh(A− a)(Y−1− m(a; X))|X]  . (F.5)
60

Detailed derivations show that Eqn. (F.5) equals the following quantity:
h2
Z
u2K(u)du  ×

EP(X)

∂aEP|P(X)
Y−1|X, A = a∂ap(a|X) p(a|X)  + EP(X) ∂2 aaEP|P(X) Y−1|X, A = a 2  + O(h3)
=h2
Z
u2K(u)du  ×  EP(X)  ∂am(a; X)∂ap(a|X) p(a|X)  + EP(X) ∂2 aam(a; X) 2  + O(h3).
Finally, by the Central Limit Theorem, we conclude that
√
Nh(PN− E(P(A),P(X),P)){φ(A, X, Y)}
converges weakly to a Gaussian process.
For the case when w= IPW, following the above derivations by setting m(a; X) = 0, ˆmk(a; X) = 0,
and Dk a = 0, we obtain
√
Nh

ˆΘIPW (a)− Θ(a) + E(P(A),P(X),P)
 Kh(A− a)Y−1
p(a|X)

=
√
Nh

(PN− E(P(A),P(X),P)){φ(A, X, Y)}

+ oP(1).
After undergoing detailed derivations, we show that E(P(A),P(X),P)

Kh(A−a)Y−1
p(a|X)

equals the following
quantity:
h2
Z
u2K(u)du  ×  EP(X) m(a; X)∂2 ap(a|X) 2p(a|X)  + EP(X) ∂am(a; X)∂ap(a|X) p(a|X)  +EP(X) ∂2 aam(a; X) 2  + O(h3).
The proof is completed.
Appendix F .5. Proofs of Proposition 3
Proof 5. We first find an equation which relates log p(z(τ0), X) and log p(z(τ1), X). Suppose that
G(·) is a bijective function and differentiable. The proof requires the change of variables in prob-
ability density theorem, i.e., given the variables (Z, X) and the corresponding density function
p(z, x), the density function of (G(Z), X) is p(G(z), x) such that
p(G(z), x) = p(z, x)

det " ∂G(z) ∂z 01×D 0D×1 ID #

 −1
⇒ log p(G(z), x) p(z, x) =− log

det " ∂G(z) ∂z 01×D 0D×1 ID #

.
Write z(τ) = [z(τ), X]⊤. From the integral equation
 z(τ0)
X(τ0)

=
a
X

+
R τ0
τ1
g(z(τ), X,τ ;θ)
0

dτ, the
corresponding differential equation is
∂z(τ)
∂τ =
" ∂z(τ)
∂τ∂X(τ)
∂τ
#
=
"
g(z(τ), X,τ ;θ)
0
#
, whereτ0≤τ≤τ1.
61

Consider ∂ log p(z(τ)) ∂τ = ∂ log p(z(τ),X) ∂τ . Write z(τ +ϵ) = [z(τ +ϵ), X]⊤ = [Tϵ(τ), X]⊤. From the first
principle of derivatives, we have
∂ log p(z(τ))
∂τ = ∂ log p(z(τ), X(τ)) ∂τ
= lim
ϵ→0+
log p(z(τ +ϵ))− log p(z(τ))
ϵ
= lim
ϵ→0+
log p(Tϵ(z(τ)), X)− log p(z(τ), X)
ϵ
= lim
ϵ→0+
− log

det " ∂Tϵ(z(τ)) ∂z(τ) 01×D 0D×1 ID #

ϵ
L’Hôpital
= − lim
ϵ→0+
∂
∂ϵ log

det " ∂Tϵ(z(τ)) ∂z(τ) 01×D 0D×1 ID #

=− lim
ϵ→0+
∂
∂ϵ

det " ∂Tϵ(z(τ)) ∂z(τ) 01×D 0D×1 ID #

det " ∂Tϵ(z(τ)) ∂z(τ) 01×D 0D×1 ID #

=
− lim
ϵ→0+
∂
∂ϵ

det " ∂Tϵ(z(τ)) ∂z(τ) 01×D 0D×1 ID #

 |                                     {z                                     }
bounded
lim
ϵ→0+

det " ∂Tϵ(z(τ)) ∂z(τ) 01×D 0D×1 ID #

 |                                      {z                                      }
1
=− lim
ϵ→0+
∂
∂ϵ

det " ∂Tϵ(z(τ)) ∂z(τ) 01×D 0D×1 ID #

.
Applying the Jacobi’s formula, we have
∂ log p(z(τ))
∂τ
=− lim
ϵ→0+
Tr

adj
" ∂Tϵ(z(τ))
∂z(τ) 01×D
0D×1 ID
#
× ∂ ∂ϵ " ∂Tϵ(z(τ)) ∂z(τ) 01×D 0D×1 ID #
=− Tr

lim
ϵ→0+
adj
" ∂Tϵ(z(τ))
∂z(τ) 01×D
0D×1 ID
#
|                                 {z                                 }
ID
× lim
ϵ→0+
∂
∂ϵ
" ∂Tϵ(z(τ))
∂z(τ) 01×D
0D×1 ID
#
=− lim
ϵ→0+
 ∂
∂ϵ
∂Tϵ(z(t))
∂z(t)

.
62

Applying Taylor series expansion on Tϵ(z(τ)) w.r.t.ϵ and taking the limit, we have
∂ log p(z(τ))
∂τ =− lim ϵ→0+
 ∂
∂ϵ
∂Tϵ(z(τ))
∂z(τ)

=− lim
ϵ→0+
 ∂
∂ϵ
∂
∂z(τ)(z(τ) + ∂z(τ) ∂τ ϵ + O(ϵ2)) 
=− lim
ϵ→0+
 ∂
∂ϵ (1 + ∂g(z(τ), X,τ ;θ) ∂z(τ) ϵ + O(ϵ2)) 
=−∂g(z(τ), X,τ ;θ) ∂z(τ) .
As such, we have
Z τ1
τ0
∂ log p(z(τ))
∂τ dτ =
Z τ1
τ0
−∂g(z(τ), X,τ ;θ) ∂z(τ) dτ
⇒ log p(z(τ1)) p(z(τ0)) = Z τ0 τ1 ∂g(z(τ), X,τ ;θ) ∂z(τ) dτ
⇒ log p(z(τ1), X) p(z(τ0), X) = Z τ0 τ1 ∂g(z(τ), X,τ ;θ) ∂z(τ) dτ.
Appendix G. Bandwidth selection
Since we estimate m(a; X) at 9 quantiles, we haveh∗ = arg min
h
P
s∈{0.1,···,0.9}
[h4[ ˆBa(s)]2 + ˆC(s,s) Nh ]. In
fact, h∗ =
 P
s∈{0.1,···,0.9}
C(s,s)
4N P
s∈{0.1,···,0.9}
(Ba(s))2
 1 5
, where
Ba(s) =
ˆΘb(a)(s)− ˆΘϵb(a)(s)
b2(1−ϵ2) , (G.1a)
C(s, ¯s) = h N NX i=1 ( ˆVi(s)− ¯V(s))( ˆVi( ¯s)− ¯V( ¯s)), (G.1b)
ˆVi = Kh(Ai− a)( ˆY−1 i − ˆm(a; Xi)) ˆf (a|Xi) + ˆm(a; Xi), (G.1c)
¯V = 1 N NX i=1 ˆVi, (G.1d)
ˆ△b a = Kb(Ai− a)( ˆY−1 i − ˆm(a; Xi)) ˆf (a|Xi) + ˆm(a; Xi), (G.1e)
ˆ△ϵb a = Kϵb(Ai− a)( ˆY−1 i − ˆm(a; Xi)) ˆf (a|Xi) + ˆm(a; Xi). (G.1f)
63

Here, we choose ϵ = 0.5∈ [0, 1], b = 2h, h = cσAN−0.2, and σA is the standard deviation of
treatment A. In the settings ϵ = 0.5∈ [0, 1], b = 2h, h = cσAN−0.2, we calculate Ba(s) and C(s, s).
After that, we compute h∗ by
 P
s∈{0.1,···,0.9}
C(s,s)
4N P
s∈{0.1,···,0.9}
(Ba(s))2
 1 5
.
Appendix H. Simulation of Gaussian Process
In this section, we present how to simulate a centered Gaussian process with a specified co-
variance function C(s, t). The simulation process can be decomposed into several steps:
Step 1 Randomly draw M points from [0, 1] where the M points are uniformly distributed.
Step 2 Denote the drawn sample by t1,··· , tM. Compute ˆC = [ ˆCi j]M×M where ˆCi j = C(ti, t j).
Step 3 Perform the Cholesky decomposition (or eigenvalue decomposition if ˆC is not positive
definite) on ˆC such that ˆC = LL⊤.
Step 4 Generate Z fromN(0, IM) such that the size of Z is M× N.
Step 5 Compute Y = LZ. Each column of YM×N represents a simulated centered Gaussian pro-
cess with the specified covariance function.
64
