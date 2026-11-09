---
title: 'SPAR: Experience-Driven Strategy Evolution in Multi-Session B2B Sales'
url: https://arxiv.org/abs/2611.01695
category: b2b
subcategory: empirical
date: 2026-11
venue: ''
authors:
- Hangming Zhang
- Yao Zhao
- Haotian Kuang
- C. L. Philip Chen
- Tong Zhang
source: arxiv
pdf_url: https://arxiv.org/pdf/2611.01695
pages: 10
chars: 40511
fetched_at: '2026-11-08T12:57:11+00:00'
kb_version: 1
---

# SPAR: Experience-Driven Strategy Evolution in Multi-Session B2B Sales

SPAR: Experience-Driven Strategy Evolution in Multi-Session B2B Sales
Hangming Zhang1*† Yao Zhao2* Haotian Kuang2
C. L. Philip Chen1 Tong Zhang1 Tengyue Ma2‡
1South China University of Technology
2Alibaba Group
hangmingzhang37@gmail.com, philip.chen@ieee.org, tony@scut.edu.cn,
{zhaoyao.zhao, kuanghaotian.kht, xianyue.mty}@taobao.com
Abstract
B2B outbound sales involves high transaction
values and relationship-based trust, so closing
a deal typically requires multiple rounds of
outreach building on prior context. Existing
LLM-based sales agents operate within single
sessions and cannot carry forward context or
refine strategies from experience. Methods that
do learn from experience store lessons as un-
structured text and treat all outcomes as equally
informative, with no mechanism to distinguish
a flawed strategy from an external factor. We
propose SPAR, a self-evolving framework that
models selling strategies as testable hypothe-
ses and refines them without parameter up-
dates. A double-loop architecture lets an in-
ner loop adapt to individual merchants through
episodic memory while an outer loop evolves
a shared strategy playbook through causal at-
tribution and hypothesis-driven evolution. In
a live A/B test on the 1688 platform with over
200,000 merchants, SPAR achieves +15.8%
conversion lift and +35.8% high-intent mer-
chant growth. Human evaluation by domain
experts rates SPAR at 4.62 out of 5 on overall
sales quality, the highest among all methods.
1 Introduction
In B2B outbound sales, high transaction values,
multi-stakeholder decisions, and relationship-based
trust mean that closing a deal typically requires
multiple rounds of persistent, targeted outreach.
Experienced salespeople handle this by carry-
ing forward context, judging which approaches
work, and refining their playbook across merchants.
Large language models have driven interest in au-
tomating this process (Chiu et al., 2022; Chang and
Chen, 2024; Kim et al., 2025), yet existing systems
remain limited to single-session interactions (He
*Equal contribution.
†Work done during internship at Alibaba Group.
‡Corresponding author.
Our search boost can double your store visibility
Traffic isn't my problem — it doesn't convert
Want to try our search boost? 30% off this month
I told you, traffic doesn't convert for me
Our product works very well and other merchants
have also given it high praise
User hung up
Not converted
Do you need search boost? 618 slots are selling out
User hung up
Our search boost can double your store visibility
Traffic isn't my problem — it doesn't convert
You mentioned conversion issues and our precision
targeting filters high-intent buyers only
That's different, tell me moreWillingness rising
We'll send you the details via text message
Peak season for your category starts next month,
ready to launch? We have a 30% discount for you.
OK, let's set it upConverted
Single- session Agent SalesHuman Sales
Willingness no change
Figure 1: Single-session agents repeat generic pitches
across isolated calls without addressing the merchant’s
core objection, leading to repeated rejections. Multi-
session human salespeople follow up on specific con-
cerns, build on prior context, and achieve conversion.
S1, S2, . . .denote session 1, session 2, and so on.
et al., 2018; Shea et al., 2024), leaving three closely
linked challenges unaddressed.
Current systems treat each session as an isolated
event, asingle-session limitationthat caps conver-
sion at first-contact performance (Chang and Chen,
2024), as Figure 1 illustrates. Even with multi-
session capability,attribution ambiguitypersists,
as it remains unclear whether a failed follow-up
reflects a flawed strategy or an external factor.
This ambiguity entrenchesmanual dependence
on hand-crafted scripts, since automating strategy
updates without reliable attribution would amplify
rather than correct errors (Deng et al., 2024). These
three barriers operate at successive levels, and each
must be resolved for the next to become effective.
While recent LLM-based agents have explored
1
arXiv:2611.01695v1  [cs.AI]  1 Nov 2026

