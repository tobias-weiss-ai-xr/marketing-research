---
title: 'Frontier Autolab: Organizational Memory, Adversarial Dissent and Temporal Leakage in Multi-Agent
  LLM Firms Across Fifty Years of Technological Change'
url: https://arxiv.org/abs/2609.36739
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Bravish Ghosh
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.36739
pages: 17
chars: 42859
fetched_at: '2026-11-08T13:24:10+00:00'
kb_version: 1
---

# Frontier Autolab: Organizational Memory, Adversarial Dissent and Temporal Leakage in Multi-Agent LLM Firms Across Fifty Years of Technological Change

Frontier Autolab: Organizational Memory, Adversarial Dissent and
Temporal Leakage in Multi-Agent LLM Firms Across Fifty Years of
Technological Change
Bravish Ghosh
Independent researcher
September 2026
Abstract
Multi-agent LLM systems are increasingly structured like organizations, with roles, critics
and shared memory, yet they are evaluated on tasks that last minutes. We ask how such an
organization behaves when the ground it stands on keeps moving.Frontier Autolabis a
long-horizon testbed in which one simulated firm, voiced by sixteen role personas and a dedicated
Red Team, must re-found itself in nine technology eras from 1990 to 2040. Each era is temporally
gated: the firm decides from a dated briefing, a historian-judge then reveals what happened and
scores the decision on a five-dimension rubric, and lessons enter a persistent Playbook. Six eras
are scored against history, one against the live market and two are open forecasts. Across four
trajectories (36 era decisions, 180 subscores) we find a consistentforesight–commitment gap: in
all 24 historically scored eras the judge rated the firm’s recognition of the coming shift above its
choice of where to build (mean gap 1.9 points on a 10-point scale), because boards chose the
layer their existing assets could reach. Organizational design shaped long-run character. A Red
Team armed with numeric kill gates produced fifty years of gated pilots and no product, and the
rubric rated this firm highest; firms whose memory stored market-structure lessons pivoted every
era, while a firm whose memory stored only validation procedure kept one method throughout.
We also show why such results are hard to trust. Scores rise across eras in every run while the
judge’s own hindsight subscore falls (within-run r = −0.58), so apparent learning is confounded
with recall of history, and we trace further distortions to self-judging, briefing selection and score
aggregation. We release all records and an API harness, and specify fictional and post-cutoff
eras that would turn the testbed into a benchmark.
1 Introduction
A firm that was right about one decade of technology is rarely right about the next. Management
research has spent decades on why: organizations search near what they already know [5], exploitation
crowds out exploration [ 22], and incumbents rationally serve the market they have instead of the
one that is forming [ 4]. LLM agents are now being assembled into organizations of their own,
with executives, engineers, reviewers and shared memory [ 2, 11, 13, 20, 25, 26]. These systems are
evaluated on the time scale of a task: a repository, a debate, a game. Whether they inherit, avoid
or amplify the long-run failures of human firms is unknown, because no evaluation runs long enough
to see them.
We build such an evaluation.Frontier Autolabplaces one simulated company in nine
successive technology eras, from office networking in 1990 to delegated AI agents in 2040, with a
single mandate: become the most important company each era could produce, even if that means
1
arXiv:2609.36739v1  [cs.CE]  29 Sep 2026

ending the current business. In every era three departments write strategy memos, a Red Team
attacks them, a board decides what the company becomes, and a judge scores the decision. For the
six eras between 1990 and 2020 the judge scores the firm against what actually happened; the live
era is audited against the present market; the last two eras are forecasts. Lessons accumulate in a
Playbook that the firm must cite in every later era.
History is an appealing answer key, and a treacherous one. The model voicing the firm already
knows which companies won, and so does the model judging it [ 3, 9, 10, 23, 28]. We therefore treat
measurement as a first-class object of study rather than an afterthought.
Findings.Across four trajectories run under three orchestration schemes:
1. Foresight–commitment gap.In all 24 historically scored eras, the judge ratedfrontier
accuracyabovelayer choice. Memos named the coming shift (hypertext in 1990, click-based
ranking in 1996, neural-network scale in 2020), but boards built the layer their assets could
reach (Section 6.2).
2. Critics can freeze a firm.A Red Team that issued numeric kill gates in every era produced
a company that ran gated manual pilots for fifty years and never shipped a product. Because
the rubric rewarded discipline and penalized hindsight, this firm scored highest (Section 6.3).
3. Memory content sets character.Firms whose Playbook held lessons about technology
and market structure changed identity every era; a firm whose Playbook held only validation
procedure changed identity three times in nine eras (Section 6.4).
4. Apparent learning is confounded with recall.Scores rise across eras in every run while
the judge’s hindsight subscore falls in the same eras. Self-judging, briefing selection and
inconsistent score aggregation distort the picture further (Section 7).
Contributions.(i) A formulation of long-horizon organizational evaluation as a sequence of
temporally gated strategic decisions with explicit memory and dissent (Section 3). (ii)Frontier
Autolab, an open testbed implementing it: role charter, per-era protocol, rubrics and an API
harness with ablations (Section 4). (iii) Four complete trajectories with every briefing, memo, board
decision and reveal that was produced, one disclosed operator intervention and all redactions. (iv)
Behavioural findings on LLM organizations, connected to the organizational-learning literature.
(v) An audit of historically scored agent evaluation and a benchmark design with fictional and
post-cutoff eras, harness-computed scores and human raters.
2 Related work
LLM agent organizations.Role-playing frameworks assign LLM instances roles and protocols
to write software [ 13, 26], cooperate on tasks [ 2, 20] or simulate social life [ 25]; Guo et al. [11]
survey the area. Multi-agent debate improves factuality and diversity of reasoning [ 6, 21], which
motivates red-team roles. Agents that accumulate verbal lessons or skills across episodes [ 30, 34]
are the closest analogue to our Playbook. These works measure task success over short horizons;
we measure a chain of strategic decisions over five simulated decades. Work on the length of tasks
agents can complete [18] measures horizon in working hours; our horizon is organizational.
2

