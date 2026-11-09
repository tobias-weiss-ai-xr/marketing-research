---
title: 'Causal-driven attribution (CDA): estimating channel influence without user-level data'
url: https://arxiv.org/abs/2512.21211
category: analytics
subcategory: measurement
date: 2026-10
venue: Journal of Marketing Analytics
authors:
- Georgios Filippou
- Boi Mai Quach
- Diana Lenghel
source: arxiv
pdf_url: https://arxiv.org/pdf/2512.21211
pages: 30
chars: 118090
fetched_at: '2026-11-08T12:59:24+00:00'
kb_version: 1
---

# Causal-driven attribution (CDA): estimating channel influence without user-level data

Causal-driven attribution (CDA): Estimating channel
influence without user-level data
Georgios Filippou∗
School of Computer Science and Statistics
Trinity College Dublin
Dublin, Ireland
filippog@tcd.ie
Boi Mai Quach
School of Computer Science and Statistics
Trinity College Dublin
Dublin, Ireland
quachm@tcd.ie
Diana Lenghel
School of Computer Science and Statistics
Trinity College Dublin
Dublin, Ireland
dlenghel@tcd.ie
Arthur White
School of Computer Science and Statistics
Trinity College Dublin
Dublin, Ireland
arwhite@tcd.ie
Ashish Kumar Jha
Trinity Business School
Trinity College Dublin
Dublin, Ireland
akjha@tcd.ie
Attributionmodellingliesattheheartofmarketingeffectiveness,yetmostexistingapproachesdependonuser-levelpath
data, which are increasingly inaccessible due to privacy regulations and platform restrictions. This paper introduces a
Causal-Driven Attribution (CDA) framework that infers channel influence using only aggregated impression-level data,
avoidinganyrelianceonuseridentifiersorclick-pathtracking. CDAintegratestemporalcausaldiscovery(usingPCMCI)
with causal effect estimation via a Structural Causal Model to recover directional channel relationships and quantify
their contributions to conversions. Using large-scale synthetic data designed to replicate real marketing dynamics, we
show that CDA achieves an average relative RMSE of 9.50% when given the true causal graph, and 24.23% when using
the predicted graph, demonstrating strong accuracy under correct structure and meaningful signal recovery even under
structural uncertainty. CDA captures cross-channel interdependencies while providing interpretable, privacy-preserving
attribution insights, offering a scalable and future-proof alternative to traditional path-based models.
KeywordsMarketing attribution· Causal inference· PCMCI· Structural Causal Model· Privacy-first analytics· Digital
advertising
1 Introduction
“When budgets are tight, marketers need to justify every penny of their spend. But without full-funnel
attribution, spending decisions are often based on what is easy to measure rather than what is actually
working.”
— MarketingWeek, 20252
Since consumers now learn and respond to marketing stimuli in a multi-channel environment, more sophisticated
frameworks are required to evaluate whether investments across these channels actually generate the desired outcomes
∗Corresponding author: filippog@tcd.ie
2https://www.marketingweek.com/full-funnel-attribution/
arXiv:2512.21211v1  [stat.ML]  24 Dec 2025

Causal-Driven AttributionGeorgios Filippou
[Berman, 2018]. This motivation gives rise to the concept of marketing effectiveness, which represents the degree to
which marketing investments drive the desired results Solcansky and Simberova [2010].
However, measuring marketing effectiveness has become increasingly challenging in the digital era. Many researchers
haveemployeddiversemethodologiestoevaluateit,includingexperimentation,qualitativeandquantitativeobservational
analyses, econometric modelling, and machine learning approaches. Among these, statistical models have become
particularly prominent as rigorous tools for assessing marketing effectiveness [Zenetti et al., 2014, Han et al., 2023,
LaBrecque et al., 2024]. Organizations increasingly rely on such models to gain actionable insights guiding strategic
decisions, particularly regarding advertising budget allocation under uncertainty [Qin et al., 2024].
One of the most widely used statistical approaches for defining marketing effectiveness is marketing attribution Buhalis
and Volchek [2021]. It has received growing attention as both a methodological and theoretical challenge. Attribution
refers to assigning credit to different marketing touchpoints influencing customer purchase paths. Drawing from
attribution theory in psychology Kelley [1967], Heider [2013], this process involves determining causal relationships
between marketing stimuli and consumer responses.
The proliferation of entertainment and advertising platforms has added further complexity to understanding consumer
behaviour Schweidel et al. [2022]. Simultaneously, changes in digital privacy, particularly Apple’s iOS14 updates
Sokol and Zhu [2021], the European Union’s General Data Protection Regulation (GDPR) Li et al. [2019], and the
California Consumer Privacy Act (CCPA) Bonta [2022], have significantly restricted access to individual level data.
In a cross-channel interaction environment, where users can move freely across touchpoints and marketing messages
appear across numerous platforms and devices, these updates create significant difficulties for accurate measurement
due to the lack of data transparency throughout the consumer journey Cui et al. [2021].
Limited data availability creates what we term the “privacy-attribution paradox” where the need for sophisticated
attribution increases as data accessibility decreases. This paradox is compounded by both technical and conceptual
limitations that existing literature treats separately but are fundamentally interconnected. Technical limitations include
privacy restrictions, limited data access, and systematic mislabelling of traffic sources Starov et al. [2018], Filippou et al.
[2024]. Conceptual limitations arise from the model’s inability to provide transparent interpretability. The results often
fail to reveal the precise insights researchers seek. For example, we may desire to understand the causal relationships
between marketing channels rather than the correlations among them.
Furthermore, the emergence of view-first (or impression-first) entertainment platforms exemplifies these interconnected
challenges. Reiley et al. [2012] found that standard click-based models can misattribute the advertising impact by
assigning credit to clicks from users who were likely to convert regardless of exposure to the advertising. Users engage
deeply with content without necessarily clicking or transitioning to websites, creating influential but unmeasured
interactions. Academic research demonstrates that impressions without website visits can generate sales Ghose and
Todri-Adamopoulos [2016], while industry studies show significant impact of views and impressions on conversion
paths without clicks (TikTok for Business 20243; Snapchat for Business 20244).
Marketing practitioners are not able to analyse the full user journey since each ad platform tracks its own touchpoints.
ThiscreatesstructuralopacityindigitalattributionRomeroLeguinaetal.[2020]whichcouldleadtobiasedorincomplete
attribution outcomes. Thus, the analytical focus shifts from tracing individual paths to inferring the mechanisms that
generate them. This is where causal inference becomes essential Ghose and Todri-Adamopoulos [2016]. In the context
of marketing effectiveness, extracting valuable knowledge from the available data continues to be a challenge for both
scholars and practitioners. When cause and effect relationships are discovered, support the decision making process of
budget allocation Zhou et al. [2023].
Building on these challenges, our study offers two primary contributions. First, we present a theoretical approach that
integrates Structural Equation Modelling (SEM) into a temporal causal discovery framework for simulating marketing
attribution. Second, we introduces a novel causal-driven attribution (CDA) framework that works entirely on aggregated
impression-level data, solving the privacy and data-access limitations of traditional user-level models. To the best of
our knowledge, none of the existing models can fully reveal the causal relationships among touch points, including
determiningthedirectionofinfluencebetweenchannelsandquantifyingtheirimpactvalueswhileusingonlyaggregated
data.
The rest of the paper unfolds as follows. We begin with a review of the relevant literature, grounding our work in the
methodological foundations of attribution modelling. We then outline our data simulation process and walk through the
modelling approach in detail. This is followed by the presentation of key findings and an extensive model validation
3https://ads.tiktok.com/business/en/blog/beyond-click-attribution-views-impact-purchase
4https://forbusiness.snapchat.com/blog/evolving-measurement-neustar
2

Causal-Driven AttributionGeorgios Filippou
process. Finally, we close with a critical discussion of the results and what they mean for both future research and
applied marketing practice.
2 Literature review
2.1 Marketing effectiveness and consumer journey
Marketing effectiveness captures the extent to which marketing activities generate desired business outcomes such
as sales, revenue growth, customer acquisition, or brand lift Solcansky and Simberova [2010], Raman et al. [2012].
Although conceptually simple, evaluating effectiveness becomes increasingly complex once we account for how
consumers behave and how marketers attempt to influence that behaviour.
Classical theories framed the consumer journey as a linear progression from awareness to consideration to purchase
Singh and Yousuf [2024], a structure that made sense in a world with limited media channels. However, these linear
frameworks struggle to explain behaviour in contemporary ecosystems where consumers discover, evaluate, and engage
with brands across search engines, social platforms, video environments, review sites, apps, and offline stimuli Nam and
Cho [2025].
The cognitive foundations of such behaviour are well established. Consumers form knowledge structures through
repeated exposure Bettman [1970], rely on associative networks to store and retrieve brand information Alba and
Hutchinson [1987], and interpret marketing messages through attributional reasoning Heider [2013], Kelley [1967].
Digitalisationacceleratedtheseprocessesbyexpandingthenumberofavailabletouchpointsandenablingmulti-platform
navigation. Verhoefetal.[2015]demonstratethathowomni-channelenvironmentsblurtheboundariesbetweenphysical
and digital experiences, while recent work shows that consumers routinely search on Google, watch YouTube videos,
browse Instagram, and ultimately purchase offline Santos and Gonçalves [2024]. Understanding this fragmented and
recursive journey has therefore become central to enhancing marketing effectiveness.
From a managerial perspective, resource allocation theory further complicates the challenge. Behavioural theories
emphasise that managers operate under bounded rationality, seeking solutions that are “good enough” rather than fully
optimalSimon[1955]. Asaresult,organisationsmustmakedecisionsunderconditionsofinformationoverload,internal
negotiation, and limited analytical capacity March and Simon [1993].
CyertandMarch[2020]arguethatfirmsdonotoptimiseinthetextbooksense. Instead, theyrelyonroutines, satisficing,
and sequential budget adjustments shaped by internal bargaining. As media channels proliferate and privacy constraints
reduce the availability of granular data, these behavioural limitations become even more pronounced. Recent work
highlights the deep uncertainty marketing leaders face when evaluating investment effectiveness, thereby increasing
demand for reliable and transparent measurement frameworks Malter et al. [2020].
Within this context of behavioural complexity, fragmented data, and managerial uncertainty, attribution modelling has
emerged as a central tool for accountability and optimisation.
2.2 Marketing Attribution
2.2.1 The heuristic attribution era
The early days of marketing attribution relied on pre-defined rules that assigned credit to specific marketing touchpoints
Donndelinger and Ferguson [2020]. Google’s attribution framework, developed between 2006 and 2015, introduced
heuristic models such as first-interaction, linear, time-decay, position-based, and last-click Gaur and Bharti [2020], Gaur
et al. [2024]. These rule-based models quickly became popular among practitioners and researchers in online marketing,
and many of them remain in use today.
Out of the various options and models, last-click, which assigns 100% of the credit to the final touchpoint before
conversion, gained significant traction as the main choice for both businesses and media companies. Despite its
conceptual weaknesses, last-click became the industry default. However, the adoption of last-click attribution increased
even as criticism mounted Kufile et al. [2023]. This persistence reflects organisational behaviour: under uncertainty,
firms gravitate toward simple and interpretable rules, even when these rules are inaccurate or questionable.
With the rise of digital media over the past decade, consumers have more options to engage with brands across multiple
platforms. Likewise, brands are able to distribute their content and advertising message in more platforms Dens and
Poels [2023]. As a result heuristic models struggled to provide sufficient information around the channel which was
solely responsible for key business activities such as purchases Tao et al. [2025].
3

Causal-Driven AttributionGeorgios Filippou
First, it reflects reductive assumptions about consumer behaviour and fails to capture the full influence of earlier
marketing interactions El Mekkaoui and Benyoussef [2024]. Second, researchers highlight the increasingly non-linear
natureofconsumerjourneysSantosandGonçalves[2024]. Contemporaryconsumerbehaviourtheoryrecogniseshighly
fragmented journeys in which users move across multiple devices and platforms, interacting with both organic and paid
content before making purchase decisions Nam and Cho [2025].
To mitigate these challenges, researchers came up with a different approach: data-driven models Romero Leguina et al.
[2020]. For some, data-driven models are considered as “next generation attribution models” because they are grounded
in mathematical and statistical methods rather than pre-defined rules.
2.2.2 The data-driven attribution era
Consumers now engage with brands across multiple platforms and devices Berman [2018], Santos and Gonçalves
[2024], Nam and Cho [2025], while brands have simultaneously expanded their presence across an increasing number
of digital touchpoints Dens and Poels [2023]. This behavioural shift created the need to analyse entire paths rather
than isolated events. Consequently, data-driven attribution models emerged as a methodological evolution, designed to
process path data, meaning the full sequence of user touchpoints before conversion, and thereby capture the complexity
of modern consumer journeys Hui et al. [2009], Kannan et al. [2016]. Several data-driven methods currently support
marketing attribution decisions. Below, we highlight the approaches that have shaped the industry and discuss recent
developments and emerging trends.
Shapley values, borrowed from cooperative game theory, provide an elegant mathematical framework for distributing
creditacrossmarketingtouchpointsShapleyetal.[1953]. Earlyworkdemonstratedtheversatilityofinfluence-attribution
methodologies, which opened the door to marketing applications Papapetrou et al. [2011]. The method was first
pioneered for marketing use in work that positioned it for practical application while acknowledging the limitations
of observational data Dalessandro et al. [2012]. The approach is theoretically sound: it calculates each touchpoint’s
marginal contribution across all possible combinations and then assigns proportional credit. Later research improved
computationalefficiency,incorporatedchannelsynergies,andexpandedthemethod’sapplicabilityYadagirietal.[2015],
Nisar and Yeung [2015], Zhao et al. [2018]. Further developments also introduced hybrid approaches that combine
Shapley values with complementary modelling techniques Kadyrov and Ignatov [2019].
MarkovchainsofferedanalternativeframeworkbymodellingconsumerjourneysasprobabilisticstatetransitionsPfeifer
andCarraway[2000],Homburgetal.[2009]. The“adgraph”conceptwaslaterintroducedtorepresentjourneysasgraphs
in which nodes capture ad events and edges encode transition probabilities Archak et al. [2010]. This approach proved
effective for identifying path dependencies and drop-off points, a conclusion supported by comprehensive empirical
validation comparing simple, forward, and backward Markov chains Anderl et al. [2014]. Subsequent extensions further
demonstrated its applicability across industries Kakalejčík et al. [2018], Sandeep et al. [2021].
Theintegrationofmachinelearning(ML)intoattributionmodellingprovidesarigorous,data-drivenapproachcapableof
detectingpatternsincustomerbehaviourandassessingthemarginalinfluenceofeachtouchpoint. Forinstance,Shaoand
Li [2011] introduced bagged logistic regression for attribution. It is worth mentioning, their work was the first published
use of the term “data-driven attribution.” Subsequent studies have developed models that distinguish between short- and
long-term effects across cohorts Breuer and Brettel [2012], as well as parametric and non-parametric frameworks that
account for spillover effects Li and Kannan [2014]. Amazon’s MTA approach leverages both randomized controlled
trials (RCTs) and machine learning models to determine how conversion credit should be distributed across Amazon
Ads touchpoints Lewis et al. [2025]. Other advances apply survival analysis to capture time-decay dynamics Zhang et al.
[2014] and utilise hazard-rate modelling to quantify the influence of individual ad exposures Ji and Wang [2017].
Building on these ML-based advances, deep learning methods have recently been applied to the MTA problem,
offering the ability to model nonlinear interactions, temporal dependencies, and user heterogeneity at scale. The Deep
Neural Net with Attention (DNAMTA) model integrates attention mechanisms to account for temporal effects and user
characteristics, achieving strong predictive performance while producing interpretable touchpoint-level contribution
estimates Arava et al. [2018]. The Dual-Attention Recurrent Neural Network (DARNN) further advances this idea by
learning attribution weights directly from the conversion objective through a dual-attention architecture, dynamically
allocating credit across a user’s full exposure sequence Ren et al. [2018]. Complementing these approaches, DeepMTA
combinesphased-LSTMnetworkswithanadditiveattributionmethodbasedonShapleyvalues,deliveringbothaccurate
conversion prediction and transparent explanations of each touchpoint’s marginal effect Yang et al. [2020]. Collectively,
these deep learning frameworks demonstrate how neural models can capture richer temporal structure and provide more
interpretable attribution estimates than traditional methods.
4

