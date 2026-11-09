---
title: A Weighted Similarity Metric for Community Detection in Sparse Data
url: https://arxiv.org/abs/2501.07025
category: social-media
subcategory: empirical
date: 2025-01
venue: AAAI 2025
authors:
- Yong Zhang
- Eric Herrison Gyamfi
source: arxiv
pdf_url: https://arxiv.org/pdf/2501.07025
pages: 22
chars: 52098
fetched_at: '2026-11-08T13:11:30+00:00'
kb_version: 1
---

# A Weighted Similarity Metric for Community Detection in Sparse Data

A Weighted Similarity Metric for Community Detection in Sparse Data
Yong Zhang1, Eric Herrison Gyamfi2
1 Corporate Functions R&D, Discovery& Innovation Platforms, P&G *
2 Department of Mathematical Sciences, Division of Statistics and Data Science, University of Cincinnati
zhang.y.13@pg.com, gyamfien@mail.uc.edu
Abstract
Many Natural Language Processing (NLP) related applica-
tions involves topics and sentiments derived from short doc-
uments such as consumer reviews and social media posts.
Topics and sentiments of short documents are highly sparse
because a short document generally covers a few topics
among hundreds of candidates. Imputation of missing data
is sometimes hard to justify and also often unpractical in
highly sparse data. We developed a method for calculating a
weighted similarity for highly sparse data without imputation.
This weighted similarity is consist of three components to
capture similarities based on both existence and lack of com-
mon properties and pattern of missing values. As a case study,
we used a community detection algorithm and this weighted
similarity to group different shampoo brands based on sparse
topic sentiments derived from short consumer reviews. Com-
pared with traditional imputation and similarity measures, the
weighted similarity shows better performance in both general
community structures and average community qualities. The
performance is consistent and robust across metrics and com-
munity complexities.
Code & Dataset — https://github.com/zhy5186612/
Weighted Similarity Without Imputation
1 Introduction
NLP and Large Language Model (LLM) have been increas-
ingly used by Consumer Packaged Goods and other indus-
tries to extract insights from large amount of textual data.
These textual data includes consumer reviews and com-
plaints, open ended comments and verbatims in a survey and
social media posts. While NLP and LLM can easily conduct
summaries and extract topics and sentiments from these tex-
tual data, advanced analytics on topics and sentiments are
generally needed to gain insights to enable better and faster
consumer understanding and product innovation. The chal-
lenge of using advanced analytics and models arises when
there are many missing data. The challenge is particularly
prominent when using topic and sentiment data derived from
short documents such as consumer reviews and social media
*This paper has been accepted for Workshop of AI for Social
Impact at AAAI 2025.
Copyright © 2025, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
posts. As an example, a review may only contain few topics
out of hundreds or even thousands topics.
Imputation is a natural solution for missing data. Main-
stream imputation methods include replacing with mean,
k-nearest neighbors (KNN) and Multivariate Imputation
by Chained Equations (MICE). Different imputation tech-
niques can significantly impact the effectiveness and qual-
ities of downstream analytics. Sometimes imputation of
missing data is hard to justify without knowing the miss-
ing mechanism. Furthermore, it is also unpractical to impute
missing values if a dataset is highly sparse (e.g., 90% values
are missing).
Similarity is an important metric for many advanced an-
alytics and models. Community detection and/or clustering
are good examples. Community detection in complex net-
works aims at identifying groups of nodes that are more
densely connected internally than with the rest of the net-
work (Brzozowski, Siudem, and Gagolewski 2023; Fortu-
nato 2010a). Community detection and/or clustering rely
heavily on similarities between data points. Both missing
data and its imputation method can significantly affect the
similarity quality and its related downstream analytics. A
new similarity metric without imputation is needed and es-
sential for meaningful downstream NLP applications involv-
ing sparse topics and sentiments from short documents.
This paper is organized as follows. In next section, we
provide a review of the traditional imputation techniques
and similarity metrics utilized in this paper. We then for-
mulate the theoretical framework of the weighted similar-
ity. We proceed to describe a case study using the weighted
similarity and imputed similarities based on an anonymized
dataset. We conclude the paper after presenting results and
discussion.
2 Imputation and Similarity Methods
Imputation is generally used to fill in missing values under
the assumption of missing at random. Here we employed
several different imputation methods for calculating differ-
ent similarity metrics in the context of community detection.
We compared the qualities of detected communities through
different imputation and similarity measures to assess the
merits of the new weighted similarity without imputation.
arXiv:2501.07025v2  [stat.ME]  7 Feb 2025

