---
title: Clustering based on Stochastic Dominance with application for risk averters and risk seekers
url: https://arxiv.org/abs/2605.24422
category: ai-marketing
subcategory: measurement
date: 2026-05
venue: ''
authors:
- Hua Li
- Xue Jia
- Yilin Kang
- Wing-Keung Wong
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.24422
pages: 44
chars: 93320
fetched_at: '2026-11-08T13:27:41+00:00'
kb_version: 1
---

# Clustering based on Stochastic Dominance with application for risk averters and risk seekers

Clustering based on Stochastic Dominance with
application for risk averters and risk seekers
Hua Lia, Xue Jiab, Yilin Kanga and Wing-Keung Wongc
aSchool of Science, Changchun University, Changchun, China.
bSchool of Mathematics and Science, Northeast Normal University, Changchun,
China.
Abstract
Stochastic Dominance (SD) theory provides a rigorous framework for
selecting superior assets tailored to the asset allocation needs of investors
with varying risk preferences (i.e., risk-averse, risk-seeking, and risk-
neutral). However, traditional stock clustering methods typically rely
on geometric metrics such as Euclidean distance, which often fail to effec-
tively capture the intrinsic risk dominance relationships among assets. To
address this limitation, this paper proposes an innovative clustering anal-
ysis framework based on SD test statistics. Methodologically, this study
deeply integrates SD theory with machine learning algorithms. Tran-
scending the limitations of traditional reliance on geometric distance, we
innovatively utilize test statistics from first-, second-, and third-order SD
to construct a ”Stochastic Dominance Coefficient Matrix.” Building upon
this matrix, we modify the classic K-means and Hierarchical Clustering
algorithms. Specifically, we derive 12 distinct algorithm variants tailored
to different orders of SD relationships. Simultaneously, we construct the
SD-SC coefficient and the SD-DBI index as specialized validity indices to
evaluate the clustering performance. Empirically, we analyze constituent
stock data from a representative developed market (the US NASDAQ In-
dex) and an emerging market (China’s CSI 100 Index). The results verify
the effectiveness and robustness of the proposed method. Furthermore, we
apply the clustering results to the modification of the Single Index Model
and the construction of Global Minimum Variance Portfolios (GMVP).
The findings demonstrate that the proposed method effectively facilitates
customized asset allocation for investors, holding significant theoretical
value and practical implications.
keywords:Stochastic Dominance; Stock Clustering; SD-K-means Clustering;
SD-Hierarchical Clustering; Portfolio Optimization; Risk Aversion; Risk Seek-
ing
1
arXiv:2605.24422v1  [stat.ML]  23 May 2026

1 Introduction
Stock clustering algorithms play a pivotal role in quantitative finance and
the asset management industry, serving as a core mechanism for understand-
ing market complexity and conducting asset preselection. Their intrinsic value
lies in enabling investors to identify the true underlying structure of the stock
market, thereby categorizing stocks with similar return characteristics or risk
profiles into distinct groups. This data-driven market segmentation not only
significantly reduces the computational dimensionality involved in portfolio con-
struction but also provides a solid foundation for formulating differentiated in-
vestment strategies.
A review of existing literature reveals that scholars both domestic and inter-
national have achieved fruitful results in stock clustering. Traditional clustering
research predominantly employs classic machine learning algorithms: Xiaojun
(2019) and Wu et al. (2022) utilized the K-means algorithm for stock partition-
ing; Huang et al. (2010) and Lu et al. (2020) explored the sectoral structures of
the SSE 50 Index and other markets based on Agglomerative Hierarchical Clus-
tering (AHC) and Spectral Clustering; Korzeniewski (2018) further introduced
the Partitioning Around Medoids (PAM) algorithm to construct portfolios with
enhanced risk resistance. In recent years, with the advancement of deep learn-
ing, L´ ucio and Caiado (2022) and Siregar and Yosia (2024) have attempted to
incorporate time-series models (such as TGARCH) or specific market features
(e.g., Indonesian stock data) into clustering frameworks. However, despite their
respective merits in capturing market trends, these methods share a common
limitation: traditional stock clustering approaches predominantly rely exclu-
sively on stock-specific information (e.g., price, volatility, or financial metrics),
neglecting the heterogeneity of market participants—namely, the ”investors”.
In reality, investors are typically categorized into three distinct types based
on their risk preferences: risk-averse, risk-seeking, and risk-neutral. Divergent
risk attitudes inevitably lead to fundamentally different asset selection logic.
In current literature, stock selection based on risk preferences often relies on
expert experience or heuristic indicators. For instance, Guy et al. (2014) utilized
decomposed Beta coefficients to assist risk decisions, while Bolos , et al. (2025)
defined ”defensive assets” based on financial metrics such as ROA and Gross
Profit Margin. Such approaches, while intuitive, often lack mathematical rigor
and are prone to subjective judgment. To overcome this defect, Stochastic
Dominance (SD) theory offers an ideal solution. In contrast to traditional Mean-
Variance analysis, SD theory does not require the assumption that returns follow
a normal distribution, nor does it restrict investors to quadratic utility functions.
Thus, it provides a mathematically rigorous framework for selecting superior
assets tailored to investors with varying preferences.
In the development of SD theory, McFadden (1989) first developed a test
for risk-averse populations using minimum/maximum statistics. Scholars such
as Klecan et al. (1991), Barrett and Donald (2003), and Linton et al. (2005)
subsequently refined this work by relaxing the Independent and Identically Dis-
tributed (IID) assumption. For risk-seeking populations, McAleer et al. (2006)
2

and Sriboonchitta et al. (2009) proposed corresponding test methods, and Bai
et al. (2015) integrated tests for both risk-averse and risk-seeking groups into
a unified framework. Despite the extensive application of SD theory in finance
(Levy (1985); Post (2003); Wong (2007)), its traditional applications are mostly
limited to pairwise asset comparisons or serving as constraints in optimization
problems. Directly applying SD to stock selection within the Chinese stock
market, which houses thousands of listed companies, would necessitate tens of
thousands of pairwise tests, resulting in a prohibitive computational burden
that is difficult to implement in practice.
To address these pain points—specifically, how to efficiently identify as-
set classes that align with specific risk preferences (risk-averse or risk-seeking)
within a large-scale market—this study innovatively proposes a clustering anal-
ysis method based on Stochastic Dominance test statistics. Distinct from tradi-
tional clustering that relies on Euclidean distance, we deeply integrate Stochastic
Dominance theory with machine learning algorithms:
1. First, we utilize the test statistics from first-, second-, and third-order
Stochastic Dominance associated with different investor preferences to construct
a core ”Stochastic Dominance Coefficient Matrix.”
2. Second, building upon this matrix, we propose improved SD-K-means
and SD-Hierarchical clustering algorithms. These new algorithms are capable
of automatically categorizing stocks according to specific investor preferences,
enabling investors to rapidly lock onto a desired pool of assets, thereby greatly
simplifying the subsequent portfolio construction process.
3. Furthermore, this paper introduces novel clustering validity indices
(SD-SC coefficient and SD-DBI index) specifically designed for these new mod-
els, further refining the theoretical framework of preference-based stock cluster-
ing.
The remainder of this paper is organized as follows: Section 2 introduces the
relevant theoretical background, including Stochastic Dominance tests and the
Bootstrap method. Section 3 details the construction process of the proposed
clustering algorithms based on SD theory, as well as the novel indices used for
evaluating clustering performance. Section 4 demonstrates the performance of
the proposed method through empirical research based on real-world market
data. Section 5 concludes the paper and discusses the practical implications
of this method for customized asset allocation as well as directions for future
research.
2 SD Test and Bootstrap Method
2.1 ASD(DSD) theorem
we letXandYbe random variables defined on [a, b] with cumulative distri-
bution functions (CDFs)FandG, and probability density functions (PDFs),f
3

andg, respectively. We define
h(x) =H A 0 (x) =H D 0 (x)
H A j (x) =
Z x
a
H A j−1(y)dy, j= 2,3
H D j (x) =
Z b
x
H D j−1(y)dy, j= 2,3
(2.1)
whereH=ForGandh=forg.µ F =µ X =
R b
a xdF(x) is the mean ofX
andµ G =µ Y =
R b
a xdG(x) is the mean ofY.
We note thatH A j in (2.1) can be used to develop the SD theory for risk
averters and thus we call this type of SD the ascending SD (ASD) and callH A j
thejth order ASD integral or thejth order cumulative probability, sinceH A j
is integrated fromH A j−1 in ascending order from the leftmost point of downside
risk. On the other hand,H D j in (2.1) can be used to develop the SD theory for
risk seekers and thus we call this type of SD the descending SD (DSD) and call
H D j thejth order DSD integral or thejth order reversed cumulative probability,
sinceH D j is integrated fromH D j−1 in descending order from the rightmost point
of upside profit. so we give the defination as follows Li (2013):
Definition 2.1GiveXandYbe random variables with cumulative distribution
functions (CDFs)FandG, in the sense of F ASD (SASD, TASD),Xdominance
YorFdominanceG, denoteX⪰ A 1 YorF⪰ A 1 G(X⪰ A 2 YorF⪰ A 2 G,X⪰ A 3
YorF⪰ A 3 G), if and only if, anyx∈[a, b],F A 1 (x)≤G A 1 (x)(F A 2 (x)≤G A 2 (x),
F A 3 (x)≤G A 3 (x)), where F ASD, SASD, TASD respectively represet First-order,
Second-order, Third-order ascending stochastic dominance.
Definition 2.2GiveXandYbe random variables with cumulative distribu-
tion functions (CDFs)FandG, in the sense of FDSD (SDSD, TDSD),X
dominanceYorFdominanceG, denoteX⪰ D 1 YorF⪰ D 1 G(X⪰ D 2 Y
orF⪰ D 2 G,X⪰ D 3 YorF⪰ D 3 G), if and only if, anyx∈[a, b],
F D 1 (x)≥G D 1 (x)(F D 2 (x)≥G D 2 (x),F D 3 (x)≥G D 3 (x)), where FDSD, SDSD,
TDSD respectively represet First-order, Second-order, Third-order descending
stochastic dominance.
The ASD and DSD approaches are regarded as two of the most useful tools
for ranking uncertain investment prospects, Li and Wong (1999) has shown that
ranking assets is equivalent to utility maximization for both risk averters and
risk seekers. The existence of ASD implies that the expected utility of the risk-
averse investor is always higher when holding the dominant asset than when
holding the dominated asset, and consequently, the dominated asset would not
be chosen. The same is true for DSD (Bai et al., 2015).
4