Causal-Driven AttributionGeorgios Filippou
2.3 The causal imperative
Imagineamarketerrunningasalecampaignacrossseveralchannels,includingemail,social,anddisplay. Historicaldata
may show that customers who receive more email messages tend to convert at higher rates. However, choosing the most
effective channels remains challenging because correlations do not reveal the true incremental effect of each touchpoint.
For instance, even if higher email volume coincides with higher conversions, it would be misleading to attribute all of
those conversions to email. Many of these users may have already formed their purchase intent through other channels,
such as search or social media, long before the email was delivered. Therefore, correlation-based attribution models can
misallocate credit across channels because they are incapable of distinguishing true causal effects from correlations.
Causal inference and marketing effectiveness have become increasingly intertwined Hair Jr and Sarstedt [2021], a
shift fuelled by advances in data availability, experimental design, and machine learning. The emphasis on causality
has moved the field beyond correlational attribution toward frameworks aimed at identifying true cause–and-effect
relationships. Conceptually, this transition reflects a broader recognition that understanding why marketing works is
essential for credible measurement and strategic decision-making Zhou et al. [2023].
Causal-based approaches to multitouch attribution address the limitations of correlational models by estimating the
incremental effect of each advertising touchpoint. Dalessandro et al. [2012] frame attribution as a causal estimation
problem, using Shapley values to allocate credit based on each ad’s marginal effect. Kumar et al. [2020] introduce
CAMTA, a causal recurrent neural network model designed to account for time-varying confounders and reduce
selection bias, although its use of click behaviour as pseudo-feedback may introduce additional sources of bias. Yao
etal.[2022]presentCausalMTA,whichaimstoeliminateconfoundingbiasfrombothstaticuserattributesanddynamic
behavioural features through counterfactual prediction. Tang [2024] advances this line of research with DCRMTA, a
deep causal representation model that isolates causal features linking user behaviour to conversion while reducing the
influence of confounding variables.
Different from the individual-level data used in most studies, Kireyev et al. [2016] utilise a dataset consisting only
of aggregate consumer behaviour to examine the dynamic interaction between paid search and display advertising.
They combine time-series analysis with Granger causality to identify cross-channel spillovers and broader advertising
dynamics. However, Granger causality does not constitute true causal inference Shojaie and Fox [2022]. It shows only
that past values of one time series improve the prediction of another, not that one variable exerts a causal effect from the
traditional causal-inference sense.
2.4 Structural challenges in attribution
Most established attribution techniques, including Shapley value models, Markov chains, deep learning architectures,
and even recent causal MTA frameworks, depend on granular, event-level behavioural data to reconstruct user paths.
However, in a privacy-first ecosystem shaped by regulations such as GDPR Li et al. [2019], CCPA Bonta [2022], and
platform-level changes such as Apple’s iOS14 Sokol and Zhu [2021], access to persistent identifiers has been severely
restricted. As a result, the data required to support these models has become increasingly unavailable, inconsistent, or
systematically mislabelled Starov et al. [2018].
Furthermore,agrowingshareofdigitalengagementnowoccursinchannelsthatdonotproduceclick-basedsignals. The
industry has been massively shaped by short-form video, influencers, connected TV, and impression-first entertainment
platforms Yuan et al. [2022]. These environments generate meaningful behavioural impact through exposure rather
than direct interaction. Ghose and Todri-Adamopoulos [2016] indicate that impressions without website visits can
materially influence conversions. Evidence from Filippou et al. [2024] further demonstrates that media exposure can
influence outcomes indirectly, for example by increasing organic branded searches that do not appear in click sequences.
Traditional path-based attribution, which relies on sequences of clicks or identifiable transitions, cannot capture these
impression-driven effects.
The marketing productivity literature consistently argues that marketing investments should be evaluated based on
their causal contribution to business outcomes Sheth and Sisodia [2002], Morgan et al. [2002], Rust et al. [2004].
Correlation-based attribution models, whether heuristic or data-driven, are prone to biased estimates, particularly in
environments characterized by endogenous targeting, cross-channel spillovers, and unobserved confounders. In the
absence of causal evidence, budget allocations can become systematically distorted, limiting firms’ ability to assess true
ROI.
2.5 Towards a new paradigm
Industry practice and academic literature increasingly converge on the same conclusion: today’s environment exposes
a critical measurement gap. Existing attribution frameworks break down when only aggregated or impression-level
5

Causal-Driven AttributionGeorgios Filippou
data are available, particularly for smaller or emerging channels that do not provide persistent user identifiers Cui et al.
[2021], Ghose and Todri-Adamopoulos [2016]. They also fail when user journeys are unobservable due to regulatory
changes, when touchpoints do not generate clicks as in impression-first platforms, and when privacy constraints prohibit
the collection of path-level behavioural data (as discussed in Section 2.4).
While a business could build complex API integrations across multiple platforms to capture user-level path data, it
must carefully weigh the trade-off between adopting a new solution and maintaining the existing one at a high and
potentially unsustainable infrastructure cost. Even with sufficient data, certain traditional MTA and deep learning
models can be difficult to deploy due to their heavy computational requirements. Singh and Yousuf [2024] emphasise
that computational efficiency is essential for modern customer-journey analytics, and models that require excessive
computing resources are unlikely to be adopted in practice.
Itisevidentthatthereisaneedforanewfamilyofattributionmethodologies. Theshiftfromindividualtoaggregatedata,
fromcorrelationtocausation,andfromclickstoimpressionsreflectsmorethanamethodologicalevolution. Itrepresents
a fundamental reconceptualization of marketing measurement, one that aligns with how consumers behave and how
privacy-conscious societies choose to govern their data. Our framework offers one step toward this reconceptualization.
Our work advances this direction through a causal-driven attribution (CDA) methodology that:
1. Operates entirely on impression-level, aggregated time-series data.
2. Explicitly designed for privacy-restricted environments.
3. Accommodates channels that do not generate user-click signals.
4. Identifies both direct and indirect causal relationships across marketing touchpoints.
5. Remains computationally lightweight and accessible to advertisers without complex data engineering require-
ments.
3 Methodology
3.1 Data Generation
Data accessibility for advertisers has been significantly affected by both regulatory and industry changes Wernerfelt
et al. [2025]. For instance, accessing user-level data typically requires API access (Facebook, 2025)5. However, using
marketing APIs effectively also demands additional infrastructure, which is often available only to larger corporations
Simon [2021]. Additionally, Cui et al. [2021] clearly outlined the challenges associated with multi-touch attribution and
how data limitations hinder its application.
Initially, we aimed to obtain a dataset that would enable a comparison between traditional multi-touch attribution
methods and our proposed approach. However, after nearly two years of exploration, we were unable to find a suitable
dataset. To the best of our knowledge, all existing publications on advertising and causal learning rely on only two
publicly available datasets Job et al. [2025], neither of which meets the requirements for this work. Due to the lack
of ground truth in real-world causal marketing data, simulation has played a vital role in method development and
evaluation Herman et al. [2025].
Motivated by these challenges, we developed an approach that allowed us to generate a synthetic dataset. Our aim is not
only to create a comprehensive and representative marketing dataset but moreover to be able to establish the so-called
ground truth required for model validation, thereby bypassing the problem of insufficient data.
We acknowledge that real marketing data cannot be perfectly simulated due to hard-to-model factors such as customer
awareness and behaviour are influenced by psychological aspects. Therefore, several simplifying assumptions were
made to ensure that our causal-driven attribution model can potentially be applied in real-world scenarios. Based
on these assumptions, we incorporated baseline impressions, growth rate, and conversion rate for each channel, as
well as random noise to capture variability. Cross-influence of marketing channels introduced as the last step. By
incorporating cross-influence, we are able to have channels as confounding variables which is essential for causal
inference conversation Suttorp et al. [2015].
3.1.1 Causal DAG Graph
Beforecrunchinganynumbers, wefirstneedahigh-levelunderstandingofthecausalrelationshipsamongourmarketing
channelsinordertodefinethescenarioforwhichwewillgeneratedata. Correlationonlydescribesstatisticalassociations
5https://developers.facebook.com/docs/graph-api/overview
6

Causal-Driven AttributionGeorgios Filippou
Figure 1: Example of a DAG’s structure, including nodes:Affiliates,Facebook,TikTok,Google Ads,YouTube, and
conversion. Edgesrepresentdirectedcausalinfluences: greenarrowsindicatepositivevalues(putativeamplification/halo),
and red arrows indicate negative values (putative substitution/crowd-out). Nodes are grouped into causal layers as
follows:𝑆 3:Affiliates,𝑆 2:Facebook,TikTok,Google Ads,𝑆 1:YouTube,𝑆 0:conversion.
between variables and cannot answer questions such as “Does changing the value of Channel A lead to a change
in Channel B?” To simulate realistic marketing behaviour, we need a visual representation of the underlying causal
structure, and this is where Directed Acyclic Graphs (DAGs) come into play.
Pearl [2009] explains that DAGs provide a natural way to represent causal structures. Causal effects arise from
underlying, unobserved processes that can be viewed as the equilibrium outcomes of a system of behavioural equations,
which themselves form a simplified model of how the world operates. Graph notation captures this structure efficiently:
nodes represent random variables that arise from some underlying data-generating process, and arrows indicate causal
influence between variables. The direction of each arrow corresponds to the direction of causality. The acyclic property
ensures that the graph does not contain feedback loops, which prevents circular causation and preserves clarity in causal
interpretation. Additionally, causal effects may be direct (e.g.,𝑋→𝑌 ), or indirect (e.g.,𝑋→𝑍→𝑌 ), where the
influence is transmitted through a mediating variable.
A directed acyclic graph (DAG)G is a visual structure consisting of a set of nodes (vertices)V and a set of directed
edges (arrows)E. Each nodeV𝑖 is associated with a random variable𝑋𝑖. In a DAG, there are no directed paths that
begin and end at the same node. Formally, no cycles exist such that a path starts atV𝑖 and returns toV𝑖 (either directly
or indirectly). A finite set𝑆denotes the causal layers (also known as a non-signalling set), which are subsets of nodes
that are causally independent (i.e., nodes within the same layer cannot signal to one another) Giarmatzi [2019], Nashed
et al. [2025]. Figure 1 illustrates the structure of a DAG, including its nodes, edges, and layered decomposition.
Recent literature highlights a growing trend toward using DAGs as an uncertainty-aware and interpretable tool for
visualizing causal graphs Xie et al. [2020]. DAGs provide a transparent way to distinguish causal influence from
correlation. Inmarketingattribution,theymapthestructuralrelationshipsamongchannelsandoutcomes,clarifyinghow
touchpointsinteract,mediate, orconfoundoneanotherthroughouttheconsumerjourney. Figure2illustratesanexample
ofcausalDAGsinamarketingcontextandshowshowchannelsinteractandultimatelyinfluenceconversions. According
to the generated DAGs, we can build mathematical equations based on the following part to run the simulation.
3.1.2 Assumptions and Equations
We acknowledge that real marketing data cannot be perfectly simulated due to hard-to-model factors such as customer
awareness and behaviour are influenced by psychological aspects. Additionally, since causal mechanisms in real-world
marketing systems are known with high uncertainty Runge et al. [2019], Brouillard et al. [2025], the simulation must
reflect the properties of the real datasets on which the algorithms will be applied. This is necessary to ensure that our
causal-driven attribution developed using simulated data can potentially translate to real-world scenarios.
7

