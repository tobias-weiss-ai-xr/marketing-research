---
title: Big Data Analytics and Behavioural Targeting in Digital Retail
url: https://doi.org/10.47715/978-93-86388-70-4/ch2
category: privacy-data
subcategory: measurement
date: 2026-05
venue: Jupiter Publications Consortium eBooks
authors:
- G. Senthil Velan
source: openalex-oa
pdf_url: https://doi.org/10.47715/978-93-86388-70-4/ch2
pages: 34
chars: 83663
fetched_at: '2026-11-08T17:36:08+00:00'
kb_version: 1
---

# Big Data Analytics and Behavioural Targeting in Digital Retail

Chapter-Level Metadata and Citation Information
 AI and Data Analytics in Business
 Edited Book
Chapter 2
Big Data Analytics and Behavioural Targeting in Digital Retail
Author(s)
G. Senthil Velan
Affiliation(s)
Assistant Professor, Department of Computer Science and Engineering, Dr. M. G. R Educational and Research
Institute, Chennai, Tamil Nadu, India
Chapter DOI
https://doi.org/10.47715/978-93-86388-70-4/Ch2
Book DOI
https://doi.org/10.47715/978-93-86388-70-4
E-ISBN
978-93-86388-70-4
Editors
S. Mohan Kumar; A. Shajin Nargunam; Hemalatha Arunachalam; Duraisamy Balaganesh
Publisher
Jupiter Publications Consortium, Chennai, Tamil Nadu, India
Publication Year
2026
Suggested Citation
Senthil Velan, G. (2026). Big Data Analytics and Behavioural Targeting in Digital Retail. In S. Mohan Kumar, A. Shajin Nargunam,
Hemalatha Arunachalam, & Duraisamy Balaganesh (Eds.), AI and Data Analytics in Business. Jupiter Publications Consortium.
https://doi.org/10.47715/978-93-86388-70-4/Ch2
Chapter File Note
This chapter PDF has been prepared for chapter-level access, citation, and dissemination. It contains this chapter metadata page followed
by the respective chapter content, including figures, tables, equations, and chapter references. The full book cover and complete front
matter are intentionally not repeated in this chapter file.
 The chapter content that follows is retained unchanged from the edited book PDF.

Chapter 2
Big Data Analytics and Behavioural
Targeting in Digital Retail
G. Senthil Velan
Assistant Professor, Department of Computer Science and Engineering
Dr. M. G. R Educational and Research Institute, Chennai, Tamil Nadu, India.
DOI: https://doi.org/10.47715/978-93-86388-70-4/Ch2
Abstract
This chapter examines how big data analytics reshapes digital retail by converting large
volumes of behavioural, transactional, contextual, and operational data into targeted
decisions. Digital retailers now observe the customer journey through search queries, clicks,
dwell time, baskets, payments, returns, loyalty records, service interactions, mobile location
signals, and social responses. These signals do not have value because they are numerous.
They become commercially useful when they are governed, integrated, interpreted, and
converted into timely interventions that improve customer relevance while protecting
trust. The chapter explains the main data sources used in retail analytics, the architecture
required to transform raw event streams into actionable insights, and the analytical
methods behind segmentation, propensity modelling, recommender systems, dynamic
offers, and customer lifetime value management. It also considers the organisational
and ethical conditions that determine whether behavioural targeting strengthens or
damages customer relationships. Particular attention is given to privacy, consent, fairness,
39

Chapter 2. Big Data Analytics and Behavioural Targeting 40
explainability, experimentation, measurement, and accountability. The chapter argues that
behavioural targeting should be understood not as a narrow advertising technique but as
a decision system operating across merchandising, marketing, pricing, service design, and
fulfilment. Retailers that combine analytical sophistication with disciplined governance
are better placed to deliver personalised experiences that are useful, measurable, and
legitimate.
Keywords
Big data analytics, behavioural targeting, digital retail, customer journey, customer
segmentation, recommender systems, data governance, customer trust
2.1 Introduction: From digital traces to retail deci-
sions
Retailing has always depended on the interpretation of customer behaviour. A shopkeeper
noticing that a regular customer buys coffee every Friday, a catalogue merchant segmenting
households by response rates, and a supermarket analysing loyalty card transactions are all
using evidence to shape commercial decisions. The granularity, velocity, and connectedness
of the evidence are new in digital retail. Every search, page view, product comparison, cart
addition, couponredemption, returnrequest, chatbotexchange, anddeliverypreferencecan
be captured as a behavioural trace. When these traces are linked to product information,
inventory positions, margin data, campaign history, and customer consent status, they
become raw materials for big data analytics. Big data analytics in digital retail refers
to the systematic use of large, varied, and fast-moving data to understand customers,
forecast demand, personalise experiences, and optimise decisions (Davenport, 2006; Chen
et al., 2012; Wedel & Kannan, 2016). The term “big” should not be interpreted only
as size. A retailer may have billions of page views but very little insight if the data are
poorly structured, isolated from business decisions, or collected without a clear purpose.
Conversely, a retailer with modest traffic can create substantial value if it captures the
right signals, connects them across channels, and uses them to improve decisions that
customers actually experience. Therefore, the managerial question is not how much data
the retailer possesses but how effectively the organisation converts data into trustworthy
actions. Behavioural targeting is the application of this analytical capability to select
messages, products, prices, services, or experiences based on observed or inferred behaviour.

Chapter 2. Big Data Analytics and Behavioural Targeting 41
In advertising, the term often refers to the use of browsing or purchase signals to decide
which advertisement to show. The concept is broader in digital retail. Targeted actions
might be a personalised homepage, replenishment reminder, recommendation carousel,
tailored search ranking, service recovery message, risk-based fraud check, loyalty incentive,
dynamic bundle, abandoned-basket nudge, or next-best-action suggestion for a customer
service agent. Targeting becomes behavioural when the trigger is not merely demographic
identity but patterns of action: what customers browse, compare, ignore, buy, return,
review, or ask.
The strategic promise is simple. If retailers can recognise what a customer is trying
to accomplish, they can reduce search effort, increase relevance, improve conversion,
raise basket value, protect margin, and build loyalty. A customer buying a camera
may need a memory card and a protective case; a customer repeatedly viewing baby
products may appreciate replenishment reminders; a customer comparing sizes may
need richer fit guidance; and a customer with repeated failed deliveries may require a
different fulfilment option. In each case, behavioural data help retailers move from generic
communication to context-aware assistance. However, the same capability creates tension
(Zuboff, 2019). Behavioural targeting can feel convenient when it solves a problem, but
intrusive when it appears to know too much, follows the customer across contexts or
manipulates vulnerability. Digital retail is not merely a technical environment; it is a
relational environment. Customers grant attention, data, and payment in exchange for
value, convenience, and confidence. If targeting practices are opaque, excessive, or unfair,
the relationship weakens, even when short-term conversion rises. Therefore, the business
case for analytics must be balanced with a trust case: why the data are needed, how the
inferenceismade, whobenefits, andwhatchoicesthecustomerretains. Thischapteradopts
a systems perspective. It begins with datafication, explaining how digital retail produces
data across the customer journey and operating model. It then turns to architecture and
analytics, describing how retailers combine data platforms, feature engineering, modelling,
and decision engines. Subsequent sections examine segmentation, predictive modelling,
recommendation, journey orchestration, experimentation, and attribution. The chapter
then addresses governance, privacy, and fairness because these issues are not external
constraints but design conditions. Finally, it sets out an implementation roadmap and
a practical case vignette showing how a retailer might build a behavioural targeting
program without losing sight of customer legitimacy. A central theme is that behavioural
targeting is not a single campaign. It is a capability that depends on data quality,
analytical discipline, process redesign, and ethical judgement. Retailers that treat it as

