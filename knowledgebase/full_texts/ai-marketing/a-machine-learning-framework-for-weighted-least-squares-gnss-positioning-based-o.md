---
title: A Machine Learning Framework for Weighted Least Squares GNSS Positioning based on Activation Functions
url: https://arxiv.org/abs/2605.21461
category: ai-marketing
subcategory: measurement
date: 2026-05
venue: ''
authors:
- Pin-Hsun Lee
- Harry Leib
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.21461
pages: 36
chars: 73516
fetched_at: '2026-11-08T13:27:12+00:00'
kb_version: 1
---

# A Machine Learning Framework for Weighted Least Squares GNSS Positioning based on Activation Functions

1
A Machine Learning Framework for Weighted
Least Squares GNSS Positioning based on
Activation Functions
Pin-Hsun Lee and Harry Leib
Abstract
Global Navigation Satellite Systems (GNSS) are widely used to provide position, velocity,
and timing (PVT) information for various applications, inc luding transportation, location-based
communication services, and intelligent agriculture. In u rban canyons, high-rise buildings and
narrow streets can cause signal obstruction, non-line-of- sight (NLOS) reception, and multipath
eﬀects that introduce errors in GNSS pseudorange measureme nts. Although multi-constellations
GNSS eﬀectively increase the number of available satellite s, the inclusion of degraded signals
can lead to severe positioning errors. This study proposes a machine learning framework for the
weighted least squares (WLS) algorithm incorporating acti vation functions to enhance positioning
accuracy. Several signal quality indicators are employed a s training features for ensemble learning
algorithms to identify poor quality signals by providing qu ality scores. Then, activation functions
are employed to transform the machine learning predicted sc ores to appropriate weights for
WLS positioning. To evaluate the performance of our approac h, experiments are conducted
using real-world datasets from Hong Kong and Tokyo urban are as. Comparative analysis of
activation functions reveals that sigmoid functions consi stently yield the greatest improvements
with diﬀerent machine learning algorithms and GNSS constel lation conﬁgurations. The proposed
algorithm demonstrates substantial reductions in positio ning errors for both single- and multi-
constellation scenarios. Furthermore, our results indica te that the proposed algorithm exhibits
strong geographical transferability. The proposed algori thm maintains comparable level of per-
formance when trained on data from other regions with simila r levels of urbanization.
Index Terms - Global navigation satellite systems (GNSS), Machine lear ning, Activation
functions, Multi-constellations GNSS, Urban canyons, NLO S signal propagation, Multipath
signal propagation.
Pin-Hsun Lee is with the Department of Electrical and Comput er Engineering, McGill University, Montreal, QC,
Canada. E-mail:pin-hsun.lee@mail.mcgill.ca.
Harry Leib is with the Department of Electrical and Computer Engineering, McGill University, Montreal, QC,
Canada. E-mail:harry.leib@mail.mcgill.ca.
arXiv:2605.21461v1  [cs.LG]  20 May 2026

2
I. Introduction
The growing reliance of existing and emerging technologies on position information prompted
an increased interest in Global Navigation Satellite Syste ms (GNSS) applications [1] [2]
[3]. From smartphone navigation [4] [5] to intelligent tran sportation systems [6] [7], GNSS
provides services that are essential to our modern society. With the rapid advancement and
commercialization of autonomous vehicles, the importance of GNSS positioning accuracy
has reached unprecedented levels [8]. However, in urban env ironments GNSS signals are
susceptible to obstruction, reﬂection, and refraction fro m high-rise buildings which lead
to degraded positioning accuracy [9]. Signal obstruction r esults in insuﬃcient number of
received signals to generate a positioning solution. Non-l ine-of-sight (NLOS) signals reﬂected
from building surfaces travel longer paths, which introduc e delays in signal arrival time [10].
These propagation delays cause pseudorange measurement er rors that can exceed one kilo-
meter [11]. Multipath interference, where the same signal i s received via multiple propagation
paths, deteriorates the correlation functions and leads to pseudorange measurement errors.
[12]. Furthermore, the satellite geometry is a critical fac tor aﬀecting positioning accuracy
and can be quantiﬁed by the dilution of precision (DOP) [13] m etrics. A high DOP indicates
poor satellite geometry that leads to higher positioning er ror [13].
To increase GNSS positioning accuracy, one of the most popul ar research directions
is GNSS NLOS/multipath detection and exclusion [14]–[16]. The advancement of artiﬁ-
cial intelligence (AI) has facilitated the application of m achine learning techniques for
NLOS/multipath signal classiﬁcation. AI models can ﬁnd hid den patterns in complex and
high-dimensional data, which can be used to identify NLOS/m ultipath signals based on
signal quality features [17]–[19]. A weighting scheme for p recise point positioning (PPP)
proposed by Li et al. [20] incorporates elevation angle, car rier-to-noise density ratio C/N0,
and the predicted NLOS probability from machine learning (M L) output. Among the popular
ML algorithms, random forest achieves the highest classiﬁc ation accuracy [20]. A support
vector machine (SVM) classiﬁer that detects NLOS signals ac hieves approximately 90%
accuracy with static data and 86% accuracy with dynamic data collected in downtown
Tokyo [14]. Crespillo et al. [18] developed a branched logis tic regression algorithm employing
multi-frequency GNSS features from diﬀerent constellatio ns independently. This algorithm
achieves 84% accuracy on static GPS dataset and 91.4% accura cy on Galileo dataset [18]. Xu

3
et al. [21] constructs a scoring system by incorporating SVM -based NLOS classiﬁer with a
shadow matching technique. The scoring system assigns scor es to particles that are generated
around the initial weighted least squares (WLS) estimate us ing Gaussian distribution [21].
The ﬁnal position solutions are computed using particles wh ose scores exceed a predeﬁned
threshold [21]. Suzuki and Amano [16] developed both SVM and neural network classiﬁers
for NLOS signal detection utilizing geometric features of c orrelation function. Although the
neural network demonstrates slightly better performance, its training time is 5 to 10 times
longer than that of the SVM. Comparative studies in [17] and [ 22] show that ensemble
machine learning algorithms can achieve higher NLOS classi ﬁcation accuracy than other
ML methods. Therefore, ensemble machine learning algorith ms are employed in our work.
Following NLOS/multipath signal detection, excluding the degraded signals can adversely
aﬀect satellite geometry [20]. As a result, a WLS method is pr oposed to address the varying
quality of pseudorange measurements [12]. WLS modiﬁes the r elative contribution of each
signal through suitable weighting that reﬂects measuremen t quality [23]–[26]. Under the con-
dition that weights correspond to the inverse of variance-c ovariance matrix of pseudorange
errors, WLS estimation satisﬁes the best linear unbiased es timator (BLUE) criterion [12],
[26]. Traditional weighting schemes employ elevation angl e and C/N0 to construct variance
estimation formulas [24], [27], [28]. Machine learning app roaches can capture the complex
relationships between selected features and signal qualit y to improve variance estimation.
An SVM-driven weighting approach for PPP was introduced by L yu and Gao [29]. The
results demonstrate a 65.4% improvement in positioning acc uracy compared to traditional
C/N0-based weighting models [29]. The random forest-based weig hting approach developed
by Li et al. [17] outperforms other traditional weighting me thods in terms of 3D mean error
and standard deviation, and has been used also in [30].
Motivated by machine learning NLOS/multipath detection, o ur work [31] considers a novel
ensemble learning-based activation function framework fo r multi-constellation GNSS WLS
positioning. The activation function framework is general in the sense that it can be used
with other machine learning algorithms, beyond those used i n this study. The ensemble
learning models are trained to identify quality of signals b ased on multiple signal quality
indicators. The activation functions are used to map the qua lity scores from machine learning
output into weights. Multi-constellation GNSS eﬀectively increases signal availability which
is beneﬁcial to the positioning accuracy especially in urba n environments. An algorithm

4
based on WLS is employed to relatively increase the contribu tion of reliable signals without
degrading satellite geometry in the process of calculating a position solution. The main
contributions of our paper are three fold: (1) three ensembl e learning techniques are employed
to assess GNSS signal quality scores using indicators that r eﬂect NLOS/multipath errors
and satellite geometry; (2) with respect to our initial cont ribution [30] the present paper
introduces a novel activation function framework and prese nts performance results with
several functions to identify the optimal one that minimize s the 3D positioning errors;
(3) real-world datasets collected from Hong Kong and Tokyo a re employed to validate the
eﬀectiveness of the proposed algorithm across single and mu lti-constellation conﬁgurations.
The rest of this paper is organized as follows: Section II pro vides an overview of the
proposed algorithm, followed by an introduction of pseudor ange model and WLS algorithm.
The selected signal quality features are also discussed in t his section. Section III derives
the machine learning algorithms and presents a selection of activation functions. Section IV
describes the experiment setup, and provides comprehensiv e analysis of results from both
Hong Kong and Tokyo datasets. Section V provides summary of r esearch outcomes and
prospective research directions.
II. The Framework, Algorithm, and Models
This section presents the concepts that lie the foundations of our framework, including
features selection for Machine Learning applications in sa tellite navigation.
A. Overview
For readers’ convenience, in Figure 1 we present the ﬂowchar t of the proposed algorithm
[31]. Initially, ordinary least squares (OLS) positioning solutions are computed using all
the available satellites. During this stage, signal qualit y features such as elevation angle,
pseudorange residual, geometric dilution of precision (GD OP) contribution, pseudorange rate
consistency, and estimated receiver clock oﬀset are calcul ated and extracted. These features
along with C/N0 are then extracted to form machine learning training and tes ting data. In
the training set, epochs with four or less signals are discar ded to ensure the eﬀectiveness of
machine learning training process. Next, machine learning models are trained for GPS and
BeiDou data separately. The predicted scores from the machi ne learning output are then

