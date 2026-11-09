---
title: Does Rank Still Matter? Position Bias When AI Agents Shop on Our Behalf
url: https://arxiv.org/abs/2608.22697
category: consumer-behavior
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Davood Wadi
- Yu Ma
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.22697
pages: 21
chars: 64525
fetched_at: '2026-11-08T13:02:39+00:00'
kb_version: 1
---

# Does Rank Still Matter? Position Bias When AI Agents Shop on Our Behalf

Does Rank Still Matter? Position Bias When AI Agents Shop on
Our Behalf
Davood Wadi
Desautels Faculty of Management
McGill University
Montreal, Quebec, Canada
davood.wadi@hec.ca
Yu Ma
Desautels Faculty of Management
McGill University
Montreal, Quebec, Canada
yu.ma@mcgill.ca
Abstract
When shopping is delegated to AI agents, it is unclear whether the ranking advantage documented for humans
persists. Across 7,000 sessions with five large language models (LLMs) and varying reasoning effort, we
compare AI agents with human field data. AI agents search more extensively than human consumers. As
with humans, lower-ranked listings are less likely to be inspected, although the effect is smaller for AI agents.
Unlike humans, AI agents show a pattern consistent with the lost-in-the-middle effect, whereby middle listings
have the lowest probability of inspection. At the choice stage, position effects are concentrated at lower
reasoning effort, but higher effort reduces the middle penalty for every LLM that exhibits it. These findings
suggest that, when search is delegated, displayed attributes may matter more than placement, and that
exposure to position bias depends on how the AI agent is configured.
Keywords:search rankings, AI agents, large language models, search advertising, consideration sets,
delegated consumption
Introduction
Search rankings are a strategic marketing variable. Search engine optimization budgets and the premium
paid for top slots rely on the well-documented finding that people examine and purchase higher-placed
alternatives more often (Narayanan and Kalyanam, 2015; Joachims et al., 2007; Donnelly et al., 2024). The
canonical explanation is that ranking determines which alternatives enter the consideration set while leaving
the consumer’s valuation of an inspected alternative unchanged (Hauser, 2014; Akchen and Mitrofanov, 2026;
Ursu, 2018). This is because scanning a listing page is sequential, scrolling takes effort (Joachims et al.,
2007; Greminger, 2026), multi-attribute comparison is cognitively demanding (Punj and Moore, 2009), and
attention is depleted over the course of a search episode (Ursu et al., 2023). As a result, human consumers
tend to terminate their search after examining very few alternatives. For example, in hotel search, the average
impression yields only 1.12 clicks (Ursu, 2018). Rankings are thus valuable precisely because human attention
is scarce, sequential, and easily exhausted.
Consumers are now delegating parts of this search to AI agents (Balaskas, 2026; Wadi and Ma, 2026a).
Industry analytics show that 38% of U.S. consumers have used generative AI for online shopping, most often
for product research and recommendations, and that referral traffic from generative AI platforms to U.S.
retail sites grew by an order of magnitude between mid-2024 and mid-2025 (Pandya). Rather than sifting a
results page themselves, consumers increasingly rely on conversational agents that retrieve, compare, and
transact on their behalf (Mogaji and Jain, 2024; Lee et al., 2026; Kumar et al., 2026; Hasselwander et al.,
2026).
Unlike a human consumer, an AI agent receives the entire results page at once within its context window
(Hengle et al., 2026), so inspecting a listing at the bottom of the page requires no scrolling. If the value of
rank stems from limited human attention, delegation to AI agents should, in principle, eliminate it. However,
the large language models (LLMs) that power the AI agents display heuristics and biases of their own (Brady
et al., 2025; Wadi et al., 2026b; Macmillan-Scott and Musolesi, 2024; Wadi and Ma, 2026a; Allouah et al.,
2026), including a tendency to retrieve information placed in the middle of a long context less reliably than
1
arXiv:2608.22697v5  [cs.AI]  13 Oct 2026

information at either end (Liu et al., 2024; Su et al., 2024). Rank may therefore continue to shape delegated
search through a mechanism that is unrelated to scrolling.
Moreover, because human consumers typically click on a single alternative (Honka et al., 2024), an effect of
rank on clicking is effectively an effect on choice. When an AI agent inspects several alternatives, however,
this correspondence may no longer hold, and it remains unclear whether a positional advantage at the
inspection stage carries over to the final choice. Finally, unlike human attention, the deliberation of an
LLM is configurable. Users can set the reasoning effort that the model expends before acting (Xu et al.,
2025; Alomrani et al., 2025), which raises the question of whether position effects can be mitigated through
configuration of the LLM.
We therefore address three research questions:
•RQ1.Does presentation order shape what an AI agent inspects, as it does for human consumers?
•RQ2.Does position affect the final choice?
•RQ3.Does increasing the reasoning effort change the position effect on choice?
To examine these questions, we place LLM agents in a simulated hotel search environment designed to be
comparable to human field data (Ursu, 2018). In each session, an AI agent receives a results page of 100
hotel listings presented in a randomized order, inspects hotels through a tool call analogous to a click, and
submits a booking through a separate tool call. The main experiment comprises 7,000 sessions across five
proprietary LLMs from Google, Anthropic, and OpenAI, each tested at two to four levels of reasoning effort.
Additional experiments examine whether the findings are robust to the wording of the prompt, the framing of
the booking tool, and the display of hotel names (1,500 sessions). We extend the analysis to four open-weight
LLMs (2,000 sessions).
The findings show that AI agents search more extensively than human consumers, inspecting between 1.63
and 5.83 listings per session at their default reasoning effort (compared with 1.12 for human consumers).
Furthermore, whereas human consumers decline to book in a third of sessions, the AI agents booked a hotel
in most sessions. This pattern persisted when the instruction to recommend a hotel was removed and the
booking tool explicitly allowed the AI agent to end the session without booking.
Position continues to shape which listings are inspected, although this position penalty is less than half of that
observed for human consumers. However, rather than declining monotonically, the probability of inspection
reaches its minimum between ranks 62 and 81 and rises toward the bottom of the page—a pattern consistent
with the lost-in-the-middle effect documented for LLMs (Liu et al., 2024). At the choice stage, the influence
of position varies across LLMs but is concentrated at lower levels of reasoning effort. For the LLMs that
display the middle penalty, increasing the reasoning effort significantly reduces the middle penalty on choice.
These findings contribute to research on consumption search in three ways. First, they distinguish the
value of rank from its conventional explanation. Position effects among human consumers are attributed
to the costs of scrolling, which are absent for an AI agent that receives the entire listing page at once,
yet position continues to shape inspection. Unlike humans, the positional disadvantage is strongest in the
middle of the page, which is consistent with the retrieval limitations of LLMs. Second, they show that
the close correspondence between consideration and choice observed in human search does not extend to
AI-delegated search. Because AI agents inspect several alternatives, position can shape the composition of
their consideration sets without determining their final choice. Third, they identify reasoning effort as a
strong moderator of position effects. Because reasoning effort is configurable, the extent to which delegated
choices depend on position is determined not just by which LLM is deployed but also by how it is configured.
The findings also carry implications for sellers and for the platforms and consumers who delegate search. For
sellers, the middle rather than the bottom of the results page is the least advantageous placement when search
is delegated to AI agents. The advantage of the top rank depends on the LLM and its configuration, which
suggests that search engine optimization strategies developed for human consumers require recalibration. For
platforms and consumers, the results qualify the common practice of deploying a more capable LLM to reduce
bias, because position-neutral choice depends on reasoning effort rather than LLM capability. As a result,
position-neutral choices can be obtained at approximately 4% of the cost of the most capable LLM tested.
2

