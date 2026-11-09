---
title: 'Optimizing Marketing Budgets for Social Influence: A Generalized Fractional Incentives Framework'
url: https://arxiv.org/abs/2610.25823
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Abhishek K. Umrawal
- Akhil Bhimaraju
- Eliot W. Robson
- Lav R. Varshney
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.25823
pages: 28
chars: 77611
fetched_at: '2026-11-08T13:31:05+00:00'
kb_version: 1
---

# Optimizing Marketing Budgets for Social Influence: A Generalized Fractional Incentives Framework

Optimizing Marketing Budgets for Social Influence: A
Generalized Fractional Incentives Framework
Abhishek K. Umrawal†
University of Illinois Urbana-Champaign, Urbana, IL 61801, USA, aumrawal@illinois.edu
Akhil Bhimaraju
University of Illinois Urbana-Champaign, Urbana, IL 61801, USA, akhilb3@illinois.edu
Eliot W. Robson
Narmi, New York, NY 10016, USA, eliot.robson24@gmail.com
Lav R. Varshney
Stony Brook University, Stony Brook, NY 11794 USA, lav.varshney@stonybrook.edu
Marketing managers routinely allocate limited budgets across individuals in social networks whose responsiveness and
influence vary substantially. We study the problem of Budgeted Generalized Fractional Influence Maximization (BGFIM),
which captures the allocation of continuous levels of marketing spend across users in the presence of heterogeneous
response and network spillovers. In this framework, adoption probabilities are governed by user-specific response functions
that capture both baseline propensity and marginal responsiveness, while incentive costs vary across users. We propose
a scalable solution approach based on a discrete greedy procedure with provable approximation guarantees, enabling
tractable optimization under realistic budget constraints. Our formulation generalizes prior influence maximization models
by allowing heterogeneous response and cost structures, providing a more flexible representation of targeted marketing
interventions. Using experiments on multiple large-scale networks, we show that continuous allocation strategies can
outperform standard heuristics and improve influence outcomes under heterogeneous conditions, and we illustrate how
the framework can support profit-oriented decision making by identifying budget levels that balance marginal returns and
costs. Overall, our results highlight the value of fine-grained budget allocation in networked marketing environments and
offer a scalable approach for data-driven marketing resource allocation.
Key words: marketing resource allocation, social networks, influence maximization, heterogeneous response, targeted
incentives, information diffusion, network effects, approximation algorithms
1. Introduction
The rapid proliferation of online social networks has transformed the landscape of modern communication
and commerce, positioning digital platforms as central hubs for consumer engagement and product promotion
(Aral et al. 2013, Holt 2016, Lobel et al. 2017, Rehman et al. 2022). This evolution has catalyzed the
emergence of a multi-billion-dollar “influencer economy,” wherein firms strategically allocate substantial
marketing budgets to incentivize individuals—often social media influencers—to adopt and advocate for
† Abhishek K. Umrawal is the corresponding author.
1
arXiv:2610.25823v1  [cs.SI]  19 Oct 2026

Budget Generalized Fractional Influence Maximization
2
products, services, or ideas (Gupta and Steenburgh 2008, Aral 2020, Pan et al. 2025). Influencer marketing
has proven to be a powerful tool for shaping consumer attitudes and purchase intentions, with effectiveness
driven by factors such as influencer credibility, social identity, and content value (Vrontis et al. 2021, Pan
et al. 2025). A growing body of research in marketing and operations has examined the role of networks
in shaping adoption and optimal targeting decisions, highlighting the importance of accounting for both
individual responsiveness and network spillovers in designing effective campaigns (Goldenberg et al. 2001b,
Libai et al. 2013, Mallipeddi et al. 2022, Kanuri et al. 2018). These patterns are also reflected in practitioner
reports and industry examples, which illustrate how influencer campaigns often combine creator–brand fit,
influencer seeding, and targeted incentives to drive engagement and product adoption (Nain 2023, Naceva
2026, Zalani 2025). In this complex and rapidly evolving environment, the efficient allocation of finite
marketing resources across individuals in a network has become a pressing managerial challenge, demanding
data-driven approaches to maximize campaign reach and return on investment (Gupta and Steenburgh 2008,
Lang et al. 2022).
To promote their products and services in such networked environments, firms must decide which indi-
viduals to target and how to allocate incentives so as to maximize downstream diffusion (Kempe et al. 2003,
Aral and Walker 2012). This decision problem has been studied in the literature on influence maximization,
which models how the selection of initial adopters can drive cascading adoption through social networks
(Kempe et al. 2003, Goyal et al. 2011a, Borgs et al. 2014). In many practical settings, firms provide monetary
incentives or discounts to encourage adoption and advocacy, with the likelihood of engagement increasing
with the level of the incentive. However, marketing budgets are inherently limited, requiring firms to balance
the potential influence of individuals against the costs of targeting them. This trade-off between influence
potential and cost has motivated a substantial body of work on budget-constrained influence maximiza-
tion (Goyal et al. 2011a, Borgs et al. 2014). A common assumption in this literature is that incentives are
binary—individuals are either fully targeted or not at all—which fails to capture the more nuanced strategies
observed in modern marketing campaigns, where firms frequently employ partial or personalized incentives
(Vondr´ak 2008, Calinescu et al. 2011, Yang et al. 2016, Chen et al. 2020).
While allowing fractional or continuous incentives provides a more flexible alternative to binary targeting,
existing approaches continue to rely on restrictive modeling assumptions that limit their applicability in mar-
keting settings. In particular, prior work often assumes a direct equivalence between the level of an incentive
and the probability of user adoption (Umrawal et al. 2023a, 2026a), effectively treating incentives and behav-
ioral responses as interchangeable. This assumption is difficult to justify in practice, as it ignores substantial
heterogeneity in consumer behavior: some individuals may adopt with minimal incentives due to inherent
affinity, while others may remain unresponsive even under substantial incentives. For example, a dedicated
early adopter might activate with a 5% discount, while a brand-loyal customer of a competing product
may remain unresponsive even under much larger incentives (e.g., 20%). These behavioral differences are

Budget Generalized Fractional Influence Maximization
3
well-documented in the marketing literature, which emphasizes the importance of consumer segmentation
and differential responsiveness to promotional stimuli (Goldenberg et al. 2001a, Libai et al. 2013, Aral
et al. 2013). Furthermore, these models do not adequately account for variation in the cost of targeting
different individuals, which is a central feature of real-world marketing campaigns. As emphasized in the
marketing literature, differences in baseline preferences, responsiveness to incentives, and economic costs
play a critical role in determining the effectiveness of targeted interventions (Goldenberg et al. 2001b, Libai
et al. 2013). These limitations highlight the need for models that can jointly capture heterogeneous responses
to incentives and heterogeneous costs within a unified framework for budget allocation in networks.
To address these limitations, we study the problem of Budgeted Generalized Fractional Influence Maxi-
mization (BGFIM), which models the allocation of marketing resources across individuals in a network in
the presence of heterogeneous response and network spillovers. In our framework, firms assign continuous
levels of incentives to users subject to a budget constraint, and adoption probabilities are governed by
user-specific response functions that capture both baseline propensity and marginal responsiveness. This
formulation separates the economic decision of how much incentive to allocate from the behavioral response
it induces, allowing for a more realistic representation of consumer heterogeneity. In addition, the model
incorporates heterogeneous costs of targeting individuals, reflecting differences in influencer compensation
and the resources required to engage different individuals. We propose a scalable solution approach based
on a discrete greedy procedure with provable approximation guarantees, enabling tractable optimization
in large-scale networks. We evaluate the performance of the approach through experiments on multiple
real-world networks and further illustrate how the framework can be used to support profit-oriented decision
making by identifying budget levels that balance marginal returns and costs.
1.1. Contributions
This paper makes three main contributions.
1.Decision framework for budget allocation in networks.We formulate the Budgeted Generalized
Fractional Influence Maximization (BGFIM) problem, which captures the challenge of allocating limited
marketing resources across individuals in a network in the presence of heterogeneous response and network
spillovers. By allowing continuous levels of incentives, heterogeneous response functions, and heterogeneous
costs, the framework provides a more realistic representation of targeted marketing interventions than existing
binary or homogeneous models.
2.Scalable solution approach with theoretical guarantees.We propose a discrete greedy algorithm that
provides a tractable approach to solving the BGFIM problem at scale and establishes provable approximation
guarantees for its performance. The method is designed to account jointly for influence generation and
incentive costs, enabling efficient optimization under realistic budget constraints.

