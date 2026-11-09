---
title: 'Causal Inference under Threshold Manipulation: Bayesian Mixture Modeling and Heterogeneous Treatment
  Effects'
url: https://arxiv.org/abs/2509.19814
category: ai-marketing
subcategory: empirical
date: 2025-09
venue: ''
authors:
- Kohsuke Kubota
- Shonosuke Sugasawa
source: arxiv
pdf_url: https://arxiv.org/pdf/2509.19814
pages: 12
chars: 48560
fetched_at: '2026-11-08T13:12:14+00:00'
kb_version: 1
---

# Causal Inference under Threshold Manipulation: Bayesian Mixture Modeling and Heterogeneous Treatment Effects

Causal Inference Under Threshold Manipulation: Bayesian Mixture Modeling
and Heterogeneous Treatment Effects
Kohsuke Kubota1, Shonosuke Sugasawa2
1NTT DOCOMO, INC., Tokyo, Japan
2Faculty of Economics, Keio University, Tokyo, Japan
kousuke.kubota.xt@nttdocomo.com, sugasawa@econ.keio.ac.jp
Abstract
Many marketing applications, including credit card incen-
tive programs, offer rewards to customers who exceed spe-
cific spending thresholds to encourage increased consump-
tion. Quantifying the causal effect of these thresholds on cus-
tomers is crucial for effective marketing strategy design. Al-
though regression discontinuity design is a standard method
for such causal inference tasks, its assumptions can be vio-
lated when customers, aware of the thresholds, strategically
manipulate their spending to qualify for the rewards. To ad-
dress this issue, we propose a novel framework for estimat-
ing the causal effect under threshold manipulation. The main
idea is to model the observed spending distribution as a mix-
ture of two distributions: one representing customers strate-
gically affected by the threshold, and the other represent-
ing those unaffected. To fit the mixture model, we adopt
a two-step Bayesian approach consisting of modeling non-
bunching customers and fitting a mixture model to a sam-
ple around the threshold. We show posterior contraction of
the resulting posterior distribution of the causal effect under
large samples. Furthermore, we extend this framework to a hi-
erarchical Bayesian setting to estimate heterogeneous causal
effects across customer subgroups, allowing for stable infer-
ence even with small subgroup sample sizes. We demonstrate
the effectiveness of our proposed methods through simula-
tion studies and illustrate their practical implications using a
real-world marketing dataset.
1 Introduction
Estimating causal effects of thresholds is important for the
effective design of marketing strategies. Many marketing ap-
plications, including loyalty programs (e.g. Kivetz, Urmin-
sky, and Zheng 2006; Nastasoiu et al. 2021) and credit card
incentive programs, offer rewards to customers who exceed
specific spending thresholds to encourage increased con-
sumption. Regression discontinuity design (RDD) is a repre-
sentative method to estimate the causal effect of thresholds
on customer behavior (Hahn, Todd, and der Klaauw 2001;
Thistlethwaite and Campbell 1960). This approach estimates
the causal effect by using local randomization around the
threshold and is widely applied as one of the most credible
research designs for causal inference, particularly because
Copyright © 2026, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
its identification assumptions are considered weak and plau-
sible (Cattaneo, Idrobo, and Titiunik 2024; McCrary 2008).
However, the local randomization assumption of RDD
can be violated when customers, aware of the thresholds,
strategically manipulate their spending to qualify for the re-
wards. This strategic behavior of customers at the thresholds
breaks the local randomization assumption supported by the
continuitycondition (Hahn, Todd, and der Klaauw 2001),
which states that the potential outcomes of customers just
below and above the threshold are the same. This condition
cannot be satisfied when customers can manipulate their be-
havior to reach the thresholds because they may have differ-
ent potential outcomes depending on whether they are above
or below the threshold (Ishihara and Sawada 2024; McCrary
2008; Lee 2008). Although the economics literature pro-
poses the bunching estimation (e.g. Bertanha et al. 2024) to
address this issue, this framework relies on the assumption
that a segment of the distribution just before the threshold,
where the probability density function becomes zero, is what
is transformed into the observed “bunch” at the threshold.
Consequently, the practical applicability of these methods
can be limited in scenarios where such a zero-density region
cannot be assumed, which often arises in marketing applica-
tions.
To address causal inference under manipulation, we pro-
pose a novel Bayesian framework called Bayesian Model-
ing of Threshold Manipulation via Mixtures (BMTM). This
framework employs a Bayesian mixture model to distin-
guish between customers strategically affected by a thresh-
old and those who are not, enabling robust causal effect esti-
mation with uncertainty quantification (see Figure 1). To fit
the mixture model, we adopt a two-step Bayesian approach
consisting of modeling non-bunching customers and fitting
a mixture model to a sample around the threshold. In addi-
tion, we extend BMTM to a hierarchical Bayesian setting to
estimate heterogeneous causal effects across subgroups of
customers, which we call hierarchical BMTM (HBMTM).
This hierarchical structure ensures stable estimation, even
for small subgroups, by borrowing information across them
to meet the increasing demand in marketing for estimating
heterogeneous causal effects.
We demonstrate the effectiveness of our proposed frame-
work through simulation studies and analysis of a real-world
marketing dataset. The results of the simulation studies in-
arXiv:2509.19814v2  [stat.ME]  16 Jan 2026

