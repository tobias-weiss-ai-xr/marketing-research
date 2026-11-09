---
title: 'Classical methods for modern applications: synthetic tabular data generation using lightweight
  discrete response continuous latent variable model'
url: https://arxiv.org/abs/2610.21674
category: ai-marketing
subcategory: measurement
date: 2026-10
venue: ''
authors:
- Bartosz Barzdajn
- Mateusz Krzysztoń
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.21674
pages: 24
chars: 64980
fetched_at: '2026-11-08T13:30:39+00:00'
kb_version: 1
---

# Classical methods for modern applications: synthetic tabular data generation using lightweight discrete response continuous latent variable model

Classical methods for modern applications: synthetic
tabular data generation using lightweight discrete response
continuous latent variable model.
Bartosz Barzdajn*1 and Mateusz Krzyszto ´ n1
1NASK National Research Institute
October 16, 2026
Abstract
In this paper, we present a lightweight algorithm for modelling tabular data containing both continu-
ous and discrete variables. The method uses empirical marginal distributions and a selected quantile
function to transform the data into a continuous latent space, where a distribution of choice, e.g. a
multivariate Gaussian, can be efficiently estimated and applied. While this approach is closely related
to classical well-established machine learning methods, we present a novel adaptation that fits well
within the contemporary computational ecosystem.
Unlike in the case of deep architectures, it results in a simple implementation with few dependen-
cies, robust training/estimation, as well as efficient sampling. The transformation preserves complex
marginal distributions and correlations, providing high-fidelity models, especially for data with uni-
modal distributions.
One of the key characteristics of the proposed approach is its continuous representation of discrete
variables. While highly desirable, this introduces a significant challenge, since a single observation
corresponds to a region rather than a point in the latent space. We show that this ambiguity naturally
leads to a Monte Carlo expectation-maximisation (MCEM) formulation, whose auxiliary objective can
be expressed as a weighted latent-space likelihood. This, in turn, allows conventional maximum-
likelihood estimators to be used within an efficient and robust optimisation procedure.
1 Note on the future revisions of this draft
While this manuscript presents the complete scientific contribution, future revisions may further elab-
orate on selected aspects, expand the discussion of related work, and adapt the presentation to the
requirements of a specific journal. We greatly appreciate any comments, suggestions, or relevant refer-
ences that could help us further improve the paper.
2 Motivation
The problem we address is the development of data-generating distributions for mixed-type data, with
particular emphasis on the formal treatment of continuous and discrete features. This work is motivated
by a cybersecurity use-case within the MIRANDA project, where we are developing a fit-for-purpose
predictive component for a cybersecurity digital twin (CDT).
*bartosz.barzdajn@nask.pl
1
arXiv:2610.21674v1  [cs.LG]  15 Oct 2026

The component will have two main tasks. The first is to generate synthetic data based on historical net-
work traffic. These data can be used to test other CDT components, balance training sets, and pre-train
more complex models while limiting overfitting. The second is to estimate the likelihood of observed
network data, which may be applied to tasks such as evaluation of decision boundaries for anomaly
detection.
The cybersecurity context imposes several practical requirements. The models must generate represen-
tative, high-fidelity samples. At the same time, it should be easy to implement with few dependencies,
if any at all, allowing independent maintenance and limiting the attack surface. It also must also be
efficient enough to operate within a larger architecture with components competing for resources, and
robust enough to be trained without extensive diagnostics or monitoring. As a result, rather than chas-
ing "state-of-the-art" we are aiming at "fit-for-purpose".
These requirements led us to revisit classical methods rather than rely on deep architectures. In par-
ticular, we draw inspiration from both classical discrete-response latent variable models [1] and data
transformations closely related to Gaussian copula modelling [2]. As we will see, this initially proved to
be a difficult marriage, ultimately leading to a novel implementation of the expectation-maximisation
algorithm. The resulting method is surprisingly simple to implement despite its formal treatment of
mixed-type data and strict handling of discrete variables. We believe that the derivation of this algo-
rithm, and its implementation, may have broader relevance, especially in contexts with requirements
similar to those described above. One of the advantages of our approach is its simple, yet explicit, con-
tinuous latent representation for all feature types, which opens a path for straightforward interpolation
and extrapolation of mixed-type data-generating distributions.
3 The core concept and its relation to other methods
Before moving forward, it is worth emphasising that the literature on generative modelling, latent-
variable methods, and copula-based approaches is extensive. Here, we focus on a small number of
representative methods that, in our view, help place the proposed approach in a broader context and
highlight its relationship to contemporary methods, while at the same time providing a smooth intro-
duction to the rather involved derivation that follows.
In many real-world applications, training data follow complex distributions that are difficult to model
directly. The core idea behind many solutions is to transform the data into a space where much simpler,
well-established distributions can be applied. This approach underlies methods such as normalising
flows [3], VAEs [4] and even, in some sense, GANs [5]. The main differences lie in how the transforma-
tion is structured and learned.
While in principle these transformations may be arbitrary, as argued above, we favour robust statistical
methods that can be evaluated directly from the data. Furthermore, since we wish to perform both
generation and inference, we require explicit access to the latent space, just as in the case of VAEs. This
allows likelihoods to be evaluated using the latent distribution (see e.g. [6] or Appendix D).
Therefore, we choose a simple two-stage transformation, similar to that used in Gaussian copula mod-
elling, although we do not restrict ourselves to the specific latent distribution typically associated with
copula models. In principle, the second stage may be defined by any continuous distribution with a
well-defined quantile function. Each feature is first mapped through its empirical CDF to the quantile
space and then through a selected quantile function, which defines the desired marginal distribution in
the latent space.
This is a well-established approach originating from Gaussian copula modelling, albeit somewhat dif-
ferent from the way copulas are commonly introduced. While the copula itself is formally defined in
the quantile space, practical Gaussian copula models are often estimated through observations trans-
formed into a latent Gaussian representation. The same two-stage transformation serves as the starting
2

point for our approach. Figure 1 illustrates the transformation for a single feature and how it is mapped
to a Gaussian target distribution.
Figure 1: Illustration of the two-stage quantile transformation used to construct the latent representa-
tion. While the transformation reshapes the marginals into the desired form, the dependence structure
remains non-trivial.
Note that this operation is applied independently to each feature and therefore only reshapes the
marginal distributions into the desired form. For multivariate data, much of the complexity of the
distribution may still be preserved through the correlation structure. This is something we must keep
in mind when constructing the model of our data.
While this approach seems straightforward, in our context we need to address another layer of com-
plexity, namely the treatment of discrete variables. Real-world network data usually contain both con-
tinuous and discrete features, and this remains a recognised challenge for generative modelling frame-
works.
One solution, often used in normalising flows, is dequantisation (see, e.g. [7]). In other words, replacing
discrete variables with their continuous surrogates. In practice, this means adding noise to discrete ob-
servations before training, so that they can be treated as continuous. From the point of view of marginal
transformations, this implicitly replaces a step-wise empirical CDF with a smoothed approximation,
where the smoothing kernel depends on the chosen noise distribution.
Copula Flows represent a related but more formal route [8]. Since discrete CDFs are step-wise and
copulas are not unique for discrete data, the method uses the distributional transform [9]. A discrete
observation is mapped stochastically to a value inside the corresponding jump of the CDF, which gives
a continuous uniform representation suitable for flow-based copula modelling. From our perspective,
this is particularly interesting because a single discrete observation is no longer associated with a single
quantile value, but with a whole range of admissible quantile representations. This will become one of
the core concepts behind our method.
Another approach can be found in CTGAN [10], which is often used as a default method for synthetic
tabular data generation. CTGAN handles mixed-type tabular data by changing the representation of
both variable types before training. Discrete features are represented by one-hot vectors, while con-
tinuous features are represented by two quantities: a mode indicator of a pre-fitted Gaussian mixture
and the value normalised within that mode. In other words, CTGAN introduces, in some sense, an
intermediate representation, in which continuous variables are partly described through discrete mode
3

