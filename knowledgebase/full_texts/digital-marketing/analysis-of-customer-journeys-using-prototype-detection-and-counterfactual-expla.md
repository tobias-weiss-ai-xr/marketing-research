---
title: Analysis of Customer Journeys Using Prototype Detection and Counterfactual Explanations for Sequential
  Data
url: https://arxiv.org/abs/2505.11086
category: digital-marketing
subcategory: empirical
date: 2025-05
venue: ''
authors:
- Keita Kinjo
source: arxiv
pdf_url: https://arxiv.org/pdf/2505.11086
pages: 19
chars: 42704
fetched_at: '2026-11-08T13:17:33+00:00'
kb_version: 1
---

# Analysis of Customer Journeys Using Prototype Detection and Counterfactual Explanations for Sequential Data

arXiv:2505.11086v1  [cs.AI]  16 May 2025
Analysis of Customer Journeys Using Prototype
Detection and Counterfactual Explanations for
Sequential Data
Keita Kinjo ∗
Faculty of Business, Kyoritsu Women’s University
2-2-1, Hitotsubashi, Chiyoda-ku, Tokyo, 101-8437, Japan
Abstract
Recently, the proliferation of omni-channel platforms has attracted interest in cus-
tomer journeys, particularly regarding their role in devel oping marketing strategies.
However, few eﬀorts have been taken to quantitatively study o r comprehensively ana-
lyze them owing to the sequential nature of their data and the complexity involved in
analysis. In this study, we propose a novel approach compris ing three steps for analyz-
ing customer journeys. First, the distance between sequent ial data is deﬁned and used
to identify and visualize representative sequences. Secon d, the likelihood of purchase
is predicted based on this distance. Third, if a sequence sug gests no purchase, coun-
terfactual sequences are recommended to increase the proba bility of a purchase using
a proposed method, which extracts counterfactual explanat ions for sequential data. A
survey was conducted, and the data were analyzed; the result s revealed that typical
sequences could be extracted, and the parts of those sequenc es important for purchase
could be detected. We believe that the proposed approach can support improvements
in various marketing activities.
Keywords: counterfactual explanation, customer journeys, sequential d ata, clustering, Lev-
enshtein distance, visualization, marketing research
1 Introduction
Consumer environments have become increasingly complex in recent years, with various
options being oﬀered for gaining increased product awareness, ga thering information, making
purchases, and sharing product reviews. Awareness can be raise d via not only mass media
but also web advertisements and social media. Physical stores, so cial media, and comparison
sites are used for information gathering. Consumers perform pur chases through multiple
∗Email: kkinjo@kyoritsu-wu.ac.jp; ORCID: 0000-0001-5907-3501
1

channels and omni-channels, including online e-commerce sites and ph ysical stores [3, 22].
Subsequently, they commonly share product reviews on social med ia and online sites.
A customer journey is a method for analyzing consumer perception s and behavior [18].
This is a typology of a particular sequence of consumer cognition and behavior that compa-
nies use in marketing strategies [11, 30, 23]. By analyzing customer j ourneys, companies can
better understand consumers and design consumer experiences more eﬃciently [17]. Speciﬁc
patterns in customer journeys have been frequently extracted through qualitative research.
However, the number of studies that quantitatively analyze or for malize customer journeys
remains limited.
One of the few to quantitatively analyze customer journeys, Rose nbaum et al. (2017)
investigated the frequency of consumer cognition and behavior at each stage of consump-
tion (pre-purchase, purchase, post-purchase) [25]. There ar e several studies similar to these
[30]. However, the length of the customer journey of each individua l is diﬀerent, and the
corresponding data should be sequential in several stages. Howe ver, since sequential data
are diﬃcult to handle in tabular data analysis, there has been limited re lated research. For
example, Herhausen et al. simply counted customer journey patte rns [13].
One of the few to formalize customer journeys, Bernard and Andr itsos (2017) did so
(deﬁning the data structure using trees) in a process mining frame work [4]. Other studies
have employed Markov models, mixed Markov models, edit distances b etween sequences, or
genetic algorithms to detect patterns [1, 12, 5, 6, 33].
Several studies have employed sequence analysis methods based o n inter-sequence dis-
tance measures. For example, Topaloglu, Oztaysi, and Dogan (202 4) analyzed more than
20 million rows of clickstream data collected from a real e-commerce s ite and proposed a
four-stage framework for extracting and interpreting visitor jo urneys. One of these stages
involved clustering based on Levenshtein distance. Their ﬁndings re vealed, among other
insights, that journeys characterized by exploratory behavior e xhibited signiﬁcantly lower
conversion rates than other behavioral patterns [29].
In another study, Bobroske et al. (2020) converted sequences of actions from 10,000
patients into strings and customized the Levenshtein edit-distanc e algorithm to evaluate
similarities between those sequences [7]. Using this distance-based a pproach for clustering,
they identiﬁed twelve representative patient-journey patterns .
Disadvantageously, existing research cannot suitably address th e following issues. First,
it is diﬃcult to extract typical cases from sequential data that hav e a structured nature—such
as the stages of consumption in a customer journey—which diﬀers f rom general, unstructured
sequences. Furthermore, in such cases, it is not only important to extract typical patterns,
but also to compare them with other sequences. To enable such com parisons, the position of
each pattern within the overall sequence space should be visualized and interpreted before
being applied. Marketers need to identify and visualize both typical a nd representative cus-
tomer journeys in order to gain insights into customer needs, unde rstand their perceptions,
and develop eﬀective strategies [8].
In the context of marketing applications, it is necessary not only to extract typical pat-
terns using sequence-based distance measures but also to predic t outcomes such as whether
a purchase will occur. For companies, whether a purchase ultimate ly takes place is a critical
factor [29]. This is because such predictions can help identify which ty pes of sequences are
more likely to lead to purchases and can also be used to estimate outc omes if the sequences
2

