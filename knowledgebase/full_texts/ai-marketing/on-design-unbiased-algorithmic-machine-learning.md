---
title: On design-unbiased algorithmic Machine Learning
url: https://arxiv.org/abs/2606.28795
category: ai-marketing
subcategory: measurement
date: 2026-06
venue: ''
authors:
- Li-Chun Zhang
- Siu-Ming Tam
- Luis Sanguiao-Sande
- Wesley Yung
- Anders Holmberg
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.28795
pages: 26
chars: 53525
fetched_at: '2026-11-08T13:27:27+00:00'
kb_version: 1
---

# On design-unbiased algorithmic Machine Learning

On design-unbiased algorithmic
Machine Learning
Li-Chun Zhang∗, University of Southampton & Statistisk sentralbyrå
Siu-Ming Tam, Australian Bureau of Statistics
Luis Sanguiao-Sande, Instituto Nacional de Estadística
Wesley Yung, Statistics Canada (Ret.)
Anders Holmberg, Australian Bureau of Statistics
Abstract
Machine Learning (ML) algorithms, such as k-Nearest Neighbours (kNN)
or random forest, eschew the ideal of true data models in favour of pre-
dictive performance. However, minimising the MSE or F-score cannot lead
to unbiasedness directly, which is important in many situations such as
official statistics. We study the conditions of algorithmic ML, other than
the existence and knowledge of true data models, which lead to unbiased
prediction or classification for a given finite population, including how the
training data may be sampled from the population, how a trained predic-
tion algorithm can be tuned to achieve unbiased prediction or classification
for that population, and how the performance of out-of-sample prediction
or classification can be assessed unbiasedly. The inference is based on the
knownprobability design of samples and training sets, rather than any
assumeddistributions or models.
Key wordspq-design, prediction estimator, debiasing, classification accuracy
1 Introduction
Breiman (2001a) contrasts algorithmic and data modelling cultures, where the
ideal of true data models is eschewed in favour of predictive performance of ML
algorithms, such as kNN or random forest. However, minimising the MSE or F-
scorecannotdirectlyleadtounbiasednessofpredictionorclassification, which
is important in many finite-population applications of ML.
For instance, many official statistics are defined as descriptive summaries
of a country’s population, economy, society or environment. While the quality
of official statistics is multi-dimensional (e.g. United Nations, 2019; European
∗Correspondence: Department of Social Statistics and Demography, Univ. of Southampton,
Highfield SO17 1BJ, Southampton, UK. Email: L.Zhang@soton.ac.uk
1
arXiv:2606.28795v1  [cs.LG]  27 Jun 2026

Commission, 2017; Statistics Canada, 2017), accuracy and reliability as mea-
sured in terms of bias and variance, respectively, are central in all the quality
frameworks necessary to maintain the public trust.
As a common approach to producing official statistics, survey sampling
shares Breiman’s perspective on ML algorithms. The focus is to improve the
sampling strategy, consisting of a probability sampling design and an associ-
ated choice of estimator (Neyman, 1934). The inference is with respect to the
known sampling design, regardless of the existence or knowledge of a true data
model. See Hansen (1987), Smith (1994), Kalton (2002), Rao (2005, 2011),
Beaumont and Haziza (2022) for reviews and appraisals.
Thewell-knownHorvitz-Thompsonestimator(HorvitzandThompson, 1952)
is the most typical example, which is exactly unbiased over repeated sampling
from a given population. To improve the efficiency by leveraging auxiliary in-
formation about the population, i.e. in addition to the sampling design, it is
popular to adopt a design-based model-assisted approach (e.g. Särndal et al.,
1992), whereby a prediction model relating the target outcome to the known
covariates can be introduced to adjust the Horvitz-Thompson estimator, but
the inference of bias and variance is still with respect to the sampling design,
without the need for the assisting model to be the true data model.
Breidt and Opsomer (2017) summarise a general “recipe” of model-assisted
estimation, which adjusts the model-prediction of the population total by the
weighted sum of sample prediction residuals, where the weights are inverse
sample inclusion probabilities as in the Horvitz-Thompson estimator.
In case the assisting model is pre-trained, i.e. not learned on the actual
sample, the resulting difference estimator (e.g. Särndal et al., 1992, Sec. 6.3)
is exactly design-unbiased. See also Angelopoulos et al. (2023) for a related
approach to independent and identically distributed (IID) samples, either by
stipulation or by with-replacement sampling from finite populations.
Otherwise, and more common in practice, estimating the model means that
the resulting estimator is no longer exactly unbiased. To justify any given ML
algorithm in this context, some authors resort to the notation of consistency
asymptotically, as the population and sample sizes increase to infinity, un-
der suitable regularity conditions. See McConville and Toth (2019) for regres-
sion trees generated by the recursive partitioning algorithm, or Dagdoug et al.
(2023) for random forest by the original algorithm of Breiman (2001b).
However, as Smith (1994) points out, the “asymptotic notion of consistency”
is not immediately applicable to the given population as “a real entity”. One
may observe an alternative notion of consistency following the works of Fisher
(1956) and Neyman (1934). For a given population and sampling method, ifˆθ
is unbiased for the vector of population totalsθ, theng(ˆθ)is called “consistent”
forg(θ)by Fisher (1956); whereas an interval estimator of a population statis-
tic is called “consistent” by Neyman (1934), if it achieves the designated level
of coverage. Zhang et al. (2025) refer to such finite-sample design-unbiased
estimators asNeyman-Fisher consistent.
Sanguiao-Sande and Zhang (2021) propose an approach to Neyman-Fisher
consistent population total estimation, which is exactly design-unbiased in the
finite-sample setting. In particular, given any ML algorithm as the assisting
2

model, one can apply Rao-Blackwellisation (Rao, 1945; Blackwell, 1947) to the
Horvitz-Thompson estimator of the total prediction errors in the population
outside the training set to achieve design-unbiasedness. The resulting estima-
tor still uses the sampling design weights explicitly, like all other traditional
design-based model-assisted estimators.
Zhang et al. (2025) extend thesubsampling Rao-Blackwell (SRB)technique
of Sanguiao-Sande and Zhang (2021) to a larger class of estimators, called the
prediction estimators(Royall, 1970; Valliant et al., 2000), where a prediction
estimator of a population total is the sum of the observed sample total and a
predicted out-of-sample total. Since one can plug in any ML algorithm for the
latter, the prediction estimator can be constructed by a working model of the
population without using the sampling weights at all, although doing so would
often cause bias over repeated sampling from the given population. Applying
Rao-Blackwellisation to the subsample-trained prediction estimator, Zhang et
al. (2025) obtain exactly design-unbiased estimators of the bias and MSE of
the resulting SRB-prediction estimators.
However, Zhang et al. (2025) did not study the general conditions of ML that
can lead to design-unbiased prediction estimators. Nor did they consider the
estimation of classification accuracy when the prediction estimator is given by
unit-level classifications of the out-of-sample units.
In this paper, we shall focus on the conditions of ML under finite population
sampling, which would yield design-unbiased estimation of population totals,
either by predicting or classifying the out-of-sample units. Since the inference
is design-based, the unbiasedness holds regardless of the ‘truthfulness’ of the
assisting model or ML algorithm. This is especially useful in applications of
ML, where unbiasedness for finite populations is of critical importance.
The specific questions we consider are: (i) how the training data may be
sampled from the population, so as to enable the inference of out-of-sample
prediction errors based on the observed in-sample test errors, (ii) how an ML
algorithm, which is formed by the training data, can be tuned by the test errors
to yield design-unbiased out-of-sample prediction, and (iii) how out-of-sample
unit-level classification can yield design-unbiased prediction estimation, and
how to assess the associated classification accuracy unbiasedly.
In the rest of the paper, Sections 2 and 4 deal with unbiased prediction and
classification, respectively. Sections 3 and 5 present illustrations, simulations
and an application of the theory developed, using kNN as the example ML
algorithm throughout. Section 6 gives concluding remarks.
2 Design-unbiased prediction
Denote byU={1, ..., N}a given finite population, with known feature vectorxi
for eachi∈U. Denote bysthe sample ofnunits with observedoutcomey i for
eachi∈s, whereasy i is unknown for the rest of the population. We treat all
the values{(y i, xi) :i∈U}as constants, whether they are known or not. The
variation of ML and prediction is due to the following two elements.
First, let the samplesbe selected fromUby a probability sampling design,
3

