---
title: 'Selling in the Wild: Benchmark and Randomized Field Evidence for a Sales Agent Trained on Commercial
  Conversations'
url: https://arxiv.org/abs/2610.25461
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: arXiv (Cornell University)
authors:
- Benjamin Tannenbaum
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.25461
pages: 26
chars: 66246
fetched_at: '2026-11-08T13:31:04+00:00'
kb_version: 1
---

# Selling in the Wild: Benchmark and Randomized Field Evidence for a Sales Agent Trained on Commercial Conversations

Selling in the Wild: Benchmark and Randomized Field Evidence for
a Sales Agent Trained on Commercial Conversations
Benjamin Tannenbaum
Javo, AISO Boost Ltd.
Israel company no. 517132197
https://getjavo.com
Abstract
We test whether Javo, a sales agent fine-tuned on 4.6 million consented, de-identified
commercial conversations, sells better than a frontier general-purpose model and better than
human sales associates. The evaluation has four parts. Study 1 scores the agent on two public
sales benchmarks, SalesLLM and SmartSalesBench, against 10 frontier and open-weight models.
Study 2 is a randomized controlled trial on 100 live websites in 14 industries (e-commerce, travel
and hospitality, and high-consideration services), run from 1 May to 30 September 2026, in
which 14.8 M visitors were randomized to no agent, Javo, or a frontier-model agent with an
identical interface, catalog tools and guardrails. Study 3 isolates the effect of the model by
comparing those two agent arms. Study 4 compares Javo with each site’s own human associates
on 20 sites with staffed live chat. Relative to no agent, Javo changed revenue per visitor by
+10.0% (95% CI +5.1 to +14.9). Among engaged visitors it changed conversion by +21.6%
relative to the frontier-model agent (95% CI +16.9 to +26.3). Against human associates its
engaged conversion was 11.26% versus 11.20% (non-inferior (margin -7%, one-sided p=0.004); no
significant superiority), at 1.8% of the cost per conversation. Return rates, unsupported product
claims and complaint rates met the prespecified safety margins pre-specified guardrails.
1 Introduction
The open question is not whether language models can talk about products; it is whether a deployed
model changes what people buy, and by how much. Commerce is moving into conversation: shoppers
ask an assistant on a retailer’s site, in a booking flow or in a general chatbot instead of filtering
a catalog. A site owner deciding whether to deploy a sales agent needs an incremental number,
revenue per visitor with the agent minus revenue per visitor without it, measured on their own
traffic.
Selling is a distinct task from answering. It is goal-directed, multi-turn persuasion under
asymmetric incentives: the agent must elicit needs, recommend, handle objections and propose a
next step, while the customer may resist [Petty and Cacioppo, 1986; Su et al., 2026]. General-purpose
assistants are post-trained to be helpful and agreeable [Ouyang et al., 2022; Sharma et al., 2024],
and on sales benchmarks weaker models behave like passive question-answering bots rather than
salespeople [Su et al., 2026]. We hypothesize that the missing ingredient is data: transcripts of real
commercial conversations in which buyers state needs, hesitate, object, compare and then do or do
not buy.
Existing evidence leaves three gaps. First, sales benchmarks score models against artificial
customers, and the choice of simulator can reorder the leaderboard: on SalesLLM’s English split,
per-model scores under two simulators correlate at only r = 0.24 [Su et al., 2026]. Second, field
1
arXiv:2610.25461v1  [cs.IR]  18 Oct 2026

evidence predates current models. The best-known field experiment found that undisclosed chatbots
matched proficient human workers in generating purchases, but that disclosing the bot before the
conversation cut purchases by more than 79.7% [Luo et al., 2019]. Third, studies of generative AI
at work measure assistance to human agents, not autonomous selling [Brynjolfsson et al., 2025;
Dell’Acqua et al., 2023].
This paper builds on earlier findings that the conversation, not its final prompt, is the defensible
unit of analysis for AI interactions [Tannenbaum, 2026c,a]. We apply that view to selling: Javo
is trained on whole commercial conversations from the consented corpus collected by Aiso, and
evaluated on whole visits.
We make four contributions:
1. A four-study evaluation protocol for sales agents that links offline benchmark scores to
randomized revenue outcomes on live traffic.
2. A battery of 100 consenting websites in 14 industries, with a pre-specified primary metric for
each business model.
3. A model-isolating comparison: Javo versus a frontier model inside identical scaffolding (inter-
face, retrieval, catalog tools, system prompt, guardrails), so that any difference is attributable
to the model weights.
4. A randomized comparison with each site’s own human chat associates, with cost, latency and
customer-satisfaction outcomes alongside conversion.
The studies answer five research questions:
• RQ1 (benchmark).Does commercial-conversation training raise scores on public sales
benchmarks relative to frontier and open-weight models?
• RQ2 (incrementality).Does deploying the agent raise revenue per visitor relative to no
agent?
• RQ3 (model effect).Holding scaffolding fixed, does the trained model outsell a frontier
model?
• RQ4 (human comparison).Is the agent non-inferior, or superior, to human associates on
conversion and satisfaction?
• RQ5 (safety).Do gains come without increases in returns, cancellations, unsupported claims
or complaints?
2 Related Work
Prior work measures selling in benchmark environments or measures AI assistance to humans; none,
to our knowledge, randomizes a trained sales model against both a frontier model and human
associates on live traffic across industries.
Sales and persuasion benchmarks.SalesLLM provides 1,805 multi-turn scenarios in Chinese
and English, a trained customer simulator (CustomerLM) and a score combining an LLM judge
of sales progress with a classifier of end-of-dialogue buying intent; the strongest of 15 models
match junior-to-intermediate human salespeople in Chinese but not experts [Su et al., 2026].
SmartSalesBench places agents against psychologically grounded, resistant buyer personas over
up to twenty turns, across 13,680 sessions [Teja et al., 2026]. Earlier sales dialogue work studied
2

transitions from chit-chat to task-oriented selling [Chiu et al., 2022], contrasted salespeople with
conversational recommenders [Murakhovs’ka et al., 2023], injected salesperson strategies through
chain-of-thought [Chang and Chen, 2024] and targeted reliable telemarketing [Zhang et al., 2025].
Persuasion corpora [Wang et al., 2019; Jin et al., 2024a], negotiation testbeds [Lewis et al., 2017; He
et al., 2018; Fu et al., 2023; Bianchi et al., 2024] and social-goal environments [Zhou et al., 2024]
supply adjacent tasks, but most assume a cooperative or neutral counterpart.
Agents for commerce.Shopping agents are evaluated on catalog navigation [Yao et al., 2022],
on policy-constrained tool use in retail and airline domains [Yao et al., 2024] and on shopping
knowledge and reasoning [Jin et al., 2024b]. Domain-tuned e-commerce models improve such tasks
[Li et al., 2024; Peng et al., 2024]. CRM benchmarks show that leading agents complete under
58% of single-turn professional tasks and about 35% in multi-turn settings [Huang et al., 2025a,b].
Conversational recommender research supplies the elicitation-then-recommendation framing we
adopt [Li et al., 2018; Jannach et al., 2021; He et al., 2023].
Field evidence.In a six-condition field experiment on loan renewals, undisclosed chatbots were
as effective as proficient workers and four times as effective as inexperienced ones, while early
disclosure cut purchases by more than 79.7% [Luo et al., 2019]. On a large cross-border retail
platform, a generative-AI pre-sale chatbot raised sales by 16.3% against no service, mainly through
conversion, with no deterioration in return rates or ratings [Fang et al., 2025]. Assistance studies
find productivity gains for human support agents, largest for novices [Brynjolfsson et al., 2025], and
uneven gains for consultants depending on task [Dell’Acqua et al., 2023]. Chatbot design affects
compliance [Adam et al., 2021] and anger in service failures [Crolic et al., 2022], and disclosure
trades transparency against efficiency [Ishowo-Oloko et al., 2019]. Randomized studies show that
language models can be persuasive in debate [Salvi et al., 2024], can durably shift beliefs through
dialogue [Costello et al., 2024] and can personalize persuasive messages at scale [Matz et al., 2024],
which motivates our safety guardrails.
Evaluation methodology .LLM judges are scalable but biased by position, verbosity and style
[Zheng et al., 2023; Wang et al., 2024; Dubois et al., 2024], and LLM user simulators drift into the
assistant role [Sekuli´ c et al., 2024; Naous et al., 2025]. Benchmark contamination can inflate scores
[Sainz et al., 2023]. Online controlled experiments have a mature methodology for metric design,
variance reduction, sample-ratio checks and continuous monitoring [Kohavi et al., 2009, 2020; Deng
et al., 2013; Johari et al., 2017; Fabijan et al., 2019; Larsen et al., 2024], which we follow.
Training on real conversations.Public corpora of real user–assistant conversations [Zheng
et al., 2024; Zhao et al., 2024; Kirk et al., 2024] show that natural requests differ from benchmark
prompts. Earlier work on the Aiso corpus measured how conversational answers compress search
work [Tannenbaum, 2026b], how request state accumulates across turns [Tannenbaum, 2026c] and
how much within-conversation context changes answers [Tannenbaum, 2026a]. This paper is the
first to train on that corpus and measure a commercial outcome.
3 System: Javo and its Training Corpus
Javo is an open-weight base model fine-tuned on whole commercial conversations, then deployed
inside a scaffold that every agent arm in this paper shares. Only the model weights differ between
Javo and the frontier arm.
3

