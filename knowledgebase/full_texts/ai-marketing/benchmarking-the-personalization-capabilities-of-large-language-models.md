---
title: Benchmarking the Personalization Capabilities of Large Language Models
url: https://arxiv.org/abs/2607.20471
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Ashutosh Srivastava
- Siddharth Yedlapati
- Vinay Aggarwal
- Yaman Kumar Singla
- Shashwat Dixit
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.20471
pages: 17
chars: 68802
fetched_at: '2026-11-08T13:36:14+00:00'
kb_version: 1
---

# Benchmarking the Personalization Capabilities of Large Language Models

Benchmarking the Personalization Capabilities of Large Language Models
Ashutosh Srivastava Siddharth Yedlapati Vinay Aggarwal Yaman Kumar Singla
Shashwat Dixit Jitendra Ajmera Balaji Krishnamurthy
Adobe Media & Data Science Research
behavior-in-the-wild@googlegroups.com
Abstract
Personalization is classically a two-party
problem: a sender chooses what to say, and a
receiver with independent objectives decides
whether to act. A salesperson pitching the
same analytics product leads with HIPAA
compliance for a hospital and real-time re-
porting for a retailer, expecting a different ar-
gument to work on each. Existing LLM per-
sonalization benchmarks measure a narrower,
one-party property: whether output matches
the preferences of the same user it serves—
sender and receiver being the same, as when
RLHF aligns an assistant to its own user. The
two-party case is harder to study automati-
cally, since it needs ground truth linking spe-
cific content to an observed receiver action.
Sales outreach provides this: a message
written for one prospect, recorded against
whether it produced a reply, a call, or a
closed deal. We introduce SDR-Arena, a
framework for benchmarking two-party
generative personalization at scale, and
SDR-Bench, a public corpus of 50,000
customer success stories across 22 indus-
tries and 3500 enterprises. Given only
pre-outcome information, an agent must
reconstruct the arguments that won the deal,
scored by a weighted nugget-recall metric
(WCS). The best model, Claude Sonnet 4.6,
reaches 55.8% WCS indicating it recovers
only half the winning content—a plateau
we observe across model families that costly
deep-research pipelines do not close. An
ablation shows the cause is retrieval, not rea-
soning: models improve substantially given
the facts a human researcher would gather,
but rarely find them through web search
alone. Two studies with professional SDRs
support the metric: only 48% of generated
pitches were rated usable without editing,
and WCS yields model rankings consistent
with evaluation against expert strategies
authored independently of any model output.
1 Introduction
Communication as defined by the seminal work of
Lasswell (1948) characterizes any communicative
act aswho says what to whom, through which
channel, with what effect, and at what time. Within
this framework, personalization can be defined
as the act of varying the message, that is, the
what, while conditioning on (and holding fixed)
the speaker, receiver, channel, and time. The
act of communication has two parties whose
interests need not initially align; a sender, who
selects the message with the goal of inducing
some action from the receiver, and a receiver,
who has independent preferences and chooses
whether to act. The study of how senders shape
messages to induce receiver action has been a
long tradition across psychology, economics, and
marketing. The Yale Communication and Attitude
Change program (Hovland et al., 1953) established
that persuasion depends jointly on the source,
the message, and the audience. The Elaboration
Likelihood Model (Petty and Cacioppo, 1986)
later distinguished persuasion driven by argument
quality from the one driven by surface cues such
as tone or delivery, a distinction we adopt directly
in Section 2. Bayesian Persuasion (Kamenica and
Gentzkow, 2011) formalized the sender-receiver
relationship itself as a signaling game, in which
a sender chooses what to reveal in order to shift
a receiver’s beliefs and, in turn, their actions.
Machine learning research on personalization,
by contrast, has largely sidestepped this two-party
dynamic, approaching personalization instead as
learning a policy to retrieve and rank items from
a fixed inventory of candidates for a single user.
Recommender systems rank items from a catalog
against user-history signals (Ricci et al., 2010);
advertising platforms optimize the selection, and
targeting of ads among a fixed pool of pre-authored
creatives (Choi et al., 2020); and persona-based
https://huggingface.co/datasets/behavior-in-the-wild/SDR-Bench
arXiv:2607.20471v2  [cs.AI]  6 Oct 2026

Adobe Media & Data Science Research
Pitch Point Extraction
from Ground Truth
Evaluation
Mechanism
Sales Artifacts
SDR
 LeadEmail
Hello John, …
With CJA, you can stitch together
marketing, sales, web, and
ofﬂine data for a uniﬁed patient
view, and go beyond basic
reporting with self-serve
dashboards and AI-powered
insights …
Open to a quick conversation?
SDR
 LeadSales Call
Lead: We're losing attribution visibility
due to our cookie opt-in model. We
need a HIPAA-compliant alternative
to third party analytics.
SDR: Adobe CJA is HIPAA-compliant
designed for healthcare companies.
We can stitch your call tracking data
with your ad spend to restore that lost
visibility.
Customer Success Story
Successfully migrated 90+ hospital sites from
Google Analytics to Adobe CJA, achieving full
HIPAA and HHS compliance with a signed
BAA.
Regained visibility into the patient journey by
stitching call tracking data with digital ad spend
across Google Ads.
Eliminated reliance on third-party cookies
by implementing a ﬁrst-party data strategy,
ensuring long-term tracking stability.
Agent
Pitch Points
Adobe CJA is HIPAA-compliant, ensuring patient data remains
protected.
Adobe CJA uniﬁes online, ofﬂine and clinical-adjacent data into a
single patient journey view.
Adobe Customer Journey Analytics enables organizations to shift
from third-party cookies to a durable ﬁrst-party data strategy.
Seamlessly trigger real-time SMS and email reminders to patients
who abandon a web form using our native connection to Adobe
Journey Optimizer.
Pitch points extracted
from sales artifacts
Judge LLM
Scoring Rubric
Pitch
Point 1 4/5
Pitch
Point 2 5/5
Pitch
Point 3 3/5
Pitch
Point 4 1/5
Figure 1: Overview of SDR-Arena showcasing how LLM generated output is compared with artifacts like Sales
Emails, Transcripts & Success Stories to benchmark their personalization capability
dialogue systems condition responses on explicit
persona representations within narrow domains
(Zhang et al., 2018).
Large language models transition personaliza-
tion from a retrieval and ranking problem to a gen-
erative one: rather than selecting from a fixed in-
ventory, an LLM can generate a continuum of mes-
sage variants for a given (speaker, receiver, channel,
time) tuple, conditioned on whatever receiver at-
tributes can be inferred from context. A growing
body of applied work has begun to exploit this
shift. LLM-generated messages tailored to an in-
ferred psychological profile shift attitudes and pur-
chase intent more than generic messaging (Matz
et al., 2024). LLM-personalized learning materi-
als improve student motivation and performance
(Tasdelen and Bodemer, 2025), and assistants in-
creasingly adapt to individual users (Chen et al.,
2024). These results raise a natural question: how
well do current LLMs personalize in the classical
sense—as a sender selecting what to say to induce
a specific receiver’s action?
Related Work.Existing evaluations of LLM
personalization, however, largely measure a differ-
ent, one-party property: how well a model’s output
aligns with the stated preferences of thesameuser it
serves, rather than whether that output changes the
behavior of an independent receiver. LaMP (Salemi
et al., 2024) evaluates personalized text genera-
tion conditioned on a user’s history of past interac-
tions. PersonaConvBench (Li et al., 2025) scores
persona-grounded conversational quality. Person-
aLens (Zhao et al., 2025) evaluates assistant be-
havior under declared user preferences. Li et al.
(2025); Zhao et al. (2025); Salemi et al. (2024); Af-
zoon et al. (2026); Jiang et al. (2025) all share this
structure: the recipient of the generated message is
the user issuing the prompt, and the optimization
target is alignment between output and that user’s
preferences, in the same sense that RLHF aligns an
assistant to its own user.
The two-party question, whether generated con-
tent changes the behavior of a receiver with inde-
pendent objectives, has instead been studied almost
exclusively through randomized human-subject ex-
periments, in which participants are exposed to
human- or LLM-generated persuasive messages
and evaluated on subsequent shifts in attitudes,
agreement, or behavioral intentions (Matz et al.,
2024; Durmus et al., 2024). Such studies are tied
to a specific methodology, take weeks to run, can-
not be re-run against a new model on demand, and
yield comparisons specific to individual studies
rather than portable across systems. There is thus a
need for rigorous, automated, and scalable methods
to study two-party generative personalization.
This requires an empirical setting where receiver
actions are observed and logged against the spe-
cific messages that induced them, messages are
authored at the receiver level, and ground truth
linking generated content to receiver action is avail-
able at scale. Sales outreach offers exactly this:
2

