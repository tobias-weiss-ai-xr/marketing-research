---
title: 'A Comparative Study of Ad Attribution Models: Evaluating the Impact on ROI Measurement'
url: https://doi.org/10.37745/ejcsit.2013/vol13n355675
category: privacy-data
subcategory: measurement
date: 2025-05
venue: European Journal of Computer Science and Information Technology
authors:
- Ashutosh Kumar Verma
source: openalex-oa
pdf_url: https://eajournals.org/ejcsit/wp-content/uploads/sites/21/2025/06/A-Comparative-Study.pdf
pages: 20
chars: 71427
fetched_at: '2026-11-08T17:34:22+00:00'
kb_version: 1
---

# A Comparative Study of Ad Attribution Models: Evaluating the Impact on ROI Measurement

European Journal of Computer Science and Information Technology,13(35),56-75, 2025
 Print ISSN: 2054-0957 (Print)
                                                                            Online ISSN: 2054-0965 (Online)
                                                                      Website: https://www.eajournals.org/
                         Publication of the European Centre for Research Training and Development -UK
56

A Comparative Study of Ad Attribution
Models: Evaluating the Impact on ROI
Measurement

Ashutosh Verma
Meta, USA

doi: https://doi.org/10.37745/ejcsit.2013/vol13n355675                                         Published June 06, 2025

Citation: Verma A (2025) A Comparative Study of Ad Attribution Models: Evaluating the Impact on ROI
Measurement, European Journal of Computer Science and Information Technology ,13(35),56-75

Abstract: This article examines the critical relationship between ad attribution modeling and return on
investment measurement in digital advertising. Through comparative analysis of prominent attribution
methodologies—including last -click, first -click, multi -touch, and data -driven models —the article
investigates how attribution choice  fundamentally shapes ROI calculations and subsequent marketing
decisions. The findings suggest that single -touch models systematically misrepresent customer journeys
and distort ROI calculations despite their implementation simplicity. Multi -touch and alg orithmic
approaches deliver more nuanced insights but present significant implementation challenges. Case studies
across e -commerce and SaaS businesses demonstrate substantial variation in perceived channel
performance based on attribution methodology. As privacy regulations reshape tracking capabilities,
emerging privacy -first attribution approaches and holistic measurement frameworks that incorporate
lifetime value and offline touchpoints represent the future direction of marketing measurement. The article
provides practical guidance for marketing professionals navigating attribution implementation challenges
and highlights the importance of attribution model selection as a strategic rather than merely technical
decision.
Keywords: Attribution modeling, di gital advertising, ROI measurement, marketing analytics, customer
journey

INTRODUCTION

In the complex ecosystem of digital advertising, accurately measuring return on investment (ROI) remains
a fundamental challenge for marketing departments. The digital advertising market has experienced
explosive growth, with increasing complexity across c hannels and touchpoints that consumers encounter
on their purchase journey. At the core of this measurement challenge lies a critical but often overlooked
factor: the attribution model employed to assign conversion credit across multiple touchpoints in the

             European Journal of Computer Science and Information Technology,13(35),56-75, 2025
 Print ISSN: 2054-0957 (Print)
                                                                            Online ISSN: 2054-0965 (Online)
                                                                      Website: https://www.eajournals.org/
                         Publication of the European Centre for Research Training and Development -UK
57

customer journey. As demonstrated by Abhishek et al. in their comprehensive study of multi -stage
attribution, consumers typically interact with 3 -4 different advertising channels before completing a
conversion, with high -consideration purchases involving as many as 7 -8 touchpoints spread across both
digital and traditional media [1].

Attribution modeling—the process of determining how conversion credit is allocated to various marketing
interactions—significantly influences how organizations perceive marketing performance, allocate
budgets, and calculate ROI. Research by Li and Kannan examining over 1,600 customer journeys across a
multichannel retailer found that attribution model selection can dramatically alter perceived channel
effectiveness, with differences as high as 143% in attributed value when comparing traditional last -click
models to more sophisticated approaches [2]. Their empirical analysis revealed that search advertising
received 94% more credit in last -click models than warranted by act ual customer behavior, while display
advertising was undervalued by approximately 36%. Despite its importance, many organizations implement
attribution models without fully understanding their implicit assumptions and limitations, leading to
systematic mis allocations of marketing resources that Li and Kannan estimated could reduce overall
marketing ROI by 7-12% in typical multichannel environments [2].

This article examines how different attribution models impact ROI measurement across digital advertising
channels. Abhishek et al. identified three distinct stages in the consumer purchase funnel —awareness,
consideration, and conversion—with each stage having different attribution requirements and effectiveness
indicators [1]. Their research demonstrated that  exposure to display advertising increased the probability
of a branded search by 16.2% and the likelihood of a direct website visit by 9.4%, yet these contributions
remained entirely invisible in single -touch attribution frameworks. By analyzing the mecha nisms,
advantages, limitations, and practical implementations of various attribution frameworks, we aim to provide
marketing professionals with a comprehensive understanding of how attribution methodologies influence
perceived campaign effectiveness and investment decisions. As Abhishek et al. concluded in their analysis
of online advertising dynamics, the choice of attribution model can alter calculated channel ROI by 30-40%
for identical marketing activities, making attribution modeling one of the most co nsequential yet under -
examined aspects of marketing measurement [1].

Attribution Models: Overview and Classification
Attribution models can be broadly categorized into three main types: single -touch, multi-touch, and data-
driven models. Each employs diffe rent methodologies and assumptions to assign conversion credit, with
significant implications for marketing measurement and investment decisions. As demonstrated in
Dalessandro et al.'s causal framework research, the selection of attribution methodology can fundamentally
alter perceived marketing effectiveness, with their study showing that a shift from traditional last -click
models to causally adjusted attribution redistributed approximately 48% of conversion credit across display
advertising campaigns [3].

             European Journal of Computer Science and Information Technology,13(35),56-75, 2025
 Print ISSN: 2054-0957 (Print)
                                                                            Online ISSN: 2054-0965 (Online)
                                                                      Website: https://www.eajournals.org/
                         Publication of the European Centre for Research Training and Development -UK
58

Single-Touch Attribution Models
Single-touch models assign 100% of conversion credit to a single interaction point along the customer
journey, representing the most straightforward approach to attribution. Despite their conceptual limitations,
these models remain prevalent in digital marketing practice. Dalessandro et al.'s analysis of attribution
methodologies found that approximately 65% of organizations primarily rely on single -touch attribution
for performance evaluation, despite the clear conceptual and empirical limitations of these approaches when
applied to complex customer journeys [3].