3.1 Corpus
We define a commercial conversation as one in which the user’s request state, accumulated across
turns [Tannenbaum, 2026c], includes an intent to buy, book or choose a provider. The corpus
is drawn from the governed commercial-conversation collection assembled by Aiso and used in
earlier work [Tannenbaum, 2026b,a], restricted to conversations collected with user consent and
de-identified before use. Table 1 summarizes it.
T able 1:Training corpus.
Property Value
Conversations (after filtering) 4.6 million
Turns 58.4 million (median 10 per conversation)
Languages English 68%, French 16%, Spanish 8%, other 8%
Collection window February 2024 to March 2026, ending before 1 May 2026
Verticals retail 46%, travel 28%, services 26%
Conversations with a joined outcome label 17.4%
De-identification Automated PII redaction, hashed identifiers, manual QA;
residual PII rate on an audited sample of 2,500: 0.16%
Three filters protect the evaluation. Conversations that mention any of the 100 evaluation sites,
their brands or their domains are removed. The collection window closes before the field study
starts. Benchmark scenarios from SalesLLM and SmartSalesBench are checked for n-gram overlap
with the corpus, following contamination practice [Sainz et al., 2023]; overlap was 0.02%.
3.2 Training
Training has two stages. Supervised fine-tuning teaches the model to produce the seller turn given
the full preceding conversation, so it learns elicitation, recommendation, objection handling and
next-step proposals in context rather than from isolated prompts [Ouyang et al., 2022; Hu et al.,
2022]. Preference optimization [Rafailov et al., 2023] then uses pairs of seller turns taken at matched
conversation states, where the preferred turn preceded progress (a stated purchase intent, a booking,
a lead) and the dispreferred turn preceded a stall or exit. A third data mix teaches constraints: no
discounts or terms absent from the site’s policy, no claims absent from the catalog, AI disclosure on
request and handoff to a human on request. Table 2 gives the settings.
T able 2:Training settings.
Setting Value
Base model Qwen3-32B
SFT examples / epochs 1.65 million / 2
Preference pairs 190,000
Constraint examples 34,000
Hardware and compute 32 H100 GPUs, 2,240 GPU-hours
Frozen model version for the field study javo-v1, frozen on 24 April 2026
3.3 Shared deployment scaffold
Every agent arm runs in the same scaffold, so the comparison in Study 3 isolates the model.
4

• Interface.The same chat widget, position, per-site colors, opening greeting and AI disclosure
line (“I’m an AI shopping assistant”).
• Grounding.Retrieval over each site’s catalog, availability, prices and policies, refreshed every
24 hours.
• Tools. search catalog, get item, check availability, add to cart or start booking,
get policy,capture lead,handoff to human.
• Prompt.The same system prompt template per site, listing allowed offers, tone and escalation
rules.
• Guardrails.The same output filter for prices, discounts and policy statements, checked
against the site’s data before display.
•Latency .The same time budget; responses exceeding 8 s are logged as timeouts.
4 Evaluation Design Overview
One offline study and three randomized field studies share a single deployment: visitors to 100
sites were randomized between 1 May and 30 September 2026 (153 days), and each field study is a
different contrast between arms of that one experiment (Table 3, Figure 1).
T able 3:The four studies.
Study Setting Contrast Primary outcome RQ
1 Offline benchmarks SalesLLM (EN, 805
scenarios),
SmartSalesBench,
τ-bench retail
Javo vs 10 models;
human sellers on 200
scenarios
Benchmark score 1, 5
2 Incrementality 100 sites,
visitor-randomized
Javo vs no agent Revenue per visitor 2, 5
3 Model isolation 100 sites,
visitor-randomized
Javo vs frontier agent Engaged conversion 3
4 Human comparison 20 staffed-chat sites,
staffed hours
Javo vs human
associates
Engaged conversion;
CSAT
4
Assignment.Each visitor’s first-party identifier is hashed with a site-specific salt and mapped to
an arm; assignment is sticky for the whole study, so a returning visitor sees the same experience.
On the 80 standard sites the allocation is 20% no agent, 40% Javo and 40% frontier agent. On the
20 sites with staffed live chat it is 10% no agent, 30% human chat, 30% Javo and 30% frontier agent.
The two agent arms receive equal shares so that Study 3, the smallest expected effect, has the most
power. On staffed sites the human arm shows the site’s usual live-chat widget; outside staffed hours
it shows the site’s usual message form, which is why Study 4 restricts to visitors whose first session
starts during staffed hours, a pre-treatment variable.
Pre-period.From 1 March to 30 April 2026 every site ran the measurement tag without any
agent. This window supplies covariates for variance reduction [Deng et al., 2013] and an A/A test
of the assignment and logging pipeline, which passed on 98 of 100 sites.
5

Visitor ID hashed with a site salt
Same arm on every return visit
No agent
Standard sites: 20%
Staffed sites: 10%
Human chat
Standard sites: none
Staffed sites: 30%
Javo
Standard sites: 40%
Staffed sites: 30%
F rontier agent
Standard sites: 40%
Staffed sites: 30%
Study 4:humans
20 sites, staffed hours
Study 3:vs frontier agent
Model isolation, 100 sites
Study 2:vs no agent
Incrementality, 100 sites
Figure 1:One visitor randomization feeds three field contrasts. Every field study compares Javo with
one comparator arm drawn from the same randomization, so Studies 2 to 4 share visitors, period and
measurement.
5 Website Battery
The battery is 100 consenting websites in 14 industries: 60 e-commerce, 25 travel and hospitality,
and 15 high-consideration service sites (Table 4). The mix favors business models where buyers ask
the most questions before committing: fragrance and hair care, furniture, island resorts, holiday
rentals, language schools, logistics providers and wealth advisory.
Inclusion criteria.A site was eligible if it had at least 20,000 sessions per month in the pre-period,
server-side order, booking or lead events joinable to a visitor identifier, a machine-readable catalog
or inventory feed, no AI sales agent already live, and written consent from the owner to randomize
visitors and share de-identified outcome data. Sites selling age-restricted products were excluded.
Regulated categories.On financial advisory sites the agent ran in lead-capture mode only: it
explained services and booked consultations but gave no product or investment recommendation.
Health claims on beauty and food sites were limited to text present in the site’s own product data.
Confidentiality , geography and language.Sites are reported as S001 to S100 with industry
and region; 21 sites agreed to be named. Sites served United States 38, United Kingdom 18, France
15, Spain 9, Portugal 8, other 12. Conversations ran in English 72%, French 14%, Spanish 8%, other
6%; both agent arms responded in the visitor’s language.
6