are modiﬁed. To achieve this, the application of machine learning meth ods based on se-
quence distance is essential. However, this topic has received limited attention in existing
research.
In addition, it is important to propose how a non-purchasing sequen ce could be improved
to lead to a purchase. Such improved sequences can help uncover t he factors that drive pur-
chasing decisions. In recent years, as many machine learning models —including those using
distance-based approaches—have been criticized for being diﬃcult to interpret or function-
ing as “black boxes,” the ﬁeld of explainable artiﬁcial intelligence (XAI) or interpretable
machine learning has gained signiﬁcant attention [21, 10]. Numerous t echniques have been
developed, including LIME and SHAP [24, 20]. Among these, counterf actual explanation
(CE) has emerged as a promising approach [15, 31]. CE identiﬁes the minimal changes re-
quired in a given instance to alter the prediction of a machine learning m odel. By analyzing
the parts of an instance that must be changed to yield a diﬀerent ou tcome, CE enables
instance-level interpretation of relevant factors. Today, CE me thods are widely used in ﬁelds
such as image analysis and time series prediction. In the context of t ime series data, some
studies have applied distance-based methods such as Dynamic Time W arping (DTW) to
generate counterfactuals that are not only interpretable but als o closer to typical patterns,
thereby ensuring realism [14].
However, these methods are designed for numerical time series da ta. Although a few
attempts have been made to apply CE to symbolic sequence data like t he kind addressed
in this study, they typically rely on mixed-integer linear programming ( MILP), which limits
their applicability to speciﬁc models [28]. To date, no method has been d eveloped that both
supports a wide range of models and generates plausible counterfa ctual sequences.
Therefore, this study proposes an approach with the following thr ee steps. (1) First, the
distances between sequential data are calculated using weighted L evenshtein distance, and
prototypes (typical patterns) are extracted by clustering usin g k-medoids and then visual-
ized. (2) Next, using these distances, predictions are made using n onparametric regression
techniques such as k-nearest neighbor (k-NN). (3) Finally, based on these predictions, mea-
sures are proposed to improve speciﬁc sequences using counterf actual explanation. The
eﬀectiveness of both steps was evaluated using actual survey da ta; based on this, a new
survey method was proposed for obtaining sequential data.
The rest of the manuscript is organized as follows. Section 2 describ es the proposed
method. Then, Section 3 describes the experimental details and th e results, and Section
4 discusses the results with respect to the aim of the study and pre sents the limitations.
Finally, Section 5 provides the concluding remarks.
2 Method
Section 2.1 introduces the problem to be solved in the study, and Sec tion 2.2 describes using
the proposed method to solve it.
3

2.1 Deﬁnition and Problem Setting
We propose the following deﬁnition with reference to customer jour ney studies such as those
of Bernard and Andritsos (2019) and the serial data mining work of Zhang et al. (2001)
[5, 6, 32].
First, let touchpoints be deﬁned as T P = {tp 1, tp2, . . . ,tpe}, where ”touchpoints” refers
to the means and places (e.g., product reviews, social media, e-com merce sites, in-store)
where consumers interact with a product.
Furthermore, let A = {a1, . . . , ah} denote h actions (including no action), such as per-
forming searches, making purchase or non-purchase decisions, a nd writing product reviews.
Let ST = ⟨st 1, . . . ,st m⟩ be a set of m ordered stages, where ”stage” refers to steps in
the consumption process, namely the pre-purchase, purchase, and post-purchase stages.
Then, the qth data point of individual i is represented as X i q ∈ (tp, a; st), where tp ∈ T P ,
a ∈ A, and st ∈ ST .
The sequential data belonging to individual i is denoted by the ordered dataset si =
⟨X i 1, . . . , Xi ni⟩, where ni is the total number of observations for individual i.
The subsequence in which each pair ( tp, a) belongs to the gth stage st g is denoted as
si(st g).
Based on the above deﬁnitions, let S = {s1, s2, . . . , sr} be a set of sequences for r indi-
viduals. Let S(st g) be the set of subsequences si(st g) belonging to stage st g.
Finally, let y = {y1, y2, . . . , yr} represent the variables to be predicted, where each yi can
be derived from ( tp, a; st), conveying information such as whether a purchase is made at the
purchase stage.
Problem: Given the sequence set S, this study aims to (1) extract k prototypes based
on the distances between sequences, and (2) predict the outcom e variable y using these
distances.
2.2 Proposed Method
2.2.1 Deﬁnition of the Distances Between Sequences
This section deﬁnes the distance between the sequences of S. The Levenshtein distance
(LD), a type of edit distance, is used. The data X i q are not usually interchanged across
stages [9, 19]. The importance of each stage should be considered; for example, the presence
or absence of purchases can result in large diﬀerences. However, conventional LD does not
account for such importance, and thus fails to capture these diﬀe rences appropriately.
To include such a condition, the distance between the two sequence s si and sj is deﬁned
as the weighted sum of the distances at each stage, as follows:
Dl(si, sj) =
m∑
g=1
wg dl (si(stg), sj(stg)) (1)
where wg ≥ 0 is the weight, and dl is the Levenshtein distance. These distances are
computed by considering each pair ( tp, a) in si(stg) as a single symbol.
4