experience-driven self-improvement (Shinn et al.,
2023; Zhao et al., 2024; Park et al., 2023), they
treat all outcomes as equally informative and store
experience as unstructured text, offering no mech-
anism to filter external noise or to systematically
validate and retire strategies.
We propose SPAR (StrategyPlaybook via
AttributedRefinement), a self-evolving framework
that models selling strategies astestable hypothe-
sesand iteratively refines them through sequential
merchant interactions without parameter updates.
Learning is organized as a double-loop architecture,
where an inner loop adapts to individual merchants
through multi-session memory, while an outer loop
systematically evolves the shared strategy playbook
across merchants through causal attribution and
hypothesis-driven evolution.
Our contributions are as follows.
• We formulate multi-session B2B sales as a
double-loop learning problem and propose
SPAR, a self-evolving framework that sepa-
rates within-merchant adaptation from cross-
merchant strategy refinement, requiring no
parameter updates.
• We model selling strategies as testable hy-
potheses with an evidence-based lifecycle of
proposal, testing, validation, and retirement,
and introduce causal attribution to isolate gen-
uinely strategy-driven outcomes for reliable
playbook updates.
• We evaluate SPAR in a live A/B test on
the 1688 platform with over 200,000 mer-
chants, achieving +15.8% conversion lift and
+35.8% high-intent merchant growth. Simu-
lation analysis also shows SPAR outperforms
the strongest baseline by 9.6% on objection
recognition and 5.5% on evidence support.
2 Related Work
2.1 Sales Dialogue Agents
Conversational agents for sales and negotiation
(Zhan et al., 2024) have progressed from scripted
pipelines (Chiu et al., 2022) to LLM-powered ap-
proaches that inject strategies through fine-tuning
(Chang and Chen, 2024) and learn adaptive policies
(Deng et al., 2024). Complementary efforts eval-
uate negotiation capabilities (Bianchi et al., 2024)
and profile users for personalization (Kim et al.,
2025; Gou et al., 2025). Despite this progress,
all existing systems operate within asingle inter-
action session, with no mechanism to revisit mer-
chants or refine strategies from ongoing experience.
Multi-session dialogue has been studied in open-
domain settings (Xu et al., 2022; Maharana et al.,
2024; Li et al., 2025). Memory systems and bench-
marks built for multi-session agents follow the
same framing, where MemMachine (Wang et al.,
2026) preserves one user’s conversational record at
the episode level for cheap personalized retrieval
and MemoryArena (He et al., 2026) tests whether
an agent uses what earlier sessions gave it rather
than recalling it on demand. This line of work is
organized around the record of a single user and
improves what an agent can recall, but these sys-
tems maintain conversational consistency rather
than adapt strategically toward conversion.
2.2 Outcome Attribution
Determining which action caused an observed out-
come is fundamental to learning from sequential
interactions. Counterfactual credit assignment in
reinforcement learning (Mesnard et al., 2021) dis-
tinguishes the agent’s contribution from external
factors. Despite this importance, LLM agent learn-
ing frameworks treat all results as equally informa-
tive. SPAR bridges this gap by separating strategy-
driven outcomes from externally-determined ones
before updating the playbook.
2.3 Experience-Driven Self-Improvement
Building on foundational agent frameworks (Yao
et al., 2022), recent work enables LLM agents to
learn from experience without parameter updates
through self-reflection (Shinn et al., 2023; Madaan
et al., 2023; Park et al., 2023), cross-episode trans-
fer (Zhao et al., 2024; Fu et al., 2024; Wang et al.,
2024), self-generated examples (Sarukkai et al.,
2026), and evolving context (Zhang et al., 2026).
However, these methods store experience as un-
structured text or flat rules, with no lifecycle to
promote validated strategies and retire failing ones.
3 Method
3.1 Task Formulation
The agent contacts N merchants sequentially, each
with behavioral profilepi. For merchant i, the agent
conducts up to K dialogue sessions. Session k pro-
duces outcome oi,k ∈ {1,0,−1}, representing suc-
cess, ongoing, and failure respectively. The agent
maintains two evolving knowledge stores. An
2

episodic memory Mi for each merchant records
structured session-level notes across follow-ups.
A sharedstrategy playbook P={h 1, . . . , hm}
accumulates selling strategies refined through ex-
perience across all merchants. The objective is to
maximize the cumulative conversion rate
R= 1 N NX i=1 max k≤K 1[oi,k = 1](1)
while simultaneously improving P such that later
merchants benefit from validated lessons learned
from earlier ones.
3.2 Framework Overview
SPAR organizes learning as adouble-loop archi-
tecture, illustrated in Figure 2. Theinner loop
adapts to individual merchants across multiple ses-
sions using episodic memory Mi. Theouter loop
evolves P across merchants by treating each inter-
action as a natural experiment that tests and refines
strategy hypotheses. Algorithm 1 summarizes the
complete pipeline, and the following subsections
detail each component.
3.3 Strategy as Testable Hypothesis
We model each strategy as atestable hypothesis
with accumulated evidence that drives lifecycle
transitions. The strategy playbook P is a collec-
tion of such hypotheses, each evolved through re-
inforcement, refinement, addition, merging, and
deprecation (§3.5). Each hypothesis h∈ P car-
ries an evidence set E(h), where each entry e∈
E(h) records the merchant context and interaction
outcome. A causal attribution function a(e)∈
{s, x, u}then labels the outcome asstrategy-driven,
externally-determined, oruncertain. Let Es(h) =
{e∈E(h)|a(e) =s} denote the strategy-
attributed evidence and Esucc s (h) the subset with
successful outcomes. Theconfidenceof h is com-
puted as the posterior mean of a Beta-Bernoulli
model with uniform prior
c(h) = 1 +|E succ s (h)| 2 +|E s(h)| (2)
which starts at c(h) = 0.5, avoids overconfidence
from small samples, and converges to the empir-
ical success rate as evidence accumulates, isolat-
ing the causal effect of the strategy by excluding
externally-attributed evidence. Each hypothesis
has status σ(h)∈ {0,+1,−1} for tentative, active,
and deprecated, transitioning by
σ(h)←