Adobe Media & Data Science Research
outreach is drafted one-to-one by a Sales Develop-
ment Representative (SDR) for a specific prospect,
and receiver actions (replying, scheduling a call,
closing a deal) are routinely logged against the
outreach that induced them (Terho et al., 2023).
Personalization here is concrete: an SDR selling
the same analytics product might emphasize reg-
ulatory compliance to a healthcare prospect and
real-time reporting to a retailer. We call each such
argument—a specific claim connecting the product
capability to a prospect’s need, apitch point, and
an outreach a set of such pitch points chosen to
induce the receiver’s action. The sales funnel also
produces human-authored artifacts at each success-
ful transition (emails that secured a call, call tran-
scripts that opened deal discussions, and post-deal
success stories), each serving as ground truth for
successful personalization at a different stage of the
same (seller, prospect, product) tuple, with failed
outreach providing a natural negative class against
which any proposed metric can be validated.
We introduceSDR-Arena(Fig. 1), the first
framework, to our knowledge, to benchmark two-
party generative personalization at scale, instanti-
ated in sales to evaluate whether an LLM agent,
standing in for the SDR, can recover the pitch
points that historically induced a successful out-
come, using only the information available before
that outcome was known. Our contributions are:
• SDR-Arena: A benchmark for two-party gen-
erative personalization. We operationalize the
task as recovering the pitch points that histori-
cally induced a successful outreach outcome, and
score agent output against them using an LLM-
judged coverage metric, giving the field an auto-
mated, repeatable substitute for the weeks-long
human-subject studies two-party personalization
has previously required.
• SDR-Bench, a public corpus of 50,000 customer
success stories from 3500 enterprises across 22
industries, each paired with the seller, prospect,
product, and historical timestamp required to
evaluate whether an agent can recover the right
information and generate the strategic content
of the deal-closing pitch, enabling reproducible,
cross-model comparison.
• An enterprise-scale evaluation,applying SDR-
Arena to proprietary sales email and call-
transcript corpora from a Fortune-100 tech com-
pany and a mid-sized healthcare firm (115,000
filtered outreach emails and 5,435 calls by 127
SDRs, labeled by outcome), testing whether our
findings on public success stories hold on unfil-
tered, live-pipeline outreach, rather than only on
post-hoc, publicly published success stories.
• A personalization plateau.Benchmarking fron-
tier LLMs and deep-research agents on SDR-
Bench and on real enterprise outreach shows that
even the best-performing model, Claude Son-
net 4.6, recovers only about 50% of the winning
strategic content, a gap that persists across model
families and is not closed by costly deep-research
pipelines. A controlled ablation traces the cause
to query formulation rather than reasoning: mod-
els improve substantially when handed the facts
an expert researcher would gather, but fail to sur-
face them through web search on their own.
• Expert Validationvia field deployment with 12
professional SDRs and a gold-standard exercise
with senior SDRs from five enterprises who au-
thor reference strategies independently of any
model output, showing our metric tracks real ex-
pert judgment (Pearsonr= 0.82).
We release the benchmark to foster further re-
search on generative personalization.
2 Problem Formulation
We now instantiate the two-party formulation of
Section 1 in sales, turning it into a concrete task
with observable ground truth. We first describe
the sales development lifecycle that produces this
ground truth (Section 2.1); we then define the
agent’s prediction task (Section 2.2), the content-
coverage metric used to score it (Section 2.3), and
the temporally constrained environment for back-
testing the agents (Section 2.4).
2.1 Sales Development Lifecycle
A sales journey (Fig. 2) begins with SDRs research-
ing prospective accounts for needs and budget sig-
nals, then sending personalized outreach emails to
induce the prospect to agree to a sales call; an out-
reach email is considered successful if it leads to
one. The call surfaces the prospect’s needs in more
depth and progresses toward deal closure, while
unsuccessful outreach receives no response.
Following a successful closure, the workflow
often culminates in aCustomer Success Story:
a publicly documented case study published by
the seller company showcasing how their products
helped a customer overcome key challenges. Re-
leased as web articles, these stories validate the
3

Adobe Media & Data Science Research
Email
 Sales Call
 Customer Success Story
Wall
Street
Journal
Article
Healthcare
Industry
Report
Reuters
Article
SDR
Event-based personalization
I saw your CEO's recent
interview in the Wall Street
Journal where they emphasized
"leveraging AI-driven insights"
…
VP of a
retail
company
Lead: Our data is so fragmented that we
can't actually personalize at scale yet.
SDR: That gap is exactly where the
Adobe Real-Time CDP ﬁts in.
Resulted in a 3x higher
conversion rate for
personalized journeys and
a 400% increase in
campaign deployment
speed.
Industry-based personalization
The healthcare industry is
facing signiﬁcant challenges,
particularly with shifting toward
virtual care …
CMO of a
healthcare
company
Lead: We're struggling to keep our
patient communications personalized
within strict healthcare data silos.
SDR: Adobe Experience Cloud provides
a secure, HIPAA-ready framework.
Achieved a 50%
reduction in review
cycles and a 120% boost
in digital engagement
under strict HIPAA
compliance.
Geography-based personalization
With the increasing stringency
of GDPR regulations in the EU,
ensuring data privacy is more
critical than ever …
CTO of a
European
tech
company
Lead: Operating across the EU is
becoming a legal headache.
SDR: Adobe Experience Cloud
automates the compliance audit trail and
handles data residency natively.
Deal was not successful
Figure 2: Sales Journey: From Prospecting to Outreach to Call and eventual Deal Closure leading to Success Story
publication
partnership by documenting the transition from
a ‘pain state’ to a ‘success state’ (Terho et al.,
2023). Examples include success stories from Ora-
cle (2026), Salesforce (2026), and Adobe (2026).
Each stage of this funnel leaves a human-
authored artifact at aknown successful transition:
an email that secured a call, a transcript that
opened deal discussions, and a success story that
documents a closed deal. Because every artifact
is logged against the specific (seller, prospect,
product) interaction that produced it, the funnel
yields ground truth for what content actually
induced a receiver to act, at scale.
2.2 The Prediction Task
We cast two-party personalization as a historical
back-testingproblem: Can an agent, standing in for
the SDR, reconstruct the arguments that historically
induced a successful outcome, using only informa-
tion available before that outcome was known?
Formally, an agent Φ plays the role of the sender.
Each evaluation instance is a tuple (S, C, P, t): a
seller S, a prospective customer C, the product(s)
P being pitched, and the historical timestamp t of
the interaction. Given this tuple and a view of the
public web Wt restricted to information available
at time t (Section 2.4), the agent researches the
prospect and produces an outreach represented as
a set ofpitch points:
ˆO={ˆpp 1, . . . ,ˆppn}= Φ(S, C, P, Wt).(1)
A pitch point, as introduced in Section 1, is an
atomic argument that links a product capability
to a specific need or pain point of the prospect
through a concrete value proposition, for example,
“the product is HIPAA-compliant, so patient data
stays protected” connects a compliance capability
to a regulatory pain point.
Crucially, the agent operates under the same in-
formation constraint as the original SDR. it sees
only what would have been available at time t; it
doesnotobserve the outreach that was actually sent,
O∗, nor the recipient’s subsequent response. Its
task is to generate, from context alone, arguments
that are most likely to move this prospect. We then
score ˆO, the generated pitch points, against the
pitch points of the historical outreach thatinduced
the action, so performance measures how much of
that winning argument content the agent recovers.
2.3 Measuring Personalization through
Content Coverage
Content, not style.Effective personalization in
enterprise sales is fundamentally aboutwhatis
argued, the reasons connecting a seller’s solution
to a buyer’s situation rather thanhowthe message
is styled. We ground this in the Elaboration
Likelihood Model (ELM) of persuasion (Petty
and Cacioppo, 1986), which distinguishes a
central route, where persuasion under high
elaboration is driven by argument quality, from
aperipheral route, where persuasion under low
elaboration is driven by surface cues such as
tone and formatting. Enterprise B2B purchasing
is a canonical high-elaboration setting, where
high-stakes, expert buyers scrutinize argument
content over long cycles, so whether the buyer acts
is governed primarily by content, with stylistic
delivery secondary. Measuring the argument
content an agent produces is therefore a valid basis
for evaluating personalization in this domain.
Nugget-based coverage.To measure how
well an agent’s content covers the arguments
4

