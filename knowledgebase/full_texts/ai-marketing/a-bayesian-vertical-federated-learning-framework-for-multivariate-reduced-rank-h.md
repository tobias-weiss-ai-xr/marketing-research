---
title: A Bayesian Vertical Federated Learning Framework for Multivariate Reduced-Rank High-Dimensional
  Regression
url: https://arxiv.org/abs/2609.22654
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Brigham Halverson
- Sharmistha Guha
- Jessica Bernard
- Rajarshi Guhaniyogi
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.22654
pages: 37
chars: 82392
fetched_at: '2026-11-08T13:26:01+00:00'
kb_version: 1
---

# A Bayesian Vertical Federated Learning Framework for Multivariate Reduced-Rank High-Dimensional Regression

A Bayesian Vertical Federated Learning Framework for
Multivariate Reduced-Rank High-Dimensional
Regression
Brigham Halverson
Department of Statistics
Texas A&M University
birghalvy@tamu.edu
Sharmistha Guha
Department of Statistics
Texas A&M University
sharmistha@tamu.edu
Jessica Bernard
Department of Psychological & Brain Sciences
Texas A&M University
jessica.bernard@tamu.edu
Rajarshi Guhaniyogi
Department of Statistics
Texas A&M University
rajguhaniyogi@tamu.edu
Abstract
Federated learning (FL) has emerged as a leading privacy-preserving framework
for collaborative machine learning across decentralized environments. While consid-
erable progress has been made in horizontal federated learning (HFL), where data
with common features is distributed across sites, vertical federated learning (VFL),
where sites share observations across distinct feature sets, remains less explored. Ad-
vancing Bayesian high-dimensional multivariate reduced-rank regression methods for
VFL poses unique challenges: (a) stringent privacy regulations preventing local site
data from being shared, and (b) fitting local regressions overlooks essential model-
ing aspects such as inter-variable correlations. In contrast HFL allows each site to
fit a comparable model independently. In this article, we presenta novel Bayesian
VFL framework for multivariate high-dimensional reduced-rank regression, coined as
BayesVFLReg, which enables precise coefficient estimation while safeguarding both
features and responses privacy. Participating sites employ a shared random sketching
matrix to compress local variables into privacy-preserving sketches. A central server
collects these sketches where Bayesian multivariate reduced-rank regression is done
using Gaussian scale mixture priors. For feature selection, we introduce a single-step
post-processing strategy based on mixture-model clustering of the absolute posterior
coefficient means to distinguish signal from noise per response variable.BayesVFLReg
1
arXiv:2609.22654v2  [stat.ML]  26 Sep 2026

is computationally scalable for large, high-dimensional datasets and facilitates efficient
variable selection. Theoretically, we establish sharp non-asymptotic bounds on the
posterior probability that the fitted density falls within a Hellinger ball centered at
the true data-generating density. Comparative simulation studies and real-world data
analyses show thatBayesVFLRegreliably identifies sparse feature effects, even under
feature correlation.
Keywords:Bayesian modeling; High-dimensional features; multivariate regression; vertical
federated learning; variable selection.
1 Introduction
Federated learning (FL) has sparked a paradigm shift in privacy-preserving and communication-
efficient analytics, empowering collaborative model training across multiple institutions with-
out direct data sharing. This innovation allows organizations to leverage distributed data
resources while maintaining strict privacy standards, making FL a cornerstone in sensitive
domains such as healthcare, finance, and multi-center research collaborations. FL is gen-
erally categorized into horizontal federated learning (HFL) and vertical federated learning
(VFL). In HFL, participating sites share identical sets of features but differ in their obser-
vations, facilitating conventional statistical aggregation strategies. In contrast, VFL deals
with sites that possess distinct feature sets for aligned subject observations. Within VFL,
there exist multiple sub-classifications; following [Wu et al., 2025]. In this article, we focus
on thePrecise VFLsetting, in which all observations are perfectly aligned across sites.
We consider inference on the parameters of a high-dimensional multivariate regression
model, which can be described as:
Y ⊤ i =X ⊤ i C+e ⊤ i , i∈ {1, . . . , n},(1)
whereX i is aP×1 vector of features for theith subject, andY i is aQ×1 vector representing
the response variables for theith subject. The regression coefficient matrixCis of sizeP×Q
and contains the parameters of interest. The noise vectore i accounts for residual variation,
and is assumed to follow an independentQ-variate normal distribution with mean zero and
a diagonal covariance structure, i.e.,e i | {σ2 1, ..., σ2 Q} iid ∼N Q(0,diag(σ 2 1, ..., σ2 Q)).
By aggregating over allnsubjects, the model can be rewritten in matrix form as:
Y=XC+E,(2)
whereYis an×Qmatrix with theith row given byY ⊤ i , andXis an×Pmatrix of
features with theith row corresponding toX ⊤ i . Similarly,Eis then×Qresidual matrix
with itsith row denoted bye ⊤ i .
A considerable amount of research has addressed the estimation of such regression mod-
els in the context ofhorizontal federated learning(HFL) [Yang et al., 2019]. In HFL, data
are distributed horizontally across multiple sites, meaning each site has a different subset of
independent subjects but each subject is observed across the same set ofPfeatures andQ
responses. This implies that for the model specified above, observations across sites remain
independent. Consequently, the model can be fitted locally at each site using its site-specific
2

data block, leading to local estimates of the parameters{C, σ 2 1, . . . , σ2 Q}. These local esti-
mates, though potentially noisy due to limited sample sizes per site, can be subsequently
transmitted to a central server, where they are aggregated to obtain final consensus esti-
mates of the regression parameters. This federated approach preserves both data privacy
(by not sharing raw data across sites) and allows for scalable analytical procedures across
decentralized and heterogeneous datasets.
In contrast, vertical federated learning (VFL) is still a relatively underexplored field, es-
pecially when compared to horizontal federated learning. This is largely due to the intrinsic
challenges of VFL: since features are distributed across different sites, no individual site can
access the entire set of features for any given data sample. This decentralized structure
complicates the process of fitting a single, unified model, as information about each sample
is distributed in a fragmented manner. To date, the majority of research on vertical feder-
ated learning (VFL) has emerged primarily within the machine learning community, with
a predominant focus on developing algorithmic solutions for model training and prediction
subject to privacy constraints [Liu et al., 2024]. In the statistical literature, investigations
under the VFL framework have been largely limited to simple linear and logistic regres-
sion models, with primary attention given to point estimation and hypothesis testing from a
frequentist standpoint. Notable studies have proposed methods for estimating model param-
eters and conducting statistical inference in these settings, often leveraging techniques such
as secure computation, cryptographic protocols, and homomorphic encryption to safeguard
data privacy [Gratton et al., 2018, Gasc´ on et al., 2017, Sanil et al., 2004, Chen et al., 2021,
Zhao et al., 2023]. Several studies have explored the application of high-dimensional ridge
regression models in the context of VFL. Yang et al. [2019] introduced a VFL algorithm
tailored for ridge regression; however, its application is restricted to settings involving only
two sites, and its reliance on gradient-based optimization methods may present efficiency
challenges. Subsequently, Liu et al. [2021] incorporated Yang’s VFL algorithm into a FL
framework designed for smart grids. Recent studies [Dai et al., 2022, Cai et al., 2022] have
emphasized that large-scale datasets and the computational overhead of homomorphic en-
cryption can considerably slow down the overall process for VFL participants. In response,
these works propose VFL algorithms for ridge regression that require only a single commu-
nication round to achieve the optimal solution, thereby eliminating the need for iterative
procedures. Although these approaches address point estimation, there is a notable lack of
methods todraw inference with uncertainty quantificationfor regression parameters within
VFL. In fact, approximating posterior distributions for regression parameters in the VFL
setting remains highly challenging due to the induced dependencies across feature effects lo-
cated at different sites. The joint likelihood function does not readily decompose across sites
as in HFL, thus hindering the use of standard distributed Bayesian computation strategies
and making scalable posterior inference difficult [Hassan et al., 2024].
1.1 Our Proposal and Contributions
To address the limitations inherent in joint parametric inference and privacy in vertical fed-
erated learning, we propose utilizingdata sketching[Ahfock et al., 2017, Dobriban and Liu,
2018, Guhaniyogi et al., 2025, Guhaniyogi and Scheffler, 2025] as a foundational aspect of our
framework. In this approach, each site multiplies its feature matrices by a random compres-
3

sion matrix, which is predetermined and shared among all participating sites before analysis
begins. This process yields a low-dimensional, sketched version of the original data at each
site. Once the sketched features are computed locally, only these sketched representations,
rather than the raw features, are sent to a central server. At the central server, a multi-
variate high-dimensional regression model, as described in equation (2), is then fitted using
the pooled sketched data from all sites. Our privacy guarantee in VFL is fundamentally
supported by an information-theoretic result: the random sketching transformation ensures
that, as the sample size increases, the mutual information between the original features and
the sketched data per feature per sample converges to zero [Zhou et al., 2009]. This im-
plies that, even with a moderately large sample size, the original feature data at any site
cannot be reconstructed or reliably inferred from the shared sketched features, which is a
key aspect of our approach. Consequently, this property provides a robust foundation for
information-theoretic privacy preservation during the collaborative learning process.
Our methodology employs a reduced-rank formulation for the coefficient matrixC, which
enables the joint modeling of multiple correlated response variables in high-dimensional
contexts while maintaining computational efficiency. To achieve adaptive shrinkage and
sparsity, we impose a global-local scale mixture of Gaussian priors on the elements ofC.
This prior naturally shrinks the coefficients of irrelevant features toward zero and promotes
sparsity across both the rows and columns of the coefficient matrix, thereby improving
interpretability and predictive performance. Importantly, our approach is fully Bayesian,
allowing for posterior inference not only on the regression coefficientsC, but also on the
error variancesσ 2 1, . . . , σ2 Q. This capability providescoherent uncertainty quantificationfor
all model parameters. We refer to the proposed approach asBayesVFLReg, a new approach
developed to fill the current gap inBayesian vertical federated learningmethods for high-
dimensional multivariate regression. Furthermore, unlike existing VFL methods for linear
regression, which often assume a single “active site” that houses all response variables for
the model, our framework supports a more flexible arrangement wherein response variables
can be distributed across multiple active sites, thereby enabling broader and more versatile
federated analyses in real-world multi-institutional settings.
A central, defining strength of our proposed VFL approach lies in its rigorous theoret-
ical foundation. Under justifiable assumptions, we prove that the posterior probability of
the fitted density concentrates around the Hellinger ball of the true density. This occurs
at a rate that closely mirrors the minimax optimal rate, seamlessly substituting traditional
sample size with the dimensions of the data sketches. Our framework provides definitive,
mathematical insights into how key model dynamics, specifically the number of predictor
coefficients, sample size, and true regression model sparsity, directly dictate the sketching
dimensions required to achieve optimal posterior concentration. The framework also iden-
tifies the exact, sufficient conditions required for both the sketching matrices and the true
regression coefficients to consistently ensure desirable and highly reliable performance. Cru-
cially, the literature on theoretically guaranteed uncertainty for Bayesian VFL is notably
scarce, making the rigorous proofs developed in this work an exceptionally vital and timely
contribution to the field.
Some clarifications are warranted. First, unlike differential privacy [Dwork and Roth,
2014, Guha and Reiter, 2025], which achieves probabilistic privacy guarantees by injecting
noise to obscure the influence of individual records, information theoretic privacy provides
4