5
mapped into weights by the activation functions. Finally, t hese weights are employed in the
WLS algorithm to calculate the ﬁnal positioning solutions.
Fig. 1: Flowchart of the proposed algorithm.
B. Pseudorange Model
The pseudorange ρ [32] is modeled by:
ρmodel i,j = √ (xi,j − xu)2 + (yi,j − yu)2 + (zi,j − zu)2 + δi ρ (1)
where ( x, y, z) is the 3-dimensional (3D) position in earth-centered eart h-ﬁxed (ECEF)
coordinates, subscript u indicates user, subscripts ( i, j) represent j-th satellite in i-th con-
stellation and δi ρ is the geometric distance equivalent of receiver clock oﬀse ts with respect to
GNSS system time. The satellite position can be computed by u sing the parameters from
GNSS navigation ﬁle. Given pseudorange measurements from m GPS signals and n BeiDou
signals, the unknown parameters of the modeled pseudorange in (1) are represented by a
5 dimensional vector xu =
[
xu yu zu δGPS ρu δBD ρu
]T
. The modeled pseudorange in (1) is
a non-linear function of user position coordinates ( xu, yu, zu) and δi ρ. However it can be

6
transformed into a set of linear equations through a ﬁrst-or der Taylor expansion around an
initial point x0 =
[
x0 y0 z0 δGPS ρ0 δBD ρ0
]T
:
ρmodel(xu) ≈ ρmodel(x0) + ∂ρ ∂x (xu − x0) + ∂ρ ∂y (yu − y0) + ∂ρ ∂z (zu − z0) + ∂ρ ∂δ GPSρ (δGPS ρu − δGPS ρ0 )+
∂ρ
∂δ BDρ (δBD ρu − δBD ρ0 )
= ρmodel(x0) + ∂ρ ∂x ∆x + ∂ρ ∂y ∆y + ∂ρ ∂z ∆z + ∂ρ ∂δ GPSρ ∆δGPSρ + ∂ρ ∂δ BDρ ∆δBDρ
(2)
where ∆x =
[
∆x ∆y ∆z δGPS ρu δBD ρu
]T
= xu − x0.
C. Fundamentals of GNSS WLS Positioning
The pseudorange measurement ρobs from a GNSS receiver is subject to various errors,
therefore it can be expressed as:
ρobs i,j = ρmodel i,j + ǫi,j (3)
where ǫ denotes the pseudorange measurement error and subscripts ( i, j) denote the j-th
satellite in i-th constellation. From (1) and (3) we have for m GPS and n BeiDou signals
the linear equations for residuals:
∆ρ = H∆x + ǫ (4)
where ∆ρ is the pseudorange residual vector:
∆ρ =

 ρobs GPS,1 − ρmodel GPS,1(x0) ... ρobs GPS,m − ρmodel GPS,m(x0) ρobs BD,1 − ρmodel BD,1 (x0) ...
ρobs BD,n − ρmodel BD,n (x0)


(m+n)×1
(5)

7
H is the measurement matrix:
H =


∂ρmodel GPS,1
∂x
∂ρmodel GPS,1
∂y
∂ρmodel GPS,1
∂z
∂ρmodel GPS,1
∂δ GPSρ
∂ρmodel GPS,1
∂δ BDρ
... ... ... ... ...
∂ρmodel GPS,m
∂x
∂ρmodel GPS,m
∂y
∂ρmodel GPS,m
∂z
∂ρmodel GPS,m
∂δ GPSρ
∂ρmodel GPS,m
∂δ BDρ
∂ρmodel BD,1
∂x
∂ρmodel BD,1
∂y
∂ρmodel BD,1
∂z
∂ρmodel BD,1
∂δ GPSρ
∂ρmodel BD,1
∂δ BDρ
... ... ... ... ...
∂ρmodel BD,n
∂x
∂ρmodel BD,n
∂y
∂ρmodel BD,n
∂z
∂ρmodel BD,n
∂δ GPSρ
∂ρmodel BD,n
∂δ BDρ


(m+n)×5
(6)
and ǫ is the pseudorange measurement error vector: ǫ =
[
ǫGPS,1 . . . ǫ GPS,m ǫBD,1 . . . ǫ BD,n
]T
.
The objective of WLS is to ﬁnd the unknowns ∆x that minimize the weighted sum of
squared residuals:
ˆ∆x = arg minxu (∆ρ − H∆x)T W (∆ρ − H∆x) (7)
where W is the weighting matrix [12]. The WLS problem in (7) is solved by:
ˆ∆x = (HT W H)−1HT W ∆ρ (8)
D. Evaluation Metrics of GNSS Positioning
Positioning performance is assessed through 3D errors for i ndividual epochs and 3D root
mean square error (RMSE) computed over all available epochs . The 3D positioning errors
in the east-north-up (ENU) reference frame are computed as f ollows:
Error 3D =
√
(ˆx − xtruth)2 + (ˆy − ytruth)2 + (ˆz − ztruth)2 (9)
where (ˆx, ˆy, ˆz) and ( xtruth, ytruth, ztruth) are estimated position and ground truth in east,
north, and up direction, respectively. The 3D RMSE quantiﬁe s overall positioning accuracy
across all epochs and is calculated as:
RM SE3D =
/radicaltp/radicalvertex/radicalvertex√ 1
T
T∑
t=1
(Error 3D,t)2 (10)
where T is the number of available epochs and the subscript t indicates the t-th epoch.

8
E. Feature Selection
1) Elevation Angle: The elevation angle of a satellite is deﬁned as the angle form ed
between the user’s local horizontal plane and the line-of-s ight (LOS) vector directed toward
the satellite [32]. Satellite signals from lower elevation angles are more susceptible to signal
obstruction, reﬂection, and refraction caused by high-ris e buildings. Consequently, the ele-
vation angle is commonly used as an indicator for identifyin g NLOS and multipath errors
in pseudorange measurements [14].
2) Carrier-to-noise Density: C/N0 is the ratio of carrier power to thermal noise power
in 1Hz bandwidth [12]. Destructive multipath reception and NLOS propagation typically
cause substantial attenuation of C/N0 [33]. In contrast, constructive multipath signal can
lead to an increase in C/N0 [33]. As a result, a low C/N0 can indicate higher possibility of
NLOS/multipath signal. Nevertheless, signals exhibiting high C/N0 values could represent
either high quality LOS signals or the results of constructi ve multipath.
3) Pseudorange Residual: Pseudorange residual is deﬁned as the diﬀerence between pse u-
dorange measurement and the modeled pseudorange using esti mated user position and re-
ceiver clock bias. It is commonly used in Receiver Autonomou s Integrity Monitoring (RAIM)
to detect faulty pseudorange measurement. Pseudorange res idual R can be expressed as:
Ri,j = ρobs i,j − ρmodel i,j (ˆxu) (11)
where ρobs is the pseudorange measurement that can be directly taken fr om GNSS obser-
vation (RINEX) ﬁle, ρmodel is calculated from (1) using the estimated position and rece iver
clock oﬀset from all available satellites. A large pseudora nge residual indicates a potential
error in the pseudorange measurement.
4) GDOP Contribution: GDOP serves as a quality indicator for satellite geometry, w here
a lower value denotes a better geometry. The GDOP of m + n satellites from two constel-
lations is computed by:
Gm+n =
√
tr((HT 5×(m+n)H5×(m+n))−1) (12)
where tr( ·) denotes the matrix trace operator and H is the measurement matrix deﬁned
in (6). The GDOP contribution of a speciﬁc satellite measure s the impact of the satellite

9
signal due to satellite geometry [34]. To obtain the GDOP con tribution of satellite k, we
ﬁrst calculate the GDOP without the k-th satellite:
Gk m+n−1 =
√
tr((H(k)T 5×(m+n−1)H(k) 5×(m+n−1))−1) (13)
Subsequently, the GDOP contribution ∆ k G of the k-th satellite is computed by:
∆k G = Gk m+n−1 − Gm+n (14)
where ∆ k G ≥ 0 [35]. A large ∆ k G indicates that excluding the k-th satellite would remarkably
compromise satellite geometry. Hence, satellites with hig her ∆k G values should receive greater
weighting in WLS positioning computations.
5) Pseudorange Rate Consistency: Doppler-based measurements generally are more ac-
curate than pseudorange measurements, as they are less sens itive to slowly changing error
sources such as atmospheric delays and hardware biases [12] . This characteristic makes the
pseudorange rate ˙ρ computed from Doppler shift more reliable [36]:
˙ρ = fDoppler · c fcarrier (15)
where fDoppler denotes the observed Doppler shift frequency, fcarrier represents the carrier
frequency and c is the speed of light. In contrast, the pseudorange rate calc ulated by the rate
of change of pseudorange measurements can contain larger er rors from more error sources.
Therefore, pseudorange rate consistency ǫ ˙ρ is adopted as a quality indicator and it can be
calculated by:
ǫ ˙ρ = (ρobs t − ρobs t−1) Te − ˙ρt (16)
where ρobs is the pseudorange measurement, the subscript t indicates t-th epoch, Te is the
time diﬀerence between two epochs and ˙ ρ is deﬁned in (15). A large ǫ ˙ρ suggest potential
NLOS/multipath contamination in the pseudorange measurem ents [37].
6) Estimated Receiver Clock Oﬀset: Estimated receiver clock oﬀset ˆδi ρ is calculated by:
ˆδi ρ = ρobs i,j − ˆri,j (17)
where ˆr =
√
(xi,j − ˆxu)2 + (yi,j − ˆyu)2 + (zi,j − ˆzu)2 is the geometric range between the
satellite position ( xi,j, yi,j, zi,j) and estimated user position (ˆ xu, ˆyu, ˆzu). The user position
is estimated by LS positioning using all available satellit es. Assuming all the pseudorange
measurements in a single epoch are accurate, the receiver cl ock oﬀsets derived from all satel-
lites j = 1, . . . , n in i-th constellation should be identical. Therefore, inconsi stent estimated

