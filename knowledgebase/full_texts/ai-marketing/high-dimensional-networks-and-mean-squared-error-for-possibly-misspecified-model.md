---
title: High-dimensional networks and mean squared error for possibly misspecified models
url: https://arxiv.org/abs/2608.13171
category: ai-marketing
subcategory: measurement
date: 2026-08
venue: ''
authors:
- Lourens Waldorp
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.13171
pages: 41
chars: 92866
fetched_at: '2026-11-08T13:29:41+00:00'
kb_version: 1
---

# High-dimensional networks and mean squared error for possibly misspecified models

High-dimensional networks and mean squared
error for possibly misspecified models
Lourens Waldorp
University of Amsterdam, Nieuwe Achtergracht 129-B, 1018 NP, the Netherlands
Abstract
To avoid missing important variables and their connections in networks, more and
more variables are included in network analysis. Here we show that in a setting with
many more parameters than observations (high-dimensional) it is possible to get a
conservative (i.e., low false positive rate) estimate of the neighbourhood for each
node (which connections are in the network). A neighbourhood is often estimated
with a linear model, and this leads to two interesting cases: (i) If the true model is
linear, then neighbourhood selection work reasonably well, and (ii) if the true model
is nonlinear, then neighbourhood selection requires a penalty for the high dimen-
sions. Here we show the impact of the ridge parameter on the mean squared error,
and how this leads to low test variance and hence to neighbourhoods with large
numbers of edges. We connect these insights with results from machine learning,
where the so-called double descent (when more parameters are included than obser-
vations, the mean squared error goes down a second time) has put the traditional
view on model selection upside down. Essentially, for adequate neighbourhood se-
lection in models with a large number of parameters, the volume of the model space
needs to be included in the penalty. Most neighbourhood selection methods (e.g.,
Lasso, AIC, BIC) lead to spurious edges (high false positive rate), but we prove
that in the high-dimensional setting, minimum description length leads to correct
neighbourhood selection or smaller (low false positive rates) in both cases when
either the model is correctly or incorrectly assumed linear.
Key words:model selection, double descent, bias-variance trade-off, mean squared
error, minimum description length
1 Introduction
Often we are concerned that the number of observations in a study is insuf-
ficient to warrant proper analysis using networks (Epskamp et al., 2018). In
Email address:waldorp@uva.nl(Lourens Waldorp).
arXiv:2608.13171v1  [stat.ML]  13 Aug 2026

particular, a network contains many possible connections and therefore many
parameters to be estimated. For instance, with 20 nodes, there are already 190
parameters for the edges in a network. In the classical statistical framework
we would need about 1000 observations to reliably estimate these parameters.
Recent advances have brought several estimation techniques that allow
for the so-called high-dimensional situation, where we have more edges than
observations (overparameterisation). Examples are the least absolute shrink-
age and selection operator (lasso, Tibshirani, 1996) and the ridge estimator
(Hoerl and Kennard, 1970; Rao, 1990). The lasso is popular because it simul-
taneously estimates and selects edges to a node (Waldorp and Haslbeck, 2024).
However, the lasso does not have a closed form solution and is discontinuous,
which makes standard inference problematic (although there are workarounds,
see e.g., B¨ uhlmann et al., 2014; Dezeure et al., 2015). In contrast, the ridge
estimator does have a closed solution and is continuous. This makes the ridge
estimate more amenable to analysis and allows for an analytical approach to
determine why generalisation is still possible in the over-parameterised regime.
The ridge estimate is constructed by adding independent dimensions to the
predictors so that a unique solution can be obtained (Hoerl and Kennard, 1970;
Rao, 1990). The solution is biased, but can relatively easily be used for infer-
ence (B¨ uhlmann, 2013). The ridge estimate can also be used for neighbourhood
selection, i.e., using Akaike and Bayes information criteria and minimum de-
scription length to obtain a reliable estimate of the neighbours of each node
in a network. Here we focus on reliable model selection for high-dimensional
linear models used to estimate the neighbourhood of any node in the network,
where the true edge relations are either linear or nonlinear.
We use the well-known nodewise regression (neighbourhood selection)
framework in graphical modelling (Lauritzen, 1996; Meinshausen and B¨ uhlmann,
2006; Jankova and van de Geer, 2017). In nodewise regression, the procedure
to find the nodes that are connected is completely local; each node is in turn
used as the dependent variable in a regression on all remaining nodes. For
each node, the objective is to identify the correct set of non-zero coefficients
(neighbours) from the (large) set of remaining nodes. Figure 1 shows three
graphs with different number of nodes (15, 32 and 320) from the perspective
of one node; the objective is to identify five non-zero edges in the space of
all other zero edges (sparse solution). When all nodes have been the focus of
a regression, all neighbourhoods can be ‘stitched’ together to form the entire
graph. For nodewise selection the objective is to select the correct neighbour-
hood or smaller but not larger (i.e., no false positive edges), because then, in
stitching together the entire graph, the number of false positive edges will be
high in large graphs.
To achieve this, we use recent work on the impact of estimation in the high-
dimensional setting on the mean squared error (MSE) in regression. Both in
Bartlett et al. (2020) and Hastie et al. (2022) the so-called ”ridgeless” es-
timator was used (see Section 2) to conclude that, surprisingly, the MSE
remains well behaved even in high dimensions. This implies that in princi-
2

15 nodes 32 nodes 320 nodes
Fig. 1. Graphs from the perspective of nodewise regression for graph sizes 15, 32
and 320. For any node there are five non-zero coefficients (blue edges), so that each
regression needs to identify among the remaining nodes the five non-zero coefficients.
ple it is possible to perform reliable neighbourhood selection in the high-
dimensional setting. Cheema and Sugiyama (2020) investigated the geometry
of high-dimensional models relating it to the impact of using a large parame-
ter space on model selection, concluding that when the large parameter space
of the overparameterised model is properly taken into account, then model
selection should work. Dwivedi et al. (2020) adapted minimum description
length, a model selection procedure, to be computationally efficient and reli-
able for large datasets. Other approaches, related to hypothesis testing, have
also been investigated in the high-dimensional setting (e.g., Meinshausen and
B¨ uhlmann, 2010; B¨ uhlmann, 2013; Shah and B¨ uhlmann, 2023). However, the
selection is based on false positive control by thresholding, which is often re-
solved by additional assumptions, such as independence for the familywise
error rate or false discovery rate (e.g., DasGupta, 2008).
Our contribution builds on these works and mostly on the work by Cheema
and Sugiyama (2020). Using linear neighbourhood selection, we leverage re-
sults about the impact of high-dimensional ridge estimation on MSE, and use
this to explain why overfitting (many parameters in linear models) can unex-
pectedly result in low MSE, causing problems for nodewise selection. Penal-
ties in the Akaike information criterion (AIC), for instance, are inadequate
and mostly select too many edges (overfit). But we prove that the penalty of
the minimum description length, as given in Gr¨ unwald (2007), in the high-
dimensional setting leads the correct neighbourhood or smaller, in both cases
when the true model for edge relation is linear or nonlinear.
We briefly explain the Gaussian graphical model in Section 2 and discuss
the problem of estimation in the high-dimensional setting. We describe that
ridge regression leads to a possible choice in obtaining a unique estimate in
high dimensions. Then in Section 3 we discuss mean squared error (MSE).
We show that the MSE remains low unexpectedly after the interpolation
point (where the number of parameters equals the number of observations).
This MSE behaviour is directly related to the ridge parameter, and we show
3

that the ridge solution is directly related to constraining the parameter space.
To achieve this, we discuss the MSE decomposition in Section 4 in terms of
squared bias and variance, also in the case of model misspecification. Then in
Section 5 we turn to model selection. Here we describe minimum description
length as an example where the geometry of the model space is taken into
account as a penalty, and prove that this will lead to correct neighbourhood
selection or smaller. In Section 6 we use simulations to confirm the theoretical
results of neighbourhood selection.
2 Estimation in the Gaussian graphical model
The Gaussian graphical model (GGM) is a Gaussian (normal) multivariate
distribution associated with a set of nodes and edges in a network. A nodej
in the network represents a Gaussian random variableX j, and an edge (i, j)
between two nodesiandjin the network represents a conditional dependence
relation between the two variablesX i andX j given all other variablesX k with
k̸=i, j.
The main characterisation in a GGM of conditional dependence is the
partial correlation (or partial covariance). That is why a GGM is sometimes
referred to as a partial correlation network. This characterisation makes sense
because whenever a partial correlation is 0, then the two variables are con-
ditionally independent (Lauritzen, 1996, Proposition 5.2) and so no edge is
present in the network; when a partial correlation is̸= 0, an edge is present
in the network. So, to construct a network we need to determine the 0 par-
tial correlations. Obtaining the partial correlations can be done by estimating
the inverse covariance covariance matrix by (penalised) maximum likelihood
(Friedman et al., 2008; Jankova and van de Geer, 2017).
The partial correlations can also be determined from regressions. This
is called neighbourhood selection or nodewise selection (Meinshausen and
B¨ uhlmann, 2006; B¨ uhlmann et al., 2014; Maathuis et al., 2018; Waldorp and
Marsman, 2021). This is because the regression coefficient is proportional to
the partial covariance. Hence, if the partial covariance is 0, then the regres-
sion coefficient must also be 0 (see Appendix A for details). Thus, determining
the GGM is reduced to a series of regressions, one regression for each node
regressed on allp−1 remaining nodes, with the objective of determining the
neighbourhood. Then, when all of the neighbourhoods have been determined,
they can be put together to make up the entire graph. We therefore discuss a
single regression, representing allpregressions for the entire graph, selecting
the nodes that are part of the neighbourhood of a node.
2.1 Nodewise regression
In nodewise selection, each node in turn is the dependent variable and the
remaining nodes are the independent or predictor variables. We call variable
4

Xi the dependent variable and denote it byYand the remaining nodes areX j
forj̸=i. In the scenarios we discuss we will be selecting a set of nodes that
are relevant to predictingY. We letJdenote the index set for the predictors
used in predictingY(which equalsX i) with a subset of the remaining nodes.
The setJnever contains the dependent variableY=X i (no self loops), so
thatJis a subset of{0,1, . . . , i−1, i+ 1, . . . , p}. We assume there is a true
subsetS, referred to as the support, such thatβ j ̸= 0 ifj∈Sandβ j = 0 if
j /∈S. To obtain the estimates ofβ j from the linear regression, we minimise
the least squares function
LS(J) =
nX
i=1
(Yi − ˆYJ )2 and ˆYJ = X
j∈J
Xj ˆβj.
For each model (subset)Jwe can obtain an estimate of the coefficients cor-
responding to the variablesx j such thatj∈J. By estimatingβ j we obtain
information on the neighbourhood of nodei: for anyβ j ̸= 0 we draw the edge
(i, j); and ifβj = 0, then there is no edge betweeniandj. We therefore require
estimates of theβ j withj∈J.
We can rewrite the model in matrix algebra, withY= (Y 1, Y2, . . . , Yn) the
n-dimensional vector,X= (X 1, X2, . . . , Xp) then×p-dimensional matrix and
β= (β 1, β2, . . . , βp),Y=Xβ. The least squares function can be written in
terms of the Euclidean distance function||a|| 2 =
q
a2 1 +a 2 2 +· · ·a2 p. The least
squares function is then LS(J) =||Y−Xβ J ||2 2. Minimisation is achieved from
the normal equations
X ⊤Xβ=X ⊤Y.(1)
Similar to numbers on the real lineR, we require that we can invertX ⊤Xso
that we obtain our estimate. For numbers on the real line we get forxb=c,
that we can invertxso thatb=c/x. Similarly, the inverse (X ⊤X) −1 has the
property that (X ⊤X) −1(X ⊤X) =I, where the identity matrixIis such that
IX=X. Then our least squares (LS) estimate is
ˆβLS = (X ⊤X) −1X ⊤Y.(2)
It is clear from this derivation that we need the inverse (X⊤X) −1. This assumes
that the rank (i.e., the number of linearly independent vectors inX) is at least
p. A necessary (but not sufficient) condition is thatp < n. For sufficiency we
also require that there is no collinearity (i.e., the eigenvalues ofX ⊤Xare all
positive). Given these assumptions, in the linear model the estimate ˆβLS is
unbiased (i.e.E( ˆβLS) =β S) and has smallest variance (i.e., var(ˆβLS)≤var(β S)
for any other estimateβ S). Good references for these results are, for instance,
Rao (1990) and Seber and Lee (2012).
5

