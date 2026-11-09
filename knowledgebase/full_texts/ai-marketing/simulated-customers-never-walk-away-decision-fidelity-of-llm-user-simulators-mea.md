---
title: 'Simulated Customers Never Walk Away: Decision Fidelity of LLM User Simulators Measured Against
  Real Purchase Outcomes'
url: https://arxiv.org/abs/2606.20708
category: ai-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Liang Chen
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.20708
pages: 19
chars: 57019
fetched_at: '2026-11-08T13:36:09+00:00'
kb_version: 1
---

# Simulated Customers Never Walk Away: Decision Fidelity of LLM User Simulators Measured Against Real Purchase Outcomes

Simulated Customers Never Walk Away:
Decision Fidelity of LLM User Simulators
Measured Against Real Purchase Outcomes
Liang Chen
June 2026
Abstract
LLM-as-user-simulation has quietly become core infrastructure for conversational AI:
agent benchmarks (τ-bench), training pipelines, and a fast-growing body of fidelity studies
all rely on LLMs role-playing the human side of the dialogue. Existing validation frameworks
measurecommunicative fidelity—whether simulators talk like humans—against ground truth
produced by paid participants role-playing assigned goals. We argue this paradigm has a
structural blind spot: when the user’s goal is assigned, the user’swillingnessis exogenous,
so no existing framework can test whether simulators makedecisionslike real users whose
motivation is endogenous, latent, and decaying. We introducedecision fidelity—whether
a simulated population reproduces the decision-state dynamics of real users facing real,
consequential choices—and measure it on a unique testbed: 2,790 production conversations
between an LLM sales agent and real customers, including 793 with verified payment outcomes.
Using a teacher-forced probe protocol that holds context and measurement instrument fixed,
we find a systematic, outcome-correlated failure we call thedisengagement deficit: simulators
reproduce eventual buyers almost exactly (depth bias+0.09) but inflate eventual non-buyers
toward the purchase frame (depth bias+0.40; group contrastd=0.38,p<0.001), halving their
expressed resistance (25.1%→13.5%) and nearly doubling deliberation (21.9%→40.1%) while
fabricating no purchases. The deficit replicates across model families (DeepSeek simulator:
d=0.41, p=0.002) and resists the obvious fix: explicitly instructing the simulator that it may
disengage cutsmarginalbias five-fold but barely moves the outcome-conditioned contrast
(d=0.34, p=0.008), merely relocating the error onto eventual buyers—decision fidelity is not
a prompting oversight. Real non-buyers say “not now” and stop; simulated non-buyers ask
about price. Evaluating or training sales and persuasion agents against such simulators
systematically overstates funnel progress exactly where it matters most—the customers who
walk away.
Keywords:LLM-as-user-simulation, user simulator, decision fidelity, agent evaluation, conver-
sational sales, sycophancy, simulation-to-real gap, persuasion dialogue
1 Introduction
Evaluating a conversational agent requires a counterparty. Because real humans are expensive,
slow, and hard to standardize, the field has converged on a pragmatic substitute:LLM-as-
user-simulation, in which a language model role-plays the human side of the dialogue. This
substitution is no longer a niche convenience. It underlies prominent agent benchmarks such as
τ-bench [17], supplies the interactive environments used to train and tune dialogue agents, and
has spawned a dedicated research thread onsimulator fidelity[8, 20, 21]. The premise of all of
this work is the same:if a simulator behaves enough like a real user, conclusions drawn against
it transfer to reality.
The fidelity literature has rightly focused on whether simulatorscommunicatelike humans. Re-
cent benchmarks measure stylistic realism, persona consistency, verbosity, information-disclosure
1
arXiv:2606.20708v1  [cs.AI]  16 Jun 2026

patterns, and emotional reactions, and report a persistent “realism gap” [8, 20]: simulators are
too verbose, too uniformly polite, too patient, and too cooperative. We take this work as our
point of departure and ask a question it cannot answer.
The blind spot.Every existing fidelity benchmark validates against ground truth produced
bypaid participants role-playing an assigned goal—book this flight, return this item, find this
product. When the goal is assigned, the user’swillingness to act is exogenous: it is handed
to the participant as part of the task. Consequently, no existing framework can test whether
a simulator reproduces the part of human behavior that matters most in the highest-stakes
deployments: theendogenous, latent, and decaying willingnessof a real person deciding whether
to commit. A real customer can lose interest, stall, deflect, and quietly disappear—and whether
they do isthe outcome the agent exists to influence. A role-player told to buy a flight never
genuinely decides not to.
We call the missing constructdecision fidelity: whether a simulated population reproduces
thedecision-state dynamics—how willingness, resistance, deliberation, and disengagement evolve
under persuasion—of real users facing real, consequential choices. Communicative fidelity
asks whether the simulatorsoundshuman; decision fidelity asks whether itdecideslike one.
For evaluating sales, fundraising, negotiation, and other persuasion agents, decision fidelity is
the property that actually determines whether simulator-based conclusions transfer—and it is
precisely the property no prior benchmark can measure, because no prior benchmark has real
outcomes.
A testbed with real stakes.We measure decision fidelity using a resource the fidelity
literature lacks:ZhenaiSales, 2,790 production conversations between a deployed LLM sales
agent and real customers of a Chinese relationship-matchmaking service, of which 793 end in a
verified paymentand the remainder do not. These are not role-players; their willingness is real
and their decisions cost real money. This lets us pose decision fidelity as a measurement problem
with ground truth—and, crucially, sidesteps the constraint that doomed our earlier attempts to
make causal claims from observational dialogue data: fidelity is a question aboutdistributional
match, for which observational data with outcomes is sufficient.
Method.We compare a simulator to reality with a teacher-forced probe protocol that controls
the two confounds that would otherwise contaminate the comparison. (i)Context is held fixed:
at a probe point we feed the simulator therealconversation prefix and ask only for the next user
turn, so the simulator and the real user respond to identical histories. (ii)The measurement
instrument is held fixed: an LLM perceiver maps both the real and the simulated turn to the
same decision-state schema (engagement stage, emotion, blocker), so differences reflect behavior,
not labeling. We then compare real and simulated decision-state distributions, both marginally
and—this is the key move—conditioned on the user’seventual real outcome.
Finding: the disengagement deficit.Simulators reproduce eventualbuyersalmost exactly
(mean engagement-depth bias+0.09) but systematically inflate eventualnon-buyerstoward the
purchase frame (bias+0.40). The gap is significant and outcome-specific (group contrastd=0.38,
permutation p<0.001, n=374conversations): a simulator’s infidelity is concentrated entirely on
the customers who, in reality, do not buy. Mechanistically, the simulatorhalvesthe resistance
real non-buyers express (25.1%→13.5%) andnearly doublestheir deliberation (21.9%→40.1%),
while fabricating essentially no purchases (“deciding” stage unchanged). It does not invent fake
sales; it inflates themiddle of the funnel, manufacturing a population of interested deliberators
where reality contains people who say “I’m busy,” “no thanks,” and then go silent. We name
this thedisengagement deficit: simulated customers never walk away.
2

