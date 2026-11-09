---
title: DATA-DRIVEN ATTRIBUTION MODELING IN DIGITAL MARKETING
url: https://doi.org/10.17721/1728-2667.2026/228-1/20
category: analytics
subcategory: measurement
date: 2026-01
venue: Bulletin of Taras Shevchenko National University of Kyiv. Economics
authors:
- Galyna Chornous
- Mariana Petrova
- Maryna HORNA
source: openalex-oa
pdf_url: https://econom.bulletin.knu.ua/article/download/3994/8045
pages: 11
chars: 63650
fetched_at: '2026-11-08T17:01:39+00:00'
kb_version: 1
---

# DATA-DRIVEN ATTRIBUTION MODELING IN DIGITAL MARKETING

ЕКОНОМІКА. 1(228)/2026 ~ 191 ~

ISSN 1728-2667 (Print), ISSN 2079-908X (Online)
UDC 004.738.5:339.138
JEL classification: C63, D83, M31, L86
DOI: https://doi.org/10.17721/1728-2667.2026/228-1/20

Galyna CHORNOUS1, DSc (Econ.), Prof.
ORCID ID: 0000-0003-4889-1247
e-mail: galyna.chornous@knu.ua

Mariana PETROVA2, DSc (Phys. & Math.), Prof.
ORCID ID: 0000-0003-1531-4312
e-mail: m.petrova@ts.uni-vt.bg

Maryna HORNA1, PhD (Econ.), Assoc. Prof.
ORCID ID: 0000-0002-6011-5753
e-mail: maryna.horna@knu.ua

Nikolay PENEV3, PhD (Econ.), Assoc. Prof.
ORCID ID: 0009-0003-7359-8357
e-mail: nikolay.penev@trakia-uni.bg

Maiia PUSTOVIT1, Bachelor
ORCID ID: 0009-0001-0472-9662
e-mail: maya.pustovit2004@knu.ua

1Taras Shevchenko National University of Kyiv, Kyiv, Ukraine
2St. Cyril and St. Methodius University of Veliko Tarnovo, Bulgaria
3Trakia University, Stara Zagora, Bulgaria

DATA-DRIVEN ATTRIBUTION MODELING IN DIGITAL MARKETING

Background.  In the contemporary digital environment, marketing communications have evolved into multi-channel,
personalized, and dynamic interactions, necessitating an increasingly precise quantification of the efficacy of each user touchpoint
with a brand. Conventional rule-based marketing attribution models, which exclusively assign value to a singular touch-point of
contact, no longer yield the requisite level of analytical granularity. In response to these methodological challenges, advance d
economic and mathematical methodologies, notably models predicated on Markov chains and Shapley values, are progressively
being deployed to facilitate a rigorously reasoned and quantitatively justifiable allocation of value across all contributing channels.
Methods .  The research methodology is based on a combination of general scientific and specialized methods. Specifically,
it utilized theoretical modeling, comparative analysis, as well as stochastic modeling (Markov chains) and cooperative game theory
(Shapley values).
Results.  This research rigorously investigated marketing attribution in the digital environment, demonstrating the inherent
limitations of traditional rule-based models and substantiating the superior efficacy of adaptive approaches, particularly Mark ov
chains and Shapley values. The empirical implementation and comparative analysis of the Shapley value model confirmed its
enhanced precision and capacity to objectively quantify each channel's contribution, leading to actionable insights for strateg ic
marketing optimization. This study provides a robust framework for understanding multi-touch attribution, emphasizing the critical
role of data-driven methodologies in contemporary marketing analytics.
Conclusions.  The work is relevant for marketing analysts and digital strategy teams, as it presents a comparative
analysis of rule-based and algorithmic attribution models and offers practical solutions for campaign optimization. The Shapley
Value model was implemented in Python and tested on real-world marketing data. The practical value lies in the ability to use t he
results for better budget allocation, identifying undervalued channels, and increasing return on marketing investment (ROMI).

Keywords:  marketing attribution, digital marketing, data-driven at tribution, Shapley values, Markov chains, multichannel
analytics, Python.

Background
In the contemporary digital landscape, marketing
communications have evolved to become multichannel,
personalized, and dynamic, thereby intensifying the need for
precise measurement of the effectiveness of each user
interaction with a brand. In this context, marketing attribution
emerges as a response to the growing demand for
understanding the actual cont ribution of each channel to
business outcomes. The primary objective of marketing
attribution is to assist brands in discerning the significance
of every touchpoint within the broader customer journey. By
identifying which channels or touchpoints yield higher
conversion rates, marketing teams can optimize budget
allocation and communication strategies. Such insights
enable marketers to clearly recognize the sequences of user
actions that most frequently lead to desired behaviors and,
ultimately, to conversions. Moreover, marketing attribution
enhances the customer experi ence by facilitating a deeper
understanding of the customer journey, highlighting pivotal
touchpoints, and identifying areas for improvement.
As a technical process, mark eting attribution entails the
systematic collection, proce ssing, and analysis of user
interaction data. The data co llection stage is implemented
through core tracking technologies such as cookies, tracking
pixels, UTM tags, and other mechanisms that enable the
identification of traffic sources and user behavior on
websites. These data, in turn, form the foundational basis for
constructing effective attribution models.
Traditional rule-based marketing attribution models,
which attribute the entirety of value to a singular touchpoint,
no longer provide a sufficient level of analytical precision. In
response to these limitations , attention is increasingly
gravitating towards the adopti on of data-driven attribution
models. While the market currently furnishes a diverse array
of tools enabling the application of classification algorithms,
Bayesian analysis, and other techniques for marketing
attribution, substantial potent ial remains for advancing this
class of models through more sophisticated mathematical
approaches. Specifically, stochastic modeling and game
theory present compelling avenues for development. In
© Chornous Galyna, Petrova Mariana, Horna Maryna, Penev Nikolay, 2026

~192 ~ ВІСНИК  Київського національного університету імені Тараса Шевченка

