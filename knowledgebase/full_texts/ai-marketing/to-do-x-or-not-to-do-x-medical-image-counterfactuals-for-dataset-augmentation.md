---
title: 'To do(x) or not to do(x): Medical Image Counterfactuals for Dataset Augmentation'
url: https://arxiv.org/abs/2609.14124
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Yasin Ibrahim
- Robin J. Evans
- Konstantinos Kamnitsas
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.14124
pages: 10
chars: 60440
fetched_at: '2026-11-08T13:28:15+00:00'
kb_version: 1
---

# To do(x) or not to do(x): Medical Image Counterfactuals for Dataset Augmentation

IEEE TRANSACTIONS AND JOURNALS TEMPLA TE 1
T o do(x) or not to do(x): Medical Image
Counterfactuals for Dataset Augmentation
Y asin Ibrahim, Robin J. Evans, and Konstantinos Kamnitsas
Abstract— Medical image analysis is often hindered by
biased datasets, which can lead to biased models and
limited clinical applicability. A promising strategy for mit-
igating such biases is to augment training data with syn-
thetic images. Counterfactual (CF) generation is one such
strategy, though the term is used in two different senses: in
some works, CFs are produced through causality-based in-
terventions derived from structural causal models, whereas
in others, they are produced by non-causal image edits or
conventional conditional generative models, such as alter-
ing anatomy or adding pathologies. In this work, we study
this distinction and evaluate its practical consequences
for medical image augmentation. We compare three con-
ditioning strategies:Deterministic, which changes selected
variables while holding the remaining variables fixed;Undi-
rected, which updates variables according to learned sta-
tistical associations without assigning causal directions;
andCausal, which propagates interventions along a di-
rected causal graph. We analyse how these choices affect
the resulting images, and explore when causally grounded
methods improve dataset augmentation or bring limited
benefit. In particular, we assess downstream performance
and fairness, where fairness refers to reduced sensitivity
to dataset biases across sensitive subgroups. Our exper-
iments demonstrate that using a causal approach to syn-
thetic training data generation can lead to tangible benefits,
with these insights offering valuable guidance to machine
learning practitioners for the effective design of data gen-
eration protocols.
Index Terms— Causality, Dataset Augmentation
I. INTRODUCTION
Medical image analysis faces the challenge of biased
datasets, which can lead to biased models [1] and hinder the
deployment of such models in real-world clinical scenarios
[2], [3]. One way to address this challenge is to generate
synthetic data to create more balanced training datasets and
counteract undesirable correlations [4]. Indeed, various works
have shown that augmenting training datasets with synthetic
data can improve the performance and subgroup fairness of
downstream models, such as disease predictors for chest x-
ray, skin lesion, and histopathology data [5], breast cancer
MRI [6], and text-prompted generation of skin lesion images
This work was sumbitted on 11 September 2026. Yasin
Ibrahim (yasin.ibrahim@eng.ox.ac.uk) and Konstantinos Kamnitsas
(konstantinos.kamnitsas@eng.ox.ac.uk) are with the Department
of Engineering Science, University of Oxford. Robin J. Evans
(evans@stats.ox.ac.uk) is with the Department of Statistics, University
of Oxford. Yasin Ibrahim is supported by the EPSRC Centre for Doctoral
Training in Health Data Science (EP/S02428X/1).
[7]. Fully synthetic training sets have also been explored,
although these generally do not perform as well as augmenting
real datasets with synthetic samples [8]. However, synthetic
data is not automatically beneficial: if the generation process
reproduces or strengthens biased correlations present in the
training set, downstream models may inherit or amplify these
biases [9]. This concern is supported by theoretical analyses
[10], [11] and empirical evidence [12]. These findings moti-
vate a careful examination of how synthetic medical images
are generated and used for augmentation. In recent years,
there has been growing interest in integrating causality into
machine learning models [13], [14]. Medical imaging is an
application area of particular promise, with several works
arguing that causal reasoning can help address confounding,
dataset shift, and robustness issues in image analysis [15], [16].
This interest has been especially prominent in the generation
of counterfactuals (CFs). In the causal sense, CF generation
involves specifying a causal diagram over relevant variables,
estimating how an intervention on one variable should affect
the others, and then using these inferred variable values to
generate a corresponding image [17], [18]. However, there
remains limited systematic evidence on when such causally
grounded mechanisms provide practical benefits such as bias
mitigation, rather than simpler conditional or deterministic
forms of generation.
Alongside its formal definition in the causality literature, the
term “counterfactual” is also commonly used in medical imag-
ing to describe synthetic modifications to an input image, such
as increasing ventricular size in a brain MRI scan or adding
signs of disease to a chest x-ray [19]. Such modifications
may be produced by direct image processing procedures or by
conventional generative models that edit an image conditioned
on a desired attribute, without explicitly modelling causal re-
lations among the associated variables. Because synthetic data
generation in medicine is sensitive to both clinical validity and
downstream bias, this distinction matters. Therefore, in this
work, we distinguish betweencausal counterfactuals, which
are derived from interventions in a causal model, and broader
image counterfactuals, which modify images without necessar-
ily encoding causal relations. This distinction allows different
methods to be evaluated and compared according to the
assumptions they actually make. To study the consequences of
these assumptions, we compare three conditioning strategies
for generative models. In theDeterministicapproach, given an
input image and associated variables, one or more variables
are set to specified values while all remaining variables are
kept fixed. In theUndirectedapproach, relationships between
arXiv:2609.14124v1  [cs.LG]  12 Sep 2026

