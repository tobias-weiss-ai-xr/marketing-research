---
title: 'How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion
  and Network Targeting'
url: https://arxiv.org/abs/2610.13890
category: social-media
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Abhishek K. Umrawal
- Curt Stutsman
- Camille Woods
- Eliot W. Robson
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.13890
pages: 44
chars: 124223
fetched_at: '2026-11-08T13:13:34+00:00'
kb_version: 1
---

# How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting

How Social Reinforcement Shapes Word-of-Mouth: A
Conviction-Based Model for Marketing Diffusion and
Network Targeting
Abhishek K. Umrawal†
University of Illinois Urbana-Champaign, Urbana, Illinois 61801, USA aumrawal@illinois.edu
Curt Stutsman
University of Illinois Urbana-Champaign, Urbana, Illinois 61801, USA curtiss8@illinois.edu
Camille Woods
University of Illinois Urbana-Champaign, Urbana, Illinois 61801, USA crwoods2@illinois.edu
Eliot W. Robson
Narmi Inc., New York City, New York 10016, USA eliot.robson24@gmail.com
Organizations increasingly rely on social networks to drive product adoption and word-of-mouth diffusion, yet a central
challenge is that consumers differ not only in whether they adopt but also in how strongly they subsequently advocate.
In particular, individuals who adopt under strong social reinforcement often develop greater conviction and become
more persuasive. Existing diffusion models largely abstract away from this mechanism by treating influence strength
as static. We introduce a conviction-based diffusion framework, the Pressure Threshold (PT) model, that captures how
social reinforcement shapes both adoption and subsequent advocacy. In this model, an individual’s influence increases
with the cumulative social pressure experienced at adoption, providing a tractable representation of conviction formation
while preserving the interpretability of classical threshold-based models. We study the managerial implications of this
mechanism through marketing targeting and seeding. We show that accounting for reinforcement fundamentally alters
optimal targeting strategies, shifting emphasis toward consumers in cohesive network regions where repeated exposure can
amplify downstream word-of-mouth. While reinforcement introduces nonstandard features into the optimization problem,
we demonstrate that scalable heuristics remain effective and provide data-dependent performance guarantees. Across
synthetic and real-world networks, we find that reinforcement often substantially increases the effectiveness of seeding
interventions, particularly in dense and clustered environments where opportunities for social validation are abundant.
Using time-stamped social media cascades, we further show that the PT model improves predictive accuracy relative to
standard diffusion models, highlighting the empirical relevance of conviction-driven amplification.
Key words: word-of-mouth; social influence; conviction; peer pressure; social reinforcement; marketing diffusion;
targeting and seeding; network interventions; influence maximization
† Abhishek K. Umrawal is the corresponding author.
1
arXiv:2610.13890v1  [cs.SI]  9 Oct 2026

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
2
1. Introduction
Word-of-mouth and social influence play a central role in the diffusion of products, beliefs, and behaviors
(Bass 1969, Goldenberg et al. 2001, Rogers 2003, Aral and Walker 2012, Libai et al. 2013). Consumers are
not only influenced by their peers’ adoption decisions, but also by the intensity and consistency of social
reinforcement they experience prior to adopting. In many settings, individuals who adopt after repeated
exposure within their social network develop stronger conviction and, in turn, become more persuasive
advocates to others. Yet most existing approaches implicitly assume that all adopters exert similar levels of
influence, regardless of how their adoption was formed. This heterogeneity in post-adoption advocacy is
critical for firms and platforms that rely on network-based interventions, such as targeted seeding, influencer
marketing, and referral programs, to maximize downstream word-of-mouth and customer lifetime social
value (Lobel et al. 2017, Libai et al. 2013).
To study these processes, a large literature models social influence using threshold-based or contagion
frameworks, in which individuals adopt when the aggregate influence from their neighbors exceeds a
threshold (Granovetter 1978, Kempe et al. 2003). Building on these models, a central decision problem
is influence maximization (IM), which seeks to identify a set of initial adopters (or “seed” nodes) that
maximizes downstream diffusion (Domingos and Richardson 2001, Kempe et al. 2003). This framework has
been widely used to guide marketing interventions such as targeted seeding, information campaigns, and
referral programs.
The modern formalization of network-based diffusion expands on threshold and contagion models of
social influence, including the Linear Threshold (LT) and Independent Cascade (IC) frameworks introduced
by Kempe et al. (2003). These models extend earlier theories of collective behavior and social thresholds
(Granovetter 1978) and connect to marketing perspectives on word-of-mouth diffusion and network-driven
adoption (Goldenberg et al. 2001, Aral et al. 2013, Lobel et al. 2017). Their appeal lies in their conceptual
clarity and tractability, which have made them the dominant models for studying how peer influence
propagates through networks and for designing data-driven marketing interventions.
A growing body of empirical and theoretical work highlights the importance of social reinforcement in
shaping diffusion outcomes. In many settings, repeated exposure within cohesive or homophilic communi-
ties increases both the likelihood of adoption and the intensity of subsequent engagement, consistent with
the idea of complex contagion (Mønsted et al. 2017). In online environments, users tend to cluster into
like-minded groups, and information transmission is disproportionately concentrated within these commu-
nities, amplifying beliefs and behaviors through repeated validation (Cinelli et al. 2021). From a marketing
perspective, such reinforcement is closely related to mechanisms of social proof and conformity, whereby
individuals infer value or credibility from observing widespread adoption among peers. Further marketing
and consumer behavior research suggests that the strength and persistence of word-of-mouth are shaped by

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
3
social context, including peer validation, conformity pressures, and repeated exposure (Aral 2020, Pan et al.
2025).
These patterns imply that influence is not merely transmitted across network connections but can be
amplified through local reinforcement. In particular, individuals who adopt after observing consistent support
from their peers may develop stronger conviction and become more active or persuasive participants in
subsequent word-of-mouth processes. This amplification mechanism is central to many real-world diffusion
phenomena. Still, it is not explicitly represented in standard diffusion models which assume static influence
exerted by an individual, independent of how their own adoption was shaped. As a result, while LT and
IC models capture whether individuals adopt in response to social exposure, they do not capture how the
process of adoption itself may shape subsequent advocacy behavior. This omission limits their ability to
capture reinforcement-driven amplification observed in practice.
To address these limitations, we introduce the Pressure Threshold (PT) model, a tractable extension of
the Linear Threshold framework that captures conviction formation through social reinforcement. In the PT
model, an individual’s influence is not fixed but instead depends on the cumulative social pressure expe-
rienced at the time of adoption. Specifically, individuals who adopt after repeated or consistent exposure
to their peers develop greater conviction and, as a result, exert stronger influence on others in subsequent
interactions. This formulation provides a simple yet expressive way to operationalize reinforcement-driven
amplification within a familiar diffusion framework. By allowing influence strength to evolve endogenously
with the adoption process, the model captures a key behavioral mechanism underlying word-of-mouth
dynamics while preserving the interpretability and transparency of threshold-based models. As such, the
PT model bridges the gap between classical diffusion models and empirical observations of reinforce-
ment, providing a foundation for studying how conviction formation shapes both diffusion patterns and the
effectiveness of network-based marketing interventions.
By retaining the additive semantics and interpretability of the Linear Threshold model while making
reinforcement explicit, the PT framework offers a principled and transparent way to move beyond static LT
and IC assumptions. Importantly, this modeling approach is strongly supported by empirical evidence. As
we demonstrate through empirical validation later in the paper, incorporating pressure-based amplification
significantly improves the accuracy of diffusion predictions on real-world social networks. The PT model
thus provides both a richer behavioral foundation for influence maximization and a practical tool for aligning
diffusion models with observed online and offline social dynamics.
1.1. Contributions
This paper makes four main contributions that advance the modeling and analysis of social influence under
reinforcement, with direct implications for marketing interventions in networks. Our contributions span
modeling, theory, and managerial insights.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
4
1.A Behavioral Model of Conviction-Driven Diffusion.We introduce the Pressure Threshold (PT)
diffusion model, an extension of the Linear Threshold (LT) model that explicitly incorporates local social
reinforcement. In PT, a node’s outgoing influence depends on the cumulative social pressure that triggered its
activation, capturing the idea that individuals who adopt under stronger peer reinforcement develop greater
conviction and become more influential in subsequent interactions. This provides a tractable and interpretable
framework for modeling amplification in word-of-mouth processes while preserving the additive structure
of threshold-based diffusion.
2.Implications for Targeting and Seeding Decisions.We study how reinforcement reshapes optimal
intervention strategies in the influence maximization problem. We show that amplification fundamentally
alters the structure of effective targeting, favoring coordinated seeding in cohesive regions of the network
where repeated exposure can strengthen downstream influence. These results provide new insights for
marketing strategies such as influencer selection, referral program design, and campaign coordination in
networked environments.
3.Empirical Evidence on Amplification and Predictive Performance.Through experiments on syn-
thetic and real-world networks, as well as validation on timestamped social media cascades, we show that
reinforcement-driven diffusion produces substantially different, and consistently larger, cascades than stan-
dard LT models, particularly in dense or clustered networks. We further demonstrate that the PT model
significantly improves diffusion prediction accuracy, indicating that explicitly modeling social pressure
yields a more faithful representation of observed word-of-mouth dynamics.
4.Theoretical and Algorithmic Foundations for Reinforcement-Based Diffusion.We provide a struc-
tural analysis of influence maximization under PT, showing that the problem remains NP-hard and that
the influence function is generally neither monotone nor submodular. Despite this departure from classical
assumptions, we develop a Sandwich Approximation framework that enables the use of greedy methods
with data-dependent guarantees, and demonstrate that scalable heuristics adapted from LT, such as CELF,
remain effective in our empirical settings. We also support these analyses with an efficient implementation
built on the CyNetDiff (Robson et al. 2024) library, enabling large-scale simulation and reproducibility.
Together, these results show that incorporating social reinforcement leads to qualitatively different diffu-
sion dynamics and targeting strategies than those predicted by static models, while remaining computationally
tractable and practically implementable for network-based decision making.
1.2. Organization
The remainder of the paper is organized as follows. Section 2 develops the conceptual motivation and situates
the paper within the related literature on reinforcement, persuasion, and amplification in social influence.
Section 3 introduces the Pressure Threshold diffusion model, provides intuition for its mechanism, and
interprets the reinforcement parameter in behavioral and decision-relevant terms. Section 4 formulates influ-
ence maximization under pressure as a managerial decision problem and analyzes its structural properties,

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
5
including NP-hardness and the failure of monotonicity and submodularity. Section 5 presents model behav-
ior and develops the sandwich approximation framework, highlighting how greedy methods can be applied
effectively despite weakened theoretical guarantees. Section 6 reports computational experiments on syn-
thetic and real-world networks, illustrating how reinforcement alters diffusion dynamics, seed selection, and
intervention outcomes. Section 7 provides an empirical evaluation of the sandwich approximation strategy
and demonstrates data-dependent approximation guarantees in practice. Section 8 evaluates the predictive
performance of the PT model using real-world social media cascades. Section 9 discusses managerial and
societal implications for marketing, platform design, and information governance. Section 10 concludes
with a summary of contributions and directions for future research.
2. Conceptual Motivation and Related Literature
Diffusion models have a long history across multiple disciplines, including marketing, sociology, and
epidemiology, where they are used to understand how behaviors, products, and information spread through
populations. In marketing, diffusion has long been studied as a central mechanism underlying product
adoption and word-of-mouth dynamics (Bass 1969, Goldenberg et al. 2001, Rogers 2003, Libai et al.
2013). More recent work emphasizes the role of social media, network interactions, and digital platforms
in shaping diffusion outcomes and firm value (Aral et al. 2013, Lobel et al. 2017). In epidemiology, the
Susceptible–Infected–Recovered (SIR) model introduced a compartmental approach that clarified how local
transmission mechanisms aggregate into population-level dynamics (Kermack and McKendrick 1927). In
the social sciences, threshold-based models provided a complementary behavioral perspective. In particular,
Granovetter (1978) conceptualized adoption as a function of cumulative peer influence, highlighting how
individual decision rules interact with network structure to produce aggregate diffusion patterns.
Building on these foundations, diffusion in networks has been widely modeled using threshold-based
and cascade-based frameworks that formalize how peer influence propagates through social structures.
Among the most prominent are the Linear Threshold (LT) and Independent Cascade (IC) models introduced
by Kempe et al. (2003), which translate behavioral insights from sociology and marketing into tractable
stochastic processes on networks. These models provide a unifying framework for studying how individual-
level responses to social exposure generate aggregate diffusion patterns and have been extensively used
to analyze word-of-mouth dynamics, social media influence, and network-based marketing interventions
(Goldenberg et al. 2001, Aral et al. 2013, Lobel et al. 2017). Their appeal lies not only in analytical tractability
but also in their interpretability: both LT and IC explicitly link adoption decisions to peer influence, making
them well suited for studying how local interactions shape global outcomes. As a result, they have become the
dominant modeling paradigms for diffusion and form the basis for much of the work on targeting, seeding,
and intervention design in networked settings.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
6
Within these models, a central decision problem is influence maximization (IM), which seeks to identify
a set of initial adopters (or “seed” nodes) that maximizes downstream diffusion. First introduced in the
context of viral marketing by Domingos and Richardson (2001), IM provides a formal framework for
allocating marketing resources across individuals in a network to maximize word-of-mouth impact. The
work of Kempe et al. (2003) established the computational foundations of the problem by proving NP-
hardness, identifying conditions under which the influence function is submodular, and introducing greedy
approximation algorithms with provable guarantees.
Building on this foundation, a large and active literature has developed algorithms to improve the scalability
and practical applicability of IM. These include algorithmic refinements such as Cost-Effective Lazy Forward
(CELF) (Leskovec et al. 2007) and its extensions (Goyal et al. 2011), sampling-based approaches such as
Reverse Influence Sampling (RIS) (Borgs et al. 2014), lightweight heuristics such as degree discounting
(Chen et al. 2009), and more recent advances in scalable implementations (Tang et al. 2015, Borgs et al.
2014). In parallel, researchers have explored extensions that incorporate network structure and learning,
including community-aware heuristics (Umrawal and Aggarwal 2023, Umrawal et al. 2023b, Robson and
Umrawal 2025) and adaptive or data-driven approaches (Kumar et al. 2022).
Beyond the classical formulation, a wide range of variants have been studied to better capture real-world
marketing and decision-making settings. These include models with partial or fractional incentives (Chen
et al. 2020, Umrawal et al. 2023a, 2026, Bhimaraju et al. 2024), online and adaptive influence maximization
(Mallipeddi et al. 2022, Agarwal et al. 2022, Nie et al. 2022, Xu and Umrawal 2026), fairness-aware
interventions (Becker et al. 2022, Lin et al. 2023, Nguyen et al. 2022), and learning-based approximations
of influence functions (Kumar et al. 2022). Comprehensive surveys of these developments can be found
in Li et al. (2023). Collectively, this body of work has significantly advanced the algorithmic treatment of
influence maximization while largely retaining the static diffusion assumptions inherited from LT and IC.
In parallel, a separate line of work has sought to move beyond static diffusion models by incorporating
temporal dynamics and evolving network structure. These approaches recognize that social systems are
often nonstationary, with influence patterns and network connections changing over time. For example,
Zhuang et al. (2013) studied diffusion processes with time-varying edges, while Xie et al. (2015) proposed
DynaDiffuse, which combines continuous-time propagation with dynamically evolving influence weights.
More broadly, continuous-time and dynamic network models have been used to capture temporal patterns
in information spread and user interaction, particularly in social media and online platforms.
From a marketing perspective, such dynamic models are closely related to efforts to understand how
timing, exposure frequency, and campaign scheduling affect consumer behavior and diffusion outcomes
(Aral et al. 2013, Pan et al. 2025, Kanuri et al. 2018). These models provide important insights into when
and how influence propagates, particularly in settings where user activity and connections evolve. However,

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
7
they primarily focus on temporal and structural variation in diffusion processes, rather than on how the
experience of social reinforcement influences individual behavior.
In contrast, the Pressure Threshold model proposed in this paper focuses on a complementary dimension:
how cumulative social pressure at the point of adoption shapes subsequent influence. While dynamic dif-
fusion models relax assumptions about time and network structure, they generally retain a static notion of
influence strength conditional on adoption. The PT model instead endogenizes influence strength through
reinforcement, enabling the study of amplification effects that arise from repeated exposure and peer vali-
dation.
Several studies have examined the empirical accuracy of diffusion models by comparing simulated
cascades with real-world diffusion data. Kuo et al. (2011) evaluated predictive performance across models
and found that IC often performs better for direct prediction tasks, whereas LT exhibits advantages in indirect
or aggregated comparisons. Ananthasubramaniam et al. (2024) analyzed Twitter hashtag propagation and
showed that predictive accuracy depends strongly on both network topology and content characteristics,
highlighting the sensitivity of diffusion outcomes to modeling assumptions.
From a marketing perspective, these findings underscore the importance of selecting diffusion models that
accurately reflect underlying behavioral mechanisms, particularly in settings where firms rely on predictive
models to guide targeting and campaign design. Empirical work by Aral and Walker (2012) provides direct
evidence of cumulative social influence in product adoption, supporting threshold-based representations of
peer effects. More recent work in influencer marketing further demonstrates the importance of repeated
exposure and reinforcement in driving engagement and diffusion outcomes. For example, Mallipeddi et al.
(2022) show using large-scale social media data that multiple exposures lead to non-linear, diminishing
returns in engagement and that message timing and spacing significantly shape diffusion outcomes. More
broadly, research on social media and influencer marketing emphasizes that exposure, repetition, and peer
validation play a central role in shaping engagement and word-of-mouth dynamics (Aral et al. 2013, Pan
et al. 2025).
Taken together, this evidence suggests that the predictive performance of diffusion models depends
critically on how they capture user behavior and social influence. While existing models account for exposure
and network structure, they typically do not incorporate reinforcement effects that arise from repeated or
consistent peer influence. This limitation is particularly important in modern online and marketing contexts,
where repeated exposure and peer validation are central to both adoption and subsequent influence.
The Pressure Threshold model introduced in this paper addresses this gap by incorporating local social
reinforcement directly into the diffusion process. By allowing influence strength to depend on cumulative
social pressure at the time of activation, the PT framework provides a tractable and interpretable way to
model conviction formation and amplification, while remaining compatible with influence maximization
analysis and empirical validation.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
8
3. Pressure Threshold Diffusion Model
This section introduces the Pressure Threshold (PT) diffusion model and formalizes the mechanism by
which local social reinforcement shapes influence propagation. Our goal is to provide a transparent and
behaviorally interpretable model that captures how conviction formed through peer pressure can amplify
downstream influence, while remaining closely connected to classical threshold-based diffusion frameworks.
This mechanism is motivated by empirical evidence from social media and marketing contexts, where
repeated exposure, peer validation, and cumulative persuasion are known to shape both adoption decisions
and subsequent word-of-mouth influence. In particular, recent studies of online engagement suggest that
individuals exposed to consistent and reinforcing social signals are not only more likely to adopt but also
more likely to actively propagate information.
We begin by reviewing the Linear Threshold (LT) model as a baseline, since PT generalizes its structure
and semantics. We then define the PT model, describe its diffusion dynamics in detail, and interpret its
key parameters in terms relevant for social and managerial decision contexts. Throughout, we emphasize
interpretability and behavioral plausibility, positioning PT as a mechanism for studying reinforcement-driven
diffusion prior to any consideration of optimization or algorithmic design.
The Linear Threshold (LT) model occupies a central role in the study of influence diffusion because
it provides a parsimonious abstraction of cumulative social influence. In the LT framework, individuals
adopt a behavior once the total influence exerted by their neighbors exceeds an individual-specific threshold,
reflecting classic theories of collective behavior and social pressure (Granovetter 1978). This additive
formulation has proven valuable both for its interpretability and for its analytical properties, forming the
basis for much of the modern influence maximization literature (Kempe et al. 2003).
Beyond its conceptual clarity, the LT model has become a standard reference point for algorithmic analysis
because it cleanly separates network structure from behavioral response. Influence is encoded through fixed
edge weights, while heterogeneity in adoption behavior is captured through exogenous thresholds. This
structure enables rigorous study of diffusion dynamics and intervention strategies, and it underpins many of
the approximation guarantees developed for influence maximization.
At the same time, the LT model treats influence strength as static and does not account for the possibility
that individuals who adopt under strong peer pressure may subsequently become more influential advocates.
As discussed in Section 2, empirical evidence from online and offline social systems suggests that local
reinforcement and social validation can substantially amplify downstream influence. These patterns are
especially salient in modern digital environments, where repeated exposure and coordinated messaging
can strengthen conviction and increase the likelihood of subsequent word-of-mouth propagation. These
observations motivate extensions of the LT framework that preserve its interpretability while relaxing its
static influence assumption.
We next present the formal definition of the Linear Threshold model, which establishes notation and
serves as the baseline against which the Pressure Threshold model is defined.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
9
3.1. Formal Definition: Linear Threshold Model
Given that the Pressure Threshold model generalizes the Linear Threshold (LT) model, we begin by formally
defining the LT diffusion process. Let𝐺=(𝑉,𝐸)be a directed graph, where𝑉is the set of nodes and
𝐸⊆𝑉×𝑉is the set of directed edges. Each edge(𝑢,𝑣)∈𝐸is assigned a weight𝑤 𝑢𝑣∈[0,1], representing
the influence exerted by node𝑢on node𝑣. The weights satisfy the normalization condition
∑︁
𝑢∈𝑁(𝑣)
𝑤𝑢𝑣≤1for each𝑣∈𝑉,
where𝑁(𝑣)denotes the set of in-neighbors of node𝑣.
Each node𝑣∈𝑉is also assigned an activation threshold𝜃 𝑣, drawn independently and uniformly at random
from the interval(0,1]. Intuitively,𝜃 𝑣 represents the minimum cumulative influence required for node𝑣to
adopt the behavior.
Diffusion proceeds in discrete time steps. Let𝑆⊆𝑉denote an initial seed set of active nodes, and let
𝐴𝑡⊆𝑉denote the set of active nodes at time𝑡, with𝐴 0 =𝑆. At each subsequent time step, an inactive
node𝑣∈𝑉\𝐴 𝑡 becomes active if the cumulative influence from its active in-neighbors meets or exceeds its
threshold:
∑︁
𝑢∈𝑃(𝑣)
𝑤𝑢𝑣≥𝜃 𝑣,
where
𝑃(𝑣)={𝑢∈𝐴 𝑡 :(𝑢,𝑣)∈𝐸}
denotes the set of currently active in-neighbors of𝑣. Once a node becomes active, it remains active perma-
nently. The diffusion process terminates when no additional nodes become active.
For clarity, we consistently distinguish between the static set of in-neighbors𝑁(𝑣)and the time-dependent
subset𝑃(𝑣)of in-neighbors that are active at time𝑡.
We define the influence of a seed set𝑆⊆𝑉under the Linear Threshold model as the expected number
of nodes activated by the diffusion process initiated from𝑆, where the expectation is taken over the random
thresholds𝜃 𝑣∈(0,1]. More generally, for any diffusion model𝑀, we denote the expected influence of𝑆by
𝜎𝑀(𝑆).
The influence maximization problem under a diffusion model𝑀is then defined as follows. Given a
directed graph𝐺=(𝑉,𝐸)and a budget𝑘, select a seed set𝑆⊆𝑉with|𝑆|≤𝑘that maximizes expected
influence:
arg max
𝑆⊆𝑉
𝜎𝑀(𝑆)subject to|𝑆|≤𝑘.
This formulation provides a direct connection between diffusion dynamics and strategic intervention, and it
serves as the decision problem studied throughout the remainder of the paper.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
10
While the Linear Threshold model provides a clean and interpretable framework for modeling cumulative
social influence, it assumes that influence strength is static throughout the diffusion process. In particular,
once a node becomes active, the influence it exerts on its neighbors is fixed by the underlying network
structure and does not depend on the circumstances under which the node itself was adopted.
A growing body of empirical evidence suggests that this assumption may be overly restrictive in many
social systems. Individuals who adopt a behavior after experiencing strong peer pressure or broad social
support often develop greater conviction and become more persuasive advocates in turn. These effects are
especially pronounced in modern digital and marketing environments, where repeated exposure, coordinated
messaging, and peer validation can significantly amplify downstream influence. Static diffusion models such
as LT do not capture this feedback between the pressure that triggers adoption and the influence exerted
thereafter.
The Pressure Threshold (PT) model relaxes this static influence assumption while preserving the core
structure and interpretability of the LT framework. Rather than modifying the activation rule itself, PT intro-
duces a localized reinforcement mechanism that adjusts a node’s outgoing influence at the moment it becomes
active, based on the cumulative social pressure it experienced. This design ensures that reinforcement arises
as a consequence of adoption, rather than as an independent driver of activation.
By making reinforcement explicit but minimal, the PT model maintains the additive semantics of threshold-
based diffusion, avoids recursive feedback loops, and remains compatible with efficient simulation and
empirical calibration. We next present the formal definition of the PT diffusion process, beginning with the
shared activation rule and then specifying how influence is updated through a two-phase mechanism.
While the activation rule in the Pressure Threshold model is identical to that of the Linear Threshold
model, PT departs from LT in how influence evolves after a node becomes active. To capture reinforcement
in a controlled and interpretable manner, the PT diffusion process is organized into two distinct phases at
each time step.
Two-phase diffusion structure.Each round of the PT diffusion process consists of the following phases:
1.Activation Phase.All inactive nodes evaluate their cumulative incoming influence based on the current
edge weights. Nodes whose cumulative influence meets or exceeds their threshold become newly active,
exactly as in the LT model.
2.Influence Adjustment Phase.Nodes that activate during the current round update the influence they
exert on their neighbors as a function of the social pressure they experienced at activation.
This separation emphasizes that reinforcement in PT is a consequence of adoption rather than a driver of
it. Influence is first evaluated using the existing network weights, and only after adoption does the model
allow a node’s outgoing influence to change. By design, this prevents reinforcement from affecting activation
decisions within the same time step and avoids recursive feedback effects that could otherwise complicate
diffusion dynamics.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
11
Incoming pressure at activation.To formalize reinforcement, we first define the total incoming influence
received by a node at the moment it becomes active. Let𝑣be a node that activates at time𝑡. We define the
incoming pressureexperienced by𝑣at activation as
𝐼𝑣 =
∑︁
𝑢∈𝑃(𝑣)
𝑤𝑢𝑣,
where𝑃(𝑣)={𝑢∈𝐴 𝑡 :(𝑢,𝑣)∈𝐸}denotes the set of active in-neighbors of𝑣at the time of activation.
The quantity𝐼 𝑣 summarizes the cumulative social influence that triggered node𝑣’s adoption. In the PT
model, this pressure plays a central role in determining how strongly𝑣influences others after becoming
active. Importantly,𝐼 𝑣 is evaluated using the pre-activation edge weights and is computed only once, at the
time of activation.
3.2. Formal Definition: Pressure Threshold Diffusion Process
We now formally define the Pressure Threshold (PT) diffusion model. The PT model is defined on the same
underlying graph structure as the Linear Threshold model and retains the same threshold-based activation
rule. As a result, PT preserves the core semantics of cumulative influence while modifying how influence
evolves after activation through a reinforcement mechanism tied to experienced social pressure.
Let𝐺=(𝑉,𝐸)be a directed graph, where𝑉denotes the set of nodes and𝐸⊆𝑉×𝑉denotes the set of
directed edges. Each edge(𝑢,𝑣)∈𝐸is assigned a weight𝑤 𝑢𝑣∈[0,1]such that
∑︁
𝑢∈𝑁(𝑣)
𝑤𝑢𝑣≤1for each𝑣∈𝑉,
where𝑁(𝑣)denotes the set of in-neighbors of𝑣. Unless otherwise stated, we initialize weights according to
the weighted-cascade convention,𝑤𝑢𝑣 =1/in-degree(𝑣). Each node𝑣∈𝑉is assigned an activation threshold
𝜃𝑣∈(0,1], drawn independently and uniformly at random.
Diffusion unfolds in discrete time steps and begins from an initial seed set𝑆⊆𝑉, which is assumed to
be active at time𝑡=0. Let𝐴 𝑡⊆𝑉denote the set of active nodes at time𝑡, with𝐴 0 =𝑆. At each subsequent
time step, inactive nodes evaluate whether the cumulative influence from their active in-neighbors meets or
exceeds their threshold.
Formally, at time step𝑡+1, a node𝑣∈𝑉\𝐴 𝑡 becomes active if
∑︁
𝑢∈𝑃(𝑣)
𝑤𝑢𝑣≥𝜃 𝑣,
where𝑃(𝑣)={𝑢∈𝐴 𝑡 :(𝑢,𝑣)∈𝐸}denotes the set of currently active in-neighbors of𝑣. As in the LT model,
the PT diffusion process is progressive: once a node becomes active, it remains active permanently. Diffusion
continues until no additional nodes activate.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
12
Influence amplification.The PT model translates incoming pressure at activation into increased outgoing
influence through a simple additive update rule. Let𝑣be a node that becomes active at time𝑡, and let𝐼 𝑣
denote the total incoming influence received at activation, as defined above. The strength of reinforcement
is governed by a nonnegative amplification parameter𝛼≥0. This parameter captures the degree to which
individuals internalize social reinforcement when forming persuasive influence.
For each outgoing edge(𝑣,𝑠)∈𝐸such that the neighbor𝑠is inactive at time𝑡, the influence weight from
𝑣to𝑠is updated according to
𝑤′ 𝑣𝑠 =min 1, 𝑤𝑣𝑠+𝛼·𝐼 𝑣 ,
where𝑤′ 𝑣𝑠 denotes the updated influence weight after reinforcement.
The use of themin(1,·)operator ensures that all influence weights remain within the unit interval,
consistent with the range of activation thresholds. Because the amplification is additive and proportional to
the pressure that triggered activation, nodes that adopt after experiencing greater cumulative influence exert
correspondingly stronger influence on their neighbors.
One-shot and localized reinforcement.Reinforcement in the PT model is applied only once, at the moment
a node becomes active. After this update, the outgoing weights of node𝑣remain fixed for the remainder of
the diffusion process. Moreover, influence adjustments are applied only to edges directed toward currently
inactive neighbors; edges pointing to already active nodes are not updated, since additional influence along
those edges would not affect future diffusion.
These restrictions are deliberate. By limiting reinforcement to a single update and restricting it to edges
that can influence future activations, the PT model avoids recursive amplification loops and maintains
stable diffusion dynamics even in dense networks. At the same time, the additive update rule preserves the
interpretability and cumulative nature of threshold-based influence aggregation.
Influence under the PT model.As in the Linear Threshold model, the diffusion process under PT is
progressive: nodes may transition from inactive to active, but never the reverse. Because reinforcement is
applied only once at the moment of activation and no subsequent feedback occurs, the PT diffusion process
is guaranteed to terminate in a finite number of steps.
We define the influence of a seed set𝑆⊆𝑉under the PT model as the expected number of nodes
activated by the diffusion process initiated from𝑆, where the expectation is taken over the random thresholds.
Consistent with our earlier notation, we denote this quantity by𝜎PT(𝑆). This influence measure serves as the
primary performance metric for both empirical evaluation and the influence maximization decision problem
analyzed in subsequent sections.
Interpretation of the reinforcement parameter.The amplification parameter𝛼governs the strength of
social reinforcement in the PT model. When𝛼=0, the influence adjustment phase is inactive, and the PT
model reduces exactly to the classical Linear Threshold model. Small values of𝛼correspond to diffusion

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
13
dynamics that remain close to LT, while larger values induce stronger reinforcement effects, allowing nodes
that adopt under high pressure to exert substantially greater downstream influence.
Importantly,𝛼modulates behavioral feedback rather than network structure. As such, it can be interpreted
as a domain-dependent reinforcement coefficient reflecting how strongly individuals internalize social vali-
dation when forming convictions. In practice,𝛼can be treated as a tunable hyperparameter and calibrated
using empirical diffusion traces, analogous to the way contagion strength or persuasion intensity is estimated
in epidemiological and social influence models.
Algorithmic summary.For clarity and reproducibility, Algorithm 1 summarizes the complete Pressure
Threshold diffusion process, including both the activation and influence adjustment phases. The algorithm
provides an explicit procedural description of PT diffusion and will serve as the basis for all simulations and
experiments reported later in the paper.
Together, the definitions above fully specify the Pressure Threshold diffusion model. PT retains the
cumulative activation semantics and interpretability of the Linear Threshold framework while introducing
a controlled form of social reinforcement through a one-shot amplification mechanism. By tying outgoing
influence to the pressure experienced at adoption, the model captures conviction-driven amplification effects
observed in real social systems without introducing recursive feedback or destabilizing dynamics.
With the diffusion process now fully defined, we turn to its implications for decision-making on networks.
In particular, we study how social reinforcement alters the influence maximization problem, a canonical
task in marketing, information campaigns, and public interventions. The next section formulates influence
maximization under the Pressure Threshold model and analyzes its computational and structural properties.
4. Influence Maximization under the Pressure Threshold Model: Implications for
Viral Marketing and Network Interventions
We now study the implications of the Pressure Threshold (PT) model for decision-making on networks,
focusing on the influence maximization (IM) problem. In many marketing and information campaign settings,
firms must identify a limited set of individuals to target in order to maximize downstream adoption and
word-of-mouth spread. Under classical diffusion models such as Linear Threshold, this problem is well-
understood and admits strong structural properties that enable efficient optimization. The PT model, however,
fundamentally alters this problem by introducing reinforcement-driven changes in influence strength, making
the effectiveness of a seed set depend not only on who adopts, but also on how adoption occurs.
Under classical diffusion models such as the Linear Threshold model, influence maximization is well
understood as a combinatorial optimization problem with favorable structural properties. In particular, the
expected influence function is known to be monotone and submodular, enabling greedy algorithms with
strong approximation guarantees. These guarantees underpin much of the practical appeal of influence
maximization methods.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
14
Algorithm 1Pressure Threshold (PT) Diffusion
Require:Directed graph𝐺=(𝑉,𝐸); influence weights𝑤 𝑢𝑣∈[0,1]; thresholds𝜃 𝑣∈(0,1]; seed set𝑆⊆𝑉;
amplification parameter𝛼≥0
1:𝑡←0;𝐴 𝑡←𝑆 ⊲initial active set
2:repeat
3:𝑁 𝑡←∅⊲nodes newly activating at time𝑡
4:for all𝑣∈𝑉\𝐴 𝑡 do⊲activation phase
5:𝑃 𝑡(𝑣)←{𝑢∈𝐴 𝑡 :(𝑢,𝑣)∈𝐸}
6:𝐼 𝑣← ˝ 𝑢∈𝑃 𝑡(𝑣) 𝑤𝑢𝑣
7:if𝐼 𝑣≥𝜃 𝑣 then
8:𝑁 𝑡←𝑁 𝑡∪{𝑣}
9:end if
10:end for
11:if𝑁 𝑡 =∅then
12:break⊲no new activations; diffusion halts
13:end if
14:for all𝑣∈𝑁 𝑡 do⊲influence adjustment phase (one-shot)
15:for all(𝑣,𝑠)∈𝐸with𝑠∉𝐴 𝑡 do
16:𝑤 𝑣𝑠←min 1, 𝑤𝑣𝑠+𝛼·𝐼 𝑣 
17:end for
18:end for
19:𝐴 𝑡+1←𝐴 𝑡∪𝑁 𝑡;𝑡←𝑡+1
20:untilfalse
21:return𝐴 𝑡
The presence of social reinforcement fundamentally alters this decision landscape. Because influence
strength in the PT model depends on the social pressure experienced at activation, the marginal value
of selecting a particular node as a seed can depend on complex interactions involving activation order,
neighborhood composition, and reinforcement dynamics. As a result, intervention strategies that are optimal
under static diffusion assumptions need not perform well when reinforcement effects are present.
We begin by formally stating the influence maximization problem induced by the Pressure Threshold
diffusion process. Let𝐺=(𝑉,𝐸)be a directed graph, and let𝜎 PT(𝑆)denote the expected influence of a
seed set𝑆⊆𝑉under the PT model, as defined in Section 3. Given a budget constraint𝑘∈N, the influence

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
15
maximization problem under PT asks for a seed set that maximizes expected spread:
max
𝑆⊆𝑉
𝜎PT(𝑆)subject to|𝑆|≤𝑘.
This formulation mirrors the classical influence maximization problem studied under the Linear Threshold
and Independent Cascade models, differing only in the underlying diffusion dynamics that determine the
influence function. However, because PT endogenizes influence strength through reinforcement, the resulting
objective function depends on both the set of activated nodes and the pathways through which activation
occurs. This distinction fundamentally alters the structural properties that enable efficient optimization under
classical models.
Before turning to algorithmic approaches, it is important to understand the inherent computational com-
plexity of influence maximization under the Pressure Threshold model. Establishing such limits clarifies
which performance guarantees are achievable in principle and which must instead rely on heuristic or
data-driven methods.
In classical diffusion settings, influence maximization is known to be computationally intractable. Under
both the Linear Threshold and Independent Cascade models, the problem is NP-hard, even to approximate
beyond a constant factor (Kempe et al. 2003). These results motivate the widespread use of greedy heuristics
supported by approximation guarantees under favorable structural conditions.
At first glance, the additional structure introduced by reinforcement might appear to simplify the decision
problem. Because PT ties influence strength to observed social pressure, one might hope that this feedback
introduces regularities that reduce combinatorial complexity or enable more efficient optimization. Whether
this intuition holds is not obvious a priori and requires careful analysis.
We next show that this is not the case. Despite its additional behavioral structure, influence maximization
under the PT model remains computationally hard. In particular, reinforcement preserves the fundamental
intractability of the classical problem, even in regimes where PT reduces to familiar diffusion dynamics. At
the same time, reinforcement disrupts key structural properties such as submodularity that underpin classical
approximation guarantees, creating new challenges for algorithm design and analysis.
4.1. Computational Complexity
We begin by establishing the computational hardness of influence maximization under the Pressure Threshold
model.
Theorem 1.Influence maximization under the Pressure Threshold (PT) diffusion model is NP-hard.
Proof.The influence maximization problem under the Linear Threshold (LT) model is known to be
NP-hard (Kempe et al. 2003). We reduce this problem to influence maximization under the PT model.
Consider an arbitrary LT instance defined on a graph𝐺=(𝑉,𝐸)with seed budget𝑘. Construct the
corresponding PT instance on the same graph with the same budget and with amplification parameter𝛼=0.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
16
When𝛼=0, the influence adjustment phase in the PT diffusion process is inactive, and the PT model reduces
exactly to the LT model. In particular, for every seed set𝑆⊆𝑉,
𝜎PT(𝑆;𝛼=0)=𝜎 LT(𝑆).
Thus, an optimal solution to the PT influence maximization problem with𝛼=0is also an optimal
solution to the original LT influence maximization problem. Because this transformation can be performed
in polynomial time, a polynomial-time algorithm for PT influence maximization would imply one for LT
influence maximization. Therefore, influence maximization under the PT model is NP-hard.
The NP-hardness result above establishes that social reinforcement does not alleviate the fundamen-
tal computational difficulty of influence maximization. Even though the PT model introduces additional
behavioral structure by linking influence strength to social pressure, this structure does not eliminate the
combinatorial difficulty inherent in selecting an optimal seed set. As a result, any algorithmic approach to
influence maximization under PT must contend with the same worst-case intractability that arises under
classical diffusion models.
At the same time, NP-hardness alone does not fully characterize the practical tractability of the problem or
the effectiveness of solution methods. In classical settings, influence maximization remains NP-hard despite
the availability of efficient greedy algorithms with strong approximation guarantees, driven by favorable
structural properties of the influence function.
These guarantees depend critically on properties such as monotonicity and submodularity. Whether such
properties continue to hold under the Pressure Threshold model is therefore a central question. Because
reinforcement introduces context dependence into diffusion dynamics, it may alter the behavior of the
influence function in ways that are incompatible with classical approximation theory.
We next examine how social reinforcement affects the monotonicity and submodularity of the PT influence
function, and discuss the implications for optimization in marketing and network intervention settings.
4.2. Monotonicity Analysis
We begin by examining the monotonicity of the influence function under the PT model. Monotonicity is a
central property in classical influence maximization, as it ensures that adding additional seed nodes cannot
reduce expected influence and supports stable targeting strategies in marketing and intervention contexts.
Definition 1 (Monotonicity).A set function𝑓: 2 𝑉→Rismonotoneif for all seed sets𝑆⊆𝑇⊆𝑉, it
holds that
𝑓(𝑆)≤𝑓(𝑇).
Under the Linear Threshold and Independent Cascade models, the expected influence function is mono-
tone. This property ensures that selecting additional seeds is never harmful and, together with submodularity,
enables greedy algorithms with strong approximation guarantees. In the absence of monotonicity, however,

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
17
standard greedy reasoning no longer applies: adding a seed may reduce overall influence, complicating both
analysis and intuition.
We now show that the influence function under the Pressure Threshold model does not satisfy monotonicity
in general. Unlike classical diffusion models, monotonicity need not hold under PT due to the endogenous
role of reinforcement at activation, which creates a subtle trade-off between early seeding and influence
amplification.
Theorem 2.There exists a directed graph𝐺, a seed budget𝑘, and an amplification parameter𝛼>0such
that the PT influence function𝜎 PT(·)is not monotone.
Proof.The proof proceeds by construction. We exhibit an instance in which adding a node to the seed
set suppresses downstream reinforcement that would otherwise arise through propagation.
Under the PT model, only nodes that activate through diffusion (as opposed to being seeded) receive
influence amplification. Thus, seeded nodes do not accumulate incoming pressure and cannot benefit from
reinforcement, whereas nodes activated endogenously may do so. As a result, seeding a node directly can
prevent that node from activating via social pressure, thereby eliminating the reinforcement effect it would
have generated had it been activated endogenously. In such cases, adding a node to the seed set can reduce
the total amplified influence in later rounds, leading to a strictly smaller expected cascade.
An explicit example demonstrating this effect is presented in the following subsection.
Illustrative example.We illustrate the non-monotonicity result in Theorem 2 with a simple example that
highlights the interaction between seeding and reinforcement.
Consider a directed graph𝐺=(𝑉,𝐸)with nodes arranged so that node𝑣can either be activated directly
as a seed or activated indirectly via social pressure from its neighbors. Let the amplification parameter
satisfy𝛼>0. Suppose that when𝑣is activated through diffusion, it receives sufficient incoming pressure to
substantially amplify its outgoing influence, enabling it to activate a downstream node𝑢. In contrast, when𝑣
is included in the seed set, it activates immediately but does not receive any incoming pressure and therefore
exerts only its baseline influence.
Let𝑆be a seed set that does not include𝑣. Under PT diffusion from𝑆, node𝑣activates endogenously
after accumulating influence from its neighbors, receives reinforcement upon activation, and subsequently
activates node𝑢. Now consider the augmented seed set𝑇=𝑆∪{𝑣}. In this case, node𝑣is activated
exogenously at the start of the diffusion process, receives no amplification, and fails to activate𝑢. As a result,
the final cascade originating from𝑇is strictly smaller than that originating from𝑆.
This example demonstrates that under PT diffusion, adding a node to the seed set can suppress downstream
reinforcement that would otherwise arise through social pressure. Consequently, the expected influence
under PT need not increase monotonically with the size of the seed set.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
18
4.3. Submodularity Analysis
We next examine submodularity of the influence function. Submodularity is a diminishing-returns property
that plays a central role in the algorithmic theory of influence maximization. Intuitively, a submodular
influence function guarantees that the marginal benefit of adding a node as a seed decreases as the seed set
grows.
Definition 2 (Submodularity).A set function𝑓: 2 𝑉→Rissubmodularif for all seed sets𝑆⊆𝑇⊆𝑉
and all nodes𝑣∈𝑉\𝑇, it holds that
𝑓(𝑆∪{𝑣})−𝑓(𝑆)≥𝑓(𝑇∪{𝑣})−𝑓(𝑇).
Under classical diffusion models such as Linear Threshold and Independent Cascade, the expected
influence function is both monotone and submodular. These properties together enable the celebrated
(1−1/𝑒)approximation guarantee for greedy algorithms (Nemhauser et al. 1978, Kempe et al. 2003).
Submodularity is particularly crucial, as it ensures that greedy selection remains near-optimal despite the
combinatorial nature of the problem.
In particular, reinforcement induces strategic complementarities among seed nodes, as the presence of
one seed can increase the marginal value of another through amplified propagation. The reinforcement
mechanism introduced by the PT model disrupts this diminishing-returns structure. Because activation under
PT can amplify future influence, the marginal contribution of a node can increase when it is added later
rather than earlier. This context dependence creates complementarities among seeds that are incompatible
with classical submodularity.
We formalize this observation below.
Theorem 3.There exists a directed graph𝐺, a seed budget𝑘, and an amplification parameter𝛼>0such
that the PT influence function𝜎 PT(·)is not submodular.
Proof.The proof again proceeds by construction. Under PT diffusion, adding a node to a larger seed
set can trigger reinforcement effects that do not arise when the same node is added to a smaller seed set.
In such cases, the marginal gain from adding a node increases with the size of the seed set, violating the
diminishing-returns property required for submodularity.
An explicit construction illustrating this effect is provided in the following subsection.
Illustrative example.We illustrate the non-submodularity result in Theorem 3 with a simple example
showing how reinforcement can increase marginal returns as the seed set grows.
Consider a directed graph in which node𝑣can be activated either weakly, with little incoming pressure,
or strongly, with substantial incoming pressure supplied by multiple active neighbors. Let𝛼>0. Suppose
that when𝑣activates under strong pressure, the resulting amplification of its outgoing influence is sufficient
to activate a downstream node𝑢, whereas activation under weak pressure fails to do so.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
19
Let𝑆be a small seed set in which only one of𝑣’s neighbors is active. Adding𝑣to𝑆causes𝑣to activate
immediately but without reinforcement, producing little downstream influence. As a result, the marginal
gain𝜎 PT(𝑆∪{𝑣})−𝜎 PT(𝑆)is small.
Now consider a larger seed set𝑇⊃𝑆that activates multiple neighbors of𝑣. In this setting, adding𝑣to
𝑇leads to activation under high incoming pressure, triggering reinforcement at activation and substantially
amplifying𝑣’s outgoing influence. This amplified influence enables𝑣to activate𝑢, yielding a larger marginal
gain:
𝜎PT(𝑇∪{𝑣})−𝜎 PT(𝑇)> 𝜎 PT(𝑆∪{𝑣})−𝜎 PT(𝑆).
Thus, the marginal contribution of node𝑣increases when it is added later rather than earlier. This behavior
directly contradicts the diminishing-returns requirement of submodularity and arises from reinforcement-
induced complementarities among seed nodes.
The results above establish that influence maximization under the Pressure Threshold model differs
fundamentally from its classical counterparts. While reinforcement does not alter the computational hardness
of the problem, it eliminates key structural properties that underpin standard approximation theory. In
particular, the PT influence function need not be monotone and need not be submodular, as reinforcement
introduces context dependence and complementarities that violate diminishing returns.
These findings have important implications for algorithm design. Classical greedy algorithms rely criti-
cally on monotonicity and submodularity to guarantee near-optimal performance. When these properties fail,
worst-case guarantees no longer apply, and naive application of greedy selection can lead to unpredictable
behavior, particularly in marketing and intervention settings where repeated exposure and peer validation
shape behavior. At the same time, the structural failures observed here are driven by meaningful behavioral
mechanisms rather than pathological constructions, suggesting that purely worst-case analysis may be overly
pessimistic.
The loss of classical structure does not preclude effective influence maximization in practice. Instead, it
calls for alternative approximation frameworks that explicitly account for reinforcement effects and provide
data-dependent performance bounds. In the next section, we develop such an approach by bounding the PT
influence function between monotone submodular surrogates, enabling principled greedy heuristics despite
the absence of traditional guarantees.
5. Model Behavior and Approximation Methods
The preceding section established that influence maximization under the Pressure Threshold (PT) model is
computationally hard and lacks the monotonicity and submodularity properties that support classical greedy
approximation guarantees. These challenges are particularly relevant in marketing and platform settings,
where decision-makers must operate with models that capture reinforcement and peer validation but still

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
20
admit tractable approximation methods. In this section, we take two complementary steps toward practical
decision support under reinforcement-driven diffusion.
First, we provide a compact model demonstration that builds intuition for how activation-triggered ampli-
fication alters diffusion dynamics relative to the Linear Threshold (LT) model. This demonstration is not
intended to establish general theoretical claims, but rather to illustrate, at a mechanistic level, how reinforce-
ment propagates through a network.
Second, we develop an algorithmic response to the loss of classical structure identified in Section 4.
By bounding the PT influence function between monotone submodular surrogates, we derive a sandwich
approximation framework that enables principled greedy seed selection despite the absence of traditional
worst-case guarantees.
5.1. Model Demonstration
To build intuition for the reinforcement dynamics introduced by the Pressure Threshold (PT) model, we
present a compact visualization contrasting PT and the classical Linear Threshold (LT) model on a small,
controlled instance. The objective is not to claim generality from a toy example, but rather to provide a
clear, step-by-step illustration of how additive amplification upon activation alters propagation relative to
static-weight diffusion on the same graph.
By holding the network structure, thresholds, and seed set fixed across models, this demonstration isolates
the effect of reinforcement and illustrates how local pressure-dependent amplification can accumulate over
time. The example serves as a concrete reference point for understanding the structural and algorithmic
results developed in later sections. In particular, it highlights how reinforcement transforms diffusion from
a purely structural process into one that depends on the history and intensity of activation.
We illustrate the PT dynamics using a small-scale example with amplification parameter𝛼=0.25on a
9-node network. Figures 1 and 2 visualize the evolution of PT diffusion alongside LT on the same graph and
with an identical seed set. A moderately large value of𝛼is chosen to highlight the qualitative distinction
between reinforcement-driven and static diffusion while keeping the example easy to trace visually.
Both models begin with two identical seed nodes at time𝑡=0. Activated nodes are shown in red, newly
activated nodes are highlighted with a black outline, and unactivated nodes are shown in blue. In the PT
model, edges whose weights are amplified during the influence adjustment phase are highlighted in red.
Node labels display the node index (underlined), together with the corresponding activation threshold𝜃.
In the earliest timesteps, PT and LT behave similarly, since all influence weights are initially identical and
no amplification has yet occurred. Differences begin to emerge once nodes activate through propagation in
PT and receive reinforcement (Figures 1). As amplification accumulates across rounds, PT enables additional
nodes to cross their activation thresholds, whereas the LT cascade stalls earlier (Figure 2). In this example,
PT ultimately achieves full network coverage, while LT terminates after activating only five nodes.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
21
PT Step 0 (No. of activated nodes = 2)
PT Step 1 (No. of activated nodes = 3)
PT Step 2 (No. of activated nodes = 5)
LT Step 0 (No. of activated nodes = 2)
LT Step 1 (No. of activated nodes = 3)
LT Step 2 (No. of activated nodes = 4)
Figure 1 Early diffusion stages under PT and LT on the same graph using an identical seed set. Visualizations
show the initial evolution of the diffusion process, during which the reinforcement effects are present but have not
yet accumulated strongly. Activated nodes are shown in red, newly activated nodes are highlighted in red with a
black outline, and unactivated nodes are shown in blue. Newly amplified edges resulting from PT’s influence
adjustment mechanism are highlighted in red. Node labels display the node index (underlined) together with the
corresponding activation threshold𝜃.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
22
PT Step 3 (No. of activated nodes = 7)
PT Step 4 (No. of activated nodes = 9)
PT Final Step (No. of activated nodes = 9)
LT Step 3 (No. of activated nodes = 5)
LT Final Step (No. of activated nodes = 5)
Figure 2 Later diffusion stages under PT and LT on the same graph using an identical seed set. As the diffusion
evolves, reinforcement effects intensify. PT continues amplifying outgoing influence along activated edges and
ultimately attains full network coverage, whereas LT halts after activating fewer nodes. Activated nodes are shown in
red, newly activated nodes are highlighted in red with a black outline, and unactivated nodes are shown in blue.
Newly amplified edges due to PT’s reinforcement mechanism are highlighted in red. Node labels display the node
index (underlined) together with the corresponding activation threshold𝜃.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
23
This simple example illustrates how activation-triggered reinforcement can qualitatively alter diffusion
outcomes, even when the network structure, thresholds, and initial seeds are fixed. In particular, it highlights
how local amplification effects can accumulate over time, enabling cascades that would otherwise stall under
static-weight diffusion. While this example is not intended to characterize typical or worst-case behavior, it
provides a concrete reference point for understanding how reinforcement manifests in the PT model. This
shift from static to reinforcement-driven diffusion is precisely what underlies the structural breakdown of
monotonicity and submodularity established earlier.
5.2. Consequences of Reinforcement for Optimization
As established in Section 4, influence maximization under the PT model remains NP-hard and lacks the
monotonicity and submodularity properties that support classical greedy guarantees. These structural vio-
lations arise from the same reinforcement mechanism illustrated in the preceding model demonstration:
activation-triggered amplification introduces context dependence and complementarities that are incompat-
ible with diminishing returns. From a decision perspective, this implies that the value of targeting a given
individual depends critically on the broader set of targeted individuals, rather than being separable across
nodes.
Rather than abandoning greedy approaches altogether, we develop an approximation framework that
explicitly accounts for reinforcement effects. Our strategy is to bound the PT influence function between
two tractable, monotone submodular functions. These bounds provide a principled way to evaluate greedy
solutions under PT, even when the true objective lacks favorable structure.
To address these challenges, we construct tractable surrogate models that preserve key aspects of PT
dynamics while restoring structural properties that enable efficient optimization.
5.2.1. Static Maximum-Pressure Model DefinitionWe begin by defining a static upper-bounding
diffusion model, denoted𝑀 +. The𝑀 + model is defined on the same graph structure as the PT and LT
models and uses the same initial parameters, but replaces PT’s dynamic reinforcement mechanism with a
static, worst-case amplification applied uniformly at the start of the diffusion process.
Let𝐺=(𝑉,𝐸)be a directed graph, where𝑉is the set of nodes and𝐸⊆𝑉×𝑉is the set of directed edges.
Each edge(𝑢,𝑣)∈𝐸is assigned a baseline weight𝑤 𝑢𝑣∈[0,1]such that ˝ 𝑢∈𝑁(𝑣) 𝑤𝑢𝑣≤1for each node𝑣,
where𝑁(𝑣)denotes the in-neighbors of𝑣. As in our earlier analyses, we initialize each weight according to
the weighted-cascade convention,𝑤𝑢𝑣 =1/in-degree(𝑣). Each node𝑣∈𝑉is assigned an activation threshold
𝜃𝑣∈(0,1].
The key observation underlying𝑀 + is that under PT diffusion, the total incoming pressure experienced
by a node at activation is bounded above by1under the weighted-cascade convention. This construction
provides a worst-case envelope of reinforcement effects, ensuring that𝑀 + captures the strongest possible
amplification consistent with the PT mechanism. Consequently, the maximum possible amplification applied

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
24
to any outgoing edge(𝑢,𝑣)during a PT cascade is𝛼. The𝑀 + model, therefore, replaces the dynamic,
activation-triggered updates of PT with a static pre-amplified weight defined as
𝑤+ 𝑢𝑣 =min{1, 𝑤𝑢𝑣+𝛼}.
Diffusion under the𝑀+ model proceeds exactly as in the Linear Threshold framework, with the exception
that static pre-amplified weights𝑤+ 𝑢𝑣 are used throughout the process. At each time step, an inactive node𝑣
becomes active if the cumulative influence from its active in-neighbors meets or exceeds its threshold:
∑︁
𝑢∈𝑃(𝑣)
𝑤+ 𝑢𝑣≥𝜃 𝑣.
As in LT and PT, the process is progressive and terminates when no further nodes activate.
Lemma 1.The𝑀 + model dominates the PT model in expected influence: for all seed sets𝑆⊆𝑉,
𝜎PT(𝑆)≤𝜎 𝑀+(𝑆).
Fix an arbitrary seed set𝑆and a realization of thresholds{𝜃 𝑣}𝑣∈𝑉 . Run both the PT and𝑀 + diffusion
processes on the same graph with these thresholds.
Let𝐴 PT 𝑡 and𝐴 𝑀+ 𝑡 denote the active sets at time𝑡under PT and𝑀 +, respectively. We prove by induction
on𝑡that𝐴 PT 𝑡 ⊆𝐴 𝑀+ 𝑡 .
In the base case,𝐴 PT 0 =𝐴 𝑀+ 0 =𝑆. Assume𝐴 PT 𝑡 ⊆𝐴 𝑀+ 𝑡 . Consider any node𝑣∉𝐴 PT 𝑡 . Under PT,𝑣activates
at time𝑡+1if the sum of dynamic incoming weights from𝐴 PT 𝑡 meets or exceeds𝜃 𝑣. Under𝑀 +,𝑣has at
least as many active parents, and each corresponding incoming weight satisfies𝑤 + 𝑢𝑣≥𝑤′ 𝑢𝑣. Therefore, any
node that activates under PT must also activate under𝑀+.
Thus𝐴 PT 𝑡+1⊆𝐴 𝑀+ 𝑡+1 , and by induction the inclusion holds at termination. Since this holds pointwise for
every threshold realization, it also holds in expectation, implying𝜎 PT(𝑆)≤𝜎 𝑀+(𝑆). This establishes that
𝑀+ provides a valid upper bound on PT diffusion for all seed sets.
Remark 1.Because the𝑀 + model uses static edge weights and follows the Linear Threshold activation
rule, its influence function𝜎 𝑀+(𝑆)is monotone and submodular (Kempe et al. 2003). As such,𝜎 𝑀+ admits
a(1−1/𝑒)approximation guarantee via greedy maximization.
5.2.2. Sandwich Approximation FormulationWe now formalize the sandwich approximation strat-
egy. Let𝜎 LT denote the influence function under the classical Linear Threshold model,𝜎 PT under the
Pressure Threshold model, and𝜎 𝑀+ under the static maximum-pressure model. For any seed set𝑆⊆𝑉,
these influence functions satisfy
𝜎LT(𝑆)≤𝜎 PT(𝑆)≤𝜎 𝑀+(𝑆).
Thus, PT diffusion is sandwiched between two monotone submodular processes that serve as tractable
lower and upper bounds.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
25
Since both𝜎 LT and𝜎 𝑀+ are monotone submodular, we may run the standard greedy algorithm on each to
obtain seed sets𝑆 LT and𝑆 𝑀+ with(1−1/𝑒)approximation guarantees. We additionally consider the seed
set𝑆 PT obtained by running greedy directly on𝜎 PT.
The sandwich strategy selects the final seed set as
𝑆sand =arg max 𝑆∈{𝑆 LT, 𝑆PT, 𝑆𝑀+} 𝜎PT(𝑆).
5.2.3. Approximation GuaranteeLet𝑆 ★ PT denote an optimal PT seed set. By standard sandwich argu-
ments (Lu et al. 2015), the selected seed set satisfies
𝜎PT(𝑆sand)≥(1−1/𝑒)·max
𝜎PT(𝑆 𝑀+)
𝜎𝑀+(𝑆 𝑀+),
𝜎LT(𝑆★ PT)
𝜎PT(𝑆★ PT)