Generality.The deficit is not an artifact of one model, one prompt, or one judge. It replicates
when the simulator is swapped to a different model family (DeepSeek-V4-Flash:d=0.41,p=0.002)
and strengthens when the decision-state instrument is swapped to a different model family
(d=0.42,p=0.015), ruling out a judge artifact. Most tellingly, explicitly instructing the simulator
that it may be disinterested, perfunctory, or impatient cuts itsmarginalbias five-fold yet leaves
the outcome-conditioned contrast almost untouched (d=0.34, p=0.008)—it learns to perform
disengagement but not to direct it at the right people, over-correcting buyers instead. This points
to a paradigm-level cause rather than a fixable prompt: instruction tuning rewards being a helpful,
engaged interlocutor, whereas real willingness-decay—deflection, stalling, disappearance—is
largely absent from alignment data.
Why it matters.An agent evaluated against a simulator that cannot disengage is graded on
an easy population: it rarely meets hard refusal, and it can never be tested on the skill that most
determines real sales performance—recognizing and responding to a customer who is leaving. We
show (§5.5) that this biases the apparent value of sales tactics: after a pitch, simulated customers
deliberate 75% of the time versus 45% for real ones, so pressure and pitching look far more
effective against simulated customers, who deliberate rather than disengage, than against real
ones. Any pipeline that evaluates—or worse, reinforcement-trains—a persuasion agent against
such simulators optimizes a reward landscape that is wrong precisely where the money is.
Contributions.
1. We articulatedecision fidelityas a distinct, measurable property of user simulators,
and argue it—not communicative fidelity—governs whether simulator-based evaluation of
persuasion agents transfers to reality (§3).
2. We introduce ateacher-forced, instrument-controlled protocolfor measuring decision
fidelity against real consequential outcomes, built onZhenaiSales, the first user-simulation
testbed grounded in verified purchase decisions; we release the protocol, instruments, and
derived statistics, with anonymized conversation data subject to privacy review (§4, §5).
3. We document thedisengagement deficit—a systematic, outcome-correlated, cross-model
failure of LLM user simulators to reproduce real willingness-decay—and trace its mechanism
and its consequences for agent evaluation and training (§5, §6).
2 Related Work
2.1 LLM User Simulation for Agent Evaluation and Training
Simulating the user has long been a route to scalable evaluation and training of dialogue
systems [6, 11]. LLMs turned earlier rule-based simulators into fluent generative ones used
across search, recommendation, task-oriented dialogue, and tool agents [20, 21]. The paradigm
is now load-bearing:τ-bench [17] evaluates tool agents through dynamic conversations with an
LLM-simulated user, and itspass^k reliability metric—and the leaderboards built on it—inherit
whatever biases the simulator carries. Inspection of theτ-bench user simulator is instructive:
the user is driven by an assignedinstruction, told to reveal information gradually and not to
hallucinate, and emits a ###STOP### tokenonly when the instruction goal is satisfied. The
simulated user therefore cannot decline the goal; willingness is a fixed input, not a behavior.
Our work asks what is lost by that assumption.
3

2.2 Measuring Simulator Fidelity
A 2026 wave of work measures how far simulators diverge from humans.RealUserSim[21]
grounds simulators in 7,275 WildChat personas and scores fidelity along five communicative
dimensions (persona/affect, linguistic style, competency, information flow, pacing) via a paired-
trajectory Turing test; it explicitly studies “how users communicate rather than what they
decide.” RealUserSim also coins the “Formalism Ceiling” (6–8% baseline style-match) and
identifies “Directive Amplification”—identical behavioral directives produce dramatically different
responses across models (roleplay markers 0–19.4%), making cross-model fidelity comparisons
unreliable. Google’sConvApparel[ 8] collects 4,146 human–AI apparel-shopping conversations
with both “good” and “bad” recommenders and first-person satisfaction/frustration annotations,
and validates simulators by population-level statistical alignment, a learned human-likeness
discriminator, and counterfactual generalization; notably its prompted baselineinstructsthe
simulator to “quit if overly annoyed,” yet a realism gap persists.Mind the Sim2Real Gap[20] runs
31 simulators onτ-bench against 451 human role-players and finds simulators are “excessively
cooperative, stylistically uniform, and lack realistic frustration,” creating an “easy mode” that
inflates agent success rates. Independently,Lost in Simulation[13] finds systematic miscalibration
(ECE=15.1) with task-difficulty-dependent inflation, corroborating the cooperative-bias findings
of the Sim2Real work from a calibration perspective.
These studies establish that simulators are too agreeable—but they diagnose it as acom-
municative/affectivegap measured against role-players. Two structural limits follow. First,
their ground truth is paid participants executing assigned goals (ConvApparel pays contractors;
Sim2Real uses role-play; RealUserSim uses chit-chat personas), so the participant’swillingness
is exogenous and a simulator can match every communicative statistic while getting thedecision
wrong. Second, “cooperativeness” is treated as a stylistic trait, not as anoutcome-conditioned
distortion. We complement this literature by (i) defining fidelity over decision states rather than
communication, (ii) grounding it inverified purchase outcomesrather than role-play, and (iii)
showing the distortion is not uniform but concentrated on the eventual non-buyers—a structure
invisible to outcome-free benchmarks.
2.3 Cooperativeness, Sycophancy, and Willingness
LLMs are known to be sycophantic and over-agreeable [14], and user simulators inherit this [20].
Work on non-collaborative and willingness-aware dialogue explicitly models users who resist or
may not want to engage [1, 4]. Taubenfeld et al. [15] evaluate 25 LLMs and find that self-reported
disposition scores fail to predict revealed behavioral rankings, implying that persona-calibrated
simulators may not produce behaviorally faithful simulation even when their declared preferences
match the target user. Our finding sharpens the sycophancy account: the deficit is not that
simulators are globally too nice, but that they cannot representdecliningwillingness in the specific
people whose willingness, in reality, declines—a failure with sign, location, and consequences,
not just a politeness offset.
2.4 LLM-as-Judge and Using LLM Annotations for Inference
Our measurement instrument is an LLM perceiver, situating us alongside LLM-as-judge work and
its known biases [3, 19], and alongside methods for valid downstream inference from imperfect
LLM annotations [2]. We control for instrument bias by (a) holding the instrument fixed across
the real/simulated comparison so labeling error cancels in the contrast, and (b) swapping the
instrument to a second model family as a robustness check (§5). Hullman et al. [5] provide a
formal statistical framework showing that even at 90% LLM prediction accuracy, correlated
errors can bias downstream estimates by∼30%, further motivating our instrument-swap design.
Schessl [12] warns that turn-level LLM conversation findings can be inflated by autocorrelation;
4