2 IEEE TRANSACTIONS AND JOURNALS TEMPLA TE
variables are modelled statistically, so changing one variable
can affect other associated variables, but the directions of these
relationships are not treated as causal. In theCausalapproach,
relationships are represented by a directed causal graph, so
interventions propagate only through the causal directions
encoded in the graph. We first investigate how the output
counterfactuals produced by these methods differ depending
on the assumed graph and the variables altered. We then
explore using data generated by these different methods for
training dataset augmentation and the effects this has on the
accuracy and fairness, with regards to bias mitigation, of a
predictor trained on this. We divide the actual data generation
approach into two methods: counterfactuals of real images
from the training set, and purely synthetic images sampled
from the latent space of the generative model. From this, we
gain insights into when it is beneficial to use an approach that
explicitly considers causal relations. In summary, we make the
following contributions:
•We demarcate a clear distinction between counterfactual
methods that do and do not use causal inference, and pro-
vide a categorisation of dataset augmentation approaches.
•We evaluate the effects of conditioning generative models
with techniques that impose different assumptions about
which relationships between modelled variables should
be preserved after an intervention.
•We identify the conditions under which generating data
using explicitly causal methods for training dataset aug-
mentation can improve downstream performance and
fairness over non-causal alternatives.
II. RELATEDWORK
To mitigate the issue of bias in medical imaging [1]–[3], a
range of strategies has been proposed, including reweighting
or resampling-based objectives [20] and domain adaptation
methods for distribution shift [21]. However, what has been
gaining particular traction is the use of data augmentation
techniques to rebalance datasets and improve the coverage of
underrepresented samples [4], [22]. By synthesising realistic
medical images, researchers can augment datasets with specific
demographic groups, pathologies, acquisition conditions, or
imaging appearances that are underrepresented in the real
data distribution. Such methods are especially relevant when
collecting additional real medical imaging data is expensive
and time-consuming, or when data sharing is constrained by
privacy, regulatory, and governance requirements [23].
Generative modelling techniques have played a central role
in the development of synthetic medical data, with some of
the most promising results have been achieved with Gener-
ative Adversarial Networks (GANs) [24], which have been
used for tasks such as lesion synthesis, MRI reconstruction,
and modality translation [25], [26]. Other deep generative
approaches, including variational models [27], normalising-
flow-based models [28], and autoregressive or discrete-latent
models, have also been explored for medical image synthesis
and representation learning. More recently, diffusion-based
generative models have shown strong performance in produc-
ing high-fidelity medical images while maintaining anatomical
consistency [29]. Synthetic generation has also been used
directly for bias mitigation and fairness-oriented augmentation
[5]. Though these methods are powerful, they often learn
observational correlations from the training data, so when
the training distribution contains confounding or undesirable
correlations, generated samples may preserve or amplify these
patterns unless the generation process is carefully controlled.
Causal reasoning offers one way to make such control
more explicit. In causal medical image modelling, relation-
ships between variables are represented not only as statistical
associations but as directed cause-effect assumptions [15],
[16]. This perspective is particularly relevant for counterfactual
generation; in a causal counterfactual, an intervention such
as changing disease status, age, or acquisition parameters is
propagated through a structural causal model, so only variables
downstream of the intervention should change, while other
variables should remain fixed except through the specified
causal pathways [17], [18]. This differs from conventional
undirected generation, where variables may be associated
but the model does not distinguish whether the association
corresponds to a causal effect, a reverse effect, or a common
cause. Causal counterfactuals therefore provide a principled
framework for specifying which aspects of an image should
and should not change under an intervention.
By contrast, many works in medical imaging use the term
counterfactual more broadly to refer to any synthetic modifi-
cation that changes a visual attribute while preserving sample
identity [19]. Examples include increasing lesion size, intro-
ducing synthetic pathologies, modifying anatomical structures,
or translating an image to a target domain defined by a desired
attribute. These approaches are valuable for data augmentation,
visual explanation, and stress testing, but they often lack
explicit causal grounding: the modification is not necessarily
derived from a model of how the underlying variables are
causally related. This difference is important because non-
causal image edits may produce realistic-looking samples
while still changing variables that should have remained fixed,
or preserving variables that should have changed under a
causal intervention.
In this paper, we categorise methods that synthesise
counterfactual-style medical images into three families.Deter-
ministicmethods set selected variables to desired values and
keep all other conditioning variables fixed. These include many
direct image-editing or image-to-image translation approaches,
such as methods based on CycleGAN [30] or Pix2Pix [31],
when they are used to map an image to a target domain
without modelling how the remaining variables should change.
Undirectedmethods model statistical relationships among
variables and use these associations when generating or editing
images, but do not assign causal directions to those relation-
ships.Causalmethods explicitly encode directed dependencies
between variables, often through Structural Causal Models
or Neural Causal Models [17], [18], so that interventions
propagate through the graph in a way that is consistent with
the assumed causal structure. Our contribution is to compare
these families under a common experimental framework and
evaluate when the stronger assumptions of causal conditioning
translate into measurable benefits for dataset augmentation,

IBRAHIMet al.: TO DO(x) OR NOT TO DO(x) 3
downstream performance, and fairness.
III. BACKGROUND
A Structural Causal Model (SCM) is defined as a tuple [18]:
M=⟨V, U,F, P(U)⟩,
whereV={v 1, . . . , vn}denotes the endogenous variables,
U={u 1, . . . , un}the exogenous noise variables,P(U)their
distribution, andF={f 1, . . . , fn}the structural mechanisms.
Each endogenous variable is determined by its parents pa i and
corresponding noise variableu i:
vi :=f i(pai, ui).(1)
Unlike purely observational models, SCMs also support
interventions through the do-operator [32]. Applying do(v i =
a)fixesv i toaand removes the influence of its parents,
resulting in
P(V|do(v i =a)) =
Y
j̸=i
p(vj|paj)·1 {vi=a}.
To obtain sample-specific counterfactuals rather than
population-level intervention effects, SCMs use the abduction–
action–prediction procedure [14]:
1)Abduction: Infer the sample-specific exogenous noise
throughp(U|V).
2)Action: Apply do(V=A)to obtain the modified model
fMdo(V=A) .
3)Prediction: Use the modified model to estimate the
counterfactual variables.
Various methods have been proposed to apply this to the
problem of generating image counterfactuals; these include
diffusion [33], V AE [17], hierarchical V AE [34] and semi-
supervised [35] approaches. In this paper, we will usexto
denote the image andpato denote the parent variables, such
as age, sex and race for chest x-rays, which “cause” the image
appearance. The counterfactual parents (post-intervention) are
denoted by fpa.
IV. METHODS
A. Model Conditioning
In the medical imaging literature, the term “counterfactual”
is often used to describe any change to an image that maintains
the sample identity, such as the removal or addition of lesions
from a scan, via direct image processing or a (non-causal)
undirected generative model. An alternative interpretation of
“counterfactual,” however, is the causal approach described
in Section III applied to the relevant variables in the model,
such as age, disease, etc. In the context of image modification,
this is typically the initial step before the inferred variable
values are input to a conditional generative model, which
then generates the corresponding altered image. To avoid
further confusion we employ the termsimage counterfactual
andcausal counterfactualto refer to these two concepts
respectively.
We thus seek to identify when the additional cost of generat-
ing causal counterfactuals is beneficial. To investigate this, we
(a) Deterministic
 (b) Undirected
 (c) Causal
Fig. 1: Effect of intervention with each approach; Yellow:
intervened, Green: affected, Red: unaffected.
propose demarcating three distinct methods for conditioning
generative models with multiple variables and relationships
between them. Fig. 1 provides an example of the differences
between them; we have a set of variables(a)−(f)with a
specified causal structure, and intervene on the first of these
viaa= ˜a. The three conditioning approaches are:
1)Deterministic: The relationships between variables are
ignored. We set the desired subset of variables to new
values and force the remainder to retain their original
values. For the example in Fig. 1a, we have:
p(fpa) =1 {a=˜a}·
Y
v̸=a
1{v=v}
This is the most common approach for conditioning
standard (non-causal) generative models.
2)Undirected: Assuming we know which variables are
associated, we impose an undirected graph structure
between them. We set a desired subset of variables to
new values and infer the remainder using the joint distri-
bution. For the example in Fig. 1b, the post-intervention
distribution becomes:
p(fpa) =1 {a=˜a}·p(b, c, d, e, f|a= ˜a)
This is a stronger prior than the previous case, as it
assumes we know which variables are related.
3)Causal: Assuming we know the causal relations between
variables, we impose a directed graph structure so that
child variables are only affected by their parents. We
conduct the abduction-action-prediction procedure (Sec-
tion III) to create CFs. As in Fig. 1c, inference is made
via the model fMdo(a=˜a). This is an even stronger prior,
with assumed known direction of causality, where only
d-connected variables are affected by the intervention.
B. Image Generation
After training, we consider two approaches to generate
synthetic images for dataset augmentation. Alongside the
counterfactual paradigm described above, we also explore gen-
erating new images by sampling directly from the latent space
(i.e. “de novo” sampling, not conditioned on input image).
Such an approach has been shown to improve performance
of downstream classifiers [5]. So far, however, this has been
limited to the case where there are no assumed relationships
between variables –Deterministicin our terminology. To do
this, for each approach, each variable is either assigned a
desired value or sampled from an unconditional distribution.

