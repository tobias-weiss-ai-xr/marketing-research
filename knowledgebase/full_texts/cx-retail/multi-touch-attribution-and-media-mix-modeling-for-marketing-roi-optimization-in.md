---
title: Multi-Touch Attribution and Media Mix Modeling for Marketing ROI Optimization in E-Commerce Platforms
url: https://doi.org/10.71465/fbf528
category: cx-retail
subcategory: framework
date: 2025-12
venue: Frontiers in Business and Finance
authors:
- Jingyi Liu
- Ying Wang
- Han Chien Lin
source: openalex-oa
pdf_url: https://sprcopen.org/index.php/FBF/article/download/528/483
pages: 20
chars: 73208
fetched_at: '2026-11-08T17:05:22+00:00'
kb_version: 1
---

# Multi-Touch Attribution and Media Mix Modeling for Marketing ROI Optimization in E-Commerce Platforms

Frontiers in Business and Finance Volume 2 Issue 2, 2025
ISSN: 3079-9325

379
Multi-Touch Attribution and Media Mix Modeling for Marketing
ROI Optimization in E-Commerce Platforms
Jingyi Liu1*, Ying Wang2, and Han Lin3
1 Cornell University, United States
2 Pepperdine University, United States
3 University of Wisconsin-Madison, United States
* Corresponding Author: jl3758@cornell.edu
Abstract
The exponential growth of digital marketing channels has created unprecedented
complexity in understanding customer journeys and optimizing marketing investments
in e -commerce platforms. Multi -touch attribution (MTA) and media mix modeling
(MMM) have emerged as complementary approaches for measuring marketing
effectiveness and maximizing return on investment (ROI). This  review examines the
theoretical foundations, methodological developments, and practical applications of
MTA and MMM in e -commerce contexts from 2019 onwards. Multi -touch attribution
enables granular tracking of individual customer touchpoints across digit al channels,
while media mix modeling provides aggregate -level insights into marketing
effectiveness through econometric analysis. Machine learning (ML) and artificial
intelligence (AI) have revolutionized both approaches, enabling more accurate
attribution modeling and predictive optimization. Recent advances integrate unified
measurement frameworks that combine the strengths of MTA and MMM to overcome
their individual limitations. This paper synthesizes current research on data
integration challenges, alg orithmic innovations, privacy considerations, and
implementation strategies. The review highlights how modern attribution systems
leverage deep learning (DL), Bayesian methods, and causal inference techniques to
navigate the increasingly complex digital ma rketing ecosystem. Emerging trends
include privacy -preserving measurement, cross -device attribution, and real -time
optimization algorithms that adapt to dynamic market conditions. The synthesis
reveals that successful ROI optimization requires not only sop histicated analytical
techniques but also organizational alignment, data infrastructure investment, and
continuous model validation against business outcomes.
Keywords
Multi-touch attribution, media mix modeling, marketing ROI, e-commerce analytics,
customer journey mapping, marketing optimization, attribution modeling, digital
marketing measurement, machine learning applications, conversion funnel analysis
Introduction
The contemporary e -commerce landscape presents marketers with an unprecedented array
of channels through which to reach potential customers, including search engines, social
media platforms, display advertising networks, email marketing, affiliate partnerships, and
mobile applications. This proliferation of touchpoints has fundamentally tran sformed the
customer journey from a linear path to a complex, non -linear process where consumers
interact with brands across multiple devices and platforms before making purchase decisions

Frontiers in Business and Finance Volume 2 Issue 2, 2025
ISSN: 3079-9325

380
[1]. Understanding the contribution of each marketing touchpoint to  final conversions has
become both critically important and exceptionally challenging for e -commerce businesses
seeking to optimize their marketing investments. Traditional last -click attribution models,
which assign full credit to the final interaction be fore conversion, have proven inadequate for
capturing the nuanced reality of modern customer journeys where awareness, consideration,
and decision -making occur across numerous interactions [2]. The inadequacy of simplistic
attribution approaches has led to  systematic misallocation of marketing budgets, with
channels that drive initial awareness or mid -funnel consideration receiving insufficient
investment while final -click channels are overvalued despite potentially benefiting from
earlier touchpoints that initiated customer interest [3].
Multi-touch attribution (MTA) emerged as a response to these limitations, offering
methodologies to distribute conversion credit across all touchpoints in the customer journey
based on their actual contribution to the final  outcome. By tracking individual user
interactions across channels and applying sophisticated algorithms to determine each
touchpoint's influence, MTA provides granular insights into channel performance and enables
more informed budget allocation decisions  [4]. The promise of MTA lies in its ability to reveal
the full complexity of customer journeys, identifying which combinations of touchpoints work
synergistically to drive conversions and how the sequence and timing of interactions
influence purchase prob ability. However, MTA faces significant challenges including data
fragmentation across platforms where different advertising networks and publishers
maintain separate tracking systems, cookie deprecation due to privacy regulations that limit
cross-site tracking capabilities, cross-device tracking limitations that create blind spots when
customers switch between smartphones and desktop computers, and the inability to measure
offline or upper -funnel brand -building activities that may not generate immediate tr ackable
interactions [5]. These constraints have led researchers and practitioners to revisit media mix
modeling (MMM), an econometric approach that uses aggregate -level data to quantify the
relationship between marketing inputs and business outcomes while  accounting for external
factors such as seasonality, pricing, and competitive activities [6].
Media mix modeling (MMM) offers complementary advantages to MTA by providing a holistic
view of marketing effectiveness across all channels, including traditiona l media that lack
digital tracking capabilities, and by being inherently privacy -compliant since it operates on
aggregated rather than individual -level data. The approach has been revitalized by advances
in machine learning (ML) and artificial intelligence  (AI) that enable more sophisticated
modeling of non -linear relationships, dynamic effects, and interaction patterns between
different marketing activities [7]. Recent developments have focused on reducing the latency
of MMM insights through automated data  pipelines and real-time model updating, addressing
a historical criticism that traditional MMM provided insights too slowly for tactical decision -
making [8]. The integration of Bayesian hierarchical modeling has further enhanced MMM by
enabling more robus t uncertainty quantification and the incorporation of prior knowledge
from past campaigns or similar markets, allowing practitioners to leverage learnings across
different product categories or geographic regions [9].
The convergence of MTA and MMM represe nts a promising frontier in marketing
measurement, with researchers developing unified frameworks that leverage the granular
insights of attribution models alongside the comprehensive perspective of econometric
analysis. These hybrid approaches aim to over come the limitations of each method
individually while providing decision -makers with a more complete understanding of
marketing effectiveness across both short -term conversion dynamics and long -term brand -

Frontiers in Business and Finance Volume 2 Issue 2, 2025
ISSN: 3079-9325