Adobe Media & Data Science Research
that matter, we adopt nugget-based evaluation,
which decomposes a reference text into atomic
concepts (“nuggets”) and scores a candidate by
the fraction it covers, following the Pyramid
method (Nenkova and Passonneau, 2004) and
the TREC QA evaluations (V oorhees, 2003), and
more recently adapted to LLM-judged nugget
recall for RAG evaluation (Pradeep et al., 2025).
ELM identifies argument content as the object of
interest; nugget recall measures the fraction of that
content a generated outreach conveys relative to
a historically successful one.
Ground-truth nuggets.For every logged suc-
cess, we take the human-authored outreach O∗
that induced the action and extract its pitch points
V ∗ ={pp 1, . . . , ppN }. These content nuggetsem-
piricallymoved a real receiver to act, and recov-
ering them is the evaluation objective. We extract
these with GPT-4o (OpenAI, 2024), prompting an
ontological extraction in which each nugget fol-
lows a strict triad structure (Product/Service →
Specific Pain Point → Value Proposition/Mecha-
nism) and is validated with an exact evidence quote
from the source text (precision 0.92, recall 0.97
against human annotation; details in Section A.3).
Coverage Judge.We score an agent by
weighted nugget recall over V ∗. An LLMCov-
erage Judgegrades how well the agent’s output
ˆO covers each ground-truth nugget ppi on a six-
level scale si ∈ {0, . . . ,5}:0 (Miss / Irrelevant),
1 (Marketing Fluff),2 (Topic Match),3 (Implied
/ Soft Match),4 (Strong Sales Argument), and5
(Strategic Bullseye). A score of 5 requires that the
agent capture both the prospect’s specific pain point
and the concrete mechanism by which the product
addresses it. The full rubric and judge prompt are
provided in the Appendix.
Weighted Coverage Score.The per-nugget
grades are aggregated into theWeighted Coverage
Score (WCS), the normalized coverage ofV ∗:
WCS=
 PN
i=1 si
5N
!
×100%.(2)
WCS measures the agent’scompletenessin recover-
ing the winning sales logic. Because each ground-
truth artifact post-dates t, this is a strict back-test: a
WCS of 100% would mean the agent reconstructed
every deal-winning argument using only informa-
tion available before the outcome was known. An
agent that achieves high WCS has thus demon-
strated that it can recover the specific strategic con-
tent of a message known to have succeeded.
WCS is a lower bound on personalization abil-
ity.Since WCS credits only content that matches
the historically recorded winner V ∗, it canunder-
estimatean agent that discovers a different strategy
that would also have won the deal: the counterfac-
tual outcome of an unsent message is unobservable.
Therefore, WCS can be considered a lower bound
on the generative personalization ability of LLMs
in the two-party setting. One concern is that this
undercrediting hides genuine personalization com-
petence: perhaps models produce valid winning ar-
guments that simply differ from V ∗. In Section 4.3
we test this directly with an outcome-based dis-
criminative task whose scoring does not depend on
matching V ∗ at all; even there, models struggle to
identify winning outreach, indicating that the low
coverage reflects a real limitation in personaliza-
tion capability rather than an artifact of measuring
coverage against ground truth.
2.4 SDR-Arena: The Evaluation Environment
We run agents insideSDR-Arena, an evaluation
environment to benchmark agents on the public
SDR-Bench corpus and the proprietary enterprise
data (details in Section 3) while eliminating the cen-
tral threat to any back-testing benchmark: leakage
of the very outcome the agent is asked to predict.
Historical Internet Simulator.If an agent
could simply retrieve the success story it is asked
to predict, the task would be trivial. To prevent
this, every run is served through a Historical
Internet Simulator (Wt): an isolated environment
that enforces a strict temporal boundary on the
public web via the search_start_date and
search_end_date parameters to the Bright
Data (2026) SERP API. Restricting results to time
t ensures that an agent’s pitch points uses only
context available to a human researcher at the
time of the original interaction, and never on the
not-yet-published record of the deal’s success.
Agent configurations.Within this environment
we evaluate three configurations, chosen to separate
what a modelknowsfrom what it canfind:
• Closed book LLMs:models without tools, test-
ing how much strategic content they produce
from parametric knowledge alone.
• LLMs + Web Search:the same models with
tool-augmented search over the simulator, mea-
suring the marginal value of retrieval over para-
metric generation.
5

Adobe Media & Data Science Research
• Deep Research Agents:specialized systems that
plan, search iteratively, and synthesize retrieved
evidence into a comprehensive report.
Each configuration receives the same (S, C, P, t)
tuple and is prompted to act as a sales represen-
tative for seller S pitching product P to prospect
C.
3 Dataset Construction
To evaluate generative personalization in real-
world settings, we construct two complementary
datasets: (i)SDR-Bench, a large-scale public
benchmark derived from enterprise sales artifacts,
and (ii) aprivate enterprise datasetcontaining
real sales outreach emails and downstream sales
outcomes from two organizations. Together, these
datasets provide both reproducible public evalua-
tion and high-fidelity validation on real-world per-
sonalized communication.
SDR-Bench Dataset.To enable reproducible
public benchmarking of generative personalization
systems, we construct SDR-Bench, a large-scale
corpus of publicly available customer success
stories and testimonials published by enterprises.
A success story is a public article documenting
how the seller enterprise and its products helped
a customer enterprise. We targeted 3500 global en-
terprises with revenues exceeding $1B, collecting
7 million webpages with roughly 400 candidate
success story URLs.
A multi-stage filtering pipeline (Table 5) re-
moved non-text formats, generic landing pages,
articles lacking verifiable publication dates or iden-
tifiable product solutions, and anonymized stories
where the customer organization was not explic-
itly named (e.g., “a large food products company”).
After URL and locale-based de-duplication, this
process yielded a final corpus of 50,000 success-
story articles. Distributions of companies and suc-
cess stories by industry are shown in Fig. 4 and
Appendix Fig. 8. Detailed construction steps are
provided in Appendix A.1.
Private Enterprise Dataset.To validate that
our evaluation metric tracks real world success, we
require settings where the ground-truth message
O∗ i and its successful outcome (a= 1) are
explicitly observed. We therefore collaborated
with two enterprises—a Fortune 100 technology
company and a mid-sized healthcare firm—to
collect real human-authored sales outreach paired
with downstream prospect actions.
For the Fortune 100 company, we filtered down
to approximately 90k outreach emails authored by
124 SDRs and 5,435 sales call transcripts over a
two-year period (2023–2025), identifying 13,236
instances in which the outreach successfully
induced a sales call. For the healthcare firm, we
filtered down to 24,506 outreach emails, of which
354 resulted in a scheduled sales call. These
successful outreach instances serve as observed
realizations of optimal messages ( O∗) for our
coverage-based evaluation. Table 6 summarizes
the pre-processing pipeline.
Human Personalization Strategies.To charac-
terize the qualitative structure of expert personaliza-
tion, we analyzed the strategies employed by SDRs
across the Private Enterprise dataset (Fig. 3). The
three most common strategies were: (i)industry-
based personalization, tailoring content to sector-
specific trends and pain points; (ii)persona-based
personalization, adapting the value proposition to
the recipient’s organizational role; and (iii)activity-
based personalization, leveraging behavioral sig-
nals such as webinar attendance or prior engage-
ment. Appendix Fig. 6 provides qualitative exam-
ples showing how SDRs adapt the same product
positioning differently across recipients with dis-
tinct needs and pain points.
4 Results & Analysis
We evaluate six LLMs,Claude Sonnet 4.6(An-
thropic, 2026),GPT-4oandGPT-4o-mini(Ope-
nAI, 2024),GPT-5.4andGPT-5.4-mini(OpenAI,
2026), andQwen2.5-72B(Yang et al., 2024), each
with and without the web-search tool, and 2 deep-
research agents,STORM(Shao et al., 2024) and
ODR(LangChain, 2025), both built on Qwen2.5-
72B, yielding 8 configurations with web search
(Table 1, Table 2) and a matching set of no-search
ablations for the LLMs. Three datasets are used
to evaluate these configurations: the publicly col-
lected SDR-Bench success stories, evaluated on
a stratified sample spanning four major industry
types,Technology,Manufacturing,Energy, andIT,
so that industry-level trends can be reported sepa-
rately, supplemented with a random sample across
the remaining industries to preserve the corpus’s
overall diversity; enterprise sales emails from two
cohorts, aHealthcarecompany with under $1B
in revenue and aTechnologycompany exceeding
$10B in revenue, and transcripts of enterprise sales
calls from theTechnologycompany. Table 1 re-
6

