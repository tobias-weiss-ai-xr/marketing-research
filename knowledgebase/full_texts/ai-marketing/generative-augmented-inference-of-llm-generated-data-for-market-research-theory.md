---
title: 'Generative Augmented Inference of LLM-generated Data for Market Research: Theory and Empirical
  Evidence'
url: https://arxiv.org/abs/2604.14575
category: ai-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Cheng Lu
- Mengxin Wang
- Dennis J. Zhang
- Heng Zhang
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.14575
pages: 74
chars: 212679
fetched_at: '2026-11-08T13:00:05+00:00'
kb_version: 1
---

# Generative Augmented Inference of LLM-generated Data for Market Research: Theory and Empirical Evidence

Generative Augmented Inference of
LLM-generated Data for Market Research:
Theory and Empirical Evidence
Cheng Lu
Olin Business School, Washington University in St. Louis, USA, cheng.lu@wustl.edu
Mengxin Wang
Naveen Jindal School of Management, University of Texas at Dallas, USA, mengxin.wang@utdallas.edu
Dennis J. Zhang
Olin Business School, Washington University in St. Louis, USA, denniszhang@wustl.edu
Heng Zhang
W. P. Carey School of Business, Arizona State University, USA, hengzhang24@asu.edu
Marketing research often relies on parameters estimated from costly human-generated data, such as conjoint
survey responses, purchase decisions, and field experiment outcomes. Recent advances in large language
models (LLMs) and other AI systems offer inexpensive auxiliary data, but introduce a new challenge: AI
outputs are not direct observations of the target outcomes, but could involve high-dimensional representations
with complex and unknown relationships to human labels. Conventional methods leverage AI predictions
as direct proxies for true labels, which can be inefficient or unreliable when this relationship is weak or
misspecified. We propose Generative Augmented Inference (GAI), a general framework that incorporates
AI-generated outputs as informative features for estimating models of human-labeled outcomes. GAI uses
an orthogonal moment construction that enables consistent estimation and valid inference with a flexible,
nonparametric relationship between LLM-generated outputs and human labels. We establish asymptotic
normality and a key dominance result: under random labeling, GAI is optimal within a unified class of debiased
estimators—including human-data-only estimators and state-of-the-art debiasing methods—and delivers strict
improvements under a mild informativeness condition. Even when the labeled sample is not representative of
the target population, an extended variant of GAI still dominates the weighted human-data-only estimator.
Empirically, GAI outperforms benchmarks across diverse marketing research settings. In a conjoint analysis,
it halves estimation error and reduces human labeling requirements by over 75%. In a pricing study, it
consistently outperforms alternative estimators when all methods receive identical auxiliary inputs. In a
health insurance study, it saves over 90% of labels while preserving decision accuracy.
Key words: Large Language Model, Data Augmentation, Causal Inference, Demand Estimation
1. Introduction
Marketing research across virtually every subfield relies on human-generated data that is expensive,
time-consuming, or difficult to collect at scale. Estimating consumer preferences requires conjoint
surveys costing$5–20 per respondent (Green and Srinivasan 1990, Bradlow et al. 2004); calibrating
1
arXiv:2604.14575v3  [cs.LG]  22 Jul 2026

Lu et al.:Generative Augmented Inference
2
demand and choice models depends on transaction records that capture realized demand (Guadagni
and Little 1983, Berry et al. 1993); learning how customers respond heterogeneously to marketing
policies typically requires large-scale customer-level data (Ban and Keskin 2021, Chen et al. 2022,
Lu et al. 2025); and measuring treatment effects demands carefully designed field experiments
(Sahni 2016, Huang et al. 2020). In each case, the cost of obtaining reliable human-generated labels
fundamentally constrains sample sizes and, consequently, the precision of parameter estimates that
inform marketing and business decisions.
The emergence of large language models (LLMs) and AI-based generation systems offers a
potential solution to this data scarcity problem (Brown et al. 2020, OpenAI 2023). AI systems
can generate annotations, simulate survey responses, and produce predictions at costs orders of
magnitude lower than human labeling—often$0.01–0.10 per observation. The digital twin paradigm,
which uses LLM-based simulations of individual decision-makers to generate synthetic behavioral
data, exemplifies this opportunity (Toubia et al. 2025). If AI-generated data could reliably augment
scarce human labels, researchers could achieve the statistical precision of large samples while
collecting only a fraction of the human-labeled observations.
However, realizing these efficiency gains while maintaining valid statistical inference presents a
fundamental challenge for two reasons. First, when AI outputs are intended as noisy substitutes for
human labels, they can differ systematically from human judgments in complex, context-dependent
ways. In our retail pricing application, LLM-based digital twins (Toubia et al. 2025) predict
purchases at a 30% rate when the true rate is 44%—a substantial and systematic bias. Naively
pooling such AI-generated data with human labels would introduce bias that could overwhelm
any efficiency gains, resulting in misleading parameter estimates and invalid confidence intervals.
Second, and more importantly, AI outputs can often be structured auxiliary representations rather
than just noisy labels—they may include reasoning traces, confidence scores, persona descriptions,
or high-dimensional embeddings that are categorically different from the outcome of interest.
This distinction fundamentally reframes the statistical problem: rather than correcting inaccurate
predictions, the goal is to leverage auxiliary information efficiently for valid inference.
Therefore, the core methodological question is:How can AI-generated signals be incorporated
into statistical estimation without requiring them to serve as accurate surrogates for the outcome?
Existing approaches to AI-augmented inference, most notably Prediction-Powered Inference (PPI;
Angelopoulos et al. 2023a,b), utilize AI-predicted labels as noisy proxies of the true outcome. Unlike
the “proxy” view, modern generative AI systems can produce outputs that are categorically different
from the outcomes researchers seek to estimate. This highlights the need for an inferential framework
that does not require AI outputs to function as surrogate labels.

Lu et al.:Generative Augmented Inference
3
0/1
 0.83
[0.12, -0.45, …, 0.79]
discrete
labels
continuous
labels
embeddings
images texts
𝒛
𝑿 𝒚 ෝ𝒈(𝑿, 𝒛)
cross-fitting
𝑤 Ƹ𝑒(𝑿, 𝒛)
𝜓 ≔ 𝑿𝑇[∇𝑏 𝑿𝛽 − 𝒈 𝑿, 𝒛
+ 𝑤 𝑒 𝑿, 𝒛 𝒈 𝑿, 𝒛 − 𝒚 ]
If either 𝒈(∙) or 𝑒(∙) is estimated
accurately, the estimation error of
the other one vanishes.
෠𝛽 recovers parameters in human
DGP with 𝑛-consistency.
human
labels
observed
or not
Abundant AI-Generated
Representations
Feature-Augmented
Nuisance Estimation
T argetParameter Estimation
via Orthogonal Score
features
AI
represen-
tations
Figure 1 GAI incorporates AI outputs as auxiliary features rather than surrogate labels. In contrast to PPI, which
applies corrections at the loss-function level and relies on AI predictions approximating the outcome, GAI embeds
auxiliary signals within a Neyman-orthogonal score function. This construction allows the estimator to leverage
auxiliary data for bias correction and efficiency gains, even when AI representations are biased, or weakly
informative.
We proposeGenerative Augmented Inference(GAI), a framework that resolves this tension
through a conceptual shift: rather than treating AI outputs as proxies for outcomes, we treat
them asinformative featuresthat help predict outcomes (Figure 1). This distinction is subtle but
consequential. Under the proxy view, AI outputs must approximate human labels to be useful; under
the feature view, AI outputs need only beinformativeof human labels to contribute information.
To illustrate, consider an LLM predicting whether a consumer will purchase a product. Under the
proxy view, its prediction substitutes for the true outcome, and the problem is framed as correcting
the bias. Under the feature view, even a biased prediction, together with other AI outputs, can still
be useful if it helps predict actual purchases: a predicted “no” may lower the expected purchase
probability, whereas a predicted “yes” may raise it. GAI exploits the representations as features
rather than requiring the predictions to be accurate proxies of human labels.
Concretely, consider estimating the parameters of a generalized linear model (GLM) from a
dataset where human labels are observed for only a subset of observations, but AI-generated auxiliary
information is available for all observations. The auxiliary information may be an LLM’s binary
purchase prediction, a high-dimensional embedding, unstructured texts, or any other AI-generated
signal—its structure is left deliberately unrestricted. GAI proceeds in two steps:
1. Estimate nuisance functions.Using the labeled subset, we estimate two functions: (i) the
outcome prediction function—the best prediction of human labels given both covariates and AI
outputs, capturing whatever predictive information the AI signal contains about the outcome;
and (ii) thepropensity score—the probability that an observation receives a human label, which
may depend on covariates and AI outputs. These nuisance functions can be estimated using
flexible machine learning methods such as random forests, neural networks, or gradient boosting.

Lu et al.:Generative Augmented Inference
4
2. Construct a bias-corrected estimator.We combine the estimated nuisance functions into a
Neyman-orthogonal score function that integrates information from both labeled and unlabeled
observations. The Neyman orthogonality property (Chernozhukov et al. 2018) ensures that
estimation error in the nuisance functions affects the final parameter estimates only at second
order. This robustness allows researchers to use flexible, data-adaptive methods for nuisance
estimation without compromising the validity of inference on the target parameters.
1.1. Contribution
This paper makes three main contributions to the marketing and business research literature:
1. Problem Formulation and Methodology.We identify that AI-assisted labeling creates a
new statistical regime: AI outputs are not noisy surrogates for human labels, but structured
auxiliary representations that can be leveraged as informative features. This distinction leads to
a different problem formulation, in which AI outputs augment the covariate space rather than
substitute for missing outcomes. Building on this insight, we develop GAI, a unified framework
for AI-augmented estimation in GLMs, where we allow model misspecification. The method
exploits a natural orthogonal moment structure, yielding a principled estimator that supports
valid statistical inference while accommodating the full diversity of modern AI outputs, including
discrete predictions, continuous scores, and high-dimensional or unstructured representations
such as text embeddings. In this way, GAI provides a general statistical framework for integrating
AI-generated signals into classical estimation problems.
2. Theoretical Guarantees.We establish that the GAI estimator is asymptotically normal,
√n-consistent, and admits a closed-form variance expression (Theorem 1). Beyond these standard
asymptotic guarantees, we prove a key dominance property: under random labeling, GAI is
guaranteed to weakly improve upon a unified family of debiased estimators, which includes
human-data-only estimation and PPI-based methods (Theorem 2). Thus, under the random-
labeling conditions of Theorem 2, incorporating AI outputs can never worsen performance relative
to ignoring auxiliary AI data entirely, regardless of how biased or inaccurate those outputs
may be. We further extend the theory tocovariate shift, where the labeled sample need not be
representative of the target population (Section 6): we develop a weighted GAI estimator for a
known density ratio and a doubly robust GAI estimator for an estimated density ratio, each
retaining √n-asymptotic normality for the target parameter. We also prove that the weighted
GAI estimator improves efficiency relative to weighted human-data-only estimation.
We further show that the efficiency gains from GAI admit an interpretable variance decom-
position (Corollary 1). Specifically, variance reduction can arise from three distinct sources:
(i)sample expansion, where auxiliary observations effectively enlarge the sample available for

Lu et al.:Generative Augmented Inference
5
estimation; (ii)representational power of AI, where AI outputs provide richer transformations of
the covariates and help approximate complex conditional expectations even when they contain
no information beyondX; and (iii)extra predictive information from AI, where AI outputs
contain signal about human labels beyond the observed covariates. This decomposition provides
a unified explanation for when and why AI augmentation improves statistical efficiency.
3. Empirical Evidence Across Three Auxiliary Data Regimes.We evaluate GAI across three
real-world business applications spanning core estimation tasks in marketing research. The three
applications span progressively more favorable regimes for existing methods. In vaccine conjoint
analysis, we estimate a logit model using both LLM choice predictions and high-dimensional
embeddings of the model’s reasoning. The LLM achieves only 54% prediction accuracy and
observes no additional information beyond features in the outcome model. In retail pricing, all
estimators receive the same systematically biased digital-twin purchase prediction (Toubia et al.
2025), which contains extra information from persona characteristics. This controlled comparison
isolates the benefit of GAI’s feature-based formulation from the additional reasoning information.
Finally, in health insurance coverage analysis, we use accurate, well-calibrated ML predictions
constructed by the PPI authors, creating a setting particularly favorable to existing methods.
GAI delivers consistent gains across all three regimes, demonstrating robustness to differences
in predictive quality, auxiliary-data format, and information content. Across all settings, GAI
substantially improves point estimation accuracy, maintains near-nominal confidence interval cov-
erage in most configurations without inflating interval width, and reduces required human labels
by 67–90%. The consistency of these results across diverse auxiliary data formats, information
structures, and prediction quality levels demonstrates the broad applicability of the framework.
2. Literature Review
AI and Machine Learning in Marketing Research.Marketing research has increasingly
embraced AI and machine learning methods across a wide range of applications. AI-based algorithms
are now used in pricing (Mikl´ os-Thal and Tucker 2019, Zhang et al. 2021), targeting (Rafieian
and Yoganarasimhan 2021, Iyer and Ke 2024, Lu et al. 2025, Rafieian et al. 2025), personalization
and recommendation (Yoganarasimhan 2020, Xu et al. 2022, Jiang et al. 2026), product design
(Toubia and Netzer 2017, Huang and Luo 2016, Sisodia et al. 2025), and sales coaching (Luo et al.
2021). Beyond these applications, researchers are exploring how AI can enhance or substitute for
traditional data collection approaches. LLMs have shown promise for simulating consumer behavior
in market research tasks (Chen et al. 2023, Wang et al. 2024). The digital twin paradigm, which uses
LLM simulations of individual decision-makers, has emerged as a promising approach for generating
synthetic behavioral data (Toubia et al. 2025). Recent work also explores training open-source

Lu et al.:Generative Augmented Inference
6
LLMs to solve optimization problems (Huang et al. 2025). However, recent studies have identified
important limitations: LLMs may fail to replicate the mechanisms underlying human decisions
and produce data with biases that differ from human behavior (Gui and Toubia 2023, Goli and
Singh 2024, Chen et al. 2025b). Our work contributes to this literature by providing a principled
framework for combining scarce human-labeled data with abundant AI-generated representations
while remaining robust to systematic AI errors.
T ransfer Learning.Classical semi-supervised methods (Nigam et al. 2000, Zhu and Goldberg
2009, Lee et al. 2013, Chakrabortty and Cai 2018) use unlabeled features to improve prediction,
while transfer learning (Pan and Yang 2009, Weiss et al. 2016) addresses distribution shift between
source and target domains, such as leveraging existing knowledge to improve decisions in new
settings (Chen et al. 2025a, Duan et al. 2024) or learning policies robust to environment shifts
between training and deployment (Si et al. 2023). Similar challenges arise in business research:
demand models, pricing algorithms, targeting policies, and operations management require real-
world behavioral data that may be scarce, expensive, or difficult to collect at scale (Bertsimas and
Thiele 2006, Besbes and Muharremoglu 2013, Levi et al. 2015, Kaynar and Siddiq 2023, Xiong and
Pelger 2023, Singhvi et al. 2024, Tang et al. 2025). The AI-augmented estimator (AAE) framework
(Wang et al. 2024) addresses the analogous challenge of combining AI and human data through
parametric debiasing. Our setting is distinct: we have AI-generatedrepresentations(not just labels)
for auxiliary data, and utilize them as features in semi-parametric estimations. GAI can be viewed as
addressing the sim-to-real problem in inference: how to leverage abundant simulated or AI-generated
data flexibly while maintaining valid inference grounded in limited real observations.
Prediction-Powered Inference.Angelopoulos et al. (2023a,b) introduced PPI and PPI++
for constructing valid confidence intervals by leveraging ML predictions on unlabeled data. PPI
uses labeled data to estimate and correct for the bias in predictions, yielding valid inference when
predictions are reasonably accurate proxies for outcomes. A recent concurrent work by Wang et al.
(2025) extends this line of research by fine-tuning LLMs for downstream statistical inference and
applying PPI-based rectification. We show that GAI weakly dominates all estimators in a unified
family of debiased estimators, which includes PPI and PPI++. We compare GAI and PPI-based
methods more comprehensively in Online Appendix A
Neyman Orthogonality and Doubly Robust Estimation.The AI-assisted labeling problem
induces a specific data structure: outcomes are partially missing, but for all observations we
observe structured AI-generated representations that may be high-dimensional, unstructured, or
categorically different from the outcome. This structure is richer than the classical missing-data
setting (Rubin 1976, Little and Rubin 2019), where the researcher observes only covariates for units

Lu et al.:Generative Augmented Inference
7
with missing outcomes. In our setting, the auxiliary signal encodes predictive information about
the latent response that goes beyond what standard covariates provide.
This problem structure naturally admits an orthogonal moment representation. Semiparametric
methods developed for missing outcomes, such as augmented inverse probability weighted (AIPW)
estimators, provide useful conceptual tools (Robins et al. 1994, Robins and Rotnitzky 1995, Hirano
et al. 2003, Bang and Robins 2005). While the resulting GAI score function shares the algebraic form
of AIPW estimators, the role of each component differs substantively. First, the augmentation term
leverages AI-generated representations that encode high-dimensional predictive information about
the latent response, rather than correcting for missing outcomes using observed covariates alone.
Second, our analysis is developed within the double machine learning framework (Chernozhukov
et al. 2018) that has been adopted and extended in recent econometrics and ML research (Kallus
et al. 2024). We provide a clean set of conditions and practical implementation tools such as
cross-fitting, allowing our estimator to achieve valid inference across a broad class of GLMs. Our
contribution is thus not a new semiparametric principle, but rather the recognition that AI-generated
representations create a new estimation regime that is well-suited to orthogonal moment methods,
together with the formal analysis of the estimator’s properties in this context.
An earlier, preliminary version of this work was accepted at the International Conference on
Machine Learning (ICML) (Anonymous 2026). The present manuscript substantially extends
that version by generalizing the dominance theorem to a unified family of debiased estimators,
developing a variance-decomposition result that captures the sources of efficiency gains, extending
the framework to covariate-shift settings, strengthening the comparison with baseline approaches,
providing additional implementation guidance for model selection in nuisance estimation, and
adding a new application that extends the experiment to richer AI data regimes.
3. Problem F ormulation
In this section, we formulate the problem within amisspecified GLMframework and describe the
corresponding data-generating and data-collection processes.
3.1. A Misspecified Generalized Linear Model F ramework and Applications
We consider the following estimation framework: We lety ∈R k denote a human label of interest,
associated with a random feature matrixX ∈ X ⊂Rk×d.y | Xfollows anunknownground truth
distribution. We aim to recover a target parameterβ ∗ ∈ B ⊂Rd , which solves:
β∗ ∈arg min
β∈B
E [ℓ(X,y;β) ] ,(1)
where ℓ(X, y; β) := b(Xβ) − y⊤Xβ denotes a loss function and b(·) : Θ →R is a known twice-
continuously differentiable convex function on an open convex set Θ ⊂R k. We assume that B is an

Lu et al.:Generative Augmented Inference
8
open convex set such that, for some compact set ˘X with X ⊂˘X , it holds thatX β∈ Θ whenever
X ∈ ˘X and β∈ B. Under these conditions, one can verify that β∗ satisfies the first-order condition:
E[∇βℓ(X,y;β ∗)] =E  X⊤ (∇b(Xβ∗)−y )  = 0.(2)
An important special case of our framework is the class of canonical GLMs, which impose a struc-
tured functional form on the conditional distribution ofy | X. In particular, canonical GLMs assume
thaty | Xbelongs to the exponential family, with density f (y | X; b,β ∗) ∝exp  b(Xβ∗)−y ⊤Xβ∗	 .
Under this specification, (1) corresponds to the expected log-likelihood minimization estimator
andX ⊤ (∇b(Xβ∗)−y ) in (2) is the canonical score function. Consequently, our framework covers
canonical GLMs that are widely used in applied modeling pipelines, including:
• Linear regression: k = 1, b(θ) = 1 2 θ2. This corresponds to squared-loss estimation for continuous
outcomes and is the workhorse model in empirical studies, including treatment-effect estimation,
forecasting, and policy evaluation. Note that linear regression, viewed as a special case of GLMs,
requires normal densities conditional onX.
• Logistic Regression and MNL:for k non-baseline classes, b(θ) = log

1 +Pk j=1 exp(θj)  . This is the
standard model for discrete choice among multiple alternatives, which is widely used for multiclass
classification applications, such as text classification, image recognition, and recommendation
systems, where predicted utilities determine selection probabilities among competing options.
Whenk= 1, this reduces to logistic regression.
• Poisson regression: k = 1, b(θ) = exp(θ). This models count outcomes and event rates, with
applications such as demand incidence, click/conversion counts, and arrival processes in computer
systems. Poisson GLMs are standard for modeling event rates in systems monitoring, reliability,
and online experimentation.
While canonical GLMs posit a specific exponential-family form for the conditional distribution
ofy | X, real-world data-generating processes rarely conform exactly to these assumptions. Our
framework explicitly accommodates such deviations by relaxing the exponential-family requirement.
In particular, we impose no restrictions on the true conditional distribution ofy | Xand allow
for an arbitrary, unknown ground-truth relationship. As a result, our approach permits model
misspecification and interprets the target parameter as the best approximation within a selected
GLM class: With a b(·) function from GLM family, (1) seeks a GLM density closest to the ground
truth density in the conditional Kullback–Leibler (KL) divergence, i.e.,
β∗ ∈arg min
β∈B
EX

Ey|X

log
 f ∗(y|X)
f(y|X;b,β)

,
where f ∗(y | X) corresponds to the true, unknown conditional density. Therefore, we broadly view
(1) as abest-in-classestimator, which can be regarded as the best generalized linear representation
of the relationship betweenyandX.

Lu et al.:Generative Augmented Inference
9
3.2. Data Generation and Collection
To estimate the best-in-class parameter β∗, we rely on observed data and an appropriate estimation
procedure. In this section, we describe the available data, the underlying data-generating process,
and the mechanism by which observations are collected.
Consider a dataset D = {Ξi = (Xi, yi, wi, zi)}n i=1 withpartially observablehuman labels. In the
baseline setting (Sections 3–5), the observed data follows the same distribution as the target
population underlying (1). Each data sample is i.i.d. In each sample,X i represent the feature
matrix,y i denote the human label of interest. Due to the substantial cost of human labeling, not
all human labels are observed. We let wi ∈ {0, 1} indicate whether the human labely i is observed.
While human annotations are expensive, AI-generated labels are comparatively low-cost. Therefore,
for each sample we additionally observez i, which denotes AI-generated auxiliary information, whose
structure is left deliberately unrestricted.zmay be structured (e.g., categorical labels, probability
scores, or continuous values), high-dimensional vectors (e.g., embeddings), or unstructured objects
(e.g., texts, images). Given D, we define theprimary(human-labeled) andauxiliary(AI-only)
subsamplesD P ={Ξ i ∈ D:wi = 1},D A ={Ξ i ∈ D:wi = 0}and letn P =|D P|,n A =|D A|.
3.2.1. Human Annotation MechanismWe assume human labels are unobserved at random
conditional on features and AI representations, i.e., w⊥ y | X, z. This assumption is natural when
primary data collection is carefully designed (e.g., random sampling of human annotations). We
define e∗(X, z) = E[w| X, z] > κfor some κ >0. In particular, e∗(X, z) represents the probability
that the actual human label is observed givenXandz. Such a data collection mechanism is common
in practice, as the decision to collect real human labels can be based on observed feature information
and AI-generated signals. For example, practitioners may prioritize human annotation for samples
with specific covariate profiles or for cases where AI-generated predictions exhibit high uncertainty.
3.2.2. AI Generation MechanismThe core idea of our method is simple: we utilizezto
extrapolateyon DA using a principled approach. Given AI-generated auxiliary informationz, we
defineg ∗(X, z) = E[y | X, z], which serves as a key object that we estimate using machine learning
methods in an intermediate step of our method (see Section 4.2). The benefit of introducingzis
twofold. First, the AI signalzmay contain predictive information aboutybeyond what is captured
byX. This can occur when AI outputs are generated using auxiliary information not included
inX, makingzinformative aboutyeven after conditioning onX. Second, even wheny ⊥ z | X,
querying a powerful AI system can produce representationszthat summarize complex patterns
inXrelevant for predictingy. Learningg ∗(X, z) using machine learning methods is often easier
compared with learning E[y | X] in practice. For these two reasons, we can use the estimate of
g∗(X, z) to effectively extrapolateyon DA and the convergence requirement in Assumption 2 is

Lu et al.:Generative Augmented Inference
10
likely to be satisfied. Then, instead of using only DP, we can utilize the entire sample D to estimate
the GLM with provably strong empirical performance. We illustrate with concrete examples below.
Example 1 (y̸⊥z|X: Digital Twin Generation). We tailor this example to the retail
pricing experiment in Section 7.2. Each observation corresponds to an individual–product–price
query. For simplicity, we letX ∈R n×2 denote the primary covariates used in the demand model (an
intercept and price). In practice, there can be other features included inX. LetU ∈R p denote a
vector of individual-level persona and demographic features. In the digital-twin setting, the agent is
trained on each individual’s persona information, so the (unobserved) purchase outcome depends
on both price andU. Concretely, suppose the ground-truth data-generating process is
P(y= 1|X,U) =σ (η∗ 0 +η ∗ 1 price +h(U)) ,(3)
where σ(t) = 1/(1 +e−t) and h(U) is an unknown (possibly high-dimensional) function capturing
heterogeneous baseline propensity to purchase across persona types. The parameter of interest for
the pricing study is thepopulationeffect ofXin a model that conditions only onX(rather than on
U). For instance, the analyst may wish to report price sensitivity under counterfactual population
compositions of persona/demographic groups.
Now suppose we also observe an AI-generated digital-twin label z∈ {0, 1}. Because the digital
twin is constructed usingU, its prediction is also a function of (X , U). For instance, we can model
the twin output as
P(z= 1|X,U) =σ

γ0 +γ 1 price +˜h(U)

,(4)
where ˜h(U) reflects the twin’s learned representation of persona-driven purchase propensity. Under
(3)–(4), both y and z depend on the latent persona vectorU. Clearly, after conditioning onX, the
variables remain correlated sinceUis a common driver of both the true purchase decision and the
twin’s prediction. In this sense,y ̸⊥ z | Xand z providesadditional information beyondXabout y
by acting as a proxy for latent heterogeneity encoded inU.■
Crucially, we note that the notationg ∗(X, z) doesnotpresume thatymust be correlated with
zconditional onX. In fact, our approach allowsyandzto be conditionally independent given
X, which is also a common scenario in AI data-generation schemes. In such cases,g ∗(X, z) =
E[y | X, z] = E[y | X]. Wheng ∗(X, z) = E[y | X], includingzas an argument ing ∗ simply reflects
that AI-generated information may serve as a useful representation for the unknown ground-truth
conditional expectation functionE[y|X], as illustrated in Example 2 in Online Appendix B.
Together, Examples 1 and 2 illustrate two typical AI data-generation schemes in whichy ̸⊥ z | X
andy ⊥ z | X. Regardless of whether such conditional correlation holds, our proposed GAI approach

Lu et al.:Generative Augmented Inference
11
achieves variance reduction whenever the working GLM mean∇b(Xβ∗) deviates from the conditional
mean E[y | X, z] in a direction picked up by the covariates—a mild informativeness/misspecification
condition (Theorem 2(iii)). We analyze the mechanisms formally in Section 5 and theoretically
justify the resulting efficiency gains. We conduct empirical experiments corresponding to these
two examples. Section 7.2 represents the digital twin generation setting described in Example 1,
whereas Section 7.1 represents the off-the-shelf LLM generation setting described in Example 2.
Both experiments yield statistically significant improvements consistent with our theoretical results.
4. Methodology
In this section, we present our proposed methodology, GAI. We first discuss the key challenges in
using both primary and auxiliary data to estimate β∗ (Section 4.1). We formally introduce GAI
in Section 4.2 and discuss practical guidance for empirical implementation in Section 4.3. Unless
noted otherwise, we let ∥·∥ denote the ℓ2-norm for a matrix or a vector. Also, ∥·∥F and ∥·∥∞ are the
Frobenius norm or the ℓ∞-norm of an appropriate object. Furthermore, given a multi-dimensional
functionf, we write∥f∥ Q,2 = (E[∥f∥ 2]) 1/2 .We useλ min(·) to denote the minimum eigenvalue.
4.1. The Challenges
Here we formalize the challenges and discuss alternative methods. The canonical scoreX⊤(∇b(Xβ) −
y) in (2) requires observingy, so it cannot be evaluated on auxiliary observations with w = 0.
Using only the primary sample DP = {Ξi = (Xi, yi, wi,z i) : wi = 1}, the standard estimator bβ P is
the solution to the empirical score equation based on the canonical GLM score:
1
nP
X
i:wi=1
X⊤ i {∇b(Xiβ) −y i}= 0.(5)
We denote by bβ P the primary-only estimator. By construction, this estimator relies exclusively
on the primary sample and is therefore fundamentally constrained by the primary sample size,
which is often small due to the high cost of human data collection. The primary difficulty with this
approach is that it ignores the auxiliary sample completely. We also remark that when e(X, z) is
not a constant and the model is indeed misspecified, it is not difficult to construct examples where
this estimator does not have the desired statistical properties, such as consistency.
An alternative approach that utilizes the entire dataset is to na ¨ ıvely pool the primary (human-
labeled) and auxiliary (AI-generated) observations and directly plug them into the empirical score
equation as if all labels were equally reliable. Specifically, the naive estimator bβNaive is the solution
to the following empirical score equation:
1
nP +n A
( X
i:wi=1
X⊤ i {∇b(Xiβ) −y i}+ X
i:wi=0
X⊤ i {∇b(Xiβ) −z i}
)
= 0.(6)