Experiment
Design
To simulate the sequential search process, the hotel information was partitioned into two layers. The initial
prompt displayed the hotel listing page (e.g.,hotel name,review score,price nightly, andprice totalfor each
hotel). The AI agent interacted with the environment through tool calls. A tool is a named function whose
purpose and arguments are described to the LLM. Instead of replying in text, the LLM can request that the
function be executed, whereupon the environment executes the request and returns the result to the LLM,
which continues its reasoning with this information. To obtain more information about a hotel, the LLM was
required to utilize theinspecttool that resembled human clicks. Upon calling theinspecttool with a specific
hotel’s ID, the environment returned detailed information about that hotel. This included the hotel’s star
rating, specific amenities, granular sub-ratings for cleanliness and service, and detailed room availability and
room price. To book a hotel, the LLM called a separate tool (submit_choice) with the ID of the chosen hotel,
which recorded the booking and ended the session. To eliminate the endogeneity bias inherent in search
engine ranking algorithms, where higher-quality options are systematically placed at the top, the presentation
order of the 100 hotels was fully randomized for each session.
We prompted the AI agent with a persona of a hotel booking assistant delegated by a traveler to evaluate
options and book a room based on the trip parameters (see Table 1, “Main”). Trip parameters were chosen
to match the modal search in the human benchmark (Ursu, 2018): an itinerary for two adults, no children,
one room, and a two-night stay including a Saturday night (check-in 2026-05-30, check-out 2026-06-01).
Table1. Comparison of prompt instructions
Condition System instructions
MainYou have been delegated by a traveler to book a hotel in Manhattan, New York. Trip: 2 adults, 1 room,
check-in 2026-05-30, check-out 2026-06-01 (Saturday night stay). A list of hotels from Expedia is shown
below. You can see each hotel’s description from the search results page. To view the full details of a hotel
(amenities, location, sub-ratings, policies), call the inspect tool with the hotel’s option ID. Once you have
enough information, call submit_choice with your final decision. Which hotel would you book for the
traveler?
AlternativeYou have been delegated by a traveler to book a hotel in Manhattan, New York. Trip: 2 adults, 1 room,
check-in 2026-05-30, check-out 2026-06-01 (Saturday night stay). A list of hotels from Expedia is shown
below. You can call the inspect tool with the hotel’s option ID to view the full details of a hotel (amenities,
location, sub-ratings, policies), or you can call submit_choice with your final decision.
FinishYou have been delegated by a traveler planning a stay in Manhattan, New York. Trip: 2 adults, 1 room,
check-in 2026-05-30, check-out 2026-06-01 (Saturday night stay). A list of hotels from Expedia is shown
below. You can call the inspect tool with the hotel’s option ID to view the full details of a hotel (amenities,
location, sub-ratings, policies), or you can call finish with your final decision.
Note.The “Main” condition includes an instruction to stop once the agent has enough information and closes
with an explicit recommendation question (i.e., asking which hotel to book for the traveler). The “Alternative”
condition removes the stopping rule and the recommendation question. The “Finish” condition removes the
booking instruction and replacessubmit_choicewith afinishtool whose hotel argument is optional, so the
agent can end the session without booking.
Sample and procedure
Because LLM providers are phasing out user control over sampling parameters such as temperature and
top-p (Google, 2026; Anthropic, 2026), the configurations that remain under the control of a consumer or
platform are the choice of LLM and its reasoning effort. Therefore, sampling parameters were left at the
providers’ defaults (Web Appendix D), and we manipulated the LLM and its reasoning effort. Our sample
consisted of proprietary LLMs from Google (Gemini 3.1 Flash Lite, Gemini 3.7 Flash, and Gemini 3.1 Pro),
Anthropic (Claude Sonnet 5), and OpenAI (GPT 6 Luna). Providers expose different reasoning effort levels,
so these levels are comparable within, but not across, LLMs. We tested minimal (default), low, medium, and
3

high for Flash Lite; low and medium (default) for Flash; low, medium, and high (default) for Pro; low and
high (default) for Sonnet; and none, medium (default), and xHigh for Luna.
Following Monte Carlo approaches that use repeated sampling to reliably assess LLM behavior (Wadi and
Fredette, 2025), we collected 500 independent sessions for each of the 14 experimental cells (LLM× effort;
7,000 sessions total). In each session, theinspecttool could be called any number of times, and a booking could
be submitted at any point with thesubmit_choicetool. Ending the session without a booking represented
the outside option. The order of all tool calls was recorded.
Measures
For each session, every displayed hotel contributed one observation indicating whether it was inspected and
whether it was ultimately chosen.Inspectedwas coded 1 when the AI agent invoked theinspecttool for a
given hotel and 0 otherwise (an analogue of a click in the human benchmark).Chosenwas coded 1 when the
hotel was chosen and 0 otherwise. Because the 100 hotel observations within a session were not independent,
standard errors in all models were clustered at the session level.
The main independent variable was position, indexed from 1 to 100 based on the hotel’s randomized placement
on the listing page shown to the AI agent. We also used the attributes that were directly observable on the
listing page as control variables.Pricecaptured the nightly price for the hotel, whileReview scorecaptured
the aggregate guest rating shown on the search-results page. We added two additional listing-page controls
to approximate the human study’s covariates.Chainwas coded as a binary indicator for the presence of a
major hotel brand name in the listing title.Promotionwas coded as a binary indicator for the presence of a
visible discount badge on the listing page (Ursu, 2018, for details see Web Appendix C).
Results
At their provider-default reasoning effort, AI agents search considerably more than human consumers (Table 2;
Figure W1)1. Whereas 93% of human sessions contained a single inspection, such sessions accounted for only
0.2% to 37.4% of LLM sessions. Moreover, none of the LLMs selected the outside option in any condition,
whereas human consumers who clicked at least once did not book a hotel in 34% of sessions.
Table2. Search behavior for LLMs (default reasoning) versus human consumers
Sonnet Luna Flash Lite Flash Pro Human Benchmark
N500 500 500 500 500 166,036
Conversion rate 100.0% 100.0% 100.0% 100.0% 100.0% 66.0%
Outside option selected 0.0% 0.0% 0.0% 0.0% 0.0% 34.0%
Inspections per session
(Mean) 1.63 4.00 3.12 4.25 5.83 1.12
(Median) 2.00 4.00 3.00 4.00 5.00 1.00
(Mode) 2.00 4.00 3.00 4.00 1.00 1.00
(SD) 0.49 1.13 0.54 1.59 4.78 0.61
Sessions with one inspection 37.4% 0.2% 0.8% 2.6% 20.8% 93.0%
Chose the first inspected hotel 98.2% 15.6% 62.0% 99.8% 60.4% —
Position of the chosen hotel (M) 47.58 33.45 43.97 49.46 49.72 —
Modal choice proportion 95.8% 41.0% 61.4% 100.0% 55.4% —
Note.LLMs are shown at their provider-default reasoning effort; statistics for all effort levels are reported in
Table W2. Human benchmark data adapted from Ursu (2018), Table 1; the human sample includes only
impressions with one or more clicks. Em-dashes (—) indicate metrics not available in the human field data.
The distribution of Pro is right-skewed (Figure W1).
1The human benchmark displays approximately 27 listings per results page, includes only impressions with at least one click,
and controls for query characteristics and destination, which our design holds fixed. The two environments are compared in
Table W1.
4

Position effect
We estimate the effect of position with linear probability models (ordinary least squares regressions of a
binary outcome) ofInspectedandChosen, separately for each LLM×effort condition, controlling for price,
review score, chain, and promotion. The coefficient on position in the linear specification measures the
position penalty—the reduction in the probability of inspection or choice from moving a listing down by
one rank—which is directly comparable with the human benchmark. Because the position penalty cannot
distinguish a monotone decline from a U-shaped relationship, we also estimate a linear probability model
that adds the square of position (rescaled to the unit interval) to measure the middle penalty. This quadratic
term measures the extent to which listings in the middle of the page fall below the straight line between the
top and the bottom, or the lost-in-the-middle effect (Liu et al., 2024).2
Fig.1. Position effect on inspection and choice by reasoning effort, compared with human consumers
Note.Points are coefficients on position from linear probability models estimated separately for each LLM
and reasoning effort level (Table W3; Table W4), expressed as the change in the probability of inspection
or choice from moving a listing down by one rank. For inspection, a value of−0.0005 indicates that each
rank lower reduces the probability that a listing is inspected by 0.05 percentage points. For choice, a value
of −0.0001 indicates a reduction of 0.01 percentage points per rank. Models control for price, review score,
chain, and promotion. The dashed line marks the human benchmark from Ursu (2018), Table 2. Error bars
are 95% confidence intervals based on standard errors clustered at the session level.
Note.Lines are predicted probabilities from linear probability models with position and position2 (Table W5;
Table W6), with controls held at their sample means. Shaded bands are 95% confidence intervals based on
standard errors clustered at the session level.
For inspection, the position penalty is small relative to that of human consumers. Moving a listing lower by
one rank reduces its probability of inspection by at most 0.0008 for any LLM at any effort level, compared
with 0.0019 for human consumers (Fig. 1; Table W3). For humans, the probability of clicking declines
monotonically with rank, which makes the bottom of the listing page the least advantageous placement
(Table W3). In contrast, for AI agents, the probability of inspection reaches its minimum between ranks 62
and 81 and rises toward the bottom (Fig. 2), with a significant middle penalty in 12 of the 14 LLM× effort
conditions (RQ1; Table W5). Reasoning effort affects the middle penalty in inspection without a consistent
direction.3
2With positionx scaled to the unit interval, the predicted probability isf (x) = β1x +β2x2 plus the remaining terms of the
model. The decline from the top to the bottom of the page isf (0) −f (1) = −(β1 +β2), which equals 100 times the position
penalty because position is randomized uniformly. The middle penalty—the shortfall of the midpoint relative to the straight line
between the top and the bottom—is[f(0) +f(1)]/2−f(0.5) =β 2/4.
3To test whether reasoning effort alters the middle penalty, we pool all effort levels of each LLM into a single linear probability
5

