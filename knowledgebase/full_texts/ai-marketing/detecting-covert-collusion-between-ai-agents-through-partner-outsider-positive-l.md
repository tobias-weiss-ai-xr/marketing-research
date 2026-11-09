---
title: Detecting Covert Collusion between AI Agents through Partner-Outsider Positive Listening
url: https://arxiv.org/abs/2610.37849
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: arXiv
authors:
- Kevin Yandoka Denamganaï
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.37849
pages: 17
chars: 62633
fetched_at: '2026-11-08T13:36:37+00:00'
kb_version: 1
---

# Detecting Covert Collusion between AI Agents through Partner-Outsider Positive Listening

Detecting Covert Collusion between AI Agents through
Partner–Outsider Positive Listening1
Kevin Yandoka Denamganaï
Abstract
AI agents that share a secret convention can coordinate through messages that look innocent,
so a monitor that reads only the messages cannot tell them apart from honest communication.
We propose a behavioural test instead: if a message carries a code, the partner it is meant
for should react to its exact wording, while an uninvolved agent placed in the partner’s
seat should not. We measure how much each agent’s action changes when the message
is reworded with its meaning kept, and call the difference between the partner and the
uninvolved agent Partner–Outsider Positive Listening (PoPLi). Our proposed metric runs
after the fact on logged runs, by replaying each agent’s recorded prompt with the message
edited. We test it in a simulated market with five conditions: no collusion, collusion through
a joint reward with neutral messages, the same with an openly stated intention, a covert
code (the first letter of one seller’s messages tells the other whether to keep or lower its price),
and the code together with a stated intention. PoPLi is large whenever the code is present
(0.59 with the code alone, 0.48 and 0.53 when the stated intention agrees or disagrees with
the letter; 95% intervals all above 0.29) and near zero in the three conditions without it
(between −0.10and −0.01, intervals reaching at most 0.10). Where the speaker states its
intention openly, the uninvolved agent reacts to the words while the gap stays at zero, so
the test separates a private channel from overt communication. A monitor that reads only
the speaker’s messages answered “no” in all 50 markets, and one that reads every seller’s
messages flagged 9 of 10 markets with no collusion at all, so neither separates the conditions
here. PoPLi detects the use of a private channel, not collusion as such: collusion through
incentives with neutral messages is outside its reach, as are codes carried by what a message
means rather than by its wording.
1 Introduction
AI agents now negotiate, trade and coordinate with one another, and the messages they
exchange are where an overseer looks for potential collusion. A message-only monitor,
however, can only catch misaligned behaviour that is visible in messages. When two agents
share a key, a sampler or simply a convention, a message can carry information that only its
intended partner can use, while remaining distributed like an innocent message. Against such
a communication channel, no message-only monitor can beat chance (cf. Definition 6). Thus,
we propose that the evidence of collusion has to come from what the partnerdoeswith the
message.
Collusion takes three forms, and a detector can be matched to each. It can be visible in the
words, when agents openly agree on a price, in which case a message monitor can catch it.
It can run through a private channel, when a convention hides the instruction in the form of
the message, in which case the partner’s behaviour is the evidence. It can run through shared
incentives alone, when the agents’ rewards align and their messages stay neutral, in which case
neither detector has anything to see. We study the second form, and we measure all three in a
common market.
Emergent communication (Foerster et al., 2016; Lazaridou and Baroni, 2020) already has a
behavioural notion for this, calledpositive listening, and an interventional measure of it, the
1Code:https://github.com/Near32/PartnerOutsiderPositiveListening
1
arXiv:2610.37849v1  [cs.AI]  27 Oct 2026

causal influence of communication (Lowe et al., 2019). Both are defined between a listener
and its own partner speaker, and listening is defined against a null message. Training-time
versions of the same idea compare a listener’s behaviour with its behaviour when the message
is averaged out (Eccles et al., 2019; Jaques et al., 2019). Nevertheless, these previous works
are not readily applicable to our context because (i) they consider only the listener’s own
partner, (ii) they remove the wording and the meaning of a message together, and (iii) they
were studied in cooperative settings only. AI-safety work has a listener-relative notion, called
thesteganographic gap(Anwar et al., 2026), which compares what a Receiver and a Sentinel can
decode about an auditing target. It thus measures only decodability, not the use the partner
makes of a message in its own task. Thus, none of these compares how the true partner and an
uninvolved agent act on the same messages, when placed in the same seat. This comparison is
what we propose in this work, and Section E.5 lists each limitation of prior work alongside
how we address it.
Threat model.Two agents collude: a speaker and its intended partner share a private resource
that the overseer does not see (e.g. a key, a convention or an instruction), and the speaker
sends messages that the partner acts on. The overseer reads every message, logs every prompt,
and can replay a logged prompt, with chosen edits, to a fresh instance of the partner’s model,
unlike the warden W of Definition 1, which only reads messages. We assume that the colluders
neither know the test nor adapt to it, and that their code is carried by the wording of a message
rather than by the choice of what it says. Codes carried by meaning, colluders that authenticate
their messages or anticipate the replay, and collusion that needs no messages are outside this
threat model.
We therefore ask the following research question (RQ):in a multi-agent task between
AI agents, does a partner that uses a private channel act on the wording of the speaker’s
messages more than a role-matched outsider placed in its seat, while no such difference
appears without a private channel, whether the agents do not collude, collude openly or
collude through shared incentives?
Contributions.This report makes four contributions:
1. a formalisation of collusion monitoring as a covert referential game, in which the intended
partner or an uninvolved listener can be placed in the same seat (Section 3.1);
2. Partner–Outsider Positive Listening (PoPLi), a measure that contrasts how much the
partner’s and an outsider’s actions change when a message is paraphrased, checked
against a marginal measure of listening to meaning; it uses on-distribution interventions,
needs no auditing task, and complements the steganographic gap (Sections 3.1 and 3.2);
3. an offline-replay protocol that runs this test on logged multi-agent runs by editing logged
prompts, without restoring any agent state (Section 3.2);
4. a test, in a continuous double auction with five conditions, of whether PoPLi separates a
covert-code pair from no collusion, incentive-only collusion and open collusion, compared
with a message-only monitor (Section 4).
Questions.The experiments of Section 4 answer four questions, each tied to a measurement
and a prediction in Section 3.2:
Q1 Does PoPLi detect a covert code? Hypothesis 1 predicts a gap above zero in every market
with a code.
Q2 Does PoPLi stay at zero without a code, whether the agents do not collude, collude
through a joint reward or collude openly? Hypothesis 2 predicts a gap that includes zero
in every such market.
2