labels.
Naturally, as mentioned before, such a review can never be even close to complete. While many recent
developments focus on achieving state-of-the-art performance, often through diffusion models [11, 12]
or based on foundation models for tabular data such as TabPFN [13], some researchers, similarly to our
work, favour classical statistical modelling over deep architectures. One such example is Synthsonic
[14], which combines a sequence of statistical transformations with Bayesian network modelling and
discriminate learning.
Continuing the line of thought introduced by the distributional transform, we take a formal approach
to the problem of mixed-type features, originally inspired by the ClustMD model [15], but in fact rooted
more broadly in the discrete-response latent variable framework introduced by Muthén [1].
The latent representation remains continuous, while discrete observations correspond to regions of the
latent space. Unlike dequantisation, we do not replace discrete observations with continuous surro-
gates, but instead model the ambiguity they imply.
The price we pay for this formal treatment is that inference becomes more involved. As we shall see,
the resulting optimisation problem naturally leads to a Monte Carlo expectation-maximisation (MCEM)
formulation. However, the corresponding auxiliary objective can be expressed as a weighted likelihood
in the latent space, turning what initially appears to be a difficult inference problem into a fairly straight-
forward optimisation procedure.
As indicated before, the benefit is that the latent representation remains continuous for all feature types.
This makes the model easy to estimate, efficient to sample from, and robust when interpolating between
observed conditions. It also provides a natural framework for future regression models, where changes
in device or deployment characteristics can be expressed through changes in the parameters of the
latent distribution.
4 The method
This section is intended as a high-level overview of the method, while a more complete treatment can
be found in Appendix A. We aim to keep the discussion accessible to readers who may be less familiar
with classical machine learning and statistical modelling. However, for the sake of brevity and clarity,
we intentionally omit some technical subtleties and focus more on the essential concepts and the novel
elements of the derivation. Readers primarily interested in the utility of the method may refer to the
following section.
The starting point for our reasoning is the Evidence Lower Bound (ELBO) [16], [17] – the go-to identity
for latent variable modelling. The goal is to approximate the solution that maximises the likelihood
of data under specific values of the model parameters, while the model is defined on the latent space,
hidden behind a reversible transformation, where latent states are not directly observable.
In general, the core idea is to "expose" the latent variables and define the joint distribution together with
ones that are observable. Then, instead of dealing with intractable integration’s that arise, we find the
lower bound of the likelihood. By maximising this bound, we match a surrogate objective for likelihood
maximisation. For convenience, the complete framework is provided in the Appendix B.
We begin by exposing the latent state through a marginalised joint distribution. For now, we do this for
a single pointxin the data space, writing the likelihood as
p(X=x|θ) =
Z
Z
p(X=x, Z=z|θ)dz,(1)
where integration is performed over the volumeZof latent states corresponding to the observationx.
In the above, the likelihood depends on the parameter vectorθ,Xis the random variable representing
the data, andZcorresponds to the latent states. Here, we use a simplified notation wherexandzare
4

vectors in a multidimensional real space.
In the continuous case, we could follow the standard ELBO framework, define the corresponding
expectation-maximisation objective, and proceed with the optimisation (again, see e.g. [16], [17] or
Appendix B). In our case, however, the transformation to the latent space is no longer one-to-one, as the
model assumes a discretised response. We therefore need to consider several key nuances.
Formally, we can define the forward transformation, an "encoder", as
xik →u ik = bFk(xi)→z ik = Φ−1 k (ui)(2)
where ˆFk is the marginal empirical cumulative distribution function (CDF) of data. For the $k$-th
feature, the first step applies column-wise the standard quantile transformation, independently with
respect to each feature, while the second applies another per-feature mapping through the quantile
function of the selected one-dimensional distribution. This is the same procedure as the one illustrated
in Figure 1. In the above, ˆFandΦare vector-valued functions with independent components. We use
the standard normal distribution as the target distribution, hence the notationΦ. In principle, this target
could be replaced by any other proper distribution, although we will see later that this choice plays an
important role.
Let us focus now on the key consequence of the adopted transformation. In the discrete-response case,
a single, i-th observation does not identify a unique latent value. Instead, together with the "decoder""
f, it defines a per-data-point pre-image
Zi ={z:f(z) =x i},(3)
i.e. a set of points corresponding to the specificx i. Since the latent space is continuous,Z i represents
a volume. This will become important later in defining explicitly our joint distribution of latent states
and data, as well as the associated probabilistic measure.
As indicated before, in a regular variational framework, where we take advantage of the ELBO, we do
not optimise the likelihood or log-likelihood directly, as in standard maximum likelihood estimation.
Instead, we aim to maximise the lower bound of equation 1. Going one step further, it is sufficient to
maximise an auxiliary function that consists only of terms depending on the parameters of the latent
distribution. In a similar fashion, we can define the auxiliary functionA(θ)that will serve as our optimi-
sation objective. After dropping the entropy term from the lower bound, it takes the following general
form:
A(θ) =
X
i
Z
Zi
logp(X=x i, Z=z|θ)q i(z)dz.(4)
The result above is very similar to the standard variational framework. The key difference lies in the
limits of integration, which arise from restrictingz|x i to the admissible regionZ i. This restriction is a
direct consequence of the relationship between the step-wise transformation and the joint distribution,
which we will address later. It also induces an observation-specific variational posteriorsq i, supported
only on the corresponding pre-image.
Althoughq’s may be arbitrary, we can show that in a more conventional setting the optimal choice, one
that maximises the lower bound, is the one that also minimises the KL divergence - see Appendix C,
DKL(q(z)∥p(z|x, θ)).
Asqapproaches the latent posteriorp, the bound becomes "tight" and we can approximate our objective.
As a result, we can define variational posteriorsq i as
qi(z) =p(Z=z|X=x i, θ).(5)
5

The notation here is almost identical to the conventional latent posterior on purpose, as we will be using
single latent "parent" model for all observations. However, each time the support will depend explicitly
on the observed response and each one of them will correspond to different restrictions, resulting in dif-
ferent normalisation. This observation-specific posterior will play the role of the probabilistic measure
and define the expectation in the optimisation objective.
Now we can write-down the near-final form of the objective. After applying the probabilistic chain rule,
to factorise the joint distribution, at the end we obtain
A(θ) =
X
i
Z
Zi
log

p(X=x i |Z=z, θ)p(Z=z|θ)| {z }
joint distribution of data and latent var.

 p(Z=z|X=x i, θ)| {z }