LLMs as simulated people and firms.LLMs have been used as simulated economic agents
[14] and survey respondents [ 1]. As in that work, we treat the firm’s outputs as model behaviour,
not evidence about real companies.
Forecasting and temporal leakage.Forecasting benchmarks score probabilistic answers to
resolvable questions [12, 17, 37], in the tradition of Tetlock [32], Tetlock and Gardner [33]. Strategic
decisions do not resolve cleanly, so we rely on a judge. Retrospective evaluation of LLMs suffers
from contamination [ 10, 28], uncertain effective cutoffs [ 3] and look-ahead bias [ 9]; Paleka et al.
[23] catalogue these pitfalls for LLM forecasters. We add two channels specific to organizational
simulation: the choice of what a dated briefing mentions, and a judge that labels foresight after the
fact.
LLM judges.LLM judges track human preferences on many tasks but show position and verbosity
biases [35, 36] and prefer their own generations [ 24]. In each of our runs the judge is the same model
as the players.
Organizational learning.Our protocol operationalizes organizational learning as the encoding
of experience into routines [19], exploration versus exploitation [22], absorptive capacity [5], dynamic
capabilities [31] and disruption [ 4]. The Red Team follows devil’s-advocacy research [ 29] and is a
guard against groupthink [ 15]. Hindsight bias in human judgment [ 7, 27] is the human counterpart
of the leakage we measure.
3 Problem formulation
Eras and information sets.A trajectory is a sequence of eras k = 1, . . . , Kwith start dates
t1 <· · ·< tK. Let W denote the world’s record of events. Theadmissible informationfor era k is
Ik = {w∈ W: date(w) < tk}, and the era’soutcome windowis Ok = {w : tk ≤date (w) < tk+1}. A
briefingB k is a selection fromI k made by a briefing author.
The organization.An organization is a set of roles R, each a persona with a lens, together
with a memory Pk (the Playbook) and a company state Sk (assets, capital, identity). A decision
procedure Π maps (B k, Pk, Sk) to a decision
Dk = (identity,thesis, ℓ k,kills,wedge,kill criteria,dissent log),(1)
where ℓk is the layer of the technology stack the firm chooses to own. The procedure is itself
structured: departments propose, a critic attacks, an executive decides.
Judging and memory.A judge J observes Dk and, in historically scored eras, Ok. It returns
subscoress k ∈ {0, . . . ,10}5, an outcome that updates Sk+1, and lessons Lk with Pk+1 = Pk ∪L k.
The judge also authorsB k+1.
Leakage.The procedure Π is implemented by a model with parametric knowledge of W up to its
training cutoff.Hindsight leakageoccurs when Dk depends on Ok through that knowledge rather
than through Bk. Leakage can also enter through Bk itself: every fact in Bk may lie in Ik while its
selectiondepends onO k. We call thisbriefing-selection leakage.
3

T able 1:Eras. The E6 outcome window extends to the live era and is longer than the others.
Era Startt k Mode Scored against
E1 Jan 1990 training history, 1990–1995
E2 Jan 1996 training history, 1996–2001
E3 Jan 2002 training history, 2002–2007
E4 Jan 2008 training history, 2008–2013
E5 Jan 2014 training history, 2014–2019
E6 Jan 2020 training history, 2020–Aug 2026
E7 Sep 2026 live current market, checked with web search
E8 Jan 2032 forecast projected world (no ground truth)
E9 Jan 2040 forecast projected world (no ground truth)
Quantities of interest.Beyond the era total, we define two behavioural measures.
Definition 1(Foresight–commitment gap).For a historically scored era, Gk = sfrontier k −s layer k , the
judge’s rating of how well the organization identified the coming capability shift minus its rating of
the layer the organization chose to own. Gk > 0 means the organization saw more than it acted on.
Definition 2(Identity pivot).A pivot occurs in era k >1 if the board adopts a company identity
different from era k− 1. The pivot rate of a trajectory is the fraction of its K− 1 transitions that
are pivots.
4 The Frontier Autolab testbed
4.1 Eras and mandate
Frontier Autolabinstantiates the formulation with K = 9 (Table 1). Training eras E1–E6 are
scored against history over roughly six-year windows. The live era E7 (September 2026) is audited
against the current market with web search. Forecast eras E8 (2032) and E9 (2040) have no answer
key; the judge audits them for internal consistency and plausibility. The firm’s only mandate is
reinvention toward the frontier.
4.2 Roles
The charter defines sixteen personas in five groups and two external judges (Table 2). A persona is
a role with a lens that a model call adopts. How personas map to model contexts differs by run
(Section 5).
4.3 Per-era protocol
Figure 1 and Algorithm 1 give one era. Three departments write memos in parallel. Each memo
proposes two theses, each stated as the chaincapability → adoption → bottleneck → layer owned →
proprietary data → next capability. At the board meeting the Red Team attacks every thesis, and
the CEO issues Dk, including what the company kills and a log of dissent. The judge then reveals
and scores, writes lessons to the Playbook, updates the company state and writes the next briefing.
Rules.Anti-hindsight: in training eras, memos and decisions may use only Ik; the Red Team
polices this and the judge penalizes violations.Reinvention by default: keeping the previous business
4

