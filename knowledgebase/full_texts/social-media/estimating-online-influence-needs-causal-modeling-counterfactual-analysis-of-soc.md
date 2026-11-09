---
title: Estimating Online Influence Needs Causal Modeling! Counterfactual Analysis of Social Media Engagement
url: https://arxiv.org/abs/2505.19355
category: social-media
subcategory: empirical
date: 2025-05
venue: ''
authors:
- Lin Tian
- Marian-Andrei Rizoiu
source: arxiv
pdf_url: https://arxiv.org/pdf/2505.19355
pages: 19
chars: 68267
fetched_at: '2026-11-08T13:04:05+00:00'
kb_version: 1
---

# Estimating Online Influence Needs Causal Modeling! Counterfactual Analysis of Social Media Engagement

arXiv:2505.19355v1  [cs.CL]  25 May 2025
Preprint. Under review.
Estimating Online Influence Needs Causal Modeling!
Counterfactual Analysis of Social Media Engagement
Lin Tian & Marian-Andrei Rizoiu
University of Technology Sydney
{Lin.Tian-3,Marian-Andrei.Rizoiu}@uts.edu.au
Abstract
Understanding true influence in social media requires distinguishing corre-
lation from causation—particularly when analyzing misinformation spread.
While existing approaches focus on exposure metrics and network struc-
tures, they often fail to capture the causal mechanisms by which external
temporal signals trigger engagement. We introduce a novel joint treatment-
outcome framework that leverages existing sequential models to simulta-
neously adapt to both policy timing and engagement effects. Our approach
adapts causal inference techniques from healthcare to estimate Average
Treatment Effects (ATE) within the sequential nature of social media interac-
tions, tackling challenges from external confounding signals. Through our
experiments on real-world misinformation and disinformation datasets,
we show that our models outperform existing benchmarks by 15-22% in
predicting engagement across diverse counterfactual scenarios, including
exposure adjustment, timing shifts, and varied intervention durations. Case
studies on 492 social media users show our causal effect measure aligns
strongly with the gold standard in influence estimation, the expert-based
empirical influence.
1 Introduction
In March 2020, as COVID-19 began its global spread, a simple graphic titled “Flatten the
Curve” created by Associate Professor Siouxsie Wiles and cartoonist Toby Morris ignited an
unprecedented cascade of social media engagement1. Within just 72 hours, the visualization
accumulated over 10 million impressions on X (formerly Twitter), was translated into more
than 25 languages, and was adopted by government health agencies worldwide (Bavel
et al., 2020). What made this particular content achieve such extraordinary reach was not
merely its clear visualization of pandemic dynamics—it was the complex interplay between
its timely release amid escalating global concern, amplification by influential public health
accounts, and concurrent spikes in search traffic as reflected in Google Trends data (Jackson
et al., 2020). As the graphic’s engagement metrics surged, a corresponding peak in “social
distancing” searches appeared across global search indices, preceding measurable changes
in mobility patterns across affected regions (Gao et al., 2020). Today, with hindsight, we say
that the “Flatten the Curve” graphic was influential as it increased the public’s awareness of
non-pharmaceutical interventions for the COVID-19 pandemic.
But what is influence? It is more than exposure or virality; it is one’s capacity to shape
attitudes and change behaviors. And while exposure (particularly repeated exposure) and
influence are intimately linked, true influence estimation require causal reasoning. This
causal perspective on influence has been established in seminal works across multiple disci-
plines (Aral et al., 2009; Eckles et al., 2016; Watts et al., 2021), which collectively demonstrate
that traditional influence measures often conflate homophily with causal effects. In online
social media, information cascades equate to exposure—they are the digital equivalent
of the word-of-mouth phenomenon that allow content to spread widely. But how do they
relate to influence? This paper introduces a causal framework to estimate user influence by
1https://www.washingtonpost.com/graphics/2020/world/corona-simulator/
1

Preprint. Under review.
conducting counterfactual analysis on misinformation and disinformation cascades. This
would allow us to understand which users, public groups or pages are truly shaping public
discourse on highly polarizing topics, and who does truly drive misinformation spread.
True influence is unobserved, and notoriously difficult to estimate (Ram & Rizoiu, 2024). We
therefore train and test our models on observed exogenous attention signals—like search
trends, news coverage cycles, or influencer amplification—and ask how do they causally
impact content engagement and information diffusion. While existing engagement pre-
diction approaches have made significant progress using content features and network
structure (Zhou et al., 2021a), they typically overlook the causal relationship between exter-
nal temporal signals and engagement dynamics. Moreover, previous studies on influence
measurement in social media have often focused on exposure rates and network structures
but have not fully incorporated a causal perspective (Cha et al., 2010; Bakshy et al., 2011;
Kwak et al., 2010). Similarly, causal inference frameworks in machine learning (Pearl, 2009;
Peters et al., 2017) generally lack the temporal sophistication needed to model the intricate
dependencies between time-varying external signals and sequential engagement outcomes.
To tackle these challenges, we introduce a causal framework that jointly models treatment
intensities – external signals driving engagement – and social engagement outcomes. Our
approach builds on advances in sequential modeling, adapting transformer architectures
(Vaswani et al., 2017) and selective state space models (e.g., Mamba (Gu & Dao, 2024))
to meet the demands of causal inference with time-varying treatments. By comparing
integration mechanisms – token-based, attention-based, layer-based, and adapter-based –
we present detailed insights into the architectural requirements for effective causal modeling
in social media contexts, particularly in scenarios involving misinformation.
This work explores three key research questions: (1) Does joint modeling of treatment inten-
sities and outcomes improve predictive accuracy under realistic policy-driven scenarios,
especially those aimed at curbing misinformation? (2) How effectively do transformers and
state space models capture the intricate temporal dependencies between external signals and
engagement outcomes? (3) How reliably can these models predict engagement outcomes
under hypothetical scenarios, such as changes in exposure rates or policy active timings?
2 Problem Statement
Let E denote a social media event with associated posts P = {p1, p2, . . ., pN}. For each post
p ∈ P, we define a tuple (t0, x, u, o, H) where t0 is the original posting time, x represents
the textual content, u captures user metadata, o ∈ Oindicates the content category from
the set of possible categories O, and H = {(tj, ej)}m j=1 is the interval-censored engagement
history with m observation intervals. Each ej is a d-dimensional vector capturing different
types of engagement (likes, shares, comments, etc.) at observation time tj.
The Google Trends information is a set of tuples G = {(tk, gk)}l k=1, with gk as a scalar representing the search intensity of keywords related to the post’s content (e.g., a spike in
searches for “election” for a political post) at time tk. These signals, collected over l time
points, serve as an exogenous signal, capturing how real-world interest.
Given an observation window τobs starting at t0, let Hτobs (p) = {(t, e) ∈ H | t0 ≤ t ≤
t0 + τobs} represent the post’s initial engagement history, and Gτobs = {(t, g) ∈ G | t0 ≤ t ≤
t0 + τobs} as the corresponding external signals. The goal is to predict the future engagement
trajectory under policy-driven modifications to the external signal patterns (e.g., adjusting
Google Trends intensity to reflect shifts in public attention). Specifically, we aim to forecast
{ ˆe(t0 + τobs + k∆t)}K k=1, where ∆t is a fixed time step (e.g., one day), and K = ⌊T/∆t⌋ is the number of prediction points over a horizon T (e.g., one month).
3 Methodology
Our framework (as shown in Fig. 1) models external signals as continuous-intensity treat-
ments through modeling that capture both immediate responses and long-range dependen-
2

Preprint. Under review.
0 1 2 3 4 5 6 7010
20
3040
50
Time, t (days)
# Engagement
Engagement oobs
Events aobs
0 1 2 3 4 5 6 70
24
6
810
Time, t (days)
# Engagement
Likes Shares
Comments Emojis
0 2 4 6 7 8 10 12 140
30
60
90120
150
Time, t (days)
Engagement f
fobs fpred
fπA
0 2 4 6 7 8 10 12 140
0.20.4
0.6
0.81
Time, t (days)
Intensity λ
λobs [πA]
0 2 4 5 6 7 8 10 12 140
30
60
90120
150
Time, t (days)
Engagement f
fobs fpred
fπA fπB
0 2 4 5 6 7 8 10 12 140
0.20.4
0.6
0.81
Time, t (days)
Intensity λ
λobs [πB]
(a) Observational data (b) Exogenous signals (c) Counterfactual signals
Figure 1: Visualization of engagement data and queries for social media post p. (a) Observa-
tional data during the period [0, 7] days. The top plot shows cumulative engagement over
time (black line with crosses) and observed events (cyan dots). The bottom plot displays in-
dividual engagement metrics: Likes (blue crosses), Shares (red squares), Comments (brown
triangles), and Emojis (purple diamonds). (b) The exogenous signal. The engagement
trajectory of post p after the observation period under policy πA, derived from Google
Trends data, with a one-day exposure time (shaded area from day 7 to 8). The top plot
shows observed engagement (solid blue line), predicted engagement without intervention
(dashed blue line), and predicted engagement under πA (dashed red line). The bottom
plot displays normalized intensity λobs (dashed green line), policy πA intensity (dashed
red line), observed events (cyan dots), and policy actions (magenta dots). A vertical line
at day 7 marks the intervention start. (c) The counterfactual signal. How the engagement
trajectory of post p would have evolved if policy πB had been applied during [0, 7] with
a three-day exposure time (shaded area from day 7 to 10). The top plot shows observed
engagement (solid blue line), predicted engagement without intervention (dashed blue line),
predicted engagement under πA (dashed red line), and counterfactual engagement under
πB (solid orange line). The bottom plot displays normalized intensity λobs(dashed green
line), counterfactual policy πB intensity (dashed orange line), observed events (cyan dots),
and policy actions (magenta dots). A vertical line at day 7 marks the intervention start.
cies. We achieve this by jointly modeling the bidirectional relationship between external
signals and engagement outcomes.
3.1 Joint Treatment-Outcome Model
Inspired by the causal modeling framework of Hızlı et al. (2023), we propose a joint
treatment-outcome model tailored for predicting social engagement in discrete-time social
media data. While Hızlı et al. (2023) use marked point processes for treatment intensity
and conditional Gaussian processes for continuous-time outcomes, we adapt this approach
to discrete time using deep sequential models. This adaptation improves scalability and
flexibility for large-scale, irregularly sampled social media datasets while preserving the
bidirectional dependency between treatments (external signals) and engagement outcomes.
Treatment Intensity Modeling We model treatment intensity λ∗ π(t) as the probability of
a binary treatment event (e.g., a Google Trends spike) at each discrete time step t. The
3

