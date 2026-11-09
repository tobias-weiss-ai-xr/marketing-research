---
title: 'Per-Market Information Leakage and Order-Flow Skill: Two Methodological Lenses on Informed Trading
  in Decentralized Prediction Markets'
url: https://arxiv.org/abs/2605.02287
category: digital-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Maksym Nechepurenko
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.02287
pages: 22
chars: 76515
fetched_at: '2026-11-08T13:01:42+00:00'
kb_version: 1
---

# Per-Market Information Leakage and Order-Flow Skill: Two Methodological Lenses on Informed Trading in Decentralized Prediction Markets

Per-Market Information Leakage and Order-Flow Skill:
Two Methodological Lenses on Informed Trading
in Decentralized Prediction Markets
Maksym Nechepurenko∗
Preprint v2 (revised) — May 15, 2026
Abstract
April 2026 saw notable methodological convergence in the academic study of informed trad-
ing on decentralized prediction markets. Three methodological approaches surfaced almost
simultaneously, each addressing the same body of documented cases on Polymarket but
operating at different methodological layers: Mitts and Ofir [2026] apply a composite sta-
tistical screen to over210,000wallet–market pairs and estimate $143million in aggregate
anomalous profit; Gomez-Cram et al. [2026] apply an event-level sign-randomization test to
the platform’s complete transaction history, classifying3.14%of accounts as “skilled winners”
who drive most price discovery, and separately apply a single-event lifecycle-and-conviction
heuristic that flags1,950accounts as “insiders”; Nechepurenko [2026b,a] develop theInforma-
tion Leakage Score(ILS) framework, which quantifies per-market information front-loading
at the article-derived public-event timestamp.
This paper provides a methodological comparison and a sketch of how the approaches
combine. The central organizing claim is that these are three distinctlayersof detection,
not three competing methods on a single layer. Sign-randomization, in particular, is best
understood as an account-level test ofpersistent directional skill conditional on opportunity
selection—not a direct test of insider trading, and not a per-market measure. The heuristic
insiderflaginGomez-Crametal.[2026]ismethodologicallyseparatefromtheirskillclassifier,
applies to a population (single-event, recently-created accounts) that the skill classifier ex-
plicitly excludes by design, and has unknown precision against an external labelled set. The
Polymarket sample on which all three approaches are evaluated pools politics, sports, crypto,
and other categories with structurally different information technologies, so a platform-wide
“skilled winner” classification is mechanism-ambiguous and category-conditioned decomposi-
tions are required before the methodology can be used as a surveillance layer.
Against this backdrop, ILSdl provides a complementary per-market quantification. The
January 2026 U.S.–Venezuela operation cluster, where the U.S. Department of Justice in-
dictment of Master Sergeant Gannon Van Dyke [U.S. Department of Justice, 2026] provides
a rare external enforcement benchmark on at least one alleged informed trader, illustrates
how the layers stack: account-level lifecycle heuristics identify a small set of suspicious
accounts with face-valid enforcement alignment; legal investigation establishes whether a
specific trader actually possessed non-public information; per-market scoring would quan-
tify how much information was leaked into each contract before public observation. None of
the three layers subsumes the others, and a combined surveillance pipeline gains in precision
precisely because each layer filters a different dimension of the problem.
Keywords:prediction markets, informed trading, market surveillance, sign-randomization,
information leakage, methodological complementarity, Polymarket, regulatory technology.
JEL Classification:D82, G14, G18, G28, C58.
∗Research Department, Devnull FZCO, Dubai, UAE. Email:maksym@devnull.ae.
1
arXiv:2605.02287v2  [q-fin.TR]  14 May 2026

1 Introduction
Decentralized prediction markets such as Polymarket aggregate dispersed beliefs into continu-
ously updated probability signals on real-world events. They have, since 2024, accumulated a
substantial public-reporting record of suspected informed trading: in the hours before the Oc-
tober 2024 Iran strike on Israel, six newly-created wallets purchased YES shares at prices as
low as ten cents and realized roughly $1.2 million when the market resolved [Mitts and Ofir,
2026]. The 2026 U.S.–Iran conflict cluster traded over $832 million in cumulative volume across
markets that public reporting flagged for anomalous pre-event positioning. The January 2026
U.S.–Venezuela operation produced a contemporaneous wave of pre-event purchases on Maduro-
and Venezuela-related markets, and culminated, on April 23, 2026, in the first U.S. federal in-
dictment for prediction-market insider trading: U.S. Army Master Sergeant Gannon Van Dyke
was charged with using classified information aboutOperation Absolute Resolveto profit roughly
$409,881 across thirteen Polymarket trades [U.S. Department of Justice, 2026, U.S. Commodity
Futures Trading Commission, 2026].
Against this empirical record, the academic literature has, until recently, lacked methodologi-
cally distinct detection frameworks. April 2026 saw three approaches surface in close succession.
1.1 Three approaches surfaced in April 2026
Mitts and Ofir [2026] construct a composite informed-trading screen combining cross-sectional
bet size, within-trader bet size, profitability, pre-event timing, and directional concentration.
They apply the screen to more than210,000wallet–market pairs covering Polymarket activity
from 2023 through early 2026 and estimate that approximately $143 million in aggregate anoma-
lous profit was extracted across the platform. Their methodology operates at the wallet-market
pair level, retrospectively, and yields an anomaly score per pair.
Gomez-Cram et al. [2026], in a working paper posted to SSRN on April 20, 2026 and revised
on April 25, 2026, develop two related methodologies applied to the complete transaction history
of Polymarket, covering 1.72 million accounts, 210,322 markets, and $13.76 billion in trading
volume across 2023–2025. Their primary contribution is a sign-randomization skill classifier
that re-runs each account’s trade history10,000times with the buy/sell direction randomized
at the event level, and classifies the account as skilled, lucky, unlucky, or unskilled based on the
location of realized PnL in the simulated null. They report that3.14%of accounts (54,477in
their test sample, restricted to accounts trading in at least ten events) qualify as “skilled winners”
whose order flow predicts both next-period price changes and final outcomes; together with mar-
ket makers, this minority captures more than30%of total platform gains. The classification
exhibits striking out-of-sample persistence:44%of accounts classified as skilled in a training
subset retain that classification on a randomly held-out test set. Their secondary contribu-
tion, methodologically separate from the skill classifier, is a single-event lifecycle-and-conviction
heuristic that flags1,950accounts as suspected insiders by independent timing and volume cri-
teria. The two components address structurally different populations and have correspondingly
different statistical properties; we discuss them in detail in Section 3.
Nechepurenko [2026b], in a methodology preprint (April 2026), introduce theInformation
Leakage Score(ILS):
ILS(M) = p(Tnews)−p(T open) pTresolve −p(T open) ,
which quantifies, on a single resolved binary market, the fraction of the terminal information
move that was priced in before the corresponding public news event. The authors specify three
operational scope conditions for the score, develop a Murphy-decomposition reading that con-
nects ILS to the proper-scoring-rule literature, and extend the score to deadline-resolved con-
tracts via thedeadline-ILSvariant ILS dl, anchored at an article-derived event timestamp. The
companion empirical paper [Nechepurenko, 2026a] applies the framework end-to-end to the 2026
2

