---
title: Consumer Behavior in Payment Failures and Retry Attempts in Online Ticket Purchasing
url: https://doi.org/10.34010/injuratech.v6i1.20734
category: consumer-behavior
subcategory: empirical
date: 2026-08
venue: International Journal of Research and Applied Technology
authors:
- Dmitrii Khaiurov
source: openalex-oa
pdf_url: https://ojs.unikom.ac.id/index.php/injuratech/article/download/20734/5988
pages: 13
chars: 44077
fetched_at: '2026-11-08T19:31:13+00:00'
kb_version: 1
---

# Consumer Behavior in Payment Failures and Retry Attempts in Online Ticket Purchasing

249

International Journal of Research and Applied Technology

6(1)(2026) 249-261
Journal homepage: https://ojs.unikom.ac.id/index.php/injuratech
Consumer Behavior in Payment Failures and Retry
Attempts in Online Ticket Purchasing
Dmitrii Khaiurov1*
1 CPO, PortalBilet, Russia
Email: *d.khaiurov@gmail.com
Abstract. A declined payment interrupts the purchase of an event ticket at the moment
of highest commitment, yet the behavioral response of the buyer to this interruption has
received limited attention. This study examines how consumers respond to payment
failures and how often interrupted orders are resolved successfully. The analysis draws
on 2 anonymized transaction datasets from the Russian ticketing industry: 25,811
acquiring operations from a ticket marketplace and 199,635 orders from 3 ticketing
companies wit hin 1 holding, covering January 2024 to June 2026. The study applies
transaction -level behavioral analysis to operational payment records and triangulates
consumer responses after a failure through the combination of operation -level and
order-level evidenc e. Declines affected 23.0% of payment attempts. A retry followed
55.7% of initially declined orders, the median pause before a repeated attempt equaled
3 minutes, and 43.7% of such orders ended in a completed payment. Recovery
depended on the cause of the failure: orders declined for reasons a buyer can correct,
such as an incorrect CVV code or insufficient funds, and recovered at close to twice the
rate of orders interrupted by processing errors. Retries made after a pause of 5 to 15
minutes succeeded in 7 4.8% of cases, while immediate repetition succeeded in 25.0% of
cases. Among recovered orders, 80.1% kept the original payment instrument. At the
order level, 27.6% of purchases expired before any payment method was selected. The
findings describe retrying  as a mass consumer response, quantify the recoverable share
of failed revenue, and provide platforms with guidance on designing retry prompts and
payment method switching at checkout. The results extend checkout abandonment
research into the interior of t he payment stage, add the interpretability of the failure
cause to models of service failure recovery, and document consumer persistence under
the time pressure of an expiring seat reservation.
Keywords: Checkout abandonment, Digital marketplace, E -commerce transactions,
Purchase recovery, Transaction decline.
1. Introduction
The purchase of an event ticket concentrates emotional involvement, scarce seat inventory,
and rigid time limits within 1 short session, a combination that distinguishes ticketing from
most other retail categories [1]. The payment step closes this session, and a declined transaction

250

International Journal of Research and Applied Technology

6(1)(2026) 249-261
Journal homepage: https://ojs.unikom.ac.id/index.php/injuratech
interrupts the purchase at the moment when the buyer's commitment is at its peak. The decline
forces an immediate decision: the consumer may try again with the same card, switch to
another payment method, or leave the checkout while the seat reservation expires. Platforms
register the financial consequences of these decisions every day, yet consumer research has
focused on the stages that precede payment and has given limited coverage to behavior within
the payment step [2].
The funnel for ticket purchases explains why this step deserves separate attention. The
buyer selects an event, chooses seats on a live map, receives a reservation with a countdown
timer, proceeds to the payment stage, selects a payment method, submits credentials, and
passes authentication, after which the acquirer routes the transaction to the issuing bank. A
failure at the last link differs from a failure at any earlier one because the buyer has already
invested search, selection, and data entry, holds a reservation of concrete seats, and faces a
timer that penalizes every minute of hesitation. The behavioral question of this study lies
within this narrow interval between the issuer's refusal and the expiration of the reservation,
an interval that lasts minutes, and that platform interfaces currently fill with a generic error
message.
Research on interrupted purchases has developed along 3 streams. Studies of cart and
checkout abandonment model the decision to leave an assembled order and trace its drivers
in clickstream records [3], in mobile checkout journeys [4], and in configurational analyses of
shopper attitudes [5]. In service failure, researchers have studied the relationships between a
digital service failure, trust, and willingness to repurchase  [6, 7]. Research on payment
behavior has examined antecedents to the use of mobile wallets and instant account to account
payments, including trust, habit and easing  [8, 9], the buyer's apprehension during the
payment confirmation step [2] and the effects of fewer clicks in checkout on th e purchase
decision in field experiments [10]. A meta-analysis of the expectancy-disconfirmation model
found that the difference between the expected and the actual level of service quality governs
satisfaction [11]. A structured comparison of these stream s clarifies the state of the art.
Abandonment research has established the drivers of exit from an assembled order and the
depth of the funnel at which exit occurs, yet its clickstream sources end at the payment
gateway and treat every terminated session a s 1 undifferentiated loss [3]. Service failure
research has established the consequences of a failed encounter for trust and for the willingness
to repurchase, yet its survey instruments record recalled episodes and lack the timing and the
cause of a speci fic transaction  [6, 7]. Research on payment behavior has established the
antecedents of method adoption and the friction costs of checkout, yet it examines completed
choices and leaves declined attempts outside the frame [2, 10]. These streams stop at the border
of the payment attempt itself. The decline of a specific transaction, the pause before a repeated
attempt, and the choice between the original card and a different instrument remain outside
published evidence, because surveys cannot capture events of this granularity, and clickstream
data end at the payment gateway. Ticketing sharpens the gap further, since an expiring
reservation compresses the time available for a second attempt, and the buyer weighs
persistence against the loss of the selected seat.
This study addresses the gap with transaction -level evidence. The objective is to describe
consumer behavior after a payment failure in online ticket purchasing and to identify the
conditions under which an interrupted order recovers into a completed pu rchase. Four
questions guide the analysis. First, how often do payments fail, and which causes dominate
the failures. Second, how fast and how persistently do consumers retry after a decline. Third,
which failures recover and through which payment instrume nts the recovery proceeds.