to be referred to as thep-designand denoted by
s∼p(s)
wherep(s)sums to 1 over all possibles, andπ i = Pr(i∈s)>0for anyi∈U.
Next, for algorithmic ML, lets1 be thetrainingset taken froms, and lets2 =s\s 1
be the correspondingtestset, which are created according to a specific design,
to be referred to as theq-designand denoted by
s1 ∼q(s 1 |s).
For instance,s 1 of sizen 1 may be selected fromsby simple random sampling
without replacement — simply SRS from now on. Or,s 1 may be created by
bootstrap ofs, in which case a given unit insmay be selected multiple times
ins 1, ands 2 contains the units insnot selected tos 1 at all. Or, byL-folding,
one would createLtest setss 2 by a randomL-partition ofs, and theLtraining
setss 1 =s\s 2 are determined accordingly.
In any case, we consider thepq-design to be well-defined for inference, if the
joint distribution of(s1, s)admits the factorisation
q(s1 |s)p(s) =f(s 1)f(s|s 1)(1)
such that the non-empty test sets2 can be regarded as a probability sample
fromU\s 1 conditional ons 1. Notice that the trivialq-design,Pr(s 1 =s|s) = 1,
does not yield a well-definedpq-design sinces2 ≡ ∅, although it is feasible for
ML with default setups, such as kNN with pre-fixedk. Well-definedpq-designs,
however, are necessary for the inference of ML.
As a typical target of interest, let us consider the populationy-total, which
can be decomposed into the observed sample total and the unknown total in
the rest of the population, denoted by
Y=
X
i∈U
yi =
X
i∈s
yi +
X
i /∈s
yi =
X
i∈s
yi +Y R
where the subscript denotesR=U\s. Let aprediction estimatorofYbe
ˆY= X
i∈s
yi +
X
i /∈s
ˆyi =
X
i∈s
yi + ˆYR
whereˆyi can be given by any ML prediction or classification algorithm.
In particular, as the out-of-sample totalY R varies withsunder repeated
samplings∼p(s), unbiased estimation ofY(as a constant) is equivalent to
unbiased prediction ofYR (as a random variable), denoted by
Ep( ˆY) =Y⇔E p( ˆYR −Y R) = 0.
4