Preprint. Under review.
intensity is computed via a square transformation of a latent function g∗ π(t):
λ∗ π(t) =  β0 + gb(t) +g∗ a (t) +g∗ o (t) +g∗ g(t) 2 ,
where β0 represents a constant baseline intensity, gb(t) is a time-dependent baseline func-
tion, g∗ a (t) models dependence on past treatments, g∗ o (t) captures dependence on past
engagement outcomes, and g∗ g(t) incorporates Google Trends intensity.
For g∗ g(t), we use discrete-time window sampling at 10-minute intervals (∆g = 10 minutes):
g∗ g(t) =
w−1
∑
k=0
αk · g(t − k∆g) · 1[t−k∆g,t−(k−1)∆g)(t),
Here, w is the number of historical windows considered, g(t − k∆g) is the Google Trends
value at time t − k∆g, αk are learnable decay coefficients, and1[a,b)(t) is an indicator function.
λ∗ π(t) is evaluated at discrete time steps, with treatments sampled as binary events based
on this probability.
To align Google Trends with engagement observations, we implement a temporal alignment
mechanism. For each observation time tj, we collect signals within a lag window:
G(tj) ={gk | tj − τlag ≤ tk < tj}
where τlag is a hyperparameter determined through cross-validation. The resulting feature
vector is vg(tj) = [g(tj − ∆g), g(tj − 2∆g), . . . ,g(tj − w∆g)].
3.2 Causal Assumptions
Our causal framework relies three key assumptions suitable for social media contexts:
Assumption 1 (Consistency). The potential engagement outcome Y[a] under a specific pattern of
external signals a equals the observed engagement Y when those exact signals actually occur.
This assumes observed Google Trends-engagement relationships persist if patterns reoc-
cur. In social media environments, this consistency is supported by the relative stability
of engagement mechanisms—including recommendation algorithms, user interfaces, and
notification systems—which function as reliable mediators between external signals and
user behavior (Becker et al., 2017). Empirical evidence from Calderon et al. (2024) reinforces
this view, as their Opinion Market Model (OMM) incorporating Google Trends signals
consistently outperformed baselines in predictive accuracy by approximately 17% lower
error rates. Similarly, Rizoiu et al. (2017) demonstrated superior popularity prediction
results with their HIP model by assuming that viewcount is externally driven by sharing
behavior (Muchnik et al., 2013) and explicitly accounting for that as an exogenous driver.
They prove that HIP has the Linear Time-Invariant property which ensures that identical
external stimuli produce consistent engagement responses regardless of when they occur.
While acknowledging temporal constraints, we assert this assumption holds within reason-
able timeframes where platform mechanics and user behavior patterns remain stable, prior
to significant algorithm updates or shifts in engagement norms.
Assumption 2 (Fully-Mediated Policy Effect). External signals (like Google Trends spikes) affect
engagement outcomes through observable mechanisms rather than hidden pathways.
This assumption states that external signals (like Google Trends spikes) affect engagement
outcomes through observable mechanisms rather than hidden pathways (Bakshy et al.,
2015). The causal process operates through a well-defined mediational sequence: exogenous
search intensity signals → heightened topical salience → content exposure via platform
mechanisms → measurable engagement behaviors (e.g., likes, shares, comments). Calderon
et al. (2024) empirically validated this pathway, showing that external signals affect both the
attention market size and opinion distribution. Similarly, Bakshy et al. (2015) provide further
evidence by showing how exposure mechanisms directly mediate the relationship between
content availability and user engagement with diverse information. Rizoiu et al. (2017)
4

Preprint. Under review.
0 2 4 6 8 10 12 140
0.20.4
0.6
0.81
Time, t (days)
Intensity λ
Base-full
0 2 4 6 8 10 12 140
0.20.4
0.6
0.81
Time, t (days)
Base-null
0 2 4 6 8 10 12 140
0.20.4
0.6
0.81
Time, t (days)
CF1-3: 60% dropout rate
0 2 4 6 8 910 12 140
0.20.4
0.6
0.81 CF2-1
CF2-2
CF2-3
Time, t (days)
Intensity λ
CF2: Temporal alignment shift
0 2 4 6 8 910 12 140
0.20.4
0.6
0.81 CF3-1
CF3-2
CF3-3
Time, t (days)
CF3: Signal duration
λobs
[ ˜πB] (partial)
[πB] (signal variant 1)
[πB] (signal variant 2)
[πB] (signal variant 3)
Figure 2: Engagement trajectory and counterfactual scenarios. Blue dashed lines represent
observed social media engagement (λobs). Red lines indicate Google Trends signals ([πB]).
˜πB as the partial observed Google Trends signals. The vertical dashed line at day 9 marks
the start of prediction period, with the gray shaded area showing the prediction region.
quantifies this relationship through their “popularity impulse response” function, measuring
how external signals directly translate to viewership through measurable platform dynamics.
Their simulated intervention experiments show that media coverage predictably shapes
opinion market shares through these mechanisms. While alternative pathways might
exist–such as algorithmic amplification or coordinated network activity–these appear to be
minimal, as evidenced by both OMM’s and HIP’s superior predictive performance when
directly modeling this attention-mediated relationship.
Assumption 3 (Temporal Precedence). Causes precede effects - current engagement can be
influenced by past external signals but not by future ones.
This assumption aligns with the natural temporal ordering of social media interactions,
where content engagement follows rather than precedes external attention signals. Rizoiu &
Xie (2017a) provide strong empirical support through their temporally-sensitive Hawkes
Intensity Process model, which demonstrates that popularity dynamics strictly follow the
causal direction where external stimuli (like promotions) at timet can only influence engage-
ment at times τ > t, with a clear measurable maturity time quantifying this temporal lag.
This maturity time metric captures the delay between external stimuli and the resulting en-
gagement effects, providing a quantitative measure of the temporal precedence relationship.
Their model’s success in predicting YouTube viewcounts using this temporal framework
validates the directional nature of the causal relationship. Similarly, Calderon et al. (2024)
validate this in their Opinion Market Model, showing improved predictive performance
when treating search trends as antecedent to engagement spikes. This temporal structure
is further reinforced by platform mechanics, as content discovery algorithms typically re-
spond to rising search interest by increasing content visibility, creating a causal chain that is
unidirectional in time (Centola et al., 2018).
These assumptions, while not exhaustively verifiable, provide a reasonable foundation for
causal inference in social media settings and allow us to identify treatment effects from
observational data. Thus, building on the potential outcomes framework, we formulate our
causal inference approach to estimate the effects of interventions on engagement trajectories.
3.3 Counterfactual Analysis
We introduce a counterfactual analysis framework that systematically manipulates exoge-
nous signals along the temporal dimension to understand their causal impact on engagement
dynamics, as shown in Figure 2. Formally, a counterfactual scenarioC as a transformation of
5