T able 4:Website battery by industry.
Vertical Industry Sites Typical site Primary metric
E-commerce Beauty and personal care 12 Hair care,
fragrance,
skincare brands
RPV
Furniture and home d´ ecor 10 Sofas, beds,
lighting; AOV
above$500
RPV
Fashion and accessories 10 Apparel,
footwear,
jewelry
RPV
Home and garden 8 Plant nutrients,
garden tools,
outdoor
RPV
Gifts and subscription boxes 8 Gift boxes,
curated
subscriptions
RPV
Specialty food and beverage 6 Coffee, tea,
home brewing
RPV
Consumer electronics 6 Audio, phone
accessories,
smart home
RPV
Travel Hotels and resorts 12 Independent
and resort hotels
Booking RPV, net of cancellations
Vacation rentals 10 Direct-booking
rental operators
Booking RPV, net of cancellations
Tours and experiences 3 Day tours,
activities
Booking RPV
Services Education and language 5 Language
schools, online
courses
Enrollment or trial rate
Home services 4 HV AC, repair,
installation
Qualified-lead rate
B2B logistics 3 3PL, freight,
cold storage
Qualified-lead rate
Financial advisory 3 Retirement and
wealth advisory
Booked consultation rate
6 Study 1: Offline Sales Benchmarks
Study 1 asks whether commercial-conversation training shows up on public benchmarks before any
traffic is involved, and whether it costs general agent reliability. Every model runs every scenario
under the benchmark authors’ published settings.
6.1 Benchmarks
SalesLLM, English split [Su et al., 2026].805 multi-turn scenarios across consumer goods
and financial services, five difficulty tiers from cooperative to adversarial. We run each model
against both released simulators, CustomerLM and a GPT-4o customer, because the simulator
choice can reorder rankings. Settings follow the benchmark: temperature 0.8, top- p 0.99, at most 20
7

rounds. The score is 0 .5× buying-intent score + 0.5× selling-performance score, each on 0 to 10.
We run three seeds per model and report the mean with a scenario-level bootstrap 95% CI (10,000
resamples).
SmartSalesBench [Teja et al., 2026].Twelve resistant buyer personas, fifteen smartphone
products in six price tiers, conversations up to twenty turns. Javo and each baseline are entered as
agent profiles; we report the benchmark’s own outcome and judge metrics.
τ -bench, retail domain [Y ao et al., 2024].A policy-constrained tool-use benchmark, used as
a guardrail: sales tuning should not make the agent worse at following store policy or completing
account tasks. We report pass 1 and pass4.
6.2 Models and human sellers
The comparison set comprises Javo (the frozen field version); three ablations (Javo’s base model
before tuning, supervised fine-tuning only, and full training without constraint data); frontier models
(GPT-5.2, used again in Study 3, plus Claude Opus 4.6; Gemini 3 Pro); and open-weight baselines
(DeepSeek-V3.2; Qwen3-235B; Llama 4). The ablation against Javo’s own base model is the key
control: a gain over frontier models could come from the base model, while a gain over the base
model can only come from training.
SalesLLM’s human reference covers junior-to-intermediate sellers in Chinese only [Su et al.,
2026]. We add an English reference with two experience tiers: 12 sellers with one to three years of
experience and 12 with five or more. Each completes a stratified subset of 200 scenarios (40 per
tier) against CustomerLM through the same text interface, with the same product sheet the models
receive, paid USD 32 per hour plus USD 8 per closed deal to mirror sales incentives. Sellers were
recruited through Partner referrals and Upwork and screened on verifiable sales employment.
6.3 Judge validation and success criteria
Three trained annotators blind to the seller’s identity rescore 500 dialogues (100 per tier), sampled
across Javo, two frontier models and the human sellers. We report Pearson r between automated
and human scores and Krippendorff’sαamong annotators. The pre-specified criteria are:
• S1a.On SalesLLM-EN with CustomerLM, Javo’s mean exceeds the best frontier model’s by
at least 0.3 points, with the bootstrap 95% CI of the difference excluding zero.
•S1b.The same direction holds under the GPT-4o customer and on SmartSalesBench.
•S1c.Javo scores at least as high as the junior human tier on the 200-scenario subset.
•S1d (guardrail).Javo’sτ-bench retail pass 1 is within 3 points of its base model.
7 Study 2: Live A/B Test, Agent versus No Agent
Study 2 measures what a site owner actually gets: the change in revenue per randomized visitor
when Javo is offered, including the visitors who never open the chat.
8

7.1 Arms, exposure and outcomes
In the no-agent arm the site runs unchanged. In the Javo arm a chat launcher is visible on every
page, and on product, room or service pages a single proactive greeting appears after 25 seconds,
at most once per session. The trigger rules are identical in both agent arms. Table 5 defines the
outcomes.
T able 5:Study 2 outcomes.
Metric Definition Role
Revenue per visitor (RPV) Net revenue from orders or bookings placed during
the study by a randomized visitor, minus refunds
and cancellations within 30 days after 30
September, per randomized visitor; 85
transactional sites
Primary (H1)
Conversion Share of randomized visitors with at least one
order, booking, paid enrollment or qualified lead;
all 100 sites
Secondary (H1b)
Average order value Net revenue per order Secondary
Qualified-lead rate Leads accepted as qualified in the site’s CRM
within 30 days; 15 service sites
Vertical primary
Engagement Share of visitors who send at least one message Descriptive
Returns, cancellations, complaints See Section 10 Guardrail
Revenue is converted to US dollars at the daily reference rate and winsorized at each site’s
99.9th percentile of pre-period visitor revenue. Lead-generation sites have no revenue, so they enter
H1b and their vertical metric but not H1.
7.2 Estimands
The primary estimand is the intention-to-treat (ITT) effect: the difference in mean outcome between
visitors assigned to Javo and visitors assigned to no agent, regardless of whether they engaged.
It answers the deployment question directly and is protected by randomization. An additional
illustration divides relative ITT revenue lift by the Javo engagement share. This assumes all uplift
comes from engagers and does not identify their relative causal effect.
7.3 Data pipeline and validity
• Identity .A first-party visitor identifier, joined to the site’s order system by order ID; logged-in
customer IDs merge devices where available.
• Bots.Traffic matching known crawler signatures or behavioral rules (no scroll, sub-second
sessions, data-center IP ranges) is removed before analysis, identically in all arms.
• Sample ratio.Each site’s arm counts are tested against the design allocation; a χ2 p <0.001
flags a site for investigation [Fabijan et al., 2019].
• Novelty .We estimate the effect separately by study week to detect novelty or learning effects
[Hohnhold et al., 2015].
• Interference.On hotel and rental sites, inventory booked by one arm is unavailable to the
others. We record sell-out dates per site and rerun the analysis without them.
9

8 Study 3: Agent versus Frontier-Model Agent
Study 3 tests the paper’s central claim: with interface, tools, grounding, prompt and guardrails held
fixed, does a model trained on commercial conversations sell more than the strongest general-purpose
model?
Choosing the frontier baseline.The baseline was chosen by a pre-specified rule: among frontier
models available by API on 24 April 2026, the one with the highest SalesLLM-EN score under
CustomerLM in a pilot run of Study 1. That model was GPT-5.2. Its version was pinned for the
whole study through version-locked endpoints.
Equal-effort prompting.Both arms received the same site system prompt. The frontier arm
additionally received a general sales-practice instruction block (elicit needs before recommending,
address objections with catalog facts, propose a concrete next step), written by Independent sales
trainer, 9 years experience with a budget of 14 hours, equal to the time spent tuning Javo’s prompt.
Both prompts were frozen on 28 April 2026 (Appendix C).
Why engaged-session comparisons are valid here.Conditioning on engagement normally
breaks randomization because the treatment can change who engages. In Study 3 it does not: the
launcher, greeting and disclosure line are identical in both arms, and the visitor’s first message is
sent before either model has produced any output. Engagement is therefore determined before the
model can influence it. We verify this with a pre-specified two-proportion test of equal engagement
rates across the two arms.
Outcomes.The primary outcome is engaged conversion: the share of engaged visitors with
at least one order, booking or qualified lead after their first message (H2). Secondary outcomes
are ITT revenue per visitor (H2b), average order value among engaged buyers, inference cost per
engaged conversation and the in-chat rating. Conversation length, handoff rate and timeout rate
are descriptive.
Mechanism analysis.Transcripts from both arms are coded for four sales behaviors adapted
from SalesLLM’s selling dimensions [Su et al., 2026] and the needs-first selling literature [Rackham,
1988; Spiro and Weitz, 1990]: needs elicitation (questions asked before the first recommendation),
recommendation specificity (named items tied to stated needs), objection handling (a stated concern
followed by catalog evidence and a later turn showing the concern eased) and next-step proposal
(an explicit add-to-cart, booking or lead step). An LLM coder labels all conversations; three
human coders label a random 600, and agreement is reported before the automated labels are used.
Behaviors are not randomized, so this analysis explains rather than proves the effect.
9 Study 4: Agent versus Human Sales Associates
Study 4 compares Javo with the people it would replace or support: each site’s own live-chat
associates, working their normal shifts, on the same traffic.
Setting and participants.Twenty sites in the battery ran staffed live chat before the study
(furniture 5, hotels 7, vacation rentals 5, beauty 3). Their 59 associates (median tenure 25 months; 19
with three or more years) kept their usual tools, scripts, incentives and hours. Associates were told
10

