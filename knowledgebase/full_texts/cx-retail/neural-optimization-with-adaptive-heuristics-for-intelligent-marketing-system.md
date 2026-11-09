---
title: Neural Optimization with Adaptive Heuristics for Intelligent Marketing System
url: https://arxiv.org/abs/2405.10490
category: cx-retail
subcategory: framework
date: 2024-08
venue: ''
authors:
- Changshuai Wei
- Benjamin Zelditch
- Joyce Chen
source: arxiv
pdf_url: https://arxiv.org/pdf/2405.10490
pages: 16
chars: 74115
fetched_at: '2026-11-08T12:57:04+00:00'
kb_version: 1
---

# Neural Optimization with Adaptive Heuristics for Intelligent Marketing System

Neural Optimization with Adaptive Heuristics for Intelligent
Marketing System
Changshuai Wei∗
LinkedIn Corporation
Seattle, USA
chawei@linkedin.com
Benjamin Zelditch
LinkedIn Corporation
New York, USA
bzelditch@linkedin.com
Joyce Chen
LinkedIn Corporation
Sunnyvale, USA
joychen@linkedin.com
Andre Assuncao Silva T Ribeiro
LinkedIn Corporation
Sunnyvale, USA
aribeiro@linkedin.com
Jingyi Kenneth Tay
LinkedIn Corporation
Sunnyvale, USA
ktay@linkedin.com
Borja Ocejo Elizondo
LinkedIn Corporation
Sunnyvale, USA
bocejo@linkedin.com
Sathiya Keerthi Selvaraj
LinkedIn Corporation
Sunnyvale, USA
keselvaraj@linkedin.com
Aman Gupta
LinkedIn Corporation
Sunnyvale, USA
amagupta@linkedin.com
Licurgo Benemann De Almeida
LinkedIn Corporation
New York, USA
lalmeida@linkedin.com
ABSTRACT
Computational marketing has become increasingly important in
today’s digital world, facing challenges such as massive hetero-
geneous data, multi-channel customer journeys, and limited mar-
keting budgets. In this paper, we propose a general framework
for marketing AI systems, the Neural Optimization with Adaptive
Heuristics (NOAH) framework. NOAH is the ￿rst general frame-
work for marketing optimization that considers both to-business
(2B) and to-consumer (2C) products, as well as both owned and
paid channels. We describe key modules of the NOAH framework,
including prediction, optimization, and adaptive heuristics, provid-
ing examples for bidding and content optimization. We then detail
the successful application of NOAH to LinkedIn’s email marketing
system, showcasing signi￿cant wins over the legacy ranking sys-
tem. Additionally, we share details and insights that are broadly
useful, particularly on: (i) addressing delayed feedback with life-
time value, (ii) performing large-scale linear programming with
randomization, (iii) improving retrieval with audience expansion,
(iv) reducing signal dilution in targeting tests, and (v) handling
zero-in￿ated heavy-tail metrics in statistical testing.
CCS CONCEPTS
• Computing methodologies !Machine learning; • Applied
computing !Marketing; • Mathematics of computing !
Probability and statistics ; Mathematical optimization.
∗Corresponding author.
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for pro￿t or commercial advantage and that copies bear this notice and the full citation
on the ￿rst page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior speci￿c permission
and/or a fee. Request permissions from permissions@acm.org.
KDD ’24, August 25–29, 2024, Barcelona, Spain
© 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 979-8-4007-0490-1/24/08
https://doi.org/10.1145/3637528.3671591
KEYWORDS
Computational Marketing, Linear Programming, Lifetime Value,
Audience Expansion
ACM Reference Format:
Changshuai Wei, Benjamin Zelditch, Joyce Chen, Andre Assuncao Silva T
Ribeiro, Jingyi Kenneth Tay, Borja Ocejo Elizondo, Sathiya Keerthi Selvaraj,
Aman Gupta, and Licurgo Benemann De Almeida. 2024. Neural Optimization
with Adaptive Heuristics for Intelligent Marketing System. In Proceedings of
the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining
(KDD ’24), August 25–29, 2024, Barcelona, Spain. ACM, New York, NY, USA,
16 pages. https://doi.org/10.1145/3637528.3671591
1 INTRODUCTION
Compared with traditional media marketing, online digital mar-
keting has become increasingly important for advertisers and mar-
keters. With online digital marketing, marketers can reach cus-
tomers more directly with personalized marketing messages. Many
of the current major internet companies build advertising plat-
forms to better connect advertisers/marketers to customers, typi-
cally through auction or bidding systems. From a marketer’s per-
spective, there are paid social channels (e.g., Facebook) and paid
search channels (e.g., Google). Besides these paid channels, there are
also owned channels like email, where marketers can connect with
customers directly. There is much literature on building machine
learning (ML) systems from ads platform’s perspective; however,
few papers have discussed ML and optimization systematically
from the marketer’s perspective. In fact, there are many unique
challenges when building an intelligent marketing system from the
marketer’s perspective:
(1) The data can be massive and heterogeneous. Since there
are multiple marketing channels, the granularity of data
from di￿erent channels are highly heterogeneous. For owned
channels like email, marketers can collect member-level user
feedback, whereas for paid channels like Google Search, mar-
keters can only collect aggregate-level information, e.g., at
the keyword or campaign level.

KDD ’24, August 25–29, 2024, Barcelona, Spain Changshuai Wei et al.
(2) The objective can be challenging to de￿ne. The mar-
keting life-cycle can be quite di￿erent across products. For
many to-consumer (2C) products, the interaction is typically
online and self-served, so the life-cycle from receiving the
marketing message to conversion can be just a few days.
For to-business (2B) products, the life-cycle can span weeks
to months, including activities such as lead generation and
sales involvement. As a result, these ML models face issues
associated with delayed feedback.
(3) The action space is complex. There are di￿erent types of
actions to optimize the marketing outcome. These include
(but are not limited to) at what time and frequency the mar-
keting message should be sent, what content (e.g., picture,
language) to use for the message, which audience to target,
how much to bid for the marketing campaign(s) on vari-
ous ads platforms. Unifying these actions under a general
optimization framework would help build a more e￿cient
marketing system.
(4) There are various types of constraints. Marketing typi-
cally comes with cost. Some costs are explicit (e.g., billing
from paid channels), while others are implicit (e.g., com-
plaints or unsubscriptions from users on owned channels).
Besides these cost constraints, there are also other opera-
tional constraints within marketing systems, e.g., capping
on message frequency, minimum volume for various type
of products. An intelligent marketing system should be able
to determine optimal actions while respecting these con-
straints.
To address these challenges, we propose Neural Optimization
with Adaptive Heuristics (NOAH), a general framework for intelli-
gent marketing systems. Before we introduce the framework, we
brie￿y review related ML and optimization works in the marketing
industry and for general recommender systems.
1.1 Related Work
1.1.1 ML in Marketing Industry. The use of ML in marketing has
been fertile over the last decades, given the wealth of data natu-
rally produced by marketing and the capacity of ML tools/methods
to transform data into information that can be used for market-
ing optimization and decision making. For instance, ML solutions
have been proposed and/or applied to multiple domains, for in-
stance: customer segmentation in industries such as retail [ 13, 31],
hospitality [1, 41] and banking [ 32, 42]; customer life time value
(LTV) [18] in industries ranging from gaming [ 11], to e-commerce
[21], to subscription services [ 27]; marketing attribution, in both
multi-touch attribution [37] and marketing mix modelling [ 22]; the
optimization of di￿erent marketing channels, such as email [ 30, 38],
paid search bidding [ 15, 17], display advertising [ 35, 39], among
others. For a comprehensive review of the use of ML in marketing,
we recommend the work presented in [25, 28].
1.1.2 Optimization in Recommender Systems. A commonly used
optimization approach for Recommender systems (RecSys) is the
ranking heuristic, where items are ranked by their relevance scores
and top-ranked items are shown/sent to users. To balance di￿erent
(and sometimes con￿icting) objectives, the relevance score is often
a linear combination of multiple predicted objective values. While a
large amount of research e￿ort has gone into applying ML and AI to
predicting the individual objective values, less work has been done
on how to choose the weights for an optimized linear combination.
In recent years, Linear Programming (LP) has been emerging in
RecSys for its capability of trading o￿ multiple objectives.
LP has been studied closely since the 1940s, and several commer-
cial solvers such as Gurobi [19] and GLPK [29] can give high-quality
solutions for small-moderate instances in reasonable time frames.
However, they cannot scale to industrial-scale problems with bil-
lions or trillions of variables due to memory or computational
constraints. One approach to handle large-scale LPs is to devise
algorithms where certain key quantities can be computed in a dis-
tributed manner. The alternating direction method of multipliers
(ADMM) [7] is one such approach; [ 43] details how ADMM can be
implemented successfully for industrial-scale problems. Another
approach is the primal-dual hybrid gradient (PDHG) method [ 9] for
a class of problems in convex optimization. [ 2] applies the PDHG
method to a saddle-point formulation of LP and adds enhancements
such as diagonal preconditioning, presolving, adaptive step sizes
and adaptive restarting to make the algorithm more e￿cient in
practice.
1.2 Our Approach
NOAH is a general framework for intelligent marketing systems
which consists of three major modules: 1) prediction module, 2)
optimization module and 3) adaptive heuristics module. The predic-
tion module provides predictions of business metrics given possible
marketing actions. The optimization module chooses marketing
actions that optimize the relevant business metrics. The adaptive
heuristics module connects various components of the system to
form a better feedback loop. We ￿rst go over more details of the
NOAH framework in Section 2, including the three NOAH modules
and some illustrative high-level examples. We then walk through a
large scale application to LinkedIn’s marketing engine in Section
3. We also share the real A/B test win results with some learnings
in Section 4 and conclude in Section 5. We would like to highlight
two major contributions of the paper:
(1) As far as we know, this is the ￿rst general framework for
marketing optimization that takes into account both 2B and
2C products, as well as both owned and paid channels.
(2) This is a large-scale application to LinkedIn marketing that
led to a major business win, and we report details of our
learnings and experiences in this paper.
These contributions imply that our approach o￿ers great scope for
improving marketing optimization in general and hence is broadly
useful.
2 NOAH FRAMEWORK
In this section, we will ￿rst give a brief overview of LinkedIn’s mar-
keting system. We then introduce the details of di￿erent modules
and components of the NOAH framework, followed by applica-
tion guidelines and high-level examples for bidding and content
optimization.

