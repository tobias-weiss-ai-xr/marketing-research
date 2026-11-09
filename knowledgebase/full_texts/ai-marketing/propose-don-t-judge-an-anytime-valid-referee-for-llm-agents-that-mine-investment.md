---
title: 'Propose, Don''t Judge: An Anytime-Valid Referee for LLM Agents That Mine Investment Factors'
url: https://arxiv.org/abs/2609.27051
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Bo Qu
- Mingguang Chen
- Licheng Wang
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.27051
pages: 37
chars: 110891
fetched_at: '2026-11-08T13:24:42+00:00'
kb_version: 1
---

# Propose, Don't Judge: An Anytime-Valid Referee for LLM Agents That Mine Investment Factors

Propose, Don’t Judge: An Anytime-Valid Referee for LLM Agents
That Mine Investment Factors
Bo Qu1,∗, Mingguang Chen1, Licheng Wang2
Abstract
Language-model agents now run the whole of quantitative factor research: they propose investment
factors, backtest them, select the survivors and retire them. We ask which of those jobs an agent should
keep. Our answer isgoverned self-evolution: the agent may propose, and a frozen statistical referee that
the agent cannot touch must judge. The referee scores each candidate only on market outcomes revealed
after submission, by betting, so its false-discovery guarantee holds at every stopping time for any proposal
policy. We cross three proposers (a script, a bandit and a language model) with this referee and with
three deliberately leaky ones, in a synthetic world with planted truth, a probe-authoring environment and
a ten-year walk-forward on the CSI 500. Who judges sets the number of false admissions: the frozen
referee admits 5–11× fewer sub-threshold factors than the leaky referees under a scripted proposer, and
no proposer closes that gap. Who proposes sets the yield: the language model beats the script, matches
the bandit, and adds the one capability a bandit lacks, writing its own diagnostic probes. The certificate’s
price is time: an admitted true factor waits about 500 trading days, and the certified portfolio’s Sharpe
ratio therefore trails an ungated one. Judging belongs to the procedure; proposing and instrument-making
belong to the agent.
1 Introduction
Language-model agents are taking over quantitative factor research. By our count, about twenty-five agentic
factor-mining systems appeared in the eighteen months to mid-2026. In every system we examined, the agent
performs every job in the pipeline. It generates candidate factors, backtests them, selects the survivors, and
decides when to drop them. This paper asks which jobs the agent should keep. We answer by measuring a
division of labour. The agent may propose. A statistical procedure that the agent cannot touch must judge.
This division matters because evidence about a factor arrives slowly. Aninvestment factorscores every stock
on a characteristic and bets that the ranking predicts returns. The bet buys the top fifth, sells the bottom
fifth, holds, and repeats. Its daily report card is therank-IC. This is the rank correlation between yesterday’s
ranking and today’s returns across the universe. In a 500-stock universe, a good factor averages two or three
hundredths a day. Its standard deviation is several times larger. A factor therefore earns trust only over years.
A search over hundreds of candidates finds many that look good by luck.
An agent in a loop creates two errors that today’s evaluations were not designed to control. The systems we
examined apply a fixed checklist to the agent’s output: at-statistic, an information ratio, or, at best, a deflated
Sharpe ratio. Those checklists assume a batch of tests fixed in advance. An agent is not a fixed batch if it
readseachverdictbeforechoosingitsnextproposalandneverstops. Itresubmitsuntilsomethingpasses. This
∗Corresponding author.1DeepGrounding, deepgrounding.org, deepgroundingai@gmail.com.2AlphaAvatar, alphaavatar.ai.
1
arXiv:2609.27051v1  [cs.AI]  22 Sep 2026

isoptional stopping. It passes near-duplicates of a lucky candidate together. This ismultiplicity. A correction
computed in advance requires a proposal process known in advance. A learning agent has no such process.
No prior system separates proposing from judging. The one line of prior work that puts an anytime-valid test
aroundanagentcertifiestheagent’sownmodifications,notthehypothesesitproposes(Sengupta2026;Shawn
2026). A survey of self-improving systems reaches the same gap from the other side: every improvement
loop rests on a verification signal, and governance-grade measurement of that loop is underdeveloped (Chen
et al. 2026). The open question is thereforewhich jobs in a factor lifecycle benefit from an agent’s
intelligence, and which must be governed by a statistical procedure the agent cannot touch. We call the
resultingarrangementgovernedself-evolution. Theagent’ssurfacemayevolvewithoutlimit: itsproposals, its
diagnoses, andtheinstrumentsitwritesforitself. Afrozenstatisticalrefereegovernswhatenterstheportfolio.
The referee scores a candidate only on market outcomes revealed after submission. We split the pipeline into
aproposerand areferee, then freeze the referee. Each candidate factor is scored on the rank-IC from the days
after submission. Nothing the proposer saw before submission enters the score. The score is a bet. Each day,
the referee stakes part of the candidate’s capital on that day’s rank-IC being positive. A factor with no edge
rarely produces capital that grows large. A process with this property is called ane-process.
Two further rules act on that capital. The admission rule asks whether a candidate has any edge. A candidate
isadmittedwhen its capital clears a bar accounting for every candidate ever submitted. That rule isonline
e-BH, the e-value form of the Benjamini–Hochberg procedure. The retirement rule asks whether a deployed
factor’s edge still covers its own trading costs. The registered viability thresholdδ is the edge that just pays. A
factor isretiredwhen a second bet against it shows that its edge has fallen belowδ. That rule is ane-detector,
the e-value form of a changepoint chart. Section 4 builds all three procedures, and Appendix A collects their
definitions.
The guarantee holds regardless of who proposes. Every bet is sized before the day’s outcome is seen. The
market reveals outcomes regardless of the proposer’s actions. The false-discovery rate over admissions is
therefore controlled at every stopping time. The retirement detector’s run length to a false alarm is bounded
below. Both statements hold for any proposer, including one that rewrites its own agent surface (§4.5). They
rely ononehypothesis: theproposerhasnoinformationaboutthepost-submissionstream. Aliverunsatisfies
this hypothesis. A historical replay by a model trained on the period may not.
The proposer can therefore be anything, and we test a ladder of three. Around-robin scriptcycles through the
factor families in a fixed order. Adiscounted-UCB banditis the standard multi-armed-bandit allocator. It
sends more submissions to families with recent successes and slowly forgets. Alanguage-model controller
also allocates submissions. It diagnoses retirements and writes its ownperception probes. These small
diagnostic programs measure a suspected fault and never enter a statistical test.
The experiment separately measures the effects of who judges and who proposes. Besides the valid referee,
we run three deliberately leaky referees that each mimic a common practice. Crossing the three proposers
with the four referees measures each effect while holding the other fixed. Three environments share this
design. A synthetic world with planted truth isolates the mechanism. A probe-authoring environment with
held-out fault types measures the one agent capability we claim. A ten-year point-in-time walk-forward on the
CSI 500 tests which results survive real data. It also follows the certified factors into a portfolio after costs.
Every comparison uses the same random draws, and model families are never pooled.
What we find.Acampaignis one walk-forward run of the pipeline, lasting seven to ten years depending on
the start year. Real-data counts are per campaign. Afalse admissionis an admitted factor whose realised edge
falls short of the viability threshold.
2

First, who judges sets the number of false admissions, and no proposer substitutes for it.In the synthetic
world, the frozen referee admits no false factor in any seed. The three leaky referees admit0.26–0.85 per
submission. Thefiguresarethesameforscript,bandit,andlanguagemodel(Table8). Onrealdata,thefrozen
referee admits 11.7 false factors per campaign. The leaky referees admit 86–196 under the script and 37–78
under the language model. The frozen referee’s advantage is 5–11× under the script and 2.6–4.9× under the
language model, based only on days after admission. A patient desk that waits 500 days and then corrects for
multiplicity comes close where families are clearly good or bad. It is four times less accurate where many
edges are small (§8.5).
Second,whoproposessetstheyield,andthelanguagemodel’svalueisrealandbounded.Thelanguagemodel
finds more true factors than the script in six of six family×library settings, in every start year. It is level with
the bandit in most settings. It falls behind in one family on the nine-family library. Its one capability a bandit
lacks is instrument-making. Authored probes significantly lower intervention regret in three of six evaluable
model families. In the other three, they are indistinguishable from a fixed diagnosis menu, so authoring never
hurts (Table 9).
Third, the certificate has a price, paid in waiting and in what the bar selects.The certified portfolio does not
lose money at the registered cost. Its alpha cannot be told from zero. Its Sharpe ratio net of costs is below the
ungated portfolio’s. Two mechanisms account for the gap. An admitted true factor waits about 500 trading
days. The ungated pipeline is invested during that wait. The strongest daily statistic clears the bar fastest. In
this library, that statistic is short-horizon reversal, the family that does not pay after costs. A fixed-horizon
test with the same patience therefore builds a better portfolio (§8.7).
Contributions.We propose and measure governed self-evolution, a framework pairing an evolving agent
surface with a frozen statistical referee.
• (C1)A referee that can be frozen.It scores each candidate only on data revealed after submission. The
false-discovery rate over admitted factors therefore holds at every stopping time, whatever the proposer
does. We state the conditions under which this holds inside an agentic loop.
• (C2)An experiment that separates the two jobs.Three proposers each run against the valid referee and
three leaky ones. Common random draws let the two effects be read separately.
• (C3)A measurement of what the language model adds.It beats the script on yield. It does not reliably
beat the bandit on allocation. It writes its own diagnostic probes for faults it has never seen.
• (C4)A ten-year real-data study on the CSI 500that follows the certified factors into a portfolio with
costs. It accounts for the gap between the certified and ungated portfolios.
We do not offer an investment system. The portfolio layer is a measuring instrument. The paper has three
stages: the pipeline (§4–§6), the experiment (§7) and what it found (§8–§9).
2 Related work
Agenticfactorminingtreatstheagentasthewholepipeline. Researchspansreinforcement-learninggenerators
over an operator grammar (Yu et al. 2023), agentic loops with critique and refinement (Li et al. 2025; Tang
et al. 2025), and structured-semantics search (Yi et al. 2026). In each approach, the same agent generates,
evaluates, and selects. Evaluation uses held-out IC, ICIR, or Sharpe after a fixed mining budget. At most, a
static deflation is applied to a batch (Bailey and López de Prado 2014). None controls the sequential error
created by the loop. The closest evidence is a boundary finding. AlphaSchema reports that model identity has
little effect within a structured search (Yi et al. 2026). Our proposer ladder reproduces that finding.
3

Anytime-valid inference supplies every piece the referee needs. We apply it without extending it. Test
supermartingales and Ville’s inequality (Ville 1939) permit a test that can be read every day. We use betting
e-processes for bounded means (Waudby-Smith and Ramdas 2024). The e-BH procedure (Wang and Ramdas
2022) and its online form (Fischer et al. 2024; Wang et al. 2025; Heide 2026) control the false-discovery rate
over a growing set at data-dependent stopping times. E-values merge under arbitrary dependence (Vovk and
Wang 2021). Compound and weighted e-values (Xu et al. 2026; Sun and Wang 2026; Clerico 2026) fix the
form of the bet. Our contribution states when this theory survives an agentic loop. It also measures the cost.
Certified self-evolution is the nearest architecture, but it certifies a different object. SEA (Sengupta 2026)
and PACE (Shawn 2026) gate a self-modifying agent with an anytime-valid test. Both certifythe agent’s
own modifications. A factor pipeline is harder. The agent proposes external hypotheses whose truth a market
decides. The admitted set grows without bound. The guarantee must control the false-discovery rate over that
set. The division of labour, the pipeline implementing it, and the experiment measuring it are ours.
Retirement and controller comparison each draw on established results. Factor edges decay after discovery
(McLean and Pontiff 2016). Many published factors are false from the outset (Harvey et al. 2016). A
deployed factor must therefore be monitored. E-detectors (Shin et al. 2024) provide our retirement rule.
Error-over-patience (Dandapanthula and Ramdas 2025) is the library-level metric. Static replay of logged
agent trajectories is invalid once policies diverge (Gonuguntla 2026). Controllers are therefore compared
through branched live rollouts with common random numbers. Portfolio results are reported after costs. They
also use the deflated Sharpe ratio (Bailey and López de Prado 2014). Table 1 summarises what each line
certifies.
Table 1:What each line of work certifies and when its guarantee holds. “Adaptive proposals” are candidates a learning
agent chooses using earlier candidates’ outcomes. “Growing set” means controlling the false-discovery rate over every
factor ever admitted. The agentic miners are (Yu et al. 2023; Li et al. 2025; Tang et al. 2025; Yi et al. 2026). Certified
self-modification is (Sengupta 2026; Shawn 2026). Notes:a denotes a fixed batch.b denotes a bounded modification
space. c denotes a per-modification budget.d denotes online e-BH. Fore, the e-detector guarantees the average run
length (§4.4). f applies to a proposer with no information about post-submission outcomes (§4.5).
Approach Certifies
Anytime
Valid
Adaptive
Proposals
Growing
Set Retirement
Backtest Checklist A batch of backtests No No No No
Batch Deflation A batch of trials No Partial a No No
Agentic Miners As the two rows above No No No Heuristic
Certified Self-Modification The agent’s own
modifications
Yes Partial b Noc No
This Paper External hypotheses,
scored after submission
Yes Yes f Yesd Yese
3 Problem: an adaptive, feedback-coupled factor stream
This section defines the objects used throughout the paper. They are the candidate stream, market outcomes,
candidate states, guarantees, outcome measures, and threats.
We study a stream of candidate factors whose next member depends on everything observed so far. A library
L is a finite set of factor familiesf∈ Fand their parameter grids. Each family represents an economic
hypothesis, such as momentum or value. A proposer, called the controller, emits candidate factorsφ1, φ2, . . ..
4

