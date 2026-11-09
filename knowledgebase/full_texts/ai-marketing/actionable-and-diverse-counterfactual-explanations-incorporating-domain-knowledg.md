---
title: Actionable and diverse counterfactual explanations incorporating domain knowledge and plausibility
  constraints
url: https://arxiv.org/abs/2511.20236
category: ai-marketing
subcategory: empirical
date: 2025-11
venue: ''
authors:
- Szymon Bobek
- Łukasz Bałec
- Grzegorz J. Nalepa
source: arxiv
pdf_url: https://arxiv.org/pdf/2511.20236
pages: 35
chars: 75827
fetched_at: '2026-11-08T13:13:49+00:00'
kb_version: 1
---

# Actionable and diverse counterfactual explanations incorporating domain knowledge and plausibility constraints

Actionable and diverse counterfactual explanations
incorporating domain knowledge and plausibility
constraints
Szymon Bobekszymon.bobek@uj.edu.pl 1, Łukasz Bałec
l.balec@cyberfolks.pl2,3, and Grzegorz J. Nalepa
grzegorz.j.nalepa@uj.edu.pl1
1Faculty of Physics, Astronomy and Applied Computer Science, Institute
of Applied Computer Science, Jagiellonian Human-Centered AI Lab
2cyber_Folks™, Krakow, Poland
3FreshMail Sp. z o.o., Krakow, Poland
May 26, 2026
Abstract
Counterfactual explanations improve the actionable interpretability of ma-
chine learning models by identifying minimal changes required to achieve
a desired outcome. However, existing methods often neglect dependencies
among features, which can lead to unrealistic or impractical modifications.
This limitation reduces the usefulness of counterfactual explanations in real-
world decision-support systems.
Motivated by applications in cybersecurity for email marketing, we pro-
pose DANCE (Diverse, Actionable, and Knowledge-Constrained Explana-
tions), a method for generating counterfactuals that incorporate feature de-
pendencies and domain constraints. DANCE models relationships between
features using linear and probabilistic structures that can be learned from data
or specified by experts. These dependencies are enforced during the search
process to improve plausibility and feasibility.
The method jointly optimizes plausibility, diversity, proximity, and spar-
sity within a unified objective. We evaluate DANCE on 140 datasets from
OpenML and demonstrate that it achieves competitive or superior perfor-
mance compared to existing approaches across multiple evaluation criteria.
Additionally, we validate the method in a real-world industrial setting in
collaboration with an email marketing platform, showing that it produces
domain-consistent and actionable recommendations.
This work has been submitted to the IEEE for possible publication. Copyright may be
transferred without notice, after which this version may no longer be accessible
arXiv:2511.20236v3  [cs.AI]  25 May 2026

1 Introduction
Explainable Artificial Intelligence (XAI) has gained substantial momentum in re-
cent years, attracting attention from both researchers and various business sectors,
including healthcare, heavy industry, and legal firms. Among various explanation
paradigms, counterfactual (CF) and contrastive explanations are often the most val-
ued by stakeholders such as end-users and domain experts [9, 24, 5] because they
give explicit examples of which features play the most influential role in AI mod-
els’ decisions and how their values should be changed in order to modify the overall
AI system output. However, CF explanations that conflict with established domain
knowledge or common sense are particularly problematic, as they fail to provide
actionable insights and reduce trust in the AI system. For example, a CF expla-
nation suggesting that reducing the risk of diabetes involves altering parameters
such as sex, age, and pregnancy status would be deemed impractical and irrele-
vant, given the well-established medical understanding of diabetes management
and common sense. Despite this, only a minority of existing methods for gener-
ating CFs consider plausibility explicitly and in a way that is auditable and allow
human modification. This issue has become one of the emerging challenges in the
XAI area, not only limited to counterfactual explanations [11], but most often in
practical implementation of XAI methods to different business cases.
Our work is on the one hand directly rooted in the very active area of basic CF
research in XAI (cf. Section 2), yet on the other hand is motivated by practical chal-
lenges in a specific domain, which is cybersecurity in online marketing (cf. Sec-
tion 3)1. In this case the ability to generate domain-informed, plausible counterfac-
tuals stands to substantially enhance the relevance and quality of email campaigns,
newsletters and communication with customers. A counterfactual should provide
actionable insights, suggesting specific alterations to a campaign (e.g., changing
the subject line length, adjusting the send time, or refining the image-to-text ratio)
to improve its perceived quality. However, the recommended modifications that do
not align with industry best practices, contradict known audience preferences, or
violate brand guidelines are unlikely to be adopted by practitioners, thus limiting
their practical utility.
In this work, we address this challenge by introducing DANCE (Diverse, Ac-
tionable, and Knowledge-Constrained Explanations), a method that explicitly mod-
1This work was supported in part by the Project "SendGuard—Improving the Security of Recipi-
ents Innovative Tool Based on Machine Learning Technology and Artificial Intelligence to Fight with
the Problem of Spam and Phishing in Marketing and Transactional E-Mail Messages" co-financed
from the Funds of European Regional Development Fund under Project POIR.01.01.01-00-0202/19-
02; The research has been supported by a grant from the Priority Research Area (DigiWorld) under
the Strategic Programme Excellence Initiative at Jagiellonian University.
2

els and enforces dependencies between features during counterfactual generation
(cf. Section 4). These dependencies can be learned from data using directed graph-
ical models or specified by domain experts. Importantly, we treat these structures
as plausibility constraints rather than universally valid causal models, allowing the
method to remain applicable across heterogeneous datasets.
DANCE integrates these constraints into a multi-objective optimization frame-
work that simultaneously accounts for correctness, proximity, sparsity, diversity,
and plausibility. The optimization is performed using a Tree-Structured Parzen Es-
timator, enabling efficient exploration of complex search spaces with conditional
dependencies.
We evaluate DANCE in two settings. First, we conduct a large-scale bench-
mark on 140 datasets from OpenML [4] to assess general performance across di-
verse domains (cf. Section 5). Second, we present a real-world case study in email
marketing, where plausible counterfactuals are essential for producing actionable
recommendations aligned with domain practices (cf. Section 7).
The results demonstrate that incorporating structured feature dependencies leads
to counterfactual explanations that are more realistic, interpretable, and useful in
practice.
2 Related works
The XAI research area has experienced a blooming period over the recent years,
which was driven both by the researchers who noticed the urgency of provid-
ing more control over the AI systems operation [29], as well as legal authorities
through the AI Act in EU [15], and DARPA challenge [12] in the USA. The full
spectrum of XAI methods is vast and has been extensively covered by several sur-
veys [17, 1, 3], to which we refer readers for a comprehensive overview of the
field. In this work, we focus specifically on counterfactual explanations, a distinct
subfield within XAI that provides example-based explanations [31].
In this type of XAI method, the explanations are presented to the user as exam-
ples of specific instances, which may be real or artificially generated. For tabular
data, the explanation takes the form of a row of feature values; in the case of image
data, it is an image; and for text data, it is a text snippet, etc. Counterfactual expla-
nations further ensure that the instance belongs to a contrasting class (potentially
defined by the user) relative to the instance being explained.
Other methods for example-based explanations include adversarial examples [3],
prototypes and critiques [21], and explanations based on prototypical parts [10],
among others. What distinguishes counterfactual explanations from these types is
that counterfactuals are expected to meet certain additional properties. The most
3

common properties are correctness, diversity, sparsity, proximity, and plausibil-
ity [17]. However, no existing methods optimize for all these properties simultane-
ously; instead, they typically focus on just a subset.
Furthermore, very few methods prioritize the plausibility of counterfactuals.
Those that do often use simple range-based constraints, which limit the ability
to capture more complex relational constraints - this is precisely where our work
focuses. Additionally, these methods typically do not permit expert interaction
with the constraints, thereby disabling domain-knowledge-based constraints and
relying solely on density-based and data-driven constraints to model plausibility. In
the following paragraphs, we provide a more in-depth analysis of existing methods
with respect to correctness, diversity, sparsity, proximity, and plausibility criteria.
Our focus is on methods that address plausibility in some form or are considered
significant milestones in the counterfactual generation landscape. A comparative
summary of these methods is provided in Table 1. For a comprehensive review of
all methods in the field, we refer the reader to [17].
One of the earliest counterfactual generation methods was Wachter [33]. It
used a simple approach that minimized a loss function composed of two terms:
one for the proximity of the counterfactual and the other for its correctness. This
basic loss function was optimized using the gradient-based algorithm. The Wachter
algorithm is often regarded as a baseline for other methods, as it was both the first
and one of the most straightforward approaches to counterfactual generation.
DCE [28] followed a similar idea as introduced in W ACH, but optimizing a
custom cost function that accounted for sparsity and proximity, but added com-
ponent responsible for keeping the counterfactual coherent. The authors defined
coherence as consistency with the underlying data structure, which was limited
to ensuring that the counterfactual generation method does not set all one-hot-
encoded features to either0or1. In this sense, we can consider this approach
as a minimal plausibility constraint. DCE was designed only to work with linear
models.
One of the most well-known methods in the area of CF is called Diverse Coun-
terfactual Explanations (DICE) [25]. It further extends the ideas of Wachter and
DCE by including additional terms in the loss function to ensure the broader spec-
trum of CF properties. It was designed to handle diversity, sparsity, and proximity
of counterfactual with a custom loss function that integrated all of the three criteria
in a form of losses and optimized with different forms of search algorithms such as
genetic algorithms, random search, gradient optimization. It utilized hinge loss to
decide on the correctness of the counterfactual. DICE does not directly account for
plausibility in the objective function but allows for predefined ranges of feature val-
ues, which can help prevent implausible counterfactuals, such as values outside the
possible scale or basic monotonicity constraints (e.g. age cannot decrease). A sim-
4

