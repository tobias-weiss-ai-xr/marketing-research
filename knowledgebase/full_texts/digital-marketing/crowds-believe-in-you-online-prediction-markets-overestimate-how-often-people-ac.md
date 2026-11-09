---
title: 'Crowds Believe in You: Online Prediction Markets Overestimate How Often People Achieve Their Own
  Goals'
url: https://arxiv.org/abs/2610.40324
category: digital-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Zihan Chen
- Lei Nico Zheng
- Di Zhu
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.40324
pages: 23
chars: 98304
fetched_at: '2026-11-08T13:23:38+00:00'
kb_version: 1
---

# Crowds Believe in You: Online Prediction Markets Overestimate How Often People Achieve Their Own Goals

CROWDSBELIEVE INYOU:
ONLINEPREDICTIONMARKETSOVERESTIMATE
HOWOFTENPEOPLEACHIEVETHEIROWNGOALS
Zihan Chen
Stevens Institute of Technology
Hoboken, NJ, USA
zchen61@stevens.edu
Di Zhu
Stevens Institute of Technology
Hoboken, NJ, USA
dzhu1@stevens.edu
Lei Nico Zheng
University of Massachusetts Boston
Boston, MA, USA
lei.zheng@umb.edu
ABSTRACT
People increasingly share personal goals online and invite others to forecast them. Research on the
planning fallacy finds that observers predict a person’s behavior less optimistically than the person
does, and prediction markets aggregate such judgments, harnessing the wisdom of crowds. We study
6,150 prediction markets on Manifold in which 1,660 users asked about their own futures (“Will I
. . . ?”), reconstruct every order and execution, and compare these self-markets with markets about
external events. Self-markets resolved YES 4.4 percentage points less often than their final prices
implied, whereas external markets were nearly calibrated (0.9 points); the difference was 2.2 points
at the same price level and 1.9 points within creators who made both kinds of market. Absent when
markets opened, the overstatement emerged within a day of trading, even where the person never
traded, and peaked in the week before close. In a market’s first day, observers moved external-market
prices down toward the base rate, but moved self-market prices 3.6 points further toward YES, except
in markets naming an outcome the person would not want, which were not overpriced. The correction
came late and largely from the person, whose orders supplied 38% of the eventual movement toward
the outcome in self-markets, against 9% in external markets. Because self-market prices mainly
failed to separate successes from failures, a recalibration learned from earlier markets improved later
forecasts by only 1.5%. Crowds believe in the futures people pose for themselves, and the information
that would correct them lies with the person.
Keywordsprediction markets · wisdom of crowds · planning fallacy · self-prediction · social prediction · forecast
calibration·online communities
1 Introduction
People increasingly announce their goals online and invite others to follow along: fitness apps share workouts with
friends [1, 2], habit trackers post streaks, and productivity communities run public accountability threads. Some
platforms go further and let others bet. On the prediction-market platform Manifold, users routinely open markets on
questions such as “Will I go to the gym three times this week?”, “Will I finish my thesis draft by Friday?”, or “Will I
stay off social media in March?”, and other users trade on them with the platform’s currency. These markets turn an old
question in social psychology, how well other people can predict what a person will do, into prices that can be checked
against what happened.
Research on the planning fallacy gives a clear prediction. People forecasting their own behavior are optimistic: they
underestimate how long their tasks will take, overestimate their own follow-through, and build their forecasts around
their plans rather than their past [3–5]. Observers forecasting the same behavior lean on base rates and past behavior
and are less optimistic [3, 6, 7]; when predicting generosity or test performance, they are also more accurate [ 6, 7].
Prediction markets should add to this advantage, because trading pools the judgments of many observers and rewards
those who correct mispricing [8, 9]. Markets about one person’s future are thin, however, and price distortions in thin
arXiv:2610.40324v1  [cs.HC]  29 Oct 2026

markets can persist for weeks [10]. Whether a market of observers forecasts a person well is therefore an empirical
question.
We answer it with the public record of Manifold. From the 194,347 markets created on the platform between 2021
and 2026, we study 6,150 resolved self-markets, in which 1,660 people asked about their own futures, and compare
them with external markets, which concern events outside anyone’s own life. We rebuild each market’s price path and
every executed purchase from the platform’s order records. This lets us compare prices with outcomes at fixed points
in a market’s life, attribute each price change to the person or to observers, and compare the purchases of the person,
of observers who had interacted with the person before, and of strangers in the same market. Two research assistants
checked the reconstruction against the live platform, recomputed our estimates independently, and labelled a stratified
sample of questions and comments to validate our coding.
Crowds believe in people too much. Self-markets resolved YES 4.4 percentage points (pp) less often than their final
prices implied. External markets made by other creators, by contrast, were close to calibrated: their outcomes occurred
about as often as their prices implied. The difference held at the same price level and within creators who made both
kinds of market. It was not present at the opening, when self-markets were, if anything, underpriced relative to external
markets; it arose with trading. Within a day of opening, self-markets resolved YES less often than external markets at
the same price, the difference was largest a week before close, and it appeared in markets in which the person never
traded. In a market’s first day, observers sold external markets down toward the lower rate at which such events occur,
but they barely moved markets about people’s own goals, and where the person never traded they did not move those
prices down at all. The information that corrected prices came late and largely from the person, whose orders supplied
38% of the movement toward the outcome in self-markets, against 9% in external markets. Markets naming outcomes
the person would not want, such as relapsing or falling ill, were not overpriced, and observers who had interacted with
the person before did not pick winning sides more often than strangers.
The study makes three contributions. First, it provides field evidence on how crowds forecast a specific person. The
observer advantage documented in the lab did not appear in markets that pay for accuracy: prices overstated the futures
people posed for themselves, the overstatement held across several benchmarks and at fixed forecasting times, and it
emerged from observers’ trading rather than from the person’s opening. Second, it traces where the bias arises and
what corrects it. Observers brought to events, but not to people, the outside view: the habit of judging a case by how
similar cases usually turn out. The person, who holds the information that decides the outcome, supplied much of the
correction near the end. The bias was absent where the question named an outcome the person would not want, and it
did not depend on whether observers had interacted with the person before. Third, it offers practical and methodological
guidance. Self-markets were less accurate mainly because their prices separated successes from failures less well, so a
statistical correction recovers little; the missing ingredient is information held by the person. For research on trading
platforms, we show that order records must be read as executions: treating each order as a trade distorts both prices and
participation.
The paper proceeds as follows. Section 2 reviews research on predicting one’s own and other people’s behavior and
on prediction markets, and derives the research questions. Section 3 describes the setting, the data, the reconstruction
of prices and executions, and the measures. Section 4 reports the results in the order of the research questions, and
Section 5 discusses their implications and limitations.
2 Background and Research Questions
2.1 Predicting one’s own behavior and predicting someone else’s
People are poor forecasters of their own conduct. They underestimate how long their tasks will take [3], overestimate
how often they will act generously [ 6], and expect to follow through on intentions they later abandon [ 4, 11]. The
planning-fallacy literature traces this optimism to how self-predictions are built: people construct a plan-based scenario
for the task at hand and set aside relevant past experience, even when that experience shows similar plans failing
[3, 5, 12]. Current intentions receive heavy weight, while the factors that decide whether intentions become behavior
receive little [4, 13]. Because intentions explain only part of later behavior [14], a forecaster who reads intentions as
outcomes will be too optimistic.
Observers are the classic remedy. In the original planning-fallacy studies, observers given information about another
person’s task predicted later completion times than the person did and drew more on past experience [ 3]. Peers
predicting someone’s exam score or lab performance are less optimistic, and therefore more accurate, than the person,
because they weight past achievement over aspiration [7]. Predictions about other people’s generosity are close to the
truth while predictions about oneself are not, partly because people consult base rates when predicting others [6]. In the
2

terms of Kahneman and Lovallo [15], observers adopt the outside view: they treat the case as one instance of a class
and ask how such cases usually turn out, the logic that reference-class forecasting builds on [16].
2.2 Two ways observers can fall short
The observer advantage rests on two conditions. The observer must be indifferent to the outcome, and the observer
must have a reference class and a record to reason from. Each condition suggests a way in which observers could lose
their advantage.
The first is motivation. Wanting an outcome can raise its judged probability [17, 18]. Direct evidence for this desirability
bias is more mixed than its familiarity suggests [ 19], but it is clear in several settings. Incentives tied to quick
completion make time predictions more optimistic by drawing attention to plans and away from past experience [20],
and desirability-driven optimism survives months of feedback and accuracy incentives [ 21, 22]. Bettors back the
outcomes they want against the odds [23]. Observers who know and like a person, or who have just read the person’s
hopeful plan, may forecast on that person’s behalf as the person would. On this motivated account, the bias follows
what the person wants: outcomes the person hopes for are overpriced, outcomes the person fears are underpriced, and
the bias is strongest among the person’s friends and supporters.
The second is a lack of information. Knowledge about a person is unevenly distributed: the person knows their own
intentions and current progress, people close to them know their habits, and strangers know little of either [24, 25]. A
stranger asked whether this person will run every day this week knows little of the person’s habits and has no obvious
reference class. What the stranger does have is the question, which states the person’s goal, and the person’s own
trades, if any. A forecaster who sees the plan but not the history behind it is in the position that, in the lab, makes actors
optimistic. Describing a possibility explicitly also raises its judged probability [ 26]. On this informational account,
observers’ trades carry little information about the outcome, prices move toward the truth mainly when the person
reveals what they know, and observers with more contact with the person forecast better than strangers.
2.3 Prediction markets and the limits of aggregation
Prediction markets are designed to correct individual errors. Traders who disagree with the price can profit by moving
it, so prices aggregate dispersed information and tend to be well calibrated [8, 9]. Aggregation does not require every
trader to be unbiased: in election markets many traders let their preferences color their trades, yet prices stay accurate
because marginal traders set them [ 27], and traders who try to push prices away from the truth can even improve
accuracy by attracting informed traders who profit from correcting them [28]. Play-money markets forecast sports about
as well as real-money markets [29], although real money improved accuracy for other events [30]. Manifold’s own
play-money markets are well calibrated, with accuracy comparable to that of traditional prediction-market platforms
[10]. In a large forecasting tournament, market prices were also more accurate than the simple average of forecasters’
probability judgments [31].
Correction, however, requires informed traders who are willing to trade, and even active markets show systematic biases.
Long shots are overpriced and favorites underpriced [32, 33], more so the longer the time to expiration [34]. Prices can
underreact to information when traders hold different beliefs and limited wealth [35], and social influence can erode the
independence that crowd accuracy relies on [36]. On Manifold itself, randomly placed trades moved prices for weeks,
and the effect was larger in markets with fewer traders and less volume [10]. A distortion that few informed traders
oppose can therefore survive aggregation.
2.4 Betting on a person
Online platforms now let people turn their goals into public, priced forecasts. Commitment devices that put money
or reputation at stake can change behavior [ 37, 38], and personal-informatics and self-improvement systems use
sharing, social feedback, and game elements to sustain effort [1, 2, 39, 40]. Behavior spreads through online ties [41],
and making intentions public is double-edged: intentions that others notice can be enacted less intensively, because
acknowledgment produces a premature sense of having reached the goal [42].
A market about one person’s goal is an unusual forecasting object. Its subject controls the outcome, usually reports
it, and can trade alongside everyone else. Its observers range from people who have followed the person for years to
strangers who arrived through the platform’s feed. Its question is the person’s own framing of their future. The person’s
record on earlier goals is visible on their profile, but their progress on the current one is visible only through what they
choose to say or trade. Such markets are also thin, which by the evidence above leaves room for prices to drift from the
truth.
3

