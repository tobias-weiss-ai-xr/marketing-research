---
title: A Systematic Approach for Selecting Trajectories for Data Augmentation
url: https://arxiv.org/abs/2606.10938
category: ai-marketing
subcategory: measurement
date: 2026-06
venue: ''
authors:
- Adam Nordling
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.10938
pages: 45
chars: 109010
fetched_at: '2026-11-08T13:27:57+00:00'
kb_version: 1
---

# A Systematic Approach for Selecting Trajectories for Data Augmentation

arXiv:2606.10938v1  [cs.LG]  9 Jun 2026
Author:Adam Nordling
Supervisor:Amilcar Soares
Examiner:Hemant Ghayvat
Semester:VT 2026
Course:5DV50E
Subject:Computer Science
Masters Degree Project
A Systematic Approach for Selecting
Trajectories for Data Augmentation

Abstract
Trajectory data augmentation is a promising approach to mitigate data scarcity in
machine learning applications, but its utility has been limited by the complexity of
preserving spatio-temporal coherence. Although prior work demonstrated the viabil-
ity of geometric perturbation, it relied on naive random selection, leaving a critical
gap in understandingwhichtrajectories should be augmented for maximal benefit.
This thesis addresses this gap by developing a systematic and scalable framework
to evaluate five systematic selection strategies: Outlierness, Diversity, Representa-
tiveness, Uncertainty, and Random selection. These strategies were rigorously tested
across four datasets covering animal behavior (Foxes and Starkey), maritime traffic
(AIS), and urban traffic (Car) using a suite of linear and non-linear machine learning
models. As part of this evaluation, an Optuna-based hyperparameter optimization
loop was integrated to empirically identify the best-performing augmentation pa-
rameters for each dataset within the explored search space. The results indicate that,
while systematic selection is not a universal solution, it offers distinct advantages
over the random baseline. Systematic strategies, particularly Outlierness and Un-
certainty, demonstrated higher stability and were less prone to performance degra-
dation observed with random sampling in dense datasets. However, the findings
also reveal that the value of augmentation is strictly conditional. Visual analysis via
UMAP demonstrates that while systematic augmentation successfully repairs topo-
logical fragmentation in sparse datasets, it can act as a corrupting noise signal in
high-quality, dense datasets. Furthermore, the study identified physical limitations
in high-velocity domains, where standard perturbation techniques lead to divergence
in feature space. This research provides a practical evidence-based framework for
practitioners, establishing that strategic data selection is not only an optimization de-
tail, but can be the primary determinant of augmentation success.
Keywords:trajectory data augmentation, systematic selection strategies, hyper-
parameter optimization, machine learning, trajectory classification, data scarcity,
mobility analysis

Preface
This thesis investigates systematic selection strategies for augmentation of trajectory data
to improve machine learning classification. The research topic was initiated by my super-
visor, Amilcar Soares, as a refinement of future work suggested in previous studies within
this field.
I would like to thank Amilcar Soares for his guidance throughout the entire project, from
the initial formulation of the research question to the final results analysis. His expertise
was essential in navigating the complexities of trajectory data and ensured that the find-
ings were interpreted with the necessary scientific nuance.
In the production of this thesis, some artificial intelligence tools were used to help solve
specific programming challenges and to improve the clarity of written explanations. Al-
though these tools provided technical and linguistic support, all conceptual decisions and
final conclusions remain my own independent work.

Contents
1 Introduction 1
1.1 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.3 Problem Formulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.4 Objectives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.5 Contributions of the Work . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.6 Scope and Limitations . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.7 Target Audience . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.8 Thesis Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2 Related Work 5
2.1 Review of Existing Research . . . . . . . . . . . . . . . . . . . . . . . . 5
2.2 Comparison of Approaches . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.3 Identified Gaps and Positioning of this Work . . . . . . . . . . . . . . . . 7
2.4 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
3 Method 8
3.1 Research Approach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
3.2 Systematic Trajectory Selection Strategies . . . . . . . . . . . . . . . . . 9
3.2.1 Random Selection . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.2.2 Outlierness-Based Selection . . . . . . . . . . . . . . . . . . . . 9
3.2.3 Diversity Maximization Selection . . . . . . . . . . . . . . . . . 10
3.2.4 Representativeness-Based Selection . . . . . . . . . . . . . . . . 11
3.2.5 Uncertainty-Based Selection . . . . . . . . . . . . . . . . . . . . 11
3.3 Experimental Framework . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.3.1 Dataset Preparation . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.3.2 Feature Extraction . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.3.3 Augmentation Process . . . . . . . . . . . . . . . . . . . . . . . 13
3.3.4 Model Training and Evaluation . . . . . . . . . . . . . . . . . . 15
3.3.5 Parameter Selection and Justification . . . . . . . . . . . . . . . 16
3.4 Implementation Details . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.5 Ethical Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.6 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
4 Results and Analysis 20
4.1 Overall Performance Comparison . . . . . . . . . . . . . . . . . . . . . 20
4.2 Statistical Analysis by Dataset . . . . . . . . . . . . . . . . . . . . . . . 21
4.2.1 AIS Subset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
4.2.2 Car Traffic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
4.2.3 Foxes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
4.2.4 Starkey . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.3 Geometric Analysis via UMAP . . . . . . . . . . . . . . . . . . . . . . . 26
4.3.1 Visualization Methodology . . . . . . . . . . . . . . . . . . . . . 26
4.3.2 Manifold Densification in the Foxes Dataset . . . . . . . . . . . . 27
4.3.3 Decision Margin Corruption in the Starkey Dataset . . . . . . . . 28
4.3.4 Feature Space Divergence in Car Dataset . . . . . . . . . . . . . 29
4.4 Impact of Model Architecture . . . . . . . . . . . . . . . . . . . . . . . 30
4.5 Summary of Findings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30

5 Discussion 32
5.1 The Primacy of Selection: An Empirical Answer to a Known Gap . . . . 32
5.2 Interpreting the Strategy Mechanisms in Context . . . . . . . . . . . . . 32
5.3 The Conditional Value of Augmentation . . . . . . . . . . . . . . . . . . 33
5.4 Physical Constraints and Domain Dynamics . . . . . . . . . . . . . . . . 33
5.5 Implications of Per Dataset Optimization . . . . . . . . . . . . . . . . . . 34
6 Conclusion and Future Work 34
References 36

1 Introduction
1.1 Background
Trajectories represent the movement of entities, such as people, vehicles, or animals,
through space and over time. Typically modeled as a sequence of timestamped geographic
coordinates, trajectories have become central to a wide range of applications, including
urban planning [1], transportation optimization [2], wildlife monitoring [3], and maritime
traffic analysis [4, 5]. For example, the data collected from the Automatic Identification
System (AIS) supports the monitoring of maritime traffic networks [6, 7, 8] and enables
the forecast of vessel routes [9]. In fisheries management, vessel trajectories help detect
fishing activity [10, 11], while in smart mobility and urban analytics, trajectory data plays
a key role in understanding movement patterns in cities [12].
Despite their utility, trajectory datasets pose substantial analytical challenges. Trajec-
tories are inherently spatiotemporal and often sampled irregularly, making them difficult
to preprocess and model [13]. Additional complications arise from GPS measurement
noise, semantic ambiguities in movement patterns, and the high dimensionality of de-
rived features. Moreover, privacy concerns and proprietary data ownership frequently
prevent the public release of high-quality trajectory datasets, limiting reproducibility and
benchmarking in research [14]. These difficulties are compounded in large-scale settings
where big data techniques are necessary to handle large volumes of movement records
[4, 15].
Trajectory data supports a wide range of tasks, such as trajectory classification [16,
17, 18], clustering [19, 20], anomaly detection [21, 5], segmentation [22, 23, 24, 25], and
forecasting [26, 27]. For example, detecting unusual vessel behavior requires analyzing
deviations from normal movement patterns using spatial, temporal, and contextual cues
[28]. Researchers are increasingly applying machine learning and deep learning meth-
ods to these tasks, but these models often rely on large labeled datasets for training and
evaluation. These datasets are typically scarce or incomplete in this domain.
One promising approach to mitigate labeled data scarcity is trajectory data augmen-
tation, which artificially expands the training dataset by generating new realistic exam-
ples from existing data. Augmentation techniques are widely adopted in computer vision
and natural language processing, where simple transformations (e.g., rotations or word
substitutions) can improve model generalization and reduce overfitting. However, in the
trajectory domain, augmentation remains underexplored [14]. This is in part due to the
complexity of maintaining the spatiotemporal coherence and semantic plausibility of gen-
erated trajectories. Designing transformations that preserve key characteristics (such as
speed, direction, and behavioral patterns) is a non-trivial task.
1.2 Motivation
Trajectory data augmentation presents several compelling opportunities in the context
of movement analysis. First, it helps mitigate the common challenge of data scarcity in
trajectory-based applications, such as urban planning, transportation optimization, wildlife
monitoring, and maritime traffic analysis, by synthetically increasing the availability of
labeled data. This enables the development of more robust and generalizable machine
learning models. Second, augmentation strategies can help address class imbalance prob-
lems frequently observed in trajectory datasets, where certain types of movement, behav-
iors, or transportation modes are underrepresented. By enriching these underrepresented
categories, augmentation supports more equitable and effective model training. Finally,
1

systematic trajectory augmentation can reveal which geometric or temporal features are
most discriminative for downstream tasks such as trajectory classification, clustering, or
anomaly detection. This contributes not only to improved model performance but also to
a deeper understanding of the structure and variability of real-world mobility patterns.
1.3 Problem Formulation
Haranwala et al. [14] proposed a trajectory augmentation algorithm that introduces ge-
ographical perturbations to selected trajectory points using two strategies: in-circle and
on-circle noise. The method randomly selects points along a trajectory and modifies their
geographic coordinates within predefined circular regions, generating augmented trajecto-
ries that preserve key spatio-temporal properties while introducing controlled variability.
However, as the authors themselves acknowledged, their implementation relied en-
tirely on the random selection of both trajectories and trajectory points for noise injection.
Although this randomness effectively demonstrated the viability of their approach, it also
limited its applicability and optimization potential. The absence of a principled selection
mechanism raises an important open question in the field:
How can trajectories be systematically selected for augmentation to improve
classification performance?
This research question focuses on a gap identified by Haranwala et al. [14], who empha-
sized the need for “systematically controlling this noise to enhance its applicability in
classification problems” and noted that “innovating new techniques for ranking trajecto-
ries presents an exciting possibility for augmenting trajectories.”
1.4 Objectives
This thesis seeks to advance trajectory data augmentation by moving beyond random
sampling toward principled methods for selecting trajectories and trajectory points to
augment. The goal is to make augmentation more effective, interpretable and tailored
to downstream classification tasks.
To address the research question, the thesis pursues the following objectives:
O1
Design and implement systematic selection strategies for trajectory
augmentation, leveraging properties such as outlierness, representa-
tiveness, diversity, and prediction uncertainty.
O2
Quantitatively evaluate the impact of different selection strategies on
classification performance across multiple datasets and model archi-
tectures.
O3
Develop a framework for benchmarking trajectory selection strate-
gies, enabling comparative analysis and providing empirical evidence
for their effectiveness in augmentation tasks.
2