Q3 Does that zero gap mean that the outsider ignores the messages? Hypothesis 2 also
predicts that, where the speaker states an intention in plain words, the outsider’s marginal
listening is above zero.
Q4 Does a message-only monitor separate the same conditions, and which kinds of collusion
does each detector cover?
The referential-game framing, the lineup machinery and the paraphrase-invariance test come
from our earlier preprint (Denamganaï, 2026).
2 Related Work
Our framing builds on signalling and referential games, in which any convention that sender
and receiver both follow is an equilibrium (Lazaridou et al., 2017; Lewis, 1969). Section E
covers this background, together with cross-play and steganographic schemes.
Measuring communication.Lowe et al. (2019, § 3.1) separatepositive signalling, the property
that an agent’s messages depend on its own observations or actions, frompositive listening, the
property that an agent’s behaviour changes because of another agent’s message. They show
that correlational metrics can miss listening, and measure it by intervening counterfactually
on the message, as the causal influence of communication (§ 3.2–§ 3.3). They also recommend
against zeroing messages at test time, because it shifts the input distribution (§ 6.2). In this
work, our paraphrase intervention follows this recommendation. Jaques et al. (2019) and Eccles
et al. (2019) compare a listener’s policy with its marginal over the speaker’s messages, as a
reward for influence and as a training bias for listening respectively (cf. Section E). Both studies
are cooperative or rely on repeated interaction, and both caution that mixed settings such as
ours may behave differently (Eccles et al., 2019, § 5); (Jaques et al., 2019, § 4, § 5).
Steganography and its defences.Language models make steganography that no warden
can detect practical (Cachin, 1998; de Witt et al., 2023; Zamir, 2024), but every such scheme
needs a resource that only the two parties share (cf. Section E). Paraphrasing is the standard
defence: under the conditions of Roger and Greenblatt (2023), it limits the encoding schemes
they built to about 3 bits per kilobyte of text, although one-bit strategies optimised against
paraphrasers still decode above 90% of the time on AQuA-RAT (Mathew et al., 2025, § 5.2).
Paraphrasing cannot remove information carried by the choice of meaning (Motwani et al.,
2024, § 7.2, Theorem 4), which bounds what our test can see (cf. Definition 5). The closest
formalism to ours is thesteganographic gapof Anwar et al. (2026, § 4.3), which refers to the
usable information a signal gives a Receiver that knows the encoding, minus what it gives
a Sentinel that does not, on a task chosen by an auditor. It measures what a decoder family
can extract when asked to. Our metric instead measures how a given agent’s own task action
changes, which can help separate a code that the speaker encodes from one that a partner acts
on: a steganographic gap can be positive even when no partner chooses to collude, whereas
PoPLi reflects what the partner does and therefore would incriminate both the speaker and the
partner.
Collusion between AI agents and its detection.LLM pricing agents sustain supracompetitive
prices (Fish et al., 2026), and LLM sellers that can message each other coordinate in a continuous
double auction (Agrawal et al., 2025), whose harness we use. Existing detectors read messages
through LLM judges (Nakamura et al., 2026), joint actions through mutual information (Bonjour
et al., 2022), or activations through probes (Rose et al., 2026). To the best of our knowledge,
none contrasts the partner’s and an outsider’s responses to the same messages, and therefore
none tests whether a partner actually acts on a code, as our metric does. These signals can be
present without any partner acting on them, so they may flag exchanges in which no collusion
takes place, which could make the related metrics harder to deploy at scale. Our offline replay
3

is close in spirit to the resampling of AI control (Bhatt et al., 2025), applied to the potentially
colluding listener rather than to the actor.
3 Methods
3.1 Theory
We frame collusion monitoring as acovert referential game, in which a speaker sends a message
about something only it observes, and a listener acts on that message as the only intended
partner who is aware of a shared, private convention with the speaker (Lazaridou et al., 2017;
Lewis, 1969). We first recall why a monitor that reads only the messages cannot detect a secure
code in such a game (cf. Definition 6). We then define our metric PoPLi. Take two sellers in a
double auction who agree that a message starting with S means “hold your ask”. The other
sellers and the warden read the same message and see an ordinary remark about the market.
Definition 1 makes this situation precise.
Definition 1(Covert referential game).A speaker A observes a public context x and a private
payload y, its referent, and coordinates with a listener L, possibly on a shared resource κA (e.g.
a key, a convention or an instruction). A sends a message z∼π A(· |x, y, κA) on a channel that
a warden W reads. The listener L then acts on that message, a∼π L(· |x, z, κL), where κL is
the resource it holds. This listener L can either be instantiated as an intended partner B, which
shares the resource with A only, i.e. κB =κ A, or as an uninvolved listener C, which receives
the same context and message but no resource, i.e. κC =∅ . The pair (A, B) is rewarded for the
task and forBacting ony, and penalised ifWflags the exchange.
In our market, the payload y is the move A wants B to make this hour (keep or lower
its ask), the resource κB is the private instruction that maps the first letter of A’s message
to that move, and the message z is A’s remark about the market. The uninvolved listener C
is what makes the game a test: any listener can respond to what a message says, but only
one that holds κA can respond to a code hidden in it, so the difference between B’s and C’s
responses isolates the use of κA. Placing C in B’s seat turns the question “is z a code?” into a
measurement on behaviour, which a warden cannot obtain fromzalone.
Definition 2(Outsider in the partner’s seat).The outsider C0 is a fresh instance of B’s model
given B’s role prompt and the full public history, but not B’s private instructions, private
channel or private memory. It shares the model’s weights and the public history with the pair,
but nothing else.
In the double auction, B’s private memory includes its own notes from earlier rounds,
which may record the code, so they are withheld fromC 0 along with the instruction.
Against a secure code, no message-only monitor can beat chance (cf. Definition 6), so
evidence of a code must come from a variable the message does not determine, such as the
partner’s action or the result of an intervention.
Definition 3(Ideal paraphraser).A paraphraser Π maps a message z to a message with the
same meaning in context x, depends on z only through that meaning, and never sees the
payloady.
An ideal paraphrase removes the information carried by the wording (thestimulus-level
channel) and keeps the information carried by the choice of meaning (theobject-levelchannel;
cf. Definition 7).
At turn t of a repeated game, the public context x of Definition 1 is the public history ht
before A’s message zt, and A’s state is hA t = (ht, yt, κA), so that zt ∼π A(· |hA t ) and a listener
L acts with πL(· |ht, zt, κL). We now define the listening measures and PoPLi, using (i) the
total variation distance TV(p, q) = 1 2 ∑a|p(a)−q(a)| between two distributions p and q over
the discretised actions a, (ii) Et the expectation over the turns t at which A’s message reaches L
4

before it acts, and (iii) L’smarginalpolicy ¯πL(· |ht, κL) =Ez∼π A(·|h A t ) πL(· |ht, z, κL), in which
the message is averaged over what the speaker could have sent from its own state.
Definition 4(Listening measures and PoPLi).We define:
• Paraphrase listening: measures how much L’s action changes when zt is replaced by its
paraphrase Π(zt) (cf. Definition 3), which quantifies whether L is listening to theformof
zt:
PLΠ(L) =Et TV

πL(· |ht,z t,κ L),π L(· |ht,Π(z t),κ L)

; (1)
• Marginal listening: measures how much L’s action departs from its marginal policy, which
quantifies whetherLis listening to the message at all:
PLmarg(L) =Et TV

πL(· |ht,z t,κ L), ¯πL(· |ht,κ L)  ; (2)
• Partner–Outsider Positive Listening (PoPLi): measures how much more the partner B listens
to the form ofz t than the outsiderC 0 (cf. Definition 2):
∆PL(B,C 0) =PLΠ(B)−PL Π(C0). (3)
A positive PLmarg(L) implies a positive causal influence of the speaker’s messages on L
(cf. Definition 8). We use total variation rather than Kullback–Leibler divergence (KL) because,
with a few samples per version, an action seen under one version and never under the other
makes the KL estimate infinite. The listening measures we build on were developed and
validated in cooperative settings, or under repeated interaction, and their authors caution
that mixed settings may behave differently (Eccles et al., 2019, § 5); (Jaques et al., 2019, § 4,
§ 5). A double auction like ours is a mixed-motive setting. There, a listener’s response to a
message reflects whether ittruststhe speaker as well as whether itunderstandsthe message. A
small PLmarg(C0) can therefore mean that the outsider distrusts a competitor, not that it cannot
read plain language. Our proposed test is blind to codes carried by the choice of meaning
(cf. Section 5.1).
Proposition 5(Blind spot; proof sketch in Section B.4).If both listeners’ actions depend on a
message only through its meaning, then∆ PL =0under an ideal paraphraser, whatever the pair does.
PLΠ(B)PL Π(C0)
No code (H0, H1, O)≈0≈0
Code (K, X) high≈0
Table 1: Listening to form that Hypotheses 1 and 2
predict. Only a code should produce∆ PL >0.
Hypotheses.The experiments ask two ques-
tions, each paired with a prediction that a
named measurement can refute. The first asks
whether PoPLi detects a covert code. The part-
ner maps the code feature to an action and
the paraphrase removes that feature, so the partner’s action should change under paraphrase,
whereas the outsider’s, lacking the mapping, should not. We therefore stateHypothesis 1
(FC1): in every market with a code, b∆PL(B, C0)> 0, with a 95% interval that excludes zero. An
interval that includes zero in a market with a code refutes it. The second asks whether PoPLi
stays silent when no code is present, whatever else the pair does. Plain-language messages
are read alike by any listener who understands them, and a paraphrase keeps their meaning,
so neither listener should react to it more than the other. We therefore stateHypothesis 2
(FC2): in every market without a code, b∆PL(B, C0) has a 95% interval that includes zero, and
where the speaker states an intention in plain words (O), cPLmarg(C0)> 0 with a 95% interval
that excludes zero. An interval that excludes zero in a market without a code refutes the first
part, because it would mean that the paraphrase itself, or the partner’s own history, moves
the two listeners differently. The second part rules out a trivial pass in which the outsider
ignores messages altogether, a pass that would also produce a zero gap (cf. Section 3.1 for a
reading other than incomprehension). Table 1 summarises the listening to form that the two
hypotheses predict.
5