Imputation Methods
Mean imputation is one of the simplest methods to handle
missing data. It replaces missing values with the mean of the
available values for that feature. This method is straightfor-
ward and computationally efficient (Little and Rubin 2002).
However, it can distort the variance and covariance struc-
tures of the data, leading to potential biases in subsequent
analyses. The K-Nearest Neighbor imputation is a more so-
phisticated method that replaces missing values with the av-
erage of the K nearest neighbors’ values. This approach
considers the local structure of the data, providing a more
context-aware imputation (Troyanskaya et al. 2001). MICE
is an advanced imputation technique that uses multiple itera-
tions and models to predict missing values (van Buuren and
Groothuis-Oudshoorn 2011).
Similarity Measures
Accurately measuring similarity between data points is cru-
cial for tasks such as clustering and community detection.
Traditional similarity measures offer different perspectives
on how to quantify similarity, each with its strengths and ap-
plications. This paper considers imputed Cosine similarity,
Euclidean distance, Canberra distance and Spearman corre-
lation coefficient as benchmarks for the weighted similarity
without imputation.
Cosine similarity measures the cosine of the angle be-
tween two vectors, focusing on the orientation rather than
magnitude. This measure is particularly effective for high-
dimensional data where the magnitude of vectors can vary
significantly (Tan, Steinbach, and Kumar 2005). However,
it does not handle missing values directly and is sensitive
to the sparsity of the vectors, which can affect its accuracy
in some cases. The Euclidean distance is one of the most
intuitive measures of similarity, representing the straight-
line distance between two points in multidimensional space
(Sneath and Sokal 1973). Euclidean distance is sensitive to
the scale of the data, requiring complete data and normaliza-
tion for meaningful comparisons.
Canberra distance is a weighted version of the Manhat-
tan distance, giving higher weight to differences where val-
ues are small. This characteristic makes it particularly sensi-
tive to small changes in values, which can be beneficial for
datasets with a wide range of scales (Lance and Williams
1967). Canberra distance is sensitive to zero values and re-
quires complete data, which can limit its applicability in
datasets with missing values. Spearman correlation mea-
sures the rank correlation between two variables, assessing
how well the relationship between two variables can be de-
scribed using a monotonic function (Spearman 1904). It also
requires complete data and does not capture linear relation-
ships as effectively as Pearson correlation.
The appendices A has detailed descriptions on imputation
methods and similarity metrics.
3 Formulation of the Weighted Similarity
Figure 1 shows a toy example of calculating the weighted
similarity between two sparse vectors V1 and V2. First, two
vectors of equal length are decomposed into three parts. Part
1 represents sub-vectors where bothV1 and V2 have numer-
ical values. This corresponds to Vn1 and Vn2 in equation
1. sNum is the similarity of Part 1. Part 2 represents sub-
vectors where both V1 and V2 have missing values. sNan
is the similarity of Part 2. Part 3 captures positions where
either V1 or V2 has a numerical value and the other has a
missing value. sNon is the similarity of Part 3.
Figure 1: How to calculate weighted similarity
As an example, V1 and V2 can represent vectors of senti-
ments of different topics of shampoo brands 1 and 2, respec-
tively. These topic sentiments can be output of any Natural
Language Processing (NLP) model on consumer reviews.
Since these reviews are generally short and only covers few
topics out of hundreds candidates, the derived vectors of sen-
timents for each brand are highly sparse data. Assume both
brands 1 and 2 provide shampooing and conditioning bene-
fits; and they have apple and mint fragrances, respectively;
neither brands offer anti-dandruff and softness benefits. In
this case, sNum captures similarity on sentiments of sham-
pooing and conditioning benefits. sNan captures dissimilar-
ity between sentiments of two categorically different fra-
grances. sNon conveys the idea that brands 1 and 2 are also
similar as they both lack anti-dandruff and softness benefits.
Similarity sNum
Similarity sNum is calculated through equation 1 based on
properties shared by both V1 and V2. Cosine similarity is
used as an example in the equation, other similarity metrics
can also be used. It uses non-missing and aligned numeri-
cal values of two vectors, scaled by the proportion of these
values. This approach mitigates the issue of data sparsity by
focusing on the available values and provides a measure that
captures the similarity in terms of direction and proportion
of available data.
Similarity sNum is given by:
sNum =



0 if |Vn1| = 0
sign(Vn1Vn2) min(∥Vn1∥,∥Vn2∥)
|V1| max(∥Vn1∥,∥Vn2∥) if |Vn1| = 1
|Vn1|
|V1| · Vn1·Vn2 ∥Vn1∥∥Vn2∥ if |Vn1| > 1
(1)
where |V1| is the length ofV1; and ∥Vn1∥ is the Euclidean
norm of Vn1.

Equation 1 also handles two corner cases. When there is
no shared position having numerical values in two vectors,
the sNum is set as 0. When there is only a single shared
position having values in two vectors, thesNum depends on
both magnitudes and signs of the two scalars.
Similarity sNan
Similarity sNan is calulated using equation 2 based on prop-
erties lacked in both V1 and V2. It uses the proportion of
missing values in both vectors. This term captures the pat-
tern of missing data. It can be informative in many real-
world datasets where the lack of properties itself carries sig-
nificant information.
Similarity sNan is given by:
sNan = cN an |V1| (2)
where cN anis the count of position having missing value
in both vectors.
Similarity sNon
Similarity sNon is calculated using equation 3. This simi-
larity component measures the proportion of non-matching
missing values in two vectors. It penalizes similarity based
on non-matching missing values. This component is vital for
datasets with significant amounts of missing data, as it pe-
nalizes positions that differ in their missing data patterns.
Similarity sNon is given by:
sNon = − cN on |V1| (3)
where cN onis the count of positions having non-matching
missing entries in both vectors.
Weighted Similarity
The weighted similarity combines similarities sNum, sNan
and sNon into a single measure in equation 4. This compos-
ite metric provides a comprehensive view of similarity, in-
corporating both the available numerical data and the miss-
ing patterns. It ensures that vectors are compared holisti-
cally, considering all aspects of their data.
similarity = sNum + sNan + sNon (4)
If the similarity metric used for the numerical Part 1 is
bounded by -1 and 1, the weighted similarity in equation
4 also has a range of [-1, 1]. In the appendix, we use cosine
similarity metric as an example to prove that the range of the
weighted similarity metric S, is S ∈ [−1, 1]. This suggests
that the formulation in equation 4 is indeed a proper metric
to measure similarity in sparse data without imputation.
4 Case Study
A case study was conducted to compare the performance
of the weighted similarity against traditional similarity mea-
sures and imputation methods in the context of commu-
nity detection using the Girvan-Newman algorithm (Girvan
and Newman 2002). We used an anonymized datasets with
78 rows and 44 columns. Each row is a shampoo brand
and each column is a topic in the shampoo product cate-
gory. The value is the sentiment on the corresponding topic
and brand. The topics and sentiments were output from
BERTopic model based on consumer reviews. Since most
reviews are short and only cover few topics, around 70% of
topic sentiments are missing. This data is also provided in
this paper’s GitHub repository.
First, pairwise brand similarities were calculated using the
weighted similarity without imputation and imputed simi-
larities. We investigated traditional Cosine, Euclidean, Can-
berra and Spearman similarities with mean, KNN (K=4),
and MICE imputations. For each similarity method, a graph
was built to represent similarities among the brands. Each
node in the graph is a brand. Each edge is the similarity be-
tween the two connected brands. For each graph, we retained
top 100, 600 and 1200 strong edges (i.e., large similari-
ties) to represent different graph complexities. The Girvan-
Newman algorithm was then used to detect 5 communi-
ties (i.e., clusters) from a graph to group different shampoo
brands together.
The performance of each similarity method is evaluated in
two folds: general community structures and average com-
munity qualities. When evaluating detected communities, it
is crucial to consider various metrics that can capture dif-
ferent aspects of community structures. Metrics of general
community structures help to assess the overall quality and
coherence of the detected communities within a network.
These metrics focus on the internal consistency and external
separation of communities, providing insights into how well
the algorithm can identify and preserve meaningful groups
of nodes. Modularity (Q) (Newman 2006), Coverage (Fortu-
nato 2010b), Dunn Index (Dunn 1974), Average Clustering
Coefficient (Watts and Strogatz 1998), Transitivity (New-
man 2003), Modularity Density (Li et al. 2008) and Triangle
Participation Ratio (TPR) (Jaewon and Jure 2012) were used
to assess general community structures.
Average community quality metrics offer a more detailed
assessment of the quality and cohesiveness of each indi-
vidual community. These metrics focus on specific proper-
ties of the communities, such as their internal connectivity,
isolation from the rest of the network, and overall density.
Conductance (Kannan, Vempala, and Vetta 2004), Expan-
sion (Leskovec et al. 2008), Normalized Cut (Shi and Ma-
lik 2000), Density (Radicchi et al. 2004), Internal Density
(Fortunato 2010b) and Local Modularity (Clauset, Newman,
and Moore 2004) were utilized to assess average community
qualities. The appendices have detailed descriptions on these
metrics and Girvan-Newman algorithm.
5 Results
Community Network Graph
As an example, figure 2 shows the network graph and com-
munity structures based on the weighted similarity and im-
puted cosine similarity using KNN. For the network graph
with 100 edges and 5 communities, the brand clusters/-
communities from the weighted similarity and imputed co-
sine similarity are similar regardless the imputation methods

