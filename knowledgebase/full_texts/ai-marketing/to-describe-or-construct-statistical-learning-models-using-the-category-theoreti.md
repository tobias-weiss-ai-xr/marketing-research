---
title: To Describe or Construct Statistical Learning Models Using the Category-theoretical Language
url: https://arxiv.org/abs/2608.03706
category: ai-marketing
subcategory: measurement
date: 2026-08
venue: ''
authors:
- Congwei Song
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.03706
pages: 26
chars: 47323
fetched_at: '2026-11-08T13:27:55+00:00'
kb_version: 1
---

# To Describe or Construct Statistical Learning Models Using the Category-theoretical Language

To Describe or Construct Statistical Learning
Models Using the Category-theoretical Language
Congwei Song
August 5, 2026
AbstractStatistical learning is a fascinating field that has long been the
mainstream of machine learning/artificial intelligence. A large number of re-
sults have been produced which can be widely applied to real-world problems.
It also leads to many research topics and also stimulates new research. This
report summarizes some classical statistical learning models and well-known al-
gorithms, especially for amateurs, and provides a category-theoretic perspective
on understanding statistical learning models. The aim is to attract researchers
from other fields, including basic mathematics, to participate in the research
related to statistical learning.
KeywordsStatistical Learning, Statistics, Category Theory, Variational
Models, Neural Networks, Deep Learning
1 Introduction
People have developed plentiful machine learning models, from the simple, such
as linear regression, logistic regression[6], to the complicated, such as deep neural
networks and large language models[5]. However, the models share with the
similar pattern as statistic models. In this report, we will investigate them
preliminarily with the help of category theory.
The main purpose of the paper is not to build a strict theory as in [19], but
to invent some notaions borrowed from category theory to describe complicated
models of machine learning.
The two primary contributions of this paper are:
(1) The utilization of categorical language to describe the models of machine
learning.
(2) The introduction of a unified descriptive approach to construct complicated
models, such as the language models.
As a nontrivial example, the Transformer is constructed based on the so-
called local model or localization trick.
We introduce the following abbreviations and notations.
Abbreviations for classical models:
1
arXiv:2608.03706v1  [cs.LG]  4 Aug 2026

•LDA/QDA: Linear Discriminant Analysis/Quadratic Discriminant Anal-
ysis
•GMM: Gaussian Mixture Model
•PCA: Principal Component Analysis
•ICA: Independent Component Analysis
•NMF: Non-negative Matrix Factorization
•(p)LSA: (Probabilistic) Latent Semantic Analysis
•HMM: Hidden Markov Model
•RNN: Recurrent Neural Network
•LSTM: Long-Short time memory (as a classical design of RNN)
Notations:
•X: sample space
•X ∗ = S t X t: sequential sample space (Kleen closure ofX)
•X: a random variable (rv)
•{X i}: a sample
•X ∗: a sequence of rv with arbitary length
•P(X): distribution of target rvX
•P(X|θ): parametric distribution
•{x λ}: a family/sequence/set indexed byλ
•{x ij}ij: a matrix indexed byi, j
•A:=B:Ais defined asB
•f(x;y): A function ofxandy, whileyis not important in theoretical
analysis and will be omitted in common cases
In the context of machine learning, we use lowercasexto represent rvs.
Furthermore, the “facts” in this paper refer to theorems that are not com-
pletely formalized. However, they can be formalized at any time.
2

2 Category theory
We do note need the entire category theory. Here, it is merely used as a language
for description machine learning.
The category theory studies objects, morphisms/arrows between them, and
functors as a mapping between cats. For simplicity, we will only consider a
category as a family of objects and view functors as a mapping from one family to
another, without explicitly discussing arrows which is the real thrust of category
theory. An object is referred to as a model, and a functor is also called a
“constructor” in this paper.
We will not recall the definition of category theory here, and for more details
about category theory, please refer to [14].
3 Probability Models
Let us depart from the definition of probability models. Probability theory is
truly built on measure theory, where distributions play a crucial role [8–10].
Definition 3.1(Probability Model 1).A probability model is a special measure
space, denoted by(Ω,A, P)where the probaility measurePsatifiseP(Ω) = 1,
Ωis the ambient space, andAis aσ-algebra onΩ.
A measurable mappingXon Ω is calledX-valued rv, if the range ofXis
the measurable space (X,B), also called the sample space ofX.
We will not explain the measure space in details, since what we are interested
in is the following special setting.
Definition 3.2(Probability Model 2).Assume that(Ω,A, P)is any probability
model. Then a probability model derived by the target rvX: Ω→ Xis
(X,B, PX ), PX (B) :=P(X∈B), B∈ B(3.1)
whereX∈Brepresent the event{ω∈ΩX(ω)∈B}, namely the preimage
X −1[B].(3.1)is written as(X, P(X))or justP(X)for short.
It is equivalent to say that the distribution ofXisP, orXobeys the
distributionP, denoted asX∼P.
Remark 3.1.The model(3.1)is named the pushback ofXin measure theory
[19].
4 Statistics
Statistics is the foundation of Statistical Learning/Machine Learning, whose
research object is the statistical models.
3

