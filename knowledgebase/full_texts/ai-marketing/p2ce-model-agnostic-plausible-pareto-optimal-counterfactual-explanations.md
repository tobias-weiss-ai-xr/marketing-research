---
title: 'P²CE: Model-Agnostic Plausible Pareto-Optimal Counterfactual Explanations'
url: https://arxiv.org/abs/2606.18418
category: ai-marketing
subcategory: measurement
date: 2026-06
venue: ''
authors:
- Arthur Hendricks Mendes de Oliveira
- Giovani Valdrighi
- Marcos Medeiros Raimundo
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.18418
pages: 19
chars: 47171
fetched_at: '2026-11-08T13:28:13+00:00'
kb_version: 1
---

# P²CE: Model-Agnostic Plausible Pareto-Optimal Counterfactual Explanations

P2CE: Model-Agnostic Plausible Pareto-Optimal
Counterfactual Explanations
Arthur Hendricks Mendes de Oliveira 1†, Giovani Valdrighi 1*†,
Marcos Medeiros Raimundo1
1Instituto de Computa¸ c˜ ao, Universidade Estadual de Campinas, Albert
Einstein Avenue, Campinas, 13083-889, S˜ ao Paulo, Brazil.
*Corresponding author(s). E-mail(s): giovani.valdrighi@ic.unicamp.br;
Contributing authors: a217048@dac.unicamp.br;
mraimundo@ic.unicamp.br;
†These authors contributed equally to this work.
Abstract
The increasing use of machine learning algorithms in social applications has
raised concerns about fairness and transparency, leading to the development
of counterfactual explanations. These explanations supports individuals to
understand and potentially alter unfavorable decisions in areas such as loan
applications, job selections, and more, by providing actionable changes to input
features that would lead to a desired outcome. Existing methods often struggle
to balance feasibility, plausibility, and computational efficiency. To address this,
we introduce P2CE, an algorithm for generating plausible Pareto-optimal coun-
terfactual explanations, offering users a diverse set of optimal trade-offs between
different notions of feasibility. P2CE employs an auxiliary isolation forest outlier
detector to ensure that explanations are in accordance with the data distribu-
tion and leverages SHAP values to obtain optimal results with short computing
times, regardless of the underlying model. Our algorithm was empirically eval-
uated on three datasets, demonstrating superior performance in terms of both
solution quality and computational efficiency compared to related techniques.
Keywords:Counterfactual Explanations, Multi-objective, Outlier Detection
This is a pre-peer review, pre-print version of this article.
1
arXiv:2606.18418v1  [cs.LG]  16 Jun 2026

1 Introduction
Machine learning algorithms are now present daily in the lives of individuals in many
small and hidden decisions. However, these algorithms are also being used for deci-
sions with a high impact on individuals, such as credit scoring, selection processes,
health diagnosis, and others. In these contexts, supporting individuals in obtaining
the desired prediction is important: “My request was denied; what should I do next
to have an accepted loan?” . Furthermore, regulations in diverse countries already ask
for explanations on predictions, such as the EU General Data Protection Regulation
(GDPR). Counterfactual explanations were proposed to answer such concerns [1],
defined as changes in feature values necessary to obtain the desired prediction. The
main objective of such explanations is to be truthful for the model’s decision-making
and to beactionable[2]. Counterfactual explanations should befeasible—suggested
changes are achievable by the particular individual — and should beplausible—
they are probable observations within the data distribution.
Given an observationx, counterfactual explanations can be expressed as a vec-
torx+awherearepresents the changes suggested for each feature. Previous works
have been developed in this context, and different methods for measuring the feasi-
bility of suggested changesahave been discussed [3]. First, suggested changes should
be small, as larger changes in features cannot be reachable for an individual (sug-
gesting a ten-fold increase in income is not a useful counterfactual explanation, for
example). Secondly, they should be sparse, suggesting changes in only a subset of
features. This is motivated because a larger number of small changes may be worse
compared to a moderate change on a smaller number of features. Furthermore, due to
the subjective preference of individuals, no single measure of feasibility can be used
for all scenarios. By providing multiple diverse solutions, different personal prefer-
ences can be supported. Previous works considered working with multiple objectives
by defining a weighted loss [4] or employing multi-objective optimization to obtain a
Pareto-optimal set of solutions [5].
0.0 0.2 0.4 0.6 0.8 1.0
x1
0.0
0.2
0.4
0.6
0.8
1.0x2
Data Distribution
Outlier
Inlier
0.0 0.2 0.4 0.6 0.8 1.0
x1
0.0
0.2
0.4
0.6
0.8
1.0x2
Classifier and Counterfactual Explanations (CX)
f(x)
f(x) <
Individual
Closest CX
Inlier CX
Fig. 1Toy example with a dataset of two features. On the left, we estimated the distribution using
KDE. On the right, two algorithms generate one counterfactual explanation for the reference point
in black. While the triangle explanation is close, it is outside the data distribution. The square point
is the closest point inside the data distribution, it is feasible and plausible.
2