2.2 Estimation whenp > n
We now know that in order to obtain an estimate ˆβwe require the inverse of
X ⊤Xto exist. Ifp > nthen this is not the case. As a consequence, there is no
unique solution (Pringle and Rayner, 1971; Searle, 1971; Schott, 1997). We can
understand this by considering the eigenvalues (spectrum) ofX ⊤X, denoted
byλ j. If thep×pmatrixX ⊤Xhas full rankp, then it haspeigenvaluesλ j >0
(Schott, 1997). IfX ⊤Xdoes not have full rank (because in our casep > n),
but has rankk, say, then there arep−keigenvalues equal to 0. This refers to
the idea that a part of the space spanned byX ⊤Xprojects on the null-space
(i.e., the space such thatX ⊤Xu= 0 for any vectoru̸= 0). Hence, there is no
unique solution whenX ⊤Xisp > n.
One way to obtain a unique solution is to impose constraints on the vector
β. One of the constraints is to impose an upper bound on the sum of absolute
values, i.e.,
P
j |βj| ≤c, for somec >0. Then the problem
min
β
||Y−Xβ|| 2 2 such that X
j̸=i
|βj| ≤c,
is called the least absolute shrinkage and selection operator, abbreviated by
lasso (Tibshirani, 1996). The lasso has several attractive properties, like se-
lecting the non-zero coefficients and consistency (i.e., converging withnto
the true value), given certain strong assumptions (see, e.g., Wainwright, 2009;
B¨ uhlmann and van de Geer, 2011; Hastie et al., 2015). The lasso has no closed
form solution and is not amenable to inference (P¨ otscher and Leeb, 2009;
B¨ uhlmann et al., 2014). However, several workarounds have been obtained,
like the debiased lasso (van de Geer et al., 2014; Waldorp and Haslbeck, 2024)
and the multi sample-split (Meinshausen et al., 2009; Dezeure et al., 2015).
Another constraint that can be imposed on the vectorβis to upper bound
the sum of squares of the parameters. This leads to the problem
min
β
||Y−Xβ|| 2 2 such that X
j̸=i
β2 j ≤c.
The solution to this minimisation problem (in terms of the Lagrangian) is
given by
ˆβ= (X ⊤X+αI p)−1X ⊤Y,(3)
whereα >0 is some constant. This is called the ridge estimator (Hoerl and
Kennard, 1970). It depends on setting the valueα. This solution is equivalent
to jointly minimising the least squares function and the sum of squared pa-
rameters (Rao and Toutenberg, 1999). Hence we obtain the solution such that
|| ˆβ||2 2 =c(Hastie et al., 2001). The solution lim α→0 ˆβis called the minimum
norm solution (Ben-Israel and Greville, 2003) or the ridgeless solution (Hastie
et al., 2019; Dar et al., 2021). Note that ifn > p,α= 0, and there is no
6

multicollinearity, then the ridge estimator ˆβin (3) reduces to the standard
least squares estimator in (2) whereXhas full rankp.
The benefits of ridge regression over the lasso are that (a) the ridge re-
gression has a closed form solution, (b) the ridge estimator is continuous and
so allows a sampling distribution and the calculation of standard errors, and
(c) the ridge estimator is able to handle multicollinearity (B¨ uhlmann, 2013).
Property (b) is especially appealing in practice because it allows for direct
inference with the ridge estimate (B¨ uhlmann, 2013; Waldorp and Haslbeck,
2024). The estimate has a bias (X ⊤X+αI p)−1X ⊤X−I, which shows that if
α→0, and there is no collinearity, then the bias reduces to 0. The variance
can be computed from which the standard errors are obtained for confidence
intervals andp-values (Hoerl and Kennard, 1970; Gruber, 1990). In B¨ uhlmann
(2013) a strategy is proposed to reduce the bias and obtain more reliable con-
fidence intervals andp-values; this is also discussed in Waldorp and Haslbeck
(2024).
The parameterαin (3) can be obtained byk-fold cross-validation. The
ridge estimator also has a Bayesian interpretation, whereαdenotes com-
mon variance for the normally distributed prior distribution with independent
parameters (Gruber, 1990), butαcan also be related to theη-generalised
Bayesian approach, whereα=η −1 (Gr¨ unwald and van Ommen, 2017). The
ridge estimator is biased (i.e., the expected value of the estimate is not the
true estimator), like the Lasso, but the solution is in closed form and is con-
tinuous. Hence, inference on the ridge estimator directly is possible (but see
B¨ uhlmann, 2013, for improvements) and, as we will see shortly, the ridge es-
timator leads to shrinkage useful for model selection and can be linked to a
geometric interpretation in high-dimensional models.
2.3 Realistic goals for high-dimensional nodewise graphical models
In the context of graphical models, the objective is to find the correct neigh-
bourhood (nodes that are directly connected to a node) of all nodes in the
graph, since then we obtain the correct set of non-zero edges for the entire
graph (Meinshausen and B¨ uhlmann, 2006). The ideal is, therefore, that with
high probability, for any node, the set of estimated and selected non-zero
edges ˆSis equal to the set of true edgesS, i.e.,P( ˆS=S) = 1−ϵ, with
smallϵ >0. However, in the high-dimensional setting this requires a strong
and untestable assumption that the smallest valueβ j is larger than a value in
the order of|S|
√
log(p)/n(the beta-min condition, B¨ uhlmann, 2013), where
|S|denotes the cardinality of the true set of non-zero edges for the node in
question. Foregoing this assumption may lead to the case where the set of true
edges in the neighbourhood of a node is in the set of estimated edges with
high probability, i.e.,P(S⊂ ˆS) = 1−ϵ(B¨ uhlmann and van de Geer, 2011).
Consequently, this may lead to an undesirably high false positive rate. If for
each node we select only a few additional, spurious edges, then for the entire
7

graph, the set of spurious edges will be proportional to the set of nodes. So,
for large graphs, the set of spurious edges will be large. Therefore, a more
realistic objective in graphical modelling is to obtain a set of neighbours such
that for any node, the estimated set of non-zero edges ˆSis in the true set of
edgesS, i.e.,P( ˆS⊆S) = 1−ϵ.
In order to achieve the goal of low false positive rate in the high-dimensional
setting, it is necessary that the large space of possible models is accounted for
(Foygel and Drton, 2013; Dwivedi et al., 2020; Cheema and Sugiyama, 2020).
Hence, a penalty for allowing such a large space of possible non-zero edges
should be part of the neighbourhood selection. We show in Section 5.1 that
because of the penalty in minimum description length (MDL), this selection
method achieves the goal of obtaining the correct neighbourhood or smaller,
but will not lead to a neighbourhood that is too large (no false positive edges).
First, we show the impact of the high-dimensional setting on the mean squared
error, which leads to the problems in neighbourhood selection.
3 Mean-squared error and the bias-variance trade-off
Determining the Gaussian graphical model was reduced to a series of regres-
sions (one for each node) when performing nodewise selection (Meinshausen
and B¨ uhlmann, 2006). Hence, model selection can be applied to each regres-
sion separately. We therefore apply ideas of mean-squared error to a single
regression to illustrate the central concepts involved.
Model selection is usually considered as a trade-off between model fit and
generalisation to other datasets. Rather than fitting exactly all datapoints of
a particular dataset (overfitting), the aim is to find regularity that will allow
the model to describe other datasets as well and generalise (Myung and Pitt,
1998; Gr¨ unwald et al., 2005; Claeskens and Hjort, 2008). How close the model
follows the dataset is related to bias and how well the model generalises to
other datasets is related to the variance; the mean-squared error is the sum
of the bias squared and the variance (made precise in Section 4, Hastie et al.,
2001). We first discuss the intuition of the bias-variance trade-off and how
this may fail in the high-dimensional setting, and then in Section 4 we discuss
rigorous results about the bias-variance trade-off in ridge regression.
The classical idea of model selection is illustrated in Figure 2. The situa-
tion is a linear regression model as described in Section 2 for the GGM. The
regression coefficients are estimated by ridge regression for an increasing num-
ber of predictors that we put in the model with a subset of the data called the
training set (we describe the details of the simulation in Section 6). In Figure
2(b) we see the bias (squared) of the test set (independent data not used for
estimation) based on the coefficients of the training set as a function ofp/n,
the ratio of the number of parameters in the model and the number of obser-
vations (in the training set). Then the mean-squared error (MSE) is obtained
in the remaining subset of observations, the test set; and is therefore called
8

test MSE test bias-variance
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8
0.0 0.5 1.0 1.5
p/n
test MSE
in sample
p/n
log bias/variance
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8
0 0.1 0.3 1 3
variance
bias
(a) (b)
Fig. 2. In (a) the test and train mean squared error (MSE) for a true linear model
as a function ofp/n, the ratio of the number of parameters and the number of
observations. The true model is atp/n≈0.15. In (b) are the squared bias (squares)
and variance (circles) for the test set.
test MSE. The correct model is atp/n≈0.15 (the dashed vertical line). We
see that the bias decreases sharply until the correct value is obtained and then
increases again, and similarly for the variance. The squared bias and variance
together make up the test MSE (also known as excess risk and prediction er-
ror). This is shown in Figure 2(a). Here we see that at the point≈0.15 (the
correct model), where the test MSE is lowest, the corresponding model should
be selected. This is the classic case discussed in for instance Hastie et al. (2001,
Chapter 7) and Gr¨ unwald et al. (2005, Chapter 1 and Chapter 2). The test
MSE is used instead of the MSE based on the training (estimation) data (seen
as the dashed green line in Figure 2(a), in sample) because the training MSE
is overly optimistic and so remains low (see Efron, 1986; Hastie et al., 2001).
This trade-off between bias and variance implies that the complexity of the
model cannot be too high because then the model tends to overfit, i.e., fit only
the training data and does not generalise well to other data.
In recent years it has appeared that this classical scenario is not all there
is to it. There are situations where a model can over fit (select too many
non-zero coefficients) and still generalise well. This phenomenon (sometimes
called benign overfitting, Bartlett et al., 2020) is seen in Figure 3(a). The lin-
ear regression coefficients are estimated using the ridge estimator where the
number of parameters (predictors) is increased such that the ratiop/n(for the
training set) ranges between 0.1 to 2. Atp/n= 0.1 we have 10 observations
per parameter and atp/n= 2 we have 0.5 observations per parameter. The
classical case is seen up top/n= 1 (i.e.,p=n), the interpolation point (as
in Figure 2). From the interpolation point on, the model is overparameterised
(p > n) and has very low training MSE (green dashed line in Figure 3(a)). In
9

MSE bias-variance
p/n
log mse
0.5 1 1.5 2
0.1 0.3 1 3 7
test MSE
train MSE
p/n
log bias/variance
0.5 1 1.5 2
0.01 0.05 0.3 1 3 4
variance
bias
variance train
bias train
(a) (b)
Fig. 3. In (a) the test and train mean squared error (MSE, in logarithm) for a true
linear model as a function ofp/n, the ratio of the number of parameters and the
number of observations (in the training set). The true model with 5 predictors is at
p/n≈0.15, indicated by the vertical grey dashed line. In (b) is the bias (squares)
and variance (circles), both in logarithm, for the test set and for the training set
(dashed lines).
Figure 3(b), we see that, as expected, the bias decreases after the interpola-
tion point. Unexpectedly, the variance starts to decrease as well, suggesting
that the model will generalise well to other datasets. But this seems paradoxi-
cal since overparametrisation (and hence overfitting) would suggest that noise
is being modeled. But the decreasing variance implies that the overparame-
terised model is capable of capturing regularities in other datasets, i.e., it will
generalise well.
This phenomenon is often referred to as the double descent (Belkin et al.,
2019), since there is a second descent after the interpolation point (p=n).
The double descent has been investigated thoroughly (e.g., Hastie et al., 2019;
Bartlett et al., 2020, 2021) with some results as follows. We assume for these
results that all random variables are normally distributed and have indepen-
dent identically distributed predictors.
(a) In linear regression when the model is approximately correct andp/nis
large (overparameterised), the global minimum of the test MSE is ob-
tained at the correct model.
(b) If the model is misspecified andp/nis large (overparameterised), then
the global minimum of the test MSEcouldbe obtained at a largely over-
parameterised (incorrect) model.
The first result (a) implies that we are still able to correctly identify the correct
neighbourhood for each node when approximately correctly specified. And the
second result (b) implies that when the model is not correctly specified, e.g.,
nonlinear, it might be the case that in neighbourhood selection far too many
10

