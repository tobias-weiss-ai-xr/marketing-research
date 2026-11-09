---
title: 'Enhancing Cross-Market Recommendation System with Graph Isomorphism Networks: A Novel Approach
  to Personalized User Experience'
url: https://arxiv.org/abs/2409.07850
category: ai-marketing
subcategory: empirical
date: 2024-09
venue: ''
authors:
- Sümeyye Öztürk
- Ahmed Burak Ercan
- Resul Tugay
- Şule Gündüz Öğüdücü
source: arxiv
pdf_url: https://arxiv.org/pdf/2409.07850
pages: 7
chars: 42652
fetched_at: '2026-11-08T13:17:06+00:00'
kb_version: 1
---

# Enhancing Cross-Market Recommendation System with Graph Isomorphism Networks: A Novel Approach to Personalized User Experience

Enhancing Cross-Market Recommendation System with Graph
Isomorphism Networks: A Novel Approach to Personalized User
Experience
Sümeyye Öztürk
ozturks20@itu.edu.tr
Istanbul Technical University
Istanbul, Turkey
Ahmed Burak Ercan
Istanbul Technical University
Istanbul, Turkey
ercana20@itu.edu.tr
Resul Tugay
Gazi University
Ankara, Turkey
resultugay@gazi.edu.tr
Şule Gündüz Öğüdücü
Istanbul Technical University
Istanbul, Turkey
sgunduz@itu.edu.tr
ABSTRACT
In today’s world of globalized commerce, cross-market recommen-
dation systems (CMRs) are crucial for providing personalized user
experiences across diverse market segments. However, traditional
recommendation algorithms have difficulties dealing with market
specificity and data sparsity, especially in new or emerging markets.
In this paper, we propose the CrossGR model, which utilizes Graph
Isomorphism Networks (GINs) to improve CMR systems. It out-
performs existing benchmarks in NDCG@10 and HR@10 metrics,
demonstrating its adaptability and accuracy in handling diverse
market segments. The CrossGR model is adaptable and accurate,
making it well-suited for handling the complexities of cross-market
recommendation tasks. Its robustness is demonstrated by consistent
performance across different evaluation timeframes, indicating its
potential to cater to evolving market trends and user preferences.
Our findings suggest that GINs represent a promising direction for
CMRs, paving the way for more sophisticated, personalized, and
context-aware recommendation systems in the dynamic landscape
of global e-commerce.
CCS CONCEPTS
• Information systems→ Data mining.
KEYWORDS
Cross-market recommendations, graph isomorphism networks
(GINs), user-item interaction modeling, market specificity in e-
commerce, pattern recognition, data mining
ACM Reference Format:
Sümeyye Öztürk, Ahmed Burak Ercan, Resul Tugay, and Şule Gündüz
Öğüdücü. 2024. Enhancing Cross-Market Recommendation System with
Graph Isomorphism Networks: A Novel Approach to Personalized User
Permission to make digital or hard copies of part or all of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for third-party components of this work must be honored.
For all other uses, contact the owner/author(s).
ICMLT 2024, May 24–26, 2024, Oslo, Norway
© 2024 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-1637-9/24/05.
https://doi.org/10.1145/3674029.3674069
Experience. In 2024 9th International Conference on Machine Learning Tech-
nologies (ICMLT) (ICMLT 2024), May 24–26, 2024, Oslo, Norway. ACM, New
York, NY, USA, 7 pages. https://doi.org/10.1145/3674029.3674069
1 INTRODUCTION
Recommendation systems play a crucial role in providing person-
alized user experiences across various fields like e-commerce, en-
tertainment, and content platforms. Most of these systems provide
recommendations exclusively for items within a specific or single
domain. Yet, traditional methods encounter challenges in target
markets where data is scarce or unavailable, along with substantial
variations in user behaviors. To address these challenges, Cross-
Domain Recommendation (CDR) and Cross-Market Recommenda-
tion (CMR) have emerged as promising approaches [3]. Although
both approaches aim to enhance recommendation performance
by utilizing information from different domains or markets, they
address distinct challenges and find applications in different sce-
narios.
CDR is to make recommendations across domains or markets. It
is concerned with providing suggestions in a target domain based
on knowledge obtained from a source domain [14]. For example,
knowledge about a user’s book purchases can also be used to offer
suggestions on some other seemingly irrelevant topics, like film or
music. This approach improves the user experience because there
may be dependencies and correlations between user preferences in
different domains. Consider a multinational e-commerce company
operating across many countries in Europe and is looking to expand
into a new market, like Spain, where there is limited local data
available. The entity can improve the quality of its recommendation
algorithms in Spain by using strong data from mature markets.
This approach not only customizes the shopping experience for the
Spanish audience but also opens up the door for the company’s
growth in the region.
CMR is the choice, for this research paper for a variety of reasons.
Firstly, it allows businesses to explore markets and seize opportuni-
ties by using data from established markets [3]. This means that
when faced with data in a new market personalized recommenda-
tions can still be offered to users enhancing their experience and
boosting engagement. Secondly, CMR tackles the challenge of data
in target markets by utilizing data from source markets that have
arXiv:2409.07850v1  [cs.IR]  12 Sep 2024