Y
Density
Observed distribution
Mixture model
Bunching distribution
Non-bunching distribution
Threshold
Figure 1: Conceptual illustration of our proposed mixture
model (red). Modeling the observed distribution (skyblue) as
a mixture of a non-bunching distribution (green, unaffected
by the threshold) and a strategic bunching distribution (blue,
distorted near the threshold).
dicate that our proposed methods achieve more accurate and
reliable estimates of causal effects than conventional RDD
methods. In particular, HBMTM provides stable estimates
of heterogeneous causal effects across customer subgroups,
even in scenarios with small sample sizes. The real-world
case study further illustrates the practical implications and
utility of our framework.
2 Related Work
This section reviews related work on bunching estimation
and methods to estimate heterogeneous causal effects us-
ing RDD. The bunching estimation examines the disconti-
nuity in the distribution of the running variable. In the litera-
ture, there are two types of discontinuities: kinks, where the
slope of an incentive schedule changes (e.g. Saez 2010), and
notches, where the level of the incentive changes discontin-
uously (e.g. Slemrod 2013). Marketing incentive programs,
which offer a discrete reward upon reaching a threshold, typ-
ically fall into the notch category. In addition to the literature
in Section 1, the existing bunching estimation methods (e.g.
Kleven and Waseem 2013) assume sharp bunching, where
individuals can precisely target and locate themselves at the
threshold. However, this assumption is often too strong in
real-world marketing scenarios because customers may not
be fully aware of the exact threshold value or face constraints
and imperfect control over their spending behavior. In con-
trast to these existing approaches that assume sharp bunch-
ing, our proposed framework explicitly models the entire
distribution of customer behavior around the threshold. By
employing a mixture model for density estimation, our pro-
posed method naturally captures the diffuse nature of bunch-
ing that arises from customers’ imperfect control, allowing
for causal effect estimation under more plausible assump-
tions for marketing applications.
In RDD (without threshold manipulation), there are some
methods to estimate the heterogeneous treatment effect
across subgroups. For example, Sugasawa, Ishihara, and
Kurisu (2023) developed a hierarchical model to estimate
the subgroup-specific causal effect, and Alcantara et al.
(2024) and Tao, Wang, and Ruppert (2025) employed the
Bayesian additive regression tree to capture heterogeneous
effects. However, these methods cannot be applied under
threshold manipulation. To our knowledge, no attempts have
been made to estimate the heterogeneous causal effects un-
der threshold manipulation. Therefore, this paper would be
the first to provide an effective method for estimating het-
erogeneous causal effects under threshold manipulation.
3 Bayesian Modeling of Threshold
Manipulation via Mixtures
3.1 Causal Inference Under Threshold
Manipulation
Consider the problem of estimating the causal effect of a
thresholdKon customers with the potential outcome frame-
work (Imbens and Rubin 2015; Rubin 1974). LetY(1)be
the potential outcome with thresholdKandY(0)be the po-
tential outcome without a threshold. Assume that there are
two types of customers: those who strategically exceed a
specific thresholdK(i.e.,bunching customers) and those
who do not exceed the threshold (i.e.,non-bunching cus-
tomers). Bunching customers increase or adjust their spend-
ing to exceed the threshold and gain greater benefits than
without it. In contrast, non-bunching customers do not ex-
ceed the threshold or gain extra benefits. Consequently, it
is assumed that the bunching customers have potential out-
comesY(t)(fort∈ {0,1}) which fall within the neigh-
borhood of the thresholdK, while non-bunching customers
have the same potential outcomes,Y(1) =Y(0)which lie
outside the neighborhood. Under the framework, the average
treatment effect of the threshold on customers is defined as
∆≡E[Y(1)−Y(0)|Y(t)∈N K, t∈ {0,1}],(1)
whereN K = [y, y]is the interval as the neighborhood of the
thresholdK. This definition can be interpreted as the aver-
age treatment effect of the threshold on bunching customers,
which is conceptually similar to the average treatment effect
on the treated (ATT) in the potential outcome framework. In
our application, we will deal with the situation with multi-
ple thresholds, but we will describe our methodology under
a single threshold for simplicity and discuss the extension in
our application.
3.2 Mixture Model for Bunching and
Non-bunching Distributions
Suppose we observe an independent and identically dis-
tributed observation,Y i fori= 1, . . . , n, wherenis the
number of customers. We assume that there are no bunching
customers outside the neighborhoodN K and they are not af-
fected by the thresholds, namelyY i =Y i(0)forY i ∈N c K,
whereN c K is the complement ofN K. On the other hand,
within the neighborhoodN K, bunching and non-bunching
customers are mixed, that is,Y i =Z iYi(1) + (1−Zi)Yi(0),
whereZ i is an unobserved indicator of bunching (Z i = 1)

and non-bunching (Z i = 0) customers. The key difference
from typical causal inference frameworks is that the binary
indicatorZ i is unobserved. Although a precise estimation of
the indicatorZ i would be difficult, the ATT defined in (1)
can be identified and estimated using a mixture model.
To perform a mixture model, we first assume the forms of
distributions forY i(t). Letg(·|θ)andf(·|γ)be distributions
forY i(0)(non-bunching) andY i(1)(bunching), respectively,
whereθandγare unknown parameters. The bunching dis-
tributionf(·|γ)is expected to exhibit a high density within
NK, allowing us to assign a relatively simple model. In
the numerical examples, we employ a skew-normal distri-
bution (Azzalini 1985), as it offers the flexibility to model
a density peak that may be slightly offset from the thresh-
oldK. On the other hand, the support of the non-bunching
distribution extends over the entire range of the observed
data, so it is appropriate to adopt a flexible model. In our
numerical illustration, we use the Singh-Maddala distribu-
tion (Singh and Maddala 1976), which is widely recognized
for its flexibility and excellent fit to income and expenditure
data (see Appendix A.3 for the density function and adjusted
likelihood).
For the latent binary variableZ i, we assume thatP(Z i =
1) =π= 1−P(Z i = 0), whereπ∈(0,1)is an unknown
mixing parameter. This gives the generative distribution of
Yi as
p(Yi|Ψ) =πf(Y i|γ) + (1−π)g(Y i|θ).(2)
forY i ∈N K, whereΨ ={π, θ, γ}is a set of unknown
parameters. Note that the distribution ofY i can be expressed
asp(Y i|Ψ) =g(Y i|θ)forY i ∈N c K.
Under the formulation (2), the ATT can be expressed as
∆(Ψ)≡
R
y∈NK yf(y|γ)dyR
y∈NK f(y|γ)dy −
R
y∈NK yg(y|θ)dyR
y∈NK g(y|θ)dy .(3)
The above quantity is a simple difference between the ex-
pectations of a bunching and a non-bunching distribution
withinN K. Since we assume that most of the mass den-
sity of the bunching distributionf(y|γ)is included inN K,
the first term of∆(Ψ)will be approximately equal to the
expectation of the density.
3.3 Two-Step Bayesian Inference
In our framework, the supports of bunching and non-
bunching distributions are expected to differ, indicating that
joint estimation of two distributions would be difficult.
Therefore, we first estimate the non-bunching distribution
g(Yi|θ)from the set of observationsD Kc ≡ {Yi;Y i ∈N c K},
and fit the mixture model (2) with estimatedg(Y i|θ), using
the set of observationsD K ≡ {Yi;Y i ∈N K}. In what fol-
lows, we consider a Bayesian approach by assigning a prior
distribution on unknown parameters. Such a Bayesian ap-
proach enables us to obtain point estimates and uncertainty
measures, and is useful for handling heterogeneous treat-
ment effects as considered in the subsequent section.
Regarding the first step, we obtain the posterior distribu-
tion ofθby assigning a prior distributionπ(θ)forθ. Since
g(Yi|θ)has a considerable mass outsideN c K, the likelihood
based on the sampleD c K should be adjusted taking into ac-
count the probability falling intoN c K. We then consider the
following posterior:
p(θ|Dc K)∝p(θ)L(θ;D c K),(4)
whereL(θ;D c K)is the adjusted likelihood given by
L(θ;D c K) = Y
Yi∈N c K
g(Yi|θ)R
y∈N c K g(y|θ)dy .(5)
As the second step, we define the posterior of(π, γ)as
p(π, γ|D) =
Z
p(π, γ|DK, θ)p∗(θ|Dc K)dθ
=p(π, γ)
Z Y
Yi∈NK
p(Yi|Ψ)p∗(θ|Dc K)dθ, (6)
wherep(π, γ)is a joint prior for(π, γ)andp ∗(θ|Dc K)is
a distribution to reflect the information from the poste-
riorp(θ|D c K). A possible example ofp ∗ is a Dirac mea-
sure onθ= ˆθwith ˆθbeing the posterior mean from (4),
which will be used in our numerical examples. The pos-
terior computation of both (4) and (6) can be performed
by the Markov Chain Monte Carlo (MCMC) algorithm us-
ing the probabilistic programming languagestan(Carpen-
ter et al. 2017), which takes advantage of the Hamiltonian
Monte Carlo algorithm (Duane et al. 1987) to sample com-
plex probability distributions efficiently. Given the posterior
samples ofΨ, we can obtain posterior samples of∆(Ψ)de-
fined in (3), which give not only a point estimate but also a
measure of uncertainty such as a90%credible interval.
3.4 Theoretical Analysis
Here, we discuss the theoretical justification of the proposed
two-step Bayesian method in terms of posterior contraction.
Let∆ 0 be the true ATT. We assume that the two models,
f(·|γ)andg(·|θ), are correctly specified, that is, there exists
a true parameterΨ 0 such that∆ 0 = ∆(Ψ0). We also assume
that|D K|=ρn, namely|D c K|= (1−ρ)nfor someρ∈(0,1),
which means that the sample sizes in the neighborhood and
the other region are not highly unbalanced.
Theorem 1.Assume regularity conditions in Appendix A.1.
Undern→ ∞, it holds that
P(|∆(Ψ)−∆ 0|> M n−1/2 | D)→0,
for a large constantM.
The proof is provided in Appendix A.2. Most of the regu-
larity conditions are standard for the model (2) and adjusted
likelihood (5), such as the identifiability of the two density
functions,f(·|γ)andg(·|θ), which is typically required to
establish the posterior contraction rate (Ghosal, Ghosh, and
Van Der Vaart 2000). The above theorem indicates that the
proposed two-step Bayesian method holds posterior conver-
gence to the true value at a rateO(n −1/2). Hence, the in-
formation from the data can be successfully accumulated
according to the sample size. This property is essential to
justify the hierarchical Bayesian formulation in Section 4.