unconditional protection, ensuring that data sketches disclose minimal information about
individuals, regardless of the capabilities of an adversary. Second, this work advances the
literature on data sketching. Earlier research has investigated sketching methods primarily
in the context of simple linear regression, emphasizing accurate coefficient estimation, and
has extended these approaches to ridge and lasso regression models, frequently analyzing
their statistical properties through leverage scores [Sarlos, 2006, Dobriban and Liu, 2018].
However, research on leveraging data sketching in high-dimensional Bayesian regression with
large sample sizes, where computational costs rapidly escalate and data sketching could
provide an effective solution, remains scarce. Exceptions are some recent studies that focus
exclusively on univariate high-dimensional regression [Geppert et al., 2017, Guhaniyogi et al.,
2025]. To the best of our knowledge, our approach is the first to develop an efficient Bayesian
computational algorithm for large-scale multivariate reduced-rank regression utilizing data
sketching, enabling accurate and uncertainty-aware inference for regression parameters in
this context.
The remainder of this paper is organized as follows. In Section 2, we introduce the
proposed vertical federated learning framework for high-dimensional multivariate regression
under a principled Bayesian approach. Section 3 demonstrates the effectiveness of data
sketching through empirical studies, highlighting how our framework ensures accurate in-
ference of regression parameters under vertical federated setting. In Section 4, we apply
our method to real data to illustrate its practical utility. Section 5 develops the theoretical
framework including assumptions and the main posterior concentration results. Finally, Sec-
tion 6 concludes the paper with a discussion of our findings and potential avenues for future
research. Appendix offers proofs of the theoretical results presented in Section 5.
2 Vertical Federated Learning for Multivariate Regres-
sion
LetN={1, . . . , n}represent the set ofnsample identifiers. Suppose there areKdistinct
participating sites, each of which securely holds unique subsets of response and feature data
corresponding to all sample IDs inN. In this context, suppose there areQresponse variables
andPfeature variables in total. Thekth site holdsQ k response variables andP k feature
variables, fork= 1, . . . , K, wherePK k=1 Qk =Qand PK k=1 Pk =P.
We allow flexibility in the storage at each site: a site may contain only responses (Pk = 0),
only features (Qk = 0), or both, provided that at least one variable type is present at the site,
i.e., max(Pk, Qk)>0. This design permits realistic configurations, such as sites specializing
in either response or feature data. LetY (k) ∈R n×Qk denote the matrix of theQ k response
variables for all sample IDs at thekth site, and letX (k) ∈R n×Pk denote the matrix ofP k
feature variables for all sample IDs at thekth site. Importantly, the raw data at each site
isprivacy-protected. This implies that the data must remain local and cannot be exchanged
with other sites or transmitted to a central server.
In the context of multivariate reduced-rank regression, our objective is to incorporate
all response and feature variables across sites to estimate regression coefficients and identify
key features corresponding to each response. However, independent analysis at each site
5

is not feasible due to the inherent limitations: many sites may exclusively contain either
response or feature data, but not both. Furthermore, performing regression analysis using
only a subset of features available at a given site neglects the inter-feature correlations and
can substantially bias the regression coefficients. This situation exemplifies the challenges
of vertical federated learning (VFL) paradigm, which is notably more challenging than hor-
izontal federated learning. In horizontal federated learning, each site possesses data for a
distinct subset of samples, but includes all features and responses for those samples. As a
result, the full model can be distributed across sites, and local inferences made at each site
are relatively straightforward, typically offering noisy approximations to the global poste-
rior distribution of regression parameters. Existing approaches leverage techniques such as
secure computation, cryptographic protocols, and homomorphic encryption to protect data
privacy [Gratton et al., 2018, Gasc´ on et al., 2017, Sanil et al., 2004, Chen et al., 2021, Zhao
et al., 2023] in VFL, but do not account for parametric uncertainty in high-dimensional
linear regression. In what follows, we develop a two-stage VFL framework to address these
challenges, with the overall procedure depicted in Figure 1.
Figure 1: VFL for Multivariate Regression using Federated Sketch Construction
2.1 Step 1: Federated Sketch Construction with Random Matri-
ces in Each Site
We propose constructing a random matrixΦof dimensionm×n, with each entry drawn
i.i.d. fromN(0,1/n) andm << n. This random matrix is shared across allKsites. Each
sitekperforms alocal and private computation, creating a small,m-dimensional sketch of
its own data:
•Local Sketched Responses:Y (k) Φ =ΦY (k)
6

•Local Sketched Features:X (k) Φ =ΦX (k)
Theselocal sketchesare then securely transmitted to a central server. Theglobal sketchis
reconstructed via a simple, communication-efficient summation:
•Global Sketched Responses:Y Φ = [Y (1) Φ :· · ·:Y(K) Φ ]∈R m×Q
•Global Sketched Features:X Φ = [X (1) Φ :· · ·:X(K) Φ ]∈R m×P
A fundamental strength of our federated sketching framework lies in its inherent privacy
protection. The random projection mechanism at its core ensures that the original data
remain secure, providing rigorous information-theoretic privacy guarantees. Specifically,
when a central server receives a local sketch, such asX (k) Φ =ΦX (k) andY (k) Φ =ΦY (k),
it encounters a highly underdetermined linear system. Because the sketch dimensionmis
much smaller than the original data dimensionn, it is not possible to uniquely reconstruct
X (k) orY (k) from their respective sketches.
This privacy property is mathematically formalized via information theory. The mutual
information between the sketch and the original data, denotedI(X (k) Φ ,X (k)), quantifies the
amount of information the sketch reveals. It can be established that the supremum of the
normalized mutual information,
I(X (k) Φ ,X (k))
nPk , is bounded above byO
 m
n

[Zhou et al., 2008].
An analogous result holds for the sketch of the responses:
I(Y (k) Φ ,Y (k))
nQk is also bounded above by
O
 m
n

. Notably, this guarantee persists even in the adversarial scenario where the sketching
matrixΦis fully known to the server. As the dataset sizengrows, these upper bounds
approach zero, demonstrating that in the limit asn→ ∞, the information contained in the
sketch about the original dataset becomes negligible. In effect, the sketched data becomes
as anonymous as a random sample independent of the original data.
In real-world federated settings, the privacy advantages are often even more pronounced.
Conventionally, only the global sketch (such asX (k) Φ ) is shared, and the random sketching
matrixΦmay remain confidential. This added layer of protection dramatically increases
the difficulty of reconstructing the original data, surpassing even the theoretical guarantees
[Guhaniyogi et al., 2025, Guhaniyogi and Scheffler, 2025]. It is important to note that this
form of privacy, rooted in the principles of information theory and computational hardness,
is fundamentally distinct from statistical privacy guarantees such as those provided byϵ-
differential privacy [Dwork and Roth, 2014]. Whereasϵ-differential privacy constrains the
probability of distinguishing individual samples, our framework ensures that the sketches in-
trinsically reveal minimal information about the original data, irrespective of computational
resources or adversarial knowledge.
2.2 Step 2: Fitting Reduced-Rank Multivariate Regression in the
Central Server
At the central server, we fit the multivariate regression model with the global sketches, given
by,
Y Φ =X ΦC+E,(3)
7

whereE= [e ⊤ 1 :. . .:e⊤ m]⊤ denotes them×Qdimensional matrix of errors, withe 1, ...,em i.i.d. ∼
NQ(0, diag(σ2 1, ..., σ2 Q)).
Model 3 closely resembles aΦ-transformed version of the original statistical model, but
with a fundamental distinction. Specifically, we donotapply theΦtransformation to
the error matrix. This design choice is rooted in insights from random matrix theory. In
particular, it has been shown that the deviation
ΦΦ⊤ −I  can be bounded by ˜Cp m n with
high probability, where ˜Cis a constant andm≪n[Vershynin, 2010]. Consequently, the
Φ-transformed errors exhibit behavior that is approximately orthogonal, preserving essential
statistical properties such as independence and Gaussianity in the sketches. By leaving the
error matrix untransformed, we avoid sharing theΦmatrix with the central server, as well
as gaining in computation when the sample sizenis large.
We assume that the matrixCpossesses a low-rank structure, specifically rank(C) =
R <min(P, Q). This assumption enables us to expressCas the product of two matrices:
C=BA ⊤, withB∈R P×R andA∈R Q×R. This factorization is referred to as the reduced-
rank representation and is commonly employed in multivariate statistical modeling [Reinsel
and Velu, 1998, Chen and Huang, 2012] to capture latent structure and to prevent overfitting
in high-dimensional regression settings.
Driven by practical applications in multivariate regression, especially those involving a
large number of features and a comparatively moderate number of responses, we focus on
the frequent scenario whereQ < P. Although it is possible to place priors directly on
the rankRto facilitate adaptive inference on the latent space, we instead pursue a more
flexible approach: we setR=Q, such that bothAandBare of full column rank. To
mitigate overfitting and limit the impact of irrelevant columns, we place continuous shrinkage
priors on the columns ofB. This approach is analogous to widely used Bayesian multi-way
regression methods, where explicit rank selection in low-rank matrix or tensor decompositions
is frequently substituted with the choice of a relatively large rank combined with shrinkage
estimation [Guha and Rodriguez, 2021, Guhaniyogi and Spencer, 2021].
More specifically, we adopt a global-local continuous shrinkage prior framework (e.g.,
Carvalho et al. [2010], Caron and Doucet [2008]), realized as global-local scale mixtures of
Gaussians [Polson and Scott, 2010]. Under this arrangement, the (p, q)th entryb p,q of the
matrixBis modeled as follows:
bp,q |λ p,q, τq ∼ N

0, λ2 p,qτ 2 q  , λ p,q ∼f 1, τ q ∼f 2,(4)
whereτ q is a global shrinkage parameter for theqth column, andλ p,q is a local shrinkage
parameter for thepth entry of theqth column. The densitiesf 1 andf 2 are supported on
R, providing flexibility in prior specification. This global-local shrinkage setup parallels ap-
proaches commonly used in high-dimensional sparse regression, with the shrinkage inducing
effective sparsity and controlling model complexity.
Different choices forf 1 andf 2 result in distinct forms of shrinkage priors. While our
framework can accommodate any global-local normal mixture prior, for demonstration and
empirical evaluation, we focus on the horseshoe prior [Carvalho et al., 2010], which is obtained
by choosing bothf 1 andf 2 as independent Half-Cauchy distributions. The horseshoe prior is
well-known for its ability to strongly shrink irrelevant coefficients while retaining important
signals. Each entry ofAis assigned a N(0,1) prior distribution. Furthermore, for the
8

