---
title: Cross-cohort TB classification using clinical data gathered in Uganda and South Africa
url: https://arxiv.org/abs/2610.03256
category: ai-marketing
subcategory: measurement
date: 2026-10
venue: ''
authors:
- Joshua M. Jansen van Vüren
- Devendra S. Parihar
- Daphne Naidoo
- Marisa Klopper
- Frank Cobelens
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.03256
pages: 9
chars: 44860
fetched_at: '2026-11-08T13:25:34+00:00'
kb_version: 1
---

# Cross-cohort TB classification using clinical data gathered in Uganda and South Africa

Cross-cohort TB classification using clinical data
gathered in Uganda and South Africa
Joshua M. Jansen van V ¨uren
 ∗, Devendra S. Parihar
 ∗, Daphne Naidoo
 †, Marisa Klopper
 †, Frank Cobelens
 ‡,
Lutz Kolbe
 §, Kimsey Zajac
 §, Willy Ssengooba
 ¶, Moses Joloba
 ¶, Grant Theron
 †, Thomas R. Niesler
 ∗
∗Department of Electrical and Electronic Engineering,University of Stellenbosch, Stellenbosch, South Africa
†South African Medical Research Council Centre for Tuberculosis Research (CTR)
Division of Molecular Biology and Human Genetics, Faculty of Medicine and Health Sciences
Stellenbosch University, Cape Town, South Africa
‡Department of Global and Amsterdam Institute for Global Health and Development
Amsterdam University Medical Centers, University of Amsterdam, Amsterdam, The Netherlands
§Faculty of Business and Economics, University of G ¨ottingen, G ¨ottingen, Germany
¶Department of Medical Microbiology, College of Health Sciences
Makerere University, Biomedical Research Center (MAKBRC), Kampala, Uganda
Corresponding authors:jjvanvueren@sun.ac.za,trn@sun.ac.za
Abstract—We present a first evaluation of machine learning
applied to patient clinical and demographic data gathered in two
different countries for the purpose of tuberculosis (TB) screening
to identify people who would benefit from expensive molecular
testing. Experiments are based on the recently-compiled CAGE-
TB dataset, which includes sub-cohorts of people with presump-
tive TB presenting at community health care centres in South
Africa and Uganda. Three neural network architectures (logistic
regression (LR), multilayer perceptrons (MLP) and convolutional
neural networks (CNN)) are considered in conjunction with
greedy feature selection. For the convolutional neural network,
a strategy that jointly optimises feature selection and feature
ordering is proposed and shown to lead to consistent development
and test set improvements. For all three models, development
set area under the receiver operating characteristic (AUROC)
curve is improved by 2-7% using feature selection. LR after
feature selection achieves an AUROC of 0.8 [0.75,0.86] (95% CI)
and 0.84 [0.78,0.9] when testing on the held-out Ugandan and
South African data respectively. Although outperforming LR on
the development cohort, the deeper networks (MLP, CNN) show
inconsistent trends on the held-out cohorts, while LR achieves
performance within 1-2% of the best achieved in terms of
AUROC. LR narrowly misses the WHO minimum requirements
by 4-9% in sensitivity even though the network is being evaluated
on a completely held-out cohort. The development of neural-
network based classifiers for TB screening therefore appears
viable.
Index Terms—tuberculosis, screening, clinical and demo-
graphic data, convolutional neural network
I. INTRODUCTION
Despite being treatable, TB remains a primary cause of mor-
tality in lower and middle income countries. A key challenge
is that many cases remain undiagnosed, allowing the disease
to spread [1]. To address this, the World Health Organisation
(WHO) guidelines propose an accessible TB screening tool
that achieves 60% specificity at 90% sensitivity as part of a two
step screening protocol [2]. Such a tool should ideally be low-
cost and scalable and, most importantly, provide an efficient
and effective way to identify people presenting at busy primary
care clinics who require costly confirmatory molecular testing.
This work describes the development of such a screen-
ing method based on easily-obtainable patient-level clinical
and demographic information, and machine learning. All the
considered clinical and demographic values are either self-
reported, or the result of a basic measurement, or the result of
a point-of-care test. While such systems have been proposed
before, we place specific focus on the robustness of such
a classifier to the domain shift of the underlying features
associated with a change in the target population. Such a cross-
cohort analysis has not yet been reported.
The contributions of our work are as follows.
•We present the first analysis of clinical and demographic
data-based TB classification using neural networks across
two different countries (South Africa and Uganda).
•We show that such classifiers can be robust to the
associated domain shift and therefore may represent a
viable approach to TB screening.
•We propose and show the effectiveness of a joint feature
selection and ordering strategy allowing the effective
application of CNN to unstructured inputs such as clin-
ical and demographic data which do not require any
laboratory-based test.
II. RELATED WORK
Several studies have considered the classification of clinical
and demographic indicators as a way to triage for tuberculosis
[3]–[5]. Several of these studies consider only linear scoring
strategies, or rely on a single isolated measurement [6]–[9].
For example, a basic linear score comprising age, sex, HIV ,
diabetes, cough, fever, weight loss, night sweats, and longer
arXiv:2610.03256v1  [cs.LG]  2 Oct 2026

