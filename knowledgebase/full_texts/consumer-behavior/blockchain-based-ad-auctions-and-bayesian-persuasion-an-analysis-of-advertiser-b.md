---
title: 'Blockchain-Based Ad Auctions and Bayesian Persuasion: An Analysis of Advertiser Behavior'
url: https://arxiv.org/abs/2410.07392
category: consumer-behavior
subcategory: empirical
date: 2024-10
venue: ''
authors:
- Xinyu Li
source: arxiv
pdf_url: https://arxiv.org/pdf/2410.07392
pages: 23
chars: 34419
fetched_at: '2026-11-08T13:06:16+00:00'
kb_version: 1
---

# Blockchain-Based Ad Auctions and Bayesian Persuasion: An Analysis of Advertiser Behavior

arXiv:2410.07392v2  [econ.GN]  6 Dec 2024
Blockchain-Based Ad Auctions and Bayesian Persuasion:
An Analysis of Advertiser Behavior
Xinyu Li
October 11, 2024
Abstract
This paper explores how ad platforms can utilize Bayesian pe rsuasion within
blockchain-based auction systems to strategically inﬂuen ce advertiser behavior despite
increased transparency. By integrating game-theoretic mo dels with machine learning
techniques and the principles of blockchain technology, we analyze the role of strategic
information disclosure in ad auctions. Our ﬁndings demonst rate that even in environ-
ments with inherent transparency, ad platforms can design s ignals to aﬀect advertisers’
beliefs and bidding strategies. A detailed case study illus trates how machine learning
can predict advertiser responses to diﬀerent signals, leadi ng to optimized signaling
strategies that increase expected revenue. The study contr ibutes to the literature by
extending Bayesian persuasion models to transparent syste ms and providing practical
insights for auction design in the digital advertising indu stry.
1

Contents
1 Introduction 4
1.1 Research Question . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2 Literature Review 5
2.1 Bayesian Persuasion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.2 Game Theory in Ad Auctions . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.3 Blockchain in Advertising . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.4 Machine Learning in Advertising . . . . . . . . . . . . . . . . . . . . . . . . 6
2.5 Gap in Literature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
3 Theoretical Framework 6
4 Model Development 6
4.1 Auction Mechanism . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
4.2 Platform’s Signaling Strategy . . . . . . . . . . . . . . . . . . . . . . . . . . 7
4.3 Advertisers’ Belief Updating . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
4.4 Advertisers’ Bidding Strategy . . . . . . . . . . . . . . . . . . . . . . . . . . 7
4.5 Platform’s Objective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
5 Integrating Machine Learning 8
5.1 Framework for Machine Learning Integration . . . . . . . . . . . . . . . . . . 9
5.2 Model Selection and Training . . . . . . . . . . . . . . . . . . . . . . . . . . 9
5.3 Prediction and Integration with Bayesian Persuasion . . . . . . . . . . . . . 10
5.3.1 Optimizing Signal Design . . . . . . . . . . . . . . . . . . . . . . . . 11
5.3.2 Feedback Loop . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
5.4 Challenges and Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . 11
6 Analysis 12
2

6.1 Advertisers’ Optimal Bidding Strategy . . . . . . . . . . . . . . . . . . . . . 12
6.2 Expected Payment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
6.3 Platform’s Revenue Maximization Problem . . . . . . . . . . . . . . . . . . . 13
6.4 Characterization of Optimal Signaling . . . . . . . . . . . . . . . . . . . . . . 13
6.5 Optimal Signaling in the Two-State Case . . . . . . . . . . . . . . . . . . . . 13
6.5.1 Full Disclosure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
6.5.2 No Disclosure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
6.5.3 Partial Disclosure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
6.6 Role of Blockchain Transparency . . . . . . . . . . . . . . . . . . . . . . . . 14
7 Case Study: Implementing Machine Learning in Signal Optim ization 15
7.1 Simulation Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
7.2 Data Preparation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
7.3 Model Training . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
7.4 Model Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
7.4.1 Performance Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
7.4.2 Interpretation of RMSE . . . . . . . . . . . . . . . . . . . . . . . . . 18
7.4.3 Model Eﬀectiveness . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
7.4.4 Residual Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
7.4.5 Conclusion on Model Performance . . . . . . . . . . . . . . . . . . . . 18
7.5 Policy Optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
7.6 Interpretation of Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
8 Discussion 20
9 Conclusion 21
3