edges will be selected because the MSE is lowest in that case. This last result
explains why in deep learning (and in machine learning) astounding results
have been obtained by hugely overparameterised models. Examples are object
and speech recognition and traffic sign classification (see, e.g., Goodfellow
et al., 2016).
The implications for neighbourhood selection are that obtaining the cor-
rect neighbourhood or smaller requires increasing the ridge parameter strongly,
so as to counteract the small MSE that is obtained for large misspecified mod-
els. It is in general questionable whether this can be achieved by carefully
selecting a ridge parameter (by e.g., cross-validation), or whether a separate
penalty is required that counteracts the low MSE obtained in the case of high-
dimensions. We will see in Section 5.1 that we require a separate penalty in
the high-dimensional case.
4 Mean-squared error decomposition in bias and variance
We remain within the framework of nodewise selection and focus on a neigh-
bourhood of any node to obtain the non-zero edges, which leads to regressing
one node on the remaining nodes.
We define the mean squared error (MSE) for linear models as a quantity
that represents the expected loss incurred by estimating with modelJinstead
of the true modelS. Let ˆYS be the prediction based on the true setSof
predictors, so thatβ j ̸= 0 ifj∈Sandβ j = 0 ifj /∈S, which we refer to
asβ S. Furthermore, we assume that the data are generated according to an
additive model where errorseare added to ˆYS, so that
Y= ˆYS +e= X
j∈S
Xjβj +e,(4)
where the errorseare independent and identically distributed with mean 0
and varianceσ 2.
Test MSE (excess risk) is defined in terms of a so-called test set, an in-
dependent point (or set of points) not encountered before in the so-called
training set (Hastie et al., 2001). Let (X 0, Y0)∈R p+1 be a test data point
independent of, but from the same distribution as, all other (X i, Yi)∈R p+1.
With the training data the ridge estimate ˆβJ with modelJis obtained. Then
the excess risk (out of sample prediction risk, Hastie et al., 2019) with respect
to the true parameterβ S, is defined as the squared difference between the
predictions obtained with modelJand the predictions obtained with the true
modelSfor test data (X 0, Y0)
R(J) =E
h
(Y0 −X ⊤ 0 ˆβJ )2 −(Y 0 −X ⊤ 0 βS)2
i
,(5)
where the expectation is conditional on the training dataX, which functions
in the ridge estimate ˆβJ = (X ⊤X+αI p)−1X ⊤Yfrom (3). Similar to Hastie
11

et al. (2019) and Bartlett et al. (2021) we can obtain the excess risk in terms
of the squared bias and variance (see Lemma B.1 in Appendix B)
R(J) =B(J) +V(J),(6)
with
B(J) = (β S −E ˆβJ )⊤Σ(βS −E ˆβJ ), V(J) =E( ˆβJ −E ˆβJ )⊤Σ( ˆβJ −E ˆβJ ),(7)
whereB(J) is called the squared bias andV(J) is called the variance, and
Σ =E(X 0X ⊤ 0 ), which is the same as the covariance matrix of the predictors
E(X ⊤X). This is the famous variance and squared bias decomposition (Hastie
et al., 2001). The classical idea is that reducing bias will increase variance and
vice versa, thus balancing the MSE. Hence, a good model will minimise the
MSE (excess risk) and most model selection methods are geared towards this
goal.
The training biasB(J) is 0 for the linear model, whenp < n, and the
linear model is correct (Hastie et al., 2019). However, for the ridge estimator
ˆβin (3) the bias is non-zero (Hoerl and Kennard, 1970). It turns out that when
the in-sample (training) residuals are 0 (i.e., overparameterised, see Appendix
I), then still the variance on the test set need not be large (Bartlett et al.,
2021). Here we explain how this can be achieved with ridge regression.
To show the impact of ridge regression on the variance and the squared
bias (and hence the MSE), we will rewrite the variance and squared bias from
(7). To do this we further assume that Σ =σ 2 ξ I(i.e., is isotropic). We then
obtain the test variance (see Lemma B.3)
V(J) =σ 2 ξ σ2 e
nX
j=1
λj
(λj +α) 2 ,
whereλ j are the eigenvalues ofX ⊤X. Hence, by increasingαwe see that we
are lowering the varianceV(J), and hence the test MSE. Additionally, we can
observe that if the contribution of the eigenvaluesλ d+1 up toλ p, for some
d < p, is small, then the variance will not increase, and hence, prediction may
still be accurate. This implies that adding more predictors (makingplarger)
will not necessarily inflate the varianceV(J) much, which is stabilised by the
ridge parameterα. This argument is used in Bartlett et al. (2020, 2021) to
explain why in some cases machine learning with a large number of parameters
predicts well; the noise is distributed among the large number of directions
(given by the eigenvectors) so that none of the eigenvaluesλ k withk > dwill
be larger than the ridge parameterα.
Similar to the test varianceV(J) the biasB(J) can also be reduced to a
more amenable form when we assume that Σ =σ 2 ξ I. With this assumption we
12

obtain (see Lemma B.2)
B(J) =σ 2 ξ γ1α2 (λ1 +α) 2 +σ 2 ξ nX j=2 α2 (λj +α) 2 ,(8)
whereγ 1 is the single non-zero eigenvalue ofβ Sβ⊤ S . This shows different be-
haviour for the squared test bias than the test varianceV(J): the squared test
bias could increase by increasingα.
This analysis shows that the peak in the test MSE for the ridge estima-
tor in Figure 3(a) is in some sense an artefact of choosing the wrong ridge
parameterα= 0.0001 (used in Figure 3). The peak disappears when we use
a carefully selected ridge parameterαusingk-fold cross-validation. This is
shown in Figure H.1 in Appendix H. It can also be seen in Figure H.1 that the
lasso also does not show such a peak but the lasso has generally larger MSE
than the ridge.
We can now conclude from this analysis that there are two views on how
to manage the test variance in the case of high-dimensional data.
(a) We can increase the ridge parameterαdirectly, reducing the test variance
V(J), and hence obtaining reasonable test MSE.
(b) we can constrain the size of||β|| 2 in the ridge estimator, therefore, de-
creasing the model complexity (volume) of the model. We do this by
constraining the ridge estimator with smallcsuch that||β|| 2 ≤c.
In both cases (a) and (b) we are either directly or indirectly constraining the
total signal||β|| 2. In model selection this can be done by either increasingα,
equivalently, decreasingcin the ridge constraint||β|| 2 ≤c, or by incorporat-
ing the complexity (volume) of the model. (The ridge parameterαcan also
be interpreted in terms of the signal-to-noise (SNR) with similar conclusions
relating to SNR, see Appendix D.)
4.1 Model misspecification
More generally, a model is defined as a class of probability distributions (in a
favourable case in terms of corresponding densities), and the model is correctly
specified if the distribution is in the particular class used for optimisation
(Myung and Pitt, 1998). In our setting of nodewise regression with Gaussian
variables, to determine the neighbourhood of a node, the model class is the set
of univariate normal distributions parameterised by the meanµand variance
σ2, with the conditional meanE(Y|x) given by a linear functionx7→x ⊤β,
so that the model is correctly specified. Model misspecification can then be
defined in terms of the model class not containing the correct distribution
(Gr¨ unwald, 2007; Dar et al., 2021; Kleijn, 2026). Continuing our example of
normal distributions, the conditional mean could be given by some nonlin-
ear functionf, say a logistic functionx7→1/(1 + exp(x ⊤β)), while we only
consider linear modelsx ⊤βfor estimation. One interpretation of the linear pa-
rameters when the true model is nonlinear, is in terms of a weighted average
13

of derivatives of the conditional mean with respect to the covariatex j, which
reduces to mixtures of treatments in causal analysis (White, 1980; Kunievsky,
2025). The problem with misspecifying the conditional mean may lead to the
situation where the residual variance is heterogeneous, and the ‘best’ model
in terms of being closest to the true model in Kullback-Leibler divergence,
is a mixture of models which is not in the model space (non-convex model
space). For more information on this see Appendix B.1 and the seminal work
of Gr¨ unwald and van Ommen (2017).
For nodewise regression with misspecification, we assume that the model is
some nonlinear functionfmodelled by a linear functionX ⊤β. If the misspec-
ification is characterised by an additive term, so that the model isX ⊤β+ξ,
where we do not know aboutξ, then the misspecification can be described by
the mismatchE||ξ|| 2 (Hastie et al., 2019; Dar et al., 2021). In our approach
we do not assume a linear decoupling, but simply that there is some nonlinear
functionf. In that case we obtain an additional term in the excess risk (see
Lemma B.4 in Appendix B)
Rf (J) =B f (J) +V f (J) +M f (J),(9)
where
Bf (J) =E
h
(f(X 0, βS)−E(X ⊤ 0 ˆβJ ))2
i
,
Vf (J) =E
h
(X ⊤ 0 ˆβJ −E(X ⊤ 0 ˆβJ ))2
i
,and
Mf (J) = 2E
h
(Y0 −f(X 0, βS))(f(X 0, βS)−X ⊤ 0 ˆβJ ) i .
If we are able to bound the misspecification|f(X 0, βS)−X ⊤ 0 ˆβJ |=O p(K),
we obtain a bound on the misspecification term by the Cauchy-Schwarz in-
equality:M f (J)≤σO(K) (see Proposition B.5). This bound on the misspec-
ification will lead to the possibility of obtaining the correct neighbourhood
or smaller with minimum description length in the high-dimensional setting.
Additionally, in linear models we can leverage the result that forL⊆J, we
have thatE[(Y 0 −X ⊤ 0 ˆβJ )2]≤E[(Y 0 −X ⊤ 0 ˆβL)2] (see also Appendix G). Hence,
the misspecification decreases as the ratiop/nincreases.
5 Nodewise selection in high dimensions
A regression model is represented by a distribution for the residuals (Hastie
et al., 2001) and, for the GGM using linear regressions, is identified with a
set of nodes in the neighbourhood of a node, indexed by the setJ. Increas-
ing the number of included nodes in a nodewise regression is hence identified
with different distributions, which can then also be indexed byJ. Nodewise
selection is therefore concerned with distinguishing probability distributions.
The Kullback-Leibler divergence (KL, Cover and Thomas, 2006) is often used
to distinguish distributions, where a KL of 0 indicates no difference between
14

