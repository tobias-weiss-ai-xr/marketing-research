---
title: 'Algorithmic Collusion or Competition: the Role of Platforms'' Recommender Systems'
url: https://arxiv.org/abs/2309.14548
category: consumer-behavior
subcategory: empirical
date: 2023-09
venue: ''
authors:
- Xingchen Xu
- Stephanie Lee
- Yong Tan
source: arxiv
pdf_url: https://arxiv.org/pdf/2309.14548
pages: 54
chars: 134898
fetched_at: '2026-11-08T13:10:50+00:00'
kb_version: 1
---

# Algorithmic Collusion or Competition: the Role of Platforms' Recommender Systems

Algorithmic Collusion or Competition: the Role of
Platforms’ Recommender Systems
Xingchen (Cedric) Xu
Michael G. Foster School of Business, University of Washington, Seattle, W A 98195, xcxu21@uw.edu
Stephanie Lee
Michael G. Foster School of Business, University of Washington, Seattle, W A 98195, stelee@uw.edu
Yong Tan
Michael G. Foster School of Business, University of Washington, Seattle, W A 98195, ytan@uw.edu
Recent scholarly work has extensively examined the phenomenon of algorithmic collusion driven by AI-
enabled pricing algorithms. However, online platforms commonly deploy recommender systems that influence
how consumers discover and purchase products, thereby shaping the reward structures faced by pricing
algorithms and ultimately affecting competition dynamics and equilibrium outcomes. To address this gap
in the literature and elucidate the role of recommender systems, we propose a novel repeated game frame-
work that integrates several key components. We first develop a structural search model to characterize
consumers’ decision-making processes in response to varying recommendation sets. This model incorpo-
rates both observable and unobservable heterogeneity in utility and search cost functions, and is estimated
using real-world data. Building on the resulting consumer model, we formulate personalized recommendation
algorithms designed to maximize either platform revenue or consumer utility. We further introduce pricing
algorithms for sellers and integrate all these elements to facilitate comprehensive numerical experiments.
Our experimental findings reveal that a revenue-maximizing recommender system intensifies algorithmic
collusion, whereas a utility-maximizing recommender system encourages more competitive pricing behavior
among sellers. Intriguingly, and contrary to conventional insights from the industrial organization and choice
modeling literature, increasing the size of recommendation sets under a utility-maximizing regime does not
consistently enhance consumer utility. This counterintuitive “more is less” effect arises because expanding
the recommendation set reduces the recommender system’s ability to effectively influence the pricing strate-
gies of AI-driven algorithms through dynamic rewards. Moreover, the degree of horizontal differentiation
moderates this phenomenon in unexpected ways. The “more is less” effect does not arise at low levels of
differentiation, but becomes increasingly pronounced as horizontal differentiation increases. This is because,
in such contexts, consumers’ decisions are driven more by their inherent preferences than by price considera-
tions. As a result, when the recommendation set is large, higher-priced products experience relatively smaller
declines in their rewards and can sustain elevated prices, supported by the persistent demand engendered
by horizontal preferences. These findings provide valuable insights for regulators, platform designers, and
market participants, and they open up a range of promising avenues for future research.
Key words: algorithmic pricing; algorithmic collusion; repeated game; consumer search; structural
estimation; reinforcement learning; recommender systems; antitrust
1
arXiv:2309.14548v2  [cs.AI]  15 Dec 2024

Xu, Lee, and T an:Algorithmic Collusion or Competition
2 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
1. Introduction
1.1. Motivation and Research F ocus
With the advancement of technology and the proliferation of sophisticated machine learning algo-
rithms, the use of automated pricing systems has increased significantly across various sectors.
For instance, a substantial share (34%) of residential units in the United States currently uti-
lize RealPage software, which provides instantaneous recommendations for optimal rental rates
(Calder-Wang and Kim 2023). Artificial Intelligence (AI)-driven pricing programs, particularly
those employing reinforcement learning techniques, have thus emerged as compelling alternatives
to conventional pricing models (Spann et al. 2024). These AI-powered systems typically require
minimal human intervention and exhibit remarkable adaptability to rapidly changing economic
conditions.
However, both researchers and policymakers have voiced concerns about the potential detrimen-
tal effects of these algorithms on consumers, particularly regarding the phenomenon of algorithmic
collusion. Algorithmic collusion refers to the capacity of algorithms to establish supra-competitive
prices through repeated interactions (Calvano et al. 2020a). In traditional markets without AI-
based pricing, game theory suggests that supra-competitive prices occur when businesses collude to
set artificially elevated prices (Athey et al. 2004). Since each seller is incentivized to undercut these
agreed-upon prices, the sustainability of a supra-competitive price depends on (1) the cartel’s abil-
ity to effectively punish deviators and (2) each firm’s perception of other members’ reactions. In the
context of algorithmic collusion, however, these mechanisms are no longer required: sellers merely
set a revenue-optimizing objective, and the pricing algorithms can independently learn to charge
supra-competitive prices without direct communication or explicit instructions on how to collude.
In such scenarios, these prices often remain stable, with algorithms consistently maintaining higher
rates at the expense of consumers (Calvano et al. 2020a).
Given the increasing attention to this issue, related legislative bills and legal cases have begun
to emerge. For example, the “Preventing Algorithmic Collusion Act” was proposed in 2024 1, and
RealPage has been sued for employing pricing algorithms that potentially harmed millions of
renters2. In parallel, a growing body of literature has attempted to address this area. On the
empirical front, research has provided suggestive evidence that the adoption of pricing algorithms
correlates with increased price synchronization among firms and elevated prices (Calder-Wang and
Kim 2023, Wieting and Sapi 2021, Assad et al. 2020). In order to better understand the underlying
mechanisms, numerical experimental approaches have been employed since the seminal work of
Calvano et al. (2020b) (Dou et al. 2024, Rocher et al. 2023).
1 See https://www.congress.gov/bill/118th-congress/senate-bill/3686 for more details.
2 See https://www.cbsnews.com/news/realpage-lawsuit-price-fixing/ for more details.

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 3
In online marketplaces such as Amazon, pricing algorithms are also widely utilized Chen et al.
(2016). Nevertheless, despite existing scholarly efforts and regulatory interventions, the role of rec-
ommender systems—which are extensively used in online marketplaces—remains largely overlooked
in the context of algorithmic pricing games. Conceptually, recommender systems can alter product
exposure and thus influence the rewards obtained by pricing algorithms, ultimately shaping pric-
ing dynamics and welfare distributions. Recognizing this gap, we aim to address it by examining
how various recommendation algorithms affect pricing dynamics and equilibrium outcomes in the
algorithmic pricing game.
1.2. Research F ramework
To examine the algorithmic pricing game under the influence of recommender systems, it is essential
to develop a modified repeated game framework. Calvano et al. (2020b) provides a seminal founda-
tion for the study of algorithmic collusion, offering a framework that has been widely adopted and
adapted in subsequent research (Dou et al. 2024, Rocher et al. 2023, Banchio and Skrzypacz 2022).
Calvano et al. (2020b) specifies three key elements: (1) the consumer demand model, where con-
sumer decisions are governed by a canonical logit model; (2) the pricing algorithms, in which sellers
employ basic Q-learning algorithms to adaptively set prices; and (3) the game sequence, where
at each discrete period, sellers simultaneously make pricing decisions and observe the resulting
demand responses.
Given our research focus, we need to specify and integrate the recommender system as a fourth
element within the framework. Furthermore, it is also necessary to adjust the other three compo-
nents accordingly to ensure coherent integration, which presents certain challenges. In the presence
of recommender systems, a key challenge is to model consumer decision-making when consumers
are exposed to multiple recommended products simultaneously. Typically, consumers observe a
ranked list of top-K products and need to expend time and effort to evaluate the options of interest
(Moraga-Gonz´ alez et al. 2023, Mortensen 2011). Additionally, position biases may influence their
choices (Guo et al. 2019, Ursu 2018). To accurately capture these considerations and establish
a solid economic foundation, we develop a customized structural search model that incorporates
heterogeneous utility functions and search costs (Chung et al. 2024, Ursu et al. 2023). We then esti-
mate the model parameters using real-world data, employing an innovative combination of Hermite
approximation methods and simulated maximum likelihood estimation to reduce computational
complexity. The calibrated model subsequently generates demand responses within the repeated
game framework.
With this demand model in place, we also specify a recommender system that optimizes the
platform’s objective, such as overall revenue or consumer utility (Compiani et al. 2024, Wang

Xu, Lee, and T an:Algorithmic Collusion or Competition
4 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
et al. 2024, Zhang et al. 2024, Li and Tuzhilin 2024a). However, when the demand model is
grounded in a sophisticated framework such as sequential search, closed-form expressions for con-
sumer choice probabilities and optimal recommendations are generally unavailable. As a result, we
follow established optimization literature and employ numerical integration methods to identify
recommendation actions that maximize the specified objective function (Compiani et al. 2024).
For the pricing algorithm and game sequence, we adopt the Q-learning approach and the simul-
taneous game structure outlined by Calvano et al. (2020b). Nonetheless, Q-learning inherently
assumes forward-looking behavior, prompting us to examine an alternative in the form of a simpler
bandit algorithm to ensure robustness. Similarly, to further test the flexibility of our framework,
we also consider an asynchronous game sequence as an additional robustness check.
By integrating all of these elements, we can analyze the impact of recommender systems on
algorithmic pricing. However, even the original framework proposed by Calvano et al. (2020b)
poses significant analytical challenges. In a multi-agent environment, each agent’s setting is non-
stationary, rendering both the learning of strategies and the determination of equilibria analytically
intractable. Introducing a recommender system, alongside adjustments to the other model com-
ponents, further complicates the analysis. In particular, the absence of closed-form expressions for
consumer choice probabilities precludes straightforward derivation of sellers’ demands and revenues
given any set of prices and recommendations.
To address these complexities, we extend the approach of Calvano et al. (2020b), relying on
numerical simulations to trace the price evolution and identify equilibrium outcomes. In each
period, after sellers have set prices and the platform has determined recommendations, we use
the empirical distribution of consumer attributes and the calibrated consumer demand model
to compute each seller’s expected reward. This involves multiple layers of numerical integration.
Through this procedure, we can efficiently execute simulations and conduct counterfactual analyses
by altering any component within the proposed framework.
1.3. Findings
Employing the aforementioned setups, we adjust various parameters within the framework to eval-
uate how such changes influence price dynamics and equilibrium outcomes. Turning to our primary
focus—the recommender system—from an economic perspective, it optimizes the platform’s objec-
tive by selecting and potentially ranking a subset of products to display to consumers from the full
set of available options (Feldman et al. 2022).
Previous research on product display algorithms in two-sided markets predominantly consid-
ers two key objectives 3. The first, Revenue-Maximization, seeks to maximize total platform-wide
3 It is noteworthy that the technical literature on recommender systems primarily categorizes these systems based
on their underlying methodologies, such as classical collaborative filtering and deep learning techniques (Zhang et al.

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 5
revenue, thereby aligning with the platform’s economic incentives through commission fees. The
second, Utility-Maximization, aims to enhance consumer utility, which may indirectly benefit the
platform by improving consumer retention (Compiani et al. 2024, Feldman et al. 2022, Derakhshan
et al. 2022, Ursu 2018). Since different objectives can substantially alter product exposure and
consequently influence sellers’ learned strategies as well as price dynamics, we pose the following
research question:
RQ1: How does the objective of the recommender system affect the algorithmic pricing game?
We address this research question through numerical simulations based on our proposed frame-
work, which comprises the following components: a structural search model calibrated with empir-
ical data to generate demand responses; Q-learning algorithms to determine pricing decisions;
recommender systems designed to generate recommendation sets for each consumer in alignment
with the platform’s objectives; and a simultaneous game sequence that integrates the behaviors of
all participants within a repeated game context.
We conduct numerical simulations under two distinct recommender system objectives—revenue
maximization and utility maximization—and compare these results to a baseline scenario in which
product display is randomized. Our findings reveal that the objectives of recommender systems
significantly influence both pricing trajectories and the resulting price equilibrium. Specifically,
revenue-maximization recommender systems tend to exacerbate algorithmic collusion, leading to
elevated market prices. In contrast, utility-maximization systems yield non-collusive outcomes char-
acterized by lower equilibrium prices. Furthermore, we explore the impact of varying the relative
weights assigned to revenue and utility objectives on market outcomes. The results demonstrate
a monotonic relationship between these weights and the resulting prices, further reinforcing the
crucial role of recommender system objectives in shaping algorithmic pricing dynamics.
Beyond the objective of the recommender system, another significant factor it can predefine is
the number of products displayed. This dimension holds considerable economic importance, as it
directly influences search friction and thus the intensity of competition among sellers (Moraga-
Gonz´ alez et al. 2023, Hong and Shum 2006). Guided by the antitrust and algorithmic collusion
literature’s emphasis on enhancing consumer welfare (Baker 2019), one may naturally question
whether displaying more products can effectively achieve this goal. The underlying rationale is that,
with a wider range of product options, consumers can bypass items they deem less desirable and
choose those that offer higher utility. This reasoning is supported by the choice modeling literature,
which suggests that the welfare derived from a product set increases as more products are made
2019, Adomavicius and Tuzhilin 2005). Objectives (outcomes) are generally self-explanatory and thus receive limited
attention within this stream of literature. In contrast, our research emphasizes these objectives from an economic
perspective.