U.S.–Iran conflict cluster, demonstrating that the article-derived anchor distinguishes signal
from proxy artefact on at least one documented case.
1.2 Shared concern, different layers
The three approaches address the same substantive concern—the presence of informed trading
in a public, on-chain prediction-market venue—but each operates at a different methodological
layer.
Mitts and Ofir [2026] and the skill classifier of Gomez-Cram et al. [2026] are wallet-level
methodologies; they produce statements aboutwho, on the platform, behaved anomalously over
their full trading history. The lifecycle-and-conviction heuristic of Gomez-Cram et al. [2026] is
also wallet-level but operates at the per-event level rather than the multi-event level; it produces
statements aboutwhich accounts exhibited a single-event behavioural signature consistent with
informed trading. The ILS framework [Nechepurenko, 2026b] is a market-level methodology;
it produces statements aboutwhich markets exhibited information front-loading prior to public
observation of the underlying event.
These layers are not substitutes. Wallet-level skill classification answers “has this account
demonstrated repeated directional ability across many events?”. Wallet-level lifecycle screening
answers “does this account exhibit the behavioural signature of a single-event informed trader?”.
Market-level information-leakage scoring answers “on this specific contract, how much of the
eventual move from opening price to resolution had been priced in before public observation?”.
The U.S. Department of Justice indictment of Van Dyke [U.S. Department of Justice, 2026]
illustrates the practical relevance of holding all of these questions simultaneously: prosecution
required(i)identifyingwhichspecifictraderisallegedtohavehadaccesstoclassifiedinformation,
which is a regulatory and legal investigation rather than a statistical inference; (ii) quantifying
which contracts the trader profited on and by how much, which is closer to a per-market measure;
and (iii) establishing a behavioural pattern of suspicious activity, which is closer to the lifecycle-
and-conviction signature. Each of the academic methodologies under consideration contributes
to one or two of these dimensions; none addresses all of them.
1.3 Contribution
This paper provides:
1. A taxonomy of detection methods for prediction markets that organizes the approaches by
methodological layer and unit of analysis (Section 2).
2. Aseparateanalysisofwhatthesign-randomizationskill classifierofGomez-Crametal.[2026]
measures (persistent directional skill conditional on opportunity selection), and what their
single-event lifecycle-and-conviction heuristicmeasures (face-valid behavioural screen with
unmeasured precision); these are two methodologically distinct components of their paper
that should not be conflated (Section 3).
3. A category-heterogeneity argument: the Polymarket sample on which all approaches are
evaluated is dominated by sports, politics, and crypto markets with structurally different
information technologies, so a platform-wide skill classification is mechanism-ambiguous and
category-conditioned decompositions are required for surveillance use (Section 3.1).
4. A parallel analysis of the ILS framework (Section 4).
5. A layered analysis of the January 2026 U.S.–Venezuela operation cluster, where the Van
Dyke indictment provides external enforcement evidence on at least one alleged informed
trader, the Gomez-Cram et al. [2026] heuristic flags three accounts whose realized PnL aligns
3

with the indictment to the dollar on the lead account, and ILSdl would in principle quantify
per-contract front-loading (Section 5).
6. A sketch of a combined surveillance pipeline usingcategory-conditioned account risk scoring
as Stage 1 (rather than a naive “run sign-randomization classifier and flag heuristic insiders”
workflow), ILSdl as Stage 2, and human compliance review as Stage 3 (Section 6).
7. Identification of three open questions that none of the methodologies in their current form
addresses: resolution-criteria uncertainty, continuous pre-event trade collection, and cross-
market coordination (Section 7).
Reproducibility note.The discussion of Gomez-Cram et al. [2026] in this paper is based on
the working paper text and tables, including Appendix B (the Maduro case study) and the topic-
decomposition tables in the main appendix. The underlying account-level classifications, the
labelled list of1,950heuristic-flagged accounts, the category-conditioned skill decompositions,
and the source code for the sign-randomization procedure have not, to our knowledge, been
released as a reproducible artifact. The Polymarket transaction history on which their analysis is
built is publicly available on-chain, so the methodology is reproduciblein principleon an aligned
account population by any researcher with sufficient infrastructure for full-history transaction
processing; we did not undertake such reproduction in the present comparative work, and we
mark this constraint as a binding limitation on operational use of the methodology in Sections 3.4
and 6.
2 A taxonomy of detection methods
We organize prediction-market informed-trading detection methodologies by three structural
dimensions:granularity(the unit of analysis),timing applicability(whether the method op-
erates retrospectively or in real time), andoutput type(anomaly score, skill classification, or
interpretable per-unit measure). Table 1 summarizes the three approaches under consideration.
2.1 Layers and the questions they answer
Each row of Table 1 answers a distinct operationally meaningful question about prediction-
market informed trading.
Wallet-level retrospective scoring on (wallet, market) pairsasks: “Among observed
wallet–market pairs, which exhibit a statistical signature of anomalous performance?” Mitts
and Ofir [2026]’s composite screen aggregates several features (cross-sectional bet size, within-
trader bet size, profitability, pre-event timing, directional concentration) into a single anomaly
score and identifies the upper tail. This methodology is well-suited to retrospective surveys of
platform-wideinsideractivityandtoestimatingeconomicmagnitudes(e.g., the$143Maggregate
figure). It does not provide a real-time signal, because profitability is only known at resolution,
and it does not separate skill from luck explicitly.
Wallet-level skill-vs-luck classification on accounts with sufficient trading history
asks: “Among the population of accounts that have traded enough events to permit statistical in-
ference, what fraction can be distinguished from luck-driven outcomes?” The sign-randomization
classifier of Gomez-Cram et al. [2026] addresses this question on accounts trading in at least ten
events. The test is statistically well-calibrated, with a clean null hypothesis (event-level ran-
domization of trade direction) and per-accountp-values, and the authors document a striking
4

Table 1: Taxonomy of detection methodologies for informed trading on prediction markets
surfaced in 2024–2026. “Wallet–market” granularity means the unit of analysis is a (wallet,
market) pair; “account, multi-event” means the wallet alone, aggregated across markets and
conditioned on a minimum-event threshold; “account, single-event” means the wallet at the per-
event level; “market” means the market alone, aggregated across wallets. The two components
of Gomez-Cram et al. [2026]—the skill classifier and the lifecycle-and-conviction heuristic—are
listed separately because they answer different questions and apply to different populations.
Method Granularity Timing Output Information used
Compositeanomaly
screen [Mitts and
Ofir, 2026]
Wallet–market
pair
Retrospective Anomaly score
on (wallet, mar-
ket) pairs
Bet size, profitability,
pre-event timing, direc-
tional concentration
Sign-randomization
skill classifier
[Gomez-Cram
et al., 2026]
Account, multi-
event (≥10
events)
Retrospective 4-category skill
classification
with calibrated
p-values
Full PnL distribution
under randomized
event-level directions
Lifecycle-and-
conviction heuristic
[Gomez-Cram
et al., 2026]
Account, single-
event
Retrospective Binary flag:
1,950accounts
in their sample
Account creation time,
single-event focus, post-
resolution dormancy,
volume and profit
thresholds
ILS / ILS dl
[Nechepurenko,
2026b]
Market Post-event, pre-
resolution
Per-market score
with scope-
condition gate
Price trajectory
[Topen, Tresolve], an-
chor atT news orT event
skill-persistence finding:44%of skilled accounts retain their classification out-of-sample, com-
pared to roughly10%in published studies of equity mutual-fund managers. The methodology
is, however, fundamentally retrospective and excludes the one-shot insider population by design.
Wallet-level lifecycle-and-conviction screening at the per-event levelasks: “Among
accounts trading a specific event, which exhibit the behavioural signature (recent creation, single-
event focus, post-resolution dormancy, sufficient volume and conviction) of a one-shot informed
trader?” The lifecycle heuristic in Gomez-Cram et al. [2026] addresses this question. It is
methodologically separate from the skill classifier: it applies to accounts the skill classifier ex-
cludes, uses different inputs (account creation timestamps and per-event activity windows rather
than full PnL distributions), and produces a binary flag rather than a graded skill score. Its
precision against an external ground-truth set has not been reported in the released paper.
Market-level information front-loadingasks: “On a specific resolved market, what frac-
tion of the terminal information move was priced in before the corresponding public news event?”
The ILS framework [Nechepurenko, 2026b] operates at this layer. The output is a per-market
score with explicit scope conditions; it is interpretable in terms of the Murphy decomposition
of the Brier score; and the relevant price trajectory is observable onceTevent has been iden-
tified, enabling post-event, pre-resolution scoring without requiring final resolution outcomes.
Wallet-level attribution is not part of the methodology proper.
2.2 What the layers leave to each other
Each layer produces information the other two cannot produce, and each leaves to the others
questions it does not address.
5

