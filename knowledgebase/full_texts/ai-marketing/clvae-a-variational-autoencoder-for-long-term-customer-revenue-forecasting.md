---
title: 'CLVAE: A Variational Autoencoder for Long-Term Customer Revenue Forecasting'
url: https://arxiv.org/abs/2604.22636
category: ai-marketing
subcategory: measurement
date: 2026-04
venue: ''
authors:
- Jeffrey Näf
- Riana Valera Mbelson
- Markus Meierer
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.22636
pages: 35
chars: 77518
fetched_at: '2026-11-08T13:26:58+00:00'
kb_version: 1
---

# CLVAE: A Variational Autoencoder for Long-Term Customer Revenue Forecasting

CL V AE: A Variational Autoencoder for Long-Term
Customer Revenue Forecasting
Jeffrey N¨ af1, Riana Valera Mbelson, Markus Meierer 2
1Research Institute for Statistics and Information Science, University of Geneva
2Institute of Management, University of Geneva
Abstract
Predicting customers’ long-term revenue from sparse and irregular transaction data
is central to marketing resource allocation in non-contractual settings, yet existing
approaches face a trade-off. Traditional probabilistic customer base models deliver
robust long-horizon forecasts by imposing strong structural assumptions, while flexible
machine-learning models often require substantial training data and careful tuning.
We propose a variational-autoencoder-based model that preserves the process-based
likelihood of established attrition–transaction–spend models conditional on customer
heterogeneity, but replaces the restrictive parametric mixing distribution with a flexible
latent representation learned by encoder-decoder networks. The resulting approach (i)
provides a single model for customer attrition, transactions and spending, (ii) remains
reliable when contextual covariates are unavailable, and (iii) flexibly incorporates rich
covariates and nonlinear effects when they are available. This design balances structural
stability with the flexibility needed to capture complex purchase dynamics. Across
multiple real-world datasets and prediction horizons, the proposed model improves
upon the latest benchmarks. Businesses benefit directly, as a better assessment of
customers’ future revenues improves the efficiency of campaign targeting. For research,
this work provides guidance on how to embed domain-specific models into the variational
autoencoder framework, enabling flexible representation learning while retaining an
econometrically meaningful process structure.
Keywords:Variational autoencoder, neural network, customer base analysis, customer
heterogeneity
1
arXiv:2604.22636v1  [stat.ML]  24 Apr 2026

1 Introduction
Firms in non-contractual settings must routinely infer customers’ long-term future revenue
from transaction data that record only purchase timing and monetary value. A central
challenge is heterogeneity. Customers differ substantially in their underlying purchase
propensities, spending levels, and attrition propensities, yet these differences are only indirectly
reflected in sparse transaction data. Because attrition itself is not directly observed, a period
without purchases is inherently ambiguous as a customer may be temporarily inactive or
may have permanently discontinued purchasing. The structure of the observed transaction
records makes learning these differences difficult. In addition, purchase behavior is highly
heterogeneous, with up to 50% of customers purchasing only once while others transact
repeatedly. Even among repeat buyers, transaction records are sparse and irregular. Purchases
occur at uneven intervals and are separated by long stretches with no transactions (see Figure
1). Finally, observation windows vary with customer tenure and are often short relative to
the forecasting horizon. As a result, the observed records contain limited information to infer
customer-specific propensities and predict long-run revenue.
A popular approach to address these challenges is to use probabilistic modeling techniques.
By disentangling customers’ attrition, transaction, and spending processes, these probabilistic
models can infer individual customers’ future revenue for arbitrary forecasting horizons. Due
to their proven robustness and wide accessibility through open-source software (Dziurzynski
et al. 2021), such models are widely used in industry. Common examples are the Pareto/NBD
model (Schmittlein et al. 1987) for capturing attrition and transactions and the Gamma-
Gamma (GG) model (Colombo and Jiang 1999, Fader et al. 2005b) for estimating each
customer’s average spend per transaction. If available, the latter may also be used to model
profits (Glady et al. 2009). Probabilistic models that combine all three processes have been
proposed by several authors, but their computational complexity and limited improvements
in predictive performance have prevented their adoption by practitioners. Although progress
has been made to increase the flexibility of these models (e.g., Abe 2009, Glady et al. 2015,
Platzer and Reutterer 2016, Bachmann et al. 2021), these extensions still rely on parametric
assumptions about customer heterogeneity that can be too restrictive.
When considering modern machine learning models, the sparsity and irregularity of the
time series for each customer make standard approaches hard to apply. One exception
is autoregressive deep learning techniques that may help to address the limited flexibility
in traditional models. They can model transaction sequences and have shown promise in
predicting customers’ transaction patterns (Valendin et al. 2022). Yet, they often require
substantial data to learn structure nonparametrically and represent customer heterogeneity
2

Note: The dashed line indicates the end of a 104-week estimation period. Customers start purchasing at
different times during this period. Transactions after the dashed line are part of the prediction period. Not
shown is the spend associated with each transaction.
Figure 1: Real-world transaction data for 20 customers (Retailer A, see Section 4).
3

only implicitly, which may be unstable with short and sparse transaction histories. Moreover,
they do not directly model spending. This limits their usefulness when the managerial
objective is to predict long-term customer revenue. Therefore, the question arises of whether
it is possible to retain the structural strengths of traditional probabilistic models while
relaxing their restrictive assumptions about latent heterogeneity by leveraging deep learning
techniques. Leveraging the ”best of both worlds” may facilitate a more robust, scalable and
accurate prediction of individual customers’ long-term revenue.
To this end, we focus on variational autoencoder techniques that build on an encoder-
decoder neural network architecture. Generally speaking, a variational autoencoder (V AE) is
a generative latent-variable model trained using variational inference. It provides a flexible
way to model high-dimensional data X via low-dimensional latent variables Z that capture
heterogeneity and structure relevant for prediction, compression and simulation. V AEs
are increasingly applied in management, marketing and information systems research (e.g.,
Sisodia et al. 2025, Yang et al. 2023, Burnap et al. 2023, Dew et al. 2022). In this paper,
we show that a V AE presents a natural nonparametric extension of traditional probabilistic
customer base models with latent heterogeneity, such as the Pareto/NBD model. Since these
models essentially compress the observed recency and frequency data (i.e., x, tx, T) to latent
variables (λ, µin the case of the Pareto/NBD model), the mapping fits naturally into an
encoder-decoder perspective. This is the driving idea behind our model development. We
consider not only attrition and transaction timing, but also the spending process, inspired
by the GG model. Specifically, we keep the likelihood of the combined Pareto/NBD and
GG model conditional on the latent heterogeneity variables, but replace the fixed parametric
mixing distribution with a latent representation learned by encoder-decoder networks and
estimated via amortized variational inference.
Central to the resulting Customer Lifetime Value Variational Autoencoder – for short,
CL V AE – is a likelihood-based V AE that preserves the canonical attrition–transaction–spend
process likelihood conditional on customer heterogeneity, while learning a flexible nonparamet-
ric mixing distribution over customer-level propensities. Our proposed approach makes five
contributions relative to prior work: First, it provides a single model to capture all three key
processes and their dependencies, which facilitates the direct estimation of customer revenue.
Second, it relaxes restrictive parametric heterogeneity assumptions by learning a flexible
heterogeneity distribution, enabling latent propensities across attrition, transaction timing,
and spending. Third, it uses a fast estimation routine based on amortized inference (Kingma
and Welling 2019), which supports both moderately sized datasets and large-scale customer
bases. Fourth, it is data-parsimonious, requiring only summary statistics of transaction
records, yet it can incorporate richer inputs such as full transaction histories and contextual
4

covariates when available. Fifth, it delivers robust and accurate results without extensive
dataset-specific tuning. Collectively, these contributions address the main practical trade-off
in long-term revenue forecasting by balancing structural stability under sparse transaction
histories with flexibility in modeling heterogeneity, while remaining scalable for operational
use.
We build on multiple real-world datasets to evaluate our approach. The results show that
it is scalable, robust, and accurate. In out-of-sample testing across three non-contractual
business settings and four prediction horizons, we find that the novel model improves upon the
latest benchmarks. To illustrate its managerial relevance and ability to account for additional
contextual information, we also show how CL V AE can serve as a practical alternative to the
common industry workflow of fitting separate models by acquisition cohort to accommodate
observed heterogeneity.
The remainder of the paper is structured as follows. Section 2 reviews related research.
Section 3 introduces the model as well as the estimation and prediction routine. Additionally,
it details extensions that broaden applicability across business settings. Section 4 reports on
our empirical applications, providing an overview of the datasets, benchmarks, and empirical
results. In Section 5, we conclude with implications for marketing research and practice. To
facilitate replication and further research, we have released a Python implementation of our
novel model along with code to reproduce our results in a public repository (link removed to
ensure anonymous review).
2 Literature
Customer base analysis is key to many customer-centric initiatives. These initiatives rely on
effective customer targeting, which often builds on long-term projections of customer behavior
(e.g., Lemmens and Gupta 2020, Simester et al. 2006). While many statistical techniques are
applicable for short-term forecasting, data limitations often restrict their direct application
for long-term revenue prediction. This is particularly true when transaction records are sparse
and the prediction horizon exceeds the available observation window.
Our work sits at the intersection of (i) probabilistic customer base models for long-term
revenue forecasting in non-contractual settings and (ii) modern machine-learning methods
for transaction data. The core tension is that long-horizon prediction benefits from strong
structural discipline when transaction histories are limited and unevenly observed. At
the same time, this discipline typically requires restrictive assumptions about unobserved
heterogeneity. We review these streams and highlight the gap that the proposed model
addresses.
5

