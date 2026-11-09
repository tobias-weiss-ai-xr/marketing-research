---
title: AI-Powered Revenue Recognition Models In Multi-Platform Ad Ecosystems
url: https://doi.org/10.29284/8hm66v67
category: privacy-data
subcategory: measurement
date: 2025-01
venue: International Journal of Advances in Signal and Image Sciences
authors:
- Faiz Ur Rahman Khan
source: openalex-oa
pdf_url: https://xlescience.org/index.php/IJASIS/article/download/1337/559
pages: 13
chars: 35940
fetched_at: '2026-11-08T17:34:43+00:00'
kb_version: 1
---

# AI-Powered Revenue Recognition Models In Multi-Platform Ad Ecosystems

Int. J.Adv.Sig.Img.Sci, Vol. 11, No. 5s, 2025
151
AI-Powered Revenue Recognition Models In Multi-Platform Ad
Ecosystems

Faiz Ur Rahman Khan

Bangalore University, Bangalore, India

Abstract
The recognition of revenues in digital advertisement has gotten more complicated as a
result of the expansion of multi -platform ad ecosystems, performance-based strategies of
price, delayed payment systems, and measurement limitations caused by privacy. In these
circumstances, the rule -based accounting methods have difficulty in reflecting the
economic substance of advertising transactions, and result in uncertainty in estimations,
long delays in reconciliation, and increased audit risk. Artificial intelligence can be used as
a viable avenue to overcome these challenges as it can be used to inference the
considerations of the variable at data point based on the goals of dynamic price allocation
and allocating transaction prices, and to identify the recognition in time with the duties of
contractual performance. This paper introduces an artificial intelligence -based revenue
recognition model of heterogeneous advertising platforms, which incorporates attribution
modelling, uncertainty -sensitive prediction, and control-focused governance. The
experiment findings show that model calibration, stability checks, and platform specific
analysis are necessary to deploy to finance -grade. The results show that AI -based
recognition of revenue, in conjunction with good gove rnance and interpretability
procedures, can increase accuracy, timeliness, and transparency in financial reporting in
intricate advertising systems.

Keywords: Artificial Intelligence; Revenue Recognition; Digital Advertising; Multi-Platform
Ecosystems; Accounting Information Systems; Predictive Modelling; Financial Reporting

Introduction
Digital advertising has developed into a multi-platform ecosystem where campaigns are
implemented on search, social, retail media, connected TV and open -web programmatic
transactions, each having different granularities of reporting and settlement policies. This
fragmentation has complicated revenue recognitio n since the amount earned in an
advertising arrangement could be based on a combination of delivery cues (impression,
clicks, views), outcome cues (conversion), and contractual modifications (make -goods,
rebates, chargeback, invalid -traffic credit), which could have latency and
disproportionately low reliability across platforms [1], [2]. Meanwhile, algorithmic
decision-making has risen to prominence in ad delivery and pricing and learning -based
bidding and optimization are currently running at scale in real-time markets [3].
Revenue recognition strength in ad ecosystems is not just vital in financial statement
compliance. The time of recognition and revenue recognition also impacts comparability
among the firms and the decision -usefulness of the performance reported especially
where the new standards increase the information on judgment and disclosures [4]. There
is empirical evidence that when adoption of modern revenue recognition guidance occurs,
it may alter the way revenue information is appreciated by markets and the way financial
data of similar type are reported by different entities, meaning that decision to measure
is economically significant and not procedural [5], [6]. These effects are further increased
in the advertising context characterized by large volume of tra nsactions, price based on
auction dynamics and multi-parties supply chain, where the establishment of a principal
versus agency economics and estimation of a variable consideration may be non -trivial
when the performance and quality signals are probabilistic or contested [4], [6].
Simultaneously, the substrate of ad measurement that was originally based on
reconciliation, which includes cross -site identity and fine -grained user-level tracking, is