probabilistic measure
dz.(6)
At this stage the structure of the objective becomes transparent. As we "go" over the latent space, the
first factor in the joint distribution,p(X=x i |Z=z, θ), is degenerate and equal to one whenzis a part
of the pre-image, and zero elsewhere. Hence, we introduced earlier the domain of integrationZ i. By
restricting it, contributions of the first factor become constant and it can be ignored.
To summarise, the probability measure is obtained by restricting the same parent latent model to the
corresponding pre-image and renormalising. In other words, all observations share a common latent
model, but each observation only "sees" the part of that model that is compatible with its own discrete
response. This is precisely the mechanism that allows us to combine a continuous latent space with
discrete observations.
The remaining difficulty lies in distributionsp(Z=z|X=x i, θ), which defines how probability
is distributed over eachZ i. Although allz∈ Z i are consistent with the observationx i, they are not
equally probable under the model. Their likelihood depends on the latent priorp(Z=z|θ), which in
turn corresponds to the model we wish to find.
This circular dependence naturally leads to an expectation-maximisation (EM) formulation. Given the
current parameter estimateθ (k), we first evaluate the posterior distribution over the latent variables
restricted toZ i, namelyp(Z=z|X=x i, θ(k)). This distribution determines the relative density of the
admissible latent states and defines the expectation step. We then updateθby maximising the expected
log-likelihood of the remaining factor in the joint distribution,p(Z=z|θ), with the expectation taken
under the posterior evaluated atθ (k). This defines the maximisation step.
The computational challenge here is the calculation of integrals for each element of the training set.
This leads to one of the key observations behind our approach. The objective can be written as a sum
of expectations with respect to the measuresp(Z=z|X=x i, θ), and such expectations can be
approximated using the Monte Carlo (MC) method. In a generic form, this approximation is given by
Z
X
h(x)p(x)dx=E p[h(X)]≈ 1 N
NX
i=1
h(xi).(7)
This simplifies the problem significantly, since we can optimise a sum of averages instead of a sum
of integrals. However, this procedure is straightforward only ifx i ∼p, that is, if the samples are
distributed according top. Here, we are dealing with a family of truncated distributions, each defined
over its own truncation region, from which efficient direct sampling may be difficult. In principle, we
could use more advanced methods, such as Markov chain Monte Carlo (MCMC). In practice, however,
applying such methods to an ensemble containing potentially as many distinct distributions as there
are unique data points would be difficult to implement and computationally expensive.
Instead, we can use self-normalized importance sampling (SNIS). Let us focus first on the sampling
procedure. When we have a discrete observation it corresponds not to a single quantile value, but to
a range of possible quantile values defined by the step-wise marginal empirical CDF. We sample these
6

values, transform them into the latent space, and use appropriate importance weights to estimate the
required integrals. This provides a good coverage of the latent space and corresponding pre-image,
since each data point is represented by controllable number of latent samples. As such, it also forms
the basis for the efficient computation of multiple expectations/integrals. The concept of sampling
illustrated in Figure 2.
single sample in the data space
sample all relevant
 quantiles
multiple samples in the latent space
Figure 2: Observation-specific sampling in the continuous latent space. Each discrete observation de-
fines an admissible regionZ i, from which multiple latent representations are generated for Monte Carlo
approximation.
The proposal distribution will have independent marginals, i.e.
q(x1, . . . , xd) =q 1(x1)q2(x2)· · ·qd(xd) =
dY
k=1
qk(xk).(8)
This way, not only can we sample each feature separately, but the calculation of the proposal density is
also very simple.
In general, the importance sampling estimate can be written as
Ep[h(X)]≈
NP
i=1
wih(Xi)
NP
i=1
wi
,(9)
where
wi := ϕ(Xi) q(Xi) .(10)
Here,ϕis the target distribution, that is, our parent distribution, for which we wish to calculate the
expectation, andqis a for now described proposal distribution from which we can actually sample. We
can now see why the choice of the distribution used as the basis of our transformation is so important.
It defines the proposal distribution. We can also see, that weights are by definition self-normalising.
Hence the name self-normalized importance sampling (SNIS).
It remains to specify the EM auxiliary function that defines the M-step objective. At iterationk, for a
single observation, we approximate its contribution by
Ai

θ, θ(k)

=
Z
Zi
logp(X=x i |Z=z, θ)p(Z=z|θ)p

Z=z|X=x i, θ(k)

dz,(11)
where the first term is constant within the corresponding integration volume. Approximating the inte-
gral withMsamples from the pre-imageZ i gives the following self-normalized importance sampling
7

estimate:
Ai(θ, θ(k))≈
MX
j=1
logp(Z=z ij |θ) p

Z=z ij |X=x i, θ(k)
ϕ(zij)
1
MP
j=1
p(Z=zij |X=x i,θ(k))
ϕ(zij )
| {z }
normalised weight˜wij
,(12)
wherez ij ∈ Zi are samples from the pre-image of observationx i,ϕ(z)is the distribution used in the
second stage of the transformation and serves as the proposal distribution, for example the standard
normal distribution, andp(Z=z ij |X=x i, θ(k))is the target sampling distribution, which depends on
the parameter estimate from the previous optimisation step. The last terms is the normalisation factor
– sum over all "weights".
Summing the individual contributions over the training set gives the complete auxiliary objective:
A(θ, θ(k))≈
NX
i=1
MX
j=1
˜wij logp(Z=z ij |θ),(13)
where˜wij, just as indicated in the previous equations, are normalised, per-observation, weights. The
maximization step therefore reduces to weighted maximum likelihood estimation of the latent model.
For the multivariate Gaussian considered here, this means estimating the mean vector and covariance
matrix from weighted samples, where the weights are determined by the current estimate of the model
parameters.
5 The final algorithm
The model parameters are estimated iteratively using the EM algorithm, which typically converges
within 10–30 iterations. At each iteration, the E-step produces a weighted sample representation of the
latent space, reducing the M-step to a standard weighted maximum-likelihood problem.
For the Gaussian latent prior with parametersθ= (µ,C), the updated mean is given by
µ=
NX
i=1
MX
j=1
˜wijzij,(14)
wherez ij denotes a sample drawn from the proposal distributionϕover the pre-imageZ i associated
with observationx i. The normalised importance weights are
˜wij = wijX
j
wij
,(15)
with unnormalised weights
wij = p

Z=z ij |x i, θ(prev)
ϕ(zij) ,(16)
wherep(· |xi, θ(prev))is in principle the observation-specific posterior induced by the latent prior from
the previous iteration. Thanks to the use of self-normalised importance sampling (SNIS), and because
the observation-specific posteriors differ only by a normalising constant, the importance weights can be
evaluated using the underlying "parent" latent model. In our case it would be the multivariate Gaussian
distribution.
Finally, using the biased covariance estimator, the covariance matrix is updated as
8