(Figures 2 and A1). This similar structure is likely due to the
fact that cosine similarity is one component in the weighed
similarity (equation 1). It could be also due to the inherent
properties of cosine similarity, which focuses on the orien-
tation of the vectors, making it less sensitive to the specific
imputation techniques.
For the rest of the imputed similarity metrics, the com-
munity structures differ substantially (Figures A2, A3, A4).
These differences can be attributed to the varying ways each
method handles missing data and measures similarity, lead-
ing to different interpretations of the network’s structure. As
the number of edges increased from 100 to 600 and then to
1200 (figures A5 and A9), the weighted similarity has a rel-
ative better clustering with well-separated clusters, compact
intra-cluster distances, higher tendency for nodes to cluster
together. These brand structures at different connectivity are
consistent with the knowledge from domain experts.
General Community Structures
Figure 3 shows metrics measuring qualities of general com-
munity structures derived from the weighted similarity and
imputed similarities. The weighted similarity and imputed
cosine similarity have comparable qualities on general com-
munity structures. They both outperforms imputed similari-
ties based on Euclidean and Canberra distances and Spear-
man correlation. These are consistent with the structures of
community network graphs.
The weighted similarity has a higher modularity (Q)
value. This means the corresponding community structures
has a denser connection within communities and sparser
connections between communities. This suggests that the
weighted similarity method can identify more cohesive com-
munity structures. All similarity measures have relatively
high value of coverage. This indicates Girvan-Newman al-
gorithm effectively captures the overall structure of their
community networks by ensuring that most edges are within
communities.
While Dunn index is small for all similarity metrics, it
is relatively higher for the weighted similarity. The higher
Dunn index suggests that the weighted similarity has a rel-
ative better clustering. The higher average clustering coef-
ficient indicates that the weighted similarity tends to create
tight and neat brand clusters.
The weighted similarity also has higher values of tran-
sitivity, modularity density and triangle participation ratio.
These suggests higher density within formed communities
and its nodes (i.e., brands) tend to form triangles more fre-
quently. These all indicates a stronger and more cohesive
community structure.
Average Community Qualities
Figure 4 presents the average of density, internal density
and local modularity across individual communities derived
from the weighted similarity and imputed similarities. The
weighted similarity outperforms all imputed similarities on
these three metrics measuring average community qualities.
Higher density indicates better internal connectivity within
communities. It suggests that the community is more cohe-
sive and well-connected.
The weighted similarity also has higher values for both
internal density and local modularity. It means nodes/brands
within each community are more tightly connected. This
again suggests a better connectivity within each community
in the well-defined and cohesive communities.
Figure 5 displays the average of conductance, expansion
and normalized cut across individual communities derived
from different similarity measures. A smaller value indicates
a better average community quality. Weighted similarity and
imputed cosine similarity have lower and comparable val-
ues in general. These lower conductance, expansion and nor-
malized cuts indicate that fewer edges leave the community
and that the community is more self-contained with fewer
connections to the rest of the network. This implies a better
community isolation and minimal connections between the
communities, and the rest of the network.
As the number of edges of the community network graph
increase from 100 to 600 (figure 5), the weighted similar-
ity starts to outperform all imputed similarities on most met-
rics for both general community structures and average com-
munity qualities (figures A6, A7, A8). This trend becomes
even more pronounced as the edges increase to 1200 (fig-
ure A9). At this level of complexity of community network
graph, the weighted similarity significantly outperforms all
imputed similarities across almost all metrics (figures A10,
A11, A12). The consistent high performance of the weighted
similarity highlights its ability to maintain high quality com-
munity detection across varying network complexities.
6 Discussion
Performance and Robustness
Performance of imputed cosine similarity is comparable
with that of the weighted similarity at lower network com-
plexity (i.e., 100 edges). The performance of imputed cosine
similarity starts to deteriorate at medium network complex-
ity (i.e., 600 edges. figures A6, A7, A8) and underperform
dramatically at high network complexity (i.e., 1200 edges.
figures A10, A11, A12). This makes senses as high complex-
ity network uses more edges and hence more imputed sim-
ilarity values. More imputations highly likely causes more
deviation from the pattern in real data. The weighted sim-
ilarity does not rely on imputation and therefore preserves
integrity of data.
The results of the case study demonstrate the robustness
and effectiveness of the weighted similarity, particularly in
datasets with significant amounts of missing data and dense
community structures. The better performance is rooted in
the fact that the weighted similarity can directly handle miss-
ing data and incorporate it into the similarity calculation.
This holistic similarity measurement considers both avail-
able data and the patterns of missing data. It helps pre-
serve data integrity and enable downstream application like
community detection algorithm to create more cohesive and
well-defined communities. Missing data themselves can be
informative in many real-world datasets if the missing pat-
tern carries significant information.
The better performance observed as the number of edges
increased from 100 to 600 and then to 1200 underscores the