Preprint. Under review.
the Google Trends signal G = {(tk, gk)}l k=1 through a temporal manipulation function Ψθ:
GC = Ψθ(G) ={(tk + δθ(tk, gk), gk · γθ(tk, gk))}l k=1,
where δθ shifts the timing of signals and γθ adjusts signal intensity, enabling three coun-
terfactual scenarios (CF): Dropout Rate (CF1) adjusts intensity ( γθ) to explore exposure
effects (0% →20% as CF1-1, 20%→40% as CF1-2, 40%→ 60% as CF1-3); Temporal Align-
ment Shifts (CF2) the onset timing (δθ) of a fixed-duration signal to test sensitivity to early
exposure; Signal Duration Manipulation (CF3) modifies persistence to evaluate sustained
attention effects (1-day as CF3-1, 3-day as CF3-2, 5-day as CF3-3). For each counterfactual
scenario, we estimate the expected engagement outcomes under the transformed signal and
calculate the causal effect as the difference between counterfactual and actual outcomes:
∆C = E[Y|GC ] − E[Y|G].
3.4 Model Training and Optimization
We train our joint model using a combined loss function that explicitly optimizes both
treatment intensity modeling and outcome prediction:
Ljoint = MSE(Ytrue(t), Ypred(t; θY)) | {z }
Outcome Loss
+α BCE(Atrue(t), λA(t; θA))| {z }
Intensity Loss
, (1)
where α is a hyperparameter controlling the relative importance between accurate outcome
prediction and accurate treatment intensity modeling. This joint optimization ensures that
the model captures both the occurrence pattern of external signals (treatments) and their
effects on engagement outcomes.
For the Mamba-based model, we additionally incorporate a temporal coherence loss,
which ensures consistent state transitions across varying time intervals with Ltemp =
1
|P |∑p∈P ∑m−1 j=0 ∥hj+1 − exp(∆t+ j · ˜At)hj∥2. The temporal coherence loss regularizes the hid-
den state dynamics to follow the theoretical state transitions defined by the continuous-time
state space model, where hj is the hidden state at time tj, ∆t+ j = tj+1 − tj is the forward time
interval, and exp(∆t+ j · ˜At) represents the state transition matrix over the interval ∆t+ j . By
minimizing this loss, we ensure that the model maintains consistent internal representations
despite the irregular sampling intervals.
For the transformer-based model, we replace the temporal coherence loss with an attention
consistency loss that encourages similar attention patterns for events with similar tem-
poral relationships with Latt = 1 |P |∑p∈P ∑i,j,k,l wijkl ∥Aij − Akl ∥2. where Aij represents the
attention weight from position i to position j, and wijkl is a similarity weight based on the
temporal distance between positions.
4 Experiment and Results
This section introduces the datasets, models and baselines, and report our experimental
findings on the optimal architecture choice for exogenously-driven engagement modeling.
4.1 Datasets
Social Media Engagement Data. The SocialSense dataset (Kong et al., 2022) is a misin-
formation dataset containing public Facebook posts collected between 2019 and 2021. It
spans four domains: Australian Bushfires (78,030 posts), Climate Change (138,278 posts),
Vaccination (178,894 posts), and COVID-19 (640,100 posts). These posts, labeled by domain
experts, focus on misinformation and conspiratorial discussions. User engagements (likes,
shares, comments, and emoji) were collected using the CrowdTangle API 2.
2https://www.crowdtangle.com/ before its termination in August 2024.
6

Preprint. Under review.
The DiN dataset (Tian et al., 2025) is a disinformation dataset comprising 746, 653 posts from
41 accounts from 2019 to 2024. It is identified by social science experts as part of coordinated
information operations. The posts are classified into 9 narratives based on the evaluation of
the content.
External Signal Data from Google Trends. We collected Google Trends data to provide
external signals aligned with both the temporal and thematic scope of the data sets. Key-
words—selected via frequency analysis of post content and expert consultation—were
theme-specific for SocialSense (e.g., “bushfire evacuation,” “climate hoax”) and narrative-
specific for DiN (e.g., “election fraud,” “deep state”). Using the Google Trends API 3, the
search information was retrieved via key phrases, normalized to 0–100, and retrieved at
10-minute intervals across the full temporal range of the social media datasets. These data
were processed in an external signal timeline G = (tk, gk)l k=1, where gk denotes the search interest at time tk, and aligned with each post using a temporal lag window τlag to model
potential causal influences on engagement.
4.2 Models and Baselines
We evaluate eight architectural variants, four Transformer-based and four Mamba-based,
each modified to incorporate external signals, with details in Appendix A.3.
Transformer-based Variants.We extend the Transformer (Vaswani et al., 2017) to model
external signals via: +Token embeds tokenized signals with engagement data for joint
self-attention; +Attention adds attention heads with custom masks for signal dependen-
cies; +Layer processes signals via MLP , integrating with sequences through cross-attention;
+Adapter inserts lightweight adapters (Houlsby et al., 2019) to model external signals.
Mamba-based Variants. We adapt Mamba (Gu & Dao, 2024), a selective state space model,
to incorporate signals via: +Token embeds tokenized signals with engagement data for
joint processing; +Selection conditions the selective scan on signal-engagement temporal
relationships; +Layer processes signals via MLP , integrating outputs into Mamba’s state;
+Adapter adds adapters to condition state transitions on signal intensities.
We compare against three baselines: vanilla TimeSeries Transformer, Mamba and MBPP (Ri-
zoiu et al., 2022), a marked point process that models engagement as a self-exciting process.
4.3 Results and Analysis
RQ1: Joint Modeling and Predictive Accuracy. Table 1 compares the performance of
architectural variants under counterfactual perturbations (see scenarios of Section 3.3).
Mamba+Adapter achieves the lowest RMSE (0.113) on baseline data, with selective state
space models effectively capturing temporal engagement dependencies. As exposure levels
increase, RMSE rises non-linearly, suggesting higher exposure renders engagement pat-
terns more predictable through stronger signal regularization. Experiments reveal a 1-3 day
optimal intervention window, with Mamba-based models handling temporally distant coun-
terfactuals better than Transformer variants. Extended policy durations challenge all models,
though Transformer+Adapter shows greater resilience to sustained signals. Appendix A.4
reveals disinformation (DiN dataset) poses greater challenges than misinformation, with
higher base RMSE and larger increases at 60% exposure, suggesting inherently greater
difficulty in predicting engagement with deliberately deceptive content.
RQ2: Architectural Differences in Temporal Causal Dependency Modeling. As shown in
Table 2, Mamba+Adapter outperforms other architectures in capturing treatment dynamics,
achieving the lowest BCE (0.35 at 60% exposure) with a 10.9% improvement over the
best Transformer variant. An inverse relationship emerges between treatment intensity
and modeling difficulty: BCE decreases from 0.488 to 0.350 as exposure rises from 20%
to 60%. This suggests that high-intensity external signals may be more consistent with
predictable patterns, offering potential for early detection of viral content trends. Temporal
misalignment further amplifies architectural differences. For 5-day early interventions,
3https://serpapi.com/google-trends-api
7

Preprint. Under review.
Table 1: Root Mean Squared Error (RMSE) of engagement prediction over a 7-day horizon
under counterfactual scenarios (see Section 3.3), averaged across two datasets. Base: Full
exposure to external signal. Scenario 1: varying exposure levels (20%, 40%, 60%); Scenario
2: altered treatment timing (-5, -3, -1 days); Scenario 3: different treatment durations (1, 3, 5
days). Lower RMSE indicates better performance. ‘*’ denotes no external signals.
Model Base Scenario 1: Exposure Scenario 2: Timing Scenario 3: Duration
20% 40% 60% -5 days -3 days -1 day 1-day 3-day 5-day
Transformer (Vaswani et al., 2017) 0.193* – – – – – – – – –
Mamba (Gu & Dao, 2024) 0.189* – – – – – – – – –
MBPP (Rizoiu et al., 2022) 0.193 0.326 0.295 0.281 0.225 0.225 0.226 0.329 0.315 0.284
Transformer + Token 0.128 0.214 0.220 0.225 0.210 0.203 0.197 0.238 0.245 0.250
Transformer + Attention 0.122 0.198 0.191 0.183 0.194 0.188 0.182 0.224 0.198 0.194
Transformer + Layer 0.125 0.202 0.194 0.187 0.198 0.192 0.186 0.228 0.202 0.198
Transformer + Adapter 0.115 0.190 0.183 0.176 0.186 0.180 0.175 0.216 0.190 0.186
Mamba + Token 0.129 0.205 0.197 0.190 0.201 0.195 0.189 0.245 0.225 0.218
Mamba + Selection 0.118 0.193 0.186 0.179 0.189 0.183 0.178 0.240 0.220 0.213
Mamba + Layer 0.120 0.195 0.188 0.180 0.191 0.185 0.179 0.242 0.222 0.215
Mamba + Adapter 0.113 0.185 0.178 0.171 0.181 0.176 0.170 0.236 0.218 0.210
Table 2: Binary Cross Entropy (BCE) evaluates treatment intensity prediction accuracy over
a 7-day horizon across counterfactual scenarios, averaged across two datasets. Lower BCE
reflects better modeling of temporal external signal patterns.
Model Scenario 1: Exposure Scenario 2: Timing Scenario 3: Treatment
20% 40% 60% -5 days -3 days -1 day 1-day 3-day 5-day
Transformer + Token 0.543 0.465 0.405 0.482 0.433 0.408 0.542 0.481 0.463
Transformer + Attention 0.510 0.421 0.378 0.450 0.390 0.352 0.533 0.465 0.446
Transformer + Layer 0.518 0.432 0.385 0.460 0.403 0.372 0.513 0.430 0.412
Transformer + Adapter 0.495 0.402 0.355 0.428 0.372 0.339 0.545 0.482 0.464
Mamba + Token 0.532 0.455 0.395 0.470 0.420 0.400 0.535 0.482 0.464
Mamba + Selection 0.502 0.413 0.368 0.435 0.378 0.346 0.535 0.470 0.454
Mamba + Layer 0.509 0.422 0.372 0.445 0.386 0.355 0.538 0.472 0.450
Mamba + Adapter 0.488 0.398 0.350 0.420 0.365 0.335 0.525 0.465 0.440
Mamba+Adapter demonstrates a 20.2% BCE advantage over Transformer+Token, showing
the strength of state space models in managing temporally shifted causal processes.
RQ3: Counterfactual Robustness and Reliability. Table 3 reveals distinct patterns in causal
relationships between external signals and engagement outcomes. The Mamba+Selection
configuration estimates the highest ATE (0.635 ± 0.135 for CF1-3, 40% → 60% exposure),
surpassing alternatives by 16.1%. This benefits from its selective scan algorithm, which is
good at isolating causally relevant temporal patterns. Exposure adjustment experiments
indicate a super-linear relationship between signal intensity and engagement impact: ATE
rises by 42.1% from 20%→ 40% (0.409) to 40%→ 60% (0.612) exposure levels, suggesting that
concentrated bursts of attention yield disproportionately high engagement returns. Timing
manipulations reveal a temporal window amplifying causal influence, with an average ATE
ratio of 1.55 between 1-day and 5-day early interventions across models, suggesting that
precise timing within narrower windows boosts engagement, informing optimal content
scheduling and promotion strategies. Having identified the optimal architectural choice—
Mamba+Adaptors, dubbed causal-Mamba—, we now turn to identifying causal influencers.
5 Case Study: Identifying Causal Influencers on Social Media
Causal effect influence. We use our causal-Mamba architecture to estimate the causal
influence of a source – users, public page and groups. We use the source’s posting behavior
as the causal treatment (compared to no exogenous signal), and we estimate its impact on
predicting engagement metrics (quotes, replies, retweets, favorites).
8