The Levenshtein distance represents the number of operations ( insertions, deletions, sub-
stitutions) required to transform one string into another. It sat isﬁes properties such as the
triangle inequality [2], and the above formulation inherits this propert y.
Proposition. If Dl(si, sj) = ∑m g=1 wg dl(si(stg), sj(stg)), wg ≥ 0, and each dl(si(stg), sj(stg))
satisﬁes the triangle inequality, then Dl(si, sj) also satisﬁes the triangle inequality.
Proof. To simplify notation, let Dl(X, Y ) = ∑m g=1 wg dl(xg, yg), where xg, yg are the gth
components of sequences X, Y . Let
X = (x1, x2), Y = (y1, y2), Z = (z1, z2)
Deﬁne:
Dl(X, Y ) = w1dl(x1, y1) + w2dl(x2, y2) (2)
Dl(X, Z) = w1dl(x1, z1) + w2dl(x2, z2) (3)
Dl(Y, Z) = w1dl(y1, z1) + w2dl(y2, z2) (4)
Assuming that dl satisﬁes the triangle inequality, we have:
dl(x1, z1) ≤ dl(x1, y1) + dl(y1, z1) (5)
dl(x2, z2) ≤ dl(x2, y2) + dl(y2, z2) (6)
Multiplying (6) by w2 ≥ 0:
w2dl(x2, z2) ≤ w2dl(x2, y2) + w2dl(y2, z2) (7)
Adding w1dl(x1, z1) to both sides of (7):
w1dl(x1, z1) + w2dl(x2, z2) ≤ w1dl(x1, z1) + w2dl(x2, y2) + w2dl(y2, z2) (8)
From (5), we have:
w1dl(x1, z1) ≤ w1dl(x1, y1) + w1dl(y1, z1) (9)
Substituting (9) into (8), we get:
w1dl(x1, z1) + w2dl(x2, y2) + w2dl(y2, z2) ≤ w1dl(x1, y1) + w1dl(y1, z1)
+ w2dl(x2, y2) + w2dl(y2, z2)
Hence,
Dl(X, Z) ≤ Dl(X, Y ) + Dl(Y, Z)
This conclusion also holds for the general case, where
Dl(X, Y ) =
m∑
g=1
wg d(xg, yg) ⇐ ⇒ Dl(si, sj) =
m∑
g=1
wg dl
(
si(stg), sj(stg)
)
.
Therefore, Dl(si, sj) satisﬁes the triangle inequality and thus deﬁnes a valid distance
metric over the space of staged sequences. □
5

The costs of replacement, insertion, and deletion operations can b e modiﬁed. However, us-
ing LD with arbitrary weights or normalization may violate the distance axioms. Therefore,
we adopt the above weighted LD formulation, which respects distan ce properties. Notably,
the total computation cost is reduced by calculating distances sep arately for each stage stg.
2.2.2 Prototype Detection and Visualization
This section describes how the proposed weighted Levenshtein dist ance is used to extract
prototypes. K-medoids, a clustering method, is employed for this p urpose [16]. K-medoids
identiﬁes data points, called medoids, that minimize the total dissimilar ity to all other data
in the same cluster. These medoids serve as the prototypes. Since only pairwise distances
between sequences are available, this method enables prototype d etection without requiring
data in vector format, which is commonly assumed in conventional clu stering methods.
Other methods such as K-means are not suitable in this context, as they require the
computation of mean vectors, which is not possible when only pairwise sequence distances
are provided.
Visualization. Let D be a matrix whose entries represent the pairwise distances Dl. Each
sequence is visualized as a point in a two-dimensional space based on t he concept of multi-
dimensional scaling (MDS) [27]. Although other dimensionality reductio n techniques such
as principal component analysis (PCA) exist, MDS is appropriate her e because it requires
only a distance matrix and not feature vectors.
Let I be an identity matrix and 1r an r-dimensional column vector of ones. The procedure
for MDS-based visualization is as follows:
1. Represent the centering matrix:
Dce = −1 2 CD 2C, where C = I − 1 r 1r1′ r (10)
2. Perform eigenvalue decomposition of Dce:
Dce = V ΛV −1 (11)
where Λ =


λ1 0 0
0 λ2 0
0 0 . . .

 contains the eigenvalues and V = [ ⃗ v1, ⃗ v2, . . .] is the matrix
of eigenvectors.
3. Compute the coordinate matrix:
X ∗ = V Λ1/2
assuming only the top two eigenvalues λ1 and λ2 are nonzero.
4. Place each data point using X ∗.
The resulting two-dimensional coordinates represent each seque nce, and the Euclidean
distances between the points approximate the original sequence d istances. This visualization
supports interpretation of the cluster structure and the distrib ution of prototype sequences.
6