C=
NX
i=1
MX
j=1
˜wijzijz⊤ ij .(17)
In practice, we use an unbiased covariance estimator, which requires a slightly modified update. Re-
gardless of the specific estimator, each EM iteration follows the same principle: the current prior pa-
rameters define the importance weights, which are then used to estimate an updated set of latent model
parameters.
It immediately becomes apparent that, despite the rather involved derivation, the resulting algorithm
is remarkably simple. Most of the implementation complexity stems from managing the sampling
procedure and normalising estimates obtained from observation-specific regions of the latent space.
6 Performance evaluation
We decided that the best way to evaluate the utility of our model is through a series of controlled
experiments using synthetic data drawn from a non-trivial parametric distribution with a controllable
level of difficulty. For each difficulty level, we sample a training set, fit the evaluated models, we will
explain the plural in a moment, and compare the data they generate with an independent reference
sample from the same distribution. We repeat this procedure across different parameters, observe how
performance changes and possible identify the conditions under which our model remains useful. To
provide meaningful points of comparison, we evaluate methods of varying complexity, including a
zero-shot baseline, our model, and an industry-standard CTGAN.
The benchmark distribution should reflect the main challenges posed by the datasets addressed in this
work. These include mixed data types, both discrete and continuous, strong correlations, and occa-
sional near-deterministic relationships between features. Such relationships may arise from feature
engineering or when the same quantity is obtained from different sources, for example, when one value
is inferred and another is measured directly. The benchmark should also expose a key limitation of our
model: its difficulty in representing distributions with ambiguous marginals, such as the commonly
used two-moons benchmark or distributions with a ring-like topology. We therefore require a paramet-
ric family that can vary between these challenging structures and simpler distributions that our model
can easily represent.
We found that the Rosenbrock distribution meets these requirements particularly well. It is easy to sam-
ple from, and its unnormalised density can be evaluated directly. Despite having only two parameters,
it can vary from an approximately elliptical distribution to one with strongly ambiguous marginals.
To reflect the mixed-type setting central to this work, we additionally discretise selected dimensions
of the sampled data. We decided that two-dimensional version will serve us well. Figure 3 illustrates
examples of distributions for selected parameters and respective discretised samples.
9

Figure 3: Unnormalised densities of the Rosenbrock distribution and corresponding discretised samples
for selected parameter settings.
The case study covers 35 four-dimensional Rosenbrock distributions, obtained from all combinations of
a∈ {0.5,1.5,2.0,2.5,3.0}andµ∈ {0.0,0.5,1.0,1.5,2.0,2.5,3.0}. For each pair of parameters, we draw
12,500 observations and discretise two dimensions,xandy, while leavinguandvcontinuous. Figure 4
illustrates a comparison between the reference (test data) and data generated using proposed method.
This example may serve well as a qualitative easement of a example with intermediate difficulty.
10

Figure 4: Reference test data (gray) and sample obtained using proposed method - DRLVM (black).
Results represent Rosenbrock distribution case study with scale and location parametera= 2.5and
µ= 2.0repectively.
In the quantitative assessment, we divide the resulting mixed-type dataset into training and test sets
using an 80:20 split. We evaluate three methods of increasing complexity: a quantile-transformation
baseline with a fitted Gaussian distribution 1, the proposed DRLVM, and CTGAN with optimised hy-
perparameters. We use each fitted model to obtain 2500 observations, which are compared with the
corresponding test set using energy distance,
bD(X, Y) = 2 nm
nX
i=1
mX
j=1
∥xi −y j∥2 − 1 n2
nX
i=1
nX
j=1
∥xi −x j∥2 − 1 m2
mX
i=1
mX
j=1
∥yi −y j∥2 ,(18)
whereX={x i}n i=1 denotes the generated sample,Y={y j}m j=1 denotes the corresponding test sample,
and∥·∥ 2 is the Euclidean norm. Lower values indicate greater agreement between the generated and
reference distributions. Results this comparison are presented in figure 5. The results, including their
surprising aspects will be discussed in the following section.
1This method consist of dequantisation by adding Gaussian noise, transforming data into quantile space by applying feature-
wise empirical CDF, projecting each column into one dimensional Gaussian quantile function and fitting a Multivariate normal
distribution. During generation discrete components are snapped to the closest value in the training set. This method can be
viewed as dequantised version of Gaussian copula modelling and a one-shot version of the proposed DRLVM.
11

Figure 5: Energy distance between the generated and reference samples for the QTDQ baseline, DR-
LVM, and CTGAN. The left and centre panels show the distance as a function of the Rosenbrock loca-
tion parameterµand precision parametera, respectively. Lines show the mean across the remaining
parameter settings, while shaded regions indicate the corresponding 0.95 confidence interval. The right
panel summarises the results across all 35 benchmark scenarios. Error bars indicate the variation be-
tween scenarios. Lower values indicate better agreement with the reference distribution.
7 Summary, discussion and future work
Taking advantage of quantile transformations can provide robust, yet high-fidelity statistical models
of data with simple latent priors. In this context, the formal treatment of discrete responses leads to
a rather involved derivation, but the resulting algorithm can be remarkably simple. With the right
approach, each EM iteration was reduced to evaluation of importance weights and performing simple
weighted maximum-likelihood estimation. For the Gaussian latent model considered here, this further
reduces to calculating a weighted mean and covariance matrix. The introduced method is therefore
computationally efficient and straightforward to implement, reducing resource usage, the number of
required external dependencies and the attack surface as a result.
Synthetic tests confirmed that the method is capable of generating high-fidelity samples, even for diffi-
cult data distributions, despite the fairly simple underlying latent model, which turn is also a significant
advantage. Furthermore, comparison with its one-shot counterpart, demonstrated that in many cases,
there is measurable benefit from applying a more formal approach rather then relying on dequantisa-
tion. Finally, explicit access to the latent space allows us to evaluate the likelihood of samples in the
data space, providing a direct way to obtain, for example, class probabilities or probabilistic decision
boundaries in anomaly detection.
The comparison with CTGAN produced an unexpected result. Although CTGAN can represent a much
broader family of distributions and reproduced the overall shape of the Rosenbrock distribution more
accurately, it achieved substantially higher energy distances than the proposed method. A closer ex-
amination suggests that CTGAN failed to match the narrow concentration of probability mass around
specific dimensions of the data manifold, despite the use of optimised hyperparameters. More detailed
results and visual comparisons will be provided in the accompanying computational notebook that will
be referenced in the next revision of this draft.
While certainly CTGAN is capable of obtaining much better results, for example with tailored pre-
12

processing, after all, our model most likely is a subset of distributions that CTGAN can in principle
represent, the result demonstrates how important is robustness of ML solutions. This aspect is quite
often neglected and lost in sophisticated pipelines.
When it comes to the future of our approach we would like to emphasise the following. The introduced
methodology consists of replaceable stages, each with a well-defined purpose. Both the transformation
and the latent model may be substituted without changing the overall structure of the algorithm. In
principle, any model with a practical weighted-likelihood estimator can be "inserted" into the EM loop,
and any distribution with a well-defined quantile function can be used in the second stage of the trans-
formation. It will be interesting to see whether richer latent models, such as mixture models, capable
of representing a much broader family of data distributions, will maintain desired "simplicity" of the
implementation.
Finally, simple parametric latent models offer a natural extension towards conditional generation, in-
cluding interpolation and prediction. An unconditional empirical CDF may, however, remove trends
that the regression model is intended to represent. On the other hand, it may be possible to replace
it with a conditional transformation based on quantile regression. The resulting conditional "decoder"
could then describe how entire marginal distributions change with the explanatory variables. Although,
this would address only part of the problem, since the dependence structure may also change. Some-
what in the spirit of copula modelling, one could therefore model the conditional marginals and the
parameters of the latent dependence structure separately. Such an extension appears natural within the
proposed framework, although its estimation is likely to be considerably more involved.
8 Acknowledgements
This paper was written as part of the MIRANDA project that received funding from the European
Union’s Horizon Europe Research and Innovation Programme under grant agreement No. 101168144
(MIRANDA). The views and opinions expressed are those of the authors only and do not necessarily
reflect those of the European Union or the European Cybersecurity Competence Centre. Neither the
European Union nor the granting authority can be held responsible.
9 References
[1] Bengt Muthén. “A General Structural Equation Model with Dichotomous, Ordered Categorical,
and Continuous Latent Variable Indicators”. In:Psychometrika49.1 (Mar. 1984), pp. 115–132.ISSN:
0033-3123, 1860-0980.DOI:10.1007/BF02294210.
[2] Abe Sklar. “Random Variables, Joint Distribution Functions, and Copulas”. In:Kybernetika9.6
(1973), pp. 449–460.
[3] Danilo Jimenez Rezende and Shakir Mohamed.Variational Inference with Normalizing Flows. Ver-
sion 6. 2015.DOI:10.48550/ARXIV.1505.05770.URL:https://arxiv.org/abs/1505.
05770(visited on 07/16/2026). Pre-published.
[4] Diederik P Kingma and Max Welling.Auto-Encoding Variational Bayes. Version 11. 2013.DOI:
10 . 48550 / ARXIV . 1312 . 6114.URL:https : / / arxiv . org / abs / 1312 . 6114(visited
on 07/16/2026). Pre-published.
[5] Ian J. Goodfellow et al.Generative Adversarial Networks. Version 1. 2014.DOI:10.48550/ARXIV.
1406 . 2661.URL:https : / / arxiv . org / abs / 1406 . 2661(visited on 07/16/2026). Pre-
published.
[6] Simon J. D. Prince.Understanding Deep Learning. Cambridge, Massachusetts London, England:
The MIT Press, 2024. 1 p.ISBN: 978-0-262-04864-4 978-0-262-37710-2.
13