10
receiver clock oﬀset for individual signals reveal possibl e NLOS/multipath degradation of
the pseudorange measurements.
F. Feature Normalization
To distinguish the relative quality of each satellite signa l in an epoch, Z-score standard-
ization is performed on an epoch-by-epoch basis as follows:
˜dj,t = dj,t − ¯dt
σt
(18)
where dj,t denotes feature of j-th signal in epoch t, ˜d is normalized feature, ¯dt and σt
are the mean value and standard deviation (STD) of the featur e in epoch t, respectively.
This normalization process eliminates the eﬀect caused by d iﬀerent numerical scales of each
feature and enhances machine learning accuracy. Furthermo re, the absolute values are taken
for normalized pseudorange residual, pseudorange rate con sistency, and estimated receiver
clock oﬀset to quantify the magnitude of deviations from the ir respective means:
˜dj,t =
⏐⏐⏐⏐⏐ dj,t − ¯dt σt ⏐⏐⏐⏐⏐ (19)
III. Machine Learning Activation Function Framework
While deep learning approaches are able to learn complex pat terns from raw features,
they typically demand extensive training datasets and subs tantial computational resources
to attain satisfactory performance [38]. In comparison, gi ven limited amount of data, simpler
structures of traditional machine learning can achieve com parable performance using less
computation power. Furthermore, studies show that ensembl e learning algorithms outper-
form other machine learning methods in NLOS classiﬁcation t asks [17], [22]. Hence, this
study employs ensemble-based machine learning algorithms to evaluate signal quality.
A. Data Labeling
Data labeling assigns informative labels to features, whic h enables supervised machine
learning algorithms to learn the relationship between inpu t features and the target output.
In this study, a label is assigned according to the best set of satellites that produces the
minimum 3D positioning errors among all the subset combinat ions using LS positioning.
Satellite signals included in this best set are assigned a la bel of 1 and the remaining signals
are labeled as 0. Such labelled data sets are essential for th e training process.

11
B. Machine Learning Algorithms
1) Bagging: Bootstrap aggregating, commonly known as bagging, involve s three stages:
bootstrapping, training, and aggregation [39]. Bootstrap sampling forms multiple subsets by
randomly selecting data points with replacement from the or iginal data [40]. Each data point
includes feature vectors with associated labels. Subseque ntly, each subset is employed to train
a weak learner in parallel. A weak learner is a simple model th at has slightly better accuracy
compared to random guessing. During aggregation, predicti ons from all weak learners are
combined through methods such as majority voting or soft vot ing [39].
Random forest is one of the bagging algorithms that employs d ecision trees as weak
learners. Figure 2 illustrates the hierarchical structure and elements of a decision tree. Each
decision tree starts with a root node, which contains all the data to be classiﬁed. The root
node and subsequent decision nodes continuously split the d ata using speciﬁc criteria until a
stopping condition is met [41]. The branch connections repr esent decision pathways linking
decision nodes to their child nodes. The leaf nodes are the ﬁn al classiﬁcation results at the
bottom of the decision tree [42]. The best splitting criteri on maximizes the purity of resulting
child nodes, where purity is measured using metrics such as G ini impurity and entropy. For
K classes classiﬁcation, Gini impurity Hgini is computed by:
Hgini =
K∑
k=1
pk(1 − pk) (20)
and the entropy Hentropy is calculated by:
Hentropy = −
K∑
k=1
pklog(pk) (21)
where pk is the proportion of samples that belong to k-th class in a node. A low Gini impurity
or entropy indicates an eﬀective split, as it reﬂects that th e majority of data points inside
each child node belong to a single class. Instead of consider ing all the features, random forest
algorithm randomly selects a subset of features and decides a best split only using features
within this subset. This approach enhances variability of b ase learners which provides good
generalization capabilities on real-world datasets [42].
2) Boosting: Unlike bagging algorithms that train independent weak lear ners in parallel,
boosting approaches train weak learners sequentially wher e each successive weak learner
focuses more on misclassiﬁed instances from previous weak l earner [39], [43].

12
Fig. 2: Decision Tree.
Adaptive boosting, abbreviated as AdaBoost, is a boosting a lgorithm developed by Freund
and Schapire [44]. The algorithm trains individual weak lea rners using identical data sets
but applies diﬀerent sample weights. Consider training dat a S with N data points
S = {(d1, l1), (d2, l2), ..., (dN , lN )} (22)
where d denotes feature vector and l is the corresponding label. The ﬁrst weak learner φ1
is trained on training data S with uniform weights w1 n = 1 N . The error rate ǫ of m-th weak
learner is calculated as the weighted proportion of misclas siﬁed instances:
ǫm =
∑
n:φm(dn)⁄=ln wm n ∑N
n=1 wm n (23)
where m = 1 , 2, ...M indicates m-th weak learner. The weight of m-th weak learner αm is
then calculated based on its error rate to reﬂect its classiﬁ cation accuracy:
αm = η · log( 1 − ǫm
ǫm ) (24)
where η is the learning rate speciﬁed by the user. To emphasize the er rors, the sample
weights of misclassiﬁed instances are increased while the w eights of correct classiﬁcations
are decreased according to:
wm+1 n =



wm n exp(−αm)
Z m , if φm(dn) = ln
wm n exp(αm)
Z m , if φm(dn) ⁄= ln
(25)
where Z m is a normalization constant to ensure the sum of sample weigh ts equals 1. The
subsequent weak learner is trained on the training data S with the updated weights. After
repeating this process for M weak learners, the AdaBoost model is constructed by combini ng
all weak learners and their weights:
Φ(d) = sign(ΣM m=1αmφm(d)) (26)

13
Gradient boosting builds a strong classiﬁer by sequentiall y ﬁtting weak learners to the
pseudo-residuals which are negative gradients of the loss f unction [45]. Given training data in
(22), the objective of gradient boosting is to construct a st rong learner Φ( d) that minimizes
the total loss over all the training samples:
ˆΦ(d) = arg min
Φ(d)
N∑
n=1
Ψ(ln, Φ(dn)) (27)
where Ψ( ·) is a loss function, N is the number of samples and subscript n indicates n-th
sample. The log loss Ψ( ln, Φ(dn)) is commonly chosen as loss function for binary classiﬁcat ion
and it is developed from negative log likelihood:
Ψ(ln, Φ(dn)) = − log L(ln, Φ(dn)) = − log( ˆP (ln = 1|dn)ln · ˆP (ln = 0|dn)1−ln)
= −ln · β + log(1 + eβ) (28)
where β = Φ(dn) is the log-odds ratio:
β = log
ˆP (ln = 1|dn)
ˆP (ln = 0|dn) . (29)
Gradient boosting begins with an initial prediction model Φ 0(d) set to the log-odds ratio of
the training samples:
Φ0(d) = log
∑N
n=1 I(ln = 1)
N −
∑N
n=1 I(ln = 1) (30)
where I(·) is the indicator function. For iteration m = 1 to M, the pseudo-residual ˜lm n is
obtained by computing the negative gradient of the log-loss function:
˜lm n = −
[
∂Ψ(ln, Φ(dn))
∂Φ(dn)
]
Φ(dn)=Φm−1(dn)
= −
[
∂(−ln · Φ(dn) + log(1 + eΦ(dn)))
∂Φ(dn)
]
Φ(dn)=Φm−1(dn)
= −
[
−ln + eΦ(dn) 1 + eΦ(dn) ] Φ(dn)=Φm−1(dn) = ln − eΦm−1(dn) 1 + eΦm−1(dn)
(31)
Since eΦm−1(dn)
1+eΦm−1(dn) = ˆP (ln = 1|dn), the pseudo-residual ˜lm n represents the discrepancy between
the true label and the predicted probability. An updated tra ining dataset is formed by using
the pseudo-residuals as labels:
Sm = {(d1, ˜lm 1 ), (d2, ˜lm 2 ), . . . ,(dN , ˜lm N )} (32)
Using the updated training set Sm, a weak learner φm(d, θm) is trained by solving the least
squares problem:
θm = arg min
θ
N∑
n=1
(
˜lm n − φm(dn, θm) )2 (33)