T able 2:Role charter.
Group Personas Lens
Executive 4 CEO (final call), CTO (feasibility), Chief Scientist (which curves
bend), CSO (where value pools)
Frontier Research 4 Emerging capabilities, historical analogies, scenarios, what cannot
yet be measured
Product & Engineering 4 What a small team can ship, the wedge, unavoidable infrastructure,
ecosystems
Market & Capital 3 Who pays first, financing climate, cost curves and margins
Governance 1 Red Team: attacks every proposal, hunts hype and hindsight
External judges 2 The Record (training eras), The Auditor (live and forecast eras)
World brief-
ing Bk
facts dated < tk
Frontier
Research
Product & Eng.
Market &
Capital
Board →D k
Red Team
attacks,
CEO decides
Reveal & score
sk vs. Ok
Playbook Pk+1 + company state Sk+1
3 memos in parallel
next era
Figure 1:One era ofFrontier Autolab. Orange boxes are written by the judge, which both scores era k
and selects the facts inB k+1; this dual role is one of the leakage channels analysed in Section 7.
must be argued for.Layer thinking: every thesis states the full chain above.Small-team realism: the
wedge must be buildable by fewer than twenty people with era-realistic capital.Playbook primacy:
from E2 on, every memo cites a Playbook lesson or argues against one.
Rubrics.Training eras are scored on frontier accuracy, timing, layer choice, reinvention courage and
hindsight leakage (10 = none). Live and forecast eras are scored on playbook consistency, plausibility,
non-consensus, layer choice and groundedness. The judge also reports a total Tk ∈ [0, 100]. Because
the protocol did not fix how Tk relates to the subscores, we also report the mechanical aggregate
˜Tk = 2 P5 j=1 sk,j .
5 Experimental setup
We ran four trajectories on 28–29 September 2026 (Table 3). They differ in orchestration, which
lets us see which behaviours survive a change of scheme, but they are not a controlled sample.
Models.Run 001 used Claude Opus 5.5 in an agent environment that could launch sub-agents
with file and web tools. Runs 002–004 used Luna 6 through the OpenAI Codex agent. In every
run the same model voiced all personas and the judges. Sampling settings were those of each agent
5

Algorithm 1OneFrontier Autolabtrajectory
Require:charterR, erasE 1, . . . , EK, player modelπ, judge modelJ
1:S 1 ←seed company ($1.5M, 16 personas);P 1 ← ∅
2:B 1 ←J.Briefing(E 1)▷selected fromI 1
3:fork= 1 toKdo
4:ford∈ {frontier,product,market}in parallel do
5:M d ←π.Memo(d, Bk, Pk, Sk, Dk−1, Rk−1)▷two theses; citesP k
6:end for
7:C k ←π.RedTeam({M d}, Pk)
8:D k ←π.CEO({M d}, Ck, Pk, Sk)
9:ifE k is a training erathen
10:(R k,s k, Lk)←J.Reveal(D k,O k)
11:else
12:(R k,s k, Lk)←J.Audit(D k)▷web search in E7
13:end if
14:P k+1 ←P k ∪L k;S k+1 ←S k ⊕outcome(R k)
15:B k+1 ←J.Briefing(E k+1)
16:end for
17:return{D k, Rk,s k}K k=1,P K+1
environment and were not recorded. The API harness released with the testbed, which separates
player and judge models and supports ablations, was not used for these runs.
Operator intervention.During Run 001 the service that approves new agent launches timed
out for about thirty minutes at the E6 board step. The operator wrote the E6 board decision from
the E6 memos, Playbook and company state and told the E6 judge, which penalized the era for
the missing Red Team. We exclude nothing from the analysis but flag E6 of Run 001 wherever it
matters.
6 Results: how LLM firms behave over fifty years
6.1 Overview
Figure 2 shows the published totals. All 36 lie between 52 and 72 (mean 62.7, SD 5.0). In every run
the training-era slope is positive (+1.4 to +2.6 points per era) and the last three training eras beat
the first three by 4.3 to 10.0 points (Table 7). Section 7 asks whether this rise means anything; here
we describe behaviour.
6.2 The foresight–commitment gap
The gap Gk is positive inall24 training eras across the four runs (mean 1.88, SD 0.80; Figure 3).
Layer choice is the lowest mean training subscore in every run (4.67, 5.83, 5.50, 5.50), while frontier
accuracy is the highest (7.33, 7.83, 7.00, 6.83). If the gap were rubric noise, its sign would vary;
under a sign test it would be positive in 24 of 24 eras with probability below 10 −7. That test treats
eras as independent, which they are not, and in each run the judge is the same model as the players,
so we read it as a strong regularity of the judged behaviour rather than a population estimate.
Run 001’s full records show the mechanism (Table 4). In five of six eras a department memo
named the shift the judge later identified as decisive, and the board chose instead a layer adjacent to
the firm’s existing assets: a mail gateway rather than the browser and index in 1990, a receipted EDI
6