(a) Weighted similarity
 (b) Cosine similarity based on KNN imputation
Figure 2: Community structures with 5 clusters and 100 connected edges based on the weighted similarity and imputed cosine
similarities using KNN.
MQ C DI ACC T MD TPR0.0
0.2
0.4
0.6
0.8
1.0Metric Value
Weighted Similarity Mean Cosine MICE Cosine KNN Cosine
(a) Imputed cosine similarity vs weighted similarity
MQ C DI ACC T MD TPR0.0
0.2
0.4
0.6
0.8
1.0Metric Value
Weighted Similarity Mean Euclidean MICE Euclidean KNN Euclidean (b) Imputed euclidean similarity vs weighted similarity
MQ C DI ACC T MD TPR0.0
0.2
0.4
0.6
0.8
1.0Metric Value
Weighted Similarity Mean Canberra MICE Canberra KNN Canberra
(c) Imputed canberra similarity vs weighted similarity
MQ C DI ACC T MD TPR0.0
0.2
0.4
0.6
0.8
1.0Metric Value
Weighted Similarity Mean Spearman MICE Spearman KNN Spearman (d) Imputed spearman similarity vs weighted similarity
Figure 3: Performance metrics on general community structures with 100 connected edges and 5 clusters. MQ: Modularity Q,
C: Coverage, DI: Dunn Index, ACC: Average Clustering Coefficient, T: Transitivity, MD: Modularity Density, TPR: Triangle
Participation Ratio. Higher bar indicates better community structure.
robustness of the weighted similarity. While other methods
showed varying degrees of performance degradation or in-
consistency with increasing edge size, the weighted simi-
larity method consistently maintained performance. This ro-
bustness can be attributed to its comprehensive approach in
handling both available data and patterns of missing data,
ensuring accurate and reliable similarity measurements re-
gardless of network complexity.
Impact of Imputation
Imputation methods such as mean, KNN, and MICE have
their weaknesses. Mean imputation can distort the variance
and covariance structures of the data, leading to potential
biases. KNN imputation, while more sophisticated, is com-
putationally intensive and may not perform well when the
nearest neighbors are not representative of the missing val-
ues. MICE, though robust, is also computationally inten-
sive and requires careful tuning and validation. These weak-
nesses can affect the overall performance of community de-
tection when using imputed similarities.
The weighted similarity method, by directly incorporat-
ing the patterns of missing data into the similarity calcula-
tion, avoids these pitfalls and provides a more reliable mea-
sure of similarity, which is reflected in the superior perfor-

Density Internal Density Local Modularity0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Cosine MICE Cosine KNN Cosine
(a) Imputed cosine similarity vs weighted similarity
Density Internal Density Local Modularity0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Euclidean MICE Euclidean KNN Euclidean (b) Imputed euclidean similarity vs weighted similarity
Density Internal Density Local Modularity0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Canberra MICE Canberra KNN Canberra
(c) Imputed canberra similarity vs weighted similarity
Density Internal Density Local Modularity0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Spearman MICE Spearman KNN Spearman (d) Imputed spearman similarity vs weighted similarity
Figure 4: Average community qualities with 100 connected edges and 5 clusters. Higher bar indicates better community.
Conductance Expansion Normalized Cut0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Cosine MICE Cosine KNN Cosine
(a) Imputed cosine similarity vs weighted similarity
Conductance Expansion Normalized Cut0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Euclidean MICE Euclidean KNN Euclidean (b) Imputed euclidean similarity vs weighted similarity
Conductance Expansion Normalized Cut0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Canberra MICE Canberra KNN Canberra
(c) Imputed canberra similarity vs weighted similarity
Conductance Expansion Normalized Cut0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Spearman MICE Spearman KNN Spearman (d) Imputed spearman similarity vs weighted similarity
Figure 5: Average community qualities with 100 connected edges and 5 clusters. Shorter bar indicates better community.
mance metrics observed in this study. Calculating similarity
without requiring imputation reduces the risk of introducing
biases and preserves the original data distribution. This ca-
pability enhances the robustness of the similarity measure,
ensuring that it accurately reflects the true relationships be-
tween data points.
Adaption and Application
The weighted similarity can be easily adapted for differ-
ent data types and structures. Whether dealing with high-
dimensional numerical data, categorical data, or mixed data
types, the method can be adapted to the specific charac-
teristics of the dataset, providing a reliable similarity mea-
sure. This adaptability makes the method suitable for vari-
ous applications, from clustering in bioinformatics to com-
munity detection in social networks. The method also allows
for fine-tuning of the similarity components to suit specific
datasets.
The weighted similarity could be extremely useful for
three application scenarios. First, if the missing information
is caused by absence of a property or attribute. For example,
a shampoo brand does not have the antidandruff benefit; a