Causal-Driven AttributionGeorgios Filippou
Figure 2: Example of a causal DAG showing the structural relationships among marketing channels. Some channels act
as upstream drivers that influence conversions indirectly through intermediate touchpoints, while others have a direct
impact on the outcome. All effects flow in a single direction with no circular feedback, providing a clear view of how
influence moves through the system.
A standard linear equation has been widely used to model the activity changes of each channel Danaher and van Heerde
[2018], Zhao et al. [2019a]. Suppose𝑥𝑡 represents the number of impressions for channel𝑋=(𝑥 1,𝑥 2...𝑥𝑡,𝑥𝑡+1...) at
time𝑡; the linear trend is defined as follows:
𝑥𝑡 =𝛼+𝛽𝑡+𝜖 𝑡,(1)
where𝑥𝑡 is the channel value at time𝑡,𝛼 represents the baseline impressions,𝛽 is the growth rate of the channel, and𝜖𝑡
denotes the random noise.
The next step was to establish the cross-influence between channel coefficients. Taking two channels as an example, let
𝑋1 representSearch advertising6 and𝑋2 denoteSocial advertising7. Each channel still follows a linear model; however,
they now influence each other directly within the same time period𝑡(i.e., no lag), as follows:
𝑥1,𝑡 =𝛼 1+𝛽 1𝑡+𝑤 12𝑥2,𝑡+𝜖 1,𝑡,
𝑥2,𝑡 =𝛼 2+𝛽 2𝑡+𝑤 21𝑥1,𝑡+𝜖 2,𝑡, (2)
where𝑥1,𝑡 and𝑥2,𝑡 represent the impression amounts ofSocial AdsandSearch Adsat time𝑡, respectively;𝛼1 and𝛼2
denote the baseline impressions for each channel;𝛽1 and𝛽2 are their respective growth rates;𝜖1,𝑡 and𝜖2,𝑡 represent
random noise terms.
More importantly,𝒘12 measures how muchSocial AdsinfluenceSearch Ads, and𝒘21 measures how muchSearch Ads
affectSocial Ads. These terms capture the directional causal effects between channels. Without them, the relationship
would represent only correlation rather than causation.
Extending the idea to multiple channels, each channel’s activity is determined not only by its own trend but also by the
concurrent activity levels of the other channels (no lag):
6Search advertising:We refer to Search advertising (Search Ads) as a form of paid digital marketing in which advertisers bid to
display sponsored messages alongside organic search results on search engines such as Google or Bing.
7Socialadvertising:WerefertoSocialadvertising(SocialAds)aspaiddigitalcommunicationdeliveredthroughsocialnetworking
platforms such as Facebook, Instagram, TikTok, or LinkedIn. It allows advertisers to target audiences based on demographic,
psychographic, and behavioral data.
8

Causal-Driven AttributionGeorgios Filippou
𝑥𝑖,𝑡 =𝛼 𝑖+𝛽 𝑖𝑡+
∑︁
𝑗≠𝑖
𝑤𝑖𝑗𝑥𝑗,𝑡+𝜖𝑖,𝑡,(3)
where𝛼𝑖 and𝛽𝑖 represent the baseline and growth trend of channel𝑖, respectively, while𝑤𝑖𝑗 measures how the current
activity of channel𝑗influences channel𝑖.𝜖 𝑖,𝑡 denotes the random noise term for channel𝑖.
Next, we transition from impressions to conversions per channel using the following relationship:
𝑦𝑡,𝑖 =𝛾 0+
𝑁∑︁
𝑖=1
𝛾𝑖𝑥𝑖,𝑡+𝜂𝑡,(4)
where 𝑦𝑡,𝑖 denotes the number of conversions for channel𝑖, 𝛾𝑖 represents the effectiveness of channel𝑖, and𝜂𝑡 is
the random noise term. This formulation captures the direct, concurrent (no-lag) causal influence among marketing
channels.
Lastly, the total number of conversions at each time step𝑡 can be expressed as the sum of baseline (non-marketing)
conversions and the conversions attributed to all marketing channels.
𝐶𝑡 =𝐵 𝑡+
𝑁∑︁
𝑖=1
𝑦𝑡,𝑖,(5)
where𝐶𝑡 represents the total conversions at time𝑡,𝐵𝑡 is the baseline component capturing conversions not driven by
advertising activities (e.g., organic or repeat behavior), and𝑦𝑡,𝑖 corresponds to the conversions generated by marketing
channel𝑖at the same time step.
Thissimulationintegratesbothorganicandpaidcontributionstooverallperformance, allowingthemodeltodisentangle
the inherent baseline trend from the incremental impact of each channel. It provides a comprehensive view of how
marketing efforts collectively contribute to total conversions while maintaining interpretability at the channel level.
Figure 3 illustrates the structure of the proposed simulation framework for generating synthetic causal marketing
attribution data. The process begins with user-defined inputs that specify the simulation context. These include: (1)
the set of marketing channels and their associated activities (e.g., impressions) along with the target key performance
indicator (KPI) such as conversions; (2) the time period over which the simulation runs (e.g., 365 days); (3) a baseline
range representing conversion levels independent of media activity; (4) the conversion-rate range for each channel,
which determines the direct impact of media exposure on conversions; and (5) the parent–child influence weight range,
capturing indirect effects that arise from causal dependencies among channels.
Given these inputs, the simulation module produces two categories of outputs. The first is the time-series data of daily
or weekly impressions and conversions for each channel (as shown in Figure 4), reflecting both direct and mediated
effects. The second is a causal graph with corresponding impact values that quantify the impact values and direction of
relationships among channels and between channels and the target KPI (Figure 5). Together, these outputs enable the
analysis of causal influence and attribution in a controlled, reproducible environment.
3.2 Modelling
Attribution is fundamentally a cause-and-effect problem. Understanding causality in attribution is a core challenge for
any discipline that involves decision-making under uncertainty Kelly et al. [2018]. A causal model identifies and maps
the qualitative cause-and-effect relationships and combines them with quantitative information about the strengths of
those relationships. Therefore, our approach uses a two-stage framework: first, we discover the causal relationships
among marketing channels; then we estimate the causal influence (weights) of each channel on the target KPI (e.g.,
conversions).
3.2.1 Causal DAG Discovery
Through data simulation, we can obtain the causal relationships between channels and conversions. In reality, however,
businesses typically have only time series data representing channel activities and total conversions over time, similar
to the simulated multi-channel dataset with the schema shown in Table 1. In practice, incrementality has become a
common approach to measure causality, as it identifies what actually caused a lift in performance. A causal DAG can
be constructed using prior knowledge combined with numerous tests, such as lift tests or A/B experiments. However,
9

Causal-Driven AttributionGeorgios Filippou
Figure 3: Overview of the simulation framework.
this expert-driven, test-and-iterate approach is expensive and time-consuming. Discovering the causal structure that
governs the relationships among variables purely from observational data remains a challenging and valuable problem.
In this work, we apply PCMCI, an automated procedure for discovering causal graphs based on graphical causal
modeling and conditional independence principles. Moreover, PCMCI scales effectively to large time series datasets
and accommodates linear, nonlinear, and time-delayed dependencies.
Table 1: Schema of the simulated multi-channel marketing dataset.
Column Type Description
indexinteger Time step index (e.g., day or week).
conversionfloat Total conversions across all marketing channels.
channel_1_impressionfloat Impressions from marketing channel 1.
channel_2_impressionfloat Impressions from marketing channel 2.
channel_3_impressionfloat Impressions from marketing channel 3.
...... ...
channel_n_impressionfloat Impressions from marketing channel𝑛.
Note:The dataset contains 365 daily observations across𝑛simulated marketing channels. Each row corresponds to a
single time step, including the number of impressions per channel and total conversions.
CausalnetworkdiscoverywithPCMCIConsideranunderlyingmultivariatetimeseries X𝑡 = 𝑋(1) 𝑡 ,𝑋(2) 𝑡 ,...,𝑋 (𝑑) 𝑡 ,
where each component represents the daily activity of a marketing channel (e.g., Facebook Ads, TikTok, Google Ads,
Affiliates). Ourobjectiveistoinferthecausalstructuregoverninghowpastchannelactivitiesinfluencecurrentoutcomes.
10

Causal-Driven AttributionGeorgios Filippou
Figure4: Arandomsimulateddataillustratingmarketingchannelimpressionsandconversionswithin365days. Thetop
panel presents the impression trends for five marketing channels, including Google Ads, Affiliates, TikTok, Facebook,
and YouTube. Each series follows a distinct stochastic pattern generated from a linear growth process with random
noise and inter-channel influence.
Figure 5: Example of a DAG output representing multi-channel interactions from randomly simulated data. Each
node represents a marketing channel (Affiliates, Google Ads, TikTok, Facebook, YouTube) or the target outcome
(Conversions). Directed arrows denote causal influence between nodes, where the direction of the arrow indicates the
flow of information from cause to effect. Green arrows correspond to positive causal weights, indicating that an increase
in the originating channel’s activity leads to a subsequent increase in the target channel or conversions.
Time lag𝜏, also know as “time-delay causality”, refers to the temporal interval between a cause and its effect. We
assume finite-order temporal dependencies up to a maximum lag𝜏max and seek, for each variable𝑋(𝑖) 𝑡 , to estimate the
11

Causal-Driven AttributionGeorgios Filippou
set of causal parents
P(𝑋(𝑖) 𝑡 )⊆  𝑋(𝑗) 𝑡−𝜏

 1≤𝑗≤𝑑,1≤𝜏≤𝜏 max 	 .(6)
PCMCI proceeds in two stages. In the first stage, a PC1 condition-selection step identifies relevant conditioning sets
bP(𝑋 𝑗 𝑡) for each variable𝑋𝑗 𝑡 . Starting from all lagged variables up to𝜏max, variables that are conditionally independent
of the target given subsets of the remaining candidates are removed using a conditional independence test (e.g., partial
correlation, ParCorr) performed at significance level𝛼PC.
In the second stage, PCMCI applies the Momentary Conditional Independence (MCI) test to evaluate whether a lagged
variable𝑋 𝑖 𝑡−𝜏 is a causal parent of𝑋𝑗 𝑡 . For each variable pair, MCI tests
𝑋𝑖 𝑡−𝜏 ̸⊥ ⊥𝑋𝑗 𝑡

 bP(𝑋 𝑗 𝑡)\{𝑋 𝑖 𝑡−𝜏}, bP(𝑋 𝑖 𝑡−𝜏),(7)
using an appropriate conditional independence test (e.g., ParCorr) at significance level𝛼MCI. If the null hypothesis of
conditional independence is rejected, the directed lagged edge𝑋𝑖 𝑡−𝜏 →𝑋 𝑗 𝑡 is included in the estimated causal graph.
Pseudocode 1 summarizes the full PCMCI procedure implemented in this study.
3.2.2 Causal Effect Estimation
In this section, we demonstrate how our proposed method quantifies causal effects under linear structural dependencies.
To estimate the causal contribution of each marketing channel to conversions, we use a Structural Causal Model (SCM)
implemented with theDoWhyframework8. An SCM represents each variable𝑋𝑖 through a structural equation
𝑋𝑖 =𝑓 𝑖
P(𝑋 𝑡 𝑖),𝑁 𝑖 ,(8)
whereP(𝑋 𝑡 𝑖) denotes the causal parents of𝑋𝑡 𝑖 and𝑁𝑖 is an exogenous noise term. After inferring the causal graph, each causal mechanism𝑓𝑖 is estimated directly from the observed data.
In causal inference, several estimands characterize the effect of an intervention, including the Average Treatment Effect
(ATE), theConditional Average Treatment Effect (CATE), theIndividual Treatment Effect (ITE),the Average Treatment
Effect on the Treated (ATT), the Average Treatment Effect on the Controls (ATC), and the Local Average Treatment
Effect (LATE) Imbens and Rubin [2015], Cheng et al. [2022]. Each estimand contrasts potential outcomes under
treatment(𝑇=1) and control(𝑇=0) , but they differ in how the averaging is performed and which subpopulations are
targeted.
In our setting, each observation is generated by a structural causal model and corresponds to a specific configuration of
channel impressions and contextual covariates. Therefore, the causal effect of a marketing channel on conversions must
be evaluatedconditionalon these observed features. The CATE is well suited for this purpose, as it measures how the
expected conversion outcome changes when a specific channel is intervened upon (e.g., setting its impression level to
zero) while holding all remaining covariates fixed.
To quantify the effect of removing a particular marketing channel, we express the intervention using the do-operator.
Let𝑋𝑗 denote the activity of channel𝑗 (e.g., impressions),𝑌𝑡 the conversion outcome, and𝑍𝑡 the collection of all other
observed covariates at time𝑡. We consider a binary intervention in which the channel is either kept at its normalized
active level (𝑋𝑗 =1) or entirely removed (𝑋𝑗 =0). The CATE of channel𝑗at covariate profile𝑧is then
Δ𝑗(𝑧)=E

𝑌𝑡

 do(𝑋𝑗 =1), 𝑍𝑡 =𝑧  −E  𝑌𝑡

 do(𝑋𝑗 =0), 𝑍𝑡 =𝑧  ,(9)
and we approximate these conditional expectations by generating interventional samples from the fitted SCM while
conditioning on the empirical distribution of𝑍𝑡.
Becausethesecounterfactualexpectationsarenotavailableinclosedform, weestimatethemusinginterventionalMonte
Carlo sampling. For each run𝑖, we generate two sets of interventional samples conditioned on the observed covariates
𝑍𝑡 =𝑧 : one under the interventiondo(𝑋𝑗 =1) and one underdo(𝑋𝑗 =0) . This yields empirical means𝑌 do(𝑋 𝑗=1),𝑖 and
𝑌 do(𝑋 𝑗=0),𝑖 . Over𝑛runs, the conditional causal effect of channel𝑗at covariate profile𝑧is then estimated by
bΔ𝑗(𝑧)= 1 𝑛 𝑛∑︁ 𝑖=1  𝑌 do(𝑋 𝑗=1),𝑖 −𝑌 do(𝑋 𝑗=0),𝑖  ,(10)
which converges to the true CATEΔ𝑗(𝑧)as𝑛increases.
8https://www.pywhy.org/dowhy
12

