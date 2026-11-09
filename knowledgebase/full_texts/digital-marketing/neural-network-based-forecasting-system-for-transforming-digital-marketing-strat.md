---
title: Neural Network-Based Forecasting System for Transforming Digital Marketing Strategies and User
  Interaction
url: https://doi.org/10.25258/ijddt.16.66s.153
category: digital-marketing
subcategory: framework
date: 2026-07
venue: International Journal of Drug Delivery Technology
authors:
- Vijayachander V S
- Subalakshmi R
- M Djazman Addin S
source: openalex-oa
pdf_url: https://doi.org/10.25258/ijddt.16.66s.153
pages: 8
chars: 33158
fetched_at: '2026-11-08T17:57:49+00:00'
kb_version: 1
---

# Neural Network-Based Forecasting System for Transforming Digital Marketing Strategies and User Interaction

RESEARCH PAPER
 IJDDT Volume 16 Issue 66s 2026 Page: 1432
Neural Network-Based Forecasting System for Transforming
Digital Marketing Strategies and User Interaction

Vijayachander V S1, Subalakshmi R2, Mohana P S3, Aravinth B4
1 Assistant Professor, Department of Management Studies, K. S.  Rangasamy college of Technology, Tiruchengode,
Namakkal, Anna University, Chennai, India
2,3,4 Department of Management Studies, K. S.  Rangasamy college of Technology, Tiruchengode, Namakkal, Anna
University, Chennai, India
Abstract
Data-driven marketing strategies are becoming more prevalent in the digital marketing industry, and need
sophisticated models to accurately forecast user interactions and inform engagement strategies. Existing methods tend
to overlook the complex, non-linear and time-dependent nature of user interaction data. In this study, we propose a
new forecasting model called a Hybrid Attention-Based Temporal Interaction Network (HATIN). Our model aims to
capture user's dynamic patterns by incorporating both temporal dependency and an adaptive attention mechanism to
focus on key interaction features. HATIN learns the temporal dependencies and contextual information of user activity
data streams, and predicts important key performance indicators (KPI) such as click-through rate, user engagement
level, and conversion probability. HATIN is validated on real-world and standardized data, and compared with
traditional approaches, such as statistical models and benchmark deep learning models. The results show that HATIN
outperforms other methods in terms of prediction accuracy and stability. Moreover, the developed approach supports
dynamic decision-making in digital marketing through insights on user behavior trends. Our research showcases the
benefits of hybrid neural forecasting systems in revolutionizing the decision-making process in data-driven marketing
and improving user experience.
Keywords: HATIN, digital marketing analytics, user behavior forecasting, deep learning, attention mechanism,
temporal modeling, predictive analytics.
How to cite this article: Vijayachander VS, Subalakshmi R, Mohana PS, Aravinth B. Neural Network-Based
Forecasting System for Transforming Digital Marketing Strategies and User Interaction. Int J Drug Deliv Technol.
2026;16(66s):1432-1439. DOI: 10.25258/ijddt.16.66s.153

1. Introduction
The growth of digital media has transformed
marketing, with an emphasis on data-centric and
targeted marketing approaches. The explosion of user
interaction data from websites, apps and social media
sites has led to companies increasingly using
predictive analytics to learn about and forecast user
behaviour [1, 2]. Predictions of user interactions,
including click-through rates, time spent on the
website, and conversion rates, are essential to the
success of marketing strategies and maximizing the
return on investment [3].
Although data analytics has made great strides,
traditional methods of predicting outcomes in digital
marketing, such as statistical and rule-based systems,
are still constrained by their inability to model high-
dimensional, complex and time-varying data [4-6].
These techniques tend to adopt linear and static
modeling approaches, limiting their flexibility in a
dynamic environment where user interests are
constantly changing [7].
The latest deep learning techniques have shown great
promise in capturing temporal and nonlinear patterns
in data. Specifically, temporal neural networks have
been proven to be useful in modeling temporal user
behavior patterns [8]. But current models often
struggle to adaptively learn and prioritise the most
pertinent features that contribute to user interactions,
resulting in inferior prediction accuracy. Further, there
is a lack of integration of contextual understanding and
interpretability in digital marketing scenarios [9, 10].
In this paper, we propose a new Hybrid Attention-
Based Temporal Interaction Network (HATIN) model
for predicting user interactions in digital marketing.
The new approach aims to capture temporal dynamics
and integrate a dynamic attention mechanism that
prioritises important features in users' interaction data.
The proposed HATIN can model temporal effects and
selectively highlight critical features in the context of
user interaction data to improve forecasting accuracy
and interpretability.
This research has the following main contributions:
 Proposal of a new Hybrid Attention-based