Chapter 2. Big Data Analytics and Behavioural Targeting 42
a marketing plug-in often create fragmented experiences: one system sends a discount,
another recommends the same product after purchase, and a third continues to retarget a
customer who has already complained. Retailers that treat it as an enterprise decision
system can coordinate across touchpoints, measure the incremental impact, and manage
the risk of over-personalisation. The difference is not only in technology but also in
governance and operating discipline. Throughout this chapter, the term customer should
be understood broadly. Digital retail analytics can support end consumers, business buyers,
marketplace sellers, delivery recipients, and service users. Similarly, the term retailer
covers pure-play e-commerce firms, omnichannel retailers, marketplaces, subscription
businesses, and direct-to-consumer brands. Their data maturity differs, but the core
managerial problem is shared: how to use behavioural evidence to make better decisions
while preserving the conditions of trust that make data use acceptable.
2.2 Datafication of the digital retail journey
The digital retail journey is highly datafied because many actions that were once invisible
are now automatically recorded. In a physical store, a retailer might know what was
purchased and perhaps infer what was considered from shelf observations or conversations
with staff. In an online store, the retailer can observe the path to purchase with far more
detail: entry source, search terms, filters used, product pages opened, images viewed,
reviews expanded, videos played, sizes selected, delivery options checked, payment failures
encountered, and exit points (Kitchin, 2014; Lemon & Verhoef, 2016). These behaviours
reveal intent, friction, and preference, even when no purchase occurs. Retail data can
be categorised into several categories. Transactional data describe purchases, payments,
refunds, returns, and subscriptions. Behavioural data describe digital events such as
clicks, scrolls, search queries, dwell time, and basket changes. Customer profile data
include account attributes, loyalty membership, communication permissions, and declared
preferences. Product data include descriptions, attributes, images, prices, margins, stock
status, and compatibility rules. Contextual data include device type, channel, time,
location where lawful and relevant, weather, campaign exposure, and referral source.
Operational data include inventory availability, delivery performance, customer service
capacity, and supplier lead times. Analytical value arises when these categories are
connected.
First-party data have become especially important in digital retail because they are
collected directly through the retailer’s own channels and relationships. Examples include

Chapter 2. Big Data Analytics and Behavioural Targeting 43
account behaviour, loyalty records, transaction histories, onsite search, app engagement,
email response, and customer service interactions. First-party data are not automatically
risk-free; they still require lawful processing, transparency, and security (European Com-
mission, n.d.-a). Nevertheless, they often provide a stronger foundation for behavioural
targeting than third-party data because they are closer to the customer’s actual relation-
ship with the retailer and can be governed within a clearer consent and purpose framework.
Event data are the most distinctive forms of digital retail evidence. An event records
that something happened at a point in time: customer A viewed product B, searched for
term C, added item D to the basket, used filter E, or clicked message F. Event data are
powerful because they support sequence analysis. The order of actions often matters more
than isolated actions. A customer who searches for “waterproof hiking boots”, filters by
size, reads reviews, and returns the next day has a different intent profile from a customer
who lands on a product page from a social post and leaves after three seconds. Therefore,
behavioural targeting should pay attention to patterns over time, not merely individual
signals.
The datafication of retail also extends to products. Product information management
systems capture attributes such as brand, material, colour, size, compatibility, ingredients,
sustainability claims, warranty length, and fulfilment restrictions. These attributes allow
algorithms to match customer intent with merchandise sales. Poor product data weaken
targeting because even a sophisticated model cannot recommend the right item if the
underlying catalogue is incomplete, inconsistent, or inaccurate. For example, a search-
ranking model may misinterpret the demand for “wide fit shoes” if the product catalogue
uses inconsistent labels such as wide, W, extra comfort, or relaxed fit. Operational
data complete this picture. A recommendation that ignores inventory may promote
out-of-stock products. A promotion that ignores fulfilment capacity may generate orders
that the retailer cannot deliver on time. A price incentive that ignores the margin may
increase revenue while reducing profitability. Behavioural targeting is therefore not just
customer analytics; it requires integration with retail operations. The target action must
be feasible, profitable, and serviceable. This point is especially important in omnichannel
retail, where customers may browse online, collect in-store, return by post, and contact
support through chat. Data quality remains a persistent challenge. Retail systems often
contain duplicate customer records, inconsistent product identifiers, missing consent states,
delayed transaction feeds, and unreliable campaign tags. Identity resolution is particularly
challenging. The same person may use a mobile app, desktop browser, guest checkout,
loyalty account, and marketplace account. Device sharing and household purchasing

Chapter 2. Big Data Analytics and Behavioural Targeting 44
further complicate this issue. Retailers must decide when identities are confidently linked,
when they should remain separate, and how to avoid making inappropriate inferences
about consumers. A false match can lead to irrelevant or embarrassing targeting, while
an overly cautious approach may reduce personalisation but protect trust. The richness
of behavioural data should not tempt retailers to collect everything indefinitely. Data
minimisation is both a legal and managerial discipline. Data that do not support a defined
purpose create storage costs, security exposure, and ethical risks. The best analytics
teams begin by identifying the decisions they want to improve, and then work backward
to the data needed to support those decisions (Davenport, 2006; Provost & Fawcett, 2013).
This approach avoids the common mistake of building a data lake that becomes a data
swamp: large, expensive, poorly understood, and disconnected from action.
Figure 2.1:Digital retail data ecosystem
Figure 2.1 explains how behavioural, transactional, product, contextual and operational
data flow into a customer analytics layer that converts raw retail signals into targeted
decisions under governance controls.

Chapter 2. Big Data Analytics and Behavioural Targeting 45
2.3 Building the analytics architecture
A behavioural targeting program requires an architecture that moves data from capture
to decision (Chen et al., 2012; Provost & Fawcett, 2013). The simplest way to understand
this architecture is as a chain: data collection, ingestion, storage, processing, feature
creation, modelling, decisioning, activation, and measurement. Each link must be reliable
and accurate. A weakness in any part of the chain can undermine the entire program.
For example, a strong machine learning model is of limited value if campaign tags are
inconsistent, consent signals are not enforced, or recommendations cannot be delivered
to the website quickly enough to influence the session. Data collection began at the
touchpoint. Websites, apps, point-of-sale systems, call centres, email platforms, and
fulfilment systems generate logs and events. These signals are usually captured through
event instrumentation, application programming interfaces, batch exports, or streaming
services. Good instrumentation requires a shared tracking plan that defines event names,
attributes, timing, and ownership. In the absence of a tracking plan, teams create
overlapping events with different meanings. One team may define add-to-cart as clicking
the basket button, another as successfully updating the cart, and another as reaching
the basket page, for example. Such ambiguity contaminates the analysis and weakens
the targeting rules. Ingestion moves the data into a central environment. Some data
arrive in real time, whereas other data arrive in scheduled batches. Real-time ingestion is
valuable for session-level targeting, fraud prevention, and stock-sensitive recommendations.
Batch ingestion is often sufficient for daily segmentation, reporting, and model training.
A mature retailer uses both methods. The key is to match the latency to the decision
need. It is unnecessary and costly to stream every field if the decision changes weekly,
but it is damaging to rely on yesterday’s data when deciding whether to show a product
that has just gone out of stock. Storage and processing are commonly organised around
data warehouses, data lakes, or lakehouse architectures. A warehouse provides structured
and governed data for analytics and reporting. A lake stores large volumes of raw or
semi-structured data. A lakehouse attempts to combine the flexibility of a lake with
the reliability of warehouse-style management. The architectural label matters less
than the management discipline: data should be discoverable, documented, secured,
versioned, and connected to business definitions. Retail teams need to know what “active
customer”, “conversion”, “net sales”, “return rate”, and “consent” mean in specific tables
and dashboards. Feature engineering converts raw data into variables that can be used by
models (Provost & Fawcett, 2013). A raw click event may become features such as the
number of product views in the last seven days, category diversity, average discount viewed,

Chapter 2. Big Data Analytics and Behavioural Targeting 46
time since the last purchase, number of failed searches, return frequency, loyalty tenure, or
preferred fulfilment method. Feature engineering is the process by which retail knowledge
is incorporated into the model. A useful feature often encodes a business hypothesis:
repeated views without purchase may signal consideration, frequent returns may signal
fit uncertainty, high use of filters may indicate specific preferences, and engagement
with care guides may indicate the need for reassurance. Feature stores are increasingly
used to consistently manage reusable features across models and channels. They reduce
duplication by allowing analysts to define a feature once and use it in the training and
serving environments. This consistency is important because many targeting failures arise
when a model is trained on one version of a variable and deployed with another. For
example, a customer lifetime value model trained on net revenue after returns should not
be served with gross revenue before returns are accounted for.
Figure 2.2:Retail analytics pipeline from event capture to activation
Figure 2.2 explains the end-to-end retail analytics pipeline, showing how captured events
are ingested, stored, engineered into features, modelled, converted into decisions, activated
in channels and measured through feedback.
This discrepancy may produce inflated value estimates and inappropriate incentives.
Decision engines connect analytics to actions. A model may estimate purchase propensity,
churn risk, or product affinity, but the retailer still needs rules to decide what to do with
the score. A decision engine can combine model outputs with business constraints, such as
margin thresholds, inventory status, eligibility rules, frequency caps, consent permissions,
and contact policies. The best available action for a touchpoint can then be selected. The
output might be a message, offer, recommendation, ranking adjustment, service script, or
suppression. Decisioning is the point at which prediction becomes a managerial choice.
Activation systems deliver the chosen action through websites, apps, emails, advertising