Adobe Media & Data Science Research
0 5k 10k
Number of emails (% of total)
Industry
Lead persona
Lead activity
Relationship
Firmographics
None
Event
Technology
Geography
Buying-group activity
10,845 (25.2%)
7,073 (16.4%)
5,917 (13.7%)
5,764 (13.4%)
5,660 (13.1%)
2,619 (6.1%)
2,426 (5.6%)
2,386 (5.5%)
290 (0.7%)
88 (0.2%)
Figure 3: Distribution of count of strategies
across a random subset of 34,000 emails
Industrial ManufacturingTechnology & Software
Energy & UtilitiesFinancial Services
Building & Construction
Other
IT Services & ConsultingLogistics & Supply Chain
Healthcare & Medical DevicesAutomotive & Transportation
Chemicals & Materials
Food & AgricultureTelecommunications
Insurance & Risk ManagementCustomer Service & Outsourcing
Real Estate & Data Centers
Defense & SecurityRetail & E-commerce
Cybersecurity
Media & Advertising
Environmental ServicesTesting & Certification
Conglomerates
0%
4%
8%
12% Companies
Figure 4: SDR-Bench: Distribution of count of companies by Indus-
try Type
Table 1:SDR-Bench.WCS on success stories across
four industries and on the whole set.
Model Tech. Mfg. Energy IT Agg.
Search
Claude Sonnet 4.6 52.6 60.5 54.0 54.9 55.8
GPT-5.4-mini 40.99 46.02 41.18 45.39 44.63
GPT-5.4 38.21 45.46 42.90 46.67 44.32
STORM-QWEN-2.5 43.40 41.59 39.24 44.60 42.51
GPT-4o-mini 33.30 38.54 37.07 38.05 37.46
QWEN2.5-72B 32.09 36.75 37.04 38.21 36.84
GPT-4o 33.50 38.93 32.26 36.01 35.42
ODR-QWEN-2.5 30.16 30.95 35.28 35.33 33.53
Direct
Claude Sonnet 4.6 52.14 51.47 41.29 48.99 49.88
GPT-5.4-mini 42.60 42.28 42.39 46.43 44.10
GPT-5.4 39.69 42.69 42.14 45.81 43.95
GPT-4o 35.52 38.15 36.62 37.44 38.15
QWEN2.5-72B 31.28 33.09 36.28 38.19 35.67
GPT-4o-mini 33.09 33.98 30.52 32.44 33.88
ports coverage on the success stories and Table 2
on the enterprise emails and sales calls. Average
per-query token consumption and inference cost
for every configuration are reported in Appendix B.
Please refer Fig. 7 for qualitative results.
4.1 Discussion of Empirical Findings
We observe several notable trends. First,Claude
Sonnet 4.6leads all models with an aggregate
WCS of 55.8% on the SDR-Bench success sto-
ries, a 25.0% relative improvement over the next
best model, GPT-5.4-mini (44.6); yet even the best
model recovers only about half the strategic content
of the ground-truth success stories. We refer to this
persistent gap as thepersonalization plateau: the
gap between the personalization capabilities of cur-
rent agents and expert human senders. The plateau
is broad rather than family-specific: the four GPT-
family models cluster between 35.4 and 44.6 (over-
lapping bootstrap CIs for the weaker ones; Ap-
pendix B.2 Table 9), and the deep-research agents
Table 2:Private Enterprise Dataset.WCS on success-
ful outreach emails and sales call transcripts.
Model Health. (<$1B) Tech. (>$10B) Calls
Search
Claude Sonnet 4.6 60.89 61.33 42.85
GPT-5.4-mini 43.67 52.66 35.72
GPT-5.4 48.71 53.02 33.61
STORM-QWEN-2.5 32.27 39.24 33.80
GPT-4o-mini 39.14 45.63 29.68
QWEN2.5-72B 36.72 36.43 29.57
GPT-4o 40.62 45.17 26.19
ODR-QWEN-2.5 30.41 39.82 26.92
Direct
Claude Sonnet 4.6 42.93 54.26 39.71
GPT-5.4-mini 42.01 54.09 34.53
GPT-5.4 46.53 55.01 36.03
GPT-4o 45.09 46.40 32.59
QWEN2.5-72B 25.57 41.24 31.34
GPT-4o-mini 30.15 42.95 30.05
STORM (42.5) and ODR (33.5) do not escape it
despite much higher cost.
The evaluation onenterprise emails and sales
calls(Table 2) shows the same plateau: Claude
leads on coverage for both cohorts:Healthcare
andTechnology, the GPT-5.4 family follows on the
email data, and the deep-research agents and Qwen
trail, yet even the strongest model recovers only
about 60% of the winning content on emails and
well under half on transcripts. Absolute coverage is
higher on the well-documented, larger Technology
company than on the smaller, sparsely-documented
Healthcare company for almost all the agent config-
urations (LLMs w/ and w/o web search + DRAs).
We next examine why: whether the plateau reflects
a failure to find the right facts on the web, or a
failure to reason with facts once found.
7