1.5 Contributions of the Work
This thesis makes the following contributions to the field of trajectory data analysis:
•Theoretical Contributions:It establishes theoretical foundations for systemati-
cally selecting trajectories and trajectory points. By doing so, this work provides the
principled, data-driven framework that was absent from the purely random methods
of previous research.
•Empirical Contributions:It provides rigorous empirical evidence on which selec-
tion strategies yield the greatest improvement in classification performance. This
offers practical evidence-based guidelines that help researchers and practitioners
make informed decisions.
•Technical Contributions:It delivers a high-performance, modular trajectory aug-
mentation framework optimized for scalability. By implementing vectorized oper-
ations and efficient binary serialization, the system goes beyond single-use scripts
to a comprehensive solution that integrates systematic selection with proven noise
techniques at scale. The complete software framework has been archived and made
publicly available to ensure reproducibility [29].
1.6 Scope and Limitations
This research focuses specifically on extending the trajectory augmentation algorithm pro-
posed by Haranwala et al. [14] by developing systematic selection strategies. Although
the original geographical noise techniques (specifically on-circle) will be utilized, this
work will not explore alternative noise application methods. The evaluation uses trajec-
tory datasets with spatial representations and preprocessing assumptions comparable to
those in the original study. In addition to one overlapping dataset, additional datasets
obtained through the same sources are included to support a consistent evaluation.
The thesis will focus on trajectory classification rather than regression or clustering.
Additionally, the work will employ a diverse suite of machine learning models, rang-
ing from linear to complex non-linear architectures, to enable robust evaluation of how
different selection strategies impact model performance.
1.7 Target Audience
This research aims at three primary audiences: (1) researchers in mobility data analysis
looking to overcome data scarcity challenges, (2) data scientists and machine learning
practitioners working with trajectory data across various domains, and (3) domain ex-
perts in transportation, urban planning and location-based services who can benefit from
improved trajectory classification models.
1.8 Thesis Structure
The remainder of this thesis is organized as follows:
•Chapter 2 - Related Work:Reviews relevant literature on trajectory data analysis,
augmentation techniques in spatiotemporal domains, and methods for identifying
important elements in trajectory data.
3

•Chapter 3 - Methodology:Details the proposed systematic selection strategies for
trajectories and trajectory points, along with the experimental setup for evaluating
their effectiveness.
•Chapter 4 - Results and Analysis:Presents findings from experiments comparing
systematic selection approaches against random selection across different datasets
and models.
•Chapter 5 - Discussion:Interprets results and discusses implications, limitations,
and insights gained about trajectory characteristics and their importance for classi-
fication tasks.
•Chapter 6 - Conclusion and Future Work:Summarizes key contributions and
outlines promising directions for future research in trajectory data augmentation.
4

2 Related Work
This chapter provides an overview of existing research and previous work relevant to the
challenges of data scarcity and the application of data augmentation techniques in tra-
jectory analysis. The purpose of this section is to position the current study within the
academic landscape, demonstrating how it is built upon or differs from previous research
on trajectory data augmentation and selection strategies. It will summarize key contribu-
tions, compare different approaches, and identify the specific gaps that this thesis aims to
address.
2.1 Review of Existing Research
Data augmentation is a well-known set of techniques for artificially increasing the size
and diversity of training datasets, thus improving the generalizability of machine learning
models and mitigating issues such as overfitting [30, 31]. Although widely used in fields
such as computer vision [32] and natural language processing [30], its application to
trajectory data has been relatively limited due to inherent spatiotemporal complexities
and the need to preserve the semantic integrity of movement patterns.
The work of Haranwala et al. [14] introduced a promising approach for trajectory
data augmentation. They proposed an algorithm that applies geographical perturbations
to trajectory points using two main strategies: “in-circle” noise and “on-circle” noise.
This method randomly selects trajectory points and modifies their geographic coordinates
within predefined circular regions, achieving significant performance improvements in
trajectory classification across multiple datasets. However, a key acknowledgment in their
work was the reliance on completely random selection of both trajectories and trajectory
points for noise injection, highlighting a need for more systematic control.
Building upon this concept, Haranwala’s subsequent work introduced AugmenTRAJ,
an open-source Python framework specifically designed for point-based trajectory data
augmentation [33]. AugmenTRAJ offers a suite of techniques, including severalcan-
didate trajectory selection strategiessuch as random selection, proportional selection
(based on class representation), length-based selection (focusing on shorter trajectories),
and representative trajectory selection (based on statistical similarity to the overall dataset).
It also expanded onpoint modification techniques, including in-circle and on-circle modi-
fications, point stretching, and point dropping. This framework provides a more structured
approach to trajectory augmentation than purely random methods.
Beyond direct trajectory data augmentation for classification, related concepts appear
in other specialized domains. For example, Agrawal et al. [34] developed TrajAug for
robust neural locomotion controllers, in which synthetic motion data are generated by
motion matching to follow random trajectories. This approach aims to re-balance datasets
and introduce sharper, more game-relevant turns, which are often underrepresented in cap-
tured motion data. Although the application (locomotion) and the generation method (mo-
tion matching) differ, the underlying principle of creating diverse, balanced data through
synthetic trajectories remains relevant.
In the field of imitation learning, Antotsiou et al. [35] addressed the challenge of
preserving the validity of augmented trajectories. They introduced a semi-supervised
correction network to rectify distorted expert actions, ensuring that augmented trajectories
remain successful in control tasks. This is a critical factor, since random distortions can
easily invalidate sequential decision-making processes.
For safety-critical applications such as autonomous driving, Mirkhani et al. [36] pro-
posed a method to augment driving scenarios while preserving their similarity to expert
5

trajectories. Their approach involves clustering trajectories to identify minority, safety-
critical groups, combining trajectories within the same cluster using geometric transfor-
mations, and then performing rigorous safety and quality checks. This highlights the
importance of context-aware augmentation, especially when dealing with high-stakes and
imbalanced data.
The problem ofwhatdata to augment, rather than justhowto augment it, has been
more explicitly addressed in other domains, such as computer vision. Lin et al. [37] de-
veloped SelectAugment, an approach that deterministically selects samples for augmen-
tation online using Hierarchical Reinforcement Learning (HRL). SelectAugment decides
whether to augment an image based on its content and the network’s current training sta-
tus, aiming to avoid potential negative effects of random augmentation, such as visual
ambiguities or induced training biases.
Ultimately, the goal of these augmentation strategies in this thesis is to improve tra-
jectory classification. Surveys like the one by da Silva et al. [38] review various trajectory
classification methods, noting that the core challenge often lies in extracting or identi-
fying features and subtrajectories that best discriminate between classes. Effective data
augmentation can directly support this by providing more and more diverse data from
which classifiers can learn.
2.2 Comparison of Approaches
The reviewed literature shows a range of approaches to data augmentation for trajectory
data. The work by Haranwala et al. [14] established the effectiveness of point perturba-
tion, applied to randomly selected trajectories. The AugmenTRAJ framework [33] for-
malized this by presenting random selection as one of several explicit strategies (alongside
proportional, length-based, etc.), giving users more control over the augmentation pro-
cess. This thesis adopts this view, treating random selection as a baseline augmentation
strategy, against which more complex data-driven methods can be compared.
In contrast to these perturbation-based methods, approaches such as TrajAug by Agrawal
et al. [34] create entirely new trajectories using generative techniques such as motion
matching. This represents a different philosophy, focused on synthesizing new data rather
than modifying existing points.
A key difference between methods is how they choose what to generate or select.
Random selection offers simplicity and serves as an important benchmark for other aug-
mentation techniques. The rule-based strategies in AugmenTRAJ [33] provide alternative
heuristic improvements. More advanced methods use learning or quality checks. For
example, Antotsiou et al. [35] use a correction network to ensure that the augmented
trajectories are still valid, while Mirkhani et al. [36] use clustering to find and enhance
safety-critical driving scenarios. These methods focus on ensuring that the augmented
data makes sense in its specific context.
The work of Lin et al. in SelectAugment [37], though in the image domain, introduces
the powerful idea of learningwhichsamples to augment. This data-driven approach,
which considers the data itself, contrasts with fixed rules or a purely random choice, and
serves as an inspiration for the systematic strategies we explore in this thesis.
Finally, the primary goal of these methods varies. Some, like Haranwala et al. [14]
and AugmenTRAJ [33], aim to improve general trajectory classification. Others are built
for specific tasks such as locomotion control (Agrawal et al. [34]) or autonomous driving
safety (Mirkhani et al. [36]).
6

2.3 Identified Gaps and Positioning of this Work
The existing literature, particularly Haranwala et al. [14], clearly identifies a key limita-
tion: the use of random selection in trajectory data augmentation. As they noted, “in-
novating new techniques for ranking trajectories presents an exciting possibility.” The
AugmenTRAJ framework [33] began to address this by offering several heuristic-based
strategies. However, these heuristics are predefined and cannot be adaptable. The de-
velopment of data-driven selection methods that consider the statistical properties of tra-
jectories within their class (such as their outlierness, representativeness, contribution to
diversity, or prediction uncertainty) remains an open area for investigation. This is the
primary gap this thesis aims to fill.
Although sophisticated selection mechanisms such as SelectAugment [37] exist for
image data, their application to the unique spatio-temporal nature of trajectory data has not
been thoroughly explored. Trajectory data presents different challenges and opportunities
for defining “sample content” and “training status” relevant for selection.
This thesis directly addresses these gaps by moving beyond the random selection
approach of Haranwala et al. [14] and the static heuristics in AugmenTRAJ [33]. By
systematically designing, implementing, and evaluating selection strategies based on out-
lierness, diversity, representativeness, and uncertainty of core statistical properties, this
work investigates the fundamental question ofwhichtrajectories are most valuable for
augmentation. This thesis provides an empirical comparison of these intelligent selec-
tion strategies with the aim of developing a practical, scalable framework for improving
trajectory classification.
2.4 Summary
The related work reveals that, while trajectory data augmentation is a new field, early
efforts have demonstrated its potential. Many methods have focused on point perturba-
tion [14, 33], while related domains offer insight into generative approaches [34], valid-
ity preservation [35], context-specific augmentation [36], and intelligent sample selec-
tion [37].
This thesis builds on the previously identified need for more systematic and intelligent
trajectory selection for augmentation, with the goal of developing and evaluating strate-
gies to improve trajectory classification performance by selecting which data to transform.
7

3 Method
This section describes the methodology used to investigate systematic trajectory selec-
tion strategies for data augmentation. The method is structured around developing, im-
plementing, and evaluating four distinct selection strategies that go beyond the random
approach established in the foundational work of Haranwala et al. [14]. The methodology
ensures that the findings are credible, replicable and provide meaningful insight into the
effectiveness of different trajectory selection approaches.
3.1 Research Approach
This study adopts a quantitative experimental research approach to evaluate and compare
systematic trajectory selection strategies with random baselines. Controlled experiments
are conducted on multiple datasets and machine learning models, with performance as-
sessed using standardized evaluation metrics and statistical significance tested on multiple
runs. This experimental design provides empirical evidence of the effectiveness of sys-
tematic selection strategies in practical trajectory classification scenarios.
In this chapter, we start in Section 3.2 by detailing how trajectory selection strategies
were mathematically defined. In Section 3.3, we provide a comprehensive breakdown of
the entire experimental pipeline, which is illustrated in Figure 3.1.
Figure 3.1: Trajectory Data Augmentation & Evaluation Pipeline
The pipeline is organized into six functional stages designed to ensure a rigorous and
reproducible comparison between the selection methods. It begins with data prepara-
tion, where raw trajectory records are cleaned and partitioned into stratified training and
testing sets. The second stage involves the extraction of baseline features to transform
raw geographic coordinates into vectorized geometric and kinematic descriptors. In the
third stage, the core experimental variable is introduced by applying systematic selection
8