2.2.3 Prediction and Counterfactual Explanation
This section explains how prediction was performed using the propos ed Levenshtein distance.
In this study, the k-nearest neighbors ( k-NN) method was employed. This is a nonparamet-
ric regression approach that leverages distance, and its use here is consistent with earlier
sections: since only pairwise distances between sequences and cor responding target values y
are available, conventional regression or machine learning models th at require feature vectors
cannot be applied.
To avoid confusion with k in k-medoids clustering, we use k′ to denote the number of
neighbors in k-NN.
The prediction for a given sequence si is computed as:
ˆy(si) = 1 k′ ∑ sj∈Ni yj (12)
where Ni is the set of k′ nearest sequences to si under the proposed distance measure.
Counterfactual Explanation. Additionally, a new type of counterfactual explanation
is proposed as an interpretability method in machine learning [15, 31]. For example, this
method suggests an alternative customer journey that changes a non-purchase prediction
into a purchase outcome, thereby highlighting factors that inﬂuen ce consumer decisions.
Speciﬁcally, the counterfactual sequence cfs i for a given si is deﬁned as:
cfsi = arg min sj∈S\{si} {loss(yobj, yj) + λ · D′(si, sj)} (13)
where:
• S \ {si} is the set of all sequences excluding si,
• yobj is the desired prediction outcome (e.g., purchase),
• λ is a hyperparameter that balances prediction loss and similarity,
• D′ is a potentially modiﬁed distance between sequences (possibly restr icted to some
stages stg).
A novel aspect of this method is that it does not generate new (syn thetic) sequences;
rather, it selects the most plausible counterfactual sequence fr om the existing data. This
contributes to producing more realistic and actionable explanations , which has not been
widely addressed in prior work.
The core idea is to detect an existing sequence that achieves the de sired target yobj and
is also close to si under the deﬁned distance metric. In practice, the process comp utes
the objective value for all candidate sequences and selects the on e with the smallest score.
The change from the original si to the selected counterfactual is analyzed to identify which
components (e.g., touchpoints or actions) diﬀer. Based on this insig ht, speciﬁc suggestions
can be made to improve customer journeys.
7

3 Experimental
Section 3.1 describes the data used in the analysis, and Section 3.2 dis cusses the results.
3.1 Data
Although automatically collected log data from e-commerce sites can be used to analyze
customer journeys, acquiring such data for general product pu rchases presents practical
challenges. Therefore, we developed and employed a new questionn aire-based method that
allowed the number of recorded actions to vary by individual.
The survey was conducted online and focused on the most recently purchased type of
cosmetics—eye shadows. It was administered to 127 female univers ity students in Japan
over a two-day period from November 30 to December 1, 2022. Par ticipants who indicated
an interest in eye shadow were ﬁrst asked: “How did you come to kno w about eye shadow?”
Subsequent questions such as “Which of the following did you do next ?” were then presented,
with responses recorded up to 10 times per participant.
The questionnaire consisted of 13 predeﬁned combinations of touc hpoints and actions:
a. Knowing the product through TV commercials [awareness]
b. Knowing the product through direct word-of-mouth communica tion [awareness]
c. Understanding the product through word-of-mouth communic ation on social media
[awareness]
d. Knowing the product through other methods [awareness]
e. Comparison and conﬁrmation through various websites by searc hing [information gath-
ering]
f. Comparison and conﬁrmation through e-commerce sites [informa tion gathering]
g. Comparison and conﬁrmation through stores [information gathe ring]
h. Comparison and conﬁrmation through social media [information ga thering]
i. Performing purchases on e-commerce sites [purchase]
j. Performing purchases in stores [purchase]
k. Not performing purchases [non-purchase]
l. Writing product reviews on social media [post-purchase]
m. Other
8

Hereafter, each symbol corresponds to the meanings described below and is also consistent
with the formal representation introduced in Section 2.1. The symb ols a to h represent the
subset of combinations of (tp, a), where tp ∈ {TV, person, social media , e-commerce site , storefront}
and a ∈ {cognition, information gathering } (corresponding to the options described above).
Here, i and j correspond to (tp = ”e-commerce site” , a = ”purchase”) and (tp = ”storefront”, a =
”purchase”), respectively. Finally, purchases in k are represented by “1” and non-purchases
by “0”.
The sequences were classiﬁed into three stages: st1 (pre-purchase: ﬁrst recognition), st2
(pre-purchase: awareness and information gathering), and st3 (purchase stage: purchase
and non-purchase). Post-purchase actions (such as items l and m) were excluded from the
analysis.
Sequences that did not include either a purchase or non-purchase action were omitted,
as were sequences with logically inconsistent stage transitions (e.g., taking a pre-purchase
action after a purchase action). Only valid paths were retained, su ch as: st1 → st1 (multiple
awareness), st1 → st2 (consideration after awareness), st2 → st2 (multiple considerations),
st2 → st1 (awareness after consideration), st1 → st3 (purchase after awareness), and st2 →
st3 (purchase after consideration).
As a result, 104 valid samples were obtained. Of these, 86 resulted in a purchase and 18
in a non-purchase.
To facilitate the recall of recent consumption behavior, responde nts were ﬁrst asked to
describe speciﬁc brand names and shopping contexts. However, t his approach may introduce
recall bias—a limitation that is acknowledged in the design of survey-b ased research.
3.2 Results
Section 3.2.1 presents descriptive statistics, Section 3.2.2 discusse s the results of prototype
detection and visualization, and Section 3.2.3 reports the results of prediction and counter-
factual explanation.
3.2.1 Descriptive Statistics
First, the descriptive statistics for each stage of the obtained da ta are presented.
For the ﬁrst stage, st1, that is, the pre-purchase (ﬁrst recognition) phase, the result s are
shown in Table 1.
Table 1: Descriptive statistics of items in Stage 1
The results show that item c, “Understanding the product through word-of-mouth com-
munication on social media,” appears most frequently, followed by ite m d, “Knowing the
9

