---
title: 'AI Strategy: How to Choose What AI Product to Implement'
url: https://arxiv.org/abs/2607.23733
category: digital-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Foster Provost
- Panos Ipeirotis
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.23733
pages: 27
chars: 71600
fetched_at: '2026-11-08T13:21:35+00:00'
kb_version: 1
---

# AI Strategy: How to Choose What AI Product to Implement

AI Strategy: How to Choose What AI Product to Implement
Foster Provost* Panos Ipeirotis†
July 28, 2026
Abstract
Firms struggle to choose AI projects that pay off: two projects can look equally promising to
smart, motivated stakeholders and yet deserve opposite decisions. At the residential real-estate
brokerage Compass, one AI product (Likely-to-Sell recommendations) flagged sales outreach
opportunities and went on to account for nine figures in annual gross commission revenue.
Another championed AI product (a Time-on-Market pricing tool) was rightly shelved. A sim-
ple ROI estimate could not distinguish the two. We present expected ROI (eROI), a framework
that decomposes each bet into three components and rates them separately:Value if Success-
ful,Likelihood of Success, andInvestment Required. Each maps to a question executives
can answer before building: How valuable would it be if it worked? How likely is it to work?
And what would it cost to implement? Separating the three breaks a common catch-22: teams
cannot estimate ROI until they know whether a project will work, yet cannot know whether it
will work without building it. Judging Value if Successful on its own dissolves the loop, letting
a team argue that a product would be valuable if it worked while it weighs how likely that is.
The framework also asks, before ranking anything, whether there are enough good ideas on
the table. After ranking, it guides assembling a portfolio of bets rather than funding only the
single top-ranked project. We illustrate eROI on Compass’s candidate AI products. Precise ROI
estimates are hard to make given the inherent uncertainty of AI projects. Coarse business-level
ratings of the three components are enough to tell strong bets from weak ones.
Keywords:AI strategy, expected ROI, AI investment, data science, machine learning, portfolio
management
1 Introduction
In 2019, the residential real-estate brokerage Compass had assembled a strong AI team and needed
to decide what AI products to implement. The company identified scores of potentially value-
adding applications and had to choose where to invest. Two candidates looked comparably at-
tractive to its business, product, and engineering leaders. One, a system that flagged which of an
*Stern School of Business, New York University. Email:fprovost@stern.nyu.edu. ORCID: 0000-0002-0307-3884
†Stern School of Business, New York University. Email:panos@stern.nyu.edu. ORCID: 0000-0002-2966-7402
1
arXiv:2607.23733v1  [cs.CY]  26 Jul 2026

agent’s contacts were most likely to sell their homes (Likely-to-Sell recommendations), was im-
plemented and grew into a lasting revenue contributor. The other, a tool that predicted how long
a home would sit on the market at a given asking price (a Time-on-Market pricing tool), was set
aside. Smart, motivated people championed both, and the simple ROI estimate companies usu-
ally demand could not tell them apart: two bets that looked equally worth making, yet deserved
opposite decisions.
The puzzle is not unique to Compass, and getting it wrong is expensive. A RAND study found
that more than 80% of AI projects fail, twice the rate of non-AI IT projects, often because teams
aim AI at targets that are simply too hard [1]. Generative AI (GenAI) has not broken the pattern:
one widely cited industry analysis estimated that roughly 95% of enterprise GenAI pilots deliver
no measurable business impact [2]. That headline figure has been debated on methodological
grounds, but it is directionally consistent with reports that companies are scrapping AI initiatives
at rising rates [3] and that even firms reporting strong returns expect few of their experiments to
reach production soon [4]. Some of this risk is inherent to “science-based” products (we don’t
know in advance whether they will work), but much of it traces to a more avoidable cause: poor
choices about what to pursue in the first place.
The eROI framework provides a systematic way to rank candidates bylikelyreturn on investment,
rather than by visibility or fashion or first-come-first-served. Its core move is to refuse to collapse
a bet into a single ROI figure and instead decompose it into three components rated separately:
Value if Successful,Likelihood of Success, andInvestment Required. Each maps to a question
executives can answer before committing:How valuable would the product be if it worked? How likely
is it to work? And what would it cost to implement?Firms have lacked such structure, and recent work
has begun to supply it, converging on a theme: organizations need structured ways to evaluate AI
investments in business terms. Kim et al. [5] argue that companies must get the “strategy-value-
AI” sequence right, starting with a compelling strategy and identifying a leap in buyer value
before deploying AI as a tool. Valentine et al. [6] presses for a shift from ad hoc experimentation to
enterprise-aligned efforts with measurable outcomes. Siegel [7] warns that most AI projects report
only technical metrics (precision, recall) rather than business metrics (profit, ROI), which often
kills projects that could otherwise succeed. An MIT SMR executive guide compiles practitioner
playbooks for extracting business value from generative AI rather than adopting it for its own
sake [8]. This work establishes the goal; what it leaves open is the mechanism for choosing among
bets.
Keeping the three components apart resolves a common catch-22: a team cannot estimate ROI un-
til it knows whether the project will work, yet cannot know whether it will work without building
it. Judging the components one at a time dissolves the loop. And of the three, one usually decides
the outcome. What sinks most AI projects is not whether a working product would be valuable
or affordable, but whether it can be built at all: whether an AI accurate enough for the application
is even achievable. This is the scientific uncertainty behind the “science-based” products of our
2

opening, the risk we cannot resolve in advance without doing the work. Rating that likelihood
on its own lets a team weigh the bet before committing to it. Precise numbers are rarely neces-
sary: coarse ratings, for example Low, Medium, High, or Very High on each component, carry
enough information to rank projects and build confidence in the choice. Each component can be
subdivided when an assessment needs it.
Before ranking anything, the framework asks whether there are enough good ideas on the table
at all: a firm that has not enumerated widely may hold no likely winner in its consideration set,
a lapse cheap to fix but fatal when skipped. In our experience the opposite problem is more
common: work with experienced AI professionals to enumerate widely, and the set of value-
adding ideas soon grows too large to fund.
We illustrate the framework on the candidate AI products of Compass, the brokerage from our
opening example: the two bets above and a third, a generative-AI tool for producing renovation
visualizations of listings. Compass is especially instructive because we can examine both the
choices made in 2019 and what happened in the years since, including one product later credited
with nine figures in annual gross commission revenue [9]. The case is rooted in residential real
estate, but the principles are not: any organization that must choose what AI projects to invest
in faces the same prioritization problem, and the same framework applies. We actually used the
framework to help prioritize Compass’s AI investments at the time, so the 2019 cases reflect it
in use rather than a post hoc reconstruction. Because we were among the decision-makers and
write with hindsight, we offer all three to show how the framework organizes such choices, not
as an independent test of its predictive accuracy. The next section presents the eROI framework
and relates it to existing methods; we then turn it into an organizational process for building a
portfolio, and work all three Compass projects through it.
2 The eROI Framework
The eROI framework breaks expected return on investment into three components: thevaluea
project would create if it succeeded, thelikelihoodthat it does, and theinvestmentit requires. Esti-
mating the three separately, rather than collapsing them into a single ROI number, is the frame-
work’s central move, and it pays off before any number is computed.
Keeping the components separate defuses the same catch-22 where funding is on the line: teams
must claim substantial potential ROI to secure it. Holding value apart from likelihood lets a team
argue that a project would deliver high ROIif successful, and assess its probability of success on
its own terms. If there is too much uncertainty for the likelihood of success to be rated as High,
the team can propose a variety of small investments (R&D studies, proofs of concept, pilots) to
reduce the uncertainty. Framing the components in business terms rather than technical terms
also addresses a failure mode Siegel [7] identifies: teams that judge projects by precision and
recall rather than profit and revenue leave executives unable to tell whether an investment is
3