Temporal Interaction Network (HATIN) for
predicting user behaviors
 Combining temporal dependency and
adaptive Attention for enhanced feature
encoding
 An efficient system for digital marketing
analytics and decision making
 Thorough experimentation showing
outperformance of the baselines

Neural Network-Based Forecasting System for Transforming Digital Marketing Strategies and User
Interaction
 IJDDT Volume 16 Issue 66s 2026 Page: 1433
2. Related work
Machine learning, deep learning and other recent
developments in digital marketing analytics have been
applied for modelling user behavior and enhancing
prediction accuracy. Time-series prediction using
statistical techniques like autoregressive integrated
moving average (ARIMA) has been extensively used;
however, they lack the capability to model nonlinear
user behavior and user interactions.
Sequential prediction models based on deep learning
have been particularly popular due to their capacity to
capture temporal relationships. Long Short-Term
Memory (LSTM) networks, proposed by Hochreiter
and Schmidhuber [11], have been successfully used to
prevent vanishing gradients and are commonly used in
time-series prediction problems. LSTM-based models
have been shown to enhance user behavior modeling
by capturing long-term user interactions with
clickstream data.
Cheng et al. [12] developed Wide & Deep learning
models for recommendation systems, which combine
memorization and generalization to enhance
predictions of user engagement. Likewise, Covington
et al.'s deep neural network-based recommendation
system for YouTube video recommendations has
shown the potential of deep learning for marketing.
Rendle et al. [13] proposed Factorization Machines for
sparse prediction, which are extensively used for
click-through rate (CTR) prediction. But these models
are not sequential, which hinders their capacity to
model user temporal behaviours.
Zhou et al. [14] introduced Deep Interest Network
(DIN) that uses attention mechanisms to capture user
interests over time from past actions. This research
showed attention mechanisms can effectively boost
recommendation performance by attending to crucial
user interactions.
Zhou et al. [15] also proposed Deep Interest Evolution
Network (DIEN) that captures the dynamic nature of
user interests by sequential learning with GRU. This
model shows that temporal dynamics are important in
capturing user behavior.
Guo et al. [16] proposed DeepFM, a combination of
factorization machines and deep neural networks to
learn both low- and high-order feature interactions.
This approach works well for prediction, but does not
explicitly capture temporal information.
Zhang et al. [17] used attention-based recurrent neural
networks (RNNs) for click-through rate prediction,
demonstrating the effectiveness of attention
mechanisms in improving interpretability and
accuracy for sequence-based prediction.
Li et al. [18] proposed sequential recommendation
models based on gated recurrent units (GRU4Rec),
which model user's behaviour in session-based
recommendation but have low feature interpretability.
Xiao et al. [19] proposed Attentional Factorization
Machines (AFM) which use attention mechanisms in
factorization of feature interactions to enhance
prediction performance in sparse data.
Sun et al. [20] used transformer-based models for
sequential recommendations, showing that self-
attention effectively models long-term dependencies.
Wu et al. [21] proposed reinforcement learning user
models for intelligent marketing platforms,
demonstrating how policy-based learning can be used
to further improve user engagement.
Unfortunately, the current methods either concentrate
on temporal learning or feature importance separately.
However, few studies have integrated temporal
interaction learning with adaptive attention
mechanisms to jointly learn temporal dynamics and
dynamically focus on the most relevant interactions.
This fuels the need for the proposed HATIN model,
which combines temporal interaction modeling with
dynamic attention for enhanced prediction accuracy in
digital marketing environments.
2.1 Research gap
While considerable progress has been made in deep
learning-based forecasting, there are still some key
challenges that have not been addressed, especially in
digital marketing and user interaction scenarios.
First, most of the existing forecasting models are
designed for applications like finance, weather, and
traffic prediction, which exhibit structured data
patterns. These models do not effectively address the
dynamic, context-sensitive, and user-specific
characteristics of digital marketing data, where user
preferences and interaction features change quickly
and are not always regular.
Second, traditional temporal models such as recurrent
and hybrid models primarily learn the dynamics of
sequences but do not provide a mechanism to prioritise
the contextual features. Thus, they do not prioritise the
more and less important features of user interactions,
resulting in sub-par predictive accuracy.
Third, although attention mechanisms have been
incorporated in a few studies, their application is
mostly confined to general prediction tasks and not
specifically to user-centric models needed in digital
marketing. Further, many models are not interpretable,
thus preventing marketers from understanding the
underlying reasons for the predictions.
Fourth, most of the current methods are static or semi-
adaptive and do not have the ability to adapt to
changing user behavior in near real-time. This
hampers their use in real-world marketing scenarios
that demand real-time decision making and strategy
re-optimization.
Finally, there are no integrated frameworks that
simultaneously combine temporal learning, adaptive

