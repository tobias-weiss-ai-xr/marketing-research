---
title: Quantifying the Privacy of Counterfactuals by Leveraging Membership Inference Attacks Against Synthetic
  Data
url: https://arxiv.org/abs/2606.06334
category: ai-marketing
subcategory: measurement
date: 2026-06
venue: ''
authors:
- Maryam Babaei
- Yingke Wang
- Hadrien Lautraite
- Heber H. Arcolezi
- Ulrich Aivodji
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.06334
pages: 35
chars: 77021
fetched_at: '2026-11-08T13:36:04+00:00'
kb_version: 1
---

# Quantifying the Privacy of Counterfactuals by Leveraging Membership Inference Attacks Against Synthetic Data

Quantifying the Privacy of Counterfactuals by Leveraging
Membership Inference Attacks Against Synthetic Data
MARYAM BABAEI,ÉTS Montreal and Mila, Canada
YINGKE WANG,ÉTS Montreal and Mila, Canada
HADRIEN LAUTRAITE,UQAM, Canada
HÉBER H. ARCOLEZI,ÉTS Montreal, Canada and Inria Grenoble, France
ULRICH AÏVODJI,ÉTS Montreal and Mila, Canada
SÉBASTIEN GAMBS,UQAM, Canada
Counterfactuals are typically used in high-stakes decision areas to explain a machine learning model by showing how changes
to the user profiles result in the desired outcome. However, explaining the model’s decisions through counterfactuals can also
be exploited by an adversary to conduct privacy attacks against the model or its training data. Drawing on the analogy that
counterfactuals provide realistic substitutes for real training data, similar to synthetic data, we demonstrate in this paper
how it is possible to successfully perform privacy attacks on counterfactuals by drawing on the attacks developed against
synthetic data. More precisely, we investigate the effectiveness of the membership inference attacks designed for synthetic
data on various types of counterfactuals. Additionally, while existing membership inference attacks against counterfactuals
usually require to be able to query the model, we show how it is possible to perform successful membership inference attacks
using only a set of counterfactuals, with no access to the model from which they are generated. Our results demonstrate that
model developers should be more cautious when releasing counterfactuals to various users, as it can lead to a privacy breach.
CCS Concepts:•Security and privacy → Social aspects of security and privacy;Privacy protections;•Computing
methodologies→Artificial intelligence;Causal reasoning and diagnostics.
Additional Key Words and Phrases: Counterfactuals, Privacy, Membership inference attacks, synthetic data
ACM Reference Format:
Maryam Babaei, Yingke Wang, Hadrien Lautraite, Héber H. Arcolezi, Ulrich Aïvodji, and Sébastien Gambs. 2026. Quantifying
the Privacy of Counterfactuals by Leveraging Membership Inference Attacks Against Synthetic Data. InThe 2026 ACM
Conference on Fairness, Accountability, and Transparency (FAccT ’26), June 25–28, 2026, Montreal, QC, Canada.ACM, New York,
NY, USA, 35 pages. https://doi.org/10.1145/3805689.3812361
1 Introduction
Counterfactuals are instances generated to show the most similar profiles to the query profile that achieve the
desired outcome [6, 18, 23, 35]. In particular, they are often used in machine learning (ML) for high-stakes decision
settings to help users understand the model’s decisions. However, counterfactuals can also reveal information
Authors’ Contact Information: Maryam Babaei, maryam.babaei.1@ens.etsmtl.ca, ÉTS Montreal and Mila, Canada; Yingke Wang, ÉTS
Montreal and Mila, Canada, yingke.wang@etsmtl.ca; Hadrien Lautraite, UQAM, Canada, lautraite.hadrien@courrier.uqam.ca; Héber H.
Arcolezi, ÉTS Montreal, Canada and Inria Grenoble, France, heber.hwang-arcolezi@etsmtl.ca; Ulrich Aïvodji, ÉTS Montreal and Mila, Canada,
ulrich.aivodji@etsmtl.ca; Sébastien Gambs, UQAM, Canada, gambs.sebastien@uqam.ca.
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that
copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page.
Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy
otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from
permissions@acm.org This work is licensed under a Creative Commons Attribution 4.0 International License.
FAccT ’26, Montreal, QC, Canada
©2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2596-8/2026/06
https://doi.org/10.1145/3805689.3812361
arXiv:2606.06334v1  [cs.LG]  4 Jun 2026

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Babaei et al.
about the model itself or the training data through privacy attacks [1, 10, 19, 36] such as membership inference
attacks (MIAs) [31]. Yet, few MIA attacks have been developed against counterfactuals [28], and additionally,
they need query access to the model. Thus, model providers can potentially prevent such attacks by limiting the
number of queries per user or providing repetitive counterfactuals for similar queries. In this paper, we investigate
how an adversary could circumvent such protection mechanisms by leveraging MIAs designed against synthetic
data in the so-calledno-box setting, in which only the set of counterfactuals generated by the model is available
to the adversary. As synthetic data is often used for sharing purposes when the privacy of training data is critical,
a wide range of research has been conducted to evaluate these data against privacy attacks such as membership
inference attacks [7, 13, 33]. Furthermore, MIAs developed to target synthetic data often do not require access to
the models generating this data [7, 27]. Rather, they are designed to predict the membership of a target instance
using only the synthetic data generated, which is consistent with the definition of a no-box attack setting [8].
However, some of these attacks also assume the availability of auxiliary data drawn from the same distribution
as the training set [33].
Since counterfactuals and synthetic data both try to generate instances similar to the training set, in this paper,
we propose to view counterfactuals as artifacts produced by the counterfactual generation process, in the same
manner as synthetic data can be considered as being derived from the training data through a generative process.
While MIAs against synthetic data have been deeply explored, their applicability to counterfactuals remains a
critical gap in the literature. Considering counterfactuals’ similarity to synthetic data, the main contribution of
this work is to bridge these two domains by investigating the transferability of state-of-the-art synthetic data
attacks to the counterfactual landscape. More precisely, we aim at determining when releasing counterfactuals
is safe when limiting queries per user and whether it is possible to perform no-box attacks against them, i.e., a
significant shift from existing literature, which often assumes stronger adversary capabilities. More precisely, we
have implemented an ensembling MIA [39] against counterfactuals generated by state-of-the-art counterfactual
generation mechanisms [6, 23, 35] and compared their effectiveness with that of counterfactual distance attack,
an MIA attack designed specifically for counterfactuals [28]. Our approach has the additional benefit of working
in the no-box setting, which is a weaker adversary model than the one usually considered for attacks against
counterfactuals.
The outline of the paper is as follows. First, in Section 2, we review the background on synthetic data and MIAs
against such data before presenting in Section 3 the counterfactual generation mechanisms that we consider, as
well as the counterfactual distance attack against which we will compare ourselves. Afterwards, in Section 4,
we explain our attack framework and methodology, followed by the reporting of our experimental results in
Section 5. Finally, we conclude in Section 6.
2 Membership inference attacks against synthetic data
Synthetic data generation approaches aim to generate realistic data that mimics the characteristics of training data.
For instance, synthetic data can be obtained by using generative models such as GANs (Generative adversarial
networks) [4, 11]. More precisely, the synthetic data should be diverse, novel and realistic with respect to the
properties of the original data distribution [ 25]. Since privacy is a critical concern in generating synthetic
data, especially in domains such as health and finance in which the training data is highly personal, synthetic
data generation methods have also been proposed based on the use of differential privacy [ 9]. These include
DP-synthetic data generation techniques that are GAN-based [5, 34] or marginal-based [21, 22].
One of the popular privacy attacks against synthetic data is MIA, which aims to determine whether a specific
profile was used during the synthetic data generator’s training phase. This attack, which has been introduced by
Hayes and collaborators [12], can be formalized for synthetic data generators as follows [33]:

Quantifying the Privacy of CFs by Leveraging MIA Against Synthetic Data FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
Definition 1.Let the random variable 𝑋 be defined onX, with distribution 𝑃𝑅(𝑋) . Let 𝐷𝑚𝑒𝑚 iid∼𝑃 𝑅(𝑋) be a
training set of independently sampled points from distribution 𝑃𝑅(𝑋) . Now let 𝐺 : 𝑍→𝑋 be a generator that
generates data given some random (e.g., Gaussian) noise 𝑍 . The generator𝐺 is trained on 𝐷𝑚𝑒𝑚 and is subsequently
used to generate a synthetic dataset 𝐷𝑠𝑦𝑛 . Finally, let 𝐴 : 𝑋→ [0, 1] be the attacker model that possesses the
synthetic dataset𝐷𝑠𝑦𝑛 , some test point 𝑥∗, with𝑋∗∼𝑃 𝑅(𝑋) , and possibly other knowledge (i.e., a reference dataset
independently sampled from 𝑃𝑅(𝑋) ). The adversary 𝐴 aims to determine whether 𝑋∗∼𝑃 𝑅(𝑋) belongs to 𝐷𝑚𝑒𝑚,
hence the perfect attacker outputs𝐴(𝑥 ∗)=1[𝑥 ∗∈𝐷 𝑚𝑒𝑚].
The main adversarial models used in this attack setting for MIA in synthetic data are the following:
• Black-box setting, in which the adversary can only blindly collect samples. They may also have access to a
reference dataset independently sampled from the training data distribution.
• Thewhite-box settingin which the adversary has access to the model generating synthetic data and its
internal settings, in addition to generated samples.
• Thepartial white-box setting, in which the adversary has some level of access to the model and some
information about the training dataset.
In this paper, we performed the ensembling MIA in which six main state-of-the-art MIAs have been implemented.
These attacks are detailed hereafter.
Distance to Closest Record (DCR/ DCR-Diff)[ 7]. Different variants of this attack exist in the black-box,
partial white-box and white-box settings. In the black-box setting, in which the adversary can only blindly collect
samples generated by the generator, these samples are used to estimate the probability of one instance being a
member of the training data of the generative model. More precisely, if the synthetic samples are closer to the
target instance than other points from the same distribution, it is inferred as a member. Equation 2 shows how
the membership probability of𝑥 is computed, in which𝜙(.,.) is the kernel function and𝐿(.,.) is the distance
metric used.
𝑃(𝑚𝑖|𝑥𝑖,𝜃𝑣)∝𝑃 G𝑣(𝑥|𝜃𝑣).(1)
𝑃G𝑣(𝑥|𝜃𝑣)= 1 𝑘 𝑘∑︁ 𝑖−1 𝜙(𝑥,G 𝑣(𝑧𝑖))≈ 1 𝑘 𝑘∑︁ 𝑖−1 𝑒𝑥𝑝(−𝐿(𝑥,G 𝑣(𝑧𝑖)));𝑧 𝑖∼𝑃 𝑧.(2)
Based on this equation, the probability of the query instance 𝑥 being a member of the training dataset of the
generative model is calculated based on its average distance to the generated synthetic data.
Monte-Carlo attack[ 13]. Similar to the DCR attack, the Monte-Carlo attack uses the distance to synthetic
data points as a proxy for membership. The intuition behind this attack is that if a generator is trained to generate
instances close to training data, it will overfit. In this respect, the probability of a target point𝑥 being a member
increases if it is close to a generated point. To estimate this probability, an𝜖-neighbourhood of point𝑥 is defined
as𝑈𝜖(𝑥)={𝑥 ′|𝑑(𝑥,𝑥 ′)≤𝜖} . The adversary looks into a ball with radius𝜖 around the target point𝑥 and counts
the number of existing generated instances in this ball. According to the Monte-Carlo theory [27], the probability
of a target point𝑥being a member of the training data of the generative model is computed as follows:
ˆ𝑓𝑀𝐶−𝜖(𝑥)= 1 𝑛 𝑛∑︁ 𝑖=1 1𝑔𝑖∈𝑈𝜖(𝑥),(3)
in which𝑔𝑖∈𝑈 𝜖(𝑥) includes instances in the ball𝑈 with radius𝜖 around query instance𝑥. If this probability is
higher than a predefined threshold, the target point is considered a member, while otherwise it is not the case.
TheDOMIAS attack[ 33] also benefits from the generative model’s overfitting to the training data in performing
MIA. An additional assumption is that the adversary has access to some auxiliary data sampled from the same

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Babaei et al.
distribution as the training data. Considering access to this data distribution, the attack formulation changes to
the following equation, in which𝑝 𝑅(𝑋)refers to the real data distribution.
𝐴𝐷𝑂𝑀𝐼𝐴𝑆(𝑥∗)=𝑓
𝑝𝐺(𝑥∗)
𝑝𝑅(𝑥∗)