Value if
Successful
Strategic
Alignment
Direct Value
Option Value
Understanding
Value
Likelihood
of Success
Product
Certainty
T echnical
Certainty
Data
Certainty
Scientific
Certainty
Investment
Required
T eam Effort
Data Assets
Integration
Expected ROI
(eROI)
Assessment
Figure 1: The architecture of the eROI framework. Expected ROI is decomposed into three pillars
(Value if Successful, Likelihood of Success, and Investment Required). Each pillar has several
distinct sub-dimensions. By isolating the scientific certainty that an accurate-enough model can
be built at all from ultimate business value, organizations can compare diverse AI initiatives on
the same terms.
worthwhile.
The separation helps in a second way: many stakeholders do not naturally reason in terms of ex-
pectations (returns weighted by probabilities), and the decomposition lets them deliberate clearly
about how to estimate each component and how it should bear on the decision.
These three components combine as:
eROI∝ Value if Successful×Likelihood of Success Investment Required (1)
We write it with a proportionality sign rather than an equals sign to signal that a project can be
attractive in more than one way. A project is worth pursuing when a large payoff is both likely
and cheap to chase. But a quick win may also be attractive: perhaps lower value if successful,
yet very likely to succeed and requiring little investment. So may a moonshot:veryhigh value
if successful, but perhaps high investment and low-to-moderate likelihood of success. We will
discuss how to deal with lower likelihoods of success later.
Figure 1 illustrates the architecture of the framework. Each of the three components, thepillarsof
the framework, breaks down into sub-dimensions, allowing teams to pinpoint where a project is
strong or weak rather than relying on a single gut-feeling estimate.
The proportionality sign carries a second message: we usually need not compute the precise quan-
tity in Equation 1. We have found that ordinal ratings often present an even more compelling case
than a single estimated ROI. We rate each component on a coarse scale (Low, Medium, High, or
Very High) and judge projects by theirprofilesacross the sub-dimensions; the final prioritization is
4

a judgment call by the stakeholders, informed by the full profile rather than a mechanical average
of it. For example, we usually need to draw in additional strategic and managerial considerations
to decide how to prioritize a quick win versus a more substantial potential blockbuster.
The sections that follow take each pillar in turn, examining the sub-dimensions a team should
weigh.
2.1 Component 1: Value if Successful
Value has several distinct dimensions. Focusing too narrowly on direct product value can cause
organizations to miss the option value and understanding value a project can create.
Strategic Alignment.Before assessing any other dimension of value, we must ask: how will this
project help the company achieve its strategic goals? Alignment is the first filter. If a project’s
strategic fit takes long explanations to justify, or its benefits are too indirect, we should question
whether it is the right investment. This is more than good hygiene: firms that capture value from
AI draw most of it from core business functions [10]. Strategic fit and realized value tend to move
together.
Direct Product Value.This is the business benefit the AI product delivers to customers or the or-
ganization. For revenue-enhancing products this is normally an estimate of the steady-state profit
the product or service will produce. For cost-reduction products we need to consider the net cost
reduction, and think end-to-end. By analogy with Amdahl’s law [11] (which holds that speeding
up one stage of a process improves the whole only as much as that stage’s share of the total), au-
tomating a single step lifts the overall workflow only in proportion to how much of it that step
governs. In addition, many AI cost-reduction solutions require business process reengineering,
including new roles for employees (for example, verifying the accuracy of AI-generated content).
The cost of the reengineering would be part of the Investment component of the eROI. But the
ongoing cost of the new roles detracts from the net cost reduction.
Option Value.Option value comprises the future opportunities a project opens up. AI projects
frequently carry such value, because the work done preparing for the project creates assets that
can be used for other purposes as well. It is not unusual for option value to exceed direct product
value [12].
Two dimensions deserve attention:
•Data Asset Value:AI projects typically create, extend, or refine data assets. Once built, those as-
sets open up options for other products and services that were previously unavailable, offering
value far beyond the specific product at hand.
5

•AI Platform Value:When taking a platform approach, every data-science component can sup-
port multiple products, so a component’s value extends beyond its first application to every
other product or service it later enables.
Understanding Value.Data science can sharpen understanding of the business: testing hypothe-
ses about what drives outcomes and surfacing patterns no one anticipated. Such insight does not
always translate immediately into product value, but often yields strategic advantage and new op-
portunities. Unlike option value, which lives in reusable data and platformassets, understanding
value lives inknowledgethat shapes strategy even when it is never shipped.
Assessing the value if successful forces one more choice, and it sets up the next component. What
level of success are we arguing for? Do we claim the product will be wildly successful, or would
a more measured level of success serve better? The choice matters because it sets the bar for
the likelihood of success: a wildly successful product is less likely than a moderately successful
one. We have found a sweet spot: the minimum (reasonable) level of success that is nonetheless
compelling to the business. The case studies below put this to work.
2.2 Component 2: Likelihood of Success
The main reason AI strategy is difficult is that AI projects face far higher uncertainty than the
projects decision-makers typically have experience with.
That uncertainty has at least four sources, and we must weigh each. Two conventions govern
how the four combine into the overall likelihood-of-success estimate. First, likelihood isgated
by its weakest necessary condition: each of the four sources is necessary, so a single source of
high uncertainty caps the overall likelihood even when the others show relative certainty, and any
further weak source only lowers the estimate. Second, we rate each source not by its uncertainty
but by its complementarycertainty, on the same Low-to-Very-High scale, so that, as with value, a
higher rating is more favorable.
Product Certainty.Would the product realize its envisioned value if we built it? Would cus-
tomers use it and find it valuable? AI-specific product risks involving trust, safety, and compli-
ance live here, alongside more familiar product uncertainty factors. A system that raises fairness,
privacy, or regulatory concerns, or that users simply do not trust, may fail to win adoption or
approval even when it performs as designed, which lowers product certainty.
Technical Certainty.Can we build the product cost-effectively with available engineering re-
sources and infrastructure? Technical uncertainty should be familiar to a firm that regularly im-
plements technical products and services. AI products bring additional technical uncertainty, es-
pecially to firms with little experience in AI algorithms, architectures, and DevOps (“MLOps”).
6