2.1 Customer base models for long-term forecasting
For long-term prediction of customer revenue, probabilistic customer base models are a
popular choice. These models generate long-horizon forecasts by distinguishing three processes:
customer attrition, transactions, and spending. Their parameter and data parsimony support
robustness and broad applicability. Moreover, time-invariant and time-varying covariates can
be incorporated, and the resulting coefficients admit standard economic interpretations (e.g.,
elasticities). Canonical approaches combine a latent attrition model, such as the Pareto/NBD
model (e.g., Schmittlein et al. 1987, Fader et al. 2005a, Abe 2009, Fader et al. 2010, Bemmaor
and Glady 2012, Braun et al. 2015) with a spending model such as the GG model (e.g.,
Colombo and Jiang 1999, Fader et al. 2005b, Schmittlein and Peterson 1994). These models
remain widely used because they provide stable forecasts from limited transaction histories.
At the same time, that stability is achieved by committing to specific parametric assumptions
about customer heterogeneity and the links between the three processes. By shrinking
individual parameters toward an assumed prior distribution, these models remain stable
in sparse histories. However, misspecification can turn that shrinkage into bias and harm
long-horizon forecasts.
Prior work has therefore introduced joint models that link attrition, transactions, and
spending and allow dependence across processes (e.g., Borle et al. 2008, Schweidel and Knox
2013, Glady et al. 2015), as well as extensions that increase flexibility in the underlying
structure and with regards to contextual factors (e.g., Platzer and Reutterer 2016, Bachmann
et al. 2021). While these models provide a richer behavioral process specification, gains in
predictive performance have often been modest, whereas computational burden and sensitivity
to estimation choices can increase substantially. As a result, stability and scalability may
be insufficient for routine, large-scale operational use, which may help explain their limited
practitioner adoption.
Modern machine-learning methods address some limitations by offering flexible function
approximation. These end-to-end-trainable models automatically learn task-relevant features
from high-dimensional data, capture complex nonlinearities and interactions, scale to large
datasets, and deliver high predictive accuracy (e.g., Gabel and Timoshenko 2022). In
case of customer base analysis, research has shown that traditional probabilistic latent
attrition models can be replaced by autoregressive sequence models to predict transactional
incidence patterns. Long Short-Term Memory (LSTM) models have been a popular choice
for this (Valendin et al. 2022). In sparse settings, this flexibility can overfit without careful
regularization. Moreover, these methods often represent heterogeneity only implicitly through
high-capacity architectures and focus on modeling transaction incidence, with spending
handled in a separate model.
6

Taken together, the literature suggests a persistent gap. Practitioners need models
that preserve the long-horizon stability of likelihood-based customer base approaches while
relaxing restrictive parametric assumptions, without sacrificing scalability and robustness on
sparse and irregular transaction data. Combining deep learning techniques with traditional
probabilistic modeling can provide a solution to this challenge. Work in other disciplines
has shown the potential of V AE approaches to facilitate such synergies (e.g., Krishnan et al.
2017).
2.2 Variational autoencoders in management, marketing and in-
formation systems
V AEs are likelihood-based latent-variable models estimated with amortized variational infer-
ence (Kingma and Welling 2019). Amortized variational inference uses a single recognition
model qϕ(Z|X ) with parameters ϕ that maps each observation X to the parameters of an
approximate posterior over latent factors Z. This replaces solving a separate variational
problem for every observation and enables fast inference for a new X via a single forward
pass. The generative model pθ(X|Z ) with parameters θ and the distribution p(Z) define
the data likelihood and the prior respectively. The parameters θ, ϕ typically parametrize
two neural networks, allowing for highly complex, nonlinear relations. Unlike discriminative
models that require labeled outputs, e.g., recurrent neural networks for sequence prediction,
V AEs learn probabilistic latent representations in an unsupervised or semi-supervised manner,
which is valuable for problems where formal labels are lacking.
V AEs are widely used across disciplines, and the literature in management, marketing, and
information systems is seeing a growing number of V AE-based applications. Existing studies
are mainly concentrated in three areas: (i) recommender systems, where the objective is
ranking or personalization, (ii) marketing design with high-dimensional inputs such as images
and (iii) text applications that learn predictive, managerially interpretable representations. In
recommender systems, Liang et al. (2018) propose a multinomial V AE for implicit-feedback
that uncovers nonlinear user-item structure, improving personalization from sparse click and
purchase histories. Similarly, Bauman et al. (2025) learn latent representations for context-
aware recommendation and Boughanmi et al. (2025) use message-passing V AEs on interlocked
hypergraphs to model categorized consumer collections (e.g., playlists) and learn embeddings
for consumers, items, and categories. In marketing design applications, studies focus on
high-dimensional inputs and design exploration. Dew et al. (2022) develop a multimodal
V AE aligning logo images with textual brand descriptors to support counterfactual analyses
of design choices and brand perceptions. In short-form video marketing, Tian et al. (2024)
7

summarize TikTok content into latent video quality representations for causal influencer
selection. In new product development, Burnap et al. (2023) combine a probabilistic V AE
with adversarial training to learn a controllable latent space of product aesthetics that predicts
appeal and generates novel designs. Extending these ideas to decision-centric conjoint, Sisodia
et al. (2025) recover interpretable latent visual factors from images and deploy them for
visual conjoint analysis. Broadening beyond recommendation and vision, Yang et al. (2023)
integrate a V AE with task supervision to produce predictive, managerially interpretable
topics from text.
Taken together, this literature shows that V AE-based representations can capture complex,
nonlinear structure beyond traditional parametric models. A common theme is that this added
flexibility can improve predictive performance when hand-crafted features or linear latent-
factor models are insufficient. However, prior work has not examined V AEs in the context of
customer base analysis. That is, using V AEs to model customer heterogeneity from sparse
and irregular transaction histories in order to support long-term revenue prediction in non-
contractual settings. More broadly, the paper contributes a modeling template for embedding
domain-specific, process-based likelihoods into V AEs, enabling flexible representation learning
without discarding econometrically meaningful process structure.
3 Model
Following our review of the relevant literature, we now derive our novel V AE-based approach.
Thereby, we first detail the structure of the new model and then the respective estimation
and prediction routine. While the first three sections detail the basic model structure, we
subsequently illustrate how to extend this basic model structure, i.e., by adding covariates
and by making more extensive use of customers’ transaction history. Appendices A to D
accompany the discussion in this section.
3.1 Model specification
Building on the definition given in Section 2.2, we note that a V AE is a neural network
technique that employs a Bayesian modeling paradigm, in which we model variables X of
dimension D using latent variables Z of smaller dimension d (Kingma and Welling 2014).
In doing so we must specify the prior p(Z), which usually does not depend on parameters,
and pθ(X|Z ), depending on a neural net parametrized by θ. Although it might also be
possible to obtain the posterior Z|X in a V AE, this is approximated by another distribution
qϕ(Z|X ). Note that in most applications, pθ(X|Z ) = N (µθ(Z), Σθ(Z)), where µθ, Σθ are
8

functions learned by a neural net with parameters θ. However, our work takes a different
route by adapting the V AE framework to the Pareto/NBD and the GG model. In this model,
X = (x, tx, T,¯z) are observed for each customer – i.e., the indicators for customers’ recency,
frequency, and monetary value (RFM) – and then modeled as latent variables Z = (λ, µ, ν).
They are sometimes referred to as latent heterogeneity variables. As such, the Pareto/NBD
and the GG model can naturally be embedded into a V AE-based framework.
Figure 2 illustrates our modeling framework, whereby pθ(x, tx, T,¯z|λ, µ, ν) is specified
𝑿
𝒙
𝒕𝒙
𝑻
𝒛
𝑿′
𝒙′
𝒕𝒙′
𝑻′
𝒛′
Input Reconstructed Input
𝜶
𝜷
𝜸 𝝀
𝝁
𝝂
Probabilistic Encoder
𝒒𝝓(𝝀, 𝝁, ȁ𝝂 𝒙, 𝒕𝒙, 𝑻, 𝒛)
Ideally identical:
𝑿 ≈ 𝑿′
Sampled
Latent
Vector
Rate
Shape
𝒓
𝒔
𝒒
𝝀 ~ 𝑮𝒂𝒎 𝜶, 𝒓
𝝁 ~ 𝑮𝒂𝒎 𝜷, 𝒔
𝝂 ~ 𝑮𝒂𝒎(𝜸, 𝒒)
Probabilistic Decoder
𝒑𝜣(𝒙, 𝒕𝒙, 𝑻, ȁ𝒛 𝝀, 𝝁, 𝝂) 𝑿′𝑿
Reconstruction loss + KL divergence
Generation
Figure 2: Conceptual Visualization of the CL V AE model
9

