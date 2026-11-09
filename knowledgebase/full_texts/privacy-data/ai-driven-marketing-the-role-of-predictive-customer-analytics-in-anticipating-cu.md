---
title: 'AI-Driven Marketing: The Role of Predictive Customer Analytics in Anticipating Customer Behaviour,
  Personalising Campaigns, and Marketing Decision-Making'
url: https://doi.org/10.33774/coe-2026-sp6h1
category: privacy-data
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Neelabh Krishna Trivedi
source: openalex-oa
pdf_url: https://www.cambridge.org/engage/api-gateway/coe/assets/orp/resource/item/6ab90f184770e67d9246a95f/original/ai-driven-marketing-the-role-of-predictive-customer-analytics-in-anticipating-customer-behaviour-personalising-campaigns-and-marketing-decision-making.pdf
pages: 20
chars: 55218
fetched_at: '2026-11-08T17:44:48+00:00'
kb_version: 1
---

# AI-Driven Marketing: The Role of Predictive Customer Analytics in Anticipating Customer Behaviour, Personalising Campaigns, and Marketing Decision-Making

AI-Driven Marketing: The Role of Predictive Customer Analytics in Anticipating
Customer Behaviour, Personalising Campaigns, and Marketing Decision-Making

Author: Neelabh Krishna Trivedi, Scholar- Business Analytics, Institute of Management
Sciences, University of Lucknow, Lucknow INDIA
Email: tneelabh.2001@gmail.com
Abstract
This paper examines how predictive customer analytics is changing marketing. It focuses on three
connected themes: anticipating c ustomer behaviour, personalising campaigns, and supporting
marketing decisions. The central problem is that a model can predict who is likely to buy or leave
without indicating who will change in response to a particular message, offer, or channel. In other
words, prediction is not the same as cause.
The review brings together research on churn prediction, purchase forecasting, customer lifetime
value, recommendation systems, triggered communication, advertising measurement, marketing-
mix models, concept drift, privacy, and AI governance. It compares what the evidence supports
with the claims often made about marketing AI. The analysis also considers whether results
remain reliable when customer behaviour, markets, platforms, or consent conditions change.
The findings show that predictive tools can improve ranking, targeting, and planning in particular
settings. However, personalization can also create fatigue, crowding out, choice overload,
substitution, and p rivacy concerns. Attribution and predictive fit do not prove causal  return on
investment. The evidence for fully autonomous strategic marketing decisions is weaker than the
evidence for bounded decision support.
The paper therefore recommends an experiment -calibrated, privacy-aware, drift-resilient causal
policy layer. This approach uses predictive scores, but tests actions against a control or baseline,
measures incremental economic and customer outcomes, monitors subgroup and long -term
effects, and  keeps human accountability. The main  conclusion is that marketing AI should
improve decisions without removing responsibility.

Keywords: artificial intelligence, predictive customer analytics, marketing personalisation,
causal inference, concept drift.

https://doi.org/10.33774/coe-2026-sp6h1 Content not peer-reviewed by Cambridge University Press. License: CC BY 4.0

GRAPHICAL ABSTRACT

Source: Author

https://doi.org/10.33774/coe-2026-sp6h1 Content not peer-reviewed by Cambridge University Press. License: CC BY 4.0

1. INTRODUCTION
AI-driven marketing has moved from  descriptive segmentation toward systems that forecast
customer behaviour and recommend or execute actions. Firms use transaction histories, browsing
events, campaign exposures, customer -service records, product data, and media signals to
estimate churn, purchase probability, customer lifetime value, lead intent, and likely response to
an intervention. The commercial promise is substantial, but three different claims are often treated
as one. A model may  predict who is likely to buy  without showing who will  buy because of a
message. A campaign may increase attributed conversions without creating incremental demand.
A system may automate a decision without proving that the decision is valid, profitable, fair, or
lawful.
This distinction matters because marketing decisions are interventions in an evolving social and
economic system. Targeting changes exposure, exposure changes behaviour, and the resulting
behaviour becomes training data for the next model. Such feedback can create selection bias,
popularity loops, over-contact, and false confidence. The central problem is therefore not whether
machine learning can improve a benchmark score. It is whether predictive analyti cs can be
integrated into marketing decision architectures in a way that produces  incremental value under
concept drift, incomplete observation, uncertain attribution, and human and regulatory constraints.
This review covers three operational pillars: beha vioral anticipation; campaign personalization;
and strategic marketing decision-making. It distinguishes four evidence states:
Demonstrated: supported within a defined empirical setting, preferably by experiments or
repeated peer-reviewed evidence. - Conditional: plausible or supported only when data, causal,
operational, and governance assumptions hold. - Qualified or contradicted: broad managerial
claims weakened by evidence of non -monotonicity, substitution, selection, or harm. -
Unsupported extrapolation: a plausible claim for which the cited literature  does not establish
generality.
Predictive performance is not treated as causal evidence. ROI is not treated as established unless
the analysis specifies the estimand, treatment and comparison, exposure opportunity, costs and
margins, time horizon, and uncertainty.

2. LITERATURE REVIEW
2.1 From statistical segmentation to machine-learning forecasting
Traditional segmentation describes groups. Predictive analytics estimates an outcome for a
customer, account, household, or market unit at a future horizon. The literature shows that
dynamic recency-frequency-monetary (RFM) features, transaction and usage histories, tenure,
product relationships, and behavior -change signals can improve churn or purchase forecasts
relative to static demographic variables in specific datasets. Recurrent and ensemble models often
perform well. However, reviews report substantial heterogeneity across datasets, class imbalance,
https://doi.org/10.33774/coe-2026-sp6h1 Content not peer-reviewed by Cambridge University Press. License: CC BY 4.0