hotel does not have a swimming pool; and a social media
user does not belong to an ethnic group. Lack of properties
in this scenario is actually informative. Consumer reviews
on the above shampoo brand or hotel naturally do not have
topics and sentiments about antidandruff or swimming pool.
The weighted similarity can capture these missing informa-
tion very well without any misleading imputation.
Second, if the data are not missing at random, any impu-
tation method may be misleading in most cases. Practically,
it is very hard to infer whether the missing pattern is random
or not. It is particularly challenging to impute the missing
data if the data are highly sparse regardless missing at ran-
dom or not. These highly sparse data are quite common in
topics and sentiments derived using NLP models and LLMs
based on short documents like consumer reviews and social
media posts. In both cases, the weighted similarity can cap-
ture the missing pattern well for downstream applications
like community detection and clustering.
7 Conclusion
A weighted similarity has been formulated to calculate sim-
ilarity without imputation. It constructs similarity based on
both existence and lack of common properties and pattern
of missing data. It is particularly useful for advanced analyt-
ics on highly sparse data such as topics and sentiments from
NLP models on consumer reviews and social media posts.
The weighted similarity outperforms a variety of similar-
ity metrics using different imputation methods in the con-
text of community detection. The superior performance is
consistent and robust across metrics on both general com-
munity structures and average community quality. The su-
periority is even more pronounced on complex community
network graphs.
The weighted similarity offers a robust and versatile ap-
proach to measure similarity in the presence of missing data.
It could have broad applications on many advanced data an-
alytics dealing with sparse data.
References
Brzozowski, L.; Siudem, G.; and Gagolewski, M. 2023.
Community detection in complex networks via node simi-
larity, graph representation learning, and hierarchical clus-
tering. ArXiv, abs/2303.12212.
Clauset, A.; Newman, M. E. J.; and Moore, C. 2004. Find-
ing community structure in very large networks. Physical
Review E, 70(6): 066111.
Dunn, J. C. 1974. Well-separated clusters and optimal fuzzy
partitions. Journal of Cybernetics, 4(1): 95–104.
Fortunato, S. 2010a. Community detection in graphs.
Physics Reports, 486(3): 75–174.
Fortunato, S. 2010b. Community detection in graphs.
Physics Reports, 486(3-5): 75–174.
Girvan, M.; and Newman, M. E. J. 2002. Community struc-
ture in social and biological networks. Proceedings of the
National Academy of Sciences , 99(12): 7821–7826.
Jaewon, Y .; and Jure, L. 2012. Defining and Evaluating Net-
work Communities based on Ground-truth. In Proceedings
of 2012 IEEE Inter- national Conference on Data Mining
(ICDM).
Kannan, R.; Vempala, S.; and Vetta, A. 2004. On cluster-
ings: Good, bad and spectral. Journal of the ACM , 51(3):
497–515.
Lance, G. N.; and Williams, W. T. 1967. A general theory
of classificatory sorting strategies: 1. Hierarchical systems.
The Computer Journal, 9(4): 373–380.
Leskovec, J.; Lang, K. J.; Dasgupta, A.; and Mahoney,
M. W. 2008. Statistical properties of community structure
in large social and information networks. In Proceedings
of the 17th International Conference on World Wide Web ,
695–704.
Li, Z.; Zhang, S.; Wang, R.-S.; Zhang, X.-S.; and Chen, L.
2008. Quantitative function for community detection. Phys-
ical Review E, 77(3): 036109.
Little, R. J. A.; and Rubin, D. B. 2002. Statistical Analysis
with Missing Data. Wiley.
Newman, M. E. J. 2003. The structure and function of com-
plex networks. SIAM Review, 45(2): 167–256.
Newman, M. E. J. 2006. Modularity and community struc-
ture in networks. Proceedings of the National Academy of
Sciences, 103(23): 8577–8582.
Radicchi, F.; Castellano, C.; Cecconi, F.; Loreto, V .; and
Parisi, D. 2004. Defining and identifying communities in
networks. Proceedings of the National Academy of Sciences,
101(9): 2658–2663.
Shi, J.; and Malik, J. 2000. Normalized cuts and image seg-
mentation. IEEE Transactions on Pattern Analysis and Ma-
chine Intelligence, 22(8): 888–905.
Sneath, P. H. A.; and Sokal, R. R. 1973. Numerical Taxon-
omy. Freeman.
Spearman, C. 1904. The proof and measurement of associa-
tion between two things. The American Journal of Psychol-
ogy, 15(1): 72–101.
Tan, P.-N.; Steinbach, M.; and Kumar, V . 2005.Introduction
to Data Mining. Pearson.
Troyanskaya, O.; Cantor, M.; Sherlock, G.; Brown, P.;
Hastie, T.; Tibshirani, R.; Botstein, D.; and Altman, R. B.
2001. Missing value estimation methods for DNA microar-
rays. Bioinformatics, 17(6): 520–525.
van Buuren, S.; and Groothuis-Oudshoorn, K. 2011. MICE:
Multivariate Imputation by Chained Equations in R.Journal
of Statistical Software, 45(3).
Watts, D. J.; and Strogatz, S. H. 1998. Collective dynamics
of ’small-world’ networks. Nature, 393(6684): 440–442.

A Appendix
Range of Weighted Similarity
Assume we use cosine similarity to quantify the similarity
for Part 1 where both verctors having numercial value. Here
we prove that the range of the weighted similarity metric S,
is S ∈ [−1, 1].
Define |Vn1| = length of the numerical Part 1, |V1| =
length of vector V1 or V2, CN an= length of missing Part 2
and CN on= length of the non-matching Part 3 , consider
− |Vn1| |V1| ≤ SN um≤ |Vn1| |V1| (A1)
0 ≤ SN an≤ CN an |V1| (A2)
− CN on
|V1| ≤ SN on≤ 0 (A3)
and
CN on+ CN an+ |Vn1| = |V1| (A4)
(A1) + (A2) + (A3) implies
−
 |Vn1| + CN on
|V1|

≤ SN um+SN an+SN on≤ |Vn1| + CN an |V1|
(A5)
Define
S = SN um+ SN an+ SN on (A6)
From (A4), it can be deduced that|Vn1| = |V1| −CN on−
CN an. Add − CN an |V1| to both sides of (A5) and combine (A6)
gives
−1 ≤ S ≤ |Vn1| |V1| (A7)
Likewise, add CN on |V1| to both sides of (A5) and combine
(A6) gives
− |Vn1| |V1| ≤ S ≤ 1 (A8)
Add (A7) and (A8) gives
−