1 Introduction
The digital advertising industry has undergone signiﬁcant transfo rmations with the advent of
emerging technologies like blockchain. Blockchain’s inherent transpa rency, immutability, and
decentralization promise to revolutionize ad auction systems by enh ancing trust, reducing
fraud, and improving supply chain eﬃciency (Joo et al., 2023).
In traditional digital advertising markets, auction processes are often opaque, with limited
visibility into bids, auction outcomes, and supply chain interactions. A dvertisers typically
have access only to their own performance metrics, lacking compre hensive insights into the
broader auction dynamics.(Kauﬀman and Wood, 2006) This opacity c an lead to ineﬃcien-
cies, ad fraud, and mistrust among market participants. (Zhang a nd Zhang, 2014)
Blockchain technology introduces a paradigm shift by recording all b ids and auction out-
comes transparently on a distributed ledger accessible to authoriz ed participants. (Soltani et al.,
2022) This transparency reduces information asymmetry, enhan ces supply chain eﬃciency,
and mitigates ad fraud by providing veriﬁable and immutable records o f transactions (Beck et al.,
2019). Advertisers can access historical data on bids and outcom es,allowing for more in-
formed decision-making and strategy development.(Jia et al., 2022) (P¨ arssinen et al., 2018)
However, this increased transparency poses challenges for ad pla tforms that traditionally
rely on information asymmetry to inﬂuence advertiser behavior.
This paper investigates how ad platforms can employ Bayesian persu asion strategies
within blockchain-based auction systems to strategically inﬂuence a dvertiser behavior, even
in the face of increased transparency. By integrating game-theo retic models with machine
learning techniques and the principles of blockchain technology, we a nalyze the role of strate-
gic information disclosure in ad auctions.
4

1.1 Research Question
How can ad platforms utilize Bayesian persuasion within blo ckchain-based auc-
tion systems to strategically inﬂuence advertiser behavio r despite increased trans-
parency?
2 Literature Review
2.1 Bayesian Persuasion
Introduced by Kamenica and Gentzkow (2011), Bayesian persuas ion explores how an in-
formed sender can inﬂuence the actions of a receiver by controlling the information ﬂow.
The sender commits to a signaling strategy that maximizes their expe cted payoﬀ, while the
receiver updates their beliefs according to Bayes’ Rule.
2.2 Game Theory in Ad Auctions
Game theory has been extensively used to model ad auctions, analy zing strategic interac-
tions between advertisers and platforms (Edelman et al., 2007). Tr aditional models assume
varying degrees of information asymmetry. (Xu and Cavallo, 2022) (Einy et al., 2014)
2.3 Blockchain in Advertising
Blockchain technology oﬀers transparency, immutability, and dece ntralization. In advertis-
ing, blockchain can enhance trust by providing veriﬁable data on ad d elivery and ensuring
that only veriﬁed, human users are counted in advertising metrics. (Kewell et al., 2017)
(Govea et al., 2024)
5

2.4 Machine Learning in Advertising
Machine learning techniques have been applied to predict user behav ior and optimize ad
targeting (Chaudhary et al., 2021). These models can capture com plex patterns in data,
enhancing decision-making processes.
2.5 Gap in Literature
While studies have explored Bayesian persuasion and blockchain sepa rately, there is a lack
of research at their intersection, particularly concerning how tra nsparency aﬀects strategic
information disclosure in ad auctions. Additionally, the integration of machine learning into
signaling strategies within this context remains underexplored.
3 Theoretical Framework
In transparent systems like blockchain-based auctions, tradition al information asymmetry is
reduced. However, platforms can still inﬂuence advertiser behav ior by designing strategic
signals within the transparent environment. We model the ad auctio n as a game between
the ad platform (sender) and advertisers (receivers). Advertis ers aim to maximize their
utility based on beliefs about the auction’s state and competitors’ a ctions. Machine learning
models are used to predict advertiser responses to diﬀerent signa ls, allowing the platform to
optimize its signaling strategy.
4 Model Development
We consider a blockchain-based advertising platform where N advertisers compete in an
auction for a single ad slot to be displayed to a user. The platform has private information
about the user engagement level, denoted by θ ∈ Θ, where Θ is a ﬁnite set of possible
engagement states (e.g., low, medium, high). The prior probability dis tribution over Θ is
6