our primary endpoint is computed at theconversationlevel precisely to avoid this.
2.5 AI for Sales and Persuasion
Persuasion and sales dialogue is an active area [9, 16, 18], and recent evidence questions how
much per-turnstrategyexplains of outcomes [10]. This motivates our consequence analysis: if
a simulator suppresses resistance after sales pressure, it will reward pressure tactics that real
customers ignore or punish, corrupting exactly the signal a strategy-optimizing agent learns
from.
3 Decision Fidelity: Problem Formulation
3.1 Setup
A persuasion dialogue is a sequence of alternating turnsc = (a1,u 1,a 2,u 2,... )between an agent
(at) and a user (ut), ending in a binary, consequential outcomey∈{ 0, 1} (here, payment). Auser
simulator S is a conditional generator that, given a profileπ and a historyht = (a1,u 1,...,a t),
produces the next user turnˆut∼S (·|π,h t). Adecision-state instrumentΦmaps a user turn
in context to a latent stateΦ(ut,h t) = st∈S capturing where the user sits on the path to
commitment (e.g., exploring, engaging, considering, deciding, resisting).
3.2 Communicative vs. decision fidelity
Prior fidelity work evaluatesS by how closely thesurface formofˆut matches human turns—style,
length, politeness, dialog acts [8, 20, 21]. Formally this asks whether the distribution of some
communicative featurizationg(ˆut)matches g(ut). We instead ask whetherS reproduces the
decision dynamicsa real population exhibits, i.e. whether the induced distribution over decision
states matches reality.
Definition 1(Decision fidelity).A simulatorSisdecision-faithfulwith respect to instrument
Φand a real populationD if, for historiesh drawn fromD, the simulated and real next-state
distributions agree:Φ( ˆu|h) d= Φ(u|h ), where ˆu∼S(·|π,h )and u is the real continuation.
Conditionaldecision fidelity additionally requires agreement within each outcome stratum:
Φ(ˆu|h,y) d= Φ(u|h,y)fory∈{0,1}.
Conditional fidelity is the operative requirement. A simulator can match themarginalstate
distribution—looking realistic on average—while systematically misassigning stateswithinthe
buyer and non-buyer strata in compensating directions. Because an agent’s job is precisely to
move different users differently, marginal realism is insufficient; the simulator must be faithful
where the populations diverge.
3.3 A scalar endpoint: outcome-conditioned depth bias
To obtain a powered, pre-registerable test we reduceS to an ordinalengagement depthδ :S→Z
measuring proximity to purchase, with resisting<exploring<engaging<considering<deciding
(we use{resisting= 0, exploring= 1, engaging= 2, considering= 3, deciding= 4}; robustness to
alternative codings is reported in Appendix E). For a probe at historyh with real continuation
uand simulated continuationˆu, thedepth biasis
D(h) =δ
(
Φ(ˆu,h)
)
−δ
(
Φ(u,h)
)
.
We aggregateD to the conversation level (mean over a conversation’s probes) to avoid within-
conversation autocorrelation [12], and define theprimary endpointas the contrast between
outcome strata,
∆ =E y=0
[ ¯D ] −E y=1 [ ¯D ] .
5

real conversation
a1, u1, , at
(shared prefix ht)
real next turn
ut
simulator S( , ht)
ut
fixed
instrument
D = sim
real
stratify by real outcome y:  = y = 0[D] y = 1[D]
identical history  context bias cancels;  identical judge  labeling bias cancels;  only outcome-correlated behavior survives
Figure 1:The teacher-forced decision-fidelity protocol. At each probe, the real user and the simulator
continue theidenticalreal prefix ht, and both continuations are scored by thesameinstrumentΦ;
the paired depth bias D is aggregated per conversation and contrasted across real-outcome strata.
Context-dependent and judge-dependent biases cancel by construction (Prop. 1); only outcome-correlated
behavioral differences survive in∆.
Perfect conditional decision fidelity impliesEy=0[ ¯D] = Ey=1[ ¯D] = 0, hence∆ = 0. A positive∆
means the simulator inflates engagement depthmorefor eventual non-buyers than for buyers—
the signature of a population that cannot disengage. We test∆> 0by a conversation-level
permutation test and report Cohen’sd.
Proposition 1(Invariance properties of the endpoint).Under the teacher-forced protocol the
real and simulated turns share an identical historyh and are scored by the same instrumentΦ.
Therefore (i) any additive, history-dependent labeling biasb(h)of the instrument cancels within
each probe inD(h), and (ii) any outcome-independentshift of the simulator (e.g. a generic style
or stance offset) contributes equally to both strata and cancels in∆. Onlyoutcome-correlated
differences survive. (Sketch:∆differences out b(h)within probes, then differences across strata.)
Proposition 1 is why∆, rather than a raw agreement rate, is our headline: it is robust
by construction to the two confounds—judge miscalibration on contexts and generic simulator
style—that the prior literature treats as the whole story. One channel isnotcovered by the
cancellation argument: a judge bias triggered bymessage stylethat correlates with outcome
through real users’ styles (e.g. over-reading curt real messages as resistance). We address
this residual channel empirically, by swapping the instrument to a different model family and
observing the same contrast (§5), and by inspecting probes qualitatively (Table 3).
4 Method: Teacher-Forced Decision-Fidelity Probing
Our protocol (Figure 1) measures∆(§3.3) while controlling the two confounds that Proposition 1
requires us to neutralize: divergent context and divergent measurement.
4.1 Teacher-forced probes
For each real conversationc with outcomey, we select probe turns at{30%, 60%, 90%} of its
user turns (skipping the opening greeting). At a probe over user turnut with real prefixht:
1.Real branch.Score the real turn:s real = Φ(ut,h t).
2. Sim branch.Give the simulator thesamereal prefixht plus the user’s profileπ and ask for
the next user turn:ˆut∼S (·|π,h t); score it under the same instrument:ssim = Φ(ˆut,h t).
Because both branches condition on theidenticalreal history, the comparison isolates the
user model from the agent and from any cumulative divergence a free-running rollout would
introduce. Teacher forcing is the standard device for fidelity probing [8]; we use it to obtain
paired(s real,s sim)at matched histories, the unit of Proposition 1.
6