than 14-days of symptoms achieved an AUROC of 0.75 [0.69-
0.80] in a validation cohort ofn=387 adults in Uganda [10].
The application of machine learning methods for TB clas-
sification using datasets that include a wider set of patient-
level clinical and demographic information is an area of
growing interest. A random forest model applied to classify the
development of TB within a six month time-frame for people
living with HIV based on 48 laboratory and demographic
indicators was shown to achieve an AUROC of 0.83 [11].
Similarly, various sets of clinical data were considered as
inputs for machine learning TB classifiers in [4] and [12],
achieving AUROCs of 0.7 and 0.8 respectively. Generally,
higher performance is reported when laboratory based tests
are included as inputs to the machine learning models. For
example, utilising eighteen features derived from complete
blood counts, an XGBoost classifier is shown to achieve an
AUROC of 0.91 when trained to classify people with TB [13].
However, reliance on laboratory tests reduces the accessibility
of such methods.
In related work developing a neural network TB classifier
based on cough audio, an AUROC of 0.74 [0.70,0.78] was
achieved [3]. This was, however, outperformed by a model
trained only on clinical data (AUROC 0.81 [0.78,0.85]). Fur-
thermore, through external validation of the cough audio based
models to cough data from Peru, which is not one of the
countries in which data from the original study was collected,
AUROC fell to between 0.48 and 0.62 [14]. This highlights the
challenge of developing a tool which is robust to application in
unseen settings as well as the necessity of external validation
for TB screening.
Studies such as those mentioned above have considered the
overall TB classification performance that can be achieved
by machine learning using various clinical and demographic
data in various settings. However, no study has systematically
examined how these classifiers generalise when applied to
a held-out cohort from another country, where demographic
and clinical features may be differently distributed due to
geographic differences in risk for contracting TB and potential
differences in health systems and clinical practices. We address
this gap by conducting a cross-cohort TB classification anal-
ysis for two countries, Uganda and South Africa. The results
we obtain can be compared with our previous work, in which
only South African data was considered [15].
III. DATA
We utilise data from the Cough Audio triaGE for TB
(CAGE-TB) dataset, which was recently compiled in South
Africa and Uganda. Each country sub-cohort includes clinical
and demographic data collected from people who have self-
presented to a community clinic and are symptomatic for TB.
We list the 28 clinical and demographic features that were
successfully collected for every such person in Table I. The
enrolment criteria for the study included that a person should
have been experiencing a cough lasting at least two weeks.
No participants experiencing haemoptysis (coughing up blood)
were enrolled.
TABLE I: Clinical and demographic data gathered for each
participant in the data used for experimentation.
Feature Type
Age Quantitative (years)
Sex Binary (female, male)
Dyspnea Binary (yes, no)
Chest pain Binary (yes, no)
Previous TB Binary (yes, no)
Night sweats Binary (yes, no)
Chronic conditions Binary (yes, no)
Fever within last two weeks Binary (yes, no)
Coughing up sputum Binary (yes, no)
Recent weight loss (>1.5kg) Binary (yes, no)
Anaemic conjunctivae Binary (yes, no)
HIV status Binary (yes, no)
Height Quantitative (cm)
Weight Quantitative (kg)
BMI Quantitative (kg/m 2)
CRP concentration Quantitative (mg/L)
Mid-upper arm circumference Quantitative (cm)
Haemoglobin concentration Quantitative (g/dl)
Cough duration Quantitative (days)
Number of symptoms Quantitative (1,2,3,4)
Years since previous TB Quantitative (years)
TBscoreII [16] Quantitative (1,2,. . .,8)
ART status Multinomial (no - HIV neg, no - HIV pos, yes - HIV pos)
Respiratory rate Quantitative (breaths/min)
Heart rate Quantitative (BPM)
Axillary/ear temperature Quantitative (Celsius)
Smoking Multinomial (current, never, stopped <1,<12,>12 months)
Fagerstrom score Quantitative (-6,0,1,...,10)
Of the CAGE-TB South African and Ugandan sub-cohorts,
we consider only those participants for whom all 28 clinical
and demographic measurements listed in Table I are available.
Records with missing values are therefore disregarded in the
work presented here. Under this constraint, the South African
sub-cohort includes 347 participants, and the Ugandan sub-
cohort 374 participants. The number of TB positive and TB
negative cases per cross-validation fold in each sub-cohort is
presented in Table II. The TB status of each individual was
determined using a composite reference standard comprising
either a MGIT 960 liquid culture or an Xpert MTB/RIF Ultra
positive result.
TABLE II: TB positive and negative participants per cross
validation fold for the South African (SA) and the Ugandan
(UG) sub-cohorts used for experimentation.
Country Fold 1 2 3 4 5 6 7 8 9 10Total
SA # Pos 5 6 8 6 7 8 6 7 9 7 69 # Neg 29 27 33 29 25 27 31 28 24 25 278
UG # Pos 10 8 8 10 9 9 8 9 10 13 94 # Neg 31 29 22 32 31 30 24 25 25 31 280
Total # Pos 15 14 16 16 16 17 14 16 19 20 163 # Neg 60 56 55 61 56 57 55 53 49 56 558
IV. EXPERIMENTAL SETUP
In the following we describe the classifier architectures
used for experimentation, the optimisation strategy for the