[7] Jonathan Ho et al.Flow++: Improving Flow-Based Generative Models with Variational Dequantization
and Architecture Design. Version 2. 2019.DOI:10.48550/ARXIV.1902.00275.URL:https:
//arxiv.org/abs/1902.00275(visited on 08/25/2026). Pre-published.
[8] Sanket Kamthe, Samuel Assefa, and Marc Deisenroth.Copula Flows for Synthetic Data Generation.
Jan. 3, 2021.DOI:10 . 48550 / arXiv . 2101 . 00598. arXiv:2101 . 00598 [stat.ML].URL:
http://arxiv.org/abs/2101.00598(visited on 08/25/2026). Pre-published.
[9] Ludger Rüschendorf. “On the Distributional Transform, Sklar’s Theorem, and the Empirical Cop-
ula Process”. In:Journal of Statistical Planning and Inference139.11 (Nov. 2009), pp. 3921–3927.ISSN:
03783758.DOI:10.1016/j.jspi.2009.05.030.
[10] Lei Xu et al.Modeling Tabular Data Using Conditional GAN. Version 2. 2019.DOI:10 . 48550 /
ARXIV.1907.00503.URL:https://arxiv.org/abs/1907.00503(visited on 08/25/2026).
Pre-published.
[11] Jayoung Kim, Chaejeong Lee, and Noseong Park.STaSy: Score-based Tabular Data Synthesis. May 29,
2023.DOI:10 . 48550 / arXiv . 2210 . 04018. arXiv:2210 . 04018 [cs.LG].URL:http : / /
arxiv.org/abs/2210.04018(visited on 08/25/2026). Pre-published.
[12] Akim Kotelnikov et al. “TabDDPM: Modelling Tabular Data with Diffusion Models”. Version 2.
In: (2022).DOI:10.48550/ARXIV.2209.15421.
[13] Noah Hollmann et al.TabPFN: A Transformer That Solves Small Tabular Classification Problems in a
Second. Sept. 16, 2023.DOI:10.48550/arXiv.2207.01848. arXiv:2207.01848 [cs.LG].
URL:http://arxiv.org/abs/2207.01848(visited on 08/25/2026). Pre-published.
[14] Max Baak et al. “Synthsonic: Fast, Probabilistic Modeling and Synthesis of Tabular Data”. In:
Proceedings of the 25th International Conference on Artificial Intelligence and Statistics. Ed. by Gustau
Camps-Valls, Francisco J. R. Ruiz, and Isabel Valera. Vol. 151. Proceedings of Machine Learning
Research. PMLR, Mar. 28–30, 2022, pp. 4747–4763.
[15] Damien McParland and Isobel Claire Gormley. “Model Based Clustering for Mixed Data: clustMD”.
In:Advances in Data Analysis and Classification10.2 (June 2016), pp. 155–169.ISSN: 1862-5347, 1862-
5355.DOI:10.1007/s11634-016-0238-x.
[16] Kevin P . Murphy.Machine Learning: A Probabilistic Perspective. 4. print. (fixed many typos). Adap-
tive Computation and Machine Learning Series. Cambridge, Mass.: MIT Press, 2013. 1071 pp.
ISBN: 978-0-262-01802-9.
[17] Christopher M. Bishop.Pattern Recognition and Machine Learning. Information Science and Statis-
tics. New York: Springer, 2006.ISBN: 978-0-387-31073-2.
A Complete derivation of the DRLVM model
A.1 Initial definition of the optimisation objective
The goal is to model the data-generating distribution efficiently. As mentioned before, we achieve this
by introducing a transformation to a latent space, together with a well-defined inverse process, such
that the distribution is simpler in the latent space. Generating new synthetic data then involves sam-
pling from this space and transforming the samples back to the original data space. This approach can
maintain high fidelity while relying on relatively simple parametric distributions, but it requires us to
model unobserved latent states. A common solution in such cases is to use variational methods. There-
fore, our derivation begins with one of the key identities of latent-variable modelling, the Evidence
Lower Bound (ELBO).
14

We encourage readers to visit other resources for further details. For convenience, we present our own
derivation in Appendix B. Note that, while our method is rooted in this framework, for the sake of
clarity, we will only provide a brief overview and focus on the key, from our perspective, elements.
Our goal is to find a latent distribution that maximises the likelihood of data. The core idea is to "expose"
the latent variables and define the a joint distribution together with variables that are observable. We
do this by introducing its marginalised ("integrated-out") version
p(X=x|θ) =
Z
Z
p(X=x, Z=z|θ)dz.(19)
In the above, left -hand side is the likelihood of data given the parametersθ,Xis the random variable
representing the data andZcorresponds to relevant latent states.
From the multiplicativity of probability and the fact that measurements themselves are independently
distributed, we know that it is preferable to work with log-likelihoods. However, this standard trans-
formation, that usually allows us to simplify the problem straightaway, because of the integral does not
gives us much in this case.
Instead of maximising the likelihood directly, after rather lengthy transformations that involve Jensen’s
inequality, we can derive the lower bound on the log-likelihood (see Appendix B). This leads to a ver-
sion of the problem that is much easier to work with. For a single data point it is defined as
ℓ(θ)≥E q(z) [logp(X=x i, Z=z)] +H(q(z)).(20)
whereθrepresents the model parameters,x i is an individual observed data point. The termq(z)is
the variational distribution, which in principle is arbitrary, but in fact, as we will see later, should
approximate the true posterior. Note thatE q(z) [·]denotes the expectation taken with respect to this
distribution. Informally
Eq(z) [. . .] =
Z
. . . q(z)dz.(21)
Finally,H(q(z))is the Shannon entropy of the variational distribution, defined asH(q(z)) =−E q(z) [logq(z)],
which regularisesqand prevents it from "collapsing". By maximising the lower bound with respect to
the model parameters, we are also approaching the maximum-likelihood solution. Unfortunately, as a
result of this transformation, we have to deal with the ambiguity introduced byq(z).
A.2 The transformation
As mentioned earlier, this model constructs a joint distribution that involves a mapping through the
empirical cumulative distribution function (CDF). The transformation proceeds in two steps. First, an
observationx i is mapped to the quantile space:
uij = ˆFj(xij) = 1 N
NX
i′
I(xi′j ≤x ij),(22)
and subsequently expressed as a latent variable:
zij =f(x ij) = Φ−1 j (uij) = Φ−1 j  ˆFk(xij)  .(23)
Here,I(·)denotes the indicator function and ˆFis the empirical CDF. Throughout this work we use
the standard normal distribution as the target distribution, hence the use of the symbolΦto denote its
CDF. Note that all transformations are performed independently for each column $j$-th (feature), and
therefore ˆFrepresents the marginal CDF for this specific feature.
This structure combines the empirical distribution with a Gaussian target, creating, in the spirit of a
15