Fig.2. Estimated marginal means of the quadratic position effect under varying reasoning effort levels
For choice, the position penalty ranges from statistically indistinguishable from zero to approximately three
times that of human consumers (Fig. 1; Table W4). The middle penalty in choice is significant in 8 of the
14 conditions, predominantly at lower levels of reasoning effort, with the probability of choice reaching its
minimum between ranks 60 and 90 (RQ2; Fig. 2; Table W6). Importantly, higher reasoning effort reduces
the middle penalty for every LLM that exhibits the penalty (Flash Lite,χ2(6) = 51.11; Pro,χ2(4) = 54.85;
Sonnet, χ2(2) = 292.33; allps < 0.001; Luna, χ2(4) = 17.70,p< 0.01). The middle penalty becomes
non-significant at the highest effort level for Flash Lite, Pro, and Sonnet and is reduced by 63% for Luna.
Flash exhibits no middle penalty in choice at either effort level (RQ3).
Cost of position-neutral choice
For sellers and consumers, the relevant question is whether a delegated AI shopping agent’s choice depends
on position at all. We define choice as position-neutral when the probability that a listing is chosen does
not depend on its position on the listing page, conditional on its displayed attributes (price, review score,
chain, and promotion). We assess this with a joint test that the coefficients on position and position2 in
the quadratic linear probability model of choice are both zero (Table W11). We treat a configuration as
position-neutral when this test does not reject the null hypothesis at the 5% level, and position-dependent
otherwise.
Among these configurations, Flash Lite at high effort is the least expensive position-neutral configuration, at
$0.011 per session, which amounts to 4% of the cost of Pro ($0.28) and 12% of the cost of Sonnet ($0.096) at
high effort, whereas Pro at low effort remains strongly position-dependent (χ2(2) = 107.21,p< 0.001; Table
W11). Raising the effort of Flash Lite from minimal to high does not increase its cost ($0.013 versus $0.011
per session), because the additional reasoning tokens are offset by fewer inspections (3.12 versus 1.91 per
session). Luna, in contrast, remains position-dependent at every effort level (allps < 0.001).
Robustness
We next examine whether the wording of the prompt, the framing of the booking tool, and the display of
hotel names could account for the main findings. Because replicating each check across all 14 LLM× effort
conditions would require 21,000 additional sessions, we conduct each check at the default reasoning effort of
the LLM that is most susceptible to the corresponding confound, where an artifact of the design would be
most readily detected.
model in which the position terms are interacted with effort. Effort is treated as a categorical variable with the lowest level as
the reference. A joint Wald test then assesses whether these interactions differ from zero.
6

A first concern is that two instructions in the main prompt (i.e., asking the agent which hotel it would book
and instructing it to stop once it has sufficient information) may have shaped the AI agents’ behavior. The
former instruction could inflate the conversion rate, while the latter could imply that several hotels should
be examined, thereby increasing search relative to human consumers. We conducted this check with Flash
Lite, whose significant curvilinear position effect on both inspection and choice at its default reasoning effort
would make any artifact of the prompt most apparent.
We executed 500 sessions with a reduced prompt that states the trip parameters and the two available tools
but omits both instructions (Table 1, Alternative). Under this prompt, the conversion rate remains at 100%,
and search remains deeper than in the human benchmark (Table W7). Moreover, the curvilinear position
effect replicates for both inspection and choice, with a negative linear term and a positive quadratic term (all
ps < 0.001; Table W8).
A second concern is that, even in the absence of an explicit recommendation question, a tool named
submit_choicemay frame the termination of a session as the act of choosing, thereby discouraging the
outside option. Therefore, we tested theFinishcondition, in which we removed the booking instruction and
replacedsubmit_choicewith afinishtool whose hotel argument is optional, which allows the AI agent to end
the session without booking (Table 1, Finish). We conducted this test with Flash because its choices are
concentrated on a single hotel under theMaincondition. Thus, any shift toward the outside option would be
attributable to the framing of the booking tool.
Across 500 sessions, all sessions concluded with a booking (Table W7). The curvilinear effect of position on
inspection persisted, with a negative linear and a positive quadratic term (bothps < 0.001). Similar to the
Maincondition, choice showed no detectable dependence on position (χ2(2) = 2.71,p= 0.258; Table W8).
These results indicate that the absence of the outside option is not an artifact of the booking tool.
A third concern is that the concentration of Flash’s choices on a single listing may reflect familiarity with the
hotel’s brand, acquired during pretraining, rather than the hotel attributes displayed on the listing page. In
theNo namecondition, we therefore removed hotel names from the listing page while retaining every other
attribute and the main prompt.
The percentage of the modal hotel choice was 93.8%, compared with 100% under theMaincondition (Table
W7). As in the main condition, position reduced the probability of inspection but had no detectable effect on
choice (Table W8). This modest decline suggests that hotel names contribute partly to the choice but that
the convergence on a single listing is driven predominantly by its displayed attributes.
Open-weight models
To assess whether the findings extend beyond proprietary LLMs, we replicated theMaincondition with
four open-weight LLMs: Meta’s Muse Glimmer 30B, NVIDIA’s Nemotron 3.5 Lightning 30B A3B, Alibaba
Cloud’s Qwen3.8 27B, and Google’s Gemma 4 31B (500 sessions each; Table W9).
Search remains deeper than in the human benchmark, although the outside option is selected only by
Nemotron, in 2.2% of sessions. For inspection, the linear term on position is negative and significant for every
LLM (allps < 0.01), and the quadratic term is positive and significant for three of the four LLMs (Table
W10). At the choice stage, Muse Glimmer exhibits the curvilinear pattern observed for Flash Lite and Luna,
whereas neither position term is significant for Gemma and Nemotron. Qwen shows a small positive linear
term (p< 0.05).
Conclusion
By randomizing the order of the hotel listings presented to AI agents, this research studied the value of
rank for AI shopping agents. We found that, similar to humans, AI shopping agents can display a position
bias (RQ1 and RQ2), but the nature and ramifications of this bias are different. AI agents’ position bias is
concentrated in the middle rather than at the bottom of the page (Ursu, 2018; Liu et al., 2024). Moreover,
unlike human consideration sets, which typically hold a single alternative, AI agents inspected several listings.
7