4.1 Statistical Models
Definition 4.1(Statistical Model (non-parameterized)).A statistical model is
a family/set of probability models with the common ambient space denoted by
(Ω,A,{P λ}). Of interest is the special case(X,{P λ(X)})that is a statistical
model generated by the target rvXwhose common ambient space is the sample
space ofX.
It is equivalent to write thatX∼P λ whereP λ is unkown.
It is possible to parameterize a family/set{a λ}indexed byλthrough a
mappingθ7→a θ, θ∈Θ, say thata θ is the parameterized form of{a λ}. Strictly
speaking, the parameter space Θ is a subset of Eulidean spaceR n [18], but we
will remove the restriction. Now we introduce the parameterized form of the
statistical models in Definition 4.1
Definition 4.2(Statistical Model (parameterized)).A parametric statistical
model is the parameterized form of a statistical model (in Definition 4.1), de-
noted as(X, P(X|θ), θ∈Θ)whereΘis the parameter space, andP(X|θ)is
a mapping onΘstrictly. If there is no ambiguity, we denote it by the para
distributionP(X|θ)without any explanation of parameter space.
Although the parameterized form is used in machine learning more fre-
quently, in theoretical analysis, nonparameteric statistical model. is commonly
used in the paper. We useP(X) to refer to a general statistical model whereP
is unknown self-declaratively.
Remark 4.1.Since we did not give any restriction for parameter space, thus
there is no essential difference between parameterized form and non-parameterized
form of the statisical model, in this paper.
[15] provides a more strict definition of statistical models. The different is
not essential. Even after this paper concludes, it won’t be too late to replace
the definition in this article with it.
4.2 Sample
Asampleis a tuple/set/family of rvs,{X 1,· · ·, XN }, drawn from a certain
population. If the sample is independent, meaning the rvs in sample are in-
dependent, then the joint distributionP(X 1,· · ·, XN ), is determined by the
popluation distribution totally, otherwise we should give out the joint distribu-
tion explicitly whose marginal distribution is the population. In the latter case,
we have consturcted a new statistical model on the sample spaceX N , based on
the original population. To distinguish the sample of the new model from the
modelM, we denote it asM ∗ for brevity.
Astatisticis a function on a sample, denoted byT(X) whereXreprestents
a sample.
Remark 4.2.(The realization of ) a sample is commonly referred to as “data”
in the context of machine learning.
4

4.3 Bayesian Models
Bayesian methods are a class of statistical techniques and principles used for
probabilistic reasoning and statistical inference. The core idea of Bayesian meth-
ods is to update our beliefs about a particular parameter represented by a dis-
tribution based on the observants. Baysian Model is the statistical model using
the method.
Definition 4.3(Baysian Model).The Baysian model is a statistical model with
priori distribution of parameters, as(M θ, p(θ)), whereMθ is a given statistical
model with parameter distributionp(x|θ). Thus a Bayesian model is identified
with a probability modelp(x, θ).
A common statistical model is a special Bayesian model with thatθobayes
so-called flatten distribution. Thus any statistical model is indeed a probality
model with joint disributionp(x, θ), where we have no sample forθ.
It will be more flexible to introduce a unknown super-parameterαfor the
priori distribution.p(θ|α).
Definition 4.4(Baysian Hierachical Model).The Baysian empirical model
is a Bayesian model with unknown priori, denoted as(M θ, p(θ|α))whereαis
unknown. If the super-parameterαhas its own distributionp(α)(named the
super priori), then we have the Baysian hierachical model(M θ, p(θ|α), p(α)).
4.4 Stochastic process
As mentioned above, when samples are not independent, we use the joint distri-
bution of sample to characterize the model. It is fundamentally different from
the model of population distribution. In another word, the sample forms a
stochastic process.
Roughly, a stochastic process is a sequence{X t}of rvsX t, t∈ T, where the
time setT= [0,∞) or{1,· · ·, T}normally. The process is charactorized by
the following family of distributions,
P(X k1 ,· · ·, XkT ), k1,· · ·, kT ∈ T(4.2)
If the time setT={1,· · ·, T}, the sequence{X t}is also named the time
series. We take theMarkov chainas a typical example. Its joint distribution is
formulated as,
P(X 1,· · ·, XT ) =P(X 1)
T−1Y
t=1
P(X t+1|Xt) (4.3)
4.5 Categories of statistical models
As is well-known, the collection of measure spaces forms a category (denoted as
Meas[19]), as do the categories of probability models and statistical models.
The following categories can be expressed based on the definitions above without
any explanation where the arrows will not be shown as mentioned.
5

•Prob: the category of all probability models, as the sub-category ofMeas;
•Prob X : the sub-category ofProbderived by the target rvX;
•Prob Y|x : the sub-category ofProbderived by the target rvY, with con-
ditional distributionP(Y|x) wherexis fixed, named the conditional vari-
able;
•Stat: the category of The statistical models;
•Stat X : the sub-category ofStatof the target rvX, where an object is
also represented byP(X) (Pis unknown)
•Stat Y|x : the sub-category ofStatof the target rvYwith respect to the
conditional variablex;
•Bayes: the category of the Baysian models;
•P ∗: the stochastic process or the sample distribution with marginal dis-
tributionP;
Remark 4.3.Here the sample distribution refers to the joint distribution of
the sample, instead of the empirical distribution.
F act 4.1.Stat≃ Prob, in some sense.
Proof.Statcould be regarded as a sub-category ofBayeswith the flatten priori.
Obversely the Bayesian model is determined by the joint distribution.P(x, θ).
As a result, we have that the two categroies,StatandProb, are identified with
each other in some sense.
Remark 4.4.The conditional distributionP(Y|x)with a givenxis also a
distribution. There is no different betweenProb Y|x andProb X as categories.
4.6 Estimator
The main task of the statistcs is the estimation, in parameterized form or non-
parameterized form. Formally, An estimation of a statistical modelP(X|θ) is
represented as mapping ˆθ:X N →Θ.
Definition 4.5(Estimator).An estimator is a statistic to estimate the param-
eter of the modelP(X|θ), denoted as ˆθ(X). A model with estimator is denoted
as(M θ, ˆθ(S))whereSis a sample with sizeN.
The best known estimator is themaximal likelihood estimator (MLE), which
has been used to construct the most algorithms in machine learning.
Definition 4.6(MLE).Given a statistical modelP(X|θ). The solution of the
following optimization problem is called MLE of the parameterθ:
max
θ
l(θ) :=
X
i
lnp(x i|θ) (4.4)
6