2.5 Research questions
Lab research predicts that a crowd of observers should be close to calibrated about a person’s future, and if anything
pessimistic. Both accounts above predict that it will not be, for different reasons, and they disagree about where the
error lies and who could correct it. Four research questions follow.
The first question is whether the crowd overstates a person’s future at all. RQ1 asks whether prices in markets about a
person’s own future overstate how often the named outcome occurs, relative to prices in markets about external events.
If they do, the overstatement could be inherited from the opening price that the person sets, or it could arise as observers
trade. RQ2 therefore asks when it arises (at the opening, with trading after the opening, or near the close) and whether
it arises in markets in which the person never trades. The two accounts also disagree about who holds the information
that would correct the price. RQ3 asks whose orders move self-market prices toward the eventual outcome, and how the
person’s purchases compare with those of observers in the same market. Finally, RQ4 confronts the accounts with the
markers each emphasizes. It asks whether the overstatement is associated with the desirability of the named outcome
and with the observers’ relationship to the person, which the motivated account stresses; with cues that anyone can see,
such as the person’s earlier record and their silence in the market; with the person’s history on the platform; or with
the type of goal. Because a systematic overstatement could in principle be removed by a correction learned from past
markets, we close by asking how much such a correction recovers. Of these questions, RQ1 and RQ2 are primary, RQ3
is secondary, and RQ4 is exploratory (Section 3.5).
3 Method
3.1 Setting
Manifold is an online prediction-market platform on which any user can open a market on a yes-or-no question and
other users trade on it with mana, the platform’s currency. An automated market maker sets prices, which are read as
the probability that the question resolves YES; traders can also post limit orders that rest until another order fills them.
The market’s creator writes the question, chooses the opening probability and closing date, may trade in the market
like anyone else, and resolves it when the outcome is known. Markets are public, and every order is time-stamped and
available through the platform’s public interface [43]. Questions from the platform have been used as a forecasting
benchmark [44], and its markets have been used for field experiments on price manipulation [10].
Many users open markets about themselves: whether they will go to the gym three times this week, finish a draft by
Friday, stay off social media for a month, or be admitted to a program. We call these self-markets, and we refer to the
creator of a self-market, whose behavior is being forecast, as the person. The person controls the outcome, usually
reports it, and can watch and join the trading. Everyone else in the market is an observer, forecasting another person’s
behavior with mana at stake.
3.2 Data and sample
We retrieved the full list of markets available through the platform’s public interface on 22 and 23 October 2026
(194,347 markets created from 2021 to 2026), and for the sampled markets every order and comment. All requests
succeeded, and markets were deduplicated by their identifiers. A market is eligible when it is binary, denominated
in mana, resolved YES or NO, had at least two unique traders according to the platform, and received at least one
purchase by someone other than its creator before it closed. Markets resolved to a probability or cancelled have no
binary outcome and are excluded; Appendix A reports how often each kind of market ended this way and how the
comparison would change if they were included.
A market is a self-market when its question asks, in the first person, about the creator’s future: it begins with “Will I”,
“Can I”, “Shall I”, or “Am I going to”, optionally after a bracketed tag or a short time phrase such as “By Friday,”. The
sampling frame used a broader first-person rule. Questions that look back (“Did I”), ask for advice (“Should I”), or
ask about a present state (“Do I”, “Am I”) were set aside (120 markets); including them leaves the results unchanged.
External markets contain no first-person reference of any kind (no I, me, my, we, us, or our) and therefore concern
events outside the creator’s own life, such as elections, sports, technology releases, or platform milestones. Questions
with other first-person content, such as markets about a creator’s relatives or about “we”, belong to neither group.
The sample contains every eligible self-market and two sets of external markets. The main benchmark is a random
draw of external markets from creators who never opened a first-person market about themselves, stratified by creation
quarter so that its timing matches that of the self-markets. The second set comprises up to five randomly chosen external
markets from every creator of a self-market. It shows how markets made by the same people behave when the question
is not about them, and it supports comparisons within creator. Table 1 describes the 6,150 self-markets from 1,660
4

Table 1: Analysis sample.
External markets
Self-markets Other creators Self-market creators
Markets 6,150 6,272 4,486
Creators 1,660 2,624 1,222
Creation years 2022–2026 2022–2026 2021–2026
Share resolved YES 45.0% 41.9% 40.0%
Mean opening price 49.8% 49.4% 49.7%
Opened at the default 50% 95% 90% 95%
Mean final price 49.4% 42.8% 41.2%
Final price between 20% and 80% 37% 17% 18%
Observers per market, median (mean) 9 (13.6) 12 (22.0) 12 (25.3)
Observer purchase volume per market, median (mana) 383 1,542 1,388
Days from creation to close, median 23.7 33.1 45.1
Creator traded before the final price 60% 60% 61%
Creator commented before the final price 50% 26% 38%
Creator silent (no trade, no comment) 22% 32% 25%
At least one encouraging observer comment 9.1% 0.5% 1.0%
Observer purchases placed by programs 20% 18% 17%
Observer purchases filling a limit order 25% 25% 23%
Note: Binary, mana-denominated markets resolved YES or NO with at least one observer purchase before close.
Self-markets ask a forward-looking question about the creator (“Will I . . . ?”); external markets contain no first-person
reference. “Other creators” never opened a first-person market about themselves; “self-market creators” are the creators
of the self-markets. Observers are traders other than the creator. Shares of purchases are averaged over markets.
creators, the 6,272 external markets from 2,624 other creators, and the 4,486 external markets from 1,222 self-market
creators. Self-markets had fewer observers and less trading volume than external markets and more often ended at an
intermediate price.
Research ethics.All data are publicly visible on the platform and were collected through its documented public
interface within its rate limits. Users appear under pseudonyms; we analyze aggregates only, report no usernames,
and paraphrase rather than quote individual questions. The study involved no interaction with users. Because many
questions concern health, relationships, and habits, the released data replace user identifiers with keyed hashes and
contain no question or comment text; they include the market identifiers needed to rebuild the data from the platform.
3.3 Reconstructing prices and executions
The platform records orders, not trades. An order’s record states the probability immediately before and after the order’s
own execution against the market maker, and its fills list what it bought or sold, when, and at what cost. A limit order
may be filled long after it was placed, in several pieces, or partly filled and then cancelled; when it is filled later, the
price change belongs to the incoming order that filled it. We therefore build two separate series. The price path is
the sequence of all orders, including cancelled and unfilled ones, in the order they were placed. Executions are the
fills, each at its own time, so that a cancelled order keeps what it had bought before cancellation and a resting order’s
purchase is dated when it was filled.
Two internal checks support this reconstruction (Appendix Table 10). The final price of the reconstructed path equals
the probability the platform reports for the market in 99.4% of sample markets, against 91.9% when only filled,
never-cancelled orders are used, and the probability before an order equals the probability after the preceding order
in 97.2% of consecutive pairs, against 85.9%. The distinction matters for participation as well as prices: 17% of all
purchase executions came from orders that were later cancelled, and 37,578 purchase orders received a fill more than a
minute after they were placed.
Two research assistants then checked the reconstruction externally. On 40 randomly drawn sample markets, the question
text, the resolution, and the number of traders shown on the live platform matched our data in all 40 markets; the last
probability on each market’s price chart was within 0.5 points of the reconstructed final price; and whether the creator
had traded matched in all 34 markets where the page showed it. Working only from the released de-identified data and
with their own code, the assistants also recomputed 23 reported quantities, including the main regression coefficients
and the purchase-level estimates. They reproduced every one to within 0.02%; one standard error differed by 1.7%
because it was computed under another small-sample convention. Synthetic checks of partial fills, late fills, cancelled
5

orders, and the estimators, together with checks of the processed data against the timing rules below, are released with
the code.
3.4 Measures
The analyses rest on four kinds of measures: forecasts and their accuracy, the activity of the person and of observers,
the roles of buyers, and the content of questions and comments.
Outcomes and forecasts.The outcome Y equals 1 if the market resolved YES and 0 if it resolved NO. Trading in a
market ends at the earlier of its scheduled close and its resolution, which we call its close. The main forecast is the final
price p, the market probability after the last order before the close. Because the final price can follow news about the
outcome, and because a market’s life depends on when it resolved, we also measure prices at fixed points, or landmarks:
at the opening; 1 hour, 6 hours, 1 day, 3 days, and 7 days after creation, for markets still open at that time; and 7 days
and 1 day before the close, for markets that had opened by then. The price at a landmark is the probability after the last
order at or before it. Three summaries of the price over the market’s life complete the set: the price at its midpoint, the
time-weighted average price, and the price after the third observer purchase.
Calibration and accuracy.For each market, the calibration gap is Y−p . Its mean is the difference between how often
markets resolve YES and how often their prices say they will. A negative mean gap means that prices overstated YES,
and we then call the prices optimistic. Because a mean gap can hide offsetting errors, we also report the Brier score, the
mean squared difference between Y and p [45]; log loss; the intercept and slope of a logistic recalibration of Y on the
log-odds of p; and the Murphy decomposition of the Brier score into reliability (miscalibration), resolution (how well
prices separate YES from NO outcomes), and uncertainty (the base rate) [46].
Price changes and creator activity.Each order’s own price change, ∆p, is attributed to the party that placed it: the
creator, a human observer, or an automated observer, meaning an order placed through the platform’s programming
interface. Multiplying ∆p by +1 for markets that resolved YES and by −1 for markets that resolved NO measures
movement toward the outcome; summed over a market’s orders, it equals the reduction in the market’s absolute error
from the opening to the final price. Summing ∆p without the sign of the outcome measures movement toward YES. A
creator is coded as never trading in a market when none of their orders placed up to the order that set the final price was
executed, and as silent when they also posted no comment by that time. Both codes therefore use only activity that
observers could see when the final price was set. The creator’s position is the number of YES shares minus NO shares
they held at that time. For each self-market, the creator’s earlier record is the share of their earlier forward-looking
self-markets, resolved before the focal market opened, that resolved YES, together with the number of such markets;
because YES can name an unwanted outcome, we call this share the prior YES rate rather than a success rate. The
record is visible to anyone who opens the creator’s profile.
Buyers and purchases.Buyer roles are assigned at the time of each purchase and are mutually exclusive, in the
following order. The creator is the market’s creator. An encourager had posted a comment in the market, before placing
the purchase order, that wished the creator well (for example “good luck”, “you got this”, “rooting for you”, or similar
emoji); congratulations, which can respond to a known outcome, are not counted. A prior interactor had traded or
commented in another sampled market of the same creator before the focal market opened. Because only sampled
markets are observed, prior interaction measures observed contact on the platform, not friendship. All remaining
observers are strangers. Two further indicators describe observers: experienced observers had traded in 50 or more
sampled markets before the focal market opened, and automated purchases were placed through the programming
interface. For each purchase we record whether the purchased side won, and its payoff per share if held to resolution (1
if the purchased side won, 0 otherwise) minus the price paid per share. The payoff accounts for the price paid. Both
measures describe purchases rather than beliefs, since a purchase also reflects timing, strategy, and the buyer’s other
positions.
Question content.Two keyword rules code self-market questions. The first flags questions whose YES answer is a
lapse or an outcome the creator would not want, such as relapsing, breaking a streak, missing a deadline, falling ill, or
losing money. It excludes negations, cessation goals (“Will I quit vaping?”), mixed outcomes (“promote or demote”),
tests that come back negative, and questions about the creator’s beliefs. The second separates behaviors the creator
performs (effort goals such as exercising, writing, or finishing a task, and restraint goals such as quitting a habit) from
outcomes that others or chance help decide (admissions, job offers, test scores, illness, winning). Both rules were
refined by reading every flagged question and keyword-in-context listings of unflagged ones, fixed before validation,
and released (Appendix B).
Validation of the coding.Two research assistants labelled a stratified sample of 726 questions and 400 comments
independently, without seeing market outcomes or the rules’ labels (Appendix Table 12). Agreement, measured by
Cohen’s κ [47], was high on whether a question concerns the creator ( κ= 0.98 ), whether it concerns the future
6