4 Heterogeneous Treatment Effect via
Hierarchical Formulation
The advantage of the proposed Bayesian framework is its
flexibility for model extensions, such as the estimation of
heterogeneous treatment effects. Here, we discuss hierar-
chical Bayesian modeling to estimate heterogeneous treat-
ment effects among customer subgroups. Let customers be
divided intoGsubgroups according to their characteris-
tics (e.g., age and sex), and letY g(t), t∈ {0,1}be the
potential outcomes in thegth subgroup. We assume that
all groups share the same thresholdK. Then, we can de-
fine ATT in each group,∆ g, in the same way as (3). Let
D(g) ={Y gi, i= 1, . . . , ng}be a set of observations in the
gth group.
We assume that the distributions of all the groups belong
to the same family of distributions with different parame-
ters, denoted byf(·|γ g)andg(·|θ g). Then, we consider the
following generative distribution
pg(Ygi|Ψg) =π gf(Y gi|γg) + (1−π g)g(Ygi|θg),(7)
forY gi ∈N K, whereπ g is a heterogeneous mixing propor-
tion. A direct application of the two-step approach given in
the previous section to each group can suffer from instability
when the group-level sample size,n g, is small. Instead, we
consider simultaneous estimation by introducing a random-
effects structureθ g ∼H θ(αθ)andγ g ∼H γ(αγ)with un-
known parametersα θ andα γ. Forπ g, we introduce a logit-
normal distribution, namelylog{π g/(1−π g)} ∼N(µπ, σ2 π)
with unknownµ π andσ 2 π. According to Theorem 1, the
group-specific parameterΨ g can be consistently estimated
asn g increases, making more precise group-level informa-
tion available. Consequently, the shrinkage effect induced by
the random effect becomes weaker whenn g is large, while
it remains strong whenn g is small. This behavior justifies
using random effects, as it allows borrowing strength across
groups adaptively depending on the sample size.
As the first step, the joint posterior ofΘ ={θ 1, . . . , θG}
andα θ based onD c K ={(D (g) K )c, g= 1, . . . , G}is given by
p(Θ, αθ|Dc K)∝p(α θ)
GY
g=1
h(θg|αθ)L(θg; (D(g) K )c),(8)
whereh(θ g|αθ)is the density ofH θ(αθ). In the second
step, the joint posterior ofΨ ={Ψ 1, . . . ,ΨG}andα=
{αγ, µπ, σ2 π}is defined as
p(Ψ, α|D)∝p(α)
GY
g=1
hγ(γg|αγ)hπ(πg|µπ, σ2 π)
×
Z Y
Ygi∈N (g) K
p(Ygi|Ψg)p∗(Ψg|Dc K)dθg,
(9)
whereh γ(γg|αγ)andh π(πg|µπ, σ2 π)are the density func-
tions ofH γ(αγ)andlogit(π g)∼N(µ π, σ2 π), respectively,
andp(α)is a prior distribution.
In our simulation study and application, we use the fol-
lowing Singh-Maddala distribution (Singh and Maddala
1976) for the non-bunching distribution:
g(Ygi|θg) = agqgyag−1
bag g (1 + (Ygi/bg)ag )qg+1 ,
whereθ g = (a g, bg, qg),a g andq g are shape parameters
andb g is a scale parameter. For these parameters, we as-
sume log-normal random effects,log(a g)∼N(µ a, σ2 a),
log(bg)∼N(µ b, σ2 b )andlog(q g)∼N(µ q, σ2 q ), with un-
known parameters,α θ = (µ a, σ2 a, µb, σ2 b , µq, σ2 q ). For the
bunching distribution, we employ the skew-normal distribu-
tion
f(Y gi|γg) = 2 ωg ϕ  Ygi −β g ωg  Φ  δg Ygi −β g ωg  ,
whereγ g = (β g, ωg, δg), which are location, scale, and
skewness parameters, respectively,ϕ(·)andΦ(·)are the
density and cumulative distribution functions ofN(0,1).
For the group-level parameters, we employ random ef-
fects models,β g ∼N(µ β, σ2 β),log(ω g)∼N(µ ω, σ2 ω)
andδ g ∼N(µ δ, σ2 δ )with unknown parametersα γ =
(µβ, σ2 β, µω, σ2 ω, µδ, σ2 δ ). The detailed settings of the prior
distributions are provided in Appendix B. We can again use
stanto generate random samples from the posterior dis-
tributions (8) and (9). Based on the group-level parameters,
Ψg, we can define the group-wise heterogeneous treatment
effect∆(Ψ g)in the same way as (3), and the posterior dis-
tributions of∆(Ψ g)can be approximated by the posterior
samples ofΨ g. This gives point estimates and measures of
uncertainty quantification of∆(Ψ g).
5 Simulation Studies
We demonstrate the effectiveness of our proposed meth-
ods by comparing their performance with the standard RDD
method. We assume that the customer thresholdKis known
and set to 50, and the observed data originate from a popu-
lation structured intoG= 100distinct subgroups. The ob-
served data for each subgroupg(g= 1, . . . ,100)are gen-
erated by a mixture model consisting of a bunching distribu-
tion and a non-bunching distribution, weighted by subgroup-
specific proportionsπ g and1−π g, respectively. The pa-
rameters defining the distributions of components, including
the proportions, can vary from subgroup to subgroup. We
equally dividedGgroups into four clusters and set the same
group-specific sample sizesn g (g= 1, . . . , G) to the same
values within the same clusters. The sample sizes of the clus-
ters are set to (50, 100, 200, 300). We consider two scenar-
ios to evaluate the model performance under different con-
ditions. Scenario (A) assumes moderate bunching with low
heterogeneity across subgroups. In contrast, Scenario (B)
presents a more sparse bunching and higher heterogeneity
than Scenario (A). The detailed simulation settings are de-
ferred to Appendix C.
For the simulated dataset, we fitted the proposed BMTM
and HBMTM models based on 12,000 posterior samples
consisting of four chains each with 3,000 samples af-
ter discarding the first 3,000 samples as burn-in. We use
CmdStanPy(version 1.2.5) for model fitting. The settings