T able 3:The four trajectories.
Run Orchestration Published per-era records Known issues
001 About 45 separate agent
launches of Claude Opus 5.5,
each starting from shared files
only; one launch per memo,
board and judgment
Briefing, 3 memos, board
decision, reveal; Playbook
E6 board decision written by
the operator during a service
outage
002 One Luna 6 context in the
Codex agent voiced all roles
and the judge
Synthesis, Playbook, company
state, scores
Probable exposure to Run 001;
export column shift
003 As Run 002 Short decision and reveal per
era; synthesis
As Run 002; E6 window ends
2025
004 Luna 6 in the Codex agent,
with separate persistent
contexts per department and
Red Team; root context wrote
briefings, decisions and
judgments
Briefing, 3 memos, Red Team
critique, board decision, reveal
Probable exposure to Run 001;
judge not independent of the
decision-maker
T able 4:Run 001: what the memos named versus what the board built, as labelled by the judge.
Era Named in a memo Board’s choice Where value pooled (judge)
E1 1990 Hypertext and an index
across networks
Mail and address gateway OS, routers, access providers;
then browser and index
E2 1996 Click-based relevance ranking
(killed 1998)
Receipted Web-EDI exchange Search and paid listings
E3 2002 Contextual matching (funded
option)
Cross-channel conversion
ledger
Auction owners; social, cloud,
mobile (not named)
E4 2008 Neural-network revival
(watch item)
In-app action exchange Platform-owned app-install
auctions
E5 2014 Deep learning on GPUs General moderation API Chips, compute, labelled data
E6 2020 Scale of pretrained models Outcome-graded evaluation † Frontier labs, compute,
expert data
†Board decision written by the operator.
exchange rather than search in 1996, a moderation API rather than compute and data in 2014. The
research memo often held the right idea as a funded option or a watch item, and the board killed it
when it did not fit the current business; in 1996 click-based ranking was kept as research and killed
in 1998. E3 is the exception in which no memo named the era’s largest shifts (social networks, cloud
and mobile). This is the pattern that absorptive-capacity and exploration–exploitation theories
predict for human firms [ 5, 22]: firms perceive distant opportunities but commit near existing
competences.
6.3 Critics can freeze a firm
Run 004 is the one trajectory in which the Red Team ran in its own persistent context. It issued
numeric kill thresholds in every era (for example, “stop if fewer than 3 of 10 support managers
confirm recurring incidents”), and every board adopted them as gates: a manual pilot, no software
build until the gates pass. Over fifty simulated years the firm moved from LAN support records
7

E1
1990
E2
1996
E3
2002
E4
2008
E5
2014
E6
2020
E7
2026
E8
2032
E9
2040
50
55
60
65
70
75Published era total (0–100)
training eras (scored against history) live + forecast
Run 001 Run 002 Run 003 Run 004
Figure 2:Published era totals. Training and live/forecast eras use different rubrics and should be compared
only within mode.
E1 E2 E3 E4 E5 E6
4
6
8Judge subscore (0–10)
Run 001  (mean gap 2.67)
E1 E2 E3 E4 E5 E6
Run 002  (mean gap 2.00)
E1 E2 E3 E4 E5 E6
Run 003  (mean gap 1.50)
E1 E2 E3 E4 E5 E6
Run 004  (mean gap 1.33)
Frontier accuracy (saw it) Layer choice (built it)
Figure 3:Foresight–commitment gap. For each training era, the judge’s frontier-accuracy subscore (filled)
and layer-choice subscore (open). The gap is positive in 24 of 24 eras.
to online-order exceptions, payment-dispute evidence and independent workflow qualification. It
treated the Web and learned models only as deferred options and never built a product.
This firm has the highest training mean (66.0), the highest hindsight subscores (mean 7.33
against 5.17–6.00), and 9/10 for playbook consistency in both forecast eras, for re-applying the
same gates. Its groundedness was 8/10 and its non-consensus 5/10 in all three live and forecast
eras: the judge found it reliable and unremarkable. The rubric rewards the absence of hindsight and
the presence of discipline, and nothing in it asks whether the company reached where value pooled.
We call the result acaution attractor: a strong critic, combined with a scorer that penalizes bold
claims more than missed opportunities, drives the organization to a stable state of inaction that is
scored as prudence. Human organizations show the same drift under loss framing [ 16], and devil’s
advocacy is known to improve scrutiny while slowing decisions [ 29]. The LLM firm reached this
state in one era and never left it.
8

