---
title: 'Profit-Based Counterfactual Explanations for Product Improvement: A Case Study of Manga Sales
  in Japan'
url: https://arxiv.org/abs/2607.01610
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Keita Kinjo
- Takeshi Ebina
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.01610
pages: 8
chars: 45757
fetched_at: '2026-11-08T13:05:14+00:00'
kb_version: 1
---

# Profit-Based Counterfactual Explanations for Product Improvement: A Case Study of Manga Sales in Japan

Profit-Based Counterfactual Explanations for Product Improvement:
A Case Study of Manga Sales in Japan*
Keita Kinjo 1 and Takeshi Ebina 2
Abstract— Counterfactual explanation (CE) is widely used
to enhance the interpretability of machine learning models
and support data-driven decision-making based on model
predictions. However, existing CE methods typically require
two exogenously specified inputs: a desired output value (target)
and a distance function that quantifies changes in explanatory
variables. In regression settings, neither the validity of target
specification nor the practical interpretation of the distance
metric has been sufficiently addressed. Furthermore, most
existing CE methods focus on altering predictions rather
than optimizing a decision objective, even though real-world
decision-making often requires explicit objective maximization.
To address these limitations, we formulate CE as a profit
maximization problem in management and marketing contexts
and propose a framework termed profit-based counterfactual
explanation (PBCE). PBCE eliminates the need for exogenous
target specification by directly maximizing profit as the primary
optimization objective. Concurrently, the distance term is rein-
terpreted as the cost of modifying product attributes, providing
a clear and economically grounded interpretation.
I. INTRODUCTION
Applications of artificial intelligence (AI) and machine
learning have been rapidly expanding across a wide range
of fields. In particular, machine-learning-based prediction
and control methods are increasingly utilized in domains
such as economics, healthcare, and marketing. Despite their
strong predictive performance, many machine learning mod-
els possess highly complex internal structures and are often
regarded as black-box models, in which the reasoning behind
the predictions is not explicitly interpretable. Consequently,
understanding why a particular prediction was made, or how
decision-makers should respond to it, is often difficult.
Therefore, considerable research has been focused on
improving the interpretability and explainability of machine
learning models [1]. Many approaches have been proposed
for extracting human-interpretable information from black-
box models. Counterfactual explanations (CE) have emerged
as a prominent framework for explaining individual predic-
tions [2]–[4]. The basic concept of CE is as follows: Given a
trained machine learning model and the predicted value for a
specific instance, the CE identifies how explanatory variables
should be modified to move the predicted outcome toward a
* Research supported by JSPS KAKENHI Grant-in-Aid for Scientific
Research.
1K. Kinjo is with the Faculty of Business Studies, Kyoritsu
Women’s University, 2-2-1, Hitotsubashi, Chiyoda-ku, Tokyo,
101-8437, Japan (corresponding author; phone: +81-3-3237-2159;
kkinjo@kyoritsu-wu.ac.jp)
2T. Ebina is with the School of Commerce, Meiji University,
1-1, Kanda-surugadai, Chiyoda-ku, Tokyo, 101-8301, Japan
ebina@meiji.ac.jp
desired target value. Simultaneously, a constraint is typically
imposed to ensure that the modified explanatory variables do
not deviate excessively from their original input values. This
is usually implemented by minimizing the distance between
the original and counterfactual inputs. In other words, the CE
problem is formulated as finding counterfactual instances that
jointly minimize prediction loss with respect to the target
value and distance from the original input. By presenting
counterfactual examples, CE enables users to identify ex-
planatory variables that play an important role in generating
predictions. The concept of CE is also closely related to
algorithmic recourse and has theoretical connections with
research on adversarial example generation [4]. A wide range
of CE methods have been proposed, differing in model type
(e.g., differentiable vs. non-differentiable models), extraction
strategy, data format (e.g., tabular, image, or text data),
and design objectives such as actionability, plausibility, and
fairness [4], [5].
Despite these technological advances, several important
challenges remain for the CE framework. The first is the
issue of specifying a target value exogenously. In classifi-
cation problems, a natural objective is defined by flipping
a predicted label. In contrast, in regression settings, the
appropriate target value is not clearly defined. Although
many studies have assumed that the target value is given
exogenously, the practical validity of this assumption has not
yet been sufficiently discussed. Second, there is the issue
of interpreting distance functions. In CE, minimizing the
distance between the original and counterfactual input is
common [6], as this is assumed to improve the acceptability
and feasibility of the explanation [7]. However, the distance
function is typically defined exogenously, for example, using
the Euclidean distance, and its correspondence with the
real-world cost of modifying explanatory variables is often
unclear. Third, most existing CE studies focus primarily on
how predictions can be altered rather than on what decisions
should be optimized. In practical decision-making contexts,
defining an appropriate objective function and optimizing
it is often more important than merely moving predictions
toward a particular target value.
Motivated by these issues, this study addresses the fol-
lowing research question: How can CEs be formulated to
directly support profit-oriented managerial decision-making?
To answer this question, focusing on product strategy in
marketing, we reformulate the CE computation problem as a
profit-maximization problem and propose a framework called
profit-based counterfactual explanation (PBCE).
This study makes three contributions. First, we avoid the
arXiv:2607.01610v1  [cs.AI]  2 Jul 2026