Data Certainty.Do we have the data necessary to build the scientific solution? Is the data quality
sufficient? Do we clearly understand the target of the AI inference? Are we dealing with proxies
rather than direct measures? A well-known key to success with AI projects is getting the data
right.
Scientific Certainty.How likely are we to achieve a sufficient level of accuracy with the AI so-
lution for the project to be successful? All AI systems make mistakes. Will the cost of the errors
render the product useless? This is the “can we even do this in the first place, and how well?”
dimension that distinguishes AI from many other product investments. Do we have compelling
hints from initial exploratory data analysis or pilot studies that a sufficiently accurate model is
feasible? Data certainty asks whether wehavethe right inputs; scientific certainty asks whether,
even with them, the target can be estimated with a low enough error rate.
Two distinct failure modes hide under this one subcomponent. The first is ordinarypredictive
difficulty: even with the right inputs, the pattern may be too weak to estimate to a useful accuracy.
The second is subtler, arising when we are deciding to take actions that will havecausaleffects
(rather than reacting to a pattern we have detected). Evaluating a causal-effect prediction requires
knowing what would have happened otherwise, the counterfactual, which is never observed for
any individual unit [13, 14]. Anaverageeffect across a group can sometimes still be recovered when
the right design is available (an experiment, or a natural experiment that supplies a comparable
control group); absent such a design, observational data alone cannot reveal it. Either way this
adds a layer of complexity in estimation and decision making [15], requiring more complex data
collection and elevated statistical expertise; Section 4.2 returns to it.
With generative AI systems, the predictive difficulty is hidden. The generated responses are pro-
duced by a predictive, machine-learned model. The systems make mistakes just like any AI sys-
tem. However, we tend not to think of the generated result as the model’spredictionof what would
be the best response to the prompt. Because the complex output of the GenAI system results from
many inference runs of the underlying model, 1 the mistakes are much more difficult to identify
automatically. Nonetheless, scientific uncertainty matters just as much. For many tasks, we do
not know in advance whether a GenAI system output will be accurate enough for a satisfactory
product, and how much the errors will cost us (which is needed for an ultimate ROI estimation).
Scientific uncertainty isn’t unique to AI. For example, pharmaceutical firms assess candidate drugs
by their odds of clearing scientific and regulatory hurdles [16, 17]. Nevertheless, scientific uncer-
tainty must be assessed explicitly: it is the extra “can we even do this?” layer on top of the more
typical product and engineering risk.
1For example, the underlying LLM for text generation or de-noising model used in an image diffusion process
7

2.3 Component 3: Investment Required
Investment is the pillar we want low rather than high: it sits in the denominator of Equation 1, so
a smaller commitment raises eROI. Teams that budget only for building the model underestimate
what a project truly costs. The cost goes well beyond the model, and three kinds of investment
matter.
Data Science Team Effort.How large a job is this for the available technical team? Is it a straight-
forward application of established techniques, or does it require research and experimentation?
Data Asset Investment.Do we need to invest in acquiring additional data assets? Can we start
with existing data for version 1.0, or are new data sources essential for success?
Integration and Productization Effort.How much effort is required to integrate the AI capabil-
ity into existing products and workflows? This includes product and UX integration, ML engi-
neering for pipelines and infrastructure, business process reengineering, guardrailing and moni-
toring systems, and potentially more humans in the loop. Applications in sensitive or regulated
domains carry an extra share of this work: legal and compliance review, fairness and privacy safe-
guards, and disclosure or consent mechanisms. This ethical and regulatory exposure can raise
the investment required well above what an R&D effort, prototype, or proof of concept would
suggest.
2.4 Putting Them Together
With the three pillars in hand, two rules govern how the ratings come together. The first con-
cerns how sub-dimensions combine within a pillar, and Value and Likelihood combine in opposite
ways. For Value, the overall rating is aholisticjudgment informed by the sub-dimension ratings
rather than a mechanical sum or average of them: the sub-ratings make the holistic call easier,
not automatic. (Some practitioners prefer instead to sum the sub-scores.) Likelihood works the
other way. As Section 2.2 explains, it isgated: a single Low on any of the four certainties, product,
technical, data, or scientific, caps overall likelihood even when the others are High, and additional
Lows only pull it lower. Investment Required combines as Value does: a holistic judgment over its
sub-dimensions rather than a sum or average, so a single High does not by itself raise the overall
investment rating when the other dimensions are lower.
The second rule concerns one fact bearing on two pillars: it may inform both without being
double-counted, because each pillar scores a distinct conditional question. For example, a cheap
incumbent solution both shrinks theincrementalpayoff (Value) and makes adoption less certain
(Likelihood).
Table 1 gives coarse anchors for the three pillars. Shared anchors help raters converge on similar
8

Table 1: Coarse rating anchors for the three eROI pillars. As noted at Equation 1, the ratings are
ordinal, and a pillar’s overall rating reflects the profile of its sub-dimensions (Figure 1). For Value
and Likelihood a higher rating is more favorable; for Investment Required alowerrating is more
favorable, since a smaller commitment raises eROI.
Low Medium High Very High
Value if
Successful
(higher is
better)
Marginal gain over
the best existing
alternative; narrow
use; little reuse.
Clear benefit to one
product area; some
strategic fit; limited
option value.
Substantial
cross-product
benefit; strong
strategic fit; creates
reusable assets.
Strategy-defining;
large direct value
plus major option
and understanding
value.
Likelihood
of Success
(higher is
better)
Low certainty on
any of the four
sources: a
good-enough
outcome is
speculative.
At least one of the
four sources still
unproven; a pilot is
needed.
High certainty on
all four sources:
well-trodden
approach, few
open risks.
Very high certainty
across all four:
proven on closely
comparable
problems.
Investment
Required
(lower is
better)
Established
techniques,
existing data, light
integration.
Substantial but
well-understood
build; some new
data or integration.
Significant research
or productization;
new data assets;
heavy integration.
Open-ended,
research-grade
build; major new
data assets and
infrastructure.
scores, so that disagreement surfaces hidden assumptions rather than mere optimism.
2.5 How eROI Relates to Existing Methods
eROI adds a decomposition tailored to the distinctive risk of AI, one that does two things a
general-purpose score leaves blended. First, it lets stakeholders discuss cleanly what the prod-
uct would be worth if it succeeded. Second, it isolatesscientificcertainty, distinct from ordinary
engineering risk: whether an accurate-enough AI system can be built, that is, whether the target is
learnable at allto a useful accuracy. Lightweight feature-ranking schemes fold that question into a
single “confidence” rating. The probability-weighted portfolio score folds it into one “probability
of technical success.” Neither surfaces it. A corollary of the same separation: option value, the
data assets and reusable components a project creates, becomes a first-class dimension rather than
a footnote to expected value.
eROI builds that decomposition from familiar ideas. Product teams rank features with lightweight
schemes such as RICE [18] or ICE [19]; finance evaluates staged commitments through real op-
tions [20, 21]; and new-product development screens projects through stage-gate reviews [22], the
staged go/no-go discipline eROI adopts for AI bets. Closest in spirit is the long tradition of R&D
and new-product portfolio management (of which pharmaceutical pipeline valuation is one in-
stance), which ranks uncertain projects by value weighted by the probability of technical success,
together with the broader machinery of decision analysis [23, 24]. eROI specializes that decision-
9

analytic machinery, supplying the structured value, likelihood, and investment dimensions an
analyst would otherwise have to assemble case by case.
A single blended “confidence” or “probability of technical success” score buries what eROI sur-
faces. We show as much below on two Compass cases: the Time-on-Market tool, which turns on
scientific certainty, and the renovation tool, which turns on option value. Both are worked through
in full later.
3 From Framework to Strategy: Guiding Principles
Evaluating individual projects is one thing; applying eROI across an organization requires a delib-
erate process integrating business, product, engineering, and scientific perspectives. That process
has two steps: enumerate candidates widely, then prioritize them into a portfolio.
3.1 Step 1: Enumerate a Large List of Potential AI Projects
This stage pairs knowledge of the business’s challenges and opportunities with knowledge of
what AI can do. Because a company usually has many possible ways to create value with AI,
talk to as many stakeholders as possible: not just founders and executives, but product managers,
engineering managers, and especially customers. Consistent with Kim et al. [5], enumeration
should be driven by business needs and buyer value, not by what the technology can do.
Having too few candidates is a common failure mode. A short list very likely omits great oppor-
tunities, sometimes the best ones. Building the list takes effort but no special expertise: managers
and customers have usually thought hard about how AI might improve their own area of respon-
sibility. If the firm has someone with real experience across AI successes and failures, empower
them as an “internal consultant” to help brainstorm the enumeration. A team that does not enu-
merate widely will not know whether its best opportunities are even on the table, and even a
carefully assembled portfolio of AI investments will then underperform.
Do resist the temptation to limit this exercise to generative AI. Although McKinsey estimates that
generative AI will add $2.6–4.4 trillion in annual value globally, this would increase the total im-
pact of all AI by only 15–40% [25]. The larger, remaining share is where most of AI’s economic
value still sits: analytical AI techniques such as predictive machine learning, causal decision mak-
ing at scale, optimization, and classification. Organizations that focus exclusively on generative
AI may overlook their highest-eROI opportunities.
3.2 Step 2: Prioritize, Then Build a Portfolio
Prioritizing the enumerated list into a funded portfolio does not mean funding the single highest-
ranked project. These are risky investments, so build a portfolio: a deliberate mix of bets beats
10

