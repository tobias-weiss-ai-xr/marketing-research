---
title: 'MomentQuant: an even more minimalist interval method with linear time complexity for time series
  classification'
url: https://arxiv.org/abs/2609.05136
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Johann Faouzi
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.05136
pages: 83
chars: 205088
fetched_at: '2026-11-08T13:30:37+00:00'
kb_version: 1
---

# MomentQuant: an even more minimalist interval method with linear time complexity for time series classification

MomentQuant: an even more minimalist interval
method with linear time complexity for time series
classification
Johann Faouzi
Univ Rennes, Ensai, CNRS, CREST - UMR 9194, F-35000 Rennes,
France.
Contributing authors: johann.faouzi@ensai.fr;
Abstract
Time series data is very common in many real-world applications and in numer-
ous domains, with increasing interest for automated information extraction using
machine learning. One of these subfields is time series classification, which con-
sists in assigning a label to each new, unseen time series. Many algorithms
have been developed over the past decades, with the trade-off between predic-
tive performance and computational cost being consistently discussed. Quant, an
interval-based algorithm extracting quantiles from recursive, fixed, dyadic inter-
vals, was shown to achieve high accuracy, while being very fast. We propose two
changes to make this algorithm even faster. The first one is a better optimized
implementation of the exact same algorithm. The second one is to derive approx-
imate quantiles, using the Cornish-Fisher expansion, instead of exact quantiles.
This change removes the necessity to sort the time series, leading to a smaller
computational complexity. We call this novel algorithm MomentQuant. We pro-
vide evidence that our implementation of Quant is faster than the original one,
and that MomentQuant is even faster than our implementation of Quant, at the
cost of a tiny decrease in predictive performance. These improvements are espe-
cially relevant for real-life applications, where inference is performed much more
often than training.
Keywords:time series classification, time series, classification, machine learning,
supervised learning, feature extraction, quantiles, moments
1
arXiv:2609.05136v1  [cs.LG]  4 Sep 2026

1 Introduction
Time series classification is the supervised learning task of assigning a discrete label to
a time-ordered sequence of measurements, and it arises across a wide range of appli-
cation domains, including health monitoring, industrial process control, astronomy,
and human activity recognition. Because the discriminative structure of a time series
can lie in its overall shape, in local patterns, or in its frequency content, depending
on the domain, methods that perform consistently well across many kinds of data sets
typically combine features extracted from several complementary representations of
the input series rather than committing to a single one. The introduction and steady
growth of the University of California, Riverside (UCR) time series archive (Dau et
al., 2019), a public collection of benchmark data sets spanning dozens of application
domains, made it possible to compare such methods systematically, and has driven
two decades of active method development in the field.
This growth has, however, exposed a persistent tension between predictive accuracy
and computational cost. The most accurate methods on the UCR archive are typi-
cally large, heterogeneous ensembles combining several complementary representations
and classifiers, such as the Hierarchical Vote Collective of Transformation Ensembles
(HIVE-COTE) 2.0 (Middlehurst et al., 2021). Their accuracy gains come at a steep
computational price, often requiring hours or days to train and test even on the com-
paratively small (by modern machine learning standards) UCR data sets, which makes
them impractical to scale to larger data sets or to apply repeatedly, e.g., for hyperpa-
rameter tuning. This tension motivated a distinct line of work seeking to reproduce
most of that accuracy at a small fraction of the cost, most prominently the Ran-
dom Convolutional Kernel Transform (ROCKET) algorithm (Dempster, Petitjean, &
Webb, 2020) and its successor MiniRocket (Dempster, Schmidt, & Webb, 2021), which
summarize each series through a large bank of (random or fixed) convolutional kernels
and train a linear classifier on the resulting features, reaching near-state-of-the-art
accuracy while being orders of magnitude cheaper to train than the heterogeneous
ensembles above.
Quant (Dempster, Schmidt, & Webb, 2024) is a recent, markedly simpler entry in
this second line of work. Rather than convolutional kernels, it computes a single type
of feature, empirical quantiles, from a fixed, hierarchical set of intervals of each series,
over four complementary representations of the series (the raw series, a smoothed first-
order difference, the second-order difference, and the magnitude of its discrete Fourier
transform), and feeds the concatenated quantiles, unchanged, to an off-the-shelf tree
ensemble classifier. Despite this minimalism, and despite using a single feature type
where most interval-based methods before it combined several, Quant matches the
accuracy of the most accurate interval-based methods on the UCR archive, and stays
close in aggregate accuracy to the very best, much more expensive heterogeneous
ensembles. Quant only needs, by the original authors’ own account, under fifteen
minutes of combined training and inference time on a single central processing unit
(CPU) core to process the 142 univariate data sets of the UCR archive (Dempster et
al., 2024).
Although Quant’s overall speed is undeniable, its computational complexity has
not been established so far. The original publication has a short section on this topic,
2

but does not provide an in-depth analysis (Dempster et al., 2024). The authors mention
that they “treat the computational cost of sorting the values as an upper bound on
the cost of computing the quantiles:O(l·log(l)), wherelis the time series length”.
However, the subseries from each interval are also sorted, not just the whole time
series, in order to compute the quantiles. Moreover, the authors do not prove that the
cost of computing the quantiles is upper bounded by the cost of sorting the values. The
authors also provide the computational complexity of the training of the classification
step of Quant, and their results demonstrate that the training the classification step is
the longest part of the whole pipeline. Overall, the original publication overlooks the
computational complexity of the transformation step, as if it was irrelevant compared
to the computational complexity of the classification step. We will demonstrate that
this analysis does not hold when considering only the inference phase of the algorithm,
which is very relevant for real-life applications of any machine learning model, and is
too often overlooked in the time series classification literature. We will also provide
an in-depth analysis of the computational complexity of Quant, both theoretical and
practical.
Quant’s overall speed does not mean that every part of its reference implemen-
tation1 is equally well suited to every setting that it is run in. The implementation
commits to a single, fixed computational structure: one call to PyTorch’s batched
torch.quantilefunction per interval, amortized over the whole batch of series at
once. This is a natural design for a tensor library built around batched, hardware-
accelerated execution. However, it is not well-matched to either end of the series-length
spectrum on a single CPU core, the setting that Quant’s own headline runtime figures
above were obtained in, as we detail in Section 3. For short series, the fixed per-call dis-
patch overhead of this design, paid once per interval regardless of how little work that
interval actually requires, comes to dominate the total cost. For long series, the same
design instead pays a growing sorting cost, since exactly computing a set of quantiles
fromlraw values requires first sorting them, which is anO(l·log(l)) operation.
This paper addresses both regimes, but its main contribution targets the long-
series one. We reimplement Quant from scratch in NumPy, both to reproduce the
original algorithm faithfully as anexactmode, which we further speed up for short
series (Section 5) by choosing between two different loop orderings for the same com-
putation, guided by a full theoretical cost analysis (Section 4). Then, we introduce a
genuinely newapproximatemode aimed at long series. Instead of sorting each inter-
val to obtain its exact quantiles, this approximate mode estimates them directly from
that interval’s own sample mean, variance, skewness, and excess kurtosis. These four
quantities are computable in a singleO(l) pass, via the Cornish-Fisher expansion
(Cornish & Fisher, 1938; Fisher & Cornish, 1960), a classical asymptotic correction of
the standard normal quantile for a distribution’s departure from normality. Doing so
trades the exact mode’sO(l·log(l)) sorting cost for anO(l) moment-based one, at the
cost of a small, and, as we show empirically, largely controllable approximation error.
Concretely, this paper makes the following contributions:
• A precise theoretical cost model, with proofs, for the exact mode and its two nat-
ural loop orderings (Section 4 and Section 5), and for the new approximate mode
1https://github.com/angus924/quant
3

(Section 6), including a closed-form asymptotic characterization of how each mode’s
total cost scales with series length.
• A moment-based approximate mode for Quant built on the Cornish-Fisher expan-
sion, together with an empirical study of its quantile-approximation fidelity and of
the resulting accuracy and runtime trade-off, conditioned on series length, across
the 142 univariate data sets of the UCR archive (Section 6 and Section 8).
• An automatic dispatch heuristic for each mode (exact and approximate), calibrated
per machine, that selects between the loop orderings, based on the series length at
hand (Section 6, Section 8).
• A comprehensive, single-threaded and multithreaded analysis of an optimization
that was mentioned in (Dempster et al., 2024), but neither implemented nor
evaluated (Section 9).
The remainder of this paper is organized as follows. Section 2 provides some back-
ground, with an overview of the time series classification literature, the interval-based
methods, and Quant. In Section 3, we explain the specific limitations of Quant’s
reference implementation that motivate this paper. Section 4 develops a theoretical
cost model for processing a single series under Quant’s exact quantile computation.
Section 5 uses this model to choose, for the exact mode, between two loop orderings
depending on series length. In Section 6, we introduce the moment-based approxi-
mate mode built on the Cornish-Fisher expansion, together with its own cost model.
Section 7 presents our experimental setup, while Section 8 presents all our results. We
investigate the optimization mentioned in Quant’s original publication in Section 9,
before concluding in Section 10.
2 Background
We divide this section dedicated to the relevant background into three parts. First, we
provide an overview of the time series classification literature. Then, we focus on the
specific family of algorithms that Quant belongs to. Finally, we provide an in-depth
presentation of the Quant algorithm. For a recent review of the time series classification
literature, we refer the readers to (Middlehurst, Sch¨ afer, & Bagnall, 2024). We will not
cover deep learning in this section and refer the readers to (Ismail Fawaz, Forestier,
Weber, Idoumghar, & Muller, 2019) and (Mohammadi Foumani et al., 2024).
2.1 Time series classification
Numerous algorithms for time series classification have been developed over the past
decades. These methods can be grouped in different families based on their structures.
Distance-based methods rely on computing (dis)similarity scores between samples.
For classification, such classic methods include nearest-neighbor methods (Cover &
Hart, 1967; Fix & Hodges, 1989) and support vector machines (Cortes & Vapnik,
1995). For time series classification, specific distances and kernels have been devel-
oped. Dynamic Time Warping (DTW) (Berndt & Clifford, 1994; Sakoe & Chiba, 1978)
is an elastic distance that uses dynamic programming to find the optimal alignment
4

between two time series by computing the minimum path through a cost matrix con-
sisting of the pairwise point-wise squared differences. Several variants of DTW have
been developed, some of them adding a region constraint on the possible set of paths
(Itakura, 1975; Sakoe & Chiba, 1978) and some others adding weights penalizing
alignments with high phase differences (Herrmann & Webb, 2023; Jeong, Jeong, &
Omitaomu, 2011). Global alignment kernels (Cuturi, 2011; Cuturi, Vert, Birkenes, &
Matsui, 2007) are kernels specific to time series that can be used with support vector
machines for classification.
Feature-based approaches consist in computing statistics from the whole time
series. For time series classification, a standard classification algorithm is then built
on top of these derived statistics. The canonical time series characteristics (Catch22)
(Lubba et al., 2019) are 22 features that have been determined to be discriminative
on the UCR data sets (Dau et al., 2019), and a decision tree was used to perform
classification. The Time Series Feature Extraction based on Scalable Hypothesis Tests
(TSFresh) algorithm (Christ, Braun, Neuffer, & Kempa-Liehr, 2018) is a set of nearly
800 features extracted from time series. This set of features can be pruned using sta-
tistical tests. The Random forest (Breiman, 2001) and AdaBoost (Freund & Schapire,
1996) algorithms were investigated to perform classification using these extracted
features.
Shapelets are subseries extracted from the training time series and used to differ-
entiate time series. To do so, the most commonly used metric is the minimum of the
Euclidean distances between the shapelet and all the subseries, of the same length as
the shapelet, extracted from the time series. For time series classification, shapelets
were first investigated in (Ye & Keogh, 2011) and the transformation was followed
by a decision tree to perform classification. The Shapelet Transform Classifier (STC)
(Hills, Lines, Baranauskas, Mapp, & Bagnall, 2014) extracts all the possible shapelets
from the training set before selecting the most discriminative ones, followed by an
ensemble of classifiers. Several refinements have been made since the release of its orig-
inal version to improve its performance and scalability, notably performing a random
search for the shapelets and using a single classification algorithm on top of the trans-
formation (Bostrom & Bagnall, 2017; Bostrom, Bagnall, & Lines, 2016). The Random
Dilated Shapelet Transform (RDST) algorithm (Guillaume, Vrain, & Elloumi, 2022)
adds two novel elements to existing shapelet-based approaches: dilation and two new
features (the position of the minimum distance and the number of occurrences of the
shapelet).
Dictionary-based methods, similarly to shapelet-based approaches, also extract
subseries from time series. However, no distance between the subseries and the time
series is computed. Instead, each subseries is turned into a short sequence of discrete
symbols, which is usually called a word. The frequencies of all the words extracted from
a time series are then computed to obtain the new representation of this time series.
For time series classification, a standard machine learning classification algorithm is
applied on top of this transformation. There exist two main symbolic representations
of time series. The first one, in the time domain, is the Symbolic Aggregate approX-
imation (SAX) (Lin, Keogh, Wei, & Lonardi, 2007), which performs dimensionality
reduction first in the time domain (using the mean from non-overlapping windows)
5

and then in the value domain (using discretization based on quantiles). The second
one, in the frequency domain, is the Symbolic Fourier Approximation (SF A) (Sch¨ afer
& H¨ ogqvist, 2012), which computes the discrete Fourier transform of the time series,
selects a subset of the Fourier coefficients, and discretizes them (using quantiles).
Several algorithms in this family have been developed, mostly using the SF A repre-
sentation. The Bag-of-SF A-Symbols (BOSS) model (Sch¨ afer, 2015) extracts subseries
from a time series using overlapping windows, then transforms each subseries into
a word using SF A, and finally the word frequencies are computed. An ensemble of
BOSS models is used in practice, with different values for several hyperparameters.
The Word Extraction for Time Series Classification (WEASEL) algorithm (Sch¨ afer &
Leser, 2017) involves several new changes compared to BOSS. Notably, the selection
of the Fourier coefficients is supervised (using ANOV A tests), the quantization of SF A
is also supervised (using information gain), bigrams and multiple window lengths are
considered, a subset of words is selected in a supervised fashion (using chi-squared
tests), and the classification step is replaced with logistic regression. WEASEL was
later refined in a new version called WEASEL 2.0 (Sch¨ afer & Leser, 2023), adding
notably a novel dilation mapping, using less supervised selection methods in SF A, and
replacing logistic regression with a Ridge classification algorithm.
Convolution-based methods rely on the convolution operator to extract features
from time series using kernels. However, it has been shown that using random kernels
instead of learned kernels is much faster but still very effective for time series classifi-
cation. This strategy was introduced with the ROCKET algorithm (Dempster et al.,
2020). ROCKET generates numerous random kernels (with random length, weights,
bias, padding and dilation), applies the convolution for each of them, and extracts two
aggregate features for each of them: the maximum value and the proportion of positive
values. Finally, a Ridge classifier is trained on these extracted features. ROCKET has
been extended in two versions. The first one is MiniRocket (Dempster et al., 2021),
which involves much less randomness in the generation of the kernels than ROCKET
and only the proportion of positive values is derived. The second extension is Multi-
Rocket (Tan, Dempster, Bergmeir, & Webb, 2022), which adopts the improvements of
MiniRocket but also includes two notable new changes: more features are derived, and
half of the convolutions are applied to the first-order difference of the time series. A
model combining both dictionary- and convolution-based approaches, called HYbrid
Dictionary-ROCKET Architecture (Hydra) (Dempster, Schmidt, & Webb, 2023), was
later proposed. The kernels are aggregated into groups, the best matching kernel
among each group is recorded, and their frequencies are computed.
Hybrid algorithms combine algorithms from different families in order to cover
as many data sets and problems as possible. HIVE-COTE (Lines, Taylor, & Bag-
nall, 2018) is a heterogeneous ensemble consisting of five algorithms, each from a
different representation. This algorithm was updated shortly after to improve its scal-
ability: HIVE-COTE 1.0 (Bagnall, Flynn, Large, Lines, & Middlehurst, 2020) uses
four algorithms instead of five, and faster algorithms from each family. HIVE-COTE
2.0 (Middlehurst et al., 2021) addresses further scalability issues and updates its
components to use better, faster algorithms.
6

2.2 Interval-based methods
The pipelines of most interval-based methods are very similar. Intervals are defined
to extract subseries from the whole series. From each subseries, descriptive statistics
(such as the mean, the variance, higher-order moments, quantiles, etc.) are extracted.
Additionally, in several methods, multiple representations (such as the first-order dif-
ference and the discrete Fourier transform) of the whole series are used in order to
extract more diverse features. All the extracted features are then concatenated to
obtain the design matrix, which is finally fed to a standard machine learning classi-
fication. Tree-based algorithms are the most commonly used classification algorithms
with interval-based methods.
The Time Series Forest (TSF) algorithm (Deng, Runger, Tuv, & Vladimir, 2013)
selects several random intervals, computes three statistics for each interval (the mean,
the standard deviation and the slope) and all the features are concatenated to train
a decision tree. This process is repeated several times (with different random inter-
vals and different trees) to build an ensemble model, with the final prediction being
obtained using majority voting.
The TSF algorithm has received two extensions. Supervised Time Series Forest
(STSF) (Cabello, Naghizade, Qi, & Kulik, 2020) includes several representations of the
time series (raw, first-order difference, and discrete Fourier transform) and a supervised
method for selecting the most discriminative interval features using a decision tree.
Several decision trees are built using this process, and the final prediction is obtained
using majority voting. Randomized STSF (RSTSF) (Cabello, Naghizade, Qi, & Kulik,
2024) extends STSF with more randomness, and builds a single design matrix used to
train an extremely randomized trees model (Geurts, Ernst, & Wehenkel, 2006).
The Random Interval Spectral Ensemble (RISE) (Flynn, Large, & Bagnall, 2019)
is similar to TSF, but was designed for tackling audio problems, and thus computes
spectral features (periodogram and auto-regression), which are known to be discrimi-
natory for such problems, instead of time-domain features. Contrary to TSF, a single
interval is randomly selected for each tree instead of several ones.
The Canonical Interval Forest (CIF) algorithm (Middlehurst, Large, & Bagnall,
2020) is another extension of TSF with more features being extracted. In addition
to the three features of TSF, the 22 Catch22 features (Lubba et al., 2019) are also
included. An ensemble of trees is built on top of the extracted features. Additional
diversity is obtained by considering only a subset of the 25 features for each tree,
similarly to what is done in a random forest (Breiman, 2001). The Diverse Represen-
tation Canonical Interval Forest (DrCIF) algorithm (Middlehurst et al., 2021) extends
CIF with two additional time series representations: periodograms and first-order
differences.
2.3 Quant
Quant (Dempster et al., 2024) is an interval-based method with a transformation
step followed by a classification step. The classification algorithm used is extremely
randomized trees (Geurts et al., 2006). Two other algorithms were also investigated in
the original publication: random forests (Breiman, 2001) and Ridge (Hoerl & Kennard,
7

1970). For the rest of this section, we focus on the transformation step of Quant. More
generally, we use the termQuantfor both the transformation step and the pipeline
of the transformation and classification steps, with the context implicitly indicating
which one.
Quant is an interval-based method with the following characteristics:
• It uses four distinct representations of the time series: the raw representation,
the (smoothed) first-order difference, the second-order difference, and the discrete
Fourier transform (in practice, the magnitudes of the complex Fourier coefficients).
• It derives fixed dyadic intervals at several levels. Starting from any representation
of the whole series, the whole series is considered, then the first half and the second
half of the whole series are considered, then the four quarters of the whole series
are considered, etc. We call these intervals the base intervals. Moreover, Quant also
includes shifted intervals for any level excluding the first one, with the shift being
equal to half the interval length. Thedepth, that is the number of levels that are
considered, and denoted byd, is a hyperparameter of Quant, and its default value
isd= 6. Figure 1 illustrates the set of intervals considered by Quant.
• The descriptive statistics computed are quantiles. Instead of using a fixed number
of quantiles per interval, which would be independent of the interval length, Quant
defines aquantile divisorsuch that the number of quantiles is proportional to the
interval length. Denoting bymthe length of any interval andνthe quantile divi-
sor, Quant computesk=m/νevenly-spaced quantiles from the minimum to the
maximum, that is the (0,1/(k−1), . . . ,(k−2)/(k−1),1) quantiles, per interval.
• The interval mean is subtracted to every other quantile. The intuition is that the
extracted features (that is, the quantiles) represent both the distribution of the val-
ues in the interval and the distribution of values in the interval relative to the mean.
Figure 2 illustrates the quantiles extracted by Quant. This idea has already been
used in other families of time series classification algorithms, notably in dictionary-
based methods where the subseries are often normalized in order to consider the
relative (to the interval) values of the subseries instead of the absolute values.
In practice, there are a few more subtleties, and we believe that it is important to
mention them:
• The four representations of a series do not have the same length. Iflis the length
of the raw representation, then the lengths of the (smoothed) first-order difference,
the second-order difference and the discrete Fourier transform arel−1,l−2, and
⌊l/2⌋+ 1 respectively, where⌊·⌋is the floor function.
• The first-order difference is smoothed with a length-5 centered moving average,
applied after padding both ends of the differenced series by 2 using edge-value
(replicate) padding, which restores its original (post-differencing) length.
• The depth of Quant is capped by the series length. Indeed, it would be impossible
to split a subseries of length 1. In practice, if⌊log 2(l)⌋< d−1, then the value of
the depth that is used is⌊log 2(l)⌋+ 1, and otherwise the provideddvalue is used.
In the general case, the value of the depth used is thus:
e= min (d,⌊log 2(l)⌋+ 1 )
8

2385
1 3
quant: a minimalist interval method for time series…
shifted by half the interval length. In the context of the tradeoff between distribution
information and location information discussed in Sect.  1, the inclusion of shifted
intervals allows us to recover location information otherwise discarded by dyadic
intervals, i.e., by capturing the distribution of the values in the ‘middle’ 50% of a
region otherwise divided into ‘left’ and ‘right’ halves.
Accordingly, the total number of intervals is 2d−1 × 4 − 2 − d for each input
representation. By default, we use a depth of d = min(6, ⌊log2 n⌋ + 1) , meaning
that there are 120 intervals per representation (for time series of length 32 or
more), and the smallest intervals are of length max(1, n ∕ 32).
As noted above, we set the number of quantiles as a proportion of interval length.
As a result, the total number of features is always proportional to time series length.
For example, for a time series of length n = 64 , if we split the time series into four
intervals of length m = n ∕ 4 = 64 ∕ 4 = 16 , and we compute m ∕ 4 = 16 ∕ 4 = 4
quantiles per interval, we produce a total of 16 features: 4 quantiles per interval for
each of 4 intervals equates to a total of 16 features. If, instead, we were to split
the same series into 8 intervals of length m = n ∕ 8 = 64 ∕ 8 = 8 , we would compute
m ∕ 4 = 8 ∕ 4 = 2 quantiles per interval producing, again, a total of 16 features: 2
quantiles per interval for each of 8 intervals equates to a total of 16 features. Includ-
ing the shifted intervals approximately doubles the total number of features.
3.3  Features
The sorted values represent the empirical distribution of values in each interval.
As noted above, using the sorted values as features allows us to capture the distri-
bution of the values in each interval directly, and use that information as the basis
for classification.
Quantiles, being a subsample of the sorted values, represent an approximation
of the full set of values, that is, an approximation of the empirical distribution.
Importantly, this approximation reduces the size of the feature space which, in turn,
reduces computational complexity (in particular, in relation to classifier training).
As noted above, we define the number of quantiles per interval in proportion to
interval length. We compute k = m ∕ v evenly-spaced quantiles per interval in the
range (0∕(k − 1),1 ∕(k − 1), ..., (k − 1)∕(k − 1)) , where m is interval length and, by
default, v = 4 . (For intervals of length one, we simply use the given value. Where
Fig. 3  An illustration of the set
of intervals for a depth of d = 4 ,
including ‘shifted’ intervals for
d > 1
r
 = 0
r
 = 1
r
 = 1
 (shift)
r
 = 2
r
 = 2
 (shift)
r
 = 3
r
 = 3
 (shift)
l
l
l
l
Fig. 1: Illustration of the set of intervals that are considered by Quant. In this example,
the value of the depth isd= 4. For every levelr∈ {0, . . . , d−1}, base intervals of
lengthl·2 −r are considered. For every levelr∈ {1, . . . , d−1}, shifted intervals of
lengthl·2 −r are considered, with the shift being equal to half the interval length (that
is,l·2 −r−1). The figure is adapted from (Dempster et al., 2024) and the corresponding
author has allowed its reuse.
2386 A. Dempster et al.
1 3
m ∕ v ≤ 1 , we use the median.) So, for example, for an interval of length m = 16 , by
default we take m ∕ v = 16∕4 = 4 quantiles from this interval. Taking m ∕ v quan-
tiles is essentially equivalent to sorting the m values in the interval and keeping only
every vth value. (We note, however, that strictly speaking, it is not necessary to sort
all of the values in an interval in order to compute the quantiles.) Taking m quantiles
per interval (i.e., v = 1 ) is equivalent to using the sorted values directly (i.e., not
subsampling).
Broadly speaking, we find that accuracy increases as the number of quantiles per
interval increases, although the actual differences in accuracy are small, and com-
puting more quantiles per interval results in proportionally higher computational
cost: see Sect. 4.2.1.
We find that it is beneficial, to subtract the interval mean (that is, the mean of all
of the values in the interval) from every second quantile: see Fig.  4. Subtracting the
mean from every second quantile allows for capturing both the ‘raw’ distribution of
values and the ‘shape’ of the distribution (i.e., divorced from mean of the values in a
given interval). (Note that we only subtract the mean where both the interval length,
and the number of quantiles per interval, are greater than or equal to two.) Although
there are multiple potential approaches to integrating this information into the fea-
tures, we find that it is efficient and effective to simply subtract the interval mean
from every second quantile. The advantage of this approach is that it has no effect on
the total number of features. Note, however, that the effect of subtracting the mean
from half of the quantiles versus not subtracting the mean is relatively small: see
Sect. 4.2.3.
3.4  Classifier
We use extremely randomised trees (Geurts et al. 2006), as per rSTSF (Cabello et al.
2023). The key distinctions with random forests are that extremely randomised trees
do not use bagging, and extremely randomised trees consider a random split point
for each candidate feature. (We demonstrate the differences in accuracy between
using extremely randomised trees versus a random forest and a ridge regression
classifier in Sect. 4.2.4.)
Interval methods can potentially produce a large number of features, depending
on the number of input representations, the number of intervals, and the number of
features per interval. For extremely randomised trees, the typical ‘default’ number of
Fig. 4  An illustration of quantiles drawn from intervals of length n ∕ 4 . We subtract the interval mean
from every second quantile, such that we compute features representing both the distribution of the val-
ues in the interval and the distribution of the values in the interval relative to the mean
Fig. 2: Illustration of the quantiles derived by Quant. This example has 4 intervals,
corresponding to the base intervals at the dyadic levelr= 2. Quantiles are (possibly
interpolated) values of the intervals. Every other quantile is centered, which is illus-
trated by the color of the dots: blue dots represent raw quantiles, while orange dots
represent centered quantiles. Raw quantiles quantify the distribution of the absolute
values in the interval, while centered quantiles quantify the distribution of the relative
values in the interval. The figure is from (Dempster et al., 2024) and the corresponding
author has allowed its reuse.
9