However, when maximizing feasibility, algorithms might present solutions that are
not likely to be based on the data distribution. In Fig. 1, we present an example of
counterfactual explanations with two features and Euclidean distance as a measure of
feasibility. In this example, while the triangular solution might be closer in Euclidean
distance to the reference sample (black dot), this solution is not inside the data dis-
tribution. The square solution, on the other hand, might be more distant from the
reference sample; however, it ensures plausibility. In this simple example, the triangle
solution was obtained by MAPOCAM [5], while the triangle algorithm is our solu-
tion. Previous algorithms have already been presented to ensure the plausibility of
counterfactual explanations [6, 7]. However, they did not consider the importance of
optimality regarding the multiple objectives.
Counterfactual explanation algorithms are also heavily dependent on the model
considered. Depending on the complexity of the model, optimal counterfactual
explanations might be challenging to obtain. Initial works presented solutions for
differentiable and linear models, with more recent approaches being model-agnostic,
considering that the model is a black box where only the predictions are known.
Although these proposals may not achieve optimal efficiency across all models in
computing cost, they are easily integrated into real-world applications.
We present P2CE, an algorithm designed to generatePlausiblePareto-optimal
CounterfactualExplanations. P2CE draws upon the previous work MAPOCAM but
further improves the algorithm to ensure the plausibility of counterfactual explana-
tions. The algorithm also addresses the limitations of prior research by enabling the
generation of counterfactual explanations applicable to any model. Our proposal is
based on a branch-and-bound search in a grid of possible counterfactual explanations.
Still, it leverages outlier detection and SHAP values to avoid searching regions with-
out useful solutions. This procedure can be done considering multiple objectives which
commonly arise in the context of counterfactual explanations. P2CE obtains Pareto-
optimal solutions; thus, no other solution in the space of counterfactual explanations
would have costs lower or equal in all of the objectives. In summary, our contributions
are as follows:
• P2CE: A novel algorithm model-agnostic for the generation of optimal counterfac-
tual explanations under multi-objectives that ensures that explanations are within
the data distribution.
• The exploration of an unexplored SHAP’s property that allows us to foresee if a set
of variables can achieve a counterfactual. Thus expanding the agnostic capability
of counterfactual explanations.
• An extensive evaluation of the proposed algorithm with multiple datasets and clas-
sifiers, compared with related techniques. The evaluation considers multi-objective
values, computing time, and outlierness of solutions.
• An open-source implementation of P2CE: github.com/hiaac-finance/p2ce
2 Background and Related Works
We now formalize the problem of generating counterfactual explanations and present
relevant works on the topic. In this section and in the remainder of this paper, we
3

consider that we have access to a datasetD= (X,Y);X∈R n×d;Y∈{0,1} n sampled
from a distributionP. We note as (x i,yi) thei-th sample ofDandx(i) as thei-th
coordinate of vectorx. We also have a fitted classifierf:R d→[0,1] that approximates
the probabilityf(x)≈P(Y= 1|X=x). The classifier is accompanied by a threshold
τ∈[0,1], and a positive decision ˆy i = 1 is made whenf(x i)≥τ.
2.1 Explanations
Explainability has emerged as a very relevant area of research in machine learning as
complex models become widely employed in applications that greatly impact individ-
uals’ lives. “Explanations” are presented in different forms, but, in general, they try
to answer the question “which features of the input were determinants of the output
of the model?” . These explanations can be “global”, with a general description of the
relevant features for any input [8, 9], or “local” where for a specific observationx, it
is desired to obtain the set of relevant features. LIME [10] and SHAP [11] are among
the most widely used methods for local explanations and present a similar concept:
studying how small perturbations in each feature impact the model prediction. For a
given observationxand a modelf, a vectorϕ∈R d is returned whereϕ(i) represents
the “importance of the featurei” in this prediction. In particular, SHAP has the prop-
erty thatf(x) =E[f(x)] + ∑d i=1ϕ(i), and eachϕ(i) can be seen as the “contribution”
of the featureito the total predictionf(x).
2.2 Counterfactual Explanations
Unlike the general idea of explanations, where the objective is to comprehend the
rationale behind complex model predictions, counterfactual explanations are designed
to give individuals the possibility ofaction[1], which are also commonly calledaction-
able recourse[2, 12]. Molnar [13] elucidates that counterfactual explanations are an
accessible method to illustrate “what-if” scenarios: “What would be the prediction of
the model for credit scoring, given that I increased my annual income by 10%?” . These
“what-if” scenarios should consider the closest world possible, as considering absurd
scenarios would not contain relevant information about the model and would not be
anactionableexplanation. Wachter et al. [1] formalized the problem of generating
counterfactual explanations as follows:
arg min
x′
max
λ
λ(f(x′)−y ′)2 +c(x,x′) (1)
This formulation searches for a valuex ′ with a predictionf(x ′) equal to the
desired outcomey′. The functioncis the distance betweenxandx ′ and encapsulates
the idea of “closest world” . This distance functioncshould be able to represent the
ease of reachingx ′ fromx′ in the real world, i.e., ifx ′ is afeasiblescenario for an
individual with attributesx. Previous works on counterfactual explanations designed
algorithms to obtain feasible counterfactual explanations [4, 5] and different metrics
cwere considered [3, 14]. Another concern is that solutions should beplausible, i.e.,
the suggested profilex ′ should be probable in real-world data [6, 7]. For example, it
4

is uncommon to observe a young individual with high investments, and a counterfac-
tual explanation should not ask for that. Lastly, to fulfill individual preferences, it is
important to provide multiple anddiversecounterfactual explanations [4, 15].
Recent work has also studied how to solve the optimization problem from Eq.1 and
similar formulations. Some of the present solutions were limited to specific models,
such as linear models [12, 15], tree ensembles [16–18], image models [19] or differ-
entiable models [4]. Model-agnostic algorithms [4, 5, 20–22] have been introduced,
offering significant advantages due to their ability to be applied across various model
types without imposing restrictions.
2.3 Pareto-Optimal Counterfactual Explanations
In the classification setting, we are interested in counterfactual explanationsx′ =x+a
such thatf(x ′)≥τwhilef(x)< τ. The vectoracan be called anactionand has
a useful interpretation: coordinatea(i) represents the increase/decrease necessary on
thei-th feature; ifa(i) = 0, no change is necessary. Feasibility has been measured in
the literature in different ways, which motivates the use of multi-objective distance
functionsc:R d×Rd :R m, where we havemobjectives. Considering thatNis the set
of indices of numerical features, one can calculate the average “length” of the change
in the values of the features. We call this metricaverage continuous distance:
c1(x,w) = 1 #N ∑ i∈N |x(i)−w(i)| r(i) (2)
Wherer(i) is the standard deviation of the featurei. Similarly, the cost of a
counterfactual explanation can be represented by the maximum length of changes.
We define themaximum continuous distanceas:
c2(x,w) = max i∈N |x(i)−w(i)|(3)
When dealing with categorical features, we cannot directly measure the length of
a suggested change. To consider such a variable type, an approach in the literature
has been to measure the number of suggested changes, that is, the number of features
with different values. This metric also arises from the idea of sparsity, which considers
that moderate changes in a small number of features might be more feasible than
small changes in a very large number of features. This can be calculated among all
the features, not only the numerical ones. We call it asnumber of changes distance:
c3(x,w) =
d∑
i=1
I[x(i)̸=w(i)] (4)
When dealing with multi-objectives, the preference among two solutionswandz
must consider all of the objectives. A solution can be seen as non-dominated if there
is no other solution that is better in all objectives. These solutions can be multiple,
and we can call them Pareto-Optimal solutions.
Definition 1(Pareto-Optimal Solutions).Given a multi-objective functionc(x,·) :
Rd→R m that we want to minimize and a set of solutionsS, a solutionwis Pareto-
optimal if and only if∄z∈Asuch thatc(x,z)⪯c(x,w), i.e.,c i(x,z)≤c i(x,w),∀i.
5