251

International Journal of Research and Applied Technology

6(1)(2026) 249-261
Journal homepage: https://ojs.unikom.ac.id/index.php/injuratech
Fourth, how do order outcomes differ across payment methods at the level of an entire
ticketing group. The evidence comes from 2 anonymized datasets of the Russian ticketing
industry that jointly cover 225,446 records over 2.5 ye ars, and the analysis combines funnel
statistics with comparisons of retry timing, persistence, recovery, and instrument switching.
A conceptual model connects the 4 questions into 1 behavioral sequence and guides the
interpretation of the results. Fig. 1 presents the model. A declined attempt delivers a message
whose content the buyer reads as an attribution of the cause, and the attributed locus separates
conditions the buyer can change during the reservation window from refusals of the issuing
bank and from errors of the processing system. The attribution feeds a decision under the
pressure of an expiring seat reservation, in which the buyer chooses among an immediate
repetition, a corrective pause followed by a new attempt, a switch of the payment instrument,
and an exit from the checkout. Each path terminates in the recovery of the order or in its
abandonment, and retry latency, persistence, and instrument choice serve as observable traces
of the decision.

Figure 1. Conceptual model of consumer behavior after a payment failure in online ticket
purchasing.
The study's contribution is threefold. First, it shifts the unit of observation from a session or
a survey response to a single payment operation, opening the interval between a decline and
the buyer's next action to direct measurement. Second, it connects the technical vocabulary of
acquiring, with its response codes and issuer refusals, to the behavioral constructs of
persistence, correction, and switching, which permits a reading of t he decline message as
information the consumer processes under time pressure. Third, it complements operation -
level depth with order-level breadth, since the same behavioral episode appears in both the
25,811 operations of 1 marketplace and the 199,635 orders of 3 companies, and the agreement
between the 2 views raises confidence in the described patterns.
The novelty of the study lies in the object of measurement. Published work on
abandonment, on service failure, and on payment adoption draws on surveys, laboratory
tasks, or clickstream records that terminate at the payment gateway, and, to the author's
knowledge, no available study observes. The present analysis ranks among the first to measure
transaction-level retry behavior, retry latency, order recove ry, and payment instrument
switching on real operational payment data, and the joint use of an operation-level array from
1 marketplace and an order -level array from 3 ticketing companies gives this measurement
depth and breadth at the same time.

252

International Journal of Research and Applied Technology

6(1)(2026) 249-261
Journal homepage: https://ojs.unikom.ac.id/index.php/injuratech