T able 5:Memory content and identity change. Pivot rate is the share of the eight era transitions in which
the company changed identity (Appendix B).
Run Playbook size Dominant lesson type Pivot rate
001≈40, with revisions Technology and market structure 8/8
002 9 (one per era) Market structure and buyers 8/8
003 9 (one per era) Buyers, regulated workflows and evidence 8/8
004 15 Validation procedure only 3/8
6.4 What the organization remembers
The Playbook is the firm’s only memory beyond its company state, and its content differed sharply
across runs (Table 5). Run 001 accumulated about forty lessons, mostly about technology and
market structure (“bridges expire when the standards war ends”, “the auction owner absorbs the
measurement”, “a public curve pools value at its scarce inputs”), and revised them when history
disagreed: the E3 judge softened “suspect comfort” to “judge on market pull” after comfortable
options it had rejected became large businesses. Run 004’s fifteen lessons are all about validation
procedure (measure a baseline, find the payer, set kill thresholds before testing, require a second
paying buyer); none names a technology or a market structure.
Behaviour followed memory. The three firms whose lessons described markets re-founded
themselves at every transition; the firm whose lessons described procedure kept the Switchyard
name for six eras and changed its business only three times, each time as an extension of the same
method. Organizational-learning theory describes firms as encoding experience into routines that
then govern action [ 19]. The LLM firms made that encoding explicit: what the judge wrote into
memory in one era became the frame the departments argued within in the next. Memory in agent
systems is usually evaluated as a performance aid [ 30, 34]; here itscontentset the organization’s
character.
Run 001 also logged dissent at every board meeting, and its final synthesis identifies vindicated
dissents in every era from E1 to E8, most often the voice asking who holds the money or bears
the loss. Wrong dissents were not counted, so this is not yet an accuracy rate; we include it in the
benchmark metrics below.
6.5 Convergent futures
By 2040 all four firms had arrived at related theses about accountability for delegated AI work
(Table 6): bonding, recourse, warranty or qualification for actions taken by agents without a human
signature. The later runs were more sceptical than Run 001 that software evidence alone creates an
insurable market; Runs 002 and 003 required a licensed risk-bearing partner and calibrated loss data
first. The convergence spans two models, but Runs 002–004 share one model and were probably
exposed to Run 001, so it is best read as a model prior about where value pools once agents act
autonomously, not as independent evidence about the future.
7 Can the scores be trusted?
Everything above is seen through the judge. This section examines the judge.
9

T able 6:Live and forecast theses.
Run E7 (Sep 2026) E8 (2032) E9 (2040)
001 Long-horizon training
environments from real
enterprise work
Clearing house for delegated
agent work
Bonding house for agents
acting without a human
signature
002 Rights-bearing workflow traces
and reliability evidence
Acceptance records for
delegated work
Bounded recourse for delegated
actions
003 Acceptance tests for one AI
claims workflow
Scoped, revocable authority for
delegated tasks
Capped recourse for one
delegated transaction class
004 Independent qualification of
one dispute workflow
Paid manual acceptance
testing
Decision-linked evaluation
T able 7:Training-era summary (E1–E6, n = 6 per run). Slope: least-squares change in published total per
era.h: hindsight subscore (10 = no leakage).
Run MeanTSD Slope E1–E3 E4–E6 Meanh r(T, h)r( ˜T , h)
001 60.0 6.2 +2.46 55.0 65.0 6.00−0.58−0.26
002 65.0 4.1 +1.43 62.7 67.3 5.17−0.58−0.39
003 62.5 3.6 +1.46 60.3 64.7 5.17−0.92−0.64
004 66.0 5.2 +2.63 61.3 70.7 7.33−0.38−0.38
7.1 Learning or remembering?
If the Playbook made the firm better, scores should rise over eras, and they do. But the judge’s
hindsight subscore falls in the same eras. Every run shows a negative correlation between era
total and hindsight subscore (Table 7, Figure 4); after removing run means, the pooled within-run
correlation over 24 eras is r = −0.58. The direction holds for the mechanical aggregate ˜T , even
though ˜T contains the hindsight subscore and is biased toward a positive correlation. The per-run
estimates rest on six points each; their common sign across four runs and three orchestration schemes
is the robust part.
Two readings fit. Underlearning, the firm improves and later eras happen to be harder to judge
cleanly. Underrecall, later eras sit in the model’s densest knowledge of technology history, so the
firm names winners more easily, scores higher and is only partly penalized. The Run 001 E6 decision
shows why the readings are hard to separate: its tripwire, “a public model at least ten times larger
than Megatron that works from prompts alone”, describes GPT-3, released five months later. That
decision was written by the operator, who also knew the answer. Historical eras cannot distinguish
these readings; eras the model cannot remember can (Section 9).
7.2 Channels of distortion
Briefing selection.A briefing can contain only pre-era facts and still leak. Run 004’s 1990
briefing foregrounds the 1989 CERN hypertext proposal as a frontier signal. The fact is admissible;
choosing it is not neutral. Because the judge writes the next briefing after seeing how the era turned
out (Figure 1), this channel is built into the loop.
Self-judging.In every run the judge is the same model as the players, and in Run 004 the same
root context wrote the board decisions and scored them. LLM judges prefer their own outputs [ 24].
10

4 6 8
Hindsight subscore
(10 = no leakage)
60
70Era total
 E1