Neural Optimization with Adaptive Heuristics for Intelligent Marketing System KDD ’24, August 25–29, 2024, Barcelona, Spain
2.1 Marketing Ecosystem at LinkedIn
LinkedIn is the world’s largest professional network and has prod-
ucts that serve both 2C and 2B needs. As a result, the marketing
system (Figure 1) needs to promote not only 2C products like Pre-
mium but also various 2B products in Talents, Learning, Ads and
Sales lines of business. The marketing system is a heterogeneous
system that involves both a ￿rst-party system and integration with
third-party tools. Marketers interact with the marketing system to
decide the optimal marketing actions for these 2B and 2C products,
including whom the marketing message should be sent to, the best
timing and frequencies for the messages to be sent, what bidding
price or target the keywords or campaigns should be set at (on paid
channel). Once the actions are decided from the Marketing Engine,
the marketing messages are delivered via various owned or paid
channels.
Paid channels include paid search, paid social and other display
ads on third-party platforms, where LinkedIn (as an advertiser) par-
ticipates in ad bidding through various auction mechanisms. Mean-
while, with owned channels, LinkedIn can promote its products on
LinkedIn itself or use the email channel to have direct connections
with customers. When a user clicks on a marketing message from
one of these channels, they are directed to an optimized landing
page where more detailed product information is shown. For 2C
products, the landing page is typically on LinkedIn’s main website
and the purchase can be typically completed in a self-serve manner.
On the other hand, for 2B products the landing page is typically
Linkedin’s 2B micro-site (e.g., https://business.linkedin.com/) where
an inquiry form can be generated for LinkedIn sales personnel to
follow up.
Figure 1: Overview of LinkedIn’s Marketing System.
2.2 NOAH Modules
In order to have a general framework that can handle di￿erent types
of entities and possible actions in owned and paid channels, we ￿rst
abstract out two de￿nitions: marketing unit and a marketing action.
A marketing unit is an entity that a marketing action can be applied
on. For example, in email marketing where we can directly connect
with members and collect engagement data, the marketing unit is
a member and a marketing action (to be optimized) can be whether
to send a particular email to the member. In paid search channels,
assuming marketers can get keyword-level data, the marketing unit
can be a keyword, and a marketing action can be the bid amount
for the keyword.
Figure 2 shows the overall diagram of the NOAH system. The
core engine (inside the large dashed green box) consists of three key
modules: (i) prediction, (ii) optimization, and (iii) adaptive heuristics.
We ￿rst introduce the components outside the core engine so that
the context, inputs and outputs around the core engine are clear.
NOAH is a human-in-the-loop system. Marketers with expert
knowledge de￿ne appropriate marketing units and marketing ac-
tions in the relevant databases. A candidate retrieval process re-
trieves the appropriate set of marketing units and actions from
the databases and feeds them to the core engine. Marketers also
provide input parameters via an UI that can guide the core engine’s
behavior. User engagement feedback and other contextual informa-
tion are also collected as input to the core engine. The core engine
processes these inputs through the three key modules to generate
optimized marketing actions.
Figure 2: NOAH Framework.
2.2.1 Prediction Module. In prediction module, we want to predict
performance metrics for each marketing unit given some marketing
action. Denoting the feature vector for marketing unit D as GD,
feature vector for marketing action 0as G0 and a metric as ~, the
prediction module builds a functional mapping:
~ = 5(GD,G0,G2),
where G2 represents a feature vector for contextual information
other than marketing unit and action (e.g., location, device). The
metrics are typically marketing objectives and constraints related
to user feedback. For example, we can build a functional mapping
for four metrics: click through rate (CTR), conversion rate, pro￿t
per conversion and cost per click (CPC). With these metrics, we
can use the chain rule to connect these conditional probabilities to
estimate the pro￿t per impression and cost per impression, which
can be further used in the optimization module. The functional
mapping 5(·) can be learnt from user feedback data. Depending on
the amount of data available and the maturity of the system, we can
use di￿erent supervised learning methods to estimate 5(·) . If the
amount of data is small and the project is at the initial stage, a simple

KDD ’24, August 25–29, 2024, Barcelona, Spain Changshuai Wei et al.
regression model is often enough. If more data is available and the
project is at the initial stage, an o￿-the-shelf gradient boosted tree
[16] or XGBoost model [ 12] can give decent performance. If data is
abundant and the project is in the iteration phase, we have found
that deep neural networks give the best performance due to their
￿exible architecture. For example, transformer architectures can be
used to generate embeddings for historical marketing interaction
with users. If multiple metrics are being modeled, multi-task learn-
ing architectures like multi-gate mixture-of-experts (MMOE [ 24])
or entire space multi-task model (ESMM [ 26]) can be employed to
exploit the relationship among multiple metrics during training.
One key characteristic of the prediction module is the inclusion
of the marketing action. If the metric prediction is conditioned
on the marketing action, the prediction module can then generate
metric estimates for all possible marketing actions, from which the
optimization module can choose the best action. However, histor-
ical data may not contain all possible marketing actions for each
unit, which may generate bias in inference[ 10]. To reduce the bias,
various causal ML methods can be used so that the 5(·) learnt better
re￿ects the causal relationship [14, 20].
2.2.2 Optimization Module. With the functional mapping of mar-
keting actions and performance metrics, we then need to choose
the best action for a given marketing unit in the optimization mod-
ule. The simplest, widely adopted approach is a ranking approach:
choose the action with the largest ~value, i.e., the largest estimated
metric. While it can often work, this ranking approach ignores
many limitations or constraints that can lead to sub-optimal and
sometimes unacceptable performance.
To address various constraints across marketing units, we can
frame the problem as a constrained optimization problem. For each
metric : = 0, 1,𝑌𝑌𝑌, , let ~: = 5:(GD,G0D ,G2) denote the estimated
value of metric : for marketing unit D under action 0D. Without
loss of generality, let ~0 be the primary metric to be optimized, and
let the remaining ~: (: 1) be metrics that are subject to various
limitations or business constraints with upper bound constraints
⇠:. Assuming no interaction e￿ects across marketing units, we can
formulate the optimization problem:
max0D
’
D
50 (GD,G0D ,G2), (1)
s.t.
’
D
5:(GD,G0D ,G2) ⇠:, 81 :  , (2)
The above optimization problem can be relaxed and solved with
e￿cient linear programming (LP) algorithm in many cases; we de-
tail some examples in Section 2.3 and Section 3.3. When latency
is a strong requirement, some compromises on accuracy need to
be made, for example, to use yesterday’s dual solution for today’s
primal calculation. Fortunately, for marketing AI use cases, latency
is not a major problem as the systems are mostly o￿ine. For exam-
ple, in email marketing, marketers control the time and frequency
and typically limit the frequency to avoid spamming users. In paid
media, marketers only need to change the non-impression-level
bid, e.g., cost-per-click (CPC) bid as the impression-level response
is taken care of by the ads platform. For these reasons, LP is well
suited for marketing AI use cases.
Besides the marketing cost and business constraints on the
"space" dimensions, there are implicit constraints on the "time"
dimension, particularly for each marketing unit. The time window
to attract and convert a potential user is typically limited. Moreover,
a marketing action taken at a given time point can impact the status
and best marketing action to take at the next time point. We can
leverage Reinforcement Learning (RL) to address optimization on
"time" dimension. Contextual bandits can be used to balance the
exploration and exploitation. Q-Learning can be used to help ￿nd
an optimal sequence of marketing actions to maximize value for a
given marketing unit.
To summarize, the optimization module addresses the resource
limitation problem. As a general principle, we recommend LP when
the resource limitation across marketing units is strict and there
are less frequent marketing interactions, and recommend RL when
there are more frequent marketing interactions and less constraints
across marketing units (or these constraints can be taken care of by
other parts of the system). We note that these two techniques are not
mutually exclusive and can be combined. For example, we can focus
on "space" constraints and use an LP formulation, while simplifying
the time horizons resolution to an LTV prediction. We can also
focus on "time" horizons and use an Q-learning formulation, while
transforming the cost constraints implicitly to reward shaping. We
argue that the former combination are often preferred in marketing,
since marketing use cases are typically less frequent interaction
with strict cost constraints.
2.2.3 Adaptive Heuristics Module. Adaptive heuristics (AH) are
lightweight components that help the whole system run stably and
coherently, each of which may have some prediction and optimiza-
tion functionality. We here brie￿y discuss two main classes of AHs
and provide more details in Appendix B.
One important class of AH is Feedback Loop Controllers for busi-
ness constraints (green boxes as shown in Figure 2). Since the mar-
ket is dynamic and the marketing AI system can have errors (e.g.,
prediction error), the observed cost ⇠0may be greater (violation) or
much less (under-utilization) than the budget ⇠. To minimize under-
or over-utilization, we can continuously monitor the performance
and build a lightweight controller, ⇠⇤= 6(⇠,⇠0), to update ⇠⇤as
the input to the optimization module instead of the original ⇠.
Another important class of AH is Hierarchical Optimization, so
that the aggregate-level constraints propagate to lower level. For ex-
ample, a macro-level optimization with a forecasting model and an
LP can be built to allocate marketing budget to di￿erent marketing
channels and products.
2.3 Guidelines and Examples
NOAH is a general framework for marketing AI systems. Ideally,
we would like to perform joint optimization for multiple types of
marketing actions, e.g., product, timing, frequencies and content.
However, this is often infeasible due to reasons such as infrastruc-
ture constraints, operational convenience, or limitations in the ML
models or optimization solvers. As a workaround, we can use the
same NOAH framework and perform optimization in a cascad-
ing/sequential manner for di￿erent types of marketing actions. For
example, we can ￿rst decide the product for each marketing unit,
then optimize the timing and frequencies, and ￿nally choose the

Neural Optimization with Adaptive Heuristics for Intelligent Marketing System KDD ’24, August 25–29, 2024, Barcelona, Spain
best content. Another bene￿t of this muti-stage design is that it al-
lows for a ￿exible combination of di￿erent optimization techniques
for di￿erent actions. Here, we give examples for two di￿erent mar-
keting actions: bidding and content optimization.
2.3.1 Bidding Optimization Example. For bidding, advertisers can
receive hourly or daily ads winning performance metrics G?, for
example, average position for each keyword, or impression winning
percentage for each campaign. One can build a series of models
to predict: number of clicks ~clicks = 5clicks (GD,G?), cost per click
~cpc = 5cpc (GD,G?), conversion rate ~cvr = 5cvr (GD) and revenue
per conversion ~rpc = 5rpc (GD). Note that we can assume ~cvr and
~rpc do not depend on ads winning performance as they happen
after users click the ad and land on the landing page. Typically, ad-
vertisers want to maximize revenue while maintaining certain level
of return-on-ad-spends (ROAS). The corresponding constrained
optimization formulation could be:
max
?(D)
’
D
~rev D,?(D) ,
s.t.
Õ
D~rev D,?(D)
Õ
D~cost D,?(D) ⇠'$(,
where ?represents the index for categorized winning performance,
and
~rev D,? = 5clicks (GD,G?) 5cvr (GD)5rpc (GD),
~cost D,? = 5clicks (GD,G?) 5cpc (GD,G?)𝑌
The constrained optimization problem can be solved with the ef-
￿cient algorithm in Appendix A.1 if the scale is large. Once the
desired optimal G⇤? is obtained, we can calculate the optimal CPC
bid as 0⇤D = 5cpc (GD,G⇤?), which can be directly used in ￿rst price
auction platforms, or as the expected-cost-per-click (ECPC) bid in
second price auction platforms.
2.3.2 Content Optimization Example. Content optimization can
happen at di￿erent stages across di￿erent marketing channels.
Without loss of generality, assume there is a slot on the landing
page where we can show di￿erent creatives 0to di￿erent users D.
We can build an online high-dimensional contextual bandit model
based on following regression model:
d1 (~) = G)F + n, n ⇠#(0,V2),
where G = (GD,G0,GD,0) is feature vector that includes features for
user GD, features for creative G0, and features for the user-creative
interaction GD,0, d(·) is a link function, and ~is observed reward.
Online updates for the posterior distribution of F8 ⇠#(`F8 ,f2F8 )
can be computed e￿ciently using factor graph and expectation
propagation (see algorithm details in Appendix A.2). Thompson
sampling can then be employed to obtain predicted rewards for
di￿erent creatives, and show users the creative with the largest
reward on the landing pages.
3 EMAIL MARKETING APPLICATION
In this section, we report the details of a large-scale application
of the NOAH framework to LinkedIn’s email marketing engine,
including important innovations and learnings.
3.1 Email System
We can think of the email marketing system as a two-stage recom-
mender system: candidates retrieval followed by email optimization
(Figure 6 in Appendix). In the candidate retrieval stage, marketers
create email marketing campaigns for di￿erent products and de￿ne
the audience list for each campaign. In the email optimization stage,
ML models are used to ￿nd the best marketing emails for a selected
group of members, so as to optimize metrics while minimizing
negative member experiences like spamming. The whole system
runs in batches, with emails sent out at regular time intervals (e.g.,
weekly). The system seeks to maximize value for LinkedIn while re-
specting multiple business constraints. Some constraints are global,
e.g., the total number of user unsubscriptions should be less than
a certain value each week, while other constraints are local, e.g.,
each member cannot receive more than certain number of emails
each week.
3.2 Prediction with LTV
LinkedIn faces distinct challenges in predicting marketing perfor-
mance due to the di￿erent nature of 2C and 2B segments, particu-
larly the extended decision-making processes and delayed feedback
for 2B products. To overcome this, we create separate models for
predicting short-term metrics and LTV, then integrate the results
to estimate the long-term metric. Here, the long-term metric @C
is a numeric measure de￿ned by marketers re￿ecting marketing
performance over an extended period C, with short-term metrics
representing observable metrics within a brief timeframe, like con-
version and unsubscription. Notably, conversion is typically de￿ned
di￿erently for 2B and 2C products. In 2B, it often refers to the sub-
mission of a quali￿ed lead, whereas in 2C, a conversion can be
marked by a customer signing up for a free trial.
To predict the short-term metrics, we develop predictive models
forming a functional mapping:
~conv D,0 = 5conv (GD,G0,G2),
~unsub D,0 = 5unsub (GD,G0,G2),
where ~conv and ~unsub represent the predicted conversion prob-
abilities and unsubscription probabilities respectively, GD denotes
the feature vectors of users capturing user pro￿les, demographics,
and other behavioral data, G0 symbolizes the marketing actions un-
dertaken, including the decision to send speci￿c marketing emails
to certain members, and G2 represents other relevant contextual
information that might in￿uence the metrics.
We have a dedicated model to predict the LTV associated with a
given conversion event. We calculate the LTVs as
~ltv D,? = 5ltv (GD,G?,G2)
where ?indexes the product that email campaign 0tries to promote.
We model the real-valued ~ltv using regression equipped with a
gamma loss function, de￿ned as
!=
’
8
h
`8:+ @12 8 exp(`8): i
where : is shape parameter, 8 indexes the observations in training
data, @12 8 is the observed 12-month long-term metric (the ground
truth value) and `8 = ;>6(~ltv 8 ). This is a long time window that

KDD ’24, August 25–29, 2024, Barcelona, Spain Changshuai Wei et al.
makes recent positive engagement unavailable for training (i.e., cen-
sored observations). In order to overcome this issue, we make aux-
iliary LTV predictions at shorter time windows (e.g., 1,3,6 months)
and use the output of those models as features for the main 12-
month LTV prediction. We found that this strategy increases pre-
diction accuracy and allows the model to respond faster to evolving
business trends.
3.3 Constrained and Multi-Objective
Optimization
3.3.1 Formulating the Constrained Optimization Problem. In our
legacy system, a ranking heuristic was used in the email optimiza-
tion stage. For each member, all candidate emails were ranked by a
linear combination of ~conv and ~unsub with ￿xed coe￿cient ^, i.e.,
~conv ^~unsub, and top-ranked emails were sent to the member
with a ￿xed frequency cap. This approach did not optimize the busi-
ness goal directly, and business constraints were only considered
implicitly.
Here we apply the constrained optimization formulation in
Section 2.2.2 to this problem. Let D = 1,𝑌𝑌𝑌,* and 9 = 1,𝑌𝑌𝑌,
index the member and campaigns respectively, and let 0D,9 2
{0, 1} denote the binary action decision of whether send email
9 to member D. We can estimate the total expected long-term met-
ric by Õ D,9 0D,9~conv D,9 ~ltv D,?( 9) , and total expected unsubscription by Õ
D,9 0D,9~unsub D,9 .
Assuming that (i) we allow a maximum of ⇠fcap emails to be sent
to each member, (ii) we must send at least⇠2B and ⇠2C emails for 2B
and 2C products respectively, and (iii) we must have no more than
⇠unsub unsubscription, we can form the constrained optimization
problem as follows:
min0D,9
’
D,9
~conv D,9 ~ltv D,?( 9) 0D,9,
s.t.
’
D,9
0D,9~unsub D,9 ⇠unsub,
’
D
’
92J2B
0D,9 ⇠2B,
’
D
’
92J2C
0D,9 ⇠2C,
’
9
0D,9 ⇠fcap, 8D,
0D,9 2{ 0, 1}, 8D, 9𝑌
where, J2B and J2C denote the email campaigns for 2B and 2C
products respectively.
We recognize the optimization problem as an integer linear pro-
gram (ILP), which can be combinatorially di￿cult to solve [ 36].
Instead, we relax the constraints on the 0D,9’s to allow them to take
on values in the interval ∪0, 1]. The resulting problem is a linear
program (LP) which is tractable (details in Section 3.3.2). We can
interpret non-integer 0D,9 as the probability with which we should
send an email about campaign 9 to member D.
3.3.2 Solving the Large-Scale LP. While there are open-source and
commercial solvers for solving LPs, the size of the LP for our ap-
plication is too large for these solvers. Recall that the optimization
variable 0has dimension * , the product of the number of mem-
bers and the number of campaigns. For a large social network like
LinkedIn, we could have 10-100 millions of members and hundreds
of email campaigns, resulting in tens of billions of variables. To
solve the LP, we turn to DuaLip [4, 33, 34], a large-scale LP solver
that we developed at LinkedIn. We brie￿y outline the algorithm
here.
The LP in 3.3.1 can be written in the following form
min0 ~>0B 𝑌 C 𝑌⇡ 01, 0 D 2B D,D 2{ 1,𝑌𝑌𝑌,* }, (3)
where 0= (01,1, ··· ,01,, ··· ,0*, )2 R* is the vector of decision
variables, ~ is the coe￿cient vector for the decision variables in
the objective, ⇡ is the design matrix in the constraints, 1 is the
constraint budget vector, and BD are additional "simple" constraints,
i.e., it is e￿cient to compute the Euclidean projection onto BD.
In particular, 1 = (⇠unsub, ⇠2B, ⇠2C), and ⇡0 corresponds to
the left-hand side of the ￿rst three constraints from the previous
section. BD corresponds to the remaining two constraints, i.e., box-
cut constraints BD = {0D,9 :0 0D,9 1 89, Õ 90D,9 ⇠fcap}.
Instead of solving the LP (3) directly, we solves a perturbed
version of the LP, which is a quadratic program (QP):
min0 ~>0+ W 2 0>0B 𝑌 C 𝑌⇡ 01, 0 D 2B D,D 2{ 1,𝑌𝑌𝑌,* }, (4)
where W > 0 is a regularization hyperparameter. Dualizing just the
polyhedral constraint ⇡0 1leads to the partial Lagrangian dual
6W(_) = min 02B
n
~>0+ W 2 0>0+ _>(⇡01) o ,
where B = Œ* D=1 BD. Then the problem is transformed to calculate
max_6W(_), assuming strong duality holds. Applying Danskin’s
theorem [6], we know that 6W is di￿erentiable and can explicitly
compute its derivative:
r6W(_) = ⇡ˆ0(_)1,
ˆ0D(_) = ⇧BD

1 W(⇡>_+ ~)D

, (5)
where ⇧BD (·) is the Euclidean projection operator onto BD, and
for a vector Iwith the same dimensions as decision variable 0, ID
denotes the sub-vector with indices corresponding to member D.
Notice that the computation of ˆ0(_) can be parallelized across mem-
bers Dand the box-cut projection ⇧BD can be computed e￿ciently
by leveraging Wolfe’s algorithm[ 40]. As a result, r6W(_) can be
computed e￿ciently. This allows us to use ￿rst-order methods such
as accelerated gradient ascent [ 5] and L-BFGS [23] to obtain _⇤W, the
dual value that optimizes the dual function 6W. From this optimal
dual value, we can obtain optimal primal values 0⇤W via (5):
(0⇤ W)D = ˆ0D(_⇤) = ⇧BD

1 W(⇡>_⇤+ ~)D

,D = 1,𝑌𝑌𝑌,*𝑌
While we obtain the optimal solution for the perturbed prob-
lem and not the original one, [ 4] shows that for su￿ciently small
W values, the perturbed solution is also optimal for the original
problem:

Neural Optimization with Adaptive Heuristics for Intelligent Marketing System KDD ’24, August 25–29, 2024, Barcelona, Spain
3.3.3 Practical Tips for Implementation. We describe a couple of
tips that make DuaLip converge much faster. (A) The choice of
W is associated with a critical trade-o￿: DuaLip’s solving of (4) is
faster if W is larger, whereas DuaLip’s approximate solution of (4)
in a given number of iterations is closer to the solution of (3) if W
is smaller. For one run, we try a grid of W values and choose the
largest W value such that the regularizer part of the objective is
small enough, i.e., the ratio, W0>0 2|~>0| is smaller than some threshold,
say 103. After ￿nding such a W value, we ￿x it and use it for all
future production runs. (B) If ⇡ is ill-conditioned (which typically
happens when di￿erent constraints are on di￿erent scales), we can
re-scale the constraints, i.e., pre-multiply ⇡ and 1 by a suitably
chosen diagonal matrix.
With Dualip, the primal solution will fall on a vertex of BD
with high probability [ 34] when W is su￿ciently small. This means
majority of solutions are already binary, i.e., in {0, 1}. However,
we still need to handle the cases when they are between 0 and 1.
Simple rounding may violate the hard constraint ⇠fcap. We devise a
randomization algorithm, basically sampling the campaign indexes
with probability calculated from the primal solution (Appendix A.3).
The randomization also provide additional bene￿t of balancing
exploration-exploitation.
3.4 Audience Expansion
In the email marketing lifecycle, dedicated marketing teams from
each business unit provide a list of candidate members for each
email campaign. Historically, we have found these candidate mem-
ber lists conservative in scope. To address this, we augment the
provided lists with additional members through an Audience Ex-
pansion (AE) module in which we retrieve additional members
who resemble the members provided by the marketing teams and
append them to the candidate lists. We ￿nd such members via an
approximate nearest neighbors (ANN) algorithm.
Formally, let U denote the overall member base at LinkedIn, let
J denote the set of marketing campaigns, and let Uo 9 ⇢U denote
the set of original candidate members provided by a marketing
team for email marketing campaign 9 2J . We leverage ANN via
locality-sensitive hashing to produce a set
Uexpansion 9 ✓ n D 2U  9 : 9D02U o 9, s.t. kGD GD0k2 X o ,
where, U 9 = U∩U o 9 and Xis a hyperparameter which controls the
size of the expansion audience. Ultimately, we combine the original
audience with expansion audience for each campaign and input
the expanded audience Ue into our optimization engine, where
Ue = – 92J Uo 9 [U expansion 9 .
We have found that as we relax X, there is a trade-o￿ between
wider campaign reach through increased expansion audience size
and diminished incremental expansion audience quality. If X is
too large, a portion of the incremental expansion members added
through AE are so dissimilar to the campaign’s original members
that they are never chosen by the LP to receive the marketing
campaign. Moreover, the computational runtime of both Audience
Expansion and the LP optimization increase in X, so choosing X too
large can lead to additional runtime for minimal gain. This latter
concern about computational e￿ciency is especially important
at LinkedIn’s scale. On the other hand, if X is too small then the
expansion audience itself will be too small to produce a signi￿cant
gain in downstream metrics of interest. We tune X through o￿ine
evaluation to balance these trade-o￿s (Appendix D.3).
4 EXPERIMENT AND RESULT
4.1 O￿line Analysis
We performed extensive o￿ine analysis of prediction models, LP
and AE. Due to space limitation, we only highlight the summary of
o￿ine analysis here and share the details of the results in Appen-
dix D.
• Prediction models evaluation. We discuss classi￿cation
and calibration performance of the two propensity models
5conv and 5unsub (Appendix D.1.1). We also evaluated the
LTV model 5ltv and ￿nd: (i) Gamma loss with auxiliary tasks
can respond faster to market changes, (ii) it performs better
than an alternative modeling approach using survival loss.
(Appendix D.1.2)
• Analysis on LP. We ￿nd that smaller W value leads to better
optimality but can take longer to converge (Appendix D.2.1).
We also validated the high probability of binary primal solu-
tions (Appendix D.2.2). More importantly, we investigated
the fallback strategy of using previous dual solution for cur-
rent LP, and ￿nd that we can maintain 99% value of the
objective if data distribution is stable (Appendix D.2.3).
• Analysis on AE. We evaluated impact of X and discuss
the trade-o￿ between audience size, quality and runtime
(Appendix D.3).
• Simulation before A/B test. We ￿nd that (i) NOAH can
make e￿cient "not-send" decisions through LP where legacy
ranking system can not, and (ii) the combination of AE and
LP helps realize the full potential of the optimization engine.
(Appendix D.4)
4.2 Online Test Design
We design an online A/B test to compare the performance of the
NOAH email system with that of the legacy system. In the test,
we randomly assigned members to treatment arm (NOAH system)
or control arm (legacy system). In addition, we included a third
experimentation arm for the legacy system equipped with AE to
isolate the impact of increasing marketing email volume on its own.
The ￿ow of the test is visualized in Figure 3.
Figure 3: AB Test Flow
The email marketing only covers a small percentage of the mem-
ber base. If the randomization splits on set of all members, the
treatment e￿ect could be diluted. We therefore focus on members

KDD ’24, August 25–29, 2024, Barcelona, Spain Changshuai Wei et al.
that are "available" to receive marketing emails. In particular, we
￿rst randomize all members to 3 buckets, Usplit 1 , where 1 2{ 1, 2, 3}.
For each week C of the experiment, we can expand the original
audience U> C to U4 C with AE. Assuming the experiment runs for )
weeks, the set of members for experiment arm 1can be obtained
as U1, )= – C) Usplit 1 \U 4 C . Note here that for control arm 1 = 1,
the legacy system will rank and send emails only for members in
original audience, i.e., over set of U> C \U split 1 for week C.
Since it is not realistic to wait for 1 year long-term metric @12,
we de￿ne a long-term surrogate index [ 3] YD = Õ ?2PD ~LTVD,? for
each member D, where PD denote the set of products that member
Dconverted during the test period, and ~LTVD,? denotes the expected
1-year long-term metric associated with the conversion on product
? for member D. It is worth noting that although each observation
consists of potentially multiple conversions, through o￿ine analysis
we have discovered that the majority of members convert at most
one time during the test period.
Besides the above primary metric, we also monitor a few sec-
ondary metrics, e.g., email volume, conversions (Conv) as well
as observed long-term metric. In addition, we have other metrics
corresponding to the LP constraints, the key one being unsubscrip-
tions (Unsub), a binary metric indicating whether or not a user
unsubscribed during the test period.
We compare the means of above metrics from di￿erent arms for
statistical testing of treatment e￿ects. It worth noting that long-
term metrics exhibit characteristics of a zero-in￿ated heavy-tail
distribution (Appendix C.1). We performed simulations on type I
error and power of t-test against these distributions, and found that
the standard t-test is actually robust (Appendix C.2). We believe
this result is broadly useful, as alternatives do not suit the needs
of such testing: (1) Winsorization removes the large data points
that actually matter (if not more), (2) Non-parametric tests (e.g.,
Mann-Whitney U test) lack a corresponding treatment e￿ects.
4.3 Online Test Results
4.3.1 Overview. The A/B test results in major wins, one of the
largest in Linkedin algorithmic marketing thus far. An overview
of the results is presented in Table 1. All the numbers in the tables
represent relative di￿erence over the control arm, i.e., ratio of the
di￿erence (between the treatment and control arms) to the mean
value in control. Results that are not statistically signi￿cant are
marked either "neutral" or "not stat sig".
Table 1: Overview of A/B Test Result
Marketing System Surrogate Index Unsub Email Volume
Legacy+AE neutral +8.08% +9.42%
NOAH +2.16% 1 +1.52% +8.44%
1 All percentages are relative to the control arm.
As shown in Table 1, NOAH produces a statistically signi￿cant
positive lift in expected 1-year long-term metric (Surrogate Index)
at the cost of a moderate uptick ( +1𝑌52%) in total unsubscription.
Given that Email Volume is increased by 8𝑌44%, the unsubscription
per email sent is actually reduced, indicating that more relevant
Table 2: Product Type Breakdown
Product Type Surrogate Index 3-Mth Metric 1 Conv
2C not stat sig neutral neutral
2B +13.21% +23.66% +13.30%
1 Observed 3-month long-term metric @3 after test concluded.
emails were sent. By comparison, the legacy ranking system with
AE (Legacy+AE) does not produce a statistically signi￿cant e￿ect
on the long-term metric, and it produces large Unsub increment
(+8𝑌08%), a magnitude similar as Email Volumne increment (+9𝑌42%).
4.3.2 Product Type Breakdown. Historically, we have faced chal-
lenges in developing a uni￿ed marketing system which optimizes
marketing emails for a heterogeneous suite of 2C and 2B products.
Our legacy marketing system tends to optimize for quick sign-up
2C products in spite of these products’ relatively small lifetime
values. On the other hand, campaigns associated with high-LTV 2B
products tend to be neglected.
A breakdown of comparison between NOAH and control into
2C and 2B product types is presented in Table 2. We observe that
NOAH is able to drive a large positive lift in both Surrogate Index
(+13𝑌21%) and total Conv ( +13𝑌30%) for high-LTV 2B products with-
out sacri￿cing these metrics for 2C products. It achieves this lift by
increasing total 2B conversions and shifting the distribution 2B con-
versions toward those with higher Surrogate Index, as visualized
in Appendix Figure 14.
Due to the nature of delayed feedback, we tracked the long-
term metric of conversions happened during A/B test after the test
concluded. We ￿nd that NOAH is able to drive a signi￿cant lift
(+23𝑌66%) in observed 3-month long-term metric (3-Mth Metric)
for 2B products. Similarly to Surrogate Index, we observed distri-
butional shift toward high-value conversions in 3-Mth Metrics, as
shown in Appendix Figure 15.
The breakdown analysis demonstrates that NOAH is able to
lift high value long-term metrics for 2B products while simultane-
ously maintaining 2C acquisition metrics and controlling Unsub.
This holistic behavior is essential for a uni￿ed marketing system
which must support a wide range of campaigns having di￿erent
downstream value.
5 CONCLUSION
In this paper, we introduce various challenges faced when building
an intelligent marketing system and propose a general framework,
NOAH, to address these challenges. We give guidelines on how to
apply the NOAH framework and provided a few high-level exam-
ples. In addition, we report a large-scale application of NOAH to
LinkedIn’s email marketing use case. We discuss important innova-
tions and learnings in the implementation and share results of the
major wins for the corresponding online A/B test.
ACKNOWLEDGMENTS
We thank Shruti Sharma, Maggie Zhang, Divyakumar Menghani,
Aarthi Jayaram, and Rehan Khan for their support of the work. We
also thank our colleagues Michael Ingley, Grinishkumar Engineer,

Neural Optimization with Adaptive Heuristics for Intelligent Marketing System KDD ’24, August 25–29, 2024, Barcelona, Spain
Artem Baranov, Sumukh Sagar Manjunath, Carlos Flores, Shawn
Bianchi, Kim Foo, Kyla Falkenhagen for their collaboration on the
email application and A/B test. Additionally, we’d like to acknowl-
edge Zhiqi Guo, Ming Wu, Miao Cheng and Faisal Farooq for their
contributions and support during the early phase of the work.
REFERENCES
[1] Elaheh Yadegaridehkordi Louis Sanzogni A. Rashid Tarik Kathy Knox Sarminah
Samad Othman Ibrahim Ali Ahani, Mehrbakhsh Nilashi. 2002. Revealing cus-
tomers’ satisfaction and preferences through online review analysis: The case of
Canary Islands hotels. Journal of Retailing and Consumer Services 51, 3 (2002),
331–343.
[2] David Applegate, Mateo Díaz, Oliver Hinder, Haihao Lu, Miles Lubin, Brendan
O’Donoghue, and Warren Schudy. 2021. Practical Large-Scale Linear Program-
ming using Primal-Dual Hybrid Gradient. 20243–20257.
[3] Susan Athey, Raj Chetty, Guido W Imbens, and Hyunseung Kang. 2019. The
surrogate index: Combining short-term proxies to estimate long-term treatment
e￿ects more rapidly and precisely. Technical Report. National Bureau of Economic
Research.
[4] Kinjal Basu, Amol Ghoting, Rahul Mazumder, and Yao Pan. 2020. ECLIPSE: An
Extreme-Scale Linear Program Solver for Web-Applications. Proceedings of the
37th International Conference on Machine Learning , 704–714.
[5] Amir Beck and Marc Teboulle. 2009. A Fast Iterative Shrinkage-Thresholding
Algorithm for Linear Inverse Problems. SIAM Journal on Imaging Sciences 2
(2009), 183–202. Issue 1. https://doi.org/10.1137/080716542
[6] Dimitri P Bertsekas. 1997. Nonlinear programming. Journal of the Operational
Research Society 48, 3 (1997), 334–334.
[7] Stephen Boyd, Neal Parikh, Eric Chu, Borja Peleato, and Jonathan Eckstein. 2011.
Distributed optimization and statistical learning via the alternating direction
method of multipliers. Foundations and Trends in Machine Learning 3 (2011),
1–122. Issue 1. https://doi.org/10.1561/2200000016
[8] Eric Breck, Shanqing Cai, Eric Nielsen, Michael Salib, and D Sculley. 2017. The
ML test score: A rubric for ML production readiness and technical debt reduction.
In 2017 IEEE International Conference on Big Data (Big Data) . IEEE, 1123–1132.
[9] Antonin Chambolle and Thomas Pock. 2011. A ￿rst-order primal-dual algorithm
for convex problems with applications to imaging. Journal of Mathematical
Imaging and Vision 40 (5 2011), 120–145. Issue 1. https://doi.org/10.1007/s10851-
010-0251-1
[10] Jiawei Chen, Hande Dong, Xiang Wang, Fuli Feng, Meng Wang, and Xiangnan
He. 2023. Bias and debias in recommender system: A survey and future directions.
ACM Transactions on Information Systems 41, 3 (2023), 1–39.
[11] Pei Pei Chen, Anna Guitart, Ana Fernández del Río, and Africa Periánez. 2018.
Customer lifetime value in video games using deep learning and parametric
models. In 2018 IEEE international conference on big data (big data) . IEEE, 2134–
2140.
[12] Tianqi Chen and Carlos Guestrin. 2016. Xgboost: A scalable tree boosting system.
In Proceedings of the 22nd acm sigkdd international conference on knowledge
discovery and data mining . 785–794.
[13] Michelle Roehm Derrick S. Boone. 2002. Retail segmentation using arti￿cial
neural networks. International Journal of Research in Marketing 19, 3 (2002),
287–301.
[14] Max H Farrell, Tengyuan Liang, and Sanjog Misra. 2020. Deep learning for
individual heterogeneity: An automatic inference framework. arXiv preprint
arXiv:2010.14694 (2020).
[15] Zhe Feng, Swati Padmanabhan, and Di Wang. 2023. Online Bidding Algorithms
for Return-on-Spend Constrained Advertisers. In Proceedings of the ACM Web
Conference 2023. 3550–3560.
[16] Jerome H Friedman. 2001. Greedy function approximation: a gradient boosting
machine. Annals of statistics (2001), 1189–1232.
[17] Hui Gao and Yihan Yang. 2022. Multi-Head Online Learning for Delayed Feedback
Modeling. arXiv preprint arXiv:2205.12406 (2022).
[18] Sunil Gupta, Dominique Hanssens, Bruce Hardie, Wiliam Kahn, V Kumar,
Nathaniel Lin, Nalini Ravishanker, and S Sriram. 2006. Modeling customer
lifetime value. Journal of service research 9, 2 (2006), 139–155.
[19] Gurobi Optimization, LLC. 2023. Gurobi Optimizer Reference Manual. https:
//www.gurobi.com
[20] Daniel Jacob. 2021. Cate meets ml: Conditional average treatment e￿ect and
machine learning. Digital Finance 3, 2 (2021), 99–148.
[21] Lukáš Kakalejčík, Jozef Bucko, and Martin Vejačka. 2019. Di￿erences in buyer
journey between high-and low-value customers of e-commerce business. Journal
of theoretical and applied electronic commerce research 14, 2 (2019), 47–58.
[22] Ajay Kumar, Ravi Shankar, and Naif Radi Aljohani. 2020. A big data driven frame-
work for demand-driven forecasting with e￿ects of marketing-mix variables.
Industrial marketing management 90 (2020), 493–507.
[23] Dong C. Liu and Jorge Nocedal. 1989. On the Limited Memory BFGS Method for
Large Scale Optimization. Mathematical Programming 45 (1989), 503–528.
[24] Jiaqi Ma, Zhe Zhao, Xinyang Yi, Jilin Chen, Lichan Hong, and Ed H Chi. 2018.
Modeling task relationships in multi-task learning with multi-gate mixture-of-
experts. In Proceedings of the 24th ACM SIGKDD international conference on
knowledge discovery & data mining . 1930–1939.
[25] Liye Ma and Baohong Sun. 2020. Machine learning and AI in marketing–
Connecting computing power to human insights. International Journal of Research
in Marketing 37, 3 (2020), 481–504.
[26] Xiao Ma, Liqin Zhao, Guan Huang, Zhi Wang, Zelin Hu, Xiaoqiang Zhu, and Kun
Gai. 2018. Entire space multi-task model: An e￿ective approach for estimating
post-click conversion rate. In The 41st International ACM SIGIR Conference on
Research & Development in Information Retrieval . 1137–1140.
[27] Edward C Malthouse and Robert C Blattberg. 2005. Can we predict customer
lifetime value? Journal of interactive marketing 19, 1 (2005), 2–16.
[28] Eric WT Ngai and Yuanyuan Wu. 2022. Machine learning in marketing: A
literature review, conceptual framework, and research agenda. Journal of Business
Research 145 (2022), 35–48.
[29] Eiji Oki. 2012. GLPK (GNU Linear Programming Kit). https://api.semanticscholar.
org/CorpusID:63578694
[30] M Paulo, Vera L Miguéis, and Ivo Pereira. 2022. Leveraging email marketing:
Using the subject line to anticipate the open rate. Expert systems with applications
207 (2022), 117974.
[31] Musthofa Galih Pradana and Hoang Thi Ha. 2021. Maximizing strategy improve-
ment in mall customer segmentation using k-means clustering. Journal of Applied
Data Sciences 2, 1 (2021), 19–25.
[32] Omri Raiter. 2021. Segmentation of bank consumers for arti￿cial intelligence
marketing. International Journal of Contemporary Financial Issues 1, 1 (2021),
39–54.
[33] Rohan Ramanath, Sathiya S. Keerthi, Kinjal Basu, Konstantin Salomatin, Pan
Yao, Amol Ghoting, and Miao Cheng. 2022. DuaLip: Dual Decomposition based
Linear Program Solver, version 2.0.0. https://github.com/linkedin/dualip
[34] Rohan Ramanath, S. Sathiya Keerthi, Yao Pan, Konstantin Salomatin, and Kinjal
Basu. 2021. E￿cient Vertex-Oriented Polytopic Projection for Web-scale Appli-
cations. arXiv preprint arXiv:2103.05277, 1–13. http://arxiv.org/abs/2103.05277
[35] Kan Ren, Weinan Zhang, Ke Chang, Yifei Rong, Yong Yu, and Jun Wang. 2017.
Bidding machine: Learning to bid for directly optimizing pro￿ts in display ad-
vertising. IEEE Transactions on Knowledge and Data Engineering 30, 4 (2017),
645–659.
[36] A. Schrijver. 1986. Theory of Linear and Integer programming. Wiley-Interscience.
[37] Xuhui Shao and Lexin Li. 2011. Data-driven multi-touch attribution models.
In Proceedings of the 17th ACM SIGKDD international conference on Knowledge
discovery and data mining . 258–264.
[38] Duncan Simester, Artem Timoshenko, and Spyros I Zoumpoulis. 2020. Targeting
prospective customers: Robustness of machine-learning methods to typical data
challenges. Management Science 66, 6 (2020), 2495–2522.
[39] Vinay Singh, Brijesh Nanavati, Arpan Kumar Kar, and Agam Gupta. 2023. How to
maximize clicks for display advertisement in digital marketing? A reinforcement
learning approach. Information Systems Frontiers 25, 4 (2023), 1621–1638.
[40] Philip Wolfe. 1976. Finding the nearest point in a polytope. Mathematical
Programming 11 (1976), 128–149.
[41] Elaheh Yadegaridehkordi, Mehrbakhsh Nilashi, Mohd Hairul Nizam Bin Md Nasir,
Saeedeh Momtazi, Sarminah Samad, Eko Supriyanto, and Fahad Ghabban. 2021.
Customers segmentation in eco-friendly hotels using multi-criteria and machine
learning techniques. Technology in Society 65 (2021), 101528.
[42] Danuta Zakrzewska and Jan Murlewski. 2005. Clustering algorithms for bank
customer segmentation. In 5th International Conference on Intelligent Systems
Design and Applications (ISDA’05). IEEE, 197–202.
[43] Jun Zhou, Yang Bao, Daohong Jian, and Hua Wu. 2023. PDAS: A Practical
Distributed ADMM System for Large-Scale Linear Programming Problems at
Alipay. Proceedings of the ACM SIGKDD International Conference on Knowledge
Discovery and Data Mining , 5717–5727. https://doi.org/10.1145/3580305.3599883

KDD ’24, August 25–29, 2024, Barcelona, Spain Changshuai Wei et al.
A ALGORITHMS
A.1 Bidding Optimization with Lagrangian
Relaxation
We introduce the constraint into the objective with Lagrangian
relaxation:
6(_) = max
?(D)2{ 1,...,%}
’
D
~rev D,?(D) _

⇠'$(
’
D
~cost D,?(D)  ’
D
~rev D,?(D)
!
=
’
D
max?(D)2{ 1,...,%}
h
(1 + _)~rev D,? _⇠'$(~cost D,?
i
For any ￿xed _= _0, we can get the optimal ?(D) simply by ￿nding
the maximum among % discrete values for each D, i.e.,
?_0(D) = argmax ? {( 1 + _0)~rev D,? _0⇠'$(~cost D,? }, 8D𝑌
Then, we can compute the subgradient with respect to _,
m6(_)|_=_0 =
’
D
~rev D,?_0(D) ⇠'$( ’ D ~cost D,?_0(D)
and use the sign of the subgradient to guide where to ￿nd _that
minimize 6(_).
Algorithm 1 Bidding Optimization with Lagrangian Relaxation
Input: ~revD,?, ~costD,? , ⇠ROAS, _init > 0, and 0 < n ⌧_init
Output: ?⇤(D) for each D
set _<8=  0 and _<0G  _init
if m6(_)|_=0 0 then
return ?0 (D)
else
while m6(_)|_=_<0G < 0 do
set _<8=  _<0G and _<0G  2_<0G
end while
end if
while _<0G _<8= > n do
set _0 _<8= +_<0G 2
if m6(_)|_=_0 > 0 then
set _<0G  _0
else if m6(_)|_=_0 < 0 then
set _<8=  _0
else
break
end if
end while
return ?_0(D)
A.2 Content Optimization with Online
Contextual Bandit
For e￿cient Bayesian online learning, we will assume the priors
for all weights are independent and Gaussian-distributed. The joint
distribution can be written in the following form:
?(~, C, B, F1,F2, ··· ,F:) = ⌘(~, C)0(C,B)6(F1,F2, ··· ,F:,B)
÷
8
A8(F8),
where
A8(F8) = N( F8; `8,f2 8 ),
6(F1, ··· ,F ,B) = X(G)F = B),
0(B, C) = N( C; B, V2),
⌘(~, C) = X(d(C) = ~),
and X(·) is the indicator function.
In the factor graph, the variable nodes {F8,B,C,~ } are connected
by the factor nodes {A8,6,0,⌘ }. We can calculate the posterior dis-
tribution ?(F8|G,~) by message passing in factor graph:
(1) Consider C as root node.
(2) Perform message passing from leaf to root and obtain ?(C) =
N( C; [, g2)⌘(~, C), where [ = Õ 8G8`8, and g2 = Õ 8G2 8f2 8 + V2.
(3) If ?(C) is not Gaussian, we use moment matching to obtain
ˆ?(C) = N( C; `C,f2 C), where `C = [+  and f2 C = g2W.
(4) Perform message passing from root to leaf and obtain poste-
rior of model weights,
?(F8) = N( F8; `F8 ,f2 F8 ),
where,
8>><
>>:
f2F8 = f2 8 ∪1 G2 8 f2 8 g2 (1 W)]
`F8 = `8 + G8 f2 8 g2
With the above, we can have following online contextual bandit
algorithm that works for high-dimensional settings. The algorithm
can be easily parallelized or set up for on-device computing.
Algorithm 2 Content Optimization with Online Contextual Bandit
Input: `8, f2 8 , V2
for time step 9 = 1, 2, ··· , do
Sample ˆF8 from #(`F8 ,f2F8 ) for all 8;
for creative 0= 1, 2, ··· , do
Sample ˆn0 from #(0,V2)
Calculate latent reward ˜C9,0 = ˆn0 + Õ 8G8,9,0 ˆF8
end for
Choose creative 09 = arg max0 ˜C9,0 and show it to user;
observe user engagement and receive reward ~9
Update `F8  `F8 + G8
f2 F8
g2 ;
Update f2F8  f2F8 ∪1 G2 8 f2 F8 g2 (1 W)]
end for
Here, the value of W and  depends on the link function. For
linear regression, W = 0 and  = ~G)F. For Probit regression,
W = 1 s( ~[ g ) and  = ~go( ~[ g ), where, o(C) = N( C;0,1) (C;0,1) and
s(C) = o(C)( o(C)+ C).
A.3 Sampling from Primal Solution
The IP to LP relaxation can be interpreted as transforming the
deterministic integer decision to the expected value of a random
integer decision, i.e., the probability of sending some marketing
email. So naturally we can add a randomization after the LP solution,

Neural Optimization with Adaptive Heuristics for Intelligent Marketing System KDD ’24, August 25–29, 2024, Barcelona, Spain
to "recover" the random integer decision 00 D,9. Formally, we want
to implement the sampling so that:
⇢(00 D,9)/ 0D,9 ’
9
00 D,9 ⇠fcap
We can follow the following algorithm to "recover" the random
integer decision 00 D,9:
(1) Calculate sampling probabilities ?D,9 = 0D,9Õ 9 0D,9
(2) Sample a set J 0D of size bÕ 90D,9 + 0𝑌5cwithout replacement,
from set of all index JD with non-uniform distribution of
?D,9
(3) We obtain 00 D,9 = ( 9 2J 0D), where (·) is indicator function.
B ADAPTIVE HEURISTICS
There are two main classes of AH: 1) Feedback Loop Controller and
2) Hierarchical Optimization. At a high-level, these two classes of
AH help optimize and stabilize the system on the "time" and "space"
dimensions respectively.
Besides the two main classes of AHs, there are other simple
AHs, for example: cool-o￿ rules so that a member cannot receive
more than some number marketing messages over a ￿xed time
window, andn-greedy exploration so that selection bias is measured
and taken into account in modeling. Most of these heuristics are
common to RecSys, and we refer readers to standard practice in
[8, 10].
Figure 4: Feedback Loop Controller
B.1 Feedback Loop Controller
Controllers can observe the feedback from the marketing units, and
is able to adjust input to the main optimization module, so as to
stabilize it when there are deviations on the constraints. This is
particularly useful when we have strict constraints, e.g., marketing
budgets/cost. Technically, this can be achieved either by a Propor-
tional–integral–derivative (PID) controller and/or a lightweight
reinforcement learning (RL) model. Figure 4 shows the overall ￿ow.
Without loss of generality, assume there is a marketing cost
metric ⇠1 we want to monitor and control from the constraint
formulation (2) in Section 2.2.2. The controller takes observed cost
⇠0 1, and other historical data G, and outputs the cost target ⇠⇤ 1
which should be used as the budget in the linear program, i.e.,
⇠⇤ 1 = 6(⇠1,⇠0 1,q(G)) 𝑌
For the case of a PID controller, q(G) represents the three quanti-
ties, proportion, integral, and derivative, which are derived from the
time series of error term 4C(G) = ⇠0 1,C ⇠1,C. Once ⇠⇤ 1 is obtained,
we can use it for main optimization module:
max0D
’
D
50 (GD,G0D ,G2),
s.t.
’
D
51 (GD,G0D ,G2) ⇠⇤ 1,
’
D
5:(GD,G0D ,G2) ⇠:, 82 :  ,
Beside PID controllers, we can also use RL to learn more complex
6(𝑌) and q(𝑌) functions.
B.2 Hierarchical Optimization
The formulation of Hierarchical Optimization is similar to the LP
formulations in Section 2.2.2, except that 1) we use aggregated data
as input, 2) the prediction model can be light-weight, and 3) the
optimization problem is small-scale.
The main use case for hierarchical optimization is macro-level
marketing budget allocation. With slight abuse of notation from
Section 2.2.2, we let D index unit of budget allocation (e.g., com-
bination of marketing channel and lines of business), and let 0D
denote the level of budget to be assigned to unit D. The resulting
optimization formulation is the same as (1) and (2).
The model used in the objective is typically the revenue on bud-
get changes ~0 = 50 (GD,G0D ,G2), where either traditional Media
Mixed Models (MMM) or modern causal ML methods can be used.
Among the constraints, the cost model ~1 = 51 (GD,G0D ,G2) can ei-
ther use learned or rule-based 51 (𝑌) (e.g., assuming cost equals ￿xed
proportion of budget) depending on the maturity of the optimiza-
tion engine. The constrained optimization problem is small-scale,
so we can typically use o￿-the-shelf solvers to solve the original
integer program without LP relaxation.
C ROBUSTNESS OF T-TEST
C.1 Zero-In￿ated Heavy-Tail Metric
We can see that in Figure 5, there is a signi￿cant probability mass at
zero and right side of the distribution is heavy-tailed for Surrogate
Index. Note that the counts on histogram plot is ;>610 scale.
Figure 5: Distribution of Surrogate Index
C.2 Simulation Result for t Test Robustness
We simulate the control and treatment based on zero-in￿ated heavy-
tail data. The control is simulated by- = /G-0, where /G is random

