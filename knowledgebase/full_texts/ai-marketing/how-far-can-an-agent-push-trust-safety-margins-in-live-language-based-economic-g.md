---
title: How Far Can an Agent Push? Trust-Safety Margins in Live Language-Based Economic Games
url: https://arxiv.org/abs/2610.25508
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: arXiv (Cornell University)
authors:
- Dima Galat
- Marian-Andrei Rizoiu
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.25508
pages: 5
chars: 16950
fetched_at: '2026-11-08T13:35:31+00:00'
kb_version: 1
---

# How Far Can an Agent Push? Trust-Safety Margins in Live Language-Based Economic Games

How Far Can an Agent Push?
Trust-Safety Margins in Live Language-Based
Economic Games
Dima Galat
University of Technology Sydney
dima.galat@student.uts.edu.au
Marian-Andrei Rizoiu
University of Technology Sydney
Marian-Andrei.Rizoiu@uts.edu.au
Abstract
Game theory identifies when a strategic action should be accepted, but not how long
a live, language-based counterpart will continue to accept it. We entered the GLEE
competition in its final week with one protected agent,Milton, and four instrument
agents that ran deterministic, per-game randomized trials of policy changes; Milton
received changes only through pre-specified gates or registered, rollback-guarded
production rules. In negotiation, learned pricing improves adjusted percentile
by 0.071 (n= 21,168 ); in bargaining, a continuation model conditioned on
the rejected offer did not improve on a recency-weighted incumbent and was
retired. In persuasion, a preregistered five-dose experiment (7,391 assigned games,
blinded until a fixed stop) shows that recommending every unit raises sales by
0.194 of the maximum (95% CI [0.147,0.241] ) where the receiver’s slack makes
obedience rational—52% of the Bayesian benchmark—lowers them where it does
not (−0.067), and produces a larger early-to-late purchase decline than honest
recommendations (−0.123). A rule fixed before unblinding now routes Milton’s
dose per cell. Milton stood 11th of 460 agents in bargaining at the fixed stop;
we also report the close, where the final day’s pool shift moved all five agents’
bargaining ratings together while their play was unchanged, and three dispatch
defects were found by checking delivered behavior against the design.
1 Introduction
The GLEE benchmark [Shapira et al., 2024] places one agent in bargaining, bilateral negotiation, and
Bayesian persuasion games against a shared, evolving population of agents and humans. Each family
has a clean reference point—discounted alternating-offer bargaining [Rubinstein, 1982], individual
rationality in trade, receiver obedience in Bayesian persuasion [Kamenica and Gentzkow, 2011]—but
none specifies how a heterogeneous, language-mediated population reacts to repeated pressure, nor
how fast that changes.
We usetrust-safety marginas a conceptual framing for departures from theoretical acceptance under
repeated pressure. We measure cooperation, not trust directly, and do not estimate an empirical
behavioral cutoff. Our agent treats theory as a guardrail but chooses actions from live, configuration-
specific response estimates, in all three games under one workflow: measure, randomize within time,
promote only gated gains. Language agents that negotiate end to end [Lewis et al., 2017] or combine
language models with strategic planning [FAIR et al., 2022], and automatic agents for repeated
persuasion games [Raifer et al., 2022], have been evaluated against human counterparts; GLEE adds
a shared pool of agents and humans that changes while the agent plays.
Contributions: (i) an architecture that converts an opaque leaderboard update into per-game adjusted
percentiles and runs causal trials without risking the entry; (ii) randomized evidence that learned
40th Conference on Neural Information Processing Systems (NeurIPS 2026). Workshop: First Workshop on Interpreting
Agent Behavior (IAB) Competition Paper Track.
arXiv:2610.25508v2  [cs.MA]  20 Oct 2026