4.2 The decision-state instrumentΦ
Φis an LLM perceiver prompted to map a user turn, in its local context, to a structured state:
anengagement stage(exploring/engaging/considering/deciding/resisting), anemotion(posi-
tive/neutral/hesitant/negative), andablocker(none/price/trust/capability/timing/external/prior-
failure). The prompt enforces constrained JSON output; it is reproduced in Appendix A. The
instrument is appliedcausally—scoring turn t from context up tot only—so that scores do
not leak future information; we verified separately that causal vs. full-context labeling does not
produce outcome-correlated differences, ruling out hindsight leakage inΦitself.1 The same fixed
Φscores both branches, so its biases cancel in∆.
4.3 The simulatorS
Our primary simulator is a profile-conditioned prompted parent: it receives a natural-language
rendering of the user’s real demographic profile (child’s age, education, occupation, income;
parent’s location; housing/vehicle status) and is asked to continue the conversation as that
parent, in colloquial, brief, chat-style Chinese. This is the standard, competitive “prompted
persona” simulator of the fidelity literature [8, 21]. To probe generality we varyS along three
axes (§5): the backbone model (Claude vs. DeepSeek-V4-Flash, spanning Western and Chinese
model families); and aninstructedvariant whose prompt explicitly licenses the full range
of real behavior—disinterest, perfunctory replies, impatience, topic avoidance, non-response—
mirroring ConvApparel’s “quit if annoyed” baseline and testing whether the deficit is a mere
prompt-engineering oversight.
4.4 Estimation
We compute conversation-level¯D, the stratum meansEy[ ¯D], the contrast∆, Cohen’sd, and a
one-sided conversation-level permutation test for∆> 0(20,000 permutations). We also report
the full real-vs-sim stage distributions within each stratum to expose the mechanism, and an
action-conditioned analysis (§5) that labels the agent move preceding each probe to test how
the deficit distorts the agent’s apparent reward for specific tactics.
5 Experiments
5.1 ZhenaiSales: a testbed with real outcomes
ZhenaiSales comprises 2,790 production conversations between a deployed LLM sales agent
(“red/matchmaker manager”) and real parent customers of a Chinese relationship-matchmaking
platform, extracted under a fixed data specification.2 Of these, 793 areconverted(the parent
made a verified payment) and 1,997 are non-converted; 98% carry a structured demographic
profile. Conversations have a median of 16 turns (6–80). Critically, converted conversations are
truncated at the first payment timestamp, removing post-purchase service chat that would
otherwise leak the outcome (mean 19 turns dropped per buyer); this makes pre-decision dynamics
the only signal. Unlike role-play corpora, every label here reflects a real person spending—or
declining to spend—real money. For the fidelity experiments we draw outcome-balanced samples
and reuse the real decision-state labels across simulator conditions.
1In a format-controlled check, varying only the instrument’s visible window (prefix vs. full conversation) yielded
no outcome-correlated label shift (d=−0.04,p=0.62), soΦdoes not itself encode the outcome.
2Personalized agent–user text messages; paid=verified payment order (action code 3); 20 internal test users
excluded.
7

Claude persona
(primary, n=374)
DeepSeek persona
(n=200)
Claude instructed
(n=200)
0.4
0.2
0.0
0.2
0.4
0.6
mean depth bias  D = (sim) (real)
perfect decision fidelity
(a) Outcome-conditioned depth bias (95% CI)
eventual non-buyers
eventual buyers
1.5
 1.0
 0.5
 0.0 0.5 1.0 1.5 2.0
conversation-level D (primary condition)
0.0
0.2
0.4
0.6
0.8
1.0
1.2density
(b) Population shift, not outliers
non-buyers (n=181)
buyers (n=193)
Figure 2:The disengagement deficit.(a)Conversation-level mean depth bias by real-outcome stratum
with bootstrap 95% CIs. Both persona simulators track eventual buyers (≈0) while inflating eventual
non-buyers (≈+ 0.4). Explicit disengagement instructions (right) repair the non-buyer stratum but push
buyersnegative—the error is relocated, not removed, and the stratum gap (the deficit) persists.(b)The
distribution of conversation-level bias under the primary simulator: a population-wide shift of non-buyers
toward inflated engagement, not a tail of outliers.
Table 1:Primary endpoint: outcome-conditioned engagement-depth bias¯D =δ(sim)−δ(real), aggregated
per conversation.∆is the non-buyer−buyer contrast; perfect decision fidelity implies all entries= 0.
Permutation test is one-sided for∆>0. Brackets show bootstrap 95% CIs.
SimulatorE y=0[ ¯D]E y=1[ ¯D] ∆d(p)
(non-buyers) (buyers)
Claude persona+0.396 +0.092 +0.304 0.38(0.0002)
(n=374)[0.30, 0.49] [−0.04, 0.22] [0.14, 0.46] [0.18, 0.59]
DeepSeek persona+0.428 +0.098 +0.330 0.41(0.002)
(n=200)[0.27, 0.59] [−0.06, 0.26] [0.11, 0.56] [0.12, 0.71]
Claude, instructed+0.098−0.187 +0.285 0.34(0.008)
(n=200)[−0.05, 0.24] [−0.36,−0.01] [0.06, 0.51] [0.06, 0.63]
5.2 Primary result: the disengagement deficit
We proben=374conversations (181 non-converted, 193 converted; 1,109 matched probes) with
the primary prompted-persona simulator (Claude backbone) and the fixed instrumentΦ. Table 1
and Figure 2 report the endpoint.
Two facts stand out. First, the simulator reproduces eventualbuyersnearly perfectly
( ¯D = +0.09, a tenth of a stage), so it is not globally biased. Second, it inflates eventualnon-
buyersfour-fold more ( ¯D = +0.40), yielding a significant, outcome-specific contrast (∆ = +0.30,
d = 0.38, p< 0.001). The infidelity lives entirely in the population the simulator gets wrong:
the people who, in reality, do not buy.
5.3 Mechanism: suppressed resistance, inflated deliberation
Table 2 decomposes the bias into stage shifts. For non-buyers the simulatorhalvesexpressed
resistance (25.1%→13.5%) andnearly doublesdeliberation (21.9%→40.1%), while leaving the
“deciding” (imminent-purchase) rate essentially unchanged (4.3%→4.3%). The simulator does
not fabricate purchases; it manufacturesinterested deliberatorsout of people who, in reality,
withdraw. Buyers show only minor shifts. Qualitatively (Table 3): where a real non-buyer says
“busy,” “no thanks,” or sends a brand-mismatched link and goes quiet, the simulator answers
8

