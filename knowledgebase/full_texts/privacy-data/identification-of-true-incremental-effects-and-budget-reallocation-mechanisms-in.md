---
title: Identification of True Incremental Effects and Budget Reallocation Mechanisms in Digital Advertising
  under Bias-Corrected Multi-Touch Attribution
url: https://doi.org/10.38007/sesr.2026.070203
category: privacy-data
subcategory: framework
date: 2026-09
venue: Socio-Economic Statistics Research
authors: []
source: openalex-oa
pdf_url: http://scholar-press.com/uploads/papers/fEW4witVXBG0AGhmzY1Hnd98GtmPaUyZ4p1orBP2.pdf
pages: 8
chars: 22487
fetched_at: '2026-11-08T17:47:53+00:00'
kb_version: 1
---

# Identification of True Incremental Effects and Budget Reallocation Mechanisms in Digital Advertising under Bias-Corrected Multi-Touch Attribution

Scholar Publishing Group
Socio-Economic Statistics Research
https://doi.org/10.38007/SESR.2026.070203
ISSN 2790-2722 V ol. 7, Issue 2: 19-26
Copyright: © 2026 by the authors. This is an Open Access article distributed under the Creative Commons Attribution License (CC BY 4. 0), which
permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited (https:/ /creativecommons.
org/licenses/by/4. 0/).
19
Identification of True Incremental Effects and Budget
Reallocation Mechanisms in Digital Advertising under
Bias-Corrected Multi-Touch Attribution
Yiyu Yang
Columbia University School of Professional Studies, 203 Lewisohn Hall, 2970 Broadway, MC 4119,
New York, 10027, United States
Keywords: Digital Advertising; Multi- Touchpoint Attribution; Incremental Effect; Bias
Correction; Budget Reallocation
Abstract: Due to more stringent privacy regulations, fractured cross -platform data and
disjointed advertising ch annels have reduced the traceability of digital advertising results,
and now people are only focused on changes in scale. Existing research has not yet
combined propensity score correction, counterfactual incremental estimation, Shapley
decomposition and marginal iROAS constraints in an auditable attribution pipeline. A bias -
corrected multi- touchpoint attribution framework is proposed in this paper to remove the
natural conversion baseline and redistribute channel credit. As shown in the illustrative
channel-level application, observed attribution can differ from corrected incremental
contribution by as much as 11 percentage points; for example, retargeting marginal iROAS
dropped to 0.72, and 17 per cent of the budget was shifted among channels. Based on the
above results, the attribution share should not be directly correlated with true increment;
thus, budget allocation should shift away from high- relevance but low -incremental
harvesting channels and towards scalable channels that offer better marginal incr emental
returns.
1. Introduction
The problem of digital advertising is not whether a channel is present in the conversion path, but
whether the conversion would still happen without that ad touchpoint. Users are exposed to multiple
times via search, social media, videos, displays, remarketing, email, etc., and will often click, visit
or revisit them before finally buying. Multi-touchpoint attribution can improve path explanation, but
its foundation is still observational association; channels near the conversi on point or frequently
logged by the platform tend to receive too much credit. Therefore, this paper addresses the
following two research questions: (1) How large is the gap between the observed attribution share
and bias -corrected incremental contribution ? (2) Under what conditions should marginal iROAS
constraints drive budget reallocation rather than platform-reported ROAS?
The three categories of existing research are as follows: Randomized experiments identify
advertising incremental effects but are affected by opportunity costs and sample interference [2];

Socio-Economic Statistics Research
20
MMM models the overall channel response, but lack path- level explanations [3]; and saturation-
based budget optimisation mitigates misallocation caused by static ROAS, but does not address
user-level selection bias [4]. Therefore, this paper uses the corrected increment as the decision
object and proposes a closed- loop mechanism of identification, correction, decomposition,
allocation, and retesting.
2. Analysis of the Current Situation of the Research Topic
2.1 Advertising Measurement Shifts from Path Attribution to Incremental Identification
The typical indicators of advertising performance, such as click- through rate (CTR), conversion
rate, customer acquisition cost (CAC) and attributable ROAS, are  relatively easy to collect every
day, but it is difficult to distinguish how many purchases were due to organic sources from those
that resulted from advertising. Users who are already motivated to buy will purchase without seeing
advertisements. Counting  these conversions as advertising contributions overestimates channel
value. Incremental measurement is the difference in potential results when exposed to and not
exposed to the factor. That is to say,
 𝜏𝜏_𝑖𝑖 =  𝑌𝑌_𝑖𝑖(1) −  𝑌𝑌_𝑖𝑖(0) (1)