Scenario Method MAE CP AL IS
RDD 3.31 – – –
(A) BMTM 0.78 0.91 4.03 4.65
HBMTM0.330.84 1.201.85
RDD 3.50 – – –
(B) BMTM 1.79 0.94 9.05 9.88
HBMTM0.370.88 1.622.15
Table 1. Simulation results of the proposed and baseline
methods in the subgroup setting. The minimum values of
MAE and IS are shown in bold.
for the prior distributions of BMTM and HBMTM are pro-
vided in Appendix B. Based on the posterior samples, we
computed the posterior means and the90%highest density
interval (HDI) of the group-wise ATT. For comparison, we
also applied an RDD method, which estimates the effect of
treatment by measuring the discontinuity in the probability
density ofYat the thresholdK. This can be achieved by
applying the kernel density estimation separately on either
side ofKand computing the difference between the density
values. In our implementation, a boundary correction tech-
nique for density estimation (Jones 1993) was applied, and
a bandwidth of 10, centered at the thresholdK= 50(cov-
ering the range[40,60]), was used. Note that this RDD does
not provide interval estimates.
The performance of the point estimation is evaluated us-
ing Mean Absolute Error (MAE), defined as
MAE= 1 G
GX
g=1

∆g − b∆g

 ,
Regarding the interval estimation, we use the Cover-
age Probability (CP), Average Length (AL), and Interval
Score (IS) (Gneiting and Raftery 2007), defined as
CP= 1 G
GX
g=1
1(lg ≤∆ g ≤u g),AL= 1 G
GX
g=1
(ug −l g),
IS= 1 G
GX
g=1

(ug −l g) + 2 α (lg −∆ g)1(∆g < lg)
+ 2 α (∆g −u g)1(∆g > ug)  ,
wherel g andu g are the lower and upper bounds of100(1−
α)% HDI for each subgroupg, respectively, and1(·)is the
indicator function. Note thatα= 0.1in our settings. The CP
measures the proportion of true values covered by the inter-
val, with an ideal value of1−α. The IS is a composite met-
ric that jointly evaluates the AL and CP of the interval. The
IS increases when the prediction interval generated by the
model is too broad and increases when the observed value
falls outside of this interval. Table 1 summarizes the above
performance measures averaged over100Monte Carlo repli-
cations.
In both scenarios, our proposed methods, BMTM and
HBMTM, substantially outperform the baseline RDD. In
0 15 30 45 60 75 90
Subgroup
−5
0
5
10
Δg
True BMTM HBMTM
Figure 2: Point estimates and 90% credible intervals of
the subgroup-specific causal effects∆ g by BMTM and
HBMTM.
particular, HBMTM consistently demonstrates superior per-
formance with the lowest MAE and IS, and the superiority
is evident in Scenario (B). In Scenario (B) with a weaker
bunching signal, the accuracy of BMTM degrades (MAE in-
creases from 0.78 to 1.79), while that of HBMTM remains
remarkably stable and accurate. In Scenario (A), although
CP of BMTM is slightly closer to the nominal 90% than that
of HBMTM, HBMTM maintains reliable CP across both
scenarios. These findings demonstrate that the hierarchical
structure of HBMTM successfully borrows strength across
subgroups to deliver highly accurate and precise causal ef-
fect estimates, even when the identifying bunching signal is
weak.
Figure 2 visually contrasts the subgroup-specific causal
effects estimates∆ g from BMTM and HBMTM in Sce-
nario (B). It confirms that the hierarchical model, HBMTM,
consistently provides more accurate point estimates and nar-
rower 90% credible intervals. These visual comparisons fur-
ther emphasize the effectiveness of our proposed HBMTM
method in estimating the threshold’s causal effect on cus-
tomers, even in the presence of small sample sizes within
subgroups.
6 Application to Promotion with Thresholds
in Marketing
In this section, we apply the HBMTM to a real-world dataset
from a marketing promotion in which consumers could earn
incentives by exceeding spending thresholds. A month-long
promotion offered consumers entry into a prize draw for
spending more than 30,000 yen. The winning odds were
tripled for spending more than 50,000 yen, multiplied by five
for spending more than 70,000 yen, and the winners were
announced after the promotion.
Figure 3 shows the histogram of the total payment
amount,Y, per participant during the promotion, with the
thresholds indicated by red lines. As shown in Figure 3,
the distribution ofYis asymmetric, with its peak skewed