distributions, and a value larger than 0 indicates different distributions (see
Appendix E). Both the Akaike information criterion (AIC) and minimum de-
scription length (MDL) can be considered as minimising the KL of a hy-
pothesised distribution (our linear regression models) and some generative
(unknown) model (Gr¨ unwald, 2000; Myung et al., 2006; Claeskens and Hjort,
2008). The AIC estimates the KL and corrects the incurred bias of doing so
(see Appendix E). The MDL, on the other hand, applies the idea of encod-
ing the data and hypothesised model to obtain a reasonably approximating
model, which we explain here.
In the high-dimensional case nodewise selection is problematic precisely
because of the large parameter space. In high dimensions we obtain eventually
near-zero training error, even with a linear model (Bartlett et al., 2020, see
Appendix I). This is because the parameter space of the model is so vast (i.e.,
high complexity), that nearly all data points can be accounted for. Conceptu-
ally, the volume of the parameter space more or less explodes with increasing
dimension and, hence, dominates the regression (see Appendix C and Ap-
pendix D). This may lead to selecting too many neighbours (over fit), which,
in nodewise selection leads to a graph with many spurious edges. In order to
obtain a correct neighbourhood or smaller in such high-dimensional situations,
this increased model complexity needs to be taken into account explicitly, es-
pecially in the case of misspecification.
Here we discuss the MDL in some detail and show that in the high-
dimensional setting it leads to no false positive edges with high probability.
The reason is that the penalty (model encoding) counteracts the large number
of possible edges in a neighbourhood. For comparison, we also show results for
the AIC, BIC, the Lasso, and another version of MDL for nodewise selection.
We discuss these in Appendices E for the AIC and F an optimised version
of MDL. There are excellent books that describe these derivations well. For
instance, the AIC and BIC (and other model selection criteria) are described
in Claeskens and Hjort (2008) and MDL is described extensively in the book
by Gr¨ unwald (2007).
5.1 Minimum description length
The minimum description length (MDL) is derived from the idea that com-
pression (encoding) of data can be translated into probabilities (Gr¨ unwald
et al., 2005). MDL is concerned with the length of (prefix or invertible)
optimal codes which can be separated into a part where the data are en-
coded given the model and a part where the model is encoded. The length
of the data can be encoded by the log likelihood (Hansen and Yu, 2001), i.e.
length(Y, x) =−logf(Y|x, ˆβ), wherefis the conditional density ofYgiven
the predictorsX=x(see Appendix E). Additionally, the model is encoded,
called the complexity, which leads to a specific formulation depending on the
type of encoding (Gr¨ unwald, 2007). This encoding term is the penalty for
the possibly large parameter space and will to a certain extent guard against
15

overfitting.
For normally distributed random variables the MDL can be approximated
by (Myung et al., 2006; Gr¨ unwald, 2007)
MDL(J) = n 2 log ˆσ2 J | {z }
data code length
+ 1 2 tr(SJ ) logn+ log Z B q det(FJ )dβ | {z }
model code length
+o(1),(10)
where tr(S J ) is the trace of matrixS J representing the effective number of
parameters for modelJ, andF J is the Fisher information matrix for modelJ,
which isF J =X ⊤X/σ2 whenn > p, and the true model is exponential family
(Gr¨ unwald et al., 2005, Chapter 2). The matrixS J is used to determine the
number of effective parameters, and isS J =X(X ⊤X) −1X ⊤ whenn > p; the
trace of this matrix isp(this is the same as the rank in this case).
However, for the high-dimensional case (p > n) we find thatX ⊤Xis
singular, implying that det(X ⊤X) = 0. This is because the rank ofX ⊤Xis
min{n, p}, and becausen < p, we have that the rank in this case isn, while
the dimensions arep×p. Thus, we must have that there arep−ndimensions
that are not represented byX ⊤X(i.e.,p−nvectors project onto the kernel
or null space). We can use ridge regression to alleviate the problem by using
instead ofX ⊤Xthe matrix from ridge regressionW(α) =X ⊤X+αI(Hastie
et al., 2001). We then find thatS J =X(X ⊤X+αI) −1X ⊤. This gives the
general equation for the number of effective parameters (Hastie et al., 2001,
Section 7.6)
d f(α) = tr(SJ ) = trX(X ⊤X+αI) −1X ⊤ =
min{p,n}X
j=1
λj
λj +α ,
whereλ j are the eigenvalues ofX ⊤X.
To approximate the integral in the penalty encoding the model in (10),
we make use of the fact that in linear regression the Fisher information is
independent of the parameterβ j, and hence the integral represents the open
p-dimensional ballB p(|| ˆβ||2) over the Fisher information where we used the
ridge parameterα(see Lemma D.1 in Appendix D). Thep-dimensional ball is
centered at|| ˆβ||2 because in the ridge solution we obtain the solution such that
α(||β|| 2 2 −c) = 0. We then obtain (Cheema and Sugiyama, 2020; Gr¨ unwald,
2007)
log
Z
B
q
det(F)dβ≈log det(X ⊤X+αI) + logB p(||β||2)/σp.(11)
Thep-dimensional ball in the last term, logB p(||β||2), represents the volume of
the parameter space and is discussed in Appendix C. The log of this term will
become large, and hence apply a stronger penalty with increasing dimension.
This is why increasing the dimension can have positive effects on the gener-
alisation error (variance in the test set). However, in determining the volume
16

in this way, we have assumed that the linear model is correct. Hence, we may
expect that when the model is misspecified, the term in the integral encoding
the model in (11) may not be sufficient to guard against incorrect decisions.
Gr¨ unwald and van Ommen (2017) show that when the model is misspecified
the model space can be non-convex, and the best approximation to the true
model may not be in the model space (see Appendix B.1). However, using
linear models we can with high probability conclude that MDL as defined in
(10) with (11) will be able to guard against overfitting. This is because of the
penalty termB p(||β||2), as predicted by Cheema and Sugiyama (2020). We are
therefore able to achieve the goal mentioned in Section 2.3, that the selected
neighbourhood of edges in a graph ˆSwith MDL is in the true neighbourhood
S, withd=|S|.
Proposition 5.1LetSdenote the true support for a (possibly nonlinear)
data generating process ofY i fori= 1, . . . , nwithnfixed, and letJrepresent
the set of predictors such thatS⊂J, where|S|=dand|J|=p. We test
linear modelsXβ J for anyJ(includingS) by MDL as given in (10) with (11).
Letpincrease andp > d. IfEˆσ 2 J > γ, for someγ >0, then with probability
at least1− d p exp(−(p−d))it holds that ˆS⊆S; equivalently, the probability
of false positives goes to 0.
A proof can be found in Appendix G.
We refer to MDL in (10) with (11) as MDL. The complexity of MDL has
also been used without the integral term (Rissanen, 1986; Gr¨ unwald, 2000).
This approximation is in that case equivalent to the Bayesian information
criterion (BIC) introduced by Schwartz (1978). Hence, we call that version
MDL-S.
6 Simulations
In order to determine the behaviour of nodewise selection in realistic high-
dimensional scenarios in graphical models, we perform simulations for a single
neighbourhood. This corresponds to the graphs shown in Figure 1, with the
perspective of a single node for which we need to determine the connected
nodes (neighbourhood) among the nodes that are not connected, of which
there are many more.
The data are generated by a Gaussian graphical model. An inverse co-
variance matrix was generated where each node had 5 neighbours with edge
coefficient 1. We then selected a node at random. Data were generated where
the total number of observations was fixed atn= 40. We vary the graph size
so that the number of possible edges to be estimated ranges fromp= 3 to
p= 320 (see Figure 1). So, we obtain a ratio of the number of edges and the
number of training observations ofp/n= 0.1 to 2 withp= 64 andp/n= 10
forp= 320. Edges (conditional dependences) are generated either according to
17

a linear model (correct model specification) or a sigmoid function (model mis-
specification). The regression coefficients for nodewise selection are estimated
as a linear model by ridge regression (3) with a training set ofn train = 32 (80%
of the total sample sizen= 40). The test set is of sizen test = 8. We consider
the case where we know the true model is linear and we estimate the linear
model (case (a) in Section 3), and we misspecify the model because the true
model is sigmoidal and we use a linear approximation (case (b) in Section 3).
We compare the AIC, AIC-CV (whereαis obtained with cross-validation),
MDL-S (which is the BIC), MDL-opt (the optimised MDL), MDL, the Lasso
(also withαobtained with cross-validation), and finally, the desparsified lasso
(Lasso-ds, van de Geer et al., 2014; Dezeure et al., 2015).
The measures we use to evaluate the nodewise selection is the proportion
of edges in a neighbourhood that is too low (under fit), correct or too high
(over fit) in terms of the estimated edges in a single neighbourhood. Then,
under, correct and over fit, respectively, forRsimulations are defined as
proportion under fit := 1 R RX r=1 1{ ˆS⊂S},
proportion correct fit := 1 R RX r=1 1{ ˆS=S},and
proportion over fit := 1 R RX r=1 1{ ˆS⊃S},
where ˆSis the set of indices for the estimated non-zero edges (support) and
Sis the true support. Given our objective of selecting a neighbourhood with
high probability which includes correct edges but no spurious connections (see
Section 2.3), we want the under and correct fit to be as large as possible and
the over fit as small as possible. To look into more detail of over fitting, we
also consider the false positive rate, defined as
fasle positive rate := 1 R RX r=1 | ˆS∩S c| |Sc| ,
whereS c is the complement of the support, the true negatives or zero edges.
This measure gives an indication of the rate of selecting too many edges in a
neighbourhood in the graph (over fitting).
6.1 Results
We start with the impact of possible neighbourhood size (p/n= 0.1 up to 10)
on MSE. Figure 4(a) shows the MSE for a correctly specified linear model, and
for a misspecified linear model in Figure 4(b). The test MSE in (a) remains
above the optimal MSE at the correct neighbourhood size withp/n≈0.15.
This implies that standard model selection with MDL-S or the AIC should
18

correct model misspecified model
p/n
log mse
012 5 10
0.10.3 1 3
test MSE
train MSE
p/n
log mse
012 5 10
0.10.3 1 3
test MSE
train MSE
(a) (b)
Fig. 4. The MSE for correctly specified (a) and misspecified model (b) for a neigh-
bourhood withpedges up to 320, so thatp/nranges between 0.1 and 10. For the
true linear model (a) the global minimum of the test MSE remains the correct model
withp= 5, approximately atp/n≈0.15. For the misspecified model (b), however,
we see that the global minimum has now shifted from the correct neighbourhood
size withp= 5 and MSE 0.0877 to the model withp/n= 10 (= 320/32) and MSE
0.0844.
work in the high-dimensional setting. However, in Figure 4(b), when the model
is misspecified, the test MSE drops below the MSE at the optimal solution,
indicating that standard neighbourhood selection need not work. Since the
MSE is lower at models with a large number of parameters, neighbourhood
selection could favour models with a large number of parameters.
The consequences for neighbourhood selection are shown in Figure 5. The
figure shows under fit ( ˆS⊂S, light blue), correct fit ( ˆS=S, blue) and over fit
( ˆS⊃S, red) in each subfigure. The left column of Figure 5 shows the results
for when the data is correctly specified as linear, while the right column shows
the results for when the model is misspecified; both are estimated with a linear
model. In the bottom row, neighbourhood selection is performed whenp max =
15, and increases top max = 32 in the middle and 320 in the top row. When the
model is correctly specified (left column) and the dimension is low (pmax = 15),
neighbourhood selection in graphical models works reasonably well in that
either the correct support is obtained, ˆS=Sor it is underestimated, i.e.,
ˆS⊂S. Only the AIC and the Lasso show increased false positive rates, i.e.,
ˆS⊃S. Increasing the dimension top max = 320 exacerbates the over fit for AIC
and Lasso (also Lasso-ds). In contrast, MDL, MDL-opt, MDL-S and AIC-CV
appear to remain accurate in the sense that over fit remains low, and over fit
is absent in the case of MDL. For MDL this is because of the large penalty on
using a large dimensional model space described in Section 5.1, in line with
Proposition 5.1.
The pattern of over fit remains relatively similar when the model is mis-
19

correct model misspecified model
proportion under/correct/over fit
AIC
AIC-CV
MDL-S
MDL
MDL-opt
Lasso
Lasso-ds
0.0 0.2 0.4 0.6 0.8 1.0
p_max = 320
proportion under/correct/over fit
AIC
AIC-CV
MDL-S
MDL
MDL-opt
Lasso
Lasso-ds
0.0 0.2 0.4 0.6 0.8 1.0
p_max = 320
proportion under/correct/over fit
AIC
AIC-CV
MDL-S
MDL
MDL-opt
Lasso
Lasso-ds
0.0 0.2 0.4 0.6 0.8 1.0
p_max = 32
proportion under/correct/over fit
AIC
AIC-CV
MDL-S
MDL
MDL-opt
Lasso
Lasso-ds
0.0 0.2 0.4 0.6 0.8 1.0
p_max = 32
proportion under/correct/over fit
AIC
AIC-CV
MDL-S
MDL
MDL-opt
Lasso
Lasso-ds
0.0 0.2 0.4 0.6 0.8 1.0
p_max = 15
proportion under/correct/over fit
AIC
AIC-CV
MDL-S
MDL
MDL-opt
Lasso
Lasso-ds
0.0 0.2 0.4 0.6 0.8 1.0
p_max = 15
Fig. 5. Proportion of decisions: underestimating (light blue), correct (blue), and
overestimating (red) the dimension of the model for both the correct (linear) and
incorrect (logistic) data generating model for different maximum number of predic-
torsp max = 15,32 or 320 in each of the respective rows, such thatp/n= 0.47, 1 and
10, respectively. In both the linear and non-linear model, there arep= 5 non-zero
coefficients. In the left column the data were generated and estimated with the
linear model; in the right column, data were generated with the non-linear model
while they were estimated with the linear model.
20