2.2 Stochastic Dominance Test
According to the definition of ASD and DSD, we can test the following null
hypothesis forj= 1,2,3:
H A(D) 0 :F A(D) j ≡G A(D) j (2.2)
Three opposing hypotheses:
H A(D) 1 :F̸≡ A(D) j G
H A(D) 1l :F≻ A(D) j G
H A(D) 1r :F≺ A(D) j G
(2.3)
Now assume that{f i;i= 1,2,· · ·, Nf }and{g i;i= 1,2,· · ·, Ng}are obser-
vations from independent random variablesXandY, respectively, with distri-
bution functionsFandG. The integralsF A(D) j andG A(D) j ofFandGare given
by (2.1),j= 1,2,3. For a given set of grid points{x k, k= 1,· · ·, K}, Davidson
and Duclos (2000) propose to testH A 1 ,H A 1l andH A 1r using the followingj-th
ASD test statistic,T A j (x), and Wong (2007) propose to testH D 1 ,H D 1l andH D 1r
using the followingj-th DSD test statistic,T D j (x):
T A j (x) = ˆF A j (x)− ˆGA j (x)q ˆV A j (x) (2.4)
T D j (x) = ˆF D j (x)− ˆGD j (x)q ˆV D j (x) (2.5)
Here,
ˆV A j (x) = ˆV A Fj (x) + ˆV A Gj (x)
ˆH A j (x) = 1 Nh(j−1)! PNh i=1(x−h i)j−1 +
ˆV A Hj (x) = 1 Nh
h
1
Nh((j−1)!)2
PNh
i=1(x−h i)2(j−1) + − ˆH A j (x)2
i
, H=F, G;h=f, g;
(2.6)
ˆV D j (x) = ˆV D Fj (x) + ˆV D Gj (x)
ˆH D j (x) = 1 Nh(j−1)! PNh i=1(hi −x) j−1 +
ˆV D Hj (x) = 1 Nh
h
1
Nh((j−1)!)2
PNh
i=1(hi −x) 2(j−1) + − ˆH D j (x)2
i
, H=F, G;h=f, g;
(2.7)
Under the null hypothesis, Bai et al. (2015) using the limiting distribution
of stochastic processes derives some theorems.
Theorem 2.1(Bai et al., 2015, Theorem 3.1) Let{f i}(i= 1,2,· · ·, Nf )and
{gi}(i= 1,2,· · ·, Ng)be random observations drawn from the independent ran-
dom variablesXandY, with CDFs,FandG, respectively. Under the null
hypothesisF≡G, thej-order ASD[DSD] test statistics,T A j (x)[T D j (x)](j= 1,
5

2, and3), weakly tends to a limiting Gaussian process with mean 0, variance 1,
and correlation functionr A(x, y)[rD(x, y)]in which for the casej= 1, we get
rA 1 (x, y) = F(x∧y)−F(x)F(y)p F(x)F(y)(1−F(x))(1−F(y))
rD 1 (x, y) = F(x∧y)−F(x)F(y)p F(x)F(y)(1−F(x))(1−F(y))
and for the casej >1, we have
rA(x, y) =
R x
a
R y
a (x−t) j−2(y−s) j−2(F(t∧s)−F(t)F(s))dtdsq
V A j (x)V A j (y)
rD(x, y) =
R b
x
R b
y (t−x) j−2(s−y) j−2(F(t∧s)−F(t)F(s))dtds q
V D j (x)V D j (y)
where ˆH A j (x)and ˆV A j (x)are defined in (2.6) and ˆH D j (x)and ˆV D j (x)are defined
in (2.7) forH=FandG,V A 1 (x) =F(x)(1−F(x)),V A j (x) = R x a R x a (x−
t)j−2(x−s) j−2(F(t∧s)−F(t)F(s))dtds,V D 1 (x) =F(x)(1−F(x)), andV D j (x) =R b
x
R b
x (t−x) j−2(s−x) j−2(F(t∧s)−F(t)F(s))dtds.
Based on this theorem, rejection regions for the aforementioned hypothesis
tests were proposed as follows.
We reject the null hypothesisH A 0 if:
max
a<x<b
|T A j (x)|>M A ∞,α/2,if the alternative hypothesis isH A 1 ;
min
a<x<b
T A j (x)<−M A ∞,α,if the alternative hypothesis isH A 1l;
max
a<x<b
T A j (x)>M A ∞,α,if the alternative hypothesis isH A 1r;
(2.8)
We reject the null hypothesisH D 0 if:
max
a<x<b
|T D j (x)|>M D ∞,α/2,if the alternative hypothesis isH D 1 ;
max
a<x<b
T D j (x)>M D ∞,α,if the alternative hypothesis isH D 1l ;
min
a<x<b
T D j (x)<−M D ∞,α,if the alternative hypothesis isH D 1r;
(2.9)
Here the critical valueM A ∞,α andM D ∞,α are given by the Bootstrap method, the
exact procedure will be described in detail later.
6

2.3 Bootstrap Methods and Critical Values
Assuming the returns of stocks are independent, and{f i;i= 1,2,· · ·, Nf }
and{g i;i= 1,2,· · ·, Ng}are independently and identically distributed sample
sequences, respectively. We put the two sample sets into one set{f (i), g(j), i=
1,2,· · ·, Nf , j= 1,2,· · ·, Ng}and perform sampling with replacement to obtain
two resampled sample sets{f ∗ i , i= 1,2,· · ·, Nf }and{g ∗ i , i= 1,2,· · ·, Ng}. In
this way, Bootstrap calculation can be performed for different SD test statistics
( ˆT A j , ˆT D j ,j= 1,2,3). By using this method, we can approximate the null dis-
tribution of the test statistic and obtainmax
a<x<b
|T A(D) j |, j= 1,2,3. The specific
details are as follows:
Step 1: Sample with replacement from the sample set{f (i), g(j), i=
1,2,· · ·, Nf , j= 1,2,· · ·, Ng}to obtain sample{f ∗ i , i= 1,2,· · ·, Nf }, and do
the same to get{g ∗ i , i= 1,2,· · ·, Ng}.
Step 2: Calculate
Aj = max A<x<B

 ˆT ∗A j (x)

 = max A<x<B

 ˆF ∗A j (x)− ˆG∗A j (x)q ˆV ∗A j (x)

 (2.10)
Dj = max A<x<B

 ˆT ∗D j (x)

 = max A<x<B

 ˆF ∗D j (x)− ˆG∗D j (x)q ˆV ∗D j (x)

 (2.11)
Repeat the above stepsNtimes to obtainNsets ofA j andD j, denoted as:
{Ajk , Djk , k= 1,2,· · ·, N}
Step 3: FindA j(α) such that #{|Ajk | ≥Aj(α), k≤N}= [N α], thenA j(α)
is theαpercentile of the corresponding distribution of ˆT ∗A j (x).
Step 4: FindD j(α) such that #{|Djk | ≥Dj(α), k≤N}= [N α], thenD j(α)
is theαpercentile of the corresponding distribution of ˆT ∗D j (x).
The preceding method makes a decision by comparing the test statistic with
the critical value determined at a given significance level. While this decision
rule provides a clear boundary, it only yields a binary conclusion of ”reject”
or ”do not reject.” Consequently, it fails to precisely characterize the degree of
risk associated with the decision (i.e., the strength of the evidence). Therefore,
to provide a more intuitive and precise reflection of statistical significance, this
paper adopts thep-value as the ultimate criterion for decision-making.
Specifically, letT A j,0 andT D j,0 denote the maximum observed values of the test
statistics calculated from the original sample (i.e.,T A j,0 = max A<x<B | ˆT A j (x)|,
T D j,0 = max A<x<B | ˆT D j (x)|). Furthermore, let{A jk , k= 1,2,· · ·, N}and
{Djk , k= 1,2,· · ·, N}represent theNresampled test statistics obtained via
the aforementioned Bootstrap procedure. The empiricalp-value can then be
calculated as follows:
7

pA j = #{Ajk ≥T A j,0, k= 1,2,· · ·, N} N (2.12)
pD j = #{Djk ≥T D j,0, k= 1,2,· · ·, N} N (2.13)
If the null hypothesis holds (i.e., there is no stochastic dominance relation-
ship between the two assets), thisp-value is typically large. Conversely, if the
calculatedp-value is sufficiently small, we are inclined to reject the null hypoth-
esis, thereby concluding the existence of a stochastic dominance relationship
between the two assets. Furthermore, the magnitude of thep-value can, to
some extent, be viewed as a ”distance” metric quantifying the deviation of the
empirical distribution from the null hypothesis. A detailed discussion from this
perspective will be elaborated in the subsequent chapter.
3 Clustering Algorithms Based on SD Test
Statistics
In clustering algorithms, distance serves as a metric for the degree of dis-
similarity between samples. To construct stock clustering models tailored to
investors with different preferences, this paper calculates a Stochastic Domi-
nance Coefficient Matrix using various stochastic dominance (SD) test statis-
tics to measure the distance (or degree of dissimilarity) between stock clusters.
Consequently, we propose the ASD-K-means, DSD-K-means, ASD-Hierarchical,
and DSD-Hierarchical clustering algorithms. Based on the different orders of
the Stochastic Dominance Coefficient Matrix, these can be further categorized
into 12 specific algorithms: F ASD-K-means, SASD-K-means, TASD-K-means,
F ASD-Hierarchical, SASD-Hierarchical, TASD-Hierarchical, FDSD-K-means,
SDSD-K-means, TDSD-K-means, FDSD-Hierarchical, SDSD-Hierarchical, and
TDSD-Hierarchical. Furthermore, the Bootstrap method is employed to esti-
mate the empiricalp-values required for the calculation of the Stochastic Dom-
inance Coefficient Matrix.
3.1 Stochastic Dominance Coefficient
In the previous section, we introduced the test statistics ˆT A j (x) and ˆT D j (x)
(j= 1,2,3) for risk-averse (ASD) and risk-seeking (DSD) investors, respectively.
Under the null hypothesisF≡G, thej-th order test statistics converge weakly
to a limit Gaussian process. Using the Bootstrap method, we simulate the
empirical distribution under the null hypothesis and calculate the empiricalp-
value as the ultimate criterion for decision-making. As is well known, if the null
hypothesis holds (i.e., there is no stochastic dominance relationship between
the two assets), thisp-value is typically large. Conversely, if the calculatedp-
value is sufficiently small, we are inclined to reject the null hypothesis, thereby
8

concluding the existence of a stochastic dominance relationship between the two
assets.
In traditional clustering analysis, algorithms inherently rely on the construc-
tion of a reasonable distance or similarity matrix. To seamlessly integrate
the results of the stochastic dominance tests into a clustering framework, we
transform the aforementionedp-values to construct the ”Stochastic Dominance
Coefficient.” This coefficient is designed to satisfy the fundamental conditions
of a distance metric: a larger coefficient indicates a more significant stochas-
tic dominance relationship betweenXandY(implying greater distinctness in
their distributions). Conversely, a smaller coefficient suggests an insignificant
stochastic dominance relationship (implying higher distributional similarity),
meaningXandYcan be grouped into the same cluster. Specifically, we de-
fine the Stochastic Dominance Coefficient as the complement of the empirical
p-value (i.e., 1−p).
In this paper, we propose novel clustering algorithms by employing the first-
, second-, and third-order Stochastic Dominance Coefficients as distance mea-
sures between stocks. The specific calculation formulas for these coefficients are
presented as follows:
P(X, Y)A j = 1−
PN
k=1 I(A jk ≥T A j,0)
N , j= 1,2,3 (3.1)
P(X, Y)D j = 1−
PN
k=1 I(D jk ≥T D j,0)
N , j= 1,2,3 (3.2)
whereP(X, Y) A j denotes the Stochastic Dominance Coefficient corresponding
to the risk-averse population;XandYrepresent any arbitrary pair of stocks
from the sample;P(X, Y) D j denotes the Stochastic Dominance Coefficient corre-
sponding to the risk-seeking population; andj= 1,2,3 correspond to the first-,
second-, and third-order stochastic dominance coefficients, respectively.I(·) is
the indicator function. Consistent with previous sections,T A j,0 andT D j,0 repre-
sent the maximum observed values of the test statistics for the risk-averse and
risk-seeking populations, respectively, computed based on the original sample
of log-returns for stockXand stockY. For the detailed calculation procedures
ofA jk andD jk , please refer to Section 2.3.
3.2 Selection of the Number of ClustersK
In clustering algorithms, the selection of the number of clusters (K) is of
paramount importance, as it directly impacts the quality of the model and
the accuracy of the clustering results. The Silhouette Coefficient measures both
intra-cluster compactness and inter-cluster separation; therefore, it is commonly
employed to determine the optimal value ofK. In this paper, by integrating the
traditional Silhouette Coefficient with the specific characteristics of our proposed
model, we construct a novel metric named the SD-SC Coefficient to determine
the optimal number of clusters.
9