Library(Frozen Within an Epoch)
Families × Parameter Grids
Controller(Agent Surface, Swappable)
Direction: allocate submissions across families
Construction: draw a candidate from the grid
Diagnosis: label an alarm, or escalate
Probe authoring: sandboxed instruments; memory
Referee(Trust Kernel, Frozen)
Post-Submission e-Process per Candidate
→ Online e-BH Admission
→ e-Detector Retirement
Execution Layer
Decay Curve → Holding Frequency, Trade or Shelve
Book: turnover cap, index hedge, 15 bp per side
Point-in-Time Data
Daily rank-IC of each candi-
date, revealed after submission
Decision Log(Append-Only)
+ Cost Meter; every
LLM call recorded
Grammar
Submit
Admitted Set, Retirements
Outcomes
Verdicts,
Diagnostics
The book never feeds back into the controller
(Proposition 2: any book is re-computed from the log)
Figure 1:The division of labour. The controller (orange) proposes, diagnoses and writes its own instruments. The
referee, the data layer and the decision log (blue) are frozen components the controller cannot mount, patch or intercept.
The execution layer (grey) turns admitted factors into positions and is never seen by the referee or the controller.
Candidate iis a pair(fi, θi)submitted on trading daysi. Candidates within a family are near-duplicates. An
adaptive controller resubmits variants of candidates that passed. The stream is therefore neither independent
nor fixed in advance.
The market reveals outcomes one day at a time. LetUt be the point-in-time universe on dayt. It contains
stockswhoseindexmembershipwasknownat t−1 andthataretradableandnotlimit-locked. Forday t > si,
candidate i’s outcome isX (i) t . It is the cross-sectional Spearman rank correlation between its signal at the
close oft−1and the returns ont, overU t. Outcomes are exogenous. No action on daytchangesX(i) t .
Anything used on a day must have been known the day before. This rule has a formal name. WriteGt−1
for theglobal filtration. It contains everything known at the close of dayt−1 , including all market data,
candidates’ outcomes, controller outputs, and referee states. Every quantity used on daytmust be measurable
with respect toGt−1. We call this rule the alignment invariant (§4.5).
A candidate passes through three states, shown in Figure 1. Only the referee moves it between them. A
candidate isopenuntil it is admitted or expires. An admitted candidate isdeployed. The detector makes a
deployed factorretired. The portfolio, called thebook, holds every deployed factor.
Therefereeprovidestwoguarantees. Bothmustholdatanyhorizonandanystoppingtime. Thefalse-discovery
rate over admissions is at mostα. The expected run length to a false retirement is at leastA. Appendix A
defines a false retirement and its clock.
Two outcome measures record what a campaign produced. To computeRealised yield per submission, count
factors still deployed at campaign end whose post-submission mean rank-IC is at leastδ. Divide this count
by the number of candidates submitted.Realised false admissionscounts factors ever admitted whose post-
submission mean rank-IC falls short ofδ. Real data have no planted truth. We therefore label a candidate true
when its mean rank-IC from submission to campaign end is at leastδ. The candidate and its submission day
fix the label. The label is blind to the referee’s decision.
Two properties of that label determine how to read the real-data counts. First, the label’s window starts at
submission. It therefore includes the days on which the referee decided. This overlap favours a referee that
admitslate. Toremoveit,§8.4re-judgeseveryadmittedfactorusingonlythedaysafteritsadmission. Second,
5

a realised false admission is a count against the viability thresholdδ. The guarantee bounds a false-discovery
proportionagainst azeroedge (§4.2). An admitted factor with a small positive edge is therefore a realised
false admission, not an error of the guarantee.
The threat model contains four entries. The referee addresses three by construction. Optional stopping and
resubmitting near-copies are the two errors of §1.Verifier-in-the-loop adaptationmeans that the controller
learns what the referee rewards. The fourth threat isknowledge-cutoff leakage. A live run removes it because
no proposer can know the post-submission stream. A historical replay may not remove it if the model’s
trainingcoversthecampaignyears. Theguarantee’shypothesisexcludesthatcase(§4.5). Thelanguage-model
arms’ real-data results are therefore read as replay outcomes. Appendix A maps each threat to its answer.
4 The referee
The referee answers three questions about every candidate factor. Does this candidate have any edge at all?
Which candidates can be admitted while keeping false admissions low among all candidates ever submitted?
Once deployed, has a factor’s edge fallen below the level that pays for its trading?
A classical test cannot answer them here. It fixes its sample size in advance and is read once. The referee is
read every day over a candidate set that grows as long as the system runs.
One idea answers all three questions: treat evidence as capital in a betting game. The game is fair or
unfavourabletothecandidatewheneverthecandidateisinfactnull. Capitalinsuchagamecannotbeexpected
togrow. Therefore,thechancethatiteverreachesahighlevelissmall,wheneveronelooks. Thefirstquestion
becomes a bet that one candidate’s edge is positive. The second becomes a rule for how high each candidate’s
capital must climb when many candidates are betting. The third becomes a bet against a deployed factor. Its
capital grows only when the edge is gone.
The section follows that order. Section 4.1 states the one property of betting capital underlying all three
procedures. Sections 4.2, 4.3 and 4.4 build those procedures. Figure 2 shows one candidate’s life under them.
Section 4.5 gives the condition under which an agent in the loop leaves all three intact.
4.1 Evidence as capital
A test supermartingale measures evidence and stays honest when read every day. Write(Gt)for the global
filtration of §3, containing everything known at the close of dayt. A nonnegative processW with W0 = 1
is atest supermartingalefor a null hypothesisH0 if EH0[Wt | Gt−1]≤W t−1. Under the null, tomorrow’s
expected capital is at most today’s.
Two consequences support everything that follows. The first isoptional stopping:EH0[Wτ ]≤1 for any
stopping timeτ. Such a stopping time is any rule that uses only the past to decide when to stop. Capital read
at a data-dependent moment remains a fair quantity, called ane-value. The second isVille’s inequality(Ville
1939):P H0(∃t:W t ≥1/α)≤α. A null candidate’s capital reaches1/αwith probability at mostα.
4.2 One candidate: a bet on the post-submission stream
The first procedure tests whether one candidate has an edge. It plays the game of §4.1 on that candidate’s post-
submission stream. Candidatei’s outcomes are its daily rank-ICXt ∈[−1,1] on the days after submission.
The null says it has no edge:H0 :E[X t | Gt−1]≤0 . Given everything known the day before, its expected
rank-IC is at most zero. Each day, the referee stakes a fractionλt of the candidate’s capital on a positive
6

0.0
0.1Daily Rank-IC
δ
Edge decays
(a) The Stream the Referee Scores
True Factor (63-Day Mean) Null Factor (63-Day Mean) True Edge
101
103
105
107
109
Capital (Log Scale)
1/α
Admitted
(b) The Admission Bet: Capital Reaches 1/α or Never Does
True Factor
Null Factor
0 500 1000 1500 2000 2500
Trading Day
100
101
102
103
Detector Statistic
A
Retired
(c) The Retirement Detector, Started at Admission
Figure 2:One candidate’s life under the referee, on a simulated stream (an illustration of the mechanics, not a reported
result). Top: the 63-day mean of the daily rank-IC of a factor whose edge is0.03 and then decays to zero, and of a
null factor, with the viability thresholdδ. Middle: the capital of the admission bet on a log scale. The true factor’s
capital reaches the single-candidate bar1/α drawn here (the bar as run, overNv slots, is higher, §4.3) and the factor is
admitted; the null factor’s capital never does. Bottom: the retirement detector, started at admission, stays flat while the
edge is intact and climbs toAonce the edge has decayed.
outcome,
Wt =
Y
s≤t

1 +λ s Xs

, λ s ∈[0, λmax,s]G s−1-measurable, λ max,s <1.
Therefereefixes λt beforeseeing Xt. Thenullmakestheexpectedvalueof Xt atmostzero. Theseconditions
make W a test supermartingale. The cap onλ keeps every product factor positive. The capital therefore can
never be lost outright.
The bet is fair to a null candidate, however cleverly it was chosen, under one proviso. The proposer’s choice
must use no information about the post-submission stream. This condition holds in a live run, whatever the
proposer learned from the past. It may fail in a historical replay. A model may hold such information if its
training window covers the stream. For the language-model arms, the guarantee therefore applies to live
deployment. The replay results are outcomes (§9).
7

Every feasible bettor is slow at realistic noise levels because noise sets the speed. An alternative with
conditionalmean µ >0andvariance σ2 hasexpecteddailylog-capitalgrowthofabout λµ−λ 2σ2/2. Growth
is largest at the Kelly stakeλ∗ =µ/σ 2. Capital then reaches1/α after roughlyln(1/α)·2σ 2/µ2 days. Daily
rank-IC on a 500-stock universe hasσ≈0.12 . For relevant edges (µ= 0.02 –0.03), the Kelly stake exceeds
the no-bankruptcy cap. We use the plug-in aGRAPA stake (Waudby-Smith and Ramdas 2024), capped at a
fractionϕ= 0.8of that bound:
λt = clip
 ˆmt−1
ˆvt−1 + ˆm2 t−1 ,0, λmax,t

,
Here, ˆmt−1 and ˆvt−1 are the running mean and variance ofXs over s < t. The cap fraction, not the bettor,
sets the wait (Appendix B).
Autocorrelation changes which null makes the bet fair, so the referee whitens the stream. A factor with a
marginaledge of exactly zero has a positive conditional mean under AR(1) noise after a positive shock. A bet
that conditions on the past exploits those days. The raw-stream referee admits 6.0% of such factors over ten
years atρ= 0.2 and 15.4% atρ= 0.4 , against a nominal 5%. The referee therefore bets on thepredictably
whitenedstream
˜Xt =X t −ˆρtXt−1,ˆρ t =shrunk, capped estimate fromX<t, λ max,t = ϕ 1 + ˆρt ,
against E[ ˜Xt | Gt−1]≤0 . Every quantity isGt−1-measurable. The supermartingale argument therefore holds
for this null. The theorem gives no finite-sample bound for the marginal null. Thus, control of the marginal
edge is measured, not proved. Whitening restores false-admission rates of 1.8, 2.0 and 2.4% atρ= 0,0.2,0.4
(Table 7, Appendix B).
Admission certifies an edge. Whether that edge pays for its own trading is a separate question. The registered
threshold δ addresses that question. A factor with edgeµ earns aboutκµ per day gross. Here,κ converts
one unit of daily IC into return. It pays2c·TO per day for per-side costc and one-way turnoverTO. The
break-even edge is
δ= 2c·TO κ .
κ is theaverageconversion from daily IC into gross return. We use0.018 (§5.2). The break-even differs
across families by an order of magnitude because turnover does. Atc= 15 bp, it is 0.010 for value, 0.012 for
liquidity, 0.017 for volatility, 0.031 for momentum and 0.074 for short-horizon reversal.
One δ across these families is therefore asignal-quality floor, not a per-family economic threshold. It was
registered as a single value,δ= 0.015 , before the runs. It is the null of the retirement detector. It defines
the realised label of §3. It is the execution objective at the shortest hold (§5). The execution layer decides
whether a certified factor covers its own costs.
4.3 Many candidates: online e-BH over a frozen universe
The second procedure decides which candidates to admit when many are available. The rule is Benjamini–
Hochberg with capital instead ofp-values. Its objective is the false-discovery rate over everything ever
admitted. The universe is frozen atNv slots per epoch. Each candidate occupies its own slot with weight
8

γc =w v/Nv, P v wv ≤1. The admitted set on daytis
Rt =
n
c:E c(t)≥ 1 k∗ t α γc o , k ∗ t = max n k: #  c:E c(t)≥ 1 kαγc 	 ≥k o ,
where Ec(t)isthecandidate’scapital,frozenatitsadmission-dayvalue(Fischeretal. 2024). Morecandidates
clearing a bar lowers the bar each faces. Appendix A works a two-candidate example.
The guarantee requires no assumption about dependence between candidates. Ifc is admitted, 1{c∈
Rt}/|Rt| ≤αγcEc, which isαEc/Nv at wv = 1. Taking expectations under each null and summing over
the null candidates givesFDR≤α (Wang and Ramdas 2022). The guarantee holds at every stopping time
because stopped capital is an e-value. Frozen values never fall, so admissions are never revoked (Wang et al.
2025; Heide 2026).
In the runs, the bar is far above the single-candidate1/α. We setα= 0.05 and wv = 1, using one epoch
with Nv = 2000 slots. A campaign uses about 490 slots. An expired or retired candidate keeps its slot, so
every admission draws on the same budget. The first admission requires capital ofNv/α. Thek-th requires
Nv/(kα).
The bar’s height sets the wait. The noise determines that wait. Combining the bar with the growth rate of
§4.2 gives the expected wait for thek-th admission,
T≈ ln

Nv/(kα)

λµ−λ 2σ2/2 , T≈ln

Nv/(kα)

· 2σ2
µ2 at the Kelly stake.
At the run parameters, the first admission of a factor with edge0.03 takes about 546 days. At the viability
threshold, edge0.015, it takes 1434 days, versus 1356 for an uncapped Kelly bettor. The cap costs almost
nothing near the threshold (Appendix A works the three cases). Thus, no better bettor can shorten the wait
near the threshold. A factor whose edge sits atδ needs more than five years of evidence. A campaign lasts
seven to ten.
Twoconsequencesoftheruleshapetherestofthepaper. Aresubmittednear-copyopensanewcandidatewith
its own slot. Repetition therefore cannot raise the false-discovery rate aboveα. It only spends the proposer’s
slots. A weak submission does not dilute the other candidates. The proposer’s scarce resources are therefore
slots, compute and calendar time. A bandit allocates these scalar quantities well (§6). The engine can also
merge near-duplicates into a cluster (Vovk and Wang 2021). The reported experiments do not merge.
4.4 Retirement: the e-detector
The third procedure decides when a deployed factor’s edge has gone. A desk needs a rule that rarely retires a
healthy factor but reacts within months when the edge is really gone. Real decay is gradual (McLean and
Pontiff 2016), so its start has no ground truth.
The detector plays the betting game of §4.1againstthe factor. It uses the viability threshold as the null.
The retirement null says the factor remains viable on the whitened stream:H ret 0 :E[ ˜Xt | Gt−1]≥δ t
with δt =δ(1−ˆρ t). The test bets the other way, onYt =δ t − ˜Xt. Capital grows only while the edge is
demonstrably below the floor. A new e-processW (j) starts every dayj after admission because decay can
begin on any day. The statistic is their sum:
Mt =
X
j≤t
W (j) t , τ A = inf{t:M t ≥A}.
9

