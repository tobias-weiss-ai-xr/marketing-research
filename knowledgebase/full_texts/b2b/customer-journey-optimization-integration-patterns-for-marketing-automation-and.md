---
title: 'Customer Journey Optimization: Integration Patterns for Marketing Automation and Experience Platforms'
url: https://doi.org/10.5281/zenodo.20478372
category: b2b
subcategory: framework
date: 2026-05
venue: Zenodo (CERN European Organization for Nuclear Research)
authors:
- Sudhakar Nuthalapati
source: openalex-oa
pdf_url: https://ijisae.org/index.php/IJISAE/article/download/8300/7288
pages: 9
chars: 32519
fetched_at: '2026-11-08T17:15:17+00:00'
kb_version: 1
---

# Customer Journey Optimization: Integration Patterns for Marketing Automation and Experience Platforms

International Journal of
INTELLIGENT SYSTEMS AND APPLICATIONS IN
ENGINEERING
ISSN:2147-67992147-6799                                       www.ijisae.org Original Research Paper

International Journal of Intelligent Systems and Applications in Engineering                      IJISAE, 2026, 14(1s), 989–997 |  989

Customer Journey Optimization: Integration Patterns for
Marketing Automation and Experience Platforms

Sudhakar Nuthalapati

Abstract: The problem most B2B marketing teams won't admit publicly: their technology stacks are a mess.
Customer data lives in six different platforms that don't talk to each other, and the "unified customer view"
promised by vendors remains perpetually twelve months away. This article documents what actually happened
when a 4,000 -employee cybersecurity company integrated its marketing automation (Marketo), customer data
platform (Segment), journey orchestration (Adobe Journey Optimizer), and analytics stack over an 18 -month
period. The results were significant but not uniform: MQL conversion improved 34% overall, but behavioral
lead scoring only outperformed demographic methods for enterprise segments ,mid-market showed no statistical
difference. Multi -touch attribution revealed that paid search, our most expensive channel, was primarily an
awareness driver contributing just 8% of last -touch conversions but 22% of multi -touch credit. Implementation
required three major course corrections, including completely rebuilding our initial lead scoring model after it
achieved only 0.62 AUC in production. The framework presented here reflects what worked, what didn't, and
the specific thresholds we landed on after eighteen months of iteration.

Keywords: Customer Journey Orchestration, Marketing Automation Integration, Behavioral Analytics, Multi -
Touch Attribution, B2b Lead Scoring