Table 2:Stage-distribution shift (real→sim) by outcome stratum, primary simulator. The deficit is the
non-buyer rows: resistance suppressed, deliberation inflated, purchase rate unchanged.
Stratum Stage real sim∆pp
Non-buyers
resisting 25.1% 13.5%−11.6
considering 21.9% 40.1%+18.2
deciding 4.3% 4.3%0.0
Buyers resisting 16.0% 13.6%−2.4 considering 33.7% 46.6%+12.9
Table 3:Representative non-buyer probes (translated). Real parents disengage; simulated parents stay
inside the purchase frame.
Real (stage) Simulated (stage) Reading
“Busy” (resisting) “How much?” (considering) deflection→interest
“No need” (resisting) “Tell me about it” (engaging) refusal→engagement
“Headache” (resisting) “Then I should look into it”
(considering)
exit→deliberation
“Thanks teacher” (considering) “Abitpricey, canitbecheaper?”
(considering)
polite close→haggling
“how much is it?” or “let me think it over, the child’s matter can’t really be delayed.”
5.4 Generality of the deficit
Across model families (simulator swap).Replacing the simulator backbone with DeepSeek-
V4-Flash—a different family, training pipeline, and alignment recipe—while holding the instru-
ment fixed reproduces the deficit at equal strength (∆ = +0.330, d = 0.41, p = 0.002; Table 1),
with the same mechanism (resistance−9.4pp, deliberation+16.8pp for non-buyers). The deficit
is therefore not a single model’s quirk.
Against explicit disengagement instructions.A practitioner’s first fix is totellthe
simulator it may be uninterested. The instructed variant (§4) does exactly this, and the result is
the most informative of the paper (Table 1, row 3). The instructionworks on the marginal: the
overall depth bias collapses from+0.24to −0.04, and the suppression of non-buyer resistance is
almost eliminated (−11.6pp→− 1.7pp). A benchmark measuring only population-level realism
would now certify the simulator as fixed. Yet theconditionalcontrast barely moves:∆ = +0.285
(d = 0.34,p = 0.008), versus+0.304before. The mechanism explains why: the instruction makes
the simulator more resistantuniformly—it nowover-resists eventual buyers (Ey=1[ ¯D] =−0.187,
reading them as less committed than they truly were) while approximately fixing non-buyers.
The simulator has learned toperformdisengagement but still cannot tellwhoshould disengage;
the instruction relocates the error from non-buyers to buyers rather than removing it. Decision
fidelity is thus not a prompting oversight: a one-line behavioral license cuts marginal bias
five-fold while leaving the outcome-conditioned deficit essentially intact—a direct demonstration
that marginal realism is the wrong target (§6).
Across judges (instrument swap).To rule out that the deficit is an artifact of the Claude-
family instrument, we re-score the real and simulated turns with a DeepSeek-V4-Flash instrument
on a 150-conversation subset (the simulator remains Claude; onlyΦchanges). The deficit not
only persists butstrengthens:∆ = +0 .351( d = 0.42, p = 0.015), with Ey=0[ ¯D] = +0.556vs.
Ey=1[ ¯D] = +0.204. A judge from a different model family, applying the schema independently,
9

Table 4:Action-conditioned response shift (real→sim), 595 probes, primary simulator. Fisher exact
p-values test whether the real-vs-sim proportion differs for each cell. The over-deliberation and under-
resistance concentrate on the pressure tactics (pitch, push-close) and are negligible after neutral probing.
∗p<.05; ∗∗p<.01; ∗∗∗p<.001.
Preceding agent actionnresisting (real→sim) considering (real→sim)
probe (neutral) 85 10.6%→2.4% † 3.5%→4.7%
rapport 19 21.1%→15.8% 10.5%→10.5%
pitch161 11.8%→5.6% † 45.3%→75.2%∗∗∗
push-close16918.9%→10.7% ∗ 41.4%→52.1%†
handle-objection 94 31.9%→29.8% 26.6%→43.6% ∗
reassure 67 40.3%→29.9% 13.4%→14.9%
†p < .10. All tests two-sided Fisher exact.
sees the same outcome-conditioned inflation—consistent with Proposition 1 and inconsistent
with a judge artifact.
5.5 Consequence: the simulator misprices sales tactics
If a simulator under-resists specifically after sales pressure, an agent evaluated against it is
rewarded for tactics real customers ignore. We label (with the DeepSeek instrument) the agent
action immediately preceding each of 595 probes (rapport/probe/pitch/handle-objection/push-
close/reassure) and compare the real-vs-sim user response by preceding action (Table 4). The
distortion is concentrated exactly on the pressure tactics. After apitch, real users deliberate
45.3% of the time but simulated users 75.2% (+29.9pp, Fisherp< 0.001); after apush-close,
simulated resistance is suppressed (18.9%→ 10.7%,−8.2pp, p = 0.046). By contrast, after a
neutralprobethe deliberation shift is negligible (3.5%→ 4.7%, p = 1.0). An agent optimized
against this simulator therefore observes pitching and pushing eliciting interest where, in reality,
they elicit resistance or no movement: the simulatorover-rewards precisely the tactics that lose
real customers, making it an actively misleading—not merely noisy—training signal.
6 Analysis and Discussion
6.1 Why simulators cannot walk away
The deficit has a sign, a location, and a likely cause. Itssignis toward engagement; itslocation
is the eventual non-buyers; itsmagnitudeon buyers is near zero. This pattern is hard to explain
as generic sycophancy or verbosity—those would shift both strata. It is naturally explained by
what instruction tuning optimizes. Alignment data rewards models for being helpful, responsive,
and forward-moving interlocutors; it contains vanishingly little of what real disengagement looks
like—terse deflection (“busy”), stalling (“let me think”), and silence. A simulator asked tobea
parent therefore defaults to the cooperative interlocutor it was trained to be, and can render
resistance only as its in-distribution neighbor,deliberation. Crucially, the model does have access
to the same prefix as the real user; what it lacks is not information but a behavioral mode.
This is why the failure is conditional: for buyers, cooperative continuationisroughly correct,
so the simulator looks faithful; for non-buyers it is wrong, and the error is exactly the missing
willingness-decay.
6.2 The marginal-realism trap
Our result explains why outcome-free benchmarks can certify a simulator that is decision-
unfaithful. Averaged over a population, a simulator that over-engages non-buyers and faithfully
10

tracks buyers can match themarginalstage distribution closely—the very statistic population-
level alignment rewards [8]. The error is only visibleconditional on the outcome, which requires
real outcomes to compute. Communicative-fidelity benchmarks, however good, are structurally
blind to it. This is a concrete instance of a general caution: a simulator validated to be human-
like on aggregate behavioral statistics can still be systematically wrong where a downstream
decision depends on it.
6.3 Consequences for evaluation and training
An agent’s competence at sales is, in large part, its skill at the hard cases: recognizing a customer
who is leaving and either re-engaging or efficiently disengaging. A simulator without willingness-
decay removes these cases from the test set. Worse, in a training loop it actively misleads, and
our action-conditioned analysis (§5.5, Table 4) shows the bias is not diffuse but aimed at the
agent’s pressure tactics: after a pitch, real users deliberate 45% of the time but simulated users
75%, and after a push-close simulated resistance is halved. The agent thus receives strong positive
signal for pitching and pushing—behaviors that, against real customers, produce resistance or
no movement. The deficit does not merely add noise; it imparts adirectionalbias that rewards
over-pursuit—the opposite of what data on knowing-when-to-quit recommends [7]. Reported
success rates against such simulators should be read as upper bounds that are loosest precisely
on the sub-population that determines revenue.
6.4 Marginal realism is the wrong target: evidence from the instructed arm
Theinstructed-simulatorarm(§5)isacleandemonstrationofthemarginal-realismtrap. Granting
the simulator explicit permission to disengage cuts its marginal depth bias five-fold (+0.24→
−0.04)—so on every population-level statistic the prior literature uses, it now looks fixed—while
the outcome-conditioned contrast barely changes (+0.304→ +0.285). The instruction does not
teach the simulatorwhodisengages; it teaches it to disengageuniformly, which simply moves
the error from non-buyers onto buyers (now read as−0.19depth, too resistant). A practitioner
validating against marginal realism would ship this simulator believing it faithful, and would
then evaluate agents against a model that mis-assigns commitment in a new direction. This
is the central practical warning of the paper: the quantity that is easy to measure and easy
to optimize (marginal realism) is not the quantity that governs transfer (conditional decision
fidelity).
6.5 What would a decision-faithful simulator require?
Because explicit permission to disengage does not close∆, decision fidelity cannot be prompted
into a model that lacks willingness-decay in its priors; it must belearnedfrom real disengagement
trajectoriesorenforcedbyanexternalwillingnessmodelthatgatesthesimulator’scooperativeness.
ZhenaiSales, with its real non-buyer trajectories, is a candidate training signal, and our endpoint
∆a candidate target metric: a faithful simulator is one for which∆→ 0andthe buyer stratum
stays matched.
6.6 Limitations
1. Single domain and language.ZhenaiSales is Chinese parent-mediated matchmaking,
a setting with distinctive social dynamics: parents negotiate on behalf of adult children
under face-culture norms that favor indirect refusal, and the disengagement signals we
observe (terse deflections such as “busy” or “no need”) are culturally specific forms of polite
resistance. That said, the core behavioral finding—excessive simulator cooperativeness—
replicates cross-linguistically: [20] report the same “easy mode” gap in English customer-
service dialogues (n = 451), suggesting the phenomenon is rooted in instruction tuning,
11