381
building impacts [10]. The rise of privacy regulat ions including the General Data Protection
Regulation and California Consumer Privacy Act has accelerated interest in measurement
solutions that balance granular insights with privacy preservation, making the MTA -MMM
integration particularly timely as mark eters seek alternatives to traditional cookie -based
tracking [11]. E -commerce platforms face unique challenges in implementing these
methodologies due to their rapid transaction cycles where purchase decisions can occur
within hours of initial exposure, hi gh customer acquisition costs that demand precise
measurement to maintain profitability, intense competition that requires continuous
optimization to maintain market share, and the need for real -time optimization to maintain
profitability in thin -margin bu sinesses where small improvements in marketing efficiency
translate directly to bottom-line results [12].
This review paper synthesizes recent academic and industry research on MTA and MMM
applications in e -commerce platforms, examining methodological inno vations,
implementation challenges, and future directions for marketing ROI optimization. The
analysis encompasses algorithmic developments in attribution modeling including deep
learning architectures and game -theoretic approaches, advances in econometric  techniques
for mix modeling including Bayesian methods and causal inference frameworks, data
infrastructure requirements for collecting and integrating multi -source marketing data,
organizational implementation considerations including change management and stakeholder
alignment, and emerging trends including privacy -preserving measurement techniques and
cross-platform attribution strategies. By providing a comprehensive overview of the current
state of knowledge, this review aims to guide both researchers  seeking to advance the field
through novel methodological contributions and practitioners working to implement effective
measurement systems in their organizations to drive tangible improvements in marketing
ROI. The subsequent sections examine the evolut ion of attribution and modeling approaches
from rule -based heuristics to sophisticated ML algorithms, explore specific methodological
frameworks including neural network architectures and Bayesian hierarchical models,
discuss practical applications and cha llenges including data quality issues and organizational
barriers, and conclude with insights into future research directions and implementation
strategies for maximizing marketing ROI in the dynamic e-commerce environment.
2. Literature Review
The evolution of marketing attribution methodologies reflects the increasing complexity of
customer journeys in digital environments where consumers may interact with dozens of
touchpoints before completing a purchase. Early research on attribution focused  primarily on
comparing simple rule -based models including first -click attribution that assigns all credit to
the initial touchpoint, last -click attribution that credits only the final interaction, and linear
attribution that distributes credit equally acr oss all touchpoints, with scholars noting that
each approach made different implicit assumptions about customer behavior and touchpoint
influence [13]. Studies comparing these heuristic models found significant discrepancies in
channel performance evaluati on depending on the attribution rule applied, with search
advertising appearing highly effective under last -click attribution but receiving less credit
under first-click models that emphasized awareness channels, highlighting the need for data -
driven appro aches that could empirically determine touchpoint contributions rather than
relying on predetermined rules [14]. The recognition that customer journeys vary
substantially across industries where business -to-business purchases involve extended
evaluation pe riods while impulse purchases complete quickly, across products where high -
consideration items generate more pre -purchase research than routine consumables, and

Frontiers in Business and Finance Volume 2 Issue 2, 2025
ISSN: 3079-9325

382
across customer segments where new customers conduct more extensive research than
repeat purcha sers, led researchers to explore algorithmic attribution methods capable of
learning optimal credit distribution from historical conversion data specific to each business
context [15].
Shapley value -based attribution emerged as a game -theoretic approach to  fairly distribute
conversion credit among touchpoints by considering all possible orderings of customer
interactions and calculating each touchpoint's marginal contribution across these
permutations, ensuring that credit allocation satisfies desirable pro perties including
symmetry where identical touchpoints receive equal credit and additivity where total credit
sums to the conversion value [16]. This method provides a mathematically principled solution
to the attribution problem and has been shown to prod uce more stable and interpretable
results compared to arbitrary rule -based approaches, particularly in scenarios where
touchpoint interactions exhibit strong synergistic effects such as when display advertising
generates awareness that makes subsequent sea rch advertisements more effective [17].
However, the computational complexity of Shapley value calculations grows exponentially
with the number of touchpoints, creating scalability challenges for e -commerce platforms
with extensive customer journeys that m ay involve twenty or more interactions across
multiple weeks, leading researchers to develop approximation algorithms using Monte Carlo
sampling and other techniques to make the approach tractable for real -world applications
with millions of customer journeys [18]. Markov chain models represent another probabilistic
approach to attribution that models customer journeys as sequences of state transitions
between touchpoints, with conversion credit allocated based on the removal effect where
each touchpoint's contribution is measured by how much conversion probability decreases
when that touchpoint is removed from possible journey paths [19].
The application of survival analysis techniques to attribution modeling has provided insights
into how different touchpo ints affect both the timing and likelihood of conversions
throughout the customer journey, recognizing that marketing effectiveness has temporal
dimensions beyond simple conversion probability. Researchers have developed hazard
models that account for the dynamic nature of conversion probabilities as customers progress
through various stages of the purchase funnel, revealing that certain touchpoints such as
retargeting advertisements primarily accelerate conversions by reducing time -to-purchase
while others  such as content marketing increase overall conversion likelihood by building
product knowledge and trust [20]. Machine learning approaches have revolutionized
attribution modeling by enabling the discovery of complex, non -linear relationships between
touchpoint exposures and conversion outcomes that traditional statistical models fail to
capture. Gradient boosting machines and random forests have been successfully applied to
predict conversion probabilities based on touchpoint sequences, with feature impor tance
metrics derived from these models used to assign attribution weights that reflect each
channel's predictive contribution to conversion outcomes [21]. Deep learning (DL) models,
particularly recurrent neural networks and long short -term memory network s, have
demonstrated superior performance in capturing sequential dependencies in customer
journeys and predicting conversion likelihood based on historical interaction patterns, with
the ability to learn that certain touchpoint sequences are particularly effective while others
signal low purchase intent [22].
Attention mechanisms adapted from natural language processing have been incorporated into
attribution models to automatically learn which touchpoints deserve more credit based on
their contextual rele vance within specific journey sequences, allowing the model to discover

Frontiers in Business and Finance Volume 2 Issue 2, 2025
ISSN: 3079-9325

383
that the same touchpoint may be highly influential in certain journey contexts but less
important in others [23]. The interpretability challenges associated with complex ML models,
particularly the black -box nature of DL architectures that make it difficult for marketers to
understand why specific attribution weights were assigned, have spurred research into
explainable AI techniques including SHAP values and attention visualization tha t can provide
transparent insights into attribution decisions while maintaining the predictive accuracy
advantages of sophisticated models [24]. Media mix modeling has undergone significant
methodological evolution since its origins in econometric analysis  of advertising effectiveness
conducted by consumer goods companies seeking to quantify television and print advertising
impacts on sales. Traditional MMM relied heavily on linear regression with lagged variables to
account for delayed effects where advert ising exposure in one period influences sales in
future periods, and adstocked transformations to capture advertising carry -over effects
where exposure builds up over time and gradually decays rather than having purely
instantaneous impact [25].
The adstoc k transformation, which models how advertising exposure accumulates in
consumer memory and decays at a rate determined by creative quality and media
characteristics, has been refined through research on optimal decay rate estimation using
methods including  grid search over candidate parameters and maximum likelihood
estimation, along with the incorporation of saturation effects that reflect diminishing
marginal returns where the tenth advertising impression generates less incremental impact
than the first [ 26]. Researchers have developed sophisticated functional forms including S -
curves that capture threshold effects where minimal advertising generates little response
until reaching awareness thresholds and Hill functions commonly used in pharmacology that
flexibly model both threshold and saturation phenomena through shape and scale parameters
[27]. Bayesian approaches to MMM have gained prominence due to their ability to incorporate
prior knowledge from previous analyses or expert judgment about reasonable effect sizes,
provide probabilistic forecasts with explicit uncertainty estimates rather than point
predictions, and naturally handle hierarchical data structures common in multi -market
analyses where some parameters are shared across markets while others vary to reflect local
conditions [28].
The development of probabilistic programming frameworks including Stan and PyMC has
made Bayesian MMM more accessible to practitioners by simplifying model specification
through high -level syntax and automating infere nce through efficient sampling algorithms
including Hamiltonian Monte Carlo that explore posterior distributions more effectively than
traditional Metropolis-Hastings approaches [29]. Research on MMM has increasingly focused
on reducing model latency by mo ving from quarterly or annual modeling cycles that provided
strategic insights but limited tactical utility, to weekly or even daily model updates enabled by
automated data pipelines that continuously ingest marketing spending and outcome data
along with e fficient estimation algorithms based on variational inference that approximate
posterior distributions orders of magnitude faster than full Markov chain Monte Carlo
sampling [30]. The integration of external data sources including weather patterns that aff ect
consumer behavior for certain product categories, economic indicators such as
unemployment rates and consumer confidence that influence discretionary spending, and
competitive activity including competitor pricing and promotional intensity, has enhance d
MMM by better isolating the true causal impact of a company's own marketing activities from
confounding factors that might otherwise bias effect estimates.