exogenous specification of target values in the CE by intro-
ducing a framework in which profit maximization is treated
as the primary objective. That is, the strategic variables are
adjusted to maximize profits, eliminating the need to specify
the external target of the dependent variable. Second, we ad-
dress the arbitrariness of the distance function by interpreting
it as the cost associated with changes in product attributes.
This interpretation provides an economically meaningful rep-
resentation of the mathematical distance measures commonly
used in CE methods and enables the feasibility of counterfac-
tual solutions to be evaluated from an economic perspective.
Third, we conduct theoretical and empirical analyses to vali-
date the proposed approach. Specifically, we derive analytical
solutions through theoretical analysis, perform numerical
validation through simulations, and conduct an empirical
analysis using data from the Japanese manga market. These
analyses demonstrate the validity of the proposed method
and provide practical managerial implications.
Tsirtsis and G ´omez-Rodr´ıguez (2020) formulated CE as
a strategic interaction between a decision-maker and an ex-
plainee and proposed a theoretical model that simultaneously
optimizes explanation strategies and policies [8]. In their
framework, the distance function was interpreted as effort
cost. By contrast, this study reformulates CE within a profit-
maximization framework in management and marketing, ex-
plicitly providing an economic interpretation of both distance
and cost. The remainder of this paper is organized as follows:
Section II presents the formulation of the problem. Section
III provides a theoretical analysis. Section IV describes
the proposed method and the empirical analysis. Section V
discusses the results and outlines the directions for future
research.
II. PROBLEM SETTING
In contrast to conventional CE methods that require an
exogenously specified target value, PBCE reformulates CE
as a profit-maximization problem under the following general
setting.
(x∗ n, p∗ n)∈argmax xn, pn pnf(x n, pn)−c(f(x n, pn))−ccg(xn, xb n).
Letx n = (x n,1, . . . , xn,K )∈R K (n= 1,2, . . . , N)
denote the product attributes of productn, whereNis
the number of products andKis the number of product
attributes. Letx b n = (x b n,1, . . . , xb n,K )∈R K denote the
baselineK-dimensional product attribute vector.x n is a
counterfactual version of the baseline attribute vectorx b n.
The variablep n ∈R + denotes the price, a one-dimensional
scalar. We assume a monopolistic market structure that serves
as a natural starting point for a profit-based CE analysis.
Functionfpredicts the quantity demandedy n based
on pricep n and product attributesx n, and is esti-
mated using machine learning methods. Specifically,f
is trained on datasetD={Y, X, P}, which com-
prisesNone-dimensional demand observationsY=
{y1, y2, . . . , yN },N K-dimensional product attribute vec-
torsX={x 1, x2, . . . , xN }, andNone-dimensional prices
P={p 1, p2, . . . , pN }. We assume thatf(x n, pn)decreases
monotonically inp n, that is,f pn (xn, pn)<0. Although
exceptions may exist in practice, this assumption is motivated
by theoretical consistency and well-established empirical
findings on the law of demand. One possible exception is
that a higher price may signal higher quality and stimulate
demand. In the manga market, however, quality signals are
primarily conveyed through reputation, serialization venue,
and reader reviews rather than price, and manga volumes
are priced within a narrow, standardized range; the signaling
effect is therefore unlikely to be dominant, making the
monotonicity assumption a reasonable approximation in this
context.
Functioncdenotes the production cost as a function of
demandf(x n, pn), and is assumed to be monotonically
increasing, i.e.,c ′(·)>0. The functionc cg represents the
adjustment cost for changing product attributes from the
baselinex b n tox n, and can be specified using a distance
function. For example, the sum of the squared differences,
or more generally, the weighted Minkowski distance, can be
employed. Such formulations are equivalent to incorporating
attribute-specific adjustment costsc k ≥0, where the non-
negativity ensures that the modification cost is economically
well-defined. The two canonical specifications are as follows.
ccg(xn, xb n) =
KX
k=1
ck(xn,k −x b n,k)2,(S1)
ccg(xn, xb n) =
 KX
k=1
ck|xn,k −x b n,k|q
!1/q
.(S2)
This study considers a setting in which a monopolistic firm
sells its products through online stores or similar channels.
In such an environment, the cost of price adjustment is
substantially lower than that of modifying other product
attributes. Accordingly, the adjustment cost functionc cg
incorporates only non-price attributes and excludes price
from the change cost.
III. THEORETICAL ANALYSIS
In this section, we present the theoretical analyses. For
simplicity, we assume that product attributex n is one-
dimensional to gain analytical tractability while preserving
the essential economic structure. We derive the solution
under different model specifications and characterize its key
properties. To simplify the notation throughout this section,
we writex n asx,p n asp, andx b n asx b.
A. General Model
Let the product attribute bex∈R +, the price bep∈R +,
and the demand quantity beQ∈R +. Letf(x, p)denote the
demand function (predictive model) as defined in Section II,
c(f(x, p))denote the production cost as a function of output
(cf. Section II), andc cg(x, xb)denote the adjustment cost
based on the distance from the baseline attributex b ∈R +.
We define the firm’s profit function as
Π(x, p) =p f(x, p)−c(f(x, p))−ccg(x, xb).