2.1 Representative training
Denote byµ(x, s1)a predictor obtained from the training data{(yj, xj :j∈s 1},
which is aimed at the outcomey-value given the associated feature vectorx.
The notation signifies that, for any unit outside the training set,i /∈s1 with
xi =x, its predictedy-valueµ(x, s 1)varies only withxands 1.
DefinitionA well-definedpq-design is said to yieldrepresentative trainingof
µ(x, s1)if,∀i∈U, we have
Epq

µ(xi, s1)|i∈s 2

=E pq

µ(xi, s1)|i /∈s

.(2)
In other words, representative training is the case, by the givenpq-design,
if the expected predictorµ(x i, s1)is the same for any uniti∈Uconditional
on its being outside the training set, regardless whether the unit needs to be
predicted (i.e.i /∈s) or is observed and may be used for inference (i.e.i∈s2).
For simplicity, we shall say a unitiisout-of-bag (OOB)if it is in the sample but
outside the training set, i.e.i∈s 2, whereas it is out-of-sample ifi /∈s.
The concept of representative training (2) is intuitive, since it allows one to
connect the unobserved out-of-sample performance ofµ(x, s1)to its observed
in-sample OOB performance. For instance, conditional ons1, all the prediction
errorsµ(x i, s1)−y i can be partitioned according toU\s 1 =s 2 ∪R, wheres 2 is a
sample fromU\s 1 with respect to thepq-design, which would allow us to make
inference of the prediction bias ofˆYR = P i∈R µ(xi, s1)later.
Lemma 1.A well-definedpq-design yields representative training,
•for all possible ML algorithmsµ(x, s1)if and only if,∀i∈U, we have
π2i := Pr(i∈s 2 |s 1) = πi −Pr(i∈s 1) 1−Pr(i∈s 1) I(i /∈s1)(3)
•for any given ML algorithmµ(x, s1)if and only if,∀i∈U, we have
Covs1

µ(xi, s1), π2i |i /∈s1

= 0.(4)
The proof is given in Appendix A, as are the proofs of other results in the
paper. Since condition (3) implies (4), the latter may be regarded as a more
generalconditionforrepresentativetraining: itmeansthatanywell-definedpq-
design may yield representative training of certain models, i.e. those satisfying
(4). However, one may be unable to verify the condition (4), which requires all
the relevant unconditional and conditional sampling probabilities to be known.
The condition (3) is thus more readily applicable, given which thepq-design
guarantees representative training ofallpossible ML algorithms.
Corollary 1.GivensbySRSfromUands 1 bySRSfroms, theSRS-SRSpq-design
satisfies(3).
Example 1.LetU={i 1, i2, i3, i4}, and(n, n1) = (2,1)for the SRS-SRSpq-design.
We haveπ2i = n−n1 N−n 1 = 1 3,∀i∈U, which satisfies(3)sinceπ i = 2 4 andPr(i∈s 1) = 1 4.
5

•Giveni 1 ∈s 2, we haves={i 1, i2},{i 1, i3},{i 1, i4}, yielding 3 distinct training
setss 1 ={i 2},{i 3},{i 4}withouti 1, each with probabilityf(s1 |i 1 ∈s 2) = 1 3.
•Giveni 1 /∈s, we haves={i2, i3},{i 2, i4},{i 3, i4}, yielding 3 distinct training sets
s1 ={i 2},{i 3},{i 4}, eachwithprobabilityf(s 1 |i 1 /∈s) =1 3. Noticethatthesame
training set can occur in differentswithouti1, such ass1 ={i 2}ins={i 2, i3}
ors={i 2, i4}, but the probability ofs1 ={i 2}is still 2 6 = 1 3.
It is clear that, given anyµtrainable ons1, the expectation ofµ(xi, s1)is the same,
either conditional oni∈s 2 ori /∈s, for anyi∈U, i.e. representative training.
Apart from SRS, it is common to generate(s1, s2)byL-folding or bootstrap
sampling. ForL-folding, suppose (i)n 2 =n/Lis an integer given the sample
sizenofs, and (ii) theLsets ofs 2 are drawn sequentially fromsby SRS. We
would then have the samef(s1)by SRS-L-folding as by the SRS-SRSpq-design,
and representative training of all possibleµ(x, s1); whereas, without (i) and (ii),
representative training can be the case approximately.
Next, when(s1, s2)are given by bootstrap sampling ofs, the probabilityf(s1)
would depend on the number of distinct units ins1, denoted bym, as well as
their realised frequencies ins1. The expected frequency is the same for each
distinctunit, anditiswellknownthatm/ntendsto1−e −1 asnincreases. Bythe
symmetry of this SRS-bootstrappq-design,π 2i = Pr(i∈s 2 |s 1)is approximately
a constant fori /∈s 1, given sufficiently largen, and we have approximately
representative training for all possibleµ(x, s1).
Corollary 2.Letsbe given by Poisson sampling fromU, ands 1 by Bernoulli
sampling froms. The Poisson-Bernoullipq-design satisfies(3).
Corollary 2 suggests that, for an unequal-probabilityp-design with fixed
sample sizen, a negligible sampling fractionn/Ncan yield approximately rep-
resentative training as long as one adopts an equal-probabilityq-design.
2.2 Prediction unbiasedness and tuning
The set of out-of-sample unitsR=U\svaries withs∼p(s). The predictor
µ(x, s1)obtained froms 1 ispq-unbiased for out-of-sample prediction, if
Epq
 X
i∈R
µ(xi, s1)

=E p
 X
i∈R
yi

(5)
over all the out-of-sample units. We leave it to future studies to investigate if
design-unbiased prediction of unit-specificyi can be achieved sensibly.
Below we provide a sufficient condition for (5) given representative training
bypq-design. Consequently, we show how it can be used totunethe given
µ(x, s1)to achieve unbiased prediction.
Proposition 1.Given representative training ofµ(x, s1)by thepq-design, it is
pq-unbiased for out-of-sample prediction(5)if, for anys∼p(s), we have
X
i∈s
 1
πi −1

Eq

µ(xi, s1)|i∈s 2

=
X
i∈s
 1
πi −1

yi.(6)
6

Corollary 3.Under the SRS-SRSpq-design, the predictorµ(x, s1)ispq-unbiased
for out-of-sample prediction if, for anys∼p(s), we have
X
i∈s
Eq

µ(xi, s1)|i∈s 2

=
X
i∈s
yi.(7)
Theq-benchmarkingcondition (6) is stated for the given samples, without
any unobservedy-values. It is likely that the equality will not hold exactly in
practice, unless the predictor is rather simplistic, such as training-set mean
given an SRS-SRSpq-design. Although this does not imply that the predictor
µ(x, s1)must be biased, since the condition is sufficient not necessary, a non-
negligible discrepancy between the two sides of (6) may be a reason for tuning
to achieve out-of-sample prediction unbiasedness.
Meanwhile, let thesubsampling Rao-Blackwell (SRB) predictorof any out-of-
sample unit withxi =xbe given as
¯µ(x, s) =Eq

µ(x, s1)|s

.(8)
By definition,¯µ(x, s)is more efficient thanµ(x, s1)because it removes the extra
training varianceV q

µ(x, s1)|s

, and it has the same out-of-sample prediction
bias asµ(x, s1)which can be removed as follows.
Proposition 2.Given a representative trainingpq-design, withπ i = Pr(i∈s)
andq 2i := Pr(i∈s 2 |i∈s), wheren R is the number of out-of-sample units, the
predictor˜µ(x, s)ispq-unbiased for out-of-sample prediction, where
˜µ(x, s) = ¯µ(x, s)−τµ(s)
and
τµ(s) = 1 nR
n
Eq
 X
i∈s2
 1
πi −1
 1
q2i µ(xi, s1)

−
X
i∈s
 1
πi −1

yi
o
.(9)
Corollary 4.Given the SRS-SRSpq-design, any given SRB-predictor(8)can be
tuned by(9)to be unbiased for out-of-sample prediction(5), whereτ µ(s)is the
average in-sample OOB prediction error which is given as
τµ(s) =E q

1
n2
X
i∈s2

µ(xi, s1)−y i

= 1 n
X
i∈s
Eq

µ(xi, s1)|i∈s 2

− 1 n
X
i∈s
yi .(10)
3 k-Nearest Neighbor (kNN) prediction
Let us illustrate with kNN as a simple ML algorithm. Given feature vectorx
and donor setsof sizen, letN k(x;s)denote the set ofknearest neighbours (or
units ins) in terms ofx, such that the kNN predictor can be given as
η(x, s) =1 k X j∈Nk(x;s) yj .
According to Stone (1977, Theorem 2 and Corollary 3), the kNN predictor
7

is IID-consistent forEXY (y|x)for any fixedx-value, as both the sample sizen
andktend to∞, whereE XY denotes model expectation over the distribution of
(x, y). WhiletheIIDassumptionmaynotbeunreasonableinmanyapplications,
it seems unrealistic to requirek→ ∞in finite-sample settings where kNN is
typically applied with a small fixedk.
Let us apply design-based prediction theory under the SRS-SRSpq-design,
where explicit results are available, which can as well be instructive for those
interested in IID-model inference. Let the population mean and its generic
prediction estimator be given as, respectively,
P= 1 N X i∈U yi and ˆP= 1 N  X i∈s yi + X i /∈s ˆµi  withˆµ i =µ(x i, s).
3.1 Debiasing kNN
Let us consider the following baseline, or kNN-based, predictors.
Sample-mean (baseline):ˆµ i = ¯ys = 1 n
X
i∈s
yi
Sample-kNN:ˆµ i =η(x i, s)
SRB-kNN: ˆµ i = ¯η(xi, s) =Eq

η(xi, s1)|s

SRB-kNN, residual-tuned:ˆµ i = ¯η(xi, s)−
n
1
n
X
k∈s
¯η(xk, s)−¯ys
o
SRB-kNN, OOB-tuned:ˆµ i = ¯η(xi, s)−
n
1
n
X
k∈s
˙η(xk, s)−¯ys
o
where˙η(x k, s1)is the OOB SRB-predictor for anyk∈s, i.e.
˙η(xk, s) =Eq

η(xk, s1)|k∈s 2

.
The sample-mean yieldspq-unbiased prediction of ¯YR = 1 N−n P i /∈syi, but it
does not use thex-feature information. Both sample-kNN and SRB-kNN are
likely to bepq-biased: while we are not aware of any exactly unbiased estimator
of the bias of sample-kNN, an unbiased bias estimator for SRB-kNN is given by
the term in{·}of the OOB-tuned SRB-kNN according to the theory above. The
residual-tuned SRB-kNN is not unbiased, although it may have a smaller bias
than SRB-kNN, whereas the OOB-tuned SRB-kNN is exactlypq-unbiased. Let
us illustrate with a simple example, where exact calculation is possible.
Example 2.In a populationUof sizeN, letx i = 1ifi= 1,2andx i = 0ifi̸= 1,2.
Lety 1 = 1andy= 0ifi̸= 1. Suppose an SRS-SRSpq-design withk= 1for
the kNN predictor. By straightforward though tedious calculation (Appendix B),
we can show that the OOB-tuned SRB-kNN is exactly unbiased, whereas the
8

prediction bias of¯YR by the different kNN-predictors are given as
Bias(sample-kNN)= 1 N−1  n N−1 −1  ,
Bias(SRB-kNN)= 1 N−1  n1 N−1 −1  ,
Bias(residual-tuned SRB-kNN)
n1=n2
= 1 N−1  5n 4(N−1) −1  .
Notice that the bias of residual-tuned SRB-kNN depends on the choice of(n1, n2),
and the result given above refers to the case ofn1 =n 2.
3.2 A simulation study
We can use simulations to illustrate the potential bias of using kNN predictors
and design-based debiasing. Let a population of values be generated as below:
yi = 1 + 0.5x1i + 0.3x2i + 6 max(0, x1i)2 +ϵ i ,
x1i, x2i
IID
∼N(0,1), Cov(x 1i, x2i) = 0.5andϵ i
IID
∼N(0,0.2).
Figure 1 depicts such a simulated population of sizeN= 250. As can be seen,
there is a dramatic ‘bend’ ofE(yi |x 1i)somewhere betweenx 1i = 0andx 1i = 1,
which can potentially cause bias in kNN-prediction since the realisedy-values
are rather imbalanced on either side ofx1i asx 1i increases.
−2 −1 0 1 2 3
0 10 20 30 40 50 60
x1
y
−3 −2 −1 0 1 2 3
0 10 20 30 40 50 60
x2
y
Figure 1: Scatter plots of simulated population,N= 250.
We now conduct a Monte Carlo simulation withBsamplessdrawn by SRS
from a simulated population, with population sizeN= 10 4 and sample size
n= 10 3. Generically, let ˆθ(1), ...,ˆθ(B) be the realised values of a given population
mean prediction estimator over theBsimulated samples. Given the population
9

meanP, let theempiricalbias and MSE of ˆθby simulation be
EBias(ˆθ) = 1 B
BX
b=1
ˆθ(b) −P  and EMSE( ˆθ) = 1 B BX b=1 ˆθ(b) −P 2 .
In addition, let theempiricalstandard error of ˆθby simulation be
ESE(ˆθ) =
vuut 1
B−1
BX
b=1
ˆθ(b) − 1 B BX b=1 ˆθ(b)2 .
In caseˆθrefers to an SRB-kNN prediction estimator, we can estimate its bias
and MSE as described in Appendix C . Letbias(ˆθ)be the average of theBbias
estimates andmse(ˆθ)that of the MSE estimate. Next,mse(ˆθ)is available when
ˆθis the unbiased sample-mean¯ys. Finally, bias and mse of the sample-5NN
are omitted in the results below, since we are unaware of any exactly unbiased
estimator of the bias or MSE of sample-kNN.
Table 1: Results by SRS-SRSpq-design,B= 100.
Sample SRB-5NN Sample
5NN Untuned Resid-tuned OOB-tuned mean
EBias -0.225 -0.795 -0.099 -0.088 -0.069
ESE 0.028 0.300 0.118 0.122 0.211
EMSE 0.051 0.721 0.024 0.023 0.049
bias N/A -0.696 -0.011 0 0
mse N/A 0.726 0.016 0.016 0.050
Table 1 shows the simulation results, based onB= 100sampless, where
kNN-predictionusesk= 5. FortheSRB-kNNpredictors, weusedT= 100forthe
MonteCarloSRBandn 1 = 50asthetrainingsetsize; seeAppendixDfordetails.
Notice that the subsample donor set sizen1 = 50is rather small compared to
the sample sizen= 1000, which is chosen here purely for illustration purposes,
becausethebiasofkNN-predictiontendstoincreaseinmagnitudeasthedonor
set size decreases, i.e.n1 for subsample-kNN ornfor sample-kNN.
We note the following about these results. Firstly, the population mean is
P= 4.107in this case. The bias of the sample-5NN or SRB-5NN prediction
estimator is not negligible: EBias is seen to dominate the corresponding ESE
for both, which is−0.225versus0.028for the sample-5NN and−0.795versus
0.300for SRB-5NN.
Secondly, the residual-tuned SRB-kNN is not unbiased, while the OOB-
tuned SRB-kNN and the sample-mean are both unbiased. However, comparing
the three EBiases by simulation, i.e.−0.099versus−0.088or−0.069in Table 1,
residual-tuningdoesseemtohaveremovedmostofthebiasofkNNinthiscase.
Nevertheless, debiasing by the OOB-tuned SRB-kNN is seen to be beneficial
here, now that it achieves unbiasedness as well as the lowest EMSE (i.e.0.023)
among all the alternatives.
10

Thirdly, when it comes to bias and MSE estimation, the result is acceptable
for the sample-mean¯ys, wheremse= 0.050compared to EMSE= 0.049. For the
SRB-5NN, we havebias=−0.696compared to EBias=−0.795and mse= 0.726
to EMSE= 0.721. For the OOB-tuned SRB-5NN that is unbiased,mse= 0.016
is reasonable compared to its ESE2 = 0.015. For the residual-tuned SRB-5NN,
we havemse= 0.016, which is clearly lower than its EMSE= 0.024but close
to bias
2
+ESE 2 = (−0.011)2 + 0.1182 = 0.014. This again suggests that its EBias
here likely overstates its bias due to the Monte Carlo error.
In summary, the simulation study here has demonstrated the potential bias
caused by direct kNN-prediction, such that debiasing by our theory may be
beneficial. Moreover, the associated inference of SRB-prediction enables one to
choose among the alternative predictors in practice. Although residual-tuning
may be able to remove much of the bias, unbiased OOB-tuning is preferable
when its MSE is not larger than that of residual-tuning.
4 Design-based classification
We have so far considered design-unbiased prediction. Unit-level classification
of categorical outcomes may be of practical interest as well. Below we consider
specifically classification of binary outcomes.
4.1 Out-of-sample classification accuracy
Letµ(x, s1)be the probability ofy= 1according toµ(·)trained ons 1, such as the
kNN-mean givenxand donor sets 1. Letˆyi(s1)be a binary classifier based on
µ(xi, s1)for anyi∈U. For instance,ˆy i(s1) =I

µ(xi, s1)>0.5

deterministically, or
ˆyi(s1) =I

ui ≤µ(x i, s1)

randomly givenui
IID
∼Unif(0,1)whereu i is independently
generated across the units for the purpose of classification.
Let theout-of-sample classification accuracyofˆyi(s1)refer to its performance
averaged over all the out-of-sample unitsR=U\s, which is defined as
ϕ(R|s 1) = 1 nR Φ(R|s 1)andΦ(R|s 1) = X i∈R I  yi = ˆyi(s1)  (11)
Aswithunbiasedprediction(5),weleaveittofuturestudytodeterminewhether
design-unbiased classification or inference of unit-specificyi can be achieved
in a sensible manner.
It follows that deterministic classification causes biased results generally.
For instance, suppose the population proportionP x = 0.2givenxis known,
thenI(P x ≥ψ)is either 0 or 1 forallthe units withx i =x, given any threshold
valueψ∈(0,1), which is clearly biased. Meanwhile, letN x be the number of
units withx i =xin the population, then the randomised classifierI(u i ≤P x)
achieves unbiased classification, in the sense that
Eu

1
Nx
X
i∈U:x i=x
I

yi =I(u i ≤P x)

=P x = 1 Nx
X
i∈U:x i=x
yi
11

where the expectation is with respect toui
IID
∼Unif(0,1).
Givenµ(x, s1)instead ofP x in practice, one can estimateϕ(R|s1)conditional
ons 1 based on the OOB classification errors{I

yi = ˆyi(s1)

:i∈s 2}, just like
estimating its prediction error based on{µ(xi, s1)−y i :i∈s 2}. However, what
is of interest is the classification accuracy associated with the corresponding
SRB-predictor¯µ(xi, s), which is more efficient thanµ(xi, s1).
Let us consider directly the Monte Carlo implementation of SRB based onT
random splits,(s (t) 1 , s(t) 2 )fort= 1, ..., T. This includes the exact SRB-probability
¯µ(x, s)as the special case ofT=C(n, n1)distinct splits. For anyi∈U, let
Ti =
TX
t=1
I(i /∈s(t) 1 )
be the number of splits where the unit is out ofs1, whereT i =Tifi /∈s. Let
˚µ(xi, s) =1 Ti
TX
t=1
µ(xi, s(t) 1 )I(i /∈s(t) 1 )(12)
for anyi∈U, which has the same expectation as the exact SRB-probability. It
follows that, given a representative trainingpq-design (2), we have
Epq

˚µ(xi, s)|i∈s 2

=E p

¯µ(xi, s)|i /∈s1

=E pq

˚µ(xi, s)|i /∈s

(13)
for anyi∈U. Let˚y i(s)be the classifier using the probability˚µ(xi, s)by (12). Let
itsout-of-sample classification accuracybe given similarly as (11),
˚ϕ(R) = 1 nR ˚Φ(R)and ˚Φ(R) = X i∈R I  yi = ˚yi(s)  (14)
4.2 OOB estimation of classification accuracy
Let the unit-specific classification accuracy using the probability˚µ(xi, s)be
˚αi =E pq

I

yi = ˚yi(s)

|i /∈s1

for anyi∈U. In other words, for given unitiwith fixedy i,˚αi measures the
performance of˚yi(s)over repeated sampling conditional oni /∈s1. Next, let us
introduce a regularity condition on˚αi as below.
(M) Given representative trainingpq-design,˚αi is a function given as
˚αi =m i

yi, xi, Epq

˚µ(xi, s)|i /∈s1

Note that the functionmi(·)is allowed to vary across the units. The condition
(M) effectively requires˚αi to be a constant given the arguments ofmi(·).
By (13), we can exchangeEpq

˚µ(xi, s)|i /∈s

andE pq

˚µ(xi, s)|i∈s 2

, such
12

that the mappingmi(·)of the condition (M) yields
˚αi =E pq

I

yi = ˚yi(s)

|i∈s 2

=E pq

I

yi = ˚yi(s)

|i /∈s

.(15)
Notice that the condition (M) is not trivial since, as the Lemma below shows:
although eachI

yi = ˚yi(s)

is a function of˚µ(xi, s), apart from(yi, xi)obviously,
it is not necessary that˚αi then only depends onEpq

˚µ(xi, s)|i /∈s1

.
Lemma 2.The random classifier˚yi(s) =I

ui ≤˚µ(xi, s)

, whereu i
IID
∼Unif(0,1),
satisfies the condition (M). The deterministic classifier˚yi(s) =I

˚µ(xi, s)≥ψ

does
not satisfy the condition (M) given any threshold valueψ∈(0,1).
Proposition 3.Given a representative trainingpq-design and a classifier satis-
fyingthecondition(M),apq-unbiasedpredictoroftheout-of-sampleclassification
accuracy ˚Φ(R)in(14)is given as
˚Φw(s) = X
i∈s
 1
πi −1

I

yi = ˚yi(s)

.(16)
Notice that we do not estimate each˚αi specifically, but rather we work with
their aggregates. The result above includes the exact SRB-probability¯µ(xi, s)
as a special case when it is feasible instead of˚µ(xi, s).
Notice also that the use of in-sample out-of-bagI

yi = ˚yi(s)

in (16) means
thatdebiasingµ(x i, s1)by tuningneedsto berestrictedtos 1, suchas kNNbased
on donor sets 11 and tuned bys 1 \s 11, wheres 11 ⊂s 1. This is because tuning
must not invalidate the ‘out-of-bag-ness’ of˚yi, i.e. tuning must be based on
the units outside eachs2 — hence, inside eachs1.
5 Illustrative application
We apply prediction tuning and classification accuracy estimation to a real
dataset to demonstrate the theory and methods developed in this paper.
5.1 Data and setup
LetN= 10 4 satellite images be randomly selected from the CropHarvest (HDF5)
dataset, each assignedy= 1in case of a coffee field ory= 0otherwise, associ-
ated with anx-vector of 216 features. We treat these images as the population
Uwith associated constants{(y i, xi) :i= 1, ..., N}over repeated sampling.
Let kNN withk= 5be the ML algorithm, based on any of the three feature
sets below:
I. (x_126, x_144, x_180, x_190, x_198) by LASSO logistic regression;
II. (x_008, x_025, x_048, x_129, x_183) by random selection;
III. (x_043, x_162, x_136, x_063, x_024) by forward selection for 5NN.
Consider the following 5NN-based predictors for out-of-sampley-classification.
13

•Sample-5NNη(x, s), given samplesof sizenselected by SRS.
•SRB-5NNE q

η(x, s1)|s

, with training sets1 of sizen 1 by SRS froms.
•OOB-tuned SRB-5NNE q

ητ (x, s1)|s

, whereη τ (x, s1)is thes 11-5NN that is
tuned by out-of-s11 errors ins 1 \s 11, givens 11 of sizen 11 by SRS froms1, i.e.
ητ (x, s1) =η(x, s11)− 1 n1−n11
X
i∈s1\s11

η(xi, s11)−y i

We use simulations to evaluate the performance of design-based debiasing
and classification accuracy prediction. Letn= 200be the size of samplesby
SRS fromU, letn 1 = 120be the size ofs 1 for SRB given by SRS froms, and let
n11 = 80be the size ofs 11 for the OOB-tuned SRB given by SRS froms1. Let
T= 100for Monte Carlo SRB, such that, for anyk∈U, the SRB-5NN predictor
is given by (12) generically, and the OOB-tuned SRB-5NN predictor is given by
˚ητ (xk, s) = 1 Tk
TX
t=1
I(k /∈s(t) 1 ) n η(xk, s(t) 11 )− 1 n1−n11 X
i∈s(t) 1 \s(t) 11

η(xi, s(t) 11 )−y i o .
Finally, for the classification accuracy (14) by randomised classifier associated
with a given OOB SRB-5NN probability, denoted by˚η(xi, s), we can replace the
random variableI

yi = ˚yi(s)

in (16) by
pi =I(y i = 1)˚η(xi, s) +I(yi = 0)

1−˚η(xi, s)

.
This is more efficient than using the random˚yi(s) =I

ui ≤˚η(xi, s)

, which is
subject to an additional variance due toui
IID
∼Unif(0,1).
5.2 Results
Denote byBthe number of simulations, each corresponding to a different
samplesfromU. Let ˆP (b) be a realised prediction estimate of the population
meanP, as defined in Section 3, whereb= 1, ..., B. Let
EBias= 1 B
BX
b=1
( ˆP (b) −P)with V(EBias)= 1 B(B−1)
BX
b=1
( ˆP (b) −P) 2
and EVar= 1 B−1
BX
b=1
{ ˆP (b) − 1 B
BX
b=1
ˆP (b)}2 .
Table 2 shows the results for debiasing, based onB= 100simulations.
Firstly, given any feature set, the OOB-tuned SRB-5NN is essentially unbiased
for the population mean: its EBias is clearly closer to 0 than the untuned SRB-
5NN and not significantly different from 0 in light of V(EBias). This confirms
again the theory of design-based debiasing developed in Section 2.
Secondly, the bias of kNN prediction depends on the selected features and
their sample distribution. In this case, the randomly selected feature set (II)
14

Table 2: Debiasing results, feature set (I)–(III),B= 100simulations
Predictor, feature set (I) EBias √V(EBias) EVar
Sample-5NN -0.01712 0.00192 0.000072
SRB-5NN -0.01776 0.00200 0.000081
OOB-tuned SRB-5NN -0.00115 0.00130 0.000166
Predictor, feature set (II) EBias √V(EBias) EVar
Sample-5NN 0.00063 0.00079 0.000061
SRB-5NN -0.00236 0.00091 0.000076
OOB-tuned SRB-5NN 0.00008 0.00104 0.000107
Predictor, feature set (III) EBias √V(EBias) EVar
Sample-5NN 0.00234 0.00043 0.000013
SRB-5NN 0.00422 0.00061 0.000019
OOB-tuned SRB-5NN -0.00035 0.00042 0.000017
causes very little bias to the standard sample-5NN, which is possible if it leads
to ‘random’ donor imputation under SRS. However, such ‘accidental’ unbiased-
nesscancomeatapriceofincreasedvariance, whichisevidentifonecompares
the EVar of sample-5NN given either feature set (II) or (III). We notice that the
results of feature set (II) are included here only for instructive purposes, since
one is unlikely to use randomly selected features for kNN in practice.
Thirdly, feature selection is an integral part of algorithmic ML. One can see
this most clearly in the poor results given feature set (I). Although it may be
a reasonable choice for logistic regression, using these features for kNN can
increase both the prediction bias and variance. In this case, the EBias of
sample-5NN (or SRB-5NN) is larger than
√
EVar and the EVar is even larger
than that given the randomly selected feature set (II).
Finally, given feature set (III) for kNN, the EBias of directly applying 5NN
is small but still appreciable compared to
√
EVar. Since the empirical MSE of
the OOB-tuned SRB-5NN is smaller than either the untuned 5NN predictors,
debiasing is worthwhile for out-of-sample prediction here.
When it comes to the classification accuracy˚ϕ(R)associated with a given
SRB-5NN predictor, as defined by (14), letˆϕ(R) =n −1 R ˚Φw(s)according to (16).
Table 3 gives the results based onB= 100simulations, where the EBias of
classification accuracy prediction is the difference between columns˚ϕ(R)and
ˆϕ(R), and the last column shows its empirical MSE over the simulations. It is
evident that Proposition 3 achieves unbiased prediction of the out-of-sample
classification accuracy in every situation.
Notice that, given either feature set (I) or (II), the classification accuracy of
the unbiased OOB-tuned SRB-5NN is clearly reduced compare to the biased
SRB-5NN. The reason is that tuning can cause the predicted probabilities to
be out of the bounds[0,1], which then leads to truncation of probabilities and
loss of classification accuracy, as illustrated by the example below.
Example 3.Suppose two out-of-sample units with(y 1, y2) = (1,0). Suppose a
15

Table 3: Mean over simulations (B= 100) of classification accuracy ˚ϕ(R), its
predictor ˆϕ(R), and associated squared error{ˆϕ(R)− ˚ϕ(R)}2
Average overBsimulations
Predictor, feature set (I) ˚ϕ(R) ˆϕ(R){ ˆϕ(R)− ˚ϕ(R)}2
SRB-5NN 0.944 0.945 0.000143
OOB-tuned SRB-5NN 0.922 0.923 0.000141
Predictor, feature set (II) ˚ϕ(R) ˆϕ(R){ ˆϕ(R)− ˚ϕ(R)}2
SRB-5NN 0.962 0.963 0.000102
OOB-tuned SRB-5NN 0.939 0.941 0.000106
Predictor, feature set (III) ˚ϕ(R) ˆϕ(R){ ˆϕ(R)− ˚ϕ(R)}2
SRB-5NN 0.989 0.989 0.000018
OOB-tuned SRB-5NN 0.987 0.987 0.000020
given predictor yields(µ 1, µ2) = (0.95,0.07), such that the probability of correct
randomised classification is 1 2 (0.95 + 0.93) = 0.94. Givenµ 1 +µ 2 = 1.02̸=y 1 +y 2,
tuning is possible, which yields, say,(˚µ1,˚µ2) = (µ 1, µ2) +ϵ. As long as(˚µ1,˚µ2)
are within the bounds[0,1], the probability of correct randomised classification is
unaffected,since 1 2 (µ1+ϵ+1−µ2−ϵ) = 1 2 (µ1+1−µ2). However,itispossibletoobtain
out-of-boundprobabilities,say,(˚µ1,˚µ2) = (1.04,0.16),inwhichcasetheprobability
of correct randomised classification would be reduced to1 2 (1 + 0.84) = 0.92.
Meanwhile, given the feature set (III) selected for kNN, the drop of classifi-
cation accuracy by debiasing is much less pronounced, i.e. 0.987 compared to
0.989, and the classification accuracy is higher compared to using the feature
set (I) or (II). In other words, not only does sensible feature selection improve
the classification accuracy, it can also reduce the risk of out-of-bounds tuning
for the purpose of unbiased population prediction estimation.
6 Summary of findings and future research
ML must use a training dataset to form the prediction model or algorithm. It
would be difficult to relate its in-sample out-of-bag prediction error of a given
unit to its out-of-sample prediction error of the same unit, if theexpectedpre-
diction would differ depending on whether the unit is in or out of the sample.
The concept of representative training articulates this intuition in terms of how
the training set can be selected from the relevant finite population, whether it
consists of persons, businesses, physical or spatial objects.
Notice that the same intuition has always existed in IID-model inference,
such as cross-validation, or out-of-bag accuracy for random forests. Since one
can obtain IID samples by with-replacement sampling from a given population,
theconceptofrepresentativetrainingcanbeviewedasageneralisationofthese
IID-model inference ideas to finite population inference, where the units may
be selected with unequal probabilities and without replacement.
16

Moreover, representative training provides generally a means for tuning a
trained algorithm, based on its in-sample out-of-bag prediction errors, so as to
achievedesign-unbiasedout-of-sampleprediction, i.e. overrepeatedsampling-
and-training under thepq-design. A topic for future study may be to investigate
representative training for interval estimation so as to achieve exact design-
based coverage as it was defined by Neyman (1934).
In addition, we have shown that out-of-sample unit-level classification of
categorical outcomes can yield unbiased prediction estimation of population
totals, and the associated classification accuracy can be assessed unbiasedly
given representative training by thepq-design.
However, one should keep in mind the distinctive needs of population-level
estimation and unit-level classification. For instance, in many applications of
ML, such as official statistics, population estimation is always required, but
unit classification is only sometimes. If unbiasedness of population estimation
is necessary, then one may have to accept a reduced classification accuracy.
This seems therefore a natural topic for future research, i.e. how to implement
unit-level classification subject to unbiased population prediction estimation,
such that the classification accuracy can be maximised.
Finally, looking back on the groundbreaking idea of Neyman (1934) to finite
population sampling, which consists of a “representative” method of sampling
and an associated “consistent” method of estimation, one may view represen-
tative trainingpq-designs as an extension of the concept of “representative”
sampling, providing an intuitive basis for broadening the scope of associated
“consistent” ML estimation by predicting or classifying the out-of-sample units.
We hope this general outlook on design-unbiased finite population inference
may be useful to many practitioners of ML.
A Proofs
Lemma 1.
Proof.For the proof here, writeπ2i(s1)forπ 2i to emphasise it as a function ofs1.
Given a well-definedpq-design, we haveEpq(·) =E s1s2(·), such that
(2)⇔
X
s1̸∋i
µ(xi, s1) f(s 1) Pr(i∈s 2 |s 1) Pr(i∈s 2) = X s1̸∋i µ(xi, s1) f(s 1) Pr(i /∈s2 |s 1) Pr(i /∈s)
⇔
X
s1̸∋i
µ(xi, s1)f(s 1) π2i(s1) πi −Pr(i∈s 1) = X s1̸∋i µ(xi, s1)f(s 1) 1−π 2i(s1) 1−π i
⇔
X
s1̸∋i
µ(xi, s1)f(s 1)π2i(s1) 1−Pr(i∈s 1) πi −Pr(i∈s 1) = X s1̸∋i µ(xi, s1)f(s 1).(17)
First, the equality (17) holds forall possibleµ(xi, s1)if and only if
π2i(s1) 1−Pr(i∈s 1) πi −Pr(i∈s 1) = 1⇔(3)
17

Next, multiplying both the sides of (17) byπi−Pr(i∈s1) {1−Pr(i∈s1)}2, the left-hand side yields
X
s1̸∋i
µ(xi, s1)π2i(s1) f(s 1) 1−Pr(i∈s 1) =E s1  µ(xi, s1)π2i(s1)|i /∈s1 
while the right-hand side can be written as
 X
s1̸∋i
µ(xi, s1) f(s 1) 1−Pr(i∈s1)

Pr(i∈s2)
1−Pr(i∈s1)

=E s1

µ(xi, s1)|i /∈s1
 X
s1̸∋i
πi2(s1) f(s 1) 1−Pr(i∈s1)

=E s1

µ(xi, s1)|i /∈s1

Es1

π2i(s1)|i /∈s1

i.e. representative training of any givenµ(x, s1)if and only if (4), including when
π2i(s1)varies withs 1 and is not given by (3).
Corollary 1.
Proof.Given sample sizesnofsandn 1 ofs 1, we haveC(N−1, n 1) = (N−1)! n1!(N−n 1−1)!
distincts 1 on either side of (2), andPr(i∈s 2 |s 1) = n−n1 N−n 1 I(i /∈s1).
Corollary 2.
Proof.Letπ i bethePoissonsamplingprobabilityofi∈U, andλthatofBernoulli
sampling froms. We havef(s 1) = Q j∈s1 λπj Q l /∈s1(1−λπ l)andPr(i∈s 1) =λπ i.
Moreover, we havePr(i∈s 2 |s 1) = πi−λπi 1−λπi I(i /∈s1)for eachi∈U.
Proposition 1.
Proof.Regarding the right-hand sides in (6) and (5), we have
Ep
 X
i∈s
 1
πi −1

yi

=
X
i∈U
yi −E p
 X
i∈s
yi

=E p
 X
i∈R
yi

.
Meanwhile, regarding the left-hand sides in (6) and (5), we have
Epq
 X
i∈s
 1
πi −1

µ(xi, s1)|i∈s 2

=E pq
 X
i∈U
I(i∈s)
πi (1−π i)µ(xi, s1)|i∈s 2

=
X
i∈U
Epq

(1−π i)µ(xi, s1)|i∈s 2, i∈s

=
X
i∈U
(1−π i)Epq

µ(xi, s1)|i∈s 2

(2)
=
X
i∈U
(1−π i)Epq

µ(xi, s1)|i /∈s

=E pq
 X
i∈R
µ(xi, s1)

given representative trainingpq-design. Thus, the condition (6) ensures (5).
Proposition 2.
18

Proof.Since the total out-of-sample prediction bias of¯µ(xi, s)is given by the
expectation of the difference between the two sides of (6), one can apportion
1/nR of this difference to eachi /∈sas ap-unbiased correction. The expression
(9) follows, since
Eq
 X
i∈s2
1
q2i
 1
πi −1

µ(xi, s1)

=
X
i∈s
 1
πi −1

Eq

µ(xi, s1)|i∈s 2

.
Lemma 2.
Proof.For the random classifier, we have
I

yi = 1 = ˚yi(s)

=
(
1ifu i ≤˚µ(xi, s)
0ifu i >˚µ(xi, s) ⇒˚αi =E pq

˚µ(xi, s)|i /∈s1

ify i = 1
I

yi = 0 = ˚yi(s)

=
(
1ifu i >˚µ(xi, s)
0ifu i ≤˚µ(xi, s) ⇒˚αi = 1−E pq

˚µ(xi, s)|i /∈s1

ify i = 0
such that˚αi is fully determined givenyi,x i andE pq

˚µ(xi, s)|i /∈s1

.
Whereas, for the deterministic classifier, we have
I

yi = 1 = ˚yi(s)

=
(
1if˚µ(x i, s)≥ψ
0otherwise ⇒˚αi = Pr

˚µ(xi, s)≥ψ|i /∈s 1

ify i = 1
I

yi = 0 = ˚yi(s)

=
(
1if˚µ(x i, s)< ψ
0otherwise ⇒˚αi = Pr

˚µ(xi, s)< ψ|i /∈s1

ify i = 0
suchthat˚αi dependsonthevarianceof˚µ(x i, s)aswellasE pq

˚µ(xi, s)|i /∈s1

.
Proposition 3.
Proof.We have
Epq
˚Φ(R)  = X
i∈U
Epq

I(i /∈s)I

yi = ˚yi(s)

=
X
i∈U
(1−π i)Epq

I

yi = ˚yi(s)

|i /∈s

(15)
=
X
i∈U
(1−π i)˚αi
Epq
˚Φw(s)  = X
i∈U
Epq

I(i∈s)
 1
πi −1

Epq

I

yi = ˚yi(s)

|i∈s 2, i∈s

=
X
i∈U
(1−π i)Epq

I

yi = ˚yi(s)

|i∈s 2

(15)
=
X
i∈U
(1−π i)˚αi.
19

B Details of Example 2
LetY R = (N−n) ¯YR. Providedn≥3, we haveη(x i, s) = 0for anyi̸= 1,2, and
ˆYR(s)−Y R n≥3 =



−1if1/∈s, P i /∈sη(xi, s) = 0, prob.N−n N
0if1∈s,2∈s, P i /∈sη(xi, s) = 0, prob. n(n−1) N(N−1)
+1if1∈s,2/∈s, P i /∈sη(xi, s) = 1, prob.N−n N n N−1 .
Thus, usingη(x, s)ispq-biased for estimatingY R except whenn=N−1.
Meanwhile, let ˆYR(s1)be the prediction estimator ofYR usingη(x i, s1)for any
i /∈s. Providedn1 ≥3, we haveη(x i, s1) = 0for anyi̸= 1,2, and
ˆYR(s1)−Y R n1≥3 =



−1if1/∈s, P i /∈sη(xi, s1) = 0, prob. N−n N
0if1∈s,2∈s, P i /∈sη(xi, s1) = 0, prob. n(n−1) N(N−1)
+1if1∈s 1,2/∈s, P i /∈sη(xi, s1) = 1, prob. N−n N n1 N−1
0if1∈s 2,2/∈s, P i /∈sη(xi, s1) = 0, prob. N−n N n2 N−1 .
Thus, using the¯η(x, s)predictor also leads topq-biased estimation generally.
For residual-tuning ofη(x, s1)byc η(s1) = 1 n P i∈s η(xi, s1)−¯ys. We have
cη(s1)
n1≥3 =



0if1/∈s, P i∈s η(xi, s1) = 0, P i∈s yi = 0, prob. N−n N
1
n if1∈s 1,2∈s, P i∈s η(xi, s1) = 2, P i∈s yi = 1, prob. n1(n−1) N(N−1)
− 1 n if1∈s 2,2∈s, P i∈s η(xi, s1) = 0, P i∈s yi = 1, prob. n2(n−1) N(N−1)
0if1∈s 1,2/∈s, P i∈s η(xi, s1) = 1, P i∈s yi = 1, prob. N−n N n1 N−1
− 1 n if1∈s 2,2/∈s, P i∈s η(xi, s1) = 0, P i∈s yi = 1, prob. N−n N n2 N−1
such that the SRB residual-tuning of¯η(x, s)is given by
¯cη(s)
n1≥3 =



0if1/∈s, prob. N−n N
n1−n2
n2 if1∈s,2∈s, prob. n(n−1) N(N−1)
− n2 n2 if1∈s,2/∈s, prob. N−n N n N−1 .
Straightforward algebra shows that this doesnotremove the bias,
1
N−n Epq
 ˆYR(s1)−Y R  −E p  ¯cη(s)  ̸= 0.
20

For out-of-bag tuning byτη(s1) = 1 n2 P i∈s2  η(xi, s1)−y i  . We have
τη(s1)
n1≥3 =



0if1/∈s, P i∈s2 η(xi, s1) = 0, P i∈s2 yi = 0, prob. N−n N
− 1 n2 if1∈s 2,2∈s, P i∈s2 η(xi, s1) = 0, P i∈s2 yi = 1, prob.∝ n2 n
0if1∈s 1,2∈s 1, P i∈s2 η(xi, s1) = 0, P i∈s2 yi = 0, prob.∝ n1(n1−1) n(n−1)
1
n2 if1∈s 1,2∈s 2, P i∈s2 η(xi, s1) = 1, P i∈s2 yi = 0, prob.∝ n2n1 n(n−1)
0if1∈s 1,2/∈s, P i∈s2 η(xi, s1) = 0, P i∈s2 yi = 0, prob. N−n N n1 N−1
− 1 n2 if1∈s 2,2/∈s, P i∈s2 η(xi, s1) = 0, P i∈s2 yi = 1, prob. N−n N n2 N−1 .
such that the SRB out-of-bag tuning of¯η(x, s)is given by
¯τη(s)
n1≥3 =



0if1/∈s, prob. N−n N
− n2−1 n(n−1) if1∈s,2∈s, prob. n(n−1) N(N−1)
− 1 n if1∈s,2/∈s, prob. N−n N n N−1 .
Straightforward algebra to shows that this does remove the bias,
1
N−n Epq
 ˆYR(s1)−Y R  −E p  ¯τη(s)  = 0.
C Design-based bias and MSE
The derivation follows the approach of Zhang et al. (2025).
Bias of SRB-kNNThe prediction error due toη(x, s1)can be written as
B(s1) = 1 N X i /∈s ei(s1)ande i(s1) =η(x i, s1)−y i.
Givenπ 2i = n2 N−n 1 under SRS-SRS, an unbiased predictor based ons2 is
ˆB(s1) = N−n N n2 X i∈s2 ei(s1)whereE s  ˆB(s1)−B(s 1)|s 1  = 0.
For the corresponding error of the SRB-kNN¯η(x, s), denoted by¯B(s), we have
ˆ¯B(s) = N−n N n2 Eq  X i∈s2 ei(s1)  = N−n N n X i∈s  ˙η(xi, s)−yi  .(18)
21

Bias of residual-tuned SRB-kNNThe prediction error due toη(x, s1)is
Bc(s1) = 1 N X i /∈s ei(s1) + N−n N 1 n X i∈s  yi −η(x i, s1) 
= 1 N X i /∈s ei(s1)−  1 n − 1 N  X i∈s1 ei(s1) + X i∈s2 ei(s1) 
= N−n N ¯eU\s (s1)−  1 n − 1 N   n1¯es1(s1) +n 2¯es2(s1) 
where¯eD(s1)denotestheaverageofe i(s1)overi∈DgivenanysetD. Conditional
ons 1, an unbiased predictor ofBc(s1)follows as
ˆBc(s1) =

1− n N  ¯es2(s1)−  1 n − 1 N   n1¯es1(s1) +n 2¯es2(s1) 
=n 1
 1
n − 1 N  ¯es2(s1)−¯es1(s1) 
such that an unbiased estimator of the bias of residual-tuned SRB-kNN is
ˆ¯Bc(s) =E q  ˆBc(s1)|s  .(19)
MSE of SRB-kNNThe errorB(s 1)has been given earlier. Conditional ons 1,
an unbiased estimator of the conditional MSE ofˆP(s 1)can be given as
mse(s1) = ˆB(s1)2 − ˆVs{ ˆB(s1)|s 1}+ ˆVs{B(s1)|s 1}
(Theorem 1, Zhang et al., 2025), where
ˆVs{ ˆB(s1)|s 1}=

1− n N 2 v2
v2 = ˆVs

¯es2(s1)|s 1

=
 1
n2
− 1 N−n 1  1 n2 −1 X i∈s2 {ei(s1)−¯es2(s1)}2
ˆVs{B(s1)|s 1}= X
i∈s2
X
j∈s2

1− π2iπ2j
π2ij

ei(s1)ej(s1)
givenπ 2i ≡ n2 N−n 1 , andπ 2ij =π 2i ifi=jorπ 2ij = n2(n2−1) (N−n 1)(N−n 1−1) ifi̸=j. A design-
unbiased estimator of the MSE of the correspondingˆPfollows as
mse=E q

mse(s1)|s

−V q
 ˆP(s 1)|s  .(20)
MSE of residual-tuned SRB-kNNThe errorB c(s1)is given earlier. Similarly
to that of SRB-kNN, we have
msec(s1) = ˆBc(s1)2 − ˆVs{ ˆBc(s1)|s 1}+ ˆVs{Bc(s1)|s 1}
22

where
ˆVs{ ˆBc(s1)|s 1}=n 2 1
 1
n − 1 N 2 v2 and ˆVs{Bc(s1)|s 1}=  n2 n 2 v2.
Notice that, regarding the variance ofBc(s1)conditional ons 1, we can simplify
the random terms inBc(s1)as
N−n
N ¯eU\s (s1)− N−n N n2 n ¯es2(s1) = N−n 1 N ¯eU\s 1(s1)− n2 N ¯es2(s1)− N−n n n2 N ¯es2(s1)
= N−n 1
N ¯eU\s 1(s1)− n2 n ¯es2(s1)
where¯eU\s 1(s1)is a constant givens1. A design-unbiased estimator of the MSE
of the corresponding ˜Pfollows as
msec =E q

msec(s1)|s

−V q
 ˆP(s 1)|s  .(21)
MSE of OOB-tuned SRB-kNNThe error due to the tunedη(x, s1)is given as
Bτ (s1) = 1 N X i /∈s ei(s1)− N−n N 1 n2 X i∈s2 ei(s1) = N−n N  ¯eU\s (s1)−¯es2(s1) 
which has expectation0conditional ons 1, since tuning has made it unbiased.
It follows that we can use ˆBτ (s1)≡0, such thatV s{ ˆBτ (s1)|s 1} ≡0as well.
Regarding the variance ofBτ (s1)conditional ons 1, we have now
¯eU\s (s1)−¯es2(s1) = N−n 1 N−n ¯eU\s 1(s1)− n2 N−n ¯es2(s1)−¯es2(s1)
= N−n 1
N−n ¯eU\s 1(s1)− N−n 1 N−n ¯es2(s1)
where¯eU\s 1(s1)is a constant givens 1, such that
mseτ (s1) = ˆVs{Bτ (s1)|s 1}=

1− n1
N
2
v2.
A design-unbiased estimator of the MSE of the correspondingˆPfollows as
mseτ =E q

mseτ (s1)|s

−V q
 ˆP(s 1)|s  .(22)
D Monte Carlo SRB
Exact calculation ofE q(·)orV q(·)is infeasible ifC(n, n 1)is too large. In such
situations, theq-expectation andq-variance need to be evaluated by Monte
Carlo based onT(training, test) sets, denoted by(s(t) 1 , s(t) 2 )fort= 1, ..., T.
23

For bias estimation by (18), one would calculate theq-expectation as
Eq
 1
n2
X
i∈s2
ei(s1)

≈ 1 T
TX
t=1
1
n2
X
i∈s(t) 2
ei(s(t) 1 ) = 1 T
TX
t=1
1
n2
X
i∈s(t) 2

η(xi, s(t) 1 )−y i  .
Similarly for otherq-expectations. For theq-variance in (20), one would use
Vq
 ˆP(s 1)|s  ≈ 1 T−1  TX t=1 ˆP(s (t) 1 )− 1 T TX t=1 ˆP(s (t) 1 ) 2 .
Similarly for theq-variance in (21) or (22).
Finally, as explained in Zhang et al. (2025, Section 2.3.2), one needs to
estimate the MSE of the Monte Carlo SRB-predictor being implemented for
out-of-sample prediction (instead of the exact SRB-predictor). Specifically, in
terms of (20) of SRB-kNN, one would use the unbiased estimator
˜mse= 1 T
TX
t=1

mse(s(t) 1 )− n ˆP(s (t) 1 )− 1 T TX t=1 ˆP(s (t) 1 ) o2 .
Similarlyfor (21)ofresidual-tunedSRB-kNN,and(22)ofOOB-tunedSRB-kNN.
References
[1] Angelopoulos, A., Bates, S., Fannjiang, A., Jordan, M.I. and Zrnic, T.
(2023). Prediction-powered inference.Science, 382:669–674(2023).DOI:
10.1126/science.adi6000
[2] Beaumont, J.-F. and Haziza, D. (2022). Statistical inference from finite
population samples: A critical review of frequentist and Bayesian ap-
proaches.The Canadian Journal of Statistics, 50:1186-1212.
[3] Blackwell, D. (1947). Conditional expectation and unbiased sequential
estimation.Annals of Mathematical Statistics, 18: 105-110.
[4] Breidt, F.J.andOpsomer, J.D.(2017).Model-assistedsurveyestimation
with modern prediction techniques.Statistical Science, 32:190-205.
[5] Breiman, L. (2001a).Statistical modelling: The two cultures.Statistical
Science, 16:199-231.
[6] Breiman, L. (2001b). Random Forests.Machine Learning, 45:5-32.
[7] Dagdoug, M., Goga, C. and Haziza, D. (2021). Model-Assisted Estimation
Through Random Forests in Finite Population Sampling.Journal of the
American Statistical Association, 118:1234-1251.
24

[8] European Commission(2017).European Statistics Code
of Practice.https://ec.europa.eu/eurostat/web/quality/
european-statistics-code-of-practice
[9] Fisher,R.A.(1956).StatisticalMethodsandScientificInference.Oliverand
Boyd, Edinburgh and London.
[10] Hansen, M. (1987). Some History and Reminiscences on Survey Sam-
pling.Statistical Science, 2:180-190.
[11] Horvitz, D. G. and Thompson, D. J. (1952). A generalization of sampling
without replacement from a finite universe.Journal of the American Sta-
tistical Association, 47:663-685.
[12] Kalton, G. (2002). Models in practice of survey sampling.Journal of Offi-
cial Statistics, 18:129-154.
[13] McConville KS, and Toth D. (2019). Automated selection of post-strata
using a model-assisted regression tree estimator.Scandinavian Journal
of Statistics, 46:389-413.
[14] Neyman, J. (1934). On the Two Different Aspects of the Representative
Method: The Method of Stratified Sampling and the Method of Purposive
Selection.Journal of the Royal Statistical Society, pp. 558-625.
[15] Rao, C. R. (1945). Information and accuracy attainable in the estima-
tion of statistical parameters.Bulletin of Calcutta Mathematical Society,
37:81-91.
[16] Rao, J. N. K. (2005). Interplay between sample survey theory and prac-
tice: An appraisal.Survey Methodology, 31:117-138.
[17] Rao, J. N. K. (2011). Impact of frequentist and Bayesian methods on sur-
vey sampling practice: A selective appraisal.Statistical Science, 26:240-
256.
[18] Royall, R.M. (1970). On finite population sampling theory under certain
linear regression models.Biometrika, 57:377-387.
[19] Sanguiao-Sande, L. and Zhang, L.-C. (2021). Design-Unbiased Statisti-
cal Learning in Survey Sampling.SankhyaA, Centenary Issue in Honour
of C. R. Rao, 83:714-744.
[20] Statistics Canada (2017).Quality Assurance Framework, 3rd edition.
https://www150.statcan.gc.ca/n1/pub/12-539-x/12-539-x2019001-eng.
htm
[21] Särndal, C.-E., Swensson, B., and Wretman, J. (1992).Model-Assisted
Survey Sampling. Springer, New York.
[22] Smith, T. M. F. (1994). Sample surveys 1975–1990; an age of reconcilia-
tion? (with discussion).International Statistical Review, 62:5-34.
25

[23] Stone, C.J. (1977). Consistent Nonparametric Regression.The Annals of
Statistics, 5:595-620.
[24] United Nations (2019).National Quality Assurance Frameworks Man-
ual for Official Statistics.https://unstats.un.org/unsd/methodology/
dataquality/
[25] Valliant, R., Dorfman, R. M., and Royall, R. M. (2000).Finite Population
Sampling and Inference: A Prediction Approach. Wiley, New York.
[26] Zhang, L.-C., Sanguiao-Sande, L. and Lee, D. (2025). Design-based pre-
dictive inference.Journal of Official Statistics, 41:404-432.
26