strategies to identify specific trajectories for augmentation and generating synthetic vari-
ants. Feature extraction is then performed on these new samples and merged with the
original data to form the final training sets. The fifth stage consists of training machine
learning models and scoring them against unseen test data using the weighted F1 score.
Finally, the results of all all experimental runs are aggregated to produce the statistical
reports and geometric visualizations used for analysis.
3.2 Systematic Trajectory Selection Strategies
Building on the geographical noise techniques introduced by Haranwala et al. [14], this
work develops four systematic trajectory selection strategies. Each strategy implements
a different theoretical approach to identifying which trajectories should be selected for
augmentation. For a given class containing a set of trajectoriesT, each strategy aims to
select a subsetS⊂Tof size|S|=p· |T|, wherepis the selection proportion.
3.2.1 Random Selection
The random selection strategy serves as the simplest augmentation approach, replicating
the original method used by Haranwala et al. [14]. Random selection chooses trajecto-
ries for augmentation using a uniform probability distribution, ensuring that each trajec-
tory has an equal chance of being selected regardless of its characteristics. This strategy
provides a baseline for comparing systematic selection approaches against unsystematic
augmentation.
Formalization:For a given class containing a set of trajectoriesT, the probability
P(t)of selecting any given trajectorytof that class is uniform:
P(t) = 1 |T| ∀t∈T(1)
Trajectories are sampled without replacement from each class until the target proportion
pis reached for that class.
The strategy randomly selects a specified proportion of trajectories from each class to
maintain the balance of the class during augmentation. The selection process uses a fixed
random seed to ensure reproducibility between experimental runs. Random selection
serves as an important comparison point to demonstrate whether systematic approaches
provide meaningful improvements over naive trajectory selection for augmentation.
3.2.2 Outlierness-Based Selection
The outlier-based selection strategy identifies trajectories that deviate significantly from
typical patterns within their class. The underlying hypothesis is that augmenting outlier
trajectories can help models better learn decision boundaries and improve the robustness
to edge cases that may be underrepresented in the original dataset.
This strategy employs the Distance-Based Outlier Score (DBOS) algorithm to quan-
tify trajectory outlierness [39]. For each class, trajectory features are extracted. To es-
tablish a data-driven radius parameterdfor DBOS, the average pairwise Euclidean dis-
tance within the class’s feature space is calculated. For computational feasibility on larger
classes, this distance is estimated using a random sample (N= 1000) of the population,
avoiding the quadratic complexity of a full pairwise distance matrix while maintaining
statistical validity. This adaptive radius is then used in the DBOS algorithm’s ball-tree
9

structure for efficient neighbor search, creating a neighborhood definition that adjusts to
the specific data distribution of each class.
Formalization:For each trajectorytwith feature vectorF(t)in a class setT, its
neighborhoodN d(t)is the set of other trajectories within radiusd:
Nd(t) ={t′ ∈T|distance(F(t), F(t ′))≤d}(2)
The raw outlier score,OS raw(t), is defined by the inverted neighborhood count, where
trajectories with fewer neighbors are assigned higher scores:
OSraw(t) = max t′∈T |Nd(t′)| − |Nd(t)|(3)
This score is then scaled to a final valueOS(t)between 0 and 1 using min-max normal-
ization to facilitate the ranking. The trajectory is ranked byOS(t)in descending order,
and the top proportionpis selected for augmentation.
The DBOS algorithm’s ball-tree structure allows for efficient neighbor searches to cal-
culate outlier scores based on the number of neighboring trajectories within the specified
radius. Trajectories with fewer neighbors receive higher outlier scores, indicating their
deviation from typical class patterns. The trajectories are subsequently ranked by their
outlier scores, and the highest-ranked trajectories are selected for augmentation. This
approach ensures that the most unusual or edge-case trajectories within each class are pri-
oritized for augmentation, potentially improving model robustness to diverse trajectory
patterns.
3.2.3 Diversity Maximization Selection
The diversity maximization strategy aims to select trajectories that collectively represent
the maximum diversity within each class. This approach is based on the hypothesis that
augmenting diverse trajectories will create a more comprehensive representation of the
class space, leading to improved model generalization capabilities. The strategy uses k-
means clustering to identify diverse trajectory groups within each class.
Formalization:For each class, the set of trajectory feature vectors is partitioned
intokclusters,C={C 1, C2, . . . , Ck}, by minimizing the within-cluster sum of squares
(WCSS):
arg min
C
kX
j=1
X
F(t)∈C j
∥F(t)−µ j∥2 (4)
whereµ j is the centroid of the clusterC j. The selection is then performed by sampling
proportionally from each cluster.
For each class, k-means clustering is applied to the trajectory feature space. The num-
ber of clusters was set tok= 5, a heuristic chosen to achieve a meaningful partitioning of
the feature space; this value was adaptively reduced for any class with fewer than five tra-
jectories. We acknowledge that using a fixedk= 5across domains as diverse as maritime
traffic and animal movement is an arbitrary heuristic and a limitation of this study. While
dynamically determining the optimalk(e.g., via Silhouette scores or the elbow method)
for each class would provide a more scientifically rigorous mapping of the dataset’s vari-
ety, a fixedkwas chosen strictly as a computational trade-off to keep the hyperparameter
optimization loop tractable.
10

Representatives are selected from each cluster, with selection proportional to clus-
ter size to ensure that larger, more representative groups contribute more trajectories to
the augmentation set. For computational efficiency with large datasets, the MiniBatchK-
Means algorithm is employed instead of standard k-means clustering.
3.2.4 Representativeness-Based Selection
The representativeness-based selection strategy identifies trajectories that are most simi-
lar to the overall distribution of their class. The hypothesis underlying this approach is
that augmenting representative trajectories will strengthen the model’s understanding of
typical class patterns, reinforcing the most common and characteristic behaviors within
each class.
This strategy uses statistical similarity measures to identify representative trajectories.
For each class, z-scores are calculated for all trajectory features, normalizing the feature
values relative to the class mean and standard deviation. A representativeness score is
computed as the sum of absolute z-scores for each trajectory, where lower scores indicate
trajectories that are closer to the class centroid in the normalized feature space.
Formalization:For each featureiin the feature vectorF(t)of a trajectoryt, a z-score
is calculated:
zi(t) = Fi(t)−µ i
σi
(5)
whereµ i andσ i are the mean and standard deviation of featureiacross all trajectories
in the class. The representativeness scoreRS(t)is the L1 norm of the z-score vector,
measuring the trajectory’s total deviation from the class centroid:
RS(t) =
mX
i=1
|zi(t)|(6)
wheremis the number of features. The trajectory with the lowestRS(t)is considered
the most typical and is selected.
Trajectories with lower representativeness scores are considered more representative
of their class and are prioritized for selection. For robustness, all missing or non-finite fea-
ture values were consistently imputed with zero prior to score calculation. This approach
selects trajectories that closely match the central tendency of their class, potentially rein-
forcing the model’s ability to recognize and classify typical patterns.
3.2.5 Uncertainty-Based Selection
This strategy selects the trajectories that the model currently finds most confusing or am-
biguous. The underlying hypothesis is that augmenting these “hard-to-classify” examples
forces the model to refine its decision boundary in regions of high uncertainty, similar to
the techniques used in active learning.
Formalization:A “scout” logistic regression model is trained on the current dataset.
For each trajectoryt, the model predicts a probability distribution over all classes. The
uncertainty scoreU(t)is computed using entropy:
U(t) =−
X
c∈C
P(y=c|t) logP(y=c|t),(7)
11

whereP(y=c|t)denotes the predicted probability that trajectorytbelongs to classc.
Trajectories with higher entropy scores correspond to cases in which the model ex-
hibits a lower confidence in the classification. These trajectories are ranked in descending
order of uncertainty, and the top proportionpis selected for augmentation. To preserve
class balance, the ranking and selection process is performed independently within each
class.
3.3 Experimental Framework
3.3.1 Dataset Preparation
To ensure the generalizability of our findings, this study evaluates selection strategies
across four diverse trajectory datasets. The datasets were selected to represent a range of
movement patterns, domains, and spatial and temporal scales, including animal behavior,
human mobility, and maritime traffic. Each dataset is split into 80% training and 20%
testing sets using stratified sampling to preserve class distributions. To ensure that strati-
fication is feasible, a preprocessing step removes classes with fewer than two samples.
In addition, several data quality checks are applied. Trajectories with zero variance
in latitude and longitude are treated as stationary artifacts and excluded to avoid errors
in kinematic feature computation. Trajectory identifiers (TIDs) are also explicitly cast
to string types to prevent integer overflow and unintended formatting issues. This entire
procedure is repeated on 20 random seeds to ensure statistical robustness.
The final datasets selected for this research are the following:
•Foxes:This dataset tracks the movement of 66 adult arctic foxes (Vulpes lagopus)
on Bylot Island, Nunavut, Canada. Originally sourced from a six year study using
Argos satellite telemetry, the data capture how these predators navigate a fluctuating
tundra environment [40]. The dataset comprises 229,657 data points and is utilized
here for gender classification. With an average trajectory length of 3,480 points, it
represents a complex record of biological movement patterns.
•Starkey:This dataset contains movement records for 253 ungulates, including elk
and deer, within the Starkey Experimental Forest and Range in Oregon, United
States [41]. It consists of 287,136 data points categorized into three behavioral
classes. The trajectories in this dataset are relatively short, averaging 1,135 points
per record. It serves as a benchmark for classifying animal behavior and habitat use
in a controlled environment.
•Car Traffic:This dataset captures the movement of 125 vehicles in Brno, Czech
Republic, and is sourced from the example collections of the PTRAIL library [13].
It contains exactly 44,905 data points categorized into two classes: car and bus. The
trajectories are characterized by a short average length of 359 points. This dataset is
included to evaluate how augmentation selection strategies perform in high velocity
urban mobility contexts.
•AIS Subset:The original maritime dataset provided for this research, which con-
tains millions of vessel trajectories, was too large for the computational scope of
the project. Therefore, a specialized subset was created. This data is derived from
the Automatic Identification System (AIS), a tracking system used ship-tracking
12

system that broadcasts a ship’s speed. To create a manageable and balanced multi-
class dataset, the original ais.csv file was processed programmatically. The script
iterated through the large file in chunks, filtering for trajectories belonging to four
specific vessel types: Fishing (label 30), Tug (label 52), Passenger Ship (label 60),
and Cargo Ship (label 70). The resulting ais_subset.csv file contains 694 unique tra-
jectories and a total of 2,660,535 data points, providing a challenging and realistic
scenario for maritime trajectory classification.
With these datasets prepared, the next step is a systematic feature-extraction process to
create a robust numerical representation for each trajectory.
3.3.2 Feature Extraction
To create a robust representation of trajectory behavior, the framework employs a system-
atic process to derive features capturing geometric, kinematic, and statistical properties.
These features serve a dual purpose: they inform the selection algorithms and provide in-
put tonal machine learning classifiers. The implementation is optimized for performance,
using vectorized calculations to efficiently process large datasets.
1.Distance-based Geometry Features:The shape of each trajectory is captured through
a multi-level sinuosity analysis. Trajectories are partitioned into segments at five
distinct levels of granularity (1-5 segments). For each segment, the ratio of the
geodesic distance (straight-line) to the cumulative path distance is calculated. To
optimize this process, the cumulative path distance is computed from a precom-
puted set of inter-point segments using fast, vectorized ellipsoidal geodesic calcula-
tions (WGS84) via the pyproj library. This process quantifies the straightness of the
trajectory versus the tortuosity on multiple scales of analysis, yielding 15 geometric
features. To overcome the computational overhead of iterative fractal summation
on large datasets, these specific calculations were optimized using Numba Just-
In-Time (JIT) compilation, achieving C-level execution speeds within the Python
environment.
2.Kinematic and Statistical Features:Movement dynamics is characterized by three
core kinematic measures: speed, acceleration, and turning angle. The implementa-
tion leverages vectorized NumPy operations to efficiently compute these measures
across entire trajectories at once, avoiding slow, iterative calculations. To go be-
yond simple averages, a comprehensive statistical profile is then computed for each
of these three measures. This includes 19 statistical metrics, such as mean, standard
deviation, skewness, kurtosis, median absolute deviation, and a range of quantiles
(e.g., 5th, 25th, 75th, 95th). This comprehensive profiling captures the full distribu-
tion of movement behaviors, providing a nuanced view of a trajectory’s dynamics.
The complete feature extraction process generates a 72-dimensional feature vector for
each trajectory (15 from geometry + 3 kinematic measures×19 statistical features), cre-
ating a rich, multi-faceted representation suitable for complex behavioral analysis.
3.3.3 Augmentation Process
The augmentation process employs the “on-circle” noise strategy from Haranwala et
al. [14] to apply realistic geographical perturbations to selected trajectories. The method-
ology is defined by its core perturbation mechanism, the hyper-parameters that govern it,
13