Preprint. Under review.
Table 3: Average Treatment Effect (ATE), computed via G-computation (Robins, 1986), quan-
tifies causal impacts of interventions over a 7-day horizon with 95% bootstrap confidence
intervals (±), normalized across four engagement metrics (likes, comments, emoji reactions,
shares). Higher ATE indicates stronger effects.
Model Exposure Adjustment Timing Adjustment Duration Adjustment
CF1-1
(0% → 20%)
CF1-2
(20% → 40%)
CF1-3
(40% → 60%)
CF2-1
(5-day early, day 0)
CF2-2
(3-day early, day 0)
CF2-3
(1-day early, day 0)
CF3-1
(1-day dur.)
CF3-2
(3-day dur.)
CF3-3
(5-day dur.)
Transformer+Token 0.173 ± 0.109 0.334 ± 0.181 0.496 ± 0.102 0.146 ± 0.075 0.188 ± 0.060 0.221 ± 0.054 0.162 ± 0.046 0.297 ± 0.086 0.425 ± 0.104
Transformer+Attention 0.180 ± 0.050 0.349 ± 0.083 0.523 ± 0.111 0.158 ± 0.083 0.202 ± 0.067 0.245 ± 0.057 0.172 ± 0.052 0.312 ± 0.090 0.456 ± 0.111
Transformer+Layer 0.161 ± 0.047 0.297 ± 0.075 0.443 ± 0.091 0.131 ± 0.067 0.170 ± 0.055 0.203 ± 0.048 0.148 ± 0.045 0.269 ± 0.076 0.389 ± 0.094
Transformer+Adapter 0.189 ± 0.052 0.364 ± 0.088 0.547 ± 0.117 0.166 ± 0.085 0.217 ± 0.071 0.257 ± 0.061 0.184 ± 0.056 0.334 ± 0.097 0.479 ± 0.117
Mamba+Token 0.197 ± 0.054 0.381 ± 0.091 0.574 ± 0.121 0.175 ± 0.090 0.230 ± 0.075 0.272 ± 0.065 0.192 ± 0.060 0.352 ± 0.102 0.503 ± 0.123
Mamba+Selection 0.221 ± 0.060 0.425 ± 0.101 0.635 ± 0.135 0.195 ± 0.099 0.256 ± 0.084 0.301 ± 0.074 0.216 ± 0.067 0.391 ± 0.112 0.559 ± 0.134
Mamba+Layer 0.193 ± 0.052 0.371 ± 0.089 0.556 ± 0.118 0.170 ± 0.087 0.224 ± 0.073 0.264 ± 0.063 0.187 ± 0.058 0.340 ± 0.098 0.487 ± 0.119
Mamba+Adapter 0.212 ± 0.058 0.409 ± 0.098 0.612 ± 0.131 0.187 ± 0.096 0.246 ± 0.080 0.290 ± 0.069 0.208 ± 0.064 0.378 ± 0.109 0.538 ± 0.131
Q1 Q2 Q3 Q4 Q5 Q6 Q7 Q8 Q9 Q10
Follower Counts
Q1Q2Q3Q4Q5Q6Q7Q8Q9Q10
Empirical Influence Scores
21 9 8 5 2 1 1 1 0 2
8 8 9 7 5 2 3 1 4 2
5 12 6 6 4 6 4 5 1 0
7 4 4 5 8 7 5 3 2 4
1 7 4 7 4 7 5 5 3 6
2 2 5 7 9 4 6 5 5 4
2 3 6 2 5 4 9 7 5 6
2 2 3 3 5 10 6 6 7 5
2 1 3 5 4 7 4 6 8 9
1 1 0 2 3 1 6 10 14 12
Empirical Influence Scores vs. Follower Counts
0.0
2.5
5.0
7.5
10.0
12.5
15.0
17.5
20.0
Q1 Q2 Q3 Q4 Q5 Q6 Q7 Q8 Q9 Q10
Causal Effect Scores
Q1Q2Q3Q4Q5Q6Q7Q8Q9Q10
Empirical Influence Scores
8 6 11 6 4 6 2 5 0 2
12 9 5 3 3 9 3 2 3 0
7 10 9 7 6 3 4 3 0 0
10 8 3 9 6 5 1 3 4 0
8 5 8 3 7 4 6 5 2 1
4 4 4 8 7 9 8 1 3 1
1 4 6 8 5 4 7 6 3 5
0 3 1 2 9 3 10 9 8 4
0 0 2 2 2 4 4 10 16 9
0 0 0 1 0 2 4 5 10 28
Empirical Influence Scores vs. Causal Effect Scores
0
5
10
15
20
25
Q1 Q2 Q3 Q4 Q5 Q6 Q7 Q8 Q9 Q10
Follower Counts
Q1Q2Q3Q4Q5Q6Q7Q8Q9Q10
Causal Effect Scores
4 9 10 9 5 3 2 3 1 4
8 9 4 6 3 6 5 2 1 5
11 3 5 4 6 6 3 2 5 4
9 8 5 2 3 6 5 5 4 2
6 2 6 5 4 7 8 5 3 3
2 9 5 7 8 5 2 7 1 3
5 3 3 4 8 3 8 2 5 8
3 2 5 5 5 5 6 6 10 2
2 2 4 2 5 5 6 11 7 5
1 2 1 5 2 3 4 6 12 14
Effect Effect Scores vs. Follower Counts
2
4
6
8
10
12
14
Figure 3: Decile Heatmaps (Spearman ρ correlation coefficient, Kendall’s W rank agreement,
Concordance Correlation Coefficient CCC): (left) Follower Counts vs. Empirical Influence
(ρ = 0.49, W = 0.67, CCC = 0.00), (centre) Causal Effect vs. Empirical Influence (0.57, 0.70,
0.21), (right) Follower Counts vs. Causal Effect (0.32, 0.21, 0.01).
Baselines and datasets. There exists no universally accepted ground truth for measuring
influence on social media. A popular proxy is the number of followers, as highly followed
users are more likely to spread a content, possible leading to adoption (therefore, influence).
The closest to a gold standard is the perceived empirical influence measure (Ram & Rizoiu,
2024), based on pairwise comparisons and an active learning-based ranking model. The
empirical influence measure is based on human judgements, and has been shown to have
desirable psychosocial properties. It is however prohibitive to scale; Ram & Rizoiu (2024)
only computed it on 492 X/Twitter users, discussing anti-climate change topics.
Causal effect is a tighter approximation of influence. Fig. 4 shows pairs of Spearman
correlation between the gold standard empirical influence and two approximations: the
follower count and our proposed causal effect influence. Visibly, the causal effect is better
estimation for empirical influence (ρ = 0.57) than follower counts (ρ = 0.49), particularly
visible for the top 10% most influential users. Further analysis using Kendall’s W confirms
this stronger rank agreement between causal effect and empirical influence (W = 0.70) com-
pared to followers (W = 0.67). The Concordance Correlation Coefficient reveals that while
follower count fails entirely to capture the magnitude of influence ( CCC = 0.00), causal
effect maintains some concordance ( CCC = 0.21). In particular, the two approximation
measures themselves show minimal agreement (ρ = 0.32, W = 0.21, CCC = 0.01), suggest-
ing they capture fundamentally different aspects of influence. These results challenge the
common assumption that account popularity (follower count) is a reliable approximation
for true influence, demonstrating causal effect as a superior estimate both in ranking and
scale.
Identify influential sources of misinformation. We analyzed the SocialSense dataset (Kong
et al., 2022), focusing specifically on vaccination and climate change narratives. For
each opinion, we calculated a weighted composite engagement score: E(o) = ˆelikes(o) +
9