as,
pθ(X|Z)
=p θ(x, tx, T,¯z|λ, µ, ν)
=
 Λθ(λ, µ, ν)xMθ(λ, µ, ν)
Λθ(λ, µ, ν) +Mθ(λ, µ, ν)
e−(Λθ(λ,µ,ν)+Mθ(λ,µ,ν))tx
+ Λθ(λ, µ, ν)x+1
Λθ(λ, µ, ν) +Mθ(λ, µ, ν)
e−(Λθ(λ,µ,ν)+Mθ(λ,µ,ν))T

(Nθ(λ, µ, ν)x)px
Γ(px) ¯zpx−1e−Nθ(λ,µ,ν)x¯z.(1)
Note that if Λ θ(λ, µ, ν) = λ, Mθ(λ, µ, ν) = µ and Nθ(λ, µ, ν) = ν, pθ(x, tx, T,¯z|λ, µ, ν) is
the standard likelihood of the Pareto/NBD and GG model conditioned on the latent variables:
That is, equation (1) combines the likelihood of the Pareto/NBD model (Fader and Hardie
2005, Equation (14)) with the density of the GG model (Fader and Hardie 2013). However, now
complex interactions between the latent variables are possible, leading to potentially arbitrary
dependence, as well as nonstandard distributions for (Λ θ(λ, µ, ν), Mθ(λ, µ, ν), Nθ(λ, µ, ν)),
even if λ, µ, νare sampled from independent Gamma distributions, as in the original
Pareto/NBD and GG model.
Following the V AE framework, we then approximate the posterior by using the function
qϕ(Z|X)
=q ϕ(λ, µ, ν|x, tx, T,¯z)
= αϕ(X) rϕ(X)λrϕ(X)−1 exp[−λαϕ(X)] Γ(rϕ(X))
βϕ(X) sϕ(X)µsϕ(X)−1 exp[−µβϕ(X)]
Γ(sϕ(X))
γϕ(X) qϕ(X)ν qϕ(X)−1 0 exp[−ν0γϕ(X)]
Γ(qϕ(X)) ,(2)
which is simply the product of three independent Gamma distributions, again motivated by
the Pareto/NBD and GG model, in which the latent variables are modeled with independent
Gamma distributions. Finally, again following the traditional framework of the Pareto/NBD
and GG model, we assume theprior p(Z) = p(λ, µ, ν) to be the product of independent
10

Gamma distributions:
p(λ, µ, ν) =αrp p λ rp−1 e−αpλ
Γ(rp)
βsp p µ sp−1 e−βpµ
Γ(sp)
γqp p ν qp−1 e−γpν
Γ(qp) ,(3)
where the prior parameters αp, rp, βp, sp, γp, qp are fixed, e.g., using the optimized values
from a fitted Pareto/NBD and GG model (see also Online Appendix 2).
We note that choosing both the prior p(λ, µ, ν), as well as the variational approximation
to the posterior qϕ(λ, µ, ν|x, tx, T,¯z) as the product of independent Gamma distributions,
not only aligns well with the framework of the Pareto/NBD as well as the GG model, but also
allows for efficient estimation and prediction, as outlined in the next two sections. However,
as mentioned above, the combination of the Pareto/NBD and GG model likelihood in (1) is
then based on (Λ θ(λ, µ, ν), Mθ(λ, µ, ν), Nθ(λ, µ, ν)), which share complex dependencies and
nonstandard distributions, leading to a true joint model of transaction, attrition and spending.
Finally, following the Pareto/NBD and GG model, we only consider the RFM indicators in
the proposed model, but we note that various extensions to include further information are
possible. Respective model extensions are discussed in Section 3.4 and 3.5.
3.2 Estimation
Having established the model specification, we now turn to the estimation procedure. Central
to our inference strategy is the maximization of the Evidence Lower Bound (ELBO), which
provides a tractable variational approximation to the intractable posterior over both the
latent variables and the learned hyperparameters. We now detail the ELBO formulation, its
decomposition, and the stochastic optimization routine used to train the parameters ( ϕ, θ).
See also Appendix A.
Following the V AE framework (Kingma and Welling 2014), the ELBO can be derived as:
Lθ,ϕ(X) =E qϕ(λ,µ,ν|X)

logp θ(X|λ, µ, ν)
−KL

qϕ(λ, µ, ν|X)∥p(λ, µ, ν)

,(4)
where KL

qϕ(λ, µ, ν|X) ∥p (λ, µ, ν)

is the Kullback-Leibler (KL) divergence between the
variational posterior and the prior for the latent variables ( λ, µ, ν). Hence, the ELBO
naturally decomposes into a trade-off between two terms: (a) a likelihood term, which
quantifies how well the model, via the variational distribution, explains the observed data
under the probabilistic decoder, and (b) a regularization term, which penalizes divergence
11

from the prior distribution over the latent variables. Consequently, optimizing the ELBO
enables scalable unsupervised learning of the approximate posterior distribution over the
latent variables.
The first term in the ELBO, pθ(X|λ, µ, ν), is given in equation (1). Moreover, using
equations (2) and (3), the variational posterior and prior factorize over the components as
KL

qϕ(λ, µ, ν|X)∥p(λ, µ, ν)

= KL

qϕ(λ|X)∥p(λ)

+ KL

qϕ(µ|X)∥p(µ)

+ KL

qϕ(ν|X)∥p(ν)

.(5)
Each component KL divergence between Gamma distributions with variational parameters
(αq, βq) and prior parameters (α p, βp) admits the explicit form according to Penny (2001),
KL

Gamma(αq, βq)∥Gamma(α p, βp)

= (αq −α p)ψ(α q)−log Γ(αq) Γ(αp)
+α p(logβ q −logβ p) +α q
βp −β q
βq
,(6)
where ψ(·) denotes the Digamma function (see e.g., Abramowitz and Stegun (1972)).
This allows to efficiently approximate (4) using values sampled from (2) and, in turn, to
approximately minimize (4) using standard stochastic gradient descent methods. We refer to
Appendix B for further details.
3.3 Prediction
After fitting the proposed model, we generate predictive distributions for customer-level
outcomes via fully vectorized Monte Carlo simulation. For details, see Appendix C.
For a customer i with transaction history xi, Ti, txi, we seek to predict total spending in
period [Ti, Ti + t]. Let Λ θ(λi, µi, νi) and Mθ(λi, µi, νi) denote the latent purchase and dropout
rates, respectively. Let moreover Ω i define the latent lifetime of a customer.
Following the proposed model, note that Ω i ∼Exp (Mθ(λi, µi, νi)) and by the memoryless-
ness property of the exponential
Ωi −T i |Ω i > Ti ∼Exp(M θ(λi, µi, νi)) (7)
The probability that an individual customer remains active at time Ti was originally
12

derived for the standard Pareto/NBD model by Schmittlein et al. (1987). It is computed as
P(Ω> Ti |X i, Zi)
=

1 + Mθ(λi, µi, νi) Λθ(λi, µi, νi) +M θ(λi, µi, νi)

e(Λθ(λi,µi,νi)+Mθ(λi,µi,νi))(Ti−txi ) −1  −1 .(8)
Note that in our model, this expression depends on the latent parameter of spending, νi as
well.
Thus, conditioned on the event that Ω i > Ti, dropout times Ω i can be sampled using an
exponential distribution with rate Mθ(λi, µi, νi), as in (7). For each customer deemed alive,
purchases are simulated sequentially with inter-purchase times drawn from an exponential
distribution with rate Λ θ(λi, µi, νi),
tx+j−1,x+j ∼Exp(Λ θ(λi, µi, νi)).(9)
as long as
Ti +
JX
j=1
tx+j−1,x+j ≤min(T i +t,Ω i) (10)
where t is the time horizon. The total number of simulated purchases for customer i in
simulation l is denoted by N (l) i , and the point estimate of expected purchase frequency is
given by
ˆNi = 1 L
LX
l=1
N (l) i ,(11)
whereLis the number of Monte Carlo samples.
Conditional on purchase counts, the total spending amount simulated from a Gamma
distribution parameterized by the auxiliary latent variables:
S(l) i ∼Gam(p·N (l) i , q).(12)
The expected total spending per customer is obtained as ˆSi = 1 L PL l=1 S(l) i . We note that this
simulation also makes it directly possible to generate the full distribution of predicted period
spending.
13