product through other methods.” This indicates that recognition t hrough social media is the
most common. Item d is considered to include recognition through oﬄine sources such as
in-store exposure.
For the next stage, st2, the pre-purchase phase (awareness and information gathering ),
the results are shown in Table 2 and Table 3.
Table 2: Descriptive statistics of items in Stage 2
Table 3: Per-sample item count statistics
The results show that item g, “Comparison and conﬁrmation through stores,” was the
most frequent, followed by item e, “Comparison and conﬁrmation through various websites
by searching,” and item h, “Comparison and conﬁrmation through social media.” In this
stage, the number of actions ranged from a minimum of 0 to a maximum of 6, with an
average of 1.32 items. In particular, it was revealed that individuals t ypically performed 1 to
3 actions during this phase. On the other hand, a value of 0 indicates that the purchase was
made immediately after recognition, suggesting behavior similar to imp ulse buying. Taken
together, these results suggest that after recognizing a produ ct, consumers generally tend to
compare or conﬁrm it in physical stores.
For the ﬁnal stage, st3, the number of purchases and non-purchases was 86 and 18,
respectively. This indicates that most respondents chose to make a purchase.
10

Finally, all stages were integrated, and a matrix of item pairs was cre ated with consider-
ation of the sequence order. The result was visualized, as shown in F igure 1. For example,
for a sequence such as a, e, i , the transitions a → e and e → i were each counted. Only item
pairs that satisfy the stage transition constraints described in Se ction 3.1 (e.g., from st1 to
st2, or from st2 to st3) were used.
Figure 1: Sequential Co-occurrence Matrix (Y-axis: From Item, X -axis: To Item)
The results show that in transitions from Stage st1 (a, b, c, d) to the next stage, the
most frequent item pairs were c → e, c → g, c → i, and d → g. This suggests that after
recognizing a product through social media, consumers often pro ceed to consider it through
websites or in physical stores. In transitions from Stage st2 (e, f, g, h) to the next stage,
g → i was by far the most frequent, followed by e → g and h → i. This indicates that many
consumers make a purchase after considering the product in stor es.
However, it should be noted that these results are based solely on p airwise frequency.
To investigate customer journeys involving more than two consecu tive actions, full sequence
analysis is necessary.
3.2.2 Results of Prototype Detection and Visualization
The analysis of the results is presented here. First, the clustering results are described. Four
diﬀerent distance measures were considered: the standard Leve nshtein distance (LD), the
Damerau-Levenshtein distance, and two weighted versions with we ights w1 = 2, w2 = 1, w3 =
1 and w1 = 2 , w2 = 1 , w3 = 10, respectively. Clustering was evaluated using the Silhouette
Coeﬃcient (SC) for cluster sizes k ∈ {2, 3, 4, 5, 6, 7, 8} [26]. Initial values were set using the
11

k-medoids++ algorithm, and random seeds were ﬁxed to ensure rep roducibility. Higher SC
values indicate better clustering performance. In general, SC can be high for smaller k, but
higher values may be preferred depending on the application.
Table 4: Clustering results (Silhouette Coeﬃcient for diﬀerent sett ings)
Table 4 shows that SC values increased when higher weights were ass igned to w3. This
reﬂects the greater inﬂuence of diﬀerences in the purchase stag e st3 under such settings. The
typical sequences extracted under the setting w1 = 2, w2 = 1, w3 = 10 with k = 6 are shown
below:
1: [c, e, g, 1]
2: [c, e, g, 0]
3: [c, g, 1]
4: [d, c, 1]
5: [c, b, e, g, 1]
6: [d, 1]
The cluster sizes were as follows: Cluster 1: 14, Cluster 2: 18, Clust er 3: 35, Cluster 4:
9, Cluster 5: 7, and Cluster 6: 20. The most common pattern was Pa ttern 3, which repre-
sented customers who recognized a product through social media , checked it in stores, and
then purchased it. The next most common was Pattern 6, which rep resented customers who
purchased a product after recognizing it through other means—p ossibly even prior familiar-
ity. Pattern 2 and Pattern 5 represent customers who performe d online searches, conﬁrmed
products in stores, and either made a purchase or did not, depend ing on the situation.
Next, the visualization results are presented in Figure 2. Although t he positions are
relative, patterns like 1 and 5 appeared in the lower right, suggestin g more careful judgment.
Conversely, patterns like 3 and 6 occupied more central or upper p ositions, indicating more
direct decision-making. The non-purchase group also tended to clu ster in areas suggesting
more deliberative behavior.
3.2.3 Results of Prediction and Counterfactual Explanatio n
Then, the k-NN algorithm was used to predict y. Speciﬁcally, in this study, S(st1) and S(st2)
were used as explanatory variables, and the purchase (“1”) or no n-purchase (“0”) decision
in S(st3) was used as the target variable y. Regarding the data, 80% and 20% were used as
training and test data, respectively. The prediction was performe d using k′ ∈ { 1, 2, 3, 4, 5},
12