(κ= 0.93 ), and whether the creator would want a YES (κ= 0.91 ), and on whether a comment encourages (κ= 0.95 )
or congratulates the creator ( κ= 0.95 ). The market classification held up: the coders labelled 98.5% to 99.5% of
200 random self-markets as forward-looking questions about the creator and 98.0% to 99.0% of 100 random external
markets as not about the creator, whereas only 18% to 20% of the first-person questions set aside were forward-looking.
The unwanted-outcome rule is precise but incomplete. Between 86% and 90% of the questions it flags were coded
unwanted, and it flags an estimated 47% of the questions both coders labelled unwanted (95% CI 35% to 66%). The
encouragement rule is likewise precise (85% to 89%) and incomplete (recall 43% to 45%). Only 0.8% of the comments
it flags showed knowledge of the outcome, against 62% of those flagged as congratulating, which supports keeping
congratulations out of the measure of encouragement. Goal type is the weakest measure: the coders agreed on how
much an outcome depends on the creator for only 65% of questions ( κ= 0.49 ). The analyses that use the keyword
rules are therefore exploratory.
3.5 Analysis
Market-level comparisons.Mean gaps and their differences are estimated by least squares with standard errors
clustered by creator, because markets from the same creator share a person, a resolution style, and often a set of traders.
Each market receives equal weight; a cap of five markets per creator and equal weights per creator serve as robustness
checks. The main comparison regresses the gap at the final price on a self-market indicator, with external markets
by other creators as the benchmark. It then adds controls for the log number of observers, log purchase volume, log
scheduled horizon, and creation-year fixed effects, and finally fixed effects for ten equal-width price bins (0–10%,
10–20%, . . . , 90–100%), which compare self- and external markets at the same price level. The controls describe the
markets themselves, so the adjusted comparison is descriptive: it compares self- and external markets of similar size,
horizon, timing, and price. A second set of specifications uses the same creators’ external markets as the benchmark,
with and without creator fixed effects. At each landmark we repeat the same-price comparison among the markets open
at that time.
Price changes and purchases.Movement toward the outcome and toward YES is averaged over markets for each party.
Purchase-level comparisons regress the indicator that the purchased side won on the role indicators, with strangers as
the reference group and market fixed effects, so that each buyer is compared with strangers buying in the same market.
Purchases are weighted by mana within each market, and each market receives equal total weight. The fixed effects
are absorbed by subtracting weighted market means, which reproduces the estimates of a model with explicit market
indicators; because markets are nested within creator clusters, the small-sample correction of the standard errors counts
only the remaining regressors. Variants use market-by-day fixed effects, which compare purchases made on the same
day of the same market; purchases made more than a day before the close; each buyer’s first purchase in a market;
equal weight per purchase; and the payoff per share as the outcome. Differences between self- and external markets
are estimated jointly in a pooled model with interactions. Standard errors are clustered two ways, by creator and by
buyer [48], because buyers trade across many creators’ markets. A within-trader comparison, which compares the same
observers’ purchases in the two kinds of market at the same price paid, serves as a robustness check.
Held-out evaluation.To ask whether the bias can be corrected, we fit logistic recalibrations of the final price on
markets created and resolved before 1 January 2025 and evaluate them on markets created afterwards, and separately in
five folds that never share a creator between fitting and evaluation. Paired differences in Brier scores against the raw
price come with intervals from a creator-cluster bootstrap.
Inference.The analyses were not preregistered. RQ1 and RQ2 are primary and RQ3 is secondary; the seven RQ4 tests
are exploratory and are reported with p-values adjusted by Holm’s method [49]. A difference that is not significant is
reported with its confidence interval and is not taken as evidence of equivalence.
4 Results
4.1 Prices overstate the futures people pose for themselves (RQ1)
Self-markets resolved YES in 45.0% of cases, while their final prices averaged 49.4%. The mean calibration gap is
therefore−4.4 percentage points (pp; SE 0.5). External markets made by other creators are close to calibrated, with a
gap of −0.9 pp (SE 0.3), so the difference between the two is −3.5 pp (SE 0.6, p < .001). Figure 1A shows where the
difference arises. Across the middle of the price range the self-market curve runs below the diagonal: according to
the logistic recalibration, a self-market priced at one half resolved YES 39% of the time, against 47% for an external
market by another creator. Near zero and one, both kinds of market are close to calibrated. Among markets whose final
price lay between 20% and 80%, the gap is −9.4 pp for self-markets (SE 1.0) and −1.2 pp for external markets by other
creators (SE 1.6); Appendix Table 13 reports the gaps for other forecasts and price ranges.
7

0.0 0.2 0.4 0.6 0.8 1.0
Final market price (probability of YES)
0.0
0.2
0.4
0.6
0.8
1.0Share resolved YES
below the diagonal:
price overstated YES
A. Calibration
External, other creators
External, same creators
Own future (self-markets)
Open 1 h 6 h 1 d 3 d 7 d 7 d 1 d Final
−10
−5
0
5
Self minus external, same price level (pp)
after creation before close
B. Gap difference over the market's life
All markets open at the time
Markets in which the person never traded
Figure 1: Calibration of self-markets and external markets. Panel A plots the share of markets that resolved YES
against the final price, in ten equal-width price bins, with 95% confidence intervals clustered by creator; points below
the dashed diagonal mean that prices overstated YES. Panel B plots, at landmarks in the markets’ lives, the difference
between self-markets and external markets by other creators in the share resolving YES minus the price, at the same
price level (fixed effects for ten price bins), with 95% confidence intervals. Filled markers use all markets open at the
time; hollow markers keep markets in which the person never traded before the final price.
Table 2: Self-markets versus external markets: regressions of the calibration gap at the final price (percentage points).
(1) (2) (3) (4) (5)
Self-market−3.5−2.5−2.2−2.1−1.9
(0.6) (0.6) (0.5) (0.6) (0.7)
Comparison: external markets by other other other same same
creators creators creators creators creators
Observers, volume, horizon (logs); year FE Yes Yes Yes Yes
Price-bin FE Yes Yes Yes
Creator FE Yes
Markets 12,422 12,422 12,422 10,636 9,956
Creators 4,284 4,284 4,284 1,660 1,222
Note: Dependent variable is Y−p at the final price. Least squares with standard errors clustered by creator in parentheses.
Columns (1)–(3) compare self-markets with external markets by creators who never opened a self-market; columns (4)
and (5) compare them with external markets by the same creators, column (5) within creator (creators who made both
kinds of market). The controls adjust the comparison descriptively (Section 3.5).
Differences in the size, horizon, and timing of markets explain only part of the gap. Table 2 regresses the gap on
a self-market indicator. Adding the number of observers, purchase volume, horizon, and creation-year fixed effects
reduces the difference from −3.5 pp to −2.5 pp, and adding price-bin fixed effects, which compare self- and external
markets at the same price level, leaves −2.2 pp (SE 0.5, p < .001). The gap is also not a matter of who makes the
markets. External markets made by the people who also make self-markets behave like those of other creators, with
a gap of −1.3 pp (SE 0.3). Against these markets the self-market difference is −2.1 pp with controls and price-bin
fixed effects (SE 0.6, p < .001), and −1.9 pp within creator (SE 0.7, p=.006 ), estimated from 5,470 self-markets by
creators who made both kinds of market. The same people’s markets were priced more optimistically when the question
was about themselves than when it was about the world.
The mean gap captures only one part of accuracy, and Table 3 reports the others. Self-markets’ final prices had a Brier
score of 0.105, against 0.049 for external markets by other creators, and their calibration intercept was more negative
(−0.38, SE 0.04, against −0.14, SE 0.05). The Murphy decomposition attributes most of the difference in Brier scores
8