The SD-SC Coefficient serves as a metric to evaluate the performance of the
proposed stochastic dominance clustering method. It incorporates two com-
ponents: cohesion and separation. Cohesion reflects the degree of compactness
between a specific sample point and other sample points within the same cluster.
For a given sample pointi, cohesion is defined as the average stochastic dom-
inance distance between that sample and all other samples within its assigned
cluster. A smaller cohesion value indicates higher similarity among samples
within the cluster and greater internal consistency, thereby implying superior
clustering performance.
Separation reflects the relationship between a sample point and elements
outside its cluster. For a given sample pointi, separation is defined as the av-
erage stochastic dominance distance between that sample and all sample points
in the nearest neighboring cluster. A larger separation value implies significant
differences between samples in distinct clusters and high discriminative power
of the clustering results, indicating superior clustering performance.
When applied to the stochastic dominance clustering model, the SD-SC Co-
efficient can scientifically assess the algorithm’s effectiveness and determine the
optimal number of clusters. In this study, the optimal number of clusters is
jointly determined by the designated stochastic dominance clustering model and
the corresponding SD-SC Coefficient. The specific procedures are as follows:
Step 1: Define the search range for the number of clusters, denoted asK∈
[Kmin, Kmax].
Step 2: Select a specific stochastic dominance clustering algorithm (e.g.,
ASD-K-means or DSD-Hierarchical) tailored to the target investor’s risk pref-
erence.
Step 3: For each candidate valueKwithin the defined search range, execute
the selected clustering algorithm to obtain the corresponding clustering result.
Step 4: Calculate the overall SD-SC Coefficient for each clustering result
obtained in Step 3. The value ofKthat yields the maximum SD-SC Coefficient
is identified as the optimal number of clusters.
The specific calculation procedures for the SD-SC Coefficient are detailed in
Section 3.5.
3.3 ASD(DSD)-K-means Clustering Algorithm
First, we define the distance metric to measure the dissimilarity between
stocks tailored to specific investor risk preferences: the Stochastic Dominance
Coefficient. For any two arbitrary stocksXandY, the calculation methods for
the stochastic dominance coefficients for risk-averse and risk-seeking investors
are precisely defined in Equations (3.1) and (3.2), respectively. Consistent with
the definitions in Section 3.1, a smaller coefficient indicates a higher degree of
distributional similarity between the two assets.
Subsequently, utilizing the Stochastic Dominance Coefficient Matrix as the
distance metric, stocks with higher similarity can be grouped into the same
cluster via the modified K-means algorithm, denoted as the ASD-K-means
or DSD-K-means algorithm. Specifically, substituting the first-order (j= 1),
10

second-order (j= 2), and third-order (j= 3) stochastic dominance coefficients
yields the F ASD(FDSD)-K-means, SASD(SDSD)-K-means, and TASD(TDSD)-
K-means clustering algorithms, respectively.
In the standard K-means algorithm, the number of clustersKmust be des-
ignated in advance (as discussed in Section 3.2). A critical distinction in our
proposed ASD(DSD)-K-means algorithm lies in the update mechanism of the
cluster centers. During each iteration, the new cluster center is updated by
calculating the cross-sectional average of the return series for all stocks cur-
rently assigned to that cluster, essentially forming an equally-weighted portfolio
of the constituents. The specific execution process of the ASD(DSD)-K-means
clustering algorithm is presented in Algorithm 1:
Algorithm 1ASD(DSD)-K-means Clustering Algorithm
Input:
The return dataset ofnstocks, denoted asR;
The designated number of clusters,K;
The maximum number of iterations,max iter= 100;
Initialization:
Randomly selectKstocks from the sample as the initial cluster centers{C t :
t= 1,2,· · ·, K};
Set iteration counterite= 0;
1:repeat
2:foreach stocki= 1,2,· · ·, ndo
3:foreach cluster centert= 1,2,· · ·, Kdo
4:Calculate the stochastic dominance distanced i,t between stockR i
and cluster centerC t using Equation (3.1) for ASD or Equation (3.2)
for DSD.
5:end for
6:Assign stockito the nearest cluster:cluster idxi ←arg min t{di,t :t=
1,2, . . . , K}
7:end for
8:foreach clustert= 1,2,· · ·, Kdo
9:Update the cluster centerC t by calculating the mean return of all stocks
currently assigned to clustert:
Ct = mean(Rcluster idx==t)
10:end for
11:ite←ite+ 1
12:untilno stocks change their cluster assignments ORite==max iter
Output:The final cluster assignments for allnstocks.
11

3.4 ASD(DSD)-Hierarchical Clustering Algorithm
Based on the order of hierarchical decomposition, hierarchical clustering
algorithms can generally be categorized into Agglomerative (bottom-up) and
Divisive (top-down) approaches. In this paper, we explicitly adopt the Agglom-
erative Hierarchical Clustering approach to construct our model. This algorithm
proceeds in a bottom-up manner, initializing by treating each individual stock
as an independent, single-element cluster. At each iterative step, it merges the
two closest clusters together until all stocks are eventually agglomerated into
one overarching cluster.
During the merging process, determining the exact ”distance” between two
clusters is crucial. While standard clustering algorithms frequently rely on
Euclidean or Mahalanobis distances, our proposed SD-Hierarchical clustering
model innovatively adopts the Stochastic Dominance Coefficient Matrix as the
fundamental distance metric. Furthermore, among the common inter-cluster
similarity measurement strategies—namely Single Linkage (minimum distance),
Complete Linkage (maximum distance), and Average Linkage—we select the
Average Linkage method. This method comprehensively incorporates the struc-
tural information of all samples within the clusters, effectively mitigating the
outlier sensitivity commonly associated with Single or Complete Linkage.
Specifically, the Average Linkage method defines the distance between clus-
terC 1 and clusterC 2 as the arithmetic mean of the stochastic dominance dis-
tances between all possible pairs of stocks across the two clusters. The inter-
cluster distances tailored to risk-averse and risk-seeking investors are mathe-
matically defined as follows:
dist(C1, C2)A j = 1 |C1| · |C2| X x∈C1 X y∈C2 P(x, y)A j (3.3)
dist(C1, C2)D j = 1 |C1| · |C2| X x∈C1 X y∈C2 P(x, y)D j (3.4)
where|C 1|and|C 2|represent the total number of stocks contained in clustersC 1
andC 2, respectively;xandyrepresent arbitrary individual stocks belonging to
C1 andC 2; andP(x, y) A j andP(x, y)D j are the pairwise Stochastic Dominance
Coefficients calculated previously.
By integrating the Agglomerative hierarchical framework with the SD Co-
efficient Matrix, we finalize the Stochastic Dominance Hierarchical clustering
model. Specifically, substitutingj= 1,2,and 3 into the distance metrics denotes
the F ASD(FDSD)-, SASD(SDSD)-, and TASD(TDSD)-Hierarchical clustering
algorithms, respectively. The specific step-by-step execution of the ASD(DSD)-
Hierarchical clustering algorithm is presented in Algorithm 2:
12

Algorithm 2ASD(DSD)-Hierarchical Clustering Algorithm
Input:
The return dataset ofnstocks, denoted asR={R 1, R2,· · ·, Rn};
The designated number of clusters,K;
The specific order of stochastic dominance,j∈ {1,2,3}.
Initialization:
Assign each stock to its own individual cluster:C i ={R i}fori= 1,2,· · ·, n;
Define the initial active cluster set:C={C 1, C2,· · ·, Cn};
Calculate the initialn×npairwise distance matrixM, whereM u,v =
P(R u, Rv)A j (orP(R u, Rv)D j ) using Equation (3.1) or (3.2) for all stocksu, v∈
{1,2,· · ·, n}.
1:whilethe total number of clusters|C|> Kdo
2:Find the pair of clustersC a andC b inCthat have the minimum inter-
cluster distance dist(C a, Cb)A j (or dist(C a, Cb)D j ) based on the Average
Linkage method calculated via Equation (3.3) or (3.4).
3:Merge the two closest clusters into a new single cluster:C new =C a ∪C b.
4:Update the active cluster set: removeC a andC b, and insertC new (C ←
C \ {Ca, Cb} ∪ {Cnew}).
5:Update the distance matrixMby calculating the new average linkage
distances betweenC new and all other remaining clusters inC.
6:end while
Output:The finalKclusters and the names of the stocks contained within
each class.
3.5 SD-SC Coefficient
The Silhouette Coefficient (SC) is a classic clustering validity index used to
measure the compactness and separation of clustering results. Traditional SC
calculations rely on Euclidean or Manhattan distances; however, these metrics
fail to account for investors’ risk preferences and thus cannot adequately reflect
the clustering performance of the model proposed in this paper. To address
this limitation, this subsection proposes a novel evaluation metric based on the
stochastic dominance distance, termed the SD-SC Coefficient, to better assess
the clustering quality.
The SD-SC Coefficient is an enhanced clustering validity index derived from
the traditional Silhouette Coefficient by substituting the standard distance met-
ric with the stochastic dominance distance. The calculation steps are as follows:
Step 1: Calculate the pairwise stochastic dominance distances between all
stocks. For any two arbitrary stocksiandv, their distances corresponding
to risk-averse and risk-seeking investors are denoted asP(i, v) A j andP(i, v) D j ,
respectively.
Step 2: Calculate the intra-cluster distancea(i) j: For a given sample point
iassigned to clusterC i, calculate the average stochastic dominance distance
betweeniand all other points within the same clusterC i.
13

a(i)A j = 1 |Ci| −1 X v∈Ci,v̸=i P(i, v)A j (3.5)
a(i)D j = 1 |Ci| −1 X v∈Ci,v̸=i P(i, v)D j (3.6)
where|C i|denotes the total number of samples in clusterC i;a(i) A j and
a(i)D j represent the intra-cluster distances corresponding to risk-averse and risk-
seeking investors under thej-th order SD, respectively.
Step 3: Calculate the inter-cluster distanceb(i) j: For sample pointi, calcu-
late the average stochastic dominance distance to all points in any other cluster
Ck (whereC k ̸=C i), and select the minimum average distance among all such
clusters:
b(i)A j = min Ck̸=Ci
(
1
|Ck|
X
v∈Ck
P(i, v)A j
)
(3.7)
b(i)D j = min Ck̸=Ci
(
1
|Ck|
X
v∈Ck
P(i, v)D j
)
(3.8)
where|C k|denotes the number of samples in clusterC k;b(i) A j andb(i) D j rep-
resent the inter-cluster distances corresponding to risk-averse and risk-seeking
investors, respectively.
Step 4: Calculate the SD-SC value for individual sample points and the
overall clustering result:
s(i)A(D) j = b(i)A(D) j −a(i) A(D) j
max{a(i)A(D) j , b(i)A(D) j } (3.9)
SD-SC A(D) j = 1 n
nX
i=1
s(i)A(D) j (3.10)
wherenis the total number of stock samples;SD-SC A j represents the overall
SD-SC coefficient value for risk-averse investors, andSD-SC D j represents the
overall SD-SC coefficient value for risk-seeking investors.
3.6 SD-DBI Index
The Davies-Bouldin Index (DBI) is a classic internal clustering validity index
used to measure the compactness and separation of clustering results. Tradi-
tional DBI calculations rely on Euclidean or Manhattan distances; however,
these metrics cannot adequately reflect the performance of the stochastic dom-
inance clustering model proposed in this paper. To address this limitation,
this subsection proposes an improved clustering validity index based on the
14

stochastic dominance distance, termed the SD-DBI Index, to better evaluate
the clustering quality.
The SD-DBI Index is derived from the traditional DBI by substituting the
standard distance metric with the stochastic dominance distance. The specific
calculation steps are as follows:
Step 1: Define the distance metrics. LetP(v, µ i)A j andP(v, µ i)D j denote
thej-th order stochastic dominance distances between a specific stockvand its
cluster centerµ i. Consistent with Section 3.3,µ i represents the mean return
series of all stocks within clusteri.
Step 2: Calculate the intra-cluster compactnessS i,j:
SA i,j = 1 |Ci| X v∈Ci P(v, µi)A j (3.11)
SD i,j = 1 |Ci| X v∈Ci P(v, µi)D j (3.12)
whereµ i is the center of clusterC i, and|C i|is the total number of samples in
clusterC i.S A i,j andS D i,j represent the intra-cluster compactness corresponding
to risk-averse and risk-seeking investors under thej-th order SD, respectively.
Step 3: Calculate the inter-cluster separationM i,k,j :
M A i,k,j =P(µ i, µk)A j (3.13)
M D i,k,j =P(µ i, µk)D j (3.14)
whereµ i andµ k are the centers of clusterC i and clusterC k, respectively.M A i,k,j
andM D i,k,j represent the inter-cluster separation between the two cluster centers.
Step 4: Calculate the inter-cluster similarityR i,k,j between clusterC i and
clusterC k:
RA(D) i,k,j = SA(D) i,j +S A(D) k,j
M A(D) i,k,j (3.15)
whereR A i,k,j andR D i,k,j represent the pairwise inter-cluster similarity for risk-
averse and risk-seeking investors, respectively.
Step 5: Calculate the maximum similarityR i,j for clusterC i:
RA(D) i,j = max k̸=i RA(D) i,k,j (3.16)
whereR A i,j andR D i,j represent the maximum similarity values between cluster
Ci and its most similar neighboring cluster.
Step 6: Calculate the overall SD-DBI Index:
SD-DBI A(D) j = 1 K
KX
i=1
RA(D) i,j (3.17)
15