2. Method
The study relies on operational data of the Russian online ticketing industry collected
between January 2024 and June 2026. The first dataset covers the acquiring operations of a
ticket marketplace from January 1, 2024, to June 29, 2026. The second dataset covers the orders
of 3 ticketing companies under 1 holding over the same window. Both datasets were exported
from the payment infrastructure in anonymized form; card numbers were masked; and no
personal information entered the analysis, which used aggregates throughout.
The operation -level dataset contains 25,811 records. Each record includes the operation
status, a detailed decline reason returned by the issuing bank or the processing system, the
order number, the payment scheme, the issuing bank, the amount, and 2 timestamps
indicating the operation's creation and completion. The status equals Completed for 19,870
operations, Declined for 5,938 operations, and Canceled for 3 operations. The 25,811 operations
belong to 20,639 unique orders, and the deepest order contains 10 attempts. The first attempt
was declined in 4,567 orders, which form the base for the retry and recovery analysis.
Completed marketplace operations totaled 274.7 million rubles, and the median order amount
was 8,400 rubles.
The order-level dataset contains 199,635 records of the 3 companies. Each record includes
the order status, payment method, and amount. The status Confirmed marks a completed
purchase; Deadline_Expired marks an order in which the payment stage started but did not
finish before the reservation deadline; Rejected marks a refused payment; and Refunded,
together with Partial_Refunded, mark post -purchase returns. Confirmed orders generated
1.78 billion rubles of revenue over the observation window, expired orders carried 1.42 billion
rubles of unrealized volume, and rejected orders carried 242.4 million rubles.
The analysis uses 5 constructs. A payment failure denotes a Declined operation in the first
dataset and a Rejected or Deadline_Expired order in the second datas et. A retry denotes a
repeated operation that shares the order number with a preceding declined operation.
Recovery denotes an order whose first attempt was declined and whose later attempt reached
the Completed status. Retry latency denotes the interval between the creation timestamps of
consecutive attempts within 1 order. Instrument switching denotes a difference in the payment
scheme or in the issuing bank between the first declined attempt and the first completed
attempt of the same order.
The 2 datasets complement each other by construction. The operation-level array observes
every attempt within an order and therefore supports measuring retries, latencies, recovery,
and instrument switching, yet it belongs to 1 marketplace and covers a specific acquir ing
contract. The order-level array lacks the attempt structure and observes each order only once,
yet it spans 3 companies with different audiences, event repertoires, and payment method
shares, and therefore tests whether the marketplace patterns describ e an idiosyncrasy or a
property of the category. The combination follows the logic of triangulation, in which depth
on a narrow base and breadth on a shallow base compensate for each other's blind zones.
Data preparation involved 4 operations. Yearly export files of each company were merged
into 1 order -level array, and a spelling variant of 1 company name in the source files was
unified before aggregation. Timestamps of the operation-level dataset were parsed from day-
first strings into datetime values. Op erations within each order were sorted by the creation
timestamp, and the sequence position of every attempt was derived from this order. For the
analysis of amount effects, initially declined orders were split into terciles of the first-attempt

253

International Journal of Research and Applied Technology

6(1)(2026) 249-261
Journal homepage: https://ojs.unikom.ac.id/index.php/injuratech
amount, with boundaries at 6,600 and 17,600 rubles, and median amounts of 3,600, 11,000, and
36,000 rubles in the low, middle, and high terciles, respectively.
Three properties of the measurement deserve attention. The decline reason reflects the
response code of the issuing bank or of the processing system, so the classification by the locus
of the failure follows the technical semantics of these codes and approximates the causal
explanation available to the buyer through the interface message. The buyer's identity is
confined to 1 order number, meaning that a return from the same person under a new order
counts as a new purchase, and the reported recovery rate therefore serves as a lower bound
for the true behavioral recovery rate. The order-level dataset records the payment method that
reached the gateway, so an expired order without a selected method indicates that the buyer
left the checkout before entering any payment details.
The classification of decline reasons by the locus of the failure follows a fixed codin g
scheme, which Table 1 documents for reproducibility. Each response code of the acquiring
documentation received 1 of 3 locus labels. A code entered the buyer-correctable class when
the named condition admits a change by the buyer during the reservation window, the issuer-
related class collects refusals that originate in the decisions of the issuing bank, and the
processing-related class collects errors of the acquiring and processing systems. The table also
reports the share of each code among all decline s, so the weight of every class in the failure
structure follows from the same source.
Table 1. Classification of decline response codes by the attributed locus of the failure.
Response code Attributed
locus
Share of
declines,
%
Rationale for the assignment
Exceed
withdrawal
frequency
Buyer-
correctable
54.4 Card limit on the frequency or
volume of withdrawals that the buyer
can raise in the banking application
Insufficient funds  Buyer-
correctable
6.6 Account balance that the buyer can
replenish before a new attempt
Expired card  Buyer-
correctable
3.1 Validity defect that the buyer resolves
with another instrument
Incorrect CVV Buyer-
correctable
2.7 Input error that reentry of the card
details removes
3-D Secure
authentication
failed
Issuer-related 8.9 Outcome of the authentication
challenge inside the issuer domain
Internal issuer
response code
Issuer-related 7.6 Bank-internal refusal without
corrective guidance for the buyer
Do not honor  Issuer-related 2.7 Opaque refusal of the issuing bank
without a stated cause
Unable to process  Processing-
related
6.7 Error inside the acquiring or
processing system
Residual technical
codes
Processing-
related
7.3 Heterogeneous low -frequency
responses of the payment
infrastructure