ICMLT 2024, May 24–26, 2024, Oslo, Norway S. Ozturk et al.
diverse interactions. This significantly improves the performance of
recommendations in the target market [34]. Lastly, it facilitates the
discovery of user preferences and behaviors that may vary across
markets [15]. By using insights from source markets, the system
can adapt to users’ distinct characteristics and preferences, in the
target market.
Traditional recommendation methods, such as collaborative fil-
tering [11] and content-based filtering [19], have been widely used
for making recommendations in one market. However, these meth-
ods often rely on user-item interactions or item attributes within a
specific market, making them less effective in understanding the
complexities of CMRs. The limitations of traditional methods in the
context of CMR can be attributed to several factors. Firstly, the lack
of data compatibility and heterogeneity across markets presents
challenges in using user-item interactions or item attributes from
one market to another. Additionally, the differences in user prefer-
ences, market dynamics, and product characteristics across markets
further complicate the recommendation task [2].
These conventional approaches depend on user-item interactions
or item attributes within a market, which restricts their usefulness
in market activities. Therefore, to provide recommendations that
apply across markets, it is necessary to employ advanced strate-
gies capable of navigating the intricacies of the global market [3].
Researchers have turned to Graph Neural Networks (GNNs) to cap-
ture relationships and dependencies in graph data to tackle these
challenges [7]. GNNs have gained popularity in recommender sys-
tems and have demonstrated exceptional capabilities in creating
user-item representations. Unlike traditional methods, GNNs can
incorporate neighborhood information and relational dependen-
cies among items and users, providing a more comprehensive and
contextually enriched representation [16].
Using GNNs in CMR systems can offer more personalized and on-
demand suggestions [21]. Compared to traditional methods, GNNs
offer great performance in CMRs due to their ability to manage
sparse data and also social information. GNN-based models utilize
high-order connectivity, which refers to the capability of these mod-
els to capture relationships beyond immediate neighbors in a graph
structure [30]. Traditional GNNs typically consider only first-order
connections, i.e., direct neighbors of a node [ 9]. However, high-
order connectivity extends this concept to include connections up
to k-th order, where k is a parameter that determines the depth of
exploration in the graph. By incorporating high-order connectivity,
GNNs can effectively capture more complex patterns and depen-
dencies in the data. This allows GNN-based models to leverage
not only direct interactions but also indirect relationships between
nodes, enabling a more comprehensive understanding of the under-
lying graph structure. In the context of collaborative filtering and
recommendation systems, high-order connectivity enables GNNs
to extract valuable information from distant nodes in the graph,
leading to more accurate and personalized suggestions for users
[27]. Furthermore, high-order connectivity enhances the ability of
GNNs to handle sparse data by using information from nodes that
are not directly connected but are reachable through intermediate
nodes. This is particularly beneficial in scenarios where data spar-
sity is a common challenge, as it enables GNNs to exploit the full
potential of the available information in the graph [32].
2 LITERATURE REVIEW
Cross-market recommendation has made significant progress in
recent years, with researchers exploring traditional methods as
well as GNNs to tackle the challenges posed by data sparsity and
cold-start issues in target markets [17].
By combining deep graph recommendation models like GNNs
and conventional models like ItemCF [22] and UserCF [33], CMR
leverages colloborative signals and similarities across marketplaces.
The efficacy of such an approach, employing a combination of
models including DeepWalk [ 20] and LightGBM [ 13], has been
notably shown on the XMRec dataset [4].
Creating generalized representations for CMR has centered on in-
tegrating self-supervised graph learning. SGLCMR, models market-
specific aspects by creating single-market graphs and market-
generalized features by creating cross-market graphs [35]. Exten-
sive studies on real-world datasets have demonstrated the supe-
riority of this methodology over state-of-the-art CMR methods,
since of its utilization of Light Graph Convolution (LGC) [8] and
self-supervised graph learning.
With models like Bert4CMR, the attention mechanism has also
been investigated in CMR with the goal of enhancing recommen-
dation performance across markets [12]. This model uses market
embedding to simulate each market’s bias and minimize mutual
interference between parallel markets, demonstrating cutting-edge
outcomes from comprehensive testing.
Graph Attention Networks (GATs) [24] was a significant break-
through that addressed the shortcomings of previous graph convo-
lution approaches and allowed for more complex interactions be-
tween nodes in a variety of applications, including protein-protein
interaction datasets and citation networks. This breakthrough was
extended by the HGNNDR model [18], which improved node fea-
ture representation in situations with sparse network connections
by using multi-order topology information. This improved the qual-
ity of recommendations. Similarly, to address the issues of data
sparsity and cold-start in item recommendation, the TransD-KGAT
method [28] used knowledge graphs, highlighting the effect of
GNN-based approaches in recommendation tasks.
Models such as GraphRec [5] and SR-GNN [26] became special-
ized frameworks concentrating on social and session-based recom-
mendations. These models demonstrate the adaptability of GNNs
in capturing complicated relationships between users and items in
a variety of recommendation scenarios, offering complete represen-
tations of user-item relationships and enhancing recommendation
accuracy. They also complement the enhanced collaborative filter-
ing recommendation model [6].
With the introduction of FOREC, the field also witnessed notable
advancements in cross-market product recommendation, where
it demonstrated its supremacy on the XMarket dataset by utiliz-
ing data from both source and target markets [3]. In addition, the
Heterogeneous Graph Attention Network (HAN) is introduced,
which extends GNNs to heterogeneous graphs and shows that it
can manage diverse data difficulties and achive better performance
on real-world heterogeneous grahps [25].
Recent advancements in CMR systems have showcased the ver-
satility and efficacy of GNNs. One notable example includes a rec-
ommendation algorithm based on graph factorization machines