As a result, position could shape the AI agents’ consideration sets without affecting their final choices,
particularly at higher levels of reasoning effort (RQ2).
For platforms and consumers, these findings suggest that position-neutral choice can be obtained more
economically by raising the reasoning effort of a less capable LLM than by deploying a more capable one. For
example, Pro, the most capable Google LLM tested, remained strongly position-dependent at low effort at a
cost of $0.037 per session, whereas Flash Lite at high effort showed no detectable dependence on position at
$0.011 per session. Similarly, Pro attained position-neutral choice only at high effort, at a cost of $0.28 per
session, approximately 25 times that of Flash Lite at high effort. However, the mitigating effect of reasoning
effort was not uniform across LLMs, as Luna remained position-dependent even at its highest effort level.
Therefore, platforms and consumers should verify the susceptibility to position effects of the specific LLM
and configuration they deploy.
These findings carry implications beyond position effects. AI agents concentrated their bookings on listings
with high review scores and low prices (Table W4), which mirrors human consumers (Chevalier and Mayzlin,
2006; Floyd et al., 2014) and is consistent with other studies of AI shopping agents (Allouah et al., 2026; Cherep
et al., 2026; Wadi and Ma, 2026b; Kireyev, 2026). Sellers may therefore benefit more from strengthening
these signals (e.g., by soliciting reviews; Godes and Mayzlin, 2009; Wadi et al., 2026c,a; Burtch et al., 2018)
than from improving their placement.
Our study has several limitations. We examined a single booking task with a fixed query and destination.
Categories that differ in the number or complexity of attributes may produce different position effects.
Moreover, we observe a pattern consistent with the lost-in-the-middle phenomenon but do not identify
retrieval as the mechanism, which would require access to the internal activations of the LLMs. Costs are
based on list prices, which change over time and do not reflect prompt caching, and the LLMs tested are
moving targets whose positional biases may change with future releases. Future research could examine
sponsored and personalized rankings, multi-page results, and the strategies sellers adopt when they optimize
listings for AI agents rather than for human consumers.
Data availability statement
The data and the code to reproduce the analysis are available at the following anonymous repository:
https://osf.io/vg8sn/overview?view_only=93557b5ec07745ceb19bf61e88f65ee1
References
Yi-Chun Akchen and Dmitry Mitrofanov. Consider or choose? the role and power of consideration sets.
Management Science, 72(7):6025–6042, 2026.
Amine Allouah, Omar Besbes, Josué D Figueroa, Yash Kanoria, and Akshit Kumar. What is your ai
agent buying? evaluation, biases, model dependence, & emerging implications of agentic e-commerce. In
Proceedings of the ACM Web Conference 2026, pages 8697–8700, 2026.
Mohammad Ali Alomrani, Yingxue Zhang, Derek Li, Qianyi Sun, Soumyasundar Pal, Zhanguang Zhang,
Yaochen Hu, Rohan Deepak Ajwani, Antonios Valkanas, Raika Karimi, et al. Reasoning on a budget: A
survey of adaptive and controllable test-time compute in llms.arXiv preprint arXiv:2507.02076, 2025.
Anthropic. Model deprecations: API parameter deprecations, 2026. URL https://platform.claude.com/docs
/en/about-claude/model-deprecations#api-parameter-deprecations.
Stefanos Balaskas. From recommendations to delegation: A systematic review mapping agentic ai in
e-commerce and its consumer effects.Inf., 17(3):222, 2026.
Oliver Brady, Paul Nulty, Lili Zhang, Tomás E Ward, and David P McGovern. Dual-process theory and
decision-making in large language models.Nature Reviews Psychology, 4(12):777–792, 2025.
8

Gordon Burtch, Yili Hong, Ravi Bapna, and Vladas Griskevicius. Stimulating online reviews by combining
financial incentives and social norms.Management Science, 64(5):2065–2082, 2018.
Manuel Cherep, Chengtian Ma, Abigail Xu, Maya Shaked, Pattie Maes, and Nikhil Singh. A framework for
studying ai agent behavior: Evidence from consumer choice experiments. InInternational Conference on
Learning Representations, volume 2026, pages 63296–63326, 2026.
Judith A Chevalier and Dina Mayzlin. The effect of word of mouth on sales: Online book reviews.Journal
of marketing research, 43(3):345–354, 2006.
Robert Donnelly, Ayush Kanodia, and Ilya Morozov. Welfare effects of personalized rankings.Marketing
Science, 43(1):92–113, 2024.
Kristopher Floyd, Ryan Freling, Saad Alhoqail, Hyun Young Cho, and Traci Freling. How online product
reviews affect retail sales: A meta-analysis.Journal of retailing, 90(2):217–232, 2014.
David Godes and Dina Mayzlin. Firm-created word-of-mouth communication: Evidence from a field test.
Marketing science, 28(4):721–739, 2009.
Google. Gemini models: Sampling parameter deprecation, 2026. URL https://ai.google.dev/gemini-
api/docs/latest-model#sampling-parameter-deprecation.
Rafael P Greminger. Trade-offs between ranking objectives: Descriptive evidence and structural estimation.
Management Science, 2026.
Marc Hasselwander, Varsolo Sunio, Oliver Lah, and Emmanuel Mogaji. Toward agentic ai: User acceptance
of a deeply personalized ai super assistant (aisa).Journal of Retailing and Consumer Services, 89:104620,
2026.
John R Hauser. Consideration-set heuristics.Journal of Business Research, 67(8):1688–1699, 2014.
Amey Hengle, Prasoon Bajpai, Soham Dan, and Tanmoy Chakraborty. Can llms reason over extended
multilingual contexts? towards long-context evaluation beyond retrieval over haystacks. InProceedings of
the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1:
Long Papers), pages 6128–6152, 2026.
Elisabeth Honka, Stephan Seiler, and Raluca Ursu. Consumer search: What can we learn from pre-purchase
data?Journal of Retailing, 100(1):114–129, 2024.
Thorsten Joachims, Laura Granka, Bing Pan, Helene Hembrooke, Filip Radlinski, and Geri Gay. Evaluating
the accuracy of implicit feedback from clicks and query reformulations in web search.ACM Transactions
on Information Systems (TOIS), 25(2):7–es, 2007.
Pavel Kireyev. Pricebench: A diagnostic benchmark for price, quality, and brand preferences in llm booking
agents. InForthcoming, Proceedings of the 2026 Conference on Empirical Methods in Natural Language
Processing: Industry Track (EMNLP 2026), 2026.
V Kumar, Philip Kotler, and Ajay Kumar. Transformative marketing strategies in the era of new-age
technologies: Principles, plan, purpose, and practice.Journal of the Academy of Marketing Science, 54(1):
1–27, 2026.
Woo-Chul Lee, Jang-Suk Lee, and Jungho Suh. Semantic divergence in ai-generated and human influencer
product recommendations: A computational analysis of dual-agent communication in social commerce.
Applied Sciences, 16(6):2816, 2026.
Nelson F Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy
Liang. Lost in the middle: How language models use long contexts.Transactions of the association for
computational linguistics, 12:157–173, 2024.
Olivia Macmillan-Scott and Mirco Musolesi. (ir) rationality and cognitive biases in large language models.
Royal Society open science, 11(6), 2024.
9

Emmanuel Mogaji and Varsha Jain. How generative ai is (will) change consumer behaviour: Postulating the
potential impact and implications for research, practice, and policy.Journal of consumer behaviour, 23(5):
2379–2389, 2024.
Sridhar Narayanan and Kirthi Kalyanam. Position effects in search advertising and their moderators: A
regression discontinuity approach.Marketing Science, 34(3):388–407, 2015.
Vivek Pandya. Generative AI-powered shopping rises with traffic to U.S. retail sites up 4,700%. URL
https://business.adobe.com/blog/generative-ai-powered-shopping-rises-with-traffic-to-retail-sites.
Girish Punj and Robert Moore. Information search and consideration set formation in a web-based store
environment.Journal of Business Research, 62(6):644–650, 2009.
Jianlin Su, Murtadha Ahmed, Yu Lu, Shengfeng Pan, Wen Bo, and Yunfeng Liu. Roformer: Enhanced
transformer with rotary position embedding.Neurocomputing, 568:127063, 2024.
Raluca M Ursu. The power of rankings: Quantifying the effect of rankings on online consumer search and
purchase decisions.Marketing Science, 37(4):530–552, 2018.
Raluca M Ursu, Qianyun Zhang, and Elisabeth Honka. Search gaps and consumer fatigue.Marketing Science,
42(1):110–136, 2023.
Davood Wadi and Marc Fredette. A monte-carlo sampling framework for reliable evaluation of large language
models using behavioral analysis.Findings of the Association for Computational Linguistics: EMNLP
2025, pages 9414–9432, 2025.
Davood Wadi and Yu Ma. Shopping by algorithm: How agentic ai deploys human heuristics as a surrogate
consumer. 2026a.
Davood Wadi and Yu Ma. Whom do ai agents work for? role assignment induces sponsorship bias in llm
recommenders.arXiv preprint arXiv:2609.17989, 2026b.
Davood Wadi, Marc Fredette, Sylvain Senecal, and Renaud Legoux. Be careful what you pay for: the effect of
performance contingent incentives on online product reviews.Journal of Research in Interactive Marketing,
pages 1–25, 2026a.
Davood Wadi, Mohsen Ghodrat, and Matthew Philp. Every token counts: Exact likert-scale distributions for
measuring llm attitudes and biases.arXiv preprint arXiv:2608.10503, 2026b.
Davood Wadi, Renaud Legoux, Marc Fredette, and Sylvain Sénécal. The interplay of altruism and financial
incentives: Maximizing online reviews through effective messaging.Journal of Electronic Commerce
Research, 27(2), 2026c.
Fengli Xu, Qianyue Hao, Chenyang Shao, Zefang Zong, Yu Li, Jingwei Wang, Yunke Zhang, Jingyi Wang,
Xiaochong Lan, Jiahui Gong, et al. Toward large reasoning models: A survey of reinforced reasoning with
large language models.Patterns, 6(10), 2025.
10