Gaussian copula, a "normalised" representation of the data. The inverse mapping proceeds by first
returning to the quantile space viau ij = Φ(z ij)and then applying the inverse empirical CDF,x ij =
ˆF −1 j (uij). More precisely, the inverse transformation selects the valuex ij corresponding to the interval
of the empirical CDF that containsu ij.
For discrete variables, the CDF is a step function. Consequently, only the decoder, that is, the inverse
transformation, is deterministic, since it represents a many-to-one mapping. The encoding operation, in
contrast, is one-to-many: a single value in the data space can be represented by multiple latent states. To
address this ambiguity, we adopt the concept of the distributional transform [cite] and assume that the
latent variable is uniformly distributed within the admissible region. Here, we refer to the intermediate
stage of the transformation, namely the quantile space. This concept will become clearer when we
introduce the sampling procedure illustrated in Figure 2. For the moment, however, let us focus on the
derivation of the objective.
A.3 Auxiliary objective function for discrete variables with continuous latent rep-
resentation
The entropy term in the ELBO does not depend onθ, so for optimisation purposes we can focus on the
joint distribution. Using the chain rule, for a given realisationz i, we have
p(X=x i, Z=z i |θ) =p(X=x i |Z=z i, θ)p(Z=z i |θ).(24)
The key consideration here is that we are modelling discrete data through the discretised response of
a continuous latent. The conditional distributionp(X|Z, θ)is degenerate, as it is induced by the
empirical CDF responsible for the discretisation. For anyzsuch thatf(z) =x i, wheref:= ˆF −1 ◦Φ, the
probability mass is equal to one, and zero elsewhere. To deal with this complex setting, we introduce
the pre-image set
Zi ={z:x i =f(z)},(25)
and use it to define the limits of integration, which in turn facilitate the discretisation. The setZ i
corresponds to the interval of latent valueszfor which the mapped quantileu= Φ(z)lies within the
bin associated withx i. This allows the problem to be expressed in terms of integrals over well-defined
regions, thereby avoiding the discontinuities introduced by the empirical CDF.
Having introduced the pre-image setsZ i, we can define the auxiliary functionA(θ), which we opti-
mise in place of the ELBO. Sincex i is associated with a set of admissible latent values rather than a
single latent state, the objective integrates over the corresponding regions in the latent space forcing an
introduction of observation-specific variational posteriorq i, yielding
A(θ) =
X
i
Z
Zi
logp(X=x i, Z=z|θ)q i(z)dz.(26)
As noted earlier, the selection oq i is, in principle, arbitrary. While in the standard ELBO formulation
the optimal selection approaches the latent posterior, in our case, we have to deal with a whole set
oq i, one per each regionZ i. We therefore introduce ansatz an observation-specific density obtained
by restricting the single "parent" posterior to the corresponding pre-image and renormalising. We will
write this as
qi(z) =p(Z=z|X=x i, θ).(27)
While in this notation the result looks very standard, we have remember about the normalisation we
discussed just a moment ago and that the condition onx i has an important meaning here. In other
words, each distinct pointx i redirect us to a pre-defined region of the latent space, where discretised
response induces appropriate normalisation of the variational density.
16

As noted earlier, the choice ofq i is, in principle, arbitrary. In the standard ELBO formulation, the
optimal choice approaches the latent posterior. In our case, however, we must deal with a family of dis-
tributionsq i, one for each regionZi. We therefore introduce an observation-specific density obtained by
restricting a single "parent" posterior to the corresponding pre-image and subsequently renormalising
it. We write
qi(z) =p(Z=z|X=x i, θ),(28)
whereprepresent the truncated and normalised "parent". Although this expression appears entirely
standard, it is important to keep in mind the normalisation discussed above and the specific role played
by the conditioning onx i. Each observationx i identifies a pre-defined region of the latent space, and
the discretised response induces the corresponding normalisation of the variational density within that
region. In other words, the particular/per-observation posterior is not defined over the entire latent
space but only over the subset of latent states consistent with the observation under the empirical CDF
mapping.
Finally, substituting the conditional structure obtained from the chain rule, we arrive at
A(θ) =
X
i
Z
Zi
log

p(X=x i |Z=z i, θ)p(Z=z i |θ)| {z }
joint distribution of data and latent var.

 p(Z=z i |X=x i, θ)| {z }
probabilistic measure
dz.(29)
At this point, the structure of the objective becomes transparent. The first factor in the joint distribution,
p(X=x i |Z=z, θ), is degenerate: it is equal to one on the integration domainZ i and zero elsewhere.
Since the integration is restricted toZ i, this term remains constant throughout the integral and can
therefore be omitted from further consideration. The second factor,p(Z=z|θ), corresponds to the
latent prior and contains the parameters of interest.
As a result, the objective takes the form of the expected log-likelihood of the latent prior over the ad-
missible latent region associated with each observation.
A.4 From a vicious cycle into a successful optimisation procedure.
The remaining difficulty lies in the conditional distributionp(Z=z|X=x i, θ), which determines
how probability mass is distributed over the pre-imageZ i. Although allz∈ Zi are consistent with the
observationx i, they are not equally probable under the model. Their relative probability is governed
by the latent priorp(Z|θ), which is itself the object of estimation.
This creates a circular dependence that naturally leads to an expectation-maximisation (EM) formula-
tion. Given a current parameter estimateθ (k), we first evaluate the posterior distribution over latent
variables restricted toZ i, namelyp(Z|X=x i, θ(k)). This distribution assigns relative weights to
the admissible latent states and constitutes the expectation step. We then updateθby maximising the
corresponding expected weighted log-likelihood under the current parameter estimate, yielding the
maximisation step.
A.5 Monte Carlo approximation and the self-normalising importance sampling
(SNIS)
At this point, we need to address the computational challenges associated with the proposed objective.
We have deliberately expressed it as a sum of expectations (see Equations 21 and 29). The resulting
difficulty is that we must evaluate many integrals, often in high-dimensional spaces. Fortunately, ex-
17