Int. J.Adv.Sig.Img.Sci, Vol. 11, No. 5s, 2025
152
limited to privacy-related changes in platform policies and regulatory force. The ensuing
shift to privacy-focused measurement restricts deterministic linkage, augments likelihood
on aggregated reporting and boosts susceptibility in attributing and increme ntal
estimations [2]. This enhances existing technical problems in programmatic advertising,
where consumer issues, in transparent intermediations and disputed measurements can
already overcomplicate the understanding of delivery and performance assertions [1]. As
a result, financial recognition procedures are progressively relying on modelling and
inferences as opposed to their direct view.
Revenue recognition models driven by artificial intelligence are becoming a viable answer
to such dynamics. The modern approaches can be methodologically combined (i) with
causal or time sensitive attribution and conversion modelling to conclude on the value
contribution of touchpoints under delayed outcomes [7], [8], (ii) auction and bidding
analytics which links the behaviour of prices to the anticipated delivery value in real time
market place [3], and (iii) governance based accounting viewpoints that ma ndate
traceability and decision -useful disclosure under ASC 606/IFRS 15 regimes [4] -[6].
Nevertheless, the existing literature is divided: advertising analytics literature tends to
maximize the performance of campaigns without considering the auditability, variability
of contracts, and financial reporting limitations; accounting literature evaluates the effect
of the adoption of standards but hardly considers the platform-stochasticity and data-loss
realities of the modern ad measurement [2], [4] -[8]-[12]. Another feasible disconnect
between quantifying uncertainty and explainability into recognition processes exists to
ensure that models-based accruals, reversals, and adjustments can be justified to auditors
and regulators and be compatible across heterogeneous platform reports [2], [4].
This review looks at how AI approaches can be designed in ways that reflect revenue
recognition requirements (performance obligations, variable consideration, and
disclosure usefulness) to multi -platform advertising ecosystems, (a) aligning model
outputs t o revenue recognition principles (performance obligations, variable
consideration and disclosure usefulness), (b) addressing cross -platform measurement
fragmentation and privacy limits and (c) creating governance controls (validation, drift
monitoring and evidence trails) that transform AI outputs into finance grade outputs.
What follows includes a synopsis of literature underpinning in advertising measurement
and accounting standard issues, an elaboration of methodological trends in AI -based
recognition identification, apparent empirical evidence and implications, and a research
conclusion on what actionable research and what evaluation criteria should be included
in future systems.

Literature Review
It can be helpful preceding the literature review to frame AI-powered revenue recognition
on multi-platform advertising as a measurement-and-accounting issue: the recognition of
revenue is increasingly based on algorithmic -evidence of delivery, performance , and
contractual obligations in walled gardens and open -web intermediaries, and privacy
restrictions and fragmentation of platforms make the results of user -level performance
observable and the estimates made by algorithms less auditable [9], [10]. Recent
advertising studies reveal that the programmatic ecosystems present material risks (e.g.,
placement quality and effectiveness variance) capable of spreading to performance-based
billing and revenue timing decisions [11], and optimization models of demand -side
platforms formalize the decision of bidding and budget allocation choices to deliver and
value signals that finance systems can use as inputs to recognition models [12].
Simultaneously, the study of accounting and auditing indicates that increasing the use of
AI in areas where judgment plays a significant role raises concerns with the explanatory
power, control, and human dependence calibration to maintain the verifiability and

Int. J.Adv.Sig.Img.Sci, Vol. 11, No. 5s, 2025
153
defend ability of model-driven estimates that must comply with assurance and reporting
standards [13], [14]. Research in accounting information systems also shows that
machine learning can organize recognition -related tasks (classification, prediction,
clustering), however , they need to be designed with specific attention to prevent opaque
automation and a lack of correspondence with accounting concepts [15], [16], as well as
new frameworks integrating machine learning and NLP to autonomously infer transaction
attributes to apply these to intelligent recognition tasks [17]. There is also empirical data
in the context of ASC 606 indicating that discretion over variable consideration and
incentives to manage earnings can interact with crisis conditions, which underlies the
significance of strong controls in the situations when algorithmic signals are used to
recognize revenue [18].