Table 3: Accuracy and calibration of final prices.
External markets
Self-markets Other creators Same creators
Brier score 0.105 (0.005) 0.049 (0.003) 0.051 (0.002)
Log lossa 0.326 (0.015) 0.169 (0.009) 0.176 (0.007)
Calibration interceptb −0.38 (0.04)−0.14 (0.05)−0.18 (0.05)
Calibration slopec 1.20 (0.04) 1.32 (0.05) 1.35 (0.05)
Implied YES rate at a price of 50% 39% 47% 46%
Reliability (miscalibration)d 0.004 0.001 0.001
Resolution (discrimination)d 0.146 0.195 0.190
Uncertainty (base rate)d 0.247 0.243 0.240
Note: Lower Brier score and log loss are better. Standard errors clustered by creator in parentheses. aPrices clipped
to [0.01, 0.99]. bIntercept of a logistic model of Y with the log-odds of the price as an offset; negative values mean
that prices overstated YES on average. cCoefficient on the log-odds of the price; values above 1 mean that outcomes
were more extreme than prices. dMurphy decomposition over ten equal-width price bins: Brier score ≈ reliability −
resolution+uncertainty.
to resolution rather than reliability. Self-market prices separated the markets that resolved YES from those that resolved
NO less well (resolution 0.146 against 0.195), while their miscalibration, though larger, was small in absolute terms
(reliability 0.004 against 0.001). Self-market prices were thus both less informative and biased toward YES, and the
bias is the systematic part of a larger shortfall in information.
The answer to RQ1 is yes. At their final prices, markets about a person’s own future overstated how often the named
outcome occurred, by about 4.4 pp on average and by about 9.4 pp when the outcome was uncertain, whereas markets
about external events were close to calibrated.
4.2 The overstatement arises with trading (RQ2)
The final price is the last of many forecasts, and it can follow news about the outcome. Figure 1B and Appendix
Table 14 therefore compare self- and external markets at the same price level at each landmark. At the opening, almost
all markets of both kinds stood at the default 50% (95% of self-markets and 90% of external markets), and self-markets
were, if anything, underpriced: at the same opening price they resolved YES 3.0 pp more often than external markets
(SE 1.3). Trading reversed this. One hour after creation the difference was −1.1 pp (SE 1.1), one day after creation
−2.4 pp (SE 1.0, p=.021 ), and seven days after creation −2.9 pp (SE 1.1, p=.008 ). It was largest in the final stretch:
−5.3 pp a week before close (SE 0.9) and −4.6 pp a day before close (SE 0.8). A self-market priced at one half a week
before close resolved YES 39% of the time, against 48% for an external market at the same price.
The person’s own trades are not needed for this pattern. In markets in which the person never traded before the final
price, self-markets were priced like external markets at the opening (difference −1.2 pp, SE 1.8). The overstatement
appeared within an hour (−3.9 pp, SE 1.7), reached−5.5 pp after a day (SE 1.7), and stood at−7.6 pp a week before
close (SE 1.5). At the final price these markets were 5.7 pp more optimistic than external markets in which the creator
never traded (SE 1.0, p < .001), a larger difference than for self-markets as a whole. Prices set by observers alone
overstated the person’s future from the first hours of trading.
The price changes in those first hours show how the overstatement arose. Table 4 attributes each price change to the
party whose order made it. In the first day after creation, human observers moved external-market prices 4.5 pp toward
NO on average, from the default 50% toward the lower rate at which such questions resolve YES. In self-markets that
did not name an unwanted outcome, they moved prices only 0.8 pp toward NO (SE 0.5), although these markets also
resolved YES less than half the time (44%). Observers’ first-day movement toward YES was thus 3.6 pp larger in these
self-markets than in external markets (SE 0.6, p < .001), and 3.0 pp larger when the eventual outcome and the creation
year are held fixed (SE 0.6). The contrast is sharpest where the person never traded. There, observers moved these
self-markets 0.7 pp toward YES (SE 0.5), while they moved external markets with a similar YES rate (38% and 37%)
4.3 pp toward NO, a difference of+5.0 pp (SE 0.9,p < .001).
Observers did move one kind of self-market toward its base rate. In markets naming an unwanted outcome, they sold
prices down by 6.4 pp in the first day (SE 2.1). Observers thus sold external events down toward their base rate, and
sold down the misfortunes people named, but not the goals people set. Where the person did trade, the person’s own
first-day orders also moved prices toward YES (by 2.9 pp, against 1.0 pp for the creators of external markets), and on
balance these orders moved prices toward the eventual outcome (by 2.2 pp).
9

0.0 2.5 5.0 7.5 10.0 12.5
Price movement toward the outcome (pp per market)
Automated traders
Human observers
The person (market creator)
1.0
2.2
9.6
4.6
0.0
-0.3
A. First day after creation
0 10 20 30 40
Price movement toward the outcome (pp per market)
3.5
10.6
34.0
18.7
-0.1
-1.5
B. Whole market, up to close
External markets, other creators Self-markets
Figure 2: Whose orders moved prices toward the eventual outcome? Each order’s own price change, signed so that
positive values move the price toward the outcome, summed by the party that placed the order and averaged over
markets, with 95% confidence intervals clustered by creator. Panel A covers the first day after creation (markets open
for at least a day); panel B covers the whole market up to close. External markets are those by other creators.
The answer to RQ2 is that the overstatement was not inherited from the opening price. It arose with trading within the
first day, it arose without the person’s trades, and it was largest in the week before close.
4.3 The person supplies much of the correction (RQ3)
If observers did not correct the overstatement early, the question is who did. Over a market’s whole life, trading moved
prices toward the outcome in both kinds of market, but less in self-markets: by 27.8 pp on average, against 37.3 pp in
external markets by other creators (Figure 2B, Table 4). The sources of that movement differed. Human observers’
orders moved self-market prices 18.7 pp toward the outcome, against 34.0 pp in external markets, and in the first day
they moved self-market prices toward the outcome about half as far (4.6 against 9.6 pp). The person’s own orders
moved self-market prices 10.6 pp toward the outcome, against 3.5 pp for the creators of external markets. The person
thus supplied 38% of the movement toward the outcome in self-markets, against 9% in external markets, and 47% of
the person’s contribution came in the final day before close. Automated observers moved self-market prices slightly
away from the outcome (−1.5 pp, SE 0.2).
Purchases tell the same story. Table 5 compares, within each market, how often each group’s purchases landed on the
side that won, relative to strangers buying in the same market. In self-markets, the person’s purchases landed on the
winning side 4.0 pp more often than strangers’ (SE 1.2, p=.001 ). In external markets, creators did no better than
strangers (−0.9 pp, SE 1.0), and the difference between the two is +4.8 pp (SE 1.6, p=.003 ). The advantage holds
when purchases are compared within the same day of the same market (+4.5 pp, SE 1.7), but it is concentrated late: for
purchases made more than a day before close it is +1.6 pp (SE 1.4), and it disappears once the price paid is taken into
account (payoff per share −0.7 pp, SE 1.7). The person bought the side that won more often, mostly near the end and at
prices that already reflected much of what they knew. Creators placed 62% of their purchase volume in self-markets in
the final day before close, much as creators of external markets did (61%), but only in self-markets did these purchases
land on the winning side more often than strangers’.
The person’s advantage can come from knowing their own progress, from controlling the behavior, or from resolving
the market. Whatever its source, the decisive information lay with the person and reached the price late. The person’s
position at the final price, which other traders can see, added little to the price in predicting the outcome (logistic
coefficient for a YES position 0.18, SE 0.11,p=.088).
4.4 Desirability, prior interaction, and visible cues (RQ4, exploratory)
The results so far show where the overstatement arises and who corrects it. RQ4 asks whether it follows the markers
that the two accounts emphasize, beginning with desirability. The motivated account predicts that the bias follows what
10

Table 4: Whose orders moved prices toward the outcome? Price changes per market, in percentage points.
External markets
Self-markets Other creators Same creators
Total movement from opening to final price+27.8 (0.9)+37.3 (0.9)+37.7 (0.4)
by the creator’s orders+10.6 (0.9)+3.5 (0.5)+5.1 (0.5)
by human observers’ orders+18.7 (0.8)+34.0 (0.8)+33.5 (0.6)
by automated orders−1.5 (0.2)−0.1 (0.3)−0.9 (0.3)
not attributed to an order−0.1 (0.0)−0.1 (0.0)+0.0 (0.0)
Creator, more than a day before close+5.6 (0.5)+1.7 (0.3)+2.8 (0.4)
Creator, final day before close+5.0 (0.7)+1.8 (0.3)+2.3 (0.2)
Observers, more than a day before close+12.9 (0.7)+23.0 (0.8)+23.6 (0.6)
Observers, final day before close+5.9 (0.3)+11.0 (0.6)+9.9 (0.4)
First day after creation (markets open for at least a day)
Creator, toward the outcome+2.2 (0.4)+1.0 (0.2)+1.3 (0.2)
Human observers, toward the outcome+4.6 (0.4)+9.6 (0.4)+9.8 (0.4)
Automated, toward the outcome−0.3 (0.1)+0.0 (0.1)+0.1 (0.1)
Creator, toward YES+2.9 (0.4)+1.0 (0.3)+0.5 (0.3)
Human observers, toward YES−1.1 (0.4)−4.5 (0.5)−4.6 (0.4)
Automated, toward YES+0.9 (0.1)−0.4 (0.1)−0.1 (0.1)
Note: Each order’s own price change, ∆p, is multiplied by +1 if the market resolved YES and −1 if it resolved NO and
summed by the group that placed the order; summed over all orders, this equals the reduction in the market’s absolute error
from the opening to the final price. “Toward YES” rows sum ∆p without the sign of the outcome. Means over markets,
with standard errors clustered by creator in parentheses.
Table 5: Purchases on the side that won, relative to strangers buying in the same market (percentage points).
Self-markets External markets Difference
The creator+4.0 (1.2)−0.9 (1.0)+4.8 (1.6)
Observers with a prior interaction+0.4 (0.8)−1.2 (0.8)+1.6 (1.1)
Observers who had encouraged+0.7 (4.2)+6.0 (5.9)−5.2 (7.4)
Experienced observers+0.2 (0.8)+1.9 (0.7)−1.7 (0.9)
Automated purchases−17.5 (2.1)−16.7 (1.4)−0.8 (2.5)
Purchases 188,201 707,742
Markets 6,150 10,758
Markets with creator and stranger purchases 3,499 6,297
The creator under alternative specifications
Market-by-day fixed effects+4.5 (1.7)+0.1 (1.4)+4.4 (2.2)
Purchases more than a day before close+1.6 (1.4)−3.0 (1.1)
Each buyer’s first purchase in the market+3.1 (1.8)−4.3 (1.4)
Equal weight per purchase+9.6 (2.5)−5.2 (2.1)
Payoff minus price paid, market-by-day fixed effects−0.7 (1.7)+0.8 (1.3)
Note: Weighted least squares of an indicator that the purchased side won on buyer-role indicators with market fixed
effects, estimated by the weighted within transformation. Roles are mutually exclusive in the order creator, encourager
(had posted an encouraging comment in the market before placing the purchase order), prior interactor (had traded or
commented in another sampled market of the creator before the market opened); strangers are the reference. Indicators
for experienced observers (50 or more earlier sampled markets) and automated purchases enter alongside. Purchases are
weighted by mana within each market and each market receives equal total weight, except where noted. The difference is
the self-market interaction in a pooled model. Standard errors two-way clustered by creator and buyer in parentheses. The
last row uses the hold-to-resolution payoff per share minus the price paid.
the person wants. Table 6 splits self-markets by the named outcome. By the keyword rule, markets naming an outcome
the person would want, or a neutral one, had a gap of −4.6 pp (SE 0.5). The 294 markets naming an unwanted outcome,
such as relapsing, breaking a streak, or falling ill, had a gap of −0.5 pp (SE 1.5; 95% CI −3.4 to +2.4); at the same
price, they were 3.7 pp less optimistic than other self-markets (SE 1.6,p=.021, Holm-adjustedp=.149).
The coders’ labels confirm that markets naming unwanted outcomes were not overpriced, and they leave open whether
such markets were underpriced. The 251 flagged markets that both coders confirmed as naming an unwanted outcome
had a gap of −1.9 pp (SE 1.6). Because the rule misses about half of unwanted questions, we also weighted the coded
11