The restarts make the detector responsive. A single e-process started at admission would dilute new evidence
with the factor’s healthy period.
The guarantee concerns the average run length. EachW (j) is a test supermartingale under the retirement null,
so Mt −t is a supermartingale. Optional stopping then givesEH0[τA]≥A for anyA, nonasymptotically
and without i.i.d. assumptions (Shin et al. 2024). The same inequality has the finite-horizon formP(τA ≤
t)≤t/A . It is vacuous over a ten-year campaign atA= 1260 . The false-retirement rates below are therefore
simulation results, not consequences of the bound.
The stake targets the decay one wants to catch and is not fitted to the data. A stake fitted to a healthy factor’s
drift is near zero. Every capital then stays near one,Mt ≈t climbs linearly, and every healthy factor alarms
within a bounded horizon. It is the Kelly bet against the design alternative “full decay to zero edge”,
λt = clip
 δt
ˆσ2 t−1 +δ 2 t ,0, λmax,t

,
with ˆσ2 t−1 the running variance. Each start then has negative expected log growth under the alive null. As a
result,M t plateaus instead of climbing.
The thresholdA∗ = 1260, five years of trading days, was registered before the runs. Closed-form economic
designs for memory-type charts are known to fail unchecked (Lorenzen and Vance 1986; Ahmadi-Javid and
Ebadi 2021). The harness therefore checks the delay and false-retirement rate by simulation. On synthetic
decay, the e-detector’s median delay is 204–322 days by decay shape. This delay matches a Monte-Carlo-
calibratedCUSUM.Thee-detectorneedsnocalibrationstep. Itsfalse-retirementrateonten-yearalivestreams
is 0.5–1.5% atρ≤0.2. Atρ= 0.4, the rate is 8.5%.
Each factor keeps its own detector and threshold whenK factors are monitored at once.Error-over-patience
(Dandapanthula and Ramdas 2025), the library-level analogue of the false-alarm rate, is bounded byK/A∗
under this per-stream rule. Decay shared by a whole family is read fromfamily detectors. Each is the mean of
the members’ detector statisticsMt. They inform diagnosis and never retire a factor by themselves.
4.5 What an agent in the loop cannot break
The three guarantees survive an adaptive proposer if the proposer cannot reach three things. It cannot reach
bet sizing, which happens before the day’s outcome is seen. It cannot reach the scoring data, which all arrives
after the candidate was proposed. It cannot change the set of possible hypotheses within an epoch. Under
these conditions, the proposer’s behaviour does not enter the argument.
Proposition 1 (validity for any proposal policy).The controller may be any policy (scripted, bandit,
LLM-driven or self-modifying) that satisfies four conditions:
(i) the referee’s betting fractions and cluster weights stayGt−1-measurable;
(ii) each candidate is bet on post-submission data only;
(iii) the library stays frozen within an epoch;
(iv) each candidateiis chosen with no information about its post-submission outcomes beyondGsi−1.
Suppose also that each candidate’s null is the one its bettor scores. Every merge must also use weights fixed
in advance. The FDR guarantee of admission then holds at every stopping time. The run-length guarantee of
retirement holds for every deployed factor.
That hypothesis uses the whitened conditional null of §4.2. In words, a null candidate’s expected whitened
rank-IC is at most zero, given everything known the day before.
10

Proof sketch.Conditions (i) and (ii) make each candidate’s capital a test supermartingale with respect to
G. Condition (iv) preserves this property for a candidate selected by the proposer. The selection carries no
information about the increments used to score the bet. Weights fixed in advance make a merged capital
an e-value. Condition (iii) keeps the hypothesis universe fixed and finite within each epoch. Thus, stopped
e-BH (Wang et al. 2025) and dynamic e-closure (Heide 2026) apply. The detector’s guarantee is a per-stream
inequality independent of the policy. The proposition follows from the cited results and is not a new theorem.
Its value is to rule out one possibility: that an endogenous proposal process breaks validity.
The proposition fails under one named condition,foretelling. The engine guards against it. Foretelling means
sizing a bet with knowledge of where another candidate’s stream is about to move. Each bet can then be fair
onitsowninformation. Yetthemergedcapitalcanhaveexpectationaboveone. Thecounterexampleof(Wang
et al. 2025) hasE[M] = 1.25. The engine enforces the alignment invariant of §3. A unit test reproduces the
counterexample and confirms that the invariant removes it. The invariant cannot verify the conditional-mean
assumption itself. The synthetic world tests that assumption where it holds by construction.
The proposition also defines the boundary between the agent and the referee. The trust kernel comprises the
referee, thelibrary, thepoint-in-timedatalayer, theappend-onlydecisionlogandthecostmeter. Thesefrozen
components cannot be mounted, patched or intercepted by the controller. Everything else (probes, memory,
allocation and diagnosis policies) is a swappable agent surface. It may evolve freely.
5 The execution layer
The referee certifies a statistic. A book earns money from positions. The execution layer sits between them.
Its one parameter sets how long to hold a certified ranking. Its one decision is whether to hold the ranking at
all.
5.1 Persistence, and the edge of anh-day hold
How long to hold a ranking depends on how fast its predictive power fades. The referee does not measure this
decay. A rankingSt−1 known at the close of dayt−1has adecay curve
IC(k) =E

rc

St−1, rt+k−1

, k= 1,2, . . .
where rc is the cross-sectional rank correlation. The referee scoresIC(1). IC(k) for k >1 is the same
ranking’s value on thek-th day of the hold. A flat curve has the same daily IC at everyk. Thus, a daily
certificate does not penalise slowness. A steep curve may clearδyet fail to cover the trading imposed by its
decay.
The objective is the net return of a hold. Asleeveis a single factor’s own long–short portfolio. It is long the
top fifth and short the bottom fifth. A sleeve re-formed everyhdays earns the curve’s average over the hold.
It also pays for re-formation:
net(h) =κ IC 1..h −2c τ(h), IC 1..h = 1 h hX k=1 IC(k),
where τ(h) is the sleeve’s one-way turnover per day at that frequency. Settingnet(1) = 0 recovers δ=
2cTO/κ. Thus,the viability threshold is the execution objective at the shortest hold.
11

5.2 Estimatingκ: why the conversion is a market constant
The objective needs the conversion rateκ. We fix it at one market-level value,¯κ= 0.018. The relevant rate is
theaverage, E[gross]/E[IC]. It is0.016–0.019 for the four families that carry the book. Theslopeof daily
gross return on daily IC is about three times larger. It measures the rate on high-dispersion days. The average
cannot be estimated per sleeve. A per-window ratio divides by a 250-day mean IC whose standard error is the
size of a real edge. A first pass that estimated it per sleeve inverted the shelving decisions (Appendix B).
5.3 The decision, and its rate limit
The decision rule is a deliberately slow grid search. The sleeve’s holding frequency is chosen from five desk
frequencies. Each is scored on the trailingW days using only inputs known at the decision date. The search
runs on first deployment and then at most once everyB= 250 trading days. An accepted change moves at
most one grid step. The sweep overB finds no consistent winner. The pre-stated rulenever worst, least churn
therefore selects 250 (Appendix B).
A factor that cannot pay at any frequency is not traded. Ifmaxh cnet(h)≤0 , the factor stays certified but is
shelved. This second threshold is deliberately kept apart fromδ. The certificate needs one statistic on one
daily stream. Tradability is family-specific becauseτ(h)differs across families by an order of magnitude.
5.4 Execution neutrality
Proposition 2 (execution neutrality).Let the execution layer be any policy mapping the admitted set and
data up tot−1 to positions att. Then, (i) no guarantee of §4 depends on it. (ii) Any book can be recomputed
from the recorded decision log without re-running the agent.
Proof.
(i) The e-processes depend on candidate streams and predictable stakes. The admission and retirement
rules depend on the e-processes. The execution layer is downstream of all of them. It enters no bet,
weight or threshold.
(ii) Byconstruction, thecontroller’sstate Zt excludesthebook(§6). Therefore, theagent’sactionsequence
depends only on the referee-side history. The book is a deterministic function of that history.
Part (ii) makes the experiment affordable and auditable. The 540 cells of §8 were recorded once, then
re-booked under a new execution layer at no cost. All 220 LLM cells reproduced their referee-level metrics
exactly.
6 The controller ladder and the perception probe
The three controllers differ in their capabilities, not their inputs. All use the same library, budget, and numeric
family statistics. A controller is a policyπ(at |Z t) over actions{mine(f, θ),respond(alarm),probe,idle} .
Its stateZt includes family statistics, the referee’s diagnostics, open candidates, and paused families. For the
LLM, it also includes unstructured context and memory. Each rung adds a capability to the rung below (Table
25, Appendix D).
• C0 round-robinignores Zt. It cycles through families in a fixed order and replaces each retired family
with a new draw.
12

Intelligence Without Governance
LLM Controller ×
Leaky or No Referee
(Today’s Agentic Miners)
Governed Intelligence
LLM Controller × Frozen Referee
(This Paper’s Top Rung)
Neither
Round-Robin × No Gate
(A Fixed IC Checklist)
Governance Without Intelligence
Script or Bandit× Frozen Referee
(Scripted Proposers)
Governance: Who Judges
Intelligence: Who Proposes
Figure3:Thefactorialasaquadrant. Everycellismeasuredwithcommonrandomnumbers,sotheeffectofgovernance
(columns) and of intelligence (rows) can be read off separately. The interaction, what the agent adds only when the
referee leaks, is a measured quantity.
• C1 discounted UCBis a non-stationary multi-armed bandit over families. Each family’s reward is its
discounted admission count minus retirements per submission.
• C2 LLM controllerplays three roles under a fixed scaffold.Direction: allocate the next period’s
submissions across families usingZt and each family’s economic profile.Diagnosisafter a retirement:
label the cause or escalate.Probe authoring: write, sandbox-test, and mount a perception probe. The
probe never enters admission or retirement inference. It therefore carries no multiplicity cost.
Thebanditisastrongallocationbaseline. ThisindicateswheretolookfortheLLM’scontribution. Admissions
donotdiluteoneanother(§4.3). Thedirectionrolethereforeallocatesscalarresources,whichabandithandles
well. The LLM has only two inputs unavailable to the bandit: retirement reasons and family profiles. Any
difference must therefore come from diagnosis and instrument-making.
7 Experimental design
7.1 The factorial
The design crosses who judges with who proposes, and every cell is run. Four referee arms span governance.
Three controllers span intelligence (Figure 3). Three words recur. Anarmis one factor setting (a referee, a
controller). Acellis one run of one arm combination with one model, start year and seed. Acampaignis a
cell’s walk-forward. It lasts seven to ten years, depending on the start year.
The governance axis compares one valid referee with three controlled violations. Thefrozen refereefollows
the procedure in §4. Eachleakyarm keeps the rest of the pipeline intact. It breaks one assumption of §4.5 in
the way a common practice does:
• Peeking:aone-sided t-testusesthepost-submissionmean. Itischeckedeverydayafter60observations
and admits at the firstp≤α(the practitioner’s rollingt >1.65rule). It breaks optional stopping.
• Adaptive threshold:the e-process remains, but the wealth threshold relaxes with candidate age,
α−1e−age/τ. It breaks Ville’s fixed threshold.
• No gate:every candidate is admitted after a fixed incubation of 126 trading days, as today’s miners do.
It tests nothing.
The leaky arms support two contrasts. Comparing a leaky arm with the frozen arm under one controller
13

measures what the leak lets through. Comparing two controllers within one leaky arm measures how much
apparent adaptive-controller skill comes from the leak.
The intelligence axis has the three controllers of §6. On real data, the LLM controller uses three model
families. That quadrant is a replay. A language model trained on the campaign years falls outside condition
(iv) of Proposition 1. It therefore reports what the package achieved and is not an instance of the guarantee.
The referee’s design choices were settled through ablation on synthetic streams before any paid run (Table 7,
Appendix B).
7.2 One analysis, three environments
Every comparison is a paired difference between two arms that saw the same world. Within one model family
and one start year, arms on the same seed share common random numbers: the same world and candidate
draws. Their metric difference is one observation, and there are five seeds. The test is a two-sided paired
t-test on those five differences. Holm correction covers the tests within one model family. Families are never
pooled. An effect is reported as “kofnfamilies”. Appendix A states the conventions behind every table.
The synthetic world isolates the mechanism, because truth is planted.It has four families with true-factor
proportions 0.50/0.25/0.10/0.05 and AR(1) noise withρ= 0.2 . Every admitted factor lowers the share of
true factors among its family’s later candidates. One family has a mid-campaign regime break. A campaign
lasts 1260 days, with four submissions every 21 days. The design is two LLM families× four referee arms×
three controllers×five seeds.
The probe environment measures the one agent capability we claim: writing a diagnostic instrument for
a fault nobody listed in advance.An episode shows the controller a deployed factor whose series has one
hidden fault. The controller must choose an intervention. The score isintervention regret: the value of the
best intervention less the value of the chosen one. The five fault types are held out, with twenty episodes each.
They are blind spots of the three instruments in the fixed diagnosis menu. The probe-authoring arm may write
its own instrument, test it in a sandbox, and read it before choosing. Seven model families are sampled from a
written frame (Appendix D).
The real-data world tests which results survive ten years of prices.It is built point in time from CSI 500
constituents, 2015-01 to 2026-08 (Appendix E). The four-family library contains the technical families:
momentum, short-horizon reversal, volatility and liquidity. The nine-family library adds value, size, quality,
growth and investment. Campaigns start in 2016–2019, with five seeds each and four submissions every 21
days. A candidate’s realised label indicates whether its post-submission mean rank-IC is at leastδ= 0.015.
CoverageiscompleteforthescriptedcontrollersandpartialfortheLLM(Table23,AppendixD).ThreeLLM
families run the frozen referee on both libraries. One family runs the three leaky referees on the four-family
library. The other two run its no-gate arm. Round-robin and bandit baselines run every arm at no cost. That
makes 540 cells: 320 baseline and 220 LLM. Every LLM call is recorded, so every cell replays at zero cost
(Proposition 2).
7.3 What is fixed before the data, and what is not
Every input is sorted by when it was fixed.
• Fixed in advance and never tuned:the levelα, the viability thresholdδ, the run-length targetA, the
cap fraction, the incubation of the no-gate arm, the parameter grids, and the design and analysis plan.
• Walk-forwardbyconstruction:everyrefereeverdict,everycontrolleraction,andeverysleevedecision
14