associated hyperparameters, the configuration of the cross-
cohort experiments, the way in which the clinical and de-
mographic features are encoded for use as classifier inputs,
and the method of feature set optimisation. The results of the
experiments themselves are then presented in Section V.
A. Neural network classifiers
We employ three different neural network architec-
tures: logistic regression, multi-layer perceptron, and a one-
dimensional convolutional neural network.
1) Logistic regression:The formulation of LR, is presented
in Equation 1, wherexis the input encoded feature vector
whilewandbare the learned weight vector and scalar bias
respectively.
ˆy= 1 1 +e−(wT x+b) (1)
The model is trained to letˆyapproximate the posterior
probability of TB positivity. LR is a linear model with com-
paratively few parameters. It therefore has the advantage of
being less likely to overfit, but is limited by its linear decision
surface.
2) Multi layer perceptron:The MLP architecture comprises
several fully connected layers, each with an activation func-
tion. The first layer receives the feature vector as input, and
the activations of this layer are passed to the subsequent
layers. The activations of all except the final layer are often
referred to ashiddenrepresentations. The final layer produces
a binary output, again approximating the posterior probability
for TB. In comparison with LR, MLPs are able to model non-
linear relationships in the training data. However, they are
also more prone to overfitting, and therefore only two and
three layer networks are considered here. The dimensionality
of the hidden representations, as well as the type of activation
function in the hidden layers are treated as hyperparameters
and optimised using a grid-search during cross-validation. The
values found in this way are presented in Table IV.
3) Convolutional neural network:Previous work has indi-
cated that a CNN can be applied to clinical and demographic
data for tuberculosis classification [15]. Here we apply the
same model architecture, as presented in Table III. As for the
LR and MLP classifiers, the network is trained to approximate
the posterior probability for TB.
TABLE III: One-dimensional CNN structure reproduced
from [15]. The output dimensions of all but the last layer
depend on the input dimension.
# Layer type Kernel dim Num (C) Stride (s) Activation
1 Conv(3×1)20 1 ReLU
2 Max pool(2×1)- 1 -
3 Conv(3×1)50 1 ReLU
4 Max pool(2×1)- 1 -
5 Dense - - - Sigmoid
Convolutional neural networks are typically applied to
images, because they have been shown to very effectively
leverage the identification of local features to achieve strong
classification performance. Images encode the specific geomet-
ric structure of the objects they contain in the spatial ordering
of the pixels. However, no such spatial structure or defined
ordering exists for the kind of demographic and clinical data
we consider here. Therefore, for a CNN to be effective, the
ordering of the feature vector must be optimised. In previous
work this was achieved through the brute-force repeated re-
training of the model using different random permutations of
the ordering. In Section IV-F we will propose a new and more
effective strategy for discovering the best way to arrange and
order the feature vector.
The closest related research considering the application of
CNNs to tabular inputs in which a natural feature ordering is
absent is found in the area of genomics and transcriptomics.
In this case, genetic tabular information is arranged into a
two-dimensional grid for application to image-based CNNs.
This can be accomplished either by preserving inter-feature
distances [17]–[19] or by learning the assignment end-to-
end [20]. Alternatively, previous work has investigated insert-
ing a learned dense projection ahead of a one-dimensional
CNN so that the convolution operates on a soft-reordering
of the input features rather than on the raw features [21]. In
contrast, in the work we present here we retain a convolution
over the raw feature vector, and perform an explicit joint
search over feature selection and positional ordering in one
dimension to directly optimise the development-set AUROC.
B. Hyperparameter search
We search the set of hyperparameters presented in Table IV
in a grid-fashion, selecting those which optimise the average
development set AUROC. The hyperparameters for each of
the three architectures are optimised separately for the Ugan-
dan and for the South African sub-cohort. In addition, the
hyperparameter search is repeated for both the full set of 28
input features as well as for the reduced set of input features
identified during sequential feature selection, as described in
Section IV-E. The Adam optimiser is utilised in all experi-
ments, with a weight decay of 0.01 [22]. Weight decay was
considered a hyperparameter in preliminary experiments, and
a value of 0.01 was found to be optimal for all three models.
All networks are trained using PyTorch [23].
C. Cross-cohort analysis
Experiments are conducted by considering only one sub-
cohort for model training and hyperparameter optimisation,
after which the optimised models are directly applied to the
other sub-cohort, which serves as a held-out test set in a
different domain (country). Subsequently, the alternate experi-
ment in which the sub-cohorts are switched is performed. This
procedure is illustrated in Figure 1.
Considering each cohort as a fully held-out test set serves
as a means of verifying that the classifiers do not overfit the
training population. For each test-set a confidence interval is
calculated using DeLong’s method [24]. Finally, because these
classifiers are intended to be used for screening, an operating

Fig. 1: Illustration of ten-fold cross-cohort cross validation. In the cross validation loop, each of the ten folds is held out in
turn as a development set for hyperparameter optimisation, while the entire held-out cohort is used as a test set.
TABLE IV: Hyperparameters and the ranges considered during
optimisation. Optimal hyperparameters for LR and the MLP
are presented for the subset of features identified during SFS.
Optimal parameters for the CNN are presented after the joint
optimisation of the order and chosen features of the input
vector. SA: Optimal hyperparameters for South Africa, UG:
Optimal hyperparameters for Uganda.
Classifier Hyperparameter Range SA UG
LR Learning rate 0.01, 0.001 0.01 0.001
LR Batch size 8, 16, 32 8 32
LR Epochs 1,. . .,128 2 66
MLP Activation ReLU, Tanh Sigmoid SigmoidSigmoid
MLP
Hidden layer [16], [64]
dimensionality [16,16], [16,64] [64] [16]
[Layer 1, . . . ,Layern][64,16], [64,64]
MLP Learning rate 0.01, 0.001, 0.0001 0.01 0.01
MLP Batch size 8, 16, 32, 64 , 128 32 32
MLP Dropout rate 0.1, 0.3, 0.5, 0.7 0.3 0.3
MLP Epochs 1,. . .,128 3 89
CNN Learning rate 0.01, 0.001 0.001 0.01
CNN Batch size 8, 16, 32 16 16
CNN Epochs 1,. . .,128 77 18
point must be determined. To accomplish this, we select the
classification threshold which achieves a 90% sensitivity for
each of the development sets (after hyperparameter optimisa-
tion) [2]. This value is then averaged and applied directly to the
held-out sub-cohort, from which a specificity and sensitivity
is reported.
D. Feature encoding
In this section we describe how the features were encoded
for presentation as input to the neural network classifiers. All
quantitative values are presented as inputs without modifica-
tion. Binary features were encoded using a value of zero to
indicate false, and a value of one to indicate true. Finally,
a one-hot representation was utilised for multinomial values.
Per-feature mean and variance normalisation, based on the
training set, is applied during training and testing.
Previous work has shown that grouping chronic conditions
into a single binary indicator afforded small but consistent
improvements over a separate encoding [15]. Therefore we
adopt this strategy here. A single binary indicator is employed
to encode whether the participant has suffered from any
chronic condition. Specifically this condition must have: lasted
for one year or longer, require ongoing medical attention, or
limit activities of daily living.
We also explore the impact of smoking habits (Table I). This
is achieved via a multinomial encoding that indicates whether
a participant has: never smoked, currently smokes, has quit
smoking less than one month ago, or between one and 12
months ago, or more than one year ago.
E. Sequential feature selection
For both sub-cohorts, the same 28 clinical and demographic
features are available (Table I). We utilise sequential feature
selection (SFS) to identify those features among these 28
which are the most useful for TB classification. SFS is
a greedy algorithm which begins by identifying the single
feature which produces the best model performance, here
assessed using AUROC. It then iteratively adds additional
features one by one from the remaining pool. Each additional
feature is selected based on whether its addition affords the
best AUROC on average across the ten development sets
during cross-validation.
We first apply SFS in this way to the South African sub-
cohort, resulting in a set of features identified as optimal
for this data. After re-introduction of the development data,
this set of features is used to train a final model using
the South African data. This model is then applied to and
evaluated against the Ugandan sub-cohort. Subsequently, the
corresponding alternative experiment is performed, where SFS
and model training is performed on the Ugandan sub-cohort,
and this is evaluated on the South African data.
F . CNN sequential feature selection and ordering
We propose a new strategy for simultaneously optimising
feature selection and feature ordering for the CNN archi-