0 100k 200k 300k 400k 500k
Y
Frequency
Thresholds Observed Data
Figure 3: Observed distribution of the total payment amount
during the promotion (skyblue) and the three thresh-
olds (red).
to the left and a long and heavy tail extending to the right.
Such a right-skewed, heavy-tailed distribution is a typical
characteristic of expenditure data. We then adopt the Singh-
Maddala distribution for non-bunching distributions, as ex-
plained in Section 4, a flexible three-parameter distribution
for positive-valued data.
In this study, we defined subgroups based on total spend-
ing in the previous month to investigate how the impact of
promotional thresholds varies across customers with differ-
ent baseline spending habits. Defining subgroups based on
prior spending is motivated by the premise that a customer’s
proximity to the promotional thresholds is a key determinant
of their behavioral response. Specifically, we constructed
G= 21subgroups by grouping participants into 10,000
yen intervals based on their previous month’s spending, with
the tier exceeding 200,000 yen treated as a single, top-coded
group.
We applied our proposed method, HBMTM, to this pro-
motion dataset. The detailed settings for the prior distri-
butions of HBMTM are provided in Appendix B.2. Since
the dataset has three threshold values, denoted byK 1 =
30,000, K2 = 50,000andK 3 = 70,000, we first define
DKc by excluding observations that fall within the interval
[20,000,80,000], which represents the combined range of
±10,000 yen around each of the three thresholds. Then we
separately apply the mixture model (2) to each neighbor-
hood,N Km = [K m −10,000, Km + 10,000]form=
1,2,3. Here, we assume that the three thresholds are mu-
tually independent, meaning that the presence of the others
does not influence customers around one threshold.
Figure 4 shows the Singh-Maddala distribution for each
subgroup estimated in the first step of HBMTM. As shown
in Figure 4, the distributional shapes differ significantly
among subgroups. This difference in shape suggests the ex-
istence of significant spending heterogeneity, which in turn
validates our adoption of the highly flexible Singh-Maddala
distribution.
Figure 5 provides the posterior median and 90% HDI for
0 100k 200k 300k 400k 500k
Y
Density
Figure 4: The non-bunching distribution for each subgroup,
estimated using the Singh-Maddala distribution.
each subgroup’s causal effect∆ g across the three thresh-
olds. The results presented in Figure 5 demonstrate a signif-
icant heterogeneity in causal effects across subgroups, with a
consistent trend observed across all thresholds. Specifically,
a clear positive causal effect was observed at every thresh-
old in subgroups where the previous month’s spending was
below or slightly above the threshold (e.g., Group index 1-
4 for K1). For some groups, 90% HDI was entirely within
the positive range, suggesting statistical confidence in the ef-
fect. This positive effect aligns with the intuitive hypothesis
that consumers increase spending to achieve the incentive,
a finding consistent with the hypotheses suggested in exist-
ing marketing research (e.g. Kivetz, Urminsky, and Zheng
2006).
In contrast, a consistent trend of diminishing and eventu-
ally negative causal effects was observed as spending in the
previous month significantly exceeded each threshold (e.g.,
Group index≥6 for K1). This spending-dampening effect
on high-spending subgroups may be explained by the an-
choring effect (e.g. Holst, Hermann, and Musshoff 2015;
Zong and Guo 2022). It is plausible that the relatively low
promotional thresholds acted as a new psychological anchor
for consumers, leading those with higher baseline spending
levels to adjust their expenditures downward, influenced by
this reference point. Although more research is needed to
elucidate the detailed mechanisms underlying these effects,
these results strongly suggest that our proposed method ef-
fectively captures heterogeneous behavioral changes under
threshold manipulation.
7 Concluding Remarks
This study addresses the challenge of estimating the causal
effects of marketing thresholds under strategic customer ma-
nipulation, a scenario where standard RDD and bunching es-
timation methods face significant limitations. To overcome
this issue, we propose BMTM, a novel Bayesian mixture
model framework. This framework robustly estimates causal
effects by modeling the observed spending distribution as
a mixture of two latent distributions: one representing cus-

1 2 3 4 5 6 7 8 9 101112131415161718192021
Group Index
−4000
−2000
0
2000
4000
Δg
(a) Threshold at 30,000
1 2 3 4 5 6 7 8 9 101112131415161718192021
Group Index
−4000
−2000
0
2000
4000
Δg
(b) Threshold at 50,000
1 2 3 4 5 6 7 8 9 101112131415161718192021
Group Index
−4000
−2000
0
2000
4000
Δg
 (c) Threshold at 70,000
Figure 5: Point estimates and 90% credible intervals of each subgroup’s causal effect∆ g obtained by the proposed method
HBMTM at each threshold.
tomers unaffected by the threshold and another representing
those strategically affected. Furthermore, we introduce its
hierarchical extension, HBMTM, which, to our knowledge,
is the first method to provide stable and accurate estimates
of heterogeneous causal effects across customer subgroups,
even with small sample sizes. Our empirical results from
both simulations and a real-world case study demonstrate
the effectiveness of our methods, yielding more accurate
and reliable estimates than conventional approaches. This
study provides a practical tool for data-driven marketing
and contributes a principled approach for causal inference
under strategic manipulation. Future research could explore
more flexible non-parametric models within this framework
and extend its application to other domains where agents re-
spond to algorithmic or policy-based thresholds.
References
Alcantara, R.; Wang, M.; Hahn, P. R.; and Lopes, H.
2024. Modified bart for learning heterogeneous ef-
fects in regression discontinuity designs.arXiv preprint
arXiv:2407.14365.
Azzalini, A. 1985. A class of distributions which includes
the normal ones.Scandinavian journal of statistics, 171–
178.
Bertanha, M.; Caetano, C.; Jales, H.; and Seegert, N. 2024.
Bunching estimation methods.Handbook of Labor , Human
Resources and Population Economics, 1–44.
Carpenter, B.; Gelman, A.; Hoffman, M. D.; Lee, D.;
Goodrich, B.; Betancourt, M.; Brubaker, M. A.; Guo, J.; Li,
P.; and Riddell, A. 2017. Stan: A probabilistic programming
language.Journal of statistical software, 76.
Cattaneo, M. D.; Idrobo, N.; and Titiunik, R. 2024.A practi-
cal introduction to regression discontinuity designs: Exten-
sions. Cambridge University Press.
Duane, S.; Kennedy, A.; Pendleton, B. J.; and Roweth, D.
1987. Hybrid Monte Carlo.Physics Letters B, 195(2): 216–
222.