Xu, Lee, and T an:Algorithmic Collusion or Competition
6 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
available (Train 2009). To investigate whether this logic holds true when pricing algorithms are in
play, we pose our second research question:
RQ2: Does displaying more products when using the utility-maximization recommender system
always benefit consumers?
By running simulations with varying numbers of displayed products, we uncover a counterintu-
itive finding: under a utility-maximization objective, increasing the number of displayed products
can sometimes reduce consumer utility. This outcome emerges from two competing mechanisms.
On one hand, offering more products improves consumers’ chances of discovering those that yield
higher utility. On the other hand, expanding the set diminishes the platform’s leverage in influ-
encing prices through recommendations. Consequently, high-priced products retain exposure and
continue to attract some consumers, experiencing relatively smaller reductions in their rewards
and thus sustaining higher equilibrium prices. When this latter effect dominates, providing more
products ultimately harms consumer welfare.
Building on the previous rationale, horizontal differentiation emerges as another key factor influ-
encing the effects of increasing the number of displayed products. When products differ only
minimally, consumers tend to select the lowest-priced option, rendering additional offerings largely
inconsequential. On the contrary, greater horizontal differentiation may allow consumers to find
products that better match their preferences, thus potentially enhancing their utility through a
broader set of options. Given the importance of horizontal differentiation in price competition and
industrial organization research (Colombo 2013, Thomadsen and Rhee 2007, Tyagi 1999), we ask
our third research question:
RQ3: How does horizontal differentiation moderate the relationship between the number of
displayed products and consumer utility?
By adjusting the horizontal differentiation parameter and examining the impact of increasing
the number of displayed products, we uncover another counterintuitive moderation effect. When
horizontal differentiation is low, offering more product options benefits consumers by enabling them
to find preferred items. However, as horizontal differentiation increases, the “more is less” effect
emerges. While greater differentiation enhances the potential gains from searching among a broader
range of products to identify those closely aligned with consumer preferences, it also enables higher-
priced offerings to retain demand and maintain elevated prices. Consequently, at high levels of
horizontal differentiation, both mechanisms intensify, and the disadvantage of sustaining higher-
priced products may outweigh the potential utility gains derived from increased product variety.
Therefore, contrary to conventional intuition, providing more products may diminish consumer
utility under high horizontal differentiation, while enhancing it when horizontal differentiation is
low.

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 7
1.4. Summary of Contributions
Our work contributes methodologically, theoretically, and practically to the literature, with subse-
quent sections providing further details on each dimension.
From a methodological perspective, we incorporate recommender systems into a repeated game
framework and appropriately adjust other model components. In doing so, we address the esti-
mation of a complex structural search model by introducing the Hermite method into the simu-
lated maximum likelihood procedure. We also derive the sequence of the game and equilibrium
using multi-layer numerical integration, while relaxing several key assumptions from Calvano et al.
(2020b). The resulting framework offers a valuable foundation for future analyses of analogous
research questions.
From a theoretical perspective, we extend the algorithmic collusion literature by highlighting the
critical role of recommender systems, which alter product exposure and thus influence the rewards
that pricing algorithms receive. This interplay ultimately affects pricing dynamics and welfare out-
comes. Additionally, we enrich the economics of recommender systems literature by incorporating
adaptive, AI-based pricing rather than presupposing static or fully informed seller-driven pricing
strategies. In other words, we demonstrate that recommender systems can reshape economic out-
comes not only by shifting consumer behavior but also by altering the dynamic incentives that drive
pricing algorithms, thus affecting welfare distributions. Furthermore, this study contributes to the
broader economics of AI literature by taking a first step toward examining the aggregate economic
effects of cross-category AI-AI interactions—specifically, those between recommender systems and
multiple pricing algorithms—rather than treating each AI intervention in isolation.
From a practical perspective, our results yield important insights for regulators, platforms,
and sellers. For instance, when regulators attempt to mitigate supracompetitive pricing through
antitrust measures, focusing exclusively on the providers of pricing algorithms may prove insuf-
ficient. Platforms, such as Amazon, may need to refine their recommendation policies by jointly
considering consumer responses and the strategic behavior of pricing algorithms. Similarly, sellers
might benefit from coordinating product design and pricing algorithm strategies to account for the
platform’s evolving recommendation criteria.
In the subsequent sections, we first review the related literature and identify our theoretical
contributions to each research stream in Section 2. In Section 3, we present our repeated game
framework, detailing its components, the challenges addressed, and ourcontributions to frameworks
and models . Section 4 outlines our parameterization strategy, describes the empirical data, and
explains the estimation procedures employed to calibrate the structural search model. Building on
this foundation, we offer our findings through numerical simulations in Section 5, followed by a
series of extended analyses in Section 6 to test the robustness of these results. Finally, Section 7

Xu, Lee, and T an:Algorithmic Collusion or Competition
8 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
concludes by discussing the practical implications of our study and suggesting directions for future
research.
2. Related Literature
By incorporating recommender systems into the repeated pricing games among sellers that uti-
lize AI-driven pricing algorithms, our study contributes to the literature on the economics of AI,
algorithmic collusion, and the economics of recommender systems. In each subsection, we first
review the relevant literature and subsequently highlight our specific contributions to each research
stream.
2.1. Economics of AI
Broadly speaking, our study is situated within the domain of the economics of AI, wherein eco-
nomic principles are applied to evaluate, design, and implement AI techniques and architectures
(Agrawal et al. 2019). A growing body of literature examines the impact of various AI systems
across diverse contexts, such as AI assistants for customer response (Brynjolfsson et al. 2023),
matching algorithms in the gig economy (Liu et al. 2024), AI copilots in software development
(Peng et al. 2023), and AI applications in creative works (Boussioux et al. 2024, Gao and Wang
2024). These insights inform the design of future AI systems to be more responsible and ethical,
thereby enhancing overall welfare and promoting its equitable distribution (Maslej et al. 2023).
The focus of this work, AI-based pricing algorithms (particularly algorithmic collusion) and
recommender systems, represents two significant subfields within the economics of AI literature.
However, these areas are typically studied separately, resulting in distinct streams of research as
discussed in the subsequent two subsections (Calvano et al. 2020b, Fleder and Hosanagar 2009). By
jointly examining the economic impacts of recommender systems and pricing algorithms, we con-
tribute to the broader literature by investigating a unique phenomenon concerning the economics
of AI-AI interactions.
2.2. Algorithmic Collusion and Antitrust Regulation
More specifically, this study is related to and contributes to burgeoning research on algorithmic
collusion. With the prevalence of learning algorithms, scholars have investigated the impact of
AI-based pricing algorithms on market competition and price equilibrium, particularly since the
seminal work by Calvano et al. (2020b). Antitrust policymakers have also expressed concerns
regarding algorithmic collusion, which could consequently lead to adverse effects on consumer
welfare (Robertson 2022, Colangelo 2021, Fzrachi and Stucke 2019, Schwalbe 2018).
To describe and understand algorithmic collusion, some early works have employed theoretical
models to illustrate how simple pricing strategies can decipher competitors’ behavior and lead to

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 9
collusive outcomes (Mikl´ os-Thal and Tucker 2019, Salcedo 2015). However, as algorithms become
more sophisticated, these models become analytically intractable, thereby necessitating numerical
simulations within the repeated game framework (Calvano et al. 2020b). Subsequently, several
studies have explored algorithmic collusion in various market contexts, such as auctions (Banchio
and Skrzypacz 2022) and securities (Dou et al. 2024, Colliard et al. 2022). Additionally, certain
empirical evidence has been documented, supporting instances of correlated and elevated prices
among multiple vendors, although the underlying mechanisms are challenging to empirically verify
(Calder-Wang and Kim 2023, Wieting and Sapi 2021, Assad et al. 2020).
Although research on algorithmic collusion is active, it is noteworthy that existing studies on
collusion in algorithmic pricing have not thoroughly considered the influence of platform recommen-
dation systems, which directly impact product exposure and profitability in online marketplaces.
This study contributes to the algorithmic collusion literature by demonstrating that the platform’s
recommendation algorithm plays a pivotal role in shaping the competitive landscape of the market
and influencing the degree of collusion among sellers. Furthermore, the study offers an alternative
explanation for the observed correlated prices in empirical studies, suggesting that the platform’s
recommendation mechanism may drive this correlation. Consequently, for antitrust regulations
targeting supracompetitive prices in online markets with recommender systems, it may be more
equitable to attribute responsibilities to both platforms and sellers.
2.3. Economics of Recommender Systems
Our study is closely aligned with the literature on the economics of recommender systems, which
investigates the downstream impacts of these systems on various economically significant outcomes,
driven by the complexity of consumer behavior in real-world settings.
For instance, Fleder and Hosanagar (2009) examine how recommender systems influence both
individual-level and market-level sales diversity through analytical models and simulations. Build-
ing on this, Lee and Hosanagar (2019) empirically test the impact of recommender systems on
diversity using field experiments. More recently, Lee and Hosanagar (2021) documents the het-
erogeneity in the economic impact of recommender systems, while Li et al. (2022) explore the
causal pathways underlying these effects. In addition to studies that focus on the economic benefits
that recommendations provide to sellers and platforms, there is also research that considers con-
sumer welfare (Wan et al. 2024, Zhang et al. 2021) and examines the dynamic interactions between
consumer choices and recommender systems (Zhou et al. 2023).
However, a significant gap in the existing literature is that previous studies on recommender
systems have typically treated product pricing as an exogenous variable. Only a few exceptions
have analytically explored the effects of recommender systems on pricing decisions and market

Xu, Lee, and T an:Algorithmic Collusion or Competition
10 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
equilibrium. In these analyses, sellers are generally modeled as revenue-seeking agents, while the
platform may possess different incentives, such as revenue maximization or utility optimization
(Zhou and Zou 2023, Li et al. 2020, 2018). Nonetheless, these studies are predominantly static in
nature and assume that sellers possess complete market information (Zhou and Zou 2023, Li et al.
2020, 2018).
In this context, our study makes a novel contribution by allowing prices to be dynamically
determined by AI-driven pricing algorithms, which learn to set prices through interaction with
the market. We then investigate the economic impact of recommender systems on price dynamics,
sellers’ benefits, and consumer utility from a holistic perspective. This approach bridges the gap in
the literature by integrating the behavior of pricing algorithms with the economics of recommender
systems, thereby providing a more comprehensive understanding of their interplay in modern online
platforms.
3. Dynamic Pricing Competition Moderated by the Platform’s
Recommendation System
3.1. General Repeated Game F ramework
Despite its critical importance, the role of platform recommendations in shaping algorithmic pric-
ing strategies remains underexplored in the existing literature. Previous studies on algorithmic
collusion, largely following the framework established by Calvano et al. (2020b), typically include
a logit demand model, employ Q-learning as the pricing algorithm, and consider a simultaneous
game sequence. To more effectively address our research questions, we develop a novel repeated
game framework that incorporates the platform’s recommendation system and modifies these three
elements accordingly.
This section presents the overall structure of our repeated game model, specifies the sequence of
play, and provides a concise summary of the principal challenges encountered. In the subsections
that follow, we discuss each key element in detail: Section 3.2 introduces the demand model,
Section 3.3 details the pricing algorithm, and Section 3.4 outlines the platform’s recommendation
algorithm. For ease of reference, Table 1 compiles the central notations employed in this study.
Although additional symbols may emerge as we formally characterize and estimate the customer
demand model, we refrain from listing them here to preserve clarity.
Specifically, consider a marketplace comprising J heterogeneous products ( j ∈ {1, 2, . . . , J})4,
each associated with an attribute vector Xj, as well as an outside option ( j = 0). At each discrete
time period t, sellers independently and simultaneously set their prices pt j. Concurrently, a cohort
4 We assume a one-to-one mapping between sellers and products. If a seller offers multiple products with distinct
dynamic pricing strategies, each product can be treated as a separate seller.

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 11
Table 1 Summary of Notations for the Main Model
Notation Explanation
t Time period t
J The number of products available on the market
K The number of products shown to each consumer
j A product j (with j = 0 representing the outside option)
pt j The price of product j at period t
Xj The other attributes of product j which are stable across periods
Dt j Demand of product j at period t
πt j Revenue of product j at period t
i A Consumer i (the index is reordered every period to simplify the notation)
Ai The consumer i’s attributes
Bi A set of products shown to the consumer i
βi The consumer’s price sensitivity
Γ Other parameters linking product’ attributes to utility
Θ Other preference parameters linking consumer’s attributes to utility
posi,j Ranking (Position) of product j seen by consumer i
ci,j The search cost of product j for consumer i
τi The constant term of consumer i’s search cost
φ The ranking effect parameter of the search cost
ui,j The consumption utility of product j for consumer i
vi,j The expected pre-search utility of product j for consumer i
ξi,j The post-search utility shock of product j for consumer i
zi,j The reservation utility of product j for consumer i
µ The horizontal differentiation level on the market
St State of the system at the period t, which is the price vector at t − 1
Qj Product j’s pricing strategy (characterized by a Q matrix in Q-learning)
T Ut Total Consumer Utility at period t
T Dt Total Demand at period t
Πt Total Revenue at period t
rt j Product j’s reward at period t
mt Platform’s reward at period t
α Learning rate of the pricing algorithm
δ Discount rate of the pricing algorithm
ϵ Exploration rate of the pricing algorithm
ω Decay rate of exploration rate
of consumers, indexed by i and each characterized by an attribute vector Ai, enters the platform.
The platform then constructs a recommendation set Bi for each consumer and establishes product
rankings posi,j to optimize its own objective. Upon viewing these recommendations, each consumer
i undertakes a search process and ultimately purchases product k, yielding utility ui,k. As a result,
each seller realizes a reward rt j, enabling it to iteratively refine its pricing algorithm over time.
Meanwhile, the platform also accrues a reward mt. This cyclical process is summarized below in
Algorithm 1.
The repeated game process described above builds on the foundational work of Calvano et al.
(2020b), a benchmark study in the field of algorithmic collusion that has influenced numerous