.(4)
In Equation (4), 𝑓 is a monotonically increasing function with a range between zero and one, showing the
probability of instance𝑥∗ being a member of the training data. Thus, increasing the probability of the target
instance belonging to the synthetic data distribution compared to that of belonging to the reference data
distribution results in a higher membership score for the query instance.
TheData Plagiarism Index (DPI)[ 37] evaluates the density ratio of synthetic data compared to the reference
(auxiliary) data to analyze the local memorization around the target point. More precisely, DPI generates a
𝑘-neighbourhood(𝑥∗) for each target point 𝑥∗ using the synthetic and reference datasets. The DPI value 𝜌 is
calculated as:
𝜌(𝑥∗)=
˝
𝑧∈𝐷(𝑥 ∗) I(𝑧∈𝑆) ˝
𝑧∈𝐷(𝑥 ∗) I(𝑧∈𝑅) .(5)
When there is no synthetic data in the neighborhood (𝐷𝑃𝐼= 0), it is a sign of underfitting. In contrast, if the
number of synthetic and reference data is equal (𝐷𝑃𝐼= 1), no data plagiarism has happened, while a higher
number of instances in synthetic data compared to the reference data (𝐷𝑃𝐼> 1) is a sign of overfitting in the
generative model, which leaks membership.
TheGen-LRA attack[ 38] builds a surrogate density estimator over𝑅 (i.e., the reference set), which is used
to estimate the likelihood of𝑆 (i.e., the synthetic data). If the likelihood of𝑆 is significantly higher in a density
estimator over𝑅∪𝑥 ∗, it illustrates overfitting. An improvement on this attack is to localize this evaluation to
samples close to𝑥∗. The membership score for the GenLRA is computed as:
fGen-LRA(𝑥∗)=
˛
𝑠∈𝑆 𝑝𝑅∪{𝑥∗}(𝑠)˛
𝑠∈𝑆 𝑝𝑅(𝑠) .(6)
LOGAN/Classifier[ 12], trains a GAN using synthetic data to approximate the target’s characteristics. The
discriminator of this GAN learns to distinguish between reference data and synthetic data. This discriminator is
then used to investigate the membership of the query instance in the training model, based on the assumption
that the member instances will be classified as synthetic data [14].
3 Counterfactual generation mechanisms
Counterfactuals are explanations of why some profiles received undesired decisions from the model [35]. They
have properties somewhat similar to those of synthetic data, which include proximity, plausibility and diver-
sity [18]. Theproximitymeans counterfactuals should be as close as possible to the query instance,plausibility
concerns generating instances that lie near the real data manifold, while finallydiversityaddresses the concern
about generating mutually distinct counterfactuals for each instance, showing various ways for changing the
outcome. Counterfactuals can be formally defined as follows:
Definition 2.Given an input profile with feature values 𝑥𝑜 1,...,𝑥 𝑜 𝑛 and the corresponding model’s prediction
𝑑1, a counterfactual explanation method generates a counterfactual with feature values 𝑐𝑓 1,...,𝑐𝑓 𝑛 satisfying two
conditions: (1) the model should assign it a different prediction than from the original instance and (2) it should be
close to the original instance in terms of a predefined distance, with the Euclidean distance being one of the most
commonly used in counterfactuals.
Various techniques have been suggested to generate counterfactuals, which can be divided into two main
categories: perturbation-based and instance-based counterfactuals. Perturbation-based methods take the original

Quantifying the Privacy of CFs by Leveraging MIA Against Synthetic Data FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
instance and then perturb its feature values toward the decision boundary until the model’s decision changes.
The associated instance is then considered as the generated counterfactual. While these methods generate coun-
terfactuals with the lowest change in the original instance, they often suffer from a low level of plausibility [20].
Instance-based counterfactuals are suggested to address this problem by using original instances from the training
dataset to generate more realistic counterfactuals. Hereafter, one method from each category is explained that
will be later used in Section 5 to assess the effectiveness of synthetic data MIA on counterfactuals generated
using both techniques.
TheNearest Instance Counterfactual Explanations (NICE)[ 6] first identifies the nearest neighbour of the
original instance for which the model makes a different prediction. Then, through an iterative process, the feature
values of the factual instance are replaced with the values of the nearest neighbour until the model changes its
prediction. The selection of the feature values is based on a reward function, which integrates several criteria
related to the quality of counterfactuals, namely proximity, sparsity and plausibility.
Diverse Counterfactual Explanations (Dice)[ 23] generates diverse actionable counterfactuals by solving
an optimization algorithm for any differentiable model. More precisely, in addition to minimizing the distance
between the original instance and its generated counterfactual, the objective of this optimization is to generate a
number of diverse counterfactuals to give users the chance to decide how they want to update their profile to
change the model’s decision. The following equation formalizes this optimization problem, which is optimized
through gradient descent:
𝐶(𝑥)=arg min
𝑐1,...,𝑐𝑘
1
𝑘
𝑘∑︁
𝑖=1
𝑦𝑙𝑜𝑠𝑠𝑓(𝑐 𝑖),𝑦 + 𝜆1 𝑘 𝑑𝑖𝑠𝑡(𝑐 𝑖,𝑥)−𝜆 2𝑑𝑝𝑝_𝑑𝑖𝑣𝑒𝑟𝑠𝑖𝑡𝑦(𝑐 1,...,𝑐 𝑘),(7)
in which𝑐𝑖 is a counterfactual explanation,𝑘 is the number of counterfactuals,𝑦𝑙𝑜𝑠𝑠 is a metric to minimize
prediction error and 𝑑𝑝𝑝_𝑑𝑖𝑣𝑒𝑟𝑠𝑖𝑡𝑦 is the diversity parameter. 𝜆1 and𝜆2 are hyperparameters to balance the
effects of proximity and diversity.
SCFEas suggested by Wachter and collaborators [ 35], is a gradient-based counterfactual generation algorithm
like DICE. This method differs from other counterfactual mechanisms in that it treats all features as numerical
features. The distance mechanism used in this method is the following:
𝑑(𝑥,𝑥 ′)= ∑︁
𝑘∈𝐹

𝑥𝑘−𝑥′ 𝑘

MAD𝑘
,(8)
in which
MAD𝑘 =median 𝑗∈𝐷

𝑋𝑗,𝑘−median𝑙∈𝑃(𝑋𝑙,𝑘)

.(9)
Instance-based Diverse Counterfactual Explanations (Dice-kdtree). In addition to instance-based and
perturbation-based counterfactual mechanisms, it is also possible to select an instance from the training dataset
that is already classified in the counterfactual class and return it as the counterfactual. Mothiel and collaborators
have proposed to fit a decision tree on the training dataset [ 23]. Then, for each query instance, the approach
identifies the closest instance to the query by following the decision tree path and outputs that instance as the
counterfactual.
Counterfactual distance attack (dist-lrt).Counterfactuals are generated as closely as possible to the original
instances [35] and, consequently, to the decision boundary. Using these assumptions, the counterfactual distance
attack [28] uses the distance between query instances and their counterfactuals as a proxy of the query instances’
distance to the decision boundary. Like in some other MIAs [31], shadow models are used to simulate the target
model properties. More precisely, shadow models are surrogate models trained to imitate the target model’s
behaviour while providing the adversary with white-box access to their inner workings, training data and
prediction vectors.

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Babaei et al.
The counterfactual distance attack trains 𝑛 shadow models on shadow datasets that do not include the
query instance. Then, all shadow models are used to generate counterfactuals for the query instance. Since
the query instance has not been used in any of the shadow models’ training sets, these distances are used to
estimate the distribution of non-member counterfactual distances. Given this distribution and the query instance’s
counterfactual distance for the target model, the adversary predicts whether each query instance belongs to the
model’s training dataset. The full likelihood ratio is defined as:
Λ= Pr[𝑐(𝑥,𝑥 ′)|𝑥∈𝐷 𝑡] Pr[𝑐(𝑥,𝑥 ′)|𝑥∉𝐷 𝑡],(10)
in which𝑐(𝑥,𝑥 ′) is the distance between the counterfactual and the query instance, and𝐷𝑡 is the training dataset.
Using diverse techniques to generate counterfactuals facilitates investigating the efficiency of our proposed attack
compared to the baseline in relation to each specific technique.
4 Methodology
This section formalizes our threat models and details the experimental pipeline used to evaluate membership
inference attacks (MIAs) on counterfactual explanations. We consider two attack categories: (i) a no-box MIA
that treats released counterfactuals as a synthetic dataset and (ii) a counterfactual-distance baseline that requires
query access to the target model.
4.1 Threat models
We define the two attacks with the following two-player security game between a challenger (model provider)
and an adversary (attacker) [17].
4.1.1 No-box MIA from released counterfactuals.
(1) The challenger picks a sample dataset from the target distribution and generates a training datasetD← D
and captures the target𝑧from the universeU.
(2) The challenger trains the model𝑓 𝜃←T(D).
(3) The challenger provides users with query access to the model𝑓𝜃 and gives a counterfactual explanation
𝑐𝑓(𝑥)for the undesired outcomes they receive for their query𝑥.
(4) The adversary collects a set of counterfactuals𝑐𝑓(𝑥)generated for various users.
(5) The adversary has no access to the model𝑓 𝜃 or training setD.
(6) The adversary makes a guess𝑔 based on their knowledge about the distributionDand the counterfactuals
they have collected.
(7) The adversary wins if𝑔∈D.
4.1.2 Counterfactual-distance baseline (query access).
(1) The challenger picks a sample dataset from the target distribution and generates a training datasetD← D
and captures the target𝑧from the universeU.
(2) The challenger trains the model𝑓 𝜃←T(D).
(3) The challenger provides users with query access to the model𝑓𝜃 and gives a counterfactual explanation
𝑐𝑓(𝑥)for the undesired outcomes they receive for their query𝑥.
(4) The adversary gets𝑥 ′ =𝑐𝑓(𝑥)from model𝑓 𝜃 and calculates distance between𝑥and𝑥 ′ as𝑐(𝑥,𝑥 ′).
(5) The adversary selects a false positive rate𝛼∈(0,1).
(6) The adversary samples𝑁 set of instancesD⟩ ⊔ from datasetD and trains𝑁 shadow models on them.D⟩ ⊔ is
considered not having instance𝑥.