3.4 Model extensions: Adding covariates to account for contextual
factors
Adding covariates within the V AE framework is not only straightforward, but also goes
beyond what covariate implementations of traditional probabilistic models for customer base
analysis can do (e.g., Abe 2009).
Often, companies have access to relevant contextual information that can be represented
by vectors of covariates Y P i , YA i , YS i for each customer i. Examples include customers’ age,
gender, or acquisition cohort membership. The latter describes an indicator variable that
details when customers started purchasing from a business as these customers have likely
been acquired through the same campaign they are often assumed to be similiar in their
behavior. So far, such covariates were incorporated into the Pareto/NBD and GG model
using a proportional hazard approach, whereby individual latent parameters were defined
through λi = exp(γ⊤ purchY P i )λ, µi = exp(γ⊤ attY A i )µ, νi = exp(γ⊤ spendY S i )ν, with λ∼Gam (α, r),
µ∼Gam (β, s) and ν∼Gam (γ, q) as before. This effectively rescaled the latent variables
for each customer, which is equivalent to drawing the latent variables from rescaled Gamma
distributions:λ i ∼Gam(α i, r),µi ∼Gam(β i, s) andνi ∼Gam(γ i, q), where
αi = exp(−γ⊤ purchY P i )α, βi = exp(−γ⊤ attY A i )β,
γi = exp(−γ⊤ spendY A i )γ
Although this approach is powerful, it is also relatively simple and only allows the scale
parameters of each Gamma distribution to be affected by the covariates. This might be
limiting in many instances. To illustrate this point, we briefly elaborate on the current practice
to account for customers’ assignment to an acquisition cohort, which is known to be an
important contextual factor in customer base analysis. If a business conducts a customer base
analysis, differences between customer acquisition cohorts are usually accounted for. Current
modeling practices mainly offer two ways to do so: (I) using separate Pareto/NBD and GG
models for each cohort, or (II) defining covariates that indicate a customer’s acquisition
cohort and fit a single Pareto/NBD and GG model with these indicator variables for all
cohorts. While (II) is much more sample efficient, the covariates can only influence α, β
and γ and do not lead to individual shape parameters. Thus, approach (II) is often less
effective than (I). This is also related to the fact that the traditional framework relying on the
Pareto/NBD and GG model naturally has limited flexibility, as does any parametric approach.
Additionally, if customers from different acquisition cohorts are widely similar, choosing (II)
might actually hurt the predictive performance of the model as adding irrelevant covariates
14

often increases the estimation error in the traditional probabilistic modeling framework (see
Online Appendix 2).
Our approach delivers a natural way to extend this framework by letting the covariates
enter the probabilistic encoder. That is, we now define for a random customer with covariates
Y=

Y P , YA, YS the posteriorq ϕ(Z|X,Y) =q ϕ(λ, µ, ν|x, tx, T,Y) using

 r(X,Y) α(X,Y) s(X,Y) β(X,Y) q(X,Y)
γ(X,Y))

 =f ϕ(X,Y)
To see the increased flexibility of this approach, consider the generation of the latent
parameter λ: In both cases, we draw λ∼Gam (α, r). In the case of the standard Pareto/NBD
and GG model, we then use the transformation exp(γ⊤ purchY P )λ, changing only the scaling,
i.e.,
exp(γ⊤ purchY P )λ∼Gam(exp(−γ ⊤ purchY P )α, r).
However, in the proposed CL V AE,Yenters into the Gamma distribution trough the highly
flexible encoder, which even if we disregard the effect of µ, ν, may lead to a complete change
in the distribution. As such, the covariates can have a much larger effect on the model, not
just changing the scaling but also the shape of the latent distributions. We will leverage this
new framework in Section 4 to provide a more effective version of approach (II).
Finally, we note that adding covariates generally increases the computational complexity
for any approach. However, the V AE framework can be run on highly optimized computational
hardware, which enables fast estimation and prediction - even for models with many covariates
(see also Online Appendix 2).
3.5 Model extensions: Leveraging additional information in cus-
tomers’ transaction data
Our base model follows the guidance of the Pareto/NBD and GG model and only uses
the recency, frequency, and monetary indicators X = ( x, tx, T,¯z) . In other words, the
transaction history of each customer is represented by only four variables. In addition to
being data parsimonious, this also has the advantage of making the model more stable over
a range of settings. However, in Appendix D, we present an extension in which a bivariate
15

Long Short-Term Memory (LSTM) model (Hochreiter and Schmidhuber 1997) is used to
instead encode the full transaction and spending history of customers. We also note that
a Transformer-based architecture (Vaswani et al. 2017) can be used instead. These model
variations have the potential to leverage substantially richer information, but they also require
considerably more parameter tuning and validation to achieve strong performance.
Whether this additional investment is worthwhile depends on the business setting and,
in particular, on the extent to which the underlying customer behavior exhibits meaningful
temporal structure or additional irregularity that is not accounted for by the RFM data. In
the latter case, LSTM- or even Transformer-based architectures can be effective in exploiting
such patterns. However, when the data are closer to a memoryless process (e.g., approximating
Poisson-type dynamics or i.i.d. purchase events), interpurchase times are largely independent
over time. In this setting, an LSTM may primarily fit noise, increasing model variance and
the risk of overfitting without improving out-of-sample generalization. Taken together, these
considerations motivate offering both model variations, so the practitioner can match the
model complexity to the richness of the data. Regardless of which variant is used, the core
idea of the proposed modeling approach remains the same, with the architecture merely
adapting to the complexity of the data.
In sum, our novel approach provides an innovative way to generalize the traditional
framework given by the Pareto/NBD and GG model. It permits both the latent variable
distributions and the conditional likelihood to be adaptively modulated by the data through
a deep neural network. As a result, the proposed model is capable of learning complex, data-
dependent relationships between covariates and latent behavioral characteristics. Thereby, it
achieves a degree of modeling flexibility surpassing that afforded by traditional parametric
methodologies.
4 Empirical application
The empirical assessment of the proposed neural network model is based on the analysis
of multiple real-world datasets. A description of these datasets follows in the next section.
Then, we apply the proposed model to these datasets and evaluate its accuracy for customer
revenue projections. Throughout, we evaluate predictions of customer-level cumulative
realized revenue during each holdout period, computed directly from the holdout transactions.
Thereby, we also provide a comparison with key benchmark models. All models are estimated
using only transactions within the estimation window. The holdout window is used exclusively
for out-of-sample evaluation, and no features or preprocessing steps use information from the
holdout period. We report results for up to four holdout horizons, measured from the end of
16

the estimation window, to reflect use cases with different forecasting requirements (52, 104,
156, 208 weeks). See Table 1 for details.
The proposed model is applied in two variations, with and without covariates. As both
cases are fairly common in industry applications, this allows assessing the model’s ability
to deliver reliable results in either case. The model implementation was executed using the
PyTorch framework (Paszke et al. 2019). For a detailed description of the model training, we
refer to Appendix B. Notably, the CL V AE models are trained with the same hyperparameters
across datasets. This avoids confounding performance differences due to dataset-specific
hyperparameter tuning. As a consequence, we interpret the results as conservative performance
estimates that emphasize comparability and robustness over dataset-specific optimization. As
mentioned above, Appendix D also presents a version of the model using the full transaction
history, instead of the more parsimonious RFM data.
We compare the proposed model to three alternatives. We deliberately select benchmarks
that are widely used in practice (PNBD + GG), represent a competitive deep-learning baseline
(LSTM + GG), and reflect state-of-the-art joint likelihood modeling (PNBDGGII). First,
the traditional approach relying on the Pareto/NBD model with and without covariates
(Schmittlein et al. 1987, Abe 2009, Bachmann et al. 2021) combined with the Gamma-Gamma
model (Colombo and Jiang 1999, Fader et al. 2005b). Due to its wide accessibility through
open-source software (e.g., Dziurzynski et al. 2021), this is likely the most used modeling
approach in industry. Second, the LSTM model by Valendin et al. (2022) combined with
the Gamma-Gamma model. The LSTM model not only has the ability to include covariates
but the implementation provided by the original authors also derives and includes seasonal
regularities and thereby constitutes a particularly strong benchmark. Further, we use the
hyperparameters recommended by the authors. Third, we implemented an improved version
of the joint model proposed by Glady et al. (2015) that builds on the foundations of the
Pareto/NBD and GG model but also captures inter-customer and intra-customer correlations.
This model also allows to include covariates in all three processes. For details, see Online
Appendix 3.
4.1 Data
This study features three real-world datasets that have been selected to cover a broad spectrum
of commonly observed customer purchase behavior. This also applies to data availability in
terms of covariates. The datasets originate from different industries and include purchase
records from three retailers: Retailer A (Marketing EDGE 2013), Retailer B (Ni et al. 2012),
and Retailer C (Kaggle 2018). This ensures that the benchmarking sufficiently accounts for
17