4 IEEE TRANSACTIONS AND JOURNALS TEMPLA TE
Fig. 2: Model outline. Green: observed, Grey: latent, Red:
predicted, Blue: causal generative, Yellow: decoding. (left)
Training: we use theypredictions for decoding unless they
are observed, (right) CF generation.
To enrich our analysis, we adapt the other two conditioning
approaches to this setting. In both cases, we begin by choosing
a variable and either assign it to a specific value or sample it
from its marginal distribution. We then sequentially sample the
remaining variables conditionally on the previously sampled
ones. In theUndirectedapproach, this means any connection
between variables induces a conditional distribution and only
variables that are entirely disconnected in the proposed graph
are sampled from their marginal distributions. ForCausal, on
the other hand, children variables are conditioned on their
parents but the reverse is not true. As in theDeterministic
case [5], these variables are then all fed to the conditional
decoder of the generative model to produce a new image.
This image generation paradigm is described in Algorithm 1.
Algorithm 1Sampling
Input:Parents (a)
Output:Generated Image (¯x)
1:a∼p(a)▷Sample or set one of the variables
2: Ďpa∼p(pa|a= ˜a)▷Sample the remaining variables
3:z∼p(z)▷Sample a latentzfrom the prior of the
generative model
4:¯x=dec(z, Ďpa)▷Feed sampled vars andzto decoder
5:return¯x
Algorithm 2Counterfactuals
Input:Image (x), Counterfactual parent (˜a)
Output:Counterfactual Image (˜x)
1:z= enc(x)▷Encodexto obtain latent representationz
2: cpa=f(x)▷Predict missing variables from imagex
3: fpa←(a= ˜a)▷Intervene on one of the variables
4: fpa∼ fMdo(a=˜a) ▷Infer the remaining variables
5:˜x=dec(z, fpa)▷Feed altered vars andzto decoder
6:return˜x
C. Architecture
We use the semi-supervised causal generative model pro-
posed by [35] as this allows us to explore the conditioning
approaches in greater depth; we can alter the amount of
available labelled data, e.g. by pretending that a percentage of
values of endogeneous variables are missing, and observe the
Fig. 3: Example coloured MNIST images
effect this has on the outputs of each approach (see Section
VI-C). By adapting the conditioning module, we implement
each of the three approaches outlined in Section IV-A.
Firstly, for theCausalapproach, we use [35] directly. This
involves a hierarchical V AE that encodes the input image to
multiple scales before decoding it at multiple latent levels. A
DAG is also specified and the arrows (relationships between
variables) are learned as normalising flows [28]. In addition,
a variable predictor is trained as an extra head on the encoder,
used to predict any missing values.
For theUndirectedapproach, we keep the DAG but add
functions (again implemented as normalising flows) in the
opposite direction to the existing arrows, to form bi-directed
edges and model undirected relations. For example, for DAG
a) in Fig. 4, we also model the functionp(d|b, f). The model
is trained as the original [35] with the added flows also
learned and used to infer any missing values. To produce
counterfactuals, we set the desired variable values and infer the
remaining using the learned conditional dependencies. Finally,
for theDeterministicapproach, we eschew the causal graph
entirely and use only the encoder from the generative model
to predict missing values. Then, to produce counterfactuals,
we infer the latentzand input the desired variable values as
conditions.
V. ANALYSIS ONMORPHO-MNIST
We now explore the approaches described in Section IV-A
when different causal relationships govern the data generating
process to study when these causal modelling assumptions are
useful. To begin, we use Morpho-MNIST [36], which provides
a framework for generating data with causal relationships
between variables of our own specification, with a known
generative process and distribution, and thus we can evaluate
counterfactuals from learned generative models against the
ground-truth log-likelihoods. This is impossible with real med-
ical data, where the true underlying distribution is unknown.
These experiments therefore provide insights that guide and
complement further exploration on medical data.
We consider five variables to create coloured MNIST images
as per [35] (Fig. 3): digitd, thicknesst, intensityi, foreground
colourfand background colourb. We then consider four
DAGs with different relationships of variables (Fig. 4) and
generate a dataset according to each DAG to investigate in
which settings the different conditional approaches offer ben-
efits. For each of these 4 datasets, we train a generative model
using each of the 3 conditioning approaches (Deterministic,
Undirected,Causal), giving 12 models in total. To evaluate
the effects of interventions, we intervene on a variable and
measure how the remaining variables changed as they appear
in the generative model’s output image. To estimate foreground
colour, background colour and digit we use external predictors

IBRAHIMet al.: TO DO(x) OR NOT TO DO(x) 5
f(x)trained on unbiased data (variable values sampled uni-
formly), whereas for thickness and intensity we use tools from
the Morpho-MNIST package [36]. The conditional variables
measured in the generated image (foreground and background
colour, thickness, intensity), are evaluated using the log-
likelihood under the true conditional distribution specified by
the DAG. More precisely, intervention on variableaof the
form do(a= ˜a)induces a joint distribution over the variables,
P( epado(a=˜a)) =
Y
v∈des(a)
p(v|a= ˜a)(2)
wheredes(a)are descendants ofa. Suppose we seek to
measure the accuracy of the generative model with regards to
variableb. We first generate the counterfactual image˜x (a=˜a)
before using a pretrained variable predictorϕ(x)to obtain ˆ˜b=
ϕ(˜x(a=˜a))|b, for which we then compute the log-likelihood
against the distribution defined in (2). The case for digit is
slightly different as it is discrete, hence we assess correctness
of an effect by measuring the difference in the highest softmax
value of the digit variable in the model’s SCM. Because digit
is never a child variable, it does not change forDeterministic
andCausalconditionings as these do not change parents by
design, but changes only forUndirected.
For the DAG in Fig. 4(a) that assumes one parent with two
children, Table I shows that when intervening on the parent
variable, digitd, both theCausalandUndirectedapproaches
estimate the effect on the children appropriately. In contrast,
theDeterministicdoes not obey the causal graph so does not
change these variables. Moreover, when one of the children
(f, b) is changed, we see no effect on the parentdwith
CausalandDeterministicbut due to the bidirected nature of
Undirected, this change has an influence on the digit variable.
These patterns are further exhibited for the other DAGs (Fig. 4
b, c, d). This shows thatDeterministickeeps variables constant
more than desired under the assumed DAG, whileUndirected
tends to change them too readily. We gain further insights
from the DAGs in Fig. 4 (b) and (c) where we have variables
with both a parent and a child (blue variables). Tables II and
III show that when we intervene on these (blue) variables,
Causalestimates the children (green) as it should, whereas
Determinsticdoes not.Causalalso maintains the parent (red)
as it should whereasUndirectedchanges it. Overall, this
demonstrates thatCausalbehaves well in all settings while
the other approaches perform only in specific settings, namely
when intervening on children forDeterministicand on parents
forUndirected. For our experiments on medical data, we thus
seek graphs taking these forms to investigate this effect further.
A. Graph Misspecification
To be beneficial, as in the above analysis, causal inference
relies on the assumption that the DAG is correctly speci-
fied, capturing the true relationships between the variables.
However, in real-world problems, we may not know the
true underlying causal relationships. How much can wrong
causal assumptions hinder generative models? We explore the
ramifications of using an incorrectly specified graph for DAG
(b) in Fig. 4. To achieve this, we keep the same data but reverse
the assumed direction of the causal relationships in the model
(Fig. 5). Clearly, this affects only theCausalmodel since the
others do not consider the directions of relationships.
As seen in Table V, this leads toCausalmatching the worse
of the other two methods in each case. Although this is an
extreme case where the arrows are deliberately reversed, it
serves as a warning of the importance of using the correct
graph if causal models are employed. In real world settings,
practitioners may use domain knowledge or statistics from the
data to narrow down the space of plausible graphs. Advanced
techniques from causal discovery [37], [38] could also be used,
though their application to visual data has been limited to date.
VI. EXPERIMENTS WITHCHESTX-RAYS
A. Setup
We continue by investigating the generative models on clin-
ical data, using the Chexpert dataset [39] of chest x-rays. We
partition the 187k samples at the patient level into a 70/20/10%
train/validation/test split. To study causal generative modelling
with this data, we identify an appropriate set of variables for
which there is clinical evidence of relationships; we posit that
agecausespleural effusion(PE). This association is supported
by the data as the mean age of patients with PE is 63.1 while
the mean of those without is only 58.7, and a t-test shows that
this difference is significant at the 5% level. Although this
does not prove that age causes PE, there is clinical evidence
to suggest that this relationship is true [40]. Regardless, for
the purpose of experimenting with causal modelling, we here
assume this correlation is causal. It is also generally accepted
that PE causes a decrease inlung volumeas the excess fluid
in the pleural space compresses lung tissue [41]. Finally, there
is evidence that lung volume decreases with age [42]. These
relationships form the DAG in Fig. 6, which we use in our
analysis. Finally, we also addsexas a conditional variable
of the V AE, so that it can be manipulated, although it is not
connected to the other graph variables. For each experiment
we report the average over 3 seeds.
B. Counterfactuals with Different Conditioning Methods
Using Chexpert, we train models with each of the condi-
tioning approaches. To evaluate the quality of CFs, we use
images of the test split and intervene on (change) each of
the variables in turn. However, unlike with Morpho-MNIST,
here we do not have the ground truth causal effects and data
generating process, so we are unable to precisely evaluate
whether variables in our image counterfactuals accurately fol-
low the proposed DAG with metrics such as the log-likelihood.
Instead, we develop a proxy metric; we first train a separate
predictor of each parentpfrom its childrenc, without using the
image as input, and denote each respective predictorϕ c→p. For
evaluation, we intervene on a parent variablepvia do(p= ˜p),
to obtain the counterfactual image,˜xp= ˜p. From this, we extract
the estimated counterfactual child value,˜c=c(˜x)using a
separately trained predictor. We then use the trained predictor
ϕc→p to estimate the value of the parent post-intervention,
ˆ˜p=ϕc→p(˜c) =ϕc→p(c(˜xp= ˜p))