staking everything on the top-ranked project, because funding then rarely hinges on a single
razor’s-edge ranking.
Building that portfolio starts with rating each candidate across the three pillars. The aim is rating,
not precise calculation: rough ratings suffice, because the eROI analysis is an input to a selection
procedure in which decision-makers layer on criteria it cannot capture. A CEO may weigh the
relative strategic alignment of two projects in ways the analytic team cannot quantify, and fund-
ing and shared resources add constraints of their own: two projects with similar, stellar eROI
may need the same scarce AI team, so the firm funds one alongside other bets whose eROIs are
attractive if not as stellar. Ratings inform the choice; they do not make it.
Comparisons are easiest when one profile dominates another (better or equal on every pillar),
which coarse ratings make common. When profiles instead conflict (one project higher on value,
another lower on investment), eROI generally will not settle the trade: stakeholders must judge
what eROI profile is desired. What the framework supplies is structure for that judgment, keeping
the opposing dimensions explicit rather than burying them in one score.
A good portfolio spans several archetypes:
•Potential big wins(Very High value, High likelihood, Medium investment), the profile of Com-
pass’s Likely-to-Sell recommendations, which we work through in the case study below.
•Quick wins(High value, High likelihood, Low investment).
•Strategic bets(Very High value, Medium likelihood, High investment).
•Research investmentsto reduce uncertainty for potential high-value projects (High value, High
Uncertainty). We say “Uncertainty” rather than “Low likelihood” to stress the difference be-
tween not knowing whether we can do it and being fairly certain that we cannot. Compass’s
Time-on-Market tool is the case below.
For astrategic bet, “High investment” describes the eventual cost profile, not a lump sum com-
mitted up front: when risks remain (Medium likelihood), the first move is a staged commitment,
a pilot or research phase that buys down uncertainty before the firm decides whether to invest
further. Aresearch investmentcan look similar, but for a causal-prediction problem such as the
Time-on-Market tool it is not an ordinary pilot: the research is a hunt for the identifying variation
the prediction needs, and absent that variation the project fails the gate rather than becoming a
funded research bet. We work through both Compass cases below.
This portfolio discipline echoes recent findings on extracting value from generative AI: firms see-
ing early returns pursue “small t” transformations that build capability over time [26] and apply
a cost test, using an LLM only where doing so costs far less than business as usual [27].
Resisting score inflation.Because the ratings inform funding, project champions have an incen-
tive to inflate them, a pressure the original 2019 decisions faced (our retrospective retelling does
11

not) and one any prospective decision maker must manage. A few practices help. Have the pro-
cess run by an independent innovation leader, with a stake in success but not in any particular
product; and have a cross-functional panel (business, product, engineering, and data science) rate
each pillar independently, then reconcile, so no single advocate sets a project’s ratings. Require a
careful, evidence-backed case to unlock the top ratings: aHighorVery Highon Likelihood should
rest on a pilot result, a comparable deployed system, or concrete signals from exploratory analy-
sis, not optimism alone, and a top Value rating should rest on a compelling business case. Treat
divergent scores not as noise to be averaged away but as a prompt to surface the assumptions
behind them. The goal is not numerical precision but a shared, defensible view that survives
cross-examination.
Revisit the portfolio as priorities shift, so promising ideas do not drift to the back of the queue
and strategically stale ones do not stay highly ranked. Selection is not the whole job: returns still
depend on complementary investments, the right data assets, an experienced AI science and en-
gineering team, and AI product management that can ship and operate AI products successfully.
Enumerate widely, prioritize into a portfolio, and defend the ratings that drive it: the case study
that follows shows the framework doing exactly that at Compass.
4 Case Study: Applying eROI at Compass
We illustrate the framework with Compass Inc., a technology-focused residential real-estate bro-
kerage and, by the standards of its industry, an unusually large one: it reported record revenue of
$7.0 billion for 2025 and in January 2026 combined with Anywhere Real Estate [28].2 In the United
States, brokerages represent home buyers and sellers through licensed agents. That scale makes
Compass a useful setting for the framework: a company with the resources to fund many AI bets
and the need to choose among them.
By 2019, Compass was building a platform to support and integrate all of an agent’s activities,
bringing a modern technology perspective to a traditionally technology-light industry, as it pur-
sued its goal of becoming the country’s largest independent brokerage.3
Compass’s Strategy.The company’s strategy centered on helping Compass agentsget more busi-
ness(acquiring more seller or buyer clients) orget more time(to spend with their families or other
priorities). This clear strategic focus became a filter for evaluating AI investments.
2Compass Inc. went public in April 2021; its 2025 revenue came with positive adjusted EBITDA but a small GAAP
net loss. The Anywhere combination was an all-stock deal.
3Two exceptions to the industry’s “technology-light” character: the Multiple Listing Services (MLSs), where agents
post and find listings, and Zillow, which offers a similar consumer platform.
12

AI Areas of Opportunity
Extensive discussions with stakeholders across the organization identified scores of potential AI
products and services, spanning the company’s major product areas:
•Compass.com(consumer and agent website): ranking search results, recommending homes,
home price estimation, image-based search, auto-generation of listing descriptions, data quality
assurance, and more.
•Marketing Center(creating marketing assets for agents): improving targeting of mail cam-
paigns, email and social media optimization, learning what creative approaches work best in
different situations.
•CRM System(managing agent contacts): building relationship graphs, helping agents farm
new leads, identifying which contacts to reach out to, creating maps of likely-to-sell properties.
•Sales Support(helping agents win business): providing sellers with what-if pricing tools, im-
proving listing presentations, providing market intelligence.
The challenge was not finding uses for AI [29]: it was choosing from among many opportunities
that seemed promising on the surface, indeed far more than the company could pursue simulta-
neously.
To illustrate how the framework guides decisions, we next work through three real Compass
cases (not hypotheticals): a funded project that succeeded (Likely-to-Sell recommendations), an
attractive project that turned out not to be a good choice to prioritize (the Time-on-Market pricing
tool), and a generative-AI product (renovation visualizations). Figure 2 previews how each of the
three products scores across every sub-dimension; the following subsections explain the ratings.
4.1 Example 1: Likely-to-Sell Recommendations for CRM Contacts
Residential real-estate agents are in the business of helping consumers buy and sell homes. Much
of their business comes from their networks. However, a typical agent has hundreds or thousands
of contacts and rarely knows whom to reach out to at any particular time. Thus many agents
simply miss getting the business of a contact who puts their home on the market. Likely-to-Sell
(LTS) recommendations point agents to the contacts most likely to sell in the near future and help
them reach out [30].
LTS was one of the top-ranked AI projects in mid-2019, as the company planned its 2020 work; its
eROI profile shows why.
4.1.1 Value if Successful
Strategic Alignment: Very High.The primary goal of LTS recommendations is to increase every
agent’s business: identifying relevant opportunities, nudging agents toward them, and facilitating
13