Lu et al.:Generative Augmented Inference
12
Algorithm 1Generative Augmented Inference
Input:DataD=D P ∪ DA, number of foldsK
1:Randomly partition all dataDintoKfoldsI 1, . . . , IK
2:fork= 1, . . . , Kdo
3:Nuisance estimation:
4:Estimatebe (k)(X,z) using all observations inD \Ik
5:Estimate bg(k)(X,z) using primary observations inD \Ik
6:Compute out-of-sample predictionsbe (k) i , bg(k) i for eachi∈I k
7:end for
8:T arget estimation:
9:Obtain bβby minimizing the norm of the average score across folds:
 1 n KX k=1 X i∈Ik Ψi(be(k), bg(k); bβ)  ⩽inf β∈B  1 n KX k=1 X i∈Ik Ψi(be(k), bg(k);β)  +o P (n−1/2)
10:V ariance estimation:
11:Compute bΨi =Ψ i(be(k), bg(k); bβ) for eachi∈I k, and estimate:
bJ= 1 n
KX
k=1
X
i∈Ik
X⊤ i ∇2b(Xi bβ)Xi, bΣ= bJ−1

1
n
KX
k=1
X
i∈Ik
bΨi bΨ⊤ i
!
bJ−1
12:where bΨi =Ψ i(be(k), bg(k); bβ)
13:return bβ, bΣ
While this procedure leverages a larger sample size, it generally yieldsbiasedestimates when the
AI-generated labels do not coincide with the true human outcomes. Additionally, when the auxiliary
signalztakes forms beyond a label surrogate, the naive pooling formulation is no longer applicable.
4.2. Generative Augmented Inference
To address these challenges, we propose the following score function:
Ψ(Ξ;e,g;β) :=X ⊤

∇b(Xβ)−g(X,z) + w e(X,z) (g(X,z)−y)  .(7)
This proposed score can be viewed as anorthogonalizedversion of the complete-data score: it
replaces the missing labelyby the regression functiong(X , z) and corrects the residual using IPW
through e(X, z). This construction allows auxiliary data (with w = 0) to contribute information
throughg(X , z), even thoughyis unobserved. For brevity, we sometimes suppress the dependency
onXandzine(·) andg(·) when clear from the context.
We now propose the GAI algorithm used to estimate the target parameters β∗. Algorithm 1
summarizes the full procedure. GAI implements a cross-fitted estimation procedure that integrates
human-labeled and AI-augmented data. We begin by partitioning all data D into K folds. For each

Lu et al.:Generative Augmented Inference
13
fold k, the algorithm proceeds in two steps. In step 1, we estimate the nuisance functions via flexible
machine learning methods: the labeling propensity be(k)(X, z) is estimated using all observations not
in fold Ik, while the conditional expectation bg(k)(X, z) is estimated using only primary observations
not in fold Ik (since estimatinggrequires observingy). We then compute out-of-sample predictions
for observations in fold Ik. In step 2, we aggregate the score functions across all folds and obtain
bβ by minimizing the norm of this aggregated score. Finally, we estimate the asymptotic variance
using the sandwich formula from Theorem 1.
GAI enables valid inference under flexible AI-generated data. In Section 5, we provide theoretical
support for GAI and formally analyze how it addresses the aforementioned challenges. Section
7 presents empirical validations of its practical performance. We now turn to implementation
considerations, offering practical guidance for applying GAI in real-world settings.
4.3. Hyperparameter Selection for Nuisance Estimation
Because GAI’s score function satisfies Neyman orthogonality, first-order errors in estimating the
nuisance functionsg(X , z) and e(X, z) do not affect the asymptotic distribution of the estimator bβ
(Chernozhukov et al. 2018). Model selection for the nuisance estimators is therefore not central to
the method’s validity. A reasonable fixed specification is sufficient in most applications.
When abundant data are available, however, practitioners may still wish to tune hyperparameters
to improve finite-sample performance. We propose a nested cross-validation procedure that preserves
the independence structure required for valid inference: within each outer fold k of the cross-fitting
procedure, an inner cross-validation loop selects the best model configuration using only data from
the remaining K− 1 folds, evaluating prediction loss on primary observations in the inner validation
set. This ensures that model selection does not contaminate the out-of-fold predictions used for final
inference. We demonstrate this procedure in the retail pricing experiment (Section 7.2), searching
over 8 configurations spanning three model classes.
5. Theoretical Guarantees
Here we present the theoretical guarantees of GAI: we establish its asymptotic normality and strong
dominance over primary-only estimators, and then analyze the sources of its efficiency improvement.
5.1. Asymptotic Normality
The theoretical properties we discuss here are built upon the following assumptions:
Assumption 1(Regularity). (i) b(·)is twice continuously differentiable with ∇2b(θ) ≻ 0on
Θ; (ii)E[X ⊤X]is positive definite; (iii)∥Cov(y|X,z)∥⩽˜σ 2; (iv)E  ∥y∥2 <∞.

Lu et al.:Generative Augmented Inference
14
Assumption 2(ML Convergence Rate).There existsα(n)↓0andr 1 +r 2 ⩾1/2such that:
∥be(X,z)−e∗(X,z)∥ Q,2 ⩽α(n)/n r1 (8)
∥bg(X,z)−g ∗(X,z)∥ Q,2 ⩽α(n)/n r2 (9)
andsup X,z |be(X,z)−e∗(X,z)| →P 0.
The product rate condition r1 + r2 ⩾ 1/2 is a standard requirement in semiparametric estimation
with machine-learned nuisance functions. Analogous conditions appear in policy learning (Athey and
Wager 2021) and causal inference with random forests (Wager and Athey 2018, Athey et al. 2019).
The condition is easily satisfied when both nuisance estimators converge at rate n−1/4 or faster.
This mild requirement is met by a wide range of modern ML methods under standard smoothness
or sparsity conditions: Lasso and its variants achieve n−1/4 rates in sparse high-dimensional models
(Bickel et al. 2009, B¨ uhlmann and van de Geer 2011); random forests and kernel methods attain
these rates under mild regularity conditions (Wager and Athey 2018); neural networks achieve them
when the target function admits a suitable compositional structure (Farrell et al. 2021); and boosting
methods reach comparable rates under appropriate complexity constraints (Luo and Spindler 2016).
We refer to Chernozhukov et al. (2018) for a thorough discussion. Under these assumptions, our
estimator has the following properties. Define the information matrixJ:=E[X ⊤∇2b(Xβ∗)X].
Theorem 1(Asymptotic Normality).Under Assumptions 1–2,
√n( bβ−β ∗)⇝N(0,Σ GAI) (10)
whereΣ GAI =J −1E[Ψ  Ξ;e ∗,g ∗;β ∗ Ψ  Ξ;e ∗,g ∗;β ∗⊤ ]J−1.
The proof (Online Appendix I.1) proceeds by: (1) establishing score validity and Neyman
orthogonality (Lemma 1) and rates for the empirical scores (Lemma 2); (2) proving consistency via
convexity arguments (Lemma 3); (3) deriving the asymptotic expansion using Donsker theory.
5.2. Efficiency with Uniform Random Sampling
In typical applications, human labels are collected via uniform random sampling—for instance,
randomly selecting respondents for annotation, randomly assigning observations to human review,
or randomly subsampling from a larger dataset. Therefore, we focus on this natural scenario in this
section and adopt the next assumption throughout.
Assumption 3(Uniform Random Sampling). The labeling indicator w is independent of
(X,y,z), so thate ∗(X,z) = P(w= 1) =ρ∈(0,1]is a known constant.

Lu et al.:Generative Augmented Inference
15
Because ρ is known, the propensity need not be estimated for GAI. Therefore, we can set be≡ρ
in Algorithm 1. Under this assumption, we further show that GAI achieves efficiency in a unified
family of debiased estimators, including primary-only (see for example (5)), PPI (Angelopoulos
et al. 2023a), and PPI++ (Angelopoulos et al. 2023b). To this end, for λ∈ [0, 1] andf(X , z) ∈R k,
we define a unified score function
Ψλ,f (Ξ;β) := w ρ X⊤ h ∇b(Xβ)−y  −λ  ∇b(Xβ)−f(X,z) i + 1−w 1−ρ λX ⊤ ∇b(Xβ)−f(X,z)  ,
(11)
and define bβλ,f := arg minβ∈B
PnΨλ,f (·;β) .1
Let us assume thatzcan be partitioned into two parts, i.e.,z= (z P, zO), wherez P ∈R k is
AI-generated prediction ofy, andz O is other information generated by AI, such as reasoning among
others. The unified score function (11) covers a wide range of debiased estimators, distinguished
uniquely by (λ, f). Four estimators of interest are members of this family, as summarized in Table 1.
In particular, primary-only ( λ = 0) discards the prediction term and reduces (11) to the score
w
ρ X⊤(∇b(Xβ) − y). PPI and PPI++ advocate soliciting the AI responsez P as the prediction and
then takef=z P (e.g., see Kreps et al. 2020). PPI and PPI++ differ only in the scalar λ. PPI takes
λ = 1. PPI++ tunes an instance-specific λ to minimize the asymptotic variance. Let us denote it
by λ⋆. GAI takes the value λ = 1−ρ together withf=g ∗, recovering the GAI score (7). That is,
Ψ1−ρ,g∗(Ξ; β) =Ψ(Ξ; e∗, g∗; β). Our main result (Theorem 2) is that GAI attains the unique optimal
asymptotic varianceΣ GAI within this family in the positive-semidefinite (Loewner) order: it weakly
dominates primary-only, PPI, and PPI++ simultaneously in every direction, and strictly dominates
each competitor in every direction along which the competitor’s score correction differs from GAI’s
on a set of positive probability. The optimal variance is unique; the pair ( λ, f) attaining it need not
be, and GAI is its canonical member. For convenience, we defineS:=X ⊤(∇b(Xβ∗) − y) = ζ + π,
withζ:=X ⊤(∇b(Xβ∗)−g ∗),π:=X ⊤(g∗ −y), andg ∗ =E[y|X,z], so thatE[π|X,z] =0.
Theorem 2(Dominance over the Unified F amily). Suppose Assumptions 1 and 3 hold,
with known e≡ρ∈ (0, 1)(so that both labeled and unlabeled units occur), andJ ≻ 0. Also, assume
that bg is LQ,2-consistent, i.e., ∥bg− g∗∥Q,2 = o(1). Consider the family { bβλ,f : λ∈R, f ∈L 2(X, z)}
defined by(11). Then:
(i) Every member is consistent and asymptotically normal for thesame β∗: √n ( bβλ,f −β ∗) ⇝
N (0, Σ(λ, f))withΣ( λ, f) =J −1Ω(λ, f)J −1, whereΩ( λ, f) = E[Ψλ,f (Ξ; β∗)Ψλ,f (Ξ; β∗)⊤]admits,
withh:=λX ⊤(∇b(Xβ∗)−f)andδ:=h−(1−ρ)S, the closed form
Ω(λ,f) =E[SS ⊤] + 1 ρ(1−ρ) E[δδ ⊤] = 1 ρ E  (S−h)(S−h) ⊤ + 1 1−ρ E[hh⊤].(12)
1 It is shown in the proof of Theorem 2 that PnΨλ,f (· ; β) =0has a solution with probability one, so the minimizer
here is well-defined. Alternatively, we can define bβλ,f as any solution that achieves an objective function value less than
inf β∈B
PnΨλ,f (· ; β)  + oP (1/√n). The proof is slightly more complex but follows along the same line as Theorem 1.

Lu et al.:Generative Augmented Inference
16
(ii) Primary-only, PPI, and PPI++ are the members λ = 0;( λ, f) = (1, zP); and( λ, f) = (λ⋆, zP),
respectively, while GAI is the member(λ,f) = (1−ρ,g ∗).
(iii) GAI is the Loewner-minimizer of the family. The optimal score correction ish ⋆ = (1 −ρ )ζ,
attained inside the family byλ= 1−ρ,f=g ∗, and yielding
ΩGAI =E[ζζ ⊤] + 1 ρ E[ππ ⊤].(13)
For every(λ,f), writing the residualr:=λ(∇b(Xβ ∗)−f)−(1−ρ)(∇b(Xβ ∗)−g ∗)∈R k,
Σ(λ,f)−Σ GAI = 1 ρ(1−ρ) J−1 E  (X⊤r)(X⊤r)⊤ J−1 ⪰0,(14)
with equality if and only ifX ⊤r=0almost surely (for GAI,r=0).
(iv) The feasible GAI estimator bβ of Algorithm 1 with be≡ρ is asymptotically equivalent to the oracle
GAI member(1 −ρ, g∗): √n ( bβ−β ∗) ⇝N (0, ΣGAI), so the Loewner dominance in part (iii)
extends to it.
The proof can be found in Online Appendix I.3. Theorem 2 shows that GAI weakly dominates
primary-only, PPI, and PPI++ in the Loewner order, and strictly dominates each whenever the
correspondingX ⊤r ̸=0on a set of positive probability. In general, this condition holds for primary-
only, PPI and PPI++, even in cases wherez=z P. The optimal score function, and henceΩ GAI and
ΣGAI, is unique. This result provides theoretical support for the superior empirical performance of
GAI over other estimators reported in the next section.
It is well-known that estimators based on Neyman-orthogonal score functions are semi-parametric
efficient in many settings, for example, when the loss function model is correctly specified as the
log-likelihood (Van der Vaart 2000, Chernozhukov et al. 2018). However, this is not necessarily true
in our setting due to model misspecification, so the dominance result given above is remarkable.
Theorem 2 establishes a “safe default” property: under random labeling, adopting GAI can never
degrade performance relative to ignoring the AI data entirely, and will strictly improve performance
whenever the AI outputs shift the conditional mean of the outcome in a direction reflected in the
score (the informativeness condition of Theorem 2(iii)). This guarantee is operationally valuable
because it eliminates the risk of “doing worse by trying to use AI data,” which is a real concern
with methods whose performance depends on prediction quality.
5.3. Source of V ariance Reduction
In this part we present deeper insight into why GAI achieves variance reduction. First, we formalize
a decomposition of variance in the following corollary when comparing GAI and primary-only.

Lu et al.:Generative Augmented Inference
17
Estimatorλf
Primary-only (human labels, IPW) 0 —
PPI 1z P
PPI++λ ⋆ (asymptotic-variance/trace minimizer)z P
GAI 1−ρg ∗ =E[y|X,z]
Table 1 Members of the Unified Debiased Estimator Family
Corollary 1(V ariance Decomposition). Under the conditions of Theorem 2, the variance
gain of GAI over primary-only estimation decomposes as:
ΣP −Σ GAI ∝( 1 ρ −1) | {z }
(I) Gain from sample expansion
·
(
E

X⊤

∇b(Xβ∗)−E[y|X]  ∇b(Xβ∗)−E[y|X] ⊤ X 
| {z }
(II) Potential gain from representational power ofz
+E

X⊤

E[y|X]−E[y|X,z]

E[y|X]−E[y|X,z]
⊤
X

| {z }
(III) Gain from extra information fromzgivenX
)
,(15)
whereρ∈(0,1)is the labeling probability of Assumption 3.
We remind readers thatg ∗ = E[y | X, z]. Both terms (II) and (III) in Equation 15 are positive
semidefinite. This decomposition identifies three distinct sources of variance reduction:
Source (I): Sample Expansion.The factor 1 /ρ− 1 captures the variance reduction from expanding
the effective sample size. Primary-only estimation uses only the nP labeled observations, whereas
GAI leverages both labeled and auxiliary observations. If either term (II) or term (III) is positive
definite, then, to leading order, this factor increases as the auxiliary sample grows relative to
the primary sample (i.e., as ρ→ 0), enlarging the variance reduction. This leading-order gain
comes with a finite-sample caveat: driving nA → ∞is counterproductive, since as ρ = nP /n→ 0
the inverse-propensity weight 1 /ρ inflates the Neyman-orthogonality remainder of Lemma 1—a
weak-overlap effect whose control is bottlenecked by nP , the only data informing bg—so the Gaussian
approximation degrades and nA is best chosen at a finite “sweet spot” rather than as large as
possible. Our empirical studies presented in subsequent sections show that in practice this choice is
usually quite robust whenρ∈[0.2,0.8].
Source (II): Representational Power ofz.This term captures the representational power ofzwhen
the ground truth model is mis-specified, meaning ∇b(Xβ∗) ̸= E[y | X]. GAI could achieve variance
reduction even ifzcontains no information beyondX, i.e.,y ⊥ z | X. This occurs because the true
conditional expectation function E[y | X] is unknown and may be highly complex, falling outside
the canonical GLM family. Model misspecification operates here at the level of conditional means:
term (II) is nonzero precisely whenX ⊤ ∇b(Xβ∗) −E [y | X]  ̸=0with positive probability—that
is, when the GLM mean deviates from the true conditional mean in a direction picked up by the

Lu et al.:Generative Augmented Inference
18
covariates, the generic situation under misspecification—and positive definite when this vector is
not almost surely confined to a proper subspace. A nonzero term (II) allows GAI to realize variance
reduction through sample expansion. Beyond this asymptotic improvement, GAI also yields a
gain in finite-sample performance whenz, leveraging its pre-trained knowledge, provides a better
representation ofX. Specifically, if E[y | X] is highly complex, estimating it using only the limited
primary sample is challenging. The auxiliary representationg(X , z) leverageszto capture part of
this complexity, thereby facilitating learning in small samples. For example, in Example 2, directly
estimating P(y|X) from primary data alone is challenging, whereas incorporatingzas an additional
feature allows even a simple logistic regression model to recover P(y|X) effectively. This illustrates
one source of variance reduction achieved by GAI.
Source (III): Extra Information inzGivenX.This term captures the additional predictive power
ofzforybeyond whatXalone provides. It is nonzero precisely whenX ⊤ E[y | X] −E [y | X, z]  ̸=0
with positive probability—that is, whenzshifts the conditionalmeanofybeyond whatXprovides;
conditional dependence betweenyandzgivenXthat appears only in higher moments is not
sufficient—and positive definite when this vector is not almost surely confined to a proper subspace.
This reveals another source of gain: if the auxiliary information provides additional signal about
the outcome, GAI can exploit this through the conditional expectationE[y|X,z].
A decomposition similar to this corollary can be derived for PPI/PPI++, but it is less intuitive,
so we skip it in the paper. Here we highlight the key failure modes for PPI/PPI++: Both methods
choose an inferior directionf=z P. PPI fixes λ = 1 regardless of the quality ofz P; whenz P is a
poor or merely misaligned surrogate forythe residualX ⊤ris large, the penalty (14) is strictly
positive, and PPI caninflatevariance even relative to primary-only. PPI++ repairs this, but only by
shrinking the single scalar λ toward the variance-optimal point of the fixed directionf=z P; it never
alters that direction. Instead, GAI uses the optimalf=g ∗. This is only achievable through a double
machine learning type framework to remove the additional bias through Neyman orthogonality of
the score function and cross-fitting. When additional informationz O is available, this advantage is
amplified: by the argument of Theorem 2, a version of GAI usingf= E[y | X, zP] improves upon
PPI/PPI++, and the full version of GAI further improves on it by focusing on the optimal direction
f=g ∗. In Appendix A, we construct a small and intuitive example in the simple case of mean
estimation to illustrate the advantage of GAI over PPI and PPI++.
Finally, the random selection condition ( e(X, z) = ρ constant) is essential for the dominance
guarantee. In Online Appendix I.8, we provide a constructive example showing that dominance
can fail when the labeling probability e(X, z) depends non-trivially on covariates or AI outputs.
Intuitively, if human labeling is strategically directed toward observations where the outcome is
more predictable (e.g., labeling “easy” cases), the unlabeled observations may contribute noise

Lu et al.:Generative Augmented Inference
19
rather than signal. When labeling is non-random, the unlabeled set may be systematically harder
to predict, and the augmentation term can amplify noise rather than reduce it. The fundamental
issue is that strategic labeling creates a selection effect that can make the labeled sample more
informative per observation than the unlabeled sample, potentially reversing the efficiency ordering.
In practice, the dominance condition is satisfied by simple uniform random selection of human
labels from a dataset whose covariate distribution matches the target population. Section 6 relaxes
this distributional alignment by allowing the labeled source population to differ from the target
population while maintaining dominance over the weighted primary estimator.
6. Extension to Covariate Shift
The analysis so far assumes that the dataset D is drawn from the same population that defines the
target parameter β∗ in (1). In many marketing applications this assumption fails by construction.
The parameter of interest is defined for a broadtargetmarket—all current and prospective customers
of a product, the population a pricing or messaging decision will ultimately affect—yet labeled and
AI-augmented observations are almost never a representative draw from that market. Human labels
are expensive, so they are collected wherever they are accessible: an online survey panel, a single
customer segment, a cohort of early adopters, or a sub-population experiment fielded on whoever
can be recruited. The covariate composition of thissourcesample—its mix of demographics, prior
purchases, price sensitivities—typically differs from that of the target market, so an estimator that
ignores the discrepancy recovers the parameter of the accessible sub-population rather than of the
market the decision is about. This is the classical problem ofcovariate shift, studied extensively in
transfer learning and the broader literature on dataset shift and domain adaptation (Shimodaira
2000, Sugiyama et al. 2012, Qui˜ nonero-Candela et al. 2008); here it interacts with the partial
labeling and AI-augmentation structure of GAI, and this section develops the corresponding theory.
The empirical counterparts in the vaccine conjoint application are reported in Online Appendix E
for the known-density-ratio design and Online Appendix F for the estimated-density-ratio design.
Setup.Let QS and QT denote the source and target populations, respectively, both joint laws of
(X, y, z); we write ES and ET for the corresponding expectations and QS,X, QT,X for the marginal
laws ofX. The dataset is drawn from the accessible source QS, but the parameter of interest is now
defined under the target population,
β∗ T ∈arg min β∈B ET[ℓ(X,y;β) ] ,equivalentlyE T  X⊤ ∇b  Xβ∗ T  −y  = 0,(16)
the target analog of the first-order condition (2). We make two assumptions throughout, stated
here in prose. First,covariate shift only: the conditional law of (y , z) givenXis common to the
source and target populations, which therefore differonlyin the marginal distribution ofX. This

Lu et al.:Generative Augmented Inference
20
is the defining restriction of the covariate-shift setting and guarantees, in particular, that the
AI mechanismg ∗(X, z) = E[y | X, z] is the same function under both populations. Second,strict
overlap:Q T,X is absolutely continuous with respect toQ S,X with a bounded density ratio
r(X) := dQT,X
dQS,X
(X)⩽M <∞Q S-almost surely,
so that every region of the target market is represented in the source sample. Together these two
conditions yield the change-of-measure identity ET[h(X, y, z)] = ES[r(X) h(X, y, z)], which is the
workhorse of the analysis below. As in the no-shift case, we maintain the regularity conditions
of Assumption 1 under QS together with ET[X⊤X] ≻ 0, which identify β∗ T as the unique target
minimizer. Two quantities recur in both subsections below, so for compactness of notation, we
define the target prediction-residual and human-label-noise terms
ζT(X,z) :=X ⊤ ∇b  Xβ∗ T  −g ∗(X,z)  andπ(X,y,z) :=X ⊤(g∗(X,z)−y ) ,(17)
the covariate-shift analogs of ζ and π in Section 5, with β∗ replaced by β∗ T in ζT (π is unchanged).
By construction E[π| X, z] = 0, while ζT is the model-misspecification/AI-representation term that
GAI eliminates on the unlabeled observations.
6.1. Known Density Ratio
When the target covariate distribution is available from external sources—census tabulations,
platform-wide logs, or a stratified sampling design as in Online Appendix E—the density ratio r(X)
is known, and covariate shift is handled by a single change of measure. We retain the partial-labeling
structure of the main paper under the random-labeling design (Assumption 3, with known ρ), and
simply reweight the GAI score byr(X):
Ψw(Ξ;g;β) :=r(X)Ψ(Ξ;ρ,g;β),
whereΨis the GAI score (7) with e≡ρ . The estimator bβw (which we refer to as GAI-W) is computed
exactly as in Algorithm 1, with be(k) ≡ρ and every observation’s score (and Jacobian) multiplied
by the known weight r(Xi); the nuisance bg is cross-fitted on the source primary observations
as before. Because r(X) enters as a fixed multiplier and not through any nuisance, the entire
argument is identical to the no-shift case, with r-reweighting throughout. Consequently, with
JT := ET[X⊤∇2b(Xβ∗ T)X], the weighted GAI estimator is √n-asymptotically normal for the target
parameter β∗ T, requiring only L2-consistency of bg, and it strictly dominates the weighted primary-
only estimator (the solution to P i:w i=1 r(Xi) ∇βℓ(Xi, yi; β) = 0) whenever ρ <1 and the weighted
mean-level residual r(X)X ⊤ ∇b(Xβ∗ T) −E [y | X, z]  is not almost surely confined to a proper
subspace (the dominance condition displayed in Theorem 4)—with the same variance structure as

Lu et al.:Generative Augmented Inference
21
Theorem 1 and Corollary 2 (stated in Online Appendix I.2), the efficiency gain again coming entirely
from eliminating the ζT term (now weighted by r(X)2) on the unlabeled observations while the
irreducible noise π contributes identically to both. We defer the formal combined statement and its
proof to Online Appendix C.2 (Theorem 4). Online Appendix E implements this known-density-ratio
construction in the vaccine conjoint application.
6.2. Doubly Robust Estimation with an Estimated Density Ratio
Outside of designed sampling schemes the density ratio is rarely known and must be estimated,
which is the genuinely new methodological challenge. We work with a natural two-sample design.
The first is a fully labeledsource sample DS = {(Xi, yi, zi)}nS i=1 of i.i.d. draws from QS (the ρ = 1
specialization of the previous subsection). The second is an independenttarget covariate sample
DT = {(Xj, zj)}nT j=1, withX j ∼Q T,X andz j obtained by querying the AI mechanism onX j; the
human labelyis never observed in DT. Such a target covariate sample is realistic precisely when
human labels are not: an experiment elicitingycan be run only on an accessible sub-population, but
the platform already records the covariatesXof its entire user base—the target market—and can
cheaply generate the AI outputzfor each. We study the regime nS, nT → ∞with nS/nT →γ∈ [0,∞ ),
and writer ∗ for the true ratio andbrfor its estimate.
The naive fix—plugging brinto the weighted score br(X)Ψ(Ξ; 1, bg; β) on the source sample—fails,
because it is not Neyman-orthogonal with respect to br: the directional derivative of the population
score in the ratio is ES[∆r(X) ζT(X, z)] ̸= 0 in general (with ∆ r := br−r∗), so under misspecification
first-order error in brcontaminates the estimate of β∗ T and invalidates √nS-inference. The two-sample
structure suggests the remedy. The only role of r(X) in the weighted score is to convert a source
average of the prediction component into a target average; with target covariates in hand, that
component can instead be evaluateddirectlyon DT, with no reweighting at all. This yields the
doubly robust score
ΨDR(g, r;β) := 1 nT
nTX
j=1
X⊤ j (∇b(Xjβ)−g(X j,z j))
| {z }
prediction component (target sample)
+ 1 nS
nSX
i=1
r(Xi)X ⊤ i (g(Xi,z i)−y i)
| {z }
bias correction (source sample)
,(18)
and the estimator bβDR (which we refer to as GAI-DR) as any approximate root ofΨ DR(bg,br; ·). The
prediction component replaces the unobserved target labels by the AI-based predictiong(X j, zj)
and uses no human labels; the bias correction estimates the systematic error of that prediction
from the fully labeled source, transported to the target by the weight r(Xi). The nuisance bg is
cross-fitted on the source sample as in Algorithm 1, while bris trained either on an auxiliary source
fold (e.g., a probabilistic classifier distinguishing source from target covariates, converted by the
standard odds transformation) or on an external sample independent ofD S.

Lu et al.:Generative Augmented Inference
22
The score (18) is Neyman-orthogonal with respect to both nuisances: perturbingg, the change in
the prediction component, −ET[X⊤∆g], is cancelled exactly by the change in the bias correction,
ES[r∗(X)X ⊤∆g] = ET[X⊤∆g], by the change of measure; perturbing r changes the population mean
by ES[∆r(X) π(X, y, z)] = 0 since E[π| X, z] = 0. Crucially, in contrast to the naive plug-in, the
ratio error now multiplies the mean-zero residual π rather than the misspecification term ζT—hence
the estimator is doubly robust, its population mean at β∗ T remaining zero if either nuisance is
correct. Because brenters multiplicatively rather than through an inverse weight, only an L2 rate on
bris needed (no sup-norm condition), and a product-rate condition ∥bg− g∗∥QS,2 ∥br−r∗∥QS,2 of the
usual order suffices; both rates are governed by the source sample size nS, which carries the human
labels and is the binding constraint.
Theorem 3(Asymptotic Normality under Covariate Shift: Estimated Density Ratio).
Under the covariate-shift and overlap conditions above, the rate conditions of Assumption 5
(product-rate conditions on bg and branalogous to Assumption 2; stated in Online Appendix J.2),
andn S/nT →γ∈[0,∞),
√nS  bβDR −β ∗ T  ⇝N  0,Σ DR  ,Σ DR =J −1 T Ωγ J−1 T ,
whereJ T =E T[X⊤∇2b(Xβ∗ T)X]and
Ωγ =γE T