pricing helps negotiation while a better-conditioned bargaining model does not; (iii) a preregistered
persuasion study of how purchases vary with deception dose and within-game repetition relative to
the Bayesian benchmark; (iv) verification of the agent’s behavior against its design.
2 Agent, measurement, and development process
Per-game measurement.GLEE maps each game’s opponent-adjusted payoff percentile within
configuration and role, henceforth theadjusted percentile zg, to a game ratingGg = 2000+8000(zg −
0.5), updates the raw rating Rg+1 =R g +η g(Gg −R g), and displays a game-count-shrunk version.
With one in-flight game per family, consecutive public statistics identify the rating increment, so
we back-solve zg. Randomized comparisons are therefore contemporaneous and never use the
path-dependent leaderboard rating as an outcome.
Protected deployment, parallel instrumentation.Milton, the protected entry, plays all three
families. Wordsworth, Chaucer, Keats, and Tennyson are instruments: server-issued game identifiers
are hashed to assign variants before the first move—restart-proof and unsteerable—and the four
estimate one policy rather than four strategies. A randomized promotion to Milton requires an overall
95% CI above zero, neither role significantly negative, no configuration with n≥80 per arm worse
than−0.02, the newest 12 hours with the same sign, and zero invalid actions.
Family policies.Bargaining: a four-hour exponentially decayed acceptance model (offer, round,
both discount factors, opponent) with Thompson sampling [Thompson, 1933]. Negotiation:
learned acceptance and payoff maps price complete-information and one-shot cells (learned
pricing); theincumbent schedulekeeps hidden-value multi-round cells. Persuasion: the buyer
keeps message-conditional trust; the seller always recommends high quality and controls the dose
q=P(recommend|low) . All are seeded, legal-by-construction rules without model inference at
move time.
Development process.Instrumented play began on 21 August, seven days before the fixed stop; on
22 August the persuasion protocol was frozen (hashes, OpenTimestamps proofs) before any seller-arm
outcome was seen. Every later change was timestamped before its outcome (Figure 1): five registered
deviations, two production notes, the stop, single unblinded run, and promotion (12:00–12:22 UTC,
28 August), and seven post-stop deployment decisions.
3 Evidence across all three games
3.1 Randomized policy trials
Table 1 reports per-game randomized comparisons on the instrument fleet. Learned pricing gains
in both negotiation roles, concentrated where both values reveal the zone of possible agreement;
hidden-value cells sit at or below the incumbent schedule, so Milton keeps it there.
In bargaining, keying continuation value on the rejected offer did not improve and was retired: its
sample was collected while the pool was hardening, so it undervalued rejection and made the agent
under-ask and over-accept—an off-policy trap. Capping Milton’s asks at the top three agents’ levels
(first offer ≈.57 , counter ≈.58 ; 7,282 observed offers) closed faster (3.8 versus 4.5 rounds) for no
gain (payoff share+0.005±0.018) and was retired.
2

Table 1: Randomized per-game trials, challenger minus incumbent (adjusted percentile; for persuasion,
sales/20 in stratum A, template population). Incumbents: Thompson continuation, incumbent
schedule, honest q=0. The ask cap ran within Milton (27–28 August); the others on the instrument
fleet.
Family Challengern 0/n1 ∆adj. pct.↑(95% CI) Decision
Bargaining rejected-offer continuation 1097/1165−0.022 [−0.043,0.000]retire
(Milton) champion ask cap 232/234−0.028 [−0.080,0.024]retire
Negotiation learned pricing10595/10573+0.071[0.064,0.077]promote
buyer 5355/5316+0.095 [0.086,0.104]
seller 5240/5257+0.046 [0.036,0.056]
Persuasion poolingq=1, stratum A 337/341+0.194[0.147,0.241]promote (A)
Competition outcome and non-stationarity.At the stop (28 August 12:20 UTC) Milton ranked
11th of 460 agents in bargaining (rating 2,169), 38th of 458 in negotiation (2,198), and 138th of 442
in persuasion (1,923; 4,053 games); at the close (30 August 12:00 UTC), 96th of 488 (2,048), 87th
of 482 (2,026), and 111th of 471 (1,974; 6,193 games). The bargaining policy and Milton’s play
were unchanged between the two (agreement 0.99, payoff share 0.49 before and after 29 August), yet
the rating rose to 2,431 (4th) on 29 August and fell nearly 400 within a day, together with all four
instruments’: a rating is a rank within that hour’s pool. The pool also hardens within hours—the
same named bargaining opponents’ acceptance of our near-equal offers fell from 45% to 33% in 18
hours, and walk-forward prediction (16,984 observations) selected a four-hour half-life (forgetting
is the standard remedy [Besbes et al., 2014]). Because the rating step floors at 0.2%, a late entry
costs learning time, not rating (Figure 1). In the final 6.5 hours Milton played only persuasion, the
family whose recent games exceeded its rating (recorded before the fact)—the one family whose rank
improved after the stop (138th to 111th); an instrument on the identical router closed 94th.
Figure 1: Milton’s public display rating versus games played, 21–30 August: per-game records
through 29 August (solid), leaderboard readings to the close (open markers). The rating is a shrunk
moving average, not an inferential outcome; effects in this paper are per-game adjusted percentiles.
3.2 Persuasion: theoretical obedience and observed purchases
Let high quality occur with probability p, value be v, and price be c. If every high unit and a fraction
q of low units are recommended, a Bayesian receiver obeys a recommendation up to the capped
obedience dose
s= p 1−p  v c −1  , q ⋆ = min{1, s},(1)
and stops buying entirely above q⋆. For known v with slack s≥1 , pooling ( q=1) is statically
obedient. Without commitment, however, a recommendation is cheap talk [Crawford and Sobel,
1982]; against a receiver who learns from realized outcomes [Lin and Chen, 2025], credibility is a
stock that lies deplete [Sobel, 1985, Best and Quigley, 2024].
Preregistered causal test.Before observing seller-arm outcomes, the four instruments randomized
q∈ {0, .25, .50, .75,1}by a fixed hash byte in every seller game (20 rounds each). The primary
outcome is sales/20. Stratum A has known v and s≥1 ; B has known v and s <1; H hides v. The
primary test (H1) is q=1 minus q=0 in A; the secondary tests are the same contrast in B (H1b) and the
arm-by-late-round interaction (H2). Tests and dose-response use 6,425 assigned template-population
games (all binary games and template text). Assignment, the 28 August 12:00 UTC stop, tests,
corrections, and exclusions were frozen before unblinding; the primary estimate is the unadjusted
difference in game-level means (HC2 OLS, randomization inference within agent × day × language,
and Holm correction as robustness). Of 7,391 assigned games, 7,372 have complete histories and
3