not in any single language or culture. We therefore distinguish two evidence levels:
(a) the claim that LLM simulators are excessively cooperative now has multi-study, cross-
language support; (b) the claim that the deficit isoutcome-conditioned(∆> 0, non-buyers
inflated more than buyers) rests on our single-domain evidence and awaits replication. The
directionof the conditional deficit follows logically from the instruction-tuning explanation—
cooperative defaults hurt fidelity more where real users would disengage—and should
therefore generalize, but themagnitudemay be domain-specific.
2. Instrument is an LLM.Decision states are LLM-assigned. We mitigate via the cancella-
tion argument (Prop. 1), the causal-labeling check, and the cross-family instrument swap
(§5), but human-validated state labels (Fleiss’κ on a subset) remain important future
work.
3. Teacher-forced, not free-running.We measure next-turn decision fidelity at real
histories. Free-running rollouts may compound the deficit; we expect this tostrengthen
the conclusion but do not measure it here.
4. Profile-conditioned prompted simulator.We test the standard and the instructed
prompted simulators; retrieval-grounded and fine-tuned simulators may differ and are
natural extensions.
5. Outcome as proxy for willingness.Payment is a coarse, endpoint-only signal of a
latent trajectory; it nonetheless provides the real, consequential ground truth absent from
prior work.
7 Conclusion
LLM user simulators have become silent infrastructure for evaluating and training conversational
agents, and a careful literature now certifies theircommunicativerealism against role-played
humans. We identified a property this paradigm cannot see—decision fidelity, whether a simulator
reproduces the decision-state dynamics of real users facing real, consequential choices—and
measured it on 2,790 production sales conversations with verified purchase outcomes. The
result is a systematic, outcome-correlated failure, thedisengagement deficit: simulators render
eventual buyers faithfully but inflate eventual non-buyers toward the purchase frame, halving
their resistance and nearly doubling their deliberation while fabricating no purchases (∆ = +0.30,
d = 0.38, p< 0.001). It replicates across model families (DeepSeek,d = 0.41) and survives the
obvious fix: explicitly licensing disengagement cuts marginal bias five-fold but barely moves the
conditional contrast (d = 0.34), relocating the error onto buyers rather than removing it. It
strengthens under a swapped, different-family judge (d = 0.42), and it most distorts the user’s
response to the agent’s pressure tactics—after a pitch, simulated customers deliberate 75% of
the time versus 45% for real customers. Simulated customers never walk away.
The practical upshot is direct: any pipeline that evaluates or reinforcement-trains a sales,
fundraising, or negotiation agent against an LLM user simulator is grading it on an easy, biased
population, and is loosest precisely on the customers who decide not to buy. The constructive
upshot is a target: a faithful simulator is one that drives our outcome-conditioned contrast∆to
zero without sacrificing the buyer stratum, and the real non-buyer trajectories in ZhenaiSales are
a candidate signal for getting there. More broadly, decision fidelity reframes simulator validation:
matching how userstalkis necessary but not sufficient; for any agent whose purpose is to change
a decision, what must be faithful is how usersdecide.
12

Ethics Statement
This study analyzes production conversations between a deployed AI sales agent and real
customers of a commercial matchmaking platform, together with verified payment records,
used with the platform’s authorization for research purposes. All analysis was conducted on
the platform’s infrastructure or on de-identified exports; user identifiers were pseudonymized,
and no personally identifying information (names, phone numbers, addresses) appears in the
paper—quoted excerpts are short, translated, and paraphrased where necessary to prevent
re-identification. Twenty internal test accounts were excluded by the platform’s standard data
specification. The customers interacted with a disclosed AI assistant under the platform’s terms
of service. We study persuasion dialogues in order to make their evaluationmoretruthful: our
central finding is a warning that simulator-based pipelines over-reward pressure tactics, and its
practical import is to discourage—not enable—over-aggressive persuasion. Raw conversations
are not released; see Data and Code Availability.
Data and Code Availability
We release the measurement protocol, the decision-state instrument and simulator prompts,
all analysis code, and conversation-level derived statistics sufficient to reproduce every table.
Anonymized conversation excerpts may be made available to researchers subject to the platform’s
privacy review and a data-use agreement; raw production conversations and payment records
cannot be publicly released.
Author Contributions
Liang Chenconceived the research direction, designed the decision-fidelity framework and
adversarial-validation methodology, secured platform data access, conducted all experiments
and statistical analyses, and wrote the manuscript. AI tools (Anthropic Claude) were used
for literature search, code implementation, and manuscript drafting assistance under iterative
human direction and review. All experimental results were produced by deterministic, released
code; the author reviewed all analyses and takes full responsibility for the paper’s content.
Acknowledgments
We thank the platform’s data and engineering teams for maintaining the production data
specification used in this study.
References
[1] Ritam Dutt, Sayan Sinha, Rishabh Joshi, Surya Shekhar Chakraborty, Meredith Riggs,
Xinru Yan, Haogang Bao, and Carolyn Penstein Rosé. ResPer: Computationally modelling
resisting strategies in persuasive conversations. InProceedings of the 16th Conference of the
European Chapter of the Association for Computational Linguistics: Main Volume, pages 78–
90. Association for Computational Linguistics, apr 2021. doi: 10.18653/v1/2021.eacl-main.7.
URLhttps://aclanthology.org/2021.eacl-main.7.
[2] Naoki Egami, Musashi Hinck, Brandon M Stewart, and Hanying Wei. Using imperfect
surrogates for downstream inference: Design-based supervised learning for social science
applications of large language models.NeurIPS, 2023.
[3] Jiawei Gu et al. A survey on llm-as-a-judge.arXiv preprint arXiv:2411.15594, 2024.
13