TABLE V: Classifier average development (±stddev) and
test (95% CI DeLong [24]) performance. Spec @ Sens: Test
set specificity and sensitivity from threshold determined to
achieve 90% sensitivity on average over the development set.
Development set values are presented as mean and standard
deviation over cross validation folds.
Model South Africa Dev AUROC Uganda Test AUROC Spec @ Sens
LR 0.84±0.08 0.77 [0.72,0.82] 0.23 @ 0.97
LR (SFS) 0.87±0.05 0.80 [0.75,0.86] 0.62 @ 0.81
CNN 0.84±0.06 0.72 [0.66,0.79] 0.55 @ 0.78
CNN (SFS)0.91±0.030.76 [0.71,0.82] 0.61 @ 0.80
MLP 0.88±0.040.82 [0.77,0.87]0.36 @ 0.94
MLP (SFS)0.91±0.060.79 [0.74,0.85] 0.71 @ 0.73
Uganda
Dev AUROC
South Africa Test
AUROC Spec @ Sens
LR 0.84±0.1 0.85 [0.79,0.91] 0.85 @ 0.71
LR (SFS) 0.86±0.08 0.84 [0.78,0.9] 0.66 @ 0.86
CNN 0.83±0.09 0.79 [0.72,0.86] 0.74 @ 0.77
CNN (SFS) 0.88±0.08 0.83 [0.77,0.89] 0.95 @ 0.39
MLP 0.89±0.060.86 [0.80,0.91]0.9 @ 0.68
MLP (SFS)0.91±0.070.84 [0.79,0.90] 0.8 @ 0.72
tecture. Previous work directly applied features selected by
a logistic regression model during SFS and then separately
optimised the ordering through repeated random shuffling the
input vector [15]. The strategy we propose here begins with
a vector of zeros, whose dimensionality is the full number
of input features. A single input feature is then inserted into
the first position in the vector, and the model is trained
and re-evaluated. This occurs in the inner cross-validation
loop, after which an average development set performance is
calculated. The same input feature is then moved to the second
position in the input vector, and the procedure is repeated. This
continues for all positions and for all input features, allowing
the best feature and its associated position in the vector to
be determined and fixed, based on the average development
set AUROC. This procedure is iterated, each time selecting
the next feature from the pool of yet unselected features and
its optimal position, until all positions in the vector have been
filled. Unlike previous applications which have applied either a
soft-reordering [21], or learn a 2D representation of the entire
feature set [17]–[20], our proposed greedy-approach identifies
a feature ordering and simultaneously identifies a subset of
features which are beneficial for classification.
V. RESULTS
Development and test set classifier performance in terms
of AUROC are presented for both countries in Table V.
The bottom half of the table presents the performance of
classifiers that were trained on the Ugandan sub-cohort and
tested on the South African sub-cohort without any fine-
tuning. Although trained and developed on data solely from
Uganda, the performance of the classifiers presented here does
not degrade on the held-out South African data compared to
previous work, which reported a mean test set AUROC of 0.83
1 5 10 15 20 25 30 35
Feature vector dimensionality
0.80
0.81
0.82
0.83
0.84
0.85
0.86
0.87
0.88
0.89
0.90
0.91AUROC
Development on South Africa
CNN
LR
MLP
1 5 10 15 20 25 30 35
Feature vector dimensionality
0.80
0.81
0.82
0.83
0.84
0.85
0.86
0.87
0.88
0.89
0.90
0.91AUROC
Development on Uganda
CNN
LR
MLP
Fig. 2: Average development set AUROC for each of the
three considered architectures (LR: Logistic regression, MLP:
Multi-layer perceptron, CNN: Convolutional neural network)
during sequential feature selection (SFS) for the South African
cohort (top) and Ugandan cohort (bottom). Horizontal axis
denotes the dimensionality of the feature vector.
with a 95% confidence interval of [0.79, 0.87] using fully-
nested cross-validation [15].
On average the South African test AUROC appears slightly
higher than for Uganda, but for the MLP after feature se-
lection, which represents the model which achieved the best
development set performance for both cohorts, the difference
is only 5% absolute and the confidence intervals overlap,
although the populations in each are distinct. This is important
because, when datasets are limited such as in the scenario we
consider, neural classifiers often do not generalise well to data
from a different domain.
Figure 2 presents the development set AUROCs for the
cross-cohort SFS results for each of the three models. The
application of feature selection improves development set
performance for both countries. The joint greedy optimisation
of the selected features and their position (Section IV-F) for the
CNN model appears to be effective, improving development
set performance by 7% and 5% on the South African and
Ugandan sub-cohorts respectively. In addition, when con-
sidering the held-out test data, consistent improvements (of
approximately 4%) are seen for the CNN, while for LR and
MLP the application of SFS achieves mixed results.
The best development set performance is consistently
achieved by the MLP after feature selection, achieving an
absolute AUROC of 0.91 for both cohorts, outperforming LR
by between 4-5% absolute in development set AUROC. Test