Preprint. Under review.
CF1­1
(0% 20%)
CF1­2
(20% 40%)
CF1­3
(40% 60%)
CF2­1
(5­day early)
CF2­2
(3­day early)
CF2­3
(1­day early)
CF3­1
(1­day dur.)
CF3­2
(3­day dur.)
CF3­3
(5­day dur.)
0
10
20
30
40
50
60
70Relative Change from Baseline (%)
3.9%
8.8%
14.9%
3.4%
8.6%
16.0%
6.2%
9.2%
11.5%
4.7%
12.4%
23.9%
4.3%
7.0%
17.3%
4.7%
23.7%
27.7%
10.4%
22.1%
60.4%
9.0%
28.4%
49.5%
11.7%
54.1%
66.7%
10%
20%
30%
40%
Relative Percentage Change in Opinion Percentiles Across Counterfactual Scenarios
Climate change isn't real (base: 85.2%)
Climate change is a UN hoax (base: 55.6%)
Changes in earth's climate are natural (base: 22.2%)
Figure 4: Relative percentage changes in engagement for three climate change misinforma-
tion narratives under counterfactual scenarios.
ˆeshares(o) +3 × ˆecomments(o) +ˆeemoji(o), then normalized these scores using percentile rank-
ing: P(o) = number of opinions with E≤E(o) total number of opinions .
Our analysis extends viral potential theory Rizoiu & Xie (2017b) to misinformation contexts,
confirming that content responsiveness to external promotion depends on baseline popular-
ity and temporal dynamics across three climate change narratives: “Climate change isn’t
real” (85.2th percentile), “Climate change is a UN hoax” (55.6th percentile), and “Changes
in earth’s climate are natural” (22.2th percentile). Under progressive exposure manipulation
(CF1), the lowest-baseline narrative exhibits super-linear amplification with a 6-fold scaling
coefficient (10.4% → 22.1% → 60.4%), confirming that small external signals can trigger
massive engagement increases. This behavior validates high-potential, low-baseline content
theory (Rizoiu & Xie, 2017b), showing that emerging misinformation operates similarly to
sleeping beauty content with high viral potential that have yet to achieve widespread atten-
tion but can rapidly amplify under external promotion. The intermediate narrative shows
moderate scaling effects (4.7% → 12.4% → 23.9%), consistent with non-linear threshold dy-
namics in social influence, as evidenced by tipping point experiments (Centola et al., 2018).
Temporal intervention analysis (CF2) reveals that initiating promotion one day earlier yields
the highest amplification across all narrative types (16.0%, 17.3%, and 28.4%, respectively).
This finding aligns with prior work on optimal promotion timing (Rizoiu & Xie, 2017b)
and supports the broader framework of social acceleration (Rosa, 2013). Extended-duration
experiments (CF3) show that a sustained 5-day exposure maximizes narrative amplification,
with the emerging narrative reaching a 66.7% increase. This result corroborates the mere
exposure effect (Zajonc, 1968), reinforcing the superiority of prolonged campaigns over
short-term bursts.
Our causal model further identified influential public groups that amplified misinformation.
For instance, @AustraliansforSafeTechnology increased the engagement score for “5G/smart
tech is unsafe” narratives from 0.51 to 0.63 in February 2020, while @ClimateChangeBat-
tleRoyale elevated “Climate change crisis isn’t real” content from 0.11 to 0.23 in September
2019.
10

Preprint. Under review.
6 Conclusion
We investigate how external signals drive social media engagement, a key factor in mis-
information and disinformation spread, using a straightforward joint treatment-outcome
approach. By tweaking advanced models such as Transformers and Mamba, we improve
the predictions of engagement under realistic policy treatments. Our approach faces in-
herent causal challenges including unobserved confounding from algorithmic amplification,
selection bias in user engagement patterns, and treatment interference through network ef-
fects. Additional limitations include dependence on high-quality external signals that aren’t
always available, sensitivity to rapidly evolving platform algorithms, and assumptions
of temporal stability in user behavior patterns. Despite these constraints, our case study
proves our causal effect measure aligns closely with empirical influence, offering platforms
and regulators a reliable metric to identify influential spreaders of misleading narratives.
Ethical Considerations and Dual-Use Concerns
This work uses publicly available social media data from platforms like X (formerly Twitter)
and Facebook to analyze engagement patterns and misinformation dynamics. All data
were collected in accordance with platform terms of service and API usage policies, and
with approvals from our institution’s Human Ethics Committee. Our analysis examines
aggregate trends at the group level rather than targeting individuals. User identifiers were
anonymized, and no personally identifiable information was collected or retained.
Our causal influence estimation framework has important ethical implications that extend
beyond data privacy. While these tools enable beneficial applications like identifying sources
of misinformation and improving platform governance, they could potentially be misused to
optimize manipulation campaigns or target influential users for spreading harmful content.
We acknowledge these dual-use concerns and propose safeguards, such as integrating with
existing content moderation frameworks to prioritize intervention efforts.
We believe that understanding the causal mechanisms of influence is necessary for designing
effective interventions against harmful content, and that responsible development prac-
tices—including limitations on individual-level influence measurements—can help mitigate
potential misuse. Our research aims to contribute to the broader effort of creating healthier
online information ecosystems while remaining mindful of these ethical challenges.
References
Sinan Aral, Lev Muchnik, and Arun Sundararajan. Distinguishing influence-based contagion
from homophily-driven diffusion in dynamic networks.Proceedings of the National Academy
of Sciences, 106(51):21544–21549, 2009.
Eytan Bakshy, Jake M Hofman, Winter A Mason, and Duncan J Watts. Everyone’s an
influencer: quantifying influence on twitter. In Proceedings of the fourth ACM international
conference on Web search and data mining, pp. 65–74, 2011.
Eytan Bakshy, Solomon Messing, and Lada A Adamic. Exposure to ideologically diverse
news and opinion on facebook. Science, 348(6239):1130–1132, 2015.
Jay J Van Bavel, Katherine Baicker, Paulo S Boggio, Valerio Capraro, Aleksandra Cichocka,
Mina Cikara, Molly J Crockett, Alia J Crum, Karen M Douglas, James N Druckman, et al.
Using social and behavioural science to support covid-19 pandemic response. Nature
human behaviour, 4(5):460–471, 2020.
Joshua Becker, Devon Brackbill, and Damon Centola. Network dynamics of social influence
in the wisdom of crowds. Proceedings of the national academy of sciences , 114(26):E5070–
E5076, 2017.
Ioana Bica, Ahmed M Alaa, James Jordon, and Mihaela van der Schaar. Estimating
counterfactual treatment outcomes over time through adversarially balanced repre-
11

Preprint. Under review.
sentations. In International Conference on Learning Representations , 2020. URL https:
//openreview.net/forum?id=BJg866NFvB.
Pio Calderon, Rohit Ram, and Marian-Andrei Rizoiu. Opinion market model: stemming
far-right opinion spread using positive interventions. In Proceedings of the international
AAAI conference on web and social media, volume 18, pp. 177–190, 2024.
Qi Cao, Huawei Shen, Keting Cen, Wentao Ouyang, and Xueqi Cheng. Deephawkes:
Bridging the gap between prediction and understanding of information cascades. In
Proceedings of the 2017 ACM on Conference on Information and Knowledge Management, pp.
1149–1158, 2017.
Damon Centola, Joshua Becker, Devon Brackbill, and Andrea Baronchelli. Experimental
evidence for tipping points in social convention. Science, 360(6393):1116–1119, 2018.
Meeyoung Cha, Hamed Haddadi, Fabricio Benevenuto, and Krishna Gummadi. Measuring
user influence in twitter: The million follower fallacy. In Proceedings of the international
AAAI conference on web and social media, volume 4, pp. 10–17, 2010.
Justin Cheng, Lada Adamic, P Alex Dow, Jon Michael Kleinberg, and Jure Leskovec. Can
cascades be predicted? In Proceedings of the 23rd international conference on World wide web,
pp. 925–936, 2014.
Tri Dao, Dan Fu, Stefano Ermon, Atri Rudra, and Christopher R ´e. Flashattention: Fast
and memory-efficient exact attention with io-awareness. Advances in neural information
processing systems, 35:16344–16359, 2022.
Keyan Ding, Ronggang Wang, and Shiqi Wang. Social media popularity prediction: A
multiple feature fusion approach with deep neural networks. In Proceedings of the 27th
ACM International Conference on Multimedia, pp. 2682–2686, 2019.
Dean Eckles, Ren´e F Kizilcec, and Eytan Bakshy. Estimating peer effects in networks with
peer encouragement designs. Proceedings of the National Academy of Sciences , 113(27):
7316–7322, 2016.
Song Gao, Jinmeng Rao, Yuhao Kang, Yunlei Liang, Jake Kruse, Dorte Dopfer, Ajay K Sethi,
Juan Francisco Mandujano Reyes, Brian S Yandell, and Jonathan A Patz. Association
of mobile phone location data indications of travel and stay-at-home mandates with
covid-19 infection rates in the us. JAMA network open, 3(9):e2020485–e2020485, 2020.
Albert Gu and Tri Dao. Mamba: Linear-time sequence modeling with selective state spaces.
In First Conference on Language Modeling, 2024. URL https://openreview.net/forum?id=
tEYskw1VY2.
Albert Gu, Tri Dao, Stefano Ermon, Atri Rudra, and Christopher R ´e. Hippo: Recurrent
memory with optimal polynomial projections. Advances in neural information processing
systems, 33:1474–1487, 2020.
C ¸a˘glar Hızlı, ST John, Anne Tuulikki Juuti, Tuure Tapani Saarinen, Kirsi Hannele Pietil¨ainen,
and Pekka Marttinen. Causal modeling of policy interventions from treatment-outcome
sequences. In International Conference on Machine Learning, pp. 13050–13084. PMLR, 2023.
Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski, Bruna Morrone, Quentin De Larous-
silhe, Andrea Gesmundo, Mona Attariyan, and Sylvain Gelly. Parameter-efficient transfer
learning for nlp. In International Conference on Machine Learning, pp. 2790–2799. PMLR,
2019.
Sarah J Jackson, Moya Bailey, and Brooke Foucault Welles.# HashtagActivism: Networks of
race and gender justice. Mit Press, 2020.
Quyu Kong, Emily Booth, Francesco Bailo, Amelia Johns, and Marian-Andrei Rizoiu. Slip-
ping to the Extreme: A Mixed Method to Explain How Extreme Opinions Infiltrate Online
Discussions. In Proceedings of the International AAAI Conference on Web and Social Media,
volume 16, pp. 524–535, 2022.
12