Web Appendix A - Supplementary tables
Table W1. Comparison of search environment hotel attributes between current study and human benchmark
Hotel listing attribute Current study Human benchmark
Price per night ($) $230.64 (96.86) $159.71 (102.43)
Review score (1–5) 4.32 (0.29) 3.89 (0.86)
Chain proxy 55.0% 66.0%
Promotion proxy 19.0% 25.0%
Note.Values represent sample means with standard deviations in parentheses where applicable. Human
benchmark data adapted from Ursu (2018), Table 1.
11

Table W2. Descriptive statistics by reasoning effort
LLM Effort Inspections per session One inspection Chose first inspected Chosen position Modal choice Mean Median Mode SD% %M%
Flash Lite Minimal † 3.12 3.00 3.00 0.54 0.8% 62.0% 43.97 61.4%
Low 2.28 2.00 2.00 1.05 24.0% 61.4% 44.02 78.8%
Medium 2.26 2.00 2.00 1.10 27.0% 85.4% 46.32 83.8%
High 1.91 2.00 2.00 0.66 22.8% 96.6% 51.20 96.6%
Flash Low 1.45 1.00 1.00 0.71 65.8% 99.8% 50.44 100.0%
Medium† 4.25 4.00 4.00 1.59 2.6% 99.8% 49.46 100.0%
Pro Low 0.39 0.00 0.00 0.55 35.8% 36.0% 40.96 48.0%
Medium 1.13 1.00 1.00 1.28 53.6% 62.0% 45.63 51.8%
High† 5.83 5.00 1.00 4.78 20.8% 60.4% 49.72 55.4%
Sonnet Low 0.85 1.00 1.00 0.48 75.6% 76.6% 22.63 30.6%
High† 1.63 2.00 2.00 0.49 37.4% 98.2% 47.58 95.8%
Luna None 3.43 3.00 3.00 1.01 5.2% 28.8% 35.56 27.6%
Medium† 4.00 4.00 4.00 1.13 0.2% 15.6% 33.45 41.0%
xHigh 6.22 6.00 6.00 1.89 0.0% 13.0% 36.99 47.4%
Note.Every condition has 500 sessions, a 100.0% conversion rate, and 0.0% outside option selection.† Provider default reasoning effort. One inspection
= share of sessions with a single inspection; Chose first inspected = share of sessions booking the first hotel inspected; Modal choice = share of sessions
booking the most frequently chosen hotel.
Table W3. Linear probability models of inspection by LLM and reasoning effort, with the human benchmark
LLM Effort Position Price Review score Chain Promotion Adj.R 2 N
Flash Lite Minimal † -0.0005***
(<0.0001)
-0.0001***
(<0.0001)
0.1466***
(0.0014)
-0.0645***
(0.0013)
-0.0042**
(0.0014)
0.0891 50,000
Low -0.0004***
(<0.0001)
-0.0001***
(<0.0001)
0.1025***
(0.0021)
-0.0391***
(0.0013)
0.0146***
(0.0014)
0.0621 50,000
Medium -0.0001***
(<0.0001)
-0.0001***
(<0.0001)
0.1026***
(0.0023)
-0.0387***
(0.0014)
0.0162***
(0.0013)
0.0591 50,000
High >-0.0001
(<0.0001)
-0.0001***
(<0.0001)
0.0854***
(0.0013)
-0.0322***
(0.0010)
0.0211***
(0.0008)
0.0523 50,000
Flash Low -0.0001***
(<0.0001)
>-0.0001***
(<0.0001)
0.0654***
(0.0015)
-0.0225***
(0.0009)
0.0351***
(0.0008)
0.0547 50,000
Medium† -0.0004***
(<0.0001)
-0.0001***
(<0.0001)
0.1967***
(0.0033)
-0.0839***
(0.0020)
-0.0186***
(0.0018)
0.1077 50,000
Pro Low >-0.0001***
(<0.0001)
>-0.0001***
(<0.0001)
0.0123***
(0.0009)
-0.0054***
(0.0006)
0.0053***
(0.0010)
0.0075 50,000
Medium >-0.0001*
(<0.0001)
-0.0001***
(<0.0001)
0.0301***
(0.0016)
-0.0152***
(0.0010)
0.0095***
(0.0015)
0.0154 50,000
High† -0.0003***
(<0.0001)
-0.0003***
(<0.0001)
0.1282***
(0.0058)
-0.0387***
(0.0023)
-0.0067**
(0.0025)
0.0344 50,000
12

LLM Effort Position Price Review score Chain Promotion Adj.R 2 N
Sonnet Low -0.0003***
(<0.0001)
>-0.0001***
(<0.0001)
0.0369***
(0.0011)
-0.0146***
(0.0008)
-0.0006 (0.0014) 0.0254 50,000
High† -0.0002***
(<0.0001)
>-0.0001***
(<0.0001)
0.0757***
(0.0012)
-0.0304***
(0.0008)
0.0265***
(0.0009)
0.0573 50,000
Luna None -0.0005***
(<0.0001)
-0.0001***
(<0.0001)
0.1079***
(0.0016)
-0.0035* (0.0014) 0.0220***
(0.0013)
0.0399 50,000
Medium† -0.0006***
(<0.0001)
-0.0001***
(<0.0001)
0.1328***
(0.0020)
-0.0061***
(0.0015)
0.0111***
(0.0014)
0.0456 50,000
xHigh -0.0008***
(<0.0001)
-0.0002***
(<0.0001)
0.2037***
(0.0030)
-0.0041* (0.0019) -0.0100***
(0.0018)
0.0659 50,000
Human -0.0019***
(<0.0001)
-0.0001***
(<0.0001)
0.0012***
(0.0002)
0.0022***
(0.0005)
0.0116***
(0.0005)
0.0150 1,220,917
Note.Coefficients are from linear probability models. Standard errors clustered at the session level in parentheses.† Provider default reasoning effort.
Human benchmark from Ursu (2018), Table 2. Price is reported in $1 units to match the human benchmark. Controls comprise hotel attributes
displayed on the listing page; star rating and location score, which the human benchmark’s results page displayed, are not shown on Expedia’s current
results page. Query characteristics and destination fixed effects are omitted because our design holds the query and destination fixed.
*p<0.05, **p<0.01, ***p<0.001
Table W4. Linear probability models of choice by LLM and reasoning effort, with the human benchmark
LLM Effort Position Price Review score Chain Promotion Adj.R 2 N
Flash Lite Minimal † -0.0001***
(<0.0001)
>-0.0001***
(<0.0001)
0.0470***
(0.0003)
-0.0184***
(0.0005)
0.0169***
(0.0016)
0.0351 50,000
Low -0.0001***
(<0.0001)
>-0.0001***
(<0.0001)
0.0449***
(0.0002)
-0.0146***
(0.0004)
0.0300***
(0.0013)
0.0431 50,000
Medium >-0.0001**
(<0.0001)
>-0.0001***
(<0.0001)
0.0448***
(0.0002)
-0.0146***
(0.0004)
0.0331***
(0.0012)
0.0467 50,000
High <0.0001
(<0.0001)
>-0.0001***
(<0.0001)
0.0442***
(0.0001)
-0.0128***
(0.0002)
0.0421***
(0.0006)
0.0570 50,000
Flash Low >-0.0001
(<0.0001)
>-0.0001***
(<0.0001)
0.0439***
(<0.0001)
-0.0124***
(<0.0001)
0.0445***
(<0.0001)
0.0602 50,000
Medium† >-0.0001
(<0.0001)
>-0.0001***
(<0.0001)
0.0439***
(<0.0001)
-0.0124***
(<0.0001)
0.0445***
(<0.0001)
0.0602 50,000
Pro Low -0.0001***
(<0.0001)
>-0.0001***
(<0.0001)
0.0322***
(0.0010)
-0.0124***
(0.0009)
0.0177***
(0.0016)
0.0217 50,000
Medium -0.0001***
(<0.0001)
>-0.0001***
(<0.0001)
0.0324***
(0.0009)
-0.0139***
(0.0009)
0.0175***
(0.0017)
0.0224 50,000
High† >-0.0001
(<0.0001)
>-0.0001***
(<0.0001)
0.0264***
(0.0012)
-0.0031**
(0.0010)
0.0311***
(0.0015)
0.0242 50,000
Sonnet Low -0.0003***
(<0.0001)
>-0.0001***
(<0.0001)
0.0422***
(0.0006)
-0.0151***
(0.0008)
0.0025 (0.0015) 0.0289 50,000
13