Algorithm 1MAPOCAM
1:procedureMAPOCAM(f,x, A,c,k)
2:Q←{(0,0)}
3:whileQ̸={}do
4:a,i←Q.pop()
5:iff(x+a)≥τthen
6:S←S∪{x+a}
7:continue
8:ifPRUNE(f,x,c,a,S,k)then continue
9:forv∈ A(i)do
10:a(i)←v
11:Q←Q∪{(a,i+ 1)}
12:returnS
13:procedurePRUNE(f,x,c,a,S,k)
14:forz∈Sdo
15:ifc(x,z)⪯c(x,x+a)then return true
16:if ∑d j=1 I[a(j)̸=0] >kthen return true
17: fa←maximum prediction
18:if fa <τthen return true
19:return false
The problem of generating counterfactual explanations has previously been
considered by Raimundo et al. [5] with MAPOCAM. This algorithm uses a branch-
and-bound strategy to find the Pareto-Optimal solutions in a large set Aof possible
counterfactual explanations.Ais built for each samplexas the product of discretized
grids for each feature A(i), i.e.,A= A(1)×···× A(d). If the discretization of each
feature has 10 different values, verifying which possibilities are valid counterfactual
explanations would have complexityO(10 dδ) whereδis the cost of callingf(x). This
complexity may be infeasible even with a few features, and MAPOCAM employs
different pruning strategies to reduce computational complexity.
MAPOCAM is presented in Alg. 1. It searches for actionsasuch thatf(x+a)≥τ,
starting witha=0, and that present at mostksuggested changes. Then, it con-
structs counterfactual explanations by considering changing a feature at a time. This
procedure can be performed efficiently due to the fact that commonly defined costs
for counterfactual explanations, such as the three presented above, have monotonicity
with respect to|a|. If|a|⪯|˜a|, we havec(x,x+a)⪯c(x,x+ ˜a). The search strategy
is designed so that if|a|⪯|a ′|, the actiona ′ will only be evaluated afterahas been
evaluated. The resulting property is that the distances will not reduce as the search
goes deeper. Based on that, each A(i) is ordered on the basis of the absolute values.
Another strategy to reduce complexity is to stop the search based on a bound
of the maximum predictionf(·) that the current node can reach. Consider that the
featuresD={1,...,j}have already been evaluated in the search, and the following
6

path will only evaluate altering the features{j+ 1,...,d}. We are interest in:
fa = max
˜a∈A
˜a(i)=a(i),i∈D
f(x+ ˜a) (5)
If we know that fa < τ, following this path will not result in valid counterfac-
tual explanations. To calculate this bound, MAPOCAM uses the property that some
classifiers have monotonicity with respect to inputx. Iffis monotonic with respect
to each coordinate ofx, the maximum value can easily be obtained by considering
the action that hasa ′(i) =a(i);∀i∈D, and fori /∈D,a ′(i) = maxA(i) iffis an
increasing function of thei-th coordinate ora ′(i) = minA(i) if it is a decreasing one.
MAPOCAM is also capable of calculating the exact value of fa with tree ensembles.
In this scenario, the trees are traversed following the values ofx+a, and when an split
is decided by a feature not inD, it should return the maximum output of following
both paths.
Although MAPOCAM is capable of obtaining Pareto-optimal counterfactual
explanations that are feasible, it may fail when considering plausibility. Certain solu-
tions may not have a significant probability of being observed in the real world.
Furthermore, the bound strategy depends on the fact thatfhas monotinicity with
respect tox, which is not valid for models such as SVM and neural networks. Our
proposal, P2CE, improves the previous work by altering the algorithm so that we gen-
erate counterfactual explanations that are inlier (Sec. 3) and supporting any model,
without the monotonicity constraint (Sec. 4).
3 Generating Inlier Counterfactual Explanations
Although many proposed algorithms focus on generating feasible counterfactual expla-
nations, they may fail to ensure plausibility. This is also the case for MAPOCAM.
Even if a counterfactual explanation is feasible and have a great proximity to the ref-
erence sample, it can still be outside the data distribution, as illustrated by the simple
example in Fig. 1. Our proposed algorithm, P2CE, was designed to generate Pareto-
optimal inlier counterfactual explanations using the isolation forest [23] algorithm for
outlier detection.
For a datasetX∼P, an outlier detection functionu(x) = 1 ifP(X=x)≤ε,
whereεis a small positive value andu(x) = 0 otherwise. Isolation forest algorithm
learns the functionuby creating multiple decision trees that are optimized to minimize
the number of samples in each leaf. Samples that are “outside” the data distribution
will be more easily isolated, and therefore the path from the root to the respective
leaf will be shorter. One useful property of Isolation Forest is that, because it is a
tree ensemble, it is capable of producing predictions when some coordinates of the
input are absent. This is achieved by exploring both potential paths when the decision
variable at a node is indeterminate. Furthermore, isolation forest has presented the
best results in outlier detection tasks in recent benchmarks [24].
7