ζT(X,z)ζ T(X,z) ⊤ +E S  r∗(X)2 π(X,y,z)π(X,y,z) ⊤ .
The two terms ofΩ γ correspond to the two independent samples: the first is the sampling
variability of the prediction component over the target sample (carrying the factor γ because
that component averages over nT observations while the normalization is √nS), and the second
is the reweighted irreducible human-label noise from the source—the ρ = 1 analog of the π-term
in the known-ratio case. The proof is in Online Appendix J.2 (Theorem 3). We note that in this
setting there is no natural benchmark for a dominance result that is parallel to Corollary 2 or
Theorem 4, because the primary-data-only (or source-data-only) estimator is biased and there is
no natural rescue to it because the density ratio is unknown. Online Appendix F implements this
estimated-density-ratio approach in the vaccine conjoint application.
7. Experiments
We evaluate GAI across three empirical applications that span materially different auxiliary data
regimes. We deliberately order these applications so that the conditions become progressively
more favorable for PPI-based methods, making GAI’s sustained advantage increasingly difficult
to attribute to any single feature of the data. Moreover, these applications demonstrate GAI’s
relevance to the central estimation problems that marketing researchers face.

Lu et al.:Generative Augmented Inference
23
First, avaccine conjoint analysis(Section 7.1) uses high-dimensional LLM embeddings derived
from near-random predictions (54% accuracy) with no extra information ( y⊥ z | X). This is the
most demanding setting for any augmentation method and illustrates GAI’s unique ability to extract
signal from unstructured AI outputs that PPI-based methods cannot even accept as input. Second, a
retail pricing study(Section 7.2) places all methods on a level playing field: every estimator receives
the same binary AI prediction. Since the digital twin is trained on persona features beyond price,z
provides extra predictive information (y̸⊥z| X), yet GAI’s advantage stems from its methodological
approach, not from a data advantage. We also illustrate the hyperparameter selection procedure
(Section 4.3). Third, ahealth insurance census analysis(Section 7.3) evaluates GAI on PPI’s home
turf: well-calibrated ML predictions with 85% accuracy and extra information ( y̸⊥z| X), using
the dataset and AI representations constructed by the PPI authors themselves.
Evaluation Metrics.Across all three applications, we evaluate each method along two comple-
mentary dimensions:point estimationandinference quality.
1. Point estimation, measured by mean absolute percentage error (MAPE) relative to ground-
truth parametersβ ∗:
MAPE = 100 d
dX
j=1
| bβj −β ∗ j |
|β∗ j |+c ,(19)
where d is the number of parameters. Following prior work (Wang et al. 2024), we set c = 1 in
the conjoint and pricing studies to stabilize ratios when |β∗ j | is close to zero. To be consistent
with Angelopoulos et al. (2023a), we set c = 0 in the census study. MAPE summarizes the
average percentage deviation of the estimated coefficients from their true values, with lower
values indicating more accurate estimation.
2. Inference quality, measured by three complementary metrics: (a)confidence interval coverage—
the empirical frequency with which 95% confidence intervals contain the true parameter value,
where valid inference requires coverage near the nominal 95% level; (b)confidence interval
width—the average width of 95% confidence intervals, where narrower intervals indicate more
precise inference but only if coverage remains valid; and (c)decision errors—cases where inference
leads to incorrect managerial decisions 2.
Benchmark Methods.We compare GAI against four benchmark approaches that represent the
main alternatives available to practitioners:
1. Primary: Maximum likelihood estimation using only human-labeled data, ignoring all AI-
generated information. This approach provides valid inference but may lack precision when
human labels are scarce.
2 We define such errors in two ways: (i) CIs that exclude the true parameter value and whose lower and upper bounds
both indicate the opposite sign of the true effect; and (ii) CIs that exclude the true value but span zero, thereby
leading managers to incorrectly conclude an effect is of the opposite sign or not significant.

Lu et al.:Generative Augmented Inference
24
2. Naive: Maximum likelihood estimation that pools human and AI labels without correction,
treating AI outputs as if they were human labels. This approach is simple but can introduce
substantial bias when AI predictions differ systematically from human judgments.
3. PPI: Prediction-powered inference approach of Angelopoulos et al. (2023a), treating AI outputs
as noisy proxies for outcomes and constructs confidence intervals that adapt to prediction quality.
4. PPI++: A computationally efficient variant of PPI (Angelopoulos et al. 2023b) that tunes a
shrinkage parameter to optimize interval width.
Before presenting the detailed results, we highlight the main empirical findings that emerge
consistently across all three applications. GAI delivers substantial improvements in point estimation
accuracy, reducing MAPE relative to the strongest debiased benchmark (PPI++) by roughly 20–45%
in the vaccine and pricing studies and by 50–80% in the census study. These gains translate into
dramatic label savings: in most applications, GAI with the smallest primary sample outperforms
Primary with the largest. Regarding inference, GAI’s confidence intervals attain coverage at or
above the nominal 95% level in nearly every configuration, whereas PPI++ frequently undercovers
(as low as 83% in the census study). Despite this higher coverage, GAI’s intervals are always better
or at least comparable in width to those of PPI++. Decision quality follows the same pattern—GAI
achieves the lowest decision error rates among methods with valid coverage across all studies,
often by a wide margin. In other words, GAI achieves substantially better coverage and decision
quality without meaningful sacrifice in interval precision. The consistency of these findings across
three diverse applications—spanning different auxiliary data formats, information structures, and
prediction accuracy levels—demonstrates the broad applicability of our approach.
7.1. V accine Conjoint Analysis
This application presents the most demanding test for AI-augmented estimation: the LLM’s discrete
predictions are barely better than a coin flip (54% accuracy), and the AI observes no information
beyond the covariates already in the model ( y⊥ z | X). Any gains must therefore arise from GAI’s
ability to extract useful structure from the AI’s outputs—either discrete labels or high-dimensional
embeddings of the reasoning process. This setting showcases GAI’s capability to leverage AI outputs
in multiple forms, even when PPI-based methods struggle to utilize them effectively.
Conjoint analysis is one of the most widely used methodologies in marketing research, providing
the foundation for product design, pricing, and positioning decisions (Green and Srinivasan 1990,
Louviere et al. 2000, Bradlow et al. 2004). Respondents repeatedly choose among product alternatives
described by attribute bundles, and researchers infer the underlying part-worth utilities governing
these choices. However, conjoint studies can be expensive to administer, while the precision of
part-worth estimates depends directly on sample size. This application explores whether flexible
AI-generated outputs can augment scarce human responses to improve preference estimation.

Lu et al.:Generative Augmented Inference
25
Data.Following Wang et al. (2024), we utilize a vaccine conjoint experiment dataset with
1,971 respondents from Kreps et al. (2020). Each task presents two hypothetical vaccines with 11
attributes and lets respondents select their preferred option. Each respondent was asked to take
five tasks in the survey. We estimate the benchmark “ground truth” parameters β∗ ∈R 11 by fitting
the same logistic choice model to the full human dataset. We exclude respondents who never select
any vaccine option, as many public LLMs are restricted from choosing an opt-out option when
generating auxiliary labels; this exclusion is applied consistently both when constructing β∗ and
when forming experimental subsamples.
AI Representations.For each choice task, Wang et al. (2024) prompts LLMs using CoT
reasoning to generate detailed deliberation about the vaccine choice before making a prediction,
recording the decision as labels z∈ {−1, 0, 1} (abstain, option 1, or option 2). 3 We evaluate multiple
auxiliary generators that vary in the underlying model. Across these configurations, we obtain
consistent, qualitatively similar results; for brevity, we report GPT-4o in the main text and defer
the full set of robustness results to Online Appendix D.1.3. We consider two forms of auxiliary
representation: (1)Labels: the discrete choice prediction z∈ {−1, 0, 1}, which can be used by both
GAI and PPI-based methods; and (2)Embeddings: the full LLM response text converted into a
vector representation using OpenAI’s text-embedding-3-large model, yieldingz ∈R 3072 that capture
the semantic content of the LLM’s reasoning. The embedding encodes not just the predicted choice,
but also the underlying reasoning patterns and attribute considerations that the LLM employs.
As explained, GPT-4o achieves low accuracy in this setting, barely better than random guessing
in a binary choice task, and the LLM observes only the same vaccine attributes that compriseX,
which implies y⊥ z | X. Any efficiency gains must therefore arise from GAI’s sample expansion
and representational power (Source (I) and (II) in Corollary 1) rather than from extra information.
PPI-based methods struggle in this setting: while they can use the discrete labels, the low prediction
accuracy limits their effectiveness, and they cannot directly utilize the high-dimensional embeddings.
Experimental Design.We construct repeated experiments by drawing a primary sample of
size nP ∈ {50, 100, 150, 200} and an auxiliary sample of size nA = 1000 from the available task pool. 4
For each (nP , nA) configuration, we run 50 independent trials. Within each trial, the underlying
random draw of observations is held fixed across methods to ensure fair comparison. All reported
statistics are averaged over the 50 trials.
GAI Implementation.We implement GAI with both auxiliary representations using 5-fold cross-
fitting. For GAI (Embeddings), given the high dimensionality of the embedding space ( dz = 3,072),
3 See Wang et al. (2024) for full details on the AI representation construction and replication materials.
4 We randomly sample nP /5 respondents and nA/5 respondents and use all their five choices to compose the primary
set and auxiliary set.

Lu et al.:Generative Augmented Inference
26
Table 2 Benchmark Comparison for Conjoint Analysis: MAPEs, coverage probabilities, and CI widths
(a) MAPE (%) (b) 95% CI Coverage (%) (c) 95% CI Width
Method 50 100 150 200 50 100 150 200 50 100 150 200
Primary 32.02 25.27 19.67 19.01 97.82 92.73 92.55 88.00 2.43 1.51 1.19 1.01
Naive 48.52 45.75 43.33 40.29 26.55 26.36 26.36 27.09 0.56 0.53 0.51 0.49
PPI – 44.57 32.96 29.21 99.82 98.00 95.82 92.91 9.28 2.71 1.94 1.58
PPI++ – 29.69 22.96 21.00 94.55 89.09 90.91 85.09 2.44 1.52 1.19 1.00
GAI (Labels) 16.86 17.52 15.97 16.64 99.82 97.09 94.73 90.91 1.94 1.36 1.11 0.96
GAI (Embeddings) 16.50 17.23 15.73 16.24 99.45 98.55 96.91 94.55 2.11 1.50 1.21 1.05
Notes: A “–” symbol indicates cases where the value exceeds 1,000, which occurs because PPI-based methods can
suffer from singularity problems in small primary samples.
we use strong ℓ2 regularization: logistic regression with ridge penalty (regularization strength
C = 0.01, maximum 2,000 iterations). The embeddings are standardized to zero mean and unit
variance before model training. For GAI (Labels), we use ℓ2-regularized logistic regression with
C = 0.05. In each fold, we fitg(X , z) on four-fifths of the primary data and generate out-of-sample
predictions for the held-out primary fold as well as for all auxiliary observations. This procedure is
repeated across the five folds, and the resulting predictions for each auxiliary observation bg(X, z) are
averaged. Because auxiliary data are never used in training, all predictions for auxiliary observations
are strictly out of sample. Predictions for primary observations are also out of sample by construction
due to cross-fitting. Since primary and auxiliary observations are randomly sampled from the same
underlying population, we setbe(X,z) to the constantn P /(nP +n A).
Under the MNL model, we then estimate bβ by solving a single optimization problem that
minimizes the GAI-adjusted cross-entropy loss:
bβ= arg min
β
1
n
nX
i=1
"
−
JX
j=1
bτij logp ij(β)
#
,
where
bτij = bg(Xi,z i)

1− wi
be

+ wiyij
be , 5 andp ij(β) = exp(X⊤ ijβ) PJ ℓ=1 exp(X⊤ iℓβ) .
This estimator coincides with the general procedure described in Algorithm 1. Finally, we compute
standard errors according to Theorem 1.
Main Results.Table 2 reports estimation accuracy and inference quality across four primary
sample sizes, with results averaged over 50 independent trials.
Point Estimation.The most striking result is the magnitude of GAI’s advantage. Panel (a) shows
that both GAI variants achieve MAPE of 16–17% across all sample sizes—nearly flat, indicating that
both labels and embeddings provide sufficient signal to stabilize estimates even with very few human
5 We clip and normalizebτi to derive well-defined probability for numerical stability.

Lu et al.:Generative Augmented Inference
27
labels. Between the two representations, GAI (Embeddings) achieves consistently lower MAPE than
GAI (Labels) across all sample sizes, suggesting that the richer semantic content in embeddings
provides additional signal for point estimation. By contrast, the Primary estimator ranges from
32% at nP = 50 down to 19% at nP = 200, reflecting its dependence on sample size. The practical
implication is dramatic: GAI with just 50 labels (16.5% MAPE) outperforms Primary with 200 labels
(19.0% MAPE), representing more than 75% reduction in required human annotations. Naive pooling
performs worst (40–49% MAPE), confirming that treating inaccurate LLM predictions as ground-
truth labels is counterproductive. PPI-based methods encounter numerical instability with small
samples (denoted “–” in the table), and when stable, their MAPEs remain substantially above GAI.
Pairedt-tests confirm that all improvements are statistically significant (Online Appendix D.1.1).
Inference Quality.Panels (b) and (c) together reveal that GAI’s estimation gains do not come
at the cost of inference quality—if anything, GAI produces the most reliable confidence intervals.
Coverage (Panel b) shows that GAI (Embeddings) maintains high and stable coverage (94.6–99.5%)—
the highest of all methods for nP ⩾ 100—at or near the nominal level except for a mild dip to 94.6%
at nP = 200, while GAI (Labels) is near-nominal at small samples but undercovers mildly as nP
grows (94.7% at nP = 150 and 90.9% at nP = 200). In contrast, PPI++ undercovers throughout
(85–95%), and Primary drops to 88% at nP = 200. Naive pooling fails (26–27%). Regarding interval
width (Panel c), GAI (Labels) produces the narrowest intervals among valid methods (1.94 at
nP = 50, narrowing to 0.96 at nP = 200). A potential reason why GAI (Labels) yields tighter
intervals than GAI (Embeddings) is that the discrete label has better representational power than
the high-dimensional embeddings. GAI (Embeddings) maintains comparable widths to PPI++,
while PPI produces extremely wide intervals at small samples (9.28 at nP = 50), reflecting overly
conservative inference. This comparison illustrates a trade-off: embeddings yield smaller MAPE and
better coverage while labels achieve narrower intervals, with both GAI variants outperforming PPI-
based methods. Paired t-tests confirm these patterns (Online Appendix D.1.1). In terms of decision
quality, GAI (Embeddings) achieves the lowest decision error rate—averaging 2.6% compared to
6.9% for Primary, 3.2% for PPI, 8.7% for PPI++, and 20.4% for Naive (Online Appendix D.1.2).
The source of GAI’s advantage in this setting is its ability to leverage AI outputs as informative
features. The LLM’s CoT reasoning generates both discrete choice labels and rich text that can be
converted to high-dimensional embeddings. The embeddings capture semantic information about
attribute trade-offs and decision heuristics, yielding superior coverage, while the discrete labels—
despite their simplicity—enable tighter confidence intervals, potentially because they provide a
more direct representation of the outcome structure. Both representations allow GAI to extract
predictive signal without requiring the LLM’s predictions to be accurate surrogates for human
choices. Additional robustness checks across different LLMs are reported in Online Appendix D.1.3.

Lu et al.:Generative Augmented Inference
28
Finally, we mention that GPT-4o’s reasoning power has been surpassed by more recent releases (e.g.,
GPT-5.3 at the time of writing), and new models are coming out frequently with much stronger
reasoning capabilities. As a result, in practical scenarios we suspect that such embedding-based
performance can be even stronger than what is presented in this empirical study.
7.2. Retail Pricing Study
Having established that GAI can extract signal from unstructured, near-random AI outputs, we
now ask a sharper question: when every method receives thesameauxiliary information, does
GAI’s feature-based approach still outperform the surrogate-label strategy of PPI? This application
provides a controlled comparison on a level playing field.
We consider the problem of estimating a logistic demand model that relates purchase decisions
to price. The AI purchase predictions exhibit systematic bias (30% vs. 44% actual purchase rate),
and we restrict all methods to the same binary AI prediction to ensure a fair comparison.
Estimating price sensitivity is a central task in quantitative marketing with demand models, as it
is the key element in pricing decisions, revenue management, and competitive strategy (Berry et al.
1993, Vulcano et al. 2012, Kok and Fisher 2007). However, obtaining reliable purchase data at the
individual level requires costly price experiments or extensive observational data (Guadagni and
Little 1983, Ban and Keskin 2021, Chen et al. 2022). This application demonstrates how GAI can
improve demand estimation by leveraging AI-generated purchase predictions as auxiliary features,
even when these predictions are systematically biased.
Data.We use the data and pricing experiment from Toubia et al. (2025), which contains 2,058
participants who completed over 500 questions spanning diverse domains including demographics,
personality traits, values, and behavioral preferences. Each participant was presented with 40
products at randomized prices and asked to indicate whether they would purchase each item.
We evaluate our methods on all products and observe consistent results. For conciseness, we
report the results of the household cleaning product in the main text and show the comprehensive
performance across products in Online Appendix D.2.3. The outcome model uses only price as the
covariate:X= [1 ,price ] ∈R n×2, yielding a two-parameter logistic regression ( d = 2). The ground-
truth parameters β∗ ∈R 2 are estimated by fitting a logistic regression to the full dataset. The
empirical purchase rate is 44%, and the AI predictions agree with actual outcomes 67% of the time.
AI Representations.The AI purchase labels z∈ {0, 1} are generated by digital twins in Toubia
et al. (2025)—LLM-based simulations of individual participants constructed from their survey
responses.6 For each participant, a persona profile is created by concatenating their answers to the
500+ survey questions, capturing demographics, personality traits, values, and stated preferences.
6 See Toubia et al. (2025) for full details on the AI representation construction and replication materials.

Lu et al.:Generative Augmented Inference
29
Table 3 Benchmark Comparison for Pricing Study: MAPEs, coverage probabilities, and CI widths
(a) MAPE (%) (b) 95% CI Coverage (%) (c) 95% CI Width
Method 100 200 300 400 500 100 200 300 400 500 100 200 300 400 500
Primary 22.36 16.03 12.47 9.59 9.53 95.00 97.00 95.00 99.00 92.00 1.17 0.82 0.66 0.57 0.51
Naive 22.22 21.97 19.99 19.67 19.43 50.00 50.00 50.00 50.00 50.00 0.37 0.35 0.33 0.32 0.31
PPI 26.91 15.31 14.10 13.98 12.88 95.00 98.00 97.00 94.00 96.00 1.40 1.01 0.85 0.75 0.69
PPI++ 22.15 14.16 11.56 9.86 9.66 94.00 99.00 93.00 99.00 92.00 1.10 0.78 0.64 0.55 0.49
GAI 12.43 9.14 8.74 6.57 7.60 100.00 100.00 99.00 100.00 96.00 1.16 0.81 0.65 0.56 0.50
This profile is then provided as context to an LLM, which is prompted to simulate whether that
specific individual would purchase each product at the given price. The AI prediction rate (30.07%)
substantially underestimates the true purchase rate (44.10%), indicating systematic bias. Since the
digital twin is trained on persona and demographic features that are not included in the outcome
model’s covariatesX, the AI prediction carries extra predictive information:y̸⊥z|X.
In our main analysis, we restrict the auxiliary information to the binary AI purchase prediction:
z∈ {0, 1}. This ensures that both GAI and PPI-based methods have access to identical information,
isolating the effect of the estimation strategy. In Online Appendix G, we extend to high-dimensional
auxiliary informationz∈R 115 including persona and demographic features.
Experimental Design.We draw primary samples of size nP ∈ {100, 200, 300, 400, 500} with a
fixed auxiliary sample of nA = 1,000. As in the conjoint study, we run 50 independent trials per
configuration with the same random draw held fixed across methods.
GAI Implementation.We use 5-fold cross-fitting with model selection to estimate the nuisance
functiong(X , z). Since primary and auxiliary observations are randomly sampled from the same
underlying population, we setbe(X, z) to the constantbe=nP /(nP +n A).
Model Selection.This application illustrates the cross-validation procedure described in
Section 4.3. We estimateg(X , z) by searching over 8 configurations spanning three model classes:
regularized logistic regression (GLM with L1/L2 penalties and C∈ {0.01, 0.1}), Random Forest
(depth ∈ {5, 10}), and LightGBM (learning rate ∈ {0.05, 0.1}). Within each of the 5 outer folds, we
perform cross-validation to select the best configuration using only the data from the remaining 4
folds. This nested structure ensures that model selection does not compromise the independence
required for valid inference. Across trials, regularized logistic regression configurations are most
frequently selected (particularly L1-penalized GLM with C = 0.1), followed by Random Forest, with
selection patterns varying by sample size and fold.
Main Results.Results in Table 3 are across five primary sample sizes, averaged over 50 trials.
Point Estimation.Panel (a) confirms that GAI outperforms all benchmarks even when given the
same information. GAI achieves MAPE of 6.6–12.4%, compared to 9.5–22.4% for Primary, 9.7–22.2%
for PPI++, and 12.9–26.9% for PPI. Naive pooling plateaus around 20% regardless of sample

Lu et al.:Generative Augmented Inference
30
Intercept Price
Feature
1.0
0.5
0.0
0.5
Parameter Value
PPI
PPI++
GAI
Ground Truth
Figure 2 Distribution of Estimates (PPI, PPI++, GAI) for Pricing Study (n P = 100)
size, reflecting persistent bias. The label savings remain substantial: GAI with 100 labels (12.4%
MAPE) matches Primary with 300 labels (12.5% MAPE), a 67% reduction in annotation cost. All
improvements are statistically significant by paired t-tests (Online Appendix D.2.1). Consistent
with these accuracy gains, Figure 2 shows that GAI yields parameter estimates that are more
tightly concentrated around the ground truth for both the intercept and price coefficient, whereas
PPI and PPI++ exhibit substantially greater dispersion.
Inference Quality.GAI’s confidence intervals maintain coverage at or above 96% across all
sample sizes (Panel b), reaching 100% at nP ∈ {100, 200, 400}. PPI and PPI++ also maintain
near-nominal coverage (92–99%), while Naive severely undercovers at 50%. Interval widths (Panel c)
are comparable across GAI, Primary, and PPI++, while PPI intervals are noticeably wider. Paired
t-tests indicate that PPI++ achieves modestly narrower intervals in this study, while GAI (Labels)
produces significantly narrower intervals than PPI++ in the conjoint analysis (Table 2); overall, the
two methods generate comparable CI widths with neither consistently dominating. GAI achieves a
0.2% decision error rate, the lowest among methods with valid coverage; Naive’s nominally lower
0.0% rate is an artifact of its severe undercoverage (50%), whose biased but narrow intervals rarely
trigger a sign or significance error (Online Appendix D.2.2).
The key insight from this study is that GAI’s advantage is methodological, not informational. Both
GAI and PPI receive the same covariate vectorX= (1 ,price )⊤ and the same binary AI prediction z.
Yet GAI substantially outperforms PPI-based methods because it models the conditional expectation
g(X, z) = E[y | X, z], extracting information from the AI prediction without assuming it is a noisy
proxy for the outcome. In Online Appendix G, we show that GAI’s advantages extend further when
z∈R 115 includes persona and demographic features. Online Appendix H provides a robustness
check confirming that GAI still outperforms benchmarks even when the AI representation does not
provide extra information beyond the covariates.

Lu et al.:Generative Augmented Inference
31
7.3. Health Insurance Census Analysis
Our final application tests GAI on PPI’s home turf: well-calibrated, continuous AI predictions
with high accuracy, using the dataset and AI representations constructed by the PPI authors
(Angelopoulos et al. 2023a). This is the regime most favorable to PPI-based methods; if GAI holds
up here as well, practitioners need not switch estimators when moving to well-calibrated AI outputs.
Understanding how interventions and individual characteristics predict consumer decisions, such
as insurance coverage and product adoption, is fundamental to marketing research and policy
evaluation (Sahni 2016, Huang et al. 2020, Lu et al. 2025, Rafieian et al. 2025). Although this
application uses observational census data rather than a field experiment, the statistical problem is
representative of the analysis stage in market research where treatment effects are estimated from
costly experimental or observational data (Ascarza et al. 2016, Feit and Berman 2019, Gao et al.
2023, Bojinov et al. 2023).
Data.We use the California census healthcare dataset with 318 ,215 individuals to investigate
the relationship between private health insurance coverage ( y∈ {0, 1}) and income using a logistic
model. Ground truth of logistic regression coefficientsβ ∗ ∈R 2 is estimated using all data.
AI Representations.Auxiliary predictions are produced by Angelopoulos et al. (2023a) using a
gradient boosting classifier trained on a richer feature set including income, race, gender, and other
covariates.7 The model outputs predicted probabilities z = P (y = 1|all features ) with 85% accuracy.
Since the classifier uses features beyond the income covariate inX, the AI prediction provides extra
information:y̸⊥z|X. Unlike the conjoint analysis, this representation is well-calibrated.
GAI Implementation.Because z already represents an accurate estimate of the conditional
mean based on richer features, learning an additionalg(X , z) offers limited benefit. We therefore
setg(X , z) = z directly, and e(X, z) to the constant nP /(nP + nA). This yields a simplified version
of our estimator requiring no first-stage nuisance estimation or cross-fitting.
Experimental Design.We varyn P ∈ {100,250,500,750,1000}withn A = 2000, again running
50 trials per configuration.
Main Results.Table 4 summarizes performance across five primary sample sizes. The most
striking finding is inferential: every other method fails to maintain nominal coverage, yet GAI
attains 99–100% throughout (Panel b). Primary and Naive exhibit severe undercoverage (30–82%),
and PPI++ ranges from 83% to 93%—consistently below the nominal 95% level. Importantly, GAI
achieves this coverage without inflating its intervals: widths are statistically indistinguishable from
PPI++ at every sample size (Panel c; Online Appendix D.3.1). Point estimation tells a similar story
(Panel a): GAI achieves MAPE of 140–161%, while Primary exceeds 290% even at nP = 1,000 and
7 See Angelopoulos et al. (2023a) for full details on the AI representation construction and replication materials.

Lu et al.:Generative Augmented Inference
32
Table 4 Benchmark Comparison for Census Analysis: MAPEs, coverage probabilities, and CI widths
(a) MAPE (%) (b) 95% CI Coverage (%) (c) 95% CI Width (10 −5)
Method 100 250 500 750 1000 100 250 500 750 1000 100 250 500 750 1000
Primary 979.83 563.85 480.99 320.68 291.80 80.00 78.00 78.00 82.00 78.00 2.16 1.31 0.92 0.74 0.65
Naive 407.95 384.70 324.56 263.13 240.38 30.00 31.00 34.00 38.00 38.00 0.61 0.58 0.53 0.49 0.46
PPI 821.83 518.82 383.92 295.40 270.66 88.00 94.00 95.00 96.00 94.00 2.48 1.85 1.29 1.10 0.96
PPI++ 866.27 508.75 404.75 299.52 282.43 83.00 88.00 91.00 93.00 89.00 2.24 1.70 1.24 1.02 0.89
GAI 161.37 147.93 147.38 139.65 141.49 100.00 100.00 100.00 99.00 99.00 2.64 1.79 1.28 1.08 0.93
PPI-based methods remain above 270%. All pairwise MAPE differences are statistically significant
(Online Appendix D.3.1). The label savings are the most dramatic of our three studies—GAI with
100 labels (161%) surpasses Primary with 1,000 labels (292%), a more than 90% reduction. GAI
also achieves zero decision errors across all configurations, compared to 4.8% for Primary, 3.0% for
PPI, 4.2% for PPI++, and 15.8% for Naive (Online Appendix D.3.2).
Taken together, the three applications demonstrate that GAI’s advantages are robust across
auxiliary data regimes: high-dimensional embeddings with y⊥ z | X(conjoint), systematically
biased discrete predictions with y̸⊥z| X(pricing), and well-calibrated continuous probabilities with
y̸⊥z| X(census). Whether the AI output is an embedding, a binary label, or a probability; whether
it carries extra information or not; and whether the prediction is accurate or near-random—GAI
consistently delivers substantial improvements in estimation accuracy and decision quality. It does so
while maintaining valid coverage and comparable interval width to the best-performing benchmark.
Additional implementation details and robustness checks are provided in Online Appendix D.
8. Conclusion
This paper introduces GAI, a framework that enables marketing researchers and practitioners to
use AI-generated data for statistical estimation while preserving inferential validity. The central
insight is conceptual: AI outputs should be treated asinformative featuresfor predicting human-
generated outcomes, rather than assurrogate labelsthat replace them. Formalized through Neyman
orthogonality, this perspective supports valid inference across a wide range of AI output quality,
from systematically biased LLM predictions or reasoning texts to well-calibrated forecasts.
Our theory shows that GAI is asymptotically normal with a closed-form variance expression,
allowing standard confidence intervals and hypothesis tests. More importantly, under random
selection into labeling, GAIdominatesa unified class of debiased estimators—including primary-only
estimation and state-of-the-art debiasing methods—and delivers strict improvements under a mild
informativeness condition (Theorem 2(iii)). In settings where the labeled sample is unrepresentative
of the population of interest, GAI can be extended to improve efficiency relative to weighted primary-
only estimation. These gains arise through three channels: sample expansion, representational power