Budget Generalized Fractional Influence Maximization
4
3.Quantitative insights for marketing resource allocation.Through experiments on multiple large-
scale networks, we demonstrate that continuous allocation strategies can outperform standard heuristics,
particularly in settings with heterogeneous response and costs. We further show how the framework can be
used to support profit-oriented decision making by identifying budget levels that balance marginal returns
and costs, providing actionable guidance for marketing campaign design.
1.2. Organization
The remainder of the paper is organized as follows. Section 2 reviews the conceptual motivation and related
literature. Section 3 introduces the modeling framework, notation, and the Budgeted Generalized Fractional
Influence Maximization (BGFIM) problem. Section 4 presents our solution approach, including the discrete
greedy algorithm and its theoretical approximation guarantees. Section 5 reports computational experiments
on real-world social networks and examines the use of nested solutions for profit-oriented budget selection.
Finally, Section 6 concludes and outlines directions for future research.
2. Conceptual Motivation and Related Literature
Diffusion and word-of-mouth processes are foundational to marketing science, where they are used to study
how products, behaviors, and information spread through populations. Classic models, such as the Bass
diffusion framework (Bass 1969) and its network-based extensions (Goldenberg et al. 2001b), highlight how
individual adoption decisions aggregate into population-level dynamics through both external influence and
interpersonal interactions. Subsequent work has emphasized the central role of social networks in shaping
these processes, demonstrating that peer effects, social reinforcement, and network structure critically
determine the speed and extent of diffusion (Libai et al. 2013, Aral et al. 2013, Lobel et al. 2017). In
modern digital environments, these mechanisms are further amplified by online platforms, where repeated
exposure, homophily, and algorithmic content curation influence both adoption behavior and downstream
word-of-mouth dynamics (Aral 2020, Pan et al. 2025). Collectively, this body of work underscores that
diffusion is inherently a networked phenomenon, in which both individual heterogeneity and interconnected
social influence must be accounted for to accurately describe and predict market outcomes.
Building on this foundation, a central concern in marketing is how firms can actively shape diffusion
outcomes through targeted interventions. A growing literature examines how firms allocate resources across
consumers and influencers to maximize engagement, adoption, and long-term value (Libai et al. 2013, Gupta
and Steenburgh 2008, Mallipeddi et al. 2022). These studies emphasize that effective marketing strategies
must account not only for who is targeted, but also for when, how, and with what intensity interventions
are deployed. Empirical and field-based research highlights the importance of timing, exposure frequency,
and content design in shaping consumer response, particularly in digital environments where users are
repeatedly exposed to competing signals (Kanuri et al. 2018, Pan et al. 2025). Moreover, the effectiveness

Budget Generalized Fractional Influence Maximization
5
of targeted interventions depends critically on network spillovers: influencing one individual can generate
indirect effects through their social connections, amplifying or attenuating the overall impact of marketing
actions. These insights collectively point to the need for decision frameworks that integrate individual-level
targeting with network-mediated spillovers, allowing firms to allocate limited marketing budgets in a manner
that accounts for both direct and indirect effects.
To operationalize marketing interventions in networked settings, researchers have long studied how
behaviors and information spread through social contagion processes. Early work in sociology and marketing
models adoption as arising from interpersonal influence and word-of-mouth interactions, where individuals
are affected by the behavior of their peers (Granovetter 1978, Schelling 2006, Goldenberg et al. 2001a,b).
Building on these insights, Domingos and Richardson (2001) introduced the idea of leveraging network
structure for targeted marketing, framing customer selection as a problem of maximizing network value.
This perspective was formalized by Kempe et al. (2003), who introduced the influence maximization (IM)
problem and provided a unified framework for studying how targeted interventions can maximize downstream
diffusion in networks.
At the core of this framework are canonical diffusion models that formalize how influence propagates
through networks. The Independent Cascade (IC) and Linear Threshold (LT) models, introduced in Kempe
et al. (2003), provide two widely used representations of diffusion dynamics. The IC model captures stochastic
contagion through pairwise interactions, closely related to word-of-mouth diffusion processes studied in
marketing (Goldenberg et al. 2001a,b), whereas the LT model captures cumulative peer influence through
threshold-based adoption rules rooted in sociological models of collective behavior (Granovetter 1978,
Schelling 2006). Under these models, the expected influence function is monotone and submodular, enabling
greedy algorithms with strong approximation guarantees (Kempe et al. 2003, Nemhauser et al. 1978). More
recent extensions enrich these models to better capture behavioral dynamics, including reinforcement effects
such as the Pressure Threshold (PT) model (Stutsman et al. 2026, Umrawal et al. 2026b).
Building on these diffusion models, a substantial body of work in computer science and operations research
has developed scalable algorithms for influence maximization. Early contributions focused on improving
the efficiency of greedy methods, including the CELF algorithm and its variants (Leskovec et al. 2007,
Goyal et al. 2011b), followed by sampling-based techniques that enable near-linear-time approximation
on large networks (Borgs et al. 2014, Tang et al. 2015). Subsequent work has incorporated structural
properties of networks to further improve scalability and solution quality, including community-aware
methods and decomposition-based approaches (Umrawal and Aggarwal 2023, Umrawal et al. 2023b, Robson
and Umrawal 2025). In parallel, extensions to adaptive and online settings have been developed to account
for uncertainty, learning, and dynamic environments (Agarwal et al. 2022, Nie et al. 2022, Xu and Umrawal
2026). Collectively, this literature provides powerful optimization tools for implementing network-based
marketing strategies at scale.

Budget Generalized Fractional Influence Maximization
6
Complementing these model-based approaches, a parallel stream of research has developed data-driven
methods that infer influence and model user response directly from observed behavior. In network science,
credit distribution approaches estimate influence by attributing observed downstream adoption to upstream
nodes based on cascade data, avoiding reliance on explicit generative diffusion assumptions (Goyal et al.
2011a). In marketing and operations, related work models engagement as a function of exposure rather than
propagation. For example, Mallipeddi et al. (2022) develops an empirical framework for influencer marketing
in which user response depends on cumulative exposure to multiple influencers, incorporating effects such as
repetition and temporal decay. These data-driven approaches provide greater empirical realism by capturing
exposure effects and behavioral heterogeneity, but they typically abstract away from explicit modeling of
incentive allocation and economic decision-making in networked settings.
Beyond binary targeting decisions, recent research has sought to better align influence maximization mod-
els with the realities of marketing practice by allowing for more flexible allocation of resources. In particular,
a growing body of work considers fractional or continuous variants of the problem, in which firms can assign
varying levels of incentives or effort across individuals rather than making purely discrete selections (Yang
et al. 2016, Chen et al. 2020, Bhimaraju et al. 2024). These formulations capture the intuition that marketing
interventions—such as discounts, payments to influencers, or promotional efforts—can be adjusted con-
tinuously to influence consumer behavior. Algorithmically, these models introduce additional complexity,
requiring optimization over high-dimensional continuous decision spaces while preserving tractable approx-
imation guarantees. Recent advances have addressed these challenges through discretization techniques,
lattice-based methods, and scalable greedy approximations (Chen et al. 2020, Umrawal et al. 2023a). Related
work has also explored extensions that incorporate structural features such as community organization and
heterogeneous influence pathways, further improving the effectiveness of network interventions in practice
(Umrawal and Aggarwal 2023, Umrawal et al. 2023b, Robson and Umrawal 2025).
Despite these advances, existing fractional formulations rely on simplifying assumptions that limit their
applicability in marketing contexts. A common modeling approach assumes a direct mapping between the
level of incentive assigned to an individual and their probability of adoption, effectively treating economic
inputs and behavioral responses as interchangeable (Umrawal et al. 2023a, 2026a). This abstraction over-
looks well-documented heterogeneity in consumer behavior, including variation in baseline preferences,
responsiveness to incentives, and sensitivity to social influence (Goldenberg et al. 2001b, Libai et al. 2013).
Moreover, most existing models do not explicitly account for heterogeneous costs of targeting individuals,
despite their central importance in real-world settings such as influencer compensation, customer acquisition,
and platform-specific pricing. These limitations highlight a gap between existing optimization frameworks
and the behavioral and economic realities of modern marketing environments.
Taken together, these streams of research highlight both the strengths and the limitations of existing
approaches to network-based marketing. Prior work provides a rich set of tools for modeling diffusion,

Budget Generalized Fractional Influence Maximization
7
designing targeted interventions, and optimizing influence in large-scale networks. However, a key gap
remains in integrating the economic and behavioral dimensions of marketing decision-making within these
frameworks. In particular, existing models do not fully capture the joint role of heterogeneous response
functions, continuous incentive allocation, and heterogeneous costs in shaping diffusion outcomes.
Motivated by these limitations, we develop a framework that more closely aligns influence optimization
with the realities of modern marketing environments. Our approach builds on the influence maximization
paradigm while generalizing it to allow for flexible incentive-response relationships and heterogeneous cost
structures across individuals. By explicitly separating the allocation decision from the resulting behavioral
response, the framework captures the interplay between economic incentives and consumer heterogeneity in
a networked setting. This perspective bridges insights from marketing, network science, and optimization,
providing a foundation for studying how firms can allocate limited resources to maximize both direct and
spillover effects in social networks.
3. Mathematical Model and Problem Formulation
Marketing interventions in social networks rely on interpersonal influence, where adoption by one individual
can affect the behavior of others through interactions such as recommendations, content sharing, and peer
endorsement, as reflected in observable engagement actions (e.g., likes, shares, or reposts), giving rise to
diffusion across the network. To capture these influence pathways, we model the social network as a directed
graph𝐺=(𝑉,𝐸), where each node𝑣∈𝑉represents an individual user and each directed edge(𝑣,𝑢)∈𝐸
indicates a potential influence relationship from user𝑣to user𝑢. That is, if(𝑣,𝑢)∈𝐸, then user𝑣may affect
the likelihood that user𝑢adopts a product or behavior. We associate each edge(𝑣,𝑢)∈𝐸with an influence
probability𝑒 𝑣,𝑢∈[0,1], capturing the strength of the relationship between users. These probabilities may
reflect factors such as interaction frequency, trust, or historical engagement, and in practical settings can
be estimated from observed diffusion or interaction data (Goyal et al. 2010, Gomez-Rodriguez et al. 2010).
This graph-based abstraction reflects the structure of online platforms, where connections encode pathways
through which influence can spread; the neighborhood of a node𝑣, denoted byN 𝑣 ={𝑢∈𝑉:(𝑣,𝑢)∈𝐸},
consists of all users that𝑣can directly influence.
As discussed in Section 2, diffusion models provide a framework for describing how adoption and
information propagate through social networks. To model how adoption propagates in our setting, we adopt
the independent cascade (IC) diffusion model (Kempe et al. 2003), which provides a tractable and widely used
representation of stochastic influence spread. Under this model, time evolves in discrete steps𝑢=0,1,2,...,
and once a user becomes active, they are given a single opportunity to influence each inactive neighbor
independently with probability𝑒 𝑣,𝑢 . If the activation attempt succeeds, the neighbor becomes active in the
next time step; otherwise, no further attempts are made along that edge. Starting from an initial set of active