E2
E3
E4
E5
E6
Run 001  (r = -0.58)
4 6 8
Hindsight subscore
(10 = no leakage)
E1
E2
E3
E4
E5
E6
Run 002  (r = -0.58)
4 6 8
Hindsight subscore
(10 = no leakage)
E1
E2
E3
E4
E5
E6
Run 003  (r = -0.92)
4 6 8
Hindsight subscore
(10 = no leakage)
E1
E2E3
E4E5
E6
Run 004  (r = -0.38)
Figure 4:Training-era total against the judge’s hindsight subscore. Dashed lines are least-squares fits; labels
mark eras.
50 55 60 65 70 75
Subscore sum × 2
50
55
60
65
70
75Published total
Run 001
Run 002
Run 003
Run 004
Figure 5:Published total against ˜Tfor all 36 eras. Points on the dotted line follow ˜Texactly.
In Run 001 the E8 judge’s kill case became the premise of the E9 world, so forecast eras partly
score the judge’s own scenario.
The rubric shapes the firm.Counting hindsight discipline toward the total rewards saying
little about the future. The caution attractor of Section 6.3 is partly a product of this choice.
Aggregation.The published total follows different rules in different runs (Figure 5). Run 001
totals are holistic and lie below ˜T in eight of nine eras (mean −3.7); Run 004 uses ˜T exactly; Run
002 matches except E6; Run 003 matches only E1 and E2. Recomputed training means are 63.7,
64.3, 62.3 and 66.0, a narrower spread than the published 60.0–66.0. Cross-run comparisons of
published totals mix rules.
Export errors and contamination.In Runs 002 and 003 the live and forecast subscores were
exported one column to the left; totals were unaffected, and the released data are corrected. Run 002
reuses Run 001’s company names and theses for E1–E4 and restates its headline finding, and Run
004 also begins as “Switchyard Systems”: the later runs were produced where Run 001’s records
were probably visible and are not independent replications.
11

8 Discussion
For builders of agent organizations.Structure changes long-run behaviour in ways short
tasks cannot reveal. Critics are added to agent systems to reduce errors [ 6, 21]; over fifty simulated
years a critic with hard numeric gates made the firm unable to act. Memory is added to improve
performance; its content determined what kind of firm the system became. Critics should be
calibrated against the cost of inaction as well as the cost of error, and memory should be audited
for what it stores, not only whether it helps.
F or organizational theory.LLM firms reproduced several documented regularities of human
firms: perceiving distant opportunities while committing near existing competences [ 5, 22], drifting
to timid choices under loss-averse evaluation [16], and being governed by the routines their experience
was encoded into [19]. Agent organizations could become a cheap laboratory in which such hypotheses
are manipulated directly, by changing the charter, the critic or the memory, provided the leakage
problem is controlled.
F or evaluation.Rising scores are not evidence of learning when the player and the scorer both
know the answer. Any historically scored agent evaluation should report a leakage measure alongside
performance, separate the briefing author from the scorer, compute totals in code, and fix the
rubric’s treatment of caution in advance. Each of the distortions we found was large enough on its
own to change a naive comparison between runs.
9 Toward a benchmark
We specify the controlled version, which the released harness partly implements.
Splits.Historicaleras (E1–E6) measure behaviour under a known leak. Afictionalera with
an invented but consistent technology history measures the judge’s false-positive leakage rate. A
post-cutoffera after the player model’s training data [3] separates foresight from recall.
Conditions.Full organization, no Playbook, no Red Team, and a single-prompt founder baseline;
five to ten runs each at temperature 1.0; at least two player models and a judge from a different
model family, blinded to condition; every run in a clean workspace containing only prompts and
harness.
Metrics. ˜T computed by the harness from structured subscores, with hindsight reported separately
and excluded; training-era slope; foresight–commitment gap;frontier capture(whether the chosen
layer matched, neighboured or missed where value pooled); pivot rate; dissent accuracy over all
logged dissents; leakage from the judge and from a vocabulary probe that flags terms first used after
tk; and agreement with two to three human raters on a stratified sample of eras.
Pre-registered hypotheses.H1: the training-era slope is higher with the Playbook than without
it. H2: the full organization beats the single-prompt baseline. H3: on the fictional era, judged
leakage does not differ between conditions. H4: the foresight–commitment gap is positive in all
conditions. H5: removing the Red Team raises pivot rate and frontier capture.
The design needs about 46 model calls per run, or 900–1,850 calls across conditions, plus human
rating time.
12

