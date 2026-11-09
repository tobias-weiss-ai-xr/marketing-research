---
title: 'Sustained Impact of Agentic Personalisation in Marketing: A Longitudinal Case Study'
url: https://arxiv.org/abs/2604.08621
category: ai-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Olivier Jeunen
- Eleanor Hanna
- Schaun Wheeler
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.08621
pages: 4
chars: 23322
fetched_at: '2026-11-08T13:06:23+00:00'
kb_version: 1
---

# Sustained Impact of Agentic Personalisation in Marketing: A Longitudinal Case Study

Sustained Impact of Agentic Personalisation in Marketing
A Longitudinal Case Study
Olivier Jeunen
aampe
Antwerp, Belgium
Eleanor Hanna
aampe
Raleigh, NC, USA
Schaun Wheeler
aampe
Cary, NC, USA
Abstract
In consumer applications, Customer Relationship Management
(CRM) has traditionally relied on the manual optimisation of static,
rule-based messaging strategies. While adaptive and autonomous
learning systems offer the promise of scalable personalisation, it
remains unclear to what extent “human-in-the-loop” oversight is re-
quired to sustain performance uplift over time. This paper presents
a longitudinal case study analysing a real-world consumer applica-
tion that leverages agentic infrastructure to personalise marketing
messaging for a large-scale user base over an 11-month period.
We compare two distinct periods: anactivephase where mar-
keters directly curated content, audiences, and strategies—followed
immediately by apassivephase where agents operated autonomously
from a fixed library of components. Our results demonstrate that
whilst active human management generates the highest relative
lift in engagement metrics, the autonomous agents successfully
sustained a positive lift during the passive period. These findings
suggest a symbiotic model where human intervention drives strate-
gic initialisation and discovery, yet autonomous agents can ensure
the scalable retention and preservation of performance gains.
1 Introduction & Motivation
Effective Customer Relationship Management (CRM) in consumer
applications relies on the timely delivery of relevant content to re-
engage users [14]. Traditionally, this orchestration has largely been
a manual and iterative endeavour. Marketing teams define static,
rule-based heuristics—segmenting users by demographics or past
behaviour and scheduling campaigns based on intuition or limited
A/B-testing [19]. However, as user bases grow to the millions and
content catalogues expand, this manual approach faces a scalability
bottleneck. The combinatorial complexity of matching the right user
to the right message at the optimal time exceeds human processing
capacity [5], leading to generic “broadcast” strategies that suffer
from diminishing engagement returns whilst failing to deliver truly
personalised user experiences.
To address this scaling challenge, the industry has increasingly
turned to machine learning and autonomous agents to operationalise
personalisation in marketing messaging. The efficacy of this shift
and widespread adoption among leading platforms has been well-
documented: Duolingo [22], Kuaishou [3], LinkedIn [4, 7, 17, 23],
Meta [13], Netflix [8], Pinterest [25], Tencent [24] and Twitter/X [15]
have all pursued this as an active research direction.
Similarly, recent work by Abboud et al . [1] highlights the po-
tential of anagenticframing, moving beyond the narrow view
of personalisation as apredictionproblem, favouring adecision-
theoretic and autonomous lens [9, 11]. These systems promise a
transition from rigid, marketer-defined schedules to adaptive, fluid
engagement strategies that learn continuously from user feedback.
Despite these technological advancements, a critical operational
question remains: what is the long-term role of the human marketer
in an agentic loop? While thetheoreticalcapabilities of reinforce-
ment learning and bandit algorithms suggest fully autonomous
operation, industry practitioners often hesitate to remove human
oversight entirely due to fears of model drift, feedback loops, or mis-
alignment with brand strategy. It remains unclear whether “human-
in-the-loop” management is a constant necessity to prevent per-
formance degradation, or if a more episodic intervention model is
sufficient. Furthermore, much of the existing literature focuses on
short-term A/B-tests, leaving a gap in our understanding of how
these systems behave longitudinally under real-world constraints.
Our work attempts to bridge this gap by presenting a longitudinal
case study of a large-scale deployment of agentic CRM infrastruc-
ture. We focus on a re-activation use-case where messaging targets
users that have not engaged for a given amount of time—an audi-
ence comprising 8.8 million users. We analyse an 11 month long
randomised controlled trial, comparing a distinct phase of active
marketer curation against a subsequent phase of autonomous agent
operation—as visualised in Figure 1. Our contributions are two-fold:
(1) We provide empirical evidence that whilst active human
management drives the highest uplift in performance, au-
tonomous agents are capable of effectively sustaining these
gains over long periods without continuous intervention.
(2) We propose a symbiotic operational model for industry
practitioners, defining clear roles for human creativity in
strategic initialisation and algorithmic agents in scalable
execution.
2 System Description & Background
The experimental platform utilised in this case study is based on the
sequential decision-making framework detailed by Abboud et al.
[1]. We refer the interested reader to their work for a full technical
derivation, and briefly summarise the core components relevant to
this longitudinal analysis. Figure 2 summarises the feedback loop
in which autonomous agents and marketing professionals operate.
2.1 Sequential Decision-Making Formulation
The system frames marketing orchestration as a sequential decision-
making problem under uncertainty. For a given user 𝑢 at time
step 𝑡, the agent observes a state vector 𝑠𝑢,𝑡 (encapsulating user
demographics, past interactions, and app-usage history) and selects
an action 𝑎𝑡 from a composite action spaceA. This action is not a
static template, but a dynamically assembled tuple comprising:
• Content Assembly:the agent selects atomic content com-
ponents (e.g. specific value propositions, greetings, visual
assets) to construct a coherent message.
arXiv:2604.08621v1  [cs.AI]  9 Apr 2026