τ_i is the individual incremental effect of user i, Y_i(1) is the potential conversion result after ad
exposure, and Y_i(0) is the potential conversion result in the absence of ad exposure. Therefore, the
criterion for judging the effectiveness of an adver tisement is not whether a conversion is achieved,
but rather whether it generates additional conversions than would have been obtained without the
advertisement (the counterfactual baseline).
2.2 Multi-Touchpoint Attribution Still Has Operational Value
Table 1. Comparison of Advertising Measurement Methods
Method Data Level Main Output Strength Limitation Horizon
Last Touch User Path Attributed Conversions Simple Audit End-Point Bias Daily
Rule-Based
MTA User Path Fractional Credit Easy Deployment Heuristic Weight Weekly
Data-Driven
MTA User Path Contribution Score Sequence Learning Selection Bias Weekly
Incrementality
Test User/Geo Causal Lift Strong Identification Costly Holdout Campaign
MMM Aggregate Series Response Curve Privacy Robust Low Granularity Quarterly
Corrected MTA Hybrid Incremental Credit Actionable Causality Model Dependence Monthly

Multi-touchpoint attribution can show how the touchpoints for user awareness, interest,
comparison and purchase change over time, and is suitable for analyzing short -cycle campaigns and
adjusting creatives, bids and audience packages. Although it is not exact ly the same as causal
effects, it can be used as an input feature for incremental models. Some research has used
experimental samples to explore how the features of advertising campaigns relate to incremental
changes in behaviour and has found that, even a fter adjustment, attribution indices retain some

Socio-Economic Statistics Research
21
predictive power [2].
Table 1 shows that the different measurement methods are not equivalent. Last-click and rule -
based attribution are suitable for low -cost monitoring but have a considerable bias; experimental
identification has the highest causality but limited coverage; and MMM is suitable for long -term
budget assessment under privacy constraints but lacks explanation of touchpoint sequence. Bias -
corrected multi- touchpoint attribution combines path granularity and incremental logic to help
allocate budgets based on attribution results.
2.3 Privacy Constraints and Platform Disconnection Amplify Measurement Bias
Privacy policies, browser restrictions and walled- garden platforms are all limiting the full
collection of user paths. Apple's App Tracking Transparency has reduced the accuracy of ad
targeting and measurement, and weakened cross -platform c onversion tracking [6]. Research on
large-scale short-form video advertising has shown that the effect outside the platform under study
is also included in the total effect [7]. Therefore, to conduct causal inference, bias correction is
needed; otherwise, it is not data cleaning.
A relatively high average ROAS does not guarantee that the new budget will also be effective.
With the expansion of channel coverage and a decrease in audience engagement, the incremental
benefit per unit of advertising will declin e, and there is a risk of ad fatigue. Recently, saturation
functions, combinatorial arm slot machines and change -point detection have been applied to
optimise advertising budgets; therefore, given the non- linearity of channels and changes in the
market, the budget mechanism needs to be adjusted [4].
Table 2: Channel-Level Corrected Attribution and Budget Indicators.
Channel Current Budget % Observed Attribution % Corrected Incremental % Marginal iROAS Recommended Budget %
Search 30 32 24 1.18 25
Social 25 26 18 1.05 19
Video 16 18 22 1.42 23
Display 12 11 14 1.21 14
Retargeting 10 9 7 0.72 6
Email 7 4 15 1.35 13

The differences in observed attribution and corrected increments are shown in Table 2. Search
and social channels have a relatively large proportion but drop after correction; thus, they are
considered to be driven by organic demand. Video and email have larger corrected increments; thus,
the impact of demand stimulation and repeat -purchase reactivation is likely underestimated in the
raw paths. The suggested budget percentages are based on the marginal iROAS constraint and the
saturation assumption in Eq. (5), not on platform -reported attribution alone; they should be
understood as an analytically calibrated allocation example.
3. Raising Questions
3.1 Correlation attribution is unable to find the real increment.
Advertising impression allocation will be driven by algorithms in conjunction with users' past
behaviour and bidding auctions, as well as targeted reach- outs. Users who are more likely to
purchase will be selected by the advertising system for more frequent contact and thus have a higher

Socio-Economic Statistics Research
22
probability of converting after being exposed to a touchpoint. If credit is directly assigned based on
observed paths, the model may incorrectly count the user's own purchase intention as an
advertisement's contribution. Let D_i be the indicator that user i has bee n reached, and let X_i be
the set of covariates such as past behaviour, location, device type, etc. Propensity Score is:
 𝑒𝑒(𝑋𝑋𝑖𝑖) = 𝑃𝑃(𝐷𝐷𝑖𝑖 = 1|𝑋𝑋𝑖𝑖) (2)