Preprint. Under review.
Quyu Kong, Pio Calderon, Rohit Ram, Olga Boichak, and Marian-Andrei Rizoiu. Interval-
censored transformer hawkes: Detecting information operations using the reaction of
social systems. In Proceedings of the ACM web conference 2023, pp. 1813–1821, 2023.
Haewoon Kwak, Changhyun Lee, Hosung Park, and Sue Moon. What is twitter, a social
network or a news media? In Proceedings of the 19th international conference on World wide
web, pp. 591–600, 2010.
Cheng Li, Jiaqi Ma, Xiaoxiao Guo, and Qiaozhu Mei. Deepcas: An end-to-end predictor of
information cascades. In Proceedings of the 26th international conference on World Wide Web,
pp. 577–586, 2017.
Bryan Lim. Forecasting treatment responses over time using recurrent marginal structural
networks. Advances in neural information processing systems, 31, 2018.
Judith J Lok. Statistical modeling of causal effects in continuous time. The Annals of Statistics,
pp. 1464–1507, 2008.
Xiaodong Lu, Shuo Ji, Le Yu, Leilei Sun, Bowen Du, and Tongyu Zhu. Continuous-time
graph learning for cascade popularity prediction. In Proceedings of the Thirty-Second
International Joint Conference on Artificial Intelligence, pp. 2224–2232, 2023.
Lev Muchnik, Sinan Aral, and Sean J Taylor. Social influence bias: A randomized experiment.
Science, 341(6146):647–651, 2013.
Judea Pearl. Causality. Cambridge university press, 2009.
Jonas Peters, Dominik Janzing, and Bernhard Sch¨olkopf. Elements of causal inference: founda-
tions and learning algorithms. The MIT Press, 2017.
Jiezhong Qiu, Jian Tang, Hao Ma, Yuxiao Dong, Kuansan Wang, and Jie Tang. Deepinf:
Social influence prediction with deep learning. In Proceedings of the 24th ACM SIGKDD
international conference on knowledge discovery & data mining, pp. 2110–2119, 2018.
Rohit Ram and Marian-Andrei Rizoiu. Empirically measuring online social influence. EPJ
Data Science, 13(1):53, 2024.
Marian-Andrei Rizoiu and Lexing Xie. Online popularity under promotion: Viral potential,
forecasting, and the economics of time. In International AAAI Conference on Web and Social
Media (ICWSM ’17), pp. 182–191, 2017a. URL https://aaai.org/ocs/index.php/ICWSM/I
CWSM17/paper/view/15553https://arxiv.org/pdf/1703.01012.pdf.
Marian-Andrei Rizoiu and Lexing Xie Xie. Online popularity under promotion: Viral
potential, forecasting, and the economics of time. In Proceedings of the International AAAI
Conference on Web and Social Media, volume 11, pp. 182–191, 2017b.
Marian-Andrei Rizoiu, Lexing Xie, Scott Sanner, Manuel Cebrian, Honglin Yu, and Pascal
Van Hentenryck. Expecting to be hip: Hawkes intensity processes for social media
popularity. In Proceedings of the 26th international conference on world wide web, pp. 735–744,
2017.
Marian-Andrei Rizoiu, Alexander Soen, Shidi Li, Pio Calderon, Leanne J Dong, Aditya Kr-
ishna Menon, and Lexing Xie. Interval-censored hawkes processes. Journal of Machine
Learning Research, 23(338):1–84, 2022.
James Robins. A new approach to causal inference in mortality studies with a sustained ex-
posure period—application to control of the healthy worker survivor effect. Mathematical
modelling, 7(9-12):1393–1512, 1986.
James M Robins, Miguel Angel Hernan, and Babette Brumback. Marginal structural models
and causal inference in epidemiology, 2000.
Hartmut Rosa. Social acceleration: A new theory of modernity . Columbia University Press,
2013.
13

Preprint. Under review.
Peter Schulam and Suchi Saria. Reliable decision support using counterfactual models.
Advances in neural information processing systems, 30, 2017.
Hossein Soleimani, Adarsh Subbaswamy, and Suchi Saria. Treatment-response models for
counterfactual reasoning with continuous-time, continuous-valued interventions. In 33rd
Conference on Uncertainty in Artificial Intelligence, UAI 2017, 2017.
Lin Tian, Emily Booth, Francesco Bailo, Julian Droogan, and Marian-Andrei Rizoiu. Be-
fore it’s too late: A state space model for the early prediction of misinformation and
disinformation engagement. arXiv preprint arXiv:2502.04655, 2025.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez,
Ł ukasz Kaiser, and Illia Polosukhin. Attention is all you need. In Advances in Neural
Information Processing Systems, volume 30. Curran Associates, Inc., 2017. URL https:
//proceedings.neurips.cc/paper files/paper/2017/file/3f5ee243547dee91fbd053c
1c4a845aa-Paper.pdf.
Jia Wang, Vincent W Zheng, Zemin Liu, and Kevin Chen-Chuan Chang. Topological
recurrent neural network for diffusion prediction. In 2017 IEEE international conference on
data mining (ICDM), pp. 475–484. IEEE, 2017a.
Yongqing Wang, Huawei Shen, Shenghua Liu, Jinhua Gao, and Xueqi Cheng. Cascade
dynamics modeling with attention-based recurrent neural network. In IJCAI, volume 17,
pp. 2985–2991, 2017b.
Duncan J Watts, David M Rothschild, and Markus Mobius. Measuring the news and its
impact on democracy. Proceedings of the National Academy of Sciences, 118(15):e1912443118,
2021.
Haixu Wu, Jiehui Xu, Jianmin Wang, and Mingsheng Long. Autoformer: Decomposition
transformers with auto-correlation for long-term series forecasting. Advances in neural
information processing systems, 34:22419–22430, 2021.
Robert B Zajonc. Attitudinal effects of mere exposure. Journal of personality and social
psychology, 9(2p2):1, 1968.
Qingyuan Zhao, Murat A Erdogdu, Hera Y He, Anand Rajaraman, and Jure Leskovec.
Seismic: A self-exciting point process model for predicting tweet popularity. InProceedings
of the 21th ACM SIGKDD international conference on knowledge discovery and data mining, pp.
1513–1522, 2015.
Fan Zhou, Xovee Xu, Goce Trajcevski, and Kunpeng Zhang. A survey of information
cascade analysis: Models, predictions, and recent advances. ACM Computing Surveys
(CSUR), 54(2):1–36, 2021a.
Haoyi Zhou, Shanghang Zhang, Jieqi Peng, Shuai Zhang, Jianxin Li, Hui Xiong, and Wancai
Zhang. Informer: Beyond efficient transformer for long sequence time-series forecasting.
In Proceedings of the AAAI conference on artificial intelligence, volume 35, pp. 11106–11115,
2021b.
Simiao Zuo, Haoming Jiang, Zichong Li, Tuo Zhao, and Hongyuan Zha. Transformer
hawkes process. In International conference on machine learning, pp. 11692–11702. PMLR,
2020.
A Appendix
A.1 Related Work
Our research lies at the intersection of social media engagement prediction, causal inference
for sequential data, and advanced sequence modeling.
14