Olivier Jeunen, Eleanor Hanna, and Schaun Wheeler
Month 0 Month 1 Month 2 Month 3 Month 4 Month 5 Month 6 Month 7 Month 8 Month 9 Month 10 Month 11
Active Management
(Human-in-the-loop)
Passive Follow-up
(Agents act independently)
• Active marketer cooperation,
• New copywriting & semantic labeling,
• Adjustments to audience de/f_initions.
• No active human intervention,
• Static pool of content and components,
• Continued learning and optimisation.
Hand-oﬀ
Figure 1: A timeline describing our longitudinal setup. We analyse 11 months of randomised controlled trial data, where the first
4 months represent an “active management” phase that benefits from dedicated marketing professionals that serve as humans-
in-the-loop. The latter 7 months are a “passive follow-up” where agents act autonomously, whilst learning continuously.
Figure 2: Visualising the feedback loop comprising end users,
marketers, and agents in our setup. From Abboud et al. [1].
• Timing Strategy:the determination of the optimal send-
time (e.g. specific hour of day, day of week, and frequency)
relative to the user’s habitual engagement patterns.
• Channel Selection:the optimal delivery medium (e.g.
push notification, e-mail, SMS) to maximise reach and in-
cremental engagement whilst minimising intrusion.
The agent’s policy 𝜋(𝑎 𝑡|𝑠𝑢,𝑡) learns to maximise a cumulative
reward signal 𝑟𝑡 (e.g. app opens, intent and conversion events) [20].
Specifically, the reward signal is a learnt scalarisation of various
configurable events, augmented with a difference-in-differences
design to measure incrementality [2]. To balance the exploration of
new strategies against the exploitation of known high-performers,
the system leverages Thompson Sampling [18], maintaining a prob-
abilistic distribution over the expected utility of potential actions.
2.2 Human-Agent Interaction
Crucially, the system is designed to scale through a modular con-
tent pipeline. Rather than writing thousands of individual message
variants, “human-in-the-loop” marketers provide the system with
atomic components—such as distinct tones of voice, offer types,
greetings, et cetera. The agentic infrastructure then autonomously
permutes these atoms to generate and serve personalised variants.
This approach has seen various empirical successes [1, 10].
In the context of this study, we treat the underlying algorithm
as a fixed operational substrate. Our analysis focuses specifically
on the longitudinal efficacy of this system when the human supply
and refinement of these atomic components is actively maintained,
versus when it is paused.
3 Experimental Setup
Context & Dataset.The study was conducted in partnership with
a leading multi-vertical consumer delivery application (anonymised
for commercial confidentiality) serving a user base in the millions.
The platform offers a diverse catalogue ranging from restaurant
delivery to grocery and retail goods. The experiment utilised an
industry standard randomized controlled trial design [12]. Users
were randomly assigned to either a treatment group, managed by
the agentic infrastructure, or a holdout control group receiving the
platform’s standard business-as-usual (BAU) messaging logic.
This trial focused on areactivationuse-case, where users were
considered messageable if they had been inactive for a given amount
of time. This yielded a total audience of roughly 8.8 million users
with a 90-10% split across Agentic and BAU respectively.
Timeline & Metrics.The longitudinal analysis spans an 11-month
period, divided into two distinct operational phases to evaluate the
interplay between human strategy and autonomous execution. Fig-
ure 1 visualises this dichotomy between anactiveandpassivephase.
We evaluate performance across the full conversion funnel, focusing
on user retention. Our primary metrics measure the number of days
a user performs a given activity on the application—higher numbers
not only reflect more activity, but also retention of returning users.
We includeEngagement(any positive logged interaction),Direct
Opens(attributed directly from clicks on push notifications),In-
tent(upper funnel events), andConversions(lower funnel events).
We also monitorGross Merchandise Value(GMV) to ensure that
engagement and conversion lifts translate into economic impact.
Statistical Methodology.To quantify the impact of the agentic
system, we calculate the relative lift (Δ) between the treatment and
holdout groups. Our longitudinal design, incorporating a persis-
tent holdout group, effectively controls for temporal dynamics. By
measuring the Δ between treatment and control at each time step,
we ensure that external factors—such as weekly periodicity and
seasonal demand fluctuations—affect both groups equally and thus
do not confound the performance attribution. Given the high vari-
ance inherent in consumer behaviour data (attributable to sparse
conversion events), we employ ML-RATE to reduce estimation
variance whilst retaining unbiasedness in our average treatment
effect estimates [6]. The Delta method provides asymptotic variance
estimates for the relative uplift estimand [16, Ch. 2].