Chapter 2. Big Data Analytics and Behavioural Targeting 47
platforms, customer service tools, or store associate applications. Activation must be fast
enough for the context and consistent enough to prevent contradictory experiences from
occurring. A customer should not receive an abandoned basket email for an item already
purchased, nor should a service agent recommend a product that the website has just
marked unavailable.
Therefore, the integration of decision and activation systems is both a technical and
customer experience issue. The measurement closes the loop. Every targeted action should
generate data on exposure, response, conversion, revenue, margin, returns, satisfaction,
and long-term behaviour. These outcomes feed dashboards, experiments, and model
retraining. Without measurement, targeting becomes a black box. With measurements,
retailers can compare interventions, estimate incremental impacts, and detect unintended
consequences (Varian, 2014; Wedel & Kannan, 2016). The architecture is therefore circular
rather than linear: data inform decisions, decisions create outcomes, outcomes become
new data, and governance supervises the loop.
2.4 Customerunderstanding: segmentation, personas
and behavioural states
Segmentation is one of the oldest uses of retail analytics, but digital behaviour changes
what segmentation means (Wedel & Kannan, 2016). Traditional segmentation often
groups customers by demographic attributes, geography, purchase value, or lifestyle survey
responses. Digital retail allows more dynamic groupings based on behaviour: browsers who
compare extensively, bargain seekers who respond to discounts, loyal replenishment buyers,
new customers in onboarding, customers at risk of churn, high-return shoppers, gift buyers,
category explorers, and customers who abandon during delivery selection. These groups
are not fixed identities; they are behavioural states that may change as the context changes.
A useful segment must be identifiable, interpretable, reachable, and actionable. Identifiable
means that the retailer can assign customers or sessions to the segment using the available
data. Interpretable means that managers can sufficiently understand the segment to design
actions. Reachable means that the retailer has permission and channels to engage the
segment. Actionable means that different treatments are likely to create different outcomes.
Segmentation that produces elegant clusters but no differentiated action is an analytical
exercise rather than a targeting capability. Descriptive segmentation uses historical data
to summarise patterns. Recency, frequency, and monetary value analysis remains useful

Chapter 2. Big Data Analytics and Behavioural Targeting 48
because it captures how recently customers purchased, how often they purchase, and how
much they spend. Digital retailers often extend this with engagement variables such as
browsing frequency, category breadth, email response, app use, and service interactions.
The result is a richer view of customer activities. However, descriptive segments should
not be confused with the causal explanations. Customers in a high-value segment may
be high value for reasons unrelated to the retailer’s treatment, and excessive incentives
may subsidise purchases they would have made anyway. Behavioural segmentation can
also be session-based. A visitor who arrives through a paid search for a specific product,
applies size and price filters, and checks delivery availability may be close to making
a purchase. Visitors who browse editorial content and inspirational collections may be
exploring. Visitors who repeatedly search with no results may become frustrated. Session
segments are valuable because they support real-time decisions, even when the retailer
knows little about the customer’s identity. This is important for guest users, new visitors,
and privacy-conscious customers who do not log in.
Personas translate analytical findings into human-centred narratives. A persona such as
“the deadline-driven gift buyer” or “the careful specification comparer” can help marketers,
merchandisers, and designers imagine customer needs. The danger is that personas can
become stereotypes if they are detached from data or treated as permanent traits. In
behavioural targeting, personas should be used as design aids, not as rigid labels. They
are most useful when they represent tasks, motivations, and friction points rather than
broad personality claims. Customer lifetime value (CLV) is a key construct in behavioural
targeting (Fader, 2012). It estimates the economic value of a customer relationship over
time, sometimes incorporating revenue, margin, retention probability, service cost, returns,
and acquisition cost. CLV can guide resource allocation by distinguishing customers
who merit retention investments from those for whom heavy discounting is unprofitable.
However, CLV should be used cautiously. If a retailer only invests in valuable customers,
it may neglect emerging customers or create inequitable service tiers. The model should
be transparent about its assumptions and monitored for systematic exclusion. Propensity
models estimate the likelihood that a customer will take a particular action, such as
purchasing, churning, responding to an email, returning an item, or buying from a category.
These scores can power targeting decisions. For example, a retailer may suppress discounts
for customers with a high purchase propensity and reserve incentives for customers whose
probability of purchase increases materially with an offer. This logic requires more than
just a prediction. This requires estimating the incremental effect. A customer likely to buy
without an offer should not be treated the same way as a customer likely to buy only if the

Chapter 2. Big Data Analytics and Behavioural Targeting 49
offer is shown. Segmentation can be harmful when it overreaches. Behavioural data may
indirectly reveal sensitive situations, such as health concerns, financial stress, or family
changes. Even when a retailer does not explicitly collect sensitive attributes, models can
infer patterns that customers would not expect. Therefore, responsible segmentation
requires purpose limitation, exclusion rules, and review. Analysts should ask whether the
segment is commercially relevant, whether the inferred label is respectful, whether the
customer would find the treatment acceptable, and whether the segment could produce
unfair or exploitative outcomes. The best segmentation systems combine both stability
and responsiveness. Stable customer-level segments support planning, budgeting, and
relationship strategies. Responsive behavioural states support real-time relevance. A
loyal customer may still be in a frustrated session, a discount-sensitive customer may
still buy urgently at full price, and a high-value customer may be shopping for someone
else. Therefore, targeting should combine long-term customer understanding with the
immediate context. This combination is one of the distinctive advantages of big data
analytics in digital retailing.
Current behavioural state
Long-term customer value
Low-cost
reactivation
Growth-oriented
engagement
High-value
recovery
Priority
personalisation
Passive / low intentActive / high intent
Lower
Higher
Figure 2.3:Behavioural segmentation matrix
Figure 2.3 explains how long-term customer value and current behavioural state can
be combined to define targeting priorities, from high-value recovery actions to low-cost
reactivation or growth-oriented engagement.
2.5 Predictive analytics and decision models
Predictive analytics uses historical data to estimate future outcomes and unknown states
(Provost & Fawcett, 2013; Varian, 2014). In digital retail, predictive models support

Chapter 2. Big Data Analytics and Behavioural Targeting 50
demand forecasting, churn prevention, product affinity, fraud detection, returns prediction,
size recommendations, promotion response, customer service routing, and stock allocation.
Prediction is valuable because retail decisions are made with uncertainty. A retailer does
not know with certainty whether a visitor will buy, whether an email will prompt action,
whether a product will be returned, or whether the demand will exceed the inventory.
Models reduce uncertainty by learning from data patterns. The modelling process begins
with a clearly defined target variable. Poorly defined targets lead to poor decisions. If
the target is to purchase within seven days, the model serves a different purpose than
purchasing during the current session. If the target is gross revenue, the model may prefer
customers who buy and return heavily. If the target is the margin after returns, the model
may choose different actions. Analysts should define the target in terms of the decisions to
be made. A targeting model for discount allocation should not simply predict purchases;
it should inform whether the offer changes profitable behaviour.
Common modelling approaches include logistic regression, decision trees, random forests,
gradient boosting, neural networks, survival models, and sequence models
(Provost & Fawcett, 2013). The choice depends on the volume and structure of the
data, the need for interpretability, computational requirements, and the cost of errors.
Simple models often perform well when the features are strong and the decisions require
explanation. More complex models can capture nonlinear relationships and interactions
but may be more difficult to govern. The goal is not to use the most fashionable technique;
rather, it is to use the method that best fits the business problem, data quality, and risk
environment. The training data should reflect the context in which the model will be
used. A model trained on customers who already receive heavy email communication may
not generalise to customers with lower contact frequencies. A recommendation model
trained during the holiday period may overstate seasonal preferences. A fraud model
trained before a new payment method is launched may miss new patterns. Retail data are
dynamic. Product ranges change, competitors react, economic conditions shift, marketing
calendars vary, and customer behaviour evolves. Therefore, monitoring drift is essential.
Model evaluation must connect statistical performance to business impact. Accuracy,
precision, recall, area under the curve and calibration are useful technical metrics, but they
do not automatically prove commercial value. A model may rank customers well but still
fail to improve profits if the action is poorly designed. A returns prediction model may
reduce returns but also discourage legitimate purchases if it is applied too aggressively.
Retailers should evaluate both the model and intervention quality. The question is