Figure 2: Visualization of the sequence clusters in 2D space
Table 5: Comparison of accuracy and F1-measure values
13

and each setting was repeated 100 times to evaluate the mean and v ariance of both accuracy
and F1-measure. These results are shown in Table 5.
Comparing the values of each model, the accuracy for k′ = 5 was approximately 0.81,
indicating that it would be possible to predict whether a product will be purchased based
on the sequence.
The results of the counterfactual explanation for the k-NN model using sequential data
are presented below. Speciﬁcally, four cases are shown in which the original sequence had a
label of y = 0 (non-purchase), and an alternative sequence improved the pr ediction to ˆy = 1
(purchase).
(Base sequence and counterfactual sequence: 1)
Base sequence: ["c", "c", "e", "g"] : y = 0
Counterfactual sequence: ["c", "b", "e", "g"] : ˆ y = 1
The improved sequence was derived by replacing c: “Knowing about the product through
word-of-mouth communication on social media” with b: “Knowing about the product through
direct word-of-mouth communication,” indicating that the respond ent might purchase the
product. This suggested the importance of direct word-of-mout h communication over com-
munication on social media with respect to purchasing decisions.
(Base sequence and counterfactual sequence: 2)
Base sequence: ["d", "e", "f"] : y = 0
Counterfactual sequence: ["c", "e", "f"] : ˆ y = 1
The improved sequence was derived by replacing d: “Knowing the product through other
methods” with c: “Knowing the product through word-of-mouth communication on social
media,” indicating that the respondent might purchase the product . This suggested the
importance of social media communication over more ambiguous or les s direct information
sources.
(Base sequence and counterfactual sequence: 3)
Base sequence: ["d", "g", "h"] : y = 0
Counterfactual sequence: ["d", "g", "e"] : ˆ y = 1
The improved sequence was derived by replacing h: “Comparison and conﬁrmation through
social media” with e: “Comparison and conﬁrmation through various websites by searc hing,”
indicating that the respondent might purchase the product. This s uggested that broader
web-based comparison may be more eﬀective than relying solely on so cial media content.
(Base sequence and counterfactual sequence: 4)
Base sequence: ["b"]: y = 0
Counterfactual sequence: ["c"]: ˆ y = 1
The improved sequence was derived by replacing b: “Knowing the product through direct
word-of-mouth communication” with c: “Understanding the product through word-of-mouth
communication on social media,” indicating that the respondent might purchase the product.
This suggested that communication on social media might have a broa der or more persuasive
inﬂuence compared to direct word-of-mouth interactions.
This analysis demonstrated that even minor changes in the sequenc e of information acqui-
sition and evaluation can inﬂuence purchase intentions. The following key ﬁndings emerged:
14

1. The mode of word-of-mouth communication (direct vs. social me dia-based) signiﬁ-
cantly impacts purchasing decisions, with eﬀectiveness varying by c ontext.
2. Social media-based information tends to be more persuasive tha n impersonal or un-
speciﬁed sources.
3. During the comparison and conﬁrmation stage, web searches oﬀ ering diverse informa-
tion may be more eﬀective than social media-based content.
These ﬁndings suggest that strategically designing information cha nnels is essential for
encouraging consumer purchases. Moreover, these results clea rly showed that it was possible
to propose ways to change a particular preselected sequence suc h that it would lead to
a purchase. Furthermore, they indicated the factors that were important for performing
purchases in each sequence.
4 Discussion
This study was conducted to formally and quantitatively analyze cus tomer journeys. The
diﬀerences between previous studies and the proposed study are discussed below.
Unlike studies that use mixed Markov models, our study speciﬁcally de tects typical
cases [12]. Then, there are several studies that have applied k-medoids to edit distances
such as LD [5]. Our study diﬀers from those in that it deﬁnes a new dist ance for more
general customer journey data with categories such as stages. Since this distance satisﬁes
the axiom of distance, it can easily be extended to other methods.
In addition, this study proposed a visualization method using MDS bas ed on the pro-
posed distance. Unlike previous research, the distance used here is not a simple Levenshtein
distance but is designed for marketing-speciﬁc applications. This ap proach not only enables
the extraction of prototypes, but also allows for identifying their r elative positioning, which
facilitates interpretation as prototypes and evaluation of their va lidity.
Furthermore, our study proposes not only clustering but also a me thod to predict and
derive counterfactual hypothetical cases. This approach also c ontributes to the research ﬁeld
of interpretable counterfactual explanations—or algorithmic rec ourse—from the following
perspectives.
First, (i) plausibility: Each suggested sequence corresponds to an actual customer jour-
ney observed in the dataset. Counterfactual recommendations are generated based on se-
quences that were empirically observed.
Second, the method improves (ii) managerial interpretability : Since each edit opera-
tion can be directly associated with a speciﬁc marketing intervention (e.g., replacing the ﬁrst
touchpoint from “direct word-of-mouth” to “social media-based word-of-mouth”). Recent
studies have shown that the usefulness of counterfactual expla nations heavily depends on
such validity.
Finally, it introduces (iii) a novel approach for sequential data : While robustness in
structured data has been extensively studied, for sequential da ta, only recently have methods
begun to address symbolic constraints on allowable edits. This study oﬀers one such method.
15