1 +|Vn1| |V1|  ≤ 2S ≤ 1 +|Vn1| |V1| . (A9)
Then
−
 |V1| + |Vn1|
2|V1|

≤ S ≤ |V1| + |Vn1| 2|V1| . (A10)
Since |V1|+|Vn1| 2|V1| > 0 then (A10) implies
−1 ≤ S ≤ 1. (A11)
Therefore, we have proved that S ∈ [−1, 1].
Traditional Imputation Methods
The formula for each of the imputation considered are de-
fined below:
1. Mean imputation: This imputation metric is defined by:
xi =
x if xi is missing
xi otherwise (A12)
where x is the mean of the non-missing values of feature
x.
2. K-Nearest Neighbors (KNN) imputation: This imputa-
tion metric is defined by:
xi = 1 K X j∈N(i) xj (A13)
where N (i) denotes the set of K nearest neighbors of
instance i.
3. MICE: The metric defined for this imputation is given
by:
ˆx(m) i = f (Xobs) +ϵ(m) i (A14)
where Xobs represents observed values, f is the imputa-
tion model, and ϵ(m) i is a random error term. The final
imputed value is an average of the multiple imputations.
Traditional Similarity Measures
The formulas of the 4 similarities considered in this paper
are defined below:
1. Cosine Similarity: This similarity formula is defined by:
Cosine Similarity = A · B ∥A∥∥B∥ (A15)
where A · B is the dot product of vectors A and B, and
∥A∥ and ∥B∥ are their magnitudes.
2. Euclidean Distance: The euclidean distance metric is de-
fined by:
Euclidean Distance =
vuut nX
i=1
(ai − bi)2 (A16)
where ai and bi are the components of vectors A and B.
3. Canberra Distance: This distance metric is defined by:
Canberra Distance =
nX
i=1
|ai − bi|
|ai| + |bi| (A17)
4. Spearman Correlation: This correlation metric is defined
by:
Spearman’s ρ = 1− 6 P d2 i
n(n2 − 1) (A18)
where di is the difference between the ranks of corre-
sponding values.

The Girvan-Newman Algorithm
The Girvan-Newman algorithm is a popular method for
community detection in complex networks. It identifies
communities by iteratively removing edges with the high-
est betweenness centrality, which measures the number of
shortest paths that pass through an edge. The removal of
these edges disrupts the network, eventually splitting it into
distinct communities (Girvan and Newman 2002).
Betweenness Centrality Betweenness centrality is a key
concept in the Girvan-Newman algorithm. It quantifies the
importance of an edge by counting the number of shortest
paths between pairs of nodes that pass through it. Formally,
the betweenness centrality CB(e) of an edge e is given by:
CB(e) =
X
s̸=t̸=e
σst(e)
σst
(A19)
where σst is the total number of shortest paths from node
s to node t, and σst(e) is the number of those paths that pass
through edge e.
Algorithm Steps The Girvan-Newman algorithm pro-
ceeds as follows:
1. Compute Betweenness Centrality : Calculate the be-
tweenness centrality for all edges in the network.
2. Remove Edge : Remove the edge with the highest be-
tweenness centrality.
3. Recompute Betweenness Centrality : Recalculate the
betweenness centrality for all remaining edges.
4. Repeat: Repeat steps 2 and 3 until no edges remain or
until the desired number of communities is achieved.
This iterative process effectively identifies the most criti-
cal edges that connect different communities. By removing
these edges, the algorithm reveals the underlying community
structure of the network. The Girvan-Newman algorithm is
advantageous because it does not require a priori knowledge
of the number of communities and can reveal hierarchical
community structures. However, it is computationally inten-
sive, especially for large networks, due to the repeated com-
putation of betweenness centrality. Additionally, the algo-
rithm’s performance is highly dependent on the quality of
the similarity measure used to define the edges. For the pur-
pose of the study, we employ parallel computing in this stage
to utilize the algorithm.
Performance Metrics of the Community Detection
As already introduced in the early section, the metrics are
grouped into two folds: general community structure perfor-
mance and average community quality metrics. The formu-
las are defined in the subsequent sections.
General Community Structures Performance Metrics
1. Modularity (Q) (Newman 2006): One of the most
widely used metrics for assessing community struc-
ture is modularity (Q) which measures the strength of
the division of a network into communities as defined
by (A20). High modularity indicates dense connections
within communities and sparse connections between
communities. The metric is defined as
Q = 1 2m X i,j  Aij − kikj 2m  δ(ci, cj) (A20)
where Aij is the adjacency matrix, ki is the degree of
node i, m is the total number of edges in the network, ci
is the community to which node i belongs, and δ(ci, cj)
is the Kronecker delta, which is 1 if ci = cj and 0 other-
wise. Modularity values range from -1 to 1. Higher val-
ues indicate a better-defined community structure, where
nodes within the same community are more densely con-
nected than nodes in different communities (stronger
community structure with dense intra-community edges
and sparse inter-community edges).
2. Coverage (Fortunato 2010b): Coverage is the fraction
of edges that fall within the detected communities com-
pared to the total number of edges in the network and is
defined by:
Coverage = Number of intra-community edges Total number of edges (A21)
Coverage values range from 0 to 1. High coverage values
suggest that the algorithm effectively captures the over-
all structure of the network by ensuring that most edges
are within communities. This metric is useful for under-
standing how well the algorithm can preserve the internal
connectivity of communities.
3. Dunn Index (Dunn 1974): As defined by (A22), Dunn
index is a ratio of the minimum inter-cluster distance to
the maximum intra-cluster distance. Higher values indi-
cate better clustering.
D = min{d(i, j)|1 ≤ i ≤ j ≤ n} max{δ(k)|1 ≤ k ≤ n} (A22)
where d(i, j) is the distance between clustersi and j, and
δ(k) is the diameter of cluster k. Higher Dunn index val-
ues indicate better clustering with well-separated clusters
and compact intra-cluster distances. This metric helps as-
sess the distinctiveness and cohesiveness of the detected
communities.
4. Average Clustering Coefficient (Watts and Strogatz
1998): This coefficient measures the degree to which
nodes in a graph tend to cluster together. Values range
from 0 to 1, with higher values indicating a higher de-
gree of clustering. It is defined by:
C = 1 n
nX
i=1
Ci (A23)
where Ci is the local clustering coefficient of node i, and
n is the total number of nodes.
5. Transitivity (Newman 2003): This metric measures the
probability that the adjacent vertices of a vertex are con-
nected as defined by (A24). Values range from 0 to 1,
with higher values indicating that nodes tend to form tri-
angles, suggesting strong community structure.