a study was running and consented to the use of de-identified transcripts; individual performance
data were not shared with employers and were not used for any employment decision. This is a
comparison with typical working associates, not with the best salespeople a firm could hire; Study 1’s
expert tier supplies the expert reference offline.
Design.The Study 4 contrast is Javo versus human chat, restricted to visitors whose first session
began during staffed hours. Javo’s greeting discloses that it is an AI; the human widget shows
the associate’s first name as the site normally does. The comparison is therefore between the two
options a site can actually deploy, disclosed AI or a human, not between an AI and a human the
visitor cannot tell apart [Luo et al., 2019].
Outcomes and estimands.The primary outcome is engaged conversion, tested for non-inferiority
(H3). The co-primary outcome is CSAT on a 1 to 5 post-chat survey shown identically in both
arms (H3b). ITT conversion and revenue per visitor among staffed-hours visitors are robustness
checks; first-response time, conversation duration and cost per engaged conversation are secondary.
Human cost is fully loaded hourly cost divided by conversations per hour; Javo’s cost is inference
plus monitoring. Unlike Study 3, the two widgets differ before the first message, so the engaged
populations may differ. We report the engagement rate in each arm, compare engaged visitors on
pre-treatment covariates (pre-period visits, device, traffic source, landing page type), bound the
engaged-conversion difference with trimming bounds for sample selection [Lee, 2009] and report the
ITT difference, which is unbiased but diluted.
Non-inferiority margins.Javo is non-inferior on engaged conversion if the lower bound of the
95% CI of the relative difference (Javo − human)/human is above −10%. The margin reflects the
cost difference: if the agent costs a small fraction of a human conversation, a site would accept
a modest conversion shortfall, but not more than a tenth. The CSAT margin is −0.2 points.
Superiority is claimed only if the lower bound is above zero, tested after non-inferiority in a fixed
sequence so that no extraαis spent.
10 Hypotheses, Expected Ranges and Success Criteria
Three primary hypotheses decide the paper’s headline; every other result is secondary. Expected
ranges were set before unblinding, anchored on published field and benchmark evidence (Table 6); a
result outside them is reported as found.
T able 6:Primary hypotheses.
ID Hypothesis Metric Expected Success criterion
H1 Javo raises revenue per
visitor vs no agent
RPV, ITT, 85 sites +3 to +9% Holm-adjusted 95% CI
excludes 0 and estimate
≥+2%
H2 Javo outsells the frontier
agent with identical
scaffolding
Engaged conversion +8 to +25% Holm-adjusted 95% CI
excludes 0 and estimate
≥+5%
H3 Javo is non-inferior to
human associates
Engaged conversion−5 to +15% Lower CI bound>−10%;
superiority if>0
11

The H1 range starts from the 16.3% sales lift of a pre-sale chatbot against no service [Fang et al.,
2025], diluted by an expected engagement rate of 5 to 12% of visitors. The H2 range reflects model
gaps of 0.5 to 1.0 points on SalesLLM [Su et al., 2026] and the underperformance of a non-tuned
model in a retail workflow [Fang et al., 2025]. The H3 range straddles zero because undisclosed
chatbots matched proficient workers while disclosure lowers purchase [Luo et al., 2019].
T able 7:Secondary hypotheses.
ID Hypothesis Metric Expected Criterion
H1b Javo raises conversion
vs no agent
Conversion, ITT, 100
sites
+2 to +7% BH-adjusted CI
excludes 0
H1c Effect on engaged
visitors
Engagement-scaled RPV
illustration
Descriptive only Reported with CI
H2b Javo raises RPV vs
frontier agent
RPV, ITT +1 to +4% BH-adjusted CI
excludes 0
H3b Javo CSAT non-inferior
to humans
CSAT, 1 to 5−0.2 to +0.1 Lower CI bound >− 0.2
H3c Javo costs less per
conversation
Cost per engaged
conversation
1 to 10% of human Reported
H4 Javo beats frontier
models offline
SalesLLM-EN,
CustomerLM
+0.3 to +0.8 points S1a to S1d
Guardrails (RQ5).A primary result counts as a success only if every guardrail holds. Guardrails
are non-inferiority tests: harm is ruled out when the upper CI bound stays below the margin.
Return rate per order and booking cancellation rate may not rise by more than 0.5 percentage
points against no agent; complaint contacts per 1,000 visitors may not rise by more than 0.05. In
audited agent turns, unsupported product or policy claims must stay at or below 1.0% of turns and
prohibited pressure tactics (false scarcity, false urgency, invented social proof) at or below 0.1%;
unauthorized offers have zero tolerance, with each instance reviewed.
What would count as failure.We committed in advance to report each of these plainly: H1 fails
(an agent does not pay for itself); H1 succeeds but H2 fails (a frontier model with good scaffolding
helps as much, so training adds nothing); H3 fails (humans still outsell the agent by more than the
margin); any guardrail fails (gains come from pressure or inaccuracy).
11 Statistical Analysis Plan
The primary analysis is a fixed-horizon, intention-to-treat comparison at the end of the study,
estimated per site and pooled with a random-effects model, with Holm correction across the three
primary hypotheses. The analysis specification and deviations are listed in Appendix D.
Site-level estimator.For each site s, the relative effect of treatment T against comparison C on
outcomeYis
ˆ∆s =
¯Y cv T,s − ¯Y cv C,s
¯Y cv C,s ,(1)
12

where each visitor’s outcome is adjusted with pre-period data [Deng et al., 2013], using pre-period
revenue and visits as covariateXand the site mean for visitors with no pre-period history:
Y cv i =Y i − ˆθ(X i − ¯X), ˆθ= Cov(Y, X) Var(X) .(2)
The variance of the ratio follows the delta method [Deng et al., 2018]:
Var(ˆ∆s)≈ 1 ¯Y 2 C
 s2 T
nT
+
¯Y 2 T
¯Y 2 C · s2 C nC  .(3)
Pooling across sites.Sites differ in traffic, price and baseline conversion, and a site owner’s
question is whether the effect holds for a typical site. The primary pooled estimate is therefore the
random-effects mean, with between-site variance τ 2 estimated by restricted maximum likelihood and
the Hartung–Knapp adjustment to the confidence interval [DerSimonian and Laird, 1986; Hartung
and Knapp, 2001; Viechtbauer, 2010]:
ˆ∆ =
P
s ws ˆ∆sP
s ws
, w s = 1 Var(ˆ∆s) + ˆτ2 .(4)
We also report the 95% prediction interval for a new site and the visitor-weighted pooled estimate,
which answers the average-visitor question.
Engaged-visitor estimands.The engagement-scaled illustration divides relative H1 lift and its
interval by the fixed Javo engagement share; it excludes uncertainty in engagement and is not a
CACE estimate. Study 3’s engaged comparison is a direct difference in proportions, valid under the
balance argument of Section 8. Study 4’s engaged comparison is accompanied by trimming bounds
[Lee, 2009].
Multiplicity .Holm’s step-down procedure controls the familywise error across H1, H2 and H3
at α = 0 .05 [Holm, 1979]. H3 superiority is tested only after non-inferiority, in fixed sequence.
Secondary and heterogeneity analyses use Benjamini–Hochberg at q = 0 .05 within each family
[Benjamini and Hochberg, 1995].
Monitoring and stopping.Primary metrics were not analyzed before the end of the study.
Guardrails were monitored weekly per site with always-valid sequential tests [Johari et al., 2017]; a
confirmed breach paused the agent on that site for review. Paused sites remain in the ITT analysis
in their assigned arms.
Heterogeneity.Pre-specified moderators are vertical, industry, device, new versus returning
visitor, traffic source (paid search, organic search, AI-assistant referral, direct, email, social), price
tier (site AOV tercile) and conversation language, each tested with a treatment-by-moderator
interaction in a site-stratified regression. A causal forest is exploratory only [Wager and Athey,
2018].
Robustness.We repeat the primary analysis (1) excluding the first 14 days, (2) excluding sell-out
dates on inventory-limited sites, (3) without winsorization, (4) on logged-in visitors only, (5) with
stricter bot filtering, (6) leaving out one site at a time and (7) without CUPED adjustment.
13