correct model misspecified model
0 2 4 6 8 10
0.00 0.05 0.10 0.15 0.20
p/n
false positive rate
AIC
AIC-CV
MDL-opt
MDL-S
Lasso
Lasso-ds
MDL
0 2 4 6 8 10
0.00 0.05 0.10 0.15 0.20
p/n
false positive rate
AIC
AIC-CV
MDL-opt
MDL-S
Lasso
Lasso-ds
MDL
(a) (b)
Fig. 6. False positive rate for each method. In (a) the model is correctly specified as
linear and in in (b) the model is misspecified as linear while the conditional mean
is a logistic function.
specified (right column of Figure 5), but the probability of selecting the correct
neighbourhood is decreased for all methods. Only MDL does not select too
many edges (no false positives), which is in line with theory as discussed in
Section 5.1 and Appendix G.
Finally, we consider the false positive rate, the probability of including too
many edges in the graph. Figure 6(a) shows the false positive rate for each
dimension in the simulationp/n= 0.1 up to 10, when the model is correctly
specified as linear. MDL stands out in that no matter the model dimension,
the false positive rate remains at 0. This corresponds to the results in the left
column of Figure 5. Most other methods have a slightly elevated false positive
rate; the AIC tends to lead to a neighbourhood that is too large from around
the interpolation point (p/n= 1) on. When the assumption of a true linear
model no longer holds, the false positive rate increases for almost all methods,
except Lasso and MDL. Both MDL and Lasso have low false positive rate for
any ratio ofp/n.
7 Conclusion and discussion
We considered nodewise selection of edges in the Gaussian graphical model
when the number of nodes exceeds the number of observations. This is an issue
because regular estimation techniques like least squares cannot work in such
situations. We used the ridge regression estimate to solve this issue, leading
to a biased but closed form estimate. We were then able to show the impact
of the ridge parameter on the mean squared error, and concluded that indeed,
21

when the true relation between edges is linear, the MSE is lowest at the correct
neighbourhood. We also showed that in the misspecified case, the MSE is co-
determined by an additional term in the MSE caused by the misspefication
of a nonlinear model by a linear model. In addition, the ridge parameter
could be interpreted as the inverse of the signal-to-noise-ratio. In low signal-
to-noise-ratio situations the ridge parameter will be high, leading to a larger
ridge penalty. This penalty was then seen to reduce the parameter variance
and, hence, implies that the generalisation can still be reasonable, suggesting
generalisation to other samples is possible. This also (partly) explains why
some highly overparameterised machine learning techniques are able to predict
well, mimicking regularised estimation by restricting the class of functions in
empirical risk minimisation (Hastie et al., 2022). Generally, selecting the ridge
parameter using cross-validation seems good practice, since it reduced the
sensitivity of the MSE and neighbourhood selection improved.
We next applied nodewise selection to ascertain whether it is possible to
obtain the correct neighbourhood or smaller, but not larger (i.e., no false pos-
itives). We proved that in the high-dimensional setting MDL can achieve this
objective of correct or smaller neighbourhood selection with high probability,
in both the case when true edge relations are linear or nonlinear. The rea-
son is that it explicitly takes into account the volume of the parameter space
to counteract the low MSE at high dimensions. Simulations confirmed these
results, and also showed that other neighbourhood selection methods (using
AIC, for example) lead to neighbourhoods that are too large. Obviously, a
low false positive rate and under fit for MDL, lead to a somewhat elevated
false negative rate (too few correct edges). Considering the discussion in Sec-
tion 2.3, we believe that, even though some edges will not be detected, this is
preferable to the case when too many edges are selected. Therefore, we rec-
ommend using MDL for nodewise selection in the high-dimensional setting for
Gaussian graphical modelling.
While the result that MDL leads to low false positives is geared towards
the application of the high-dimensional setting in graphical modelling, it is
more general. We used the framework of nodewise regression, and so it is valid
within the context of regression. But we used the fact that there is a bound on
the misspecification for the conditional mean and that the residual variance is
bounded away from 0. Given these settings, the result on MDL can be applied
to other regression settings.
Acknowledgements
The research conducted by L. Waldorp has been supported by a grant from the
ERC (ERC project 101053880) and by the “New Science of Mental Disorders”,
the Dutch Research Council and the Dutch Ministry of Education, Culture
and Science (NWO), grant number 024.004.016.
22

References
Bartlett, P. L., Long, P. M., Lugosi, G., and Tsigler, A. (2020). Benign overfit-
ting in linear regression.Proceedings of the National Academy of Sciences,
117(48):30063–30070.
Bartlett, P. L., Montanari, A., and Rakhlin, A. (2021). Deep learning: a
statistical viewpoint.arXiv preprint arXiv:2103.09177.
Belkin, M., Hsu, D., Ma, S., and Mandal, S. (2019). Reconciling modern
machine-learning practice and the classical bias–variance trade-off.Pro-
ceedings of the National Academy of Sciences, 116(32):15849–15854.
Ben-Israel, A. and Greville, T. (1974).Generalized inverses: theory and ap-
plications. New York: John Wiley and Sons.
Ben-Israel, A. and Greville, T. (2003).Generalized inverses: Theory and ap-
plications. New York: Springer.
Bilodeau, M. and Brenner, D. (1999).Theory of multivariate statistics. New
York: Springer-Verlag.
B¨ uhlmann, P. (2013). Statistical significance in high-dimensional linear mod-
els.Bernoulli, 19(4):1212–1242.
B¨ uhlmann, P., Kalisch, M., and Meier, L. (2014). High-dimensional statistics
with a view toward applications in biology.Annual Review of Statistics and
Its Application, 1:255–278.
B¨ uhlmann, P. and van de Geer, S. (2011).Statistics for High-Dimensional
Data: Methods, Theory and Applications. Springer.
Cheema, P. and Sugiyama, M. (2020). Double descent risk and volume satu-
ration effects: A geometric perspective.arXiv preprint arXiv:2006.04366.
Claeskens, G. and Hjort, N. (2008).Model selection and model averaging.
Cambridge University Press, Cambridge.
Cover, T. and Thomas, J. (2006).Elements of information theory. Wiley and
Sons, 2nd edition.
Dar, Y., Muthukumar, V., and Baraniuk, R. G. (2021). A farewell to the bias-
variance tradeoff? an overview of the theory of overparameterized machine
learning.arXiv preprint arXiv:2109.02355.
DasGupta, A. (2008).Asymptotic Theory of Statistics and Probability.
Springer-Verlag, New York.
Dezeure, R., B¨ uhlmann, P., Meier, L., and Meinshausen, N. (2015). High-
dimensional inference: confidence intervals, p-values and r-software hdi.Sta-
tistical science, pages 533–558.
Dwivedi, R., Singh, C., Yu, B., and Wainwright, M. J. (2020). Revisiting
complexity and the bias-variance tradeoff.arXiv preprint arXiv:2006.10189.
Efron, B. (1986). How biased is the apparent error rate of a prediction rule?
Journal of the American statistical Association, 81(394):461–470.
Epskamp, S., Borsboom, D., and Fried, E. I. (2018). Estimating psychological
networks and their accuracy: A tutorial paper.Behavior Research Methods,
50(1):195–212.
Epskamp, S. and Fried, E. I. (2018). A tutorial on regularized partial correla-
23

tion networks.Psychological methods, 23(4):617.
Foygel, R. and Drton, M. (2013). Bayesian model choice and information
criteria in sparse generalized linear models. Technical report, University of
Chicago.
Friedman, J., Hastie, T., and Tibshirani, R. (2008). Sparse inverse covariance
estimation with the graphical lasso.Biostatistics, 9(3):432–441.
Giraud, C. (2014).Introduction to high-dimensional statistics, volume 138.
CRC Press.
Goodfellow, I., Bengio, Y., Courville, A., and Bengio, Y. (2016).Deep learning,
volume 1. MIT press Cambridge.
Gruber, M. (1990).Regression Estimators: A Comparative Study. Academic
Press, Boston.
Gr¨ unwald, P. (2000). Model selection based on minimum description length.
Journal of Mathematical Psychology, 44:133–152.
Gr¨ unwald, P. and van Ommen, T. (2017). Inconsistency of bayesian inference
for misspecified linear models, and a proposal for repairing it.Bayesian
Analysis, 12(4):1069–1103.
Gr¨ unwald, P. D. (2007).The minimum description length principle. MIT
press.
Gr¨ unwald, P. D., Myung, I. J., and Pitt, M. A. (2005).Advances in minimum
description length: Theory and applications. MIT press.
Hansen, M. H. and Yu, B. (2001). Model selection and the principle of min-
imum description length.Journal of the American Statistical Association,
96(454):746–774.
Hastie, T., Montanari, A., Rosset, S., and Tibshirani, R. J. (2019). Surprises
in high-dimensional ridgeless least squares interpolation.arXiv preprint
arXiv:1903.08560.
Hastie, T., Montanari, A., Rosset, S., and Tibshirani, R. J. (2022). Surprises in
high-dimensional ridgeless least squares interpolation.Annals of statistics,
50(2):949.
Hastie, T., Tibshirani, R., and Friedman, J. (2001).The Elements of Statistical
Learning. Springer-Verlag, New York.
Hastie, T., Tibshirani, R., and Wainwright, M. (2015).Statistical learning
with sparsity: the lasso and generalizations. CRC Press.
Hoerl, A. and Kennard, R. (1970). Ridge regression: Biased estimation for
nonorthogonal problems.Technometrics, 12(1):55–67.
Jacod, J. and Protter, P. (2004).Probability essentials. Springer-Verlag, New
York.
Jankova, J. and van de Geer, S. (2017). Inference for high-dimensional graph-
ical models. In Drton, M., Maathuis, M., Lauritzen, S., and Wainwright,
M., editors,Handbook of graphical models. Taylor & Francis Group.
Jones, B. and West, M. (2005). Covariance decomposition in undirected gaus-
sian graphical models.Biometrika, 92(4):79–786.
Kleijn, B. (2026). The frequentist theory of bayesian statistics.
Koller, D. and Friedman, N. (2009).Probabilistic graphical models: Principles
24