Focus Findings (key results and conclusions) Ref
Privacy
constraints in
targeted
advertising
measurement
Synthesizes technical and regulatory drivers of
reduced user-level observability (e.g., tracking limits),
motivating aggregated/Privacy-Enhancing
measurement approaches and raising uncertainty in
attribution-based billing inputs.
[9]
Privacy research
agenda in
advertising
Reviews privacy as a core contextual determinant for
advertising effectiveness and measurement; outlines
research directions that emphasize governance,
transparency, and consumer/market impacts relevant
to platform policy shifts.
[10]
Programmatic
placement quality
and advertising
effectiveness risk
Shows that site quality/placement context can
materially affect outcomes, implying that
heterogeneous inventory risk can distort performance
signals that downstream revenue recognition models
may consume.
[11]
DSP optimization
under generic
auctions
Develops an optimization model for
bidding/allocation/budget spending in RTB settings,
clarifying how auction and constraint mechanics shape
delivery and spend trajectories that finance systems
may treat as contractual performance evidence.
[12]
Explainable AI in
auditing
Provides an XAI-oriented framing for applying
interpretable ML techniques (e.g., LIME/SHAP-style
explanations) to auditing tasks, supporting
transparency requirements when AI informs risk or
estimate assessments.
[13]
Auditor reliance
on AI for complex
estimates
Demonstrates conditions under which auditors
discount or rely on AI advice in complex estimation
settings, highlighting “algorithm aversion”/reliance
calibration issues that matter when revenue estimates
are model-assisted.
[14]
ML in
management
accounting
research
Reviews how ML methods and new data sources map
to management accounting problems; identifies
methodological pathways and cautions for inference,
validity, and managerial use of ML outputs.
[15]

Int. J.Adv.Sig.Img.Sci, Vol. 11, No. 5s, 2025
154
AIS meta-theory
framework for ML
opportunities
Organizes ML applications in accounting research into
task types and design choices; emphasizes aligning
model objectives with accounting constructs to
improve interpretability and usefulness.
[16]
ML + NLP
framework for
accounting
recognition
Proposes a framework combining ML and NLP to
understand transaction nature and automate
intelligent recognition (demonstrated via recognition
modelling), relevant to building scalable recognition
pipelines.
[17]
ASC 606 variable
consideration,
earnings
management, and
continuity
Finds that ASC 606 variable consideration settings
relate to earnings management behaviour and
continuity concerns during crisis conditions,
underscoring control needs around discretion in
revenue estimates.
[18]

Methodology
Multi-platform advertising requires recognition of revenue based on (i) the ability to
quantify delivery and results on fragmented platforms, (ii) the ability to assign
consideration on performance commitments and time, and (iii) generation of auditable
and consistent estimates in uncertainty. The suggested methodology operationalizes such
requirements as an awareness of governance ML pipeline which transforms
heterogeneous ad -event signalling into contract -consistent recognised clearances and
maintain traceability to provide assurance and control testing [19], [23].

1) Study design and scope
The conducted study is presented as a design science / applied analytics approach where
there are three layers that are integrated:
1. Measuring layer: ingestion, normalization, privacy/ consent enforcing, identity
resolving and deduplicating cross platform events.
2. Inference layer: causal/attribution and pricing/allocation models which implement
an estimate of the value earned by the obligation and period.
3. Recognition layer + control layer: rules + ML outputs converted to revenue schedules
with audit logs, uncertainty bounds as well as monitoring triggers [19], [24], [25].
This design has been consistent with the fact that adaptive algorithms can be trusted more
in conditions of increased estimation uncertainty when controls and interpretability cues
are available to promote trust and oversight [23], and that ML can enhance the quality of
accounting estimates when trained on reliable settlement/ ground-truth results [20].

2) End to end pipeline (Block diagram)
Figure 1 displays the pathway between raw ad signals and recognized revenue postings,
and it has a very clear controls loop to ensure change governance and auditability of the
pipeline [19].

Int. J.Adv.Sig.Img.Sci, Vol. 11, No. 5s, 2025
155
Figure 1. Advertising signals to the identified revenue.

Impressions/clicks/conversions (event) multi-platforms are standardised and sent via a
privacy/identity layer , which is then sent via attribution/incrementality models to
approximate attributable outcome. These estimates populate an AI revenue recognition
engine that (a) estimates variable consideration, (b) assigns value to obligations and (c)
decides timing one of which a parallel controls/auditability component documents
lineage, explanations, and monitoring evidence [19], [21], [22].