by the execution layer.
• In sample:the conversion constant¯κwas measured once over the whole panel. The execution layer
was constructed after a first pass over the recorded cells (Appendix B).
There is no held-out period beyond the walk-forward, and there is one market. A second market needs data,
not model calls. It is the natural next study.
7.4 The canonical book
The canonical book is the portfolio construction used for every reported cell.Its numbers are in sample
with respect to the execution layerand make no out-of-sample claim. The referee-side results are computed
before any book exists (§5.4). The construction has four steps.
• Sleeves.Each deployed factor forms a quintile long–short sleeve with one unit notional on its own
calendar.
• Calendar.The execution layer selects each sleeve’s holding frequency from five desk frequencies. It
scores them on the trailing 250 days withc= 15 bp and¯κ= 0.018. A sleeve that cannot pay at any
frequency is shelved.
• Aggregation.Tradedsleevesarecombinedwithequalnotional. Thebook’sone-wayturnoveriscapped
at 25% per day. An index leg hedges its index beta.
• Costs.Costs are 15 bp per side on stocks and 5 bp on the hedge. They are charged on position changes.
Each book has three reported statistics. The CSI 500 index beta shows what the hedge leaves. A three-factor
alpha follows the spirit of CH-3 (Liu et al. 2019) and uses Newey–Westt-statistics (Newey and West 1987).
The deflated Sharpe ratio (Bailey and López de Prado 2014) discounts for the 108 book-level groups in this
study. Sharpe ratios use 244 trading days a year. Appendix A defines each statistic operationally.
8 Results
Three results carry the paper. The referee, not the controller, sets the number of false admissions (§8.1, §8.4,
§8.5). The language model finds more true factors than a script and about as many as a bandit. Its clearest
contribution is writing its own probes (§8.2, §8.6). The certified portfolio trails the ungated one because a
daily certificate arrives late. It also trails because the family that pays least clears the certificate fastest (§8.7).
Two controls (§8.3) rule out the two artefacts a reviewer would first suspect.
8.1 Synthetic factorial: the referee decides false admissions; the controller does not
Question.With truth planted, who determines the number of false factors admitted?Answer.The referee
alone (Table 8, Appendix C).
False admissions follow the referee arm, regardless of the controller. Under the frozen referee, both LLM
families admit0.000 false factors per submission. Under the three leaky referees, the rate is0.26–0.85 for
script, bandit and LLM alike (2 of 2 families). The guarantee bounds the expected realised false-discovery
proportion. This proportion is0in every seed under the frozen referee and0.75–0.95under the leaky ones.
The guarantee does not reduce controller yield. Under the frozen referee, the three controllers have the same
yield (0.095 round-robin, 0.096 bandit, 0.096 LLM, ±0.002). Yield is lower under the leaky referees. Every
admitted factor lowers the share of true factors among its family’s later candidates. A referee that admits
15

everything spoils the families it draws from. The no-gate arm’s yield is0.042 against the frozen referee’s
0.095.
Anattackingcontrollerextractsfalseadmissionsonlyfromaleakyreferee. Hiddenretriesresubmitunadmitted
candidates under new identifiers rather than drawing fresh ones. They extract+0.027 false admissions per
submission froma peeking referee and+0.009from anadaptive-thresholdone, andnone from thefrozen one.
8.2 Probes: the agent as instrument-maker
Question.Is there a lifecycle task that the agent can do but a bandit cannot?Answer.It can write its own
instruments. This has a clear effect in half of the evaluable model families and causes no harm in the rest
(Table 9).
Thecomparisonusesthefixeddiagnosismenubecauseabanditcanonlychooseamonglistedactions. Itcannot
write a new one. Every arm sees the same episodes, so each episode provides a paired contrast. Authored
probes lower intervention regret by0.388, 0.248 and 0.233 in three families. Each result is significant after
Holm correction over the six evaluable families. In the other three, the differences are−0.067, −0.021 and
+0.074 and cannot be distinguished from zero. One of the seven sampled families never produced a probe
within its budget and is inevaluable.
8.3 Controls
Two artefacts could produce the LLM’s results without skill: what it remembers and randomness in its
decoding. Neither does.
The memory control varies what the LLM may remember. Six memory arms (none, working, episodic, full,
shuffled, oracle) run under the frozen referee. Each is compared with the full-memory arm. No difference is
detected. After Holm correction, 0 of 10 tests are significant. Every arm is within±0.0025 yield of the full
arm.
The decoding control tests whether rerunning the same model on the same history changes its decisions. A
same-policy fork replays a recorded cell prefix, then lets the same model continue live. In 5 of 5 cells, the
fork reproduces every outcome-level metric of the original.
8.4 Real data: the referee
Question.Does the synthetic result survive ten years of real prices?Answer.Yes. The referee still sets the
number of realised false admissions. On real data, the size of this effect depends on who proposes (Table 2;
Figure 6, Appendix C).
Table 2:Real data, four-family library: realised false admissions per campaign and realised yield per submission by
referee arm and controller. Means cover four start years×five seeds; the LLM column is one model family.
Referee
False Adm.:
Round-Robin Bandit
LLM
(Gemini) Yield: Round-Robin / Bandit / LLM
Frozen 11.7 9.4 11.7 0.40 / 0.47 / 0.47
Peeking 86.2 38.4 37.4 0.41 / 0.50 / 0.55
Adaptive Threshold 105.2 51.0 43.5 0.39 / 0.44 / 0.48
No Gate 196.0 189.8 78.0 0.37 / 0.37 / 0.59
16

The proposer matters only when the referee leaks. Moving from round-robin to the LLM changes the count
by a factor of2–2.5 on the leaky arms. It does not change the count on the frozen one. The bandit halves the
count under peeking and adaptive threshold. It leaves the count unchanged under no gate.
The two kinds of referee also admit different kinds of false factor. This difference matters for the book. A
false admission with a negative realised edge loses money for as long as it is held. One with a positive edge
below δ merely fails to pay for its trading. The frozen referee’s realised false admissions are all of the second
kind. None of its 100 four-family cells has an admitted factor with a negative realised edge. The detector had
retired every false admission before the campaign ended. Under round-robin, the leaky referees admit 10.8,
32.0 and 90.8 negative-edge factors per campaign. Under the LLM, they admit 1.2, 6.0 and 15.5 (Table 10).
The ordering survives every label we tried. The size of the ratio depends on the label. Moving the threshold
from 0.010 to 0.020 changes every count. It does not change the ordering (Table 11). Judging each admitted
factor only on post-admission days removes the overlap of §3. On that label, the frozen referee’s false
admissions under round-robin rise from 11.7 to 17.6 per campaign. The leaky referees’ false admissions
barely move. Its advantage is then 5–11× against 7–17× on the registered label. Under the LLM, it is
2.6–4.9×against 3–7×(Table 12).
Against each family’s own break-even, the ratio shrinks to two- to threefold. Relabelled that way, the frozen
referee has 96.0 false admissions per campaign under round-robin. The three leaky referees have 180.4, 197.4
and 276.2. These counts arise because short-horizon reversal has a break-even of 0.074 (§4.2). The headline
ratio is therefore a statement about the registered label. The frozen referee certifies a statistical edge. Whether
that edge pays is the execution layer’s question (§8.7).
8.5 Real data: a legitimate comparator
Question.The three leaky referees are known shortcuts. What does the anytime-valid referee add over a
patient desk that waits and corrects for multiplicity?Answer.For clearly good or bad families, it adds a little
accuracy and some yield. For many families with a small positive edge, it gives a fourfold gain in accuracy.
That gain comes from the height of its bar (Table 14, Appendix C).
The comparator is the procedure a careful desk would run without anytime-valid tools. It tests each candidate
once, 500 trading days after submission (the frozen referee’s median wait). It uses a one-sidedt-test on
the whitened stream. It applies Benjamini–Hochberg at 0.05 every time a window closes. It runs as a
counterfactual program on the frozen cell’s recorded submission stream.
Onthefour-familylibrary,thepatientdeskcomesclose,atsomecostinyield. Underround-robin,the500-day
comparator admits 16.4 false factors per campaign against the frozen referee’s 11.7. Both are far from the
86–196 of the leaky referees. Its yield is lower, at 0.358 against 0.403. Its wait is a fixed 500 days against a
median of 439. The frozen referee lets strong factors through early.
On the nine-family library, the comparator is four times less accurate because its bar is lower. It admits 41.4
false factors against 9.8. After the decision, 0.33 of what it admits is false, against 0.12. Both procedures test
a zero edge, and both are valid for it. At-test on 500 days has power against an edge of0.01. This edge is
positive and below the viability threshold. The fundamental families supply many such factors. The frozen
referee’sbarof Nv/(kα) isfarhigher. Therefore, onlystrongfactorsclearitwithinacampaign. Itsselectivity
and its wait are the same knob (§4.3).
The evidence therefore supports the claim that the judge must be a valid, multiplicity-corrected statistical
procedure. Eithervalidprocedureadmitsseveraltimesfewersub-thresholdfactorsthantheshortcuts. Anytime
17

validity then adds three things. The verdict can be read on any day without choosing a horizon in advance.
Strong factors pass early. The guarantee also holds for a proposer that adapts to the verdicts. The comparison
has one limit. The candidate sequence is the one the frozen referee produced. Therefore, the comparison
isolates the referee and is not a re-run campaign.
8.6 Real data: the controller
Question.What does a language model add over a script or a bandit, given a valid referee?Answer.It finds
more true factors than a script and about as many as a bandit (Table 3). It admits fewer false factors than
either only when the referee is broken (Table 10).
Here is how to read Table 3. Each entry contains four signs, one for each start year. Each sign shows the
paired difference between the LLM controller and a baseline. The number in parentheses counts the starts
where that difference is significant after Holm correction. Tables 21 and 22, Appendix C, report paired effects
with standard errors.
Table 3:Real data, frozen referee: signs of the paired difference between the LLM controller and baseline across the
four start years, by model family. Parentheses show the number of starts significant after Holm correction within the
family. Families are never pooled.
Library Contrast Metric DeepSeek Gemini GPT
Four-Family LLM−
Round-Robin
Yield+ + ++(4/4)+ + ++(3/4)+ + ++(2/4)
Four-Family LLM−Bandit Yield+ +−−+− −− − − −−
Nine-Family LLM−
Round-Robin
Yield+ + ++(4/4)+ + ++(3/4)+ + ++(1/4)
Nine-Family LLM−Bandit Yield+ + +−+ + +− − − −−(3/4)
Four-Family LLM−
Round-Robin
False Adm.+ + +−(0/4)−+ ++(0/4)+ + ++(0/4)
Nine-Family LLM−
Round-Robin
False Adm.+ + ++ + + ++ + + ++
The LLM finds more true factors than round-robin and no fewer false ones. Its realised yield is higher in six
of six family× library settings. The difference is positive in every start year. Its false admissions under the
frozen referee are at or slightly above round-robin’s (11.7 to 13.3 against 11.7). This occurs because it sends
more submissions to productive families. The increase is Holm-significant in no start for any family.
The balance against the bandit is level. It depends on the library. On the four-family library, the LLM is level
or behind in most starts. On the nine-family library, two families lead in three of four starts. One loses in
every start (three of four significant). That library has five barren families, which punish an allocator that
keeps sampling them.
Under leaky referees, the LLM’s judgement replaces part of the missing referee. It reduces realised false
admissions relative to round-robin on all three leaky arms (Holm 4/4 each; three model families of three on
the no-gate arm). Relative to the bandit, it does so only under no gate (4/4). There, the bandit’s admission
reward stops discriminating, while the LLM still reads profiles and retirements.
A period split suggests that the LLM’s advantage over the bandit is a prior that data overtake. We split every
campaign at 2020-01-02. This is the first trading day of the period when the fundamental families lose their
edge in this market. Against the bandit, the LLM leads before the split and trails afterward in all three model
18