Franco, S.; and Azzalini, A. 2024. The information matrix of
the bivariate extended skew-normal distribution.METRON,
1–25.
Ghosal, S.; Ghosh, J. K.; and Van Der Vaart, A. W. 2000.
Convergence rates of posterior distributions.Annals of
Statistics, 500–531.
Gneiting, T.; and Raftery, A. E. 2007. Strictly proper scoring
rules, prediction, and estimation.Journal of the American
statistical Association, 102(477): 359–378.
Hahn, J.; Todd, P.; and der Klaauw, W. V . 2001. Identifica-
tion and Estimation of Treatment Effects with a Regression-
Discontinuity Design.Econometrica, 69(1): 201–209.
Holst, G. S.; Hermann, D.; and Musshoff, O. 2015. An-
choring effects in an experimental auction – Are farmers an-
chored?Journal of Economic Psychology, 48: 106–117.
Imbens, G. W.; and Rubin, D. B. 2015.Causal inference
in statistics, social, and biomedical sciences. Cambridge
university press.
Ishihara, T.; and Sawada, M. 2024. Manipulation-Robust
Regression Discontinuity Designs. arXiv:2009.07551.
Jones, M. C. 1993. Simple boundary correction for kernel
density estimation.Statistics and computing, 3: 135–146.
Kivetz, R.; Urminsky, O.; and Zheng, Y . 2006. The Goal-
Gradient Hypothesis Resurrected: Purchase Acceleration, Il-
lusionary Goal Progress, and Customer Retention.Journal
of Marketing Research, 43(1): 39–58.
Kleven, H. J.; and Waseem, M. 2013. Using Notches to
Uncover Optimization Frictions and Structural Elasticities:
Theory and Evidence from Pakistan *.The Quarterly Jour-
nal of Economics, 128(2): 669–723.
Lee, D. S. 2008. Randomized experiments from non-random
selection in U.S. House elections.Journal of Econometrics,
142(2): 675–697. The regression discontinuity design: The-
ory and applications.
Mahmoud, M. R.; and Abd El-Ghafour, A. S. 2015. Fisher
information matrix for the generalized Feller-Pareto distri-
bution.Communications in Statistics-Theory and Methods,
44(20): 4396–4407.
McCrary, J. 2008. Manipulation of the running variable in
the regression discontinuity design: A density test.Journal
of Econometrics, 142(2): 698–714. The regression disconti-
nuity design: Theory and applications.
Nastasoiu, A.; Bendle, N. T.; Bagga, C. K.; Vandenbosch,
M.; and Navarro, S. 2021. Separating customer heterogene-
ity, points pressure and rewarded behavior to assess a retail
loyalty program.Journal of the Academy of Marketing Sci-
ence, 49: 1132–1150.
Rubin, D. B. 1974. Estimating causal effects of treatments
in randomized and nonrandomized studies.Journal of edu-
cational Psychology, 66(5): 688.
Saez, E. 2010. Do Taxpayers Bunch at Kink Points?Amer-
ican Economic Journal: Economic Policy, 2(3): 180–212.
Singh, S. K.; and Maddala, G. S. 1976. A Function for Size
Distribution of Incomes.Econometrica, 44(5): 963–970.
Slemrod, J. 2013. Buenas notches: lines and notches in tax
system design.Ejtr, 11: 259.
Sugasawa, S.; Ishihara, T.; and Kurisu, D. 2023. Hierar-
chical Regression Discontinuity Design: Pursuing Subgroup
Treatment Effects.arXiv preprint arXiv:2309.01404.
Tao, K.; Wang, Y . S.; and Ruppert, D. 2025. Bayesian anal-
ysis of regression discontinuity designs with heterogeneous
treatment effects.arXiv preprint arXiv:2504.10652.
Thistlethwaite, D. L.; and Campbell, D. T. 1960.
Regression-discontinuity analysis: An alternative to the ex
post facto experiment.Journal of Educational psychology,
51(6): 309.
Van der Vaart, A. W. 2000.Asymptotic statistics, volume 3.
Cambridge university press.
Zong, Y .; and Guo, X. 2022. An Experimental Study on
Anchoring Effect of Consumers’ Price Judgment Based on
Consumers’ Experiencing Scenes.Frontiers in Psychology,
V olume 13 - 2022.

A Technical Details
A.1 Regularity conditions
We introduce the regularity conditions required for the proof
of Theorem 1. In what follows, we defineKL(p(x)∥q(x))as
the Kullbuck-Leibler divergence between two density func-
tions,p(x)andq(x), defined as
KL(p(x)∥q(x)) =
Z
p(x) log
 p(x)
q(x)

dx
We first define the adjusted likelihood for a single observa-
tion as
L(x|θ) = g(x|θ)R
y∈N c K g(y|θ)dy .
To establish the posterior contraction rate given in Theo-
rem 1, we assume the following regularity conditions:
(C1) The parameter space ofΦis compact and the trueΦ 0 =
{π0, θ0, γ0}is an interior point of the space.
(C2) The adjusted likelihood functionL(x|θ), non-bunching
distributiong(x|θ), and the bunching distributionf(x|γ)
are second-order continuously differentiable.
(C3) For allγ̸=γ 0 andθ̸=θ 0, it holds that
KL(g(x|θ0), g(x|θ))>0andKL(f(x|γ 0), f(x|γ))>
0.
(C4) The Fisher information matrices
E
 ∂logg(Y|θ)
∂θ
∂logg(Y|θ)
∂θ ⊤

E
 ∂logf(Y|γ)
∂γ
∂logf(Y|γ)
∂γ ⊤

are both positive definite.
(C5) There existδ >0such that a prior distribution forΨ
satisfiesinf ∥Ψ−Ψ0∥<δ π(Ψ)>0.
(C6) For anyγandθ,KL(f(x|γ)∥g(x|θ))>0.
(C7) The surrogate posteriorp ∗(θ| Dc K)is a continuous map-
ping of the original posteriorp(θ| D c K)with respect to
the topology of weak convergence.
(C8)τ(Ψ)is a continuously differentiable function ofΨ.
Conditions (C1)-(C5) are the standard conditions for
establishing the contraction rate of posterior distributions
(Van der Vaart 2000; Ghosal, Ghosh, and Van Der Vaart
2000). Condition (C6) ensures that the mixture model is
identifiable. Condition (C7) is satisfied by, for example, set-
tingp ∗ to a Dirac measure on the posterior mean, as used
in our simulation and application. Condition (C8) is needed
to establish posterior convergence given the convergence of
the posterior ofΨ.
In our simulation and application, the Singh-Madala and
skew-normal distributions forg(y|θ)andf(y|γ), respec-
tively. The properties of the Fisher information matrices of
these distributions have been investigated in Mahmoud and
Abd El-Ghafour (2015) for the Singh-Madala distribution
and in Franco and Azzalini (2024) for the skew-normal dis-
tribution.
A.2 Proof of Theorem 1
Under conditions (C1)-(C5), the posterior distribution
p(θ|Dc K)holds posterior contraction
P(∥θ−θ 0∥≥M 1n−1/2 | Dc K)→0
asn→ ∞for a constantM 1 >0(e.g. Ghosal, Ghosh, and
Van Der Vaart 2000). Then, we also obtain the same poste-
rior contraction result for the surrogate posteriorp ∗(θ|Dc K)
from (C7).
Given the true value ofθ0, the mixture model is expressed
as
p(y|π, γ) =πf(y|γ) + (1−π)g(y|θ 0).
It holds that
a(y|π, γ)≡ ∂logp(y|π, γ) ∂π = f(y|γ)−g(y|θ 0) p(y|π, γ)
b(y|π, γ)≡ ∂logp(y|π, γ) ∂γ = π·∂f(y|γ)/∂γ p(y|π, γ)
Then, the Fisher information matrixI(π, γ)is given by
I(π, γ) =
 Iππ Iπγ