the robustness of each model across a variety of scenarios.
In addition to this reasoning, a key criterion for selecting these datasets was also their
accessibility. All datasets are publicly available, which facilitates replication of the reported
results. Because covariate information in public datasets is often limited, proprietary datasets
may yield better predictive performance by providing richer contextual variables. Balancing
the trade-off between using public and proprietary datasets, our benchmarking setup highlights
the practical importance of methods that remain reliable when only transaction histories are
available, while still providing a pathway to leverage richer covariates when firms have them.
Table 1: Key Descriptive Statistics
Dataset Retailer A Retailer B Retailer C
Total number of customers 4,785 4,661 5,843
Acquisition cohort definition a 12 months 24 months 24 months
Estimation period 2 years 2 years 2 years
Holdout period 4 years 3 years 4 years
Zero repeaters 55.4% 48.1% 27.6%
Number of purchases b 19,854 19,938 20,628
Average number of transactions b
(standard deviation)
4.15
(5.76)
4.28
(4.60)
3.53
(3.19)
Average transaction valueb
(standard deviation)
75.99
(138.20)
338.19
(496.11)
40.14
(66.23)
Average interpurchase timeb
(standard deviation)
33.56
(22.13)
54.26
(50.49)
21.65
(16.21)
Publicly available yes yes yes
Note: a The acquisition cohort definition indicates the time bin used to group customers by acquisition date (e.g., 12-month
cohorts). b Quantities measured for the estimation period.
Table 1 provides a summary of key descriptive statistics for all datasets. Importantly, the
datasets span regimes with high one-time purchase rates, long interpurchase times, and high
spend dispersion, directly reflecting the sparse and heterogeneous conditions under which
long-horizon revenue forecasting is most difficult. For example, the inter-purchase time varies
across the datasets between 21 and 54 days, while at the same time the average transaction
value varies between 40 and 338 USD. Also, the descriptive statistics for zero-repeaters, i.e.
customers who only purchase a single time, vary considerably between 27% and 55%. For all
datasets, purchase records are available for multiple years, which enables testing of different
prediction horizons. We conclude that this dataset selection facilitates robust benchmarking.
18

4.2 Results
We present the results of our benchmarking in two parts. First, we assess the predictive
performance for our proposed approach for scenarios where covariate data is not available.
Second, we leverage a case study that mimics a real-world customer base analysis application
to assess the predictive performance of our proposed approach for scenarios where covariate
data is available. This structure isolates the value of (i) flexible latent heterogeneity modeling
in the absence of covariates and (ii) the incremental predictive value of incorporating covariates
for a common use case.
The first benchmarking focuses on comparing four models over different prediction horizons.
For all models, we compare the predictive performance for customer-level revenue prediction
based on the root-mean-square error metric for each holdout period. Each model is trained
on two years of data (see Table 1). As mentioned above, in addition to our novel approach,
we also estimate the Pareto/NBD model combined with the GG model (PNBD + GG), the
LSTM model combined with the GG model (LSTM + GG), and a joint model based on
the work of Glady et al. (2015) (PNBDGGII). None of these models uses customer-level
covariates. However, the LSTM implementation automatically adds seasonality features, so
it effectively benefits from additional inputs relative to the other benchmarks. Further, note
that using models without any covariates is still a common choice due to privacy regulations,
data quality issues (e.g., high number of missing values), or the requirement to build less
complex predictive models in a shorter period of time.
The results of this first benchmarking are presented in Table 2 and are complemented
by Online Appendix 1, which reports mean absolute error (MAE). Overall, the evidence
supports the proposed CL V AE (Model 4) as the most accurate approach in this no-covariates
setting. Across datasets and prediction horizons, CL V AE delivers the lowest out-of-sample
RMSE.
Relative to the traditional two-stage baseline PNBD + GG (Model 1), CL V AE yields
systematic improvements that persist across different revenue scales and dispersion levels.
For Retailer A, the gains widen substantially over longer horizons (e.g., 352.40 vs. 459.58 at
208 weeks), suggesting that jointly capturing heterogeneity in attrition, transaction timing,
and spending improves long-term revenue forecasts even when using parsimonious RFM-style
inputs rather than full transaction histories (see Appendix D). The same pattern is observed
for Retailer B, where revenue levels and dispersion are markedly higher. CL V AE remains
best at each reported horizon (e.g., 1,291.00 vs. 1,328.44 at 156 weeks), suggesting that the
advantage generalizes beyond comparatively low-variance settings. For Retailer C, differences
are small at the shortest horizon, but CL V AE becomes clearly superior in the medium and
long term (104 to 208 weeks).
19

Table 2: Benchmarking of models without covariates (RMSE customer-level revenue predic-
tions)
Dataset Model Prediction Periods (W eeks) 52 104 156 208
Retailer
A
(1) PNBD + GG 119.59 219.75 336.24 459.58
(2) LSTM + GG 105.58 173.67 262.14 359.41
(3) PNBDGGII 126.57 188.90 276.22 369.22
(4) CL V AE102.00 165.09 256.23 352.40
Retailer
B
(1) PNBD + GG 578.07 968.47 1,328.44 -
(2) LSTM + GG 612.28 1,069.45 1,529.45 -
(3) PNBDGGII 628.68 975.35 1,300.08 -
(4) CL V AE565.90 945.12 1,291.00-
Retailer
C
(1) PNBD + GG 102.58 188.95 265.00 342.42
(2) LSTM + GG 103.01 190.48 259.32 321.99
(3) PNBDGGII 113.01 206.61 279.69 344.62
(4) CL V AE98.73 175.84 236.70 293.35
Note: RMSE is computed across customers using cumulative realized revenue over the indicated prediction horizon. The best
performing model per scenario is highlighted in bold.
Importantly, these improvements are not explained simply by adopting any joint spec-
ification or by relying on sequence-based prediction. The joint model benchmark (Model
3) does not close the gap to CL V AE and is often comparable to, or worse than, the PNBD
+ GG baseline, implying that coupling processes through a more rigid joint formulation is
insufficient. Meanwhile, the LSTM + GG benchmark (Model 2), which is explicitly designed
to take advantage of sequential purchase histories, can be competitive in some cases, but
it still does not match CL V AE’s accuracy across prediction horizons. Taken together, the
pattern is consistent with CL V AE’s flexible latent-variable structure capturing persistent
customer-level heterogeneity across attrition, transaction timing and spending, translating
into systematically improved customer-level revenue predictions, especially as uncertainty
compounds over longer forecast windows. Notably, this conclusion is conservative with respect
to the LSTM + GG benchmark, which benefits from additional engineered seasonality inputs,
yet does not dominate CL V AE at longer horizons.
A second benchmarking focuses on assessing the ability to account for contextual in-
formation through covariates. To this end, we leverage a case study that looks at one of
the key modeling challenges in customer base analysis, i.e., how to best account for het-
erogeneity between customers from different acquisition cohorts. Industry practice follows
20

recommendations from scholarly research, where instead of looking at the entire customer
base, possible observed heterogeneity is accounted for by distinguishing more homogeneous
cohorts of customers. These cohorts are formed according to the time period a customer
started buying from the firm. There are multiple ways to address this from a modeling
perspective:
• A naive approach would ignore this readily available information and estimate a single
model across the entire customer base, which comes with minimal modeling complexity
but also ignores a well-founded source of observed customer heterogeneity.
• An alternative fits models such as the Pareto/NBD and GG separately for each of these
cohorts. This reflects the assumption that customers that start in the same period (e.g.
month) are relatively similar, and thus might be captured well by a parametric model.
However, not only does this increase computational complexity and technical debt due
to the estimation of multiple models, but this approach also may pose a challenge when
estimating separate models for customers that have only been observed for a few days,
weeks, or even months. In the latter case, the available training data is limited, which
may lead to convergence issues during estimation or unreliable results. However, this
approach has the advantage that all model parameters can vary by customer acquisition
cohort, allowing for a lot of flexibility to adapt to particular purchase patterns for these
customer groups.
• Another alternative is to explicitly account for the information on customers’ acquisition
cohort in the model. In other words, a single model that accounts for a customer’s
assignment to a cohort with covariates is used to assess simultaneously all customers
in a firm’s customer base. Dummy variables are used to indicate in which period
a customer started the relationship with the business. Depending on the modeling
approach, this information is incorporated in different ways: (a) For the traditional
modeling approaches, such as the combination of the Pareto/NBD and the GG model,
the rate parameters α and β are cohort-specific, while all other parameters are shared.
While this approach reduces modeling complexity and technical debt, its ability to
account for the observed customer heterogeneity is limited. (b) For the LSTM model,
cohort membership is incorporated as a set of time-invariant customer-level covariates
that are replicated across all time steps, transformed through a dense layer, and then
concatenated with the time-varying seasonality and transaction inputs before being
processed by the recurrent layer—both during training and autoregressive forecasting.
(c) Including covariates on customers’ acquisition cohort membership in the CL V AE
model provides an alternative that combines all advantages. Being a single model, the
21