Likely-to-Sell
Recommendations
Time-on-Market
Pricing Tool
GenAI Renovation
Visualizations
Strategic
Alignment
Direct Product
Value
Option
Value
Understanding
Value
Product
Certainty
T echnical
Certainty
Data
Certainty
Scientific
Certainty
Data Science
T eam Effort
Data Asset
Investment
Integration &
Productization
Very High High Low to Medium
High Medium Low to Medium
High Low Low to Medium
High High Low
High Medium Medium
High High Medium
High Low High
High Low Medium
Medium Very High Medium
Medium Medium Low
Medium High High
Value if
Successful
Likelihood
of Success
Investment
Required
Cell color: how favorable each rating is for expected ROI
Unfavorable Less favorable More favorable Favorable
Each cell shows a project's rating on that dimension. For Investment Required, a lower requirement is more favorable.
Figure 2: The eROI framework applied to three AI projects at Compass. Each cell gives a project’s
rating on one sub-dimension (Low, Medium, High, or Very High); the cell color shows howfa-
vorablethat rating is for expected ROI, from orange (unfavorable) to blue (favorable), so that blue
always indicates higher eROI regardless of the pillar. Because a smaller commitment is better, a
low Investment Required is shown blue. Each cell is also labeled with its rating, so the figure does
not rely on color alone, and the blue–orange scale is colorblind-safe.
outreach. This is directly aligned with Compass’s strategy of helping agents get more business.
Direct Product Value: High.As the framework advises, we anchor on a reasonable, not overblown,
level of success: for LTS, that it adds just one sale per agent per year. As the uncertainties below
show, this is not a trivial bar to clear, but it is far from unreasonable. With the average Compass
listing around $1 million and commission rates averaging approximately 2.5%, each added listing
brings in about $25,000 in additional commission revenue. Across Compass’s at-the-time approx-
imately 20,000 agents,4 that one extra sale apiece implies around $20 billion in additional annual
real-estate transaction volume and roughly half a billion dollars of additional commissions (such
commissions are Compass’s top-line revenue, split between the agent and the brokerage).
4Compass’s approximate total agent count (including agents who are team members) during the case-study period,
larger than the “principal agents” figure in its financial reporting.
14

Option Value: High.The models built for the LTS product help far beyond CRM recommen-
dations. Many likely-to-sell homes aren’t owned by Compass contacts, suggesting further lead-
generation/sales-support products. And the infrastructure built can support other agent recom-
mendations: contacts with rising activity, consumers likely to buy or likely to refer business.
Understanding Value: High.Understanding the sales dynamics of properties increases the com-
pany’s ability to create complementary products serving agents, sellers, and buyers.
Overall Value Assessment: Very High.Strategic Alignment is Very High and the other three
dimensions are High; the direct fit with the core strategy and the breadth of follow-on products
lift the profile to Very High, a judgment over the profile, not an average.
4.1.2 Likelihood of Success
Product Certainty: High.Agents repeatedly named not knowing which contacts to call as a
challenge. LTS focuses agents on their own homeowner contacts, rather than cold-call leads. This
should result in a relatively high likelihood that the agent will be willing to initiate a conversation
with the homeowner, as well as a relatively high likelihood that the lead will be willing to talk to
the agent. A large portion of the agents use the CRM regularly, so product adoption is relatively
light (clicking on an additional tab in the CRM system). And even if the homeowner is not ready
to sell their home immediately, the conversation will bring the agent (back) into the consciousness
of the homeowner, and thus into the consideration set if/when they are interested in talking about
selling.5
Technical Certainty: High.The team could build the tool with resources on hand; the existing,
well-used, industry-leading Compass CRM system was a very suitable place to house it, and the
CRM technical team was excited about adding this functionality.
Data Certainty: High.Detailed lists of all prior property sales were available as training in-
stances. The majority of agents’ contacts could be mapped to the home(s) they owned, so a
property-level prediction could be tied to a specific contact to call. Although the existing data
did not include direct signals for why people sell (life events, family changes), useful proxies were
available: how long owners had been in the home, house size, school district, etc., and how those
factors had recently correlated with selling. Demand signals were available too: which property
types were sought after, neighborhood price and sales trends, and sale frequency for each prop-
erty.6
5Note that the vast majority of homesellers talk to only one agent when choosing who to represent them [31].
6For more on feature engineering for LTS, see https://medium.com/compass-true-north/framing-feature-
engineering-for-machine-learning-a-generative-model-of-home-likelihood-to-sell-f96f21d6d6d0.
15

Scientific Certainty: High.The modeling and inference problems were straightforward for an
experienced AI team [32].
Overall Likelihood Assessment: High.
4.1.3 Investment Required
Data Science Team Effort: Medium.The modeling and evaluation work was a substantial but
well-understood job for the team.
Data Asset Investment: Medium.The team could start with existing data for version 1.0 and
invest in additional data assets later, to possibly improve LTS prediction accuracy.
Integration and Productization Effort: Medium.The CRM product and engineering team was
willing to devote resources to product integration, which aligned with their interests.
Overall Investment Assessment: Medium.
4.1.4 The Upshot
We can now see why this was a top priority: Very High value across multiple dimensions, High
likelihood of success, and only Medium investment. By construction, that results in a very high
eROI.
The Result:Compass invested in building, integrating, and marketing LTS recommendations,
and the product became a lasting part of the platform. In its 2021 Q4 earnings call, the company
reported a nine-figure sum in annual gross commission revenue from listings the tool had flagged
before they came to market [9].
This wasincrementalrevenue (attributable to the recommendations rather than to listings agents
would have won anyway). Measuring that increment after the fact is exactly what the Time-on-
Market tool could not do, as the next example shows; here it was possible because the gradual
rollout of the recommendations created a natural experiment. Because each agent received only
a couple of recommendations per day, many to-be-recommended contacts had not yet been sur-
faced when they listed their homes. Among contacts the model scored as comparably likely to
sell, we have a treatment group (those listed homes where a recommendation was given) and a
control group (those not-yet-recommended homes). Comparing these groups, we see not only
the market share Compass won after recommending, but also the market share Compass won on
comparable homeswithouta recommendation [14]. Measuring the share Compass won onsur-
facedrecommendations versus that baseline isolates the additional business the recommendations
brought in.
16

As with all causal conclusions, the estimate rests on assumptions. In this case, the principal as-
sumption is that (setting aside the impact of the recommendation itself) at similar model scores,
listing just before rather than just after being surfaced is unrelated to whether a seller chooses a
Compass agent. Even so, Likely-to-Sell is a case where a product’s causalimpact, not merely its
predictive accuracy, could be measured. This available, observable counterfactual contrasts with
the case for the Time-on-Market tool, as we discuss in Section 4.2. The LTS product has continued
to evolve and expand, building on the AI platform components and data assets created in the
initial investment.
4.2 Example 2: Time-on-Market Pricing Tool
Contrast LTS with another application that drew strong stakeholder interest in 2019: a “what-if”
tool estimating how long a property would sit on the market at a given asking price, helping
agents weigh a seller’s wish to sell quickly against the higher price a longer wait might bring.
4.2.1 Value if Successful
Strategic Alignment: High.Such a tool would help agents price their clients’ listings and focus
their effort.
Direct Product Value: Medium.In the best case, the product could eliminate listings that expire
unsold. The benefit of selling faster is harder to quantify, as the value of time varies by agent
and client. We size this generously, on its best case, and the choice is deliberate: Likely-to-Sell
was credited only a modest one extra sale per agent per year, whereas we grant the Time-on-
Market tool its optimistic ceiling. The asymmetry favors the rejected project, so any ranking that
survives it is on firm ground. Of the roughly 30% of listings that do not convert, unrealistic pricing
accounts for perhaps three-quarters (about 22.5% of all listings), so a tool that reliably steered
sellers off overpricing would address the single largest cause. Converting even a fifth of those
would add roughly one extra sold listing for every five or six agents per year. At about $25,000 in
commissions per listing, that is on the order of $90 million across Compass’s 20,000 agents. Even
credited its best case, the tool lands far below the modestly credited Likely-to-Sell (roughly half
a billion dollars), though above the renovation tool discussed next; the ranking therefore holdsa
fortiori.
Option Value: Low.The team would need to brainstorm other applications, so the value here
was uncertain, though building the team’s capabilities in causal prediction (defined under Scien-
tific Certainty below) had some option value.
Understanding Value: High.Understanding the price–time relationship would likely inform
other strategies and tactics.
17