6 IEEE TRANSACTIONS AND JOURNALS TEMPLA TE
Fig. 4: We implemented four generative processes for synthesising four coloured MNIST datasets, when relations between
variables are follow the above DAGs. Variables: Digitd, thicknesst, intensityi, background colourb, foreground colourf.
Int. Effect Det. Undir. Causal
d f(↑) -2.56 -1.52 -1.51 b(↑) -2.55 -1.75 -1.72
f b(↑) -1.15 -2.12 -1.14 d(↓) 0 0.17 0
b f(↑) -1.04 -2.72 -1.04 d(↓) 0 0.16 0
T ABLE I: CFs on DAG (a).
Int. Effect Det. Undir. Causal
t i(↑) -7.03 -4.17 -4.13 f(↑) -5.05 -3.72 -3.77
i t(↑) -2.19 -5.25 -2.18 f(↑) -5.93 -3.91 -3.97
f t(↑) -2.65 -5.27 -2.57 i(↑) -3.86 -6.95 -3.93
T ABLE II: CFs on DAG (b).
Int. Effect Det. Undir. Causal
d f(↑) -2.73 -0.65 -0.67 b(↑) -2.65 -0.43 -0.39
b f(↑) -2.61 -0.65 -0.66 d(↓) 0 0.13 0
f b(↑) -0.84 -2.63 -0.83 d(↓) 0 0.13 0
d& f(↑) -2.62 -0.99 -0.96b
T ABLE III: CFs on DAG (c).
Int. Effect Det. Undir. Causal
d t(↑) -5.35 -3.29 -3.31 f(↑) -2.64 -1.50 -1.54
t f(↑) -2.24 -1.28 -1.27 d(↓) 0 0.14 0
f t(↑) -2.75 -5.30 -2.73 d(↓) 0 0.16 0
d& f(↑) -2.42 -1.15 -1.19t
T ABLE IV: CFs on DAG (d).
TABLES I-IV: Effect of intervening on each variable in each DAG in Fig. 4. Forf, b, t, iwe measure log-likelihood while for
dwe use 1 - softmax correct digit. Arrows represent whether a higher or lower score is better. Bold denotes the best performing
model, while underline denotes the second.Causalis always the best or not statistically significantly worse than the best.
Fig. 5
Int. Effect Det. Undir. Causal
t i(↑) -6.94 -4.21 -6.93 f(↑) -4.96 -3.81 -4.89
i t(↑) -2.17 -5.25 -5.16 f(↑) -5.68 -4.03 -5.65
f t(↑) -2.44 -5.52 -5.30 i(↑) -3.85 -6.74 -6.99
T ABLE V
Fig 5: True relations (green) are reversed in the misspecified
model (red). TABLE V: Similar to Table II but for misspecified
model (Fig 5). “Wrong assumptions” affectCausal.
This allows us to calculate the error|| ˆ˜p−˜p||, through which
we estimate the effectiveness of the intervention [43] 1. To
obtain a useful predictorϕ c→p whencis a discrete variable,
we train on soft labels, namely the probability output of a
predictor forcwhen applied on the training images. To ensure
that these probabilities are meaningful, we use the validation
set for calibration. For parents of variables that are intervened
on, we simply check that they are left unchanged, an extension
of the Composition metric proposed by [43].
Results from evaluating counterfactuals on the test-split are
shown in Table VI. These support the findings from Section
V thatCausalandDeterministicperform better at maintaining
the value of parent variables when a child variable is changed.
This effect is very clear for the effect on age, as these two
approaches change it far less thanUndirected. However, for
the effect on the pleural effusion variable, there appears to
be greater entanglement as both of these methods flip this
variable incorrectly∼30%of the time when lung size is
changed. Moreover, the effect on the variable that is intervened
on is similar across the models as this does not rely on any
variable relationships and is more a measure of the ability of
1We experimentally verified this metric by testing it on Morpho-MNIST
and comparing it with the ground truth (not shown due to space limitations).
Fig. 6
Intervention Effect (↓) Det. Undir. Causal
Age
Age 2.983 3.176 2.808
PE* 23.721 8.346 8.335
Lungs* 23.820 11.901 11.713
PE
Age 3.455 9.711 3.788
PE 0.066 0.069 0.064
Lungs* 0.476 0.354 0.371
Lung Size
Age 3.700 10.640 3.825
PE 0.318 0.564 0.307
Lungs 0.018 0.020 0.019
T ABLE VI
Fig 6: DAG used for the chest x-ray experiments. Age(a)
causes pleural effusion(p), and both cause lung volume(l).
TABLE VI: Effect on parent of changing child variable for
each of the approaches. Age is measured in MAE, Pleural Ef-
fusion (PE) is measured by percentage error. Effects followed
by * are evaluated via the proxy approach described above
and thus, measured using the intervention.
the generative model to respect desired conditions. Overall, the
Causalapproach gives either the best or close-to-best results
in all cases, while the other two fail for different types of
interventions.
C. Dataset Augmentation
We now explore how generating data using these approaches
helps ameliorate unwanted biases in training data. We sample
the original data in such a way as to induce a strong, spurious
correlation between the PE and sex variables. More precisely,
we define a “bias level”b∈[0,1]. Forb=b 0, we sample the
data so thatb 0 proportion of male samples are healthy,1−b 0
have pleural effusion, and the opposite for females (b 0 pleural
effusion). We then train a PE classifier using thisbiaseddata
before evaluating the predictor on theunbiased, original test-
split. Such a PE classifier will have sub-optimal performance
on unbiased test data, due to using spuriously correlated
features to predict PE, such as using obvious anatomical