Sustained Impact of Agentic Personalisation in Marketing
+0.0 +0.5 +1.0 +1.5 +2.0 +2.5 +3.0
Relative Li/f_t in Metric (ˆµ∆ ± SE)
Conversion⋆
Conversion
Intent
Engagement
Active Phase Passive Phase
Figure 3: Relative lift across metrics and phases.
4 Results & Discussion
The Value of the Human-in-the-Loop.During theactiveman-
agement phase, the influence from human marketers to guide au-
tonomous agents yielded the largest incremental lift in performance
metrics. As shown in Figure 3, results are unilaterally positive across
all funnel stages relative to control.
Not visualised but notably—we observed a +65.3% (±1.31) in-
crease in days with direct app opens attributable to push notifica-
tions, validating the agents’ ability to optimise composite messaging
strategies effectively. Overall days with positive engagement were
up by +2.8% (±0.19), days with intent by +0.3% (±0.23), and days
with conversions by +0.3% (±0.24). Agentic messaging especially
favoured conversions within a given vertical that is important to
the business (Conversion★), up by+1.2%(±0.62).
We have validated that these findings translate to proportional
updates in GMV (i.e. no adverse effects on conversion magnitude).
Sustained Impact & Robust Autonomy.A key finding of this study
is the system’s resilience during thepassivephase. Despite the ces-
sation of manual content injection and optimisation for 7 months,
performance across funnel metrics did not revert to the baseline ex-
pectation of the BAU experience. Autonomous agents successfully
sustained a +57%(±0.11) lift in notification clicks, +2.4% (±0.21)
days with engagement per user, and a +0.2% (±0.27) lift in intent
and conversion metrics. This validates that the infrastructure is not
merely a delivery layer for human-managed message orchestration,
but possesses an intrinsic ability to learn and adapt to user pref-
erences over time, preventing the “cliff-edge” decay often seen in
static rule-based campaigns.
Implications: A Symbiotic Model.Whilst the passive phase con-
firms robustness, the delta between phases reveals the tangible
value of human oversight. The transition to fully autonomous op-
eration resulted in a relative dampening of lift: roughly−15% for
overall engagement,−12%for notification opens, and−26%for days
with intent and days with conversion events per user—compared to
the uplift observed during the active phase. These results suggest a
symbiotic operating model for industry practitioners:
Strategic Initialisation. Active human-in-the-loop manage-
ment acts as a performance multiplier, necessary for driving initial
lift, strategic discovery, and setting up a component library.
Autonomous Maintenance. Agents serve as a high-fidelity
retention layer, sustaining gains and ensuring that performance
remains significantly above baseline even when human attention
is diverted elsewhere.
We additionally studied the trend in relative uplift over time,
observing a clear pattern across all metrics: a rising trend during
the active management period, a plateauing trend during the first 4
months of the passive period, and a declining trend towards the end
of the trial. This reinforces our view that agents independently sus-
tain performance improvements brought by an initial, human-led,
strategic effort to set up a component library—for a period spanning
several months. Nevertheless, active human-agent management
and cooperation maximises potential and sustained impact.
5 Conclusions & Outlook
Customer Relationship Management and marketing messaging
are moving from rule-driven strategies to autonomous, adaptive,
learned personalisation systems. This shift brings along questions
regarding the long-term feasibility and resilience of such systems
under varying human-in-the-loop dynamics.
In this paper, we presented a longitudinal analysis of an agentic
personalisation system deployed in a large-scale consumer appli-
cation over an 11-month period. By contrasting a phase of active
human management against a subsequent phase of autonomous
operation, we quantified both the operational resilience of agentic
systems and the specific value-add of marketing professionals.
Our results challenge the dichotomy that CRM must be either
fully manual or autonomous. We propose a symbiotic model:
Agents as the Baseline:The agentic infrastructure success-
fully maintained positive lift (i.a. +57% in direct opens) even af-
ter 7 months of independent operation, proving that autonomous
systems can prevent a steep performance decay that is typically
associated with static rule-based campaigns.
Humans as the Multiplier:Active human management pro-
vided a critical “performance premium” (an additional∼12–26% lift),
suggesting that human intervention remains essential for strategic
novelty and creative refreshment.
Future Outlook: Generative Augmentation.Whilst this study lever-
ages human-authored “atomic content” components, the natural
evolution of this framework lies with generative models. The cur-
rent bottleneck—manual production of diverse message variants for
the agents to experiment with—is a prime candidate for automation
via Large Language Models (LLMs).
Nevertheless, these models come with their own sets of chal-
lenges regarding steerability, hallucinations, and consistency [21].
Recent work has started to look into these applications areas, re-
porting operational successes [3]. These systems could potentially
help close the gap between the “active” and “passive” phases ob-
served in this study, enabling the agent not just toselectthe best
available content components that are available, but to dynamically
createthe optimal message for every user context.
References
[1] Sami Abboud, Eleanor Hanna, Olivier Jeunen, Vineesha Raheja, and Schaun
Wheeler. 2025. Agentic Personalisation of Cross-Channel Marketing Experiences.
InProceedings of the Nineteenth ACM Conference on Recommender Systems (RecSys
’25). ACM, 907–910. doi:10.1145/3705328.3748125
[2] Susan Athey and Guido W. Imbens. 2006. Identification and Inference in Non-
linear Difference-in-Differences Models.Econometrica74, 2 (2006), 431–497.
doi:10.1111/j.1468-0262.2006.00668.x
[3] Shifu Bie, Jiangxia Cao, Zixiao Luo, Yichuan Zou, Lei Liang, Lu Zhang, Linxun
Chen, Zhaojie Liu, Xuanping Li, Guorui Zhou, Kaiqiao Zhan, and Kun Gai. 2025.

