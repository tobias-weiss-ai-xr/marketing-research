---
title: Privacy-Aware Adaptive Diffusion-Propensity Mapping for E-Commerce Advertising Targeting
url: https://doi.org/10.21203/rs.3.rs-11009842/v1
category: privacy-data
subcategory: empirical
date: 2026-09
venue: Research Square
authors:
- Shridul Gupta
source: openalex-oa
pdf_url: https://www.researchsquare.com/article/rs-11009842/latest.pdf
pages: 24
chars: 82771
fetched_at: '2026-11-08T17:47:14+00:00'
kb_version: 1
---

# Privacy-Aware Adaptive Diffusion-Propensity Mapping for E-Commerce Advertising Targeting

Privacy-Aware Adaptive Diffusion-Propensity Mapping for
E-Commerce Advertising Targeting
Shridul Gupta 
Maharaja Agrasen Institute of Management Studies
Research Article
Keywords: social network measurement, adaptive advertising, creator targeting, network brokerage, privacy-aware
modeling, e-commerce
Posted Date: September 30th, 2026
DOI: https://doi.org/10.21203/rs.3.rs-11009842/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.   Read Full License
Additional Declarations: No competing interests reported.
Page 1/24

Abstract
This study develops and tests a framework for e-commerce advertising that combines privacy preserving techniques and
adaptive social sway mapping. The framework utilizes social network structures, ads engagement, campaign relevance,
and community redundancy to enhance seed selection in different market conditions. A public benchmark of 117
creators is converted to an aﬃliation network. Here, ties represent shared content categories and audience countries.
Estimators of network centrality, brokerage, and clustering are computed and implemented in 1,000 contexts of
advertisement campaigns. Four advertising allocation policies are used: targeting based on follower size, targeting based
only on engagement, targeting using the brokerage of a static network, and context-adaptive targeting of the network.
The adaptive policy sequentially selects ﬁve creators using a sway score with a redundancy penalty. The empirical
analysis reveals that follower count has a negative relationship with average engagement and that shortest-path
brokerage is positively related to engagement. The adaptive policy generates an average qualiﬁed engagement of
13.98 million or 23.49 percent compared to the engagement-only policy and an average of 122.98 percent and 110.69
percent, respectively, compared to the policies of follower-size targeting and static network targeting. In simulated
campaigns, the superiority of the adaptive policy is validated through paired parametric and nonparametric tests. A
privacy-stress test is performed by applying Laplace perturbation to bounded sway scores. At epsilon 1 the system
retains 94.10 percent of the value of adaptive decisions. The estimates show that the combination of structural
brokerage, context ﬁt, and redundancy control, when used in the order of time, yield better advertising intelligence than
when used as separate measures. The study adds a reproducible decision framework connecting network science,
marketing quantitative modeling, and privacy-aware selection while distinguishing the ad value in modeled decisions
from the ad value recorded sales or purchase-response estimates.
1. Introduction
As data usage expands in advertising, so do the data-points used to target users. Businesses now have to factor in how
users’ attention is distributed across many connected networks. Campaigns may reach the same users multiple times in
the form of dense user clusters, billboard accounts whose popularity (judged by high follower counts) is overestimated
and doesn’t warrant high levels of engagement, and fast-moving groups that aren’t sustainable. The pattern poses a
problem of networks when designing an advertising campaign. The strategies used for social network analysis help
describe what it means to be structurally central in a network and the broker and community framework, for which
scholarship in marketing is useful. The seed of an idea, word of mouth, and personalized campaigns all affect marketing
practices (Hinz et al., 2011; Trusov et al., 2009). The unanswered question in marketing is how these ideas can be
combined in a generalized framework rather than a best-practices approach.
One advantage of the static popularity heuristic is that evaluating user accounts is straightforward, but the literature is
clear that “popular” users are not more likely to engage with an advertisement. Large scale diffusion research shows that,
in the past, audience size and diffusive tendencies were imperfectly correlated and that successful, cost-effective
diffusion is attributable to a collection of “ordinary” users rather than a sole high-proﬁle user (Bakshy et al., 2011). In this
research, large follower accounts may overestimate a user’s popularity and may not be correlated with opinion
leadership. The ﬁt of the user and product is critical in this relationship (De Veirman et al., 2017). Network science adds a
complementary inference: a node's value is not solely about the number of contacts it has. It is about the pathways and
communities it connects. For this reason, brokerage centrality and other brokerage concepts are useful for advertising.
They identify accounts capable of spanning disconnected parts of an opportunity space (Borgatti, 2005; Burt, 2004).
The ability to adapt has gained importance as change and innovations in social media and data infrastructure happen.
Recent research on temporal diffusion maximization treats activation probabilities and topology as time dependent and
expects that improving network state rather than assuming it is constant leads to better selection of seeds (Meena et al.,
2025). Decentralized Open Networks are the main focus of recent scholarship, which sets a precedent and establishes
Page 2/24

the size and value of such platforms to academia. Quelle and Bovet (2025) studied a Bluesky network with roughly
5 million users and mentioned the network's user friendliness towards academia. Smith et al. (2026) made A Blue Start, a
public data resource containing 39.7 million accounts, 2.4 billion following relations and about 365.8 thousand user-
curated starter packs publicly available. These advances won't completely solve the access and interoperability issues
that commercial advertisers deal with, but they will make it possible to test temporal network science on public assets
instead of simply proprietary platform data.
Privacy should always go hand in hand with adaptive and personalized advertising. There is a trade-off that needs to be
made between privacy and advertising. Increasing privacy can decrease the response to advertising, but can also
increase the control that users perceive they have over their data. Privacy is an important part of advertising control, and
can change how users and consumers perceive advertising compliance (Tucker, 2014). Privacy and data regulation can
have considerable negative effects on the performance of advertising (Goldfarb and Tucker, 2011). Complexities of
privacy economics relate to asymmetric information and context and the trade-offs of welfare, which go beyond the
dichotomy of data processing and data protection (Acquisti et al., 2016). The Digital Personal Data Protection Act, 2023,
and the Digital Personal Data Protection Rules, 2025, introduce a phased statutory framework for the processing of
digital personal data in India, which stipulates provision of notice, obtaining of consent, and providing security and
accountability. A publication-centric advertising framework therefore, must deﬁne decision value and must not advocate
the false notion that any application of public social data is intrinsically unconstrained.
This study aims to provide a solution to this issue by employing a deliberately open design. It repurposes an openly
available, advertising-oriented creator benchmark to a market-aﬃliation network based on shared content categories and
dominant audience countries. The network will not be represented as a recorded follower graph. Instead, it is designed to
model proximity in an advertising opportunity space. Two creators will be in a more structurally closer position if they
compete for or provide access to the same market segments. The network is analyzed in conjunction with recorded
engagement. Four policies for selecting seeds are explored in 1,000 reproduced contexts: follower size, engagement,
static network brokerage, and a combined context-sensitive policy consisting of recorded engagement, structural
brokerage, relevance to the campaign, and a redundancy penalty. A privacy-related perturbation study measures the
effect of decision value when controlled noise is introduced to the bounded diffusion-propensity score.
This article has three scholarly components. First, it provides a detailed mechanism from an interdisciplinary perspective
instead of a generic argument that network measurement can improve marketing. The mechanism separates the
diffusion-propensity level from the contextual practical value and explicitly punishes redundant seed selections from the
same network community. It also reports an empirical and computational comparison where all policies act with the
same ﬁve-seed budget and are executed on the same 1,000 contexts. It also describes a privacy–decision-value stress
test, which it purposely describes as trade stability to Laplace perturbation. This is different from a formal graph-level
differential-privacy guarantee. It is of substance because rigorous differential privacy implies a neighboring-dataset
deﬁnition and sensitivity assessment relative to the release mechanism. For this reason, it describes how a privacy-
sensitive trade-off can be tested without overstating the legal or mathematical protection offered.
The main focus is on whether adaptive selection of creators, which integrates recorded engagement, network brokerage,
campaign relevance, and community redundancy, engages users at a higher quality level than policies that favors
followers, engagements, and static network brokerage, and what stability and scope do privacy-motivated perturbations
offer? The answer to this question is important to the management of advertisement interventions since an adaptive
policy is only justiﬁed if it outperforms other policies. If ranking engagements in campaigns is enough to select
advertisements, then no network structure is required. If a purely structural policy is the best, then a campaign is very
relevant. If the adaptive policy yields an important advantage that is sustained after mild perturbation, then measuring
social networks becomes a priority layer of ads allocation over descriptive reporting.
Page 3/24