MAPOCAM searches for counterfactual explanations in a grid Athat is defined
based on the product of discretized feature values. However, a counterfactual explana-
tionx+amay be feasible but outside of the data distribution, as Ais created without
considering the correlation between the features. In that sense, such counterfactual
explanation may not be useful to an individual, as the pointx+ais not reachable.
Our objective is then to collect all Pareto-Optimal solutions in the set of inlier coun-
terfactual explanations. It is important to note that this procedure will result in a
different set of solutions than obtaining all Pareto-optimal actions and removing the
ones from this set that are outliers.
P2CE is presented in Alg. 2. Whenever a valid solutionx+ais found in the
search, P2CE verifies whether this counterfactual explanation is an outlier. If not, we
can add this solution to the setS. Otherwise, this solution should not be included
in the set of solutions. Although the cost of the counterfactual explanation will only
increase when considering further changes in coordinatei, larger changes can return
to being within the data distribution. This procedure could be performed with an
arbitrary outlier detectionu, such as isolation forest, autoencoder-based approaches,
local outlier factor.
An additional gain in efficiency can be obtained ifucan evaluate whether samples
˜xwith missing values are outliers.u(˜x) = 1 indicates that placing any value in the
undefined coordinates will also result in an out-of-distribution sample. In that way,
there is no need to consider further changes in this coordinates. This procedure is
performed by P2CE on lines (20-21).
4 Estimating Maximum Prediction for Any Model
As presented in Alg. 2, the branch-and-bound strategy used by P2CE depends on the
estimation of fa, the maximum prediction obtainable by further changes in action
a. If this value is lower thanτ, traversing this branch becomes unnecessary. In
MAPOCAM, this estimate is done under the assumption of model monotonicity, as
discussed in Sec. 2. Widely used models, including KNN, neural networks, SVM, and
others, do not adhere to this assumption. We present a method for estimating the
maximum prediction based on SHAP values [11] using the additive property of feature
attributions.
In more detail, we have a partial solutionx+awith a set of featuresDthat will
not have their values altered (either they were fixed by the user or they are fixed
because their values have already been altered previously in the search process). Let
X(a,D) denote the space where all elements have the same fixed values asx, i.e., if ˜a∈
X(a,D) =⇒a(i) = ˜a(i),∀i∈D. The goal is to determine fa := max˜a∈X(a,D)f(x+ ˜a).
If fa <τ, there is no valid counterfactual inX (a,D).
SHAP values have the property of being additive feature attributions, that is,
f(x) =E[f(x)] + ∑d i=1ϕi(x), whereϕ i(x) represents the attribution of thei-th fea-
ture calculated for samplex. Notice that ∑ i∈Dϕi(x) reflects the attribution of fixed
features, while ∑ i/∈Dϕi(x) relates to open ones. Consider that ϕp is the maximum
attribution of the featurepfor any value ofxin the domain ofX. Although we may
not have access to the support ofX, we can approximate ϕp by calculating the feature
8

Algorithm 2P2CE
1:procedureP2CE(f,x, A,c,k)
2:Q←{(0,0)}
3:whileQ̸={}do
4:a,i←Q.pop()
5:iff(x+a)>τthen
6:ifu(x+a)̸= 1then
7:S←S∪{x+a}
8:continue
9:ifPRUNE(f,u,x,c,a,i,S,k)then continue
10:forv∈ A(i)do
11:a(i)←v
12:Q←Q∪{(a,i+ 1)}
13:returnS
14:procedurePRUNE(f,u,x,c,a,i,S,k)
15:forz∈Sdo
16:ifc(x,z)⪯c(x,x+a)then return true
17:if ∑d j=1 I[a(j)̸=0] >kthen return true
18: fa←maximum prediction
19:if fa <τthen return true
20:˜x←[x(0) +a(0),...,x(i) +a(i),NULL,...,NULL]
21:ifu(˜x) = 1then return true
22:return false
attributions of a large dataset and calculating the maximum value. Thus, we obtain
a bound for fa:
max
˜a∈X(a,D)
f(x+ ˜a) =E[f(x)] +
∑
i∈D
ϕi(x⋆) + ∑
i/∈D
ϕi(x⋆)
≤E[f(x)] +
∑
i∈D
ϕi(x⋆) + ∑
i/∈D
ϕi
=E[f(x)] +
∑
i∈D
ϕi(x) +
∑
i/∈D
ϕi +
(∑
i∈D
ϕi(x⋆)− ∑
i∈D
ϕi(x)
)
=E[f(x)] +
∑
i∈D
ϕi(x) +
∑
i/∈D
ϕi +R (x,D)
=f(x)−
∑
i/∈D
ϕi(x) +
∑
i/∈D
ϕi +R (x,D)
(6)
wherex ⋆ solves the maximization problem,ϕ i(x) andϕ i(x⋆) are the SHAP values
for thei-th feature for the solutionsxandx ⋆ respectively. Notice that this upper
9