+1|E s(h)| ≥τp ∧c(h)≥θ p
−1|E s(h)| ≥τd ∧c(h)< θ d
σ(h)otherwise
(3)
where (τp, θp) and (τd, θd) are promotion and dep-
recation thresholds. P + ={h∈ P |σ(h)≥0}
denotes the non-deprecated hypotheses. To balance
exploitation and exploration, each hypothesis car-
ries anexploration prioritycombining Bernoulli
outcome variance with a sample-size exploration
bonus
I(h) =c(h)·

1−c(h)

+ 1 1 +n (4)
wheren=|E s(h)|.
3.4 Within-Merchant Adaptation
The inner loop maintains anepisodic memory Mi
for each merchant. After each session, the agent
generates a structuredreflectionsummarizing what
happened, why the outcome occurred, and what to
try next, then stores it in Mi alongside the outcome
and strategy used. This reflection provides action-
able context for follow-up sessions and supplies
the qualitative signal needed for causal attribution
in the outer loop.
At the start of each session, the agent concate-
nates the merchant profile pi, interaction history
Mi, and the non-deprecated hypothesis set P + as
selection context. An LLM-based selector imple-
ments the scoring function f in Algorithm 1, choos-
ing h∗ ∈ P+ by evaluating precondition alignment,
consistency with prior outcomes, and exploration
priority I(h). In follow-up sessions, recorded fail-
ure modes steer the selector away from repeating
unsuccessful strategies.
3.5 Cross-Merchant Strategy Evolution
After each merchant interaction, the outer loop
transforms raw experience into systematic play-
book improvements through causal attribution, hy-
pothesis evolution, and quality curation.
Causal Attribution.The LLM examines the di-
alogue, merchant profile, outcome, and strategy
used, then assigns an attribution label a(e)∈
{s, x, u}. This counterfactual credit assignment
(Mesnard et al., 2021) gates playbook updates.
Only outcomes with a(e) =s enter Es(h∗) and
trigger evolution. External outcomes are recorded
but do not affectc(h).
3

Outer Loop: Strategy Evolution
Strategy Playbook
Hypothesis Preconditions
Action Evidence
Failure
pattern
Success
pattern
Structure
Active Strategies
: Free Trial for Small-scale Merchants
Step1: Retrieve & Select
Merchant Context
Session
History
Monthly 
GMV: 80K
Industry:
Women's
Fashion
Strategies 
Strategy Retrieve & Select
Merchant Attributes
Budget
sensitive
Small-scale
Business
: Free Trial
for Small-scale
Merchants
Step 2: Inner Loop: Merchant Adaptation
Reflect
Memory
operate
Interact
Step 3: Outcome Attribute
Strategy Uncertain
 External
Context & Outcome
Deprecated Strategies
Step 4: Update hypotheses
Valid
Evidence
Invalid
Evidence
Evolve playbook if
Success patternObserved
Hypothesis: Offering a free trial to budget-
sensitive small-scale merchants lowers the
decision barrier and increases conversion rate
Preconditions: Budget-sensitive, Small-scale
Business
Success pattern: Merchant proactively asks
about campaign details
Failure pattern: Merchant perceives free as
low-quality and declines
success +1, confidence , new
pattern added
Matches
(a) The double-loop architecture. The outer loop maintains and evolves a strategy playbook P of testable hypotheses through
four steps after each interaction. The inner loop adapts to individual merchants across sessions using episodic memoryM i.
Inner Loop: Per-Merchant Adaptation : Free Trial for Small-scale Merchants
Budget
Sensitive
Merchant
Profile
Women's
Fashion
Small-scale
Merchant
Memory
Session 1: First Contact
Are you interested in our advertising products?
No, Budget is tight
You can have a free trial for 7 days, no
commitment
Let me think about it
You can see results first, then decide
Outcome: Pending
Reflect
Interested in free framing
Unclear on expected metrics
Fashion store, peak season July
Session 2: Follow-up
Worried about metrics last time. I prepared data
This looks solid
Projected CTR for your category
Let me look into it more
I can set up a free trial whenever you're
ready
Outcome: Considering
Reflect
Category data built credibility
Merchant needs time
Mention peak season next time as urgency lever
Session 3: Closing
Had a chance to look at the data?
The numbers look good
Peak season is 4 weeks away, early setup means better results
That makes sense
Want me to set up the campaign today?
Outcome: Converted
Reflect
Peak-season urgency was the decisive factor
Low-pressure closing works for cautious merchants
Pattern: data first →  build trust →  time pressure to close
OK, let's do it
Budget-sensitive, resists upfront
commitment
Responded well to free framing
Fashion store, peak season in July
User hung up
User hung up
Budgetsensitive, responds to low-risk framing,
pushing backfires
Free trial works, but needs category-specific data
Fashion store, peak season July, use as urgency
lever next time
Budget-sensitive: free trial removed risk; data
proof beats promises
Peak-season urgency works as closer, not opener
Conversion pattern: free trial →  real data →  time
pressure
(b) Detailed view of the inner loop for a single merchant across three sessions. Episodic memory accumulates observations from
each session and guides follow-up strategies, enabling the agent to build rapport and adapt its approach over time.
Figure 2: Overview of the SPAR framework. All strategies and merchant data shown are anonymized. The
illustration is a simplified example for readability. Real B2B sales scenarios involve more complex merchant profiles
and longer interaction sequences.
Hypothesis Evolution.For outcomes causally at-
tributed to the strategy, the agent applies structured
delta updates to the relevant hypothesis
P ←Φ(P, h∗, e)(5)
where e is the newly constructed evidence. The
LLM implements Φ by selecting from seven evolu-
tion actions, designed around aminimal revision
principlethat always prefers the smallest targeted
change sufficient to incorporate new evidence.Re-
inforce,Update,Condition, andNonepreserve ex-
isting hypotheses with increasing degrees of mod-
ification.Add,Merge, andDeprecaterestructure
the playbook more aggressively when incremental
updates are insufficient. Together these comple-
mentary actions cover evidence accumulation, hy-
pothesis refinement, and structural reorganization.
Exploration and Curation.The agent performs
fork discoveryafter each interaction, identifying
unexplored strategy directions from the dialogue as
exploration candidates. The playbook is dedupli-
cated at regular intervals, and the deprecation rule
in Eq. 3 is applied after every interaction.
4 Experiments
4.1 Experimental Setup
Dataset.We construct a multi-session B2B sales
evaluation dataset from 1,642 real conversations
between an experienced human sales team and mer-
chants on 1688, a major B2B online platform. Each
conversation is manually annotated with detailed
merchant profiles, behavioral archetypes, session-
level outcomes, and strategy labels.
4