Enhancing Cross-Market Recommendation System with Graph Isomorphism Networks: A Novel Approach to Personalized User Experience ICMLT 2024, May 24–26, 2024, Oslo, Norway
that incorporates an attention mechanism and graph construction
[23]. This approach utilizes GNNs to notably enhance recommen-
dation performance by encoding collaboration signals. Similarly,
the Neural Graph for Personalized Tag Recommendation (NGTR)
model [31] employs GNNs to improve tag representation learning,
thereby increasing the accuracy of tag recommendations.
3 METHODOLOGY
To address CMR challenges, we propose "CrossGR, " a new method
utilizing GIN for their ability to analyze complex user-item graphs,
enhancing CMR effectiveness. GINs, introduced by Xu et al. (2018)
[29], matches the Weisfeiler-Lehman test in graph analysis prowess,
offering a nuanced understanding of graph topology, which marks
a significant advancement over prior graph neural network models.
This approach allows "CrossGR" to more effectively harness the in-
herent topological features of graphs for improved recommendation
accuracy.
The motivation behind GIN for our CMR task arises from its
unique aggregation function that updates node representations by
summing the features of neighboring nodes, including the node
itself. This approach ensures that the network can distinguish be-
tween different graph structures, a property known as injectivity,
which is critical when dealing with diverse and sparse data inherent
in cross-market scenarios. The steps applied in our methodology,
from data representation to model optimization, are visually sum-
marized in Figure 1, which complements the detailed explanations
provided in the following subsections.
3.1 Data Representation
3.1.1 Notation. In the construction of our graph-based data rep-
resentation for the CMR system, we encapsulate the user-item
interactions within graph 𝐺, composed of a set of nodes 𝑉 and
a set of edges 𝐸. The nodes in 𝑉 represent both users and items
in the dataset, drafted as sets𝑈 and𝐼 respectively, reflecting the
dual nature of our marketplaces. Interactions between users and
items, such as ratings or purchases, form the edges in𝐸, bridging
the two distinct sets within our graph. To quantify the interactions
encapsulated by𝐸, we introduce an adjacency matrix𝐴, where the
weight of each edge 𝐴𝑖𝑗 signifies the strength and nature of the
interaction between user𝑖 and item 𝑗. This setup inherently forms
a bipartite graph, capturing the distinct user-item relationships
within our system.
To ensure that our model can learn from these interactions with-
out bias toward nodes with higher degrees of connectivity, we
normalize the adjacency matrix using the diagonal degree matrix
𝐷, where each diagonal element 𝐷𝑖𝑖 corresponds to the sum of
weights connected to node𝑖. The normalization process, yielding
˜𝐴 =𝐷−1𝐴, ensures that the influence of each node is adjusted by its
connectivity, facilitating a balanced and effective learning process.
3.2 Graph Isomorphism Network Architecture
Our CrossGr model employs embeddings for initially representing
users and items, mapping their features into a latent space. This
foundational step is crucial for capturing the essence of user-item
interactions. Subsequently, through the application of GINConv
layers, we refine these embeddings by aggregating and transform-
ing features from their neighborhoods. This process enhances the
model’s ability to accurately reflect the complex dynamics of inter-
actions.
The GIN leverages a message-passing framework that iteratively
updates node representations by aggregating features from their
neighborhoods, thus encapsulating local and global market struc-
tures. The model’s forward pass involves a series of convolutional
operations, each comprising two key components: feature transfor-
mation and neighborhood aggregation. Specifically, the GINConv
layer employs an "add" aggregation function – a choice motivated by
its effectiveness in preventing the over-smoothing of node features,
a common challenge in deep GNNs where node representations
can become indistinguishable.
The embeddings are updated through the forward pass of the net-
work, where GINConv aggregates features from the nodes’ neigh-
borhoods, refining the representations based on local and global
structural information. The convolutional layers in our model are
designed to enhance the expressiveness of node embeddings. They
employ learnable linear transformations followed by a non-linear
activation function, ReLU, The layers are parameterized to allow
for the flexibility needed to capture the diverse interaction patterns
found in cross-market data. The process can be mathematically
expressed as:
𝐻(𝑘+1) =𝑀𝐿𝑃(𝑘) '›
«
(1+𝜖(𝑘))· 𝐻(𝑘)+ ∑︁
𝑢∈𝑁(𝑣)
𝐻(𝑘) 𝑢 “ﬁ
‹
(1)
Where𝐻(𝑘) represents the node features at the 𝑘𝑡ℎ iteration,
𝑁(𝑣) denotes the set of neighbors of node 𝑣, and𝜖 is a learnable
parameter that modulates the contribution of the node’s features in
the aggregation process. An MLP (Multi-Layer Perceptron) allows
for a more profound combination of features before updating the
node representation.
In practice, the embeddings are passed through a sequence of
ReLU-activated GINConv layers, followed by a final MLP that com-
bines user and item embeddings to predict the interaction score.
The MLP consists of a linear layer that doubles the embedding size,
a ReLU activation, and another linear layer that projects the com-
bined embeddings down to a single score. This score is then passed
through a sigmoid function to yield a probability, representing the
likelihood of interaction between the user and the item. The process
can be mathematically expressed as follows:
𝐻(𝑘+1) = ReLU  GINConv  𝐻(𝑘),𝐴  +𝜖(𝑘)·𝐻(𝑘)  (2)
Where 𝐻(𝑘) denotes the hidden representations of nodes at
the𝑘-th layer,𝐴 is the adjacency matrix, and 𝜖(𝑘) is a learnable
parameter that allows for distinguishing the node’s features from
its neighbors. The GINConv operation performs a sum aggregation
of neighbor features followed by a linear transformation.
3.3 Model Optimization and Hyperparameters
The model concatenates user and item embeddings to predict in-
teraction scores via a Multi-Layer Perceptron (MLP). We employ
Binary Cross-Entropy (BCE) as our loss function:

ICMLT 2024, May 24–26, 2024, Oslo, Norway S. Ozturk et al.
Figure 1: Overview of the CrossGR framework for enhancing cross-market recommendations. Input of the model is a bipartite
graph that represents interactions between users and items. The model utilizes two GINConv layers to transform these
interactions into an embedding space. Then concationation of these embbeddings is passed through an MLP layer to predict
the interaction scores. Lastly, a sigmoid function is applied to convert the scores into probabilities, providing the final
recommendation prediction.
L =− 1 𝑁 ∑︁ (𝑢,𝑖)∈𝐷 (𝑦𝑢𝑖 log(𝜎( ˆ𝑦𝑢𝑖))+( 1−𝑦𝑢𝑖) log(1−𝜎( ˆ𝑦𝑢𝑖)))
(3)
where𝐷 is the set of user-item pairs, 𝑦𝑢𝑖 is the true label, ˆ𝑦𝑢𝑖
is the predicted score, and 𝜎 denotes the sigmoid function. The
loss is minimized using the Adam optimizer with a learning rate
𝛼, and other hyperparameters such as the mini-batch size 𝐵, the
weight decay coefficient𝜆, and dropout rate𝑝 to prevent overfit-
ting. The specific values for these hyperparameters are empirically
determined through a grid search on the validation set.
For model optimization, we utilize the Adam optimizer with a
learning rate specified by adam_lr. The choice of Adam is due to its
adaptive learning rate capabilities, which are particularly beneficial
in the sparse and skewed distribution of CMR datasets. This process
iteratively adjusts the embeddings and the weights of the GINConv
and MLP layers to enhance the model’s predictive performance on
the training data.
4 EXPERIMENTS
In this section, we evaluate the performance of our proposed
CrossGr model through a series of experiments. We aim to demon-
strate CrossGr’s effectiveness in enhancing cross-market recom-
mendation systems compared to existing models. To prepare for
our experimental analysis, we have divided this section into several
key subsections. Firstly, we describe the datasets used in our study,
highlighting their relevance and the challenges they pose for cross-
market recommendation systems. Then, we provide details about
the experimental setup, including parameter settings and the rea-
sons for selecting certain evaluation metrics. Finally, we discuss the
implications of our findings, providing insights into the potential
impact of CrossGr on the field of recommendation systems. This
structured approach ensures a comprehensive evaluation of our
model’s capabilities and comparative effectiveness.
4.1 Data & Data Analysis
The Dataset provided by the competition organizer [ 1] contains
user interactions from five distinct markets, detailed in Table 1.
This table presents a breakdown of the datasets into three source
markets (s1, s2, and s3) with a substantial number of users and in-
teractions, highlighting the breadth of consumer data available for
analysis. Additionally, two target markets (t1 and t2) are included,
showcasing a more focused set of interactions that will be cru-
cial for testing the transferability of our recommendation system.
The variation in the number of users and interactions across these
markets underscores the need for a recommendation system that
can adapt to different levels of market data density and user-item
interaction frequency.
Table 1: General Description of Datasets
Dataset # Users # Items # Interactions
s1 6466 9762 77173
s2 7109 2198 48302
s3 3328 1245 23367
t1 2697 1357 19615
t2 5482 2917 41226
Dataset Structure: For an effective CMR system, understanding
the shared item count across markets is essential. Our analysis,
depicted in Table 2, focuses on the item overlap between different
markets. Importantly, it should be noted that there are no common
users between these markets, underscoring the distinct nature of
each market’s user base and the unique challenge it presents in
CMRs. This information can potentially assist in closing the gap
between user preferences and expectations across different markets.
4.1.1 Data Characteristics. The following highlights were obtained
from the dataset:
• The market ratings are mostly between 4 to 5 with an average
of 4.6, indicating the feasibility of direct knowledge transfer
based on ratings.