modeling complexity is low, and thus, the practical applicability is straightforward,
while the way that covariates are considered within the model provides similar levels of
flexibility than running individual cohort-level models.
This case study therefore tests whether cohort information is best handled via either
operationally costly cohort-specific model estimation or a single model that can flexibly
absorb cohort effects. We assess these alternatives for Retailer C, the largest among the
three datasets. For this dataset, we define monthly cohorts. As the training data builds on
a 24-month definition for the focal acquisition cohort (see Table 1), we define 24 monthly
cohort indicators to control for the homogeneity of customers acquired in the same month.
The cohorts are the foundation to apply the modeling alternatives described above. Results
are shown in Table 3, with the benchmarks from Table 2 added for convenience (Model 1 &
2). Model 3 mirrors the common operational workflow of fitting separate likelihood-based
models by acquisition cohort, which increases maintenance burden and can be unstable for
newly acquired cohorts with very little training data.
Table 3: Case study on models with covariates (RMSE customer-level revenue predictions;
Retailer C)
Model Prediction Periods (W eeks) 52 104 156 208
(1) PNBD + GG 102.58 188.95 265.00 342.42
(2) CL V AE 98.73 175.84 236.70 293.35
(3) PNBD + GG (separate model for each acquisition co-
hort)
103.75 190.79 265.79 338.17
(4) LSTM with covariates + GG 102.36 184.00 248.87 307.31
(5) PNBDGGII with covariates 111.75 204.40 276.46 340.12
(6) PNBD with covariates + GG 104.75 192.59 270.69 350.09
(7) CL V AE with covariates98.32 173.74 233.50 284.11
Note: RMSE is computed across customers using cumulative realized revenue over the indicated prediction horizon. The best
performing model per scenario is highlighted in bold.
Overall, the results show that cohort indicators can improve long-term revenue predictions,
but the gains depend strongly on whether the model can translate cohort differences into
flexible changes in customers’ attrition, transaction, and spending processes. The CL V AE
with covariates (Model 7) is the best-performing specification across all four horizons, and it
improves consistently over the same architecture without covariates (Model 2). This pattern
indicates that cohort membership adds an incremental predictive signal beyond what is
captured by the baseline CL V AE specification. In contrast, fitting separate PNBD + GG
models (Model 3) by monthly cohorts yields no gain over the single PNBD + GG model and
22

is slightly worse across prediction horizons, indicating that cohort splitting alone does not
translate into better long-horizon revenue forecasts in this setting. In this setting, CL V AE
with covariates delivers the accuracy benefits one would seek from cohort-specific modeling
while retaining a single-model deployment workflow.
The results also clarify why this advantage is specific to the proposed approach rather than
a generic “covariates help” effect. Adding cohort indicators to traditional parametric specifi-
cations yields limited improvements and can even degrade performance when heterogeneity is
forced through a narrow parameter subset (Model 6) or when estimation becomes more fragile
in richer joint specifications (Model 5). The LSTM model with covariates (Model 4) improves
over the covariate-free LSTM benchmark from Table 2, but it remains materially less accurate
than CL V AE with covariates. This applies especially to longer horizons, suggesting that the
proposed model extracts more of the cohort signal in the regime most relevant for long-run
value assessment.
Taken together, the evidence suggests that acquisition-cohort membership contains a
relevant predictive signal for long-term revenue. However, fully exploiting it requires a model
that can flexibly propagate cohort effects through the full set of latent processes governing
customers’ attrition, transaction timing and spending. The covariate-augmented CL V AE
provides this combination: a single deployable model with cohort-aware flexibility that delivers
the most accurate predictions across all forecast horizons in this case study.
Summing up the two benchmark studies, CL V AE improves customer-level long-horizon
revenue prediction across datasets and forecast horizons in non-contractual settings. This
supports its value when transaction histories are sparse and irregular and heterogeneity
modeling is consequential.
5 Discussion
This paper addresses a core problem in customer base analysis: forecasting long-horizon cus-
tomer revenue from sparse and irregular transaction histories in non-contractual settings. We
show that a V AE can bypass restrictive heterogeneity assumptions in traditional probabilistic
models while preserving their tripartite process structure. CL V AE keeps the Empirical-Bayes
anchoring that gives traditional models stability, but gains flexibility through amortized
inference that learns a nonparametric heterogeneity distribution. As a result, this hybrid
design provides robust, accurate, and scalable predictions, even with parsimonious data
input, while also being able to account for a broad set of covariates if available. Given these
properties, our novel approach is applicable to a diverse set of non-contractual business
settings. Managerially, this supports a single-model deployment workflow for long-horizon
23

revenue prediction, avoiding the operational burden of maintaining separate cohort-specific
models while still exploiting cohort information if available.
Our empirical results provide evidence that the combination of the V AE framework with
traditional probabilistic models advances customer base analysis. Previous literature has
identified several advantageous features for any customer base model that have not yet been
available in a single approach. Leveraging techniques from traditional probabilistic modeling
and deep learning, our approach brings together isolated streams within the literature on
customer base analysis. Thereby, the proposed approach does not just simply use the
standard V AE framework but carefully tailors it to traditional probabilistic customer base
models that have stood the test of time, namely the Pareto/NBD model and the GG model.
As a consequence, the approach yields an approximate posterior over customer-level latent
propensities that represent customers’ attrition, transaction, and spending processes. Thereby,
we extend strictly parametric mixing assumptions by learning a flexible latent representation
of heterogeneity. This design balances process discipline with flexible heterogeneity modeling,
improving stability in sparse regimes while avoiding purely autoregressive overfitting. In
addition, the proposed approach allows modeling the full dependence structure between the
individual processes.
In summary, CL V AE improves out-of-sample customer-level revenue forecasts relative
to traditional probabilistic approaches and competitive deep-learning across datasets and
prediction horizons. Critically, it does so with a single deployable model that remains data-
parsimonious when only transaction histories are available and can incorporate covariates
when firms have access to such information and are permitted to use it. This combination of
process-based structure with a learned heterogeneity distribution explains why gains persist
as the forecast horizon lengthens.
Compared to the application of an LSTM model as in Valendin et al. (2022), our approach
allows retaining some of the structure of the widely successful Pareto/NBD model, while
also allowing for a natural inclusion of the spending process via the GG model. In other
words, it still builds on the same economic primitives that defined the “gold standard” in
customer base analysis for several decades (Jerath et al. 2011) and thus contrasts itself to
standard autoregressive forecasting approaches. The natural split into customers’ attrition,
transaction and spending process is still present in the CL V AE model. This not only makes
our model more data parsimonious, working well with only the RFM data (in contrast to
the full transaction history), but can also lead to improved forecasts, as shown in Section 4.
On a technical level, we note that, while the approach of Valendin et al. (2022) necessitates
discretization of time, the CL V AE model builds on a process that is still truly continuous
with purchases potentially happening at any time point.
24

Several avenues emerge for future research. First, while we demonstrate performance
across multiple real-world datasets, an extension would be to include time-varying covariates
such as seasonality indicators. This would require defining time-varying latent variables in
the model specification. However, the proposed model in its current form already outperforms
deep-learning benchmarks that include such information (see Section 4). If the goal is
predictive accuracy at the customer level rather than evaluating the customer cohort as a
whole, the impact of adding such seasonality indicators, which vary only by calendar time but
not by customer, may be limited (Bachmann et al. 2021). Second, further extensions have
been proposed in customer base modeling that might be worth exploring in a V AE framework,
e.g., regularity of purchase behavior (Platzer and Reutterer 2016) or intra-customer process
correlation (Glady et al. 2015). While these extensions may be possible to accommodate
in the V AE framework, they also come with more data requirements. Beyond data on how
recently customers purchased, how often customers bought, and how much they spent, they
also require access to the complete transaction history. In conclusion, these directions for
further research would strongly build, but not change, the fundamental contribution that we
make with the present work. They may nevertheless provide further guidance for customer
base analysis in specific business settings.
In summary, our novel approach extends the toolkit of marketing researchers with a scalable
likelihood-based modeling technique that learns and leverages latent customer heterogeneity
for long-horizon revenue prediction in non-contractual settings. More broadly, we outline a
way to bring V AE-style representation learning to research settings where process structure
matters. Thus, the econometrically meaningful process structure can be retained rather
than replaced them with a black-box mapping. To facilitate replication and further research,
we released a Python implementation of our novel model along with code to reproduce our
results in a public repository (link removed to ensure anonymous review).
25

A Neural network architecture
The proposed approach is a deep generative framework for modeling customer revenue, in
particular, for deriving long-term prediction. Hereby, we generalize the combination of the
Pareto/NBD and the GG model into a single architecture that captures nonlinearities and
interactions in the latent posterior distribution. Key characteristics of the model have been
discussed, in Section 3.1. For key details of the model architecture, see Figure 3.
Input
X∈R 4 (RFM data) orX∈R 4+p (RFM data pluspcovariates)
Encoder Hidden 1
ReLU
Encoder Hidden 2
ReLU
Encoder Output
6 parameters via Softplus
rq, αq, sq, βq, qq, γq
encode
Latent VariableZ∼q ϕ(Z|X), Z∈R 3
sampling
Decoder Hidden 1
ReLU
Decoder Hidden 2
ReLU
Decoder Output
3 parameters via Softplus
Λθ(Z), Mθ(Z), Nθ(Z)
decode
ENCODER
DECODER
Figure 3: Architecture of the CL V AE model
The architecture comprises an encoder and a decoder, both implemented as fully connected
feedforward neural networks with ReLU activations. The encoder maps observed customer-
level features into the parameters of latent Gamma distributions, thereby defining customer-
level latent variables that capture heterogeneity in customer behavior. The decoder then
transforms sampled latent variables into the parameters of the conditional likelihood over
observed transactions, enabling probabilistic reconstruction of customer behavior .
The encoder maps the inputX, which consists of RFM data and, if available, customer-level
covariates, through two ReLU layers to produce six positive parameters ( rq, αq, sq, βq, qq, γq)
26

