---
title: Decision-aware User Simulation Agent for Evaluating Conversational Recommender Systems
url: https://arxiv.org/abs/2605.05250
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Yuan-Chi Li
- Li-Chi Chen
- Sung-Yi Wu
- Yu-Che Tsai
- Shou-De Lin
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.05250
pages: 15
chars: 57497
fetched_at: '2026-11-08T13:36:08+00:00'
kb_version: 1
---

# Decision-aware User Simulation Agent for Evaluating Conversational Recommender Systems

Decision-aware User Simulation Agent
for Evaluating Conversational Recommender Systems
Yuan-Chi Li Li-Chi Chen Sung-Yi Wu Yu-Che Tsai Shou-De Lin
Department of Computer Science and Information Engineering
National Taiwan University
{b09902110, r14922012, b11701201, f09922081, sdlin}@csie.ntu.edu.tw
Abstract
Conversational recommender systems (CRS)
increasingly rely on user simulators for auto-
mated evaluation of sales agents. A key re-
quirement for such simulators is the ability
to model human decision-making. However,
most LLM-based simulators often exhibit un-
realistically strong information-processing ca-
pabilities, rarely exhibiting the hesitation and
decision deferral commonly observed in real
consumer behavior, resulting in overly high
acceptance rates. To address this limitation,
we propose Hesitator, a theory-grounded user
simulation framework that explicitly models
human decision-making under choice overload.
The framework introduces a modular Decision
Module that separates utility-based item selec-
tion from overload-aware commitment deci-
sions. Experiments across multiple user simu-
lation frameworks, domains, sales modes, and
LLM backbones show that integrating our mod-
ule consistently mitigates unrealistic behaviors
under increasing overload conditions. Further-
more, Hesitator reproduces established behav-
ioral patterns from psychological economics,
demonstrating its ability to model human deci-
sion behavior.
1 Introduction
Large language model (LLM) agents have recently
been deployed across a wide range of applications,
including conversational assistants (Achiam et al.,
2023), autonomous task planning and tool use (Yao
et al., 2022; Schick et al., 2023), and complex multi-
step reasoning tasks (Wei et al., 2022). Among
these, conversational recommender systems (CRS)
represent a particularly compelling use case, where
agent-driven dialogues guide users toward purchase
decisions. Building effective sales agents for CRS,
however, demands reliable automated evaluation
pipelines, which in turn depend on realistic user
simulation (Zhang and Balog, 2020; Yoon et al.,
2024). In such simulated environments, faithfully
Great products!
Let’s make a
purchase!
Great products!
But I’m overloaded,
let’s defer.
Real Human
Purchase Needs:
I want to get a new pair of runners that is high-quality.
My budget is $150.
Sales
User
Hesitator
Considering
several overload
factors, I need to
defer.
Prior Agents
Here are some recommendations that fit your needs:
Item#1: [Brand A], [$120], ....., [Material B], ......, etc.
Item#2: [Brand B], [$100], ....., [Material C], ......, etc.
......
Item#9: [Brand C], [$150], ....., [Material A], ......, etc.
Item#10: [Brand D], [$170], ....., [Material D], ......, etc.
Figure 1: Motivation of Hesitator. Prior user agents
often make immediate purchase decisions after iden-
tifying good items, ignoring cognitive constraints. In
contrast, humans may defer decisions under choice over-
load. This gap motivates Hesitator, which models hesi-
tation by incorporating overload factors.
modeling human decision-making is critical for
assessing CRS effectiveness (Yoon et al., 2024).
When user simulators fail to capture the gap be-
tween stated intentions and actual behavior, esti-
mated purchase probabilities tend to be overly opti-
mistic, obscuring the intention–behavior frictions
that reduce real-world conversion rates (Sheeran,
2002; Carrington et al., 2014).
A prominent research direction for evaluating
sales agents involves simulating human behavior
through LLM-based agents. For instance, RecUser-
Sim implements a multi-module LLM agent archi-
tecture with persona, memory, and action modules,
whereas UserSimCRS follows an agenda-based
framework relying on predefined agenda transi-
tions and predefined goals. While these works
have demonstrated strong capabilities in model-
ing realistic individual personas and diverse user
populations (Zhao et al., 2025; Bernard and Ba-
log, 2025; Chen et al., 2025), a critical dimension
remains largely overlooked: the cognitive deci-
sion processes underlying user choices (Bettman
arXiv:2605.05250v1  [cs.IR]  5 May 2026

et al., 1998). Specifically, in real-world settings,
users do not always respond to recommendations
immediately or decisively. They may defer deci-
sions when presented with an excessive number of
options. This is a well-documented phenomenon
known as choice overload. However, because LLM-
based user agents inherit the strong information-
processing capabilities of their underlying mod-
els (Brown et al., 2020; Minaee et al., 2024), they
can handle large volumes of unstructured informa-
tion without exhibiting such cognitive strain. As a
result, existing user simulation frameworks tend to
underrepresent the hesitation and decision deferral
that commonly arise in real consumer behavior.
To address this limitation, we proposeHesitator,
a decision-aware user simulation framework built
around a Decision Module with two cognitively
grounded components. TheSelection Moduleem-
ploys a two-stage decision process from Bettman
et al. (1998), applying non-compensatory filtering
to prune the candidate set before compensatory
evaluation selects the final item. Without this ex-
plicit filtering stage, LLM-based agents tend to give
equal consideration to all presented items, which
does not reflect how real users selectively attend
to options under cognitive constraints. TheHesi-
tation Modulequantifies choice overload through
a four-dimensional overload vector whose dimen-
sions correspond directly to the moderator cate-
gories identified in the meta-analysis of Chernev
et al. (2015): the number of alternatives, attribute
complexity, decision goal, and preference uncer-
tainty. Crucially, rather than relying on LLM judg-
ment alone, we leverage the regression coefficients
derived from that meta-analysis to construct a cal-
ibrated mapping function that translates the over-
load vector into an acceptance probability, ground-
ing the agent’s deferral behavior in large-scale em-
pirical evidence rather than model priors.
Experimental results yield two key findings.
First,Hesitatorreproduces well-established re-
sults from behavioral economics, including the
inverted-U effect of total information load (Jacoby
et al., 1974), the increasing-then-plateau effect of
attribute information (Fasolo et al., 2007), and de-
cision conflict theory (Tversky and Shafir, 1992;
Anderson, 2003). Second, integrating our decision
module into three existing user simulation frame-
works demonstrates that this lightweight addition
significantly mitigates unrealistic user behaviors
across diverse datasets, sales agent configurations,
and LLM backbones. Notably, while existing user
agents exhibit flat or even increasing acceptance
rates under severe choice overload, augmented
agents with our decision module display a clear
decline consistent with human cognitive patterns.
These results together demonstrate thatHesitator
reliably models the deferral aspect of human de-
cision behavior under diverse overload conditions.
We summarize our contributions as follows:
• We identify a key limitation of existing LLM-
based user simulators for conversational recom-
mender systems (CRS): their lack of cognitive
constraints when processing large amounts of
information often leads to unrealistically high
acceptance rates, inflating estimates of CRS per-
formance.
• We propose a plug-and-playDecision Module
that models intention–behavior friction under
choice overload, enabling simulated users to
adapt their commitment decisions according to
the cognitive load of the decision environment.
• We introduceHesitator, a modular user simula-
tion framework that integrates the Decision Mod-
ule and reproduces established behavioral pat-
terns from decision-making research, enabling
more realistic and reliable CRS evaluation.
2 Preliminary
2.1 Psychological Economics Theory
8 16 24 32 48 72
TOTAL INFORMATION
0
2
4
6
8
10# CORRECT CHOICES
Figure 2: Illustration of the inverted-U relationship be-
tween information load and decision quality in con-
sumer decision research (Jacoby et al., 1974). As in-
formation increases, decision performance initially im-
proves but eventually declines due to cognitive overload.
Inverted U Information Overload CurveEarly
work in consumer psychology established the con-
cept of information overload. As shown in Figure 2,
prior studies proposed an inverted-U relationship
between total information load and consumer de-
cision quality (Jacoby et al., 1974). This model
jointly considers assortment size and attribute quan-
tity, suggesting that decision performance improves
up to an optimal point but subsequently declines