variance parametersσ 2 q , we assign independent Jeffreys priors, specified asπ(σ 2 1)∝1/σ 2 q .
This noninformative prior supports robust estimation of variance components within our
model.
2.2.1 Posterior Approximation
With prior distributions onBandAset as above, the posterior computation using a blocked
Metropolis-within-Gibbs algorithm cycles through updating the full conditional distributions
as expressed in Algorithm 1.
Algorithm 1Metropolis-within-Gibbs Algorithm
InitializeB (0),A (0),{σ 2,(0) q }Q q=1,{λ (0) p,q}P,Q p,q=1,{τ (0) q }Q q=1
fort= 1 toT samps do
Step 1:DrawB (t) fromB|X Φ,Y Φ,A (t−1),{σ 2,(t−1) q }Q q=1,{λ (t−1) p,q }P,Q p,q=1,{τ (t−1) q }Q q=1
Step 2:DrawA (t) fromA|X Φ,Y Φ,B (t),{σ 2,(t−1) q }Q q=1
Step 3:Draw{σ 2,(t) q }Q q=1 fromσ 2 q |X Φ,Y Φ,A (t),B(t)
Step 4:Draw{λ (t) p,q}P,Q p,q=1 fromλ p,q |τ (t−1) q ,B (t) and{τ (t) q }Q q=1 fromτ q | {λ(t) p,q}P p=1,B (t)
end for
Explicit expressions for steps 1-4 for the horseshoe shrinkage prior are available in the
supplementary material. Although updating 2-4 is computationally straightforward, up-
dating 1 faces computational challenges. To see this, letβ=vec(B) ⊤ ∈R P Q×1,Λ=
diag(λ2 11τ 2 1 , ..., λ2 1Qτ 2 Q, ..., λ2 P Qτ 2 Q)∈R P Q×P Q + ,y Φ = vec(Y ⊤ Φ)∈R mQ×1,Σ= diag(σ 2 1, ..., σ2 q )∈
RQ×Q + and ˜Σ= diag(Σ, ...,Σ)∈R mQ×mQ + . The full conditional distribution ofβis given by,
β|X Φ,Y Φ,A,{σ 2 q }Q q=1,{λ p,q}P,Q p,q=1,{τ q}Q q=1 ∼N P Q(Ω−1 B ˜X ⊤ ˜Y,Ω −1 B ) (5)
where ˜Y Φ = ˜Σ −1/2 Y Φ, ˜X Φ = ˜Σ −1/2 (X Φ ⊗A),Ω B = ( ˜X ⊤ Φ ˜X Φ +Λ −1).
Given that in most applicationsP >> m, performing the first step can be computation-
ally intensive, with complexityO((P Q) 3). To address this, we take an approach adapted
from Guha and Rodriguez [2020], and implement the following algorithm:
Algorithm 2Samplingβ
Step 1:Sampleu∼N(0,Λ),δ∼N(0, I mQ)
Step 2:Setv= ˜X Φu+δ
Step 3:Solve ( ˜X ΦΛ ˜X ⊤ Φ +I mq)w= ( ˜Y Φ −v) to obtainw
Step 4:Setβ=u+Λ ˜X ⊤ Φw
This reduces the complexity fromO(P 3Q3) toO(Q 3min(m3, P)), resulting in linear scal-
ing with the number of featuresPand cubic scaling with respect tom. Sincem≪n, this
demonstrates that the method is highly scalable even when bothnandPare large.
9

2.2.2 Post-Processing and Variable Selection
It is important to note that, although the shrinkage prior pulls unimportant coefficients to-
ward zero, it does not set them exactly to zero. To identify the most relevant variables, we
apply a post-processing procedure based on the method proposed in Guha and Rodriguez
[2021], as described below. This approach uses Gaussian clustering to divide the predic-
tors into two groups: those associated with zero and those with non-zero coefficients. The
procedure is as follows:
Algorithm 3Feature Classification Algorithm
Step 1:Obtain a posterior or mean estimate ofC, call this bC
Step 2:Let ˜Cbe the absolute value applied to each element of bC
Step 3:Cluster the rows of ˜Cinto two groups using a two-component mixture of Gaussian
distributions
Step 4:Use the generated probability (p j,j= 1, . . . , p) that a given feature is allocated
to the mixture component with the lowest mean
Step 5:For ˜α= 0.05, use the above probabilities to classify if the given feature is
non-zero, i.e.,p j <˜α⇒featurejis classified as non-zero
The parameter ˜αserves as a model selection threshold. In this work, we set ˜α= 0.05 to
ensure a low probability of misclassifying a variable as non-zero, that is, we require at least
95% confidence that a selected variable truly differs from zero.
3 Simulation
This section evaluates the efficacy of our proposedBayesVFLRegframework in estimating
the coefficient matrixCfrom model (3), leveraging induced reduced-rank priors. We present
two different simulation scenarios.Simulation 1examines the performance ofBayesVFLReg
on simulated data from Model (2) withn= 500,P= 300, andQ= 5. Here, we analyze our
approach alongside Model (1) applied to a centralized model that makes use of unsketched
global data. This allows for the comparison of the posterior distributions ofCunder varying
privacy levels and sparsity degrees. These results provide insight into how theBayesVFLReg
approach stacks up against the “gold standard” centralized setting, where all data are ob-
served on a central server, revealing the impact of privacy constraints and model sparsity on
estimation accuracy. Additionally, we assess computational efficiency of theBayesVFLReg
approach.
Simulation 2examines larger-scale data (n= 1,000,P= 1,000,Q= 5), where direct
benchmarking with full Bayesian computation of Model (1) is computationally infeasible. In
this context, we evaluate theBayesVFLRegmethod against a state-of-the-art federated com-
petitor, distributed ridge regression (dRidge) [Gratton et al., 2018], as well as two efficient
non-federated alternatives that operate on data centrally stored but offer greater compu-
tational tractability compared to full Bayesian modeling of Model (1) for estimatingC.
Specifically, one approach follows a frequentist paradigm [Chen and Huang, 2012], while the
other employs a variational Bayesian framework [Ruffieux et al., 2017]. This comprehensive
10

comparison enables us to rigorously assess both the accuracy and computational efficiency
ofBayesVFLReg, relative to leading federated algorithms and conventional non-federated
strategies for high-dimensional multivariate regression.
3.1 Simulation 1: Effect of Privacy
Simulation 1is designed to assess the performance ofBayesVFLRegacross different levels
of sparsity and privacy. We simulaten= 500 data observations from theQ-variate high-
dimensional regression model (2), withQ= 5, P= 300 andσ h = 1 for allh. Each
P-dimensional feature vectorX i is simulated from aN(0,Σ), whereΣ= (1−ρ)I P +ρJ P ,
andJ P is a matrix of sizeP×Pwith all entries equal to 1. We fixρ= 0.5 to ensure
moderate correlation between all features.
The coefficient matrixC=BA ⊤ is constructed by first simulating the entries of the
matrixAfromN(0,1), and subsequently constructingBsuch that exactlysrows ofBare
non-zero (with each non-zero entry sampled from N(0,1)). The simulation study variess
across 10,30, and 50 to represent different degrees of sparsity. The constructedC, together
with the simulated feature vectorsX i, is used to simulate the response matrixY.
Our central objective is to study the influence of privacy and sparsity on the accuracy of
the proposedBayesVFLRegframework. Privacy protection is tuned by varying the sketch
dimension, settingm= 50,100,250. This results in normalized mutual information be-
tweenXandX Φ (and betweenYandY Φ) approximately 0.0005(0.043), 0.001(0.087), and
0.003(0.217) bits, respectively, as calculated under the linear Gaussian model [Cover and
Thomas, 2006]. These values indicate a high degree of privacy in each simulation setting. In
this context, bits quantify the adversary’s ability to infer the true data: each bit of leaked
information halves the set of feasible guesses. Consequently, releasing a sketch that leaks
kbits of information reduces the adversary’s plausible guesses by a factor of 2 k [Cover and
Thomas, 2006]. We compare our approach to the “gold standard” Bayesian multivariate
reduced rank regression fit on the unsketched data in a central server, referred to as the
centralized model, repeating the analysis over 50 simulated datasets to ensure robustness.
We evaluate inferential performance using
MSE =∥vec( bC)−vec(C)∥ 2 2/qp,MSE nz =∥vec( bC nz)−vec(C nz)∥2 2/qs,(6)
where bCis the posterior mean estimate of the entire coefficient matrixC, and bC nz represents
the posterior mean for the true non-zero entries (denoted byC nz).
To further evaluate the accuracy of the estimated posterior distributions of the coeffi-
cient entries, we use the centralized model as the baseline and introduce a metric based on
the Hellinger distance. This metric quantifies how closely the posterior for each coefficient
obtained via theBayesVFLRegapproach,π m(cjh |Y ϕ,X ϕ), approximates the centralized
posteriorπ(c jh |Y,X):
Accuracyj,h,m = 1− 1 2 Z C q πm(cjh |Y ϕ,X ϕ)− q π(cjh |Y,X) 2 dcjh (7)
This accuracy metric, Accuracyj,h,m, ranges from 0 to 1, with values near 1 indicating strong
agreement between theBayesVFLRegand centralized posteriors. To provide more detailed
11

insights, we summarize accuracy separately for zero and non-zero coefficients as follows:
Accuracym,nz = 1 sQ X j,h:cjh ̸=0 Accuracyj,h,m,
Accuracym,z = 1 (P−s)Q X j,h:cjh =0 Accuracyj,h,m.
Since the posterior distribution ofc jh cannot be computed in closed form, we approximate
bothπ m andπnumerically. Posterior samples ofBandAare used to construct samples
ofC; subsequently, we employ the Bernstein-von Mises (Bayesian Central Limit Theorem)
approximation as follows:
1. CollectBposterior draws ofc (m) ij andc ij fromc (m) ij |Y ϕ,X ϕ andc ij |Y,Xrespectively;
2. Estimate the posterior mean and variances; ˜µm = 1 B PB b=1 c(m,b) ij ,˜σ2 m = 1 B−1 PB b=1(c(m,b) ij −
˜µm)2,˜µ= 1 B PB b=1 c(b) ij ,˜σ2 = 1 B−1 PB b=1(c(b) ij −˜µ)2;
3. Then given a random grid with valuesc (f) ij forf= 1,2, . . . , F,
Accuracyj,h,m ≈1− 1 2F
FX
f=1
q
N(c (f) ij |˜µm,˜σ2 m)− q N(c (f) ij |˜µ,˜σ2) 2 (8)
This simulation also illustrates the computational efficiency gained by incorporating the
global sketch. Let ESS m be the total effective sample size ofC, obtained by summing the
effective sample sizes across all coefficients when usingΦwith rank(Φ) =mto generate
5,000 posterior samples (from 5 independent chains of 1,000 draws each with a burn-in of
200) inT m seconds.
Computational Efficiencym = log2 ESSm/Tm,(9)
where ESS m across features is computed using thecodapackage inR. Computational Effi-
ciency is also computed for the non-federated posterior. All metrics are reported as averages
across the 50 replicated datasets in each scenario.
3.1.1 Simulation 1 Results
We fit the models using MCMC chains with 5,000 draws, discarding the first 2,000 samples
as burn-in and retaining the remaining 3,000 draws for posterior analysis. Figure 2 depicts
the MSE and MSE nz, respectively. Figure 2 shows that, as privacy level decreases (with
the increase of sketching dimensionm), both MSE and MSE nz improve, indicating higher
inferential accuracy. Furthermore, performance depends critically on the ratios/m: as this
ratio becomes smaller, theBayesVFLRegmodel’s accuracy approaches that of the model fit
to centralized data. This finding highlights that higher levels of sparsity allow for stronger
privacy protection while maintaining nearly similar inference as that from the centralized
model.
12

Figure 2: Figure shows a summary of the MSE (blue) and MSE nz (red) across the 50
replicates. The dots denote mean MSE with intervals around the mean showing standard
errors over 50 replications. As privacy decreases (largerm), accuracy improves. At higher-
degree of sparsity (smallers), more privacy can be guaranteed while achieving competitive
performance relative to the uncompressed model.
Table 1 depicts both the accuracy and the computational efficiency at different privacy
levels (m= 50,100,250), and degrees of sparsity. Table 1 reports Accuracy m,nz, Accuracym,z,
and computational efficiency across privacy levels and sparsity settings. TheBayesVFLReg
posteriorπ m(C|Y Φ,X Φ) closely approximates the centralized posteriorπ(C|Y,X), with
average accuracies near 1 in all scenarios. The computational efficiency metric shows that
higher privacy (smallerm) yields substantially more efficient sampling than the full posterior,
a benefit that becomes increasingly important asPgrows. The computational efficiency for
BayesVFLRegis found to be a few folds higher than the gold standard centralized posterior.
13