Adobe Media & Data Science Research
4.2 The Bottleneck Is Retrieval, Not
Reasoning
TheLLM + Web Searchconfiguration is
motivated by the premise that account-specific
evidence (facts that make a pitch successful) must
be retrieved rather than recalled from parametric
memory. To test whether models actually convert
retrieval into recovered strategic content, we re-ran
every LLM with search disabled, holding prompts
and inputs fixed (theDirectrows of Table 1 and
Table 2).
Weaker models do not exploit search.Re-
moving web search changes WCS by less than
one point for GPT-5.4 ( 44.32→43.95 ), GPT-
5.4-mini (44.63→44.10 ), and QWEN-2.5-72B
(36.84→35.67 ), and evenimprovesGPT-4o
(35.42→38.15 ). If retrieval were supplying
the deal-winning specifics, removing it should
sharply reduce coverage; instead WCS is nearly
invariant or rises, indicating these models fall
back on prior knowledge or generic firmographic
content rather than converting search into strategic
content.Claude is the exception.It is the only
model whose coverage depends substantially on
search: removing it costs Claude 17.96 points
on Healthcare email outreach and 7.07 on Tech,
by far the largest such gaps of any model, with
a matching drop from 55.80 to 49.88 on the
success stories. Search also helps most where
documentation is sparsest: on the well-documented
Tech cohort, adding search is redundant or mildly
harmful for weaker models, whereas on the sparser
Healthcare cohort several weaker models gain
substantially (Table 2).
Pre-training leakage is not driving WCS.A
memorization probe, splitting SDR-Bench into pre-
and post-2024 stories relative to GPT-4o’s training
cutoff, shows negligible WCS differences across
the split (STORM: 0.42 vs. 0.43; GPT-4o: 0.36
vs. 0.36), ruling out memorization of the specific
ground-truth artifact as a confound.
Having shown that most models fail tofindthe
relevant content through open search, we next iso-
late whether the plateau is a retrieval failure or a
reasoning failure: can models synthesize a winning
pitch when handed the relevant facts directly? We
asked expert SDRs for 50 questions they routinely
ask when researching a deal (spanning customer,
seller, and product), issued these as queries through
the temporally constrained simulator, and compiled
the results into four expert-curated research reports:
Table 3:Expert-guided research reports. ∆WCS
from expert-curated reports covering the customer,
seller, product, or all three. Results are relative to each
configuration’s no-report baseline. All results reported
as averages over 3 runs.
QWEN-2.5-72B Claude Sonnet 4.6
Report supplied Direct+Search Direct+Search
+Customer−2.5−3.6 +0.9−2.4
+Seller+5.2 +1.8 +5.9 +1.1
+Product+5.5+2.8 +5.7 +1.7
+All+5.3 +3.3+7.0+6.6
one per element (seller, product and customer), and
one combining all three. We supply each report at
generation time to the weakest model (Qwen2.5-
72B) and the strongest (Claude), each in Direct and
+Search configurations, and report ∆WCS relative
to the no-report baseline in Table 3.
Given the expert-curated content, models
improve substantially, and the gain persists even
in the +Search configuration, where the model
already has live web access: an expert-curated
report still lifts WCS well beyond what the model’s
own search achieves on the same account (gains
of +5.3 and +3.3 WCS for QWEN (Direct /
+Search) and +7.0 and +6.6 for Claude (Table 3).
The bottleneck is therefore not the ability to reason
and synthesize once content is available, but query
formulation and information retrieval, knowing
what to search for. Models can convert strategic
content into stronger pitches once it is surfaced,
whether by their own search or an expert’s; they
simply do not know how to surface it themselves.
Seller and product evidence drive the gain;
customer evidence alone does not.Reports
about the seller and the product account for
almost the entire improvement, whereas the
customer-only report is flat-to-negative in three
of four configurations (Table 3), despite customer
research being the part of the task that most
resembles classical personalization. Facts about
the customer in isolation appear to steer models
toward restating the prospect’s business rather
than constructing an argument for why the product
addresses their needs; the gain materializes only
once seller and product information, facts that
do not vary across prospects, are also provided.
Combining all three sources yields the most robust
gain, indicating they are complementary once the
model is anchored on what to look for.
8

Adobe Media & Data Science Research
Table 4:Discriminative N-way accuracy( N= 5 :
one successful email vs. four same-industry unsuccess-
ful cold outbounds), for the web-search LLMs and the
deep-research agents, alongside their WCS on enter-
prise emails and success stories.
Model
N-way
Acc. (%)
Email-Succ.
WCS
Story-Agg.
WCS
Claude Sonnet 4.6 45.8 61.11 55.80
GPT-5.4 40.5 50.87 44.32
GPT-5.4-mini 39.0 48.17 44.63
GPT-4o 37.0 42.90 35.42
GPT-4o-mini 37.0 42.39 37.46
STORM 36.2 35.76 42.51
QWEN-2.5-72B 35.0 36.58 36.84
ODR 32.2 35.12 33.53
Spearmanρ(Acc. vs. WCS):0.97(Email),0.84(Story)
4.3 The Plateau Persists in a Discriminative
Task
Since WCS credits only content which matches the
single recorded winner V ∗, a low score could in
principle reflect a competent model that produced
a valid but different winning argument, one absent
from the ground truth. The personalization plateau
would then be an artifact of matching generated
content to ground truth rather than a real capability
gap. We test this directly with a discriminative task
whose scoring does not depend on matching V ∗
at all; the agent must recognize a winning email
rather than reconstruct it.
Setup.We set up the discriminative task as anN-
way forced choice. Each instance presents N= 5
real cold outbound sales emails, one that received
a positive response (a reply or booked call) and
four that did not, all sent to prospects in thesame
industry, and the agent must identify the one that
succeeded out of the 5 emails.
Even when choosing the successful email,
the best model is right less than half the time.
Models struggle on this task despite having to
onlyrecognizethe winning email, not author it,
and random guessing already yields 20%. The
best frontier model, Claude Sonnet 4.6, picks the
winning email out of five only 45.8% of the time
(Table 4), less than half. The GPT-5.4 and GPT-4o
families occupy the middle ( 37–40.5%), and
QWEN-2.5-72B sits at 35.0%; the deep-research
agents fare worst, with STORM at 36.2% and
ODR at32.2%despite their far higher cost.
These results show that the models are not able
to reliably differentiate a successful email from
unsuccessful emails, reinforcing the finding of a
personalization plateau. The discriminative task
shows that the personalization plateau is a gen-
uine limitation in personalization capability and
not a byproduct of measuring coverage against a
recorded winner. The same ranking of models also
emerges here as on the generative task, discrimi-
nation accuracy and WCS are rank-correlated at
Spearman ρ= 0.97 (p <0.001) against enterprise-
email WCS and ρ= 0.84 (p≈0.01 ) against SDR-
Bench story WCS, showing that the two tasks agree
on which models are weaker, but both place every
model far short of reliable personalization.
4.4 Token Usage, Cost, and Performance
Per-query token usage, inference cost, and WCS
for every configuration are reported in Table 8
and visualized in Figure 5. GPT-5.4-mini is the
most efficient frontier model ( 44.6 WCS at ∼8k
tokens), whereas the deep-research agents spend
one to two orders of magnitude more tokens
than LLM+search baselines without escaping
the personalization plateau. Claude Sonnet 4.6
achieves the highest WCS (55.8) at a token budget
comparable to STORM and ODR, both of which
trail it by more than 13 points.
5k 10k 20k 50k 100k
Total tokens per query (prompt + completion, log scale)
30
40
50
60WCS (%)
STORM
ODR
Qwen2.5-72B
GPT-4o
GPT-4o-mini
GPT-5.4-mini
GPT-5.4
Claude Sonnet 4.6Cost / query
$0.01 $0.05 $0.27
Best model LLM + web search Deep-research agent
Figure 5: Token usage vs. performance on SDR-Bench.
Each point is a configuration; the x-axis is total tokens
per query (log scale), the y-axis is WCS, and bubble
area encodes inference cost per query.
4.5 Human Alignment and Validation
To check that WCS reflects real-world quality, we
validate the Coverage Judge against independent
human raters and test its rankings against the judge-
ment of professional sales representatives.
We conducted a human study on 20 success
stories, scoring 100 model responses from five
web-search agents: STORM, ODR, Claude
Sonnet 4.6, and the best-performing GPT and
Qwen configurations. Three independent human
9

Adobe Media & Data Science Research
annotators, blinded to model identity, scored
coverage following the exact protocol of our
LLM-based Coverage Judge.
The study yields three convergent signals on
Judge fidelity. First, the Judge tracks human
scores with strong rank correlation (Spearman’s
ρ= 0.7435 , p <0.0001 ), holding across mod-
els (Claude: 0.7685; ODR: 0.7768; GPT: 0.7575;
Qwen: 0.7330; STORM: 0.6963). Second, the
Judgepreserves model ordering: both human-
and Judge-graded WCS rank Claude > STORM
≈ GPT > Qwen > ODR, so absolute-score dif-
ferences do not distort comparative conclusions.
Third, the Judge is systematically more conserva-
tive than human raters (Claude: 48.06 vs. 55.29;
GPT: 37.94 vs. 44.04; ODR: 31.10 vs. 41.69), rul-
ing out score inflation and establishing WCS as
a conservative, empirically validated proxy that
tracks human judgement.
We show that the WCS-based ranking transfers
to expert SDR judgment through two field studies
with 12 senior SDRs from the partner enterprises.
The first study measuresper-pitch usefulness:
whether a generated pitch point would be used
verbatim in real outreach. The second measures
strategy-level overlapbetween model output and
SDR-authored gold standards, probing per-point
quality and overall strategic match respectively.
Per-pitch usefulness.12 SDRs used our best-
performing model (Claude Sonnet 4.6) with SDR-
Arena to generate pitch points for 200+ new
prospects inside their normal outbound pipeline,
auditing output on accounts they were actively
working. Each generated pitch point was rated on
whether it (a) reflected genuine understanding of
the prospect’s pain points and (b) was usable with-
out rewriting;48.2%met both criteria, roughly half
of agent output being expert-grade in live deploy-
ment which is consistent with the personalization
plateau identified in results.
Gold-standard alignment.Senior SDRs ( ≥10
years of experience, ≥5 at the firm) from five en-
terprises authored reference “gold-standard” strate-
gies for 30 products across 5 prospects each, with-
out seeing any model output. Correlating expert-
overlap scores against automated WCS across mod-
els yields Pearson r= 0.816 , showing the WCS
ranking transfers to senior-SDR judgment without
re-tuning the rubric per enterprise.
Together, these studies establish that our frame-
work’s outputs are both factually grounded and
meaningful in live sales contexts.
5 Conclusion
We introduced SDR-Arena, a framework for
benchmarking two-party generative personaliza-
tion at scale, and SDR-Bench, a public corpus
of ∼50k customer success stories, to measure
whether an LLM can recover the strategic content
that historically induced a receiver to act. Across
frontier LLMs and deep-research agents, we find
a consistent personalization plateau: even the
strongest model recovers only about half the strate-
gic content of outreach known to have succeeded.
An independent discriminative task and field
deployment with professional sales representatives
confirm this reflects a real shortfall rather than an
artifact of scoring against a single ground truth.
The gap traces to retrieval, not reasoning: models
improve substantially when handed the facts an
expert researcher would find, but cannot surface
those facts through open web search on their own.
We release SDR-Arena and SDR-Bench to support
reproducible research on this capability.
Limitations:Our study has several limitations.
Our evidence comes from English-language sales
outreach across a large but still a limited set of en-
terprises, so the personalization plateau we observe
may not transfer to other languages, or receivers
outside the enterprise sales context we study. Sec-
ond, ground-truth pitch points and their coverage
are produced by LLM-based extraction and judg-
ing; although both are validated against human
annotators (extraction precision 0.92 / recall 0.97;
judge Spearman ρ= 0.74 ), residual model bias
may remain. Finally, the WCS measures argument-
content coverage grounded in the ELM and delib-
erately does not capture stylistic delivery or multi-
turn conversational quality.
5.1 Ethical Considerations
Our benchmark could help build more manipula-
tive outreach, but we believe openly measuring
such systems is safer than leaving them unevalu-
ated. The proprietary emails were processed under
access control with all PII anonymized or redacted,
and arenotreleased. SDR-Bench contains only
published, enterprise-level success stories, and our
web search tool honors robots.txt. An Accept-
able Use Policy will prohibit using our artifacts
for spam, undisclosed AI-written correspondence,
or phishing.
10

Adobe Media & Data Science Research
References
Adobe. 2026. Marriott customer success
story. https://business.adobe.
com/customer-success-stories/
marriott-case-study.html. Ac-
cessed: 2026-09-02.
Saleh Afzoon, Zahra Jamali, Usman Naseem, and
Amin Beheshti. 2026. PersoBench: Bench-
marking personalized response generation in
large language models.IEEE Transactions on
Artificial Intelligence. Early access. Preprint:
arXiv:2410.03198v2.
Anthropic. 2026. Claude Sonnet 4.6. https://
www.anthropic.com/claude/sonnet.
Accessed: 2026-05-07.
Bright Data. 2026. Bright Data SERP
API. https://brightdata.com/
products/serp-api. Accessed: 2026-05-
07.
Jin Chen, Zheng Liu, Xu Huang, Chenwang Wu,
Qi Liu, Gangwei Jiang, Yuanhao Pu, Yuxuan
Lei, Xiaolong Chen, Xingmei Wang, Defu Lian,
and Enhong Chen. 2024. When large language
models meet personalization: Perspectives of
challenges and opportunities.World Wide Web,
27(4):42.
Hana Choi, Carl F. Mela, Santiago R. Balseiro,
and Adam Leary. 2020. Online display ad-
vertising markets: A literature review and fu-
ture directions.Information Systems Research,
31(2):556–575.
Esin Durmus, Liane Lovitt, Alex Tamkin,
Stuart Ritchie, Jack Clark, and Deep
Ganguli. 2024. Measuring the per-
suasiveness of language models.
https://www.anthropic.com/news/
measuring-model-persuasiveness.
Accessed: 2026-09-29.
Carl I. Hovland, Irving L. Janis, and Harold H.
Kelley. 1953.Communication and Persuasion:
Psychological Studies of Opinion Change. Yale
paperbound. Yale University Press.
Bowen Jiang, Yuan Yuan, Maohao Shen, Zhuo-
qun Hao, Zhangchen Xu, Zichen Chen, Ziyi Liu,
Anvesh Rao Vijjini, Jiashu He, Hanchao Yu,
Radha Poovendran, Gregory Wornell, Lyle Un-
gar, Dan Roth, Sihao Chen, and Camillo Jose
Taylor. 2025. PersonaMem-v2: Towards per-
sonalized intelligence via learning implicit user
personas and agentic memory.arXiv preprint
arXiv:2512.06688v1.
Emir Kamenica and Matthew Gentzkow. 2011.
Bayesian persuasion.American Economic Re-
view, 101(6):2590–2615.
LangChain. 2025. Open Deep Re-
search. https://github.com/
langchain-ai/open_deep_research.
Accessed: 2026-05-07.
Harold D. Lasswell. 1948. The structure and func-
tion of communication in society. In Lyman
Bryson, editor,The Communication of Ideas,
pages 37–51. Institute for Religious and Social
Studies; distributed by Harper & Brothers, New
York.
Li Li, Peilin Cai, Ryan A. Rossi, Franck Der-
noncourt, Branislav Kveton, Junda Wu, Tong
Yu, Linxin Song, Tiankai Yang, Yuehan Qin,
Nesreen K. Ahmed, Samyadeep Basu, Sub-
hojyoti Mukherjee, Ruiyi Zhang, Zhengmian
Hu, Bo Ni, Yuxiao Zhou, Zichao Wang, Yue
Huang, Yu Wang, Xiangliang Zhang, Philip S.
Yu, Xiyang Hu, and Yue Zhao. 2025. A
personalized conversational benchmark: To-
wards simulating personalized conversations. In
NeurIPS 2025 Workshop on Multi-Turn Inter-
actions in Large Language Models. Preprint:
arXiv:2505.14106v2.
Sandra C. Matz, Jacob D. Teeny, Sumer S. Vaid,
Heinrich Peters, Gabriella M. Harari, and Moran
Cerf. 2024. The potential of generative AI for
personalized persuasion at scale.Scientific Re-
ports, 14(1):4692.
Ani Nenkova and Rebecca Passonneau. 2004.
Evaluating content selection in summarization:
The pyramid method. InProceedings of the Hu-
man Language Technology Conference of the
North American Chapter of the Association for
Computational Linguistics (HLT-NAACL), pages
145–152, Boston, Massachusetts, USA. Associ-
ation for Computational Linguistics.
11

Adobe Media & Data Science Research
OpenAI. 2024. GPT-4o system card.arXiv
preprint arXiv:2410.21276v1.
OpenAI. 2026. GPT-5.4 Thinking System
Card. https://openai.com/index/
gpt-5-4-thinking-system-card/ .
Accessed: 2026-09-01.
Oracle. 2026. Careem technical case study.
https://www.oracle.com/cloud/
technical-case-studies/careem/.
Accessed: 2026-09-02.
Richard E. Petty and John T. Cacioppo. 1986.
The Elaboration Likelihood Model of persua-
sion. In Leonard Berkowitz, editor,Advances
in Experimental Social Psychology, volume 19
ofAdvances in Experimental Social Psychology,
pages 123–205. Academic Press.
Ronak Pradeep, Nandan Thakur, Shivani Upad-
hyay, Daniel Campos, Nick Craswell, Ian Sobo-
roff, Hoa Trang Dang, and Jimmy Lin. 2025.
The great nugget recall: Automating fact extrac-
tion and RAG evaluation with large language
models. InProceedings of the 48th Interna-
tional ACM SIGIR Conference on Research and
Development in Information Retrieval (SIGIR),
pages 180–190. Preprint: arXiv:2504.15068v1.
Francesco Ricci, Lior Rokach, and Bracha Shapira.
2010. Introduction to Recommender Systems
Handbook. InRecommender Systems Hand-
book, pages 1–35. Springer.
Alireza Salemi, Sheshera Mysore, Michael Ben-
dersky, and Hamed Zamani. 2024. LaMP: When
large language models meet personalization. In
Proceedings of the 62nd Annual Meeting of the
Association for Computational Linguistics (Vol-
ume 1: Long Papers), pages 7370–7392.
Salesforce. 2026. Snapology customer story.
https://www.salesforce.com/
resources/customer-stories/
snapology/. Accessed: 2026-09-02.
Yijia Shao, Yucheng Jiang, Theodore Kanell, Pe-
ter Xu, Omar Khattab, and Monica Lam. 2024.
Assisting in writing Wikipedia-like articles from
scratch with large language models. InPro-
ceedings of the 2024 Conference of the North
American Chapter of the Association for Com-
putational Linguistics: Human Language Tech-
nologies (Volume 1: Long Papers), pages 6252–
6278, Mexico City, Mexico. Association for
Computational Linguistics.
Osman Tasdelen and Daniel Bodemer. 2025. Gen-
erative AI in the classroom: Effects of context-
personalized learning material and tasks on
motivation and performance.International
Journal of Artificial Intelligence in Education,
35(5):3049–3070.
Harri Terho, Anna Salonen, and Meri Yrjänen.
2023. Toward a contextualized understanding
of inside sales: The role of sales development
in effective lead funnel management.Journal
of Business & Industrial Marketing, 38(2):337–
352.
Ellen M. V oorhees. 2003. Overview of the TREC
2003 question answering track. InProceedings
of the Twelfth Text REtrieval Conference (TREC
2003), pages 54–68. NIST. NIST Special Publi-
cation 500-255.
An Yang, Baosong Yang, Beichen Zhang, Binyuan
Hui, Bo Zheng, Bowen Yu, Chengyuan Li,
Dayiheng Liu, Fei Huang, Haoran Wei, Huan
Lin, Jian Yang, Jianhong Tu, Jianwei Zhang,
Jianxin Yang, Jiaxi Yang, Jingren Zhou, Jun-
yang Lin, Kai Dang, Keming Lu, Keqin Bao,
Kexin Yang, Le Yu, Mei Li, Mingfeng Xue, Pei
Zhang, Qin Zhu, Rui Men, Runji Lin, Tianhao
Li, Tianyi Tang, Tingyu Xia, Xingzhang Ren,
Xuancheng Ren, Yang Fan, Yang Su, Yichang
Zhang, Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru
Zhang, and Zihan Qiu. 2024. Qwen2.5 technical
report.arXiv preprint arXiv:2412.15115v2.
Saizheng Zhang, Emily Dinan, Jack Urbanek,
Arthur Szlam, Douwe Kiela, and Jason Weston.
2018. Personalizing dialogue agents: I have a
dog, do you have pets too? InProceedings of
the 56th Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Pa-
pers), pages 2204–2213, Melbourne, Australia.
Association for Computational Linguistics.
12