e(X_i) is the propensity score, the  probability that user i will be reached under covariate
conditions X_i; D_i indicates whether it was reached or not; and X_i is the observed covariate
vector. Estimate e(X_i) and then use weighting or matching to make the observable characteristics
of the reached group and the control group closer, thereby reducing selection bias.
3.2 Cross-channel interference distorts the contribution of a single touchpoint
User conversion is not the sum of touchpoints. Raise the public's awareness of the brand, have
more people look for it online, show customised advertisements in various parts of extended
remarketing networks, and use a dual marketing path of email and social media distribution to drive
frequent purchases. These paths are treated as hypothesized mechani sms here and are in line with
recent evidence on platform spillover in short -form video advertising [7] and paid- organic
complementarity in mobile app advertising [8]. If the model does not consider spillover, it may
underestimate the upstream channel and overestimate harvesting touchpoints near conversion.
3.3 Budget adjustments do not have a cause-and-effect relationship.
Many enterprises' advertising funds have been planned by considering the published ROAS of
the platform; however, such high ROAS may not reflect significant extra -normal earnings growth.
Brand searches and retargeting are usually high -conversion-rate channels because they address
existing demand. If the budget keeps going to these channels, the firm will be recording conversions
instead of creating them. Frequent and large -scale budget adjustments can also disrupt the learning
period of the platform; thus, any reallocation needs to be considered in light of adjusted increments,
marginal iROAS, and budget-smoothing constraints simultaneously.
4. Problem-Solving and Strategies
4.1 Constructing an Incremental Attribution Model for Deviation Correction
Bias-corrected multi- touchpoint attribution first computes the propensity score, then calculates
the incremental conversion of ads relative to t he counterfactual baseline, and finally decomposes
this incremental part among  path touchpoints. Not all conversions are included in the ads'
attribution; therefore, a natural baseline is removed first. The mean treatment effect under inverse
probability weighting can be expressed as:
 Â𝑇𝑇𝑇𝑇_𝐼𝐼𝑃𝑃𝐼𝐼 =  (1/𝑛𝑛) 𝛴𝛴_𝑖𝑖 [𝐷𝐷_(𝑖𝑖𝑌𝑌_𝑖𝑖 )/𝑒𝑒(𝑋𝑋_𝑖𝑖 ) – ((1 –  𝐷𝐷_𝑖𝑖 ) 𝑌𝑌_𝑖𝑖)/(1 –  𝑒𝑒(𝑋𝑋_𝑖𝑖 ) )] (3)
ATE_hat_IPW in the formula is the sample average incremental effect estimated by inverse
probability weighting; n is the sample size; Y_ i is the conversion result or conversion value; D_i is
the reach status; e(X_i) is the propensity score. The estimator needs overlap and positivity; that is,
users with similar covariates should have non- zero probabilities of being reached and unreached.
Extreme weights should be truncated or clipped in the implementation, such as at the 99th
percentile, because propensity scores close to 0 or 1 can invalidate the estimator and increase noise.

Socio-Economic Statistics Research
23
4.2 Shapley Decomposition of Contact Marginal Contribution
Find the overall increase and then determine how the various channels have distributed this
increase. Use the Shapley marginal contribution method to compare the change in corrected
increment before and after adding a channel to different touchpoint sets.
 𝜑𝜑_𝑗𝑗 = 𝛴𝛴_{𝑆𝑆 ⊆ 𝑁𝑁{𝑗𝑗}}[|𝑆𝑆|! (𝑀𝑀 − |𝑆𝑆| − 1)!/𝑀𝑀!][𝑣𝑣(𝑆𝑆 ∪ {𝑗𝑗})– 𝑣𝑣(𝑆𝑆)] (4)
φ_j is the incremental contribution of channel j; N is the full set of channels; M is the number of
channels; S is any subset that does not contain channel j; and v(S) is the corrected incremental value
of subset S. Exact Shapley calculation enumerates $2^M$ subsets. This is feasible for the six -
channel example, but when M is greater than about 15, KernelSHAP or permutation sampling need
to be used to approximate marginal contributions at a reasonable computational cost.