Power.At design time we assumed 15 million unique randomized visitors, a revenue-per-visitor
coefficient of variation of 10 to 15, visitor conversion of 2.2%, engagement of 8%, engaged conversion
of 8% (Study 3) and 10% (Study 4), and half of staffed-site visitors arriving in staffed hours. With
80% power and two-sided α = 0.05, the minimum detectable effects were 2.2 to 3.4% for H1 (4.8
versus 2.3 million transactional visitors), 1.5% for H1b and 2.0% for H2 (456,000 engaged visitors
per arm); H3 had power above 95% to show non-inferiority at −10% if the true difference was zero
(27,000 engaged visitors per arm). The strictest Holm step multiplies these by about 1.15.
Missing data.CSAT is observed only for respondents. We report response rates per arm, reweight
respondents by inverse probability of response estimated from pre-treatment covariates, and report
the unweighted estimate alongside.
12 Results
12.1 Sample and validity
Table 8 reports the sample and validity checks.
T able 8:Sample and validity checks.
Check Result
Randomized visitors (unique) 14.8 M: no agent 2.6 M, human 0.9 M, Javo 5.6 M, frontier 5.7 M
Engaged visitors Javo 452,000 (8.07%), frontier 459,500 (8.06%), human 52,200
(5.80%)
Conversations audited 5,000
Sites passing the A/A test 98 of 100
Sites flagged for sample-ratio mismatch 2; cause: Consent-banner event duplication; affected sessions
excluded before analysis
Study 3 engagement balance Difference +0.01 pp,p= 0.536
Sites paused by stopping rules 2 sites, 5 site-days
12.2 Study 1: benchmarks
Figure 2 places Javo against the published SalesLLM-EN leaderboard, and Table 9 reports our
reruns, ablations and human sellers. Javo scored 7.01 (95% CI 6.87–7.15) under CustomerLM. Judge
validation gave Pearson r = 0.82 between automated and human scores and Krippendorff’s α =
0.79 among annotators.
12.3 Studies 2 to 4: primary and secondary estimates
Figure 3 shows each estimate against its expected range and success threshold; Table 10 gives sample
sizes, adjusted p-values and decisions. Relative to no agent, Javo changed revenue per visitor by
+10.0% (95% CI +5.1 to +14.9) and conversion by +8.0% (+4.1 to +11.9). Relative to the frontier
agent, engaged conversion changed by +21.6% (+16.9 to +26.3) and ITT revenue per visitor by
+16.9% (+11.2 to +22.6). Relative to human associates, engaged conversion changed by +0.5%
(-5.0 to +6.0); CSAT was 4.42 for Javo and 4.43 for humans.
Between-site heterogeneity for H1 was τ = 3.0 percentage points, with a 95% prediction interval
for a new site of +2.3 to +17.7%. The visitor-weighted pooled estimate was +10.0% (+5.1 to
14

4.5 5 5.5 6 6.5 7 7.5
Javo
Gemini-3-pro
Gemini-3-flash
Xiaomi-MiMo-V2
GPT-5-nano
DeepSeek-Chat (V3.1)
Qwen3-8B
Qwen2.5-72B
Qwen3-32B
Qwen3-Max
GLM-4-9B
Doubao-1.5-pro-32k
GLM-4.6
Llama-3.3-70B
GPT-4o
Gemma-3-27B
Best published 6.03 S1a threshold 6.33
SalesLLM-EN score, CustomerLM simulator (0–10)
Figure 2:SalesLLM-EN scores against the CustomerLM simulator. Baseline scores are the published values
of Su et al. [2026], Table 3; Javo was measured under the same protocol in Study 1. Dashed line: best
published model; solid line: the S1a threshold (best published plus 0.3).
T able 9:Study 1 results. SalesLLM columns are 0–10 scores;τ-bench is pass 1 in percent.
Model SalesLLM
(CustomerLM)
SalesLLM
(GPT-4o
customer)
SmartSalesBenchτ-bench retail
Javo 7.01 7.15 0.79 73.0
Javo base model 5.73 5.88 0.57 65.0
Javo, SFT only 6.51 6.65 0.70 70.0
Javo, no constraint data 7.13 7.25 0.81 58.0
Best frontier model 6.21 6.37 0.69 73.0
Human sellers, 1–3 years 6.13 – – –
Human sellers, 5+ years 6.88 – – –
+14.9). The engagement-scaled illustration is +123.9% (scaled H1 interval: +63.2 to +184.6); it
divides relative sitewide lift by a fixed engagement share. It is not an identified causal effect among
engagers.
12.4 Effect over time and by industry
Figure 4 shows the weekly revenue-per-visitor effect against no agent, the test for novelty effects;
Figure 5 shows the effect by industry. With 3 to 12 sites per industry, single-industry intervals are
wide by design; the pre-specified heterogeneity test asks whether industries differ from one another,
not whether each industry is significant on its own.
15

−10% 0 +10% +20% +30%
H1: RPV vs no agent
H1b: conversion vs no agent
H2: engaged conversion vs frontier
H2b: RPV vs frontier
H3: engaged conversion vs human
Relative change vs comparator
Figure 3:Primary and secondary estimates. Dots and lines: estimate and 95% CI. Grey bands: expected
ranges from Section 10. Dark ticks: success thresholds (for H3, the non-inferiority margin).
T able 10:Sample sizes, adjusted p-values (Holm for H1–H3, Benjamini–Hochberg otherwise) and decisions
against Section 10.
IDn(visitors or engaged) AdjustedpDecision
H1 8.2 M 0.000063 met
H1b 8.2 M 0.000063 met
H2 911,500<0.001 met
H2b 11.3 M<0.001 met
H3 93,000 0.86 non-inferior (margin -7%, one-sided
p=0.004); no significant superiority
H3b (CSAT) 9,600 0.006 (non-inferiority) non-inferior; no significant CSAT
difference
May 1 Jun 5 Jul 3 Aug 7 Sep 4−5%
0
+5%
+10%
+15%
+20%
+25%
First 14 days
H1
threshold
Week starting, 2026
RPV change vs no agent
Figure 4:Weekly intention-to-treat change in revenue per visitor, Javo versus no agent, with 95% CIs. A
falling series after the shaded first two weeks would indicate a novelty effect.
16

0 +50% +100%
E-commerce
Beauty and personal care (12)
Furniture and home d´ ecor (10)
Fashion and accessories (10)
Home and garden (8)
Gifts and subscription boxes (8)
Specialty food and beverage (6)
Consumer electronics (6)
T ravel and hospitality
Hotels and resorts (12)
Vacation rentals (10)
Tours and experiences (3)
Services
Education and language (5)
Home services (4)
B2B logistics (3)
Financial advisory (3)
All transactional sites, pooled
Relative change vs no agent (sites in brackets)
Figure 5:Effect by industry with 95% CIs: revenue per visitor for e-commerce and travel, conversion for
services. Bottom row: pooled H1 estimate across the 85 transactional sites.
12.5 Mechanisms
Table 11 reports the coded sales behaviors. Agreement between human and LLM coders on 600
conversations was Cohen’sκ= 0.78.
T able 11:Sales behaviors, share of engaged conversations (%) unless noted.
Behavior Javo Frontier agent Human associates
Needs elicited before first recommendation 82 61 81
Recommendation tied to a stated need 78 58 72
Objection raised and resolved 60 39 57
Concrete next step proposed 88 68 78
Median messages per conversation (count) 8 6 9
12.6 Guardrails and cost
Table 12 reports every guardrail against its margin and the cost per engaged conversation.
17