Adobe Media & Data Science Research
Zheng Zhao, Clara Vania, Subhradeep Kayal, Naila
Khan, Shay B. Cohen, and Emine Yilmaz. 2025.
PersonaLens: A benchmark for personalization
evaluation in conversational AI assistants. In
Findings of the Association for Computational
Linguistics: ACL 2025, pages 18023–18055.
A Replication Details
A.1 SDR-Bench Dataset Curation
SDR-Bench is built from publicly available cus-
tomer success stories. Starting from ∼12,000
global enterprises with revenue exceeding $1B,
we resolved company domains, located sitemaps,
and harvested candidate success-story URLs us-
ing path heuristics (e.g., /customer-stories,
/case-study). A multi-stage pipeline then re-
moved non-text formats, generic or listicle pages,
articles without a verifiable publication date or iden-
tifiable product, and anonymized stories whose cus-
tomer was not explicitly named. Each stage and its
surviving count are reported in Table 5, yielding a
final corpus of 50,000 stories across 22 industries.
Table 5: Filtration criteria and surviving counts for the
public data collected to build SDR-Bench.
Filtration Criteria Count
Domains for companies with >$1B rev-
enue
∼30k
B2B companies with>$1B revenue 12,080
Companies whose URLs were discov-
ered
3,500
Total webpages found∼7M
Candidate success story URLs∼400k
After Qwen content filter (listicle/parent/
generic/no-date pages removed)
∼60k
After removing non-specific customers 50,000
A.2 Enterprise Sales Email Processing
Table 6: Processing of Enterprise Sales Email Data
Metric / Artifact Category Healthcare Tech
Number of SDRs 3 124
Total Emails Collected 48,150 609,191
Deduplication 31,034 186,379
Sales Outreach Emails 24,506 90,809
Successful Outreach (Call
Scheduled)
354 13,236
A.2.1 Filtering and Extraction
Let E={e 1, e2, . . . , eN } denote the raw corpus
of sales emails. We apply a three-stage filtering
pipeline:
• Language filtering:remove non-English emails
via language detection, yieldingE en ⊂ E.
• Deduplication:remove duplicate templates us-
ing exact matching and fuzzy string comparison,
yieldingE dedup ⊂ Een.
• Intent classification:an LLM judge J:e→
{0,1} retains valid outreach (J(e) = 1 ) and dis-
cards generic, administrative, or non-sales email,
givingE filtered ={e∈ Ededup :J(e) = 1}.
For each e∈ Efiltered we use an LLM to extract
the strategies employed, Strat(e)⊆ S , and the
fine-grained pitch points pp(e) ={pp 1, . . . , ppk};
the latter constitute the ground truth against which
agent outputs are scored. Each annotated sample
stores the target company Ti, sender company Si,
email body Ei, timestamp t, product P , strategy
labels Strat(e), and pitch points pp(e). The result-
ing strategy-frequency distribution P(s) and the
product-conditional distribution P(s|Product k)
summarize how human SDRs operationalize per-
sonalization in practice.
A.2.2 Personalization Strategy Taxonomy
To characterize personalization strategies we used
a two-step pipeline: (i) domain experts manually
annotated a seed set of emails to identify recur-
ring patterns, and (ii) an LLM extracted and clus-
tered strategies from 500 randomly sampled emails,
which were reconciled with the expert annotations
into a unified taxonomy. A strategy s∈ S de-
notes the primary information source used to es-
tablish relevance between the seller’s value propo-
sition and the buyer’s needs. The strategy space
S={s 1, . . . , s10}comprises:
• Industry-based:industry-specific trends, pain
points, competitors, or case studies.
• Event-based:trigger events (funding, M&A,
launches, earnings, news) signaling timely needs.
• Technology-based:the recipient’s current tech
stack, for replacement, integration, or comple-
mentary solutions.
• Lead-activity-based:direct actions by the lead
(downloads, webinar attendance, pricing-page
visits, demos).
• Buying-group-activity-based:collective ac-
tions by the lead’s team or buying committee.
• Geography-based:location or regional regula-
tory context (e.g., GDPR, CCPA).
13