The wallet-level approaches do not, on their own, identifywhich contractsthe wallets traded
with informational advantage; they aggregate across all markets in which a wallet was active.
A skilled wallet whose skill consists of identifying mispricings in NBA prop markets is, by
sign-randomization, indistinguishable from a wallet whose skill consists of trading on classified
geopolitical information. The market-level approach makes the question per-market explicit: a
high ILSdl on a specific Maduro market is a different statement from a high ILSdl on a NBA
market.
The market-level approach, conversely, does not on its own identifywhich walletswere re-
sponsible for the front-loading. A market with high ILSdl may have been moved by a single
wallet with classified information, by a coordinating group of wallets, or by a large number of
independent traders responding to a leak in semi-private channels. Wallet-level methods address
this in the same way the present comparison treats their methodology: as a complementary layer,
not a substitute.
3 What sign-randomization measures
We summarize the methodology of Gomez-Cram et al. [2026] as documented in their working
paper, then characterize what the methodology captures well and what it cannot do. The
discussion in this section relies on the working paper text and on the appendix tables therein;
we have not independently reproduced the underlying classification on Polymarket data.
The Gomez-Cram et al. paper combines two methodologically distinct components: a sign-
randomizationskill classifierthat operates over each account’s full trading history, and a sepa-
ratesingle-event lifecycle-and-conviction heuristicthat flags accounts the skill classifier explicitly
cannot identify. We discuss the two components separately because they answer different ques-
tions, have different statistical properties, and require different operational treatment.
3.1 Sign-randomization skill classifier
For each account in the Polymarket population, the authors construct the realized profit-and-
loss trajectory across the account’s full trading history. They then construct a counterfactual
distribution of PnL trajectories by holding all trades fixed in event, market, contract size, price,
and timing, and randomizing only the buy/sell direction. The randomization is applied at the
event level: all trades within a single event are correlated under the null, both to capture position-
building within a market and to capture related bets across multiple markets within the same
event (e.g., simultaneously buying “Trump wins” and “Harris loses”). The procedure is repeated
10,000times.
The realized PnL is then compared to the simulated null distribution and the account is
assigned ap-value. Accounts withp <0.05are classified asskilled winners(54,477accounts in
the test sample,3.14%of the population); accounts withp >0.95areunskilled losers(110,703
accounts,6.4%); the remainder arelucky winners(positive realized PnL, no statistical signif-
icance,29.0%) orunlucky losers(negative realized PnL, no significance,61.4%). A residual
category of market makers (0.1%) is identified separately by liquidity-provision behaviour.
The headline aggregate findings of the classifier are: skilled winners plus market makers,
comprising under3.5%of accounts, capture more than30%of platform gains; lucky winners
(29%of accounts) capture the remaining69%; unlucky and unskilled losers (67%of accounts)
absorb the entirety of platform aggregate losses. The skill classification exhibits out-of-sample
persistence: of accounts classified as skilled in a training subset of events,44%retain that
classification on a randomly held-out test set, in contrast to roughly10%retention for skilled
mutual-fund managers in published equity-fund persistence studies.
6

What the skill classifier measures.The natural reading of the skill test is that it mea-
surespersistent directional profitability conditional on the account’s chosen opportunity set. The
randomization holds fixed which events the account chose to trade, which markets within those
events, what size positions it took, and when it took them; it varies only the directional side
(buy vs. sell) of each event-level decision. The test therefore answers the question: “given this ac-
count’s chosen events, markets, sizes, and timing, was its realized direction unusually profitable
relative to a randomized-direction counterfactual?”
This is methodologically stronger than naive top-PnL ranking—which treats winners and
losers symmetrically without correcting for the bimodal resolution structure of binary outcome
markets, and which would incorrectly attribute large lucky payouts to skill—but it is alsonar-
rowerthan a direct test of insider trading. The test does not ask, and does not answer:
•whether the trader’s information was private rather than public;
•whether private information, if held, was illegally obtained or constituted material non-public
information (MNPI) in the regulatory sense;
•whetherthetraderwasaninsiderinanyspecificoperationaldefinition(e.g., theU.S.statutory
“Eddie Murphy Rule” under Dodd-Frank Section746);
•on which specific markets within an account’s history the directional skill was concentrated;
•whether the directional skill reflects superior public-information processing (e.g., faster news
ingestion, better statistical modelling, on-chain analytics for crypto markets, public weather-
model output for meteorological markets) or genuinely non-public information.
A skilled sports bettor specialised in NBA injury-news ingestion, a crypto on-chain ana-
lyst trading whale-flow patterns, a weather modeller trading hurricane probabilities, an ar-
bitrageur exploiting cross-platform pricing inefficiencies, a journalist with industry contacts,
and a classified-information geopolitical insider can all appear as “skilled winners” under sign-
randomization. The mechanisms behind their skill are categorically different, and the regulatory
significance of the trading is correspondingly different.
Category heterogeneity in the underlying sample.The Polymarket sample on which the
classifier is evaluated is structurally heterogeneous in its information content. Sports markets
account for42.05%of all markets and35.37%of total trading volume; politics markets account
for7.52%of markets and35.85%of volume; crypto markets account for36.96%of markets
and18.73%of volume; the remaining categories (culture, economy, technology, finance) jointly
accountforunder10%ofvolume[Gomez-Crametal.,2026, TableA.2]. Together, sports, politics,
and crypto cover roughly89%of platform volume, and these categories rest on entirely different
information technologies. “Skill” in NBA prop markets is the ability to ingest injury news and
lineup updates faster than the consensus; “skill” in cryptocurrency markets is the ability to read
on-chain analytics and exchange flow signals; “skill” in geopolitical markets may, on the upper
tail, involve access to genuinely non-public state information.
A platform-wide skilled-winner classification therefore conflates qualitatively different pop-
ulations. The54,477skilled accounts include sports bettors, crypto analysts, weather mod-
ellers, scheduled-news traders, arbitrageurs, and on the upper tail, accounts whose realized
profit is consistent with informed trading on private information. Without category-conditioned
decomposition—a per-category classification that reports skilled-winner rates, profit shares,
and persistence rates separately for sports, politics, crypto, and the remaining categories—the
platform-wide statistic is mechanism-ambiguous and cannot be used as a direct surveillance
signal.
7

One-shot insiders are excluded from the skill test by construction.A statistically
reliable sign-randomizationp-value requires repeated decisions: the test gains power as the
number of independent event-level decisions in an account’s history increases. Gomez-Cram
et al. [2026] restrict their main classification analysis (Figure2of their paper) to accounts that
traded in at least ten events, on the grounds that fewer events do not permit reliable skill-
vs-luck separation. This is statistically reasonable; it has, however, an immediate operational
consequence for surveillance: a one-shot informed trader—an account opened specifically to
trade on classified information for a single event, then closed—fails the ten-event threshold
and falls outside the skill classifier’s scope. The authors themselves note in their Maduro case-
study analysis that the three suspicious accounts are classified aslucky winnersrather than
skilled winners, “as the sign-randomization test cannot identify skill from a single informed
trade” [Gomez-Cram et al., 2026, Section 4.4].
This is not a defect of sign-randomization; it is a design choice with a known scope. But
it means that the skill classifier alone is unsuited to detecting the canonical insider-trading
pattern that has dominated the public-reporting record on Polymarket: an account opened in
the days before a single high-stakes event, taking a concentrated position, and going dormant
after resolution.
3.2 Single-event lifecycle-and-conviction heuristic
To address the population the skill classifier cannot reach, Gomez-Cram et al. [2026] apply a
separate two-criterion heuristic. An account is flagged as a “suspected insider” if it satisfies
both:timing—the account is created within seven days before an event and places no further
trades after that event resolves—andconviction—the account trades exclusively in that one
event, with at least $1,000in volume and at least $1,000in realized profit. The authors report
that this heuristic flags1,950accounts across the Polymarket sample, with mean realized profit
per flagged account of $15,012.92and median of $2,758.29. Insider order imbalance (i.e., the
net buy direction of flagged accounts) predicts both next-period price changes (t= 2.54) and
final market outcomes (t= 8.65) at high statistical significance; insider trading volume does not
significantly reduce absolute pricing error.
What the heuristic measures.The heuristic identifies accounts whoselifecycle behaviour
is consistent with a stylized informed trader: open shortly before an event, trade concentrated
in that one event, exit after resolution. It is a behavioural signature, not a mechanism test. The
authors are explicit that this is a face-valid screen rather than a calibrated insider classifier, and
they motivate it by reference to the Maduro case study before applying it to the full sample.
What the heuristic does not measure.The lifecycle-and-conviction signature is consistent
with several populations besides classified-information insiders:
•Curious new userswho join the platform during a viral or high-attention event, place a single
sizable bet, and do not return when the event resolves. The 2024 U.S. presidential cycle and
the 2026 Iran conflict cluster both attracted substantial influxes of first-time accounts.
•Sybil and promotional farms: accounts opened structurally on a per-event basis to harvest
airdrop campaigns, referral bonuses, or platform promotions, which by design exhibit single-
event activity and post-resolution dormancy.
•Single-strategy botsdeployed for one specific event and then disabled.
•Privacy-rotating accountsof legitimate traders who, for operational-security reasons, segre-
gate their activity into per-event accounts.
8