Chapter 2. Big Data Analytics and Behavioural Targeting 51
not only “did the model predict?” but “did the model help the organisation choose a
better action?” Uplift modelling addresses this question more directly by estimating the
incremental effect of the treatment (Varian, 2014; Wedel & Kannan, 2016). Instead of
predicting who is likely to buy, uplift models attempt to identify who is more likely to buy
because of the treatment. This distinction is critical for behavioural targeting. Sending a
discount to everyone with a high purchase propensity may waste the margin. Sending
it to customers with positive incremental responses may improve profits. Uplift models
require experimental or quasi-experimental data because they depend on comparisons
of treated and untreated outcomes. They illustrate why analytics and experimentation
should be designed to work together.
Prescriptive analytics goes beyond prediction by recommending actions within constraints.
For example, a retailer may have a budget for offers, a limit on customer contact frequency,
inventory constraints, margin targets, and fairness rules. A prescriptive system can
allocate offers or messages to optimise an objective within these constraints. This is where
behavioural targeting becomes a decision-optimisation problem. It also becomes more
governance-intensive because the objectives must be explicit. Optimising for short-term
revenue may produce different actions from optimising for long-term customer value,
margin, satisfaction, or trust.
Explainability is important because retail decisions affect customer experience and organi-
sational accountability (National Institute of Standards and Technology, 2023). Managers
need to understand why a model recommends a segment, suppresses an offer, or prioritises
a product. In some contexts, customers may also require meaningful explanations. Ex-
plainability can be supported by using interpretable models, feature importance analysis,
local explanation tools, documentation, model cards, and decision logs. The purpose
is not to reveal proprietary code but to ensure that the retailer can justify the logic
of consequential decisions. The most reliable predictive capability is achieved through
iterative learning. Analysts define a decision, develop a model, deploy it to a limited
context, measure its performance, review errors, adjust features, and repeat. Large, one-off
modelling projects often disappoint because they treat predictions as deliverables rather
than managed capabilities. Retail behaviour changes too quickly for static models to
remain valid. Continuous monitoring, retraining and business review are necessary to
keep predictive analytics aligned with customer behaviour and retail strategy.
Figure 2.4 explains the workflow that turns a predictive target into a governed retail
action through feature creation, model training, scoring, business rules, action selection

Chapter 2. Big Data Analytics and Behavioural Targeting 52
Figure 2.4:Prediction-to-decision workflow
and continuous monitoring.
2.6 Recommender systems and personalised merchan-
dising
Recommender systems are among the most visible applications of big data analytics in
digital retailing (Shankar, 2018; Wedel & Kannan, 2016). They select products, content, or
services that a customer may find relevant. A recommendation can appear as “customers
also bought”, “you may also like”, “complete the look”, “recommended for you”, “popular
in your size”, “frequently bought together”, or “because you viewed”. Although these labels
seem simple, the underlying models can be sophisticated, and their commercial impact
can be substantial when recommendations reduce search effort and expose customers to
appropriate merchandise. Collaborative filtering recommends items based on patterns
among users and items. If customers who bought item A also bought item B, item B may
be recommended to another customer viewing item A. User-based methods look for similar
customers; item-based methods look for similar products. Collaborative filtering can
discover relationships that are not obvious from product taxonomy; however, it struggles
with cold starts when new products or customers have limited history. It may also reinforce
popularity by repeatedly recommending bestsellers while underexposing niche or new
products. Content-based recommendation systems use product attributes and customer
preferences. If a customer views linen shirts in neutral colours, the system may recommend
similar items based on fabric, category, colour, style, and price range. Content-based
approaches are useful when product metadata are rich and behavioural history is sparse.
Their weakness is that they can become narrow, recommending only close substitutes and

Chapter 2. Big Data Analytics and Behavioural Targeting 53
failing to inspire new discoveries. Hybrid systems combine collaborative, content-based,
and contextual signals to balance relevance, novelty, and diversity.
Personalised merchandising extends recommendations to the arrangement of the retail
interface. Search results, category pages, homepage modules, banners, filters, and editorial
content can be adapted to customer behaviour. A customer who frequently buys premium
skincare products may see higher-end products earlier; a customer searching for sustainable
materials may see relevant filters; and a customer in a hurry may see availability and
delivery speed emphasised. The aim is not to create a completely different store for every
customer, which can be confusing, but to reduce friction and highlight relevant options.
The same customer may require different recommendations depending on the mission. A
customer buying a gift should not receive recommendations based solely on their personal
purchase history. A customer replacing a broken appliance may prioritise availability and
compatibility over discovery. A customer browsing a sale may be more price-sensitive.
Behavioural targeting should therefore infer shopping missions where possible and provide
ways for customers to correct the system. Explicit preference controls, filters, and feedback
buttons can improve both relevance and trust. Recommendation systems should be
optimised more than the click-through rate. A product that attracts clicks may not
generate profitable or satisfactory sales. Retailers should consider conversion, margin,
return rate, inventory position, customer satisfaction, diversity of exposure, and long-term
value. For fashion, a recommendation that improves fit accuracy may reduce returns, even
if it lowers the immediate basket size. For groceries, replenishment recommendations may
improve convenience and retention. For electronics, compatibility recommendations can
prevent service problems. The objective design determines the behaviour of the system.
Figure 2.5 explains how collaborative filtering, content-based features, contextual signals,
merchant rules and customer profile data are fused in a hybrid recommendation engine
and ranked against commercial and customer-experience objectives.
There is a risk of filter bubbles in retail, where customers are repeatedly shown similar
products, and the assortment feels narrower than it is. This can reduce discovery and
disadvantage new brands and minority suppliers. Diversity and exploration mechanisms
can help address this issue. A system can reserve space for new products, complementary
categories, editorial selections, or serendipitous suggestions. Exploration should be
managed carefully to ensure that the recommendations remain useful. The challenge
is to balance the exploitation of known preferences with the discovery of potentially
valuable alternatives. Recommender systems require continuous curation. Algorithms may

Chapter 2. Big Data Analytics and Behavioural Targeting 54
Figure 2.5:Hybrid recommender system in digital retail

Chapter 2. Big Data Analytics and Behavioural Targeting 55
identify statistical associations that are commercially inappropriate, such as recommending
incompatible accessories, insensitive products after a service complaint, or items that
conflict with regulatory guidelines. Human merchandising rules are still important
(Shankar, 2018). Retailers need exclusion lists, compatibility constraints, brand guidelines,
margin thresholds, and safety checks. The strongest systems combine the algorithmic
scale with merchant judgement. They allow humans to set strategic intent and guardrails
while machines handle ranking across large catalogues and rapidly evolving contexts.
Transparency can improve this acceptance. Labels such as “because you viewed running
shoes” or “popular with customers who bought this item” help customers understand why
a recommendation is made. However, the explanations must be truthful. Misleading labels
erode this confidence. Customers should also have control mechanisms, such as hiding
recommendations, correcting preferences, or turning off certain forms of personalisation,
where feasible. Personalised merchandising is most effective when it feels like assistance
rather than surveillance.
2.7 Behavioural targeting across the retail customer
journey
Behavioural targeting should be mapped to the customer journey rather than treated
as an isolated message (Lemon & Verhoef, 2016). A digital retail journey typically
includes awareness, discovery, evaluation, purchase, fulfilment, usage, service, return,
replenishment, and loyalty. Each stage produces signals and contains opportunities for
relevant interventions. Journey mapping helps retailers avoid overconcentrating analytics
on acquisition while neglecting retention, service quality, and post-purchase experience.
It also reveals that targeting can solve customer problems rather than merely pushing
products. At the discovery stage, targeting helps customers navigate the abundance
of products. A large assortment can create an overload of choices. Search ranking,
category filters, personalised landing pages, and guided selling tools can use behavioural
signals to make discovery easier. For example, a returning customer who often buys
cruelty-free beauty products may see these filters promoted. Visitors using technical
search terms may receive comparison guides. Customers browsing entry-level equipment
may receive educational content. These interventions target behaviour but are framed as
assistance. During evaluation, behavioural targeting can reduce uncertainty. Retailers
can identify signals of hesitation, such as repeated visits to the same product, extensive
review reading, size-guide use, shipping-cost checks, or comparisons across similar items.