and a rigorous seed management protocol that ensures all experimental results are fully
reproducible and statistically sound. The systematic method for selecting optimal values
for these hyper-parameters is detailed in Section 3.3.5.
1.Reproducibility and Seed Management:To ensure the scientific validity and com-
plete reproducibility of the experiments, a meticulous seed management protocol is
enforced. The entire experimental framework uses 20 master seeds, derived from
consecutive digits ofπ(1415, 9265, 3589, etc.). Each master seed controls one
complete experimental run, dictating the randomness for dataset splitting, trajec-
tory selection, and the augmentation operations within that run. Crucially, for any
given augmentation operation, a unique and deterministic seed is calculated from
the master seed, the augmentation number (from 1 ton), and the trajectory’s unique
ID. This multi-level seeding strategy is fundamental, as it ensures that when com-
paring the effects of different selection strategies, the underlying randomness of
the perturbation applied to a specific trajectory remains constant, thereby robustly
isolating the impact of the selection method itself.
2.Geographical Perturbation Mechanism:The on-circle strategy modifies a trajec-
tory by relocating a subset of itsinteriorpoints, thereby preserving the original
start and end points to maintain the trajectory’s overall structural integrity. For
each point chosen for perturbation, it is moved to a new random location on the
circumference of a circle centered at its original position. A critical feature of this
implementation is the dynamic scaling of the radius of the circle. The radius is not
a fixed value, but is set instead at 50% of the distance to thenextpoint in the trajec-
tory. This adaptive approach is fundamental because it ensures that perturbations
are context-aware. In dense, slow-moving segments where the points are close to-
gether, the perturbation radius is small, preserving the fine-grained structure of the
movement. In contrast, in sparse, fast-moving segments, the radius is larger, intro-
ducing more significant (but still plausible) geographical noise. This prevents the
generation of unrealistic and jerky movements and ensures that the augmented data
remain semantically coherent with the original movement patterns.
3.Governing Hyperparameters:The intensity and scale of the augmentation process
are controlled by a set of three key hyperparameters. These parameters serve as the
primary variables in the experimental design, enabling a systematic exploration of
the impact of the augmentation strategy, namely:
• TheTrajectory Selection Proportion (p), which dictates what fraction of tra-
jectories to augment.
• TheNumber of Augmentations (n), which defines how many new versions are
created for each selected trajectory.
• ThePoint Modification Proportion (pp), which determines the proportion of
interior points within a selected trajectory that are to be perturbed.
Each newly generated trajectory is assigned a unique identifier and metadata that trace it
back to its parent trajectory. The final augmented dataset for training is a union of the
original trajectories and their newly generated counterparts, enriching the training data
while preserving the original class distribution.
14

3.3.4 Model Training and Evaluation
To strictly evaluate the impact of the augmentation strategies, a diverse suite of four ma-
chine learning models was employed: Random Forest, XGBoost, a Multi-Layer Percep-
tron (MLP), and Logistic Regression. This selection spans multiple algorithmic families
to ensure the generalizability of the findings.
A primary challenge in this experimental design is the vast search space created by
combining model hyper-parameters with augmentation hyper-parameters. A simultane-
ous, exhaustive optimization of both was computationally infeasible. Such an approach
would lead to a combinatorial explosion, as the 27 augmentation configurations (3 trajec-
tory selection proportions×3 augmentation counts×3 point modification proportions)
would need to be cross-multiplied with the extensive hyperparameter grids for each of the
four models. For a single model such as XGBoost, this would have resulted in more than
11,000 combinations to test in each experimental run.
To overcome this computational barrier, the parameter search spaces were decoupled.
This led to the adoption of a systematic two-phase tuning process that is not only compu-
tationally tractable but also methodologically more robust. This “baseline-first” approach
is designed to isolate the effect of data augmentation from the effect of model hyperpa-
rameter tuning.
1.Baseline Model Tuning:For each dataset and each of the 20 master seeds, the
models are first tuned exclusively on the original, non-augmented 80% training
data. This is performed using a 3-fold cross-validated Grid Search (GridSearchCV)
to find the optimal hyperparameter configuration for each model under baseline
conditions. These baseline parameters that perform best are then serialized and
cached on disk. This strictly enforces that subsequent runs on augmented data use
the exact same model configuration, isolating the data quality as the only variable.
2.Augmentation Evaluation:When evaluating a given augmentation strategy (e.g.,
Outlierness with a specific set of Optuna-derived hyperparameters), the models are
retrained on the newly augmented dataset. Crucially, they are trained using the
optimal baseline parameters discovered and cached in the first phase.
This protocol ensures that any observed performance difference between the baseline and
an augmented version can be attributed directly to the quality of the augmented training
data, rather than to coincidental benefits from simultaneous model re-tuning.
The selected models and their corresponding hyperparameter search spaces for the
initialGridSearchCVtuning are as follows:
Random Forest:An ensemble method using multiple decision trees.
• n_estimators: [100, 300, 500]
• max_depth: [10, 20, 40, None]
• min_samples_leaf: [1, 2, 5]
• max_features: [’sqrt’, ’log2’]
• criterion: [’gini’, ’entropy’]
XGBoost:A gradient boosting framework using decision trees.
15

• n_estimators: [100, 300, 500]
• max_depth: [3, 5, 8]
• learning_rate: [0.02, 0.05, 0.1, 0.2]
• subsample: [0.8, 1.0]
• colsample_bytree: [0.8, 1.0]
• gamma: [0, 0.1, 0.5]
MLP:A feedforward artificial neural network (Multi-Layer Perceptron).
• classifier__hidden_layer_sizes: [(50, 50), (100,), (200,), (100, 50), (100, 100),
(100, 50, 50), (100, 100, 50), (100, 100, 100)]
• classifier__alpha: [0.0001, 0.001, 0.01]
• classifier__activation: [’relu’, ’tanh’]
• classifier__learning_rate_init: [0.001, 0.01]
Logistic Regression:A linear model for binary/multiclass classification.
• classifier__C: [0.01, 0.1, 1.0, 10.0, 100.0]
• classifier__penalty: [’l1’, ’l2’]
• classifier__solver: [’saga’]
Performance is consistently measured in the same 20% holding test set for all experi-
ments. The evaluation metric used is the weighted F1-score, which is chosen to properly
account for potential class imbalances in the datasets. The final reported results are the
average scores across all 20 master seeds, ensuring robust and statistically sound conclu-
sions.
3.3.5 Parameter Selection and Justification
A core contribution of this thesis is to move beyond a “one-size-fits-all” approach to aug-
mentation. Preliminary research and the diverse nature of trajectory datasets suggest that
a single fixed set of augmentation parameters is unlikely to be optimal across all contexts.
For example, a data-scarce dataset may benefit from a more aggressive augmentation
strategy than a large, dense dataset.
Therefore, this work departs significantly from prior methods that rely on predefined
parameters. Instead, it implements a systematic hyperparameter optimization framework
to empirically determine the most effective augmentation configurations on a per-dataset
basis. This ensures that the evaluation is not based on an arbitrary configuration but rather
on the strongest possible application of each augmentation strategy for a given dataset.
To manage this search, theOptunahyperparameter optimization library is integrated
into the experimental pipeline. For each dataset, an optimization “study” is conducted
with the goal of finding the combination of augmentation parameters that maximizes
model performance. The metric to be maximized is the average weighted F1-score across
all four machine learning models and all 20 master seeds for a given parameter set.
16

The optimization process explores the three governing hyperparameters defined in
Section 3.3.3. A discrete search space was defined for each, balancing a wide range of in-
tensities of augmentation with computational feasibility. To ensure that the true optimum
within this space was always found, the study was configured to use Optuna’sGridSam-
pler. This strategy performs an exhaustive grid search on all possible combinations rather
than a random or probabilistic search.
The search space for the 27 unique augmentation configurations is as follows:
•Trajectory Selection Proportion (p):[0.1, 0.2, 0.4]
•Number of Augmentations (n):[1, 3, 5]
•Point Modification Proportion (pp):[0.1, 0.2, 0.4]
While the high-level augmentation strategy was optimized, the low-level perturbation
mechanism parameter remained fixed, as its adaptive nature makes it broadly applicable.
•Circle Radius (50% of the distance to the next point):This parameter was kept con-
stant throughout all experiments. To clarify, this does not mean the spatial radius
was a static global value. Because it is calculated as a percentage of the distance be-
tween two specific consecutive points, the physical radius scales dynamically with
the object’s velocity. For a fast-moving car where points are miles apart, the pertur-
bation radius expands to miles; for a slow-moving fox, the radius shrinks to meters.
Its dynamic, data-driven scaling provides a highly adaptive, localized perturbation.
For each point chosen for modification, the radius is recalculated. This ensures that
perturbations are context-aware: smaller in dense, slow-moving segments to pre-
serve fine-grained structure, and larger in sparse, fast-moving segments to introduce
meaningful variation. This approach has been validated in previous research [14]
and effectively generates realistic geographical noise regardless of the dataset’s do-
main, from local animal movements (Foxes) to urban mobility (Car Traffic).
This optimization-centric approach enables a data-driven, per-dataset determination of
the optimal augmentation strategy. The final results, presented in Section 4, are therefore
based not on a fixed assumption but on an empirical comparison of the most effective
augmentation configurations for each specific data context, ensuring a fair and robust
evaluation of the selection strategies themselves.
3.4 Implementation Details
The complete methodology is implemented in Python, using several specialized libraries.
Core dependencies includepandasandnumpyfor data manipulation;scikit-learnfor ma-
chine learning algorithms and preprocessing;xgboostfor the gradient boosting implemen-
tation; andOptunafor the hyperparameter optimization framework. A critical technical
enhancement involved the use of thepyprojlibrary for geographical calculations. Compu-
tational bottlenecks were addressed by replacing iterative distance metrics with vectorized
operations usingpyproj. By mapping the WGS84 ellipsoid calculations directly to the un-
derlying C arrays, the feature extraction and augmentation phases achieved a speedup of
several orders of magnitude compared to standard iterative approaches, allowing efficient
processing of millions of trajectory points.
Computational considerations are further addressed through several optimization strate-
gies. A multi-level parallel processing strategy is employed. At the experiment level,
17