and techniques. MIT Press.
Kullback, S. and Leibler, R. (1951). On information and sufficiency.Annals
of mathematical statistics, 22:79–86.
Kunievsky, N. (2025). Linear regression in a nonlinear world.arXiv preprint
arXiv:2512.13645.
Lauritzen, S. (1996).Graphical Models. Oxford University Press, Oxford.
Maathuis, M., Drton, M., Lauritzen, S., and Wainwright, M. (2018).Handbook
of graphical models. CRC Press.
Meinshausen, N. and B¨ uhlmann, P. (2006). High-dimensional graphs and
variable selection with the lasso.The Annals of Statistics, 34(3):1436–1462.
Meinshausen, N. and B¨ uhlmann, P. (2010). Stability selection.Journal of the
Royal Statistical Society, Series B, 72(4):1436–1462.
Meinshausen, N., Meier, L., and B¨ uhlmann, P. (2009). P-values for high-
dimensional regression.Journal of the American Statistical Association,
104(488).
Myung, I. and Pitt, M. (1998). Issues in selecting mathematical models of
cognition. In Grainger, J. and Jacobs, A., editors,Localist connectionist ap-
proaches to human cognition, pages 327–355. Lawrence Erlbaum Associates.
Myung, J. I., Navarro, D. J., and Pitt, M. A. (2006). Model selection
by normalized maximum likelihood.Journal of Mathematical Psychology,
50(2):167–179.
P¨ otscher, B. M. and Leeb, H. (2009). On the distribution of penalized max-
imum likelihood estimators: The lasso, scad, and thresholding.Journal of
Multivariate Analysis, 100(9):2065–2082.
Pringle, R. and Rayner, A. (1971).Generalized inverse matrices with applica-
tions to statistics. Charles Griffin and Company, London.
Rao, C. (1990).Linear statistical inference and its applications. John Wiley
and Sons, second edition edition.
Rao, C. and Toutenberg, H. (1999).Linear models: least squares and alterna-
tives. Springer.
Rissanen, J. (1986). Stochastic complexity and modeling.The Annals of
Statistics, 14:1080–1100.
Schott, J. R. (1997).Matrix analysis for statistics. New York: John Wiley &
Sons.
Schwartz, G. (1978). Estimating the dimension of a model.The Annals of
Statistics, 6:461–464.
Searle, S. (1971).Linear Models. John Wiley and Sons, New York.
Seber, G. A. and Lee, A. J. (2012).Linear regression analysis, volume 936.
John Wiley & Sons.
Shah, R. D. and B¨ uhlmann, P. (2023). Double-estimation-friendly inference
for high-dimensional misspecified models.Statistical Science, 38(1):68–91.
Tibshirani, R. (1996). Regression shrinkage and selection via the lasso.Journal
of the Royal Statistical Society. Series B (Methodological), 58(1):267–288.
Vaart, A. v. d. (1998).Asymptotic Statistics. New York: Cambridge University
Press.
25

van de Geer, S., B¨ uhlmann, P., Ritov, Y., and Dezeure, R. (2014). On asymp-
totically optimal confidence regions and tests for high-dimensional models.
The Annals of Statistics, 42(3):1166–1202.
Vershynin, R. (2018).High-dimensional probability: An introduction with ap-
plications in data science, volume 47. Cambridge University Press.
Vuong, Q. H. (1989). Likelihood ratio tests for model selection and non-nested
hypotheses.Econometrica: Journal of the Econometric Society, pages 307–
333.
Wainwright, M. J. (2009). Sharp thresholds for high-dimensional and noisy
sparsity recovery using-constrained quadratic programming (lasso).IEEE
Transactions on Information Theory, 55(5):2183–2202.
Waldorp, L. and Haslbeck, J. (2024). Network inference with the lasso.Mul-
tivariate Behavioral Research, 12(in press):1–20.
Waldorp, L. and Marsman, M. (2021). Relations between networks, regression,
partial correlation, and the latent variable model.Multivariate Behavioral
Research, pages 1–13.
White, H. (1980). Using least squares to approximate unknown regression
functions.International Economic Review, 21(1):149–170.
Appendix
A Gaussian graphical model
The Gaussian graphical model (GGM) is characterised by the correspondence
between a network ofpnodes, labeledj= 1,2, . . . , pand a set of random
variablesX 1, X2, . . . , Xp that are jointly Gaussian (multivariate normally)
distributed (Koller and Friedman, 2009). The edges in a GGM correspond
to conditional dependence between nodes (given all reamining variables). The
Gaussian distribution is completely described by its meansµ j and covariances
σij. The inverse of the covariance matrix Σ = (σ ij, i, j= 1,2, . . . , p), denoted
by Σ−1 = Θ, contain the partial covariances. The partial covarianceθ ij is de-
fined as the covariance between the residuals of nodesiandjwhen all other
variables (notiandj) have been regressed out (Lauritzen, 1996). In a GGM
a partial covariance of 0 is equal to conditional independence. We show this
by example.
Consider three Gaussian variables with mean 0 and covariance matrix Σ.
We write the density of the three variables asf 123 and the conditional density
asf 13|2 for the joint density of variablesX 1 andX 3 givenX 2. We will want
to come to the conclusion that the product of the conditional distributions
f1|2f3|2 is the same as the conditional distributionf 13|2. To do this we consider
26

an example with covariance and inverse covariance matrix, respectively,
Σ =

 3/4−1/2 1/4 −1/2 1−1/2
1/4−1/2 3/4

 and Θ =

 2 1 0 1 2 1
0 1 2

 .
Note the 0 atθ 13 =θ 31 such that variablesX 1 andX 3 are conditionally inde-
pendent givenX 2. In terms of the distribution this implies the following. So
this implies that we have the densityf 13|2. We now compute this from the den-
sity of thew corresponding conditional Gaussian distribution. The distribution
with Θ is
f123(x) = 1q
(2π)3
q
det(Θ) exp

− 1 2 x⊤Θx  ,
where the term in the exponential is
x⊤Θx= 2x 2 1 + 2x2 2 + 2x2 3 + 2x1x2 + 2x2x3.
Note that becauseθ 13 = 0 there is no term 2x 1x3 and that is why we can
rewrite the density. If we take the density ofX 1 andX 2, using the first two
rows and columns of Θ and calling that Θ 12, then we obtain
f12(x1, x2) = 1 2π det(Θ12) exp  − 1 2 (2x2 1 + 2x1x2 + 2x2 2)  .
And similarly for the density ofX 2 andX 3 with Θ 23 the second and third
rows and columns of Θ, gives
f23(x2, x3) = 1 2π det(Θ23) exp  − 1 2 (2x2 2 + 2x2x3 + 2x2 3)  .
The density of onlyX 2, ignoring the other two variables is
f2(x2) = 1√ 2π Θ22 exp  − 1 2 2x2 2  .
Then we find (after some algebra) that
f12f23
f2
=f 123 ⇐ ⇒ f12f23
f2f2
=f 1|2f3|2 =f 13|2.
And we see that if a conditional covarianceθ ij = 0, then there is a conditional
independence. This is true only for the multivariate normal distribution.
Hence, the GGM is particularly attractive for graphical models because
whenever the partial correlation between variablesX i andX j is 0, thenX i
andX j are conditionally independent given all other variables (Lauritzen,
1996, Proposition 5.2). Hence, an edge in the GGM is present if and only
27

if the partial correlation is non-zero. The partial correlation is a function of
the inverse covariance matrix and has elementsθ ij. The partial correlation
betweenX i andX j is defined by (Koller and Friedman, 2009; Epskamp and
Fried, 2018)
ρij|⋆ =− θijq
θiiθjj
,
where⋆indicates all remaining variables in the network exceptiandj. If
ρij|⋆ = 0, then no edge should be present between nodesiandjin the network.
A GGM can be interpreted as a network where a correlation corresponds to a
(set of) path(s) between two nodes (Jones and West, 2005).
We can determine whether a partial correlation also by considering the
regression coefficientsβ ij from the regression
Xi =
X
j̸=i
Xjβij +e i,
where the sum is over all nodesjthat are noti. The reason for the correspon-
dence between the partial correlation and the regression coefficient is that
(Lauritzen, 1996)
βij =− θij
θii
.
Hence, wheneverβ ij = 0 then alsoθ ij = 0 and vice versa. We can, therefore,
consider each node in turn and determine the non-zero coefficients of the
regressions. Because we have bothβ ij andβ ji we will have to decide to use
theand-rule, where bothβ ij andβ ji are non-zero to include the edge (i, j),
or theor-rule, where eitherβ ij orβ ji is non-zero to include the edge (i, j)
(Meinshausen and B¨ uhlmann, 2006).
B Excess risk and mean squared error (Section 4)
We defined the excess risk as
R(J) =E
h
(Y0 −X ⊤ 0 ˆβJ )2 −(Y 0 −X ⊤ 0 βS)2
i
=E
h
(Y0 −X ⊤ 0 ˆβJ )2
i
−E
h
(Y0 −X ⊤ 0 βS)2
i
.
where the expectation is conditional on the training dataX. This is equivalent
to the risk defined in Hastie et al. (2022) and Bartlett et al. (2021). Then we
obtain the following decomposition.
Lemma B.1(Mean squared error decomposition)Assume that the linear
model (4) is correct. The excess risk (test mean squared error) can be de-
28

composed asR(J) =B(J) +V(J)in (6) with
B(J) = (β S −E ˆβJ )⊤Σ(βS −E ˆβJ ), V(J) =E( ˆβJ −E ˆβJ )⊤Σ( ˆβJ −E ˆβJ ),
whereB(J)is called the squared bias andV(J)is called the variance.
ProofAssuming that the linear model is correct, so thatEY 0 −X ⊤ 0 βS = 0,
we get
R(J) =E
h
(Y0 −X ⊤ 0 βS +X ⊤ 0 (βS − ˆβJ ))2
i
−E
h
(Y0 −X ⊤ 0 βS)2
i
=E

X ⊤ 0 (βS −E ˆβJ )−X ⊤ 0 ( ˆβJ −E ˆβJ ) 2
This gives
R(J) =E

X ⊤ 0 (βS −E ˆβJ ) 2 +E  X ⊤ 0 ( ˆβJ −E ˆβJ ) 2
−2E(β S −E ˆβJ )⊤X0X ⊤ 0 ( ˆβJ −E ˆβJ )
Recalling that (X, Y) and (X 0, Y0) are independent, we obtain for the cross
product
E(βS −E ˆβJ )⊤X0X ⊤ 0 ( ˆβJ −E ˆβJ ) = (βS −E ˆβJ )⊤ΣE( ˆβJ −E ˆβJ ) = 0,
becauseE( ˆβJ −E ˆβJ ) = 0, and where Σ =E(X 0X ⊤ 0 ), which is the same as the
covariance matrix of the predictorsE(X ⊤X). Then we obtainB(J) andV(J)
in (7) from the two remaining terms.2
This is the famous variance and squared bias decomposition (Hastie et al.,
2022).
Next, we show the formulation of the bias and variance of the MSE with
the ridge estimator ˆβ=W(α)X ⊤Y, whereW(α) = (X ⊤X+αI).
Lemma B.2Assume that the linear model (4) is true and thatΣ =σ 2 ξ Iis
the covariance matrix of the covariates. Then the squared bias is
B(J) =σ 2 ξ γ1α2 (λ1 +α) 2 +σ 2 ξ nX j=2 α2 (λj +α) 2 .
ProofRecall that the expectation is conditional onXand (X 0, Y0) and
(X, Y) are independent. Plugging in the ridge estimator (3) in the bias term
and assuming Σ =σ ξI, yields
B(J) =E(β S −E ˆβJ )⊤X ⊤ 0 X0(βS −E ˆβJ )
= tr(βS −W(α) −1X ⊤Xβ S)(βS −W(α) −1X ⊤Xβ S)⊤E(X ⊤ 0 X0)
= tr((I−W(α) −1X ⊤X)β S)((I−W(α) −1X ⊤X)β S)⊤Σ
=σ 2 ξ tr(I−W(α) −1X ⊤X) 2βSβ⊤ S .
29