ISSN 1728-3817
particular, Markov chain models and Shapley value-based
approaches enable a rational and quantitatively verifiable
allocation of value across all digital marketing channels. The
adoption of such models thus presents novel opportunities
for developing evidence-based frameworks for marketing
resource allocation and for the strategic governance of
communication channels. Consequently, research into
marketing attribution models retains substantial relevance.
This imperative is driven, on the one hand, by the exigencies
arising from the escalating complexity of the modern digital
landscape, alongside heightened demands for
computational precision, a nalytical transparency, and
judicious budget management; and, on the other hand, by
the imperative for businesses to access practical tools for
resolving marketing attribution challenges.
The paper aims to propose an accessible, high-quality,
and effective data-driven tool for addressing marketing
attribution challenges within today's complex digital
multichannel environment. To achieve this objective, several
key tasks were undertaken: conducting a comparative
analysis of current marketing attribution models in terms of
their capabilities and limitations in practical digital marketing
applications; outlining the strong potential of data-driven
approaches – particularly stochastic and game-theoretic
models – for enhancing the accuracy of channel contribution
evaluation in a complex multichannel context; conceptualizing
the process of attribution modeling based on Shapley values
using Python libraries; and practically implementing the
proposed approach using real-world marketing campaign
data to develop actionable recommendations for improving
digital marketing performance.
The research findings demonstrate that rational and
effective marketing attribution models, along with accessible
tools, can be successfully adopted by companies of various
sizes and levels of IT infrastructure maturity. These tools can
contribute to improved marketing campaign performance,
more efficient advertising budget allocation, and better
decision-making based on more accurate analytical models.
Literature review.  Recent years have witnessed
substantial advancements in the field of digital marketing,
particularly in attribution modeling, which enables
companies to more effectively assess the impact of their
marketing efforts. Foundati onal studies, such as the
systematic review (Dhar, & Singh, 2020), underscore the
escalating complexity and paramount importance of
attribution modeling for comprehending customer pathways
to conversion, concurrently providing a comprehensive
overview of extant me thodologies and delineating
prospective research trajectories. Similarly, a review (Yusup
et al., 2024) centers on the pivotal role of artificial
intelligence within digital market ing, a factor critical to the
advancement of novel algorithmic attribution models.
Modern attribution approaches actively employ
advanced algorithmic techniques. The authors of such a
study (Lee et al., 2021) conduct a comparative analysis and
interpretation of models for predicting online conversions, an
integral component of assessing marketing touchpoint
efficacy. Karray, Martín-Herrán, and Sigué (2022) address
the management of adverti sing investments across
marketing channels, thereb y underscoring the critical
importance of multichannel a nalytics and strategic budget
allocation. Particular emphasis is placed on models capable
of accounting for the intricate interactions among
touchpoints. Dhar and Singh (2020) presented a
comprehensive literature review on attribution modeling in
marketing, offering a soli d theoretical foundation and
identifying key directions for future research. Furthermore,
other researchers (Zhao, Mahboobi, & Bagheri, 2022) delve
into game-theoretic models of marketing attribution,
enabling the equitable distribution of value among various
marketing channels based on their incremental contribution,
notably through the application of Shapley value theory.
Understanding user behavior and optimizing advertising
activities are central to effective digital marketing. A
simulation-based model is proposed to forecast the
dynamics of consumer behavior under digital advertising
influence and to support budget allocation decisions
(Dorokhova et al., 2023). Furthermore, contemporary
research actively utilizes data science for modeling. Some
studies (Chornous, & Fareniuk, 2021) apply data science
technologies to model the marketing mix in pharmaceutical
companies, demonstrating t he practical application of
algorithmic models for evaluating investment effectiveness.
Ben Mrad and Hnich introduce an intelligent attribution
modeling framework in this context (Ben Mrad, & Hnich,
2024) that leverages advanced analytics to optimize digital
marketing performance. Likewise, Seth and Ramakrishnan
present innovations in multi-touch attribution models tailored
to the pharmaceutical sector, moving beyond traditional
marketing analytics to capture the nuanced contributions of
diverse channels (Seth, & Ramakrishnan, 2025).
Recent literature demonstrates a significant evolution of
marketing mix modeling (MMM) and attribution analytics,
moving from classical brand-management frameworks
(Cain, 2014) toward data-driven, digitally oriented
methodologies. Studies on di gital strategy adaptation
(Dumitrescu et al., 2018) and foundational reviews of
attribution modeling (Gaur, & Bharti, 2020; Mathew, 2016)
highlight the increasing analytic al complexity of evaluating
channel effectiveness. Research further explores advanced
approaches for multi-channel attribution across competitors
(Li et al., 2017) and the shift toward inferential and post-
cookie attribution techniques (Kamena, 2021; Hosahally et
al., 2025). Modern MMM has pr ogressed from traditional
regression models to AI-powered and neural-network–based
architectures (Gujar et al., 2024; Mulc et al., 2025), while
applications in real business environments confirm their
practical suitability (Ravid, 2025; Sciarrino et al., 2025).
Additional studies emphasize model comparison (Sharma,
Meena, & Ibrahim, 2017),  omnichannel attribution challenges
(Méndez-Suárez, & Monfort, 2021), and the integration of
multi-information fusion to bridge MTA and MMM (Zhou, Pei,
& Li, 2024). Together, these works reflect a consolidated trend
toward more granular, algorithmic, and privacy-resilient
attribution models in contemporary digital marketing.
A review of contemporary literature reveals a growing
trend towards applying sophisticated algorithmic models
based on game theory, machin e learning, and stochastic
modeling (including Markov chains) for more precise
marketing attribution and invest ment optimization in digital
and multichannel marketing. These studies form the
foundation for more effective st rategies that consider the
dynamics of consumer behavior and the complexity of
interactions between marketing channels. This paper
conducts a comparative analysis of modern attribution
models and proposes and implements a model based on
Shapley values in a Python environment, which can be
beneficial for real-world businesses of various sizes and
IT infrastructure maturities.
Methods
The paper employs both general scientific and
specialized research methods. General scientific methods
include the dialectical method, systems approach, methods
of analysis and synthesis, and induction and deduction.

ЕКОНОМІКА. 1(228)/2026 ~ 193 ~