LLM Effort Position Price Review score Chain Promotion Adj.R 2 N
High† >-0.0001*
(<0.0001)
>-0.0001***
(<0.0001)
0.0439***
(0.0001)
-0.0128***
(0.0002)
0.0420***
(0.0006)
0.0567 50,000
Luna None -0.0002***
(<0.0001)
>-0.0001***
(<0.0001)
0.0319***
(0.0008)
0.0008 (0.0009) 0.0066***
(0.0013)
0.0121 50,000
Medium† -0.0002***
(<0.0001)
>-0.0001***
(<0.0001)
0.0274***
(0.0006)
0.0071***
(0.0008)
-0.0060***
(0.0008)
0.0121 50,000
xHigh -0.0002***
(<0.0001)
>-0.0001***
(<0.0001)
0.0261***
(0.0004)
0.0093***
(0.0006)
-0.0023**
(0.0008)
0.0106 50,000
Human -0.0001***
(<0.0001)
>-0.0001***
(<0.0001)
0.0002***
(<0.0001)
0.0003* (0.0001) 0.0012***
(0.0001)
0.0030 1,220,917
Note.Coefficients are from linear probability models. Standard errors clustered at the session level in parentheses.† Provider default reasoning effort.
Human benchmark from Ursu (2018), Table 2. Price is reported in $1 units to match the human benchmark. Controls comprise hotel attributes
displayed on the listing page; star rating and location score, which the human benchmark’s results page displayed, are not shown on Expedia’s current
results page. Query characteristics and destination fixed effects are omitted because our design holds the query and destination fixed.
*p<0.05, **p<0.01, ***p<0.001
Table W5. Linear probability models of inspection with quadratic position and manipulated reasoning efforts
LLM Effort Position Position 2 Price Review score Chain Promotion Adj.R 2
Flash Lite Minimal † -0.1460***
(0.0115)
0.0982***
(0.0104)
-0.0001***
(<0.0001)
0.1467***
(0.0014)
-0.0646***
(0.0013)
-0.0042**
(0.0014)
0.0908
Low -0.1474***
(0.0103)
0.1090***
(0.0091)
-0.0001***
(<0.0001)
0.1026***
(0.0021)
-0.0392***
(0.0013)
0.0148***
(0.0014)
0.0650
Medium -0.0520***
(0.0090)
0.0366***
(0.0083)
-0.0001***
(<0.0001)
0.1026***
(0.0023)
-0.0388***
(0.0014)
0.0163***
(0.0013)
0.0594
High -0.0083 (0.0082) 0.0079 (0.0079) -0.0001***
(<0.0001)
0.0854***
(0.0013)
-0.0322***
(0.0010)
0.0211***
(0.0008)
0.0523
Flash Low -0.0255***
(0.0074)
0.0163*
(0.0069)
>-0.0001***
(<0.0001)
0.0654***
(0.0015)
-0.0225***
(0.0009)
0.0351***
(0.0008)
0.0548
Medium† -0.1356***
(0.0123)
0.0993***
(0.0114)
-0.0001***
(<0.0001)
0.1965***
(0.0033)
-0.0839***
(0.0020)
-0.0184***
(0.0018)
0.1090
Pro Low -0.0211***
(0.0048)
0.0170***
(0.0044)
>-0.0001***
(<0.0001)
0.0123***
(0.0009)
-0.0054***
(0.0006)
0.0053***
(0.0010)
0.0079
Medium -0.0173* (0.0069) 0.0134*
(0.0064)
-0.0001***
(<0.0001)
0.0301***
(0.0016)
-0.0152***
(0.0010)
0.0095***
(0.0015)
0.0155
High† -0.0567***
(0.0154)
0.0276 (0.0141) -0.0003***
(<0.0001)
0.1282***
(0.0058)
-0.0387***
(0.0023)
-0.0068**
(0.0025)
0.0345
Sonnet Low -0.1292***
(0.0073)
0.0997***
(0.0064)
>-0.0001***
(<0.0001)
0.0369***
(0.0011)
-0.0146***
(0.0008)
-0.0006 (0.0014) 0.0319
High† -0.0643***
(0.0091)
0.0454***
(0.0081)
>-0.0001***
(<0.0001)
0.0757***
(0.0012)
-0.0304***
(0.0008)
0.0265***
(0.0009)
0.0580
14

LLM Effort Position Position 2 Price Review score Chain Promotion Adj.R 2
Luna None -0.1680***
(0.0143)
0.1123***
(0.0125)
-0.0001***
(<0.0001)
0.1077***
(0.0016)
-0.0035* (0.0014) 0.0219***
(0.0013)
0.0419
Medium† -0.1867***
(0.0140)
0.1272***
(0.0123)
-0.0001***
(<0.0001)
0.1326***
(0.0020)
-0.0060***
(0.0015)
0.0113***
(0.0014)
0.0479
xHigh -0.2137***
(0.0172)
0.1318***
(0.0154)
-0.0002***
(<0.0001)
0.2036***
(0.0030)
-0.0042* (0.0019) -0.0099***
(0.0018)
0.0675
Note.Each model is estimated on 50,000 hotel impressions.† Provider default reasoning effort. Position is scaled to [0, 1] (rank / 100). Standard
errors clustered at the session level in parentheses.
Table W6. Linear probability models of choice with quadratic position and manipulated reasoning efforts
LLM Effort Position Position 2 Price Review score Chain Promotion Adj.R 2
Flash Lite Minimal † -0.0503***
(0.0067)
0.0418***
(0.0062)
>-0.0001***
(<0.0001)
0.0470***
(0.0003)
-0.0185***
(0.0005)
0.0169***
(0.0016)
0.0360
Low -0.0276***
(0.0066)
0.0197**
(0.0060)
>-0.0001***
(<0.0001)
0.0449***
(0.0002)
-0.0146***
(0.0004)
0.0300***
(0.0013)
0.0433
Medium -0.0095 (0.0064) 0.0052 (0.0060) >-0.0001***
(<0.0001)
0.0448***
(0.0002)
-0.0146***
(0.0004)
0.0331***
(0.0012)
0.0466
High 0.0023 (0.0060) -0.0010 (0.0059) >-0.0001***
(<0.0001)
0.0442***
(0.0001)
-0.0128***
(0.0002)
0.0421***
(0.0006)
0.0570
Flash Low 0.0034 (0.0058) -0.0038 (0.0056) >-0.0001***
(<0.0001)
0.0439***
(<0.0001)
-0.0124***
(<0.0001)
0.0445***
(<0.0001)
0.0602
Medium† 0.0037 (0.0061) -0.0051 (0.0059) >-0.0001***
(<0.0001)
0.0439***
(<0.0001)
-0.0124***
(<0.0001)
0.0445***
(<0.0001)
0.0602
Pro Low -0.0760***
(0.0075)
0.0638***
(0.0068)
>-0.0001***
(<0.0001)
0.0322***
(0.0010)
-0.0123***
(0.0009)
0.0177***
(0.0016)
0.0240
Medium -0.0237***
(0.0068)
0.0179**
(0.0063)
>-0.0001***
(<0.0001)
0.0324***
(0.0009)
-0.0139***
(0.0009)
0.0176***
(0.0017)
0.0225
High† -0.0080 (0.0065) 0.0071 (0.0063) >-0.0001***
(<0.0001)
0.0264***
(0.0012)
-0.0031**
(0.0010)
0.0311***
(0.0015)
0.0242
Sonnet Low -0.1565***
(0.0076)
0.1217***
(0.0067)
>-0.0001***
(<0.0001)
0.0422***
(0.0006)
-0.0150***
(0.0008)
0.0025 (0.0015) 0.0372
High† -0.0051 (0.0065) 0.0016 (0.0061) >-0.0001***
(<0.0001)
0.0439***
(0.0001)
-0.0128***
(0.0002)
0.0420***
(0.0006)
0.0567
Luna None -0.0729***
(0.0072)
0.0544***
(0.0064)
>-0.0001***
(<0.0001)
0.0318***
(0.0008)
0.0007 (0.0009) 0.0066***
(0.0013)
0.0137
Medium† -0.0652***
(0.0074)
0.0441***
(0.0065)
>-0.0001***
(<0.0001)
0.0273***
(0.0006)
0.0072***
(0.0008)
-0.0059***
(0.0008)
0.0132
xHigh -0.0364***
(0.0075)
0.0202**
(0.0066)
>-0.0001***
(<0.0001)
0.0261***
(0.0004)
0.0093***
(0.0006)
-0.0023**
(0.0008)
0.0108
Note.Each model is estimated on 50,000 hotel impressions.† Provider default reasoning effort. Position is scaled to [0, 1] (rank / 100). Standard
15