Last-Click Attribution credits the final touchpoint preceding conversion with the entire value of that
conversion. This remains the default model in many analytics platforms due to its implementation simplicity
and clear line of sight to conversion events. However, Kireyev et al.'s empirical examination of display -
search dynamics revealed significant limitations in this approach. Their vector autoregression analy sis
demonstrated that display advertising exposures increased branded search activity by approximately 14.5%
within a 4-week window, despite receiving zero credit in last-click attribution frameworks [4]. Their study
further demonstrated that last -click at tribution underestimates display advertising's contribution by
approximately 34.7% on average, leading to systematic underinvestment in awareness -building activities
across the marketing funnel.

First-Click Attribution assigns all conversion credit to the  initial touchpoint, emphasizing the value of
channels that introduce customers to the brand. This approach inverts the biases present in last-click models
by systematically overvaluing awareness -generating activities. Dalessandro et al.'s causal attributi on
framework revealed that first-click models overestimate the contribution of top-funnel display impressions
by approximately 27 -41% compared to causal attribution methods [3]. Their counterfactual analysis
demonstrated that first -click attribution often leads organizations to underinvest in retargeting and
conversion-focused campaigns, with potentially substantial negative impacts on overall campaign
performance and efficiency.

Multi-Touch Attribution Models
Multi-touch models distribute conversion credit across multiple touchpoints according to predefined rules,
addressing the fundamental limitations of single -touch approaches by acknowledging the cumulative
impact of marketing interactions throughout the customer journey. According to Dalessandro et al. 's
research, multi -touch attribution methodologies significantly alter channel valuation across digital
marketing investments, with an average redistribution of 31.4% of conversion credit when comparing rule-
based multi-touch models to traditional last-click approaches across their dataset [3].

Linear Attribution distributes credit equally across all touchpoints in the conversion path, assigning each
interaction the same weight regardless of position or timing. This approach recognizes the contribution of
all channels but fails to account for the varying impact of different touchpoints. Dalessandro et al. found
that linear attribution increased attributed value for middle -funnel display impressions by approximately
22.6% compared to last-click models in their experimental framework [3]. However, their causal analysis

             European Journal of Computer Science and Information Technology,13(35),56-75, 2025
 Print ISSN: 2054-0957 (Print)
                                                                            Online ISSN: 2054-0965 (Online)
                                                                      Website: https://www.eajournals.org/
                         Publication of the European Centre for Research Training and Development -UK
59

demonstrated that linear attribution's equal weighting assumption contradicts observed influence patterns
in actual consumer behavior, where certain advertising exposures demonstrated 2.7-3.5 times higher causal
impact on eventual conversion probability than others along the same path.

Time-Decay Attribution allocates progressively more credit to touchpoints closer to conversion, using a
mathematical decay function to determine weights. This mod el acknowledges the increasing influence of
marketing activities as consumers approach purchase decisions. Kireyev et al.'s vector autoregressive
modeling found that time -decay models with a standard half -life of 7 days provide a more accurate
representation of the diminishing impact of display advertising over time, with their impulse response
function showing that the effect of display exposures on conversion probability declines by approximately
55% after one week and 84% after two weeks [4]. Their empir ical analysis demonstrated that time-decay
attribution reduces the measurement gap between display advertising's true contribution and its attributed
value by approximately 41% compared to last-click models.

Position-Based (U-Shaped) Attribution typically assigns 40% credit to both first and last interactions, with
the remaining 20% distributed among intermediate touchpoints. This hybrid approach attempts to balance
the recognition of both introduction and conversion touchpoints. Dalessandro et al.'s exper imental
comparison of attribution methodologies found that U-shaped models produced attribution allocations that
fell between linear and time -decay models in terms of their deviation from causally -adjusted attribution
values [3]. Their analysis showed that  U-shaped attribution increased the attributed value of awareness
channels by 31.6% on average compared to last -click models while maintaining 73.2% of conversion -
proximity credit, representing a pragmatic compromise between implementation simplicity and
measurement accuracy.

Data-Driven and Algorithmic Models
Advanced attribution approaches employ statistical techniques to derive attribution weights from actual
user behavior, representing the most sophisticated attribution methodologies currently availabl e. Kireyev
et al.'s comprehensive analysis demonstrated that data-driven attribution models reduced measurement error
by 38-44% compared to rule -based approaches when validated against their vector autoregression results
for cross-channel effects [4].

Markov Chain Models utilize probability theory to map the customer journey as a series of state transitions,
calculating the removal effect of each channel to determine its importance. These models estimate the
probability of conversion through different path combinations, assigning value based on each touchpoint's
marginal contribution to conversion likelihood. Dalessandro et al.'s research demonstrated that probabilistic
Markov models produced attribution values that more closely aligned with their causal framework results,
reducing measurement discrepancies by approximately 29% compared to rule-based approaches [3]. Their
study found that Markov Chain attribution identified 26.7% more incremental value from mid -funnel
display impressions and 24.3% less va lue from branded search compared to traditional last -click
methodologies.

             European Journal of Computer Science and Information Technology,13(35),56-75, 2025
 Print ISSN: 2054-0957 (Print)
                                                                            Online ISSN: 2054-0965 (Online)
                                                                      Website: https://www.eajournals.org/
                         Publication of the European Centre for Research Training and Development -UK
60

Shapley Value Models apply game theory principles to fairly distribute conversion credit based on each
channel's marginal contribution. This approach considers all possible combinati ons of marketing
touchpoints to determine the incremental value each channel contributes. Kireyev et al.'s cross -channel
analysis found that Shapley value attribution more accurately captured the synergistic relationships between
display and search adverti sing, with their model identifying that display exposures increased the
effectiveness of subsequent search clicks by approximately 17.2% [4]. Their research demonstrated that
Shapley models could account for both the direct and indirect effects of advertising exposures, providing a
more comprehensive measurement framework for cross-channel marketing investments.

Machine Learning Models leverage regression analysis, neural networks, or other algorithms to
dynamically determine attribution weights based on h istorical patterns and predictive modeling. These
approaches can incorporate vast arrays of variables beyond simple touchpoint sequences. Dalessandro et
al.'s experimental implementation of a causally motivated machine learning attribution framework
demonstrated that properly trained algorithms could reduce attribution bias by up to 32% compared to rule-
based approaches [3]. Their research showed that machine learning models achieved the highest accuracy
when incorporating not just conversion path data but also user characteristics, contextual factors, and
temporal variables, identifying causal relationships that remained invisible in traditional attribution
frameworks.
Table 1: Attribution Model Types and Characteristics [3,4]
Attribution Model Description Implementation
Complexity
Relative Accuracy Ranking
Last-Click Credits final touchpoint before
conversion
Low Lowest (25.7% deviation
from baseline)
First-Click Credits the initial touchpoint Low Very Low (overestimates
top-funnel by 21-41%)
Linear Equal credit across all
touchpoints
Medium Moderate
Time-Decay More credit to touchpoints
closer to conversion
Medium Moderate-High (41%
improvement over last-click)
Position-Based 40% first, 40% last, 20% middle
touchpoints
Medium High (within 11.6% of
experimental baseline)
Markov Chain Credits based on conversion
probability impact
High Very High (29% better than
rule-based models)
Shapley Value Game theory-based attribution High Very High
Machine Learning Algorithm-determined dynamic
weights
Very High Highest (32% less bias than
rule-based models)

             European Journal of Computer Science and Information Technology,13(35),56-75, 2025
 Print ISSN: 2054-0957 (Print)
                                                                            Online ISSN: 2054-0965 (Online)
                                                                      Website: https://www.eajournals.org/
                         Publication of the European Centre for Research Training and Development -UK