Letλ j be the eigenvalues ofX ⊤Xandγ 1 be the only non-zero eigenvalue of
βSβ⊤ S . Then, noting thatU ⊤U=I, we obtain forW(α) =X ⊤X+αIthe
eigenvalue decomposition forW(α) isUΛ(α)U ⊤ with diagonal matrix Λ(α)
with elementsλ j +α. The squared inverseW(α) −2 is thenUΛ(α) −2U ⊤ with
diagonal matrix Λ(α)−2 with elements 1/(λj +α) 2. Plugging this in the above
result, we obtainB(J). This completes the proof.2
Lemma B.3Assume that the linear model (4) is true and thatΣ =σ 2 ξ Iis
the covariance matrix of the covariates. Then the variance is
V(J) =σ 2 ξ σ2 e
nX
j=1
λj
(λj +α) 2 .
ProofAgain, we note that the expectation is conditional onXand (X 0, Y0)
and (X, Y) are independent. Plugging in the ridge estimator (3) in the variance
term and assuming Σ =σ ξI, yields
V(J) =Etr( ˆβJ −E ˆβJ )( ˆβJ −E ˆβJ )⊤X ⊤ 0 X0
= tr(W(α) −1X ⊤Y−W(α) −1X ⊤Xβ S)
×(W(α) −1X ⊤Y−W(α) −1X ⊤Xβ S)⊤E(X ⊤ 0 X0)
= trW(α) −2(X ⊤(Xβ S +e−Xβ S))(X ⊤(Xβ S +e−Xβ S))⊤Σ
=σ 2 ξ σ2 e tr(W(α) −2X ⊤X),
where we used that the variance of the residualseisσ 2 e I. Similar to Lemma
B.2 we use that the eigenvalue decomposition forW(α) isUΛ(α)U ⊤ with
diagonal matrix Λ(α) with elementsλ j +α. The squared inverseW(α) −2 is
thenUΛ(α) −2U ⊤ with diagonal matrix Λ(α) −2 with elements 1/(λ j +α) 2.
Plugging this in the above results, we obtainV(J). This completes the proof.
2
B.1 Model misspecification
Misspecification is defined with respect to a family of models. LetMdenote
a class of probability distributions that are indexed by parametersθ∈Θ⊆
Rp, i.e.,M={p θ :θ∈Θ}(we assume that the probability distribution is
dominated by Lebesgue measure so that a densitypθ exists, Jacod and Protter,
2004). An example of a model is a class of normal distributions with meanµ
and varianceσ 2, where the mean is generated by a nonlinear function, such as
f:R p×Rp →Rsuch thatx7→1/(1+exp(−x ⊤β)); thenθ= (β, σ 2) is thep+1
dimensional parameter vector. Furthermore, letM lin ⊂ Mbe a strict subset
consisting of only those distributions where the conditional meanE(Y|x) is
generated by a linear functionx7→x ⊤β. We say that a model is misspecified
30