s= 10 s= 30 s= 50
Avg. Accuracy nz
m= 50 0.995 0.997 0.998
m= 100 0.994 0.997 0.998
m= 250 0.994 0.996 0.997
Avg. Accuracy z
m= 50 0.997 0.997 0.998
m= 100 0.998 0.998 0.999
m= 250 0.999 0.999 0.999
Comp. Efficiency
m= 50 9.880 9.846 9.917
m= 100 7.748 7.463 7.680
m= 250 5.562 4.540 5.542
centralized 3.261 3.228 2.932
Table 1: The top six rows depict the measure of accuracy of estimating the full posterior
ofCfrom compressed data, as expressed in 8. Results are disaggregated by zero and non-
zero features, varying sparsity levels, and different values ofm= 50,100,250 representing
differing privacy levels. This metric is averaged over 50 replicates; values closer to the
upper bound of 1 indicate better posterior estimates with compressed data. These results
demonstrate that the compressed approach closely approximates the centralized posterior.
The bottom 4 rows present computational efficiency (see 9), also averaged over 50 replicates,
illustrating that data compression substantially improves computational performance relative
to uncompressed methods.
3.2 Simulation 2: Global Data Sketch versus Competitors
InSimulation 2, we simulate our data usingn= 1000,P= 1000 andQ= 5. We follow the
same data generation process as outlined inSimulation 1. However, we generate features
by varying correlations among features (ρ) to assess performance with changing feature
correlations. The scenarios are as follows:
Scenario 1:Independent features withρ= 0.
Scenario 2:Moderately correlated features withρ= 0.5.
Scenario 3:Strongly correlated features withρ= 0.7.
BothAandBare generated as inSimulation 1, with varying levels of sparsity set at
s= 10,30,50. Once simulated, the data are randomly partitioned acrossK= 3 separate
sites, under the assumption that no communication occurs between sites. This simulation
procedure is replicated 50 times for each combination of correlation scenario and sparsity
level.
We choosem= 200 to keep the normalized mutual information below 0.0015 bits at
each site betweenXandX Φ forScenarios 1, 2, & 3. To assess the impact of sketching on
posterior estimation ofC, we implement three competing estimators. As aBayesVFLReg
competitor, we usedRidge, a distributed ridge regression approach proposed by Gratton
et al. [2018], which we fit separately to each response due to its univariate regression design.
For non-VFL methods operating on the full, centralized data, we implement the variational
Bayes approachlocus[Ruffieux et al., 2017], and the frequentist sparse reduced-rank re-
gression method,srrr[Chen and Huang, 2012]. In the absence of a centralized posterior
gold standard,locusandsrrrserve as benchmarks for non-VFL performance, enabling a
14

comparative assessment withBayesVFLReg.
We evaluate inferential accuracy using the MSE and MSEnz metrics defined as inSimu-
lation 1. We also examine the coverage of 95% credible or confidence intervals, both overall
and for the non-zero coefficients (coverage nz). FordRidge, we implement bootstrap-based
repeated sampling for uncertainty quantification, which incurs substantially higher compu-
tational cost. For the frequentistsrrrcompetitor, we do not implement repeated sampling
and therefore do not report uncertainty measures forsrrr. Finally, we apply the variable
selection procedures described in Algorithm 3 and compute the false discovery rate (FDR)
for each method to evaluate its ability to identify important features.
3.2.1 Simulation 2 Results
Figure 3 compares the MSE results for all zero and non-zero values ofC. We observe that the
two VFL methods,BayesVFLReganddRidge, achieve MSE performance comparable to the
non-VFL competitors when correlation is low. As correlation among covariates increases, the
BayesVFLRegmethod increasingly outperformslocus, while being comparable to the other
competing methods, particularly for estimating nonzero coefficients (Figure 3). In high-
correlation, low-sparsity settings,BayesVFLRegprovides notably more accurate estimates
of the non-zero coefficients than the other VFL competitordRidge.
Figure 4 presents coverage results across different correlation scenarios and sparsity levels.
Overall, all methods achieve coverage close to one. However, consistent with prior literature
on high-dimensional regression [Guhaniyogi et al., 2025], all methods exhibit under-coverage
when estimating non-zero coefficients. Notably,BayesVFLRegprovides substantially better
coveragenz for non-zero coefficients compared todRidge, which shows pronounced under-
coverage and much shorter 95% credible intervals. The centralized methodlocus, which uses
variational approximation, also greatly underestimates the coverage for non-zero coefficients,
yielding the narrowest intervals. For all methods, under-coverage of non-zero coefficients
becomes more pronounced as correlation increases and sparsity decreases.
Scenario 1 Scenario 2 Scenario 3
s= 10 s= 30 s= 50 s= 10 s= 30 s= 50 s= 10 s= 30 s= 50
BayesVFLReg 0.004 0.037 0.063 0.074 0.117 0.159 0.132 0.079 0.202
dRidge 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
locus 0.789 0.561 0.435 0.797 0.575 0.464 0.804 0.586 0.471
srrr 0.349 0.241 0.134 0.391 0.343 0.252 0.316 0.288 0.271
Table 2: Table reports theaverage false discovery rate (FDR). Given ˜α= 0.05, this
value should be close to 0.05. WhiledRidgesuccessfully separates non-zero from zero coef-
ficients, as indicated by the coverage, it struggles to accurately estimate their magnitude.
Table 2 depicts the FDR of the post processing procedure to identify important features.
BayesVFLRegoutperforms each method in terms of FDR exceptdRidge, which appears
to be the best performer. Taken together, these results indicate thatdRidgeis effective
at separating zero and non-zero features (very low FDR) but provides inferior uncertainty
quantification, severely underestimating uncertainty of non-zero effects. TheBayesVFLReg,
15

Figure 3: Figure depicts the MSE (blue) and MSE nz (red) of the four respective mod-
els;BayesVFLReg,dRidge,locusandsrrron the log scale. The points depict the average
log(MSE) or log(MSE nz) across replicates while the bars depict a 95% interval of the repli-
cates. It can be observed that, as the correlation increases, the data sketching approach
exhibits progressively better comparative performance.
in contrast, delivers a more favorable trade-off: it achieves competitive MSE, higher coverage
of non-zero coefficients, and reasonably low FDR across all sparsity and correlation scenarios,
making it the most reliable option in settings with highly correlated, predominantly null
features.
16

Figure 4: Figure displays average coverage (blue) and average coverage nz (red) as bars,
along with points denoting the average interval width under each simulation case. This
demonstrates thatBayesVFLRegachieves superior overall coverage; however, its interval
widths are larger than those of the other two methods, which, in turn, exhibit notably
poorer performance for coverage nz.
17

4 Study of Neuroimaging Data on Aging
We apply the Bayesian VFL Regression (BayesVFLReg) to multi-modal human neuroimag-
ing data collected first-hand by co-author Dr. Bernard, at the Lifespan Cognitive and Mo-
tor Neuroimaging Laboratory at Texas A&M University. The original study recruited 138
healthy adults living independently aged 35 to 86 years. After excluding participants due
to incomplete or noisy data, the final sample for our analysis consisted of 126 individuals
(mean age: 57 years; 54% female). The participants underwent structural and resting-state
magnetic resonance imaging (MRI), and data preprocessing was carried out according to
Hicks et al. [2023] and Ballard et al. [2022]. Following the network definitions of Jackson
and Bernard [2023], an initial set of 75 regions of interest (ROIs) were defined based on 6 key
networks: the default mode, frontal-parietal, control, emotion, motor, and cerebellar-basal
ganglia. After excluding 6 ROIs for alignment with structural data, the final analysis used
a set of 69 cortical and subcortical ROIs.
For each participant, a 69×69 correlation matrix was generated by cross-correlating
the time series extracted from 69 regions of interest (ROIs). This analysis was performed
in the CONN toolbox (version 21a) [Whitfield-Gabrieli and Nieto-Castanon, 2012]. The
upper triangle of each matrix was then vectorized, resulting in 2,346 connectivity predic-
tors for each subject. In addition, participants completed several behavioral measures:
the Montreal Cognitive Assessment (MoCA) as a global cognitive screening tool; the Pur-
due Pegboard task, yielding bi-manual and unilateral dexterity scores (Pegboard.Both,
Avg.Right,Avg.Left), a grip strength test, summarized as average left and right hand
strength (Avg.Left,Avg.Right), and a Digit Symbol Coding task (Digit.Symbol.Coding)
measuring processing speed, attention, and psychomotor efficiency. Collectively, these mea-
sures provide a cognitive-motor profile that serve as a behavioral basis for examining indi-
vidual variations in functional connectivity.
Under a vertical federated learning framework, we assume that the dataset was vertically
partitioned across two secure, independent sites: one hosting the MRI imaging data and the
other holding the corresponding cognitive and motor test results for the same participant
cohort. In compliance with data privacy protocols, raw data was not exchanged between the
sites.
Consistent with a large body of neuroscientific literature, we hypothesized a sparse rela-
tionship between functional brain connectivity and behavior [Varoquaux and Craddock, 2013,
Smith et al., 2009]. This implies that while the number of potential predictors (i.e., network
edges) is large, a small subset of these connections should be meaningfully associated with
participants’ cognitive and motor abilities. In the absence of ground-truth for the regression
coefficient matrix (C) for real-world data, we evaluate our proposedBayesVFLRegmethod
by benchmarking it against the competitors, distributed ridge regression (dRidge) [Gratton
et al., 2018],locus[Ruffieux et al., 2017], and sparse reduced rank regression (srrr) [Chen
and Huang, 2012]. Our evaluation is designed to assess the model’s predictive accuracy. To
compare how well each model fit the out-of-sample behavioral data (Y), we compute the
ratio of their respective Mean Squared Errors (MSE):
MSEY = ∥vec(Y)−vec( bCX)∥ 2
∥vec(Y)−vec( eCX)|| 2
18

Where eCrepresents the estimated coefficient matrix of the competitor and bCis the posterior
mean fromBayesVFLReg. This ratio directly measures the predictive accuracy of our model
relative to the competitors as a benchmark for each choice ofm. A value less than one
indicates a superior predictive fit forBayesVFLReg. We present these results form∈
{20,30,50,75,100}in Figure 5.
Figure 5: Shows relative predictive performance, measured as the ratio of the Mean Squared
Error (MSE Y ) ofBayesVFLRegto that of each respective competitor. The horizontal ref-
erence line at 1.0 indicates performance parity with each competitor; values below this line
demonstrate thatBayesVFLRegoutperforms the competitor.
Based on the results presented in Figure 5,m= 50 is selected for subsequent post-
processing. This value is chosen as yields a near-minimal predictive Mean Squared Error
(MSEY ) comparatively across competitors.
Our analysis of 2,346 potential network connections identified a key subset of 60 links
that significantly influenced participants’ cognitive and motor functions, these 60 links are
depicted within Figure 6. Across the set of significant ROI-ROI correlations, a consistent
pattern emerged in large-scale networks that plausibly underlie both cognitive and motor
outcomes. Many effects involved frontoparietal and default-mode nodes, including the left
inferior parietal lobule, lateral parietal cortex, posterior cingulate/retrosplenial regions, and
mesial prefrontal cortex. These regions are central to multimodal integration, attention,
episodic memory, and higher-order cognitive control, suggesting that altered coupling within
and between parietal and midline default-mode structures is associated with patients’ cogni-
tive performance. Parahippocampal connections further implicate medial temporal-default-
mode circuitry, consistent with effects on memory and global cognition.
A second prominent theme was the involvement of cortico-striato-motor loops. The
superior ventral striatum, dorsal caudate, and ventral/dorsal rostral putamen appeared fre-
quently, with significant correlations to cingulate (medial, supragenual, dorsal anterior),
19