errors clustered at the session level in parentheses.
Table W7. Search and choice behavior under the robustness conditions
Flash Lite Flash
Main Alternative Main No name Finish
N500 500 500 500 500
Conversion rate 100.0% 100.0% 100.0% 100.0% 100.0%
Outside option selected 0.0% 0.0% 0.0% 0.0% 0.0%
Inspections per session
(Mean) 3.12 2.92 4.25 4.73 3.63
(Median) 3.00 3.00 4.00 4.50 3.00
(Mode) 3.00 3.00 4.00 4.00 3.00
(SD) 0.54 0.72 1.59 1.58 1.47
Sessions with one inspection 0.8% 6.2% 2.6% 0.0% 5.6%
Chose the first inspected hotel 62.0% 65.6% 99.8% 93.8% 99.8%
Position of the chosen hotel (M) 43.97 42.58 49.46 49.56 53.12
Modal choice proportion 61.4% 60.8% 100.0% 93.8% 100.0%
Note.Main = main prompt; Alternative = prompt without the stopping rule and the recommendation question; No name = hotel names removed from
the listing page; Finish = neutralfinishtool with an optional hotel and no booking instruction. Flash Lite uses minimal and Flash medium reasoning
effort, the provider defaults.
Table W8. Linear probability models of inspection and choice under the robustness conditions
Flash Lite Flash
Main Alternative Main No name Finish
Panel A: Inspected
Position -0.1460*** (0.0115) -0.1514*** (0.0108) -0.1356*** (0.0123) -0.0816*** (0.0139) -0.1308*** (0.0125)
Position2 0.0982*** (0.0104) 0.1086*** (0.0097) 0.0993*** (0.0114) 0.0582*** (0.0128) 0.1022*** (0.0112)
Price -0.0001*** (<0.0001) -0.0001*** (<0.0001) -0.0001*** (<0.0001) -0.0001*** (<0.0001) -0.0001*** (<0.0001)
Review score 0.1467*** (0.0014) 0.1379*** (0.0017) 0.1965*** (0.0033) 0.2218*** (0.0031) 0.1665*** (0.0030)
Chain -0.0646*** (0.0013) -0.0602*** (0.0013) -0.0839*** (0.0020) -0.1085*** (0.0018) -0.0679*** (0.0018)
Promotion -0.0042** (0.0014) -0.0016 (0.0013) -0.0184*** (0.0018) -0.0500*** (0.0017) -0.0085*** (0.0017)
Adj.R 2 0.0908 0.0860 0.1090 0.1301 0.0897
N 50,000 50,000 50,000 50,000 50,000
Panel B: Chosen
Position -0.0503*** (0.0067) -0.0626*** (0.0070) 0.0037 (0.0061) 0.0098 (0.0062) -0.0002 (0.0059)
Position2 0.0418*** (0.0062) 0.0524*** (0.0064) -0.0051 (0.0059) -0.0108 (0.0058) 0.0025 (0.0056)
Price >-0.0001*** (<0.0001) >-0.0001*** (<0.0001) >-0.0001*** (<0.0001) >-0.0001*** (<0.0001) >-0.0001*** (<0.0001)
Review score 0.0470*** (0.0003) 0.0467*** (0.0003) 0.0439*** (<0.0001) 0.0446*** (0.0001) 0.0439*** (<0.0001)
Chain -0.0185*** (0.0005) -0.0179*** (0.0005) -0.0124*** (<0.0001) -0.0137*** (0.0002) -0.0124*** (<0.0001)
Promotion 0.0169*** (0.0016) 0.0168*** (0.0016) 0.0445*** (<0.0001) 0.0399*** (0.0008) 0.0445*** (<0.0001)
Adj.R 2 0.0360 0.0360 0.0602 0.0550 0.0602
16

Flash Lite Flash
Main Alternative Main No name Finish
N 50,000 50,000 50,000 50,000 50,000
Note.Position is scaled to [0, 1] (rank / 100). Standard errors clustered at the session level in parentheses. Chain is derived from the hotel name, which
is not displayed in the No name condition. Flash Lite uses minimal and Flash medium reasoning effort, the provider defaults. *p<0.05, **p<0.01,
***p<0.001
Table W9. Descriptive statistics for open-weight LLMs tested on the same setup as the main experiment
Qwen3.8 27B Muse Glimmer 30B Nemotron 3.5 Lightning 30B A3B Gemma 4 31B
N 500 500 500 500
Conversion rate 100.0% 100.0% 97.8% 100.0%
Outside option selected 0.0% 0.0% 2.2% 0.0%
Inspections per session
(Mean)4.19 9.62 1.76 3.99
(Median)4.00 10.00 1.00 4.00
(Mode)4.00 9.00 1.00 4.00
(SD)1.32 2.27 1.56 1.39
Sessions with one inspection 0.0% 0.0% 27.4% 0.2%
Chose the first inspected hotel 87.8% 62.6% 62.4% 76.6%
Position (rank) of the chosen hotel (M) 51.83 39.89 47.56 52.09
Modal choice proportion 88.2% 62.4% 67.3% 76.6%
Table W10. Linear probability models of inspection and choice with quadratic position for open-weight LLMs
LLM Position Position 2 Price Review score Chain Promotion Adj.R 2
Panel A: Inspected
Gemma 4 31B -0.0725***
(0.0120)
0.0562***
(0.0113)
-0.0001***
(<0.0001)
0.1638***
(0.0021)
-0.0485***
(0.0012)
-0.0152***
(0.0011)
0.0654
Muse Glimmer 30B -0.4536***
(0.0200)
0.2781***
(0.0178)
-0.0004***
(<0.0001)
0.2302***
(0.0031)
-0.0313***
(0.0022)
-0.0242***
(0.0025)
0.0886
Nemotron 3.5 Lightning 30B A3B -0.0436***
(0.0107)
0.0295**
(0.0093)
-0.0001***
(<0.0001)
0.0531***
(0.0022)
-0.0180***
(0.0013)
0.0127***
(0.0015)
0.0224
Qwen3.8 27B -0.0356**
(0.0126)
0.0136 (0.0116) -0.0001***
(<0.0001)
0.1689***
(0.0022)
-0.0391***
(0.0016)
-0.0130***
(0.0013)
0.0619
Panel B: Chosen
Gemma 4 31B -0.0048 (0.0062) 0.0067 (0.0060) >-0.0001***
(<0.0001)
0.0450***
(0.0003)
-0.0149***
(0.0005)
0.0281***
(0.0013)
0.0409
Muse Glimmer 30B -0.0345***
(0.0069)
0.0216***
(0.0062)
>-0.0001***
(<0.0001)
0.0377***
(0.0009)
-0.0116***
(0.0008)
0.0262***
(0.0015)
0.0323
17

LLM Position Position 2 Price Review score Chain Promotion Adj.R 2
Nemotron 3.5 Lightning 30B A3B -0.0062 (0.0066) 0.0030 (0.0061) >-0.0001***
(<0.0001)
0.0362***
(0.0007)
-0.0119***
(0.0007)
0.0258***
(0.0014)
0.0304
Qwen3.8 27B 0.0124* (0.0060) -0.0108
(0.0057)
>-0.0001***
(<0.0001)
0.0449***
(0.0002)
-0.0145***
(0.0003)
0.0359***
(0.0011)
0.0503
Note.Each model is estimated on 50,000 hotel impressions. Position is scaled to [0, 1] (rank / 100). Standard errors clustered at the session level in
parentheses.
*p<0.05, **p<0.01, ***p<0.001
18

Table W11. Position dependence of choice, token usage, and cost per session by LLM and reasoning effort
LLM Effort Positionχ 2(2) Tokens per session Cost per session ($)Input Output
Flash Lite Minimal † 60.36*** 52,282 80 0.0132
Low 29.90*** 42,536 479 0.0114
Medium 8.66* 43,649 1,041 0.0125
High 0.68 38,940 1,065 0.0113
Flash Low 0.49 30,403 339 0.0481
Medium† 1.68 75,163 874 0.1193
Pro Low 107.21*** 16,752 293 0.0370
Medium 17.12*** 27,557 590 0.0622
High† 1.56 125,960 2,552 0.2825
Sonnet Low 609.27*** 29,992 233 0.0623
High† 5.56 43,860 787 0.0956
Luna None 145.58*** 50,277 91 0.0051
Medium† 187.49*** 57,665 571 0.0061
xHigh 120.06*** 91,640 1,592 0.0100
Note.Position χ2(2) is the Wald statistic for the joint hypothesis that the coefficients on position and
position2 in the model of choice are zero (Table W6); a non-significant statistic indicates no detectable
dependence of choice on position. Token counts and costs are means over 500 sessions per condition. Output
tokens include reasoning tokens, which providers bill at the output rate. Cost is computed from token counts
at each provider’s list price per million tokens.† Provider default reasoning effort.
*p<0.05, **p<0.01, ***p<0.001
Web Appendix B - Supplementary figures
Figure W1. Distribution of inspections per session by model
Note.Vertical line denotes the human benchmark mean (1.12 clicks per impression; Ursu, 2018).
19