Chapter 2. Big Data Analytics and Behavioural Targeting 56
Suitable interventions include fit advice, comparison tables, social proof, stock availability,
delivery estimates, warranty information, and access to live support. Discounts are not
always the appropriate response to hesitation. Sometimes, customers need confidence, not
a lower price. Analytics should distinguish price friction from information friction, where
possible.
Targeting must be especially careful at the basket and checkout stages. Abandoned-
basket emails and exit-intent offers are common; however, if used indiscriminately, they
can train customers to wait for discounts. Better targeting considers customer history,
product margin, inventory, purchase urgency, previous discount response, and potential
irritation. A new customer abandoning due to unexpected delivery costs may require
transparent shipping options. A loyal customer interrupted by a payment failure may
require a service-oriented reminder. A customer repeatedly abandoning high-margin
products may be a limited incentive. The action should match the inferred cause of
abandonment. Post-purchase targeting is often underdeveloped and requires further
research. After purchase, customers need confirmation, delivery visibility, setup guidance,
care instructions, replenishment reminders, and service access. Behavioural data can
identify when a customer may require support. For example, a customer who reads return
policy pages shortly after delivery may be uncertain; a customer who searches for “how
to assemble” may need instructions; and a grocery customer whose regular purchase
cycle is due may appreciate a reminder. These interventions can reduce returns, increase
satisfaction, and build loyalty without aggressive selling. Retention targeting focuses
on sustaining relationships. Churn risk models, declining engagement signals, lapsing
purchase cycles, and negative service interactions can trigger retention actions. However,
retention does not simply mean sending discounts to customers who are leaving. The
reasons for disengagement are important. Some customers leave because their needs change,
others because of poor service, stockouts, price perception, irrelevant communication, or a
better competitor offer. Behavioural targeting should diagnose the likely cause and select
responses that preserve value. Apologies, improved services, replenishment convenience,
loyalty recognition, and product education may be more effective than vouchers.
Cross-selling and up-selling are classic targeting objectives, but they require relevance
and timing to be effective. Cross-selling recommends complementary products, whereas
up-selling encourages a higher-value alternative. Both can be helpful when they reflect
customer needs. They become intrusive when they appear to be opportunistic or irrelevant.
A customer buying a printer may benefit from compatible ink recommendations, a customer

Chapter 2. Big Data Analytics and Behavioural Targeting 57
buying a premium laptop may appreciate warranty options, and a customer buying a baby
seat should not be overwhelmed with unrelated promotions. The ethical and commercial
tests are whether the offer improves the customer’s task. Frequency management is critical
throughout the journey. Behavioural signals can trigger many systems simultaneously:
email, app push, advertising retargeting, onsite banners, and service scripts. Without
coordination, customers experience repetition. A central contact policy should define
eligibility, suppression, frequency caps, channel preferences, and priority rules. A customer
who has just complained should not receive a celebratory cross-sell offer. A customer
who opted out of email should not be targeted through a workaround that violates their
expectations. Journey orchestration requires both technology and policies. The customer
journey is not linear in nature. A customer may discover on social media, evaluate on
mobile, purchase on desktop, collect in store, return by post, and later seek support through
chat. Behavioural targeting must account for this omnichannel reality. Offline events such
as store purchases, returns, and service interactions should inform digital targeting where
lawful and feasible. Similarly, digital behaviour can support store associates, such as
showing wish-list items or loyalty preferences to them. The aim is a coherent relationship,
not a collection of channel-specific tactics. Behavioural targeting should also include
suppression. Not showing a message can be as valuable as showing one. Suppression may
apply when a customer has already purchased, when stock is unavailable, when contact
frequency is high, when the model is uncertain, when a customer is vulnerable, when
consent is absent, or when a product is inappropriate. Suppression is a sign of maturity
because it recognises that relevance includes restraint. A retailer that knows when not to
target the consumer protects their attention and trust.
Awareness Discovery Evaluation Purchase
Retention Replenishment Service Fulfilment
Targeted interventions: assistance, confidence building,
recovery, replenishment, and loyalty
Figure 2.6:Journey-based behavioural targeting map
Figure 2.6 explains how each stage of the customer journey produces different data signals
and therefore requires different interventions, from discovery assistance to service recovery,

Chapter 2. Big Data Analytics and Behavioural Targeting 58
replenishment and retention.
2.8 Measurement, experimentation and attribution
The performance of behavioural targeting cannot be judged by activity metrics alone. Im-
pressions, opens, clicks, and views indicate exposure or engagement, but they do not prove
that the intervention created value. A customer may click on a recommendation and still
buy something they would have bought anyway. An abandoned-basket email may generate
revenue but merely captures purchases that are already imminent. Retargeting campaigns
may claim credit for sales driven by brand demand. Therefore, the measurement must
distinguish the observed response from the incremental impact. Controlled experiments
are the most effective method for estimating incremental impacts (Varian, 2014). In
a randomised A/B test, eligible customers or sessions are assigned to treatment and
control groups. The treatment group receives the targeted intervention, and the control
group receives either no intervention or an alternative. Randomisation helps ensure that
differences in outcomes are caused by the intervention rather than pre-existing differences
among customers. Experiments can test recommendation algorithms, message timing,
incentive levels, search ranking changes, checkout prompts, and onboarding journeys. The
experimental design requires careful consideration. The unit of randomisation should
match the decision. If the intervention affects a session, randomise sessions; if it affects
the customer relationship, randomise customers. Tests should have a sufficient sample
size, clear primary metrics, guardrail metrics, and a predefined duration. Guardrails
protect against narrow optimisations. For example, a discount test may use conversion as
a primary metric but monitor margin, returns, and unsubscribes. A recommendation test
may monitor revenue, product diversity, return rate, and page speed. Without guardrails,
a test may declare victory while damaging other results. Holdout groups are useful for
ongoing targeting programs. A retailer can exclude a small, representative group from a
campaign or decision-making system to estimate the long-term incremental value. This
is especially important for lifecycle marketing and personalisation, where interventions
occur repeatedly. Holdouts help answer whether a program creates value beyond natural
customer behaviour. They also provide data for uplift modelling. The commercial sacrifice
of withholding treatment from a small group can be justified by the learning it produces.
Attribution attempts to assign credit for outcomes across the touchpoints (Wedel &
Kannan, 2016). In digital retail, customers may see search ads, social posts, emails,
push notifications, display retargeting, affiliate links, and onsite recommendations before