61

Impact of Attribution Models on ROI Measurement
The choice of attribution model creates substantial variation in perceived channel performance and ROI
calculations. This section examines these effects  through comparative analysis, revealing how attribution
methodology fundamentally shapes marketing investment decisions. According to comprehensive research
by Li et al., attribution model selection significantly alters channel performance evaluation, wit h their
experimental findings demonstrating that conversion path analysis using different methodologies can
produce variance in attributed channel value by up to 30% for identical marketing investments, particularly
for channels with complementary effects in the customer journey [5].

Systematic Biases in Single-Touch Models
Last-click attribution systematically overvalues channels that appear later in the conversion funnel (e.g.,
branded search, retargeting) while undervaluing awareness and consideration channels (e.g., display
advertising, social media). Li et al.'s research using controlled experiments across multiple retail advertisers
demonstrated that last -click attribution missed approximately 77% of the true impact from display
advertising on conver ting customers [5]. Their analysis found that traditional last -click approaches
overestimated the value of branded search terms by up to 23% versus incrementality tests, creating
persistent measurement distortions that affected budget allocation decisions. Advertisers in their study who
relied exclusively on last-click attribution showed significant underinvestment in upper -funnel marketing
activities, with budget allocations to awareness channels averaging 14% below experimentally-determined
optimal levels.

Conversely, first-click models overemphasize top-of-funnel activities while minimizing the contribution of
conversion-focused channels. Abhishek et al.'s multi -stage attribution research examining customer
journeys across display advertising, search, an d direct website visits revealed that first -click attribution
systematically overvalued initial display advertising exposures by up to 21% compared to their causal
impact on conversion probability [6]. Their analysis of the purchase funnel through awarenes s,
consideration, and conversion stages demonstrated that neither first -click nor last-click models accurately
captured cross-channel effects, with both approaches creating a fragmented view of the customer journey
that led to suboptimal budget allocation. Their study of 10,000 customers exposed to display ads found that
first-click attribution failed to properly value conversion -supporting touchpoints, underestimating the
effectiveness of performance-focused marketing activities by approximately 19% on average.

Channel-Specific ROI Distortions
Attribution model selection particularly impacts ROI measurement for specific channels, creating
systematic biases that distort perceived marketing effectiveness across the digital ecosystem. Li et al.'s
experiments with alternative attribution frameworks revealed substantial variation in perceived channel
performance depending on the chosen methodology [5].

Paid Search experiences dramatic valuation shifts across attribution methodologies. Li et al.'s research
comparing traditional last -click attribution against multi -touch models found that paid search attribution

             European Journal of Computer Science and Information Technology,13(35),56-75, 2025
 Print ISSN: 2054-0957 (Print)
                                                                            Online ISSN: 2054-0965 (Online)
                                                                      Website: https://www.eajournals.org/
                         Publication of the European Centre for Research Training and Development -UK
62

could vary by 18 -25% depending on the selected methodology [5]. Their analysis revealed that branded
search terms in particular received disproportionate credit in last-click models, with attribution overvaluing
these terms by approximately 21% compared to their true incremental value as determined through
experimental design. This overvaluation creates a systematic bias toward investing in lower-funnel search
activities at the expense of more complementary channels. According to their findings, multi -touch
attribution models typically reallocated 15-20% of conversion credit away from search advertising toward
display and other upper -funnel channels, suggest ing significant measurement distortion in traditional
approaches.

Display Advertising campaigns are systematically undervalued in last -click models, as their primary
contribution occurs earlier in the customer journey. Abhishek et al.'s research using a state-space model to
analyze the effects of display advertising demonstrated that display ads increased the probability of a
customer transitioning from awareness to the consideration stage by 15.2% on average, yet received
minimal credit in last-click frameworks [6]. Their study of 40,000 impressions across multiple campaigns
found that display advertising increased the probability of direct website visits by 6.3% and branded search
clicks by 9.2%, yet these indirect contributions remained almost entirely invisible in traditional attribution
models. Li et al.'s experimental comparison found that display advertising's attributed ROI increased by 21-
35% when measured with multi -touch approaches versus last -click methodologies, with particularly
significant differences observed for prospecting campaigns targeting new audience segments [5].

Email Marketing attribution varies significantly based on campaign type and customer journey position. Li
et al.'s attribution experiments demonstrated that triggered emails appearing near conversion received
approximately 1.7 times more credit under last -click attribution than warranted by their true incremental
value, while nurture email campaigns earlier in the customer journey received only 0.4 times their true
contribution [5]. Their analysis revealed that standard last-click models credited cart abandonment emails
with 24% more conversions than warranted by controlled experiments, while awareness -building email
campaigns to inactive customers were undervalued by 31%, creating a persistent measurement bias toward
short-term tactical email programs rather than strategic relationship development.

Social Media contributions are frequently underestimated in last -click frameworks due to their
predominantly upper-funnel influence. Abhishek et al.'s research modeling the customer purchase funnel
found that social media exposures increased the likelihood of a customer transitioning from awareness to
consideration phases by 12% and reduced the probability of abandonment during consideration by 8%, yet
these effects remained largely uncaptured in traditional attribution models [6]. Their analysis demonstrated
that social media's impact on conversion typically manifested through indirect effects that standard
attribution models failed to recognize. Li et al.'s comparison of attribution methodologies found that social
media channels showed approximately 25-40% higher attributed ROI under multi-touch models compared
to last-click frameworks, with particularly significant differences for video content and awareness-focused
campaigns [5].

             European Journal of Computer Science and Information Technology,13(35),56-75, 2025
 Print ISSN: 2054-0957 (Print)
                                                                            Online ISSN: 2054-0965 (Online)
                                                                      Website: https://www.eajournals.org/
                         Publication of the European Centre for Research Training and Development -UK
63

Temporal Effects on Attribution and ROI
Attribution models also create temporal distortions in ROI measurement, particularly affecting marketing
activities with extended impact patterns or time-lagged effects. Li et al.'s longitudinal analysis demonstrated
that attribution methodologies varied significantly in their ability to capture these temporal dimensions [5].
Conversion Lag Effects create systematic measurement distortions as last -click models fail to account for
the time lag between initial exposure and conversion. This limitation is particularly problematic for products
with longer consideration cycles. Li et al.'s research examining purchase journeys across different product
categories found that for high-consideration purchases, last-click attribution undervalued initial touchpoints
by approximately 35% on average compared to more sophisticated approaches accounting for temporal
effects [5]. Their attribution experiments demonstrated that customer j ourneys extending beyond 14 days
showed the most significant measurement discrepancies across attribution models, with early touchpoints
receiving 60-70% less credit in last-click models than their experimentally verified contribution to eventual
conversion probability.