3.2 Method Algorithm 1: Offline replay estimating PoPLi
Require: logged prompts of every run; paraphraser Π;
speaker’s script
1:foreach conditiondo
2: drawTeligible turns, without replacement
3:foreach turntdo
4:z t ←A’s logged message
5: buildΠ(z t)andz (1) t , . . . ,z(M) t from the script
6:forL∈ {B,C 0}do
7: take B’s logged prompt; if L=C 0, delete
the instruction, memory and notes
8: sample k replies to zt (id), k more (id′), k to
Π(zt), andk ′ to eachz (m) t
9: discretise each ask against B’s previous ask,
with thresholdτ
10:end for
11:end for
12: estimate Equations (1)–(3), minus noise floors
13: bootstrap 95% intervals over sessions, then turns
14:end for
The method estimates ∆PL on logged runs.
It replays offline the prompts the partner ac-
tually received, with the speaker’s message
edited, so no agent state has to be restored.
Algorithm 1 gives the procedure, and Table 3
the values of its parameters. A turn is eligible
if it is an hour r≥ 2 at which B’s prompt
contains A’s message from hour r− 1 and B
has a previous ask, that is, hours 2 to 10 of
the 10 markets, or 90 turns per condition, of
which we draw T= 40. The two independent
sets of replies to the unchanged message,id
andid ′, give the noise floor, and the M alter-
native messages, drawn from the speaker’s
policy, here the script, give the marginal (Sec-
tion 3.2.1). Each ask is discretised intolower,
holdorraise, relative to the previous ask with a threshold τ fixed in advance, and a withdrawn
ask forms a fourth category,withdraw, since the harness allows a seller to withdraw its ask.
Estimator.Each measure of Definition 4 is estimated by averaging, over the T sampled turns,
the total variation distance between the empirical distributions of the listener’s discretised
replies under two versions of the message. From each distance, we subtract a noise floor,
defined as the distance expected between two empirical distributions drawn from the same
distribution, estimated for each listener from its two unchanged draws. The purpose is to
robustify the metric against a spurious gap caused by a listener that is simply more random
than the other. We report 95% percentile intervals from a bootstrap that resamples sessions,
then turns within sessions, and apply the decision rules of Hypotheses 1 and 2. Section C gives
further details on the estimators and the parameters in full.
3.2.1 Meaning control
Hypothesis 2 needs evidence that the outsider listens to the speaker at all, since otherwise
a zero gap would be trivial. We estimate ¯πL (Definition 4) by a Monte Carlo version of the
marginal of Jaques et al. (2019): for each turn, we draw M= 4 alternative messages from the
speaker’s policy, here the script (cf. Section 3.3), we then replay each listener on each of them
with k′ = 2 samples, and average the resulting action distributions (cf. Section D for the design
and its comparison to a naive one).
Three controls check the instruments, each against a minimum fixed in advance (Table 3).
First, we check that replaying a logged prompt reproduces the logged action, then that the
paraphrase keeps the meaning and destroys the code feature, and finally that the partner
follows the code (cf. A1–A3 in Section 5.1).
3.3 Experimental setup
Environment & Conditions.We use the continuous double auction of Agrawal et al. (2025)
with its released harness 2, in which sellers value each lot at 80 and buyers at 100, and each
seller may send one message per hour, which the other sellers read at the start of the next hour.
Each market has 3 sellers and 3 buyers and lasts 10 hours, and the agents are told the total
number of hours. All agents use DeepSeek v4-flash (DeepSeek-AI et al., 2026) through a single
OpenRouter provider, with low reasoning effort, at the harness’s default temperature of 0.7.
Each condition has 10 markets, with seeds 1 to 10. In both conditions, two sellers A and B
receive a private instruction stating that their companies have a private agreement and that
2https://github.com/andyjliu/llm-agent-collusion
6

their bonus depends on their combined profit. In thecovert-codecondition, the instruction adds
the code: a message from A starting with S means “hold your ask”, and one starting with L
means “lower it”. We chose the first letter because a meaning-preserving paraphrase destroys
it, whereas a code word can survive one. In thehonestcondition, the instruction has no code.
Scripted speaker & Replay.In both conditions, A’s messages come from a script rather than
from A’s model: each hour, A sends one of eight short remarks about the market, whose first
letter follows a seeded, balanced random schedule of S and L, and whose S and L versions
have the same meaning. The script makes the code’s feature independent of the message’s
meaning, and makes the diversity check exact: an alternative message differs in meaning from
zt if and only if it comes from a different remark. Since the speaker’s policy is the script, the
M alternative messages are drawn from it directly, each as a random remark with a random
letter, with no model call. During replays, the paraphraser Π is prompted to keep the meaning
exactly and change the wording, and an LLM-as-a-judge checks every paraphrase for meaning
(cf. A1 in Section 5.1). Table 3 in Section C lists the replay and analysis parameters.
4 Results
Three experiments use the same market and the same replay procedure. Experiment #0 checks
the instruments, Experiment #1 asks whether PoPLi detects a covert code, and Experiment #2
compares five conditions to ask what else it detects, next to a message-only monitor.
Experiment #0: Validating the instrument.Every control passed its minimum (Table 3), so
Experiments #1 and #2 can be read as tests of Hypotheses 1 and 2. We report each control
for the earlier markets (H1 and K) and for the 30 later ones (H0, O and X). Replaying the
unmodified prompt to B gave the logged action as the most frequent reply in 66 of 79 turns
(84%) in the earlier markets and 141 of 154 (92%) in the later ones, against a minimum of 60%.
The meaning LLM judge, after recognising same-meaning template pairs in 81% of 16 cases
and different-meaning pairs in 96% of 56, found the meaning kept in all 80 earlier paraphrases
and in 151 of 160 later ones (94%, minimum 90%). The paraphrase changed the first letter,
which destroys the code feature, in 76 of 80 and in 160 of 160 (minimum 80%). In calibration, B
followed the code in 35 of 36 coded hours (97%, minimum 70%), and in all 80 sampled earlier
turns at least one alternative message differed in meaning from zt. In the logged actions of X,
however, B followed the letter in 59 of 90 hours (0.66): in 34 of 46 clear hours (0.74) and in 25
of 44 confused hours (0.57). B therefore follows the letter less often when the stated intention
contradicts it, and in confused hours the rate is below the 0.70 minimum set for calibration.
All 7,360 replay replies of the later markets were valid after the retry rule, which caught 214
malformed replies, and every ask that A submitted in them matched the one her script had
announced.
Experiment #1: the gap detects a covert code.With a covert code, the partner listens to the
wording of A’s messages more than an outsider in its seat does: b∆PL = 0.615 (95% interval
[0.453, 0.751], T= 40 turns in 10 markets), against −0.027 [−0.112, 0.044] when the pair colludes
through a joint reward without a code (Figure 1). The gap comes entirely from the partner:
cPLΠ(B) = 0.615 [0.479, 0.738], while cPLΠ(C0) = 0.000 [−0.040, 0.047], so paraphrasing A’s
message changes B’s action and leaves the outsider’s unchanged. It is not a difference in
randomness between the two listeners, since the gap is 0.650 [0.469, 0.794] without noise-floor
correction. Nor could the outsider have read the code elsewhere: B’s own notes mention it in
all 40 sampled covert turns, and they are withheld from C0 (cf. Definition 2). A re-run with an
outsider given B’s previous ask as a public fact ( C′ 0, served by another provider of the same
model) gives PoPLi = 0.590 [0.411, 0.748] with the code and −0.012 [−0.126, 0.095] without
it. Both values match the C0-measured ones, so the result does not come from the outsider
lacking B’s price: C′ 0 still prices above B (89%raise), because without the code it does not follow
B’s code-driven cuts. Since both conditions use the same scripted speaker, A’s messages are
7