interpretability problems, concept drift, meaning changes in the data-generating relationship over
time, and limited eval uation of  deployed profit. There is no demonstrated universal winner
between logistic regression, tree ensembles, recurrent neural networks, transformers, or other
deep architectures.
Customer lifetime value (CLV), meaning the expected future value of a cu stomer over a defined
horizon, adds a financial horizon to prediction. CLV models formalize expected future
transactions, retention or attrition, margin, cost -to-serve, discounting, and sometimes marketing
effects. This makes CLV more decision -relevant tha n a generic propensity  score, but it also
introduces more assumptions. Long-horizon CLV is  sensitive to the discount rate, margin
forecasts, censoring, non-contractual inactivity, returns, cross-buying, price changes, and future
interventions. CLV should therefore be reported with sensitivity analysis and uncertainty, not as
observed truth.
Lead and intent scoring is less mature than its vendor language suggests. The literature establishes
that browsing, email, contact, and historical  opportunity data can rank purchase probability.  It
provides much weaker evidence that a score changes sales outcomes, because conversion labels
also reflect eligibility,  sales capacity, contact attempts,  inventory, pricing, and salesperson
selection. A lead score can learn the organization’s prior routing policy rather than intrinsic intent.
2.2 Behavioural anticipation as a sequence problem
A further development in  predictive marketing is  the shift from  static customer attributes to
sequences of events. A single purchase, click, or service complaint is often less informative than
the order and timing of several events. For example, declining usage followed by repeated service
contacts may signal a different risk state from declining usage alone.
Sequence-based models can capture these transitions. However, they also make the data -
generating process harder to interpret. The model must distinguish a genuine change in
customer behaviour from a change in how the firm records behaviour. A sudden fall in website
activity may indicate reduced interest, a consent withdrawal, a tracking failure, or a change in
the user interface.
This distinction matters for churn prediction. Contractual churn provides a relatively clear event
because the customer cancels o r fails to renew. Non -contractual churn is more ambiguous. A
customer who has not purchased recently may be inactive, temporarily satisfied with an existing
product, unable to purchase, or purchasing through an unobserved channel. Treating inactivity
as certain churn can create unnecessary contact and discounting. Survival analysis, competing -
risk models, and explicit opportunity-to-buy variables are therefore preferable to a simple binary
label when the customer relationship is non-contractual.
Prediction quality also depends on calibration, meaning the agreement between predicted
probabilities and observed outcome  rates. A model that ranks customers correctly but assigns
probabilities that are too high can lead to excessive contact and unrealistic financial forecasts.
Calibration should be assessed across time, cohorts, channels, and relevant customer groups.
https://doi.org/10.33774/coe-2026-sp6h1 Content not peer-reviewed by Cambridge University Press. License: CC BY 4.0

Precision-recall, lift at operational capacity, Brier scores, expected profit, and time -to-detection
are often more informative than accuracy or area under the ROC curve alone. The best model is
not necessarily the model with the highest discrimination. It is the model  that supports a sound
decision under the organisation’s actual capacity, cost, and risk constraints.
2.3 Customer lifetime value and the problem of long horizons
CLV is attractive because it translates customer analytics into financial language. However,
CLV is a forecast of future value. It is not a balance displayed in  an accounting system. Its
estimate depends on how the organisation models repeat purchase, retention, discounting,
margin, service cost,  returns, referrals, and future  marketing. A model  can produce precise-
looking CLV values while hiding uncertainty about each of these components.
The use of CLV also creates a strategic trade-off. High-value customers may receive more service
and retention investment. Yet a  policy based only on current CLV may  neglect lower -value
customers with strong future potential. It may also reinforce historical inequality if some group s
have lower observed value because they  received fewer offers, had less access  to a channel, or
were poorly measured. A responsible CLV system should therefore report uncertainty, examine
opportunity-to-benefit, and evaluate whether the policy changes future customer value rather than
merely predicting it.
The strongest implementation combines CLV with treatment response. A high-value customer
who is not persuadable may not be the best target for an intervention. A medium-value customer
with high incremental response may generate greater expected profit from a carefully designed
offer. This is the practical reason to combine CLV, uplift, costs, and capacity rather than ranking
customers on a single score.
2.4 The boundary between hyper-personalization and fatigue
Personalized advertising copy, triggered email, recommendation exposure, and integrated
online/offline promotions have produced positive effects in field experiments. These findings
justify targeted experimentation. They do not justify the general proposition that more
personalization is always better.
The strongest counterevidence concerns non -monotonicity and opportunity cost. Targeted
promotions can increase sales of  the promoted item  while crowding out other browsing and
failing to maximize total incremental sales. Recommendation-set size can have an Inverted-U
relationship with purchase because excessive choice reduces search initiation.
Recommendation algorithms can increase discovery while also concentrating demand on popular
products . Personalized email can generate reactance when the message is perceived as intrusive
. Cross-channel campaigns can cause substitution, migration, and delayed effects that disappear
or reverse under a narrow attribution window .
The operational implication is that personalization requires exposure-level data, frequency and
https://doi.org/10.33774/coe-2026-sp6h1 Content not peer-reviewed by Cambridge University Press. License: CC BY 4.0

sequence controls, consent state, content and model versioning, margins, returns, complaints,
opt-outs, and long -run outcomes. A click or conversion propensity is not a treatme nt-effect
estimate. The system must distinguish customers likely to buy from customers whose
probability of buying changes because of a particular message, offer, channel, or sequence.
2.5 Predictive insight in actual decision architectures
Attribution systems allocate credit. Causal designs estimate counterfactual change. Large -scale
field-experiment evidence shows that advertising effects can be noisy and expensive to measure.
The same evidence shows that selection bias can make observational returns estimates unreliable
. Attribution can misallocate budget because prior exposure credit is not the same as marginal
effectiveness . Non-experimental approaches sometimes approximate experimental effects, but
they do not do so reliably enough to justify treating platform-reported ROAS as ground truth .
MMM can be useful because it works  at an aggregate level and can represent lag,  saturation,
seasonality, and cross-channel effects. It is still observational causal inference. Even
Google’s methodological guidance s tates that conditional exchangeability, the assumption that
treated and untreated units are comparable after observed controls, is untestable. It also states that
different well-fitting models can produce different ROI and allocation results, and that predictive
fit is not sufficient for causal  validity. MMM should therefore be calibrated with experiments
where feasible and presented with uncertainty and assumption sensitivity.
Strategic automation has the highest consequence and the thinnest evidence. The marketing
literature generally favors AI as augmentation rather than replacement. It also emphasizes ill-
defined objectives, explainability, controllability, bias, and responsibility . The more authority  a
system has to change budgets, bids, targeting, cre ative, pricing, or go -to-market priorities, the
stronger the case for bounded authority, spend limits, rollback, minimum test cells, and named
human accountability.

Source: Author
Behavioral data contain predictive signal. Demonstrated, conditional. Dynamic behavior
predicts future outcomes in studied firms.  Performance still depends on label quality,
observation completeness, timing, and stability.
2.6 Digital Interface and Recent Research Work
Research indicates that AI -powered tools like intelligent tutoring systems personalize learning.
They also improve educator efficiency. However, their integration faces significant hurdles.
These include algorithmic bias, data privacy concerns, and a lack of educator readiness (Siddiqui
et al., 2025). Consumers are vital to any market. Attracting more customers increases profits
CLAIM EVIDENCE
JUDGEMENT
WHY?
https://doi.org/10.33774/coe-2026-sp6h1 Content not peer-reviewed by Cambridge University Press. License: CC BY 4.0