3) Hypothesized theoretical model (constructs and relationships)
Figure 2 establishes a theoretical framework that has an association between ecological
drivers and recognition outcomes via AI capacity:

Figure 2. Theoretical framework between ecosystem drivers, AI capability, and
outcomes of revenue recognition.

• The completeness, latency, deduplication introduce measurement error resulting
in or affecting the downstream attribution-reliability, and consequently
recognitions accuracy.
• Complexity of contract (multi -deliverables, variable consideration) raises the
uncertainty in model/estimation and needs better governance and calibration.

Int. J.Adv.Sig.Img.Sci, Vol. 11, No. 5s, 2025
156
• Operational risk is moderated by governance and controls (lineage, auditability,
change management) and enables auditors to be prepared to work with AI-based
systems [19].
• These drivers identify the ability of AI models, which in turn impacts the
recognition accuracy (reduced misstatement risk) and recognition timeliness
(shorter close, reduced disputes) [19], [20], [23].
Attribution choice is the decision methodology that survival/time -to-event strategies
have incorporated contributions to hazards by touchpoint [22], whereas Shapley -based
models offer axiomatic credit assignment and diagnosis to accommodate journeys of
multiple stages [21].

4) Target variables, data and labels.
Input (samples): Some of the inputs include the following: timestamped delivery records,
entry/context signals (where allowed), campaign records, pacing/budget records,
conversion records, refunds/credits/chargebacks, and invoice/settlement records.
Supervision targets (labels): settlement -confirmed results (e.g. payable amounts,
makegoods, clawbacks) and performance satisfaction results stipulated in a contract. This
is in line with evidence that ML is optimal in terms of accounting estimates anchore d on
believable, realised results [20].
Primary outputs:
• Period-level recognized revenue amount (including a state of uncertainty)
• Sharing between obligations/campaign components.
• Exception flags: the unusual uplift, the unusual probability of a refund, the drift
signal, or the low-confidence estimates [24], [25].

5) Model set (core algorithms)
An ensemble can be practiced in the form of a set:
1. Estimation of attribution / incrementality.
• Survival/time-to-event attribution to indicate the timing of conversion and the
influence of multi-touch [22].
• Axiomatic consistency checks and counterfactual adjustments in multi-stage journeys
by Shapley-based attribution [21].

2. Estimation and allocation of revenue.
• Supervised regression (e.g., gradient boosting / generalized additive models) of
expected payable value based on observed delivery and contract characteristics; ML
is inspired by the empirical evidence that it can be used in accounting contexts to
enhance the quality of estimates [20].
• Allocation model which assigns estimated value to obligations based on constraint -
sensitive optimization (e.g. nonnegativity, total consideration constraints), and rule
constraints to impose contractual reasoning.

3. Indecision and calibration layer.
• Probabilistic diagnostics of calibration, and correct scoring rules to have both sharp
and well-calibrated estimates to use in the decision and control levels [24].
• Optional conformal prediction to generate distribution -free prediction intervals of
payable value at the point of operational robustness is needed [26].

6) Protocol validation and assessment measures.
Validation is intended to reflect audit/ close objectives:

Int. J.Adv.Sig.Img.Sci, Vol. 11, No. 5s, 2025
157
• Payable value Back-testing vs settlements: MAE/MAPE; allocation error; timing error.
• Calibration: reliability tests and scoring principles to avoid the overconfident
recognition estimates [24].
• Stability against drift: rolling -windows are used to observe degradation in case the
platform policies, the dynamics of an auction or identity constraints change [25].
• Control effectiveness: market coverage percentage; explanation coverage (whether it
is comprehensive); rates and outcomes of overriding (to identify bias in the system)
[19], [23].

7) Governance-aware lifecycle (controls + monitoring)

Figure 3. Lifecycle AI-powered revenue recognition models in governance cognizant.

Figure 3 offers a lifecycle, which is operational: training - validation - deployment -
monitoring - human review/override - model update. Specific artifacts are needed, such
as model cards, data lineage, versioning, access controls, and change approvals, to be
auditable and auditor ready [19]. Constant monitoring is required due to concept drift by
ad ecosystems (policy, seasonality, changes in the auction/bid landscape), which may
cause revenue estimates to be biased silently, should there not be such management [25].
Human reliance is supported by the governance loop, too: adaptive systems are useful in
under uncertainty decisions, but through transparency and oversight, which minimize
perceived risk [23].