whereKis the designated total number of clusters.SD-DBI A j andSD-DBI D j
represent the overall SD-DBI coefficient values for risk-averse and risk-seeking
investor scenarios, respectively. A smaller SD-DBI value indicates better clus-
tering performance (i.e., high intra-cluster compactness and high inter-cluster
separation).
4 Empirical Research
In this chapter, the empirical dataset comprises the weekly closing price
data of the constituent stocks from two major market indices: the NASDAQ
100 Index (spanning from March 23, 2014, to March 24, 2024) and the CSI 100
Index (spanning from March 24, 2013, to March 24, 2024). Although the the-
oretical framework established in Chapter 3 encompasses up to the third-order
stochastic dominance, this empirical section focuses exclusively on the first-
and second-order SD clustering. In financial economics, the first two orders are
generally sufficient to capture the fundamental investor preferences regarding
non-satiation and risk aversion (or risk-seeking). Higher-order dominance rela-
tions often exhibit marginal empirical significance in broad market clustering
and can overly complicate the interpretation of the results. Therefore, utiliz-
ing the first- and second-order stochastic dominance test statistics, we conduct
stochastic dominance clustering analyses specifically tailored to risk-averse and
risk-seeking investors.
4.1 Data Sources and Processing
4.1.1 Data Sources
The NASDAQ 100 Index selects 100 of the largest domestic and international
non-financial companies listed on the NASDAQ Stock Market based on market
capitalization. Dominated primarily by high-tech and growth-oriented equities,
it serves as a critical benchmark reflecting the overall trajectory of the US
technology sector.
Conversely, the CSI 100 Index comprises 100 large-capitalization and highly
liquid stocks selected from the Shanghai and Shenzhen stock exchanges. It
covers a diverse range of sectors, including finance, energy, consumer goods,
and healthcare, effectively diversifying unsystematic risk while maintaining low
liquidity risk. It is widely regarded as a representative barometer for the overall
performance of blue-chip companies in China’s A-share market.
The historical trading data utilized in this study were retrieved from the
Choice Financial Terminal (East Money Information Co., Ltd.), a comprehen-
sive and professional financial database widely used in Chinese financial re-
search.
16

4.1.2 Data Processing
To ensure the integrity of a balanced panel dataset, this study systematically
excludes assets with incomplete trading records, specifically those unlisted at
the onset of the sample period and those subject to prolonged suspensions.
Following this rigorous filtering process, the finalized dataset curated for the
subsequent clustering analysis retains 83 constituent stocks from the NASDAQ
100 and 76 from the CSI 100.
This study utilizes logarithmic returns rather than simple discrete returns
for modeling. Logarithmic returns possess several highly desirable statistical
properties: notably, they satisfy time-additivity, which facilitates the calculation
of multi-period returns, and they help mitigate the inherent positive skewness
of asset prices. Therefore, logarithmic returns are highly suitable for long-term
portfolio performance evaluation and robust stochastic modeling.
Furthermore, to construct the return series, we aggregate daily closing prices
into weekly intervals. Using weekly data effectively alleviates market microstruc-
ture noise (such as bid-ask bounce and asynchronous trading effects) prevalent
in daily, high-frequency data. Simultaneously, it preserves sufficient observa-
tions to accurately capture the medium-to-long-term distributional characteris-
tics and trends of the constituent stocks.
4.2 SD-K-means Clustering Analysis
Based on the theoretical framework established in Section 3.3, this section
conducts K-means clustering analysis on the constituent stocks of the CSI 100
and the NASDAQ 100 indices. Depending on the investors’ specific risk pref-
erences and the applied order of stochastic dominance (j), the clustering algo-
rithms are systematically categorized as follows:
For risk-averse investors, the model adopts the ASD-K-means algorithm.
Specifically, when utilizing the first-order (j= 1), second-order (j= 2), and
third-order (j= 3) stochastic dominance test statistics, the algorithms are
denoted as F ASD-K-means, SASD-K-means, and TASD-K-means, respectively.
Conversely, for risk-seeking investors, the model applies the DSD-K-means
algorithm. Accordingly, corresponding toj= 1,2,and 3, the algorithms are
defined as FDSD-K-means, SDSD-K-means, and TDSD-K-means, respectively.
While the full algorithmic suite incorporates up to the third order, the fol-
lowing empirical evaluations and results will primarily focus on the first- and
second-order clustering scenarios, as they sufficiently capture the fundamental
market behaviors of non-satiation and risk attitude.
4.2.1 ASD-K-means Clustering
This section first applies the first-order ASD-K-means clustering algorithm
tailored for risk-averse investors. Building upon the first-order clustering results,
we subsequently perform second-order ASD-K-means clustering to further refine
the asset groupings. The empirical analysis utilizes the constituent stocks of
both the NASDAQ 100 and the CSI 100 indices.
17

Based on the SD-SC evaluation criteria discussed previously, the optimal
number of clusters for the NASDAQ 100 stocks is determined to be 3, denoted
asK= 3. Figure 4.1 illustrates the heatmap of the stochastic dominance co-
efficient matrix generated from the first-order clustering. In this heatmap, the
horizontal and vertical axes represent individual stocks, and each tiny square
indicates the stochastic dominance distance between a given pair of stocks. A
larger coefficient corresponds to a darker shade. The visual clustering pattern
demonstrates excellent algorithmic performance. For instance, the first-order
stochastic dominance coefficients among stocks within the third cluster are rel-
atively low, creating a distinctively lighter square region along the diagonal.
Conversely, the coefficients between these intra-cluster stocks and those outside
the cluster are notably larger, as evidenced by the surrounding darker regions.
Figure 4.1: F ASD-Kmeans Stochastic Dominance Coefficient Heatmap (NAS-
DAQ)
Table 4.1 displays the constituency of each cluster following the first-order
ASD-K-means clustering of the NASDAQ stocks. Subsequently, the calculated
center of each cluster is selected as its representative to compare the first-order
stochastic dominance relationships among the three clusters.
Observations from Table 4.2 indicate that the first cluster center strictly
dominates the second in the first order, denoted asC 1 ≻1 C2. However, no
definitive first-order stochastic dominance relationship can be established be-
tweenC 1 andC 3, or betweenC 2 andC 3. To resolve this ambiguity, a gran-
ular comparison is conducted between the individual constituent stocks of the
third cluster and the centersC 1 andC 2. A comprehensive analysis reveals
that five specific stocks within the third cluster—Costco Wholesale, Keurig Dr
Pepper, Mondelez International, Paychex, and Xcel Energy—first-order stochas-
18

Table 4.1: F ASD-K-means Clustering Results (NASDAQ)
Cluster Stock Names Count
1 Apple, Adobe, Analog Devices, Automatic Data Processing
(ADP), Autodesk, Applied Materials, AMD, Amgen, Amazon,
ANSYS, ASML, Broadcom, AstraZeneca (US ADR), Biogen,
Booking Holdings, Baker Hughes, Cadence Design Systems, CDW
Corp, Charter Communications, Copart, CoStar Group, Cintas,
Cognizant, Dollar Tree, DexCom, Electronic Arts, Diamondback
Energy, Fastenal, Fortinet, Gilead Sciences, Alphabet C (GOOG),
Alphabet A (GOOGL), IDEXX Laboratories, Illumina, Intel, In-
tuit, Intuitive Surgical, KLA Corp, Lam Research, Lululemon
Athletica, Marriott International, Microchip Technology, Mer-
cadoLibre, Meta Platforms, Monster Beverage, Marvell Tech-
nology, Microsoft, Micron Technology, Netflix, NVIDIA, NXP
Semiconductors, Old Dominion Freight Line, ON Semiconductor,
O’Reilly Automotive, Palo Alto Networks, PACCAR, Qualcomm,
Regeneron Pharmaceuticals, Ross Stores, Sirius XM, Synopsys, T-
Mobile US, Tesla, Take-Two Interactive, Texas Instruments, Ver-
tex Pharmaceuticals, Walgreens Boots Alliance, Workday
68
2 PepsiCo 1
3 American Electric Power, Coca-Cola Europacific Partners, Com-
cast, Costco Wholesale, Cisco Systems, Exelon, Honeywell In-
ternational, Keurig Dr Pepper, Mondelez International, Paychex,
Roper Technologies, Starbucks, Verisk Analytics, Xcel Energy
14
Table 4.2: F ASD-Kmeans Stochastic Dominance Relationships Among Cluster
Centers (NASDAQ)
Cluster 1 (C 1) Cluster 2 (C 2) Cluster 3 (C 3)
Cluster 1-≻ 1 ≻1
Cluster 2- -≻ 1
Cluster 3≻ 1 ≻1 -
Note:≻ 1 indicates dominance,≺ 1 indicates being dominated, and≻ 1≺1 indicates
no clear dominance relationship.
19

tically dominateC 2. Among these, Costco Wholesale, Paychex, and Xcel En-
ergy exhibit no clear first-order dominance relationship withC 1, whereas all
other remaining stocks in the third cluster are strictly dominated byC 1 at
the first-order level. Consequently, this study extracts these three specific non-
dominated stocks—Costco Wholesale, Paychex, and Xcel Energy—and merges
them with the constituents of the first cluster to perform a subsequent second-
order stochastic dominance clustering. This targeted refinement aims to further
isolate the asset pools and determine the optimal stock groupings tailored to
distinct investor types.
It is found that there is no significant first-order stochastic dominance re-
lationship among the 76 stocks of CSI 100 index, indicating that there is no
superiority or inferiority of these stocks under the first-order stochastic domi-
nance condition, which needs to be further analysed by higher-order stochastic
dominance Kmeans clustering.
For risk-averse investors, the SASD-K-means clustering algorithm is applied
to the refined pools comprising 71 NASDAQ constituent stocks and 76 CSI 100
constituent stocks. By maximizing the SD-SC evaluation metric, the optimal
number of clusters is determined to be three for the NASDAQ subset and two
for the CSI 100 subset. The corresponding second-order stochastic dominance
coefficient heatmaps are presented in Figure 4.2. Bypassing basic coordinate
definitions, the visual evidence in the left panel clearly partitions the NASDAQ
stocks into three distinct classes based on the magnitude of their stochastic
dominance coefficients. Concurrently, the right panel depicts the CSI 100 con-
stituents, revealing that the stocks within the second cluster, located in the
bottom-right corner, exhibit remarkably large stochastic dominance coefficients
when compared against other stocks. This strong visual contrast indicates a
highly pronounced second-order stochastic dominance relationship.
(a)
 (b)
Figure 4.2: SASD-Kmeans Stochastic Dominance Coefficient Heatmap
A comparison of the stochastic dominance relationships among the centers of
the three NASDAQ clusters reveals no definitive second-order stochastic dom-
inance between the second and third clusters. However, both of these clusters
20