The analysis proceeds in 4 steps. The first step establishes the incidence of failures and the
distribution of reasons for decline. The second step measures retry frequency, persistence, and

254

International Journal of Research and Applied Technology

6(1)(2026) 249-261
Journal homepage: https://ojs.unikom.ac.id/index.php/injuratech
latency, and relates the success of a retry to the pause that precedes it. The third step computes
recovery rates by the reason of the first decline, classifies the reasons by the attributed locus of
the failure according to the coding scheme of Table 1, which separates causes a buyer can
correct from causes located at the issuing bank and from causes located in the processing
system, and decomposes recovered orders by the relation between the failed and the successful
instrument. The fourth step aggregates order outcomes across the holding and compares
payment methods, conditioning on orders with a selected method. Latency intervals span 7
buckets, from under 1 minute to over 24 hours, and the success of a retry equals the share of
completed operations across the retries in a bucket. Computations used Python 3 with the
pandas library, and the classification of decline reasons followed the response codes of the
acquiring documentation.

3. Results and Discussion
Declines affected 5,938 of 25,811 payment attempts at the marketplace, corresponding to
23.0% of operations from January 2024 to June 2026. The rate remained near 21.5% in 2024 and
20.4% in 2025, and rose to 30.6% in the first half of 2026, so the failure of a payment reflects a
stable background of ticket retailing rather than an episodic disturbance. One cause dominates
the structure of failures. The issuer response ExceedWithdrawalFrequency accounts for 54.4%
of all declines and reflects card limits on the frequency or the volume of withdrawals. Failed
3-D Secure authentication accounts for 8.9%; an internal issuer response code adds 7.6%; the
processing response UnableToProcess adds 6.7%; insufficient funds adds 6.6%; an expired
card adds 3.1%; an incorrect CVV code adds 2.7%; and the opaque issuer refusal DoNotHonor
adds 2.7%. The structure carries behavioral meaning. Limits, balances, card validity, and input
errors are within the buyer's control, whereas processing errors and opaque refusals leave the
buyer without a corrective action; the following sections show that this distinction predicts
both persistence and recovery.
The failure background moves over time and across schemes. The decline rate equaled
21.5% in 2024 and 20.4% in 2025 and rose to 30.6% in the first half of 2026, while the recovery
rate of initially declined orders grew from 39.3% in 2024 to 41.2% in 2025 and 49.4% in 2026.
The 2 movements together indicate that a growing share of declines belongs to the correctable
classes, since buyers convert an increasing portion of failures into completed payments. The
daily rhythm adds a nuance: operations created between midnight and 7 a.m. fail in 29.0% of
cases, compared with 21.7% for daytime operations, a gap that matches the concentration of
limit-related refusals at the end of a spending day. Payment schemes also separate the risk.
Transactions of the domestic scheme MIR fail in 24.0% of cases across 18,851 operations, Visa
transactions fail in 26.8% of cases across 3,108 operations, and Mastercard transactions fail in
13.9% of cases across 3,787 operations, a spread that reappears at the order level of the holding
in the confirmation gap between card types.
A retry followed the first decline in 55.7% of the 4,567 initially declined orders, a nd the
remaining 44.3% of these orders contain a single abandoned attempt. Persistence remains
shallow; the mean number of attempts per initially declined order is 1.75, and orders with
more than 3 attempts account for less than 4% of the group. The reacti on's timing is
compressed. Fig. 2 presents the distribution of the 3,308 retries that followed a decline across
latency intervals, together with the success rate of a retry in each interval. The median pause
between a failure and the next attempt is 3 minutes; 68.1% of retries occur within 5 minutes of
the failure, and retries more than 1 hour after the failure account for 4.2% of the total. Success
depends on the pause. Immediate repetition within 1 minute succeeds in 25.0% of cases, a retry

255

International Journal of Research and Applied Technology

6(1)(2026) 249-261
Journal homepage: https://ojs.unikom.ac.id/index.php/injuratech
after a pause of 1 to 5 minutes succeeds in 59.7% of cases, and a retry after 5 to 15 minutes
reaches 74.8%. The curve then declines toward 50.0% for pauses of 1 to 6 hours and 43.9% for
pauses of 6 to 24 hours, while the 85.0% success rate for retries later than 24 hours rests on a
small subsample and warrants caution. The pattern separates 2 behavioral modes. An
impulsive repetition reproduces the failed conditions and inherits the issuer's refusal, whereas
a short corrective pause gives the buyer time to raise a limit, replenish an account, or reenter
card details, after which the second attempt succeeds. The reservation timer in a ticketing
checkout compresses exactly this corrective window, linking the retry pattern to the time
pressure that distinguishes the category [1]. The latency gradient admits a selection reading
alongside the causal one, since buyers who pause may differ from buyers who repeat at once
in the course of their failure or in their composure, and the observational design of the study
cannot separate the effect of the pause from the effect of the person. The managerial reading
survives this ambiguity in a weakened form, because an interface that inserts a short diagnostic
step converts a part of the impulsive segment into the corrective one, regardless of the source
of the original difference.
The depth of persistence falls fast. Among the 4,567 initially declined orders, 2,024 contain
a single attempt, 1,924 contain 2 attempts, 457 contain 3 attempts, and 162 contain 4 or more
attempts, so a fourth attempt exists in 3.5% of interrupted orders. The mean of 1.75 attempts
hides this asymmetry, since the typical persistent buyer makes exactly 1 additional attempt
and stops after its outcome. The distribution matches the incentive structure of a ticketing
checkout, where each additional attempt consumes a portion of the reservation window and
the marginal information from a repeated identical failure approach 0 after the second refusal.