Xu, Lee, and T an:Algorithmic Collusion or Competition
12 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
Algorithm 1 General Repeated Game Process
Require: Initial price p0 1,..., p0 J ; product attribute X1,...,XJ ; initial pricing strategies Q1,..., QJ ;
consumer attribute At 1,...,At N ; consumer decision model CM ; initial recommendation strategy
RS.
1: while t ≤ tmax do
2: Step 1: Pricing Decision
3: for each seller j: do
4: pt j is made based on Qj.
5: end for
6: Step 2: Recommendation and Demand Realization
7: for each consumer i: do
8: Consumer i sees a list of products with ranking Bi which is determined based on p0 1,...,
p0 J , X1,...,XJ , and At i by RS t.
9: Consumer i makes the search and purchase decisions following the decision model M .
10: end for
11: for each seller j: do
12: Demand Dt j and Profits Rt j are realized.
13: end for
14: Total utility T U, total demand T Dt, and total Revenue Π t on the platform are realized.
15: Step 3: Algorithm Update
16: for each seller j: do
17: Pricing strategy Qj is updated based on the seller’s objective rt j.
18: end for
19: Platform also realizes the reward mt.
20: t ← t + 1.
21: end while
subsequent investigations (Dou et al. 2024, Rocher et al. 2023). However, incorporating recommen-
dation systems into this framework introduces a set of additional methodological complexities.
First, the introduction of recommender systems necessitates modeling consumer decision-making
amid multiple simultaneously presented product recommendations. Consumers typically encounter
a ranked list of products and need to devote time and effort to assess those of interest (Moraga-
Gonz´ alez et al. 2023). Additionally, position biases may influence their choices (Jeunen and
Goethals 2021, Guo et al. 2019, Ursu 2018, Hofmann et al. 2014). In response, we develop a model
that incorporates both consumer search behaviors and position biases, as discussed in Section 3.2.

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 13
Second, consumers exhibit inherent heterogeneity, requiring sufficient flexibility in both the
demand model and the associated personalized recommendation algorithms (Chung et al. 2024,
Morozov et al. 2021, Zhang et al. 2019). Accounting for such realities complicates the estimation of
demand models and the optimization of recommendation strategies. We address these challenges
in Sections 3.2, 3.4, and 4.
Finally, while the framework introduced by Calvano et al. (2020b) is notably adaptable and
involves relatively fewer stringent assumptions, it still presupposes forward-looking pricing algo-
rithms and simultaneous decision-making among sellers. We critically examine these assumptions
and relax them, thereby extending the model’s scope and robustness. The details of these modifi-
cations and their implications are presented in Section 6.
3.2. Consumer Demand Model
In this subsection, we examine a structural search model to elucidate the decision-making processes
of consumers when presented with platform-based recommendations. We adopt the sequential
search framework for several reasons. First, consumers typically lack complete information about
all available products in the market and face significant costs when seeking information (Moraga-
Gonz´ alez et al. 2023, Mortensen 2011). This aligns with the objectives of recommender systems,
which aim to alleviate the challenges of information overload and search frictions (Zhang et al.
2019). The sequential search model addresses these issues by explicitly incorporating the search
costs incurred by consumers in accessing product information (Ursu et al. 2023, Weitzman 1979).
Second, when multiple products are recommended, position bias may emerge, a phenomenon that
the sequential search framework can effectively capture (Chung et al. 2024, Ursu 2018). Third, the
sequential search model allows for the incorporation of heterogeneous preferences and search costs
among consumers, thereby facilitating personalized recommendations within this framework (Ursu
et al. 2023, Morozov et al. 2021).
Specifically, each consumer i is presented with a recommendation set Bi, resulting from the
platform’s top-K recommendation algorithm (K ≤ J)5. Here, Bi denotes a consumer-specific subset
of all products ( j = 1, 2, . . . , J) in the marketplace. The position of product j for consumer i is
represented by posi,j (posi,j ∈ {1, 2, . . . , K}). From the consumer’s perspective, the value of each
product is quantified by the purchase utility function. This utility, ui,j, derived by consumer i from
product j, is decomposed into two components:
ui,j = vi,j + ξi,j (1)
5 In this section, the time index t is omitted for simplicity, although pt j and At i may vary over time.

Xu, Lee, and T an:Algorithmic Collusion or Competition
14 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
The first component, vi,j, represents the utility observable on the search results page prior to
clicking. In contrast, the second component, ξi,j, which follows a normal distribution N (0, δ2 ξ ),
denotes the utility revealed only after navigating to the product’s webpage.
Moreover, each product j is characterized by its price pj and a vector of attributes Xj, which
are disclosed to consumers prior to their search. Similarly, consumer i has a series of attributes Ai.
Consequently, the decision-making context for each consumer i includes the following elements:
the consumer i with attributes Ai, product j with its price pj and attributes Xj (j ∈ Bi), and
the ranking of these product ψi,j. Consistent with prior research on sequential search models, we
postulate a linear parametric relationship between these observed attributes and the consumer’s
pre-search expected utility (Chung et al. 2024, Ursu 2018):
vi,j = βi ∗ pj + Γ′ ∗ Xj + Θ′ ∗ Ai (2)
In addition to the utility derived from purchasing products, consumers incur a cost associated
with the search required to ascertain ξi,j. This cost is encapsulated by the search cost function ci,j,
which, in accordance with extant literature, adheres to an exponential function contingent upon
the product’s ranking:
ci,j = exp (τi + φ · posi,j) (3)
Given consumers’ uncertainty regarding the precise magnitude of ξi,j—with only its probabilistic
distribution known—it becomes necessary for consumers to balance the potential utility gains from
discovering products that offer higher purchase utility, ui,j, against the associated search costs, ci,j.
This trade-off in consumer decision-making is encapsulated by the concept of reservation utility
(Weitzman 1979). The reservation utility for a product, denoted by zi,j, is defined as the utility
level at which the consumer is indifferent between continuing the search for product j or obtaining
a utility of zi,j with certainty. Mathematically, this represents the equivalence between the marginal
utility derived from searching for product j and the marginal cost incurred, expressed as:
ci,j =
Z ∞
zi,j
(ui,j − zi,j) f (ui,j)dui,j
=
Z ∞
zi,j
(vi,j + ξi,j − zi,j) f (ξi,j)dξi,j
(4)
Incorporating purchase utility and search costs, the framework that governs consumer search
and selection behavior is delineated by three fundamental rules: the selection, stopping, and choice
rules. These rules comprehensively characterize consumer behavior, as detailed below:
1. Selection Rule : This rule stipulates that consumers rank products in descending order
based on their reservation utilities, denoted by zi,j. This ranking determines the sequence in which
products are searched. Specifically, the product with the highest reservation utility, zi,j, is selected
as the next candidate for evaluation.

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 15
2. Stopping Rule : After evaluating the set of products Hi and observing their post-search
utilities6, consumer i needs to decide whether to continue the search or terminate it. The search
proceeds if the highest utility realized from the searched products Bi is less than the maximum
reservation utility among the yet-to-be-searched options, Bi \ Hi:
max
j∈Hi
ui,j < max j∈Bi\Hi zi,j (5)
Conversely, the search is terminated if the above condition is not met. In other words, the max-
imal utility among all the searched products exceeds the reservation utilities of all the unsearched
products. Additionally, the search process also terminates if all options have been searched.
3. Choice Rule: Upon cessation of the search, the consumer selects the product k that exhibits
the highest utility from all the searched products:
ui,k ≥ max j∈Hi ui,j (6)
By integrating these rules, consumers make search and purchase decisions based on available
information. The entire process is visualized in Appendix A. Section 4 provides further details on
how to estimate this model and derive parameters from the data.
3.3. Pricing Algorithms Adopted by Sellers
In modeling the pricing algorithm, we employ the canonical Q-learning for investigating pric-
ing games, consistent with prior research on algorithmic collusion (Dou et al. 2024, Wang et al.
2023a, Colliard et al. 2022, Banchio and Skrzypacz 2022). The selection of the classical Q-learning
approach is motivated by several compelling factors (Calvano et al. 2020b). First, Q-learning is
extensively utilized in practice and serves as the foundation for numerous state-of-the-art reinforce-
ment learning algorithms (Li 2023), including DQN (Mnih et al. 2015), Double DQN (Van Hasselt
et al. 2016), Double-Dueling DQN (Wang et al. 2023b), and many advanced variants (Silver et al.
2018, 2016). Consequently, studying Q-learning provides insights into a broad spectrum of algo-
rithmic pricing models that build upon its adaptations. Second, Q-learning models the reward
structure non-parametrically and requires only a minimal number of parameters. Its simplicity,
relative to neural network-based algorithms, requires fewer assumptions and facilitates a clearer
interpretation of the parameters’ impact on game dynamics. Third, Q-learning’s capacity to oper-
ate without prior knowledge of the economic environment aligns with real-world scenarios where
sellers possess limited market information, thereby enhancing the practical applicability of our
pricing model.
6 Consistent with prior literature, we assume that consumers are aware of their outside option before searching
recommended alternatives. Consequently, we further assume Hi(0) = 0 for notational simplicity (Ursu et al. 2023).

Xu, Lee, and T an:Algorithmic Collusion or Competition
16 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
We now provide a detailed description of our Q-learning algorithm and introduce the relevant
notation for our framework. Building on the foundational work on Q-learning, we define the agent’s
state, action, immediate reward, and objective to determine its optimal strategy within the frame-
work of Markov decision processes (Watkins 1989). In each discrete period t, the pricing agent j
(i.e., seller j on the platform) observes the current state variable st and selects a pricing action
pt j from a set of feasible actions P . Although the pricing agent has access to historical pricing
data, to streamline calculations and maintain consistency with prior studies, we assume a one-
period memory (Calvano et al. 2020b), resulting in the state being represented by the prices of
all products in the previous period: st = (pt−1 1 , . . . , pt−1 J ). Subsequently, the pricing agent receives a
reward rt j from the environment and observes the complete set of prices transitioning to the next
period, denoted by st+1 = (pt 1, . . . , pt J ). In the context of our pricing game, the reward corresponds
to the seller’s revenue generated by the demand model. The primary objective of the pricing agent
j is to maximize the total discounted cumulative reward (i.e., revenue for seller j), expressed as
E
P∞
t=0 δtrt j  , where δ represents the discount factor.
Since each agent’s action influences not only the immediate reward but also the subsequent state
transition, it is imperative for the agent to adopt a forward-looking perspective that accounts for
the value of each state s7. This state-specific value can be expressed as the maximum expected
value obtained by summing the immediate reward from an action and the anticipated value of the
ensuing state s′ resulting from action p8. This concept is traditionally encapsulated by Bellman’s
value function:
V (s) = max
p∈P
{E [ri | s, p] + δE [V (s′) | s, p]} (7)
In line with the prevalent methodology for addressing this optimization problem, we adopt the
Q-function, which encapsulates the expected reward of taking a particular action in a given state,
thereby circumventing the direct solution of Bellman’s equations (Li 2023, Watkins 1989). The
Q-function is represented as a matrix with dimensions |S| × |P |, and each element is computed
according to the following procedure:
Qj (s, p) = E [rj | s, p] + δE

max
p′∈P Qj (s′, p′) | s, p

(8)
If the true Q-function were known, the agent could readily determine the optimal action to take
in the current state. Therefore, the essence of Q-learning lies in approximating the Q-function
by exploring various actions while minimizing the loss of rewards due to sub-optimal choices. To
7 This assumption will be relaxed in Section 6.
8 For notational simplicity, variables pertaining to the current period are denoted without a prime, while variables
representing the subsequent period are indicated with a prime.

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 17
estimate the Q matrix Qj, at each period t, agent j selects an action pt j based on the current state
st, observes the resulting state transition st+1, receives the corresponding reward rt j, and updates
the Q-value for this state-action pair as follows:
Qj(s = st, p= pt j) = (1− α)Qj(s, p) +α

rt j + δ max p′∈P Qj  st+1, p′ (9)
For all other state-action pairs where s ̸= st or p ̸= pt j, the Q-values remain unchanged. Here,
we introduce a hyperparameter α, representing the learning rate. This parameter determines the
extent to which the updated Q-value depends on newly acquired information during the current
period relative to the previous Q-value.
Beginning with minimal information and an arbitrary Q matrix, the agent must learn the value
associated with each state-action pair. Given the uncertainty in the environment, particularly the
unknown actions of other sellers, each element in the Q table may require numerous iterations
to accurately estimate its expected value. However, uniformly exploring all actions can lead to
the opportunity cost of selecting sub-optimal actions. Consequently, the Q-learning agent needs to
balance exploration and exploitation. To address this, a common strategy is the ϵ-greedy approach,
where, in each period, the agent selects a random action with probability ϵ (exploration) and
chooses the optimal action based on the current Q matrix with probability 1 − ϵ (exploitation).
Moreover, acknowledging that the reliability of the Q matrix improves as the agent gathers more
information, it is customary to employ a time-decaying ϵ value, thereby increasing the propensity
for exploitation over time. In accordance with this methodology, we incorporate an exponential
time decay for ϵ, defined as ϵ = exp(−ωt), where ω denotes the decay rate.
3.4. Recommender Systems Adopted by the Platform
In this subsection, we delineate the specific recommender systems employed by the platform.
Although our study primarily investigates the economic impact of recommender systems rather
than seeking technical enhancements (Li et al. 2020, 2018, Fleder and Hosanagar 2009), we aim to
ensure that the algorithm aligns rigorously with the economic setting, as established in prior works
on product display algorithms (Compiani et al. 2024, Derakhshan et al. 2022, Ferreira et al. 2022).
Simultaneously, we also need to maintain the ease of tracking economic properties and conducting
counterfactual evaluations.
Achieving these objectives collectively presents inherent complexity, as even minor extensions
to the choice model can render the derivation of closed-form expressions for choice probabilities
intractable, not to mention the subsequent implications (such as expected revenue or consumer
utility) (Train 2009). Consequently, even when the platform possesses precise knowledge of the
demand model parameters and no heterogeneity exists, determining the optimal assortment and