given by π(θ) = Pr( θ). Each advertiser i ∈ A = {1, 2, ..., N} aims to maximize their expected
utility, which depends on their valuation of the ad impression, vi(θ), which is a function of
the user engagement level θ and the bidding strategy of other advertisers.
4.1 Auction Mechanism
The auction mechanism is a sealed-bid, second-price auction where a dvertisers submit bids
without knowing others’ bids. The highest bidder wins the slot and pa ys the amount of the
second-highest bid. While bids and outcomes are transparently rec orded on the blockchain,
the engagement level θ remains private to the platform.
4.2 Platform’s Signaling Strategy
The platform commits to a signaling policy σ : Θ → ∆(S), where S is the set of possible
signals the platform can send. ∆( S) is the set of probability distributions over S.
For each state θ ∈ Θ, the platform sends signal s ∈ S with probability σ(s | θ). The
signaling policy is common knowledge among advertisers.
4.3 Advertisers’ Belief Updating
Upon receiving signal s ∈ S, advertisers update their beliefs about the state θ using Bayes’
Rule:
µ(θ | s) = σ(s | θ)π(θ)∑
θ′∈Θ σ(s | θ′)π(θ′) . (1)
4.4 Advertisers’ Bidding Strategy
Advertisers choose bids to maximize their expected utility given their updated beliefs. The
expected utility for advertiser i is:
7

EUi(bi, b−i | s) =
∑
θ∈Θ
µ(θ | s) [vi(θ) − ci(bi, b−i)] qi(bi, b−i), (2)
where ci(bi, b−i) is the expected payment if advertiser i wins. qi(bi, b−i) is the probability
that advertiser i wins the auction. In a symmetric equilibrium, advertisers adopt biddin g
strategies that are functions of their expected valuations.
4.5 Platform’s Objective
The platform aims to maximize expected revenue by choosing an optim al signaling policy
σ∗. The expected revenue R(σ) is:
R(σ) =
∑
θ∈Θ
π(θ)
∑
s∈S
σ(s | θ)Eb[P (b | s)], (3)
where Eb[P (b | s)] is the expected payment from the auction given signal s.
The signaling policy must satisfy:
∑
s∈S
σ(s | θ) = 1 , ∀θ ∈ Θ, (4)
and
σ(s | θ) ≥ 0, ∀s ∈ S, θ ∈ Θ. (5)
5 Integrating Machine Learning
While our theoretical model provides a structured approach to un derstanding advertiser be-
havior, real-world bidding strategies may be inﬂuenced by numerous factors that are complex
and nonlinear. Machine learning (ML) techniques can capture these complexities by learning
patterns from ad auction data, allowing us to predict advertiser re sponses to diﬀerent signals
more accurately.
8

5.1 Framework for Machine Learning Integration
We integrate machine learning into our methodology through three k ey steps: data col-
lection and preparation; model selection and training; and predictio n and integration with
Bayesian persuasion. We use data from ad auctions, which includes a dvertiser bids bi for
various auctions, signals s sent by the platform in those auctions, user engagement levels
θ, and auction outcomes. Additionally, we collect advertiser-speciﬁc features such as bud-
get, industry sector, and bidding aggressiveness, as well as cont extual features like time of
day and ad category. Given the sensitive nature of the data, we mu st ensure compliance
with data protection regulations such as GDPR and CCPA. Anonymiza tion and aggregation
techniques should be employed to protect individual advertiser iden tities, thereby safeguard-
ing privacy while allowing for eﬀective model training. Data preproces sing involves several
steps. First, we perform data cleaning by removing or imputing missin g or erroneous data.
Next, we engage in feature engineering to create relevant featur es that capture important
aspects of advertiser behavior. We then normalize the features t o ensure consistent ranges
across variables, facilitating eﬀective learning by the model. Finally, w e split the dataset
into training, validation, and test sets to enable proper evaluation a nd prevent overﬁtting.
5.2 Model Selection and Training
Several machine learning models are suitable for predicting advertis er bids, including regres-
sion models such as linear regression, Lasso, and Ridge regression; tree-based models like
decision trees, Random Forests, and Gradient Boosting Machines ( e.g., XGBoost, Light-
GBM); neural networks, particularly feedforward neural netwo rks useful for capturing non-
linear relationships; and Support Vector Machines, which are eﬀect ive for high-dimensional
feature spaces. Given the complexity and size of the data, tree-b ased ensemble methods and
neural networks are promising candidates due to their ability to han dle nonlinearities and
interactions between features.
The training process involves several key steps. First, we deﬁne t he primary objective,
9