If the profit functionΠis strictly concave onX×P, the
solution(x ∗, p∗)to the maximization problem is unique.
A sufficient condition for uniqueness is that the stationary
point(x ∗, p∗)is unique and the Hessian matrixHis negative
definite onX×P.
Accordingly, in addition to satisfying the first-order con-
ditions,
(
Πx = [p−c ′(f)]f x −c cg,x = 0,
Πp =f+ [p−c ′(f)]f p = 0,
it is sufficient for the Hessian matrixHto satisfy the second-
order condition of negative definiteness, where
H=∇ 2Π(x, p) =
Πxx Πxp
Πpx Πpp

.
Here, the second-order partial derivatives are given by
Πxx = [p−c ′(f)]f xx −c ′′(f)(f x)2 −c cg,xx,Π px = Πxp =
(1−c ′′(f)f p)f x + [p−c ′(f)]f xp, andΠ pp = 2f p + [p−
c′(f)]f pp −c′′(f)(f p)2. In this case, the following conditions
hold: (
Πxx <0,
det(H) = Π xxΠpp −Π pxΠxp >0.
Even whenxisK-dimensional, the maximization problem
can be solved similarly if the corresponding Hessian matrix
is negative definite.
Remark 1 (Marketing Interpretations).First, consider price
optimality given byΠ p = 0.c ′(f)represents the marginal
production cost when output increases by one unit. Ac-
cordingly,[p−c ′(f)]denotes the price-cost markup. The
optimal price equates the marginal revenue gain from a
unit price increase, captured byf, to the marginal revenue
loss from the induced reduction in demand, represented by
[p−c ′(f)]f p. Second, consider attribute optimality given by
Πx = 0.[p−c ′(f)]f x represents the marginal revenue from
a unit increase in the product attribute, whilec cg,x denotes
the corresponding marginal adjustment cost. Therefore, the
optimal attribute level is determined by equating marginal
revenue with marginal adjustment cost.
B. Linear Model
Next, we derive an optimal solution using a linear model
specification. Specifically, we assumeQ=f(x, p) =α+
βx−γp,c(f(x, p)) =δ f(x, p), andc cg(x) =η(x−x b)2
(based on S1). Without loss of generality, we imposeα/γ >
δ≥0,γ >0,β >0,η >0. To ensure that the Hessian
matrix is negative definite, we additionally assumedet(H) =
4γη−β 2 >0. Under these assumptions, the profit function
is given by
Π(x, p) =p(α+βx−γp)−δ(α+βx−γp)−η(x−x b)2.
SettingΠ p = 0givesp(x) = (α+βx+γδ)/(2γ), and
Πx = 0givesx(p) =x b +β(p−δ)/(2η); substituting these
into each other yields the solution below.
Solving this maximization problem yields
p∗ =δ+ 2η(α+βx b −γδ) 4γη−β 2 , x ∗ =x b+ β(α+βx b −γδ) 4γη−β 2 .
In this case, the optimal quantity is
Q∗ ≡Q(p ∗) = 2γη(α+βx b −γδ) 4γη−β 2 ,
and the optimal profit is
Π∗ ≡Π(x ∗, p∗) = η(α+βx b −γδ) 2
4γη−β 2 .
These closed-form expressions show that the optimal price
p∗ is obtained by adding2η(α+βx b −γδ)/(4γη−β 2)
to the marginal costδ, whereas the optimal attributex ∗ is
obtained by addingβ(α+βx b −γδ)/(4γη−β 2)to the
baselinex b. Both adjustments share the common factor(α+
βxb −γδ)/(4γη−β 2), whose magnitude is governed by the
model parameters.
IV. EMPIRICAL ANALYSIS
As discussed in Section III, when a simple linear model
is assumed, an optimal solution can be derived analytically.
However, obtaining a closed-form solution is difficult for
general nonlinear models or models with interaction effects.
Therefore, we propose a method to estimate a black-box
nonlinear machine-learning model from the observed data
and derive the corresponding PBCE.
A. Empirical Methods
The proposed method proceeds in the following two steps.
(i)Estimation and comparison off:We first estimate the
demand functionfusing the datasetD={Y, X, P}.
To do so, monotonicity has to be imposed on the price
variablep n. One possible approach is to estimatef
using standard regression methods. However, such ap-
proaches may be insufficient when complex nonlinear
relationships and interaction effects are present among
variables. Therefore, we employ machine learning mod-
els that enable explicit monotonicity constraints, such
as constrained monotonic neural networks (CMNNs)
[9]. The predictive performance of the estimated mod-
els is evaluated and compared using metrics for con-
tinuous outcomes, such as mean squared error (MSE).
(ii)Derivation of optimalx n andp n:Given a baseline
product attribute vectorx b n, we derive the optimal price
and product attributes by solving a constrained non-
linear optimization problem. Standard numerical opti-
mization algorithms, such as sequential least-squares
programming (SLSQP) and trust-region constrained
methods, can be employed for this purpose. When ana-
lytical partial derivatives are available, they are used to
improve computational efficiency; otherwise, numerical
differentiation is applied. The optimization problem
may admit multiple local optima; hence, the procedure
is repeated with multiple initial values, and the solution
that yields the highest profit is selected. Deriving CEs
for the different values ofx b n and comparing their
distributions and summary statistics enable the iden-
tification of variables that are consistently important
across multiple cases.

B. Evaluation Methods
In the CE literature, various evaluation metrics have been
proposed, includingValidity, which measures how close a
counterfactual outcome is to a predefined target value, and
Proximity, which captures the distance between an original
instance and its CE [2]. However, the proposed approach
is not intended for evaluation solely in terms of target-
oriented validity. Accordingly, for the PBCE, we introduce
the following evaluation metrics and assess the proposed
method based on them.
Profit:We evaluate PBCE using the achieved profitπ n
and its average across instances. Higher values of the optimal
profitπ n indicate better performance. Additionally, we report
the corresponding optimal product attributesx ∗ n, pricesp ∗ n,
and predicted demandy ∗ n as reference values.
Dissimilarity:Dissimilarity operationalizes Proximity as
the squared Euclidean distance of the changes in non-price
attributes,diss= P k(x∗ n,k −x b n,k)2, reported without
the cost coefficient and consistent withc cg; smaller values
indicate more desirable (lower-cost) CEs. As reference in-
formation, we also examined the magnitude and direction
of changes in the decision variables, includingx ∗ n −x b n and
p∗ n −p b n.
Mean Absolute Error (MAE):In settings such as simu-
lation studies, where the optimal values ofx ∗ n,p ∗ n, andπ ∗ n
can be computed analytically, we evaluate the accuracy of the
proposed numerical optimization method using the mean ab-
solute error (MAE). This evaluation enables the assessment
of the closeness of the numerical solutions to the theoretical
optima. Specifically, we definediff optx=|¯x ∗ n −x ∗ n|,
diff optp=|¯p ∗ n −p ∗ n|, anddiff optπ=|¯π ∗ n −π ∗ n|, where
the overbar denotes the theoretical optimal values.
C. Experiment
We validate the method proposed in Section IV-A in two
stages: a simulation study and a real-data application. In the
simulations, we assess whether the method could recover the
theoretical optimum. We then apply it to real-world data.
1) Simulation Data:In this simulation, the explanatory
variablesx n and the pricep n (≥0)are generated from a
uniform distribution on[0,1]. This normalization places all
variables on a common scale, which facilitates the compa-
rability of the adjustment magnitudes and distance functions
in CEs. Notably, this range is purely a scaling choice for
data generation and does not represent economically feasible
domains. Therefore, optimal solutions may lie outside this
interval. The error termε n is assumed to follow a standard
normal distribution,N(0,1). Using the model specified
below, we generate the outcome variabley n and construct
the datasetD={Y, X, P}. A total of 5,000 samples are
generated. We further assume that the firm does not optimize
xn andp n with respect to profits prior to the simulation.
yn = 3 + 2xn −p n + 0.05εn.
Using datasetD, we estimate the demand functions using
both linear regression (LR) and machine learning (ML)
approaches. We then compare the predictive performances
TABLE I
COMPARISON OFMODELPREDICTIVEACCURACY
Model MSE MAE
Linear regression 0.003 0.040
CMNN(2,2) 1.785 1.013
CMNN(3,2) 0.154 0.281
CMNN(4,2) 0.421 0.439
CMNN(2,3) 0.334 0.436
CMNN(3,3) 0.319 0.379
CMNN(4,3) 0.072 0.213
CMNN(2,4) 0.312 0.424
CMNN(3,4) 0.166 0.303
CMNN(4,4) 0.511 0.463
TABLE II
SUMMARYSTATISTICS OFCES(LR)
xn pn yn πn x∗ n −xb n p∗ n −pb n diss
count 50 50 50 50 50 50 50
mean 0.424 0.424 3.302 0.069 0.186 1.813 0.036
std 0.279 0.279 0.639 0.910 0.031 0.426 0.012
min 0.001 0.001 2.088−1.941 0.139 0.946 0.019
max 0.978 0.978 4.782 1.818 0.248 2.836 0.061
x∗ n p∗ n y∗ n π∗ n
count 50 50 50 50
mean 0.610 2.359 1.860 3.197
std 0.310 0.310 0.310 1.060
min 0.140 1.888 1.389 1.735
max 1.225 2.974 2.476 5.513
of LR and CMNNs with different hyperparameter settings
(e.g., CMNN(3,2): two hidden layers with three and two
units) using MSE (Table I). For reference, we also compute
the MAE. Predictive performance is evaluated using 5-fold
cross-validation (CV) on the full dataset; the reported MSE
and MAE values in Table I represent the averages across the
five folds. Among the ML models, the architecture with the
lowest CV MSE is selected.
The results show that LR achieved the best predictive
performance overall, whereas among the CMNN models,
architectures with four and three hidden layers yielded the
lowest prediction errors.
We next compute CEs. The cost functions arec(Z) =
0.5Zandc cg(xn, xb n) = 10(x n −x b n)2, and the CEs were
derived based on these cost settings. We use 15 random ini-
tializations with SLSQP; the maximum number of iterations
(30) serves as the convergence criterion, with the default
SLSQP tolerance otherwise applied. No attribute bounds are
imposed.
We compare the distributions of the original estimated
variablesx n,p n,y n, andπ n with those of their counterfac-
tual counterpartsx ∗ n,p ∗ n,y ∗ n, andπ ∗ n. We also examine the
differences from the baseline values, including|x ∗ n −x b n|and
|p∗ n −p b n|, to assess the magnitude of the changes induced by
the counterfactual solutions (Table II; LR-based; cf. Table III
for ML-based).
The PBCE achieves profit improvements for many prod-
ucts with relatively limited attribute adjustments. The average

TABLE III
SUMMARYSTATISTICS OFCES(ML: CMNN)
xn pn yn πn x∗ n −xb n p∗ n −pb n diss
count 50 50 50 50 50 50 50
mean 0.424 0.424 3.303 0.081 0.207 1.476 0.066
std 0.279 0.279 0.710 0.911 0.154 0.632 0.081
min 0.001 0.001 1.840−1.899−0.197 0.600 0.000
max 0.978 0.978 4.679 1.922 0.660 2.990 0.436
x∗ n p∗ n y∗ n π∗ n
count 50 50 50 50
mean 0.631 2.022 2.302 2.798
std 0.331 0.717 0.717 1.303
min 0.144 1.023 0.496 1.157
max 1.493 3.214 3.693 6.260
squared attribute change (diss= 0.036) is small, suggesting
that profit gains can be realized without large modifica-
tions (mean change inx: 0.186). Profit improvements are
achieved primarily through price adjustments, and profitπ n
can vary considerably. In many cases, the counterfactual
profit satisfiesπ ∗ n ≥π n, with the maximum counterfactual
profit reachingπ ∗ n = 5.51. Moreover, the results indicate a
structure in which profits increase even when sales volumes
decrease. In many cases,y ∗ n is lower than the original
value. This finding implies that firms that do not apply this
CE-based optimization tend to overproduce their quantities.
Instead, profit maximization can be achieved by reducing
sales volumes and raising prices, thereby increasing the
margin per unit. From a marketing perspective, this indicates
that profit maximization does not necessarily require sales
maximization. Although some firms pursue sales volume or
market share maximization as their primary objective (e.g.,
[10]), the present results suggest that such strategies may not
always be consistent with profit maximization. We discuss
this point further in Section V .
Table III reports the summary statistics of the PBCE
derived from the demand function estimated using the ML
model. The average attribute change induced by CE is mod-
erate (mean = 0.207), indicating that profit improvements
require both price and attribute adjustments. The average
price change is 1.476, suggesting that price remains the most
influential decision variable. The average squared attribute
change (diss) is small (0.066), indicating that ML-based
CEs propose realistic and feasible levels of change. When
we examine the optimal solutions after applying CE, the
minimum profit increases dramatically to 1.157, compared
with−1.899in the original data, implying a substantial re-
duction in downside profit risk. The maximum profit reaches
6.260, exceeding the original maximum profit of 4.679.
Although sales decrease on average, an increase in unit price
contributes to higher profits. Compared with the LR-based
CEs, the ML-based CEs exhibit smaller price adjustments
(mean = 1.476 vs. 1.813). Finally, to assess deviations from
the theoretical optimum, we compare the summary statistics
ofdiff optx,diff optpanddiff optπ, which measure
the absolute differences between the theoretical optimal
TABLE IV
SUMMARYSTATISTICS OFDIFFERENCESBETWEENTHEORETICAL AND
NUMERICALOPTIMALCE SOLUTIONS
LR ML
diffpdiffxdiffπdiffydiffpdiffxdiffπdiffy
count 50 50 50 50 50 50 50 50
mean 0.0014 0.0000 0.0028 0.0003 0.468 0.114 0.547 0.598
std 0.0001 0.0000 0.0001 0.0002 0.333 0.105 0.437 0.447
min 0.0012 0.0000 0.0024 0.0000 0.007 0.006 0.029 0.004
max 0.0015 0.0001 0.0028 0.0006 1.379 0.434 1.795 1.584
values and the corresponding numerically obtained solutions
(Table IV).
The LR model yields near-zero average differences from
the theoretical optima ( diff p= 0.0014, diff x≈0,
diff π= 0.0028), confirming that the proposed numerical
optimization accurately recovers the analytical solution. By
contrast, the ML (CMNN) model exhibits larger differences
(diff p= 0.468, diff π= 0.547). This is expected: the theo-
retical optimum is derived from the linear model parameters,
whereas the CMNN numerical solution reflects a different
nonlinear model structure. Accordingly, the ML differences
quantify model divergence rather than optimization error.
Overall, these results demonstrate that the proposed PBCE
accurately recovers the analytical optimum when a correctly
specified demand model is used. The near-zero LR differ-
ences confirm the validity of the numerical procedure, while
the larger ML differences reflect inherent model misspecifi-
cation relative to the linear theoretical benchmark.
2) Real Data:Next, using data on manga (Japanese
comics) sales volumes, prices, and other attributes in Japan,
we examine how each manga title can be modified to achieve
higher profits. We assume that product attributes remain
constant over the publication period of each manga series.
For empirical data, we collected the top 206 manga titles in
terms of cumulative sales in Japan as of 2023 [11]. Two titles
were excluded due to missing attribute data, yielding a final
sample of 204 observations. The sample size is limited by
the availability of publicly accessible sales information, and
the dataset is relatively small for machine learning analysis;
therefore, the results should be interpreted with caution
because of the potential risks of overfitting and estimation in-
stability. From these data, we computed an approximate per-
volume sales figure by dividing the cumulative sales of each
manga by the number of volumes published and using this
value asY. This procedure implicitly assumes that sales are
uniformly distributed across volumes. In practice, earlier vol-
umes tend to sell more copies than later volumes. However,
this is a simplifying assumption, providing a tractable and
consistent measure of average commercial performance at the
series level, which is the unit of analysis in this study. Next,
based on the total price of all newly published print volumes
and the number of volumes, we calculate the approximate
average price per volume, which is used asP. Finally, as
an explanatory variableX, we employ the eight attributes
listed below. Manga inherently contains rich information at
the episode level and exhibits complex sequential structures