Xu, Lee, and T an:Algorithmic Collusion or Competition
18 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
rankings typically necessitates a brute-force approach (Compiani et al. 2024). In our case, the
demand model presented in Section 3.2 incorporates both observed and unobserved heterogeneity,
further complicating the derivation of a recommendation strategy. To overcome these challenges,
we perform multi-layer numerical integration over the distributions of these heterogeneities and
the taste shocks, followed by a brute-force search process to identify the optimal recommendations
(including assortment and ranking) based on specific objective functions (Compiani et al. 2024).
As discussed in Section 1, previous economic and optimization studies predominantly consider
revenue and consumer utility as the primary objective functions for platforms (Compiani et al. 2024,
Derakhshan et al. 2022). Consequently, we design the recommendation algorithms to optimize these
two objectives, aligning with our first research question: How does the objective of the recommender
system influence the algorithmic pricing game?
Specifically, in each time period, J products are available, each characterized by a vector of static
attributes Xj and a price pj set by the seller9. Each consumer is represented by observed attributes
Ai, as well as two unobserved attributes, βi and τi, which are not observable to the platform.
Nevertheless, the platform can infer the distributions of these parameters across the consumer
base using available data. In the subsequent subsections, we outline the platform’s decision-making
process in presenting products to each consumer i, focusing on the two aforementioned objectives.
For comparative analysis, we also consider a baseline scenario in which the platform does not
utilize any optimization techniques, opting instead to present each consumer with a randomly
assorted and ranked selection of products.
3.4.1. Revenue-Maximization Recommender System
The revenue-maximization recommender system aims to maximize the total revenue for all the
sellers on the market (Compiani et al. 2024). This approach closely aligns with the objectives of
platforms that generate income by collecting a portion of sellers’ revenue as commission fees, as
observed in prominent platforms such as Amazon and Tmall.
For each consumer i, the platform is privy to her observable attributes Ai as well as the distri-
butions of unobservable heterogeneities βi and τi, but not their precise values. Additionally, the
exact values of the post-search match values ξi,j also remain unknown to the platform; only their
distributions are accessible. Consequently, for each potential recommendation set 10, the platform
computes the expected revenue and identifies the sets that maximize this expected revenue for
exposure through the following process (Algorithm 2).
9 For clarity and simplicity, the time index is omitted in our notation, as previously done in Section 3.2.
10 For instance, consider three products (indexed as 1, 2, and 3), where the platform must recommend two to the
consumer, with the ranking of the displayed products being important. In this case, there are six possible bundles:
{1,2}, {2,1}, {1,3}, {3,1}, {2,3}, {3,2}.

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 19
Specifically, the recommendation generation process for consumer i proceeds as follows. For each
potential recommendation set, we first sample the unobserved heterogeneitiesβi and τi (outer loop),
followed by sampling the post-search shocks for each product, cξi,j (inner loop). In the inner loop,
the calibrated structural search model is employed to simulate the consumer’s purchase decisions,
thereby determining the revenue for each sample. By averaging across the samples in the inner loop,
we numerically integrate out the post-search shocks, obtaining the expected revenue conditional on
the specific unobservable heterogeneities ( βi and τi). Subsequently, in the outer loop, we average
over all sampled unobservable heterogeneities to derive the unconditional expected revenue for
the recommendation set. This numerical integration process is widely utilized in optimization and
econometrics, such as in simulated maximum likelihood estimation, and will be further detailed
in Section 4. Finally, we compare the expected revenues across all recommendation sets, identify
those with the highest revenue, and randomly recommend one of these sets to consumer i.
3.4.2. Utility-Maximization recommender system
In contrast, utility-maximization recommender systems are designed to enhance the utility expe-
rienced by consumers on the platform (Compiani et al. 2024). Utility serves as an economic mea-
sure of consumer satisfaction, which benefits the platform by improving consumer retention rates,
thereby making it a common objective for many platforms (Zhang et al. 2019, Ursu 2018). Similar to
revenue-maximization recommender systems, utility-maximization systems also employ numerical
integration techniques to estimate the expected consumer utility for each potential recommenda-
tion set. The primary distinction lies in the post-simulation analysis: for each sample, the calibrated
structural model is used to simulate consumer behavior, after which the search history and pur-
chase decisions are utilized to calculate utility (purchase utility minus total search costs) instead of
revenue. Once the expected utility for each recommendation set is derived, the platform identifies
those sets that maximize utility and randomly selects one of these optimal sets to recommend to
consumer i. This process is further detailed in Algorithm 3.
4. Data, Structural Estimation, and Parameterization
Although we aim to design our framework to be robust against parameter variations and minimize
reliance on assumptions, certain parameters still need to be specified prior to conducting numerical
experiments. In this section, we describe the calibration of the structural search model using real-
world data, the setup of the pricing algorithms, and the integration of these components for step-
by-step simulations.

Xu, Lee, and T an:Algorithmic Collusion or Competition
20 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
Algorithm 2 Revenue-Maximization Recommender Systems
Require: K, F(βi), F(τi), F(ξi,j), Ai, pt j, and Xj for j = 1, 2, . . . , J
Require: Calibrated Structural Search Model CM
1: Derive all the potential K-product recommendation sets, each represented by Bb
2: for each Bb do
3: for each sample of unobserved heterogenities ( N S1 samples) do
4: Sample bβi based on F (βi)
5: Sample bτi based on F (τi)
6: for each sample of post-search shocks ( N S2 samples) do
7: Sample bξi, which is a vector of cξi,j, based on F (ξi,j)
8: Simulate the purchase decision bki following CM
9: Derive the platform’s award (revenue): m|(Bb, bβi, bτi, bξi) = pt bki
10: end for
11: Approximate the conditional expected revenue:
m|(Bb, bβi, bτi) = 1 N S2 X m|(Bb, bβi, bτi, bξi)
12: end for
13: Approximate the conditional expected revenue:
m|Bb = 1 N S1 X m|(Bb, bβi, bτi)
14: end for
15: Find the Bb with the largest expected revenue m|Bb
16: Output: Equally assign the exposure to these sets with the largest expected revenue
4.1. Parameterization of the Consumer Demand Model
In modeling consumer demand, we aim to derive consumers’ price sensitivity, attribute preferences,
search costs, and positional biases within a real-world context. To achieve this, we draw upon
established literature and estimate our model using customer search and choice data made publicly
available by Expedia (Compiani et al. 2024, Ursu 2018).
4.1.1. Data
The Expedia dataset is provided at the level of search impressions, defined as ordered lists of
hotels and their characteristics presented to consumers in response to their trip queries. Notably,
this dataset originates from a field experiment wherein consumers searching for hotels during
the observational window were randomized into two groups: (i) those viewing Expedia’s standard

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 21
Algorithm 3 Utility-Maximization Recommender Systems
Require: K, F(βi), F(τi), F(ξi,j), Ai, pt j, and Xj for j = 1, 2, . . . , J
Require: Calibrated Structural Search Model CM
1: Derive all the potential K-product recommendation sets, each represented by Bb
2: for each Bb do
3: for each sample of unobserved heterogenities ( N S1 samples) do
4: Sample bβi based on F (βi)
5: Sample bτi based on F (τi)
6: for each sample of post-search shocks ( N S2 samples) do
7: Sample bξi, which is a vector of cξi,j, based on F (ξi,j)
8: Simulate the search sequence cHi and purchase decision bki following CM
9: Derive the utility:
m|(Bb, bβi, bτi, bξi) = ui, bki − X
j∈ cHi
ci,j
10: end for
11: Approximate the conditional expected utility:
m|(Bb, bβi, bτi) = 1 N S2 X m|(Bb, bβi, bτi, bξi)
12: end for
13: Approximate the conditional expected utility:
m|Bb = 1 N S1 X m|(Bb, bβi, bτi)
14: end for
15: Find the Bb with the largest expected utility m|Bb
16: Output: Equally assign the exposure to these sets with the largest expected utility
ranking, where hotels are ordered by relevance, and (ii) those viewing a random ranking, where
hotels are displayed in a random order. Consequently, for the randomized group, the hotel display
is exogenous to their attributes, eliminating the influence of the platform’s existing algorithms on
the customer modeling process. We utilize this random-ranking sample for our model estimation
(Chung et al. 2024, Ursu 2018).
Following prior literature, we also partition the dataset by travel destination, recognizing that
each destination may differ significantly in terms of hotels and travelers, and that hotels in different
destinations do not directly compete with each other (Chung et al. 2024, Ursu 2018). We thus focus

Xu, Lee, and T an:Algorithmic Collusion or Competition
22 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
on the destination with the largest number of observations (destination ID 8192). After applying
additional filtering procedures to exclude null values and outliers, we obtain 35,769 observations,
where each observation represents one available alternative. Further details on data cleaning, vari-
able descriptions, and summary statistics are provided in Appendix D.
4.1.2. Estimation
As researchers, we observe some covariates ( Ai, Xj), consumers’ search sequences Hi =
{Hi(0), . . . ,Hi(h)}, and their final purchase decisions k. However, the utility parameters ( βi, Γ,
Θ) and search cost parameters ( τi, φ) are unobserved and need to be estimated from the data.
Following the sequential search literature, we also do not observe the exact values of the post-search
shocks ξi,j but assume they are drawn from the standard normal distribution N (0, 1) (Ursu 2018,
Weitzman 1979)11. From the consumers’ decision rules, we can infer the following mathematical
relationships:
1. A product searched later has a reservation utility higher than the utilities of products searched
earlier:
zi,Hi(q) ≥
q−1
max
j=0
ui,Hi(j), ∀q ∈ {1, . . . , h}. (10)
2. The reservation utilities of all unsearched products are lower than the maximum utility among
the searched ones:
max
q∈Bi\Hi
zi,Hi(q) ≤ max j∈Hi ui,j. (11)
3. The purchased product has the highest utility among all searched products:
ui,k ≥ max j∈Hi ui,j. (12)
By integrating these relationships, the probability of consumers’ search sequences and purchase
decisions that align with the observed data can be expressed as:
Pi,k,Hi = Pr

zi,Hi(q) ≥
q−1
max
j=0
ui,Hi(j), ∀q ∈ {1, . . . , h}

∩

max
q∈Bi\Hi
zi,Hi(q) ≤ max j∈Hi ui,j

∩

ui,k ≥ max j∈Hi ui,j

(13)
To estimate the model, we address two primary challenges. First, structural search models typ-
ically lack closed-form expressions that directly relate parameters to choice probabilities. Conse-
quently, consistent with prior literature, we employ simulated maximum likelihood (SML) estima-
tion using a logit-smoothed accept-reject (AR) simulator (Ursu et al. 2023). Second, to enhance
11 This is a standard assumption in the sequential search literature because, in any utility maximization framework,
only differences among choices matter (Ursu et al. 2023). Consequently, only therelative magnitudes of the search cost
and the post-search variance are crucial in balancing the costs and benefits of conducting searches. This normalization
allows us to fix one part while estimating the other.

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 23
the model’s flexibility in analyzing the pricing game under the influence of recommendations, it is
essential to account for unobservable heterogeneities in price coefficients and search costs. Specifi-
cally, we assume that the price coefficient and search cost are drawn from log-normal distributions
(see Equations 14 and 15):
βi ∼ exp(mβ + σβ · yβ,i) (14)
ci,j ∼ exp(mτ + στ · yτ,i + φ · posi,j) (15)
where yβ,i ∼ N (0, 1) and yτ,i ∼ N (0, 1).
Although SML is commonly utilized for econometric models with random coefficients (Train
2009), incorporating an additional layer of simulation to capture unobservable heterogeneities sub-
stantially increases the computational burden. To mitigate this, we innovatively integrate Gaussian
Hermite quadrature into the estimation procedure (Ak¸ sin et al. 2013). To the best of our knowl-
edge, this represents the first application of the Hermite approach to estimate a structural search
model incorporating unobservable heterogeneities. After addressing these challenges, we obtain the
model estimates presented in Table 2.
Table 2 Structural Estimation Results
V ariable Coefficients Std
mβ -1.0384∗∗∗ (0.0047)
σβ 0.0067∗∗∗ (0.0025)
ΓHotelStars 0.4955∗∗∗ (0.0197)
ΓHotelReview -0.1897∗∗∗ (0.0387)
ΓBrand 0.0030 (0.0235)
ΓHotelLocationScore -0.1851∗∗∗ (0.0469)
ΓP romo 0.0408∗ (0.0247)
ΘReqRoomN um -0.1315∗∗∗ (0.0197)
ΘSatN ight 0.1045∗∗∗ (0.0168)
vi,0 0.1653 (0.3173)
mτ -1.1490∗∗∗ (0.0172)
στ 0.0050∗ (0.0029)
φ 0.0050∗∗∗ (0.0009)
Note: Bootstrap standard errors in parentheses; ∗∗∗ p<0.01, ∗∗ p<0.05, ∗ p<0.1.

Xu, Lee, and T an:Algorithmic Collusion or Competition
24 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
4.2. Parameterization of the Pricing Algorithms
In our repeated game framework, the pricing algorithms necessitate the specification of several
hyperparameters prior to simulation. Since these parameters do not influence the qualitative out-
comes, we adopt the hyperparameter settings from Calvano et al. (2020b), specifically assigning
a learning rate of α = 0.15 and a discount factor of δ = 0.95. To accommodate the presence of
three agents, we enhance exploration by utilizing a smaller exploration rate, ω = 1.5 × 10−6. We
define the minimum and maximum permissible prices for sellers as the 10th and 90th percentiles
of the dataset’s prices (i.e., 0.5 and 2.59), respectively. This price range is discretized into nine
equal intervals, resulting in ten available pricing actions. Additionally, we relax these parameter
assumptions in Section 6.
4.3. Integration into the Simulation
To evaluate the outcomes and address our research questions within the repeated game framework,
we implement several additional steps. First, for our primary simulation, we consider a scenario
involving three sellers, where the platform recommends two out of the three available products to
each consumer in each period. This configuration represents the most fundamental case in which
assortment and position biases are relevant, while avoiding excessive computational complexity
following prior studies (Dou et al. 2024, Calvano et al. 2020b).
Second, to establish the static characteristics of the sellers, we utilize the median values from
the dataset, thereby creating a balanced market that facilitates easy interpretations of effect sizes.
However, this approach results in homogeneity among alternatives aside from price. To introduce
horizontal differentiation, we add a zero-mean term of the form ( µ · N (0, 1)), where µ can be
adjusted to simulate various economic environments and address our third research question 12.
Third, we employ the empirical distribution of all consumers from the dataset. This distribution,
combined with the calibrated structural search model, enables us to generate demand and thereby
determine the rewards for both sellers and the platform. To compute the expected value of these
rewards, we follow the same numerical integration procedure used for the recommender system,
accounting for both consumer heterogeneity and taste shocks. Having established these elements,
we integrate the calibrated structural search model and the pricing algorithms into the repeated
game framework to carry out the simulations.
5. Results
After completing these aforementioned steps, we proceed to conduct numerical experiments to
address our research questions. Specifically, as outlined in Algorithm 1, each simulation run extends
12 Since our utility magnitudes are comparable to those in Calvano et al. (2020b), we also vary µ from 0 to 0.5 to
sufficiently explore its impact and employ µ = 0.25 to illustrate the main results.

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 25
over multiple periods. At the commencement of each period, each seller utilizes its respective pricing
algorithm, as detailed in Section 3.3, to determine pricing decisions. Subsequently, the platform
generates recommendations for each consumer following the strategy described in Section 3.4.
Consumers then observe the recommended set and make purchase decisions based on the calibrated
structural search model presented in Section 3.2. Each seller realizes revenue and updates its
algorithm accordingly. With parameters fixed as described in Section 4, the simulation framework
is fully specified.
In the subsequent three subsections, we vary different elements of the framework to evaluate
how these variations produce different counterfactual outcomes, thereby systematically addressing
each of our research questions.
5.1. Effect of the Recommender Systems’ Objectives
As motivated in our RQ1, one of the fundamental economic aspects of recommender systems is
their underlying objective, as it directly shapes which products are highlighted for consumers and
influences sellers’ rewards and game directions. Among the commonly considered objectives are
Revenue-Maximization, which seeks to increase total platform-wide revenue and thereby aligns with
the platform’s economic interests through commission fees, and Utility-Maximization, which aims
to enhance consumer utility, potentially benefiting the platform by fostering consumer retention
(Compiani et al. 2024, Feldman et al. 2022, Derakhshan et al. 2022, Ursu 2018).
To evaluate how different objectives influence the dynamics of the algorithmic game, we conduct
a series of numerical experiments. Specifically, we compare the equilibrium outcomes of the game
(prices, overall revenue, and consumer utility) under three distinct scenarios as specified in Section
3.4: (i) a revenue-maximization recommender system, (ii) a utility-maximization recommender
system, and (iii) a baseline scenario that does not incorporate recommendation optimization as a
point of reference.
For each scenario, we conduct 50 simulation runs, each spanning 3,000,000 periods 13. At each
period, we record the average price and revenue for the three sellers, as well as the average consumer
utility across all consumers. These values are then averaged over the 50 runs, and their means
from the final 1,000 periods are reported in Table 3. Standard deviations, presented in parentheses,
provide insight into the degree of end-game fluctuation.
Our findings indicate that the objectives of recommender systems substantially shape the trajec-
tory of pricing strategies and their eventual equilibrium outcomes. Under revenue-maximization,
sellers gravitate toward more collusive behavior, resulting in higher equilibrium prices (2.3844) and
13 Q-learning agents often converge slowly because only one element is updated in each period (Calvano et al. 2020b).
However, as shown in Figure 1, the game’s duration primarily affects the magnitude of the effects rather than their
qualitative direction.