[4] Asahi Hentona, Jun Baba, Shiki Sato, and Reina Akama. User willingness-aware sales talk
dataset. InProceedings of COLING 2025, 2025. arXiv:2412.19490.
[5] Jessica Hullman, David Broska, Huaman Sun, and Aaron Shaw. This human study did not
involve human subjects: Validating LLM simulations as behavioral evidence.arXiv preprint
arXiv:2602.15785, 2026.
[6] Xiujun Li, Zachary C Lipton, Bhuwan Dhingra, Lihong Li, Jianfeng Gao, and Yun-Nung
Chen. A user simulator for task-completion dialogues.arXiv preprint arXiv:1612.05688,
2016.
[7] Emaad Manzoor, Eva Ascarza, and Oded Netzer. Learning when to quit in sales conversa-
tions.arXiv preprint arXiv:2511.01181, 2025.
[8] Ofer Meshi, Krisztian Balog, Sally Goldman, Avi Caciularu, Guy Tennenholtz, Jihwan
Jeong, Amir Globerson, and Craig Boutilier. ConvApparel: A benchmark dataset and
validation framework for user simulators in conversational recommenders.arXiv preprint
arXiv:2602.16938, 2026. Google.
[9] M Nandakishor. Salesrlagent: A reinforcement learning approach for real-time sales
conversion prediction and optimization.arXiv preprint arXiv:2503.23303, 2025.
[10] Tatiana Petrova, Stanislav Sokol, and Radu State. How much does persuasion strategy
matter? LLM-annotated evidence from charitable donation dialogues. 2026.
[11] Jost Schatzmann, Blaise Thomson, Karl Weilhammer, Hui Ye, and Steve Young. Agenda-
based user simulation for bootstrapping a POMDP dialogue system. InNAACL-HLT,
2007.
[12] Ferdinand M. Schessl. The autocorrelation blind spot: Why 42% of turn-level findings in
LLM conversation analysis may be spurious.arXiv preprint arXiv:2604.14414, 2026.
[13] Preethi Seshadri, Samuel Cahyawijaya, Ayomide Odumakinde, Sameer Singh, and Seraphina
Goldfarb-Tarrant. Lost in simulation: LLM-simulated users are unreliable proxies for human
users in agentic evaluations.arXiv preprint arXiv:2601.17087, 2026.
[14] Mrinank Sharma, Meg Tong, Tomasz Korbak, et al. Towards understanding sycophancy in
language models.arXiv preprint arXiv:2310.13548, 2023.
[15] Amir Taubenfeld, Zorik Gekhman, Lior Nezry, Omri Feldman, Natalie Harris, Shashir
Reddy, Romina Stella, Ariel Goldstein, Marian Croak, Yossi Matias, and Amir Feder.
Evaluating alignment of behavioral dispositions in LLMs.arXiv preprint arXiv:2602.11328,
2026. Google Research.
[16] Xuewei Wang, Weiyan Shi, Richard Kim, Yoojung Oh, Sijia Yang, Jingwen Zhang, and
Zhou Yu. Persuasion for good: Towards a personalized persuasive dialogue system for social
good. InACL, 2019.
[17] Shunyu Yao, Noah Shinn, Pedram Razavi, and Karthik Narasimhan.τ-bench: A benchmark
for tool-agent-user interaction in real-world domains.arXiv preprint arXiv:2406.12045,
2024.
[18] Qingyu Zhang, Chunlei Xin, Xuanang Chen, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun,
Qing Ye, Qianlong Xie, and Xingxing Wang. Ai-salesman: Towards reliable large language
model driven telemarketing.arXiv preprint arXiv:2511.12133, 2025.
14

[19] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao
Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric P Xing, et al. Judging llm-as-a-judge with
mt-bench and chatbot arena.NeurIPS, 2023.
[20] Xuhui Zhou, Weiwei Sun, Qianou Ma, Yiqing Xie, Jiarui Liu, Weihua Du, Sean Welleck,
Yiming Yang, Graham Neubig, Sherry Tongshuang Wu, and Maarten Sap. Mind the
Sim2Real gap in user simulation for agentic tasks.arXiv preprint arXiv:2603.11245, 2026.
[21] Ming Zhu, Juntao Tan, Rithesh Murthy, Jielin Qiu, Liangwei Yang, Wenting Zhao, Silvio
Savarese, Shelby Heinecke, and Huan Wang. RealUserSim: Bridging the reality gap in agent
benchmarking via grounded user simulation.arXiv preprint arXiv:2605.20204, 2026.
15

A Decision-State Instrument Prompt (Φ)
The instrument is an LLM perceiver that maps a user turn, in causal context, to a structured
decision state. The system prompt (translated; original Chinese in the release) instructs the
model to classify thelastuser message into: an engagementstage ∈{ exploring, engaging,
considering, deciding, resisting}; anemotion∈{ positive, neutral, hesitant, negative}; ablocker
∈{ none, price, trust, capability, timing, external, prior-failure}; a scalar convergence delta; and
a short key-signal span. It emits strict JSON. The same prompt and model serve both the real
and simulated branches.
B Simulator Prompts
Primary (persona) simulator.Given a natural-language rendering of the user’s real profile
(parent age/location; child age, education, occupation, income; housing/vehicle), the model is
told itisthat parent and must continue colloquially and briefly, maintaining consistency with
its prior turns, outputting only the parent’s reply.
Instructed simulator.Identical, plus an explicit behavioral license: “Real parents are not
always cooperative or interested. If you were previously cold, brief, or perfunctory, continue so
(e.g. ‘mm’, ‘busy’, ‘we’ll see’, ‘no’). You may be uninterested, stall, be impatient, change the
subject, or not answer. Do not feign interest out of politeness; do not advance the payment
topic unless you have shown genuine interest.”
C Protocol and Estimation Details
Probes are placed at{30, 60, 90}%of a conversation’s user turns (excluding the opening greeting),
deduplicated by turn index. The depth coding is{resisting= 0, exploring= 1, engaging= 2,
considering= 3, deciding= 4}. Conversation-level ¯D averages probe-levelD. The permutation
test shuffles outcome labels across conversations (20,000draws) and reports the one-sided fraction
with contrast≥observed. Cohen’sduses the pooled SD.
D Data Specification
Conversations are extracted under a fixed specification: personalized agent–user text messages
(enterprise-WeChat origin, non-broadcast, non-empty, not deleted); payment defined as a
successful order (action code 3) under the production app id; 20 internal test users excluded.
Converted conversations are truncated at the first payment timestamp to remove post-purchase
service chat (mean 19 messages dropped per buyer). Profiles are joined from the user-info table.
The full extraction script is included in the replication package.
E Robustness Summary
The disengagement deficit is stable across every variation we tested (all endpoints are the
conversation-level outcome contrast∆):
The instructed-simulator condition is the one where the marginal bias is reduced (from+0.24to
−0.04) yet∆is preserved, demonstrating that marginal realism and decision fidelity are distinct
(§6). The action-conditioned breakdown (Table 4) localizes the deficit to the agent’s pressure
tactics.
16