However, establishing robustness guarantees for the proposed approach remains an im-
portant topic for future work.
Moreover, we propose a new survey method and a method for clean sing data rather than
just providing a formal deﬁnition of data. These two are novelties a nd contributions in this
study.
Regarding the shortcomings of the proposed study, they are pre sented below.
1. First, a customer journey not only includes diﬀerent stages but also the actual behaviors
(search, purchase, and non-purchase) and psychological stat es of consumers (such as
perceived needs) and more speciﬁc information at touchpoints [4, 33]. Therefore, it is
necessary to incorporate and extend this information. Since thes e pieces of information
may have complex structures, distances between sequences can be obtained by using
approaches like tree structures and graphs.
2. Another issue is estimating the level of awareness of consumers regarding their behavior
and changes in their awareness.
3. Finally, regarding problems such as recall bias in data collection, a m ethod that enables
automatic data collection should be considered.
5 Conclusions
The overall contributions of the study are listed below.
1. A method to formally deﬁne data sequences and the distances be tween them using
Levenshtein distance (LD) was proposed.
2. Typical cases were extracted using k-medoids. Furthermore, a method for visualizing
these data was presented.
3. Both a method for predicting purchases using k-NN with the proposed distance and
a method for extracting counterfactual explanations to interpr et the prediction results
were proposed.
4. A new survey method to obtain the data used in the study was pro posed.
The survey-based data analysis revealed typical interpretable pa tterns. Furthermore,
through visualization, the positioning of the data could be understo od, predictions could
be made regarding whether purchases would be performed, and co unterfactual hypothetical
cases and important elements could be detected.
The analysis and research methods used in this study will be useful f or understanding
the future behavior of consumers and designing consumer experie nces [17].
Acknowledgments
I would like to thank Yui Nakazawa (Faculty of Business, Kyoritsu Wo men’s University) for
her help in designing and collecting the data used in the study. This stu dy was supported
by a JSPS Grant-in-Aid for Scientiﬁc Research (25K05381).
16

References
[1] E. Anderl, I. Becker, F. von Wangenheim, and J. H. Schumann. M apping the customer
journey: Lessons learned from graph-based online attribution mo deling. International
Journal of Research in Marketing , 33(3):457–474, 2016.
[2] G. V. Bard. Spelling-error tolerant, order-independent pass- phrases via the damerau-
levenshtein string-edit distance metric. In Proceedings of the Fifth Australasian Sym-
posium on ACSW Frontiers , volume 68, pages 117–124. Australian Computer Society,
2007.
[3] N. Barwitz and P. Maas. Understanding the omnichannel custom er journey: determi-
nants of interaction choice. Journal of Interactive Marketing , 43(1):116–133, 2018.
[4] G. Bernard and P. Andritsos. A process mining based model for c ustomer journey
mapping. In Proceedings of the Forum and Doctoral Consortium Papers Presented at the
29th International Conference on Advanced Information Sys tems Engineering (CAiSE
2017), volume 1848, pages 49–56, 2017.
[5] G. Bernard and P. Andritsos. Contextual and behavioral cust omer journey discovery
using a genetic approach. In Advances in Databases and Information Systems: 23rd Eu-
ropean Conference, ADBIS 2019 , volume 11695 of Lecture Notes in Computer Science ,
pages 251–266. Springer, 2019.
[6] G. Bernard and P. Andritsos. Discovering customer journeys f rom evidence: A genetic
approach inspired by process mining. In Information Systems Engineering in Responsi-
ble Information Systems: CAiSE Forum 2019 , volume 350 of Lecture Notes in Business
Information Processing, pages 36–47. Springer, 2019.
[7] K. Bobroske, C. Larish, A. Cattrell, M. V. Bjarnad´ ottir, and L . Huan. The bird’s-
eye view: a data-driven approach to understanding patient journ eys from claims data.
Journal of the American Medical Informatics Association , 27(7):1037–1045, 2020.
[8] C. Bradley, L. Oliveira, S. Birrell, and R. Cain. A new perspective on personas and cus-
tomer journey maps: Proposing systemic ux. International Journal of Human-Computer
Studies, 148:102583, 2021.
[9] F. J. Damerau. A technique for computer detection and correc tion of spelling errors.
Communications of the ACM , 7(3):171–176, 1964.
[10] R. Dwivedi, D. Dave, H. Naik, S. Singhal, R. Omer, P. Patel, B. Qian , Z. Wen, T. Shah,
G. Morgan, and R. Ranjan. Explainable ai (xai): Core ideas, techniq ues, and solutions.
ACM Computing Surveys , 55(9):1–33, 2023.
[11] A. Følstad and K. Kvale. Customer journeys: A systematic liter ature review. Journal
of Service Theory and Practice , 28(2):196–227, 2018.
17