(Tripathi et al., 2024). Nanotechnology enhances the efficiency, reliability, and sustainability of
solar cells, fuel cells, batteries, and supe rcapacitors. This plays a pivotal role in accelerating the
green economy (Taneja et al., 2025). Without proper behavior management methods, therapy
outcomes prove ineffective (Kamate et al., 2025). Understanding intended clients is essential for
successfully operating and expanding a firm (Roy et al., 2023). Leaders must understand the types
of people they lead. Team members identify as a unit and plan organizational development to
achieve shared strategies and objectives (Rastogi et al., 2025). The future performance of firms
depends upon their employees (Bargavi et al., 2023).
Analysis of the Indian tobacco market shows a revenue imbalance. The government collects more
tax from non-smoke tobacco products. It spends less on mitigating negative externalities. These
include healthcare and environmental cleanup. Yet the underlying social costs remain substantial
(Verma et al., 2024). Brand personality dimensions, such as prestige, attractiveness, credibility,
and snobbishness, significantly influence brand trust, commitment, and attachment (Mishra et al.,
2025).
Industry-specific applications are becoming more sophisticated. AI in talent acquisition is
revolutionizing modern human resource management (Kamal et al., 2025b). Parallel
advancements occur in the transportation sector. Aviation focuses on performance optimization.
This improves customer satisfaction and operational efficiency (Kamal & Ahmad, 2025). Beyond
traditional operations, AI -powered branding strategies create a gravitational pull of  innovation.
This is noted within advertising and design fields (Kamal et al., 2026b). These technological tools
collectively contribute to human augmentation and enhanced creativity. Individuals and
organizations can extend their potential beyond traditional limits (Srivastava et al., 2025).
Kamal et al. (2026e) revealed that contemporary branding is shifting. It moves from rigid,
intuition-driven narratives into dynamic, data -informed ecosystems. To leverage this strategic
differentiator, organizations must combine robust data governance and generative AI. They also
need hyper -personalized engagement channels. Marketers must integrate ethical artificial
intelligence and robust data strategies. This builds responsive, trusted brands (Kamal et al.,
2026e).
Modern enterprises are adopting strategic approaches. They pursue e -business transformation.
This keeps them competitive in a rapidly evolving digital landscape (Kamal & Ahmad, 2024).
This shift is part of a larger global movement. It empowers social and ec onomic sustainability
through AI-driven digital transformation. Technological progress must align with broader societal
needs (Kamal & Ahmad, 2026). Within the Society 5.0 framework, organizations harness AI, data
science, and blockchain. These technologies facilitate human-centric product development. User
experience remains the central priority (Kamal et al., 2025). Ultimately, long -term success
depends on leveraging strategic analytics. Such tools enhance organizational maturity. They also
build systemic resilience against market fluctuations (Roy et al., 2025).
Understanding the human element is crucial. This is especially true when demystifying cognitive
schema effects on consumer buying patterns. Advanced deep learning techniques enable this
https://doi.org/10.33774/coe-2026-sp6h1 Content not peer-reviewed by Cambridge University Press. License: CC BY 4.0

analysis ( Rizvi et al., 2026). To refine marketing strategies further, researchers explore
neuromarketing opportunities and risks. These relate to generating deep consumer insights (Roy
& Kamal, 2026). External digital feedback plays a vital role in brand management. Online reviews
and celebrity endorsements significantly impact healthcare brand reputation in India (Ahmad et
al., 2026). Similarly, electronic word -of-mouth is a primary driver of brand reputation and visit
intentions. This holds true within the hospitality sector (Mishra et al., 2026b). The emergence of
audio-first interfaces marks a significant technological return to secondary orality (Mishra et al.,
2026a).
Figure 1: Genesis of Digital and AI Driven Marketing

Source: Author

3. RESEARCH OBJECTIVES / PROBLEM STATEMENT

This paper addresses the gap between predictive model performance and economically, ethically,
and operationally valid marketing action. Its objectives are to map research on behavioural
forecasting, campaign personalisation, and AI -supported marketing decisions; compare  these
pillars across data maturity, autonomy and oversight, and ROI measurement; identify
methodological, operational, ethical, and structural gaps; and select one priority direction for
future research and implementation.
The paper does not test a new algorithm or claim a universal effect size. It is a critical secondary
review of predictive customer analytics in marketing. Its central proposition is that marketing AI
https://doi.org/10.33774/coe-2026-sp6h1 Content not peer-reviewed by Cambridge University Press. License: CC BY 4.0

should be evaluated as a governed decision system: predictive accuracy may be necessary, but it
is insufficient without treatment exposure, counterfactual measurement, economic outcomes, drift
monitoring, and explicit responsibility.
4. RESEARCH METHODOLOGY
This paper uses  a structured secondary literature review. The  evidence base  comprises peer-
reviewed studies, systematic reviews, causal marketing research, concept-drift research, and
authoritative governance guidance. Academic evidence was grouped into behavioural anticipation,
campaign personalisation, and strategic marketing decision-making. Field experiments and causal
studies were prioritised for claims about incremental effects, while systematic reviews were used
to identify recurring methodological limitations. NIST, ICO, and related governance sources were
used for risk, privacy, and  accountability claims rather than as substitutes for causal marketing
evidence.
The analysis applies thematic synthesis rather than statistical meta-analysis. Studies were assessed
according to their r esearch object, data structure, identification strategy, outcome metric,
deployment assumptions, and limitations. Claims were classified as demonstrated within a defined
setting, conditional on assumptions, qualified by contradictory evidence, or unsupport ed
extrapolations. The three pillars were compared with a common framework: data maturity and
hygiene; decision autonomy and human oversight; and ROI measurement and attribution blind
spots.
The review is limited by proprietary datasets, setting -specific effect sizes, retrospective
validation, and the concentration of research in particular sectors and channels. The findings
should therefore be treated as an evidence-calibrated research agenda rather than  a universal
estimate of marketing AI returns.
5. ANALYSIS AND INTERPRETATION
The evidence points to one clear pattern: predictive tools are useful for identifying risk and
opportunity, but prediction  alone does not show that a  marketing action caused a result. The
strongest evidence supports carefully tested, limited interventions. The weakest evidence
concerns fully autonomous decisions about budgets, targeting, pricing, or go-to-market strategy.
The table below  summarises the main  finding for  each pillar. It separates what the literature
supports from the conditions that must be checked before a firm acts on the result.