KDD ’24, August 25–29, 2024, Barcelona, Spain Changshuai Wei et al.
binary variable with E∪/G] = ?0, and -0is sampled from a heavy-
tail distribution. The treatment is simulated by . = /~.0, where
E∪/~] = ?0 + ? and E∪log(.0)] = E∪log(-0)] + .
The null model is simulated by setting  = 0 and ? = 0. Besides
varying the size of the test ( U), we also (i) vary ?0 at 0.02 and at 0.8,
(ii) vary distribution of -0at %obs and %ln. Here %obs is empirical
distribution of positive Surrogate Index in AB test, and %ln is log
normal distribution with `(log(-0)) = 2 and f(log(-0)) = 2.W e
perform t-test on the simulated samples and calculated the esti-
mated type 1 errors. We can see type 1 errors are well controlled as
shown in Table 3.
Table 3: Type 1 errors of t test against zero-
in￿ated heavy-tail distribution
U1 -0⇠%obs -0⇠%ln ?0 = 0𝑌02 ?0 = 0𝑌8 ?0 = 0𝑌02 ?0 = 0𝑌8
0.05 0.03038 0.04837 0.02464 0.03917
0.01 0.00227 0.00858 0.00168 0.00524
0.005 0.00072 0.00376 0.00048 0.00211
0.001 0.00002 0.0005 0.00002 0.00031
1 Size of the test.
The alternative model is simulated by varying value of  and
?. For simplicity, we ￿x U = 0𝑌05, ?0 = 0𝑌2 and vary distribution
of -0at %obs and %ln. We can see in Table 4 that power increases as
? increases or as  increases.
Table 4: Power of t test against
zero-in￿ated heavy-tail distribu-
tion
?  -0⇠%obs -0⇠%ln
0 1.0 0.451 0.153
0 2.0 0.909 0.496
0.005 1.0 0.673 0.295
0.005 2.0 0.976 0.637
D OFFLINE ANALYSIS FOR EMAIL
APPLICATION
D.1 Prediction Models Evaluation
D.1.1 Propensity Model Evaluation. We evaluate our propensity
models ~convD,0 = 5conv (GD,G0,G2) and ~unsubD,0 = 5unsub (GD,G0,G2)
using standard o￿ine metrics for binary classi￿cation models, such
as area under the ROC curve (AUC) and area under the precision-
recall curve (AUPR). Average values for these metrics are provided
in Table 5. ROC curves for representative training runs of 5conv
and 5unsub, respectively, are shown in Figure 7. These models are
re-trained on a regular cadence to account for distributional shifts
resulting from evolving member engagement patterns and updated
marketing campaigns.
Table 5: Propensity model o￿line
performance
Propensity Model AUC AUPR
5conv 0.895 0.002
5unsub 0.715 0.002
We also evaluate the calibration performance of our propen-
sity models, as their output estimates serve as the inputs to the
LP. Miscalibration in these estimates can distort the LP’s ability
to optimize accurately, leading to sub-optimal downstream per-
formance. In practice, we ￿nd varying calibration performance
from our propensity models. To address this, we can include an
additional calibration layer via isotonic regression to improve cali-
bration performance. We can then monitor o￿ine metrics such as
Brier score and log-loss before and after calibration to validate the
improvement. An example calibration plot for 5unsub is shown in
Figure 8.
D.1.2 LTV Model Evaluation. We evaluate the performance of LTV
models by comparing the predictions to the observed long term
metric @12 of previous conversion.
To handle "censored observations" for recent conversions, we
leverage auxiliary tasks modeling metric observed for 1 month,
3 month and 6 months, i.e., @1, @3 and @6, and use the predicted
value from auxiliary tasks as input to the main task. We found that
model with auxiliary tasks has lower prediction error and more
importantly, can respond faster to evolving trends on long-term
metric as shown in Figure 9.
Figure 9: Gamma model with and without auxiliary tasks
Alternatively, we can also handle the censored observation by
survival modeling. The long-term metric can be modeled as a prod-
uct of survival time and the long-term metric generated per time
unit, where the second term is modeled using mean squared error
loss. The survival time can be modeled with accelerated failure rate
loss, assuming latent survival time followed log-logistic distribution,
i.e.,
;8 =
(
log(2 + 4
B8 `8
f + 4
`8 B8
f ) if B8 is observed
B8 `8
f + log(1 + 4
`8 B8
f ) if B8 is right censored

Neural Optimization with Adaptive Heuristics for Intelligent Marketing System KDD ’24, August 25–29, 2024, Barcelona, Spain
Figure 6: Two-stage Email Marketing System with NOAH
Figure 7: ROC curves for Conv and Unsub predictions
Figure 8: Calibration curve for Unsub predictions
where, f is scale parameter, B8 = log(C8), C8 is observed survival
time (or right-censored survival time), and `8 = log(~8) is the log
transformation of the predicted survival time.
We show the Spearman correlation between predictions and
@12 for 5 representative product groups under the Survival model
and the Gamma model (with auxiliary tasks) in Table 6. Overall,
the Gamma model has better performance for most of the product
groups. We also show the calibration curve of LTV predictions vs
@12 observation in Figure 10.

KDD ’24, August 25–29, 2024, Barcelona, Spain Changshuai Wei et al.
Table 6: Spearman rank correlation of Survival
and Gamma Models
Product Group Survival Gamma Rel. Di￿.
2C #1 0.448 0.491 +9.6%
2C #2 0.526 0.557 +5.9%
2C #3 0.425 0.489 +15%
2B #1 0.336 0.369 +9.8%
2B #2 0.458 0.396 -13%
Figure 10: Calibration curve for LTV prediction
D.2 Analysis on LP
D.2.1 Impact of W values. For the LP in Section 3.3.1, the two items
that are important are: (a) the value of the primal objective that
is being maximized; and (b) how well the constraints are satis￿ed.
Given a constraint 3) 8 0 18, we can de￿ne a (normalized) quantity,
E8 = max{0, (18 3) 8 0)∝( 1 +| 18|)} that says how much the 8-th
constraint is violated. With many constraints, we can de￿ne a
single violation score called feasibility as max8E8. Figure 11 gives
the DuaLip trajectories (primal objective, feasibility) for various W
values. The vertical line de￿nes the maximum allowed feasibility
violation for our application. Thus, even though during a large part
of an optimization trajectory the primal objective has large values,
they are unacceptable from the feasibility angle. We would choose
the point having the largest primal objective among the acceptable
feasible points to the left of the vertical feasibility line. As expected,
smaller W values yield much better solutions.
D.2.2 Vertex primal solutions. The primal solution 0D,9 for a given
member D and given email campaign 9 will be binary with high
probability. We ran Dualip with W = 108 for multiple di￿erent
datasets from di￿erent weeks. Averaging across these datasets, the
percentage of members with a binary primal solution was 95.81%
(S.E. 0.61%).
D.2.3 Freshness of dual solution. There is a service-level-agreement
(SLA) that the optimization stage has to be completed within a cer-
tain time so that marketing emails can be sent out as planned.
However, there are times when the LP algorithm takes longer than
the SLA to converge. As a fallback strategy when this happens, we
Figure 11: Primal objective vs. feasibility for di￿erentWvalues
use the dual solution (_) saved from the previous period to compute
the primal solution for the current period using (5). The assumption
is that optimality is not impacted much if the data distribution of
the inputs of the LP does not vary much across weeks.
We investigate this assumption by using datasets from consecu-
tive weeks. We ￿rst validated the stableness of the data distribution
week-over-week using the Kolmogorov-Smirnov (KS) statistic (Fig-
ure 13). We then ran the Dualip algorithm for each of the consecu-
tive weeks. For each week, we compare the primal objective value,
i.e., Õ D,9 0D,9~conv D,9 ~ltv D,?( 9) , achieved by the dual solution from Week
0 against that achieved by the current dual solution (Figure 12). The
primal objective achieved by Week 0’s dual never dropped below
99% of that achieved by the current week’s dual.
Week
Primal value achieved (as % of optimal)98.0
98.5
99.0
99.5
100.0
0 1 2 3 4
Week 0 dual Current dual
Primal objective over time (as % of optimal primal objective)
Figure 12: Comparison of primal objective achieved by cur-
rent and Week 0 dual solution