set performance, however, is similar to that achieved by the
much simpler LR model. Specifically, LR (SFS) outperforms
the MLP by 1% absolute in AUROC when testing on the
Ugandan sub-cohort while equal performance is achieved for
the South African sub-cohort. Therefore, for these cohorts,
the application of the simple logistic regression model appears
favourable. If the dataset could be enlarged, the deeper models
may show further potential.
In Figure 3 we show the average development set AUROC
achieved after 250 random permutations of the feature vector
ordering for the CNN. The distribution shows that the ordering
has a substantial impact on CNN classification performance,
with a total spread of approximately 9% absolute in AUROC.
For both countries, the proposed joint feature selection and
ordering optimisation algorithm identifies an ordering which
far surpasses the average performance of the random permuta-
tions. This pattern is even stronger when the feature ordering
is selected based on the results of SFS with LR. After selecting
the ordering which achieved the best average development
performance of the 250 variants, the random search yields an
AUROC of 0.87 and 0.86 for the South African and Ugandan
development sets respectively, trailing our proposed search
strategy by 4% and 2% absolute.
0.74 0.76 0.78 0.80 0.82 0.84
Development AUROC
0
5
10
15
20
25
30
35
40
45Count
Development on South Africa across 250 feature orderings
Average AUROC:  0.79 ± 0.02
Proposed feature ordering algorithm: 0.84
0.74 0.76 0.78 0.80 0.82 0.84
Development AUROC
0
5
10
15
20
25
30
35
40
45Count
Development on Uganda across 250 feature orderings
Average AUROC:  0.80 ± 0.01
Proposed feature ordering algorithm: 0.83
Fig. 3: Average development set AUROC over 250 CNN
retraining runs, each using a different random ordering of the
full input vector. Bins widths are 0.5%.
The optimal hyperparameters when utilising features se-
lected by SFS were presented in Table IV. For both co-
horts, the optimal MLP hyperparameters indicate that a small
two layer model is preferred, despite deeper networks being
searched. Again, it therefore appears that, given the small
size of the corpus, more regularised models such as logistic
regression remain a better choice.
A. Feature ordering
Given the variability across development and test set results
seen for the deeper models (CNN, MLP) we elect to inter-
rogate the features selected by SFS when used with logistic
regression. Figure 4 shows that for the South African cohort,
optimal performance is achieved when including just six of
the possible 28 features: CRP, anaemic conjunctivae, BMI,
haemoglobin concentration, age and fever. For the Ugandan
cohort, on the other hand, thirteen features are selected:
CRP, ART status, previous TB, years since previous TB dis-
ease, respiration rate, dyspnea, height, anaemic conjunctivae,
haemoglobin concentration, recent weight loss, age, night
sweats and fever. Among these, CRP, anaemic conjunctivae,
age, haemoglobin concentration, and fever occur in both sets.
Although CRP is always chosen first, and requires a point-
of-care tests, an additional≈4% improvement in AUROC is
achieved by leveraging the additional features, all of which
are easily obtainable through questionnaire, or simple mea-
surement. For both cohorts, neither knowledge of chronic
conditions nor of smoking habits had any positive impact on
TB classification.
B. WHO target product profile for TB screening
In 2025, the World Health Organization (WHO) released
an updated target product profile for TB screening tests which
recommended a minimum specificity of 60% at a sensitivity
of 90%. This tool could then form the first of a two-stage
screening process, where individuals positively identified in
the first are recommended for further testing in the second,
for example using microbiological tests or chest X-rays [2].
This strategy aims to minimise the number of people without
TB who are sent for expensive confirmatory testing.
Figure 5 presents the ROC curves for each of the classifiers,
both utilising all 28 features and those features identified by
SFS. If we consider the operating points determined on the
development sets which aim to satisfy the 90% sensitivity
requirements for the neural network classifiers (Section IV-C),
marked as⋆(SFS) and×(before SFS) in the figure, the
thresholds determined on the Ugandan development cohort
appear to produce performance with specificity well above
the minimum requirement at the expense of sensitivity on the
South African test set. The opposite appears to be true for the
classifiers developed on the South African data and evaluated
on the Ugandan sub-cohort. This highlights the challenge of
applying a developed neural network classifier to a held-out
setting, and may substantiate the need for network calibration
and potentially additional data collection from the target area
to determine a cohort specific threshold. This inconsistency is
seen for all classifiers except for LR after SFS.
The model which achieves the most consistent performance
across both cohorts is LR after applying SFS. This model
narrowly misses the WHO minimum specifications for a
screening tool by 4% in terms of sensitivity (86% sensitivity

81 82 83 84 85 86 87
Average development
set AUROC after inclusion of value
CRP concentration
Anaemic conjunctivae
BMI
Haemoglobin concentration
Age
Fever
Fagerstrom score
Sex
Middle upper arm circumference
Weight
Coughing up sputum
Height
Chest pain
HIV
Respiratory rate
Dyspnea
Cough duration
Heart rate
TBscoreII
T emperature
Other chronic conditions
Recent weight loss
Years since previous TB
Night sweats
Number of symptoms
ART
When did they stop smoking
Previous TB
(a) South African development set.
81 82 83 84 85 86 87
Average development
set AUROC after inclusion of value
CRP concentration
ART
Previous TB
Years since previous TB
Respiratory rate
Dyspnea
Height
Anaemic conjunctivae
Haemoglobin concentration
Recent weight loss
Age
Night sweats
Fever
Fagerstrom score
BMI
HIV
Cough duration
Other chronic conditions
Chest pain
TBscoreII
Number of symptoms
Coughing up sputum
Sex
Weight
T emperature
Heart rate
Middle upper arm circumference
When did they stop smoking (b) Ugandan development set.
Fig. 4: Average development set AUROC after including each variable during sequential feature selection for either the South
Africa (a) or Ugandan (b) cohorts.
at specificity 66%) when tested on the South African sub-
cohort, and by 9% in sensitivity (81% sensitivity at specificity
62%) when tested on the Ugandan sub-cohort. The minimum
specificity requirements are achieved for both the sub-cohorts.
Therefore, among the three considered architectures, LR shows
merit as a potential screening tool, producing values which are
consistently closer to the WHO minimum requirements.
VI. CONCLUSION
We have evaluated the effect of country domain shift on the
performance of neural network tuberculosis (TB) classification
based on clinical and demographic data. Experiments were
performed using two sub-cohorts of the CAGE-TB dataset,
collected in Uganda and South Africa respectively, which were
used to train three classifier architectures: logistic regression,
multilayer perceptron, and convolutional neural network.
Overall, the results show that such classifiers are robust
to the domain shift associated with a change in the country
from which the testing population is drawn. The simple
linear classifier (LR) was shown to achieve AUROCs of 0.8
[0.75,0.86] and 0.84 [0.78,0.9] when testing on the held-out
Ugandan and South African data respectively. The same model
afforded the most consistent performance when evaluated at
an operating point determined on the development set to
achieve 90% sensitivity, achieving test set sensitivity of 0.81
and specificity of 0.62 for Uganda and a sensitivity of 0.86
and specificity of 0.66 for South Africa. This narrowly misses
the WHO minimum requirements by 4-9% in sensitivity even
though the network is being evaluated on a completely held-
out cohort.
Our investigation represents the first report of an evaluation
of such classifiers across different countries, and indicates that
TB triage and screening based on the automatic classification
of clinical and demographic data is potentially viable. Future
work will include the verification of these first results using
larger and more varied cohorts whose heterogeneity may
further validate the techniques applied here.
VII. ETHICS ANDDATAAVAILABILITY
This study is approved by the Health Research Ethics
Committee of Stellenbosch University (M21/10/022), City of
Cape Town (9517), and Western Cape Department of Health
(WC 202203 035).
VIII. ACKNOWLEDGEMENTS
We acknowledge funding from the EDCTP2 program sup-
ported by the European Union (RIA2020I-3305, CAGE-TB).
This project is also supported by Global Health EDCTP3
and its members (101145817, 4-CAGE-TB). We gratefully
acknowledge financial support from Telkom (South Africa) for
the research presented in this paper. Computations were per-
formed using the University of Stellenbosch’s HPC1 (Rhasat-
sha).