(a) Brain Images with Highlighted
ROIs
 (b) Significant brain connections
Figure 6: The significant ROI-ROI correlations on the participants’ cognitive and motor
functions are depicted here. Figure (6a) depicts the brain highlighting the ROIs that were
found among the 60 significant links. Figure (6b) illustrates the significant ROI-ROI corre-
lations with the edge width depicting the absolute strength of the relationship between the
correlation and the cognitive and motor functions of the participants found by taking the
row means of the posterior mean ofC. A full list of significant ROI with their shorthand
mappings can be found in Table 3 from the Appendix.
anterior insula, mesial prefrontal cortex, and multiple premotor and primary sensorimotor
ROIs (e.g., left lateral premotor cortex, dorsolateral premotor cortex, primary sensorimotor
cortex). This pattern is characteristic of basal ganglia circuits supporting motor control,
action selection, and reward-based decision-making, and aligns well with the observed rela-
tionships to motor measures such as pegboard performance. ROIs that recur across many
significant edges include the left dorsal caudate, left ventral/dorsal rostral putamen, right
superior ventral striatum, medial/dorsal anterior cingulate cortex, left lateral/dorsolateral
premotor cortex, inferior/lateral parietal cortex, and posterior/retrosplenial cingulate, high-
lighting these regions as key hubs where connectivity differences are most strongly linked to
patients’ cognitive and motor abilities.
5 Theoretical Guarantees for BayesVFLReg
5.1 Motivation and Overview
This section establishes theoretical gurantee forBayesVFLRegframework described in Sec-
tion 2. For algebraic simplicity, we setσ 2 1 =· · ·=σ2 Q and set them at 1, without loss of
generality. While Section 2 performs full posterior computation using the standard posterior,
our theoretical analysis, however, is conducted under theα-fractional posterior framework
20

withα∈(0,1), following popular approaches [Chakraborty et al., 2020]. The adoption of
the fractional posterior is primarily a technical convenience: it requires only a prior mass
condition on Kullback-Leibler (KL) neighborhoods of the truth to establish posterior concen-
tration, whereas the standard posterior additionally requires the construction of sieves and
exponentially consistent test functions, which are difficult to verify for heavy-tailed shrinkage
priors. In this section, we further show how convergence ofα-fractional posterior to the full
posterior whenα→1. Consequently, any concentration result established for the fractional
posterior atα∈(0,1) carries over to the standard posterior used inBayesVFLReg.
5.2 Notations and Framework
5.2.1 Divergence Measures
We collect here the divergence measures used in the theoretical analysis. For two probability
densitiespandqdefined with respect to a common dominating measureµ:
•Hellinger distance:h 2(p, q) = R √p− √q 2 dµ.
•Total Variation distance:T V(p, q) =
R

p−q|dµ.
•Kullback–Leibler (KL) divergence:KL(p, q) =
R
plog(p/q)dµ.
•R´ enyi divergence(of orderα∈(0,1)):D α(p, q) = 1 α−1 log R pαq1−α dµ.
•α-affinity:A α(p, q) =
R
pαq1−α dµ=e −(1−α)Dα(p,q).
Whenα= 1/2,A 1/2(p, q) coincides with the Hellinger affinity. These divergences
satisfy the equivalence relations
D1/2(p, q)≥2h 2(p, q), α β · 1−β 1−α Dβ ≤D α ≤D β,0< α≤β <1.
Matrices are denoted by bold uppercase letters;∥ · ∥F and∥ · ∥2 denote the Frobenius andl 2
norms respectively;λ max(H) denotes the largest eigenvalue of a square matrixH.
5.2.2 Data Generating Model
Recall from Section 2 that the true data-generating model is
Y=XC ∗ +E,e i iid ∼ NQ(0,I Q),(1)
whereC ∗ ∈R P×Q is the true coefficient matrix generating the data. Similar to fitted model,
we assumed unit variance for the true data generating model. Pre-multiplying both sides of
equation (1) by the shared sketching matrixΦ∈R m×n yields thetrue sketched model:
Y Φ =X ΦC ∗ +ΦE,ΦE∼MatrixNormal(0,ΦΦ T ,I Q),(2)
This acts as the true data generating sketched model in our theoretical analysis. Let the
density of our fitted model with regression coefficientCis denotedp (m)(Y Φ |X Φ,C), and
the density of the true data generating model with the true regression coefficientC ∗ is
denotedp (m)(Y Φ |X Φ,C ∗).
21

5.3 Assumptions
Assumption 1 (Fixed response dimension).The number of response variablesQis
fixed asn→ ∞.
Assumption 2 (Sparse low-rank true coefficient).The true coefficient matrix ad-
mits the decompositionC ∗ =B ∗A∗T ,whereB ∗ ∈R P×R ∗ ,A ∗ ∈R Q×R∗ , andR ∗ =
κQfor someκ∈ {1/Q,2/Q, . . . ,1}.The matrixA ∗ is semi-orthogonal, (A ∗)T A∗ =I R∗,
and all buts ∗ rows ofB ∗ are identically zero, wheres ∗ =o(P). Furthermore, max j,h

C ∗ j,h

 <
Tfor someT >0.
Assumption 3 (Bounded design matrix).ForX j thejth column ofX, max 1≤j≤P ∥X j∥2 =
O(n).
Assumption 4 (Sketching dimension).The sketching dimensionmsatisfiess ∗ log(P) =
o(m), m=o(n).
Assumption 5 (Concentration of sketching matrix).For some positive constants
c′, c′′ >0,∥ΦΦ T −I m∥2 ≤c ′p m/n,
Remark:Assumption 5 holds with probability at least 1−e −c′m over the construction ofΦ
in this article. This holds almost surely for Gaussian sketching matrices Vershynin [2011],
Guhaniyogi and Scheffler [2025].
Remark.Assumption 5 connects the sketching dimension to the intrinsic complexity of the
true model: choosing
m≍s ∗ logP
(up to constants) is the minimal sketching dimension needed to preserve the sparse low-rank
structure ofC ∗. Assumption 2 mirrors the structure exploited by the shrinkage prior onC
in Section 2.2.
5.4 Fractional Posterior and Contraction Rate
Forα∈(0,1), theα-fractional posterior forCunder the approximating sketched model is
Πα(C| ˜Y,X Φ)∝  p(m)(Y Φ |X Φ,C) 	α π(C),(3)
whereπ(C) is the prior onC=BA T induced by the shrinkage prior onBand the standard
Gaussian prior onAspecified in Section 2.2. The contraction rates derived below for Π α
withα∈(0,1) carry over to the standard posterior Π 1 used inBayesVFLReg, as we argue
in this section through Theorem 5.5.
Define thecontraction ratefor the sketched model as
ϵ2 m = QR∗ +R ∗s∗ logP m .(4)
This is the analogue of the minimax rate QR∗+R∗s∗ logP n for the full-data model Bunea et al.
[2012], with the effective sample size replaced by the sketching dimensionm. Assumption 5
ensuresmϵ 2 m → ∞, which is necessary for the posterior to concentrate.
22

5.5 Main Results
We state the three main theoretical results. All proofs are deferred to the Appendix.
Lemma 5.1(Prior concentration in the sketched model).Define the KL neighborhood of
the true coefficient matrix at radiusϵ m as
B∗ m(C ∗, ϵm) =  C: KL  p(m)(Y Φ |X Φ,C ∗), p(m)(Y Φ |X Φ,C)  ≤mϵ 2 m 	 .
Under Assumptions 1-5, there exists a positive constantKsuch that,
π(B ∗ m(C ∗, ϵm))≥e −Kmϵ2 m.
Lemma 5.1 establishes that the shrinkage prior induced by theBayesVFLRegprior spec-
ification assigns exponentially large mass to Kullback–Leibler neighborhoods of the truth in
the sketched model.
Lemma 5.2(Lower bound for the fractional posterior denominator).Let
Dm =
Z
e−α r(C,C∗) π(C)dC, r(C,C ∗) = log p(m)(Y Φ |X Φ,C ∗) p(m)(Y Φ |X Φ,C) .
Under Assumptions 1-5, for anyD >1andt >0, withP (m) C∗ -probability at least1−K ′/{(D−
1 +t) 2mϵ2 m},
Dm ≥e −(D+t)mϵ2 m,
for some positive constantK ′ >0.
Theorem 5.2 provides the high-probability lower bound on the normalizing constant of the
fractional posterior that, combined with the upper bound on the numerator derived from
Fubini’s theorem and Markov’s inequality, yields Theorem 5.3 below.
Theorem 5.3(Fractional posterior concentration under the R´ enyi divergence).Let
Um =

C:D α

p(m)(Y Φ |X Φ,C ∗), p(m)(Y Φ |X Φ,C)  ≥ D+ 3t 1−α mϵ2 m

.
Under Assumptions 1–5, for anyD≥1,t >0and some positive constantK ′, withP (m) C∗ -
probability at least1−K ′/{(D−1 +t) 2mϵ2 m},
Πα

Um | ˜Y

≤e −tmϵ2 m.
Theorem 5.4(Fractional posterior concentration under the Hellinger distance).Under As-
sumptions 1–5, withP (m) C∗ -probability at least1−K ′/{(D−1 +t) 2mϵ2 m},
Πα
 
C: 1 m h2 p(m)(Y Φ |X Φ,C ∗), p(m)(Y Φ |X Φ,C)  ≥ D+ 3t 2(1−α) ϵ2 m


 ˜Y ! ≤e −tmϵ2 m,
for anyD≥1,t≥0, and some positive constantK ′ for largen.
23

Remark.Theorem 5.4 follows immediately from Theorem 5.3 via the equivalence between
R’enyi divergences and the Hellinger distance established in Section 5.2.1. Together, The-
orems 5.3 and 5.4 provide non-asymptotic bounds on the fractional posterior probability
that the fitted density of the sketched data deviates from the true density by more than a
threshold governed by
ϵ2 m = QR∗ +R ∗s∗ logP m ,
Notably, this threshold shares the same form as the minimax risk for sparse low-rank regres-
sion in the full-data model Bunea et al. [2012], with the full sample sizenreplaced by the
sketching dimensionm, reflecting the statistical cost of privacy-preserving data compression.
Remark.For analytical convenience, Assumption 5 is treated as holding with probability 1
throughout the proofs. In practice, however, it holds with probability at least 1−e −c′m
over the draw ofΦ. To make the non-asymptotic bound explicit under this probabilistic
guarantee, define the event
A=
n
Φ:∥ΦΦ T −I m∥F ≤c ′′p m/n o
and observe that
Πα(Um | ˜Y)≤Π α(Um | ˜Y,A) +P(A c)≤e −tmϵ2 m +e −c′m,
so the overall bound retains the same exponential form, with an additional term that is
negligible for largem.
Since the non-asymptotic bound in Theorems 5.3 and 5.4 is established under theα-
fractional posterior, it is natural to ask how closely the fractional posterior approximates the
standard posterior corresponding toα= 1. We address this in the following result.
Theorem 5.5.LetΠ α(C| ˜Y)andΠ(C| ˜Y)be theα-fractional posterior and ordinary full
posterior (atα= 1). Thenlim
α→1
TV(Πα(C| ˜Y),Π(C| ˜Y)) = 0
6 Conclusion
We introduce the Bayesian Vertical Federated Learning (BayesVFLReg) framework tailored
for high-dimensional multivariate sparse reduced-rank regression. While traditional hori-
zontal approaches dominate the literature, our method tackles the more complex setting
of vertically partitioned data distributed across multiple distinct sites. By leveraging data
sketching techniques, our framework successfully constructs a centralized, global represen-
tation of the posterior distribution without compromising site-level privacy. Crucially, this
approach enables principled uncertainty quantification, a feature largely missing from exist-
ing VFL methodologies.
Beyond its foundational architecture, we established the theoretical validity of our method
by deriving non-asymptotic bounds for the posterior concentration around the true density.
Our simulation studies further demonstrate that the proposed framework delivers competi-
tive, and often superior, performance against both alternative VFL methods and standard
algorithms built for centralized data. Ultimately, the privacy-compliant sketched data rep-
resentation introduced here provides a versatile bridge to downstream models. This paves
24