Causal-Driven AttributionGeorgios Filippou
Algorithm 1PCMCI for multivariate time series causal discovery
1:Input:Multivariate time series{X 𝑡}𝑇 𝑡=1 with𝑑variables; maximum lag𝜏 max; thresholds𝛼PC and𝛼 MCI.
2:Output:Set of directed lagged edgesE.
3:Construct candidate parent sets:
P0(𝑋(𝑖) 𝑡 )=  𝑋(𝑗) 𝑡−𝜏

 1≤𝑗≤𝑑,1≤𝜏≤𝜏 max 	 .
4:Stage 1: PC condition selection
5:for𝑖=1to𝑑do
6:P(𝑋 (𝑖) 𝑡 )←P 0(𝑋(𝑖) 𝑡 )
7:𝑘←0
8:whileconditioning sets of size𝑘existdo
9:for all𝑋 (𝑗) 𝑡−𝜏 ∈P(𝑋 (𝑖) 𝑡 )do
10:For allZ⊆P(𝑋 (𝑖) 𝑡 )\{𝑋 (𝑗) 𝑡−𝜏}with|Z|=𝑘, test:
𝐻0 :𝑋 (𝑗) 𝑡−𝜏 ⊥ ⊥𝑋(𝑖) 𝑡

 Z.
11:ifany𝑝 >𝛼 PC then
12:Remove𝑋 (𝑗) 𝑡−𝜏 fromP(𝑋 (𝑖) 𝑡 )
13:end if
14:end for
15:𝑘←𝑘+1
16:end while
17:end for
18:Stage 2: MCI testing
19:E←∅
20:for𝑖=1to𝑑do
21:for all𝑋 (𝑗) 𝑡−𝜏 ∈P(𝑋 (𝑖) 𝑡 )do
22:Define the MCI conditioning set:
ZMCI=P(𝑋 (𝑖) 𝑡 )\{𝑋 (𝑗) 𝑡−𝜏}.
23:Test the dependence condition:
𝑋(𝑗) 𝑡−𝜏 ̸⊥ ⊥𝑋(𝑖) 𝑡

 ZMCI.
24:if𝑝≤𝛼 MCI then
25:Add edge(𝑋 (𝑗) 𝑡−𝜏 →𝑋 (𝑖) 𝑡 )toE
26:end if
27:end for
28:end for
29:returnE
Repeatingthissamplingprocedureovernrunsyieldsastableestimateoftheconditionalcausaleffect bΔ𝑗(𝑧),representing
the expected change in conversions when channel𝑗 is switched from its active statedo(𝑋𝑗 =1) to the inactive state
do(𝑋𝑗 =0) atcovariateprofile 𝑧. ThisMonteCarloprocedurealsoprovidesuncertaintyquantificationwithoutrequiring
parametric assumptions on the structural equations.
To express the causal effect on a comparable scale across channels, we compute a per-unit causal contribution by
normalizing the estimated effect by the average activity level of channel𝑗:
ACE per unit(𝑗)=
bΔ𝑗(𝑧)
E[𝑋𝑗].(11)
This quantity represents the incremental causal contribution of a single unit of channel activity (e.g., one impression) to
expected conversions.
13

Causal-Driven AttributionGeorgios Filippou
3.3 Evaluation Metrics
3.3.1 Causal DAG Discovery
To quantify the DAG structures learned by our proposed causal-discovery algorithm, we adopt two complementary
families of metrics: (i)edge-based graph classification measuresto compare the number of edges that differ between
two graphs Cheng et al. [2022], and (ii)graph-distance-based measures, which evaluate how well the learned graph
supports valid identifying formulas for effects, and. Below we go through each measure in detail.
The edge-based graph distance will be based on the intuition that directional adjacency relations can be treated as a
binary classification problem. Therefore, a variety of metrics in classification tasks can be used such as AUC, True
Positive Rate (TPR), False Positive Rate (FPR), and𝐹𝛽.
True Positive Rate and False Positive RateWe consider a finite set of random variables𝑋1,...,𝑋 𝐷 with index set
V={1,...,𝐷}. A graphG=(V,E)consists of the node setVand an edge setE⊆V×V.
LetG true=(V,E true)denote the ground truth DAG, and letGpred=(V,E pred)denote the predicted DAG.
The true positive rate (TPR) is defined as the ratio of correctly recovered edges, meaning the edges that appear in both
Epred andE true, relative to the total number of edges in the ground truth graph. Formally,
TPR= |Epred∩E true| |Etrue| .(12)
The false positive rate (FPR) measures the proportion of incorrectly added edges, meaning the edges that appear inEpred
but not inEtrue, relative to the number of edges that are not present in the ground truth graph. Formally,
FPR= |Epred\E true| |(V×V)\E true|,(13)
whereV×Vdenotes the set of all possible directed edges among the variables, excluding self loops if desired.
TPR and FPR are computed from the p-value matrices after applying a p% (e.g., 5%) significance threshold. TPR
measures the fraction of true causal links that the method correctly identifies, while FPR measures the fraction of absent
links that the method incorrectly labels as causal. Formally, TPR is the number of correctly detected links divided
by the number of true links, and FPR is the number of falsely detected links divided by the number of absent links.
Ideally, a causal discovery algorithm should recover true causal links with high sensitivity while keeping false positive
(incorrect link) detections under control.
Area Under the ROC CurveArea under ROC curve (AUC) is the area under the curve of recall versus FPR at
different thresholds. The AUC quantifies the ability of the model to distinguish true causal links from non-links based
on the score matrices returned by PCMCI. Each score matrix contains non-negative values, where a larger entry at
position(𝑖,𝑗) indicates greater confidence in a causal edge𝑖→𝑗 . The corresponding ground-truth label is binary (1 for
a true causal link, 0 otherwise). Higher AUC values, with a maximum of 1, indicate stronger separation between true
and false links.
F-measure (𝐹𝛽)The F-measure, also computed on thresholded p-value matrices, evaluates the harmonic mean of
precision and recall. It ranges from 0 (poor performance) to 1 (perfect precision and recall). In this study, we use
𝐹0.5, which places greater emphasis on precision than recall, reducing the impact of false negatives. This makes𝐹0.5
particularly suitable when the cost of false positives is higher or when identifying spurious edges is more detrimental
than missing weak ones.
Nevertheless, the number of differing edges between two graphs does not capture how the graphs differ with respect
to the identifying formulas they imply for causal effects. Therefore, edge-based metrics cannot quantify whether a
predicted graph preserves the causal semantics encoded by the true graph. In particular, two graphs may differ in
several edges yet induce the same interventional distributions, while another pair may differ by only a few edges but
imply fundamentally different causal effects. To evaluate causal fidelity rather than purely structural similarity, we
additionallyemploygraph-distance-basedmeasuresthatcomparegraphsintermsofthecausalrelationshipstheyencode,
as described in the next section.
Structural Hamming DistanceThe Structural Hamming Distance (SHD) [Acid and de Campos, 2003, Tsamardinos
et al., 2006] is one of the most commonly used metrics for evaluating the accuracy of a learned causal graph. Intuitively,
SHD counts the number of edge insertions, deletions, and orientation reversals required to transform the learned graph
14

Causal-Driven AttributionGeorgios Filippou
into the true graph. A low SHD value indicates a more accurate reconstruction of the true causal structure, whereas a
higher SHD reflects greater structural deviation and thus poorer causal discovery performance.
Givenatruecausalgraph 𝐺true andapredicted(learned)graph 𝐺pred, bothdefinedoverthesamevertexset V, wedefine
their adjacency matrices𝐴true,𝐴 pred∈{0,1} 𝐷×𝐷 such that𝐴[𝑖,𝑗]=1if there is an edge𝑋 𝑖→𝑋 𝑗.
The Hamming distance between binary vectors measures the number of directed edges that differ between the two
adjacency matrices. Formally,
SHD(𝐺true,𝐺 pred)=
𝐷∑︁
𝑖=1
𝐷∑︁
𝑗=1
|𝐴true[𝑖,𝑗]−𝐴 pred[𝑖,𝑗]|
=∥𝐴 true−𝐴 pred∥1.
(14)
Alternatively, for each unordered pair of nodes(𝑖,𝑗)with𝑖< 𝑗, define
𝛿𝑖𝑗 =
 

1,if𝐴 true[𝑖,𝑗]≠𝐴 pred[𝑖,𝑗]
or𝐴 true[𝑗,𝑖]≠𝐴 pred[𝑗,𝑖],
0,otherwise.
(15)
Then,
SHD(𝐺true,𝐺 pred)=
∑︁
1≤𝑖<𝑗≤𝐷
𝛿𝑖𝑗.(16)
A normalized variant scales the distance by the number of possible unordered node pairs:
𝑛𝑆𝐻𝐷(𝐺 true,𝐺 pred)= 1𝐷
2

∑︁
1≤𝑖<𝑗≤𝐷
𝛿𝑖𝑗,(17)
so that𝑛SHD∈[0,1] . This normalization expresses the proportion of differing edges relative to the total possible
pairwise relations.
While the SHD implementation is simple and efficient to compute, it only reflects local structural differences and does
not account for causal equivalence or d-separation patterns. A very small structural change (e.g., flipping a single edge
𝐴→𝐵→𝐶 to𝐴←𝐵→𝐶 ) can completely alter the causal implications of a graph even when SHD suggests that the
two graphs are nearly identical. Consequently, SHD has been criticized for failing to capture the full causal implications
of structural differences between graphs. This limitation has motivated the development of more causally informed
distance measures, such as the Structural Intervention Distance (SID), which will be discussed below.
Structural Intervention DistanceThe Structural Intervention Distance (SID) counts the number of ordered node
pairs(𝑖,𝑗) forwhichtheinterventionaldistributionsimpliedbythetrueDAGandthelearnedDAGdiffer. Tounderstand
SID, we first introduce the intervention distribution.
Given a directed acyclic graph (DAG)G over variablesX=(𝑋 1,...,𝑋 𝑝) with joint distributionL(X), the parents of a
node𝑋 𝑗 are defined as
PAG 𝑗 ={𝑋 𝑖 :(𝑖,𝑗)∈E},(18)
meaning that𝑋𝑖 is a parent of𝑋𝑗 whenever the edge𝑋𝑖→𝑋 𝑗 is present.
Pearl’sdo-operatorformalisesinterventionsbyreplacingtheconditionaldistributionoftheintervenednode. Intervening
on𝑋 𝑗 with a distribution˜𝑝(𝑥𝑗)yields
𝑝(𝑥 1,...,𝑥 𝑝|𝑑𝑜(𝑋 𝑗 =˜𝑝(𝑥 𝑗)))=
Ö
𝑖≠𝑗
𝑝(𝑥𝑖|𝑥 PA𝑖)·˜𝑝(𝑥 𝑗),(19)
whenever𝑝(𝑥 1,...,𝑥 𝑝)>0, and zero otherwise.
A point intervention𝑑𝑜(𝑋𝑗 =˜𝑥𝑗)is obtained by choosing˜𝑝(𝑥𝑗)=𝛿 𝑥 𝑗,˜𝑥𝑗:
𝑝(𝑥 1,...,𝑥 𝑝|𝑑𝑜(𝑋 𝑗 =˜𝑥𝑗))=
Ö
𝑖≠𝑗
𝑝(𝑥𝑖|𝑥 PA𝑖)·𝛿 𝑥 𝑗,˜𝑥𝑗.(20)
15

Causal-Driven AttributionGeorgios Filippou
Often we are interested only in the marginal effect of𝑋𝑗 on another variable𝑋𝑖. If𝑋𝑖 is not a parent of𝑋𝑗, the parent
adjustment formula (Theorem 3.2.2 in Pearl [2009]) gives:
𝑝(𝑥𝑖|𝑑𝑜(𝑋 𝑗 =˜𝑥𝑗))=
∑︁
𝑥PA𝑗
𝑝(𝑥𝑖|˜𝑥𝑗,𝑥 PA𝑖)𝑝(𝑥 PA𝑗).(21)
SID compares a true graphGtrue with an estimated graphGpred by counting the number of node pairs(𝑖,𝑗) for which the
interventional distributions differ:
SID(Gtrue,Gpred)=

  (𝑖,𝑗):𝑝 Gpred(𝑋𝑗|𝑑𝑜(𝑋 𝑖))
≠𝑝 Gtrue(𝑋𝑗|𝑑𝑜(𝑋 𝑖))

. (22)
A pair(𝑖,𝑗) is calledgoodif the intervention distribution obtained from the learned graph matches that from the true
graph for all observational distributionsL(X). Otherwise, the pair contributes one unit to the SID score. In this way,
SID evaluates errors in causal ordering, whereas SHD counts only incorrect edges.
For a graph with𝑉nodes, the total number of ordered node pairs(𝑖,𝑗)with𝑖≠𝑗is
𝑁pairs=𝑉(𝑉−1).(23)
The normalized Structural Intervention Distance is defined as
nSID(Gtrue,Gpred)= SID(Gtrue,Gpred) 𝑉(𝑉−1) .(24)
Therefore, nSID measures the proportion of causal effects that the learned graph gets wrong. Values close to 0 indicate
high causal accuracy, whereas values close to 1 indicate poor causal estimation.
3.3.2 Causal Effect Estimation
After estimating the CATE for each marketing channel (as shown in Section 3.2.2), we evaluate the accuracy of the
causal-driven attribution model using three complementary metrics.
Relative Root Mean Square ErrorThe relative root mean square error (RRMSE) measures the scale-normalized
deviation between the estimated causal effectsˆ𝜏𝑖 and the ground-truth effects𝜏𝑖:
RRMSE=
√︃
1
𝑛
˝𝑛
𝑖=1(ˆ𝜏𝑖−𝜏𝑖)2
1
𝑛
˝𝑛
𝑖=1|𝜏𝑖|
,(25)
where𝑛is the number of channels. This metric captures overall estimation error relative to the magnitude of true effects.
The interpretation of the RRMSE depends entirely on the context, domain, and units of the outcome variable. Different
research areas adopt different thresholds for what constitutes an acceptable level of normalized error. For example, in
the energy and agricultural modeling literature, model accuracy is often consideredexcellentwhenRRMSE<10% ,
goodwhen 10%≤RRMSE<20% ,fairfor 20%≤RRMSE<30% , andpoorwhen RRMSE≥30% Jamieson et al.
[1991], Despotovic et al. [2016]. These thresholds illustrate that RRMSE benchmarks are not universal but rather
depend on the application context and the expected signal-to-noise ratio in the data.
Mean Absolute Percentage ErrorThe mean absolute percentage error (MAPE) expresses the average proportional
deviation:
MAPE= 100% 𝑛 𝑛∑︁ 𝑖=1

 ˆ𝜏𝑖−𝜏𝑖 𝜏𝑖