Campaign Interaction Effects are measured with varying accuracy across attribution methodologies.
Different attribution models produce substantially different assessments of how campaigns interact over
time and across channels. Abhishek et al.'s multi-stage attribution framework revealed that the combination
of display advertising followed by search clicks increased conversion probability by 17% compared to
search clicks alone, yet traditional attribution models failed to capture this synergistic relationship [6]. Their
analysis demonstrated that exposure to display advertising increased the effectiveness of subsequent
branded search by approximately 11%, creating cross -channel effects that remained invisible in siloed
attribution approaches. Li et al.'s research showed that attribution models incorporating interaction effects
identified 22-29% more value from complementary channel combinations than traditional models treating
channels independently [5].

Seasonality Interpretation varies sign ificantly across attribution methodologies, creating substantial
measurement inconsistencies during high -volume periods. Li et al.'s experimental research found that
during peak sales periods, last-click attribution models systematically overattributed conversion increases
to bottom-funnel activities, misrepresenting the true drivers of seasonal performance [5]. Their analysis
demonstrated that during promotional periods, last-click models overvalued tactical remarketing campaigns
by approximately 19 -27% while undervaluing brand awareness activities by 22 -31% compared to their
controlled experiment results. This measurement distortion creates persistent misunderstandings about
which marketing activities truly drive seasonal performance, leading to suboptimal  budget allocations
during critical business periods when accurate measurement is most valuable.

             European Journal of Computer Science and Information Technology,13(35),56-75, 2025
 Print ISSN: 2054-0957 (Print)
                                                                            Online ISSN: 2054-0965 (Online)
                                                                      Website: https://www.eajournals.org/
                         Publication of the European Centre for Research Training and Development -UK
64

Table 2: Channel-Specific ROI Distortions by Attribution Model [5,6]
Channel Last-Click Bias First-Click Bias Multi-Touch
Impact
Data-Driven
Revelation
Paid Search Overvalued
(+21%)
Undervalued Reduced ROI vs.
last-click
More accurate
valuation of branded
terms
Display
Advertising
Severely
undervalued
Overvalued
(+21%)
Increased ROI
(+21-35%)
Captures indirect
conversion effects
Email
Marketing
Overvalues trigger
emails (+70%)
Undervalues
trigger emails
More balanced
valuation
Distinguishes
between tactical and
strategic campaigns
Social Media Severely
undervalued
Overvalued Higher attributed
ROI (+25-40%)
Captures transition
effects between
funnel stages
Organic Search Moderately
undervalued
Overvalued More balanced
valuation
Reveals carryover
effects (+17.8%)
Direct
Navigation
Overvalued Undervalued Reduced
attribution
Shows influence from
previous channels

Empirical Case Studies
Empirical evidence from real -world attribution implementations provides crucial insights into how
attribution model selection impacts perceived marketing performance and subsequent business outcomes.
This section examines case studies across different busi ness models to demonstrate the practical
implications of attribution methodology choices on ROI measurement and budget allocation decisions.

Case Study: E-commerce Retailer
The implementation of comprehensive attribution frameworks in e -commerce environme nts reveals
dramatic variations in channel valuation and ROI assessment based on attribution methodology. Anderl et
al. conducted an extensive empirical analysis using a comprehensive dataset from a major European online
retailer with more than 29.1 million customer journeys across paid search, social media, display advertising,
affiliate marketing, and email campaigns [7]. Their study implemented seven distinct attribution
methodologies—last-click, first -click, linear, time -decay, position -based, Markov -chain, and their
proposed graph-based data-driven approach—to evaluate identical marketing performance across a 30-day
conversion window.

The analysis revealed significant channel -specific ROI variations depending on attribution methodology.
According to Anderl et al., the channel with the highest sensitivity to attribution model selection was display
advertising, with attributed conversion volume varying by up to 204% between models [7]. Their data

             European Journal of Computer Science and Information Technology,13(35),56-75, 2025
 Print ISSN: 2054-0957 (Print)
                                                                            Online ISSN: 2054-0965 (Online)
                                                                      Website: https://www.eajournals.org/
                         Publication of the European Centre for Research Training and Development -UK
65

showed that under last -click attribution, display advertisi ng received credit for only 4.2% of total
conversions, while the same campaigns received credit for 12.8% of conversions under their graph -based
attribution model. This dramatic difference reflected display advertising's predominantly upper -funnel
influence, with their clickstream analysis revealing that 71.3% of display touchpoints occurred in early
stages of customer journeys, yet received minimal credit in last-click frameworks.

Anderl et al.'s research further demonstrated substantial variation in soci al media valuation across
attribution methodologies. Their study found that social channels received 165% more conversion credit
under first-click attribution compared to last-click approaches [7]. The empirical data indicated that organic
social media tou chpoints in particular showed extreme attribution variability, receiving 3.4 times more
conversion credit in first -click models than last -click models. The researchers noted that social media's
position distribution in customer journeys was distinctly non -uniform, with touchpoints appearing
prominently in both early awareness -building stages (26.7% occurring as first touchpoints) and later
consideration phases (18.5% occurring within 48 hours of conversion).

Email marketing conversion attribution demonstra ted significant inconsistency across attribution
approaches in Anderl et al.'s study. Their analysis revealed that triggered email campaigns appearing near
conversion received 3.1 times more credit under last-click attribution than first-click models, while broader
newsletter campaigns were undervalued by approximately 54% in last -click models compared to their
graph-based attribution approach [7]. The researchers found that email touchpoints had the highest
conversion rate among all channels (5.2% versus an average of 2.1% across other channels), yet this metric
alone masked significant variation in incremental impact. Their path analysis demonstrated that email
touchpoints appearing after direct search visits had 86% higher conversion probability than the same emails
delivered without prior channel exposure, suggesting significant interaction effects that most attribution
models failed to capture.

Perhaps most significantly, Anderl et al. found that overall marketing ROI assessments across their entire
dataset differed by 31% between the most extreme attribution models [7]. Their analysis indicated that
cross-channel effects fundamentally influenced conversion probability, with their data showing that
customer journeys containing touchpoints from three or more channels had 24.5% higher conversion rates
than single-channel journeys, yet these synergistic relationships remained largely uncaptured in traditional
attribution frameworks. The research team's controlled simulations suggested that position -based
attribution models provided the closest approximation to actual incremental value among the rule -based
approaches (within 11.6% of their experimental baseline), while last -click models produced the most
significant measurement distortion (differing by 25.7% from the experimental baseline).