or in nonparameterized form,
max
p
l(p) :=
X
i
lnp(x i) (4.5)
where{x i}is the independent sample.
In most cases, we use MLE, so the estimator has been implied by a model.
Meanwhile, the word “estimator” and “model” are treated as the synonyms.
Definition 4.7(Maximum a posteriori estimation).The solution of the follow-
ing optimization problem is called maximum a posteriori estimation (MAPE) of
θ.
max
θ
l(θ) :=
X
i
lnp(x i|θ) +Nlnp(θ) (4.6)
where{x i}is the independent sample with the sizeN.
We can redefine the category of statistical models as a tuple of a distribution
familyP(X|θ) and a sample{x i}, that makes it different from the category of
probability models.
5 Statistical Learning
Machine learning models are divided to two main subclasses: supervised (learn-
ing) models and unsupervised (learning) models. We accept this important
partition in the field of statistical learning.
5.1 supervised learning model
In the classical realm of machine learning, A model generally represents the re-
lation of its input variablextaking values in the spaceX, and its corresponding
output variableYtaking values in the spaceY. Formally we give the following
rough definition of machine learning models.
Definition 5.1.A machine learning model is determined by a mappingf:X →
Y, could be written asy∼f(x)simply, without an exponential distribution of
xandy.
People expect that the instances (xi, yi) chould satisfy the equationsf(x i) =
yi, i= 1· · ·, N, that derives the following optimization problem:
min
f
X
i
l(yi, f(xi)) (5.7)
wherelis a loss function defined onY × Y.
In statistical learning, the supervised learning model is described by a dis-
tribution, and has two basic forms: the determinant form and the generative
form.
The determinant models are the probabilitic form of the machine learning
models.
7

Definition 5.2(Supervised learning model (determinant form)).A super-
vised learning model with the input variablexand the output variableyis
exactly depicted by the unknown conditional distributionP(y|x), and denoted
as(X,Y, P(y|x)). It is called the determinant model. It could be seen as a
family ofStat y|x objects indexed by the observations ofx.
Remark 5.1.The formal names ofXandYare the independent variable/en-
dogenous variable/explanatory variable/regression factor/predictor), and depen-
dent variable/exogenous variable/explained variable/regression object/predictor,
respectively. But we tend to prefer using the colloquial expression, “input vari-
able” and “output variable”.
F act 5.1.A determinant model based on the sample{(x i, yi)}, is totally iden-
tified with a statistical model:
(Y N , P(Y|X) = Y
i
P(y i|xi)) (5.8)
where the sampleX={x i}is fixed, named the design variable (design matrix
, if it forms a matrix) andY={y i}is aY N -valued sample point of the model
(5.8).
We shall maximize the conditional liklihood max p l(p) = lnp(y i|xi), named
theconditional maximial likelihood estimation (CMLE)that is not fundamen-
tally different from MLE.
Fact 5.1 is the reason why the author claims that the statistical learning
(model) is identified with the conditionalized statistics (model).
The definition of generative form is more simple in the abstract view.su-
pervised learning model (generative form)The generative model is denoted as
(X,Y, P(x, y)) that is not different from the statistical model (X × Y, P(x, y)).
supervised learning model (Bayesian form)The Bayesian form of supervied
learning model is a special but common case of generateive model, denoted as
(X,Y, P(x|y), P(y)) whereP(x|y) andP(y) is the generative distribution and
priori distribution of the model respectively. Here the key point is that the two
distribution are designed seperatively.
5.2 Unsupervised learning models
Definition 5.3.In general, unsupervised learning models only have genera-
tive form:(X,Z, P(x, z))wherezis unobservable, that is, no sample ofzis
observed.
From the view of population, the unsupervised learning model is not dis-
tingusied with the generative supervised learning model, and from the view
of sample, it is the same with the statistical model (X, P(x)), whereP(x)
is the marginal distribution ofP(x, z), but it always has the prediction task
withP(z|x). The MLE ofP(X) is themaximal marginal likelihood estima-
tion (MMLE)of the unsupervised learning model. As you see, the determinant
model could not be solved by MMLE.
8

An unobservale rv is also called thelatent variable. A model with latent
variables is called thelatent variable model. Hence the unsupervised learning
models are the latent variable models.
5.3 Bayesian statistical learning models
Applying the Bayesian method into statistical learning, we get the Bayesian
statistical learning models (also called Bayesian models). LetM θ is the unsu-
pervised learning model with the distributionP(x, z|θ), then the corresponding
Bayesian model is the tuple (M θ, P(θ)). As we know, It is characterized by the
joint distributionP(x, z, θ).
Like Fact 4.1, we have the following fact.
F act 5.2.The statistical learning models, statistical models and probability mod-
els are equivalent to each other in some sense.
We consider any statistical learning model as a Bayesian model:P(x, z, θ)
where the latent variableZand the parameterθare both unobservable variables,
could be integrated to one variable. It is conluded that, any statistical learning
model has the following form,
P(x, z) (5.9)
wherezis unobservable.
Now, we have eliminated the boundaries of hidden variables and parameters.
It implies that we can estimate the parameterθand predict the latent variable
Zsimultaneously, by solving the following optimization problem,
max
θ,{zi}
X
i
lnp(x i, zi, θ) (5.10)
named themode maximal likelihood estimation (MoMLE), instead of the noto-
rious EM algorithm, whereXis the sample. In fact, that is what the classical
matrix factorization algorithms do, such as PCA and MNF. Moreover, MoMLE
could solve the determinant unsupervised learning modelsP(z|x), by
max
θ,{zi}
X
i
lnp(z i|xi, θ)
5.4 Learner
A learner is defined as an estimator for a statistical learning model:
(Mθ, ˆθ(D))
whereM θ is a statistical model,Dis the sample. By the same reason about the
estimator, the learner is also the synonym of the ambient statistical model.
It is useful to write the the learner explicitly in some cases. For instance, One
can define a latent variable model as a learner (P(x, z), ˆθ(X)) for unsupervised
learning; (P(X, Y), ˆθ(X, Y)) for supervised learning.
9