Quantifying the Privacy of CFs by Leveraging MIA Against Synthetic Data FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
(7) The adversary generates counterfactuals for query instance𝑥 using all𝑁 shadow models and gets counter-
factual distances{𝑐(𝑥,𝑥 ′(1)),...,𝑐(𝑥,𝑥 ′(𝑁))}.
(8) The adversary calculates the maximum likelihood estimates for the mean ( ˆ𝜇MLE and variance ˆ𝜎 2 MLE of these
shadow distances.
(9) The adversary compares the target distance𝑐(𝑥,𝑥 ′) against this estimated distribution. if𝑥(𝑥,𝑥 ′) is bigger
than𝑍1−𝛼 quintile of the non-member distribution, the guess𝑔 is non-members. Otherwise,𝑔 is a member.
(10) The adversary wins if𝑔is correct.
4.2 Attack framework
Figure 1 presents a high-level overview of the attack pipeline. Our evaluation follows a common pipeline across
datasets and counterfactual generation mechanisms. For each dataset, we split the data into training (60%), test
(20%) and counterfactual (20%) sets. We first train the target model on the training set before evaluating it on
the test set. Finally, counterfactuals were generated for instances drawn from the counterfactual split. These
counterfactuals constitute the “synthetic” dataset available to the no-box adversary. The default synthetic set size
for the attack is 10000 instances. Details on the implementations and sizes are provided in Section 5.
Following the approach used by Ward and collaborators [39] to build an attack dataset, we sample an equal
number (𝑛= 500) of members from the training set and non-members from the test set (ensuring the non-member
set contains no training instances via re-identification checks). Additionally, we sample a reference set from the
test set following the same general protocol as non-members, which is utilized by some of the individual attacks
in the ensemble, compared to the counterfactual distances baseline attack, which requires inference access to the
model’s predictions and counterfactuals.
Dataset
Train
Test
Eval. Counterfactual
Generator
Members
Nonmembers
Model
Counterfactual
Set
Attack Set
Attack
Mechanism result
1- Dataset and Splits 2- Model Artifacts 3- Attack inputs 4- Membership Attack
Auxiliary
Set
Fig. 1. Attack pipeline. The attacker has no access to or information about the model or counterfactual generator. They only
have a set of counterfactuals, a small auxiliary set from the same distribution of the dataset, and a set of query instances to
find their membership status.
Following our pipeline in Figure 1, synthetic and attack datasets are fed into the attack model. More precisely,
for the no-box setting, we apply an ensemble of MIAs originally designed for synthetic tabular data using the
collected counterfactuals as the synthetic dataset. The implemented attacks include Distance to Closest Record
DCR/DCR-Diff, DOMIAS, Data Plagiarism Index (DPI), Gen-LRA, LOGAN/Classifier, and Monte Carlo (MC).
Each attack outputs a membership score per target instance and we then apply ensembling to combine signals
across attacks. In particular, the following ensembling strategies are used:

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Babaei et al.
• Majority voting. Each instance is considered a member by majority voting if the majority of individual
attacks decide it is a member with confidence larger than a predefined threshold. We followed [39], which
used majority voting with thresholds ranging from 90% to 98%.
• Mean aggregation. The membership score assigned to the instance is the mean score assigned to it by all
individual attacks.
While ensembling does not always outperform all individual attacks, it typically achieves better performance
than using any single individual attack. According to Ward and collaborators [ 39], ensembling works well
because each individual attack performs better on some synthetic data depending on the dataset properties and
the algorithm used to generate it. Therefore, ensembling helps strong attacks to influence the final prediction
more than weak attacks, which is helpful because the adversary does not know how synthetic data (in our case,
counterfactuals) are generated or which attack will perform better on the data.
5 Experimental evaluation
The experimental results of the attacks are provided in this section. To provide reproducibility, our code is
available at Counterfactual distance attack and No-box ensemble MIA. Both repositories have an execution
guide.ipynb file. All results presented here, including counterfactual information, the model’s accuracy and attack
results for no-box and baseline attack, are averaged over five individual executions using different random seeds.
5.1 Experimental setup
Datasets.We performed our attack on four tabular datasets (summarized in Table 1), including Adult income,
Acs_income, Compas and Heloc.Adult income[ 3] includes information of 48842 individuals that are described
with 14 features, with the learning task being to predict whether the profile owner earns more than 50k. Following
the literature, we dropped five features (education-num, fnlwgt, native-country, capital-gain and capital-loss) that
are redundant or not related to the training task, and all the experiments used 9 related features.Acs_incomeis
the new version of the Adult dataset, with 10 features and a training set of 1.66M instances. In our implementation,
after preprocessing and removing instances with missing feature values, the final dataset size is 199,665 instances.
Compas[ 2] is a dataset used for recidivism prediction composed of 6172 profiles described by 8 features. The
prediction task of this dataset is to predict the risk of recidivism.Heloc[ 26], or home equity line of credit, uses
23 features to predict whether a profile is high-risk or low-risk of approval for the line of credit. An overview of
the datasets and the accuracy of models trained on them is presented in Table 1.
Adult Compas HelocAcs_income
#features 9 8 23 10
Dataset size 48842 6172 10000 199665
Class Income Low_risk Riskperformance Income
Accuracy 81% 68% 72% 80%
Table 1. Summary of datasets characteristics and accuracy of their models.
To determine the appropriate size of the attack and synthetic set sizes, we performed two sets of ablation
studies. The corresponding results are provided in Appendix C. Our findings indicate that for small datasets such
as Compas and Heloc, relatively small attack set sizes of 200 to 400 instances are sufficient to achieve optimal
attack performance. For these datasets, a synthetic (counterfactual) set size of 500 to 1000 is required to optimize
the attack performance. For larger datasets, both a larger attack set and a higher number of counterfactuals
are necessary to optimize the attack. In particular, an attack dataset of 1000 instances is needed for adult and

Quantifying the Privacy of CFs by Leveraging MIA Against Synthetic Data FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
𝑎𝑐𝑠_𝑖𝑛𝑐𝑜𝑚𝑒 to obtain the most effective attack. For these datasets, the counterfactual set must contain 5000 to 10000
instances to reach the highest performance. Table 2 shows a sample of this ablation study for𝐴𝑐𝑠_𝑖𝑛𝑐𝑜𝑚𝑒 , showing
how increasing attack set size improves attack performance. More detailed results are presented in Appendix C.
Synth Size ROC AUCTPR@FPR.01 TPR@FPR.1PR AUC
500 0.505 0.011 0.103 0.505
1000 0.503 0.016 0.110 0.508
2000 0.502 0.016 0.113 0.510
5000 0.505 0.017 0.120 0.512
10000 0.506 0.016 0.117 0.512
Table 2.𝐴𝑐𝑠_𝐼𝑛𝑐𝑜𝑚𝑒- Fixed Attack Set Size 1000.
Having the results of the ablation study, to perform a MIA, we generated up to 10000 counterfactuals using
each method for instances in the counterfactual set explained in Section 1. For smaller datasets, such as Heloc
and Compas, which have fewer instances, both the synthetic and attack datasets are smaller since there are fewer
instances in the counterfactual set to generate counterfactuals, and fewer instances in the test set to be used
as non-members. For Compas, the synthetic dataset size is1443instances and the attack set size contains500
instances. Consequently, for Heloc, the attack set includes1995instances, while the attack set size maintains
the size of1000. To keep consistency and fair comparison, for the baseline attack,i.e., counterfactual distance
attack, the same attack set size of1000instances has been used to generate counterfactuals and perform the
attack. While the no-box ensemble attack has access to a reference set of 500 instances sampled from non-member
instances of the training distribution, the baseline counterfactual distance attack has additional access to the
model’s predictions and counterfactuals.
Counterfactual methods.We implemented four counterfactual mechanisms to generate counterfactuals. Since
our no-box attack is not limited to any synthetic data generation mechanism, we did not limit counterfactual
generation mechanisms as well. To be more precise, since various attacks are ensembled in our setting, each
individual attack can take advantage of some of the counterfactual generation mechanisms and their properties
and improve the ensemble results. Thus, we implemented various techniques to see how this attack works on
counterfactuals generated using each of them, without limiting the counterfactual methods used.
These generated counterfactuals are used in our no-box attack setting, in which the adversary, lacking access
to the original model, uses them as synthetic data to perform a membership inference attack. The counterfactual
mechanisms implemented are Nice, a representative of instance-based counterfactuals, Dice_gradient and SCFE,
representatives of perturbation-based counterfactuals, as well as Dice-kdtree, used as a sanity check since all
counterfactuals produced are members of the training dataset. The reason why we have implemented two
perturbation-based counterfactuals is their use of different encoding for feature values, which affects the final
counterfactuals generated. dice_gradient uses one-hot encoding for categorical features and standard scaler
for numerical features, with the tendency to perturb numerical features, while SCFE treats all features as
numerical values using standard scalers for them. Among counterfactual methods we used,𝑑𝑖𝑐𝑒_𝑔𝑟𝑎𝑑𝑖𝑒𝑛𝑡 has
the potential for setting various hyperparameters to prioritize different objectives, including proximity, diversity,
sparsity and actionability. The parameters used for the results presented in the main paper are as follows:
𝑝𝑟𝑜𝑥𝑖𝑚𝑖𝑡𝑦_𝑤𝑒𝑖𝑔ℎ𝑡 : 0.1,𝑑𝑖𝑣𝑒𝑟𝑠𝑖𝑡𝑦_𝑤𝑒𝑖𝑔ℎ𝑡 : 1.0and all features are allowed to change during the counterfactual
generation mechanism. This setting has been used to achieve fair results compared to the baseline attack, without
tailoring counterfactuals toward a more vulnerable setting to our no-box attack. The statistical analysis of
counterfactuals generated using each method is presented in Table 3.

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Babaei et al.
Dataset CF avg_distance±std avg_reid_rate±std success_rate
acs_income NICE 0.355±0.311 0.108±0.320 100.000
dice_gradient 0.783±0.398 0.000±0.000 99.967
dice_kdtree 1.104±0.476 1.011±0.125 100.000
scfe 0.538±0.623 0.000±0.000 99.999
adult NICE 0.922±0.848 0.760±1.302 100.000
dice_gradient 1.346±0.415 0.000±0.000 99.947
dice_kdtree 1.085±0.573 1.222±0.666 100.000
scfe 0.434±0.632 0.000±0.000 99.994
compas NICE 0.194±0.268 3.019±4.849 100.000
dice_gradient 0.824±0.315 0.001±0.042 99.945
dice_kdtree 0.388±0.456 3.451±3.710 99.945
scfe 0.014±0.071 0.000±0.000 100.000
heloc NICE 0.298±0.305 0.000±0.009 100.000
dice_gradient 1.132±0.315 0.000±0.000 100.000
dice_kdtree 0.841±0.471 0.810±0.391 100.000
scfe 0.073±0.168 0.000±0.000 91.635
Table 3. Counterfactuals statistic analysis across datasets and methods. 𝑎𝑣𝑔_𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒 is the average distance of generated
counterfactuals to the query instance,𝑎𝑣𝑔_𝑟𝑒𝑖𝑑_𝑟𝑎𝑡𝑒 shows the average number of exact matches existing in the training
dataset for each counterfactual.𝑠𝑢𝑐𝑐𝑒𝑠𝑠_𝑟𝑎𝑡𝑒 shows the percentage of queries for which the method successfully generated
a valid counterfactual.
Baseline attack.To evaluate the effectiveness of the ensemble-MIA attack designed for synthetic data, we
implemented the counterfactual distance attack [28], which relies on counterfactual distances and their distri-
butions for members and non-members to infer whether a target instance belongs to the training dataset. This
attack requires query access to the model, as the adversary must be able to request counterfactuals for query
instances to compute counterfactual distance and compare it with the distributions of distances generated by the
shadow models. Due to different operational requirements, we run this attack in a separate pipeline, using the
same datasets and the same counterfactual metrics. To the best of our knowledge, it remains the only MIA attack
implemented on counterfactuals generated for tabular datasets.
Evaluation metrics.To evaluate the performance of the attacks, we have used the following metrics in accordance
with the literature [7, 13, 15, 31, 33, 39]:
•Access level (white-box, black-box, no-box).
•Shadow models training required.
• TPR for fixed small FPR: True positive rate at low false positive rate, measuring the ability to correctly
identify members while maintaining a low false alarm rate.
•ROC AUC: The overall attack ability to distinguish members and non-members across all attack datasets,
independent of any decision threshold.
• Precision-Recall (PR) curve: Evaluates the trade-offs between successful member identification (proportion
of samples identified as members that are actually members) and overall attack coverage (proportion of
true members correctly identified).

Quantifying the Privacy of CFs by Leveraging MIA Against Synthetic Data FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
Dataset CF Attack ROC AUCTPR@FPR.01 TPR@FPR.1PR AUC
Compas Nice Ensemble 0.615 0.011 0.175 0.599
Dist Lrt 0.496 0.009 0.103 0.500
Compas dice_kdtree Ensemble 0.624 0.012 0.192 0.607
Dist Lrt 0.495 0.011 0.109 0.501
Compas gradient Ensemble 0.602 0.019 0.200 0.592
Dist Lrt0.652 0.023 0.328 0.643
Compas scfe Ensemble 0.694 0.029 0.337 0.683
Dist Lrt 0.572 0.010 0.144 0.551
Heloc Nice Ensemble 0.515 0.019 0.128 0.522
Dist Lrt 0.482 0.010 0.092 0.489
Heloc dice_kdtree Ensemble 0.534 0.047 0.164 0.555
Dist Lrt 0.481 0.015 0.111 0.501
Heloc gradient Ensemble 0.491 0.009 0.093 0.496
Dist Lrt 0.471 0.0060.0980.477
Heloc scfe Ensemble 0.495 0.009 0.095 0.498
Dist Lrt 0.472 0.004 0.093 0.476
Adult Nice Ensemble 0.514 0.017 0.134 0.524
Dist Lrt 0.497 0.011 0.104 0.502
Adult dice_kdtree Ensemble 0.509 0.031 0.131 0.527
Dist Lrt 0.495 0.014 0.101 0.503
Adult gradient Ensemble 0.512 0.011 0.116 0.511
Dist Lrt 0.490 0.011 0.097 0.492
Adult scfe Ensemble 0.513 0.007 0.120 0.512
Dist Lrt 0.4870.0090.062 0.479
Acs_income Nice Ensemble 0.511 0.015 0.115 0.512
Dist Lrt 0.506 0.011 0.105 0.500
Acs_income dice_kdtree Ensemble 0.510 0.017 0.121 0.519
Dist Lrt 0.497 0.014 0.094 0.499
Acs_income gradient Ensemble 0.505 0.018 0.112 0.511
Dist Lrt 0.504 0.013 0.108 0.510
Acs_income scfe Ensemble 0.513 0.013 0.107 0.515
Dist Lrt 0.496 0.002 0.061 0.476
Table 4. Comparison of counterfactual-based attacks. Results are averaged over five different random seeds. It is worth
mentioning that two differences between the Ensemble and Dist Lrt attacks are in the access level and shadow model training,
where the Ensemble attack is no-box with no access to the model or training data, and the Dist Lrt has query access to the
model and trains shadow models, which increases the complexity of the attack.
5.2 Experimental results
We evaluate the no-box ensemble MIA [39] (originally designed for synthetic data) against the counterfactual
distance attack (Dist-LRT) baseline [28], with both attacks run on a server with 12 GB of RAM. Figure 2 and Table 4
summarize the performance of both attacks.
Overall, the ensemble MIA is consistently stronger than Dist-LRT in nearly all settings, with the main exception
being dice_gradient on Compas. These results suggest that meaningful membership leakage can arise even without

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Babaei et al.
any model-query access when counterfactuals are released. More specifically, the ensemble MIA outperforms the
distance-based attack on instance-based counterfactuals (i.e., dice_kdtree and NICE). In contrast, both attacks
exhibit near-random-guess performance on perturbation-based methods (i.e., dice_gradient and SCFE), with
the ensemble MIA performing slightly better than the distance-based attack. This suggests that counterfactual
realism or proximity to training points increases vulnerability to MIAs tailored for synthetic data.
To support this claim, we performed a comparison of the distributions between the training and counterfactual
sets for all CF generation mechanisms, presented in Appendix A. This comparison shows that the member-
ship inference attack performs better when counterfactual distributions are more similar to the training set.
According to the distribution comparison, instance-based methods (i.e., 𝑑𝑖𝑐𝑒_𝑘𝑑𝑡𝑟𝑒𝑒 and NICE) generate CFs
with higher similarity to the train set, which makes them more vulnerable to MIAs against synthetic data. In
contrast, perturbation-based methods (i.e.,𝑑𝑖𝑐𝑒_𝑔𝑟𝑎𝑑𝑖𝑒𝑛𝑡 and SCFE) change the distribution and thus reduce the
performance of the ensemble attack.
We also conducted another set of experiments to evaluate the effect of proximity, diversity and actionability of
the counterfactuals to their vulnerability to the membership inference attack. By setting various hyperparameters
for𝑑𝑖𝑐𝑒_𝑔𝑟𝑎𝑑𝑖𝑒𝑛𝑡 , we generated counterfactuals with focus on each of these hyperparameters to investigate
how the attack performance changes. Table 5 provides a synthesized overview of these experiments, while
comprehensive results are reported in Appendix D. Overall, the results of these experiments show that:
• When no limitation on changeable features is applied, higher proximity slightly increases vulnerability to
membership inference attack when proximity increases from0.5to1, but increasing this hyperparameter
more than1reduces this vulnerability.
• Limiting the changeable features to the actionable features only increases vulnerability to the membership
inference attack for𝑎𝑐𝑠_𝑖𝑛𝑐𝑜𝑚𝑒 , while decreasing the vulnerability for datasets such as Compas with more
difficult classification tasks with higher dimensions.
CF ROC AUCTPR@FPR.01 TPR@FPR.1PR AUC
dice_gradient_pw0.5_dw0.1_ftv-all 0.502 0.010 0.106 0.506
dice_gradient_pw0.5_dw0.1_ftv_actionable 0.519 0.029 0.098 0.518
dice_gradient_pw0.5_dw0.5_ftv-all 0.502 0.010 0.106 0.506
dice_gradient_pw1_dw0.1_ftv_actionable 0.506 0.011 0.105 0.506
Table 5. 𝐴𝑐𝑠_𝐼𝑛𝑐𝑜𝑚𝑒 - evaluation of attack performance across various proximity/diversity/actionability settings for Dice
Gradient mechanisms.
Since the effect of various hyperparameter settings is not consistent among all datasets, we keep this direction
open for more investigations.
Another set of experiments we performed is the evaluation of the attack performance based on the distance to
the decision boundary. More precisely, we divided query instances into five different bins based on their distance
to the decision boundary. We used confidence score as a proxy for this distance [28, 30]. The more confident
the prediction is, the further the instance is from the decision boundary. As expected, our results show that the
membership inference attack is more successful for instances closer to the decision boundary. The results of
these experiments are provided in Appendix E Finally, we observe that attack performance is higher on smaller
datasets such as Compas and Heloc, which is consistent with prior evidence [32] that smaller datasets can yield
more memorization and thus higher MIA risk.
To explain why ensembling is more effective than individual attacks on counterfactuals in a no-box setting,
we investigated the effectiveness of the individual attacks on different datasets and counterfactual generation

Quantifying the Privacy of CFs by Leveraging MIA Against Synthetic Data FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
mechanisms, and compared their effectiveness with the ensemble attacks. The results (seeTable 6) show that,
while there are some individual attacks achieving higher performance compared to the ensembling for each
dataset and counterfactual generation mechanism, there is no special attack that performs best for all. For instance,
while distance-based attacks perform better when perturbation-based mechanisms like dice-gradient or SCFE
are used, in the case of using instance-based mechanisms like NICE or dice-kdtree, neighbourhood-based and
GAN-based attacks are more effective. The ensembling benefits from the most effective attacks in the no-box
setting, where no information is provided about the counterfactual generation mechanism or training data
distribution. Detailed results of individual attacks are presented in Appendix B.
Dataset Attack CF ROC AUCTPR@FPR.01 TPR@FPR.1PR AUC
Compas 𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=20 NICE 0.621 0.006 0.180 0.595
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=500.646 0.044 0.282 0.650
Heloc 𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=10 Dice_KDtree 0.550 0.040 0.204 0.577
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=200.544 0.034 0.194 0.569
Acs_income 𝐷𝐶𝑅_𝐷𝑖𝑓𝑓_𝐿 2 Dice_Gradient 0.504 0.013 0.114 0.513
𝐷𝐶𝑅_𝐿 2 0.484 0.006 0.095 0.489
Adult 𝐷𝐶𝑅_𝐿 2 SCFE 0.546 0.019 0.152 0.552
𝐷𝑂𝑀𝐼𝐴𝑆0.515 0.010 0.093 0.508
Table 6. Sample results of Individual attacks.
6 Conclusion
In this work, we evaluate the effectiveness of MIAs originally designed for synthetic data when applied to
counterfactual explanations. We have shown that successful MIAs are possible even without any access to the
model or knowledge of the counterfactual generation mechanism.
Our results demonstrate that even without access to the model, successful MIAs against counterfactuals are
possible, suggesting that practitioners should apply suitable privacy measures when generating counterfactuals.
In particular, ensemble MIA works in a no-box setting, which is a weaker adversary model, while achieving better
performance than the existing attacks targeting counterfactuals with query access to the model. For instance, we
achieve an improvement of 26% in Compas (dice-kdtree) which is significant enough to raise attention to the
privacy issue of releasing counterfactuals without privacy measures, even when no further information or access
is provided. Finally, our results also highlight that the attack is more effective on smaller datasets and on more
realistic counterfactuals. Moreover, adopting this no-box attack setting enables auditors to assess privacy leakage
in deployed models without requiring any access to the models themselves.
To prevent no-box MIAs, the model providers might consider using differential privacy [9] in counterfactual
generation mechanisms [16, 24, 29]. Another defense technique is to return prototypic instances for each class,
instead of generating query-specific counterfactuals. These techniques, by reducing the counterfactual set size
available to the adversary, will limit the potential for performing successful MIAs. One limitation of our work
is that even with the improvement of the membership inference attack performance using the no-box attack,
which is a stronger attack with weaker access, for some datasets and counterfactuals, the performance of the
attack is just slightly higher than a random guess. This low performance of the attack should not be mistaken for
guaranteed privacy. Privacy leakage can still exist, even when membership inference attacks fail. To guarantee the
privacy of data, practitioners should always consider implementing reliable countermeasures when generating
and releasing counterfactuals.

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Babaei et al.
No-box attack CF-distance-attack
Compas
Heloc
Adult
Acs Income
Fig. 2. Attack performance comparison. Blue lines show ROC curves fordice_gradient, green lines fordice_kdtree, orange
lines for NICE, and red lines for SCFE. While No-box attacks work better on instance-based counterfactuals, the counterfactual
distance attack is more accurate in the case of perturbation-based counterfactuals. Still, except for the Compas dataset, the
counterfactual distance attack performs a bit better than a random guess.
Acknowledgments
The authors acknowledge the support of the Digital Research Alliance of Canada (alliancecan.ca) and the advanced
research computing resources made available through its national computing infrastructure. Héber H. Arcolezi is
supported by the French National Research Agency (ANR) research grants (ANR-24-CE23-6239, ANR-23-IACL-
0006). Ulrich Aïvodji is supported by the Fonds de recherche du Québec – Nature et technologies (FRQNT) Team
Research Project grant (327090) and Natural Sciences and Engineering Research Council of Canada (NSERC)
Discovery grant (RGPIN-2022-04006). Sébastien Gambs is supported by the Canada Research Chair in Privacy-
preserving and Ethical Analysis of Big Data, FRQNT Team Project grant (327090) and NSERC Discovery grant
(RGPIN-2022-05031).

Quantifying the Privacy of CFs by Leveraging MIA Against Synthetic Data FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
References
[1] Ulrich Aïvodji, Alexandre Bolot, and Sébastien Gambs. 2020. Model extraction from counterfactual explanations.arXiv preprint
arXiv:2009.01884(2020).
[2] Julia Angwin, Jeff Larson, Surya Mattu, and Lauren Kirchner. 2016. Machine Bias: Risk Assessments in Criminal Sentencing. https:
//github.com/propublica/compas-analysis. Accessed 2025-05-15.
[3] Arthur Asuncion and David Newman. 2007. UCI machine learning repository.
[4] André Bauer, Simon Trapp, Michael Stenger, Robert Leppich, Samuel Kounev, Mark Leznik, Kyle Chard, and Ian Foster. 2024. Compre-
hensive exploration of synthetic data generation: A survey.arXiv preprint arXiv:2401.02524(2024).
[5] Brett K Beaulieu-Jones, Zhiwei Steven Wu, Chris Williams, Ran Lee, Sanjeev P Bhavnani, James Brian Byrd, and Casey S Greene. 2019.
Privacy-preserving generative deep neural networks support clinical data sharing.Circulation: Cardiovascular Quality and Outcomes12,
7 (2019), e005122.
[6] Dieter Brughmans, Pieter Leyman, and David Martens. 2023. Nice: an algorithm for nearest instance counterfactual explanations.Data
Mining and Knowledge Discovery(2023), 1–39.
[7] Dingfan Chen, Ning Yu, Yang Zhang, and Mario Fritz. 2020. Gan-leaks: A taxonomy of membership inference attacks against generative
models. InProceedings of the 2020 ACM SIGSAC conference on computer and communications security. 343–362.
[8] Pin-Yu Chen, Huan Zhang, Yash Sharma, Jinfeng Yi, and Cho-Jui Hsieh. 2017. Zoo: Zeroth order optimization based black-box attacks to
deep neural networks without training substitute models. InProceedings of the 10th ACM workshop on artificial intelligence and security.
15–26.
[9] Cynthia Dwork, Aaron Roth, et al. 2014. The algorithmic foundations of differential privacy.Foundations and Trends®in Theoretical
Computer Science9, 3–4 (2014), 211–407.
[10] Sofie Goethals, Kenneth Sörensen, and David Martens. 2023. The Privacy Issue of Counterfactual Explanations: Explanation Linkage
Attacks.ACM Trans. Intell. Syst. Technol.14, 5, Article 83 (aug 2023), 24 pages. doi:10.1145/3608482
[11] Ian J Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, and Yoshua Bengio.
2014. Generative adversarial nets.Advances in neural information processing systems27 (2014).
[12] Jamie Hayes, Luca Melis, George Danezis, and Emiliano De Cristofaro. 2017. Logan: Membership inference attacks against generative
models.arXiv preprint arXiv:1705.07663(2017).
[13] Benjamin Hilprecht, Martin Härterich, and Daniel Bernau. 2019. Monte carlo and reconstruction membership inference attacks against
generative models.Proceedings on Privacy Enhancing Technologies(2019).
[14] Florimond Houssiau, James Jordon, Samuel N Cohen, Owen Daniel, Andrew Elliott, James Geddes, Callum Mole, Camila Rangel-Smith,
and Lukasz Szpruch. 2022. TAPAS: a toolbox for adversarial privacy auditing of synthetic data.arXiv preprint arXiv:2211.06550(2022).
[15] Aoting Hu, Renjie Xie, Zhigang Lu, Aiqun Hu, and Minhui Xue. 2021. Tablegan-mca: Evaluating membership collisions of gan-synthesized
tabular data releasing. InProceedings of the 2021 ACM SIGSAC Conference on Computer and Communications Security. 2096–2112.
[16] Catherine Huang, Chelse Swoopes, Christina Xiao, Jiaqi Ma, and Himabindu Lakkaraju. 2023. Accurate, Explainable, and Private Models:
Providing Recourse While Minimizing Training Data Leakage.arXiv preprint arXiv:2308.04341(2023).
[17] Ling Huang, Anthony D Joseph, Blaine Nelson, Benjamin IP Rubinstein, and J Doug Tygar. 2011. Adversarial machine learning. In
Proceedings of the 4th ACM workshop on Security and artificial intelligence. 43–58.
[18] Amir-Hossein Karimi, Gilles Barthe, Bernhard Schölkopf, and Isabel Valera. 2022. A survey of algorithmic recourse: contrastive
explanations and consequential recommendations.Comput. Surveys55, 5 (2022), 1–29.
[19] Aditya Kuppa and Nhien-An Le-Khac. 2021. Adversarial XAI methods in cybersecurity.IEEE transactions on information forensics and
security16 (2021), 4924–4938.
[20] Thibault Laugel, Marie-Jeanne Lesot, Christophe Marsala, Xavier Renard, and Marcin Detyniecki. 2019. The dangers of post-hoc
interpretability: unjustified counterfactual explanations. InProceedings of the 28th International Joint Conference on Artificial Intelligence
(Macao, China)(IJCAI’19). 2801–2807.
[21] Ryan McKenna, Gerome Miklau, and Daniel Sheldon. 2021. Winning the nist contest: A scalable and general approach to differentially
private synthetic data.arXiv preprint arXiv:2108.04978(2021).
[22] Ryan McKenna, Brett Mullins, Daniel Sheldon, and Gerome Miklau. 2022. AIM: an adaptive and iterative mechanism for differentially
private synthetic data.Proc. VLDB Endow.15, 11 (July 2022), 2599–2612. doi:10.14778/3551793.3551817
[23] Ramaravind K Mothilal, Amit Sharma, and Chenhao Tan. 2020. Explaining machine learning classifiers through diverse counterfactual
explanations. InProceedings of the 2020 conference on fairness, accountability, and transparency. 607–617.
[24] DJ Nelson. 2022.Privacy-preserving counterfactual explanations to help humans contest AI-based decisions. Master’s thesis. University of
Twente.
[25] Sergey I Nikolenko et al. 2021.Synthetic data for deep learning. Vol. 174. Springer.
[26] OpenML. 2018. FICO-HELOC-cleaned Dataset. https://openml.org/d/45554. Accessed 2025-05-15.
[27] Art B. Owen. 2013.Monte Carlo theory, methods and examples. https://artowen.su.domains/mc/.

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Babaei et al.
[28] Martin Pawelczyk, Himabindu Lakkaraju, and Seth Neel. 2023. On the privacy risks of algorithmic recourse. InInternational Conference
on Artificial Intelligence and Statistics. PMLR, 9680–9696.
[29] Sikha Pentyala, Shubham Sharma, Sanjay Kariyappa, Freddy Lecue, and Daniele Magazzeni. 2023. Privacy-Preserving Algorithmic
Recourse.arXiv preprint arXiv:2311.14137(2023).
[30] Reza Shokri, Martin Strobel, and Yair Zick. 2021. On the privacy risks of model explanations. InProceedings of the 2021 AAAI/ACM
Conference on AI, Ethics, and Society. 231–241.
[31] Reza Shokri, Marco Stronati, Congzheng Song, and Vitaly Shmatikov. 2017. Membership inference attacks against machine learning
models. In2017 IEEE symposium on security and privacy (SP). IEEE, 3–18.
[32] Marlon Tobaben, Hibiki Ito, Joonas Jälkö, Yuan He, and Antti Honkela. 2025. Impact of Dataset Properties on Membership Inference
Vulnerability of Deep Transfer Learning. InAdvances in Neural Information Processing Systems, Vol. 38. 67486–67537.
[33] Boris van Breugel, Hao Sun, Zhaozhi Qian, and Mihaela van der Schaar. 2023. Membership Inference Attacks against Synthetic Data
through Overfitting Detection. InInternational Conference on Artificial Intelligence and Statistics. PMLR, 3493–3514.
[34] Giuseppe Vietri, Cedric Archambeau, Sergul Aydore, William Brown, Michael Kearns, Aaron Roth, Ankit Siva, Shuai Tang, and Steven Z
Wu. 2022. Private synthetic data for multitask learning and marginal queries.Advances in Neural Information Processing Systems35
(2022), 18282–18295.
[35] Sandra Wachter, Brent Mittelstadt, and Chris Russell. 2017. Counterfactual explanations without opening the black box: Automated
decisions and the GDPR.Harv. JL & Tech.31 (2017), 841.
[36] Yongjie Wang, Hangwei Qian, and Chunyan Miao. 2022. DualCF: Efficient Model Extraction Attack from Counterfactual Explanations.
In2022 ACM Conference on Fairness, Accountability, and Transparency. 1318–1329.
[37] Joshua Ward, Chi-Hua Wang, and Guang Cheng. 2024. Data plagiarism index: Characterizing the privacy risk of data-copying in tabular
generative models.arXiv preprint arXiv:2406.13012(2024).
[38] Joshua Ward, Chi-Hua Wang, and Guang Cheng. 2025. Privacy Auditing Synthetic Data Release through Local Likelihood Attacks.
arXiv preprint arXiv:2508.21146(2025).
[39] Joshua Ward, Yuxuan Yang, Chi-Hua Wang, and Guang Cheng. 2025. Ensembling Membership Inference Attacks Against Tabular
Generative Models. InProceedings of the 18th ACM Workshop on Artificial Intelligence and Security (AISec ’25). Association for Computing
Machinery, New York, NY, USA, 182–193. doi:10.1145/3733799.3762977
A Distribution comparison between real and counterfactual datasets
Comparing the distribution between the original and synthetic (Counterfactuals) datasets shows that the more
these two distributions match, the more effectively the attack performs.

Quantifying the Privacy of CFs by Leveraging MIA Against Synthetic Data FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
dice_kdtree
 Nice
dice_gradient
 scfe
Fig. 3. Acs_income – distribution_comparison between real dataset and counterfactual sets used to perform no-box ensemble
attack.

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Babaei et al.
dice_kdtree
 Nice
dice_gradient
 scfe
Fig. 4. Compas – distribution_comparison between real dataset and counterfactual sets used to perform no-box ensemble
attack.

Quantifying the Privacy of CFs by Leveraging MIA Against Synthetic Data FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
dice_kdtree
 Nice
dice_gradient
 scfe
Fig. 5. heloc – distribution_comparison between real dataset and counterfactual sets used to perform no-box ensemble
attack.

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Babaei et al.
dice_kdtree
 Nice
dice_gradient
 scfe
Fig. 6. adult – distribution_comparison between real dataset and counterfactual sets used to perform no-box ensemble
attack.

Quantifying the Privacy of CFs by Leveraging MIA Against Synthetic Data FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
B Individual attack results
In this section, the results of individual attacks on various counterfactual techniques are presented. These results
show that some individual attacks are working better than the ensemble attacks across datasets and counterfactual
generation mechanisms, but since the best attack is not the same for all datasets, or all counterfactual generation
techniques per dataset, in the no-box setting where the attacker has no information about the methods and data
distributions, they cannot decide on the best attack, and ensembling improves the average attack performance.

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Babaei et al.
Attack CF ROC AUCTPR@FPR.01 TPR@FPR.1PR AUC
𝐷𝐶𝑅_𝐷𝑖𝑓𝑓_𝐿 2 𝑁𝐼𝐶𝐸0.514 0.017 0.111 0.521
𝐷𝐶𝑅_𝐿 2 0.497 0.019 0.109 0.509
𝐷𝑂𝑀𝐼𝐴𝑆0.503 0.018 0.111 0.511
𝐷𝑃𝐼_𝐿 2_𝐾=10 0.509 0.011 0.105 0.507
𝐷𝑃𝐼_𝐿 2_𝐾=200.502 0.010 0.103 0.502
𝐺𝐸𝑁_𝐿𝑅𝐴_𝐾=1 0.505 0.008 0.120 0.510
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=100.509 0.014 0.118 0.513
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=20 0.508 0.010 0.117 0.512
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=500.506 0.008 0.108 0.508
𝐿𝑂𝐺𝐴𝑁 0.509 0.017 0.102 0.511
𝐷𝐶𝑅_𝐷𝑖𝑓𝑓_𝐿 2 𝐷𝑖𝑐𝑒_𝐺𝑟𝑎𝑑𝑖𝑒𝑛𝑡0.504 0.013 0.114 0.513
𝐷𝐶𝑅_𝐿 2 0.484 0.006 0.095 0.489
𝐷𝑂𝑀𝐼𝐴𝑆0.498 0.016 0.122 0.512
𝐷𝑃𝐼_𝐿 2_𝐾=10 0.501 0.011 0.107 0.504
𝐷𝑃𝐼_𝐿 2_𝐾=200.500 0.011 0.111 0.503
𝐺𝐸𝑁_𝐿𝑅𝐴_𝐾=1 0.496 0.015 0.106 0.509
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=100.499 0.014 0.119 0.511
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=20 0.499 0.017 0.112 0.511
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=500.502 0.016 0.113 0.513
𝐿𝑂𝐺𝐴𝑁 0.506 0.016 0.099 0.510
𝐷𝐶𝑅_𝐷𝑖𝑓𝑓_𝐿 2 𝐷𝑖𝑐𝑒_𝐾𝐷𝑇𝑟𝑒𝑒0.516 0.027 0.137 0.538
𝐷𝐶𝑅_𝐿 2 0.507 0.048 0.127 0.538
𝐷𝑂𝑀𝐼𝐴𝑆0.506 0.022 0.127 0.527
𝐷𝑃𝐼_𝐿 2_𝐾=10 0.502 0.010 0.104 0.503
𝐷𝑃𝐼_𝐿 2_𝐾=200.498 0.010 0.103 0.501
𝐺𝐸𝑁_𝐿𝑅𝐴_𝐾=1 0.510 0.015 0.136 0.524
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=100.506 0.018 0.129 0.520
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=20 0.504 0.017 0.124 0.516
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=500.502 0.018 0.107 0.509
𝐿𝑂𝐺𝐴𝑁 0.507 0.016 0.117 0.514
𝐷𝐶𝑅_𝐷𝑖𝑓𝑓_𝐿 2 𝑆𝐶𝐹𝐸0.514 0.018 0.116 0.519
𝐷𝐶𝑅_𝐿 2 0.490 0.014 0.102 0.499
𝐷𝑂𝑀𝐼𝐴𝑆0.507 0.015 0.122 0.516
𝐷𝑃𝐼_𝐿 2_𝐾=10 0.507 0.010 0.105 0.505
𝐷𝑃𝐼_𝐿 2_𝐾=200.501 0.010 0.105 0.503
𝐺𝐸𝑁_𝐿𝑅𝐴_𝐾=1 0.502 0.012 0.123 0.510
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=100.506 0.014 0.109 0.512
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=20 0.504 0.013 0.118 0.510
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=500.505 0.010 0.111 0.508
𝐿𝑂𝐺𝐴𝑁 0.509 0.016 0.116 0.515
Table 7. Individual attack results for𝐴𝑐𝑠_𝐼𝑛𝑐𝑜𝑚𝑒

Quantifying the Privacy of CFs by Leveraging MIA Against Synthetic Data FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
Attack CF ROC AUCTPR@FPR.01 TPR@FPR.1PR AUC
𝐷𝐶𝑅_𝐷𝑖𝑓𝑓_𝐿 2 𝑁𝐼𝐶𝐸0.497 0.016 0.106 0.509
𝐷𝐶𝑅_𝐿 2 0.537 0.057 0.161 0.563
𝐷𝑂𝑀𝐼𝐴𝑆0.525 0.015 0.137 0.529
𝐷𝑃𝐼_𝐿 2_𝐾=10 0.501 0.011 0.105 0.504
𝐷𝑃𝐼_𝐿 2_𝐾=200.506 0.011 0.109 0.507
𝐺𝐸𝑁_𝐿𝑅𝐴_𝐾=1 0.496 0.013 0.090 0.494
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=100.499 0.012 0.087 0.494
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=20 0.502 0.010 0.087 0.497
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=500.508 0.014 0.088 0.503
𝐿𝑂𝐺𝐴𝑁 0.456 0.011 0.090 0.477
𝐷𝐶𝑅_𝐷𝑖𝑓𝑓_𝐿 2 𝐷𝑖𝑐𝑒_𝐺𝑟𝑎𝑑𝑖𝑒𝑛𝑡0.508 0.013 0.106 0.510
𝐷𝐶𝑅_𝐿 2 0.544 0.030 0.150 0.555
𝐷𝑂𝑀𝐼𝐴𝑆0.527 0.013 0.127 0.528
𝐷𝑃𝐼_𝐿 2_𝐾=10 0.515 0.011 0.111 0.513
𝐷𝑃𝐼_𝐿 2_𝐾=200.514 0.011 0.106 0.512
𝐺𝐸𝑁_𝐿𝑅𝐴_𝐾=1 0.500 0.008 0.077 0.491
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=100.498 0.009 0.072 0.489
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=20 0.496 0.007 0.076 0.489
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=500.501 0.008 0.078 0.493
𝐿𝑂𝐺𝐴𝑁 0.460 0.013 0.093 0.481
𝐷𝐶𝑅_𝐷𝑖𝑓𝑓_𝐿 2 𝐷𝑖𝑐𝑒_𝐾𝐷𝑇𝑟𝑒𝑒0.500 0.027 0.130 0.526
𝐷𝐶𝑅_𝐿 2 0.547 0.082 0.161 0.580
𝐷𝑂𝑀𝐼𝐴𝑆0.521 0.022 0.124 0.529
𝐷𝑃𝐼_𝐿 2_𝐾=10 0.490 0.011 0.105 0.500
𝐷𝑃𝐼_𝐿 2_𝐾=200.495 0.011 0.112 0.504
𝐺𝐸𝑁_𝐿𝑅𝐴_𝐾=1 0.494 0.018 0.099 0.502
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=100.495 0.015 0.095 0.500
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=20 0.495 0.015 0.098 0.500
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=500.503 0.013 0.096 0.503
𝐿𝑂𝐺𝐴𝑁 0.464 0.014 0.092 0.483
𝐷𝐶𝑅_𝐷𝑖𝑓𝑓_𝐿 2 𝑆𝐶𝐹𝐸0.477 0.008 0.080 0.480
𝐷𝐶𝑅_𝐿 2 0.546 0.019 0.152 0.552
𝐷𝑂𝑀𝐼𝐴𝑆0.515 0.010 0.093 0.508
𝐷𝑃𝐼_𝐿 2_𝐾=10 0.503 0.010 0.102 0.503
𝐷𝑃𝐼_𝐿 2_𝐾=200.511 0.011 0.105 0.507
𝐺𝐸𝑁_𝐿𝑅𝐴_𝐾=1 0.451 0.007 0.073 0.466
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=100.465 0.009 0.082 0.475
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=20 0.477 0.008 0.085 0.482
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=500.499 0.010 0.094 0.497
𝐿𝑂𝐺𝐴𝑁 0.452 0.010 0.090 0.474
Table 8. Individual attack results for Adult.

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Babaei et al.
Attack CF ROC AUCTPR@FPR.01 TPR@FPR.1PR AUC
𝐷𝐶𝑅_𝐷𝑖𝑓𝑓_𝐿 2 𝑁𝐼𝐶𝐸0.607 0.013 0.146 0.579
𝐷𝐶𝑅_𝐿 2 0.642 0.055 0.240 0.638
𝐷𝑂𝑀𝐼𝐴𝑆0.634 0.067 0.272 0.649
𝐷𝑃𝐼_𝐿 2_𝐾=10 0.626 0.022 0.224 0.609
𝐷𝑃𝐼_𝐿 2_𝐾=200.641 0.036 0.292 0.638
𝐺𝐸𝑁_𝐿𝑅𝐴_𝐾=1 0.585 0.012 0.086 0.542
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=100.605 0.007 0.139 0.571
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=20 0.621 0.006 0.180 0.595
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=500.646 0.044 0.282 0.650
𝐿𝑂𝐺𝐴𝑁 0.357 0.006 0.050 0.413
𝐷𝐶𝑅_𝐷𝑖𝑓𝑓_𝐿 2 𝐷𝑖𝑐𝑒_𝐺𝑟𝑎𝑑𝑖𝑒𝑛𝑡0.595 0.018 0.162 0.576
𝐷𝐶𝑅_𝐿 2 0.621 0.051 0.206 0.619
𝐷𝑂𝑀𝐼𝐴𝑆0.571 0.006 0.098 0.537
𝐷𝑃𝐼_𝐿 2_𝐾=10 0.572 0.026 0.178 0.566
𝐷𝑃𝐼_𝐿 2_𝐾=200.595 0.019 0.177 0.583
𝐺𝐸𝑁_𝐿𝑅𝐴_𝐾=1 0.541 0.003 0.114 0.531
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=100.541 0.007 0.100 0.525
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=20 0.521 0.007 0.086 0.510
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=500.519 0.008 0.060 0.505
𝐿𝑂𝐺𝐴𝑁 0.418 0.005 0.052 0.440
𝐷𝐶𝑅_𝐷𝑖𝑓𝑓_𝐿 2 𝐷𝑖𝑐𝑒_𝐾𝐷𝑇𝑟𝑒𝑒0.640 0.010 0.302 0.641
𝐷𝐶𝑅_𝐿 2 0.660 0.226 0.339 0.708
𝐷𝑂𝑀𝐼𝐴𝑆0.645 0.068 0.350 0.681
𝐷𝑃𝐼_𝐿 2_𝐾=10 0.639 0.033 0.316 0.639
𝐷𝑃𝐼_𝐿 2_𝐾=200.652 0.045 0.322 0.657
𝐺𝐸𝑁_𝐿𝑅𝐴_𝐾=1 0.613 0.008 0.160 0.576
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=100.640 0.002 0.268 0.618
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=20 0.653 0.022 0.302 0.647
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=500.670 0.048 0.332 0.679
𝐿𝑂𝐺𝐴𝑁 0.340 0.004 0.056 0.413
𝐷𝐶𝑅_𝐷𝑖𝑓𝑓_𝐿 2 𝑆𝐶𝐹𝐸0.587 0.005 0.082 0.531
𝐷𝐶𝑅_𝐿 2 0.697 0.070 0.347 0.704
𝐷𝑂𝑀𝐼𝐴𝑆0.691 0.006 0.307 0.658
𝐷𝑃𝐼_𝐿 2_𝐾=10 0.683 0.032 0.316 0.655
𝐷𝑃𝐼_𝐿 2_𝐾=200.699 0.056 0.372 0.690
𝐺𝐸𝑁_𝐿𝑅𝐴_𝐾=1 0.508 0.007 0.053 0.483
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=100.603 0.008 0.110 0.559
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=20 0.652 0.006 0.206 0.611
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=500.690 0.025 0.341 0.677
𝐿𝑂𝐺𝐴𝑁 0.352 0.008 0.050 0.415
Table 9. Individual attack results for𝐶𝑜𝑚𝑝𝑎𝑠.

Quantifying the Privacy of CFs by Leveraging MIA Against Synthetic Data FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
Attack CF ROC AUCTPR@FPR.01 TPR@FPR.1PR AUC
𝐷𝐶𝑅_𝐷𝑖𝑓𝑓_𝐿 2 𝑁𝐼𝐶𝐸0.512 0.032 0.131 0.529
𝐷𝐶𝑅_𝐿 2 0.520 0.023 0.108 0.527
𝐷𝑂𝑀𝐼𝐴𝑆0.503 0.016 0.108 0.512
𝐷𝑃𝐼_𝐿 2_𝐾=10 0.495 0.012 0.108 0.501
𝐷𝑃𝐼_𝐿 2_𝐾=200.491 0.011 0.105 0.498
𝐺𝐸𝑁_𝐿𝑅𝐴_𝐾=1 0.515 0.021 0.139 0.527
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=100.514 0.016 0.126 0.523
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=20 0.515 0.017 0.119 0.519
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=500.512 0.014 0.113 0.513
𝐿𝑂𝐺𝐴𝑁 0.498 0.011 0.103 0.502
𝐷𝐶𝑅_𝐷𝑖𝑓𝑓_𝐿 2 𝐷𝑖𝑐𝑒_𝐺𝑟𝑎𝑑𝑖𝑒𝑛𝑡0.481 0.013 0.098 0.493
𝐷𝐶𝑅_𝐿 2 0.492 0.008 0.103 0.497
𝐷𝑂𝑀𝐼𝐴𝑆0.483 0.011 0.094 0.491
𝐷𝑃𝐼_𝐿 2_𝐾=10 0.475 0.009 0.085 0.485
𝐷𝑃𝐼_𝐿 2_𝐾=200.480 0.010 0.093 0.488
𝐺𝐸𝑁_𝐿𝑅𝐴_𝐾=1 0.505 0.011 0.102 0.505
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=100.498 0.007 0.102 0.501
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=20 0.496 0.010 0.101 0.498
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=500.495 0.006 0.094 0.494
𝐿𝑂𝐺𝐴𝑁 0.502 0.013 0.103 0.504
𝐷𝐶𝑅_𝐷𝑖𝑓𝑓_𝐿 2 𝐷𝑖𝑐𝑒_𝐾𝐷𝑇𝑟𝑒𝑒0.539 0.150 0.213 0.611
𝐷𝐶𝑅_𝐿 2 0.546 0.148 0.205 0.612
𝐷𝑂𝑀𝐼𝐴𝑆0.542 0.117 0.206 0.602
𝐷𝑃𝐼_𝐿 2_𝐾=10 0.492 0.011 0.106 0.499
𝐷𝑃𝐼_𝐿 2_𝐾=200.488 0.012 0.111 0.499
𝐺𝐸𝑁_𝐿𝑅𝐴_𝐾=1 0.543 0.079 0.212 0.597
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=100.550 0.040 0.204 0.577
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=20 0.544 0.034 0.194 0.569
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=500.532 0.027 0.176 0.556
𝐿𝑂𝐺𝐴𝑁 0.497 0.015 0.103 0.500
𝐷𝐶𝑅_𝐷𝑖𝑓𝑓_𝐿 2 𝑆𝐶𝐹𝐸0.507 0.011 0.093 0.504
𝐷𝐶𝑅_𝐿 2 0.509 0.013 0.106 0.507
𝐷𝑂𝑀𝐼𝐴𝑆0.505 0.009 0.100 0.504
𝐷𝑃𝐼_𝐿 2_𝐾=10 0.502 0.009 0.093 0.500
𝐷𝑃𝐼_𝐿 2_𝐾=200.494 0.010 0.098 0.499
𝐺𝐸𝑁_𝐿𝑅𝐴_𝐾=1 0.510 0.010 0.100 0.509
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=100.505 0.012 0.114 0.508
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=20 0.503 0.014 0.111 0.507
𝐺𝐸𝑁_𝑙𝑟𝑎_𝐾=500.507 0.012 0.114 0.510
𝐿𝑂𝐺𝐴𝑁 0.495 0.010 0.101 0.499
Table 10. Individual attack results for𝐻𝑒𝑙𝑜𝑐.

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Babaei et al.
C Ablation study results
To evaluate the effectiveness of the no-box attack when the size of the synthetic data is small, we performed
an ablation study over various synthetic set-attack set sizes. Two groups of experiments have been executed:
First, by keeping the size fixed of the synthetic dataset (counterfactuals), we evaluated the effectiveness of the
no-box attack on varying attack set sizes, changing from 200 to 2000 instances (except for the Compas dataset
that is the smallest dataset in our experiment, both synthetic and attack set sizes for the experiments regarding
this dataset are small as well). This study shows that for small datasets like Compas and Heloc, having an attack
dataset as small as 200 instances can result in the best attack performance for most counterfactual methods. For
larger datasets like𝑎𝑐𝑠_𝑖𝑛𝑐𝑜𝑚𝑒and adult, attack set sizes of 1000 and 2000 can result in more accurate attacks.
CF Attack Set Size ROC AUCTPR@FPR.01 TPR@FPR.1PR AUC
𝑁𝐼𝐶𝐸200 0.490 0.015 0.087 0.507
400 0.504 0.022 0.102 0.513
1000 0.495 0.013 0.096 0.501
2000 0.509 0.011 0.107 0.510
𝐷𝑖𝑐𝑒_𝐺𝑟𝑎𝑑𝑖𝑒𝑛𝑡200 0.500 0.023 0.101 0.523
400 0.482 0.010 0.078 0.497
1000 0.495 0.017 0.122 0.512
2000 0.506 0.016 0.117 0.512
𝐷𝑖𝑐𝑒_𝐾−𝐷𝑇𝑟𝑒𝑒200 0.507 0.012 0.107 0.521
400 0.503 0.030 0.117 0.523
1000 0.507 0.026 0.118 0.519
2000 0.510 0.024 0.128 0.523
𝑆𝐶𝐹𝐸200 0.479 0.008 0.098 0.502
400 0.501 0.021 0.111 0.514
1000 0.495 0.015 0.109 0.505
2000 0.510 0.014 0.108 0.509
Table 11. Acs_Income - Fixed Synth Size 10000.

Quantifying the Privacy of CFs by Leveraging MIA Against Synthetic Data FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
CF Attack Set Size ROC AUCTPR@FPR.01 TPR@FPR.1PR AUC
𝑁𝐼𝐶𝐸200 0.510 0.010 0.106 0.523
400 0.499 0.008 0.080 0.501
1000 0.510 0.008 0.082 0.505
2000 0.506 0.008 0.088 0.504
𝐷𝑖𝑐𝑒_𝐺𝑟𝑎𝑑𝑖𝑒𝑛𝑡200 0.522 0.007 0.130 0.537
400 0.502 0.006 0.089 0.507
1000 0.515 0.008 0.102 0.514
2000 0.515 0.008 0.101 0.512
𝐷𝑖𝑐𝑒_𝐾−𝐷𝑇𝑟𝑒𝑒200 0.525 0.014 0.126 0.536
400 0.517 0.013 0.117 0.522
1000 0.525 0.012 0.109 0.520
2000 0.506 0.013 0.112 0.509
𝑆𝐶𝐹𝐸200 0.478 0.010 0.103 0.495
400 0.491 0.012 0.081 0.489
1000 0.495 0.010 0.096 0.497
2000 0.488 0.008 0.083 0.488
Table 12. Adult - Fixed Synth Size 10000.
CF Attack Set Size ROC AUCTPR@FPR.01 TPR@FPR.1PR AUC
𝑁𝐼𝐶𝐸200 0.615 0.010 0.164 0.604
400 0.610 0.022 0.221 0.610
1000 0.616 0.011 0.177 0.601
𝐷𝑖𝑐𝑒_𝐺𝑟𝑎𝑑𝑖𝑒𝑛𝑡 200 0.609 0.033 0.213 0.607
400 0.607 0.018 0.218 0.600
1000 0.603 0.024 0.204 0.593
𝐷𝑖𝑐𝑒_𝐾−𝐷𝑇𝑟𝑒𝑒200 0.685 0.047 0.351 0.667
400 0.617 0.014 0.235 0.618
1000 0.618 0.008 0.180 0.606
𝑆𝐶𝐹𝐸 200 0.680 0.052 0.302 0.665
400 0.674 0.021 0.301 0.657
1000 0.694 0.026 0.336 0.684
Table 13. Compas - Fixed Synth Size 2000.

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Babaei et al.
CF Attack Set Size ROC AUCTPR@FPR.01 TPR@FPR.1PR AUC
𝑁𝐼𝐶𝐸200 0.509 0.031 0.162 0.539
400 0.481 0.016 0.090 0.492
1000 0.506 0.020 0.120 0.517
2000 0.513 0.021 0.126 0.522
𝐷𝑖𝑐𝑒_𝐺𝑟𝑎𝑑𝑖𝑒𝑛𝑡200 0.474 0.036 0.130 0.521
400 0.497 0.017 0.099 0.509
1000 0.502 0.010 0.123 0.509
2000 0.486 0.009 0.091 0.494
𝐷𝑖𝑐𝑒_𝐾−𝐷𝑇𝑟𝑒𝑒200 0.549 0.146 0.212 0.596
400 0.506 0.086 0.168 0.548
1000 0.531 0.067 0.165 0.563
2000 0.537 0.060 0.175 0.564
𝑆𝐶𝐹𝐸200 0.515 0.039 0.141 0.542
400 0.476 0.026 0.086 0.500
1000 0.507 0.012 0.100 0.508
2000 0.496 0.008 0.097 0.498
Table 14. Heloc - Fixed Synth Size 10000.

Quantifying the Privacy of CFs by Leveraging MIA Against Synthetic Data FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
The other ablation study we performed fixed the attack set size and varied the synthetic data size to evaluate
how many counterfactuals are needed to perform a successful no-box attack. These results show that while for
larger datasets like𝐴𝑐𝑠_𝑖𝑛𝑐𝑜𝑚𝑒 and Adult, the synthetic set size of 5000 to 10000 instances maximizes the attack
performance, for smaller datasets like Compas and Heloc, a synthetic set size of 500 to 1000 instances is enough
for the adversary user to perform a successful attack.
CF Synth Size ROC AUCTPR@FPR.01 TPR@FPR.1PR AUC
𝑁𝐼𝐶𝐸500 0.507 0.013 0.101 0.506
1000 0.508 0.013 0.101 0.508
2000 0.503 0.013 0.103 0.506
5000 0.508 0.013 0.100 0.506
10000 0.509 0.011 0.107 0.510
𝐷𝑖𝑐𝑒_𝐺𝑟𝑎𝑑𝑖𝑒𝑛𝑡 500 0.505 0.011 0.103 0.505
1000 0.503 0.016 0.110 0.508
2000 0.502 0.016 0.113 0.510
5000 0.505 0.017 0.120 0.512
10000 0.506 0.016 0.117 0.512
𝐷𝑖𝑐𝑒_𝐾−𝐷𝑇𝑟𝑒𝑒500 0.505 0.013 0.105 0.505
1000 0.505 0.016 0.111 0.508
2000 0.507 0.014 0.112 0.510
5000 0.511 0.022 0.113 0.516
10000 0.510 0.024 0.128 0.523
𝑆𝐶𝐹𝐸 500 0.510 0.014 0.122 0.511
1000 0.503 0.013 0.105 0.506
2000 0.504 0.016 0.106 0.508
5000 0.511 0.015 0.104 0.510
10000 0.510 0.014 0.108 0.509
Table 15.𝐴𝑐𝑠_𝐼𝑛𝑐𝑜𝑚𝑒- Fixed Attack Set Size 1000.

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Babaei et al.
CF Synth Size ROC AUCTPR@FPR.01 TPR@FPR.1PR AUC
𝑁𝐼𝐶𝐸500 0.516 0.008 0.100 0.514
1000 0.517 0.009 0.100 0.513
2000 0.514 0.008 0.094 0.510
5000 0.510 0.009 0.090 0.507
10000 0.506 0.008 0.088 0.504
𝐷𝑖𝑐𝑒_𝐺𝑟𝑎𝑑𝑖𝑒𝑛𝑡 500 0.517 0.009 0.097 0.513
1000 0.516 0.009 0.101 0.513
2000 0.518 0.008 0.101 0.513
5000 0.518 0.009 0.100 0.512
10000 0.515 0.008 0.101 0.512
𝐷𝑖𝑐𝑒_𝐾−𝐷𝑇𝑟𝑒𝑒500 0.517 0.011 0.110 0.517
1000 0.513 0.009 0.104 0.512
2000 0.507 0.010 0.105 0.509
5000 0.509 0.013 0.109 0.511
10000 0.506 0.013 0.112 0.509
𝑆𝐶𝐹𝐸 500 0.524 0.007 0.086 0.514
1000 0.524 0.008 0.109 0.517
2000 0.520 0.008 0.093 0.510
5000 0.500 0.008 0.087 0.495
10000 0.488 0.008 0.083 0.488
Table 16. Adult - Fixed Attack Set Size 1000.

Quantifying the Privacy of CFs by Leveraging MIA Against Synthetic Data FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
CF Synth Size ROC AUC𝑇𝑃𝑅@𝐹𝑃𝑅.01𝑇𝑃𝑅@𝐹𝑃𝑅.1PR AUC
𝑁𝐼𝐶𝐸500 0.626 0.013 0.201 0.609
1000 0.618 0.012 0.184 0.601
2000 0.616 0.011 0.177 0.601
5000 0.615 0.011 0.176 0.600
10000 0.616 0.010 0.176 0.600
𝐷𝑖𝑐𝑒_𝐺𝑟𝑎𝑑𝑖𝑒𝑛𝑡 500 0.619 0.017 0.179 0.594
1000 0.612 0.020 0.219 0.602
2000 0.603 0.024 0.204 0.593
5000 0.603 0.019 0.202 0.593
10000 0.602 0.020 0.201 0.592
𝐷𝑖𝑐𝑒_𝐾−𝐷𝑇𝑟𝑒𝑒500 0.609 0.009 0.200 0.611
1000 0.620 0.008 0.188 0.611
2000 0.618 0.008 0.180 0.606
5000 0.617 0.005 0.178 0.606
10000 0.620 0.011 0.200 0.610
𝑆𝐶𝐹𝐸 500 0.706 0.024 0.396 0.701
1000 0.697 0.031 0.357 0.689
2000 0.694 0.026 0.336 0.684
5000 0.694 0.027 0.336 0.683
10000 0.695 0.030 0.335 0.684
Table 17. Compas - Fixed Attack Set Size 500.

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Babaei et al.
CF Synth Size ROC AUCTPR@FPR.01 TPR@FPR.1PR AUC
𝑁𝐼𝐶𝐸500 0.500 0.012 0.105 0.506
1000 0.511 0.019 0.123 0.516
2000 0.512 0.021 0.126 0.522
5000 0.512 0.021 0.126 0.522
10000 0.513 0.021 0.126 0.522
𝐷𝑖𝑐𝑒_𝐺𝑟𝑎𝑑𝑖𝑒𝑛𝑡 500 0.487 0.009 0.091 0.492
1000 0.491 0.009 0.097 0.496
2000 0.486 0.009 0.090 0.494
5000 0.486 0.008 0.090 0.494
10000 0.486 0.009 0.091 0.494
𝐷𝑖𝑐𝑒_𝐾−𝐷𝑇𝑟𝑒𝑒500 0.519 0.050 0.147 0.542
1000 0.536 0.055 0.170 0.557
2000 0.537 0.061 0.175 0.564
5000 0.537 0.060 0.175 0.564
10000 0.537 0.060 0.175 0.564
𝑆𝐶𝐹𝐸 500 0.505 0.011 0.116 0.507
1000 0.502 0.010 0.102 0.503
2000 0.496 0.009 0.097 0.498
5000 0.496 0.008 0.097 0.498
10000 0.496 0.008 0.097 0.498
Table 18. Heloc - Fixed Attack Set Size 1000.

Quantifying the Privacy of CFs by Leveraging MIA Against Synthetic Data FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
D Evaluating the effects of Proximity, Diversity and Actionability on No-box attack performance
To study in more detail how counterfactual properties affect the attack performance, we generated various
versions of the dice attack using different settings for Proximity, Diversity, and Actionability. For proximity and
diversity variation, we implemented 9 different combinations of proximity/diversity weights in the dice explainer
setting:
•𝑃𝑟𝑜𝑥𝑖𝑚𝑖𝑡𝑦_𝑤𝑒𝑖𝑔ℎ𝑡∈(.5,1,2).
•𝐷𝑖𝑣𝑒𝑟𝑠𝑖𝑡𝑦_𝑤𝑒𝑖𝑔ℎ𝑡∈(.1,.5,1).
To address Actionability, we applied the limitation feature_to_vary in the dice setting. First, we allowed all feature
values to change when generating counterfactuals. In the second set of experiments, we limited dice to only
change numerical features. Results of these experiments are presented in tables 19, 20.
CF ROC AUCTPR@FPR.01 TPR@FPR.1PR AUC
dice_gradient_pw0.5_dw0.1_ftv-all 0.502 0.010 0.106 0.506
dice_gradient_pw0.5_dw0.1_ftv_actionable 0.519 0.029 0.098 0.518
dice_gradient_pw0.5_dw0.5_ftv-all 0.502 0.010 0.106 0.506
dice_gradient_pw0.5_dw0.5_ftv_actionable 0.520 0.029 0.098 0.519
dice_gradient_pw0.5_dw1_ftv-all 0.502 0.010 0.106 0.506
dice_gradient_pw0.5_dw1_ftv_actionable 0.520 0.029 0.098 0.519
dice_gradient_pw1_dw0.1_ftv-all 0.509 0.015 0.116 0.512
dice_gradient_pw1_dw0.1_ftv_actionable 0.506 0.011 0.105 0.506
dice_gradient_pw1_dw0.5_ftv-all 0.509 0.015 0.116 0.512
dice_gradient_pw1_dw0.5_ftv_actionable 0.494 0.016 0.098 0.503
dice_gradient_pw1_dw1_ftv-all 0.502 0.0150.1160.508
dice_gradient_pw1_dw1_ftv_actionable 0.495 0.017 0.111 0.508
dice_gradient_pw2_dw0.1_ftv-all 0.496 0.015 0.101 0.504
dice_gradient_pw2_dw0.1_ftv_actionable 0.496 0.010 0.098 0.502
dice_gradient_pw2_dw0.5_ftv-all 0.496 0.012 0.105 0.504
dice_gradient_pw2_dw0.5_ftv_actionable 0.497 0.010 0.098 0.502
dice_gradient_pw2_dw1_ftv-all 0.496 0.011 0.105 0.504
dice_gradient_pw2_dw1_ftv_actionable 0.496 0.010 0.098 0.502
Table 19. 𝐴𝑐𝑠_𝐼𝑛𝑐𝑜𝑚𝑒 - evaluation of attack performance across various proximity/diversity/actionability settings for Dice
Gradient mechanisms.

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Babaei et al.
CF ROC AUCTPR@FPR.01 TPR@FPR.1PR AUC
dice_gradient_pw0.5_dw0.1_ftv-all 0.602 0.016 0.231 0.601
dice_gradient_pw0.5_dw0.1_ftv_actionable 0.563 0.008 0.119 0.543
dice_gradient_pw0.5_dw0.5_ftv-all 0.602 0.016 0.230 0.601
dice_gradient_pw0.5_dw0.5_ftv_actionable 0.566 0.009 0.121 0.544
dice_gradient_pw0.5_dw1_ftv-all 0.603 0.017 0.229 0.601
dice_gradient_pw0.5_dw1_ftv_actionable 0.569 0.009 0.126 0.548
dice_gradient_pw1_dw0.1_ftv-all 0.620 0.0230.2830.626
dice_gradient_pw1_dw0.1_ftv_actionable 0.585 0.010 0.142 0.563
dice_gradient_pw1_dw0.5_ftv-all0.6210.0230.283 0.626
dice_gradient_pw1_dw0.5_ftv_actionable 0.585 0.010 0.142 0.563
dice_gradient_pw1_dw1_ftv-all 0.6200.0240.2830.626
dice_gradient_pw1_dw1_ftv_actionable 0.585 0.010 0.142 0.563
dice_gradient_pw2_dw0.1_ftv-all 0.619 0.020 0.264 0.620
dice_gradient_pw2_dw0.1_ftv_actionable 0.592 0.013 0.142 0.567
dice_gradient_pw2_dw0.5_ftv-all 0.619 0.020 0.264 0.620
dice_gradient_pw2_dw0.5_ftv_actionable 0.592 0.013 0.142 0.567
dice_gradient_pw2_dw1_ftv-all 0.619 0.020 0.265 0.620
dice_gradient_pw2_dw1_ftv_actionable 0.592 0.012 0.141 0.567
Table 20. 𝐶𝑜𝑚𝑝𝑎𝑠 - evaluation of attack performance across various proximity/diversity/actionability settings for Dice
Gradient mechanisms.
E Attack analysis based on distance to the decision boundary
To evaluate the effectiveness of the no-box attack regarding distance to the decision boundary, we performed
some extra experiments. In this set of experiments, we divided input instances into five bins and generated
counterfactuals for each bin. Then, the attack was performed following the setting explained in the main body of
the paper on each bin. To measure the distance to the decision boundary, we used confidence score as a proxy for
distance to the decision boundary [30]. This way, the higher the confidence score is, the further the instance is
from the decision boundary. Table 21 illustrates the results of these experiments for𝐴𝐶𝑆_𝑖𝑛𝑐𝑜𝑚𝑒 using NICE and
𝑑𝑖𝑐𝑒_𝑔𝑟𝑎𝑑𝑖𝑒𝑛𝑡 counterfactual generation mechanisms. These results show that by increasing the confidence score
(which means more distant instances from the decision boundary), the attack success rate slightly decreases,
which complies with the expectations according to the existing studies [28, 30].

Quantifying the Privacy of CFs by Leveraging MIA Against Synthetic Data FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
CF Confidence Bin ROC AUCTPR@FPR.01 TPR@FPR.1PR AUC
NICE 50-60 0.509 0.006 0.102 0.506
60-70 0.511 0.011 0.095 0.505
70-80 0.508 0.0120.1110.512
80-90 0.510 0.016 0.111 0.512
90-100 0.494 0.008 0.102 0.500
dice_gradient 50-60 0.510 0.014 0.104 0.509
60-70 0.500 0.015 0.098 0.504
70-80 0.503 0.014 0.100 0.505
80-90 0.5030.0160.107 0.508
90-100 0.500 0.012 0.102 0.503
Table 21.𝐴𝑐𝑠_𝐼𝑛𝑐𝑜𝑚𝑒- evaluation of attack performance with confidence bins.