Case Study: SaaS Company
The impact of attribution modeling on subscription -based businesses reveals unique challenges related to
customer acquisition cost (CAC) and lifetime value (LTV) calculations. Li and Kannan exami ned
attribution model performance within a major software -as-a-service (SaaS) provider offering marketing

             European Journal of Computer Science and Information Technology,13(35),56-75, 2025
 Print ISSN: 2054-0957 (Print)
                                                                            Online ISSN: 2054-0965 (Online)
                                                                      Website: https://www.eajournals.org/
                         Publication of the European Centre for Research Training and Development -UK
66

automation solutions to business customers, with particular focus on the relationship between channel
attribution and customer value prediction [8].

Their study implemented multiple attribution methodologies to evaluate identical marketing performance
data, comparing traditional rule -based approaches against their proposed integrated attribution model,
incorporating both direct and carryover effects. The research focused on how attribution models influenced
customer acquisition cost calculations and their alignment with eventual customer lifetime value across six
key marketing channels: direct navigation, organic search, paid search, display advertising, referral sources,
and email marketing.

Li and Kannan's research demonstrated that data -driven attribution models identified key upper -funnel
touchpoints that significantly influenced eventual customer lifetime value but remained undervalued in
traditional models [8]. Their analysis revealed that organic search interactions, while less likely to
immediately precede conversion (only 14.2% of conversions had organic search as the last touchpoint), had
substantial carryover effects on other channels. Accordi ng to their model estimation, exposure to organic
search content increased the effectiveness of subsequent paid search interactions by 17.8% and direct site
visits by 9.2%, yet these indirect contributions remained invisible in last-touch attribution frameworks. By
incorporating these carryover effects, their model reassigned approximately 21.4% of conversion credit
across channels compared to traditional approaches.

The research revealed that algorithmic attribution substantially altered customer acquisit ion cost
calculations for certain channels by better recognizing their full contribution to conversions. Li and
Kannan's data showed that traditional last-interaction models assigned an average acquisition cost of $95.64
for customers converted through pai d search, while their integrated approach assigned $82.43 after
accounting for paid search's role in supporting conversions through other channels [8]. Their analysis found
that channels with high direct conversion impact received 34.6% more credit on average in last-interaction
models than warranted by their true incremental contribution, while channels with significant carryover
effects were systematically undervalued by 27.3%.

Li and Kannan's research demonstrated that the implementation of sophisticate d attribution led to
significant performance improvements through budget reallocation [8]. Their counterfactual simulations
showed that optimal budget allocation based on their integrated attribution model could increase overall
conversion volume by 12.7% without additional spending, primarily by redistributing investment toward
channels with high carryover effects. The research revealed that channels traditionally viewed as "assisting"
(with conversion rates below the site average but high carryover effect s) were significantly underinvested
in, receiving 31.8% less budget than optimal levels under traditional attribution approaches. Most notably,
their model demonstrated that considering both direct and indirect channel contributions reduced overall
customer acquisition costs by 14.2% by recognizing the full value of upper -funnel activities in driving
eventual conversions.

             European Journal of Computer Science and Information Technology,13(35),56-75, 2025
 Print ISSN: 2054-0957 (Print)
                                                                            Online ISSN: 2054-0965 (Online)
                                                                      Website: https://www.eajournals.org/
                         Publication of the European Centre for Research Training and Development -UK
67

Table 3: Case Study Findings: E-commerce vs. SaaS Attribution Impact [7,8]
Aspect E-commerce Retailer
Findings
SaaS Company Findings
Dataset Scale 29.1 million customer
journeys
Multiple attribution
methodologies
Display Attribution
Variance
204% between models Influenced CLV but invisible
in last-click
Social Media Credit 165% more in first-click
vs. last-click
Not specifically measured
Email Performance 3.1x more credit to
triggered emails in last-
click
Not specifically measured
Cross-Channel Effects 24.5% higher conversion
with 3+ channels
Organic search boosted paid
search (+17.8%)
Overall ROI Difference 31% between extreme
models
12.7% conversion increase
through reallocation
Model Accuracy Position-based closest to
the experimental baseline
Algorithmic models reduced
CAC by ~$13 per customer
Key Insight U-shaped models
provided the best
compromise
Carryover effects redistributed
21.4% of credit

Practical Implementation Considerations
When selecting and implementing attribution models, organizations must consider several practical factors
that influence ROI measurement. These implementation considerations significantly impact attribution
effectiveness and ultimately determine whether theoretical measurement improvements translate into actual
business value. According to comprehensive research by Amplitude Analytics examining attribution
implementation chall enges across more than 200 digital -first companies, technical requirements, data
quality issues, and organizational alignment represent the most significant barriers to successful attribution
deployment, with approximately 70% of organizations struggling t o implement their ideal attribution
approach due to these constraints [9].

Technical Requirements
Different attribution approaches require varying levels of technical infrastructure, creating significant
implementation challenges that directly impact ROI measurement capabilities. Amplitude's analysis of
attribution implementations across diverse organizations found that technical infrastructure requirements
represent the primary barrier to advanced attribution adoption, with many organizations defaulting t o
simpler methodologies despite understanding their limitations [9].

             European Journal of Computer Science and Information Technology,13(35),56-75, 2025
 Print ISSN: 2054-0957 (Print)
                                                                            Online ISSN: 2054-0965 (Online)
                                                                      Website: https://www.eajournals.org/
                         Publication of the European Centre for Research Training and Development -UK
68

Single-touch models can be implemented with basic analytics platforms but provide limited insight into
actual marketing effectiveness. According to Bucklin and Sismeiro's comprehensive an alysis of web
browsing behavior, single -touch attribution can be implemented with relatively straightforward tracking
mechanisms, requiring only basic page tagging and conversion tracking [10]. Their research demonstrated
that simple models analyzing only the final site visit before conversion could be implemented without
sophisticated cross -session user identification or complex data integration, explaining the continued
prevalence of last-click methodologies despite their known limitations. However, their analysis of browsing
patterns showed that focusing exclusively on conversion -proximate interactions fundamentally
misrepresented the customer journey, as their data revealed that users typically visited a site multiple times
before converting, with an ave rage of 2.3 visits per user in their study. This disconnect between
implementation simplicity and measurement accuracy represents a fundamental attribution challenge.

Multi-touch models require more sophisticated tracking and integration between marketing  platforms,
creating both technical and organizational challenges. Amplitude's research found that effective multi-touch
attribution implementation typically requires comprehensive user identification across touchpoints, with
cross-domain tracking and prop er session stitching representing significant technical hurdles [9]. Their
analysis revealed that organizations implementing multi -touch attribution needed to develop capabilities
for tracking users across multiple sessions, devices, and channels, with ide ntity resolution representing a
particularly challenging requirement. According to their research, multi-touch attribution implementations
typically required integration across various marketing platforms, analytics systems, and backend
databases, creating significant technical complexity compared to single-touch approaches. Amplitude noted
that proper multi -touch attribution implementation required dedicated tracking infrastructure beyond
standard analytics implementations, with custom event tracking and user identification strategies necessary
for accurate journey mapping.