none an invalid action; realized q was 0.000/0.249/0.499/0.747/1.000 and every high unit was
recommended.
Results (Figure 2).In stratum A pooling raised sales/20 from 0.613 to 0.807 (H1 +0.194, SE
0.024; achieved MDE 0.067; p <10−4, randomization p= 0.0002), 52% of the Bayesian (1−p)
benchmark. In stratum B it lowered sales (H1b −0.067, SE 0.024, Holm p= 0.005), as obedience
theory predicts; sales generally increase with dose in A, decrease in B, and show a smaller overall
increase in H. Within games, purchases under q=1 start at 0.78 in round 1 and converge to the honest
arm’s 0.46 by round 6 (H2, late minus early relative to q=0: −0.123, SE 0.011, p <10 −4)—a
relative decline in purchases omitted by the static benchmark.
Figure 2: Registered dose-response (template population, mean sales/20, 95% CIs) against the
Bayesian-receiver curve in strata A, B, H; per-round purchase rate under honest (q=0) and pooling
(q=1) sellers.
Text games also randomized wording (template 50%, rhetoric 25%, minimal “Yes.”/“No.” 25%,
outcome-adaptive); exploratory (n≈900/460 ): minimal minus template −0.001 ([−0.049,0.047] ),
rhetoric minus template−0.044([−0.092,0.003]); both CIs include zero.
Promotion and validation.By the rule fixed before unblinding (per stratum × channel, promote the
arm whose CI lower bound exceeds the incumbent’s projected sales at its realized dose 0.09), Milton
now pools in stratum A (text 0.755 [0.688,0.823], binary 0.841 [0.798,0.885], versus projections
0.612/0.653) and uses q=0.75 in hidden-value text games (0.492 [0.441,0.542]versus 0.432); the
other cells keep the incumbent. An 8-hour within-instrument A/B of {incumbent, router} (declared;
shortened from 24 h) gave router minus incumbent +0.038 (95% CI [−0.030,0.107] ; n= 248/249):
the gain sits in hidden-value text (+0.109), and stratum A is flat (−0.016) because the incumbent
already ramps to full pooling late in the game there—the rule’s fleet-average projection understated it.
H1 compares pooling with honesty; the estimated deployment gain over the incumbent is smaller
than the dose-response alone suggests. One post-hoc, non-randomized refinement followed on 29
August: three reads at the obedience boundary (1≤s <2 ) were all negative (−0.07 to −0.13) while
s≥2cells gained, so the router now returns the incumbent there.
4 Agent behavior analysis
Does the behavior match the design, and how was that ensured?Alignment was not assumed;
delivered behavior was compared with the design, and it failed three times: (a) for 54 minutes the
language factor delivered the template under the persuasive arm; (b) for about 32 hours Milton’s
negotiation pin never fired, so it ran the instruments’ randomized κ in hidden-value cells; (c) for 94
minutes the first production pooling rule did not fire. All three had one cause—the loop passes the
arm name as the variant. Each got a corrected timestamped activation, and the verification script now
replays recorded payloads through the live dispatch path, asserting per arm the delivered message,
realized dose, and frozen policy hash. Wording delivery is 100%, the instruments produced no invalid
action (Milton’s 18 fall in one incident on 22 August), and seeds permit exact replay.
Behavioral structure and limits.Pooling captures half the Bayesian gain in A, reduces sales
in B, and produces a greater early-to-late purchase decline than honest recommendations. Limits:
game-level inference does not account for repeated-opponent dependence or cross-agent spillovers
in this non-stationary pool. Post-hoc production refinements are non-randomized and language
comparisons exploratory. These competition responses do not establish that deception is desirable
or safe in deployed systems [Scheurer et al., 2023]. Our lesson: calibrate pressure to observed
cooperation.
4