1. Introduction
1.1 Research Context and Motivation
The B2B buying process has fundamentally
changed, and most marketing organizations haven't
caught up. Modern enterprise buyers complete 70%
of their research before talking to sales,they're
reading your documentation, comparing you to
competitors, and forming vendor preferences while
your SDRs are still trying to book discovery calls.
This creates a measurement problem: by the time a
prospect raises their hand, the journey that shaped
their decision is largely invisible. Our
organization,a publicly traded cybersecurity
company with $2.8B ARR serving enterprise
customers in regulated industries,faced this
challenge acutely. Sales cycles averaged 127 days.
Buying committees included 6 -8 stakeholders. And
our marketing technology stack had grown
organically to include 14 different platforms, none
of which shared a common customer identifier.
The fragmentation wasn't anyone's fault,it was the
predictable result of solving immediate problems
with point solutions. Email automation in Marketo.
Web analytics in Google Analytics and Adobe
Analytics (yes, both,don't ask). Intent data from
Bombora. Product usage from Pendo. CRM in
Salesforce. Event tracking in Segment. Each
system captured valuable behavioral signals, but
integration was limited to nightly batch syncs that
regularly broke. The practical impact: a prospect
could attend our webinar, download three
whitepapers, visit the pricing page six times, and
our SDRs would see none of it because the data
hadn't propagated to Salesforce yet.
1.2 Research Problem
Academic literature on marketing technology
integration is surprisingly thin on implementation
specifics. Plenty of frameworks exist,conceptual
models showing boxes connected by arrows,but try
finding a paper that tells you whether to use
Independent Researcher, USA

International Journal of Intelligent Systems and Applications in Engineering                      IJISAE, 2026, 14(1s), 989–997 |  990

webhook-based event streaming or batch ETL for
CDP synchronization. The gap matters because
marketing leaders face real pressure to justify
technology investments, and abstract frameworks
don't help when the CFO asks what the $400K
annual platform spend actually delivers. We needed
evidence connecting integration architecture to
measurable business outcomes: not "improved
customer experience" but "X% increase in MQL
conversion with Y statistical confidence."
The lack of stringent return -on-investment models
exacerbates the adoption process since marketing
leaders are growing increasingly pressured to
explain to them the use of technology as a method
of spending money in quantifiable financial terms.
The organizations are reluctant to invest in
integration to result in wholesome outcomes unless
they have credible evidence to support the
relationship between the integration investments
and the actual outcome. This is an evidential void,
especially in B2B settings where long purchase
processes, decision makers, and complicated
attribution conditions can distinguish enterprise
settings and transactional consumer markets. Also,
there are systematic approaches to real -time
personalisation that have been specially designed to
be used in the context of B2B, such as behavioral
signals capture, predictive leads scoring, and
dynamic content optimization, which should be
further empirically studied and validated [2].
1.3 Research Objectives and Contributions
This study documents the integration architecture
we implemented, the specific results we measured,
and,importantly,the failures we encountered along
the way. The technical contribution includes event
streaming patterns connecting Marketo, Segment,
and Salesforce with sub -second latency; behavioral
scoring models with specific signal weights; and
attribution methodology accounting for 127 -day
average sales cycles. The practical contribution
includes decision thresholds for lead routing,
content personalization rules by journey stage, and
the organizational changes required to
operationalize real-time customer data.

2. Literature Review and Theoretical
Framework
2.1 Customer Journey Orchestration Theory
Customer journey orchestration sounds
straightforward until you try to implement it. The
theory says: track customer interactions across
channels, build unified profiles, deliver coordinated
experiences. The practice involves wrestling with
identity resolution (is john.smith@company.com
the same person as jsmith@company.com who
attended your webinar?), latency constraints (can
you personalize a web experience before the page
loads?), and organizational silos (does marketing
even have access to product usage data?). B2B
journeys add complexity: enterprise deals involve
multiple stakeholders researching independently,
evaluating on different criteria, and ultimately
making collective decisions. A single "customer
journey" is actually five or six parallel journeys
that occasionally intersect.
B2B and B2C journeys differ in ways that break
assumptions baked into most marketing
technology. Consumer purchases are individual
decisions with short consideration windows,you
can A/B test checkout flows and see results in days.
Enterprise purchases involve committees, take
months, and require consensus among stakeholders
with different priorities. The security buyer cares
about threat detection capabilities; the IT
operations lead cares about deployment
complexity; the CFO cares about total cost of
ownership; the CISO cares about compliance
certifications. Marketing content that resonates
with one stakeholder may be irrelevant to another,
and traditional funnel metrics assume a single
decision-maker progressing through linear stages.

International Journal of Intelligent Systems and Applications in Engineering                      IJISAE, 2026, 14(1s), 989–997 |  991

Fig 1: Customer Journey Orchestration Framework [3, 4]

2.2 Marketing Automation and Platform
Integration
Customer Data Platform architectures eliminate the
problem of fragmented customer information by
resolving identities and unifying profiles. The ways
of architecture are as varied as analytic data
warehouses and real -time update operating
systems. Effective implementations will entail
massive investments in data governance structures,
identity matching algorithms, and quality
maintenance processes [4].
The maturity models of marketing automation
identify organizational development between
simple task automation and smart marketing
interactions. The first attempts involve operational
efficiency, and the middle stages involve
behavioral tracking and segmentation. Advanced
maturity includes predictive analytics,
personalization at work, and coordinated cross -
channel experiences. At greater maturity,
companies exhibit better conversion rates, and
progress is challenged by such factors as skill
deficiencies and organizational opposition [3].
Real-time decisioning is where theory meets
infrastructure constraints. The concept: process
customer events against predictive models to
generate personalized responses in milliseconds.
The reality: you need streaming data infrastructure
(we used Segment's real -time pipelines), low -
latency profile access (sub -50ms lookups against
unified customer profiles), and decision logic that
executes fast enough for web page personalization.
Our initial implementation targeted 200ms end -to-
end latency from event capture to personalized
response. We achieved 180ms for simple rules but
400-600ms for ML -based predictions,fast enough
for email but too slow for in -session web
personalization. We ended up running simpler rule -
based logic for real -time web experiences and
reserving ML predictions for next -session
personalization.
2.3 Attribution and Performance Measurement
Multi-touch attribution in B2B is genuinely hard,
and anyone claiming otherwise is selling
something. Enterprise deals involve 50 -100
touchpoints over 4 -6 months, including offline
interactions (sales calls, conferences, dinners) that
don't appear in digital tracking. First -touch
attribution credits the initial interaction,usually
paid search or content syndication,while ignoring
the 47 subsequent touches that actually built the
relationship. Last-touch credits the demo request or
sales meeting while ignori ng the months of
nurturing that made that request possible. Data -
driven attribution uses machine learning to estimate
causal effects, but requires large sample sizes we
didn't have for enterprise deals (maybe 200 -300

International Journal of Intelligent Systems and Applications in Engineering                      IJISAE, 2026, 14(1s), 989–997 |  992

closed-won opportunities per year). We ultimately
implemented a position-based model: 30% credit to
first touch, 30% to last touch, 40% distributed
across middle interactions. Not perfect, but
defensible and operationally useful.
The marketing qualified lead optimization systems
recognize prospects that indicate readiness to
purchase. Modern methods involve behavioral
scoring of interaction patterns, content
consumption, and the frequency of engagement.
Studies indicate that behavioral analytics are
superior to demographic methods of conversion
prediction. Time -efficiency measurements are in
the form of pipeline velocity to measure the stage -
throughput of opportunities. Integrated platforms
allow quantifiable velocity boosts via coordinated
engagement, cutting down on buyer friction [4].
2.4 Research Gaps and Hypotheses
Literature provides the theoretical bases but does
not present any empirical information about
particular implementation architecture and
quantified B2B results. Three hypotheses drive
research: H1: the integrated orchestration enhances
the marketing qualified lead conversion with
improved customer -level understanding and
coordinated messaging; H2: real -time behavioral
analytics lead to an improved engagement with the
content with dynamic -based optimization; H3:
unified data architecture boosts pipeline velocity
with less information latency and responsive
engagement [3].

3. Methodology
3.1 Research Context
This study documents an 18 -month integration
initiative at a publicly traded cybersecurity
company (anonymized per NDA requirements, but
you'd recognize the name). The organization serves
enterprise customers in financial services,
healthcare, and government verticals, with average
deal sizes of $180K and sales cycles averaging 127
days. Before the initiative, customer data was
fragmented across Marketo (email automation),
Salesforce (CRM), Segment (event tracking),
Adobe Analytics (web), Bombora (intent), and
Pendo (product usage). Integration between
systems was limited to nightly batch syncs with
frequent failures. The technology stack post -
integration connected these platforms through
event streaming with sub -second synchronization,
enabling real -time behavioral analytics and
coordinated cross-channel engagement.
Technology stack architecture brings together the
capabilities of marketing automation and customer
experience tools, consolidated data stores, journey
management systems, and analytics. This structure
counterbalances the issues of fragmentation,
whereby different systems record the customer data
uncoordinatedly. The architecture is designed to
handle large volumes of interaction over digital
property, email messages, and content platforms,
enabling extensive capabilities of behavioral
tracking and cross-channel orchestration [6].
3.2 Integration Architecture Design
Behavioral signal capture required defining which
interactions actually predict purchase intent,and our
initial assumptions were mostly wrong. We started
with obvious signals: pricing page visits, demo
requests, contact form submissions. These were
correlated with intent but took place too late in the
trip that they could be used to identify them early.
The fast forward analysis with iterative analyses
helped us to recognize the leading indicators:
repeat visits in 7 days (3 times higher to convert
than single visits), depth of technical
documentation (intense intent signal, yet the
nurturing strategy was needed), comparison of
competitive elements (good intent signal, although
a delicate approach to fostering needed).  We
weighted signals on a 100 -point scale: pricing page
= 15 points, technical docs = 10 points per page
(max 30), repeat visit within 7 days = 20 points,
webinar attendance = 12 points, email engagement
= 5 points per click (max 15).

International Journal of Intelligent Systems and Applications in Engineering                      IJISAE, 2026, 14(1s), 989–997 |  993

Fig 2: Integration Architecture Design [5, 6]

3.3 Experimental Design
A/B testing in B2B requires patience and statistical
discipline that most marketing teams lack. With
200-300 enterprise deals closing annually,
detecting a 20% improvement in conversion
requires months of data collection. Our three
experiments were (1) Integrated journey
orchestration vs. traditional segmented campaigns
(n=4,200 prospects (8 -month test window), (2)
Behavioral lead scoring vs.
demographic/firmographic scoring (n=2,800 MQLs
(6-month test window), and (3) Real -time content
personalization vs. static content delivery
(n=12,400 web sessions (4 -month test window).
The assignment was done randomly as per the first
touch, and the prospects stayed in their assigned
status during the journey. We used Bayesian
analysis with 95% credible intervals rather than
frequentist significance testing, given our sample
size constraints.

Design Element Treatment Group Control Group Measurement Method
Journey
Orchestration
Integrated multi-channel coordination
with unified data
Traditional segmented
campaigns
MQL conversion rate
comparison
Personalization Real-time behavioral analytics, dynamic content Static content delivery Engagement score differential
Lead Scoring Behavioral signals and predictive models Demographic and firmographic criteria Prediction accuracy metrics
Attribution Multi-touch algorithmic model Last-touch attribution Channel contribution analysis
Data Integration Event streaming, sub-second sync Batch processing, daily updates Pipeline velocity tracking
Assignment
Method Random allocation at the initial engagement point Propensity score matching
Table 1: Experimental Design Configuration [5, 6]

International Journal of Intelligent Systems and Applications in Engineering                      IJISAE, 2026, 14(1s), 989–997 |  994

3.4 Measurement Framework
The definition of "marketing qualified lead" defines
uniform qualification standards with firmographic
fit and behavioral engagement limits. Engagement
scoring is a measure of the intensity of interaction
that is based on aggregating behavioral signals with
weights, and algorithms of engagement scoring are
calibrated using historical conversion analysis.
Attribution modeling apportions conversion credit
between touchpoints by the use of algorithmic
methods, balancing between awareness,
consideration, and conversion contributions.
Measurements based on pipeline acceleration
assess the rate of temporal velocity in terms of
treatment versus control group velocity in order to
evaluate the pace of sales in a standardized sales
phase [5].
3.5 Data Collection and Analysis
The 18-month post-implementation period saw the
collection of 847,000 prospect interactions on
23,400 accounts. We have traced individual -level
behavioral events (page views, content downloads,
and email interaction) and aggregated them into
account-level in terms of B2B analytics. Analytical
techniques were logistic regression to convert
predictions to prediction, propensity score
matching to remove the selection bias in the
assignment of an A/B test, and interrupted time -
series analysis to isolate the influence of
implementation on seasonal variation. Model
validation was done in 70/30 train -test splits with
cross validation of 5 -folds of training data. Our
benchmarking was based on the B2B marketing
performance benchmarking provided by Forrester
and the conversion rate benchmarking offered by
SiriusDecisions to enterprise technology.

4. Results and Findings
4.1 Journey Optimization Outcomes
The 34% overall (95% CI: 26% -42) saw in
integrated journey orchestration had significant
variations by segment. Enterprise prospects (more
than 5,000 employees) were the most responsive:
47 percent increase in MQL conversion, where the
effect was top -mid-journey levels of alignment, in
which coordinated multi -channel intervention
substituted the disconnected email campaigns.
Amidst mid -market prospects (500 -5,000
employees) the improvement was more modest 22
with broader confidence ranges implying more
variability in response. Interestingly, the impact
was the most critical in regulated industries
(financial services, healthcare) where the longer the
evaluation cycle, the more it gave a chance to
maintain a long-term engagement. The prospects in
the technology sector, where cycles are less, and
the evaluation paths are more direct, were less
significant but still significant.
4.2 Behavioral Analytics and Lead Scoring
Our initial lead scoring model was a failure,0.62
AUC in production, barely better than random. The
problem: we had built the model on historical data
that included page view counts without dwell time.
A prospect who bounced from the pricing page in 3
seconds received the same signal weight as one
who spent 8 minutes studying pricing tiers. Once
we incorporated dwell time thresholds (minimum
30 seconds for page view credit, weighted scaling
up to 3 minutes), model performance jumped to
0.74 AUC. Adding decay functions for recency
(signals older than 30 days weighted at 50%, older
than 60 days at 25%) pushed performance to 0.78
AUC. The lesson: raw event counts are noisy;
engagement intensity and recency matter more than
volume.
4.3 Content Personalization Impact
Personalization of real -time content enhanced
engagement although the effect size was very
context-dependent. Personalization of websites
(suggestion of content based on behavioral
indicators) boosted the depth of pages by 28
percent and length of sessions by 34 percent. The
impact was most pronounced in the case of the
return visitors and behavioral history--in the case of
new visitors we were minimal in improving them
due to the lack of data to customize. The email
personalization also presented rather modest
outcomes: with the personalization of content
recommendations, using previous engagement
levels as the basis, the rates of click -throughs
improved by 12%. Its limitation was latency: our
ML-based suggestions required 400 -600ms, which
was too slow to be used in -session during web
personalization, but reasonable in email. We
resorted to rule -based customization of the real -
time web experiences (when visited pricing page,
then display ROI calculator; when read technical
documentation, display integration guide) and ML -
based suggestions of next-session targeting.

International Journal of Intelligent Systems and Applications in Engineering                      IJISAE, 2026, 14(1s), 989–997 |  995

4.4 Business Value Metrics
The quantification of financial impact involves the
relationship of the marketing measures to the
pipeline results, which most companies find
difficult. Three were the metrics we monitored: (1)
Marketing-sourced pipeline grew by 38 percent. (1)
Marketing-sourced pipeline increased by 38
percent every year. (2) Marketing -sourced pipeline
increased by $58M to $42M. (2) Marketing -
sourced pipeline increased by 58M to 42M. (3)
Enterprise segments were the most responsive to
journey orchestration (where journey orchestration
had the biggest impact). (2) Sales cycles
compression: Sales of high -touch integrated
journeys (>20 protocoled touchpoints) took an
average of 23 days less to close (104 days vs. 127
days baseline). (3) The rates of win increased
slightly, from 24 to 27, a 12.5 percentage point
relative improvement and statistically significant,
but less than that of pipeline generation. The
incremental revenue that is expected to result as a
result of the initiative is about 4.2M per year, as
compared to the technology and implementation
cost about 1.8M (including platform costs,
integration development, and team time).
4.5 Attribution Analysis
Multi-touch attribution provided channel
contributions that were not in line with our
expectations and altered budget allocation. In the
category of last -touch attribution, paid search was
attributed with 8 per cent of conversion credit,
which does not seem efficient considering that it is
35 per cent of the marketing budget. Based on
multi-touch (position -based with the 30/40/30
weighting), paid search got 22 percent of the credit-
it was generating top of funnel awareness which
later translated into conversion by other mediums.
The contribution of organic content, which
obtained little last -touch credit (prospects do not
always convert directly out of blog posts), was 31%
multi-touch contribution, confirming that content
marketing should be continued to invest in. The
most curious discovery: direct visions of the site,
which prevailed in the case of last -touch attribution
with 34% fell to 18 percent with multi-touch. These
were not technically direct but follow -ups by
prospects who first learned of us in some other way
but then bookmarked the site or typed in the URL.

Channel/Touchpoi
nt
Last-Touch
Model
Multi-Touch
Model Strategic Role
Paid Search 8% 22% Awareness driver, initial discovery
Display Advertising 3% 9% Brand recognition, retargeting support
Organic Content 11% 31% Consistent mid-journey contributor
Webinars 4% 18% Educational touchpoint, consideration stage
Email Nurturing 12% 18% Nurture channel, supporting throughout
Case Studies 8% 14% Social proof, decision validation
Product Demo 19% 16% High intent, late-stage conversion
Direct Website 34% 18% Return visits from prior touchpoints
Sales Interaction 28% 22% Final conversion, requires journey context
Table 2: Channel Attribution Model Comparison Analysis [7, 8]

5. Discussion
5.1 Theoretical Implications
The results confirm with significant reservations
the theoretical hypothesis that single -customer data
structures enhance marketing coordination. The 34
percent increase in MQL and a shorter cycle of 23
days give support to the assertions that have been
more of a theoretical nature in B2B marketing
books. Nonetheless, the data also fall within
boundary conditions: the implication was in
enterprise segments of complex buying journeys

International Journal of Intelligent Systems and Applications in Engineering                      IJISAE, 2026, 14(1s), 989–997 |  996

better performance, and mid -market statistically
nonsignificant difference. This implies that
orchestration benefits must have an appropriate
level of complexity of journeys to become
apparent. The results of the behavioral analytics are
subverting the conventional theory of firmographic
segmentation: the signal of digital engagement was
more effectively predictors of conversion than
company size, industry, or job title,at least among
enterprise prospects having more developed digital
footprint.
5.2 Practical Implications
Implementation advice, gained with the help of
bitter experience: begin with data infrastructure,
not orchestration capabilities. We also went wrong
by implementing journey orchestration when our
identity resolutions were not fully established,
having duplicate profiles, conflicting messages, and
campaigns that conveyed mixed messages to the
same prospect. Orders of sequence: (1) Event
streaming and identity resolution (3 -4 months), (2)
Unified customer profiles with behavioral data (2 -3
months), (3) Cross -channel journey orchestration
can only be enabled at this point (3 -4 months). Full
realistic schedule: 12 -18 months to full
functionality, but not 6 months as vendors will
claim. Budget 30% contingency,we were 40
percent above our original estimate because of the
complexity in integration with the legacy systems.
5.3 Generalizability and Boundary Conditions
Limits to generalizability are evident. The
framework is most applicable to B2B enterprise
technology where the selling and buying process is
more complex with multi -stakeholder purchases
and sales cycle being over 90 days long. We are
fairly sure it generalizes into similar situations:
enterprise software, professional services,
industrial equipment, and complicated financial
products. Healthcare and pharmaceuticals are also
under further restrictions of HIPAA and other laws
that restrict behavioral tracking. Procedures
involving a high level of offline touchpoint (trade
show, field sales) in manufacturing demand other
data capture solutions than discussed here. Those
consumer markets whose cycle is shorter and
whose decision -makers would act individually are
governed by entirely different dynamics --the
structure would need significant reworking.

5.4 Limitations
There are serious limitations of the study that
should be taken into account by the readers. Single -
case methodology is rich in description, but it lacks
breadth: we might be seeing organizational
peculiarities, and not necessarily their general
trends. The situation in the cybersecurity industry
presents certain boundary conditions: buyers of
security are exceptionally technical, appraisals
entail security -related requirements, and usually,
purchasing decisions are made after a peer
organization has been breached. These dynamics
may fail to be transferred to other categories of
enterprise technology. Another limitation is
platform dependency: we were strongly dependent
on the event streaming functionality of Segment
and the automation features of Marketo. With the
adoption of other platforms, organizations would
have to implement patterns of integration on a large
scale. Last but not least, the 18 months
implementation and stabilization but not long -term
sustainability is encompassed within the
observation window. It is yet to be known whether
benefits will continue, degenerate, or accumulate
over 3-5 years.
5.5 Future Research Directions
These findings would be enhanced by three
research directions. First, cross industry replication:
are there similar results with similar architectures
in professional services, manufacturing or in
healthcare? Boundary conditions would be highly
defined by comparative studies that would adjust
industry-specific factors. Second, longitudinal
sustainability: our 18 months window will
represent effects of implementation but not the
long-term dynamics. Do benefits persist? Are
systems in constant need of optimization
investment? Does organizational capability plateau
or develop? Third, AI implementation: AI
technologies that start to develop in 2024 -2025,
like generative AI, will transform the nature of
content personalization significantly and drive the
potential of scoring. A study on the differences
between AI -enhanced and rule -based journey
orchestration would be both timely and practically
helpful.

Conclusion
Integrated marketing technology platforms deliver
measurable business value in enterprise B2B

International Journal of Intelligent Systems and Applications in Engineering                      IJISAE, 2026, 14(1s), 989–997 |  997

settings,but the path to value is longer and more
complex than vendor pitches suggest. Our 18 -
month initiative produced 34% improvement in
MQL conversion, 38% increase in marketing -
sourced pipeline, and 23 -day reduction in sales
cycle duration. These results justify the investment.
But they required three major course corrections,
including rebuilding our lead scoring model after
initial deployment failed, and total investment
approximately 40% higher than initial estimates.
The framework presented here reflects what
actually worked after iteration, not theoretical best
practices. Organizations pursuing similar initiatives
should expect 12 -18 months to full capability,
budget significant contingency, and prioritize data
infrastructure over orchestration features. The
competitive advantage from integrated customer
data is real, but it compounds over time rather than
appearing immediately. Start now, be patient, and
measure relentlessly.

References
[1] Lisa Lundin and Daniel Kindström,
"Digitalizing customer journeys in B2B markets,"
ScienceDirect, 2023. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S
0148296322011043
[2] Ravi Surampudi, "The Integration Challenge:
how Siloed Marketing Technology Stacks Hinder
Campaign Orchestration and Budget
Optimization," ResearchGate, 2025. [Online].
Available:
https://www.researchgate.net/publication/39679160
0_The_Integration_Challenge_how_Siloed_Market
ing_Technology_Stacks_Hinder_Campaign_Orche
stration_and_Budget_Optimization
[3] W. W. Moe and P. S. Fader, "Dynamic
Conversion Behavior at E -Commerce Sites,"
Management Science, vol. 50, no. 3, pp. 326 -335,
2004. [Online]. Available:
https://doi.org/10.1287/mnsc.1040.0153
[4] V. Kumar et al., "Creating a Measurable Social
Media Marketing Strategy for Hokey Pokey:
Increasing the Value and ROI of Intangibles and
Tangibles," Marketing Science, vol. 32, no. 2, pp.
194-212, 2013. [Online]. Available:
https://doi.org/10.1287/mksc.1120.0768
[5] Nicholas Larsen et al., "Statistical Challenges in
Online Controlled Experiments: A Review of A/B
Testing Methodology," The American Statistician,
2024. [Online]. Available:
https://www.tandfonline.com/doi/pdf/10.1080/0003
1305.2023.2257237
[6] Maria Holmlund et al., "Customer experience
management in the age of big data analytics: A
strategic framework," ScienceDirect, 2020.
[Online]. Available:
https://www.sciencedirect.com/science/article/pii/S
0148296320300345
[7] Nelito Calixto and João Ferreira, "Salespeople
Performance Evaluation with Predictive Analytics
in B2B," MDPI, 2020. [Online]. Available:
https://www.mdpi.com/2076-3417/10/11/4036
[8] P. Anderl et al., "Mapping the Customer
Journey: Lessons Learned from Graph -Based
Online Attribution Modeling," International
Journal of Research in Marketing, vol. 33, no. 3,
pp. 457 -474, 2016. [Online]. Available:
https://doi.org/10.1016/j.ijresmar.2016.03.001
[9] Nicola Bellantuono et al., "Digital
Transformation Models for the I4.0 Transition:
Lessons from the Change Management Literature,"
MDPI, 2021. [Online]. Available:
https://www.mdpi.com/2071-1050/13/23/12941
[10] Sanjeev Verma et al., "Artificial intelligence in
marketing: Systematic review and future research
direction," ScienceDirect, 2021. [Online].
Available:
https://www.sciencedirect.com/science/article/pii/S
2667096820300021