5.5 predictor and generator
In real-world situations, people are most concerned with the task of predicting
the outputy, given the inputx. A predictor is used to do such task, namely
computing arg maxy P(y|x) orE(y|x).
A generator of statistical learning model is simulation of the distribution
P(x, y) fundamentally.
A full structure of statistical learning model is considered to include the
predictor, even the generator. As most cases, models already contain them in
an implicit manner.
5.6 Classic Models in Statistical Learning
Following lists the classical models in statistical learning, supplemented by com-
mon examples. Each of them form a category that will not be explained in
details.
•Supervised Model:
–Regression:P(y|x), linear regression, ridge/LASSO regression
–Classification:
∗Discriminative form:P(y|x), logistic regression
∗Generative form:P(x, y), LDA/QDA/Naive Bayesian classifier
•Unsupervised Model/Latent Variable Models:
–Clustering:P(x, z), whereZis unobservable (hereafter), K-means/GMM
–Dimension reduction:P(x, z), such as PCA/ICA/MNF/(p)LSA
–Time Series models:P(X 1:T , Z1:T ) where (Xt, Zt)∼PorP(X ∗, Z∗)
for arbitray length, such as HMM.
•Semi-supervied Model:P(X (0), Z)P(X(1), Y) (also as a latent variable
model)
There must be series models under supervised settings, and Naive Bayesian
classifiers also have unsupervised versions. However, such models are not as
widely recognized or renowned in the study of machine learning.
5.7 The beginners’ Cube
Let us incorporate the classical models as categories within the diagram in
Figure 1, which I propose to name “the beginners’ cube”. This nomenclature
is chosen due to its resemblance to a cube and the importance of beginners
initially familiarizing themselves with the models contained in it.
The vertices in the diagram are categories of the models, but labeled by the
generic form of their constituent objects. The arrows symbolize functors con-
necting any two given categories, with parallel arrows considered as equivalents.
10

Figure 1: The beginner’s cube
Consequently, we assign specific names to the arrows fromP(X) toP(Y|X)
orP(X, Y),P(x, z) andP(X ∗) respectively:
(1) Conditionalizing (w.r.t.x), denoted by C x;
(2) Adding hidden/latent variablez, denoted by L V z;
(3) Serialization, denoted byS, or TS z to emphasize that only thez t form a
Markov chain;
Hence we haveP(x, z) =L z(P(x)) for general latent variable models. Spe-
cially, if the hidden variable takes finite values in the latent varable model
P(x, z), then we replaceL z withM ix, say, mixing distributions to construct a
mixed model.
We have following simple facts:
(1)GM M=M ix(N(µ,Σ))
(2)HM M= TS zP(x, z) = TSzL Vz(x, z) and Gaussian-HM M= TSzGM M.
Remark 5.2.To enhance readability and reduce redundancy, we routinely omit
subscripts in the constructors when there is no possibility of confusion.
5.8 Probabilitic Graphic Models
Another way to describe the statistical (learning) model is theprobabilitic graphic
models (PGMs). There are two types of PGMs: theBayesian networkand the
Markov network(also named the random field).
11

We will not recall the whole theory of PGMs here. instead we give an exam-
ple of Bayesian network for HMM with joint distribution:p(z1) Q t p(xt|zt) Q t p(xt+1|zt).
Figure 2: HMM Diagram
F act 5.3.Statis a sub-category of the graph category.
6 Methods
In this section, we shall exibit the general methods to enhance the basic models.
They are treated as the functors/constructors of the categoryStat.
6.1 Traditional methods
Definition 6.1(Variational model).A variational distributionQis always an
apprximation of a given distributionP. A variational model of the unsuper-
vised modelP(x, z), is represented by a tuple of the model distributionP(x, z)
and the variational distributionQ(z|x)of the conditional distributionP(z|x),
(P(x, z), Q(z|x)). As well known, the estimator of the model is the maximal of
the variational lower boundness,
F(p, q;{xi}) :=
X
i
F(p, q;xi)
=
X
i
Z
z
q(z|x i) ln p(xi, z) q(z|x i) dz(6.11)
Remark 6.1.An autoencoder is a tuple of an encoderϕ:X → Zand a decoder
ψ:Z → X, learning from the data whereXandZare the sample space and
the encoding/latent space respectively. When the an encoder and the decoder are
stochastic, represented by the conditional distributionsP(z|x)andP(x|z)of the
latent variable modelP(x, z), it is called the probabilistic/stochastic autoencoder.
Now if the encoderP(z|x)is replaced with the variational distributionQ(z|x),
then it is named the variational autoencoder (V AE)[11].
Following are the traditional methods, as the constructors, mapping the
modelP(X, Y) orP(x, z) to
Of course, adding conditional variational and Bayes method (adding priori)
is one of such methods, have been introduced above.
12

Table 1: Summary of the methods and their descriptions. “-” means that the
author has not designed the symbol.
T echnique Symbol of Constructor Description
Kernel trick K P(ϕ(X), Y)
Localization (refer to§8.3) Loc K(x ∗, X) lnP(X) wherex ∗ is the target
point
Hierarchical model H P(x, z1,· · ·, zn, Y) whereX→z 1 →
· · · →zn →Y, forms Markov chain usu-
ally andz 1,· · ·, zn are hidden
Variational trick V (P(x, z), Q(z|x)) whereQ(z|x) is the
variational distribution
Time Series TS z(n), wherez(0) =X, z(T)∼N(0,1)
6.2 Neural models
The neural models are defined as the models equipped with artificial neural
networks. Usually, they are obtained through replacing the linear structures by
the neural networks.
A neural method provides an implementation of a conditional distribtion,
instead of changing the basic structure of the model. Denote NN(M) for any
possible application of neural networks to modelM. The following arrow is
used to describe how the neural networks are assembled into a statistical model:
NN :P(y|x)→Y=f(X) (6.12)
wherefrepresents any neural network, andP(y|x) is any conditional distribu-
tion of two rvs in a model.
•Feedforward Neural Models: the hierachical structure of linear neural net-
work layers
•RNN/LSTM: as a conditional HMM implemented by the neural network,
that could be denoted as NN(C(HM M))
•Neural Autoencoder: NLPCA [12], integrating neural network into the
autoencoder
•Probabilistic/Stochastic Neural Autoencoder: Kingma-Welling’s Varia-
tional Autoencoder[11]
•Stochastic neural network(SNN): neural network with Dropout(the stochas-
tic perturbation affacts the weights of the layers, or the outputs of the
layers)
•Hierarchical V AE: Diffusion Model/Consistency Model
Normalization Flow is a method to simulate a distribution directly, by the
following fact.
13