Olivier Jeunen, Eleanor Hanna, and Schaun Wheeler
PushGen: Push Notifications Generation with LLM. arXiv:2512.14490 [cs.IR]
https://arxiv.org/abs/2512.14490 To appear in WSDM ’26.
[4] Yan Gao, Viral Gupta, Jinyun Yan, Changji Shi, Zhongen Tao, PJ Xiao, Curtis
Wang, Shipeng Yu, Romer Rosales, Ajith Muralidharan, and Shaunak Chatterjee.
2018. Near Real-time Optimization of Activity-based Notifications. InProceedings
of the 24th ACM SIGKDD International Conference on Knowledge Discovery &
Data Mining(London, United Kingdom)(KDD ’18). Association for Computing
Machinery, New York, NY, USA, 283–292. doi:10.1145/3219819.3219880
[5] Carlos A. Gomez-Uribe and Neil Hunt. 2016. The Netflix Recommender System:
Algorithms, Business Value, and Innovation.ACM Trans. Manage. Inf. Syst.6, 4,
Article 13 (Dec. 2016), 19 pages. doi:10.1145/2843948
[6] Yongyi Guo, Dominic Coey, Mikael Konutgan, Wenting Li, Chris Schoener, and
Matt Goldman. 2021. Machine Learning for Variance Reduction in Online Exper-
iments. InAdvances in Neural Information Processing Systems, Vol. 34. Curran
Associates, Inc., 8637–8648.
[7] Rupesh Gupta, Guanfeng Liang, Hsiao-Ping Tseng, Ravi Kiran Holur Vijay, Xi-
aoyu Chen, and Romer Rosales. 2016. Email Volume Optimization at LinkedIn.
InProceedings of the 22nd ACM SIGKDD International Conference on Knowledge
Discovery and Data Mining(San Francisco, California, USA)(KDD ’16). Asso-
ciation for Computing Machinery, New York, NY, USA, 97–106. doi:10.1145/
2939672.2939692
[8] Grace Huang. 2020. Mesa: Building a Personalized Messaging System at Net-
flix. Data Council. https://aicouncil.com/talks/mesa-building-a-personalized-
messaging-system-at-netflix Accessed: 2026-02.
[9] Olivier Jeunen, Thorsten Joachims, Harrie Oosterhuis, Yuta Saito, and Flavian
Vasile. 2022. CONSEQUENCES — Causality, Counterfactuals and Sequential
Decision-Making for Recommender Systems. InProc. of the 16th ACM Confer-
ence on Recommender Systems (RecSys ’22). ACM, 654–657. doi:10.1145/3523227.
3547409
[10] Olivier Jeunen and Schaun Wheeler. 2026. Behavioural Effects of Agentic Messag-
ing. InAdvances in Information Retrieval. Springer Nature Switzerland, 105–110.
[11] Thorsten Joachims, Ben London, Yi Su, Adith Swaminathan, and Lequn Wang.
2021. Recommendations as Treatments.AI Magazine42, 3 (Nov. 2021), 19–30.
[12] Ron Kohavi, Diane Tang, and Ya Xu. 2020.Trustworthy online controlled experi-
ments: A practical guide to A/B testing. Cambridge University Press.
[13] Christian Kroer, Deeksha Sinha, Xuan Zhang, Shiwen Cheng, and Ziyu
Zhou. 2023. Fair Notification Optimization: An Auction Approach.
arXiv:2302.04835 [cs.GT] https://arxiv.org/abs/2302.04835
[14] Vineet Kumar and Werner Reinartz. 2018.Customer relationship management.
Springer.
[15] Conor O’Brien, Huasen Wu, Shaodan Zhai, Dalin Guo, Wenzhe Shi, and
Jonathan J Hunt. 2022. Should I send this notification? Optimizing push no-
tifications decision making by modeling the future. arXiv:2202.08812 [cs.IR]
https://arxiv.org/abs/2202.08812
[16] Art B. Owen. 2013.Monte Carlo theory, methods and examples.
[17] Prakruthi Prabhakar, Yiping Yuan, Guangyu Yang, Wensheng Sun, and Ajith
Muralidharan. 2022. Multi-objective Optimization of Notifications Using Offline
Reinforcement Learning. InProceedings of the 28th ACM SIGKDD Conference
on Knowledge Discovery and Data Mining(Washington DC, USA)(KDD ’22).
Association for Computing Machinery, New York, NY, USA, 3752–3760. doi:10.
1145/3534678.3539193
[18] William R. Thompson. 1933. On the Likelihood that One Unknown Probability
Exceeds Another in View of the Evidence of Two Samples.Biometrika25, 3/4
(1933), 285–294. http://www.jstor.org/stable/2332286
[19] A. Caroline Tynan and Jennifer Drayton. 1987. Market segmentation.Journal of
Marketing Management2, 3 (1987), 301–335. doi:10.1080/0267257X.1987.9964020
[20] Flavian Vasile, David Rohde, Olivier Jeunen, and Amine Benhalloum. 2020. A
Gentle Introduction to Recommendation as Counterfactual Policy Learning. In
Proc. of the 28th ACM Conference on User Modeling, Adaptation and Personalization
(UMAP ’20). ACM, 392–393. doi:10.1145/3340631.3398666
[21] Schaun Wheeler and Olivier Jeunen. 2025. Procedural Memory Is Not All You
Need: Bridging Cognitive Gaps in LLM-Based Agents. InAdjunct Proceedings
of the 33rd ACM Conference on User Modeling, Adaptation and Personalization
(UMAP Adjunct ’25). Association for Computing Machinery, New York, NY, USA,
360–364. doi:10.1145/3708319.3734172
[22] Kevin P. Yancey and Burr Settles. 2020. A Sleeping, Recovering Bandit Algorithm
for Optimizing Recurring Notifications. InProceedings of the 26th ACM SIGKDD
International Conference on Knowledge Discovery & Data Mining(Virtual Event,
CA, USA)(KDD ’20). Association for Computing Machinery, New York, NY, USA,
3008–3016. doi:10.1145/3394486.3403351
[23] Yiping Yuan, Ajith Muralidharan, Preetam Nandy, Miao Cheng, and Prakruthi
Prabhakar. 2022. Offline Reinforcement Learning for Mobile Notifications. In
Proceedings of the 31st ACM International Conference on Information & Knowl-
edge Management(Atlanta, GA, USA)(CIKM ’22). Association for Computing
Machinery, New York, NY, USA, 3614–3623. doi:10.1145/3511808.3557083
[24] Yuchen Zhang, Mingjun Zhao, Chenglin Li, Weiyu Tou, Haolan Chen, Di Niu,
Cunxiang Yin, Yancheng He, and Fei Guo. 2023. Online Volume Optimization for
Notifications via Long Short-Term Value Modeling. InAdvances in Knowledge
Discovery and Data Mining, Hisashi Kashima, Tsuyoshi Ide, and Wen-Chih Peng
(Eds.). Springer Nature Switzerland, Cham, 16–28.
[25] Bo Zhao, Koichiro Narita, Burkay Orten, and John Egan. 2018. Notification
Volume Control and Optimization System at Pinterest. InProceedings of the 24th
ACM SIGKDD International Conference on Knowledge Discovery & Data Mining
(London, United Kingdom)(KDD ’18). Association for Computing Machinery,
New York, NY, USA, 1012–1020. doi:10.1145/3219819.3219906