14
where θm is the parameters of m-th weak learner. Finally, the strong learner is updated by
adding the trained weak learner:
Φm(d) = Φ m−1(d) + η · φm(d, θm) (34)
where η is the learning rate speciﬁed by the user. After executing M iterations, the ﬁnal
prediction model is given by:
ΦM (d) = Φ 0(d) +
M∑
m=1
η · φm(d, θm) (35)
3) Evaluation Metrics of Machine Learning: To evaluate the machine learning perfor-
mance, we use 0.5 as a threshold. When the predicted scores is larger than 0.5 it is treated
as label 1; otherwise, label 0. The accuracy is calculated by :
Accuracy = Number of Correct Predictions Total Number of Predictions . (36)
When calculating the testing accuracy, we omit the epochs wi th four or less signals since all
the available signals are used to produce positioning resul ts.
C. Activation Function
Inspired by neural networks (NN), activation functions are employed to convert quality
scores from machine learning output into appropriate weigh ts for least squares positioning.
Each layer of an NN represents a summary statistics of input w here only part of the input
information that maximizes the information retained about the target output is preserved
[46]. Figure 3 illustrates a hidden layer. The mutual inform ation (MI) between hidden layer T
and input d is represented as M I(d, T ) and MI between hidden layer and output l is denoted
by M I(T, l). An information plane is formed by M I(d, T ) and M I(T, l) where the ﬁtting
phase and compression phase are observed during the trainin g process [46]. Throughout
the ﬁtting phase, both M I(d, T ) and M I(T, l) increase, suggesting that the hidden layer is
learning to associate input features with corresponding ou tput labels [46]. In the compression
stage, the hidden layer discards the irrelevant input infor mation which decreases M I(d, T ).
A subsequent compression phase after ﬁtting phase can be obs erved in the information
plane when applying double-sided saturating functions suc h as tanh and sigmoid [46]. The
compression phase starts when the activation function ente rs their saturation region. For
linear functions or single-sided saturating functions suc h as rectiﬁed linear unit (ReLU),

15
ﬁtting and compression phases occur simultaneously and onl y the task-irrelevant information
is compressed. Our approach leverages the compression prop erties of activation functions to
suppress the noise or task-irrelevant information in machi ne learning outputs.
Furthermore, a NN relies on activation functions to introdu ce nonlinearities into the algo-
rithm [47]. The selection of appropriate activation functi ons signiﬁcantly impacts the training
process and performance. Non-linear activation functions are usually preferred over linear
ones in practical scenarios [48]. The saturation character istics of certain activation functions
assign zero weights to low-quality signals and uniform weig hts to high-quality signals, while
moderately weighting intermediate-quality signals to pre serve beneﬁcial satellite geometry
and improve the accuracy of the LS solution. In this study, th e input to the activation
function is the predicted probability from the machine lear ning, ranging from [0 , 1] while
the corresponding outputs are maintained within the same [0 , 1] interval.
Several activation functions are selected to assess their e ﬀects on weight design in the
WLS framework. Figure 4 illustrates the selected activatio n functions. The constant function
that assigns identical weights to all measurement serves as a baseline. It is expressed as
fconst(ˆp) = 1 where ˆp is the predicted probability from machine learning output. The WLS
problem turns into OLS problem in this case. The linear funct ion directly translates the
machine learning output scores into weights. It is expresse d as flinear(ˆp) = ˆp. The unit-step
function implements a hard threshold by selecting only a sub set of satellites to produce an
OLS solution. The predicted scores below the threshold are a ssigned zero weights and the
remaining signals with predicted scores above the threshol d are given unit weights. The unit
step function funit(·) can be expressed as:
funit(ˆp) =



1, ˆp ≥ τ
0, ˆp < τ
(37)
where τ ∈ [0, 1] is the threshold. The threshold is set to the mean predicte d scores of all
available signals in a certain epoch. If the number of signal s with unit weight is insuﬃcient
to generate LS results, the threshold is lowered by 0.05. ReL U activation function assigns
zero weights to low-quality measurements whose predicted s cores are below threshold τ and
linearly maps the remaining scores to the range [0 , 1]. It is deﬁned as:
ReLU(ˆp) =



ˆp−τ
1−τ , ˆp ≥ τ
0, ˆp < τ
(38)

16
where τ ∈ [0, 1]. In this study, τ is selected as the minimum predicted scores among all
available signals in current epoch. The sigmoid function ma kes soft decision that lowers
weights for poor-quality signals and increases weights for high-quality ones. It is deﬁned as:
sigmoid(ˆp; a, b) = 1 1 + e−b(ˆp−a) . (39)
where a and b controls the horizontal shift and steepness of the curve, re spectively. When
the steepness is inﬁnitely large, the sigmoid function beco mes a step function. To optimize
the performance of the sigmoid function for various cases, w e consider diﬀerent values of
shaping parameter b in the positioning results while parameter a is set to mean predicted
scores of all available signals in the current epoch.
Fig. 3: Hidden Layer.
IV. Experimental Results
This section presents results obtained when applying our fr amework to real life measure-
ments.
A. Experimental Setup
This study employs the UrbanNav open-source dataset, which provides GNSS observation
data and ground truth information for datasets collected in Hong Kong and Tokyo urban
areas [49]. The GNSS observation data are written in Receive r Independent Exchange

17
0 0.2 0.4 0.6 0.8 1
0
0.5
1
1.5
2
Weight
Constant
0 0.2 0.4 0.6 0.8 1
0
0.2
0.4
0.6
0.8
1
Weight
Linear
0 1
0
0.2
0.4
0.6
0.8
1
Weight
Unit step
0 1
0
0.2
0.4
0.6
0.8
1
Weight
ReLU
0 0.2 0.4 0.6 0.8 1
0
0.2
0.4
0.6
0.8
1
Weight
Sigmoid
a=0.5
b=50
0 0.2 0.4 0.6 0.8 1
0
0.2
0.4
0.6
0.8
1
Weight
Sigmoid
a=0.5
b=100
Fig. 4: Activation Functions.
(RINEX) format. The ground truth data are written in txt ﬁles for Hong Kong data and csv
ﬁles for Tokyo data. GPS L1 C/A and BeiDou B1I signals are used in this study. An elevation
mask that excludes signals with elevation angle below 15 ◦ is applied to avoid low-quality
signals.
1) Hong Kong Dataset: For Hong Kong dataset, the GNSS observation data were record ed
using a low-cost u-blox EVK-M8T receiver with 1 Hz output fre quency. Ground truth data
were collected by NovAtel SPAN-CPT receiver at an output fre quency of 1 Hz with post-
processing conducted by Inertial Explorer software [49].
The Hong Kong dataset consists of data collected from three l ocations with diﬀerent
urbanization levels: medium urban in Tsim Sha Tsui, deep urb an in Whampoa and harsh
urban in Mong Kok [49]. Medium urban data include 768 epochs, deep urban data consist
of 1518 epochs and harsh urban data contain 2312 epochs. Trai ning set for machine learning
includes deep urban and harsh urban data while medium urban d ata serve as testing set.
Figure 5a depicts the ground truth trajectories of medium ur ban data where the vehicle
started at epoch 1, following a clockwise route for two loops and ended at epoch 768.
2) Tokyo Dataset: For Tokyo dataset, GNSS observation data were collected by a u-blox
ZED-F9P sensor at a 5Hz output frequency. Ground truth data w ere collected by Applanix

18
22°17'50"N
22°17'55"N
22°18'N
22°18'05"N
22°18'10"NLatitude
114°10'40"E
Longitude
Start: Epoch 1
End:
Epoch 768
Esri, TomTom, Garmin, METI/NASA, USGS
(a)
35°41'N
35°41'15"N
35°41'30"N
35°41'45"NLatitude
139°41'15"E 139°41'30"E 139°41'45"E
Longitude
Start: Epoch 1End: Epoch 2095
Esri, TomTom, Garmin,
GeoTechnologies, Inc, METI/NASA,
USGS
(b)
Fig. 5: Ground truth of testing data (a) medium urban data fro m Hong Kong (b)
Shinjuku data from Tokyo.
POS L V620 at an output frequency of 10Hz. To maintain consist ency with the Hong Kong
dataset, both datasets were downsampled to 1 Hz by extractin g measurements at integer
seconds.
The Tokyo experimental dataset comprises data from two urba n locations: Shinjuku and
Odaiba. Shinjuku data are collected in the dense urban envir onment whereas Odaiba data
are collected in the suburban area with more open spaces and l ower buildings. Odaiba data
include 1241 epochs and Shinjuku data contain 2095 epochs. F igure 5b shows the ground
truth of Shinjuku data where the vehicle follows clockwise r oute to circle around the area and
the park from epoch 1 and stops at epoch 2095. Since Hong Kong d ataset has comparable
urbanization level as Shinjuku data, we use Shinjuku data as testing set and Hong Kong data
as training set to verify the applicability of the proposed a lgorithm in diﬀerent locations.
In addition, we compare its performance with the case where m achine learning models are
trained on Odaiba data.
B. Calibration using the CSRS-PPP Tool
Firstly, we check the correctness of our implemented baseli ne LS algorithm for position-
ing using all available GPS+BeiDou satellites in an open-sk y environment where machine

19
Fig. 6: Google Earth 3D view of the open sky ground truth traje ctory for the Odaiba
dataset epochs 291–300.
learning is not used, since all available signals are not dis torted. Such positioning results
are compared with solutions obtained from the Canadian Spat ial Reference System Precise
Point Positioning (CSRS-PPP) tool [50] when using the same d ata base. The CSRS-PPP
service oﬀers high-accuracy positioning solutions which w e use as a reference for comparison..
Figure 6 illustrates the ground truth trajectory for epochs 291–300 of the Odaiba data
set corresponding to an open-sky environment. Table I prese nts a comparison of the 3D
positioning errors obtained when using our LS algorithm emp loying a total of 14 satellites
(6 from GPS and 8 from BeiDou) and the CSRS-PPP solutions. The diﬀerences between
LS and CSRS-PPP results are around 30 (cm). We see that our pos itioning LS algorithm
provides results that are consistent with those from the hig h-precision CSRS-PPP service
in an open-sky environment. When using the CSRS-PPP tool on d ata obtained from non-
open sky environments, where satellite signals may suﬀer se vere propagation distortion, it
is noticed that 43.37 % of the epochs were rejected. This indi cates that the CSRS-PPP
tool is not eﬃcient in handling densily built urban environm ents. These are precisely the
environments where we envisage machine learning approache s to be useful.
C. Results of Hong Kong Dataset
1) Machine Learning Results: The machine learning results for GPS data are summarized
in Table II. The testing accuracies are 8 .66% and 8 .23% lower than training accuracies
for random forest and gradient boosting algorithms, respec tively. These results show that
the machine learning models are aﬀected by various distorti ons in the training data, and