[12] M. Harbich, G. Bernard, P. Berkes, B. Garbinato, and P. Andr itsos. Discovering cus-
tomer journey maps using a mixture of markov models. In Proceedings of the Inter-
national Symposium on Data-Driven Process Discovery and An alysis (SIMPDA 2017) ,
pages 3–7, 2017.
[13] D. Herhausen, K. Kleinlercher, P. C. Verhoef, O. Emrich, and T . Rudolph. Loyalty
formation for diﬀerent customer journey segments. Journal of Retailing , 95(3):9–29,
2019.
[14] P. Hosseinzadeh, P. Li, O. Bahri, S. F. Boubrahimi, and S. M. Ham di. Acts: Adap-
tive counterfactual explanations for time series data using baryc enters. In 2024 IEEE
International Conference on Big Data (BigData) , pages 1327–1332. IEEE, 2024.
[15] A. H. Karimi, G. Barthe, B. Sch¨ olkopf, and I. Valera. A survey of algorithmic recourse:
Contrastive explanations and consequential recommendations. ACM Computing Sur-
veys, 55(5):1–29, 2022.
[16] L. Kaufman and P. J. Rousseeuw. Partitioning around medoids ( program pam). In
Finding Groups in Data: An Introduction to Cluster Analysis , pages 68–125. Wiley,
1990.
[17] C. Kuehnl, D. Jozic, and C. Homburg. Eﬀective customer journ ey design: Consumers’
conception, measurement, and consequences. Journal of the Academy of Marketing
Science, 47:551–568, 2019.
[18] K. N. Lemon and P. C. Verhoef. Understanding customer expe rience throughout the
customer journey. Journal of Marketing , 80(6):69–96, 2016.
[19] V. I. Levenshtein. Binary codes capable of correcting deletion s, insertions, and reversals.
Soviet Physics Doklady , 10(8):707–710, 1966.
[20] S. M. Lundberg and S.-I. Lee. A uniﬁed approach to interpretin g model predictions.
In Advances in Neural Information Processing Systems , volume 30, pages 4765–4774,
2017.
[21] C. Molnar. Interpretable Machine Learning . Lulu.com, 2020.
[22] S. A. Neslin. The omnichannel continuum: Integrating online and oﬄine channels along
the customer journey. Journal of Retailing , 98(1):111–132, 2022.
[23] M. Palaz´ on, M. L´ opez, M. Sicilia, and I. L´ opez. The customer journey: A proposal
of indicators to evaluate integration and customer orientation. Journal of Marketing
Communications, 28(5):528–559, 2022.
[24] M. T. Ribeiro, S. Singh, and C. Guestrin. ”why should i trust you ?”: Explaining the
predictions of any classiﬁer. In Proceedings of the 22nd ACM SIGKDD International
Conference on Knowledge Discovery and Data Mining , pages 1135–1144, 2016.
18

[25] M. S. Rosenbaum, M. L. Otalora, and G. C. Ram ´ ırez. How to cre ate a realistic customer
journey map. Business Horizons , 60(1):143–150, 2017.
[26] P. J. Rousseeuw. Silhouettes: A graphical aid to the interpret ation and validation of
cluster analysis. Journal of Computational and Applied Mathematics , 20:53–65, 1987.
[27] N. Saeed, H. Nam, M. I. U. Haq, and D. B. Muhammad Saqib. A sur vey on multidi-
mensional scaling. ACM Computing Surveys , 51(3):1–25, 2018.
[28] M. Shvo, A. C. Li, R. T. Icarte, and S. A. McIlraith. Interpret able sequence classiﬁ-
cation via discrete optimization. In Proceedings of the AAAI Conference on Artiﬁcial
Intelligence, volume 35, pages 9647–9656, 2021.
[29] B. Topaloglu, B. Oztaysi, and O. Dogan. Cart-state-aware dis covery of e-commerce
visitor journeys with process mining. Journal of Theoretical and Applied Electronic
Commerce Research, 19(4):2851–2879, 2024.
[30] Y. Tueanrat, S. Papagiannidis, and E. Alamanos. Going on a jour ney: A review of the
customer journey literature. Journal of Business Research , 125:336–353, 2021.
[31] S. Verma, V. Boonsanong, M. Hoang, K. Hines, J. Dickerson, a nd C. Shah. Counter-
factual explanations and algorithmic recourses for machine learnin g: A review. ACM
Computing Surveys , 56(12):1–42, 2024.
[32] M. Zhang, B. Kao, C. L. Yip, and D. Cheung. A gsp-based eﬃcien t algorithm for mining
frequent sequences. In Proceedings of the 2001 International Conference on Artiﬁc ial
Intelligence, pages 497–503. CSREA Press, 2001.
[33] S. Zhao, W.-L. Hsu, G. Ma, T. Xu, G. Jacobson, and R. Rustamo v. Characterizing and
learning representation on customer contact journeys in cellular s ervices. In Proceedings
of the 26th ACM SIGKDD International Conference on Knowledg e Discovery & Data
Mining, pages 3252–3260. ACM, 2020.
19