which is to predict the bid amount bi given the signal s and other features. We use Mean
Squared Error (MSE) as the loss function for regression tasks, a iming to minimize the average
squared diﬀerence between the predicted and actual bid amounts . Hyperparameter tuning is
performed using techniques like grid search to ﬁnd optimal model pa rameters that enhance
performance. To assess model performance and prevent overﬁ tting, we employ k-fold cross-
validation, which involves partitioning the data into subsets, training the model on some
subsets, and validating it on others.
We then evaluate the model’s performance using metrics such as Mea n Absolute Error
(MAE), which measures the average magnitude of errors without c onsidering their direc-
tion; Root Mean Squared Error (RMSE), which penalizes larger erro rs more than MAE by
squaring the errors before averaging and taking the square root ; and R-squared ( R2), which
represents the proportion of variance in the dependent variable t hat is predictable from the
independent variables. These metrics provide a comprehensive und erstanding of the model’s
accuracy and reliability in predicting advertiser bids.
5.3 Prediction and Integration with Bayesian Persuasion
Once trained, the model can predict how advertisers are likely to ad just their bids in response
to diﬀerent signals:
ˆbi = fML(s, xi), (6)
where fML represents the machine learning model and xi are the features related to
advertiser i. This prediction function enables us to estimate the expected bids b ased on
various signaling strategies.
10

5.3.1 Optimizing Signal Design
The platform can use these predictions to optimize its signaling strat egy σ. This involves
simulating diﬀerent signaling policies and predicting the corresponding advertiser bids, calcu-
lating expected revenue for each policy using the predicted bids, an d selecting the signaling
policy that maximizes expected revenue. By evaluating the revenue outcomes associated
with diﬀerent signals, the platform can strategically choose the info rmation to disclose to
advertisers.
5.3.2 Feedback Loop
In a dynamic environment, the platform can continuously update th e machine learning model
with new data. This includes using online learning to update model para meters incrementally
as new data arrives, ensuring that the model remains accurate ov er time. Additionally, the
platform can adjust signaling policies in real-time based on the latest p redictions, allowing
for adaptive strategies that respond to changing market conditio ns and advertiser behaviors.
5.4 Challenges and Considerations
The eﬀectiveness of machine learning models depends on the availabilit y of high-quality
data. Insuﬃcient data can lead to overﬁtting, where the model lea rns noise instead of the
underlying patterns, or underperformance due to the inability to c apture the complexity of
advertiser behaviors. Therefore, collecting a large and diverse da taset is crucial for model
robustness.
Complex models like neural networks may lack interpretability, making it diﬃcult to
understand how speciﬁc features inﬂuence predictions. This opac ity can be problematic
when explaining the model’s decisions to stakeholders or when diagnos ing issues. Tree-based
models, on the other hand, may oﬀer better interpretability throu gh visualization of decision
paths and feature importance measures.
Using machine learning to inﬂuence advertiser behavior raises ethica l considerations. It
11