Figure 2. Latency of retry attempts after a payment decline and retry success rate by latency,
n = 3,308 retry attempts, marketplace data for January 2024 to June 2026

Recovery closes the loop between a failure and a purchase. Among the 4,567 orders with a
declined first attempt, 43.7% reached a completed payment, an d recovered orders returned
46.7 million rubles, which equals 17.0% of the marketplace's completed payment volume.
Orders that never recovered accounted for 65.8 million rubles in attempted volume. Recovery
accumulates fast. The second attempt lifts the cumulative recovered share to 36.6%, the third
attempt lifts it to 42.0%, and the curve reaches its plateau of 43.7% by the sixth attempt, so
attempts beyond the third add under 2 percentage points. Fig. 3 relates the recovery rate to the
reason for the first decline and groups the reasons by the failure's attributed locus.

256

International Journal of Research and Applied Technology

6(1)(2026) 249-261
Journal homepage: https://ojs.unikom.ac.id/index.php/injuratech

Figure 3. Order recovery rate by reason of the first payment decline, n = 4,567 initially
declined orders, the dotted line marks the overall recovery rate of 43.7%

Orders interrupted by an incorrect CVV recover in 68.5% of cases, insufficient funds recover
in 66.2% of cases, and an expired card recovers in 59.9% of cases. The opaque issuer refusal
DoNotHonor recovers in 57.1% of cases and the buyer-correctable withdrawal-frequency limit
in 44.4% , failed authentication recovers in 42.6% of cases, and the system -side response
UnableToProcess together with the residual group recover in 28.6% and 22.6% of cases. Retry
propensity follows the same gradient; buyers repeat the attempt after 74.8% of CVV errors and
after 41.9% of processing errors. Consumers read the decline message as a diagnosis. A failure
that names a correctable cause invites persistence and rewards it, whereas an opaque or
technical failure suppresses the second attempt and lowers its payoff. This gradient mirrors
the role of attributed controllability in reactions to online service failures [6] and follows the
logic of expectancy disconfirmation, in which the interpretation of a service gap shapes the
behavioral response to it [11]. Attribution theory supplies the frame for this gradient, since the
perceived locus, controllability, and stability of a cause govern the reaction to a negative
outcome, and a decline message operates as a direct manipulation of these attributiona l
dimensions [12]. A message that places the cause within the buyer’s control invites coping
through correction, while a message that places the cause in the bank or in the infrastructure
signals a state the buyer cannot change, in which a repeated attempt  promises little.
Information processing under time pressure completes the account, because an expiring
reservation narrows the search for alternatives and pushes the buyer toward the action that
the message itself makes salient. The finding also refines s ervice-recovery research: the
platform receives a second chance without an apology and without compensation, because the
buyer performs the recovery personally whenever the diagnosis permits a correction [7]. The
data document the association between the named cause and the rates of retry and recovery,
while the cognitive step between the message and the action stays outside the records and
holds the status of a plausible interpretation.
The amount at stake shapes persistence to a measurable and bounded deg ree. Initially
declined orders of the low tercile, with a median first-attempt amount of 3,600 rubles, retried
in 51.6% of cases and recovered in 39.5% of cases. Orders of the middle tercile, with a median
of 11,000 rubles, retried in 56.9% of cases and re covered in 44.8% of cases, and orders of the
high tercile, with a median of 36,000 rubles, retried in 57.7% of cases and recovered in 45.7%

257

International Journal of Research and Applied Technology

6(1)(2026) 249-261
Journal homepage: https://ojs.unikom.ac.id/index.php/injuratech
of cases. The gradient stays moderate; a 10 -fold difference in the median amount shifts
recovery by 6.2 percentage points, whereas the difference between a correctable and a technical
failure shifts it by more than 40 percentage points. The comparison narrows the room for a
purely economic account of retry behavior and supports an informational account, in which
the content of the decline message outweighs the value of the interrupted basket in the buyer's
decision.
The mechanism of successful recovery lies in the choice of payment instrument. Table 2
decomposes the 1,997 recovered orders by the relation between the inst rument of the first
declined attempt and the instrument of the first completed attempt of the same order.