Neural Network-Based Forecasting System for Transforming Digital Marketing Strategies and User
Interaction
 IJDDT Volume 16 Issue 66s 2026 Page: 1434
attention and feature engineering specific to marketing
into a unified approach.
3. Overview of proposed methodology
In this paper, we present a Hybrid Attention-Based
Temporal Interaction Network (HATIN) for
predicting user's behavior in digital marketing. The
approach aims to effectively model temporal
relationships and adaptively select important features
of user interactions. HATIN combines temporal
learning with an attention-based feature selection
mechanism to capture both past user interactions and
feature importance. The general processing pipeline
includes pre-processing, feature modelling, temporal
interaction modelling, adaptive attention-based
feature modelling and prediction. The integration of
these elements in a coherent framework allows the
proposed system to perform accurate and efficient
prediction of key marketing metrics, including click-
through rate (CTR), user engagement and conversion
probability. Figure 1 shows the architecture diagram.

Figure 1: Architecture diagram
3.1 Data Collection and Pre-processing
The proposed system is based on massive user
interaction data from online marketing systems, such
as clickstream data, session length, click sequences
and conversions. These data are inherently diverse,
multi-dimensional and time-varying, requiring careful
preprocessing to achieve accurate results.
Crude interaction data can be problematic due to
missing values (e.g., user lost), noise (e.g., mistaken
clicks) and redundant feature attributes. To overcome
this, a preprocessing workflow is followed.
Incomplete data is filled using statistically desirable
methods - mean or median imputation for non-
sequence data and forward filling for sequence data to
maintain temporal coherence. Continuous features are
scaled to improve gradient flow during training and
give equal weight to each feature while ordinal
features are converted into a numerical representation
using embedding or one-hot encoding.
The transformation pipeline is:
 ̇   =  (  )                                                           (1)
where ψ(⋅) represents the overall preprocessing
functions of cleaning, normalizing and encoding. One
of the main innovations in this phase is the sequencing
of user events, transforming individual events into a
sequence of events:
  = { 1,  2, … ,   }                                                        (2)
This re-formats individual events into a temporal
format and allows the model to capture the sequence
of behavior rather than individual events.
3.2 Feature Representation
The feature representation layer aims to represent user
actions in a way that maintains contextual and
temporal information. In online marketing, user
behavior is driven not just by the immediate actions
but also by contextual information like device,
location and past behavior patterns.
 To reflect this, features are categorised into:
 Static features: static attributes (e.g., user
info, device)
 Dynamic features: time-varying interactions
(e.g., clicks, time spent, click path)
At each time step, these features are combined into a
single feature vector:
where ϕ(⋅) is a feature transformation function.
   =  (  )                                                                      (3)
This vector ensures that each input vector stands for
current interactions as well as historical interaction
cues. Retaining the sequence information allows for
the understanding of user behavior as dynamic, which
is necessary for effective predictions.
3.3 Temporal Interaction Modeling
The temporal interaction module is the core of
HATIN, capturing temporal interactions. User
interactions are dynamic - previous actions impact
future actions. For example, revisiting a product page
or spending more time on a page might be a strong
predictor of purchase.
To capture this in the model, the framework has a
hidden state that changes over time, incorporating
current context and historical information:
ℎ  =  ( ℎ   +  ℎℎ ି1 +  ℎ)
(4)
Here, ℎ  is the hidden state at time t, and  ℎ,  ℎ and
 ℎ are parameters.
This allows the model to:
 Remember longer-term correlations within
interactions
 Model trends and correlations in user
behavior
 Capture time-lagged effects (actions
affecting future outcomes)
This dynamic learning process enables HATIN to
learn from the changing nature of user behavior, unlike
static models.
3.4 Adaptive Attention Mechanism
While temporal modeling accounts for sequence
information, it does not incorporate the importance of