pectations of this kind can be approximated efficiently using Monte Carlo (MC) sampling:
Ep[h(x)]≈ 1 N X j h(xj),wherex j ∼p(x),(30)
where, for the moment,hdenotes an arbitrary well-behaved function. This approximation is particu-
larly attractive in the context of probabilistic integrals.
We ultimately wish to sample from the distributionp(Z=z|X=x i, θ)restricted to the pre-image
Zi. However, given the large number of expectations that must be evaluated, even efficient sampling
from such constrained regions can become challenging. In principle, one could resort to Markov chain
methods or rejection sampling. In our case, however, both approaches are likely to be computationally
prohibitive. For example, a straightforward implementation based on Markov chains would require
maintaining a separate chain for every observation, each exploring its own admissible region in the
latent space.
A better alternative is provided by importance sampling. Rather than drawing samples directly from
each restricted distribution, we can sample from a more convenient proposal distribution and account
for the discrepancy through appropriately chosen importance weights. As we will see, this allows the
expectations appearing in the objective to be approximated quite efficiently.
Here, we arrive at one of the key elements of the proposed approach. For each observationx i, we
draw samples uniformly from the corresponding quantile interval, in accordance with the distribu-
tional transform, and map them through the second stage of the transformation into the latent space.
This procedure is illustrated in Figure 2. In this way, we obtain a set of samples that provides good
coverage of the associated regionsZ i. Although more importantly, the procedure guarantees that every
observation contributes a controllable number samples from its admissible region in the latent space.
Moving forward, our ultimate goal, is to evaluate expectations with respect top(Z=z|X=x i, θ),
that is, the latent model restricted to the regionZ i. The samples constructed above do not follow this
distribution. As a result, they cannot be used directly to estimate the expectation.
This is precisely where importance sampling becomes useful. Although the samples are generated from
a more convenient proposal distribution, their contribution can be reweighted to recover expectations
under thep(Z=z|X=x i, θ).
Consider a truncated distribution
p(x) = 1 C ϕ(x)IA(x), C= Z A ϕ(x)dx,(31)
whereCis the normalisation constant,ϕis the parent distribution, andAis the truncation volume.
Note that these are general consideration and the notation is not related directly to the main derivation.
The goal here is to calculate the expectation of a well-behaved functionfunder this distribution
Ep[f(X)] =
Z
V
f(x)p(x)dx= 1 C Z V f(x)ϕ(x)dx.(32)
Assume that we can only sample fromX i ∼q(x). The expectation can be expressed as a ratio of two
integrals. The numerator is
Z
A
f(x)ϕ(x)dx=
Z
A
f(x) ϕ(x) q(x) q(x)dx=E q

f(X) ϕ(X) q(X)  ,(33)
and the denominator is
C=
Z
A
ϕ(x)dx=E q
 ϕ(X)
q(X)

.(34)
18

The result is:
Ep[f(X)] =
Eq
h
f(X) ϕ(X) q(X)
i
Eq
h
ϕ(X)
q(X)
i .(35)
Given thatX 1, . . . , XN ∼q,
Eq[g(X)]≈ 1 N
NX
i=1
g(Xi).(36)
Then
Ep[f(X)]≈
NP
i=1
f(X i) ϕ(Xi) q(Xi)
NP
i=1
ϕ(Xi)
q(Xi)
.(37)
It immediately transpires that if
wi := ϕ(Xi) q(Xi) .(38)
The above leads to
Ep[f(X)]≈
NP
i=1
wif(X i)
NP
i=1
wi
.(39)
This expression is exactly what we need to address the problem presented in this section. Our compli-
cated sum over integrals can be reduced to a sum over weighted averages.
A.6 SNIS and the final version of the auxiliary objective in our EM framework
Here, all components of the derivation come together. We have shown that Monte Carlo (MC) integra-
tion and self-normalized importance sampling (SNIS) can effectively address the challenges introduced
by discrete variables in latent variable models. These challenges include evaluating the truncated form
of the parent distribution, which must be normalized separately for each observation, and constructing
a proposal distribution based on quantiles and data transformations. The latter, while provides a good
coverage of the latent space, it introduces similar challenges.
The final step is to complete the definition of the EM auxiliary function and the corresponding M-step
optimisation objective. This function now depends explicitly on both the current parameter estimate,
θ(k), and the parameter vector being optimised in the current iteration,θ. For a single observation, in
the k-th iteration, we approximate the integral
Ai

θ, θ(k)

=
Z
Zi
logp(X=x i |Z=z, θ)p(Z=z|θ)p

Z=z|X=x i, θ(k)

dz,(40)
where, as established earlier, the first term equals one throughout the integration regionZ i. UsingM
samples drawn from an observation-specific proposal distribution, we get
Ai(θ, θ(k))≈
MX
j=1
logp(Z=z ij |θ) p

Z=z ij |X=x i, θ(k)
ϕ(zij)
1
MP
j=1
p(Z=zij |X=x i,θ(k))
ϕ(zij )
| {z }
normalised weight
wij (41)
wherez ij ∈ Zi are samples from the pre-image,ϕ(z)is the distribution from the second stage of trans-
formation – the base for our proposal during the sampling that samples each feature independently.
Here we change our notation slightly and the second index is not responsible for indexing the feature,
19

but the sub-sample from approximating the probabilistic integral. This means we still operate with
vectors of data and their latent representations.
Furthermore,p(Z=z ij |θ)now explicitely represents the current model andθthe parameter vector
that we want to optimise in thek+ 1step. Thep(Z=z ij |X=x i)is the variational posterior. Here,
thanks to application of SNIS we can replace it with the distribution that we refereed earlier as the
"parent". In practice, this is our model under previous parametersθ k.
Finally, the complete auxiliary objective is obtained by summing the contributions over all data points,
A(θ, θ(k))≈
NX
i=1
MX
j=1
wij logp(Z=z ij |θ).(42)
The above result is essentially a well-known weighted likelihood problem which, for many models,
including the Gaussian distribution, can be solved efficiently using maximum-likelihood estimates of
θ(the M-step). For example, in the Gaussian case, estimating the expectation reduces to computing
a weighted average. The samplesz ij, wherej= 1, . . . , M, used to compute these estimates, form
an "oversampled" representation of the latent state within the pre-image ofx i, while the weightsw ij
provide an SNIS
In general, at the $(k+1)$-th maximisation step, the parametersθare estimated by maximising a weighted
likelihood over the sampled latent representations. The weights are computed using the model ob-
tained in the previous iteration and approximate the corresponding posterior probabilities. As the
optimisation progresses, they are expected to become increasingly aligned with the target posterior
distribution.
Since each observationx i defines its own truncation regionZ i, the corresponding integral is approxi-
mated using an observation-specific proposal distribution. The importance weightsw ij must therefore
be normalised separately for each observation, over its associatedMlatent samples. This is necessary
because the proposal distribution depends on the truncation region and thus varies across data points.
For the complete objective we just sum-up all contributions from all over-sampled data-points.
To summarise the key idea, each observation corresponds to a different discretisation of the continuous
latent space and therefore to a different posterior distribution. These observation-specific posteriors
are all induced by the same underlying latent model. By pooling evidence across these complemen-
tary "views" of the latent space, we can efficiently recover a single set of parametersθdescribing the
underlying continuous distribution.
The complexity lies in finding the right latent representation. Once this is in place, the resulting algo-
rithm is remarkably simple; see Section 5 to see the description of the final optimisation loop.
B Deriving the ELBO and EM surrogate objective
The Evidence Lower Bound (ELBO) provides one of the standard frameworks for dealing with latent-
variable models. We introduce it by exposing the latent states and writing the likelihood of the observed
data, given the model parameters, as a marginalised joint distribution
p(X=x|θ) =
Z
p(X=x, Z=z|θ)dz.(43)
Here,xrepresents a value in the data space, whilezrepresents a latent state.
We now introduce an arbitrary variational densityq(z)by multiplying and dividing the integrand by
the same quantity. This allows us to rewrite the marginal likelihood as an expectation with respect toq,
i.e.
p(X=x|θ) =
Z
q(z) p(X=x, Z=z|θ) q(z) dz=E q(z)
 p(X=x, Z=z|θ)