bound has a residual termR (x,D) that is the difference between the attributions of
fixed features (fromD) of the initial observationxand the solutionx ⋆. Later, we will
discuss how the residualR(x,D) is a small value wheneverX (a,D) is small.
As we are using an upper bound on the optimization problem, we overstate the
maximum prediction, which could increase the computational time. However, this
overestimation does not compromise the quality of the solutions obtained. In Sec. 5,
we evaluate the computing cost of our solution in real-world datasets.
We can make a small alteration to the previously formulated problem to reduce
the upper bound. This is done by considering that the generation of counterfactuals is
usually done with a constraint on how many features will be changed simultaneously.
Letkbe the number of features that can be further altered from the partial solution
x+aandX (a,D,k) ={˜a∈X (a,D)|∑ i/∈DI[ai̸= ˜ai]≤k}that is, the set of actions
that have at mostkopen features different froma. LetO k⊆D C be the set ofkopen
features that have thek-biggest ϕi, i.e., ifi∈O k =⇒ ϕi≥ ϕj∀j /∈Ok. Using the
same idea as from the previous proof, we can obtain a similar upper bound:
max
˜a∈X(a,D,k)
f(x+ ˜a)≤f(x)−
∑
i∈Ok
ϕi(x) +
∑
i∈Ok
ϕi +R (x,Ok) (7)
AsO k ⊆D C, we have ( −∑ i∈Ok ϕi(x) +∑ i∈Ok ϕi ) <(
−∑ i∈DCϕi(x) +∑ i∈DCϕi ) and this formulation gives an upper bound that is
lower than the previous one obtained. We will estimate that fa is smaller thanτ
more frequently, thus, reducing the number of branches that the algorithm needs to
search for.
One last detail is the residual termR. This term is the difference between the
feature attributions of the reference samplexand the pointx ⋆ that maximizesf(x ⋆)
(x⋆ =x+a ′,a′∈X (a,D,k)). The lower this value, the more tight our upper bound is
going to be. During the search,xandx ⋆ will be close values, since onlykfeatures
are changed at most. Previous work by Khan et al. [25] has theoretically analyzed
explainer astuteness: how much explanations can change when the input sample is
altered. Their work has shown that when two pointsxandx ′ are sufficiently close,
the SHAP attributions of these two samples will be bounded by the distance between
them with high probability.
5 Experiments
To evaluate the proposed algorithm and compare it against related techniques, we
performed a set of experiments using common classifiers and real-world benchmark
datasets. Our experiments evaluated the capabilities of P2CE in generating solutions
that are inside data distribution and are optimal in regard to multiple objectives.
Datasets.We considered three benchmark datasets of different sizes (in terms of
the number of samples and features). Two datasets are from finance and are widely
used to evaluate credit scoring techniques. German Credit [26] contains 1000 samples
with 27 client features and a classification as good or bad risk (with 70%-30% distri-
bution). Taiwan [27] dataset includes information on credit card default from 30,000
clients of a Taiwanese bank with 11 features after preprocessing. We also considered
10

Adult dataset [28], a dataset with personal information and income data collected
from the US 1994 census with 8 features for 48,000 individuals. To be able to support
MAPOCAM, we have not included categorical features that are not binary. In each
dataset, we selected a set of features that should be considered to generate counterfac-
tual explanations, avoiding unmutable personal characteristics. In the end, German
Credit had 21 considered features, Taiwan 10 and Adult had 8.
Classifiers.Our experiments included commonly employed classifier algorithms,
which include a Logistic Regression (LR), Gradient-Boosting (LightGBM) and a
Multi-Layer Perceptron (MLP). LR satisfies the monotonicity constraints imposed by
MAPOCAM and was used in a ablation study of the inlieness of counterfactual expla-
nations. Remaining classifiers are highly complex with non-linearities and highlight
the flexibility of P2CE.
Compared Algorithms.Experiments included comparisons with MAPOCAM [5] to
demonstrate the improvements obtained from our novel algorithm. A comparison was
also made with DICE [4] and NICE [21], two popular algorithms for counterfactual
explanations. DICE was initially presented as a gradient-based algorithm to gener-
ate diverse solutions, however, we employ a genetic implementation with the same
objective but that is model-agnostic. It can generate an arbitrary number of coun-
terfactual explanations and tries to maximize diversity among them. NICE is a fast
approach that uses information from neighboring samples to generate counterfactual
explanations. It is limited to generating only one solution for the input sample.
Setting.The datasets were separated into train, validation, and test sets of size 40%,
10%, 50%. Hyperparameter tuning was performed with the Optuna package [29] with
50 trials, and the final models are those that achieved the highest balanced accuracy in
the validation set. P2CE used an isolation forest fitted to the training data. A stronger
algorithm, the extended isolation forest [30], was fitted on the test data to evaluate
the plausibility of counterfactual explanations. To classify outliers, we consider that
all datasets have an infection rate of 5% of outlier samples. The metrics reported in
the remaining of the section are the average result of generating counterfactuals for 50
randomly selected individuals from the test set that obtained the negative prediction.
5.1 Inlierness of Counterfactual Explanations
The initial experiment is intended to demonstrate the ability of P2CE in generating
plausible counterfactual explanations compared to MAPOCAM. To do so, we gener-
ated counterfactual explanations for the LR model, which satisfies monotonicity with
respect to inputx. In that way, P2CE does need to use SHAP to estimate fa, and
the difference between algorithms is how they deal with outlier solutions. We also
performed an ablation study by removing the procedure from lines 20-21 of Alg. 2
that evaluates if partial solutions can already be classified as outliers. We call this
simplified version P2CE (Ablation). Both algorithms were executed considering solu-
tions with at maximum 3 changes and considering only one objective, the average
continuous distance.
The results are depicted in Tab. 1, including the average computation time, the
average distance of the solutions, and the percentage of solutions that were outliers.
11