20
TABLE I: The 3D positioning errors in meters for epochs 291–3 00 under open-sky using
the LS algorithm with 14 GPS+BeiDou satellites and the CSRS- PPP tool.
Epoch LS 3D Error CSRS-PPP 3D Error
291 2.1564 1.8546
292 2.1754 1.8475
293 2.1372 1.8582
294 2.1493 1.8756
295 2.1850 1.8904
296 2.1895 1.9019
297 2.2034 1.9134
298 2.2320 1.8962
299 2.3440 1.8955
300 2.4671 1.8837
TABLE II: Machine learning results for GPS with Hong Kong Dat aset.
Random Forest AdaBoost Gradient Boosting
Training Accuracy 0.8308 0.7603 0.8086
Testing Accuracy 0.7442 0.7669 0.7263
can lead to low generalization ability to unseen data in the t esting process. In contrast,
despite AdaBoost’s lower training accuracy compared to ran dom forest and gradient boosting
approaches, its testing performance aligns closely with it s training results and delivers the
best testing accuracy among all the algorithms evaluated in this work.
For BeiDou data, the machine learning results are presented in Table III. Similar to
the results of GPS data, random forest and gradient boosting suﬀer from overﬁtting with
a signiﬁcant drop of 6 .96% and 5 .75% from training to testing accuracies, respectively.
AdaBoost maintains the most stable accuracies between trai ning and testing results and
achieves the highest testing accuracy at 70.43%.
Machine learning performance for GPS data is better than tha t for BeiDou data which
might be reﬂected on positioning accuracy. Since random for est and AdaBoost achieve
comparable testing accuracies, the following section will consider positioning results of these
two algorithms. We will start with an analysis of activation functions, since they signiﬁcantly
aﬀect positioning accuracy.

21
TABLE III: Machine learning results for BeiDou with Hong Kon g Dataset.
Random Forest AdaBoost Gradient Boosting
Training Accuracy 0.7595 0.7133 0.7446
Testing Accuracy 0.7020 0.7043 0.6750
2) Activation Function Analysis: In the proposed framework, activation functions are used
to map predicted scores by a machine learning algorithm to we ights for WLS positioning
calculation.. Figure 7 presents the weight distribution of GPS testing data after applying the
activation functions on AdaBoost predicted scores. Figure 7a presents the weight ditribution
for the constant activation function of Figure 4 where the we ights of all signals are unity.
Figure 7b employes the linear function from Figure 4 which di rectly assigns the predicted
scores from AdaBoost results to WLS weights without any proc essing. The predicted scores
are within a narrow interval between 0.4 to 0.7, and hence the use of this activation functionn
results in a small variation among the assigned weights. Whe n the weights become nearly
identical, the WLS algorithm reduces to OLS which diminishe s the intended advantage
of weighting. Figure 7c illustrates the weight distributio n corresponding to the unit step
activation function of Figure 4 where the threshold is set to the mean predicted scores
for a given epoch. This case is equivalent to a satellite sele ction algorithms that calculates
an OLS solution using satellite subsets. The weight distrib ution shows that nearly half
of the measurements are excluded from producing solutions, that can seriously degrade
the satellite geometry. The weight distribution of the ReLU function avoids deteriorating
satellite geometry by eliminating only the signal with the l owest predicted score as shown
in Figure 7d. The weights of remaining signals are linearly m apped to the range [0,1]. To
further amplify the diﬀerence between weights of signals wh ile excluding signals of extremely
low quality, the sigmoid function is employed. In Figure 7e a nd Figure 7f we present the
weight distribution of sigmoid functions with parameters b = 50 and b = 100, respectively.
When the parameter b increases, more measurements are pushed towards the extrem e values
0 and 1 while the remaining signals have weights more evenly d istributed between these two
values. Rather than directly excluding low-quality signal s, the sigmoid function gradually
reduces their weights in accordance with their predicted qu ality. This soft approach preserves
potentially useful measurements while still limiting thei r inﬂuence on the WLS solution.

22
As a result, a sigmoid function can eﬀectively reject poor qu ality signals while preserving
satellite geometry. In addition, the widely spread weight d istribution produced by a sigmoid
function is preferred over a concentrated distribution pro duced by a linear function, since it
enables WLS to better distinguish between high and low quali ty signals, thereby improving
positioning accuracy. With all the advantages described, t he sigmoid function can outperform
other activation functions selected in this study. While Re LU might also be able to improve
positioning accuracy by excluding the lowest quality signa l, its improvement might not be
as large compared to a sigmoid function due to a more concentr ated weight distribution.
In the following positioning results analysis, the constan t function will serve as the baseline
and results of ReLU and sigmoid functions will be compared.
3) GPS-only Positioning Results: The impact of the shaping parameter b of the sigmoid
function on positioning performance has been evaluated for values ranging from b = 1 to
b = 200. Using the random forest predicted scores, the optimal performance occurs at b = 27
with a 3D RMSE of 167.627 (m). For the AdaBoost predicted scor es, the minimum 3D RMSE
of 164.803 (m) is achieved when b = 108. The diﬀerence in the optimal values of parameter
b arises from the distinct predicted scores distributions pr oduced by the random forest and
AdaBoost algorithms. In the subsequent positioning analys is, the sigmoid function with the
optimal values of parameter b is used.
Figure 8 presents the overall 3D RMSE of GPS-only positionin g results. The baseline
3D RMSE produced by the constant activation function is arou nd 192 (m). The best set
refers to the satellite subset that yields the minimum 3D RMS E among all possible subset
combinations. “AdaBoost ReLU” and “Random Forest ReLU” res ults are 61.35% and 49.68%
respectively from baseline towards the best set. “AdaBoost Sigmoid” and “Random Forest
Sigmoid” results show an even larger improvement of 75.52% a nd 67.68% respectively from
the baseline towards the best set results. These results dem onstrate that all the proposed
methods eﬀectively enhance positioning accuracy when usin g single constellations, while
AdaBoost performs better than random forest. The fact that t he sigmoid function performs
better than ReLU also aligns well with our activation functi on analysis.
Figure 9 presents the 3D positioning errors using AdaBoost p redicted scores. This ﬁgure
includes only the epochs with available positioning soluti ons, i.e., those with four or more
signals available. The positioning errors produced by the R eLU and sigmoid activation
functions are generally lower than those of the baseline. In certain epochs, the proposed

23
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
Weight
0
500
1000
1500
2000
2500
3000
3500
4000Number of measurements
(a)
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
Weight
0
500
1000
1500
2000
2500Number of measurements
(b)
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
Weight
0
500
1000
1500
2000
2500
3000Number of measurements
(c)
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
Weight
0
100
200
300
400
500
600
700
800
900
1000Number of measurements
(d)
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
Weight
0
100
200
300
400
500
600
700
800Number of measurements
(e)
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
Weight
0
200
400
600
800
1000
1200
1400
1600Number of measurements
(f)
Fig. 7: Weight distribution of GPS data with activation func tions: (a) constant (b) linear
(c) unit step (d) ReLU (e) sigmoid a=mean b=50 (f) sigmoid a=m ean b=100.

24
methods achieve performance comparable to that of the best s et. However, the ReLU curve
shows more frequent error spikes and greater variability co mpared to the sigmoid. For
example, “AdaBoost ReLU” generates a peak error at epoch 394 which is caused by the
inaccurate machine learning prediction. In this epoch, GPS space vehicle identiﬁers (SVID)
4, 7, 9, 21, and 27 are available and the best set includes GPS S VID 7, 9, 21, and 27.
However, ReLU activation function assigns zero weight to go od quality GPS SVID 27 signal
and the remaining GPS SVID 4, 7, 9, 21 signals produce large po sitioning error. When only
a few satellites are available, each one has a greater inﬂuen ce on the ﬁnal WLS solution.
In such cases, excluding a high-quality satellite signal an d including a low-quality one can
substantially reduce positioning accuracy.
3D RMSE
Best set
155.9832 (m)
0%
AdaBoost
Sigmoid
164.8031 (m)
24.48%
Random Forest
Sigmoid
167.6269 (m)
32.32%
AdaBoost
ReLU
169.9064 (m)
38.65%
Random Forest
ReLU
174.11 (m)
50.32%
Constant
192.0091 (m)
100%
Fig. 8: 3D RMSE of GPS-only positioning using Medium Urban da ta.
0 100 200 300 400 500 600
Epoch (s)
0
200
400
600
800
1000
12003D Positioning Error (m)
Best Set
AdaBoost Sigmoid
AdaBoost ReLU
Constant
0 50 100
0
100
200
X 394
Y 785.186
Fig. 9: 3D errors of GPS-only positioning using Medium Urban data.