multiprocessing distributes independent dataset seeds across available CPU cores, while
at the model level, scikit-learn utilizes threaded parallelism forGridSearchoperations.
Explicit memory management (garbage collection) was implemented to prevent RAM
saturation during these concurrent high-load operations. Additionally, I/O overhead was
minimized using the LZ4-compressed Feather binary format for intermediate data storage.
Unlike CSVs, Feather files preserve native Pandas data types, and the LZ4 compression
significantly reduces disk I/O bottlenecks and storage footprint without compromising the
high-speed read/write throughput required for repeatedly loading large trajectory datasets
across multiple experimental seeds. To ensure transparency and reproducibility, the com-
plete source code for this framework has been archived and made publicly available [29].
The pipeline also features a multi-level caching system to maximize computational
efficiency. At a low level, it avoids redundant feature extraction by checking for existing
feature files before processing raw data. At a higher level, the Optuna study incorporates
a robust caching mechanism that saves the final F1-score for each completed trial. This
prevents the costly re-execution of entire experimental runs if the study is interrupted and
resumed, or if the same parameters are evaluated more than once.
The implementation follows best practices in software engineering, including modu-
lar design for maintainability, comprehensive error handling, and extensive logging. To
ensure the resilience of the pipeline, a robust fallback mechanism was implemented. In
cases where systematic strategies encountered mathematical instabilities, such as classes
with zero feature variance that prevented a valid calculation of the outlier score, the sys-
tem automatically defaulted to random selection for that specific class. This prevented
experimental failure while preserving the maximum amount of usable data. This modular
architecture enables easy extension with additional selection strategies, supporting future
research directions.
3.5 Ethical Considerations
This research involves the analysis of trajectory datasets that may contain location infor-
mation with potential privacy implications. Several ethical considerations are carefully
addressed to ensure responsible research conduct. All datasets used in this study are pub-
licly available and have been previously published in academic contexts with appropriate
permissions and ethical clearances. During research, no personally identifiable informa-
tion is processed or stored and all analysis is conducted on aggregated or anonymized
trajectory data.
The data augmentation techniques are designed to preserve privacy by introducing
geographical noise that obscures exact locations while preserving overall movement pat-
terns. The results are reported in aggregate form without exposing individual trajectory
patterns or specific location information. The research contributes positively to the field
by enabling the development of better machine learning models with limited data, poten-
tially reducing the need to collect additional sensitive trajectory information from indi-
viduals.
3.6 Summary
This section has described a comprehensive methodology for investigating systematic
trajectory selection strategies in data augmentation. The approach combines theoretical
foundations from outlier detection, diversity maximization, and representativeness anal-
ysis with practical implementation in a robust, optimization-driven experimental frame-
work. The methodology enables a rigorous, data-driven comparison of selection strategies
18

across multiple datasets and models, providing empirical evidence for their effectiveness
in improving trajectory classification performance.
The systematic approach ensures that the results are reliable, valid and generalizable
across different trajectory domains. The next section will present the detailed results
of applying this methodology, demonstrating the comparative effectiveness of different
selection strategies and their impact on the performance of the machine learning model
across the four evaluation datasets.
19

4 Results and Analysis
This section presents the findings of the systematic evaluation of the trajectory selection
strategy. The performance of each selection strategy was evaluated across the four desig-
nated datasets (AIS Subset, Car Traffic, Foxes, and Starkey) using four machine learning
models (Logistic Regression, MLP, Random Forest, and XGBoost). The primary metric
for evaluation is the weighted F1-score, averaged across twenty different random seeds to
ensure statistical robustness and mitigate the effects of random initialization.
Table 4.1: Performance comparison using the optimal augmentation hyperparameters
identified for each dataset. Each score represents the weighted F1-score, averaged over
all seeds, for that specific model and strategy. Scores higher than the baseline are inbold.
For each dataset, the selected parameters are shown in parentheses:
Sel = proportion of trajectories selected
Augs = number of augmentations per trajectory
Pts = proportion of points modified.
Model Baseline Diversity Outlierness Random Representativeness Uncertainty
Ais Subset Dataset(Sel: 20%, Augs: 1, Pts: 10%)
LogisticReg68.54%68.55% 68.61%67.99%68.95% 68.63%
MLP68.14%68.26% 68.77% 68.53% 69.57% 69.75%
RandomForest76.48%76.45%76.98% 76.50% 76.52%76.33%
XGBoost74.55%74.73% 75.09% 74.69% 74.99% 74.96%
Car Traffic Dataset(Sel: 20%, Augs: 3, Pts: 10%)
LogisticReg84.69%85.08% 84.87%84.44%85.10%83.41%
MLP84.39%85.64% 84.53%83.87%86.05% 84.99%
RandomForest82.28%82.96%82.18%82.57%82.18%82.38%
XGBoost85.89%86.55% 87.01%84.95%84.35%83.92%
Foxes Dataset(Sel: 40%, Augs: 5, Pts: 10%)
LogisticReg42.25%46.83% 49.60% 47.59% 49.07% 47.08%
MLP46.78%41.64%50.54% 47.73% 48.19% 53.69%
RandomForest43.75%45.11% 47.44% 47.69% 51.35% 52.01%
XGBoost50.94%48.83%51.03% 53.49% 51.74%50.60%
Starkey Dataset(Sel: 20%, Augs: 3, Pts: 10%)
LogisticReg88.32%88.61% 88.75% 88.84% 88.34%88.13%
MLP86.22%88.20% 88.22% 88.30% 87.66% 89.53%
RandomForest92.00%91.39%90.38%91.64%90.65%91.38%
XGBoost90.37%90.67%88.96%90.17%89.45%90.75%
4.1 Overall Performance Comparison
The central outcome of the experimental pipeline is a comparison of the performance
of the baseline model with the performance achieved using each of the five systematic
augmentation strategies: Diversity, Outlierness, Random, Representativeness, and Uncer-
tainty.
Table 4.1 presents a high-level summary of the optimal performance achieved for
each dataset. The values represent the mean weighted F1-score in all 20 seeds. A critical
component of these results is the dataset-specific optimization performed by the Optuna
framework. As indicated in the table headers, the optimal augmentation configuration
defined by the Selection Proportion (Sel), Number of Augmentations (Augs), and Point
20

Modification Proportion (P ts) varied significantly between domains. This variance un-
derscores that the intensity of augmentation must be tailored to the specific sparsity and
noise characteristics of the underlying data.
The tabulated results indicate a distinct heterogeneity in the effectiveness of data aug-
mentation in different data contexts. TheFoxesdataset, characterized by sparsity and
complex animal movement, exhibited the most substantial response to augmentation.
In this data-scarce environment, the baseline models struggled to generalize, achieving
scores between 42% and 50%. However, the introduction of systematic augmentation
resulted in transformative gains, with the Representativeness and Uncertainty strategies
pushing performance up by more than 8 to 11 percentage points for the Random For-
est model. This confirms the hypothesis that systematic augmentation acts as a powerful
regularizer in high-variance, low-data regimes.
In contrast to the sparse Foxes dataset, theCar TrafficandStarkeydatasets possessed
high baseline F1-scores, ranging from 82% to over 90%. These domains proved far more
resistant to augmentation. For the Car Traffic dataset, the gains were marginal or non-
existent, illustrating a saturation point where the decision boundaries were already well-
defined by the original data. In such high-quality data environments, additional synthetic
data yield diminishing returns and, in some cases, risk introducing noise that degrades the
classifier’s precision.
A comparison of the selection strategies reveals a consistent trend where systematic
approaches outperformed the naive Random baseline. Although random selection occa-
sionally provided marginal benefits, it consistently trailed behind strategies such as Out-
lierness and Uncertainty. For instance, in the AIS Subset, the Random strategy failed to
improve upon the baseline for the Logistic Regression model, whereas the Representative-
ness and Uncertainty strategies achieved notable gains. This validates the core premise of
this thesis that the strategic selection ofwhichtrajectories to augment is as critical as the
augmentation mechanism itself.
Furthermore, the results highlight a strong interaction between the selection strategy
and the model architecture. Non-linear models, particularly the Multi-Layer Perceptron
(MLP), demonstrated a unique capacity to leverage the Uncertainty strategy. Although
tree-based models such as Random Forest often plateaued on dense AIS and Starkey
datasets, the MLP model achieved its highest scores when trained on data augmented via
Uncertainty selection. This suggests that neural networks, which optimize non-convex
loss functions, benefit significantly from active-learning-style data injection that targets
ambiguous regions of the feature space, preventing convergence to suboptimal local min-
ima.
4.2 Statistical Analysis by Dataset
To validate whether the observed improvements are statistically significant or simply arti-
facts of random seed variance, a rigorous paired t-test (α= 0.05) was conducted for each
dataset.
It is important to clarify the distinction between this analysis and the previous sum-
mary. Although Table 4.1 presented the absolute weighted F1-scores, the following anal-
ysis isolates therelative performance gain(or loss) achieved by the optimal augmentation
configuration compared to its specific seed-matched baseline. This paired comparison fil-
ters out the variance inherent in random initialization, providing a stricter test of whether
the augmentation strategy truly contributes value beyond the baseline variance.
21

4.2.1 AIS Subset
TheAIS Subsetrepresents a challenging maritime environment with high density and
complex vessel interaction. As shown in Table 4.2, the high baseline performance of
the tree-based models made further improvements difficult. For Logistic Regression,
Random Forest, and XGBoost, no strategy yielded statistically significant improvements
(p >0.05), and mean improvements were negligible or slightly negative.
However, a critical breakthrough with the Multi-Layer Perceptron is observed. The
Uncertainty strategy achieved a statistically significant mean improvement of +1.61%
(p= 0.0441). This suggests that in a dense maritime dataset, while the typical trajec-
tory of a vessel is easily learned, the neural network struggles primarily with ambiguous
transition zones between classes. The Uncertainty strategy likely targets these ambiguous
instances for augmentation, forcing the model to refine its decision boundary in the most
confusing regions of the manifold.
Table 4.2: Statistical analysis of the performance improvement for each optimally-tuned
augmentation strategy compared to the baseline. This table presents the final, rigorous
comparison, in contrast to the exploratory overview in the previous table. An asterisk (*)
denotes a statistically significant result (p < 0.05).
Model Strategy Mean Improv. (%) p-value
LogisticRegression
Diversity +0.01 0.9868
Outlierness +0.07 0.8814
Random -0.09 0.8073
Representativeness +0.41 0.2176
Uncertainty +0.09 0.8161
MLP
Diversity +0.12 0.8949
Outlierness +0.63 0.4374
Random -0.08 0.9155
Representativeness +1.43 0.1444
Uncertainty +1.61 0.0441*
RandomForest
Diversity -0.03 0.9308
Outlierness +0.50 0.0936
Random +0.05 0.8693
Representativeness +0.04 0.8040
Uncertainty -0.16 0.6194
XGBoost
Diversity +0.18 0.5423
Outlierness +0.54 0.1878
Random +0.48 0.1423
Representativeness +0.44 0.1335
Uncertainty +0.41 0.2969
22

4.2.2 Car Traffic
TheCar Trafficdataset, representing high-velocity urban mobility, presented a scenario
of high model saturation. As detailed in Table 4.3, the baseline performance of all models
was already robust, ranging between 82% and 85%.
Statistical analysis reveals that no augmentation strategy provided a statistically sig-
nificant improvement for any model in this dataset. Although the MLP model saw a mean
improvement of +1.25% using the Diversity strategy and +1.66% using Representative-
ness, the high p-values (0.2958 and 0.1684, respectively) indicate high variance between
seeds, suggesting that these gains are not reliable. The resistance of this dataset to aug-
mentation implies that the decision boundaries are already well-defined by the original
data, or that the physical constraints of road networks make standard geometric perturba-
tion less effective at generating informative synthetic samples.
Table 4.3: Statistical analysis of the performance improvement for each optimally-tuned
augmentation strategy compared to the baseline. This table presents the final, rigorous
comparison, in contrast to the exploratory overview in the previous table. An asterisk (*)
denotes a statistically significant result (p < 0.05).
Model Strategy Mean Improv. (%) p-value
LogisticRegression
Diversity +0.38 0.8107
Outlierness +0.18 0.8891
Random -1.05 0.2057
Representativeness +0.41 0.6423
Uncertainty -0.10 0.8932
MLP
Diversity +1.25 0.2958
Outlierness +0.14 0.8695
Random +1.06 0.4347
Representativeness +1.66 0.1684
Uncertainty -0.69 0.3838
RandomForest
Diversity +0.68 0.2515
Outlierness -0.10 0.5770
Random +0.10 0.3299
Representativeness -0.10 0.3299
Uncertainty +0.10 0.3299
XGBoost
Diversity +0.66 0.4829
Outlierness +1.12 0.2712
Random +0.18 0.8601
Representativeness -1.54 0.2323
Uncertainty -1.20 0.2469
23