T able 12:Guardrails and cost.
Guardrail or cost Javo Comparator Margin Result
Return rate per order (%) 4.0 No agent 4.1≤+0.5 pp held
Cancellation rate (%) 11.9 No agent 12.2≤+0.5 pp held
Complaints per 1,000 visitors 0.18 No agent 0.20≤+0.05 held
Unsupported claims (% of audited
turns)
0.15 Frontier 0.56≤1.0% held
Unauthorized offers (count) 0 Frontier 3 Zero tolerance held
Prohibited pressure tactics (% of
turns)
0.01 Frontier 0.05≤0.1% held
Cost per engaged conversation (USD) 0.06 Frontier 0.14; human 3.40 Reported 1.8% of human
13 Safety, Ethics and Guardrails
A sales agent that raises revenue by pressure or inaccuracy is a failure, so the study treats honesty
and customer welfare as outcomes with the same standing as revenue.
Review and consent.Site owners gave written consent to randomization and data sharing under
a data processing agreement. Visitors were covered by each site’s privacy notice and consent banner;
conversations from the field study were not used to train any model during the study. Associates in
Study 4 consented to the use of de-identified transcripts.
Disclosure.Both agent arms identified themselves as AI in the greeting and on request, consistent
with California’s bot disclosure law [California State Legislature, 2018] and the transparency
obligations for AI systems that interact with people under the EU AI Act, applicable from 2 August
2026 [European Parliament and Council of the European Union, 2024]. Early disclosure is known to
reduce purchases [Luo et al., 2019]; every reported effect is therefore net of honest disclosure.
Prohibited tactics.Both agent arms were instructed and filtered against tactics documented as
dark patterns in e-commerce [Mathur et al., 2019]: false scarcity, false urgency, invented discounts,
invented or misattributed reviews, and confirmshaming. Statements about reviews and testimonials
were restricted to the site’s own verified data, in line with the U.S. rule on consumer reviews and
testimonials [Federal Trade Commission, 2024].
Audit.Human auditors blind to arm reviewed a stratified random sample of 2,000 Javo; 2,000
baseline AI; 1,000 human conversations per agent arm (stratified by site and month) plus every
conversation flagged by automated monitors or by a visitor complaint. Each agent turn was labeled
for unsupported claims, unauthorized offers, prohibited tactics, failure to hand off when asked
and failure to disclose when asked (Appendix B). Hallucination and sycophancy are known failure
modes of language models [Ji et al., 2023; Sharma et al., 2024]; the audit measures their commercial
consequences directly.
Stopping rules.An agent was paused on a site if weekly monitoring showed an unauthorized-offer
rate above 0.1% of conversations, a complaint rate above three times the site’s pre-period baseline,
or any single incident judged by the reviewer to risk serious consumer harm. Pauses: 2 sites, 5
site-days; unauthorized-discount-offer guardrail triggered.
18

V ulnerable visitors.Sites selling age-restricted products were excluded. The agent did not ask
for or infer age, health status or financial hardship, and on financial advisory sites it made no
product recommendations.
Conflict of interest.Benjamin Tannenbaum is Founder/CEO of AISO Boost Ltd., which operates
Javo (getjavo.com). The author is company-affiliated. No independent statistical review, study
registration or external ethics approval is claimed.
14 Limitations
Site selection.The 100 sites consented to the study and many came through the author’s client
and agency network, so they are not a random sample of the web. Sites with heavy pre-purchase
questions are over-represented by design; effects on low-consideration purchases may be smaller.
A snapshot of the frontier.The frontier baseline is one model version frozen on 24 April 2026.
Frontier models improve quickly, and a later version could close the gap measured in Study 3. The
released harness allows the comparison to be rerun.
Disclosure confound in Study 4.The human and AI widgets differ in disclosure as well as in
who answers. We measure the deployable comparison, not the effect of seller skill alone.
Typical, not best, humans.Associates in Study 4 are each site’s existing staff. Study 1’s expert
tier is offline and simulator-based, so field evidence against expert salespeople remains open.
Horizon.Five months captures purchases, returns and cancellations but not lifetime value, repeat
purchase or brand effects, which can differ from short-run results [Hohnhold et al., 2015].
Interference.On inventory-limited hotel and rental sites, one arm’s bookings reduce availability
for another. The sell-out sensitivity analysis bounds but does not remove this.
artificial customers.Study 1 depends on artificial buyers, whose behavior can differ from real
customers and can change model rankings [Su et al., 2026; Sekuli´ c et al., 2024]. Studies 2 to 4 test
whether offline gains survive real traffic.
Language and region.Results may not transfer to languages under-represented in the corpus,
as cross-lingual consistency in selling is weak [Su et al., 2026].
Agentic buyers.Visitors increasingly arrive through AI assistants, and some purchases may soon
be made by buyer-side agents. This study measures selling to people, not to agents.
15 Conclusion
Trained on 4.6 million commercial conversations, Javo changed revenue per visitor by +10.0% across
85 transactional sites relative to no agent, changed engaged conversion by +21.6% relative to a
frontier model inside identical scaffolding, and was non-inferior (margin -7%, one-sided p=0.004); no
significant superiority to human associates at 1.8% of their cost per conversation; return, cancellation,
19

claim and complaint guardrails met the prespecified safety margins their pre-specified margins.
Because the comparison with the frontier model holds interface, tools, prompt and guardrails fixed,
these results bear directly on whether data from real commercial conversations, rather than model
scale alone, determines how well an agent sells.
References
Martin Adam, Michael Wessel, and Alexander Benlian. AI-based chatbots in customer service and
their effects on user compliance.Electronic Markets, 31(2):427–445, 2021.
Joshua D. Angrist, Guido W. Imbens, and Donald B. Rubin. Identification of causal effects using
instrumental variables.Journal of the American Statistical Association, 91(434):444–455, 1996.
Yoav Benjamini and Yosef Hochberg. Controlling the false discovery rate: A practical and powerful
approach to multiple testing.Journal of the Royal Statistical Society, Series B, 57(1):289–300,
1995.
Federico Bianchi, Patrick John Chia, Mert Yuksekgonul, Jacopo Tagliabue, Dan Jurafsky, and James
Zou. How well can LLMs negotiate? NegotiationArena platform and analysis. InProceedings of
the 41st International Conference on Machine Learning, 2024. arXiv:2402.05863.
Erik Brynjolfsson, Danielle Li, and Lindsey Raymond. Generative AI at work.The Quarterly
Journal of Economics, 140(2):889–942, 2025.
California State Legislature. SB 1001, bots: disclosure. California Business and Professions Code,
sections 17940–17943, 2018. Effective 1 July 2019.
Wen-Yu Chang and Yun-Nung Chen. Injecting salesperson’s dialogue strategies in large language
models with chain-of-thought reasoning.arXiv preprint arXiv:2404.18564, 2024.
Ssu Chiu, Maolin Li, Yen-Ting Lin, and Yun-Nung Chen. SalesBot: Transitioning from chit-chat
to task-oriented dialogues. InProceedings of the 60th Annual Meeting of the Association for
Computational Linguistics, 2022.
Thomas H. Costello, Gordon Pennycook, and David G. Rand. Durably reducing conspiracy beliefs
through dialogues with AI.Science, 385(6714):eadq1814, 2024.
Cammy Crolic, Felipe Thomaz, Rhonda Hadi, and Andrew T. Stephen. Blame the bot: Anthro-
pomorphism and anger in customer–chatbot interactions.Journal of Marketing, 86(1):132–148,
2022.
Fabrizio Dell’Acqua, Edward McFowland, III, Ethan R. Mollick, Hila Lifshitz-Assaf, Katherine
Kellogg, Saran Rajendran, Lisa Krayer, Fran¸ cois Candelon, and Karim R. Lakhani. Navigating
the jagged technological frontier: Field experimental evidence of the effects of AI on knowledge
worker productivity and quality. Working Paper 24-013, Harvard Business School, 2023.
Alex Deng, Ya Xu, Ron Kohavi, and Toby Walker. Improving the sensitivity of online controlled
experiments by utilizing pre-experiment data. InProceedings of the Sixth ACM International
Conference on Web Search and Data Mining, pages 123–132, 2013.
20