25
4) GPS+BeiDou Positioning Results: In multi-constellation positioning using GPS and
BeiDou data, the optimal values of the parameter b in the sigmoid functions are b = 12 and
b = 120 for random forest and AdaBoost predicted scores, respe ctively. Figure 10 presents the
3D RMSE results for GPS+BeiDou positioning. It is seen that “ AdaBoost Sigmoid” achieves
the best performance which improves the 3D RMSE by 53.78% fro m baseline towards the
optimal set. “Random forest sigmoid” also demonstrates a mo derate improvement of 37.07%
while “Random forest ReLU” and “AdaBoost ReLU” show similar improvement of around
26% from baseline towards the best set. Using GPS and Beidou d ata together results in a
lower improvement in 3D RMSE compared to the that achieved in GPS-only positioning.
This can be attributed to the relatively lower machine learn ing accuracy of BeiDou data
compared to that of GPS data as shown in Table II and III. Multi ple constellations do not
aleays produce more accurate results than single constella tions.
Figure 11 presents 3D errors of multi-constellation positi oning results using AdaBoost
predicted scores. The overall trends of “AdaBoost Sigmoid” and “AdaBoost ReLU” generate
lower 3D positioning error than the baseline results. These results indicate that machine
learning algorithms can eﬀectively predict signals qualit y scores, while activation functions
convert these predicted scores into suitable weights for WL S positioning that reduce errors.
Among the activation functions, “AdaBoost Sigmoid” perfor ms better than “AdaBoost
ReLU” across most of the epochs. Furthermore, as shown in the zoomed-in section in Figure
11, the performance of “AdaBoost Sigmoid” indicated by the o range line approaches that of
best set indicated by the blue line. Since the ReLU activatio n function excludes only a single
signal in each epoch, its impact on positioning performance may be limited when a large
number of signals are available in multi-constellation pos itioning. In contrast, the sigmoid
function can assign near-zero weights to multiple low-qual ity signals while amplifying the
weight contrast between measurements to enhance the distin ction between signals. These
characteristics make sigmoid function more eﬀective in enh ancing positioning accuracy.
3D RMSE
Best set
43.8732 (m)
0%
AdaBoost
ReLU
98.4515 (m)
75.35%
AdaBoost
Sigmoid
77.3521 (m)
46.22%
Random
forest
ReLU
96.6684 (m)
72.89%
Random forest
Sigmoid
89.4573 (m)
62.93%
Constant
116.3093 (m)
100%
Fig. 10: 3D RMSE of GPS+BeiDou positioning using Medium Urba n data.

26
0 100 200 300 400 500 600 700 800
Epoch (s)
0
100
200
300
400
500
600
700
8003D Positioning Error (m)
Best Set
AdaBoost Sigmoid
AdaBoost ReLU
Constant
550 560 570 580 590 600
0
100
200
Fig. 11: 3D errors of GPS+Beidou positioning using Medium Ur ban data.
5) Comparison of Single- and Multi-constellations: Figure 12 presents 3D positioning
errors and time availability of GPS-only, BeiDou-only and G PS+BeiDou conﬁgurations with
their respective best-performing combination of machine l earning algorithm and activation
function. The time availability results indicate that inco rporating both GPS and BeiDou
satellites enables position solutions to be obtained in nea rly all epochs. This improve-
ment stems from the increased number of available signals, w hich reduces the likelihood
of encountering epochs with insuﬃcient number of signal for a solution. In contrast, single-
constellation GNSS conﬁgurations, such as GPS-only or BeiD ou-only, experience longer and
more frequent gaps in time availability. Despite multi-constellation GNSS providing position-
ing solutions when single-constellation systems lack suﬃc ient signals for LS computation,
the 3D errors of the positioning results are usually large, a s observed in epochs 237–248.
Such scenarios commonly involve signiﬁcant signal obstruc tion and increased probability of
NLOS/multipath eﬀects. At epochs where positioning soluti ons are available for all conﬁg-
urations, GPS+BeiDou results typically produce 3D errors t hat fall below or between the
errors observed in GPS-only and BeiDou-only results. When o ne of these two constellation
provide much worse results than the other constellation, us ing these two together will provide

27
degraded results compared to using only the better constell ation. Hence to exploit the two
constellations in order to have results better than any sing le one, the performance of each
one must be satisfactory.
0 100 200 300 400 500 600 700 800
Epoch (s)
0
100
200
300
400
500
600
700
8003D Positioning Error (m)
GPS-only AdaBoost Sigmoid
BeiDou-only Random Forest Sigmoid
GPS+BeiDou AdaBoost Sigmoid
400 420 440 460 480 500
0
100
200
300
400
0 100 200 300 400 500 600 700
Epoch (s)
Availability
Fig. 12: Single and multi-constellation 3D positioning err ors and time availabilities
comparison.
D. Results of Shinjuku Data Using Odaiba Training Set
The Tokyo dataset is utilized to assess the generalization a bility of the proposed algorithm
across diﬀerent geographical locations. In the following a nalysis, Odaiba data are used for
machine learning training and Shinjuku data are used for tes ting. We focus exclusively on
the best-performing AdaBoost algorithm for evaluation.
1) Machine Learning Results: Table IV summarizes the training and testing accuracies of
AdaBoost. The training accuracy is approximately 10% highe r than the testing accuracy for
both GPS and BeiDou data. This can be caused by the environmen t diﬀerences between the
training data and testing data. The Odaiba dataset includes mainly measurements collected

28
in open areas, where NLOS and multipath errors are less likel y to occur while the Shinjuku
dataset contains signals collected in dense urban environm ents with a higher possibility
of such errors. Consequently, in this case machine learning models do not generalize well
to detect degraded signals, leading to a noticeable reducti on in accuracy from training to
testing.
TABLE IV: Machine learning results with Odaiba training set and Shinjuku testing set.
AdaBoost GPS BeiDou
Training Accuracy 0.7910 0.7551
Testing Accuracy 0.6999 0.6596
2) GPS+BeiDou Positioning Results: The best parameter of the sigmoid function is b =
47 for GPS+BeiDou Shinjuku data and it results in a 3D RMSE of 1 25.586 (m). The 3D
RMSE of the proposed algorithm with respect to baseline and b est set is shown in Figure
13. The “AdaBoost Sigmoid” algorithm produces a 3D RMSE whic h is 62.02% away from
the best set. While this represents an improvement, it is les s signiﬁcant compared to the
previous cases, where the gap from the best set was reduced to 46.22% for GPS+BeiDou
positioning and 24.48% for GPS-only positioning, relative to the baseline, in medium urban
Hong Kong data. This can be the result of the lower machine lea rning testing accuracy. The
AdaBoost testing accuracies of Shinjuku GPS data and BeiDou data in Table IV are 6.7%
and 4.47% lower than those in Hong Kong medium urban dataset i n Table II and III. The
3D RMSE of “AdaBoost ReLU” is not shown in Figure 13 as it reach es 236.13 (m) which is
1.7 times larger than the baseline 3D RMSE. This is due to the p resence of multiple large
error peaks, one of which reaches 8440.47 (m).
Figure 14 presents 3D errors of multi-constellation positi oning results using AdaBoost pre-
dicted scores. For most epochs, “AdaBoost Sigmoid” and “Ada Boost ReLU” yield smaller 3D
positioning errors compared to the baseline. However, peak errors occur more frequently with
the “AdaBoost Sigmoid” and “AdaBoost ReLU” methods, during which their positioning
errors exceed the baseline errors. This outcome may be expla ined by the inaccurate machine
learning predictions due to relatively low testing accurac y. For example, between epochs 771
and 843, the “AdaBoost Sigmoid” and “AdaBoost ReLU” methods produce higher 3D errors
than the baseline. In epoch 801, the available signals are fr om GPS SVID 10, 12, 15, 20, 24,

29
25, 32 and BeiDou SVID 6, 7, 9, 16, 24, 25. The LS solution using all available satellites
yields a 3D error of 73.6675 (m). The best set includes GPS SVI D 10, 15 and BeiDou SVID
6, 7, 16 which generates a 3D error of 4.7112 (m). The “AdaBoos t Sigmoid” method assigns
weights above 0.6 to GPS SVIDs 10, 20, and 25, as well as BeiDou SVIDs 7, 16, and 24. This
weight distribution is inconsistent with the best set which leads to a 3D RMSE of nearly
139 (m). This epoch demonstrates the inﬂuence of machine lea rning prediction accuracy on
the resulting positioning errors.
3D RMSE
Best set
106.0391 (m)
0%
AdaBoost
Sigmoid
125.586 (m)
62.02%
Constant
137.5587 (m)
100%
Fig. 13: 3D RMSE of GPS+BeiDou positioning using Shinjuku da ta.
0 200 400 600 800 1000 1200 1400 1600 1800 2000
Epoch (s)
0
100
200
300
400
500
6003D Positioning Error (m)
Best Set
AdaBoost ReLU
AdaBoost Sigmoid
Constant
1200 1250 1300
0
100
200
Fig. 14: 3D errors of GPS-only positioning using Shinjuku da ta.
E. Results of Shinjuku Data Using Hong Kong Training Set
To assess the applicability of the proposed method when the m achine learning model is
trained in a diﬀerent geographical location with similar ur banization levels, the Hong Kong