Metric Score
Outcome agreement 98.7%
Key-behavior recall 91%
Turn-count deviation 0.9±1.3
Paired comparison accuracy 87%
Expert approval 89%
Table 1: Merchant simulator fidelity validated against
300 real conversations and human evaluation from the
sales team.
Merchant Simulator.We use GPT-4o as the sim-
ulated merchant, conditioned on a detailed profile
with target prices, behavioral traits, and session-
specific goals. We validate fidelity by replaying
300 real conversations and conducting a human
evaluation with the sales team. The simulator is
conditioned on the full conversation context from
real human merchant interactions, yielding 98.7%
outcome agreement as shown in Table 1. The 87%
paired comparison accuracy further confirms that
the simulator responds differently to strong and
weak strategies. Expert approval reaches 89%, val-
idating its use as a reliable evaluation proxy.
Baselines.We compare SPAR against three base-
lines.Direct Promptinguses the same backbone
LLM with only the item description and no mem-
ory or evolving playbook.Reflexion(Shinn et al.,
2023) generates a natural-language lesson after
each conversation and stores it per merchant as
self-reflective feedback for future interactions.Ex-
peL(Zhao et al., 2024) extracts reusable insights
from past interactions and retrieves them based on
task similarity to guide decision-making.
Metrics.We evaluate agents along three dimen-
sions of sales dialogue quality.
• Objection handlingmeasures whether the
agent recognizes the merchant’s core objec-
tion, responds to it directly, and supports its
response with concrete evidence.
• Dialogue qualityis assessed throughmono-
logue rate, the fraction of sessions dominated
by lengthy seller utterances, andrepetition
rate, the fraction of follow-up sessions that
duplicate earlier questions or arguments.
• Memory recallmeasures whether the agent
proactively references specific facts from prior
sessions before the merchant raises them, eval-
uated only after the first session.
For LLM-based evaluation, all metrics except repe-
tition rate are scored by an LLM evaluator (Zheng
et al., 2023) at the session level across all real con-
versations. Repetition rate is computed via text
similarity between consecutive sessions.
Hypothesis Design.The hypothesis schema is
derived from LLM-assisted analysis of 51,603 ses-
sion notes from a top-performing B2B sales team
on 1688 and validated against 3,637 sales cases.
Each hypothesis contains six fields:description,
preconditions,action steps,rationale,success and
failure patterns, and anevidenceset with causal
attribution labels. Confidence scoring and lifecy-
cle thresholds are similarly grounded in observed
patterns of how experienced salespeople adopt and
retire strategies. The session notes used for schema
design have no overlap with the 1,642 evaluation
conversations.
Implementation.All agents use GPT-4o as the
backbone LLM. The playbook is initialized with a
small set of domain-specific tentative seed strate-
gies and capped at 50 entries.
4.2 Results and Ablation
LLM-based Evaluation.Table 2 presents results
across baselines and ablation variants under two
judge models, where SPARleads on most met-
ricsunder both. Under GPT Eval, the advantage
is most pronounced onevidence support, where
SPAR achieves65.6% higherthan Direct Prompt-
ing and5.5% higherthan the strongest baseline,
showing that the double-loop architecture yields
more substantive selling arguments. SPAR also
achieves the lowest repetition rate at 0.002 and the
highest memory recall at 0.071. ExpeL and Reflex-
ion improve through experience accumulation, yet
both lack the structured hypothesis lifecycle that
allows SPAR to validate effective strategies and
retire failing ones. The recognition gain over the
strongest baseline is9.6%. Under Claude Eval,
SPAR leads the strongest baseline by16.6%on re-
sponse, cuts the repetition rate to0.003from 0.006,
and raises memory recall to0.064from 0.042.
Human Evaluation.Three domain experts an-
notate dialogues with 300+ real merchants under
blind conditions (Table 2). SPAR achieves thehigh-
est scores across all seven metrics, with a Sales
Quality of4.62 out of 5and evidence support at
0.926. The advantage is most visible onrepeti-
tionat0.132, an18.5%reduction over the next-
best method, confirming that playbook evolution
produces non-repetitive follow-up interactions. Di-
5