is important to ensure transparency so that advertisers are awa re of how their data is used
and how the platform’s strategies may aﬀect them. Fairness must b e considered to ensure
that the model does not unfairly disadvantage certain advertiser s, possibly due to biases in
the data. Additionally, compliance with regulations that require explic it consent for data
usage, such as GDPR and CCPA, is essential to protect user privac y and maintain trust in
the platform.
6 Analysis
6.1 Advertisers’ Optimal Bidding Strategy
Given the updated beliefs µ(θ | s), advertiser i calculates their expected valuation:
ˆvi(s) = Eθ[vi(θ) | s] =
∑
θ∈Θ
µ(θ | s)vi(θ). (7)
In a second-price auction, the dominant strategy is to bid their exp ected valuation:
b∗ i (s) = ˆvi(s). (8)
6.2 Expected Payment
The expected payment for the platform is determined by the expec ted second-highest bid.
Assuming symmetric bidders, the bids are independent and identically distributed random
variables conditioned on the signal s.
The cumulative distribution function (CDF) of bids is:
F (b | s) = Pr ( b∗ i (s) ≤ b) = Pr (ˆvi(s) ≤ b) . (9)
The expected payment is then:
12

Eb[P (b | s)] = E
[
b(2) | s
]
, (10)
where b(2) denotes the second-highest bid.
6.3 Platform’s Revenue Maximization Problem
Substituting the expected payment into Equation (3), the platfor m’s optimization problem
becomes:
max
σ
R(σ) =
∑
θ∈Θ
π(θ)
∑
s∈S
σ(s | θ)E
[
b(2) | s
]
(11)
subject to
∑
s∈S
σ(s | θ) = 1 , ∀θ ∈ Θ, (12)
σ(s | θ) ≥ 0, ∀s ∈ S, θ ∈ Θ. (13)
6.4 Characterization of Optimal Signaling
The platform can design signals by partitioning the state space Θ into information structures
that maximize expected revenue. The key is to determine how ﬁnely t o partition Θ:
• Full Disclosure: Each state θ is associated with a unique signal.
• No Disclosure : All states share the same signal.
• Partial Disclosure : States are grouped, and each group shares a signal.
6.5 Optimal Signaling in the Two-State Case
Consider Θ = {θL, θH} with π(θL) = πL and π(θH) = πH , where θL < θ H .
13

6.5.1 Full Disclosure
Signals: S = {sL, sH}, where sL corresponds to θL and sH corresponds to θH . Beliefs:
µ(θL | sL) = 1, µ(θH | sH) = 1. Advertisers’ Bids: b∗ i (sL) = vi(θL), b∗ i (sH) = vi(θH ).
6.5.2 No Disclosure
Signals: S = {s}; the same signal is sent regardless of θ. Beliefs: µ(θL | s) = πL, µ(θH | s) =
πH . Advertisers’ Bids: b∗ i (s) = πLvi(θL) + πH vi(θH ).
6.5.3 Partial Disclosure
The platform can randomize signals to create mixed beliefs. Signals: S = {s1, s2}. Signaling
Policy:
σ(s1 | θL) = α, σ (s1 | θH ) = β,
σ(s2 | θL) = 1 − α, σ (s2 | θH ) = 1 − β,
where 0 ≤ α, β ≤ 1.
Advertisers update their beliefs using Equation (1) and adjust the ir bids accordingly.
For Θ with more than two states, the platform can design a signaling s cheme that par-
titions Θ into subsets, each associated with a signal. The optimal par tition can be found
using techniques from convex optimization and information design.
6.6 Role of Blockchain Transparency
Blockchain transparency ensures that all bids and outcomes are p ublicly recorded. However,
the platform’s private information about θ and strategic signaling remain tools for inﬂuencing
advertiser behavior.
14

The equilibrium consists of the platform’s optimal signaling policy σ∗ and advertisers’
bidding strategies b∗ i (s) based on updated beliefs.
This equilibrium is stable if no advertiser or the platform has an incentiv e to deviate
unilaterally.
7 Case Study: Implementing Machine Learning in Sig-
nal Optimization
7.1 Simulation Setup
To illustrate the integration of machine learning into the signaling stra tegy, we simulate
an environment characterized by 1,000 advertisers with varying ch aracteristics, data from
10,000 historical auctions, and signals representing diﬀerent levels of user engagement.
Generating Advertiser Proﬁles For each advertiser i, we assign a set of features. The
budget Bi is sampled from a normal distribution with a mean of $10,000 and a standard
deviation of $2,000. The industry sector Ii is a categorical variable representing the adver-
tiser’s industry, selected from multiple categories. The bidding aggr essiveness Ai is a value
between 0 and 1, sampled uniformly, indicating how aggressively the a dvertiser bids.
Simulating Auctions In simulating each auction j, we randomly select a subset of ad-
vertisers to participate. We assign a true user engagement level θj, sampled from a discrete
distribution—for example, low, medium, and high engagement levels wit h probabilities of
0.3, 0.5, and 0.2, respectively. Based on a predeﬁned signaling policy σ, we generate signals
sj to be sent to the advertisers.
Generating Bids For each advertiser i participating in auction j, we simulate their bid
bij using the equation:
15