•Single-event public-news traderswho placed an informed bet based on publicly available in-
formation that the consensus had not yet absorbed—a population that overlaps in behaviour
with insiders but is not regulatorily equivalent.
The aggregate1,950count is therefore not a precise estimate of insider accounts; it is an
upper bound on the population of accountswhose lifecycle behaviour is consistent with informed
single-event trading. The strong predictive performance of insider order imbalance on price and
outcome (reported in the authors’ Table 6, Panel B) is consistent with the heuristic having high
recall on real informed trades—true insiders, when present, do exhibit this lifecycle pattern—but
the precision of the heuristic against an external ground-truth set has not, to our knowledge,
been reported. Without such a precision study, the operational use of the1,950accounts as a
surveillance flag would yield an unknown but plausibly substantial false-positive rate.
3.3 What sign-randomization, as a whole, captures and does not capture
Combining the two components, the Gomez-Cram et al. [2026] methodology contributes the
following:
•A statistically calibrated population-level distribution of persistent directional skill, with
strong evidence that price discovery on Polymarket is concentrated in a small minority and
that the platform aggregate cannot be modelled as a uniform-skill / lucky-draw process.
•A documented out-of-sample skill-persistence finding (44%retention) that contrasts sharply
with the corresponding mutual-fund literature.
•A face-valid lifecycle heuristic that captures conduct consistent with informed trading when
applied to the Maduro case study, and whose order-imbalance regressions show strong con-
temporaneous price-prediction power.
The methodology does not, in either component, provide:
•A direct identification of insider trading in the regulatory sense; only conditional directional
skill (skill classifier) or lifecycle suspicion (heuristic).
•Acategory-conditioneddecomposition; theplatform-wideskilled-winnerstatisticismechanism-
ambiguous in a sample dominated by sports, politics, and crypto.
•A real-time signal on active markets; both components require resolved outcomes and final
PnL.
•A per-market quantification; the unit of analysis is the account, aggregated across markets.
•A separation of resolution-criteria uncertainty from informed front-loading; markets that
misprice for criteria-ambiguity reasons (Iran-Apr30 in Nechepurenko [2026a] is an example)
generate spurious skill or unskill classifications under the test.
3.4 Reproducibility
Gomez-Cram et al. [2026] describe their data construction and methodology at the level of detail
customary for a finance working paper. The underlying account-level skill classifications, the
labelled list of1,950heuristic-insider accounts, the category-conditioned decompositions, and
the source code for the sign-randomization procedure have not, to our knowledge, been released
as a reproducible artifact. The Polymarket transaction history on which their analysis is built
is publicly available on-chain, so the methodology is reproduciblein principleon an aligned
account population by any researcher with sufficient infrastructure for full-history transaction
processing; we did not undertake such reproduction in the present work.
9

For operational use as a surveillance layer, the absence of released account labels is a binding
constraint: the1,950flagged accounts cannot be cross-referenced against an external compliance
database or against subsequent enforcement actions without independent reproduction. The
strongest research finding of Gomez-Cram et al. [2026]—that price discovery on Polymarket is
concentrated in a small minority of skilled accounts—stands on its own as a contribution to the
platform-economics literature regardless of whether the underlying classifications are released.
The operational use of the methodology in a surveillance pipeline, however, requires either the
release of labels or independent reproduction with category-conditioned decomposition. We
return to this point in Section 6.
4 What ILS dl measures
We now perform the parallel analysis on the deadline-ILS framework of Nechepurenko [2026b,a].
4.1 Methodology recap
For a deadline-resolved binary marketMwith first trade atTopen, contractual deadlineTdeadline,
recovered public-event timestampT event ∈[T open, Tdeadline], formal resolution atT resolve, and
binary outcomep Tresolve ∈ {0,1}:
ILSdl(M) = p(T − event)−p(T open) pTresolve −p(T open) ,
wherep(T − event)is the market price one minute before public observation of the underlying
event. The score is admitted only when three scope conditions are all met: (i) theedge-effect
condition|p(T open)−0.5| ≤0.4, requiring substantive uncertainty at market opening; (ii) the
non-trivial-movecondition|∆ total| ≥ε(we useε= 0.05), requiring a measurable terminal
move so that the denominator of the score is well-conditioned; and (iii) theanchor-sensitivity
condition that the score be robust to small perturbations ofTevent. Markets that fail any of these
conditions—including markets with|∆ total|< ε(trivial total move), opening prices near0or
1(consensus markets), or numerically unstable scores under anchor perturbation—are excluded
from analysis rather than scored unreliably. The framework adoptsθ Topen ≡p(T open)as a
conservative baseline and a per-category exponential survival functionS(τ) = exp(−λτ)for the
time-to-event distribution, with hazard rateλfitted by maximum likelihood on a comparable
population.
The empirical companion paper [Nechepurenko, 2026a] demonstrates the framework end-to-
end on the largest applicable case in the FFIC inventory: “US forces enter Iran by April 30,” a
$269M-volume contract for whichTevent =April 3, 2026 (F-15E special operations entry) was
recovered via LLM-assisted multi-source verification. The article-derived anchor yieldsILSdl =
+0.113; the resolution-anchored proxy (Tresolve−1 h) yields−0.331; the two values lie on opposite
sides of zero and differ by0.444in magnitude.
4.2 What the methodology captures well
Per-market interpretability.The output of the framework is one number per market, with
anexplicitinterpretation:ILS dl(M) = 0.6meansroughly60%oftheeventualmovefromopening
price to resolution had been priced in before public observation of the underlying event. This is
the natural unit for a regulator or platform officer asking a contract-specific question, and it is
the natural unit for a research investigator constructing case studies.
Post-event, pre-resolution applicability.The score depends only on the price trajectory
up to timetand on the recoveredTevent when known; it does not require resolution outcome or
10

final PnL. For a market that is currently active,ILSdl can be computed up toTevent as soon as
the public event is identified. We emphasize that this ispost-event, pre-resolutionapplicability
rather than pre-event real-time monitoring: the score is well-defined after the underlying event
has been identified in public reporting, but before the contract has formally resolved through the
platform’s oracle. A pre-event alarm in the strict sense—a signal raisedbeforethe underlying
event occurs, based on price-trajectory features alone—is a separate methodological problem
that the framework does not currently address. The companion methodology paper develops
the architectural consequences of post-event causal inference: every feature used at inference
time is causal in the public information available at that time.
Scope conditions are explicit, not implicit.The three scope conditions (edge effect, trivial
resolution, anchor sensitivity) are stated as preconditions for interpreting the score; markets
failing them are excluded from analysis rather than scored unreliably. This is methodologically
conservative: the framework prefers a smaller domain of confident application to a larger domain
of noisy results.
Connection to proper scoring rules.Through the Murphy decomposition of the Brier
score, ILS admits an interpretation as the share of the resolution component of the Brier score
accumulated beforeT news [Nechepurenko, 2026b]. This connects label generation to a well-
developed literature on probabilistic forecasting and provides a theoretical grounding the score
does not borrow from elsewhere.
Resolution-criteria uncertainty is separable.The Iran-Apr30 case study [Nechepurenko,
2026a] demonstrates that ILSdl measures something distinct from market-level resolution-criteria
uncertainty. A market that mispredicts its eventual outcome because participants are uncertain
about resolution criteria can still produce a coherentILSdl at the article-derived anchor; the
score does not conflate the two phenomena.
4.3 What the methodology cannot do
Population-level skill distribution is not produced.The score does not, on its own,
classify wallets or characterize the dispersion of trader skill on the platform. For population-
economics questions of the form “what fraction of accounts is skilled?”, ILSdl is not the relevant
tool.
Tevent measurement error.The framework anchors the score at an article-derivedT event
recovered from public reporting. In practice, public information about an event diffuses through
multiple channels that may precede a publishable news article: real-time social media (Telegram
channels, Twitter, Discord), government press hints, on-the-record briefings to wire services, and
informed participant commentary in the market itself. The recoveredT event is therefore the
timestamp of the earliest reproducible news source, not necessarily the timestamp at which the
information first became available to a sufficiently networked participant. To the extent that
information leaks earlier through informal channels, the article-derived anchor systematically
over-estimates the pre-event window and under-estimates the leakage measured by ILSdl. The
companionempiricalpapernotesthisconcernbutdoesnotcharacterizeitsmagnitude; anexplicit
study of inter-source timestamp dispersion would be a natural next-stage refinement.
Denominator instability.The scope condition|∆ total| ≥εguards the denominator of the
score against numerical instability when the terminal move is small. The thresholdε= 0.05is a
practical choice and not a calibrated cut. Markets near this threshold produce ILSdl values that
are admitted under the condition but are sensitive to small perturbations inp(Topen)orp Tresolve;
11