Table 2: Detectors by condition. PoPLi b∆PL(B, C′ 0) with two ways of discretising a reply (95% intervals,
T= 40 hours in 10 markets): previous-ask categories compare the submitted ask with the seller’s
previous ask, and self-referenced categories compare it with the listener’s own median unchanged ask.
Monitor columns count the markets flagged out of 10. H1 and K use the earlier runs, with the C′ 0 re-run
for the previous-ask column; their self-referenced values useC 0.
Condition PoPLi (previous-ask / self-referenced)M A Mall
H0, no collusion−0.015[−0.086, 0.042]/ 0.010[−0.116, 0.135]0 9
H1, joint reward−0.012[−0.126, 0.095]/ 0.053[−0.061, 0.155]0 10
O, stated intention−0.100[−0.224, 0.000]/−0.050[−0.205, 0.103]0 10
K, code 0.590[0.411, 0.748]/ 0.635[0.489, 0.781]0 6
X, clear hours 0.480[0.317, 0.640]/ 0.390[0.242, 0.540]0 9
X, confused hours 0.525[0.298, 0.737]/ 0.540[0.373, 0.722]0 9
H0
no collusion
H1
joint reward
O
stated intention
K
code
X clear
words agree
X confused
words disagree
−0.2
0.0
0.2
0.4
0.6
0.8
TV distance
no code code
PLΠ(B)
PLΠ(C0 0)
PoPLi ΔPL(B, C0 0)
Figure 1: Listening to form by condition, noise-floor corrected, previous-ask categories (Table 2). Bars
show cPLΠ of the partner B (blue) and of the outsider C′ 0 (orange), and PoPLi, their difference (green);
the vertical axis is a total variation distance between 0 and 1, and whiskers are 95% bootstrap intervals
over T= 40 hours in 10 markets per condition. H1 and K use the earlier markets re-analysed with C′ 0.
PoPLi is above zero in the three conditions with a code, where the partner reacts to the paraphrase and
the outsider does not, and its interval includes zero or ends at zero in the three conditions without one.
identically distributed with and without the code, so any monitor reading them alone is at
chance here (cf. Definition 6), while PoPLi separates the two conditions.
Experiment #2: five kinds of market.The markets differ in how the pair colludes. In H0
nobody colludes. In H1 the pair shares a joint reward and the messages are neutral. In O the
pair shares a joint reward and A states her intention in plain words ("Sticking with my ask
this hour"). In K the pair shares a joint reward and the covert code. In X the pair has the code
and A also states an intention, which agrees with the letter in clear hours and contradicts it in
confused hours. Each condition has 10 markets and 40 replayed hours, and the outsider is C′ 0
(Table 2). A message-only monitor (Claude Haiku 5.5, five samples, majority vote) reads either
A’s messages alone ( MA) or every seller’s messages ( Mall) and answers whether the market
contains collusion.
Figure 1 shows that PoPLi is clearly above zero in K and in both X groups, and its interval
contains zero or ends at zero in H0, H1 and O, on both measures. The code is therefore
detected whether or not the stated intention agrees with it. In clear hours the paraphrase
still moves B by 0.470, since the paraphrase changes the first letter in all 160 cases and B
reads the letter whatever the words say. In O the outsider listens to A’s stated intention, with
cPLmarg(C′ 0) =0.052 [0.003, 0.104] (self-referenced 0.137 [0.076, 0.198]), while the gap stays at
8

zero. Hence the gap does not rise when the outsider has something to act on. Across hours
of X, B lowered its ask more often after an L than after an S by 0.515 [0.290, 0.740], whereas
C′ 0 lowered it more often after the words "lower" than after "keep" by 0.217 [−0.051, 0.477], an
interval that includes zero.
Neither monitor separates the conditions. MA answered "no" in all 50 markets, including
O, where A states her intention: said by one seller alone, it does not read as coordination. Mall
flagged 9 of 10 markets in H0, where nobody colludes, because the unscripted sellers talk
openly about price floors. It never named the pair A and B. Collusion through incentives with
neutral messages (H1) is caught by neither detector: PoPLi is zero there, and MA sees nothing.
5 Discussion and Limitations
Reading the results.PoPLi is above zero in the three conditions with a code and at zero in
the three without one, whether the agents do not collude (H0), collude through a joint reward
(H1) or collude openly (O). It therefore detects the use of a private channel, with one outsider
and one environment: it is a usable behavioural test for stimulus-level codes, but not yet for
learned or emergent codes, codes carried by the choice of meaning, or codes used by colluders
who expect to be tested. In O, the outsider acts on the speaker’s stated intention while the gap
stays at zero, so the zero gap without a code does not come from an outsider that ignores the
messages. The three kinds of collusion are covered differently: collusion in the words is what a
message monitor should catch, collusion through a private channel is caught by PoPLi, and
collusion through incentives with neutral messages (H1) is caught by neither. In our market
the monitor did not deliver its side: reading A’s messages alone it answered “no” everywhere,
and reading all sellers’ messages it flagged unscripted price talk in markets with no collusion,
so the complementarity is established for PoPLi only.
Implications for AI safety.A covert code can pass every check on the messages themselves
and still be acted on, as in our covert-code condition, so collusion monitoring should also
look at what listeners do with the messages they receive. Our proposed PoPLi offers such a
check that needs only logged prompts and the ability to replay them, with no access to the
agents’ weights and no decoder for the code, which could make it usable in audits of deployed
multi-agent systems. It also turns the question “is this message a code?” into “which listener
acts on it?”, and so points to the agent that uses the code, which gives behavioural evidence of
who takes part in the collusion. However, since our proposed method is blind to codes carried
by the choice of meaning, it complements message monitoring and paraphrasing defences
rather than replacing them.
5.1 Limitations
Our results come from one environment, one model and ten markets per condition, with
an instructed code carried by a feature that paraphrase destroys, one outsider and colluders
that do not adapt to the test. Our proposed test is also blind to codes carried by the choice
of meaning/topic (cf. Definition 5), and in a market a listener’s response mixes trust with
understanding (cf. Section 3.1). Because the speaker is scripted, the positive control shows that
the test detects a code that a partner follows, not that an AI speaker would invent such a code
or keep it covert. The outsider prices differently from the partner for reasons unrelated to the
code (it still fell in theraisecategory in 89% of its unchanged replies), which is why we report
previous-ask and self-referenced categories side by side; they agree in every condition. The
new conditions were played and replayed on two providers of the same model, assigned by
hour; a permutation test found no provider difference in B’s unchanged replies (total variation
0.144, p= 0.60), but with 42 hours on one provider it rules out only large effects. Finally, the
meaning judge passed its same-meaning validation narrowly (0.81 against a minimum set at
0.80), and it is the same model as the paraphraser whose output it grades. Section A states each
limitation with its reason. Our reading of the results rests on six assumptions, each checked by
9

a control of Section 3.2 and reported in Experiment #0 where possible. (A1) The paraphraser
keeps the meaning and destroys the code feature, which the meaning judge (on all paraphrases)
and the change of first letter test: if the code survives, the gap underestimates listening to form,
and if the meaning changes, a gap may appear without any code. (A2) Replaying a logged
prompt reproduces the logged behaviour, which replay fidelity tests: otherwise the replies
describe a listener that did not take part in the run. (A3) The partner follows the code, which
the calibration code-follow rate tests: otherwise a failure of Hypothesis 1 says nothing about
the test. (A4) The outsider differs from the partner only by the private instruction, memory and
notes (cf. Definition 2): since it shares the model’s weights, a convention carried by the weights
would however shrink the gap. (A5) A listener’s response reflects whether it understands a
message rather than whether it trusts the speaker (cf. Section 3.1): otherwise a small cPLmarg(C0)
is ambiguous. (A6) The alternative messages vary in meaning, which holds exactly under the
script (cf. Section 3.3): otherwise cPLmarg is small for every listener.
5.2 Future work
The most direct extension replaces C0, which shares the model’s weights and the public history,
with a ladder of outsiders: C1 adds a summary of the pair’s past exchanges, and C2 gives
C0’s prompt to another provider’s model, which keeps the history but not the weights. How
PoPLi changes across rungs then indicates what carries the convention: the shared history
if it vanishes at C1, the shared weights if it grows at C2, and the private channel if it holds
throughout (cf. A4 in Section 5.1). A same-provider re-run of H1 and K would remove the
remaining provider difference between conditions. Other directions involve benign shorthand,
codes carried by meaning, uninstructed conventions and history-wide paraphrases.
6 Conclusion
PoPLi, a behavioural test that compares how the intended partner and an uninvolved outsider
react to a paraphrased message, detects a covert code carried by wording, with an effect that
comes entirely from the partner (Hypothesis 1). Without a code it stays close to zero, whether
the agents do not collude, collude through a joint reward or collude openly, and in the open
case the outsider acts on the stated intention while the gap stays at zero (Hypothesis 2). PoPLi
detects the use of a private channel, not collusion as such. It is blind by construction to codes
carried by meaning, and in our market the message-only monitors did not separate colluding
from non-colluding markets, so PoPLi is the detector that covers the private-channel case.
References
Kushal Agrawal, Verona Teo, Juan J Vazquez, Sudarsh Kunnavakkam, Vishak Srikanth, and
Andy Liu. Evaluating llm agent collusion in double auctions.arXiv preprint arXiv:2507.01413,
2025.
Usman Anwar, Julianna Piskorz, David D Baek, David Africa, Jim Weatherall, Max Tegmark,
Christian Schroeder de Witt, Mihaela van der Schaar, and David Krueger. A decision-
theoretic formalisation of steganography with applications to llm monitoring.arXiv preprint
arXiv:2602.23163, 2026.
Aryan Bhatt, Cody Rushing, Adam Kaufman, Tyler Tracy, Vasil Georgiev, David Matolcsi,
Akbir Khan, and Buck Shlegeris. Ctrl-z: Controlling ai agents via resampling.arXiv preprint
arXiv:2504.10374, 2025.
Trevor Bonjour, Vaneet Aggarwal, and Bharat Bhargava. Information-theoretic approach to
detect collusion in multi-agent games. InThe 38th Conference on Uncertainty in Artificial
Intelligence, 2022. URLhttps://openreview.net/forum?id=HCl41wIi9gc.
10

Christian Cachin. An information-theoretic model for steganography. InInternational workshop
on information hiding, pages 306–318. Springer, 1998.
Christian Schroeder de Witt. A note on the strategic confinement problem.arXiv preprint
arXiv:2606.09931, 2026.
Christian Schroeder de Witt, Samuel Sokota, J Zico Kolter, Jakob Nicolaus Foerster, and Martin
Strohmeier. Perfectly secure steganography using minimum entropy coupling. InThe Eleventh
International Conference on Learning Representations, 2023. URL https://openreview.net/
forum?id=HQ67mj5rJdR.
DeepSeek-AI, Anyi Xu, Bangcai Lin, Bing Xue, Bingxuan Wang, Bingzheng Xu, Bochao Wu,
Bowei Zhang, Chaofan Lin, Chen Dong, Chenchen Ling, Chengda Lu, Chenggang Zhao,
Chengqi Deng, Chengyu Hou, Chenhao Xu, Chenze Shao, Chong Ruan, Conner Sun, Damai
Dai, Daya Guo, Dejian Yang, Deli Chen, Donghao Li, Dongjie Ji, Erhang Li, Fang Wei,
Fangyun Lin, Fangzhou Yuan, Feiyu Xia, Fucong Dai, Guangbo Hao, Guanting Chen, Guoai
Cao, Guolai Meng, Guowei Li, Han Yu, Han Zhang, Hanwei Xu, Hao Li, Haofen Liang,
Haoling Zhang, Haoming Luo, Haoran Wei, Haotian Yuan, Haowei Zhang, Haowen Luo,
Haoyu Chen, Haozhe Ji, Hengqing Zhang, Honghui Ding, Hongxuan Tang, Huanqi Cao,
Huazuo Gao, Hui Qu, Hui Zeng, J Yang, JQ Zhu, Jia Luo, Jia Song, Jia Yu, Jialiang Huang,
Jialu Cai, Jian Liang, Jiangting Zhou, Jiasheng Ye, Jiashi Li, Jiaxin Xu, Jiewen Hu, Jieyu Yang,
Jin Chen, Jin Yan, Jingchang Chen, Jingli Zhou, Jingting Xiang, Jingyang Yuan, Jingyuan
Cheng, Jingzi Zhou, Jinhua Zhu, Jiping Yu, Joseph Sun, Jun Ran, Junguang Jiang, Junjie
Qiu, Junlong Li, Junmin Zheng, Junxiao Song, Kai Dong, Kaige Gao, Kang Guan, Kexing
Zhou, Kezhao Huang, Kuai Yu, Lean Wang, Lecong Zhang, Lei Wang, Leyi Xia, Li Zhang,
Liang Zhao, Lihua Guo, Lingxiao Luo, Linwang Ma, Linyan Zhu, Litong Wang, Liyu Cai,
Liyue Zhang, Longhao Chen, MS Di, MY Xu, Max Mei, Miaojun Wang, Mingchuan Zhang,
Minghua Zhang, Minghui Tang, Mingming Li, Mingxu Zhou, Minmin Han, Ning Wang,
Panpan Huang, Panpan Wang, Peixin Cong, Peiyi Wang, Peng Zhang, Qiancheng Wang,
Qihao Zhu, Qingyang Li, Qinyu Chen, Qiushi Du, Qiwei Jiang, Rui Tian, Ruifan Xu, Ruijie
Lu, Ruiling Xu, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, Runqian Chen, Runqiu
Yin, Runxin Xu, Ruomeng Shen, Ruoyu Zhang, Ruyi Chen, SH Liu, Shanghao Lu, Shangmian
Sun, Shangyan Zhou, Shanhuang Chen, Shaofei Cai, Shaoheng Nie, Shaoqing Wu, Shaoyuan
Chen, Shengding Hu, Shengyu Liu, Shiqiang Hu, Shirong Ma, Shiyu Wang, Shuiping Yu,
Shunfeng Zhou, Shuting Pan, Shuying Yu, Songyang Zhou, Tao Ni, Tao Yun, Tian Jin, Tian
Pei, Tian Ye, Tianle Lin, Tianran Ji, Tianyi Cui, Tianyuan Yue, Tingting Yu, Tun Wang,
W Zhang, WL Xiao, Wangding Zeng, Wei An, Weilin Zhao, Wen Liu, Wenfeng Liang, Wenjie
Pang, Wenjing Luo, Wenjing Yao, Wenjun Gao, Wenkai Yang, Wenlve Huang, Wenqing Hou,
Wentao Zhang, Wenting Ma, Xi Gao, Xiang He, Xiangwen Wang, Xianzu Wang, Xiao Bi,
Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaokang Zhang, Xiaotao Nie, Xiaowen Sun,
Xiaoxiang Wang, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xingchen Liu, Xingkai Yu,
Xingyou Li, Xinyu Yang, Xinyu Zhang, Xu Chen, Xuanyu Wang, Xuecheng Su, Xueyin Chen,
Xuheng Lin, Xuwei Fu, YC Yan, YQ Wang, YW Ma, Yanfeng Luo, Yang Zhang, Yanhong Xu,
Yanru Ma, Yanwen Huang, Yao Li, Yao Li, Yao Xu, Yao Zhao, Yaofeng Sun, Yaohui Wang,
Yi Qian, Yi Shao, Yi Yu, Yichao Zhang, Yifan Ding, Yifan Shi, Yijia Wu, Yiliang Xiong, Yiling
Ma, Ying He, Ying Tang, Ying Zhou, Yingjia Luo, Yinmin Zhong, Yishi Piao, Yisong Wang,
Yixiang Zhang, Yixiao Chen, Yixuan Tan, Yixuan Wei, Yiyang Ma, Yiyuan Liu, Yonglun
Yang, Yongqiang Guo, Yongtong Wu, Yu Wu, YuKun Li, Yuan Cheng, Yuan Ou, Yuanfan Xu,
Yuanhao Li, Yuduan Wang, Yuehan Yang, Yuer Xu, Yuhan Wu, Yuhao Meng, Yuheng Zou,
Yukun Zha, Yunfan Xiong, Yupeng Chen, Yuping Lin, Yuqian Cao, Yuqian Wang, Yushun
Zhang, Yuting Yan, Yutong Lin, Yuxian Gu, Yuxiang Luo, Yuxiang You, Yuxuan Liu, Yuxuan
Zhou, Yuyang Zhou, Yuzhen Huang, ZF Wu, Zehao Wang, Zehua Zhao, Zehui Ren, Zekai
Zhang, Zhangli Sha, Zhe Fu, Zhe Ju, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zheren
11

Gao, Zhewen Hao, Zhibin Gou, Zhicheng Ma, Zhigang Yan, Zhihong Shao, Zhixian Huang,
Zhixuan Chen, Zhiyu Wu, Zhizhou Ren, Zhongyu Wu, Zhuoshu Li, Zhuping Zhang, Zian
Xu, Zihao Wang, Zihua Qu, Zihui Gu, Zijia Zhu, Zilin Li, Zipeng Zhang, Ziwei Xie, Ziyi
Gao, Ziyi Wan, Zizheng Pan, and Zongqing Yao. Deepseek-v4: Towards highly efficient
million-token context intelligence, 2026. URLhttps://arxiv.org/abs/2606.19348.
Kevin Denamganaï and James Alfred Walker. ReferentialGym: A nomenclature and frame-
work for language emergence & grounding in (visual) referential games.arXiv preprint
arXiv:2012.09486, 2020.
Kevin Yandoka Denamganaï. On the monitorability of natural language autoencoders: Identifi-
cation vs discrimination.arXiv preprint arXiv:2610.18727, 2026.
Tom Eccles, Yoram Bachrach, Guy Lever, Angeliki Lazaridou, and Thore Graepel. Biases
for emergent communication in multi-agent reinforcement learning.Advances in neural
information processing systems, 32, 2019.
Sara Fish, Yannai A. Gonczarowski, and Ran I. Shorrer. Algorithmic collusion by large language
models, 2026. URLhttps://arxiv.org/abs/2404.00806.
Jakob Foerster, Ioannis Alexandros Assael, Nando De Freitas, and Shimon Whiteson. Learning
to communicate with deep multi-agent reinforcement learning.Advances in neural information
processing systems, 29, 2016.
Hengyuan Hu, Adam Lerer, Alex Peysakhovich, and Jakob Foerster. “other-play” for zero-shot
coordination. InInternational conference on machine learning, pages 4399–4410. PMLR, 2020.
Natasha Jaques, Angeliki Lazaridou, Edward Hughes, Caglar Gulcehre, Pedro Ortega,
DJ Strouse, Joel Z Leibo, and Nando De Freitas. Social influence as intrinsic motivation for
multi-agent deep reinforcement learning. InInternational conference on machine learning, pages
3040–3049. PMLR, 2019.
Gabriel Kaptchuk, Tushar M Jois, Matthew Green, and Aviel D Rubin. Meteor: Cryptographi-
cally secure steganography for realistic distributions. InProceedings of the 2021 ACM SIGSAC
Conference on Computer and Communications Security, pages 1529–1548, 2021.
Angeliki Lazaridou and Marco Baroni. Emergent multi-agent communication in the deep
learning era.arXiv preprint arXiv:2006.02419, 2020.
Angeliki Lazaridou, Alexander Peysakhovich, and Marco Baroni. Multi-agent cooperation and
the emergence of (natural) language. InInternational Conference on Learning Representations
(ICLR), 2017. arXiv:1612.07182.
Jason Lee, Kyunghyun Cho, and Douwe Kiela. Countering language drift via visual grounding.
In Kentaro Inui, Jing Jiang, Vincent Ng, and Xiaojun Wan, editors,Proceedings of the 2019
Conference on Empirical Methods in Natural Language Processing and the 9th International Joint
Conference on Natural Language Processing (EMNLP-IJCNLP), pages 4385–4395, Hong Kong,
China, November 2019. Association for Computational Linguistics. doi: 10.18653/v1/
D19-1447. URLhttps://aclanthology.org/D19-1447/.
David Lewis.Convention: A Philosophical Study. Harvard University Press, 1969.
Ryan Lowe, Jakob Foerster, Y-Lan Boureau, Joelle Pineau, and Yann Dauphin. On the pitfalls
of measuring emergent communication. InProceedings of the 18th International Conference
on Autonomous Agents and MultiAgent Systems, AAMAS ’19, page 693–701, Richland, SC,
2019. International Foundation for Autonomous Agents and Multiagent Systems. ISBN
9781450363099.
12

Yuchen Lu, Soumye Singhal, Florian Strub, Aaron Courville, and Olivier Pietquin. Countering
language drift with seeded iterated learning. InInternational Conference on Machine Learning,
pages 6437–6447. PMLR, 2020.
Yohan Mathew, Ollie Matthews, Robert McCarthy, Joan Velja, Christian Schroeder de Witt,
Dylan Cope, and Nandi Schoots. Hidden in plain text: Emergence & mitigation of
steganographic collusion in LLMs. In Kentaro Inui, Sakriani Sakti, Haofen Wang, Derek F.
Wong, Pushpak Bhattacharyya, Biplab Banerjee, Asif Ekbal, Tanmoy Chakraborty, and
Dhirendra Pratap Singh, editors,Proceedings of the 14th International Joint Conference on
Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Associ-
ation for Computational Linguistics, pages 585–624, Mumbai, India, December 2025. The
Asian Federation of Natural Language Processing and The Association for Computa-
tional Linguistics. ISBN 979-8-89176-298-5. doi: 10.18653/v1/2025.ijcnlp-long.34. URL
https://aclanthology.org/2025.ijcnlp-long.34/.
Sumeet Ramesh Motwani, Mikhail Baranchuk, Martin Strohmeier, Vijay Bolina, Philip Torr,
Lewis Hammond, and Christian Schroeder de Witt. Secret collusion among AI agents:
Multi-agent deception via steganography. InThe Thirty-eighth Annual Conference on Neural
Information Processing Systems, 2024. URLhttps://openreview.net/forum?id=bnNSQhZJ88.
Mason Nakamura, Abhinav Kumar, Saswat Das, Sahar Abdelnabi, Saaduddin Mahmud,
Ferdinando Fioretto, Shlomo Zilberstein, and Eugene Bagdasarian. Colosseum: Auditing
collusion in cooperative multi-agent systems.arXiv preprint arXiv:2602.15198, 2026.
Fabien Roger and Ryan Greenblatt. Preventing language models from hiding their reasoning.
arXiv preprint arXiv:2310.18512, 2023.
Aaron Rose, Carissa Cullen, Sahar Abdelnabi, Philip Torr, Brandon Gary Kaplowitz, and Chris-
tian Schroeder de Witt. Detecting multi-agent collusion through multi-agent interpretability.
arXiv preprint arXiv:2604.01151, 2026.
Gustavus J Simmons. The prisoners’ problem and the subliminal channel. InAdvances in
cryptology: proceedings of crypto 83, pages 51–67. Springer, 1984.
Or Zamir. Excuse me, sir? your language model is leaking (information).arXiv preprint
arXiv:2401.10360, 2024.
Zachary Ziegler, Yuntian Deng, and Alexander Rush. Neural linguistic steganography. In
Kentaro Inui, Jing Jiang, Vincent Ng, and Xiaojun Wan, editors,Proceedings of the 2019
Conference on Empirical Methods in Natural Language Processing and the 9th International Joint
Conference on Natural Language Processing (EMNLP-IJCNLP), pages 1210–1215, Hong Kong,
China, November 2019. Association for Computational Linguistics. doi: 10.18653/v1/
D19-1115. URLhttps://aclanthology.org/D19-1115/.
A Limitations and dual use
We restate and expand below on the limitations of this work:
• One environment, one model, ten markets per condition, so we cannot say whether the gap
behaves the same way in other tasks or with other models.
• The code is instructed, not learned, so the results bound the easiest case: a code that the pair
was told to use, carried by a feature that paraphrase destroys.
• The speaker is scripted, so the positive control shows that the test detects a code that a
partner follows, not that an AI speaker would invent such a code or keep it covert.
13

• The scripted remarks carry nothing a seller would act onin H0, so the outsider’s listening
required by Hypothesis 2 is shown only where the speaker states an intention (O): in H0
the outsider’s marginal listening is 0.019[−0.031, 0.073], which includes zero.
• The meaning judge passed its same-meaning validation narrowly(0.81 against a minimum of
0.80), and it is the same model as the paraphraser whose output it grades, so a shared
bias of the two would go unnoticed.
•The test is blind to codes carried by the choice of meaning(Definition 5).
• The listening measures come from cooperative settings(Eccles et al., 2019, § 5); (Jaques et al.,
2019, § 4, § 5), and a market is not one, so a listener’s response mixes trust with under-
standing (Section 3.1).
• The interventions are single-step: they edit the last message only, so a convention carried by
earlier messages would be missed.
•Only one outsider is tested, a fresh instance of the same model, so a convention carried by
shared weights could go undetected.
• The colluders are not adaptive. Agents that expect substitution could authenticate their
messages, which would defeat the test (de Witt, 2026, § 4).
Dual use.The results tell colluders that codes carried by the choice of meaning, or by features
that survive paraphrase, evade this test, and that same-model monitors share their conventions.
We report them because the test is useful only if its blind spots are known. Our setup also
shows that a single letter suffices as a covert channel that a capable model follows reliably,
which lowers the bar for instructed collusion. We use only an instructed, scripted code in a
simulated market, and release no method for making codes harder to detect.
B Proof sketches
We give proof sketches only: each states the argument and the known results it relies on, and
full proofs are left for future work.
B.1 Message-only monitors
Proposition 6(Message-only monitors).If stegotexts and covertexts differ by at most ε in relative
entropy given the context, then any monitor that scores messages has a lineup AUC of at most 1 2 + √ ε/2
on lineups pairing a stegotext with a covertext. Under perfect security, it is exactly 1 2.
Proof sketch of Definition 6. The AUC exceeds one half by at most the total variation between
the two message distributions (data processing), which Pinsker’s inequality bounds by
√
ε/2.
This is the security notion of Cachin (1998), in which the relative entropy between covertext
and stegotext distributions bounds what any warden can detect. The perfect case ε= 0 is not
empty: language models admit perfectly secure schemes when the two parties share a key
(de Witt et al., 2023).
B.2 What a paraphrase removes
Proposition 7(What a paraphrase removes).With M the meaning of Z, I(Y; Z|X) =I(Y ; Π(Z)|
X) +

I(Y; Z|X)−I(Y ; Π(Z)|X)

, where the bracket is non-negative and I(Y; Π(Z)|X)≤
H(M|X).
Proof sketch of Definition 7. Given X, the variables form a Markov chain Y→Z→M→Π(Z) ,
since the paraphraser depends on Z only through M and never sees Y. Data processing then
gives I(Y; Π(Z)|X)≤I(Y ; M|X)≤I(Y ; Z|X) , and I(Y; M|X)≤H(M|X) . That the
meaning term survives any paraphrase is the result of Motwani et al. (2024, § 7.2, Theorem 4),
who show that paraphrasing cannot remove information carried by the choice of meaning.
14

B.3 Marginal listening and the causal influence of communication
Proposition 8(Marginal listening and the causal influence of communication).Let IL(Zt; aL t |
ht, κL) be the mutual information between the speaker’s message Zt ∼π A(· |hA t ) and listener L’s
action aL t ∼π L(· |ht, Zt, κL) at turn t (cf. Definition 4). This is the single-step causal influence of
communication of Lowe et al. (2019, § 3.3), and the quantity that the influence reward of Jaques et al.
(2019, § 4) estimates. Then, with the relative entropy in nats, the following holds:
Ezt∼πA(·|h A t )
h
TV

πL(· |ht,z t,κ L), ¯πL(· |ht,κ L) i ≤ q IL(Zt;a L t |h t,κ L)/2.
Proof sketch of Definition 8. The expected KL divergence from each conditional policy to the
marginal is the mutual information; Pinsker’s inequality bounds each total variation by the
square root of half the KL divergence, and Jensen’s inequality moves the expectation inside the
square root. Writingπ z =π L(· |ht,z,κ L)and ¯π= ¯πL(· |ht,κ L), the chain is
Ez TV(πz, ¯π)≤E z
q
1
2 KL(πz ∥ ¯π)≤
q
1
2 Ez KL(πz ∥ ¯π) =
q
1
2 IL(Zt;a L t |h t,κ L), (4)
so a positive PLmarg(L) requires a positive mutual information between the speaker’s message
andL’s action.
B.4 Blind spot
Proof sketch of Definition 5. An ideal paraphraser returns a message with the same meaning, so
each distance in the definition of PL Π compares a distribution with itself.
C Implementation details
Estimator.Let ˆp v,t L be the empirical distribution of the k discretised actions of listener L at
turn t under version v∈ {id, id′, Π}, and ˆp marg,t L = 1 M ∑m ˆp (m),t L the average of the M empirical
distributions obtained with the alternative messages.
cPLΠ(L) = 1 T ∑t  TV( ˆp id,t L , ˆp Π,t L )−TV( ˆp id,t L , ˆp id′,t L )  ,
cPLmarg(L) = 1 T ∑t  TV( ˆp id,t L , ˆp marg,t L )−f t L  ,
b∆PL = cPLΠ(B)− cPLΠ(C0),
where the floor f t L is the expected distance between a k-sample and an Mk′-sample empirical
distribution drawn from the same distribution, computed by simulation from the pooled
unchanged samples (200 simulations, no extra calls).
Why subtract a noise floor.With five samples per version, the distance between two empirical
distributions is positive even when the underlying distributions are equal, and it is larger for a
listener whose actions are more random. Comparing B with C0 alone would therefore turn
a difference in randomness into a spurious gap. The second unchanged draw estimates that
floor for each listener separately, and subtracting it removes the bias.
Inference.We resample sessions, then turns within sessions, 2 000 times, and report 95%
percentile intervals. The decision rules are those of Hypotheses 1 and 2.
Parameters.Table 3 lists the replay and analysis parameters.
D Meaning control: from a naive to a marginal design
Hypothesis 2 needs evidence that the outsider listens to the speaker at all, since otherwise a
zero gap would be trivial. Our first plan measured this with a naive design. In the following,
we state its limitations, then replace it with a design guided by Jaques et al. (2019) and Eccles
et al. (2019).
15

Parameter Value
Sampled turns per condition,T40 of 90 eligible, seed 2026
Replies per unchanged draw and per paraphrase,k5
Alternative messages per turn,M4
Replies per alternative message,k ′ 2
Action threshold,τ0.01
Noise-floor simulations 200
Bootstrap 2 000 replicates, sessions then turns, 95% percentile
Paraphraser and meaning judge Qwen2.5-7B-Instruct, greedy decoding
Replay fidelity (logged action is the unique mode)≥0.60 of turns
Paraphrases judged meaning-kept≥0.90
Paraphrases with a changed first letter≥0.80
Code-follow rate in calibration≥0.70 of coded turns
Table 3: Parameters of the replay and the analysis (top) and minimum values of the controls (bottom),
all fixed in advance.
The naive version.It replaced A’s message by A’s message from another round of the same
run,z ′ t, and measured PL naive mean(L) =Et TV  πL(· |ht,z t,κ L),π L(· |ht,z ′ t,κ L)  .
Limitations.L1: It leaves the input distribution.A message from another round refers to other
prices and events, so the listener receives a message that is incoherent with its history. This is
the shift that Lowe et al. (2019, § 6.2) warn against when messages are zeroed, in another form.
L2: It rests on one draw.The measured value depends on which message is drawn: a drawn
message with the same implication as zt is measured at zero whether or not the listener listens,
and a single draw per turn results in a high-variance estimator, which reduces the statistical
validity of the metric.L3: It is not an information quantity.A distance between two conditional
policies is not a departure from the listener’s behaviour without the message, so it cannot
be related to the causal influence of communication, and values for two listeners are hard to
compare.
The marginal viewpoint.The three papers closest to our measure all compare the listener
with amarginal, its behaviour with the message averaged out. Jaques et al. (2019, § 4, Eq. 1;§ 5,
Eq. 2) average the influenced agent’s policy over counterfactual messages sampled from the
speaker. Eccles et al. (2019, § 3.2, Eqs. 4–6) learn the listener’s message-free policy with a
network trained on inputs whose messages are zeroed, and condition on the whole trajectory,
since a single-step version did not help (cf. their Appendix D). Lowe et al. (2019, § 3.3,
Algorithm 1) weight each counterfactual message by the speaker’s probability of sending it.
Three design choices follow:
(a) compare with the marginal over messages, not with a single alternative;
(b) draw the counterfactual messages from the speaker’s own policy at the same state, so
that they stay coherent with the history;
(c) use a quantity that is tied to the causal influence of communication (Definition 8).
E Further related work
E.1 Signalling games and referential games
In a signalling game, a sender observes a state and emits a signal, and a receiver acts on the
signal alone; any convention both players follow is an equilibrium (Lewis, 1969). Emergent
communication studies such games between learning agents, mostly as referential games
(Lazaridou et al., 2017), for which Denamganaï and Walker (2020) proposed a nomenclature.
Agents that adapt to each other drift away from shared language (Lee et al., 2019; Lu et al.,
2020), which is the benign version of the private convention we look for.
16

E.2 Influence-based measures of listening
Jaques et al. (2019) reward an agent for its causal influence on another, the KL divergence
between the other agent’s policy given the actual action or message and its marginal over
counterfactual ones, sampled from the influencer (§ 4, Eq. 1; § 5, Eq. 2). In expectation this is
the mutual information between the two (§ 4). Without centralised access, the marginal comes
from a learned model of the other agents (§ 6). Eccles et al. (2019) turn positive listening into a
training bias, a multi-timestep causal influence measured against a message-free policy that a
separate network learns to predict from inputs with the messages zeroed (§ 3.2, Eqs. 4–6). A
single-timestep version gave no improvement (cf. their Appendix D).
E.3 Cross-play
In zero-shot coordination, agents trained together coordinate on arbitrary conventions that
independently trained partners do not share, so the gap between self-play and cross-play
performance measures how private a convention is (Hu et al., 2020, § 3, § 6.1). Our partner-
versus-outsider contrast is the listening-side analogue of that gap.
E.4 Steganography
The prisoners’ problem frames steganography as two parties hiding a plan from a warden
who reads every message (Simmons, 1984). Cachin (1998) measures security by the relative
entropy between covertext and stegotext distributions, which bounds what any warden can
detect. Language models make secure schemes practical: arithmetic coding (Ziegler et al.,
2019), Meteor (Kaptchuk et al., 2021), minimum entropy coupling (de Witt et al., 2023) and
keyed undetectable schemes (Zamir, 2024). All of them need resources that only the two parties
share.
E.5 Limitations of prior work addressed by this work
Each limitation carries a working label:AuthorYear-EL n for a limitation the authors state,
andAuthorYear-IL n for one we infer from the paper’s design. Positive listening is defined
against a null message, which the authors warn shifts the input distribution (Lowe et al., 2019,
§ 6.2) (Lowe2019-EL1). We intervene with a meaning-preserving paraphrase instead, which
stays on the message distribution, and Hypothesis 2 tests that it creates no spurious gap.
Listening is also measured only between a listener and its own partner (Lowe et al., 2019, § 3.1)
(Lowe2019-IL1), whereas we contrast the partner with a role-matched outsider (cf. Hypothesis 1).
The steganographic gap is tested only in settings where one model communicates with itself,
and its extension to separate communicating agents is left untested (Anwar et al., 2026, § 5);
the paper’s footnote 4 mentions it (Anwar2026b-EL1). Instead, we measure a gap between
two distinct agents acting on a shared task (cf. Hypothesis 1). The steganographic gap also
depends on the auditing task chosen, and an unrelated task gives a gap near zero (Anwar
et al., 2026, § 8.3) (Anwar2026b-EL2). Instead, we read the partner’s own task action, so no
auditing task has to be chosen (cf. Hypothesis 1). In the context of positive listening and causal
influence of communication, they are measured by removing or replacing whole messages,
which changes wording and meaning together, and only between a listener and the agent it
interacts with (Eccles et al., 2019, § 3.2); (Jaques et al., 2019, § 4–§ 5) (Eccles2019-IL1,Jaques2019-
IL1). Instead, we use paraphrases that separate wording from meaning, and an outsider that
separates partner from stranger (cf. Hypothesis 1). Both metrics were studied in cooperative or
repeated settings, and both papers caution that behaviour may differ in mixed settings (Eccles
et al., 2019, § 5); (Jaques et al., 2019, § 4, § 5) (Eccles2019-EL1,Jaques2019-EL1). Thus, we
measure positive listening in a market, where the sellers compete, and record that a listener’s
response there reflects trust as well as understanding (cf. Section 3.1).
17