bij = ftrue(sj, Bi, Ii, Ai, ǫij), (14)
where ftrue is the true (unknown) bidding function, and ǫij is a random noise term
reﬂecting unobserved factors, sampled from a normal distributio n with mean 0 and standard
deviation σǫ. The function ftrue captures how advertisers adjust their bids based on the
signal received and their own characteristics.
7.2 Data Preparation
Features We construct input features Xij for each advertiser-auction pair, including the
signal sj, which is encoded as numerical or categorical variables. The adver tiser features
comprise the budget Bi, industry sector Ii, and bidding aggressiveness Ai. Additionally, we
incorporate contextual features such as time of day and ad cate gory to capture environmental
factors that may inﬂuence bidding behavior.
Target Variable The target variable is the bid bij, representing the simulated bid sub-
mitted by advertiser i in auction j.
Data Splitting We split the dataset into a training set containing 70% of the data, a
validation set with 15%, and a test set comprising the remaining 15%. T his division allows
for eﬀective model training, hyperparameter tuning, and unbiase d evaluation of the model’s
predictive performance.
7.3 Model Training
Model Selection We select a Gradient Boosting Machine (GBM), speciﬁcally XGBoost,
due to its ability to handle nonlinear relationships and interactions bet ween features eﬃ-
ciently, especially with large datasets. XGBoost is well-suited for reg ression tasks and has
proven eﬀective in various predictive modeling applications.
16

Hyperparameter Tuning Hyperparameter tuning is performed using grid search over
a deﬁned set of parameters. We explore diﬀerent values for the lea rning rate (e.g., 0.01,
0.1, 0.2), maximum tree depth (e.g., 3, 5, 7), and the number of estim ators (trees) (e.g.,
100, 200, 500). Cross-validation on the training set is utilized to sele ct the combination of
hyperparameters that results in the best model performance wh ile preventing overﬁtting.
Training Process The model is trained to minimize the Mean Squared Error (MSE)
between the predicted bids ˆbij and the actual bids bij:
MSE = 1 Ntrain ∑ (i,j)∈Train (bij − ˆbij)2, (15)
where Ntrain is the number of samples in the training set. By minimizing the MSE, the
model learns to predict bid amounts that are as close as possible to t he actual bids in the
training data.
7.4 Model Evaluation
7.4.1 Performance Metrics
We evaluate the model on the test set using the Root Mean Squared Error (RMSE) and the
coeﬃcient of determination ( R2). The RMSE is calculated as:
RMSE =
√ 1
Ntest
∑
(i,j)∈Test
(bij − ˆbij)2, (16)
where Ntest is the number of samples in the test set. The R2 score is computed as:
R2 = 1 −
∑
(i,j)∈Test(bij − ˆbij)2 ∑
(i,j)∈Test(bij − ¯b)2 , (17)
where ¯b is the mean of the actual bids in the test set. These metrics provide insight into
the model’s accuracy and its ability to explain the variance in the bid amo unts.
17