Budget Generalized Fractional Influence Maximization
8
users𝑆⊆𝑉at time𝑢=0, the diffusion process unfolds through successive rounds of such influence attempts
until no further activations occur.
To formalize the diffusion process, let
𝑌(𝑣) 𝑢 =
(
1,if node𝑣is active at time𝑢,
0,otherwise.
The diffusion isprogressive, meaning that nodes can switch from inactive to active, but not back.
Definition 1 (Influence Function).Given a seed set𝑆⊆𝑉, the influence𝜎(𝑆)is defined as the
expected number of active nodes at the end of the diffusion process:
𝜎(𝑆)=E
"∑︁
𝑣∈𝑉
𝑌(𝑣) 𝑇

𝑌(𝑣) 0 =1∀𝑣∈𝑆, 𝑌 (𝑣) 0 =0∀𝑣∉𝑆 # ,
where𝑇denotes the (random) time at which the diffusion process terminates.
The influence function𝜎: 2 𝑉→R≥0 captures the total reach generated by targeting an initial set of users.
Definition 2 (Monotonicity).A set function𝑓: 2 𝑉→R≥0 is monotone if for any𝐴⊆𝐵⊆𝑉, we have
𝑓(𝐴)≤𝑓(𝐵).
Definition 3 (Submodularity).A set function𝑓: 2 𝑉→R≥0 is submodular if for any𝐴⊆𝐵⊆𝑉and
any node𝑣∉𝐵, it holds that
𝑓(𝐴∪{𝑣})−𝑓(𝐴)≥𝑓(𝐵∪{𝑣})−𝑓(𝐵).
Lemma 1(Kempe et al. (2003)).Under the IC model, the influence function𝜎(·)is monotone and sub-
modular.
Monotonicity reflects the idea that targeting additional users cannot reduce the expected spread of influ-
ence. Submodularity captures diminishing returns: the marginal benefit of adding a new user is larger when
few users have already been targeted. In marketing terms, early targeted users can reach previously untapped
segments of the network, whereas additional users increasingly generate overlapping influence.
Problem 1 (Discrete Influence Maximization (DIM)).The classical influence maximization prob-
lem seeks to identify a seed set𝑆⊆𝑉of size at most𝑘that maximizes the influence function𝜎(𝑆):
arg max
𝑆⊆𝑉
𝜎(𝑆)
s.t.|𝑆|≤𝑘.
Problem 1 is known to be NP-hard (Kempe et al. 2003), reflecting the combinatorial complexity of selecting
an optimal set of users in large networks.
While the discrete formulation provides important structural insights, it abstracts away from key features of
practical marketing interventions. In many applications, firms do not make purely binary targeting decisions;

Budget Generalized Fractional Influence Maximization
9
instead, they allocate varying levels of incentives across users, resulting in heterogeneous and probabilistic
adoption behavior (Domingos and Richardson 2001, Goldenberg et al. 2001a,b, Aral et al. 2009, Iyengar
et al. 2011, Yoganarasimhan 2012, Yang et al. 2016). Such practices are commonly observed in referral
programs and targeted promotional campaigns, where the intensity of incentives influences the likelihood of
user participation (Ryu and Feick 2007, Schmitt et al. 2011). This motivates the development of more general
fractional models that accommodate continuous decision variables and user-specific response functions.
Motivated by the need to model heterogeneous and non-binary marketing interventions, we generalize the
discrete formulation by allowing continuous decision variables. Specifically, instead of selecting a binary
seed set𝑆⊆𝑉, we consider a vectorx=(𝑥 1,...,𝑥 𝑛)∈[0,1] 𝑛, where𝑥 𝑣 denotes the level of incentive or
marketing effort allocated to user𝑣.
We assume that each user𝑣∈𝑉becomes active at time𝑢=0with probability𝑓 𝑣(𝑥 𝑣), where𝑓 𝑣 :[0,1]→
[0,1]is a non-decreasing function capturing how incentives translate into initial adoption probabilities. This
formulation allows for heterogeneous user responses to marketing interventions, reflecting differences in
preferences, responsiveness, and baseline propensity to adopt. The subsequent diffusion process then evolves
according to the same independent cascade (IC) dynamics as in the discrete setting.
Definition 4 (Continuous Influence Function).Given an allocation vectorx∈[0,1] 𝑛, the expected
influence is defined as
˜𝜎(x)=E
"∑︁
𝑣∈𝑉
𝑌(𝑣) 𝑇

𝑌(𝑣) 0 =1with probability𝑓 𝑣(𝑥 𝑣)independently for each𝑣∈𝑉 # .
The function˜𝜎:[0,1] 𝑛→R≥0 captures the expected spread of influence resulting from heterogeneous
and probabilistic seeding induced by continuous marketing actions.
An equivalent and useful interpretation expresses the model in terms of a distribution over random seed
sets. Let𝑆 0⊆𝑉denote the random set of nodes activated at time0. Then the expected influence can be
written as
˜𝜎(x)=E 𝑆0[𝜎(𝑆 0)|x ],
where𝜎(𝑆 0)denotes the expected cascade size under the IC model starting from seed set𝑆0. This perspective
highlights that the continuous formulation can be viewed as inducing a probabilistic relaxation of the discrete
influence maximization problem.
The general formulation above allows for flexibility in modeling how incentives translate into adoption
probabilities. A natural and widely studied special case assumes a linear relationship, i.e.,𝑓 𝑣(𝑥 𝑣)=𝑥 𝑣 for
all𝑣∈𝑉. Under this assumption, each component𝑥 𝑣 can be interpreted directly as the probability that user
𝑣is initially activated, and the random seed set𝑆 0 is generated by including each𝑣independently with
probability𝑥 𝑣. In this case, the expected influence function˜𝜎(x)coincides with the multilinear extension of

Budget Generalized Fractional Influence Maximization
10
the discrete influence function𝜎(·)associated with the independent cascade model (Umrawal et al. 2023a,
2026a).
While this identity-based formulation admits strong algorithmic guarantees, it imposes a restrictive
assumption that the level of incentive directly corresponds to the probability of adoption and that this
relationship is identical across users.
More generally, we consider affine response functions of the form𝑓 𝑣(𝑥 𝑣)=𝑎 𝑣𝑥𝑣+𝑏 𝑣, where𝑎 𝑣≥0and
𝑏𝑣∈[0,1]are user-specific parameters. In this work, we focus on this class of activation functions and
develop a polynomial-time approximation algorithm with a constant-factor guarantee for this generalized
setting.
This formulation captures two key dimensions of user heterogeneity:
1. The parameter𝑏 𝑣 represents thebase activation probabilityof user𝑣, i.e., the likelihood that the user
adopts the product even in the absence of any incentive. This accounts for organic interest or pre-existing
affinity toward the product.
2. The parameter𝑎 𝑣 quantifies thesusceptibilityof user𝑣to incentives. A higher value of𝑎 𝑣 indicates
that the user’s activation probability increases rapidly with additional marketing effort, reflecting high price
sensitivity or promotional responsiveness. Conversely, a lower𝑎 𝑣 suggests that the user is less influenced
by incentives, perhaps due to brand loyalty or lack of interest.
By allowing both baseline adoption and marginal responsiveness to vary across users, the affine formula-
tion extends the identity model to capture richer and more realistic patterns of user behavior in networked
diffusion processes.
From a modeling perspective, the affine structure provides a simple yet expressive parametric family that
balances flexibility with analytical tractability. In particular, it enables the incorporation of heterogeneous
user behavior while avoiding more complex nonlinear response functions that may hinder optimization.
From an applied standpoint, the parameters𝑎 𝑣 and𝑏 𝑣 can be estimated from historical user engagement and
campaign data, for example, by analyzing how observed adoption probabilities vary with different levels of
incentives across users.
Prior work in marketing and social networks has emphasized the importance of heterogeneous influence
and adoption behavior (Aral et al. 2009, Iyengar et al. 2011), while continuous and discretized influence
maximization frameworks (Yang et al. 2016, Chen et al. 2020) allow for heterogeneous response functions
across users. Our formulation makes this heterogeneity explicit and interpretable, providing a natural bridge
between data-driven modeling and tractable network optimization.
Furthermore, in many practical settings, marketing interventions are subject to budget constraints and
heterogeneous costs across users. The cost of allocating incentives to a user may depend on factors such as
their reach, engagement level, or alignment with the product, making it unrealistic to assume uniform cost

Budget Generalized Fractional Influence Maximization
11
structures. To capture this, we associate each user𝑣∈𝑉with a cost parameter𝑤 𝑣>0, which represents the
cost per unit of incentive allocated to that user.
Given a total budget𝑘∈R ≥0, the allocation vectorxmust satisfy a budget constraint that accounts for
heterogeneous user costs. For vectorsx,w∈R 𝑛, we denote the inner product by
⟨w,x⟩=
∑︁
𝑣∈𝑉
𝑤𝑣𝑥𝑣,
so that the budget constraint can be written compactly as
⟨w,x⟩≤𝑘.
Let𝑘∈R ≥0 denote the total available budget. The objective is to select an allocation vectorx=
(𝑥1,...,𝑥 𝑛)∈[0,1] 𝑛 that maximizes the expected spread of influence, subject to a budget constraint.
The decision maker seeks to allocate incentives across users to maximize the expected spread of influence
subject to the budget constraint. This leads to the following optimization problem, which we refer to as the
Budgeted Generalized Fractional Influence Maximization (BGFIM) problem:
Problem 2 (Budgeted Generalized Fractional Influence Maximization (BGFIM)).
arg max
x∈[0,1] 𝑛
˜𝜎(x),
s.t.⟨w,x⟩≤𝑘.
This formulation generalizes several models studied in the literature. In the case where the cost parameters
are uniform, i.e.,𝑤 𝑣 =1for all𝑣∈𝑉, the problem reduces to a generalized fractional influence maximization
(GFIM) framework with heterogeneous activation functions (Bhimaraju et al. 2024). Furthermore, when the
activation functions take the identity form𝑓 𝑣(𝑥 𝑣)=𝑥 𝑣, and the cost parameters are uniform, the formulation
recovers the fractional influence maximization (FIM) problem (Umrawal et al. 2023a, 2026a).
By allowing both heterogeneous cost parameters and affine activation functions, the proposed BGFIM
formulation strictly generalizes these prior models and provides a more expressive framework for modeling
incentive-driven diffusion in social networks.
4. Efficient Approximation Algorithm with Provable Guarantees
We now turn to the problem of solving the Budgeted Generalized Fractional Influence Maximization
(BGFIM) problem defined in Problem 2. In the classical discrete influence maximization setting, the
objective function is monotone and submodular, enabling the use of efficient greedy algorithms with
strong approximation guarantees (Kempe et al. 2003, Nemhauser et al. 1978). More generally, submodular
maximization under cardinality and knapsack constraints has been extensively studied, with both discrete

Budget Generalized Fractional Influence Maximization
12
and continuous variants admitting(1−1/𝑒)-approximation algorithms (Vondr ´ak 2008, Calinescu et al.
2011).
However, extending these techniques to the BGFIM setting presents significant challenges. In particular,
the objective function˜𝜎(x)is defined over a continuous domain and depends on user-specific activation
functions and heterogeneous cost parameters. Unlike the identity case, where the objective reduces to the
multilinear extension of a submodular function, the presence of affine activation functions alters this structure
and complicates the direct application of existing optimization methods. As a result, designing scalable
algorithms with provable guarantees for Problem 2 requires new techniques that can effectively handle both
continuous decision variables and heterogeneous user behavior.
Our approach builds on the observation that, despite the loss of a standard multilinear structure, the
objective function˜𝜎(x)still retains a form of smooth marginal behavior that can be exploited algorithmically.
In particular, the impact of allocating a small amount of incentive to a user can be characterized through
the local sensitivity of their activation function. For affine functions of the form𝑓 𝑣(𝑥 𝑣)=𝑎 𝑣𝑥𝑣+𝑏 𝑣, this
sensitivity is captured by the parameter𝑎 𝑣, which determines how rapidly the user’s activation probability
increases with additional incentives.
This insight enables a natural extension of the classical greedy paradigm for submodular maximization.
Rather than selecting nodes solely based on their marginal contribution to influence, we instead consider a
cost-normalized marginal gain that incorporates both the responsiveness of the user and the cost of targeting
them. Specifically, we prioritize nodes according to a marginal gain-per-cost criterion scaled by the factor
𝑎𝑣/𝑤 𝑣, thereby favoring users who provide the largest increase in expected influence per unit of budget.
This formulation preserves the intuitive structure of greedy optimization while explicitly accounting for
heterogeneity in both behavioral response and cost, and forms the basis of our algorithmic design.
Building on this intuition, our method proceeds by iteratively allocating budget to nodes in a greedy
fashion, guided by a suitably defined marginal gain-per-cost criterion. At a high level, the algorithm incre-
mentally constructs a solution by selecting nodes that offer the greatest increase in expected influence relative
to their cost, adjusted for their responsiveness to incentives.
To formalize and justify this approach, it is important to understand how the continuous influence function
˜𝜎(x)behaves as a function of the allocation vectorx. In particular, we require a representation that captures
how marginal improvements in incentives translate into expected influence gains under heterogeneous
activation functions. The following subsection develops key structural properties of˜𝜎(x)that underpin our
algorithmic design and analysis.
To motivate and analyze our algorithmic approach, we first examine key structural properties of the
influence function˜𝜎(x).
Recall that under the randomized seeding mechanism, the initial active set𝑆0 is a random subset of nodes
where each node𝑣is included independently with probability𝑓 𝑣(𝑥 𝑣). Conditioning on𝑆 0, the subsequent

Budget Generalized Fractional Influence Maximization
13
diffusion follows the IC model, and the total expected influence is given by the discrete influence function
𝜎(𝑆 0).
Using this perspective, the continuous influence function can be expressed as
˜𝜎(x)=E 𝑆0[𝜎(𝑆 0)|x ] =
∑︁
𝑆0⊆𝑉
𝜎(𝑆 0)
Ö
𝑣∈𝑆 0
𝑓𝑣(𝑥 𝑣)
Ö
𝑣∉𝑆0
(1−𝑓 𝑣(𝑥 𝑣)).(1)
This representation makes explicit the connection between the continuous formulation and a distribution
over discrete seed sets, and will be central to the analysis that follows.
Under the identity activation functions𝑓 𝑣(𝑥 𝑣)=𝑥 𝑣, the expression in (1) reduces to
˜𝜎(x)=
∑︁
𝑆⊆𝑉
𝜎(𝑆)
Ö
𝑣∈𝑆
𝑥𝑣
Ö
𝑣∉𝑆
(1−𝑥 𝑣),
which coincides with the standard multilinear extension of𝜎(·).
This establishes a direct connection between the continuous formulation and classical approaches to
submodular maximization.
We now consider affine activation functions of the form𝑓 𝑣(𝑥 𝑣)=𝑎 𝑣𝑥𝑣+𝑏 𝑣. Substituting into (1), we
observe that˜𝜎(x)can still be expressed as a weighted sum over subsets𝑆⊆𝑉, with weights determined
by the parameters{𝑎 𝑣,𝑏 𝑣}𝑣∈𝑉 and the allocation vectorx. While the resulting function is no longer the
standard multilinear extension of𝜎(·), it retains a related polynomial structure that preserves key features
of marginal influence contributions.
This perspective highlights that, although the affine formulation departs from classical multilinear settings,
it preserves sufficient structure—particularly in terms of marginal gain behavior—to enable the design of
efficient greedy algorithms. These observations provide the foundation for our algorithmic approach in the
BGFIM setting.
Leveraging these structural insights, we now develop a discrete-greedy algorithm for solving the BGFIM
problem. The algorithm iteratively allocates incentives to users by selecting those that provide the greatest
marginal increase in expected influence per unit cost, adjusted for their responsiveness to incentives. This
approach extends classical greedy methods for submodular maximization to the present setting, while
explicitly accounting for heterogeneity in both activation behavior and targeting costs. We formalize this
approach in Algorithm 1.

Budget Generalized Fractional Influence Maximization
14
Algorithm 1Generalized Discrete-Greedy Algorithm for Problem 2
Input:Users𝑉, influence function𝜎: 2 𝑉→R≥0, budget𝑘
Output:Allocation vector𝑦∈R |𝑉| ≥0 , where𝑦 𝑣 denotes incentive assigned to user𝑣
1:Initialize𝑦 𝑣←0for all𝑣∈𝑉 ⊲No initial incentives to any user
2:𝑆 0←∅⊲Empty initial set of targeted users
3:while ˝ 𝑣∈𝑉 𝑤𝑣𝑦𝑣<𝑘and𝑆 0 ≠𝑉do⊲Continue until budget is exhausted or all users are targeted
4:𝑣 next←arg max 𝑣∉𝑆0(𝜎(𝑆 0∪{𝑣})−𝜎(𝑆 0))· 𝑓′ 𝑣(0) 𝑤𝑣 ⊲Select a user that maximizes influence gain per
unit cost
5:𝑦 𝑣next←min

𝑓−1 𝑣next(1), 𝑘−˝ 𝑣∈𝑉 𝑤𝑣 𝑦𝑣 𝑤𝑣next  ⊲Allocate maximum feasible incentive within budget
6:𝑆 0←𝑆 0∪{𝑣 next}⊲Add user to targeted set
7:end while
Algorithm Description.Algorithm 1 formalizes the discrete-greedy strategy for solving Problem 2. The
method incrementally allocates incentives across users in the social network by selecting, at each step, the
user that delivers the highest increase in expected influence per unit of budget. Crucially, this marginal
contribution is weighted by the user’s responsiveness to incentives, captured by the local sensitivity of
the activation function. This design allows the algorithm to simultaneously account for network effects,
heterogeneous adoption behavior, and variation in targeting costs within a unified allocation framework.
Initialization (Lines 1–2).The algorithm begins with no incentives allocated, i.e.,𝑦 𝑣 =0for all users
𝑣∈𝑉, and an empty set𝑆 0 representing the users initially targeted in the campaign. At this stage, no adoption
has been triggered, and the subsequent allocation decisions are driven entirely by the marginal influence
gains generated through the network.
Greedy Selection Loop (Lines 3–6).At each iteration, the algorithm evaluates the marginal impact
of allocating incentives to users who have not yet been targeted. Specifically, it selects the user𝑣 next that
maximizes
(𝜎(𝑆 0∪{𝑣})−𝜎(𝑆 0)) 𝑓′ 𝑣(0) 𝑤𝑣 ,
which captures the expected increase in overall adoption per unit of budget. This selection rule balances
three key considerations: the incremental influence a user can generate through the network, the user’s
responsiveness to incentives, and the cost required to engage that user. By prioritizing users with the highest
influence-per-cost ratio, the algorithm effectively allocates resources toward individuals who can trigger the
most impactful diffusion cascades in the social network.
Set Update (Line 6).The selected user is added to the targeted set𝑆0, and the allocation process continues.
This update reflects the sequential expansion of the campaign, where each newly incentivized user contributes
to the growing pool of adopters who can influence others through the social network.

Budget Generalized Fractional Influence Maximization
15
Termination.The algorithm terminates when the available campaign budget𝑘is fully utilized or when all
users have been considered for targeting. The resulting allocation vector𝑦specifies the incentives assigned
across users, effectively defining the final campaign strategy. This allocation balances influence potential,
user responsiveness, and cost constraints, yielding a targeted deployment of incentives designed to maximize
overall adoption through the social network.
The design of Algorithm 1 closely parallels classical greedy approaches for submodular maximization
under budget constraints, while incorporating key adjustments to account for heterogeneous user respon-
siveness and incentive costs. By prioritizing users based on their cost-adjusted marginal contribution to
expected adoption, the algorithm effectively allocates the campaign budget toward individuals with the
greatest potential to drive network-wide diffusion.
Despite the additional complexity introduced by heterogeneous activation functions, we show that this
greedy allocation strategy retains strong performance guarantees. In particular, we establish that the proposed
algorithm achieves a(1−1/𝑒)-approximation to the optimal solution of Problem 2.
Theorem 1(Constant-Factor Approximation Guarantee).Suppose that the user activation functions
are affine, i.e.,𝑓 𝑣(𝑦 𝑣)=𝑎 𝑣𝑦𝑣+𝑏 𝑣 with𝑎 𝑣,𝑏 𝑣≥0for all users𝑣∈𝑉. Then the incentive allocation vector𝑦
returned by Algorithm 1 satisfies
𝐹(𝑦)≥

1− 1 𝑒  𝐹(𝑦∗),
where𝑦∗ is an optimal solution to Problem 2.
Proof Sketch.The proof adapts the classical analysis of greedy algorithms for submodular maximization
under budget constraints to the present setting with heterogeneous user behavior. The central idea is to
interpret the progression of the campaign as a function of the allocated budget𝑘, and to relate the marginal
increase in expected influence achieved by the algorithm to the remaining gap between the current allocation
and the optimal solution.
At each step, the algorithm selects the user that maximizes the cost-adjusted marginal gain
(𝜎(𝑆 0∪{𝑣})−𝜎(𝑆 0)) 𝑎𝑣 𝑤𝑣 ,
which can be interpreted as the rate at which expected influence increases per unit of budget. Using the
structure of the influence function together with the chain rule, this quantity corresponds to the derivative
of the objective𝐹(𝑦)with respect to the budget𝑘. Intuitively, the algorithm prioritizes users who deliver
the largest marginal increase in adoption for each additional unit of incentive, ensuring that the allocation
progresses in the most effective direction at every stage.
To complete the analysis, we compare this rate of improvement with the best possible marginal gain
achievable by the optimal allocation𝑦 ∗. Using submodularity of the underlying influence function and the

Budget Generalized Fractional Influence Maximization
16
budget constraint, we obtain a bound showing that the rate at which𝐹(𝑦)increases under the algorithm is at
least a constant fraction of the remaining optimality gap𝐹(𝑦∗)−𝐹(𝑦). This leads to a differential inequality
of the form
𝑑
𝑑𝑘𝐹(𝑦)≥ 1 𝑘(𝐹(𝑦∗)−𝐹(𝑦) ),
which captures how the algorithm steadily closes the gap to optimality as the budget is allocated.
Solving this inequality over the interval[0,𝑘]yields
𝐹(𝑦)≥

1− 1 𝑒  𝐹(𝑦∗),
establishing the desired(1−1/𝑒)approximation guarantee. This matches the classical bound for submodular
maximization under knapsack constraints and demonstrates that the proposed algorithm retains strong
performance despite the presence of heterogeneous user responses and incentive costs.
Time Complexity.Each iteration of Algorithm 1 selects one user, and thus the procedure runs for at most|𝑉|
iterations, where𝑉denotes the set of users in the social network. In each iteration, the algorithm evaluates
the marginal influence gain for up to|𝑉|candidate users, each requiring a call to𝜎(·), which can be estimated
via Monte Carlo simulation in time𝑇. Therefore, the overall time complexity is𝑂(|𝑉| 2𝑇), matching the
complexity of standard greedy methods for influence maximization and enabling scalable implementation
for large-scale marketing campaigns.
5. Experiments
In this section, we pursue two complementary objectives. First, we evaluate the scalability and effectiveness
of the proposed greedy approximation algorithm on large real-world networks spanning multiple application
domains. Second, we demonstrate how the nested solutions generated by the algorithm can be leveraged to
support budget-selection decisions under varying cost-benefit tradeoffs. Together, these experiments assess
both the algorithmic performance of the proposed method and its value as a decision-support tool for
influence-based resource allocation.
5.1. Experimental Setup
We begin by describing the datasets and preprocessing steps used in our experiments.
5.1.1. Network DataWe evaluate our algorithm on five large-scale real-world networks sourced from
Leskovec and Krevl (2014), each representing a distinct domain of social or economic interaction. Table 1
summarizes their structural properties. These networks were selected because they represent five distinct
influence-allocation settings: governance and voting (Wikipedia), social interaction (Facebook), digital
content consumption (Deezer), knowledge diffusion (DBLP), and product adoption (Amazon). Together, they
allow us to evaluate whether the proposed algorithm generalizes across fundamentally different behavioral
and economic environments.

Budget Generalized Fractional Influence Maximization
17
Network Name Type Node Count Edge Count
Wikipedia (Leskovec et al. 2010b,a) Directed 7,115 201,524
Facebook (Leskovec and Mcauley 2012) Undirected 4,039 176,468
Deezer (Rozemberczki and Sarkar 2020) Undirected 28,281 185,504
DBLP (Yang and Leskovec 2012) Undirected 317,080 2,099,732
Amazon (Yang and Leskovec 2012) Undirected 334,863 1,851,744
Table 1 Basic information about each network. The data was retrieved from Leskovec and Krevl (2014).
1.Wikipedia (Directed):A voting network where each edge represents a vote cast by one user for
another in Wikipedia’s administrator elections. This graph models directional influence and is relevant for
studying trust, reputation systems, and decision-making dynamics in online communities.
2.Facebook (Undirected):A social network of user friendships. As a prototypical example of peer-to-
peer influence, this dataset is widely used in studies of viral marketing, information diffusion, and community
detection.
3.Deezer (Undirected):A music streaming platform network where edges represent social connections
or shared listening behavior. This network is useful for evaluating influence-based recommendation systems
and incentive mechanisms in digital entertainment platforms.
4.DBLP (Undirected):A co-authorship network in computer science, where edges indicate joint pub-
lications. It serves as a model for academic collaboration and the diffusion of ideas, making it relevant for
incentive design in research communities.
5.Amazon (Undirected):A product co-purchase network, where edges connect items frequently bought
together. This network is highly applicable to e-commerce, especially for optimizing bundling strategies,
targeted promotions, and influence-aware discount allocation.
The diversity of these networks—in terms of size, structure, and domain—allows us to assess the scala-
bility and robustness of our algorithm across different real-world scenarios. Each network presents unique
challenges for influence maximization, such as varying degrees of sparsity, clustering, and centrality, which
we explore in subsequent sections.
To ensure consistency in influence modeling, we converted all undirected networks into directed graphs
by replacing each undirected edge with two directed edges. For edge weights, we adopted theweighted
cascade model(Kempe et al. 2003), where for each node𝑣∈𝑉, the weight of each incoming edge is set to
1/in-degree(𝑣). This normalization ensures that the total incoming influence to any node is bounded by 1,
aligning with standard assumptions in influence maximization literature.
We used thePoochlibrary (Uieda et al. 2020) for automated data retrieval and theNetworkXlibrary
(Hagberg et al. 2008) for graph preprocessing and manipulation.
5.1.2. Experimental DetailsA central feature of our framework is that different individuals may
respond differently to incentives. In practice, customers, users, and agents rarely exhibit identical responsive-
ness or activation costs. Accordingly, our experimental design incorporates heterogeneous activation and

Budget Generalized Fractional Influence Maximization
18
cost parameters. To simulate realistic incentive allocation scenarios, we randomly assigned each node𝑣∈𝑉a
linear activation function𝑓 𝑣(𝑦 𝑣)=𝑎 𝑣𝑦𝑣+𝑏 𝑣, where the coefficients𝑎 𝑣,𝑏 𝑣, and cost weights𝑤 𝑣 were drawn
uniformly at random from the sets𝐴={0.5,1},𝐵={0,0.2}, and𝑊={0.5,1}, respectively. These choices
reflect heterogeneous agent responsiveness and cost structures, which are common in managerial settings
such as marketing campaigns, subsidy allocation, or targeted interventions. For example, some individuals
may require higher incentives to reach full activation (low𝑎 𝑣), while others may be more responsive even
with minimal investment (high𝑎 𝑣, low𝑏 𝑣).
We set the total budget to𝐾=10.0, representing a constrained resource environment typical in managerial
decision-making. This budget level allows us to evaluate how effectively the algorithm prioritizes high-impact
nodes under limited resources.
To estimate the expected influence spread resulting from each discount vector𝑦, we performed 10,000
Monte Carlo simulations per experiment. These simulations model stochastic diffusion processes, capturing
the uncertainty inherent in real-world influence propagation.
All experiments were conducted on a workstation equipped with a 3.00 GHz 8-core Intel Xeon E5-1660v3
CPU and 64 GB of RAM. The implementation was written in Python, using theCyNetDifflibrary (Robson
et al. 2024) for efficient simulation of influence diffusion. To improve runtime performance, we incorporated
a priority queue optimization inspired by the Cost-Effective Lazy Forward (CELF) algorithm (Leskovec
et al. 2007), which reduces redundant evaluations when selecting the node with the highest marginal gain in
step 4 of Algorithm 1.
5.2. Greedy Approximation
We implement Algorithm 1 in Python across all networks described in Section 5.1.1. As a baseline for
comparison, we use a generalized version of the degree discount heuristic from Chen et al. (2009), where the
degree discount score𝑑𝑑 𝑣 is divided by the activation cost𝑦 𝑣𝑤𝑣. This baseline is chosen for its simplicity
and speed, and because degree-based heuristics are widely used in practice due to their intuitive appeal:
high-degree nodes often represent popular or central individuals, making them natural targets for influence
campaigns.
Figure 1 shows the influence spread (estimated via 10,000 Monte Carlo simulations) on the𝑦-axis as a
function of budget usage on the𝑥-axis. The budget values correspond to the cumulative cost of the selected
nodes at each iteration of the algorithm, up to the maximum budget of𝐾=10.0. Similarly, Figure 2 presents
the runtime (on the𝑦-axis) performance of the algorithm as a function of budget (on the𝑥-axis).
These results generate several managerial insights:
•Strategic Resource Allocation:The greedy algorithm provides a principled way to allocate limited
incentives across a population to maximize influence. This is directly applicable to domains such as marketing
(e.g., targeting influential customers), public health (e.g., vaccine outreach), and platform growth (e.g.,
onboarding key users in a network).

Budget Generalized Fractional Influence Maximization
19
0 2 4 6 8 10
0
500
1,000
1,500
2,000
Budget
Influence
Generalized Degree Discount
Generalized Discrete Greedy
(a) Amazon network
0 2 4 6 8 10
0
500
1,000
1,500
2,000
Budget
Influence
Generalized Degree Discount
Generalized Discrete Greedy
(b) DBLP network
0 2 4 6 8 10
0
200
400
600
800
1,000
1,200
Budget
Influence
Generalized Degree Discount
Generalized Discrete Greedy
(c) Deezer network
0 2 4 6 8 10
0
200
400
600
800
1,000
Budget
Influence
Generalized Degree Discount
Generalized Discrete Greedy
(d) Facebook network
0 2 4 6 8 10
0
500
1,000
1,500
Budget
Influence
Generalized Degree Discount
Generalized Discrete Greedy
(e) Wikipedia network
Figure 1 Influence vs. Budget (𝐾) for different networks.

Budget Generalized Fractional Influence Maximization
20
0 2 4 6 8 10
0
50
100
150
200
250
Budget
Runtime
Generalized Degree Discount
Generalized Discrete Greedy
(a) Amazon network
0 2 4 6 8 10
0
100
200
300
Budget
Runtime
Generalized Degree Discount
Generalized Discrete Greedy
(b) DBLP network
0 2 4 6 8 10
−10
0
10
20
30
40
Budget
Runtime
Generalized Degree Discount
Generalized Discrete Greedy
(c) Deezer network
0 2 4 6 8 10
0
50
100
150
Budget
Runtime
Generalized Degree Discount
Generalized Discrete Greedy
(d) Facebook network
0 2 4 6 8 10
0
100
200
300
Budget
Runtime
Generalized Degree Discount
Generalized Discrete Greedy
(e) Wikipedia network
Figure 2 Runtime (in seconds) vs. Budget (𝐾) for different networks.

Budget Generalized Fractional Influence Maximization
21
•Scalability and Efficiency:The use of CELF-style optimizations (Leskovec et al. 2007) ensures that
the algorithm remains computationally tractable even on large-scale networks. This is crucial for managers
who need to make timely decisions under resource constraints.
•Performance vs. Heuristics:Compared to the generalized degree discount heuristic, our algorithm
consistently achieves higher influence, especially at larger budget levels. This demonstrates the value of using
theoretically grounded methods over simple heuristics, particularly when the stakes of resource allocation
are high.
•Transparency and Interpretability:The greedy algorithm’s step-by-step selection process offers
transparency in decision-making, allowing managers to justify why certain individuals or nodes were
prioritized for incentives.
Overall, our framework bridges the gap between algorithmic rigor and managerial applicability, offering
a scalable and interpretable solution for influence maximization under budget constraints.
5.3. Profit-Optimized Budget Selection
The experiments thus far have focused on influence maximization under a fixed budget. In practice, however,
managers often face the inverse problem: determining how much budget should be allocated in the first
place. This requires balancing the additional influence generated by larger budgets against the corresponding
increase in incentive costs. Because our greedy algorithm produces a nested sequence of solutions, the
resulting influence estimates can be reused across many candidate budget levels, enabling efficient profit-
based decision-making.
In real-world marketing campaigns, the goal is not merely to maximize influence but to do so in a way
that maximizes profit. Each unit of budget spent on incentives incurs a cost, while each successful activation
generates revenue. The challenge for marketers is to determine the optimal budget allocation that balances
these two forces—maximizing reach without overspending.
Let𝑝≥0denote the price per unit of the product being promoted, and𝑐≥0the cost of sponsoring one
unit. Then, the profit𝜋(𝑡)from sponsoring𝑡units is given by:
total profit=total revenue−total cost of sponsorship,
=price per unit×influence−cost per unit×budget,
𝜋(𝑡)=𝑝˜𝜎(x(𝑡))−𝑐𝑡(2)
Here,˜𝜎(x(𝑡))represents the expected influence achieved by incentivizing𝑡users, selected using our
greedy algorithm.
To identify the budget𝑡that maximizes profit𝜋(𝑡), we useternary search. Ternary search is a standard
optimization procedure for unimodal functions, i.e., functions that increase up to a single maximum and then
decrease. At each iteration, the method evaluates two interior points within the current budget interval and

Budget Generalized Fractional Influence Maximization
22
eliminates the region that cannot contain the optimum. By repeatedly shrinking the search interval, ternary
search efficiently identifies the profit-maximizing budget.
Importantly, our greedy algorithm records the order in which nodes are selected, allowing influence
to be evaluated incrementally and avoiding recomputation. Once the influence dictionary has been con-
structed, managers can rapidly evaluate alternative pricing and cost scenarios without rerunning the under-
lying influence-maximization algorithm. This effectively separates the computationally intensive influence-
maximization step from the subsequent budget-selection problem, making profit optimization computation-
ally inexpensive.
Graph Budget Payoff Search Time Initial Computation Time
Wikipedia 2.82 275.54 63.21 212.30
Facebook 1.58 45.57 25.94 61.99
Deezer 0.59 29.90 9.12 39.34
DBLP 7.65 250.41 75.13 265.84
Amazon 7.14 295.35 60.50 219.26
Table 2 Results of optimal budget selection across networks. Experiments used a maximum budget of𝐾=8.00,
price per unit𝑝=0.5, cost per unit𝑐=80.0, and𝜖=0.1.
Table 2 presents the results of our profit-optimized budget selection experiments across five real-world
networks: Wikipedia, Facebook, Deezer, DBLP, and Amazon. For each graph, we report four key metrics:
1. Optimal Budget: The budget value that maximizes profit under the given pricing and cost parameters.
2. Payoff: The resulting profit achieved at the optimal budget.
3. Search Time: The time taken to perform a ternary search over the budget space to identify the profit-
maximizing point.
4. Initial Computation Time: The time required to compute the influence dictionary up to the maximum
budget𝐾=8.00.
These experiments were conducted using a fixed price per unit of𝑝=0.5, a cost per unit of𝑐=80.0, and
a fractional evaluation precision of𝜖=0.1. The results reveal several important trends:
•Efficiency of Optimization:Across all networks, the ternary search procedure is significantly faster
than the initial influence computation. For example, in the Wikipedia network, the search time (63.21
seconds) is less than one-third of the initial computation time (212.30 seconds). This demonstrates that once
the influence landscape is computed, profit optimization becomes highly efficient and scalable.
•Network-Specific Budgets:The optimal budget varies significantly across networks, reflecting differ-
ences in network structure and user responsiveness. For instance, Deezer achieves its maximum profit with
a budget of just 0.59, while DBLP requires a much larger budget of 7.65. This highlights the importance of
tailoring budget strategies to the underlying network characteristics.

Budget Generalized Fractional Influence Maximization
23
•Profit Sensitivity:The payoff values also vary widely, with Amazon yielding the highest profit (295.35)
and Deezer the lowest (29.90). These differences underscore the impact of network topology and influence
dynamics on campaign profitability.
•Managerial Implication:From a business perspective, these results validate the practicality of our
framework. Marketing managers can precompute influence dictionaries for their target networks and then
rapidly evaluate optimal budget levels under different pricing and cost scenarios. This enables data-driven
decision-making and supports agile campaign planning in dynamic environments.
Overall, this case study demonstrates that our framework not only provides theoretical guarantees and
algorithmic efficiency but also delivers actionable insights for real-world marketing applications, offering a
clear and actionable pathway from data to profit.
6. Conclusion
We conclude the paper by summarizing our contributions, discussing the framework’s industry readiness,
outlining its limitations, and identifying promising directions for future research.
6.1. Summary
In this work, we addressed the problem of influence maximization using partial incentives under a general-
ized marketing model. We formally defined the Budgeted Generalized Fractional Influence Maximization
(BGFIM) problem, which extends prior work by incorporating two key real-world factors: (i) a flexible affine
relationship between the offered discount and a user’s probability of activation, and (ii) a generalized budget
constraint that accounts for heterogeneous costs in incentivizing different users.
To solve this more realistic and complex problem, we proposed an efficient greedy algorithm with a prov-
able approximation guarantee of(1−1/𝑒) relative to the optimal solution. Through extensive experiments on
five large-scale real-world networks, we demonstrated the algorithm’s scalability and superior performance
compared to common heuristics. Additionally, we showcased its utility in a profit-maximization setting,
highlighting its relevance for strategic marketing decisions.
6.2. Industry Readiness
Our framework is well-positioned for real-world deployment in marketing and advertising platforms. The
ability to model heterogeneous user costs and partial incentives aligns with how modern platforms oper-
ate—offering personalized discounts, targeting high-value users, and optimizing campaign budgets. The
profit-optimized budget selection method enables marketers to make data-driven decisions that balance
cost and reach, maximizing return on investment (ROI). Moreover, the reuse of influence computations
across different pricing scenarios makes the approach scalable and cost-effective for dynamic business
environments.

Budget Generalized Fractional Influence Maximization
24
6.3. Limitations
While our model generalizes prior work, it still assumes a linear relationship between discount and activation
probability. In practice, user behavior may follow more complex patterns—such as diminishing returns
or sigmoid responses—where small discounts have little effect until a threshold is reached, after which
influence grows rapidly and then plateaus. Our current framework does not capture such non-linear dynamics.
Additionally, the cost of incentivizing users is treated as static, whereas in real-world settings, costs may
evolve over time due to factors like user popularity
6.4. Future Steps
Building on this foundation, several promising directions emerge. First, we aim to extend the model to support
non-linear activation functions, such as convex or sigmoid relationships, which better reflect real-world
consumer behavior. Second, we plan to explore dynamic cost models where the cost of incentivizing a user
may change over time, enabling more adaptive campaign strategies. Finally, we are interested in developing
online algorithms for influence maximization in uncertain environments, where activation probabilities are
not known in advance and must be learned over time through exploration and feedback (Agarwal et al.
2022, Nie et al. 2022, Xu and Umrawal 2026). These extensions will further enhance the applicability of
our framework to real-time, data-driven marketing systems.
Acknowledgments
A preliminary version of this paper appeared at the 33rd ACM International Conference on Information
and Knowledge Management (CIKM), 2024 (Bhimaraju et al. 2024). The present manuscript substantially
extends and revises that earlier version.
References
Agarwal M, Aggarwal V, Umrawal AK, Quinn CJ (2022) Stochastic top k-subset bandits with linear space and non-
linear feedback with applications to social influence maximization.ACM/IMS Transactions on Data Science
(TDS)2(4):1–39.
Aral S (2020)The Hype Machine: How Social Media Disrupts Our Elections, Our Economy, and Our Health—and
How We Must Adapt(New York: Currency), ISBN 978-0525574514.
Aral S, Dellarocas C, Godes D (2013) Social media and business transformation: A framework for research.Information
Systems Research24(1):3–13, URLhttp://dx.doi.org/10.1287/isre.1120.0470.
Aral S, Muchnik L, Sundararajan A (2009) Distinguishing influence-based contagion from homophily-driven diffusion
in dynamic networks.Proceedings of the National Academy of Sciences106(51):21544–21549, URLhttp:
//dx.doi.org/10.1073/pnas.0908800106.
Aral S, Walker D (2012) Identifying influential and susceptible members of social networks.Science337(6092):337–
341, URLhttp://dx.doi.org/10.1126/science.1215842.

Budget Generalized Fractional Influence Maximization
25
Bass FM (1969) A new product growth model for consumer durables.Management Science15(5):215–227.
Bhimaraju A, Robson EW, Varshney LR, Umrawal AK (2024) Fractional budget allocation for influence maximization
under general marketing strategies.Proceedings of the 33rd ACM International Conference on Information and
Knowledge Management (CIKM), 3627–3631.
Borgs C, Brautbar M, Chayes J, Lucier B (2014) Maximizing social influence in nearly optimal time.Proceedings of
the Twenty-Fifth Annual ACM-SIAM Symposium on Discrete Algorithms (SODA), 946–957 (SIAM).
Calinescu G, Chekuri C, Pal M, Vondr´ak J (2011) Maximizing a monotone submodular function subject to a matroid
constraint.SIAM Journal on Computing40(6):1740–1766.
Chen W, Wang Y, Yang S (2009) Efficient influence maximization in social networks.Proceedings of the 15th ACM
SIGKDD International Conference on Knowledge Discovery and Data Mining, 199–208.
Chen W, Wu R, Yu Z (2020) Scalable lattice influence maximization.IEEE Transactions on Computational Social
Systems7(4):956–970.
Domingos P, Richardson M (2001) Mining the network value of customers.Proceedings of the Seventh ACM SIGKDD
International Conference on Knowledge Discovery and Data Mining, 57–66 (ACM).
Goldenberg J, Libai B, Muller E (2001a) Talk of the network: A complex systems look at the underlying process of
word-of-mouth.Marketing Letters12(3):211–223.
Goldenberg J, Libai B, Muller E (2001b) Using complex systems analysis to advance marketing theory develop-
ment: Modeling heterogeneity effects on new product growth through stochastic cellular automata.Academy of
Marketing Science Review9(3):1–18.
Gomez-Rodriguez M, Leskovec J, Krause A (2010) Inferring networks of diffusion and influence.Proceedings of the
16th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD), 1019–1028
(ACM), URLhttp://dx.doi.org/10.1145/1835804.1835933.
Goyal A, Bonchi F, Lakshmanan LV (2011a) A data-based approach to social influence maximization.Proceedings of
the VLDB Endowment5(1):73–84.
Goyal A, Bonchi F, Lakshmanan LVS (2010) Learning influence probabilities in social networks.Proceedings of
the 3rd ACM International Conference on Web Search and Data Mining (WSDM), 241–250 (ACM), URL
http://dx.doi.org/10.1145/1718487.1718518.
Goyal A, Lu W, Lakshmanan LV (2011b) CELF++: Optimizing the greedy algorithm for influence maximization in
social networks.Proceedings of the 20th International Conference on World Wide Web (WWW), 47–48.
Granovetter M (1978) Threshold models of collective behavior.American Journal of Sociology83(6):1420–1443.
Gupta S, Steenburgh TJ (2008) Allocating marketing resources. Technical Report 08-069, Har-
vard Business School, URLhttps://www.hbs.edu/ris/Publication%20Files/08-069_
17a7715d-c34b-4d9e-92fa-2ea2834a0cbe.pdf.