0.0 0.2 0.4 0.6 0.8 1.0
0.0
0.2
0.4
0.6
0.8
1.0
Uganda T est
LR OP
LR (0.77)
LR SFS OP
LR SFS (0.80)
WHO Criterion
0.0 0.2 0.4 0.6 0.8 1.0
0.0
0.2
0.4
0.6
0.8
1.0
South Africa T est
LR OP
LR (0.85)
LR SFS OP
LR SFS (0.84)
WHO Criterion
0.0 0.2 0.4 0.6 0.8 1.0
0.0
0.2
0.4
0.6
0.8
1.0
MLP OP
MLP (0.82)
MLP SFS OP
MLP SFS (0.79)
WHO Criterion
0.0 0.2 0.4 0.6 0.8 1.0
0.0
0.2
0.4
0.6
0.8
1.0
MLP OP
MLP (0.86)
MLP SFS OP
MLP SFS (0.84)
WHO Criterion
0.0 0.2 0.4 0.6 0.8 1.0
0.0
0.2
0.4
0.6
0.8
1.0
CNN OP
CNN (0.72)
CNN SFS OP
CNN SFS (0.76)
WHO Criterion
0.0 0.2 0.4 0.6 0.8 1.0
0.0
0.2
0.4
0.6
0.8
1.0
CNN OP
CNN (0.79)
CNN SFS OP
CNN SFS (0.83)
WHO Criterion
Fig. 5: Neural network cross-cohort performance. Models are
trained and thresholds determined on one cohort and tested
on the held-out cohort. Stars (⋆) and crosses (×) represent
classifier operating points with and without SFS respectively
after optimising the threshold on the development set to
obtain 90% sensitivity. Plus (+) represents the minimum WHO
requirements for a screening test. OP: Operating point.
ORCID
Joshua M. Jansen van V ¨uren
 orcid.org/0000-0002-3406-4788
Devendra S. Parihar
 orcid.org/0000-0001-6404-6428
Daphne Naidoo
 orcid.org/0000-0001-7711-9526
Marisa Klopper
 orcid.org/0000-0002-9318-8289
Frank Cobelens
 orcid.org/0000-0002-4367-1133
Lutz Kolbe
 orcid.org/0000-0003-4852-0040
Kimsey Zajac
 orcid.org/0009-0005-0385-185X
Willy Ssengooba
 orcid.org/0000-0002-1643-110X
Moses Joloba
 orcid.org/0000-0002-0334-9983