Data-driven models demand robust data collection, processing capabilities, and often specialized expertise,
limiting their adoption despite their measurement advantages. Bucklin and Sis meiro's research on web
browsing behavior demonstrated the computational complexity of modeling customer journeys at scale,
with their relatively simple statistical model requiring significant computational resources for a limited
dataset [10]. Their study showed that even basic model-based approaches required sophisticated statistical
knowledge and technical implementation capabilities beyond those available in standard analytics
platforms. Amplitude's analysis of attribution implementations found that data-driven approaches required
both comprehensive data collection across touchpoints and sophisticated modeling capabilities to transform
this data into actionable insights [9]. Their research indicated that algorithmic attribution necessitated
specialized d ata science expertise to develop, validate, and maintain models, with many organizations
lacking these capabilities internally. According to their findings, fully implemented data-driven attribution
systems typically required both significant upfront investment in data infrastructure and ongoing resources
for maintenance and refinement, creating substantial barriers to adoption.

             European Journal of Computer Science and Information Technology,13(35),56-75, 2025
 Print ISSN: 2054-0957 (Print)
                                                                            Online ISSN: 2054-0965 (Online)
                                                                      Website: https://www.eajournals.org/
                         Publication of the European Centre for Research Training and Development -UK
69

Data Quality Challenges
Attribution accuracy fundamentally depends on data quality, with implementation challenges increasingly
complicated by privacy regulations and technical limitations. Amplitude's research on attribution
implementation found that data quality issues affected a majority of attribution initiatives, with most
organizations struggling to maintain consistent data collection across touchpoints [9].

Cookie deprecation and privacy regulations increasingly limit cross -channel tracking capabilities,
fundamentally constraining attribution model effectiveness. Amplitude's analysis of attribution challenges
noted that priv acy regulations like GDPR and CCPA have significantly impacted data collection
capabilities, with many organizations forced to reduce tracking scope and granularity to maintain
compliance [9]. Their research highlighted how browser privacy changes, particu larly the deprecation of
third-party cookies, have created substantial challenges for cross -site tracking, with organizations
increasingly unable to connect user journeys across different domains. According to their findings, these
privacy changes have par ticularly impacted the measurement of upper -funnel activities, as awareness -
building touchpoints often occur outside owned properties where first -party data collection is possible.
Amplitude noted that organizations have responded to these challenges by increasing reliance on first-party
data and developing alternative identification strategies, though these approaches typically provide less
comprehensive journey visibility than previously available with cross-site tracking.

Walled gardens (e.g., Facebook,  Amazon) restrict data sharing, creating attribution blind spots that
fundamentally limit measurement completeness. Amplitude's research found that major advertising
platforms increasingly limit the data they share externally, making it difficult to incorp orate these
touchpoints into comprehensive attribution models [9]. Their analysis highlighted how platform -specific
attribution systems operate independently from other marketing measurement, creating fragmented
visibility across the customer journey. Acco rding to their findings, walled garden environments typically
provide aggregated rather than user-level data, making it impossible to incorporate these touchpoints into
path-based attribution models. Amplitude noted that this data fragmentation forces many  organizations to
maintain separate attribution systems for different channels, reducing measurement consistency and
creating challenges for holistic marketing evaluation.

Cross-device journeys remain difficult to track comprehensively, affecting attribut ion accuracy in
increasingly fragmented digital environments. Bucklin and Sismeiro's analysis of web browsing behavior
demonstrated the challenges of tracking users across sessions even within a single website environment,
with their research showing signi ficant complexity in properly connecting user behavior across multiple
visits [10]. While their study focused on desktop browsing behavior, they identified the fundamental
challenge of maintaining consistent user identification across sessions —a challenge that increases
exponentially when considering multiple devices. Amplitude's attribution research highlighted how device
fragmentation has complicated attribution implementation, with users frequently switching between
smartphones, tablets, desktop computers, and other connected devices throughout their purchase journeys
[9]. Their analysis indicated that without robust cross-device identification capabilities, attribution models

             European Journal of Computer Science and Information Technology,13(35),56-75, 2025
 Print ISSN: 2054-0957 (Print)
                                                                            Online ISSN: 2054-0965 (Online)
                                                                      Website: https://www.eajournals.org/
                         Publication of the European Centre for Research Training and Development -UK
70

systematically misattribute conversions to the final device used rather than pr operly crediting touchpoints
across the complete journey. According to their findings, this measurement limitation particularly affects
mobile touchpoints, which frequently occur earlier in the customer journey but may not receive appropriate
credit if conversion happens later on another device.

Organizational Alignment
Attribution model selection has significant organizational implications that extend beyond technical
considerations to impact team dynamics, performance evaluation, and strategic decision -making.
Amplitude's research on attribution implementation found that organizational factors often determined
attribution success more strongly than technical capabilities, with alignment across teams representing a
critical success factor [9].

Channel-specific teams may resist models that reduce their perceived contribution, creating internal barriers
to attribution advancement. According to Amplitude's analysis of attribution implementation challenges,
many organizations experience internal resistance whe n transitioning to more sophisticated attribution
models that redistribute conversion credit across channels [9]. Their research found that teams managing
historically high-credited channels, particularly those focused on lower-funnel conversion activities, often
perceive attribution changes as threats to their perceived value and potentially to their resource allocation.
Amplitude noted that this resistance typically manifests as questioning of methodology, reluctance to
integrate necessary tracking, or continued reliance on channel-specific metrics rather than shared attribution
frameworks. According to their findings, successful attribution implementations typically addressed these
organizational concerns proactively by focusing on overall measurement imp rovement rather than
emphasizing the redistribution of credit between channels.

Executive buy-in requires clear communication about attribution limitations and assumptions, particularly
regarding expected business outcomes. Amplitude's research on attribu tion implementation found that
sustainable attribution initiatives typically enjoyed strong executive support based on clear understanding
of both capabilities and limitations [9]. Their analysis highlighted the importance of setting realistic
expectations about what attribution can and cannot accomplish, particularly regarding the inherent
assumptions in any attribution methodology. According to their findings, organizations that positioned
attribution as a decision-support tool rather than an absolute measure of truth typically experienced greater
executive alignment and more sustainable implementation. Amplitude noted that successful attribution
initiatives generally established clear connections between attribution insights and business outcomes,
demonstrating how improved measurement would lead to better decision -making and ultimately to
improved marketing performance.