30
training set and the Shinjuku testing set are employed in the following analysis. Our analysis
focuses on the performance of the proposed method using the b est-performing AdaBoost
algorithm.
1) Machine Learning Results: The training and testing accuracies of AdaBoost algorithm
are presented in Table V. The testing accuracy improves by 4. 24% for GPS data and 6.95%
for BeiDou data compared to the results in Table IV where the O daiba dataset is used
as the training set. This improvement suggests that trainin g a machine learning model
on data collected in an urban environment similar to the test ing conditions can eﬀectively
enhance the testing accuracy. Furthermore, the AdaBoost al gorithm achieves similar training
and testing accuracies which suggests that the model genera lizes well to testing data. The
accuracy problem observed when using the Odaiba training se t is not present when the
model is trained on the Hong Kong dataset.
TABLE V: Machine Learning Results with Hong Kong training se t and Shinjuku testing
set.
AdaBoost GPS BeiDou
Training Accuracy 0.7603 0.7133
Testing Accuracy 0.7424 0.7291
2) GPS+BeiDou Positioning Results: The optimal value of for the sigmoid function
parameter is b = 57 which produces a 3D RMSE of 123.1257 (m). Figure 15 illust rates the 3D
RMSE of proposed methods. The 3D RMSE of “AdaBoost Sigmoid” m ethod is 54.21% away
from the best set relative to the baseline. This represents a n improvement of 7.81% closer to
the best set compared with the results obtained when using th e Odaiba dataset for training.
This result highlights the beneﬁt of training the model with data collected in environments
of comparable urbanization levels. Despite the geographic al distance between Hong Kong
and Tokyo, both Hong Kong training data and Shinjuku testing data are collected in
dense urban environments, which leads to improved machine l earning generalization and
enhanced positioning performance. These results demonstr ate that the proposed algorithms
are applicable across diﬀerent geographical locations. Ho wever, “AdaBoost ReLU” method
is not shown in the ﬁgure as it results in a 3D RMSE of 143.8039 ( m) which exceeds the
baseline 3D RMSE. This can be attributed to the peak errors th at are larger than 3000 (m)

31
in 4 of the epochs.
Figure 16 presents 3D errors of GPS+BeiDou positioning usin g AdaBoost predicted scores.
Overall, the “AdaBoost Sigmoid” and “AdaBoost ReLU” method s achieve lower 3D errors
than the baseline which demonstrates both the eﬀectiveness of the proposed algorithm and
its applicability when the training data are obtained from g eographically distant locations
relative to the testing data. Compared to Figure 14, we can ob serve that the 3D errors
of “AdaBoost Sigmoid” in Figure 16 are lower. The diﬀerences between these two results
demonstrate the importance of selecting training data and i ts impact on positioning accu-
racy. However, there are still epochs where the proposed alg orithms results in larger 3D
errors than the baseline due to the inaccurate machine learn ing prediction.
The results from Hong Kong training data show that the propos ed method does not require
training with datasets from every new site. Instead, a model trained on data collected in
an environment with a similar level of urbanization is appli cable to other locations under
comparable conditions. This characteristic reduces the ne ed of location-speciﬁc datasets,
allowing the overall dataset size to remain relatively smal l.
3D RMSE
Best set
106.0391 (m)
0%
AdaBoost
Sigmoid
123.1257 (m)
54.21%
Constant
137.5587 (m)
100%
Fig. 15: 3D RMSE of GPS+BeiDou positioning using Shinjuku da ta.
V. Conclusion
This study proposes ensemble-based machine learning-aide d WLS algorithms within a
novel activation function framework. Six signal quality in dicators are employed as machine
learning input features to diﬀerentiate the quality of meas urements. Ensemble machine
learning algorithms, including random forest, AdaBoost an d gradient boosting, are used to
learn the relationship between selected features and optim al satellite subset. The activation
functions are then used to transform the predicted scores fr om machine learning output
into appropriate weights for WLS positioning. The proposed algorithms are evaluated using
real-world datasets from two diﬀerent locations, Hong Kong and Tokyo. Firstly, Hong Kong
harsh urban and deep urban data are used for training and Hong Kong medium urban

32
0 200 400 600 800 1000 1200 1400 1600 1800 2000
Epoch (s)
0
100
200
300
400
500
6003D Positioning Error (m)
Best Set
AdaBoost ReLU
AdaBoost Sigmoid
Constant
550 600 650
0
100
200
Fig. 16: 3D errors of GPS-only positioning using Shinjuku da ta.
data are used for testing. We demonstrate that AdaBoost algo rithm performs better than
random forest and sigmoid function outperforms ReLU. The 3D RMSE of best performing
“AdaBoost Sigmoid” results are 24.48% and 46.32% away from t hat of the best set for GPS-
only and GPS+BeiDou positioning, respectively. This shows the proposed algorithms are
eﬀective in assigninig proper weigths to degraded signals i n challenging urban environments
which lead to improved positioning accuracy. Secondly, we c onducted the experiment using
Odaiba training set and Shinjuku testing set. The 3D RMSE of “ AdaBoost Sigmoid” result is
62.02% away from best set for GPS+BeiDou positioning. Due to the environment diﬀerence
in training and testing data, the improvement is not as signi ﬁcant as previous case. Lastly,
the Hong Kong training data and Shinjuku testing data are use d, both of which were
collected in dense urban areas despite their diﬀerent geogr aphical locations. The 3D RMSE
of “AdaBoost Sigmoid” result is 54.21% away from best set for GPS+BeiDou positioning.
In comparison with the previous case, this result proves tha t training with data collected
from environments that share a similar level of urbanizatio n with the testing data can lead
to better performance.
Future work includes the integration of GNSS with inertial n avigation systems (INS) using

33
techniques such as Kalman ﬁltering and factor graph optimiz ation within the proposed ma-
chine learning–based activation function framework to fur ther enhance positioning accuracy
and time availability in challenging environments. The sha pe of the used activation function
is critical in obtaining good results. In our work we show tha t Sigmoid activation functions
provide good results for the data sets we ued. An interesting future research direction could
be the use of machine learning techniques to adaptively sele ct (or build) optimal activation
functions, matching the parameters to the environment and o verall signal quality.
Acknowledgements
The GNSS datasets that are used in this paper are obtained fro m open-source UrbanNav
repository collected by the Intelligent Positioning and Na vigation Laboratory. UrbanNav
datasets can be downloaded from https://github.com/IPNL-POLYU/UrbanNavDataset. The
authors thank the members of the Intelligent Positioning an d Navigation Laboratory led by
Dr. Li-Ta Hsu from The Hong Kong Polytechnique University fo r collecting and making
UrbanNav dataset available.
References
[1] C. J. Hegarty and E. Chatre, “Evolution of the global navi gation satellitesystem (gnss),” Proceedings of the
IEEE, vol. 96, no. 12, pp. 1902–1917, 2009.
[2] C. Fernandez-Prades, L. L. Presti, and E. Falletti, “Sat ellite radiolocalization from GPS to GNSS and beyond:
Novel technologies and applications for civil mass market, ” Proceedings of the IEEE , vol. 99, no. 11, pp. 1882–
1904, 2011.
[3] D. Egea-Roca, M. Arizabaleta-Diez, T. Pany, F. Antreich , J. A. Lopez-Salcedo, M. Paonni, and G. Seco-
Granados, “GNSS user technology: State-of-the-art and fut ure trends,” IEEE Access, vol. 10, pp. 39 939–39 968,
2022.
[4] F. Zangenehnejad and Y. Gao, “GNSS smartphones position ing: Advances, challenges, opportunities, and future
perspectives,” Satellite navigation , vol. 2, no. 1, p. 24, 2021.
[5] A. Siemuri, K. Selvan, H. Kuusniemi, P. V¨ alisuo, and M. S . Elmusrati, “Improving precision gnss positioning and
navigation accuracy on smartphones using machine learning ,” in Proceedings of the 34th International Technical
Meeting of the Satellite Division of The Institute of Naviga tion (ION GNSS+ 2021) , 2021, pp. 3081–3093.
[6] R. Jin, G. Zhang, L.-T. Hsu, and Y. Hu, “A survey on coopera tive positioning using GNSS measurements,”
IEEE Transactions on Intelligent Vehicles , vol. 9, no. 11, pp. 7402–7429, 2024.
[7] Y. He, J. Li, and J. Liu, “Research on GNSS INS & GNSS/INS in tegrated navigation method for autonomous
vehicles: A survey,” IEEE Access, vol. 11, pp. 79 033–79 055, 2023.
[8] Y. Lu, H. Ma, E. Smart, and H. Yu, “Real-time performance- focused localization techniques for autonomous
vehicle: A review,” IEEE Transactions on Intelligent Transportation Systems, vol. 23, no. 7, pp. 6082–6100, 2021.