F act 6.1.For any distributionP, we can find a functionf, that satisfies
x∼P⇐ ⇒f(z), z∼Q(6.13)
whereQis an easy-to-sample-from distribution such as standard Gaussian dis-
tribution, uniform distribution.
In practice, we always letfbe a neural network.
7 To create advanced models
The main role of the category-theoretical tool is to create or describe statistical
learning models by applying functors. We give some examples as follows.
7.1 Take V AE as an example
The V AE proposed by [11] is a special model of stochastic autoencoder imple-
mented by neural networks.
Following is the path to produce a general V AE.
P(x)→P(x, z)
→(P(x, z), Q(z|x=x)∼N(g(x), h(x)))
→(P(x, z), Q(z|x=x) =g(x) +ξh(x)), ξ∼N(0,1) (7.14)
Write it in the style of the composition of functors (informally)
V AE(f, g, h) = Rep◦V◦L V(P(X)) (7.15)
regarding functionsf, g, has parameters.
A V AE could be implemented by the following SNN (with a regularizing
term):
y∼f(g(x) +h(x)ξ) (7.16)
trained through self-supervised manner with data{(x i, xi)}, wheref, g, hare
all neural networks,ξ∼N(0,1) is the perturbation variable of the hidden layer
g(x).
The network structure for V AE can be referred to as astochastic neural
networkdue to its hidden layer containing stochastic perturbations. This implies
an interesting fact: stochastic perturbations in the hidden layer of a neural
network can result in better learning outcomes.
7.2 Take RNN as an example
Essentially, an RNN is a special type of conditional HMM, which is constructed
as,
P(y)→ · · · →P(y∗, z∗|x∗)
14

Then it will be implimented by the neural networks:
→y t ∼N et(xt, zt−1), zt ∼N et(xt, zt−1), t= 1,2,· · ·
Finally, an RNN could be formulated as,
RN N= NN◦TS z ◦C◦L V(P) (7.17)
In the same manner, it is easy to create time series version of V AE, that is
TSz(V(Cx(P))).
RNNs struggle with long-term dependencies due to the vanishing gradient
problem, where gradients become smaller and smaller as they propagate through
the network. LSTM addresses this issue by adding memory cells to the RNN
architecture. In LSTM there is tow types of hidden variables, but combining
these two variables, we will find it never change the basic structure of RNN.
7.3 To understand the Large Language Models
In this section, we will construct Large Language Models (LLMs) by the category-
theoretic languange.
Recall the brief history of the development of LLMs through the following
three models:
•RNN/LSTM model of languages [1]
•BiRNN/BiLSTM (Bidirection LSTM) / ELMo (Embeddings from Lan-
guage Models)[16]
•BERT[3]
The RNN model for natural language is no different from the ordinary RNN
(see§7.2), except that the input and output are both word embeddings. Now
let us understand the other two structures.
7.3.1 ELMo
ELMo (Embeddings from Language Models) is a deep learning-based language
model that learns contextualized word representations by jointly training a bidi-
rectional language model.
Remark 7.1.Figure 3 is not a typical GPM, only used after the introduction
of BiLSTM.
There is an issue, but not so serious. The objective of ELMo seams not a
true joint distribution. If there is not any common parameter in the two log
likelihoods, then optimize the objective is equivalent to optimize them sepera-
tively. However there are shared parameters in two distributions. So it is not
a joint distribution any longer, instead it is just a loss function for a statistical
desicion. If it is normalized (becoming a true distribution.), then we speculate
that it will perfume better then the unnormlized one, and call ELMo with such
distribution the normalized ELMo.
15

Figure 3: The structure of ELMo. A more detailed figure can be found in [3]
7.3.2 BER T
Figure 4: The structure of BERT (a whole layer is the local model of Transformer
Definition 8.9)
BERT is just the distribution of the token sequence instead of introducing
Markov structure of the sequence. Since BERT casts off the Markov chain of
the states, it must take the hierachical form, otherwise, it will form a cycle as a
bidirection model, that is illegal in the directed graph model.
In the next section, we will give the way to construct the Transformer.
8 Statisitical Decision
Many machine learning models are not described via an explicit distribution,
such as Kmeans clustering and Definition 5.1. In this case, we construct a model
16

only with a loss function based on the sample or its corresponding optimization
problem. The localization method is subsequently addressed.
8.1 The definition of the statisitical decision
Definition 8.1(Statisitical Decision[18]).Assume thatl(x, θ)is the loss on
the single pointxof parameterθ. The loss/risk of the model is defined as the
expectationEl(X, θ), and replaced by the empirical risk
J(θ) := 1 N X i l(xi, θ) (8.18)
if the real distribution is unknown. The statisitical decision is just the following
optimization problem,
min
θ
J(θ) (8.19)
that is the principle of the empirical risk minimization (ERM).
We usel(x, θ) to denote a statisitical decision.
Obviously, the MLE is a special case of statisitical decision or ERM whose
loss is the negative likelihood. And it is not difficult to define statisitical de-
cision for statistical learning models. For example, the statisitical decision for
regression models could defined as the following optimization problem,
min
θ

J(θ) := 1 N X i l(xi, yi, θ) 	 (8.20)
where{(x i, yi)}is the sample. (8.20) can be created by applying the condition-
alizing constructor C to the statisitical decisionl, deonted as C(l).
Another example is that the statisitical decision for latent variable model
could defined as the following optimization problem, as a generalization of
MoMLE,
min
θ,{zi}