Frontiers in Business and Finance Volume 2 Issue 2, 2025
ISSN: 3079-9325

384
Causal inference techniques have been incorporated into both attribution and media mix
modeling to  strengthen the credibility of derived insights and support counterfactual
reasoning about what outcomes would have occurred under alternative marketing strategies,
moving beyond correlational analysis to establish more defensible causal claims. Recent
symmetry-aware causal -inference frameworks for web performance modeling further
illustrate how incorporating structural knowledge and invariant dependency patterns can
improve causal identifiability and intervention effectiveness, offering valuable methodological
guidance for causal marketing attribution and ROI optimization in complex digital ecosystems
[31]. Researchers have applied difference -in-differences designs to estimate incremental lift
from marketing campaigns by comparing outcomes in treated groups  exposed to marketing
activities versus control groups that were not exposed, while accounting for pre -existing
trends that might otherwise be mistaken for marketing effects [32]. Synthetic control
methods originally developed for policy evaluation have be en adapted to marketing contexts
to construct appropriate counterfactuals for treated units by creating weighted combinations
of control units that closely match pre -intervention characteristics, enabling causal inference
in settings where traditional rand omized experiments are infeasible due to business
constraints [33]. Instrumental variable approaches have been used to address endogeneity
concerns in MMM where marketing spending decisions may be correlated with unobserved
factors affecting sales, such as  anticipated demand shocks based on proprietary market
intelligence that prompt managers to increase advertising investment in specific periods,
creating spurious correlation between spending and outcomes [34].
The integration of MTA and MMM has emerged as  a critical research direction aimed at
overcoming the complementary limitations of each approach and providing marketers with a
more complete picture of marketing effectiveness. While MTA provides granular user -level
insights into the digital customer jou rney but struggles with view -through attribution where
display advertisement exposures may influence consumers who do not immediately click, and
cannot measure offline channels including television and outdoor advertising, MMM offers
comprehensive channel coverage including traditional media but lacks the individual journey
details needed to understand conversion path dynamics and optimize real -time bidding
strategies [35]. Unified measurement frameworks attempt to combine these strengths by
using MTA insig hts to inform MMM prior distributions on digital channel effectiveness,
incorporating MMM -derived estimates of offline channel impact as additional features in
attribution models to account for unmeasured touchpoints, or jointly estimating both models
within a hierarchical Bayesian framework that enforces consistency between the granular and
aggregate perspectives [36].
Research has explored how bottom -up MTA data aggregated to weekly or daily levels can be
used to validate and calibrate top -down MMM estima tes, creating a consistency check where
substantial divergence between the two approaches signals potential issues such as tracking
gaps in the attribution data or misspecified functional forms in the mix model that warrant
further investigation [37]. The complementary time horizons of MTA which excels at
explaining short -term conversion dynamics that occur within days or weeks of touchpoint
exposure, and MMM which better captures long -term brand -building effects that may take
months to fully manifest in sa les outcomes, have motivated researchers to develop
frameworks that explicitly model different temporal scales of marketing impact through
multi-level models with separate parameters for immediate response and long -term brand
equity contributions [38]. Pri vacy considerations have become increasingly central to
attribution and modeling research as regulatory changes including the European Union's
General Data Protection Regulation that requires explicit user consent for tracking and

Frontiers in Business and Finance Volume 2 Issue 2, 2025
ISSN: 3079-9325

385
platform policy changes i ncluding Apple's App Tracking Transparency framework and
Google's planned deprecation of third -party cookies limit access to individual -level tracking
data that has historically powered attribution systems [39].
Differential privacy techniques that add cal ibrated noise to attribution results have been
proposed to enable MTA while providing mathematical guarantees that individual user data
cannot be reconstructed from published attribution results, balancing the utility of attribution
insights with privacy p rotection through tunable privacy budgets [40]. Federated learning
approaches allow attribution models to be trained on decentralized data across multiple
parties including advertisers, publishers, and measurement providers without sharing raw
user-level d ata, instead exchanging only model parameters or gradients that aggregate
information from many users, addressing both privacy concerns and the data fragmentation
challenges inherent in cross -platform attribution [41]. Researchers have investigated how
MMM can serve as a privacy-friendly alternative or complement to MTA in the post-cookie era,
with empirical studies showing that aggregate -level modeling can still provide actionable
insights for strategic budget allocation decisions even when the granular us er-level data
required for tactical optimization is unavailable due to privacy constraints [42]. Cross -device
attribution has emerged as a critical challenge given that modern consumers frequently
switch between smartphones used for mobile browsing during commutes, tablets used for
relaxed evening research, and desktop computers used for final purchase transactions,
creating fragmented journey views when tracking systems cannot link these devices to the
same individual [43]. Deterministic cross-device matching based on user logins to proprietary
accounts provides accurate device linking when available, but requires users to authenticate
across all touchpoints which occurs inconsistently in practice as consumers may browse
anonymously before logging in to complete purchases [44].
3. Methodological Frameworks and Algorithmic Innovations
Contemporary MTA frameworks increasingly leverage advanced ML algorithms to model the
complex relationships between customer touchpoints and conversion outcomes, moving
beyond s imple rule -based credit allocation to sophisticated predictive models that learn
attribution patterns from data. Deep neural network architectures have been specifically
designed to process sequential customer journey data, with researchers developing mode ls
that incorporate attention mechanisms adapted from natural language processing to
automatically identify which interactions are most influential for particular types of
conversions, allowing the same touchpoint to receive different credit depending on i ts context
within the broader journey [45]. These DL approaches treat customer journeys as sequences
analogous to sentences in text analysis, applying recurrent layers including long short -term
memory units that maintain memory of earlier touchpoints while  processing later
interactions to capture temporal dependencies, and using embedding layers to represent
different channel types as continuous vectors that encode behavioral similarities discovered
from data rather than relying on manually specified channel taxonomies [46].

Frontiers in Business and Finance Volume 2 Issue 2, 2025
ISSN: 3079-9325

386

Figure 1: Neural network architecture for multi -touch attribution showing the input layer,
embedding layers, recurrent LSTM layers, attention mechanism, and conversion probability
output.
Figure 1 illustrates the neural network archite cture commonly employed for deep learning -
based multi -touch attribution. The input layer receives touchpoint sequences where each
interaction is represented as a combination of channel type, timestamp, and engagement
features such as click depth and time-on-site. Embedding layers transform categorical channel
identifiers into dense vector representations that capture behavioral similarities between
channels learned from data. The recurrent LSTM layers process sequential journey data while
maintaining memory  of previous interactions, enabling the model to learn that certain
touchpoint sequences are particularly effective predictors of conversion. The attention
mechanism computes importance weights for each touchpoint based on contextual relevance,
allowing the same channel to receive different attribution credit depending on its position and
surrounding interactions within the journey. The output layer produces conversion
probability predictions that, when compared across journeys with and without specific
touchpoints, yield attribution weights reflecting each channel's incremental contribution.
The ability of these models to automatically learn hierarchical representations from raw
clickstream data eliminates the need for extensive manual feature engineering t hat
characterized earlier attribution systems, making them particularly valuable in e -commerce
environments where customer behavior patterns evolve rapidly due to changing consumer
preferences, emerging technologies, and competitive dynamics [47]. Transfor mer-based
architectures originally developed for machine translation have been adapted to attribution
tasks, with self -attention mechanisms enabling the model to weigh the relevance of each
touchpoint relative to all other touchpoints in the journey simult aneously rather than
processing them sequentially from first to last, overcoming limitations of recurrent models
that may struggle to maintain memory across very long journey sequences [48]. This parallel
processing capability not only improves computation al efficiency for long customer journeys
involving dozens of interactions but also allows the model to discover long -range