Overall Value Assessment: Medium to High.
4.2.2 Likelihood of Success
Product Certainty: Medium.Stakeholders were enthusiastic, but it was unclear whether agents
and their clients would trust and act on a model’s “what-if” pricing advice.
Technical Certainty: High.Serving such a tool in the company’s tech platform was well within
the team’s engineering capabilities.
Data Certainty: Low.Rich observational data on past listings existed, but the kind of data
needed to isolate what would happen with different prices, i.e., thecausaleffect of price, did not.
(There was little-to-no data on cases where the asking price varied for reasons unrelated to the
home itself, and since each home is unique it is difficult to match different-priced homesceteris
paribus).
Scientific Certainty: Low.This is acausal predictiontask: the AI estimates the effect of an in-
tervention (the asking price). The counterfactual ground truth (what would have happened at a
different price) is never observed. The obstacle was structural. Causal effects can be identified
with experiments, instruments (factors that shift price on their own, unrelated to the home), or
quasi-experimental variation [33], but the team had none of these: no way to randomize asking
prices when homes are listed, no instrument shifting price independently of the home. What it
had was observational data and pervasive unobserved confounding (hidden factors moving both
price and time to sell), which made cause and effect nearly impossible to disentangle here.
It did seem possible to predict time on market for a past pricing decision, but turning it into a
“what-if” tool would require strong, risky assumptions about the causal structure.
As discussed earlier, for likelihood, having even one “Low” source gates the overall assessment.
For the Time-on-Market tool, we have two.
Overall Likelihood Assessment: Low.
4.2.3 Investment Required
Data Science Team Effort: Very High.This was a research-grade problem within AI and data
science: the effort would be substantial, with real uncertainty about whether it would yield a
usable product at all.
Data Asset Investment: Medium.Beyond the observational data already on hand, building
toward the causal evidence the method needs would take real effort.
18

Integration and Productization Effort: High.Turning a research-grade model into a what-if
pricing tool that agents and clients could trust would demand careful product and UX work.
Overall Investment Assessment: High.The research-grade Team Effort (Very High) and heavy
Integration (High) set the level; the Medium data-asset investment does not pull the overall down
to Medium, since this is a judgment over the profile, not an average.
4.2.4 The Upshot
High scientific uncertainty and high investment together led the eROI to rate this project well
below other AI products.
Yet the strong strategic alignment suggested a different kind of investment:researchto clarify
the value-adding product idea and, if one existed, reduce the scientific uncertainty through ex-
ploration and pilots. The framework thus guides not just yes/no decisions but when a smaller
research investment makes sense first: its signature is high value if successful paired with a likeli-
hood capped by scientific uncertainty that targeted research might reduce. For a causal prediction
like this one, though, that research means a hunt for identifying variation (a natural experiment
or other source of exogenous price movement), not just an ordinary product pilot, since observa-
tional data alone cannot reveal the counterfactual.
The nature of the causal estimation differs fundamentally between the two tools. Likely-to-Sell
does not make causal predictions (calling a contact does not change the model’s estimate of their
likelihood to sell), so its only causal question is thepost-hocevaluation of whether the product
raised revenue, and there a usable counterfactual was close at hand (Section 4.1): had the nat-
ural experiment’s assumptions seemed too strong, a simple A/B test would have sufficed. The
Time-on-Market tool instead asks the AI to make a causalprediction(list at this price and time
on market will be such-and-such), and even assembling the training data would require running
price experiments on real homes with real sellers.
Two lessons follow. First, whether or not the AI product itself makes causal predictions, it pays to
have sophisticated causal-estimation expertise on the team; assuming that A/B tests are the only
route to causal estimates is a real handicap when such tests are costly or impossible (a business-
to-business firm, for instance, can rarely withhold a major new AI offering from a random subset
of its customers). Second, when the product itselfdependson causal estimation, scientific uncer-
tainty is generally much higher, and so is the sophistication (and the associated investment) of the
scientific work required.
4.3 Example 3: GenAI Renovation Visualizations
Our third case applies the framework to a generative-AI product idea: rendering how a dated
home would look after renovation.
19

Many on-market properties have not been recently renovated or refurbished. This can lower a
prospective buyer’s assessment of the home, especially if the buyer does not have much experi-
ence with modern renovations. The idea was to build an AI renovation-visualization tool, to help
buyers see a dated property’s potential. The main value assumption was that some listings fail
to convert because buyers cannot see past the home’s current condition. The tool would allow
agents to show prospective buyers how the kitchen, say, would look after renovation. A worn
kitchen with dated cabinetry and tired flooring could be compared with a newly renovated coun-
terpart. The technical idea: use generative AI to create an image of how the kitchen would look
after renovation.
4.3.1 Value if Successful
Strategic Alignment: Low to Medium.The tool would help sell properties that might otherwise
languish, supporting “get more business,” but would address a narrow slice of listings: those
where cosmetic condition, not pricing or location, is the main barrier. Its direct monetary value
to agents and the firm is minimal. If it worked, its stronger source of strategic value would lie
in agents’ interactions with prospective clients, helping differentiate them from other brokerages
and thus win more business.
Direct Product Value: Low to Medium.The upside here is small, perhaps $50 million across
20,000 agents (an order of magnitude below Likely-to-Sell’s roughly half a billion dollars), and
even that figure is optimistic. One reasoning chain that gets us there picks up where the Time-on-
Market tool left off: of the roughly 30% of listings that do not convert, pricing explains perhaps
three-quarters, leaving about 7.5% of listings where propertyconditionis the main barrier. Opti-
mistically, perhaps a third of those (roughly 2.5% of all listings) involve homes attractive enough
on other dimensions that a renovation visualization could tip a buyer’s decision.
With Compass agents averaging about four seller listings per year, that amounts to roughly 0.1
additional sold listings per agent per year. At approximately $25,000 in commission revenue per
listing, this yields roughly $2,500 per agent annually, or the $50 million total above. The figure
is crude and sensitive to the assumed lift; treat it as a rough scale. Even $50 million likely over-
states the gain: agents already had a cheaper, accepted alternative (virtual staging/renovation 7),
so much of the value was already captured, leaving littleincrementalgain, and no solid evidence
the tool would lift agents’ win rate with prospective clients.
Option Value: Low to Medium.The generative rendering would likely lean on a third-party
model, and thus would not create a proprietary data or model asset or platform component. There
is some option value in the team improving its capability with generative AI for images.
7Available even in 2019 from third parties, though time-consuming and costly.
20