.(26)
RRMSE and MAPE capture complementary aspects of estimation accuracy. RRMSE gives more weight to larger errors
because it is based onsquared deviationsthat are normalized by the scale of the true effects, making it sensitive to
large misestimations. In contrast, MAPE provides an interpretable percentage-based measure of accuracy by averaging
absolute proportional errors. For instance, a MAPE of5% indicates that the estimated causal effects deviate from
the true effects by only5% on average. Using both metrics allows us to assess estimation quality in terms of both
scale-normalized sensitivity to large errors (RRMSE) and average relative deviation (MAPE).
16

Causal-Driven AttributionGeorgios Filippou
SpearmanRankCorrelationToevaluatewhethertheattributionmodelpreservestherelativeimportanceofmarketing
channels, we compute the Spearman rank correlation between the ground truth causal effects and the estimated causal
effects obtained from the model Cornell et al. [2024], Arshad et al. [2024].
Suppose𝐶 denotes the list of marketing channels sorted (either ascending or descending) according to their true causal
effects (ground-truth ranking), and𝐶𝑝 denotes the list of the same channels sorted by their estimated causal effects from
the attribution model. For each channel𝑥, we define its rank in the true and predicted lists as
𝑟𝐶(𝑥)=position of channel𝑥in𝐶,
𝑟𝐶𝑝(𝑥)=position of channel𝑥in𝐶 𝑝. (27)
From these ranks, we construct two ranked vectors:
𝑅𝐶 = 𝑟𝐶(𝑥1), 𝑟𝐶(𝑥2), ..., 𝑟𝐶(𝑥𝑛),
𝑅𝐶𝑝 = 𝑟𝐶𝑝(𝑥1), 𝑟𝐶𝑝(𝑥2), ..., 𝑟𝐶𝑝(𝑥𝑛), (28)
where𝑛is the total number of marketing channels.
The Spearman rank correlation coefficient𝜌between the two ranked lists is defined as
𝜌=1− 6˝𝑛 𝑖=1𝑑2 𝑖
𝑛(𝑛 2−1) ,(29)
where𝑑𝑖 =𝑟 𝐶(𝑥𝑖)−𝑟 𝐶𝑝(𝑥𝑖) isthedifferenceinrankforthe 𝑖𝑡ℎ channel,and 𝑛isthetotalnumberofmarketingchannels.
Spearman’s𝜌 takesvaluesbetween −1and 1. Avalueof 𝜌=1 indicatesperfectagreement,meaningthemodelrecovers
the exact ordering of true causal contributions across marketing channels. A value of𝜌=−1 means the estimated
ranking is the exact reverse of the true ranking. A value of𝜌=0 indicates no monotonic relationship between the
estimatedandtruerankings. Inourstudy,ahighSpearmancorrelationsignifiesthatthemodelcorrectlyidentifieswhich
channels are more or less influential, even if the estimated magnitudes differ. This property is particularly important for
resource allocation and budget optimization, where the correct ordering of channel importance often matters more than
precise effect magnitudes.
4 Results
ThisstudyusesTigramite 9,anopen-sourcePythonpackageforreconstructinggraphicalmodels(conditionalindependence
graphs) from multivariate time series based on the PCMCI framework, andDoWhy10 for estimating causal effects.
The algorithm proceeds in two steps. First, a PC step screens candidate parent sets using a permissive threshold
(𝛼PC =0.2 ) to favour recall and preserve potentially relevant dependencies. Second, a Momentary Conditional
Independence (MCI) test re-evaluates each retained link at a stricter significance level (𝛼MCI =0.05 ), ensuring
robustness and suppressing spurious associations. This two-step procedure balances false negatives and false positives,
yielding stable edge sets across repeated runs.
To ensure a DAG causal structure, bidirectional links are pruned by retaining the edge whose time-lagged effect has the
greater magnitude, and any remaining cycles are resolved using a priority rule that preserves edges directed into the
main outcome variable (e.g., conversions). This enforces causal directionality toward the dependent variable of interest.
4.1 Optimal Time-delay Causality
Nevertheless, a major challenge when using PCMCI is specifying the appropriate time lag needed to reliably estimate
causallinks. Wedonotknowinadvancewhichtimelagbestreflectstheunderlyingcausalrelationshipsinthesimulated
data. Therefore, anempiricalassessmentisnecessarytoidentifywhichlagvaluesallowPCMCItomostreliablyrecover
the underlying causal structure in our simulated environment.
To this end, we explore temporal lags up to𝜏max=60 and evaluate model performance across1,000 simulated datasets.
For each lag value𝜏, we compute several predictive and structural metrics, including AUC, TPR, FPR, F0.5, SHD, and
SID, and summarize their empirical distributions using kernel density estimates (KDEs), as visualized in Fig. 6. Each
ridge in the figure corresponds to1,000 simulations at a fixed lag and illustrates how both the central tendency and
variability of each metric evolve as𝜏increases.
9https://jakobrunge.github.io/tigramite/
10https://github.com/py-why/dowhy
17