q(z)

.(44)
20

Since the same density appears in the numerator and denominator, this operation does not change
the marginal likelihood. Taking the logarithm of both sides, as is standard in maximum-likelihood
estimation, we express the log-likelihood as the logarithm of an expectation
ℓ(θ) = lnE q(z)
 p(X=x, Z=z|θ)
q(z)

.(45)
The problem is that it would be much more convenient to work with the expectation of a logarithm
rather than with the logarithm of an expectation. We can achieve this by applying Jensen’s inequality.
In general, for a concave functionf
f(E[X])≥E[f(X)].(46)
Since the logarithm is concave, the logarithm of an expectation is bounded from below by the expecta-
tion of the logarithm,
ℓ(θ)≥E q(z)

ln p(X=x, Z=z|θ) q(z)  .(47)
We can now define the lower bound on the log-likelihood, which depends on the variational density
and the model parameters. Expanding the logarithm gives the standard Evidence Lower Bound (ELBO)
ELBO(q, θ) =Eq(z) [lnp(X=x, Z=z|θ)]−E q(z) [lnq(z)],(48)
such that
ℓ(θ)≥ELBO(q, θ).(49)
The ELBO consists of the expected joint log-likelihood and the entropy of the variational density,
H(q) =−E q(z) [lnq(z)].(50)
When optimising with respect toθwhile keepingqfixed, the entropy term does not depend on the
model parameters and can be omitted. The relevant objective is therefore the expected joint log-likelihood,
commonly referred to as the EM auxiliary function or $Q$-function,
Q(θ, q) =Eq(z) [lnp(X=x, Z=z|θ)].(51)
C Choosing the variational posterior
The remaining question in Appendix B was how to choose the variational densityq. To answer it, we
consider the Kullback–Leibler divergence betweenq(z)and the true latent posteriorp(Z=z|X=x, θ):
DKL(q(z)∥p(Z=z|X=x, θ)) =E q(z)

ln q(z) p(Z=z|X=x, θ)  .(52)
Using Bayes’ rule,
p(Z=z|X=x, θ) = p(X=x, Z=z|θ) p(X=x|θ) ,(53)
we can rewrite the KL divergence as
DKL(q(z)∥p(Z=z|X=x, θ)) =E q(z) [lnq(z)](54)
−E q(z) [lnp(X=x, Z=z|θ)](55)
+ lnp(X=x|θ).(56)
21

KL(q∥p)
L(q, θ)
lnp(X|θ)
Figure 6: Relationship between the log-likelihood, the Evidence Lower Bound (ELBO), and the KL
divergence. For fixed model parameters, bringingqcloser to the true latent posterior reduces the KL
divergence and tightens the lower bound. Taken from [17].
The first two terms on the right-hand side form the negative ELBO. Rearranging therefore gives
lnp(X=x|θ) = ELBO(q, θ) +D KL(q(z)∥p(Z=z|X=x, θ)).(57)
This decomposition of the log-likelihood provides a basis for interpreting the lower bound. Since the
KL divergence is, by definition, non-negative,
DKL(q(z)∥p(Z=z|X=x, θ))≥0,(58)
the difference between the log-likelihood and the ELBO is always greater than or equal to zero. Fur-
thermore, it is exactly the KL divergence between the variational density and the latent posterior:
lnp(X=x|θ)−ELBO(q, θ) =D KL(q(z)∥p(Z=z|X=x, θ)).(59)
For fixed model parametersθ, the bound is therefore maximised by choosing
q⋆(z) =p(Z=z|X=x, θ).(60)
Under this choice, the KL divergence vanishes and the bound becomes tight:
ELBO(q⋆, θ) = lnp(X=x|θ).(61)
This result provides the basis for the expectation-maximisation procedure. For fixed model parameters,
bringingqcloser to the true posterior tightens the lower bound. Keepingqfixed and maximising the
resulting bound with respect toθ, in turn, brings us closer to the maximum-likelihood estimate. The
EM algorithm alternates between these two steps. This concept is illustrated in the figure
D Likelihood of a sample from the latent distribution (WIP)
Results presented here are standard derivation that can be found in many textbooks. We include them
here for convenience.
Latent-variable models allow us to estimate the likelihood of an observation using the corresponding
latent distribution. We assume a model
z∼p(z) :=p(z|θ),(62)
together with an encoder and decoder,
z=f(x), x=g(z).(63)
22

Given a new observationx, we wish to estimate its marginal likelihoodp(x). From the probabilistic
chain rule,
p(x) =
Z
p(x, z)dz=
Z
p(x|z)p(z)dz=E p(z)[p(x|Z)].(64)
A direct Monte Carlo approximation can be obtained by drawing latent samplesz k ∼p(z)and averag-
ing the corresponding conditional likelihoods as
bp(x) =1 K
KX
k=1
p(x|z k).(65)
In practice, this estimate may be inefficient, since most samples drawn from the latent model can con-
tribute very little to the likelihood of a particular observation. This is especially problematic when
p(x|z)is concentrated within a small region of the latent space.
We can improve the estimate using importance sampling. Letq(z)be a proposal distribution chosen to
place more samples in the region relevant tox. Multiplying and dividing the integrand byq(z)gives
p(x) =
Z p(x|z)p(z)
q(z) q(z)dz=E q(z)
 p(x|z)p(z)
q(z)

.(66)
Given samplesz k ∼q(z), the likelihood can therefore be estimated as
bp(x) =1 K
KX
k=1
p(x|z k)p(zk)
q(zk) .(67)
The remaining question is how to choose the proposal distribution. Using Bayes’ rule,
p(z|x) = p(x|z)p(z) p(x) ,(68)
and rearranging,
p(x) = p(x|z)p(z) p(z|x) .(69)
Comparing this expression with the importance-sampling estimate shows that the optimal proposal is
the latent posterior,
q⋆(z) =p(z|x).(70)
Under this choice, the importance ratio is constant and equal top(x), giving a zero-variance estimate.
In practice, the exact posterior is usually unavailable, but this result provides a useful principle: the
proposal should approximatep(z|x)as closely as possible.
We therefore use a conditional proposalq(z|x)and write
p(x) =E q(z|x)
 p(x|z)p(z)
q(z|x)

≈ 1 K
KX
k=1
wk,(71)
where
wk = p(x|z k)p(zk) q(zk |x) , z k ∼q(z|x).(72)
A simple example is
q(z|x) =N

z|f(x), σ 2 pI  , p(x|z) =N  x|g(z), σ 2 oI  , p(z) =N(z|µ,Σ).(73)
Here,q(z|x)places samples around the encoded representation ofx,p(x|z)measures how well the
23

corresponding latent state reconstructs the observation, andp(z)evaluates that state under the fitted
latent model.
For numerical stability, the calculation is performed in the logarithmic domain. We define
lnw k = lnp(x|z k) + lnp(zk)−lnq(z k |x).(74)
The log-likelihood estimate is then
lnbp(x) = LogSumExp(lnw1, . . . ,lnwK)−lnK.(75)
This provides a generic Monte Carlo estimate of the likelihood of an observation under a latent-variable
model. Its precision depends primarily on how well the conditional proposalq(z|x)covers the parts
of the latent space that make a substantial contribution top(x).
24