Understanding Value: Low.The project yields little insight into business dynamics or customer
behavior.
Overall Value Assessment: Low to Medium.
4.3.2 Likelihood of Success
Product Certainty: Medium.Because agents already had an accepted, lower-cost option in vir-
tual staging, it was unclear how many would adopt a renovation-visualization tool on top of it.
There was a further risk that the gap between the rendered visualization and the real property
couldincreasebuyer disappointment on visiting, undermining trust in the agent and the listing.
Technical Certainty: Medium.Generative models could produce convincing renovation ren-
derings; however, they still sometimes made glaring errors. It was unclear whether those would
scuttle the product. The core engineering carried little risk.
Data Certainty: High.Compass had listing photos for all listed and to-be-listed properties. The
generative models require minimal training data for the focal properties.
Scientific Certainty: Medium.The image generation itself was feasible with contemporaneous
models, but achieving consistentlyrealistic and tastefulresults (appropriate to the property’s price
point, neighborhood, and architecture) required substantial prompt engineering and quality con-
trol. Unrealistic or generic-looking outputs could harm credibility.
Overall Likelihood Assessment: Medium.
4.3.3 Investment Required
Data Science Team Effort: Medium.When using a pre-trained model without fine-tuning, the
data-science effort shifts to prompt engineering, increased complexity of system output evalua-
tion, and API integration rather than ML model development.
Data Asset Investment: Low.Existing listing photos suffice.
Integration and Productization Effort: High.The tool needs careful UX design (including dis-
claimers), quality review workflows, agent training, and potentially legal review of generated
images in the context of real-estate disclosures.
Overall Investment Assessment: Medium.The single High on integration does not lift the over-
all rating, because the other two dimensions are Low (data assets) and Medium (team effort); the
overall is a judgment call over the profile, not an average.
21

4.3.4 The Upshot
Despite the appeal of a GenAI-powered product, the renovation visualization tool ranks below the
LTS product on nearly every dimension: lower value, lower likelihood, and comparable invest-
ment. Novelty does not translate into high eROI. The framework asks decision-makers to judge
GenAI opportunities by the same standard as traditional ones, not to favor a project simply for
using the latest technology.
Compass did build a renovation visualization tool. 8 However, as the risk from the GenAI errors
was eventually deemed too large to deploy, the Compass Lens took a different approach, which in
retrospect was a better product idea at the time. Specifically, given photos of a dated kitchen (for
example), Compass Lens used AI to find very similar kitchens that had been renovated recently. It
turned out that, in the huge database of homes on the market or recently sold, one could usually
find a renovated kitchen remarkably similar in layout to the focal kitchen.
The product’s reception was consistent with this modest assessment: it gained only limited trac-
tion, with many agents continuing to favor virtual staging, which met much of the same need at
lower cost and risk. The episode illustrates that Direct Product Value must be judged against the
best available alternative: the question is not whether a feature is valuable in a vacuum, but how
much value it adds beyond what teams would do without it.
5 Conclusion: From Scores to Decisions
The eROI framework does not eliminate judgment; it structures it, making assumptions explicit
and breaking the deadlock of needing to estimate ROI before knowing whether a project will
work. Splitting one nebulous number into three lets a team see exactly where it agrees and where
it disagrees, and prompts the conversation across business, product, engineering, and data science
that a single score would bury. It complements recent guidance emphasizing strategy before tech-
nology [5] and capability-building through incremental wins [26]: eROI supplies the structure for
choosingwhichprojects to fund. Whether the candidate is a traditional machine learning appli-
cation, a generative-AI product, or a research investment, the same three questions apply: How
valuable will it be if it succeeds? How likely is it to succeed? And what will it cost?
The template is short: rate the three pillars and their sub-dimensions on the coarse Low-to-Very-
High scale using the anchors in Table 1, visualize the profile as in Figure 2 so stakeholders can
grasp it at a glance, and revisit the rankings as new information emerges. The step easiest to skip
is one we have already argued for and the one that carries the most weight: build a portfolio
rather than picking the single top-ranked project, funding a mix whose values, likelihoods, and
costs balance one another instead of crowning one winner.
Our analysis has limits: as noted, although we used the framework at the time, the Compass case
8"Compass Lens," reported in the company’s S1 filing.
22

is retrospective and author-involved, so it illustrates how the framework organizes such choices
rather than providing a test of its predictive accuracy. The business cases throughout are coarse,
back-of-the-envelope estimates meant to expose the reasoning, not audited figures. A single com-
pany in a single industry cannot establish how far the framework generalizes. We have used the
framework in other settings, and our students have even more broadly; even so, we expect its
dimensions to be refined as others apply it in settings we have not seen.
A final caution concerns responsible deployment. The products in our case study are human-
facing: Likely-to-Sell ranks an agent’s personal contacts, and the renovation tool generates mar-
keting imagery of real homes. Putting such systems into production raises questions the eROI
score does not settle. How is contact data obtained, consented to, and secured? Could targeting or
generated imagery disadvantage particular neighborhoods or price tiers, a fair-housing concern
in U.S. residential real estate? Are AI-generated renderings disclosed so that buyers are not mis-
led? Many of these concerns are already inside the framework, in dimensions the earlier sections
named: compliance review, fairness and privacy safeguards, and disclosure add to Integration
and Productization Effort, and trust and safety risks lower Product Certainty, so a project that
cannot be deployed responsibly is not high-eROI. The concerns that do not fit a dimension we
treat as a gating constraint on what reaches production, not an afterthought.
Few projects will match Likely-to-Sell’s impact, but systematically choosing high-eROI projects
substantially improves the odds of AI investment success.
Author contributions
Both authors contributed equally to this work. Under the CRediT taxonomy, both share the roles
of Conceptualization, Writing – original draft, and Writing – review & editing.
Statements and Declarations
Ethical considerations.This article does not report research involving human participants, hu-
man data, human tissue, or animals, so ethical approval was not required. The AI products dis-
cussed in the case study are nonetheless human-facing; we address their privacy, fair-housing,
and disclosure implications in the Conclusion.
Consent to participate.Not applicable; this article does not involve human participants.
Consent for publication.Not applicable; this article does not contain data, images, or videos
from any identifiable individual.
23

Declaration of conflicting interest.The authors disclose the following potential conflicts of in-
terest. Both authors were employees of Compass Inc. from 2019 to 2022, the period during which
the AI initiatives described in this case study were undertaken. In addition, Panos Ipeirotis is
listed as a member of the editorial board ofBig Data, though he is inactive in that role and has
not served as a handling editor for the journal; he has no role in the editorial handling or peer
review of this manuscript, which the journal manages independently in line with its policy for
editorial-board submissions. The authors declare no other competing interests.
Funding statement.The authors received no financial support for the research, authorship, and/or
publication of this article.
Data availability.This article presents a conceptual framework and a retrospective case study; it
does not generate or analyze a research dataset. All quantitative figures are either drawn from the
publicly available sources cited herein or are explicitly labeled back-of-the-envelope estimates, so
no dataset is available to share.
Use of artificial intelligence.The authors used large language models as assistive tools for copy-
editing and language refinement, and for editorial review and revision of the manuscript, under
the authors’ direction and final review. No generative AI was used to produce the research, its
analysis, or its results, and no AI system is listed as an author.
References
[1] James Ryseff, Brandon F. De Bruhl, and Sydne J. Newberry. The root causes of failure for
artificial intelligence projects and how they can succeed: Avoiding the anti-patterns of AI.
Technical Report RR-A2680-1, RAND Corporation, 2024. URLhttps://www.rand.org/pubs/
research_reports/RRA2680-1.html.
[2] Aditya Challapally, Chris Pease, Ramesh Raskar, and Pradyumna Chari. The GenAI divide:
State of AI in business 2025. Technical report, MIT Project NANDA, July 2025. URLhttps:
//nanda.media.mit.edu/ai_report_2025.pdf.
[3] S&P Global Market Intelligence. Generative AI shows rapid growth but yields
mixed results. Voice of the Enterprise: AI & Machine Learning, 2025. URL
https://www.spglobal.com/market-intelligence/en/news-insights/research/2025/
10/generative-ai-shows-rapid-growth-but-yields-mixed-results.
[4] Deloitte. Now decides next: The state of generative AI in the enterprise. Deloitte
Global Survey, 2025. URLhttps://www.deloitte.com/az/en/issues/generative-ai/
state-of-generative-ai-in-enterprise.html. Fourth-quarter wave, published January
2025.
24