Lu et al.:Generative Augmented Inference
33
of AI, and extra predictive information from AI. Our empirical results across three applications
provide strong evidence to support these predictions.
GAI helps resolve a core tension in data-driven marketing research: precise estimation requires
large labeled samples, but human-generated ground truth is costly. By combining a limited number
of human labels with abundant AI-generated data, GAI reduces this burden while maintaining
statistical rigor. Across all applications, GAI consistently matches the precision of substantially
larger human-labeled samples, often reducing labeling needs by more than half. Such gains can
translate into substantial cost savings in settings such as conjoint analysis, demand estimation, and
field experimentation. The same tension extends beyond these core marketing applications: platform
operations rely on expert human judgment to identify fraudulent reviews and content (Luca and
Zervas 2016), while clinical trials for healthcare interventions can cost tens of thousands of dollars
per patient (Anderer et al. 2022). More broadly, the framework applies wherever human labels are
scarce or expensive and AI-generated signals are readily available. In each case, GAI provides a
principled way to combine expensive human judgments with inexpensive AI-generated information.
One limitation is that integrating GAI into real-time decision systems may create computational
challenges. Developing online versions of the framework is therefore a promising direction for future
research.
More broadly, AI outputs create a statistical setting that is neither standard missing data nor
noisy labeling, but one with auxiliary representations available for all observations. This shifts
the inferential challenge from bias correction toward efficient information extraction. Human
labels remain the gold standard, but AI-generated signals can substantially reduce the amount of
human input needed to achieve a desired level of precision. As AI capabilities continue to advance,
frameworks with rigorous guarantees for human-AI data integration will become increasingly
important for credible empirical research in marketing and beyond.
References
Anderer A, Bastani H, Silberholz J (2022) Adaptive clinical trial designs with surrogates: When should we
bother?Management Science68(3):1982–2002, URLhttp://dx.doi.org/10.1287/mnsc.2021.4096.
Angelopoulos AN, Bates S, Cand` es EJ, Jordan MI, Lei L (2023a) Prediction-powered inference.Science
382(6671):669–674.
Angelopoulos AN, Duchi JC, Zrnic T (2023b) Ppi++: Efficient prediction-powered inference.arXiv preprint
arXiv:2311.01453.
Anonymous (2026) Generative augmented inference.Proceedings of the International Conference on Machine
Learning (ICML), accepted.

Lu et al.:Generative Augmented Inference
34
Ascarza E, Iyengar R, Schleicher M (2016) The perils of proactive churn prevention using plan recommenda-
tions: Evidence from a field experiment.Journal of Marketing Research53(1):46–60.
Athey S, Tibshirani J, Wager S (2019) Generalized random forests.The Annals of Statistics47(2):1148–1178.
Athey S, Wager S (2021) Policy learning with observational data.Econometrica89(1):133–161.
Ban GY, Keskin NB (2021) Personalized dynamic pricing with machine learning: High-dimensional features
and heterogeneous elasticity.Management Science67(9):5549–5568, URL http://dx.doi.org/10.
1287/mnsc.2020.3680.
Bang H, Robins JM (2005) Doubly robust estimation in missing data and causal inference models.Biometrics
61(4):962–973.
Berry ST, Levinsohn JA, Pakes A (1993) Automobile prices in market equilibrium: Part i and ii.
Bertsimas D, Thiele A (2006) A robust optimization approach to inventory theory.Operations Research
54(1):150–168, URLhttp://dx.doi.org/10.1287/opre.1050.0238.
Besbes O, Muharremoglu A (2013) On implications of demand censoring in the newsvendor problem.
Management Science59(6):1407–1424, URLhttp://dx.doi.org/10.1287/mnsc.1120.1654.
Bickel PJ, Ritov Y, Tsybakov AB (2009) Simultaneous analysis of Lasso and Dantzig selector.The Annals of
Statistics37(4):1705–1732.
Bojinov I, Simchi-Levi D, Zhao J (2023) Design and analysis of switchback experiments.Management Science
69(7):3759–3777.
Bradlow ET, Hu Y, Ho TH (2004) Modeling behavioral regularities of consumer learning in conjoint analysis.
Journal of Marketing Research41(4):392–396.
Brown T, et al. (2020) Language models are few-shot learners.Advances in Neural Information Processing
Systems33:1877–1901.
B¨ uhlmann P, van de Geer S (2011)Statistics for High-Dimensional Data: Methods, Theory and Applications
(Springer).
Chakrabortty A, Cai T (2018) Efficient and adaptive linear regression in semi-supervised settings.The Annals
of Statistics46(4), ISSN 0090-5364, URLhttp://dx.doi.org/10.1214/17-aos1594.
Chen E, Chen X, Jing W (2025a) Data-driven knowledge transfer in batch q* learning.Journal of the
American Statistical Association1–25.
Chen X, Simchi-Levi D, Wang Y (2022) Privacy-preserving dynamic personalized pricing with demand
learning.Management Science68(7):4878–4898.
Chen Y, Kirshner SN, Ovchinnikov A, Andiappan M, Jenkin T (2025b) A manager and an AI walk into a bar:
Does ChatGPT make biased decisions like we do?Manufacturing & Service Operations Management
27(2):354–368, URLhttp://dx.doi.org/10.1287/msom.2023.0279.

Lu et al.:Generative Augmented Inference
35
Chen Y, Liu TX, Shan Y, Zhong S (2023) The emergence of economic rationality of gpt.Proceedings of the
National Academy of Sciences120(51):e2316205120.
Chernozhukov V, Chetverikov D, Demirer M, Duflo E, Hansen C, Newey W, Robins J (2018) Double/debiased
machine learning for treatment and structural parameters.The Econometrics Journal21(1):C1–C68.
Duan J, Pelger M, Xiong R (2024) Target pca: Transfer learning large dimensional panel data.Journal of
Econometrics244(2):105521.
Farrell MH, Liang T, Misra S (2021) Deep neural networks for estimation and inference.Econometrica
89(1):181–213.
Feit EM, Berman R (2019) Test & roll: Profit-maximizing a/b tests.Marketing Science38(6):1038–1058.
Gao Y, Li M, Sun S (2023) Field experiments in operations management.Journal of Operations Management
69(4):676–701, URLhttp://dx.doi.org/10.1002/joom.1240.
Goli A, Singh A (2024) Frontiers: Can large language models capture human preferences?Marketing Science
43(4):709–722.
Green PE, Srinivasan V (1990) Conjoint analysis in marketing: New developments with implications for
research and practice.Journal of Marketing54(4):3–19.
Guadagni PM, Little JD (1983) A logit model of brand choice calibrated on scanner data.Marketing science
2(3):203–238.
Gui G, Toubia O (2023) The challenge of using llms to simulate human behavior: A causal inference perspective.
arXiv preprint arXiv:2312.15524.
Hirano K, Imbens GW, Ridder G (2003) Efficient estimation of average treatment effects using the estimated
propensity score.Econometrica71(4):1161–1189.
Huang C, Tang Z, Hu S, Jiang R, Zheng X, Ge D, Wang B, Wang Z (2025) Orlm: A customizable framework
in training large models for automated optimization modeling.Operations Research73(6):2986–3009.
Huang D, Luo L (2016) Consumer preference elicitation of complex products using fuzzy support vector
machine active learning.Marketing Science35(3):445–464.
Huang S, Aral S, Hu YJ, Brynjolfsson E (2020) Social advertising effectiveness across products: A large-scale
field experiment.Marketing Science39(6):1142–1165.
Iyer G, Ke TT (2024) Competitive model selection in algorithmic targeting.Marketing Science43(6):1226–
1241.
Jiang Y, Yuan K, Shang J, Chen X, Jiang Y (2026) From sparsity to precision: Enhancing bundle recom-
mendations via large language model augmentation and multi-graph fusion.Decision Support Systems
114732.
Kallus N, Mao X, Uehara M (2024) Localized debiased machine learning: Efficient inference on quantile
treatment effects and beyond.Journal of Machine Learning Research25(16):1–59.

Lu et al.:Generative Augmented Inference
36
Kaynar N, Siddiq A (2023) Estimating effects of incentive contracts in online labor platforms.Management
Science69(4):2106–2126.
Kok AG, Fisher ML (2007) Demand estimation and assortment optimization under substitution: Methodology
and application.Operations Research55(6):1001–1021, URL http://dx.doi.org/10.1287/opre.1070.
0409.
Kreps S, Prasad S, Brownstein JS, Hswen Y, Garibaldi BT, Zhang B, Kriner DL (2020) Factors associated with
us adults’ likelihood of accepting covid-19 vaccination.JAMA network open3(10):e2025594–e2025594.
Lee DH, et al. (2013) Pseudo-label: The simple and efficient semi-supervised learning method for deep neural
networks.Workshop on challenges in representation learning, ICML, volume 3, 896 (Atlanta).
Levi R, Perakis G, Uichanco J (2015) The data-driven newsvendor problem: New bounds and insights.
Operations Research63(6):1294–1306, URLhttp://dx.doi.org/10.1287/opre.2015.1422.
Little RJ, Rubin DB (2019)Statistical analysis with missing data(John Wiley & Sons), 3 edition.
Louviere JJ, Hensher DA, Swait JD (2000) Stated choice methods: analysis and applications.Cambridge
University Press.
Lu H, Simester D, Zhu Y (2025) Optimizing scalable targeted marketing policies with constraints.Marketing
Science44(5):1082–1103.
Luca M, Zervas G (2016) Fake it till you make it: Reputation, competition, and Yelp review fraud.Management
Science62(12):3412–3427, URLhttp://dx.doi.org/10.1287/mnsc.2015.2304.
Luo X, Qin MS, Fang Z, Qu Z (2021) Artificial intelligence coaches for sales agents: Caveats and solutions.
Journal of Marketing85(2):14–32.
Luo Y, Spindler M (2016) High-dimensionalL2 boosting: Rate of convergence.arXiv preprint arXiv:1602.08927
.
Mikl´ os-Thal J, Tucker C (2019) Collusion by algorithm: Does better demand prediction facilitate coordination
between sellers?Management Science65(4):1552–1561.
Newey WK, McFadden D (1994) Large sample estimation and hypothesis testing.Handbook of Econometrics,
volume 4, 2111–2245 (Elsevier).
Nigam K, McCallum AK, Thrun S, Mitchell T (2000) Text classification from labeled and unlabeled documents
using em.Machine learning39(2):103–134.
OpenAI (2023) Gpt-4 technical report.arXiv preprint arXiv:2303.08774.
Pan SJ, Yang Q (2009) A survey on transfer learning.IEEE Transactions on Knowledge and Data Engineering
22(10):1345–1359.
Pollard D (1991) Asymptotics for least absolute deviationregression estimators.Econometric Theory7(2):186–
199.

Lu et al.:Generative Augmented Inference
37
Qui˜ nonero-Candela J, Sugiyama M, Schwaighofer A, Lawrence ND (2008)Dataset Shift in Machine Learning
(MIT Press).
Rafieian O, Kapoor A, Sharma A (2025) Multiobjective personalization of marketing interventions.Marketing
Science44(2):457–477.
Rafieian O, Yoganarasimhan H (2021) Targeting and privacy in mobile advertising.Marketing Science
40(2):193–218.
Robins JM, Rotnitzky A (1995) Semiparametric efficiency in multivariate regression models with missing
data.Journal of the American Statistical Association90(429):122–129.
Robins JM, Rotnitzky A, Zhao LP (1994) Estimation of regression coefficients when some regressors are not
always observed.Journal of the American Statistical Association89(427):846–866.
Rubin DB (1976) Inference and missing data.Biometrika63(3):581–592.
Sahni NS (2016) Advertising spillovers: Evidence from online field experiments and implications for returns
on advertising.Journal of Marketing Research53(4):459–478.
Shimodaira H (2000) Improving predictive inference under covariate shift by weighting the log-likelihood
function.Journal of statistical planning and inference90(2):227–244.
Si N, Zhang F, Zhou Z, Blanchet J (2023) Distributionally robust batch contextual bandits.Management
Science69(10):5772–5793.
Singhvi D, Singhvi S, Zhang X (2024) A data-driven approach to improve artisans’ productivity in distributed
supply chains.Proceedings of the 25th ACM Conference on Economics and Computation, 244–245.
Sisodia A, Burnap A, Kumar V (2025) Generative interpretable visual design: Using disentanglement for
visual conjoint analysis.Journal of Marketing Research62(3):405–428.
Sugiyama M, Suzuki T, Kanamori T (2012)Density ratio estimation in machine learning(Cambridge
University Press).
Tang J, Qi Z, Fang E, Shi C (2025) Offline feature-based pricing under censored demand: A causal inference
approach.Manufacturing & Service Operations Management27(2):535–553.
Toubia O, Gui GZ, Peng T, Merlau DJ, Li A, Chen H (2025) Database report: Twin-2k-500: A data set for
building digital twins of over 2,000 people based on their answers to over 500 questions.Marketing
Science44(6):1446–1455.
Toubia O, Netzer O (2017) Idea generation, creativity, and prototypicality.Marketing science36(1):1–20.
Vaart Avd, Wellner JA (2023) Empirical processes.Weak Convergence and Empirical Processes: With
Applications to Statistics, 127–384 (Springer).
Van der Vaart A W (2000)Asymptotic statistics, volume 3 (Cambridge university press).
Vulcano G, van Ryzin G, Ratliff R (2012) Estimating primary demand for substitutable products from sales
transaction data.Operations Research60(2):313–334, URL http://dx.doi.org/10.1287/opre.1110.
1012.

Lu et al.:Generative Augmented Inference
38
Wager S, Athey S (2018) Estimation and inference of heterogeneous treatment effects using random forests.
Journal of the American Statistical Association113(523):1228–1242.
Wang L, Ye Z, Zhao J (2025) Efficient inference using large language models with limited human data:
Fine-tuning then rectification.arXiv preprint arXiv:2511.19486.
Wang M, Zhang DJ, Zhang H (2024) Large language models for market research: A data-augmentation
approach.arXiv preprint arXiv:2412.19363.
Weiss K, Khoshgoftaar TM, Wang D (2016) A survey of transfer learning.Journal of Big Data3(1):1–40.
Xiong R, Pelger M (2023) Large dimensional latent factor modeling with missing observations and applications
to causal inference.Journal of Econometrics233(1):271–301.
Xu B, Deng Y, Mela C (2022) A scalable recommendation engine for new users and items.arXiv preprint
arXiv:2209.06128.
Yoganarasimhan H (2020) Search personalization using machine learning.Management Science66(3):1045–
1070.
Zhang S, Mehta N, Singh PV, Srinivasan K (2021) Frontiers: Can an artificial intelligence algorithm mitigate
racial economic inequality? an analysis in the context of airbnb.Marketing Science40(5):813–820.
Zhu X, Goldberg AB (2009) Introduction to semi-supervised learning.Synthesis Lectures on Artificial
Intelligence and Machine Learning3(1):1–130.

Lu et al.:Generative Augmented Inference
39
Online Appendices
Appendix A: Distinction between GAI and PPI
It is instructive to compare our approach with PPI (Angelopoulos et al. 2023a,b), which further highlights the
generality of GAI for AI-data augmentation. The comparison reveals two key differences. First, PPI treats AI
outputs as surrogate labels foryand therefore cannot be directly applied whenzis categorically different
fromy—precisely the setting that motivates our framework, as discussed in the introduction.
Second, PPI’s confidence-interval construction and statistical guarantees requirezto be a deterministic
function based solely onX. However, AI-generated data differs in two key ways: (i)zmay be inherently
stochastic due to the internal randomization of AI models; andmore fundamentally, (ii)zmay depend on
predictive information beyondX, as in our retail pricing experiment with digital twins (see Example 1 for
details). In such cases, the PPI-based methods do not apply and might only inflate variance relative to
using human labels alone, whereas GAI, by Corollary 2, is guaranteed to weakly dominate the primary-only
estimator.
We construct the following example illustrating the key distinction between GAI and PPI. Let X be a
binary random variable such that P(X = 1) = P(X = −1) = 1 2 . Let U be a hidden random variable with
E[U ] = 0 and Var(U ) = σ2. X and U are independent. We assume that y is governed by both X and the hidden
random variable as y = XU . We have E[y] = E[X]E[U ] = 0 and Var(y) = Var(X)Var(U ) = σ2. Suppose that
the AI model fails to correctly specify the rule on X, but captures the hidden variable U , outputting z = U .
We observe two independent datasets: DP = {(Xi, yi, zi)}nP i=1 i.i.d. and DA = {(Xj, zj)}nA j=1 i.i.d.. Suppose our
goal is to estimate the mean of y. Let nP /n = ρ, and write n := nP and N := nA for the primary and auxiliary
sample sizes. Following Angelopoulos et al. (2023b), given a fixed constant λ∈R , the PPI mean estimator
can be written as
bθPPI(λ) = 1 nP
nPX
i=1
yi +λ

1
N
nAX
j=1
zj − 1 nA
nAX
i=1
zi
!
.
Asn→ ∞, it is easy to verify that
√n( bθPPI(λ)−0) d − → N  0, σ2
ρ

1 + λ2
1−ρ

.
Meanwhile, we know that the human data-only estimator is bθP = 1 nP Pn i=1 yi, with
√n(bθP −0) d − → N  0, σ2
ρ

.
The basic PPI corresponds to the case of λ = 1, which inflates the variance from the human data-only
estimator. PPI++ optimizes λ by minimizing the asymptotic variance, yielding λ∗ = 0 (see Example 6.1 of
Angelopoulos et al. (2023b).) As a result, PPI++ has no improvement over the human data-only estimator,
as it is essentially discarding all auxiliary samples.
Under this setup, the AI-signal correlates weakly with the actual human label because it fails to capture the
entire mechanism behind y (missing X). However, it provides significant information on inferring actual human
label by recovering the hidden variable U . PPI fails to utilize this information. In contrast, GAI operates in a
fundamentally different way. Using GAI, we can easily recover the relationship between X and y, obtaining

Lu et al.:Generative Augmented Inference
40
g∗(X, z) = Xz with the primary set. Then, the GAI estimator is bθGAI = 1 n
PnP
i=1 yi + PnA j=1 g∗(Xj, zj)  =
1
n
PnP
i=1 yi + PnA j=1 yj  , where
√n(bθGAI −θ ∗) d − → N  0, σ2 ,
which always reduces the asymptotic variance from the human data-only estimator and efficiently uses all
data samples.
Appendix B: Auxiliary Example for Section 3.2
Example 2 (y⊥z|X: Off-the-Shelf LLM Generation).This example follows the setting of Wang
et al. (2024). They consider a conjoint analysis framework in whichXdenotes the feature vectors of a
choice set with K alternatives,yrepresents the consumer’s choice, andzis the AI-generated choice. The
model corresponds tob(θ) = log

1 +PK j=1 exp(θj)  , yielding a standard MNL formulation. While similar to
Example 1,zmay in principle be correlated withyconditional onX, for example when the AI system is
queried using additional customer persona or behavioral data. However, in many applications it is practically
convenient to use LLMs in an off-the-shelf fashion. In such cases bothyandzare generated solely fromX,
implyingy ⊥ z | X. Consequently,zdoes not contain additional information aboutybeyond what is already
present inX.
Despite this conditional independence,zcan still be useful for estimation. If the AI output has strong
representational power and provides a highly informative summary ofX, then a simple parameterization
such as
g(j)(X,z) = exp

β∗⊤x(j) +η[z=j] 
1 +P ℓ∈K exp  β∗⊤x(ℓ) +η[z=ℓ]  =g j(X,z;β ∗),∀j∈ K,
as proposed in Online Appendix A of Wang et al. (2024), can approximateP(y=j|X,z) well.
To see the intuition, supposez= ϕ(X) where ϕ(·) is a complex nonlinear mapping implicitly learned by the
LLM. Recovering an equivalent representation usingXalone would require estimating
exp

β∗⊤x(j) +η[ϕ(X) =j] 
1 +P ℓ∈K exp  β∗⊤x(ℓ) +η[ϕ(X) =ℓ]  ,∀j∈ K,
which may be difficult in practice. One might attempt to approximate ϕ(·) using flexible methods such
as polynomial or spline expansions. However, with limited human-labeled data this approach may lead
to substantial model misspecification or overfitting on the small labeled sample DP, making it difficult to
extrapolateyto the full dataset D. In such cases the resulting performance may not be substantially better
than usingD P alone and ignoring the auxiliary sample.
Although this example is deliberately stylized, the same intuition extends to more general set-
tings—particularly when the AI signalztakes more flexible or high-dimensional forms. In such cases
AI-generated features can act as rich summaries of latent structure in E[y | X], improving estimation even
wheny⊥z|X. ■

Lu et al.:Generative Augmented Inference
41
Appendix C: Extension to Covariate Shift
This appendix complements Section 6, which develops the extension of GAI to covariate shift in the main body
and states the doubly robust theorem (Theorem 3) and the doubly robust score (18) there. Here we record
the material deferred from the main body: the formal covariate-shift setting and assumptions (Section C.1),
and the combined known-density-ratio result that establishes both √n-asymptotic normality and variance
dominance for the weighted GAI estimator (Section C.2). All proofs—of the combined known-ratio theorem
below and of the main-body doubly robust theorem—are collected in Section J.
C.1. Setting and Assumptions
Let QS and QT denote the source and target populations, respectively; both are joint laws of (X , y, z). The
dataset D = {Ξi = (Xi, yi, wi, zi)}n i=1 consists of i.i.d. draws from QS, with human labels partially observed
according to the labeling indicator w, exactly as in Section 3.2. We write ES and ET for expectations under
QS and QT, and QS,X and QT,X for the corresponding marginal laws ofX. With slight abuse of notation,
ES also denotes expectation over the source data-generating process including the labeling indicator, i.e.,
over the joint law of (X , y, z, w) with (X , y, z) ∼Q S and w as in Section 3.2. We let r(X) :=
dQT,X
dQS,X (X) denote
the density ratio of the covariate distributions; we always display the argument and write r(X), so that
no confusion with the rates r1, r2 in Assumption 2 arises. Analogously to ∥·∥Q,2 in the main text, given a
multi-dimensional functionfwe write∥f∥ QS,2 := (ES[∥f∥ 2]) 1/2 and∥f∥ QT,2 := (ET[∥f∥ 2]) 1/2 .
The parameter of interest is the target parameter β∗ T defined in (16), which, under Assumption 4 below
and by the same argument as for (2), satisfies the first-order condition
ET

X⊤  ∇b  Xβ∗ T  −y  = 0.(20)
Following the proof of Corollary 2 (Section I.2.1), we define
ζT(X,z) :=X ⊤  ∇b  Xβ∗ T  −g ∗(X,z)  andπ(X,y,z) :=X ⊤ (g∗(X,z)−y) ;
these are the covariate-shift analogs of ζ and π defined there, with β∗ replaced by β∗ T in ζT (π is unchanged);
they coincide with the quantities ζT and π introduced in (17). Our analysis relies on the following assumption,
which formalizes the two conditions stated in prose in Section 6.
Assumption 4(Covariate Shift Setting). (i)(Covariate shift only)The conditional law of(y , z)given
Xis identical under QS and QT; the two populations differ only in the marginal distribution ofX. (ii)
(Strict overlap) QT,X is absolutely continuous with respect to QS,X, and r(X) ⩽M <∞, QS-almost surely.
(iii)(Homogeneous labeling) w is independent of(X , y, z)with P(w = 1) =ρ∈ (0, 1], and ρ is known. (iv)
(Target identification)Assumption 1 holds under QS; in addition, ET[X⊤X] ≻ 0and β∗ T ∈ Bsolves the target
population problemmin β∈B ET [ℓ(X,y;β)].
We record several direct consequences of Assumption 4 that we use repeatedly. First, under item (i),
g∗(X, z) = E[y | X, z] is the same function under both populations, and items (i)–(ii) yield the change-of-
measure identity
ET [h(X,y,z)] =E S [r(X)h(X,y,z)] (21)

Lu et al.:Generative Augmented Inference
42
for any QT-integrable function h. Second, item (ii) implies supp(QT,X) ⊆supp (QS,X) ⊆ ˘X , where ˘X is the
compact set containing X introduced in Section 3.1; hence the boundedness ofXover ˘X extends to the
target population without further conditions; likewise, the bound ∥Cov(y | X, z)∥⩽˜σ2 in Assumption 1(iii)
transfers to the target population automatically by items (i)–(ii), and we do not re-assume it. Similarly,
the square-integrability ofyin Assumption 1(iv), which holds underQ S by item (iv), extends to the target
population, since ET

∥y∥2 = ES  r(X)∥y∥2 ⩽ME S  ∥y∥2 by (21) and item (ii). Third, under item (iv), β∗ T
is the unique minimizer of the target population problem: strict convexity of ET [ℓ(X,y;β)] follows from
ET[X⊤X]≻0 by the same argument as in the proof of Lemma 2.
We also record the rate conditions used by the doubly robust theorem of Section 6 (Theorem 3), the
counterpart of Assumption 2. To avoid any confusion with the density ratior ∗(X) and with the ratesr 1, r2
of Assumption 2, we denote the rate exponents by rg and rr, and write r∗(X) for the true density ratio (the
object denotedr(X) above) andbrfor its estimator.
Assumption 5(ML Convergence Rates for Doubly Robust Estimation). There exist α(n) ↓ 0
andr g, rr ⩾0withr g +r r ⩾1/2such that
∥bg−g ∗∥QS,2 ⩽α(n S)/n rg S and∥br−r ∗∥QS,2 ⩽α(n S)/nrr S .
Two features of Assumption 5 are worth highlighting. First, unlike the condition on bein Assumption 2,
no sup-norm consistency condition on bris required: brenters the doubly robust score (18) multiplicatively
rather than through an inverse weight, so its error never appears in a denominator and an L2 rate suffices.
Second, both rates are indexed by the source sample size nS, even though brmay also use the (typically much
larger) target sample: estimatingg ∗ requires the source labels, and the precision of bris limited by how well
the source covariate distribution QS,X can be learned from nS draws, no matter how precisely QT,X is known.
Finally, no separate rate condition under the target population is needed: by the change-of-measure identity
(21) and Assumption 4(ii),
∥∆g∥2 QT,2 =E S
h
r∗(X)∥∆ g∥2
i
⩽M∥∆ g∥2 QS,2 ,
so the source-population rate for bg transfers automatically to the target population; this is a derived fact, not
an additional assumption.
C.2. Known Density Ratio
We first give the formal combined statement for the known-density-ratio case discussed in Section 6.1. When
the density ratio r(X) is known—for example when the target covariate distribution is available from external
sources such as census tabulations or platform-wide logs, as in the stratified design of Section E—we retain
the partial-labeling structure under the random labeling design (Assumption 4(iii), with known ρ) and define
the weighted GAI score
Ψw(Ξ;g;β) :=r(X)X ⊤

∇b(Xβ)−g(X,z) + w ρ (g(X,z)−y)  =r(X)Ψ(Ξ;ρ,g;β),(22)
whereΨis the GAI score in (7) with e≡ρ . The estimation procedure is Algorithm 1 with two modifications:
(a) because the labeling probability is known, we set be(k) ≡ρ rather than estimating it; and (b) the score of each

Lu et al.:Generative Augmented Inference
43
observation is multiplied by the known weight r(Xi), as in (22); correspondingly, in the variance-estimation
step the Jacobian estimate is also weighted, bJw = 1 n PK k=1 P i∈Ik r(Xi)X ⊤ i ∇2b  Xi bβw  Xi. The nuisance bg(k)
is cross-fitted on the source primary observations exactly as in Algorithm 1. The weighted GAI estimator bβw
then satisfies  1 n KX k=1 X i∈Ik Ψw  Ξi; bg(k); bβw   ⩽inf β∈B  1 n KX k=1 X i∈Ik Ψw  Ξi; bg(k);β   +o P (n−1/2).
DefineJ T := ES

r(X)X ⊤∇2b  Xβ∗ T  X  = ET  X⊤∇2b  Xβ∗ T  X  , where the equality follows from (21). The
natural human-data benchmark reweighted to the target population is theweighted primary-onlyestimator
bβP,w, a solution to X
i:w i=1
r(Xi)∇ βℓ(Xi,y i;β) = 0,(23)
or, equivalently, Pn i=1 wi r(Xi) ∇βℓ(Xi, yi; β) = 0. This estimating equation is valid for β∗ T: by Assump-
tion 4(iii) and (21),
ES

w r(X)∇βℓ

X,y;β ∗ T  =ρE S  r(X)∇ βℓ  X,y;β ∗ T  =ρE T  ∇βℓ  X,y;β ∗ T  = 0,
where the last equality is the first-order condition (20). The following theorem combines the asymptotic
normality of the weighted GAI estimator with its dominance over this benchmark.
Theorem 4(Asymptotic Normality and Dominance under Covariate Shift: Known Density Ratio).
Suppose Assumption 4 holds and ∥bg− g∗∥QS,2 = o(1). Then the weighted GAI estimator is √n-asymptotically
normal for the target parameterβ ∗ T,
√n  bβw −β ∗ T  ⇝N  0,Σ w  ,Σ w =J −1 T Ωw J−1 T ,
whereΩ w :=E S

Ψw(Ξ;g ∗;β ∗ T)Ψ w(Ξ;g ∗;β ∗ T)⊤ admits the decomposition
Ωw =E S

r(X)2 ζTζ ⊤ T  + 1 ρ ES  r(X)2 ππ ⊤ .(24)
Moreover, the weighted primary-only estimator bβP,w of (23) is √n-asymptotically normal, √n  bβP,w −β ∗ T  ⇝
N

0,Σ P,w , with
ΣP,w = 1 ρ J−1 T  ES  r(X)2 ζTζ ⊤ T  +E S  r(X)2 ππ ⊤ J−1 T ,
and bβw dominates it:
ΣP,w −Σ w =
 1
ρ −1

J−1 T ES  r(X)2 ζTζ ⊤ T  J−1 T ⪰0,(25)
withΣ P,w ≻Σ w if and only ifρ <1and
ES

r(X)2 X⊤  ∇b  Xβ∗ T  −E[y|X,z]   ∇b  Xβ∗ T  −E[y|X,z] ⊤ X  ≻0.
The proof is given in Section J.1. The decomposition (24) holds because the cross terms between ζT and π
vanish: E[π| X, z] = 0, andw is independent of (X, y, z) with E[w/ρ] = 1 andE[w/ρ2] = 1/ρ. As in the known-ρ
case of Corollary 2 and the discussion following it, the normality conclusion requires only L2-consistency of bg
in place of Assumption 2: since both ρ and r(X) are known, the remainder terms driven by a propensity
estimate vanish identically, so no rate or sup-norm condition is needed. The gap (25) is the exact structural
analog of Corollary 1: the entire efficiency gain comes from eliminating the misspecification/representation
term ζT on the unlabeled observations—now weighted by r(X)2—while the irreducible human-label noise
termπcontributes identically to both asymptotic variances.

Lu et al.:Generative Augmented Inference
44
Table 5 Paired t-test p-values (GAI (Embeddings) vs benchmarks) for Conjoint Analysis
(a) MAPE (b) 95% CI Coverage (c) 95% CI Width
Method 50 100 150 200 50 100 150 200 50 100 150 200
Primary 5e-33 3e-37 2e-38 2e-40 0.02 9e-5 5e-4 2e-4 4e-11 0.56 3e-3 5e-8
Naive 9e-33 9e-37 6e-38 8e-40 2e-117 1e-94 6e-85 2e-69 1e-41 6e-51 3e-57 3e-57
PPI 0.31 5e-37 5e-38 3e-40 0.31 0.48 0.31 0.26 0.02 1e-20 3e-28 2e-30
PPI++ 0.01 4e-37 3e-38 2e-40 7e-5 4e-8 8e-5 1e-7 2e-8 0.42 0.02 1e-8
Table 6 Paired t-test p-values (GAI (Labels) vs benchmarks) for Conjoint Analysis
(a) MAPE (b) 95% CI Coverage (c) 95% CI Width
Method 50 100 150 200 50 100 150 200 50 100 150 200
Primary 3e-15 2e-12 5e-7 3e-6 3e-3 6e-4 0.03 0.02 7e-19 5e-17 2e-16 2e-15
Naive 6e-46 2e-44 5e-49 3e-40 5e-71 8e-55 3e-49 6e-41 5e-53 3e-64 7e-67 1e-68
PPI 0.32 2e-18 8e-15 1e-15 1.00 0.30 0.29 0.15 0.02 2e-22 9e-30 9e-32
PPI++ 0.01 3e-15 3e-11 1e-10 3e-5 3e-7 3e-3 3e-5 2e-14 9e-17 9e-15 2e-15
Remark 1 (No Comparison with Unweighted Primary-Only Estimation).Theunweighted
primary-only estimator, i.e., a solution to P i:w i=1 ∇βℓ(Xi, yi; β) = 0 as in Corollary 2, converges to the
source pseudo-true parameter β∗ S ∈arg min β∈B ES [ℓ(X,y;β)] . Under model misspecification, β∗ S ̸= β∗ T in
general, so the unweighted estimator carries an O(1) asymptotic bias and is inconsistent for the target
parameter β∗ T; no meaningful variance comparison with bβw exists. If the GLM were correctly specified—that
is, if E[y | X] = ∇b(Xβ◦) for some β◦ ∈ B—then β∗ S = β∗ T = β◦ and the issue would disappear; our framework,
however, explicitly allows for misspecification.
C.3. Estimated Density Ratio
For the estimated-density-ratio case, the doubly robust estimator, its doubly robust score (18), the two-sample
design, and the asymptotic normality result (Theorem 3) are developed in the main body in Section 6.2; its
proof is given in Section J.2.
Appendix D: Detailed Results of Experiments
D.1. V accine Conjoint Analysis
D.1.1. Tests for Performance ImprovementWe conduct paired t-tests comparing GAI to each
benchmark method across repeated trials for each metric (MAPE, coverage, CI width). The paired design
controls for sampling variation and isolates estimator differences.
Tables 5 and 6 report p-values for GAI (Embeddings) and GAI (Labels), respectively. Both GAI variants
achieve significant MAPE improvements over all benchmarks. Coverage differences relative to Primary, Naive,
and PPI++ are significant for both variants. For CI width, GAI (Labels) produces significantly narrower
intervals than PPI++ across all sample sizes, while GAI (Embeddings) produces narrower intervals than
PPI++ atn P = 50 but modestly wider intervals atn P ∈ {150,200}.
D.1.2. Decision ErrorsTable 7 reports decision errors. GAI (Embeddings) averages 2.6%, lower than
Primary (6.9%), PPI (3.2%), PPI++ (8.7%), and Naive (20.4%). GAI (Labels) averages 4.4%, also substantially

Lu et al.:Generative Augmented Inference
45
Table 7 Decision Errors for Conjoint Analysis (% of all CIs)
Methodn P =50n P =100n P =150n P =200
Primary 1.82 6.73 7.09 12.00
Naive 19.09 20.00 20.73 21.64
PPI 0.00 1.82 3.82 7.09
PPI++ 2.91 9.09 8.18 14.55
GAI (Labels) 0.18 2.91 5.27 9.09
GAI (Embeddings) 0.55 1.45 3.09 5.45
Table 8 Benchmark Comparison for Conjoint Analysis: MAPE (%)
nP = 50n P = 100
GAI GAI
Model Primary Naive PPI PPI++ Lab Emb Primary Naive PPI PPI++ Lab Emb
GPT-3.5-Turbo-0613 32.02 48.83 – – 17.23 16.51 25.27 45.89 – – 17.61 17.06
GPT-3.5-Turbo-0125 32.02 42.98 – – 17.48 16.45 25.27 39.97 50.55 30.41 17.92 17.35
GPT-4 32.02 50.14 – – 16.79 16.81 25.27 47.75 48.56 29.40 17.37 17.36
GPT-4o 32.02 48.52 – – 16.86 16.50 25.27 45.75 44.57 29.69 17.52 17.23
nP = 150n P = 200
GAI GAI
Model Primary Naive PPI PPI++ Lab Emb Primary Naive PPI PPI++ Lab Emb
GPT-3.5-Turbo-0613 19.67 42.73 39.02 22.60 16.35 16.62 19.01 40.10 35.08 21.20 17.22 16.87
GPT-3.5-Turbo-0125 19.67 37.40 36.11 23.07 16.64 16.13 19.01 35.17 29.95 20.96 17.22 16.63
GPT-4 19.67 46.00 33.54 22.62 15.96 16.04 19.01 43.11 29.21 20.96 16.64 16.53
GPT-4o 19.67 43.33 32.96 22.96 15.97 15.73 19.01 40.29 29.21 21.00 16.64 16.24
Notes: All models use CoT prompting. A “–” symbol indicates cases where the value exceeds 1,000, which occurs
because PPI-based methods can suffer from singularity problems in small primary samples.
lower than most benchmarks, except for PPI. Although PPI achieves the lowest error rate only at nP = 50
(and the lowest average among the non-GAI benchmarks), GAI (Embeddings) attains the lowest average
decision-error rate overall; PPI’s low rates come at the cost of wider intervals.
D.1.3. Robustness to Auxiliary GeneratorTables 8–10 report results using different LLMs (GPT-
3.5-Turbo, GPT-4, GPT-4o) with CoT prompting, comparing both label-based (z=Labels) and embedding-
based ( z=Embeddings) auxiliary representations. GAI consistently achieves the lowest MAPE across all
configurations while maintaining near-nominal coverage, demonstrating robustness to both the choice of
auxiliary generator and representation type.
D.2. Retail Pricing Study
D.2.1. Tests for Performance ImprovementWe conduct paired t-tests comparing GAI to each
benchmark method across repeated trials for each metric (MAPE, coverage, CI width). The paired design
controls for sampling variation and isolates estimator differences.
Table 11 reports p-values for the pricing study. GAI’s MAPE improvements over all benchmarks are
significant at most sample sizes. For CI width, PPI++ produces narrower intervals than GAI.

Lu et al.:Generative Augmented Inference
46
Table 9 Benchmark Comparison for Conjoint Analysis: 95% CI Coverage Probability (%)
nP = 50n P = 100
GAI GAI
Model Primary Naive PPI PPI++ Lab Emb Primary Naive PPI PPI++ Lab Emb
GPT-3.5-Turbo-0613 97.82 27.27 100.00 95.82 99.64 100.00 92.73 27.64 99.82 89.09 96.91 98.18
GPT-3.5-Turbo-0125 97.82 20.00 100.00 93.82 100.00 100.00 92.73 22.00 98.18 88.36 97.09 97.64
GPT-4 97.82 28.55 100.00 94.18 99.45 100.00 92.73 28.00 99.09 89.64 96.91 98.00
GPT-4o 97.82 26.55 99.82 94.55 99.82 99.45 92.73 26.36 98.00 89.09 97.09 98.55
nP = 150n P = 200
GAI GAI
Model Primary Naive PPI PPI++ Lab Emb Primary Naive PPI PPI++ Lab Emb
GPT-3.5-Turbo-0613 92.55 27.45 98.00 90.36 94.73 96.73 88.00 29.09 95.64 84.73 90.18 94.36
GPT-3.5-Turbo-0125 92.55 24.36 96.73 90.91 94.18 96.91 88.00 27.45 94.55 84.73 90.00 93.45
GPT-4 92.55 27.27 97.64 90.18 94.73 96.91 88.00 26.18 92.55 84.36 91.09 95.64
GPT-4o 92.55 26.36 95.82 90.91 94.73 96.91 88.00 27.09 92.91 85.09 90.91 94.55
Table 10 Benchmark Comparison for Conjoint Analysis: 95% CI Width
nP = 50n P = 100
GAI GAI
Model Primary Naive PPI PPI++ Lab Emb Primary Naive PPI PPI++ Lab Emb
GPT-3.5-Turbo-0613 2.43 0.57 14.21 2.62 1.93 2.15 1.51 0.54 5.18 1.50 1.36 1.50
GPT-3.5-Turbo-0125 2.43 0.51 37.35 2.48 1.92 2.15 1.51 0.49 3.30 1.51 1.35 1.50
GPT-4 2.43 0.56 21.23 2.44 1.93 2.07 1.51 0.54 3.41 1.51 1.35 1.48
GPT-4o 2.43 0.55 9.28 2.44 1.94 2.11 1.51 0.53 2.71 1.52 1.36 1.50
nP = 150n P = 200
GAI GAI
Model Primary Naive PPI PPI++ Lab Emb Primary Naive PPI PPI++ Lab Emb
GPT-3.5-Turbo-0613 1.19 0.52 2.39 1.19 1.11 1.23 1.01 0.50 1.99 1.01 0.96 1.05
GPT-3.5-Turbo-0125 1.19 0.47 2.14 1.19 1.11 1.23 1.01 0.46 1.67 1.01 0.96 1.04
GPT-4 1.19 0.52 1.97 1.19 1.11 1.21 1.01 0.50 1.61 1.00 0.96 1.04
GPT-4o 1.19 0.51 1.94 1.19 1.11 1.21 1.01 0.49 1.58 1.00 0.96 1.05
Table 11 Paired t-test p-values (GAI vs benchmarks) for Pricing Study
(a) MAPE (b) 95% CI Coverage (c) 95% CI Width
Method 100 200 300 400 500 100 200 300 400 500 100 200 300 400 500
Primary 7e-5 6e-5 0.01 2e-3 0.11 0.06 0.18 0.15 0.32 0.30 0.44 0.08 5e-3 5e-5 4e-8
Naive 4e-11 2e-20 8e-17 1e-31 1e-21 ≈0≈0 3e-43≈0 2e-28 5e-55 3e-67 8e-61 4e-68 3e-63
PPI 1e-5 5e-4 3e-3 2e-5 9e-5 0.06 0.16 0.41 0.06 1.00 8e-14 5e-30 1e-41 2e-46 7e-58
PPI++ 1e-4 2e-3 0.06 1e-3 0.09 0.03 0.32 0.11 0.32 0.26 9e-5 1e-7 4e-4 7e-4 3e-3
Notes:≈0 represents p-value<10 −300.
D.2.2. Decision ErrorsTable 12 reports decision errors. GAI achieves 0.2% averaged across sample
sizes, lower than PPI (1.2%), PPI++ (1.8%), and Primary (2.2%). Naive attains 0.0%, but this reflects its
severe undercoverage (50%): its biased yet narrow intervals seldom trigger a sign or significance error, so its
zero rate is not a sign of reliable inference.

Lu et al.:Generative Augmented Inference
47
Table 12 Decision Errors for Pricing Study (% of all CIs)
Methodn P =100n P =200n P =300n P =400n P =500
Primary 4.0 2.0 3.0 0.0 2.0
Naive 0.0 0.0 0.0 0.0 0.0
PPI 2.0 0.0 1.0 2.0 1.0
PPI++ 4.0 0.0 4.0 0.0 1.0
GAI 0.0 0.0 0.0 0.0 1.0
Table 13 Pricing Study Averaged Across All 40 Products: MAPEs, coverage probabilities, and CI widths
(a) MAPE (%) (b) 95% CI Coverage (%) (c) 95% CI Width
Method 100 200 300 400 500 100 200 300 400 500 100 200 300 400 500
Primary 14.34 9.66 7.80 6.23 5.62 96.10 96.45 97.12 97.90 97.98 0.88 0.62 0.50 0.43 0.39
Naive 22.48 21.06 19.64 18.32 17.00 46.32 46.95 46.90 47.28 48.10 0.28 0.27 0.25 0.24 0.23
PPI 17.73 12.17 10.11 8.81 8.03 96.68 96.42 97.10 96.72 96.80 1.07 0.77 0.64 0.57 0.52
PPI++ 14.16 9.40 7.60 6.14 5.51 94.88 95.92 96.78 97.52 97.52 0.84 0.59 0.48 0.42 0.38
GAI 8.51 6.94 6.14 5.07 4.68 99.25 98.60 98.65 99.02 98.92 0.88 0.61 0.49 0.42 0.38
Table 14 Paired t-test p-values (GAI vs benchmarks) for Census Analysis
(a) MAPE (b) 95% CI Coverage (c) 95% CI Width
Method 100 250 500 750 1k 100 250 500 750 1k 100 250 500 750 1k
Primary 2e-10 2e-8 5e-9 5e-6 7e-6 3e-4 1e-4 1e-4 8e-4 1e-4 0.09 5e-5 4e-8 1e-13 1e-15
Naive 1e-7 6e-8 3e-5 6e-4 4e-3 3e-25 4e-25 5e-25 6e-27 6e-27 4e-10 1e-15 2e-18 4e-23 1e-24
PPI 3e-7 7e-10 1e-7 6e-6 1e-4 2e-3 0.03 0.02 0.17 0.05 0.78 0.74 0.98 0.65 0.36
PPI++ 1e-9 2e-9 1e-7 1e-5 2e-5 6e-4 2e-3 0.01 0.05 0.01 0.16 0.54 0.53 0.26 0.30
D.2.3. Results Across All ProductsTable 13 reports results averaged across all 40 products in the
Toubia et al. (2025) dataset, where we use the same experimental design as Section 7.2 and estimateg(X , z)
usingℓ 1-regularized logistic regression (C= 0.1) with 5-fold cross-fitting.
The results across all 40 products reinforce the main findings: (1) GAI achieves the lowest MAPE at every
sample size; (2) GAI maintains coverage above 98% while Naive severely undercovers (46–48%); and (3) CI
widths are comparable across valid methods. These patterns confirm that GAI’s advantages generalize across
diverse product categories.
D.3. Health Insurance Census Analysis
D.3.1. Tests for Performance ImprovementWe conduct paired t-tests comparing GAI to each
benchmark method across repeated trials for each metric (MAPE, coverage, CI width). The paired design
controls for sampling variation and isolates estimator differences.
Table 14 shows GAI significantly outperforms all benchmarks in MAPE and coverage. For CI width, GAI
and PPI++ show no significant difference.
D.3.2. Decision ErrorsAs shown in Table 15, GAI achieves zero decision errors across all sample sizes,
while Naive exhibits 12–20% error rates and Primary, PPI, PPI++ show moderate rates (2–11%).

Lu et al.:Generative Augmented Inference
48
Table 15 Decision Errors for Census Analysis (% of all CIs)
Methodn P =100n P =250n P =500n P =750n P =1000
Primary 11.0 4.0 4.0 2.0 3.0
Naive 20.0 19.0 16.0 12.0 12.0
PPI 8.0 0.0 3.0 2.0 2.0
PPI++ 10.0 3.0 3.0 2.0 3.0
GAI 0.0 0.0 0.0 0.0 0.0
Appendix E: V accine Conjoint Analysis under Covariate Shift: Known Density Ratio
This appendix considers a practical problem: the labeled and AI-augmented data may come from one source
population, while the parameter of interest is defined for a different target population. This can occur when
a conjoint survey is fielded to an accessible online panel, a specific customer segment, or an early-adopter
sample, but the researcher wants to report preferences for a broader market whose covariate distribution
differs from the source sample. In this setting, the estimating equations need to be weighted to the target
covariate distribution. This appendix corresponds to the known-density-ratio case in Section 6.1, where the
source-to-target density ratio is determined by the sampling design.
We illustrate this source-to-target setting in the vaccine conjoint application. The covariate shift is defined
by the severe-side-effect probability of Vaccine A with two strata: 1 in 1 ,000,000 and 1 in 10 ,000. The target
covariate distribution is balanced, placing 50% mass on each stratum. For each nP ∈ {50, 100, 150}8, we
draw the primary sample without replacement so that 70% of observations have severe side-effect probability
1 in 1 ,000,000 and 30% have severe side-effect probability 1 in 10 ,000. We then draw nA = 700 auxiliary
observations without replacement from the complement of the primary sample, using the same 70/30 source
distribution. Thus, the primary and auxiliary samples have matching covariate distributions, which differs
from the balanced 50/50 target distribution. All estimators are evaluated on the same sample path. We
compute the ground-truth parameter β∗ by fitting the same choice model to the full human-labeled sample
with the target covariate distribution.
We correct the source-to-target covariate shift by weighting each observation’s GAI score. For observation
iin severe-side-effect stratums, the weight is
qi = πtarget(s) πsample(s) .
Under the 70/30 source distribution and the 50/50 target distribution, these weights are approximately 0.71
for the 1 in 1 ,000,000 stratum and 1.67 for the 1 in 10 ,000 stratum. GAI-W estimates g(X, z) = E[Y| X, z]
with cross-fitted logistic regression. Since the primary and auxiliary samples share the same source covariate
distribution, GAI-W uses the constant labeling probabilitye=n P /(nP +n A).
We also weight the benchmark estimators to adjust for this distributional difference. Primary-W fits a
weighted logistic regression using only the primary human labels. Naive-W fits a weighted logistic regression
on the primary-plus-auxiliary union, using human labels for primary observations and LLM labels for auxiliary
observations. PPI-W and PPI++-W pass weights for both labeled and auxiliary rows to the PPI package.
8 Because this stratified sampling design requires a larger underlying pool, we reduce both the primary and auxiliary
sample sizes in this application.

Lu et al.:Generative Augmented Inference
49
Table 16 Benchmark Comparison for GAI-W under Side-Effect Covariate Shift
(a) MAPE (%) (b) 95% CI Coverage (%) (c) 95% CI Width
Method 50 100 150 50 100 150 50 100 150
Primary-W 55.60 30.30 25.02 90.18 90.73 90.18 2.70 1.64 1.31
Naive-W 113.30 86.25 70.29 13.64 14.18 15.64 1.15 0.93 0.81
PPI-W 84.31 60.53 36.70 100.00 99.63 98.00 15.03 4.49 2.33
PPI++-W 50.87 31.59 25.11 89.84 90.91 90.18 2.67 1.63 1.30
GAI-W 18.04 16.78 16.01 99.64 99.09 97.45 2.15 1.49 1.21
Notes: The auxiliary sample is drawn to match the primary sample’s 70/30 severe-side-effect distribution. All
methods use post-stratification weights to target the balanced severe-side-effect distribution. PPI-W and PPI++-W
summaries drop numerical failures; they are based on 34 successful trials atn P = 50, 49 atn P = 100, and 50 at
nP = 150.
Table 17 Paired t-test p-values (GAI-W vs weighted benchmarks) under Side-Effect Covariate Shift
(a) MAPE (b) 95% CI Coverage (c) 95% CI Width
Method 50 100 150 50 100 150 50 100 150
Primary-W 1.01e-19 2.42e-17 1.18e-14 1.40e-9 5.48e-9 5.19e-8 4.67e-15 2.01e-12 3.34e-14
Naive-W 9.37e-44 8.06e-40 8.40e-47 2.44e-56 2.64e-54 6.61e-51 2.47e-46 5.66e-48 2.34e-54
PPI-W 1.40e-7 2.91e-12 1.09e-17 – 0.26 0.50 0.08 6.03e-7 2.07e-25
PPI++-W 1.21e-14 2.52e-16 3.21e-16 2.47e-7 1.02e-6 5.19e-8 1.79e-9 4.21e-14 1.62e-13
Notes: A “–” indicates that paired coverage for GAI-W and PPI-W was identical across trials when PPI-W does not
fail due to singularity problems, so the pairedt-statistic is undefined.
Table 18 Decision Errors for GAI-W under Side-Effect Covariate Shift (% of all CIs)
Methodn P =50n P =100n P =150
Primary-W 7.27 8.36 7.82
Naive-W 23.27 22.73 22.55
PPI-W 0.00 0.37 1.82
PPI++-W 6.68 7.61 7.64
GAI-W 0.36 0.91 2.55
Results.Table 16 shows that GAI-W has the lowest MAPE across all primary sample sizes, while
maintaining coverage above the nominal level and producing narrower intervals than the other valid methods.
Naive-W remains biased despite weighting, indicating that correcting the covariate distribution does not
remove the bias from treating auxiliary labels as human labels. PPI-W attains high coverage, but with
substantially wider intervals, especially at small primary sample sizes.
Table 17 confirms that GAI-W’s MAPE improvements are statistically significant relative to all weighted
benchmarks at every primary sample size. Coverage improvements are significant relative to Primary-W,
Naive-W, and PPI++-W. For interval width, GAI-W is significantly narrower than Primary-W and PPI++-W
at all sample sizes and narrower than PPI-W at nP = 100 and 150, while Naive-W is narrower but invalid
because it severely undercovers.
Table 18 reports decision errors for the same matched-auxiliary design. GAI-W has substantially lower
decision-error rates than Primary-W, Naive-W, and PPI++-W. PPI-W has slightly lower decision-error

Lu et al.:Generative Augmented Inference
50
Table 19 Benchmark Comparison for GAI-DR under Estimated Density-Ratio Covariate Shift
(a) MAPE (%) (b) 95% CI Coverage (%) (c) 95% CI Width
Method 50 100 150 50 100 150 50 100 150
Primary 60.59 32.42 24.30 87.45 89.45 89.82 2.65 1.52 1.19
Naive 121.00 87.65 70.70 10.00 13.82 19.45 1.07 0.82 0.71
PPI 131.43 71.92 75.70 100.00 100.00 98.73 97.30 6.58 47.15
PPI++ 54.35 33.04 25.51 91.43 89.09 90.55 3.87 1.54 1.21
GAI-DR 27.29 19.21 17.60 97.45 98.91 98.18 1.89 1.53 1.43
rates, but this again reflects its wider confidence intervals and lower test power rather than superior point
estimation.
Appendix F: V accine Conjoint Analysis under Covariate Shift: Estimated Density
Ratio
This appendix reports an estimated-density-ratio version of the vaccine conjoint covariate-shift experiment.
This appendix provides the empirical implementation of the GAI-DR estimator developed in Section 6.2.
In contrast to the known-ratio design in Section E, the source-to-target density ratio is not supplied to the
researcher and must be estimated from source and target covariates.
We construct source and target populations by tilting the finite vaccine conjoint pool along three attributes:
90% efficacy, five-year coverage, and rare severe side effects (1 in 1 ,000,000). The source population places
lower mass on these favorable attributes, while the target population places higher mass on them.
For each trial and each nP ∈ {50, 100, 150}, we draw nP fully labeled source observations and nT = 700
target observations with covariates and LLM labels. All estimators are evaluated on the same sample paths
and target the full-target-population ground-truth parameter. GAI-DR estimates the source-to-target density
ratio using a cross-fitted logistic classifier with L2 regularization ( C = 1). The nuisance prediction g(X, z) is
estimated using cross-fitted L2 logistic regression ( C = 0.05). Because the density ratio is unknown in this
setting, the empirical benchmarks do not receive density-ratio weights.
Results.Table 19 shows that GAI-DR has the lowest MAPE at all three source-label sample sizes after
estimating the source-to-target density ratio. The improvements are large: at nP = 50, GAI-DR reduces MAPE
from 60.59% for Primary and 54.35% for PPI++ to 27.29%. GAI-DR also restores nominal coverage, attaining
97–99% coverage across sample sizes, whereas Primary, Naive, and PPI++ remain below 95%. Importantly,
the coverage improvement is not driven by excessively wide intervals: GAI-DR intervals are comparable to
Primary and PPI++ at nP = 100 and only moderately wider at nP = 150, while being substantially narrower
than PPI.
Table 20 shows that GAI-DR also yields low decision-error rates. Its average decision-error rate is 1.27%,
compared with 8.97% for Primary, 36.24% for Naive, and 7.75% for PPI++. PPI has similarly low decision
errors, but this comes from extremely wide intervals rather than from accurate point estimation.
Table 21 confirms that GAI-DR’s MAPE improvements are statistically significant relative to every
benchmark at every source-label sample size. Coverage improvements relative to Primary, Naive, and PPI++
are also statistically significant throughout. For interval width, GAI-DR is substantially narrower than

Lu et al.:Generative Augmented Inference
51
Table 20 Decision Errors for GAI-DR under Estimated Density-Ratio Covariate Shift (% of all CIs)
Methodn P =50n P =100n P =150
Primary 9.09 8.91 8.91
Naive 38.18 36.91 33.64
PPI 0.00 0.00 1.27
PPI++ 5.45 9.45 8.36
GAI-DR 1.82 0.73 1.27
Table 21 Paired t-test p-values (GAI-DR vs unweighted benchmarks) under Estimated Density-Ratio Covariate
Shift
(a) MAPE (b) 95% CI Coverage (c) 95% CI Width
Method 50 100 150 50 100 150 50 100 150
Primary 2.70e-13 1.76e-18 3.76e-13 1.43e-06 3.97e-09 7.13e-08 4.13e-14 0.69 1.06e-09
Naive 9.57e-43 5.70e-49 1.62e-44 8.28e-49 1.75e-49 2.47e-46 9.76e-25 3.09e-26 4.88e-28
PPI 3.99e-04 1.16e-07 3.40e-03 6.25e-03 0.03 0.37 0.26 2.95e-03 0.30
PPI++ 1.46e-04 1.13e-18 2.03e-12 1.00e-03 5.78e-09 2.73e-07 0.15 0.73 1.04e-08
Table 22 Pricing Study with High-dimensional Auxiliary Information: MAPEs, coverage probabilities, and CI
widths
(a) MAPE (%) (b) 95% CI Coverage (%) (c) 95% CI Width
Method 100 200 300 400 500 100 200 300 400 500 100 200 300 400 500
Primary 22.36 16.03 12.47 9.59 9.53 95.00 97.00 95.00 99.00 92.00 1.17 0.82 0.66 0.57 0.51
Naive 22.22 21.97 19.99 19.67 19.43 50.00 50.00 50.00 50.00 50.00 0.37 0.35 0.33 0.32 0.31
PPI 26.91 15.31 14.10 13.98 12.88 95.00 98.00 97.00 94.00 96.00 1.40 1.01 0.85 0.75 0.69
PPI++ 22.15 14.16 11.56 9.86 9.66 94.00 99.00 93.00 99.00 92.00 1.10 0.78 0.64 0.55 0.49
GAI 6.64 4.34 4.42 3.95 4.62 100.00 100.00 100.00 100.00 100.00 1.12 0.80 0.65 0.57 0.50
Primary at nP = 50 and PPI at nP = 100, but moderately wider than Primary and PPI++ at nP = 150.
Naive yields the narrowest intervals around the biased point estimates.
Appendix G: Pricing Study with High-dimensional Auxiliary Information
We extend the auxiliary information to include persona and demographic features:z=
[z,persona,demographics ] ∈R 115, where z is the scalar AI prediction, persona includes 54 psychometric
features, and demographics includes 60 indicator variables. The outcome model remainsX= [1,price].
We estimateg(X,z) usingℓ 1-regularized logistic regression (C= 0.01) with 5-fold cross-fitting.
Results.Table 22 reports results across 50 Monte Carlo trials.
Panel (a) shows GAI achieves substantially lower MAPE. Panel (b) shows GAI maintains 100% coverage
across all sample sizes while Naive undercovers (50%). Panel (c) shows GAI produces CI widths comparable
to Primary and PPI++ while achieving better point estimation. Decision errors (Table 23): GAI averages
0.00% vs 1.20% for PPI, 1.80% for PPI++, and 2.20% for Primary.
Table 24 reports p-values. GAI achieves significant MAPE reductions at all sample sizes. For CI width,
GAI and PPI++ produce comparable intervals.

Lu et al.:Generative Augmented Inference
52
Table 23 Decision Errors for Pricing Study with High-dimensional Auxiliary Information (% of all CIs)
Methodn P =100n P =200n P =300n P =400n P =500
Primary 4.00 2.00 3.00 0.00 2.00
Naive 0.00 0.00 0.00 0.00 0.00
PPI 2.00 0.00 1.00 2.00 1.00
PPI++ 4.00 0.00 4.00 0.00 1.00
GAI 0.00 0.00 0.00 0.00 0.00
Table 24 Paired t-test p-values (GAI vs benchmarks) for Pricing Study with High-dimensional Auxiliary
Information
(a) MAPE (b) 95% CI Coverage (c) 95% CI Width
Method 100 200 300 400 500 100 200 300 400 500 100 200 300 400 500
Primary 7e-10 4e-11 9e-9 4e-9 1e-5 0.06 0.18 0.06 0.32 0.02 7e-4 9e-6 5e-4 0.06 4e-5
Naive 6e-49 1e-58 4e-44 3e-45 4e-42 ≈0≈0≈0≈0≈0 8e-58 2e-69 3e-71 6e-69 3e-71
PPI 5e-9 1e-9 4e-8 2e-8 4e-10 0.06 0.16 0.18 0.06 0.10 8e-16 6e-31 2e-38 2e-45 6e-53
PPI++ 3e-9 2e-9 1e-7 2e-9 5e-6 0.03 0.32 0.05 0.32 0.01 0.07 6e-4 2e-5 2e-7 9e-8
Notes:≈0 represents p-value<10 −300.
Table 25 Pricing Study with High-dimensional Covariates: MAPEs, coverage probabilities, and CI widths
(a) MAPE (%) (b) 95% CI Coverage (%) (c) 95% CI Width
Method 100 200 300 400 500 100 200 300 400 500 100 200 300 400 500
Primary – 73.83 25.72 15.65 11.68 48.97 84.44 89.97 94.46 94.21 – 2.57 1.09 0.77 0.57
Naive 6.61 5.93 5.40 5.08 4.77 94.31 93.85 94.18 93.67 92.62 0.34 0.31 0.27 0.27 0.23
PPI N/A 38.16 97.06 56.76 52.33 N/A 100.00 99.91 99.85 99.91 N/A 5.30 57.75 19.14 16.90
PPI++ N/A 24.55 25.10 15.66 11.32 N/A 91.35 91.92 94.81 93.32 N/A 4.04 4.15 1.11 0.47
GAI 3.95 3.80 3.68 3.47 3.32 100.00 99.44 98.85 98.95 99.15 0.81 0.57 0.44 0.44 0.39
Notes: “–” indicates Primary estimator values exceeding 1,000 due to quasi-complete separation in unregularized
logistic regression at small sample sizes. “N/A” indicates PPI/PPI++ failed to produce valid estimates due to
singular Hessian matrices arising from extreme predicted probabilities.
Appendix H: Pricing Study with High-dimensional Covariates and Scalar Auxiliary
Information
This appendix examines a setting where the outcome model includes high-dimensional covariates (X ∈R 115,
reduced to 77 PCA components) while auxiliary information remains scalar (z∈ {0,1}). This confirms GAI
outperforms benchmarks even when the auxiliary prediction provides no extra information beyond what
PPI-based methods can exploit.
We estimateg(X, z) usingℓ 1-regularized logistic regression (C= 0.01) with 5-fold cross-fitting.
Results.Table 25 reports results across 50 Monte Carlo trials.
Panel (a) shows GAI achieves MAPE of 3.3–3.9% across all sample sizes, while Naive exhibits 4.8–6.6%
and PPI-based methods 11–97%. PPI/PPI++ fail at nP = 100 due to quasi-complete separation. Statistical
tests confirm GAI’s improvements (Table 27).
Panel (b) shows GAI maintains coverage near 99%, while Primary undercovers severely at small nP (49%
at nP = 100). Decision errors (Table 26): GAI averages 0.71% vs 2.33% for PPI++, 3.26% for Naive, and

Lu et al.:Generative Augmented Inference
53
Table 26 Decision Errors for Pricing Study with High-dimensional Covariates (% of all CIs)
Methodn P =100n P =200n P =300n P =400n P =500
Primary 22.44 6.69 3.87 1.82 1.92
Naive 3.03 3.13 3.03 3.23 3.87
PPI N/A 0.00 0.04 0.09 0.00
PPI++ N/A 4.17 3.55 1.70 2.24
GAI 0.00 0.56 1.15 1.05 0.77
Notes: PPI/PPI++ failed to produce valid estimates atn P = 100 due to singular Hessian matrices.
Table 27 Paired t-test p-values (GAI vs benchmarks) for Pricing Study with High-dimensional Covariates
(a) MAPE (b) 95% CI Coverage (c) 95% CI Width
Method 100 200 300 400 500 100 200 300 400 500 100 200 300 400 500
Primary 2e-19 5e-15 1e-16 7e-22 9e-19 3e-39 2e-11 6e-7 8e-7 9e-9 1e-10 1e-21 4e-26 1e-7 2e-5
Naive 3e-50 7e-27 4e-31 6e-31 2e-46 2e-23 1e-21 1e-19 7e-24 1e-27 2e-14 1e-12 1e-43 2e-3 1e-4
PPI – 7e-3 3e-5 1e-5 3e-3 – 1e-7 9e-18 3e-15 5e-7 – 0.20 0.04 0.03 0.17
PPI++ – 0.12 2e-3 2e-6 2e-4 – 0.17 4e-3 7e-8 5e-7 – 0.37 0.08 0.01 0.10
Notes: “–” indicates PPI/PPI++ failed atn P = 100 due to singular Hessian matrices.
7.35% for Primary. Panel (c) shows GAI intervals are narrower than PPI/PPI++ (0.39–0.81 vs 0.47–4.15)
while maintaining valid coverage.
Table 27 reports p-values. GAI achieves significant MAPE reductions and coverage improvement at all
sample sizes.
Appendix I: Supporting Results for Section 5
This appendix collects the proofs of the results in Section 5 together with an example demonstrating that the
dominance guarantee can fail outside the random-labeling design.
I.1. Proof of Theorem 1
In the proof, for simplicity we assume without loss of generality that we can split the dataset into I and I c,
each of sizen. We obtainbe(·) and bg(·) onI c and estimate bβonI. Let us define
τ(Ξ;e,g) :=X ⊤

g(X,z)− w e(X,z) (g(X,z)−y)  (26)
soΨ(Ξ; e, g; β) =X ⊤∇b(Xβ) −τ (Ξ; e, g) for all β∈ B. Throughout these proofs we abbreviate the nuisance
estimation errors by ∆ g := bg(X, z) − g∗(X, z) and ∆ e := be(X, z) −e ∗(X, z), suppressing the arguments (X , z)
when no confusion arises. For simplicity, following the empirical process literature (see Van der Vaart 2000,
Vaart and Wellner 2023), we often use the shorthand notation Pnf to denote the empirical expectation of a
function f based on data in I and Gnf to denote the empirical process based on data in I; the population
expectation of f is written E[f ]. With the boundedness assumption on X , we assume that there is C such
that for anyX∈ X,∥X∥,∥X∥ F ⩽C. We letB(x, ϵ) denote an open ball of radiusϵaroundx∈R q.
The next lemma establishes that our score function given in 7 is valid and states the key consequence of its
Neyman orthogonal design.
Lemma 1(Score F unction and Neyman Orthogonality).It holds that
E[Ψ(e∗,g ∗;β ∗)] = 0andP nτ(be,bg)−P nτ(e ∗,g ∗) =o P (n−1/2).

Lu et al.:Generative Augmented Inference
54
The next two key lemmas explore the concavity of our loss function. The first one clarifies the convergence
rate of the empirical score functions. Building on this, we present a consistency proof.
Lemma 2(Rates of Empirical Scores).It holds that
PnΨ  e∗,g ∗; bβ ,inf β∈B PnΨ  be,bg;β  =o P (1/√n).
Lemma 3(Consistency). bβ→ P β∗.
With these lemmas we finish the proof of the main result. For ease of exposition, from this point on we
suppress e∗ andg ∗ inΨ( ·; e∗, g∗; β) and write it asΨ( ·; β). We first establish that the score function is locally
Lipschitz. Indeed, fix an arbitraryϵand considerβ 1,β 2 ∈B(β ∗, ϵ), we have
∥Ψ(Ξ;β 1)−Ψ(Ξ;β 2)∥=
X⊤∇b(Xβ1)−X ⊤∇b(Xβ2)  = X⊤ Z 1
0
∇2b(X(β 1 +t(β 2 −β 1)))dt(β 2 −β 1)

⩽
X⊤ Z 1
0
∇2b(X(β 1 +t(β 2 −β 1)))dt
 ∥β2 −β 1∥⩽∥X∥ Z 1
0
∇2b(X(β 1 +t(β 2 −β 1)))  dt∥β2 −β 1∥
⩽∥β 2 −β 1∥

∥X∥sup
β∈B(β∗,ϵ)
∥∇2b(Xβ)∥
!
⩽C 1∥X∥∥β2 −β 1∥
where we define C1 := supβ∈B(β∗,ϵ),X∈ ˘X ∥∇2b(Xβ)∥<∞ . Indeed, the supremum is finite because it is taken
over the compact set ˘X ×B(β ∗, ϵ)and ∇2b(·) is continuous; consequently the local Lipschitz modulus
m(Ξ) := C1∥X∥ satisfies E[m2] = C 2 1 E  ∥X∥2 <∞ . The class moreover admits a square-integrable envelope.
WritingΨ(Ξ;β) =X ⊤∇b(Xβ)−τ(Ξ;e ∗,g ∗), theβ-dependent term is uniformly bounded overβ∈ B(β ∗, ϵ)
andX ∈ ˘X by the continuity of ∇b on this compact set, so it suffices to verify that E  ∥Ψ(Ξ; e∗, g∗; β∗)∥2 <∞ .
DecomposeΨ(Ξ; e∗, g∗; β∗) = ζ + w e∗ π with ζ =X ⊤ ∇b(Xβ∗) − g∗ and π =X ⊤(g∗ − y). The irreducible-noise
block is finite by Assumption 1(iii): usingw/e ∗ ⩽1/κand∥X∥ F ⩽C,
E
h w e∗ π  2i ⩽κ −2 E  ∥X∥2 F ∥Cov(y|X,z)∥  ⩽κ −2C 2 ˜σ2 <∞.
The representational block is finite by Assumption 1(iv): sinceg ∗ = E[y | X, z], conditional
Jensen gives E∥g∗∥2 ⩽E∥ y∥2 <∞ , so E  ∥ζ∥2 ⩽ 2C 2 supX∈ ˘X ∥∇b(Xβ∗)∥2 + E∥g∗∥2 <∞ . Hence
E

∥Ψ(Ξ; e∗, g∗; β∗)∥2 <∞ , and the envelope ∥Ψ(·; e∗, g∗; β∗)∥ + m(·) diam  B(β ∗, ϵ)  is square-integrable.
Therefore, by Example 19.7 and Theorem 19.5 in Van der Vaart (2000), {Ψ(·;β) :β∈B(β ∗, ϵ)}forms a
Donsker class. By Lemma 3, bβ→ P β∗. Then, by Theorem 19.9 in Van der Vaart (2000), it holds that
GnΨ( bβ)−G nΨ(β∗)→ P 0.Thus,
√n(E[Ψ( bβ)]−E[Ψ(β ∗)]) =−  GnΨ( bβ)−G nΨ(β∗)  + √nPnΨ  bβ  − √nPnΨ  β∗ (a) =− √nPnΨ  β∗ +o P (1),
where (a) follows from Lemma 2. We apply the Taylor expansion on the left-side of the equation, by continuous
mapping, we have
√n h E[X⊤∇2b(Xβ∗)X]  bβ−β ∗ +o P (1)  bβ−β ∗  i =− √nPnΨ  β∗ +o P (1) =O P (1).(27)
As shown in the proof of Lemma 2,E[X⊤∇2b(Xβ∗)X] is invertible. Therefore, (27) implies that √n  bβ−β ∗  =
OP (1). Therefore, applying (27) again,
√n  bβ−β ∗  =−  E[X⊤∇2b(Xβ∗)X] −1√nPnΨ  β∗ +o P (1).

Lu et al.:Generative Augmented Inference
55
Finally, since E[Ψ(e∗, g∗; β∗)] = 0 by Lemma 1 and E  ∥Ψ(e∗, g∗; β∗)∥2 <∞ as established above, the
multivariate central limit theorem gives √nPnΨ(β∗) ⇝N  0,E [ΨΨ⊤]  with E[ΨΨ⊤] finite; in particular √nPnΨ(β∗) = OP (1), which justifies the order bound asserted in (27). Combined with the invertibility of
J= E[X⊤∇2b(Xβ∗)X], the displayed linearization and Slutsky’s theorem yield √n( bβ−β ∗) ⇝N  0, ΣGAI
withΣ GAI =J −1E[ΨΨ⊤]J−1 finite, as claimed in Theorem 1.
I.2. Dominance over Primary-Only
The following corollary strengthens Theorem 1 under known ρ (dropping the rate and sup-norm conditions
of Assumption 2) and records the comparison with primary-only estimation. Its dominance conclusion is
the primary-only special case of Theorem 2, but we prove it directly from the analysis of Theorem 1, both
because of the weaker assumptions and because the direct argument is reused in the covariate-shift proofs.
Corollary 2(Dominance over Primary-Only). Suppose Assumptions 1 and 3 hold and that bg is
L2-consistent, ∥bg− g∗∥Q,2 = o(1), with be≡ρ. Then the conclusion of Theorem 1 continues to holdwithoutthe
rate and sup-norm conditions of Assumption 2. Moreover, let bβP be the primary-only estimator obtained from
human data alone, i.e., a solution to P i∈DP ∇βℓ(Xi,y i; β) = 0. Then √n  bβP −β ∗  ⇝N  0,Σ P , where
ΣP = 1 ρ J−1E[∇βℓ(X,y;β ∗)∇βℓ(X,y;β ∗)⊤]J −1 andΣ P ⪰Σ GAI. Also,Σ P ≻Σ GAI as long asρ <1and
E

X⊤  ∇b  Xβ∗ −E[y|X,z]  ·  ∇b  Xβ∗ −E[y|X,z] ⊤ X  ≻0.
I.2.1. Proof of Corollary 2Asymptotic normality of the GAI estimator.We first record why the
conclusion of Theorem 1 continues to hold under Assumption 3 with Assumption 2 weakened to the L2-
consistency of bg. With be≡e∗ ≡ρ known, the proof of Theorem 1 changes only in the orthogonality step
(Lemma 1), at three points: (i) the remainder Pnτ (be,bg) −P nτ (e∗, g∗) collapses to term (I) alone, which
islinearin bg− g∗ and is oP (n−1/2) under ∥bg− g∗∥Q,2 = o(1) by the conditional Markov argument there,
requiring no convergence rate; (ii) the second-order remainder term (III) is absent, as it carries the factor
be−e∗ = 0; and (iii) term (II), driven by the estimation error of be, vanishes for the same reason, so no rate or
sup-norm condition on a propensity estimate enters. All other steps—consistency (Lemma 3), the Donsker
class and Taylor expansion, and the central limit theorem—are unchanged, and √n( bβ−β ∗) ⇝N (0, ΣGAI)
follows as in Theorem 1.
Dominance.To start, we first note that the empirical score equation, i.e., P i∈DP ∇βℓ(Xi,y i; β) = 0, is
equivalent to Pn i=1 wi∇βℓ(Xi,y i; β) = 0 . Note that by independence of w with respect to other random
variables, it holds that
E[w∇ βℓ(X,y;β ∗)] =ρE[∇ βℓ(X,y;β ∗)] = 0.
Thus, under the preset assumptions, it is easy to show that with probability approaching one, the solu-
tion to this equation, i.e., bβP, exists, and √n  bβP −β ∗  ⇝N  0,Σ P . We skip the proof. We further
note that ∇βℓ(X, y; β∗) := ζ(X, z) +π(X, y, z) where ζ(X, z) :=X ⊤ (∇b(Xβ∗)−g ∗(X,z)) and π(X, y, z) =
X⊤ (g∗(X,z)−y) and, becauseE[g ∗(X,z)−y|X,z] = 0, we have
ΣP = 1 ρ  J−1E  ζ(X,z)ζ(X,z) ⊤ J−1 +J −1E  π(X,y,z)π(X,y,z) ⊤ J−1  .(28)
Furthermore, observe thatΨ(Ξ;e,g;β) =ζ(X,z) + w ρ π(X,y,z), so
ΣGAI =J −1E  ζ(X,z)ζ(X,z) ⊤ J−1 + 1 ρ J−1E  π(X,y,z)π(X,y,z) ⊤ J−1.(29)
The conclusion follows straightforwardly given (28) and (29).

Lu et al.:Generative Augmented Inference
56
I.3. Proof of Theorem 2
Throughout we work under Assumption 1 and Assumption 3, so e≡ρ∈ (0, 1) is known, w⊥ (X, y, z), andJ=
E[X⊤∇2b(Xβ∗)X] ≻ 0. We use the full-data scoreS:=X ⊤(∇b(Xβ∗) −y) = ζ + π with ζ =X ⊤(∇b(Xβ∗) −g∗),
π =X ⊤(g∗ − y),g ∗ = E[y | X, z], so that E[π| X, z] =0. We abbreviate the (X , z)-measurable score correction
byh:=λX ⊤(∇b(Xβ∗)−f), wheref=f(X,z) does not depend ony.
Step 1 (mean-zero at the commonβ ∗).Evaluating the family score (11) atβ ∗ and taking expectations,
E

Ψλ,f (Ξ;β ∗)  (a) =E  w ρ  E  X⊤(∇b(Xβ∗)−y)  −E  w ρ  E[h] +E  1−w 1−ρ  E[h]
(b)
=E

X⊤(∇b(Xβ∗)−y)  −E[h] +E[h] =E[S] (c) =0,
where (a) factors the propensity weights out of the (X , y, z)-measurable terms using w⊥ (X, y, z) and writes
h= λX⊤(∇b(Xβ∗) − f), ( b) uses E[w/ρ] = E[(1 −w )/(1 −ρ )] = 1 so that the two λ-terms cancel, and ( c) is
the population first-order condition E[X⊤(∇b(Xβ∗) − y)] =0defining β∗. Hence every member of the family
has a mean-zero estimating equation at thesameβ ∗.
Furthermore, for any β, again by w⊥ (X, y, z) and E[w/ρ] = E[(1 −w )/(1 −ρ )] = 1, the two λ-terms of
E[Ψλ,f (Ξ; β)] cancel exactly as in Step 1, so the population estimating function ofeverymember coincides
with that of the primary GLM: ¯Ψλ,f (β) := E[Ψλ,f (Ξ; β)] = E[X⊤(∇b(Xβ) − y)] = ∇L(β), where L(β) :=
E[ℓ(X, y; β)]. By Assumption 1(i)–(ii), ∇2L(β) = E[X⊤∇2b(Xβ)X] ≻ 0 for every β∈ B(the fact established
in the proof of Lemma 2), so L is strictly convex on the convex set B with unique minimizer β∗, which is thus
the unique zero of ¯Ψλ,f on B, with common nonsingular derivative ∇ ¯Ψλ,f (β∗) =J, which is straightforward
to verify by algebra again usingw⊥(X,y,z) andE[w/ρ] =E[(1−w)/(1−ρ)] = 1.
Step 2 (consistency and asymptotic normality).Because λ∈ [0, 1], one can easily verify that ¯Ψλ,f (β) =
˜ℓλ,f (Ξ;β), where ˜ℓλ,f (Ξ;β) is convex inβand defined as
˜ℓλ,f (Ξ;β) :=
 w
ρ (1−λ) + 1−w 1−ρ λ  b(Xβ)− w ρ y⊤Xβ+  w ρ + 1−w 1−ρ  λf ⊤Xβ.
Therefore, mimicking the steps in the proof of Lemma 2, we can show that with probability approaching
one, there is a solution, bβλ,f , to the minimization problem and gives PnΨλ,f (· ; β) =0. This implies that with
probability that goes to one, it also solves minβ∈B Pn ˜ℓλ,f (·; β), whose solution is consistent by Theorem 2.7 of
Newey and McFadden (1994).
Since ρ∈ (0, 1) is known, the weights w/ρ and (1 −w )/(1 −ρ ) are bounded by 1 /ρ and 1/(1 −ρ ). Grouping
(11) at β∗ aroundS=X ⊤(∇b(Xβ∗) − y) andh= λX⊤(∇b(Xβ∗) − f) givesΨ λ,f (Ξ; β∗) = w ρ (S − h) + 1−w 1−ρ h.
On the compact set ˘X we have ∥X∥F ⩽C and, by continuity of ∇b,X ⊤∇b(Xβ∗) is bounded; moreover
E∥X⊤y∥2 ⩽C 2 E∥y∥2 <∞ by Assumption 1(iv), and E∥X⊤f ∥2 ⩽C 2 E∥f ∥2 <∞ becausef ∈L 2(X, z). Hence
E

∥Ψλ,f (Ξ; β∗)∥2 <∞ , soΩ( λ, f) is finite. The only β-dependent part ofΨ λ,f is  w ρ (1−λ)+ 1−w 1−ρ λ  X⊤∇b(Xβ),
a bounded random multiple ofX ⊤∇b(Xβ); the local Lipschitz and envelope bounds of the proof of Theorem 1
therefore apply verbatim, and {Ψλ,f (·; β) : β∈ B(β ∗, ϵ)}is a Donsker class with square-integrable envelope
by Example 19.7 and Theorem 19.5 in Van der Vaart (2000). Then, the rest of the proof is the same as that
of Theorem 1. The form of the asymptotic matrix is easy to compute directly.

Lu et al.:Generative Augmented Inference
57
Step 3 (closed form forΩ).Regrouping (11) atβ ∗ aroundSandh,
Ψλ,f (Ξ;β ∗) = w ρ  S−h  + 1−w 1−ρ h.(30)
Taking the outer product and the expectation,
Ω(λ,f)
(a)
=E
 w2
ρ2 (S−h)(S−h) ⊤

+E
 w(1−w)
ρ(1−ρ)

(S−h)h ⊤ +h(S−h) ⊤ +E  (1−w) 2
(1−ρ) 2 hh⊤

(b)
= 1 ρ E  (S−h)(S−h) ⊤ + 1 1−ρ E[hh⊤],(31)
where (a) expands the outer product of (30), and ( b) uses w∈ {0, 1}, so that w2 = w, (1 −w )2 = 1−w , and
w(1 −w ) = 0, whence the cross term vanishes identically; then w⊥ (X, y, z) gives E[w2/ρ2] = E[w/ρ2] = 1/ρ
and E[(1 −w )2/(1 −ρ )2] = 1/(1 −ρ ), factoring out of the (X , y, z)-measurable blocks. This is the second
equality of (12). To obtain the first, complete the square around (1 −ρ )Sby writing δ :=h − (1 −ρ )S, so
S−h=ρS−δandh= (1−ρ)S+δ. Substituting into (31),
Ω(λ,f)
(c)
= 1 ρ E  (ρS−δ)(ρS−δ) ⊤ + 1 1−ρ E  ((1−ρ)S+δ)((1−ρ)S+δ) ⊤
(d)
=

ρ+ (1−ρ)

E[SS⊤] +  −1 + 1  E[Sδ⊤] +E[δS ⊤]  +  1 ρ + 1 1−ρ  E[δδ ⊤]
(e)
=E[SS ⊤] + 1 ρ(1−ρ) E[δδ ⊤],
where (c) substitutes the two reparametrized increments, ( d) collects theSS ⊤, cross, and δδ ⊤ blocks (the
cross-block coefficient is 1 ρ (−ρ) + 1 1−ρ (1 −ρ ) = −1 + 1 = 0), and ( e) uses ρ + (1 −ρ ) = 1 together with
1
ρ + 1 1−ρ = 1 ρ(1−ρ) . This is exactly (12) and completes part (i).
Step 4 (Pythagoras and Loewner minimization).Resolve δ into its (X , z)-measurable and conditionally
mean-zero parts. With the residualr:=λ(∇b(Xβ ∗)−f)−(1−ρ)(∇b(Xβ ∗)−g ∗)∈R k,
δ=h−(1−ρ)S
(a)
=

X⊤r  −(1−ρ)π,(32)
where (a) writesh= λX⊤(∇b(Xβ∗) − f) and (1 −ρ )S= (1 −ρ )X⊤(∇b(Xβ∗) − y) = (1−ρ )X⊤(∇b(Xβ∗) −
g∗) + (1−ρ )X⊤(g∗ − y), then collects the (X , z)-measurable terms intoX ⊤rand identifies the remainder
−(1−ρ)X ⊤(g∗ −y) =−(1−ρ)π. SinceX ⊤ris (X,z)-measurable andE[π|X,z] =0,
E[δδ ⊤] (b) =E  (X⊤r)(X⊤r)⊤ + (1−ρ) 2 E[ππ ⊤],(33)
where (b) is the Pythagorean identity: the cross terms E[(X⊤r)π⊤] and E[π(X⊤r)⊤] vanish by the law of
iterated expectations, sinceX ⊤rpasses through the conditional expectation given (X , z) and E[π| X, z] =0.
The first summand of (33) is the only ( λ, f)-dependent term, is positive semidefinite, and is Loewner-
minimized—ineverydirection simultaneously—at its zero valueX ⊤r=0a.s. Combining δ =X ⊤r − (1 −ρ )π
from (32) withh= (1 −ρ )S+ δ andS −π = ζ gives the identityh= (1 −ρ )ζ +X ⊤r; henceX ⊤r=0a.s. is
equivalentlyh=h ⋆ := (1 −ρ )ζ, which corresponds to δ = −(1 −ρ )π. This optimum lies inside the family:
taking λ = 1 −ρ andf=g ∗ givesh= (1 −ρ )X⊤(∇b(Xβ∗) − g∗) = (1 −ρ )ζ =h ⋆ andr=0. Substituting
X⊤r=0into (12) through (33),
ΩGAI (c) =E[SS ⊤] + 1 ρ(1−ρ) (1−ρ) 2 E[ππ ⊤] (d) =E[ζζ ⊤] +E[ππ ⊤] + 1−ρ ρ E[ππ ⊤] (e) =E[ζζ ⊤] + 1 ρ E[ππ ⊤],

Lu et al.:Generative Augmented Inference
58
where (c) sets the ( λ, f)-dependent block to zero, ( d) uses the orthogonal decomposition E[SS⊤] = E[ζζ ⊤] +
E[ππ ⊤] (valid becauseS= ζ + π with E[π| X, z] =0, so the ζ–π cross terms vanish) and simplifies
(1−ρ)2
ρ(1−ρ) = 1−ρ ρ , and ( e) combines 1 + 1−ρ ρ = 1 ρ on the E[ππ ⊤] block. This is (13). For the gap, subtract the GAI
values from (12) and (33) and conjugate byJ −1:
Σ(λ,f)−Σ GAI (f) =J −1 Ω(λ,f)−Ω GAI J−1 (g) = 1 ρ(1−ρ) J−1 E  (X⊤r)(X⊤r)⊤ J−1 (h) ⪰0,
where (f ) usesΣ=J −1ΩJ−1 with the commonJfrom Step 2, ( g) cancels the ( λ, f)-free blocks E[SS⊤] and
(1−ρ)2
ρ(1−ρ) E[ππ ⊤] betweenΩ( λ, f) andΩ GAI via (33), leaving only 1 ρ(1−ρ) E[(X⊤r)(X⊤r)⊤], and (h) holds because
E[(X⊤r)(X⊤r)⊤] is positive semidefinite, 1 ρ(1−ρ) > 0, and congruence byJ −1 preserves the Loewner order.
This is (14). Equality holds if and only if the only ( λ, f)-dependent block vanishes, i.e. E[(X⊤r)(X⊤r)⊤] =0,
equivalentlyX ⊤r=0almost surely; for GAI,r=0identically. This proves part (iii), and hence the weak
Loewner dominance over every member, with strictness whenever the correspondingX ⊤r ̸=0on a set of
positive probability.
The optimal correctionh ⋆ = (1−ρ )ζ, and thusΩ GAI andΣ GAI, is unique becauseX ⊤r=0a.s. pins downh.
The pair ( λ, f) attaining it is not unique:X ⊤r=0holds whenever λ(∇b(Xβ∗) − f) = (1 −ρ )(∇b(Xβ∗) − g∗),
i.e. for any λ̸ = 0 withf= ∇b(Xβ∗) − 1−ρ λ (∇b(Xβ∗) − g∗), of which GAI ( λ = 1 −ρ∈ (0, 1),f=g ∗) is the
canonical representative.
Step 5 (special-case collapses).We verify the two members directly from (11) before. Note that although PPI
and PPI++ are formulated as convex loss minimization problems (M-estimators), their first-order conditions
are exactly special cases of (11) with the specified ( λ, f). The asymptotic distribution of the M-estimator
formulation is asymptotically equivalent to our Z-estimator formulation.
(i) GAI,λ= 1−ρ,f=g ∗.Substituting,
Ψ1−ρ,g∗ (Ξ;β)
(a)
= w ρ X⊤ h (∇b(Xβ)−y)−(1−ρ)(∇b(Xβ)−g ∗) i + 1−w 1−ρ (1−ρ)X ⊤(∇b(Xβ)−g ∗)
(b)
= w ρ X⊤ ρ∇b(Xβ)−y+ (1−ρ)g ∗ + (1−w)X ⊤(∇b(Xβ)−g ∗)
(c)
=X ⊤
h
∇b(Xβ)−g ∗ + w ρ (g∗ −y) i ,
where (a) inserts λ = 1−ρ ,f=g ∗, (b) expands the bracket inside w/ρ as (1 − (1 −ρ ))∇b(Xβ) − y+ (1 −ρ )g∗ =
ρ∇b(Xβ) − y+ (1 −ρ )g∗ and cancels (1 −ρ ) in the second term, and ( c) groups the ∇b andg ∗ coefficients: the
∇b(Xβ) terms give w ρ ρ + (1−w ) = w + 1−w = 1, and theg ∗ terms give w ρ (1 −ρ ) − (1 −w ) = w ρ −w− 1 +w =
w
ρ − 1, so the constant-in- β part is −g∗ + w ρ (g∗ − y) after combining with the − w ρ yterm. This is exactly the
GAI score (7) withe≡ρ.
(ii) Primary-only, λ = 0.Setting λ = 0 in (11) annihilateshand the unlabeled block, leavingΨ 0,f (Ξ; β) =
w
ρ X⊤(∇b(Xβ) − y), the IPW human-labels-only score, whose asymptotic variance isΣ P from Corollary 2;
this member uses no predictionf, consistent with the entry “λ= 0” of part (ii).
Step 6 (feasible GAI).Part (iv) concerns the feasible GAI estimator bβ computed by Algorithm 1 with the
known propensity be≡ρ and a cross-fitted nuisance bg, in place of the oracle member (1 −ρ, g∗) analyzed in
Steps 1–5. By Corollary 2 (proved in Section I.2.1, using exactly the LQ,2-consistency of bg and be≡ρ under
Assumption 3, and no rate or sup-norm condition), this feasible estimator satisfies √n( bβ−β ∗) ⇝N (0, ΣGAI),
the same limit law as the oracle GAI member of parts (ii)–(iii). Hence the Loewner dominance established in
part (iii) applies verbatim to bβ, which proves part (iv). This completes the proof of Theorem 2.

Lu et al.:Generative Augmented Inference
59
I.4. Proof of Lemma 1
To begin, first we note that by the definition ofτ(e ∗,g ∗)
E[τ(e ∗,g ∗)] =E

X⊤

g∗(X,z)− w e∗(X,z) (g∗(X,z)−y) 
(a)
=E

X⊤

g∗(X,z)− E[w|X,z] e∗(X,z)  g∗(X,z)−E[y|X,z]  (b) =E  X⊤E[y|X,z]  =E  X⊤y  ,
where (a) follows from the law of iterated expectations and the conditional independence of w andy, and (b)
follows from the definition thatE[w|X,z] =e ∗(X,z). Therefore,
E[Ψ(e∗,g ∗;β ∗)] =E  X⊤∇b(Xβ∗)−τ(Ξ;e ∗,g ∗)  =E  X⊤∇b(Xβ∗)−X ⊤y  = 0.
Here the last equality is the population first-order condition (2) defining β∗. This proves the first part. For
the second, we notice that
√n(P nτ(be,bg)−P nτ(e ∗,g ∗)) = √nPn h 1− w e∗  X⊤∆g i | {z }
(I)
+ √nPn
 w∆ e
bee∗ X⊤(g∗ −y)

| {z }
(II)
+ √nPn
 w∆ e
bee∗ X⊤∆g

| {z }
(III)
.
We treat each term separately. For (I), we note that
E

1− w e∗  X⊤∆g

 I c  =E  1− E[w|X,z, I c] e∗  X⊤∆g

 I c  = 0 (34)
so (I) has zero mean. Therefore, by Markov inequality
P

∥(I)∥⩾ϵ

I c ⩽ E[∥(I)∥2|I c] ϵ2 = 1 ϵ2 dX j=1 Var √nPn h 1− w e∗  x⊤ (j)∆g i

I c  = 1 ϵ2 dX j=1 Var  1− w e∗  x⊤ (j)∆g

I c 
= 1 ϵ2 E   1− w e∗  X⊤∆g  2

 I c  .(35)
From here, we note that
  1− w e∗  X⊤∆g  2 Q,2 ⩽ 4 κ2 X⊤∆g 2 Q,2 ⩽ 4C 2 κ2 ∥∆g∥2 Q,2 (c) →0,
which implies the RHS of (35) converges to zero in probability by the Markov’s inequality. Here (c) uses only
the L2-consistency ∥bg− g∗∥Q,2 → 0 implied by Assumption 2; no convergence rate is needed for term (I).
Since P(∥(I)∥⩾ϵ|I c) is bounded therefore uniformly integrable, we can take expectation and conclude that
(I) is oP (1). An argument similar to (34) shows that (II) has zero mean. An argument similar to (35) shows
that
P

∥(II)∥⩾ϵ

 I c ⩽ 1 ϵ2 E
" w∆ e bee∗ X⊤(g∗ −y)  2

 I c # (d) = 2 κ2ϵ2 E w∆ e X⊤(g∗ −y) 2

 I c  +o P (1)
= 2 κ2ϵ2 E
"
|∆e|2
dX
j=1
x⊤ (j)Cov(y|X,z, I c)x(j)

 I c # +o P (1) (e) ⩽ 2˜σ2 κ2ϵ2 E " |∆e|2 dX j=1 x⊤ (j)x(j)

 I c # +o P (1)
= 2˜σ2
κ2ϵ2 E

|∆e|2∥X∥2 F

 I c  +o P (1) = 2C 2 ˜σ2 κ2ϵ2 E  |∆e|2

 I c  +o P (1),(36)
where (d) follows because for allXandz, (1) by assumption e∗(X, z) ⩾κ and (2) Assumption 2 states
that supX,z |∆e| →P 0, so with probability approaching one it holds that be(X, z) ⩾κ/ 2. (e) holds because
the distribution ofyis independent of I c so Cov(y|X, z, Ic) = Cov(y|X, z) and ∥Cov(y|X, z)∥⩽˜σ2. By an

Lu et al.:Generative Augmented Inference
60
argument similar to the above discussion regarding (I), we have E

|∆e|2

 I c = oP (1). Therefore, (II) is also
oP (1). For the third term, we have
P

∥(III)∥∞ ⩾ϵ

 I c ⩽ dX
j=1
P
√n

Pn w∆ e bee∗ x⊤ (j)∆g

 ⩾ϵ

 I c  ⩽ √n ϵ dX j=1 E 

 w∆ e bee∗ x⊤ (j)∆g

 I c 
(f)
⩽ 2√n κ2ϵ dX j=1 E 

∆e x⊤ (j)∆g

 I c +o P (1) (g) ⩽ 2√n κ2ϵ dX j=1 E  |∆e| x(j)  ∥∆g∥

 I c +o P (1)
⩽ 2√nC κ2ϵ dX j=1 E  |∆e| ∥∆g∥

 I c +o P (1),
where (f) follows from an argument similar to above and (g) follows from the Cauchy–Schwarz inequality.
Finally, we have
E[|∆ e| ∥∆g∥]⩽∥∆ e∥Q,2 ∥∆g∥Q,2 ⩽α(n) 2/nr1+r2 =o(n −1/2).
Therefore,P(∥(III)∥ ∞ ⩾ϵ|I c) iso P (1) and (III) iso P (1) too. We conclude the proof.
I.5. Proof of Lemma 2
For any functionse(·) andg(·), data point Ξ, andβ, let us define
¯ℓ(Ξ;e,g;β) :=b(Xβ)−

g(X,z)− w e(X,z) (g(X,z)−y) ⊤ Xβ,
so ∇β ¯ℓ(Ξ; e, g; β) =Ψ(Ξ; e, g; β) and ∇2 β ¯ℓ(Ξ; e, g; β) =X ⊤∇2b(Xβ)X ⪰ 0. Therefore ¯ℓ(·) is convex. In partic-
ular,E[ ¯ℓ(Ξ, e∗,g ∗,β)] is convex inβ. We first notice that
∇βE[¯ℓ(e∗,g ∗,β ∗)] =∇ βE[ℓ(X,y;β ∗)] +E

X⊤(y−g ∗(X,z))

1− w e∗(X,z)  = 0.
Also, for any fixed β∈ B it holds that ∇2 βE[¯ℓ(e∗, g∗,β )] = E[X⊤∇2b(Xβ)X] ≻ 0. The last inequal-
ity follows because by assumption for anyX ∈ ˘X , λmin

∇2b(Xβ)  > 0. For the purpose of contradic-
tion, if inf X∈ ˘X λmin

∇2b(Xβ)  = 0, there is a converging sequence {Xm}∞ m=1 with limit eX∈ ˘X such
that λmin

∇2b  eXβ  = 0 by continuity of ∇2b(·). This is a contradiction. Therefore, ∇2 βE[¯ℓ(e∗, g∗,β )] ≻
inf X∈ ˘X λmin

∇2b(Xβ)  ·E [X⊤X] ≻ 0. In other words, E[¯ℓ(e∗, g∗,β )] is strictly convex. Therefore, β∗ is the
unique minimum. By compactness of ˘X and continuity of b(·), we have Pn ¯ℓ(e∗, g∗; β) →P E[¯ℓ(e∗, g∗; β)] as an
application of the weak law of large numbers. By Theorem 2.7 of Newey and McFadden (1994), it holds that
there is a random sequence { ˇβn}∞ n=1 that solves minβ∈B Pn ¯ℓ(e∗, g∗; β) and converges to β∗ with probability
one. This implies that with probability one there is a sequence { ˇβn}∞ n=1 such that PnΨ(e∗, g∗; ˇβn) =0. By
Lemma 1, it holds that
√nPnΨ(be,bg; ˇβn) = √nPnΨ(e∗,g ∗; ˇβn) +√n(P nτ(e ∗,g ∗)−P nτ(be,bg)) =o P (1),(37)
or inf β∈B
PnΨ  be,bg; β  = oP (1/√n). This implies PnΨ  be,bg; bβ  = oP (1/√n). Using the argument in (37)
again, we haveP nΨ

e∗,g ∗; bβ  =o P (1/√n). This concludes the proof.

Lu et al.:Generative Augmented Inference
61
I.6. Proof of Lemma 3
The notations and definitions are the same as in the proof of the Lemma 2. Fix arbitrary ϵ1 < ϵ2 such that
B(β ∗, ϵ2)⊂ B. OnB(β ∗, ϵ2)\B(β ∗, ϵ1), by a Taylor expansion, it must be that
E[¯ℓ(e∗,g ∗;β)] =E[ ¯ℓ(e∗,g ∗;β ∗)] + 1 2 (β−β ∗)⊤E[X⊤∇2b(X ˜β)X](β−β ∗) (a) ⩾E[ ¯ℓ(e∗,g ∗;β ∗)] + c 2 ∥β−β ∗∥2
which can be further lower bounded by E[¯ℓ(e∗, g∗; β∗)] + cϵ2 1 2 , for some ˜β∈ [β∗,β ] ⊂ B(β ∗, ϵ2) that depends
on β and a universal c >0. We prove the inequality (a) as follows. It suffices to show that λmin (∇2b(Xβ))
is uniformly lower bounded by some positive number, when β ranges over B(β ∗, ϵ2) andXranges over X .
Suppose otherwise, there is then {(Xm,β m)}
∞
m=1 such that λmin (∇2b(Xmβm))→ 0. By taking subsequence is
necessary, we assume thatX m → ¯X∈ ˘X and βm → ¯β∈ B(β ∗, ϵ2)⊂ B. By assumption ¯X ¯β∈ Θ and continuity
of∇ 2b(·) impliesλ min  ∇2b  ¯X ¯β)  = 0, which contradicts our assumption.
By the convexity lemma Pollard (1991), convexity of ¯ℓ(·) and the compactness of B(β ∗, ϵ2), it holds
that Pn ¯ℓ  e∗, g∗; β  converges to E ¯ℓ  e∗, g∗; β  in probability uniformly on B(β ∗, ϵ2). Consequently, with
probability approaching one, it must be that∀β∈ B(β ∗, ϵ2)\B(β ∗, ϵ1),
Pn ¯ℓ(e∗,g ∗;β)− cϵ2 1
4 ⩾P n ¯ℓ(e∗,g ∗;β ∗) (b) ⩾P n ¯ℓ(e∗,g ∗;β) + (β−β ∗)⊤PnΨ(e∗,g ∗;β)
=P n ¯ℓ(e∗,g ∗;β) +∥β−β ∗∥ ·(β∗ −β) ⊤
∥β−β ∗∥ PnΨ(e∗,g ∗;β),
where (b) follows from subgradient inequality. This implies that
(β−β ∗)⊤
∥β−β ∗∥ PnΨ(e∗,g ∗;β)⩾ cϵ2 1 4ϵ2 .(38)
Next, consider any β∈ B \B(β ∗, ϵ2), there is ˜β = λβ + (1−λ )β∗ ∈ B(β ∗, ϵ2)\B (β∗, ϵ1). By the integral form
of the intermediate value theorem,
(β−β ∗)⊤
∥β−β ∗∥

PnΨ(e∗,g ∗;β)−P nΨ(e∗,g ∗;β ∗) 
= (β−β ∗)⊤
∥β−β ∗∥
Z 1
0
PnX⊤∇2b  X(β∗ +t(β−β ∗))  Xdt(β−β ∗)
= ( ˜β−β ∗)⊤
λ∥ ˜β−β ∗∥
Z 1
0
PnX⊤∇2b

X

β∗ + t λ ( ˜β−β ∗)  Xdt( ˜β−β ∗)
(c)
= ( ˜β−β ∗)⊤
∥ ˜β−β ∗∥
Z 1
λ
0
PnX⊤∇2b  X  β∗ +t( ˜β−β ∗)   Xdt( ˜β−β ∗)
(d)
⩾ ( ˜β−β ∗)⊤
∥ ˜β−β ∗∥
Z 1
0
PnX⊤∇2b  X  β∗ +t( ˜β−β ∗)   Xdt( ˜β−β ∗)·
= ( ˜β−β ∗)⊤
∥ ˜β−β ∗∥

PnΨ(e∗,g ∗; ˜β)−P nΨ(e∗,g ∗;β ∗)  (e) ⩾ cϵ2 1
4ϵ2
− ( ˜β−β ∗)⊤
∥ ˜β−β ∗∥ PnΨ(e∗,g ∗;β ∗),
where (c) follows from a change of variable in the integral, (d) follows because the ∇2b(·) is positive definite,
and (e) uses (38). Combining this again with (38), we conclude that with probability converging to one,
∥PnΨ(e∗,g ∗;β)∥⩾ (β−β ∗)⊤
∥β−β ∗∥ PnΨ(e∗,g ∗;β)⩾ cϵ2 1 4ϵ2 ∀β∈ B \B(β∗, ϵ1).
Finally, we note that by Lemma 2,
PnΨ  e∗, g∗; bβ  = oP (1/√n). Therefore, it must be that bβ∈B (β∗, ϵ1)
with probability converging to one. We finish the proof.

Lu et al.:Generative Augmented Inference
62
I.7. Proof of Corollary 1
This appendix provides the proof of Corollary 1, which decomposes the variance gain of GAI into two
interpretable components.
Recall that the primary-only estimator uses only labeled observations, while GAI incorporates auxiliary
data through the conditional expectation E[y | X, z]. To understand the variance gain, we decompose the
GLM score∇ βℓ(X,y;β ∗) =X ⊤(∇b(Xβ∗)−y) by inserting intermediate quantities.
From the proof of Corollary 2, the asymptotic variance of the primary-only estimator minus that of the
GAI estimator is proportional to:
ΣP −Σ GAI ∝( 1 ρ −1)·E  X⊤  ∇b(Xβ∗)−E[y|X,z]  ∇b(Xβ∗)−E[y|X,z] ⊤ X  ,(39)
where ρ∈ (0, 1) is the labeling probability of Assumption 3, so that the labeled fraction nP /n converges to ρ.
This expression is always positive semidefinite (PSD), confirming that GAI never increases variance relative
to primary-only estimation.
The variance reduction in (39) is strictly positive definite (i.e., GAI strictly dominates) whenever the inner
expectation is positive definite. We decompose the gap ∇b(Xβ∗) −E [y | X, z] into interpretable components:
∇b(Xβ∗)−E[y|X,z] =  ∇b(Xβ∗)−E[y|X] 
| {z }
(II) Model misspecification
+

E[y|X]−E[y|X,z]

| {z }
(III) Extra information inz
.(40)
Since E[y | X] = E

E[y | X, z]

 X  by the law of iterated expectations, term (III) has conditional mean zero
givenX. This implies that the cross-product between terms (II) and (III) vanishes:
E
h
(II)·(III)
⊤
i
=E
h
(II)·E

(III)
⊤
|X
i
= 0.
Therefore, the variance gain decomposes additively into two non-negative components as stated in Corollary 1.
I.8. An Example of F ailure of Dominance
Generally, if e(X, z) is carefully constructed so that it is “advantageous” to ignore the data points with
missing label, one can show the following negative result.
Example 3. (Failure of Dominance) Consider a setting with canonical GLMs such that the GLM
density is correctly specified. Assume that k = 1 and b(θ) = 1 2 θ2. In this case, we writeX=x ⊤ ∈R 1×d. We
further assume thatxis generated through a mixture distribution and there is ˜wsuch that ˜w= 1 with
probability p and zero otherwise. Also, E[xx⊤ |˜w] =Ifor all ˜w∈ {0, 1}. Conditional on ˜w, the supports of
xare disjoint and we denote them by Xw. We assume that E[y| x] =x ⊤β∗, and Var(y| x) = σ2 w whenever
x ∈ Xw. Set z = y− x⊤β sog ∗(x, z) = y. e(x, z) = 1 ifx ∈ X1 and e(x, z) = κ ifx ∈ X0. Conditional on ˜w, w is
independent of ( y, z). In the setup, the GAI estimator leads to the same asymptotic variance as the case
where y is fully observed, i.e., ( pσ2 1 + (1−p )σ2 0)I. It is easy to see that bβP obtained under the score function
wi∇βℓ(xi,y i;β) is asymptotically normal with covariance given by
A Var
 bβP = pσ2 1 + (1−p)σ 2 0κ [p+ (1−p)κ] 2 I≺A Var  bβGAI = (pσ 2 1 + (1−p)σ 2 0)I,
which holds whenσ 1, κ↓0.

Lu et al.:Generative Augmented Inference
63
Appendix J: Supporting Results for Section 6
This appendix collects the proofs deferred from Section 6 and from Section C: the proof of the combined
known-density-ratio result (Theorem 4) and the proof of the doubly robust result stated in the main body
(Theorem 3).
J.1. Proof of Theorem 4
Theorem 4 combines two claims: the asymptotic normality of the weighted GAI estimator bβw and its
dominance over the weighted primary-only estimator bβP,w. We prove the normality claim first and then the
dominance claim.
Asymptotic normality of bβw.The proof follows exactly the structure of the proof of Theorem 1 in Section I.1:
we first establish the counterparts of Lemmas 1–3 for the weighted score (22), and then complete the argument
with the same Donsker/Taylor step. For each step we indicate explicitly whether the existing argument
applies—in which case we cite it and state the substitution—and we write out in full only the steps that are
genuinely new.
As in the proof of Theorem 1, we assume without loss of generality that the dataset is split into I and I c,
each of size n; the nuisance bg is obtained on I c and bβw is estimated on I. Here neither ρ nor r(X) is estimated,
so bg is the only nuisance trained on I c. We use the same shorthand Pn and Gn as in Section I.1, where
now the population expectation is taken under the source data-generating process (including the labeling
indicator w) and is written ES[ · ], and the same constant C such that ∥X∥,∥ X∥F ⩽C for allX ∈ ˘X ; by
Assumption 4(ii), the same bound applies under the target population. Mirroring the definition of τ (Ξ; e, g)
at the start of Section I.1, we define theβ-free part of the weighted score,
τw(Ξ;g) :=r(X)X ⊤

g(X,z)− w ρ  g(X,z)−y  =r(X)τ(Ξ;ρ,g),
so thatΨ w(Ξ;g;β) =r(X)X ⊤∇b(Xβ)−τ w(Ξ;g) for allβ∈ B.
The first lemma is the counterpart of Lemma 1.
Lemma 4(Score V alidity and Neyman Orthogonality under Covariate Shift).It holds that
ES[Ψw

g∗;β ∗ T  ] = 0andP nτw(bg)−P nτw(g∗) =o P (n−1/2).
Proof of Lemma 4.For the first claim, by the definition ofτ w,
ES[τw(g∗)] =E S

r(X)X ⊤

g∗(X,z)− w ρ  g∗(X,z)−y 
(a)
=E S

r(X)X ⊤

g∗(X,z)− E[w|X,z] ρ  g∗(X,z)−E[y|X,z] 
(b)
=E S

r(X)X ⊤E[y|X,z]  =E S  r(X)X ⊤y  (c) =E T  X⊤y  ,
where (a) follows from the law of iterated expectations and the independence of w and (X , y, z) under
Assumption 4(iii) (note that r(X) is a known function ofXand passes through the conditional expectation),
(b) follows from E[w| X, z] = ρ andg ∗(X, z) = E[y | X, z], and (c) is the change-of-measure identity (21).
Steps (a)–(b) are identical to steps (a)–(b) in the proof of Lemma 1, with e∗(X, z) ≡ρ and the bounded

Lu et al.:Generative Augmented Inference
64
known factor r(X) carried through; step (c) is new. Similarly, sinceX ⊤∇b  Xβ∗ T  is a function ofXalone,
(21) yields
ES

r(X)X ⊤∇b  Xβ∗ T  =E T  X⊤∇b  Xβ∗ T  .
Combining the two displays,
ES[Ψw

g∗;β ∗ T  ] =E T  X⊤  ∇b  Xβ∗ T  −y  = 0
by the target first-order condition (20). The two change-of-measure steps—which convert the weighted source
moments into target moments, so that the target first-order condition rather than the source one closes the
argument—are the only new ingredients relative to the proof of Lemma 1.
For the second claim, since the labeling probability is known and not estimated, we have be≡e∗ ≡ρ , and
therefore
√n(P nτw(bg)−P nτw(g∗)) = √nP n

r(X)

1− w ρ  X⊤∆g  | {z }
(Iw)
.
This is the exact analog of term (I) in the proof of Lemma 1, weighted by r(X); in the notation of that proof,
the analogs of terms (II) and (III)—both of which carry the factor ∆ e—areidentically zerohere because
be≡e∗ ≡ρ . This observation, although trivial, is what removes the need for any rate or sup-norm condition
on the nuisances: only (I w) must be controlled, which requires only theL 2-consistency of bg.
We control (Iw) by the same argument used for term (I) there. First, conditional on I c, it has zero mean:
exactly as in (34),E[w|X,z, I c] =ρby Assumption 4(iii) and the independence ofIandI c, so
E

r(X)

1− w ρ  X⊤∆g

 I c  =E  r(X)  1− E[w|X,z, I c] ρ  X⊤∆g

 I c  = 0.
Second, by the same conditional Markov/variance computation as in (35),
P

∥(Iw)∥⩾ϵ

 I c ⩽E
"r(X)  1− w ρ  X⊤∆g  2

 I c #  ϵ2.
The only change relative to the bound following (35) is the constant: since 0 ⩽r (X) ⩽M by Assumption 4(ii)
and|1−w/ρ|⩽1 + 1/ρ⩽2/ρforρ∈(0,1],
r(X)  1− w ρ  X⊤∆g  2 QS,2 ⩽ 4M 2 ρ2 C 2 ∥∆g∥2 QS,2 →0,
where the constant 4 M 2/ρ2 replaces 4 /κ2 in the proof of Lemma 1, and the convergence uses only the
hypothesis ∥∆g∥QS,2 = o(1) of Theorem 4 in place of Assumption 2. The conclusion that (I w) is oP (1) then
follows by the same uniform-integrability argument as in the proof of Lemma 1. This concludes the proof of
the lemma. ■
The next lemma is the counterpart of Lemma 2.
Lemma 5(Rates of Empirical Scores under Covariate Shift).It holds that
PnΨw  g∗; bβw ,inf β∈B PnΨw bg;β  =o P (1/√n).

Lu et al.:Generative Augmented Inference
65
Proof of Lemma 5.Mirroring ¯ℓin the proof of Lemma 2, define
¯ℓw(Ξ;g;β) :=r(X)b(Xβ)−τ w(Ξ;g) ⊤β,
written here through τw so that the gradient identity is immediate: ∇β ¯ℓw(Ξ;g; β) =Ψ w(Ξ;g; β) and
∇2 β ¯ℓw(Ξ;g; β) = r(X)X ⊤∇2b(Xβ)X ⪰ 0. The only new observation needed for convexity is that the known
weight satisfies r(X) ⩾ 0, so the weighting preserves the positive semidefiniteness of the Hessian; hence ¯ℓw is
convex inβ, and so isE S[¯ℓw(g∗;β)]. By Lemma 4,
∇βES[¯ℓw

g∗;β ∗ T  ] =E S[Ψw  g∗;β ∗ T  ] = 0.
The strict convexity of the population objective is the second genuinely new step: for any fixed β∈ B, since
X⊤∇2b(Xβ)Xis a function ofXalone, the change-of-measure identity (21) gives
∇2 βES[¯ℓw(g∗;β)] =E S  r(X)X ⊤∇2b(Xβ)X  =E T  X⊤∇2b(Xβ)X  ⪰inf
X∈ ˘X
λmin

∇2b(Xβ)  ·E T  X⊤X  ≻0,
where inf X∈ ˘X λmin

∇2b(Xβ)  > 0 by exactly the compactness/contradiction argument in the proof of Lemma 2,
which we cite rather than repeat, and ET[X⊤X] ≻ 0 by Assumption 4(iv). The positive-definiteness argu-
ment thus runs through thetargetsecond-moment matrix ET[X⊤X] rather than ES[X⊤X]. Consequently,
ES[¯ℓw(g∗;β)] is strictly convex andβ ∗ T is its unique minimizer.
The remainder of the proof is unchanged from the proof of Lemma 2. Since 0 ⩽r (X) ⩽M , the compactness
of ˘X and the continuity of b(·) imply, by the weak law of large numbers, Pn ¯ℓw(g∗; β) →P ES[¯ℓw(g∗; β)];
the bounded weight does not affect the moment requirements. By Theorem 2.7 of Newey and McFadden
(1994), applied exactly as in the proof of Lemma 2, there is a random sequence { ˇβn}∞ n=1 that solves
minβ∈B Pn ¯ℓw(g∗; β) and converges to β∗ T with probability one; in particular, PnΨw(g∗; ˇβn) =0. Noting that
Ψw(bg; β) − Ψw(g∗; β) = τw(g∗) −τ w(bg) does not depend on β, Lemma 4 yields the exact counterpart of (37):
√nPnΨw(bg; ˇβn) = √nPnΨw(g∗; ˇβn) +√n(P nτw(g∗)−P nτw(bg)) =o P (1).(41)
Hence inf β∈B
PnΨw(bg; β)  = oP (1/√n), which implies PnΨw bg; bβw  = oP (1/√n) by the definition of bβw.
Using the argument in (41) again,P nΨw

g∗; bβw  =o P (1/√n). This concludes the proof of the lemma.■
The final lemma is the counterpart of Lemma 3.
Lemma 6(Consistency under Covariate Shift). bβw →P β∗ T.
Proof of Lemma 6.The proof of Lemma 3 carries over with ¯ℓ,Ψ, and β∗ replaced by ¯ℓw,Ψ w, and β∗ T
throughout; we verify the two steps where the weighting enters and cite the rest. Fix arbitrary ϵ1 < ϵ2
such that B(β ∗ T, ϵ2)⊂ B. First, the uniform convergence step: by Pollard (1991), the convexity of ¯ℓw(g∗; ·)
established in the proof of Lemma 5 and the compactness of B(β ∗ T, ϵ2) imply thatP n ¯ℓw(g∗;β) converges to
ES[¯ℓw(g∗; β)] in probability uniformly on B(β ∗ T, ϵ2); the argument is unchanged because r(X) ⩽M keeps all
required moments finite. Second, the quadratic-growth lower bound (inequality (a) in the proof of Lemma 3):
for β∈ B(β ∗ T, ϵ2)\B (β∗ T, ϵ1) and the corresponding intermediate point ˜β∈ [β∗ T,β ], the change-of-measure
identity (21) gives
(β−β ∗ T)⊤ES
h
r(X)X ⊤∇2b  X ˜β  X i (β−β ∗ T) = (β−β ∗ T)⊤ET h X⊤∇2b  X ˜β  X i (β−β ∗ T)⩾c w∥β−β ∗ T∥2

Lu et al.:Generative Augmented Inference
66
with the new constant cw := inf

λmin

∇2b(Xβ)  :X ∈ ˘X,β∈ B(β ∗ T, ϵ2) 	 ·λ min  ET[X⊤X]  > 0: the first
factor is positive by the same compactness/contradiction argument given in the proof of Lemma 3, and
the second is positive by Assumption 4(iv); the lower-bound constant thus runs through ET[X⊤X]. All
remaining steps—the subgradient inequality, the gradient lower bound (38), its extension from the annulus to
B \B(β ∗ T, ϵ2) via the integral form of the intermediate value theorem (which only uses ∇2 β ¯ℓw ⪰ 0, valid here
since r(X) ⩾ 0), and the conclusion via Lemma 5—carry over verbatim, and we cite them rather than repeat.
This concludes the proof of the lemma.■
With these three lemmas, the completion of the proof is identical to the Donsker/Taylor step in Section I.1;
we indicate the substitutions. From this point on we suppressg ∗ and writeΨ w(·; β). First, the local Lipschitz
property: forβ 1,β 2 ∈B(β ∗ T, ϵ),
∥Ψw(Ξ;β 1)−Ψ w(Ξ;β 2)∥=r(X)
X⊤∇b(Xβ1)−X ⊤∇b(Xβ2)  ⩽M C1∥X∥∥β1 −β 2∥,
where the bound on the unweighted difference is exactly the local Lipschitz display in the proof of Theorem 1,
with C1 := supβ∈B(β∗ T,ϵ),X∈ ˘X ∥∇2b(Xβ)∥<∞ defined as there (with β∗ T in place of β∗); the Lipschitz constant
simply picks up the factor M . Since ES

M 2C 2 1 ∥X∥2 <∞ , by Example 19.7 and Theorem 19.5 in Van der
Vaart (2000), {Ψw(·;β) :β∈B(β ∗ T, ϵ)}forms a Donsker class. By Lemma 6, bβw →P β∗ T, so by Theorem 19.9
in Van der Vaart (2000),G nΨw( bβw)−G nΨw(β∗ T)→ P 0. Thus, exactly as in Section I.1,
√n  ES[Ψw( bβw)]−E S[Ψw(β∗ T)]  =−  GnΨw( bβw)−G nΨw(β∗ T)  + √nPnΨw( bβw)− √nPnΨw(β∗ T)
=− √nPnΨw(β∗ T) +oP (1),
where the last equality follows from Lemma 5. Applying the Taylor expansion to the left-hand side, the
Jacobian of the population map β7→E S[Ψw(β)] at β∗ T isJ T = ES  r(X)X ⊤∇2b  Xβ∗ T  X  , and we obtain the
counterpart of (27):
√n h JT  bβw −β ∗ T  +o P (1)  bβw −β ∗ T  i =− √nPnΨw(β∗ T) +oP (1) =O P (1).(42)
Here √nPnΨw(β∗ T) = OP (1) by the central limit theorem: it is a scaled i.i.d. sum with mean zero by
Lemma 4, and its covariance matrixΩ w = ES

Ψw(g∗; β∗ T)Ψw(g∗; β∗ T)⊤ is finite because r(X) ⩽M , ∥X∥⩽C ,
and ∥Cov(y | X, z)∥⩽˜σ2—the same moment conditions as in the main text (together with the square-
integrability ofyin Assumption 1(iv), which bounds the ζT-block ofΩ w via ES∥g∗(X, z)∥2 ⩽E S∥y∥2).
Moreover,J T = ET

X⊤∇2b  Xβ∗ T  X  is invertible by the argument in the proof of Lemma 5. Therefore, (42)
implies √n  bβw −β ∗ T  =O P (1), and applying (42) again,
√n  bβw −β ∗ T  =−J −1 T √nPnΨw(β∗ T) +oP (1)⇝N  0,J −1 T ΩwJ−1 T  =N  0,Σ w  .
It remains to verify the decomposition (24). By the definitions ofζ T andπin Section C.1,
Ψw

Ξ;g ∗;β ∗ T  =r(X)X ⊤

∇b

Xβ∗ T  −g ∗(X,z) + w ρ  g∗(X,z)−y  =r(X)  ζT + w ρ π  ,
so that
Ωw =E S

r(X)2 ζTζ ⊤ T  +E S

r(X)2 w ρ  ζTπ⊤ +πζ ⊤ T  +E S  r(X)2 w2 ρ2 ππ ⊤  .

Lu et al.:Generative Augmented Inference
67
For the cross terms, condition on (X , z): both r(X) and ζT are functions of (X , z), and since w⊥ (X, y, z)
with E[w/ρ] = 1 and E[π| X, z] =X ⊤ g∗(X, z) −E [y | X, z]  = 0, we have E[(w/ρ)π|X,z] = E[w/ρ] ·
E[π| X, z] = 0; hence both cross terms vanish. For the last term, w2 = w and the independence of w
give ES [r(X)2(w/ρ)2ππ ⊤] = E[w/ρ2] ·E S [r(X)2ππ ⊤] = 1 ρ ES [r(X)2ππ ⊤]. This proves (24), paralleling the
computation of (29), and completes the proof of the normality claim.
Dominance of bβw over bβP,w.The dominance argument mirrors the proof of Corollary 2 in Section I.2.1. To
start, as noted in Section C.2, the estimating equation (23) is equivalent to Pn i=1 wi r(Xi) ∇βℓ(Xi, yi; β) = 0,
and its population validity at β∗ T, i.e., ES  w r(X) ∇βℓ  X, y; β∗ T  = 0, was established in the display preceding
the statement of Theorem 4; we do not repeat it. Thus, under the preset assumptions, with probability
approaching one a solution bβP,w to this equation exists and √n  bβP,w −β ∗ T  ⇝N  0, ΣP,w : the proof follows
the same M-estimation argument as the normality argument above, with the bounded known weight w r(X) in
place of r(X) and no nuisance functions (so the argument only simplifies), exactly as the proof of Corollary 2
treats the unweighted primary-only estimator. We skip the proof and record the two components of the
sandwich covariance. For the Jacobian, by the independence ofwunder Assumption 4(iii),
ES

w r(X)X⊤∇2b  Xβ∗ T  X  =ρE S  r(X)X ⊤∇2b  Xβ∗ T  X  =ρJ T.
For the score variance, write, as in the proof of Corollary 2,
∇βℓ

X,y;β ∗ T  =ζ T(X,z) +π(X,y,z),
now with β∗ T in place of β∗ in ζT. Because E[g ∗(X,z)−y|X,z] = 0, the cross term between ζT and π
vanishes by the same iterated-expectations argument used for (28), and, using w2 = w together with the
independence ofw,
ES
h
w r(X)2 ∇βℓ  X,y;β ∗ T  ∇βℓ  X,y;β ∗ T ⊤ i =ρ  ES  r(X)2 ζTζ ⊤ T  +E S  r(X)2 ππ ⊤ .
The sandwich formula then gives
ΣP,w = (ρJT)−1 ρ  ES  r(X)2 ζTζ ⊤ T  +E S  r(X)2 ππ ⊤ (ρJT)−1 = 1 ρ J−1 T  ES  r(X)2 ζTζ ⊤ T  +E S  r(X)2 ππ ⊤ J−1 T ,
which is the expression forΣ P,w in Theorem 4 and parallels (28). On the GAI side, as shown in the normality
argument above,Ψ w

Ξ;g ∗;β ∗ T  =r(X)  ζT + w ρ π  andΩ w admits the decomposition (24); hence
Σw =J −1 T ES  r(X)2 ζTζ ⊤ T  J−1 T + 1 ρ J−1 T ES  r(X)2 ππ ⊤ J−1 T ,
paralleling (29). Subtracting the two displays yields (25), which is positive semidefinite because ρ⩽ 1 and
ES [r(X)2 ζTζ ⊤ T ]⪰ 0. Moreover, sinceJ T is invertible, the gap (25) is positive definite if and only if ρ <1 and
ES [r(X)2 ζTζ ⊤ T ]≻ 0; substituting ζT =X ⊤ ∇b  Xβ∗ T  −E [y | X, z]  gives exactly the dominance condition
displayed in Theorem 4. This completes the proof of the dominance claim, and with it the proof of Theorem 4.

Lu et al.:Generative Augmented Inference
68
J.2. Proof of Theorem 3
The proof follows exactly the structure of the proof of Theorem 1 in Section I.1 and of its known-ratio
counterpart in Section J.1: we first establish the counterparts of Lemmas 1–3 for the doubly robust score
(18), and then complete the argument with the same Donsker/Taylor step, now with a two-sample central
limit theorem. For each step we indicate explicitly whether the existing argument applies—in which case
we cite it and state the substitution—and we write out in full only the steps that are genuinely new. The
genuinely new ingredients are all consequences of the two-sample structure.
We first fix notation and the independence convention. We write PnT and PnS for the empirical means
over the target sample DT and the source sample DS, respectively, e.g., PnT f := 1 nT PnT j=1 f (Xj, zj), and
GnT f := √nT (PnT f−E Tf) for the target empirical process. As in Section I.1, we assume without loss of
generality (the split-sample device) that the nuisances are trained on auxiliary data, collectively denoted
I c, with the independence structure stated in Section J.2: bg is trained on an auxiliary source fold, hence
independent of all observations entering (18)—independence from the target sample is automatic, since bg
uses only source data and the two samples are independent; bris trained on data independent of the source
observations entering the bias-correction term, and is allowed to depend on the target covariates. The latter is
innocuous: brmultiplies only source rows in (18), and the only term of the decomposition below that involves
the target-sample average, term (I ′), involves thetrueratio r∗ rather than br, so a possible dependence of br
on DT never interacts with the target-sample average. Accordingly, in the conditional Markov arguments
below we condition, exactly as in the proof of Lemma 1, on the training data of the nuisances entering the
term at hand: on all of I c for the terms built from source evaluation observations, which are independent of
I c in its entirety, and on the auxiliary source fold alone for the target-sample part of term (I ′), which involves
only bg. For brevity we write all such conditionings as conditioning on I c. We use the same constant C with
∥X∥,∥ X∥F ⩽C for allX ∈ ˘X ; by Assumption 4(ii) the same bound applies under the target population. We
abbreviate ∆ g := bg−g ∗ and ∆r :=br−r∗.
Mirroring the definition of τ (Ξ; e, g) at the start of Section I.1, we collect the β-free part of the doubly
robust score:
τDR(g, r) :=PnT

X⊤g(X,z)  −P nS  r(X)X ⊤ g(X,z)−y  ,
so that
ΨDR(g, r;β) =P nT

X⊤∇b(Xβ)  −τ DR(g, r) for allβ∈ B.
Two structural facts drive the entire proof and we highlight them at the outset: (a) only the target-sample
term of (18) depends on β—the bias-correction term is a constant vector in β; and (b) the two samples
are independent. Fact (a) means that the convexity machinery of Lemmas 2 and 3 operates entirely on the
target sample, with the bias correction entering only as a β-free random shift; fact (b) is what permits the
two-sample mean cancellation in term (I ′) below and the two-sample central limit theorem at the end.
The first lemma is the counterpart of Lemma 1.
Lemma 7(Score V alidity and Neyman Orthogonality for the Doubly Robust Score). It holds
that
ET [ζT] = 0,E S [r∗(X)π] = 0,andτ DR(bg,br)−τDR(g∗, r∗) =o P  n −1/2 S  .

Lu et al.:Generative Augmented Inference
69
Throughout the proof we use the prediction residual ζT(X, z) =X ⊤ ∇b  Xβ∗ T  − g∗(X, z)  and the label
residual π(X, y, z) =X ⊤ g∗(X, z) − y  , both defined in Section C.1. The first two claims state that the
population means of the two sample-terms ofΨ DR

g∗, r∗; β∗ T  —namely ET  X⊤ ∇b  Xβ∗ T  − g∗ = ET[ζT]
and ES

r∗(X)π  —areeachzero, not merely that their sum is zero. This is a genuinely new requirement
relative to Lemma 1, where validity of the score only requires the single population mean E[Ψ(e∗, g∗; β∗)] to
vanish: here the two terms are averages over two different samples with different sizes, so the two-sample
central limit theorem at the end of the proof requires each sample-term to be centered separately.
Proof of Lemma 7.We begin with the two validity claims; both are new but short. For the second claim,
ES [r∗(X)π] (a) =E S [r∗(X)E[π|X,z]] (b) =E T [π] (c) = 0;
where (a) follows from the law of iterated expectations, conditioning on (X , z) (note that r∗(X) is a function
ofXand passes through the conditional expectation), (b) is the change-of-measure identity (21), and (c)
uses E[π| X, z] =X ⊤ g∗(X, z) −E [y | X, z]  =0, sinceg ∗(X, z) = E[y | X, z]. The first expectation vanishes
already because E[π| X, z] =0, and we record the identity ET[π] = 0 separately because we use it next. For
the first claim,
ET [ζT]
(d)
=E T

X⊤  ∇b  Xβ∗ T  −y  −E T [π] (e) = 0−0 = 0,
where (d) adds and subtracts ET[y] to write ζT =X ⊤ ∇b(Xβ∗ T) − y  −π , and (e) follows because the first
expectation is zero by the target first-order condition (20) and the second is zero by claim two just established.
Note that no change of measure is needed for the first claim: the prediction component of (18) is evaluated
directly under the target population, which is precisely the point of the two-sample construction.
For the third claim, decompose br(bg− y) −r ∗(g∗ − y) = r∗∆g + ∆r(g∗ − y) + ∆r∆g inside the bias-correction
term to obtain
√nS (τDR(bg,br)−τDR(g∗, r∗)) = (I ′)−(II ′)−(III ′),(43)
where
(I′) := √nS PnT  X⊤∆g  − √nS PnS  r∗(X)X ⊤∆g  ,
(II′) := √nS PnS  ∆r(X)X ⊤ g∗(X,z)−y  ,
(III′) := √nS PnS  ∆r(X)X ⊤∆g  .
This decomposition is the two-sample counterpart of the decomposition (I)–(III) in the proof of Lemma 1:
(II′) and (III ′) mirror (II) and (III) with ∆ r in place of be−e∗, while (I ′) replaces the single-sample term (I)
by adifference of averages over the two samples, which is the genuinely new structure. We treat each term
separately, conditioning onI c throughout.
Term (I′).Unlike term (I) in the proof of Lemma 1, neither average in (I ′) has zero conditional mean by
itself. Instead, the two conditional means cancel exactly across the two samples: conditional onI c,
E

r∗(X)X ⊤∆g

 I c  (a) =E S  r∗(X)X ⊤∆g

 I c (b) =E T  X⊤∆g

 I c ,

Lu et al.:Generative Augmented Inference
70
where (a) records that the source observations entering the bias-correction term have law QS given I c, and
(b) is the change-of-measure identity (21); the right-hand side is exactly the conditional mean of PnT [X⊤∆g]
(here we use that bgis independent of both evaluation samples). Therefore
(I′) = √nS (PnT −E T)  X⊤∆g  − √nS (PnS −E S)  r∗(X)X ⊤∆g  ,
a difference of two mean-deviation terms that are independent conditional on the auxiliary source fold on
which bg is trained (fact (b)). Each is controlled by the conditional Markov/variance argument of (35), with
new constants. For the target part, the summands are i.i.d. conditional on I c (by the convention above, the
conditioning here is on the auxiliary source fold that trains bg, of which the target sample is independent), so
E
√nS (PnT −E T)  X⊤∆g 2

 I c  (c) ⩽ nS nT ET hX⊤∆g 2

 I c i (d) ⩽ nS nT C 2 ∥∆g∥2 QT,2 (e) ⩽ nS nT C 2M∥∆ g∥2 QS,2 →0,
where (c) bounds the variance of the mean-deviation term by 1 /nT times the summand second moment (the
summands being i.i.d. conditional on I c), (d) uses ∥X∥⩽C , and (e) is the QT-norm conversion derived after
Assumption 5; the convergence holds because nS/nT →γ <∞ is bounded and ∥∆g∥QS,2 → 0 by Assumption 5.
The requirement nS/nT →γ <∞ enters the proof exactly here (and again in the Donsker and CLT steps
below). For the source part,
E
√nS (PnS −E S)  r∗(X)X ⊤∆g 2

 I c  (f) ⩽E S  r∗(X)2 X⊤∆g 2

 I c  (g) ⩽M 2C 2 ∥∆g∥2 QS,2 →0,
where (f) bounds the variance of the mean-deviation term by the summand second moment, and (g) uses
r∗(X) ⩽M and ∥X∥⩽C . By the conditional Markov inequality applied as in (35) to each of the two parts,
followed by the same uniform-integrability argument as in the proof of Lemma 1 to remove the conditioning,
(I′) is oP (1). The two-sample mean cancellation and the QT-norm conversion are the new ingredients; the
Markov/variance mechanics are unchanged.
Term (II ′).This term mirrors term (II) in the proof of Lemma 1 with ∆ r in place of be−e∗, and is in
fact simpler: because brenters multiplicatively rather than through an estimated denominator, no analog of
the factor 1 /κ2 appears and no sup-norm condition on bris invoked. Conditional on I c, (II ′) has zero mean:
by the argument of (34), E

g∗(X, z) − y | X, z, Ic = E  g∗(X, z) − y | X, z  = 0, and ∆r(X) is a function of
(X, Ic) only (recall that bris trained on data independent of the source evaluation observations; its possible
dependence on the target covariates is part of I c and is irrelevant here, since (II ′) involves only source
observations). For the conditional variance, by the same computation as in the bound for (II) in the proof of
Lemma 1,
E
h
∥(II′)∥2

 I c i (a) ⩽E S  ∆r(X)2 X⊤ g∗(X,z)−y 2

 I c  (b) ⩽˜σ2C 2 ∥∆r∥2 QS,2 →0,
where (a) bounds the variance of the zero-mean i.i.d. average by the summand second moment, and (b)
uses Cov(y | X, z, Ic) = Cov(y | X, z) with ∥Cov(y | X, z)∥⩽˜σ2 and ∥X∥F ⩽C ; the convergence holds by
Assumption 5. The conditional Markov inequality and the uniform-integrability argument then give (II ′)
=o P (1), exactly as for (II).

Lu et al.:Generative Augmented Inference
71
Term (III′).This term mirrors term (III) in the proof of Lemma 1, with the product ∆ r∆g in place of
(be−e∗)(bg− g∗) and no constant from an estimated denominator (the factor 2 /κ2 obtained there is absent
becausebrenters multiplicatively). Conditional onI c,
P

∥(III′)∥⩾ϵ

 I c (a) ⩽ √nS
ϵ ES

|∆r(X)|
X⊤∆g 

 I c  (b) ⩽ C√nS ϵ ∥∆r∥QS,2 ∥∆g∥QS,2 (c) ⩽ C ϵ α(nS)2 n 1/2−rg −rr S
which converges to zero, where (a) is the Markov inequality applied to the first moment, (b) uses ∥X∥⩽C
together with the Cauchy–Schwarz inequality, and (c) uses Assumption 5 and rg + rr ⩾ 1/2; this is exactly
the role played by the product-rate condition r1 + r2 ⩾ 1/2 for term (III) in the proof of Lemma 1. Hence
(III′) =o P (1), and combining the three terms in (43) concludes the proof of the lemma.■
The next lemma is the counterpart of Lemma 2.
Lemma 8(Rates of Empirical Scores for the Doubly Robust Estimator).It holds that
ΨDR  g∗, r∗; bβDR ,inf β∈B ΨDR bg,br;β  =o P  1/√nS  .
Proof of Lemma 8.Mirroring ¯ℓin the proof of Lemma 2, define, for nuisances (g, r),
¯ℓDR(g, r;β) :=P nT

b(Xβ)−g(X,z) ⊤Xβ  +ξ nS(g, r)⊤β,ξ nS (g, r) :=PnS  r(X)X ⊤ g(X,z)−y  ,
so that ∇β ¯ℓDR(g, r; β) =Ψ DR(g, r; β). The correction term ξnS(g, r) is aconstant vector in β (fact (a)), so it
contributes a linear term to the objective and drops out of the Hessian:
∇2 β ¯ℓDR(g, r;β) =P nT  X⊤∇2b(Xβ)X  ⪰0,
so ¯ℓDR is convex in β regardless of the nuisances; this one-line observation is the only new step needed for
convexity. The population (true-nuisance) objective is
L(β) :=E T

b(Xβ)−g ∗(X,z) ⊤Xβ  ,
with no linear correction, because the population mean of ξnS(g∗, r∗) is ES  r∗(X)π  = 0 by Lemma 7. By
Lemma 7 again,∇L

β∗ T  =E T  ζT  = 0, and for any fixedβ∈ B,
∇2L(β) =E T  X⊤∇2b(Xβ)X  (a) ⪰inf
X∈ ˘X
λmin

∇2b(Xβ)  ·E T  X⊤X  (b) ≻0,
where (a) bounds ∇2b(Xβ) below by its smallest eigenvalue over ˘X , and (b) holds because the positivity of
the infimum is the compactness/contradiction argument in the proof of Lemma 2, which we cite rather than
repeat, and ET[X⊤X] ≻ 0 by Assumption 4(iv); this is the same substitution—the target second-moment
matrix in place of E[X⊤X]—already used in the proof of Lemma 5. Hence L is strictly convex and β∗ T is its
unique minimizer.
We next verify that the empirical objective at the true nuisances converges pointwise to L, which is
where theβ-free correction requires a (short) new argument. The target-sample partP nT

b(Xβ)−g ∗⊤Xβ 
converges in probability to ET

b(Xβ) − g∗⊤Xβ  for each β by the weak law of large numbers, exactly
as in the proof of Lemma 2, with the required moments finite under QT by the boundedness ofXand
ET∥g∗∥2
(a)
⩽E T∥y∥2 (b) =E S  r∗(X)∥y∥2 (c) ⩽ME S∥y∥2 <∞ , where (a) is the conditional Jensen inequality

Lu et al.:Generative Augmented Inference
72
applied tog ∗(X, z) = E[y | X, z], (b) is the change-of-measure identity (21), and (c) uses r∗(X) ⩽M (the
square-integrability ofyholding by Assumption 1(iv)). For the correction term at the true nuisances,
ξnS(g∗, r∗) is an i.i.d. average with mean zero (Lemma 7) and bounded summand variance,
ES
h
∥r∗(X)π∥ 2
i
=E S
h
r∗(X)2 ∥π∥2
i (a)
⩽M 2 ˜σ2C 2 <∞,
where (a) uses r∗(X) ⩽M , ∥Cov(y | X, z)∥⩽˜σ2, and ∥X∥⩽C , so ξnS (g∗, r∗) = OP  n −1/2 S  = oP (1); conse-
quently the linear term ξnS (g∗, r∗)⊤β vanishes in probability for each fixed β∈ B, and ¯ℓDR(g∗, r∗; β) →P L(β)
for each β. (At the estimated nuisances, Lemma 7 adds only an oP

n
−1/2
S

perturbation to τDR, so the
corresponding statements hold there as well; we only need the true-nuisance version in what follows.) By
Theorem 2.7 of Newey and McFadden (1994), applied exactly as in the proof of Lemma 2 to the convex
objective ¯ℓDR(g∗, r∗; ·) with unique population minimizer β∗ T, there is a random sequence { ˇβn} (the subscript
n indexing the joint asymptotic regime in which nS, nT → ∞) that solves minβ∈B ¯ℓDR(g∗, r∗; β) and converges
toβ ∗ T with probability one; in particular,Ψ DR(g∗, r∗; ˇβn) =0.
The transformation between the ( bg,br)-score and the (g ∗, r∗)-score is identical in logic to (37) and (41):
sinceΨ DR(bg,br;β)−Ψ DR(g∗, r∗;β) =τ DR(g∗, r∗)−τ DR(bg,br) does not depend onβ, Lemma 7 yields
√nS ΨDR(bg,br;ˇβn) = √nS ΨDR(g∗, r∗; ˇβn) +√nS (τDR(g∗, r∗)−τ DR(bg,br)) =oP (1).(44)
Hence inf β∈B
ΨDR(bg,br; β)  = oP  1/√nS  , which impliesΨ DR bg,br; bβDR  = oP  1/√nS  by the definition of
bβDR. Using the argument in (44) again,Ψ DR

g∗, r∗; bβDR  = oP  1/√nS  . This concludes the proof of the
lemma. ■
The final lemma is the counterpart of Lemma 3.
Lemma 9(Consistency of the Doubly Robust Estimator). bβDR →P β∗ T.
Proof of Lemma 9.The proof of Lemma 3 carries over with ¯ℓ,Ψ, Pn, and β∗ replaced by ¯ℓDR(g∗, r∗; ·),
ΨDR(g∗, r∗; ·), PnT , and β∗ T; we verify the three places where the two-sample structure enters and cite the rest.
Fix arbitrary ϵ1 < ϵ2 such that B(β ∗ T, ϵ2)⊂ B. First, the uniform convergence step: by Pollard (1991), the
convexity of the target-sample objective PnT

b(Xβ) − g∗(X, z)⊤Xβ  (established in the proof of Lemma 8)
and the compactness of B(β ∗ T, ϵ2) imply that it converges in probability, uniformly on B(β ∗ T, ϵ2), to L(β) =
ET

b(Xβ) − g∗(X, z)⊤Xβ  , exactly as in the proof of Lemma 3, now under QT and with the moment bound
ong ∗ from the proof of Lemma 8. The full empirical objective ¯ℓDR(g∗, r∗; β) differs from this target-sample
objective by the β-free linear term ξnS(g∗, r∗)⊤β, which is bounded in norm by ∥ξnS(g∗, r∗)∥  ∥β∗ T∥ + ϵ2  =
oP (1) uniformly over the ball since ξnS (g∗, r∗) = OP  n −1/2 S  ; hence ¯ℓDR(g∗, r∗; ·) also converges to L uniformly.
This β-free perturbation is the only new ingredient in the uniform-convergence step. Second, the quadratic-
growth lower bound (inequality (a) in the proof of Lemma 3): for β in the annulus and the corresponding
intermediate point ˜β,
(β−β ∗ T)⊤ ET
h
X⊤∇2b  X ˜β  X i (β−β ∗ T)⩾c DR ∥β−β ∗ T∥2 ,
with cDR := inf

λmin

∇2b(Xβ)  :X ∈ ˘X,β∈ B(β ∗ T, ϵ2) 	 ·λ min  ET[X⊤X]  > 0 by the compact-
ness/contradiction argument cited in the proof of Lemma 3 and Assumption 4(iv); as in the proof of Lemma 6,

Lu et al.:Generative Augmented Inference
73
the constant runs through the target second-moment matrix ET[X⊤X]. Third, the extension from the annulus
to B \B(β ∗ T, ϵ2) via the integral form of the intermediate value theorem uses only the positive semidefiniteness
of the empirical Hessian, which here is PnT

X⊤∇2b(Xβ)X  ⪰ 0—unaffected by the linear correction term (fact
(a)). All remaining steps—the subgradient inequality, the gradient lower bound(38), and the conclusion—carry
over verbatim with the stated substitutions, the conclusion now invoking
ΨDR  g∗, r∗; bβDR  = oP  1/√nS 
from Lemma 8. This concludes the proof of the lemma.■
With these three lemmas, the completion of the proof follows the Donsker/Taylor step in Section I.1; we
indicate the substitutions and write out in full the two-sample scaling and the two-sample central limit
theorem, which are new. Writef β(X) :=X ⊤∇b(Xβ), the only β-dependent part of the score (fact (a)). The
local Lipschitz bound in the proof of Theorem 1 applies verbatim: for β1,β 2 ∈B (β∗ T, ϵ), ∥fβ1 (X) − fβ2 (X)∥⩽
C1∥X∥∥β1 −β 2∥ with C1 := supβ∈B(β∗ T,ϵ),X∈ ˘X ∥∇2b(Xβ)∥<∞ ; unlike the weighted score of Section J.1, no
factor M arises, because the target-sample term of (18) carries no weight. Since ET

C 2 1 ∥X∥2 <∞ by the
boundedness ofXunder the target population, Example 19.7 and Theorem 19.5 in Van der Vaart (2000)
imply that {fβ :β∈B(β ∗ T, ϵ)}is a Donsker class under QT. By Lemma 9, bβDR →P β∗ T, so Theorem 19.9
in Van der Vaart (2000) gives GnT f bβDR −G nT fβ∗ T →P 0. The new two-sample wrinkle is the scaling: the
asymptotic equicontinuity statement is in the √nT scale, while the theorem is normalized by √nS, so we
multiply by
p
nS/nT, which converges to √γ <∞; hence
√nS (PnT −E T)  f bβDR −f β∗ T  = r nS nT  GnT f bβDR −G nT fβ∗ T  =o P (1).
Define the population score map ¯Ψ(β) := ET

X⊤ ∇b(Xβ) − g∗(X, z)  = ∇L(β); note that differences of
ΨDR(g∗, r∗; ·) across two values of β equal PnT -differences off β, since the β-free parts cancel. Thus, exactly
as in Section I.1,
√nS  ¯Ψ  bβDR  − ¯Ψ  β∗ T  =− r nS nT  GnT f bβDR −G nT fβ∗ T  + √nS ΨDR  g∗, r∗; bβDR  − √nS ΨDR  g∗, r∗;β ∗ T 
=− √nS ΨDR  g∗, r∗;β ∗ T  +o P (1),
where the last equality follows from Lemma 8. Applying the Taylor expansion to the left-hand side, by
continuous mapping, the Jacobian of ¯Ψ at β∗ T isJ T = ET  X⊤∇2b  Xβ∗ T  X  , and we obtain the counterpart
of (27):
√nS h JT  bβDR −β ∗ T  +o P (1)  bβDR −β ∗ T  i =− √nS ΨDR  g∗, r∗;β ∗ T  +o P (1) =O P (1).(45)
HereJ T = ∇2L  β∗ T  is invertible by the argument in the proof of Lemma 8, and the OP (1) claim follows
from the two-sample central limit theorem that we now establish; it is the final new step.
By the definitions ofζ T andπand fact (b),
√nS ΨDR  g∗, r∗;β ∗ T  = r nS nT · √nT PnT [ζT] + √nS PnS [r∗(X)π],(46)
a sum of twoindependentterms, each an i.i.d. average centered at zero by Lemma 7—this is where the
separate centering of the two components is indispensable. For the source term, the summands have finite
covariance matrix
ES

r∗(X)2 ππ ⊤ ,

Lu et al.:Generative Augmented Inference
74
which is the ρ = 1 specialization of the last term of (24) and is finite since r∗(X) ⩽M , ∥X∥⩽C , and
∥Cov(y|X,z)∥⩽˜σ 2; hence by the central limit theorem,
√nS PnS [r∗(X)π]⇝N  0,E S  r∗(X)2 ππ ⊤ .
For the target term, ET

ζTζ ⊤ T  is finite—∥X∥⩽C under the target population and ET∥g∗∥2 ⩽ME S∥y∥2 <∞
as noted in the proof of Lemma 8—so √nT PnT [ζT]⇝N  0,E T  ζTζ ⊤ T  by the central limit theorem under
QT. If γ >0, then
p
nS/nT → √γ and, by Slutsky’s theorem, the first term of (46) converges weakly to
N

0, γET

ζTζ ⊤ T  . If γ = 0, the first term is p nS/nT ·O P (1) →P 0, i.e., it degenerates to zero in probability;
this case is still covered, the limit below holding with the first term ofΩ γ equal to zero. Because the two
terms of (46) are independent for every ( nS, nT), they converge jointly to independent limits, and their sum
satisfies
√nS ΨDR  g∗, r∗;β ∗ T  ⇝N  0, γET  ζTζ ⊤ T  +E S  r∗(X)2 ππ ⊤ =N  0,Ω γ  ,
for allγ∈[0,∞); in particular it isO P (1), as claimed in (45).
SinceJ T is invertible, (45) implies √nS  bβDR −β ∗ T  =O P (1), and applying (45) again,
√nS  bβDR −β ∗ T  =−J −1 T √nS ΨDR  g∗, r∗;β ∗ T  +o P (1)⇝N  0,J −1 T ΩγJ−1 T  =N  0,Σ DR  ,
as desired. This completes the proof of Theorem 3.