ilar approach to handling implausible feature values was proposed in MACE [20]
and CFNOW [13]. None of the aforementioned methods consider complex cases,
where the constraints are conditional, or in some kind of relation (e.g. linear) with
respect to each other.
Another group of methods approaches plausibility through representation learn-
ing. This includes algorithms such as CEM [14], EBCF [23], and CEGP [32], or
FRACE [36]. These methods rely on autoencoders to ensure that the reconstruction
loss of a newly generated sample (counterfactual candidate) is minimal, confirm-
ing that it is plausible—that is, that it belongs to the representation learned by the
autoencoder during training.
Finally, the last group of methods ensures the plausibility of newly generated
samples by positioning them in areas of high-density points or aligning them with
the underlying data distribution. This group can be further divided into endoge-
nous explainers, which provide explanations by selecting existing samples from
the given dataset (such as LUX [6], LORE [18]), and exogenous explainers, which
generate artificial samples such as DACE [19], OCEAN [27], or PPCF [35].
The motivation for our work, which stemmed from the visible gap in the land-
scape of state-of-the-art counterfactual explainers, was additionally backed by the
practical needs. A detailed description of the business motivation is given in the
following section.
3 Motivation grounded in practical use case from cyber-
security in email marketing
In the rapidly evolving digital landscape, Communication Platform as a Service
(CPaaS) providers have gained critical importance by enabling businesses to ef-
ficiently engage with their audiences through various communication channels.
Among these channels, email marketing remains a fundamental tool for customer
outreach, brand awareness, and relationship building. Modern CPaaS solutions of-
fer comprehensive platforms for creating, managing, and distributing large-scale
email campaigns. However, ensuring that these messages are both welcomed by
recipients and meet stringent quality standards poses a significant challenge. The
delicate balance between delivering valuable, personalized promotions and avoid-
ing unwanted or irrelevant content – colloquially known as spam – lies at the core
of the email marketing domain.
Furthermore, there is a growing trend in cybersecurity, to fight misinformation
in all possible channels. Thus, carefully engineering spam messages that could be
injected into a viable marketing campaign can cause an important security threat.
Although in the work described in this paper we consider content quality on a gen-
5

eral level, and do not address cybersecurity directly, the technology we developed
within theSendguardproject with Freshmail is in fact security-oriented [16]. The
broader R&D effort motivating this work aimed at developing AI-based techniques
to strengthen the security of company mail servers by protecting them from sending
spam or phishing messages. The project was co-financed by the Polish National
Centre for Research and Development (NCBiR) between 2020-2023
Freshmail offers its customers a diverse platform for email marketing. It is
most commonly used with so-called marketing campaigns that their customers de-
sign with their marketers. A campaign is first designed around a given topic, with
a number of factors regarding both content and its form identified and configured.
Furthermore, possible target groups of campaign recipients are identified. Using
such a configuration, and additional schedules based on expert knowledge (e.g.
when specific target groups tend to read their emails), large batches (tens or even
hundreds of thousands) of email messages are sent. Quality of messages is impor-
tant not only from marketing point of view, but also security. Should there be an
increased level of low quality messages sent, the company servers could be put on
blacklists by backbone Internet providers and effectively blocked from operation.
In this work, to quantify undesirability of email messages, we adopted an
engagement-centric metric: an extremely low email open rate (e.g., less than 2%)
suggests that recipients do not find value in the content. While straightforward in
principle, this approach surfaced deeper issues. The open rate alone could not fully
explain the complex interactions among countless features that influence campaign
performance. Factors such as subject line specificity, visual composition, send
time, and audience segmentation all interweave to determine how a campaign is
received.
This multifaceted nature of campaign data, enriched by detailed server logs,
event records, and behavioral analytics, made classification and prediction pro-
foundly challenging. Consequently, understanding why a model identified a cam-
paign as undesirable was nearly as difficult as classifying the campaign itself. This
realization underscored the necessity for the use of XAI methods. Introducing XAI
techniques enabled us to decipher the reasoning behind model predictions, illumi-
nating which features or interactions influenced the classification of a campaign
as spam-like. Such a transparency is instrumental in guiding both model refine-
ment and practical improvements to the campaigns themselves. Instead of simply
labeling a campaign as undesirable, explanations, such as counterfactuals, guide
marketers in transforming an ineffective campaign into one that engages and res-
onates with recipients.
While counterfactual explanations hold significant promise, existing genera-
tion methods are often limited by restrictive assumptions. Standard approaches
frequently overlook the complex joint distributions and dependencies present in
6

real-world datasets. In real world scenarios, unrealistic or impractical changes
proposed by counterfactuals limit their adoption and business value. From the
company perspective, the ability to generate domain-informed, plausible consis-
tent counterfactuals stands to substantially enhance the relevance and quality of
email marketing campaigns. Having this requirement as a practically grounded
motivation, our research highlights a path forward for integrating complex data-
driven models with domain expertise to produce results that are not only correct
in theory but also valuable in practice. More broadly, this work fits the growing
intersection of explainable AI and networked online systems, where model out-
puts translate into interventions that affect how information is delivered, perceived,
and acted upon at scale. In such settings (including email marketing and adjacent
platform pipelines such as recommendation, targeting, and moderation), explana-
tions must be not only diverse and close to the original instance, but also feasible
under structured dependencies among user, content, and context variables. Our
dependency-graph constraints can be viewed as a lightweight network-structured
prior over features, enabling counterfactual recourse that remains aligned with op-
erational rules and observed conditional regularities. This perspective connects
counterfactual explanation research with practical questions of trustworthy deci-
sion support in social systems, where transparency and actionability are prerequi-
sites for adoption and responsible use. This complements ongoing efforts to make
AI systems deployed in large-scale digital communication pipelines more transpar-
ent and practically trustworthy.
In the following sections, we detail the algorithmic foundations of our ap-
proach, followed by empirical evaluations validating its benefits, and the broader
implications for the future of AI-driven marketing communications and its security.
4 Method description
4.1 Background
DANCE allows us to learn the structure and magnitude of dependencies between
features used by the blackbox model in the form of linear or nonlinear constraints
on the feature values. This structure is then used to generate counterfactuals consis-
tent with it, and therefore more plausible and actionable. Alternatively, the struc-
ture and/or specific constraint values can be provided in advance by an expert if
they are knowna priori.
We are focusing on two types of relation between features: a linear relation
and possibly nonlinear conditional relations. As the CF by definition is an instance
that is produced by altering features values of the original instance, the relations
ensure that modifications are consistent with given relations. We employ a cus-
7

tom cost function to ensure not only plausibility, but also diversity and sparsity of
explanations given in equation below and employed Tree-structured Parzen Esti-
mator optimization algorithm to minimize it [34]. Figure 1 shows the cases that
our method handles.
x15 6
1
2
3
x2
Feature space that is not plausible, i.e. counterfacuals there are not valid nor actionable
Non plausible
counterfactual
Plausible and actionable counterfactual
Known, linear or conditional
 relationship between input features 4