Chapter 2. Big Data Analytics and Behavioural Targeting 59
making a purchase. Last-click attribution gives all credit to the final touchpoint, which is
simple but often misleading. First-click attribution emphasises acquisition but ignores
later influence. Multi-touch attribution distributes credit, but the allocation rules may be
arbitrary unless they are supported by causal methods. Retailers should treat attribution
reports as decision aids, not as objective truths. Incrementality testing is especially
important for paid media retargeting. Retargeting often reaches people who have already
shown strong intent, making it easy to overestimate the impact. Geo experiments, audience
holdouts, and conversion lift studies can estimate whether advertising changed behaviour.
The results may show that some retargeting is valuable, some is wasteful, and some irritates
customers. This nuance is essential to this study. The goal is not to abandon targeting
but to allocate spending where it creates incremental profit and to suppress exposures that
do not. Customer lifetime metrics are needed because behavioural targeting can shift the
outcomes over time. A promotion may increase today’s conversion while training customers
to wait for discounts. Aggressive emails may raise short-term revenue while increasing
unsubscribes and reducing trust. Personalised service may cost more in the short term
but improves retention. Therefore, retailers should track long-term metrics, such as repeat
purchases, margin after returns, retention, complaints, satisfaction, opt-out rates, contact
fatigue, and lifetime value. The measurement horizon should reflect strategic objectives.
Qualitative evidence complements quantitative measurements. Customer interviews,
usability tests, complaint analysis, and service transcripts reveal why interventions succeed
or fail. A test may show that a checkout prompt reduces abandonment, but qualitative
research may explain that customers are confused by delivery fees. A recommendation
model may underperform because customers do not understand why items are suggested
to them. Combining behavioural data with customer voice prevents analytics teams
from mistaking correlation for understanding. Measurement governance ensures that
teams do not cherry-pick metrics. Before launch, each targeting initiative should have a
measurement plan defining the hypothesis, eligible audience, treatment, control, primary
metric, guardrails, analysis method, decision rule, and owner. After launch, the results
should be documented, whether positive or negative. Learning from failed tests is valuable
because it prevents the repetition of mistakes. A mature experimental culture rewards
disciplined learning, not only successful outcomes.

Chapter 2. Big Data Analytics and Behavioural Targeting 60
2.9 Privacy, fairness and responsible behavioural tar-
geting
Privacy is central to behavioural targeting because this practice depends on observing,
linking, and interpreting customer behaviour. Customers may accept data use when it is
transparent, proportionate, and beneficial. They may object when it is hidden, excessive,
unexpected, or difficult to control. Therefore, the legitimacy of behavioural targeting
depends on more than just legal compliance. It depends on the retailer’s ability to explain
why data are collected, how they are used, how long they are retained, who receives
them, and what choices customers have. Data protection principles provide a practical
framework for this (European Commission, n.d.-a). Lawfulness, fairness, and transparency
require a clear basis for processing and understandable communication. Purpose limitation
requires data to be used for specified purposes rather than being endlessly repurposed.
Data minimisation requires collecting what is needed, not everything that is technically
available. Accuracy is important because incorrect data can lead to unfair treatment.
Storage limitations reduce unnecessary retention. Integrity and confidentiality require
security measures. Accountability requires evidence that these principles have been
implemented. These principles should shape the system design from the beginning, rather
than being applied as a late-stage legal review.
Consent management is a visible element of privacy governance; however, consent alone
does not solve all issues. Customers often face complex notices and may not understand
downstream modelling. Retailers should avoid treating consent as blanket permission
to do anything. Preferences should be granular, where feasible, and withdrawals should
be respected across systems. If a customer opts out of personalised advertising, the
signal must propagate to the activation platforms, data pipelines, and decision engines.
Broken consent propagation is both a compliance risk and trust failure. The distinction
between personalisation and manipulation is important. Personalisation helps customers
achieve their goals, while manipulation steers customers through asymmetric information,
pressure, or exploitation of vulnerability. Dark patterns, scarcity pressure, confusing
consent interfaces, and excessive urgency cues can convert targeting into manipulation
(European Commission, n.d.-b; Zuboff, 2019). Behavioural analytics can identify when
customers are impulsive, anxious, inexperienced, or financially stressed. Responsible
retailers should use such knowledge to protect their customers rather than exploit them.
This may require suppressing certain offers, limiting credit prompts, or reviewing targeting
for vulnerable groups.

Chapter 2. Big Data Analytics and Behavioural Targeting 61
Fairness is another core issue in this regard. Behavioural targeting can allocate opportuni-
ties unevenly. Some customers may receive better prices, faster service, richer offers, or
more favourable recommendations than others. Differentiation is not automatically unfair;
loyalty programs and targeted promotions are longstanding retail practices. Concerns arise
when differentiation is opaque, based on sensitive or proxy attributes, or systematically
disadvantages protected or vulnerable groups. A fairness review should examine both
inputs and outcomes (National Institute of Standards and Technology, 2023). A model that
excludes sensitive attributes may still reproduce bias through correlated variables such as
postcodes, device types, or purchase histories. Algorithmic explainability supports fairness
and accountability in AI. Retailers should be able to describe the purpose of a model, the
data used, the main factors influencing decisions, the intended action, the monitoring
process, and the escalation route for concerns. Documentation, such as model cards, data
sheets, impact assessments, and decision logs, can make this practical. Explainability
should be tailored to the audience. A data scientist needs technical details; a marketing
manager needs decision logic; and a customer needs a plain-language explanation and
control.
Figure 2.7 explains the governance controls that should surround behavioural targeting,
including clear purpose, consent, minimisation, fairness review, security, measurement,
accountability and customer control.
Security is inseparable from behavioural targeting. Customer behavioural data can
reveal habits, locations, preferences, household circumstances, and financial patterns.
Therefore, breaches can cause harm beyond payment fraud. Retailers should apply access
controls, encryption, retention limits, monitoring, vendor due diligence, and incident
response. Data should be classified according to sensitivity, and access should follow
the principle of least privilege. Analysts do not need unrestricted access to identifiable
records when aggregated or pseudonymized data would suffice. Regulatory developments
increasingly address targeted advertising, platform transparency, and AI governance
(European Commission, n.d.-b; European Commission, 2024). In the European context,
the General Data Protection Regulation provides broad principles for personal data
processing, the Digital Services Act includes restrictions on certain forms of targeted
advertising, andtheAIActcreatesrisk-basedobligationsforAIsystems. Theseframeworks
differ in scope, but they signal a common direction: organisations must be able to justify
data use, manage risks, and respect fundamental rights. Retailers operating across
jurisdictions should design governance for the highest reasonable standard, rather than

Chapter 2. Big Data Analytics and Behavioural Targeting 62
Figure 2.7:Responsible-targeting governance framework

Chapter 2. Big Data Analytics and Behavioural Targeting 63
the weakest local minimum.
Responsible behavioural targeting also requires organisational verification. A privacy
review board, data ethics committee, or cross-functional governance forum can evaluate
high-risk use cases. The forum should include marketing, analytics, legal, security, product,
customer experience, and operations. The purpose, data sources, customer expectations,
benefits, risks, mitigations, measurements, and escalation should be reviewed. Governance
should not be a bureaucratic theatre. This should help teams make better decisions earlier
and avoid costly rework after launch. One practical tool is a targeted impact assessment
(National Institute of Standards and Technology, 2023). Before deploying a behavioural
targeting use case, the team documents the customer problem, business objective, data
used, lawful basis or permission status, model logic, sensitive inferences, potential harms,
fairness checks, opt-out mechanisms, retention, security, measurement plan, and review
date. The assessment does not need to be lengthy for low-risk use cases, but it should be
proportionate to the risk. A simple replenishment reminder requires less scrutiny than
a model that infers financial vulnerability or health-related interests. Trust should be
treated as an asset. A retailer may be able to increase short-term conversion through
aggressive targeting; however, if customers feel watched or pressured, they may reduce
engagement, opt out, complain, or switch. Trust is built when personalisation is useful,
explainable, restrained, and easy to control. It is damaged when the targeting is surprising,
persistent, or inconsistent with the customer’s understanding of the relationship. The
most sustainable behavioural targeting strategies are those that make the customer feel
recognised and not exposed.
2.10 Organisational capability and implementation
roadmap
Implementing behavioural targeting is not simply a technology procurement project
(Davenport, 2006). It requires an operating model that integrates data engineering,
analytics, marketing, merchandising, product management, customer experience, legal,
security, and operations. Many retailers buy tools before defining the decisions that
those tools will improve. The result is underused platforms, inconsistent campaigns,
and fragmented data. A better approach starts with business questions, prioritises use
cases, builds reusable capabilities, and establishes governance from the outset. The
first stage is use case prioritisation. Candidate use cases should be assessed against