Changing attribution models requires carefully managed transitions to avoid disruptive performance
comparisons and ensure organizational adoption. Bucklin and Sismeiro's research on web browsing
behavior demonstrated how even small changes in measurement approach can significantly impact metrics,
with their model showing substantial differences in user behavior interpretation depending on analytical

             European Journal of Computer Science and Information Technology,13(35),56-75, 2025
 Print ISSN: 2054-0957 (Print)
                                                                            Online ISSN: 2054-0965 (Online)
                                                                      Website: https://www.eajournals.org/
                         Publication of the European Centre for Research Training and Development -UK
71

methodology [10]. This fundamental reality creates significant challenges when transitioning attribution
approaches, as metrics will inevitably change even if underlying performance remains constant.
Amplitude's attribution research highlighted the importance of managing these transitions carefully, with
their analysis recommending phased implementation approaches that allow for appropriate comparison and
calibration between methodologies [9]. According to their findings, successful attribution transitions
typically included periods of parallel reporting, during which both legacy and new attribution approaches
operated simultaneously to establish conversion factors and build confidence in the new methodology.
Amplitude noted that organizations that implemented attribution changes as iterative improvements rather
than dramatic shifts typically experienced smoother transitions and greater organizational adoption of new
measurement frameworks.

Table 4: Implementation Challenges and Considerations [9,10]
Challenge
Category
Key Issues Technical Requirements Organizational Impact
Technical
Requirements
Infrastructure
complexity
Single-touch: Basic
analytics platform
Resource allocation
decisions
Data integration Multi-touch: Cross-session
tracking
Expertise requirements
Computational needs Data-driven: Advanced
modeling capabilities
Budget implications
Data Quality
Challenges
Privacy regulations User identification
limitations
Attribution accuracy
degradation
Walled gardens Platform data restrictions Measurement
fragmentation
Cross-device tracking Session stitching complexity Journey visibility gaps
Organizational
Alignment
Team resistance Performance evaluation
impact
Channel-specific
concerns
Executive buy-in Communication of
limitations
Expectation
management
Transition management Parallel reporting needs Methodology calibration

Future Directions in Attribution Modeling
The attribution landscape continues to evolve in response to technological and regulatory changes, with
organizations adapting measurement approaches to address new challenges and leverage emerging
capabilities. Current a ttribution methodologies face fundamental disruption from privacy regulations,

             European Journal of Computer Science and Information Technology,13(35),56-75, 2025
 Print ISSN: 2054-0957 (Print)
                                                                            Online ISSN: 2054-0965 (Online)
                                                                      Website: https://www.eajournals.org/
                         Publication of the European Centre for Research Training and Development -UK
72

technological shifts, and evolving business requirements, necessitating significant innovation in
measurement approaches. According to research by the Forbes Business Council examining developments
across digital advertising, marketing measurement technologies are undergoing their most significant
transformation in recent history, driven primarily by the impending deprecation of third-party cookies and
strengthening privacy regulations worldwide [11].

Privacy-First Attribution
As third-party cookies phase out and privacy regulations strengthen, new approaches to attribution have
emerged that balance measurement needs with privacy requirements. Forbes Business Council's analysis of
privacy-centric marketing strategies found that organizations are increasingly developing measurement
frameworks that operate effectively within a more constrained data environment, with industry leaders
recognizing that the future of attribution will re quire fundamentally different approaches than those that
have dominated the past decade [11].

Aggregated conversion modeling using machine learning to infer attribution without individual -level
tracking represents a promising approach to maintaining measurement capabilities while respecting privacy
constraints. According to Mozilla's research into privacy -preserving advertising technology, emerging
approaches like Privacy Preserving Attribution (PPA) aim to provide essential measurement capabilities
for marketers without compromising user privacy through individual tracking [12]. Their development
work demonstrates that aggregated attribution models can provide advertisers with critical conversion
information while maintaining strong privacy guarantees thro ugh techniques such as differential privacy,
secure multi-party computation, and aggregated reporting. Mozilla's documentation indicates that these
privacy-preserving approaches can effectively answer key marketing questions such as which campaigns
led to conversions and the relative performance of different advertising approaches without tracking
individual users across the web. Their Privacy Preserving Attribution specification has been designed to
support both click -based and view -based attribution while  providing flexible attribution windows that
accommodate different marketing use cases, demonstrating that sophisticated measurement remains
possible even with enhanced privacy protections.

Data clean rooms that enable privacy -compliant analysis across platforms have emerged as a technical
solution for maintaining measurement capabilities within a privacy -constrained environment. Forbes
Business Council's examination of post -cookie measurement strategies highlights data clean rooms as a
promising technological solution that allows advertisers and publishers to share and analyze data in privacy-
compliant ways [11]. Their analysis indicates that clean room technology creates secure environments
where first-party data from multiple sources can be analyzed without directly sharing user-level information
between parties, enabling attribution analysis while maintaining privacy compliance. According to their
research, major platforms including Google, Amazon, and Facebook have developed clean room solutions
that allow advertisers to upload their first -party data for secure matching against platform data, creating
attribution capabilities that don't rely on third-party cookies or cross-site tracking. These implementations
have seen rapid growth in adoption among larger advertisers seeking to maintain measurement capabilities

             European Journal of Computer Science and Information Technology,13(35),56-75, 2025
 Print ISSN: 2054-0957 (Print)
                                                                            Online ISSN: 2054-0965 (Online)
                                                                      Website: https://www.eajournals.org/
                         Publication of the European Centre for Research Training and Development -UK
73

while preparing for a cookieless future, with clean rooms emerging as a central component of privacy -
centric attribution strategies.

Incrementality testing is becoming more central to validating attribution models as traditional path -based
approaches face increasing limitations. Mozilla's privacy research acknowledges that while attribution
technology is evolving to become more priva cy-preserving, there remains a need for methodologies that
can assess the true incremental impact of advertising beyond simple correlation [12]. Their analysis
indicates that as individual -level tracking becomes more constrained, experimental approaches li ke
incrementality testing will become increasingly valuable for validating other measurement methodologies.
Mozilla's documentation notes that privacy -preserving attribution approaches can potentially support
experimental measurement through randomized con trolled trials conducted within privacy boundaries,
allowing advertisers to measure true causal impact rather than relying solely on correlational attribution
methods. These experimental approaches provide critical validation of other measurement systems w hile
maintaining alignment with evolving privacy standards, suggesting a complementary relationship between
privacy-preserving attribution and experimental measurement methodologies.

Holistic Business Outcome Measurement
Advanced organizations are moving beyond conversion -focused attribution to develop more
comprehensive measurement frameworks that better align with strategic business objectives. Forbes
Business Council's analysis of attribution evolution found that leading organizations increasingly view
conversion measurement as just one component of a broader marketing effectiveness framework that
incorporates longer-term business outcomes and cross-channel effects [11].