once cognitive load exceeds an individual’s pro-
cessing capacity (Eppler and Mengis, 2004; Lurie,
2004). Furthermore, meta-analytic evidence sug-
gests that individuals with lower preference un-
certainty are less susceptible to information over-
load, as experts are better able to process and
filter large amounts of information than novices
(Chernev et al., 2015).
Independent Effects of Assortment and At-
tributesSubsequent research suggests that as-
sortment size and the number of attributes should
be treated as independent factors rather than a
single aggregate information measure (Malhotra,
1982; Keller and Staelin, 1987). Increasing the
number of attributes can improve decision perfor-
mance by providing more diagnostic information
(Fasolo et al., 2007). In contrast, larger assortments
may impair decision performance when additional
options introduce substantial tradeoffs. Accord-
ing to decision conflict theory, when alternatives
possess complementary attributes such that none
clearly dominates, consumers experience psycho-
logical conflict (Tversky and Shafir, 1992; Ander-
son, 2003), which often leads to decision deferral
or reduced transaction likelihood (Iyengar and Lep-
per, 2000; Chernev, 2003).
2.2 Notations
The notation used throughout this work is defined
as follows. Calligraphic letters (e.g., G) denote
high-level modules or sets, bold symbols (e.g., v)
represent multidimensional vectors, and Greek let-
ters (e.g., ϕ, σ) indicate internal persona traits or
external scenario constraints. Table 2 summarizes
the main symbols.
Agent State RepresentationThe core of our
framework is the global user agent state G=
(P,S) , which encapsulates the interaction between
a user’s stable characteristics and their immediate
environment. Thepersona( P) represents the in-
trinsic psychological profile of the user, parameter-
ized by a vector of traits ϕ= [ϕ O, ϕK, ϕU ]⊤ cor-
responding toOpenness,Pickiness, andPreference
Uncertainty. Thescenario( S) captures the contex-
tual conditions of the recommendation task through
environmental constraints σ= [σ N , σB, σT ]⊤, rep-
resentingCurrent Needs,Budget, andTime Pres-
sure. In addition, thedialogue history( H) records
the sequential interaction between the agents, for-
mulated as H={(u 0),(r 1, u1), . . . ,(rt, ut)},
where r denotes the response of the Sales Agent
andudenotes the response of the User Agent.
Cognitive Overload HierarchyFollowing the
theoretical framework of Chernev et al. (2015), the
consumer cognitive state is modeled using a multi-
dimensional overload vector v= [v a, vs, vt, vu]⊤.
This vector decomposes the choice environment
into four primary antecedents:Assortment Size
(va),Choice Set Complexity( vs),Task Difficulty
(vt), andPreference Uncertainty( vu). These fac-
tors are further organized into a hierarchical struc-
ture of leaf variables. The aggregate cognitive im-
pact of these factors is quantified as the total over-
load effect size dtotal, which serves as the primary
latent variable governing the agent’s decision to
accept or reject.
2.3 Simulation Process
The simulation framework operates in a CRS as a
turn-based dialogue between a Sales Agent and a
User Agent. The interaction is governed by a global
user state G= (P,S) , where P denotes the user
persona and S the shopping scenario. A dialogue
history H={(u 0),(r 1, u1), . . . ,(rt, ut)} is main-
tained, where rt and ut denote the responses of the
Sales Agent and User Agent at turn t, respectively.
The interaction is initialized by the User Agent
with an initial message u0 describing the user’s
needs given G. At each turn t, the Sales Agent
generates rt by retrieving candidate items from
the database based on inferred preferences and
dialogue history H. The User Agent then eval-
uates rt together with G and produces ut, which
includes the decision outcome (e.g., accept, reject,
or defer) and an explanation when rejecting the
recommendation. The dialogue history is updated
as H ← H ∪ {(rt, ut)}, and the interaction con-
tinues until a purchase decision is reported or the
predefined turn limitTis reached.
3 Method
In this section, we presentHesitator, an LLM-
based framework that simulates user decisions via
three different modules. As illustrated in Fig. 3,
the Decision Module consists of aSelection Mod-
ulethat identifies items satisfying the user’s needs
and aHesitation Modulethat models commitment
decisions under cognitive overload. To support
conversational recommendation, aResponse Mod-
ulefurther converts internal decisions into natural
language responses.