Grant Theron
 orcid.org/0000-0002-9216-2415
Thomas R. Niesler
 orcid.org/0000-0002-7341-1017
REFERENCES
[1] World Health Organization, “Global tuberculosis report 2025,” World
Health Organization, Tech. Rep., 2025. [Online]. Available: https://www.
who.int/teams/global-programme-on-tuberculosis-and-lung-health/
tb-reports/global-tuberculosis-report-2025
[2] ——, “Target product profiles for tuberculosis screening tests,”
World Health Organization, Tech. Rep., 2025. [Online]. Available:
https://www.who.int/publications/i/item/9789240113572
[3] D. Jaganath, S. K. Sieberts, M. Raberahona, S. Huddart, L. Omberg,
R. Rakotoarivelo, I. Lyimo, O. Lweno, D. J. Christopher, N. V . Nhung,
W. Worodria, C. Yu, J.-Y . Chen, S.-H. Chen, T.-M. Chen, C.-H. Huang,
K.-L. Huang, F. Mulier, D. Rafter, E. S. C. Shih, Y . Tsao, H.-K.
Wang, C.-H. Wu, C. Bachman, S. Burkot, P. Dewan, S. Kulhare, P. M.
Small, V . Yadav, S. Grandjean Lapierre, G. Theron, A. Cattamanchi,
and o. b. o. the Cough Diagnostic Algorithm for Tuberculosis
(CODA TB) DREAM Challenge Consortium, “Accelerating cough-
based algorithms for pulmonary tuberculosis screening: Results
from the CODA TB DREAM challenge,”Open Forum Infectious
Diseases, vol. 12, no. 10, p. ofaf572, 10 2025. [Online]. Available:
https://doi.org/10.1093/ofid/ofaf572
[4] A. D. Orjuela-Ca ˜n´on, A. F. Romero-G ´omez, A. L. Jutinico, C. E.
Awad, E. Vergara, and M. A. Palencia, “Data fusion of medical records
and clinical data to enhance tuberculosis diagnosis in resource-limited
settings,”Appl. Sci. (Basel), vol. 15, no. 10, p. 5423, May 2025.
[5] G. P. Kafentzis, S. Tetsing, J. Brew, L. Jover, M. Galvosas, C. Chaccour,
and P. M. Small, “Predicting tuberculosis from real-world cough audio
recordings and metadata,”arXiv preprint arXiv:2307.04842, 2023.
[6] M. Ruperez, K. Shanaube, L. Mureithi, C. Wapamesa, J. M. Burnett,
B. Kosloff, P. de Haas, R. Hayes, S. Fidler, T. Gachie, A. Schaap,
S. Floyd, E. Klinkenberg, H. Ayles, A. Africa, M. Amofa-Skeyi,
V . Bond, M. Cheeba, P. Dodd, N. Kalisvaart, B. Kangololo, N. Kasese,
T. Mainga, A. Mwinga, V . Nikolayevskyy, B. Nyondo, R. Paulsen,
M. Simwinga, C. Sisam, L. Telisinghe, R. Thomas, R. Vermaak, and
F. Vijn, “Use of point-of-care C-reactive protein testing for screening
of tuberculosis in the community in high-burden settings: a prospective,
cross-sectional study in Zambia and South Africa,”The Lancet Global
Health, vol. 11, no. 5, pp. e704–e714, May 2023. [Online]. Available:
https://doi.org/10.1016/S2214-109X(23)00113-4
[7] S. R. Cox, K. C. Erisa, P. J. Kitonsa, A. Nalutaaya, M. Nantale,
F. Kayondo, J. Mukiibi, M. Mukiibi, O. Nakasolya, D. W. Dowdy,
A. Katamba, and E. A. Kendall, “Accuracy of C-Reactive protein for
tuberculosis detection in general-population screening and ambulatory-
care triage in Uganda,”Ann Am Thorac Soc, vol. 21, no. 6, pp. 875–883,
Jun. 2024.
[8] C. J. Calderwood, B. W. Reeve, T. Mann, Z. Palmer, G. Nyawo,
H. Mishra, G. Ndlangalavu, I. Abubakar, M. Noursadeghi, G. Theron,
and R. K. Gupta, “Clinical utility of C-reactive protein-based triage for
presumptive pulmonary tuberculosis in South African adults,”J Infect,
vol. 86, no. 1, pp. 24–32, Nov. 2022.
[9] B. Derendinger, T. K. Mochizuki, D. Marcelo, D. Shankar, W. Mangeni,
H. Nguyen, S. Yerikaya, W. Worodria, C. Yu, N. V . Nguyen, D. J.
Christopher, G. Theron, P. P. J. Phillips, P. Nahid, C. M. Denkinger,
A. Cattamanchi, and C. Yoon, “C-reactive protein-based screening
of people with tuberculosis symptoms: A diagnostic accuracy study,”
American Journal of Respiratory and Critical Care Medicine, vol. 211,
no. 3, pp. 499–506, 2025.
[10] Y . Baik, H. M. Rickman, C. F. Hanrahan, L. Mmolawa, P. J. Kitonsa,
T. Sewelana, A. Nalutaaya, E. A. Kendall, L. Lebina, N. Martinson,
A. Katamba, and D. W. Dowdy, “A clinical score for identifying active
tuberculosis while awaiting microbiological results: Development and
validation of a multivariable prediction model in sub-Saharan Africa,”
PLOS Medicine, vol. 17, no. 11, pp. 1–23, 11 2020. [Online]. Available:
https://doi.org/10.1371/journal.pmed.1003420
[11] L. Bartl, M. Zeeb, M. K ¨alin, T. Loosli, J. Notter, H. Furrer, M. Hoff-
mann, H. H. Hirsch, R. Zangerle, K. Grabmeier-Pfistershammer,
M. Knappik, A. Calmy, J. D. Fernandez, N. D. Labhardt, E. Bernasconi,
H. F. G ¨unthard, R. D. Kouyos, K. Kusejko, and J. Nemeth, “Machine
learning-based prediction of active tuberculosis in people with HIV using
clinical data,”Clin. Infect. Dis., Mar. 2025.
[12] G. Botha, G. Theron, R. Warren, M. Klopper, K. Dheda, P. Van Helden,
and T. Niesler, “Detection of tuberculosis by automatic cough sound
analysis,”Physiological Measurement, vol. 39, no. 4, p. 045005, 2018.