Table 2. Payment instrument switching among recovered orders due to the first decline.
First-decline
reason
Recovered
orders, n
Same
instrument, %
Different issuer,
same scheme, %
Different payment
scheme, %
Insufficient
funds
217  90.3 2.8 6.9
Do not honor  66 87.9 6.1 6.1
Incorrect CVV 85 87.1 1.2 11.8
Withdrawal
frequency limit
1,143  82.9 8.9 8.1
Expired card  85 76.5 5.9 17.6
3-D Secure
authentication
failed
170  74.7 13.5 11.8
All recovered
orders
1,997  80.1 8.4 11.5

A share of 80.1% of recovered orders finished with the same card, 8.4% finished with a card
from a different issuing bank within the same scheme, and 11.5% finished after a switch to a
different payment scheme. Switching concentrates where the original instrument lost its
validity. An expired card led to a change of the instrument in 23.5% of its recoveries, a failed
authentication in 25.3%, an insufficient f unds error in 9.7%, and a CVV error in 12.9%.
Persistence with the original instrument serves as the default recovery path, and the buyer
abandons the card when its defect prevents further attempts. The default carries a managerial
consequence, since an in terface that proposes an alternative instrument after every failure
interferes with the dominant behavior, whereas a proposal conditioned on the failure type
supports it.
The composition of the switching categories clarifies the buyer's resources. A completed
attempt with a card from a different issuing bank within the same scheme, which covers 8.4%
of recoveries, indicates a second card is already present in the wallet or in the device's saved
methods, and its use requires seconds. A switch to the payment scheme, which covers 11.5%
of recoveries, is more often accompanied by authentication failures or card validity issues,
where a defective credential blocks the entire scheme for the buyer. The remaining 80.1% of
recoveries proceed through the original card, and their weight explains why the cumulative
recovery curve saturates at the third attempt, since a correction of a limit, a balance, or an input
error either works at once or reveals the failure as uncorrectable. In money terms, the recovered
orders returned 46.7 million rubles against 65.8 million rubles of attempted volume in orders

258

International Journal of Research and Applied Technology

6(1)(2026) 249-261
Journal homepage: https://ojs.unikom.ac.id/index.php/injuratech
that never recovered, so the failure stage of the marketplace divides close to 275 million rubles
of realized revenue into a loss pool equal to 24% of that.
The order-level view across the holding widens the frame from a failed operation to a failed
purchase. Of the 199,635 orders, 199,603 reached a terminal status; among them Confirmed
orders form 63.7% , Deadline_Expired orders form 27.6%, Rejected orders form 4.9%, and
refunds cover the remaining 3.8%. In terms of money, the expired orders carried 1.42 billion
rubles of unrealized volume against 1.78 billion rubles of confirmed revenue, which makes the
expiration of a started payment the largest single loss channel for the group. Payment methods
are split across orders that selected a method, because an expired order leaves the method field
empty in 99.9% of cases. Orders paid through the in stant account -to-account scheme reach
confirmation in 94.5% of cases, and orders paid through wallet services reach confirmation in
94.2% of cases, while card orders reach 86.4% for Mastercard, 83.8% for Visa, and 77.9% for the
domestic scheme MIR, which also carries a rejection share of 13.6%. Two conclusions follow.
First, the silent loss of a ticketing order occurs before any card number is entered into the form,
which places this loss closer to late -stage checkout abandonment than to a technical refusal
and extends abandonment research into the interior of the payment stage  [4-5]. The 27.6%
share of expired orders sits below the abandonment levels reported for retail carts, since the
observation starts after seat selection, at a depth of the funnel where commitment has already
filtered the traffic. Second, the confirmation gap between instant schemes and manual card
entry aligns with adoption research, which shows that reduced input effort and trusted
authentication within a banking application drive both use and completion of a payment [8-
9].
The near -0 rejection rate of the instant account -to-account scheme warrants a separate
remark, as its 37,140 orders show a 0.0% rejection rate, compared with 13.6% for the domestic
card scheme. The instant scheme tra nsfers the entire authentication to the buyer's banking
application, removes the manual entry of card credentials, and settles from the current
account, eliminating the 3 largest decline categories of the card path at once: limit refusals,
authentication failures, and input errors. The scheme therefore functions as a built-in recovery
channel, and its position in the interface after a card failure carries direct revenue
consequences, which the switching behavior described above addresses from the buyer's side.
The pattern holds across the 3 brands of the holding. The largest company confirms 62.8%
of its 85,972 orders, the second confirms 63.3% of its 80,768 orders, and the third confirms 67.3%
of its 32,863 orders, while the expiration share ranges from 24.4% to 28.5%, and the rejection
share stays near 5% at every brand. The narrow spread across brands with different audiences
and with median order amounts between 8,200 and 10,200 rubles points to a structural origin
of the losses, which sit in the design o f the payment stage and in the behavior this design
induces, and which therefore respond to interface changes at any of the brands in a comparable
way.
The results carry 2 theoretical consequences. The first consequence concerns the boundary
between abandonment research and failure research. Published models treat the exit from a
checkout as a decision of the consumer and treat a technical refusal as an event outside
consumer behavior, whereas the evidence here shows a single episode in which the refusal
supplies information and the consumer answers it with persistence, correction, switching, or
exit [6], [3]. A complete model of the final funnel stage needs the decision and the event within
1 frame. The second consequence concerns expectancy disconfirmation. The decline of a paid-
for, time-limited good constitutes a sharp negative disconfirmation, and the observed behavior
shows that its effect depends on the interpretability of the gap: a named, correctable cause