Table 1: Digital Marketing Bases and Origin

Marketing pillar What the evidence supports Main caution
https://doi.org/10.33774/coe-2026-sp6h1 Content not peer-reviewed by Cambridge University Press. License: CC BY 4.0

Behavioural anticipation
Customer behaviour can be
forecast from transaction,
usage, and interaction patterns.
A high predicted risk does not
prove that a customer will
respond to a message or offer.

Campaign personalisation
Messages, recommendations,
and triggered campaigns can
create lift in particular
settings.
More personalisation can also
cause fatigue, crowding out,
choice overload, privacy
concerns, or substitution.

Strategic decision-making
Experiments and carefully
specified MMMs can inform
allocation and planning.
Attribution and model fit do
not by themselves prove
causal ROI or justify
unrestricted automation.
Source: Author
The decision process should move from data to prediction, then to treatment-response estimation,
policy checks, action, and measurement. The feedback loop is important: results and drift signals
should update the system, but only through controlled review rather than automatic expansion.
Data maturity and hygiene — Customer-level event histories are often available. The weak points
are censoring, opportunity -to-buy denominators, leakage, missing -not-at-random observation,
inconsistent churn definitions, and absent profit labels. — Event richness can be high. However,
identity resolution, consent, expo sure and non -exposure logs, rank position, creative versions,
frequency, returns, and long -term outcomes are commonly incomplete or proprietary. —
Aggregate spend and outcome data are more common than experimental ground truth. Causal
graphs, confounders, lag, saturation, structural breaks, and margin data are often under-specified.
Drift and shocks — Churn and purchase patterns can break after economic, product, policy, or
tracking changes. Monitor calibration, residuals, prevalence, and time-to-detection. — Consent
changes, inventory, platform policies, feedback loops,  and campaign learning alter response
functions. — Business-cycle variation and structural breaks change elasticities; automated
reallocation also changes the future data-generating process.
Ethical and structural exposure — Proxy discrimination, surveillance, cumulative over-contact,
and misreading silence as intent. — Privacy reactance, inferred vulnerability, manipulation,
popularity bias, and cross-context tracking. — Vendor opacity, concentrated platform power,
weak reproducibility, and strategic over-automation.
Overall, predictive infrastructure  is more mature  than causal policy integration. Tactic-level
experimentation is ahead of  cross-channel, long -run personalization. Strategic autonomous
execution is the least evidenced use case.
5.1 How the three pillars interact in practice
The three pillars are analytically distinct but operationally connected. A churn model may identify
a customer at risk. A personalisation system may select  a message or incentive. A budget -
https://doi.org/10.33774/coe-2026-sp6h1 Content not peer-reviewed by Cambridge University Press. License: CC BY 4.0

allocation system may decide whether the retention programme deserves more funding  than
acquisition or cross-selling. If each system is optimised separately, the overall policy may become
inconsistent. The churn model may maximise recall. The personalisation system may maximise
clicks. The budget model may maximise attributed revenue. None of these objectives necessarily
maximises incremental customer value.
A unified decision architecture should pass information between the pillars while preserving their
different meanings. The behavioural model should provide risk and uncertainty. The treatment
model should estimate how different interventions alter outcomes. The strategic model  should
allocate resources across actions using incremental margin, capacity, and long-run effects. This
architecture also needs a clear hierarchy of objectives. For example, a firm may require that the
system first respect consent and suppression rules, then protect against unacceptable customer
harm, then optimise incremental contribution margin within the remaining feasible action space.
This hierarchy matters because marketing objectives can conflict. A discount may prevent churn
but reduce margin. A personalised recommendation may increase a product sale while reducing
category discovery. A retargeting campaign may increase short-term conversion while increasing
complaints or opt-outs. An MMM may recommend a budget shift that improves aggregate sales
but reduces learning about a new channel. These are not technical anomalies. They are competing
outcomes that must be represented explicitly in the decision policy.
5.2 Concept drift and macroeconomic shocks
Concept drift is especially important in marketing because customer behaviour is shaped by
events outside the firm’s control. Inflation can change price sensitivity. A competitor launch can
change consideration sets. A product redesign can make historical usage patterns less comparable.
A privacy-policy change can remove an important feature. A recession can alter both demand and
the effectiveness of advertising. During a shock, the relationships learned from historical data
may fail even if the input variables continue to look familiar.
Drift monitoring should therefore cover more than feature distributions. Firms should monitor
label prevalence, calibration, residuals, treatment effects, subgroup performance, consent rates,
delivery rates, and changes in the relationship between exposure and outcome. A model can show
stable feature distributions while its response function has changed. Conversely, a feature
distribution may shift without materially changing the decision if the model is robust to that
change.
A safe response to drift  is not always immediate retraining. Rapid retrainin g can overreact to a
temporary shock, erase long -run preferences, or reinforce a short -lived pattern. Alternative
responses include recalibration, reducing automated authority, widening uncertainty intervals,
reverting to a simpler baseline, increasing experimentation, or requiring human  approval. The
correct response depends on whether the drift reflects a temporary disturbance, a permanent
regime change, a measurement failure, or an emerging customer segment.
https://doi.org/10.33774/coe-2026-sp6h1 Content not peer-reviewed by Cambridge University Press. License: CC BY 4.0