Preprint. Under review.
Social Media Engagement Prediction. Social media engagement prediction has evolved
from early content and user-focused models (Cheng et al., 2014) to approaches incorporating
network structures (Zhao et al., 2015) and temporal dynamics (Rizoiu et al., 2017). Recent
deep learning advances include DeepCas (Li et al., 2017), which uses random walks and
attention mechanisms for cascade prediction; SNPP (Ding et al., 2019), applying temporal
point processes with recurrent architectures; and Topo-LSTM (Wang et al., 2017a), which
models user interactions through topological structures. Graph-based approaches like
DeepInf (Qiu et al., 2018) leverage network structures to predict user behaviors. Temporal
dynamics have been addressed through several specialized frameworks. DeepHawkes (Cao
et al., 2017) combines reinforcement learning with Hawkes processes, while HIP (Rizoiu
et al., 2017) and MBPP (Rizoiu et al., 2022) model view count dynamics on YouTube. IC-
TH (Kong et al., 2023) tackles interval-censored observations in retweet prediction, and
OMM (Calderon et al., 2024) offers a cross-platform mathematical framework for predicting
content spread.
While these approaches have cascade modeling, they typically rely on historical engagement
patterns without considering external causal drivers. Our work explicitly models how
external signals (like Google Trends) causally impact engagement dynamics.
Causal Inference for Sequential Data. Causal inference with sequential data builds on
foundations like g-methods (Robins, 1986) and marginal structural models (Robins et al.,
2000), which handle time-varying treatments and confounders. These approaches have been
extended to continuous-time settings (Lok, 2008; Schulam & Saria, 2017). Neural approaches
include Recurrent Marginal Structural Networks (Lim, 2018), which extend traditional
causal models with recurrent architectures, and Counterfactual Recurrent Network (Bica
et al., 2020), which uses adversarial learning to address time-varying confounding. For
continuous-time treatments, researchers have developed personalized treatment response
curves using Gaussian processes (Soleimani et al., 2017) and counterfactual frameworks for
disease trajectory modeling (Schulam & Saria, 2017). Recently, Hızlı et al. (2023) introduced a
joint treatment-outcome model combining marked point processes with Gaussian processes
for healthcare policy interventions. These methods, while advanced, often lack the flexibility
to capture social media’s unique engagement dynamics and the complex temporal patterns
of external influence.
State Space Models and Transformers for Sequence Modeling. Sequence modeling has
recently been dominated by transformer architectures (Vaswani et al., 2017) and state space
models. Time series adaptations include Informer (Zhou et al., 2021b), using ProbSparse
self-attention, and Autoformer (Wu et al., 2021), leveraging auto-correlation for period-
based dependencies. State Space Models (SSMs) have emerged as efficient alternatives for
capturing long-range dependencies (Gu et al., 2020), processing extremely long sequences
(Dao et al., 2022), and achieving competitive performance in language modeling (Gu & Dao,
2024). The Mamba architecture (Gu & Dao, 2024) introduced selective state space modeling,
achieving state-of-the-art results with reduced computational requirements.
Despite these advances, few studies have applied modern SSMs to social media engagement
prediction in causal contexts. Existing approaches typically rely on graph-based (Lu et al.,
2023), RNN (Wang et al., 2017b), or transformer methods (Zuo et al., 2020) that assume
uniform sampling or discrete snapshots, overlooking the fine-grained temporal patterns
essential to engagement dynamics.
A.2 Training Details
Models are trained on 4x NVIDIA A100 GPUs with PyTorch, using the joint loss function
from Section 3.4 ( α = 0.5, β = 0.1). Optimization uses AdamW with a learning rate of
10−4, batch size of 64, and early stopping based on validation RMSE (patience = 10 epochs).
Hyperparameters (e.g., τlag = 24 hours, w = 6) are tuned via grid search.
15

Preprint. Under review.
A.3 Model Architecture Details
Our implementation uses a depth-L architecture with embedding dimension d and hidden
dimension h. Here are the details for each integration mechanism:
Token Integration: For the token-based approach, external signalsgt at time t are embedded
through a projection Eg ∈ R|g|×d:
et g = Embedding(gt) =Wggt + bg
These embedded tokens are then interleaved with engagement embeddings in the input
sequence:
X = [e1, e1 g, e2, e2 g, . . . ,en, en g]
Attention Integration: For attention-based integration, we modify the self-attention mecha-
nism to include specialized heads focused on learning external signals. Given query Q, key
K, and value V matrices, we compute:
Attention(Q, K, V) =softmax
 QKT
√dk ⊙ M

V
where M is a masking matrix with elements mij = exp(−β|ti − tj|) that emphasizes tempo-
rally proximate signal-engagement pairs with decay parameter β = 0.1.
Layer Integration: Our layer-based approach processes external signals through a separate
MLP layer:
hl g = MLPl g(hl−1 g ) =Wl 2 · GeLU(Wl 1hl−1 g + bl 1) +bl 2
which is merged with the main sequence representations through cross-attention at each
layer l:
hl e = hl−1 e + CrossAttention(hl−1 e , hl g, hl g)
Adapter Integration: For adapter-based integration, we insert compact bottleneck modules
after each self-attention and feed-forward layer:
hout = hin + Wup · GeLU(Wdown · hin + bdown) +bup
where Wdown ∈ Rd×r and Wup ∈ Rr×d with bottleneck dimension r = d/8.
For the Mamba variants, we extend the selective state space model with signal-conditioned
selection mechanisms. The state update equation* becomes:
ht = A(gt)ht−1 + B(gt)xt
where the state transition matrix A(gt) and input projection B(gt) are conditioned on
external signals gt through a low-rank adaptation:
A(gt) =A0 + ∆A · σ(Wggt)
The selective scan algorithm uses a similar signal-aware mechanism to compute selection
weights, allowing the model to dynamically focus on relevant temporal dependencies based
on external signal patterns.
A.4 Detailed Results Across Individual Datasets
This appendix presents detailed experimental results for the predictive performance of
various model architectures across five distinct datasets: bushfire, covid, vaccination, climate
change, and DiN. The tables provided here complement the aggregated results reported in
Section 4.3, which represent the mean Root Mean Squared Error (RMSE) and Binary Cross
Entropy (BCE) across these datasets. Here, we report individual dataset results to offer a
granular view of model behavior under different counterfactual scenarios.
16

Preprint. Under review.
Model Base Scenario 1: Exposure Scenario 2: Timing Scenario 3: Duration
20% 40% 60% -5 days -3 days -1 day 1-day 3-day 5-day
Transformer + Token 0.147 0.233 0.242 0.243 0.232 0.213 0.207 0.252 0.263 0.272
Transformer + Attention 0.133 0.212 0.193 0.197 0.208 0.202 0.188 0.242 0.208 0.212
Transformer + Layer 0.142 0.208 0.192 0.193 0.212 0.198 0.192 0.238 0.212 0.208
Transformer + Adapter 0.123 0.192 0.173 0.182 0.188 0.182 0.173 0.222 0.188 0.192
Mamba + Token 0.143 0.207 0.183 0.192 0.203 0.197 0.183 0.263 0.247 0.232
Mamba + Selection 0.132 0.183 0.177 0.178 0.187 0.173 0.177 0.262 0.238 0.223
Mamba + Layer 0.128 0.177 0.162 0.158 0.173 0.167 0.153 0.252 0.228 0.217
Mamba + Adapter 0.127 0.183 0.172 0.173 0.187 0.183 0.172 0.258 0.232 0.208
Table 4: Root Mean Squared Error (RMSE) of predicted social media engagement metrics
over a 7-day horizon under counterfactual scenarios for the DiN dataset.
Model Scenario 1: Exposure Scenario 2: Timing Scenario 3: Treatment
20% 40% 60% -5 days -3 days -1 day 1-day 3-day 5-day
Transformer + Token 0.592 0.502 0.438 0.527 0.458 0.437 0.583 0.522 0.488
Transformer + Attention 0.543 0.442 0.403 0.487 0.403 0.377 0.582 0.498 0.487
Transformer + Layer 0.563 0.457 0.417 0.493 0.432 0.393 0.562 0.463 0.437
Transformer + Adapter 0.532 0.423 0.387 0.453 0.397 0.358 0.578 0.507 0.493
Mamba + Token 0.577 0.488 0.437 0.503 0.457 0.433 0.572 0.513 0.497
Mamba + Selection 0.547 0.442 0.393 0.457 0.403 0.367 0.568 0.507 0.483
Mamba + Layer 0.552 0.443 0.397 0.463 0.407 0.368 0.572 0.497 0.483
Mamba + Adapter 0.533 0.427 0.378 0.452 0.388 0.362 0.558 0.493 0.477
Table 5: Binary Cross Entropy (BCE) of treatment intensity predictions over a 7-day horizon
for the DiN dataset across counterfactual scenarios.
Model Base Scenario 1: Exposure Scenario 2: Timing Scenario 3: Duration
20% 40% 60% -5 days -3 days -1 day 1-day 3-day 5-day
Transformer + Token 0.129 0.216 0.218 0.223 0.208 0.203 0.198 0.241 0.243 0.248
Transformer + Attention 0.123 0.198 0.193 0.183 0.193 0.188 0.183 0.223 0.198 0.193
Transformer + Layer 0.126 0.203 0.198 0.188 0.198 0.193 0.188 0.228 0.203 0.198
Transformer + Adapter 0.117 0.193 0.188 0.178 0.188 0.183 0.178 0.218 0.193 0.188
Mamba + Token 0.130 0.208 0.203 0.193 0.203 0.198 0.193 0.243 0.223 0.218
Mamba + Selection 0.119 0.198 0.193 0.183 0.193 0.188 0.183 0.238 0.218 0.213
Mamba + Layer 0.121 0.203 0.198 0.188 0.198 0.193 0.188 0.243 0.223 0.218
Mamba + Adapter 0.114 0.188 0.183 0.173 0.183 0.178 0.173 0.233 0.218 0.213
Table 6: Root Mean Squared Error (RMSE) of predicted social media engagement metrics
over a 7-day horizon under counterfactual scenarios for the climate change dataset.
Model Scenario 1: Exposure Scenario 2: Timing Scenario 3: Treatment
20% 40% 60% -5 days -3 days -1 day 1-day 3-day 5-day
Transformer + Token 0.538 0.463 0.403 0.478 0.433 0.408 0.538 0.478 0.463
Transformer + Attention 0.508 0.423 0.378 0.448 0.393 0.353 0.528 0.463 0.443
Transformer + Layer 0.513 0.433 0.383 0.458 0.403 0.373 0.508 0.428 0.413
Transformer + Adapter 0.493 0.403 0.353 0.428 0.373 0.338 0.543 0.483 0.463
Mamba + Token 0.528 0.453 0.393 0.468 0.418 0.398 0.533 0.478 0.463
Mamba + Selection 0.498 0.413 0.368 0.438 0.378 0.348 0.533 0.468 0.453
Mamba + Layer 0.503 0.423 0.373 0.448 0.388 0.358 0.538 0.473 0.448
Mamba + Adapter 0.483 0.398 0.348 0.418 0.363 0.333 0.523 0.458 0.438
Table 7: Binary Cross Entropy (BCE) of treatment intensity predictions over a 7-day horizon
for the climate change dataset across counterfactual scenarios.
17