Objection Handling Dialogue Quality Memory Sales Quality
Method Recognize↑Respond↑Evidence↑Monologue↓Repetition↓Recall↑Score↑
GPT Eval
Direct Prompting 0.741 0.540 0.4280.186 0.005 – –
ExpeL 0.705 0.623 0.607 0.262 0.016 – –
Reflexion 0.759 0.638 0.672 0.221 0.017 0.053 –
SPAR w/o Inner Loop 0.684 0.579 0.596 0.281 0.018 – –
SPAR w/o Outer Loop 0.800 0.672 0.672 0.272 0.009 0.065 –
SPAR w/o Evolution 0.695 0.661 0.627 0.288 0.007 – –
SPAR0.832 0.729 0.709 0.221 0.002 0.071 –
Claude Eval
Direct Prompting 0.714 0.492 0.4150.178 0.006 – –
ExpeL 0.642 0.578 0.548 0.275 0.020 – –
Reflexion 0.728 0.584 0.621 0.211 0.024 0.042 –
SPAR w/o Inner Loop 0.635 0.542 0.536 0.289 0.018 – –
SPAR w/o Outer Loop 0.761 0.618 0.628 0.252 0.013 0.059 –
SPAR w/o Evolution 0.651 0.622 0.574 0.284 0.009 – –
SPAR0.798 0.681 0.662 0.205 0.003 0.064 –
Human Eval
Direct Prompting 0.762 0.884 0.741 0.306 0.346 – 2.83
ExpeL 0.871 0.857 0.879 0.384 0.337 – 3.64
Reflexion 0.846 0.903 0.896 0.318 0.162 0.762 3.97
SPAR0.921 0.938 0.926 0.258 0.132 0.813 4.62
Table 2: Results on the B2B sales evaluation dataset. Bold with underline marks the best and underline marks
the second-best in each column. Recognize, Respond, and Evidence measure objection handling, Monologue and
Repetition measure dialogue quality, and Recall measures proactive memory callback in follow-up sessions. GPT
Eval and Claude Eval score the same dialogues with GPT-4o and with Claude Sonnet 4.5. Sales Quality is rated by
three domain experts on a 1–5 scale under blind conditions (rubric in Appendix C).
rect Prompting scores competitively on response at
0.884, reflecting the strong zero-shot capability of
the backbone LLM, but falls behind on recognition
at0.762and evidence at0.741, where structured
learning provides the largest gains. The perfor-
mance gaps are narrower than in LLM-based eval-
uation under both judge models, yet theranking
across methods remains consistent, confirming
that the automated metrics reliably capture quality
differences perceived by experienced salespeople.
Ablation Study.The ablation variants isolate
each component’s contribution. Under GPT Eval,
removing the inner loop causes thelargest degra-
dation, with recognition dropping17.8%and
memory recall falling to zero, showing thatper-
merchant memory is essentialfor cross-session
continuity. Removing the outer loop retains strong
recognition at only 3.8% below SPAR but lags
7.8%on response and5.2%on evidence, con-
firming thatthe evolving playbook drives deeper
objection handling. Removing evolution freezes
the playbook after seeding, falling9.3%behind
on response and11.6%on evidence, as the agent
cannot refine strategies from new experience. Un-
der Claude Eval, recognition falls20.4%without
the inner loop and evidence falls13.3%without
evolution. These results confirm thatall three com-
ponents are necessary and mutually reinforcing.
Method Conv.↑Sessions↓M1 Rate↑
Direct Prompting – – –
ExpeL +1.1% +0.3% +9.2%
Reflexion +9.6%−4.6% +27.9%
SPAR w/o Inner Loop +10.1%−6.3% +34.5%
SPAR w/o Outer Loop +12.6% −11.2% +22.3%
SPAR w/o Evolution +9.6%−3.0% +18.7%
SPAR+15.8% −9.2% +35.8%
Table 3: Online A/B test results on the 1688 platform.
All values are relative changes over the Direct Prompt-
ing baseline. Conv. is conversion rate, Sessions is the
number of outreach sessions needed, and M1 Rate is
first-milestone achievement rate. Bold with underline
marks the best and underline marks the second-best.
4.3 Online A/B Test
To validate that simulation improvements transfer
to the real world, we deploy all methods on the
1688 platform in a live A/B test with over 30,000
merchants per group. Conversion is defined as
completing a target transaction within 7 days of
the final outreach session. The M1 high-intent rate
measures how often merchants reach high-intent
status during the sales process. Table 3 reports the
relative change over the Direct Prompting baseline
on three business metrics. Statistical significance is
assessed via a two-proportion z-test with 95% CIs
from 1,000-iteration bootstrap, and all SPAR lifts
are significant atp <0.001.
6