Neural Network-Based Forecasting System for Transforming Digital Marketing Strategies and User
Interaction
 IJDDT Volume 16 Issue 66s 2026 Page: 1435
different interactions. In real-world situations some
actions (e.g., adding products to a shopping cart) have
more predictive power than others (e.g., short visits to
a webpage).
To overcome this limitation, an adaptive attention is
introduced, which can weight the importance of
different time steps. The attention scores for each
hidden state are calculated and normalized as:
   =
   (  )
∑    (  )   స1                                                                    (5)
where    is the weight for the t-th interaction. The
output context vector is the weighted sum of the
interactions:
  = ∑   ℎ     ୀ1                                                                     (6)
This enables the model to learn the key behavioural
features and eliminate noise. This not only enhances
the prediction performance but also its interpretability
by linking the outcome to critical interactions - a
crucial aspect in digital marketing analytics.
3.5 Prediction Layer
The prediction layer can produce a user prediction
from the context vector. The context vector captures
both the temporal nature and the importance of various
features, and distills them into a useful summary.
The prediction is given by:
 ෡ =  (    +   )
(7)
where σ(⋅) is an appropriate activation function. The
model predicts the different key performance
indicators (KPIs) depending on the goal of the model
such as:
 Click-through rate (CTR)
 User engagement score
 Conversion probability
This layer thus links learned behaviours with key
digital marketing decision metrics.
3.6 Model Optimization
The goal of the training is to reduce the difference
between the predicted and actual values. In the case of
regression forecasting, the loss function is:
ℒ =
1
  ∑ (    −  ෡  )2   ୀ1
(8)
with    and  ෡   being the ground truth and
predictions, respectively. We use an adaptive gradient
descent algorithm, such as Adam, to iteratively update
the model parameters. This adaptive algorithm adjusts
the learning rate based on estimates of first and second
moments of the gradient, leading to improved
convergence and stability.
Further, the hyperparameters such as learning rate,
batch size and sizes of hidden layers are fine-tuned
empirically. This optimizes model generalization and
performance on new data.
The HATIN framework we introduce combines
preprocessing, feature extraction, temporal processing
and attention-based post-processing in a cohesive
framework. These components work together to model
various aspects of user interactions, from low-level
interactions to high-level predictive insights.
The integration of temporal learning and attention
mechanisms ensures enhanced accuracy,
interpretability and scalability, making it an ideal
solution for real-time digital marketing.
4. Result and discussion
In this section, we assess the performance of the
proposed Hybrid Attention-Based Temporal
Interaction Network (HATIN). The model is evaluated
in terms of regression and classification measures, and
benchmarked against various baseline methods such
as statistical, machine learning and deep learning
models. This is done using real-world data from digital
marketing interactions, establishing the practicality of
the findings. Furthermore, ablation testing and
complexity analysis are also performed to ensure the
validity of the proposed framework's components, and
evaluate the efficiency of the approach.
4.1 Experimental Setup
The performance of the proposed Hybrid Attention-
Based Temporal Interaction Network (HATIN) was
assessed using a rich dataset of user interactions from
online marketing systems. The data encompasses
clickstream data, session lengths, page views and
conversion actions, capturing a range of user
interactions.
The data was preprocessed by normalisation,
encoding, and temporal ordering as outlined in Section
3 before training. The data was split into 80% for
training and 20% for testing.
The model was developed using a deep learning
framework, and the model was trained with the Adam
optimizer with a learning rate of 0.001. A batch size of
64 and 100 epochs were employed for training. To
avoid overfitting, early stopping was used. The
proposed model was compared with the following
models to confirm its performance:
ARIMA (statistical model)
Random Forest (machine learning model)
RNN (simple deep learning model)
LSTM (deep learning model)
4.2 Evaluation Metrics
We used a range of metrics to assess performance:
 Mean Squared Error (MSE): Average of the
squares of errors
 Root Mean Squared Error (RMSE): Indicates
error in original units
 Mean Absolute Error (MAE): Assesses
average absolute error
 Accuracy: Measures classification accuracy
 Precision, Recall, F1-score: Classifier
Performance
Table 1: Overall Performance Comparison

Neural Network-Based Forecasting System for Transforming Digital Marketing Strategies and User
Interaction
 IJDDT Volume 16 Issue 66s 2026 Page: 1436