the way for promising future extensions into vertically federated generalized linear models,
survival analysis, and complex non-parametric Bayesian learning.
Acknowledgments
Dr. Rajarshi Guhaniyogi is supported by National Science Foundation DMS-2210672, and
National Institute of Health R01NS131604.
Portions of this research were conducted with the advanced computing resources provided
by Texas A&M Department of Statistics Arseven Computing Cluster.
Data and Software Availability
An open-source implementation of theBayesVFLRegalgorithm, is publicly available on
GitHub athttps://github.com/brighalvy/BayesVFLReg.
25

A Full Conditionals
We begin by vectorizingΦY=ΦXC+Eto obtain:
y=µ y +e(10)
Letting,
y= vec((ΦY) T )∈R mQ×1
µy = vec((ΦXC) T ) = (ΦX⊗A)β= (ΦXB⊗I Q)a∈R mQ×1
e= vec(E T )∼N mQ(0, ˜Σ)
β= vec(B T )∈R P Q×1
a= vec(A)∈R Q2×1
˜Σ= diag(Σ, ...,Σ)∈R mQ×mQ +
Σ= diag(σ 2 1, ..., σ2 Q)∈R Q×Q +
Thus the likelihood can be expressed as
y|X,Φ,A,B,{σ 2 q }q= 1 Q ∼N mQ(µy, ˜Σ) (11)
Noting the independence among the elements ofBin the prior, the joint prior forβis
β| {λp,q}P,Q p,q=1,{τ q}Q q=1 ∼N P Q(0,Λ)
whereΛ= diag(λ 2 1,1τ 2 1 , ..., λ2 1,Qτ 2 Q, ..., λ2 P,Qτ 2 Q)∈R P Q×P Q + . Further, the independence on the
prior for elements ofAinduces the following prior upona:
a∼N Q2(0,I Q2)
A.1 Full conditional ofB(β)
The full conditional ofβis derived as follows;
p(β| ·)∝N mQ(y|µ y, ˜Σ)NP Q(β|0,Λ)
∝exp

− 1 2 (y−µ y)T ˜Σ −1 (y−µ y)  exp  − 1 2 βT Λ−1β 
= exp

− 1 2 h (y−(ΦX⊗A)β) T ˜Σ −1 (y−(ΦX⊗A)β) +β T Λ−1β i
= exp

− 1 2 h yT ˜Σ −1 y−2β T (ΦX⊗A) T ˜Σ −1 y+β T (ΦX⊗A) T ˜Σ −1 (ΦX⊗A)β+β T Λ−1β i
∝exp

− 1 2 h βT ( ˜X T ˜X+Λ −1)β−2β T ˜X T ˜y i
Where ˜y= ˜Σ −1/2 y, ˜X= ˜Σ −1/2 (ΦX⊗A),Ω B = ( ˜X T ˜X+Λ −1). Thus identifying the
multivariate normal kernel we find,
β| · ∼NP Q(Ω−1 B ˜X T ˜y,Ω −1 B ) (12)
26

A.2 Full Conditional ofA(a)
The full conditional ofais derived below:
p(a| ·)∝N mQ(y|µ y, ˜Σ)NQ2(a|0,I Q2)
∝exp

− 1 2 (y−µ y)T ˜Σ −1 (y−µ y)  exp  − 1 2 aT a 
= exp

− 1 2 h (y−(ΦXB⊗I Q)a)T ˜Σ −1 (y−(ΦXB⊗I Q)a) +a T a i
∝exp

− 1 2  −2aT (ΦXB⊗I Q)T Σ−1y+a T (ΦXB⊗I Q)T Σ−1(ΦXB⊗I Q)a+a T a 
= exp

− 1 2  aT ((ΦXB⊗I Q)T Σ−1(ΦXB⊗I Q) +I Q2)a−2a T (ΦXB⊗I Q)T Σ−1y 
= exp

− 1 2  aT ΩAa−2a T (ΦXB⊗I Q)T Σ−1y 
∝exp

− 1 2 (a−Ω −1 A X T ∗ ˜y)T ΩA(a−Ω −1 A X T ∗ ˜y) 
Thus identifying the multivariate normal distribution kernel, the full conditional is,
a| · ∼NQ2(Ω−1 A X T ∗ ˜y,Ω −1 A ) (13)
whereΩ A = (X T ∗ X ∗ +I Q2),X ∗ = ˜Σ −1/2 (ΦXB⊗I Q), and ˜y= ˜Σ −1/2 y.
A.3 Full Conditional ofσ 2 q
We derive the full conditional ofσ 2 q as follows:
p(σ2 q | ·)∝NmQ(y|µ y, ˜Σ) 1 σ2 q
∝det( ˜Σ)−1/2 exp

− 1 2 (y−µ y)T ˜Σ −1 (y−µ y)  1 σ2 q
∝(σ 2 q )−m/2−1 exp
(
− 1 2
QX
q′=1
mX
i=1
(y−µ y)2 q′i/σ2 q′
)
∝(σ 2 q )−m/2−1 exp

− 1 2σ2 q yT q yq

Utilizing the fact that ˜Σis a diagonal matrix and hence det(˜Σ) = QQ q=1 Qm i=1 σ2 q = QQ q=1(σ2 q )m,
and that ˜Σ −1 = (Σ−1, ...,Σ−1) andΣ −1 = diag(1/σ2 1, ...,1/σ2 Q). Letting,
yq =Γ q(y−µ y)∈R mQ×1
Γq = diag(1q, . . . ,1q)∈R mQ×mQ
1q ∈R Q×1 is a vector of zeros with 1 in theq th position.
27

Thus,
σ2 q | · ∼IG(m 2 , yT q yq 2 ) (14)
A.4 Full conditional ofλ p,q
The full conditional forλ p,q is found as:
p(λp,q | ·)∝NP Q(β|0,Λ)C +(λp,q |0,1)
∝det(Λ) −1 exp{− 1 2 βT Λ−1β} 1 1 +λ 2 p,q
=
" QY
q′=1
PY
p′=1
1
λ2 p′,q′τ 2 q′
#
exp{− 1 2
QX
q′=1
PX
p′=1
b2 p′,q′/λp′,q′2τ 2 q′} 1 1 +λ 2 p,q
∝ 1 λ2 p,q exp{− 1 2 b2 p,q λ2 p,qτ 2 q } 1 1 +λ 2 p,q
This is not a known distribution. A slice sampler will be used as outlined in Section B to
draw from this conditional distribution.
A.5 Full conditional ofτ 2 q
We find,
p(τq | ·)∝NP Q(β|0,Λ)C +(τh |0,1)
∝det(Λ) −1 exp{− 1 2 βT Λ−1β} 1 1 +τ 2 h
=
" QY
q′=1
PY
p′=1
1
λ2 p′q′τ 2 q′
#
exp{− 1 2
qX
q′=1
PX
p′=1
b2 p′q′/λp′q′2τ 2 q′} 1 1 +τ 2 h
∝ 1 τ 2p q exp{− 1 2τ 2 q
PX
p=1
b2 pq
λ2 p,q } 1 1 +τ 2 h
This is an unknown distribution and the sampler is described in Section B.
B Gibbs Sampler
We follow the 4-step Metropolis-within-Gibbs in Algorithm1 outlined in the article to cycle
through updating the full conditional distributions. Step 2 leverages the spectral decompo-
sition ofΩ −1 A outlined below:
1. Compute the spectral decomposition ofΩ −1 A =QDQ ⊤
2. Drawz∼N Q2(0,1)
28

3. Leta ∗ =Ω −1 A X T ∗ ˜y+QD 1/2z
Step 4 employs a slice sampling algorithm following Polson et al. [2014]:
1. Sampleuuniformly on the interval (0, 1 1+η ).
2. Sampleηfrom a truncated Exp(2/µ) with zero probability outside the interval (0, 1−u u ),
whereη= 1/λ 2 p,q or 1/τ 2 q . Ifη= 1/λ 2 p,q thenµ= b2 pq τ 2q , otherwise forη= 1/τ 2 q letµ= PP
p=1
b2 pq
λ2p,q .
C Neuroimaging Data Application
Table 3: 53 ROIs found in the 60 significant ROI-ROI connections with corresponding short-
hand codes (short hand codes following Di Martino et al. [2008], Desikan et al. [2006],
Diedrichsen et al. [2009]).
Index Code Region of Interest (ROI)
1L IPLLeft inferior parietal lobule
2L VSsLeft superior ventral striatum
3L AMYGLeft amygdala
4L DCaudLeft dorsal caudate
5R VSsRight superior ventral striatum
6R LPCRight lateral parietal cortex
7PCCPosterior cingulate cortex
8R Cereb VIRight Cerebellar Lobule VI
9L dlPFCLeft dorsolateral prefrontal cortex
10R Cereb VRight Cerebellar Lobule V
11L lPMCLeft lateral premotor cortex
12RSCRetro Splenial
13R dlPFCRight dorsolateral prefrontal cortex
14vmPFCVentromedial prefrontal cortex
15L PHGLeft parahippocampus gyrus
16R PHGRight parahippocampus gyrus
17R IPSRight intraparietal sulcus
18R SFCRight superior frontal cortex
19L vlPMCLeft ventral lateral premotor cortex
20L OFCLeft orbitofrontal cortex
21R lPFCRight lateral prefrontal cortex
22L PCunLeft precuneus
23L PHCLeft parahippocampus
24L IPSLeft intraparietal sulcus
25R CrusIRight Cerebellar Crus I
26R VSiRight inferior ventral striatum
27R CrusIIRight Cerebellar Crus II
28R aINSRight anterior insula
29

Table 3: 53 ROIs found in the 60 significant ROI-ROI connections with corresponding short-
hand codes (short hand codes following Di Martino et al. [2008], Desikan et al. [2006],
Diedrichsen et al. [2009]).
Index Code Region of Interest (ROI)
29L vrPUTLeft ventral rostral putamen
30L drPUTLeft dorsal rostral putamen
31L VSiLeft inferior ventral striatum
32L aINSLeft anterior insula
33R OFCRight orbitofrontal cortex
34amPFCAnterior medial prefrontal cortex
35L SMCLeft sensorimotor cortex
36L FGLeft frontal gyrus
37R DCaudRight dorsal caudate
38PCC 2Posterior cingulate cortex 2
39L aPFCLeft anterior prefrontal cortex
40R PHCRight parahippocampus
41L dlPMCLeft dorsolateral premotor cortex
42L M1Left primary motor cortex
43R vlPMCRight ventral lateral premotor cortex
44R SMCRight sensorimotor cortex
45R M1Right primary motor cortex
46R PCunRight precuneus
47L dcPUTLeft dorsal caudal putamen
48R vrPUTRight ventral rostral putamen
49R dcPUTRight dorsal caudal putamen
50R drPUTRight dorsal rostral putamen
51dACCDorsal anterior cingulate cortex
52mPFCMesial prefrontal cortex
53R ITLRight inferior temporal lobe
D Theoretical Guarantees: Proofs
Proof of Lemma 5.1
Step 1:Note that Var(vec(Y Φ)) under the fitted model has isI mQ while Var(vec(Y Φ)) under
the true data generating sketched model isI Q ⊗ΦΦ T , we compute the KL divergence between
the two fitted densities. Using the formula for KL divergence between two Gaussian matrix-variate
densities:
KL