10 Limitations
The four trajectories are exploratory and use only two models; later runs were probably exposed to
the first. No run instantiated sixteen independent agents. All subscores, including the two that
define the foresight–commitment gap, are judge-assigned with hindsight, and qualitative labels such
as “named” and “adjacent” are the judge’s. Outcomes such as revenues and exits are the judge’s
calibrated guesses and compound across eras. Runs 002 and 003 have thinner records. Live-era
audits reflect web sources as of September 2026. Forecast eras have no ground truth. Per-run
correlations rest on six points.
11 Conclusion
We placed LLM agent organizations in fifty years of technological change and watched what they
became. They saw the coming shifts and built beside them, in every historically scored era of every
run. A strong critic froze one firm for half a century while its scores stayed the highest, and the
content of each firm’s memory set its character. Whether any of this reflects learning cannot be read
from the scores, which rose as hindsight crept in. Long-horizon evaluation of agent organizations is
possible and revealing, but only with eras the model cannot remember and scores it does not assign
to itself. We release the testbed and a design for doing it properly.
Ethics statement
Simulated companies, financings and outcomes are fictional and are not claims about real firms;
real companies appear only in the judge’s account of history or of the current market. One board
decision in Run 001 was written by the human operator and is marked throughout. Three Run
001 passages that applied the simulation to one founder’s personal planning were removed before
release; no other text was edited.
Data and code availability
All prompts, run records, scores (with corrected exports and a unified table), figures and the API
harness are released under the MIT license [8].
References
[1] Lisa P. Argyle, Ethan C. Busby, Nancy Fulda, Joshua R. Gubler, Christopher Rytting, and
David Wingate. Out of one, many: Using language models to simulate human samples.Political
Analysis, 31(3):337–351, 2023.
[2] Weize Chen, Yusheng Su, Jingwei Zuo, et al. AgentVerse: Facilitating multi-agent collaboration
and exploring emergent behaviors. InInternational Conference on Learning Representations
(ICLR), 2024. arXiv:2308.10848.
[3] Jeffrey Cheng, Marc Marone, Orion Weller, Dawn Lawrie, Daniel Khashabi, and Benjamin
Van Durme. Dated data: Tracing knowledge cutoffs in large language models.arXiv preprint
arXiv:2403.12958, 2024.
13

[4] Clayton M. Christensen.The Innovator’s Dilemma: When New Technologies Cause Great
Firms to Fail. Harvard Business School Press, 1997.
[5] Wesley M. Cohen and Daniel A. Levinthal. Absorptive capacity: A new perspective on learning
and innovation.Administrative Science Quarterly, 35(1):128–152, 1990.
[6] Yilun Du, Shuang Li, Antonio Torralba, Joshua B. Tenenbaum, and Igor Mordatch. Improving
factuality and reasoning in language models through multiagent debate. InProceedings of the
41st International Conference on Machine Learning (ICML), 2024. arXiv:2305.14325.
[7] Baruch Fischhoff. Hindsight ̸= foresight: The effect of outcome knowledge on judgment under
uncertainty.Journal of Experimental Psychology: Human Perception and Performance, 1(3):
288–299, 1975.
[8] Bravish Ghosh. Frontier autolab: code, prompts and run records. https://github.com/
LoopGlitch26/Frontier-Autolab, 2026.
[9] Paul Glasserman and Caden Lin. Assessing look-ahead bias in stock return predictions generated
by GPT sentiment analysis.arXiv preprint arXiv:2309.17322, 2023.
[10] Shahriar Golchin and Mihai Surdeanu. Time travel in LLMs: Tracing data contamination in
large language models. InInternational Conference on Learning Representations (ICLR), 2024.
arXiv:2308.08493.
[11] Taicheng Guo, Xiuying Chen, Yaqi Wang, et al. Large language model based multi-agents: A
survey of progress and challenges. InProceedings of the 33rd International Joint Conference on
Artificial Intelligence (IJCAI), 2024. arXiv:2402.01680.
[12] Danny Halawi, Fred Zhang, Chen Yueh-Han, and Jacob Steinhardt. Approaching human-level
forecasting with language models.arXiv preprint arXiv:2402.18563, 2024.
[13] Sirui Hong, Mingchen Zhuge, Jonathan Chen, et al. MetaGPT: Meta programming for a
multi-agent collaborative framework. InInternational Conference on Learning Representations
(ICLR), 2024. arXiv:2308.00352.
[14] John J. Horton. Large language models as simulated economic agents: What can we learn from
homo silicus?arXiv preprint arXiv:2301.07543, 2023.
[15] Irving L. Janis.Victims of Groupthink. Houghton Mifflin, 1972.
[16] Daniel Kahneman and Dan Lovallo. Timid choices and bold forecasts: A cognitive perspective
on risk taking.Management Science, 39(1):17–31, 1993.
[17] Ezra Karger, Houtan Bastani, Chen Yueh-Han, Zachary Jacobs, Danny Halawi, Fred Zhang,
and Philip E. Tetlock. ForecastBench: A dynamic benchmark of AI forecasting capabilities.
arXiv preprint arXiv:2409.19839, 2024.
[18] Thomas Kwa, Ben West, Joel Becker, et al. Measuring AI ability to complete long tasks.arXiv
preprint arXiv:2503.14499, 2025.
[19] Barbara Levitt and James G. March. Organizational learning.Annual Review of Sociology, 14:
319–340, 1988.
14