2. Theoretical Background and Literature Development
2.1 Social structure, centrality and brokerage
The study of social networks is premised on the idea that one’s relational position affects one’s information, attention,
and opportunity. Freeman (1979) clariﬁed that there are different forms of centrality and distinguish degree, closeness,
and brokerage centrality. Subsequent research has stated that there is no one true measure of centrality. The move of
resources, information, or diffusion propensity through the network is what matters in the interpretation of the measure
(Borgatti, 2005). This applies directly to advertising. In a follower graph, high degree may indicate high immediate reach,
and in a market-aﬃliation network, through shortest-path brokerage centrality, one may be able to cross deﬁed market
segments. Seeing the two measures as one metric of diffusion propensity masks the process under study.
Nonredundant exposure is one of the aims of advertising brokerage. The reason for this is that cohesive groups can be
bridged, and information can ﬂow through social boundaries (Granovetter's, 1973). In the structural-hole perspective,
brokers have access to disparate information and opportunities (Burt, 2004). This is normally the aim of advertising. In a
situation where advertising is neither redundant nor repeated to the same audiences, a condition of high brokerage is
met. The current study puts the structural idea of shortest-path brokerage centrality coupled with inverse clustering into
practice. It rewards nodes that are less locally embedded and lie on many weighted shortest paths. This metric does not
claim interpersonal communication, but is structural and indicates nonredundant location in the advertising opportunity
network.
Community structure adds another layer to the thinking. Real networks cut into objects with a lot of connections
internally, but very few connections externally. These types of networks lend themselves very well to a methodology of
community detection (Blondel et al., 2008; Newman, 2006). This is a very important aspect to seed selection. It means
that two, otherwise very, strong creators can be jointly very weak when they both target nearly the same audiences. In
reversed, selecting across communities allows for a wider range of possibilities in the portfolio. Because of this, the
adaptive policy implements sequential redundancy penalty. This is a simple algorithmic approach and attempts to treat
the established concept of network science in the context of advertising management that is testable and recalculable in
a spreadsheet.
Homophily provides a theoretical rationale as to why category and geography can help in network development. In social
networks and the nature of exposing one’s self to information, homophily is often present; however, this is context
speciﬁc and across different elements/dimensions (McPherson et al., 2001). Looking from an advertising perspective,
category and greatest audience geographical location are not the same as in friendship ties, but they do suggest similar
positioning in the market. For this reason, the network constructed in this document should be seen more as an aﬃliation
or opportunity network, rather than a social relations network. This is essential for construct validity; the study of the
market position resembles brokerage and informs marketing strategy rather than whether the named creators are
personally connected.
2.2 diffusion maximization and adaptive seeding
Diffusion maximization formalizes the limitation of selecting the optimal set of seed nodes in a given context to
maximize expected diffusion. Kempe et al. (2003), in their pioneering work, focused on the basis of the problem within
the context of stochastic diffusion. Subsequent works in marketing have veriﬁed empirically that the performance of
seeding policies can be signiﬁcant. Hinz et al. (2011) for example, in their work and by conducting experiments and real
campaigns, showed signiﬁcant distinctions in success when comparing different policies. In the context of such studies,
treating the creators as a portfolio problem rather than an integral part of media planning is warranted.
Page 4/24

The classical approach assumes that the network and propagation process are steady enough for one optimally selected
seed set to remain informative. This assumption is violated in digital markets. Topics, communities, creators, and users'
interests shift over time. Scholarship on diffusion in this dependent and changing world has focused on dynamically
updating seed selection based on how the propagation process is changing. Other recent algorithms have learned to
minimize computation, prune redundancy in prediction of diffusion, and adapt to changing social media networks (Meena
et al., 2025). This study is not competing with these algorithms on computation. Its contribution is managerial. It
introduces ﬂexibility in a simple scoring policy that adapts to the campaign type and country while assuming a ﬁxed
benchmark network. Context therefore plays the role of a changing state variable.
An adaptive advertising policy also needs to take into account the uncertainty about a user’s diffusion propensity. Bakshy
et al. (2011) found that with even signiﬁcant historical data, predicting who would generate a big cascade was diﬃcult.
Watts and Dodds (2007) rejected the simplistic ‘high-diffusion-user’ hypothesis by indicating how the settings of a
network and the population’s susceptibility could matter as much as users themselves. The estimates support the need
for portfolio diversiﬁcation and ﬂexibility. Unlike assuming that the globally highest-scoring creator is always the best, the
adaptive policy encourages relevance to the campaign and punishes covering the same community. Thus, it is more
closely related to a stable allocation heuristic than to a hypothesis that diffusion propensity is measurable and ﬁxed.
There are nuanced interpretations of diffusion propensity and susceptibility. Aral and Walker (2012) note that in their
studies, susceptible and high diffusion members could be identiﬁed and that social contagion estimates without the use
of experiments could be problematic. For this reason, interpersonal diffusion propensity is not described with causal
language in this study. Engagement is recorded at the creator level and network metrics and campaign estimates are
described structural characteristics and proxy decisions, respectively. The scoring system deﬁned a higher qualiﬁed-
engagement threshold. This indicates that the selected portfolio combines larger recorded engagement and higher
contextual relevance based on the framework used, however, it should be noted that these creators do not certainly
cause additional purchases, nor would exposure necessarily diffuse through their follower network.
2.3 creator marketing, engagement and contextual ﬁt
Follower counts are an insuﬃcient management by objective (MbO) metric in the context of creator marketing. De
Veirman et al. (2017) found that the number of followers can impact the perception of popularity, while also pointing to
the presence of critical boundaries and divergence in the perceived uniqueness of the product. This means that in e-
commerce, the interpretation of reach should be contextual. A beauty campaign run in one country should not
incorporate a celebrity who is globally large and not related to the campaign. This reason relevance is explicitly depicted
in the adaptive model is that engagement is a better signal than follower counts, however, it has limitations.
Engagement can be a reﬂection of content quality and controversy, as well as audience composition, intensity, and
repeated exposure. It should not be confused for revenue. It may not be perfect, but it does provide a more proximate
measure of advertising attention than audience size. Word-of Mouth scholarships reported that social communication
can ultimately have an effect on both the acquisition and the growth of a system (Trusov et al., 2009). Creator
scholarship stated that the economic value of seed accounts is associated with the expected response, not just nominal
popularity (Bakshy et al., 2011). Thus, the model focuses on the percentile rank of authentic engagement, rather than
structural brokerage, when forming the primary diffusion-propensity score.
The framework's marketing logic may be broken into three parts of a ﬁt. The historical engagement asks if the creator has
shown the capability of generating a response; brokerage, if the creator inhabits a necessary structural position in the
advertising opportunity network; and campaign relevance, if the response and the position are pertinent to the product-
market ﬁt. Community redundancy is at the portfolio level. The method follows a common trend in that it breaks from
scoring systems that aggregate variables once and produce a ﬁnal leaderboard. The ﬁnal ranking is based on the
advertising campaign and the creators that were selected.
Page 5/24

2.4 Privacy, governance and open social data
A dilemma of advertising measurement is that it creates a permanent privacy-value conﬂict. Goldfarb and Tucker (2011)
studied the after effects of privacy laws on the measurement of online-ads and found that performance of online
advertising suffered as a result of weaker regulations of privacy. Tucker (2014) studied a different, but complimentary
effect. Personalized advertising was more effective as users had greater control over the personal data of advertising
targeting. These estimates show that privacy cannot be thought of as a strictly external measure to advertising. Trust and
control, regulations and data availability can change both targeted advertising sets and consumer responsiveness.
From an economic viewpoint, privacy decisions involve incomplete information and context-dependent tradeoffs
(Acquisti et al., 2016). From a technical viewpoint, graphical data create additional challenges since relationships can
provide information even if direct identity ﬁelds are removed. Because of this, the relatively new area of privacy research
focused on graph data principally investigates perturbation, local differential privacy, federated learning and graph release
as the primary techniques, as opposed to assuming that simple anonymization is suﬃcient. For example, Hao et al.
(2025) proposed a novel approach for publishing social network graphs and retaining the structural decisions while
introducing noise. This work informs the privacy stress test conducted in this article, while also providing a clear
indication that publishing a graph with a proven differential privacy guarantee is not the same as adding Laplace noise to
a bounded score.
The regulatory environment in India has advanced. The Digital Personal Data Protection Act of 2023 provides a
framework to process digital personal data and the Digital Personal Data Protection Rules of 2025 were notiﬁed on
November 13, 2025, with a phased implementation. The rules and commencement notiﬁcations place an operating
design challenge for governance of e-commerce for Indian companies, instead of a problem to be addressed in the far
future. An advertising measurement workﬂow must minimize the use of excessive personal characteristics to document
the deﬁnition and source of all variables and maintain a record of all modiﬁcations. It also must contain restrictions to
access raw identity ﬁelds when they are unnecessarily included, and evaluate the impact of removing sensitive scoring
inputs or perturbing them on the overall performance of the system.
Open-source platforms such as Bluesky are relevant because they can lower some roadblocks and enable greater
barriers to reproducible social-network research. Quelle and Bovet (2025) described the platform’s academic content and
openness to interpretation and designed code and identity ﬁelds that could be reconstructed using general application
programming interfaces. Smith et al. (2026) enlarged the open data environment with a massive resource of extensive
network connections. Such data do not permit unrestricted commercial proﬁling, and ethical data use still demands
consideration of the platform, redetection risk and the applicable law. For this research, public auditing is of high
procedural value. This type of auditing reports that contemporary social network science, as a result of the openness of
public infrastructure, can be audited, enhancing the external pertinence of a public visible SNA-based advertising
framework.
3. Study question, Conceptual Model and Hypotheses
Study question: With context-speciﬁc media selection focused on campaign-recorded engagement, brokerage, and
rational modularity and redundancy compared to follower count, quantiﬁcation, and static brokerage policies, to what
extent would each of these strategies improve advertising performance, and to what extent would be perturbations to
privacy a remedy?
The model of advertising allocation consists of four decisions: estimation of historical response, mapping of structural
non- redundancy, testing campaign-exact relevance, and diversiﬁcation of the selected portfolio. Figure 1 illustrates the
model in an editable table-formatted schematic.
Page 6/24

Figure 1. Editable conceptual framework for Privacy-Aware Adaptive Diffusion-Propensity Mapping.
Recorded
engagement
→ Market-aﬃliation
network
→ Context
relevance
→ Adaptive seed portfolio
Historical response
signal
  Brokerage + 
community
  Category + 
country
  Redundancy-controlled
selection
H1: The size of the followers is not positively monotonic to engagement; therefore, the number of followers will report a
non-positive rank association with average engagement in the benchmark.
H2: Network brokerage will report a positive bivariate association with recorded creator engagement.
H3: The context-adaptive policy will generate higher mean qualiﬁed engagement than follower-size targeting.
H4: The context-adaptive policy will generate higher mean qualiﬁed engagement than engagement-only targeting.
H5: The context-adaptive policy will generate higher mean qualiﬁed engagement than static network-brokerage targeting.
H6: Moderate score perturbation at epsilon = 1 will retain at least 90 percent of the unperturbed adaptive policy decision
value in the stated stress test.
H1 is stated as a benchmark-exact empirical expectation.
H2 is similar and is bivariate and descriptive. H3-H5 relate to the performance of the policy under a common seed
budget, whereas H6 is a stability threshold of the perturbation. None of the hypotheses are considered as causal to
purchases or sales.
4. Data and Study design
4.1 Data sources and quantitative scope
The main benchmark is a September 2022 Instagram creator dataset publicly available. In this study, the ﬁelds are
creator name, follower count, primary audience country, authentic engagement, average engagement and primary
category. The assessment processed 117 complete creator records found in the supporting benchmark contained in the
reproducible workbook. Terse numeric variables such as M and K have been expanded to exact values. The dataset is
informative because it provides relevant advertising responses and segments in one simple public dataset, although it is
not a live 2026 dataset. Thus, the authors of the article clearly state the period of data collection and refrain from
reporting statistics of named accounts as current account values.
Contemporary external validity is provided by currently publicly available studies of social networks, rather than by silently
updating benchmark values. Quelle and Bovet (2025) described a Bluesky interaction network comprising approximately
ﬁve million users, and Smith et al. (2026) reported 39.7 million accounts and approximately 2.4 billion following
relationships and 365.8 thousand starter-pack groups in A Blue Start. The advertising benchmark and the network
resources differ in a substantive way: the benchmark provides fully reproducible advertising calculations, and the newer
datasets show that large, structurally rich public social networks exist, which may be further replicated and extended.
The unit of recorded assessments is creators. The unit of experimental assessments is a synthetic campaign context,
one content category and one audience country. Campaign contexts are drawn with replacement from recorded category-
country combinations of records where the audience country is known. The calibration grounds simulated contexts in the
support of the data that has been recorded, and thus does not fabricate unrelated market segments. A thousand contexts
Page 7/24

are generated with the random seed value 20260909, meaning that all policy comparisons in the accompanying Excel
workbook can be reproduced exactly.
For the experiment, a ﬁve-creator budget per policy has been applied. This budget has to be ﬁxed as a policy that chooses
more creators will automatically increase the qualiﬁed engagement sum. The score metric is not click through rate,
conversion rate, likelihood to purchase or expected revenue. It is a proxy for qualiﬁed engagement for each selected
creator, and is calculated based on the creator’s average engagement, adjusted for relevance of the campaign. This
metric makes it possible to conduct a legitimate analysis based on publicly accessible data.
Constructs that are used in the analysis are described in Table 1. This is presented here prior to reporting.
Table 1
Operational deﬁnitions and quantitative functions of variables.
Construct Meaning Operationalization Function
Follower count Recorded nominal
audience size
Benchmark ﬁeld converted to absolute
count
Baseline popularity
policy
Authentic
engagement
Recorded quality-
adjusted engagement
count
Benchmark ﬁeld converted to absolute
count
Historical response
component
Average
engagement
Recorded average
interaction count
Benchmark ﬁeld converted to absolute
count
Qualiﬁed-engagement
performance score
input
Aﬃliation edge Shared advertising-
market position
1 if same category + 1 if same
audience country
Network construction
Shortest-path
brokerage
centrality
Weighted shortest-path
brokerage
NetworkX weighted shortest-path
brokerage centrality; distance = 
1/edge weight
Brokerage component
Clustering Local embeddedness Weighted clustering coeﬃcient Inverse component of
brokerage
Community Dense structural
segment
Greedy modularity community Portfolio redundancy
control
Campaign
relevance
Contextual ﬁt 0.2 + 0.4 category match + 0.4 country
match
Adaptive weighting
Qualiﬁed
engagement
modeled campaign
decision value
Sum of average engagement ×
relevance
Policy comparison
performance score
4.2 Market-aﬃliation network construction
An advertising network G = (V, E) is constructed with the 117 creators. An undirected edge exists when two creators
share a main content category, audience country, or both. Edge weight is therefore 1 or 2. The edge is meant to represent
advertising market aﬃnity. The edge is not meant to represent friendship, following, communication of information. The
advantage is that the network can be reproduced from publicly available data, without reconstructing the follower
relationship.
w_ij = I(Category_i = Category_j) + I(Country_i = Country_j) (1)
For weighted shortest-path calculations, distance d_ij = 1/w_ij. Therefore, an edge sharing category and country is treated
as a shorter market distance than an edge sharing only one dimension. Measures of degree centrality, weighted shortest-
path brokerage, eigenvector, and weighted clustering will be used for a descriptive assessment. Greedy modularity will be
used to decompose the graph into communities. Although Louvain- and Leiden-family algorithms are popular in extensive
Page 8/24

networks (Blondel et al., 2008; Traag et al., 2019), greedy modularity will suﬃce for the small, dense benchmark and has
the advantage of a deterministic implementation under the given ordering.
Table 2 shows the calculated network. The network contains 117 nodes and 2,594 edges, which gives a density of
0.3823. Four communities were found, and the largest contains 51 creators.
Table 2
Structural summary of the advertising-
market aﬃliation network.
Metric Value
Nodes 117
Edges 2594
Density 0.3823
Mean weighted clustering 0.4666
Communities 4
Largest community 51
4.3 Brokerage, diffusion propensity and contextual relevance
The network brokerage score combines shortest-path brokerage centrality and inverse clustering. Each component was
percentile ranked among the 117 creators before weighting. Percentile ranking reduces the effect of the extreme right
skew in raw shortest-path brokerage centrality. The creator’s shortest-path brokerage centrality was given weight 0.60
because the main structural aspect of the market was bridging. Inverse clustering was given weight 0.40 because low
local redundancy is desirable, but not suﬃcient on its own.
Brokerage_i = 0.60·P(Shortest-path brokerage centrality_i) + 0.40·P(− Clustering_i) (2)
The core diffusion-propensity score then combines recorded authentic engagement with network brokerage. Authentic
engagement was weighted 0.65 and brokerage 0.35. These weights do not consider causality. They are designed to
amplify recorded responses and are adjustable within the network's rank. Transparency is a part of this design: within the
supporting workbook or assessment code, managers can change the weights and run the policy comparison again.
CorePropensity_i = 0.65·P(AuthenticEngagement_i) + 0.35·Brokerage_i (3)
Campaign relevance r_ic is limited to the range of 0.2 to 1.0. Every creator gets a core relevance of 0.2. An additional 0.4
is added for a category and country match. Therefore, one match of category and country yields a relevance of 1.0, one
match of either category or country yields a relevance of 0.6, and a nonmatching creator gets a relevance of 0.2. The
nonzero relevance shows the model that all cross-category and cross-country diffusion is not useless, while still making
an exact market ﬁt ﬁve times as important as no match.
r_ic = 0.2 + 0.4·I(Category_i = Category_c) + 0.4·I(Country_i = Country_c) (4)
4.4 Targeting policies
The follower-size policy chooses the ﬁve accounts with the largest follower counts and does this for every campaign.
This is a typical reach-oriented approach. The engagement-only policy chooses the ﬁve accounts with the highest
authentic engagement, also globally and without any context. The static SNA policy chooses the ﬁve highest network
brokerage scores. These baselines show the three well known decision criteria: nominal reach, historical response, and
structural non redundancy.
Page 9/24

The adaptive policy operates a sequential selection algorithm for each campaign context. Candidate priority is deﬁned as
the product of the degree of Core diffusion propensity, campaign relevance, and the divisor of the redundancy factor. The
redundancy factor is incremented by 0.20 for each candidate’s community seed previously chosen. After one creator is
chosen, priorities are recalculated for the following selection. Each creator cannot be selected more than once. The
process is meant to allow a given context to supersede a lower global rank and to allow for the ﬂexibility of the portfolio
following selection.
Priority_i,c,S = CorePropensity_i · r_ic / [1 + 0.20·n_same-community(i,S)] (5)
Qualiﬁed engagement is the average engagement score for each selected creator multiplied by the campaign relevance.
As the performance score is additive and the seed budget is ﬁxed, the main source of policy differentiation is found in the
selection and how well the selected accounts relate to the campaign. The measure should be interpreted as a proxy for
attention allocation. It is meaningful in the context of various engagement rules to assess the relative impact across
similar contexts, but it cannot quantify the causal impact on purchases.
QEng(S,c) = Σ_(i ∈ S) AverageEngagement_i · r_ic (6)
4.5 Statistical appraisal
Descriptive statistics for count, mean, standard deviation, quartiles, extrema, skewness and kurtosis will be reported.
Given that follower and engagement variables are extremely right-skewed, for the bivariate hypothesis tests for
monotonic association, Spearman rank correlations will be reported. This reduction in contingency greatly aids the
relative ranking hypothesis. P-values were provided by the automated statistics software.
This paper outlines two supplementary models that examine whether structural metrics provide additional explanation
beyond follower size. Averages of engagements and follower counts are transformed using ln(1 + x). Model 1 exclusively
contains log of follower counts. Model 2 incorporates shortest-path brokerage centrality and clustering in addition to log
of follower counts. Heteroscedasticity-consistent HC3 standard errors are used to report results of this study. Uneven
residual variance may exist in small cross-sectional samples. Regressions of this nature are used for diagnostics rather
than to establish causality. The aﬃliation network was constructed based on observed traits, and there is no external
source to determine network position.
Since all four policies are tested in the same 1,000 campaign contexts, pairs of policies are made for comparison. For
each baseline, the difference in qualiﬁed engagement with respect to the adaptive policy, relative to the baseline, is
analyzed using a paired t-test and a Wilcoxon signed-rank test. The paired t-test calculates both the mean difference and
conﬁdence interval, while the signed-rank test is used to evaluate the distribution. The difference is summarized via
Cohen’s dz, where dz is the mean of the paired differences relative to the standard deviation of the paired differences.
Since the number of campaign contexts is extremely large, the differences are expected to be structured with small p-
values. Consequently, emphasis is placed on the difference and its associated conﬁdence interval and percentage uplift
and not the p-values.
Reproducibility is established using a ﬁxed random seed, a data dictionary that is provided as supplementary material,
retained intermediate data, and an Excel workbook that is supplemented with a step-by-step explanation of the
computations and the summary output. Random campaign contexts are generated using a seed of 20260909 and privacy
perturbations use a seed of 20260910. All policy outputs are generated automatically from the same dataset and no
estimate reported in this article is based on a manual edit of a statistic.
4.6 Privacy-motivated perturbation stress test
Page 10/24

This privacy experiment focuses on a speciﬁc stability question: how much adaptive targeting decision value will be
preserved if some amount of noise is added to the bound core DPS? Each score is perturbed by Independent Laplace
noise with scale 0.05/epsilon and the estimated score is clipped to the range [0,1]. Smaller epsilon results in larger
perturbations. The adaptive selection procedure is applied to the noisy score. We study epsilon values of 0.5, 1, 2 and 5.
The privacy mechanism that is used here resembles a differential privacy based noise mechanism, but is not
implemented in the context of graph differential privacy. A formal guarantee would require an exact neighboring-dataset
deﬁnition, sensitivity bound for the released statistic, privacy accounting for multiple releases, and a statement about
how and to whom information would be released. Privacy for graphs is particularly challenging, as edges themselves can
be sensitive, and recent studies have used speciﬁc mechanisms to preserve graph decision value under privacy
constraints (Hao et al., 2025). Rather than this, we conduct a stress test of operational rigor to measure the level of score
distortion that we can tolerate.
PerturbedPropensity_i = clip(CorePropensity_i + Laplace(0, 0.05/ε), 0, 1) (7)
DecisionValueRetention_ε = 100 · Mean(QEng_ε) / Mean(QEng_unperturbed) (8)
5. Estimates
5.1 Descriptive characteristics and network structure
The main recorded and network variables are shown in Table 3. The average follower count of each account is
81.54 million, with a highly variable SD of 99.21 million, and a strong right skew of 2.53. Average authentic engagement is
1.319 million and average engagement is 1.695 million, and both measures are highly skewed. Shortest path brokerage
centrality is especially concentrated with a mean of 0.0060, a maximum of 0.0808, and a strong right skew of 5.23. Given
these distributions, a rank-dependent bivariate assessment and recasting of percentiles is justiﬁed for the decision
scores.
Table 3
Descriptive statistics for recorded creator and network variables.
Variable Mean SD Min Median Max Skew
Followers 81,540,170.940 99,213,151.815 10,500,000.000 48,300,000.000 546,600,000.000 2.530
Authentic
engagement
1,318,641.026 1,370,582.786 78,800.000 929,300.000 9,900,000.000 3.324
Average
engagement
1,695,061.538 1,556,725.518 100,300.000 1,200,000.000 9,900,000.000 2.581
Degree
centrality
0.382 0.176 0.009 0.388 0.603 -0.367
Shortest-
path
brokerage
centrality
0.006 0.009 0.000 0.003 0.081 5.229
Clustering 0.467 0.090 0.000 0.483 0.569 -1.718
The network's denseness indicates a considerable overlap of categories and/or countries of audience, but the four-
community solution ﬁnds a signiﬁcant structural segmentation. In the benchmarks, the largest category group contains
Cinema and Actor accounts, with the second largest group being Sports accounts. The United States and India are the
most dominant audience countries. In the benchmarks, category and country determine edge formation. Therefore, the
Page 11/24

distributions explain how some accounts become bridges. An example would be a creator with a rare country but large
category or a large country with a rare category. These individuals would connect a remote region of the opportunity
network.
5.2 Bivariate associations
Table 4 presents some examples of Spearman rank co-movements. The estimate of follower engagement is not aligned
with the simple scale hypothesis. In the benchmarks, follower count is related to authentic engagement (ρ = −0.274, p = 
0.0028) and mean engagement (ρ = −0.278, p = 0.0024) in a negative way. These coeﬃcients do not imply that follower
count diminishes engagement; in the benchmarks, large accounts do not ﬁll the most engaged positions. Thus, H1 is
supported for the benchmarks.
Shortest-path brokerage centrality is positively related to authentic engagement (ρ = 0.310, p < 0.001) and average
engagement (ρ = 0.310, p < 0.001) in the bivariate analysis, supporting H2. In the benchmarks, clustering is negatively
related to authentic engagement (ρ = −0.202, p = 0.029) and average engagement (ρ = −0.246, p = 0.0075), supporting the
concept that less locally redundant positions can be informative. Such associations should not be causally interpreted
and should be seen as an example of empirical motivation to consider response and brokerage in combination. Instead
of assuming that a higher level of diffusion propensity strongly correlates with a larger follower count, we should
consider another approach.
Table 4
Selected Spearman rank co-movements among scale, engagement and network structure.
Variable 1 Variable 2 Spearman ρ p-value
Followers Average engagement -0.278 0.0024
Followers Authentic engagement -0.274 0.0028
Authentic engagement Shortest-path brokerage centrality 0.310 < 0.001
Average engagement Shortest-path brokerage centrality 0.310 < 0.001
Average engagement Clustering -0.246 0.0075
Shortest-path brokerage centrality Clustering -0.631 < 0.001
Figure 2 shows the most important bivariate rank associations as a native Word table in which the user can edit the
values and bar symbols.
5.3 Regression diagnostics
The supplementary regressions in Table 5 give a more conservative check. Model 1 explains very little of the variance for
logged average engagement (R² = 0.032). The logged follower count is negatively associated with the model’s
explanatory variable (− 0.159) and thus remains unexplained (p = 0.140). When we add brokerage centrality and clustering
(Model 2), we see a much better model (R² = 0.088), but the coeﬃcients remain imprecise. With the addition of the other
variables, we see that brokerage centrality is positively associated with the model (14.667, p = 0.567) and clustering is
negatively associated with the model (− 0.951, p = 0.493). The logged follower count is also negatively correlated with the
model (− 0.165, p = 0.118). The AIC decreased (from 275.97 to 273.08) and the BIC increased, which is expected due to
the addition of new parameters.
These regression analyses do not disprove what we found in the bivariate analyses. Our sample consists of only 117
measurements, network variables are interdependent, shortest-path brokerage centrality is extremely skewed, and our
created association network depends on categories and countries instead of an independently collected social network.
Page 12/24

Therefore, the overall conclusion we can draw from this is limited: the rank co-movements suggest that brokerage and
engagement are more strongly associated in the benchmark than follower size, but the cross-sectional regressions do
not identify brokerage as a clear explanatory factor. The policy experiment evaluates a different hypothesis. Does the use
of a transparent decision rule, based on characteristics, result in a more successful allocation of a ﬁxed seed budget,
when applied to its objective function?
Table 5
Ordinary least squares diagnostics for logged average engagement with HC3 heteroskedasticity-consistent standard
errors.
Model Term Coeﬃcient HC3
SE
p-
value
95% CI
M1: size only log_followers -0.159 0.108 0.140 [-0.371, 0.052]
M2: size + brokerage + 
clustering
log_followers -0.165 0.105 0.118 [-0.371, 0.042]
M2: size + brokerage + 
clustering
Shortest-path brokerage
centrality
14.667 25.611 0.567 [-35.531,
64.864]
M2: size + brokerage + 
clustering
Clustering -0.951 1.388 0.493 [-3.671, 1.768]
5.4 Targeting-policy performance
The central comparison of the experiment is reported in Table 6. In this case, the follower-size policy results in a mean of
6.268 million qualiﬁed engagements. Mean qualiﬁed engagements increase to 11.317 million via the engagement-only
targeting policy. The use of static network brokerage targeting results in 6.633 million mean qualiﬁed engagements,
reﬂecting a key constraint of context-free structural selection. This constraint is that in most sampled campaigns, its
globally strongest brokers are located in market positions that are irrelevant. The adaptive policy results in an mean of
13.976 million with a 95% conﬁdence interval of 13.748 million to 14.204 million. It also results in a mean relevance of
0.747, far above the baseline mean relevance of 0.320 to 0.410.
Improvement is partly attributable to the statistics associated with the composition of the portfolio. The adaptive policy
selects, on average, 4.949 of the ﬁve creators who match at least one of the campaign dimensions and 1.892 who match
category and country. Exact-match baseline ﬁgures range from 0.128 to 0.148. Though relevance was strongly imposed,
community coverage remained above two communities on average, indicating that the redundancy penalty prevented the
algorithm from collapsing to one segment. The estimate is not simply ‘choose the most relevant accounts’, but rather
‘choose relevant accounts that have strong recorded engagement and structurally informative positions and retain
portfolio diversity’.
Table 6
Performance of four ﬁve-seed targeting policies throughout 1,000 campaign contexts.
Policy Mean
QEng
95% CI
low
95% CI
high
Mean
relevance
Community
coverage
Any
match
Exact
Follower 6,267,804 6,162,882 6,372,726 0.340 3.000 1.621 0.128
Engagement 11,317,400 11,176,883 11,457,917 0.320 3.000 1.356 0.148
Static SNA 6,633,400 6,426,339 6,840,461 0.410 2.000 2.482 0.138
Adaptive 13,975,961 13,747,264 14,204,658 0.747 2.421 4.949 1.892
5.5 Paired inferential comparisons and difference sizes
Page 13/24

Table 7 shows the adaptive advantage is structured across campaign contexts. Compared to follower-size targeting, the
mean difference of 7.708 million qualiﬁed engagements presents a 122.98 percent increase, with a Cohen's dz = 1.983.
The metric for engagement-only targeting shows a difference of 2.659 million, with a 23.49 percent increase, and a dz = 
0.825. For static SNA targeting, the mean 7.343 million represents a 110.69 percent increase with dz = 1.476. All the
paired t-tests and Wilcoxon tests provide evidence for rejecting equality at extremely low signiﬁcance levels.
In terms of baseline, the engagement-only targeting is the most diﬃcult to describe because it already exploits the
strongest recorded response signal. A 23.49 percent improvement on that approach captures why the adaptive scholarly
value is not simply dwarﬁng or favoring highly engaging accounts. Relevance weighting determines which high-
engagement accounts are informative for a campaign, and the network component alters the order in which the accounts
enter the portfolio. That is why for H3, H4, and H5, the experimental design supports those hypotheses. The differences
shown should not be interpreted to mean a lot in terms of sales. The objective function is constructed from recorded
engagement and relevance weights. Thus, the bounds have been established for making internal decisions under the
given proxy.
Table 7
Paired comparisons of adaptive targeting with baseline policies.
Comparator Mean difference 95% CI low 95% CI high Uplift Cohen dz Paired t p Wilcoxon p
Follower 7,708,157 7,466,995 7,949,320 122.98% 1.983 < 0.001 < 0.001
Engagement 2,658,561 2,458,574 2,858,549 23.49% 0.825 < 0.001 < 0.001
Static SNA 7,342,561 7,033,787 7,651,335 110.69% 1.476 < 0.001 < 0.001
5.6 privacy–decision-value stress test
The privacy motivated perturbation estimates are reported in Table 8. For epsilon 0.5 and noise scale 0.10, the adaptive
system retained 85.75 percent of the qualiﬁed engagement decision value. For epsilon 1, noise scale 0.05, retention was
94.10 percent. For epsilon 2 and 5, retention was 97.70 and 99.28 percent respectively. 0.745–0.749 is the range for
mean contextual relevance across all perturbation levels. This indicates that most of the effect of noise is for contextual
ﬁt to shift the order of similarly relevant candidates.
H6 is supported as there is decision-value retention at epsilon 1 that is greater than the prespeciﬁed 90 percent. This
provides an informative design principle. If there are many candidate creators with similar contextual ﬁt, it may not have a
signiﬁcant effect on portfolio performance to have slight imprecision in a bounded diffusion-propensity score. This is
good for privacy-aware engineering, as organizations may be able to reduce their reliance on exact person scores, but
may not lose most of the allocation decision value. This does not provide any evidence that epsilon 1 is legally suﬃcient,
ethically highest-scoring, or formally differentially private in the setting. Those claims need a formal release mechanism
and an application-exact threat model.
Table 8
Adaptive-policy decision value under Laplace score perturbation.
Epsilon Noise
scale
Mean
QEng
SD decision value
retained
Mean
relevance
Community
coverage
0.5 0.100 11,985,033 3,542,436 85.75% 0.745 2.406
1 0.050 13,150,701 3,521,921 94.10% 0.747 2.405
2 0.025 13,655,206 3,585,842 97.70% 0.749 2.412
5 0.010 13,874,923 3,629,058 99.28% 0.748 2.416
Page 14/24

Figure 4 shows the privacy–decision-value tradeoff. The native Word table in the chart shows numerical values that can
be edited in the chart.
5.7 Hypothesis appraisal
Table 9 brings together the hypothesis decisions, evidence, and conclusions.
Table 9
Summary of hypotheses, decisions and supporting evidence.
Hypothesis Prediction Decision Evidence
H1 Follower count has non-positive rank
association with engagement
Supported in
benchmark
ρ with average engagement = − 
0.278; p = 0.0024
H2 Brokerage positively associates with
engagement
Supported
bivariately
ρ with average engagement = 
0.310; p < 0.001
H3 Adaptive > follower-size policy Supported 122.98% uplift; dz = 1.983
H4 Adaptive > engagement-only policy Supported 23.49% uplift; dz = 0.825
H5 Adaptive > static SNA policy Supported 110.69% uplift; dz = 1.476
H6 At ε = 1, ≥ 90% decision value retained Supported 94.10% decision-value retention
6. Discussion
The main estimate is that adaptive selection beats the other three options in this case. Controlling for contexts, the other
options are simpler. The evidence is in support of a broader claim that making measurements of social networks is
helpful in managing advertising. Value is not due to centrality alone. Engagement-only targeting is much better than
targeting followers on average, and static brokerage is only slightly better than targeting followers. Networks are
informative only together with context. The estimate is important because many applied SNA projects stop after
detecting high-centrality users. The provided estimates state why a leaderboard is not a policy on advertising.
Negative rank co-movement of follower engagement conﬁrms this. In the 2022 benchmark, many large accounts have
relatively low engagement, while some small accounts have high authentic engagement. This pattern reﬂects evidence of
creator marketing in which having a large follower count can make people perceive you as popular, but doesn't guarantee
you will have positive opinions or product ﬁt (De Veirman et al., 2017). This also corresponds with diffusion research that
states that at the individual level it is diﬃcult to determine the propensity to diffuse (Bakshy et al., 2011). For managers,
this means they shouldn't completely stop tracking metrics for reach, but should consider their value depending on how
well the campaign ﬁts and the quality of the responses.
The brokerage estimate is more reﬁned. Centrality of brokerage and shortest path in engagement rank and clustering is
negatively correlated to engagement on average, but regression values are vague. A reasonable interpretation is that
brokerage captures accounts that are structurally important in the opportunity network. brokerage likely doesn't cause
engagement. The cross-section data can't determine if creators with high engagement are positioned in different
segments, if engagement and brokerage is driven by latent celebrity traits, or if the relationship is mechanical due to
category-country composition. This is why the policy experiment is testing a decision rule rather than a structural causal
model.
Conﬁguration is the strongest scholarly value. The adaptive algorithm is well-suited because it integrates four levels of
appraisal. At the node level, historical engagement represents the obtained response. At the network level, brokerage is a
nonredundant market position. At the campaign level, relevance denotes a category and geography. At the portfolio level,
Page 15/24

the redundancy penalty spreads selections across communities. Each level solves the previous one's problem.
Engagement without relevance may select the best accounts for the wrong market; relevance without engagement may
select poor, niched accounts; absence of network variety may lead to redundant portfolios; and network structure without
context may reward brokers who are irrelevant to the campaign.
This conﬁguration also illuminates how this study advances the literature. Many papers in network science focus on
adjusting the anticipated spread or ﬁt in an allocated graph structure, while many marketing papers focus on source
characteristics, persuasion, and/or credibility. The proposed framework sits between both. It doesn't require a fully known
and speciﬁed diffusion probability on all edges. Instead, it substitutes recorded historical engagement or interaction as a
prior empirical response and uses network brokerage as a structural diversiﬁcation signal. This overall framework makes
the method much easier to deploy in e-commerce organizations that have incomplete cross-platform graphs, but retain
creator performance histories and audience descriptions.
This privacy estimate presents a second scholarly value. The experiment shows that the decision value can remain high
even if the diffusion propensity score is intentionally set to a low level. At epsilon 1, 94.10 percent of unperturbed
decision value was retained. The estimate provides engineering logic for data minimization. If a targeting system is still
informative after score perturbation, an organization should wonder if keeping maximal precision about every person is
warranted. This logic is consistent with the economics of privacy, where data value should be balanced with risk, trust
and governance, rather than being considered for free (Acquisti et al., 2016). It also complements the empirical evidence
that user control is constructive with regard to the personalization of innovative services (Tucker, 2014).
That said, the privacy estimation should not be overinterpreted. Differential privacy is a formal deﬁnition of a randomized
mechanism within a deﬁned neighboring dataset. The current perturbation is a modiﬁcation to the Laplace-noise method
to examine the stability of the ranking. It doesn't defend the latent graph and doesn't address the concern of repeated
queries. It also does not protect against connection attacks. Recent studies on publishing graphs show the additional
methods and tools necessary to defend these attacks (Hao et al., 2025). For publication, the constraint is an advantage,
not a problem, since it ensures not let privacy extends beyond the limits set by formal methods.
The modern literature on Bluesky also provides evidence in support of future replication. Quelle and Bovet (2025)
reported that millions of users can be studied via an open decentralized platform, and Smith et al. (2026) supply a
pairwise and higher-order network at a scale far beyond any existing benchmark. Diffusion studies also support the need
to analyze the effect of changing network topology simultaneously (Meena et al., 2025). A later iteration could replace the
static market aﬃliation graph with rolling interaction snapshots. It could also estimate velocity of diffusion propensity
and rerun campaign allocation as communities and engagement trajectories change. This article lays out the foundation
for this extension with the decision architecture and reproducibility layer.
Table 10 places the existing benchmark along with the newly public network resources. The table isn’t indicating that the
datasets capture the same concepts. The 2022 creator benchmark is more advertising focused and contains
engagement/category/country ﬁelds. Bluesky resources are more contemporary social network datasets with much
more relational complexity and other advertising ﬁelds. The resources are complementary and make explicit the other
important condition for combining advertising data and performance data – the advertising data is likely to be from
social networks that were not built for that purpose.
Page 16/24

Table 10
Advertising benchmark and contemporary public social-network resources.
Resource Period Scale Key variables Function in the study
Instagram
creator
benchmark
September
2022
117 records applied
here
Follower, engagement,
category, audience country
Main reproducible
advertising
benchmark
Quelle & Bovet 2025 ~ 5 million users Interaction/network topology
and curation
Contemporary open-
network feasibility
A Blue Start
(Smith et al.)
2026 39.7M accounts;
~2.4B follow ties;
365.8K groups
Pairwise following + higher-
order starter packs
Large-scale external
network context
7. Managerial, Ethical and Regulatory Implications
For advertising managers, the most signiﬁcant impact is the separation of global creator ranking from campaign
allocation. A global score is useful, but the ﬁnal portfolio should be recomputed when the target category or geography
changes. In manager terms, a campaign management dashboard should maintain a core diffusion propensity score for
each eligible creator. The score is multiplied by campaign relevance and a portfolio-variety penalty is applied as a seed is
chosen. The architecture supports real-time updating since only the input scores need to be updated. The allocation logic
remains unchanged and is auditable.
The second implication concerns organizational design. Most social network analysis techniques are not helpful to
marketing professionals. This is because marketing professionals deal with real-world challenges and constraints, while
network scientists deal with abstract challenges. The framework introduces several variables that these two groups can
share: engagement, relevance, brokerage, community, and seed budget. Rather than hiding the variable weights in an
impenetrable model, a cross-functional team can decide on the weights explicitly. Data scientists can explore the limits of
uncertainty and stability, and if the other variables are adequately deﬁned, legal teams can deﬁne the restrictions on the
use of the data, the scope of marketing activities can be ﬂexibly deﬁned, campaign managers can test the limits of uplift,
and legal teams can test how far the risk is worth taking.
The third implication is that ﬁrms should look at network variety as a budget-eﬃciency variable. In the case of two sellers
selling to the same market segment, a purchase may yield diminishing marginal returns. The adaptive penalty captures
this logic, even without perceptual level detail. In ﬁrms that have reach/frequency or audience overlap estimates, the
penalty can be replaced with an empirically based overlap function. The logic is the same: person scores should be
tested jointly, since a portfolio can be redundant, even if each of the members is dominated by the rest.
Fourth, when addressing privacy in quant mod, privacy governance should be baked into the modeling pipeline rather than
done as an afterthought. A supporting workbook shows relevant trails for edge rules, score formulas, seeds used, and
source connections. With a production system, this should be broadened to cover deﬁned retention windows, lawful
purpose justiﬁcation, access control, and logs for model changes. With regard to India’s Digital Personal Data Protection
Act, organizations should consider the staged roll out, where applicable, as well as the notice and consent requirements,
among others, addressing the security and accountability prongs. The drafting of the legislation does not contain legal
opinions. Rather, the legislation is focused more on providing the context of the governance framework.
Fifth, organizations must recognize public availability does not equate to ethical permissibility. Although a public social
post or proﬁle may be accessible to the general public and therefore technically available without requiring
authentication, a great deal of data aggregation, proﬁling, and inference may pose a risk to the person because of the
lack of control. The principle of minimum necessity supports the use of traits if they provide suﬃcient value in the
Page 17/24

decision-making process and if it is determined that perturbing or aggregating the data would change the decision. The
privacy engineering stress test provides a useful framework to consider the question “how much performance would be
lost if we allow some degree of lack of precision?”
The framework enables cross-platform interoperability. Firms can map proprietary measurements to a limited set of
quantitative primitives. These primitives can allow apples-to-apples comparisons across various platforms. The
primitives include: the historical response, the market’s relevancy, structural brokerage, and conﬁdence level of data. This
mapping preserves the decision rule’s meaning, and source systems are allowed to be different. Follow graphs from
Bluesky, performance tables from Instagram, and an e-commerce referral network, can all be represented.
8. Stability, Boundary Settings and Reproducibility
An empirical paper that can be published has to be concise. This is exactly what the recommendation for advertising
sets. The benchmark refers to the advertising data for September 2022, and therefore, it shouldn’t be used to rank the
current creators. The benchmark’s goal is to create a framework for others to validate the advertising data within the
open network. In this case, it is better to work with real-time or recent platform data, and not what the article claims to
have done.
The other boundary is contextual. In the aﬃliation graph, edges represent similar categories or audiences that are in the
same country. Therefore, a strong edge indicates market overlap, and not communication. Shortest-path brokerage
centrality in the graph can be interpreted as brokerage in advertising-market aﬃnities. If a researcher rebuilt the actual
replied, retweeted, or follower networks, the shortest-path brokerage centrality would mean brokerage in communication,
as opposed to market brokerage. The same formulas would be used, and the conclusion would be aligned with the
semantics in the graph.
The third boundary is related to the performance score. Qualiﬁed engagement is a proxy for allocation that relies on
average engagement and relevance. Because the adaptive policy is sensitive to related inputs, it is expected to perform
well to the end set. Comparing policies is still informative because the baselines apply the same performance score and
budget, but external validity requires the recording of campaign estimates such as perceptions, clicks, assisted purchase
completions, incremental sales, or brand lift measured in an experimental setting. For this analysis, then, improvement in
decision making is sought, rather than an assessment of the causal effect of advertising.
The fourth boundary relates to the choice of parameters. A value of 0.65/0.35 for engagement and brokerage, a value of
0.4/0.4 for category and country match, and a value of 0.20 for community redundancy are design parameters. Estimated
values should be used for production systems; validated with a holdout period, and ideally nested temporal validation
should be used to avoid "leakage". The design of the workbook makes sure to show the formulas. This allows for
different values to be tested.
The ﬁfth boundary refers to sampling. Campaign contexts are sampled from recorded category-country combinations
with replacement. This method attempts to create a realistic, yet repeatable, sample like that of the benchmark. Policy
estimates are done for campaign contexts that are representative of the distributions of Cinema/Actor and Sports
categories, and India and the US audiences. A different campaign media mix should dictate a reweighting or resampling
contexts. The methodology is ﬂexible but the effect should not be taken as universal.
The sixth boundary is inferential contingency. Simulations of campaigns reuse the same 117 creator records. Because of
this, 1000 estimates do not reﬂect 1000 independent ﬁeld campaigns. The consistency of answers for the decision-
making contexts is measured against pairs of statistical tests. General population sampling uncertainty for the 1000
separate campaigns is not what is being measured. Because of this, it is more justiﬁed to present estimates of
Page 18/24

differences and comparisons of algorithms. It should not be interpreted as saying that the p-values demonstrate general
causal relationships.
The seventh boundary is privacy. The Laplace test is a score-stability test. It does not ensure differential privacy of user,
edge, or graph levels. In order to formalize the framework into a private mechanism, a scholar would have to deﬁne
neighboring datasets, bound sensitivity, manage the privacy budget for the repeated releases, and possibly adopt
community-aware or graph-centric perturbation. The recent privacy literature offers the methods needed to do this, but it
would change the estimate and would require a separate validation study.
The eighth boundary is platform interoperability. Deﬁnitions of an engagement may vary across platforms. Audience
categorization and deﬁnition of engagement may vary across platforms. Reposts and other metrics used for assessing
engagement may have different exposure denominators and different algorithms for selection. Thus, variables must be
standardized across platforms by either percentile or z-score, and the platform metric must be retained. The current
components are headed in this direction. They provide relative rank rather than absolute value for the diffusion-propensity
score.
The ninth consideration concerns choice of algorithm. The shortest-path brokerage centrality and inverse clustering were
selected as they are best aligned to brokerage and redundancy. Other algorithms may include k-core, PageRank,
eigenvector centrality, participation coeﬃcient, bridging centrality or community-aware diffusion-propensity scores. The
descriptive estimates indicate degree and eigenvector centralities are rank-co-moved in the aﬃliation graph, therefore,
using several centrality measures to capture distinct information may lead to multicollinearity. Multiple centrality
measures should only be used if they add value to the determination process.
The tenth consideration is fairness. An adaptive ranking that sequentially favors historically active users can create an
advantage that becomes increasingly inequitable for higher status creators. Market segmentation that favors large
creators and ignores newer, minority creators will likely become inequitable. Quotas of questions may be incorporated
along with a minimum representation constraint to guarantee outcomes for new creators and uncertainty bonuses or
budget share. This would shift the objective from achieving the objective of qualiﬁed engagement to an objective of
achieving eﬃciency, fairness, discovery and balance. The existing modular structure would easily enable this constraint
to be added.
The two documents mentioned in this article are designed to aid in the reproducibility of the work. One is a Word article
with editable tables, formulas, and charts. The other is an Excel workbook which contains creator data, network data,
descriptive statistics, regression output, rank co-movement matrix, context of 1,000 campaigns, comparisons of policies,
privacy estimates, data sources, and audit trails. Formula-based summary cells recalculate the means, conﬁdence
intervals, and the privacy-retention tradeoffs for the campaigns that were kept. Stochastic elements are created with ﬁxed
seeds, and the results are kept. This allows a reader to audit the exact numbers that were reported.
The workbook separates source and derived data and computational outputs and summary spreadsheets. Creator Data
has variables and network metrics; Campaign_Simulation has every context and policy performance score;
Policy_Comparison has policy-level summaries; Privacy_Value has decision-value retention; Regression_Models and
Spearman_Rank_Matrix have inferential outputs; and Audit_Trail has the quantitative equations. This separation
decreases the risk that a summary number becomes disassociated from its source data.
Additionally, the word article uses conservative language for unpublished or non-peer-reviewed work. The main
benchmark is cited as a public data source relating to the Data Availability statement instead of being reported as a peer-
reviewed empirical study. The scholarly references given are published works and the oﬃcial regulatory documents cited
in the text. DOI-bearing publications are supplied with full connections as https://doi.org/is required for auditability.
Page 19/24

A direct replication protocol is rather simple. First, import the public benchmark, and normalize truncated numeric ﬁelds.
Then, construct the aﬃliation graph using Eq. 1 and compute network metrics. Next, perform percentile rankings of the
variables of interest and then compute Equations 2–3. Next, generate 1,000 campaign contexts along with the four policy
rules, using a ﬁxed random seed. Then, calculate qualiﬁed engagements using Eq. 6 and perform the pairwise
comparison. Subsequently, compute decision-value retention using Eq. 7, and score perturbation, all under a ﬁxed random
privacy seed. Finally, check each generated table against the audit ranges in the workbook. There is no step involving a
subjective manual statistical adjustment.
A stronger ﬁeld validation would occur if the retailer implemented the adaptive policy with a randomized control
experiment. Here, all campaigns within a given product category would be segmented by geographic area, and some
media budget would be allocated to both the engagement-only and adaptive seeding approaches. All the estimates
would include reach, frequency, click-through rates, completed purchases, incremental sales, and exposure to adjacent
market segments. There would also be pre-registration of the score weights, as well as the primary performance score
prior to exposure. This would move the scholarly research in advertising more toward performance causality from a
computational decision-making perspective.
Stronger temporal network validation could measure interactions on bluesky. Shortest-path brokerage centrality,
community membership and engagement could be measured daily or hourly, and a diffusion propensity-velocity term
could describe change instead of a level. If brokerage velocity is reasonably high, a broker with moderate centrality may
outrank a falling account that was once the most central. The Temporal diffusion propensity scholarship provides a logic
basis for this approach (Meena et al., 2025), and current resources for Bluesky provide a unique and user-reproducible
testing environment (Quelle and Bovet, 2025; Smith et al., 2026).
More private portfolio publication could replace the score perturbation method with controlled private releases. One
alternative could release centrally bounded suﬃcient statistics; another, graph-tailored local differential privacy or privacy-
preserving computation. The sensitive units determine the appropriate method, and may be a feature of a user edge or a
local neighborhood or a campaign performance score. Therefore, privacy must be related to the real threat model, not
epsilon.
The proposed extensions deﬁne a coherent publication plan. This article offers a framework of interpretable adaptive
allocation and a basis for reproducible computation. A second article could provide large-scale, temporal replication of a
public social network. A third article could test causal campaign performance through ﬁeld experiments. A fourth article
could provide formal privacy guarantees and quantify the privacy–decision-value frontier for legally and technically
deﬁned data-release mechanisms. The sequence isn’t trying to perform causal analysis, operate at the general level, and
exhaust formal privacy from a single small public benchmark.
9. Conclusion
The authors determined if social network measurement can progress beyond associative rankings of creators and help
make a deﬁnitive ad placement decision. Within a 117 creator benchmark that is open, an ad market association network
was built from category and audience country similarity. The ranking of followers by size was found to be negatively rank-
co-moved with the average of all engagements, whereas shortest-path brokerage was positively rank-co-moved with
engagement. While these descriptions help, they do not simplify the audience size to the degree of conﬁdence in the
diffusion potential. Brokerage, however, could not be validated through additional regressions.
The primary evidence is the comparative static policy. For 1,000 ﬁxed campaign contexts, and a constant ﬁve-budget-
seed, the adaptive policy yielded a mean of 13.976 million qualiﬁed engagements. This was a 23.49% increase compared
to targeting engagements only, a 122.98% increase over targeting followers, and a 110.69% increase over targeting
Page 20/24

network brokerage. The estimates show that ratio and combined network brokerage, alongside recorded response,
contextual ﬁt, and redundant portfolio control, become the most relevant information. Single, static centrality is
insuﬃcient.
The privacy stress test found that the adaptive decision rule was resilient to moderate score noise. At epsilon 1, 94.10%
of the unperturbed decision value was retained. This estimate helps to make a case for data minimization, but does not
give a differential privacy guarantee. For this reason, the article uses a privacy-aware instead of a privacy-proven
framework. This leaves enough room for creativity and helps to identify the next step for this scholarship.
There is broader interdisciplinary value. Network science brings the broker and community structures; marketing brings
engagement and relevance and some logic of seeding. Privacy scholarship brings the decision-value risk perspective and
governance brings the requirement of auditable, purpose-limited data processing. The components are integrated into a
format which can be used and extended. It yields an exact result: in the given context, adaptive, controlled decision-value
redundancy signiﬁcantly outperformed the three commonly used decision-value bounds in the same objective and budget
scenarios.
For now, the next step should be to apply the same framework to the most recent temporal interaction graphs and test it
against real world online advertising estimates. The 2025–2026 Bluesky scholarship ecosystem shows that large public
network data could support this. Until this veriﬁcation is done, the numerical gains seen should only be considered
replicable computational evidence towards an allocation principle rather than an expected economic return.
Declarations
Data Availability and Reproducibility Assertion
The advertised benchmark creates an open-source code which can be found on the GitHub public benchmark. An
interpretation of the data as that of September 2022 has been made, and the benchmark has been used as simulated
current account data. The accompanying support workbook has been provided with this article. It contains the
calculation workbook, the Parameter_Register, downstream summary worksheets, retained outputs, policy comparisons,
privacy perturbation outputs, and a validity check called Cross-File-Check.
Ethics, Funding and Competing Financial or Nonﬁnancial Ties
The study uses a publicly available benchmark based on creator-level attributes. No private messages, personal contacts,
or non-public records of the platform will be collected. This is a procedural study, and no evaluation of individuals is
made. No resources were expended in this evaluation. Competitive ﬁnancial or nonﬁnancial interests are not reported.
According to the method used, scholars on live personal data are required to have ethics approval, contracts, and legal
approval from the related departments where applicable.
No competing ﬁnancial and/or non-ﬁnancial interests
I declare that the author has no competing interests as deﬁned by Springer, or other interests that might be perceived to
inﬂuence the results and/or discussion reported in this paper.
The research in this manuscript is Not supported by any funding?
The author hereby declares that this research did not receive any funding.
References
Page 21/24

1. Acquisti A, Taylor C, Wagman L (2016) The economics of privacy. J Econ Lit 54(2):442–492.
https://doi.org/10.1257/jel.54.2.442
2. Aral S, Walker D (2012) Identifying inﬂuential and susceptible members of social networks. Science 337(6092):337–
341. https://doi.org/10.1126/science.1215842
3. Bakshy E, Hofman JM, Mason WA, Watts DJ (2011) Everyone's an inﬂuencer: Quantifying inﬂuence on Twitter.
Proceedings of the Fourth ACM International Conference on Web Search and Data Mining, 65–74.
https://doi.org/10.1145/1935826.1935845
4. Blondel VD, Guillaume J-L, Lambiotte R, Lefebvre E (2008) Fast unfolding of communities in large networks. J Stat
Mech: Theory Exp 2008(10):P10008. https://doi.org/10.1088/1742-5468/2008/10/P10008
5. Borgatti SP (2005) Centrality and network ﬂow. Social Networks 27(1):55–71.
https://doi.org/10.1016/j.socnet.2004.11.008
6. Burt RS (2004) Structural holes and good ideas. Am J Sociol 110(2):349–399. https://doi.org/10.1086/421787
7. De Veirman M, Cauberghe V, Hudders L (2017) Marketing via Instagram inﬂuencers: The effect of number of
followers and product divergence on brand attitude. Int J Advertising 36(5):798–828.
https://doi.org/10.1080/02650487.2017.1348035
8. Fortunato S (2010) Community detection in graphs. Phys Rep 486(3–5):75–174.
https://doi.org/10.1016/j.physrep.2009.11.002
9. Freeman LC (1979) Centrality in social networks: Conceptual clariﬁcation. Social Networks 1(3):215–239.
https://doi.org/10.1016/0378-8733(78)90021-7
10. Goldfarb A, Tucker CE (2011) Privacy regulation and online advertising. Manage Sci 57(1):57–71.
https://doi.org/10.1287/mnsc.1100.1246
11. Government of India (2023) The Digital Personal Data Protection Act, 2023 (Act No. 22 of 2023). India Code.
https://www.indiacode.nic.in/indiacode/handle/123456789/22037
12. Granovetter MS (1973) The strength of weak ties. Am J Sociol 78(6):1360–1380. https://doi.org/10.1086/225469
13. Hao F, Zhao S, Gu T, Ma Y (2025) dK-DGDP: A differential privacy method on directed social network graphs.
Computers Secur 159:104647. https://doi.org/10.1016/j.cose.2025.104647
14. Hinz O, Skiera B, Barrot C, Becker JU (2011) Seeding policies for viral marketing: An empirical comparison. J Mark
75(6):55–71. https://doi.org/10.1509/jm.10.0088
15. Kempe D, Kleinberg J, Tardos É (2003) Maximizing the spread of inﬂuence via a social network. Proceedings of the
Ninth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 137–146.
https://doi.org/10.1145/956750.956769
16. McPherson M, Smith-Lovin L, Cook JM (2001) Birds of a feather: Homophily in social networks. Ann Rev Sociol
27:415–444. https://doi.org/10.1146/annurev.soc.27.1.415
17. Meena SK, Singh S, S., Singh K (2025) Pruning-enabled temporal inﬂuence maximization via antlion optimization.
Knowledge-Grounded Syst 317:113406. https://doi.org/10.1016/j.knosys.2025.113406
18. Ministry of Electronics and Information Technology (2025) Digital Personal Data Protection Rules, 2025. Gazette of
India, G.S.R. 846(E), 13 November 2025. https://www.meity.gov.in/documents/act-and-policies/digital-personal-data-
protection-rules-2025-gDOxUjMtQWa
19. Newman MEJ (2006) Modularity and community structure in networks. Proceedings of the National Academy of
Sciences, 103(23), 8577–8582. https://doi.org/10.1073/pnas.0601602103
20. Quelle D, Bovet A (2025) Bluesky: Network topology, polarization, and algorithmic curation. PLoS ONE
20(2):e0318034. https://doi.org/10.1371/journal.pone.0318034
Page 22/24

21. Smith AH, Amburg I, Kumar S, Foucault Welles B, Landry NW (2026) Sci Data 13:585.
https://doi.org/10.1038/s41597-026-06920-1. A Blue Start: A large-scale pairwise and higher-order social network
dataset
22. Traag VA, Waltman L, van Eck NJ (2019) From Louvain to Leiden: Guaranteeing well-connected communities. Sci Rep
9:5233. https://doi.org/10.1038/s41598-019-41695-z
23. Trusov M, Bucklin RE, Pauwels K (2009) Effects of word-of-mouth versus traditional marketing: Results from an
Internet social networking site. J Mark 73(5):90–102. https://doi.org/10.1509/jmkg.73.5.90
24. Tucker CE (2014) Social networks, personalized advertising, and privacy controls. J Mark Scholarsh 51(5):546–562.
https://doi.org/10.1509/jmr.10.0355
25. Watts DJ, Dodds PS (2007) Inﬂuentials, networks, and public opinion formation. J Consumer Scholarsh 34(4):441–
458. https://doi.org/10.1086/518527
Figures
Figure 1
Editable conceptual framework for Privacy-Aware Adaptive Diffusion-Propensity Mapping.
Figure 2
Selected Spearman rank associations among follower size, engagement and network structure. Native editable Word
table chart.
Figure 3
Page 23/24

Figure 4. Decision-value retention by epsilon under privacy-motivated score perturbation. Native editable Word table
chart.
Supplementary Files
This is a list of supplementary ﬁles associated with this preprint. Click to download.
PrivacyAwareAdaptiveDiffusionPropensityMappingAdvertisingTargetingSupportingEvidence.xlsx
Page 24/24