IBRAHIMet al.: TO DO(x) OR NOT TO DO(x) 7
differences between males and females, artificially induced in
the training data.
To study how well they can mitigate the bias, we then
train 3 generative models, one per conditioning approach,
with the biased training data. For each of the 3 models sepa-
rately, we generate images using 2 approaches: counterfactuals
and sampling from the latent space (Sec. IV-B). With each
approach, we create one synthetic sample per image in the
biased training set, with inverse proportion of healthy/PE per
sex (inverse bias level,1−b), to rebalance the training data.
Finally, for each method, we train a PE classifier on the
corresponding augmented, rebalanced training data (synthetics
+original biased). We then evaluate the PE classifier on the
unbiased test-split, where better generalisation indicates that
the corresponding generative method removed the spurious
correlations from the data, by better handling of the underlying
variables (sex, PE). Results are shown in Table VII.
Labels Bias No Aug. Sampling Counterfactual Det. Undir . Causal Det. Undir . Causal
100%
0.5 91.4 92.0 91.0 91.8 91.2 91.9 91.6
0.8 86.4 87.8 87.4 87.3 88.0 87.2 87.6
0.9 85.1 85.1 85.2 83.5 84.3 86.7 85.0
0.95 81.8 82.2 83.6 83.1 82.6 84.0 84.3
1 50.3 51.5 51.1 51.8 52.8 51.3 52.7
20%
0.5 86.2 88.3 90.3 90.5 87.2 88.9 88.5
0.8 85.0 87.2 87.1 89.9 86.3 87.9 89.3
0.9 78.7 79.6 82.3 82.1 80.1 82.5 82.4
0.95 77.0 77.4 80.7 79.8 77.4 79.5 79.7
10%
0.5 85.7 86.7 88.5 88.6 87.1 88.7 87.9
0.8 81.5 82.4 86.4 85.9 81.6 85.2 86.1
0.9 78.7 80.9 82.0 81.9 80.3 82.2 82.1
0.95 75.5 77.4 80.6 79.3 75.8 79.6 79.7
5%
0.5 85.1 86.5 88.0 88.5 85.9 87.7 86.3
0.8 76.8 77.1 81.5 81.4 75.9 79.1 77.8
0.9 75.4 79.2 79.2 80.5 76.9 78.4 80.1
0.95 74.7 76.9 78.0 79.0 75.7 76.3 77.5
1%
0.5 78.3 83.5 85.0 87.2 81.9 83.3 83.7
0.8 75.6 79.3 81.8 81.5 76.9 78.8 80.4
0.9 74.7 79.3 79.3 79.0 74.1 77.5 77.7
0.95 72.8 74.4 76.1 76.2 73.8 75.6 74.7
Average 78.90 80.65 82.15 82.33 79.79 81.54 81.67
T ABLE VII: AUC of pleural effusion predictor for raw CheX-
pert data (no augmentation) and augmented with synthetic data
from each of the three conditioning approaches and each of
the two generation methods. Green indicates the best AUC
in that row. Bold indicates the best performance within the
specific generation approach (sampling/counterfactual).
The results show that augmenting the data with synthetic
images improves classifier performance, as shown in the
literature when training data forDeterministicgenerative
models [5]. Importantly, though, we find this is the case
for all labelled percentages and bias levels, suggesting even
generative models trained with fewer labels and more biased
data can provide benefits. When the dataset is fully labelled,
the three conditioning approaches perform similarly. However,
as the labelled percentage decreases, we find thatUndirected
andCausaltend to outperformDeterministic. This suggests
that the stronger inductive biases provided by the graph in
these models can ameliorate the lack of labels. Since pleural
effusion is correlated with a variable (sex) outside of the
modelled causal graph (Fig. 6), we hypothesise the additional
information provided by the age and lung size variables are
key in providing counterracting this bias.
Another important observation is that for higher labelled
percentages, the performance using synthetic data generated
Metric Sampling Counterfactual Det. Undir. Causal Det. Undir. Causal
FID 2.280 2.292 3.307 1.815 2.221 1.730
MMD 0.054 0.049 0.055 0.051 0.048 0.038
SSIM 4.37% 5.36% 4.79% 4.01% 3.85% 4.07%
LPIPS 0.198 0.157 0.158 0.147 0.135 0.150
T ABLE VIII: Quality of the data generated by each method.
via counterfactuals tends to be better than when using sampled
data. We believe this is due to the counterfactuals being
of slightly better image quality due to the image prior that
is provided. To investigate this, we measure the quality of
images generated by each method (Table VIII). For all metrics,
we first embed the images to a shared latent space using a
DenseNet121 model pre-trained on chest x-ray data [44]. To
evaluate image quality, we consider the case with 1% of the
data labelled to show that even in this case, CFs produce better
quality, although we find similar results for all label levels.
For metrics, we use FID [45], maximum mean discrepancy,
structural similarity index metric [46] and the LPIPS metric
[47]. This allows us to build a comprehensive picture of how
the distribution of generated images compares to our training
samples. As shown in Table VIII, the images produced by
the counterfactuals tend to be of higher quality than those
produced by sampling. Example outputs are shown in Fig. 7
(left), where the counterfactuals (bottom) appear to be of
higher perceptual quality than the sampled images (top).
Fig. 7: Left: Examples of sampled (top) and counterfactual
(bottom) images. Right: PCA of embeddings of images gener-
ated via Sampling vs Counterfactual when 1% data is labelled.
However, in lower label regimes, the sampling approach
begins to perform better. We suspect that this is because with
a counterfactual we only create a modification of an existing
labelled sample. Thus when labelled samples are few, the
diversity of counterfactuals is also low. To measure diversity
we encode the images into the same latent embedding space
and then use a range of metrics such as the average L2 distance
between the points in the latent space and the covariance of
these points, with larger values for each indicating greater
spread and thus, diversity. We also measure the proportion of
points with nearest neighbour further than a certain threshold,
ϵ= 0.0005. Finally, we conduct k-means clustering and use
these clusters to calculate the entropy of the embedded data.
In Fig. 8, we see that, especially for lower label percentages,
sampling results in more diverse images than counterfactuals.
This is further portrayed in Fig. 7 (right), which clearly depicts
the greater spread of the first two principal components of the
embeddings of the images from sampling compared to those
from counterfactuals.