J(θ,{z i}) := 1 N X i l(xi, zi, θ) 	 (8.21)
where{x i}is the sample andz i is unobservable. (8.21) can be constructed as
L Vz(l).
8.2 Decision Tree
People think that decision trees are not common statistical learning models.
However, after carefully examining decision tree algorithms such as ID3, a de-
cision tree is a recursive decision based on the following parametric model,
P(y|x, j) =P(y|x j), j= 1,· · ·, p(8.22)
whereX j is thej-th component ofX. As known, the MLE of (8.22) is equivalent
to the principle of maximum information gain, which determines the splitting
17

rule of the tree. We create a construtor Tr(J) to depict a decision tree based on
any statisitical decisionJ(θ) including the MLE like (8.22). For example, the
linear tree [4] is represented by Tr(P(y|x)) whereP(y|x) is a linear classifier.
We denote the decision tree as Tr(M), whereMis a model to determine the
splitting rules.
8.3 Local statistical decision
It is more natural to describe the localizaiton method from the view of statistical
decision.
Definition 8.2(Local statistical decision/Local model).Given a loss function
land a kernelK(x, y), we say the following optimization problem is a local
statistical decision at the target pointx ∗,
min
θ
1
N
X
i
K(x ∗, xi)l(xi, θ) (8.23)
wherel(x, θ)is a loss at the single pointx,{x i}is the sample. We would like
to say that(8.23)is built through appling the localization trick to thel.
the kernelKin local model is more free then that in the kernel method. In
most cases, it is only expected to be non-negative.
since it is not required to be symmetric, A kernelK(x, x′) can be represented
by two different feature mappingsϕ, ψ:X →HwhereHis a Hilbert space,
namely
K(x, x′) =⟨ϕ(x), ψ(x′)⟩
WhenHis a low dimensional Euclidean space, the feature mappings are also
called the embedding or the distributional/real representation. More generally,
we define
K(x, x′) =F(ϕ(x), ψ(x′))
such asK(x, x′) =e ⟨ϕ(x),ψ(x′)⟩.
The solution of (8.23) is related tox ∗, thus denoted as ˆθ(x∗).
The total loss on the sample is
J(K) =
X
i
l(xi, ˆθ(xi;K)) (8.24)
where the expressionsJ(K) and ˆθ(xi;K) stress that the loss is also related to
the kernelK.
Following definition reflects the original idea of localization.
Definition 8.3(Local model for machine learning).Given a machine learing
modely∼f(x, θ), we define its localized model as
min
θ
1
N
X
i
K(x ∗, xi)|yi −f(x i, θ)|2 (8.25)
18

or for some purposes,
min
θ
1
N
X
i
K(x ∗, y0, xi, yi)|yi −f(x i, θ)|2 (8.26)
Finnally, we introduceLoc(M) (orLoc(l)) to describe a local model whose
fundamental model isMor (determined by a loss functionl).
8.4 Local average
The terminal goal of the regression is to calculate the conditional expection,
E(y|x)≈
X
xi∈Ux
yi (8.27)
whereU x is a certain neighorhood ofx.
On the basis of (8.27), we give the following concept.
Definition 8.4(Local average/Local regression).A local average of the sample
{(xi, yi)}on target varx ∗, is defined as,
ˆy(x∗) :=
X
i
K(x ∗, xi)yi/
X
i
K(x ∗, xi) (8.28)
where the sample spaceYofyis assumed to be the real numbersRor the
Euclidean spaceR p.
F act 8.1.Any local regression is reduced to the local average, approximately.
Especially, we have the local average of the sample{(x i, xi)}, also named
the self local average of{x i}.
Definition 8.5.The (self ) local average mapping/transform (or mean shifting)
is defined as,
m(x∗) :=
X
i
K(x ∗, xi)xi/
X
i
K(x ∗, xi) :X → X.(8.29)
Mapping on the sampleX={x i}, we have
m(xi) :=
X
j
K(x i, xj)xj/
X
j
K(x i, xj) :X N → XN (8.30)
i.e.m(X) = ˜KX(8.31)
where ˜Kis the is the normlization of the kernel matrixK(X, X).
We can call (8.29) “the self-local average”, partly in the reason that it has
the same form with “the query-key-value model” of the self-attention [20].
Remark 8.1.The famous MeanShift algorithm [2] is the iteration of the map-
pingm.
19

Remark 8.2.The local linear embedding (LLE)[17] is indeed a self-local average
with learnable kernelK.
For classification, we have the following analogy.
Definition 8.6(Local mode/Local classification).A local mode of the sample
{(xi, yi)}on target varx ∗, is defined as,
ˆy(x∗) := arg max k
X
yi=k
K(x ∗, xi) (8.32)
where the sample spaceYofyis a finite set, taking the valuesk= 1,· · ·, K.
A classisification model can be transformed to a regression model, by em-
bedding the discrete spaceYinto a continuous space, as in word embedding.
8.5 Local latent variable model
It is possible to apply the localization trick into the latent variable models. As
we all know, the common method to solve the latent variable model is based
on the variational lower bound, instead of the likelihood function, as the loss
function of the model. Hence it is able to define a “local variational lower
bound”.
Here, we consider the autoencoder as a special latent variable model. We
realize that the autoencoder should also be linear in the local domain, and the
most typical linear latent variable model/autoencoder is PCA. Therefore, we
can directly establish a “local PCA” model, denoted as Loc(P CA).
As we all know, the optimization of the latent variable model is the vari-
ational lower bound, which is to replace the likelihood function with the vari-
ational lower bound as the loss function. We can define the “local variational
lower bound”. Here, we consider the autoencoder as a special latent variable
model. We realize that the autoencoder should also be linear in the local range,
and the most typical linear autoencoder is PCA.
Obviously, the autoencoder can also be constant locally, and defined as the
following optimization problem.
min
z
X
i
K(x ∗, xi)∥xi −z∥ 2 2 (8.33)
It is easy to see that the solution to (8.33) is ˆz(x∗) = P i K(x ∗, xi)xi/ P i K(x ∗, xi),
that is the local average. This implies the following fact.
F act 8.2.The local dimensionality reduction, the local clustering, and the local
average are equivalent concepts in some sense.
8.6 Local statistical decision for autoregression
Now we delve into the local statistical decision for the autoregression or discrete
dynamics (of 1-order), that is represented as follows:
xt+1 ∼f(x t, t), xt ∈ X, t= 1,2,· · ·(8.34)
20