if the correct distribution is not in the class of probability distributions we
consider in the optimisation (Vaart, 1998; Gr¨ unwald, 2007; Kleijn, 2026), i.e.,
p0 /∈ Mlin, wherep 0 =p θ0. In our setting, this means that the distribution
has a mean that is generated by a nonlinear function, while we use only a
linear function for optimisation. In such a case, the linear modelx ⊤ ˆβcan be
interpreted as corresponding to a densityp θ that is closest withinM lin to
p0 inMin terms of Kullback-Leibler divergence (Vuong, 1989; Vaart, 1998).
Here we have suppressed the variance parameterσ 2 of the residualsY−f,
wherefis the true linear model for the conditional mean. However, seminal
work by Gr¨ unwald and van Ommen (2017) shows that misspecification using
linear models, as we do here, also leads to misspecification of the varianceσ 2
(i.e., it depends on the value ofx), and leads to non-convexity of the model
spaceM lin. This in turn leads to models that can be combinations of linear
models (like with variance depending onx) that are in the convex hull of the
model spaceM lin and are closer to the true generating model not inM lin than
any model inM lin itself; Gr¨ unwald and van Ommen (2017) called this bad
misspecification.
We approximate a functionfby a linear functionXβwithβ∈R p and
p > nvery large.
Lemma B.4(Mean squared error for misspecification)Assume that the true
functionf:R p ×R p →R, andY=f(X, β S) +e, withβ S the true parameter
vector inf. We estimatef(X, β S)byXβ J with|J|=p > n. Then the risk
under model misspecification is
Rf (J) =E
h
(f(X 0, βS)−E(X ⊤ 0 ˆβJ )2
i
+E
h
(f(X 0, βS)−E(X ⊤ 0 ˆβJ )2
i
+ 2E
h
(Y0 −f(X 0, βS))(f(X 0, βS)−X ⊤ 0 ˆβJ ) i
which we refer to asR f (J) =B f (J) +V f (J) +M f (J).
ProofThe proof follows Lemma B.1 except that the cross products do not
vanish because of misspecification. We have that the excess risk is
Rf (J) =E
h
(Y0 −f(X 0, βS) +f(X 0, βS)−X ⊤ 0 ˆβJ ))2
i
−E
h
(Y0 −f(X 0, βS))2
i
.
Working out the cross products cancelsE[(Y 0 −f(X 0, βS)2], without assuming
that the model is correct. What remains isB f (J),V f (J), similarly obtained
as in Lemma B.1, but the cross product that remains is
Mf (J) = 2E
h
(Y0 −f(X 0, βS))(f(X 0, βS)−X ⊤ 0 ˆβJ ) i .
This was to be proved.2
Proposition B.5(Misspecification bound)Assume the model with additive
noiseY=f(X, β S) +e, where the conditional meanE(Y|x)is given by the
31

function isf:R p ×R p →Rande=Y−f(X, β S)has mean zero and finite
varianceσ 2. Furthermore, we estimatef(X, β S)byXβ J with|J|=p > n,
and assume that the approximation error is bounded in probability byK, i.e.,
f(X 0, βS)−X ⊤ 0 ˆβJ =O p(K). Then the misspecification is bounded by
Mf (J) = 2E
h

(Y0 −f(X 0, βS))(f(X 0, βS)−X ⊤ 0 ˆβJ )

 i ≤2σO(K)
ProofBy the Cauchy-Schwarz theorem we can bound the expectation of the
product, and so,
E
h
|e(f(X 0, βS)−X ⊤ 0 ˆβJ )| i2 ≤E(e 2)E h (f(X 0, βS)−X ⊤ 0 ˆβJ )2 i
where we used thatY 0 −f(X 0, βS) =e. By assumption,ehas mean 0 and
varianceσ 2, and soE(e 2) =σ 2. For the second term, we assumed that
f(X 0, βS)−X ⊤ 0 ˆβJ =O p(K), and so
E
h
(f(X 0, βS)−X ⊤ 0 ˆβJ )2
i
=E
h
Op(K) 2
i
=O(K 2)
Taking the square root of the product gives the required bound.2
C High-dimensional space
For some intuition on high-dimensional spaces, the isotropic Gaussian, i.e.,
with mean 0 and variances of 1 and covariances of 0, is convenient. LetXbe a
Gaussian random variable of dimensionpwith mean 0 and isotropic covariance
matrixE(XX ⊤) = Σ of dimensionsp×p. We will consider an inequality that
shows that with high probability, for large dimensionpmost of the draws
from an isotropic distribution are at √p, the radius of the spheroid of the
distribution.
We can make this clear by considering the probability of an observation
falling within a certain bound of the origin (Vershynin, 2018, Chapter 3).
Suppose we are interested in the length (norm) of the vectorXinpdimensions,
i.e., we want to know the probability of||X|| 2 =
√
X 2 1 +X 2 2 +· · ·X2 p being
smaller than √p. It is intuitive that the length ofXis indeed √pbecause
E||X|| 2 2 =E
pX
j=1
X 2 j =
pX
j=1
EX 2 j =p.
So, we should expect many of the values of the square||X|| 2 2 to be around √p.
Suppose we are considering the probability ofXbeing near 0, i.e.,||X|| 2 ≈0.
Then we find that
P(|||X|| 2 − √p| ≤t)≈P( √p≤t).
32

0 5 10 15 20 25 30
0 1 2 3 4 5
dimension p
volume p-ball
0 50 100 150 200 250 300
0.0 0.2 0.4 0.6 0.8 1.0
dimension p
fraction near surface
(a) (b)
Fig. C.1. In (a) we see that, indeed, the volume of ap-dimensional ball with radius 1
in high dimensions gets smaller and smaller, already arep= 20 is the volume close
to 0. In (b) is the consequence of this, where we see that the fraction of observations
from an isotropic distribution near the surface increases exponentially to 1.
So, for small valuest, say 1 or 2, the probability can only be high ifpis small.
Another way to consider this is by looking at the volume of ap-dimensional
ball. The volume of thep-dimensional ball in Euclidean spaceR p with radius
ris (Giraud, 2014, Section 1.2)
Bp(r) = πp/2
Γ(p/2 + 1)rp ≈

2πer2
p
!p/2
1
pπ for largep,(C.1)
where Γ is the Gamma function Γ(α) =
R ∞
0 tα−1e−tdtandα >0. Figure C.1(a)
shows that the volume of the ball is close to 0 already when the dimension
is about 20. Moreover, Figure C.1(b) shows that most of the points from the
Gaussian isotropic distribution will be near the surface of thep-dimensional
ballB p(√p). The figure shows the fraction of the points outside an innerp-
dimensional ball of radius 0.95r, so very close to the ball of radiusr. The
fraction increases to 1 exponentially fast (Giraud, 2014). Already atp= 30
the fraction in the last 5% of the ball is nearly 80%. This shows that most of
the points will be near the surface of thep-dimensional ball.
D Geometry and metric entropy of Gaussian process (Section 5)
Here we first prove that the the ratio of signal and noise volumes can, for
linear models in the high-dimensional setting, be written in terms of the ridge
estimator. This also implies that the ridge parameterαcan be interpreted as
the inverse of the signal to noise ratio.
33

Lemma D.1(Volume linear model)We assume the linear modelXβwhere
Xis ann×pmatrix andβis ap-dimensional vector, such thatY=Xβ+e
andeis Gaussian with mean 0 and varianceσ 2 e I. The volume ratio of the
linear model with ridge regression with respect to the noiseeis
vol(Xβ)
vol(e) =
q
det(X ⊤X+αI p),
whereα −1 =||β|| 2 2/σ2 e .
ProofLet vol(β) =B n(√n||β||2) be then-dimensional ball with radius √n||β||2.
Compared to the volume of the noiseB(
√
nσ2), we obtain the ratio
vol(Xβ)
vol(e) =
q
det(XX ⊤) Bn(√n||β||2)
Bn( √ nσ2 e ) .
Ann-dimensional ballB n(r) with radiusrcan be written in terms of then-
dimensional ball with radius 1:B n(1)rn. Hence we find for the ratio of volumes
vol(Xβ)/vol(e)
q
det(XX ⊤)

||β||2 2
σ2 e
!n/2
=
q
det(α−1XX ⊤),
whereα −1 =||β|| 2 2/σ2 e is the signal-to-noise-ratio (SNR).
It turns out that whenp > nwe obtainX ⊤(XX ⊤)Yas the so-called
minimum norm estimate ˆβM N ofβ(Ben-Israel and Greville, 1974; Bartlett
et al., 2021). The minimum-norm solution is related to the ridge estimator as
follows
lim
α→0+
(X ⊤X+αI) −1X ⊤ =X ⊤(XX ⊤)−1.
Intuitively, the minimum-norm solution is obtained for the smallestαthat
makes the augmented inverse ofX ⊤Xpossible. It is therefore reasonable to
substitute forXX ⊤ the ridge versionX ⊤X+αI, whereαis small. Hence,
we obtain the volume ratio vol((X ⊤, √αI) ⊤β)/vol(e) with the ridge version
(Cheema and Sugiyama, 2020)
q
det(α−1XX ⊤ +I n) =
q
det(X ⊤X+αI p),
by the Weinstein–Aronszajn identity.2
Becauseα= 1/SNR =σ 2 e /||β||2 2, we obtain smallα, close to the minimum-
norm estimate, if we have high signal||β|| 2 2.
Clearly, the tuning parameterαcan be expressed as the inverse of the
signal-to-noise ratio (SNR). The SNR is defined as the ratio of the Euclidean
length of the parameters (||β|| 2 2, see Appendix 2.2) and the noise varianceσ 2 e ;
34

thenα= 1/SNR and SNR =||β|| 2 2/σ2 e . The Euclidean length is a representa-
tion of the volume for the variablesβ. So, if we restrict||β|| 2 2 to be no larger
thanc(ridge regression), then we are restricting the volume of the possible
values that the parameters inβcan take. This implies that when we increase
the volume (||β|| 2 2) we reduce the tuning parameterα, and hence penalise the
regression less. This can be interpreted as follows: imposing a higherαin ridge
regression will lead to decreased variance (this was shown in Section 4). This
also implies that the peak at the interpolation point in Figure 3 is an artifact
of applying a suboptimal tuning parameter (see Figure H.1, where in the mid-
dle row the peak has disappeared upon careful selection ofα). Summarising,
we can say the following.
(a) We can increaseαdirectly, reducing the test variance, and hence obtain-
ing reasonable test MSE. This leads indirectly to a lower SNR (because
α= 1/SNR); or
(b) we can constrain the size of||β|| 2 in the ridge estimator, therefore, de-
creasing the model complexity (volume) of the model. This will reduce
SNR and hence, increaseα, leading to a decrease in the test variance.
We do this by constraining the ridge estimator with smallcsuch that
||β||2 ≤c.
In both cases (a) and (b) we are either directly or indirectly constraining the
total signal||β|| 2. In model selection this can be done by either increasingα, or
equivalently, decreasingcin the ridge constraint||β|| 2 ≤c, or by incorporating
the complexity (volume) of the model (then-dimensional ballB n(||β||2), see
Appendix D).
E Akaike information criterion
For the derivation of the Akaike information criterion (AIC), we follow Claeskens
and Hjort (2008). The AIC can be derived from the Kullbeck-Leibler diver-
gence (KL). The KL is a way to quantify the overlap between two distributions.
The KL is 0 if the distributions are the same (almost surely) and is>0 if
they are not the same. Hence, the AIC aims to minimise the KL across the
different models.
Letfandgbe two densities, where we designategas the true underlying
distribution and we usefas an approximation. In practice we estimate a
parameter ˆβthat we plug-inf, denoted byf(·, ˆβ). The KL is forfandg
defined as (Kullback and Leibler, 1951; Cover and Thomas, 2006)
KL(f, g) =EY|x logg(Y|x)−E Y|x logf(Y|x, ˆβ),
whereE Y|x indicates the expectation overYconditional onx(the values
of the predictors in the nodewise GGM). Across different models the term
EY|x logg(Y|x) is fixed and so we concentrate on the second term. So, max-
imising the second term of the KL equals minimising the KL itself. The ex-
35

pectation of this second term is
L=E X

EY|x logf(Y|x, ˆβ)

.
The AIC tries to estimate this expectation and then select the model with
the highest value (and hence the minimal value of KL). This expectation is
estimated by the log-likelihood 1 n L( ˆβ) = 1 n Pn i=1 f(Y i |x i, ˆβ). And it can then
be shown that this estimate is biased and needs to be corrected, since
E( 1 n L( ˆβ)−L)≈ p n and, hence 1 n (−2L( ˆβ) + 2p).
Discarding the 1/nleads to the standard AIC.
Here, for the GGM we used the Gaussian distribution forf. Then (Seber
and Lee, 2012)
nX
i=1
logf(Y i |x i, β) =
nX
i=1
− 1 2σ2 (Yi −x ⊤ i β)2 − n 2 logσ 2 − n 2 log 2π.
Plugging in our ridge estimate ˆβJ for modelJ(see (3)), multiplying by -2 and
ignoring constants, we obtain the AIC
AIC(J) =nlog ˆσJ + 2pJ ,
wherep J is the number of parameters for modelJand
ˆσ2 J = 1 n nX i=1 (yi −x ⊤ i ˆβJ )2
is plugged in forσ 2. The standard AIC has a fixed (independent of the data)
value of the ridge parameterα. The AIC-CV has a ridge parameterαthat
has been obtained withk-fold cross validation.
F Minimum description length: optimised
The minimum description length (MDL) principle has been extended to the
high-dimensional setting ofn < pin another way than in Section 5.1. The
principle of approximating the code length for the data given the model and
the code length for the model is the same, but in order to account for the
high-dimensions (such thatd/n→γ <∞), the effective degrees of freedom
are used in combination with an optimalαfor the effective degrees of freedom
(Dwivedi et al., 2020). The MDL is then obtained by minimising a function
forαthat gives the smallest MDL value. The function to be optimised overα
is
MDL-opt = n 2 log ˆσ2 + 1 2ˆσ2 || ˆβ||2 2 + min{n,d}X j=1 log  1 + λj α ! ,
36

whereλ j are the eigenvalues ofX ⊤Xand ˆβis the ridge estimator with value
α. The second term is included here because of the Bayesian interpretation
of MDL in Dwivedi et al. (2020), where this term is entered as a prior forβ.
This version of MDL is referred to as MDL-opt.
G MDL leads to underfit in high-dimensional settings
Proposition5.1 LetSdenote the true support for a (possibly nonlinear) data
generating process ofY i fori= 1, . . . , nwithnfixed, and letJrepresent the
set of predictors such thatS⊂J, where|S|=dand|J|=p. We test linear
modelsXβ J for anyJ(includingS) by MDL as given in (10) with (11). Let
pincrease andp > d. IfEˆσ 2 J > γ, for someγ >0, then with probability at
least 1− d p exp(−(p−d)) it holds that ˆS⊆S; equivalently, the probability of
false positives goes to 0.
ProofWe first note that
P( ˆS⊆S) =P(min
J
MDL(J)≤MDL(S) :|J| ≥ |S|)
And using the complement rule and exponentiation we can rewrite this as
1−P(min
J
exp[MDL(S)−MDL(J)]<1 :|J| ≥ |S|)
Then we apply Markov’s inequality to show that ford=|S| ≤ |J|=p
P(exp[MDL(S)−MDL(J)]<1)≤E(exp[MDL(S)−MDL(J)])
We start with the first part of the MDL, the log of the empirical variance,
defined as (using maximum likelihood) ˆσ 2 J = 1 n ||Y−X ⊤ ˆβJ ||2. For models
withp=|J| ≥ |S|, we have that the in-sample variance is ˆσ 2 J ≤ˆσ2 S P-a.e.
(Bilodeau and Brenner, 1999), and soEˆσ2 J ≤Eˆσ2 S by monotonicity. Therefore,
and because both terms are positive, using Jensen’s inequality for concave
functions such thatE(logX)≤logE(X), we obtain that
0≤Elog ˆσ 2 S −Elog ˆσ2 J ≤logEˆσ2 S −logEˆσ2 J = log Eˆσ2 S Eˆσ2 J
The expectationE 1 n ||Y−X ⊤ ˆβJ ||2 under the true model isσ 2 +E 1 n ||f(X, βS)−
X ⊤ ˆβJ ||2, and similarly for the expectationσ 2 +E 1 n ||f(X, βS)−X ⊤ ˆβJ ||2, which
are bounded by the assumption on misspecification in Lemma B.4. Using
monotonicity above and the assumption thatEˆσ2 J >0 is bounded away from 0,
the ratio above is positive and bounded byK/γ, with|f(X, β S)−X ⊤ ˆβS|< K.
Then we move on to the next part tr(S J ) lognof MDL. In the setting
of linear regression, we have that the sets of predictors in the design matrix
37

X= (x 1, x2, . . . , xp) are nested, so thatS⊆Jfor|J| ≥ |S|. For a fixedα >0,
n >|S|=d, and|J|=p > n, we obtain
tr(SS) =
dX
j=1
λj
λj +α ≤
nX
j=1
λj
λj +α = tr(SJ )≤
dX
j=1
λj
λj +α + (n−d) 1 α
sinceλ j ≥0. Then, for the difference between these two MDL parts we obtain
(tr(SS)−tr(S J )) logn≤ −(n−d) 1 α logn
For the last part of MDL, we use a result by Cheema and Sugiyama (2020,
Theorem 3)
E

log det(X⊤X+αI) + logB p(||β||2)/σp

≤logd+ n 2 log(α+ 1) + logB p(1)
BecauseB p(1)≤B d(1), whered=|S| ≤ |J|=p, we obtain that
log Bd(1) Bp(1) = logπ −(p−d)/2 exp(−(p−d)/2) +O(d/p)
where we used Stirling’s approximation for factorials and the approximation
of the Euclidean ballB p(1) given in (C.1).
Putting the three elements together gives the upper bound on the expec-
tation
log Eˆσ2 S
Eˆσ2 J + logn −(n−d)/α + log d p + logπ −(p−d)/2 exp(−(p−d)/2)
Since the first term is bounded byK/γ, we observe that the above is dominated
by the last term, which goes to 0 aspincreases. In particular, we find that
π−(p−d)/2 exp(−(p−d)/2)≤ d p exp(−(p−d))
Consequently, we obtain that
E(exp[MDL(S)−MDL(J)])→0
And, therefore, aspincreases
P( ˆS⊆S) =P(min
J
MDL(J)≤MDL(S) :|J| ≥ |S|)≤1− d p exp(−(p−d))
as was to be shown.2
38

H Simulation details
In the case where the true model is linear we havef(X) =Xβ. In the
misspecified case we used instead of the linear model the sigmoid function
f(X) = 1/(1 + exp(Xβ)). Again we keepd= 5 non-zero coefficients fixed.
The coefficientsβwere normalised so that theL 2 norm was 1, i.e.,||β|| 2 = 1.
The signal-to-noise ratio (SNR) is defined as||β|| 2 2/σ2, the ratio of the variance
of the signal (coefficients) and the noise variance. Since we fix||β|| 2 2 = 1, the
variance of the noise determines the SNR, set to 2, so that the noise variance
is 0.5. The number of generated observations is fixed atn= 40.
For estimation we selected a fraction of 0.80 for training (estimation) of
parameters and the remaining 0.20 for testing. We fixn= 40 observations in
total, and so obtainn train = 32 andn test = 8. We fix the dimension of the true
model atd= 5 and vary the number of parameterspfrom 3 to 320. Hence we
obtain the ratiop/nfor training data from 0.09 to 10, where the last setting
means we have ten parameters per observation. With fixedd= 5 we have that
the correct ratiop/nis at 5/32 = 0.15625.
The ridge estimate is either obtained with parameterα= 0.5, or the ridge
estimate is obtained withαestimated with 10-fold cross-validation, with theα
with the smallest MSE. The Lasso is obtained with parameterαfrom 10-fold
cross-validation. Estimation was performed with theRpackageglmnet.
I Residuals in training and test samples
The interpolation point atp=nis the point where it is possible that each
datapoint is captured by the model in the training set, also in the linear case.
We see this in Figure I.1(a), where the residuals of the training (estimation)
data as a function of the predicted values ˆYare plotted. Here, the true number
of non-zero coefficients is 5 but in the overparameterised case we usep= 64.
As seen, the training residuals are 0 and so ˆYS = P j∈S Xjβis the same as
ˆYJ = P j∈J Xj ˆβJ , where ˆβJ is the ridge estimate for modelJand modelJ
contains all 64 predictors. Because the observations are predicted exactly, it
was assumed that the variance of the residuals on a test set would be large.
Figure I.1(b) shows that this is not the case. There is some variance in the
residuals of the test set but not too much. The noise that ends up in the
predictors is “hidden” in the unimportant directions of the predictors because
of the ridge parameter (Bartlett et al., 2020).
39

test MSE bias-variance
ridge
p/n
log mse
0.5 1 1.5 2
0.1 0.3 1 3 7
ridge
in sample
p/n
log bias/variance
0.5 1 1.5 2
0 0.1 0.3 1 3
variance
bias
ridge cv
p/n
log mse
0.5 1 1.5 2
0.1 0.3 1 3 7
ridge cv
in sample
p/n
log bias/variance
0.5 1 1.5 2
0 0.1 0.3 1
variance
bias
lasso cv
p/n
log mse
0.5 1 1.5 2
0.1 0.3 1 3 7
lasso
in sample
p/n
log bias/variance
0.5 1 1.5 2
0 0.1 0.3 1 variance
bias
Fig. H.1. Test MSE (left column) and its decomposition in squared bias and vari-
ance. The top row is obtained with a fixed valueα= 0.0001, the middle row is
obtained with anαestimated using 10-fold cross-validation, and the bottom row is
obtained with the lasso, where also the penalty parameter is obtained with 10-fold
cross-validation.
40

-2 -1 0 1
-4 -2 0 2 4
y^
residuals training set
-0.5 0.0 0.5
-4 -2 0 2 4
y^
residuals test set
(a) (b)
Fig. I.1. Residuals of the training set (a), showing that the model with 64 predictors
(while correct is 5) is interpolating the data, fitting exactly each point. The residuals
of the test set (b) remain relatively small, indicating that the variance need not
explode beyond the interpolation point.
41