the companion methodology paper recommends reporting the score together with a sensitivity
range over the threshold.
Interpretationofnegativeandover-unityvalues.Thescorecantakevaluesin(−∞,+∞)
in principle. Negative values indicate that∆pre moved in the opposite direction from∆total: the
price was moving against the eventual outcome before the public event. Values greater than one
indicate that the price had already moved beyond the resolution level before the public event
and subsequently retraced. Both regimes are diagnostic but require careful interpretation. In
particular, ILSdl >1is consistent with either strong informed front-loading followed by partial
retracement, or with resolution-criteria uncertainty causing the market to overshoot before re-
anchoring on the final outcome [the Iran-Apr30 case study in Nechepurenko, 2026a, illustrates
the latter]. The methodology paper provides the formal interpretation of these regimes but
does not, in the present companion empirical paper, examine the populations of negative-ILS or
over-unity-ILS markets in detail.
Wallet attribution requires per-trade data not currently in scope.The companion
empirical paper [Nechepurenko, 2026a] reports that wallet-level features for the FFIC cluster
were constrained by the available trade history to the resolution-settlement window, owing to
The Graph subgraph indexer’s coverage policy. The signature “cross-market wallet coordination
atT − event” that one would naturally want to test alongside ILSdl is not retrievable retrospectively
from the Polymarket subgraph; it requires continuous per-trade collection fromTopen onward as
a separable infrastructure investment.
Sample-size limited by pipeline requirements.Computing ILS dl end-to-end requires re-
covered article-derivedT event, complete CLOB price coverage fromTopen, scope-condition com-
pliance, and positive lead timeτ=T event −T open. Of the eighteen substantive markets in the
2026 U.S.–Iran cluster at which the empirical companion paper attemptsTevent recovery, only
one satisfies all four requirements. The pipeline is methodologically demanding, and population-
scale empirical evaluation of the framework is gated on infrastructure improvements rather than
on the methodology itself.
Article-derivedT event recovery is not free.Each recoveredT event involves an LLM call
with multi-source web verification (approximately $0.09per market in the companion paper’s
pipeline)andhumanreviewforhigh-stakescases. Thiscomparesunfavourablytosign-randomization,
which requires only the on-chain trade history that is already public.
4.4 Where these limits matter
For population-level economics questions about prediction-market structure, the framework is
silent. For per-account skill ranking across the full corpus, the framework is silent. The method-
ology operates one market at a time, and for many empirical questions of platform interest, that
is the wrong unit.
5 The Maduro / Venezuela Cluster as a Layered Test Case
The January 2026 U.S.–Venezuela operation cluster offers a case study where the methodological
layers under consideration can be observed to stack constructively, and where the U.S. Depart-
ment of Justice indictment of Master Sergeant Gannon Van Dyke [U.S. Department of Justice,
2026] provides an external enforcement benchmark on at least one alleged informed trader. We
examine the cluster from each layer in turn. We emphasize that the cluster is a layeredtest
caserather than a completed three-method convergence: the lifecycle-and-conviction screen of
12

Gomez-Cram et al. [2026] and the legal fact pattern of the DOJ indictment are observed in the
cluster, while ILSdl is onlyproposedon these markets and not actually computed in the present
comparative paper.
5.1 The cluster as a cross-methodological test case
Operation Absolute Resolvewas a U.S. military operation, executed in the predawn hours of
January 3, 2026, that resulted in the apprehension of Venezuelan President Nicolás Maduro and
his wife in Caracas. The operation had been in classified planning since at least December 8,
2025, with active execution-planning involvement of multiple U.S. Army Special Forces person-
nel. On April 23, 2026, the U.S. Department of Justice unsealed an indictment charging Master
Sergeant Gannon Van Dyke, an active-duty Army Special Forces soldier with documented oper-
ational involvement in the planning and execution ofOperation Absolute Resolve, with thirteen
Polymarket trades placed between December 27, 2025 and January 2, 2026. Van Dyke realized
approximately $409,881in profit on these trades. The markets named in the DOJ indictment
include “U.S. Forces in Venezuela by January 31, 2026,” “Maduro out by January 31, 2026,”
“Trump invokes War Powers against Venezuela by...,” and “Will the U.S. invade Venezuela by
January 31, 2026.”
The corresponding Polymarket contracts in the FFIC inventory [Nechepurenko, 2026b] are
11markets with approximately $89M cumulative volume:7contracts that resolved YES on or
shortly after January 3, 2026, and4context contracts (deadline-miss or strict-criterion NO out-
comes) that resolved NO. The cluster is thus a deadline-contract cluster of the form documented
as the dominant structural type in the public-reporting record on Polymarket insider trading.
The convergence between the three methodological approaches is summarized in Table 2.
We treat each in turn.
5.2 What sign-randomization identifies on the cluster
Gomez-Cram et al. [2026, Appendix B and Table B.1] report a case study of three Polymarket
accounts that took sizable positions in Maduro-related markets in the days and hours before the
January 3, 2026 operation. The three accounts and their reported activity, as documented in
the working paper, are summarized in Table 3.
All three accounts satisfy the timing-and-conviction heuristic of Section 3.2: each was created
within seven days before the Maduro event; each traded predominantly in the “Maduro out by
January 31, 2026?” contract; each met the volume and profit thresholds; and two of the three
went dormant entirely after their Maduro positions resolved [the third placed a single $4,000
trade in an unrelated market before going dormant; see Gomez-Cram et al., 2026, Section B].
The accounts’ realized profits collectively exceed $630,000, with conviction visible in the working
paper’s Figure B.1: the three accounts placed an unusually large order of approximately80,000
shares late on January1, followed by six transactions of comparable size around midnight on
January3, before the price rose sharply.
Table 4 summarizes the evidentiary status of each component of the layered analysis on this
cluster.
Face validity but no exact-identity attribution from the paper alone.The temporal
alignment between the first flagged account and the U.S. Department of Justice indictment is
striking. The first row of Table 3 reports a realized PnL of $409,882.03; the DOJ indictment
of Master Sergeant Gannon Van Dyke alleges that he “profited approximately $409,881” across
thirteen Polymarket trades on Maduro- and Venezuela-related contracts [U.S. Department of
Justice, 2026]. The two figures match to the dollar, and the dates are consistent with Van
Dyke’s alleged trading window of December 27, 2025 through January 2, 2026 [U.S. Commodity
Futures Trading Commission, 2026]. Taken together, the public-record evidence is consistent
13