Table 6: Self-markets by named outcome, goal type, and the creator’s earlier record (exploratory).
Markets Resolved YES Mean final price Gap (pp)
Named outcome wanted or neutral 5,856 45.9% 50.5%−4.6 (0.5)
Named outcome unwanted (lapse, illness, loss) 294 27.2% 27.7%−0.5 (1.5)
Effort goal (exercise, write, finish) 2,236 46.2% 52.5%−6.3 (1.0)
Restraint goal (quit, stay off) 71 52.1% 55.0%−2.9 (3.9)
Outcome others or chance help decide 1,345 42.5% 45.8%−3.3 (0.9)
Unclassified 2,498 45.1% 48.5%−3.4 (0.6)
Prior YES rate, lowest third (28%) 928 37.6% 41.5%−3.9 (1.1)
Prior YES rate, middle third (50%) 927 41.6% 48.5%−6.9 (1.4)
Prior YES rate, highest third (75%) 928 50.1% 54.4%−4.3 (1.3)
Note: Gap is the share resolved YES minus the mean final price, with creator-clustered standard errors in parentheses.
Named-outcome and goal codes come from released keyword rules applied to the question text. The last panel uses
self-markets whose creator had at least three earlier forward-looking self-markets resolved before the market opened; the
prior YES rate is the share of those that resolved YES (in parentheses, the mean within the third).
sample to the population of self-markets. These estimates rest mostly on the random draw of 200 self-markets, whose
own gap was −2.9 pp, against −4.4 pp for all self-markets. Markets the coders agreed named a wanted outcome had
a gap of −2.5 pp (SE 2.8), neutral or unclear ones −5.6 pp (SE 4.1), and unwanted ones +4.2 pp (95% CI −2.3 to
+10.8). At the same price, unwanted outcomes were 7.8 pp less optimistic than wanted ones (SE 4.9, p=.111 ). A
crowd siding with the person would produce this positive gap, but the estimate rests largely on 9 unwanted questions
that the rule missed in the random sample, each standing for many markets. These markets opened near 50% although
such outcomes occurred 27% of the time, and trading moved them down quickly, to 35% after a day. In these markets,
siding with the person and applying the base rate both push prices down, so the two accounts make the same prediction.
Prior interaction did not distinguish observers. Observers who had interacted with the person on the platform before the
market opened picked the winning side as often as strangers (+0.4 pp, SE 0.8; 95% CI −1.2 to +2.0). Encouragement
before a purchase was rare once comments made after the purchase were excluded (1,276 purchases in the 241 markets
that also had strangers’ purchases), and its estimate is too imprecise to interpret (+0.7 pp, SE 4.2). Most YES purchases
in self-markets came from strangers (67% of observers’ YES purchases). Experience on the platform helped with
external markets (+1.9 pp, SE 0.7) but not with self-markets (+0.2 pp, SE 0.8).
The cues that anyone can see added little to the price. Prices followed a person’s earlier record: self-markets by people
in the lowest third of prior YES rates traded at 41% on average, against 54% for people in the highest third. Conditional
on the price, however, the record added no detectable predictive value. In 2,783 self-markets by 286 creators with at
least three earlier resolved self-markets, the coefficient on the prior YES rate in a logistic model with the log-odds
of the price is −0.60 (SE 0.39, p=.118 , Holm-adjusted p=.592 ). Adding the record changed out-of-sample Brier
scores by +0.0001 in creator-disjoint folds (95% CI −0.0007 to +0.0008) and by +0.0007 when fitted on earlier and
evaluated on later markets (−0.0012 to +0.0025). Silence was priced in the same way. Silent self-markets, in which the
person neither traded nor commented before the final price, had a larger raw gap (−7.4 pp against −3.6 pp), but with
price-bin fixed effects silence added−1.0 pp (SE 1.2).
The person’s history on the platform and the type of goal complete the picture. The gap did not shrink with a person’s
history, and if anything it was larger for people with long histories: among intermediate-priced self-markets it was
−6.6 pp for people with no earlier resolved self-market and −13.7 pp for people with thirty or more (log number of
earlier self-markets, −0.5 pp, SE 0.3). Because later markets attract different observers and different goals, this pattern
describes heterogeneity across histories rather than a failure of the same observers to learn. Effort goals showed the
largest gap, −6.3 pp (SE 1.0), against −3.3 pp (SE 0.9) for outcomes that others or chance help decide; with price-bin
fixed effects, the difference between behavior goals and outcomes is −2.4 pp (SE 1.2, p=.054 , Holm-adjusted
p=.325).
In sum, the exploratory tests found no overpricing in markets naming outcomes the person would not want, and no sign
that prior interaction or visible cues account for the bias.
4.5 How much can a correction help?
Because the bias is systematic, a correction learned from past markets could in principle remove it. Table 7 reports
held-out Brier scores. Fitted on markets created and resolved before 2025 and evaluated on later ones, a recalibration
that treats self-markets separately lowered the self-market Brier score by 1.5% (change −0.0021, 95% CI −0.0058 to
12

Table 7: Held-out Brier scores of market prices and simple corrections.
Self-markets External markets, other creators
Forecast Brier Change [95% CI] Brier Change [95% CI]
Chronological split, final price
Market price 0.141 0.062
Base rate by market type 0.249 0.1079 [0.0906, 0.1259] 0.246 0.1839 [0.1720, 0.1956]
Pooled recalibration 0.139−0.0015 [−0.0041, 0.0012] 0.062−0.0002 [−0.0019, 0.0016]
Self-aware recalibration 0.139−0.0021 [−0.0058, 0.0022] 0.061−0.0009 [−0.0020, 0.0001]
Self-aware with market features 0.139−0.0016 [−0.0058, 0.0032] 0.061−0.0006 [−0.0019, 0.0006]
Chronological split, price one day after creation
Market price 0.230 0.183
Base rate by market type 0.248 0.0181 [0.0061, 0.0310] 0.243 0.0603 [0.0490, 0.0709]
Pooled recalibration 0.224−0.0057 [−0.0114,−0.0008] 0.184 0.0012 [−0.0027, 0.0051]
Self-aware recalibration 0.224−0.0056 [−0.0122, 0.0008] 0.183−0.0000 [−0.0032, 0.0029]
Self-aware with market features 0.226−0.0041 [−0.0117, 0.0030] 0.183 0.0003 [−0.0028, 0.0034]
Creator-disjoint folds, final price
Market price 0.105 0.049
Base rate by market type 0.248 0.1426 0.244 0.1950
Pooled recalibration 0.102−0.0030 0.048−0.0004
Self-aware recalibration 0.102−0.0037 0.048−0.0008
Self-aware with market features 0.102−0.0035 0.048−0.0009
Note: Chronological split: corrections are fitted on markets created and resolved before 1 January 2025 (11,435 markets) and
evaluated on markets created afterwards (1,297 self-markets and 1,315 external markets by other creators). Creator-disjoint
folds: five folds in which no creator appears in both training and evaluation; changes are pooled over folds. Recalibration
models are logistic regressions on the log-odds of the price; the self-aware model lets the intercept and slope differ for
self-markets; the feature model adds, for self-markets, whether the creator had traded and the log number of observers, both
measured as of the forecast (by the final price, or within the first day). Changes are relative to the market price; negative
changes are improvements. Intervals from a creator-cluster bootstrap of the paired score difference.
0.0022); in creator-disjoint folds it lowered it by 3.5%. Applied to prices one day after creation, a pooled recalibration
lowered the Brier score by 2.5% (95% CI for the change −0.0114 to −0.0008). The gains are small, and for final
prices the chronological test cannot distinguish them from zero. The decomposition above explains why: most of what
self-market prices lack is the ability to tell successes from failures, which no transformation of the price can add.
4.6 Robustness
Table 8 repeats the final-price comparison under 25 variations of the forecast, the sample, the benchmark, and the
adjustment. The self-market difference ranges from −5.7 to −2.2 pp and is significant at the 5% level in all of them
(largest p-value: p=.033 ). The forecast can be the price one day after creation or one day before close, the price at
mid-life, the time-weighted average price, or the price after the third observer purchase. The sample can be restricted to
markets whose final trade came within a day of close, to markets with at least seven or fifteen observers, to markets in
which the creator never traded, or to either half of the sample period; it can exclude the ten most active self-market
creators, markets in which a fifth or more of observer purchases were automated, same-day and same-week questions,
and questions about the market itself or about chance devices such as coins and dice. Each creator can be limited to five
markets of each kind or given equal weight. External questions that mention a user handle or a third-person pronoun
can be dropped, and self-markets can be defined by the broad first-person rule. The benchmark can be the same creators’
external markets or all external markets, and the adjustment can use twenty price bins or reweight external markets to
resemble self-markets in size, horizon, year, opening, and price.
Two further checks address the selection of markets and of traders. Markets without a YES or NO resolution were
about as common among self-markets as among external markets (92% and 91% resolved YES or NO; Appendix
Table 11), and counting them with a gap of zero leaves the self-market gap at −4.1 pp and the external gap at −0.9
pp. A within-trader comparison does not detect a difference in the purchases of the same observers: among the 8,611
observers who bought in both kinds of market, YES purchases in self-markets returned −0.3 pp per share relative to the
same trader’s YES purchases in external markets at the same price paid (SE 1.8), and NO purchases +0.8 pp (SE 1.8).
13

Table 8: Robustness of the self-market difference in calibration gaps (percentage points).
Variation DifferenceNselfNtotal
Forecast Baseline: final price, no controls−3.5 (0.6) 6,150 12,422
Price at mid-life−4.8 (0.9) 6,150 12,422
Time-weighted average price−4.5 (0.8) 6,150 12,422
Price after third observer purchase−2.2 (1.0) 5,757 11,702
Price one day after creation−3.7 (1.0) 5,383 10,820
Price one day before close−4.8 (0.8) 5,383 10,820
Sample Final trade within a day of close−2.8 (0.6) 4,308 8,850
At least 7 observers−3.2 (0.5) 4,024 8,622
At least 15 observers−2.3 (0.7) 1,673 4,228
At most 5 markets per creator and type−4.4 (0.7) 3,480 7,838
Equal weight per creator within type−2.9 (0.8) 6,150 12,422
Without the 10 most active self-market creators−3.4 (0.6) 5,081 11,353
Automated purchases under 20%−2.8 (0.7) 3,429 7,236
Creator never traded−5.7 (1.0) 2,466 5,004
Excluding same-day and same-week questions−3.5 (0.5) 5,337 11,457
Excluding self-referential and chance questions−3.6 (0.6) 5,982 12,254
External questions without person mentions−3.7 (0.6) 6,150 12,196
Created 2021–2023−3.1 (0.8) 3,603 7,281
Created 2024–2026−4.2 (0.9) 2,547 5,141
Broad self-market definition (all first-person leads)−3.5 (0.6) 6,270 12,542
Benchmark Benchmark: same creators’ external markets−3.1 (0.6) 6,150 10,636
Benchmark: all external markets−3.4 (0.6) 6,150 16,908
Adjustment Controls and 10 price-bin effects−2.2 (0.5) 6,150 12,422
Controls and 20 price-bin effects−2.2 (0.5) 6,150 12,422
Reweighted external markets (propensity, trimmed)−3.5 (0.9) 6,150 12,421
Note: Coefficient on a self-market indicator in a regression of Y−p (without controls unless stated); standard errors
clustered by creator in parentheses. Unless stated otherwise, p is the final price and the benchmark is external markets
by other creators. The reweighting row weights external markets by the odds of a propensity score built from observers,
volume, horizon, year, default opening, and price bin, after trimming scores outside [0.05, 0.95].
5 Discussion
5.1 Theoretical implications
Lab studies of self- and social prediction cast observers as the corrective to optimistic self-prediction: free of the actor’s
plans and hopes, they consult base rates and past behavior [3, 6, 7]. In the markets studied here, observers aggregated
through a market and paid for accuracy did not play that role. They brought an outside view to external events, selling
prices down toward the rate at which such events occur, but not to the goals people set for themselves, and markets
about people ended up overstating those goals. The observer advantage evidently depends on conditions that online
crowds forecasting a specific person do not meet. Lab observers share a task with the actor, see the actor’s history, and
judge one person at a time. Observers on a platform see a question, a price, perhaps the person’s own trades, and at
most a profile. With a plan in view and little else about the person at hand, they are in the position that makes actors
optimistic in the lab, and their prices look like the actor’s forecast: the outcome the person aims for is treated as more
likely than it is.
Why observers price people this way is the question our data cannot settle. Two accounts fit parts of the evidence. On a
motivated account, observers share the person’s hopes; consistent with it, the bias was absent from markets naming
outcomes the person would not want, in the first day observers held up the prices of people’s goals while selling down
the prices of the misfortunes they named, and by the coders’ labels unwanted outcomes were, if anything, underpriced.
On an informational account, observers read a stated goal as evidence of what will happen and have nothing better to
go on; consistent with it, the unwanted outcomes the rule flags and the coders confirmed were not underpriced, prior
interactors traded like strangers, and prices moved toward the truth when the person, who holds the decisive information,
traded. Both accounts agree that observers lacked, or did not use, a reference class for the person. Separating them
requires holding information fixed while varying the observer’s stake in the person, the kind of experiment described in
Section 5.3.
14