Xu, Lee, and T an:Algorithmic Collusion or Competition
26 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
Table 3 Price, Revenue, and Utility Comparison Across Objectives
Revenue-
Maximization
Utility-
Maximization
Baseline
Prices 2.3844 (0.0137) 0.9095 (0.0478) 1.6617 (0.0236)
Revenue 0.2583 (0.0003) 0.1174 (0.0041) 0.2163 (0.0015)
Utility 0.3749 (0.0012) 0.6506 (0.0063) 0.4765 (0.0032)
revenue (0.2583) at the expense of consumer utility (0.3749). Conversely, when the system aims
to maximize consumer utility, the equilibrium is less collusive, featuring lower prices (0.9095) and
higher consumer utility (0.6506), but reduced seller revenue (0.1174).
Figure 1 illustrates the temporal evolution of prices under the three scenarios, further corrobo-
rating our findings. In the revenue-maximization setting, sellers gradually and stably converge to
higher prices. Under utility-maximization, they tend to settle at lower prices but exhibit greater
volatility in their pricing behavior.
An additional noteworthy pattern emerges under utility-maximization recommender systems:
two sellers maintain slightly higher prices, while one sets a lower price. In this asymmetric equilib-
rium, each seller seeks to optimize its own revenue. The two high-price sellers face lower exposure
and sales, yet each sale generates relatively higher revenue. The low-price seller benefits from
increased exposure and sales volume, but at a lower per-sale revenue. This interplay ensures that all
three sellers achieve similar revenue levels, while the platform also meets its utility-maximization
objective despite the asymmetric pricing configuration.
To further elucidate this asymmetry, we can examine the underlying incentives of the sellers
and the platform. On one hand, a high-priced seller might find it beneficial to deviate by lower-
ing its price. However, after that, in the presence of two low-priced competitors, the remaining
high-priced seller receives minimal exposure and revenue due to the platform’s utility-maximizing
recommender system. This scenario incentivizes the high-priced seller to also reduce its price. The
resulting intensified competition diminishes the revenues of all three sellers, rendering such devi-
ations unstable. Conversely, sellers have limited motivation to increase prices, as doing so would
lead to decreased exposure and revenue. These opposing dynamics converge to an asymmetric equi-
librium that exhibits significant fluctuations, thereby accounting for the relatively high standard
deviation observed under the utility-maximization framework.
Conversely, the revenue-maximization scenario converges rapidly and maintains relative stability.
In this context, both the sellers and the platform are incentivized to sustain higher prices. Starting
from a lower price, if a seller raises its price, the likelihood of purchase will decrease, assuming
all other factors remain constant. However, in the presence of revenue-maximizing recommender

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 27
(a) Revenue-Maximization RS
 (b) Utility-Maximization RS
(c) Baseline
Figure 1 Learning Dynamics
Note: The points on the continuous lines depict the moving average, with a window size of
1000, of the average price observed across 50 experiments at each t. The shaded region’s upper
and lower limits indicate the highest and lowest values occurring within the window.
systems, this reduced likelihood of purchase may be offset by increased product exposure, thereby
compensating for the higher price. As a result, prices within the revenue-maximization scenario
can escalate to collusive levels and remain at these levels over time. At these collusive price points,
all products within the recommendation set receive equal exposure. If a seller deviates by setting
a different price, this deviation leads to a decrease in overall revenue for displaying the deviating
seller. Consequently, the platform responds by prioritizing the other sellers: the deviating seller
experiences significantly lower exposure and rewards, while the non-deviating sellers receive even
higher rewards. This mechanism incentivizes the deviating seller to revert to the collusive price,
and the non-deviating sellers have no incentive to follow the deviation. Consequently, driven by the

Xu, Lee, and T an:Algorithmic Collusion or Competition
28 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
revenue-driven incentives of the three sellers and the platform’s revenue-maximizing recommenda-
tion system, a collusive price equilibrium is both achievable and stable.
Furthermore, certain recommender systems in two-sided markets balance the interests of various
stakeholders by adopting a composite objective that integrates both revenue and consumer utility.
Consequently, beyond the aforementioned analysis, we examine the impact of varying the relative
weights assigned to revenue and utility objectives on market outcomes, as detailed in Appendix J.
The findings indicate a monotonic relationship between these weights and the resulting equilibrium,
thereby highlighting the critical role of recommender system objectives in shaping algorithmic
pricing dynamics. Therefore, when antitrust regulators aim to control supracompetitive prices, they
should not solely attribute such phenomena to sellers and pricing algorithm providers. Instead,
platforms that implement recommender systems should also be considered as part of the responsible
entities.
5.2. Effect of the Recommendation Size
Apart from the objectives of recommender systems, another aspect of particular interest regarding
their economic impact is the size of recommendations. As motivated in our second research question
(RQ2 ), this dimension holds significant economic importance, as it directly influences search friction
and competition among sellers (Moraga-Gonz´ alez et al. 2023, Hong and Shum 2006). Guided by
the antitrust and algorithmic collusion literature’s emphasis on enhancing consumer welfare (Baker
2019), it is natural to question whether displaying more products can effectively achieve this goal.
The rationale is as follows: with a greater number of options, consumers can disregard products
they do not prefer while selecting those that enhance their utility. This intuition is supported by
choice modeling literature, where the welfare function of a product set increases as more products
are included (Train 2009).
To assess the impact of recommendation size when using the utility-maximization recommender
system and address our RQ2, we conduct numerical experiments with K = 1, 2, 3 under Top- K
utility maximization recommender systems. For each scenario, we perform 50 simulation runs (each
consisting of 3,000,000 periods) and record the average equilibrium price, revenue, and utility in
Table 4.
Contrary to conventional wisdom and the choice modeling literature, as illustrated in the third
row of Table 4, increasing the number of displayed products does not consistently enhance consumer
utility (0.6506 > 0.6128 > 0.5522). This seemingly counterintuitive result arises from two compet-
ing mechanisms. On the one hand, displaying more products provides consumers with greater
opportunities to identify products that offer higher utility, potentially increasing their overall util-
ity. On the other hand, a larger number of displayed products diminishes the platform’s ability

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 29
to effectively influence prices through recommendations. High-priced products continue to receive
exposure, and some consumers purchase them based on their horizontal preferences. Consequently,
higher-priced products experience relatively smaller losses in their rewards, leading to relatively
higher equilibrium prices after repeated interactions. This effect is reflected in the first row of
Table 4 (1.3115 > 0.9095 > 0.6857). When the latter mechanism predominates, recommending more
products can be detrimental from the consumer’s perspective.
This result also suggests that future research on the economics of recommender systems should
also consider sellers’ price responses as a crucial outcome, particularly in the presence of pricing
algorithms in the market.
Table 4 Price, Revenue, and Utility Comparison Across Recommendation Sizes
K = 1 K = 2 K = 3
Prices 0.6857 (0.0295) 0.9095 (0.0478) 1.3115 (0.0261)
Revenue 0.0788 (0.0014) 0.1174 (0.0041) 0.2040 (0.0027)
Utility 0.5522 (0.0022) 0.6506 (0.0063) 0.6128 (0.0045)
5.3. Horizontal Differentiation Levels as the Moderator
Building on the mechanisms discussed in RQ2, the extent of horizontal differentiation appears to be
a critical moderator influencing the benefits of displaying additional products. As highlighted in our
motivation process of RQ3, when products are highly homogeneous aside from their prices, most
consumers simply choose the least expensive option and ignore others. Consequently, increasing
the number of displayed products provides minimal benefit under conditions of low horizontal
differentiation. Given the pivotal role that horizontal differentiation plays in consumer decision-
making, prior literature in price competition and industrial organization consistently identifies
it as an important factor (Colombo 2013, Thomadsen and Rhee 2007, Tyagi 1999). Within our
pricing game framework, similar logic suggests that greater horizontal differentiation could enhance
consumer utility by offering a wider range of product choices.
To investigate the moderating role of horizontal differentiation and thereby address RQ3, we
conduct a series of simulations by varyingµ and examining scenarios where K = 1, 2, 3. We replicate
the same analyses as in the previous subsection, demonstrating two sets of results below: one with
µ = 0 in Table 5 and another with µ = 0.5 in Table 6.
Surprisingly, our findings uncover a counterintuitive pattern. As horizontal differentiation
increases, the previously observed “more is less” phenomenon emerges (see row 3 of Table 6). In
contrast, when horizontal differentiation is relatively low, increasing the number of recommended
products actually enhances consumer utility (see row 3 of Table 5).

Xu, Lee, and T an:Algorithmic Collusion or Competition
30 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
This outcome can be explained as follows. On the one hand, greater horizontal differentiation
strengthens the mechanism by which consumers more effectively identify products that align with
their preferences, thus gaining additional utility from a broader range of options. On the other hand,
it reinforces a secondary mechanism: as horizontal differentiation increases, consumers’ choices
become more preference-driven rather than price-driven. Consequently, when the recommendation
set is large, higher-priced products experience relatively smaller declines in rewards and can sustain
elevated prices due to persistent demand fueled by horizontal preferences.
When horizontal differentiation is high, both mechanisms intensify, but the latter may dominate.
As a result, contrary to conventional expectations, displaying more products can sometimes reduce
consumer utility when horizontal differentiation is high, while it increases consumer utility when
horizontal differentiation is low.
Table 5 Price, Revenue, and Utility Comparison Across Recommendation Sizes ( µ = 0)
K = 1 K = 2 K = 3
Prices 0.6368 (0.0241) 0.8837 (0.0498) 0.9386 (0.0459)
Revenue 0.0765 (0.0013) 0.1036 (0.0035) 0.1257 (0.0041)
Utility 0.5356 (0.0019) 0.6183 (0.0056) 0.6356 (0.0067)
Table 6 Price, Revenue, and Utility Comparison Across Recommendation Sizes ( µ = 0.5)
K = 1 K = 2 K = 3
Prices 0.6887 (0.0261) 0.8781 (0.0410) 1.7614 (0.0283)
Revenue 0.0815 (0.0016) 0.1292 (0.0047) 0.2740 (0.0028)
Utility 0.6102 (0.0026) 0.7471 (0.0066) 0.6569 (0.0050)
6. F ramework Comparison and Extended Analyses
To incorporate recommender systems and address our research questions, we develop a repeated
game framework that builds upon, yet significantly differs from, the framework proposed by Calvano
et al. (2020b). We nonetheless adopt several assumptions from Calvano et al. (2020b), and thus
conduct a series of extended analyses to examine these assumptions individually, thereby providing
a more holistic perspective. All comparisons and extended analyses are summarized in Table 7.
With respect to the demand model, most studies on algorithmic collusion follow Calvano et al.
(2020b) by employing a reduced-form model in which parameters are directly specified to generate

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 31
Table 7 Framework Comparison and Summary of Extensions
Calvano et al. (2020b) This Work
Demand Model: Model Form Reduced-form Models Structural Models (more in
Appendix A, B, C)
Demand Model: Data Usage No data Real-world dataset (more in
Appendix D)
Demand Model: Choice Set All the products Recommended Products
Demand Model: Position Bias Not Applicable Yes
Pricing Algorithm: Sufficient
Exploration
Yes Relaxed (more in Appendix E)
Pricing Algorithm:
Forward-Looking
Yes Relaxed (more in Appendix F)
Pricing Algorithm: Objective Revenue Relaxed (more in Appendix G)
Game Sequence Simultaneous Relaxed (more in Appendix H)
Recommender Systems No Yes (More in Appendix I and J)
Objective Misalignment Not Applicable Yes
demand responses. In contrast, our main analyses seek to more accurately capture consumer behav-
ior in the presence of recommended products and to systematically characterize the underlying
utility functions. To this end, we develop a sequential search model that incorporates heterogeneous
consumer preferences and search costs, as detailed in Section 3.2 and Appendix A. We estimate
the model parameters using the procedure outlined in Section 4 and a real-world dataset described
in Appendix D, enabling us to conduct counterfactual simulations and derive empirically grounded
insights. Further distinguishing our approach, Calvano et al. (2020b) assume that all products are
fully visible to consumers, providing them with complete information. In contrast, and to more
closely reflect the information overload often encountered in online markets, our model restricts
the consumer choice set primarily to recommended products and introduces search costs for addi-
tional information. We also incorporate position bias into the sequential search model, allowing
for differential consideration of products based on their placement within the recommendation set.
Although this sequential search model offers several advantages, we additionally employ a canoni-
cal logit demand model for robustness checks. As shown in Appendices B and C, the core insights
remain robust even when using a logit demand model with or without heterogeneity in the outside
option.
For the pricing algorithm, we follow Calvano et al. (2020b) and implement a basic Q-learning
approach. Q-learning is chosen due to its prominence in reinforcement learning, its minimal
input requirements, and its nonparametric simplicity. However, Q-learning inherently embodies a
forward-looking component through its state transitions. Therefore, we conduct a robustness check
by relaxing the forward-looking assumption and modeling the algorithms as basic multi-armed ban-
dits. As demonstrated in Appendix F, this modification does not fundamentally alter our results,
indicating that forward-looking behavior is not essential for the core mechanism underlying our