8 IEEE TRANSACTIONS AND JOURNALS TEMPLA TE
Samp
Det
Samp
Undir
Samp
Causal
CF
Det
CF
Undir
CF
Causal
Method
0.0004
0.0005
0.0006
0.0007
0.0008
0.0009L2 Value
L2
Samp
Det
Samp
Undir
Samp
Causal
CF
Det
CF
Undir
CF
Causal
Method
36000
35000
34000
33000
32000
31000
30000
Covariance Value
Covariance
Labels
100
20
10
5
1
Samp
Det
Samp
Undir
Samp
Causal
CF
Det
CF
Undir
CF
Causal
Method
0.5
0.6
0.7
0.8Nearest Neighbour Percentage
Nearest Neighbour
Samp
Det
Samp
Undir
Samp
Causal
CF
Det
CF
Undir
CF
Causal
Method
2.9
3.0
3.1
3.2
3.3Entropy Value
Entropy
Diversity of each method for different label proportions
Fig. 8: Diversity of the data generated by each of the methods. Higher indicates greater diversity for each metric.
Overall, these results suggest that both theCausaland
Undirectedapproaches provide improved performance over
simpler conditioning when augmenting a training dataset.
Moreover, when a large proportion of labels are available,
the greater realism of counterfactuals provides a benefit
over sampling new images. On the other hand, these
counterfactuals suffer from a lack of diversity when in low
label regimes, when the diversity of the sampled images leads
to better downstream results.
D. Fairness
We extend the previous analysis to explore the effect
of the different conditioning approaches on the fairness of
downstream predictors. We consider the performance of the PE
classifier on five age categories (-20, 20-40, 40-60, 60-80, 80-
). We report the difference in AUC between the best and worst
performing groups (fairness gap) in the same label and bias
settings as in Sec. VI-C, when generating synthetic data such
that it counteracts the correlation between PE and sex. Note
that even though we consider the fairness gap between age
categories, we do not explicitly control for bias in age when
augmenting the training data. Results are shown in Fig. 9. The
non-augmented data often results in the least fair model, due
to the inherent imbalanced prevalence of PE in older groups
(Sec. VI-A). Augmentation via theUndirectedmethod is the
worst at improving fairness with respect to age, which we
analyse further below.
0.5 0.8 0.9 0.95
Bias Level
12
14
16
18
20
22
24
26
28Fairness Gap
1% Labels
No Augmentation
Sample Deterministic
Sample Undirected
Sample Causal
CF Deterministic
CF Undirected
CF Causal
0.5 0.8 0.9 0.95
Bias Level
12
14
16
18
20
22
24Fairness Gap
5% Labels
0.5 0.8 0.9 0.95
Bias Level
12.5
15.0
17.5
20.0
22.5
25.0
27.5
30.0Fairness Gap
10% Labels
0.5 0.8 0.9 0.95
Bias Level
12
13
14
15
16
17
18
19Fairness Gap
20% Labels
Fig. 9: AUC of each method stratified by age group.
We further study fairness under distribution shift. We con-
duct similar experiments as before, by training generative
models on artificially biased CheXpert (10% labels) and
augmenting it with synthetic images, so that the prevalence of
PE is balanced between sexes. We then train one PE classifier
for each version of the balanced augmented data. Differently
than before, however, we now test performance on MIMIC
[48], while measuring performance gap with respect to sex,
as well as age as before. Table IX shows the results. We
again see that augmentation with synthetic data improves the
performance of the PE classifier, in particular theUndirected
andCausalapproaches. Moreover, we find that the CFs en-
hance performance slightly more than unconditional sampling,
supporting the previous conclusion from Table VIII. As we are
controlling for sex when synthesising data, we also see that
there is a slight improvement (decrease) in the fairness gap
for sex with all methods.
Method Acc. (↑) AUC (↑) F1 (↑) Gap - Sex (↓) Gap AUC - Age (↓)
No Augmentation 0.7262 0.8729 0.5963 0.0214 0.0867
Sample
Deterministic 0.7490 0.8918 0.6027 0.0192 0.0552
Undirected 0.7638 0.8899 0.6129 0.0187 0.0697
Causal 0.7604 0.8922 0.6183 0.0199 0.0519
CF
Deterministic 0.7518 0.8905 0.6115 0.0196 0.0622
Undirected 0.7652 0.8942 0.6186 0.0202 0.0774
Causal 0.7641 0.8967 0.6207 0.0194 0.0667
T ABLE IX: Performance on MIMIC data of methods trained
using non-augmented and augmented Chexpert data.
However, for age, a variable we do not control for, we
find there is a statistically significant difference (ANOV A)
between the resultant fairness gaps by the three conditioning
approaches.DeterministicandCausalreduce this gap for both
generation methods, whereasUndirectedprovides less benefit.
This may be due to the DAG connection from PE to age,
which is only present in theUndirectedconstruction (in this
direction). After intervening on the PE variable for a particular
image, such as to synthetise a healthy CF, we then have to
sample age conditional on the PE variable. This results in
a bimodal distribution of many healthy younger samples and
diseased older samples, undesirably over-amplifying the learnt
correlation between age and PE in the anti-causal direction.
On the other hand, asDeterministicandCausaldo not have
this connection (in this direction), age is sampled uncondi-
tionally, enabling augmentations that rebalance the existing
correlations. These differences are presented visually in the
kernel density estimate plots in Fig. 10. Finally, we present
two examples of interventions in Fig. 11 to observe how
these differences manifest visually. TheCausalapproach alters
almost exclusively the lungs to add/remove PE. Conversely,
whileUndirectedchanges the lungs, it also alters other parts
of the image, potentially because they are affected by variables
that are mistakenly changed (e.g. age). In conclusion, these
results show that in the setting where we try to mitigate a
spurious correlation of 2 variables, here sex and PE, theUndi-