Frontiers in Business and Finance Volume 2 Issue 2, 2025
ISSN: 3079-9325

387
dependencies such as how an initial display advertisement exposure weeks before purchase
interacts with a final retargeting advertisement to drive conversion.
Graph neural networks (GNN) represent another innovative approach to attribution modeling
that explicitly represents customer journeys as directed graphs where nodes correspond to
touchpoints and edges represent transitions betwee n them, with edge weights potentially
encoding the time interval between touchpoints or the strength of engagement. Related
graph-based learning advances in other transactional domains, such as multi -distance spatial-
temporal GNNs for anomaly detection in blockchain transactions, demonstrate how jointly
modeling structural dependencies and temporal dynamics can significantly enhance detection
accuracy—insights that are directly transferable to identifying anomalous or high -impact
touchpoint patterns in comp lex customer journey graphs [49]. By applying message -passing
algorithms on these journey graphs where information about conversion outcomes
propagates backward through the network from the final conversion node to earlier
touchpoints, GNN models can deter mine how much credit each touchpoint deserves based on
its structural position and connectivity patterns within the overall journey topology [50]. This
graph-based perspective naturally handles the varied structures of different customer
journeys without requiring all journeys to have the same length or follow the same sequence
of channel types, eliminating the need for padding short journeys or truncating long ones that
would be necessary for fixed -length input representations. Research has shown that GNN
attribution models excel at capturing synergistic effects between channels where the
contribution of one touchpoint depends on which other touchpoints preceded or followed it
[51].

Table 1: A comprehensive comparison table of attribution modeling approac hes across
computational complexity, data requirements, interpretability, modeling capabilities, and
scalability.
Table 1 presents a systematic comparison of nine attribution modeling approaches across
seven evaluation dimensions. Rule -based methods exhibit a clear trade -off pattern: Last-Click
and First -Click offer O(1) complexity with minimal data requirements and very high
interpretability but cannot capture non -linear effects or sequential dependencies, making

Frontiers in Business and Finance Volume 2 Issue 2, 2025
ISSN: 3079-9325

388
them suitable only for simple tracking and awareness analysis respectively. Linear and Time -
Decay methods require O(n) complexity and moderate data while maintaining high
interpretability, with Time -Decay offering limited sequential dependency modeling for
recency-focused optimization. Shapley Valu e provides fair credit allocation with sequential
dependency capture but suffers from O(2^n) complexity and poor scalability beyond 15
touchpoints. Markov Chain models balance O(n^2) complexity with good scalability while
capturing both non -linear effects and sequential dependencies, suited for path analysis.
Machine Learning methods achieve O(n·m·log m) complexity with strong modeling
capabilities but require over 100,000 journeys and sacrifice some interpretability. Deep
Learning demands the highest data requirements (>1M journeys) with O(n·m·d) complexity
and low interpretability but provides strong sequential dependency modeling for complex
patterns. Graph Neural Networks uniquely combine excellent scalability to long journeys with
strong sequential mode ling and non -linear effects capture, making them optimal for journey
topology and synergy effect analysis despite very high data requirements (>500k journeys).
Reinforcement learning (RL) has been applied to attribution problems by framing the
marketing op timization task as a sequential decision process where an agent learns to
allocate budget across channels to maximize cumulative conversions over time. This
framework integrates attribution measurement directly with optimization, learning both
which touchp oints are effective (the attribution question) and how to optimally sequence
marketing exposures (the optimization question) within a unified model [52]. Actor -critic
algorithms maintain separate policy networks that decide which marketing actions to take
and value networks that estimate expected future conversions, learning attribution weights
implicitly through the value function that reflects each touchpoint's contribution to long -term
outcomes rather than immediate conversions [53]. The exploration -exploitation tradeoff
inherent in RL naturally addresses the cold -start problem for new marketing channels or
creative variants by balancing the desire to exploit known effective strategies with the need to
gather information about potentially superior alterna tives, ensuring that attribution models
remain adaptive rather than becoming locked into suboptimal strategies based on historical
data [54].
Bayesian neural networks combine the representational flexibility of DL with probabilistic
reasoning, producing at tribution estimates accompanied by uncertainty quantification that
explicitly represents both epistemic uncertainty about the true model structure and aleatoric
uncertainty arising from inherent randomness in customer behavior [55]. These models
output ful l probability distributions over attribution weights rather than point estimates,
enabling risk-aware decision making where marketers can evaluate not just expected channel
performance but also the reliability of those expectations when allocating budgets.  For
channels or customer journey patterns with sparse data, the model appropriately expresses
high uncertainty, while frequently observed patterns receive confident predictions, providing
transparency about where measurement insights are most and least re liable [56]. Variational
inference techniques enable scalable training of Bayesian neural networks on large -scale
clickstream datasets by approximating intractable posterior distributions over network
weights with simpler parametric distributions optimized  through gradient -based methods,
making probabilistic DL computationally feasible for enterprise attribution applications
processing millions of customer journeys [57].
Media mix modeling has similarly benefited from algorithmic innovations that enhance it s
ability to capture complex, dynamic marketing response patterns. Regularized regression
techniques including ridge regression that shrinks coefficients toward zero proportionally,

Frontiers in Business and Finance Volume 2 Issue 2, 2025
ISSN: 3079-9325

389
lasso regression that drives some coefficients exactly to zero for automat ic variable selection,
and elastic net that combines both penalties have been widely adopted to address
multicollinearity issues that arise when multiple marketing channels are correlated in their
spending patterns across time periods [58]. Multicollineari ty inflates coefficient standard
errors and produces unstable estimates where small changes in data lead to large changes in
fitted parameters, making it difficult to reliably assess individual channel contributions.
Regularization methods improve estimate  stability by constraining coefficient magnitudes,
with cross-validation across time periods used to select optimal regularization strength that
balances model fit on training data with generalization to held-out test periods [59].
Bayesian structural time  series models provide a flexible framework for MMM that
decomposes sales outcomes into multiple additive components including a trend component
capturing long-term growth or decline, seasonal components at multiple time scales including
day-of-week and mo nth-of-year effects, holiday effects for major shopping events including
Black Friday and Cyber Monday, and marketing -driven components representing the causal
impact of advertising spending [60]. This decomposition enables practitioners to isolate
marketing effects from organic baseline sales and environmental factors, providing clearer
attribution of outcomes to marketing activities versus external drivers. The Bayesian
approach facilitates incorporation of prior knowledge about reasonable parameter value s
based on previous analyses or industry benchmarks, regularizing estimates toward sensible
ranges while allowing data to override priors when evidence is sufficiently strong [61]. State -
space representations enable efficient recursive estimation algorithm s that update model fits
incrementally as new data arrives rather than refitting from scratch, supporting the move
toward real -time MMM that provides continuously updated insights rather than quarterly
retrospective analyses [62].

Frontiers in Business and Finance Volume 2 Issue 2, 2025
ISSN: 3079-9325