5.3 Privacy, consent, and customer autonomy
Privacy is not only a legal constraint on data collection. It changes the measurement system and
therefore changes what the model can learn. When users refuse tracking, delete. identifiers, move
between devices, or exercise data rights, the missingness is not random. The remaining data may
overrepresent customers who are more comfortable with surveillance or who use particular
channels. A model  trained on this data can appear accurate for observed users while becoming
less valid for the wider customer population.
Customer autonomy also requires attention to the experience of being targeted. A message can be
relevant and still feel invasive if the customer did not expect the firm to connect activities across
contexts. Personalisation may be technically lawful yet perceived as manipulative when it exploits
vulnerability, urgency, mood,  or limited attention. Evaluation should  therefore include
comprehension, refusal  usability, perceived  control, and  complaint behaviour, not only
conversion.
The practical response is data minimisation and purpose limitation. Firms should collect only what
is needed for the stated decision, separate sensitive attributes from  routine targeting features,
document inferred variables, and provide meaningful suppression and correction routes. Where a
less intrusive contextual method can achieve the objective, it should be considered  before
individual-level behavioural profiling. Privacy-preserving computation can help, but it does not
remove the need to define a lawful purpose or assess whether the resulting decision is fair.
5.4 Methodological gaps
First, the field lacks  prospective, multi -firm benchmarks with standardized definitions of
churn, CLV, intent,  exposure, treatment, margin, and opportunity. Retrospective random
splits overstate transportability when customers, channels, and policies are changing.
Second, more studies must connect score -based targeting to incremental retention, contribution
margin, CLV, and customer welfare. Response models should be compared with uplift models,
causal forests, bandits, and human decisions under realistic capacity constraints.
Third, models should jointly represent churn, purchase, margin, price sensitivity, treatment
response, service experience, repeated churn/win -back, and i nterference. Independently
optimized scores can be internally accurate while being economically incoherent.
Fourth, concept drift needs operational evaluation under real macro shocks, competitor moves,
privacy changes, product launches, and instrumentation  failures. Concept drift is a change in the
data-generating distribution; detection, localization,  explanation, and adaptation are distinct
problems [28]. Drift explanations are inherently  domain-specific and cannot be reduced to a
generic feature-importance chart.
5.5 Operational gaps
The typical gap is not a missing model. It is the missing decision infrastructure around the model.
https://doi.org/10.33774/coe-2026-sp6h1 Content not peer-reviewed by Cambridge University Press. License: CC BY 4.0

Firms often lack immutable logs of eligibility, exposure, delivery, treatment, contactability,
suppression, creat ive/model version, override, cost, and outcome. They  also lack  integrated
finance, CRM, media, product, inventory, service, returns, and consent data.
6. DISCUSSION
The single highest-priority direction is, prospectively evaluate an experiment-calibrated, privacy-
aware, drift-resilient causal policy layer that converts predictive customer analytics into bounded
marketing actions under explicit profit-and-welfare constraints.
The policy layer should include:
a) A pre-specified estimand and horizon, such as incremental contribution margin, retention, or
long-run CLV.
b) Consent-aware, first-party, timestamped data with exposure opportunity and missingness
recorded.
c) Randomized holdouts, geo tests, or other defensible quasi-experiments to establish
counterfactuals.
d) Uplift or heterogeneous-treatment models, not response-only targeting.
Costs, margin, returns, service burden, fatigue, complaints, opt-outs, retention, and long-run value
in the objective.
e) Uncertainty, subgroup evaluation, drift and shock detection, fallback policies, and rollback.
f) Bounded authority with spend caps, minimum  test cells,  escalation thresholds, named decision
owners, override logs, and post-decision audits.
The success criterion is not AUC,  CTR, or attributed ROAS. It is incremental economic and
customer outcome relative to a randomized or operational baseline, with uncertainty and harm
metrics reported.
6.1 Why a policy layer is more useful than a single model
A policy layer is useful because it creates a controlled boundary between prediction and action.
The model may estimate churn risk, purchase propensity, or treatment response, but the policy
decides whether action is permitted. It can incorporate frequency caps, customer preferences,
inventory, budget, channel capacity, margin, uncertainty, and fairness rules. This separation also
makes auditing easier. If the outcome is poor, analysts can ask whether the prediction was wrong,
whether the policy selected the wrong action, or whether the action was executed incorrectly.
The policy layer should be evaluated against meaningful alternatives. A useful comparison may
include the existing marketing rule, response -model targeting, uplift targeting, and a
conservative no -action or holdout condition. The objective sho uld be pre -registered where
possible. Evaluation should include both average treatment effects and treatment -effect
https://doi.org/10.33774/coe-2026-sp6h1 Content not peer-reviewed by Cambridge University Press. License: CC BY 4.0

heterogeneity, since a policy that works for the average customer may harm a subgroup or fail
under capacity limits.
The approach is also co mpatible with gradual automation. At first, the policy can recommend
actions to a human operator. Once the recommendation is shown to be reliable, a narrow subset
of low-risk decisions can be automated. Higher -risk decisions can remain subject to approval.
This arrangement avoids treating autonomy as a binary choice. It makes authority a variable that
can be increased or reduced according to evidence.
6.2 Expected contribution to marketing science
The priority direction contributes to marketing science by c onnecting forecasting, causal
inference, and organisational decision -making. It asks not only whether an intervention works,
but for whom, under what circumstances, at  what cost, and  with what consequences for  future
behaviour. It also  treats measurement i nfrastructure as part of the research object. Consent
changes, missing exposure data, platform rules, and operational capacity are not distractions from
the model. They are part of the environment in which the model is used.
This framework can also improve theory. It moves the discussion away from a simple opposition
between human marketing and algorithmic marketing. The more useful distinction is between
ungoverned automation and evidence-based decision support. A system can be highly automated
while remaining bounded, transparent, reversible, and accountable.
Conversely, a nominally human  process can be poorly governed if staff rely on opaque scores
without understanding their limitations.
6.3 Data maturity is a governance and measurement property
Data maturity should not be equated with data volume. A firm may possess billions of clickstream
events and still lack the information needed to support a valid marketing  decision. The decisive
properties are temporal validity, provenance, completeness, treatment exposure, outcome quality,
and economic interpretation. A customer -level feature is useful only if its timestamp is known,
its lawful basis is documented, its meaning is stable, and it would have been available when the
decision was made. This requireme nt is stricter than ordinary  predictive modelling  because
operational processes can create leakage.  For example, a service -contact flag recorded after a
retention intervention may appear highly predictive of churn while actually encoding the
intervention itself.
6.4 Autonomy, human oversight, and organizational failure
The question is not whether a human is present somewhere in the workflow. The relevant question
is whether the human has the authority, information, time, and incentives to challenge the system.
A marketer who approves  thousands of recommendations through a default button  provides
symbolic rather than substantive oversight. Conversely, a bounded system can support meaningful
human judgment by presenting uncertainty, affected segments, counterfactu al alternatives, data-
https://doi.org/10.33774/coe-2026-sp6h1 Content not peer-reviewed by Cambridge University Press. License: CC BY 4.0