Causal-Driven AttributionGeorgios Filippou
Across all six metrics, a consistent pattern emerges: performance steadily improves with increasing lag, reaches its
optimum around𝜏=45 , and then either plateaus or slightly deteriorates. At𝜏=45 , the KDE ridges indicate three
desirable properties:(i)the best concentration of high-performing metric values,(ii)the lowest variability across seeds,
and(iii)a balanced trade-off between predictive accuracy (AUC, TPR, F0.5) and structural recovery (SHD, SID). In
addition, the FPR remains well controlled around this lag, meaning it does not increase substantially despite gains
in sensitivity (TPR). Such behaviour is consistent with a saturation effect, where additional lag increases no longer
introduce new false positives because most meaningful dependencies have already been captured. This confluence of
high performance and low uncertainty identifies𝜏=45as the optimal lag value𝜏𝑚𝑎𝑥.
In conclusion, this result indicates that the simulated system exhibits a characteristic time delay of approximately 45
time steps between channel impressions and observed conversions. At this lag, PCMCI most effectively captures the
temporal propagation of causal influence across variables. For this reason, all subsequent causal attribution experiments
adopt𝜏𝑚𝑎𝑥 =45as the default time-delay configuration.
4.2 Causal-Driven Attribution Analysis
4.2.1 Illustrative Example
Causal DAG DiscoveryFig. 7 compares the ground-truth causal graph (left) with the graph predicted by the PCMCI
algorithm (right). The true DAG is generated from our simulated structural model (withseedvalue 155 in this
illustration), where each directed edge corresponds to a known causal relationship and all effects on the target variable,
conversion. Of course, the choice of seed is arbitrary, and any random seed would produce a valid instance of the
simulated structural model. Overall, our estimator successfully recovers the major components of the underlying
structure.
According to graph-distance–based metrics, the comparison determined an SHD of 0.133 and an SID of 0.10, indicating
strongagreementwiththeground-truthDAGinbothitsstructuralconfigurationanditsimpliedinterventional behaviour.
These low values suggest that only a small number of edge discrepancies remain and that the learned graph preserves
most of the true causal dependencies.
From a classification perspective, we also obtained a strong performance. The TPR is 0.90, which means that 90% of
actual causal edges were correctly identified. The FPR is relatively low at 0.05, indicating that the predicted graph is
well calibrated in its edge decisions. Furthermore, the AUC is 0.925, showing that our method achieves a high level of
discriminative power when ranking edges by their likelihood of being causal. The𝐹0.5 score is 0.90, which confirms
that the majority of the identified edges are accurate and not attributable to false detections.
Although our causal graph discovery approach recovers much of the true structure, it also introduces minor errors. For
example, it fails to detect a true edge fromFacebook→ Affiliates, and it incorrectly introduces spurious edges such as
Google Ads→ YouTube. Additionally, the learned graph contains certain sign errors, where the direction of causal
influence is correct but the estimated effect is negative rather than positive. To address these issues, a post-estimation
refinement step will be applied to improve the accuracy of the predicted DAG.
Causal Effect EstimationTo assess the performance of our causal effect estimator, we first evaluate it under ideal
conditions by providing the true causal DAG as input. Since the simulated data are generated from this ground-truth
structure, the estimated causal effects should closely match the true effects. This step verifies that the estimator is
correctly specified and capable of recovering the underlying causal relationships when the structure is known. We then
apply the estimation using the DAG learned by our discovery approach. To obtain robust estimates of causal effects, we
follow the procedure described in Section 3.2.2 and compute CATE using a Monte Carlo approach. The estimation
process is repeated 5,000 times under independent stochastic draws, and the resulting estimates are averaged to reduce
variance.
It is important to note that small deviations are expected even when using the true graph. Each channel inherently
contains noise, which causes estimation error to accumulate along causal pathways with multiple parent nodes. For
example, in the graph shown in Fig. 7 (a), bothFacebookandYouTubehave several outgoing connections, which
increases noise propagation when the estimator calibrates their effects. As a result, channels with direct causal links
such asAffiliates,Google Ads, andTikTokshow nearly perfect recovery, whereasFacebookandYouTubedisplay slightly
higher residual error. This expectation is indeed reflected in the results shown in Fig. 8 (a).
When the estimator is applied to the predicted DAG (as depicted in Fig.8 (b), the overall accuracy maintains a high level
of accuracy, with effect estimates that closely reflect the true underlying causal effects across channels. As expected, the
residuals increase slightly relative to the true-graph case, particularly for channels whose incoming or outgoing edges
18

Causal-Driven AttributionGeorgios Filippou
(a)
 (b)
(c)
 (d)
(e)
 (f)
Figure 6: Kernel density estimates (KDEs) of six evaluation metrics, including AUC, TPR, FPR, F0.5, SHD, and SID
across lag values (𝜏). Each subplot shows how the empirical distribution of the metric varies as𝜏 increases from 0 to 60,
using 1000 simulation seeds for each𝜏. The viridis color gradient is used to visually distinguish KDE ridges at different
lag values; color does not encode density or any statistical quantity. Instead, the horizontal width of each ridge reflects
the density and spread of metric values at a given lag. The red dashed vertical line marks𝜏=45 , and the red dashed
horizontal line denotes the corresponding median metric value at that lag.
were misidentified in the learned structure. Nevertheless, the deviations are small, implying that the predicted graph is
sufficiently accurate to support reliable causal effect estimation.
These observations are quantitatively supported by the results presented in Table 2. Using the true graph yields very low
estimation error, with RRMSE of 3.16% and MAPE of 2.17%, along with perfect rank preservation as indicated by
a Spearman correlation of 1.00. When the predicted graph is used, error measures increase moderately to RRMSE
of 5.27% and MAPE of 4.20%, while rank correlation remains high at 0.90. This indicates that although structural
imperfections in the learned graph introduce some additional estimation error, the overall magnitude of causal effects
and their relative ordering across channels are still captured with high fidelity.
In summary, the results indicate that the estimator performs effectively whether it receives the true DAG or the predicted
DAG as input, confirming that the workflow is both reliable and robust. However, this evaluation is based on only a
19

Causal-Driven AttributionGeorgios Filippou
(a) True Causal DAG
 (b) Predicted Causal DAG
Figure 7: Comparison between the ground-truth DAG (a) and the DAG predicted using PCMCI (b).
single synthetic instance. To obtain a more reliable and statistically grounded assessment, the next section presents a
broader simulation study. Using the same evaluation metrics, this extended analysis provides deeper insight into the
performance of our causal-driven attribution framework.
(a) CDA result on True Causal Graph
 (b) CDA result on Predicted Causal Graph
Figure 8: Comparison of causal effect estimates and residuals for (a) the predicted causal graph and (b) the simulated
ground-truth causal graph, compared to the true causal effects. Each panel shows the estimated causal effects per
marketing channel and the residual differences between estimated and true values.
4.2.2 Aggregate Simulation Results
Table 3 summarizes the estimation performance across 1,000 simulations, generated by sampling 200 random DAGs for
each depth level from 2 to 6 layers (corresponding to our setup with five input channels and one target). This balanced
20

Causal-Driven AttributionGeorgios Filippou
Table 2: Comparison of causal effect estimation accuracy using the true causal graph versus the predicted graph.
Lower RRMSE and MAPE indicate better estimation accuracy, while higher Spearman correlation reflects better rank
preservation.
DAG Input RRMSE (%) MAPE (%) Spearman Corr
True Graph 3.16 2.17 1.00
Predicted Graph 5.27 4.20 0.90
Table 3: Estimation performance across DAG depths. Values report mean±standard deviation over 200 simulations per
depth.
Input Metric 2 Layers 3 Layers 4 Layers 5 Layers 6 Layers All
True DAG
RRMSE (%)0.79±0.44 7.71±7.36 10.48±9.38 13.56±10.81 14.96±12.67 9.50±10.44
MAPE (%)0.69±0.38 4.43±4.08 6.32±5.80 9.00±7.77 10.18±9.00 6.12±7.05
Spearman𝜌0.98±0.05 0.92±0.16 0.87±0.24 0.84±0.22 0.84±0.23 0.89±0.20
Predicted DAG
RRMSE (%)12.92±10.20 20.65±12.97 25.50±13.72 29.34±15.37 32.76±15.43 24.23±15.31
MAPE (%)9.31±7.38 15.97±10.72 22.34±26.91 24.52±14.13 26.85±14.07 19.80±17.26
Spearman𝜌0.78±0.29 0.63±0.38 0.50±0.44 0.40±0.47 0.37±0.49 0.53±0.45
design ensures that each layer of structural complexity contributes equally to the overall results. Several insights emerge
regarding the behaviour and robustness of the causal effect estimator as DAG depth increases and the underlying causal
architecture becomes more complex.
Performance when using the true DAGAcross different DAG depths, the estimator demonstrates strong accuracy
when provided with the true causal DAG. Both RRMSE and MAPE remain low for shallower graphs with two to three
layers and increase gradually as depth grows, reflecting the inherent difficulty of recovering causal effects in structures
with more parent–child dependencies and greater noise accumulation. Even in the deepest configurations with five
to six layers, the estimation error remains moderate relative to the scale of the simulated effects. The Spearman rank
correlation also remains consistently high, ranging from 0.84 to 0.98, indicating that the estimator reliably preserves the
relative ordering of channel importance even as absolute estimation error increases with graph complexity.
The aggregated results across all depths provide further confirmation of the estimator’s robustness. With an overall
RRMSEof9.50%,MAPEof6.12%,andSpearmancorrelationof0.89,theestimatorrecoversthetruecausaleffectswith
high fidelity on average across a broad range of DAG structures. These metrics demonstrate that the proposed approach
maintains strong performance under the ideal condition of perfect structural knowledge, establishing a performance
benchmarkagainstwhichresultsusingthepredictedgraphcanbeevaluated. Theconsistentpreservationofrankordering
is particularly noteworthy from a practical standpoint, as marketing decision-makers often prioritize understanding the
relative importance of channels over obtaining precise point estimates of individual effects.
Performance when using the predicted DAGWhen the estimator relies on the predicted graph rather than the true
DAG, estimation error increases, as expected. This decline in performance is statistically significant in deeper DAGs
(five to six layers), where inaccuracies in the predicted structure intensify the inherent complexity of the task. For
instance, the RRMSE grows sharply from 12.92% at depth 2 to 32.76% at depth 6, and the MAPE shows a similar
pattern, rising from 9.31% to 26.85%. The Spearman correlation also drops steadily as the number of layers increases,
falling from 0.78 at two layers to 0.37 at six layers. This indicates that inaccuracies in the predicted structure make it
harder for the model to correctly rank the importance of different channels.
Even so, the overall performance across all simulations indicates that the estimator remains informative. With an
RRMSE of 24.23% and MAPE of 19.80%, the estimated causal effects differ from the true magnitudes by roughly 20 to
25 percent on average. While this represents a non-trivial loss of numerical precision compared to using the true graph,
it still falls within a practically acceptable range for most real-world attribution scenarios, where measurement noise and
structural uncertainty are unavoidable. The moderate Spearman𝜌 of 0.53 further demonstrates that the estimator retains
meaningful discriminatory power, preserving the ability to distinguish high-impact channels from lower-impact ones,
even though the ranking is no longer perfectly reliable.
Taken together, these results demonstrate that the proposed causal-driven attribution approach remains useful under
realistic conditions, providing meaningful insight into relative channel contributions despite the presence of substantial
structural noise in the learned DAGs.
21

Causal-Driven AttributionGeorgios Filippou
Effect of DAG depthBoth the true-DAG and predicted-DAG results reveal a clear and consistent pattern: deeper
graphs with a greater number of causal layers systematically reduce estimation accuracy. This decline is intuitive, as
increasing depth introduces more intermediate nodes and pathways through which random noise can propagate, thereby
amplifyingvarianceintheestimatedeffects. Additionally,deeperstructurescreatemoreopportunitiesforsmallerrorsin
the estimated relationships to accumulate and magnify as they propagate downstream through the causal chain. Whether
these errors stem from incorrect edge magnitudes or from the presence or absence of connections in the learned graph,
their cumulative impact grows substantially with each additional layer.
The impact of depth becomes particularly pronounced when the estimator relies on the predicted DAG rather than the
true structure. In this scenario, inaccuracies in the learned graph interact with the inherent complexity of deeper causal
architectures, resulting in compounding estimation errors that degrade both numerical precision and rank-ordering
performance. This heightened deterioration underscores the sensitivity of causal effect estimation to structural
misspecification, especially in settings where causal pathways span multiple layers or involve densely connected nodes.
Overall, the results demonstrate that while the estimator maintains robust performance for shallower graphs, deeper
causalarchitecturesposesubstantiallygreaterchallenges. Thedegradationmanifestsbothintermsofabsolutenumerical
accuracy and in the model’s ability to preserve the correct relative ordering of channel effects. These findings have
practical implications for marketing attribution. In contexts where channel interactions are known to involve multiple
layers of indirect influence, practitioners should anticipate greater uncertainty in effect estimates and may need to place
greater emphasis on directional insights and relative rankings rather than precise point estimates. The results also
highlight the value of pursuing accurate structural discovery, as even modest improvements in the learned graph can
yield meaningful gains in downstream estimation quality when dealing with complex causal systems.
5 Discussion and conclusion
Now more than ever, businesses rely on data-driven decision making to allocate marketing resources and maximize
return on investment. However, the growing integration of AI into data driven technologies in digital advertising, such
as recommendation systems Jabbar et al. [2020] and digital platforms Purmonen et al. [2023], has made consumer
journeys increasingly complex, creating multi touchpoint pathways that span numerous channels Micheaux and Bosio
[2019], Roy et al. [2025], Hardcastle et al. [2025]. Simultaneously, the rise of big data has introduced challenges related
to missing and uncertain information, complicating the interpretation of marketing signals. Furthermore, stringent
privacy regulations (as discussed in Section 2.4), together with platform level restrictions such as the deprecation
of third party cookies, have sharply reduced access to the user-level data required by traditional attribution models.
Consequently, conventional attribution methods that rely on tracking individual user journeys across touchpoints have
become increasingly impractical and, in many cases, impossible to implement. This confluence of factors creates an
urgent need for new attribution approaches that can operate effectively in privacy-constrained environments while still
capturing the complex interdependencies that characterize modern marketing ecosystems.
To the best of our knowledge this is the first ever causal-driven attribution utilising impression data without path
information. When introducing a new attribution model, it is essential to consider the standards and challenges it must
address to be practically viable. The first and most fundamental issue concerns the type of data it requires. As discussed
in the literature review, numerous attribution methodologies exist, and many provide reliable results that businesses
can trust. However, a major limitation of existing attribution approaches is their dependence on user-level path data.
These models can only operate when detailed sequences of individual user interactions across touchpoints are available.
If a business does not collect or have access to such data, it cannot apply these methods regardless of its analytical
capabilities or resources. Therefore, our causal-driven attribution solved this challenges by using alternative data
structures, in particular aggregated data that does not require tracking individual user journeys while still representing
the relationships between marketing channels and conversions.
Second, our approach uses impressions as independent variables, representing a necessary evolution beyond path-based
attribution models that depend primarily on clicks or visits. As privacy regulations restrict user level tracking,
organisations lose the ability to validate platform reported click counts, which makes the collection of accurate and
reliable click records progressively more challenging. This shift aligns with a broader industry recognition that
impressionscapturevaluablebrandexposurethatmaynotgenerateimmediateinteractionsbutcansignificantlyinfluence
downstream consumer behaviour over time. As discussed in Section 2.4, we have concluded that exposure effects
often precede and facilitate subsequent conversions, even in the absence of direct click engagement. Therefore,
impression-based models not only address the practical reality of diminished click tracking but also provide a more
comprehensive view of marketing influence by accounting for both direct response mechanisms and longer-term
awareness-building effects that traditional click-centric approaches overlook.
22

Causal-Driven AttributionGeorgios Filippou
Third, the trustworthiness of attribution methods is grounded in their ability to uncover meaningful causal relationships
among marketing channels rather than simple correlations Hair Jr and Sarstedt [2021]. Marketing practitioners must
understand which channels truly drive outcomes, not merely which ones exhibit statistical associations with conversions.
Our causal driven attribution model addresses this requirement by estimating channel effects within a structured causal
framework. Although many researchers have developed reliable attribution approaches, most of these methods rely on
user path data (as discussed in Section 2.3). While the use of aggregated data does prevent the identification of causal
effects at the level of individual user journeys, this limitation is not problematic in practice. Businesses make strategic
budget decisions at the population level, where the primary concern is the overall influence of channels rather than
the behaviour of specific individuals. Without a causal understanding of these effects, firms risk allocating resources
to channels that appear effective but do not actually contribute to performance. For this reason, an attribution model
that operates on aggregated data must still deliver credible causal inference. Our approach is designed to meet this
requirement and support actionable marketing decisions.
Finally, becauseourapproachdoesnotrequirePersonallyIdentifiableInformation, itcanbeusedinenvironmentswhere
tracking individual users is restricted by privacy or security rules. This makes it especially valuable for highly regulated
industries such as pharmaceuticals, telecommunications, healthcare, and education, where strict data protection laws
often make traditional tracking methods impractical or illegal Onifade et al. [2021], Seth and Ramakrishnan [2025].
Beyond these regulated sectors, the framework offers a practical solution for any organization that needs effective
marketing attribution while avoiding the substantial infrastructure costs associated with collecting, storing, and securing
user-level tracking data. By operating on aggregated data, our approach reduces both financial barriers and compliance
burdens, thereby making advanced attribution analysis accessible to organisations of varied sizes and capacities.
5.1 Theoretical implications
This paper contributes to the marketing and causal inference literature by proposing a novel causal-driven attribution
framework designed to operate exclusively on aggregated marketing data, specifically impression-level time series,
without relying on path-level or user-level tracking. This addresses a critical and growing need for privacy-preserving,
scalable, and interpretable attribution models in marketing analytics, particularly in regulatory environments where
access to granular, identifiable data is increasingly restricted or prohibited.
Firstofall,althoughStructuralEquationModellingistraditionallyemployedforpathanalysisandhypothesistestingStein
et al. [2011], its generative nature makes it well suited for simulating synthetic datasets with controlled causal structures.
In this study, we leverage SEM as a mechanism to generate data that follow predefined structural relationships among
marketing channels and conversion outcomes. By encoding causal pathways, functional forms, and noise processes
directly into the model, SEM enables us to simulate realistic datasets that mimic the multivariate dependencies observed
in marketing environments. While no simulation framework can perfectly reproduce real behavioral data, SEM provides
a coherent and interpretable approximation of the underlying data-generating process through its regression-based
formulation of structural relations Iacobucci [2009]. These modeling assumptions offer a transparent and theoretically
grounded foundation for constructing synthetic data, enabling controlled experimentation while preserving essential
features of causal structure, noise propagation, and channel interactions.
Our causal-driven attribution framework reconceptualizes attribution as a causal inference problem rather than a
correlational one, aligning with insights from prior studies Smith and Pell [2003], Hair Jr and Sarstedt [2021]. It
contributestoattributiontheorybyintegratingcausaldiscoveryandcausalestimationwithinaunifiedanalyticalpipeline.
In the discovery stage, the framework employs the PCMCI algorithm to identify temporal conditional independencies
and recover the directional structure among marketing channels using only impression-level time series, establishing a
causal graph without requiring user-level tracking data. In the estimation stage, the inferred structure is used to compute
Conditional Average Treatment Effects that quantify both direct and indirect channel contributions to conversions. A
Monte Carlo procedure is applied to obtain stable effect estimates under uncertainty. Together, these stages offer a
transparent and rigorous approach to attribution by linking structural discovery with causal effect quantification. Across
multiple simulated settings, the framework achieves strong empirical performance, recovering true causal effects with
an average RRMSE of 9.50% and Spearman correlation of 0.89 when the true graph is provided, and maintaining
reasonable accuracy under the predicted graph with an average RRMSE of 24.23% and Spearman correlation of
0.53. This integration extends existing attribution theory by demonstrating how causal inference can be achieved from
aggregated data while preserving interpretability and robustness.
A third contribution in theoretical implications of this study is the development of a comprehensive benchmarking
framework for evaluating attribution models under controlled causal conditions. Since real world marketing data rarely
reveal the true causal relationships among channels, empirical validation of attribution models is typically constrained
or indirect. By constructing a simulation environment grounded in structural equation modelling, predefined causal
graphs, and systematically varied graph layers, our approach generates datasets where the true channel effects are known
23

Causal-Driven AttributionGeorgios Filippou
by design. This enables robust, repeatable comparisons of attribution performance across a wide range of structural
complexities and data generating processes. The benchmark not only facilitates the assessment of our own framework
but also offers a foundation that future research can use to evaluate alternative attribution methods under transparent and
reproducible conditions. As a result, it contributes to the field’s methodological foundations by establishing establishing
a standard approach for testing causal attribution models when the true causal structure cannot be directly observed.
5.2 Managerial implications
Our causal-driven attribution model carries several practical implications for marketing managers, analysts, and
decision-makers who operate in increasingly complex and privacy-constrained environments. First, managers no longer
need to rely on user-level data or cookies to make data-driven decisions. Our approach applies only on aggregated
impression-level data, making it highly applicable in industries where access to granular information is restricted by
privacy regulations such as Apple’s iOS14, GDPR, CCPA or technological changes such as cookie deprecation (as
detailed in Section 2.4. This opens the door for more organizations that can adopt evidence-based attribution strategies,
including those that lack advanced data infrastructure.
A further managerial insight from this study concerns the ability of the causal-driven attribution framework to capture
the overall marketing funnel. Many traditional attribution models, including machine learning and deep learning
approaches, emphasize immediate conversion signals. They typically use user-path data to predict whether a specific
sequenceofinteractionswillleadtoaconversionandthenderivechannelattributionbytracingmodelweightsorfeature
contributions. Such approaches overlook the broader dynamics of how channels interact and influence one another
throughout the customer journey. In contrast, our framework provides stakeholders with visibility into how digital
channels work together across the funnel, revealing both direct and indirect effects. This holistic perspective enables
decision-makers to understand the collaborative role of channels, which is essential for strategic planning and long-term
business growth Liu et al. [2022].
An important managerial contribution is related to marketing budget allocation. With global advertising spending
projected to exceed $1.17 trillion in 2025 Statista [2025], effective budget allocation has become a critical managerial
priority. Existing literature presents several approaches to budget allocation Zhao et al. [2019b], Fischer et al. [2011];
however, most offer only partial visibility into the unique contributions of each channel within the overall marketing
system. By estimating both the direct and indirect influence of each channel, our framework offers managers clearer
and more actionable guidance for budget allocation. In addition, the ability to identify channels that exert negative or
counterproductive influence enables firms to avoid wasteful spending and reallocate resources toward more effective
activities.
Based on these insights, managers should reconsider how they evaluate performance metrics and KPIs within their
marketing mix. Our method provides a more comprehensive perspective on channel influence, enabling a refinement
of existing measurement practices. This expanded perspective can help managers rebalance their media portfolios by
identifying undervalued yet effective touchpoints that may not be highlighted by traditional models. The simplicity
and scalability of the framework make it suitable for both early stage firms with limited analytical capacity and large
organizations overseeing complex multichannel campaigns. By reducing data requirements while enhancing the
analytical richness, our approach helps democratize marketing measurement and supports more informed strategic
decision making across diverse organizational contexts.
5.3 Limitations and directions for future research
This study has certain limitations that suggest promising directions for future work. We begin with the limitations of our
causal discovery method. The model relies only on observational data and does not incorporate interventional evidence,
which is known to enhance discovery performance Silva [2016]. Additionally, as noted by Runge et al. [2019], causal
inference is grounded in a set of underlying assumptions. Our approach assumes causal sufficiency, which means that
all relevant variables are included and that no unobserved factors influence more than one channel. It also relies on
the causal Markov condition, which states that each variable is independent of its non-effects given its direct causes.
Finally, it assumes faithfulness, which requires that observed conditional independence relationships arise from genuine
structural independence without spurious cancellations. Further research should explore the use of interventional
data to strengthen causal identification and reduce reliance on strong structural assumptions. Researchers should also
enhance the simulation framework by incorporating more realistic temporal patterns and behavioural dynamics that
better represent actual marketing environments.
Second, a wide range of causal discovery methodologies has been developed, as documented in the comprehensive
review by Niu et al. [2024]. Determining a suitable algorithm requires alignment between the analytical goals and the
assumptions that can plausibly be applied to the data generating process. In this study, PCMCI was chosen because it is
24

Causal-Driven AttributionGeorgios Filippou
well suited to impression level time series and can accommodate temporal dependence structures that are common
in marketing contexts. Nevertheless, other discovery techniques may achieve stronger performance under different
modelling assumptions or where the data generating process follows structural patterns not well captured by PCMCI.
The present work therefore provides a benchmark against which future research may evaluate and refine other causal
discovery approaches, with the potential to enhance the accuracy and robustness of causal driven attribution models.
A further set of limitations arises from the causal estimation stage, which relies on observational data and therefore
cannot fully eliminate the challenges associated with non-experimental inference. As Li and Kannan [2014] note,
models estimated with non-experimental data are inherently vulnerable to endogeneity and omitted variable bias.
Although our framework accounts for temporal ordering and conditional relationships, unobserved heterogeneity or
strategic behaviour, such as selective targeting or endogenous channel activation, may still distort the estimated causal
effects. These challenges are amplified in marketing settings, where channels often exhibit interdependent spillover
and carryover dynamics that are difficult to separate without controlled interventions Jin et al. [2017]. Future research
could extend the present model by explicitly incorporating spillover and carryover mechanisms to better capture the
interconnected nature of marketing activities.
Moreover, as Ferketich et al. [1984] discuss, residual analysis in causal models often reveals violations of model
assumptions, such as misspecification of functional forms, nonlinearity, and correlated errors across equations. These
violations can undermine causal validity, particularly when feedback mechanisms or dynamic dependencies exist but
are not explicitly modelled. In our framework, residual dependencies or systematic patterns may indicate modelled
confounding or non-stationarity, which could lead to overestimation or underestimation of true causal effects. Future
work should therefore explore robustness checks, alternative identification strategies, and the use of experimental or
quasi-experimental designs to validate the causal pathways uncovered through our discovery and analysis stages.
As mentioned in Section 3.1, despite our efforts to identify a dataset suitable for comparison between our causal-driven
attribution and traditional multi-touch attribution models, no such dataset was found. This is primarily because publicly
availablemarketingdatasetsdonotincludethetruecausaleffectsortheunderlyingcausalrelationshipsamongchannels,
both of which are necessary for a valid benchmark. We therefore constructed a synthetic dataset designed to preserve
the statistical properties of real-world data Raghunathan [2021]. Prior studies Yao et al. [2022], Zhao et al. [2019b] have
likewise relied on synthetic data to evaluate attribution methodologies. We encourage future researchers to compare our
CDA with ground truth derived from actual marketing data.
6 Competing interests
No competing interest is declared.
7 Authors’ contributions
G.F. was responsible for the ideation of the model, and G.F. initialized the results using the causal exploration algorithm.
G.F. wrote the first, second, and third drafts of the publication. B.Q. provided valuable feedback on the algorithmic
process and offered recommendations. B.Q. suggested the use of a synthetic dataset and created the process. B.Q.
updated the model process, updated the results section, and provided feedback on model evaluation. B.Q. also wrote the
model evaluation section. D.L. provided feedback on the readability and flow of the article. A.W. provided feedback on
the method and evaluation process and suggested the initial model evaluation approach. A.J. provided feedback on the
introduction and literature review and suggested relevant journals.
8 Acknowledgments
The authors thank the anonymous reviewers for their valuable suggestions.
9 Code availability
All scripts supporting the algorithm and data simulation will be made available upon publication. If you would like to
access them beforehand, please contact the corresponding author.
References
Ron Berman. Beyond the last touch: Attribution in online advertising.Marketing Science, 37(5):771–792, 2018.
25

Causal-Driven AttributionGeorgios Filippou
Marek Solcansky and Iveta Simberova. Measurement of marketing effectiveness.Economics and management, 15:
755–759, 2010.
German Zenetti, Tammo HA Bijmolt, Peter SH Leeflang, and Daniel Klapper. Search engine advertising effectiveness
in a multimedia campaign.International Journal of Electronic Commerce, 18(3):7–38, 2014.
Xiao Han, Leye Wang, and Weiguo Fan. Cost-effective social media influencer marketing.INFORMS Journal on
Computing, 35(1):138–157, 2023.
Alexander C LaBrecque, Clay M Voorhees, Farnoosh Khodakarami, and Paul W Fombelle. Native advertising
effectiveness: Theroleofcongruenceandconsumerannoyanceonclicks,bounces,andvisits.JournaloftheAcademy
of Marketing Science, 52(6):1692–1712, 2024.
Vivian Qin, Koen Pauwels, and Bobby Zhou. Data-driven budget allocation of retail media by ad product, funnel metric,
and brand size.Journal of Marketing Analytics, 12(2):235–249, 2024.
Dimitrios Buhalis and Katerina Volchek. Bridging marketing theory and big data analytics: The taxonomy of marketing
attribution.International Journal of Information Management, 56:102253, 2021.
HaroldHKelley. Attributiontheoryinsocialpsychology. InNebraskasymposiumonmotivation.UniversityofNebraska
Press, 1967.
Fritz Heider.The psychology of interpersonal relations. Psychology Press, 2013.
David A Schweidel, Yakov Bart, J Jeffrey Inman, Andrew T Stephen, Barak Libai, Michelle Andrews, Ana Babić
Rosario, Inyoung Chae, Zoey Chen, Daniella Kupor, et al. How consumer digital signals are reshaping the customer
journey.Journal of the Academy of Marketing Science, 50(6):1257–1276, 2022.
D Daniel Sokol and Feng Zhu. Harming competition and consumers under the guise of protecting privacy: An analysis
of apple’s ios 14 policy updates.Cornell L. Rev. Online, 107:94, 2021.
He Li, Lu Yu, and Wu He. The impact of gdpr on global technology development, 2019.
RobBonta. Californiaconsumerprivacyact(ccpa).RetrievedfromStateofCaliforniaDepartmentofJustice: https://oag.
ca. gov/privacy/ccpa, 2022.
Tony Haitao Cui, Anindya Ghose, Hanna Halaburda, Raghuram Iyengar, Koen Pauwels, S Sriram, Catherine Tucker,
and Sriraman Venkataraman. Informational challenges in omnichannel marketing: Remedies and future research.
Journal of marketing, 85(1):103–120, 2021.
Oleksii Starov, Yuchen Zhou, Xiao Zhang, Najmeh Miramirkhani, and Nick Nikiforakis. Betrayed by your dashboard:
Discovering malicious campaigns via web analytics. InProceedings of the 2018 World Wide Web Conference, pages
227–236, 2018.
Georgios Filippou, Athanasios G Georgiadis, and Ashish Kumar Jha. Establishing the link: Does web traffic from
various marketing channels influence direct traffic source purchases?Marketing Letters, 35(1):59–71, 2024.
David Reiley, Randall A Lewis, and Taylor Schreiner. Ad attributes and attribution: Large-scale field experiments
measure online customer acquisition.Available at SSRN 2049457, 2012.
Anindya Ghose and Vilma Todri-Adamopoulos. Toward a digital attribution model.MIS quarterly, 40(4):889–910,
2016.
Jesús Romero Leguina, Ángel Cuevas Rumín, and Rubén Cuevas Rumín. Digital marketing attribution: Understanding
the user path.Electronics, 9(11):1822, 2020.
Hao Zhou, Shaoming Li, Guibin Jiang, Jiaqi Zheng, and Dong Wang. Direct heterogeneous causal learning for resource
allocation problems in marketing. InProceedings of the AAAI Conference on Artificial Intelligence, volume 37, pages
5446–5454, 2023.
Kalyan Raman, Murali K Mantrala, Shrihari Sridhar, and Yihui Tang. Optimal resource allocation with time-varying
marketing effectiveness, margins and costs.Journal of Interactive Marketing, 26(1):43–52, 2012.
Chandra Pratap Singh and Rizwan Yousuf. Enhancing marketing strategies through big data-driven customer journey
mapping: Ananalysisusingmachinelearningalgorithms. In2024InternationalConferenceonEmergingInnovations
and Advanced Computing (INNOCOMP), pages 479–484. IEEE, 2024.
Kihwan Nam and Kanghyun Cho. Navigating the digital purchase journey: the impact of device type and visit channels
on consumer behavior.Industrial Management & Data Systems, 2025.
James R Bettman. Information processing models of consumer behavior.Journal of Marketing Research, 7(3):370–376,
1970.
26

Causal-Driven AttributionGeorgios Filippou
Joseph W Alba and J Wesley Hutchinson. Dimensions of consumer expertise.Journal of consumer research, pages
411–454, 1987.
Peter C Verhoef, Pallassana K Kannan, and J Jeffrey Inman. From multi-channel retailing to omni-channel retailing:
introduction to the special issue on multi-channel retailing.Journal of retailing, 91(2):174–181, 2015.
Susana Santos and Helena Martins Gonçalves. Consumer decision journey: Mapping with real-time longitudinal online
and offline touchpoint data.European Management Journal, 42(3):397–413, 2024.
Herbert A Simon. A behavioral model of rational choice.The quarterly journal of economics, pages 99–118, 1955.
James G March and Herbert A Simon.Organizations. John wiley & sons, 1993.
Richard Michael Cyert and James G March.A behavioral theory of the firm. Barakaldo Books, 2020.
Maayan S Malter, Morris B Holbrook, Barbara E Kahn, Jeffrey R Parker, and Donald R Lehmann. The past, present,
and future of consumer research.Marketing Letters, 31(2):137–149, 2020.
Joseph A Donndelinger and Scott M Ferguson. Design for the marketing mix: The past, present, and future of
market-driven engineering design.Journal of Mechanical Design, 142(6):060801, 2020.
JitendraGaurandKumkumBharti. Attributionmodellinginmarketing: Literaturereviewandresearchagenda.Academy
of Marketing Studies Journal, 24(4):1–21, 2020.
Jitendra Gaur, Kumkum Bharti, and Rahul Bajaj. Maximizing marketing impact: heuristic vs ensemble models for
attribution modeling.Global Knowledge, Memory and Communication, 2024.
Omolola Temitope Kufile, Oluwatolani Vivian Akinrinoye, Abiodun Yusuf Onifade, Onyinye Gift Ejike,
Bisayo Oluwatosin Otokiti, and Samuel Augustine Umezurike. Developing conceptual attribution models for
cross-platform marketing performance evaluation.International Journal of Multidisciplinary Research and Growth
Evaluation, 4(2):844–854, 2023.
Nathalie Dens and Karolien Poels. The rise, growth, and future of branded content in the digital media landscape.
International Journal of Advertising, 42(1):141–150, 2023.
Jun Tao, Qian Chen, James W Snyder Jr, Arava Sai Kumar, Amirhossein Meisami, and Lingzhou Xue. A graphical
point process framework for understanding removal effects in multi-touch attribution.Management Science, 71(9):
7312–7332, 2025.
Zine El Abidine El Mekkaoui and Hatim Benyoussef. The evolution of multi-touch attribution: Integrating advanced
technologies for superior marketing insights. InInternational Conference on Advanced Intelligent Systems for
Sustainable Development, pages 426–435. Springer, 2024.
Sam K Hui, Peter S Fader, and Eric T Bradlow. Path data in marketing: An integrative framework and prospectus for
model building.Marketing Science, 28(2):320–335, 2009.
PK Kannan, Werner Reinartz, and Peter C Verhoef. The path to purchase and attribution modeling: Introduction to
special section, 2016.
Lloyd S Shapley et al. A value for n-person games. 1953.
Panagiotis Papapetrou, Aristides Gionis, and Heikki Mannila. A shapley value approach for influence attribution. In
Joint European conference on machine learning and knowledge discovery in databases, pages 549–564. Springer,
2011.
Brian Dalessandro, Claudia Perlich, Ori Stitelman, and Foster Provost. Causally motivated attribution for online
advertising. InProceedings of the sixth international workshop on data mining for online advertising and internet
economy, pages 1–9, 2012.
Meghanath Macha Yadagiri, Shiv Kumar Saini, and Ritwik Sinha. A non-parametric approach to the multi-channel
attribution problem. InInternational Conference on Web Information Systems Engineering, pages 338–352. Springer,
2015.
Tahir Nisar and Man Yeung. Purchase conversions and attribution modeling in online advertising: an empirical
investigation. 2015.
Kaifeng Zhao, Seyed Hanif Mahboobi, and Saeed R Bagheri. Shapley value methods for attribution modeling in online
advertising.arXiv preprint arXiv:1804.05327, 2018.
T Kadyrov and DI Ignatov. Attribution of customers’ actions based on machine learning approach? InCEUR Workshop
Proceedings, pages 77–88, 2019.
Phillip E Pfeifer and Robert L Carraway. Modeling customer relationships as markov chains.Journal of interactive
marketing, 14(2):43–55, 2000.
27

Causal-Driven AttributionGeorgios Filippou
Christian Homburg, Viviana V Steiner, and Dirk Totzek. Managing dynamics in a customer portfolio.Journal of
marketing, 73(5):70–89, 2009.
Nikolay Archak, Vahab S Mirrokni, and S Muthukrishnan. Mining advertiser-specific user behavior using adfactors. In
Proceedings of the 19th international conference on World wide web, pages 31–40, 2010.
Eva Anderl, Ingo Becker, Florian V Wangenheim, and Jan Hendrik Schumann. Mapping the customer journey: A
graph-based framework for online attribution modeling.Available at SSRN 2343077, 2014.
Lukáš Kakalejčík, Jozef Bucko, PA Resende, and Martina Ferencova. Multichannel marketing attribution using markov
chains.Journal of Applied Management and Investments, 7(1):49–60, 2018.
N Sandeep, S Vasavi, and G Shruthi. Channel attribution using markov chain model.Turkish Online Journal of
Qualitative Inquiry, 12(7), 2021.
Xuhui Shao and Lexin Li. Data-driven multi-touch attribution models. InProceedings of the 17th ACM SIGKDD
international conference on Knowledge discovery and data mining, pages 258–264, 2011.
Ralph Breuer and Malte Brettel. Short-and long-term effects of online advertising: Differences between new and
existing customers.Journal of Interactive Marketing, 26(3):155–166, 2012.
HongshuangLiandPKKannan. Attributingconversionsinamultichannelonlinemarketingenvironment: Anempirical
model and a field experiment.Journal of marketing research, 51(1):40–56, 2014.
Randall Lewis, Florian Zettelmeyer, Brett R Gordon, Cristobal Garib, Johannes Hermle, Mike Perry, Henrique Romero,
and German Schnaidt. Amazon ads multi-touch attribution. Technical report, 2025.
Ya Zhang, Yi Wei, and Jianbiao Ren. Multi-touch attribution in online advertising with survival theory. In2014 ieee
international conference on data mining, pages 687–696. IEEE, 2014.
Wendi Ji and Xiaoling Wang. Additional multi-touch attribution for online advertising. InProceedings of the aaai
conference on artificial intelligence, volume 31, 2017.
Sai Kumar Arava, Chen Dong, Zhenyu Yan, Abhishek Pani, et al. Deep neural net with attention for multi-channel
multi-touch attribution.arXiv preprint arXiv:1809.02230, 2018.
KanRen,YuchenFang,WeinanZhang,ShuhaoLiu,JiajunLi,YaZhang,YongYu,andJunWang. Learningmulti-touch
conversion attribution with dual-attention mechanisms for online advertising. InProceedings of the 27th acm
international conference on information and knowledge management, pages 1433–1442, 2018.
Dongdong Yang, Kevin Dyer, and Senzhang Wang. Interpretable deep learning model for online multi-touch attribution.
CoRR, 2020.
Joseph F Hair Jr and Marko Sarstedt. Data, measurement, and causal inferences in machine learning: opportunities and
challenges for marketing.Journal of Marketing Theory and Practice, 29(1):65–77, 2021.
Sachin Kumar, Garima Gupta, Ranjitha Prasad, Arnab Chatterjee, Lovekesh Vig, and Gautam Shroff. Camta: Causal
attention model for multi-touch attribution. In2020 international conference on data mining workshops (icdmw),
pages 79–86. IEEE, 2020.
Di Yao, Chang Gong, Lei Zhang, Sheng Chen, and Jingping Bi. Causalmta: Eliminating the user confounding bias for
causal multi-touch attribution. InProceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and
Data Mining, pages 4342–4352, 2022.
Jiaming Tang. Dcrmta: Unbiased causal representation for multi-touch attribution.arXiv preprint arXiv:2401.08875,
2024.
Pavel Kireyev, Koen Pauwels, and Sunil Gupta. Do display ads influence search? attribution and dynamics in online
advertising.International Journal of Research in Marketing, 33(3):475–490, 2016.
Ali Shojaie and Emily B Fox. Granger causality: A review and recent advances.Annual Review of Statistics and Its
Application, 9(1):289–319, 2022.
Lin Yuan, Hao Xia, and Qiang Ye. The effect of advertising strategies on a short video platform: evidence from tiktok.
Industrial Management & Data Systems, 122(8):1956–1974, 2022.
Jagdish N Sheth and Rajendra S Sisodia. Marketing productivity: issues and analysis.Journal of Business research, 55
(5):349–362, 2002.
Neil A Morgan, Bruce H Clark, and Rich Gooner. Marketing productivity, marketing audits, and systems for marketing
performance assessment: integrating multiple perspectives.Journal of business research, 55(5):363–375, 2002.
Roland T Rust, Tim Ambler, Gregory S Carpenter, Vl Kumar, and Rajendra K Srivastava. Measuring marketing
productivity: Current knowledge and future directions.Journal of marketing, 68(4):76–89, 2004.
28

Causal-Driven AttributionGeorgios Filippou
Nils Wernerfelt, Anna Tuchman, Bradley T Shapiro, and Robert Moakler. Estimating the value of offsite tracking data
to advertisers: Evidence from meta.Marketing Science, 44(2):268–286, 2025.
Jean Paul Simon. Apis, the glue under the hood. looking for the “api economy”.Digital Policy, Regulation and
Governance, 23(5):489–508, 2021.
Simi Job, Xiaohui Tao, Taotao Cai, Haoran Xie, Lin Li, Qing Li, and Jianming Yong. Exploring causal learning through
graphneuralnetworks: Anin-depthreview.WileyInterdisciplinaryReviews: DataMiningandKnowledgeDiscovery,
15(2):e70024, 2025.
Rebecca J Herman, Jonas Wahl, Urmi Ninad, and Jakob Runge. Unitless unrestricted markov-consistent scm generation:
Better benchmark datasets for causal discovery. InCausal Learning and Reasoning, pages 1506–1531. PMLR, 2025.
Marit M Suttorp, Bob Siegerink, Kitty J Jager, Carmine Zoccali, and Friedo W Dekker. Graphical presentation of
confounding in directed acyclic graphs.Nephrology Dialysis Transplantation, 30(9):1418–1423, 2015.
Judea Pearl.Causality. Cambridge university press, 2009.
Christina Giarmatzi. A quantum causal discovery algorithm. InRethinking Causality in Quantum Mechanics, pages
125–150. Springer, 2019.
Samer B Nashed, Saaduddin Mahmud, Claudia V Goldman, and Shlomo Zilberstein. Causal explanations for sequential
decision making.Journal of Artificial Intelligence Research, 83, 2025.
Xiao Xie, Fan Du, and Yingcai Wu. A visual analytics approach for exploratory causal analysis: Exploration, validation,
and applications.IEEE Transactions on Visualization and Computer Graphics, 27(2):1448–1458, 2020.
Jakob Runge, Sebastian Bathiany, Erik Bollt, Gustau Camps-Valls, Dim Coumou, Ethan Deyle, Clark Glymour, Marlene
Kretschmer, Miguel D Mahecha, Jordi Muñoz-Marí, et al. Inferring causation from time series in earth system
sciences.Nature communications, 10(1):2553, 2019.
Philippe Brouillard, Chandler Squires, Jonas Wahl, Karen Sachs, Alexandre Drouin, Dhanya Sridhar, et al. The
landscape of causal discovery data: Grounding causal discovery in real-world applications. InCausal Learning and
Reasoning, pages 834–873. PMLR, 2025.
Peter J Danaher and Harald J van Heerde. Delusion in attribution: Caveats in using attribution for multimedia budget
allocation.Journal of Marketing Research, 55(5):667–685, 2018.
KaifengZhao, SeyedHanifMahboobi, andSaeedRBagheri. Revenue-basedattributionmodelingforonlineadvertising.
International Journal of Market Research, 61(2):195–209, 2019a.
Joseph Kelly, Jon Vaver, and Jim Koehler. A causal framework for digital attribution. Technical report, Technical report,
Google LLC, 2018. URL https://ai. google/research/pubs ..., 2018.
Guido W Imbens and Donald B Rubin.Causal inference in statistics, social, and biomedical sciences. Cambridge
university press, 2015.
Lu Cheng, Ruocheng Guo, Raha Moraffah, Paras Sheth, K Selçuk Candan, and Huan Liu. Evaluation methods and
measures for causal learning algorithms.IEEE Transactions on Artificial Intelligence, 3(6):924–943, 2022.
Silvia Acid and Luis M de Campos. Searching for bayesian network structures in the space of restricted acyclic partially
directed graphs.Journal of artificial intelligence research, 18:445–490, 2003.
Ioannis Tsamardinos, Laura E Brown, and Constantin F Aliferis. The max-min hill-climbing bayesian network structure
learning algorithm.Machine learning, 65(1):31–78, 2006.
Peter D Jamieson, John R Porter, and DR Wilson. A test of the computer simulation model arcwheat1 on wheat crops
grown in new zealand.Field crops research, 27(4):337–350, 1991.
Milan Despotovic, Vladimir Nedic, Danijela Despotovic, and Slobodan Cvetanovic. Evaluation of empirical models for
predicting monthly mean horizontal diffuse solar radiation.Renewable and Sustainable Energy Reviews, 56:246–260,
2016.
Cameron Cornell, Lewis Mitchell, and Matthew Roughan. Rank is all you need: development and analysis of robust
causal networks.Applied Network Science, 9(1):39, 2024.
Muhammad Arbab Arshad, Pallavi Kandanur, Saurabh Sonawani, Laiba Batool, and Muhammad Umar Habib. From
predictive importance to causality: Which machine learning model reflects reality?arXiv preprint arXiv:2409.02130,
2024.
Abdul Jabbar, Pervaiz Akhtar, and Samir Dani. Real-time big data processing for instantaneous marketing decisions: A
problematization approach.Industrial Marketing Management, 90:558–569, 2020.
29

Causal-Driven AttributionGeorgios Filippou
Arttu Purmonen, Elina Jaakkola, and Harri Terho. B2b customer journeys: Conceptualization and an integrative
framework.Industrial marketing management, 113:74–87, 2023.
Andrea Micheaux and Birgit Bosio. Customer journey mapping as a new way to teach data-driven marketing as a
service.Journal of Marketing Education, 41(2):127–140, 2019.
Sanjit K Roy, Bidit L Dey, David M Brown, Aman Abid, Chrysostomos Apostolidis, Michael Christofi, and Shlomo
Tarba. Business model innovation through ai adaptation: the role of strategic human resources management.British
Journal of Management, 36(2):546–559, 2025.
KimberleyHardcastle,LizetteVorster,andDavidMBrown. Understandingcustomerresponsestoai-drivenpersonalized
journeys: impacts on the customer experience.Journal of Advertising, 54(2):176–195, 2025.
ABIODUNYUSUFOnifade,JEFFREYCHIDERAOgeawuchi,AAAbayomi,OAAgboola,andOOGeorge. Advances
in multi-channel attribution modeling for enhancing marketing roi in emerging economies.Iconic Research and
Engineering Journals, 5(6):360–376, 2021.
Shantanu Seth and Sivakumar Ramakrishnan. Innovations in multi-touch attribution models: Beyond traditional
marketing analytics in the pharmaceutical sector. In2025 International Conference on Emerging Smart Computing
and Informatics (ESCI), pages 1–5. IEEE, 2025.
Catherine M Stein, Nathan J Morris, and Nora L Nock. Structural equation modeling. InStatistical human genetics:
Methods and protocols, pages 495–512. Springer, 2011.
Dawn Iacobucci. Everything you always wanted to know about sem (structural equations modeling) but were afraid to
ask.Journal of Consumer Psychology, 19(4):673–680, 2009.
Gordon CS Smith and Jill P Pell. Parachute use to prevent death and major trauma related to gravitational challenge:
systematic review of randomised controlled trials.Bmj, 327(7429):1459–1461, 2003.
Weihua Liu, Yanjie Liang, Ou Tang, and Xin Ma. Channel competition and collaboration in the presence of hybrid
retailing.Transportation Research Part E: Logistics and Transportation Review, 160:102658, 2022.
Statista. Advertising worldwide – statistics & forecasts.https://www.statista.com/outlook/amo/advertisi
ng/worldwide, 2025. Accessed: 28 October 2025.
Kui Zhao, Junhao Hua, Ling Yan, Qi Zhang, Huan Xu, and Cheng Yang. A unified framework for marketing budget
allocation. InProceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data
Mining, pages 1820–1830, 2019b.
Marc Fischer, Sönke Albers, Nils Wagner, and Monika Frie. Practice prize winner—dynamic marketing budget
allocation across countries, products, and marketing activities.Marketing Science, 30(4):568–585, 2011.
Ricardo Silva. Observational-interventional priors for dose-response learning.Advances in Neural Information
Processing Systems, 29, 2016.
WenjinNiu,ZijunGao,LiyanSong,andLingboLi. Comprehensivereviewandempiricalevaluationofcausaldiscovery
algorithms for numerical data.arXiv preprint arXiv:2407.13054, 2024.
Yuxue Jin, Yueqing Wang, Yunting Sun, David Chan, and Jim Koehler. Bayesian methods for media mix modeling with
carryover and shape effects.Google Research, pages 1–34, 2017.
Sandra L Ferketich, Joyce A Verran, Elizabeth A Hefferin, Frank E McLaughlin, Roberta Ann Smith, Ada Sue Hinshaw,
and Katherine J Young. Residual analysis for causal model assumptions.Western Journal of Nursing Research, 6(1):
41–76, 1984.
Trivellore E Raghunathan. Synthetic data.Annual review of statistics and its application, 8(1):129–140, 2021.
30