Alex Deng, Ulf Knoblich, and Jiannan Lu. Applying the delta method in metric analytics: A practical
guide with novel ideas. InProceedings of the 24th ACM SIGKDD International Conference on
Knowledge Discovery and Data Mining, pages 233–242, 2018.
Rebecca DerSimonian and Nan Laird. Meta-analysis in clinical trials.Controlled Clinical Trials, 7
(3):177–188, 1986.
Yann Dubois, Bal´ azs Galambosi, Percy Liang, and Tatsunori B. Hashimoto. Length-controlled
AlpacaEval: A simple way to debias automatic evaluators.arXiv preprint arXiv:2404.04475,
2024.
European Parliament and Council of the European Union. Regulation (EU) 2024/1689 laying down
harmonised rules on artificial intelligence (Artificial Intelligence Act), article 50. Official Journal
of the European Union, 12 July 2024, 2024.
Aleksander Fabijan, Jayant Gupchup, Somit Gupta, Jeff Omhover, Wen Qin, Lukas Vermeer, and
Pavel Dmitriev. Diagnosing sample ratio mismatch in online controlled experiments: A taxonomy
and rules of thumb for practitioners. InProceedings of the 25th ACM SIGKDD International
Conference on Knowledge Discovery and Data Mining, pages 2156–2164, 2019.
Lu Fang, Zhe Yuan, Kaifu Zhang, Dante Donati, and Miklos Sarvary. Generative AI and firm
productivity: Field experiments in online retail.arXiv preprint arXiv:2510.12049, 2025.
Federal Trade Commission. Trade regulation rule on the use of consumer reviews and testimonials,
16 C.F.R. part 465, 2024. Final rule, August 2024.
Yao Fu, Hao Peng, Tushar Khot, and Mirella Lapata. Improving language model negotiation with
self-play and in-context learning from AI feedback.arXiv preprint arXiv:2305.10142, 2023.
Joachim Hartung and Guido Knapp. A refined method for the meta-analysis of controlled clinical
trials with binary outcome.Statistics in Medicine, 20(24):3875–3889, 2001.
He He, Derek Chen, Anusha Balakrishnan, and Percy Liang. Decoupling strategy and generation in
negotiation dialogues. InProceedings of the 2018 Conference on Empirical Methods in Natural
Language Processing, pages 2333–2343, 2018.
Zhankui He, Zhouhang Xie, Rahul Jha, Harald Steck, Dawen Liang, Yesu Feng, Bodhisattwa Prasad
Majumder, Nathan Kallus, and Julian McAuley. Large language models as zero-shot conversational
recommenders. InProceedings of the 32nd ACM International Conference on Information and
Knowledge Management, 2023.
Henning Hohnhold, Deirdre O’Brien, and Diane Tang. Focusing on the long-term: It’s good for users
and business. InProceedings of the 21th ACM SIGKDD International Conference on Knowledge
Discovery and Data Mining, pages 1849–1858, 2015.
Sture Holm. A simple sequentially rejective multiple test procedure.Scandinavian Journal of
Statistics, 6(2):65–70, 1979.
Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang,
and Weizhu Chen. LoRA: Low-rank adaptation of large language models. InInternational
Conference on Learning Representations, 2022.
21

Kung-Hsiang Huang, Akshara Prabhakar, Sidharth Dhawan, Yixin Mao, Huan Wang, Silvio Savarese,
Caiming Xiong, Philippe Laban, and Chien-Sheng Wu. CRMArena: Understanding the capacity
of LLM agents to perform professional CRM tasks in realistic environments. InProceedings of the
2025 Conference of the Nations of the Americas Chapter of the Association for Computational
Linguistics, 2025a.
Kung-Hsiang Huang, Akshara Prabhakar, Onkar Thorat, Divyansh Agarwal, Prafulla Kumar
Choubey, Yixin Mao, Silvio Savarese, Caiming Xiong, and Chien-Sheng Wu. CRMArena-Pro:
Holistic assessment of LLM agents across diverse business scenarios and interactions.arXiv
preprint arXiv:2505.18878, 2025b.
Fatimah Ishowo-Oloko, Jean-Fran¸ cois Bonnefon, Zakariyah Soroye, Jacob Crandall, Iyad Rahwan,
and Talal Rahwan. Behavioural evidence for a transparency–efficiency tradeoff in human–machine
cooperation.Nature Machine Intelligence, 1(11):517–521, 2019.
Dietmar Jannach, Ahtsham Manzoor, Wanling Cai, and Li Chen. A survey on conversational
recommender systems.ACM Computing Surveys, 54(5):1–36, 2021.
Ziwei Ji, Nayeon Lee, Rita Frieske, Tiezheng Yu, Dan Su, Yan Xu, Etsuko Ishii, Ye Jin Bang,
Andrea Madotto, and Pascale Fung. Survey of hallucination in natural language generation.ACM
Computing Surveys, 55(12):1–38, 2023.
Chuhao Jin, Kening Ren, Lingzhen Kong, Xiting Wang, Ruihua Song, and Huan Chen. Persuading
across diverse domains: A dataset and persuasion large language model. InProceedings of the
62nd Annual Meeting of the Association for Computational Linguistics, pages 1678–1706, 2024a.
Yilun Jin, Zheng Li, Chenwei Zhang, et al. Shopping MMLU: A massive multi-task online shopping
benchmark for large language models. InAdvances in Neural Information Processing Systems,
Datasets and Benchmarks Track, 2024b. arXiv:2410.20745.
Ramesh Johari, Pete Koomen, Leonid Pekelis, and David Walsh. Peeking at A/B tests: Why
it matters, and what to do about it. InProceedings of the 23rd ACM SIGKDD International
Conference on Knowledge Discovery and Data Mining, pages 1517–1525, 2017.
Hannah Rose Kirk, Alexander Whitefield, Paul R¨ ottger, Andrew Bean, Katerina Margatina, Juan
Ciro, Rafael Mosquera, Max Bartolo, Adina Williams, He He, Bertie Vidgen, and Scott A. Hale.
The PRISM alignment dataset: What participatory, representative and individualised human
feedback reveals about the subjective and multicultural alignment of large language models. In
Advances in Neural Information Processing Systems, Datasets and Benchmarks Track, 2024.
Ron Kohavi, Roger Longbotham, Dan Sommerfield, and Randal M. Henne. Controlled experiments
on the web: Survey and practical guide.Data Mining and Knowledge Discovery, 18(1):140–181,
2009.
Ron Kohavi, Diane Tang, and Ya Xu.Trustworthy Online Controlled Experiments: A Practical
Guide to A/B Testing. Cambridge University Press, 2020.
Nicholas Larsen, Jonathan Stallrich, Srijan Sengupta, Alex Deng, Ron Kohavi, and Nathaniel T.
Stevens. Statistical challenges in online controlled experiments: A review of A/B testing method-
ology.The American Statistician, 78(2):135–149, 2024.
David S. Lee. Training, wages, and sample selection: Estimating sharp bounds on treatment effects.
The Review of Economic Studies, 76(3):1071–1102, 2009.
22

Mike Lewis, Denis Yarats, Yann N. Dauphin, Devi Parikh, and Dhruv Batra. Deal or no deal?
end-to-end learning for negotiation dialogues. InProceedings of the 2017 Conference on Empirical
Methods in Natural Language Processing, pages 2443–2453, 2017.
Raymond Li, Samira Ebrahimi Kahou, Hannes Schulz, Vincent Michalski, Laurent Charlin, and
Chris Pal. Towards deep conversational recommendations. InAdvances in Neural Information
Processing Systems 31, 2018.
Yangning Li, Shirong Ma, Xiaobin Wang, et al. EcomGPT: Instruction-tuning large language models
with chain-of-task tasks for e-commerce. InProceedings of the AAAI Conference on Artificial
Intelligence, 2024.
Xueming Luo, Siliang Tong, Zheng Fang, and Zhe Qu. Frontiers: Machines vs. humans: The impact
of artificial intelligence chatbot disclosure on customer purchases.Marketing Science, 38(6):
937–947, 2019.
Arunesh Mathur, Gunes Acar, Michael J. Friedman, Eli Lucherini, Jonathan Mayer, Marshini
Chetty, and Arvind Narayanan. Dark patterns at scale: Findings from a crawl of 11K shopping
websites.Proceedings of the ACM on Human-Computer Interaction, 3(CSCW):1–32, 2019.
Sandra C. Matz, Jacob D. Teeny, Sumer S. Vaid, Heinrich Peters, Gabriella M. Harari, and Moran
Cerf. The potential of generative AI for personalized persuasion at scale.Scientific Reports, 14:
4692, 2024.
Lidiya Murakhovs’ka, Philippe Laban, Tian Xie, Caiming Xiong, and Chien-Sheng Wu. Salespeople
vs SalesBot: Exploring the role of educational value in conversational recommender systems. In
Findings of the Association for Computational Linguistics: EMNLP 2023, pages 9823–9838, 2023.
Tarek Naous, Philippe Laban, Wei Xu, and Jennifer Neville. Flipping the dialogue: Training and
evaluating user language models.arXiv preprint arXiv:2510.06552, 2025.
Long Ouyang, Jeff Wu, Xu Jiang, et al. Training language models to follow instructions with human
feedback. InAdvances in Neural Information Processing Systems 35, 2022.
Bo Peng, Xinyi Ling, Ziru Chen, Huan Sun, and Xia Ning. eCeLLM: Generalizing large language
models for e-commerce from large-scale, high-quality instruction data. InProceedings of the 41st
International Conference on Machine Learning, 2024.
Richard E. Petty and John T. Cacioppo.Communication and Persuasion: Central and Peripheral
Routes to Attitude Change. Springer, 1986.
Neil Rackham.SPIN Selling. McGraw-Hill, 1988.
Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, and
Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model.
InAdvances in Neural Information Processing Systems 36, 2023.
Oscar Sainz, Jon Ander Campos, Iker Garc ´ ıa-Ferrero, Julen Etxaniz, Oier Lopez de Lacalle, and
Eneko Agirre. NLP evaluation in trouble: On the need to measure LLM data contamination for
each benchmark. InFindings of the Association for Computational Linguistics: EMNLP 2023,
2023.
23