SPAR achieves thehighest conversion lift at
+15.8%and thehighest M1 achievement lift at
+35.8%, while reducing outreach sessions by9.2%.
The conversion advantage over the next-best vari-
ant is25.4%, confirming that the full double-loop
architecture delivers the strongest end-to-end sell-
ing capability in production. At scale, this yields
operational savings while easing merchant fatigue
from repeated contact.
The ablation pattern mirrors the simulation re-
sults. SPAR w/o Outer Loop achieves the second-
highest conversion at +12.6% and the largest ses-
sion reduction at −11.2%, while SPAR w/o In-
ner Loop yields +10.1% conversion with the high-
est M1 lift among ablation variants at +34.5%.
SPAR w/o Evolution drops M1 to +18.7%, con-
firming thatstrategy evolution nearly doubles
the M1 gain. ExpeL shows minimal improvement
at +1.1% conversion, suggesting that unstructured
insight accumulation provides limited benefit in
multi-session B2B sales. We provide a qualitative
analysis of playbook evolution in Appendix A.
5 Conclusion
We presented SPAR, a self-evolving framework
that models selling strategies as testable hypotheses
and refines them through a double-loop architecture
with causal attribution. In a live A/B test on the
1688 platform with over 200,000 merchants, SPAR
achieves +15.8% conversion lift and +35.8% high-
intent merchant growth. Simulation analysis shows
SPAR outperforms the strongest baseline by 9.6%
on objection recognition and 5.5% on evidence
support. These results are validated in real-world
B2B commercial outreach where merchants make
purchasing decisions.
Limitations
SPAR requires multiple interactions before the
playbook meaningfully evolves, so early merchants
do not benefit from accumulated experience. This
cold-start cost is inherent to any online learning
approach, and investigating warm-start techniques
such as transferring playbooks across domains is a
promising direction for future work.
The strategy evolution process relies on LLM
reasoning, which inherently introduces a degree
of randomness and unpredictability in playbook
updates. While the confidence mechanism and
lifecycle thresholds provide gradual self-correction
over time, individual evolution decisions may be
suboptimal. Incorporating an auxiliary verification
agent to validate proposed strategy changes before
they enter the playbook is a promising direction for
improving reliability.
Merchants are processed sequentially in our cur-
rent experiments. In practice, sales teams handle
multiple merchants concurrently, where parallel
interactions may produce fundamentally different
learning dynamics. Evaluating SPAR in concurrent
settings remains future work.
Acknowledgments
This work is supported by the CCF-1688 Yuanbao
Cooperation Fund (No. CCF-Alibaba2025007) and
the Key-Area Research and Development Program
of Guangdong Province (No. 2023B0303030001).
References
Federico Bianchi, Patrick John Chia, Mert Yuksekgonul,
Jacopo Tagliabue, Dan Jurafsky, and James Zou.
2024. How well can llms negotiate? negotiationarena
platform and analysis. InInternational Conference
on Machine Learning, pages 3935–3951. PMLR.
Wen Chang and Yun-Nung Chen. 2024. Injecting sales-
person’s dialogue strategies in large language mod-
els with chain-of-thought reasoning. InFindings of
the Association for Computational Linguistics: ACL
2024, pages 3798–3812.
Ssu Chiu, Maolin Li, Yen-Ting Lin, and Yun-Nung
Chen. 2022. Salesbot: Transitioning from chit-chat
to task-oriented dialogues. InProceedings of the 60th
Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 6143–
6158.
Yang Deng, Wenxuan Zhang, Wai Lam, See-Kiong
Ng, and Tat-Seng Chua. 2024. Plug-and-play policy
planner for large language model powered dialogue
agents. InInternational Conference on Learning
Representations, volume 2024, pages 10058–10090.
Yao Fu, Dong-Ki Kim, Jaekyeom Kim, Sungryull
Sohn, Lajanugen Logeswaran, Kyunghoon Bae, and
Honglak Lee. 2024. Autoguide: Automated gener-
ation and selection of context-aware guidelines for
large language model agents.Advances in Neural
Information Processing Systems, 37:119919–119948.
Qi Gou, Zehua Xia, Li Juan, Qingyang Zhao, and Wen-
jing Yang. 2025. Advancing e-commerce merchants
telemarketing with synthetic data-driven llms. In
Proceedings of the 2025 Conference on Empirical
Methods in Natural Language Processing: Industry
Track, pages 2146–2154.
He He, Derek Chen, Anusha Balakrishnan, and Percy
Liang. 2018. Decoupling strategy and generation in
7