dominate the first cluster in the second order, expressed mathematically as
C2 ≡C 3,C 2 ≻2 C1, andC 3 ≻2 C1. Consequently, this study merges the
second and third clusters into a single unified class, with the consolidated clus-
tering results presented in Table 4.3. Furthermore, Table 4.4 details the specific
constituency of each stock class following the CSI 100 clustering.
By calculating the cross-sectional mean of all samples within the second
cluster of Table 4.3 to serve as the updated cluster center, a subsequent com-
parison reveals that the second cluster strictly dominates the first in the second
order, denoted asC 2 ≻2 C1. Consequently, this study ultimately selects the 13
constituent stocks from the second NASDAQ cluster for investment and final
portfolio construction. Following a parallel evaluation of the two cluster centers
detailed in Table 4.4, the results identically demonstrate that the second cluster
strictly dominates the first, expressed mathematically asC 2 ≻2 C1. Therefore,
for risk-averse investors, allocating capital to the two specific constituent stocks
of this optimal CSI 100 cluster—China Yangtze Power and the Industrial and
Commercial Bank of China—yields a substantially higher expected utility.
Table 4.3: SASD-K-means Clustering Results (NASDAQ)
Cluster Stock Names Count
1 Apple, Adobe, Analog Devices, Autodesk, Applied Materi-
als, AMD, Amazon, ANSYS, ASML, Broadcom, AstraZeneca
(US ADR), Biogen, Booking Holdings, Baker Hughes, Char-
ter Communications, Copart, CoStar Group, Cognizant, Dollar
Tree, DexCom, Electronic Arts, Diamondback Energy, Fastenal,
Fortinet, Gilead Sciences, Alphabet C (GOOG), Alphabet A
(GOOGL), IDEXX Laboratories, Illumina, Intel, Intuit, Intu-
itive Surgical, KLA Corp, Lam Research, Lululemon Athletica,
Marriott International, Microchip Technology, MercadoLibre,
Meta Platforms, Monster Beverage, Marvell Technology, Mi-
cron Technology, Netflix, NVIDIA, NXP Semiconductors, Old
Dominion Freight Line, ON Semiconductor, Palo Alto Networks,
PACCAR, Qualcomm, Regeneron Pharmaceuticals, Ross Stores,
Sirius XM, Tesla, Take-Two Interactive, Vertex Pharmaceuti-
cals, Walgreens Boots Alliance, Workday
58
2 Costco Wholesale, Xcel Energy, Automatic Data Processing
(ADP), Amgen, Cadence Design Systems, CDW Corp, Cintas,
Microsoft, O’Reilly Automotive, Paychex, Synopsys, T-Mobile
US, Texas Instruments
13
4.2.2 DSD-K-means Clustering
Subsequently, stock K-means clustering is performed for risk-seeking in-
vestors, first performing first-order K-means clustering (FDSD-K-means clus-
tering), and on the basis of the first-order clustering, continuing to perform
21

Table 4.4: SASD-K-means Clustering Results (CSI 100)
Cluster Stock Names Count
1 China Vanke, ZTE Corporation, TCL Technology, East-
ern Shenghong, Weichai Power, Gree Electric Appliances,
Changchun High-Tech, BOE Technology, Qinghai Salt Lake
Industry, Unisplendour, Focus Media, Unigroup Guoxin Mi-
croelectronics, TCL Zhonghuan Renewable Energy, iFLYTEK,
Goertek, Oriental Yuhong, SF Holding, NAURA Technol-
ogy, Glodon, Hikvision, Ganfeng Lithium, Tianqi Lithium,
Luxshare Precision, Rongsheng Petrochemical, 37 Interactive
Entertainment, BYD, LB Group, Satellite Chemical, EVE
Energy, Aier Eye Hospital, Zhifei Biological, Inovance Tech-
nology, Walvax Biotechnology, Sungrow Power Supply, Zhongji
Innolight, Tigermed, Baotou Steel, Baoshan Iron & Steel (Baos-
teel), Sinopec, CITIC Securities, SANY Heavy Industry, China
Merchants Bank, Poly Developments, China Unicom, TBEA,
China Northern Rare Earth, China Jushi, Hengrui Medicine,
Wanhua Chemical, Hengli Petrochemical, NARI Technology,
Hualu Hengsheng, Pien Tze Huang, Tongwei, Kweichow Moutai,
Shandong Gold, Hundsun Technologies, Conch Cement, Yonyou
Network, Haier Smart Home, Wingtech Technology, AECC Avi-
ation Power, LONGi Green Energy, China Shenhua Energy, Ping
An Insurance, China Railway Group, Aluminum Corporation of
China (Chalco), China State Construction Engineering (CSCEC),
CRRC, PetroChina, China Tourism Group Duty Free, Zijin Min-
ing, COSCO SHIPPING Holdings, CMOC Group
74
2 China Yangtze Power, Industrial and Commercial Bank of China
(ICBC)
2
22

second-order K-means clustering (SDSD-K-means clustering). Both theoretical
and experimental results indicate that the results of F ASD-K-means clustering
and FDSD-K-means clustering are the same. Therefore, for risk-seeking in-
vestors, this paper still performs SDSD-K-means clustering on the 71 NASDAQ
constituent stocks and 76 CSI 100 constituent stocks.
(a)
 (b)
Figure 4.3: SDSD-Kmeans Stochastic Dominance Coefficient Heatmap
The optimal number of clusters for NASDAQ is 4, and the optimal number
of clusters for CSI 100 stocks is 7. The left chart in Figure 4-3 is the stochastic
dominance coefficient heatmap for NASDAQ after clustering, and the right chart
is for the CSI 100 constituents. In the figure, the horizontal and vertical axes
represent each individual stock, and each small square represents the stochastic
dominance coefficient value between two stocks; the larger the value, the darker
the color of the square. It can be seen from the figure that the effect after
clustering the two datasets is very good, and the stocks are clustered into several
classes with obvious differences in stochastic dominance coefficients.
The specific stock clustering situation is shown in Table 4-5 and Table 4-6.
Comparing the second-order stochastic dominance relationships among the cen-
ters of each class of stocks in Table 4-5, it is found thatC 1 ≻2 C2,C 1 ≻2 C3,
C1 ≻2 C4. For risk-seeking investors, the 42 stocks in the first class can be
selected from the NASDAQ constituents for subsequent investment portfolios.
Comparing the second-order stochastic dominance relationships among the clus-
ter centers in Table 4-6, the results show that the center of Class 1 stochastically
dominates the centers of all other classes in the second order. Therefore, the 72
stocks in Class 1 of Table 4-6 are selected for the investment portfolio.
4.2.3 Model Performance Evaluation
The values of the classic K-means clustering results are compared with those
of the SD clustering models. To ensure comparability, the number of clusters
selected for the classic clustering models is kept consistent with that of the SD
models.
23

Table 4.5: SDSD-K-means Clustering Results (NASDAQ)
Cluster Stock Names Count
1 Adobe, Autodesk, Applied Materials, AMD, Amazon, ASML,
Broadcom, Biogen, Booking Holdings, Baker Hughes, Cadence
Design Systems, CoStar Group, Dollar Tree, DexCom, Di-
amondback Energy, Fortinet, IDEXX Laboratories, Illumina,
Intel, Intuitive Surgical, KLA Corp, Lam Research, Lulule-
mon Athletica, Marriott International, Microchip Technology,
MercadoLibre, Meta Platforms, Marvell Technology, Micron
Technology, Netflix, NVIDIA, NXP Semiconductors, Old Do-
minion Freight Line, ON Semiconductor, Palo Alto Networks,
Qualcomm, Regeneron Pharmaceuticals, Synopsys, Tesla, Take-
Two Interactive, Vertex Pharmaceuticals, Workday
42
2 Automatic Data Processing (ADP), Costco Wholesale, Paychex,
Walgreens Boots Alliance
4
3 Xcel Energy 1
4 Apple, Analog Devices, Amgen, ANSYS, AstraZeneca (US
ADR), CDW Corp, Charter Communications, Copart, Cintas,
Cognizant, Electronic Arts, Fastenal, Gilead Sciences, Alphabet
C (GOOG), Alphabet A (GOOGL), Intuit, Monster Beverage,
Microsoft, O’Reilly Automotive, PACCAR, Ross Stores, Sirius
XM, T-Mobile US, Texas Instruments
24
24

Table 4.6: SDSD-K-means Clustering Results (CSI 100)
Cluster Stock Names Count
1 ZTE Corporation, Eastern Shenghong, Changchun High-Tech,
Unisplendour, Focus Media, Unigroup Guoxin Microelectron-
ics, TCL Zhonghuan Renewable Energy, iFLYTEK, Goertek,
Oriental Yuhong, SF Holding, NAURA Technology, Glodon,
Ganfeng Lithium, Tianqi Lithium, Luxshare Precision, Rong-
sheng Petrochemical, 37 Interactive Entertainment, BYD, LB
Group, Satellite Chemical, EVE Energy, Aier Eye Hospital,
Zhifei Biological, Inovance Technology, Walvax Biotechnology,
Sungrow Power Supply, Zhongji Innolight, Tigermed, China
Northern Rare Earth, China Jushi, Hengli Petrochemical, Hualu
Hengsheng, Tongwei, Hundsun Technologies, Yonyou Network,
Wingtech Technology, AECC Aviation Power, LONGi Green
Energy, China Tourism Group Duty Free, COSCO SHIPPING
Holdings, CMOC Group, China Vanke, TCL Technology, BOE
Technology, Qinghai Salt Lake Industry, Hikvision, Baotou
Steel, CITIC Securities, Poly Developments, China Unicom,
TBEA, Wanhua Chemical, NARI Technology, Pien Tze Huang,
Shandong Gold, China Railway Group, Aluminum Corpora-
tion of China (Chalco), China State Construction Engineering
(CSCEC), CRRC, Zijin Mining, Weichai Power, Gree Electric
Appliances, Baoshan Iron & Steel (Baosteel), SANY Heavy In-
dustry, China Merchants Bank, Hengrui Medicine, Kweichow
Moutai, Conch Cement, Haier Smart Home, China Shenhua
Energy, Ping An Insurance
72
2 Sinopec, PetroChina 2
3 China Yangtze Power 1
4 Industrial and Commercial Bank of China (ICBC) 1
Table 4.7: Comparison of SD-SC Values Between Classical and SD Clustering
Models
NASDAQ Dataset CSI 100 Dataset
SD Classical SD Classical
F ASD(DSD)-K-means 0.1495 0.0546
SASD-K-means 0.3838 -0.3760 0.4827 0.0894
SDSD-K-means 0.1424 -0.1541 0.1872 -0.1645
25

Table 4.8: Comparison of SD-DBI Values Between Classical and SD Clustering
Models
NASDAQ Dataset CSI 100 Dataset
SD Classical SD Classical
F ASD(DSD)-K-means 0.6674 1.5815
SASD-K-means 1.6135 2.6940 1.8048 0.9175
SDSD-K-means 1.0787 2.2599 2.2029 1.3338
Table 4-7 presents the SD-SC values, and Table 4-8 presents the SD-DBI
values. As seen in Table 4-7, the SD-SC values for all ASD-K-means and DSD-K-
means clustering models across both datasets are higher than those of the classic
clustering results. Table 4-8 shows that the SD-DBI values for the first-order
and second-order ASD-K-means and DSD-K-means models on the NASDAQ
dataset are all lower than the classic clustering results, verifying the quality
of the clustering. However, the SD-DBI values for the CSI 100 dataset are
all higher than the classic clustering results, which may be due to the weaker
applicability of the SD-DBI index on this specific dataset.
A comprehensive analysis combining both indices reveals that higher SD-
SC coefficient values reflect better intra-class compactness and inter-class sep-
aration, while lower DBI values verify the rationality and effectiveness of the
clustering results. Therefore, the index results demonstrate that the stochastic
dominance K-means clustering models proposed in this paper exhibit superior
performance in stock clustering tasks targeting different investment preferences.
Consequently, it can be concluded that the ASD-K-means and DSD-K-means
clustering models possess significant advantages in applications regarding stock
clustering based on investor preferences, providing more reliable references for
investment decision-making.
4.3 SD-Hierarchical Clustering Analysis
Based on the theoretical framework established in Section 3.4, this section
conducts hierarchical clustering analysis on the constituent stocks of the CSI 100
and the NASDAQ 100 indices. Depending on the investors’ specific risk prefer-
ences and the applied order of stochastic dominance, the clustering algorithms
are systematically categorized as follows:
For risk-averse investors, the model adopts the ASD-Hierarchical algorithm.
Specifically, when utilizing the first-order, second-order, and third-order stochas-
tic dominance test statistics, the algorithms are denoted as F ASD-Hierarchical,
SASD-Hierarchical, and TASD-Hierarchical, respectively.
Conversely, for risk-seeking investors, the model applies the DSD-
Hierarchical algorithm. Accordingly, corresponding to the application of the
first-order, second-order, and third-order statistics, the algorithms are defined as
FDSD-Hierarchical, SDSD-Hierarchical, and TDSD-Hierarchical, respectively.
26