·𝜎 PT(𝑆★ PT).
While the second term depends on the unknown optimum𝑆 ★ PT, the first term is fully computable. This
yields a practical, data-dependent approximation guarantee of
(1−1/𝑒)· 𝜎PT(𝑆 𝑀+) 𝜎𝑀+(𝑆 𝑀+),
which can be evaluated efficiently using Monte Carlo estimation of influence.
This framework demonstrates that even in the absence of classical structural guarantees, reinforcement-
aware diffusion models can still support principled and effective decision-making.
6. Computational Experiments
We now evaluate the implications of pressure-based reinforcement for diffusion dynamics and network-based
interventions. Our experiments are designed to address three central questions: (i) how reinforcement alters
seed selection in influence maximization, (ii) how it impacts realized diffusion outcomes across different
network structures, and (iii) how sensitive these effects are to the strength of social reinforcement.
Consistent with the decision-oriented perspective of this paper, our goal is not only to compare the Pressure
Threshold (PT) model with the Linear Threshold (LT) model, but also to understand how reinforcement
reshapes the effectiveness of intervention strategies in practice. We therefore emphasize both behavioral
differences in diffusion and their consequences for decision quality. In particular, our experiments are
designed to assess when accounting for reinforcement leads to meaningfully different intervention decisions
compared to classical diffusion assumptions.
Across all experiments, we follow a common methodology. We evaluate diffusion on a combination
of real-world and synthetic networks, use Monte Carlo simulation to estimate influence, and compare PT
against LT under matched conditions to isolate the effect of reinforcement. Unless otherwise stated, all results
reflect progressive diffusion processes and average outcomes across repeated simulations. All comparisons
are conducted under identical initial conditions to ensure that differences in outcomes are driven solely by
the presence of reinforcement.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
26
6.1. Network Data
We evaluate the Pressure Threshold (PT) model against the Linear Threshold (LT) model on four networks
spanning distinct topologies and application domains. Three of these are real-world networks drawn from
the Stanford Large Network Dataset Collection (SNAP) (Leskovec and Krevl 2014): (i) Facebook social
circles (Leskovec and Mcauley 2012), (ii) Wikipedia voting (Leskovec et al. 2010a,b), and (iii) Bitcoin OTC
trust (Kumar et al. 2016, 2018). To complement these datasets, we also include a synthetic Erd ˝os–R´enyi
random network𝐺(𝑛,𝑝)(Erd ˝os and R´enyi 1959).
These networks were selected to capture variation in structural properties that are expected to interact
with reinforcement, including density, clustering, and directionality of influence. These properties directly
influence the extent to which nodes are exposed to repeated influence, a key driver of amplification under
the PT model. In particular, denser networks provide more opportunities for repeated exposure and therefore
greater potential for amplification under PT.
Table 1 summarizes key statistics for each network, including the number of nodes, number of edges,
and edge-to-node ratio. This variation allows us to examine how the effects of reinforcement depend on
underlying network structure.
Network Nodes Edges Edge/Node Ratio
Facebook 4,039 88,234 21.846
Bitcoin 5,881 35,592 6.052
Wikipedia 7,115 103,689 14.573
Erd˝os–R´enyi 5,000 62,597 12.519
Table 1 Basic statistics of the networks used in experiments.
Graph construction and directionality.The four networks differ in how edges encode influence relation-
ships, and we standardize them to a unified directed framework consistent with threshold-based diffusion.
The Facebook social circles dataset is originally undirected, with an edge indicating mutual friendship.
Following standard practice in diffusion modeling (Kempe et al. 2003), we convert each undirected edge
{𝑢,𝑣}into two directed edges(𝑢,𝑣)and(𝑣,𝑢), preserving symmetric opportunities for influence.
The Bitcoin OTC trust and Wikipedia voting networks are inherently directed. In the Bitcoin network, an
edge(𝑢,𝑣)represents a trust rating assigned by user𝑢to user𝑣, while in the Wikipedia network, an edge
(𝑢,𝑣)indicates that user𝑢voted for user𝑣in an administrative election. These interpretations naturally align
with directed influence flow.
For the Erd ˝os–R´enyi network, we generate a random graph𝐺(𝑛,𝑝)with𝑛=5,000and𝑝=0.005, and
similarly convert each undirected edge into two directed edges. This provides a controlled baseline without
community structure, allowing us to isolate the role of network topology in shaping reinforcement effects.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
27
Edge weights and normalization.We adopt the weighted-cascade convention (Kempe et al. 2003), assign-
ing each directed edge(𝑢,𝑣)the weight
𝑤𝑢𝑣 = 1 in-degree(𝑣).
This normalization ensures that the total incoming influence to any node is bounded by one, i.e.,
˝
𝑢∈𝑁(𝑣) 𝑤𝑢𝑣≤1, which is consistent with the interpretation of thresholds as adoption constraints. This
normalization is particularly important under PT, as it ensures that reinforcement operates within a bounded
and interpretable range of influence.
Under the Pressure Threshold (PT) model, these baseline weights evolve endogenously through the
reinforcement mechanism described in Section 3. In particular, when a node activates, its outgoing influence
weights may increase as a function of the incoming pressure it experienced. All updates respect the cap
𝑤𝑢𝑣≤1, ensuring comparability with LT and interpretability of influence magnitudes.
Thresholds and stochasticity.In all experiments, node thresholds𝜃 𝑣 are drawn independently from the
uniform distribution on(0,1], following the standard assumption in threshold-based diffusion models. This
choice provides a neutral baseline that does not favor either early or late adoption and allows comparisons
across models to focus on differences in influence dynamics.
To ensure fair comparisons between PT and LT, we use matched randomness: for any given seed set
and trial, the same realization of thresholds is used under both models. This pairing isolates the impact of
reinforcement by controlling for stochastic variation in activation thresholds. As a result, differences between
PT and LT can be interpreted causally as arising from the reinforcement mechanism rather than stochastic
variation.
All reported influence values are computed as averages over independent Monte Carlo simulations. Unless
otherwise specified, each estimate is based on 1,000 trials, which provides stable estimates of expected
spread and allows consistent comparison across networks and parameter settings.
Interpretation for decision-making.This experimental design isolates the effect of reinforcement while
holding the underlying network structure and baseline influence assumptions fixed. As a result, differences
in observed diffusion outcomes can be attributed directly to the presence or absence of pressure-based
amplification.
For decision makers, this setup provides a direct analogue of intervention strategies designed under
static influence assumptions (LT) versus those that account for conviction and reinforcement (PT). The
experiments, therefore, provide insight not only into diffusion behavior but also into how modeling choices
affect the evaluation and selection of network interventions.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
28
6.2. Experimental Design
To understand how reinforcement affects both diffusion outcomes and intervention strategies, we organize
our empirical analysis around three complementary questions:
1.How does reinforcement alter seed selection?Do strategies optimized under PT select different
nodes compared to LT, and if so, how do these differences emerge?
2.How does reinforcement impact diffusion outcomes?For a given budget, how much additional
influence does PT generate relative to LT across networks with different structural properties?
3.How sensitive are outcomes to the strength of reinforcement?How does variation in the amplifica-
tion parameter𝛼affect the magnitude and stability of diffusion outcomes?
Together, these questions allow us to disentangle how reinforcement affects both the selection of inter-
vention targets and the realized impact of those interventions.
We design a set of experiments to isolate each of these questions while maintaining consistent assumptions
across models.
Seed selection under reinforcement.To examine how reinforcement reshapes intervention strategies, we
compare seed sets obtained under the PT and LT models on the Facebook network. Specifically, we solve
the influence maximization problem using the CELF algorithm (Leskovec et al. 2007) with a seed budget of
𝑘=20.
Influence is estimated using1,000Monte Carlo simulations per marginal gain evaluation. For PT, we set
𝛼=0.1, which empirically provides a regime in which reinforcement effects are visible but do not induce
immediate saturation. To ensure comparability, we use the same threshold realizations for both PT and LT
during seed selection.
Rather than focusing only on final influence values, we track the full sequence of node selections made by
CELF. This allows us to examine how reinforcement affects marginal gains over time and where divergences
between models emerge. In particular, it allows us to identify when reinforcement begins to alter marginal
contributions in ways that deviate from classical diminishing-returns intuition.
Influence as a function of budget.To quantify the impact of reinforcement on realized diffusion outcomes,
we evaluate influence as a function of the seed budget across all four networks. For each budget𝑘∈
{1,2,...,60}, we run CELF under three settings: LT, PT with𝛼=0.001, and PT with𝛼=0.005.
Each influence evaluation during the optimization process is computed using1,000Monte Carlo simu-
lations. The selected values of𝛼are chosen to illustrate meaningful deviations from LT without inducing
trivial full-network cascades, particularly in denser graphs.
This experiment allows us to characterize how reinforcement shifts the return on additional seeds and
how these effects depend on network topology.
Remark 2 (Robustness to threshold distributions).We evaluated alternative threshold distribu-
tions, including Normal(0.5,0.1)and Beta distributions with parameters(2,5)and(5,2). Across all cases,

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
29
the qualitative differences between PT and LT remained consistent. For brevity, we report results under the
standard uniform prior.
Sensitivity to the reinforcement parameter.To isolate the effect of reinforcement strength, we fix a seed set
size of𝑘=10on the Facebook network and vary the amplification parameter𝛼over the interval[10 −4,10−1]
using a fine grid.
For each value of𝛼, we estimate influence using1,000Monte Carlo simulations and report the average
cascade size. To reduce high-frequency variability due to stochastic thresholds, we apply a centered moving
average with a window of nine grid points.
This analysis provides a direct view of how amplification strength translates into incremental influence,
allowing us to assess whether reinforcement effects scale smoothly or exhibit threshold-like behavior.
6.3. Seed Selection under Reinforcement
We begin by examining how reinforcement alters the composition of optimal seed sets. Figure 3 and Table 2
compare the sequence of nodes selected by the CELF algorithm under the LT and PT models on the Facebook
network for a budget of𝑘=20.
Figure 3 CELF seed-selection timeline for the Facebook network (PT vs. LT,𝑘=20). Horizontal position shows the
selection step; vertical links mark common seeds. Early overlap is followed by divergence as PT accounts for
reinforcement effects.
Model Seeds selected (in order)
Linear Threshold 107, 351, 1821, 352, 0, 348, 1831, 349, 366, 1490, 1373, 1827, 2154,
1285, 838, 2806, 1149, 2130, 2403, 2088
Pressure Threshold 107, 351, 352, 1821, 0, 348, 1490, 1215, 1831, 1285, 1426, 1373,
2806, 366, 2403, 3234, 349, 2145, 1827, 2832
Table 2 Ordered seed sets returned by CELF for the Facebook network (𝑘=20).
The two models exhibit strong agreement in the early stages of the selection process. The first several
nodes selected under PT and LT largely coincide, indicating that nodes with strong intrinsic influence,

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
30
those capable of generating substantial spread independently, remain important even when reinforcement is
present.
However, meaningful divergence emerges in later selection steps. Beginning around iteration8, PT selects
nodes that do not appear in the LT seed set, while omitting several nodes that are included under LT. This
divergence reflects a fundamental shift in how marginal gains are evaluated under reinforcement.
Under the PT model, the marginal contribution of a node depends not only on its direct influence, but
also on the extent to which it enables amplification through its neighborhood. Nodes embedded in densely
connected regions are more likely to receive substantial incoming pressure before activation, which in turn
increases their outgoing influence after activation. As a result, PT tends to favor nodes that participate in
tightly knit local structures, where reinforcement can accumulate. This reflects the complementarity effects
identified in Section 4, where the value of a node depends on its interaction with previously selected seeds.
In contrast, the LT model evaluates nodes solely on static influence weights, without accounting for
downstream amplification. This leads to a preference for nodes with high immediate reach, even if their
neighborhoods do not support strong reinforcement effects.
Implications for intervention strategy.These results indicate that reinforcement can fundamentally alter
optimal seeding strategies. While high-degree or high-centrality nodes remain relevant, PT shifts emphasis
toward nodes that are positioned to benefit from coordinated activation and repeated exposure.
From a managerial perspective, this suggests that effective interventions in reinforcement-driven settings
should prioritize not just influential individuals, but also cohesive groups in which social pressure can
accumulate. Strategies based solely on static centrality measures may fail to identify nodes that are critical
for triggering amplification-driven cascades.
6.4. Influence as a Function of Budget
We next examine how reinforcement affects realized diffusion outcomes as a function of intervention budget.
Figures 4–7 plot the expected influence spread as the seed budget𝑘increases across the four networks under
both LT and PT.
Across all networks, the PT model produces consistently larger influence spreads than LT for the same
budget. This confirms that reinforcement increases the effectiveness of seeding interventions not merely by
accelerating diffusion, but by expanding the set of nodes that can ultimately be activated.
However, the magnitude of these gains varies substantially across networks, revealing an important
interaction between reinforcement and network structure. In the Facebook and Wikipedia networks, which
have relatively high edge-to-node ratios and pronounced clustering, PT yields significantly larger gains
over LT. In contrast, the Bitcoin network, which is much sparser and less clustered, exhibits only modest
improvements under PT.
This variation reflects the mechanism underlying pressure-based amplification. Reinforcement in the PT
model depends on nodes receiving sufficient cumulative influence prior to activation. Dense and clustered

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
31
0 10 20 30 40 50 60
0
1,000
2,000
3,000
Budget𝑘
Influence
Pressure Threshold (𝛼=0.005)
Pressure Threshold (𝛼=0.001)
Linear Threshold (𝛼=0)
Figure 4 Influence vs. budget for the Facebook
network.
0 10 20 30 40 50 60
0
2,000
4,000
6,000
Budget𝑘
Influence
Pressure Threshold (𝛼=0.005)
Pressure Threshold (𝛼=0.001)
Linear Threshold (𝛼=0)
Figure 5 Influence vs. budget for the Wikipedia
network.
0 10 20 30 40 50 60
0
1,000
2,000
3,000
4,000
5,000
Budget𝑘
Influence
Pressure Threshold (𝛼=0.005)
Pressure Threshold (𝛼=0.001)
Linear Threshold (𝛼=0)
Figure 6 Influence vs. budget for the Bitcoin
network.
0 10 20 30 40 50 60
0
1,000
2,000
3,000
4,000
5,000
Budget𝑘
Influence
Pressure Threshold (𝛼=0.005)
Pressure Threshold (𝛼=0.001)
Linear Threshold (𝛼=0)
Figure 7 Influence vs. budget for the Erd ˝os–R´enyi
network.
networks provide multiple pathways for influence to accumulate, increasing the likelihood that nodes activate
under high pressure and subsequently amplify their outgoing influence. In sparse networks, opportunities
for such accumulation are limited, reducing the scope for reinforcement to affect diffusion.
The Erd˝os–R´enyi network provides a useful intermediate benchmark. Although random, its edge density
enables reinforcement effects to accumulate more readily than in the Bitcoin network, leading to faster growth
in influence under PT. In this setting, we observe that PT can reach full network activation at relatively low
budgets compared to LT, illustrating how amplification can accelerate saturation in sufficiently connected
graphs.
Shape of diffusion curves.Despite these differences in scale, the qualitative shapes of the influence curves
remain similar across models. Both LT and PT exhibit diminishing returns as the budget increases, with
early seeds generating larger marginal gains than later ones even in the absence of global submodularity

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
32
0 2·10 −2 4·10 −2 6·10 −2 8·10 −2 0.1
0
1,000
2,000
3,000
4,000
𝛼
Influence
Pressure Threshold Model
Figure 8 Effect of the reinforcement parameter𝛼on influence spread (Facebook network,𝑘=10). Values are
smoothed using a centered moving average (window size 9).
under the PT model. This suggests that while reinforcement alters the magnitude of diffusion, it does not
fundamentally eliminate saturation effects arising from overlapping neighborhoods and limited remaining
reachable nodes.
At the same time, PT shifts the entire influence curve upward, effectively increasing the return on each seed
within the regime where diffusion has not yet saturated. This upward shift is not uniform across networks,
but is largest in those where structural conditions enable repeated exposure and reinforcement.
Implications for intervention design.These results highlight that the value of modeling reinforcement
depends critically on network structure. In dense, highly connected environments such as online social
platforms or tightly knit communities, ignoring reinforcement can lead to substantial underestimation of
achievable influence and misallocation of seeding resources.
Conversely, in sparse or weakly connected networks, the incremental benefit of accounting for reinforce-
ment may be limited, suggesting that simpler models such as LT may suffice for decision-making.
Overall, the results indicate that the effectiveness of influence interventions under PT is mediated by
the interaction between seeding strategies and endogenous amplification, emphasizing the importance of
aligning diffusion models with the structural characteristics of the target network.
6.5. Sensitivity to Reinforcement Strength
We finally examine how the strength of social reinforcement affects diffusion outcomes. Figure 8 plots
the expected influence spread under the PT model as a function of the amplification parameter𝛼for the
Facebook network with a fixed seed budget of𝑘=10.
As expected, influence spread increases with the level of reinforcement. When𝛼=0, the PT model
reduces to the Linear Threshold model, yielding the baseline level of diffusion. As𝛼increases, nodes that
activate under social pressure exert greater downstream influence, leading to larger cascades. This effect

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
33
arises because higher amplification increases the likelihood that nodes activate under sufficient pressure to
trigger further reinforcement downstream.
The relationship between𝛼and influence, however, is not purely linear. At low values of𝛼, increases
in reinforcement produce gradual improvements in spread, reflecting incremental amplification of local
influence. In an intermediate regime, the marginal impact of𝛼becomes more pronounced, as reinforcement
begins to systematically enable additional nodes to cross their activation thresholds. At higher values of
𝛼, the curve begins to flatten, indicating diminishing returns to additional amplification as the network
approaches saturation.
These regimes illustrate how the effect of reinforcement depends both on its magnitude and on the
underlying network structure. When amplification is weak, diffusion remains close to the LT baseline. When
amplification is moderate, reinforcement meaningfully expands the reachable portion of the network. Beyond
a certain point, further increases in𝛼primarily accelerate diffusion rather than expand its eventual reach.
Interpretation for model calibration.From a modeling perspective, these results highlight the importance
of calibrating𝛼to empirical data. Extremely small values may fail to capture observed reinforcement
effects, while excessively large values may overstate amplification and lead to unrealistically fast or saturated
cascades.
In practical settings,𝛼can be interpreted as a behavioral sensitivity parameter governing how strongly
individuals internalize social pressure. Estimating this parameter from observed cascade data, as explored
in Section 8, is therefore critical for accurate prediction and reliable decision support.
Implications for intervention design.For decision makers, the results suggest that the impact of
reinforcement-aware strategies depends on the regime in which the system operates. In environments with
moderate reinforcement, accounting for amplification can substantially increase the effectiveness of seeding
interventions. In contrast, when reinforcement is either negligible or already saturated, the incremental
benefit of adjusting strategies may be limited.
Overall, this analysis shows that reinforcement is not simply a binary feature of diffusion, but a tunable
mechanism whose strength shapes both the scale and efficiency of influence propagation. More broadly,
these findings highlight that reinforcement is not merely an incremental extension of classical diffusion but
a mechanism that reshapes both the scale and structure of influence propagation, with direct implications
for intervention design.
7. Empirical Evaluation of Approximation Guarantees
While Section 5 establishes theoretical bounds for influence maximization under the Pressure Threshold
(PT) model, it is important to understand how these guarantees translate into practice. In this section,
we empirically evaluate the sandwich approximation strategy on a real-world network and quantify the
resulting data-dependent performance guarantees. In particular, we assess whether the theoretical relaxation

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
34
introduced by the sandwich framework leads to practically useful guarantees when applied to realistic
network structures.
7.1. Experimental Setup
To assess the effectiveness of the sandwich approximation framework, we conduct experiments on a high-
activity subgraph derived from the Higgs Twitter dataset. This subgraph captures realistic structural prop-
erties while remaining computationally tractable for detailed analysis. The resulting graph contains1,198
nodes and1,319edges, with an edge-to-node ratio of1.101.
We set the amplification parameter to𝛼=0.5, representing a regime with substantial reinforcement,
and fix the seed budget at𝑘=5. This choice places the system in a high-reinforcement regime where the
gap between PT and its submodular surrogates is most pronounced. For each model, Linear Threshold
(LT), Pressure Threshold (PT), and the upper-bound model (𝑀+), we apply the CELF algorithm to obtain
corresponding seed sets𝑆 𝐿𝑇 ,𝑆 𝑃𝑇 , and𝑆 𝑀+.
Each influence estimate is computed using1,000Monte Carlo simulations with independently sampled
thresholds. Following the sandwich approximation procedure, we evaluate all candidate seed sets under the
PT model and select the seed set that achieves the largest expected influence.
7.2. Results
Model Seeds selected (in order) Expected Spread under PT
LT 64911, 103447, 28951, 35729, 112673 245.493
PT 35729, 112673, 142899, 232429, 339158 258.912
𝑀+ 1276, 112673, 142899, 232429, 339158 231.674
Table 3 Seed sets obtained under LT, PT, and𝑀 + along with their expected influence under PT (𝑘=5,𝛼=0.5).
The relative ordering of seed sets reflects the differing objectives optimized under each model, with PT
capturing reinforcement-aware interactions that are absent in LT and𝑀+.
Table 3 reports the seed sets obtained under each model and their corresponding influence evaluated under
PT. Among the candidate sets, the PT-derived seed set𝑆 𝑃𝑇 achieves the highest expected spread, and is
therefore selected as the final solution𝑆 sand.
While this selection reflects empirical performance, the sandwich framework also enables a formal
approximation guarantee through the upper-bound model𝑀 +. Specifically, we compute the ratio between
the PT and𝑀 + influence values for the seed set𝑆 𝑀+:
𝜎𝑃𝑇(𝑆 𝑀+)
𝜎𝑀+(𝑆 𝑀+) = 231.67 260.00≈0.891.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
35
This ratio serves as a data-dependent relaxation factor. Intuitively, it measures how tightly the upper-bound
model𝑀 + approximates PT for its own optimized seed set. Combining this with the classical(1−1/𝑒)
guarantee for submodular maximization yields the bound:
𝜎𝑃𝑇(𝑆sand)≥0.891·(1−1/𝑒)·𝜎 𝑃𝑇(𝑆∗ 𝑃𝑇)≈0.563·𝜎 𝑃𝑇(𝑆∗ 𝑃𝑇).
This guarantee holds without requiring monotonicity or submodularity of the PT influence function.
Interpretation.This result demonstrates that, despite the loss of monotonicity and submodularity, the
sandwich approximation strategy yields strong performance guarantees in practice. The achieved bound
of56.3%of the optimal influence is close to the classical63.2%guarantee for submodular influence
maximization, indicating that the practical loss from reinforcement-induced non-submodularity is limited
in this instance. From a decision-making perspective, this suggests that reinforcement-aware strategies can
be deployed with performance guarantees that remain close to classical benchmarks.
More broadly, these findings suggest that worst-case theoretical limitations may overstate the practical
difficulty of influence maximization under reinforcement. By combining tractable surrogate models with
data-driven evaluation, the sandwich framework provides a principled and implementable approach for
optimizing interventions in reinforcement-driven diffusion settings.
This empirical evaluation of the sandwich framework bridges the gap between theoretical guarantees
and practical applicability, demonstrating that reinforcement-aware optimization can be both principled and
effective in real-world settings.
8. Empirical Validation
While the previous sections evaluate the behavioral and algorithmic implications of reinforcement, we
now assess whether the Pressure Threshold (PT) model provides a more accurate description of real-
world diffusion. To this end, we compare PT and the Linear Threshold (LT) model against observed social
media cascades and evaluate their predictive performance. This comparison allows us to assess whether
incorporating reinforcement leads to systematically improved alignment between modeled and observed
diffusion.
8.1. Data and Experimental Setup
We conduct our analysis on the Higgs Twitter dataset (De Domenico et al. 2013), which captures information
diffusion surrounding the announcement of the Higgs boson discovery in July 2012. The dataset includes
multiple interaction networks: retweets, replies, mentions, and follower relationships, and provides precise
timestamps that allow for temporal validation of diffusion models.
We focus on the retweet network, where a user is considered active once they retweet a message. For
each experiment, we extract a cascade by selecting a seed node and collecting all users activated through
subsequent retweets. This produces a sequence of real-world activations over time.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
36
To ensure that models are evaluated conservatively, we augment each cascade subgraph by adding 500
neighboring nodes from the global follower network that were not part of the observed cascade. This
penalizes models that over-predict diffusion and ensures that predictive accuracy reflects both under- and
over-estimation.
We construct 100 such subgraphs, each representing a distinct cascade. For each subgraph, we record
structural properties including density, clustering, and seed centrality, to support the interpretation of model
performance across different network environments. These variations allow us to examine whether rein-
forcement improves predictive accuracy uniformly or primarily in structurally dense and highly interactive
settings.
8.2. Simulation Protocol
For each cascade subgraph, we simulate diffusion under both PT and LT using the observed seed node as
the initial activation. Edge weights and thresholds follow the same conventions used in earlier sections.
To align model dynamics with real-world timing, we discretize time such that one simulation step
corresponds to 10 hours of real-world activity. For each model and parameter setting, we estimate expected
influence trajectories using1,000independent Monte Carlo simulations. This ensures that differences in
predictive performance reflect model structure rather than sampling variability.
To evaluate the role of reinforcement strength, we vary the amplification parameter over the range
𝛼∈[0,1.5]with step size0.05. For each value of𝛼, we compute the prediction error across all sampled
cascades. This enables identification of the reinforcement regime that best aligns with observed diffusion
behavior.
8.3. Evaluation Metrics
We measure predictive accuracy using the Normalized Mean Squared Error (NMSE) over time. For a cascade
with𝑁nodes, the loss at time𝑡is given by:
NMSE(𝑡)=
𝜎Actual(𝑡Actual)−E[𝜎 Predicted(𝑡)]
𝑁
2
.
This normalization facilitates comparison across cascades of different sizes.
Here,𝜎 Actual denotes the cumulative number of activated nodes observed in the real cascade, and
E[𝜎Predicted(𝑡)]is the expected number of activations in the simulated diffusion process.
We report the final prediction error averaged across all cascades for each value of𝛼.
8.4. Results
Figure 9 compares predicted and observed activation trajectories for representative cascades. The PT model
consistently tracks the empirical diffusion curve more closely than LT, particularly in later stages of the
cascade. This improvement is consistent with PT’s ability to capture amplification arising from repeated

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
37
0 5 10 15 20
100
101
102
Time𝑡
Influence Pressure Threshold (𝛼=0.5)
Pressure Threshold (𝛼=0.2)
Linear Threshold (𝛼=0)
Empirical Data
0 5 10 15 20
100
101
102
Time𝑡
Influence Pressure Threshold (𝛼=0.5)
Pressure Threshold (𝛼=0.2)
Linear Threshold (𝛼=0)
Empirical Data
Figure 9 Predicted and observed influence over time for representative cascades.
0 0.2 0.4 0.6 0.8 1 1.2 1.4
0
0.2
0.4
0.6
0.8
Alpha𝛼
Loss
Figure 10 Average final NMSE as a function of the reinforcement parameter𝛼.
exposure over time. In contrast, LT systematically underestimates cascade growth due to its inability to
capture amplification arising from repeated exposure.
Figure 10 plots the average prediction error across cascades as a function of𝛼. When𝛼=0, the PT model
reduces to LT and exhibits the same level of error. As𝛼increases, prediction accuracy improves significantly,
indicating that reinforcement plays an important role in explaining observed diffusion behavior. Importantly,
accuracy improves monotonically only up to a point, after which additional amplification yields diminishing
predictive returns.
The error curve stabilizes for larger values of𝛼, suggesting diminishing returns from additional amplifi-
cation and identifying a regime in which the model is well calibrated to the data.
Interpretation.These results provide strong empirical support for the relevance of pressure-based rein-
forcement in real-world diffusion. By allowing influence strength to depend on social pressure at activation,
the PT model captures dynamics that are not explained by static threshold models.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
38
From a modeling perspective, the findings highlight the importance of incorporating reinforcement effects
when analyzing diffusion in settings characterized by repeated exposure and social validation. From a
decision-making perspective, improved predictive accuracy translates directly into better-informed interven-
tion strategies, particularly in high-activity social systems where amplification is prominent.
These improvements in predictive accuracy directly enhance the reliability of reinforcement-aware inter-
vention strategies derived from the PT model.
9. Managerial and Societal Implications
Our findings have direct implications for organizations and policymakers that rely on network-based inter-
ventions. In many real-world settings, such as marketing campaigns, political communication, and online
information diffusion, individual behavior is shaped not only by exposure but also by the intensity and
consistency of social reinforcement. The Pressure Threshold (PT) model provides a framework for incorpo-
rating this mechanism into both prediction and decision-making. In particular, it highlights how accounting
for reinforcement can lead to systematically different intervention strategies compared to classical diffusion
models.
Implications for intervention design.A central insight of our analysis is that reinforcement fundamentally
alters which individuals should be targeted in influence campaigns. While traditional strategies emphasize
high-degree or high-centrality nodes, our results show that under reinforcement, optimal interventions
prioritize nodes embedded in structurally cohesive regions of the network. These regions enable repeated
exposure, increasing the likelihood of high-pressure activation and subsequent amplification. This behavior
directly reflects the complementarity effects identified in Section 4.
For practitioners, this implies that effective interventions should balance reach with reinforcement poten-
tial. Rather than focusing solely on globally influential individuals, it may be more effective to target clusters
or communities where coordinated activation can generate compounding effects. This shift has implications
for marketing strategies, viral content design, and grassroots mobilization efforts. In practice, this may
require coordinated targeting strategies rather than isolated seeding decisions.
Implications for resource allocation.Our experiments demonstrate that the benefits of accounting for
reinforcement depend strongly on network structure. In dense and highly clustered networks, reinforcement
substantially increases diffusion outcomes, suggesting that more sophisticated models such as PT can
significantly improve the return on investment for seeding strategies. In contrast, in sparse or weakly
connected networks, the gains from reinforcement are more limited, and simpler models such as LT may
suffice.
This suggests a context-dependent approach to model selection: organizations should evaluate the struc-
tural properties of the target network before committing to more complex intervention strategies. In environ-
ments where repeated exposure is common, neglecting reinforcement may lead to systematic underestimation
of achievable influence.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
39
Implications for platform design and governance.Beyond strategic interventions, our results also shed
light on broader societal dynamics. Reinforcement mechanisms contribute to phenomena such as echo
chambers, rapid information cascades, and the amplification of misinformation. By capturing how local
pressure translates into increased influence, the PT model provides a tool for analyzing how platform design
choices, such as recommendation algorithms or content exposure patterns, can shape aggregate diffusion
outcomes by influencing both exposure patterns and the accumulation of social pressure.
From a policy perspective, incorporating reinforcement into diffusion models enables more realistic
evaluation of interventions aimed at promoting beneficial behaviors or mitigating harmful ones. This includes
applications in public health campaigns, information integrity efforts, and the regulation of online platforms.
Summary.Overall, our results highlight that influence in social networks is not solely a function of
exposure, but also of reinforcement-driven conviction. Accounting for this mechanism can improve both
the effectiveness of targeted interventions and the accuracy of system-level predictions in networked envi-
ronments. This perspective provides a unifying lens for understanding how local interactions scale into
system-level diffusion outcomes.
10. Conclusion
10.1. Summary of Contributions
This paper studies how social reinforcement shapes diffusion dynamics and the design of network-based
interventions. We introduced the Pressure Threshold (PT) model, a diffusion framework that extends the
Linear Threshold (LT) model by allowing a node’s outgoing influence to depend on the social pressure that
triggered its activation. This mechanism captures the formation of conviction under peer influence and the
resulting amplification of downstream persuasion.
We show that incorporating reinforcement fundamentally alters the structure of influence maximization.
While the problem remains NP-hard, the PT influence function is neither monotone nor submodular when
𝛼>0, implying that classical approximation guarantees do not directly apply. This highlights a fundamental
shift from separable to interaction-driven optimization. To address this challenge, we develop a sandwich
approximation framework that bounds the PT objective between tractable submodular surrogates, enabling
greedy algorithms with data-dependent performance guarantees.
Our computational experiments demonstrate that reinforcement yields qualitatively different seeding
strategies and substantially larger diffusion outcomes relative to LT. In particular, we show that PT favors
nodes embedded in structurally cohesive regions, where repeated exposure enables amplification, rather
than simply high-degree or high-centrality nodes. We further show that the benefits of reinforcement depend
strongly on network structure, with significantly larger gains in dense and highly clustered networks and more
modest improvements in sparse settings. These findings consistently illustrate the behavioral and structural
consequences of reinforcement across both synthetic and real-world settings.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
40
We complement these findings with an empirical evaluation of the sandwich approximation strategy,
demonstrating that strong data-dependent guarantees can be achieved in practice despite the loss of classical
structure. On a real-world network, the resulting solution achieves a guarantee of56%of the optimal
influence, approaching the performance levels associated with submodular objectives.
Finally, using time-stamped diffusion traces from the Higgs dataset, we provide empirical validation
that the PT model improves predictive accuracy relative to LT. These results confirm that pressure-based
amplification is not only a theoretical construct but also a practically relevant mechanism for modeling
real-world diffusion with measurable impact on both predictive accuracy and intervention effectiveness.
10.2. Future Research
Several directions for future research emerge from this work. On the theoretical side, an important question
is to characterize regimes in which the PT influence function exhibits approximate monotonicity or submod-
ularity, enabling stronger guarantees for greedy optimization. Identifying structural or parameter-dependent
conditions under which classical approximation guarantees can be recovered remains an open challenge.
Such characterization would clarify when reinforcement preserves enough structure to support efficient
optimization.
On the empirical side, estimating the reinforcement parameter𝛼from large-scale diffusion data is a key
direction. Such calibration would enable the PT model to serve as a predictive tool tailored to specific
domains and platforms and would enable reinforcement-aware models to be deployed as predictive tools
in operational settings. Extending the model to incorporate heterogeneous sensitivity to social pressure,
temporal dynamics, or evolving network structure also represents a promising avenue for future work.
Overall, our results highlight that influence in social networks is not only a function of exposure, but also of
conviction formed through reinforcement. Accounting for this mechanism is essential for both understanding
and effectively shaping diffusion in modern networked systems.
Ethical Statement
The Pressure Threshold (PT) model provides a framework for understanding and optimizing information
diffusion in social networks. However, such methods also have the potential for misuse in influence operations,
targeted persuasion, or the amplification of misinformation.
We therefore emphasize the dual-use nature of reinforcement-aware diffusion models. When applied
in real-world settings, particularly in public communication, marketing, or platform design, intervention
strategies based on amplification and seed selection should be evaluated carefully for unintended conse-
quences, including manipulation, polarization, and inequitable impact across user groups. Mechanisms for
transparency, auditing, and fairness-aware design are important safeguards for responsible deployment.
All data used in this study are publicly available and anonymized. No personally identifiable information
was collected or processed.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
41
We encourage future work to develop reinforcement-aware diffusion models that incorporate fairness,
accountability, and transparency by design.
Acknowledgments
A preliminary version of this paper appeared at the 20th International AAAI Conference on Web and
Social Media (ICWSM), 2026, held in Los Angeles, CA (Stutsman et al. 2026). The present manuscript
substantially extends and revises that earlier version.
References
Agarwal M, Aggarwal V, Umrawal AK, Quinn CJ (2022) Stochastic top k-subset bandits with linear space and non-
linear feedback with applications to social influence maximization.ACM/IMS Transactions on Data Science
(TDS)2(4):1–39.
Ananthasubramaniam A, Zhu Y, Jurgens D, Romero D (2024) The role of network and identity in the diffusion of
hashtags.arXiv preprint arXiv:2407.12771.
Aral S (2020)The Hype Machine: How Social Media Disrupts Our Elections, Our Economy, and Our Health—and
How We Must Adapt(Currency).
Aral S, Dellarocas C, Godes D (2013) Social media and business transformation: A framework for research.Information
Systems Research24(1):3–13, URLhttp://dx.doi.org/10.1287/isre.1120.0470.
Aral S, Walker D (2012) Identifying influential and susceptible members of social networks.Science337(6092):337–
341, URLhttp://dx.doi.org/10.1126/science.1215842.
Bass FM (1969) A new product growth model for consumer durables.Management Science15(5):215–227.
Becker R, D’ Angelo G, Ghobadi S, Gilbert H (2022) Fairness in influence maximization through randomization.Journal
of Artificial Intelligence Research73:1251–1283, URLhttp://dx.doi.org/10.1613/JAIR.1.13367.
Bhimaraju A, Robson EW, Varshney LR, Umrawal AK (2024) Fractional budget allocation for influence maximization
under general marketing strategies.Proceedings of 33rd ACM International Conference on Information and
Knowledge Management, 3627–3631.
Borgs C, Brautbar M, Chayes J, Lucier B (2014) Maximizing social influence in nearly optimal time.Proceedings of
Twenty-fifth Annual ACM-SIAM Symp. on Discrete algorithms, 946–957 (SIAM).
Chen W, Wang Y, Yang S (2009) Efficient influence maximization in social networks.Proceedings of the 15th
ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 199–208 (Association for
Computing Machinery), ISBN 9781605584959.
Chen W, Wu R, Yu Z (2020) Scalable lattice influence maximization.IEEE Transactions on Computational Social
Systems7(4):956–970.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
42
Cinelli M, De Francisci Morales G, Galeazzi A, Quattrociocchi W, Starnini M (2021) The echo chamber effect on social
media.Proceedings of the National Academy of Sciences118(9):e2023301118, URLhttps://www.pnas.org/
doi/10.1073/pnas.2023301118.
De Domenico M, Lima A, Mougel PO, Musolesi M (2013) The anatomy of a scientific rumor.Scientific Reports
3(1):2980, URLhttp://dx.doi.org/10.1038/srep02980.
Domingos P, Richardson M (2001) Mining the network value of customers.Proceedings of Seventh ACM SIGKDD
International Conference on Knowledge Discovery and Data Mining, 57–66 (ACM).
Erd˝os P, R´enyi A (1959) On random graphs i.Publicationes Mathematicae Debrecen6(290-297):18.
Goldenberg J, Libai B, Muller E (2001) Talk network: A complex systems look at the underlying process of word-of-
mouth.Marketing letters12(3):211–223.
Goyal A, Lu W, Lakshmanan LV (2011) Celf++: optimizing the greedy algorithm for influence maximization in social
networks. 47–48, WWW ’11 (Association for Computing Machinery), ISBN 9781450306379.
Granovetter M (1978) Threshold models of collective behavior.American Journal of Sociology83(6):1420–1443.
Kanuri VK, Chen Y, Sridhar S (2018) Scheduling content on social media: Theory, evidence, and application.Journal
of Marketing82(6):89–108.
Kempe D, Kleinberg J, Tardos ´E (2003) Maximizing the spread of influence through a social network.Proceedings of
9th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 137–146 (ACM).
Kermack WO, McKendrick AG (1927) A contribution to the mathematical theory of epidemics.Proceedings of the
Royal Society of London. Series A, Containing Papers of a Mathematical and Physical Character115(772):700–
721, ISSN 09501207.
Kumar S, Hooi B, Makhija D, Kumar M, Faloutsos C, Subrahmanian V (2018) Rev2: Fraudulent user prediction
in rating platforms.Proceedings of Eleventh ACM International Conference on Web Search and Data Mining,
333–341 (ACM).
Kumar S, Mallik A, Khetarpal A, Panda B (2022) Influence maximization in social networks using graph embedding
and graph neural network.Information Sciences607:1617–1636, ISSN 0020-0255, URLhttp://dx.doi.org/
https://doi.org/10.1016/j.ins.2022.06.075.
Kumar S, Spezzano F, Subrahmanian V, Faloutsos C (2016) Edge weight prediction in weighted signed networks.Data
Mining (ICDM), 2016 IEEE 16th International Conference on, 221–230 (IEEE).
Kuo TT, Hung SC, Lin WS, de Lin S, Peng TC, Shih CC (2011) Assessing the quality of diffusion models using
real-world social network data.2011 International Conference on Technologies and Applications of Artificial
Intelligence200–205.
Leskovec J, Huttenlocher D, Kleinberg J (2010a) Predicting positive and negative links in online social networks.
Proceedings of 19th International Conference WWW, 641–650.
Leskovec J, Huttenlocher D, Kleinberg J (2010b) Signed networks in social media.Proceedings of SIGCHI Conference
on Human Factors in Computing Systems, 1361–1370.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
43
Leskovec J, Krause A, Guestrin C, Faloutsos C, VanBriesen J, Glance N (2007) Cost-effective outbreak detection
in networks.Proceedings of 13th ACM SIGKDD International Conference on Knowledge Discovery and Data
Mining, 420–429.
Leskovec J, Krevl A (2014) SNAP Datasets: Stanford large network dataset collection.http://snap.stanford.
edu/data.
Leskovec J, Mcauley JJ (2012) Learning to discover social circles in ego networks.Advances in Neural Information
Processing Systems, 539–547.
Li Y, Gao H, Gao Y, Guo J, Wu W (2023) A survey on influence maximization: From an ml-based combinatorial
optimization.ACM Transactions on Knowledge Discovery from Data17(9):1–50.
Libai B, Muller E, Peres R (2013) Customer lifetime social value (clsv).Journal of Marketing77(6):139–153, URL
http://dx.doi.org/10.1509/jm.12.0460.
Lin M, Sun L, Yang R, Liu X, Wang Y, Li D, Li W, Lu S (2023) Fair influence maximization in large-scale social
networks based on attribute-aware reverse influence sampling.Journal of Artificial Intelligence Research76:925–
957, URLhttp://dx.doi.org/10.1613/JAIR.1.14450.
Lobel I, Sadler E, Varshney LR (2017) Customer referral incentives and social media.Management Science
63(10):3514–3529, URLhttp://dx.doi.org/10.1287/mnsc.2016.2504.
Lu W, Chen W, Lakshmanan LVS (2015) From competition to complementarity: comparative influence diffusion and
maximization.Proceedings of the VLDB Endowment9(2):60–71, ISSN 2150-8097, URLhttp://dx.doi.
org/10.14778/2850578.2850581.
Mallipeddi RR, Kumar S, Sriskandarajah C, Zhu Y (2022) A framework for analyzing influencer marketing in social
networks: selection and scheduling of influencers.Management Science68(1):75–104.
Mønsted B, Sapie˙ zy´nski P, Ferrara E, Lehmann S (2017) Evidence of complex contagion of information in social
media: An experiment using twitter bots.PLOS ONE12(9):e0184148, URLhttps://pmc.ncbi.nlm.nih.
gov/articles/PMC5609738/.
Nemhauser GL, Wolsey LA, Fisher ML (1978) An analysis of approximations for maximizing submodular set func-
tions—i.Mathematical Programming14(1):265–294.
Nguyen BNT, Pham PNH, Le VV, Sn´aˇsel V (2022) Influence maximization under fairness budget distribution in online
social networks.Mathematics10(22), ISSN 2227-7390, URLhttp://dx.doi.org/10.3390/math10224185.
Nie G, Agarwal M, Umrawal AK, Aggarwal V, Quinn CJ (2022) An explore-then-commit algorithm for submodular
maximization under full-bandit feedback.Uncertainty in Artificial Intelligence, 1541–1551 (PMLR).
Pan M, Blut M, Ghiassaleh A, Lee ZWY (2025) Influencer marketing effectiveness: A meta-analytic review.Journal of
the Academy of Marketing Science53:52–78, URLhttp://dx.doi.org/10.1007/s11747-024-01052-7.
Robson EW, Reddy D, Umrawal AK (2024) Cynetdiff: A python library for accelerated implementation of network
diffusion models.Proceedings of the VLDB Endowment17(12):4409–4412.