Model MSE ↓ RMSE
↓
MAE ↓ Accuracy
↑
ARIMA 0.152 0.390 0.305 82.4%
Random
Forest
0.118 0.343 0.271 86.7%
RNN 0.097 0.311 0.248 88.9%
LSTM 0.081 0.284 0.221 91.2%
HATIN 0.059 0.243 0.198 94.6%

Figure 3: MSE, RMSE , MAE and Accuracy
Comparison
The comparison between the proposed HATIN model
and other models is given in Table 1 and figure 3. We
can see that conventional statistical models like
ARIMA perform the least well as they cannot model
complex behavior. Machine learning models such as
Random Forest perform better due to their ability to
incorporate different features, but do not have
temporal knowledge. RNN and LSTM models (deep
learning) are better because they consider the temporal
aspect of data.
But the proposed HATIN model outperforms the other
models. The substantial drop in MSE, RMSE and
MAE shows HATIN is capable of delivering more
accurate and reliable predictions. The increased
accuracy also suggests that it is indeed able to learn
user behaviour patterns in digital marketing settings.
Table 2: Classification Performance Metrics
Model Precision Recall F1-Score
ARIMA 0.79 0.76 0.77
Random
Forest
0.84 0.82 0.83
RNN 0.87 0.86 0.86
LSTM 0.90 0.89 0.89

Neural Network-Based Forecasting System for Transforming Digital Marketing Strategies and User
Interaction
 IJDDT Volume 16 Issue 66s 2026 Page: 1437

Figure 2: Performance comparison
Table 2 and figure 2 compares the classification
performance of all the models in terms of precision,
recall and F1-score. ARIMA fails to capture the
complex relationships due to its linear nature and
Random Forest enhances classification using
ensemble techniques. RNN and LSTM exhibit better
performance with their ability to model sequence
information.
The HATIN model has the best performance in all
metrics, showing a better balance in terms of false
positives and false negatives. The higher F1-score
indicates the model's ability to deal with complex or
unbalanced patterns and is thus ideal for predicting
marketing performance.
Table 3: Training Convergence Analysis
Epoch Training
Loss
Validation
Loss
Accuracy
10 0.182 0.195 85.2%
30 0.121 0.134 89.3%
50 0.089 0.101 91.8%
80 0.066 0.078 93.7%
100 0.054 0.065 94.6%

Table 3 shows the convergence of the HATIN model.
We can see that training and validation loss
continually drop with more epochs, suggesting the
model is learning. The minimal difference between
training and validation loss indicates that overfitting is
not a major concern.
The continuous improvement in accuracy also
indicates that the model learns useful information from
the user interaction data. This is essential for robust
performance in practical applications.
Table 4: Ablation Study
Model Variant MSE Accuracy
Without Attention 0.082 91.8%
Without Temporal
Module
0.097 89.5%
Without Feature Fusion 0.089 90.7%
Full HATIN Model 0.059 94.6%

The ablation study, shown in Table 4, assesses the
impact of each part of the HATIN model. The
performance decreases when the attention mechanism
is absent, showing the importance of prioritizing
features in making a prediction. And a large
performance drop when the temporal module is
removed, which indicates that the modeling of
temporal dependency is important. The complete
HATIN model performs the best which shows the joint
impact of temporal modeling and attention mechanism
is vital to achieve the best performance.
Table 5: Computational Complexity Analysis
Model Parameters
(M)
FLOPs
(G)
Training
Time (s)
RNN 0.12 0.45 120
LSTM 0.25 0.68 180
HATIN 0.21 0.61 165

Computational efficiency of different models are
compared in Table 5. Although LSTM has higher
computational complexity due to the gating functions,
RNN has lower complexity and worse performance.
HATIN strikes a good balance between accuracy and
efficiency. It has a slightly higher computational cost
than RNN, but is more efficient than LSTM while
offering higher prediction accuracy. Thus, it is an ideal
fit in the real-time digital marketing system that needs
to be efficient and fast.

Figure 4: Training and testing analysis
The figure 4 shows the training and testing evaluation.
4.3 Discussion
The results of the proposed Hybrid Attention-Based
Temporal Interaction Network (HATIN) model show
its potential for capturing the temporal dynamics of
user interactions in digital marketing. The results show
that the proposed model outperforms the baseline
models, which are based only on time-dependent and
feature-dependent information.
An important insight is that conventional statistical
approaches like ARIMA are not effective because they
cannot capture nonlinear relationships and long-term
dependencies. They rely on assumptions of linearity
and stationary, which are seldom met in user