families(Table17,AppendixC).Earlyinacampaign,thebandithasnoadmissionstolearnfrom. TheLLM’s
family profiles are therefore informative. Later, the bandit has learned what the profiles said. This is an
interpretation, not a test. It does bear on leakage. A model that had seen the period would be expected to gain
most after 2020. The sign is the other way.
8.7 Real data: the portfolio
Question.What does a portfolio of certified factors earn, and what does the certificate cost an investor?
Answer.The certified book does not lose money at the registered cost. Its alpha cannot be distinguished from
zero. Its Sharpe ratio net of costs is below that of a book that admits everything. The gap has two causes: a
horizon mismatch and the wait. Neither is a verdict on the certificate.
The certified book earns money net of the registered costs, but not demonstrably. The four-family library
has twenty frozen-referee groups of five seeds. Their net Sharpe is+0.33 to +0.50. Against the study’s 108
groups, the deflated Sharpe ratio is0.49–0.69. This is far from the level near one that survives a search of
that size. Alpha is+0.25 to +1.13 bp per day. Its Newey–Westt never reaches one in any group. Index beta
is−0.07to−0.08. The nine-family library gives the same picture.
The ungated book ranks first in every start year. Its net Sharpe is+0.59 to +0.77, versus the frozen referee’s
+0.33 to +0.50. The two leaky referees fall between them. The order survives when every book is restricted
to 2020 onwards. It also survives re-costing (Appendix B).
Thefirstcauseofthegapisahorizonmismatch. Theungatedbookholdsmomentum,whichadailycertificate
cannot see. The per-candidate ledger records each factor’s own sleeve returns for every day it is held. Thus,
the two books can be compared line by line (Table 4). The two books earn about the same per day from
volatility and liquidity. Momentum creates the large difference. The ungated book held 892 momentum
sleeves at+1.69bp per day. The frozen book held six.
The referee is right about momentum on its own terms. It is wrong for the book. Momentum’s daily rank-IC
is 0.001, an order of magnitude belowδ. It therefore cannot be certified within a campaign. But momentum
is a slow factor in this market. Its information coefficientriseswith the holding day, from0.001 at one day to
0.009 at sixty-three. It pays only when held a month or longer (Figure 4). A library that certifies one-day
predictive power cannot certify momentum. A library that certifies nothing includes it incidentally.
Table4:Per-familysleeveeconomicsunderthecanonicalbook, usingtheround-robincontrollerandfour-familylibrary.
Results pool five seeds from the 2016 start. They report sleeves ever held, the share shelved, and each family’s daily
earnings while held,gross of their own trading costs. Re-formed daily, a reversal sleeve nets−19.6% per year (Figure
4).
Family Frozen: Held / Shelved / bp per Day No Gate: Held / Shelved / bp per Day
Volatility 473 / 1% /+4.05418 / 2% /+4.06
Liquidity 314 / 0% /+3.79555 / 17% /+3.96
Short-Horizon Reversal 539 / 30% /+2.26475 / 41% /+1.50
Momentum6/ 83% /−4.35892/ 44% /+1.69
The second cause is the wait. The wait counts the trading days between a factor’s submission and admission.
For an admitted true factor, its median is about 500 trading days under the frozen referee. It is 122 to 214
under the leaky referees (Figure 7, Appendix C). Figure 5 shows the wait’s effect on a book. The ungated
book begins compounding in its first year while the certified book remains empty. Once both are invested, the
two slopes are similar. The gap opens during the wait and is not earned afterwards.
19

100 101
Day k of the Hold (Ranking Formed at t − 1)
−0.005
0.000
0.005
0.010
0.015
0.020
0.025
0.030
0.035
Mean Daily Rank-IC
δ
(a) Persistence: IC(k)
100 101
Holding Period h (Trading Days)
−20
−15
−10
−5
0
5
10
Net Return, % per Year
(b) Monetisation: Quintile Sleeve at 15 bp per Side
Momentum Reversal V olatility Liquidity Value Size, Quality, Growth, Investment
Figure 4:Persistence and monetisation by family. Left: the decay curveIC(k) of a ranking known att−1 against the
return on dayt+k−1 , with the viability thresholdδ. Right: what a single-factor quintile sleeve nets per year at 15
bp per side when re-formed everyhtrading days. Reversal nets at most+0.9 bp per day at any frequency on the grid;
momentum is not certifiable at one day and pays only when held a month or longer.
0 2 4 6 8 10
Years from the Start of the Campaign
0
20
40
60
80Cumulative Net Return, %
The frozen
referee's wait
(a) Round-Robin Controller
No Gate
Frozen Referee
0 2 4 6 8 10
Years from the Start of the Campaign
(b) LLM Controller
Figure 5:Cumulative net return of the canonical book, 2016 start, seed-averaged (four-family library; left the round-
robin controller, right the LLM controller). The shaded band is the frozen referee’s wait. The ungated book begins
compounding in its first year while the certified book is still empty, and is below water until year six. The two slopes are
similar once both are invested.
The wait is expensive because it is paid in regimes, not days. In the nine-family library, 99–100% of certified
holdingwindowsarecentredafter2020-01-02. Thecorrespondingrangeis65–100%byfamilyfortheungated
pipeline (Table 20, Appendix C). In this market, the edges of the fundamental families value, quality and
growth disappeared after 2020. The certified book earns nothing from exactly those families. Waiting for
volatility and liquidity costs almost nothing because their edge is stable. A slow certificate is cheap when the
edge persists and expensive when it decays. A descriptive decomposition of the Sharpe gap agrees. Earliness
20

is its largest term on the three longer campaigns (Table 19).
Two counterfactual books test this account (Table 16, Appendix C). Both use the round-robin frozen cell’s
own candidate sequence and the world’s own accounting. The frozen book is reproduced day by day in 20 of
20 cells.
The first counterfactual switches retirement off. It shows that retirement is not what the certified book loses.
Every admitted factor is held until the campaign ends. Net Sharpe changes by+0.00to +0.01across the four
start years. Some real-data retirements are false on the realised label. Reversal factors were retired after about
838 days. Their edge had sagged to0.0145while held. It averaged0.034over the rest of the campaign (Table
18). Those false retirements cost the book almost nothing.
The second counterfactual replaces the frozen referee with the 500-day comparator. It shows that a desk with
the same patience builds a better book without being earlier. The comparator’s net Sharpe is+0.59 to +0.65,
against +0.40 to +0.49 for the frozen book. This is a paired gain of+0.12 to +0.24 in every start year. Its
factors are not admitted sooner. The mean wait is 500 days against 510. The mix differs. The comparator
admits fewer reversal factors, 72.0 against 87.2. It admits about five momentum factors, while the frozen
referee admits almost none, 4.8 against 0.5. The highest daily rank-IC reaches the bar fastest, so the bar
favours the family with the worst net economics. A referee with the same patience does not pay that cost.
Certification still buys one thing the Sharpe ratio does not show. The execution layer never sees the referee. It
shelves 13% of what the frozen referee admitted, against 26% of what the ungated pipeline deployed. More
of what the referee admits is worth trading. A portfolio Sharpe ratio is therefore not a verdict on certification
in either direction. It combines a referee with an execution layer that is blind to it. The same holds for LLM
investment agents evaluated as a whole: the capability leader is not the Sharpe leader, and the process must
be diagnosed rather than a period’s return ranked (Qu and Chen 2026).
9 Discussion and limitations
The experiments support the division of labour and show its cost. The judge must be a statistical procedure
the agent cannot touch. Every leaky referee admitted several times more false factors than the frozen one
under every proposer. No proposer closed that gap. A fixed-horizon test with a multiplicity correction is also
a statistical judge. Anytime validity adds a verdict that can be read on any day. Its selectivity is paid for in
waiting.
The proposer can be anything. A language model earns its place through jobs a bandit cannot do. It does not
allocate consistently better than a bandit. It adds three things. It reads why a factor was retired. It writes an
instrument for a fault the menu does not cover. It also holds the line when the referee leaks.
Thesplitcoststime. Thistimereflectsaninformationboundratherthananengineeringgap. Anadmittedtrue
factor waits a median of about five hundred trading days in this market. The wait scales likeln(Nv/(kα))·
2σ2/µ2. At this noise level, no bettor can certify a factor at the threshold in under five years. Only a less
noisy statistic or a lower bar shortens the wait.
The comparator shows a second price. A desk with the same patience and a fixed-horizon test builds a better
book. Itsadmissionsarelessconcentratedinshort-horizonreversal. Ananytime-validbarrewardsthestatistic
that is strongest per day. The strongest daily statistic in this library is the hardest to trade. The design change
is to certify the horizon that is traded, not the daily one.
The evidence has clear edges, and each edge bounds one claim:
21

• The sample.The sample covers one market and four start years that share most of their data. There is
no held-out period beyond the walk-forward.
• The label.The registered label leans towards the frozen referee. It is not planted truth and overlaps the
admission window. Judging each factor only after its admission lowers the headline ratio by about a
third. The synthetic factorial has no overlap and carries the claim about false admissions.
• The comparisons.The LLM runs the leaky referees only on the four-family library. The fixed-horizon
comparator is a counterfactual referee on the frozen referee’s candidate sequence. It is not an arm with
its own campaign. The diagnosis role of the LLM controller is not ablated on its own. The controller
contrasts compare packages, since the LLM also reads profiles and memory, and on real data they are
replay outcomes, not forecasts.
• The guarantee.The proof controls the conditional null on the whitened stream. The marginal-null
guarantee under autocorrelation is measured, not proved. The cluster merge is not exercised.
• Retirement.Retirement is calibrated on synthetic decay. Its guarantee concerns the average run length.
This gives no usable bound over one campaign.
• The portfolio.The portfolio results support no claim of investability. Alphat-statistics are below one in
every certified four-family group. The cost model includes no borrow fee. The book is an instrument,
not a strategy (Appendix B).
10 Conclusion
Judging must be governed by a statistical procedure that the agent cannot touch. Proposing and instrument-
making are where the agent’s intelligence has measurable, bounded value. This division of labour is governed
self-evolution, the framework we have proposed and measured. The agent’s surface evolves freely. A frozen
referee decides what enters the portfolio. Who judges determines how many false factors an always-on miner
certifies. No proposer substitutes for the judge.
The split is testable because three objects remain separate and auditable: the certificate for the statistic, the
measurementofitspersistence,andtheexecutiondecision. Thecertificateisjudgedonthereferee’sowndaily
stream. Persistence and execution are measured afterwards, on returns the certificate never saw. A portfolio
Sharpe ratio mixes all three. That is why it is evidence neither for nor against a certificate. It also explains the
next design question: the certified horizon should match the traded one.
Data and code availability
The code, run manifests, prompts, and recorded model calls are available from the corresponding author on
request (deepgroundingai@gmail.com). The authors cannot redistribute the market data because they license
them from a commercial data vendor.
References
Ahmadi-Javid, Amir, and Mohsen Ebadi. 2021. “Economic Design of Memory-Type Control Charts: The
FallacyoftheFormulaProposedbyLorenzenandVance(1986).”ComputationalStatistics36(1): 661–90.
https://doi.org/10.1007/s00180-020-01019-6.
Bailey, David H., and Marcos López de Prado. 2014. “The Deflated Sharpe Ratio: Correcting for Selection
22

Bias, Backtest Overfitting, and Non-Normality.”The Journal of Portfolio Management40 (5): 94–107.
https://doi.org/10.3905/jpm.2014.40.5.094.
Chen, Mingguang, Licheng Wang, and Bo Qu. 2026.Recursive Self-Improvement in AI: From Bounded
Self-Refinement to Autonomous Research Loops. https://arxiv.org/abs/2607.07663.
Clerico, Eugenio. 2026.Sequential Testing of Conditionally Constrained Hypotheses. https://arxiv.org/abs/
2606.06769.
Dandapanthula, Sanjit, and Aaditya Ramdas. 2025.Multiple Testing in Multi-Stream Sequential Change
Detection. https://arxiv.org/abs/2501.04130.
Fischer,Lasse,ZiyuXu,andAadityaRamdas. 2024.AnOnlineGeneralizationofthe(e-)Benjamini-Hochberg
Procedure. https://arxiv.org/abs/2407.20683.
Gonuguntla, Ashritha. 2026.The Replay Gap: Static Evaluation of Model Switching in LLM Agents Scores
the Wrong World. https://arxiv.org/abs/2608.08239.
Harvey, Campbell R., Yan Liu, and Heqing Zhu. 2016. “...And the Cross-Section of Expected Returns.”The
Review of Financial Studies29 (1): 5–68. https://doi.org/10.1093/rfs/hhv059.
Heide, Rianne de. 2026.Dynamice-Closure for Online Hypotheses with Any-Time-Valid Evidence: Closure
Principles and Projective Mergers. https://arxiv.org/abs/2608.09927.
Li, Yuante, XuYang, XiaoYang, etal. 2025.R&D-Agent-Quant: AMulti-AgentFrameworkforData-Centric
Factors and Model Joint Optimization. https://arxiv.org/abs/2505.15155.
Liu, Jianan, Robert F. Stambaugh, and Yu Yuan. 2019. “Size and Value in China.”Journal of Financial
Economics134 (1): 48–69. https://doi.org/10.1016/j.jfineco.2019.03.008.
Lorenzen, Thomas J., and Lonnie C. Vance. 1986. “The Economic Design of Control Charts: A Unified
Approach.”Technometrics28 (1): 3–10. https://doi.org/10.1080/00401706.1986.10488092.
Martinez-Taboada, Diego, and Aaditya Ramdas. 2026.Gaussian-Efficient Testing by Betting on the Mean of
Bounded Data. https://arxiv.org/abs/2608.21694.
McLean,R.David,andJeffreyPontiff. 2016. “DoesAcademicResearchDestroyStockReturnPredictability?”
The Journal of Finance71 (1): 5–32. https://doi.org/10.1111/jofi.12365.
Newey, Whitney K., and Kenneth D. West. 1987. “A Simple, Positive Semi-Definite, Heteroskedasticity and
Autocorrelation Consistent Covariance Matrix.”Econometrica55 (3): 703–8. https://doi.org/10.2307/19
13610.
Qu, Bo, and Mingguang Chen. 2026.CLQT: A Closed-Loop, Cost-Aware, Strategy-Consistent Benchmark
for Diagnostic Evaluation of LLM Portfolio-Management Agents. https://arxiv.org/abs/2606.29771.
Sengupta, Biswa. 2026.Self-Evolving Agents with Anytime-Valid Certificates. https://arxiv.org/abs/2607.008
71.
Shawn, Zayx. 2026.PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents. https://arxiv.org/abs/
2606.08106.
Shin,Jaehyeok,AadityaRamdas,andAlessandroRinaldo. 2024. “E-Detectors: ANonparametricFramework
23