Neural Optimization with Adaptive Heuristics for Intelligent Marketing System KDD ’24, August 25–29, 2024, Barcelona, Spain
Figure 13: Kolmogorov-Smirnov (KS) statistic of data distri-
bution from week C relative to that of week 0
D.3 Analysis on AE
The hyperparameter X controls the size of the incremental expan-
sion audience. As we increase X, both the size of the expansion
audience and the overall runtime of the engine increase, but there
is diminishing marginal audience quality. The relationship between
X and these variables is shown in Table 8.
Table 7: In￿uence ofXon expanded audience size, LP output
size, and overall runtime
X Audience Size LP Output Size Overall Runtime
0.00001 +0.38% +0.33% +4.21%
0.00005 +1.04% +0.95% +4.77%
0.0001 +3.77% +3.23% +15.42%
0.0005 +28.42% +8.44% +16.11%
0.001 >+250% +9.59% >+300%
Audience size and overall runtime increase dramatically in X, but
the LP output size plateaus. This indicates that the quality of the
incremental expansion audience decreases signi￿cantly as we relax
X.
D.4 Simulation before A/B Test
Prior to the launch of the actual A/B test, we conduct o￿ine eval-
uations of our optimization engine using historical data. This as-
sessment aims to understand the engine’s performance compre-
hensively and allow for necessary adjustments, particularly to the
parameters of LP constraints.
D.4.1 Four-Way Comparison. The evaluation is designed to com-
pare four distinct scenarios to understand the optimization engine’s
e￿cacy fully:
• Legacy ranking system with the original audience list (Legacy).
• Legacy ranking system with the AE list (Legacy with AE).
• NOAH optimization system with the original list (NOAH
without AE).
• NOAH optimization system with the AE list (NOAH).
D.4.2 Simulation Result. The comparison results are shown in
Table 8 and 9. All the numbers in the table are relative to the per-
formance of the Legacy ranking system.
Table 8 shows the relative number of members that receives
0, 1 and 2+ Emails. It worth noting that the comparison is based
on counterfactual audience from AE (details in 4.2). We can see
that the rate of sending "0 Emails" is much higher for the two
scenarios that utilized LP ( +92% for NOAH without AE and +158%
for NOAH). This indicates that LP optimization can make e￿cient
"not-send" decision, so that it can reduce spamming and improve
member experience. In fact, the ranking heuristics itself can’t make
"not-send" decision at all.
From Table 9, we can see that NOAH without AE can reduce
Unsub rate by 9%, but only improved long-term metric by 2%. This
suggests that LP’s potential is limited by the original list’s audience
coverage. Meanwhile, with AE widens the top funnel, Legacy rank-
ing system could not control Unsub rate (+9%). It is the combination
of LP and AE that realize the optimization of long-term metrics
(+7%) without negatively impacting member experience.
Table 8: Email distribution
Scenario 2+ Emails 1 Email 0 Emails
Legacy 1.00 1.00 1.00
Legacy with AE 1.19 1 1.08 0.00
NOAH without AE 0.99 0.99 1.92
NOAH 1.16 1.05 2.58
1 all values are relative to the Legacy system.
Table 9: Expected long-term metrics and Unsub
rates
Scenario Emails Volume Long-term Metric Unsub. Rate
Legacy 1.00 1.00 1.00
Legacy with AE 1.12 1 1.05 1.09
NOAH without AE 0.99 1.02 0.91
NOAH 1.09 1.07 0.92
1 all values are relative to the Legacy system.

KDD ’24, August 25–29, 2024, Barcelona, Spain Changshuai Wei et al.
E ADDTIONAL A/B TEST RESULTS
E.1 Distribution of Long-Term Metrics on 2B
Conversions
Figure 14: Distribution of Surrogate Index for 2B Conversions
Figure 15: Distribution of 3-Month Metric for 2B conversions