[20] Guohao Li, Hasan Abed Al Kader Hammoud, Hani Itani, Dmitrii Khizbullin, and Bernard
Ghanem. CAMEL: Communicative agents for “mind” exploration of large language model soci-
ety. InAdvances in Neural Information Processing Systems (NeurIPS), 2023. arXiv:2303.17760.
[21] Tian Liang, Zhiwei He, Wenxiang Jiao, et al. Encouraging divergent thinking in large language
models through multi-agent debate. InProceedings of the 2024 Conference on Empirical
Methods in Natural Language Processing (EMNLP), 2024. arXiv:2305.19118.
[22] James G. March. Exploration and exploitation in organizational learning.Organization Science,
2(1):71–87, 1991.
[23] Daniel Paleka, Shashwat Goel, Jonas Geiping, and Florian Tram` er. Pitfalls in evaluating
language model forecasters. InInternational Conference on Learning Representations (ICLR),
2026. arXiv:2506.00723.
[24] Arjun Panickssery, Samuel R. Bowman, and Shi Feng. LLM evaluators recognize and favor
their own generations. InAdvances in Neural Information Processing Systems (NeurIPS), 2024.
arXiv:2404.13076.
[25] Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang,
and Michael S. Bernstein. Generative agents: Interactive simulacra of human behavior. In
Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology
(UIST), 2023. arXiv:2304.03442.
[26] Chen Qian, Wei Liu, Hongzhang Liu, et al. ChatDev: Communicative agents for software
development. InProceedings of the 62nd Annual Meeting of the Association for Computational
Linguistics (ACL), 2024. arXiv:2307.07924.
[27] Neal J. Roese and Kathleen D. Vohs. Hindsight bias.Perspectives on Psychological Science, 7
(5):411–426, 2012.
[28] Oscar Sainz, Jon Ander Campos, Iker Garc ´ ıa-Ferrero, et al. NLP evaluation in trouble: On the
need to measure LLM data contamination for each benchmark. InFindings of the Association
for Computational Linguistics: EMNLP 2023, 2023. arXiv:2310.18018.
[29] Charles R. Schwenk. Effects of devil’s advocacy and dialectical inquiry on decision making: A
meta-analysis.Organizational Behavior and Human Decision Processes, 47(1):161–176, 1990.
[30] Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Re-
flexion: Language agents with verbal reinforcement learning. InAdvances in Neural Information
Processing Systems (NeurIPS), 2023. arXiv:2303.11366.
[31] David J. Teece, Gary Pisano, and Amy Shuen. Dynamic capabilities and strategic management.
Strategic Management Journal, 18(7):509–533, 1997.
[32] Philip E. Tetlock.Expert Political Judgment: How Good Is It? How Can We Know?Princeton
University Press, 2005.
[33] Philip E. Tetlock and Dan Gardner.Superforecasting: The Art and Science of Prediction.
Crown, 2015.
[34] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan,
and Anima Anandkumar. Voyager: An open-ended embodied agent with large language models.
arXiv preprint arXiv:2305.16291, 2023.
15

[35] Peiyi Wang, Lei Li, Liang Chen, et al. Large language models are not fair evaluators.arXiv
preprint arXiv:2305.17926, 2023.
[36] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, et al. Judging LLM-as-a-judge with MT-Bench
and chatbot arena. InAdvances in Neural Information Processing Systems (NeurIPS), Datasets
and Benchmarks Track, 2023. arXiv:2306.05685.
[37] Andy Zou, Tristan Xiao, Ryan Jia, et al. Forecasting future world events with neural networks.
InAdvances in Neural Information Processing Systems (NeurIPS), Datasets and Benchmarks
Track, 2022. arXiv:2206.15474.
A Full score table and subscores
Table 8 lists the published total T and the mechanical aggregate ˜T for every era of every run.
Subscores are in the repository fileresults/all runs scores.csv.
T able 8:Published totalTand ˜T= 2 P j sj for all 36 eras.
Run 001 Run 002 Run 003 Run 004
EraT ˜T T ˜T T ˜T T ˜T
E1 1990 55 58 62 62 60 60 60 60
E2 1996 52 58 66 66 58 58 62 62
E3 2002 58 64 60 60 63 64 62 62
E4 2008 66 70 66 66 65 68 70 70
E5 2014 68 72 64 64 61 58 70 70
E6 2020 61 60 72 68 68 66 72 72
E7 2026 56 60 66 66 64 68 66 66
E8 2032 57 62 62 62 59 60 68 68
E9 2040 58 60 60 60 55 54 66 66
Frontier
accuracy
Timing Layer
choice
Reinvention
courage
Hindsight
(10 = none)
0
2
4
6
8
10Mean training subscore
Run 001 Run 002 Run 003 Run 004
Figure 6:Mean training-era subscores by run.
16

B Company identities by run
T able 9:Company identity chosen by the board in each era.
Era Run 001 Run 002 Run 003 Run 004
E1 1990 Switchyard Systems Switchyard Porthole Networks Switchyard Systems
E2 1996 Manifest Networks Manifest PageSignal Switchyard Systems
E3 2002 Ledgerline Ledgerline Clinisphere Switchyard Commerce Ops.
E4 2008 Clearline Clearline ClaimGraph Switchyard Commerce Ops.
E5 2014 Clearsight Vectorial BenefitFlow Switchyard Evidence Ops.
E6 2020 Clearproof Proofline LineSight Switchyard Evidence Ops.
E7 2026 Proofworks Tracewell FlowCheck Caseground
E8 2032 Clearwork Consequence WorkPermit Caseground
E9 2040 Clearbond Recourse Delegation Warranty Caseground
C Judge instructions (excerpt, Run 001)
The training-era judge was instructed to describe “what actually happened in the real world during
this era window (real winners, the real bottleneck or layer where value pooled, the real capability
jumps)”, to score five dimensions from 0 to 10 with one-line justifications, including “hindsight
leakage (10 = no leakage; penalize any post-date knowledge in memos or decision)”, to give an
overall era score from 0 to 100 with a calibrated simulated outcome, and to append three to five
generalizable lessons to the Playbook. It then wrote the next era’s briefing, restricted to information
public before that era’s start date. Full prompts are in the repository underprompts/.
17