ISSN 1728-2667 (Print), ISSN 2079-908X (Online)
Within the framework of economic-mathematical modeling,
stochastic modeling (Markov chains) and elements of
cooperative game theory (specif ically, Shapley values) are
considered. The methodological toolkit of the study also
encompasses methods from probability theory, rule-based
modeling, data analysis and pr ocessing using the Python
programming environment (pandas, numpy, matplotlib
libraries), methods of comp arative analysis, and results
visualization. The application of these approaches ensured
a comprehensive analysis of the selected problematic area
and enhanced the reliability of the conclusions drawn.
The marketing attribution models examined in the study
are categorized into two main groups: deterministic (rule-
based models) and adaptive (algorithmic). The first group of
models includes Single-Touch Attribution Models,
specifically First Touch Attribution and Last Click Attribution,
as well as Multi-Touch Attribution Models such as Linear
Attribution, Time-Decay Attribution, Position-Based
Attribution, W-Shaped Attribut ion, and Custom Attribution
(Sun, 2023). Web analytics platforms, such as Google
Analytics, traditionally use a Single-Touch Attribution
approach by default for conducting attribution analysis.
Adaptive models study histor ical user data to identify
patterns in interactions with marketing channels. Among
these models, the most co mmon is the data-driven
attribution approach (Ben Mrad, & Hnich, 2024), which
involves using classification algorithms, Bayesian analysis,
or ensemble methods to distribute value among channels
based on their actual contribution to conversion. The group
of adaptive models also includes Markov chains, which are
probabilistic models explored in this study. Markov chains
enable the representation of user interaction sequences and
the calculation of transit ion probabilities between
touchpoints (Mehta, & Singhal , 2020). Markov chains are
characterized by a defined stat e space, a transition matrix
(describing probabilities between states), and an initial state
or distribution. The constructed graph represents interaction
points with existing transitions corresponding to specific
probabilities. Graph construction is based on historical user
interaction data. Conversion is modeled as a final state,
while abandonment (null) is an alternative terminal state. To
assess the significance of each channel, the "removal effect"
approach is applied. This involves analyzing how the
elimination of a specific node impacts the probability of
achieving conversion (e.g., purchase, other primary action).
Markov chains effectively account for not only the sequence
of touchpoints but also their interdependencies, including
the presence of cycles (loops ) that occur when a user
repeatedly interacts with the same channel. For more
complex graphs with numerous cycles, iterative
approximation methods are us ed to estimate conversion
probability, even with an infinite number of possible paths.
The Shapley value model implemented in this study
originates from game theory. The main problem addressed
by the Shapley value is the fair distribution of credit in a
game where players can form coalitions (Zhao, Mahboobi,
& Bagheri, 2022). In the contex t of marketing attribution,
game theory is utilized to model customer interactions with
marketing channels as a cooperative game, where each
marketing channel can be viewed as a player. The collective
of all players/channels works together to drive conversions
and assigns each touchpoint fair credit (using these Shapley
values) for a conversion based on its true contribution. The
calculation of Shapley values for each channel 𝑖 is
performed using the formula:
ϕ௜(𝑁, 𝑣) =
=
ଵ
|ே|! ∑ |𝑆|! (|𝑁| − |𝑆| − 1)!ௌ⊆ே∖{௜} ⋅ ሾ𝑣(𝑆∪ {𝑖}) −𝑣 (𝑆)ሿ,   (1)
where 𝑁 – the set of all channels (players); 𝑆⊆𝑁∖ {𝑖} – a
subset of channels not including channel 𝑖; 𝑣(𝑆) – the value
function (conversion rate) generated by the coalition 𝑆 ;
𝑣(𝑆∪ {𝑖}) −𝑣 (𝑆) – marginal contribution of channel 𝑖 to
coalition S; |𝑆|! (|𝑁| − |𝑆| − 1)!  – weighting factors
considering the number of permutations of channels before
and after the inclusion of channel 𝑖 .
For each channel, all coalitions to which it does not yet
belong are iterated over, and its marginal contribution to
each of them is evaluated. T he marginal contribution is
defined as the difference between the value of the coalition
after the inclusion of the given channel and its initial value:
contrib௜(𝑆) = 𝑣(𝑆∪ {𝑖}) −𝑣 (𝑆).                (2)
The contribution can be weig hted using a combinatorial
coefficient that accounts for the number of possible orders
in which the channel can enter the coalition:
weight௜(𝑆) =
|ௌ|!⋅(|ே|ି|ௌ|ିଵ)!
|ே|! .                    (3)
Thus, the Shapley model provides an objective and
mathematically justified as sessment of each channel's
contribution to conversion based on its marginal effect
across all possible channel coalitions.
Results
Model Comparison . The analysis of rule-based
attribution models has revealed their advantages but also
highlighted significant limitations, primarily in their ability to
accurately capture the complex nature of consumer
behavior. Table 1 presents a co mparative overview of the
main traditional marketing attribution models.

Table 1
Comparative Table of Main Rule-Based Marketing Attribution Models
Attribution model Value Distribution Optimal Use Case
First Touch All value is as signed to the first touchpoint Measuring the effectiveness of initial brand awareness
Last Touch All value is assigned to the last touchpoint Determining t he final influence on decision-making
Linear Value is evenly distributed across all touchpoint s When all touchpoints are considered equally important
in the conversion process
Time-decay More value is given to recent interactions, less to
earlier ones
For longer sales cycles or when recent interactions have
a stronger impact on conversion
Position-based Value is distri buted among different touchpoints
(depending on the model or platform)
When both the first and last interactions are important
Custom Value is assigned according to what is most
important for the business
Best suited for companies with specific goals or unique
customer journeys
Source: compiled by the authors.

Against the backdrop of the limitations of traditional
models, adaptive approaches are gaining increasing
importance. These approaches account for temporal
dynamics, the sequence of touchpoints, and their statistical
significance in driving conversion.
Markov chains effectively model the interrelationships
between marketing channels, considering the sequence of
actions, repeated interactions  (cycles), and context in
higher-order models. They are particularly useful for
analyzing complex and long conversion paths where

~194 ~ ВІСНИК  Київського національного університету імені Тараса Шевченка

ISSN 1728-3817
traditional attribution models are insufficient. The application
of the "removal effect" metric allows for the identification of
channels with a critical impact on conversion, while
robustness to noise and flexibility ensure the model's
scalability. Nevertheless, the model has several limitations:
it is based on correlations rather than causal relationships,
which may lead to erroneous attribution of results to
channels. Additionally, the classical "memoryless" approach
does not always accurately reflect user behavior in complex
scenarios. Model implementation requires a significant
volume of data, access to complete user paths (including
non-converting ones), and the use of specialized
computational tools. Despit e these challenges, Markov
chains remain a powerful tool for evaluating channel
effectiveness, provided a critical approach is taken to
modeling and interpreting results.
The Shapley value model is widely used in the analytical
systems of major advertising platforms to quantitatively
assess the contribution of marketing channels to
conversions by analyzing all possible channel coalitions.
Due to the exponential growth in the number of
combinations, its practical implementation requires
substantial computational res ources. To enable scalability
for large datasets, approximation techniques and SHAP
(SHapley Additive exPlanations) tools are commonly
employed. The key advantages of the model include a fair
and proportional allocation of channel influence that
accounts for channel interactions, enhancing both
interpretability and predictive accuracy compared to
traditional approaches. At the same time, the model is
constrained by high computational complexity, sensitivity to
data variation, the need for la rge volumes of detailed data,
and the inability to account for the sequence of interactions.
These limitations highlight the need for further development
of extended versions and efficient algorithmic solutions.
Table 2 presents a comparative analysis of the main
characteristics of Markov chain-based and Shapley value-
based attribution models.

Table 2
Comparative Analysis of Markov Chain-Based and Shapley Value-Based Attribution Models
Comparison feature Markov chain-Based Model Shapley value-Based Model
Model Type Probabilistic, sequent ial Game-theoretic, cooperative
Analysis of Channel Order Context Takes the transit ion order into account Order is not critical
Dependence on Temporal Structure High Minimal
Consideration of Channel Interactions Limited, based on transitions Compre hensive, considers all coalitions
Robustness to Sample Size Variation High with large samples Depends on computational resources
Computational Complexity Moderate High (exponential growth)
Flexibility to Adapt to Complex Scenarios Limited by the first-order model High due to the coalition-based approach
Interpretability of Results High, but requires an explanation of the
transition probability matrix
High, especially with SHAP visualizations
Dependence on Specification of Payoff
Function (Business Goals)
Does not require an explicit definition Requires a characteristic function
Relevance in Modern Tools Common in web analytics Integrated in modern ML platforms
Source: compiled by the authors.