I ⊤ πγ Iγγ

,
where
Iππ =E[a(Y|π, γ) 2], Iπγ =E[a(Y|π, γ)b(Y|π, γ)],
Iγγ =E[b(Y|π, γ)b(Y|π, γ)⊤.
To state thatI(π, γ)is positive definite, it is sufficient
to show that (i)I γγ is positive definite and (ii)I ππ −
Iπγ I −1 γγ I ⊤ πγ >0. For (i),I γγ can be expressed as
Iγγ =E
" πf(Y|γ)
p(Y|π, γ)
2
· ∂logf(Y|γ) ∂γ · ∂logf(Y|γ) ∂γ ⊤
#
.
From (C4), it holds thatE[(c ⊤∂logf(Y|γ)/∂γ) 2]>0for
an arbitrary non-zero vectorc. This indicates that the func-
tionc ⊤∂logf(y|γ)/∂γis not identical to0. Hence, we have
c⊤Iγγ c=E
" πf(Y|γ)
p(Y|π, γ)
2
·

c⊤ ∂logf(Y|γ) ∂γ 2# >0.
Moreover, the condition (ii) follows from the Cauchy-
Schwarz inequality and the fact thata(y|π, γ)andb(y|π, γ)
are not linearly dependent under the identifiability condition
(C6). Hence, the Fisher information matrixI(π, γ)is posi-
tive definite, which leads to the posterior contraction of the
conditional posterior distributionp(π, γ|DK, θ0)
P(∥(π, γ)−(π 0, γ0)∥≥M 2n−1/2)→0
asn→ ∞for a constantM 2 >0.
LetA n ={(π, γ)| ∥(π, γ)−(π0, γ0)∥> M2n−1/2}. Let
p(An|D)be the marginal posterior probability ofA n, and
letp(A n|DK, θ)be its conditional posterior probability. It
holds that
p(An|D) =
Z
p(An|DK, θ)p∗(θ|Dc K)dθ
=
Z
∥θ−θ0∥≤ϵn
p(An|DK, θ)p∗(θ|Dc K)dθ
+
Z
∥θ−θ0∥>ϵn
p(An|DK, θ)p∗(θ|Dc K)dθ,

whereϵ n =M 1n−1/2. The second term is bounded by the
posterior probability of the event∥θ−θ 0∥> ϵn, which goes
to0asn→ ∞due to the posterior contraction ofp ∗(θ|Dc K).
For the first term, we first note that
sup
∥θ−θ0∥≤ϵn
|p(y|π, γ, θ)−p(y|π, γ, θ0)|≤C 1ϵn,
for a constantC 1 >0and arbitraryy,πandθ, from (C1)
and (C2). This leads to
sup
∥θ−θ0∥≤ϵn
|p(π, γ|DK, θ)−p(π, γ|DK, θ0)|≤C 2ϵn
for a constantC 2 >0and arbitraryπandθ. Then, it follows
thatZ
∥θ−θ0∥≤ϵn
p(An|DK, θ)π∗(θ|Dc K)dθ
≤
Z
∥θ−θ0∥≤ϵn
|p(An|DK, θ)−p(An|DK, θ0)|π∗(θ|Dc K)dθ
+
Z
∥θ−θ0∥≤ϵn
p(An|DK, θ0)|π∗(θ|Dc K)dθ
≤C 2εn +p(A n|DK, θ0),
which goes to0asn→ ∞, from the posterior contrac-
tion of the conditional posterior. Therefore, it holds that
π(An|D)→0asn→ ∞, which completes the proof from
(C8).
A.3 Singh-Madala distribution and its adjusted
likelihood
The Singh-Madala distribution is a flexible three-parameter
distribution on the positive real line, often used to model
economic data such as income and expenditure. The param-
eter vector is denoted asθ= (a, b, q), whereaandqare
shape parameters, andbis a scale parameter. The probabil-
ity density function is given by
g(y|θ) = aqy a−1
ba(1 + (y/b)a)q+1 , y >0.
In addition, its distribution function is given by
G(y|θ) = 1−

1 +
 y
b
a−q
, y >0.
Hence, the adjusted likelihood function underN K = [K−
a, K+a]for somea∈(0, K)is obtained as
L(θ;D c K) = Y
Yi∈Dc K
g(Yi|θ)
1−G(K+a|θ) +G(K−a|θ) .
B Prior Specifications
B.1 Prior distributions for BMTM and HBMTM
in simulation studies
For the first step model of BMTM, the prior for each element
of the unknown parameter vectorθ= (a, b, q)is specified
as follows:
log(a),log(b)∼N(0,1.5 2), q∼N(log(40),1).
For the second step model of BMTM, the priors for the un-
known parametersγ= (β, ω, δ)andπare specified as fol-
lows:
ω∼N(0,10 2), δ∼N(0,2 2),log
 π
1−π

∼N(0,1.5 2).
For the location parameterβof the skew-normal distribu-
tion, we setβ=K. This specification reflects the prior be-
lief that the location of the bunching distribution is at the
thresholdK.
For HBMTM, the priors for the unknown parameterαθ =
(µa, σ2 a, µb, σ2 b , µq, σ2 q )in the first step model are specified
as follows:
µa ∼N(0,2.5 2), µb ∼N(3,2 2), µq ∼N(0,2.5 2),
σa, σb, σq ∼N +(0,1),
whereN +(·)denotes a half-normal distribution, a truncated
normal distribution with a lower bound of 0. The priors for
the unknown parameter in the random effects distributions
for the heterogeneous mixing proportionπ g and the skew-
normal parameters are specified as follows:
µω ∼N(2,1), µ δ ∼N(0,1), µ π ∼N(0,1.5 2),
σω, σδ, σπ ∼N +(0,1).
For the heterogeneous location parameterβ g, we set its hy-
perparameters toµ β =Kandσ β = 0, which implies that
βg =Kfor allg= 1, . . . , G. This choice reflects the prior
belief that the location of the bunching distribution for every
group is at the thresholdK.
B.2 Prior distributions for HBMTM in
real-world application
For the first step model, the priors for the unknown parame-
tersα θ = (µa, σ2 a, µb, σ2 b , µq, σ2 q )are specified as follows:
µa ∼N(1,1), µ b ∼N(10,2 2), µq ∼N(0,1),
σa ∼N +(0.5,1), σ b ∼N +(10,2 2), σq ∼N +(0,1).
For the second step model, the priors for the unknown pa-
rameters of the random effects distributions for the hetero-
geneous mixing proportionπ g and the skew-normal param-
eters are specified as follows:
µπ ∼N(2,1), µ ω ∼N(7,0.5 2), µδ ∼N(0,1),
σπ ∼N +(0,0.5 2), σω ∼N +(0,1), σ δ ∼N +(0,0.5 2).
As in the simulation, we set the parameters for the heteroge-
neous location parameterβ g toµ β =Kandσ β = 0, which
implies thatβ g =Kfor allg= 1, . . . , G. This specifica-
tion reflects the prior belief that the location of the bunching
distribution is at the thresholdK.
C Supplementary Details of Numerical
Studies
C.1 Details of data generating process in
simulation studies
The data for our simulation studies are generated from the
hierarchical model described in Section 4. The parameter

settings for the bunching and non-bunching distributions,
which are common to both scenarios (A) and (B), are as fol-
lows:
ωg ∼N(µ ω, σ2 ω), δg ∼N(µ δ, σ2 δ ), ag ∼N +(µa, σ2 a),
bg ∼N +(µb, σ2 b ), qg ∼N +(µq, σ2 q ),
where the hyperparameters are drawn from:
µω ∼N(3,0.1 2), µδ ∼N(4,0.1 2), µa ∼N(3.5,0.1 2),
µb ∼N(39,1), µ q ∼N(1.5,0.1 2), σb ∼N +(2,1),
σω, σδ ∼N +(0.5,0.1 2), σa, σq ∼N +(0.2,0.1 2),
The location parameter for the bunching,β g, is fixed in the
thresholdKfor all groups.
The two scenarios differ only in the heterogeneous mix-
ing proportionπ g. Assuming thatlog{π g/(1−π g)} ∼
N(µ π, σ2 π), the settings for each scenario are as follows:
Scenario (A):µ π ∼N(−2,0.1 2), σπ ∼N +(0.5,0.1 2),
Scenario (B):µ π ∼N(−4,0.1 2), σπ ∼N +(1.5,0.1 2).
Scenario (A) represents a case where the mixing proportion
of the bunching component is moderate and exhibits low het-
erogeneity across groups. In contrast, Scenario (B) features
a more sparse bunching component (i.e.,low mixing pro-
portion) but with higher heterogeneity than Scenario (A). By
comparing these two scenarios, we examine how the model’s
performance is affected by the overall share of the bunching
component and the degree of its cross-group heterogeneity.
C.2 Validation of the bunching region
To validate this model specification, we verify that the esti-
mated bunching distribution has a negligible density outside
this region. Our proposed method assumes that the bunch-
ing is fully contained within the bunching regionN Km =
[Km −10,000, Km + 10,000]form= 1,2,3. Specifically,
we confirm that the density is zero at the endpoints of the
interval,K m ±10,000.
We present the case forK 2 = 50,000as a representa-
tive example. Specifically, for the bunching distribution esti-
mated for each subgroup, we calculated its probability den-
sity at the two endpoints ofN K2: 40,000 and 60,000. Fig-
ure A6 shows violin plots of these density values at two
endpoints across all subgroups. As shown in Figure A6, the
distributions of the density values in both (a) the lower and
(b)the upper bounds are concentrated at nearly zero. These
results indicate that the estimated bunching distribution has
negligible leakage outside the boundaries of the bunching
regionN K2. Therefore, these results support the model’s as-
sumption that the bunching effect is limited to the interval
[Km−10000, Km+10,000], thus justifying the model spec-
ification.
C.3 Sensitivity analysis on the prior in real-world
application
In this section, we present a sensitivity analysis to assess
the robustness of our findings to the prior specification for
the bunching location parameter,β g. Our primary analy-
sis (See Section 6) fixed this parameter at the thresold for
−0.2
0.0
0.2
0.4
0.6
0.8
1.0
1.2
Density
1e−10
(a) Lower bound
0.0
0.5
1.0
1.5
2.0Density
1e−8
(b) Upper bound
Figure A6: Distribution of bunching regionN Km endpoints
across subgroups (Threshold: 50,000). Violin plots show the
estimated (a) lower and (b) upper bounds of the region.
all groups (i.e.,β g =K) described in Section B.2. Here,
we relax this fixed assumption and instead adopt the follow-
ing hierarchical prior, which allowsβg to vary across groups
with a mean ofK:
µβ =K, σ β ∼N +(0,1000 2).
Figure A7 provides the estimated causal effects∆ g for
each subgroup under this alternative specification. As shown
in Figure A7, our sensitivity analyses confirm this primary
finding. First, a clear positive causal effect was consistently
observed in all model specifications for subgroups with
prior-month spending near or slightly above the threshold.
For some of these groups, the 90% HDI remained entirely in
the positive range, suggesting that the effect is statistically
robust. Second, the trend of diminishing effects for high-
spending subgroups also proved robust, though this pattern
was prominent at the K1 and K3 thresholds and less appar-
ent at the K2 threshold. Therefore, the qualitative conclu-
sions from our main analysis hold under this alternative prior
specification.

1 2 3 4 5 6 7 8 9 101112131415161718192021
Group Index
−4000
−2000
0
2000
4000
6000
8000
Δg
(a) Threshold at 30,000
1 2 3 4 5 6 7 8 9 101112131415161718192021
Group Index
−4000
−2000
0
2000
4000
6000
8000
Δg
(b) Threshold at 50,000
1 2 3 4 5 6 7 8 9 101112131415161718192021
Group Index
−4000
−2000
0
2000
4000
6000
8000
Δg
 (c) Threshold at 70,000
Figure A7: Point estimates and 90% credible intervals of∆ g obtained by the proposed method HBMTM at each threshold
under the alternative prior specification.