Discussion
In this section, representative experimental findings of testing AI -based models of
revenue recognition under multi-platform advertisement settings (heterogeneous signals,
delayed corrections and uncertainty in settlement) are reported. The evaluation plan  is
based on the conventional guidelines regarding measurement of forecast error and
comparison of models, where MAE/MAPE are the main accuracy measures of monetary
estimations [27]. Gradient -boosting techniques on tabular data structured [28] and
scalable tree boosting algorithms commonly used in practice are motivated by model
families. In aid of finance -grade deployment, it further provides calibration diagnostics
and a time-stability (drift proxy) view, which is in line with the focus on explainability and
lifecycle monitoring in black-box model use [30], as well as the challenges of concept drift
in changing data settings [31] known. In cases where the bounds of uncertainty are
needed, the literature of prediction interval encourages interval -based meth ods of
evaluation of point forecasts [32].
Experimental setup (summary)

Int. J.Adv.Sig.Img.Sci, Vol. 11, No. 5s, 2025
158
• Unit of data invoice -level revenue data (N = 5, 000) on 5 platforms and 12 months
(artificial yet structurally realistic).
• Target variable settled revenue (ground truth), which refers to post -adjustment
payable value, accounting for the impact of disputes/credits/latency effects.
• Compared models:
o Rule baseline: platform reward+ simple heuristics with homemade minor
modifications (finance rules + simple heuristics).
o ML (boosted trees): extended covariate feature based payable value estimator.
o ML + calibration/uncertainty: this shrinkage coupled with reduced -variance
estimator will be more stable and easier to audit.

Table 3. General performance indicators

Model MAE (₹) MAPE (%)
Rule baseline 164.30 13.43
ML (boosted trees) 178.61 13.67
ML +
calibration/uncertai
nty
181.64 14.02

Under this experimental set-up the rule baseline had the lowest MAE as domain anchored
heuristics works better than ML in situations where labels are noisy, the features are
imperfect proxies to settlement logic, or the ML model is not constrained enough to
capture contractual structure. The finding is in line with the advice in forecast -accuracy
literature that the comparisons of models are sensitive to both loss choice and data
regimes, and that models that are operationally better need to be evaluated with respect
to the error measure that is operationally relevant [27]. In practical applications, this
drives constraint -sensitive learning (e.g. contract -consistent monotonicity/limits) and
more powerful calibration procedures of ML results [30].

Table 4. Breakdown Platform-level MAE [?]

Platform MAE Rule MAE ML MAE ML+UQ
Search 168.66 186.28 188.38
Social 158.73 171.30 175.93
Retail Media 166.02 178.05 182.03
CTV 182.57 193.08 194.69
Open Web 156.07 173.37 175.10

Higher MAE of CTV is also in line with the environment CTV is more responsive to quality
of delivery and delayed reconciliation, which amplifies volatility in payable value. This
brings out the importance of the explicitly modelling and tracking platform heterogeneity,
as opposed to the assumption of a single homogenous error profile across ecosystems
[31].

Int. J.Adv.Sig.Img.Sci, Vol. 11, No. 5s, 2025
159
Figure 4. Cut-off error of model (MAE)

This bar chart indicates that the rule baseline generates the lowest MAE in such an
experiment, which supports the necessity of finance-grade constraints, transparency, and
governance when ML is applied in the estimation of recognized revenues [30].

Figure 5. Calibration plot of ML + uncertainty model.

This calibration plot compares predicted payable value mean, that is, settled value mean
per prediction bin. The failure to follow the diagonal shows systematic bias (over - or
under-estimation) over some range of values. Calibration checks are critical in the case of
covering the accounting estimates and controls the model outputs, particularly in black -
box learners [30].

Figure 6. Stability of error between months(monthly MAE) drift proxy.

Int. J.Adv.Sig.Img.Sci, Vol. 11, No. 5s, 2025
160
This line chart monitors monthly MAE of each model as a proxy of the drift. Constant MAE
or regime changes are also compatible with concept drift, which is a familiar threat in
changing environments such as multi -platform advertising (policy changes, aucti on
dynamics, reporting changes) [31].