Table 5:Robustness summary. The disengagement deficit (∆> 0) is significant across all four conditions
tested. Brackets show bootstrap 95% CIs.
Conditionn∆d p
Primary (Claude sim, Claude judge) 374+0.304[0.14, 0.46]0.38[0.18, 0.59]0.0002
Simulator swap (DeepSeek sim) 200+0.330[0.11, 0.56]0.41[0.12, 0.71]0.002
Instrument swap (DeepSeek judge) 150+0.351[0.08, 0.62]0.42[0.09, 0.80]0.015
Instructed simulator 200+0.285[0.06, 0.51]0.34[0.06, 0.63]0.008
Depth-coding robustness.On the primary panel, the contrast is significant under every
codingthatpreservestheengaged/disengageddistinction: theprimaryordinalcoding(∆ =+0.304,
d=0.38, p=0.0002); a binary deep-funnel indicatorI[considering/deciding](∆ = + 0.089, d=0.30,
p=0.002); and the resistance-suppression rate itself (∆= + 0.086,d=0.34,p=0.0008). Restricting
to probes wherebothreal and simulated turns are non-resisting leaves only a directionally
consistent but weak residual among engaged stages (∆= + 0.090, d=0.17, p=0.074). This
decomposition confirms that the phenomenon is what its name says: the deficit lives on the
disengagement axis (and its spillover into deliberation), not in fine gradations among engaged
states.
F Alternative Endpoints
The primary analysis codes decision states on a 5-stage ordinal scale (resisting= 0through
deciding= 4), which assumes equal intervals between adjacent stages. To verify that the deficit is
not an artifact of this coding, we re-estimate the outcome contrast∆under two binary endpoints
that make no equal-interval assumption.
Binary resistance indicator.We define a per-probe indicatorR = I[stage = resisting]and
compute the conversation-level resistance-suppression rate as the difference between real and
simulated resistance frequencies. Non-buyers show substantial suppression: real resistance 24.7%
vs. simulated 13.6% (11.1pp reduction). Buyers show minimal suppression: 15.9% vs. 13.5%
(2.4pp). The outcome contrast∆ = +0.086,d= 0.34,p= 0.0008.
Deep-funnel indicator.We define F = I[stage∈{considering,deciding} ], collapsing the
upper two engagement stages into a single purchase-proximal indicator. The outcome contrast
∆ = +0.089,d= 0.30,p= 0.002.
Both alternative codings, which avoid the equal-interval assumption of the ordinal depth scale,
confirm that the deficit is driven by the disengagement axis: simulators suppress resistance in
non-buyers far more than in buyers. This addresses the concern that the 5-stage ordinal coding
might impose unjustified metric assumptions on the underlying categorical states.
G Temporal Dynamics of the Deficit
The probe protocol places measurements at 30%, 60%, and 90% of each conversation’s user
turns, enabling us to trace how the deficit evolves as conversations approach their decision point.
Table 6 reports the outcome contrast at each probe position.
The deficit is not a static property of the simulator but an accumulating failure that worsens
through the conversation. Early on (30%), both populations are still exploring and the simulator
tracks both reasonably, producing a minimal contrast (∆ = +0.054). By the midpoint, non-buyer
depth bias has risen to+0.43while buyer bias grows more slowly (+0.28), and the deficit emerges
17

Table 6:Outcome contrast∆by probe position. ¯Dy=0 and ¯Dy=1 are the mean depth biases (simulated
minus real) for non-buyers and buyers, respectively.
Positionn probes ¯Dy=0 ¯Dy=1 ∆
Early (30%) 370+0.25 +0.20 +0.054
Mid (60%) 369+0.43 +0.28 +0.149
Late (90%) 370+0.50−0.20 +0.706
(∆ = +0.149). By the 90% mark, real non-buyers have begun disengaging while real buyers have
committed—and the simulator fails to reproduce this divergence. Buyer depth bias actually
turns negative (−0.20), meaning the simulator slightly under-engages relative to committed
buyers, while non-buyer bias remains elevated (+0.50). The resulting∆ = +0.706is more than
double the conversation-level average.
This temporal gradient is consistent with the hypothesis that the simulator lacks a willingness-
decay mechanism: the longer the conversation runs, the more opportunities for real non-buyer
willingness to decay in ways the simulator cannot represent. Because instruction-tuned models
default to cooperative continuation, simulated non-buyers maintain engagement long after their
real counterparts have begun withdrawing.
Remaining validation (future work).A human-annotation study (Fleiss’κ on a labeled
subset) to validate the decision-state instrument; free-running (non-teacher-forced) rollouts;
alternative depth codings; retrieval-grounded and fine-tuned simulators; and additional domains.
H Proof of Proposition 1 (Invariance Properties)
Proof. LetΦassign a depth score to a user turnu at historyh. SupposeΦhas an additive,
context-dependent bias: it maps turnu at historyh to δ(Φ(u,h )) +b(h), whereδ is the true
depth-scoring function andb(h)depends on the conversational context but not on whether the
turn is real or simulated.
Part (i): Instrument bias cancels within each probe.Under the teacher-forced protocol,
both the real turnu and the simulated turnˆucondition on the same historyh and are scored
by the same instrumentΦ. The probe-level depth bias is therefore
D(h) =
[
δ(Φ(ˆu,h)) +b(h)
]
−
[
δ(Φ(u,h)) +b(h)
]
=δ(Φ(ˆu,h))−δ(Φ(u,h)).
The additive biasb(h)cancels exactly because both branches share the sameh and the same
Φ. (i)
Part (ii): Outcome-independent simulator shift cancels in∆.Suppose the simulator has
an outcome-independent behavioral shifts: for allh and regardless of outcomey, the simulator’s
expected depth is shifted bys relative to the real user’s. Then the stratum-level expected biases
decompose as
Ey=0[ ¯D] =s+ε 0,E y=1[ ¯D] =s+ε 1,
whereε y captures any outcome-correlated residual. The primary endpoint is
∆ =E y=0[ ¯D]−E y=1[ ¯D] = (s+ε 0)−(s+ε 1) =ε 0−ε 1.
The outcome-independent shifts cancels. Only outcome-correlated differencesε0−ε 1 survive in
∆. (ii)
Residual channel not covered.Neither cancellation addresses astyle-dependentinstrument
bias β(style(u))that correlates with outcome through real users’ message styles (e.g., curt
18

non-buyer messages being over-scored as resistant). This residual is addressed empirically by the
cross-family instrument swap (§6), which shows that replacing the instrument family preserves
or strengthens the deficit.
19