across episodes. However, as quantifying such information in
a consistent and comparable manner is difficult, this study
focused on work-level attributes related to the overall visual
elements and story characteristics of each manga title. This
issue will be discussed in the following section. The eight
attributes are as follows.
(1) Number of years since first publication. This vari-
able is constructed based on the year the manga was first
published. (2) Serialization of the manga in theWeekly
Shonen Jump. TheWeekly Shonen Jumpis the most popular
weekly manga magazine in Japan; a large share of top-
selling manga titles have been serialized in this magazine.
Therefore, we include this attribute. (3–5) Three feature
vectors related to manga’s visual characteristics. For each
manga title, five images are collected using an image search
engine, excluding non-manga images. These images are
then embedded using a Vision Transformer (ViT), resulting
in 768-dimensional feature vectors [12]. We subsequently
apply principal component analysis (PCA) and reduce the
dimensionality to three components selected based on scree
plots and semantic interpretability. The resulting visual com-
ponents are interpreted as follows (Table V):vit1represents a
spectrum from dramatic (high values: cinematic and intense
visual styles) to gentle (low values: everyday and soft visual
styles).vit2captures a range from realistic (high values:
greater realism and stronger shading) to cartoonish (low
values: deformation and a simplified style).vit3reflects a
continuum ranging from a stylized appearance (high values:
mature and fashionable style) to youthful characteristics
(low values: youthfulness and cuteness). (6–8) Three feature
vectors related to the story and building characteristics. Using
textual data, we construct three features based on story
descriptions. Specifically, we extract the English-language
summaries of each manga from MyAnimeList [13]. These
texts are embedded using BERT, yielding 768-dimensional
vectors [14]. We then apply PCA to these embeddings and
compress them into three components that are selected based
on scree plots and semantic interpretability. Based on the
interpretation of high-loading examples, the textual compo-
nents are defined as follows (Table VI):bert1represents a
spectrum ranging from heroic (high values: battles, death,
fate, and extraordinary events) to mundane (low values: ev-
eryday life, humor, and family).bert2captures a continuum
from masculine (high values: social roles and occupations)
to emotional (low values: emotions and aesthetics).bert3
reflects a range from epic (high values: history, fantasy, and
mythology) to contemporary (low values: modern settings,
youth, and school life). PCA is conducted independently
for the visual and textual features. As these features belong
to different representational spaces, their variance structures
are not directly comparable, reflecting the differences in the
amount and nature of information captured by each modality.
Tables VII and VIII report the summary statistics for the
dependent and explanatory variables, respectively.
Predictive accuracy is evaluated using 5-fold CV . Prior
to model fitting, all explanatory variables are standardized
to zero mean and unit variance for model input only; the
TABLE V
TOP ANDBOTTOMVALUES OFFEATUREDIMENSIONS(VIT)
Title vit1 Title vit2 Title vit3
Fist of the North Star 1.948 Record of Ragnarok 1.009 Coffee & Vanilla 1.723
Toriko 1.644 Black Butler 0.981 Initial D 1.484
Eyeshield 21 1.642 Yamikin Ushijima-kun 0.972 The King of Minami 1.040
Dragon Ball 1.507 Terra Formars 0.953 GANTZ 0.989
Kinnikuman 1.471 Vagabond 0.933 BLEACH 0.963
Video Girl Ai−1.455 Crayon Shin-chan−1.131 To Love-Ru−0.880
Atashin’chi−1.464 Kochikame−1.146 Honey Lemon Soda−0.927
His and Her Circumstances−1.501 Sazae-san−1.206 Ao Haru Ride−0.973
Animal Doctor−1.525 High School! Kimengumi−1.305 The Quintessential Quintuplets−1.001
Chibi Maruko-chan−1.556 Tsuribaka Nisshi−1.326 Rurouni Kenshin−1.017
TABLE VI
TOP ANDBOTTOMVALUES OFFEATUREDIMENSIONS(BERT)
Title bert1 Title bert2 Title bert3
GANTZ 5.608 The King of Minami 5.443 D.Gray-man 5.030
Seraph of the End 5.029 Ranma 1/2 5.348 Sukeban Deka 4.308
Tokyo Ghoul 4.880 Rokudenashi BLUES 5.298 Nausica ¨a of the Valley of the Wind 3.934
NARUTO 4.857 Yu-Gi-Oh! 5.245 Romance of the Three Kingdoms 3.725
Maison Ikkoku 4.590 Animal Doctor 4.619 Record of Lodoss War 3.701
Y AW ARA!−6.113 Urusei Yatsura−3.713 Play Ball−3.210
Asari-chan−6.151 The Rose of Versailles−3.736 Silver Spoon−3.319
Sazae-san−6.393 Tenjho Tenge−4.138 Ao Haru Ride−3.405
Osomatsu-kun−6.496 ONE PIECE−4.236 H2−3.426
Kaguya-sama: Love Is War−6.722 Record of Ragnarok−4.354 Itazura na Kiss−3.468
optimization and cost function operate on the original scale.
CMNN training uses a batch size of 16, a maximum of
100 epochs, and early stopping (patience of 5 epochs) to
prevent overfitting. The CMNN with the lowest CV MAE
is selected as the base model for CE derivation. Table IX
reports the predictive accuracy of the LR and several CMNN
models. According to the MSE and MAE metrics, the LR
exhibits the smallest errors, indicating a strong fit between
the linear model and the data. Among the CMNN mod-
els, CMNN(5,5,5) achieves the best performance (MSE =
26382.287, MAE = 94.791), with error levels close to those
of LR. This result suggests that the relationship between
the variables is approximately linear, although the relatively
small sample size (N= 204) may also limit the performance
of more flexible machine learning models. However, the
CMNN models achieve comparable predictive accuracies.
In the context of the PBCE, employing models that satisfy
economic constraints, such as a monotonic decrease in de-
mand with respect to price, is particularly important. CMNNs
can directly incorporate the monotonicity constraints. Al-
though their prediction errors are slightly larger than those
of LR, CMNNs offer the advantage of balancing economic
consistency and model flexibility. Therefore, in this study,
we adopt the CMNN(5,5,5) as the base model for CE,
as it preserves theoretical consistency while maintaining a
sufficiently high predictive accuracy.
We now derive the CEs. For simplicity, the cost functions
are specified asc(Z) = 10Zandc cg based on S1 with a
common coefficientc k = 500for allk, givingc cg(xn, xb n) =
500 PK k=1(xn,k −x b n,k)2. We use 5 random initializations
with SLSQP; the maximum number of iterations (30) serves
as the convergence criterion, with the default SLSQP tol-
erance otherwise applied.yearandjumpare held fixed
via equality constraints; PCA-based features are bounded to
[−3,3]; and price is left effectively unconstrained. We now
turn to the results of the CEs (Table X). In Tables X and XI,
basedenotes the baseline value,cfthe counterfactual value,
diffthe difference (cf−base), anddemandthe predicted