Budget Generalized Fractional Influence Maximization
26
Hagberg AA, Schult DA, Swart PJ (2008) Exploring network structure, dynamics, and function using networkx.
Varoquaux G, Vaught T, Millman J, eds.,Proceedings of the 7th Python in Science Conference (SciPy), 11–15
(Pasadena, CA, USA).
Holt D (2016) Branding in the age of social media.Harvard Business ReviewURLhttps://hbr.org/2016/03/
branding-in-the-age-of-social-media.
Iyengar R, Van den Bulte C, Valente TW (2011) Opinion leadership and social contagion in new product diffusion.
Marketing Science30(2):195–212, URLhttp://dx.doi.org/10.1287/mksc.1100.0566.
Kanuri VK, Chen Y, Sridhar S (2018) Scheduling content on social media: Theory, evidence, and application.Journal
of Marketing82(6):89–108.
Kempe D, Kleinberg J, Tardos ´E (2003) Maximizing the spread of influence through a social network.Proceedings
of the Ninth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 137–146
(Association for Computing Machinery), URLhttp://dx.doi.org/10.1145/956750.956769.
Lang N, Wang L, Zha Q (2022) Targeted allocation of marketing resource in networks based on opinion dynamics.
Mathematics10(3):394, URLhttp://dx.doi.org/10.3390/math10030394.
Leskovec J, Huttenlocher D, Kleinberg J (2010a) Predicting positive and negative links in online social networks.
Proceedings of the 19th International Conference on World Wide Web (WWW), 641–650.
Leskovec J, Huttenlocher D, Kleinberg J (2010b) Signed networks in social media.Proceedings of the SIGCHI
Conference on Human Factors in Computing Systems (CHI), 1361–1370.
Leskovec J, Krause A, Guestrin C, Faloutsos C, VanBriesen J, Glance N (2007) Cost-effective outbreak detec-
tion in networks.Proceedings of the 13th ACM SIGKDD International Conference on Knowledge Discovery
and Data Mining, 420–429, KDD ’07 (New York, NY, USA: Association for Computing Machinery), ISBN
9781595936097, URLhttp://dx.doi.org/10.1145/1281192.1281239.
Leskovec J, Krevl A (2014) SNAP Datasets: Stanford large network dataset collection.http://snap.stanford.
edu/data.
Leskovec J, Mcauley JJ (2012) Learning to discover social circles in ego networks.Advances in Neural Information
Processing Systems, 539–547.
Libai B, Muller E, Peres R (2013) Customer lifetime social value (clsv).Journal of Marketing77(6):139–153, URL
http://dx.doi.org/10.1509/jm.12.0460.
Lobel I, Sadler E, Varshney LR (2017) Customer referral incentives and social media.Management Science
63(10):3514–3529, URLhttp://dx.doi.org/10.1287/mnsc.2016.2504.
Mallipeddi RR, Kumar S, Sriskandarajah C, Zhu Y (2022) A framework for analyzing influencer marketing in social
networks: selection and scheduling of influencers.Management Science68(1):75–104.
Naceva N (2026) 10 influencer marketing campaign examples in 2026. URLhttps://influencermarketinghub.
com/influencer-marketing-examples/.