390
Figure 2: A decompositi on plot showing the Bayesian structural time series model components
for a representative e-commerce company over a one-year period.
Figure 2 demonstrates Bayesian structural time series decomposition applied to e -commerce
revenue data over a one -year per iod. The top panel displays observed weekly revenue
alongside the model fit, with shaded regions indicating 90% credible intervals that quantify
estimation uncertainty. The trend component in the second panel reveals gradual growth
trajectory after control ling for seasonal and marketing effects, providing insight into
underlying business momentum. The seasonal panel captures recurring patterns including
elevated weekend activity and month -end spikes associated with payroll cycles, which must
be isolated to accurately attribute remaining variation to marketing activities. The bottom
panel decomposes marketing contributions by channel, showing paid search as the largest
contributor, display advertising providing moderate incremental revenue, social media
advertising with growing contribution over time suggesting increasing effectiveness or
investment, and email marketing delivering consistent baseline returns. The credible intervals
widen for channels with smaller contributions, appropriately reflecting greater  uncertainty
when signal -to-noise ratios are lower, enabling marketers to distinguish reliably measured
effects from estimates requiring additional data or validation.
Hierarchical Bayesian modeling extends MMM to scenarios involving multiple products,
geographic markets, or customer segments by allowing marketing response parameters to
vary across groups while sharing information through hierarchical priors that encode the
assumption that different groups have related but not identical response patterns  [63]. This
partial pooling approach produces more stable estimates for groups with limited data by
borrowing strength from other similar groups, while still allowing for group -specific effects
when data support divergence from the overall pattern. For exa mple, a national retailer
operating in dozens of markets might find that some markets exhibit stronger price sensitivity
while others respond more to advertising, with hierarchical modeling enabling reliable
market-specific parameter estimates even when in dividual market samples are modest by
leveraging cross -market patterns [64]. Hierarchical structures also naturally represent
organizational realities where marketing effectiveness often exhibits both systematic
differences across business units and common  patterns that apply broadly, aligning model
structure with business structure to produce actionable insights at multiple organizational
levels [65].
4. Implementation Strategies and Practical Challenges
The practical implementation of MTA and MMM systems in e-commerce platforms extends far
beyond selecting appropriate algorithms, encompassing data infrastructure development,
organizational change management, continuous validation processes, and strategic alignment
of measurement frameworks with business ob jectives. Data integration represents a
fundamental challenge as customer journey information typically resides in fragmented
systems across advertising platforms that log impression and click data, web analytics tools
that capture on -site behavior, custom er relationship management systems that maintain
purchase history and customer attributes, email service providers that track message delivery
and engagement, and mobile app analytics that record in-app interactions. Establishing robust
data pipelines that  can reliably collect, normalize, transform, and integrate these disparate
data sources requires significant engineering investment in both initial development and
ongoing maintenance to accommodate frequent platform API changes, evolving data schemas,
and scaling challenges as transaction volumes grow. Related advances in adaptive

Frontiers in Business and Finance Volume 2 Issue 2, 2025
ISSN: 3079-9325

391
reinforcement learning for automated cybersecurity incident response illustrate how policy -
learning agents can optimize sequential decision -making under uncertainty and dynamic
operational conditions, offering transferable insights for implementing robust, real -time
optimization strategies in large -scale marketing attribution and budget allocation systems
[66].
The challenge is compounded by pervasive data quality issues including  missing touchpoints
due to tracking implementation errors or ad blocker usage that prevents pixel fires, duplicate
events generated by instrumentation bugs that fire the same tracking code multiple times, bot
traffic from scrapers and fraudulent click gen erators that must be filtered to avoid distorting
attribution models with non -human interactions, and identifier fragmentation where the
same customer appears as multiple distinct users due to cookie deletion or switching between
authenticated and anonymou s browsing [67]. Implementing comprehensive data quality
monitoring with automated alerts for anomalies such as sudden drops in tracking coverage or
unusual spikes in certain event types, along with regular audits comparing different data
sources to identi fy discrepancies, becomes essential for maintaining attribution system
accuracy [68]. Privacy regulations including consent requirements under the General Data
Protection Regulation and California Consumer Privacy Act impose additional constraints on
data collection practices, necessitating consent management systems that track user
preferences and ensure data pipelines respect opt -out choices, while data retention policies
require automated deletion of historical journey data after specified periods [69].
Organizational resistance to new attribution methodologies frequently emerges when
sophisticated data-driven models produce results that differ substantially from familiar last -
click attribution, particularly when channels that previously appeared highly e ffective receive
reduced credit under more nuanced approaches that account for upper -funnel contribution.
Marketing managers whose performance is evaluated based on channel -specific metrics may
perceive attribution changes as threatening to their team's re sources or reputation, creating
political dynamics that impede adoption regardless of analytical merit [70]. Effective change
management strategies must address these concerns through transparent communication
about model logic using concrete journey examples that illustrate how credit allocation works,
rigorous validation of results against experimental ground truth from randomized holdout
tests or geo-experiments that provide unbiased lift estimates, phased rollouts that begin with
pilot channels or busin ess units to build confidence before enterprise -wide deployment, and
stakeholder involvement in model development to create buy -in and ensure the final system
addresses real business questions rather than being technically sophisticated but practically
irrelevant [71].
The technical skills required to develop, deploy, and maintain advanced attribution and
modeling systems create talent acquisition and retention challenges, as data scientists
possessing both deep technical expertise in ML and domain knowledg e of marketing
dynamics remain scarce relative to demand across industries. Organizations must decide
whether to build internal capabilities through hiring and training, partner with specialized
analytics vendors who provide measurement platforms and manag ed services, or adopt
hybrid approaches that combine internal strategic oversight with external technical execution
[72]. Each approach involves tradeoffs between control and flexibility favoring in -house
development, speed to deployment and access to best  practices favoring vendor solutions,
and cost considerations that vary depending on organizational scale and analytical maturity.
Building effective analytics teams requires not only individual technical skills but also cross -
functional collaboration capa bilities as attribution systems succeed only when data scientists

Frontiers in Business and Finance Volume 2 Issue 2, 2025
ISSN: 3079-9325

392
work closely with marketing practitioners who provide domain expertise and business
context [73].
Real-time optimization based on attribution insights requires low-latency data processing and
model inference capabilities that can update marketing tactics within operational timeframes
measured in hours rather than days or weeks, often necessitating investment in streaming
data infrastructure using technologies including Apache Kafka for messag e queuing and
Apache Flink for real -time computation, along with model serving platforms that expose
trained attribution models through low -latency APIs [74]. The engineering complexity of
production ML systems extends beyond model training to encompass fe ature engineering
pipelines that compute derived attributes from raw clickstream data, model monitoring
systems that detect performance degradation through metrics including prediction accuracy
and feature distribution shifts, and automated retraining work flows that periodically update
models as customer behavior evolves, requiring ML operations capabilities that many
marketing organizations initially lack [75].
Model interpretability demands from business stakeholders who must trust and act on model
outputs have driven adoption of explainable AI techniques that articulate why specific
attribution weights emerged from complex algorithms even when underlying models involve
non-linear transformations difficult to intuit directly. Techniques including SHAP valu es
derived from game theory provide locally faithful explanations showing how each feature
contributed to individual journey predictions, attention weight visualization reveals which
touchpoints the model focused on when making attribution decisions, and c ounterfactual
explanations demonstrate how attribution would change if certain touchpoints were removed
[76]. Providing these interpretability tools alongside attribution estimates helps build
stakeholder confidence and enables productive conversations abo ut model behavior,
facilitating identification of potential issues where models may have learned spurious
correlations from biased training data or where business logic suggests model outputs require
adjustment [77].
Validation and performance monitoring o f attribution models presents unique challenges
because true attribution weights are fundamentally unobservable, unlike supervised learning
tasks where ground truth labels enable straightforward accuracy measurement. Practitioners
must rely on indirect val idation approaches including internal consistency checks where
different attribution methodologies are compared and substantial divergence investigated,
experimental validation where randomized holdout tests or geo -experiments provide
unbiased estimates of channel lift that serve as benchmarks for model calibration, and out -of-
sample prediction accuracy where models are evaluated on their ability to forecast future
conversions based on journey prefixes [78]. Establishing rigorous validation frameworks
requires investment in experimentation infrastructure including the ability to randomly
assign users or geographic markets to treatment and control conditions, along with statistical
methods for analyzing experiment results accounting for factors including spil lover effects
where marketing in treatment markets affects control markets, and interference where
treating some users within a market affects untreated users through word -of-mouth or
marketplace dynamics [79].
The cost-benefit analysis of implementing sop histicated measurement systems must carefully
weigh development and maintenance costs against incremental value from improved
marketing decisions, recognizing that smaller e -commerce operations with limited marketing
budgets may find that simpler heuristic  models provide sufficient guidance relative to their