7.4.2 Interpretation of RMSE
The RMSE of approximately 0.15 is low relative to the range and variabilit y of the bids
in our dataset. Speciﬁcally, the bids range from $0.1 to around $20.0, with an average bid
of approximately $5.0 and a standard deviation of about $2.5. An RMSE of 0.15 indicates
that the model’s predictions deviate from the actual bids by only $0.15 on average, which
is small compared to the average bid value and standard deviation. T his demonstrates that
the model has strong predictive accuracy.
7.4.3 Model Eﬀectiveness
The high R2 score of 0.85 signiﬁes that 85% of the variance in the bid amounts is ex plained
by the model. Combined with the low RMSE, these metrics indicate that the Gradient
Boosting Machine eﬀectively captures the complex relationships bet ween the input features
(signals, advertiser characteristics, and contextual factors) and the bid amounts.
7.4.4 Residual Analysis
To further assess the model’s performance, we conduct a residua l analysis. The residuals,
which are the diﬀerences between the actual and predicted bids, a re centered around zero
with no signiﬁcant patterns, suggesting that the model does not h ave systematic biases.
The spread of residuals is consistent across diﬀerent levels of pred icted bids, indicating
homoscedasticity, or constant variance. Additionally, the residua ls approximately follow a
normal distribution, which is desirable for regression models and sup ports the validity of the
model’s predictions.
7.4.5 Conclusion on Model Performance
The evaluation metrics and residual analysis conﬁrm that the machin e learning model pro-
vides accurate predictions of advertiser bids based on the featur es considered. This high
18

level of accuracy is essential for the platform to eﬀectively use th e model in optimizing its
signaling strategy and maximizing expected revenue.
7.5 Policy Optimization
Deﬁning Signaling Policies We consider three signaling policies: full disclosure ( σfull),
where signals perfectly reveal θj; no disclosure ( σnone), where signals provide no information
about θj; and optimized partial disclosure ( σopt), where signals are designed to strategically
inﬂuence advertiser beliefs to maximize revenue.
Simulating Advertiser Responses For each policy σ, we simulate advertiser bids using
the trained model:
ˆbσ ij = fML(sσ j , Xij), (18)
where sσ j is the signal sent under policy σ in auction j, and Xij represents the features
for advertiser i in auction j. This allows us to predict how advertisers adjust their bids in
response to diﬀerent signaling policies.
Calculating Expected Revenue For each auction j, we obtain the predicted bids ˆbσ ij for
all participating advertisers. The winner of the auction is the adver tiser with the highest
predicted bid, and the payment P σ j is the second-highest predicted bid, following the second-
price auction mechanism. The total expected revenue Rσ under policy σ is calculated as:
Rσ =
10,000∑
j=1
P σ j . (19)
Comparing Revenue Across Policies We calculate the percentage increase in expected
revenue when using the optimized partial disclosure policy compared to full disclosure:
19

Revenue Increase (%) =
(Rσopt − Rσfull
Rσfull
)
× 100%. (20)
Results Our simulation yields a revenue under full disclosure Rσfull of $9,190.47 and a
revenue under optimized partial disclosure Rσopt of $10,274.72. This represents a revenue
increase of approximately 11.80%, demonstrating the eﬀectivenes s of the optimized signaling
policy.
7.6 Interpretation of Results
Model Eﬀectiveness The high R2 score indicates that the machine learning model eﬀec-
tively captures the relationship between signals, advertiser featu res, and bidding behavior.
The model’s accuracy enables reliable predictions of how advertisers respond to diﬀerent
signals, which is crucial for optimizing the signaling strategy.
Impact of Optimized Signaling The optimized partial disclosure policy leads to a sig-
niﬁcant increase in expected revenue compared to full disclosure. This demonstrates that
strategic signal design can inﬂuence advertiser bids even in transp arent systems. By carefully
selecting the information disclosed through signals, the platform ca n shape advertiser beliefs
and bidding strategies to enhance revenue outcomes.
8 Discussion
The integration of machine learning into the platform’s signaling strat egy has signiﬁcant
practical implications for both ad platforms and advertisers. By lev eraging machine learn-
ing models, platforms can enhance their ability to predict advertiser responses to diﬀerent
signals, allowing for the optimization of signaling policies and an increase in expected rev-
enue. This advancement necessitates investment in data collection , model development, and
20