p(m)(Y Φ |X Φ,C ∗), p(m)(Y Φ |X Φ,C)  = Q 2  tr(ΦΦT −I m)−log det(ΦΦ T )  + 1 2 ∥X Φ(C−C ∗)∥2 F ,
where we used det(I Q ⊗ΦΦ T ) = (det(ΦΦT ))Q and tr(I Q ⊗ΦΦ T ) =Q·tr(ΦΦ T ). Since tr(H)−
log det(H)−d≤ ∥H−I d∥2 F for anyd×dpositive definite matrixH, we obtain:
KL

p(m)(Y Φ |X Φ,C ∗), p(m)(Y Φ |X Φ,C)  ≤ Q 2 ∥ΦΦT −I m∥2 F + 1 2 ∥X Φ(C−C ∗)∥2 F .(S1)
30

Step 2:By Assumptions 1 and 5:
Q
2 ∥ΦΦT −I m∥2 F ≤ Qc′′2m 2n ≤ mϵ2 m 2 ,
where the last inequality holds sincem/n=o(mϵ 2 m) under Assumption 4.
Step 3:For the second term in (S1), using the Cauchy–Schwarz inequality:
∥X Φ(C−C ∗)∥2 F ≤ ∥XΦ∥2 F ∥C−C ∗∥2 F ≤Qmax 1≤j≤P ∥X Φj∥2∥C−C ∗∥2 F .
By Assumption 5,λ max(ΦΦT )≤1 +c ′′p m/n, so:
∥X Φj∥2 =∥ΦX j∥2 ≤λ max(ΦΦT )∥X j∥2 ≤  1 +c ′′p m/n  ∥X j∥2 =O(n),
where the last step uses Assumption 3. Therefore:
∥X Φ(C−C ∗)∥2 F ≤Q·O(n)· ∥C−C ∗∥2 F .(S2)
It follows that:
π

C:∥X Φ(C−C ∗)∥2 F ≤mϵ 2 m  ≥π  C:∥C−C ∗∥2 F ≤ mϵ2 m Q·O(n)  =π  C:∥C−C ∗∥2 F ≤δ 2 C  ,
whereδ C ={(QR ∗+R∗s∗ logP)/n} 1/2, sincemϵ 2 m/(Qn) = (QR∗+R∗s∗ logP)/n=δ 2 C by definition
ofϵ 2 m. Assumption 1 has also been used here.
Step 4:Under Assumption 2, By Lemma S5 of the supplementary material of Chakraborty et al.
[2020], the priorπ(C) satisfies:
π(C:∥C−C ∗∥F < δC)≥e −K(QR ∗+R∗s∗ logP) =e −Kmϵ2 m,
for some positive constantK.
From Steps 2–4, the KL neighborhoodB ∗ m(C∗, ϵm) contains the set{C:∥X Φ(C−C ∗)∥2 F ≤
mϵ2 m}, which in turn contains a Frobenius ball of radiusδ C aroundC ∗. Therefore:
π(B ∗ m(C∗, ϵm))≥π  C:∥C−C ∗∥2 F ≤δ 2 C  ≥e −Kmϵ2 m.■
Proof of Lemma 5.2
The proof follows three steps.
Step 1:SinceD m ≥0, restricting the integral toB ∗ m(C∗, ϵm) gives:
Dm ≥π(B ∗ m(C∗, ϵm))
Z
B∗m(C∗,ϵm)
e−αr(C,C ∗) dπ(B) C =:π(B ∗ m(C∗, ϵm))·D ∗ m,
wheredπ (B) C =π(B ∗ m(C∗, ϵm))−1dπC is the prior restricted toB ∗ m(C∗, ϵm). By Lemma 5.1:
π(B ∗ m(C∗, ϵm))≥e −Kmϵ2 m.(S3)
Step 2:Applying Jensen’s inequality to the concave function log(·):
logD ∗ m ≥ −α
Z
B∗m
r(C,C ∗)dπ (B) C =Z.
31

Taking expectation underP (m) C∗ :
EC∗[Z] =−α
Z
B∗m(C∗,ϵm)
EC∗[r(C,C ∗)]dπ (B) C
=−α
Z
B∗m(C∗,ϵm)
KL

p(m)(Y Φ|X Φ,C ∗), p(m)(Y Φ|X Φ,C)  dπ(B) C ≥ −αmϵ2 m,(S4)
where the last inequality follows because, by definition ofB ∗ m(C∗, ϵm), each integrand is at most
mϵ2 m.
Step 3:We now compute Var C∗(Z). SinceZ=−α R B∗m(C∗,ϵm) r(C,C ∗)dπ (B) C :
VarC∗(Z)≤α 2
Z
B∗m(C∗,ϵm)
VarC∗(r(C,C ∗))dπ (B) C ,
where the variance of the log-likelihood ratio is:
VarC∗(r(C,C ∗)) =
Z
p(m)(Y Φ|X Φ,C ∗)

log p(m)(Y Φ|X Φ,C ∗) p(m)(Y Φ|X Φ,C) !2 dY Φ
−
h
KL

p(m)(Y Φ|X Φ,C ∗), p(m)(Y Φ|X Φ,C) i2 .
From the second-moment calculation, with∆=X Φ(C−C ∗):
VarC∗(r(C,C ∗)) = Q 2 ∥ΦΦT −I m∥2 F | {z }
T1
+ tr[∆T ΦΦT ∆]| {z }
T2
.
We bound each term onB ∗ m(C∗, ϵm).
•Bound onT 1:By Assumptions 1, 4, 5,∥ΦΦ T −I m∥2 F ≤c ′′2m/n, so:
T1 = Q 2 ∥ΦΦT −I m∥2 F ≤ Qc′′2m 2n ≤K 1mϵ2 m.
•Bound onT 2:By Assumption 5,λ max(ΦΦT )≤1 +c ′′p m/n, so:
T2 = tr[∆T ΦΦT ∆]≤λ max(ΦΦT )∥∆∥2 F ≤  1 +c ′′p m/n  ∥X Φ(C−C ∗)∥2 F ≤K 2mϵ2 m,
where the last inequality uses∥X Φ(C−C ∗)∥2 F ≤mϵ 2 m onB ∗ m(C∗, ϵm), which follows from
the KL bound established in Step 1 of Lemma 5.1.
Therefore, withK ′ =K 1 +K 2:
VarC∗(Z)≤α 2
Z
B∗m(C∗,ϵm)
(T1 +T 2)dπ (B) C ≤K ′α2mϵ2 m.(S5)
ApplyingChebyshev’s inequalityand equations (S4) and (S5):
P (m) C∗  Z≤ −α(D+t)mϵ 2 m  ≤ VarC∗(Z) {α(D−1 +t)mϵ 2m}2 ≤ K′ (D−1 +t) 2mϵ2m .
32

Hence, withP (m) C∗ -probability at least 1−K ′/{(D−1 +t) 2mϵ2 m}:
logD ∗ m ≥Z≥ −α(D+t)mϵ 2 m =⇒D ∗ m ≥e −α(D+t)mϵ2 m.
Using equation (S3) and the bound onD ∗ m, and noting thate −Kmϵ2 m gets absorbed into
e−(D+t)mϵ2 m forD >1:
Dm ≥π(B ∗ m(C∗, ϵm))·D ∗ m ≥e −(D+t)mϵ2 m.■
Proof of Theorem 5.3
Write the fractional posterior probability as a ratio:
Πα(Um |Y Φ) = Nm Dm , N m = Z Um e−αr(C,C ∗)π(C)dC, D m = Z e−αr(C,C ∗)π(C)dC
Using the identity
Aα

p(m)(Y Φ|X Φ,C ∗), p(m)(Y Φ|X Φ,C)  =e −(1−α)Dα(p(m)(Y Φ|X Φ,C∗), p(m)(Y Φ|X Φ,C))
and Fubini’s theorem:
EC∗[Nm] =
Z
Um
EC∗
h
e−αr(C,C ∗) i π(C)dC= Z
Um
e−(1−α)Dα(p(m)(Y Φ|X Φ,C∗), p(m)(Y Φ|X Φ,C))π(C)dC.
OnU m, by definition, (1−α)D α(p(m)(Y Φ|X Φ,C ∗), p(m)(Y Φ|X Φ,C))≥(D+ 3t)mϵ 2 m, so:
EC∗[Nm]≤e −(D+3t)mϵ2 m · Z
Um
π(C)dC≤e −(D+3t)mϵ2 m.
ApplyingMarkov’s inequality:
P (m) C∗

Nm ≥e −(D+2t)mϵ2 m

≤ EC∗[Nm] e−(D+2t)mϵ2m ≤e −tmϵ2 m ≤ 1 (D−1 +t) 2 mϵ2m .(S6)
Hence, withP (m) C∗ -probability at least 1−1/{(D−1 +t) 2mϵ2 m}:
Nm ≤e −(D+2t)mϵ2 m.(S7)
From Theorem 5.2,D m ≥e −(D+t)mϵ2 m withP (m) C∗ -probability at least 1−K ′/{(D−1 +t) 2mϵ2 m},
for some positive constantK ′. Combining the aforementioned two results, we obtain
Πα(Um |Y Φ) = Nm Dm , N m = e−(D+2t)mϵ2 m e−(D+t)mϵ2m ≤e −tmϵ2 m.
withP (m) C∗ -probability at least 1−K ′/{(D−1 +t) 2mϵ2 m}■
Proof of Theorem 5.5
Define,
mα(Y Φ) =
Z
{p(m)(Y Φ|X Φ,C)} απ(C)dC, m(Y Φ) =
Z
p(m)(Y Φ|X Φ,C)π(C)dC.
33

Define, for anyM >0,A M ={C:p (m)(Y Φ|X Φ,C)≤M}. OnA M ,{p (m)(Y Φ|X Φ,C)} α ≤
max{1, Mα} ≤max{1, M}. Asα→1,{p (m)(Y Φ|X Φ,C)} απ(C)→p (m)(Y Φ|X Φ,C)π(C), andR
AM p(m)(Y Φ|X Φ,C)π(C)dC≤ ∞, by dominated convergence theorem,
Z
AM
{p(m)(Y Φ|X Φ,C)} απ(C)dC→
Z
AM
p(m)(Y Φ|X Φ,C)π(C)dC,asα→1.
π(Ac M ) =π(C:p (m)(Y Φ|X Φ,C)≤M)≤ m(Y Φ) M , by Markov inequality.
Usingx α < xforx >1, we have
Z
Ac M
{p(m)(Y Φ|X Φ,C)} απ(C)dC≤
Z
Ac M
p(m)(Y Φ|X Φ,C)π(C) =
Z
C:p(m)>M
p(m)(Y Φ|X Φ,C)π(C)→0,
asM→ ∞.
For anyϵ >0, chooseMlarge enough so that
Z
Ac M
p(m)(Y Φ|X Φ,C)π(C)dC< ϵ/3.
Then forαsufficiently close to 1,
|mα(Y Φ)−m(Y Φ)| ≤

 Z AM {p(m)(Y Φ|X Φ,C)} απ(C)dC− Z AM p(m)(Y Φ|X Φ,C)π(C)dC