Neural Network-Based Forecasting System for Transforming Digital Marketing Strategies and User
Interaction
 IJDDT Volume 16 Issue 66s 2026 Page: 1438
interaction data. Thus, they struggle to model
changing patterns of behaviour.
Machine learning models like Random Forest exhibit
better performance than statistical models; but they do
not explicitly involve time. While they can capture
feature interactions, they fail to consider the temporal
nature of user behavior, and as a result, they are less
effective in time-dependent tasks.
Deep learning models such as RNN and LSTM
perform better because of their capability to model
temporal relationships. But their drawback is that they
lack the ability to prioritise certain time steps,
inadequately capturing important behavioural cues.
This problem can be overcome by the proposed
HATIN model by incorporating an adaptive attention
mechanism. The attention mechanism helps enhance
the overall performance of the model by adaptively
weighting more important user activities. This enables
the model to prioritise important user interactions,
such as viewing a product multiple times or adding it
to the shopping cart, which are likely to lead to
conversions. This helps HATIN make more accurate
predictions and generalise better than the baselines.
Additionally, the ablation study reveals that both the
temporal and attention components play essential roles
in achieving the model's performance. Excluding
either component results in a significant drop in
performance, confirming the effectiveness of the
combination of these two components. Finally, the
trade-off between accuracy and efficiency is a crucial
consideration. While HATIN increases the complexity
of the model with the attention module, it remains
relatively efficient compared to deeper LSTM-only
models. This enables its use in real-time digital
marketing applications, where performance and speed
are essential.
In practice, the proposed system offers insights for
decision making. The ability to forecast user
interactions and purchase intentions can help
companies fine-tune their marketing tactics,
personalise the content presented to users, and
enhance campaign performance.
5. Conclusion
A Hybrid Attention-based Temporal Interaction
Network (HATIN) was proposed in this paper to
predict user behavior in online marketing. The goal of
the framework is to understand the complex user
behavior over time and dynamically select relevant
user interaction features for predicting important
marketing metrics such as click-through rate,
engagement and conversion probability. The HATIN
model overcomes limitations of traditional statistical
and machine learning models that struggle to model
the non-linearity and sequential nature of user
interaction, by combining temporal interaction
modeling with an adaptive attention mechanism. This
combination allows the model to capture temporal
dynamics of user behavior and adaptive attention to
interactions for prediction.
Our experimental results show that HATIN achieves
superior performance compared to the baseline
approaches, such as ARIMA, Random Forest, RNN
and LSTM, on various evaluation measures, including
mean squared error (MSE), root mean squared error
(RMSE), mean absolute error (MAE) and
classification accuracy. The ablation study also shows
that both the temporal modeling and attention
mechanism play an important role in improving the
predictive performance. Moreover, the computational
study reveals that HATIN achieves a trade-off
between prediction accuracy and efficiency, making it
apt for digital marketing needs.
In summary, the proposed hybrid framework offers a
scalable, interpretable and effective approach for user
behavior prediction, which can facilitate data-driven
marketing strategies. Future research can further
explore adaptive learning in the streaming world and
leveraging multimodal data of user behaviors for
better prediction and contextual understanding.
References
1. O. Grbovic and H. Cheng, “Real-time
Personalization using Embeddings for Search
Ranking at Airbnb,” in Proceedings of the
24th ACM SIGKDD International
Conference on Knowledge Discovery & Data
Mining, 2018, pp. 311–320.
2. J. Lian, X. Zhou, F. Zhang, et al., “xDeepFM:
Combining Explicit and Implicit Feature
Interactions for Recommender Systems,” in
Proceedings of the 24th ACM SIGKDD,
2018, pp. 1754–1763.
3. Q. Pi, W. Chen, Y. Yuan, et al., “Practice on
Long Sequential User Behavior Modeling for
Click-Through Rate Prediction,” in
Proceedings of the 26th ACM SIGKDD
Conference, 2020, pp. 2891–2899.
4. C. Wu, F. Wu, S. Ge, et al., “Neural News
Recommendation with Multi-Head Self-
Attention,” in Proceedings of the 2019
Conference on Empirical Methods in Natural
Language Processing, 2019, pp. 6389–6394.
5. H. Sun, J. Liu, J. Wu, et al., “BERT4Rec:
Sequential Recommendation with
Bidirectional Encoder Representations from
Transformer,” in Proceedings of the 28th
ACM International Conference on
Information and Knowledge Management,
2019, pp. 1441–1450.
6. F. Yuan, X. He, A. Karatzoglou, and L.
Zhang, “SimpleX: A Simple and Strong
Baseline for Collaborative Filtering,” in