4.2.3 Foxes
TheFoxesdataset represents the data-scarce scenario, where the baseline models per-
formed poorly. Table 4.4 shows that this domain benefited the most dramatically from
systematic augmentation. Unlike previous datasets, nearly all systematic strategies deliv-
ered substantial improvements. For Logistic Regression, the Diversity, Outlierness and
Representativeness strategies all yielded statistically significant gains, with Outlierness
improving the score by more than 7%.
The most profound impact was observed in the Random Forest model. Here, the
Representativeness strategy achieved a remarkable mean improvement of +11.56% (p=
0.0004), and the Uncertainty strategy improved performance by +8.26% (p= 0.0331).
This confirms that in sparse and noisy biological datasets, systematic augmentation acts
as a powerful regularizer, synthesizing the necessary data volume that allows complex
models to generalize rather than overfit. Notably, the naive Random selection often trailed
behind systematic approaches or failed to achieve significance, validating the thesis hy-
pothesis.
Table 4.4: Statistical analysis of the performance improvement for each optimally-tuned
augmentation strategy compared to the baseline. This table presents the final, rigorous
comparison, in contrast to the exploratory overview in the previous table. An asterisk (*)
denotes a statistically significant result (p < 0.05).
Model Strategy Mean Improv. (%) p-value
LogisticRegression
Diversity +5.80 0.0454*
Outlierness +7.18 0.0153*
Random +4.94 0.0691
Representativeness +4.84 0.0456*
Uncertainty +4.82 0.2079
MLP
Diversity +0.87 0.7930
Outlierness +3.35 0.2464
Random +1.42 0.7396
Representativeness +2.43 0.4560
Uncertainty +6.91 0.0550
RandomForest
Diversity +2.66 0.3309
Outlierness +3.55 0.2441
Random +6.52 0.0505
Representativeness +11.56 0.0004*
Uncertainty +8.26 0.0331*
XGBoost
Diversity +0.95 0.6802
Outlierness +1.70 0.3492
Random +4.27 0.1283
Representativeness +0.89 0.7597
Uncertainty -0.35 0.8563
24

4.2.4 Starkey
TheStarkeydataset serves as a control case for sufficient, high-quality data, with base-
lines exceeding 86%. Table 4.5 illustrates the potential risks of augmentation in such
environments.
For the Random Forest model, applying the Outlierness and Representativeness strate-
gies actually resulted in statistically significant performance degradation (-0.95% and -
1.16% respectively). This indicates that when the data manifold is already well-sampled,
adding synthetic noise can corrupt the feature space rather than enhance it.
However, the MLP model again demonstrated a unique synergy with the Uncertainty
strategy, achieving a statistically significant improvement of +3.18% (p= 0.0087). This
reinforces the finding from the AIS dataset that, while tree-based models may reject aug-
mentation on high-quality data, neural networks can still benefit significantly from active-
learning-style data injection to resolve specific ambiguities in the decision boundary.
Table 4.5: Statistical analysis of the performance improvement for each optimally-tuned
augmentation strategy compared to the baseline. This table presents the final, rigorous
comparison, in contrast to the exploratory overview in the previous table. An asterisk (*)
denotes a statistically significant result (p < 0.05).
Model Strategy Mean Improv. (%) p-value
LogisticRegression
Diversity +0.29 0.6303
Outlierness +0.75 0.2118
Random +0.52 0.2811
Representativeness -0.31 0.5700
Uncertainty +0.34 0.5900
MLP
Diversity +1.98 0.1031
Outlierness +1.15 0.3267
Random +2.07 0.1244
Representativeness +1.95 0.1005
Uncertainty +3.18 0.0087*
RandomForest
Diversity -0.61 0.2526
Outlierness -0.95 0.0108
Random -0.36 0.3650
Representativeness -1.16 0.0414
Uncertainty -0.47 0.3742
XGBoost
Diversity +0.30 0.5614
Outlierness -0.12 0.8368
Random -0.20 0.6737
Representativeness -0.10 0.7993
Uncertainty +0.09 0.8744
25

4.3 Geometric Analysis via UMAP
The quantitative results in Section 4.1 demonstrate that augmentation works in specific
contexts. However, numbers alone do not explain why. To understand the underlying
mechanisms driving these results, we visualize the impact of synthetic data on the feature
manifold. The following analysis examines three distinct geometric phenomena observed
during the experiments to illustrate how different strategies interact with the data topology.
4.3.1 Visualization Methodology
Directly visualizing the 72 dimensional feature space is impossible. Furthermore, stan-
dard reduction techniques such as principal component analysis (PCA) rely on linear pro-
jections that often obscure the complex boundaries characteristic of trajectory data.
Therefore, we employ Uniform Manifold Approximation and Projection (UMAP).
UMAP constructs a high dimensional graph representation of the data using k Nearest
Neighbors (kNN) and optimizes a low dimensional layout to preserve the local connec-
tivity of that graph. This makes it uniquely successful in preserving the local density
structure of the classes. It allows us to observe whether the augmented trajectories remain
topologically connected to their parent clusters or drift into invalid regions.
To visualize the decision landscape within this 2D projection, we train a kNN classi-
fier on the 2D embeddings. The background colors in the following figures represent the
decision regions learned by this proxy classifier. This choice is methodological. Since
UMAP is a neighbor-based algorithm, a kNN decision boundary provides the most faith-
ful representation of how the local data density has been altered by augmentation.
In the following visualizations1, the left panel represents the baseline model state and
the right panel represents the state after retraining on augmented data:
•Circles (◦): Original test data points.
•Stars (⋆): Trajectories selected for augmentation.
•Pluses (+): New synthetic trajectories generated.
•Dashed Lines: Connect a parent trajectory to its augmented child. This visualizes
the magnitude of the perturbation.
•Background Color: The decision region learned by the visualization proxy classi-
fier (k Nearest Neighbors).
1The F1 Scores reported in the figure titles correspond to the Random Forest model trained on the full 72
dimensional dataset from Section 4.1. They do not correspond to the 2D proxy model. The visualizations
serve to explain the geometric cause of these performance shifts.
26

4.3.2 Manifold Densification in the Foxes Dataset
The strongest validation of systematic selection is observed in theFoxesdataset, where
data is sparse and noisy. Figure 4.2 illustrates a specific seed (1415) in which the Outlier-
ness strategy improved the Random Forest F1-score by +20.58%.
Figure 4.2: Visual analysis of Manifold Densification (Foxes, Seed 1415). The Outlier-
ness strategy identifies sparse, fragmented regions of the minority class. By injecting
synthetic density (pluses) into these gaps, the model is forced to carve out new decision
regions (Right), significantly improving recall.
Visual inspection of the baseline state (Left) reveals a highly fragmented manifold. The
decision boundary (dark blue vs. brown) is simplistic, failing to capture the complex,
scattered nature of the classes. Specifically, the model misses several sub-clusters of the
minority class, merging them into the background.
The Outlierness strategy (Right) successfully identifies these boundary cases, namely
trajectories that lie at the edges of the known distribution. The augmentation process
generates clouds of synthetic points (pluses) around these selected outliers. This pro-
cess, which we term Manifold Densification, artificially increases the local density of the
minority class in sparse regions.
The impact on the classifier is drastic: the decision boundary shifts from a simple
curve to a complex, multi-modal shape. Note the large new brown region that appears
in the top-right quadrant of the augmented plot. The model has “learned” a new valid
region of the feature space that was previously ignored, explaining the massive +20%
performance jump.
27

4.3.3 Decision Margin Corruption in the Starkey Dataset
Although augmentation is beneficial for sparse data, Figure 4.3 demonstrates why it can
fail on high-quality data. In theStarkeydataset (Seed 2862), the Representativeness strat-
egy caused a performance degradation of -3.84%.
Figure 4.3: Visual analysis of Decision Margin Corruption (Starkey, Seed 2862). The
Representativeness strategy selects central, typical examples (stars). However, in a dense
dataset, adding noise to these points blurs the separation between classes (Right), causing
the decision boundary to become jagged and less precise.
In the baseline state (Left), the classes are well-separated with high density (F1-Score>
96%). The decision boundaries are sharp and follow the natural gaps between clusters.
The Representativeness strategy selects the most “typical” points near the centroids of
these clusters (indicated by stars deep inside the class blobs).
However, the augmentation process injects noise into these central points, spreading
them outward toward the class boundaries (indicated by the dashed lines pushing out-
wards). Instead of reinforcing the class definition, this corrupts the decision margin. The
synthetic points fill the clean gaps that previously separated the classes.
The Random Forest, attempting to classify this noisy overlap, produces a highly irreg-
ular decision boundary with excessive complexity (Right). This over-fitting to synthetic
noise reduces the model’s ability to generalize to the clean test set, resulting in a net
loss of accuracy. This confirms that when a manifold is already well-defined, heuristic
augmentation often acts as a contaminant rather than a regularizer.
It is critical to highlight that this performance degradation is not a failure of the exper-
imental methodology, but rather a primary finding of this research. By systematically ob-
serving how noise is added to the natural differences between classes, we demonstrate that
geometric augmentation is fundamentally inappropriate for clean, well-separated mani-
folds, as it forces the model to overfit to an artificial overlap.
28

4.3.4 Feature Space Divergence in Car Dataset
The final case study explains the “null result” often observed in the Car Traffic dataset.
Figure 4.4 shows Seed 3832 under the Diversity strategy, where the net performance
improvement was exactly +0.00%.
Figure 4.4: Visual analysis of Feature Space Divergence (Car Traffic, Seed 3832). Due to
high object velocity, the geometric perturbation projects augmented points far away from
the original manifold (Right). The model learns to classify these “out-of-distribution
points” (pluses on the far left), but the decision boundary around the real data remains
unchanged.
This visualization captures a phenomenon driven by the physics of the domain. Because
cars travel at high velocities, the physical distance between GPS updates is large. Con-
sequently, a percentage-based perturbation (e.g., 50% of the segment length) results in a
massive geographical displacement.
Because the algorithm does not take into account the existence of absolute physical
constraints (such as road networks), the creation of these artificial paths results in trajec-
tories with a high chance of passing through buildings or off-road areas. As observed
by the 0.00% improvement, this lack of physical plausibility renders the augmented data
semantically useless to the classifier in urban contexts.
In the UMAP projection (Right), this is visible as Feature Space Divergence. The
augmented points (pluses) are projected far to the left, completely disconnected from
the original data cluster (circles). The dashed lines connecting parents to children are ex-
tremely long, indicating that the synthetic data no longer resemble the original distribution
therefore it is “out-of-distribution”.
The classifier successfully learns to classify these new “out-of-distribution” clusters,
creating complex decision regions on the far left of the plot. However, because these new
regions do not intersect with the original data manifold, the decision boundarywithinthe
dense test cluster remains virtually identical to the baseline. As a result, the classification
of the test set is unchanged, leading to the observed 0.00% improvement. This highlights
a critical physical limit of geometric augmentation for high-velocity domains.
29