negotiation dialogues. InProceedings of the 2018
Conference on Empirical Methods in Natural Lan-
guage Processing, pages 2333–2343.
Zexue He, Jiaxin Pei, and Alex Pentland. 2026. Memo-
ryarena: Benchmarking agent memory in interdepen-
dent multi-session agentic tasks. In4th Workshop on
Towards Knowledgeable Foundation Models at ACL
2026.
Tongyoung Kim, Jeongeun Lee, SooJin Yoon, SungH-
wan Kim, and Dongha Lee. 2025. Towards person-
alized conversational sales agents: Contextual user
profiling for strategic action. InFindings of the Asso-
ciation for Computational Linguistics: EMNLP 2025,
pages 5131–5154, Suzhou, China. Association for
Computational Linguistics.
Hao Li, Chenghao Yang, An Zhang, Yang Deng, Xi-
ang Wang, and Tat-Seng Chua. 2025. Hello again!
llm-powered personalized agent for long-term dia-
logue. InProceedings of the 2025 Conference of the
Nations of the Americas Chapter of the Association
for Computational Linguistics: Human Language
Technologies (Volume 1: Long Papers), pages 5259–
5276.
Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler
Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon,
Nouha Dziri, Shrimai Prabhumoye, Yiming Yang,
et al. 2023. Self-refine: Iterative refinement with
self-feedback.Advances in neural information pro-
cessing systems, 36:46534–46594.
Adyasha Maharana, Dong-Ho Lee, Sergey Tulyakov,
Mohit Bansal, Francesco Barbieri, and Yuwei Fang.
2024. Evaluating very long-term conversational
memory of llm agents. InProceedings of the 62nd
Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 13851–
13870.
Thomas Mesnard, Theophane Weber, Fabio Viola, Shan-
tanu Thakoor, Alaa Saade, Anna Harutyunyan, Will
Dabney, Thomas S Stepleton, Nicolas Heess, Arthur
Guez, et al. 2021. Counterfactual credit assignment
in model-free reinforcement learning. InInterna-
tional Conference on Machine Learning, pages 7654–
7664. PMLR.
Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Mered-
ith Ringel Morris, Percy Liang, and Michael S Bern-
stein. 2023. Generative agents: Interactive simulacra
of human behavior. InProceedings of the 36th an-
nual acm symposium on user interface software and
technology, pages 1–22.
Vishnu Sarukkai, Zhiqiang Xie, and Kayvon Fatahalian.
2026. Self-generated in-context examples improve
llm agents for sequential decision-making tasks.Ad-
vances in Neural Information Processing Systems,
38:64392–64425.
Ryan Shea, Aymen Kallala, Xin Lucy Liu, Michael W
Morris, and Zhou Yu. 2024. Ace: A llm-based nego-
tiation coaching system. InProceedings of the 2024
conference on empirical methods in natural language
processing, pages 12720–12749.
Noah Shinn, Federico Cassano, Ashwin Gopinath,
Karthik Narasimhan, and Shunyu Yao. 2023. Re-
flexion: Language agents with verbal reinforcement
learning.Advances in neural information processing
systems, 36:8634–8652.
Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Man-
dlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and
Anima Anandkumar. 2024. V oyager: An open-ended
embodied agent with large language models.Trans-
actions on Machine Learning Research.
Shu Wang, Edwin Yu, Oscar Love, Tom Zhang,
Tom Wong, Steve Scargall, and Charles Fan. 2026.
Memmachine: A ground-truth-preserving mem-
ory system for personalized ai agents.Preprint,
arXiv:2604.04853.
Jing Xu, Arthur Szlam, and Jason Weston. 2022. Be-
yond goldfish memory: Long-term open-domain con-
versation. InProceedings of the 60th annual meeting
of the association for computational linguistics (vol-
ume 1: long papers), pages 5180–5197.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
Shafran, Karthik Narasimhan, and Yuan Cao. 2022.
React: Synergizing reasoning and acting in language
models.arXiv preprint arXiv:2210.03629.
Haolan Zhan, Yufei Wang, Zhuang Li, Tao Feng,
Yuncheng Hua, Suraj Sharma, Lizhen Qu,
Zhaleh Semnani Azad, Ingrid Zukerman, and
Reza Haf. 2024. Let’s negotiate! a survey of
negotiation dialogue systems. InFindings of the
Association for Computational Linguistics: EACL
2024, pages 2019–2031.
Qizheng Zhang, Changran Hu, Shubhangi Upasani,
Boyuan Ma, Fenglu Hong, Vamsidhar Kamanuru, Jay
Rainton, Chen Wu, Mengmeng Ji, Hanchen Li, Ur-
mish Thakker, James Zou, and Kunle Olukotun. 2026.
Agentic context engineering: Evolving contexts for
self-improving language models. InThe Fourteenth
International Conference on Learning Representa-
tions.
Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu
Lin, Yong-Jin Liu, and Gao Huang. 2024. Expel:
Llm agents are experiential learners. InProceedings
of the AAAI Conference on Artificial Intelligence,
volume 38, pages 19632–19642.
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan
Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin,
Zhuohan Li, Dacheng Li, Eric Xing, et al. 2023.
Judging llm-as-a-judge with mt-bench and chatbot
arena.Advances in neural information processing
systems, 36:46595–46623.
8