Xu, Lee, and T an:Algorithmic Collusion or Competition
32 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
findings. Moreover, we also examine alternative seller objectives in Appendix G to explore the
broader applicability of our findings.
Regarding the sequence of the game, Calvano et al. (2020b) assume that all sellers make their
decisions simultaneously. While we retain this assumption in our primary analyses, we also relax
it by allowing sellers to update their prices asynchronously. As shown in Appendix H, the core
results remain stable under both simultaneous and asynchronous updating protocols, reinforcing
the generality of our conclusions.
Finally, our framework introduces a key innovation by explicitly incorporating recommender
systems. Beyond addressing the technical challenges of developing an algorithm that is both empir-
ically relevant and theoretically tractable, this addition enables us to examine objective misalign-
ments among various stakeholders. In the main analyses, we illustrate the impact of differing
objectives by considering two polar cases. To further enhance realism, we also examine scenarios in
which the platform optimizes a weighted combination of revenue and utility, with results reported
in Appendix J. Additionally, although consumer utility is closely related to purchase probability
and demand, making demand-maximization theoretically similar to utility-maximization, we nev-
ertheless explicitly test this scenario in Appendix I. In this analysis, we report outcomes for sellers
who optimize either demand or revenue under a demand-maximizing recommender system. Col-
lectively, these results underscore the influential role of recommender systems in shaping product
exposure, influencing seller payoffs, and guiding the evolution of the game.
7. Conclusions
AI-based pricing algorithms are widely adopted by sellers due to their minimal requirement for
human intervention and their remarkable adaptability to rapidly changing economic conditions.
However, both researchers and policymakers have raised concerns regarding the potentially detri-
mental effects of these algorithms on consumer welfare, particularly in relation to the phenomenon
of algorithmic collusion.
In online markets, the high level of digitization facilitates the widespread adoption of pricing
algorithms by sellers. Concurrently, platforms extensively employ recommender systems to optimize
their own objectives, which can alter product exposure and significantly impact the competitive
landscape and pricing dynamics. Despite active research on algorithmic collusion, the role of rec-
ommender systems has been largely overlooked. This study aims to address this gap by developing
a new repeated game framework that incorporates recommender systems and appropriately adjusts
other model components.
After addressing several challenges in specifying and solving the repeated game, we obtain a
series of results that hold significant implications for antitrust regulations, platforms, and sellers.
Additionally, these findings can also inform and guide future research endeavors in this domain.

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 33
For regulators, we demonstrate that the objectives of recommender systems significantly influ-
ence price dynamics and equilibrium outcomes, even when AI-based pricing algorithms are present.
Given the pivotal role of recommender systems, when antitrust legislation seeks to curb supra-
competitive pricing, it may not be sufficient to hold only the AI pricing providers responsible, as
current practice often does (Robertson 2022, Colangelo 2021). It may be beneficial to compare
market outcomes both with and without the existing recommendation systems—particularly those
that disproportionately favor certain stakeholders (e.g., sellers’ revenue or consumers’ utility in
two-sided platforms). Such comparisons would enable regulatory authorities to attribute parts of
any supracompetitive pricing not only to the underlying pricing algorithms, but also to the plat-
form’s recommender system. This approach would yield a more equitable and nuanced regulatory
framework.
However, it is also important to recognize that a platform’s recommender system often functions
as a black box for external regulators. In fact, the pricing algorithms are typically opaque, and
the interaction between these algorithms and the recommender system further complicates the
analysis. Thus, enhanced AI transparency is a fundamental prerequisite for effective regulation.
To promote responsible AI practices and improve regulatory oversight, platforms may need to
disclose additional information about the recommender systems they employ, including the specific
optimization objectives guiding their design.
As for the platform, we also find that when a platform’s objective is to enhance consumer utility,
increasing the number of products displayed may inadvertently have adverse effects in the presence
of pricing algorithms. Moreover, this outcome is moderated by the level of horizontal differentia-
tion among products. Platforms should therefore consider the presence of pricing algorithms and
prevailing market conditions (e.g., the degree of horizontal differentiation) when designing recom-
mender systems. For example, platforms like Amazon could tailor their recommendation strategies
by category: if a market features highly differentiated products, reducing the number of recom-
mended items might improve long-term consumer satisfaction; in markets with less differentiation,
the opposite approach may be more appropriate.
At a broader conceptual level, effective recommender system design in the presence of pricing
algorithms may necessitate transitioning from a “two-tower” recommendation framework (Guo
et al. 2019) to a “three-tower” approach. Traditionally, platforms have focused on understand-
ing consumers’ decision-making processes (one tower) and adjusting the recommendation strategy
accordingly (the second tower). However, as pricing algorithms can also respond strategically and
dynamically, it is essential to incorporate sellers’ pricing behaviors (the third tower) into the frame-
work. This ensures that recommender systems remain adaptable to changes in both consumer and
seller behavior over time.

Xu, Lee, and T an:Algorithmic Collusion or Competition
34 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
For sellers that design or adopt pricing algorithms, our findings indicate that the effectiveness
of these algorithms is contingent upon the platform’s recommendation mechanisms. Consequently,
these stakeholders must concurrently evaluate both the pricing algorithms and the platform’s
revenue-sharing structure, rather than considering them as isolated components. Furthermore, since
product differentiation may influence the platform’s recommendation strategies and subsequently
affect the rewards garnered by pricing algorithms, it is advantageous for sellers to jointly reconsider
both product design and pricing algorithm strategies.
Our study also identifies several future exploration directions for both researchers and practi-
tioners. First, this study is situated within the broader field of the economics of AI, which seeks
to evaluate, design, and implement AI systems through the application of economic principles.
As AI adoption becomes more widespread, it is increasingly important to consider the economic
and societal impacts arising from the interactions among various AI systems. In particular, AI–AI
dynamics, such as those between recommender systems and pricing algorithms, should be evaluated
jointly rather than in isolation. Our work marks an initial step in examining these interactions and
highlights the significance of further investigation into their long-term effects.
Focusing on our specific domain, we contribute to the algorithmic collusion literature by under-
scoring the role of recommender systems in shaping algorithmic pricing competition. In doing so,
we introduce a new analytical framework that may be valuable for future studies examining similar
issues. Besides, our findings also extend the economics of recommender systems literature by incor-
porating adaptive, AI-based pricing, rather than assuming static or fully informed seller-driven
pricing strategies. In other words, the economic impact of recommender systems emerges from
their ability to change product exposure and their influence on the dynamic rewards available to
pricing algorithms. For empirical researchers and companies with the capacity to conduct large-
scale field experiments, examining how price responses evolve (an understudied outcome) under
varying recommendation policies would be a valuable future avenue of study. Such efforts also
require advancement in causal inference methodologies (including experimental design and suitable
evaluation frameworks) to address interference issues arising from dynamic price competition.
Following this line of reasoning, several areas remain for future research. Throughout this study,
due to the unavailability of high-frequency pricing data from the sellers’ side—consistent with other
algorithmic collusion studies across various contexts (Dou et al. 2024, Colliard et al. 2022, Calvano
et al. 2020b)—we directly specify the parameters of pricing algorithms. Nevertheless, acquiring
detailed pricing data, uncovering sellers’ strategies, empirically quantifying levels of collusion, and
conducting additional market design studies represent promising and important avenues for future
research.

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 35
In addition, we focus on the scenario where consumers are presented with the recommended set
and only make their search and purchase decisions among these recommended products (including
outside options). In reality, certain consumers may exhibit strong loyalty to specific products and
possess extensive knowledge about them. These consumers may purchase these products irrespec-
tive of pricing competition or the behavior of recommender systems. Since they do not influence the
relative rewards across different pricing decisions of each seller, they do not affect pricing dynamics
and can thus be safely excluded from our analyses. There may also be consumers who are already
knowledgeable about specific products, potentially encompassing all products within a small mar-
ket. For these consumers, recommender systems serve solely as tools for additional information
discovery. As the proportion of such informed consumers increases, the impact of recommender
systems diminishes. In an extreme case where all consumers are aware of all available products in
the market beforehand, recommender systems would lose their effectiveness. However, the existence
of informed consumers affects only the magnitude, rather than the qualitative direction, of our
findings. For the sake of clarity and ease of interpretation, we focus on the setting where consumers
view and select from the recommendation set. Future research could explore the heterogeneous
welfare impacts of recommender systems and pricing strategies on various types of consumers.
Finally, it is worth noting that translating the economic research of recommender systems into
their technical designs necessitates additional efforts (Li and Tuzhilin 2024b, Wang et al. 2024,
Bi et al. 2024, Li et al. 2023). Although this endeavor is beyond the scope of the present study,
we encourage algorithm designers in both academia and industry to recognize and account for the
strategic pricing decisions enabled by AI-driven pricing algorithms. By doing so, they can develop
algorithms that enhance both the overall welfare and the equitable distribution of benefits among
stakeholders.