Budget Generalized Fractional Influence Maximization
27
Nain P (2023) How graza reached $100k+ in week 1 with influencer marketing. URLhttps://www.getsaral.com/
academy/graza-influencer-marketing.
Nemhauser GL, Wolsey LA, Fisher ML (1978) An analysis of approximations for maximizing submodular set func-
tions—i.Mathematical Programming14(1):265–294.
Nie G, Agarwal M, Umrawal AK, Aggarwal V, Quinn CJ (2022) An explore-then-commit algorithm for submodular
maximization under full-bandit feedback.Uncertainty in Artificial Intelligence, 1541–1551 (PMLR).
Pan M, Blut M, Ghiassaleh A, Lee ZWY (2025) Influencer marketing effectiveness: A meta-analytic review.Journal of
the Academy of Marketing Science53:52–78, URLhttp://dx.doi.org/10.1007/s11747-024-01052-7.
Rehman Su, Gulzar R, Aslam W (2022) Developing the integrated marketing communication (imc) through social
media (sm): The modern marketing communication approach.SAGE Open12(2):1–23, URLhttp://dx.doi.
org/10.1177/21582440221099936.
Robson EW, Reddy D, Umrawal AK (2024) Cynetdiff: A python library for accelerated implementation of network
diffusion models.Proceedings of the VLDB Endowment17(12):4409–4412.
Robson EW, Umrawal AK (2025) A community-aware framework for influence maximization with explicit accounting
for inter-community influence.arXiv preprint arXiv:2512.23973.
Rozemberczki B, Sarkar R (2020) Characteristic functions on graphs: Birds of a feather, from statistical descriptors
to parametric models.Proceedings of the 29th ACM International Conference on Information and Knowledge
Management (CIKM), 1325–1334 (ACM).
Ryu G, Feick L (2007) A penny for your thoughts: Referral reward programs and referral likelihood.Marketing Science
26(2):171–187, URLhttp://dx.doi.org/10.1287/mksc.1060.0248.
Schelling TC (2006)Micromotives and Macrobehavior(W. W. Norton & Company).
Schmitt P, Skiera B, Van den Bulte C (2011) Referral programs and customer value.Journal of Marketing75(1):46–59,
URLhttp://dx.doi.org/10.1509/jm.75.1.46.
Stutsman C, Robson EW, Umrawal AK (2026) A pressure-based diffusion model for influence maximization on social
networks.Proceedings of the International AAAI Conference on Web and Social Media, volume 20, 2238–2251.
Tang Y, Shi Y, Xiao X (2015) Influence maximization in near-linear time: A martingale approach.Proceedings of the
2015 ACM SIGMOD International Conference on Management of Data, 1539–1554.
Uieda L, Soler SR, Rampin R, van Kemenade H, Turk M, Shapero D, Banihirwe A, Leeman J (2020) Pooch: A friend
to fetch your data files.Journal of Open Source Software5(45):1943, URLhttp://dx.doi.org/10.21105/
joss.01943.
Umrawal AK, Aggarwal V (2023) Leveraging the community structure of a social network for maximizing the spread
of influence.ACM SIGMETRICS Performance Evaluation Review50(4):17–19.
Umrawal AK, Aggarwal V, Quinn CJ (2023a) Fractional budget allocation for influence maximization.Proceedings
of the 62nd IEEE Conference on Decision and Control (CDC), 4327–4332, URLhttp://dx.doi.org/10.
1109/CDC49753.2023.10384250.