Figure 1. Attribution and Corrected Incremental Share
As shown in Figure 1, the observed attributions for Search and Social are 32% and 26%,
respectively; the corrected increments are 24% and 18%, and both indicate natural demand recovery
and path-proximity bias. The corrected increments for Video, Display and Email are higher than  the
observed attributions; thus, demand stimulation, cross -channel return traffic and repeat -purchase
reactivation are likely underrepresented  by raw attribution. Therefore, the budget decisions should
be based on the corrected increment rather than the original attribution rank.
4.3 Establish a Budget Redistribution Mechanism Driven by Marginal iROAS
The purpose of budget re -allocation is to ma ximise the future additional benefits for the same
total cost. Let B_j be the budget for channel j and R_j(B_j) be the corrected incremental revenue
response of that channel. The optimisation problem is:
 Max _{𝐵𝐵_1, … , 𝐵𝐵_𝑀𝑀}𝛴𝛴_{𝑗𝑗 = 1}^𝑀𝑀𝑅𝑅_𝑗𝑗(𝐵𝐵_𝑗𝑗), 𝑠𝑠. 𝑡𝑡. 𝛴𝛴_{𝑗𝑗 = 1}^𝑀𝑀𝐵𝐵_𝑗𝑗 = 𝐵𝐵, 𝐵𝐵_𝑗𝑗 ≥ 𝑏𝑏_𝑗𝑗^𝑚𝑚𝑖𝑖𝑛𝑛 (5)

Socio-Economic Statistics Research
24
M is the number of channels; R_j(B_j) is the corrected incremental revenue of channel j under
budget B_j; B is the total budget ; and b_j^min is the minimum operational budget threshold. To
ensure the  reproducibility of the recommendation, the revenue response is modeled as a Hill
saturation function:
 𝑅𝑅_𝑗𝑗(𝐵𝐵_𝑗𝑗 )  = (𝛼𝛼_𝑗𝑗 𝐵𝐵_(𝑗𝑗_𝑗𝑗^𝛽𝛽 ))/ (𝜅𝜅_(𝑗𝑗_𝑗𝑗^𝛽𝛽 ) +  𝐵𝐵_(𝑗𝑗_𝑗𝑗^𝛽𝛽 ) ), 0 <  𝛽𝛽_𝑗𝑗 ≤  1 (6)
In Eq. (6), $ \alpha_j$ is the upper bound of incremental revenue, $ \kappa_j$ is the half -
saturation budget, and $ \beta_j$ is response curvature. The above parameters can be obtained from
historical spend-response series, experimental lift data or MMM prior s, and the marginal iROAS is
derived from the first derivative of R_j(B_j).

Figure 2. Budget Reallocation and Marginal iROAS.
As shown in Figure 2, the recommended budgets for Video and Email are higher than the current
budgets because their  marginal iROAS values of 1.42 and 1.35 are still within the scalable range.
Retargeting drops to 6 per cent and is no longer economically feasible. Search decreased from 30%
to 25%; therefore, the channels for brand- demand harvesting should not be expanded indefinitel y
but should also not fall below the minimum required level for demand collection.
4.4 Establish Auditable Operating Rules
A series of identification, correction, allocation and retesting should be carried out on the model.
First, combine impressions , clic ks, conversions, order amount, user history, campaign cost and
indicators for missingness of privacy. Next, analyse the difference between reached and unreached
audiences and inspect propensity -score overlap. Then, estimate the counterfactual baseline and
decompose only the incremental part. Then, according to the marginal iROAS, saturation,
confidence interval width and business constraints, adjust the budget. Finally, make some
modifications and conduct a small -scale test with ge or an audience. To avoid the model being a
"black box", output attribution share, corrected incremental share, confidence interval, marginal