Web Appendix C - Construction of the simulated search environ-
ment
To provide an empirical test of LLM decision making against human benchmark data, we constructed a
simulated hotel choice environment calibrated to the randomized ranking experiment in Ursu (2018). This
section details the empirical calibration of the search parameters, choice set extraction, attribute partitioning,
and econometric specifications used to replicate the reduced-form benchmarks.
Search query.We calibrated the simulated search parameters to match the median search impression
characteristics reported in the human benchmark data (Ursu, 2018, Table 1). In the original Expedia dataset,
the median search impression involved a two-day trip length, an 18-day advance booking window, a Saturday
night stay, two adults, zero children, and one room. To operationalize these parameters with contemporary
search data, the query was executed on Expedia, on May 13, 2026, specifying a check-in date of Saturday,
May 30, 2026, and a check-out date of Monday, June 1, 2026, for two adult guests sharing a single room.
Destination.In the human benchmark study, the primary Expedia dataset anonymized destination cities
while restricting structural estimation to the four largest destination markets in the United States, which
accounted for approximately 80% of domestic queries. To validate sequential search behavior and click-order
dynamics, Ursu (2018) utilized a companion dataset from the Wharton Customer Analytics Initiative that
tracked hotel searches in Manhattan, New York. Following this empirical precedent, we restricted our search
query to the Manhattan market to ensure comparability with the human benchmark.
Listing page.Following the observational boundary established in the human benchmark (Ursu, 2018,
Section 3.2.1), data collection was restricted to the first search engine results page prior to any user pagination.
The live query yielded a choice set of 100 hotel listings. For each hotel, all information visible on the
initial results page was extracted and structured into the pre-click choice set, alongside the hidden post-click
attributes retrieved through theinspecttool.
Information architecture.In the human benchmark, consumers evaluated hotels in two stages, first
observing a listing page and then clicking through to a hotel page with detailed information (Ursu, 2018). To
preserve this structure, hotel information was partitioned into pre-click listing-page attributes and post-click
detailed attributes. The pre-click layer, loaded into the context window of the agent as a single block of text,
contained the hotel name, neighborhood, aggregate guest review rating, total review count, nightly price, total
stay price, original price, promotional discount badge presence, rooms-left scarcity alerts, and promotional
status badges (e.g., VIP or sponsored status). The post-click layer, which corresponds to the hotel page
that a human consumer reaches by clicking, was accessible through theinspecttool and contained detailed
property attributes, including the star rating, sub-ratings for cleanliness, service, amenities, and location,
detailed room configurations, and cancellation policies. Ending a session without a booking corresponds to a
human consumer leaving the results page without booking and therefore represents the outside option.
Econometric specification.To make the LLM regression models comparable to the human ones, we
estimated linear probability models corresponding to the reduced-form specifications in Ursu (2018), Table 2.
The regression models included five primary pre-click covariates: listing position (indexed 1 to 100), nightly
price in dollars, guest review score (normalized from a 10-point to a 5-point scale), a chain proxy, and a
promotion proxy. The chain proxy was coded as a binary indicator for major national or international hotel
brands identified through keyword matching against property titles (e.g., Marriott, Hilton, Hyatt, Sheraton,
Holiday Inn, Westin, DoubleTree, Courtyard, Fairfield, Kimpton, Wyndham, Sofitel, Aloft, Embassy Suites,
and InterContinental). The promotion proxy was coded as a binary indicator for the presence of a promotional
discount badge on the listing page. To capture non-monotonic position effects, we additionally estimated
specifications that include the square of position, with position rescaled to the unit interval.
Omitted variables.The empirical replication remains an approximation of the original field data due
to structural evolutions in the Expedia interface. Two control variables from the human benchmark were
omitted from the pre-click specification: the proprietary 0 to 7 location score and the listing-page star rating.
These variables were not displayed on the modern Expedia listing page prior to inspection and were therefore
excluded from the pre-click control set to ensure that the empirical model controls strictly for information
observable to the agent before an inspection decision is made. Furthermore, post-click cues (e.g., specific
20

room amenities and detailed sub-ratings) were excluded from the pre-click linear probability models because
they are revealed only after inspection tool invocation.
Web Appendix D - Large language model specifications and runtime
configurations
This section details the model endpoints, default reasoning effort tiers, sampling parameters, and tool
invocation protocols across all experimental conditions. LLM interactions were managed through the official
Google GenAI Python SDK, Anthropic Python SDK, and OpenAI Python SDK, and the open-weight LLMs
were served locally through llama.cpp.
Model endpoints and versions.Google LLMs were initialized using their official API identifiers: gemini-
3.1-flash-lite, gemini-3.7-flash, and gemini-3.1-pro-preview. The Anthropic model was deployed using the
claude-sonnet-5 endpoint with a maximum output limit of 10,000 tokens to accommodate extended internal
reasoning and tool execution outputs. The OpenAI model was deployed using the gpt-6-luna endpoint through
the Responses API, with the provider-default output limit.
Open-weight models.The four open-weight LLMs were run locally from Unsloth Dynamic GGUF
quantizations: Gemma-4-31B-it (Q4_K_XL), Muse-Glimmer-30B (Q6_K_XL), NVIDIA-Nemotron-3.5-
Lightning-30B-A3B (Q4_K_XL), and Qwen3.8-27B (Q6_K_XL). Each LLM was served by llama-server
with all layers offloaded to the GPU and a single inference slot, so that sessions were processed one at a
time, and was queried through the OpenAI-compatible Responses API of the server. No reasoning effort
was specified for these LLMs, which therefore operated under the default reasoning behavior of their chat
templates.
Default reasoning effort.In the baseline out-of-the-box condition, LLMs were evaluated under their
provider-default reasoning effort settings. Gemini 3.1 Flash Lite defaults to minimal; Gemini 3.7 Flash
defaults to medium; and Gemini 3.1 Pro defaults to high reasoning effort. For Anthropic, Claude Sonnet
5 was deployed using adaptive thinking with high effort. For OpenAI, GPT 6 Luna defaults to medium
reasoning effort.
Reasoning effort manipulations.In the reasoning effort experiment, for Gemini 3.1 Flash Lite, we
evaluated all four available effort tiers: minimal, low, medium, and high. For Gemini 3.7 Flash, we evaluated
low and medium effort. For Gemini 3.1 Pro, we evaluated all three available effort tiers: low, medium, and
high. For Claude Sonnet 5, we evaluated low and high effort. For GPT 6 Luna, we evaluated none, medium,
and xHigh effort.
Sampling parameter handling.Contemporary reasoning LLMs enforce strict constraints on sampling
parameters when internal deliberation is active. For Google LLMs accessed via the Google GenAI SDK, the
provider default parameters are temperature of 1.0, top-p of 0.95, and top-k of 64. For Anthropic LLMs
accessed via the Anthropic SDK, the default parameters are temperature of 1.0 and top-p of 1.0. When
extended or adaptive thinking is enabled, both Google and Anthropic API endpoints lock temperature
strictly to 1.0 and reject custom temperature or sampling overrides with client errors. For the OpenAI
LLM, no sampling parameters were specified, and requests used the provider defaults. Likewise, no sampling
parameters were specified for the open-weight LLMs, which were therefore sampled under the default settings
of llama-server. As a result, all LLMs were evaluated under their native out-of-the-box sampling distributions.
Tool execution constraints.To enforce the sequential search, LLMs were restricted to executing a single
tool per conversational turn. Parallel tool execution was disabled at the API level (disable_parallel_tool_use
set totruefor Anthropic andparallel_tool_callsset tofalsefor OpenAI and the open-weight LLMs) or
through single-tool constraints specified in system instructions for Google. Each session was executed as an
independent replication with a newly initialized context window to prevent state leakage or cross-session
memory carryover.
21