While the full algorithmic suite incorporates up to the third order, the fol-
lowing empirical evaluations and results will primarily focus on the first- and
second-order clustering scenarios, as they sufficiently capture the fundamental
market behaviors of non-satiation and risk attitude.
4.3.1 ASD-Hierarchical Clustering
This paper first conducts first-order stock hierarchical clustering (F ASD-
Hierarchical clustering) for risk-averse investors, followed by second-order hier-
archical clustering (SASD-Hierarchical clustering) based on the first-order re-
sults. The F ASD-Hierarchical clustering is performed on NASDAQ index con-
stituents and CSI 100 constituents respectively. The optimal number of clusters
selected for NASDAQ stocks is 20. Figure 4-4 plots the heatmap of stochastic
dominance coefficients after clustering. In the figure, the horizontal and vertical
axes represent individual stocks, and each small square represents the stochas-
tic dominance coefficient value between two stocks; larger values correspond
to darker colors. The figure reveals a clear block structure in the stochas-
tic dominance coefficients between stocks after clustering. Compared to the
F ASD-K-means and FDSD-K-means results, the stochastic dominance relation-
ships within and between classes are more distinct after F ASD-Hierarchical and
FDSD-Hierarchical clustering.
Figure 4.4: F ASD-Hierarchical Stochastic Dominance Coefficient Heatmap
(NASDAQ)
Subsequently, the center of each class of stocks is selected as a representative
to compare the first-order stochastic dominance relationships between cluster
centers. Based on the first-order stochastic dominance results of the cluster
27

centers, this paper ultimately selects 75 stocks (excluding those in classes 3,
6, 16, and 17) for second-order hierarchical clustering to obtain more distinct
stochastic dominance relationships and select the optimal stocks for an invest-
ment portfolio. The details of each class of NASDAQ stocks after first-order
hierarchical clustering are shown in Table 4-9.
Table 4.9: F ASD-Hierarchical Clustering Results (NASDAQ)
Cluster Stock Names Count
1 Autodesk, Amazon, ASML, Broadcom, KLA Corp, Meta Plat-
forms
6
2 CoStar Group, IDEXX Laboratories, Intuitive Surgical, Microchip
Technology, Old Dominion Freight Line, Take-Two Interactive
6
3 Gilead Sciences, Sirius XM 2
4 Amgen, AstraZeneca (US ADR), Cognizant, Fastenal, PACCAR,
T-Mobile US, Texas Instruments
7
5 Applied Materials, Fortinet, Lam Research, Lululemon Athletica,
Palo Alto Networks
5
6 Baker Hughes, Illumina, Marvell Technology, Workday 4
7 Booking Holdings, Dollar Tree, Intel, NXP Semiconductors, Qual-
comm, Regeneron Pharmaceuticals, Vertex Pharmaceuticals
7
8 Coca-Cola Europacific Partners, Comcast, Cisco Systems, Star-
bucks
4
9 Micron Technology, ON Semiconductor 2
10 DexCom, Diamondback Energy, MercadoLibre, Netflix 4
11 Apple, Adobe, ANSYS, Cadence Design Systems, CDW Corp,
Intuit, Synopsys
7
12 Analog Devices, Charter Communications, Copart, Electronic
Arts, Alphabet C (GOOG), Alphabet A (GOOGL), Marriott In-
ternational, Monster Beverage, Ross Stores
9
13 Automatic Data Processing (ADP), Costco Wholesale, Paychex,
Roper Technologies, Verisk Analytics
5
14 American Electric Power, Exelon, Honeywell International, Keurig
Dr Pepper, Mondelez International, Xcel Energy
6
15 Cintas, Microsoft, O’Reilly Automotive 3
16 Biogen 1
17 Walgreens Boots Alliance 1
18 NVIDIA 1
19 PepsiCo 1
20 AMD, Tesla 2
Research indicates that there are no obvious first-order stochastic dominance
relationships among the CSI 100 stocks. Therefore, second-order hierarchical
clustering (SASD-Hierarchical clustering) is performed directly on the 76 CSI
100 stocks.
For risk-averse investors, SASD-Hierarchical clustering is conducted on the
28

(a)
 (b)
Figure 4.5: SASD-Hierarchical Stochastic Dominance Coefficient Heatmap
75 NASDAQ constituent stocks and the 76 CSI 100 constituent stocks. The
optimal number of clusters for NASDAQ is 7, while for CSI 100 stocks, the
silhouette coefficient is maximized at approximately 0.72 when clustered into
5 classes. The left chart in Figure 4-5 is the heatmap of stochastic dominance
coefficients for NASDAQ after clustering. It can be seen that stocks are clus-
tered into 7 distinct classes based on the magnitude of stochastic dominance
coefficients; the right chart shows CSI 100 constituents, indicating relatively
poor differentiation in second-order stochastic dominance coefficients.
Comparing the stochastic dominance relationships of the centers of each
class in Table 4-10, it is found thatC 2 ≡C 6 ≡C 7,C 2(C6, C7)≻ 2 C4, and
C2(C6, C7)≻ 2 C5;C 1 ≡C 3, andC 1(C3)≻ 2 C4. Therefore, this paper merges
classes 2, 6, and 7 to form a new class; classes 1 and 3 are merged to form a
new second class. The second-order stochastic dominance relationship between
the two new classes is then compared. Specifics are shown in Table 4-11.
Taking the mean value of the samples in each class in Table 4-11 as the
cluster center, and comparing the second-order stochastic dominance relation-
ship between the centers of the two classes, it is found thatC 1 ≻2 C2. For the
NASDAQ dataset, risk-averse investors can select the 31 stocks in the first class
for investment.
In Table 4-12, comparing the second-order stochastic dominance relation-
ships of the cluster centers reveals thatC 3 ≡C 4 ≡C 5, and they stochastically
dominate all other cluster centers in the second order. For the CSI 100 dataset,
stocks in classes 3, 4, and 5 are selected to construct a suitable investment
portfolio.
4.3.2 DSD-Hierarchical Clustering
Subsequently, stock hierarchical clustering is performed for risk-seeking
investors, starting with first-order hierarchical clustering (FDSD-Hierarchical
clustering), followed by second-order hierarchical clustering (SDSD-Hierarchical
clustering). Both theoretical and experimental results indicate that the results of
29

Table 4.10: SASD-Hierarchical Clustering Results (NASDAQ)
Cluster Stock Names Count
1 ANSYS, Cadence Design Systems, CDW Corp, Intuit, Synopsys 5
2 Analog Devices, Amgen, AstraZeneca (US ADR), Coca-Cola Eu-
ropacific Partners, Comcast, Copart, Cisco Systems, Cognizant,
Electronic Arts, Exelon, Fastenal, Keurig Dr Pepper, Monster
Beverage, PACCAR, Ross Stores, Starbucks, T-Mobile US
17
3 Adobe, Autodesk, Applied Materials, ASML, Broadcom, Booking
Holdings, Charter Communications, Dollar Tree, IDEXX Labo-
ratories, Intel, KLA Corp, Lam Research, Lululemon Athletica,
Marriott International, Meta Platforms, NXP Semiconductors,
Old Dominion Freight Line, Qualcomm, Regeneron Pharmaceuti-
cals, Take-Two Interactive, Vertex Pharmaceuticals
21
4 Tesla 1
5 Apple, AMD, Amazon, CoStar Group, DexCom, Diamondback
Energy, Fortinet, Alphabet C (GOOG), Alphabet A (GOOGL),
Intuitive Surgical, Microchip Technology, MercadoLibre, Micron
Technology, Netflix, NVIDIA, ON Semiconductor, Palo Alto Net-
works
17
6 Automatic Data Processing (ADP), American Electric Power,
Costco Wholesale, Cintas, Honeywell International, Mondelez
International, Microsoft, O’Reilly Automotive, Paychex, Roper
Technologies, Texas Instruments, Verisk Analytics, Xcel Energy
13
7 PepsiCo 1
Table 4.11: Merged SASD-Hierarchical Clustering Results (NASDAQ)
Cluster Stock Names Count
1 Analog Devices, Amgen, AstraZeneca (US ADR), Coca-Cola Eu-
ropacific Partners, Comcast, Copart, Cisco Systems, Cognizant,
Electronic Arts, Exelon, Fastenal, Keurig Dr Pepper, Monster
Beverage, PACCAR, Ross Stores, Starbucks, T-Mobile US, Texas
Instruments, Verisk Analytics, Xcel Energy, Automatic Data Pro-
cessing (ADP), American Electric Power, Costco Wholesale, Cin-
tas, Honeywell International, Mondelez International, Microsoft,
O’Reilly Automotive, Paychex, Roper Technologies, PepsiCo
31
2 ANSYS, Cadence Design Systems, CDW Corp, Intuit, Synopsys,
Adobe, Autodesk, Applied Materials, ASML, Broadcom, Booking
Holdings, Charter Communications, Dollar Tree, IDEXX Labo-
ratories, Intel, KLA Corp, Lam Research, Lululemon Athletica,
Marriott International, Meta Platforms, NXP Semiconductors,
Old Dominion Freight Line, Qualcomm, Regeneron Pharmaceuti-
cals, Take-Two Interactive, Vertex Pharmaceuticals
26
30

Table 4.12: SASD-Hierarchical Clustering Results (CSI 100)
Cluster Stock Names Count
1 China Vanke, TCL Technology, Gree Electric Appliances, BOE
Technology, Hikvision, BYD, Baoshan Iron & Steel (Baosteel),
CITIC Securities, SANY Heavy Industry, Poly Developments,
China Unicom, TBEA, Hengrui Medicine, Wanhua Chemical,
NARI Technology, Hualu Hengsheng, Pien Tze Huang, Shan-
dong Gold, Conch Cement, Haier Smart Home, China Shenhua
Energy, Ping An Insurance, China Railway Group, China State
Construction Engineering (CSCEC), CRRC, Zijin Mining
26
2 ZTE Corporation, Eastern Shenghong, Weichai Power,
Changchun High-Tech, Qinghai Salt Lake Industry, Unisplen-
dour, Focus Media, Unigroup Guoxin Microelectronics, TCL
Zhonghuan Renewable Energy, iFLYTEK, Goertek, Oriental
Yuhong, SF Holding, NAURA Technology, Glodon, Ganfeng
Lithium, Tianqi Lithium, Luxshare Precision, Rongsheng Petro-
chemical, 37 Interactive Entertainment, LB Group, Satellite
Chemical, EVE Energy, Aier Eye Hospital, Zhifei Biological, In-
ovance Technology, Walvax Biotechnology, Sungrow Power Sup-
ply, Zhongji Innolight, Tigermed, Baotou Steel, China North-
ern Rare Earth, China Jushi, Hengli Petrochemical, Tongwei,
Hundsun Technologies, Yonyou Network, Wingtech Technology,
AECC Aviation Power, LONGi Green Energy, Aluminum Cor-
poration of China (Chalco), China Tourism Group Duty Free,
COSCO SHIPPING Holdings, CMOC Group
44
3 China Yangtze Power 1
4 Industrial and Commercial Bank of China (ICBC) 1
5 Sinopec, China Merchants Bank, Kweichow Moutai, PetroChina 4
31