42 31
Conditional relations
P(x2|x1,x3)
P(x4|x3)
P(x3|x1)
P(x1)
x1 x2
x3
x4
Linear relations
x1 x2
x3
x4
Figure 1: Illustration of inter-feature plausibility constraints targeted by DANCE.
A counterfactual that changes one variable in isolation may become infeasible
when other variables are structurally linked (linear dependencies), and conditional
constraints can exclude regions of the feature space (e.g., forbidden combinations).
DANCE incorporates such constraints via a directed relationship graph and penal-
izes violations during search.
The linear relation between features prevent the method from altering only
one feature value without changing the value of another one. The relation can be
provided in a form of directed acyclic graph, where nodes represent variables and
edges contain information about the linear relationship between them. This can
be used to describe linear relationships such as"Increasing the ambient pressure,
increases the temperature of boiling of a liquid".
Conditional dependencies allow one to model more complex constraints that
are non-linear, e.g. mark "forbidden" feature space areas. Similarly to the previous
type of constraints, this type is also defined by the directed acyclic graph, however,
the nodes contain conditional probability distribution of feature value given the
feature values of nodes from incoming edges. This in fact can be modeled in the
form of a Bayesian network and can handle relationships that are more complex
than simple linear constraints such as the aforementioned forbidden areas in the
8