Table 2: Layered methodological readings of the January 2026 U.S.–Venezuela operation cluster.
The DOJ indictment of Van Dyke (April 23, 2026) provides external enforcement evidence on at
least one alleged informed trader. Numerical claims about Gomez-Cram et al. [2026] are drawn
from the working paper text and tables, including Appendix B; account-level labels for the1,950
flagged accounts are not part of the released paper.
Approach Output on the cluster What it does not produce
Sign-randomization skill
classifier [Gomez-Cram
et al., 2026]
Skill classifier excludes one-
shot accounts (ten-event min-
imum); the three Maduro-
cluster accounts therefore ap-
pear as “lucky winners” in the
skill classification, not skilled
Detection of one-shot informed trading;
per-contract front-loading; whetherspe-
cificmarkets were anomalously priced ver-
sus reasonable consensus
Lifecycle-and-conviction
heuristic [Gomez-Cram
et al., 2026]
Three accounts
flagged:0x31a...b8ed9,
0x6ba...a94c5,
0xa72...febd4. Com-
bined PnL $626,484. The first
account’s PnL of $409,882
matches the DOJ indictment’s
quoted Van Dyke profit of
$409,881to the dollar.
Per-contract front-loading; precision
against full1,950-account flagged popula-
tion (Maduro provides face validity, not
full-population precision)
DOJ indictment [U.S. De-
partment of Justice, 2026]
One trader identified by name
and role; $409,881profit
across 13 trades; specific mar-
kets named
A general detection methodology; the in-
dictment provides external enforcement ev-
idence on this case but not a generalizable
test
ILSdl framework [Nechep-
urenko, 2026b,a]
Would provide per-market
ILSdl on the7YES-resolved
contracts; not executed in this
paper
Wallet-level identification of which ac-
counts moved each market
with the first flagged account corresponding to an account allegedly used by Van Dyke. We do
not, however, have access to a verified mapping between the abbreviated address0x31a...b8ed9
and the specific account(s) named in the legal proceedings, and Gomez-Cram et al. [2026] do
not in their working paper assert such a mapping; we therefore restrict ourselves to noting the
consistency of the public-record evidence rather than asserting an identity match.
Heuristic recall and what the case study does and does not demonstrate.The
Maduro case study provides strong face-valid evidence that the lifecycle-and-conviction heuristic
captures conduct consistent with informed trading: at least one of the three flagged accounts is
highly likely, on the public-record evidence, to correspond to a trader subsequently charged crim-
inally in connection with classified information about the underlying event. This is informative
about the heuristic’srecallon enforcement-aligned cases—when a documented insider trades,
the heuristic appears to flag the relevant accounts—but it does not establish the heuristic’spre-
cisionon the full1,950-account flagged population. Most of the flagged accounts will not have
associated DOJ enforcement actions; whether the remaining∼1,947accounts include other
genuine insiders, sybil-farm accounts, viral-event newcomers, or single-strategy bots cannot be
determined from the case study alone.
What sign-randomization does not produce on the cluster.The sign-randomization
skill classifier proper doesnotidentify the Maduro accounts; the three accounts trade in only
one event each and therefore fail the ten-event threshold for the skill test. The authors explicitly
14

Table 3: The three accounts flagged by Gomez-Cram et al. [2026, Appendix B, Table B.1] in the
Maduro / Venezuela cluster case study. All three traded the contract “Maduro out by January
31, 2026?” before the public announcement ofOperation Absolute Resolveon January 3, 2026.
Account addresses are reported in abbreviated form in the working paper; the full addresses
have not been released.
Address (abbr.) Created (UTC) Last traded (UTC) PnL ($) V olume ($)
0x31a...b8ed92025-12-27 05:05 2026-01-04 00:03409,882.03 33,933.26
0x6ba...a94c52026-01-03 03:42 2026-01-12 22:30141,619.92 25,089.86
0xa72...febd42026-01-02 21:44 2026-01-02 21:4474,982.34 5,782.66
Total profit across the three accounts626,484.29
note this: “Under our baseline classification, these accounts appear in the lucky winners group
rather than among skilled winners, as the sign-randomization test cannot identify skill from
a single informed trade” [Gomez-Cram et al., 2026, Section 4.4]. The Maduro detection is
therefore wholly attributable to the lifecycle-and-conviction heuristic, not to the skill classifier.
This reinforces the methodological-separation point of Section 3: the two components of Gomez-
Cram et al. [2026] answer different questions and apply to different populations.
The Gomez-Cram analysis, taken together, also does not produce a per-contract decomposi-
tion of the cluster. Van Dyke’s alleged trades span4distinct contracts with different deadlines,
different specific event criteria (Maduro custody vs. U.S. forces in Venezuela vs. U.S. invasion
vs. presidential War Powers invocation), and different YES/NO outcomes. From the case study
alone, one cannot say “on this specific deadline contract,X%of the move from opening price to
resolution had been priced in before January 3, 2026 at 10:00 UTC, while on this other contract
the corresponding figure isY%.”
5.3 What ILS dl would provide on the cluster
We propose, but do not execute in this paper, the application of the ILSdl framework to the
7YES-resolved markets in the cluster. The pipeline is identical to the Iran-Apr30 application
reported in Nechepurenko [2026a]: for each market, recover the article-derivedTevent (in the
Maduro cluster,T event is January 3, 2026 at approximately 10:00 UTC, the time of the public
announcement), check scope conditions, computeILSdl against the article-derived anchor, and
report the per-market score together with short-window variants.
The expected output, by methodological design, is a vector of seven per-contract scores
quantifying, individually for each contract in the cluster, how much of the eventual move from
opening price to resolution had been priced in before January 3, 2026 at 10:00 UTC. This
per-contract decomposition is structurally absent from both components of Gomez-Cram et al.
[2026] and structurally absent from the DOJ indictment’s per-trader summary.
We defer the actual computation to a separate work because the seven-market application
requires (i) Tier 3 LLM-assistedTevent verification on each market, (ii) confirmation of CLOB
price coverage fromT open for each market, (iii) scope-condition checks per market, and (iv) a
methodologically careful accounting of the resolution-criteria differences across the seven con-
tracts. The companion empirical paper’s reported coverage rate of18%of positive-τmarkets
having full CLOB price coverage suggests that not all seven markets will be evaluable end-to-end
with the present infrastructure; partial application is the realistic expectation.
15

Table 4: Evidentiary status of each layered component on the Maduro / Venezuela cluster. “Re-
ported” means the claim is documented in the cited source; “not released” means the underlying
labels or data are not publicly available; “not executed” means the analysis is proposed in the
present comparative paper but not carried out.
Component Status Source / note
Sign-randomization skill classi-
fication of cluster accounts
Reported (lucky winners,
not skilled)
Gomez-Cram et al. [2026, Section 4.4];
one-shot accounts excluded from skill test
by ten-event threshold
Lifecycle-and-conviction
heuristic case study (3 ac-
counts)
Reported with full Ap-
pendix B detail
Gomez-Crametal.[2026, AppendixB,Ta-
ble B.1]
Heuristic-flagged account la-
bels (full1,950population)
Not released Account labels, code, and category-
conditioned decompositions are not part
of the released paper
Maduro account-to-trader
identity mapping
Not released; consistent
with public-record evi-
dence to the dollar on
lead account
Gomez-Cram et al. [2026]; U.S. Depart-
ment of Justice [2026]
DOJ enforcement on Van Dyke
(alleged informed trader)
Public allegation, not yet
conviction
U.S. Department of Justice [2026]; U.S.
Commodity Futures Trading Commission
[2026]
ILSdl scores on the seven YES-
resolved cluster contracts
Not executed Proposed in Section 5.3 of the present pa-
per; pipeline expansion required
5.4 How the layers stack on this cluster
The DOJ indictment of Van Dyke alleges, on the basis of a fact-finding investigation, that a
specific named individual had access to classified information and traded on it. The lifecycle
heuristic of Gomez-Cram et al. [2026] flags a small set of three accounts behaviourally consistent
with informed trading, the leading account’s PnL aligning with the indicted profit figure to the
dollar. The ILS dl methodology, in the application proposed but not executed in this paper,
would identify which contracts in the cluster moved most strongly relative to public information
arrival, and would quantify the per-contract magnitude.
These layers are in principle complementary; on the present cluster only two of them are
empirically observed (lifecycle screening and legal investigation). The role of ILSdl in this case
is to specify the missing per-contract quantification layer, not to claim it has been measured.
For a regulator or platform compliance officer aiming to:
•identifywhomto investigate, the lifecycle-and-conviction heuristic of Gomez-Cram et al.
[2026]—once category-conditioned and reproduced with released account labels—is the nat-
ural population-level filter;
•quantifyhow muchinformation was extracted onwhichspecific contract, ILS dl is the natural
per-market measure;
•establishwhethera specific trader actually possessed non-public information, neither method-
ology is sufficient—this is the proper domain of legal and regulatory investigation, which
addresses questions that statistical inference cannot.
The layers stack. The Maduro / Venezuela cluster does not show that one approach is correct
and the others wrong; it shows that each layer answers a question the others do not, and that
16