IBRAHIMet al.: TO DO(x) OR NOT TO DO(x) 9
20 40 60 80 100
Age
0.000
0.005
0.010
0.015
0.020Density
Healthy
Pleural Effusion
Healthy
Pleural Effusion
20 40 60 80 100
Age
0.000
0.005
0.010
0.015
0.020Density
Density of Sampled Ages using Undirected Approach
20 40 60 80 100
Age
0.0000
0.0025
0.0050
0.0075
0.0100
0.0125
0.0150
0.0175
0.0200Density
Density of Sampled Ages using Deterministic/Causal Approach
Healthy
Pleural Effusion
Healthy
Pleural Effusion
Density of Sampled Ages using Deterministic/Causal Approach
20 40 60 80 100
Age
0.0000
0.0025
0.0050
0.0075
0.0100
0.0125
0.0150
0.0175
0.0200Density
0.0100Density
Fig. 10: Density estimate of ages from samples produced
by each method.Undirectedsamples age depends on disease
status, resulting in a difference between ages of samples with
pleural effusion (red) and those without (green).Deterministic
andCausalsample age unconditionally, resulting in greater
overlap between samples with and without pleural effusion.
rectedapproach mishandles the parent (age) of the intervened
variable (PE). In this setting,CausalorDeterministicseem
preferable.
Fig. 11: Example interventions usingCausalvsUndirected.
On the left (red), we intervene with do(disease) and on the
right (green) with do(healthy). For each of these we show
the original image, interventions usingCausalandUndirected,
and difference maps between original and counterfactuals.
VII. CONCLUSION
In this work, we present and investigated six approaches
to generative modelling for synthesising medical images.
We delineate three approaches for conditioning a generative
model, of increasingly strong assumptions about the causal
relationships between variables. Moreover, we consider gen-
erating images both by synthesising counterfactuals of existing
images and synthesising “de novo” images by sampling from
the latent space of the generative model. The study explores
which approach is appropriate under different conditions.
Analysis on Morpho-MNIST, where we control the data
generating process, shows a clear distinction between the three
conditioning approaches for generating counterfactuals. If the
correct causal graph has been identified,Causalmodelling
offers consistently high performance on all explored types of
DAGs. TheDeterministicapproach is found too rigid and,
by design, will only change the variable that we intervene
on. Conversely, theUndirectedapproach is too flexible and
changes variables more than it should. However, when the
graph is misspecified, the advantage ofCausalmodelling
disappears. The results highlight that when an ML practitioner
is uncertain about the DAG underlying the data generating
process,DeterministicorUndirectedconditioning may be
preferable overCausalmodelling.
By experimenting on clinical chest x-rays, although we
could not control the data generating process, we obtain key
insights about under what conditions causal modelling and
counterfactual generation are beneficial. Firstly, the stronger
inductive biases inCausalandUndirectedallow these models
to better overcome biases and a lack of labels in the data;
training on datasets augmented with data generated using
these approaches provides improved disease prediction perfor-
mance over no augmentation and the commonDeterministic
approach. Furthermore, with regards to the generation method,
we uncover a trade-off between the quality and diversity of the
synthetic data. While sampling new images allows us to gener-
ate essentially limitless quantities of data, the counterfactuals
are typically more perceptually accurate by being tied to a
real image. As such, sampling tends to perform better in low-
label settings where the number of possible counterfactuals is
limited. Conversely, the latter is favourable in high-label set-
tings where there are more possible counterfactuals and hence,
a smaller gap in diversity between approaches. Finally, we
explore implications of these approaches on fairness. Through
experiments on both CheXpert and MIMIC, we discover a
latent downside ofUndirected, namely that the bidirectional
relationships may lead it to exacerbate existing biases unless
carefully controlled for. This is in contrast toDeterministic
andCausal, provided the proposed DAG is correct. Overall,
we have demonstrated the utility of causal techniques for
synthetic data augmentation, under which conditioned each
is advantageous, and hope that future research will build on
this to design ever more potent models.
VIII. FUTUREWORK
This investigation covered three conditioning approaches,
using a variant [35] of a causal hierarchical V AE [34] for
its proven capabilities in counterfactual generation. While no
assumptions were made about the underlying model, validating
our findings using different causal models (e.g. diffusion)
would be desirable. Moreover, we experimented on 2D images,
because sufficiently capable 3D causal generative models have
not yet been developed, but should they become available,
it would be interesting to further validate these insights on
volumetric data. This would also allow for richer analysis with
data such as brain MRI where there are a greater number of
meta-variables and structures within the volume to control.
This would lend itself to another natural extension of using a
more complex causal graph. However, this also comes with the
pitfall that these more subtle changes may not produce visible
changes. Furthermore, in this work we have only explored the
use of synthetic data to augment training datasets. It would
thus be interesting to explore whether the benefits of the
causal model in this context carry over to other applications
such as stress testing pre-trained models. This is critical for
model deployment in real-world clinical settings through both
understanding how the model must be improved, and where
not possible, how to avoid deploying it in vulnerable settings.