Ford= 6, it means that the series of lengthl <32 have fewer than 6 dyadic levels.
• All the intervals of any levelr∈ {1, . . . , e−1}are not exactly equal-sized, unlessl
is exactly divisible by 2 r. Given the implementation chosen in Quant, the lengths
of any two intervals of the same level differ by at most±1. Letq r ands r be the
quotient and the remainder of the Euclidean division oflby 2 r respectively:
qr =⌊l·2 −r⌋ands r =l−q r ·2 r
There are exactly 2 r −s r intervals of lengthq r ands r intervals of lengthq r + 1.
• The exact value for the shift of the shifted intervals of any levelr∈ {1, . . . , e−1}
is⌈l·2 −r−1⌉.
• At the last levelr=e−1, shifted intervals are included if and only if the median
of the base interval lengths of this level is greater than 1, which is equivalent to
l≥1.5·2 e−1.
• There are three different cases (two edge cases and the normal case) to compute the
quantiles:
1. If a subseries is of lengthm= 1, the single value of the subseries is returned.
2. If a subseries is of lengthmlarger than 1 and lower than or equal to the quantile
divisorν, that is 1< m≤ν, then only the median is computed (and no centering
is performed).
3. Otherwise, the actual number of quantiles is equal to 1 +⌊(m−1)/ν⌋. However,
in the general case, the quantiles are not exact values from the subseries. For
instance, consider a subseries of length 11. If the number of quantiles is equal
to 5, the three quartiles would correspond to the following indices (using zero-
based numbering) of the sorted values: 2.5, 5, and 7.5. However, two indices are
not integers (2.5 and 7.5). When an index is not an integer, linear interpolation
is performed between the lower and upper bounds.
3 Limitations of Quant’s reference implementation
Quant’s reference implementation2 is written in Python and commits to a single, fixed
computational structure for extracting interval quantiles. First, given the length of
each time seriesland the maximum depthd, the fixed endpoints of all the intervals
are computed (not shown). Each interval issues one call to the f_quantilefunction,
which invokes the torch.quantilefunction on the entire batch of time series at once,
as illustrated in 1. This process is repeated for all the intervals using a for loop (over
all the intervals), as illustrated in 2.
This implementation has an obvious utility for researchers: it is extremely simple
(very few lines of code) and easily readable. Nonetheless, it might not be optimal in
practice. Indeed, this design amortizes the cost of every quantile computation across
the full batch of samples, and is a natural choice for a tensor library built around
batched, hardware-accelerated execution such as graphical processing units (GPU).
On CPU, however, this single fixed structure exposes two distinct inefficiencies at
2https://github.com/angus924/quant
10

Listing 1Simplified version of the f_quantilesPython function used to compute the
quantiles for all the samples for a given interval in Quant’s reference implementation.
def f_quantiles(X, div=4):
m = X.shape[-1]# m is the interval width
num_quantiles = 1 + (m - 1) // div# Number of quantiles computed
if num_quantiles == 1:# If a single quantile is computed
# Compute the median
quantiles = X.quantile(torch.tensor([0.5]), dim=-1)
else:# If several quantiles are computed
# Compute the quantiles for the base intervals
quantiles = X.quantile(torch.linspace(0, 1, num_quantiles), dim=-1)
# Center every other quantile
quantiles[..., 1::2] = quantiles[..., 1::2] - X.mean(-1)
return quantiles
Listing 2Simplified version of the for loop, over the intervals, used to compute the
quantiles for all the samples and all the intervals in Quant’s reference implementation.
features = []# Instantiate an empty list
for a, b in intervals:# For each interval
# Compute the quantiles for this interval
features.append(f_quantile(X[..., a:b], div = self.div))
# Concatenate all the quantiles into a single tensor
features = torch.cat(features, -1)
opposite ends of the series-length spectrum, both of which stem from the same root
cause: the number of torch.quantileinvocations is fixed by the total number of
intervals (which is bounded by the value ofdin practice), independent of how much
actual numerical work each invocation performs.
For short series, interval widths are small, so each torch.quantilecall does very
little genuine sorting and interpolation work. What dominates instead is the fixed,
per-call cost of going through PyTorch’s dispatcher. This overhead is paid once per
interval, regardless of interval width, and is largely unavoidable within PyTorch’s
general-purpose tensor-operation model.
For long series, the opposite failure mode appears. For the first depth level, the
quantiles for the whole time series are computed. The torch.quantilefunction sorts
the input to compute the quantiles. This sorting operation has anO(l·logl) cost just
to sort the whole time series. This cost does not even include sorting all the subseries
extracted.
Quant’s fixed structure is not well-matched to either extreme of time series length
by design: it always pays per-call dispatch overhead proportional to the total number
of intervals (which is the predominant term for short series), and always pays a total
11