for a high-profile case with public enforcement evidence, two of the three layers are observed
and the third specifies the missing per-contract quantification that would complete the picture.
6 A combined surveillance pipeline
We sketch a three-stage surveillance pipeline that integrates the two academic methodologies
under consideration. The pipeline is not a proposal for production deployment; we offer it as an
organizing framework for thinking about how the two layers compose.
6.1 Stage 1 — category-conditioned account risk scoring
Stage 1 runs on a periodic batch schedule (e.g., monthly) over the platform’s complete on-chain
trade history. The naive form of Stage 1—“run sign-randomization classification, output flagged
accounts”—is, on the analysis of Section 3, insufficient as a surveillance layer. We sketch a
stronger form that we will refer to ascategory-conditioned account risk scoring.
The inputs to Stage 1 are:
•Per-account sign-randomization skill classification, computed separately within each target
category (politics, sports, crypto, finance, etc.) rather than pooled at the platform level.
This produces a per-account, per-category skill statistic that is mechanism-anchored: a
sports-category skill is interpretable as injury-news / line-shading / arbitrage skill; a politics-
categoryskillisinterpretableintermsofpublic-newsingestionor, ontheuppertail, suspected
leak-driven trading. We note that category-conditioning trades interpretability for statistical
power: an account that traded fifteen events overall but only two in geopolitics will have an
underpowered within-category skill statistic for geopolitics, even if its pooled multi-category
statistic was significant. Operationally, this means that the category-conditioned classifier
will produce reliable per-category skill labels only for accounts that meet a within-category
minimum-event threshold, and the population covered by Stage 1 will accordingly be smaller
than the pooled-classification population.
•Per-account lifecycle-and-conviction heuristic flags as in Section 3.2, computed at the per-
event level. This catches the one-shot informed-trader pattern that the skill classifier explic-
itly cannot reach.
•Per-account composite anomaly score along the lines of Mitts and Ofir [2026], applied se-
lectively to markets of regulatory interest (markets with sufficient volume and event-class
membership).
•Per-account context features: wallet age, funding-source provenance (CEX-deposit vs. on-
chain mixer), known sybil-cluster membership, account participation in airdrop or promo-
tional campaigns, position concentration within events of interest, and any known cross-
platform identifiers.
•Category-specificpriorriskweights: ahighskillscoreinasportsmarketisweighteddifferently
from a high skill score in a geopolitical-event market, because the regulatory implications of
skill in those domains differ. The weights are themselves a calibration parameter, and the
methodology should support auditing and revision as ground-truth cases accumulate.
The output of Stage 1 is a per-account risk score that is mechanism-aware: an account
that scores high on sports skill, has a wallet age of two years, and has funding entirely from
a regulated CEX is treated differently from an account that scores high on geopolitics skill,
was opened seven days before a high-stakes military event, and has funding from a privacy-
preserving mixer. Accounts above a category-conditioned threshold are flagged forward to Stage
17

2; the cardinality of the flagged set is tunable by the threshold and by the category-specific
weights.
Stage 1 alone produces high false-positive rates if used as a sole filter for surveillance ac-
tion, because each input feature has its own false-positive distribution and category-conditioned
aggregation does not eliminate this. It is a triage stage, not a terminal one. The naive “run
sign-randomization classifier and flag the1,950heuristic insiders” workflow is, in our reading,
insufficient on three grounds: it pools categorically heterogeneous skill into a single number; it
relies on a heuristic with unmeasured precision; and the underlying account labels would, for op-
erational use, need to be reproduced and released, which has not yet been done by Gomez-Cram
et al. [2026].
6.2 Stage 2 — per-market scoring on flagged-wallet markets
Stage 2 operates on individual markets after a public event timestamp has been identified and
before formal resolution. For each market in which one or more flagged accounts has taken
a significant position—a threshold that is itself a calibration parameter, but in the simplest
version, “flagged account holds≥X%of long-side notional”—Stage 2 computes ILS dl against
the current best estimate ofTevent, together with short-window variants. Markets in which no
flagged account holds a significant position are not scored, so the per-market computational cost
is bounded by the number of flagged-account-active markets at any given time, which is small
relative to the platform’s total open-market count.
The output of Stage 2 is a per-market score gated by scope conditions. Markets failing
the scope conditions (high opening-price extremes, trivial-resolution moves, anchor-insensitive
scores) are not flagged forward. Markets passing the scope conditions and exhibitingILS dl
above a calibration threshold, in conjunction with a short-window variant above its threshold,
are flagged forward. The companion empirical paper [Nechepurenko, 2026a] proposes a starting
threshold ofILS dl >0.25jointly with a short-window variant exceeding0.10, drawn from a
single observation and explicitly preliminary.
6.3 Stage 3 — human review on jointly-flagged contracts
Stage 3 applies human compliance review to the contracts surfaced by Stage 2: contracts where
a flagged-account population holds significant positionandwhere the per-market ILSdl exceeds
threshold. The expected cardinality of Stage 3 is small enough to be tractable for human review
on a continuing basis, by construction: the joint of Stage 1’s wallet filter and Stage 2’s market
filter is much smaller than either alone.
Stage 3 is where the surveillance system interfaces with regulatory or law-enforcement pro-
cesses; the academic methodologies do not directly produce indictments or platform suspensions,
and we do not attempt to specify Stage 3 in this paper.
6.4 Comparison to single-method approaches
A single-method approach using only Stage 1 (wallet classification) is informative for population-
economics characterization and identifies populations of interest, but it produces a flagged-
account count—approximately1,950for the heuristic insider category—that is too large for
manual investigation as a routine surveillance practice and too imprecise for direct regulatory
action. A single-method approach using only Stage 2 (per-market scoring) operates at the right
unit for individual contract investigation but, without the wallet-level filter, applies to all open
markets passing scope conditions and is computationally and operationally undirected.
The pipeline of the form Stage 1→Stage 2→Stage 3 inherits the methodological strengths
of both layers and pushes the false-positive rate of each into a regime where joint flagging is
plausibly tractable for human review. We emphasize again that this is an architectural sketch,
18

not a calibrated proposal: each stage’s threshold is an empirical question we do not address here,
and the tractability claim is therefore qualitative.
7 Open questions neither methodology addresses
We close by identifying three open questions that none of the three methodologies under consid-
eration, in their current form, addresses.
7.1 Resolution-criteria uncertainty
The Iran-Apr30 case study [Nechepurenko, 2026a] illustrates a phenomenon that is methodolog-
ically distinct from informed trading: a market that broadly mispredicts its eventual resolution
outcome because participants are uncertain about how the contract’s resolution criteria will be
applied to ambiguous events. In the Iran-Apr30 case, the market priced down to near-zero on
consensus that the F-15E rescue operation did not constitute “U.S. forces entering Iran,” and
was subsequently resolved YES by the UMA Optimistic Oracle.
Sign-randomization classifies the NO-buyers in this market as “unskilled losers,” which is
misleading; they were in fact responding to publicly observable information about an ambiguous
criterion, not exhibiting absence of skill. ILSdl produces a coherent score against the article-
derivedT event, but the score does not separate “front-loading on informed prediction of the
underlying event” from “front-loading on informed prediction of how the criterion would be
interpreted”—if such a separation is even meaningful. A diagnostic that explicitly separates
resolution-criteria uncertainty from informed front-loading would complement both wallet-level
methods and per-market scoring; we are not aware of such a diagnostic in the present literature.
7.2 Continuous pre-event trade collection
Both methodologies are constrained, in their applicability to specific cases, by the retrospective
availability of per-trade history. The companion empirical paper [Nechepurenko, 2026a] reports
that Iran-cluster trade history was retrievable only from the resolution-settlement window on-
ward, owing to The Graph subgraph indexer’s coverage policy on low-volume markets at the
time of indexing decision. Gomez-Cram et al. [2026] have access to the full Polymarket transac-
tion history because they query at population-scale retrospectively; per-market real-time access
requires continuous collection fromTopen for each open market in the target categories.
This is an infrastructure problem rather than a methodological one, but it is the binding
constraint on both approaches’ application to surveillance use cases. Continuous per-trade
collection would unblock real-time wallet-level features (for sign-randomization-style methods)
and enable wallet-level diagnostics on ILSdl-flagged markets. The methodological approaches
under consideration depend on such infrastructure existing.
7.3 Cross-market coordination
Neither sign-randomization nor ILSdl directly addresses coordination patterns across multiple
related markets. Sign-randomization aggregates an account’s history across all markets; it does
not test whether an account’s trades on MarketAare correlated with another account’s trades
on MarketBin ways suggestive of coordinated information flow. ILSdl scores individual markets;
it does not test whether high ILSdl on MarketAis statistically correlated with high ILS dl on
MarketBfor related underlying events.
The Iran-cluster wallet analysis in Nechepurenko [2026a], although limited by trade-history
availability, identified332walletsactiveinbothoftwoclustermarketsintheresolution-settlement
window. With pre-event trade collection in place, a cross-market coordination diagnostic would
test whether such overlap is statistically anomalous prior to the underlying event, conditional
19