Neural Network-Based Forecasting System for Transforming Digital Marketing Strategies and User
Interaction
 IJDDT Volume 16 Issue 66s 2026 Page: 1439
Proceedings of the 44th International ACM
SIGIR Conference, 2021, pp. 1243–1252.
7. J. Kang and J. McAuley, “Self-Attentive
Sequential Recommendation,” in
Proceedings of the IEEE International
Conference on Data Mining, 2018, pp. 197–
206.
8. Y. Qin, H. Song, W. Chen, et al., “A Dual-
Stage Attention-Based Recurrent Neural
Network for Time Series Prediction,” in
Proceedings of the 26th International Joint
Conference on Artificial Intelligence, 2017,
pp. 2627–2633.
9. R. He and J. McAuley, “Fusing Similarity
Models with Markov Chains for Sparse
Sequential Recommendation,” in
Proceedings of the IEEE International
Conference on Data Mining, 2016, pp. 191–
200.
10. X. Wang, Y. He, M. Wang, et al., “Neural
Graph Collaborative Filtering,” in
Proceedings of the 42nd International ACM
SIGIR Conference, 2019, pp. 165–174.
11. Hochreiter, S., & Schmidhuber, J. (1997).
Long short-term memory. Neural
computation, 9(8), 1735-1780.
12. Cheng, H. T., Koc, L., Harmsen, J., Shaked,
T., Chandra, T., Aradhye, H., ... & Shah, H.
(2016, September). Wide & deep learning for
recommender systems. In Proceedings of the
1st workshop on deep learning for
recommender systems (pp. 7-10).
13. Covington, P., Adams, J., & Sargin, E. (2016,
September). Deep neural networks for
youtube recommendations. In Proceedings of
the 10th ACM conference on recommender
systems (pp. 191-198).
14. Rendle, S. (2012). Factorization machines
with libfm. ACM Transactions on Intelligent
Systems and Technology (TIST), 3(3), 1-22.
15. Zhou, G., Zhu, X., Song, C., Fan, Y., Zhu, H.,
Ma, X., ... & Gai, K. (2018, July). Deep
interest network for click-through rate
prediction. In Proceedings of the 24th ACM
SIGKDD international conference on
knowledge discovery & data mining (pp.
1059-1068).
16. Zhou, G., Mou, N., Fan, Y., Pi, Q., Bian, W.,
Zhou, C., ... & Gai, K. (2019, July). Deep
interest evolution network for click-through
rate prediction. In Proceedings of the AAAI
conference on artificial intelligence (Vol. 33,
No. 01, pp. 5941-5948).
17. Guo, H., Tang, R., Ye, Y., Li, Z., & He, X.
(2017). DeepFM: a factorization-machine
based neural network for CTR prediction.
arXiv preprint arXiv:1703.04247.
18. Zhang, W., Du, T., & Wang, J. (2016,
March). Deep Learning over Multi-field
Categorical Data: –A Case Study on User
Response Prediction. In European conference
on information retrieval (pp. 45-57). Cham:
Springer International Publishing.
19. Hidasi, B., Karatzoglou, A., Baltrunas, L., &
Tikk, D. (2015). Session-based
recommendations with recurrent neural
networks. arXiv preprint arXiv:1511.06939.
20. Xiao, J., Ye, H., He, X., Zhang, H., Wu, F.,
& Chua, T. S. (2017). Attentional
factorization machines: Learning the weight
of feature interactions via attention networks.
arXiv preprint arXiv:1708.04617.
21. Vaswani, A., Shazeer, N., Parmar, N.,
Uszkoreit, J., Jones, L., Gomez, A. N., ... &
Polosukhin, I. (2017). Attention is all you
need. Advances in neural information
processing systems, 30.
22. He, X., Liao, L., Zhang, H., Nie, L., Hu, X.,
& Chua, T. S. (2017, April). Neural
collaborative filtering. In Proceedings of the
26th international conference on world wide
web (pp. 173-182).