[13] M. Ghermi, M. Messedi, C. Adida, K. Belarbi, M. E. A. Djazouli, Z. I.
Berrazeg, M. Kallel Sellami, Y . Ghezini, and M. Louati, “TubIAgno-
sis: A machine learning-based web application for active tuberculosis
diagnosis using complete blood count data,”Digit. Health, vol. 10, p.
20552076241278211, Jan. 2024.
[14] A. J. Zimmer, P. Espinoza-Lopez, V . Ravi, S. K. Sieberts,
S. Abbasgholizadeh Rahimi, M. Pai, C. Ugarte-Gil, and
S. Grandjean Lapierre, “External validation of cough-based algorithms
for pulmonary tuberculosis screening from the coda tb dream challenge
using cough data from peru,”Scientific Reports, May 2026. [Online].
Available: https://doi.org/10.1038/s41598-026-50492-4
[15] D. S. Parihar, J. J. van V ¨uren, T. Niesler, G. Theron, D. Naidoo,
M. Klopper, F. Cobelens, L. Kolbe, K. Zajac, W. Ssengooba, and
M. Joloba, “Neural network-based identification of easily-obtainable
demographic and clinical characteristics to identify people with tuber-
culosis,”medRxiv, 2025.
[16] F. Rudolf, G. Lemvik, E. Abate, J. Verkuilen, T. Sch ¨on, V . F. Gomes,
J. Eugen-Olsen, L. Østergaard, and C. Wejse, “TBscore II: refining and
validating a simple clinical score for treatment monitoring of patients
with pulmonary tuberculosis,”Scand J Infect Dis, vol. 45, no. 11, pp.
825–836, Sep. 2013.
[17] Y . Zhu, T. Brettin, F. Xia, A. Partin, M. Shukla, H. Yoo, Y . A. Evrard,
J. H. Doroshow, and R. L. Stevens, “Converting tabular data into
images for deep learning with convolutional neural networks,”Scientific
Reports, vol. 11, no. 1, p. 11325, May 2021. [Online]. Available:
https://doi.org/10.1038/s41598-021-90923-y
[18] O. Bazgir, R. Zhang, S. R. Dhruba, R. Rahman, S. Ghosh, and
R. Pal, “Representation of features as images with neighborhood
dependencies for compatibility with convolutional neural networks,”
Nature Communications, vol. 11, no. 1, p. 4391, Sep 2020. [Online].
Available: https://doi.org/10.1038/s41467-020-18197-y
[19] A. Sharma, E. Vans, D. Shigemizu, K. A. Boroevich, and T. Tsunoda,
“DeepInsight: A methodology to transform a non-image data to
an image for convolution neural network architecture,”Scientific
Reports, vol. 9, no. 1, p. 11399, Aug 2019. [Online]. Available:
https://doi.org/10.1038/s41598-019-47765-6
[20] T. Matsuda, K. Uchida, S. Saito, and S. Shirakawa, “HACNet:
End-to-end learning of interpretable table-to-image converter and
convolutional neural network,”Knowledge-Based Systems, vol. 284,
p. 111293, 2024. [Online]. Available: https://www.sciencedirect.com/
science/article/pii/S0950705123010419
[21] H. Qian, P. Ma, S. Gao, and Y . Song, “Soft reordering one-dimensional
convolutional neural network for credit scoring,”Knowledge-Based
Systems, vol. 266, p. 110414, 2023. [Online]. Available: https:
//www.sciencedirect.com/science/article/pii/S0950705123001648
[22] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimiza-
tion,” inProceedings of the 3rd International Conference on Learning
Representations (ICLR), San Diego, USA, 2015.
[23] J. Ansel, E. Yang, H. He, N. Gimelshein, A. Jain, M. V oznesensky,
B. Bao, P. Bell, D. Berard, E. Burovski, G. Chauhan, A. Chourdia,
W. Constable, A. Desmaison, Z. DeVito, E. Ellison, W. Feng, J. Gong,
M. Gschwind, B. Hirsh, S. Huang, K. Kalambarkar, L. Kirsch,
M. Lazos, M. Lezcano, Y . Liang, J. Liang, Y . Lu, C. K. Luk,
B. Maher, Y . Pan, C. Puhrsch, M. Reso, M. Saroufim, M. Y .
Siraichi, H. Suk, S. Zhang, M. Suo, P. Tillet, X. Zhao, E. Wang,
K. Zhou, R. Zou, X. Wang, A. Mathews, W. Wen, G. Chanan,
P. Wu, and S. Chintala, “PyTorch 2: Faster machine learning through
dynamic python bytecode transformation and graph compilation,” in
Proceedings of the 29th ACM International Conference on Architectural
Support for Programming Languages and Operating Systems, Volume
2, New York, NY , USA, 2024, p. 929–947. [Online]. Available:
https://doi.org/10.1145/3620665.3640366
[24] E. R. DeLong, D. M. DeLong, and D. L. Clarke-Pearson, “Comparing
the areas under two or more correlated receiver operating characteristic
curves: A nonparametric approach,”Biometrics, vol. 44, no. 3, pp. 837–
845, 1988.