quality warnings, and clear escalation criteria.
Oversight should be proportionate to reversibility and consequence. A low-value recommendation
displayed on a web page may be allowed to operate with automated
monitoring and rapid rollback. A system that changes a customer’s price, suppresses service, ranks
a lead for sales  attention, or reallocates a substantial budget requires  stronger controls. These
controls include approval thresholds, spend caps, protected groups or segments, minimum
experimental cells, rate limits, rollback procedures, and a named accountable owner. The owner
should be able to explain not only  what the system did, but why the organisation permitted it to
do so.
7. CONCLUSION
Predictive customer analytics can improve marketing forecasting and support effective
interventions, but the evidence is conditional. Behavioural anticipation is comparatively mature
as a prediction problem. Campaign personalisation has credible tactic-level experiments but also
produces c rowding out, choice overload, fatigue, substitution, and privacy -reactance risks.
Strategic decision-making has sophisticated causal and allocation methods but faces expensive
experimentation, assumption-sensitive marketing-mix models, weak attribution, an d limited
evidence for autonomous execution.
The main conclusion is that marketing AI should be developed as a governed causal decision
system. The priority is an experiment -calibrated, privacy-aware, drift-resilient policy layer that
separates propensity from treatment response, measures incremental economic and customer
outcomes, monitors subgroup and long-run effects, and limits  automated authority. A practical
first study should use one reversible retention or triggered-messaging use case, compare response
targeting with uplift targeting and a human baseline, maintain a randomised holdout, integrate
margin and fatigue outcomes, and define rollback conditions. Only after prospective evidence
supports the bounded policy should the system expand to cross -channel orchestration or budget
reallocation.
References:

1. Ahmad, S., Srivastava, V., Mishra, R. K., & Kamal, Y. (2026). Impact of online reviews
and celebrity endorsement on the brand reputation of healthcare services: evidence from
India. International Journal of Process Management and Benchmarking, 22(4), 510 –
537. https://doi.org/10.1504/ijpmb.2026.152637
2. Alboukaey, N., Joukhadar, A., & Ghneim, N. (2020). Dynamic behavior based churn
prediction in mobile telecom. Expert Systems with Applications, 162, 11 3779.
https://doi.org/10.1016/j.eswa.2020.113779
3. Bargavi, N., Roy, A., Kumar, V., Shrivastava, G., Varma, R. A., & Shrivastava, A.
(2023). An Empirical Study On Employee Turnover And Job Satisfacti on In Human
Resource Management Practices. E3S Web of Conferences, 399, 07001.
https://doi.org/10.1051/e3sconf/202339907001
https://doi.org/10.33774/coe-2026-sp6h1 Content not peer-reviewed by Cambridge University Press. License: CC BY 4.0

4. Castéran, H., Meyer -Waarden, L., & Reinartz, W. (2021). Modeling Custo mer Lifetime
Value, Retention, and Churn. In Handbook of Market Research (pp. 1001–1033). Springer
International Publishing. https://doi.org/10.1007/978-3-319-57413-4_21
5. Danaher, P. J., & van Heerde, H. J. (2018). Delusion in Attribution: Caveats in Using
Attribution for Multimedia Budget Allocation. Journal of Marketing Research.
https://doi.org/10.1509/jmr.16.0112
6. Danaher, P. J., Danaher, T. S., Smith, M. S., & Loaiza -Maya, R. (2020). Advertising
Effectiveness for Multiple Retailer -Brands in a Multimedia and Multichannel
Environment. Journal of Marketing Research, 57(3), 445 –467.
https://doi.org/10.1177/0022243720910104
7. De Bruyn, A., Viswanathan, V., Beh, Y. S., Brock, J. K. -U., & Von Wangenheim, F.
(2020). Artificial Intelligence and Marketing: Pitfalls and Opportunities. Journal of
Interactive Marketing, 51(1), 91–105. https://doi.org/10.1016/j.intmar.2020.04.007
8. Fakhar, I., Siddiqui, M. T., & Faizi, A. (2026). Effects of Remittances on Household
Welfare: An Econometrics Analysis from Kunar Province, Afgh anistan. Journal of
Social Sciences and Humanities, 3(2), 451–467. https://doi.org/10.62810/jssh.v3i2.243
9. Fleder, D. M., & Hosanagar, K. (2007). Recommender systems and their impact on sales
diversity. In Proceedings of the 8th ACM conference on Electronic commerce (pp. 192 –
199). ACM. EC07: ACM Conference on Electronic Commerce.
https://doi.org/10.1145/1250910.1250939
10. Fong, N., Zhang, Y., Luo, X.,  & Wang, X. (2019). Targeted Promotions on an E -Book
Platform: Crowding Out, Heterogeneity, and Opportunity Costs. Journal of Marketing
Research, 56(2), 310–323. https://doi.org/10.1177/0022243718817513
11. Goic, M., Rojas, A., & Saavedra, I. (2021). The Effectiveness of Triggered Email
Marketing in Addressing Browse Abandonments. Journal of Interactive Marketing, 55(1),
118–145. https://doi.org/10.1016/j.intmar.2021.02.002
12. Guo, B., & Jiang, Z. (2023). Influence of personalised advertising copy on consumer
engagement: a field experiment approach. Electronic Commerce Research, 25(2), 1281 –
1310. https://doi.org/10.1007/s10660-023-09721-5
13. Gupta, S., Hanssens, D., Hardie, B., Kahn, W., Kumar, V., Lin, N., Ravishanker, N., &
Sriram, S. (2006). Modeling Customer Lifetime Value. Journal of Service Research, 9(2),
139–155. https://doi.org/10.1177/1094670506293810
14. Kamal, Y. (2026). An Analytical Study on Customer’s Adaptability and Satisfaction for
Electronic Banking Services. Elsevier BV. https://doi.org/10.2139/ssrn.6046356
15. Kamal, Y. Ahmad, M., Ahmad, S., Rizvi, (2026f). The Symbiosis of Marketing
Intelligence and Customer Experience: Building a Data -Driven Strategy. Elsevier BV.
http://dx.doi.org/10.2139/ssrn.6504998
16. Kamal, Y., & Ahmad, I. (2025). Performance Optimization in Aviation. In Airline
Customer Experience (pp. 81 –103). Routledge.
https://doi.org/10.4324/9781003625100-6
17. Kamal, Y., & Ahmad, S. (2024). Strategic Approaches to E -Business Transformation.
In Advances in E -Business Research (pp. 89 –126). IGI Global.
https://doi.org/10.4018/979-8-3693-7056-8.ch004
18. Kamal, Y., & Ahmad, S. (2026). Empowering Social and Economic Sustainability
Through AI -Driven Digital Transformation. In Contributions to Environmental
https://doi.org/10.33774/coe-2026-sp6h1 Content not peer-reviewed by Cambridge University Press. License: CC BY 4.0