whereXis assumed to be Euclidean spaceR p, otherwise we should embed it
into the real space first. It is indeed a stochatic process, but in a supervised
learning form (Definition 5.1).
According to the Definition 8.2 or Definition 8.3, the local model of (8.34)
could be expressed as the following local average,
ˆxt+1 :=
X
s
K(x t, t, xs, s)xs+1/
X
s
K(x t, t, xs, s) (8.35)
treating the tuple (x t, t) as the input andx t+1 as the outputs. (8.35) could
be written as Loc(x t+1 ∼f(x t, t)) roughly. Let us rewrite it in the following
definition.
Definition 8.7(Local autoregression/Dynamical system/Local time-series).
The local model of(8.34)is called the local autoregression/time-series, expressed
as
ˆxt =m(x t, t) :=
X
s
K(x t, t, xs, s)xs/
X
s
K(x t, t, xs, s) (8.36)
where the timetcould theoretically take any type of values, andx t is the series
on it. We prefer using the sequential form:{ˆx t}=m({x t})that is a mapping
from the sequential spaceX ∗ to itself.
F act 8.3.The local average(8.36)can approximate any autoregression model
or discrete dynamics (of any order). In fact, it is the result of the construction
of local HMM, write,Loc(HM M).
It follows from (8.26) that the local autoregression is a local regression of
T → X, write, Loc(xt =f(t)). We conclude that,
F act 8.4.All local models are equivalent in some sence, and they are all local
average.
When the kernel is unrelated to the positions, i.e.,Kis designed asK(x t, xs),
it is reduced to ordinary self-local average[13]. Otherwise, (8.36) could be termed
as “serialized self-local average”, providing a strict mathematical interpretation
for self-attention.
A simple design ofKisK 1(xt, xs)K2(t, s) orK1(xt, xs)K2(t−s), whereK 1
represent the graphic-dependence of elements inXstatically andK 2 represents
the “position-encoding”. It is essentially the weighted moving average.
Hence, what the localization really dose is to transform the time-dependency
to graphic-dependency that is no limited on long-dependency theoretically.
Definition 8.8(self attention with absolute positional embedding[20]).The
self attention is a local dynamical system with kernelK(x t +p(t), xs +p(s))
wherep(t)is the position-encoding oft.
Strictly, the local dynamical system should learnKto implement the self-
attention, that is to solve the following optimization problem:
min
K
J(K) :=∥X− ˜KX∥ 2 F (8.37)
whereX={x (j) t }tj and ˜Kis the normlization ofK={K(x t, t, xs, s)}st.
21

8.7 Local-local model
A local model is determined by a local lossJ(x ∗, θ;K). It is also a loss function
at a single sample point. Based on this, we can further construct a local loss as
follows:
J ′(x∗, θ;K, K′) = X
k
K ′(x∗, xk)J(x k, θ;K)
=
X
kj
K ′(x∗, xk)K(x k, xj)l(xj, θ) (8.38)
In matrix form, it can be expressed asJ ′(X, θ) =K′(X, X)K(X, X)l(X, θ).
We refer to (8.38) as the “local-local loss”, and the corresponding decision
model as the “local-local model”.
(8.38) is equivalent to the local loss of the (composite) kernel (x, y)7→P
k K ′(x, xk)K(x k, y). Therefore, the local-local model is still a local model.
Similarly, the local-local average can be constructed, that is the local average
of the composition of normalized kernels:
ˆxi =
X
kj
˜K ′ ik ˜Kkj xj,i.e. ˆX= ˜K ′KX(8.39)
To prevent a hierarchical local model from deteriorating into an ordinary
local model, we insert a nonlinear function between two kernels, mimicking the
feedforward neural network:
ˆxi =
X
k
˜K ′ ikf( X
j
˜Kkj xj), f:R p →R p,i.e. ˆX= ˜K ′f(KX) (8.40)
where ˜K ′ is the normalization ofK(X ′, X′),X ′ =f( ˜KX). It is more reasonable
to rewrite (8.40) as
ˆX=m K′(f(m K(X))) (8.41)
by the local average mapping.
Based on (8.40), we can further construct “local-local-local models” and so
on. We collectively refer to these models as “hierarchical local models”. We coin
a symbol LocL, for such construction, whereLis the number of the kernels, and
Loc1 = Loc. In fact, Transformer, the most popular large model structure, is a
such hierarchical local model.
Definition 8.9(Transformer).The encoder part of the Transformer can be
represented as the following sequence mapping:
ˆX=m KL (fL−1(· · ·(f1(mK1 (X))))) (8.42)
wherem Kl is the (sequential) local average of kernelK l, andf l represents a
feed-forward neural network.
22