c(x, x′) % Outliers Time (s)
German Credit
MAPOCAM 0.093 (±0.081) 0 15.7 (±13.6)
P2CE (Ablation) 0.093 (±0.081) 0 16.0 (±13.6)
P2CE 0.093 (±0.081) 0 16.2 (±14.1)
Taiwan
MAPOCAM 0.274 (±0.120) 8 58.8 (±51.8)
P2CE (Ablation) 0.276 (±0.119) 6 56.0 (±49.2)
P2CE 0.276 (±0.119) 6 51.7 (±77.1)
Adult
MAPOCAM 0.138 (±0.066) 16 1.3 (±0.8)
P2CE (Ablation) 0.183 (±0.145) 6 3.9 (±8.0)
P2CE 0.171 (±0.107) 2 2.4 (±3.1)
T able 1Results of MAPOCAM and P2CE using a LR model.
Reported results are the average cost and time on 50 individuals
and the percentage of occurrence of outliers solutions among all
individuals.
Due to only using one objective, the set of Pareto-Optimal solutions is only com-
posed of one solution. On German Credit, none of the techniques have presented
outliers counterfactual explanations. This might occur because of the simplicity of
the dataset, which is only composed of 1000 samples. However, in Taiwan and Adult
datasets, P2CE generates fewer outlier counterfactual explanations than MAPOCAM.
Although P2CE had a higher average computing time and a higher distance of solu-
tions, this is expected. By removing solutions fromA(due to them being outliers), one
might remove solutions that would be Pareto-Optimal. This also increases the num-
ber of solutions that must be evaluated before finding a valid one. When comparing
P2CE and P2CE (Ablation), the average computing time shows that the procedure
of evaluating if partial solutions are already outliers can help the algorithm in avoid
unnecessary search.
5.2 One Objective in Non-linear Classifiers
Using an LGBM and an MLP, we evaluated P2CE, MAPOCAM, DICE and NICE
capabilities of generating a counterfactual with small distance (one objective). P2CE
and MAPOCAM were configured with the average continuous distance objective
and considering actions that change at most three features. P2CE is using the Tree
Explainer for the LGBM model and Deep Explainer for the MLP model. MAPOCAM
uses the adapted version for tree ensembles in the experiments with LGBM. DICE is
set to generate only one solution. We present the results at Fig. 2 separated by model
and dataset.
In all scenarios, P2CE achieved the lowest cost while maintaining highly competi-
tive computational time. The difference in computing time between MAPOCAM and
P2CE is more evident in the MLP experiments. MAPOCAM did not use an estimate
offa and had to evaluate many possibilities fromA, taking 100 seconds on average in
the Taiwan dataset. P2CE was able to obtain the solutions in a few seconds. On the
LGBM experiment, while MAPOCAM uses the tree structure to estimate the max-
imum prediction of the model, the cost of this procure is higher than the approach
12

Fig. 2Resulting in computing time, distance and occurrence of outliers of P2CE and three compared
algorithms with three datasets and two models. In the scatter plot, lines represent 90% range of
observed costs.
used by P2CE, as the average computing time shows. The results show that DICE
and NICE algorithms are faster than P2CE, yet, they do not have the guarantees
of generating Pareto-optimal solutions. NICE only obtained competitive costs in the
Taiwan and Adult dataset with the LGBM model. Furthermore, NICE cannot handle
multiple objectives or generate more than one counterfactual.
The bar plots at the bottom of Fig. 2 show the percentage of outlier solutions
generated by each algorithm. In all cases, P2CE has an outlier rate of less than 5%,
and the only other algorithm with competitive results was MAPOCAM. However,
P2CE significantly exceeded the results from MAPOCAM with the MLP model.
5.3 Multiple-objective
To evaluate our proposal considering multiple objectives, we execute P2CE using the
three objectives present in Sec. 2: average continuous distance, maximum continuous
distance, and number of changes. MAPOCAM was executed using the same objectives,
DICE was executed to generate 4 counterfactual explanations for each individual,
and NICE was not included in this experiment, as its formulation does not consider
multiple objectives. Comparing solutions with multiple objectives is not a straightfor-
ward procedure. To do so, we utilize hypervolumes, a metric defined as the “volume”
defined between the Pareto frontier (region of Pareto-optimal solutions) and the worse
performance identified. This measure is between 0 and 1, and the larger this volume,
the better the solutions.
Results are displayed in Tab. 2. We also included the percentage of solutions
that were outliers and the average computing time. With all datasets and models,
MAPOCAM presented the highest volume, closely followed by P2CE. This result
was expected as MAPOCAM presents guarantees in obtaining Pareto-Optimal solu-
tions. Even though P2CE also presents such theorical guarantees, it is not capable of
13

obtaining MAPOCAM solutions, as some of them are outliers and also due to SHAP
approximation error. However, the low distances of MAPOCAM solutions is accompa-
nied by a high computational cost. For example, MAPOCAM required 100 seconds to
generate counterfactual explanations with the Taiwan dataset and MLP, while P2CE
took less than one second. In all data sets and models, DiCE represented really low
hypervolume values, which is not competitive with the other two techniques.
Algorithm Hypervolume % Outliers Time (s)
German Credit with LGBM
MAPOCAM 0.53 (±0.11) 4 2.23 (±3.1)
DICE 0.31 (±0.21) 20 0.18 (±0.0)
P2CE 0.52 (±0.12) 4 0.93 (±1.7)
Taiwan with LGBM
MAPOCAM 0.65 (±0.02) 13 8.0 (±12.2)
DICE 0.41 (±0.15) 83 1.0 (±4.0)
P2CE 0.64 (±0.07) 6 0.48 (±0.6)
Adult with LGBM
MAPOCAM 0.58 (±0.06) 14 0.91 (±0.5)
DICE 0.35 (±0.16) 90 0.17 (±0.0)
P2CE 0.48 (±0.2) 1 0.94 (±1.0)
German Credit with MLP
MAPOCAM 0.45 (±0.2) 14 49.62 (±42.4)
DICE 0.24 (±0.16) 20 0.23 (±0.0)
P2CE 0.44 (±0.21) 5 9.32 (±6.0)
Taiwan with MLP
MAPOCAM 0.41 (±0.16) 11 118.51 (±96.8)
DICE 0.27 (±0.16) 93 0.28 (±0.02)
P2CE 0.39 (±0.16) 1 0.81 (±1.0)
Adult with MLP
MAPOCAM 0.42 (±0.17) 58 6.24 (±4.3)
DICE 0.27 (±0.14) 87 0.19 (±0.0)
P2CE 0.4 (±0.18) 11 2.34 (±1.4)
T able 2Average hypervolume, percentage of outliers
solutions and average computing time of P2CE and two
compared algorithms. The higher the hypervolume, the
better. While MAPOCAM obtains higher hypervolume than
MAPOFCEM, it is accompanied by significant
disadvantages in generating outlier counterfactual
explanations and a high computing time.
We also present an example of the solutions identified by each of the algorithms
in Tab. 3. These were the solutions generated for a specific individual from the Adult
dataset that obtained the negative prediction from the MLP model. The table con-
tains only the features that were altered by any of the solutions and also includes
whether the solution is an outlier (u(x)) and what was the classifier prediction (f(x)).
All solutions provided by Dice were outliers and MAPOCAM just presented one in-
distribution solution. In two of the examples, Dice asks for 97 hours of weekly work,
which is obsviouly an solution with no plausability. It also suggest large changes on
capital gain and capital loss. Notice that while the MAPOCAM and P2CE solutions
14