TABLE VII
SUMMARYSTATISTICS OF THEDEPENDENTVARIABLE
circ num volume price per num per price
count 204 204 204 204 204
mean 4067.775 29.711 18627.931 169.861 741.177
std 5468.118 29.628 15896.025 156.789 477.643
min 1000 1 748 12.200 104.500
max 50000 211 121508 1000.000 5280.000
TABLE VIII
SUMMARYSTATISTICS OF THEEXPLANATORYVARIABLES
year jump vit1 vit2 vit3 bert1 bert2 bert3
count 204 204 204 204 204 204 204 204
mean 26.279 0.265−0.006 0.009−0.004 0.000 0.000 0.000
std 14.670 0.442 0.791 0.505 0.457 2.898 2.140 1.747
min 4 0−1.556−1.326−1.017−6.722−4.354−3.468
max 78 1 1.948 1.009 1.723 5.608 5.443 5.030
demand.
Case 1: Naruto.For Naruto, CE shifts the visual style
toward realism and strong shading (vit2) and strengthens
epic elements (bert3), increasing both demand and profit.
In practice, thevit2shift suggests enhancing shading and
anatomical detail—adjustments feasible at the character-
design and panel-composition stages.
Case 2: Doraemon.For Doraemon, CE adjusts visual fea-
tures toward more dramatic and realistic styles (vit1,vit2) and
shifts the narrative toward social and contemporary themes
(bert2,bert3), also modifying price. Compared with Naruto,
Doraemon requires adjustments across a larger number of
elements. In practice, thebert2andbert3shifts suggest
foregrounding everyday social interactions and contemporary
settings—achievable through scenario selection.
Across all titles, ViT-based features shift toward greater
realism (vit2) and stylized designs (vit3), while BERT-
based features strengthen heroic (bert1) and epic (bert3)
themes (Table XI). Average demand increases and profit
improves from 94,612 to 97,603, confirming that PBCEs
identify profit-improving solutions through content-related
adjustments rather than exogenous conditions such as price
or publication information.
V. DISCUSSION
We propose a CE framework that reformulates profit
maximization as its primary objective, with a method for
deriving such explanations and tailored evaluation metrics.
Theoretical analysis provides analytical solutions character-
izing the key properties of PBCE. Simulation results confirm
that the method recovers solutions close to the theoretical
optima, and real-data analysis yields practically meaningful
managerial insights.
In the literature on CEs and algorithmic recourse, the
dominant approach is to generate counterfactuals that achieve
the desired output, while distances are either exogenously
specified or interpreted as effort or adjustment costs [4],
[8]. Moreover, when regression or continuous outcomes
are considered, the choice of target value is often deter-
mined exogenously (e.g., [2]). By contrast, our approach
TABLE IX
COMPARISON OFMODELPREDICTIVEACCURACY
Model MSE MAE
Linear regression 23502.243 96.080
CMNN(4,5,5) 31885.983 109.645
CMNN(4,5,6) 26368.902 96.237
CMNN(4,6,5) 26449.038 98.928
CMNN(5,5,5) 26382.287 94.791
CMNN(5,5,4) 27069.018 96.337
TABLE X
COUNTERFACTUALEXPLANATIONS FOR AREPRESENTATIVECASE
price year jump vit1 vit2 vit3
NARUTO
base 484.300 25 1 0.977−0.675 0.143
cf 484.296 25 1 0.903−0.518 0.174
diff−0.004 0 0−0.074 0.157 0.031
Doraemon
base 567.100 55 0−1.301−0.937−0.101
cf 567.208 55 0−1.232−0.862−0.122
diff 0.108 0 0 0.069 0.075−0.020
bert1 bert2 bert3 demand profit diss
NARUTO
base 4.857 3.519 0.733 158.700 75271.305
cf 4.894 3.493 0.856 162.040 76830.617
diff 0.037−0.027 0.123 0.048
Doraemon
base−3.269 2.837−0.759 120.898 67352.297
cf−3.261 2.961−0.954 123.424 68740.805
diff 0.008 0.124−0.195 0.064
directly maximizes profit as the primary managerial objec-
tive, thereby avoiding the problem of target specification.
Furthermore, by interpreting distances as costs associated
with changes in products, prices, or managerial actions, the
proposed profit-based CE provides explanations based on
the practical constraints of managerial decision making. This
finding resonates with the long-standing debate in marketing
that profit maximization does not necessarily require sales
maximization [10], [15]. The results provide a data-driven
illustration of this divergence, suggesting that firms oriented
toward sales or market share maximization may be forgoing
substantial profit gains.
This study has several limitations. First, there is the issue
of the robustness of CEs [16], namely, how robust the derived
CEs are to model misspecification, estimation errors, or
changes in the data-generating process. In this study, CEs
were extracted from a single predictive model; however,
more robust explanations can be obtained by deriving CEs
from multiple models and aggregating the results. Second,
the models employed do not guarantee causal relationships;
PBCEs are derived from predictive models and do not
directly represent intervention effects. Although predictive
models may capture certain causal patterns [17], explicit
causal modeling would further improve the reliability of
recommendations. Third, there is an issue of data bias. The
manga data analyzed in this study include many popular
titles and are concentrated in specific media outlets (e.g.,
serialization inWeekly Shonen Jump). Therefore, caution
should be exercised when generalizing these findings to other
media platforms or genres. In addition, visual and textual