Enhancing Cross-Market Recommendation System with Graph Isomorphism Networks: A Novel Approach to Personalized User Experience ICMLT 2024, May 24–26, 2024, Oslo, Norway
Table 2: Summary of Overlap Items
Market Total s1 s2 s3 t1 t2
t1 1357 796 863 712 - 530
t2 2917 1834 789 548 530 -
• The users in each market are distinct and non-overlapping
to prevent overfitting of specific user behaviors.
• The items, on the other hand, exhibit a pronounced overlap,
especially in the target markets. This reinforces the signifi-
cance of using item information across markets to improve
the recommendation system’s accuracy.
4.2 Evaluation Metrics
In order to evaluate the performance of our recommendation system
simply and accurately, we utilize a strict evaluation methodology
that attaches to the highest standards in the field. This methodology
utilizes the XMRec dataset, a comprehensive collection of cross-
market user-item interaction data. The real-world e-commerce sce-
narios provided by this dataset serve as a robust basis for assessing
our system’s effectiveness.
We measure the effectiveness of our model using Hit Rate (HR)
and Normalized Discounted Cumulative Gain (NDCG), with a spe-
cific focus on the top-10 recommendations. HR directly measures
whether the actual items of interest to users are captured within
the top-N recommendations. Formally, HR is defined as:
𝐻𝑅 = 1 |𝑈| ∑︁ 𝑢∈𝑈 𝛿(𝑝𝑢≤𝑡𝑜𝑝𝑁) (4)
where𝛿 is the indicator function,𝑝𝑢 denotes the rank position
of the test item for user𝑢, and𝑈 represents the user base.
NDCG emphasizes the importance of the ranking order in the
recommendation list by assigning more value to highly placed
recommendations. This approach ensures that recommendations
appearing earlier, and thus more likely to be seen by users, are
given priority in the evaluation. Such a metric becomes crucial in
scenarios where the position of a recommendation is as important
as its presence. NDCG is defined as:
𝑁𝐷𝐶𝐺 = 1 |𝑈| ∑︁ 𝑢∈𝑈 log2(1+𝛿(𝑝𝑢)) log2(𝑝𝑢+ 1) (5)
These metrics, HR and NDCG, serve as the cornerstone of our
evaluation, providing a dual-lens view of our model’s ability to
predict preferences accurately and rank them in a manner that
aligns with user expectations and behaviors. Through these met-
rics, we aim to present a comprehensive analysis of our model’s
performance on the XMRec dataset, thereby substantiating the
effectiveness of our CMR approach.
4.3 Baselines
To establish the comparative efficacy of our proposed Graph Iso-
morphism Network (GIN) for CMRs, we compare its performance
with several well-established baselines. These models, recognized
for their proficiency in conventional single-market recommenda-
tion tasks, serve as a benchmark to highlight the advancements
our GIN model brings to the cross-market domain. The baselines
included in our evaluation are:
• GMF++ [10]: An enhanced version of the Generalized Matrix
Factorization (GMF) model, GMF++ extends the traditional
matrix factorization approach by integrating a linear kernel
to capture latent features. This model excels in distilling user-
item interactions into a latent space where recommendations
are derived from the linear interactions of these features.
• MLP [10]: Using a nonlinear kernel, the Multilayer Percep-
tron (MLP) delves into the complexity of user-item interac-
tion data. It employs a deep architecture to model intricate
and high-level feature interactions, which are not directly
observable through linear methods alone. This allows MLP
to capture the slight patterns of user preferences and item
attributes.
• NMF [10]: The Neural Matrix Factorization (NMF) model
is a hybrid approach that combines the strengths of GMF
and MLP. It takes advantage of both the linearity of GMF
and the nonlinearity of MLP to uncover a rich hierarchy of
features and interactions. With this comprehensive model for
recommendation systems, NMF offers a powerful solution
that can provide valuable insights.
• ItemCF [22]: ItemCf algorithm recommends items to users
based on their past interests. It does this by finding items
that are similar to ones that the user has previously shown
interest in. The goal is to provide more personalized recom-
mendations that reflect the user’s own interests.
• UserCF [33]: UserCF algorithm recommends items based on
the interests of other users who share similar preferences. It
focuses on groups with similar interests and recommends
popular items within those groups. This approach results in
more social recommendations that reflect the popularity of
items among users with similar interests.
4.4 Hyperparameter Configuration
In our search for a fair and strict comparison, we carefully optimized
the hyperparameters of our GIN based recommendation system.
This optimization is crucial to ensure that our model operates at
its full potential when addressing the unique challenges posed by
CMR tasks.
The model’s parameters were initialized from a Gaussian dis-
tributionN( 0, 0.12), setting the stage for a diverse exploration
of the solution space during the training process. We employed
the Adam optimizer, celebrated for its adaptive learning rate capa-
bilities, which is particularly beneficial given cross-market data’s
diverse and sparse nature. The learning rate was set to a value of
0.01, chosen to balance convergence speed and stability.
The batch size, a critical parameter influencing the gradient
estimation, was set to 1024, providing a representative sample of
user-item interactions while maintaining computational efficiency.
Regularization is critical to preventing overfitting, particularly in
models with a high capacity such as ours; thus, we applied a weight
decay, denoted by𝜆2, of 1× 10−7.
The GIN model’s capacity to encode user and item features into
a latent space was determined by the latent dimension size, set at 8.
To ensure that our model learns to differentiate between positive