Sciences; Innovative Business Technology (pp. 35 –61). Springer Nature Singapore.
https://doi.org/10.1007/978-981-95-8473-4_2
19. Kamal, Y., & Siddiqui, M. T. (2025). 7 Slot Radiator Grille and 70 years of Mileage:
Who Drove Off Road on Road? Elsevier BV. https://doi.org/10.2139/ssrn.5928514
20. Kamal, Y., Ahmad, M., Ahmad, S., Rizvi, A. A., Ansari, J. A. N., & Dubey, R. (2026e).
AI-powered branding strategies. In Reference Module in Social Sciences. Elsevier.
https://doi.org/10.1016/b978-0-443-29863-9.00007-6
21. Kamal, Y., Ahmad, M., Ahmad, S., Rizvi, A. A., Ansari, J. A. N., & Dubey, R. (2026).
AI-powered branding strategies. In Reference Module in Social Sciences . Elsevier.
https://doi.org/10.1016/b978-0-443-29863-9.00007-6
22. Kamal, Y., Pirzada, T. R., & Roy, A. (2026d). The Geopolitical Displacement of Global
Capital and the New Zealand (NZ) Safe Haven Logic: A Critique of the Active Investor
Plus (AIP) Visa Ecosystem. Cambridge University Press (CUP).
https://doi.org/10.33774/coe-2026-7lbxv
23. Kamal, Y., Rizvi, A. A., Ahmad, S., Siddiqui, M. T., Mishra, R. K., & Roy, A. (2026b).
AI-Powered Branding Strategies’ Gravitational Pull of Innovation Through the AI’s
Impact on Adve rtising and Design. In Advances in Computational Intelligence and
Robotics (pp. 357–388). IGI Global Scientific Publishing. https://doi.org/10.4018/979-
8-3373-7036-1.ch011
24. Kamal, Y., Rizvi, A. A., Srivastava, V., & Singh, N. (2026). Immersive Personalization
in the Metaverse: Transforming Marketing Through Intelligent Adaptation. In
Encyclopedia of Artificial Intelligence in Marketing (pp. 1 –15). Springer Nature
Switzerland. https://doi.org/10.1007/978-3-031-75316-9_136-1
25. Kamal, Y., Rizvi, A. A., Srivastava, V., Ahmad, S., Kumar, S., & Siddiqui, M. T.
(2027). Harnessing Artificial Intelligence for Strategic Retail Promotions: A Path to
Consumer-Centric Shopping. In M. Khan, P. Praveen, A. Verma, R. Khan, & I. Kumar
(Eds.), Driving Global Economic Transformation Through AI and Machine
Learning (pp. 363-398). IGI Global Scientific Publishing. https://doi.org/10.4018/979-
8-3373-7267-9.ch016
26. Kamal, Y., Roy, A., Ahmad, S., & Mishra, R. K. (2025a). Harnessing AI, data science,
and block chain for human -centric product development in society 5.0. In Hum an-
Centric Integration of Next-Generation Data Science and Blockchain  Technology (pp.
15–30). Elsevier. https://doi.org/10.1016/b978-0-443-33498-6.00020-0
27. Kamal, Y., Roy, A., Ahmad, S., & Mishra, R. K. (2025b). AI in Talent Acquisition. In
AI and Innovation in HRM (pp. 254 –275). Routledge.
https://doi.org/10.4324/9781003522157-16
28. Kamate, W., Kurup, R. R., Roy, A., Pillai, A., Malho tra, P., & Hajare, A. (2025).
Attitude of Parents Towards Various Behavior Management Techniques Utilized in
Pediatric Dental Treatments. Research Journal of Pharmacy and Technology, 1380 –
1385. https://doi.org/10.52711/0974-360x.2025.00199
29. Kaya, E., Dong, X., Suhara, Y., Balcisoy, S., Bozkaya, B., & Pentland, A. “Sandy.” (2018).
Behavioral attributes and financial churn prediction. EPJ Data Science, 7(1).
https://doi.org/10.1140/epjds/s13688-018-0165-5
30. KumarSaini, D., & Ahmad, M. (2012). Return on Investment and Effort Expenditure in
the Software Development Environment. International Journal of Applied Information
Systems, 4(7), 35–41. https://doi.org/10.5120/ijais12-450813
https://doi.org/10.33774/coe-2026-sp6h1 Content not peer-reviewed by Cambridge University Press. License: CC BY 4.0

31. Lambrecht, A., Tucker, C., & Zhang, X. (2023). TV Advertising and Online Sales: A Case
Study of Intertemporal Substitution Effects for an Online Travel Platfo rm. Journal of
Marketing Research, 61(2), 248–270. https://doi.org/10.1177/00222437231180171
32. Lee, S. Y., Son, Y., & Oh, W. (2021). Effectiveness of Integrated Offline -and-Online
Promotions in Omnich annel Targeting: A Randomized Field Experiment. Journal of
Management Information Systems, 38(2), 484 –516.
https://doi.org/10.1080/07421222.2021.1912935
33. Long, X., Sun, J., Dai, H., Zhang, D., Zhang, J., Chen, Y., Hu, H., & Zhao, B. (2025). The
Choice Overload Effect in Online Recommender Systems. Manufacturing &amp; Service
Operations Management, 27(1), 249–268. https://doi.org/10.1287/msom.2022.0659
34. Manzoor, A., Atif Qureshi, M., Kidney, E., & Longo, L. (2024). A Review on Machine
Learning Methods for Customer Churn Prediction and Recommendations for Business
Practitioners. IEEE Access, 12, 70434 –70463.
https://doi.org/10.1109/access.2024.3402092
35. Martínez, A., Schmuck, C., Pereverzyev, S., Jr., Pirker, C., & Haltmeier, M. (2020). A
machine learning framework for customer purchase prediction in the non -contractual
setting. European Jou rnal of Operational Research, 281(3), 588 –596.
https://doi.org/10.1016/j.ejor.2018.04.034
36. Mena, G., Coussement, K., De Bock, K. W., De Caigny, A., & Lessmann, S. (2023).
Exploiting time-varying RFM measures for customer churn prediction with deep neural
networks. Annals of Operations Research, 339(1 –2), 765 –787.
https://doi.org/10.1007/s10479-023-05259-9
37. Mishra, R. K., Ahmad, S., & Siddiqui,  M. T. (2026a). Voice Commerce and
Conversational Marketing: Understanding Consumer Decision Paths and Trust
Formation in Audio-Based AI Interfaces. In Encyclopedia of Artificial Intelligence in
Marketing (pp. 1–16). Springer Nature Switzerland. https://doi.org/10.1007/978-3-031-
75316-9_139-1
38. Mishra, R. K., Singh, N., Ahmad, S., & Kamal, Y. (2026b). Does electronic word -of-
mouth impact brand reputation and visit intention of guests in the hosp itality sector
Empirical evidence. International Journal of Electronic Business, 21(4), 385 –407.
https://doi.org/10.1504/ijeb.2026.10078242
39. Mishra, R. K., Srivastava, V., Singh, N., & Ahmad, S. (2025). Influence of brand
personality on brand equity of fashion products in the digital age: an empirical evidence.
International Journal of Learning and Change, 17(4), 333 –352.
https://doi.org/10.1504/ijlc.2025.149637
40. Mohammad Talha Siddiqui. (2025). AI -Enabled Pedagogy: Advancing Education
Through Innovative Teaching Tools and the AI-TEACH Model. Journal of Informatics
Education and Research, 5(1). https://doi.org/10.52783/jier.v5i1.2261
41. Nygård, R., & Mezei, J. (2020). Automating Lead Scoring with Machine Learning: An
Experimental Study. In Proceedings of the Annual Hawaii International Con ference on
System Sciences. Hawaii International Conference on System Sciences. Hawaii
International Conference on System Sciences. https://doi.org/10.24251/hicss.2020.177
42. Rastogi, S., Roy, A., Tiwari , A., Singh, S., & Vatsa, M. (2025). Models for analyzing
the impact of leadership and followership values on organizational outcomes. In
Mathematical Modeling, Design, and Optimization of Complex Engineering Systems
(pp. 287–295). CRC Press. https://doi.org/10.1201/9781003642152-23
https://doi.org/10.33774/coe-2026-sp6h1 Content not peer-reviewed by Cambridge University Press. License: CC BY 4.0