F ASD-Hierarchical clustering and FDSD-Hierarchical clustering are the same.
Therefore, for risk-seeking investors, this paper performs SDSD-Hierarchical
clustering on the 75 NASDAQ constituent stocks and 76 CSI 100 constituent
stocks. The optimal numbers of clusters are 8 and 10, respectively. The left
chart in Figure 4-6 is the heatmap for NASDAQ, the right chart is for CSI 100.
The figure shows good clustering effects for both datasets, with stocks clustered
into classes with distinct differences in stochastic dominance coefficients.
(a)
 (b)
Figure 4.6: SDSD-Hierarchical Stochastic Dominance Coefficient Heatmap
Table 4-13 details the situation where NASDAQ stocks are clustered into 8
classes. Comparing the second-order stochastic dominance relationships of the
stock centers in the table, the centers of classes 4, 5, 6, and 7 stochastically
dominate the centers of classes 1, 2, 3, and 8 in the second order. Therefore, the
stocks in classes 4, 5, 6, and 7 of Table 4-13 are selected for investment choices.
Table 4-14 shows the second-order clustering situation for CSI 100 stocks.
Comparing the second-order stochastic dominance relationships of the stock
centers in the table, it is found that the centers of classes 1 and 2 in Table 4-14
stochastically dominate other class centers in the second order. Therefore, the
16 stocks in classes 1 and 2 of the table are selected for investment choices.
4.3.3 Model Performance Evaluation
The values of the classic Hierarchical clustering results are compared with
those of the ASD-Hierarchical and DSD-Hierarchical clustering models. To en-
sure comparability, the number of clusters selected for the classic clustering
models is kept consistent with that of the SD models.
Table 4-15 presents the SD-SC values, and Table 4-16 presents the SD-DBI
values. As seen in Table 4-15, the SD-SC values for all ASD-Hierarchical and
DSD-Hierarchical clustering models across both datasets are higher than those
of the classic clustering results. Table 4-16 shows that the SD-DBI values for the
first-order and second-order ASD-Hierarchical and DSD-Hierarchical models on
32

Table 4.13: SDSD-Hierarchical Clustering Results (NASDAQ)
Cluster Stock Names Count
1 American Electric Power, Mondelez International, Xcel Energy 3
2 Automatic Data Processing (ADP), Comcast, Costco Wholesale,
Cisco Systems, Exelon, Honeywell International, Keurig Dr Pep-
per, Paychex, Roper Technologies, Starbucks, Verisk Analytics
11
3 Amgen, AstraZeneca (US ADR), Coca-Cola Europacific Part-
ners, Cintas, Cognizant, Fastenal, Microsoft, O’Reilly Automo-
tive, PACCAR, T-Mobile US, Texas Instruments
11
4 Apple, Adobe, Analog Devices, ANSYS, Cadence Design Systems,
CDW Corp, Charter Communications, Copart, CoStar Group,
Dollar Tree, Electronic Arts, Alphabet C (GOOG), Alphabet A
(GOOGL), IDEXX Laboratories, Intel, Intuit, Monster Beverage,
Old Dominion Freight Line, Ross Stores, Synopsys, Take-Two In-
teractive
21
5 Autodesk, Applied Materials, Amazon, ASML, Broadcom, Book-
ing Holdings, Fortinet, Intuitive Surgical, KLA Corp, Lam Re-
search, Lululemon Athletica, Marriott International, Microchip
Technology, Meta Platforms, NXP Semiconductors, Palo Alto
Networks, Qualcomm, Regeneron Pharmaceuticals, Vertex Phar-
maceuticals
19
6 AMD, Tesla 2
7 DexCom, Diamondback Energy, MercadoLibre, Micron Technol-
ogy, Netflix, NVIDIA, ON Semiconductor
7
8 PepsiCo 1
33

Table 4.14: SDSD-Hierarchical Clustering Results (CSI 100)
Cluster Stock Names Count
1 Unisplendour, Unigroup Guoxin Microelectronics, Tianqi
Lithium, 37 Interactive Entertainment, Zhongji Innolight,
Wingtech Technology
6
2 NAURA Technology, Ganfeng Lithium, EVE Energy, Zhifei Bi-
ological, Sungrow Power Supply, Tigermed, Tongwei, Hundsun
Technologies, Yonyou Network, LONGi Green Energy
10
3 Focus Media, SF Holding, AECC Aviation Power, COSCO SHIP-
PING Holdings
4
4 ZTE Corporation, Eastern Shenghong, Changchun High-Tech,
Qinghai Salt Lake Industry, TCL Zhonghuan Renewable Energy,
iFLYTEK, Goertek, Oriental Yuhong, Glodon, Rongsheng Petro-
chemical, BYD, LB Group, Satellite Chemical, Inovance Technol-
ogy, Walvax Biotechnology, China Northern Rare Earth, Hengli
Petrochemical, Aluminum Corporation of China (Chalco), China
Tourism Group Duty Free, CMOC Group
20
5 China Vanke, TCL Technology, BOE Technology, Hikvision, Aier
Eye Hospital, Poly Developments, TBEA, China Jushi, Wanhua
Chemical, NARI Technology, Hualu Hengsheng, Pien Tze Huang,
Shandong Gold, Zijin Mining
14
6 Weichai Power, Gree Electric Appliances, Baoshan Iron & Steel
(Baosteel), SANY Heavy Industry, China Merchants Bank, Hen-
grui Medicine, Kweichow Moutai, Conch Cement, Haier Smart
Home, China Shenhua Energy, Ping An Insurance
11
7 Luxshare Precision 1
8 Baotou Steel, CITIC Securities, China Unicom, China Railway
Group, China State Construction Engineering (CSCEC), CRRC
6
9 China Yangtze Power, Industrial and Commercial Bank of China
(ICBC)
2
10 Sinopec, PetroChina 2
Table 4.15: Comparison of SD-SC Values Between Classical and SD Clustering
Models
NASDAQ Dataset CSI 100 Dataset
SD Classical SD Classical
F ASD(DSD)-HIE 0.4301 0.2019
SASD-HIE 0.5460 -0.5140 0.7167 -0.0431
SDSD-HIE 0.3667 -0.3195 0.3263 -0.3097
34

Table 4.16: Comparison of SD-DBI Values Between Classical and SD Clustering
Models
NASDAQ Dataset CSI 100 Dataset
SD Classical SD Classical
F ASD(DSD)-HIE 1.25 1.4509
SASD-HIE 2.2078 2.4571 2.2598 1.101
SDSD-HIE 1.6318 1.6602 8.4478 0.998
the NASDAQ dataset are all lower than the classic clustering results, verifying
the quality of the clustering. However, the SD-DBI values for the CSI 100
dataset are all higher than the classic clustering results, which may be due to
the weaker applicability of the SD-DBI index on this specific dataset.
A comprehensive analysis combining both indices reveals that higher SD-SC
coefficient values reflect better intra-class compactness and inter-class separa-
tion, while lower DBI values verify the rationality and effectiveness of the clus-
tering results. Therefore, the index results demonstrate that the SD-Hierarchical
clustering models proposed in this paper exhibit superior performance in stock
clustering tasks targeting different investment preferences. Consequently, it
can be concluded that the ASD-Hierarchical and DSD-Hierarchical clustering
models possess significant advantages in applications regarding stock clustering
based on investor preferences, providing more reliable references for investment
decision-making.
4.4 SD-K-means Model Application
4.4.1α−βPlots
Figure 4-7 plots the excess return and risk volatility of NASDAQ constituents
relative to the NASDAQ index average return, as well as CSI 100 constituents
relative to the CSI 100 index average return. The horizontal axisαrepresents
the excess return of a stock or portfolio relative to the market average return;
the vertical axisβrepresents the volatility of a stock or portfolio relative to
the entire market, i.e., risk. Additionally, the relationship between stock return
changes and overall market performance can be intuitively understood from the
figure, providing wiser guidance for investors.
From the perspective of creation potential, the difference between the opti-
mal class of stocks selected and the unselected stocks is not significant, but there
are significant differences in terms of market fluctuations: theβvalues of stocks
selected by the SASD-K-means algorithm are lower than those of other classes,
locating these stocks in the lower half of the graph. Conversely, theβvalues
of stocks selected by the SDSD-K-means algorithm are opposite, located in the
upper half. This aligns with the behavior of risk-averse individuals preferring
low risk and low return, and risk-seekers preferring high risk and high return.
35

(a) NASDAQ SASD K-meansα-β
 (b) NASDAQ SDSD K-meansα-β
(c) CSI 100 SASD K-meansα-β
 (d) CSI 100 SDSD K-meansα-β
Figure 4.7:α−βPlots for Different Datasets
36

4.4.2 Portfolio Risk-Return Plots
Figure 4.8: NASDAQ ASD portfolio
effect
Figure 4.9: NASDAQ DSD portfolio
effect
Figure 4.10: CSI 100 ASD portfolio
effect
Figure 4.11: CSI 100 DSD portfolio
effect
Appropriate numbers of stocks are selected from the optimal class and the
non-optimal class respectively to construct minimum variance portfolios, an-
alyzing the risk and expected return of portfolios from different classes. The
horizontal axis represents portfolio risk, and the vertical axis represents expected
return. As seen in Figures 4-8 and 4-9, after clustering NASDAQ constituents,
there are clear class relationships in the risk-expected return of portfolios con-
structed by drawing different numbers of stocks from different classes.
For risk-averse investors, judging from the NASDAQ clustering results (Fig-
ure 4-8), portfolios constructed from stocks selected by the SASD-K-means algo-
rithm possess low risk and high return, indicating significant algorithm effective-
ness. Due to the smaller number of optimal stocks in CSI 100, no obvious cluster
structure is visible (see Figure 4-10), but the selected stocks and constructed
portfolios still possess low risk and low return characteristics compared to other
37

stocks. When the number of stocks in the portfolio is 2, after 100 draws, the
average return of the optimal class is 0.0023, lower than the non-optimal class’s
0.0026; but simultaneously, the risk is 0.0004, also lower than the non-optimal
class’s 0.0032, aligning with risk-averse preferences.
For risk-seeking investors, Figure 4-9 reveals that portfolios constructed from
NASDAQ stocks selected by the SDSD-K-means algorithm possess high risk and
high return, and there is an obvious cluster structure among portfolios; the more
stocks in the portfolio, the clearer the structure. As seen in Figure 4-11, the
effect for CSI 100 is relatively worse than NASDAQ due to the number of stocks,
but still exhibits high risk and high return characteristics. For example, when
the number of stocks is 2, after 100 draws, the average return of the optimal
class is 0.0026, higher than the non-optimal class’s 0.0017; but simultaneously,
the risk is 0.00109, also higher than the non-optimal class’s 0.00047, aligning
with risk-seeking preferences.
Through the above graphical analysis, it is found that: stochastic domi-
nance clustering algorithms can effectively cluster numerous stocks into differ-
ent classes based on investor preferences, and portfolios constructed from the
selected optimal stocks also exhibit clear cluster structures. This verifies that
the novel stochastic dominance clustering models proposed in this paper have
significant application value in constructing minimum variance portfolios and
can provide customized investment portfolio selection schemes for investor pref-
erences. Furthermore, the new models are operable in risk control and asset
allocation, allowing for asset allocation based on the risk levels investors can
accept.
4.5 SD-Hierarchical Model Application
4.5.1α−βPlots
Figure 4-12 plots the excess return and risk volatility of NASDAQ con-
stituents relative to the NASDAQ index average return, as well as CSI 100
constituents relative to the CSI 100 index average return. The horizontal axis
αrepresents the excess return of a stock or investment portfolio relative to the
market average return; the vertical axisβrepresents the volatility of a stock or
investment portfolio relative to the entire market, i.e., risk. From the perspective
of creation potential, similar to the K-means clustering results, the difference
between the optimal class of stocks selected and the unselected stocks is not
significant; however, in terms of risk, there are differences in the risk of stocks
selected by algorithms corresponding to different risk preferences. Additionally,
the relationship between stock return changes and overall market performance
can be intuitively understood from the figure, providing wiser guidance for in-
vestors to make decisions.
The SASD-Hierarchical algorithm and SDSD-Hierarchical algorithm perform
better on the NASDAQ dataset than on the CSI 100 constituent stocks. The
α−βplot for NASDAQ stocks shows a clear cluster structure. Theβvalues
of stocks selected by the SASD-Hierarchical algorithm are relatively low, while
38