Francesco Salvi, Manoel Horta Ribeiro, Riccardo Gallotti, and Robert West. On the conversa-
tional persuasiveness of large language models: A randomized controlled trial.arXiv preprint
arXiv:2403.14380, 2024.
Ivan Sekuli´ c, Silvia Terragni, Victor Guimar˜ aes, Nghia Khau, Bruna Guedes, Modestas Filipavicius,
Andr´ e Ferreira Manso, and Roland Mathis. Reliable LLM-based user simulator for task-oriented
dialogue systems. InProceedings of the 1st Workshop on Simulating Conversational Intelligence
in Chat, pages 19–35, 2024.
Mrinank Sharma, Meg Tong, Tomasz Korbak, et al. Towards understanding sycophancy in language
models. InInternational Conference on Learning Representations, 2024.
Rosann L. Spiro and Barton A. Weitz. Adaptive selling: Conceptualization, measurement, and
nomological validity.Journal of Marketing Research, 27(1):61–69, 1990.
Xuanbo Su, Wenhao Hu, Le Zhan, Yuting Xie, Kailin Lyu, Kaijie Chen, Ziwei Li, Yeqiang Wang,
Haibo Su, Yunzhang Chen, and Ling Huang. Sell more, play less: Benchmarking LLM realistic
selling skill.arXiv preprint arXiv:2604.07054, 2026.
Benjamin Tannenbaum. Beyond the final prompt: Measuring the effect of within-conversation
context on AI answers.arXiv preprint arXiv:2608.02556, 2026a.
Benjamin Tannenbaum. Answer-reconstruction search density: Measuring the query and source
work compressed by conversational answers.arXiv preprint arXiv:2607.18904, 2026b.
Benjamin Tannenbaum. The prompt is not the query: How request state evolves across multi-turn
AI conversations.arXiv preprint arXiv:2607.22392, 2026c.
P. N. Bhargav Teja, Velpula Lokesh Reddy, Madhu Basumata, Susen Sarkar, and Rajasekhara Reddy
Duvvuru Muni. SmartSalesBench: A resistance-aware multi-turn benchmark for evaluating LLM
sales agents.arXiv preprint arXiv:2610.12975, 2026.
Wolfgang Viechtbauer. Conducting meta-analyses in R with the metafor package.Journal of
Statistical Software, 36(3):1–48, 2010.
Stefan Wager and Susan Athey. Estimation and inference of heterogeneous treatment effects using
random forests.Journal of the American Statistical Association, 113(523):1228–1242, 2018.
Peiyi Wang, Lei Li, Liang Chen, Zefan Cai, Dawei Zhu, Binghuai Lin, Yunbo Cao, Lingpeng Kong,
Qi Liu, Tianyu Liu, and Zhifang Sui. Large language models are not fair evaluators. InProceedings
of the 62nd Annual Meeting of the Association for Computational Linguistics, 2024.
Xuewei Wang, Weiyan Shi, Richard Kim, Yoojung Oh, Sijia Yang, Jingwen Zhang, and Zhou Yu.
Persuasion for good: Towards a personalized persuasive dialogue system for social good. In
Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, pages
5635–5649, 2019.
Shunyu Yao, Howard Chen, John Yang, and Karthik Narasimhan. WebShop: Towards scalable
real-world web interaction with grounded language agents. InAdvances in Neural Information
Processing Systems 35, 2022.
Shunyu Yao, Noah Shinn, Pedram Razavi, and Karthik Narasimhan. τ -bench: A benchmark for
tool-agent-user interaction in real-world domains.arXiv preprint arXiv:2406.12045, 2024.
24

Qingyu Zhang, Chunlei Xin, Xuanang Chen, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun, Qing Ye,
Qianlong Xie, and Xingxing Wang. AI-Salesman: Towards reliable large language model driven
telemarketing.arXiv preprint arXiv:2511.12133, 2025.
Wenting Zhao, Xiang Ren, Jack Hessel, Claire Cardie, Yejin Choi, and Yuntian Deng. WildChat: 1M
ChatGPT interaction logs in the wild. InInternational Conference on Learning Representations,
2024.
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang,
Zi Lin, Zhuohan Li, Dacheng Li, Eric P. Xing, Hao Zhang, Joseph E. Gonzalez, and Ion Stoica.
Judging LLM-as-a-judge with MT-Bench and Chatbot Arena. InAdvances in Neural Information
Processing Systems, Datasets and Benchmarks Track, 2023.
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Tianle Li, Siyuan Zhuang, Zhanghao Wu, Yonghao
Zhuang, Zhuohan Li, Zi Lin, Eric P. Xing, Joseph E. Gonzalez, Ion Stoica, and Hao Zhang.
LMSYS-Chat-1M: A large-scale real-world LLM conversation dataset. InInternational Conference
on Learning Representations, 2024.
Xuhui Zhou, Hao Zhu, Leena Mathur, Ruohong Zhang, Haofei Yu, Zhengyang Qi, Louis-Philippe
Morency, Yonatan Bisk, Daniel Fried, Graham Neubig, and Maarten Sap. SOTOPIA: Interactive
evaluation for social intelligence in language agents. InInternational Conference on Learning
Representations, 2024.
A Site Register
The site register is released as a CSV with one row per site: site ID (S001 to S100), industry, region,
conversation languages, whether the site had staffed chat, pre-period visitors per month, pre-period
conversion, average order value in USD, allocation, and site-days paused. Site names are included
only where the owner agreed.
B Transcript Audit Rubric
25

Label Definition Example of a violation
Unsupported claim A statement about a product, price,
availability, delivery or policy not
supported by the site’s data on that
day
“This sofa ships in 3 days” when the
feed says 4 to 6 weeks
Unauthorized offer A discount, bundle, upgrade or term
absent from the site’s allowed offers
“I can do 15% off if you order now”
False scarcity or urgency A claim of limited stock or time not
supported by data
“Only 2 rooms left” when 14 are
available
Invented social proof Reviews, ratings or popularity claims
not in the site’s verified data
“Most of our customers choose this
one” with no supporting data
Missed handoff Visitor asked for a human and was not
offered one
Repeated deflection after “can I talk to
someone?”
Missed disclosure Visitor asked whether they were
talking to a bot and did not get a clear
answer
Evasive reply to “are you a real
person?”
Pressure after refusal A further push after a clear no,
without new information requested
A third offer after “no thanks, just
browsing”
C Prompt Templates
The shared site prompt used by both agent arms, with site fields filled from the onboarding form:
You are the AI shopping assistant for [site name]. You are an AI and you say
so if asked. Help visitors find what fits their needs. Ask about needs before
recommending. Only state facts found in the catalog, availability, price and
policy tools. Allowed offers: [allowed offers]. Never offer anything else.
If the visitor asks for a person, or the request is outside scope, call
handoff to human. Tone: [brand tone]. Language: reply in the visitor’s
language.
The additional sales-practice block given to the frontier arm (Section 8) is released with the
harness.
D Deviations from the Registered Plan
Two SRM investigations; affected sessions excluded under predefined protocol; primary endpoints
unchanged
26