Frontiers in Business and Finance Volume 2 Issue 2, 2025
ISSN: 3079-9325

393
decision complexity, while larger enterprises spending millions annually on customer
acquisition can justify substantial investment in advanced analytics infrastructure that
produces even modest percent age improvements in efficiency [80]. Beyond direct system
costs, organizations must consider opportunity costs of data science resources devoted to
attribution versus alternative applications including demand forecasting, personalization, or
inventory optimization, ensuring measurement investments align with strategic priorities and
capability gaps [81]. Demonstrating attribution system value requires establishing clear links
between measurement insights and business actions taken in response, along with
quantification of outcome improvements attributable to those actions, creating accountability
for analytics investments and building institutional support for continued development [82].
The dynamic nature of digital marketing ecosystems means that attributi on models inevitably
deteriorate over time as customer behavior shifts in response to technological change
including mobile adoption and voice search, as new marketing channels emerge including
connected television and streaming audio that create novel tou chpoint types, and as
competitive dynamics evolve with entry of new rivals or shifts in incumbent strategies.
Continuous model monitoring tracks leading indicators of degradation including declining
prediction accuracy on recent data compared to historical  performance, increasing frequency
of rare journey patterns not well represented in training data, and divergence between
model-based attribution and experimental lift measurements [83]. Automated retraining
pipelines that periodically update models on rol ling windows of recent data help maintain
accuracy, though practitioners must balance model freshness against stability concerns where
overly frequent updates create volatility in attribution weights that complicates longitudinal
analysis and performance evaluation [84].
5. Conclusion
The landscape of marketing measurement in e -commerce platforms has undergone
remarkable transformation through the maturation of multi -touch attribution and media mix
modeling methodologies enhanced by advances in ML and AI te chnologies. The
complementary nature of MTA, which provides granular customer journey insights, and MMM,
which offers comprehensive cross -channel perspective including unmeasurable touchpoints,
creates opportunities for integrated measurement frameworks th at deliver more complete
understanding of marketing effectiveness than either approach alone. As customer journeys
grow increasingly complex with proliferating touchpoints across expanding device
ecosystems and channel options, sophisticated analytical app roaches become essential for
navigating this complexity and extracting actionable insights that drive marketing ROI
optimization.
The algorithmic innovations spanning DL architectures that process sequential journey data
through attention mechanisms and re current networks, graph neural networks that explicitly
model journey topology and touchpoint relationships, RL frameworks that integrate
measurement and optimization, Bayesian hierarchical models that enable information sharing
across markets while accoun ting for local variation, and causal inference techniques that
strengthen credibility of derived insights represent substantial progress in technical
capabilities available to marketing analysts. However, successful implementation requires
addressing numer ous practical challenges including data integration across fragmented
systems, organizational change management to build stakeholder buy -in for sophisticated
approaches, continuous validation against experimental benchmarks, and significant

Frontiers in Business and Finance Volume 2 Issue 2, 2025
ISSN: 3079-9325

394
investment in both technical infrastructure and human capabilities spanning data engineering,
ML operations, and cross-functional collaboration.
Privacy considerations have emerged as defining constraints shaping the evolution of
attribution practices as third -party cook ie deprecation and tightening regulatory
requirements limit granular user tracking. MMM gains renewed relevance as a privacy -
compliant approach operating on aggregate data, while emerging techniques including
differential privacy and federated learning off er paths toward preserving measurement
capabilities with reduced privacy risk. The ability to validate models through rigorous
experimentation and maintain multiple complementary measurement perspectives becomes
increasingly critical as marketers navigate tradeoffs between comprehensive tracking and
privacy respect. Organizations must develop flexible measurement strategies that can adapt
to evolving privacy landscape while maintaining sufficient insight for effective decision
making.
Looking forward, sever al critical challenges demand continued research and innovation.
Cross-device attribution remains imperfectly solved absent deterministic identifiers,
requiring advances in probabilistic identity resolution. Integration of offline touchpoints
including store visits and traditional media exposures into unified journey views necessitates
new measurement technologies and methodologies. Real -time optimization capabilities must
continue evolving to reduce latency between execution and feedback. The field will be nefit
from ongoing collaboration between academic researchers developing novel methods and
industry practitioners testing approaches in operational environments, creating virtuous
cycles where practical challenges motivate theoretical advances that subsequ ently transform
practice. As e-commerce continues capturing increasing share of retail activity and marketing
budgets expand to address intensifying competition, accurate measurement and optimization
capabilities will become even more critical competitive differentiators rewarding
organizations that successfully navigate the complex landscape of modern marketing
analytics.
References
[1] Pires, P. B., Prisco, M., Delgado, C., & Santos, J. D. (2024). A conceptual approach to understanding
the customer experience  in e-commerce: An empirical study. Journal of Theoretical and Applied
Electronic Commerce Research, 19(3), 1943-1983.
[2] Yang, J., Zeng, Z., & Shen, Z. (2025). Neural -Symbolic Dual -Indexing Architectures for Scalable
Retrieval-Augmented Generation. IEEE Access.
[3] Busca, L., & Bertrandias, L. (2020). A framework for digital marketing research: investigating the
four cultural eras of digital marketing. Journal of Interactive Marketing, 49(1), 1-19.
[4] Wang, Z., Yang, C., Yuan, H., & Zhang, Y. (2021). Aggregation bia s in estimating log‐log demand
function. Production and Operations Management, 30(11), 3906-3922.
[5] Marin, J. (2023). Bayesian Methods for Media Mix Modelling with shape and funnel effects. arXiv
preprint arXiv:2311.05587.
[6] Chen, Y., & Liu, J. (2025, May). AI-Driven Marketing Strategy Optimization in the Digital Economy: A
Machine Learning Approach. In Proceedings of the 2025 International Conference on Digital
Economy and Intelligent Computing (pp. 239-242).
[7] Hosseinnia Shavaki, F., & Ebrahimi Ghahnavieh, A. ( 2023). Applications of deep learning into
supply chain management: a systematic literature review and a framework for future research.
Artificial Intelligence Review, 56(5), 4447-4489.
[8] Pajari, R. (2023). The potential benefits of simultaneous use of media mix modeling and attribution
modeling for advertising effectiveness.
[9] M. Allenby, G. (2025). Advancing the science of marketing. Marketing Letters, 36(2), 205-214.

Frontiers in Business and Finance Volume 2 Issue 2, 2025
ISSN: 3079-9325