+ 2
Z
Ac M
p(m)(Y Φ|X Φ,C)π(C)dC< ϵ.
Thereforem α(Y Φ)→m(Y Φ) asα→1, forP (m) C∗ -almost everyY Φ.
For eachCandP (m) C∗ -almost everyY Φ,
Πα(C|Y Φ) = {p(m)(Y Φ|X Φ,C)} απ(C) mα(Y Φ) → p(m)(Y Φ|X Φ,C)π(C) m(Y Φ) = Π(C|Y Φ),
pointwise asα→1, since both the numerator converges pointwise andm α(Y Φ)→m(Y Φ)>0.
Since Πα(· |Y) and Π(· |YΦ) are both probability densities integrating to 1, and the pointwise
limit holds, an application ofScheff´ e’s theoremgives:
TV(Πα(· |YΦ),Π(· |YΦ)) =
Z
|Πα −Π|dΠ→0,asα→1.■
References
Daniel Ahfock, William J Astle, and Sylvia Richardson. Statistical properties of sketching algo-
rithms.arXiv preprint arXiv:1706.03665, 2017.
Hannah K. Ballard, T. Bryan Jackson, Abigail C. Symm, Tracey H. Hicks, and Jessica A. Bernard.
Age-related differences in functional network segregation in the context of sex and reproductive
stage.Human Brain Mapping, 44(5):1949–1963, 2022. doi: 10.1002/hbm.26184.
Florentina Bunea, Yiyuan She, and Marten H Wegkamp. Joint variable and rank selection for
parsimonious estimation of high-dimensional matrices. 2012.
34

Jianping Cai, Ximeng Liu, Zhiyong Yu, Kun Guo, and Jiayin Li. Efficient vertical federated learning
method for ridge regression of large-scale samples.IEEE Transactions on Emerging Topics in
Computing, 11(2):511–526, 2022.
Fran¸ cois Caron and Arnaud Doucet. Sparse Bayesian nonparametric regression. InProceedings of
the 25th international conference on Machine learning, pages 88–95, 2008.
Carlos M Carvalho, Nicholas G Polson, and James G Scott. The horseshoe estimator for sparse
signals.Biometrika, 97(2):465–480, 2010.
Antik Chakraborty, Anirban Bhattacharya, and Bani K Mallick. Bayesian sparse multiple regression
for simultaneous rank reduction and variable selection.Biometrika, 107(1):205–221, 2020.
Chaochao Chen, Jun Zhou, Li Wang, Xibin Wu, Wenjing Fang, Jin Tan, Lei Wang, Alex X Liu,
Hao Wang, and Cheng Hong. When homomorphic encryption marries secret sharing: Secure
large-scale sparse logistic regression and applications in risk control. InProceedings of the 27th
ACM SIGKDD conference on knowledge discovery & data mining, pages 2652–2662, 2021.
Lisha Chen and Jianhua Z Huang. Sparse reduced-rank regression for simultaneous dimension
reduction and variable selection.Journal of the American Statistical Association, 107(500):
1533–1545, 2012.
Thomas M. Cover and Joy A. Thomas.Elements of Information Theory. Wiley-Interscience,
Hoboken, NJ, 2nd edition, 2006. doi: 10.1002/047174882X.
Mingjun Dai, Ziying Zheng, Zhaoyan Hong, Shengli Zhang, and Hui Wang. Edge computing-aided
coded vertical federated linear regression.IEEE Transactions on Cognitive Communications and
Networking, 8(3):1543–1551, 2022.
Rahul S Desikan, Florent S´ egonne, Bruce Fischl, Brian T Quinn, Bradford C Dickerson, Deborah
Blacker, Randy L Buckner, Anders M Dale, R Paul Maguire, Bradley T Hyman, et al. An
automated labeling system for subdividing the human cerebral cortex on mri scans into gyral
based regions of interest.NeuroImage, 31(3):968–980, 2006.
Adriana Di Martino, Anouk Scheres, Daniel S Margulies, A M Clare Kelly, Lucina Q Uddin, Zarrar
Shehzad, Bharat Biswal, F Xavier Castellanos, and Michael P Milham. Functional connectivity
of human striatum subregions.Cerebral Cortex, 18(12):2735–2747, 2008.
J¨ orn Diedrichsen, Joshua H Balsters, Jonathan Flavell, Emily Cussans, and Narender Ramnani. A
probabilistic mr atlas of the human cerebellum.NeuroImage, 46(1):39–46, 2009.
Edgar Dobriban and Sifan Liu. A new theory for sketching in linear regression.arXiv preprint
arXiv:1810.06089, 2018.
Cynthia Dwork and Aaron Roth. The algorithmic foundations of differential privacy.Foundations
and trends®in theoretical computer science, 9(3-4):211–487, 2014.
Adri` a Gasc´ on, Phillipp Schoppmann, Borja Balle, Mariana Raykova, Jack Doerner, Samee Za-
hur, and David Evans. Privacy-preserving distributed linear regression on high-dimensional
data.Proceedings on Privacy Enhancing Technologies, 2017(4):345–364, 2017. doi: 10.1515/
popets-2017-0053.
35

Leo N Geppert, Katja Ickstadt, Alexander Munteanu, Jens Quedenfeld, and Christian Sohler.
Random projections for Bayesian regression.Statistics and Computing, 27(1):79–101, 2017.
Cristiano Gratton, Naveen KD Venkategowda, Reza Arablouei, and Stefan Werner. Distributed
ridge regression with feature partitioning. In2018 52nd Asilomar Conference on Signals, Sys-
tems, and Computers, pages 1423–1427. IEEE, 2018.
Sharmistha Guha and Jerome P Reiter. Differentially private estimation of weighted average treat-
ment effects for binary outcomes.Computational Statistics & Data Analysis, 207:108145, 2025.
Sharmistha Guha and Abel Rodriguez. Bayesian regression with undirected network predictors
with an application to brain connectome data.Journal of the American Statistical Association,
pages 1–13, 2020.
Sharmistha Guha and Abel Rodriguez. Bayesian regression with undirected network predictors
with an application to brain connectome data.Journal of the American Statistical Association,
116(534):581–593, 2021.
Rajarshi Guhaniyogi and Aaron Wolfe Scheffler. Sketching in high-dimensional regression with big
data using gaussian scale mixture priors.Journal of Machine Learning Research, 26(271):1–28,
2025.
Rajarshi Guhaniyogi and Daniel Spencer. Bayesian tensor response regression with an application
to brain activation studies.Bayesian Analysis, 16(4):1221–1249, 2021.
Rajarshi Guhaniyogi, Laura Baracaldo, and Sudipto Banerjee. Bayesian data sketching for varying
coefficient regression models.Journal of Machine Learning Research, 26(98):1–29, 2025.
Conor Hassan, Matthew Sutton, Antonietta Mira, and Kerrie Mengersen. Scalable vertical federated
learning via data augmentation and amortized inference.arXiv preprint arXiv:2405.04043, 2024.
Tracey H. Hicks, Thamires N. Magalh˜ aes, Hannah K. Ballard, T. Bryan Jackson, Sydney J. Cox,
and Jessica A. Bernard. Network segregation in aging females and evaluation of the impact of
sex steroid hormones.Frontiers in Human Neuroscience, 17, Feb 2023. doi: 10.3389/fnhum.
2023.1059091.
T. Bryan Jackson and Jessica A. Bernard. Cerebello-basal ganglia networks and cortical network
global efficiency.The Cerebellum, 22:588–600, 2023. doi: 10.1007/s12311-022-01418-z.
Haizhou Liu, Xuan Zhang, Xinwei Shen, and Hongbin Sun. A federated learning framework for
smart grids: Securing power traces in collaborative learning.arXiv preprint arXiv:2103.11870,
2021.
Yang Liu, Yan Kang, Tianyuan Zou, Yanhong Pu, Yuanqin He, Xiaozhou Ye, Ye Ouyang, Ya-Qin
Zhang, and Qiang Yang. Vertical federated learning: Concepts, advances, and challenges.IEEE
transactions on knowledge and data engineering, 36(7):3615–3634, 2024.
Nicholas G Polson and James G Scott. Shrink globally, act locally: Sparse Bayesian regularization
and prediction.Bayesian Statistics, 9:501–538, 2010.
Nicholas G Polson, James G Scott, and Jesse Windle. The bayesian bridge.Journal of the Royal
Statistical Society Series B: Statistical Methodology, 76(4):713–733, 2014.
36

Gregory C Reinsel and Raja P Velu.Multivariate reduced-rank regression. Springer, 1998.
Helene Ruffieux, Anthony C Davison, Jorg Hager, and Irina Irincheeva. Efficient inference for
genetic association studies with multiple outcomes.Biostatistics, 18(4):618–636, 2017.
Ashish P Sanil, Alan F Karr, Xiaodong Lin, and Jerome P Reiter. Privacy preserving regression
modelling via distributed computation. InProceedings of the tenth ACM SIGKDD international
conference on Knowledge discovery and data mining, pages 677–682, 2004.
Tamas Sarlos. Improved approximation algorithms for large matrices via random projections. In
2006 47th Annual IEEE Symposium on Foundations of Computer Science (FOCS’06), pages
143–152. IEEE, 2006.
Stephen M Smith, Peter T Fox, Karla L Miller, David C Glahn, P M Fox, Charles E Mackay,
Nicola Filippini, Kate E Watkins, Roberto Toro, Angela R Laird, and Christian F Beckmann.
Correspondence of the brain’s functional architecture during activation and rest.Proceedings of
the National Academy of Sciences, 106(31):13040–13045, 2009.
Ga¨ el Varoquaux and R Cameron Craddock. Learning and comparing functional connectomes across
subjects.NeuroImage, 80:405–415, 2013.
Roman Vershynin. Introduction to the non-asymptotic analysis of random matrices.arXiv preprint
arXiv:1011.3027, 2010.
Roman Vershynin. Spectral norm of products of random and deterministic matrices.Probability
theory and related fields, 150(3):471–509, 2011.
Susan L. Whitfield-Gabrieli and Alfonso Nieto-Castanon. Conn: A functional connectivity toolbox
for correlated and anticorrelated brain networks.Brain connectivity, 2 3:125–41, 2012.
Zhaomin Wu, Zhen Qin, Junyi Hou, Haodong Zhao, Qinbin Li, Bingsheng He, and Lixin Fan.
Vertical federated learning in practice: The good, the bad, and the ugly.arXiv preprint
arXiv:2502.08160, 2025.
Qiang Yang, Yang Liu, Tianjian Chen, and Yongxin Tong. Federated machine learning: Concept
and applications.ACM Transactions on Intelligent Systems and Technology (TIST), 10(2):1–19,
2019.
Jiaqi Zhao, Hui Zhu, Fengwei Wang, Rongxing Lu, Ermei Wang, Linfeng Li, and Hui Li. Vflr:
An efficient and privacy-preserving vertical federated framework for logistic regression.IEEE
Transactions on Cloud Computing, 11(4):3326–3340, 2023.
Shuheng Zhou, Larry Wasserman, and John D Lafferty. Compressed regression. InAdvances in
Neural Information Processing Systems, pages 1713–1720, 2008.
Shuheng Zhou, John Lafferty, and Larry Wasserman. Compressed and privacy-sensitive sparse
regression.IEEE Transactions on Information Theory, 55(2):846–866, 2009.
37