4.4 Impact of Model Architecture
The impact of augmentation varied significantly depending on the machine learning al-
gorithm used. The results highlight how different model architectures react to synthetic
noise.
•Linear Models (Logistic Regression):These models showed the most binary re-
sponse. In the sparseFoxesdataset, where the linear decision boundary was ini-
tially poor, augmentation provided the largest relative gains by reshaping the class
distribution. However, in dense datasets likeCar Traffic, these models reached sat-
uration. Once the best possible linear boundary was found using the original data,
adding synthetic points provided no benefit. This confirms that linear models are
limited by their own simplicity rather than just data volume in high density scenar-
ios.
•Tree Ensembles (Random Forest, XGBoost):These models generally had the high-
est baseline scores, but also showed the highest sensitivity to bad augmentation. In
theStarkeydataset, Random Forest performance was significantly degraded when
using the Representativeness strategy (-1.16%). This indicates that tree based mod-
els, which create complex decision boundaries by splitting feature space, are prone
to overfitting the synthetic noise when it fills the gaps between classes.
•Neural Networks (MLP):The MLP showed a specific robustness in datasets where
tree based models plateaued. In both theAIS SubsetandStarkeydatasets, the Ran-
dom Forest model failed to improve or degrade. In contrast, the MLP achieved
statistically significant gains using the Uncertainty strategy (+1.61% and +3.18%
respectively). Although this trend was not universal across all datasets (Random
Forest outperformed MLP inFoxes), it suggests that the neural network was bet-
ter able to utilize the ambiguous examples selected by the Uncertainty strategy to
refine its probability estimates in dense data regimes.
4.5 Summary of Findings
The evaluation of systematic trajectory selection strategies reveals four main findings that
address the central research objectives of this thesis:
•Systematic Selection Reduces Risk:While systematic strategies did not always
guarantee a performance boost, they proved generally more robust than the Random
baseline. The Random strategy frequently resulted in performance degradation, par-
ticularly in theStarkeyandAISdatasets. Systematic strategies like Outlierness and
Uncertainty either provided gains or maintained parity, effectively acting as a more
robust alternative to naive sampling.
•Augmentation is Conditional on Data Scarcity:The results define a clear boundary
for when augmentation is useful. In the data scarceFoxesdataset, every strategy
worked, yielding gains. In the data richStarkeydataset, most strategies failed or
degraded performance. This proves that geometric augmentation acts primarily as
a regularizer: it is transformative when data is lacking, but can become a source of
corrupting noise when the dataset is already sufficient.
•Uncertainty Selection Aids in Dense Environments:In scenarios where the dataset
was large and dense (AIS and Starkey), standard geometric heuristics often failed.
30

The Uncertainty strategy was the only approach to yield statistically significant im-
provements in these difficult conditions, specifically for the MLP model. This indi-
cates that targeting the specific trajectories that confuse the model is more effective
than targeting geometric outliers when the data manifold is already well populated.
•Physical Limits of Percentage-Based Noise:The results from theCar Trafficdataset
reveal a technical limitation. The standard approach of defining the perturbation
radius as a percentage of segment length breaks down for high velocity objects.
This resulted in synthetic data being projected far outside the valid feature space
(Feature Space Divergence), rendering the augmentation mathematically valid but
practically useless for the classifier. This “null” finding confirms that standard ge-
ometric augmentation procedures are essentially out of phase with high-velocity
realms and require map-matching constraints to be viable.
31

5 Discussion
This thesis aims to answer a fundamental question: Can trajectories be systematically
selected for augmentation to improve classification performance? The preceding results
provide a nuanced and conditional answer. The findings indicate that while systematic
selection strategies generally offer a more robust alternative to random sampling, they
do not universally improve classification performance over the original baseline in all
contexts. Instead, the utility of these strategies is primarily determined by the quality
and density of the underlying data. While systematic approaches deliver improvements in
sparse and noisy regimes, they often reach a saturation point in high quality datasets where
the decision boundaries are already well defined. This section interprets these findings,
discusses their implications in the context of the existing literature, and contextualizes the
contributions of this work.
5.1 The Primacy of Selection: An Empirical Answer to a Known Gap
A primary finding of this study is that systematic selection strategies generally offer
distinct advantages over a naive random approach. Although random selection is often
volatile and prone to inducing performance degradation, systematic strategies provide a
more stable and effective method for identifying augmentation candidates. The results
demonstrate that the strategic selection of data is a critical determinant of augmenta-
tion success, especially in data scarce regimes.The foundational work by Haranwala et
al. [14] first demonstrated the viability of perturbation based augmentation but explicitly
acknowledged that their reliance on purely random selection was a key limitation, noting
that “innovating new techniques for ranking trajectories presents an exciting possibility.”
The findings in this thesis provide a direct and empirical answer to the gap they identified
by demonstrating that selection logic is a critical factor for augmentation success.
Although the later AugmenTRAJ framework [33] began to address this by offering
several predefined heuristic strategies, this work goes a step further. By providing a data
driven comparison of strategies grounded in core statistical properties (outlierness, di-
versity, representativeness, uncertainty), it confirms that how trajectories are selected de-
termines the stability of the model. Simply increasing the volume of training data is
insufficient; the strategic choice of which examples to generate is paramount to avoid the
volatility and performance degradation frequently observed in the random baseline. The
goal of these systematic strategies is not to claim universal performance dominance, but
rather to mitigate risk. When the standard method of augmenting data (random sampling)
is highly volatile, applying a systematic approach ensures that we do not unknowingly
degrade the model’s original base performance.
5.2 Interpreting the Strategy Mechanisms in Context
The varied performance of the systematic strategies offers deep insight into their under-
lying mechanisms and allows for a comparison with similar concepts in the literature.
The Outlierness based selection proved to be one of the most reliable performer in sparse
regimes, acting as a “boundary refiner.” This approach validates the practical implemen-
tation of the idea that the most informative samples for a classifier are often those near the
decision boundary. By augmenting the most unusual examples, this strategy effectively
forces the model to expand its decision region to encompass valid but rare trajectory pat-
terns.
32

Diversity based selection acts as a “feature space explorer.” Its use of clustering to
identify and sample from various groups of trajectories shares a philosophical similarity
with the work of Mirkhani et al. [36], who used clustering to identify and augment safety
critical driving scenarios. However, our results add a caveat to this approach: explor-
ing the feature space is beneficial only when the augmentation mechanism respects the
domain physics. In theCar Trafficdataset, diversity maximization led to feature space
divergence, creating synthetic data that are too distinct from the original manifold to be
useful.
Representativeness based selection offered diminishing returns or degradation in high
quality datasets. By reinforcing the “average” patterns, this strategy appears to compound
the density at the cluster centers. In dense datasets likeStarkey, this outward expansion
from the center resulted in the corruption of decision margins. This suggests that for
standard classification, the most valuable information for a model often lies not at the
class centroid, but at its boundaries.
Uncertainty based selection demonstrated a unique synergy with neural network ar-
chitectures. While tree based models often rejected augmentation in dense regimes, the
MLP model extracted value from the ambiguous examples selected by this strategy. This
effectively transfers the benefits of Active Learning to the augmentation domain, sug-
gesting that for non convex optimization problems, targeting the specific instances that
confuse the model is more robust than relying on geometric heuristics alone.
A notable observation across all datasets is the absence of a single “winning”strategy
that is universally effective. The results demonstrate a deep sensitivity between the selec-
tion strategy and the underlying model architecture. For instance, the Uncertainty strategy
frequently assisted the Multi-Layer Perceptron (MLP) by resolving ambiguous boundary
cases, but it had little to no positive effect on tree-based ensembles like Random Forest
on the same data. This inconsistency implies that selection strategies must be carefully
mapped to the learning dynamics of the chosen classifier, a complex relationship that
warrants deeper investigation in future research.
5.3 The Conditional Value of Augmentation
Perhaps the most crucial contribution of this thesis is the empirical demonstration that data
augmentation is not a universal panacea, but a powerful tool whose value is conditional.
The contrasting results from theStarkeyandFoxesdatasets provide clear evidence for this
principle.
The performance degradation on the high qualityStarkeydataset reveals a critical lim-
itation of simple perturbation techniques: when applied to sufficient, well separated data,
augmentation acts as a harmful “corrupting noise signal.” This finding serves as an im-
portant counterpoint to the generally positive results reported by Haranwala et al. [14] and
highlights a critical prerequisite for applying these methods. Augmentation functions best
as a repair mechanism for data deficiency rather than as a generic performance booster.
5.4 Physical Constraints and Domain Dynamics
The null results observed in theCar Trafficdataset highlight a critical dependency be-
tween the augmentation algorithm and the physical dynamics of the moving object. The
standard approach of defining the perturbation radius as a percentage of the segment
length implicitly assumes spatial continuity. However, high velocity objects create sparse,
long distance segments. Applying a percentage based perturbation to these segments re-
sults in “Kinematic Distortion”, projecting points far away from the road network.
33

This aligns with challenges seen in other domains, such as the work by Antotsiou et
al. [35] who sought to preserve the validity of augmented actions in imitation learning.
Future frameworks must incorporate absolute physical constraints rather than rely solely
on relative geometric ratios.
5.5 Implications of Per Dataset Optimization
A final critical contribution of this work is the validation of the hyperparameter opti-
mization strategy per data set. This approach goes beyond the static heuristics of Aug-
menTRAJ [33] and introduces a more advanced adaptive methodology. The fact that the
Optuna framework identified vastly different optimized configurations for each dataset
is a finding in its own right. The sparseFoxesdataset required aggressive augmentation
(40% selection, 5 variations), while the denseCar Trafficdataset tolerated only minimal
intervention.
This aligns with the principles of sophisticated selection mechanisms in other do-
mains, such as SelectAugment for image data [37], which advocate learningwhichand
howto augment rather than relying on fixed rules. By integrating Optuna, this thesis pro-
vides a methodological blueprint for applying this data driven philosophy to the trajectory
domain.
6 Conclusion and Future Work
This thesis established a systematic and scalable framework for selecting specific trajec-
tories for data augmentation. By comparing strategies based on outlierness, diversity,
representativeness, and prediction uncertainty, the research moved beyond simple ran-
dom sampling to provide a more controlled approach to mobility analysis. The results
show that systematic selection is generally safer and more stable than random selection,
although its success depends heavily on the dataset. The findings confirm that augmenta-
tion is most effective as a repair mechanism for sparse or fragmented data. In dense and
high quality datasets, even systematic augmentation can act as a corrupting noise signal
that reduces model accuracy by blurring the decision margins between classes.
The research also identified a clear physical limit to geometric augmentation in high
velocity domains. The results from the car traffic data demonstrated that percentage based
perturbations can lead to feature space divergence, where synthetic trajectories become
mathematically valid but practically useless because they no longer resemble real move-
ment patterns. These insights show that the strategic selection of data is not just a tech-
nical detail but a primary factor in whether augmentation succeeds. This work provides
a practical guide for using an optimized tuning process to identify exactly when and how
to apply synthetic data to improve machine learning models.
For future research, the following areas should be explored:
1.Tuning the perturbation radius:This study used a fixed radius of 50 percent for the
noise injection. Future work should include this radius as a parameter in the opti-
mization loop. Letting a tool like Optuna choose a smaller radius for high quality
datasets might prevent the performance degradation observed in this research and
allow for more subtle improvements.
2.Adding road network constraints:To fix the divergence seen in vehicle trajectories,
future algorithms should incorporate spatial constraints. This would ensure that
34

synthetic points are shifted only to locations that exist on valid road networks or
paths, preserving the semantic meaning of the movement in urban environments.
3.Testing other selection metrics:While this study tested five core strategies, other
methods for ranking trajectories could be investigated. Future research could ex-
plore selection based on the geometric complexity of a path or the specific contri-
bution of a trajectory to the overall class boundary, which may provide even better
results for linear models.
35