How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
44
Robson EW, Umrawal AK (2025) A community-aware framework for influence maximization with explicit accounting
for inter-community influence.arXiv preprint arXiv:2512.23973.
Rogers EM (2003)Diffusion of Innovations(Free Press), 5th edition.
Stutsman C, Robson EW, Umrawal AK (2026) A pressure-based diffusion model for influence maximization on social
networks.Proceedings of the International AAAI Conference on Web and Social Media, volume 20, 2238–2251.
Tang Y, Shi Y, Xiao X (2015) Influence maximization in near-linear time: A martingale approach.Proceedings of 2015
ACM SIGMOD International Conference on Management of Data, 1539–1554.
Umrawal AK, Aggarwal V (2023) Leveraging the community structure of a social network for maximizing the spread
of influence.ACM SIGMETRICS Performance Evaluation Review50(4):17–19.
Umrawal AK, Aggarwal V, Quinn CJ (2023a) Fractional budget allocation for influence maximization.2023 62nd
IEEE Conference on Decision and Control (CDC), 4327–4332 (IEEE).
Umrawal AK, Quinn CJ, Aggarwal V (2023b) A community-aware framework for social influence maximization.IEEE
Transactions on Emerging Topics in Computational Intelligence7(4):1253–1262.
Umrawal AK, Robson EW, Aggarwal V, Quinn CJ (2026) Maximizing the spread of influence through a social network
using partial incentives.Journal of Artificial Intelligence Research86, URLhttp://dx.doi.org/10.1613/
jair.1.20410.
Xie M, Yang Q, Wang Q, Cong G, Melo G (2015) Dynadiffuse: A dynamic diffusion model for continuous time
constrained influence maximization.Proceedings of the AAAI Conference on Artificial Intelligence29(1).
Xu J, Umrawal AK (2026) Lofa: Online influence maximization under full-bandit feedback using lazy forward selection.
arXiv preprint arXiv:2601.00933.
Zhuang H, Sun Y, Tang J, Zhang J, Sun X (2013) Influence maximization in dynamic social networks.2013 IEEE 13th
International Conference on Data Mining, 1313–1318, URLhttp://dx.doi.org/10.1109/ICDM.2013.145.