References
Omar Besbes, Yonatan Gur, and Assaf Zeevi. Stochastic multi-armed-bandit problem with non-
stationary rewards. InAdvances in Neural Information Processing Systems 27 (NeurIPS), pages
199–207, 2014.
James Best and Daniel Quigley. Persuasion for the long run.Journal of Political Economy, 132(5):
1740–1791, 2024. doi: 10.1086/727282.
Vincent P. Crawford and Joel Sobel. Strategic information transmission.Econometrica, 50(6):
1431–1451, 1982. doi: 10.2307/1913390.
FAIR, Anton Bakhtin, Noam Brown, Emily Dinan, Gabriele Farina, Colin Flaherty, Daniel Fried,
Andrew Goff, Jonathan Gray, Hengyuan Hu, Athul Paul Jacob, Mojtaba Komeili, Karthik Konath,
Minae Kwon, Adam Lerer, Mike Lewis, Alexander H. Miller, Sasha Mitts, Adithya Renduchintala,
Stephen Roller, Dirk Rowe, Weiyan Shi, Joe Spisak, Alexander Wei, David Wu, Hugh Zhang, and
Markus Zijlstra. Human-level play in the game of Diplomacy by combining language models with
strategic reasoning.Science, 378:1067–1074, 2022. doi: 10.1126/science.ade9097.
Emir Kamenica and Matthew Gentzkow. Bayesian persuasion.American Economic Review, 101(6):
2590–2615, 2011. doi: 10.1257/aer.101.6.2590.
Mike Lewis, Denis Yarats, Yann Dauphin, Devi Parikh, and Dhruv Batra. Deal or no deal? End-to-end
learning of negotiation dialogues. InProceedings of the 2017 Conference on Empirical Methods in
Natural Language Processing (EMNLP), pages 2443–2453, 2017. doi: 10.18653/v1/D17-1259.
Tao Lin and Yiling Chen. Generalized principal-agent problem with a learning agent. InInterna-
tional Conference on Learning Representations (ICLR), 2025. URL https://openreview.net/
forum?id=LqTz13JS2P.
Maya Raifer, Guy Rotman, Reut Apel, Moshe Tennenholtz, and Roi Reichart. Designing an
automatic agent for repeated language-based persuasion games.Transactions of the Association
for Computational Linguistics, 10:307–324, 2022. doi: 10.1162/tacl_a_00462.
Ariel Rubinstein. Perfect equilibrium in a bargaining model.Econometrica, 50(1):97–109, 1982.
doi: 10.2307/1912531.
Jérémy Scheurer, Mikita Balesni, and Marius Hobbhahn. Large language models can strategically
deceive their users when put under pressure.arXiv preprint arXiv:2311.07590, 2023.
Eilam Shapira, Omer Madmon, Itamar Reinman, Samuel Joseph Amouyal, Roi Reichart, and
Moshe Tennenholtz. GLEE: A unified framework and benchmark for language-based economic
environments.arXiv preprint arXiv:2410.05254, 2024. URL https://arxiv.org/abs/2410.
05254.
Joel Sobel. A theory of credibility.The Review of Economic Studies, 52(4):557–573, 1985. doi:
10.2307/2297732.
William R. Thompson. On the likelihood that one unknown probability exceeds another in view of the
evidence of two samples.Biometrika, 25(3–4):285–294, 1933. doi: 10.1093/biomet/25.3-4.285.
5