259

International Journal of Research and Applied Technology

6(1)(2026) 249-261
Journal homepage: https://ojs.unikom.ac.id/index.php/injuratech
converts the disconfirmation into action, wh ile an opaque cause converts it into exit  [11].
Interpretability of a service gap thus enters the paradigm as a moderator that transaction data
measures directly.
The results translate into design levers for the payment step. First, the recovery curve
supports an active retry policy: close to half of failed orders return without any platform
intervention, attempts beyond the third add under 2 percentage points, and prompts should
focus on the first 2 attempts. Second, the latency pattern argues against inst ant automatic
repetition and in favor of a short, guided pause in which the interface names the cause of the
failure and proposes a concrete correction, a design that converts the observed 25.0% success
of impulsive retries into the 74.8% success of correc tive ones. Third, the switching pattern
supports an early offer of an alternative instrument after failures that invalidate the card, and
the confirmation gap between payment methods supports the promotion of low -friction
checkout schemes, a direction consistent with field evidence on the causal effect of reduced
clicks on purchases  [10]. Fourth, the concentration of silent losses before method selection
shifts managerial attention from the acquirer to the checkout screen itself, where reservation
timers, form length, and the visibility of payment options govern order expiration [5], [2]. The
economics of these levers follow from the observed magnitudes: a recovered order returns
8,400 rubles at the median, the recovered flow of the marketplace reached 46.7 million rubles
over the window, and the expired flow of the holding reached 1.42 billion rubles, so a shift of
several percentage points in recovery or in expiration translates into a material share of annual
revenue.
A comparison with published magnitudes places the findings on the map of the literature.
Abandonment studies report that most assembled retail carts never convert, whereas 27.6% of
ticketing orders expire after seat selection, and the difference reflects the depth of the
observation point, since a buyer who reached the payment stage of a ticketing checkout has
already passed the filters at which retail carts empty [5], [3]. Recovery magnitudes lack direct
analogs in consumer journals, and the 43.7% figure therefore serves as a first benchmark for
the category. Generalization of the numbers requires care. The market under study runs on a
domestic card scheme, on an instant account -to-account system with wide adoption, and on
banking applications that handle authentication, so the composition of decline reasons and the
payoff of a corrective pause may differ in markets with other authentication regimes [8-9]. The
behavioral core of the findings, the reading of a failure message as a diagnosis, and the
concentration of recovery in the earliest attem pts, rests on mechanisms without a link to a
specific scheme and travels across markets with fewer reservations. A further boundary
separates the empirical layer of the study from its interpretive layer. Frequencies, latencies,
recovery rates, and switching shares follow from the records without additional assumptions,
whereas the mechanisms proposed for them, such as the replenishment of an account during
a corrective pause or the reading of a message as a diagnosis, represent theoretical
explanations that the experimental agenda below is designed to test.
The observational findings define a compact experimental agenda. A first test randomizes
the content of the failure screen between a raw response code and a plain-language diagnosis
with a suggested correction and measures the shift in retry propensity and recovery across the
locus classes of Fig. 3. A second test randomizes the timing policy between an immediate
automatic repetition and a guided pause of several minutes and measures whether the 74.8%
success of delayed retries survives an exogenous assignment of the delay. A third test
randomizes the moment at which the interface proposes an alternative payment method, after
the first failure, or after a failure that invalidates the card, and measures completion together

260

International Journal of Research and Applied Technology

6(1)(2026) 249-261
Journal homepage: https://ojs.unikom.ac.id/index.php/injuratech
with the satisfaction of the buyer. A fourth test varies the reservation timer after a failed
attempt, since extending the window removes the sharpest constraint on the corrective pause.
Each test relies on metrics this study has already benchmarked, which turns the reported rates
into baselines for effect-size planning.