Preprint. Under review.
Model Base Scenario 1: Exposure Scenario 2: Timing Scenario 3: Duration
20% 40% 60% -5 days -3 days -1 day 1-day 3-day 5-day
Transformer + Token 0.126 0.211 0.213 0.218 0.203 0.198 0.193 0.235 0.238 0.243
Transformer + Attention 0.121 0.193 0.188 0.178 0.188 0.183 0.178 0.218 0.193 0.188
Transformer + Layer 0.123 0.198 0.193 0.183 0.193 0.188 0.183 0.223 0.198 0.193
Transformer + Adapter 0.114 0.188 0.183 0.173 0.183 0.178 0.173 0.213 0.188 0.183
Mamba + Token 0.127 0.203 0.198 0.188 0.198 0.193 0.188 0.238 0.218 0.213
Mamba + Selection 0.117 0.193 0.188 0.178 0.188 0.183 0.178 0.233 0.213 0.208
Mamba + Layer 0.119 0.198 0.193 0.183 0.193 0.188 0.183 0.238 0.218 0.213
Mamba + Adapter 0.112 0.183 0.178 0.168 0.178 0.173 0.168 0.228 0.213 0.208
Table 8: Root Mean Squared Error (RMSE) of predicted social media engagement metrics
over a 7-day horizon under counterfactual scenarios for the vaccination dataset.
Model Scenario 1: Exposure Scenario 2: Timing Scenario 3: Treatment
20% 40% 60% -5 days -3 days -1 day 1-day 3-day 5-day
Transformer + Token 0.533 0.458 0.398 0.473 0.428 0.403 0.533 0.473 0.458
Transformer + Attention 0.503 0.418 0.373 0.443 0.388 0.348 0.523 0.458 0.438
Transformer + Layer 0.508 0.428 0.378 0.453 0.398 0.368 0.503 0.423 0.408
Transformer + Adapter 0.488 0.398 0.348 0.423 0.368 0.333 0.538 0.478 0.458
Mamba + Token 0.523 0.448 0.388 0.463 0.413 0.393 0.528 0.473 0.458
Mamba + Selection 0.493 0.408 0.363 0.433 0.373 0.343 0.528 0.463 0.448
Mamba + Layer 0.498 0.418 0.368 0.443 0.383 0.353 0.533 0.468 0.443
Mamba + Adapter 0.478 0.393 0.343 0.413 0.358 0.328 0.518 0.453 0.433
Table 9: Binary Cross Entropy (BCE) of treatment intensity predictions over a 7-day horizon
for the vaccination dataset across counterfactual scenarios.
Model Base Scenario 1: Exposure Scenario 2: Timing Scenario 3: Duration
20% 40% 60% -5 days -3 days -1 day 1-day 3-day 5-day
Transformer + Token 0.123 0.208 0.213 0.218 0.203 0.198 0.193 0.235 0.238 0.243
Transformer + Attention 0.117 0.193 0.188 0.178 0.188 0.183 0.178 0.218 0.193 0.188
Transformer + Layer 0.119 0.198 0.193 0.183 0.193 0.188 0.183 0.223 0.198 0.193
Transformer + Adapter 0.112 0.188 0.183 0.173 0.183 0.178 0.173 0.213 0.188 0.183
Mamba + Token 0.124 0.203 0.198 0.188 0.198 0.193 0.188 0.238 0.218 0.213
Mamba + Selection 0.115 0.193 0.188 0.178 0.188 0.183 0.178 0.233 0.213 0.208
Mamba + Layer 0.117 0.198 0.193 0.183 0.193 0.188 0.183 0.238 0.218 0.213
Mamba + Adapter 0.110 0.183 0.178 0.168 0.178 0.173 0.168 0.228 0.213 0.208
Table 10: Root Mean Squared Error (RMSE) of predicted social media engagement metrics
over a 7-day horizon under counterfactual scenarios for the covid dataset.
Model Scenario 1: Exposure Scenario 2: Timing Scenario 3: Treatment
20% 40% 60% -5 days -3 days -1 day 1-day 3-day 5-day
Transformer + Token 0.531 0.453 0.393 0.468 0.423 0.398 0.528 0.468 0.453
Transformer + Attention 0.498 0.413 0.368 0.438 0.383 0.343 0.518 0.453 0.433
Transformer + Layer 0.503 0.423 0.373 0.448 0.393 0.363 0.498 0.418 0.403
Transformer + Adapter 0.483 0.393 0.343 0.418 0.363 0.333 0.533 0.473 0.453
Mamba + Token 0.518 0.443 0.383 0.458 0.408 0.388 0.523 0.473 0.453
Mamba + Selection 0.488 0.403 0.358 0.428 0.368 0.338 0.523 0.458 0.443
Mamba + Layer 0.493 0.413 0.363 0.438 0.378 0.348 0.528 0.463 0.438
Mamba + Adapter 0.473 0.388 0.338 0.413 0.358 0.328 0.513 0.448 0.428
Table 11: Binary Cross Entropy (BCE) of treatment intensity predictions over a 7-day horizon
for the covid dataset across counterfactual scenarios.
18

Preprint. Under review.
Model Base Scenario 1: Exposure Scenario 2: Timing Scenario 3: Duration
20% 40% 60% -5 days -3 days -1 day 1-day 3-day 5-day
Transformer + Token 0.121 0.206 0.212 0.217 0.202 0.193 0.188 0.231 0.237 0.242
Transformer + Attention 0.116 0.192 0.187 0.173 0.186 0.178 0.172 0.216 0.191 0.183
Transformer + Layer 0.117 0.196 0.188 0.181 0.192 0.187 0.182 0.218 0.193 0.192
Transformer + Adapter 0.111 0.183 0.182 0.171 0.179 0.173 0.168 0.211 0.186 0.178
Mamba + Token 0.123 0.201 0.197 0.183 0.196 0.192 0.187 0.233 0.217 0.208
Mamba + Selection 0.113 0.188 0.186 0.176 0.183 0.181 0.173 0.232 0.211 0.207
Mamba + Layer 0.116 0.193 0.192 0.178 0.188 0.183 0.181 0.236 0.213 0.212
Mamba + Adapter 0.107 0.181 0.173 0.166 0.177 0.172 0.163 0.223 0.208 0.203
Table 12: Root Mean Squared Error (RMSE) of predicted social media engagement metrics
over a 7-day horizon under counterfactual scenarios for the bushfire dataset.
Model Scenario 1: Exposure Scenario 2: Timing Scenario 3: Treatment
20% 40% 60% -5 days -3 days -1 day 1-day 3-day 5-day
Transformer + Token 0.522 0.447 0.383 0.462 0.413 0.392 0.518 0.461 0.443
Transformer + Attention 0.488 0.403 0.362 0.428 0.377 0.333 0.512 0.447 0.426
Transformer + Layer 0.497 0.417 0.363 0.442 0.383 0.357 0.492 0.408 0.397
Transformer + Adapter 0.473 0.387 0.338 0.412 0.353 0.327 0.523 0.467 0.443
Mamba + Token 0.512 0.433 0.377 0.452 0.402 0.378 0.517 0.463 0.447
Mamba + Selection 0.478 0.397 0.352 0.413 0.362 0.328 0.513 0.452 0.433
Mamba + Layer 0.483 0.407 0.353 0.427 0.372 0.342 0.517 0.453 0.432
Mamba + Adapter 0.467 0.378 0.337 0.398 0.352 0.318 0.507 0.447 0.418
Table 13: Binary Cross Entropy (BCE) of treatment intensity predictions over a 7-day horizon
for the bushfire dataset across counterfactual scenarios.
19