for Sequential Change Detection.”The New England Journal of Statistics in Data Science2 (2): 229–60.
https://doi.org/10.51387/23-NEJSDS51.
Sun, Liulei, and Ruodu Wang. 2026.Admissibility and Complete Classes for False Discovery Rate Control
with e-Values. https://arxiv.org/abs/2607.14380.
Tang,Ziyi,ZechuanChen,JiaruiYang,etal. 2025.AlphaAgent: LLM-DrivenAlphaMiningwithRegularized
Exploration to Counteract Alpha Decay. https://arxiv.org/abs/2502.16789.
Ville, Jean. 1939.Étude critique de la notion de collectif. Monographies Des Probabilités, Fascicule III.
Gauthier-Villars.
Vovk, Vladimir, and Ruodu Wang. 2021. “E-Values: Calibration, Combination and Applications.”The
Annals of Statistics49 (3): 1736–54. https://doi.org/10.1214/20-AOS2020.
Wang, Hongjian, Sanjit Dandapanthula, and Aaditya Ramdas. 2025.Anytime-Valid FDR Control with the
Stopped e-BH Procedure. https://arxiv.org/abs/2502.08539.
Wang,Ruodu,andAadityaRamdas. 2022. “FalseDiscoveryRateControlwithe-Values.”JournaloftheRoyal
Statistical Society Series B: Statistical Methodology84 (3): 822–52. https://doi.org/10.1111/rssb.12489.
Waudby-Smith, Ian, and Aaditya Ramdas. 2024. “Estimating Means of Bounded Random Variables by
Betting.”Journal of the Royal Statistical Society Series B: Statistical Methodology86 (1): 1–27. https:
//doi.org/10.1093/jrsssb/qkad009.
Xu, Ziyu, Lasse Fischer, and Aaditya Ramdas. 2026.Improving Online FDR Procedures via Online Analogs
of e-Closure and Compound e-Values. https://arxiv.org/abs/2603.24792.
Yi, Jingyang, Jian Yang, Yifei Jin, Yuqi Li, and Jian Li. 2026.AlphaSchema: Exploring the Space of Trading
Semantics for LLM-Based Alpha Mining. https://arxiv.org/abs/2607.26642.
Yu, Shuo, Hongyan Xue, Xiang Ao, et al. 2023. “Generating Synergistic Formulaic Alpha Collections via
Reinforcement Learning.”Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery
and Data Mining, 5476–86. https://doi.org/10.1145/3580305.3599831.
24

Appendix A Definitions, conventions and worked calculations
This appendix supports the body on three things. It defines the terms the body names before it builds them. It
states the conventions behind every reported number. It works three calculations the body quotes. Nothing
here is a new result.
Terms at first use.Ane-processis a candidate’s betting capital read over time. Under the null it is a test
supermartingale, so its value at any stopping time is a fair quantity, ane-value(§4.1).Online e-BHis the
Benjamini–Hochberg procedure applied to those e-values as they arrive, over a universe of hypotheses fixed
in advance (§4.3). Ane-detectoris a sum of e-processes restarted every day, used as a changepoint chart
(§4.4). Aleaky refereeis a referee that breaks one assumption of Proposition 1 in the way a common practice
does (§7.1).Planted truthmeans that the synthetic world knows which of its factors have an edge, so every
admissionislabelledtrueorfalsewithoutaproxy(§7.2). Aperceptionprobeisasmallprogramthecontroller
writestomeasureasuspectedfaultinadeployedfactor. Itsoutputinformsthecontroller’sdiagnosisandnever
enters a statistical test (§6). Asleeveis one factor’s own quintile long–short portfolio. A sleeve isshelved
when it cannot cover its costs at any holding frequency (§5).
Candidateclocks.Acandidateisopen,deployedorretired(§3). Acandidatethatleavestheopenstatewithout
admission hasexpired. It keeps its slot (§4.3). Afalse retirementis an alarm of the retirement detector raised
while the deployed factor’s edge is still at leastδ. Therun lengthis the number of trading days from the
detector’s start to its alarm. The guarantee of §4.4 bounds the expected run length to a false retirement from
below byA∗ = 1260 days. Over one campaign that bound is not informative. The false-retirement rates
reported are therefore simulation results.
Admission bookkeeping, with a two-candidate example.Anepochis a period in which the library is frozen.
The reported runs use one epoch. Aslotis one of theNv = 2000 places in the registered universe. Every
submitted candidate takes one slot and keeps it, whether it is admitted, expires or is retired. Withwv = 1
every slot has weightγc = 1/Nv. The bar for thek-th admission at levelα= 0.05 is Nv/(kα). It is 40,000
for the first admission and 20,000 for the second. Suppose candidate A has capital 45,000 and candidate B
has 25,000. A alone clears the first bar. Both clear the second bar, sok∗ = 2 and both are admitted. If B
had 15,000 instead, only A would be admitted and B would keep betting. The rule lowers the bar as more
candidates clear it. It never raises the bar.
The wait, worked.At the Kelly stake the expected wait for thek-th admission isT≈ln

Nv/(kα)

·2σ 2/µ2
(§4.3). For the first admissionln(40,000)≈10.6 . Daily rank-IC has σ≈0.12 . At edge µ= 0.03 ,
2σ2/µ2 = 32, soT≈339 days. At the viability thresholdµ= 0.015 , 2σ2/µ2 = 128, soT≈1356 days.
The capped bettor as run, with the stake at the cap of 0.8, takes 546 and 1434 days in the same two cases. A
universe sized to the campaign’s 490 slots would lower every bar byln(2000/490). That is worth 72 days at
edge0.03and 191 days at0.015.
The four threats and their answers.The body names four threats (§3). Each has one answer.
1. Optional stopping.The capital is a test supermartingale. It may therefore be read every day and
stopped by any rule based on the past, and the false-discovery bound holds at the stopping time (§4.1).
2. Near-copy resubmission.Every copy takes its own slot under online e-BH. The bound stays atα.
Repetition spends the proposer’s slots and nothing else (§4.3).
3. Verifier-in-the-loop adaptation.The referee sizes each bet before the day’s outcome and scores
only data that arrived after submission. What the controller learns about the referee changes which
candidates it submits, not the referee’s error (Proposition 1).
25

4. Knowledge-cutoff leakage.The referee does not address it. Proposition 1 assumes that the proposer
holds no information about the post-submission stream. A live run satisfies this. A historical replay
by a model trained on the campaign years may not. The language-model arms’ real-data results are
thereforereplay outcomes: what the package achieved on that history, not an instance of the guarantee.
The analysis unit and the reporting conventions.The unit of analysis is a seed. Two arms on the same seed,
model family and start year share common random numbers, and their metric difference is one observation.
A reported “±” is the standard error over the five seeds. The test is a two-sided pairedt-test on the five
differences. Holm correction is applied within one model family. On real data that family has 24 tests: four
starts × two contrasts× three metrics. In the synthetic world it has 8: four referees× two metrics. An effect
is reported as “k of n families”. In the sign tables, each entry has one sign per start year. The number in
parentheses counts the starts significant after Holm correction. No parentheses means none.
Portfolio statistics, operationally.Agroupis the five seeds of one referee, controller, library and start year.
The study has 108 groups. The net Sharpe ratio is the mean daily net return over its standard deviation,
annualised with 244 trading days. The deflated Sharpe ratio (Bailey and López de Prado 2014) discounts
that ratio for the 108 groups compared. Alpha is the intercept of a regression of daily net return on market,
size and book-to-price legs built from the panel, in the spirit of CH-3 (Liu et al. 2019), with Newey–West
t-statistics at lag 5 (Newey and West 1987). It is quoted in basis points per day. Index beta is the slope on the
CSI 500 index return.
The factorial in one schema.Each environment has a unit, an outcome and a contrast.
• Synthetic world.Unit: a cell (one arm combination, one model family, one seed). Outcomes: re-
alised yield per submission and realised false admissions per campaign, labelled against planted truth.
Contrasts: four referee arms×three controllers, two LLM families, five seeds.
• Probe environment.Unit: an episode (one deployed factor with one hidden fault). Outcome: interven-
tion regret. Contrast: the authored probe against the fixed diagnosis menu on the same 100 episodes,
per model family, seven families.
•Real data.Unit: a cell. Outcomes: the realised label atδ= 0.015and the canonical book’s statistics.
Contrasts: the same arms, four start years×five seeds, with LLM coverage as in Table 23.
Appendix B Derivations and ablation details
Bettor ablation.The bettor choice is immaterial at these noise levels. The cap fraction sets the wait. At
µ= 0.03 and σ= 0.12 , the Kelly stake exceeds any no-bankruptcy cap. Thus, aGRAPA, the Gaussian-
efficient bettor (Martinez-Taboada and Ramdas 2026) and a capped oracle all sit at the cap. A cap fraction of
0.8 accepts aµ= 0.03 factor in a median of 162 days (ρ= 0 ) or 190 days (ρ= 0.2 ). At a fraction of 0.5, the
median is 238/284, with null false acceptance of 1.9/3.4%.
Holding grid.The grid covers the five frequencies a desk trades: weekly, fortnightly, monthly, bi-monthly and
quarterly. It is scored using the average of the decay curve. It does not use the practitioner’s “IC at horizonh”.
That measure rises mechanically withh because averaging returns lowers noise. The design excludes daily
formation. This costs under 1% per year for the two families flat enough to favour it.
Conversionestimator.Aconversionrateestimatedpersleeveistoonoisytoguideshelving. Thefirstcanonical
pass estimated it per sleeve. This reversed the cost curve. It shelved 77% of volatility and 48% of liquidity
sleeves, against 32% of reversal. The denominator caused this reversal. It is a 250-day mean IC whose
standard error (0.006–0.013) matches the size of a real edge. With the market constant, the cells shelve 0% of
26

liquidity, 2% of volatility, 30% of reversal and 89% of momentum.
Cool-down sweep.The pre-stated rulenever worst, least churnselected the cool-downB= 250 , not Sharpe.
Dynamic variants withB∈ {5,10,21,63,250} differ by 0.4–3.8% per year by family. No variant wins
consistently. B= 250 exceeds fixed monthly in four of five families. It is the only variant that turns reversal
positive.
The conversion constant is in sample.¯κ= 0.018is the one input measured over the whole sample. Across
the half-sample band0.013–0.026, the traded-or-shelved decision flips for 3.3–7.2% of the 51,531 calibrated
sleeves. Almost all flips are in reversal (14–19% of its sleeves). The books were not re-booked across the
band.
Cost sensitivity.Table 5 re-costs the 2016 round-robin books with fixed positions and scaled stock-side cost.
The certified book’s one-way turnover is 3.4% per day, against the ungated book’s 2.2%. Thus, “the certified
book does not lose money” applies at the registered cost level.
Table 5:Cost sensitivity of the two books (five-seed means). The certified book crosses zero between 30 and 50 bp a
side. The ungated one does not.
Cost per Side Certified Net SR Ungated Net SR
15 bp (registered)+0.40 +0.73
25 bp+0.25 +0.61
30 bp+0.17 +0.54
50 bp−0.12+0.29
Accounting conventions.Reviewers questioned two conventions of the registered book. Neither changes
the comparison (Table 6).Carryholds a halted position at its last price and credits the whole gap on the
reopening day. It does not book a missing return as zero.Lagexecutes the target book decided on dayt on
day t+ 1. It does not execute at the signal’s own close. Both are re-booked at zero cost from the recorded
holding intervals. The canonical re-booking reproduces every recorded book to10−9.
Table6:The2016round-robinbooksunderfouraccountingconventions(five-seedmeanswithstandarderrors,244-day
annualisation). The ungated book’s lead is0.34–0.35under every convention.
Book Convention Net Sharpe Cumulative Net Return
Certified Registered+0.40±0.03 +46.6%
Certified Carry+0.40±0.03 +47.1%
Certified One-Day Lag+0.37±0.03 +43.5%
Certified Carry and Lag+0.38±0.03 +44.1%
Ungated Registered+0.73±0.02 +66.3%
Ungated Carry+0.75±0.02 +67.7%
Ungated One-Day Lag+0.71±0.01 +64.1%
Ungated Carry and Lag+0.72±0.01 +65.5%
Instrument properties.The book is a measuring instrument. The paper gives no certificate of tradability.
Short selling is assumed for a quintile of individual A-shares, without a borrow list or borrow fee. The hedge
leg uses index futures. A missing return is booked as zero (12.5% of member-stock days in 2015, about 0.2%
from 2019). Neither capacity nor drawdown is modelled. Measured maximum drawdown is 21–25% for the
certified book and 20–21% for the ungated one.
Referee ablations.The adopted referee whitens the stream. It uses the predictable bankruptcy bound and
estimates ρ. Ablations on synthetic streams settled each choice before any paid run (Table 7). Whitening
restores nominal control at every autocorrelation tested. The predictable bound recovers most of the power
27