The findings also qualify the aggregation argument for prediction markets. Markets correct individual errors when
informed traders oppose them [8, 27, 28]. In self-markets the best-informed trader is a single person who may not trade,
and who learns most about the outcome near the end. Most observer purchases came from strangers, and in a market’s
first day observers’ trades moved self-market prices only about half as far toward the outcome as external-market
prices, so the correction arrived late and incompletely. This matches the field evidence that price distortions on the
same platform persist when few traders are present [10], and it adds a distinct reason for a distortion to survive: the
information that would remove it is held by the person whose future is being priced.
Finally, the accuracy of forecasts about people depends more on information than on bias. Self-markets were biased
toward YES, but most of their shortfall in accuracy came from prices that separated successes from failures less well,
and a statistical correction learned from past markets recovered little of it. The visible cues that might stand in for
private information, such as a person’s earlier record and their silence, added no detectable predictive value beyond the
price. Forecasts about people may therefore be harder to improve by disclosing public information or by correcting bias
than forecasts about events, because what they lack is held privately by the person.
5.2 Practical implications
Systems that make personal goals public, including commitment contracts, accountability communities, social fitness
apps, and prediction platforms [1, 2, 37, 40], increasingly show users what others expect of them. Three implications
follow, each a design hypothesis to be tested rather than a demonstrated remedy. First, crowd expectations about a
person’s goal can run optimistic, and designers who display them could show, alongside the crowd’s view, how often
similar goals by similar users succeeded. Second, because the person holds the information that decides the outcome,
features that invite the person to report progress, or to state their own probability, may improve such forecasts more than
features that attract more observers. Third, the bias is an average over markets, and a market’s price remains informative
about a person’s chances even though prices run high on average. Publicly noticed intentions can feel like progress [42],
and whether optimistic crowd signals help or hurt goal pursuit is an open question for such systems.
For prediction platforms, markets on individuals’ own conduct differ from markets on public events in a way that matters
for design. The person whose behavior is forecast trades with information others lack and usually decides the resolution.
In our data, the person’s purchases landed on the winning side more often than strangers’ only in self-markets, mostly
near the close. Rules about whether and when the subject may trade, how progress is disclosed, and how resolutions are
verified therefore shape both the accuracy of the price and its fairness to other traders.
5.3 Limitations and future research
Several features of the setting open directions for further work. The first concerns how far the findings generalize. The
markets use play money, and the platform’s users are a particular online community. Play-money markets forecast
sports about as well as real-money markets [29], but real money improved accuracy for other events [30], so replicating
the analysis with real stakes, and with users of mainstream goal-tracking or social platforms, would show how far
the pattern extends. The analysis is also limited to markets that resolved YES or NO. Markets that were cancelled or
resolved to a probability were about as common among self-markets as among external markets, but their outcomes are
unknown.
The second concerns measurement. The classification of questions and the measures of named outcomes, goals, and
encouragement rest on keyword rules. Independent coding confirmed the market classification, but it showed that the
unwanted-outcome and encouragement rules find only about half of the cases they target, and that a question’s title says
too little to code goal types reliably. Larger coded samples, or coding that draws on market descriptions, would sharpen
the comparisons of desirability and goal type, which here rest on few unwanted questions and on a coarse goal measure.
Prior interaction is measured within the sampled markets, so it captures observed contact on the platform rather than
friendship, and encouragement before a purchase was too rare to evaluate; data that link platform activity to offline
relationships would show whether people who know the person forecast better. Finally, the person usually reports the
outcome, and late purchases can reflect progress, control over the behavior, or resolution practices. Whether others
could verify an outcome could not be coded reliably from titles ( κ= 0.22 ), and studies of disputes and moderator
corrections could assess how reporting affects measured calibration.
The third concerns mechanism. The design is observational, and it cannot hold observers’ information fixed while their
stake in the person varies. Experiments that elicit probabilities from the person and from observers at the same moment,
vary how a question is framed (naming success or failure), display a reference class, or vary observers’ access to the
person’s progress separately from their stake in the person could test the accounts discussed here and the remedies they
suggest.
15

6 Conclusion
When people ask the crowd about their own futures, the crowd believes them too readily. Across 6,150 prediction
markets about people’s own goals and prospects, prices overstated the futures people posed for themselves, except
when the question named an outcome the person would not want, while markets about external events were close to
calibrated. The overstatement was not present when markets opened; it arose as observers traded, appeared where the
person never traded, and was largest in the week before close. Observers brought the outside view to events but not to
people, and the information that corrected prices came late and largely from the person. Platforms that turn personal
goals into public forecasts should not expect a crowd to supply the base rates that lab observers supply, and should look
to the person for the information that the crowd does not have.
References
[1] Sean A. Munson and Sunny Consolvo. Exploring goal-setting, rewards, self-monitoring, and sharing to motivate
physical activity. InProceedings of the 6th International Conference on Pervasive Computing Technologies for
Healthcare, pages 25–32, 2012. doi: 10.4108/icst.pervasivehealth.2012.248691.
[2] Juho Hamari and Jonna Koivisto. “Working out for likes”: An empirical study on social influence in exercise
gamification.Computers in Human Behavior, 50:333–347, 2015. doi: 10.1016/j.chb.2015.04.018.
[3] Roger Buehler, Dale Griffin, and Michael Ross. Exploring the “planning fallacy”: Why people underestimate
their task completion times.Journal of Personality and Social Psychology, 67(3):366–381, 1994. doi: 10.1037/
0022-3514.67.3.366.
[4] Derek J. Koehler and Connie S. K. Poon. Self-predictions overweight strength of current intentions.Journal of
Experimental Social Psychology, 42(4):517–524, 2006. doi: 10.1016/j.jesp.2005.08.003.
[5] Roger Buehler, Dale Griffin, and Johanna Peetz. The planning fallacy: Cognitive, motivational, and social
origins. InAdvances in Experimental Social Psychology, volume 43, pages 1–62. Academic Press, 2010. doi:
10.1016/S0065-2601(10)43001-4.
[6] Nicholas Epley and David Dunning. Feeling “holier than thou”: Are self-serving assessments produced by
errors in self- or social prediction?Journal of Personality and Social Psychology, 79(6):861–875, 2000. doi:
10.1037/0022-3514.79.6.861.
[7] Erik G. Helzer and David Dunning. Why and when peer prediction is superior to self-prediction: The weight
given to future aspiration versus past achievement.Journal of Personality and Social Psychology, 103(1):38–53,
2012. doi: 10.1037/a0028124.
[8] Justin Wolfers and Eric Zitzewitz. Prediction markets.Journal of Economic Perspectives, 18(2):107–126, 2004.
doi: 10.1257/0895330041371321.
[9] Kenneth J. Arrow, Robert Forsythe, Michael Gorham, Robert Hahn, Robin Hanson, John O. Ledyard, Saul
Levmore, Robert Litan, Paul Milgrom, Forrest D. Nelson, George R. Neumann, Marco Ottaviani, Thomas C.
Schelling, Robert J. Shiller, Vernon L. Smith, Erik Snowberg, Cass R. Sunstein, Paul C. Tetlock, Philip E. Tetlock,
Hal R. Varian, Justin Wolfers, and Eric Zitzewitz. The promise of prediction markets.Science, 320(5878):
877–878, 2008. doi: 10.1126/science.1157679.
[10] Itzhak Rasooly and Roberto Rozzi. How manipulable are prediction markets? arXiv preprint arXiv:2503.03312,
2025.
[11] Derek J. Koehler, Rebecca J. White, and Leslie K. John. Good intentions, optimistic self-predictions, and missed
opportunities.Social Psychological and Personality Science, 2(1):90–96, 2011. doi: 10.1177/1948550610375722.
[12] Ian R. Newby-Clark, Michael Ross, Roger Buehler, Derek J. Koehler, and Dale Griffin. People focus on optimistic
scenarios and disregard pessimistic scenarios while predicting task completion times.Journal of Experimental
Psychology: Applied, 6(3):171–182, 2000. doi: 10.1037/1076-898X.6.3.171.
[13] Paschal Sheeran and Thomas L. Webb. The intention–behavior gap.Social and Personality Psychology Compass,
10(9):503–518, 2016. doi: 10.1111/spc3.12265.
[14] Paschal Sheeran. Intention–behavior relations: A conceptual and empirical review.European Review of Social
Psychology, 12(1):1–36, 2002. doi: 10.1080/14792772143000003.
[15] Daniel Kahneman and Dan Lovallo. Timid choices and bold forecasts: A cognitive perspective on risk taking.
Management Science, 39(1):17–31, 1993. doi: 10.1287/mnsc.39.1.17.
[16] Bent Flyvbjerg. Curbing optimism bias and strategic misrepresentation in planning: Reference class forecasting
in practice.European Planning Studies, 16(1):3–21, 2008. doi: 10.1080/09654310701747936.
16