T = 3 × number of triangles number of connected triples of vertices (A24)
6. Modularity Density (Li et al. 2008): This metric consid-
ers the density of communities. Higher values indicate
better community structure with consideration for den-
sity and is defined by (A25).
QD =
kX
i=1
 2mi
ni(ni − 1)
 di
m (A25)
where mi is the number of edges in community i, ni is
the number of nodes in community i, di is the internal
density of community i, and m is the total number of
edges in the network.
7. Triangle Participation Ratio (TPR) (Jaewon and Jure
2012): As defined by (A26), this ratio measures the frac-
tion of nodes participating in at least one triangle. Values
range from 0 to 1, with higher values indicating more par-
ticipation in triangles, suggesting a stronger community
structure.
TPR = |{v ∈ V : v participates in at least one triangle}| |V |
(A26)
where V is the set of all nodes.
Average Community Quality Metrics
1. Conductance (Kannan, Vempala, and Vetta 2004): Con-
ductance is a crucial metric for evaluating the quality of
individual communities. It measures the fraction of to-
tal edge volume that points outside the community, pro-
viding an indication of how well-defined and isolated
the community is. Conductance values range from 0 to
1. Lower conductance values suggest better community
quality, as fewer edges leave the community, indicating
that the community is more self-contained. The metric is
defined by
ϕ(S) = cS
2mS + cS
(A27)
where cS is the number of edges leaving the community
S and mS is the number of edges inside the community
S.
2. Expansion (Leskovec et al. 2008): This metric measures
the number of edges per node that point outside the com-
munity. Lower values indicate better community isola-
tion with fewer connections to the rest of the network.
This metric helps evaluate how well the community is
separated from the rest of the network, which is crucial
for understanding the distinctiveness of the community
and is defined by:
Expansion(S) = |{(u, v) ∈ E : u ∈ S, v /∈ S}| |S| (A28)
where |S| is the number of nodes in community S.
3. Normalized Cut (Shi and Malik 2000): This metric mea-
sures the total edge weight connecting the nodes in the
community to the rest of the graph. Lower values indi-
cate better community isolation and minimal connections
between the community and the rest of the network. This
metric provides insights into the overall quality of the
community structure by considering both the internal and
external connections of the community and is defined by:
Ncut(S) = cS
2mS + cS
+ cT
2mT + cT
(A29)
where cS is the number of edges leaving community S,
mS is the number of edges inside communityS, cT is the
number of edges leaving the complement of community
S, and mT is the number of edges inside the complement
of community S.
4. Density (Radicchi et al. 2004): This metric measures the
fraction of possible edges within the community that are
actually present. Values range from 0 to 1, with higher
values indicating denser communities, suggesting that
the nodes within the community are more tightly con-
nected. This metric helps assess the internal connectivity
of the community and its overall cohesiveness and is de-
fined by:
Density(S) = 2mS
|S|(|S| −1) (A30)
where mS is the number of edges within community S
and |S| is the number of nodes in community S.
5. Internal Density (Fortunato 2010b): This metric mea-
sures the density of edges within the community. Val-
ues range from 0 to 1, with higher values indicating bet-
ter internal connectivity within communities, suggesting
that the community is more cohesive and well-connected.
This metric provides insights into the quality of the inter-
nal structure of the community. Internal Density is de-
fined by:
Internal Density(S) = 2mS
|S|(|S| −1) (A31)
where mS is the number of edges within community S
and |S| is the number of nodes in community S.
6. Local Modularity (Clauset, Newman, and Moore 2004):
This metric measures the quality of the division of a net-
work into communities on a local scale. Higher values
indicate better community structure, suggesting that the
community is well-defined and cohesive. This metric is
particularly useful for understanding the local properties
of the community and its overall quality. It is defined by:
Qlocal =
kX
i=1

li
m −
 di
2m
2!
(A32)
where li is the number of edges within community i, di
is the sum of the degrees of the nodes in community i,
and m is the total number of edges in the network.

(a) Cosine similarity based on mean imputation
 (b) Cosine similarity based on MICE imputation
Figure A1: Community structures with 5 clusters and 100 connected edges based on the weighted similarity and imputed cosine
similarities using mean and MICE.

(a) Weighted similarity
 (b) Euclidean similarity based on mean imputation
(c) Euclidean similarity based on MICE imputation
 (d) Euclidean similarity based on KNN(k=4) imputation
Figure A2: Community structures with 5 clusters and 100 connected edges based on the weighted similarity and imputed
euclidean similarities.

(a) Weighted similarity
 (b) Canberra similarity based on mean imputation
(c) Canberra similarity based on MICE imputation
 (d) Canberra similarity based on KNN(k=4) imputation
Figure A3: Community structures with 5 clusters and 100 connected edges based on the weighted similarity and imputed
canberra similarities.

(a) Weighted similarity
 (b) Spearman similarity based on mean imputation
(c) Spearman similarity based on MICE imputation
 (d) Spearman similarity based on KNN(k=4) imputation
Figure A4: Community structures with 5 clusters and 100 connected edges based on the weighted similarity and imputed
spearman similarities.

(a) Weighted similarity
 (b) Cosine similarity based on mean imputation