395
[10] Kim, M., & Zhang, J. (2023). Discovering online shopping preference structures in large and
frequently changing store assortments. Journal of Marketing Research, 60(4), 665-686.
[11] Goldfarb, A., & Tucker, C. E. (Eds.). (2024). The Economics of Privacy. University of Chicago Press.
[12] Van Ewijk, B. J., Stubbe, A., Gijsbrechts, E., & Dekimpe, M. G. (2021 ). Online display advertising for
CPG brands:(When) does it work?. International Journal of Research in Marketing, 38(2), 271-289.
[13] Beck, B. B., Petersen, J. A., & Venkatesan, R. (2021). Multichannel data -driven attribution models:
A review and research age nda. Marketing Accountability for Marketing and Non -marketing
Outcomes, 153-189.
[14] Yang, S., Ding, G., Chen, Z., & Yang, J. (2025). GART: Graph Neural Network -based Adaptive and
Robust Task Scheduler for Heterogeneous Distributed Computing. IEEE Access.
[15] Berman R, Katona Z. Curation algorithms and filter bubbles in social networks. Marketing Science.
2020;39(2):296-316.
[16] Kadyrov, T., & Ignatov, D. I. (2019). Attribution of customers’ actions based on machine learning
approach.
[17] Molina, E., Tejada, J., & Weiss, T . (2022). Some game theoretic marketing attribution models.
Annals of Operations Research, 318(2), 1043-1075.
[18] Liang, Z., Gao, H., & Zhang, J. (2024). Towards Efficient, Fair and Interpretable Neural Dynamic
Data Valuation.
[19] Gao, L., Melero, I., & Sese, F. J . (2020). Multichannel integration along the customer journey: a
systematic review and research agenda. The Service Industries Journal, 40(15-16), 1087-1118.
[20] Yin, J., Feng, Y., & Liu, Y. (2025). Modeling behavioral dynamics in digital content consumption: An
attention-based neural point process approach with applications in video games. Marketing
Science, 44(1), 220-239.
[21] Chopra, R., Bhardwaj, S., Thaichon, P., & Nair, K. (2025). Unpacking service failures in artificial
intelligence: future research directio ns. Asia Pacific Journal of Marketing and Logistics, 37(2),
349-364.
[22] Yang, D., Dyer, K., & Wang, S. (2020). Interpretable deep learning model for online multi -touch
attribution. arXiv preprint arXiv:2004.00384.
[23] Xue, S., He, C., Hua, Z., Li, S., Wang, G., &  Cao, L. (2024). Interactive attention -based capsule
network for click-through rate prediction. IEEE Access.
[24] Guidotti, R., Monreale, A., Pedreschi, D., & Giannotti, F. (2021). Principles of explainable artificial
intelligence. In Explainable AI within the digital transformation and cyber physical systems: XAI
Methods and Applications (pp. 9-31). Cham: Springer International Publishing.
[25] Kilian, L., & Zhou, X. (2023). The econometrics of oil market VAR models. In Essays in honor of
joon y. park: Econometric methodology in empirical applications (pp. 65-95). Emerald Publishing
Limited.
[26] Abedian, M., Amindoust, A., Maddahi, R., & Jouzdani, J. (2022). A game theory approach to
selecting marketing-mix strategies. Journal of Advances in Management Research, 19(1), 139-158.
[27] Newell, J. (2022). Political advertising saturation in the 2016 Iowa caucuses. Journal of Political
Marketing, 21(1), 1-22.
[28] McAlister, L., Germann, F., Chisam, N., Hayes, P., Lynch, A., & Stewart, B. (2023). A taxonomy of
marketing organizations. Journal of the Academy of Marketing Science, 51(3), 617-635.
[29] Marwala, T., Mbuvha, R., & Mongwe, W. T. (2023). Hamiltonian Monte Carlo methods in machine
learning. Elsevier.
[30] Bobrytskyy, S., & Stříteský, V. (2024). A systematic review of online marketing effe cts on online
and offline sales: A framework and state of research. Market-Tržište, 36(1), 59-82.
[31] Lin, H., & Liu, W. (2025). Symmetry -Aware Causal-Inference-Driven Web Performance Modeling:
A Structure -Aware Framework for Predictive Analysis and Actionable  Optimization. Symmetry,
17(12), 2058.
[32] Dargnies, M. P., Hakimov, R., & Kübler, D. (2024). Aversion to hiring algorithms: Transparency,
gender profiling, and self-confidence. Management Science.
[33] Chen, Q., & Li, W. (2024). On the sparsity of synthetic contro l method. Journal of Applied
Economics, 27(1), 2361184.

Frontiers in Business and Finance Volume 2 Issue 2, 2025
ISSN: 3079-9325

396
[34] Gordon, B. R., Zettelmeyer, F., Bhargava, N., & Chapsky, D. (2019). A comparison of approaches to
advertising measurement: Evidence from big field experiments at Facebook. Marketing Science,
38(2), 193-225.
[35] Zhou, M., Abhishek, V., Kennedy, E. H., Srinivasan, K., & Sinha, R. (2025). Linking clicks to bricks:
Understanding the effects of email advertising on multichannel sales. Information Systems
Research, 36(1), 225-238.
[36] LOURO, A. C., Jaklič, J., & Brandão, M. M. (2023). Marketing Analytics & Organizational Culture Fit:
scale development and validation. International Journal of Business and Marketing, 8(1), 45-61.
[37] Wang, Y., Ding, G., Zeng, Z., & Yang, S. (2025). Causal -Aware Multimodal Transformer fo r Supply
Chain Demand Forecasting: Integrating Text, Time Series, and Satellite Imagery. IEEE Access.
[38] Danaher, P. J., Danaher, T. S., Smith, M. S., & Loaiza -Maya, R. (2020). Advertising effectiveness for
multiple retailer -brands in a multimedia and multich annel environment. Journal of Marketing
Research, 57(3), 445-467.
[39] Johnson, G. A., Shriver, S. K., & Du, S. (2020). Consumer privacy choice in online advertising: Who
opts out and at what cost to industry?. Marketing Science, 39(1), 33-51.
[40] Singh, M. (2024).  Privacy-preserving marketing analytics: Navigating the future of cookieless
tracking. International Journal of Enhanced Research in Management & Computer Applications,
13, 2319-7471.
[41] Yang, Q., Liu, Y., Chen, T., & Tong, Y. (2019). Federated machine learning: Concept and applications.
ACM Transactions on Intelligent Systems and Technology (TIST), 10(2), 1-19.
[42] Agrawal, A., Gans, J., & Goldfarb, A. (2019). Economic policy for artificial intelligence. Innovation
policy and the economy, 19(1), 139-159.
[43] Li, J., Luo, X., Lu, X., & Moriguchi, T. (2021). The double -edged effects of e -commerce cart
retargeting: does retargeting too early backfire?. Journal of Marketing, 85(4), 123-140.
[44] De Keyzer, F., Van Noort, G., & Kruikemeier, S. (2022). Going too far? How consume rs respond to
personalized advertising from different sources. Journal of Electronic Commerce Research, 23(3),
138-159.
[45] Ramachandran, P., Parmar, N., Vaswani, A., Bello, I., Levskaya, A., & Shlens, J. (2019). Stand -alone
self-attention in vision models. Advances in neural information processing systems, 32.
[46] Scaronel, B., Baeza-Yates, R., & Bernhardson, E. (2023, July). Understanding Search Behavior Bias.
In Advances in Bias and Fairness in Information Retrieval: 4th International Workshop, BIAS
2023, Dublin, Ireland, April 2, 2023, Revised Selected Papers (p. 134). Springer Nature.
[47] Ou, W., Chen, B., Dai, X., Zhang, W., Liu, W., Tang, R., & Yu, Y. (2023). A survey on bid optimization
in real-time bidding display advertising. ACM Transactions on Knowledge Disc overy from Data,
18(3), 1-31.
[48] Su, L., Zuo, X., Li, R., Wang, X., Zhao, H., & Huang, B. (2025). A systematic review for transformer -
based long-term series forecasting. Artificial Intelligence Review, 58(3), 80.
[49] Chen, S., Liu, Y., Zhang, Q., Shao, Z., & Wang , Z. (2025). Multi‐Distance Spatial‐Temporal Graph
Neural Network for Anomaly Detection in Blockchain Transactions. Advanced Intelligent Systems,
2400898.
[50] Hamilton, W. L. (2020). Graph representation learning. Morgan & Claypool Publishers.
[51] Kotaru, C., Uday araju, P., Kolasani, D., Sayana, R., Tumkunta, S., & Gummadi, V. (2025, March).
Behavioral Pattern Analysis Framework with Markov Chains and Graph Neural Networks for
Scalable Customer Behavior Prediction in Travel Reservations. In 2025 International Confe rence
on Machine Learning and Autonomous Systems (ICMLAS) (pp. 880-888). IEEE.
[52] Cai, T., Jiang, J., Zhang, W., Zhou, S., Song, X., Yu, L., ... & Zhang, G. (2023, February). Marketing
budget allocation with offline constrained deep reinforcement learning. In  Proceedings of the
Sixteenth ACM International Conference on Web Search and Data Mining (pp. 186-194).
[53] Mou, Z., Huo, Y., Bai, R., Xie, M., Yu, C., Xu, J., & Zheng, B. (2022). Sustainable online reinforcement
learning for auto-bidding. Advances in Neural Information Processing Systems, 35, 2651-2663.
[54] Chen, C., Wang, G., Liu, B., Song, S., Mao, K., Yu, S., & Liu, J. (2025). Real -time bidding with multi -
agent reinforcement learning in multi -channel display advertising. Neural Computing and
Applications, 37(1), 499-511.