34
[9] O. K. Isik, I. Petrunin, G. Inalhan, A. Tsourdos, R. V. Mor eno, and R. Grech, “A Machine Learning Based
GNSS Performance Prediction for Urban Air Mobility Using En vironment Recognition,” in 2021 IEEE/AIAA
40th Digital Avionics Systems Conference , Oct. 2021, pp. 1–5.
[10] L.-T. Hsu, “Analysis and modeling GPS NLOS eﬀect in high ly urbanized area,” GPS Solutions , vol. 22, no. 1,
p. 7, Nov. 2017. [Online]. A vailable: https://doi.org/10. 1007/s10291-017-0667-9
[11] P. D. Groves and Z. Jiang, “Height Aiding, C/N0 Weightin g and Consistency Checking for GNSS NLOS and
Multipath Mitigation in Urban Areas,” The Journal of Navigation , vol. 66, no. 5, pp. 653–669, Sep. 2013.
[12] P. J. Teunissen and O. Montenbruck, Eds., Springer Handbook of Global Navigation Satellite Systems . Cham:
Springer International Publishing, 2017, pp. 3-23, 433-43 4, 444-503, 639-660.
[13] C. Dussault, R. Courtois, J.-P. Ouellet, and J. Huot, “I nﬂuence of Satellite Geometry and Diﬀerential Correction
on GPS Location Accuracy,” Wildlife Society Bulletin (1973-2006) , vol. 29, no. 1, pp. 171–179, 2001.
[14] T. Ozeki and N. Kubo, “GNSS NLOS Signal Classiﬁcation Ba sed on Machine Learning and Pseudorange Residual
Check,” Frontiers in Robotics and AI , vol. 9, May 2022, art. no. 868608.
[15] A. Kirmaz, D. S. Michalopoulos, I. Balan, and W. Gerstac ker, “LOS/NLOS Classiﬁcation Using Scenario-
Dependent Unsupervised Machine Learning,” in 2021 IEEE 32nd Annual International Symposium on Personal,
Indoor and Mobile Radio Communications (PIMRC) , Sep. 2021, pp. 1134–1140.
[16] T. Suzuki and Y. Amano, “NLOS Multipath Classiﬁcation o f GNSS Signal Correlation Output Using Machine
Learning,” Sensors, vol. 21, no. 7, Jan. 2021, art. no. 2503.
[17] L. Li, M. Elhajj, Y. Feng, and W. Y. Ochieng, “Machine lea rning based GNSS signal classiﬁcation and weighting
scheme design in the built environment: a comparative exper iment,” Satellite Navigation , vol. 4, no. 1, May 2023,
art. no. 12.
[18] O. Garc ´ ıa Crespillo, J. C. Ruiz-Sicilia, A. Kliman, an d J. Marais, “Robust design of a machine learning-based
GNSS NLOS detector with multi-frequency features,” Frontiers in Robotics and AI , vol. 10, Jul. 2023, art. no.
1171255.
[19] S. Ali, T. Abuhmed, S. El-Sappagh, K. Muhammad, J. M. Alo nso-Moral, R. Confalonieri, R. Guidotti, J. Del Ser,
N. D ´ ıaz-Rodr ´ ıguez, and F. Herrera, “Explainable Artiﬁcial Intelligence (XAI): What we know and what is left
to attain Trustworthy Artiﬁcial Intelligence,” Information Fusion, vol. 99, Nov. 2023, art. no. 101805.
[20] L. Li, Z. Xu, Z. Jia, L. Lai, and Y. Shen, “An eﬃcient GNSS N LOS signal identiﬁcation and processing method
using random forest and factor analysis with visual labels, ” GPS Solutions , vol. 28, no. 2, p. 77, Feb. 2024.
[21] H. Xu, A. Angrisano, S. Gaglione, and L.-T. Hsu, “Machin e learning based LOS/NLOS classiﬁer and robust
estimator for GNSS shadow matching,” Satellite Navigation , vol. 1, no. 1, May 2020, art. no. 15.
[22] S. R. S. J. Koiloth, D. S. Achanta, and P. R. Koppireddi, “ ML-based LOS/NLOS/multipath signal classiﬁers
for GNSS in simulated multipath environment,” Aerospace Systems, vol. 7, no. 2, pp. 237–250, Jun. 2024.
[23] A. Tabatabaei, M. R. Mosavi, A. Khavari, and H. S. Shahho seini, “Reliable Urban Canyon Navigation Solution
in GPS and GLONASS Integrated Receiver Using Improved Fuzzy Weighted Least-Square Method,” Wireless
Personal Communications, vol. 94, no. 4, pp. 3181–3196, Jun. 2017.
[24] H.-F. Ng, G. Zhang, K.-Y. Yang, S.-X. Yang, and L.-T. Hsu , “Improved weighting scheme using consumer-level
GNSS L5/E5a/B2a pseudorange measurements in the urban area ,” Advances in Space Research, vol. 66, no. 7,
pp. 1647–1658, Oct. 2020.
[25] M. A. Akram, P. Liu, Y. Wang, and J. Qian, “GNSS Positioni ng Accuracy Enhancement Based on Robust
Statistical MM Estimation Theory for Ground Vehicles in Cha llenging Environments,” Applied Sciences, vol. 8,
no. 6, p. 876, Jun. 2018, number: 6 Publisher: Multidiscipli nary Digital Publishing Institute.

35
[26] L. Li, J. Zhong, and M. Zhao, “Doppler-Aided GNSS Positi on Estimation With Weighted Least Squares,” IEEE
Transactions on Vehicular Technology, vol. 60, no. 8, pp. 3615–3624, Oct. 2011.
[27] Y. Li, C. Cai, and Z. Xu, “A Combined Elevation Angle and C /N0 Weighting Method for GNSS PPP on Xiaomi
MI8 Smartphones,” Sensors, vol. 22, no. 7, p. 2804, Apr. 2022.
[28] J. Li and M. Wu, “The Improvement of Positioning Accurac y with Weighted Least Square Based on SNR,” in
2009 5th International Conference on Wireless Communicati ons, Networking and Mobile Computing , Sep. 2009,
pp. 1–4, iSSN: 2161-9654.
[29] Z. Lyu and Y. Gao, “An SVM Based Weight Scheme for Improvi ng Kinematic GNSS Positioning Accuracy with
Low-Cost GNSS Receiver in Urban Environments,” Sensors, vol. 20, no. 24, p. 7265, Dec. 2020.
[30] P.-H. Lee and H. Leib, “Machine learning based multi-co nstellation satellite selection algorithm in urban area,”
in AIAA/DATC IEEE 44th Digital Avionics Systems Conference (D ASC), 2025, pp. 1–10.
[31] P.-H. Lee, “Machine Learning Techniques for Multi-GNS S Positioning,” Master’s thesis, McGill University,
Montreal, Quebec, Canada, October 2025.
[32] P. D. Groves, Principles of GNSS, Inertial, and Multisensor Integrated N avigation Systems , 2nd ed. Boston:
Artech House, Jan. 2013, pp. 349-436.
[33] Z. Zhang, B. Li, Y. Shen, Y. Gao, and M. Wang, “Site-Speci ﬁc Unmodeled Error Mitigation for GNSS Positioning
in Urban Environments Using a Real-Time Adaptive Weighting Model,” Remote Sensing , vol. 10, no. 7, Jul.
2018, art. no. 1157.
[34] G. Li, C. Xu, P. Zhang, and C. Hu, “A Modiﬁed Satellite Sel ection Algorithm Based on Satellite Contribution
for GDOP in GNSS,” in Advances in Mechanical and Electronic Engineering , D. Jin and S. Lin, Eds. Berlin,
Heidelberg: Springer, 2012, pp. 415–421.
[35] R. Yarlagadda, I. Ali, N. Al-Dhahir, and J. Hershey, “GP S GDOP metric,” IEE Proc. - Radar, Sonar and Navig. ,
vol. 147, no. 5, pp. 259–264, Oct. 2000.
[36] D. Borio, C. Gioia, and N. Mitchison, “Identifying a low -frequency oscillation in Galileo IOV pseudorange rates,”
GPS Solutions , vol. 20, no. 3, pp. 363–372, Jul. 2016.
[37] L.-T. Hsu, “GNSS multipath detection using a machine le arning approach,” in 2017 IEEE 20th International
Conference on Intelligent Transportation Systems , Oct. 2017, pp. 1–6.
[38] I. Goodfellow, Y. Bengio, and A. Courville, Deep Learning. Cambridge, Mass: The MIT Press, 2016, pp. 1-28.
[39] A. Kumar and M. Jain, Ensemble Learning for AI Developers: Learn Bagging, Stacki ng, and Boosting Methods
with Use Cases . Berkeley, CA: Apress Publishers, 2020, pp. 11-29, 49-60.
[40] G. Bonaccorso, Mastering Machine Learning Algorithms - Second Edition , 2nd ed. Birmingham: Packt
Publishing, Jan. 2020.
[41] E. Alpaydin, Introduction to Machine Learning, fourth edition , 4th ed. Cambridge, Massachusetts London: The
MIT Press, Mar. 2020, pp. 173-180, 351-372.
[42] Z.-H. Zhou, Machine Learning, 1st ed. Singapore: Springer, Aug. 2022, pp. 79-102, 181-21 0.
[43] ——, Ensemble Methods: Foundations and Algorithms , 1st ed. Chapman & Hall/CRC, May 2012, pp. 23-46.
[44] Y. Freund and R. E. Schapire, “A Decision-Theoretic Gen eralization of On-Line Learning and an Application
to Boosting,” Journal of Computer and System Sciences , vol. 55, no. 1, pp. 119–139, Aug. 1997.
[45] J. H. Friedman, “Greedy function approximation: A grad ient boosting machine. ”The Annals of Statistics, vol. 29,
no. 5, pp. 1189–1232, Oct. 2001.
[46] A. M. Saxe, Y. Bansal, J. Dapello, M. Advani, A. Kolchins ky, B. D. Tracey, and D. D. Cox, “On the information

36
bottleneck theory of deep learning,” Journal of Statistical Mechanics: Theory and Experiment , vol. 2019, no. 12,
p. 124020, Dec. 2019.
[47] S. R. Dubey, S. K. Singh, and B. B. Chaudhuri, “Activatio n functions in deep learning: A comprehensive survey
and benchmark,” Neurocomputing, vol. 503, pp. 92–108, Sep. 2022.
[48] S. Sharma, S. Sharma, and A. Athaiya, “ACTIV ATION FUNCT IONS IN NEURAL NETWORKS,” Interna-
tional Journal of Engineering Applied Sciences and Technol ogy, vol. 04, no. 12, pp. 310–316, May 2020.
[49] L.-T. Hsu, F. Huang, H.-F. Ng, G. Zhang, Y. Zhong, X. Bai, and W. Wen, “Hong Kong UrbanNav: An Open-
Source Multisensory Dataset for Benchmarking Urban Naviga tion Algorithms,” NA VIGATION: Journal of the
Institute of Navigation , vol. 70, no. 4, Dec. 2023.
[50] Natural Resources Canada, “Canadian Spatial Referenc e System Precise Point Positioning (CSRS-PPP). ”
[Online]. A vailable: https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/tools-outils/ppp.php