Adobe Media & Data Science Research
Industry Based Personalization
Hi Prospect,
When speaking with businesses in your
industry, we often hear the same challenge: How
do we move from real-time data collection to
real-time customer experiences?
Many platforms promise "real-time," but the reality
often looks like this:
• Data is collected instantly, but activation takes
hours
• Proﬁles stay fragmented across marketing, IT, and
service teams
• Rigid data models slow down campaign agility
ABC is designed to change that. It helps unify
known and anonymous data into live proﬁles that
can instantly power personalized experiences
across every channel. Would you be open to a quick
chat about how similar companies are seeing
measurable ROI in just weeks?
Prospect Activity Based Personalization
Hi Prospect,
I noticed you recently explored content around
ABC, great to see that interest in real-time data
activation. Since you're helping drive growth at
XYZ, I ﬁgured I'd ride along (Couldn't resist the
pun) and reach out.
ABC helps brands bring together customer data
from every touchpoint, web, app, and campaign and
activate it instantly across channels. It's helping
teams like yours deliver personalized experiences
that move as fast as your customers do.
If you're exploring how to better use ﬁrst-party data,
streamline customer journeys, or break down data
silos, I'd be happy to share how other teams are
making it work with ABC. Would you be open to a
quick 15-minute chat?
Figure 6: Personalization in actual sales emails: SDRs
adapt the same product positioning across recipients
with distinct needs and pain points.
• Lead-persona-based:the lead’s role, title, or re-
sponsibilities mapped to role-specific pain points.
• Firmographics-based:company-level metrics
(headcount growth, revenue, department size).
• Relationship-based:existing customer relation-
ships, cross-sell or upsell.
• None:generic outreach lacking recipient-
specific context.
A.3 Pitch-Point Extraction and Human
Validation
Ground-truth pitch points V ∗ are extracted from
each artifact with GPT-4o under an ontological
prompt (App. A.4): each pitch point must follow
the triadProduct/Service → Specific Pain Point
→ Value Proposition/Mechanismand be validated
with an exact evidence quote from the source text.
To assess extraction quality, three annotators re-
viewed the extracted pitch points on a random
sample of 30 customer success stories, flagging
hallucinated points (false positives) and missing
points (false negatives). Table 7 reports the result-
ing counts: precision 0.92, recall 0.97, and F1 0.95,
indicating strong alignment with expert judgment.
Table 7: Human evaluation of LLM-extracted pitch
points on 30 customer success stories, assessing preci-
sion (factual consistency, hallucination flagging) and
recall (missed pitch points).
TP FP FN Precision Recall F1
138 11 3 0.92 0.97 0.95
A.4 Prompt Library
We provide the exact prompts used for LLM-
based judging (Box 1), pitch-point generation
(Box 2), and ground-truth pitch-point extrac-
tion (Box 3). Placeholders in {braces} or
<<<angle brackets>>> are substituted at
runtime.
Box 1: LLM-as-a-Judge Evaluation Prompt
SYSTEM — Role:You are a Senior Sales Enable-
ment Evaluator. Your goal is to determine if an AI
agent has successfully extracted the “Winning Pitch
Points” from a customer success story.
INPUT DATA
1. Ground-Truth (GT) Winning Points— the
proven, specific facts that won the deal:
<<<gt_pitch_points_str>>>
2. Candidate Pitch (Predicted)— the
points generated by the AI agent:
<<<candidate_pitch_points_str>>>
TASK:For each Ground-Truth point, determine how
well the Candidate Pitch covers it. Grade onSales
EffectivenessandFactual Precision.
SCORING RUBRIC (0–5):
• 0 (Miss / Irrelevant):completely misses this con-
cept.
• 1 (Marketing Fluff):vaguely mentions the topic
(e.g., “improved efficiency”) with no specific sub-
stance.
• 2 (Topic Match):correct Product or Pain Point,
14