10 IEEE TRANSACTIONS AND JOURNALS TEMPLA TE
REFERENCES
[1] A. Vrudhula, A. Kwan, D. Ouyang, and S. Cheng, “Machine learning
and bias in medical imaging: Opportunities and challenges,”Circulation.
Cardiovascular imaging, vol. 17, p. e015495, 02 2024.
[2] A. Paleyes, R.-G. Urma, and N. D. Lawrence, “Challenges in deploying
machine learning: A survey of case studies,”ACM Computing Surveys,
vol. 55, pp. 1 – 29, 2020.
[3] C. Jones, D. C. Castro, F. D. S. Ribeiro, O. Oktay, M. McCradden,
and B. Glocker, “No fair lunch: A causal perspective on dataset bias in
machine learning for medical imaging,” 2023.
[4] M. A. Shahul Hameed, A. M. Qureshi, and A. Kaushik, “Bias mitigation
via synthetic data generation: A review,”Electronics, vol. 13, no. 19,
2024.
[5] S. I. Ktena, O. Wiles, I. Albuquerque, S.-A. Rebuffi, R. Tanno,
A. Guha Roy, S. Azizi, D. Belgrave, P. Kohli, A. Cemgil, A. Karthike-
salingam, and S. Gowal, “Generative models improve fairness of medical
classifiers under distribution shifts,”Nature Medicine, vol. 30, pp. 1–8,
04 2024.
[6] P. A. Mor ˜ao, Y . Forghani, N. Louc ¸˜ao, P. Gouveia, M. A. T. Figueiredo,
and J. Santinha, “Data augmentation for medical imaging: Counter-
factual simulation of acquisition parameters via conditional diffusion
model,” inMedical Imaging with Deep Learning, 2025.
[7] L. W. Sagers, J. A. Diao, L. Melas-Kyriazi, M. Groh, P. Rajpurkar,
A. S. Adamson, V . Rotemberg, R. Daneshjou, and A. K. Manrai,
“Augmenting medical image classifiers with synthetic data from latent
diffusion models,” 2023.
[8] B. Khosravi, F. Li, T. Dapamede, P. Rouzrokh, C. Gamble, H. M. Trivedi,
C. C. Wyles, A. B. Sellergren, S. Purkayastha, B. J. Erickson, and J. W.
Gichoya, “Synthetically enhanced: unveiling synthetic data’s potential
in medical imaging research,”eBioMedicine, vol. 104, 2023.
[9] Z. Wang, Z. Wu, J. Zhang, X. Guan, N. Jain, S. Lu, S. Gupta,
and A. Koshiyama, “Bias amplification: Large language models as
increasingly biased media,” 2025.
[10] S. C. Wyllie, I. Shumailov, and N. Papernot, “Fairness feedback loops:
Training on synthetic data amplifies bias,” inThe 2024 ACM Conference
on Fairness, Accountability, and Transparency, FAccT 2024, Rio de
Janeiro, Brazil, June 3-6, 2024. ACM, 2024, pp. 2113–2147.
[11] A. Subramonian, S. Bell, L. Sagun, and E. Dohmatob, “An effective
theory of bias amplification,” inICLR, 2025.
[12] T. Chen, Y . Hirota, M. Otani, N. Garc ´ıa, and Y . Nakashima, “Would
deep generative models amplify bias in future models?”2024 IEEE/CVF
Conference on Computer Vision and Pattern Recognition (CVPR), pp.
10 833–10 843, 2024.
[13] Y . Bengio, A. C. Courville, and P. Vincent, “Representation learning: A
review and new perspectives,”IEEE Transactions on Pattern Analysis
and Machine Intelligence, vol. 35, pp. 1798–1828, 2012.
[14] J. Peters, D. Janzing, and B. Sch ¨olkopf,Elements of Causal Inference:
Foundations and Learning Algorithms, ser. Adaptive Computation and
Machine Learning. MIT Press, 2017.
[15] D. Coelho de Castro, I. Walker, and B. Glocker, “Causality matters in
medical imaging,”Nature Communications, vol. 11, 12 2020.
[16] A. Vlontzos, D. Rueckert, and B. Kainz, “A review of causality for
learning algorithms in medical image analysis,” 2022.
[17] N. Pawlowski, D. C. Castro, and B. Glocker, “Deep structural causal
models for tractable counterfactual inference,” inNeurIPS, 2020.
[18] K. Xia, K.-Z. Lee, Y . Bengio, and E. Bareinboim, “The causal-neural
connection: Expressiveness, learnability, and inference,” inNeurIPS,
2021.
[19] N. Dhinagar, S. Thomopoulos, E. Laltoo, and P. Thompson, “Counter-
factual mri generation with denoising diffusion models for interpretable
alzheimer’s disease effect detection,”bioRxiv, pp. 1–6, 07 2024.
[20] Y . Zong, Y . Yang, and T. M. Hospedales, “MEDFAIR: Benchmarking
fairness for medical imaging,” inICLR, 2023.
[21] Y . Li and Y . Fan, “Medical image segmentation with domain adaptation:
A survey,”arXiv preprint arXiv:2311.01702, 2023.
[22] E. Goceri, “Medical image data augmentation: techniques, comparisons
and interpretations,”Artificial Intelligence Review, vol. 56, no. 11, pp.
12 561–12 605, 2023.
[23] J. T. Guibas, T. S. Virdi, and P. S. Li, “Synthetic medical images from
dual generative adversarial networks,”arXiv preprint arXiv:1709.01872,
2017.
[24] I. J. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley,
S. Ozair, A. Courville, and Y . Bengio, “Generative adversarial networks,”
2014.
[25] M. Frid-Adar, E. Klang, M. Amitai, J. Goldberger, and H. Greenspan,
“Synthetic data augmentation using gan for improved liver lesion clas-
sification,” in2018 IEEE 15th International Symposium on Biomedical
Imaging (ISBI 2018), 04 2018, pp. 289–293.
[26] X. Yi, E. Walia, and P. Babyn, “Generative adversarial network in
medical imaging: A review,”Medical Image Analysis, vol. 58, p. 101552,
Dec. 2019.
[27] D. P. Kingma and M. Welling, “Auto-encoding variational bayes,” 2022.
[28] D. J. Rezende and S. Mohamed, “Variational inference with normalizing
flows,” inICML, ser. ICML’15. JMLR.org, 2015, pp. 1530–1538.
[29] A. Kazerouni, E. Khodapanah Aghdam, M. Heidari, R. Azad,
M. Fayyaz, I. Hacihaliloglu, and D. Merhof, “Diffusion models in
medical imaging: A comprehensive survey,”Medical Image Analysis,
vol. 88, p. 102846, 05 2023.
[30] J.-Y . Zhu, T. Park, P. Isola, and A. A. Efros, “Unpaired image-to-image
translation using cycle-consistent adversarial networks,” inICCV, 2017.
[31] P. Isola, J.-Y . Zhu, T. Zhou, and A. A. Efros, “Image-to-image translation
with conditional adversarial networks,”CVPR, 2017.
[32] E. Bareinboim, J. D. Correa, D. Ibeling, and T. F. Icard, “On pearl’s
hierarchy and the foundations of causal inference,”Probabilistic and
Causal Inference, 2022.
[33] P. Sanchez and S. A. Tsaftaris, “Diffusion causal models for counter-
factual estimation,” inProceedings of the First Conference on Causal
Learning and Reasoning, ser. Proceedings of Machine Learning Re-
search, B. Sch ¨olkopf, C. Uhler, and K. Zhang, Eds., vol. 177. PMLR,
Apr. 2022, pp. 647–668.
[34] F. De Sousa Ribeiro, T. Xia, M. Monteiro, N. Pawlowski, and
B. Glocker, “High fidelity image counterfactuals with probabilistic
causal models,” inICML, ser. Proceedings of Machine Learning Re-
search, vol. 202, 07 2023, pp. 7390–7425.
[35] Y . Ibrahim, H. Warr, and K. Kamnitsas, “Semi-supervised learning for
deep causal generative models,” inMICCAI. Springer, 2024, pp. 294–
303.
[36] D. C. Castro, J. Tan, B. Kainz, E. Konukoglu, and B. Glocker, “Morpho-
MNIST: Quantitative assessment and diagnostics for representation
learning,”Journal of Machine Learning Research, vol. 20, no. 178, 2019.
[37] P. Gradu, T. Zrnic, Y . Wang, and M. I. Jordan, “Valid inference after
causal discovery,”ArXiv, vol. abs/2208.05949, 2022.
[38] C. Glymour, K. Zhang, and P. Spirtes, “Review of causal discovery
methods based on graphical models,”Frontiers in Genetics, vol. 10,
2019.
[39] J. Irvin, P. Rajpurkar, M. Ko, Y . Yu, S. Ciurea-Ilcus, C. Chute, H. Mark-
lund, B. Haghgoo, R. Ball, K. Shpanskaya, J. Seekins, D. A. Mong,
S. S. Halabi, J. K. Sandberg, R. Jones, D. B. Larson, C. P. Langlotz,
B. N. Patel, M. P. Lungren, and A. Y . Ng, “Chexpert: a large chest
radiograph dataset with uncertainty labels and expert comparison,” ser.
AAAI’19/IAAI’19/EAAI’19. AAAI Press, 2019.
[40] P. Korczynski, J. Klimiuk, A. Safianowska, and R. Krenke, “Impact of
age on the diagnostic yield of four different biomarkers of tuberculous
pleural effusion,”Tuberculosis, vol. 114, 11 2018.
[41] B. Jany and T. Welte, “Pleural Effusion in Adults - Etiology, Diagnosis,
and Treatment,”Dtsch Arztebl International, vol. 116, no. 21, pp. 377–
386, 2019.
[42] G. Sharma and J. Goodwin, “Effect of aging on respiratory system
physiology and immunology,”Clin. Interv. Aging, vol. 1, no. 3, pp.
253–260, 2006.
[43] M. Monteiro, F. D. S. Ribeiro, N. Pawlowski, D. C. Castro, and
B. Glocker, “Measuring axiomatic soundness of counterfactual image
models,” 2023.
[44] J. P. Cohen, J. D. Viviano, P. Bertin, P. Morrison, P. Torabian,
M. Guarrera, M. P. Lungren, A. Chaudhari, R. Brooks, M. Hashir, and
H. Bertrand, “TorchXRayVision: A library of chest X-ray datasets and
models,” inMedical Imaging with Deep Learning, 2022.
[45] M. Heusel, H. Ramsauer, T. Unterthiner, B. Nessler, and S. Hochreiter,
“Gans trained by a two time-scale update rule converge to a local nash
equilibrium,” 12 2017.
[46] Z. Wang, A. Bovik, H. Sheikh, and E. Simoncelli, “Image quality assess-
ment: from error visibility to structural similarity,”IEEE Transactions
on Image Processing, vol. 13, no. 4, pp. 600–612, 2004.
[47] R. Zhang, P. Isola, A. A. Efros, E. Shechtman, and O. Wang, “The
unreasonable effectiveness of deep features as a perceptual metric,” in
CVPR, 2018.
[48] A. E. W. Johnson, T. J. Pollard, S. J. Berkowitz, N. R. Greenbaum, M. P.
Lungren, C. ying Deng, R. G. Mark, and S. Horng, “Mimic-cxr, a de-
identified publicly available database of chest radiographs with free-text
reports,”Scientific Data, vol. 6, 2019.