Future Directions
The use of AI -driven revenue recognition in multi -platform advertising systems has
several research directions. To begin with, causal inference and counterfactual learning
should be better applied to the processes of revenue estimation. Predictive models m ay
be used to estimate the payable value but those methods that are causal would be more
appropriate in isolating the incremental performance which can be traced to the exposure
to the advertisement, thus, enhancing the correspondence between the amount of
recognized revenue and the economic substance [33]. Recent developments in causal
machine learning open the way to the reconciliation of attribution accuracy to accounting
defensibility in a setting of partial observability.
Second, explainable and auditable AI is a significant field of work in the future. More and
more, as accounting estimates are based on increasingly complex models, regulators and
auditors need to be able to trace the rationale, consistency and traceability. The studies of
interpretable machine learning show that model explanations may have significant effects
on trust and reliance in high-stakes decision environments, and explainability is a design
goal that warrant first-class consideration instead of a design consideration [34].
Third, an issue with continuous learning under regulatory and market drift is a major
problem. Advertising systems often change the reporting criteria, auctions, and privacy
rules and cause non-stationarity in data distributions. It is the future research that should
examine an adaptive learning approach that does not compromise model validity but
instead, the change-management and approval controls must remain rigid as expected of
the accounting governance [35].
Fourth, enterprise accounting system/standards integration should be further explored.
The gap between AI outputs and enterprise resource planning (ERP) systems, disclosure
requirements and internal controls over financial reporting is not well developed. The
practical adoption would be enhanced by empirical research on the interaction between
AI-assisted estimates and the professional judgment, internal audit functions and external
assurance processes [36].
Lastly, ethical and compliance concerns of algorithmically -driven decision -making in
financial reporting have to be maintained. Propagation of bias, excessive automation and
opacity can bring forth new types of reporting risk unless actively addressed. Fut ure
labour should look at governance systems that will see a balanced approach to
automation, allowing to maintain accountability and human control [37].

Conclusion
AI based revenue recognition models are an important breakthrough in dealing with
structural complexities of contemporary multi -platform advertising systems. Such
systems can be improved to suit uncertain considerations in executing machine learning
by att ribution analytics with uncertainty modelling and governance controls. The
experimental analysis highlights the fact that it is not enough that accuracy is done, but
that there should be calibration, time stability, and transparency to achieve finance grade
deployment. Although there is massive potential in AI methods, the success of such
methods, in turn, will be determined by attentive compliance with accounting standards,
by strong control mechanisms, and by strict lifecycle management. With the ongoing
changes in the advertising ecosystem under the pressure of technology and regulations,

Int. J.Adv.Sig.Img.Sci, Vol. 11, No. 5s, 2025
161
AI-based revenue recognition promises to become a key element of sound, transparent,
and decision-useful financial reporting.