on the events’ related underlying causes. The Maduro/Venezuela cluster, with7YES-resolved
markets sharing a single underlying event (Operation Absolute Resolve), is a natural test bed.
8 Conclusion
Multiple methodologically distinct approaches to detecting informed trading on Polymarket
emerged in close succession in early 2026: a wallet-market composite anomaly screen [Mitts and
Ofir, 2026], a wallet-level sign-randomization skill classifier together with a separate single-event
lifecycle-and-conviction heuristic [Gomez-Cram et al., 2026], and a market-level information-
leakage score [Nechepurenko, 2026b,a]. The strongest organizing claim of this paper is that
these are distinctlayersof detection rather than competing methods on a single layer. Sign-
randomization, in particular, identifies persistent directional skill conditional on opportunity se-
lection; this is a substantively different question from identifying insider trading in the regulatory
sense. The Polymarket sample on which the methodology is evaluated combines economically
heterogeneous categories (sports, politics, crypto, finance) with structurally different informa-
tion technologies, so a platform-wide skill classification is mechanism-ambiguous and should be
category-conditioned before deployment in a surveillance context. The lifecycle-and-conviction
heuristic captures the canonical one-shot insider pattern that the skill classifier excludes by
design, but its precision against an external ground-truth set has not been reported and its op-
erational use in a surveillance pipeline requires both reproduction with released account labels
and validation against known cases.
The Maduro / Venezuela cluster illustrates how the layers stack constructively. The lifecycle
heuristic of Gomez-Cram et al. [2026] flags three accounts whose realized profits collectively ex-
ceed $626,000, with the lead account’s PnL of $409,882matching the U.S. Department of Justice
indictment’s quoted Van Dyke profit of $409,881to the dollar—a striking face-valid alignment
that establishes recall on at least this case while leaving precision on the full population an
open question. Legal and regulatory investigation [U.S. Department of Justice, 2026, U.S. Com-
modity Futures Trading Commission, 2026] addresses whether a specific named trader actually
possessed non-public information, which is not a question that any statistical methodology can
answer. ILSdl would in principle quantify, contract by contract, how much information was front-
loaded into each of the seven YES-resolved markets in the cluster before public observation of
the underlying event; this per-contract decomposition is structurally absent from both Gomez-
Cram et al. [2026] components and from the DOJ indictment. On the present cluster, two of the
three layers are empirically observed (lifecycle screening and legal investigation), and the third
specifies the missing per-contract quantification that would complete the layered analysis.
Three open questions—resolution-criteria uncertainty, continuous pre-event trade collection,
and cross-market coordination—remain outside the scope of the methodologies under consider-
ation and define a research agenda for the next stage of the field. The combined surveillance
pipeline sketched in Section 6 uses category-conditioned account risk scoring as Stage 1 (rather
than a naive “run sign-randomization classifier” workflow), ILSdl as Stage 2, and human com-
pliance review as Stage 3. Each stage has known limitations; the value of the composition is
precisely that the limitations of each stage are partially offset by the strengths of the others.
We close with a constructive note. The Gomez-Cram et al. [2026] paper is, in our reading,
a substantial contribution to the platform-economics literature on prediction markets, with a
calibrated methodology, a striking skill-persistence empirical finding, and a documented case
study aligned with subsequent enforcement action. The recommendations in this paper for
category-conditioned decomposition, account-label release, and methodological separation be-
tween the skill classifier and the lifecycle heuristic are directed at the operationalization of the
methodology for surveillance, not at the academic contribution of the paper. We expect that
with such operationalization, sign-randomization-style classification and ILSdl-style per-market
scoring will compose into a substantially stronger surveillance capacity than either methodology
20

alone provides.
Revision note (v2)
This v2 revision is a coordinated update with the companion methodology and empirical papers
[Nechepurenko, 2026b,a]. Two findings from the platform data audit motivate the revision: (i) a
category-labeling correction reclassifying15,542esports markets (predominantly Counter-Strike)
out of the military / geopolitical category, and (ii) an expansion of the Tier-3 event-timestamp
recoverysampleusedinthecompanionempiricalpaperfromthev1budget-cappedsubset(n= 9)
tothefullavailableTier-3population(n= 18)formilitary/geopoliticalmarkets. Thev1hazard
estimate (ˆλ= 0.306, half-life2.3d) lies inside the v2 95% confidence interval[0.143,0.365], so
the two estimates are statistically consistent; the v2 point estimate isˆλ= 0.241with half-life
2.9d and KS adequacyp= 0.426.
The methodological comparison developed in this paper is unaffected by either finding. The
taxonomy of detection layers (Table 1), the analysis of category heterogeneity (Section 3), the
separation between the sign-randomization skill classifier and the lifecycle-and-conviction heuris-
tic, and the layered reading of the U.S.–Venezuela operation cluster (Section 5) all stand as
written in v1. Cross-references to the companion empirical paper’s hazard estimates now re-
solve to the v2 values via the updated bibliography. Three accompanying datasets are released
openly with this revision:polymarket-tnews-tevent-recovery-v1,polymarket-hazard-rates-v1, and
polymarket-ils-corpus-v1, all athttps://github.com/ForesightFlow/datasets.
Generative AI Disclosure
In preparing this manuscript, the author used Anthropic’s Claude Opus 4.7 for copy-editing,
structural review against an external referee report, and rendering of tables from numerical
data. All methodology, analysis, and conclusions are the author’s own; the author reviewed and
edited all AI-generated content and takes full responsibility for the final manuscript.
References
Roberto Gomez-Cram, Yunhan Guo, Theis Ingerslev Jensen, and Howard Kung. Prediction
market accuracy: Crowd wisdom or informed minority? SSRN Working Paper 6617059,
posted April 20, 2026, revised April 25, 2026, April 2026. URLhttps://ssrn.com/abstract=
6617059.
Joshua Mitts and Moran Ofir. From Iran to Taylor Swift: Informed trading in prediction markets.
SSRN Working Paper No. 6426778, 2026.
Maksym Nechepurenko. Empirical evaluation of deadline-resolved information leakage on
documented Polymarket insider cases. arXiv:2605.02286 [q-fin.TR]. SSRN Working Paper
6687398, doi:10.48550/arXiv.2605.02286. Companion empirical paper, May 2026a. URL
https://arxiv.org/abs/2605.02286.
Maksym Nechepurenko. ForesightFlow: An information leakage score framework for
prediction markets. arXiv:2605.00493 [q-fin.TR]. SSRN Working Paper 6687361,
doi:10.48550/arXiv.2605.00493. Companion methodology paper, May 2026b. URLhttps:
//arxiv.org/abs/2605.00493.
U.S. Commodity Futures Trading Commission. CFTC charges active-duty U.S. army master
sergeant in connection with first-ever prediction-market insider-trading action. CFTC press
release and complaint, April 2026.
21

U.S. Department of Justice. U.s. soldier charged with using classified in-
formation to profit from prediction market bets. Office of Public Af-
fairs press release, April 2026. URLhttps://www.justice.gov/opa/pr/
us-soldier-charged-using-classified-information-profit-prediction-market-bets.
22