via a Softplus output layer, with biases initialized from Gamma prior means. The encoder is
parameterized byϕ, defining the variational posteriorq ϕ(Z|X).
Next, latent variables Z∈R 3 are sampled from this posterior and passed through the
decoder, which consists of two ReLU layers and outputs three positive parameters (Λ , M, N)
via Softplus, parameterized by θ, defining the conditional likelihood over observed customer
transactions.
B Neural network training
The model parameters ( ϕ, θ) are trained by maximizing the Evidence Lower Bound (ELBO)
via stochastic gradient descent. We adopt the canonical fitted parameters for the Pareto/NBD
and the GG model as prior parameters. In this context, we note that the likelihood (1) also
includes the parameter p. This parameter is fixed to the parameter obtained through the
GG model. However, it is also possible to adapt a fully Bayesian approach where p itself
is endowed with a prior distribution, with the posterior approximated by the V AE. Given
this setup, we encode the parameters of the variational latent Gamma distributions. Then,
the samples are drawn using differentiable, reparameterizable Gamma sampling, leveraging
stochastic primitives available in frameworks such as PyTorch (Figurnov et al. 2018).
For computational scalability, the dataset is randomly shuffled and partitioned into
mini-batches at each epoch. Since training is unsupervised, overfitting is monitored via
the validation ELBO, and early stopping is applied with a predefined patience criterion.
Architectural hyperparameters, including the number of hidden layers, units per layer, and
latent dimensionality, must be tuned according to dataset size and complexity, balancing
model expressiveness with generalization performance. To further improve stability in our
model, we initialize the output-layer biases of the encoder using Gamma prior means and
apply Softplus activations to ensure all inferred latent parameters remain positive.
The model hyperparameters and training configuration used to produce the results
reported in Section 4 are summarized in Table 4.
27

Table 4: Model hyperparameters and training configuration
Category Item V alue
Model Hyperparameters
Encoder hidden layers 2
Encoder units per layer 64, 32
Latent dimension 3
Decoder hidden layers 2
Decoder units per layer 32, 64
Training Configuration
Optimizer Adam
Learning rate 0.001
Loss ELBO
Batch size 64
Max epochs 1000
MC samples 10
Early stopping patience 100
Seed 50
C Prediction routine
In the following, we suppress the index i, writing out the simulation for a “generic” customer
and use the shorthand Λ θ = Λ θ(λ, µ, ν), Mθ = Mθ(λ, µ, ν) and Nθ = Nθ(λ, µ, ν). We
then repeatedly exploit that, conditional on Λ θ, Mθ, Nθ, the assumed data-generating process
follows the distribution of the Pareto/NBD and GG model. Note that spending is independent
of the number of transactions conditioned on Λ θ, Mθ, Nθ. Thus, if S(t) is the total spending
in the period [ T, T+ t) and N (t) the total number of transactions in [ T, T+ t), adapting the
derivations in Fader and Hardie (2005, 2013), we seek to approximate:
E[S(t)|r, α, s, β, x, tx, T]
=
Z ∞
0
Z ∞
0
Z ∞
T
E[
N(t)X
j=1
Sj |N θ,Λ θ, ω]
f(ω|M θ,Ω> T)dωP(Ω> T|Λ θ, Mθ, x, tx, T)
g(Λθ, Mθ, Nθ |x, tx, T,¯z)dΛθdMθdNθ.
28

In the above, E[PN(t) j=1 Sj |N θ, Λθ, ω] is the expectation over a random sum with N (t)
elements, whereby N (t) is the number of events in a Poisson process with parameter Λ θ on
[T,min(T+t, ω)], andS j ∼Gam(q, Nθ), and
P(Ω> T|Λ θ, Mθ, x, tx, T)
=

1 + Mθ
Λθ +M θ

exp

(Λθ +M θ)(T−t x)

−1
−1
,(13)
adapted from (Fader and Hardie 2005, Section 5). By the memorylessness property of the
exponential distribution, it follows that f (ω|M θ, Ω > T) is the density of an exponential
distribution itself with parameterM θ.
We simulate expected number of purchases and expected total spending, for all customers
using fully vectorized Monte Carlo simulations over latent variables Z = ( λ, µ, ν), and
horizons t1, . . . , tK. Let tmax = max(t1, . . . , tK). Though, we consider a generic customer
here, whenever possible calculations are vectorized over customers, simulations, and horizons.
1.Sample latent variables:Forl= 1, . . . , LMonte Carlo samples, draw
λl ∼Gam(ˆr,ˆα), µl ∼Gam(ˆs,ˆβ), νl ∼Gam(ˆq,ˆγ),
where the hyperparameters
(ˆr,ˆα,ˆs,ˆβ,ˆq,ˆγ,ˆp) =fϕ([x, tx, T,Y])
are outputs of the proposed neural network fϕ, optimized on the dataset, withY
representing covariates.
2.Combine latent posterior using the decoder:For each samplel, compute
(Λl θ, Ml θ, Nl θ) = Φθ(λl, µl, νl),
where Φθ is the encoder neural network optimized on the dataset.
3. Compute survival probability:Draw a Bernoulli mask for each customer and using
(13), simulating the event1{Ω> T}given Λ l θ, Ml θ, x, tx, T.
4.Sample dropout times:If the customer has1{Ω> T}= 1, draw
Ωl ∼T+ Exp(M θ),
29

otherwise if1{Ω> T}= 0 (customer is inactive afterT), set Ω l =T.
5.Simulate cumulative interpurchase times:Generate interpurchase times:
tl x+j−1,x+j ∼Exp(Λ θ), j= 1, . . . , Nmax,
and compute transaction times:
tl x,x+j =T+
jX
ℓ=1
tl x+ℓ−1,x+ℓ,
as long ast l x,x+j ≤min(T+t max,Ω l).
6. Multiple horizons:For a list of forecast horizons t1, . . . , tK, count valid purchases
per horizon by checking which cumulative times fall below each horizon and are before
dropout. This leads to a number N (l)(tk) of simulated transactions for simulation l and
horizont k.
7. Simulate total spending:Sample spending from a Gamma distribution for simulation
land horizont k:
S(l)(tk)∼Gam(shape =p·N (l)(tk),rate =q).
8. Compute expected values:Average over L simulations to get expected purchases,
spending for each customer and horizon:
E[N(t k)] = 1 L
LX
l=1
N (l)(tk),
E[S(tk)] = 1 L
LX
l=1
S(l)(tk).
9. V ectorization and scalability:All steps (survival, dropout, interpurchase, spending)
are implemented using fully vectorized tensor operations, enabling efficient simulation
for large numbers of customers and Monte Carlo samples without loops.
We note that certain steps in this simulation could be simplified with closed-form expres-
sions. However, speed gains appear to be modest and the previous formulation leaves room
to allow for more general models.
30

D Model extensions: Leveraging additional information
in customers’ transaction data
For a generic customer, let t0, t1, . . . , tx be the transaction times with associated spending
values z0, . . . , zx. Here, ( t0, z0) correspond to the timing and the spending of the first
transaction (i.e., a customer becoming ”alive”).
As discussed in the main text, the CL V AE outlined in Section 3.1, only considers RFM
indicators (x, tx, T,¯z). This is natural for the probabilistic decoder, as the likelihood of the
Pareto/NBD model combined with the likelihood of the GG model is a function of these
data only, as seen in Equation (1). Moreover, it can be shown that the posterior distribution
ofλ, µ, νconditioned on the transaction history also depends on (x, tx, T,¯z) only. Since the
encoder approximates this posterior distribution, this motivated our approach in the main
text. However, in the V AE framework the probabilistic encoder might benefit from having
access to the full transaction history to better approximate the posterior distribution.
As such, we build here a model extension, whereby we let the decoder depend on
the interpurchase timest= ( t0, t0,1, . . . , tx−1,x), with tj−1,j = tj −t j−1 and spendingz=
(z0, z1, . . . , zx). The encoder now uses X = [t, z], for a given customer to create the parameters
α(X), r(X), β(X), s(X), γ(X), q(X). This is used to sample the posterior ( λ, µ, ν) and then
fed into the same decoder as before. In practice, Xi now has different lengths for each
customer i. To deal with this, we use a bivariate LSTM model in the first layers of the
encoder. We refer to the model in the main text as CL V AE (RFM) and to the model using
the LSTM as CL V AE (LSTM). Importantly, we also considered the somewhat more complex
Transformer architecture (Vaswani et al. 2017) in place of the LSTM architecture, but did
not find consistent improvements across our datasets that would justify this computationally
more intensive approach.
There are two essential ways to look at CL V AE (LSTM) in comparison to CL V AE (RFM):
First, the encoder is now simply a neural net capable of taking the full transaction history as
an input. Second, in our CL V AE (LSTM) architecture, we concatenate an LSTM model with
the layers used in the encoder of the original CL V AE (RFM). As such, while we manually
compress the full transaction data into the RFM data ( x, tx, T,¯z) for the CL V AE (RFM),
the CL V AE (LSTM) learns the compression in the first step through an LSTM component.
In essence, this corresponds to exchanging a manual compression for one that is learned by
the model, bringing advantages and disadvantages simultaneously.
These considerations are reflected in the results of an additional benchmarking shown in
Table 5. While we are better than the original model for Retailer C, we are somewhat worse
in the other two, at least with our chosen tuning parameters. A crucial difficulty in the full
31