[5] W. Chan Kim, Renée Mauborgne, and Mi Ji. Make sure your AI strategy actually cre-
ates value.Harvard Business Review, September 2025. URLhttps://hbr.org/2025/09/
make-sure-your-ai-strategy-actually-creates-value.
[6] Melissa Valentine, Daniel J. Politzer, and Thomas H. Davenport. How to make enterprise
Gen AI work.Harvard Business Review, September 2025. URLhttps://hbr.org/2025/09/
how-to-make-enterprise-gen-ai-work.
[7] Eric Siegel. What leaders should know about measuring AI project value.MIT
Sloan Management Review, February 2024. URLhttps://sloanreview.mit.edu/article/
what-leaders-should-know-about-measuring-ai-project-value/.
[8] MIT Sloan Management Review. Gaining real business benefits from GenAI:
An MIT SMR executive guide. MIT Sloan Management Review Execu-
tive Guide, January 2025. URLhttps://sloanreview.mit.edu/article/
gaining-real-business-benefits-from-genai-an-mit-smr-executive-guide/.
[9] Compass Inc. Compass Inc. Q4 2021 earnings call transcript.
Seeking Alpha, 2022. URLhttps://seekingalpha.com/article/
4487666-compass-inc-comp-ceo-robert-reffkin-on-q4-2021-results-earnings-call-transcript.
Open-access transcript:https://www.fool.com/earnings/call-transcripts/2022/02/17/
compass-inc-comp-q4-2021-earnings-call-transcript/.
[10] Boston Consulting Group. Where’s the value in AI? BCG, 2024. URLhttps://www.bcg.com/
publications/2024/wheres-value-in-ai.
[11] Gene M. Amdahl. Validity of the single processor approach to achieving large scale com-
puting capabilities. InProceedings of the April 18–20, 1967, Spring Joint Computer Conference
(AFIPS), pages 483–485, 1967. doi: 10.1145/1465482.1465560.
[12] Foster Provost and Tom Fawcett.Data Science for Business: What You Need to Know about Data
Mining and Data-Analytic Thinking. O’Reilly Media, 2013. ISBN 978-1449361327.
[13] Paul W. Holland. Statistics and causal inference.Journal of the American Statistical Association,
81(396):945–960, 1986. doi: 10.1080/01621459.1986.10478354.
[14] Guido W. Imbens and Donald B. Rubin.Causal Inference for Statistics, Social, and Biomedical
Sciences: An Introduction. Cambridge University Press, New York, 2015. ISBN 978-0521885881.
doi: 10.1017/CBO9781139025751.
[15] Carlos Fernández-Loría and Foster Provost. Causal decision making and causal effect esti-
mation are not the same. . . and why it matters.INFORMS Journal on Data Science, 1(1):4–16,
2022. URLhttps://arxiv.org/abs/2104.04103.
25

[16] Joseph A. DiMasi. Risks in new drug development: Approval success rates for investigational
drugs.Clinical Pharmacology & Therapeutics, 69(5):297–307, 2001. doi: 10.1067/mcp.2001.
115446.
[17] Joseph A. DiMasi, Ronald W. Hansen, and Henry G. Grabowski. The price of innovation:
New estimates of drug development costs.Journal of Health Economics, 22(2):151–185, 2003.
doi: 10.1016/S0167-6296(02)00126-1.
[18] Sean McBride. RICE: Simple prioritization for product man-
agers. Intercom Blog, 2018. URLhttps://www.intercom.com/blog/
rice-simple-prioritization-for-product-managers/.
[19] Sean Ellis and Morgan Brown.Hacking Growth: How Today’s Fastest-Growing Companies Drive
Breakout Success. Currency, New York, 2017. ISBN 978-0451497215.
[20] Avinash K. Dixit and Robert S. Pindyck.Investment under Uncertainty. Princeton University
Press, Princeton, NJ, 1994. ISBN 978-0691034102.
[21] Lenos Trigeorgis.Real Options: Managerial Flexibility and Strategy in Resource Allocation. MIT
Press, Cambridge, MA, 1996. ISBN 978-0262201025.
[22] Robert G. Cooper. Stage-gate systems: A new tool for managing new products.Business
Horizons, 33(3):44–54, 1990. doi: 10.1016/0007-6813(90)90040-I.
[23] Robert G. Cooper, Scott J. Edgett, and Elko J. Kleinschmidt.Portfolio Management for New
Products. Perseus Publishing, Cambridge, MA, 2nd edition, 2001. ISBN 978-0738205144.
[24] Ronald A. Howard. Decision analysis: Practice and promise.Management Science, 34(6):
679–695, 1988. doi: 10.1287/mnsc.34.6.679.
[25] McKinsey Global Institute. The economic potential of generative AI:
The next productivity frontier. McKinsey & Company, 2023. URL
https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/
the-economic-potential-of-generative-ai-the-next-productivity-frontier.
[26] Melissa Webster and George Westerman. Generate value from GenAI with “small t” trans-
formations.MIT Sloan Management Review, January 2025. URLhttps://sloanreview.mit.
edu/article/generate-value-from-gen-ai-with-small-t-transformations/.
[27] Rama Ramakrishnan. A practical guide to gaining value from LLMs.MIT
Sloan Management Review, 66(2), 2024. URLhttps://sloanreview.mit.edu/article/
a-practical-guide-to-gaining-value-from-llms/.
[28] Compass, Inc. Compass, Inc. reports record fourth quarter and full-year 2025 re-
sults. Press release, 2026. URLhttps://www.prnewswire.com/news-releases/
26

compass-inc-reports-record-fourth-quarter-and-full-year-2025-results-302698918.
html.
[29] Christopher Mims. Ai isn’t magical and won’t help you reopen your busi-
ness.The Wall Street Journal, 2020. URLhttps://www.wsj.com/articles/
ai-isnt-magical-and-wont-help-you-reopen-your-business-11590811201.
[30] Compass True North. Likely to sell recommendations for real estate. Com-
pass Engineering Blog, 2020. URLhttps://medium.com/compass-true-north/
likely-to-sell-recommendations-for-real-estate-47e2f5c37f4.
[31] Jessica Lautz et al. 2023 profile of home buyers and sellers. National Associa-
tion of REALTORS, 2023. URLhttps://www.nar.realtor/research-and-statistics/
research-reports/highlights-from-the-profile-of-home-buyers-and-sellers.
[32] Compass True North. Machine learning in action for Compass’s likely-to-sell recommen-
dations. Compass Engineering Blog, 2020. URLhttps://medium.com/compass-true-north/
machine-learning-in-action-for-compasss-likely-to-sell-recommendations-699a6dcd5076.
[33] Joshua D. Angrist and Jörn-Steffen Pischke.Mostly Harmless Econometrics: An Empiricist’s
Companion. Princeton University Press, Princeton, NJ, 2009. ISBN 978-0691120355.
27