ICMLT 2024, May 24–26, 2024, Oslo, Norway S. Ozturk et al.
and negative interactions, we specified the number of negative
samples per positive interaction as 4.
The model’s architecture includes user and item embeddings,
which remain flexible to adjust various configurations, and we allow
for the possibility of pre-trained embeddings to be incorporated
through the embedding_user and embedding_item settings. We
also enable the saving of the trained model via the save_trained
parameter, facilitating the utilization of the model without retrain-
ing.
The count of users and items, which limits the size of the em-
bedding matrices, was dynamically set based on the highest index
values observed in the data, ensuring that our model’s capacity
aligns with the dataset’s scope.
Through these carefully tuned hyperparameters, our model is
poised to learn from the intricate patterns of cross-market interac-
tions and generalize these learnings to new, unseen market data,
pushing the boundaries of what is possible in CMRs.
The model is trained over a series of epochs, with the best model
state saved based on the validation performance, specifically moni-
toring the Normalized Discounted Cumulative Gain (NDCG@10)
and Recall@10. These metrics guide the training process and facili-
tate early stopping to prevent overfitting.
4.5 Results and Discussion
Table 3: Comparative Performance Analysis of Recommen-
dation Algorithms on Cross-Market Datasets Highlighting
Top Achievers in NDCG@10 and HR@10 Metrics
Method t1 t2
NDCG@10 HR@10 NDCG@10 HR@10
GMF++ 0.3343 0.5190 0.3397 0.4574
MLP 0.3245 0.5113 0.3309 0.5222
NMF 0.5456 0.6078 0.4898 0.5932
ItemCF 0.4838 0.5622 0.4132 0.5056
UserCF 0.5267 0.5897 0.4472 0.5643
CrossGR 0.6524 0.7609 0.6113 0.7206
In the process of evaluating various recommendation algorithms
across different market datasets, our study focused on two key
performance metrics: NDCG@10 and HR@10. These metrics were
selected for their ability to effectively measure the accuracy and
relevance of the recommendations, as well as the models’ capacity
to prioritize the most relevant items for each user. We evaluated
the performance of several algorithms, including GMF++, MLP,
NMF, ItemCF, UserCF, and our proposed method, CrossGR, over
two distinct evaluation periods, t1 and t2, to measure both their
immediate efficacy and their stability over time. Table 3 illustrates
the performance of these models.
From the results (Table 3), CrossGR emerges as the superior
model, achieving the highest scores in both NDCG@10 and HR@10
across both evaluation periods. Specifically, in the t1 market,
CrossGR recorded an NDCG@10 of 0.6524 and an HR@10 of 0.7609.
Its performance in the t2 market, with an NDCG@10 of 0.6113 and
an HR@10 of 0.7206, underscores its consistency and reliability
over time, surpassing the other models evaluated. Comparatively,
traditional models like GMF++, MLP, NMF and even collabora-
tive filtering methods such as ItemCF and UserCF, displayed lower
performance metrics. For instance, NMF, the closest competitor,
achieved an NDCG@10 of 0.5456 and an HR@10 of 0.6078 dur-
ing t1, and an NDCG@10 of 0.4898 and an HR@10 of 0.5932 in t2,
significantly trailing behind CrossGR.
Our proposed method, CrossGR, utilizes a Graph Isomorphism
Network model that incorporates a novel approach to encoding
user and item features into a high-dimensional latent space. This
approach is crucial for capturing the complex and non-linear rela-
tionships inherent in user-item interactions, particularly in cross-
market scenarios where user preferences and item characteristics
may vary significantly across datasets.
We conducted hyperparameter optimization to fine-tune the GIN
model, providing it operates optimally under the unique constraints
of cross-market recommendations. The model’s parameters were
initialized from a Gaussian distribution, with the Adam optimizer
selected for its adaptive learning rate properties. This was particu-
larly useful for managing the sparse and diverse data encountered
in cross-market recommendation systems.
The GIN model’s architecture is designed to capture the intricate
patterns of user-item interactions. By employing a Multi-Layer Per-
ceptron (MLP) to predict interaction scores, the model can leverage
deep learning to enhance the accuracy of its recommendations.
Binary cross-entropy serves as the loss function, guiding the model
towards more precise predictions. We also implemented regulariza-
tion techniques, such as weight decay and dropout, to mitigate the
risk of overfitting, ensuring that the model remains generalizable
and robust across different datasets.
The evaluation methodology was designed to reflect real-world
e-commerce scenarios accurately. We utilized the XMRec dataset,
renowned for its comprehensive cross-market user-item interac-
tion data. The use of NDCG@10 and HR@10 metrics provided a
comprehensive view of each model’s performance, evaluating not
only the accuracy of the recommendations but also their ranking
in alignment with user preferences.
CrossGR was benchmarked against several well-established mod-
els to highlight its relative performance advantages. This compara-
tive analysis underscores the significant improvements our model
introduces, particularly in the context of cross-market recommen-
dations, where traditional models often struggle to account for the
variability and diversity of user preferences and item attributes
across different markets.
5 CONCLUSIONS
In this work, we have presented a novel approach to CMRs by
employing Graph Isomorphism Networks (GINs), which have
demonstrated capability in capturing complex user-item interac-
tion patterns within diverse market scenarios. Our approach, called
CrossGR, has shown significant improvement over traditional rec-
ommendation systems in terms of NDCG@10 and HR@10 metrics.
CrossGR is adaptable and accurate, which makes it a potential tool
for improving user engagement and satisfaction across different
market segments. Our research suggests that GINs can effectively
handle the complexities of cross-market data, and provide a scalable