References
1. Samuel, A., White, G. R. T ., Thomas, R., & Jones, P . (2021). Programmatic advertising:
An exegesis of consumer concerns. Computers in Human Behavior, 116, 106657.
https://doi.org/10.1016/j.chb.2020.106657
2. Johnson, G. A., Shriver, S. K., & Goldberg, S. M. (2022). Privacy -centric digital
advertising: Implications for research. Journal of Marketing Analytics.
https://doi.org/10.1007/s40547-022-00125-4
3. Tunuguntla, S., & Hoban, P . R. (2021). A near-optimal bidding strategy for real -time
display advertising auctions. Journal of Marketing Research, 58(1).
https://doi.org/10.1177/0022243720968547
4. Hinson, L. A., Pu  ndrich, G. P ., & Zakota, M. (2024). The decision-usefulness of ASC 606
revenue disaggregation. The Accounting Review, 99(3), 225–258.
https://doi.org/10.2308/TAR-2022-0078
5. (Advances in Accounting). (2024). The effect of ASC 606 adoption on value relevance
of revenues: Early evidence. Advances in Accounting, 68, 100770.
https://doi.org/10.1016/j.adiac.2024.100770
6. Lee, W. J., & Choi, S. U. (2024). The effect of the new revenue recognition principle
(IFRS 15) on financial statement comparability: Evidence from Korea. Journal of
International Accounting, Auditing and Taxation, 54, 100601.
https://doi.org/10.1016/j.intaccaudtax.2024.100601
7. Shender, D., Amini, A. N., Bao, X., Dikmen, M., Richardson Fricke, A., & Wang, J. (2023).
A time-to-event framework for multi-touch attribution. Journal of Data Science.
https://doi.org/10.6339/23-JDS1101
8. Ji, W ., & Wang, X. (2017). Additional multi-touch attribution for online advertising.
Proceedings of the AAAI Conference on Artificial Intelligence, 31(1).
https://doi.org/10.1609/aaai.v31i1.10737
9. Ullah, S., Mian, A. N., Rehman, A., Abbas, H., Shah, G. A., & Cheng, X. (2022). A survey on
privacy in mobile targeted advertising. International Journal of Information Security,
21(6), 1289–1319. https://doi.org/10.1007/s10207-022-00655-x
10. Boerman, S. C., & Smit, E. G. (2023). Advertising and privacy: An overview of past
research and a research agenda. International Journal of Advertising, 42(1), 60 –68.
https://doi.org/10.1080/02650487.2022.2122251
11. Shehu, E., Papies, D., & Neslin, S. A. (2021). The risk of programmatic advertising:
Effects of website quality on advertising effectiveness. International Journal of
Research in Marketing, 38(3), 663–680.
https://doi.org/10.1016/j.ijresmar.2020.10.004
12. Grigas, P ., Lobos, A., Wen, Z., & Lee, K. -C. (2025). Optimal bidding, allocation, and
budget spending for a demand -side platform with generic auctions. Production and
Operations Management. https://doi.org/10.1177/10591478251356002
13. Zhang, C., Cho, S., & Vasarhelyi, M. A. (2022). Explainable artificial intelligence (XAI) in
auditing. International Journal of Accounting Information Systems, 46, 100572.
https://doi.org/10.1016/j.accinf.2022.100572
14. Commerford, B. P ., Dennis, S. A., Joe, J. R., & Ulla, J. W. (2022). Man versus machine:
Complex estimates and auditor reliance on artificial intelligence. Journal of
Accounting Research, 60(1), 171–201. https://doi.org/10.1111/1475-679X.12407
15. Ranta, M., Ylinen, M., & Ja rvenpa a , M. (2023). Machine learning in management
accounting research: Literature review and pathways for the future. European
Accounting Review, 32(3), 607–636.