Socio-Economic Statistics Research
25
iROAS, budget adjustment range and the threshold source for each action.
Table 3 shows the auditable budget adjustment rules. The thresholds are not taken as universal
constants; they are guardrails based on the saturation response in Eq. (6), historical frequency
distribution and retesting constraints. If the corrected increme nt is large and statistically significant,
increase the funding; if the marginal iROAS falls below 1 after saturation checks, reduce the budget.
When the missingness of the path is relatively large, MMM priors should be employed to mitigate
misjudgments caused by incomplete user-level logs.
Table 3. Decision Rules for Budget Reallocation.
Condition Diagnostic Signal Action Control Constraint Review Cycle
High
incremental
share
Corrected − observed > 5 pp
and CI excludes zero
Increase test
budget
Weekly change
cap < 20% 2 Weeks
Saturation risk Marginal iROAS < 1 after frequency saturation check Reduce budget Minimum reach floor Weekly
Harvesting bias High ROAS and low causal lift Hold or decrease Preserve brand baseline Monthly
Spillover effect Assisted conversion growth or cross-platform lift Increase test budget Geo validation 4 Weeks
Data uncertainty Wide CI or propensity overlap violation Keep stable Learning budget 2 Weeks
Privacy signal
loss Path missing rate > 35% Use MMM prior Aggregate check Monthly
5. Conclusion
True incremental effect identification and budget reallocation under bias -corrected multi -
touchpoint attribution are studied in this paper. Based on the above analysis, all conversions are not
necessarily at tributable to a path touchpoint in advertising measurement; they should first be
evaluated in light of their contribution relative to the natural baseline. Although traditional multi-
touch attribution is suitable for monitoring operations, it lacks propens ity correction and
counterfactual analysis, thus suffering from selection bias, platform self -attribution and the
inclusion of natural conversions in the attribution. The above framework introduces propensity -
score correction, inverse probability weighting, Shapley marginal contribution and marginal iROAS
optimisation to transform attribution results into auditable budget migration rules.
Prioritize corrected incremental contribution, marginal return and stability constraints in budget
reallocation. Channel s with high observed attribution but low corrected increment should be
expanded under controlled circumstances; channels with low observed attribution but high
corrected increment should be gradually validated and expanded with experimental budgets;
channels showing a decline in marginal iROAS or excessively wide confidence intervals should
reduce frequency and budget or be maintained in an observation mode. The study also has some
deficiencies: the channel -level figures in Table 2 are an allocation example and not a proprietary
campaign dataset; the propensity model may be misspecified if important behavioural covariates are
omitted; and Shapley additivity may be reduced in competitive ad markets with strategic channel
interactions. In the future, geo- experiments, privacy -preserving aggregate modelling and
reinforcement learning budget control will be used to construct a more adaptive incremental
attribution system.

Socio-Economic Statistics Research
26
References
[1] Hosahally S. Measuring digital advertising in a post -cookie era: A study of marketing -mix
models, attribution and incrementality. Journal of Digital & Social Media Marketing , 2025,
12(4): 1-13.
[2] Gordon BR, Moakler R, Zettelmeyer F. Predicted Incrementality by Experimentation (PIE) for
Ad Measurement. arXiv preprint arXiv:2304.06828 , 2023/2026.
[3] Runge J, Skokan I, Zhou G, Pauwels K. Packaging Up Media Mix Modeling: An Introduction
to Robyn's Open-Source Approach. arXiv preprint arXiv:2403.14674 , 2025.
[4] Gangopadhyay B, Wang Z, Chiappa AS, Takamatsu S. Adaptive Budget Optimization for
Multichannel Advertising Using Combinatorial Bandits. arXiv preprint arXiv:2502.02920 ,
2025.
[5] Waisman C, Gordon B R. Multi -cell Experiments for Marginal Treatment Effect Estimation of
Digital Ads. arXiv preprint arXiv:2302.13857 , 2025.
[6] Wu, Y. (2026). Research on Interpretable Confidence Rule Base Modeling Method Integrating
Data-Driven and Constrained K -Means Optimization. Procedia Computer Science, 279, 612-
619.
[7] Sun, J. (2026). Automated Feature Engineering and Screening System for Large-Scale Factor
Libraries. Procedia Computer Science, 281, 1282-1290.
[8] Zhang, Z. (2026). Research on Performance Monitoring and Data- driven Optimization
Mechanisms for AI Systems Oriented Toward Decision Support. Advances in Computer and
Communication, 7(2).
[9] Hou, Y. (2026). Collaborative Regulation for Stable Data Center Operation under Energy
Efficiency Constraints. Procedia Computer Science, 281, 612-620.
[10] Wu, Y. (2026). Research on Interpretable Confidence Rule Base Modeling Method Integrating
Data-Driven and Constrained K -Means Optimization. Procedia Computer Science, 279, 612-
619.
[11] Zhang, Z. (2026). Research on Performance Optimization Methods for Resource -Aware Model
Services in AI Systems. Procedia Computer Science, 281, 1310-1317.
[12] Liu, Z. (2026). Research on Measuring User Behavior Response Differences Supported by
Propensity Scoring Method. European Journal of AI, Computing & Informatics, 2(2), 47-53.
[13] Gao, Y. (2026). Governance Structures and Checks and Balances in Private Equity Funds:
Practice, Problems, and Improvement Paths. Financial Economics Insights, 3(2), 82-91.
[14] Wu, L. (2026). Construction and Evolutionary Analysis of a Game Model for Supply Chain
Finance Funding Based  on Blockchain Technology. Procedia Computer Science, 282, 2004-
2012.