TABLE XI
AVERAGECOUNTERFACTUALADJUSTMENTSACROSSALLTITLES
price year jump vit1 vit2 vit3
Total (avg)
base 741.177 26.279 0.265−0.006 0.009−0.004
cf 741.177 26.279 0.265−0.013 0.031 0.012
diff 0.000 0.000 0.000−0.007 0.022 0.016
bert1 bert2 bert3 demand profit diss
Total (avg)
base 0.000 0.000 0.000 128.251 94612.352
cf 0.032−0.015 0.009 132.232 97602.943
diff 0.032−0.015 0.009 0.078
features rely on data obtained from search engines and
MyAnimeList, making it difficult to fully eliminate potential
information bias.
Finally, we conclude by discussing possible extensions
and future research directions. First, the proposed method
applies to a wide range of goods (e.g., consumer products);
more rigorous estimation of adjustment costs from historical
data or expert judgment [18] would assess the feasibility of
recommended changes. A further extension would learn cost
functions from decision-making histories. Second, in this
study, no distance or adjustment cost was imposed on price
pn, based on the assumption that price changes are relatively
easy to implement, particularly in online settings (e.g., [19]).
However, in contexts such as printed books, where prices
are printed directly on products, or in brick-and-mortar
retail environments where price changes incur operational
costs, it is necessary to incorporate price adjustment costs.
This can be addressed by introducing a cost function of
the formc cg