feature space:"Given the person is a man, the probability of him being pregnant
equals 0".
The core of our approach was to design and optimize a loss function in a way
that will evenly value different properties of final set of counterfactuals such as
fidelity, proximity, sparsity, plausibility, and diversity. For the design of the loss
function, we build on the concepts introduced by Wachter and DICE, integrating
different properties as separate components of the function, as shown in Equa-
tion (1).
L=
Maximum of zero and difference between maximum probability of
desired classdversus other classes.
z }| {
max

0,max
c̸=d
( ˆPi,c − ˆPi,d)

+λ·

ωdLdiv +ω xLprox +ω sLspars +ω pLplaus

| {z }
Diversity, Proximity, Sparsity and Plausibility losses with weights.λis a
global weight.
(1)
Here,xdenotes the instance being explained,dis the desired class, andˆp c(x)
denotes the predicted probability of classcreturned by the black-box model. We
minimizeL, so each component is defined as a non-negative penalty. We scale
Ldiv, Lprox, Lspars, Lplaus to approximately[0,1]to make the weightsωeasier to
interpret, and we use equal weights (ω= 1) as a neutral default in the benchmark.
The first term ensures the correctness of the counterfactual by enforcing that
the predicted probability of the desired class exceeds that of all other classes. It is
formulated as a hinge loss that becomes zero once this condition is satisfied, guar-
anteeing the intended classification change. In Figure 1, this corresponds to moving
the query point across the decision boundary. However, simply crossing the bound-
ary is not enough to make a counterfactual useful. The second term determines
where the counterfactual is placed, ensuring it does not end up in an arbitrary region
but in a part of the feature space that makes it actionable. This is achieved through
a weighted combination of property-specific objectives—plausibility, proximity,
sparsity, and diversity—that must be carefully balanced. For example, a minimal
change that violates domain constraints may technically achieve the desired predic-
tion but remains unrealistic and therefore not actionable. Figure 1 illustrates why
plausibility is critical: counterfactuals should respect both conditional dependen-
cies (e.g.,P(x 2 |x 1, x3)andP(x 4 |x 3)) and linear relationships among features.
Ignoring these relationships can lead to invalid suggestions, such as feature com-
binations that cannot occur in practice. By jointly optimizing these properties, the
approach ensures that counterfactuals are not only effective in altering predictions
but also realistic, interpretable, and suitable for decision-making. All components
are scaled to comparable ranges to allow the use of uniform weights. This pro-
9

vides a neutral default configuration that can be adjusted in application-specific
scenarios.
In the following sections, we describe in-depth the design of particular loss
components and the process of search for optimal solution.
4.2 Plausibility
The plausibility in our approach is defined as a consistency of a newly generated
sample (counterfactual candidate) with the predefined relationships between fea-
ture values. This relationship can be given a priori by the expert (in which case
it may reflect underlying mechanisms) or can be discovered automatically from
the data. In the case of automatic graph discovery, we use the DirectLiNGAM
method [30] for linear relationship graph discovery. For conditional probability
graph learning we use again DirectLiNGAM, or alternatively NOTEARS [37] for
structure learning and estimate probability distribution with Bayesian parameter
estimation. In both cases, the relationships are represented in our approach as a
directed acyclic graph (DAG) as presented in Figure 2. From a practical point of
view, in the implementation of our method, the graph is represented as an adja-
cency matrix. In the following paragraphs, these two approaches are described in
more detail.
Discovery of relationships with graphWe employ DirectLiNGAM when a lin-
ear dependency model is a reasonable approximation and when interpretable edge
weights are required, as these can be directly incorporated as soft linear constraints
during optimization. As an alternative, NOTEARS provides a continuous opti-
mization framework for learning DAG structures; within our approach, it serves
the same purpose of estimating a directed dependency structure and is particularly
useful when the assumptions underlying DirectLiNGAM are not satisfied. Im-
portantly, in the large-scale benchmark setting, the learned graph is treated as a
structural plausibility model rather than a causal model, and we do not assume a
universally valid causal interpretation across heterogeneous datasets.
Expert constraints and conflicts.When expert-provided constraints are available,
we treat them ashardstructural edges (fixed directions and, if provided, coeffi-
cients) and learn only the remaining parts from data. If an expert rule conflicts
with data-driven structure, the expert rule takes precedence; contradictory learned
edges are removed. Optionally, constraints can be relaxed into soft penalties by
increasingL plaus for violations (future work).
DirectLiNGAM [30] assumes that the data is generated by a linear non-Gaussian
10

acyclic model (LiNGAM), defined as:
x=Bx+e(2)
wherex∈R d is the vector of observed variables,B∈R d×d is a strictly lower
triangular matrix encoding the directed structure, ande∈R d is a vector of in-
dependent, non-Gaussian noise terms. The method identifies variable ordering by
iteratively detecting exogenous variables - those independent of regression residu-
als. For each variablex j, residualsr (j) i are computed by regressing other variables
xi onx j, and independence is tested:
xj ⊥r (j) i ∀i̸=j(3)
The intuition behind this is that ifx j is truly exogenous, then any dependence
ofx i onx j must be due tox j’s influence onx i, not the reverse. This is because if
we regressx i onx j, the residualr (j) i captures the part ofx i that is not explained
byx j.
Ifx j is exogenous, then it should be statistically independent of the residuals
r(j) i , becausex j is not influenced by any other variable and the residuals represent
influences from other variables or noise, which are independent ofx j .
Therefore, if the variable is exogenous, i.e.x j =e j it becomes the parent node
in the graph. Once the ordering is established, the matrixBis estimated via least
squares regression. TheBrepresent the linear relationship graph. For instance,
in Figure 2 the relationship for well known Wine dataset [2] was presented which
was calculated with the described method. As discussed earlier, theBis strictly
lower triangular, therefore no cycles are observed in the graph, and the non-zero
elements at the intersection of rows and columns indicate the weight of the edge
(the relation between features) depicted in the graph.
Conditional Probability Distribution EstimationOnce the directed structure
is obtained using DirectLiNGAM or NOTEARS, we additionally allow to estimate
the conditional probability distributions (CPDs) for each node in the resulting di-
rected acyclic graph (DAG). If the observed variables are continuous, we first dis-
cretize them into a finite number of bins, transforming the data into categorical
form suitable for discrete probabilistic modeling.
We employ the Bayesian parameter estimation, which provides tools for learn-
ing CPDs from data given a fixed DAG structure. For each variableX i, the condi-
tional probability distributionP(X i |Pa(X i))is estimated using maximum like-
lihood estimation (MLE) or Bayesian estimation, wherePa(X i)denotes the set of
parent variables ofX i in the learned structure.
11

Each CPD is represented as a conditional probability table that specifies the
probability of each discrete stateX i =x i given all possible configurations of its
parent statesPa(X i) =xpa:
P(X i =x i |Pa(X i) =xpa) = N(X i =x i,Pa(X i) =xpa) N(Pa(X i) =xpa) ,
whereN(·)denotes the empirical count in the discretized dataset.
The resulting set of CPDs defines a fully parameterized Bayesian network con-
sistent with the discovered directed structure, enabling probabilistic inference and
sampling over the joint distribution of all variables. Compared to using the linear
coefficients from DirectLiNGAM, this discretized CPD approach has the advan-
tage of capturing potentially nonlinear or non-monotonic relationships between
each variable and its parents, since each parent configuration is associated with an
empirically estimated probability distribution rather than a fixed linear effect.
ﬁxed acidity
volatile acidity
0.21
citric acid
0.50
density
0.43
pH
-1.09
alcohol
-0.20
-0.43
residual sugar
-0.17
chlorides
-0.37
free sulfur dioxide
0.33
total sulfur dioxide
0.47
sulphates
-0.77
-0.41
0.61-0.27-0.481.82 1.37
-0.52
Figure 2: Relationship graph for a Wine dataset. The edges represent the magni-
tude in which change in the parent node values impact the children node values.
For instance increase in residual sugar decreases the alcohol in the wine and the
counterfactual that does not preserve this constrain is considered implausible and
not actionable.
Plausibility loss estimationGiven a relationship graphG= (V, E), we penal-
ize counterfactual candidates that violate constraints. We support two realizations
ofL plaus: Linear dependency mode and probabilistic mode. In linear dependency
12

mode, each node is reconstructed from its parents using learned edge weights, and
we compute a normalized mean squared reconstruction error. In probabilistic de-
pendency mode (used when conditional probability tables are available), we com-
pute a normalized negative log-likelihood under the learned/encoded CPDs, which
naturally handles discretized and categorical variables.
In linear mode, let cf i be thei-th feature value in the counterfactual candi-
date andPa(i)the parent set of nodeiinG. The reconstructed value isv i =P
p∈Pa(i) wp→i cfp. The plausibility penalty is defined in Equation 4 as the aver-
age mean squared error between the candidate and its reconstruction, normalized
by the number of features|V|.
Lplaus(cf, G) =1 |V| X i∈V  cfi −v i 2,
vi =
X
p∈Pa(i)
wp→i cfp.
(4)
In probabilistic mode, after discretization the CF instance, for each nodeiwe
estimate a CPDP(X i |Pa(X i)). We then defineLplaus as the average negative log-
likelihood of the candidate under these CPDs (optionally normalized), which yields
a bounded penalty and supports nonlinear, conditional constraints. The formula
is given in Equation 5, wherez i(cf)is the discretized value of featureiin the
candidate.
Lprob plaus(cf, G) =1 |V| X i∈V  −logP  Zi =z i(cf)

 ZPa(i) =z Pa(i)(cf)  .(5)
4.3 Proximity
Proximity encourages counterfactuals to stay close to the explained instance. We
use a weighted cosinedistanceon normalized features so that the term can be
minimized. Let˜xand ecf denote feature-wise normalized vectors (continuous fea-
tures scaled to[0,1]; categorical one-hot groups treated as blocks). The proximity
penalty is defined in Equation 6 as one minus the weighted cosine similarity, where
ωi are feature-specific weights (e.g., inverse median absolute deviation) that can be
tuned to adjust the importance of proximity for different features.
Lprox(cf, x) = 1−
PM
i=1 ωi ecfi ˜xiqPM
i=1 ωi ecf 2 i qPM i=1 ωi ˜x2 i .(6)
This quantity is close to0when vectors are aligned.
13

4.4 Sparsity
The sparsity measures how drastic is the modification of an original instance is
in order to transform it into counterfactual, which by the definition is theminimal
change in original feature. In practice, this is reduced to the number of features that
values’ were altered in CF compared to original instance, as shown in Equation 7.
Lspars(cf, x) =1 M MX i=1 I(cfi ̸=x i)(7)
Note, that the function is non-convex, hence it cannot be included in the loss
function if the optimization is gradient-based. However, but we use optimization
method that works with non-convex functions and allows us to include it in the
total loss.
4.5 Diversity
To encourage a set ofdistinctcounterfactuals, we follow the determinantal point
process (DPP) style objective used in [25]. We define a similarity kernel matrixK
over the already selected counterfactualsCF={cf (1), . . . ,cf(N) }and minimize
a bounded penalty as shown in Equation 8, wheredet(K)is the determinant of
Kand serves as a measure of diversity (higher determinant indicates more diverse
set).
Ldiv(CF) = 1−det(K).(8)
We use a kernel based on Euclidean distance in the normalized space:
Kij = 1
1 +∥ecf (i) − ecf (j) ∥2 +ϵ δij,
whereδ ij is the Kronecker delta andϵis a small constant (we use10 −6) that stabi-
lizes the determinant by ensuring numerical well-conditioning. With this construc-
tiondet(K)∈(0,1], soL div ∈[0,1).
All of the componentsL div, Lprox, Lspars, Lplaus described before are finally
added to the global loss function presented in Equation 1 and optimized with an
approach presented in the following section.
4.6 Counterfactual search
The process of search for counterfactuals can be divided into three stages that are
executed in the following order. The compact representation of this process is also
presented in Algorithm 1.
14

1. In the first stage, the relationship graph is created. It can be either generated
automatically in a data-driven manner or provided explicitly by the expert.
If the full graph is not known, only partial relationships can be defined.
2. In the second stage, data generation is performed to create a pool of coun-
terfactual candidates. The initial set of candidates is generated by sampling
from the provided dataset, or, if unavailable, by generative sampling from the
relationship graph. In the case of additive and linear models, data can also
be generated using information about feature contributions similar to [28]
and [19].
3. Finally, the loss function is optimized using a Tree-Structured Parzen Esti-
mator [34] which is a kind of Bayesian optimization approach that allows
for tree structure search spaces (i.e. spaces with possible conditional param-
eters).
Search space and initialization.The search space is defined per feature by (i) em-
pirical min–max ranges from the training data, (ii) optional expert-provided bounds
and immutability masks (features that must not change), and (iii) relationship-
graph-based feasibility filtering (linear or probabilistic mode). Initial candidates
X ′ are drawn from (a) observed samples (including nearest opposite-class samples
when available) and (b) ancestral sampling from the relationship graph when en-
abled. The Tree-structured Parzen Estimator then proposes candidate edits within
these bounds, and candidates that violate hard constraints are rejected while soft
violations are penalized byL plaus.
One of the most important parts of the method is the relationship graph that
captures directed dependencies between variables and represents linear or proba-
bilistic relationships between features’ values. Figure 2 presents a sample graph
trained on the well-known Wine dataset [2] which was selected solely for illustra-
tive purposes due to its simplicity and widespread familiarity, which help to clearly
demonstrate the underlying concepts. The structure and coefficients on the edges
were learned using DirectLiNGAM approach. As mentioned previously, the graph
paragraph can be obtained from experts (fully or only partially) or can be learned
automatically from the data. If the graph is provided by the expert, it does not
have to be complete, as the method automatically finds missing relationships from
the data. The graph is used in the plausibility loss component to ensure that the
counterfactual is aligned with it and does not contain feature values that are not
consistent with the background knowledge.
Additionally to relationship graph, we can narrow the search space with range-
based constraints, such that prevent certain variables from taking certain values
(i.e. values from outside of the domain, or forbidden values (e.g. age of a person
15

Algorithm 1DANCE Counterfactual search algorithm
1:Input:Blackbox ModelM; Training datasetX; Relationship graphG; De-
sired number of counterfactualsN; Weightsωfor the loss function from Equa-
tion (1); Desired classd
2:Output:ListCFofNcounterfactual examples
3:
4:Initialize result setCF←∅;
5:ifG=∅then
6:TrainGwithXand LiNGAM, or Bayesian parameter estimation
7:end if
8:fori∈1,2, . . . , Ndo
9:Create initial counterfactual candidatesX ′
10:X ′ ←samples fromXand generated withG
11:ifMis additive or linearthen
12:X ′ ←samples generated fromM
13:end if
14:Find counterfactualcf i ←arg mincfi L(M, cfi, CF, G, X′, d, ω)
15:Addcf i to the result setCF←{cf i} ∪CF
16:end for
17:Return:List of plausible, diverse, and sparse counterfactualsCF
lower than actual). Such constraints also allow us to mask features that should not
be modified at all by the algorithm.
Our method ensures diversity among counterfactuals, allowing the desired num-
ber of counterfactuals to be specified as output. Counterfactuals are generated
sequentially: in the first iteration, the best counterfactual is identified, and in sub-
sequent iterations, additional diverse counterfactuals are sought.
5 Quantitative evaluation
We compared our method with selected state-of-the-art approaches, focusing ex-
clusively on model-agnostic methods for which publicly available implementations
exist. In addition to the full version of our approach, we conducted an ablation
study in which the plausibility component was removed in order to assess its in-
fluence on the remaining criteria, such as diversity and sparsity. All experiments
were conducted on 140 datasets from the OpenML repository2 , using Explainable
Boosting Machines (EBM) [22] as the underlying classification model. We chose
2See:https://www.openml.org/.
16

EBM for its stable probabilistic outputs and availability across all datasets; how-
ever, the DANCE optimizer only queriesˆp c(·)and does not rely on gradients or
internal model structure, so it is model-agnostic by design. Due to the large num-
ber and heterogeneity of datasets considered, expert-defined relationship graphs
were not feasible; therefore, relationship graphs were automatically discovered
from data using DirectLiNGAM. Expert-validated graphs were used only in the
dedicated use-case scenario described later in the paper (Section 7). Unless stated
otherwise, all weightsωin Eq. 1 were set to 1.0. Because each loss component
is scaled to a comparable range, equal weights form a neutral default that avoids
ad-hoc tuning across 140 heterogeneous datasets. We discuss this choice and its
implications in Section 8. To guarantee a fair comparison, each evaluated method
was provided with exactly the same instances for counterfactual explanation and
was instructed to generate three diverse counterfactuals per instance. For methods
that do not natively support diversity, the explanation process was repeated three
times consecutively. All evaluation metrics were computed strictly according to
the definitions and equations presented in Section 4.1. Detailed quantitative results
for individual properties are reported in the appendices. The source code required
to reproduce all experiments is publicly available in our GitHub repository 3, and
precomputed metrics for all methods and datasets are provided as supplementary
material.
5.1 Analysis of the results
A summary of these results is shown in Figure 3. The plot presents the scores
obtained by each method across 140 datasets. The score is calculated as the area
under a spider plot (AUS) in a form of sum areas of triangles defined by the center
of the plot and neighborhood vertices. Each vertex representing the 1 Ri of a method, whereR i is the average ranking obtained from Friedman post-hoc statistical tests
for thei−thproperty of a given method. The formulas for this combined metric is
given in Equation (9). The closer a method’s score is to the maximum possible area
defined as N M2 2 sin  2π N  , the better its overall performance. TheMrepresents the
total number of methods tested.
AU S= 1 2 sin  2π N  NX i=1 1 RiRi+1 (9)
This evaluation method is adopted from [6], where the authors use it to illus-
trate multi-criteria evaluation results in scenarios where there is a known trade-off
between the metrics. The area can be affected by the order of vertices, hence it is
3See:https://anonymous.4open.science/r/xaibench-ACD8/.
17

recommended to put metrics that there is known trade-off between (e.g. precision
and recall) next to each other. In the plot, we includedprobabilitymetric showing
how confident the model predictions were for a given counterfactual. In our case,
all metrics are treated equally as the trade-off exists between all of them.
Fidelity
Probability
Proximity Loss
Sparsity Loss
Plausability Loss
Diversity
Execution Time
Fidelity
1
2
3
4
5
6
7
The larger the area the better
DANCE (122.49)
DICE (84.08)
LUX (68.74)
LORE (42.58)
CEM (32.67)
CEGP (58.81)
Wachter (33.52)
cfnow (68.24)
Figure 3: Combined evaluation metric visualized in a form of spiderplot. The
larger the area, the better the method.
Additionally, we tested the statistical significance of the differences of our
method compared to the rest. We have conducted Friedman post-hoc test followed
by Nemenyi test and have proven that our method is significantly better than others
in plausibility and sparsity and probability metrics. In the remaining metrics, it
also achieved top scores, but the differences were not statistically significant. The
only metric that our method was not the best was diversity, where it lost to Wachter,
DICE and LORE. This is particularly remarkable because Wachter and LORE does
not inherently optimize counterfactuals for diversity. Instead, we simulated this by
running Wachter and LORE multiple times and collecting results from each run.
As a result, the observed diversity was primarily due to the stochastic nature of
counterfactual generation implemented within these methods. The critical distance
18

plots and statistical analysis of the tests are provided in 6.
6 Statistical tests for quantitative evaluation
With 8 algorithms and 140 datasets, we had 7 x 973 degrees of freedom, respec-
tively. This enabled us to establish that the critical distance for the post-hoc Ne-
menyi test, withF(7,973)andα= 0.05is 0.75 for all the subsequent cases.
Figure 4 shows that DANCE achieves the highest plausibility (Eq. 4) with sta-
tistically significant differences. Occasional inferior results to LUX stem from its
endogenous nature, selecting only existing (thus always plausible) instances.
2.5 3.0 3.5 4.0 4.5 5.0 5.5 6.0
DANCE (2.5)
LUX (3.6)
cfnow (4.1)
CEGP (4.2)
(6.1) CEM
(5.9) Wachter
(5.2) LORE
(4.3) Dice
Figure 4: Critical distance plot for plausibility loss.
Figure 5 presents the results DANCE achieved in terms of diversity metric
defined in Equation (8). It is notable that the results were comparable to LORE
and CEGP, but is statistically worse than Dice and Wachter. It can be observed
that the diversity comes with a trade off to plausibility, by comparing Figure 5 and
Figure 4. This is especially visible in case of Wachter, which took opposite places
for both of these metrics. In many cases assuring plausibility comes at a cost of
diversity, especially where there are strong relationships between variables, that
prevent diverse changes to their values.
3.0 3.5 4.0 4.5 5.0 5.5 6.0 6.5 7.0
Wachter (3)
Dice (3.4)
LORE (3.9)
DANCE (4.3)
(7) cfnow
(4.9) LUX
(4.9) CEM
(4.6) CEGP
Figure 5: Critical distance plot for diversity.
19

2.5 3.0 3.5 4.0 4.5 5.0 5.5 6.0
DANCE (2.6)
cfnow (3.3)
CEGP (3.9)
Dice (4)
(6.2) Wachter
(5.9) LORE
(5.8) CEM
(4.4) LUX
Figure 6: Critical distance plot for proximity loss.
Figure 6 shows the results of the proximity evaluation defined in Equation (6).
The DANCE obtained the best results along with CFNOW. Proximity correlates
with sparsity (Fig. 7, Eq. 7), with sparse methods achieving better proximity.
2 3 4 5 6
DANCE (2)
Dice (3.2)
cfnow (3.4)
CEGP (4.5)
(6.5) Wachter
(6.2) LORE
(5.1) CEM
(5) LUX
Figure 7: Critical distance plot for sparsity loss.
Figure 8 presents the results for the fidelity metric that measures ratio of cor-
rectly discovered counterfactuals (counterfactulas that indeed changed the predic-
tion of the model). A clearly visible two clusters of methods were formed here
with a significant gap between them.
3.0 3.5 4.0 4.5 5.0 5.5 6.0
DANCE (2.9)
Dice (3.5)
cfnow (3.6)
LUX (4.2)
(6) Wachter
(5.9) CEM
(5.7) LORE
(4.2) CEGP
Figure 8: Critical distance plot for fidelity.
Figure 9 shows the results obtained for the probability metric. It is highly cor-
related with fidelity, as it shows the probability of the counterfactual obtained from
the black-box model for a desired class. However, in this plot it can be seen that
20

although the fidelity metric was similar to several algorithms, in case of probability
metric, the DANCE stands out as the best one.
2.0 2.5 3.0 3.5 4.0 4.5 5.0 5.5 6.0
DANCE (1.8)
Dice (3.9)
LUX (4.3)
cfnow (4.3)
(5.8) CEM
(5.6) Wachter
(5.5) CEGP
(4.8) LORE
Figure 9: Critical distance plot for probability.
The evaluation of execution time was presented in Figure 10. The reported
execution time includes only the counterfactual search phase. The construction
of the relationship graph is treated as an offline preprocessing step and is therefore
excluded from runtime comparisons, as it can be reused across multiple explanation
queries.
2.5 3.0 3.5 4.0 4.5 5.0 5.5 6.0 6.5
DANCE (2.4)
LUX (3.1)
Dice (3.7)
cfnow (4.1)
(6.3) Wachter
(6.2) CEM
(5.1) CEGP
(5) LORE
Figure 10: Critical distance plot for execution time.
6.1 Ablation study
We restrict the ablation analysis to removing the plausibility component because
enforcing structured dependencies is the primary additional mechanism introduced
by DANCE; the remaining terms follow standard formulations used in prior work
and are included to provide a balanced objective.
In this study, we removed the plausibility objective from the total loss function
to observe how it affects the overall performance of other properties. In particular,
we aimed at finding if plausibility negatively affects other metrics, especially such
as diversity or sparsity. We tested these two models on the same set of datasets as
discussed in previous section.
21

The difference in performance of the model with plausibility turned on rela-
tive to the model, where we turned off the plausibility component, is presented
in Figure 11. The most noticeable difference is observed in plausibility, which
is approximately 20% higher for the model incorporating the plausibility compo-
nent. Conversely, the metrics visibly negatively impacted are diversity and sparsity.
Also, the probability of the predictions of the black-box model for generated coun-
terfactuals dropped by 10% in plausible model. The fidelity remains the same for
both solutions with small changes to proximity and execution time.
The reduction in sparsity and diversity arises from the method’s inherently con-
strained search space for counterfactuals, guided by the relationship graph. This
constraint leads to cascading modifications of dependent features within the graph,
thereby reducing sparsity. Similarly, the diversity is constrained by the relation-
ship graph, as there are areas of the feature space that cannot be explored without
a negative impact on plausibility.
Fidelity
Probability Proximity Sparsity Plausability Diversity
Execution time
Metric
30
20
10
0
10
20
Loss in perfromance (%)
Ablation study results
Figure 11: Decrease in performance with respect to different metrics of a model
with plausibility optimization turned on.
22

7 Evaluation in the business case study
In this section we present a case study of the practical usage of DANCE method
in real business case. The case study is a part of a Sendguard project carried out
in collaboration with Freshmail company that one of the main operating goals is
delivering tools that allow clients to design, manage, and send their own marketing
campaigns through CPaaS approach to guard their quality. Despite adhering to best
practices and maintaining a strong emphasis on quality and consent, or due to the
security challenges, the company mass distribution of emails frequently faces the
risk of being misclassified as spam.
The core challenge driving this study stems from the observation that some
clients of company’s CPaaS platform, despite developing ostensibly high-quality
email campaigns (e.g., regularly updated subscriber lists, thematically relevant and
appealing content), often achieve suboptimal user engagement rates. Analyzes
revealed that issues such as poorly constructed subject lines or suboptimal sending
times can overshadow otherwise robust campaign content. Consequently, these
campaigns frequently yield results similar to, or even worse than, campaigns of
objectively lower content quality (e.g., stale subscriber lists, purely promotional or
repetitive messages).
In light of this, our primary objective was to devise a mechanism that suggests
optimizations of selected campaign parameters, particularly those most visible to
recipients (e.g., subject line elements, sending hour) and most likely to affect open
and click rates. Rather than relying solely on heuristic guidelines, we sought a
data-driven approach that would integrate expert knowledge about email marketing
practices while respecting the intricate dependencies among features. In this case,
the counterfactuals delivered by DANCE are a solution to our case. The overall
idea of the system incorporating DANCE method is presented in Figure 12. In the
following sections we elaborate on the dataset we used and results obtained with
our approach.
7.1 Dataset description
In our study we used company’s own dataset spanning the period of 2019 to 2021.
Part of this dataset was made publicly available on the Zenodo platform [8]]. The
total number of analyzed campaigns exceeded one million, though for model build-
ing we utilized a stratified sample of 100,000 campaigns (66% for training, 33% for
testing). This sample captured a broad cross-section of sending behaviors, content
styles, and thematic tags. Importantly, the dataset does not include any personal
or sensitive information. By design, only the most influential high-level parame-
ters were retained, thereby ensuring broad applicability across different types of
23

SendGuard
DANCE
Bad quality Good Quality
What to change to improve
the quality of the campaign?
Historical data
New/Improved
marketing campaign
Create/Improve
Learn
Classify
Actionable
counterfactuals
Relationship graph
Marketer
Data-discovered
relationships
Figure 12: Workflow of the case study. The marketing campaign is processed
through the Sendguard system to assess its quality. If the campaign is deemed of
poor quality, the DANCE method generates counterfactual suggestions for poten-
tial modifications to enhance its possible open rate among addressees.
email campaigns. This not only avoids potential biases or discrimination in feature
selection but also makes the modeling approach scalable regardless of individual
subscriber histories or sensitive demographic data. Each campaign record was de-
scribed by the following primary features:
• Tag (e.g., Sport, Heavy-Industry, Events, Toys, etc.): Captures the general
content category.
• Sending Hour and Day of the Week: Indicate the temporal configuration of
the campaign.
• Content Composition: Includes the number of links, the number of images,
and a text-to-HTML ratio measure.
• Subject Line Properties: Subject length, presence of personalization tokens,
emotive language, or question marks.
The target variable identified whether a campaign was consideredbad quality
(0) orneutral/good quality(1). These classes were derived from aggregate open
rates, click rates, spam complaint rates, and unsubscribe rates, combined into a
weighted score. This approach allowed us to separate lower-performing campaigns
from those reaching acceptable or positive engagement benchmarks.
For the core predictive model, we employed the Explainable Boosting Machine
(EBM) from the InterpretML toolkit achieving the following evaluation metrics:
24

Accuracy: 0.6707, Recall: 0.6707, Precision: 0.6724, F1 Score: 0.6427, ROC
AUC: 0.7471. Our primary aim was not to maximize predictive accuracy at all
costs. Instead, we required a sufficiently robust classifier that could differentiate
between suboptimal and acceptable campaigns while remaining interpretable. The
ROC AUC of approximately 0.75 satisfied our baseline requirement for deploy-
ment and subsequent counterfactual analysis.
7.2 Relationship graph
A key premise of our method is that the optimal campaign parameters must re-
flect established best practices and domain-specific insights. For example, subject
lines containing numbers (e.g., "5 Ways to...") or percentages (e.g., "Save 20%")
often draw attention and bolster open rates. Conversely, overuse of emotional trig-
gers or special symbols can trigger spam filters or frustrate recipients. Similarly,
it is widely acknowledged that sending hours can significantly affect campaign
performance, as recipients in certain industries are more likely to engage with
emails during specific windows (e.g. early morning for B2B segments). Through
close collaboration with marketing experts, we formalized these observations as
a set of business rules governing how features such astitle_has_numbers,
title_has_emotions,title_has_emojis, andcampaign_sent_hour
should interplay. The business rules were then encoded in the relationship graph
used by the DANCE method and are depicted in Figure 13. Notably, the brand
context (B2B vs. B2C) and content category (tag) further modulate which strate-
gies are likely to resonate with different audiences. This expert knowledge pre-
vents the optimization process from suggesting unrealistic or domain-inconsistent
changes—thereby ensuring the feasibility and credibility of any recommended
modifications.
7.3 Counterfactual generation
To translate the above insights into actionable changes, we used DANCE that inte-
grates both the learned model (EBM) and expert-driven constraints. This prevents
suggestions that violate fundamental marketing principles or appear unrealistic in
real-world deployments. In keeping with our initial design premise - to optimize
only those parameters that recipients directly perceive before deciding whether
to open a message or mark it as spam – we deliberately excluded from the set
of optimizable features any that pertain explicitly to the content domain (tag) or
to the overall message composition features. The rationale behind this constraint
is twofold: first, thematic or domain-specific elements often require more sub-
stantial, brand-aligned revisions than simple parameter tweaks; second, altering
25

title_has_personalization
title_has_currencies
0.96
title_has_numbers
0.29
message_content_ratio_cluster
0.65
tag
-13.77
1.03 message_images_count
-0.10
message_links_count
0.02
title_has_percents
0.65 title_has_emojis
0.21
title_has_emotions
0.13
-0.74
title_ends_emotion
0.90
-0.93 0.63
campaign_sent_hour
-0.10
Figure 13: Relationship graph for the business case, created in collaboration in
domain experts from the marketing field.
deeper structural aspects of a campaign’s body (e.g., message layout, multimedia
elements) goes beyond the minimal, high-impact changes that our mechanism aims
to propose. In practice, the counterfactual generator identifies campaigns predicted
to bebad quality(0) and proposes minimal yet meaningful feature shifts-such as
modifying sending hour or introducing certain elements in the subject line-that
could alter the model’s prediction toneutral/good quality(1). It does so by:
1. Checking feasible ranges and valid combinations for each allowable feature
(e.g., limiting emotive punctuation in B2B contexts).
2. Prioritizing changes that are easiest to implement and most likely to improve
engagement (e.g., adjustingcampaign_sent_hourbefore attempting
more drastic subject line modifications).
3. Maintaining a record of which features were changed and by how much,
allowing marketers to evaluate both the acceptability and practical effort of
each proposed adjustment.
26

7.4 Results and discussion
We tested our approach on a holdout set of 5,000 campaigns initially classified as
bad quality. The counterfactual generator was able to propose at least one success-
ful modification (i.e., one that changed the predicted class toneutral/good quality)
for 3,248 samples, corresponding to 64.96% of this subset.
The sending hour (campaign_sent_hour) was by far the most common
parameter to change (4,455 times), suggesting that a poorly timed send can markedly
reduce engagement. The next most frequent changes involved the presence of emo-
jis, numbers, and percentages in the subject line.
Additionally, 4,351 of the generated counterfactuals required exactly one fea-
ture change, while 732 involved two features. Only 107 cases required three or
more modifications. These findings confirm that even relatively small tweaks – es-
pecially in timing – can often suffice to transition a campaign from low-performing
to adequate or better. The exemplary explanation of a sample campaign with do-
main expert comment regarding it was presented in Table 3.
In the illustrated example in Table 3, the DANCE mechanism proposed mod-
ifications to the subject line by removing percentages and emojis. This combi-
nation is commonly encountered in promotional campaigns within the "Cosmet-
ics and Beauty" domain, where messages often highlight discounts or special of-
fers. However, such content frequently receives a lukewarm reception and can
even be perceived negatively. Consequently, the recommended adjustment encour-
ages employing alternative content types rather than relying primarily on explicit
promotional cues. Moreover, the mechanism advised changing the dispatch time
from 11:00 AM to 8:00 AM. Empirical observations show that this audience seg-
ment is more inclined to engage with such content during morning inbox checks;
messages sent later in the workday are frequently deprioritized and overlooked as
lower-importance communications.
To further verify that domain constraints were respected, we grouped cam-
paigns by tag (B2B, B2C, Mixed) and examined the statistical distribution of pro-
posed feature values. Notably, the distribution ofcampaign_sent_hourin
post-optimization campaigns varied significantly across these segments, as indi-
cated by a chi-square test (χ 2 = 104.45, andp <0.000001), suggesting the
mechanism indeed adjusted sending times in ways consistent with the distinct pref-
erences of different audience groups. This alignment with established industry
practices underscores the value of incorporating domain expertise into the opti-
mization logic, rather than relying on purely data-driven heuristics.
27

8 Limitations
Several limitations affect interpretation. In the OpenML benchmark we learn a
directed relationship graph from observational data and use it as a structural con-
straint in counterfactual search. Because such graphs rely on strong assumptions
(e.g., linearity, non-Gaussian noise, and acyclicity for DirectLiNGAM) that may
not hold across heterogeneous datasets, results should be read as plausibility un-
der alearned plausibility model, not as universally valid causal directions. As
the learned graph is approximate, missing/spurious edges or wrong directions can
make constraints too permissive (admitting implausible counterfactuals) or too re-
strictive (rejecting valid ones), motivating expert review or partial specification in
high-stakes settings.
Graph construction can be costly and preprocessing-dependent. We treat it as
an offline, reusable step (optionally expert-provided), so reported runtime covers
only online search; end-to-end time is higher when graph learning is included. In
practice, the graph can be refreshed periodically (e.g., after drift) while keeping
online explanations lightweight.
Plausibility consistency is implemented via a linear parent-reconstruction penalty:
efficient and smooth, but potentially insufficient for nonlinear or context-specific
constraints. When conditional probability tables are available, the probabilistic
mode better supports discretized/categorical variables and nonlinear conditional
relations, but adds modeling choices (discretization, smoothing, CPD sparsity) that
affect calibration; a systematic comparison is beyond scope.
We use equal weights for scaled loss terms to avoid per-dataset tuning and
preserve comparability across 140 datasets; however, trade-offs among proxim-
ity, sparsity, diversity, and plausibility are application-dependent, and deployments
may re-weight terms, enforce selected constraints as hard rules, or use domain-
specific distance metrics.
9 Summary
This paper targets a practical bottleneck in counterfactual (CF) explanation: many
existing methods treat features as largely independent, which often produces CFs
that violate real-world dependencies and therefore appear unrealistic, impractical,
or misaligned with domain requirements (e.g., industry standards, audience prefer-
ences, or brand guidelines). Such CFs are difficult to act upon, limiting the useful-
ness of CF-based XAI in operational settings.
We propose DANCE, a dependency-aware CF generation method that explic-
itly models relationships between features and enforces them during CF search.
28

DANCE represents dependencies as linear or nonlinear constraints whose structure
and strength can be learned from data or specified (partially or fully) by domain
experts. By integrating these constraints into the generation process, DANCE pro-
motes CFs that better reflect feasible interventions and domain-consistent changes.
Methodologically, DANCE optimizes a composite objective designed to bal-
ance key CF qualities—including plausibility, sparsity, and diversity—and em-
ploys the Bayesian optimization technique to efficiently discover high-quality CF
sets. We evaluate DANCE in two complementary ways: (i) through a real business
use case in cybersecurity for online marketing, developed in collaboration with
Freshmail within the Sendguard project and deployed in security and marketing
operations, and (ii) through a large-scale benchmark on 140 OpenML datasets to
assess generality beyond the motivating application. Across these settings, the re-
sults demonstrate that making feature dependencies explicit is an effective step to-
ward CF explanations that are more actionable and better aligned with real-world
constraints in domains where feasible interventions matter, including healthcare
and industrial maintenance [26, 7].
References
[1] Adel Abusitta, Miles Q. Li, and Benjamin C.M. Fung. Survey on explainable
ai: Techniques, challenges and open issues.Expert Systems with Applica-
tions, 255:124710, 2024.
[2] Stefan Aeberhard and M. Forina. Wine. UCI Machine Learning Repository,
1992. DOI: https://doi.org/10.24432/C5PC7J.
[3] Hubert Baniecki and Przemyslaw Biecek. Adversarial attacks and de-
fenses in explainable artificial intelligence: A survey.Information Fusion,
107:102303, 2024.
[4] Bernd Bischl, Giuseppe Casalicchio, Taniya Das, Matthias Feurer, Sebas-
tian Fischer, Pieter Gijsbers, Subhaditya Mukherjee, Andreas C Müller, Lás-
zló Németh, Luis Oala, Lennart Purucker, Sahithya Ravi, Jan N van Rijn,
Prabhant Singh, Joaquin Vanschoren, Jos van der Velde, and Marcel Wever.
Openml: Insights from 10 years and more than a thousand papers.Patterns,
6(7):101317, 2025.
[5] Szymon Bobek, Paloma Koryci ´nska, Monika Krakowska, Maciej Mo-
zolewski, Dorota Rak, Magdalena Zych, Magdalena Wójcik, and Grzegorz J.
Nalepa. User-centric evaluation of explainability of ai with and for humans:
29

A comprehensive empirical study.International Journal of Human-Computer
Studies, 205:103625, 2025.
[6] Szymon Bobek and Grzegorz J. Nalepa. Local universal rule-based explainer
(lux), 2025.
[7] Szymon Bobek and Grzegorz J. Nalepa. Tsproto: Fusing deep feature extrac-
tion with interpretable glass-box surrogate model for explainable time-series
classification.Information Fusion, page 103357, 2025.
[8] Szymon Bobek, Grzegorz J. Nalepa, Sebastian Obara, Piotr Suszalski, and
Łukasz Bałec. Sendguard900k: Massive dataset for metadata-based quality
assurance of email marketing, 12 2025.
[9] Raphaela Butz, Renée Schulz, Arjen Hommersom, and Marko van Eekelen.
Investigating the understandability of xai methods for enhanced user experi-
ence: When bayesian network users became detectives.Artificial Intelligence
in Medicine, 134:102438, 2022.
[10] Chaofan Chen, Oscar Li, Chaofan Tao, Alina Jade Barnett, Jonathan Su, and
Cynthia Rudin. This looks like that: deep learning for interpretable image
recognition. InProceedings of the 33rd International Conference on Neural
Information Processing Systems, Red Hook, NY , USA, 2019. Curran Asso-
ciates Inc.
[11] Yu-Liang Chou, Catarina Moreira, Peter Bruza, Chun Ouyang, and Joaquim
Jorge. Counterfactuals and causability in explainable artificial intelligence:
Theory, algorithms, and applications.Information Fusion, 81:59–83, 2022.
[12] DARPA. Explainable Artificial Intelligence.
[13] Raphael Mazzine Barbosa de Oliveira, Kenneth Sörensen, and David
Martens. A model-agnostic and data-independent tabu search algorithm to
generate counterfactuals for tabular, image, and text data.European Journal
of Operational Research, 2023.
[14] Amit Dhurandhar, Tejaswini Pedapati, Avinash Balakrishnan, Pin-Yu Chen,
Karthikeyan Shanmugam, and Ruchir Puri. Model agnostic contrastive ex-
planations for structured data, 2019.
[15] EU. Proposal for a Regulation of the European Parliment and of the Council
Laying Down Harmonised Rules on Artificial Intelligence (Artificial Intelli-
gence Act) and Amending Certain Union Legislative Aacts, 2021.
30

[16] Wojciech Gałka, Jan G. Bazan, Urszula Bentkowska, Kamil Szwed, Marcin
Mrukowicz, Paweł Dryga ´s, Lech Zar˛ eba, Marcin Szpyrka, Piotr Suszalski,
and Sebastian Obara. Aggregation-based ensemble classifier versus neural
networks models for recognizing phishing attacks.IEEE Access, 13:48469–
48487, 2025.
[17] Riccardo Guidotti. Counterfactual explanations and how to find them: litera-
ture review and benchmarking.
[18] Riccardo Guidotti, Anna Monreale, Fosca Giannotti, Dino Pedreschi, Salva-
tore Ruggieri, and Franco Turini. Factual and counterfactual explanations for
black box decision making.IEEE Intelligent Systems, 34(6):14–23, 2019.
[19] Kentaro Kanamori, Takuya Takagi, Ken Kobayashi, and Hiroki Arimura.
Dace: Distribution-aware counterfactual explanation by mixed-integer linear
optimization. In Christian Bessiere, editor,Proceedings of the Twenty-Ninth
International Joint Conference on Artificial Intelligence, IJCAI-20, pages
2855–2862. International Joint Conferences on Artificial Intelligence Orga-
nization, 7 2020. Main track.
[20] Amir-Hossein Karimi, Gilles Barthe, Borja Balle, and Isabel Valera. Model-
agnostic counterfactual explanations for consequential decisions. In Sil-
via Chiappa and Roberto Calandra, editors,The 23rd International Confer-
ence on Artificial Intelligence and Statistics, AISTATS 2020, 26-28 August
2020, Online [Palermo, Sicily, Italy], volume 108 ofProceedings of Machine
Learning Research, pages 895–905. PMLR, 2020.
[21] Been Kim, Rajiv Khanna, and Oluwasanmi Koyejo. Examples are not
enough, learn to criticize! criticism for interpretability. InProceedings of the
30th International Conference on Neural Information Processing Systems,
NIPS’16, page 2288–2296, Red Hook, NY , USA, 2016. Curran Associates
Inc.
[22] Yin Lou, Rich Caruana, Johannes Gehrke, and Giles Hooker. Accurate intel-
ligible models with pairwise interactions. InProceedings of the 19th ACM
SIGKDD International Conference on Knowledge Discovery and Data Min-
ing, KDD ’13, page 623–631, New York, NY , USA, 2013. Association for
Computing Machinery.
[23] Divyat Mahajan, Chenhao Tan, and Amit Sharma. Preserving causal con-
straints in counterfactual explanations for machine learning classifiers, 2020.
31

[24] Tim Miller. Explanation in artificial intelligence: Insights from the social
sciences.Artificial Intelligence, 267:1–38, 2019.
[25] Ramaravind K. Mothilal, Amit Sharma, and Chenhao Tan. Explaining ma-
chine learning classifiers through diverse counterfactual explanations. In
Proceedings of the 2020 Conference on Fairness, Accountability, and Trans-
parency, FAT* ’20, page 607–617, New York, NY , USA, 2020. Association
for Computing Machinery.
[26] Maciej Mozolewski, Betül Bayrak, Kerstin Bach, and Grzegorz J. Nalepa.
From prototypes to sparse ecg explanations: Shap-driven counterfactuals for
multivariate time-series multi-class classification, 2025.
[27] Axel Parmentier and Thibaut Vidal. Optimal counterfactual explanations in
tree ensembles. In Marina Meila and Tong Zhang, editors,Proceedings of
the 38th International Conference on Machine Learning, volume 139 ofPro-
ceedings of Machine Learning Research, pages 8422–8431. PMLR, 18–24
Jul 2021.
[28] Chris Russell. Efficient search for diverse coherent explanations. InProceed-
ings of the Conference on Fairness, Accountability, and Transparency, FAT*
’19, page 20–28, New York, NY , USA, 2019. Association for Computing
Machinery.
[29] Stuart Russell.Artificial Intelligence and the Problem of Control, pages 19–
24. Springer International Publishing, Cham, 2022.
[30] Shohei Shimizu, Patrik O. Hoyer, Aapo Hyvärinen, and Antti Kerminen. A
linear non-gaussian acyclic model for causal discovery.J. Mach. Learn. Res.,
7:2003–2030, December 2006.
[31] Jasper van der Waa, Elisabeth Nieuwburg, Anita Cremers, and Mark Neer-
incx. Evaluating xai: A comparison of rule-based and example-based expla-
nations.Artificial Intelligence, 291:103404, 2021.
[32] Arnaud Van Looveren and Janis Klaise. Interpretable counterfactual expla-
nations guided by prototypes. In Nuria Oliver, Fernando Pérez-Cruz, Stefan
Kramer, Jesse Read, and Jose A. Lozano, editors,Machine Learning and
Knowledge Discovery in Databases. Research Track, pages 650–665, Cham,
2021. Springer International Publishing.
[33] Sandra Wachter, Brent D. Mittelstadt, and Chris Russell. Counterfactual
explanations without opening the black box: Automated decisions and the
GDPR.CoRR, abs/1711.00399, 2017.
32

[34] Shuhei Watanabe. Tree-structured parzen estimator: Understanding its algo-
rithm components and their roles for better empirical performance, 2023.
[35] Patryk Wielopolski, Oleksii Furman, Jerzy Stefanowski, and Maciej Zi˛ eba.
Probabilistically plausible counterfactual explanations with normalizing
flows, 2024.
[36] Yunxia Zhao. Fast real-time counterfactual explanations, 2020.
[37] Xun Zheng, Bryon Aragam, Pradeep Ravikumar, and Eric P. Xing. Dags with
no tears: continuous optimization for structure learning. InProceedings of the
32nd International Conference on Neural Information Processing Systems,
NIPS’18, page 9492–9503, Red Hook, NY , USA, 2018. Curran Associates
Inc.
33

Table 1: Comparison of representative counterfactual explanation methods.
Columns indicate whether a method explicitly optimizes a given property (Yes),
supports it indirectly (e.g., by repeated runs), or does not address it.Plausibility
summarizes the main mechanism used to encourage feasibility (bounds/constraints,
density, representation learning, or structured plausibility constraints).
Method Optimization
Mechanism
Diversity Sparsity Proximity Plausibility Model-
Agnosticism
Expert-
Based
Con-
straints
DICE [25] Various Yes Yes Yes Constraint-
based
Yes Range-
based
DCE [28] Linear program-
ming
Yes Yes Yes Minimal Linear models
only
No
CEM [14] FISTA optimizer No No Yes Autoencoder-
based
Yes Range-
based
EBCF [23] Gradient-based No No Yes Autoencoder
+ man-
ually
encoded
plausi-
bility
con-
straints
Yes Yes
DACE [19] CPLEX optimizer No No Yes Density-
based /
outlier-
based
Linear and
tree-based
No
MACE [20] SAT solvers Yes Yes Yes Constraint-
based
No Range-
based
OCEAN [27] Custom loss func-
tion
Not na-
tively
No Yes Density-
based /
outlier-
based
Only for tree
ensembles
Logical
and Lin-
ear
CEGP [32] FISTA + K-D Tree
search
No Yes Yes Autoencoder-
based
Yes No
PPCF [35] Gradient-based No No Yes Density-
based
Requires gra-
dients
No
LUX [6] Entropy and dis-
tance
Not na-
tively
No Yes Density-
based
Yes No
LORE [18] Entropy and dis-
tance
No No Yes Density-
based
Yes No
Wachter [33] Gradient-based No Yes Yes No Yes No
CFNOW [13] Tabu search No Yes Yes No Yes No
34

Table 2: Summary of results from quantitative evaluation. Values represent average
rank of the method over 140 datasets. The lower the better. The↑denotes winners
that were statistically significantly better the the rest.
DANCE Dice LUX LORE CEM CEGP Wachter cfnow
Fidelity2.863.54 4.16 5.74 5.89 4.21 5.98 3.61
Probability1.75↑3.87 4.31 4.83 5.81 5.47 5.62 4.34
Proximity Loss2.554.01 4.36 5.88 5.81 3.91 6.17 3.29
Sparsity Loss2.03↑3.21 5.03 6.19 5.12 4.54 6.48 3.40
Plausibility Loss2.54↑4.33 3.55 5.21 6.14 4.24 5.92 4.06
Diversity 4.34 3.44 4.92 3.92 4.88 4.572.966.97
Execution Time2.373.67 3.14 5.04 6.21 5.11 6.34 4.12
Total Wins60 0 0 0 0 1 0
Table 3: Comparison of feature values between sample campaign marked asbad
qualityand counterfactual generated with DANCE. Bold rows indicate values that
were changed by the mechanism.
Campaign feature Origin DANCE
title_has_numbers 1 1
title_has_personalization 0 0
title_has_percents 1 0
title_has_emotions 1 1
title_has_questions 0 0
title_has_quotes 0 0
title_has_emojis 1 0
title_has_currencies 0 0
title_has_brackets 0 0
title_ends_question 0 0
title_ends_emotion 1 1
campaign_sent_hour 11 8
campaign_sent_dayofweek 5 5
campaign_sent_day 28 28
tag Cosmetic, Beauty Cosmetic, Beauty
message_content_ratio_cluster 1 1
message_links_count 24.0 24.0
message_images_count 14.0 14.0
35