Budget Generalized Fractional Influence Maximization
28
Umrawal AK, Quinn CJ, Aggarwal V (2023b) A community-aware framework for social influence maximization.IEEE
Transactions on Emerging Topics in Computational Intelligence7(4):1253–1262.
Umrawal AK, Robson EW, Aggarwal V, Quinn CJ (2026a) Maximizing the spread of influence through a social network
using partial incentives.Journal of Artificial Intelligence Research86, URLhttp://dx.doi.org/10.1613/
jair.1.20410.
Umrawal AK, Stutsman C, Woods C, Robson EW (2026b) How social reinforcement shapes word-of-mouth: A
conviction-based model for marketing diffusion and network targeting.arXiv preprint arXiv:2610.13890.
Vondr´ak J (2008) Optimal approximation for the submodular welfare problem in the value oracle model.Proceedings
of the 40th Annual ACM Symposium on Theory of Computing, 67–74.
Vrontis D, Makrides A, Christofi M, Thrassou A (2021) Social media influencer marketing: A systematic review,
integrative framework and future research agenda.International Journal of Consumer Studies45(4):617–644,
URLhttp://dx.doi.org/10.1111/ijcs.12647.
Xu J, Umrawal AK (2026) Lofa: Online influence maximization under full-bandit feedback using lazy forward selection.
arXiv preprint arXiv:2601.00933.
Yang J, Leskovec J (2012) Defining and evaluating network communities based on ground-truth.Proceedings of the
ACM SIGKDD Workshop on Mining Data Semantics, MDS ’12 (New York, NY, USA: Association for Computing
Machinery), ISBN 9781450315463, URLhttp://dx.doi.org/10.1145/2350190.2350193.
Yang Y, Mao X, Pei J, He X (2016) Continuous influence maximization: What discounts should we offer to social
network users?Proceedings of the 2016 International Conference on Management of Data (SIGMOD), 727–741.
Yoganarasimhan H (2012) Impact of social network structure on content propagation: A study using youtube data.
Management Science58(6):1076–1094, URLhttp://dx.doi.org/10.1287/mnsc.1110.1464.
Zalani R (2025) 12 influencer marketing campaign examples [+ key takeaways]. URLhttps://www.modash.io/
blog/influencer-marketing-campaign-examples.