43. Rizvi, A. A., Ahmad, S., Kumar, M., & Kamal, Y. (2026a). Demystifying the effects of
cognitive schema on consumer buying patterns: an in -depth exploration utilizing deep
learning technique. Quality & Quantity, 60(2), 7753 –7780.
https://doi.org/10.1007/s11135-026-02601-8
44. Rizvi, A. A., Kamal, Y., & Ahmad, S. (2026b). When Moral Identity Fails: The
Structural Limits o f Sustainable Consumption. Elsevier BV .
https://doi.org/10.2139/ssrn.6513480
45. Roy, A., & Kamal, Y. (2026). Neuromarketing opportunities and risks in consumer
insight generation. In Redefining Innovative Practices in the Age of AI (pp. 157 –173).
CRC Press. https://doi.org/10.1201/9781003679295-24
46. Roy, A., Kamal, Y., Raj Kumar, M., & Ahmad, S. (2025). Leveraging Strategic
Analytics to Enhance Organizational Maturity and Resilience. In Information Systems
Engineering and Management (pp. 89 –111). Springer Nature Switzerland.
https://doi.org/10.1007/978-3-031-82369-5_6
47. Roy, A., Shete, A. S., Tiwari, A., Paliwal, M., Singh, S., & Vatsa, M. (2023). Marketing
Research and Market -Focused Production as an Effective Business Tool in Power
Sector. In 2023 IEEE Renewable Energy and Sustainable E -Mobility Conference
(RESEM) (pp. 1–3). IEEE. 2023 IEEE Renewable Energy and Sustainable E-Mobility
Conference (RESEM). https://doi.org/10.1109/resem57584.2023.10236290
48. Siddiqui, M. T., & Kamal, Y. (2026). Responsible Automation in E -business: A
Framework for Agentic AI Integration and Governance. BIMTECH Business
Perspectives. https://doi.org/10.1177/25819542261479531
49. Srivastava, V., Kamal, Y., & Mishra, R. K. (2025). Human Augmentation and Enhanced
Creativity. In Advances in Computational Intelligence and Robotics (pp. 195–226). IGI
Global Scientific Publishing. https://doi.org/10.4018/979-8-3373-7153-5.ch007
50. Taneja, D., Singh, S. R., Madaan, V., Roy, A., Tyagi, M., & Bhateja, R. (2025).
Implementing Nanotechnology for the Supply of Sustainable Energy to Construct a
Green Economy. In Advances in Environmen tal Engineering and Green Technologies
(pp. 283–300). IGI Global Scientific Publishing.  https://doi.org/10.4018/979-8-3693-
9471-7.ch018
51. Tripathi, S., Tiwari, A., Singh, S., Roy, A., Singla, J., & Chaudhry, R. (2024). Analyzing
the Consumer Buying Behavior by Adapting Artificial Intelligence (AI). In 2024
International Conference on Healthcare Innovations, Software and Engineering
Technologies (HISET) (pp. 377 –379). IEEE. 2024 International Con ference on
Healthcare Innovations, Software and Engineering Technologies (HISET).
https://doi.org/10.1109/hiset61796.2024.00110
52. Verma, D., Shimpi, L. S., Srivastava, S. kr., Ahmad, S., & Yadav, S. (2024). Non -
Smoke Tobacco Consumption in India: A Cost -Benefit Analysis. Journal of Applied
Business and Economics, 26(5). https://doi.org/10.33423/jabe.v26i5.7356
53. Wu, M., Andreev, P., & Benyoucef, M. (2023). The state of lead scoring models and their
impact on sales performance. Information Technology and Management, 25(1), 69 –98.
https://doi.org/10.1007/s10799-023-00388-w
54. Yadav, S., Ahmad, I., Kamal, Y., Rizvi, A. A., & Siddiqui, M. T. (2026). Promoting
Cultural Sensitivity in Bleisure Tourism: Strategies for Sustainable Engagement.
Elsevier BV. https://doi.org/10.2139/ssrn.6208798
https://doi.org/10.33774/coe-2026-sp6h1 Content not peer-reviewed by Cambridge University Press. License: CC BY 4.0

55. Yadav, S., Ahmad, I., Rizvi, A. A., Ahmad, S., & Kamal, Y. (2026). Impact of New
Distribution Capabilities (NDC) Standard on Future Travel Agency Business. Elsevier
BV. https://doi.org/10.2139/ssrn.6208898

https://doi.org/10.33774/coe-2026-sp6h1 Content not peer-reviewed by Cambridge University Press. License: CC BY 4.0