Xu, Lee, and T an:Algorithmic Collusion or Competition
36 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
References
Adomavicius G, Tuzhilin A (2005) Toward the next generation of recommender systems: A survey of the state-
of-the-art and possible extensions. IEEE transactions on knowledge and data engineering 17(6):734–749.
Agrawal A, Gans J, Goldfarb A (2019) The economics of artificial intelligence: an agenda (University of
Chicago Press).
Ak¸ sin Z, Ata B, Emadi SM, Su CL (2013) Structural estimation of callers’ delay sensitivity in call centers.
Management Science 59(12):2727–2746.
Assad S, Clark R, Ershov D, Xu L (2020) Algorithmic pricing and competition: Empirical evidence from the
german retail gasoline market .
Athey S, Bagwell K, Sanchirico C (2004) Collusion and price rigidity. The Review of Economic Studies
71(2):317–349.
Baker JB (2019) The antitrust paradigm: Restoring a competitive economy (Harvard University Press).
Banchio M, Skrzypacz A (2022) Artificial intelligence and auction design. Proceedings of the 23rd ACM
Conference on Economics and Computation , 30–31.
Bi X, Yang M, Adomavicius G (2024) Consumer acquisition for recommender systems: A theoretical frame-
work and empirical evaluations. Information Systems Research 35(1):339–362.
Boussioux L, Lane JN, Zhang M, Jacimovic V, Lakhani KR (2024) The crowdless future? generative ai and
creative problem-solving. Organization Science 35(5):1589–1607.
Brynjolfsson E, Li D, Raymond LR (2023) Generative ai at work. Technical report, National Bureau of
Economic Research.
Calder-Wang S, Kim GH (2023) Coordinated vs efficient prices: The impact of algorithmic pricing on mul-
tifamily rental markets. Available at SSRN 4403058 .
Calvano E, Calzolari G, Denicol` o V, Harrington Jr JE, Pastorello S (2020a) Protecting consumers from
collusive prices due to ai. Science 370(6520):1040–1042.
Calvano E, Calzolari G, Denicolo V, Pastorello S (2020b) Artificial intelligence, algorithmic pricing, and
collusion. American Economic Review 110(10):3267–3297.
Chen L, Mislove A, Wilson C (2016) An empirical analysis of algorithmic pricing on amazon marketplace.
Proceedings of the 25th international conference on World Wide Web , 1339–1349.
Chung JH, Chintagunta P, Misra S (2024) Simulated maximum likelihood estimation of the sequential search
model. Quantitative Marketing and Economics 1–60.
Colangelo G (2021) Artificial intelligence and anticompetitive collusion: From the ‘meeting of minds’ towards
the ‘meeting of algorithms’ ? TTLF Stanford Law School Working Paper .
Colliard JE, Foucault T, Lovo S (2022) Algorithmic pricing and liquidity in securities markets. HEC Paris
Research Paper .

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 37
Colombo S (2013) Product differentiation and collusion sustainability when collusion is costly. Marketing
Science 32(4):669–674.
Compiani G, Lewis G, Peng S, Wang P (2024) Online search and optimal product rankings: An empirical
framework. Marketing Science 43(3):615–636.
Derakhshan M, Golrezaei N, Manshadi V, Mirrokni V (2022) Product ranking on online platforms. Manage-
ment Science 68(6):4024–4041.
Dou WW, Goldstein I, Ji Y (2024) Ai-powered trading, algorithmic collusion, and price efficiency. Jacobs
Levy Equity Management Center for Quantitative Financial Research Paper .
Feldman J, Zhang DJ, Liu X, Zhang N (2022) Customer choice models vs. machine learning: Finding optimal
product displays on alibaba. Operations Research 70(1):309–328.
Ferreira KJ, Parthasarathy S, Sekar S (2022) Learning to rank an assortment of products. Management
Science 68(3):1828–1848.
Fleder D, Hosanagar K (2009) Blockbuster culture’s next rise or fall: The impact of recommender systems
on sales diversity. Management science 55(5):697–712.
Fzrachi A, Stucke ME (2019) Sustainable and unchallenged algorithmic tacit collusion.Nw. J. Tech. & Intell.
Prop. 17:217.
Gao J, Wang D (2024) Quantifying the use and potential benefits of artificial intelligence in scientific research.
Nature Human Behaviour 1–12.
Guo H, Yu J, Liu Q, Tang R, Zhang Y (2019) Pal: a position-bias aware learning framework for ctr prediction
in live recommender systems. Proceedings of the 13th ACM Conference on Recommender Systems ,
452–456.
Hofmann K, Schuth A, Bellogin A, De Rijke M (2014) Effects of position bias on click-based recommender
evaluation. Advances in Information Retrieval: 36th European Conference on IR Research, ECIR 2014,
Amsterdam, The Netherlands, April 13-16, 2014. Proceedings 36 , 624–630 (Springer).
Hong H, Shum M (2006) Using price distributions to estimate search costs.The RAND Journal of Economics
37(2):257–275.
Jeunen O, Goethals B (2021) Top-k contextual bandits with equity of exposure. Proceedings of the 15th
ACM Conference on Recommender Systems , 310–320.
Lee D, Hosanagar K (2019) How do recommender systems affect sales diversity? a cross-category investigation
via randomized field experiment. Information Systems Research 30(1):239–259.
Lee D, Hosanagar K (2021) How do product attributes and reviews moderate the impact of recommender
systems through purchase stages? Management Science 67(1):524–546.
Li L, Chen J, Raghunathan S (2018) Recommender system rethink: Implications for an electronic marketplace
with competing manufacturers. Information Systems Research 29(4):1003–1023.

Xu, Lee, and T an:Algorithmic Collusion or Competition
38 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
Li L, Chen J, Raghunathan S (2020) Informative role of recommender systems in electronic marketplaces:
A boon or a bane for competing sellers. MIS Quarterly 44(4).
Li P, Tuzhilin A (2024a) Deep pareto reinforcement learning for multi-objective recommender systems.arXiv
preprint arXiv:2407.03580 .
Li P, Tuzhilin A (2024b) When variety seeking meets unexpectedness: Incorporating variety-seeking behaviors
into design of unexpected recommender systems. Information Systems Research 35(3):1257–1273.
Li P, Wang Y, Chi EH, Chen M (2023) Hierarchical reinforcement learning for modeling user novelty-seeking
intent in recommender systems. arXiv preprint arXiv:2306.01476 .
Li SE (2023) Reinforcement learning for sequential decision and optimal control (Springer).
Li X, Grahl J, Hinz O (2022) How do recommender systems lead to consumer purchases? a causal mediation
analysis of a field experiment. Information Systems Research 33(2):620–637.
Liu Y, Lou B, Zhao X, Li X (2024) Unintended consequences of advances in matching technologies: Informa-
tion revelation and strategic participation on gig-economy platforms. Management Science 70(3):1729–
1754.
Maslej N, Fattorini L, Brynjolfsson E, Etchemendy J, Ligett K, Lyons T, Manyika J, Ngo H, Niebles JC,
Parli V, et al. (2023) Artificial intelligence index report 2023. arXiv preprint arXiv:2310.03715 .
Mikl´ os-Thal J, Tucker C (2019) Collusion by algorithm: Does better demand prediction facilitate coordination
between sellers? Management Science 65(4):1552–1561.
Mnih V, Kavukcuoglu K, Silver D, Rusu AA, Veness J, Bellemare MG, Graves A, Riedmiller M, Fidje-
land AK, Ostrovski G, et al. (2015) Human-level control through deep reinforcement learning. nature
518(7540):529–533.
Moraga-Gonz´ alez JL, S´ andor Z, Wildenbeest MR (2023) Consumer search and prices in the automobile
market. The Review of Economic Studies 90(3):1394–1440.
Morozov I, Seiler S, Dong X, Hou L (2021) Estimation of preference heterogeneity in markets with costly
search. Marketing Science 40(5):871–899.
Mortensen DT (2011) Markets with search friction and the dmp model. American Economic Review
101(4):1073–1091.
Narahari Y, Garg D, Narayanam R, Prakash H (2009) Game theoretic problems in network economics and
mechanism design solutions (Springer Science & Business Media).
Peng S, Kalliamvakou E, Cihon P, Demirer M (2023) The impact of ai on developer productivity: Evidence
from github copilot. arXiv preprint arXiv:2302.06590 .
Robertson VH (2022) Antitrust law and digital markets: a guide to the european competition law experience
in the digital economy .

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 39
Rocher L, Tournier AJ, de Montjoye YA (2023) Adversarial competition and collusion in algorithmic markets.
Nature Machine Intelligence 5(5):497–504.
Salcedo B (2015) Pricing algorithms and tacit collusion. Manuscript, Pennsylvania State University .
Schwalbe U (2018) Algorithms, machine learning, and collusion. Journal of Competition Law & Economics
14(4):568–607.
Silver D, Huang A, Maddison CJ, Guez A, Sifre L, Van Den Driessche G, Schrittwieser J, Antonoglou I,
Panneershelvam V, Lanctot M, et al. (2016) Mastering the game of go with deep neural networks and
tree search. nature 529(7587):484–489.
Silver D, Hubert T, Schrittwieser J, Antonoglou I, Lai M, Guez A, Lanctot M, Sifre L, Kumaran D, Graepel
T, et al. (2018) A general reinforcement learning algorithm that masters chess, shogi, and go through
self-play. Science 362(6419):1140–1144.
Spann M, Bertini M, Koenigsberg O, Zeithammer R, Aparicio D, Chen Y, Fantini F, Jin GZ, Morwitz V,
Leszczyc PP, et al. (2024) Algorithmic pricing: Implications for consumers, managers, and regulators.
Technical report, National Bureau of Economic Research.
Thomadsen R, Rhee KE (2007) Costly collusion in differentiated industries. Marketing Science 26(5):660–
665.
Train KE (2009) Discrete choice methods with simulation (Cambridge university press).
Tyagi RK (1999) On the relationship between product substitutability and tacit collusion. Managerial and
Decision Economics 20(6):293–298.
Ursu R, Seiler S, Honka E (2023) The sequential search model: A framework for empirical research. Available
at SSRN 4236738 .
Ursu RM (2018) The power of rankings: Quantifying the effect of rankings on online consumer search and
purchase decisions. Marketing Science 37(4):530–552.
Van Hasselt H, Guez A, Silver D (2016) Deep reinforcement learning with double q-learning. Proceedings of
the AAAI conference on artificial intelligence , volume 30.
Wan X, Kumar A, Li X (2024) How do product recommendations help consumers search? evidence from a
field experiment. Management Science 70(9):5776–5794.
Wang Q, Huang Y, Singh PV, Srinivasan K (2023a) Algorithms, artificial intelligence and simple rule based
pricing. Available at SSRN 4144905 .
Wang W, Li B, Luo X, Wang X (2023b) Deep reinforcement learning for sequential targeting. Management
Science 69(9):5439–5460.
Wang Y, Tao L, Zhang XX (2024) Recommending for a multi-sided marketplace: A multi-objective hierar-
chical approach. Marketing Science .
Watkins CJCH (1989) Learning from delayed rewards .

Xu, Lee, and T an:Algorithmic Collusion or Competition
40 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
Weitzman M (1979) Optimal search for the best alternative. Econometrica 47(3):641–654.
Wieting M, Sapi G (2021) Algorithms in the marketplace: An empirical analysis of automated pricing in
e-commerce. Available at SSRN 3945137 .
Zhang J, Yang M, Bi X, Wei Q (2024) Algorithmic governance via recommender systems: The case of short
video platform. Available at SSRN 4572513 .
Zhang S, Yao L, Sun A, Tay Y (2019) Deep learning based recommender system: A survey and new per-
spectives. ACM computing surveys (CSUR) 52(1):1–38.
Zhang X, Ferreira P, Godinho de Matos M, Belo R (2021) Welfare properties of profit maximizing recom-
mender systems: Theory and results from a randomized experiment. MIS Quarterly 45(1).
Zhou B, Zou T (2023) Competing for recommendations: The strategic impact of personalized product rec-
ommendations in online marketplaces. Marketing Science 42(2):360–376.
Zhou M, Zhang J, Adomavicius G (2023) Longitudinal impact of preference biases on recommender systems’
performance. Information Systems Research .

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 41
Appendix A: Consumer Search and Purchase Process
Figure A1 Consumer Search and Purchase Process

Xu, Lee, and T an:Algorithmic Collusion or Competition
42 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
Appendix B: Alternative Economic Environment: Logit Demand
To align our proposed structural search model with the traditional algorithmic collusion literature (Calvano
et al. 2020b), which typically employs the canonical logit model, we also evaluate our results using the
logit model as a robustness check. In fact, the logit demand model can be considered a restricted version
derived from the sequential search model. Specifically, from the sequential search model, we can (1) set
the search cost to zero instead of allowing it to take any value estimated from data, (2) assume that all
recommended products’ full information is available to consumers, thereby eliminating position bias under
this full information perspective (a natural consequence of (1)), and (3) change the distribution of taste
shocks from a normal distribution to a type-I extreme value distribution to facilitate a closed-form expression
of the choice probability as a logit function. This modification yields the logit choice model when a consumer
i sees a recommendation set:
dt i,j = e
vj −pt j
µ
P
k∈Bi e
vk −pt k
µ + e
v0
µ
(16)
Here, the parameters vj represent representative utility for each product j, capturing vertical differentia-
tion. The parameter µ reflects the degree of horizontal differentiation where perfect substitution is achieved
as µ approaches 0. The denominator of the equation represents the exponential sum over all products’
consumption utilities within the recommendation set Bi along with the outside good, characterized by the
quality index v0. Furthermore, under the assumption that all consumers are homogeneous in their observable
preferences and differ solely in their idiosyncratic taste shocks, the above single-individual choice probability
also characterizes the demand for product j when a unit of consumers is presented with the recommendation
set Bi.
In alignment with our primary framework, we continue to address a two-out-of-three recommendation
scenario. In the absence of position bias within this logit demand model, product ranking does not influence
consumer behavior, thereby reducing the platform’s task to an assortment optimization problem. Further-
more, since consumers are perceived as homogeneous by the platform, it is sufficient to construct a single
recommendation set that either maximizes revenue or maximizes consumer utility to all consumers.
Table B1 Price, Revenue, and Utility Comparison (Logit Demand Model)
Revenue-
Maximization
Utility-
Maximization
Baseline
Prices 0.8829 (0.0051) 0.3071 (0.0194) 0.5553 (0.0128)
Revenue 0.2243 (0.0002) 0.0703 (0.0046) 0.1630 (0.0033)
Utility 0.3543 (0.0012) 0.9525 (0.0150) 0.6499 (0.0117)
The expected revenue for each recommendation set can be computed as:
rBi =
X
j∈Bi
pt j · exp

vj −pt j
µ

P
k∈Bi exp

vk−pt k
µ

+ exp

v0
µ
 (17)

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 43
Conversely, the expected utility for a recommendation set is calculated using the welfare formula (Train
2009):
T UBi =
X
k∈Bi
exp
 vk − pt k
µ

+ exp
 v0
µ

(18)
We adhere to the game sequence outlined in Algorithm 1 of Section 3.1 and employ Q-learning pricing
algorithms with consistent parameters. We normalize the valuations vj of all products to 1 and set the
outside option valuation v0 to 0, allowing prices to fluctuate between 0 and 1. After conducting 50 simulation
trials, each spanning 3,000,000 periods, we present the equilibrium prices, revenue, and utility in a manner
consistent with Section 5.
As illustrated in Table B1, the comparisons across the three cases are qualitatively similar to our main
results, thereby reinforcing the robustness of our findings across different demand model specifications.

Xu, Lee, and T an:Algorithmic Collusion or Competition
44 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
Appendix C: Alternative Economic Environment: Heterogeneous Logit Demand
In Appendix B, we employ a logit demand model that does not incorporate customer segmentation (Calvano
et al. 2020b). In this appendix, we extend the economic environment by introducing heterogeneous customer
types and subsequently adapt the recommender systems to optimize for different customer categories.
Specifically, we allow each consumer to possess heterogeneous outside option values. To illustrate, we assign
half of the consumers a higher outside option value of v0 = 0.25, while the remaining consumers have a lower
outside option value of v0 = 0. For each segment, we recommend the set that maximizes either expected
revenue or expected utility. With all other settings held constant, we present the results in Table C1.
Notably, the primary findings remain consistent under this modified setting. When the recommender
system is configured for revenue maximization, sellers tend to engage in more collusive behavior, resulting
in elevated equilibrium prices (0.7979) and increased revenue (0.1907) at the expense of consumer utility
(0.4563). Conversely, when the system prioritizes the maximization of consumer utility, the equilibrium is
characterized by lower prices (0.5229) and enhanced consumer utility (0.6925), alongside a reduction in seller
revenue (0.1469).
Table C1 Price, Revenue, and Utility Comparison (Heterogeneous Logit Demand Model)
Revenue-
Maximization
Utility-
Maximization
Baseline
Prices 0.7979 (0.0086) 0.3075 (0.0189) 0.5229 (0.0105)
Revenue 0.1907 (0.0004) 0.0659 (0.0039) 0.1469 (0.0024)
Utility 0.4563 (0.0050) 0.9666 (0.0131) 0.6925 (0.0091)

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 45
Appendix D: Empirical Data Description and Summary Statistics
In this appendix, we detail the construction of our dataset for structural estimation, basically following the
steps taken in Chung et al. (2024) and Ursu (2018). The original Expedia dataset contains millions of search
impressions, including query information and all displayed hotels. Because the dataset is divided into training
and test sets, and the test set lacks consumer decision data (search or purchase), we focus exclusively on the
training set.
We apply the following filtering procedures to the training set:
1. Exclude search impressions that include any hotels with extreme prices (less than $10 or more than
$1,000).
2. For search impressions that led to transactions, infer the tax from the total spending and displayed
prices, and exclude those impressions where the inferred tax is less than $1 or exceeds 30% of the price.
3. Drop search impressions containing any missing values (NaN) in query or hotel attributes.
4. Exclude search impressions based on Expedia’s ranking rather than the random ranking.
5. Segment the dataset by travel destination, recognizing that consumers and hotels may vary significantly
across destinations, and focus on the destination with the highest volume of search impressions (destination
ID 8192).
6. Although most impressions have similar lengths (number of hotels displayed), there are outliers. For
the selected destination, the number of hotels per impression ranges from 5 to 35, with the 25th percentile
at 29. Therefore, we restrict our analysis to search impressions with lengths greater than 29 14.
The final dataset comprises 1,067 impressions and 34,702 observations, where each observation represents a
hotel option within a search impression. It includes hotel information, query information (customer attributes
constant across different hotels within one search impression), and final decisions (search or purchase).
Additionally, we add an outside option for each search impression, coded as a purchase decision equal to
one if the customer does not buy from any displayed hotel and zero otherwise. Thus, for the structural
estimation, the total number of observations is 35,769 (34,702 hotel options plus 1,067 outside options). For
34,702 hotel options, the variable descriptions and summary statistics are provided in Table D1.
14 This is slightly less stringent than Ursu (2018), which only uses the two most frequently occurring search impression
lengths.

Xu, Lee, and T an:Algorithmic Collusion or Competition
46 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
Table D1 Variable Description and Summary Statistics
V ariable Description Mean Std Min Max
Price ($100) Price of the hotel ( $100) 1.4326 0.9026 0.1700 9.8400
HotelStars The star rating of the hotel 3.9291 0.8633 2 5
HotelReview Average customer review rating 4.0370 0.4901 3 5
Brand A binary indicator of chained hotel 0.7872 0.4093 0 1
HotelLocationScore A score of location desirability 4.0328 0.3011 3.0400 4.3800
Promo A binary indicator of promotion 0.5919 0.4915 0 1
ReqRoomNum Number of rooms required 1.1414 0.4151 1 4
SatNight A binary indicator of Saturday
night involved in travel
0.4752 0.4994 0 1
Click A binary indicator of whether the
customer search the hotel
0.0370 0.1888 0 1
Tran A binary indicator of whether the
customer book the hotel
0.0026 0.0511 0 1

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 47
Appendix E: Alternative Pricing Algorithm: More Exploration
In our primary analyses, we demonstrate that prices increase (decrease) under conditions where product
exposure is governed by revenue-maximizing (utility-maximizing) recommender systems. As illustrated in
Figure 1, the algorithms’ exploration process appears to alter only the magnitude of price changes rather
than their direction across the three different scenarios examined. Nevertheless, it remains plausible that
extended and more comprehensive exploration could yield different outcomes, such as the algorithms learning
to collude even in the presence of utility-maximizing recommender systems. Therefore, in this appendix, we
investigate the effects of increased exploration on price dynamics and equilibrium outcomes.
Using an ϵ-greedy algorithm, the exploration rate, denoted by ϵ, modulates the probability of undertaking
a stochastic action at each temporal interval according to the equation ϵ = e−ωt. This probability undergoes
exponential decay, governed by both the decay rate ω and the time parameter t. Extended exploration peri-
ods enable the algorithm to obtain more accurate estimates of the optimal pricing strategy; however, they
also incur higher opportunity costs due to the exploration of suboptimal pricing alternatives. In our baseline
configuration, the decay rate ω is set to 1.5 × 10−6. In contrast, this appendix explores a “More Exploration”
scenario, wherein we employ a substantially smaller decay rate of ω = 5× 10−8, thereby significantly increas-
ing exploratory activities. For example, after three million periods, the pricing algorithms in the baseline
configuration retain an approximate probability of 1 .11% for opting for a stochastic action. In contrast, in
the “More Exploration” scenario, this probability remains above 80%.
To ensure experimental consistency, all parameters remain identical to those in the baseline configuration,
with the sole modification being the exploration rate parameter ω. We conduct 20 simulation runs, each
spanning 80,000,000 periods, after which the exploration probability falls below 1%. The resulting average
equilibrium prices and profits are presented in Table E1, while the temporal evolution of the learning dynam-
ics is depicted in Figure E1. Notably, the equilibrium prices attained in the “More Exploration” scenario
exhibit substantial congruence with those observed in the baseline scenario. Specifically, compared to the
equilibrium price of 1.6861 observed in the baseline condition, the implementation of revenue-maximizing
recommender systems results in an elevated price of 2.3734. Conversely, the deployment of utility-maximizing
recommender systems leads to a reduced price of 1.6861. Furthermore, the learning dynamics of the pricing
algorithms, influenced by the different types of recommender systems, continue to progress monotonically
toward their respective equilibria, in alignment with the objectives of the respective recommender systems.

Xu, Lee, and T an:Algorithmic Collusion or Competition
48 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
Table E1 Price, Revenue, and Utility Comparison ( µ = 0.25, ω = 5× 10−8)
Revenue-
Maximization
Utility-
Maximization
Baseline
Prices 2.3734 (0.0225) 0.8260 (0.0665) 1.6861 (0.0463)
Revenue 0.2578 (0.0006) 0.1067 (0.0052) 0.2165 (0.0028)
Utility 0.3746 (0.0017) 0.6664 (0.0078) 0.4740 (0.0062)
(a) Revenue-Maximization RS
 (b) Utility-Maximization RS
(c) Baseline
Figure E1 Learning Dynamics ( µ = 0.25, ω = 5× 10−8)
Note: The points on the continuous lines depict the moving average, with a window size of
10000, of the average price observed across 20 experiments at each t. The shaded region’s
upper and lower limits indicate the highest and lowest values occurring within the window.

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 49
Appendix F: Alternative Pricing Algorithm: Multi-armed Bandit
Q-learning inherently incorporates a forward-looking component through its state transitions. To assess the
robustness of our findings, we relax the forward-looking assumption by modeling the algorithms as basic
multi-armed bandits. Instead of constructing a Q-table of size |S| × |P | to record the rewards of various
pricing decisions under different states (i.e., past pricing outcomes), we now construct a reward table of
size 2 × |P |, which tracks the number of times each pricing decision (arm) has been attempted and the
corresponding average reward for each arm. We maintain an initially empty reward table for each pricing
agent (seller) and allow each seller to learn to set prices through sampling. Consistent with our Q-learning
approach, we employ an ϵ-greedy sampling strategy with the same exploration rate.
We follow the simultaneous game sequence once more and present the equilibrium results in Table F1 and
the price dynamics in Figure F1. Notably, the results remain largely consistent with our primary findings.
This consistency arises because our core mechanism relies on the recommender system’s influence on the
pricing agents’ rewards, making forward-looking behavior an unnecessary condition for the pricing algorithms
to produce the observed outcomes.
Table F1 Price, Revenue, and Utility Comparison Across Objectives (MAB)
Revenue-
Maximization
Utility-
Maximization
Baseline
Prices 2.3393 (0.0149) 0.9881 (0.0118) 1.6596 (0.0057)
Revenue 0.2576 (0.0003) 0.1544 (0.0013) 0.2195 (0.0007)
Utility 0.3805 (0.0015) 0.6118 (0.0018) 0.4753 (0.0010)

Xu, Lee, and T an:Algorithmic Collusion or Competition
50 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
(a) Revenue-Maximization RS
 (b) Utility-Maximization RS
(c) Baseline
Figure F1 Learning Dynamics (MAB)
Note: The points on the continuous lines depict the moving average, with a window size of
1000, of the average price observed across 50 experiments at each t. The shaded region’s upper
and lower limits indicate the highest and lowest values occurring within the window.

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 51
Appendix G: Alternative Pricing Objective of Sellers
In Calvano et al. (2020b), sellers are assumed to optimize revenue. When sellers maximize revenue, they
must balance a trade-off between demand and per-sale revenue: setting lower prices can boost demand but
reduce revenue per sale, whereas setting higher prices can increase revenue per sale but suppress demand.
In such contexts, sellers may engage in price undercutting, thereby intensifying price competition.
Accordingly, starting from the Bertrand game, most studies in industrial organization and traditional game
theory assume that sellers aim to maximize revenue, ensuring meaningful competitive dynamics (Narahari
et al. 2009). By contrast, if a seller instead sought to maximize demand (or consumer utility), it could
simply set its price to zero, regardless of competitors’ prices, thereby removing any incentive for strategic
interactions.
Despite these considerations, we show that recommender systems retain their influence even when sellers
optimize demand and willingly offer the lowest possible prices. To illustrate this, we modify the seller’s
objective to demand maximization and rerun our numerical experiments. As reported in Table I1, both
the utility-maximizing and the baseline scenarios produce the lowest possible prices. Nevertheless, when the
platform pursues revenue maximization, it still induces sellers to sustain relatively higher prices. In fact, these
prices even exceed the equilibrium levels observed under baseline conditions with revenue-driven sellers. This
finding further emphasizes the pivotal role of recommender systems in shaping algorithmic pricing strategies.
Furthermore, when some sellers prioritize demand while others focus on revenue maximization, an asym-
metric equilibrium might emerge. For example, consider a scenario in which one seller aims to maximize
demand and two sellers aim to maximize revenue, with the recommender system oriented towards utility
maximization. In this case, the utility-driven seller reduces its price to the lowest possible level, while the
revenue-driven sellers converge to slightly higher prices, though these prices remain lower than those observed
in the baseline scenario. Due to the vast number of possible combinations, we do not present all these results
here. However, from all these interesting asymmetric equilibria, we consistently observe the influential role
of recommender systems across various configurations.
Table G1 Price, Revenue, and Utility Comparison Across Objectives (Demand-Driven Sellers)
Revenue-
Maximization
Utility-
Maximization
Baseline
Prices 1.8128 (0.0062) 0.5109 (0.0103) 0.5109 (0.0103)
Revenue 0.2389 (0.0002) 0.0901 (0.0001) 0.0914 (0.0005)
Utility 0.4449 (0.0005) 0.6974 (0.0004) 0.6654 (0.0032)

Xu, Lee, and T an:Algorithmic Collusion or Competition
52 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
Appendix H: Alternative Game Sequence: Asynchronous Pricing Game
In our primary analyses, we adhere to the framework established by Calvano et al. (2020b), assuming that
all sellers make pricing decisions simultaneously. While this assumption underpins our main analyses, we
revisit and relax it in this section.
If we permit sellers to update their pricing decisions sequentially—following the order of seller 1, seller
2, seller 3, and so forth—the decision-making process unfolds as follows: seller 1 updates, followed by seller
2 and then seller 3. Considering the structure of Q-learning, seller 1 observes the prices from the preced-
ing three periods before making a decision. Afterwards, the environment changes in the subsequent two
periods following seller 1’s decision. By aggregating these three periods into a single “macro” period, the
scenario reverts to the simultaneous decision-making framework. Therefore, from a theoretical standpoint,
an asynchronous game sequence does not significantly alter the nature of the algorithmic pricing game.
This reasoning similarly applies to settings where multi-armed bandits (MAB) serve as the pricing algo-
rithms. For the sake of comparison, we present the results of the MAB approach under the aforementioned
asynchronous game in Table H1. As anticipated, these results are largely consistent with those reported in
Appendix F, thereby reinforcing the robustness of our findings. The same consistency is observed in the
Q-learning based pricing game.
Table H1 Price, Revenue, and Utility Comparison Across Objectives (Asynchronous)
Revenue-
Maximization
Utility-
Maximization
Baseline
Prices 2.3566 (0.0147) 0.9677 (0.0081) 1.6598 (0.0062)
Revenue 0.2578 (0.0003) 0.1513 (0.0004) 0.2195 (0.0007)
Utility 0.3783 (0.0015) 0.6162 (0.0005) 0.4753 (0.0010)

Xu, Lee, and T an:Algorithmic Collusion or Competition
Article submitted toManagement Science; manuscript no. MS-0000-0000.00 53
Appendix I: Alternative Recommendation Objective: T otal Demand
It is worth noting that demand can serve as another plausible objective for the platform. Economically,
demand is analogous to utility, since higher utility increases consumers’ purchase probability and, conse-
quently, overall demand. To maintain conceptual clarity and alignment with the existing literature, we pri-
marily focus on revenue and consumer utility in our main analyses, while nonetheless examining demand as
an alternative objective here. Specifically, we substitute the platform’s objective with total market demand,
keeping all other aspects of the recommender system unchanged.
We conduct two sets of numerical experiments, one with revenue-driven sellers and another with demand-
driven sellers, both operating under a demand-maximizing recommender system. As reported in Table I1,
our rationale holds. Under the standard revenue-driven pricing framework, the equilibrium price settles at
a level lower than the baseline scenario (see Table 3 for comparison). When sellers optimize demand, as
expected, the price converges to its minimum possible level, consistent with the outcomes shown in Table
G1.
Table I1 Price, Revenue, and Utility Comparison Across Different Pricing Objectives
Revenue-Driven Sellers Demand-Driven Sellers
Prices 1.0992 (0.0101) 0.5109 (0.0103)
Revenue 0.1726 (0.0008) 0.0930 (0.0007)
Utility 0.5633 (0.0013) 0.6717 (0.0002)

Xu, Lee, and T an:Algorithmic Collusion or Competition
54 Article submitted toManagement Science; manuscript no. MS-0000-0000.00
Appendix J: Alternative Recommendation Objective: W eighted Average
It is worth noting that, in practice, platforms may adopt a mixed objective to balance the welfare of both
sellers (revenue) and consumers (utility). To illustrate how varying the weight assigned to these two objectives
influences the pricing dynamics, we examine five different cases with weights ranging from 0 (pure utility
maximization) to 1 (pure revenue maximization) and conduct corresponding numerical experiments. Our
findings indicate that as the weight increases, equilibrium prices and sellers’ revenues also increase, while
consumer utility gradually decreases. Given the monotonic relationship between the weights and equilibrium
prices, we infer that when the weight is set between 0.25 and 0.5, the equilibrium price aligns with the
baseline scenario (with no optimization, as shown in Table 3). This result further underscores the pivotal
role of platform recommendations in shaping market outcomes.
Table J1 Price, Revenue, and Utility Comparison Across Objectives (Different Weights)
W eight 0 0.25 0.5 0.75 1
Prices 0.9095
(0.0478)
1.4257
(0.0062)
2.1463
(0.0168)
2.2925
(0.0188)
2.3844
(0.0137)
Revenue 0.1174
(0.0041)
0.2079
(0.0009)
0.2468
(0.0004)
0.2566
(0.0004)
0.2583
(0.0003)
Utility 0.6506
(0.0063)
0.5388
(0.0010)
0.4284
(0.0014)
0.3940
(0.0016)
0.3749
(0.0012)