Enhancing Cross-Market Recommendation System with Graph Isomorphism Networks: A Novel Approach to Personalized User Experience ICMLT 2024, May 24–26, 2024, Oslo, Norway
solution for personalized recommendation services in a globally
interconnected marketplace.
In future work, we intend to explore the integration of heteroge-
neous market data within cross-market recommendation systems.
By investigating the interplay between different market dynam-
ics, we plan to generate insights that will refine our approach to
recommendation systems.
REFERENCES
[1] 2023. WSDM Cup on Cross-Market Recommendation Competition Dataset . Re-
trieved October 01, 2023 from https://xmrec.github.io/wsdmcup/
[2] Xiaomei Bai, Mengyang Wang, Ivan Lee, Zhuo Yang, Xiangjie Kong, and Feng
Xia. 2019. Scientific Paper Recommendation: A Survey. IEEE Access 7 (2019),
9324–9339. https://doi.org/10.1109/access.2018.2890388
[3] H. Bonab, M. Aliannejadi, A. Vardasbi, E. Kanoulas, and J. Allan. 2021. Cross-
market product recommendation. Proceedings of the 30th ACM International
Conference on Information &Amp; Knowledge Management (2021). https://doi.
org/10.1145/3459637.3482493
[4] Zeyuan Chen, He Wang, Xiangyu Zhu, Haiyan Wu, Congcong Gu, Shumeng Liu,
Jinchao Huang, and Wei Zhang. 2022. A Practical Two-stage Ranking Framework
for Cross-market Recommendation. https://doi.org/10.48550/ARXIV.2204.12682
[5] Wenqi Fan, Yao Ma, Qing Li, Yuan He, Eric Zhao, Jiliang Tang, and Dawei Yin.
2019. Graph Neural Networks for Social Recommendation. https://doi.org/10.
48550/ARXIV.1902.07243
[6] Benjamin Fischer, Ethan Brown, Maria Perez, and Andrew Sanchez. 2023. En-
hanced Collaborative Filtering Recommendation Model for Graph Neural Net-
works Based on Meta-Paths. (March 2023). https://doi.org/10.21203/rs.3.rs-
2744708/v1
[7] Y. Gao, Y. Li, Y. Lin, H. Gao, and L. Khan. 2020. Deep learning on knowledge
graph for recommender system: a survey. (2020). https://doi.org/10.48550/arxiv.
2004.00387
[8] Xiangnan He, Kuan Deng, Xiang Wang, Yan Li, Yongdong Zhang, and Meng
Wang. 2020. LightGCN: Simplifying and Powering Graph Convolution Network
for Recommendation. CoRR abs/2002.02126 (2020). arXiv:2002.02126 https:
//arxiv.org/abs/2002.02126
[9] Xiangnan He, Lizi Liao, Hanwang Zhang, Liqiang Nie, Xia Hu, and Tat-Seng Chua.
2017. Neural Collaborative Filtering. https://doi.org/10.48550/ARXIV.1708.05031
[10] Xiangnan He, Lizi Liao, Hanwang Zhang, Liqiang Nie, Xia Hu, and Tat-Seng Chua.
2017. Neural Collaborative Filtering. https://doi.org/10.48550/ARXIV.1708.05031
[11] Jonathan L. Herlocker, Joseph A. Konstan, Loren G. Terveen, and John T. Riedl.
2004. Evaluating collaborative filtering recommender systems. ACM Transactions
on Information Systems 22, 1 (Jan. 2004), 5–53. https://doi.org/10.1145/963770.
963772
[12] Zheng Hu, Satoshi Nakagawa, Shi-Min Cai, and Fuji Ren. 2023. Bert4XMR:
Cross-Market Recommendation with Bidirectional Encoder Representations from
Transformer. https://doi.org/10.48550/ARXIV.2305.15145
[13] Guolin Ke, Qi Meng, Thomas Finley, Taifeng Wang, Wei Chen, Weidong Ma,
Qiwei Ye, and Tie-Yan Liu. 2017. LightGBM: A Highly Efficient Gradient Boosting
Decision Tree. In Advances in Neural Information Processing Systems , I. Guyon,
U. Von Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett
(Eds.), Vol. 30. Curran Associates, Inc. https://proceedings.neurips.cc/paper_
files/paper/2017/file/6449f44a102fde848669bdd9eb6b76fa-Paper.pdf
[14] M. M. Khan, R. Ibrahim, and I. Ghani. 2017. Cross domain recommender systems.
Comput. Surveys 50 (2017), 1–34. Issue 3. https://doi.org/10.1145/3073565
[15] Yehuda Koren, Robert Bell, and Chris Volinsky. 2009. Matrix factorization tech-
niques for recommender systems. Computer 42, 8 (2009), 30–37.
[16] W. Li, M. He, Z. Huang, X. Wang, S. Feng, W. Su, and Y. Sun. 2021. Graph4rec: a
universal toolkit with graph neural networks for recommender systems. (2021).
https://doi.org/10.48550/arxiv.2112.01035
[17] Tendai Mukande. 2022. Heterogeneous Graph Representation Learning for multi-
target Cross-Domain Recommendation. InProceedings of the 16th ACM Conference
on Recommender Systems. ACM. https://doi.org/10.1145/3523227.3547426
[18] Marlowe Norton, Arwen Kingsley, Asher Wellington, and Juniper Prescott. 2023.
HGNNDR: Heterogeneous Graph Neural Network Recommendation Model based
on Feature Aggregation. (July 2023). https://doi.org/10.21203/rs.3.rs-3201618/v1
[19] Michael J. Pazzani and Daniel Billsus. [n.d.]. Content-Based Recommendation
Systems. Springer Berlin Heidelberg, 325–341. https://doi.org/10.1007/978-3-
540-72079-9_10
[20] B. Perozzi, R. Al-Rfou, and S. Skiena. 2014. Deepwalk: online learning of social
representations. (2014). https://doi.org/10.48550/arxiv.1403.6652
[21] L. Ruiz, F. Gama, A. G. Marques, and A. Ribeiro. 2020. Invariance-preserving
localized activation functions for graph neural networks. IEEE Transactions on
Signal Processing 68 (2020), 127–141. https://doi.org/10.1109/tsp.2019.2955832
[22] Badrul Sarwar, George Karypis, Joseph Konstan, and John Riedl. 2001. Item-based
collaborative filtering recommendation algorithms. In Proceedings of the 10th
international conference on World Wide Web (WWW01) . ACM. https://doi.org/10.
1145/371920.372071
[23] Shanghang Song, Bing Kong, and Lihua Zhou. 2023. Graph factorization machine
based recommendation algorithm with graph construction and attention mecha-
nism. In Eighth International Symposium on Advances in Electrical, Electronics,
and Computer Engineering (ISAEECE 2023) , Pavel Loskot and Shubin Yan (Eds.).
SPIE. https://doi.org/10.1117/12.2680552
[24] Petar Veličković, Guillem Cucurull, Arantxa Casanova, Adriana Romero, Pietro
Liò, and Yoshua Bengio. 2017. Graph Attention Networks. https://doi.org/10.
48550/ARXIV.1710.10903
[25] Xiao Wang, Houye Ji, Chuan Shi, Bai Wang, Yanfang Ye, Peng Cui, and Philip S
Yu. 2019. Heterogeneous Graph Attention Network. In The World Wide Web
Conference. ACM. https://doi.org/10.1145/3308558.3313562
[26] Shu Wu, Yuyuan Tang, Yanqiao Zhu, Liang Wang, Xing Xie, and Tieniu Tan.
2018. Session-based Recommendation with Graph Neural Networks. (2018).
https://doi.org/10.48550/ARXIV.1811.00855
[27] Z. Wu, S. Pan, F. Chen, G. Long, C. Zhang, and P. S. Yu. 2021. A comprehensive
survey on graph neural networks. IEEE Transactions on Neural Networks and
Learning Systems 32 (2021), 4–24. Issue 1. https://doi.org/10.1109/tnnls.2020.
2978386
[28] Chunfu Xie. 2023. Commodity knowledge graph-based TransD-KGAT method
for recommendation. In Fifth International Conference on Computer Information
Science and Artificial Intelligence (CISAI 2022) , Yuanchang Zhong (Ed.). SPIE.
https://doi.org/10.1117/12.2667700
[29] Keyulu Xu, Weihua Hu, Jure Leskovec, and Stefanie Jegelka. 2018. How Powerful
are Graph Neural Networks? https://doi.org/10.48550/ARXIV.1810.00826
[30] R. Ying, R. He, K. Chen, P. Eksombatchai, W. L. Hamilton, and J. Leskovec. 2018.
Graph convolutional neural networks for web-scale recommender systems. (2018).
https://doi.org/10.48550/arxiv.1806.01973
[31] Yonghong Yu, Xuewen Chen, Li Zhang, Rong Gao, and Haiyan Gao. 2022. Neural
Graph for Personalized Tag Recommendation. IEEE Intelligent Systems 37, 1 (Jan.
2022), 51–59. https://doi.org/10.1109/mis.2020.3040046
[32] Y. Yu, W. Qian, L. Zhang, and R. Gao. 2022. A graph-neural-network-based social
network recommendation algorithm using high-order neighbor information.
Sensors 22 (2022), 7122. Issue 19. https://doi.org/10.3390/s22197122
[33] Ruisheng Zhang, Qi-dong Liu, Chun-Gui, Jia-Xuan Wei, and Huiyi-Ma. 2014.
Collaborative Filtering for Recommender Systems. In 2014 Second International
Conference on Advanced Cloud and Big Data . 301–308. https://doi.org/10.1109/
CBD.2014.47
[34] Shuai Zhang, Lina Yao, Aixin Sun, and Yi Tay. 2019. Deep learning based recom-
mender system: A survey and new perspectives. ACM computing surveys (CSUR)
52, 1 (2019), 1–38.
[35] Xinping Zhao and Yingchun Yang. 2022. SGLCMR: Self-supervised Graph
Learning of Generalized Representations for Cross-Market Recommendation. In
2022 International Joint Conference on Neural Networks (IJCNN) . IEEE. https:
//doi.org/10.1109/ijcnn55064.2022.9892928