A Playbook Evolution Analysis
We examine how the strategy playbook evolves dur-
ing the online A/B test to illustrate the hypothesis
lifecycle. The playbook is initialized with six ten-
tative seed strategies. As larger-scale manual anal-
ysis is infeasible, we qualitatively examine its evo-
lution on a sample of 200+ real merchants drawn
from the A/B test.
Lifecycle Progression.Two of the six seed strate-
gies are promoted toactivestatus through accumu-
lated evidence. Strategy H002, which instructs the
agent to reference prior conversations with return-
ing merchants, accumulates 108 strategy-attributed
successes and is promoted after reaching the ev-
idence threshold. Strategy H001, which recom-
mends offering trial programs when merchants hes-
itate, follows a similar trajectory with 89 attributed
successes. Two other seed strategies are deprecated
after repeated failures, illustrating that the lifecycle
correctly retires ineffective approaches. The evolu-
tion process also discovers and validates five new
strategies beyond the initial seeds, demonstrating
that the playbook grows organically from interac-
tion experience.
Fork Discovery.The evolution process identi-
fies 9 unexplored strategy directions from dialogue
analysis. These directions capture recurring pat-
terns that existing strategies do not address, such
as offering hands-on onboarding support and pro-
viding industry-specific case studies to build cred-
ibility. Each direction is logged with the number
of times it appears across interactions, creating a
prioritized queue for future hypothesis generation.
Attribution Filtering.The causal attribution
mechanism labels a subset of outcomes as exter-
nally driven, preventing them from distorting strat-
egy confidence scores. When a merchant walks
away due to a recently reduced internal budget
rather than a flaw in the agent’s approach, the attri-
bution module assigns label x and the correspond-
ing evidence does not affect c(h). This filtering
ensures that the playbook reflects genuine strategy
effectiveness rather than environmental noise.
B Algorithm
Algorithm 1 describes the complete SPAR pipeline.
The outer loop iterates over merchants sequentially.
For each merchant, the inner loop runs up to K
sessions. At each session, the agent selects a strat-
egy hypothesis h∗ from the non-deprecated set P +
using a scoring function that considers precondi-
tion alignment, prior interaction history, and explo-
ration priority I(h). After dialogue execution, a
reflection is stored in episodic memory Mi. The
outer loop then constructs evidence from the in-
teraction, assigns a causal attribution label, and
triggers playbook evolution Φ only for strategy-
attributed outcomes. The session loop terminates
early on deal closure (o= 1 ) or merchant decline
with no follow-up opportunity (o=−1).
Algorithm 1SPAR Double-Loop Learning
Require: Merchants 1, . . . , Nwith profiles {pi},
max sessionsK, playbookP
Ensure:Evolved playbookP
1:fori= 1toNdo
2:Initialize episodic memoryM i ← ∅
3:fork= 1toKdo
4:// Inner Loop - Strategy Selection
5:h ∗ ←arg max h∈P + f(h, pi, Mi, I(h))
6:Conduct dialogue usingh ∗, observeo i,k
7:Generate reflection, store inM i
8:// Outer Loop - Evolution
9: Construct evidence e from pi, h∗, oi,k,
and dialogue
10:Assign attributiona(e)∈ {s, x, u}
11:Appendeto evidence setE(h ∗)
12:ifa(e) =sthen
13:P ←Φ(P, h ∗, e)
14:end if
15:Updateσ(h)for allh∈ P
16:ifo i,k = 1then
17:break// deal closed
18:else ifo i,k =−1then
19:break// declined, no follow-up
20:end if
21:end for
22:end for
23:returnP
C Sales Quality Rubric
Three domain experts rate each dialogue on a 1–5
scale based on the following rubric. Each level
describes both overall dialogue quality and selling-
strategy execution along four dimensions, namely
strategic fit,objection handling,rapport building,
andclosing effectiveness.
• 5 – Excellent.The agent demonstrates
outstanding professional handling and effec-
tively guides toward conversion. Strategic fit
9

matches the merchant’s profile and stage pre-
cisely, objections are addressed with concrete
evidence, rapport is consistently built across
sessions, and closing is clear and well-timed.
Suitable as a reference example for sales train-
ing.
• 4 – Good.The agent handles the conversa-
tion professionally. Strategic fit is generally
appropriate, objections are addressed with rel-
evant supporting points, rapport is established
across sessions, and closing is clear, with only
minor opportunities for improvement.
• 3 – Acceptable.The agent completes the
basic sales flow. Strategic fit is partial, objec-
tions are acknowledged but not always sup-
ported with concrete evidence, rapport is lim-
ited, and closing lacks decisiveness.
• 2 – Poor.The agent makes noticeable errors.
Strategic fit is weak or mismatched, key ob-
jections are missed or inadequately handled,
rapport is minimal, and no clear closing is of-
fered, reducing the likelihood of conversion.
• 1 – Unacceptable.The agent provides irrel-
evant or inaccurate responses. Strategic fit is
broken, objections are ignored or aggravated,
no rapport is established, and the conversation
may harm the merchant relationship.
10