(a) NASDAQ SASD Hierarchicalα-β
 (b) NASDAQ SDSD Hierarchicalα-β
(c) CSI 100 SASD Hierarchicalα-β
 (d) CSI 100 SDSD Hierarchicalα-β
Figure 4.12:α−βPlots for Different Datasets
39

theβvalues of stocks selected by the SDSD-Hierarchical algorithm are at a
relatively high level. However, there is no obvious segmentation among CSI 100
stocks. The differences in the market structure and development potential of the
US and Chinese stock markets are considered to lead to the difference in results
on theα−βplots. Next, this paper selects an appropriate number of stocks
from different classes to construct minimum variance portfolios, compares the
risk and expected return of portfolios from different classes, and discusses the
performance of the proposed algorithms in another application scenario.
4.5.2 Portfolio Risk-Return Plots
Figure 4.13: NASDAQ ASD portfolio
effect
Figure 4.14: NASDAQ DSD portfolio
effect
Figure 4.15: CSI 100 ASD portfolio
effect
Figure 4.16: CSI 100 DSD portfolio
effect
In the figures, the horizontal axis represents the risk of the investment port-
folio, and the vertical axis represents the expected return of the portfolio. Fig-
ures 4-13 and 4-15 are the risk-return plots of investment portfolios constructed
from stocks selected by risk-averse investors. The portfolios constructed from
40

the optimal class of stocks have relatively lower returns compared to portfolios
constructed from other classes of stocks, but simultaneously, the risk is also
low. Figures 4-14 and 4-16 are the risk-return plots of investment portfolios
constructed from stocks selected by the SDSD-Hierarchical algorithm for the
two datasets, both exhibiting high risk and high return characteristics. The
investment portfolios constructed from stocks obtained by these two hierarchi-
cal clustering methods show clear cluster structures between classes. As the
number of investment portfolios increases, the cluster structure becomes more
obvious, and the risk-expected return of stocks within the same class is compact
and similar.
The risk-return distribution plots above indicate: stochastic dominance clus-
tering algorithms can effectively cluster numerous stocks into different classes
based on investor preferences, and the investment portfolios constructed from
the selected optimal stocks also exhibit clear cluster structures. This verifies
that the novel stochastic dominance clustering models proposed in this paper
have significant application value in constructing minimum variance portfolios
and can provide customized investment portfolio selection schemes for investor
preferences. Furthermore, the new models are operable in risk control and as-
set allocation, allowing for reasonable asset allocation based on the risk levels
investors can accept.
A comprehensive comparison of the clustering performance of ASD-K-means,
ASD-Hierarchical, DSD-K-means, and DSD-Hierarchical algorithms across dif-
ferent datasets reveals: judging from the distribution plots of investment port-
folios, compared to the DSD-K-means algorithm, the clustering effect of the
DSD-Hierarchical algorithm is more significant, and the inter-class separation
is greater, meaning the Hierarchical algorithm is better able to cluster stocks
into classes with significant stochastic dominance relationships. In addition, it
can also be found that the performance of NASDAQ constituent stock data on
stochastic dominance clustering models is superior to that of CSI 100 constituent
stock data.
5 Conclusion and Outlook
This paper proposed corresponding SD-K-means clustering algorithms and
SD-Hierarchical clustering algorithms based on the first-order, second-order, and
third-order stochastic dominance relationships for risk-averse and risk-seeking
investors, respectively. Using the clustering algorithms and the SD-SC coeffi-
cient to select the optimal number of clusters, the NASDAQ index constituents
and CSI 100 index constituents were clustered. After clustering, the class center
was taken as the representative of each class to compare the stochastic dom-
inance relationships between cluster centers, and the class where the center
stochastically dominating other class centers is located was selected for subse-
quent investment or portfolio construction.
Since using the first-order and second-order stochastic dominance relation-
ships of stocks can already divide stocks into classes with obvious structures, this
41

paper used first-order and second-order clustering algorithms. If the first-order
and second-order clustering algorithms cannot well divide stocks into classes
with obvious stochastic dominance relationships, one can further consider third-
order or higher-order K-means clustering and Hierarchical clustering algorithms
to cluster stocks.
When constructing the SD-SC coefficient and SD-DBI index to evaluate the
clustering results, it was found that for the NASDAQ dataset, the final cluster-
ing results of the clustering models in this paper had higher SD-SC coefficient
values and lower DBI values compared to classic K-means clustering and Hi-
erarchical clustering models. This reflects better intra-class compactness and
inter-class separation, confirming the rationality of the clustering results of the
new algorithms proposed in this paper. The SD-SC coefficient values for the
CSI 100 index dataset were also higher than those of the classic K-means clus-
tering and Hierarchical clustering models, but the SD-DBI values were all higher
than the classic clustering results, which is considered to be due to the weaker
applicability of the SD-DBI index on this dataset.
In addition, the application effects of the SD clustering models on single
index models and the construction of global minimum variance portfolios were
explored, which also verified that the algorithms proposed in this paper can
well provide customized asset allocation schemes for investors with different
risk preferences, possessing great practical application value. A comprehensive
comparative analysis of the effects shows: compared to the SD-K-means cluster-
ing algorithm, the SD-Hierarchical algorithm is better able to cluster stocks into
classes with significant stochastic dominance relationships, and the clustering
effect is superior. Furthermore, the performance of NASDAQ constituent stock
data on stochastic dominance clustering models is superior to that of CSI 100
constituent stock data.
The analysis in this paper also found that the algorithms proposed herein
can divide stocks into two categories based on their stochastic dominance rela-
tionships: for risk-averse investors, the selected stocks have the characteristics
of low risk and low return; for risk-seeking investors, the selected stocks provide
higher returns and higher risks. The expected returns and returns of investment
portfolios constructed from different categories of stocks also show different clus-
ter structures. This indicates that the algorithms proposed in this paper can
well provide assistance to investors with different preferences when making in-
vestment decisions.
Although the SD-Hierarchical clustering algorithm and SD-K-means cluster-
ing algorithm proposed in this paper have achieved relatively good results in the
clustering analysis of NASDAQ 100 index and CSI 100 constituents, there are
still some deficiencies. Firstly, the sample scope is limited: currently, empirical
research is only conducted on specific markets (such as US stocks and partial
A-share constituents) and has not yet been expanded to the entire stock market,
which may affect the universality of the model. Secondly, currently, only the
SD-SC coefficient and SD-DBI index have been constructed to evaluate the clus-
tering results, and a more comprehensive investor preference-oriented evaluation
system has not yet been constructed.
42

Based on the results and deficiencies of this study, future research can be
deepened from the following aspects: First, consider expanding the research
scope to conduct empirical analysis on the entire stock market. In addition, this
paper will further optimize the SD-K-means clustering algorithm and modify
the distance matrices of other classic clustering algorithms to improve more al-
gorithms, compare the performance of different algorithms, and conduct a more
comprehensive and scientific evaluation of the effectiveness and applicability of
various clustering methods under different market conditions on a larger scale.
Furthermore, consider constructing other stochastic dominance clustering eval-
uation indices and deeply analyzing the applicability issue of the SD-DBI index
on the CSI 100 dataset, in order to comprehensively verify that the clustering
models in this paper have significant advantages in investor preference-oriented
stock clustering applications, providing more reliable references for risk-averse
and risk-seeking investors when making investment decisions.
References
Yang Xiaojun. Research on k-means clustering algorithm and its application in
stock investment. Master’s thesis, Chongqing University, 2019.
Dingming Wu, Xiaolong Wang, and Shaocong Wu. Construction of stock port-
folios based on k-means clustering of continuous trend features.Knowledge-
Based Systems, 252:109358, 2022.
xue Fei Huang, Xin Zhao, and Cheng Li. Clustering effect of style based on
pearson correlation: Example of sse50 sample stocks. In2010 International
Conference on Internet Technology and Applications, pages 1–4. IEEE, 2010.
Yahui Lu, Minghao Li, Xiaochu Tang, and Hui Wang. A new cluster validity
index for stock clustering based on efficient frontier. In2020 5th IEEE Inter-
national Conference on Big Data Analytics (ICBDA), pages 193–197. IEEE,
2020.
Jerzy Korzeniewski. Efficient stock portfolio construction by means of clustering.
Acta Universitatis Lodziensis. Folia Oeconomica, 1(333):85–92, 2018.
Francisco L´ ucio and Jorge Caiado. Covid-19 and stock market volatility: A
clustering approach for s&p 500 industry indices.Finance Research Letters,
49:103141, 2022.
Bakti Siregar and Yosia Yosia. Implementation of k-means clustering algorithm
for the indonesian stock exchange.Jurnal Sisfotek Global, 14(1):49–56, 2024.
CF A Guy et al. Upside and downside beta portfolio construction: A different
approach to risk measurement and portfolio construction.Available at SSRN
2612235, 2014.
43

Marcel-Ioan Bolos,, S, tefan Rusu, Marius Leordeanu, Claudia Diana Sab˘ au-Popa,
Diana Claudia Pert,icas,, and Mihai-Ioan Cris,an. K-means clustering for port-
folio optimization: Symmetry in risk–return tradeoff, liquidity, profitability,
and solvency.Symmetry, 17(6):847, 2025.
Daniel McFadden. Testing for stochastic dominance. In Thomas B. Fomby and
Tae Kun Seo, editors,Studies in the Economics of Uncertainty: In Honor of
Josef Hadar, pages 113–134. Springer New York, New York, NY, 1989. ISBN
978-1-4613-8924-8 978-1-4613-8922-4.
Lindsey Klecan, Raymond McFadden, and Daniel McFadden. A robust test for
stochastic dominance.working paper, Department of Economics, MIT, 1991.
Garry F. Barrett and Stephen G. Donald. Consistent tests for stochastic domi-
nance.Econometrica, 71(1):71–104, 2003.
Oliver Linton, Esfandiar Maasoumi, and Yoon-Jae Whang. Consistent testing
for stochastic dominance under general sampling schemes.The Review of
Economic Studies, 72(3):735–765, 2005.
Michael McAleer, Hooi Hooi Lean, and Wing-Keung Wong. Stochastic domi-
nance test for risk seekers: An application to oil spot and futures markets.
SSRN Electronic Journal, 2006.
Songsak Sriboonchitta, Wing-Keung Wong, s Dhompongsa, and Hung Nguyen.
Stochastic Dominance and Applications to Finance, Risk and Economics.
Chapman and Hall/CRC, 2009. ISBN 978-0-429-13814-0.
Zhidong Bai, Hua Li, Michael McAleer, and Wing-Keung Wong. Stochastic
dominance statistics for risk averters and risk seekers: An analysis of stock
preferences for usa and china.Quantitative Finance, 15(5):889–900, 2015.
Haim Levy. Upper and lower bounds of put and call option value: Stochastic
dominance approach.The Journal of Finance, 40(4):1197–1217, 1985.
Thierry Post. Empirical tests for stochastic dominance efficiency.The Journal
of Finance, 58(5):1905–1931, 2003.
Wing-Keung Wong. Stochastic dominance and mean–variance measures of profit
and loss for business planning and investment.European Journal of Opera-
tional Research, 182(2):829–843, 2007.
Hua Li.Test Statistics for Prospect and Markowitz Stochastic Dominances with
Applications. PhD thesis, Northeast Normal University, 2013.
Chi-Kwong Li and Wing-Keung Wong. Extension of stochastic dominance
theory to random variables.RAIRO - Operations Research - Recherche
Op´ erationnelle, 33(4):509–524, 1999.
Russell Davidson and Jean-Yves Duclos. Statistical inference for stochastic
dominance and for the measurement of poverty and inequality.Econometrica,
68(6):1435–1464, 2000.
44