Decision Module
Selection Module
EBA
WADD
Utility
Threshold
Hesitation Module
CRS
Recommendation
[𝑣!,𝑣",𝑣#,𝑣$]
∅(𝑑)
𝑃!""#$%
Random
Value
Budget
𝜎!
 Current
Needs
𝜎"
Attribute Weight
𝑤
Response Module
Response
Generator
Action
Selector
Accept
Reject
LLM Perception
User  Response
Sales  Response
No Recommendation
Accept
Reject
Figure 3: Architecture of the Hesitator framework. The Selection Module filters and ranks items (EBA → W ADD).
If the recommendation passes the selection stage (accept), it proceeds to the Hesitation Module, which estimates the
final acceptance probability based on perceived overload factors; otherwise, the system directly generates a rejection
response. Solid lines indicate data flow, while dashed lines denote internal stage transitions within the user agent.
3.1 Decision Module
Real-world decisions involve both evaluating op-
tion quality and determining whether to commit
under cognitive constraints. Accordingly, theDeci-
sion Moduleis formulated as a conditional sequen-
tial pipeline: first, theSelection Moduleevaluates
the intrinsic utility of the recommended items I
based on the last sales agent recommendation re-
sponse rt. If the options fail to meet basic expecta-
tions (encoded in G), the agent directly rejects the
recommendation at this turn. Conversely, if an ac-
ceptable option is identified, the process advances
to theHesitation Module, which models choice
overload to determine whether the user commits
to the choice or defers. The final outcome D is
subsequently routed to theResponse Module.
3.1.1 Selection Module
Evaluating multiple recommended items can be
cognitively demanding, making it impractical to
exhaustively compare all options. To approxi-
mate human decision strategies, theSelection Mod-
uleadopts a two-stage heuristic-to-compensatory
process, which is commonly observed in human
decision-making (Bettman et al., 1998). This
pipeline is grounded in the constructive consumer
choice framework of Bettman et al. (1998) and rep-
resents one cognitively plausible family of heuris-
tics that fits attribute-driven shopping behavior—
the dominant regime in CRS research, where users
express constraints and preferences over discrete
attribute dimensions such as price, brand, and spec-
ifications. We do not claim it as a universal model
of human decision-making; less attribute-driven
settings (e.g., aesthetic-driven, emotion-driven, or
exploratory shopping) may follow different cog-
nitive strategies and motivate alternative selection
strategies as future work. Specifically, it first elimi-
nates options that violate the user’s hard constraints
and then estimates compensatory utility over the
remaining candidates.
Stage 1: Non-compensatory Filtering.If the
initial set |I|> θ, the agent employs Elimination
by Aspects (EBA). An item i∈ Iis retained in the
candidate set C if it satisfies all critical constraints
K(e.g., price≤σ B):
C={i∈ I | ∀k∈ K,Ik(i) = 1}(1)
Stage 2: Compensatory Evaluation.When
|C| ≤θ(we set θ= 3 following established heuris-
tics (Bettman et al., 1998)), the agent evaluates
utility ui via a Weighted Additive (WADD) func-
tion:
ui =w ⊤ai =
nX
j=1
wj ·a ij (2)
where aij is the attribute vector perceived by the
LLM and wj is extracted from historical reviews
(see Appendix C.1).

Acceptance MechanismFollowing compen-
satory evaluation, the selection outcome s=
{su, si} is defined by the highest utility su =
maxi∈C ui and the corresponding item si =
arg maxi∈C ui. The agent compares su with a
pickiness-dependent threshold τ(ϕ K) =γ+αϕ K
(with γ= 0.6, α= 0.1 ), where γ and α are tun-
able hyperparameters used to simulate different
user acceptance levels. If su < τ(ϕK), the recom-
mendation is rejected and passed to theResponse
Module; otherwise, it proceeds to theHesitation
Module fhesitate to evaluate potential deferral. The
Selection Module is architecturally modular: alter-
native selection strategies can be substituted as a
drop-in replacement without modifying the Hesita-
tion Module or Response Module.
3.1.2 Hesitation Module
Even when a satisfactory option exists, users may
defer decisions due to cognitive overload (Chernev
et al., 2015). To capture this phenomenon, theHes-
itation Modulemodels the probability that a user
commits to the identified option given the perceived
cognitive load of the decision environment. This
module operates in three phases: (1) inferring the
user’s cognitive state (v) from dialogue, (2) cali-
brating these observations to behavioral effect sizes
(dtotal), and (3) mapping the aggregated overload to
the final acceptance probability (Paccept).
Phase 1: State Perception.The framework elicits
granular intensity scores v∈ {1,2,3} for five leaf
dimensions (i.e., va, vs,d, vs,a, vt,a, and vt,f ) via
LLM-based prediction. The remaining leaf vari-
ables, vu and vt,p, are predefined constants deter-
mined by the user persona (ϕU) and task constraints
(σT ). Composite factors vk ∈ {vs, vt} are formally
defined as the arithmetic mean of their respective
constituent leaf sets.
Phase 2: Meta-Analytic Calibration. The Hesi-
tation Module needs to map a perceived overload
state into a real-valued acceptance probability, and
this mapping should be grounded in evidence about
real human deferral behavior rather than model pri-
ors. Relying on an LLM alone to judge how much
a given overload level should reduce commitment
willingness would require fine-grained behavioral
calibration that LLMs handle poorly and incon-
sistently. Instead, we leverage the meta-analytic
regression of Chernev et al. (2015), which aggre-
gates effect sizes across 99 published experimental
observations and provides an empirically estimated
mapping from overload moderators to standard-
ized effect sizes (Cohen’s d). By inheriting their
regression coefficients, our module obtains a cal-
ibration that reflects population-scale human de-
cision behavior. To connect discrete LLM-based
perceptions with continuous behavioral effects, we
map perceived overload factors to empirical effect
sizes derived from the meta-analysis of Chernev
et al. (2015). This meta-analysis reports standard-
ized effect sizes (Cohen’s d) across heterogeneous
experimental settings. Specifically, δ encodes, for
each overload factor, the minimum and maximum
effect sizes observed across the meta-analyzed stud-
ies. We use δ to construct the interpolation function
finterp(·), which maps a discrete LLM-perceived
overload level v∈ {1,2,3} onto a continuous ef-
fect-size value within this empirically observed
range. Without δ, the perceived overload levels
would have no behavioral scale; δ is what gives
them magnitude grounded in empirical evidence.
Four key overload factors are perceived by an
LLM:assortment size( va),choice set complexity
(vs),task difficulty( vt), andpreference uncer-
tainty( vu), while factors with negligible effects in
CRS are omitted (Appendix B.1). Each perceived
factor level is mapped to an empirical effect-size
range viaf interp(·).
Following the meta-analytic regression formu-
lation, the aggregate overload effect is computed
as:
dtotal =β ⊤finterp(v, δ)(3)
where v= [v a, vs, vt, vu] denotes the perceived
factor levels and β are moderator coefficients
from the meta-analysis. Detailed mapping proce-
dures and parameter settings are provided in Ap-
pendix B.4.
Phase 3: Probabilistic Mapping.To convert the
aggregated overload effect size into a decision prob-
ability, we adopt the arcsine-based proportion trans-
formation commonly used in statistical power anal-
ysis (Cohen, 2013; Fleiss et al., 2013). Rearranging
the formulation yields the following closed-form
expression:
Paccept = sin2

arcsin(
p
Pbase)− dtotal 2  (4)
The derivation is provided in Appendix B.2.
Here, Pbase = 0.5 represents a neutral prior that
balances the bidirectional effects of the “more-
is-better” tendency and choice overload (see Ap-
pendix B.3). The value of dtotal is bounded to

ensure that the resulting probability remains within
[0,1] . With Pbase = 0.5, dtotal is truncated to the
range [−π/2, π/2]. A purchase is triggered only if
a random sample ϵ≤P accept; otherwise, the agent
defers the decision and provides a rationale.
3.2 Response Module
TheResponse Moduleconverts internal decisions
into communicative actions through two prompt-
based substeps. It first performsAction Selec-
tion A=LLM(G,H,D) , prompting an LLM to
choose a high-level communicative intent (e.g., ac-
cept, ask follow-up, request clarification, or de-
fer) given the global state, dialogue history, and
decision outcome. Finally,Response Synthesis
R=LLM(G,H,D,A) prompts the LLM to ver-
balize the final response R conditioned on the same
context together with the selected action. The full
prompts used for both substeps are provided in
Appendix??.
4 Experiments
4.1 Experimental Setup
Simulation Environment.We simulate conver-
sational recommendation interactions using two
domains from theAmazon Reviews 2023dataset
(Hou et al., 2024):ElectronicsandVideo Games.
Each experimental configuration is evaluated over
N= 40 independent sessions. A session follows a
turn-based dialogue history H and imposes a maxi-
mum of T= 20 interaction turns. Each session is
initialized with a unique global state G that defines
the user persona and shopping scenario.
User Profiles.The user state G consists of a per-
sona P={ϕ O, ϕK, ϕU } and a shopping scenario
S={σ N , σB, σT }. Persona traits include open-
ness, pickiness, and preference uncertainty, while
the scenario specifies the user’s needs, budget, and
time pressure, without revealing the item title to
avoid data leakage (Zhu et al., 2024).
Sales Agent.We adopt CSI (Kim et al., 2025) as
the sales agent framework and usegpt-oss-20b as
the backbone model. The agent retrieves candidate
items through a vector retrieval system built on
Qwen3-Embedding-0.6B. It operates in two modes:
Basic(preference probing and suggestion) andPer-
suasive(strategic persuasion actions).
Baselines.We compare our method against three
representative user simulators:PersonaLens(Zhao
et al., 2025),UserSimCRS(Bernard and Balog,
2025), andRecUserSim(Chen et al., 2025), the
current SOTA user simulator for CRS. All baselines
share the same backbone model ( gpt-oss-20b)
and identical initialization states to ensure a con-
trolled comparison.
Evaluation Metrics.We evaluate the user agent
systems using three complementary metrics:Suc-
cess Rate (SR),Subjective Dialogue Quality
(Chen et al., 2025), andBelievability(Xiao et al.,
2023). SR measures the proportion of sessions end-
ing with a purchase decision. Dialogue quality is
assessed through pairwise comparisons along five
dimensions (realism, naturalness, relevance, clar-
ity, adaptability). Believability is measured via the
hallucination ratio ¯HR. Detailed system implemen-
tation and metrics are provided in Appendix C and
D, respectively.
4.2 Overload Effect
We analyze how user-agent decision behavior
changes under different cognitive overload levels.
Specifically, we evaluate three conditions:Low,
Medium, andSevere. The exact parameter settings
for these conditions are described in Appendix D.2.
Anomalous Baseline BehaviorsFigure 4 shows
the success rates of different user-agent frameworks
under increasing cognitive overload. Without the
Decision Module, baseline simulators exhibit un-
realistic patterns: their success rates remain stable
or even increase as overload intensifies from Low
to Severe. For example, in the Electronics domain,
PersonaLensrises from 60.0 to 70.0 andUserSim-
CRSfrom 35.0 to 55.0. Similar trends appear in the
Video Games domain, wherePersonaLensreaches
75.0 andUserSimCRSmaintains 70.0 under Se-
vere overload. These behaviors contradict well-
established findings in consumer decision-making,
where increasing overload typically raises cogni-
tive conflict and leads to decision deferral.
Behavioral Correction via Decision Module
After integrating the Decision Module (+DM), all
baseline user simulators exhibit behavior consis-
tent with human decision patterns: success rates
decline as overload increases from Low to Se-
vere. For example, in the Electronics domain,
RecUserSim+DMdrops from 67.5 to 22.5 and
PersonaLens+DMfrom 90.0 to 35.0. A similar
trend is observed forUserSimCRS+DM, which
decreases from 65.0 to 50.0. Consistent patterns
also appear in the Video Games domain, where
RecUserSim+DMfalls from 70.0 to 12.5 andPer-
sonaLens+DMfrom 77.5 to 22.5 under Severe

Low Overload Medium Severe Overload
UserSimCRS
PersonaLens
RecUserSim
Hesitator
UserSimCRS + DM
PersonaLens + DM
RecUserSim + DM
35.0* 42.5 55.0
60.0 62.5 70.0
50.0 45.0 45.0
85.0*** 95.0 35.0
65.0 67.5 50.0
90.0*** 77.5 35.0
67.5*** 55.0 22.5
Electronics
Low Overload Medium Severe Overload
60.0 72.5 70.0
60.0 50.0 75.0
60.0 40.0 60.0
82.5*** 80.0 32.5
62.5* 70.0 37.5
77.5*** 62.5 22.5
70.0*** 47.5 12.5
Video Games
Figure 4: Simulation success rates (%) of different user agents under varying levels of cognitive overload in two
domains (Electronics and Video Games). The Decision Module (+DM) is designed to mitigate the original tendency
of user agents to remain insensitive to cognitive overload, enabling their decision behavior to vary more appropriately
with overload level. As a result, success rates decline under severe overload, better reflecting human decision
patterns. Statistical significance is determined using the Wilcoxon signed-rank test(Low vs. Severe overload); *
(p <0.05), ** (p <0.01), and *** (p <0.001).
0 10 20 30 40 50 60 70
Information Amount (Nrec × Nattr)
0.25
0.50
0.75Success Rate
PU = 1
PU = 2
PU = 3
(a) Success rate vs. total information
1 2 3 4 5 6 7 8
Number of Attributes (Nattr)
0.25
0.50
0.75Success Rate
PU=1
PU=2
PU=3 (b) Success rate vs. number of attributes
1 2 3 4 5 6 7 8
Assortment Size (Nrec)
0.25
0.50
0.75Success Rate
PU=1
PU=2
PU=3 (c) Success rate vs. assortment size
Figure 5: Decision success under different information conditions and preference uncertainty (PU). (a) Total
information exhibits an inverted-U relationship with success rate, consistent with information overload findings. (b)
Increasing attribute information improves success initially but shows diminishing returns. (c) Larger assortments
reduce success under high uncertainty, reflecting decision conflict and choice overload.
overload. Overall, these results indicate that the
Decision Module corrects unrealistic decision be-
havior in existing simulators and enables them to
reproduce the decline in decision commitment com-
monly observed under severe cognitive overload.
Additional results across different sales agents and
LLM backbones are provided in Appendix F.1.
4.3 Analysis on Psychological Economics
Theory
To further evaluate the realism of the proposed
user agent, we examine whetherHesitatorcan re-
produce established findings in psychological eco-
nomics.
Inverted-U Information Overload CurveAs
shown in Figure 5a, the pattern closely follows
the classical findings of Jacoby et al. (1974) (Fig-
ure 2): success rates initially increase as infor-
mation grows, peak at moderate information lev-
els, and then decline once cognitive load be-
comes excessive, forming an inverted-U relation-
ship between information quantity and decision
performance. Notably, the decline becomes less
pronounced as preference uncertainty decreases.
Agents with lower uncertainty exhibit a flatter
post-peak slope, indicating greater resilience to
information overload. This reproduces a well-
documented behavioral phenomenon in consumer
decision-making: individuals with higher exper-
tise are less likely to defer decisions under high
information load.
Independent Effects of Assortment and At-
tributesWe further analyze the independent ef-
fects of assortment size (Nrec) and attribute quan-
tity (Nattr), as illustrated in Fig. 5b and Fig. 5c.
Consistent with prior studies (Malhotra, 1982;
Keller and Staelin, 1987), the two factors exhibit
distinct impacts on decision behavior. Increasing
attribute information generally improves decision
performance by providing more diagnostic cues for
evaluating alternatives. In contrast, larger assort-
ments introduce decision conflict among compet-
ing options, causing success rates to decline as the
number of recommendations increases (Tversky
and Shafir, 1992).
4.4 Comprehensive Conversation Simulation
Evaluation
Subjective EvaluationFigure 6 compares the
conversational simulation quality across user
agents. Hesitator consistently outperforms the base-
line simulators (RecUserSim, UserSimCRS, and

Overall
Naturalness
Clarity
Adaptability
Relevance
Realism
10
20
30
40
50
Hesitator
RecUserSim
UserSimCRS
PersonaLens
Figure 6: Subjective evaluation of conversational simu-
lation quality across user agents.
PersonaLens) across multiple evaluation dimen-
sions, including overall quality, naturalness, clarity,
adaptability, relevance, and realism. This indicates
that our user agent not only models decision be-
havior more realistically but also maintains strong
conversational quality, producing responses that
are more natural, coherent, and contextually appro-
priate than existing simulators. Detailed evaluation
setup is provided in Appendix D.1.2
Believability EvaluationTable 1 reports hallu-
cination ratios under vanilla and decision-module
settings. Adding the Decision Module does not
increase hallucination and slightly reduces hal-
lucination for most simulators. PersonaLens de-
creases from 0.1290 to 0.1088 and UserSimCRS
from 0.2548 to 0.2268, while RecUserSim changes
only marginally from 0.0584 to 0.0624. These re-
sults suggest that the Decision Module preserves re-
sponse believability without introducing additional
hallucination. Hesitator nevertheless exhibits a
higher hallucination ratio than RecUserSim, likely
because the latter includes a dedicated response
refinement stage that helps reduce hallucinations
before output.
4.5 Ablation Study
To isolate the effect of structured item evaluation
in the proposed framework, we conduct an abla-
tion study on theSelection Moduleby replacing it
with a standard rating-based prompt. The Selec-
tion Module models human-like item evaluation
via a two-stage decision strategy. As shown in Fig-
ure 7, removing this module leads to unstable per-
formance as the number of attributes increases, and
the expected positive effect of additional attributes
Model Vanilla DM
Hesitator 0.0969 –
PersonaLens 0.1290 0.1088
RecUserSim 0.0584 0.0624
UserSimCRS 0.2548 0.2268
Table 1: Average hallucination ratio under vanilla and
decision-module (+DM) settings. The Decision Module
does not increase hallucination and slightly reduces it
for most simulators, indicating preserved response be-
lievability.
1 2 3 4 5 6 7 8
Number of Attributes (Nattr)
0.4
0.6
0.8Success Rate
w/ Item Selector
w/o Item Selector
Figure 7: Ablation results for the Selection Module with
varying numbers of attributes.
is no longer consistently observed, deviating from
human behavior. This suggests that, without struc-
tured utility computation, the user agent fails to
faithfully reproduce human decision-making.
5 Related Work
User Simulation for Conversational Recommen-
dationUser simulation is widely used to evalu-
ate CRS without requiring costly human studies.
Early work relied on rule-based simulators that gen-
erate responses using predefined policies or slot-
filling strategies (Zhang and Balog, 2020), offering
strong controllability but limited linguistic diver-
sity; later agenda-based simulators model users as
goal-driven agents maintaining structured dialogue
goals, as exemplified byUserSimCRS(Bernard and
Balog, 2025). Recent research increasingly adopts
LLM-based simulators to produce more natural
and context-aware responses. For instance,Per-
sonaLens(Zhao et al., 2025) conditions LLMs on
persona descriptions and dialogue context, while
RecUserSim(Chen et al., 2025) introduces a mod-
ular architecture to improve behavioral diversity
and extensibility. Other work enhances simulation
realism by modeling richer user characteristics and
evolving intents, such as personality-driven simu-
lators that condition LLMs on stable persona traits
(Ma et al., 2025; Gromada et al., 2025) and CRS
methods that track intent evolution during dialogue
(e.g., DICR (Zhou et al., 2022) and Chat-REC (Gao

et al., 2023)). However, LLM-based simulators rely
on implicit reasoning without explicitly modeling
human decision processes, often producing overly
rational behaviors that overlook hesitation under
choice overload. We address this by introducing
an explicit Decision Module that separates utility-
based selection from overload-aware hesitation to
enable structured and controllable commitment de-
cisions.
Cognitive Architectures for Decision Modeling
Cognitive science has long studied computational
models of human decision-making. Architectures
such as ACT-R (Anderson et al., 2004) and SOAR
(Laird, 2019) simulate human cognition through
structured modules for perception, memory, and
action selection, enabling the modeling of com-
plex behavioral patterns. However, these architec-
tures are typically designed for controlled labora-
tory tasks and rely on symbolic representations that
are difficult to integrate with modern conversational
systems. In contrast, our approach augments LLM-
based simulators with a theory-grounded Decision
Module that models cognitive constraints such as
choice overload.
6 Conclusion
In this paper, we introduce Hesitator, a theory-
grounded user simulation framework designed to
model one important dimension of human decision-
making under cognitive constraints in conversa-
tional recommendation : decision deferral under
choice overload. By integrating a modular De-
cision Module, composed of a Selection Module
that mimics heuristic to compensatory item evalu-
ation and a Hesitation Module that models choice
overload, the framework enables LLM-based user
agents to simulate both utility-driven selection and
overload-induced decision deferral. Experimental
results show that incorporating our module consis-
tently corrects unrealistic behaviors in existing sim-
ulators under increasing overload conditions while
maintaining strong conversational quality. More
importantly, Hesitator reproduces established be-
havioral patterns from psychological economics,
demonstrating its effectiveness in capturing this
overload-driven aspect of human-like decision dy-
namics and providing a more reliable benchmark
for evaluating conversational recommendation sys-
tems.
Limitations
This work has several limitations. First, our ex-
periments focus on two product domains from the
Amazon Reviews dataset. Although these domains
are widely used in conversational recommendation
research, future work should examine whether sim-
ilar behavioral patterns emerge in other domains
with different decision characteristics. Second, the
hesitation mechanism relies on parameters derived
from a large-scale meta-analysis in consumer psy-
chology. While this grounding provides empirical
support for the modeling assumptions, future work
could explore adaptive calibration using domain-
specific behavioral data. Finally, user personas are
treated as static throughout each interaction session,
whereas real-world user preferences may evolve
during conversations. Extending the framework
to model dynamic preference shifts could further
improve simulation realism.
References
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama
Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
Diogo Almeida, Janko Altenschmidt, Sam Altman,
Shyamal Anadkat, and 1 others. 2023. Gpt-4 techni-
cal report.arXiv preprint arXiv:2303.08774.
Christopher J Anderson. 2003. The psychology of doing
nothing: forms of decision avoidance result from rea-
son and emotion.Psychological bulletin, 129(1):139.
John R Anderson, Daniel Bothell, Michael D Byrne,
Scott Douglass, Christian Lebiere, and Yulin Qin.
2004. An integrated theory of the mind.Psychologi-
cal review, 111(4):1036.
Nolwenn Bernard and Krisztian Balog. 2025. User-
simcrs v2: Simulation-based evaluation for con-
versational recommender systems.arXiv preprint
arXiv:2512.04588.
James R Bettman, Mary Frances Luce, and John W
Payne. 1998. Constructive consumer choice pro-
cesses.Journal of consumer research, 25(3):187–
217.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, and 1 others. 2020. Language models are
few-shot learners.Advances in neural information
processing systems, 33:1877–1901.
Michal J Carrington, Benjamin A Neville, and Gregory J
Whitwell. 2014. Lost in translation: Exploring the
ethical consumer intention–behavior gap.Journal of
business research, 67(1):2759–2767.

Luyu Chen, Quanyu Dai, Zeyu Zhang, Xueyang Feng,
Mingyu Zhang, Pengcheng Tang, Xu Chen, Yue Zhu,
and Zhenhua Dong. 2025. Recusersim: A realistic
and diverse user simulator for evaluating conversa-
tional recommender systems. InCompanion Pro-
ceedings of the ACM on Web Conference 2025, pages
133–142.
Alexander Chernev. 2003. When more is less and less
is more: The role of ideal point availability and as-
sortment in consumer choice.Journal of consumer
Research, 30(2):170–183.
Alexander Chernev, Ulf Böckenholt, and Joseph Good-
man. 2015. Choice overload: A conceptual review
and meta-analysis.Journal of Consumer Psychology,
25(2):333–358.
Jacob Cohen. 2013.Statistical power analysis for the
behavioral sciences. routledge.
Martin J Eppler and Jeanne Mengis. 2004. The con-
cept of information overload: A review of literature
from organization science, accounting, marketing,
mis, and related disciplines.The information society,
20(5):325–344.
Barbara Fasolo, Gary H McClelland, and Peter M Todd.
2007. Escaping the tyranny of choice: When fewer
attributes make choice easier.Marketing theory,
7(1):13–26.
Joseph L Fleiss, Bruce Levin, and Myunghee Cho Paik.
2013.Statistical methods for rates and proportions.
john wiley & sons.
Yunfan Gao, Tao Sheng, Youlin Xiang, Yun Xiong,
Haofen Wang, and Jiawei Zhang. 2023. Chat-
rec: Towards interactive and explainable llms-
augmented recommender system.arXiv preprint
arXiv:2303.14524.
Justyna Gromada, Alicja Kasicka, Ewa Komkowska,
Lukasz Krajewski, Natalia Krawczyk, Morgan
Veyret, Bartosz Przybył, Lina M Rojas Barahona,
and Michał K Szczerbak. 2025. Evaluating conver-
sational agents with persona-driven user simulations
based on large language models: A sales bot case
study. InProceedings of the 2025 Conference on
Empirical Methods in Natural Language Processing:
Industry Track, pages 230–245.
Yupeng Hou, Jiacheng Li, Zhankui He, An Yan, Xiusi
Chen, and Julian McAuley. 2024. Bridging language
and items for retrieval and recommendation.arXiv
preprint arXiv:2403.03952.
Sheena S Iyengar and Mark R Lepper. 2000. When
choice is demotivating: Can one desire too much
of a good thing?Journal of personality and social
psychology, 79(6):995.
Jacob Jacoby, Donald E Speller, and Carol A Kohn.
1974. Brand choice behavior as a function of informa-
tion load.Journal of marketing research, 11(1):63–
69.
Kevin Lane Keller and Richard Staelin. 1987. Effects of
quality and quantity of information on decision effec-
tiveness.Journal of consumer research, 14(2):200–
213.
Tongyoung Kim, Jeongeun Lee, Soojin Yoon, Sungh-
wan Kim, and Dongha Lee. 2025. Towards per-
sonalized conversational sales agents: Contextual
user profiling for strategic action.arXiv preprint
arXiv:2504.08754.
John E Laird. 2019.The Soar cognitive architecture.
MIT press.
Nicholas H Lurie. 2004. Decision making in
information-rich environments: The role of infor-
mation structure.Journal of consumer research,
30(4):473–486.
Chenglong Ma, Ziqi Xu, Yongli Ren, Danula Het-
tiachchi, and Jeffrey Chan. 2025. Pub: an llm-
enhanced personality-driven user behaviour simula-
tor for recommender system evaluation. InProceed-
ings of the 48th International ACM SIGIR Confer-
ence on Research and Development in Information
Retrieval, pages 2690–2694.
Naresh K Malhotra. 1982. Information load and con-
sumer decision making.Journal of consumer re-
search, pages 419–430.
Shervin Minaee, Tomas Mikolov, Narjes Nikzad,
Meysam Chenaghlu, Richard Socher, Xavier Am-
atriain, and Jianfeng Gao. 2024. Large language
models: A survey.arXiv preprint arXiv:2402.06196.
Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta
Raileanu, Maria Lomeli, Eric Hambro, Luke Zettle-
moyer, Nicola Cancedda, and Thomas Scialom. 2023.
Toolformer: Language models can teach themselves
to use tools.Advances in neural information process-
ing systems, 36:68539–68551.
Paschal Sheeran. 2002. Intention—behavior relations:
a conceptual and empirical review.European review
of social psychology, 12(1):1–36.
Amos Tversky and Eldar Shafir. 1992. Choice under
conflict: The dynamics of deferred decision.Psycho-
logical science, 3(6):358–361.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou,
and 1 others. 2022. Chain-of-thought prompting elic-
its reasoning in large language models.Advances
in neural information processing systems, 35:24824–
24837.
Colin White, Samuel Dooley, Manley Roberts, Arka
Pal, Ben Feuer, Siddhartha Jain, Ravid Shwartz-
Ziv, Neel Jain, Khalid Saifullah, Sreemanti Dey,
and 1 others. 2024. Livebench: A challeng-
ing, contamination-limited llm benchmark.arXiv
preprint arXiv:2406.19314.

Yang Xiao, Yi Cheng, Jinlan Fu, Jiashuo Wang, Wenjie
Li, and Pengfei Liu. 2023. How far are llms from
believable ai? a benchmark for evaluating the believ-
ability of human behavior simulation.arXiv preprint
arXiv:2312.17115.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
Shafran, Karthik R Narasimhan, and Yuan Cao. 2022.
React: Synergizing reasoning and acting in language
models. InThe eleventh international conference on
learning representations.
Se-eun Yoon, Zhankui He, Jessica Echterhoff, and Ju-
lian McAuley. 2024. Evaluating large language mod-
els as generative user simulators for conversational
recommendation. InProceedings of the 2024 Con-
ference of the North American Chapter of the Asso-
ciation for Computational Linguistics: Human Lan-
guage Technologies (V olume 1: Long Papers), pages
1490–1504.
Shuo Zhang and Krisztian Balog. 2020. Evaluating con-
versational recommender systems via user simulation.
InProceedings of the 26th acm sigkdd international
conference on knowledge discovery & data mining,
pages 1512–1520.
Zheng Zhao, Clara Vania, Subhradeep Kayal, Naila
Khan, Shay B Cohen, and Emine Yilmaz. 2025. Per-
sonalens: A benchmark for personalization evalua-
tion in conversational ai assistants. InFindings of
the Association for Computational Linguistics: ACL
2025, pages 18023–18055.
Jinfeng Zhou, Bo Wang, Minlie Huang, Dongming
Zhao, Kun Huang, Ruifang He, and Yuexian Hou.
2022. Aligning recommendation and conversation
via dual imitation. InProceedings of the 2022 Con-
ference on Empirical Methods in Natural Language
Processing, pages 549–561.
Lixi Zhu, Xiaowen Huang, and Jitao Sang. 2024. How
reliable is your simulator? analysis on the limitations
of current llm-based user simulators for conversa-
tional recommendation. InCompanion Proceedings
of the ACM Web Conference 2024, pages 1726–1732.
A Notation Summary
B Theoretical Background
B.1 Rationale for Omitting Partial Overload
Factors
Although Chernev et al. (2015) identifies a broader
set of determinants, we selectively exclude dimen-
sions that are incompatible with our experimen-
tal design. For example, the Decision Goal fac-
tor, including decision intent (buying vs. browsing)
and decision accountability, is omitted. In our set-
ting, user profiles are initialized with explicit goal-
oriented purchase needs, rendering browsing be-
havior irrelevant. Moreover, accountability effects,
Symbol Description
State V ariables
GGlobal user agent state(P,S)
PPersona
ϕO, ϕK , ϕU Openness, Pickiness, and Preference Uncer-
tainty
SPurchase Scenario
σN , σB, σT Current Needs, Budget, and Time Pressure
HDialogue History{(r 1, u1), . . .}
rResponse of the Sales Agent
uResponse of the User Agent
Cognitive Overload Modeling
vOverload vector[v a, vs, vt, vu]⊤
va Assortment Size
vs Choice Set Complexity
vs,d Dominance (Presence of dominant option)
vs,a Alignability (Attribute commensurability)
vt Task Difficulty
vt,p Time Pressure
vt,a Number of Attributes
vt,f Format Complexity
vu Preference Uncertainty
βCoefficients of the four overload factors
dtotal Calculated overload effect size
Decision Process
I,C Initial and candidate recommendation sets
(C ⊆ I)
θCognitive threshold for filtering
ai,wAttribute vector of itemiand user weights
ui Evaluated utility of itemi
Pbase Base acceptance probability (default: 0.5)
Paccept Final acceptance probability
Table 2: Summary of the main notations.
which arise when consumers must justify their deci-
sions to others, do not apply in a private interaction
between a simulated user agent and a sales system.
Within our experimental framework, these dimen-
sions inherently yield a null effect; specifically and
contribute an effect size of zero to the regression
model established by Chernev et al. (2015). Conse-
quently, their exclusion does not compromise the
validity of the analysis.
B.2 The Formula Derivation for Equation 4
Starting from the definition of the total effect size:
dtotal = 2

arcsin
p
Pbase −arcsin
p
Padjust

(5)
Dividing both sides by2gives
dtotal
2 = arcsin
p
Pbase −arcsin
p
Padjust.(6)
Rearranging to isolate the term containing
Padjust:
arcsin
p
Padjust = arcsin
p
Pbase − dtotal 2 .(7)

Applying the sine function to both sides yields
p
Padjust = sin

arcsin
p
Pbase − dtotal 2  .(8)
Finally, squaring both sides and letting Padjust =
Paccept gives
Paccept = sin2

arcsin
p
Pbase − dtotal 2  .(9)
B.3 Design forP base
Notably, the impact of assortment size on consumer
behavior is bi-directional and contingent upon the
specific moderating environment. When the an-
tecedents of overload—such as task difficulty or
choice set complexity—are at low levels, the ob-
served effect size (Cohen’s d) typically becomes
negative. This negative d-value signifies a "more-
is-better" effect, where larger assortments provide
a competitive advantage by increasing the likeli-
hood of an ideal preference match without exceed-
ing cognitive limits. To achieve behavioral high-
fidelity, a simulation framework must therefore sup-
port bi-directional dynamics: it must decrease the
acceptance probability to model choice deferral
under high-overload conditions, while conversely
increasing it when the cognitive load is sufficiently
low to reflect the utility gains and increased satis-
faction inherent in extensive assortments.
B.4 Connection to the Meta-Analytic
Regression Model
Chernev et al. (2015) estimates the magnitude of
the choice overload effect using a meta-analytic
regression model of the form
d=β 0 +β sxs +β txt +β uxu +ϵ(10)
where d denotes the standardized effect size re-
ported in each experimental observation, xk rep-
resents moderator variables characterizing the de-
cision environment, and β denotes the regression
coefficients estimated in the meta-analysis (see Ta-
ble 3 for the exact values).
In the original analysis, assortment size is pri-
marily operationalized through experimental con-
trasts between small and large choice sets and is
therefore absorbed into the intercept term. In our
simulation environment, however, the number of
recommended items varies explicitly across dia-
logue turns. To capture this variation, we reparame-
terize the baseline effect as a moderator associated
with assortment size.
Factorβ k δmin k δmax k
va 0.41 -0.18 1.22
vs 0.55 -1.65 0.48
vt 0.37 -0.59 0.81
vu 0.32 -1.34 1.21
Table 3: Parameters used to compute the overload effect
size.
Concretely, we express the assortment contribu-
tion as
da =f interp(va, δa)(11)
and define the total effect size as
dtotal =β ada +β sds +β tdt +β udu (12)
where the assortment coefficient βa reflects the
baseline magnitude of the assortment-size contrast
captured by the intercept term in the original meta-
analytic regression.
C Implementation Details
C.1 User Profile Construction
The global user state G is defined as the combina-
tion of a persona P={ϕ O, ϕK, ϕU } and a shop-
ping scenario S={σ N , σB, σT }. We instantiate
these components using synthesized profiles de-
rived from the Amazon Reviews 2023 corpus.
Persona and Scenario InstantiationFollowing
Kim et al. (2025), the openness valueϕO is inferred
from historical reviews via LLM-based analysis.
The pickiness ϕK and preference uncertainty ϕU
are treated as controllable variables in {1,2,3} .
For the shopping scenario, the dynamic budget σB
is sampled from the interquartile range of prices
within the corresponding leaf category to ensure
realistic purchasing power, while the time pressure
σT serves as a task-specific constraint.
The granularity of the user’s current needs σN is
modulated by preference uncertainty ϕU. When un-
certainty is medium or high (ϕU ∈ {2,3}), the user
is modeled with vague preferences: item descrip-
tions are limited to coarse attributes, and the weight
vector w is initialized uniformly. Conversely, when
uncertainty is low (ϕU = 1), the user is modeled as
a more expert decision-maker, using a non-uniform
weight vector w extracted from historical review
data.

Asymmetric InitializationTo better reflect re-
alistic sales interactions, we adopt an asymmetric
profile design. The User Agent is initialized with
the complete global state G. In contrast, the Sales
Agent is provided only with the observable profile
{ϕO, ϕK}, representing traits that could plausibly
be inferred from a user’s review history. This in-
formation asymmetry requires the Sales Agent to
proactively infer the user’s latent intent and con-
straints through dialogue.
C.2 Sales Agent Implementation
Recommendation Retrieval MechanismTo fa-
cilitate efficient and relevant item retrieval, we
construct a vector-based retrieval system using
Qwen3-Embedding-0.6B as the backbone embed-
ding model. All retrieval operations are performed
using cosine similarity over an HNSW-based vector
index, returning the top-Kresults (K= 50).
Database EstablishmentFor each item in Ama-
zon Reviews 2023 across the target domains, we
construct a textual representation by concatenating
the title, category path, and product description.
This representation is then embedded into a 1,024-
dimensional vector space and stored in a vector
database for subsequent retrieval.
Retrieval MechanismsThe Sales Agent em-
ploys two retrieval modes to support different
strategic actions.
• Query-based Retrieval (Suggest).When the
agent identifies explicit user preferences, it
converts the inferred preference description
into a query embedding and retrieves the top-
Kcandidate items from valid subcategories.
• Item-based Retrieval (Persuade).To sup-
port persuasive strategies, the agent performs
a similarity search centered on the currently
recommended item. By retrieving items with
high semantic similarity, the agent can present
alternative products that reinforce salient at-
tributes or provide comparative context.
D Experimental Setup
D.1 Evaluation Metrics
D.1.1 Success Rate
Success Rate (SR) measures the proportion of sim-
ulated sessions that end with a completed purchase
decision. Given N simulated sessions, it is defined
as
SR= 1 N NX i=1 I(purchasei),(13)
where I(·) is the indicator function, which equals
1if sessioniends in purchase and0otherwise.
D.1.2 Subjective Dialogue Quality
We evaluate dialogue quality using pairwise com-
parisons between dialogues generated by different
user agents. Given four agents, we construct all4
2

agent pairs and conduct dialogue-level compar-
isons for each pair. Each pair is evaluated along
five dimensions:realism,naturalness,relevance,
clarity, andadaptability, where the judge selects
the better dialogue for each dimension.
We useGemini 3 Flashas the judge model be-
cause it provides stronger analytical and reasoning
capabilities than the backbone model,gpt-oss-20b,
used for dialogue simulation (White et al., 2024).
For each comparison setting, we aggregate the out-
comes across all N= 40 simulated sessions and
report the resulting win rates.
D.1.3 Hallucination Ratio
To assess the believability of the simulated user
agent, we compute the Hallucination Ratio ( ¯HR),
which quantifies the proportion of mentioned en-
tities that are not supported by the available evi-
dence.
For each dialogue turn t in scenario i, the turn-
level hallucination ratio is defined as
HR,i,t = Hi,t Hi,t +R i,t ,(14)
where Hi,t is the number of hallucinated entities
and Ri,t is the number of grounded entities. An
entity is considered grounded if it can be verified
from either the user profile P or the dialogue his-
tory H; otherwise, it is counted as hallucinated.
Entity extraction and classification are performed
using a structured LLM-as-a-judge parser.
To obtain the final reported score, we first av-
erage the turn-level ratios over the T= 20 turns
within each scenario, and then average the resulting
scenario-level values across all N= 40 indepen-
dent sessions:
¯HR = 1 N NX i=1  1 T TX t=1 HR,i,t ! .(15)
user’s historical review sentiments.

D.2 Hyper-parameters for Overload
Experiments
Low Medium Severe
ϕO (Openness) 2 2 2
vt,p (Time Pressure) 1 2 3
vt,f (Format Complexity) 1 1 3
vu (Preference Uncertainty) 1 2 3
|I|(Recommendations) 3 3 3
vt,a (Number of Attributes) 8 8 8
Table 4: Hyper-parameter settings used in the overload-
effect experiment.
D.3 Hyper-parameters for Behavioral
Reproduction
The following parameters are fixed across all ex-
periments:
Parameter Value
ϕO (Openness) 2
ϕK (Pickiness) 2
vt,p (Time Pressure) 2
vt,f (Format Complexity) 1
Table 5: Fixed hyper-parameters in behavioral reproduc-
tion experiments.
Total Information CurveBoth assortment size
va and number of attributesv t,a are varied.
Assortment Size Curve vt,a = 5 , while va is
varied.
Number of Attributes Curve va = 3, while vt,a
is varied.
E Use-of-LLMs
Large language models (LLMs) are used in this
work primarily as core components of the proposed
framework. Specifically, LLMs serve as the back-
bone of the user simulator, generating conversa-
tional behaviors under different experimental con-
ditions. They are also used as embedding models
to encode items into dense representations for the
embedding process, and as automatic evaluators
(LLM-as-a-judge) to provide complementary eval-
uation signals.
Outside the modeling pipeline, LLMs are used
only for minor writing and coding assistance, with-
out affecting the experimental design or results.
F Additional Experimental Results
F.1 Additional Overload Results Across
Sales-Agent Settings

Low Overload Medium Severe Overload
UserSimCRS
PersonaLens
RecUserSim
Hesitator
UserSimCRS + DM
PersonaLens + DM
RecUserSim + DM
60.0 62.5 57.5
80.0 80.0 80.0
62.5 45.0 60.0
87.5*** 82.5 40.0
60.0* 72.5 42.5
70.0* 80.0 47.5
65.0 70.0 50.0
Electronics
Low Overload Medium Severe Overload
62.5 62.5 67.5
72.5 77.5 77.5
60.0 62.5 57.5
85.0*** 77.5 40.0
77.5** 70.0 47.5
75.0** 75.0 45.0
57.5* 55.0 32.5
Video Games
Figure 8: Simulation success rates under varying levels of cognitive overload when the Sales Agent operates in
persuasive mode. The overall trend remains consistent with the main findings: after adding the Decision Module,
user simulators exhibit a clearer decline in success rates as overload increases.
Low Overload Medium Severe Overload
UserSimCRS
PersonaLens
RecUserSim
Hesitator
UserSimCRS + DM
PersonaLens + DM
RecUserSim + DM
37.5 37.5 30.0
37.5 55.0 55.0
27.5 30.0 27.5
62.5** 60.0 35.0
40.0** 60.0 12.5
52.5 75.0 55.0
42.5* 55.0 17.5
Electronics
Low Overload Medium Severe Overload
42.5 37.5 45.0
57.5 57.5 57.5
35.0 30.0 32.5
70.0*** 67.5 30.0
52.5* 57.5 25.0
77.5 80.0 65.0
52.5** 62.5 17.5
Video Games
Figure 9: Simulation success rates under varying levels of cognitive overload across different LLM backbones. The
Decision Module consistently improves overload sensitivity across backbone choices, indicating that the behavioral
correction effect is robust to the underlying model.