Frontiers in Business and Finance Volume 2 Issue 2, 2025
ISSN: 3079-9325

397
[55] Filos, A., Farquhar, S., Gomez, A. N., Rudner, T. G., Kenton, Z., Smith, L., ... & Gal, Y. (2019). A
systematic comparison of bayesian deep learning robustness in diabetic retinopathy tasks. arXiv
preprint arXiv:1912.10481.
[56] Jospin, L. V., Buntin e, W., Boussaid, F., Laga, H., & Bennamoun, M. (2020). Hands -on Bayesian
Neural Networks –a Tutorial for Deep Learning Users. arXiv e -prints, page. arXiv preprint
arXiv:2007.06823.
[57] Ganguly, A., & Earp, S. W. (2021). An introduction to variational inference.  arXiv preprint
arXiv:2108.13083.
[58] Gurung, B., Singh, K. N., Lama, A., & Gurung, B. (2023). Least Absolute Shrinkage and Selection
Operator (LASSO) Regression. Statistical Procedures for Analyzing Agricultural Data using R, 113.
[59] Frost, R., Armstrong, B. C.,  & Christiansen, M. H. (2019). Statistical learning research: A critical
review and possible new directions. Psychological bulletin, 145(12), 1128.
[60] Gianacas, C., Liu, B., Kirk, M., Di Tanna, G. L., Belcher, J., Blogg, S., & Muscatello, D. J. (2023).
Bayesian structural time series, an alternative to interrupted time series in the right
circumstances. Journal of Clinical Epidemiology, 163, 102-110.
[61] OGUNDEJI, R., & Okemakinde, S. S. (2025). Bayesian Structural Time Series Model and SARIMA
Model for Rainfall Forecasting in Nigeria. Journal of Statistical Modeling & Analytics (JOSMA), 7(1).
[62] Durbin J, Koopman SJ. Time Series Analysis by State Space Methods. Oxford University Press;
2019.
[63] Ghitza, Y., & Gelman, A. (2020). Voter registration databases and MRP: Toward the use of large -
scale databases in public opinion research. Political Analysis, 28(4), 507-531.
[64] Xavier, B. (2025). Bayesian Methods in Marketing: A Bibliometric Examination of Trends and
Patterns. Bibliometric Analyses in Data‐Driven Decision‐Making, 527-549.
[65] Mallik, A. (2021). Statistical Rethinking: A Bayesian Course with Examples in R and Stan: edited
by Richard McElreath, Boca Raton, FL: CRC Taylor and Francis, 2020, xvi+ 589 pp., $94.94
(Hardback), ISBN: 978-0-367-13991-9.
[66] Ren, S., Jin, J., Niu , G., & Liu, Y. (2025). ARCS: Adaptive Reinforcement Learning Framework for
Automated Cybersecurity Incident Response Strategy Optimization. Applied Sciences, 15(2), 951.
[67] Pons, S., Huertas‐Garcia, R., Lengler, J., & de Mattos Nascimento, D. L. (2025). Natu ral Language
Processing Algorithms to Improve Digital Marketing Data Quality and Its Ethical Implications.
Psychology & Marketing.
[68] Tu, D., He, Y., Cui, W., Ge, S., Zhang, H., Han, S., ... & Chaudhuri, S. (2023, August). Auto -validate by-
history: auto -program data quality constraints to validate recurring data pipelines. In
Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (pp.
4991-5003).
[69] Moradi, M. (2021). Importance of internet of things (IoT) in marketing research and i ts ethical
and data privacy challenges. Business Ethics and Leadership, 5(1), 22-30.
[70] Petrescu, M., & Krishen, A. S. (2021). Focusing on the quality and performance implications of
marketing analytics. Journal of Marketing Analytics, 9(3), 155-156.
[71] Suri, N. (2021). Book review: Thomas H. Davenport and Jeanne G. Harris, Competing on Analytics.
[72] Lozada, N., Arias-Pérez, J., & Henao-García, E. A. (2023). Unveiling the effects of big data analytics
capability on innovation capability through absorptive capacity: why more and better insights
matter. Journal of Enterprise Information Management, 36(2), 680-701.
[73] Sawang, S., & Kivits, R. A. (2024). Revolutionizing family businesses with artificial intelligence: a
perspective article. Journal of Family Business Management, 14(4), 802-807.
[74] van de Wetering, R., Mikalef, P., & Krogstie, J. (2019, July). Strategic value creation through big
data analytics capabilities: a configurational approach. In 2019 IEEE 21st Conference on Business
Informatics (CBI) (Vol. 1, pp. 268-275). IEEE.
[75] Mollestad, M. E. (2023). Mitigating Hidden Technical Debt in Machine Learning Systems (Master's
thesis, NTNU).
[76] de Bie, K., Lucic, A., & Haned, H. (2021). To trust or not to trust a regressor: Estimating and
explaining trustworthiness of regression predictions. arXiv preprint arXiv:2104.06982.
[77] Liu, J., Wang, J., & Lin, H. (2025). Coordinated Physics -Informed Multi -Agent Reinforcement
Learning for Risk-Aware Supply Chain Optimization. IEEE Access, 13, 190980-190993.

Frontiers in Business and Finance Volume 2 Issue 2, 2025
ISSN: 3079-9325

398
[78] Bozich, M. L. (2025). The Efficac y of Television Advertising Instrumenting Advertising in Product
Level Regressions (Doctoral dissertation, University of Minnesota).
[79] Kim, D., & Pal, P. (2025). Nonparametric estimation of sponsored search auctions and impact of
Ad quality on search revenue. Management Science.
[80] Brynjolfsson, E., & McElheran, K. (2019). Data in action: data -driven decision making and
predictive analytics in US manufacturing. Rotman School of Management Working Paper,
(3422397).
[81] Dennehy, D., Griva, A., Pouloudi, N., Dwivedi, Y. K., Mäntymäki, M., & Pappas, I. O. (2023). Artificial
intelligence (AI) and information systems: perspectives to responsible AI. Information Systems
Frontiers, 25(1), 1-7.
[82] Guo, F., Li, Y., Maruping, L. M., & Masli, A. (2023). Complementarity between inve stment in
information technology (IT) and IT human resources: implications for different types of firm
innovation. Information Systems Research, 34(3), 1259-1275.
[83] Lu, J., Cairns, L., & Smith, L. (2021). Data science in the business environment: customer an alytics
case studies in SMEs. Journal of Modelling in Management, 16(2), 689-713.
[84] Filho, C. P., Marques Jr, E., Chang, V., Dos Santos, L., Bernardini, F., Pires, P. F., ... & Delicato, F. C.
(2022). A systematic literature review on distributed machine lea rning in edge computing.
Sensors, 22(7), 2665.