Adobe Media & Data Science Research
but misses the specific Solution or Outcome.
• 3 (Implied / Soft Match):captures the core value
proposition, but misses “hero evidence” (specific
numbers, names, mechanisms).
• 4 (Strong Sales Argument):captures core value
andthe key mechanism/outcome; may miss a mi-
nor detail.
• 5 (Strategic Bullseye):perfect extraction captur-
ing Product + Pain + Value + Specific Metric/Evi-
dence, essentially verbatim.
OUTPUT FORMAT (JSON only):
{
"evaluations": [
{
"gt_point_id": <int>,
"gt_summary": "<
,→short_summary_of_gt_point>",
"best_match_candidate_text":
,→"<
,→text_from_candidate_or_null>",
,→
"score": <0-5>,
"reasoning": "<
,→concise_sales_analysis>"
}
]
}
Box 2: Pitch-Point Generation Prompt
I am a BDR at{seller} ({seller_website}).
I want to sell {seller} products to {customer}
({customer_website}). How should I pitch
{products} to {customer}? Generate 3 tar-
geted pitch points and value propositions that ad-
dress the customer’s pain points, which I can send to
{customer} or their CEO / leads / decision makers.
Provide reasoning for each pitch point.
Requirements for each pitch point:
• Specific to the target company (use real facts you
discover).
• Connects the sender’s products/services to the tar-
get’s needs/pain points.
• Atomic — one clear value proposition per point.
• Compelling and actionable.
After researching, generate 3 pitch points, each with
a single value proposition addressing the customer’s
pain point. Each must be unique (the same product or
pain point may recur, but the value proposition must
differ).
Respond with a JSON array of pitch-point strings:
[
"First pitch point text here",
"Second pitch point text here",
,→
"Third pitch point text here"
]
Strictly adhere to the JSON format above.
Box 3: Pitch-Point Extraction Prompt
You are an expert sales analyst. Analyze the following
success-story content for {company_name} (the
seller) and their product {product_name}. Story
content:{story_html}.
Extract specific, causal pitch points that explainwhy
the product was successful, and provide exact quotes
from the text as evidence.
STRICT FORMAT:return a JSON object with a
single key "pitch_points" containing a list of
objects of the form:
{
"summary": "<Product/Service>
,→solved <Specific Pain Point>
,→of <Customer>
because of <Value Proposition
,→/Mechanism>[, resulting in <
,→Quantitative Result>]",
"evidence": [
"Exact quote from the text
,→supporting the pain point
,→...",
"Another exact quote..."
]
}
GUIDELINES:
1. Product/Service:use the specific product name
if available.
2. Specific Pain Point:name the exact problem;
distinguish “slow/manual work” from “inaccura-
cy/errors” — these are distinct.
3. Value Proposition/Mechanism:the specific fea-
ture that solved it.
4. Quantitative Result:if the text gives a number
(e.g., “70% faster”), you must include it in the
summary.
5. Evidence:quote the original text; do not para-
phrase.
Example output:
{
"pitch_points": [
{
"summary": "The Aldec
,→G3 solved the high energy
,→costs of T.Z. Osborne
because of its
,→PowerTubes technology that
,→recovers kinetic energy,
reducing consumption
,→by 20%.",
"evidence": ["Facing
,→rising energy costs...",
"The PowerTubes
,→technology recovers kinetic
,→energy,
reducing consumption
,→by 20%"]
},
{
"summary": "Oracle
15

Adobe Media & Data Science Research
,→Integration solved the issue
,→of manual entry errors
at Careem because of
,→its automated GRN matching
,→feature.",
"evidence": ["Manual
,→entry led to mismatches and
,→compliance gaps.",
"Automating GRN
,→matching has significantly
,→reduced errors."]
}
]
}
B Supplementary Results and Analysis
Table 8: Per-query token usage, inference cost, and
WCS on the SDR-Bench evaluation set.Search=
temporally-constrained web search;Direct= no tool use.
Deep-research agents are search-only. Token counts are
mean prompt/completion tokens per query; costs use
public API list prices at evaluation time. The deep-
research pipelines (STORM, ODR) consume one to two
orders of magnitude more tokens than the LLM+search
baselines for comparable or lower WCS.
Model Mode Prompt Compl. Cost WCS
Tok. Tok. ($)
STORM Search 29k 6.3k 0.135 42.51
ODR Search 66k 8.6k 0.250 33.53
Claude Sonnet 4.6 Search 79k 2.2k 0.27055.80 Direct 0.3k 1.2k 0.019 49.88
GPT-5.4-mini Search 7.6k 0.7k 0.009 44.63 Direct 0.3k 0.67k 0.003 44.10
GPT-5.4 Search 12.1k 0.9k 0.044 44.32 Direct 0.3k 1.15k 0.018 43.95
GPT-4o-mini Search 12.2k 0.6k 0.002 37.46 Direct 0.3k 0.4k 0.0003 33.88
Qwen2.5-72B Search 5.6k 0.25k 0.002 36.84 Direct 0.3k 0.35k 0.0003 35.67
GPT-4o Search 9.2k 0.4k 0.027 35.42 Direct 0.3k 0.55k 0.006 38.15
B.1 Qualitative Example
B.2 Bootstrap Confidence Intervals
Table 9: Bootstrap estimates of WCS on the SDR-Bench
evaluation set (1,000 resamples), with per-configuration
means and 95% confidence intervals. The weaker GPT-
family and Qwen intervals overlap (the personaliza-
tion plateau), while Claude Sonnet 4.6 separates clearly
above the rest.
Model Mean WCS 95% CI
Claude Sonnet 4.6 0.5580 [0.5238, 0.5906]
GPT-5.4-mini 0.4488 [0.4265, 0.4700]
GPT-5.4 0.4457 [0.4216, 0.4683]
STORM 0.4251 [0.4003, 0.4517]
GPT-4o-mini 0.3767 [0.3567, 0.3977]
Qwen-2.5-72B 0.3684 [0.3478, 0.3878]
GPT-4o 0.3562 [0.3345, 0.3775]
ODR 0.3353 [0.3139, 0.3570]
B.3 Success-Story Distribution by Industry
0% 10% 20% 30%
Share of success stories
Technology & Software
Industrial Manufacturing
Energy & Utilities
Other
Real Estate & Data Centers
IT Services & Consulting
Telecommunications
Building & Construction
Media & Advertising
Financial Services
Chemicals & Materials
Automotive & Transportation
Retail & E-commerce
Customer Service & Outsourcing
Logistics & Supply Chain
Cybersecurity
Healthcare & Medical Devices
Defense & Security
Food & Agriculture
Insurance & Risk Management
Testing & Certification
Environmental Services
Conglomerates
26.3%
13.1%
10.5%
9.4%
5.0%
4.8%
4.7%
4.2%
4.2%
2.9%
2.7%
2.2%
2.1%
1.8%
1.3%
1.2%
0.9%
0.9%
0.8%
0.5%
0.3%
0.2%
0.1%
Figure 8: SDR-Bench: Distribution of the count of suc-
cess stories across different industries, complementing
the company-level distribution in Figure 4. The corpus
spans a broad range of sectors, with technology, manu-
facturing, and energy the most represented.
16

Adobe Media & Data Science Research
4 GT #1: Salesforce B2B Commerce solved Ovation Medical's inefﬁcient reordering process for returning customers
because of its self-service and automation features, making reordering as simple as clicking a button.
Best Match: "Optimize Online Ordering and Customer Self-Service: By integrating Salesforce B2B Commerce, Ovation
Medical can create a seamless online ordering experience for its customers. This will reduce the administrative burden on
the sales and customer service teams, allowing them to focus on more strategic activities. Additionally, a robust self-
service portal can provide customers with 24/7 access to order history, invoices, and support, leading to improved
customer satisfaction and operational efﬁciency."
💡  The candidate pitch captures the self-service and automation features well, emphasizing customer ease and operational
efﬁciency. However, it does not explicitly mention the simplicity of reordering or the 'clicking a button' mechanism.
2 GT #2: Salesforce B2B Commerce solved Ovation Medical's challenge of maintaining custom order ﬂows because of
its ability to support customizations that align with speciﬁc business requirements, ensuring continuity of
established processes.
Best Match: "Enhance Product Catalog Management: Salesforce B2B Commerce offers powerful tools for managing
product catalogs, including dynamic pricing, inventory management, and product recommendations. These features can
help Ovation Medical maintain an up-to-date and accurate catalog, ensuring that customers have access to the latest
products and pricing information."
💡  The candidate pitch touches on customization and catalog management but does not address the speciﬁc need for
maintaining custom order ﬂows or continuity of established processes.
Figure 7:Qualitative exampleof the Coverage Judge: ground-truth pitch points matched against the agent’s
generated pitch points and scored on the 0–5 rubric of Appendix A.4, illustrating how partial topic matches are
separated from strategic bullseyes.
17