Capital Gain Capital Loss Hours per Week Has Degree Is Married Gov. Jobu(x)f(x)
0 0 30 0 0 0 - 0.32
P2CE
7520 0 36 0 1 0 0 0.50
0 0 52 0 1 0 0 0.50
0 0 30 1 1 0 0 0.54
MAPOCAM
0 1980 30 1 0 1 1 0.50
4512 891 30 0 1 0 1 0.50
5264 792 30 0 1 0 1 0.50
10528 0 30 0 1 0 1 0.50
0 0 30 1 1 0 0 0.54
Dice
36470 0 30 0 1 0 1 0.65
39877 0 30 0 0 0 1 0.53
0 0 97 0 1 0 1 0.61
21794 0 97 0 0 0 1 0.63
T able 3Example of counterfactual explanations for an random sample from the Adult dataset that
received the negative prediction from the MLP model. These solutions were obtained by P2CE and
MAPOCAM using multiple objectives and DICE configured to generate 4 solutions.
had exactlyf(x) = 0.5, the minimum value necessary to obtain the positive predic-
tion, the DICE solutions had higher values. P2CE can generate solutions considering
other threshold valuesτthat can give greater confidence in the positive prediction.
6 Limitations and Future Work
P2CE is capable of generating multiple Pareto-optimal counterfactual explanations for
any model. Furthermore, the solutions are obtained with practical computing time.
In this section, we discuss some of the limitations of our proposal and present future
directions.
SHAP Dependency.Our algorithm uses Shapley values to obtain an upper bound
of the prediction of a model, as presented in Sec. 4. Shapley values have exponential
computing time in the number of variables of the model, and the current literature pro-
vides algorithms to approximate such values. This is valid for SHAP algorithms such as
Kernel Explainer, Permutation Explainer [11] or DeepLift [11, 31]. Tree Explainer [32]
is an exception, which leverages the tree structure to account for feature interactions.
Furthermore, certain models and SHAP implementations may have a higher com-
puting cost than others. The approximation error and computing time from SHAP
algorithms should be considered as P2CE is dependent on it. The approximation error
might mislead the prunning strategy, however, our solutions presented really lower
costs than algorithms such as NICE and DICE, and having only higher costs than
MAPOCAM, which is guaranteed to obtain Pareto-optimal solutions. Furthermore,
research is still being done to obtain exact and efficient SHAP values, which we believe
will further improve the capabilities of P2CE.
Discretized Grid.P2CE searches for counterfactual explanations within a discrete
grid of possibilities, and the granularity of this grid limits how close a solution can
15

be identified. Although increasing granularity will result in better optimal solutions,
it will also increase search duration. Due to the practical use of counterfactual expla-
nations, a really thin granularity is not necessary. For example, on a credit loan
application, a counterfactual explanation that suggests an increase in income by 1000
is equally as good as one that suggests an increase by 998. P2CE allows the grid to
be set with great control for each application by selecting minimum and maximum
values and the specific granularity of each future. A possible future direction is devel-
oping an adaptive grid, which will automatically increase the granularity of features
that can indeed alter the predictions and decreasing the granularity of features that
have a low impact on the outcome. This procedure could also take advantage of SHAP
values to do so.
7 Conclusion
In this work, we presented P2CE, a novel algorithm for generating Pareto-optimal
counterfactual explanations. P2CE distinguishes itself through its model-agnostic
design and distribution awareness, achieved by integrating an isolation forest for out-
lier detection and leveraging SHAP values for efficient computation. This approach
allows P2CE to provide users with a diverse set of actionable and plausible expla-
nations, even for complex nonlinear models. Our empirical evaluation across various
datasets and scenarios demonstrated that P2CE achieves Pareto-optimal solutions
with superior performance in terms of computational cost and outlier detection,
enabling faster and more informed decision-making in real-world applications.
References
[1] Wachter, S., Mittelstadt, B., Russell, C.: Counterfactual explanations without
opening the black box: Automated decisions and the gdpr. Harv. JL & Tech.31,
841 (2017)
[2] Karimi, A.-H., Sch¨ olkopf, B., Valera, I.: Algorithmic recourse: from counterfactual
explanations to interventions. In: Proceedings of the 2021 ACM Conference on
Fairness, Accountability, and Transparency, pp. 353–362 (2021)
[3] Verma, S., Boonsanong, V., Hoang, M., Hines, K., Dickerson, J., Shah, C.: Coun-
terfactual explanations and algorithmic recourses for machine learning: A review.
ACM Computing Surveys56(12), 1–42 (2024)
[4] Mothilal, R.K., Sharma, A., Tan, C.: Explaining machine learning classi-
fiers through diverse counterfactual explanations. In: Proceedings of the 2020
Conference on Fairness, Accountability, and Transparency, pp. 607–617 (2020)
[5] Raimundo, M.M., Nonato, L.G., Poco, J.: Mining pareto-optimal counterfactual
antecedents with a branch-and-bound model-agnostic algorithm. Data Mining
and Knowledge Discovery, 1–33 (2022)
16