(c) Cosine similarity based on MICE imputation
 (d) Cosine similarity based on KNN(k=4) imputation
Figure A5: Community structures with 5 clusters and 600 connected edges based on the weighted similarity and imputed cosine
similarities.

MQ C DI ACC T MD TPR0.0
0.2
0.4
0.6
0.8
1.0Metric Value
Weighted Similarity Mean Cosine MICE Cosine KNN Cosine
(a) Imputed cosine similarity vs. weighted similarity
MQ C DI ACC T MD TPR0.0
0.2
0.4
0.6
0.8
1.0Metric Value
Weighted Similarity Mean Euclidean MICE Euclidean KNN Euclidean (b) Imputed euclidean similarity vs. weighted similarity
MQ C DI ACC T MD TPR0.0
0.2
0.4
0.6
0.8
1.0Metric Value
Weighted Similarity Mean Canberra MICE Canberra KNN Canberra
(c) Imputed canberra similarity vs. weighted similarity
MQ C DI ACC T MD TPR0.0
0.2
0.4
0.6
0.8
1.0Metric Value
Weighted Similarity Mean Spearman MICE Spearman KNN Spearman (d) Imputed spearman vs. weighted similarity
Figure A6: Performance metrics on general community structures with 600 connected edges and 5 clusters. MQ: Modularity Q,
C: Coverage, DI: Dunn Index, ACC: Average Clustering Coefficient, T: Transitivity, MD: Modularity Density, TPR: Triangle
Participation Ratio. Higher bar indicates better community structure.

Density Internal Density Local Modularity0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Cosine MICE Cosine KNN Cosine
(a) Imputed cosine similarity vs. weighted similarity
Density Internal Density Local Modularity0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Euclidean MICE Euclidean KNN Euclidean (b) Imputed euclidean similarity vs. weighted similarity
Density Internal Density Local Modularity0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Canberra MICE Canberra KNN Canberra
(c) Imputed canberra similarity vs. weighted similarity
Density Internal Density Local Modularity0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Spearman MICE Spearman KNN Spearman (d) Imputed spearman similarity vs. weighted similarity
Figure A7: Average community qualities with 600 connected edges and 5 clusters. Higher bar indicates better community.

Conductance Expansion Normalized Cut0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Cosine MICE Cosine KNN Cosine
(a) Imputed cosine similarity vs. weighted similarity
Conductance Expansion Normalized Cut0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Euclidean MICE Euclidean KNN Euclidean (b) Imputed euclidean similarity vs. weighted similarity
Conductance Expansion Normalized Cut0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Canberra MICE Canberra KNN Canberra
(c) Imputed canberra similarity vs. weighted similarity
Conductance Expansion Normalized Cut0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Spearman MICE Spearman KNN Spearman (d) Imputed spearman similarity vs. weighted similarity
Figure A8: Average community qualities with 600 connected edges and 5 clusters. Shorter bar indicates better community.

(a) Weighted similarity
 (b) Cosine similarity based on mean imputation
(c) Cosine similarity based on MICE imputation
 (d) Cosine similarity based on KNN(k=4) imputation
Figure A9: Community structures with 5 clusters and 1200 connected edges based on the weighted similarity and imputed
cosine similarities.

MQ C DI ACC T MD TPR0.0
0.2
0.4
0.6
0.8
1.0Metric Value
Weighted Similarity Mean Cosine MICE Cosine KNN Cosine
(a) Imputed cosine similarity vs. weighted similarity
MQ C DI ACC T MD TPR0.0
0.2
0.4
0.6
0.8
1.0Metric Value
Weighted Similarity Mean Euclidean MICE Euclidean KNN Euclidean (b) Imputed euclidean similarity vs.weighted similarity
MQ C DI ACC T MD TPR0.0
0.2
0.4
0.6
0.8
1.0Metric Value
Weighted Similarity Mean Canberra MICE Canberra KNN Canberra
(c) Imputed canberra similarity vs. weighted similarity
MQ C DI ACC T MD TPR0.0
0.2
0.4
0.6
0.8
1.0Metric Value
Weighted Similarity Mean Spearman MICE Spearman KNN Spearman (d) Imputed spearman similarity vs. weighted similarity
Figure A10: Performance metrics on general community structures with 1200 connected edges and 5 clusters. MQ: Modularity
Q, C: Coverage, DI: Dunn Index, ACC: Average Clustering Coefficient, T: Transitivity, MD: Modularity Density, TPR: Triangle
Participation Ratio. Higher bar indicates better community structure.

Density Internal Density Local Modularity0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Cosine MICE Cosine KNN Cosine
(a) Imputed cosine similarity vs. weighted similarity
Density Internal Density Local Modularity0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Euclidean MICE Euclidean KNN Euclidean (b) Imputed euclidean similarity vs. weighted similarity
Density Internal Density Local Modularity0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Canberra MICE Canberra KNN Canberra
(c) Imputed canberra similarity vs. weighted similarity
Density Internal Density Local Modularity0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Spearman MICE Spearman KNN Spearman (d) Imputed spearman similarity vs. weighted similarity
Figure A11: Average community qualities with 1200 connected edges and 5 clusters. Higher bar indicates better community.

Conductance Expansion Normalized Cut0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Cosine MICE Cosine KNN Cosine
(a) Imputed cosine similarity vs. weighted similarity
Conductance Expansion Normalized Cut0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Euclidean MICE Euclidean KNN Euclidean (b) Imputed euclidean similarity based vs. weighted similarity
Conductance Expansion Normalized Cut0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Canberra MICE Canberra KNN Canberra
(c) Imputed canberra similarity vs. weighted similarity
Conductance Expansion Normalized Cut0.0
0.2
0.4
0.6
0.8
1.0Average Metric Value
Weighted Similarity Mean Spearman MICE Spearman KNN Spearman (d) Imputed spearman similarity vs. weighted similarity
Figure A12: Average community qualities with 1200 connected edges and 5 clusters. Shorter bar indicates better community.