(xn, pn),(x b n, pb n)  that explicitly incorporates
price changes. Third, the cost functions employed—linear
production costs and quadratic attribute adjustment costs—
represent one particular parametric specification. Alternatives
such as economies of scale in production or heterogeneous
attribute-specific adjustment costs would alter PBCE solu-
tions. Even under nonlinear production costs such as an S-
shaped cost curve, the qualitative result that a monopolist
equates marginal revenue (MR) with marginal cost (MC) is
preserved. Heterogeneous attribute adjustment costs would
concentrate recommended changes on lower-cost attributes,
yielding more targeted counterfactuals; examining such sen-
sitivity is an important direction for future research. Finally,
while the present analysis treats each manga title as a
single unit, future work could extend the framework to
episode-level analysis using text analysis and image features.
Extending the framework to oligopolistic or competitive
market structures constitutes another promising direction.
Such an extension requires modifying the demand function
to incorporate rivals’ prices and attributes, with Nash equi-
librium replacing the monopoly optimum as the solution
concept. Competition would generally be expected to lower
equilibrium prices and increase the distance between a firm’s
own product attributes and those of its rivals relative to
the monopoly benchmark, while the specific direction of
product-attribute adjustments would depend on the oligopoly
model structure, altering both the direction and magnitude of
PBCE-recommended adjustments.
ACKNOWLEDGMENT
This study was supported by the JSPS KAKENHI
Grants-in-Aid for Scientific Research (C) JP21K01468,
JP25K05082, and JP25K05381.
REFERENCES
[1] C. Molnar,Interpretable Machine Learning. Lulu.com, 2020.
[2] S. Verma, V . Boonsanong, M. Hoang, K. E. Hines, J. P. Dickerson, and
C. Shah, “Counterfactual explanations and algorithmic recourses for
machine learning: A review,”arXiv preprint arXiv:2010.10596, 2020.
[3] I. Stepin, J. M. Alonso, A. Catala, and M. Pereira-Fari ˜na, “A survey
of contrastive and counterfactual explanation generation methods for
explainable artificial intelligence,”IEEE Access, vol. 9, pp. 11974–
12001, 2021.
[4] A.-H. Karimi, G. Barthe, B. Sch ¨olkopf, and I. Valera, “A survey
of algorithmic recourse: Contrastive explanations and consequential
recommendations,”ACM Comput. Surv., vol. 55, no. 5, pp. 1–29, 2022.
[5] K. Kinjo, “Fair counterfactual explanation: Application to education,”
AI and Ethics, vol. 6, Art. no. 113, 2026.
[6] D. Lewis,Counterfactuals. New York, NY , USA: John Wiley & Sons,
2013.
[7] S. Wachter, B. Mittelstadt, and C. Russell, “Counterfactual explana-
tions without opening the black box: Automated decisions and the
GDPR,”Harvard J. Law Technol., vol. 31, no. 2, pp. 841–887, 2018.
[8] S. Tsirtsis and M. Gomez-Rodriguez, “Decisions, counterfactual ex-
planations and strategic behavior,” inAdv. Neural Inf. Process. Syst.,
vol. 33, pp. 16749–16760, 2020.
[9] D. Runje and S. M. Shankaranarayana, “Constrained monotonic neural
networks,” inProc. Int. Conf. Mach. Learn. (ICML), 2023, pp. 29338–
29353.
[10] W. J. Baumol,Business Behavior, Value and Growth. New York, NY ,
USA: Macmillan, 1959.
[11] Mangazenkan, “Rekidai total sales ranking.” [Online]. Available:
https://www.mangazenkan.com/r/rekidai/total
[12] A. Dosovitskiyet al., “An image is worth 16×16 words: Transformers
for image recognition at scale,” inProc. Int. Conf. Learn. Represen-
tations (ICLR), 2021.
[13] “MyAnimeList.” [Online]. Available:https://myanimelist.
net/
[14] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “BERT: Pre-
training of deep bidirectional transformers for language understand-
ing,” inProc. NAACL-HLT, 2019, pp. 4171–4186.
[15] J. S. Armstrong and F. Collopy, “Competitor orientation: Effects of
objectives and information on managerial decisions and profitability,”
J. Marketing Res., vol. 33, no. 2, pp. 188–199, 1996.
[16] J. Jiang, F. Leofante, A. Rago, and F. Toni, “Robust counterfac-
tual explanations in machine learning: A survey,”arXiv preprint
arXiv:2402.01928, 2024.
[17] J. D. Nichols and E. G. Cooch, “Predictive models are indeed useful
for causal inference,”Ecology, vol. 106, no. 1, Art. no. e4517, 2025.
[18] K. Rawal and H. Lakkaraju, “Learning recourse costs from pairwise
feature comparisons,”arXiv preprint arXiv:2409.13940, 2024.
[19] T. Ebina and K. Nishide, “Product repositioning with a Markov-
switching regime,”Ann Oper Res, vol. 355, pp. 2901–2937, 2025.