Integration of customer lifetime value into attribution frameworks represents a significant advancement in
connecting marketing measurement to financial outcomes. Forbes Business Council's research indicates
that forward-thinking organizations are increasingly incorporating customer lifetime value considerations
into their attribution models, recognizing that not all conversions carry equal long -term value [11]. Their
analysis found that organizations integrating CLV into attribution are better positioned to optimize for
sustainable growth rather than short -term conversion volume, particu larly important as privacy changes
limit some tactical optimization capabilities. According to their research, this integration enables more
sophisticated budget allocation decisions that prioritize acquiring and retaining high-value customers rather
than maximizing raw conversion counts, creating more sustainable business outcomes. The Forbes Business
Council notes that this CLV integration represents part of a broader trend toward connecting attribution
more directly to business outcomes rather than focus ing exclusively on marketing metrics, with leading
organizations developing measurement frameworks that directly link marketing activities to financial
performance through more sophisticated valuation models.

Incorporation of offline touchpoints into digi tal attribution models enables more comprehensive
measurement across the customer journey. Forbes Business Council's examination of attribution trends
highlights the growing importance of unified measurement across both digital and traditional channels,

             European Journal of Computer Science and Information Technology,13(35),56-75, 2025
 Print ISSN: 2054-0957 (Print)
                                                                            Online ISSN: 2054-0965 (Online)
                                                                      Website: https://www.eajournals.org/
                         Publication of the European Centre for Research Training and Development -UK
74

particularly as consumer journeys increasingly blend online and offline interactions [11]. Their analysis
indicates that organizations are increasingly developing measurement approaches that incorporate data from
point-of-sale systems, call centers, CRM platforms, and physical locations alongside digital touchpoints to
create a more complete view of the customer journey. This comprehensive approach recognizes that modern
customer experiences typically span multiple environments, with online research influenci ng offline
purchases and physical experiences driving digital engagement. According to their research, leading
organizations are implementing identity resolution strategies that connect online and offline interactions
through loyalty programs, customer acc ounts, and other authenticated touchpoints, creating more holistic
attribution capabilities that better reflect actual consumer behavior.

Unified marketing measurement approaches that combine attribution with marketing mix modeling are
emerging as the mos t sophisticated solution to comprehensive marketing effectiveness measurement.
Mozilla's privacy research acknowledges that while their Privacy Preserving Attribution work focuses
specifically on connecting ads to conversions, comprehensive marketing measu rement will likely require
multiple complementary methodologies as privacy protection increases [12]. Their documentation indicates
that a layered measurement approach combining multiple methodologies may provide the most complete
picture as individual tra cking becomes more limited. Forbes Business Council's analysis supports this
perspective, noting that leading organizations are increasingly implementing hybrid measurement
frameworks that leverage both detailed attribution, where available, and broader ec onometric modeling
where privacy constraints limit granular tracking [11]. Their research indicates that these unified
approaches typically provide attribution-like granularity for channels and touchpoints where user-level data
remains available through fi rst-party relationships, while using econometric techniques to measure
traditional media, brand marketing, and external factors affecting performance. According to their analysis,
this hybrid approach enables organizations to maintain measurement continuity through privacy transitions
while potentially developing more comprehensive marketing effectiveness frameworks than were possible
even with unlimited tracking capabilities.

CONCLUSION

Attribution model selection fundamentally shapes how organizations perceive marketing effectiveness and
make investment decisions. The evidence demonstrates that no single attribution model perfectly captures
the complex reality of customer journeys, but s ome approaches more accurately reflect marketing
contributions than others. Single -touch models systematically misrepresent channel contributions and
distort ROI calculations, while multi-touch and algorithmic approaches provide more balanced insights at
the cost of greater implementation complexity. As the digital landscape evolves with strengthened privacy
regulations and technological changes, forward-thinking organizations are adopting privacy-first attribution
methods and holistic measurement framework s that connect marketing activities to broader business
outcomes. The future of attribution lies in approaches that balance granular insights with privacy
compliance while integrating metrics beyond immediate conversions. Organizations that treat attributi on

             European Journal of Computer Science and Information Technology,13(35),56-75, 2025
 Print ISSN: 2054-0957 (Print)
                                                                            Online ISSN: 2054-0965 (Online)
                                                                      Website: https://www.eajournals.org/
                         Publication of the European Centre for Research Training and Development -UK
75

as a strategic decision framework rather than a technical implementation detail gain significant competitive
advantage in optimizing marketing investments and accurately measuring true marketing ROI.

REFERENCES

[1] Ya Zhang; Yi Wei; Jianbiao Ren,  "Multi-touch Attribution in Online Advertising with Survival
Theory," IEEE, 2015. https://ieeexplore.ieee.org/document/7023386
[2] Hongshuang (Alice) Li, et al, "Attributing conversions in a multichannel online marketing
environment: An empirical model and a field experiment," Sage journals, 2014.
https://journals.sagepub.com/doi/abs/10.1509/jmr.13.0050
[3] Brian Dalessandro, et al.,  "Causally motivated attribution for online advertising," UCL, 2012.
http://www0.cs.ucl.ac.uk/staff/w.zhang/rtb-papers/causual-conv-att.pdf
[4] Pavel Kireyev, et al., "Do display ads influence search? Attribution and dynamics in online
advertising," ScienceDirect, 2016.
https://www.sciencedirect.com/science/article/abs/pii/S0167811615001159
[5] Evert de Haan, "Attribution Modeling," ResearchGate, 2022.
https://www.researchgate.net/publication/362558530_Attribution_Modeling
[6] Vibhanshu Abhishek et al., "Media Exposure Through the Funnel: A Model of Multi-Stage
Attribution," SSRN,  2012. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2158421
[7] Eva Anderl, et al., "Mapping the Customer Journey: Lessons Learned from Graph-Based Online
Attribution Modeling," ScienceDirect, 2016.
https://www.sciencedirect.com/science/article/abs/pii/S0167811616300349
[8] Anindya Ghose and Vilma Todri-Adamopoulos, "Toward a Digital Attribution Model," JSTOR, 2016.
https://www.jstor.org/stable/26629681
[9] Darshil Gandhi, "A Beginner's Guide to Attribution Model Frameworks," Amplitude Analytics, 2024.
https://amplitude.com/blog/attribution-model-frameworks
[10] Randolph E. Bucklin, "A Model of Web Site Browsing Behavior Estimated on Clickstream Data,"
Sage journals, 2003. https://journals.sagepub.com/doi/10.1509/jmkr.40.3.249.19241
[11] Jeff Kupietzky, "What Is The Future Of Advertising In A Post-Cookie World?", Forbes, June 15,
2021. https://www.forbes.com/sites/forbesbusinesscouncil/2021/06/15/what-is-the-future-of-
advertising-in-a-post-cookie-world/
[12] Udbhav Tiwari, "Privacy-Preserving Attribution: Testing for a New Era of Privacy in Digital
Advertising", Mozilla, August 22, 2024. https://blog.mozilla.org/netpolicy/2024/08/22/ppa-
update/