sort cost (which is the predominant term for long series), with no mechanism to trade
one off against the other.
We propose two distinct solutions to improve the runtimes of Quant in both settings
(short and long series). But first, we provide an analysis of the theoretical complexity
of processing a single time series.
4 Complexity of processing a single series
In this section, we investigate the theoretical complexity of processing a single time
series. First, we focus on the processing of only the raw series. Then, we explain how
to generalize the results for the whole processing, which includes the four different rep-
resentations of the series. For any given representation, there are two dominant terms
in the processing: sorting the values in each interval and extracting the interpolated
(and possibly centered) quantiles from the sorted values in each interval. To keep the
main text focused on the results themselves, the proofs of every theorem and lemma
in this section, as well as in Section 5 and Section 6, are deferred to Appendix A.
4.1 Processing the raw series
4.1.1 Preliminary results
Before diving into the total cost of both dominant terms, we provide preliminary
results about the number of intervals derived by Quant (Theorem 1), the total width
of all these intervals (Theorem 2), the total number of quantiles extracted by Quant
(Theorem 3 and Theorem 4), and the number of length-one intervals (Theorem 5).
Theorem 1(Number of intervals)For any series lengthland any depthd, definek=
min(d−1,⌊log 2(l)⌋). The total number of intervals that Quant builds, denoted byN i(l, d), is
equal to:
Ni(l, d) :=
(
2k+2 −k−3ifl≥1.5·2 k
3·2 k −k−2ifl <1.5·2 k = Θ

2k

ProofSee the proof of Theorem 1 on page 57 of Appendix A.□
Theorem 2(Total width)For any series lengthland any depthd, definek= min(d−
1,⌊log 2(l)⌋). The total width, that is the sum of the widths of all the base and shifted intervals,
and denoted byW(l, d), is equal to:
W(l, d) :=




2k+ 2 −k

·l−
kX
r=1
l
l·2 −r
m
−l·2 −r

ifl≥1.5·2 k

2k−1 + 2 −(k−1)

·l−
k−1X
r=1
l
l·2 −r
m
−l·2 −r

ifl <1.5·2 k
= Θ (k·l)
ProofSee the proof of Theorem 2 on page 57 of Appendix A.□
12

Theorem 3(Total number of quantiles)Let{x}be the fractional part of any positive real
numberx, that is{x}=x− ⌊x⌋with0≤ {x}<1. For any series lengthl, any depthd, and
any quantile divisorν, the total number of quantiles, denoted byN q(l, d, ν), is equal to:
Nq(l, d, ν) :=Ni(l, d) +W(l, d)−N i(l, d) ν − X j  mj −1 ν 
with the sum being over all the base and shifted intervals andm j being the width of thej-th
interval.
ProofSee the proof of Theorem 3 on page 58 of Appendix A.□
We denote byE(l, d, ν) the residual term in the formula ofN q(l, d, ν):
E(l, d, ν) :=
X
j
 mj −1
ν

≥0
The residual termE(l, d, ν) is always non-zero (except in trivial settings), but a simple
bound can be derived. We state these results in Theorem 4.
Theorem 4(Value of the residual term)Forν= 1, and for anylandd, the residual term
E(l, d, ν)is always zero. Ford= 1, the residual term is zero if and only ifl−1is exactly
divisible byν. For anyd≥2andν≥2, and for anyl, the residual termE(l, d, ν)is always
non-zero, is bounded by ν−1 ν ·N i(l, d), with the bound being attained for anylbeing exactly
divisible by2 d−1 ·ν.
ProofSee the proof of Theorem 4 on page 58 of Appendix A.□
Among the intervals counted by Theorem 1, those of width 1 play no role in the
sort and extraction costs studied later in this section: sorting a single value is a no-
op, and no quantile is interpolated from it (the value is simply copied). Theorem 5
counts these width-1 intervals exactly, which lets the extraction-cost results in this
section (Theorem 9, Theorem 16 and their approximate-algorithm counterparts) be
stated exactly, rather than as small-series approximations.
Theorem 5(Number of length-one intervals)For any series lengthland any depthd, define
k= min(d−1,⌊log 2(l)⌋). The number of intervals of width1that Quant builds, denoted by
N (1) i (l, d), is equal to:
N (1) i (l, d) :=



0ifk=d−1<⌊log 2(l)⌋
2k+1 −lifk=⌊log 2(l)⌋andl <1.5·2 k
2·

2k+1 −l  ifk=⌊log 2(l)⌋andl≥1.5·2 k
Consequently, denoting byN >1 i (l, d) :=N i(l, d)−N (1) i (l, d)the number of intervals of
width strictly greater than1, and byW >1(l, d) :=W(l, d)−N (1) i (l, d)andN >1q (l, d, ν) :=
13

Nq(l, d, ν)−N(1) i (l, d)the total width and total number of quantiles restricted to those inter-
vals, all three quantities are fully determined by Theorem 1, Theorem 2, Theorem 3 and
N (1) i (l, d): each width-1interval contributes exactly1toW(l, d)(its own width) and exactly
nq(1, ν) = 1toN q(l, d, ν)(Theorem 3’s proof ), so subtractingN(1) i (l, d)removes exactly their
contribution from each.
ProofSee the proof of Theorem 5 on page 59 of Appendix A.□
4.1.2 T otal sort
In order to compute the total sort cost, we start with the ideal case in which the series
lengthlis exactly divisible by the maximum factor 2 k, making all the intervals of each
level have the exact same length. The results are provided in Theorem 6. We provide
a generalization for any arbitrary series lengthlin Theorem 7. We finally provide the
computational complexity of the total sort in Theorem 8.
Theorem 6(Total sort cost forlexactly divisible by 2 k)For any series lengthland any
depthd, definek= min(d−1,⌊log 2(l)⌋). Iflis exactly divisible by2 k, under the sort-cost
accounting where an interval of sizemcostsm·log 2(m), the total cost of sorting all the
intervals that Quant builds for the raw representation of one series is:
T r∗ s (l, d) :=c1 ·l· h 2k+ 2 −k  ·log 2(l)−  k2 +k−2 + (k+ 2)·2 −k i
withc 1 being the empirical time-per-unit-of-sort-work constant (in seconds), which is positive
and hardware-specific.
ProofSee the proof of Theorem 6 on page 59 of Appendix A.□
Theorem 7(Total sort cost for arbitraryl)For any series lengthland any depthd, define
k= min(d−1,⌊log 2(l)⌋). Under the sort-cost accounting where an interval of sizemcostsm·
log2(m), the total cost of sorting all the intervals that Quant builds for the raw representation
of one series is:
T r s (l, d) :=c1·l· h 2k+ 2 −k  ·log 2(l)−  k2 +k−2 + (k+ 2)·2 −k i +O  2k  +O(k·log(l))
ProofSee the proof of Theorem 7 on page 60 of Appendix A.□
Theorem 8(Computational complexity of the total sort)For any series lengthland any
depthd, definee= min(d,⌊log 2(l)⌋+ 1). Under the sort-cost accounting where an interval of
sizemcostsm·log 2(m), the computational complexity of sorting all the intervals that Quant
builds for one series is:
T r s (l, d) = Θ (l·e·log(l))
14

Equivalently, splitting by which term wins in the minimum in the formula ofe:
T r s (l, d) =
(
Θ (d·l·log(l)) ifl≥2 d−1 (saturated regime)
Θ

l·(log(l)) 2

ifl <2 d−1 (unsaturated regime)
ProofSee the proof of Theorem 8 on page 62 of Appendix A.□
4.1.3 T otal extraction
We now provide the results about the total extraction cost. The general results are
stated in Theorem 9. We finally provide the computational complexity of the total
extraction in Theorem 10.
Theorem 9(Total extraction cost)The total extraction cost for the raw representation of
a single series of lengthl, denoted byT re (l, d, ν), is:
T r e (l, d, ν) :=c2 ·N >1 q (l, d, ν) +c3 ·W >1(l, d)
withN >1q (l, d, ν)andW>1(l, d)as defined in Theorem 5,c 2 being the empirical per-quantile
extraction cost (in seconds/quantile), andc 3 being the empirical per-element extraction cost
(in seconds/element), both constants being positive and hardware-specific.
ProofSee the proof of Theorem 9 on page 63 of Appendix A.□
Theorem 10For any series lengthl, any depthd, definee= min(d,⌊log 2 l⌋+ 1). For any
positive integerν(even as a function oflandd), the computational complexity of the total
extraction for one series does not depend onνand is equal to:
T r e (l, d, ν) = Θ(e·l)
Equivalently, splitting by which term wins in the minimum in the formula ofe:
T r e (l, d, ν) =
(
Θ(d·l) ifl≥2 d−1 (saturated regime)
Θ(l·log(l)) ifl <2 d−1 (unsaturated regime)
ProofSee the proof of Theorem 10 on page 63 of Appendix A.□
4.1.4 T otal processing cost
We first state, in Lemma 1, the decomposition of the total processing cost into the total
sort cost and the total extraction cost. This assumption was implicit since the start
of this section, but we make it explicit here so that it can be cross-referenced directly.
We then provide the computational complexity of the total processing in Theorem 11.
Lemma 1(Total processing cost decomposition)For any series lengthl, depthd, and quan-
tile divisorν, the total processing cost for the raw representation of a single series is the sum
of the total sort cost and the total extraction cost:
T r(l, d, ν) =Tr s (l, d) +Tr e (l, d, ν)
15

ProofSee the proof of Lemma 1 on page 64 of Appendix A.□
Theorem 11(Computational complexity of the total processing)For any series lengthl,
any depthd, and any quantile divisorν, under the sort-cost accounting where an interval
of sizemcostsm·log 2(m), the computational complexity of Quant’s processing of the raw
representation of a single series is:
T r(l, d, ν) =
(
Θ (d·l·log(l)) ifl≥2 d−1 (saturated regime)
Θ

l·(log(l)) 2

ifl <2 d−1 (unsaturated regime)
ProofSee the proof of Theorem 11 on page 64 of Appendix A.□
4.1.5 Simplified expressions with more assumptions
All the results presented above are general, for any value ofdandν. Quant has default
values for both its hyperparameters: the depth is equal to 6 (d= 6) and the quantile
divisor is equal to 4 (ν= 4). These default values were used on all the data sets in
the main experiments presented in (Dempster et al., 2024). In the rest of this section,
we fix the values of both hyperparameters to their default values. We only consider
the saturated regime, which is attained for any series lengthl≥32, and also implies
thatk=d−1 = 5. Indeed, 32 is a small value for series length, and one of the main
advantages of Quant is to be fast, especially for long series. Finally, to simplify the
formulae even further, we assume the series length to be a power of 2, that isl= 2 b
withb≥5 being an integer.
With these assumptions, we provide the simplified exact formulae for the total sort
cost, the total extraction cost, and the total processing cost for the raw representation
of a single series, in Theorem 12, Theorem 13, and Theorem 14 respectively. They
illustrate how the theoretical costs provided in Theorem 6, Theorem 7, and Theorem 9
can be turned into concrete runtimes.
Theorem 12(Total sort cost)Assuming thatd= 6, andl= 2 b for any positive integerb
greater than or equal to5, the exact formula for the total sort cost simplifies to:
T r s

2b,6  = 3·c 1 ·2 b−5 ·(107·b−301)
ProofSee the proof of Theorem 12 on page 65 of Appendix A.□
Theorem 13(Total extraction cost)Assuming thatd= 6,ν= 4andl= 2 b for any positive
integerbgreater than or equal to5, the exact formula for the total extraction cost simplifies
to:
T r e

2b,6,4  =



80·c 2 + 258·c 3 ifb= 5
192·c 2 + 642·c 3 ifb= 6
321·

2b−7 ·c 2 + 2b−5 ·c 3

ifb≥7
16

ProofSee the proof of Theorem 13 on page 65 of Appendix A.□
Theorem 14(Total processing cost)Assuming thatd= 6,ν= 4andl= 2 b for any positive
integerbgreater than or equal to5, the exact formula for the total processing cost simplifies
to:
T r

2b,6,4  =



702·c 1 + 80·c 2 + 258·c 3 ifb= 5
2046·c 1 + 192·c 2 + 642·c 3 ifb= 6
2(b−5) ·

3·c 1 ·(107·b−301) + 321 4 ·c 2 + 321·c 3

ifb≥7
ProofSee the proof of Theorem 14 on page 66 of Appendix A.□
4.2 Generalizing to the four representations
So far, every result in this section has been stated for the raw representation of a
single series. Quant actually extracts features from four representations of each series:
the raw series itself, a smoothed first-order difference, the second-order difference,
and the magnitude of the real discrete Fourier transform, processed independently
and sequentially. We now generalize Theorem 1 through Theorem 14 to the total cost
across all four representations.
Lemma 2(Representation lengths)For a raw series of lengthl≥3, index Quant’s four
representations byp∈ {1,2,3,4}(raw, smoothed first-difference, second-difference, and FFT-
magnitude, respectively), and denote byl p(l)the length of representationp. Then:
l1(l) =l, l 2(l) =l−1, l 3(l) =l−2, l 4(l) =
 l
2

+ 1
ProofSee the proof of Lemma 2 on page 66 of Appendix A.□
Remark 1None of Theorem 1 through Theorem 11 use any property of the raw series beyond
its lengthl: the “r” superscript onT rs ,T re , andT r is bookkeeping (indicating that these results
were first stated for the raw representation), not a restriction on what the results apply to.
Every one of those results holds, unchanged, for any single sequence that Quant partitions into
intervals via the same depth-d, divisor-νprocedure and processes by sorting and extracting
quantiles. In particular, for each of the other three representations, we just have to replace this
representation’s own lengthl p(l) in place ofl. Moreover, because the same sort-then-extract
kernel processes every representation (only the input array differs), the hardware constants
c1,c 2,c 3 are shared across all four representations: they are not representation-specific, unlike
the implementation-specific constants introduced in Theorem 19 and Theorem 20.
Theorem 15(Total sort cost across all four representations)For any series lengthl≥3
and depthd, under the sort-cost accounting where an interval of sizemcostsm·log 2(m),
17

the total cost of sorting all the intervals that Quant builds across all four representations of
one series is:
Ts(l, d) =
4X
p=1
T rp s (lp(l), d)
with each term given by Theorem 7 (applied, per Lemma 2 and Remark 1, withlreplaced by
lp(l)).
ProofSee the proof of Theorem 15 on page 66 of Appendix A.□
Theorem 16(Total extraction cost across all four representations)For any series length
l≥3, depthd, and quantile divisorν, the total extraction cost across all four representations
of one series is:
Te(l, d, ν) =
4X
p=1
T rp e (lp(l), d, ν) =c2 ·
4X
p=1
N >1 q (lp(l), d, ν) +c3 ·
4X
p=1
W >1 (lp(l), d)
withN >1q (lp(l), d, ν)andW>1(lp(l), d)exactly given by Theorem 5, evaluated atl p(l).
ProofSee the proof of Theorem 16 on page 67 of Appendix A.□
Theorem 17(Total processing cost across all four representations)For any series length
l≥3, depthd, and quantile divisorν, the total processing cost across all four representations
of one series is:
T(l, d, ν) =Ts(l, d) +Te(l, d, ν)
ProofSee the proof of Theorem 17 on page 67 of Appendix A.□
Theorem 18(Computational complexity of the total, across all four representations)For
any series lengthland depthd, definee= min(d,⌊log 2(l)⌋+ 1)as in Theorem 8 and
Theorem 10. Then, for any positiveν:
Ts(l, d) = Θ(l·e·log(l)), T e(l, d, ν) = Θ(e·l), T(l, d, ν) = Θ(l·e·log(l))
Equivalently:
T(l, d, ν) =
(
Θ (d·l·log(l)) ifl≥2 d−1 (saturated regime)
Θ

l·(log(l)) 2

ifl <2 d−1 (unsaturated regime)
i.e., summing across all four representations does not change the complexity class obtained
for the raw representation alone in Theorem 8, Theorem 10, and Theorem 11.
ProofSee the proof of Theorem 18 on page 67 of Appendix A.□
18

Remark 2Unlike the extraction cost (Theorem 16), which is exact for anylvia Theorem 2
and Theorem 3, the closed forms of Theorem 12, Theorem 13, and Theorem 14 rely onlbeing
exactly divisible by 2k (in particular, onl= 2 b in thed= 6, ν= 4 simplification). This holds
for the raw representation’s lengthl 1(l) =lby assumption, but generally fails for the other
three:l 2(l) = 2b −1 andl 4(l) = 2b−1 +1 are odd for everyb≥1, andl 3(l) = 2b −2, while even,
is not itself a power of two forb≥2. Consequently, even under the simplifying assumptions
of Theorem 12 through Theorem 14 (d= 6,ν= 4,l= 2 b), only the raw representation’s
contribution toT s(l, d),Te(l, d, ν), andT(l, d, ν) admits a closed form as clean as Theorem 12
through Theorem 14. The other three representations’ contributions are governed by the
fully general Theorem 7 (sort, with itsO(·) correction terms) and Theorem 9 (extraction,
exact but without the simplification of the residual termE(l, d, ν) available whenlis exactly
divisible by 2 k, used in deriving Theorem 12 through Theorem 14).
5 Making Quant faster for short series
Quant, applied to a data set ofnunivariate time series of lengthl, consists in process-
ing every (series, interval) ordered pair. We consider a sequential processing of this
data set, meaning that two nested for loops (one over all the series and one over all
the intervals) are required to process the whole data set. The question that remains
to be answered is: Which loop should be the outer loop? We analyze the computa-
tional complexities of both approaches to determine in which settings each approach
is optimal.
Before comparing each approach, we also make explicit an assumption that was
already implicit in Theorem 6 through Theorem 14: the constantsc 1,c 2, andc 3
were defined asempirical, hardware-specificconstants, and nothing in the proofs of
Theorem 7, Theorem 9, or Theorem 11 assumed a particular way of executing the
sort and extraction operations, as only thenumberof operations was counted. We
now make this dependence on the implementation explicit, and derive the total-cost
formula for a data set ofnseries for each of Quant’s two natural implementation
strategies.
The total cost of either strategy is linear (with an intercept, i.e., affine) in the
number of seriesn:
total cost = setup cost + (marginal cost×number of series)
As an analogy, one can think of baking cookies: there are constant (i.e., independent
of the number of cookies) costs such as preheating the oven, and there are marginal
(i.e., proportional to the number of cookies) costs such as making each cookie from
the dough and placing it on the baking sheet. Here, a cookie is a single series, and we
need to derive the setup cost (coming from the structure of the code) and the marginal
cost (processing a single series) of each strategy. As we show below, the two strategies
differ sharply in how much of their cost is genuinely a shared, amortizable setup cost.
To state the marginal cost of either strategy, it is convenient to name the sort-work
quantity that was left as an anonymous bracket expression in Theorem 7. We define:
Σ(l, d) :=l·

2k+ 2 −k ·log 2(l)−  k2 +k−2 + (k+ 2)·2 −k +O  2k +O (k·log(l) )
19

withk= min(d−1,⌊log 2(l)⌋), so that Theorem 7 readsT r s (l, d) =c 1 ·Σ(l, d). For
each implementation strategyv∈ {I, S}(interval-outer and series-outer, defined
below), we writec (v) 1 , c(v) 2 , c(v) 3 for that implementation’s own hardware-specific sort
and extraction constants, and define its per-series total processing cost as
T r,(v)(l, d, ν) :=c(v) 1 ·Σ(l, d) +c(v) 2 ·N >1 q (l, d, ν) +c(v) 3 ·W >1(l, d)
i.e., Lemma 1’s single-series total cost, evaluated with implementationv’s own
constants (N >1 q andW >1 as in Theorem 5, per Theorem 9).
5.1 Outer loop over the intervals
In Quant’s reference implementation, the outer loop is the loop over the intervals:
for each of theN i(l, d) intervals, a single vectorized (NumPy) call either sorts and
extracts quantiles from that interval (if its width is greater than 1) or directly copies
its single value (if its width is 1), across allnseries at once. We refer to this strategy
asinterval-outer, or version (I).
Theorem 19(Total cost of the interval-outer implementation)For any number of series
n≥1, series lengthl, depthd, and quantile divisorν, the total wall-clock cost of processing
the raw representation ofnseries with the interval-outer implementation is:
T r,(I)(n, l, d, ν) =N>1 i (l, d)·κ(I) (l) +n·T r,(I)(l, d, ν)
withN >1 i (l, d)as in Theorem 5, andκ (I) (l)≥0being the hardware-specific per-interval
overhead (the Python loop-iteration cost plus the NumPy call-dispatch cost of one vectorized
sort-and-extract call, in seconds), a positive constant for a givenl.
ProofSee the proof of Theorem 19 on page 67 of Appendix A.□
5.2 Outer loop over the series
The alternative strategy makes the outer loop the loop over thenseries: for each
series, a single compiled (Numba) call sorts and extracts quantiles from allN i(l, d)
intervals of that series internally, with no further Python-level looping. We refer to
this strategy asseries-outer, or version (S).
Theorem 20(Total cost of the series-outer implementation)For anyn≥1,l,d,ν, the
total wall-clock cost of processing the raw representation ofnseries with the series-outer
implementation is:
T r,(S)(n, l, d, ν) =n· h κ(S)(l) +T r,(S)(l, d, ν) i
withκ (S)(l)≥0being the hardware-specific per-series call-dispatch overhead (in seconds) of
invoking the compiled kernel at series lengthl, a positive constant for a givenl. Unlikeκ (I) (l),
which counts a dispatch call issued once per non-trivialinterval,κ (S)(l)counts a dispatch
call issued once perseries. We do not assume, a priori, that this quantity is independent of
l(see Remark 4 below).
20

ProofSee the proof of Theorem 20 on page 68 of Appendix A.□
Remark 3UnlikeT r,(I), the costT r,(S)(n, l, d, ν) is exactly proportional ton: the series-outer
implementation has no analogue of the interval-outer implementation’sn-independent setup
termN i(l, d)·κ (I) (l), because every series requires its own call-dispatch overheadκ (S)(l).
There is no cost shared, and thus amortizable, across series. Conversely, the interval-outer
implementation amortizes its per-interval dispatch overhead across allnseries at once, at the
cost of paying forN i(l, d) such dispatches regardless of how smallnis.
Remark 4(κ (S)(l) is not, empirically,l-independent) During our initial experiments, we
naturally treatedκ (S) as a single constant, independent oflandd, on the grounds that it
counts the dispatch overhead of a single compiled function call, unlikeκ (I) (l), which is paid
once per interval and therefore has an obvious reason to scale withl. Fittingκ (S) this way,
however, leaves a residual (observed minus predicted processing cost, divided out over the
four representations) that grows smoothly and monotonically withl, by roughly two orders of
magnitude across the fitting grid, withr 2 ≥0.999 at every individuall(thus a real trend, not
measurement noise). We therefore modelκ (S)(l) as depending onl, fit with the sameA−B/l
closed form used forκ (I) (l) (Section 7 and Section 8). The fit’s ownr 2 against this functional
form is low, consistent with a small, close-to-constant residual rather than a strong trend
of its own. This is different from the approximate algorithm’s case, discussed in Remark 12,
where the dependence onlis considerably stronger and this same functional form does not
fit well. A plausible source of this dependence is that invoking the compiled kernel is not, in
practice, a fixed-cost operation: it involves marshalling anl-dependent volume of data (the
input series and the output feature array) across the Python/compiled-code boundary, a cost
that the idealized “one dispatch, fixed overhead” argument of Theorem 20’s proof does not
account for. As withκ (I) (l)’s own closed-form fit, we caution against extrapolatingκ (S)(l)
far outside the interior of the series-length grid that it is fit on: a held-out check of this style
of fit shows degraded predictive accuracy near and beyond the grid’s boundary.
5.3 Comparing both approaches
Theorem 21(Crossover sample size, raw representation)For the raw representation
(Section 4) and anyl,d,ν, define the per-series marginal costsB I (l, d, ν) :=Tr,(I)(l, d, ν)
andB S(l, d, ν) :=κ(S)(l) +T r,(S)(l, d, ν), and the interval-outer setup costA I (l, d) :=
N >1 i (l, d)·κ(I) (l)(Theorem 5).
• IfB S(l, d, ν)≤BI (l, d, ν), thenTr,(S)(n, l, d, ν)≤Tr,(I)(n, l, d, ν)for everyn≥1:
the series-outer implementation is at least as fast for every sample size.
• IfB S(l, d, ν)> BI (l, d, ν), define the crossover sample size
n∗(l, d, ν) := AI (l, d) BS(l, d, ν)−BI (l, d, ν)
ThenT r,(S)(n, l, d, ν)< Tr,(I)(n, l, d, ν)forn < n∗(l, d, ν), andTr,(I)(n, l, d, ν)<
T r,(S)(n, l, d, ν)forn > n∗(l, d, ν).
21

In either case, the interval-outer implementation is only worth using oncenexceeds a thresh-
old that grows with the number of non-trivial intervalsN >1 i (l, d)(hence, other things equal,
withl). For a small enough data set, the series-outer implementation is never worse.
ProofSee the proof of Theorem 21 on page 68 of Appendix A.□
Remark 5Theorem 21 formalizes this section’s motivating question, for the raw representa-
tion in isolation. Whether the series-outer implementation is preferable foreverysample size,
or only up to a crossovern ∗(l, d, ν), is itself an empirical question. It depends on the sign
ofB S(l, d, ν)−BI (l, d, ν), i.e., on which implementation has the lower per-series marginal
cost once its own call-dispatch overhead is included. We estimateκ (I) (l),κ (S)(l), and the
version-specificc (v) 1 , c(v) 2 , c(v) 3 empirically in Section 7 and Section 8, and use Theorem 21 to
determine, for realistic values oflandν, which strategy Quant should use as a function of the
number of seriesn, and whether short series are better served by one strategy regardless ofn.
In practice, however, Quant processes four representations per series (Section 4), not
the raw representation alone, and Theorem 21 is deliberately not generalized to that set-
ting the way Theorem 33 generalizes its approximate-algorithm counterpart: composing a
four-representation crossover from Theorem 21 would require, for each representationp, its
own separately-fittedκ (I) (lp(l)), and anl-dependent quantity such asκ (I) (·) is compara-
tively hard to estimate reliably from a finite series-length grid, and unsafe to extrapolate
beyond it. Our reference implementation’s actual dispatch rule sidesteps this: rather than
composingκ (I) (lp(l)) representation by representation, it estimates a single, pooled, effec-
tivelyl-independent overhead directly from the wall-clock time of the full four-representation
call, fitted directly against measured runtimes rather than assembled from the theorem’s own
per-operation constants. Theorem 21’s crossover therefore serves in this article as an inde-
pendent theoretical cross-check of that practical heuristic’s soundness, not as the formula the
heuristic itself evaluates. This pooled overhead is fit once per (mode, depth, div) triple, at
the fixed depth and quantile divisor used throughout this article’s experiments (Section 7). It
is not portable to a differently configured instance without being refit, and, since Remark 4
shows the underlying per-series overhead genuinely varies withl, pooling it into a single scalar
is itself a simplification of the same kind Theorem 21 avoids by keepingκ (I) (l) explicit in
l. This is an intentional, practical trade-off, made for the reasons given above, and not an
oversight.
6 Making an approximate version of Quant for long
series using moment-based quantiles
Section 3 identified sorting as the dominant cost for long series, and Theorem 8 con-
firmed it: the total sort cost is Θ(d·l·log(l)) in the saturated regime, strictly worse
than linear inl. Section 5 addressed this without changing what Quant computes, only
how the computation is dispatched. In this section, we instead change the computa-
tion itself: we propose an approximate variant of Quant that replaces each interval’s
exact order statistics, which require sorting, with quantileestimatesobtained from
that interval’s first four moments via the Cornish-Fisher expansion, computed in a sin-
gle linear pass with no sorting at all. This trades exactness for asymptotic speed, and
22

is intended specifically for long series, where Theorem 8’s extra log(l) factor is most
costly and where a single long series already carries enough information for a moment-
based approximation to be reasonable. Whether the resulting approximation error is
acceptable in practice is an empirical question addressed in Section 7 and Section 8,
not in this section.
6.1 Background: moment-based quantile approximation
For a sample ofmreal values, define its raw central momentsM 2 = P i(xi − ¯x)2,
M3 = P i(xi − ¯x)3, andM 4 = P i(xi − ¯x)4, where ¯xis the sample mean. These,
together with ¯xitself andm, can be computed in a single pass over themvalues
using the Welford-Pebay online update. Maintaining running values ofm, ¯x,M 2,
M3,M 4, each new observation updates all five quantities using only the previous
running values and the new observation, with a fixed (i.e., independent ofm) number
of arithmetic operations per update. Unlike sorting, which requires the whole interval
to be available at once and whose cost per element grows with the interval’s size (an
interval of sizemcostsm·log 2(m), i.e. log2(m) per element, under the accounting used
in Section 4), this online update touches each element exactly once and performs the
same constant amount of work regardless ofmor of how many elements have already
been processed. We additionally track the running minimum and maximum alongside
the four moments, at the negligible extra cost of two comparisons per element.
From (m, M2, M3, M4), the sample variance, skewness, and excess kurtosis are
obtained via:
var = M2
m skew = M3/m std3 exkurt = M4/m var2 −3
with std = √var, each a fixed number of arithmetic operations, independent ofm.
The Cornish-Fisher expansion, introduced in (Cornish & Fisher, 1938) and given
its now-standard explicit form up to the fourth cumulant in (Fisher & Cornish, 1960),
approximates the quantile at probabilityq∈(0,1) of a distribution from estimates
of its mean, variance, skewness, and excess kurtosis, by adjusting the corresponding
standard normal quantile for the distribution’s departure from normality. Writing
z= Φ −1(q) for the standard normal quantile function evaluated atq(itself computed
via a fixed-cost rational approximation, independent ofmor ofq’s specific value
beyond selecting which of a small, constant number of branches of the approximation
to evaluate), the Cornish-Fisher approximation used in this study is:
w(z) :=z+ z2 −1 6 ·skew + z3 −3z 24 ·exkurt− 2z3 −5z 36 ·skew 2
bQ(q) := mean + std·w(z)
Bothw(z) and bQ(q) are, like Φ −1(q) itself, a fixed number of arithmetic operations,
independent ofm: once the moments of an interval are known, approximating any one
quantile from them costs the same, regardless of how large the interval is.
23

The expansion is undefined at the boundary probabilitiesq= 0 andq= 1 (where
Φ−1 is infinite), so Quant’s exact minimum and maximum are used directly at these
two positions instead, whenever they are requested. They are both already available
at no extra asymptotic cost, since they are computed in the same linear pass as
the moments. Only the strictly interior quantile positions of an interval’s requested
layout (i.e., every requested quantile except these two boundary ones, when present)
go through the Cornish-Fisher expansion.
Bothw(z) and bQ(q) above are obtained by formally inverting an Edgeworth
expansion of the distribution function, so the expansion’s classical error theory is
inherited from Edgeworth expansion theory. Hill and Davis (1968) generalized the
Cornish-Fisher expansion to arbitrary order and to limiting distributions other than
the normal, and gave the asymptotic order of the truncation error as a function of
the number of cumulant terms retained. This fourth-moment expansion such as the
one above is, in this classical framework, accurate up to a residual term that vanishes
as the underlying distribution approaches normality (equivalently, as its standard-
ized skewness and excess kurtosis approach zero). This classical theory assumes the
target distribution sits in a sequence approaching normality (as in a Central Limit
Theorem refinement), which is not guaranteed to hold for the empirical distribution
of an arbitrary interval’s raw values, as used here. Ulyanov, Aoshima, and Fujikoshi
(2016) instead derive genuinely non-asymptotic error bounds for the Cornish-Fisher
expansion, though still under regularity conditions on the target distribution (e.g., a
bounded density and finite higher moments) that we neither verify nor assume hold
for every interval in this study.
A further, well-documented deficiency of the truncated Cornish-Fisher expansion,
independent of the error-magnitude questions above, is that the approximate quan-
tile bQ(q) is not guaranteed to be monotonically increasing inqfor every combination
of skewness and excess kurtosis. Monotonicity only holds within a bounded region
of the (skewness, excess kurtosis) plane known as the expansion’sdomain of validity
(Jaschke, 2002; Maillard, 2020). Using the raw sample skewness and excess kurtosis
of a highly non-normal interval can, in principle, fall outside this region and yield a
non-monotonic (hence invalid, as a quantile function) approximation on that interval.
Maillard (2020) additionally warns against a related, purely practical pitfall: for small
samples, the skewness and excess kurtosisparametersplugged intow(z) are themselves
only estimates of the interval’s true skewness and excess kurtosis, and this estima-
tion error compounds with the expansion’s own truncation error. We do not check
membership in the domain of validity per interval in this study, and instead treat the
resulting approximation error, including any contribution from non-monotonicity, as
an empirical question, addressed alongside runtime in Section 7 and Section 8. Indeed,
doing so would add a per-interval cost beyond the fixed number of arithmetic opera-
tions counted in Subsection 6.2. Am´ ed´ ee-Manesme, Barth´ el´ emy, and Maillard (2019)
propose a corrected variant that re-estimates an effective skewness and excess kurtosis
via a response-surface method specifically to stay within the domain of validity and
reduce this source of error. We use the direct, uncorrected expansion of Subsection 6.1
throughout this study for its lower, stillO(1)-per-quantile cost, and leave adopting
such a correction to future work.
24

6.2 Complexity of processing a single series
The interval structure Quant builds, and the set of quantile positions requested from
each interval, do not depend on how each interval’s quantiles are actually computed:
Theorem 1 (N i(l, d), the number of intervals), Theorem 2 (W(l, d), the total width),
and Theorem 3 (N q(l, d, ν), the total number of quantiles) therefore apply unchanged
to the approximate algorithm of this section. What changes is only how each inter-
val’s contribution to the total cost is computed: a linear moment pass instead of a
sort, and a Cornish-Fisher evaluation instead of an interpolation from sorted values.
We mark every cost quantity specific to the approximate algorithm with a tilde, to
distinguish it from its exact-algorithm counterpart of Section 4 (e.g. eT r versusT r),
and introduce three new hardware-specific constants, ˜c1, ˜c2, ˜c3, playing the same role
for the approximate algorithm thatc 1, c2, c3 played for the exact one.
6.2.1 T otal moment computation cost
Theorem 22(Total moment computation cost)For any series lengthland depthd, under
the moment-cost accounting where an interval of sizemcosts exactlym(i.e.,log 2(m)replaced
by1, relative to the sort-cost accounting of Theorem 6), the total cost of computing the
moments of allN i(l, d)intervals that Quant builds for the raw representation of one series
is exactly:
eT r m(l, d) := ˜c1 ·W(l, d)
with˜c1 being the empirical time-per-element moment-update constant (in seconds/element),
positive and hardware-specific.
ProofSee the proof of Theorem 22 on page 68 of Appendix A.□
Remark 6Unlike Theorem 7, Theorem 22 needs no separate treatment of the case wherel
is not exactly divisible by 2 k: the moment-cost accounting is exactly linear in each interval’s
width, with no analogue of sorting’s convexity (thef(m) =mlog 2(m) used in Theorem 7’s
proof is strictly convex, which is precisely what made rounding the interval widths to integers
costly to bound. The linear cost model of this section has no such curvature, so Theorem 2’s
exact closed form forW(l, d) transfers to eT rm(l, d) without any correction term at all).
Theorem 23(Computational complexity of the total moment computation)For any series
lengthland any depthd, definee= min(d,⌊log 2(l)⌋+ 1). Under the moment-cost accounting
of Theorem 22, the computational complexity of computing the moments of all the intervals
that Quant builds for one series is:
eT r m(l, d) = Θ(e·l)
Equivalently, splitting by which term wins in the minimum in the formula ofe:
eT r m(l, d) =
(
Θ(d·l) ifl≥2 d−1 (saturated regime)
Θ(l·log(l)) ifl <2 d−1 (unsaturated regime)
ProofSee the proof of Theorem 23 on page 68 of Appendix A.□
25

6.2.2 T otal extraction cost
Theorem 24(Total extraction cost, Cornish-Fisher)The total extraction cost for the raw
representation of a single series of lengthl, under the approximate (moment-based) algorithm,
denoted by eT re (l, d, ν), is:
eT r e (l, d, ν) := ˜c2 ·N >1 q (l, d, ν) + ˜c3 ·N i(l, d)
withN >1q as in Theorem 5,˜c2 being the empirical per-quantile Cornish-Fisher evaluation cost
(in seconds/quantile), and˜c3 being the empirical per-interval cost of converting an interval’s
raw moments into (variance, skewness, excess kurtosis) (in seconds/interval), both constants
being positive and hardware-specific.
ProofSee the proof of Theorem 24 on page 68 of Appendix A.□
Remark 7(˜c2 as an average cost) Every one of theN >1q (l, d, ν) quantile positions is charged
the same rate ˜c2 in Theorem 24, even though the (at most two, per non-trivial interval)
boundary positionsq= 0 andq= 1 use the interval’s already-known exact minimum/max-
imum rather than a genuine Cornish-Fisher evaluation (Subsection 6.1), and are therefore
strictly cheaper. ˜c2 is best read as an average per-quantile cost over this mix. Since the num-
ber of boundary positions is at most 2·N >1 i (l, d) =O(l), whileN >1q (l, d, ν) = Θ(l) or larger
(Theorem 10’s proof), this simplification changes the constant ˜c 2 but not the asymptotic
complexity derived in Theorem 25 below.
Theorem 25(Computational complexity of the total extraction, Cornish-Fisher)For any
series lengthl, any depthd, definee= min(d,⌊log 2(l)⌋+ 1). For any positive integerν(even
as a function oflandd), the computational complexity of the total (approximate) extraction
cost for one series does not depend onνand is equal to:
eT r e (l, d, ν) = Θ(e·l)
Equivalently, splitting by which term wins in the minimum in the formula ofe:
eT r e (l, d, ν) =
(
Θ(d·l) ifl≥2 d−1 (saturated regime)
Θ(l·log(l)) ifl <2 d−1 (unsaturated regime)
ProofSee the proof of Theorem 25 on page 69 of Appendix A.□
6.2.3 T otal processing cost
Lemma 3(Total processing cost decomposition, approximate algorithm)For any series
lengthl, depthd, and quantile divisorν, the total processing cost for the raw representation of
a single series, under the approximate algorithm, is the sum of the total moment computation
cost and the total extraction cost:
eT r(l, d, ν) =eT r m(l, d) +eT r e (l, d, ν)
ProofSee the proof of Lemma 3 on page 69 of Appendix A.□
26

Theorem 26(Computational complexity of the total processing, approximate algorithm)
For any series lengthl, any depthd, and any quantile divisorν, under the moment-
cost/Cornish-Fisher accounting of this section, the computational complexity of Quant’s
approximate processing of the raw representation of a single series is:
eT r(l, d, ν) =
(
Θ(d·l) ifl≥2 d−1 (saturated regime)
Θ(l·log(l)) ifl <2 d−1 (unsaturated regime)
ProofSee the proof of Theorem 26 on page 69 of Appendix A.□
Remark 8(Asymptotic speedup from moment-based quantiles) Combining Theorem 11
(exact algorithm) and Theorem 26 (approximate algorithm), for anyl, d, ν:
T r(l, d, ν)
eT r(l, d, ν) = Θ(log(l))
in both the saturated regime (Θ(d·l·log(l))/Θ(d·l)) and the unsaturated regime (Θ(l·
(log(l))2)/Θ(l·log(l))). In both regimes, the moment-based algorithm removes exactly one
factor of log(l) relative to the exact algorithm, and this speedup grows, without bound, as
lgrows. This is consistent with this section’s motivation (Section 3): the longer the series,
the more this trade-off favors the approximate algorithm, while for short series the result-
ing speedup is small in absolute terms and may not be worth its approximation error, an
orthogonal question addressed empirically in Section 7 and Section 8.
6.2.4 Generalizing to the four representations
So far, every result in this subsection has been stated for the raw representation of a
single series. As in Section 4, Quant applies the same moment-based procedure to all
four representations of a series (the raw series itself, the smoothed first-order difference,
the second-order difference, and the magnitude of the real discrete Fourier transform)
processed independently and sequentially, with representationp’s own lengthl p(l)
given by Lemma 2. We now generalize Theorem 22 through Theorem 26 to the total
cost across all four representations, mirroring Theorem 15 through Theorem 18.
Remark 9None of Theorem 22 through Theorem 26 use any property of the raw series beyond
its lengthl: exactly as for the exact algorithm (Remark 1), the “r” superscript on eT rm, eT re ,
and eT r is bookkeeping, not a restriction. Every one of those results holds, unchanged, for
any single sequence that Quant partitions into intervals via the same depth-d, divisor-νpro-
cedure and processes by computing moments and evaluating the Cornish-Fisher expansion.
In particular, for each of the other three representations, the only change is to use that rep-
resentation’s own lengthl p(l) in place ofl. The moment-based kernel is shared across all
four representations (only the input array differs), so the hardware constants ˜c 1, ˜c2, ˜c3 are
likewise shared, not representation-specific.
Theorem 27(Total moment computation cost across all four representations)For any series
lengthl≥3and depthd, the total cost of computing the moments of all the intervals that
27

Quant builds across all four representations of one series is:
eTm(l, d) =
4X
p=1
eT rp m (lp(l), d)
with each term given by Theorem 22 (applied, per Lemma 2 and Remark 9, withlreplaced
byl p(l)).
ProofSee the proof of Theorem 27 on page 69 of Appendix A.□
Theorem 28(Total extraction cost across all four representations, Cornish-Fisher)For any
series lengthl≥3, depthd, and quantile divisorν, the total extraction cost across all four
representations of one series is:
eTe(l, d, ν) =
4X
p=1
eT rp e (lp(l), d, ν) = ˜c2 ·
4X
p=1
N >1 q (lp(l), d, ν) + ˜c3 ·
4X
p=1
Ni (lp(l), d)
withN >1q (lp(l), d, ν)as in Theorem 5, andN i(lp(l), d)exactly given by Theorem 1, both
evaluated atl p(l).
ProofSee the proof of Theorem 28 on page 70 of Appendix A.□
Theorem 29(Total processing cost across all four representations, approximate algorithm)
For any series lengthl≥3, depthd, and quantile divisorν, the total processing cost across
all four representations of one series, under the approximate algorithm, is:
eT(l, d, ν) =eTm(l, d) +eTe(l, d, ν)
ProofSee the proof of Theorem 29 on page 70 of Appendix A.□
Theorem 30(Computational complexity of the total, across all four representations, approx-
imate algorithm)For any series lengthland depthd, definee= min(d,⌊log 2(l)⌋+ 1)as in
Theorem 23 and Theorem 25. Then, for any positiveν:
eTm(l, d) = Θ(e·l), eTe(l, d, ν) = Θ(e·l), eT(l, d, ν) = Θ(e·l)
Equivalently:
eT(l, d, ν) =
(
Θ(d·l) ifl≥2 d−1 (saturated regime)
Θ(l·log(l)) ifl <2 d−1 (unsaturated regime)
Summing across all four representations does not change the complexity class obtained for
the raw representation alone in Theorem 23, Theorem 25, and Theorem 26.
ProofSee the proof of Theorem 30 on page 70 of Appendix A.□
28

Remark 10(Asymptotic speedup from moment-based quantiles, across all four represen-
tations) Combining Theorem 18 (exact algorithm, four representations) and Theorem 30
(approximate algorithm, four representations), for anyl, d, ν:
T(l, d, ν)
eT(l, d, ν) = Θ(log(l))
in both regimes, exactly as in Remark 8 for the raw representation alone: summing across
all four representations preserves the single factor of log(l) that the moment-based algorithm
removes. Since Quant always processes all four representations of every series, this is the
practically relevant comparison, more so than Remark 8.
6.3 Outer loop over the intervals
As in Section 5 for the exact algorithm, the approximate algorithm admits two natural
implementations, differing in which loop (over the intervals or over thenseries) is the
outer one:
• a NumPy-vectorized implementation that dispatches one call per interval, processing
allnseries at once for a given representation (interval-outer, version (I)), and
• a compiled (Numba) implementation that dispatches one call per representation,
processing allnseries and all their intervals internally (series-outer, version (S)).
Both implementations process the four representations independently and sequen-
tially, exactly as in Theorem 27 through Theorem 30. We reuse Section 5’s total-cost
decomposition (a per-implementation setup cost, independent ofn, plus a per-
implementation marginal cost, proportional ton), applied to the approximate
algorithm’s own constants: forv∈ {I, S}, define the per-representation marginal cost
eT r,(v)(l, d, ν) :=˜c(v) 1 ·W(l, d) +˜c(v) 2 ·N >1 q (l, d, ν) +˜c(v) 3 ·N i(l, d)
(i.e., Lemma 3’s single-series, single-representation total cost, evaluated with imple-
mentationv’s own constants, withN >1 q as in Theorem 5: only the Cornish-Fisher
evaluation term excludes trivial intervals, since both the moment computation
(Theorem 22, using the inclusiveW(l, d)) and the moments-to-(variance, skewness,
excess kurtosis) conversion (using the inclusiveN i(l, d)) are dispatched as single calls
covering every interval, trivial or not, see Theorem 24), and the total marginal cost
across all four representations
eT (v) Σ (l, d, ν) :=
4X
p=1
eT r,(v) (lp(l), d, ν)
Theorem 31(Total cost of the interval-outer implementation, approximate algorithm, across
all four representations)For any number of seriesn≥1, series lengthl, depthd, and quantile
divisorν, the total wall-clock cost of processing all four representations ofnseries with the
interval-outer implementation of the approximate algorithm is:
eT (I) (n, l, d, ν) =
4X
p=1
N >1 i (lp(l), d)·˜κ(I) (lp(l)) +n· eT (I) Σ (l, d, ν)
29

withN >1 i as in Theorem 5, and˜κ (I) (l)≥0being the hardware-specific per-interval overhead
(the Python loop-iteration cost plus the NumPy call-dispatch cost of one vectorized Cornish-
Fisher extraction call, in seconds), a positive constant for a givenl.
ProofSee the proof of Theorem 31 on page 70 of Appendix A.□
6.4 Outer loop over the series
Theorem 32(Total cost of the series-outer implementation, approximate algorithm, across
all four representations)For anyn≥1,l,d,ν, the total wall-clock cost of processing all four
representations ofnseries with the series-outer implementation of the approximate algorithm
is:
eT (S)(n, l, d, ν) =n· h ˜κ(S) Σ (l) + eT (S) Σ (l, d, ν) i ,˜κ (S) Σ (l) := 4X
p=1
˜κ(S) (lp(l))
with˜κ(S)(l)≥0being the hardware-specific per-series, per-representation call-dispatch over-
head (in seconds) of invoking the compiled kernel on a representation of lengthl, a positive
constant for a givenl. As withκ (S)(l)(Section 5, Remark 4), we do not assume˜κ (S)(l)is
independent oflord(see Remark 12 below).
ProofSee the proof of Theorem 32 on page 70 of Appendix A.□
Remark 11As in Section 5, eT (S)(n, l, d, ν) is exactly proportional ton, with no analogue of
the interval-outer implementation’s amortizable,n-independent setup term P p N >1 i (lp(l), d)·
˜κ(I) (lp(l)): every series requires its own call-dispatch overhead ˜κ (S) Σ (l), paid once per rep-
resentation, under the series-outer implementation, while the interval-outer implementation
amortizes its per-interval dispatch overhead across allnseries at once.
Remark 12(˜κ (S)(l) is notl-independent, and does not converge to a constant) Unlike
the exact algorithm’sκ (S)(l) (Remark 4), the approximate algorithm’s four-representation
dispatch cost (Theorem 32) is proven, not merely conjectured by analogy from the raw-
representation case. Fitting the implied per-representation residual ˜κ(S)(l) against measured
runtimes shows that treating ˜κ(S) as a single constant does not hold empirically, and more
severely than for the exact algorithm: the residual grows smoothly withlby roughly two
orders of magnitude across the fitting grid and shows no sign of converging to a constant as
lgrows. Instead, it follows an empirical power law ˜κ (S)(l)≈A+C·l P , withP≈0.74, vali-
dated by leave-one-out cross-validation rather than in-sample fit alone (since it has one more
free parameter than theA−B/lform that continues to describeκ (S)(l) adequately): the
A−B/lform reachesr 2 ≈0.18 in-sample and≈0.10 under cross-validation on this residual,
againstr 2 ≈0.99 both in-sample and under cross-validation for the power law (Section 7
and Section 8). The exponentPhas no theoretical derivation offered here: we report it as
an empirical finding, not a new theorem, and state Theorem 32 above with ˜κ (S)(l) left as a
general function oflrather than asserting its independence froml. We flag two possible, non-
exclusive explanations, neither confirmed here. First, the same call-marshalling argument as
Remark 4, here compounded across four representations of differing lengths. Second, that
30

part of the truel-dependent moment-computation or Cornish-Fisher extraction cost (Sub-
section 6.2) is not fully captured by ˜c 1,˜c2,˜c3 and is instead absorbed into the residual this
fit labels ˜κ(S)(l).
6.5 Comparing both approaches
Theorem 33(Crossover sample size, approximate algorithm, across all four represen-
tations)For anyl,d,ν, define the per-series marginal costs eBI (l, d, ν) := eT (I) Σ (l, d, ν)
and eBS(l, d, ν) := ˜κ(S) Σ (l) + eT (S) Σ (l, d, ν), and the interval-outer setup cost eAI (l, d) :=P4
p=1 N >1 i (lp(l), d)·˜κ(I) (lp(l))(Theorem 5).
• If eBS(l, d, ν)≤eBI (l, d, ν), theneT (S)(n, l, d, ν)≤eT (I) (n, l, d, ν)for everyn≥1.
• If eBS(l, d, ν)>eBI (l, d, ν), define the crossover sample size
˜n∗(l, d, ν) := eAI (l, d) eBS(l, d, ν)−eBI (l, d, ν)
Then eT (S)(n, l, d, ν)<eT (I) (n, l, d, ν)forn < ˜n∗(l, d, ν), and eT (I) (n, l, d, ν)<
eT (S)(n, l, d, ν)forn >˜n∗(l, d, ν).
ProofSee the proof of Theorem 33 on page 71 of Appendix A.□
Remark 13As in Section 5, whether the series-outer implementation of the approximate
algorithm is preferable for every sample size, or only up to a crossover ˜n∗(l, d, ν), depends on
the sign of eBS(l, d, ν)−eBI (l, d, ν), itself an empirical question. We estimate ˜κ(I) (l), ˜κ(S)(l),
and the version-specific ˜c(v) 1 ,˜c(v) 2 ,˜c(v) 3 empirically in Section 7 and Section 8, alongside the
exact algorithm’s own constants, and use Theorem 33 together with Remark 10 to determine,
for realistic values ofl,n, andν, whether the exact or the approximate algorithm should be
used, and with which outer loop.
7 Experimental setup
7.1 Data sets and algorithms
We use the UCR time series archive (Dau et al., 2019) to assess the speed and predic-
tive performance of all the algorithms. More precisely, we consider the 142 univariate
time series classification data sets from this archive: the 112 univariate equal-length
no-missing-value data sets, plus the 30 data sets of the “bake off redux” study (Mid-
dlehurst, Sch¨ afer, & Bagnall, 2024). We use the same 30 resamples, for each of the
142 data sets, that have been used in the most recent studies on this topic, making
our results comparable to the ones from such studies.
We consider the following eight algorithms:
31

• MomentQuant("exact", "samples")is our implementation of Quant with exact
quantiles using a series-outer loop.
• MomentQuant("exact", "intervals")is our implementation of Quant with exact
quantiles using an interval-outer loop.
• MomentQuant("exact", "auto")is our implementation of Quant with exact quan-
tiles using automatically either the series-outer or interval-outer loop.
• MomentQuant("approx", "samples")is our implementation of Quant with approxi-
mate moment-based quantiles using a series-outer loop.
• MomentQuant("approx", "intervals")is our implementation of Quant with approx-
imate moment-based quantiles using an interval-outer loop.
• MomentQuant("approx", "auto")is our implementation of Quant with approximate
moment-based quantiles using automatically either the series-outer or interval-outer
loop.
• QuantFloat64is the original implementation of Quant, in PyTorch, with the only
change being the use of double precision instead of single precision.
• QuantNumpyis the one-to-one translation of QuantFloat64in NumPy, notably using
the numpy.quantilefunction.
For MomentQuant, if the outer loop is not specified, it implicitly means
that we refer to the automatic modes: MomentQuant("exact")refers
to MomentQuant("exact", "auto"), and MomentQuant("approx")refers to
MomentQuant("approx", "auto"). Indeed, the whole point of the automatic modes
is to try to automatically pick the faster version based on the size of the data set,
and they are the default modes in our implementation. The choice for the outer-loop
( "samples", "intervals"or "auto") has no impact on the transformation output,
and thus on the classification performance, but only on the runtime. Finally, for clas-
sification performance, MomentQuant refers to MomentQuant("approx"), while Quant
refers to either MomentQuant("exact")or QuantFloat64(which are theoretically
identical).
Compared to Quant’s reference implementation, we made several changes in order
to improve runtime performance and to perform fair comparisons:
• We changed the library used to perform all the mathematical operations, replacing
PyTorch with NumPy. Indeed, we had to use Numba to obtain optimal performances
for mathematical operations that could not be easily vectorized, and Numba was
designed to be used with NumPy arrays. It would not be fair to have two different
libraries in the comparisons as these two libraries might potentially have different
optimizations and performances.
• The PyTorch function doing the most work in Quant’s reference implementation,
that is torch.quantiles, was known to be significantly slower than NumPy’s equiv-
alent function,3 although very recent improvements have been made to improve the
performance of torch.quantileson CPU. 4
3https://github.com/pytorch/pytorch/issues/64947
4https://github.com/pytorch/pytorch/pull/188394
32

• We actually did not use the numpy.quantilefunction in practice because it is very
suboptimal when many quantiles are computed, which is the case in Quant for large
lbecause, at any level, the number of quantiles is proportional to the length of each
interval, which itself is proportional to the series lengthl. We reported this issue. 5
• Furthermore, we changed the precision used, replacing the simple precision with
double precision. Simple precision is the default data type in PyTorch (and in deep
learning in general) as it divides by two the random-access memory required and
makes floating-point arithmetic slightly faster. In non-deep machine learning, double
precision is more common. In order to have fair comparisons, we had to use the
same precision everywhere, and made the arbitrary decision to use double precision.
We provide numerical results highlighting the impact of these changes in Subsec-
tion 8.1.
For the classification step, we naturally use extremely randomized trees (Geurts et
al., 2006), since it is the algorithm used with Quant (Dempster et al., 2024). We also
use the default values for the hyperparameters of Quant (depthd= 6 and quantile
divisorν= 4) and the same values for the hyperparameters of extremely randomized
trees as in (Dempster et al., 2024).
7.2 Metrics and comparisons
We use the accuracy (ACC) as the main metric in our comparative analyses, but
we also report the scores for four other metrics on the 142 UCR data sets in order
to make our algorithms easily comparable to existing ones. These four metrics are
balanced accuracy (BALACC), area under the receiver operating characteristic curve
(AUROC), negative log-likelihood (NLL) and F1-score (F1).
In order to compare the performance of two algorithms on the 142 data sets,
we use paired t-tests and Wilcoxon tests to test the equality of means and medians
respectively, with a significance level ofα= 0.05.
7.3 Experiments, implementation and reproducibility
All the experiments were run on a MacBook Air (M1, 2020) with 16 GB RAM using
Python 3.13.14. We used the following Python packages to implement MomentQuant:
• Numba(0.63.1) (Lam, Pitrou, & Seibert, 2015) is an open source just-in-time
compiler that translates a subset of Python and NumPy code into fast machine code.
• NumPy(2.3.5) (Harris et al., 2020) is a standard Python package for manipulating
n-dimensional arrays.
• scikit-learn(1.8.0) (Pedregosa et al., 2011) is a popular Python package dedicated to
machine learning, providing implementations of many algorithms as well as utility
tools.
Additionally, to perform all the experiments, including saving the results and
generating the figures, we also used the following Python packages:
5https://github.com/numpy/numpy/issues/32187
33

• aeon(1.5.0) (Middlehurst, Ismail-Fawaz, et al., 2024) is a popular Python package
for time series machine learning tasks such as classification, regression, clustering,
anomaly detection, segmentation and similarity search.
• joblib(1.5.3) is a set of tools to provide lightweight pipelining in Python, notably
transparent disk-caching of functions and lazy re-evaluation, as well as easy simple
parallel computing.
• Matplotlib(3.11.1) (Hunter, 2007) is a comprehensive library for creating static,
animated, and interactive visualizations in Python.
• pandas(2.3.3) (Wes McKinney, 2010) is a fast, powerful, flexible and easy to use
open source data analysis and manipulation tool.
• SciPy(1.17.1) (Virtanen et al., 2020)
• seaborn(0.13.2) (Waskom, 2021) is a Python data visualization library based on
Matplotlib, providing a high-level interface for drawing attractive and informative
statistical graphics.
• PyTorch(2.13.0) (Paszke et al., 2019) is an optimized tensor library for deep
learning.
The source code is publicly available on a GitHub repository.6 We provide detailed
instructions so that our results can be easily reproduced by anyone.
8 Results
We present our results in several sections. Subsection 8.1 highlights the impact of the
implementation choice on the runtime. In Subsection 8.2, we provide empirical results
comparing theory and practice. Subsection 8.3 compares the transformation runtimes
for different algorithms. In Subsection 8.4, we compare the classification performance
and the end-to-end runtimes for different algorithms. Subsection 8.5 provides empirical
comparisons between the true and approximated, moment-based quantiles.
8.1 The impact of the implementation choice
We mentioned in Section 5 that we reimplemented Quant in NumPy. We now provide
quantitative results justifying this decision. Our benchmark includes 300 series at each
ofl∈ {512,1024, . . . ,32768}, and three implementations:QuantFloat64, QuantNumpy,
and MomentQuant("exact", "intervals"). MomentQuant("exact", "intervals")is
implemented in NumPy only, and is very similar to QuantNumpy, but we compute
the quantilesmanuallyinstead of using the numpy.quantilefunction: we use the
numpy.sortfunction to sort the (sub)series and compute the quantiles based on
the sorted values using linear interpolation. We insist on the fact that all three
implementations are theoretically and algorithmically strictly identical.
Table 1 provides the measured runtimes. QuantNumpywas only timed up tol=
4096, since it was already unambiguously the slowest implementation well before that
point, and its relative runtimes kept growing withl. We also omit multi-threading
runtimes for NumPy-based implementations, since the functions involved do not have
6https://github.com/johannfaouzi/moment-quant
34

T able 1: Wall-clock runtime of MomentQuant("exact", "intervals"), QuantFloat64
(1 thread and 8 threads), and QuantNumpy, as a function of series lengthl, and
each implementation’s runtime relative to MomentQuant("exact", "intervals")’s run-
times.
l
MomentQuant
("exact", "intervals")
QuantFloat64
(1 thread)
QuantFloat64
(8 threads)
QuantNumpy
512 0.073s 0.156s 0.137s 0.348s
1024 0.175s 0.340s 0.254s 1.077s
2048 0.397s 0.768s 0.463s 3.621s
4096 0.895s 1.731s 0.786s 12.915s
8192 1.982s 3.842s 1.388s –
16384 4.329s 8.490s 2.609s –
32768 9.373s 18.537s 4.905s –
512 1.00×2.14×1.89×4.79×
1024 1.00×1.95×1.45×6.17×
2048 1.00×1.94×1.17×9.13×
4096 1.00×1.93×0.88×14.43×
8192 1.00×1.94×0.70×–
16384 1.00×1.96×0.60×–
32768 1.00×1.98×0.52×–
native multi-threading, so the runtimes for single-threading and multi-threading are
identical.
Although the three implementations are theoretically strictly identical, their run-
times are much different. Focusing on the single-threaded runtimes first, we see that
our implementation is around 2 times faster than the one in PyTorch across all the
value ofl, and much faster than the implementation using the numpy.quantilefunc-
tion. After digging into the source code of both libraries, we managed to understand
the source of both these differences:
• PyTorch’s implementation of sorting always performs the sorting of both the values
( sort) and the indices ( argsort), which is not the case in NumPy. We show in
Section 9 that, contrary to a naive swap-counting argument, this roughly 2×gap
does not come from PyTorch performing more comparisons or swaps than NumPy.
• The numpy.quantilefunction does not sort all the values, and performs partitions
instead. Indeed, in order to compute quantiles, it is not necessary to sort all the
values: the only values needed are the values before and after each quantile of interest
(in order to perform the linear interpolations). However, the cost of a partition for
a vector of sizemis Θ(m), so the cost ofaindependent partitions is Θ(m·a),
which is much worse than Θ(m·log(m)) (the cost of a full sort) for large values
ofa, which is the case in Quant’s transformation. Indeed, the number of quantiles
computed in Quant is (approximately) proportional to the length of each subseries,
so the complexity of using independent partitions is Θ(m 2), hence the non-linear
relative runtime increase for QuantNumpywhenlincreases.
35

Regarding multi-threading, we observe that the benefit becomes bigger as the
series length increases. These results are logical: the larger the series, the longer the
sorting takes, while the overhead remains constant. On our machine with 8 threads,
QuantFloat64with multi-threading becomes faster than MomentQuantfor a series
length between 2048 and 4096.
Taken together, these results illustrate how large a difference implementation choice
alone can make to several functions computing the exact same quantities.
8.2 Theory versus practice
We derived closed-form cost models for MomentQuant’s exact and approx modes
in Section 4 and Section 6, and for both outer-loop strategies (interval-outer and
series-outer) in Section 5 and Subsection 6.3. These cost models depend on multiple
hardware-specific constants:
• the sort and extraction constants for the exact mode:c (v) 1 , c(v) 2 , c(v) 3 ,
• the moment update, Cornish-Fisher evaluation and moment conversion for the
approx mode: ˜c(v) 1 , ˜c(v) 2 , ˜c(v) 3 , and
• the per-call dispatch overheadsκ (I) (l),κ (S)(l), ˜κ(I) (l), and ˜κ(S)(l) for the interval-
outer and series-outer versions, and the exact and approx modes respectively.
These constants say nothing about whether the resulting formulas actually predict
real wall-clock time, only that the formulas are internally consistent. We checked
the former directly, for all five estimators that this project has a cost model for:
MomentQuant’s four (mode, version) combinations and QuantFloat64 (structurally
identical to exact/intervals).
8.2.1 Estimating the hardware-specific constants
All constants above were estimated from a single, dedicated calibration sweep: series
lengthlcrossed with number of seriesn, over a grid spanningl∈ {16, . . . ,8192}
andn∈ {1, . . . ,10 000}, timed single-threaded. At eachl, the measured runtime as
a function ofnis affine (an intercept plus a term linear inn, see Theorem 19 and
Theorem 20). Regressing runtime againstnat eachlseparately recovers, perl, a
per-series marginal cost (the slope) and a fixed per-call overhead (the intercept).
The constantsc (v) 1 , c(v) 2 , c(v) 3 are then obtained by a single ordinary-least-squares
regression of the per-lmarginal costs against the theorem’s own basis functions (sort
work, number of quantiles extracted, and total interval width), computed exactly
from the real interval layout MomentQuant builds internally (not from the power-
of-2-restricted closed forms of Section 4, which would not apply to everylon the
grid).κ (I) (l) andκ (S)(l) are obtained from the same per-lintercepts, modeled as
κ(l) =A−B/l(Remark 4).
The approx-mode constants ˜c1, ˜c2, ˜c3 are estimated the same way in principle, but
from a dedicated microbenchmark that times the moment-computation and Cornish-
Fisher-extraction phases separately, rather than only ever as a fused total. The two
natural regressors for the fused fit are collinear enough (correlation>0.999 in our
36

T able 2: Relative errors between the theoretical and empirical runtimes.
Estimator Mean Standard deviation Minimum Maximum
MomentQuant("exact", "samples")−1.5% 1.8%−5.4% +0.6%
MomentQuant("exact", "intervals")+3.6% 15.1%−37.0% +23.3%
MomentQuant("approx", "samples")−2.8% 24.5%−68.4% +24.5%
MomentQuant("approx", "intervals")+5.7% 24.8%−24.4% +38.0%
QuantFloat64+15.4% 12.6%−6.6% +45.2%
experiments) that a joint fit leaves ˜c2 and ˜c3 only weakly identified, occasionally pro-
ducing a physically implausible negative coefficient. Timing the two phases separately
avoids this by regressing against a far less collinear pair of basis functions.
All constants are specific to the fixed configuration used throughout this study
(d= 6,ν= 4) and to the machine that they were measured on.
8.2.2 Holdout validation
We also performed holdout validation of these constants by comparing the theoretical
and empirical runtimes for new experiments. We used a grid of series lengths spanning
l∈ {16, . . . ,4096}and a fixedn= 698 number of series. Furthermore, we used a grid
of numbers of series spanningn∈ {64, . . . ,16 384}and a fixedl= 384 series length.
Not only none of the (n, l) combination in this holdout validation appears in the grid
used to estimate the hardware-specific constants, but these runtimes are also obtained
from new experiments.
Table 2 shows that the cost model transfers well to held-out (l, n) combinations,
with a mean error within a few percents of zero for four of the five estimators.
MomentQuant("exact", "samples")is the tightest fit by a wide margin (mean−1.5%,
standard deviation 1.8%, never off by more than 5.4% in either direction). The
series-outer kernel’s compiled, single-call-per-series structure is evidently the easi-
est of the five to model precisely. QuantFloat64is the outlier: despite sharing the
same functional form as MomentQuant("exact", "intervals"), its predictions carry
the largest systematic bias of any estimator (+15.4% on average, consistently in the
same direction), These results suggest that fitting its ownc 1, c2, c3 andκ (I) (l) directly,
rather than reusing MomentQuant’s exact-mode constants, still leaves some PyTorch-
specific overhead unaccounted for that this cost model was not designed to cap-
ture. MomentQuant("approx", "intervals"), MomentQuant("exact", "intervals"),
MomentQuant("approx", "samples")show wider spreads, with individual worst-case
errors reaching 37 to 68%. Inspecting these directly shows the largest errors cluster
at the smallestlornvalues in each sweep, exactly where the fixed per-call dispatch
overheadκ(l) (the hardest-to-model term) makes up the largest share of the total
predicted cost.
37

T able 3: Comparisons between the calibrated dispatch
nheuristic and theorem-derivedn ∗ theorem (Theorem 21 and
Theorem 33 extended to all four representations) crossovers, by
mode and series lengthl, single-threading only.
Model n heuristic n∗ theorem Ratio
MomentQuant("exact")
16 23 170 20.0 1161×
64 2 482 44.8 55×
256 395 51.2 7.7×
1024 72.4 12.8 5.7×
4096 14.3 2.9 5.0×
8192 6.5 1.4 4.7×
MomentQuant("approx")
16 39 964 1 057 38×
64 9 991 610 16×
256 2 498 216 11.6×
1024 624 75.8 8.2×
4096 156 28.5 5.5×
8192 78.1 17.9 4.3×
8.2.3 Dispatch crossover
Beyond checking whether the cost model predicts raw runtime, we can check whether
it predicts the rightdecision: at what sample countnshould the automatic switch
from the series-outer to the interval-outer kernel. Theorem 21 and Theorem 33 give
a formal crossover sample sizen ∗(l, d, ν), assembled bottom-up from the same per-
operation constants validated above, evaluated here with their all-four-representations
rather than the raw-representation-only theorem statement. The calibrated threshold
actually used by the automatic switch is fit a different way entirely: directly against
measured runtimes, as a single pooled, effectivelyl-independent overhead, precisely
because Theorem 21’s own remark argues that composingn ∗ representation-by-
representation, andl-value byl-value, from the theorem’s ownl-dependent constants
is impractical to estimate reliably. Table 3 compares the two crossovers directly, across
the calibration grid’s ownl∈ {16, . . . ,8192}.
Theory and practice disagree sharply, and always in the same direction. At everyl
tested and in both modes, we havenheuristic ≫n ∗ theorem: the calibrated rule keeps using
the series-outer kernel for a far larger sample count than the theorem says is optimal.
However, the size of the disagreement is not stable. It is largest at the smallestl(a
factor of 1161×for exact mode atl= 16, 38×for approx mode) and shrinks steadily,
by two to three orders of magnitude, aslgrows, settling into a roughly constant 4 to
5×(exact) or 4 to 6×(approx) residual gap that persists even atl= 8192, the largest
lon the calibration grid. It lines up with a mechanism that we already anticipated
rather than a new one: the calibrated heuristic fits a single, pooled overhead with
nol-dependence of its own, whileκ (I) (l) and ˜κ(I) (l), the quantities that the theorem
actually plugs in, are themselves stronglyl-dependent and largest in relative terms at
smalll. A pooled,l-independent stand-in for a genuinelyl-dependent quantity should
disagree with the theorem most where that quantity varies fastest (smalll) and least
38

T able 4: Total wall-clock runtime to transform all 142 UCR archive
data sets (training and test set merged), using 1 thread and 8 threads,
and the resulting speedup.
Estimator 1 thread 8 threads Speedup
MomentQuant("exact", "samples")117.97s 26.67s 4.42×
MomentQuant("exact", "intervals")64.80s 65.27s 0.99×
MomentQuant("exact", "auto")69.15s 26.56s 2.60×
MomentQuant("approx", "samples")38.45s 23.41s 1.64×
MomentQuant("approx", "intervals")39.44s 40.25s 0.98×
MomentQuant("approx", "auto")38.74s 23.36s 1.66×
QuantFloat64105.55s 65.63s 1.61×
where it flattens out (largel), which is exactly the shape Table 3 shows. This is
consistent with the pooling simplification being the dominant source of disagreement
between the two models, rather than a more basic misspecification of either one.
Theorem 21 and Theorem 33’s crossovers should be read as validating the existence and
functional form of a crossover, not as a formula that can substitute for the calibrated,
measurement-fit threshold at any particularl.
In our implementation of MomentQuant, the automatic version uses the cali-
brated dispatch crossovers instead of the theorem-derived crossovers, both in the
single-threaded and multithreaded setups.
8.3 Transformation runtimes
We now move from controlled, single-length microbenchmarks to a full, realistic work-
load: transforming both the training and test sets of all 142 data sets of the UCR
archive, for all six combinations of MomentQuant, alongside QuantFloat64as an
external reference, in both single-threaded and multithreaded (8 threads) setups.
Table 4 provides the corresponding runtimes. In the single-
threaded setup, we obtain the same ordering as the one established in
Table 1. MomentQuant("exact", "intervals")(64.80s) is faster than both
MomentQuant("exact", "samples")(117.97s, 1.8×slower) and QuantFloat64
(105.55s, 1.6×slower). These results are not surprising, since the archive mixes many
(n, l) combinations, some of which genuinely favor the interval kernel. The approx
mode is faster still, as expected from its better asymptotic complexity: all three
variants cluster tightly between 38 and 39s, roughly 1.7 to 1.8×faster than the best
exact-mode variant and 2.7 to 3.1×faster than QuantFloat64.
The multithreaded setup benefits the two kernels very differently. The interval-
outer kernel shows no speedup at all from 8 threads, since it is not parallelized in this
implementation, while the series-outer kernel (parallelized across series via Numba)
speeds up substantially: 4.42×for exact mode, a more modest 1.64×for approx mode.
QuantFloat64also benefits from PyTorch’s own default multi-threading (1.61×),
39

consistent with the results in Table 1. We tried to parallelize the interval-outer ker-
nel, but obtained worse results than in the single-threaded setup, which is why the
interval-outer kernel always use single-threading.
The automatic variants track whichever manual variant is actually faster in
each regime closely, without ever being the worst choice. In the single-threaded
setup, MomentQuant("exact", "auto")(69.2s) lands within 7% of the best single-
threaded choice ( MomentQuant("exact", "intervals"), 64.8s), so it does not always
pick the faster variant. At 8 threads, MomentQuant("exact", "auto")(26.56s) essen-
tially matches the best choice outright ( MomentQuant("exact", "samples"), 26.67s),
since the parallel-specific threshold correctly steers the large majority of the archive
toward the now much faster samples kernel. The same holds for the approx mode in
both settings ( MomentQuant("approx", "auto")within 1% of the best manual variant
single-threaded, and matching it at 8 threads). This is an end-to-end validation of the
calibrated dispatch rule described above, at a scale and data set diversity well beyond
the single-length microbenchmark that it was calibrated on.
8.4 Classification performance and end-to-end runtimes
We now evaluate the automatic versions of both the approximate
( MomentQuant("approx")) and exact ( MomentQuant("exact")) modes, alongside
QuantFloat64as an external reference, on all 142 UCR archive data sets, using
30 resamples per data set. Regarding the values of the hyperparameters of the
classification algorithms, we use the same ones as in (Dempster et al., 2024).
8.4.1 Classification performance
First, we compare three classification algorithms built on top of MomentQuant:
extremely randomized trees (Geurts et al., 2006), random forests (Breiman, 2001),
and Ridge (Hoerl & Kennard, 1970). In (Dempster et al., 2024), the authors showed
that Quant performed significantly better with extremely randomized trees than with
the other two algorithms. Figure 3 shows the pairwise accuracy between the three
algorithms, with extremely randomized trees as the reference. MomentQuant is sig-
nificantly better with extremely randomized trees (mean accuracy 0.8505) than with
random forests (mean accuracy 0.8396,p <0.001) and Ridge (mean accuracy 0.7678,
p <0.001). These results are consistent with the ones in (Dempster et al., 2024).
We now compare the classification performances of MomentQuant with both
MomentQuant("exact")and QuantFloat64. Table 5 provides the classification perfor-
mance of MomentQuant("approx"), MomentQuant("exact")and QuantFloat64, on the
142 UCR data sets. MomentQuant("approx")and QuantFloat64have (almost) the
same performance (at least up to 4 decimals, except for the negative log-likelihood).
MomentQuant("approx")is slightly behind MomentQuant("exact")for all five metrics,
but with less than 0.01 for each metric.
Figure 4 shows the pairwise accuracy between the three algorithms, with
MomentQuant as the reference. MomentQuant has a slightly lower mean accuracy
(0.8505) than both MomentQuant("exact")(0.8551) and QuantFloat64(0.8551), but
40

0.4 0.5 0.6 0.7 0.8 0.9 1.0
Random forest accuracy
(mean: 0.8396)
0.4
0.5
0.6
0.7
0.8
0.9
1.0
Extra trees accuracy
(mean: 0.8505)
* Dashed lines represent the median
Extra trees wins here
[112W, 5T, 25L]
Random forest wins here
[25W, 5T, 112L]
Wilcoxon test for equality of medians: p-value ≤ 1e-3
Paired t-test for equality of means: p-value ≤ 1e-3
0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
Ridge accuracy
(mean: 0.7678)
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
Extra trees accuracy
(mean: 0.8505)
* Dashed lines represent the median
Extra trees wins here
[126W, 2T, 14L]
Ridge wins here
[14W, 2T, 126L]
Wilcoxon test for equality of medians: p-value ≤ 1e-3
Paired t-test for equality of means: p-value ≤ 1e-3
Fig. 3: Pairwise accuracy for MomentQuant with extremely randomized trees
(default), compared to with random forest (left) and Ridge (right) in terms of accuracy
on the 142 UCR data sets. The mean accuracy scores are computed over 30 resamples
for each data set.
T able 5: Classification performance of MomentQuant("approx"),
MomentQuant("exact")and QuantFloat64, on the 142 UCR data sets.
For each algorithm and each metric, the mean score is computed over the
142×30 (data set, resample) pairs. The direction of each arrow indicates in
which direction a better score is for each metric.
Estimator ACC↑BALACC↑AUROC↑NLL↓F1↑
MomentQuant("approx")0.8505 0.8264 0.9541 0.5345 0.8262
MomentQuant("exact")0.8551 0.8301 0.9559 0.5332 0.8305
QuantFloat640.8551 0.8301 0.9559 0.5333 0.8305
the differences are significant (p= 0.002). The worst raw difference in terms of accu-
racy occurs on the ShapeletSim data set, where accuracy drops from 0.9852 to 0.8269
(−0.1583). Otherwise, the raw accuracy difference lies between−0.0470 (ACSF1) and
+0.0339 (Lightning2). This outlier (ShapeletSim) is easily visible in Figure 4.
Although MomentQuant("exact")and QuantFloat64are theoretically identical,
they actually slightly differ in practice due to the different libraries used (NumPy and
PyTorch). We identified two reasons that can make the results very slightly different:
• Different mean computation: NumPy and PyTorch compute the mean via different
summation orders, and double-precision addition is known to be non-associative
because of rounding errors possibly occurring at each step. This difference can make
centered quantiles very slightly different depending on the library.
41

0.4 0.5 0.6 0.7 0.8 0.9 1.0
MomentQuant("approx") accuracy
(mean: 0.8505)
0.4
0.5
0.6
0.7
0.8
0.9
1.0
MomentQuant("exact") accuracy
(mean: 0.8551)
* Dashed lines represent the median
MomentQuant("exact") wins here
[79W, 9T, 54L]
MomentQuant("approx") wins here
[54W, 9T, 79L]
Wilcoxon test for equality of medians: p-value = 0.005
Paired t-test for equality of means: p-value = 0.002
0.4 0.5 0.6 0.7 0.8 0.9 1.0
MomentQuant("approx") accuracy
(mean: 0.8505)
0.4
0.5
0.6
0.7
0.8
0.9
1.0
Quant accuracy
(mean: 0.8551)
* Dashed lines represent the median
Quant wins here
[76W, 9T, 57L]
MomentQuant("approx") wins here
[57W, 9T, 76L]
Wilcoxon test for equality of medians: p-value = 0.007
Paired t-test for equality of means: p-value = 0.002
Fig. 4: Pairwise accuracy for MomentQuant("approx")compared to
MomentQuant("exact")(left) and QuantFloat64(right) in terms of accuracy on the
142 UCR data sets. The mean accuracy scores are computed over 30 resamples for
each data set.
• Discrete Fourier transform: We compared the results of the discrete Fourier trans-
form for multiple series lengths between both libraries and identified one value (2047)
where the results were very slightly different. More values of series lengths leading
to slightly different results is a possibility.
On the 142 data sets, MomentQuant("exact")has 10 wins, 129 ties and 3 losses com-
pared to QuantFloat64, and the difference in mean accuracy (0.855099 vs 0.855077)
is not significant (p= 0.087).
8.4.2 End-to-end and inference-only runtimes
We now compare the runtimes of the whole pipeline (transformation step + classifica-
tion step) instead of the transformation step only. Table 6 provides the total runtimes
of MomentQuant("approx"), MomentQuant("exact"), and QuantFloat64, summed over
the 142 UCR data sets and averaged over the 30 resamples, in the single- and
multithreaded setups.
Starting with the total (training + inference) runtimes, the gains of
both MomentQuant("approx")and MomentQuant("exact")are mild compared to
QuantFloat64, but relatively higher in the multithreaded setup than in the single-
threaded setup. In the single-threaded setup, the total runtimes are respectively
401s (−15%), 436s (−8%), and 474s. In the multithreaded setup, the total run-
times are respectively 156s (−22%), 161s (−19%), and 200s. Indeed, as noted in
(Dempster et al., 2024), most of the total runtime comes from training the classi-
fication algorithm. This is even more exacerbated by the runtime improvements of
MomentQuant("approx")and MomentQuant("exact"). Figure 5 shows the breakdown of
42

T able 6: Total and inference-only wall-clock runtime, summed over 142 data sets
and averaged over the 30 resamples, in the single-threaded and multithreaded
setups.
Estimator Total (1 thread) Inference-only (1 thread) Total (8 threads) Inference-only (8 threads)
MomentQuant("approx")401s 29s 156s 22s
MomentQuant("exact")436s 47s 161s 25s
QuantFloat64474s 68s 200s 48s
the total single-threaded runtime of MomentQuant("approx"), MomentQuant("exact"),
and QuantFloat64into its four stages: training (transformation, classification) and
inference (transformation, classification). The breakdown is averaged over the 142
UCR data sets, but split into four bins for the series length: short (l <150, 35 data
sets), medium-short (150≤l <320, 36 data sets), medium-long (320≤l <720, 38
data sets) and long (l >720, 33 data sets). In every situation, training the classifi-
cation algorithm is the step taking the most (relative) time. The differences between
MomentQuant("approx"), MomentQuant("exact"), and QuantFloat64are the biggest
for long series, which is consistent with our previous results. Indeed, the computational
complexities for MomentQuant("approx")and MomentQuant("exact")in the saturated
regime are Θ(d·l) and Θ(d·l·log(l)) respectively. The absolute difference becomes
bigger for larger values of log(l), that is for larger values ofl.
We believe that benchmarking time series classification algorithms using the total
runtime (training + inference) only is inappropriate. Indeed, in actual real-life applica-
tions, training an algorithm is performed once (in a while), while its use in production
is much more common, potentially daily. Therefore, we believe that time series clas-
sification algorithms should also be benchmarked using the inference-only runtime.
Figure 6 shows the corresponding breakdown of the inference-only single-threaded
runtime of MomentQuant("approx"), MomentQuant("exact"), and QuantFloat64. In
every situation, the transformation step is taking the most (relative) time. For all
three estimators, the bigger the series length, the higher the proportion of the trans-
formation step in the inference-only runtime. These results prove that optimizing the
transformation steps of Quant and MomentQuant is actually relevant.
We now provide theoretical explanations for these differences in relative runtimes
between the transformation and classification steps in the training and inferences
phases. To make the analysis simpler, we will focus on the asymptotic complexities
and overlook the constants terms (e.g., for the overheads). For a given series length,
the transformation steps of Quant and MomentQuant are always proportional to the
number of series in the data set, independently of the phase (training or inference).
The only additional work that the transformation step of the training phase has to per-
form is to compute the intervals based on the series length, which has a Θ(min(l,2 d))
computational complexity and is thus negligible. On the other hand, classification algo-
rithms take much longer to train than to infer from. For instance, the computational
43

MomentQuant("approx")
MomentQuant("exact")
Quant
MomentQuant("approx")
MomentQuant("exact")
Quant
MomentQuant("approx")
MomentQuant("exact")
Quant
MomentQuant("approx")
MomentQuant("exact")
Quant
0
20
40
60
80
100Mean % of total pipeline time
Short Medium-short Medium-long Long
Transformation (training)
Classification (training)
Transformation (inference)
Classification (inference)
Fig. 5: Breakdown of the total wall-clock single-threaded runtime of
MomentQuant("approx"), MomentQuant("exact"), and QuantFloat64into its four
stages: training (transformation, classification) and inference (transformation, classi-
fication). The breakdown is averaged over the 142 UCR data sets, but split into four
bins for the series length: short, medium-short, medium-long and long.
44

MomentQuant("approx")
MomentQuant("exact")
Quant
MomentQuant("approx")
MomentQuant("exact")
Quant
MomentQuant("approx")
MomentQuant("exact")
Quant
MomentQuant("approx")
MomentQuant("exact")
Quant
0
20
40
60
80
100Mean % of total inference time
Short Medium-short Medium-long Long
Transformation (inference) Classification (inference)
Fig. 6: Breakdown of the inference-only wall-clock single-threaded runtime of
MomentQuant("approx"), MomentQuant("exact"), and QuantFloat64into its two
stages: transformation and classification. The breakdown is averaged over the 142
UCR data sets, but split into four bins for the series length: short, medium-short,
medium-long and long.
45

complexity of training an extremely randomized trees model isO(m·k·n·log(n)),
wheremis the number of trees,kis the number of randomly selected features at each
node, andnis the number of training samples (Geurts et al., 2006). However, its infer-
ence computational complexity is onlyO(m·p·log(n)), withpbeing the number of
samples. Assuming that the training and test sets have the same number of samples
(n=p), we can see that the training computational complexity has an extra factor
k. In our experiments, we setk= 0.1 as it is done in (Dempster et al., 2024), mean-
ing that the number of randomly selected features at each node is proportional to the
number of features, which is proportional to the series lengthl. Thus, for training and
test sets with the same number of samplesn, the computational complexity of train-
ing the extremely randomized trees model isO(m·l·n·log(n)), which has an extral
factor compared to its inference computational complexity, which isO(m·n·log(n)).
8.4.3 T rade-offs
We now investigate the trade-offs that MomentQuant makes compared to Quant.
We first compare the accuracy differences and runtime speedups to the series
lengths. Indeed, Section 6 motivates MomentQuant specifically for long series, where
its better asymptotic complexity should matter most. Table 7 provides the mean
accuracy scores and the median single-threaded end-to-end runtimes between the
"approx"and "exact"versions of MomentQuant, for each four bin of series lengths.
There is no clean, monotonic pattern in these results. The biggest deficits for the
"approx"version, both in terms of accuracy difference (−0.94) and runtime speedup
(0.997×), occur for the medium-long series length bin. For the other three bins, the
"approx"version performs worse, but to a lesser extent (accuracy differences ranging
from−0.58 to−0.08), and is faster (speedup ratios ranging from 1.06 to 1.21), than
the "exact"version. However, the runtimes are end-to-end (i.e., including the clas-
sification steps) and the numbers of samples are not taken into account, which might
explain the absence of monotonicity. Figure 7 complements Table 7 with the results
for the 142 data sets.
We also compare the trade-offs in accuracy and transform-runtime between
MomentQuant("approx")and MomentQuant("exact"). Figure 8 shows the results for
the 142 data sets. MomentQuant("approx")is faster for 108 data sets, and bet-
ter for 40 out of the 108 data sets. On the other hand, MomentQuant("exact")
is faster for 34 data sets, and better for 20 out of the 34 data sets. Interest-
ingly, the proportion of times when MomentQuant("approx")is better is similar when
MomentQuant("approx")is faster (37%) and slower (41%). Likewise, the proportion of
times when MomentQuant("approx")is faster is similar when MomentQuant("approx")
is better (74%) and worse (77%). The Pearson correlation coefficient (0.0884) confirms
the weak linear relationship between the accuracy differences and the transform-
runtime speedup ratios.
46

T able 7: Mean accuracy and median single-threaded end-to-end runtime between the
"approx"and "exact"versions of MomentQuant, by series-length bin. ∆ is the mean,
over the data sets in the bin, of each data set’s own ( "approx"− "exact") accuracy
difference. Speedup is likewise the mean, over the data sets in the bin, of each data set’s
own "exact"/ "approx"runtime ratio. This is a per-data-set average, not the ratio
of the two (bin-aggregated) Runtime columns shown here, so it does not necessarily
match a naive division of these two columns.
Series length bin Accuracy Runtime
"approx" "exact"∆ "approx" "exact"Speedup
Short 0.8818 0.8826−0.0008 0.415 0.470 1.206×
Medium-short 0.8663 0.8683−0.0020 0.592 0.670 1.064×
Medium-long 0.8279 0.8373−0.0094 0.623 0.648 0.997×
Long 0.8262 0.8320−0.0058 5.115 5.344 1.162×
102 103
Series length (in time points)
0.4
0.5
0.6
0.7
0.8
0.9
1.0Accuracy
MomentQuant("approx")
MomentQuant("exact")
102 103
Series length (in time points)
1
1.5
2
End-to-end runtime speedup (exact / approx)
Fig. 7: Accuracy (left) and speedup ratios (right) compared to series length for
MomentQuant("approx")and MomentQuant("exact"). For each of the 142 UCR data
sets, the mean accuracy is computed over 30 resamples and plotted, the median
runtime is computed over 30 resamples, and the ratio of the medians is plotted. Addi-
tionally, the mean accuracy and speedup ratio for each bin of series length (short,
medium-short, medium-long and long) are also plotted.
8.5 Fidelity of the moment-based quantile approximation
All the previous comparisons regarding the approx mode are downstream. They mea-
sure its effect on classification accuracy and runtime, but never the quality of the
Cornish-Fisher approximation itself, at the level of individual quantile values. We
close this gap in this section by comparing the true and approximate moment-based
quantiles using Pearson correlation. We investigate the distributions of the Pearson
correlation coefficients at each level on six length-diverse UCR data sets. Naturally,
47

0.25 0.5 1 2 4 8
Transform-runtime speedup (exact / approx)
−0.150
−0.125
−0.100
−0.075
−0.050
−0.025
0.000
0.025
Accuracy delta (approx - exact)
faster, more accurate
(n=40)
slower, more accurate
(n=14)
faster, less accurate
(n=68)
slower, less accurate
(n=20)
Fig. 8: Accuracy difference compared to transform-runtime speedup between
MomentQuant("approx")and MomentQuant("exact"). For each of the 142 UCR data
sets, the mean accuracy is computed over 30 resamples. To the right of the vertical line,
MomentQuant("approx")is faster than MomentQuant("exact"). Above the horizontal
line, MomentQuant("approx")is better than MomentQuant("exact").
we only include columns for which approximate quantiles are computed (because even
MomentQuant computes exact quantiles for the minimum and maximum).
Table 8 provides information about the series length and descriptive statistics on
the distribution of the Pearson correlation coefficients on the six data sets. Median
correlation is consistently high (0.598 to 0.988 depending on the data set), but every
data set’s distribution has a long negative tail (minima from−0.049 to−0.980), pulling
the mean substantially below the median in every case.
Figure 9 shows the distribution of Pearson correlation coefficients at each level for
the StarLightCurves data set, the largest one among the six considered, making its
per-depth histograms the least noisy of the six. The correlation rises monotonically
48

T able 8: Descriptive statistics of the distribution of the Pearson corre-
lation coefficients between the true and approximate quantiles, per data
set, pooled over every genuinely-approximated column.
Data setlNumber of columns Mean Median Minimum
ItalyPowerDemand 24 112 0.900 0.988−0.049
ECG200 96 570 0.820 0.881−0.849
GunPoint 150 870 0.689 0.878−0.959
Wafer 152 858 0.521 0.598−0.584
Yoga 426 3 033 0.702 0.847−0.980
StarLightCurves 1024 8 034 0.819 0.943−0.968
and substantially with depth, from a median of 0.650 at depth 0 to 0.729, 0.885, 0.962,
0.981, and finally 0.992 at depth 5. The deepest, shortest intervals are approximated
more reliably than the shallowest, longest ones, the opposite of what shrinking sample
size per interval alone would suggest. A plausible, but not independently confirmed,
explanation lies in which quantiles are actually being approximated at each depth.
At the shallowest levels, the extreme quantiles are closer to the tails (qnear 0 or 1),
which the Cornish-Fisher expansion is well known to approximate worst. On the other
hand, at the deepest levels, the extreme quantiles are less close to the tails, making
the approximation possibly less inaccurate. The remaining five data sets (Appendix B)
show the same qualitative direction wherever their own depth range is wide enough to
check it, though with visibly more sampling noise given their smaller column counts
per depth.
However, it is interesting to note that a Pearson correlation coefficient close to−1
is not necessarily bad for a downstream classification task. Indeed, changing the sign of
a variable has no impact for several families of classification algorithms such as linear
models and tree-based algorithms. Moreover, the algorithm used for MomentQuant
and Quant, extremely randomized trees, is a tree-based method.
9 One final experiment
In the original publication of Quant (Dempster et al., 2024), the authors proposed
the following optimization:
“In principle, we could sort each input representation once, keeping track of the indices of
the sorted values, and then form any interval by selecting the already-sorted values using
their indices. In practice, even the naive approach incurs negligible overall computational
cost. Median transform time over 142 data sets in the expanded UCR archive is less than
one second. The majority of compute time is spent in training the classifier. In other words,
any attempt at optimizing total compute time should concentrate on reducing the size of
the feature space, and/or improving the efficiency of classifier training. We leave further
optimization for future work.”
While our results confirmed that most of the runtime is dominated by the classification
algorithm and not Quant’s transformation, we focus in this study on the optimization
49

−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
25
50
75
100
125
150
Depth level 0 (n=889, median=0.6496)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
50
100
150
200
250
Depth level 1 (n=1321, median=0.7291)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
100
200
300
400
500
600
Depth level 2 (n=1513, median=0.8852)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
200
400
600
800
1000
Depth level 3 (n=1561, median=0.9616)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
200
400
600
800
1000
1200
Depth level 4 (n=1489, median=0.9809)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
200
400
600
800
1000
Depth level 5 (n=1261, median=0.9921)
Fig. 9: Distribution of the Pearson correlation coefficients between the exact and
approximated moment-based quantile values on the StarLightCurves data set (l=
1024), with one histogram per depth level 0 to 5. Each panel’s title reports the number
of genuinely-approximated columns at that depth and their median correlation.
50

of Quant’s transformation. We were thus interested in the proposed optimization.
However, it is only presented at the end of this article because the results are mixed.
As shown by Theorem 8, the total cost of sorting every interval separately is Θ(d·
l·log(l)) in the saturated regime: each of theddepth levels re-sorts (a subdivision of)
the whole series from scratch, even though the intervals’ endpoints are fixed and data-
independent. Quant’s authors anticipated this and suggested, without implementing
it, a fix: sort the series once, whose cost isO(l·log(l)), and reuse that single global
order to read off every interval’s sorted values directly, instead of sorting each interval’s
subsequence again. Since a given depth level’s (base or shifted) intervals partition [0, l)
into a small, fixed number of non-overlapping pieces, recovering their sorted values
from the global order only requires grouping each of thelglobally-sorted positions by
which interval it falls into. This is a bucket assignment known in advance from the
interval boundaries alone. If that grouping step could be done inO(l) per level, as a
genuine counting (bucket) sort would (since the number of distinct buckets per level
is small and fixed, so a comparison-based sort is not needed to group them), the total
cost would fall toO(l·log(l) +d·l), which is asymptotically better than Θ(d·l·log(l))
as soon asd≥2.
We implemented this optimization exactly as described, both in NumPy and
PyTorch. In both cases we first checked that the optimization produces numerically
identical output to the naive per-interval computation, before benchmarking it. The
two implementations tell different stories, for reasons specific to how each library is
built.
Table 9 provides the wall-clock runtimes of the naive and proposed implementa-
tions for multiple series lengths in both libraries. In NumPy, we do not distinguish
the single-threaded and multithreaded setups as both the NumPy functions involved,
numpy.sort()and numpy.argsort(), do not benefit from multi-threading. The results
in NumPy are underwhelming: the proposed optimization is consistently slower, by
a factor of roughly 2.4 to 2.7×, with the gap narrowing slowly aslgrows but never
closing. The results in PyTorch are more positive, without being outstanding. In
the single-threaded setup, the proposed optimization is slower forl≤2048, roughly
matches the naive implementation aroundl= 4096–8192, and is consistently 6 to
9% faster forl≥16384. In the multithreaded setup (with 8 threads in our experi-
ments), the proposed optimization is faster than the naive implementation at every
ltested. However, its advantage now shrinks aslgrows, from roughly 27% faster at
l= 1024 down to roughly 2% faster atl= 32768, which is the opposite trend from
the single-threaded setup. Two library-level differences explain these results.
First, there is a library-level difference in the cost of obtaining the permutation,
which explains why the proposed optimization sometimes works in PyTorch, but never
works in NumPy. The proposed optimization’s one mandatory global sort must be an
indexed sort ( argsort): it needs not only the sorted values but the original position
of each one, so that every value can later be assigned to the interval that it came
from. We already showed in Subsection 8.1 that the naive “swap-doubling” argument
does not hold up under isolation: pairing a value with an index adds only a modest
overhead, not a full 2×. The actual cost of an indexed sort relative to a plain sort in
NumPy depends strongly onl. Forl≲1024–2048, numpy.argsortis roughly as fast
51

T able 9: Wall-clock runtime of the naive and proposed implementa-
tions, and their ratio, as a function of series lengthl, in NumPy and
PyTorch.
LibrarylNaive version Proposed version Proposed / Naive
NumPy
512 0.072s 0.206s 2.85×
1024 0.171s 0.456s 2.66×
2048 0.393s 0.990s 2.52×
4096 0.904s 2.090s 2.31×
8192 1.989s 4.567s 2.30×
16384 4.295s 9.761s 2.27×
32768 9.264s 21.067s 2.27×
PyTorch
(1 thread)
512 0.153s 0.187s 1.22×
1024 0.337s 0.389s 1.15×
2048 0.745s 0.820s 1.10×
4096 1.703s 1.663s 0.98×
8192 3.762s 3.726s 0.99×
16384 8.325s 7.817s 0.94×
32768 18.288s 16.934s 0.93×
PyTorch
(8 threads)
512 0.130s 0.107s 0.82×
1024 0.244s 0.177s 0.73×
2048 0.449s 0.338s 0.75×
4096 0.754s 0.594s 0.79×
8192 1.293s 1.170s 0.90×
16384 2.318s 2.208s 0.95×
32768 4.722s 4.647s 0.98×
as numpy.sort, or even slightly faster. Beyond that point the ratio grows steadily,
reaching roughly 2×in double precision and 4 to 4.5×in single precision byl= 32768.
This is consistent with the 2.3×overhead of the proposed optimization over the naive
one observed in Table 9 at the samel.
This is not primarily a matter of doing more work: an indexed and a non-indexed
sort perform the exact same number of comparisons and swaps at everyl. Rather, it
is a matter of how that work accesses memory, compounded by a second, larger effect
specific to real-world implementations. To separate the two effects, we implemented
and compiled with Numba three quicksort variants sharing the exact same introsort
skeleton (median-of-three pivot, insertion-sort cutoff), so that Numba never invokes
a vectorizedsingle instruction, multiple data(SIMD) fast path for any of them, and
so that all three perform identical comparison and swap counts at everyl(verified
exactly):
• direct: a plain value sort. Comparisons and swaps both act directly and sequen-
tially on the values array. This mirrors the kernel behind numpy.sort.
• indirect: an indexed sort in which the values array is read-only, and only an
index array is permuted, with comparisons dereferencing through it. This mirrors
the kernel behind numpy.argsort.
52

T able 10: Wall-clock runtime of the direct, keyvalue, and indirectquicksort vari-
ants, as a function ofl, along with the keyvalue/ directand indirect/ directratios.
Units (µs or ms) are given per row. The four largest values ofl(from 65536 onward, below
the second horizontal rule) are well beyond any series length this paper’s pipeline ever
processes. They are included only to show where the indirect/ directratio is headed
asymptotically.
l direct keyvalue indirect keyvalue/ direct indirect/ direct
4 0.351µs 0.600µs 0.594µs 1.71×1.69×
8 0.360µs 0.607µs 0.613µs 1.69×1.70×
16 0.408µs 0.662µs 0.679µs 1.62×1.66×
32 0.480µs 0.762µs 0.784µs 1.59×1.63×
64 0.676µs 0.959µs 1.07µs 1.42×1.58×
128 1.16µs 1.55µs 1.71µs 1.33×1.47×
256 2.15µs 2.71µs 3.03µs 1.26×1.41×
512 4.35µs 5.18µs 5.88µs 1.19×1.35×
1024 9.20µs 10.7µs 12.2µs 1.17×1.32×
2048 22.5µs 29.5µs 28.7µs 1.31×1.28×
4096 123µs 130µs 157µs 1.06×1.28×
8192 365µs 378µs 457µs 1.04×1.25×
16384 0.843ms 0.875ms 1.06ms 1.04×1.26×
32768 1.85ms 1.96ms 2.34ms 1.06×1.26×
65536 3.95ms 4.25ms 5.04ms 1.08×1.27×
262144 18.1ms 18.9ms 23.0ms 1.05×1.28×
1048576 81.4ms 85.1ms 105ms 1.04×1.29×
4194304 356ms 372ms 501ms 1.04×1.41×
• keyvalue: an indexed sort in which the values and the indices are permuted together
on every swap, so comparisons stay direct and sequential on the values array,
exactly like direct. This mirrors PyTorch’s sorting kernel, used by both sortand
argsort.
Table 10 reports the wall-clock runtime of the three variants for everylin our grid,
along with the keyvalue/ directand indirect/ directratios.
The keyvalue/ directratio stays modest throughout, from about 1.7×at the
smallestl(dominated by fixed per-call overhead) down to 1.0–1.1×forl≥4096,
and it stays in that same narrow band all the way out tol= 4 194 304: pairing a
value with an index, on its own, is nowhere near twice the cost of a plain swap, at
any scale that we tested. This is directly relevant to the roughly 2×gap between
QuantFloat64and MomentQuant("exact", "intervals")observed earlier in Table 1
(Subsection 8.1): since PyTorch’s sorting kernel follows the keyvaluestrategy while
NumPy’s sortfollows direct, the keyvalue/ directratio here rules out swap-
counting as the explanation for that gap as well. The gap in Table 1 is more likely
dominated by PyTorch’s per-call dispatch and tensor-allocation overhead than by the
sorting algorithm itself. The indirect/ directratio is somewhat larger and follows a
53

mild U-shape: high at very smalll(again, fixed overhead), settling into a broad plateau
of roughly 1.25–1.29×froml= 4096 up tol= 262144, and then climbing again at the
two largest sizes tested, reaching 1.41×atl= 4 194 304. This ratio is past the plateau,
but still well short of the several-fold gap that a purely cache-miss-driven effect would
be expected to reach at even larger scales. The entries atl= 1024, 2048, and 4096
are also visibly noisier across repeated runs than their neighbors (up to a 3.5×spread
between the fastest and slowest of 40 repeats, against roughly 1.1–1.2×for most other
l). This spread did not shrink when we quadrupled the number of repeats, which
suggests a repeatable effect tied to this transition region. A plausible explanation,
but not verified, is neighboring jobs of very different sizes in the shuffled run order
interacting with the CPU’s frequency scaling, rather than one-off measurement noise.
This confirms that indirection has a real, cache-driven cost that keeps growing with
lwell beyond this paper’s operational range (l≤32768), but one that remains far
too small, at least at the scales tested here, to explain the roughly 2 to 4.5×gap
observed with the real numpy.argsortat the samel. The rest of that gap comes from a
second effect that this SIMD-free isolation deliberately excludes: NumPy’s sorthas a
vectorized SIMD fast path with no equivalent for argsort. SIMD is true simultaneous
parallel hardware-level execution and is different from multi-threading. This fast path
only pays off oncelis large enough, which is why the real argsort/ sortgap is
negligible, or even inverted, below roughlyl= 1024–2048, and only opens up beyond
that. This is a much sharper transition than the SIMD-free indirect/ directratio
in Table 10, which grows far more gradually across the same range and remains well
under 2×even atl= 4 194 304.
Second, PyTorch’s kernels generally parallelize across independent rows of a batch,
and the naive and proposed implementations are not equally well suited to this paral-
lelism. The naive implementation performs many independent sorts, one per interval,
most of them short, especially near the leaves of the depth hierarchy. In this case,
there is little work per call for several threads to split up, so more threads barely
help at smalll(its wall-clock time only fell by about 1.2×going from 1 to 8 threads
atl= 512). The proposed optimization performs a handful of large operations per
representation instead (one global sort, plus one redistribution pass per depth level).
This is coarser-grained work that several threads can split up efficiently even whenl
is small (about 1.75×faster atl= 512 going from 1 to 8 threads). This asymmetry is
largest exactly where the proposed optimization’s multithreaded advantage is biggest
(smalll), and shrinks aslgrows and the naive implementation’s individual interval
sorts become large enough to parallelize well too.
10 Conclusion
The start of this research work set out from a narrow observation: Quant’s reference
implementation, despite being fast and simple overall, commits to a single computa-
tional structure that is not well-matched to either end of the series-length spectrum on
a single CPU core. We addressed both ends. For short series, a theoretical cost model
showed that choosing between two loop orderings, rather than committing to Quant’s
fixed one, removes most of the avoidable dispatch overhead. For long series, our main
54

contribution, we replaced exact per-interval sorting with a moment-based approxima-
tion of the same quantiles via the Cornish-Fisher expansion, trading itsO(l·log(l))
sorting cost for anO(l) one. Moreover, for each mode, a calibrated dispatch heuris-
tic automatically tries to choose the faster loop order, although it does not always
succeed.
We derived a complete analysis of the computational complexities of Quant and
MomentQuant. Thanks to this analysis, it becomes much easier to compare these two
algorithms to other time series classification algorithms in terms of computational
complexity. Indeed, we provided evidence that empirical comparisons have impor-
tant limitations: the choice of a library, or even a single function from a library, can
have a substantial impact on runtime, independently of the theoretical computational
complexity.
At full UCR-archive scale, MomentQuant’s better asymptotic complexity trans-
lates into a real, measurable advantage: roughly 1.7×faster feature extraction than
exact mode, and further still against Quant’s own reference implementation, at a small
but genuine accuracy cost (under half a percentage point on average), and one that
it does not pay uniformly, since it still wins outright on over a third of the data sets
tested. That said, the practical picture is more nuanced than the asymptotic argument
alone would suggest: once downstream classifier fitting is counted, which dominates
end-to-end cost on this archive, most of the runtime gap disappears, only to re-emerge
once inference-only cost is isolated. Splitting the comparison by series length shows
a real but non-monotonic pattern rather than the clean, uniformly-widening advan-
tage a length-only reading of the cost model would predict. MomentQuant’s advantage
is therefore most relevant where feature extraction itself, not classifier fitting, is the
bottleneck: at inference time, in deployment, or wherever series are long enough that
sorting cost stops being a rounding error.
Several questions remain open. We did not enforce the Cornish-Fisher expansion’s
domain of validity per interval, nor test whether a genuinely linear-time counting sort
would close the residual gap identified for the exact mode’s alternative kernel. Both
are natural targets for tightening MomentQuant’s worst-case behavior further. More
broadly, this study evaluated MomentQuant as a drop-in replacement for Quant’s
own quantile computation. Whether the same moment-based idea transfers to other
interval- or quantile-based feature extractors is left to future work. This study is also
restricted to univariate series, following both Quant’s own reference implementation
and the univariate UCR archive used throughout this paper. Extending our cost model
to multivariate series is not immediate: treating each channel independently and con-
catenating its own quantile features, as most interval-based methods do, would simply
multiply every result derived here by the number of channels, leaving the complexity
class inlunchanged, but the dispatch-overhead constants of Section 5 and Subsec-
tion 6.3, and the resulting crossover sample size, would likely need to be recalibrated,
since channels are a natural additional axis to batch alongside the number of series
n. A multivariate design that builds intervals jointly across channels, rather than
independently per channel, would instead need a genuinely new cost model.
55

Overall, we believe this work shows that a small, principled amount of approxima-
tion, applied where it costs the least and helps the most, is a practical way to make
an already fast method for time series classification even faster.
11 Declarations
All the data sets used in this study are publicly available from the UCR Time Series
Archive (Dau et al., 2019). We would like to thank Professor Eamonn Keogh and all
the people who have contributed to this archive. The data sets can be downloaded
in several ways, either manually from the website 7 or automatically using libraries
such as theaeon(Middlehurst, Ismail-Fawaz, et al., 2024) Python package. The whole
source code supporting this study is publicly available on a GitHub repository, 8 with
detailed instructions to reproduce all the experiments. The results are also directly
available, so that other researchers can easily compare their algorithms with ours. The
repository is under the BSD 3-Clause License, making it reusable by other researchers.
Generative artificial intelligence has been used in this study, both for generating
code and analyzing the results. Nonetheless, the authors agree to be accountable for
all the materials associated with this study (this manuscript and the provided public
GitHub repository).
No funding was received for conducting this study. The authors have no relevant
financial or non-financial interests to disclose. The authors have no conflicts of interest
to declare that are relevant to the content of this article. The authors certify that
they have no affiliations with or involvement in any organization or entity with any
financial interest or non-financial interest in the matter or materials discussed in this
manuscript. The authors have no financial or proprietary interests in any material
discussed in this article.
7https://timeseriesclassification.com/dataset.php
8https://github.com/johannfaouzi/moment-quant
56

Appendix A Proofs
This appendix collects the proofs of every theorem and lemma stated in Section 4,
Section 5, and Section 6, in the order in which they appear in the main text.
Proof of Theorem 1At any levelr∈ {0, . . . , k}, Quant builds 2r base intervals. Whenr >0,
Quant also builds 2 r −1 shifted intervals. In total, Quant builds 1 + Pk r=1 2r + 2r −1 =
2k+2−k−3 intervals. However, at levelr=k, the shifted intervals are actually built if and only
if the median of the widths of the base intervals at levelkis greater than 1, which occurs if and
only ifl≥1.5·2 k. Therefore, in this case, Quant builds 2k+2 −k−3−  2k −1  = 3·2 k −k−2.
In conclusion, Quant exactly buildsN i(l, d) intervals with:
Ni(l, d) =
(
2k+2 −k−3 ifl≥1.5·2 k
3·2 k −k−2 ifl <1.5·2 k
In both cases, the dominant term is proportional to 2 k. Therefore:
Ni(l, d) = Θ

2k

□
Proof of Theorem 2At any levelr∈ {0, . . . , k}, the widths of the base intervals sum to
exactlyland the widths of the shifted intervals sum tol− ⌈l·2 −r⌉, except ifr=kand
l <1.5·2 k, in which case there are no shifted intervals, so their widths sum to 0. For any
levelr∈ {0, . . . , k}, defineϵr =⌈l·2 −r⌉ −l·2 −r. Summing over the levels, we have two
distinct cases:
• ifl≥1.5·2 k, we have:
kX
r=0

2l−l·2 −r −ϵ r  =  2k+ 2 −k ·l− kX
r=1
ϵr
• ifl <1.5·2 k, we have:
k−1X
r=0

2l−l·2 −r −ϵ r  +l=  2k−1 + 2 −(k−1)  ·l− k−1X
r=1
ϵr
Therefore, the total widthW(l, d) is equal to:
W(l, d) =




2k+ 2 −k

·l−
kX
r=1
l
l·2 −r
m
−l·2 −r

ifl≥1.5·2 k

2k−1 + 2 −(k−1)

·l−
k−1X
r=1
l
l·2 −r
m
−l·2 −r

ifl <1.5·2 k
= Θ (k·l)
In both cases, the first term is Θ(k·l), and the correction term is negative andO(k), thus
dominated by the first term:
−k≤ −
kX
r=1
l
l·2 −r
m
−l·2 −r
| {z }
∈[0,1)
≤ −
k−1X
r=1
l
l·2 −r
m
−l·2 −r
| {z }
∈[0,1)
≤0
57

Therefore:
W(l, d) = Θ (k·l)
□
Proof of Theorem 3The number of quantiles extracted for an interval of any lengthm,
denoted byn q(m) is:
nq(m, ν) = 1 +
 (m−1)
ν

= 1 + (m−1) ν −  (m−1) ν 
Summing over all theN i(l, d) intervals (Theorem 1) and using the fact thatP j mj =W(l, d)
(Theorem 2), the total number of quantiles is equal to:
Nq(l, d, ν) =
X
j
nq(mj , ν) =Ni(l, d) +W(l, d)−N i(l, d) ν − X j  mj −1 ν 
□
Proof of Theorem 4We split the proof in three parts (one for each case).
Case ν= 1. It is trivial since
n (m−1)
ν
o
= 0 for anym≥1.
Case d= 1. It is trivial because there is a single interval (for the whole series) and the single
condition is
n
l−1
ν
o
= 0, which is obtained if and only ifl−1 is exactly divisible byν.
Case d≥2 and ν≥2. For any levelr∈ {1, . . . , d−1}:
• iflis exactly divisible by 2 r, then all the intervals have the same widthl·2 −r, and
• iflis not exactly divisible by 2 r, then there are 2 r −s r base intervals of length
qr =⌊l·2 −r⌋ands r base intervals of lengthq r + 1, withs r >0.
Thus, we have the two following cases:
• If there exists anyr∈ {1, . . . , d−1}such thatlis not exactly divisible by 2r, then
bothq r −1 andq r would have to be exactly divisible byν, which implies that 1
would need to be divisible byν, which is impossible for anyν≥2.
• Iflis exactly divisible by 2 d−1, then writel=a·2 d−1 withabeing a positive
integer. Looking at the two deepest levels (d−1 andd−2), we would need both
a−1 and 2a−1 to be exactly divisible byν, which implies that 1 would need to
be divisible byν, which is impossible forν≥2.
For each individual term, we have:
0≤
 mj −1
ν

≤ ν−1 ν
Summing over all theN i(l, d) provides the bound:
0≤E(l, d, ν)≤ ν−1 ν ·N i(l, d)
Forl=a·2 d−1 ·ν, withabeing any positive integer, for any levelr∈ {0, . . . , d−1}, all
the intervals of levelrhave the same widtha·2 d−r−1 ·ν, and we have:
(
a·2 d−r−1 ·ν−1
ν
)
= ν−1 ν
58

Summing over all the intervals, we have:
E(a·2 d−1 ·ν, d, ν) =ν−1 ν ·N i(l, d)
□
Proof of Theorem 5An interval built at levelrhas width 1 only ifr=k: for any levelr < k,
both 2r ≤2 k−1 andl≥2 k hold, sol·2 −r ≥2, hence every base interval at levelrhas width
⌊l·2 −r⌋ ≥2. Every shifted interval at levelrreuses a base interval’s width at that level
(shown below), hence also has width at least 2.
Ifk=d−1<⌊log 2(l)⌋, thenl≥2 k+1, so⌊l·2 −k⌋ ≥2 as well, and every interval at
levelk(base or shifted) has width at least 2:N (1) i (l, d) = 0.
Otherwise,k=⌊log 2(l)⌋, so 2 k ≤l <2 k+1. Writel= 2 k +ρwith 0≤ρ <2 k. The base
intervals at levelkare given by indices i =⌊i·l·2 −k⌋fori= 0, . . . ,2k, which partitions [0, l]
into 2 k pieces of which exactlyρhave width 2 and the remaining 2 k −ρ= 2 k+1 −lhave
width 1.
Ifl <1.5·2 k (i.e.,ρ <2 k−1), no shifted intervals are built at levelk(Theorem 1), so
N (1) i (l, d) = 2k+1 −l.
Ifl≥1.5·2 k (i.e.,ρ≥2 k−1 ≥1, sincek≥1 whenever shifted intervals exist), shifted
intervals are built at levelkby shifting and then dropping the last of the 2 k base intervals
(Theorem 1). The last base interval has width indices2k −indices 2k−1 =l−

l− ⌈l·2−k⌉  =
⌈l·2 −k⌉= 2 (using⌊x−y⌋=x− ⌈y⌉for integerx, andρ >0). Consequently, the 2 k −1
shifted intervals reuse the base intervals’ widths minus this one dropped width-2 instance:
ρ−1 of width 2 and 2 k −ρof width 1, contributing 2 k −ρ= 2 k+1 −lfurther length-one
intervals. In total:N (1) i (l, d) = 2·  2k+1 −l  .□
Proof of Theorem 6At any levelr∈ {0, . . . , k}, there are exactly 2r intervals of lengthl·2 −r.
Their total sort cost is thus:
base ideal(r) = 2r ·l·2 −r ·log 2(l·2 −r) =l·(log 2(l)−r)
At any levelr∈ {1, . . . , k−1}, there are exactly 2r −1 shifted intervals of lengthl·2 −r.
Their total sort cost is thus:
shift ideal(r) =

2r −1  ·l·2 −r ·log 2(l·2 −r) =  1−2 −r  ·l·(log 2(l)−r)
At levelr=k, shifted intervals are only included if the median width of the base intervals
at levelkis greater than 1, which occurs if and only ifl≥1.5·2 k. The above formula for
shift ideal(r) actually still holds forr=kforl= 2 k because log 2(2k)−k= 0. Thus, we can
use it for anylin this setting because we assumed thatlis exactly divisible by 2 k.
Therefore, at any levelr∈ {1, . . . , k}:
base ideal(r) + shift ideal(r) =l·(log 2(l)−r)
h
1 + (1−2 −r) i =l·(log 2(l)−r)·  2−2 −r 
Thus, the total sort costT r∗s (l, d) is proportional to:
T r∗ s (l, d)∝base ideal(0) +
kX
r=1
base ideal(r) + shift ideal(r)
∝l·log 2(l) +
kX
r=1
l(log 2(l)−r)·

2−2 −r

59

∝l·log 2(l)·
"
1 +
kX
r=1
(2−2 −r)
#
−l·
kX
r=1
r·(2−2 −r)
∝l·log 2(l)·
h
2k+ 2 −k
i
−l
h
k2 +k−2 + (k+ 2)·2 −k
i
T r∗ s (l, d)∝l· h 2k+ 2 −k  ·log 2(l)−  k2 +k−2 + (k+ 2)·2 −k i
Definingc 1 as the empirical time-per-unit-of-sort-work constant, we obtain the desired result:
T r∗ s (l, d) =c1 ·l· h 2k+ 2 −k  ·log 2(l)−  k2 +k−2 + (k+ 2)·2 −k i
□
Proof of Theorem 7For any levelr∈ {1, . . . , k}, all the interval lengths might not be equal
tol·2 −r since it might not be an integer. Letq r =⌊l·2 −r⌋ands r (with 0≤s r <2 r) be
the quotient and the remainder of the Euclidean division oflby 2 r respectively. With the
implementation chosen in Quant, there are exactly 2 r −s r base intervals of lengthq r ands r
base intervals of lengthq r + 1. The width of the last base interval, denoted byw r, is equal
toq r + 1 ifs r >0 elseq r. We mention this information because the total width of all the
shifted intervals is equal to the total width of the first 2 r −1 base intervals (i.e., all the base
intervals except the last one). Indeed, the 2 r −1 shifted intervals are the first 2 r −1 base
intervals shifted by⌈l·2 −r−1⌉.
To simplify the equations, we definef(m) =m·log 2(m) as the sort cost of an interval of
lengthm. For any levelr∈ {1, . . . , k}, the total sort cost of the base intervals is:
base(r) =

2r −s r  ·f(q r) +s r ·f(q r + 1)
For any levelr∈ {1, . . . , k−1}, the total sort cost of the shifted intervals is:
shift(r) = base(r)−f(w r)
Similarly to the proofs of Theorem 1 and Theorem 2, we need to distinguish two cases:
• ifl <1.5·2 k, there are no shifted intervals at levelr=k, thus:
shift(k) = 0
• ifl≥1.5·2 k, there are shifted intervals at levelr=k, and the formula above still
holds, thus:
shift(k) = base(k)−f(w k)
Case l≥1.5·2 k. Summing over the levels, the total sort costT(l) is equal to:
T r s (l, d) =f(l) +
kX
r=1
2·base(r)−f(w r)
Now, we need to bound the gap between the ideal case (whenlis exactly divisible by 2 k)
and the arbitrary case (whenlis not exactly divisible by 2 r). Let’s recall the total sort cost
of the all the base intervals at any levelr∈ {0, . . . , k}in the ideal case:
base ideal(r) = 2r ·f(l·2 −r)
At levelr= 0, the whole series is used, so the ideal and arbitrary cases exactly match:
base(0) = base ideal(0) =f(l)
60

Sincefis convex, by the standard Lagrange remainder for linear interpolation, forθ=
sr ·2 −r ∈[0,1), there existsξ∈(q r, qr + 1) such that:
(1−θ)·f(q r) +θ·f(q r + 1)−f(q r +θ) = f ′′(ξ) 2 ·θ·(1−θ)
Multiplying by 2 r both sides of the equation, we have:
0≤base(r)−base ideal(r) = 2r · f ′′(ξ) 2 ·θ·(1−θ)
Using the facts thatθ·(1−θ)≤1/4 (because 1/4 is the maximum value of functionx7→
x·(1−x), attained at 1/2) and thatf ′′(ξ)≤f ′′(qr)≤f ′′(1) = 1/log(2) (becausef ′′(m) =
1/(m·log(2)) is decreasing), we have:
0≤base(r)−base ideal(r)≤ 2r
8 log(2)
Summing over all the levels, we have:
0≤
kX
r=0
base(r)−base ideal(r)≤
kX
r=1
2r
8 log(2) =O

2k

Now, let’s focus on the shifted intervals, and more specifically onf(w r), and let’s compare
it to its ideal counterpartf(l·2 −r). Recall thatq r =⌊l·2 −r⌋and thatw r is equal to eitherq r
(ifs r = 0) orq r + 1 (ifs r >0). Thus, we havel·2 −r ∈[q r, qr + 1] andw r ∈[q r, qr + 1]. Since
fis differentiable, using the mean value inequality and the fact thatfis convex, we have:
|f(w r)−f(l·2 −r)| ≤max
[qr,qr+1]
|f ′|=f ′(qr + 1) = log2(qr + 1) + 1 log(2)
Sinceq r =⌊l·2 −r⌋ ≤l·2−r, we have:
log2(qr + 1)≤log 2(l·2 −r + 1)≤log 2(l·2 −r) + log2(2) = log2(l)−r+ 1
Summing over all the levels, we have:
kX
r=1

log2(qr + 1) + 1 log(2)  ≤k·  log2(l) + 1 + 1 log(2)  − k·(k+ 1) 2 =O(k·log(l))
Putting it together, the total deviation from the ideal case is:
T r s (l, d)−T r∗ s (l, d) =c1 ·
 kX
r=1
(base(r)−base ideal(r)) + (shift(r)−shift ideal(r))
!
= 2·c 1 ·
 kX
r=1
(base(r)−base ideal(r)) +
kX
r=1
(f(l·2 −r)−f(w r))
!
T r s (l, d)−T r∗ s (l, d) =c1 · O  2k  +O(k·log(l))
Thus, the total sort cost for an arbitrary lengthlis:
T r s (l, d) =c1·l· h 2k+ 2 −k  ·log 2(l)−  k2 +k−2 + (k+ 2)·2 −k i +O  2k  +O(k·log(l))
Case l <1.5·2 k. In this case, the correction term only removes the following positive term:
base(k)−f(w k) =

2k −s k

·f(q k) +s k ·f(q k + 1)−f(w k)
Therefore, it does not change the bound obtained whenl≥1.5·2 k.
General case, any arbitrary l. Since the result holds for both cases, we have:
T r s (l, d) =c1·l· h 2k+ 2 −k  ·log 2(l)−  k2 +k−2 + (k+ 2)·2 −k i +O  2k  +O(k·log(l))
□
61

Proof of Theorem 8The proof starts with the results of Theorem 7:
T r s (l, d) =l· h 2k+ 2 −k  ·log 2(l)−  k2 +k−2 + (k+ 2)·2 −k i +O  2k  +O(k·log(l))
withk=e−1. We split the proof in two parts (one for each case).
Saturated regimeIn the saturated regime (l≥2 d−1), we havek=d−1≤log 2(l). We
derive both an upper bound and a lower bound. For the first term, we have:

2k+ 2 −k

·log 2(l)≤(2k+ 1) log 2(l) =O(d·log(l))
0≤

k2 +k−2 + (k+ 2)·2 −k

=O

k2

⊆ O(d·log(l))
Therefore, we have:
l·
h
2k+ 2 −k

·log 2(l)−

k2 +k−2 + (k+ 2)·2 −k
i
=O(d·l·log(l))
Both correction terms being dominated by the first term, we obtain the desired upper bound:
T r s (l, d) =O(d·l·log(l))
For the lower bound, let’s view the bracketed expression as a function ofx= log 2(l):
g(x) =

2k+ 2 −k

·x−

k2 +k−2 + (k+ 2)·2 −k

Sincegis affine inxwith slope 2k+ 2 −k ≥k, and sincek≤log 2(l) in the saturated regime,
for anyx≥kwe have:
g(x) =g(k) + (x−k)·

2k+ 2 −k

≥g(k) + (x−k)·k
We now lower-boundg(k) =k 2 −k+ 2−2 1−k for every integerk≥0. Fork= 0, we have
g(0) = 0 = 0 2/2. Fork= 1, we haveg(1) = 1≥1/2 = 1 2/2. Fork≥2, using 2 1−k ≤2, we
have:
g(k)≥k 2 −k+ 2−2 =k(k−1)≥ k2
2
In every case,g(k)≥k 2/2. Combining with the slope bound above, for anyx≥k:
g(x)≥ k2
2 + (x−k)·k=kx− k2 2 ≥ kx 2
where the last step usesx≥k. Substitutingx= log 2(l), this holds for everylin the saturated
regime (i.e. everyl≥2 k), not only atl= 2 k:

2k+ 2 −k

·log 2(l)−

k2 +k−2 + (k+ 2)·2 −k

≥ k·log 2(l) 2
Therefore, we have:
l·
h
2k+ 2 −k

·log 2(l)−

k2 +k−2 + (k+ 2)·2 −k
i
= Ω(d·l·log(l))
Once again, both correction terms being dominated by the first term, we obtain the desired
lower bound:
T r s (l, d) = Ω (d·l·log(l))
With both the upper and lower bounds matching, we have:
T r s (l, d) = Θ (d·l·log(l))
Unsaturated regimeIn the unsaturated regime (l <2 d−1), we havek=⌊log 2(l)⌋,
hence log2(l) =k+{log 2(l)}. Focusing on the terms inside the brackets, we have: 
2k+ 2 −k

·log 2(l)−

k2 +k−2 + (k+ 2)·2 −k

62

=

2k+ 2 −k

·(k+{log 2(l)})−

k2 +k−2 + (k+ 2)·2 −k

=k 2 + (2k· {log2(l)} −k+ 2)| {z }
=O(k)
+ 2−k({log2(l)} −2)| {z }
o(1)
=k 2 +O(k 2) +o(1)
= Θ

k2

= Θ

(log(l))2

Therefore, for the first term, we have:
l·
h
2k+ 2 −k

·log 2(l)−

k2 +k−2 + (k+ 2)·2 −k
i
= Θ

l·(log(l)) 2

Moreover, both correction terms are dominated by the first term:
O

2k

=O(l)
O(k·log(l)) =O

(log(l))2

Therefore, we have:
T r s (l, d) = Θ  l·(log(l)) 2 
□
Proof of Theorem 9An interval of width 1 contributes no extraction cost: its single value is
copied directly, with no sorting, no quantile interpolation, and no mean computed. For every
other interval, of widthm >1, the extraction cost consists of two terms:
• the cost of extracting the quantiles, which is proportional to the number of quantiles,
and
• the cost of computing the mean of the subseries, which is proportional to the series
lengthm.
Thus, the cost of the extraction step for a single sorted subseries of widthm >1 is:
extraction(m) =c 2 ·n q(m, ν) +c3 ·m
withc 2 being the empirical per-quantile extraction cost (in seconds/quantile), andc 3 being
the empirical per-element extraction cost (in seconds/element). Summing over all the intervals
of width strictly greater than 1 (Theorem 5), we have:
T r e (l, d, ν) =c2 ·N >1 q (l, d, ν) +c3 ·W >1(l, d)
□
Proof of Theorem 10We first show that restricting the count and the total width to intervals
of width strictly greater than 1 does not change their asymptotic order. By Theorem 5,
N (1) i (l, d)≤2·2 k+1 =O  2k  , andN i(l, d) = Θ  2k  (Theorem 1), so:
N >1 i (l, d) =Ni(l, d)−N (1) i (l, d) = Θ  2k 
Likewise, sinceW(l, d) = Θ(k·l) (Theorem 2) andN (1) i (l, d) =O  2k  =O(l)⊆ O(k·l), we
have:
W >1(l, d) =W(l, d)−N(1) i (l, d) = Θ(k·l)
63

For any lengthm≥1 and anyν≥1, we have:
1≤n q(m, ν) = 1 +
 (m−1)
ν

≤1 + m ν ≤1 +m
Summing over all theN >1 i (l, d) intervals of width strictly greater than 1, we have:
N >1 i (l, d)≤N >1 q (l, d, ν)≤N>1 i (l, d) +W>1(l, d)
Using Theorem 9, we have:
c2 ·N >1 i (l, d) +c3 ·W >1(l, d)≤T r e (l, d, ν)≤c2 ·N >1 i (l, d) + (c2 +c 3)·W >1(l, d)
SinceN >1 i (l, d) = Θ  2k  andW >1(l, d)≥l−N (1) i (l, d) = Ω(l) (asW(l, d)≥lby definition
andN (1) i (l, d) =O(2k) =O(l)), we haveN >1 i (l, d) =O  W >1(l, d)  , hence:
T r e (l, d, ν) = Θ  W >1(l, d)  = Θ(k·l) = Θ(e·l)
Sincee=din the saturated regime, ande=⌊log 2 l⌋+ 1 in the unsaturated regime, we
conclude:
T r e (l, d, ν) =
(
Θ(d·l) ifl≥2 d−1 (saturated regime)
Θ(l·log(l)) ifl <2 d−1 (unsaturated regime)
□
Proof of Lemma 1Quant processes each non-trivial interval by first sorting its values and
then extracting the (interpolated, possibly centered) quantiles from the sorted values. These
are the only two operations performed on an interval, and they are applied sequentially, so the
processing cost of a single interval is the sum of its sort cost and its extraction cost. Summing
over all the intervals (Theorem 1) preserves this additivity, givingT r(l, d, ν) =Trs (l, d) +
T re (l, d, ν), whereTrs (l, d) andTre (l, d, ν) are respectively the total sort cost (Theorem 7) and
the total extraction cost (Theorem 9).□
Proof of Theorem 11By Lemma 1, we have:
T r(l, d, ν) =Tr s (l, d) +Tr e (l, d, ν)
We recall the results of Theorem 8 and Theorem 10 below:
T r s (l, d) =
(
Θ (d·l·log(l)) ifl≥2 d−1 (saturated regime)
Θ

l·(log(l)) 2

ifl <2 d−1 (unsaturated regime)
T r e (l, d, ν) =
(
Θ(d·l) ifl≥2 d−1 (saturated regime)
Θ(l·log(l)) ifl <2 d−1 (unsaturated regime)
In the saturated regime, we haved≤ ⌊log 2(l)⌋+ 1, sod·l=o(d·l·log(l)), thus the
extraction term is asymptotically negligible next to the sort term.
In the non-saturated regime, we havel·log(l) =o

l·(log(l)) 2

, thus the extraction term
is also asymptotically negligible next to the sort term.
Therefore, in both regimes, the extraction term is asymptotically negligible next to the
sort term, leading to the desired result:
T r(l, d, ν) =Tr s (l, d) =
(
Θ (d·l·log(l)) ifl≥2 d−1 (saturated regime)
Θ

l·(log(l)) 2

ifl <2 d−1 (unsaturated regime)
□
64

Proof of Theorem 12Using Theorem 6 and replacingkwith 5, we have:
T r s (l,6) =c 1 ·l·
 321
32 ·log 2(l)− 903 32 
Replacinglwith 2 b, we have:
T r s

2b,6  =c 1 ·2 b ·  321 32 ·b− 903 32  =c 1 ·2 b−5 ·(321b−903) = 3·c 1 ·2 b−5 ·(107·b−301)
□
Proof of Theorem 13The starting point of the proof is Theorem 9,T re (l, d, ν) =
c2 ·N >1q (l, d, ν) +c3 ·W >1(l, d), together with Theorem 3,N q(l, d, ν) =N i(l, d) +
(W(l, d)−N i(l, d))/ν−E(l, d, ν), whereE(l, d, ν) =P j {(mj −1)/ν}is summed over all
the base and shifted intervals, and Theorem 5, which givesN (1) i (2b,6) = 0 for everyb≥6
considered below (so thatN >1q =N q andW >1 =Wthroughout theb >5 case), and
N (1) i (32,6) = 32̸= 0 forb= 5, treated separately at the end.
Sincel= 2 b is divisible by 2 r for everyr∈ {0, . . . , b}, and in particular for every
r∈ {0, . . . , k}withk= min(5, b) = 5 (asb≥5), every level-rcorrection term in
Theorem 2 vanishes exactly, soN i(2b,6) andW(2 b,6) reduce to the leading terms of
Theorem 1 and Theorem 2. For the same reason, every base and shifted interval at levelr
has the exact same width 2 b−r, so the corresponding term ofE(2 b,6,4) is identical across
all of them, and the sum over intervalsjcollapses to a sum over levelsr:E(2 b,6,4) =Pk
r=0

2r+1 −1  n (2b−r −1)/4 o if levelkhas shifted intervals (i.e. 2 b >1.5·2 k), or the same
sum truncated tor∈ {0, . . . , k−1}if it does not (i.e. 2b = 2k), per the proof of Theorem 1.
There are two different cases:b= 5 andb >5. We start with the latter.
Case b >5. Herel= 2 b >1.5·2 5 = 48 (sinceb >5 means 2 b ≥64), so Theorem 1 gives
Ni(2b,6) = 2 7 −5−3 = 120, Theorem 2 givesW(2 b,6) = (2·5 + 2 −5)·2 b = 321 32 ·2 b, and level
k= 5 has shifted intervals, soE(2 b,6,4) = P5 r=0  2r+1 −1  n (2b−r −1)/4 o . Substituting
into Theorem 3 and Theorem 9, we have:
T r e

2b,6,4  =c 2 ·120· 3 4 + 2b ·  321 32   c2 4 +c 3  −c 2 · 5X r=0  2r+1 −1  ( 2b−r −1 4 )
T r e

2b,6,4  = 90·c 2 + 2b · 321 128 ·c 2 + 2b · 321 32 ·c 3 −c 2 5X r=0  2r+1 −1  ( 2b−r −1 4 )
We have two cases to distinguish to simplify the last term. For anyr∈ {0, . . . ,5}:
• ifb−r= 1, then  (2b−r −1)/4 	 = 0.25,
• ifb−r≥2, then  (2b−r −1)/4 	 = 0.75.
Thus, we have:
5X
r=0

2r+1 −1  ( 2b−r −1 4 ) = ( 0.75×(1 + 3 + 7 + 15 + 31) + 0.25×63 = 58.5 ifb= 6 0.75×120 = 90 ifb≥7
Simplifying the formula with the value of the last term derived above, we have:
T r e

2b,6,4  = ( 192·c 2 + 642·c 3 ifb= 6 321·  2b−7 ·c 2 + 2b−5 ·c 3  ifb≥7
65

Case b= 5. Herel= 32 = 2 5 <1.5×2 5 = 48, so Theorem 1 givesN i(32,6) = 3×32−5−2 =
89, Theorem 2 givesW(32,6) = (9 + 2 −4)×32 = 290, and levelk= 5 has no shifted
intervals here, soE(32,6,4) = P4 r=0  2r+1 −1  n (25−r −1)/4 o , which, using the same
case-split as above withb= 5, evaluates to 27.25. Substituting into Theorem 3, we have
Nq(32,6,4) = 89·3/4+(290−89×3/4×4/3)/4−27.25, which simplifies toN q(32,6,4) = 112.
Unlike theb >5 case, herek= 5 =⌊log 2(32)⌋is exactly the deepest level reached
(Theorem 1’s proof), so this case has trivial (length-1) intervals, and Theorem 9 actually
applies. Since 32<1.5×2 5 = 48, Theorem 5 givesN (1) i (32,6) = 2 6 −32 = 32, so:
N >1 i (32,6) = 89−32 = 57
W >1(32,6) = 290−32 = 258
N >1 q (32,6,4) = 112−32 = 80
Substituting into Theorem 9, we have:
T r e (32,6,4) =c 2 ·N >1 q (32,6,4) +c 3 ·W >1(32,6,4) = 80·c 2 + 258·c 3
General case b≥5. We conclude:
T r e

2b,6,4  =



80·c 2 + 258·c 3 ifb= 5
192·c 2 + 642·c 3 ifb= 6
321·

2b−7 ·c 2 + 2b−5 ·c 3

ifb≥7
□
Proof of Theorem 14We use Theorem 12 to derive the total sort cost forb= 5 andb= 6,
Theorem 13 to derive the total extraction cost, sum both terms and simplify the expressions
to obtain the desired result:
T r

2b,6,4  =



702·c 1 + 80·c 2 + 258·c 3 ifb= 5
2046·c 1 + 192·c 2 + 642·c 3 ifb= 6
2(b−5) ·

3·c 1 ·(107·b−301) + 321 4 ·c 2 + 321·c 3

ifb≥7
□
Proof of Lemma 2The raw representation is the series itself, of lengthl 1(l) =l. The first-
order difference of a length-lseries has lengthl−1. Quant smooths it with a length-5 centered
moving average after padding both ends by 2 (using edge-value padding), which restores the
original (post-differencing) length, so the smoothed first-difference representation has length
l2(l) =l−1. The second-order difference (the first-order difference applied twice) removes one
point at each step, giving lengthl 3(l) =l−2. The one-sided magnitude spectrum of the real
discrete Fourier transform of a length-lreal sequence has⌊l/2⌋+ 1 non-redundant frequency
bins (indices 0 through⌊l/2⌋), sol 4(l) =⌊l/2⌋+ 1. We requirel≥3 so thatl 3(l)≥1, i.e., so
that every representation is well-defined and non-empty.□
Proof of Theorem 15Quant processes the four representations of a series independently and
sequentially, applying the same interval-building-and-sorting procedure to each. The total
sort cost is therefore exactly the sum, over the four representations, of the per-representation
sort cost. By Remark 1, the per-representation sort cost of representationpis given by
Theorem 7 evaluated at lengthl p(l) (Lemma 2), giving the desired result.□
66

Proof of Theorem 16Identical to the proof of Theorem 15, using Theorem 9 in place of
Theorem 7 for the per-representation extraction cost. Unlike Theorem 7, Theorem 9 is exact
(it carries noO(·) correction term), so the total is exact as soon asN >1q andW >1 are
evaluated exactly via Theorem 5.□
Proof of Theorem 17The total processing cost is the sum of the total sort cost (Theorem 15)
and the total extraction cost (Theorem 16), exactly as in Lemma 1.□
Proof of Theorem 18We first show that each representation’s length is within a bounded
factor ofl: by Lemma 2,l 1(l) =l,l 2(l) =l−1, andl 3(l) =l−2 differ fromlby an additive
constant, andl 4(l) =⌊l/2⌋+ 1 satisfiesl/2≤l 4(l)≤l/2 + 1. For everypand everyl≥4, we
therefore havel/2≤l p(l)≤l, i.e.,l p(l) = Θ(l).
Consequently, log 2(lp(l)) = log 2(l) +O(1) for everyp. Writingk p = min(d−
1,⌊log 2(lp(l))⌋) (the exponent Theorem 7 associates with representationp) and recalling
k= min(d−1,⌊log 2(l)⌋) (the exponent for the raw representation), the bound above gives
kp ∈ {k−1, k, k+ 1} ∩ {0, . . . , d−1}for everypand everyl≥4: a bounded (O(1)) deviation
fromk. Equivalently,e p :=k p + 1 =e+O(1), withe p ≤dalways.
We now bound each term of Theorem 15 and Theorem 16 using Theorem 8 and
Theorem 10 applied atl p(l) in place ofl:
T rp s (lp(l), d) = Θ (lp(l)·e p ·log(l p(l))), T rp e (lp(l), d, ν) = Θ(ep ·l p(l))
Sincel p(l) = Θ(l) ande p =e+O(1) with bothe p andebounded above bydand below
by 1 (so that anO(1) additive shift is also a Θ(1) multiplicative factor whenevere= Θ(1),
and is asymptotically negligible whenevere= Θ(logl)→ ∞), we havee p = Θ(e) and
log2(lp(l)) = Θ(log(l)). Substituting:
T rp s (lp(l), d) = Θ(l·e·log(l)), T rp e (lp(l), d, ν) = Θ(e·l)
for everyp∈ {1,2,3,4}. Summing four terms of matching Θ-order does not change the order
(the constant factor 4 is absorbed into the Θ), so:
Ts(l, d) =
4X
p=1
T rp s (lp(l), d) = Θ(l·e·log(l)), T e(l, d, ν) =
4X
p=1
T rp e (lp(l), d, ν) = Θ(e·l)
Sincee·l=O(l·e·log(l)) (as log 2(l)≥1 forl≥2),T e(l, d, ν) is dominated byTs(l, d), exactly
as in the proof of Theorem 11, so, by Theorem 17,T(l, d, ν) =T s(l, d) +Te(l, d, ν) = Θ(l·e·
log(l)). Splitting by which term wins in the definition oferecovers the saturated/unsaturated
case split, identical in form to Theorem 11.□
Proof of Theorem 19The interval-outer implementation performs exactlyN i(l, d) iterations
of its outer loop (Theorem 1), one per interval, but only theN >1 i (l, d) iterations visiting an
interval of width strictly greater than 1 (Theorem 5) dispatch the vectorized sort-and-extract
call thatκ (I) (l) accounts for: an iteration visiting a width-1 interval instead copies a single
value directly, at a cost that does not scale withnthe way the sort-and-extract dispatch
cost does, and which Theorem 9 already established is otherwise negligible for the purpose
of this cost model. Summing over theN >1 i (l, d) sort-and-extract iterations gives the setup
termN >1 i (l, d)·κ(I) (l).
Within a single interval’s vectorized call, NumPy sorts and extracts from each of the
nrows of the (n×m) sub-array independently, at the same per-row cost as sorting and
extracting from a single length-marray. Summing this cost across thenrows, and then
67

across theN i(l, d) intervals, therefore reproduces exactlyntimes the per-series sort-work and
extraction accounting of Theorem 7 and Theorem 9, evaluated with this implementation’s
own constantsc (I) 1 , c(I) 2 , c(I) 3 . This gives the marginal termn·T r,(I)(l, d, ν).□
Proof of Theorem 20The series-outer implementation performs exactlyniterations of its
outer loop, one per series. Each iteration dispatches a single compiled call that processes all
Ni(l, d) intervals of that series internally. Because the loop over intervals is compiled rather
than interpreted, it contributes no dispatch overhead of its own, so the only cost per iteration
beyond the compiled kernel’s own work is the single call-dispatch overheadκ(S)(l) of invoking
it, a quantity that may itself vary withl(e.g., through the cost of marshalling anl-dependent
amount of data into and out of the compiled call). The compiled kernel implements the
same sort-then-extract algorithm accounted for in Theorem 7 and Theorem 9, so its cost for
one series is exactlyT r,(S)(l, d, ν), using this implementation’s own constantsc(S) 1 , c(S) 2 , c(S) 3 .
Summing the per-iteration costκ (S)(l) +T r,(S)(l, d, ν) over thenindependent series gives
the result. □
Proof of Theorem 21BothT r,(I) andT r,(S) are affine inn(Theorem 19, Theorem 20):
T r,(I)(n) =A I +B I ·nandT r,(S)(n) =B S ·n, withA I ≥0.
IfB S ≤B I : sinceA I ≥0, we haveT r,(S)(n) =B S ·n≤B I ·n≤A I +B I ·n=T r,(I)(n)
for everyn≥1.
IfB S > BI : the differenceT r,(I)(n)−T r,(S)(n) =A I −(B S −B I )·nis a strictly
decreasing affine function ofn, non-negative atn= 0 (sinceA I ≥0), and equal to zero
atn=n ∗(l, d, ν) :=AI /(BS −B I ). Therefore,T r,(I)(n)> T r,(S)(n) forn < n ∗, and
T r,(I)(n)< Tr,(S)(n) forn > n∗.□
Proof of Theorem 22Computing the moments of a single interval of widthmrequires exactly
one Welford/Pebay pass over itsmelements (Subsection 6.1): each element is visited exactly
once, and each visit performs the same fixed number of arithmetic operations regardless of
mor of the element’s position within the interval. Charging this fixed per-element work at
rate ˜c1, the cost of computing the moments of a single interval of widthmis exactly ˜c 1 ·m,
with no further dependence onmor ond. Summing over allN i(l, d) intervals, and usingP
j mj =W(l, d) (Theorem 2), the total moment computation cost is exactly:
eT r m(l, d) = ˜c1 · X
j
mj = ˜c1 ·W(l, d)
□
Proof of Theorem 23By Theorem 22, eT rm(l, d) = ˜c1 ·W(l, d), and by Theorem 2,W(l, d) =
Θ(k·l) = Θ(e·l) withk=e−1. Therefore, eT rm(l, d) = Θ(e·l). Splitting by regime as in
the proof of Theorem 8 (e=din the saturated regime,e=⌊log 2(l)⌋+ 1 = Θ(log(l)) in the
unsaturated regime) gives the stated two cases.□
Proof of Theorem 24For a single interval whose moments have already been computed
(Theorem 22), the extraction step consists of two sub-steps, which the two constants keep
separate precisely because they behave differently on trivial (length-1, kind = 0) intervals.
Converting the raw moments (m, M 2, M3, M4) into (variance, skewness, excess kurtosis)
(Subsection 6.1) is applied uniformly to every interval, including trivial ones, at the fixed
68

per-interval rate ˜c3, since Quant computes it as a single element-wise pass over the moments
ofallN i(l, d) intervals at once, with no branch skipping trivial ones. Evaluating the Cornish-
Fisher expansion, by contrast, is applied only to a trivial interval’s non-existent request for an
approximated quantile. A trivial interval’s single requested position is instead filled directly
from its (degenerate) mean, exactly as its exact-mode counterpart is filled directly from the
interval’s raw value (Theorem 9). Thus, only the interior, genuinely-evaluated positions of
theN >1q (l, d, ν) non-trivial-interval quantiles (Theorem 5) are charged at rate ˜c 2. There-
fore, the extraction cost for a single non-trivial interval withn q(m, ν) requested quantiles
is ˜c2 ·n q(m, ν) + ˜c3, while a trivial interval costs only ˜c 3 (the conversion, still performed,
but no Cornish-Fisher evaluation). Summing over allN i(l, d) intervals for the ˜c3 term, and
over the non-trivial ones only for the ˜c2 term, and using P j:m j >1 nq(mj , ν) =N>1q (l, d, ν)
(Theorem 5), we obtain:
eT r e (l, d, ν) = ˜c2 ·N >1 q (l, d, ν) + ˜c3 ·N i(l, d)
□
Proof of Theorem 25By the same per-interval argument as in the proof of Theorem 10 (1≤
nq(m, ν)≤mfor every interval), restricted to theN >1 i (l, d) non-trivial intervals:N>1 i (l, d)≤
N >1q (l, d, ν)≤N>1 i (l, d) +W(l, d) (the upper bound usingW(l, d), rather than the tighter
W >1(l, d), sinceW>1(l, d)≤W(l, d)). Combined with Theorem 24, this gives:
˜c2 ·N >1 i (l, d) + ˜c3 ·N i(l, d)≤ eT r e (l, d, ν)≤˜c2 ·  N >1 i (l, d) +W(l, d)  + ˜c3 ·N i(l, d)
SinceN i(l, d) =O(l) =O(W(l, d)) (Theorem 1, andW(l, d)≥lby definition) and likewise
N >1 i (l, d)≤N i(l, d) =O(W(l, d)), both the lower and upper bounds above are Θ(W(l, d)),
exactly as in the proof of Theorem 10, so:
eT r e (l, d, ν) = Θ(W(l, d)) = Θ(e·l)
using Theorem 2. Splitting by regime as in Theorem 10 gives the stated two cases.□
Proof of Lemma 3The approximate algorithm processes each interval by first computing its
moments and then extracting the (Cornish-Fisher-approximated, possibly centered) quantiles
from those moments. These are the only two operations performed on an interval, applied
sequentially, exactly as in the proof of Lemma 1 for the exact algorithm’s sort-then-extract
processing. Summing over all the intervals (Theorem 1) preserves this additivity.□
Proof of Theorem 26By Lemma 3, eT r(l, d, ν) =eT rm(l, d) +eT re (l, d, ν). By Theorem 23 and
Theorem 25, both terms are Θ(e·l), unlike the exact algorithm (Theorem 11), where the sort
term dominates the extraction term. Here the two terms are already of the same order, so
their sum is Θ(e·l) as well. Splitting by regime as in Theorem 8 gives the stated two cases.□
Proof of Theorem 27Quant computes the moments of the four representations of a
series independently and sequentially, applying the same interval-building-and-moment-
computation procedure to each. The total moment computation cost is therefore exactly the
sum, over the four representations, of the per-representation moment cost. By Remark 9, the
per-representation cost of representationpis given by Theorem 22 evaluated at lengthl p(l)
(Lemma 2), giving the desired result.□
69

Proof of Theorem 28Identical to the proof of Theorem 27, using Theorem 24 in place of
Theorem 22 for the per-representation extraction cost. As in Theorem 16, Theorem 24 is
exact (it carries noO(·) correction term), so the total is exact as soon asN >1q andN i are
evaluated exactly via Theorem 5 and Theorem 1.□
Proof of Theorem 29The total processing cost is the sum of the total moment computation
cost (Theorem 27) and the total extraction cost (Theorem 28), exactly as in Lemma 3.□
Proof of Theorem 30By the proof of Theorem 18,l p(l) = Θ(l) and, writinge p :=
min(d,⌊log 2(lp(l))⌋+ 1), we havee p = Θ(e) for everyp∈ {1,2,3,4}. Applying Theorem 23
and Theorem 25 atl p(l) in place ofl:
eT rp m (lp(l), d) = Θ(ep ·l p(l)) = Θ(e·l), eT rp e (lp(l), d, ν) = Θ(ep ·l p(l)) = Θ(e·l)
for everyp. Summing four terms of matching Θ-order does not change the order (the constant
factor 4 is absorbed into the Θ), so, using Theorem 27 and Theorem 28:
eTm(l, d) =
4X
p=1
eT rp m (lp(l), d) = Θ(e·l), eTe(l, d, ν) =
4X
p=1
eT rp e (lp(l), d, ν) = Θ(e·l)
By Theorem 29, eT(l, d, ν) =eTm(l, d) +eTe(l, d, ν) is the sum of two terms of the same order,
hence itself Θ(e·l). Splitting by which term wins in the definition ofegives the stated two
cases, identical in form to Theorem 23 and Theorem 25.□
Proof of Theorem 31For a single representationp, the moment computation of all
Ni(lp(l), d) intervals (Theorem 22) is dispatched as a single call, independent ofn i. It is the
subsequent per-interval extraction step, converting each interval’s moments into its requested
quantiles, that the interval-outer implementation runs asNi(lp(l), d) separate outer-loop iter-
ations, one per interval (Theorem 1, evaluated atl p(l)), mirroring the proof of Theorem 19.
Of these, only theN >1 i (lp(l), d) iterations visiting a non-trivial interval (Theorem 5) dispatch
a genuine Cornish-Fisher evaluation call. An iteration visiting a trivial interval instead copies
its already-known mean directly, at a cost this proof, like that of Theorem 19 and Theorem 24,
treats as negligible. This gives the setup termN >1 i (lp(l), d)·˜κ(I) (lp(l)) for representationp.
The moment computation and (for non-trivial intervals) Cornish-Fisher extraction are each
applied to allnrows at once within their respective calls, reproducingntimes Theorem 22
and Theorem 24’s per-series accounting at lengthl p(l), evaluated with this implementation’s
own constants, giving the marginal termn· eT r,(I)(lp(l), d, ν). Since the four representations
are processed independently and sequentially, summing this per-representation cost over
p∈ {1,2,3,4}gives the total, using P p n· eT r,(I)(lp(l), d, ν) =n·eT (I) Σ (l, d, ν).□
Proof of Theorem 32For a single representationp, the argument is identical in struc-
ture to the proof of Theorem 20: the series-outer implementation performsnouter-loop
iterations, each incurring a per-series overhead ˜κ (S)(lp(l)), possibly varying with the rep-
resentation’s own lengthl p(l). The compiled kernel’s cost for one series at lengthl p(l) is
exactly eT r,(S)(lp(l), d, ν), using this implementation’s own constants. Summing over then
independent series givesn·
h
˜κ(S)(lp(l)) + eT r,(S)(lp(l), d, ν) i for representationpalone. Since
70

the four representations are processed independently and sequentially, each incurring its own
per-series call-dispatch overhead ˜κ(S)(lp(l)), summing overp∈ {1,2,3,4}gives:
eT (S)(n, l, d, ν) =
4X
p=1
n·
h
˜κ(S)(lp(l)) + eT r,(S)(lp(l), d, ν) i
=n·


4X
p=1
˜κ(S)(lp(l)) +
4X
p=1
eT r,(S)(lp(l), d, ν)


T (S)(n, l, d, ν) =n· h ˜κ(S) Σ (l) + eT (S) Σ (l, d, ν) i
□
Proof of Theorem 33Identical to the proof of Theorem 21, substituting
eT (I) , eT (S), eAI , eBI , eBS for their exact-algorithm counterparts: the argument only uses that
both eT (I) (n) and eT (S)(n) are affine inn(Theorem 31, Theorem 32), with a non-negative
intercept for eT (I) , which holds here by the same reasoning as in the exact algorithm.□
Appendix B Additional results
Subsection 8.5 shows the exact-vs-approx quantile correlation histograms for
StarLightCurves in the main text, the largest and most fully depth-populated of the
six data sets used there. Figure B1 through Figure B5 show the same figure for the
remaining five data sets (see Table 8 for their summary statistics). ItalyPowerDemand
only populates depths 0 to 4, since its series length (l= 24) is short enough that
the depth cap min(d,⌊log 2(l)⌋+ 1) (Section 3) binds before the configuredd= 6 is
reached, leaving its depth-5 panel empty.
71

−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
2
4
6
8
10
Depth level 0 (n=77, median=0.6106)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0.0
2.5
5.0
7.5
10.0
12.5
15.0
17.5
Depth level 1 (n=103, median=0.8144)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
5
10
15
20
25
30
Depth level 2 (n=92, median=0.8856)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
2
4
6
8
10
Depth level 3 (n=45, median=0.7319)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
5
10
15
20
25
30
Depth level 4 (n=31, median=0.9758)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
25
50
75
100
125
150
Depth level 5 (n=222, median=0.9913)
Fig. B1: Distribution of the Pearson correlation coefficients between the exact and
approximated moment-based quantile values on the ECG200 data set (l= 96), with
one histogram per depth level 0 to 5. Each panel’s title reports the number of genuinely-
approximated columns at that depth and their median correlation.
72

−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
5
10
15
20
25
Depth level 0 (n=124, median=0.1840)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
5
10
15
20
Depth level 1 (n=177, median=0.6107)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
10
20
30
40
50
60
Depth level 2 (n=189, median=0.8942)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
10
20
30
40
50
60
70
Depth level 3 (n=150, median=0.9353)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
10
20
30
40
50
Depth level 4 (n=101, median=0.9270)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
20
40
60
80
100
120
Depth level 5 (n=129, median=0.9999)
Fig. B2: Distribution of the Pearson correlation coefficients between the exact and
approximated moment-based quantile values on the GunPoint data set (l= 150),
with one histogram per depth level 0 to 5. Each panel’s title reports the number of
genuinely-approximated columns at that depth and their median correlation.
73

−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Depth level 0 (n=14, median=0.7669)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Depth level 1 (n=9, median=0.6225)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
1
2
3
4
Depth level 2 (n=7, median=0.9415)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
10
20
30
40
Depth level 3 (n=54, median=0.9889)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
5
10
15
20
25
Depth level 4 (n=28, median=1.0000)
−1.00−0.75−0.50−0.25 0.00 0.25 0.50 0.75 1.00
0.0
0.2
0.4
0.6
0.8
1.0
Depth level 5 (no data)
Fig. B3: Distribution of the Pearson correlation coefficients between the exact and
approximated moment-based quantile values on the ItalyPowerDemand data set (l=
24), with one histogram per depth level 0 to 5. The depth cap binds for this data set,
so the panel for depth level 5 has no data. Each panel’s title reports the number of
genuinely-approximated columns at that depth and their median correlation.
74

−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
2
4
6
8
10
12
14
Depth level 0 (n=126, median=0.0528)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
5
10
15
20
Depth level 1 (n=177, median=0.3103)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
5
10
15
20
25
Depth level 2 (n=189, median=0.5753)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0.0
2.5
5.0
7.5
10.0
12.5
15.0
17.5
Depth level 3 (n=150, median=0.6174)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
5
10
15
20
Depth level 4 (n=99, median=0.7017)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
20
40
60
80
100
Depth level 5 (n=117, median=0.9942)
Fig. B4: Distribution of the Pearson correlation coefficients between the exact and
approximated moment-based quantile values on the Wafer data set (l= 152), with one
histogram per depth level 0 to 5. Each panel’s title reports the number of genuinely-
approximated columns at that depth and their median correlation.
75

−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
10
20
30
40
50
Depth level 0 (n=366, median=0.3207)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
20
40
60
80
100
Depth level 1 (n=538, median=0.7612)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
50
100
150
200
Depth level 2 (n=609, median=0.8798)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
50
100
150
200
250
300
Depth level 3 (n=615, median=0.9229)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
50
100
150
200
250
Depth level 4 (n=527, median=0.9266)
−1.0 −0.5 0.0 0.5 1.0
Pearson correlation
0
25
50
75
100
125
150
Depth level 5 (n=378, median=0.9053)
Fig. B5: Distribution of the Pearson correlation coefficients between the exact and
approximated moment-based quantile values on the Yoga data set (l= 426), with one
histogram per depth level 0 to 5. Each panel’s title reports the number of genuinely-
approximated columns at that depth and their median correlation.
76

References
Am´ ed´ ee-Manesme, C.-O., Barth´ el´ emy, F., Maillard, D. (2019). Computation of
the corrected cornish–fisher expansion using the response surface methodol-
ogy: Application to VaR and CVaR.Annals of Operations Research,281(1-2),
423–453,
Bagnall, A., Flynn, M., Large, J., Lines, J., Middlehurst, M. (2020, September). On the
Usage and Performance of the Hierarchical Vote Collective of Transformation-
Based Ensembles Version 1.0 (HIVE-COTE v1.0).Advanced Analytics and
Learning on Temporal Data: 5th ECML PKDD Workshop, AALTD 2020, Ghent,
Belgium, September 18, 2020, Revised Selected Papers(pp. 3–18). Berlin,
Heidelberg: Springer-Verlag.
Berndt, D.J., & Clifford, J. (1994, July). Using dynamic time warping to find patterns
in time series.Proceedings of the 3rd International Conference on Knowledge
Discovery and Data Mining(pp. 359–370). Seattle, W A: AAAI Press.
Bostrom, A., & Bagnall, A. (2017). Binary shapelet transform for multiclass time series
classification (extended version). A. Hameurlain, J. K¨ ung, R. Wagner, S. Madria,
& T. Hara (Eds.),Transactions on Large-Scale Data- and Knowledge-Centered
Systems XXXII(Vol. 10420, pp. 24–46). Springer.
Bostrom, A., Bagnall, A., Lines, J. (2016). Evaluating Improvements to the Shapelet
Transform.Second SIGKDD Workshop on Mining and Learning from Time
Series.
Breiman, L. (2001, October). Random Forests.Machine Learning,45(1), 5–32,
https://doi.org/10.1023/A:1010933404324
Cabello, N., Naghizade, E., Qi, J., Kulik, L. (2020, November). Fast and Accu-
rate Time Series Classification Through Supervised Interval Search.2020 IEEE
International Conference on Data Mining (ICDM), 948–953, https://doi.org/
10.1109/ICDM50108.2020.00107
Cabello, N., Naghizade, E., Qi, J., Kulik, L. (2024, March). Fast, accurate and
explainable time series classification through randomization.Data Mining and
Knowledge Discovery,38(2), 748–811, https://doi.org/10.1007/s10618-023
-00978-w
Christ, M., Braun, N., Neuffer, J., Kempa-Liehr, A.W. (2018, September). Time Series
FeatuRe Extraction on basis of Scalable Hypothesis tests (tsfresh – A Python
package).Neurocomputing,307, 72–77, https://doi.org/10.1016/j.neucom.2018
77

.03.067
Cornish, E.A., & Fisher, R.A. (1938). Moments and cumulants in the specification of
distributions.Revue de l’Institut International de Statistique,5(4), 307–320,
Cortes, C., & Vapnik, V. (1995, September). Support-Vector Networks.Machine
Learning,20(3), 273–297, https://doi.org/10.1023/A:1022627411411
Cover, T., & Hart, P. (1967, January). Nearest neighbor pattern classification.IEEE
Transactions on Information Theory,13(1), 21–27, https://doi.org/10.1109/
TIT.1967.1053964
Cuturi, M. (2011, June). Fast global alignment kernels.Proceedings of the 28th Inter-
national Conference on International Conference on Machine Learning(pp.
929–936). Madison, WI, USA: Omnipress.
Cuturi, M., Vert, J.-P., Birkenes, O., Matsui, T. (2007, April). A kernel for time series
based on global alignments.2007 IEEE International Conference on Acoustics,
Speech and Signal Processing - ICASSP ’07(p. II-413-II-416).
Dau, H.A., Bagnall, A., Kamgar, K., Yeh, C.-C.M., Zhu, Y., Gharghabi, S., . . .
Keogh, E. (2019, November). The UCR time series archive.IEEE/CAA
Journal of Automatica Sinica,6(6), 1293–1305, https://doi.org/10.1109/
JAS.2019.1911747
Dempster, A., Petitjean, F., Webb, G.I. (2020, September). ROCKET: Exceptionally
fast and accurate time series classification using random convolutional kernels.
Data Mining and Knowledge Discovery,34(5), 1454–1495, https://doi.org/
10.1007/s10618-020-00701-z
Dempster, A., Schmidt, D.F., Webb, G.I. (2021, August). MiniRocket: A Very Fast
(Almost) Deterministic Transform for Time Series Classification.Proceedings of
the 27th ACM SIGKDD Conference on Knowledge Discovery & Data Mining
(pp. 248–257). New York, NY, USA: Association for Computing Machinery.
Dempster, A., Schmidt, D.F., Webb, G.I. (2023, September). Hydra: Competing
convolutional kernels for fast and accurate time series classification.Data Mining
and Knowledge Discovery,37(5), 1779–1805, https://doi.org/10.1007/s10618
-023-00939-3
78

Dempster, A., Schmidt, D.F., Webb, G.I. (2024, July). Quant: A minimalist interval
method for time series classification.Data Mining and Knowledge Discovery,
38(4), 2377–2402, https://doi.org/10.1007/s10618-024-01036-9
Deng, H., Runger, G., Tuv, E., Vladimir, M. (2013, August). A time series forest
for classification and feature extraction.Information Sciences,239, 142–153,
https://doi.org/10.1016/j.ins.2013.02.030
Fisher, R.A., & Cornish, E.A. (1960). The percentile points of distributions having
known cumulants.Technometrics,2(2), 209–225,
Fix, E., & Hodges, J.L. (1989). Discriminatory Analysis. Nonparametric Dis-
crimination: Consistency Properties.International Statistical Review / Revue
Internationale de Statistique,57(3), 238–247, https://doi.org/10.2307/1403797
1403797
Flynn, M., Large, J., Bagnall, T. (2019, September). The Contract Random Interval
Spectral Ensemble (c-RISE): The Effect of Contracting a Classifier on Accu-
racy.Hybrid Artificial Intelligent Systems: 14th International Conference, HAIS
2019, Le´ on, Spain, September 4–6, 2019, Proceedings(pp. 381–392). Berlin,
Heidelberg: Springer-Verlag.
Freund, Y., & Schapire, R.E. (1996, July). Experiments with a new boosting algo-
rithm.Proceedings of the Thirteenth International Conference on International
Conference on Machine Learning(pp. 148–156). San Francisco, CA, USA:
Morgan Kaufmann Publishers Inc.
Geurts, P., Ernst, D., Wehenkel, L. (2006, April). Extremely randomized trees.
Machine Learning,63(1), 3–42, https://doi.org/10.1007/s10994-006-6226-1
Guillaume, A., Vrain, C., Elloumi, W. (2022, June). Random Dilated Shapelet Trans-
form: A New Approach for Time Series Shapelets.Pattern Recognition and
Artificial Intelligence: Third International Conference, ICPRAI 2022, Paris,
France, June 1–3, 2022, Proceedings, Part I(pp. 653–664). Berlin, Heidelberg:
Springer-Verlag.
Harris, C.R., Millman, K.J., van der Walt, S.J., Gommers, R., Virtanen, P., Cour-
napeau, D., . . . Oliphant, T.E. (2020, September). Array programming with
NumPy.Nature,585(7825), 357–362, https://doi.org/10.1038/s41586-020-2649
-2
79

Herrmann, M., & Webb, G.I. (2023, May). Amercing: An intuitive and effec-
tive constraint for dynamic time warping.Pattern Recognition,137, 109333,
https://doi.org/10.1016/j.patcog.2023.109333
Hill, G.W., & Davis, A.W. (1968). Generalized asymptotic expansions of cornish-fisher
type.Annals of Mathematical Statistics,39(4), 1264–1273,
Hills, J., Lines, J., Baranauskas, E., Mapp, J., Bagnall, A. (2014, July). Classification
of time series by shapelet transformation.Data Min. Knowl. Discov.,28(4),
851–881, https://doi.org/10.1007/s10618-013-0322-1
Hoerl, A.E., & Kennard, R.W. (1970). Ridge Regression: Applications to Nonorthog-
onal Problems.Technometrics,12(1), 69–82, https://doi.org/10.2307/1267352
1267352
Hunter, J.D. (2007, May). Matplotlib: A 2D Graphics Environment.Computing in
Science Engineering,9(3), 90–95, https://doi.org/10.1109/MCSE.2007.55
Ismail Fawaz, H., Forestier, G., Weber, J., Idoumghar, L., Muller, P.-A. (2019,
July). Deep learning for time series classification: A review.Data Mining
and Knowledge Discovery,33(4), 917–963, https://doi.org/10.1007/s10618-019
-00619-1
Itakura, F. (1975, February). Minimum prediction residual principle applied to speech
recognition.IEEE Transactions on Acoustics, Speech, and Signal Processing,
23(1), 67–72, https://doi.org/10.1109/TASSP.1975.1162641
Jaschke, S. (2002). The cornish-fisher expansion in the context of delta-gamma-normal
approximations.Journal of Risk,4(4), 33–52,
Jeong, Y.-S., Jeong, M.K., Omitaomu, O.A. (2011, September). Weighted dynamic
time warping for time series classification.Pattern Recognition,44(9), 2231–
2240, https://doi.org/10.1016/j.patcog.2010.09.022
Lam, S.K., Pitrou, A., Seibert, S. (2015). Numba: A LL VM-based Python JIT Com-
piler.Proceedings of the Second Workshop on the LL VM Compiler Infrastructure
in HPC(pp. 7:1–7:6). Austin, Texas: ACM.
80

Lin, J., Keogh, E., Wei, L., Lonardi, S. (2007, October). Experiencing SAX: A novel
symbolic representation of time series.Data Mining and Knowledge Discovery,
15(2), 107–144, https://doi.org/10.1007/s10618-007-0064-z
Lines, J., Taylor, S., Bagnall, A. (2018, July). Time Series Classification with HIVE-
COTE: The Hierarchical Vote Collective of Transformation-Based Ensembles.
ACM Trans. Knowl. Discov. Data,12(5), 52:1–52:35, https://doi.org/10.1145/
3182382
Lubba, C.H., Sethi, S.S., Knaute, P., Schultz, S.R., Fulcher, B.D., Jones, N.S. (2019,
November). Catch22: CAnonical Time-series CHaracteristics.Data Mining and
Knowledge Discovery,33(6), 1821–1852, https://doi.org/10.1007/s10618-019
-00647-x
Maillard, D. (2020, December).A User’s Guide to the Cornish Fisher Expansion.
Retrieved from https://hal.science/hal-02987694 (working paper or preprint)
Middlehurst, M., Ismail-Fawaz, A., Guillaume, A., Holder, C., Guijo-Rubio, D., Bula-
tova, G., . . . Bagnall, A. (2024). Aeon: A Python Toolkit for Learning from
Time Series.Journal of Machine Learning Research,25(289), 1–10,
Middlehurst, M., Large, J., Bagnall, A. (2020, December). The Canonical Interval
Forest (CIF) Classifier for Time Series Classification.2020 IEEE International
Conference on Big Data (Big Data)(pp. 188–195).
Middlehurst, M., Large, J., Flynn, M., Lines, J., Bostrom, A., Bagnall, A. (2021,
December). HIVE-COTE 2.0: A new meta ensemble for time series classification.
Machine Learning,110(11), 3211–3243, https://doi.org/10.1007/s10994-021
-06057-9
Middlehurst, M., Sch¨ afer, P., Bagnall, A. (2024, July). Bake off redux: A review
and experimental evaluation of recent time series classification algorithms.Data
Mining and Knowledge Discovery,38(4), 1958–2031, https://doi.org/10.1007/
s10618-024-01022-1
Mohammadi Foumani, N., Miller, L., Tan, C.W., Webb, G.I., Forestier, G., Salehi,
M. (2024, April). Deep Learning for Time Series Classification and Extrin-
sic Regression: A Current Survey.ACM Comput. Surv.,56(9), 217:1–217:45,
https://doi.org/10.1145/3649448
81

Paszke, A., Gross, S., Massa, F., Lerer, A., Bradbury, J., Chanan, G., . . . Chintala,
S. (2019). PyTorch: An Imperative Style, High-Performance Deep Learning
Library.Advances in Neural Information Processing Systems(Vol. 32). Curran
Associates, Inc.
Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., . . .
Duchesnay, ´E. (2011, October). Scikit-learn: Machine Learning in Python.
Journal of Machine Learning Research,12, 2825-2830,
Sakoe, H., & Chiba, S. (1978, February). Dynamic programming algorithm opti-
mization for spoken word recognition.IEEE Transactions on Acoustics, Speech,
and Signal Processing,26(1), 43–49, https://doi.org/10.1109/TASSP.1978
.1163055
Sch¨ afer, P. (2015, November). The BOSS is concerned with time series classification in
the presence of noise.Data Mining and Knowledge Discovery,29(6), 1505–1530,
https://doi.org/10.1007/s10618-014-0377-7
Sch¨ afer, P., & H¨ ogqvist, M. (2012). SF A: A symbolic fourier approximation and
index for similarity search in high dimensional datasets.Proceedings of the
15th International Conference on Extending Database Technology - EDBT ’12
(p. 516). Berlin, Germany: ACM Press.
Sch¨ afer, P., & Leser, U. (2017, November). Fast and Accurate Time Series Clas-
sification with WEASEL.Proceedings of the 2017 ACM on Conference on
Information and Knowledge Management(pp. 637–646). New York, NY, USA:
Association for Computing Machinery.
Sch¨ afer, P., & Leser, U. (2023, December). WEASEL 2.0: A random dilated dictionary
transform for fast, accurate and memory constrained time series classification.
Machine Learning,112(12), 4763–4788, https://doi.org/10.1007/s10994-023
-06395-w
Tan, C.W., Dempster, A., Bergmeir, C., Webb, G.I. (2022, September). MultiRocket:
Multiple pooling operators and transformations for fast and effective time
series classification.Data Mining and Knowledge Discovery,36(5), 1623–1646,
https://doi.org/10.1007/s10618-022-00844-1
Ulyanov, V.V., Aoshima, M., Fujikoshi, Y. (2016). Non-asymptotic results for cornish–
fisher expansions.Journal of Mathematical Sciences,218, 363–368,
82

Virtanen, P., Gommers, R., Oliphant, T.E., Haberland, M., Reddy, T., Cournapeau,
D., . . . van Mulbregt, P. (2020, March). SciPy 1.0: Fundamental algorithms
for scientific computing in Python.Nature Methods,17(3), 261–272, https://
doi.org/10.1038/s41592-019-0686-2
Waskom, M.L. (2021, April). Seaborn: Statistical data visualization.Journal of Open
Source Software,6(60), 3021, https://doi.org/10.21105/joss.03021
Wes McKinney (2010). Data Structures for Statistical Computing in Python. St´ efan
van der Walt & Jarrod Millman (Eds.),Proceedings of the 9th Python in Science
Conference(p. 56 - 61).
Ye, L., & Keogh, E. (2011, January). Time series shapelets: A novel technique
that allows accurate, interpretable and fast classification.Data Mining and
Knowledge Discovery,22(1), 149–182, https://doi.org/10.1007/s10618-010
-0179-5
83