[20] suggestsL= 6, thus Transformer = Loc 6(yt ∼f(x t, t)). (Here, we have
not yet introduced the multi-head structure.)
Definition 8.9 only provides the structure of the Transformer encoder, and
according to the suggestion in (8.35), the decoder part is redundant.
Remark 8.3.Note that, in Definition 8.9, the Transformer is defined to be one
layer of transformer blocks in the architecture of BERT (Figure 4), instead of a
single transformer block.
8.8 Tied models
Inspired by ELMo as a BiLSTM, we propose a new model or constructor, called
tied model, denoted as the following pair,
Tie(P(X|θ 1, θ0), P(X|θ2, θ0)) (8.43)
whereθ 0 is the common parameter andθ i, i= 1,2 are the private parameters.
The estimation of parameter is to maximize “the tied log-likelihood”,
αlnP(X|θ 1, θ0) + (1−α) lnP(X|θ 2, θ0) (8.44)
where 0≤α≤1 is a constant.
As mentioned above, (8.44) is not a real likelihood, but a special loss func-
tion. The tied model is judged to be a product of experts [7] but unnormalized
and could be regarded as a statistical decision.
8.9 Markov decesion process
TheMarkov decesion process (MDP)is a subcategory of time seriesP ∗({xt}).
As a decistion model, it has the loss function in the following form,
l(θ;x 1,· · ·, xT ) =
T−1X
t=1
l(θ;x t+1|xt) (8.45)
wherel(θ;x t+1|xt) represents a transition loss in thet-th step.
Reinforcement learning is indeed a special type of Markov decision process,
where the policy governing actions from a given state serves as the parameter,
and the conventional notion of loss is substituted with the concept of reward,
while the true value of rewardl(θ;x t+1|xt) is obtained through the interaction
with environment.
We can create a latent variable model for MDP, as L V {zt}(M DP), and get
the so-called partially observable MDP.
9 Novel paradigms of machine learning
Numerous novel paradigms have been developed in the field of machine learning,
including:
23

•Reinforcement learning
•Ensemble Learning
•Transfer Learning
•Incremental Learning (Continual Learning, On-line Learning)
•Life-Long Learning (as a more general form of incremental learning)
•Meta Learning
•Multi-task Learning
•Dual Learning
We do not plan to discuss the paramdigms here. For the transfer Learning,
several potential statistical definitions include:
•(P(X s|θ1), P(Xt|θ2)), θ1, θ2 ∼P(θ|α)
•(P(X s|θ1, θ0), P(Xt|θ2, θ0))
•(P(ϕ(X s)|θ), P(ϕ(Xt)|θ)) whereϕis learnable for makingϕ(X s) and
ϕ(X t) have the same distribution.
Here,X s represents the source domain, andX t represents the target domain.
10 Future Works
This paper’s fundamental objective is to employ category theory as a unified lan-
guage to describe statistical learning models, and even to construct novel models
using this framework. Currently, the number of statistical learning models de-
scribed in this way is limited, but the author believes that other models newly
developed, especially the LLMs, can also be described similarly. If successful,
future efforts will be directed towards establishing a more systematic category-
theoretical framework for statistical learning as well as the novel paradigms of
machine learning listed in section 9. Guided by category theory, we will further
invent new models.
It is worth mentioning that we have strictly defined the local decision-making
model, also regarded as a constructor, and based on this, we have constructed
the Transformer.
The facts stated in thet paper are not strict, as informal theorems, with the
phrase “in some sense”.
24

References
[1] Yonatan Belinkov, Nadir Durrani, Fahim Dalvi, Hassan Sajjad, and
James R. Glass. What do neural machine translation models learn about
morphology? InAnnual Meeting of the Association for Computational
Linguistics, 2017.
[2] Dorin Comaniciu and Peter Meer. Mean shift: A robust approach toward
feature space analysis.IEEE Transactions on Pattern Analysis and Ma-
chine Intelligence, 24(5):603–619, 2002.
[3] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert:
Pre-training of deep bidirectional transformers for language understanding.
InNorth American Chapter of the Association for Computational Linguis-
tics, 2019.
[4] Jo˜ ao Gama and Pavel Brazdil. Linear tree.Intelligent Data Analysis,
3(1):1–22, 1999.
[5] Ian Goodfellow, Yoshua Bengio, and Aaron Courville.Deep Learning. The
MIT Press, 2016.
[6] T. Hastie, R. Tibshirani, and J.H. Friedman.The Elements of Statisti-
cal Learning: Data Mining, Inference, and Prediction. Springer series in
statistics. Springer, 2009.
[7] Geoffrey E. Hinton. Training products of experts by minimizing contrastive
divergence.Neural Computation, 14:1771–1800, 2002.
[8] J¨ urgen Jost, Hˆ ong Vˆ an Lˆ e, Duc Hoang Luu, and Tat Dat Tran. Proba-
bilistic mappings and bayesian nonparametrics.arXiv: Statistics Theory,
2019.
[9] Davar Khoshnevisan.Probability, volume 80. American Mathematical Soc.,
2007.
[10] Kiessler and C Peter. Measure theory and probability theory.Publications
of the American Statistical Association, 102(479):1078–1078, 1998.
[11] Diederik P. Kingma and Max Welling. Auto-encoding variational bayes.
CoRR, abs/1312.6114, 2013.
[12] M. A. Kramer. Nonlinear principal component analysis using autoassocia-
tive neural networks.AIChE Journal, 37(2), 1991.
[13] Joon Lee, Yun Lee, Jinwoo Kim, Alexander R Kosiorek, Sunmin Choi,
and Yee Wei Teh. Set transformer: A framework for attention-based
permutation-invariant neural networks. 97:3744–3753, 2019.
[14] Saunders Maclane. Categories for the working mathematician. 1978.
25

[15] Peter McCullagh. What is a statistical model?The Annals of Statistics,
30(5):1225–1310, 2002.
[16] Matthew E. Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christo-
pher Clark, Kenton Lee, and Luke Zettlemoyer. Deep contextualized word
representations.ArXiv, abs/1802.05365, 2018.
[17] S. T. Roweis and L. K. Saul. Locally linear embedding.Science 290,
9:2323–2326, 2000.
[18] J. Shao.Mathematical Statistics. Springer Verlag, second edition, 2007.
[19] Dan Shiebler. Categorical Stochastic Processes and Likelihood.Composi-
tionality, 3, April 2021.
[20] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones,
Aidan N Gomez,  L ukasz Kaiser, and Illia Polosukhin. Attention is all you
need. In I. Guyon, U. Von Luxburg, S. Bengio, H. Wallach, R. Fergus,
S. Vishwanathan, and R. Garnett, editors,Advances in Neural Information
Processing Systems, volume 30. Curran Associates, Inc., 2017.
26