The comparative analysis indicates that the Markov chain
model is effective for accounting for the order of actions and is
less resource-intensive, whereas the Shapley value model
provides a more precise evaluation of each channel's
contribution but requires substantial computational resources.
Therefore, the choice between the two depends on the
complexity of user paths, analytical objectives, and available
resources. Both models have practical applications; however,
in scenarios involving complex funnels and a high demand for
attribution accuracy, the Shapley value model should be
preferred. The following conceptual steps are proposed for its
implementation in Python.
Conceptualization. The first stage involves performing
preliminary data analysis. Using the Python libraries
pandas, numpy, and matplotlib, the dataset is loaded and its
structure is initially explored (including general data
overview and exploratory data analysis – EDA), missing
values and anomalies are identified, key variables are
determined, and preliminary vis ualizations of interactions
between variables are created (libraries matplotlib, seaborn,
and plotly.express).
Next, data preparation for m odeling is conducted. This
stage includes aggregating data to the user level by
constructing ordered sequences of channels (user
journeys), which enables the representation of individual
interaction paths with the campaign. For each user, a set of
channels interacted with is form ed, along with a record of
whether a conversion occurred.  A coalition table is created
containing unique channel combinations and the
corresponding number of conversions, providing a basis for
subsequent calculations.
The following step is building the attribution model based
on Shapley values. The methodology involves generating
the full set of possible channel coalitions, calculating the
marginal contribution of each channel across all possible
combinations, and normalizing the results to obtain relative
influence shares. The resulting values are visualized using
Python's graphical tools to enhance interpretability and
facilitate comparison of individual channel contributions.
To improve the robustness of the analysis, it is advisable to
additionally implement rule-based marketing attribution
models, such as Linear Attribution and Last Touch Attribution.
This allows for the comparison of the adaptive approach results
with traditional methods, identification of key discrepancies in
channel contribution assessments, and evaluation of model
quality through benchmarking against baseline methods. To
implement the previous three steps, in addition to the
aforementioned Python libraries (such as NumPy and pandas),
the study also employed Seaborn and Plotly Express libraries
for data visualization, as well as the built-in Python modules
itertools.combinations for working with iterators and
collections.defaultdict for enhanced data structures.
The next stage involves a co mparative analysis of the
obtained results, during which the effectiveness of channels
across different attribution models is evaluated. This
analysis enables the identific ation of key channels that
demonstrate consistent influence across various
approaches, as well as the det ection of channels whose

ЕКОНОМІКА. 1(228)/2026 ~ 195 ~