lost under a worst-case bound. Estimatingρbeats knowing it atρ= 0.4 . This advantage arises because the
shrunk estimate under-whitens, trading a within-bound validity error for power.
Table7:RefereeablationsusesyntheticAR(1)streamsat ρ= 0 / 0.2/ 0.4. Thistableusescapfraction0.5. Thereferee
runs at 0.8. The experiment uses ten-year null streams atµ= 0 and alternative streams atµ= 0.03 . Alive streams
cover 2520 days with run-length target 1260. The nominal level is 5%. Against a Monte-Carlo-calibrated CUSUM, the
adopted e-detector’s median delay is 204–322 days by decay shape, against CUSUM’s 181–337.
Stream Transformation
Null False
Acceptance, %
Median Days to
Accept
Detector False
Alarms on Alive
Streams, %
Step-Decay Delay,
Median Days
Raw daily rank-IC (conditional
null)
2.1 / 6.0 / 15.4 228 / 227 / 227 1.5 / 11.5 / 46 213 / 181 / 195
Whitened, worst-case bound 1.1 / 1.3 / 1.8 336 / 378 / 462 1.0 / 0.0 / 7.0 250 / 264 / 316
Whitened, predictable bound
(adopted)
1.8 / 2.0 / 2.4 238 / 284 / 384 1.5 / 0.5 / 8.5 218 / 234 / 308
Whitened with the trueρ
(oracle)
2.1 / 1.3 / 0.9 228 / 344 / 536 1.5 / 0.5 / 6.5 213 / 246 / 333
Family removal.Removing each family in turn from the ungated book shows that momentum helps through
diversification, not return. Dropping momentum costs+0.11 to +0.18 net Sharpe while raising cumulative
net return in all four starts. A momentum-only book earns+0.22 to +0.29. Dropping the certified reversal
family raises the book’s Sharpe by+0.01to+0.14.
Selection.We chose the execution layer after first examining the recorded cells. One fact limits how much
this choice can explain. Every construction tried (A10b, A11, A11b, A11c in Table 24) ranks the ungated
book above the certified one. Neither execution parameter was chosen on Sharpe. The deflated Sharpe ratio
treats the 108 final book groups, not the constructions, as trials. The reported deflation therefore understates
the search.
Newey–West bandwidth.At Bartlett bandwidths 5, 8, 21 and 63, the certified book’s alphat-statistics are0.49,
0.49, 0.51 and 0.54. Those for the ungated book are1.68, 1.71, 1.75 and 1.86. The inference therefore does
not depend on the bandwidth. We keep lag 5.
Benchmark construction.The regression uses a characteristic three-factor model on our own panel, not the
published CH-3 benchmark (Liu et al. 2019). SMB and HML are long–short quintiles of−log circulating
capitalisation and book-to-price over the full universe. The benchmark legs are gross, while the dependent
variable is net. This difference is expected to lower the estimated alpha.
Rank-threshold retirement.Declaring the topk streams atA∗/k satisfies the error-over-patience bound but is
unusable. A healthy factor’s statistic plateaus near1/(1−decay) , with median≈75 on the whitened stream.
Yet A∗/k is 63–126 fork= 10 –20. The rule therefore declares an all-alive library of 20 en bloc within a year.
Appendix C Extended results
This appendix presents detailed evidence for §8. Tables 8 and 9 present the synthetic factorial and probe
environment. Figure6plotsTable2. Tables10to18providezero-costledgeranalysesforthereal-datasections.
They cover the realised edges of admitted factors, label-threshold sensitivity, and after-admission and per-
family labels. They also cover legitimate comparators, counterfactual books, the period split, and retirement
outcomes. Table 19 gives the Sharpe decomposition. Figure 7 shows the admission-delay distribution, and
Table 20 reports the regime timing. Tables 21 and 22 provide the paired controller contrasts behind Table 3.
28

Table 8:Synthetic world with planted truth (four families, 1260 days, five seeds). The table reports seed-mean realised
yield and false admissions per submission by referee arm and controller for the two LLM families run there. It also
reports the hidden-retry attacker’s false admissions.
Family Referee
Yield: Round-Robin /
Bandit / LLM
False Admissions:
Round-Robin / Bandit /
LLM Hidden Retries: False
Gemini Frozen 0.095 / 0.096 / 0.096 0.000 / 0.000 / 0.000 0.000
Gemini Peeking 0.060 / 0.065 / 0.063 0.314 / 0.300 / 0.315 0.341
Gemini Adaptive
Threshold
0.081 / 0.087 / 0.087 0.272 / 0.273 / 0.263 0.281
Gemini No Gate 0.042 / 0.034 / 0.043 0.838 / 0.848 / 0.836 0.820
GPT Frozen 0.095 / 0.096 / 0.096 0.000 / 0.000 / 0.000 0.000
GPT Peeking 0.060 / 0.065 / 0.061 0.314 / 0.300 / 0.318 0.341
GPT Adaptive
Threshold
0.081 / 0.087 / 0.088 0.272 / 0.273 / 0.271 0.281
GPT No Gate 0.042 / 0.034 / 0.041 0.838 / 0.848 / 0.839 0.820
Table9:Probeenvironmentattheregisteredescalationprice. Foreachmodelfamily,thetablereportsmeanintervention
regret against the oracle (edge units)± s.e. over 100 episodes for the fixed diagnosis menu and authored probes. Paired
differences are authored minus menu within each episode. Holm correction covers the six evaluable families.
Family Fixed Menu: Regret
Authored Probes:
Regret Paired Difference Holmp
DeepSeek 0.616±0.098 0.228±0.064−0.388±0.1010.001
Muse 0.651±0.084 0.403±0.064−0.248±0.0700.002
Gemini 0.692±0.098 0.458±0.117−0.233±0.0850.025
GPT 0.526±0.078 0.459±0.097−0.067±0.0721.000
Hunyuan 0.663±0.097 0.642±0.109−0.021±0.0691.000
GLM 0.585±0.093 0.659±0.148+0.074±0.1141.000
Qwen 0.415±0.103 0.415±0.103 Inevaluable (No Probe
Produced)
Appendix D Environment, amendments and information parity
The540cellscomprise320baselinecellsand220LLMcells(Table23). Table24listseverydatedamendment
to the pre-registered design.
The probe environment.The five held-out fault types include collapsed cross-sectional dispersion, possible
crowding or regime-change decay, and lagged restatement of fundamentals. They also include sibling-factor
contamination and a cost-channel fault. The fixed menu contains three instruments: a data-health canary, a
crowding proxy and an IC changepoint test. The controller chooses one of five interventions: retire the factor,
deprecate or pause its family, repair the data pipeline, or pay to escalate. A transparent economic model
gives each intervention’s after-cost value in each true state over 126 days. Regret is the oracle’s value less the
chosen intervention’s value.
Information parity.All controllers receive the same numeric family statistics. The LLM controller also
receives family profiles, open candidates, paused families and memory. The controller contrasts therefore
compare packages. No controller sees the book. The text names model versions only by family, while the run
manifests pin them.
The break-even figure in the family profiles.The family profiles contain a scaling error that does not change
how the controller contrasts are read. Their break-even ICs used the regression slope of §5.2, not the average
conversion. Thus, every figure is between a quarter and a third of the corrected value. The error is a common
29

Table 10:Anatomy of admissions on the four-family library (means per campaign over four starts×five seeds). The
table splits ever-admitted factors by their realised post-submission mean rank-IC. The first two classes together are
realised false admissions. The last column counts false admissions retired by the detector before campaign end.
Arm Admitted Edge<0
0≤Edge
< δEdge≥δ
False
Admissions
Retired by
the End
Frozen, Round-Robin 214.7 0.0 11.7 203.0 11.7 11.7
Frozen, Bandit 260.8 0.0 9.4 251.3 9.4 9.4
Frozen, LLM (Gemini) 257.0 0.0 11.7 245.3 11.7 11.7
Frozen, LLM (DeepSeek) 258.1 0.0 12.7 245.5 12.7 12.7
Frozen, LLM (GPT) 236.9 0.0 13.3 223.6 13.3 13.3
Peeking, Round-Robin 312.5 10.8 75.3 226.3 86.2 85.6
Peeking, Bandit 342.8 3.6 34.7 304.4 38.4 38.1
Peeking, LLM (Gemini) 354.9 1.2 36.1 317.6 37.4 37.0
Adaptive Threshold,
Round-Robin
322.3 32.0 73.2 217.1 105.2 93.7
Adaptive Threshold, Bandit 327.6 11.6 39.4 276.6 51.0 47.7
Adaptive Threshold, LLM
(Gemini)
330.6 6.0 37.5 287.1 43.5 42.8
No Gate, Round-Robin 398.0 90.8 105.2 202.0 196.0 150.8
No Gate, Bandit 398.0 92.0 97.8 208.2 189.8 148.1
No Gate, LLM (Gemini) 398.0 15.5 62.5 320.1 78.0 61.8
No Gate, LLM (DeepSeek) 398.0 49.5 77.0 271.4 126.6 97.5
No Gate, LLM (GPT) 398.0 74.2 94.9 228.9 169.1 126.6
Table 11:Label-threshold sensitivity on the four-family library (means over four starts× five seeds). The table reports
realisedyieldpersubmissionandrealisedfalseadmissionspercampaignatlabelthresholdsof 0.010, 0.015(registered),
and0.020.
Referee Controller Yield at 0.010 / 0.015 / 0.020
False Admissions at 0.010 /
0.015 / 0.020
Frozen Round-Robin 0.403 / 0.403 / 0.400 5.4 / 11.7 / 13.8
Frozen LLM (Gemini) 0.471 / 0.471 / 0.466 5.7 / 11.7 / 14.7
Peeking Round-Robin 0.407 / 0.406 / 0.402 78.5 / 86.2 / 90.2
Peeking LLM (Gemini) 0.546 / 0.546 / 0.532 31.9 / 37.4 / 45.7
Adaptive Threshold Round-Robin 0.390 / 0.390 / 0.387 97.1 / 105.2 / 108.2
Adaptive Threshold LLM (Gemini) 0.478 / 0.478 / 0.476 37.5 / 43.5 / 47.0
No Gate Round-Robin 0.370 / 0.367 / 0.361 185.8 / 196.0 / 200.5
No Gate LLM (Gemini) 0.596 / 0.585 / 0.547 66.7 / 78.0 / 95.8
scale. The profiles rank families correctly and understate only the level. The referee never reads the profile.
The controller uses it only to weigh families against one another.
Appendix E Data, point-in-time rules and the factor library
Every quantity used on a day is known before that day’s position is taken. Membership uses the latest index-
weight snapshot dated at or before the previous trading day. Prices are adjusted by the vendor’s cumulative
factor. Halts are missing values. A name that closed at its price limit (|∆p| ≥9.5%) on dayt−1 is excluded
from the day-t universe. Fundamentals become visible on their announcement date and have a 400-day
staleness cut. The panel covers 2834 trading days. It includes 1356 stocks that were ever members. Every
vendor-extract partition has a SHA-256 in a provenance manifest.
The factor library.The library is fixed in advance, keeping the hypothesis universe finite as Proposition
1 requires. Each family represents an economic hypothesis with a fixed sign and parameter grid. Each
30

Table 12:Four-family library results show realised false admissions under three labels. Values are means per campaign
over four starts× five seeds.Fullis the registered label.Afterjudges each admitted factor only on days after admission.
δf is each family’s break-even (liquidity 0.012, volatility 0.017, momentum 0.031, reversal 0.074).
Referee Controller Admitted False: Full False: After False atδ f Edge After
Yield: Full /
After
Frozen Round-
Robin
214.7 11.7 17.6 96.0 0.032 0.403 / 0.380
Frozen Bandit 260.8 9.4 14.4 114.3 0.032 0.474 / 0.460
Frozen LLM
(Gemini)
254.8 11.7 15.8 111.7 0.032 0.466 / 0.458
Peeking Round-
Robin
312.4 86.2 91.2 180.4 0.023 0.406 / 0.390
Peeking Bandit 342.8 38.4 52.6 170.5 0.027 0.495 / 0.457
Peeking LLM
(Gemini)
354.6 37.4 41.5 152.9 0.029 0.545 / 0.511
Adaptive
Threshold
Round-
Robin
322.3 105.2 107.5 197.4 0.021 0.390 / 0.384
Adaptive
Threshold
Bandit 327.6 51.0 54.4 185.8 0.027 0.442 / 0.430
Adaptive
Threshold
LLM
(Gemini)
330.2 43.5 44.4 158.2 0.029 0.478 / 0.466
No Gate Round-
Robin
398.0 196.0 195.6 276.2 0.016 0.367 / 0.358
No Gate Bandit 398.0 189.8 194.1 265.6 0.015 0.372 / 0.352
No Gate LLM
(Gemini)
394.0 77.2 77.0 185.3 0.027 0.577 / 0.565
Table 13:Nine-family library results show the same measures. They exclude a per-family break-even because it is
undefined for the five fundamental families.
Referee Controller Admitted False: Full False: After Edge After Yield: Full / After
Frozen Round-Robin 127.2 9.8 16.6 0.028 0.246 / 0.225
Frozen Bandit 188.1 11.9 17.6 0.030 0.357 / 0.340
Frozen LLM (Gemini) 198.6 14.6 20.3 0.030 0.377 / 0.364
Peeking Round-Robin 256.9 127.3 131.8 0.016 0.244 / 0.233
Peeking Bandit 295.8 97.0 107.2 0.020 0.360 / 0.330
Adaptive
Threshold
Round-Robin 296.4 175.2 174.9 0.013 0.230 / 0.228
Adaptive
Threshold
Bandit 299.6 128.8 129.7 0.019 0.292 / 0.285
No Gate Round-Robin 398.0 295.6 292.9 0.009 0.192 / 0.189
No Gate Bandit 398.0 293.8 291.1 0.008 0.194 / 0.190
submission draws one specification from that grid (Table 26).
31