[17] Neil D. Weinstein. Unrealistic optimism about future life events.Journal of Personality and Social Psychology,
39(5):806–820, 1980. doi: 10.1037/0022-3514.39.5.806.
[18] Ziva Kunda. The case for motivated reasoning.Psychological Bulletin, 108(3):480–498, 1990. doi: 10.1037/
0033-2909.108.3.480.
[19] Zlatan Krizan and Paul D. Windschitl. The influence of outcome desirability on optimism.Psychological Bulletin,
133(1):95–121, 2007. doi: 10.1037/0033-2909.133.1.95.
[20] Roger Buehler, Dale Griffin, and Heather MacDonald. The role of motivated reasoning in optimistic time
predictions.Personality and Social Psychology Bulletin, 23(3):238–247, 1997. doi: 10.1177/0146167297233003.
[21] Cade Massey, Joseph P. Simmons, and David A. Armor. Hope over experience: Desirability and the persistence of
optimism.Psychological Science, 22(2):274–281, 2011. doi: 10.1177/0956797610396223.
[22] Joseph P. Simmons and Cade Massey. Is optimism real?Journal of Experimental Psychology: General, 141(4):
630–634, 2012. doi: 10.1037/a0027405.
[23] Elisha Babad and Yosi Katz. Wishful thinking—against all odds.Journal of Applied Social Psychology, 21(23):
1921–1938, 1991. doi: 10.1111/j.1559-1816.1991.tb00514.x.
[24] Simine Vazire. Who knows what about a person? The self–other knowledge asymmetry (SOKA) model.Journal
of Personality and Social Psychology, 98(2):281–300, 2010. doi: 10.1037/a0017908.
[25] Simine Vazire and Matthias R. Mehl. Knowing me, knowing you: The accuracy and unique predictive validity of
self-ratings and other-ratings of daily behavior.Journal of Personality and Social Psychology, 95(5):1202–1216,
2008. doi: 10.1037/a0013314.
[26] Amos Tversky and Derek J. Koehler. Support theory: A nonextensional representation of subjective probability.
Psychological Review, 101(4):547–567, 1994. doi: 10.1037/0033-295X.101.4.547.
[27] Robert Forsythe, Thomas A. Rietz, and Thomas W. Ross. Wishes, expectations and actions: A survey on price
formation in election stock markets.Journal of Economic Behavior & Organization, 39(1):83–110, 1999. doi:
10.1016/S0167-2681(99)00027-X.
[28] Robin Hanson and Ryan Oprea. A manipulator can aid prediction market accuracy.Economica, 76(302):304–314,
2009. doi: 10.1111/j.1468-0335.2008.00734.x.
[29] Emile Servan-Schreiber, Justin Wolfers, David M. Pennock, and Brian Galebach. Prediction markets: Does money
matter?Electronic Markets, 14(3):243–251, 2004. doi: 10.1080/1019678042000245254.
[30] E. S. Rosenbloom and William Notz. Statistical tests of real-money versus play-money prediction markets.
Electronic Markets, 16(1):63–69, 2006. doi: 10.1080/10196780500491303.
[31] Pavel Atanasov, Phillip Rescober, Eric Stone, Samuel A. Swift, Emile Servan-Schreiber, Philip Tetlock, Lyle
Ungar, and Barbara Mellers. Distilling the wisdom of crowds: Prediction markets vs. prediction polls.Management
Science, 63(3):691–706, 2017. doi: 10.1287/mnsc.2015.2374.
[32] Richard H. Thaler and William T. Ziemba. Anomalies: Parimutuel betting markets: Racetracks and lotteries.
Journal of Economic Perspectives, 2(2):161–174, 1988. doi: 10.1257/jep.2.2.161.
[33] Erik Snowberg and Justin Wolfers. Explaining the favorite–long shot bias: Is it risk-love or misperceptions?
Journal of Political Economy, 118(4):723–746, 2010. doi: 10.1086/655844.
[34] Lionel Page and Robert T. Clemen. Do prediction markets produce well-calibrated probability forecasts?The
Economic Journal, 123(568):491–513, 2013. doi: 10.1111/j.1468-0297.2012.02561.x.
[35] Marco Ottaviani and Peter Norman Sørensen. Price reaction to information with heterogeneous beliefs and
wealth effects: Underreaction, momentum, and reversal.American Economic Review, 105(1):1–34, 2015. doi:
10.1257/aer.20120881.
[36] Jan Lorenz, Heiko Rauhut, Frank Schweitzer, and Dirk Helbing. How social influence can undermine the
wisdom of crowd effect.Proceedings of the National Academy of Sciences, 108(22):9020–9025, 2011. doi:
10.1073/pnas.1008636108.
[37] Gharad Bryan, Dean Karlan, and Scott Nelson. Commitment devices.Annual Review of Economics, 2(1):671–698,
2010. doi: 10.1146/annurev.economics.102308.124324.
[38] Xavier Giné, Dean Karlan, and Jonathan Zinman. Put your money where your butt is: A commitment contract for
smoking cessation.American Economic Journal: Applied Economics, 2(4):213–235, 2010. doi: 10.1257/app.2.4.
213.
17

[39] Michael Sailer, Jan Ulrich Hense, Sarah Katharina Mayr, and Heinz Mandl. How gamification motivates: An
experimental study of the effects of specific game design elements on psychological need satisfaction.Computers
in Human Behavior, 69:371–380, 2017. doi: 10.1016/j.chb.2016.12.033.
[40] Jonna Koivisto and Juho Hamari. The rise of motivational information systems: A review of gamification research.
International Journal of Information Management, 45:191–210, 2019. doi: 10.1016/j.ijinfomgt.2018.10.013.
[41] Damon Centola. The spread of behavior in an online social network experiment.Science, 329(5996):1194–1197,
2010. doi: 10.1126/science.1185231.
[42] Peter M. Gollwitzer, Paschal Sheeran, Verena Michalski, and Andrea E. Seifert. When intentions go public:
Does social reality widen the intention–behavior gap?Psychological Science, 20(5):612–618, 2009. doi:
10.1111/j.1467-9280.2009.02336.x.
[43] Manifold Markets. Manifold API documentation.https://docs.manifold.markets/api, 2026.
[44] Danny Halawi, Fred Zhang, Chen Yueh-Han, and Jacob Steinhardt. Approaching human-level forecasting with
language models. InAdvances in Neural Information Processing Systems, volume 37, pages 50426–50468, 2024.
doi: 10.52202/079017-1598.
[45] Glenn W. Brier. Verification of forecasts expressed in terms of probability.Monthly Weather Review, 78(1):1–3,
1950. doi: 10.1175/1520-0493(1950)078<0001:VOFEIT>2.0.CO;2.
[46] Allan H. Murphy. A new vector partition of the probability score.Journal of Applied Meteorology, 12(4):595–600,
1973. doi: 10.1175/1520-0450(1973)012<0595:ANVPOT>2.0.CO;2.
[47] Jacob Cohen. A coefficient of agreement for nominal scales.Educational and Psychological Measurement, 20(1):
37–46, 1960. doi: 10.1177/001316446002000104.
[48] A. Colin Cameron, Jonah B. Gelbach, and Douglas L. Miller. Robust inference with multiway clustering.Journal
of Business & Economic Statistics, 29(2):238–249, 2011. doi: 10.1198/jbes.2010.07136.
[49] Sture Holm. A simple sequentially rejective multiple test procedure.Scandinavian Journal of Statistics, 6(2):
65–70, 1979.
A Sample construction and reconstruction
Table 9 traces the sample from the full list of markets retrieved from the platform to the analysis sample. Table 10
reports the checks of the reconstructed prices and executions described in Section 3. Table 11 compares how often
self-markets and external markets ended without a YES or NO resolution, among binary, mana-denominated markets
with at least two traders that closed before 1 July 2026, and shows the mean gap at each market’s last price when such
markets are added with a gap of zero, or when all of them are assigned NO or all YES.
18

Table 9: Sample construction.
Step Markets
All markets retrieved from the platform 194,347
Binary (yes/no) markets 140,090
Denominated in mana 139,818
Resolved YES or NO 98,456
At least two unique traders 94,701
of which first-person questions about the creator 6,272
of which external markets 81,791
of which other first-person markets 6,638
Sample: all first-person questions about the creator 6,272
Sample: external markets by self-market creators (up to 5 each) 4,548
Sample: external markets by other creators (random, quarter-stratified) 6,272
Sample total 17,092
of which with at least one comment 12,504
Analysis: forward-looking self-markets with an observer purchase 6,150
first-person questions set aside (retrospective, normative, present-state) 120
Analysis: external markets by other creators with an observer purchase 6,272
Analysis: external markets by self-market creators with an observer purchase 4,486
Note: The analysis also sets aside 62 external markets whose creators asked only questions outside the forward-
looking definition.
Table 10: Reconstruction of prices and executions from order records.
Order records in the sample markets 1,346,194
Consecutive orders whose prices connect: all orders 97.2%
filled, never-cancelled orders only 85.9%
Final price equal to the platform’s reported probability: all orders 99.4%
filled, never-cancelled orders only 91.9%
Cancelled orders with at least one fill 141,685
Purchase orders with a fill more than a minute after placement 37,578
Orders whose fills do not sum to the order’s shares 0
Purchase executions before close 901,706
from orders later cancelled 17.0%
from limit orders 30.2%
Note: Two consecutive orders connect when the probability before the later order equals the probability after the
earlier one. The reported probability is the market probability in the platform’s market list.
Table 11: Selection into a YES or NO resolution.
Status Mean gap at last price (pp)
Markets YES/NO Cancelled Probability Unresolved YES/NO only Others as priced Others NO; YES
Self-markets 6,475 92.0% 5.0% 1.3% 1.7%−4.5−4.1−7.9;+0.1
External markets 87,457 90.8% 4.6% 1.8% 2.8%−1.0−0.9−4.7;+4.6
Note: Binary, mana-denominated markets with at least two traders whose close date was before 1 July 2026. “Probability”
marks markets resolved to a probability. “Others as priced” counts every market without a YES or NO resolution with a gap of
zero; the last column assigns all of them NO, or all of them YES, at their last price.
19