[6] Kanamori, K., Takagi, T., Kobayashi, K., Arimura, H.: Dace: distribution-aware
counterfactual explanation by mixed-integer linear optimization. In: Proceedings
of the Twenty-Ninth International Conference on International Joint Conferences
on Artificial Intelligence, pp. 2855–2862 (2021)
[7] Poyiadzi, R., Sokol, K., Santos-Rodriguez, R., De Bie, T., Flach, P.: Face: feasible
and actionable counterfactual explanations. In: Proceedings of the AAAI/ACM
Conference on AI, Ethics, and Society, pp. 344–350 (2020)
[8] Friedman, J.H.: Greedy function approximation: a gradient boosting machine.
Annals of statistics, 1189–1232 (2001)
[9] Goldstein, A., Kapelner, A., Bleich, J., Pitkin, E.: Peeking inside the black box:
Visualizing statistical learning with plots of individual conditional expectation.
journal of Computational and Graphical Statistics24(1), 44–65 (2015)
[10] Ribeiro, M.T., Singh, S., Guestrin, C.: ” why should i trust you?” explaining
the predictions of any classifier. In: Proceedings of the 22nd ACM SIGKDD
International Conference on Knowledge Discovery and Data Mining, pp. 1135–
1144 (2016)
[11] Lundberg, S.M., Lee, S.-I.: A unified approach to interpreting model predictions.
Advances in Neural Information Processing Systems30(2017)
[12] Ustun, B., Spangher, A., Liu, Y.: Actionable recourse in linear classification. In:
Proceedings of the Conference on Fairness, Accountability, and Transparency, pp.
10–19 (2019)
[13] Molnar, C.: A guide for making black box models explainable. URL:
https://christophm. github. io/interpretable-ml-book, 3 (2018)
[14] Guidotti, R.: Counterfactual explanations and how to find them: literature review
and benchmarking. Data Mining and Knowledge Discovery38(5), 2770–2824
(2024)
[15] Russell, C.: Efficient search for diverse coherent explanations. In: Proceedings of
the Conference on Fairness, Accountability, and Transparency, pp. 20–28 (2019)
[16] Dutta, S., Long, J., Mishra, S., Tilli, C., Magazzeni, D.: Robust counterfactual
explanations for tree-based ensembles. In: International Conference on Machine
Learning, pp. 5742–5756 (2022). PMLR
[17] Lucic, A., Oosterhuis, H., Haned, H., Rijke, M.: Focus: Flexible optimizable
counterfactual explanations for tree ensembles. In: Proceedings of the AAAI
Conference on Artificial Intelligence, vol. 36, pp. 5313–5322 (2022)
[18] Parmentier, A., Vidal, T.: Optimal counterfactual explanations in tree ensembles.
17

In: International Conference on Machine Learning, pp. 8422–8431 (2021). PMLR
[19] Augustin, M., Boreiko, V., Croce, F., Hein, M.: Diffusion visual counterfactual
explanations. Advances in Neural Information Processing Systems35, 364–377
(2022)
[20] Karimi, A.-H., Barthe, G., Balle, B., Valera, I.: Model-agnostic counterfactual
explanations for consequential decisions. In: International Conference on Artificial
Intelligence and Statistics, pp. 895–905 (2020). PMLR
[21] Brughmans, D., Leyman, P., Martens, D.: Nice: an algorithm for nearest instance
counterfactual explanations. Data mining and knowledge discovery38(5), 2665–
2703 (2024)
[22] Guidotti, R., Monreale, A., Ruggieri, S., Naretto, F., Turini, F., Pedreschi, D.,
Giannotti, F.: Stable and actionable explanations of black-box models through
factual and counterfactual rules. Data Mining and Knowledge Discovery38(5),
2825–2862 (2024)
[23] Liu, F.T., Ting, K.M., Zhou, Z.-H.: Isolation forest. In: 2008 Eighth Ieee
International Conference on Data Mining, pp. 413–422 (2008). IEEE
[24] Bouman, R., Bukhsh, Z., Heskes, T.: Unsupervised anomaly detection algorithms
on real-world data: how many do we need? Journal of Machine Learning Research
25(105), 1–34 (2024)
[25] Khan, Z.Q., Hill, D., Masoomi, A., Bone, J.T., Dy, J.: Analyzing explainer
robustness via probabilistic lipschitzness of prediction functions. In: International
Conference on Artificial Intelligence and Statistics, pp. 1378–1386 (2024). PMLR
[26] Hofmann, H.: Statlog (German Credit Data). UCI Machine Learning Repository.
DOI: https://doi.org/10.24432/C5NC77 (1994)
[27] Yeh, I.-C.: default of credit card clients. UCI Machine Learning Repository. DOI:
https://doi.org/10.24432/C55S3H (2016)
[28] Becker, B., Kohavi, R.: Adult. UCI Machine Learning Repository. DOI:
https://doi.org/10.24432/C5XW20 (1996)
[29] Akiba, T., Sano, S., Yanase, T., Ohta, T., Koyama, M.: Optuna: A next-
generation hyperparameter optimization framework. In: Proceedings of the
25th ACM SIGKDD International Conference on Knowledge Discovery &
Data Mining. KDD ’19, pp. 2623–2631. Association for Computing Machin-
ery, New York, NY, USA (2019). https://doi.org/10.1145/3292500.3330701 .
https://doi.org/10.1145/3292500.3330701
18

[30] Hariri, S., Kind, M.C., Brunner, R.J.: Extended isolation forest. IEEE transac-
tions on knowledge and data engineering33(4), 1479–1489 (2019)
[31] Shrikumar, A., Greenside, P., Kundaje, A.: Learning important features through
propagating activation differences. In: International Conference on Machine
Learning, pp. 3145–3153 (2017). PMlR
[32] Lundberg, S.M., Erion, G.G., Lee, S.-I.: Consistent individualized feature attri-
bution for tree ensembles. arXiv preprint arXiv:1802.03888 (2018)
19