Int. J.Adv.Sig.Img.Sci, Vol. 11, No. 5s, 2025
162
https://doi.org/10.1080/09638180.2022.2137221
16. Booker , A., Chiu, V., Groff, N., & Richardson, V. J. (2024). AIS research opportunities
utilizing machine learning: From a meta-theory of accounting literature. International
Journal of Accounting Information Systems, 52, 100661.
https://doi.org/10.1016/j.accinf.2023.100661
17. Chen, Y., Huang, X., & Cao, J. (2025). A framework for applying machine learning and
natural language processing methods to accounting recognition. Accounting Horizons,
39(4), 45–55. https://doi.org/10.2308/HORIZONS-2023-093
18. Yassin, M. M., Al -Sraheen, D. A. D., Al Daoud, K. A., Alhadab, M., & Altahtamouni, F .
(2024). Variable considerations in ASC 606, earnings management and business
continuity during crisis. International Journal of Financial Studies, 12(1), Article 1.
https://doi.org/10.3390/ijfs12010001
19. Li, Y., & Goel, S. (2025). Artificial intelligence auditability and auditor readiness for
auditing artificial intelligence systems. International Journal of Accounting
Information Systems. https://doi.org/10.1016/j.accinf.2025.100739
20. Ding, K., Lev, B., Peng, X., Sun, T ., & Vasarhelyi, M. A. (2020). Machine learning improves
accounting estimates: Evidence from insurance payments. Review of Accounting
Studies, 25(3), 1098–1134. https://doi.org/10.1007/s11142-020-09546-9
21. Singal, R., Besbes, O., De sir, A., Goyal, V., & Iyengar , G. (2022). Shapley meets uniform:
An axiomatic framework for attribution in online advertising. Management Science,
68(10), 7457–7479. https://doi.org/10.1287/mnsc.2021.4263
22. Zhang, Y., Wei, Y., & Ren, J. (2014). Multi-touch attribution in online advertising with
survival theory. In 2014 IEEE International Conference on Data Mining (ICDM) (pp.
687–696). IEEE. https://doi.org/10.1109/ICDM.2014.130
23. Ulla, J. W., & Commerford, B. P . (2025). Reliance on algorithmic estimates: The joint
influence of algorithm adaptability and estimation uncertainty. The Accounting
Review, 100(6), 285–308. https://doi.org/10.2308/TAR-2024-0109
24. Gneiting, T ., Balabdaoui, F., & Raftery, A. E. (2007). Probabilistic forecasts, calibration
and sharpness. Journal of the Royal Statistical Society: Series B (Statistical
Methodology), 69(2), 243–268. https://doi.org/10.1111/j.1467-9868.2007.00587.x
25. Hinder, F., Vaquet, V ., & Hammer, B. (2024). One or two things we know about concept
drift—A survey on monitoring in evolving environments. Part A: Detecting concept
drift. Frontiers in Artificial Intelligence. https://doi.org/10.3389/frai.2024.1330257
26. (PLOS Computational Biology). (2025). Conformal prediction for uncertainty
quantification in dynamic models. PLOS Computational Biology.
https://doi.org/10.1371/journal.pcbi.1013098
27. Hyndman, R. J., & Koehler, A. B. (2006). Another look at measures of forecast accuracy.
International Journal of Forecasting, 22(4), 679–688.
https://doi.org/10.1016/j.ijforecast.2006.03.001
28. Friedman, J. H. (2001). Greedy function approximation: A gradient boosting machine.
The Annals of Statistics, 29(5), 1189–1232.
https://doi.org/10.1214/aos/1013203451
29. Chen, T ., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. In
Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge
Discovery and Data Mining (pp. 785–794).
https://doi.org/10.1145/2939672.2939785
30. Guidotti, R., Monreale, A., Ruggieri, S., Turini, F., Pedreschi, D., & Giannotti, F. (2018). A
survey of methods for explaining black box models. ACM Computing Surveys, 51(5),
Article 93. https://doi.org/10.1145/3236009

Int. J.Adv.Sig.Img.Sci, Vol. 11, No. 5s, 2025
163
31. Gama, J., Z  liobaite , I., Bifet, A., Pechenizkiy, M., & Bouchachia, A. (2014). A survey on
concept drift adaptation. ACM Computing Surveys, 46(4), Article 44.
https://doi.org/10.1145/2523813
32. Khosravi, A., Nahavandi, S., Creighton, D., & Atiya, A. F. (2011). Comprehensive review
of neural network-based prediction intervals and new advances. IEEE Transactions on
Neural Networks, 22(9), 1341–1356. https://doi.org/10.1109/TNN.2011.2162110
33. Athey, S., & Imbens, G. W . (2016). Recursive partitioning for heterogeneous causal
effects. Proceedings of the National Academy of Sciences, 113(27), 7353 –7360.
https://doi.org/10.1073/pnas.1510489113
34. Ribeiro, M. T ., Singh, S., & Guestrin, C. (2016). “Why should I trust you?” Explaining
the predictions of any classifier. In Proceedings of the 22nd ACM SIGKDD
International Conference on Knowledge Discovery and Data Mining (pp. 1135–
1144). https://doi.org/10.1145/2939672.2939778
35. Widmer, G., & Kubat, M. (1996). Learning in the presence of concept drift and hidden
contexts. Machine Learning, 23(1), 69–101. https://doi.org/10.1007/BF00116900
36. Appelbaum, D., Kogan, A., & Vasarhelyi, M. A. (2017). Big data and analytics in the
modern audit engagement: Research needs. Auditing: A Journal of Practice & Theory,
36(4), 1–27. https://doi.org/10.2308/ajpt-51684
37. Martin, K. (2019). Ethical implications and accountability of algorithms. Journal of
Business Ethics, 160(4), 835–850. https://doi.org/10.1007/s10551-018-3921-3