Chapter 2. Big Data Analytics and Behavioural Targeting 64
customer value, commercial value, data readiness, operational feasibility, risk, and time to
impact. Examples include personalised search, abandoned-basket recovery, replenishment
reminders, churn prevention, product recommendations, size guidance, service recovery,
next-best-action in contact centres, and loyalty onboarding. A high-priority use case is
not necessarily the most advanced. Data are available, the action is clear, the customer
benefit is credible, and the impact can be measured.
The second stage is data readiness. Teams should map the required data sources, evaluate
their quality, identify missing fields, confirm consent, and define key entities such as
customer, product, order, and session. Data readiness often reveals foundational issues,
such as inconsistent product taxonomies, missing campaign tags, duplicate customer
records, delayed returns data, or incomplete opt-out propagation. These issues should be
addressed as part of a roadmap. Behavioural targeting cannot be reliable if the underlying
data are unstable. The third stage is the decision design. For each use case, the team
should define the eligible audience, trigger, decision logic, action, channel, frequency limits,
exclusions, customer controls, and success metrics. This stage prevents the common error
of building a model without knowing how the score will be used. A churn model is not
useful until the retailer defines the following: what action will be taken for high-risk
customers, which customers should be excluded, how costs will be controlled, and how
success will be measured. Decision design connects analytics and operations.
The fourth stage is pilot deployment. Pilots should be narrow enough to manage risk but
broad enough to produce valid results. A retailer might test personalised recommendations
in one category, replenishment reminders for one consumable product group, or service
recoverytargetingaspecificfailuremode. Pilotsshouldincludecontrolgroups, documented
hypotheses, monitoring, and customer feedback. They should also test operational
processes: who reviews performance, who changes the rules, who approves new features,
and who responds when the system behaves unexpectedly. The fifth stage is scaling the
model. Scaling requires standard patterns for data pipelines, model deployment, feature
reuse, consent enforcement, experimentation, and reporting. Without standardisation,
each use case becomes a bespoke project. Reusable components reduce costs and risks.
For example, a unified identity layer, product attribute service, feature store, decision
API, and experimentation platform can support multiple targeting applications. Scaling
also requires training business users to interpret the model outputs and understand
the limitations. Talent and roles are important factors. Data engineers build reliable
pipelines; analysts explore patterns and design metrics; data scientists develop models;

Chapter 2. Big Data Analytics and Behavioural Targeting 65
machine learning engineers deploy and monitor them; marketers design treatments;
merchandisers provide product and category judgments; legal and privacy specialists
review risks; product managers coordinate delivery; and customer experience teams
interpret qualitative feedback. No single role can own behavioural targeting. Effective
organisations create cross-functional squads aligned with customer journeys or use cases.
Governance should include model lifecycle management as well. Each model should
have an owner, purpose, training data description, version history, evaluation metrics,
monitoring plan, retraining schedule, and retirement criteria. Models should not be
run indefinitely without review. A recommendation algorithm developed before a major
change in assortment may become stale. A churn model trained during a crisis period
may overpredict risk. Lifecycle management ensures that models remain aligned with
current behaviours and business strategies. Change management is often underestimated.
Behavioural targeting alters decision-making. Merchandisers may worry that algorithms
reduce their control; marketers may need to shift from campaign calendars to trigger-based
orchestration; service teams may need to trust next-best-action recommendations; and
executives may need to accept experimentation results that challenge intuition. Successful
implementation includes communication, training, transparent performance reporting,
and clear escalation. Analytics should augment retail expertise rather than dismiss it.
A practical roadmap usually moves from the foundation to sophistication. Early work
focused on data quality, consent, descriptive analytics, and simple trigger-based use
cases. The next stage introduces propensity models, recommendations, experimentation,
and journey orchestration. More advanced stages include uplift modelling, real-time
decision-making, dynamic creative optimisation, multi-objective optimisation, and privacy-
preserving analytics. Retailers should not skip the foundations. Advanced techniques
based on weak data and governance create fragile systems.
2.11 Case vignette: NovaMart’s behavioural target-
ing programme
Consider NovaMart, a fictional omnichannel retailer selling home, beauty, and lifestyle
products. NovaMart has a strong loyalty program and growing e-commerce traffic, but its
digital experience is generic. Email campaigns are planned by category teams, the website
shows the same homepage to most visitors, paid retargeting continues after purchase,
and customer service data are not used in marketing suppression. Senior managers

Chapter 2. Big Data Analytics and Behavioural Targeting 66
want to increase digital revenue, but customer complaints about irrelevant messages are
increasing. The organisation decides to build a behavioural targeting programme focused
on usefulness and restraint.The first step is to define use cases. NovaMart rejects the
vague goal of “more personalisation” and selects three pilots: replenishment reminders
for consumable beauty products, personalised category recommendations for logged-in
customers, and service recovery suppression for customers with recent delivery failures.
These use cases were chosen because they have clear customer value, available data,
and measurable outcomes. Replenishment reminders help customers avoid running out
of products; category recommendations reduce browsing effort; and service recovery
suppression prevents insensitive promotional messages after a negative experience. Data
mapping revealed several issues. Product data include inconsistent pack size attributes,
making replenishment timing difficult. Customer identity is fragmented between online
accounts and loyalty cards. Delivery complaints are stored on the service platform and
are not connected to marketing tools. Consent preferences are captured but are updated
nightly, which is too slow for real-time suppression. NovaMart creates a small data
readiness backlog: standardise product attributes, improve identity matching for logged-in
loyalty customers, stream service failure flags to the decision engine and update consent
signals more frequently.
For the replenishment pilot, analysts estimate the typical repurchase intervals by product
and customer. The model considers the purchase date, quantity, pack size, prior repurchase
patterns, and category norms. The decision rules exclude customers who returned items,
opted out of emails, recently complained, or repurchased items. The message is framed as
a reminder rather than a pressure tactic: “You may be running low soon.” Customers can
adjust the reminder frequency or turn it off. The primary metric is incremental repurchase;
guardrails include the unsubscribe rate, complaints, and margin after promotions. For
personalised category recommendations, NovaMart uses a hybrid approach. Collaborative
signals identify products that are often purchased together, whereas content-based signals
use product attributes such as material, scent, colour, and style. Merchandisers set
constraints to avoid recommending incompatible items, low-stock products, or products
with a high return risk. The interface explains recommendations with simple labels such
as “because you bought” or “popular with customers viewing this range.” Customers
can hide items and update their preferences. The pilot runs were conducted in two
categories before expansion. For service recovery suppression, NovaMart creates a rule
that pauses promotional messaging for customers with unresolved delivery failures or open
complaints. Instead of a generic sales email, eligible customers receive service updates or

Chapter 2. Big Data Analytics and Behavioural Targeting 67
apology messages where appropriate. This is a form of behavioural targeting because it
uses behaviour and operational context to decide not to sell data. The commercial team
initially worries about lost sales, but the pilot measures complaint resolution, subsequent
purchases, and opt-out behaviour. The results show that restraint improves satisfaction
and does not significantly reduce long-term revenue.
NovaMart’s measurement plan includes randomised controls for the replenishment and
recommendation pilots, plus a holdout group for the service suppression program. The
team reports not only revenue but also margin, repeat purchases, return rates, unsubscribes,
and customer feedback. Some of the findings challenge these assumptions. Replenishment
reminders perform well for predictable consumables but poorly for discretionary fragrances.
Recommendations increase basket size in home accessories but increase returns in apparel-
like categories, where fit and colour perception matter. These results lead to refinement,
rather than abandonment. The governance process is lightweight but real-time. Each pilot
has a targeted impact assessment, documenting data sources, customer benefits, consent
status, risks, exclusions, and metrics. A cross-functional group reviews the results monthly.
When analysts propose a model to infer “financial stress” from payment behaviour to
target cheaper alternatives, the group rejects the label as intrusive and reframes the use
case around explicit budget filters and customer-controlled preferences. This decision
protects trust while addressing affordability needs. After six months, NovaMart has not
become fully personalised, but it has developed a repeatable capability. The company has
improved product data, connected service signals, established experimentation practices,
and trained marketers to think in terms of triggers, exclusions, and incremental impact.
The lesson is that behavioural targeting maturity emerges through disciplined choice.
NovaMart succeeds not because it collects every possible signal but because it connects
selected signals to useful actions, measures outcomes, and respects boundaries.
2.12 Future directions in digital retail analytics
Digital retail analytics will continue to evolve as data sources, computational methods,
consumer expectations, and regulations change. Several directions are particularly signifi-
cant. The first is the move from channel personalisation to journey-level orchestration:
Retailers increasingly need systems that coordinate across email, app, web, marketplace,
store, and service interactions. This requires unified decision-making, real-time context,
suppression logic, and measurement across touchpoints. A retailer that optimises each
channel separately may create local gains but global incoherence. The second direction is