computational resources. Advertisers, in turn, must be aware o f these strategic signaling ef-
forts and may consider developing their own predictive models to ant icipate and counteract
platform strategies, leading to a complex interplay in bidding behavior s.
Machine learning models contribute to reﬁning the Bayesian updating process by pro-
viding more accurate estimations of advertisers’ expected valuat ions. The predicted bids
feed into the calculation of posterior beliefs, inﬂuencing both the pla tform’s and advertisers’
strategic decisions. While this integration oﬀers improved accuracy and real-time adapta-
tion of strategies, it also introduces challenges such as dependenc y on high-quality data and
increased computational demands.
Future work should focus on validating the proposed methodology u sing real-world auc-
tion data to assess its practical applicability and eﬀectiveness. Inc orporating dynamic mod-
els that account for advertiser adaptation over time could provide deeper insights into the
evolving strategic interactions between platforms and advertiser s. Additionally, exploring
advanced techniques like reinforcement learning for policy optimizat ion and considering the
potential for adversarial models used by advertisers can furthe r enhance the robustness and
sophistication of signaling strategies in blockchain-based ad auction s. Ethical considerations,
including transparency, fairness, and compliance with data protec tion regulations, remain
paramount as these technologies continue to evolve.
9 Conclusion
This paper demonstrates that Bayesian persuasion remains releva nt in blockchain-based
ad auctions with inherent transparency. By integrating machine lea rning, ad platforms can
strategically design signals to inﬂuence advertiser behavior, impact ing bidding strategies and
platform revenue. Our ﬁndings contribute to the theoretical und erstanding of information
economics in transparent systems and oﬀer practical insights for auction design in the digital
advertising industry.
21

References
Beck, R., W¨ ust, K., and Gervais, A. (2019). The transparency ch allenge of blockchain in
organizations. Electronic Markets, 29:499–512.
Chaudhary, K., Alam, M., Al-Rakhami, M. S., and Gumaei, A. (2021). Ma chine learning-
based mathematical modelling for prediction of social media consume r behavior using big
data analytics. Journal of Big Data , 8(1):1–20.
Edelman, B., Ostrovsky, M., and Schwarz, M. (2007). Internet ad vertising and the gen-
eralized second-price auction: Selling billions of dollars worth of keywo rds. American
Economic Review, 97(1):242–259.
Einy, E., Haimanko, O., Orzach, R., and Sela, A. (2014). Common-valu e all-pay auctions
with asymmetric information. International Journal of Game Theory , 42(2):219–254.
Govea, J., Gaibor-Naranjo, W., and Villegas-Ch, W. (2024). Securin g critical infrastructure
with blockchain technology: An approach to cyber-resilience. Computers, 13(5):122.
Jia, X., Song, X., and Sohail, M. (2022). Eﬀective consensus-based distributed auction
scheme for secure data sharing in internet of things. Symmetry, 14(8):1664.
Joo, M., Kim, S. H., Ghose, A., and Wilbur, K. C. (2023). Designing distr ibuted ledger
technologies, like blockchain, for advertising markets. International Journal of Research
in Marketing , 40(1):12–21.
Kamenica, E. and Gentzkow, M. (2011). Bayesian persuasion. American Economic Review ,
101(6):2590–2615.
Kauﬀman, R. J. and Wood, C. A. (2006). Doing their bidding: An empir ical examination
of factors that aﬀect a buyer’s utility in internet auctions. Information Technology and
Management, 7(3):171–190.
22

Kewell, B., Adams, R., and Parry, G. (2017). Blockchain for good? st rategic change. Strategic
Change, 26(5):429–437.
P¨ arssinen, M., Kotila, M., Cuevas, R., Phansalkar, A., and Manner, J . (2018). Is blockchain
ready to revolutionize online advertising? IEEE Access, 6:54884–54899.
Soltani, R., Zaman, M., Joshi, R., and Sampalli, S. (2022). Distributed le dger technologies
and their applications: A review. Applied Sciences, 12(15):7898.
Xu, H. and Cavallo, R. (2022). The strange role of information asym metry in auctions—does
more accurate value estimation beneﬁt a bidder? Proceedings of the AAAI Conference on
Artiﬁcial Intelligence , 36(5):5236–5243.
Zhang, C. and Zhang, E. (2014). Optimized bidding algorithm of real- time bidding in online
ads auction. In 2014 International Conference on Management Science & Engi neering
(21th Annual Conference Proceedings), pages 33–42. IEEE.
23