4. Conclusion
This study described consumer behavior following payment failures in online ticket
purchasing, based on 25,811 acquiring operations from a ticket marketplace and 199,635 orders
from 3 ticketing companies, observed between January 2024 and June 2026. Declines
interrupted 23.0% of payment attempts; a retry followed 55.7% of initially declined orders,
with a median pause of 3 minutes; and 43.7% of interrupted orde rs ended in a completed
payment, with recovery concentrated in the second and third attempts.
The outcome of a retry depended on the cause of the failure and on its timing; causes a
buyer can correct led to recovery at close to twice the rate of technical causes, a pause of 5 to
15 minutes raised the success of a repetition to 74.8% against 25.0% for an immediate one, and
80.1% of recovered orders kept the original payment instrument. At the group level, expiration
of a started payment before selecting a m ethod accounted for the largest loss channel, with
1.42 billion rubles in unrealized volume, and instant account-to-account payments confirmed
orders more often than manual card entry.
The findings rest on 1 national market and 1 industry, the data describe the payment stage
without the preceding funnel, and the observational design excludes causal claims, so
replication in other markets and experimental tests of retry prompts remain tasks for future
research. For practitioners, the results quantify the re coverable share of failed revenue and
justify a retry design that names the cause of a failure, schedules a short pause, and offers an
instrument switch when the original card loses its validity.

References
[1] Kim, K. Y., López, C., & Lee, Y. H. (2025). Get your tickets here: An examination of how
reputation and pricing strategies of ticket sellers affect consumers’ willingness to
purchase sport tickets. Sport Marketing Quarterly, 34 (1), 16 –30.
https://doi.org/10.32731/SMQ.341.032025.02
[2] Li, Z., Liu, J., Chen, J., & Zhang, Y. (2026). Why consumers hesitate to pay online: Evidence
from online transactions. Australian Journal of Management, 51 (1), 147 –173.
https://doi.org/10.1177/03128962241312715
[3] Kukar-Kinney, M., Scheinbaum, A. C., Orimoloye, L. O., Carlson, J. R., & He, H. (2022). A
model of online shopping cart abandonment: Evidence from e -tail clickstream data.
Journal of the Academy of Marketing Science, 50 (5), 961 –980.
https://doi.org/10.1007/s11747-022-00857-8
[4] Kapoor, A. P., & Vij, M. (2021). Following you wherever you go: Mobile shopping ‘cart-
checkout’ abandonment. Journal of Retailing and Consumer Services, 61 , 102553.
https://doi.org/10.1016/j.jretconser.2021.102553
[5] Khan, A., Rezaei, S., &  Valaei, N. (2022). Social commerce advertising avoidance and
shopping cart abandonment: A fs/QCA analysis of German consumers. Journal of
Retailing and Consumer Services, 67 , 102976.
https://doi.org/10.1016/j.jretconser.2022.102976

261

International Journal of Research and Applied Technology

6(1)(2026) 249-261
Journal homepage: https://ojs.unikom.ac.id/index.php/injuratech
[6] Adil, M., Sadiq, M., Je barajakirthy, C., Maseeh, H. I., Sangroya, D., & Bharti, K. (2022).
Online service failure: Antecedents, moderators and consequences. Journal of Service
Theory and Practice, 32(6), 797–842. https://doi.org/10.1108/JSTP-01-2022-0019
[7] Gao, J., Yao, L., Xiao, X., & Li, P. (2022). Recover from failure: Examining the impact of
service recovery stages on relationship marketing strategies. Frontiers in Psychology, 13,
852306. https://doi.org/10.3389/fpsyg.2022.852306
[8] Bailey, A. A., Bonifield, C. M., Arias, A., & Villegas, J. (2022). Mobile payment adoption in
Latin America. Journal of Services Marketing, 36 (8), 1058 –1075.
https://doi.org/10.1108/JSM-04-2021-0130
[9] Padma Kiran, K., & Vedala , N. S. (2025). Assessing Unified Payments Interface (UPI)
adoption and usage through the interplay of UTAUT factors. Humanities and Social
Sciences Communications, 12, 1060. https://doi.org/10.1057/s41599-025-05313-w
[10] Unal, M., & Park, Y.-H. (2023). Fewer clicks, more purchases. Management Science, 69(12),
7317 –7334. https://doi.org/10.1287/mnsc.2023.4716
[11] Schiebler, T., Lee, N., & Brodbeck, F. C. (2026). Expectancy-disconfirmation and consumer
satisfaction: A meta-analysis. Journal of the Academy of Marketing Science, 54 (1), 91–112.
https://doi.org/10.1007/s11747-024-01078-x
[12] Weiner, B. (2000). Attribution thoughts about consumer behavior. Journal of Consumer
Research, 27(3), 382–387. https://doi.org/10.1086/317592