B Coding rules
Market classification.A question is a self-market when it opens, after an optional bracketed tag and an optional short
time phrase followed by a comma (beginning with by, before, on, in, this, next, today, tonight, or tomorrow), with “will
I”, “can I”, “shall I”, or “am I going to”. The sampling frame used a broader lead that also admitted would, could, do,
does, am, should, and did; those questions are set aside in the analysis and used in a robustness check. A question is an
external market when it contains none of the words I, me, my, mine, myself, I’m, I’ll, I’ve, I’d, we, us, our, ours, or
ourselves. All remaining questions, for example those about a creator’s relatives or those phrased with “we”, belong
to neither group. External questions can still concern named people; dropping external questions that mention a user
handle, the word “creator”, or a third-person pronoun leaves the results unchanged (Table 8).
Unwanted named outcomes.A self-market question is flagged when YES names a lapse or an adverse event for the
creator: relapsing, breaking a streak, diet, or promise; losing a game, a job, money, mana, or a possession; failing;
missing a class, a flight, or a deadline; falling sick or testing positive; injury, hospitalization, or an accident; being fired,
laid off, banned, suspended, or arrested; regret; procrastinating, oversleeping, skipping, or staying up late; drinking
alcohol, smoking, vaping, or bingeing; going over budget; breaking up or dropping out; and demotion. The flag is
withdrawn when the question negates the term or asks about stopping or avoiding it (not, without, never, quit, stop,
avoid), names a mixed outcome (“promote or demote”, “lose or gain”), asks about a negative test, a vaccine, or a
recovery, or asks about the creator’s beliefs (believe, agree, convinced). The rules were refined by reading every
question flagged by an earlier version and keyword-in-context listings of unflagged questions containing related terms.
Goal content.The goal-type rule assigns each self-market question to the first matching category in the order restraint,
outcome, effort. Restraint terms include quit, stop, avoid, abstain, stay off, sober, relapse, no-spend, no social media,
and procrastinate. Outcome terms include accepted, admitted, hired, job offer, promoted, win, elected, approved,
funded, pregnant, sick, COVID, pass an exam, score, rank, qualify, followers, and price. Effort terms include gym,
work out, run, walk, lift, meditate, journal, write, post, publish, read, study, practice, finish, complete, submit, launch,
build, code, clean, cook, apply, wake up, go to bed, streak, daily, and times per week. Questions matching none of
the lists are unclassified. Many outcomes, such as exam results or audience growth, depend on both effort and outside
forces; the categories are coarse.
Encouragement.A comment encourages the creator when it contains a well-wishing expression such as good luck, best
of luck, you got this, you can do it, rooting for you, believe in you, go for it, keep going, fingers crossed, hope you make
it, don’t give up, or stay strong, or a flexed-biceps, four-leaf-clover, or crossed-fingers emoji. Congratulations (congrats,
well done, good job, proud of you, and party or clapping emoji) are coded separately and not counted, because they can
respond to an outcome that is already known; ambiguous cues (let’s go, hearts) are in neither list. An observer counts as
an encourager for a purchase only if the comment was posted before the purchase order was placed.
Prior interaction.An observer is a prior interactor of a creator in a market when the observer’s first trade or comment
in any other sampled market by the same creator predates the focal market’s creation. Because the sample includes
every self-market and up to five external markets per self-market creator, but only one sampled market for most other
creators, prior interaction is observed most completely for self-market creators.
Orders and executions.Price paths use every order, including cancelled and unfilled limit orders, in the order they
were placed; an order’s own price change is the difference between the probability after and before it. Purchases are fills
with positive shares and positive cost, dated at the time of the fill, excluding the platform’s automatic share redemptions;
a cancelled order keeps the fills it received before cancellation. Positions count purchases and sales up to the order
that set the final price; redemptions remove equal numbers of YES and NO shares and leave positions unchanged. A
purchase is automated when it was placed through the platform’s programming interface.
Table 12 compares these rules with the labels of two independent coders.
20

Table 12: Validation of the coding rules against two coders’ labels.
Coder 1 Coder 2 Agreed labels
Agreement between the two coders, Cohen’sκ(percent agreement)
Question is about the creator 0.98 (99.6%)
Time of the event (future, present, past) 0.93 (99.2%)
Forecast rather than advice 0.75 (99.0%)
Creator would want YES 0.91 (93.9%)
Creator’s control (effort, restraint, outcome, mixed) 0.49 (64.7%)
Outcome verifiable by others 0.22 (54.8%)
Comment encourages 0.95 (98.0%)
Comment congratulates 0.95 (98.8%)
Comment knows the outcome 0.52 (84.2%)
Comment doubts the creator 0.84 (97.8%)
The paper’s rules against the coders’ labels
Random self-markets coded as forward-looking questions about the creator 98.5% 99.5% 98.5%
Random external markets coded as not about the creator 98.0% 99.0% 98.0%
Set-aside first-person questions coded as forward-looking 20.0% 18.3% 15.0%
Unwanted-outcome rule: flagged questions coded unwanted (precision) 90% 86% 90%
Unwanted-outcome rule: unwanted questions it flags (recall)a 43% 47% 47%
Goal-type rule: category matches the coded controlb 69% 74% 66%
Encouragement rule: precision 85% 89% 88%
Encouragement rule: recalla 45% 43% 47%
Congratulation rule: precision 98% 97% 98%
Congratulation rule: recalla 50% 39% 66%
Note: Two coders labelled 726 market questions and 400 comments independently, without seeing market outcomes or the
rules’ labels. Questions came from five strata: 200 random self-markets, every question the unwanted-outcome rule flags, the
unflagged self-market questions containing an adverse word, 60 first-person questions set aside from the analysis, and 100
random external markets; comments were drawn from those flagged as encouraging, those flagged as congratulating, and the
rest. “Agreed labels” uses the items on which the coders agreed. aWeighted to the population of self-markets (questions) or
comments by the sampling strata. bAmong random self-markets the rule classifies (127 of 200).
21

C Additional tables
Tables 13 and 14 give the detailed numbers behind Sections 4.1 and 4.2. In both tables, a gap is the share of markets
that resolved YES minus the price, in percentage points, so a negative gap means that prices overstated how often YES
occurred.
Gaps under other forecasts.Table 13 repeats the comparison of Section 4.1 using prices other than the final price.
Each row uses a different price as the forecast. The first three columns give the mean gap in each group of markets,
and the last two give the difference between self-markets and each group of external markets, without controls. Three
patterns stand out. First, in the upper rows, under every forecast other than the opening price, self-markets overstated
YES more than external markets by other creators did, by 2.2 to 4.8 pp. Second, the opening price is the exception.
Most markets opened at the default 50% and fewer than half resolved YES, so every group has a negative gap at the
opening, but the gap was smaller for self-markets ( −4.8 against −7.6 pp): before trading began, self-markets were
not overpriced relative to external markets. Third, the bottom rows split the final price by range. The overstatement is
concentrated in markets whose final price lay between 20% and 80% (difference −8.2 pp), whereas markets priced
below 20% or above 80% were close to calibrated in both groups. Against the same creators’ external markets the
pattern is similar, but the differences for two early prices are smaller and not significant at the 5% level (−1.8 pp one
day after creation and−0.8 pp after the third observer purchase).
Table 13: Calibration gaps: share resolved YES minus price, in percentage points.
External markets Self minus external
Price used as the forecast Self-markets Other creators Same creators Other creators Same creators
Final price−4.4 (0.5)−0.9 (0.3)−1.3 (0.3)−3.5 (0.6)−3.1 (0.6)
Opening price−4.8 (1.1)−7.6 (0.7)−9.7 (0.8)+2.8 (1.3)+4.9 (1.3)
Price one day after creationa −9.2 (0.8)−5.5 (0.6)−7.4 (0.7)−3.7 (1.0)−1.8 (1.0)
Price one day before closea −5.0 (0.7)−0.2 (0.5)+0.0 (0.5)−4.8 (0.8)−5.0 (0.8)
Price at mid-life−7.5 (0.7)−2.7 (0.5)−3.7 (0.6)−4.8 (0.9)−3.9 (0.9)
Time-weighted average price−7.0 (0.7)−2.6 (0.5)−3.5 (0.6)−4.5 (0.8)−3.5 (0.9)
Price after third observer purchaseb −8.3 (0.8)−6.1 (0.6)−7.5 (0.7)−2.2 (1.0)−0.8 (1.0)
Final price, 20–80% only−9.4 (1.0)−1.2 (1.6)−3.2 (1.6)−8.2 (1.9)−6.2 (1.9)
Final price,<20% or>80% only−1.5 (0.4)−0.8 (0.2)−0.8 (0.2)
Note: Mean of Y−p , where Y= 1 if the market resolved YES; negative values mean that prices overstated how often
YES occurred. “Same creators” are external markets made by the creators of self-markets. Differences are coefficients on a
self-market indicator without other controls. Standard errors clustered by creator in parentheses. aMarkets open at the time
(one day after creation: 5,383 self-markets and 5,437 external markets by other creators). bMarkets with at least three observer
purchases.
Gaps over the market’s life.Table 14 follows calibration through the landmarks defined in Section 3.4, from the
opening to the final price; its last two columns are the estimates plotted in Figure 1B. For self-markets and external
markets by other creators, each row reports how many markets were open at that point, their mean gap, and the YES
rate implied for a market priced at 50% (a value below 50% means that such markets resolved YES less than half the
time). The last two columns give the self-market difference at the same price level, for all markets and for markets
in which the person never traded. Because these differences compare markets at the same price, they differ from the
raw differences in Table 13 (at the final price, −2.4 against −3.5 pp). A landmark a given time after creation and the
landmark the same time before close cover the same markets, namely those that lasted at least that long, so the two
7-day rows compare the same markets early and late in their lives.
Reading down the table shows three patterns. At the opening, self-markets were, if anything, underpriced: at the same
price they resolved YES 3.0 pp more often than external markets. Within an hour the sign reversed, and the difference
grew over the market’s life, peaking at −5.3 pp a week before close before narrowing to −2.4 pp at the final price.
The implied YES rate at 50% shows the same shift: in self-markets it fell from 45% at the opening to 38% seven days
after creation, whereas in external markets it stayed between 41% and 43% in the first week and rose to 50% a day
before close. Finally, in markets in which the person never traded, the difference was larger at every landmark after
the opening, from −3.9 pp after an hour to −7.6 pp a week before close, so the overstatement arose even where only
observers traded.
22

Table 14: Calibration at fixed points in the markets’ lives.
Markets open Mean gap (pp) YES rate at 50% Self minus external, same price (pp)
Point in the market’s life Self External Self External Self External All markets Person never traded
At the opening 6,150 6,272−4.8−7.6 45% 42%+3.0 (1.3)−1.2 (1.8)
1 hour after creation 6,047 6,055−8.0−5.8 42% 43%−1.1 (1.1)−3.9 (1.7)
6 hours after creation 5,925 5,864−8.3−5.2 41% 43%−2.0 (1.1)−5.5 (1.7)
1 day after creation 5,383 5,437−9.2−5.5 40% 43%−2.4 (1.0)−5.5 (1.7)
3 days after creation 4,932 4,914−9.8−6.0 39% 42%−2.4 (1.1)−5.7 (1.9)
7 days after creation 4,204 4,356−10.7−6.5 38% 41%−2.9 (1.1)−5.2 (1.9)
7 days before close 4,204 4,356−6.9−1.3 39% 48%−5.3 (0.9)−7.6 (1.5)
1 day before close 5,383 5,437−5.0−0.2 42% 50%−4.6 (0.8)−6.4 (1.3)
Final price 6,150 6,272−4.4−0.9 39% 47%−2.4 (0.5)−3.7 (1.0)
Note: External markets are those by other creators. A market enters a landmark after creation if it was still open at that
time, and a landmark before the close if it had opened by then; the price at a landmark is the market probability after the last
order at or before it. “YES rate at 50%” is the implied share resolving YES for a market priced at one half, from a logistic
recalibration. The same-price comparison regresses Y−p on a self-market indicator with fixed effects for ten equal-width
price bins; standard errors clustered by creator in parentheses. The last column keeps markets in which the creator made no
trade before the final price (2,466 self, 2,538 external); this label uses the market’s whole history.
23