Chapter 2. Big Data Analytics and Behavioural Targeting 68
the use of generative and conversational AI in retail (Shankar, 2018; National Institute of
Standards and Technology, 2023). Chatbots, shopping assistants, content generation tools,
and automated product copy can make discovery more conversational. However, these
systems require careful grounding in product facts, inventory, policies, and customer per-
missions. A conversational assistant that invents product capabilities or ignores the returns
policy can quickly damage trust. Behavioural data may help such systems understand
context, but governance must ensure accuracy, transparency, and appropriate escalation
to human support. The third direction is privacy-preserving analysis. Techniques such
as pseudonymisation, clean rooms, aggregated reporting, differential privacy, federated
learning, and secure data collaboration are increasingly relevant as retailers seek insights
without unnecessary exposure to identifiable data. These methods do not eliminate all
risks and are not substitutes for purpose limitation, but they can support more responsible
data collaboration. For example, a retailer and media partner may analyse campaign
impact in a controlled environment without exchanging raw customer-level data.
The fourth direction is multi-objective optimisation (MOO). Future targeting systems
will increasingly balance revenue, margin, customer satisfaction, inventory, fairness, sus-
tainability, service capacity, and trust. This is more complex than maximising clicks,
but it reflects the true nature of retail management. A recommendation that sells excess
inventory may help operations; a fulfilment-aware offer may reduce delivery emissions;
and a fairness constraint may ensure that valuable opportunities are not systematically
withheld from certain groups. The challenge is to make the objectives explicit and govern
the trade-offs. The fifth direction is the greater customer agency (European Commission,
n.d.-a; Zuboff, 2019). Personalisation is more sustainable when customers can influence
it. Preference centres, explainable recommendations, adjustable reminder frequencies,
feedback controls, and data access tools give customers a role in shaping their experience.
This can improve data quality because declared preferences complement behavioural
inference. It also reduces the sense of surveillance by making the targeting process more
participatory. Retailers should treat customers not as passive data sources but as partners.
Therefore, future capabilities will depend on the combination of technical innovation
and institutional maturity. More data and more powerful models do not automatically
produce better retailing. The decisive factors will be clarity of purpose, quality of data,
robustness of measurement, ethical restraint, regulatory awareness, and customer-centred
design. Retailers that thrive will be those that use analytics to make commerce easier,
more relevant, and more trustworthy, rather than merely more intrusive.

Chapter 2. Big Data Analytics and Behavioural Targeting 69
2.13 Conclusion
Big data analytics has transformed digital retail by making customer behaviour observable,
analysable, and actionable at an unprecedented scale. Behavioural targeting applies this
capability to select experiences, offers, recommendations, and services based on what
customers do and what those actions imply. When used well, it reduces friction, improves
relevance, supports retention, and helps retailers allocate resources efficiently. When used
poorly, it becomes noisy, manipulative, unfair, or intrusive. The same data that enable
personalisation can also undermine trust if collected or used without restraint. This
chapter argues that successful behavioural targeting is an enterprise capability rather than
a campaign technique. It requires high-quality data, an integrated architecture, feature
engineering, predictive models, decision rules, activation systems, and measurements.
It also requires governance: consent management, privacy-by-design, fairness review,
security, explainability, and accountability. Retailers must design not only for what can be
predicted but also for what should be done with the prediction. This distinction separates
responsible analytics from mechanical automation. For managers, the practical implication
is to begin with decisions and customer-related problems. The question should not be
“how can we use all this data?” but “which customer experience or retail decision should
improve, what data are necessary, what action will follow, how will impact be measured,
and what boundaries protect trust?” This discipline helps retailers avoid technology-led
personalisation, which produces little value. It also supports cross-functional collaboration
because marketing, merchandising, technology, analytics, operations, and legal teams can
align around specific decisions. For researchers and students, digital retail offers a rich
setting for studying the interaction between data, markets, and society. It shows how
algorithms shape everyday consumption, how measurement changes managerial behaviour,
and how privacy and fairness become operational design questions. Behavioural targeting
is not simply about selling more products. It is about how retailers interpret human
behaviour and how they choose to respond. Therefore, the most important capability may
be judgement: the ability to combine analytical evidence with commercial understanding
and ethical responsibility. The future of digital retail will not be defined by personalisation
alone but by trusted personalisation. Customers will continue to value convenience,
relevance, and recognition, but they will also expect transparency, control, and respect.
Retailers that understand this balance will use big data analytics to build relationships
rather than merely optimising transactions. This is the strategic challenge and opportunity
at the heart of behavioural targeting in digital retail.

Chapter 2. Big Data Analytics and Behavioural Targeting 70
2.14 Managerial checklist for responsible targeting
A useful way to close this chapter is to translate the discussion into a managerial checklist.
The first question is purpose: what customer problem or retail decision is the targeted
initiative intended to improve? A vague promise of personalisation should be replaced
with a specific decision, such as which replenishment reminder to send, which product
to recommend, which service message to prioritise, or which discount to suppress. The
second question is data necessity: which data are genuinely required for that decision, and
can the same result be achieved with less sensitive or less granular information? These
questions prevent analytical ambition from drifting into indiscriminate data collections.
The third question is the actionability. A score, segment, or cluster has limited value unless
it changes an action. Managers should specify the treatment, eligibility rules, exclusions,
contact limits, channel, timing, and fallback options before commissioning complex models.
The fourth question pertains to measurement. Every initiative should define a primary
outcome, guardrail metrics, a control or holdout design where feasible, and a decision rule
for scaling, revising, or stopping the intervention. Without this discipline, behavioural
targeting becomes a stream of plausible activities rather than a learning system. The fifth
question concerns customer legitimacy. Would a reasonable customer understand the use
of their data in this context? Does the intervention feel helpful, or does it feel as if the
retailer is exploiting their hidden knowledge? Are customers given meaningful controls,
and are opt-outs respected in all systems? The sixth question was fairness. Could the
targeting logic systematically exclude, disadvantage, or pressure certain groups? Are
sensitive inferences avoided and proxy variables reviewed? These questions should be
asked before deployment, not after complaints arise. The final question concerns the
operating ownership. Who maintains the data pipeline, monitors model drift, reviews
performance, approves new use cases, handles incidents, and retires ineffective models?
Behavioural targeting is sustainable only when ownership is explicit. Therefore, retailers
should treat each targeting capability as a living product with a roadmap, governance,
user feedback, risk controls, and continuous improvement. This managerial perspective
maintains the connection between technology and commercial value and customer trust.

Chapter 2. Big Data Analytics and Behavioural Targeting 71
References
Chen, H., Chiang, R. H. L., & Storey, V. C. (2012). Business intelligence and
analytics: From big data to big impact.MIS Quarterly, 36(4), 1165–1188.
Davenport, T. H. (2006). Competing on analytics.Harvard Business Review, 84(1),
98–107.
European Commission. (2024, August 1).AI Act enters into force.
European Commission. (n.d.-b).The Digital Services Act: Rules on ad transparency,
sensitive data targeting, and dark patterns.
European Commission. (n.d.-a).Data protection explained: Principles of personal data
processing under the GDPR.
Fader, P. (2012).Customer centricity: Focus on the right customers for strategic advantage.
Wharton Digital Press.
Kitchin, R. (2014).The data revolution: Big data, open data, data infrastructures and
their consequences. SAGE.
Lemon, K. N., & Verhoef, P. C. (2016). Understanding customer experience throughout
the customer journey.Journal of Marketing, 80(6), 69–96.
National Institute of Standards and Technology. (2023).Artificial intelligence risk
management framework (AI RMF 1.0)(NIST AI 100-1). https://doi.org/10.6028/NI
ST.AI.100-1
Provost, F., & Fawcett, T. (2013).Data science for business. O’Reilly Media.
Shankar, V. (2018). How artificial intelligence is reshaping retailing.Journal of Retailing,
94(4), vi–xi.
Varian, H. R. (2014). Big data: New tricks for econometrics.Journal of Economic
Perspectives, 28(2), 3–28.
Wedel, M., & Kannan, P. K. (2016). Marketing analytics for data-rich environments.
Journal of Marketing, 80(6), 97–121.
Zuboff, S. (2019).The age of surveillance capitalism. PublicAffairs.