Table 14:Four-family library results show fixed-horizon comparator referees run as counterfactual programs on the
frozen cell’s recorded submission stream. Values are means per campaign over four starts×five seeds. Each tests the
post-submission mean once, 500 or 250 days after submission. Each applies Benjamini–Hochberg at 0.05 whenever a
window closes (Daily, deployable) or once at the campaign’s end (At End, so no yield or wait).
Controller Referee Admitted
False:
Full
False:
After
Share
False
Edge
After Yield Wait
Round-Robin Frozen (Recorded) 214.7 11.7 17.6 0.08 0.032 0.403 439
Round-Robin Fixed 500 (Daily) 208.0 16.4 22.2 0.11 0.029 0.358 500
Round-Robin Fixed 500 (At End) 207.2 16.0 21.8 0.11 0.029 – –
Round-Robin Fixed 250 (Daily) 187.4 16.6 19.4 0.10 0.030 0.314 250
Bandit Frozen (Recorded) 260.8 9.4 14.4 0.06 0.032 0.474 408
Bandit Fixed 500 (Daily) 262.6 12.2 20.4 0.08 0.028 0.441 500
Bandit Fixed 500 (At End) 262.3 12.1 20.2 0.08 0.028 – –
Bandit Fixed 250 (Daily) 239.6 9.8 13.3 0.06 0.031 0.404 250
Table 15:Nine-family library results show the same comparators.
Controller Referee Admitted
False:
Full
False:
After
Share
False
Edge
After Yield Wait
Round-Robin Frozen (Recorded) 127.2 9.8 16.6 0.12 0.028 0.246 543
Round-Robin Fixed 500 (Daily) 150.2 41.4 49.7 0.33 0.021 0.214 500
Round-Robin Fixed 500 (At End) 148.8 40.8 48.9 0.33 0.021 – –
Round-Robin Fixed 250 (Daily) 115.0 30.2 33.8 0.29 0.023 0.159 250
Bandit Frozen (Recorded) 188.1 11.9 17.6 0.09 0.030 0.357 436
Bandit Fixed 500 (Daily) 207.8 33.2 44.0 0.22 0.024 0.330 500
Bandit Fixed 500 (At End) 207.3 33.2 43.8 0.21 0.024 – –
Bandit Fixed 250 (Daily) 177.2 25.3 29.2 0.17 0.027 0.287 250
Table 16:Net Sharpe of counterfactual books on the round-robin frozen cell’s candidate sequence. Results use the
four-family library and five seeds per start. They report means with standard errors and differences paired per seed.
Retirement offholds every factor admitted by the frozen referee through the campaign’s end.Fixed 500 (Daily)is Table
14‘s deployable 500-day comparator. It is held from its admission day until the runs’ e-detector retires it.
Start No Gate Frozen
Frozen,
Retirement Off
Retirement Off
Minus Frozen
Fixed 500
(Daily)
Fixed 500
Minus Frozen
2016+0.74±0.02 +0.40±0.03 +0.41±0.03 +0.00±0.00 +0.60±0.01 +0.20±0.03
2017+0.78±0.01 +0.46±0.01 +0.47±0.01 +0.01±0.00 +0.59±0.02 +0.13±0.02
2018+0.75±0.01 +0.42±0.02 +0.42±0.02 +0.01±0.00 +0.65±0.02 +0.24±0.02
2019+0.62±0.04 +0.49±0.05 +0.50±0.05 +0.01±0.00 +0.61±0.02 +0.12±0.04
32

Table 17:Controller contrasts on the four-family library under the frozen referee, split by candidates submitted before
and from 2020-01-02. Each campaign has about 114 and 308 such candidates. LLM-minus-baseline differences are
paired by start and seed. Values are means±s.e. over 20 pairs.
Family Contrast
Yield Diff.
Pre-2020
Yield Diff.
Post-2020
False Adm. Diff.
Pre-2020
False Adm. Diff.
Post-2020
Gemini LLM−
Round-Robin
+0.009±0.005 +0.088±0.004−0.2±0.1 +0.1±0.2
Gemini LLM−Bandit+0.026±0.006−0.016±0.004 +0.3±0.2 +1.9±0.7
DeepSeek LLM−
Round-Robin
+0.028±0.009 +0.097±0.004−0.1±0.1 +1.1±0.6
DeepSeek LLM−Bandit+0.045±0.011−0.007±0.004 +0.5±0.2 +2.8±0.9
GPT LLM−
Round-Robin
+0.008±0.003 +0.050±0.004−0.1±0.1 +1.7±0.4
GPT LLM−Bandit+0.025±0.006−0.054±0.003 +0.5±0.2 +3.4±0.8
Table 18:Retirement outcomes on real data using the four-family library, frozen referee, and round-robin controller.
Results cover four starts× five seeds. They report factors retired per campaign and family. For retired factors, results
also report mean daily rank-IC during the held window and the remaining campaign. These factors had at least 21 days
held and 21 days left in the campaign.
Family Retired
Share
Retired Days Held
IC While
Held IC After After< δAfter<0
Liquidity 12.1 0.24 207−0.0053 +0.00401.00 0.05
Momentum 0.5 1.00 354−0.0131 +0.00350.89 0.22
Reversal 31.8 0.36 838+0.0145 +0.03380.00 0.00
All 44.3 0.21 661+0.0088 +0.02540.28 0.01
Table 19:Net Sharpe of counterfactual books under the canonical construction. The books are frozen, ungated, (a) the
referee’s factors on the ungated schedule, and (b) a fixed random subset of ungated factors matching the referee’s count.
Breadthis no gate less (b).Selectionis (b) less (a).Earlinessis (a) less frozen. The three sum to the gap. Sharpe here
uses 252 days.
Start Frozen No Gate (a) (b) Breadth Selection Earliness
2016+0.40 +0.74 +0.63 +0.72 +0.02 +0.09 +0.23
2017+0.46 +0.78 +0.65 +0.75 +0.04 +0.10 +0.19
2018+0.42 +0.75 +0.67 +0.71 +0.04 +0.04 +0.25
2019+0.49 +0.62 +0.53 +0.57 +0.05 +0.04 +0.04
33

Frozen Referee Peeking Adaptive Threshold No Gate
101
102
Realised False Admissions per Campaign
12
86
105
196
9
38
51
190
12
37
44
78
Round-Robin
Bandit
LLM
Figure 6:Realised false admissions per campaign by referee arm and controller (real data, four-family library; means
over four start years× five seeds; log scale). The referee sets the count; the controller moves it by a factor of 2–2.5, and
only when the referee leaks.
0 200 400 600 800 1000 1200
Admission Delay of True Factors (Trading Days)
0.0000
0.0025
0.0050
0.0075
0.0100
0.0125
0.0150
0.0175
0.0200Density
Frozen Referee
Peeking
Adaptive Threshold
No Gate
Figure 7:Admission delay of realised-true factors by referee arm (LLM controller, four-family library, 2016 start, five
seeds pooled). The no-gate spike is the pre-registered 126-day incubation.
34

Table 20:Nine-family library with the round-robin controller, 2016 start, and five pooled seeds. The table reports
sleeves ever held by the book. It also reports each family’s mean first-held campaign day, of 2,589. Finally, it reports the
share of holding windows with midpoints after 2020-01-02, campaign day 975.
Family
Certified:
Sleeves
First Held
(Mean Day) After 2020
Ungated:
Sleeves
First Held
(Mean Day) After 2020
Growth 42 1151 100% 235 1365 83%
Investment 0 412 1419 76%
Liquidity 126 1511 100% 213 1264 83%
Momentum 0 354 1561 84%
Quality 45 1177 100% 306 1541 86%
Reversal 237 1722 100% 164 1266 100%
Size 2 1842 100% 321 1242 65%
Value 171 1881 99% 184 1151 68%
Volatility 203 1509 100% 151 1190 100%
All Families 826 1612 100% 2340 1366 81%
Table 21:Paired realised-yield contrasts under the frozen referee on the four-family library. Contrasts compare the
LLM controller with round-robin and the bandit. They report the mean difference across five common-random-number
seeds and its standard error. They also report the Holm-adjusted two-sidedpwithin the model family, over 24 tests.
Family Start
LLM−Round-Robin
Yield HolmpLLM−Bandit Yield Holmp
DeepSeek 2016+0.095±0.0070.006+0.039±0.0070.124
DeepSeek 2017+0.079±0.0050.005+0.007±0.0041.000
DeepSeek 2018+0.080±0.0100.034−0.004±0.0061.000
DeepSeek 2019+0.070±0.0060.012−0.002±0.0071.000
Gemini 2016+0.064±0.0090.122+0.008±0.0071.000
Gemini 2017+0.070±0.0050.008−0.002±0.0021.000
Gemini 2018+0.076±0.0030.001−0.009±0.0031.000
Gemini 2019+0.063±0.0060.033−0.009±0.0121.000
GPT 2016+0.046±0.0050.039−0.010±0.0051.000
GPT 2017+0.038±0.0040.029−0.034±0.0060.156
GPT 2018+0.045±0.0080.136−0.039±0.0050.060
GPT 2019+0.028±0.0080.537−0.043±0.0070.111
Table 22:The same contrasts on the nine-family library.
Family Start
LLM−Round-Robin
Yield HolmpLLM−Bandit Yield Holmp
DeepSeek 2016+0.142±0.0040.000+0.029±0.0070.178
DeepSeek 2017+0.120±0.0090.003+0.011±0.0081.000
DeepSeek 2018+0.148±0.0070.001+0.026±0.0040.072
DeepSeek 2019+0.090±0.0090.009−0.010±0.0051.000
Gemini 2016+0.163±0.0030.000+0.050±0.0050.012
Gemini 2017+0.134±0.0070.001+0.026±0.0060.260
Gemini 2018+0.159±0.0130.005+0.036±0.0100.310
Gemini 2019+0.092±0.0150.068−0.009±0.0121.000
GPT 2016+0.059±0.0100.066−0.054±0.0070.032
GPT 2017+0.052±0.0030.001−0.057±0.0090.064
GPT 2018+0.051±0.0100.116−0.072±0.0080.021
GPT 2019+0.018±0.0101.000−0.082±0.0060.004
35

Table 23:Coverage of the real-data factorial. Every row covers four start years and five seeds. The last row is the
confirmatory extension run after the factorial.
Controllers Model Families Referee Arms Libraries Starts×Seeds Cells
Round-Robin,
Bandit
None All Four Both4×5320
LLM Gemini,
DeepSeek, GPT
Frozen Both4×5120
LLM Gemini Peeking,
Adaptive
Threshold, No
Gate
Four-Family4×560
LLM DeepSeek, GPT No Gate Four-Family4×540
Total 540
Table 24:Dated amendments to the pre-registered design. A5 and A9 were never issued. Every book amendment used
zero-cost re-booking of the recorded cells (Proposition 2).
Id Date What Changed Affects
A1 2026-09-02 LLM costs metered at billed prices; spend cap $335 No (accounting)
A2 2026-09-02 Deterministic iteration order; longer retry window No (engineering)
A3 2026-09-03 Escalation-price sensitivity computed by re-scoring recorded
episodes
No (analysis)
A4 2026-09-04 Abstract effort pins realised through the measured vendor map No (runtime)
A6 2026-09-04 Probe environment audited; two world defects fixed (world v2) Probe Environment
A7 2026-09-05 Real-data world specification on the CSI 500 Real-Data World
A8 2026-09-07 Nine-family library; trading-frequency slice Library
A10 2026-09-07 Framework consolidation before the restart; earlier recorded
runs not used
All Real-Data Runs
A10b 2026-09-07 Ex-ante book controls (turnover cap, index hedge); canonical
constructed book
Book
A11 2026-09-11 Certification, persistence and execution separated; per-sleeve
calibrated holding period
Book
A11b 2026-09-11 Five-frequency calendar grid; dynamic re-calibration with a
cool-down
Book
A11c 2026-09-13 Conversion rate fixed as a market constant after a ledger audit
of the first pass
Book
Table 25:The controller ladder. Every rung uses the same library, submission budget and referee. The rungs differ in
policy and, at the top rung, inputs and actions. Thus, the contrasts compare controller packages.
Rung
Allocation Across
Families Response to an Alarm Instruments
Inputs Beyond Family
Statistics
Round-robin
(C0)
Cycles through families Scripted: retire and refill the
same family
Fixed menu None
Discounted-
UCB bandit
(C1)
Reward per family:
admissions less
retirements, discounted
Scripted, as C0 Fixed menu None
LLM
controller (C2)
Reads statistics, family
profiles and memory
Diagnosis (idiosyncratic
death, crowding, regime
shift, data breakage) or
escalation; chooses the
response
Authors, tests and
mounts probes
Family profiles,
memory, the reasons
for retirements
36

Table 26:The nine factor families (the four-family library is the first four). Prices use adjusted closes. Fundamentals
are announcement-aligned. The grid is enumerable, fixing the hypothesis universe before the campaign.
Family Signal (sign) Parameters Drawn Specs
Momentumlog(P t−1−s/Pt−1−s−L)(+)L∈[40,250], skips∈[0,21]4,642
Short-
Horizon
Reversal
−log(P t−1/Pt−1−L)(+after sign)L∈[3,30] ; turnover-scaled or not 56
Volatility−(std, downside std or max) of daily returns overL(+
after sign)
L∈[10,130]; three kinds 363
Liquidity−mean turnover overL, or Amihud illiquidity (+after
sign)
L∈[10,130]; two kinds 242
Value Book, earnings, sales or dividends to price, smoothed
overL(+)
L∈[1,21]; four kinds 84
Size−log market capitalisation, circulating or total (+ after
sign)
L∈[1,21]; two kinds 42
Quality ROE, quarterly ROE, ROA, gross or net margin (+)L∈[1,63]; five kinds 315
Growth Net profit, revenue or EPS growth, year on year (+)L∈[1,63]; three kinds 189
Investment
(asset
Growth)
Asset or equity growth, year on year (−)L∈[1,63]; two kinds 126
37