ISSN 1728-2667 (Print), ISSN 2079-908X (Online)
contribution significantly increases only within the context of
multichannel interactions.
The final stage consists of formulating conclusions and
practical recommendations for optimizing marketing
budgets, enhancing channel effectiveness, and designing
multichannel campaigns based on attribution results. These
insights empower companies to make informed and rational
strategic decisions grounded in data.
Experiment. To develop the Shapley value–based
attribution model, a real dataset from a digital advertising
campaign was utilized, comprising 10,037 records of user
interactions with various marketing channels throughout
January 2018. The campaign promoted a digital product
offering online educational services. The key variables
selected for modeling include user_id (a unique identifier
distinguishing individual users within the dataset),
marketing_channel (indicating the channel through which
the marketing message was delivered: Email, Facebook,
Instagram, Push, House Ads) , date_served (the date the
marketing message was shown, necessary for determining
the order of touchpoints in the user journey), and converted
(a binary variable: True if the user completed a conversion
such as a purchase or subscription following the interaction,
False otherwise. This is the primary target variable for
attribution modeling as it defines interaction success. These
variables contain a minimal amount of missing data (up to
0.2%) and allow tracking of individual user paths to
conversion. Other subscription-related variables were
excluded due to their irrelevance to the attribution analysis.
Missing values in critical variables were handled by row
deletion without compromising data quality. Exploratory data
analysis focused on deriving insights, verifying data
distributions, and preparing for modeling, with particular
attention to the conversion rate, frequency of channel
usage, and channel combinations leading to conversions.
The analysis revealed a moderate class imbalance, with
successful conversions (converted = True) constituting
approximately 60% of observations and unsuccessful ones
(converted = False) about 40%, which is favorable for model
training without additional adjustment. Regarding channel
usage, House Ads emerged as  the most engaged channel
with over 250 impressions, followed by Instagram and
Facebook (~105 impressions each), indicating an uneven
distribution of marketing efforts. The relationship between
impression frequency and number of conversions showed a
direct linear correlation: House Ads led both in impressions
and conversions, whereas Instagram and Facebook
exhibited high conversion rates despite fewer impressions.
Email and Push had limited impressions and
correspondingly fewer successful interactions. These
findings confirm that an increase in interaction volume
directly correlates with a rise in the absolute number of
conversions (Fig. 1).

Fig. 1. Relationship Between the Number of Impressions and Conversions
Source: Compiled by the authors using Python environment

Continuing the analysis of channel effectiveness, the
next stage focused on examining the interrelationships
among marketing channels t hat appear together within a
single user's journey. Frequency of impressions and
conversion rates – even when combined with conversion
share metrics – do not fully capture the multichannel nature
of digital campaigns. It is therefore essential to identify which
channels most frequently co-occur in user interactions. A
channel co-occurrence matrix constructed in the Python
environment (see Fig. 2) rev ealed that House Ads is the
most integrated channel, frequently appearing alongside
Instagram (70 cases), Facebook (43), and Push (20),
emphasizing its central role in the campaign. Instagram also
frequently co-occurs with Facebook (29), forming a stable
interaction cluster. In contrast, Email and Push are less
commonly found in combinations, typically appearing in
isolated or supplementary scenarios.

~196 ~ ВІСНИК  Київського національного університету імені Тараса Шевченка

ISSN 1728-3817

Fig. 2. Heatmap of Channel Co-Occurrence Frequency per User
Source: Compiled by the authors using Python environment

The data indicate a moderate class imbalance, with
approximately 60% of interacti ons resulting in conversions.
House Ads clearly dominate in both the number of
impressions and conversions, followed by Instagram and
Facebook in intermediate positions. Although Email
demonstrated a lower reach, it  exhibited a high conversion
rate when applied in a targeted manner. The analysis of
channel combinations confirms  the central role of House
Ads and the strong interconnection between Instagram and
Facebook, which constitutes an important business insight
for evaluating the results of attribution models.
In the next stage of the st udy, a Shapley value–based
marketing attribution model was constructed to determine
the marginal contribution of each marketing channel to
conversions, taking into account all possible combinations
of its occurrence in user paths. Before calculating the
Shapley values, the data were aggregated at the user level:
for each user_id, the unique marketing_channel values that
appeared in the sequence of impressions were
concatenated. The uniqueness function ensured that each
channel in a user journey wa s considered only once, but
preserved the order of appearance. The result was a string
such as 'Email, Push, Facebook', representing the user's
journey. Each user was also assigned a binary label
indicating whether their path ended in a conversion.
The following step involved grouping users by unique
channel combinations, reflecting all observed channel
coalitions in actual journeys.  For each such coalition, the
number of conversions completed by users who followed
that specific path was calculated. As a result, an aggregated
coalition combination was c onstructed, with each entry
representing a specific channe l combination along with the
corresponding number of successful conversions (Fig. 3).

Fig. 3. Main Channel Combinations by Conversions
Source: Compiled by the authors using Python environment

ЕКОНОМІКА. 1(228)/2026 ~ 197 ~

ISSN 1728-2667 (Print), ISSN 2079-908X (Online)
To proceed with the calculation of Shapley values, a
complete set of potential chan nel coalitions that could
theoretically arise within user  interactions was generated.
This involved creating all poss ible non-empty subsets from
the available list of channels, including individual channels,
pairs, triplets, and so forth. These subsets are treated as
coalitions, with each possessing a potential "value", i.e., the
number of conversions associated with that specific channel
combination (Cooper, 2022). For this stage, a function was
implemented that, given a list of channels, generates all
possible combinations (subsets) of length from 1 to n, where n
is the number of unique ch annels in the dataset. These
combinations represent all configurations in which the channels
may jointly appear. An auxiliary function converts each subset
into a sorted string format (e.g., 'Email, Facebook'), ensuring
consistent storage of values in subsequent dictionaries. This
process produced the analytical space of all possible coalitions,
forming the foundation for computing the marginal contribution
of each channel.
The next stage involved defining the value function v(S),
which calculates the overall "value" or effectiveness of a
given coalition – its conversion  strength. For each coalition
(e.g., ['Email', 'Facebook']), the function searches for all its
subsets (such as ['Email'], ['Facebook'], and ['Email,
Facebook']) and sums their corresponding values from the
conversion_dict.
𝑣(𝑆) = ∑ conversion(𝑇)்⊆ௌ ,                   (4)
where 𝑆 denotes a coalition of channels, and 𝑇 refers to a
subset of 𝑆 that is present in the conversion dictionary.
For example: v(['Email', 'Push']) = conversion('Email') +
conversion('Push') + conversion('Email, Push').
Next, the Shapley values for each channel 𝑖 were
calculated using the classical formula (1).
The calculation was implemented as a separate function
that received as input an aggregated Data Frame containing
channel combinations and the corresponding number of
conversions for each. From this Data Frame, a dictionary was
created where the keys were strings representing the channel
combinations (e.g., "Email, Push"), and the values represented
the number of conversions attributed to each coalition. This
structure enabled efficient access to the necessary values
during computation. Subsequently, all channels that appeared
in solo combinations – i.e., in user paths where only one
channel was encountered – were  identified. The next step
involved calculating the coalition value function, as previously
defined, for all possible subsets of channels. For example, if a
coalition consisted of three channels, its value was computed
as the sum of conversions for all single, pairwise, and triple
combinations present in the dataset. For each channel, all
coalitions in which it was not initially present were iterated over,
and its marginal contribution to each was evaluated (using
formulas (2) – (3)).
As a result, each channel received a Shapley value,
interpreted as its average marginal contribution to achieving a
conversion, taking into account all possible coalitions and
interaction sequences. The highest Shapley value was
observed for the House Ads channel, with a contribution of
137.33, indicating its critical role in the user's path to the target
action. This result confirms not only its high frequency of use
but also its significance in combinations with other channels –
House Ads consistently delivers the highest incremental value
to the coalitions it is part of. Facebook ranked second in terms
of influence, with a Shapley value of 51.83, reflecting the
channel's stable effect both in solo and multi-channel pathways.
Email and Instagram demonstrated similar levels of influence –
36.33 and 31.50, respectively – indicating moderate yet
systematic involvement in conversion chains. The lowest
contribution was observed for Push (15.00), which correlates
with its less frequent usage and limited marginal effect in the
context of interactions with other channels.
To evaluate the results, normalization of the values was
performed by converting the abs olute contributions of the
channels into relative shares (Table 3). This process
involved dividing each channel's contribution by the total
sum of contributions, thus det ermining its share of the
overall conversion impact. House Ads accounts for 50% of
the total influence. While functi onally effective, this also
indicates a potential dependence of the overall conversion
strategy on this internal ch annel. Such a concentration
poses a risk of overreliance but simultaneously presents an
opportunity to scale this successful pattern to external or
emerging channels. Facebook, with a share of 19.06%, may
serve as a connecting touchpoint between user interactions
across different channels. This signals the potential for
further investment in Facebook as a channel with growth
capacity through enhanced engagement. Email and
Instagram exhibit relatively similar performance – 13.36%
and 11.58%, respectively – demonstrating consistent,
though moderate, contributions to conversion. Push
notifications represent only 5.51%  of the total. Despite the
low share, this communication channel holds potential for
targeted impact, particularly in reactivating dormant users or
executing time-sensitive promotional campaigns.

Table 3
Normalized percentage contributions of channels to conversion according to three attribution models, %
Marketing Channel Attribution Model Shapley Values Attribution Linear Attribution Last Touch Attribution
House Ads 50.49 47.86 60.23  
Facebook 19.06   18.08   14.62  
Email 13.36   10.62   8.48  
Instagram 11.58   16.81   10.82  
Push 5.51   6.63   5.85  
Source: compiled by the authors.

To evaluate the effectiveness of the developed model
and validate the accuracy of the calculated contributions, its
results were compared with classical rule-based attribution
models, which constituted t he next step of the study.
Specifically, the logic of the Linear Attribution model was
implemented, in which the contribution to conversion is
evenly distributed among all c hannels present in the user's
journey. This model does not account for the order of
influence but only for the presence of a channel. Each
channel involved in the path to conversion receives an equal
share of the attribution. After normalizing the contribution of
each channel, the highest percentage contribution, similar to
the Shapley Values model, was assigned to the House Ads
channel (47.86%). Facebook ranked second (18.08%),
followed by Instagram (16.81%), while Email accounted for
10.62%. The smallest share was assigned to Push

~198 ~ ВІСНИК  Київського національного університету імені Тараса Шевченка

ISSN 1728-3817
notifications (6.63%). Additionally, a Touchpoints table
(Table 4) was created to determine the specific stage in the
user journey at which each channel had the greatest impact.
For instance, in the sequence Email → Facebook → House
Ads, Email corresponds to Touchpoint 1, Facebook to
Touchpoint 2, and House Ads to Touchpoint 3. The
maximum number of touchpoints in the dataset is three.

Table 4
Distribution of Channel Contribution by Touchpoints (Linear Attribution)
Channel Touchpoint 1 (%) Touchpoint 2 (%) Touchpoint 3 (%) Total (%)
House Ads 44.07 61.44 100.0 47.86
Facebook 18.68 16.49 0.0 18.08
Instagram 17.90 13.03 0.0 16.81
Email 13.18 0.00 0.0 10.62
Push 6.17 09.04 0.0 6.63
Source: compiled by the authors.

The analytical results indicate that the House Ads channel
demonstrates dominance across all stages of the user
journey, including the final touchpoint. Facebook and
Instagram primarily appear at the initial and intermediate
stages (1st–2nd touchpoints), thus serving as acquisition or
supporting channels. Consequently, their contribution to the
final conversion may be underestimated by traditional
attribution models, such as the Last Touch approach. Email
frequently functions as the initial point of contact that initiates
user engagement (e.g., via newsletters) and, in certain
instances, may independently lead to conversion within a
single-step purchase path. Push notifications act as
supplementary communication tools, predominantly occurring
within the first two touchpoints. They typically function as
reminders activated through mobile applications and have a
relatively limited impact on conversion outcomes.
The Last Touch Attribution model evaluates the impact
of channels based on their role  in concluding the user
journey before conversion, disregarding previous
interactions. It is suitable for scenarios where the final
contact is considered decisiv e. According to the analysis
conducted in Python, the le ading channel is House Ads,
accounting for 60.23% of conversions as the last touchpoint
due to its dominance at the se cond and third touchpoints.
This channel frequently serves as the final element in the
communication chain, effectively "closing" the deal.
Facebook (14.62%), Instagram (10.82%), and Email
(8.48%) play less significant roles. Notably, Email appears
exclusively at the first touc hpoint and is absent from the
second, meaning that under the Last Touch model,
conversions associated with Email are attributed only when
it serves as the initiating contact.
Within the framework of a comparative analysis of three
attribution models – Shapley Values, Linear Attribution, and
Last Touch Attribution – certain differences in the distribution
of marketing channel contribu tions were identified. These
findings allow for a series of conclusions regarding user
behavior, the effectiveness of  marketing efforts, and the
characteristics of each model. The results of the channel
contribution comparison are presented in Table 3.
First, the Last Touch Attribution model places maximum
emphasis on the final point of contact, assigning the entire
value of the conversion to the last channel in the user's
journey. This leads to an overestimation of channels that
frequently conclude interactions, particularly House Ads,
which receive the highest shar e (60.23%). However, this
model neglects prior stages of the user journey. Second, the
Linear Attribution model distributes value evenly across all
channels in the conversion path, reducing the weight of the
final touchpoint and increasing the contribution of channels
that consistently appear in mu lti-touch sequences, such as
Instagram and Email. These channels demonstrate higher
contributions compared to the Last Touch model, as their
supporting role in a multichannel context is recognized.
Third, the Shapley Values model offers the most structured
and mathematically grounded assessment by allocating the
value of each channel according to its marginal contribution
across all possible channel coalitions. This approach
identifies channels whose effectiveness increases through
interaction with others (e.g., Email, with a share of 13.36%
under Shapley versus 8.48% under Last Touch), eliminates
the "last-touch bias," provides a more realistic estimate of
the weight of House Ads (50.49%), and consistently
excludes low-impact channels such as Push, which
maintains a minimal contribution across all models.
Thus, the differences in evaluation are determined by the
conceptual assumptions of each model regarding the causal
relationships between channels and conversion: Last Touch
simplifies them to the final interaction; Linear distributes
value evenly without considering context; Shapley assesses
the actual impact, accounting for the sequence and
interaction of channels. This is why Shapley Values is
considered more appropriate for optimizing marketing
budgets in complex multichannel environments.
Based on the implemented model, marketers gain
valuable insights into the effectiveness of their marketing
efforts and budget planning. Regarding the strongest
conversion driver – House Ad s (50.49%) – the following
recommendations are appropriate: continue investing in
internal advertising (in-app ads, banners, recommendation
blocks within the interface); further unlock the channel's
potential through enhanced personalization (e.g., adapting
creatives based on past user in teractions); use House Ads
as a retargeting tool for users who have previously
interacted with other channels (e.g., Email or Instagram);
develop behavior-based scenarios (e.g., "House Ads only
after email open").
Facebook (19.06%) – an effective support and engagement
channel. It plays a role in both the upper and middle stages of
the funnel, generating initial interest and maintaining the
momentum of user transitions. Its contribution in coalitions is
significant, especially in combination with House Ads.
Recommendations for channel optimization: launch ad
campaigns with detailed audience targeting (Lookalike
Audiences based on conversion behavior); use Facebook as a
"reminder" channel, especially in interaction sequences where
it is not the first touchpoint; test video formats and interactive
posts to increase engagement depth before the appearance of
House Ads.
Email (13.36%) – a stable channel, yet requires
systematic expansion of inte ractions. It does not function
independently as a final trigge r, but significantly amplifies
the effect of combinations. Th e contribution in the Shapley
model is higher than in Last T ouch. Further integration of

ЕКОНОМІКА. 1(228)/2026 ~ 199 ~

ISSN 1728-2667 (Print), ISSN 2079-908X (Online)
email marketing at the final st ages of the user journey is
needed. As a core CRM tool, Email should re-engage users
who did not convert at earlier stages. Recommended
actions: identify audience segments with a high likelihood of
email response (e.g., based on Retention data); apply
trigger-based campaigns such as abandoned cart, re-
engagement, and onboarding; conduct A/B tests on subject
lines, send times, and CTA formats (call-to-action).
Instagram (11.58%) received higher scores in traditional
models but lower scores in the Shapley model. The nature
of this channel points to high visibility but a relatively weak
marginal effect, indicating a limited impact on final decision-
making and its appearance alongside more influential
channels. It primarily builds emotional connection and
enhances user engagement. Practical recommendations:
use Instagram mainly at t he early stages of the funnel
(awareness), with creatives t hat build brand perception;
integrate it with House Ad s or Facebook to support
multichannel communication; run campaigns linking to a
landing page (LP) rather than just the brand profile to
increase the likelihood of final conversion.
Push notifications (5.51%) – a low-impact channel in need
of relaunch. It shows the smallest contribution across all
models. Its influence is insufficient and poorly structured. As the
channel with the fewest impressions, it requires traffic growth
for proper testing and assessment of its effectiveness. There's
a rationale to revise the tactic or audience targeting.
Recommendations for optimization: shift to more personalized
push notifications (e.g., referencing prior user actions); limit
frequency and apply A/B testing – whether to send push before
or after email or other channels; measure open time and its
influence on re-engagement.
Therefore, by leveraging the flexibility and precision of
the Shapley model, a company can effectively assess the
marginal effect of each touchpoint. This approach will
mitigate dependence on traditional models, which
consistently overvalue the fina l stages of user interaction
with channels. Concurrently, it will facilitate a more efficient
allocation of the marketing budget, as channels with
negligible impact will no longer receive disproportionate
funding. Basing decisions on the actual impact of channels,
rather than merely their frequency or reach, will enable more
precise planning of multichannel campaigns. Ultimately, this
will empower the company to formulate a truly coherent
marketing strategy, wherein each channel functions as part
of a synchronized system geared towards effective user
engagement.
Discussion and conclusions
The study addresses the problem of marketing
attribution in the modern di gital environment and proposes
effective approaches for modeling channel impact using
both traditional and adaptive methods. The theoretical
foundations of marketing attribution are summarized, and a
comparative analysis of its principal models is presented. It
is established that traditional  rule-based models (such as
First/Last Click, Linear, and U-shaped), while popular due to
their simplicity, present signific ant limitations in the context
of complex multichannel interactions. These models fail to
consider the sequence, context, and interdependencies
between touchpoints, resulting in a distorted understanding
of the actual contribution of channels. Particular attention is
given to Markov chains as a stochastic method for assessing
channel impact, as well as to the Shapley value model
derived from cooperative ga me theory. Both approaches
demonstrate a stronger capac ity to account for channel
interactions, user journey context, and multichannel effects
– substantially outperforming rule-based models in digital
marketing settings. The Shapley Values Attribution model
was implemented in a Python environment using real-world
data. This allowed for the rec onstruction of detailed user
journeys, the formation of channel coalitions, the calculation
of the marginal contribution of each channel across all
possible combinations, and the vi sualization of the results.
As a result, the analysis identified the channels with the
greatest marginal effect in driving conversions while
avoiding the overvaluation of channels with high interaction
frequency but minimal actual impact.
It is important to acknow ledge that the findings
presented in this study are derived from a single dataset;
comparable approaches have been employed by other
explorers (Mehta & Singhal, 2020; Ben Mrad & Hnich, 2024),
who similarly conducted analyses on limited samples. To
strengthen the external validity and generalizability of these
results, future research should consider applying the
proposed methodology to diverse datasets encompassing
varying product verticals, temporal frameworks, and channel
configurations. Such extens ions would facilitate the
evaluation of the model's robustness across different
contexts and enhance confidence in the applicability of the
conclusions drawn.
Notwithstanding the model's pot ential precision, critical
questions remain concerning the practical interpretability of
Shapley value–based attribution outcomes, particularly
when juxtaposed with simpler, more conventional models
favored by practitioners. A dditionally, the feasibility of
implementing this approach in small enterprises with
constrained computational re sources, alongside its
limitations under conditions of  fluctuating user behavior,
warrants further investigat ion. Moreover, systematic
comparisons with other publicly  available empirical studies
are recommended to enable a more comprehensive
understanding of the influenc e exerted by individual
marketing channels.
A comparative analysis of the results from rule-based
models (Last Click, Linear Attr ibution) and the algorithmic
Shapley-based approach confirmed that rule-based models
tend to overly concentrate or  oversimplify influence. In
contrast, the Shapley model enabled an objective evaluation
of channel contributions ac ross different combinations,
confirming its superior accura cy, flexibility, and predictive
power in marketing analytics.
Based on the results, a meaningful interpretation of channel
contributions was proposed. The roles of individual channels
within the user journey were identified, key channels at different
stages of the funnel were determined, and budget optimization
opportunities were revealed. The findings not only confirmed
the advantages of adaptive at tribution models but also
illustrated how accurate analytics can become a strategic asset
in a world where every customer interaction matters. Future
research will aim to expand the analysis by incorporating
additional factors such as the temporal dynamics of
interactions, acquisition costs across different channels, and
user segmentation by behavioral and demographic
characteristics. This will facilitate the development of more
sophisticated and flexible attribution models that consider not
only the contribution of channels to conversions, but also their
effectiveness over time, across audience segments, and within
budgetary constraints.

Authors' contribution: Galyna Chornous – conceptualization,
methodology development, writing (review and editing); Mariana
Petrova – іdeas; formulation or evolution of overarching research
goals and aims; Maryna Horna – data validation, writing (original
draft), literature analysis, preparation of the literature review and

~200 ~ ВІСНИК  Київського національного університету імені Тараса Шевченка

ISSN 1728-3817
theoretical background; Nikolay Penev – іdeas; formulation or
evolution of overarching research goals and aims; Maiia Pustovit –
empirical data collection and validation, implementation of empirical
research.

Sources of funding. This study did not receive any grant from
a funding institution in the public, commercial, or non-commercial
sectors. The funding is covered by the authors' own expense.

References
Ben Mrad, A., & Hnich, B. (2024). Intelligent attribution modeling for
enhanced digital marketing performance. Intelligent Systems with
Applications, 21, 200337. https://doi.org/10.1016/j.iswa.2024.200337.
Cain, P. M. (2014). Brand management and the marketing mix model.
Journal of Marketing Analytics, 2(1), 33–42.
Chornous G., & Fareniuk Y. (2021). Marketing  mix  modeling  for
pharmaceutical  companies  on  the  basis  of  data  science  technologies.
Access  to  science,  business,  innovation  in  digital economy , 2(3), 274–
289. https://doi.org/10.46656/access.2021.2.3(6)
Cooper, A. (2022, December 31). How Shapley values work.
https://www.aidancooper.co.uk/how-shapley-values-work/
Dhar, S., & Singh, N. (2020). Attribution Modelling in Marketing: Literature
Review and Research Agenda. Academy of Marketing Studies Journal, 24(4),
1–21. https://www.abacademies.org/art icles/Attribution-modelling-in-
marketing-Literature-review-and-Research-Agenda-1528-2678-24-4-313.pdf
Dorokhova, L., Kuusik, A., Dimitrov, R., Pentus, K., Dorokhov, O., &
Petrova, M. (2023). Planning the digital marketing budget: computer
modelling for decision making. Access to science, business, innovation in the
digital economy, 4(2), 248–260. https://doi.org/10.46656/access.2023.4.2(7)
Gaur, J., & Bharti, K. (2020). Attribution Modelling in Marketing: Literature
Review and Research Agenda. Academy of Marketing Studies Journal, 24(4),
1–21. https://www.abacademies.org/articles/attribution-modelling-in-marketing-
literature-review-and-research-agenda-9492.html
Gujar, P., Paliwal, G., Panyam, S., & Kewalramani, C. (2024). Тhe evolution of ads
marketing mix modeling (MMM): From regression models to AI-powered planning for
SMBs. IEEE Technology and Engineering Management Society Journal, 1(1), 1–6.
https://doi.org/10.1109/TEMSCONLATAM61834.2024.10717768.
Hosahally, S., Bharadwaj, M., Zare mba, A., & Volkova, O. (2025).
Measuring digital advertising in a post-cookie era: A study of marketing-mix
models, attribution and incrementality. Journal of Digital & Social Media
Marketing. 12(4), 348–373.   https://doi.org/10.69554/wsat6359.
Kamena, R. (2021). Moving towards inferential attribution modelling in a
world without third-party cookies. Applied Marketing Analytics: The Peer-
Reviewed Journal. 7(2), 122–130. https://doi.org/10.69554/gltl7716.
Karray  S.,  Martín-Herrán  G.,  Sigué  S. P.  Managing  advertising  investments
in  marketing  channels.  Journal  of  Retailing  and  Consumer  Services, 2022,
65,  102852. https://doi.org/10.1016/j.jretconser.2021.102852
Lee, J., Jung, O., Lee, Y., Kim, O., & Park, C. (2021). A Comparison and
Interpretation of Machine Learning Algorithm for the Prediction of Online Purchase
Conversion. Journal of Theoretical and Applied Electronic Commerce Research,
16(5), 1472–1491. https://doi.org/10.3390/jtaer16050083
Li, Y., Xie, Y., & Zheng, Z. (2017).  Modeling Multi-Channel Advertising
Attribution Across Competitors. Microeconomics: Intertemporal Consumer
Choice & Savings eJournal , (Working Paper No. 3047981, pp. 1–58).
https://doi.org/10.2139/ssrn.3047981.
Mathew, M. (2016). Attribution: Untangling the web of confusion – a primer
for marketers. Applied Marketing Analytics: The Peer-Reviewed Journal,
329–339. https://doi.org/10.69554/ijhx1689.
Mehta, K., & Singhal, E. (2020). Marketing channel attribution modelling:
Markov chain analysis. International Journal of Indian Culture and Business
Management, 21(1), 63–77. https://doi.org/10.1504/ijicbm.2020.10027991
Méndez-Suárez, M., & Monfort, A. (2021). Marketing Attribution in
Omnichannel Retailing,  Springer (114–120). https://doi.org/10.1007/978-3-
030-76935-2_14.
Mulc, T., Anderson, M., Cubre, P., Zhang, H., Liu, I., & Kumar, S. (2025).
NNN: Next-Generation Neural Netw orks for Marketing Mix Modeling . ArXiv,
abs/2504.06212. https://doi.org/10.48550/arXiv.2504.06212.
Ravid, R. (2025). Marketing Mix Modeling in Lemonade.  ArXiv,
abs/2501.01276. https://doi.org/10.48550/arXiv.2501.01276.
Sciarrino, J., Friedman, J., Kirk, W. T., Mayers, C. A., & Prudente, J. J.
(2025). Salespersons as media channel: Making marketing mix modelling
work for business-to-business. Journal of Digital & Social Media Marketing ,
12(4). https://doi.org/10.69554/WNIS8466
Seth, S., & Ramakrishnan, S. (2025). Innovations in Multi-Touch Attribution
Models: Beyond Traditional Marketing Analytics in the Pharmaceutical
Sector. 2025 International Conference on Emerging Smart Computing and
Informatics (ESCI) (pp. 1–5). Institute of Electrical and Electronics Engineers
(IEEE). https://doi.org/10.1109/ESCI6 3694.2025.10988316. https://doi.org/
10.1109/ESCI63694.2025.10988316.
Sharma, P., Meena, J., & Ibrahim, S. (2017). Media mix modeling comparison
of interaction model to simple log-linear model. Asian Journal of Pharmaceutical
and Clinical Research, 10, 390. 10.22159/ajpcr.2017.v10s1.19763.
Sun, Y. (2023). Marketing attribution models: A survey of techniques used
in the industry.  Statsig. https://www.statsig. com/blog/marketing-attribution-
models-tech-survey
Yusup, M., Wijono, S., Manongga, D., Sembiring, I., Prasetyo, S. Y., &
Wellen, T. (2024). Systematic Literature Review: The Role of Artificial
Intelligence in Digital Marketing. Journal Sensi,  10(1), 56–66.
https://doi.org/10.33050/sensi.v10i1.3117
Zhao, K., Mahboobi, S. J., & Bagheri, S. R. (2022). Some game theoretic
marketing attribution models. Annals of Operations Research, 322, 153–179.
https://doi.org/10.1007/s10479-022-04944-5
Zhou, S., Pei, Q., & Li, J. (2024). From Multi-Touch Attribution to Marketing
Mix Modeling: Leveraging Multi-Information Fusion for Advanced Advertising
Analytics. IEEE/WIC International Conference on Web Intelligence and
Intelligent Agent Technology (WI-IAT) (pp. 677–681). ). Institute of Electrical
and Electronics Engineers (IEEE). https://doi.org/10.1109/WI-
IAT62293.2024.00109.

Отримано  редакцією  журналу  / Received: 22.07.25
Прорецензовано  / Revised: 01.08.25
Схвалено  до  друку  / Accepted: 15.08.25

Галина ЧОРНОУС1, д-р екон. наук, проф.
ORCID ID: 0000-0003-4889-1247
e-mail: galyna.chornous@knu.ua

Маріана ПЕТРОВА2, д-р фіз.-мат. наук, проф.
ORCID ID: 0000-0003-1531-4312
e-mail: m.petrova@ts.uni-vt.bg

Марина ГОРНА1, канд. екон. наук, доц.
ORCID ID: 0000-0002-6011-5753
e-mail: maryna.horna@knu.ua

Ніколай ПЕНЕВ3, канд. екон. наук, доц.
ORCID ID: 0009-0003-7359-8357
e-mail: nikolay.penev@trakia-uni.bg

Майя ПУСТОВІТ1, бакалавр
ORCID ID: 0009-0001-0472-9662
e-mail: maya.pustovit2004@knu.ua

1 Київський національний університет імені Тараса Шевченка, Київ, Україна
2 Великотирновський університет імені Св. Кирилла та Св. Мефодія, Велико-Тирново, Болгарія
3 Тракійський університет, Стара Загора, Болгарія

МОДЕЛЮВАННЯ АТРИБУЦІЇ НА ОСНОВІ ДАНИХ У ЦИФРОВОМУ МАРКЕТИНГУ

Вступ .  У сучасному цифровому середовищі маркетингові комунікації стали багатоканальними, персоналізованими та
динамічними, що зумовлює зростаючу потребу у точному вимірюванні ефективності кожної взаємодії користувача з брендом.
Традиційні правила маркетингової атрибуції, які надають усю цінність одній точці контакту, вже не забезпечують належного рівня
аналітичної точності. У відповідь на ці виклики все ширше застосовують економіко-математичні методи, зокрема й моделі на основі
ланцюгів Маркова та значень Шеплі, що дають змогу аргументовано й кількісно обґрунтовано розподіляти цінність між усіма каналами.

ЕКОНОМІКА. 1(228)/2026 ~ 201 ~

ISSN 1728-2667 (Print), ISSN 2079-908X (Online)
Методи .  Методологія дослідження ґрунтується на поєднанні загальнонаукових і спеціалізованих методів. Зокрема, використано
теоретичне моделювання, порівняльний аналіз, а також стохастичне моделювання (ланцюги Маркова) та теорію кооперативних ігор
(значення Шеплі).
Результати .  У цьому дослідженні вивчено проблему маркетингової атрибуції в цифровому середовищі, доведено обмеженість
традиційних моделей та обґрунтовано переваги адаптивних підходів, таких як ланцюги Маркова та значення Шеплі. Практична
реалізація та порівняльний аналіз моделі на основі значень Шеплі підтвердили її вищу точність і здатність об'єктивно оцінювати
внесок кожного каналу, що дозволило сформулювати цінні рекомендації для оптимізації маркетингових стратегій.
Висновки .  Розроблено та впроваджено модель атрибуції на основі значень Шеплі, що дає змогу враховувати маржинальний
внесок каналів у всіх можливих комбінаціях взаємодій, на відміну від традиційних моделей маркетингової атрибуції, що засновані на
правилах. Результати дослідження можуть бути використані компаніями для точнішого оцінювання ефективності маркетингових
каналів, оптимізації бюджету та підвищення рентабельності інвестицій у цифрову рекламу.

Ключові  слова :  маркетингова атрибуція, цифровий маркетинг, атрибуція на основі даних, значення Шеплі, ланцюги Маркова,
мультиканальна аналітика, Python.

Автори заявляють про відсутність конфлікту інтересів. Спонсори не брали участі в розробленні дослідження; у зборі, аналізі чи
інтерпретації даних; у написанні рукопису; в рішенні про публікацію результатів.
The authors declare no conflicts of interest. The funders had no role in the design of the study; in the collection, analyses or interpretation
of data; in the writing of the manuscript; in the decision to publish the results.