References
[1] X. Zhao, Z. Li, X. Zhang, S. Guo, and Y . Wu, “A survey on trajectory
generation methods with reinforcement learning,”Artificial Intelligence Review,
2023. [Online]. Available: https://doi.org/10.1007/s10462-023-10598-x
[2] W. Liu, X. Lu, M. Duan, and Z. Wang, “Road passenger load probability prediction
based on trajectory big data,”Applied Sciences, vol. 14, no. 17, p. 7756, 2024.
[Online]. Available: https://www.mdpi.com/2076-3417/14/17/7756
[3] S. Garrido-Carretero, G. Escribano-Avila, M. Peichl, J. Morales-González, and
J. M. Fedriani, “Multi-constellation, multi-frequency gnss collars improve precision
and accuracy in wildlife tracking,”The Journal of Wildlife Management, vol. 87,
no. 3, p. e22378, 2023. [Online]. Available: https://wildlife.onlinelibrary.wiley.com
/doi/10.1002/jwmg.22378
[4] D. Ribeiro de Almeida, C. de Souza Baptista, F. Gomes de Andrade, and A. Soares,
“A survey on big data for trajectory analytics,”ISPRS International Journal of Geo-
Information, vol. 9, no. 2, p. 88, 2020.
[5] F. H. Abreu, A. Soares, F. V . Paulovich, and S. Matwin, “A trajectory scoring tool
for local anomaly detection in maritime traffic using visual analytics,”ISPRS Inter-
national Journal of Geo-Information, vol. 10, no. 6, p. 412, 2021.
[6] R. Song, G. Spadon, R. Pelot, S. Matwin, and A. Soares, “Enhancing global mar-
itime traffic network forecasting with gravity-inspired deep learning models,”Sci-
entific reports, vol. 14, no. 1, p. 16665, 2024.
[7] E. Carlini, V . M. de Lira, A. Soares, M. Etemad, B. Brandoli, and S. Matwin, “Un-
derstanding evolution of maritime networks from automatic identification system
data,”GeoInformatica, pp. 1–25, 2022.
[8] A. Soares, R. Dividino, F. Abreu, M. Brousseau, A. W. Isenor, S. Webb, and
S. Matwin, “Crisis: Integrating ais and ocean data streams using semantic web
standards for event detection,” in2019 International conference on military com-
munications and information systems (ICMCIS). IEEE, 2019, pp. 1–7.
[9] G. Spadon, J. Kumar, D. Eden, J. van Berkel, T. Foster, A. Soares, R. Fablet,
S. Matwin, and R. Pelot, “Multi-path long-term vessel trajectories forecasting with
probabilistic feature fusion for problem shifting,”Ocean Engineering, vol. 312, p.
119138, 2024.
[10] M. D. Ferreira, G. Spadon, A. Soares, and S. Matwin, “A semi-supervised method-
ology for fishing activity detection using the geometry behind the trajectory of mul-
tiple vessels,”Sensors, vol. 22, no. 16, p. 6063, 2022.
[11] P. Adibi, F. Pranovi, A. Raffaetà, E. Russo, C. Silvestri, M. Simeoni, A. Soares, and
S. Matwin, “Predicting fishing effort and catch using semantic trajectories and ma-
chine learning,” inInternational Workshop on Multiple-Aspect Analysis of Semantic
Trajectories. Springer International Publishing Cham, 2019, pp. 83–99.
36

[12] Y . J. Haranwala, S. Haidri, T. S. Tricco, V . P. da Fonseca, and A. Soares, “A dash-
board tool for mobility data mining preprocessing tasks,” in2022 23rd IEEE In-
ternational Conference on Mobile Data Management (MDM). IEEE, 2022, pp.
278–281.
[13] S. Haidri, Y . J. Haranwala, V . Bogorny, C. Renso, V . P. da Fonseca, and A. Soares,
“PTRAIL — A python package for parallel trajectory data preprocessing,”Soft-
wareX, vol. 19, p. 101176, 2022.
[14] Y . J. Haranwala, G. Spadon, C. Renso, and A. Soares, “A data augmentation al-
gorithm for trajectory data,” in1st ACM SIGSPATIAL International Workshop on
Methods for Enriched Mobility Data: Emerging issues and Ethical perspectives
2023 (EMODE ’23). Hamburg, Germany: ACM, November 2023, pp. 1–5, [On-
line]. Available at: doi:10.1145/3615885.3628008.
[15] M. D. Ferreira, J. Campbell, E. Purney, A. Soares, and S. Matwin, “Assessing com-
pression algorithms to improve the efficiency of clustering analysis on ais vessel
trajectories,”International Journal of Geographical Information Science, vol. 37,
no. 3, pp. 660–683, 2023.
[16] H. Lee, S. Kim, and J. Park, “Deep learning for trajectory classification: A
survey,”Pattern Recognition, vol. 135, p. 109084, 2023. [Online]. Available:
https://doi.org/10.1016/j.patcog.2022.109084
[17] A. S. Júnior, C. Renso, and S. Matwin, “Analytic: An active learning system for
trajectory classification,”IEEE computer graphics and applications, vol. 37, no. 5,
pp. 28–39, 2017.
[18] Y . Tavakoli, L. Peña-Castillo, and A. Soares, “A study on the geometric and kine-
matic descriptors of trajectories in the classification of ship types,”Sensors, vol. 22,
no. 15, p. 5588, 2022.
[19] Y . Wang and Y . Y . Tang, “Trajectory clustering analysis,” inMachine Learning for
Data Science Handbook, L. Rokach, O. Maimon, and E. Shmueli, Eds. Springer,
2023, pp. 171–189. [Online]. Available: https://doi.org/10.1007/978-3-031-24628
-9_10
[20] M. T. Johnson and E. L. Smith, “A three-dimensional hail trajectory clustering
technique,”Monthly Weather Review, vol. 151, no. 9, pp. 3001–3020, 2023.
[Online]. Available: https://doi.org/10.1175/MWR-D-22-0345.1
[21] D. T. Lan and S. Yoon, “Trajectory clustering-based anomaly detection in indoor
human movement,”Sensors, vol. 23, no. 6, p. 3318, 2023. [Online]. Available:
https://doi.org/10.3390/s23063318
[22] W. Tan, M. Liu, and L. Zhao, “Motion segmentation of pedestrian trajectories
using angular gaussian mixture model,” inProceedings of the 2023 5th World
Symposium on Software Engineering (WSSE ’23). ACM, 2023, pp. 102–110.
[Online]. Available: https://doi.org/10.1145/3631991.3632040
[23] M. Etemad, A. Soares, E. Etemad, J. Rose, L. Torgo, and S. Matwin, “Sws: an
unsupervised trajectory segmentation algorithm based on change detection with in-
terpolation kernels,”GeoInformatica, vol. 25, no. 2, pp. 269–289, 2021.
37

[24] A. S. Junior, V . C. Times, C. Renso, S. Matwin, and L. A. Cabral, “A semi-
supervised approach for the semantic segmentation of trajectories,” in2018 19th
IEEE international conference on mobile data management (MDM). IEEE, 2018,
pp. 145–154.
[25] A. Soares Júnior, B. N. Moreno, V . C. Times, S. Matwin, and L. d. A. F. Cabral,
“Grasp-uts: an algorithm for unsupervised trajectory segmentation,”International
Journal of Geographical Information Science, vol. 29, no. 1, pp. 46–68, 2015.
[26] G. Spadon, M. D. Ferreira, A. Soares, and S. Matwin, “Unfolding ais transmission
behavior for vessel movement modeling on noisy data leveraging machine learning,”
IEEE Access, vol. 11, pp. 18 821–18 837, 2022.
[27] L. May Petry, A. Soares, V . Bogorny, B. Brandoli, and S. Matwin, “Challenges in
vessel behavior and anomaly detection: From classical machine learning to deep
learning,” inAdvances in Artificial Intelligence: 33rd Canadian Conference on Ar-
tificial Intelligence, Canadian AI 2020, Ottawa, ON, Canada, May 13–15, 2020,
Proceedings 33. Springer, 2020, pp. 401–407.
[28] E. Carlini, V . M. de Lira, A. Soares, M. Etemad, B. B. Machado, and S. Matwin,
“Uncovering vessel movement patterns from ais data with graph evolution analysis,”
inEDBT/ICDT Workshops, 2020.
[29] A. Nordling, “Trajectory Data Augmentation Framework,” 2026. [Online].
Available: https://doi.org/10.5281/zenodo.19323839
[30] J. Chen, D. Tam, C. Raffel, M. Bansal, and D. Yang, “An empirical survey of
data augmentation for limited data learning in nlp,”Transactions of the Association
for Computational Linguistics, vol. 11, pp. 191–211, 2023. [Online]. Available:
https://aclanthology.org/2023.tacl-1.12/
[31] C. Cao, F. Zhou, Y . Dai, J. Wang, and K. Zhang, “A survey of mix-based
data augmentation: Taxonomy, methods, applications, and explainability,”ACM
Computing Surveys, vol. 57, no. 2, pp. 1–38, 2024. [Online]. Available:
https://dl.acm.org/doi/10.1145/3696206
[32] M. Xu, S. Yoon, A. Fuentes, and D. S. Park, “A comprehensive survey of image
augmentation techniques for deep learning,”Pattern Recognition, vol. 137, p.
109347, 2023. [Online]. Available: https://doi.org/10.1016/j.patcog.2023.109347
[33] Y . J. Haranwala, “AugmenTRAJ: A framework for point-based trajectory data
augmentation,” Master’s thesis, Memorial University of Newfoundland and
Labrador, Department of Computer Science, 2023, [Online]. Available at:
doi:10.48550/arXiv.2311.15097. Accessed: 2024-03-15.
[34] D. Agrawal, M. König, J. Buhmann, R. Sumner, and M. Guay, “Trajec-
tory augmentation for robust neural locomotion controllers,” inMIG ’23: Mo-
tion, Interaction and Games. ACM, 2023, pp. 1–11, [Online]. Available at:
doi:10.1145/3623267.3623274.
[35] D. Antotsiou, C. Ciliberto, and T.-K. Kim, “Adversarial imitation learning with tra-
jectorial augmentation and correction,” in2021 IEEE International Conference on
Robotics and Automation (ICRA). IEEE, 2021, pp. 3342–3348, [Online]. Available
at: doi:10.1109/ICRA48506.2021.9561915.
38

[36] H. Mirkhani, B. Khamidehi, and K. Rezaee, “Augmenting safety-critical driving
scenarios while preserving similarity to expert trajectories,” in2024 IEEE Intel-
ligent Vehicles Symposium (IV). IEEE, 2024, pp. 1–6, [Online]. Available at:
doi:10.1109/IV55156.2024.10588830.
[37] S. Lin, Z. Zhang, X. Li, and Z. Chen, “SelectAugment: Hierarchical deterministic
sample selection for data augmentation,” inThe Thirty-Seventh AAAI Conference
on Artificial Intelligence (AAAI-23). AAAI Press, 2023, pp. 1892–1900, [Online].
Available at: doi:10.1609/aaai.v37i2.25247.
[38] C. L. da Silva, L. M. Petry, and V . Bogorny, “A survey and comparison of
trajectory classification methods,” in2019 8th Brazilian Conference on Intelli-
gent Systems (BRACIS). IEEE, 2019, pp. 479–484, [Online]. Available at:
doi:10.1109/BRACIS.2019.00089.
[39] E. M. Knorr and R. T. Ng, “A unified approach for mining outliers,” inProceed-
ings of the 1997 conference of the Centre for Advanced Studies on Collaborative
research, 1997, p. 11.
[40] S. Lai, J. Bêty, and D. Berteaux, “Movement tactics of a mobile predator in a meta-
ecosystem with fluctuating resources: the arctic fox in the high arctic,”Oikos, vol.
126, no. 7, pp. 937–947, 2017.
[41] M. J. Wisdom,The Starkey Project: a synthesis of long-term studies of elk and mule
deer. Lawrence, Kansas: Alliance Communications Group, 2005, rep. PNW-GTR-
634.
39

Appendix 1: Source Code and Reproducibility
To ensure full transparency and reproducibility of the results discussed in this thesis, the
complete Python framework has been open-sourced. The repository includes the data pre-
processing scripts, the systematic selection algorithms, the multi-core feature extraction
optimized with Numba, and the Optuna hyperparameter optimization database.
GitHub Repository:https://github.com/adamnordling/master-thesis-t
rajectory-data-augmentation
A