model lies in the fact that more tuning parameters must be chosen, in addition to a higher
estimation error.
Table 5: Benchmarking of additional models without covariates (RMSE customer-level revenue
predictions)
Dataset Model Prediction Periods (W eeks) 52 104 156 208
Retailer
A
(2) CL V AE (RFM) 102.00 165.09 256.23 352.40
(5) CL V AE (LSTM)99.82 161.15 249.24 338.86
Retailer
B
(4) CL V AE (RFM)565.90 945.12 1291.00-
(5) CL V AE (LSTM) 567.53 948.78 1299.21 -
Retailer
C
(4) CL V AE (RFM)98.73 175.84 236.70 293.35
(5) CL V AE (LSTM) 104.29 190.92 260.53 322.71
Note: The best performing model per scenario is highlighted in bold.
32

References
Abe M (2009) ”Counting Your Customers” One by One: A Hierarchical Bayes Extension to the
Pareto/NBD Model.Marketing Science28(3):541–553.
Abramowitz M, Stegun IA (1972) 6.3 psi (digamma) function. Abramowitz M, Stegun IA, eds.,
Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables, 258–259
(New York: Dover), 10th edition.
Bachmann P, Meierer M, N¨ af J (2021) The Role of Time-Varying Contextual Factors in Latent
Attrition Models for Customer Base Analysis.Marketing Science40(4):783–809.
Bauman K, Tuzhilin A, Unger M (2025) HyperCARS: Using Hyperbolic Embeddings for Generating
Hierarchical Contextual Situations in Context-Aware Recommender Systems.Information
Systems Research36(2):871–895.
Bemmaor AC, Glady N (2012) Modeling Purchasing Behavior with Sudden “Death”: A Flexible
Customer Lifetime Model.Management Science58(5):1012–1021.
Borle S, Singh SS, Jain DC (2008) Customer Lifetime Value Measurement.Management Science
54(1):100–112.
Boughanmi K, Ansari A, Li Y (2025) Modeling Categorized Consumer Collections with Interlocked
Hypergraph Neural Networks.Journal of Marketing Research62(6):1101–1124.
Braun M, Schweidel DA, Stein E (2015) Transaction Attributes and Customer Valuation.Journal
of Marketing Research52(6):848–864.
Burnap A, Hauser JR, Timoshenko A (2023) Product Aesthetic Design: A Machine Learning
Augmentation.Marketing Science42(6):1029–1056.
Colombo R, Jiang W (1999) A Stochastic RFM Model.Journal of Interactive Marketing13(3):2–12.
Dew R, Ansari A, Toubia O (2022) Letting Logos Speak: Leveraging Multiview Representation
Learning for Data-Driven Branding and Logo Design.Marketing Science41(2):401–425.
Dziurzynski L, Wadsworth E, McCarthy D (2021)BTYD: Implementing Buy ’Til You Die Models.
URLhttps://CRAN.R-project.org/package=BTYD,Rpackage version 2.4.3.
Fader PS, Hardie BG (2005) A Note on Deriving the Pareto/NBD Model and Related Expressions.
Technical Note9.
Fader PS, Hardie BG (2013) The Gamma-Gamma Model of Monetary Value.Technical Note25.
Fader PS, Hardie BG, Lee K (2005a) ’Counting Your Customers’ the Easy Way: An Alternative to
the Pareto/NBD Model.Marketing Science24(2):275–284.
Fader PS, Hardie BG, Lee K (2005b) RFM and CL V: Using Iso-Value Curves for Customer Base
Analysis.Journal of Marketing Research42(4):415–430.
Fader PS, Hardie BG, Shang J (2010) Customer-Base Analysis in a Discrete-Time Noncontractual
Setting.Marketing Science29(6):1086–1108.
33

Figurnov M, Mohamed S, Mnih A (2018) Implicit Reparameterization Gradients.Advances in
Neural Information Processing Systems (NeurIPS ’18), volume 31 (Montr´ eal, Canada).
Gabel S, Timoshenko A (2022) Product Choice with Large Assortments: A Scalable Deep-Learning
Model.Management Science68(3):1808–1827.
Glady N, Baesens B, Croux C (2009) A Modified Pareto/NBD Approach for Predicting Customer
Lifetime Value.Expert Systems with Applications36(2):2062–2071.
Glady N, Lemmens A, Croux C (2015) Unveiling the Relationship Between the Transaction Timing,
Spending and Dropout Behavior of Customers.International Journal of Research in Marketing
32(1):78–93.
Hochreiter S, Schmidhuber J (1997) Long Short-term Memory.Neural Computation9(8):1735–1780.
Jerath K, Fader PS, Hardie BGS (2011) New Perspectives on Customer ’Death’ Using a Generaliza-
tion of the Pareto/NBD Model.Marketing Science30(5):866–880.
Kaggle (2018) German Retail Book Store Dataset. URLhttps://www.kaggle.com/c/ralfdata/.
Kingma DP, Welling M (2014) Auto-Encoding Variational Bayes.Proceedings of the 2nd International
Conference on Learning Representations (ICLR ’14’), volume 2 (Banff, Canada).
Kingma DP, Welling M (2019) An Introduction to Variational Autoencoders.Foundations and
Trends in Machine Learning12(4):307–392.
Krishnan RG, Shalit U, Sontag D (2017) Structured Inference Networks for Nonlinear State Space
Models.Proceedings of the Conference on Artificial Intelligence (AAAI’17), volume 31 (San
Francisco, USA).
Lemmens A, Gupta S (2020) Managing Churn to Maximize Profits.Marketing Science39(5):956–973.
Liang D, Krishnan RG, Hoffman MD, Jebara T (2018) Variational Autoencoders for Collaborative
Filtering.Proceedings of the World Wide Web Conference (WWW ’18), volume 27 (Lyon,
France).
Marketing EDGE (2013) Dataset 9: Multichannel Gift Company. URL http://www.marketingedge.
org/marketing-programs/data-set-library.
Ni J, Neslin, A S, Sun B (2012) The ISMS Durable Goods Data Sets.Marketing Science31(6):1008–
1013.
Paszke A, Gross S, Massa F, Lerer A, Bradbury J, Chanan G, Killeen T, Lin Z, Gimelshein N,
Antiga L, Desmaison A, K¨ opf A, Yang E, DeVito Z, Raison M, Tejani A, Chilamkurthy S,
Steiner B, Fang L, Bai J, Chintala S (2019) Pytorch: An Imperative Style, High-Performance
Deep Learning Library.Advances in Neural Information Processing Systems (NeurIPS ’19),
volume 32 (Vancouver, Canada).
Penny WD (2001) KL-Divergences of Normal, Gamma, Dirichlet and Wishart Densities.Technical
Note.
34

Platzer M, Reutterer T (2016) Ticking Away the Moments: Timing Regularity Helps to Better
Predict Customer Activity.Marketing Science35(5):779–799.
Schmittlein DC, Morrison DG, Colombo R (1987) Counting Your Customers: Who Are They and
What Will They Do Next?Management Science33(1):1–24.
Schmittlein DC, Peterson RA (1994) Customer Base Analysis: An Industrial Purchase Process
Application.Marketing Science13(1):41–67.
Schweidel DA, Knox G (2013) Incorporating Direct Marketing Activity into Latent Attrition Models.
Marketing Science32(3):471–487.
Simester DI, Sun P, Tsitsiklis JN (2006) Dynamic Catalog Mailing Policies.Management Science
52(5):683–696.
Sisodia A, Burnap A, Kumar V (2025) Generative Interpretable Visual Design: Using Disentangle-
ment for Visual Conjoint Analysis.Journal of Marketing Research62(3):405–428.
Tian Z, Dew R, Iyengar R (2024) Mega or Micro? Influencer Selection Using Follower Elasticity.
Journal of Marketing Research61(3):472–495.
Valendin J, Reutterer T, Platzer M, Kalcher K (2022) Customer Base Analysis with Recurrent
Neural Networks.International Journal of Research in Marketing39(4):988–1018.
Vaswani A, Shazeer N, Parmar N, Uszkoreit J, Jones L, Gomez AN, Kaiser  L, Polosukhin I (2017)
Attention is All You Need.Advances in Neural Information Processing Systems (NeurIPS ’17),
volume 30 (Long Beach, USA).
Yang Y, Zhang K, Fan Y (2023) sDTM: A Supervised Bayesian Deep Topic Model for Text Analytics.
Information Systems Research34(1):137–156.
35
