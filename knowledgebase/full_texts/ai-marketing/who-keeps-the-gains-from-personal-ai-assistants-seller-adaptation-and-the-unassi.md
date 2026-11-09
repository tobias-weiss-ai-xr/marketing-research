---
title: Who Keeps the Gains from Personal AI Assistants? Seller Adaptation and the Unassisted in a Language-Model
  Market Simulation
url: https://arxiv.org/abs/2610.05823
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Haonan Huang
- Joey Xiao
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.05823
pages: 11
chars: 43417
fetched_at: '2026-11-08T13:23:37+00:00'
kb_version: 1
---

# Who Keeps the Gains from Personal AI Assistants? Seller Adaptation and the Unassisted in a Language-Model Market Simulation

Who Keeps the Gains from Personal AI Assistants? Seller
Adaptation and the Unassisted in a Language-Model Market
Simulation
Haonan Huang
Princeton University
Joey Xiao
New York University
Abstract
Personal AI assistants are beginning to transact for con-
sumers,andearlyadopterscapturerealsavings. Whether
those savings survive, and what happens to consumers
who have no assistant, depends on how sellers respond
— a question single-user evidence cannot answer. We
build an agent-based rental market in which language
models playconsumers, assistants, and sixadaptive sell-
ers guided by an algorithmic pricing tool. Half the pop-
ulationreceivesanassistantunderanadvisoryoranexe-
cuting mandate; the contract pairs a fee only the renter’s
physical action avoids with a pre-selected add-on an au-
thorisedassistantcancancelonline. Ananalyticalbench-
mark and a behaviourally calibrated rule market supply
ex-antepredictions,andpairedbrancheswithfrozenver-
sus adaptive sellers separate adoption effects from mar-
ketfeedback. Acrossthirtysimulatedmarkets,executing
assistantscutadopters’spendingby13.7USDperrenter-
daywhensellersarefrozen;adaptationclawsbackabout
athird, leaving8.7, withthegainsarrivingbothaslower
billsandasrentalscompletedatall. Sellersraiseheadline
rateswhilecuttingfees,andthecalibratedforecastofthe
burdenonunassistedconsumers(+3.6)doesnottransfer:
their mean spending change is +0.4, confidence interval
−0.6 to +1.3. Seller-model swaps and a within-market
transfer of fee-setting to the pricing tool show that fee
conduct, and with it the division of the gains, is decided
on the seller side. Assistants, we conclude, should be
evaluated at market level — completion, total spending,
and non-users included — and the comparison layers lo-
cate exactly where a calibrated behavioural forecast fails
in a language-model market.
1 Introduction
Assistants that act, rather than merely answer, are reach-
ing consumers now: a deployed agent asks its principal
beforeeachpurchaseandoperatesinsidescopedappper-
missions[1],andthemandatestructuresthatwillgovern
suchdelegationarebeingdesignedinparallel[2,3]. Dif-
fusion is already measurably uneven across customers
and journey stages [4], so for years every market will
mix assisted and unassisted customers. On the individ-
ual scale the technology plainly works. In a randomised
fieldmarketplace,ashoppingtoolthatsurfacestheall-in
price eliminated most of the drip-pricing overcharge for
its users [5]. Two questions decide what that success
amounts to socially, and single-user evidence cannot an-
swer either. First, through which channel does the assis-
tant create value: by informing a consumer who would
nothaveread,orbyactingwheretheconsumerreadsand
stillfailstoact? Second,oncesellerswhosemarginslive
in contingent fees re-optimise against a partially assisted
population, where does the saving end up: with the as-
sisted, with the sellers, or extracted from the bystanders
who have no assistant?
Economic theory sharpens the second question into a
warning. In models of shrouded attributes, customers
who dodge a contingent fee are cross-subsidised by cus-
tomers who pay it, so any technology that makes avoid-
ance free for one segment pushes the competitive head-
line price up for everyone [6, 7]. Assistants would then
actasaregressivetransfer: adopterssave,sellersreprice,
bystandersfundthedifference. Thatprediction,however,
hinges on behavioural parameters the theory assumes
rather than observes, and on sellers who respond only
through prices when real sellers also choose disclosure
and obstruction.
We answer both questions inside a simulated market
smallenoughtoauditandrichenoughtobite(Figure1).
A language model (LLM) is first measured, cell by cell,
in the roles it will play: a renter living one errand-filled
day, andanassistantholdingeitheranadvisoryoranex-
ecuting mandate over a single digital act. The measured
agents then populate a rental market whose contract car-
ries a daily rate plus two contingent fees engineered for
identification: arefuellingfeethatonlytherenter’sphys-
ical action can avoid, and a pre-ticked add-on whose on-
linecancellationanassistantcanperform. Sixlanguage-
modelsellers,eachequippedwithanalgorithmicpricing
aid, adapt rates, fees, disclosure placement, and decline-
1
arXiv:2610.05823v1  [cs.MA]  5 Oct 2026

step obstruction. Handing an assistant to every second
person, holding a fixed panel of never-adopters aside,
and pairing every shocked path with its unshocked twin
under common random draws yields three audited quan-
tities: theadopters’outlaychange,thebystanders’outlay
change, and the sellers’ revenue recovery. Design, sam-
plesizes,andreadingruleswerelockedandfingerprinted
with no outcome yet in view.
The answers reorder the usual story. Value comes
from acting, not reading: the simulated consumer reads
the fine print on most days — hundreds of times field
readership — and still pays, while an assistant holding
a concrete, approved plan completes the cancellation al-
mostalways(advicenearlymatchesfulldelegation)and,
moremundanely,makessureacarissecuredatall. Sell-
ersdoreprice: theyrebuildabouthalfthelostfeestream
throughtheheadlineratewhileabandoningthefeesthem-
selves, leaving adopters 8.7 of the 13.7 USD per renter-
day they would keep under frozen sellers — about two-
thirds,ofwhichovertwo-fifthsiscompletedtransactions
rather than dodged charges. The feared bystander tax,
finally, fails to appear — thirty markets bound it within
about a dollar a day — and what would create it does
notbelongtotheassistantatall; itbelongstothesellers’
fee-setting: acrosssevenmarketconfigurationsspanning
two model families, agent-replacement hybrids, and a
controlled reassignment of fee-setting rights to the sell-
ers’ownpricingtool,thebystanderoutcomemovesfrom
burden to saving in step with the fee margin the market
carried when assistants arrived, resolved at the two ends
of that scale. Where selling is tool-priced, fees are thin,
vanishentirelyundertheshock,andeveryone—assisted
or not — buys at an all-in price.
Contributions.(1) A measurement-first pipeline in
which the same pre-registered estimands pass from an
analytical benchmark through a calibrated behavioural
markettoalanguage-modelsociety,sothatagreementis
informativeanddisagreementisattributable(Sections3–
6). (2) An acting-not-reading account of assistant value,
quantified down to its two components — fee avoid-
ance and task completion — of which only the first is
contestable by sellers (Sections 4, 6). (3) A conduct-
dependenceresultforthedistributionalquestion,includ-
ing a within-market institutional intervention: a con-
trolled transfer of fee-setting to the pricing tool, whose
announcementalonemakessellersadoptitpre-emptively
andemptiesthemarketoffees(Section7),withthepolicy
reading in Section 8.
2 Related work
Agentic consumers meeting adaptive sellers.The-
ory on AI-mediated purchase finds that cheaper search
can help buyers even after sellers respond, while better-
informed search can soften competition [8]; delegating
choicetoanLLMinsideastaticduopolytransferssurplus
betweendelegatorsandnon-delegatorsthroughauniform
price [9]; and simulated airline sellers earn drip revenue
only on the human remainder as booking bots spread
[10]. Reviews of the field flag dynamics and seller-side
instrument choice as the open front [11]. A cluster of
adjacent designs — delegation depth [12], autonomous
search [13], selling bots against buying bots [14, 15],
platform gatekeeping of comparison agents [16], collu-
sionunderconsumerAI[17],endogenoussophistication
[18],agentswiththeirownattentionfrictions[19]—and
the open agent marketplaces [20, 21] share our motiva-
tionbutnonecrossespartialadoptionwithafeethatonly
somecustomerscanescape. Onthesellerside,deployed
agents shade truth under incentive [22] and drift toward
profit framings unprompted [23]; assistant memory can
discipline platforms at full adoption [24]; long-horizon
agent economies are unstable [25, 26], which our short,
zero-sum-audited window avoids.
Contingent charges.The cross-subsidy logic we test
descends from add-on pricing [27], shrouding equilibria
[6], and contingent-charge contracts [7], with the sur-
vival of exploitative terms under competition [28, 29],
obfuscation as strategy [30, 31]. Empirically, banned
fees migrate into salient prices at most partially [32] —
our recovery benchmark — and shrouding moves de-
mand[33,34];mandatedall-inpricingshifts,ratherthan
destroys, fee revenue [35, 36]. The assistant-facing fric-
tionswemodelaredocumentedpractice: incumbentsuits
against buying agents [37], bot walls and CAPTCHAs
[38], and dark-pattern incidence benchmarks [39–42].
Simulating with language models.LLM agents re-
produce some economic behaviour [43–46] and miss
other parts — competitive convergence [47], pre-
registered treatment effects [48], outside options [49].
Weadopttheconstruct-validitydisciplineurgedforsuch
simulations [50]: measure the agent first, predict with
a transparent baseline, register the read, and report the
simulator’s own noise. Benchmarks of shopping-agent
behaviour [51, 52] anchor our assistant-side measure-
ments.
3 A market that fits in one day
This section walks the construction of Figure 1: the day,
thecontract,thethreeparties,andthedesign;thesupple-
ment lists every constant.
One renter-day.Each simulated person lives ten
hourly blocks between 08:00 and 18:00, holding four
fixedappointmentsandfiveorsixopenhours;eachopen
hourcan absorboneerrand worthabout8 USD.Errands
require the rental car, which must come back by 18:00.
A day on which no car gets secured falls back to taxis,
2

Figure 1: The simulation at a glance: (a) two hundred renters, half assisted at the shock, a fixed never-assisted panel
— the bystanders; (b) one day, the mandate’s reach, and the refuel window only the renter can use; (c) the contract’s
rate and two fees, each tied to who can escape it; (d) the sellers’ levers, from the pricing tool’s rate to obstruction or
the badge; (e) the paired branch design that turns differences into the three registered quantities.
billed at 120 USD. The renter carries a scratchpad of
bounded length, picks one action per open hour from a
menu of currently feasible moves, and is told nothing
else: no fee, no deadline, and no reminder ever appears
initsinstructions,soanyavoidanceitachievesisitsown.
Thecontract.Sixsellerslistadailyratenear70USD
against a marginal cost of 80 per rented day, recoup-
ing the gap through two contingent charges buried in a
twenty-clauseagreement. Arefuelling charge,cappedat
15 USD, falls due when the tank returns below seven-
eighths; escaping it requires the renter itself to spend an
open hour at the pump after its last drive — no software
can do this. Anadd-on bundle, capped at 12 USD, ar-
rives pre-ticked and bills automatically unless cancelled
ahead of a deadline stated deep in the agreement; the
cancellation itself is a two-minute online act. The pair is
the identification device: one charge reachable by dele-
gation, one not.
The assistant.Half the population, drawn once and
stratifiedonmeasuredreadingpropensity,receivesanas-
sistant — the identical model given a clean context and
authority over every seller’s small print. Holding only
theadvisorymandate it summarises, recommends, and
sets reminders, while the renter still clicks. Promoted
to theexecutingmandate, it additionally carries out the
cancellationitself,onceperrental,afteritsplanwinsthe
renter’s approval. It also books the renter’s lunch under
both mandates, so mandate contrasts isolate the cancel-
lation right. A tenth of the population is a permanently
unassisted panel — our bystanders — and the remainder
without assistants complete the demand side.
The sellers.Every period each seller’s LLM receives
its ledger and itspricing tool’srecommendation — a
best-response rate and fee schedule computed from the
seller’s own observed paying rates at the measured de-
mand elasticity — and chooses: both fee levels; where
each charge appears (listing card, numbered clause, or
appendix);whethertoobstructthecancellationpathwith
a phone-only requirement, a CAPTCHA, or a confirma-
tion maze; whether to qualify for a verified transparency
badge by listing both charges and obstructing nothing;
and a headline rate within ten percent of the tool’s quote
forthe chosenpackage. Sellersneverobserve whoholds
an assistant; a mishandled charge costs them an 8 USD
complaint. Obstruction is not free theatre: a phone-only
pathdefeatsassistedcancellationalmostsurely,andeach
obstacle carries a measured or declared failure probabil-
ity for renter and assistant alike.
Design and estimands.A market instance is burned
in for eight periods with no assistants, snapshotted, then
branched for twenty-four periods: an unshocked con-
tinuation, the two mandate shocks, and copies of each
with sellers frozen at the snapshot — six branches shar-
ing renters, days, and draws through common random
numbers, so differences are treatment, not luck. The fi-
nal eight periods supply the three registered quantities,
market by market, the market being the inference unit;
forty of the two hundred rent in any period, henceper
sampled renter-day. Prose quotes savings and burdens
as positive magnitudes; figures plot the signed outlay
change. Theadopters’ saving: spending per sampled
renter-dayamongwould-beadopters,shockedminusun-
3

Figure 2: Reading against acting in the role measurements: (a) shares of days or rentals on which the renter reads,
cancels in time, refuels, and ends carless — unassisted against both mandates, 95 % Wilson intervals, denominators
beneath each cell, the 0.1–1 % human readership band from field tracking [53]; (b) the executing chain’s leak points
and the split of timely cancellations between the assistant’s own click and the renter acting on its plan.
shocked, carless days entering at the taxi fallback. The
bystanders’ burden: the same difference for the fixed
panel. Thesellers’ recovery: revenue regained by adap-
tive sellers relative to frozen ones, as a fraction of the
fee revenue freezing shows they lost, split into a rate
part and a fee part. A twin unshocked run supplies the
simulator’sownreplicationnoise;anycontrastwhosein-
terval overlaps that scale is reported as unresolved, not
as a finding. Estimands, market counts, windows, and
these reading rules were frozen and fingerprinted ahead
ofthefirstbranchbeingopened; thepilot-stageinterface
repairs and each later addition carry dated amendments
in the released log.
4 Whyassistanceworks: measured,notas-
sumed
The renter reads the terms on 0.825 of days yet beats the
cancellationdeadlineononly0.36ofrentals: thatpairof
numbers, measured before any market ran, is the paper’s
first result. The role measurements behind it use accep-
tance bands set beforehand and thirty-to-forty-day cells,
each rate carrying its own denominator. Renters and as-
sistantsrunonQwen3.8-27Binfour-bitquantisationand
sellersonGemma-4-31B;asixteen-bitcheckreproduces
therentercellswithintheirintervals; noproprietaryAPI
touches any run, and prompts ship with the release.
Information is not the constraint.The simulated
renteropenssomebody’sfineprinton0.825ofreference
days—twotothreeordersofmagnitudeabovethe0.1–1
% of shoppers whom field tracking catches opening a
licence [53] — and its reading barely responds to work-
load. Acting is the constraint: at the reference fee its
cancellation beats the deadline on 0.36 of rentals (0.25
when little is at stake), and it refuels on 0.72 of the days
the tank rule binds. The screening gate we had regis-
tered treated heavy reading as disqualifying; the model
failedthatgateonbothfamilies,andweproceededunder
the registered fallback — the population isreaders who
under-execute, and every market claim is a claim about
that population. Its price sensitivity, a conditional-logit
scale of 0.84 USD from rate-dispersed listings, feeds the
sellers’ pricing aid, so seller beliefs match measured de-
mand by construction.
Acting is.Figure 2 shows the flip. Given the ex-
ecuting mandate, the assistant lifts timely cancellation
from 0.36 to 0.97; advice alone reaches 0.93, because
this renter, unlike its unassisted baseline, follows a con-
crete plan it has approved. The physical charge moves
the other way: refuelling on threatened days edges from
0.72downto0.67underexecution—delegatingthedig-
ital chore slightly crowds out the pump. And a channel
invisible to fee accounting appears: one in six unas-
sisted renter-days ends with no car secured at all, against
none with an assistant of either mandate. The mecha-
nism is mundane. An unassisted renter can burn its free
hours without ever finishing a booking, the more often
the higher the posted fees (0.07 carless at the low fee,
0.17 at the reference); the channel therefore mixes price
response with pure follow-through, and an assistant re-
stores the follow-through. Where the executing chain
leaks, it leaks at authority and initiative: the mandate
arrives on 0.90 of bookings, an attempt follows on two-
thirdsofgrants,thecancellationtoolsucceedingon0.94
of attempts. Only 0.57 of the timely cancellations are
4

the assistant’s own click; the rest are the renter carry-
ing out the plan it approved. Against seller obstruction
theasymmetrysharpens: aphone-onlycancellationpath
caps assisted timely success at 0.13, while the verified
transparency badge is worth near 2 USD to the assistant
and near 6.5 to the renter.
5 What repricing should do: benchmark
and calibrated forecast
Twotransparentlayers,runbeforethesocietyandfrozen
as its forecast, say what seller adaptation ought to look
like if the measurements are taken seriously.
A pencil-and-paper bound.In a zero-profit contract
with a contingent charge, the customers who pay it sub-
sidise the headline for those who dodge it [7]. Remove
the add-on stream from half the customer base and the
break-even headline must climb by the per-customer fee
margin times the adopting share — 5 USD here at half
adoption — while the charge stays profitable on who-
ever remains. That is the cross-subsidy warning in its
purest form: bystanders pay more, assisted or not. The
bound also announces its own fragility: at the measured
behaviour, a fee-free entrant already beats the incum-
bent contract before any assistant exists, so the fee-laden
configuration is a repricing baseline rather than a resting
point.
Amarketofthemeasuredparameters.Substituting
everymeasuredrateintodeterministicrenters,assistants,
and tool-following sellers — no language model in the
loop—andrunningtheidenticalbranchdesign120times
gives therule market, the calibrated forecast the society
isjudgedagainst. Itsadaptedstateisfee-lightanddearer
per day: under the executing shock the headline climbs
9.6 USD, adopters retain about two-fifths of a 13.8 USD
first-day saving, recovery lands at 0.66 of the lost fee
stream — the migration fraction observed after real fee
regulation [32] — and the bystander burden settles at
3.60±0.34 per renter-day. The forecast, frozen there,
will prove right in direction and high on pass-through.
Oneofitsingredientsdeservesemphasis: bystanderbur-
den flips sign when sellers’ pricing beliefs loosen, so
the forecast’s own sensitivity analysis already nominates
seller conduct, not assistant capability, as the decisive
unknown.
6 What the market did
Adopters keep about two-thirds, in two currencies.
ThirtymarketinstancesranthebranchdesignwithLLM
renters, assistants, and sellers — the ten registered up
front, then twenty more under a replication protocol de-
clared before launch, pooled here as that protocol fixed
andreadoncebytheregisteredscript(Figure3,Table1).
Onthefirstshockedday,would-beadoptersspend13.3±
1.5 USD per renter-day less than their unshocked selves;
bythefinaleightperiods,8.7±1.4ofitremains—66%,
wheretherulemarketforecasttwo-fifths. Anaccounting
identity — outlay equals the carless share times the taxi
cost plus the rest times the bill — splits the surviving
saving into 5.0 USD through a cheaper bill and 3.7 USD
throughcarssecured,ascarlessdayscollapsefrom0.148
to0.002ofadopterrenter-days. Onlythecheaper-billpart
is fee arbitrage; the cars-secured part is follow-through,
and the seller responses below barely reach it.
Sellers rebuild half the lost fees through the rate
while abandoning the instrument.Freezing sellers
shows the shock costs them 4.3 USD of fee revenue per
rental;adaptivesellersregain0.55±0.31ofit,allthrough
a headline rate 4.4±1.8 USD higher (rate component
1.20,feecomponent−0.65),underboththeforecast0.66
and the migration fraction real fee regulation produced.
The instrument itself is dying where it is being repriced:
both posted fees fall, one seller-period in five goes fee-
free against almost none unshocked, and theunassisted
get billed the add-on on 30 points fewer rentals — a fee
a seller stops charging stops being charged to everyone.
Transparency, for its part, belongs to the reading popu-
lation rather than to the shock: 5.6 of six sellers hold
the badge, a third of a seller obstructs, and prices keep
cycling at 2.1 USD per period into the final window, an
adaptation transient honestly averaged, not an equilib-
rium.
Bystanders: no detectable burden.Under the exe-
cuting shock the fixed panel’s spending shifts by +0.38
±0.94 USD per renter-day over the thirty markets —
zero inside the interval, the whole effect bounded within
about±1.3 on a 100 USD daily outlay, and +0.13±0.73
overthewholehorizon. Thedeclaredprotocolreportsits
threecutssidebyside: theregisteredtenaloneread+1.71
±1.61, the twenty replication markets−0.28±1.14, the
poolasabove;thetwin-runnoisescaleofasinglemarket,
2.6 USD, dwarfs all three. The replication also answers
theregisteredten’soneoddity—theirfiveviabilityflags
andstrongerrepricing: alltwentynewmarketsareviable,
theirsellersrepriceless(rate+3.1±2.2,recovery0.33±
0.43), and the pooled society accordingly sitsbelowthe
rule-market forecast on pass-through while its adopters
keep more. With thirty markets the society’s precision
separates it from its forecast: the bystander, rate, and
adopter intervals now exclude the rule market’s means
while recovery covers — the deterministic layer called
thedirectionofeveryresponseandoverstatedhowmuch
of it sellers complete. The advisory mandate, run on the
registered ten, tells the stronger-for-adopters story there
(−8.1±3.1 against the chain’s−4.2) with the same null
bystander reading.
5

Figure 3: The shock’s three audiences over thirty markets, small dots one market each, filled marks executing and
hollow advisory (advisory arms exist on the registered ten): (a) adopters on day one and adapted, with the adapted
saving split into the cheaper bill and cars secured; (b) the sellers’ side, rate change beside the recovery of the lost fees;
(c)bystandersagainsttherule-marketforecast. Thegreybandisthetwin-runscaleofasingleunchangedmarket,three
pairs, printed for calibration only.
Table 1: Rule-market forecast against society outcome,
executingmandate,finaleightperiods;USDpersampled
renter-day except rows marked as shares or ratios. So-
ciety: thirty pooled markets (the registered ten and the
twenty-market replication are reported separately in the
text; advisory column in the released materials).
registered quantity forecast outcome (30) twin-run noise
adopters’ saving, first day 13.8±0.4 13.3±1.5 —
adopters’ saving, adapted 5.6±0.3 8.7±1.4 1.8
... of it through cars se-
cured (share)
— 0.43 —
bystanders’ burden, adapted 3.60±0.34 0.38±0.94 2.6
headline rate rise 9.6±0.3 4.4±1.8 2.5
sellers’ recovery of lost fees
(ratio)
0.66±0.03 0.55±0.31 —
... through rate / through
fees (ratio)
0.81 /−0.15 1.20 /−0.65 —
adopters’ add-on billed less
often (share of rentals)
0.99 0.74±0.03 —
fee-freeseller-periodsunder
the shock (share)
— 0.19 —
7 Seller conduct decides who pays
The society’s null bystander reading could mean assis-
tantsarebenign, orcouldmeanthismarkethadlittleleft
to extract. Seven configurations separate the two: re-
runs of the same environment varying which tier is an
LLM, which model family plays it, and who controls
fees. Figure 4 aligns them on one axis — the fee margin
at stake, measured as what the fixed panel pays in fees
per renter-day in each configuration’s unshocked state.
The margin orders the outcome, and the margin
is conduct’s footprint.At the fee-heavy end, the rule
market (12.7 USD at stake) taxes bystanders a resolved
3.6, and LLM sellers facing non-reading deterministic
renters(14.6atstake)taxthem5.6whileobstructinghalf
thestorefronts. Atthefee-lightend, threeconfigurations
whose sellers hew to the pricing tool — a second model
familyineveryrole,aswapofthesellermodelalone,and
thesocietyundertransferredfeeauthority—carry2to6
USD at stake, answer the shock with little or no rate rise
(−0.7 to +3.5), and show bystanderssaving:−4.7±2.0,
−2.7±6.2,−2.6±4.6. Only the two ends are resolved
— the rule market’s burden, the second family’s saving
— and the rest carry intervals through zero; adopters’
saving thins with the margin, its completed-transactions
component the slower-moving part. Across the seven
configurations the association is near-monotone (Spear-
man about 0.9), a descriptive synthesis across designed
variants, pattern rather than test. Conduct also acts be-
yondthe margin. At thesame12.7 atstake, thesociety’s
sellers — who take the tool’s fee advice on a quarter
of their choices — pass through a tenth of what the fully
strategicrulemarketdoes(+0.4against+3.6). Andwhere
deterministic tool-followers meet reading LLM renters,
half the fees are gone before any assistant arrives; the
6

Figure 4: Seven configurations on one axis — the fee margin at stake, the fees the fixed panel pays unshocked: (a)
the bystander outcome crosses from burden to saving as the margin thins, resolved at the ends; the dashed ring is the
six-market baseline of the fee-authority arm and the arrow its within-market shift, fee-free seller-periods roughly 0.2
to 0.9; (b) the adopters’ saving, positive up, thins as the margin does. Final eight periods; intervals on both axes.
residual burden (+1.3±5.2) is already indistinguishable
from zero.
The seller model carries its conduct.Family com-
parisonsbraidthreechangestogether. Onearmtherefore
changesthesellermodelalone: samerenters,sameassis-
tants,sameseeds,sellersswappedfromthefee-defending
family to the tool-following one. The swapped market
reproduces the second family wholesale — 87 % fee-
free seller-periods, universal badges, zero obstruction,
flatrates—establishingthatfeeconducttravelswiththe
seller model, not with the population it faces.
Announcing tool-set fees empties the market.The
sharpestprobetransfersfee-settingtothepricingtoolin-
side six of the society’s own markets, everything else
pinned. Sellers are told the tool’s fee schedule will
be executed; their LLMs keep presentation, obstruction,
badges,andboundedratediscretion. Sellersdonotresist;
they anticipate, proposing the tool’s own schedule on 99
%ofseller-periods,andfee-freeseller-periodsjumpfrom
0.19 to 0.89 of the total. Read as the announced institu-
tion it is, window by window. Over the whole horizon
adopters’savinghalves: 10.4fallingto5.1perrenter-day,
a 5.3±4.2 USD drop with every one of the six markets
positive; the registered final window puts the drop at 2.8
±5.0. About 29 % of the whole-horizon change flows
through the cars-secured channel, because fee-free sell-
ersrescuemarginalunshockedrentalstoo,trimmingeven
thefollow-throughslice. Bystanders’whole-horizoncell
goes−0.7 to−3.0 (a−2.3±4.3 change) and the final-
windowcell+0.8to−2.6(−3.4±6.6): thetool-following
direction, both spans crossing zero, the latter leaning on
one market. The institutional claim therefore stays with
Table 2: The fee-authority transfer over six paired mar-
kets,inUSDforeachsampledrenter-day,splitbywindow
(per-market detail in the released materials).
quantity·window sellers set fees tool sets fees change
unshocked renters’ outlay·
whole
101.3 99.8−1.5
assisted renters’ outlay·
whole
90.9 94.7 +3.8
adopters’ saving·whole 10.4 5.1−5.3±4.2
adopters’saving·finaleight 7.5 4.7−2.8±5.0
bystanders’ burden·whole−0.7−3.0−2.3±4.3
bystanders’ burden·final
eight
+0.8−2.6−3.4±6.6
fee-free seller-periods
(share)·shock
0.19 0.89 +0.70
the resolved cells. Fees vanish, the contestable half of
assistantvaluevanisheswiththem,andnothingindicates
bystanders are hurt in the process.
8 What it means
For the junk-fee debate.Regulators pursue all-in pric-
ing by rule [35, 54]; in this market something close to it
emergedfromautomationonbothsidesofthecounter—
an outcome of these simulations, offered as a hypothesis
about real markets rather than a conclusion. Executing
assistantsoperateasdecentralisedenforcement,sinceev-
ery cancellation they complete taxes the shrouding strat-
egy. Tool-driven fee-setting on the seller side finishes
the job: a pricing tool computing on observed paying
rates simply stops recommending a charge its market
7

has learned to dodge. The convergence point, reached
here without a statute, is a dearer honest headline and
no contingent charges: the CARD-Act pattern of partial
fee-to-ratemigration[32],runtocompletion. Theequity
objectiontoconsumerAI—thatitpricestheunprotected
out — appears in our data only where fee margins are
thick and defended. In the society it is smaller than the
simulator’sownnoise,anditinvertswheresellingistool-
priced. What deserves the regulatory eye instead is the
cancellation step. A phone-only requirement neutralises
assistance almost completely in our measurements; ob-
struction of agents, already visible in the field [37, 38],
is the one seller instrument that re-segments a market
assistants would otherwise clean.
Fortheassistantbusiness.Halfofthevaluethatsur-
vivesrepricinghereisfeearbitrage(ondayone,closerto
three-quarters), and that share is self-liquidating: sellers
reprice it away for adopters, and competition or institu-
tions erase it for everyone. The part that persisted in
every configuration we ran is follow-through — the as-
sistantcompletesthetransactionitsprincipalfumbles—
worth 3.75±0.64 USD per renter-day within the soci-
ety, and dented only where fee-free selling rescues the
unshocked side’s rentals as well. Products sold on fee
savings price their own obsolescence; products built on
execution reliability sell what the market left standing.
Validity,honestly.Wefollowtheguardrailsliterature
for LLM simulations [50]: agents measured before de-
ployment, forecasts frozen before outcomes, estimands
and rules hashed in advance, the simulator’s replication
noise printed beside every primary contrast. Conver-
gencegetsreported,neverpresumed[47]. Theregistered
screeninggatefailed—themodelreadstoomuch—and
weproceededundertheregisteredfallback. Externalva-
lidity is therefore explicitly conditional: this is a market
of tireless readers who under-execute, one plausible cor-
ner of the coming assisted economy, not a calibrated
portrait of human renters. Seller conduct findings are
configurationcontrastsoverahandfulofmodelfamilies;
the margin-burden alignment of Figure 4 is descriptive;
thefee-authoritytransferidentifiesanannouncedinstitu-
tion,notaconcealedcounterfactual;andatwenty-market
replication of the society, registered before launch, was
still running at submission with its analysis frozen. The
carless-daychannelearnsitsowncaution: itisanLLM’s
follow-through failure priced at the taxi fallback, and
thoughitrespondstofeesashumannon-bookingwould,
its level need not transfer to people.
The sentence to keep.Assistants help because they
act; markets answer by folding fees into honest prices;
who funds the transition is written in the sellers’ fee
ledger, not in the assistant’s code. And whenever either
side automated the fee decision here, the fees, the bur-
den,andthearbitrageshranktogether,leavingcompleted
transactions as the value still standing.
References
[1] Meta Platforms, Inc. Introducing Muse: The
world’s first personal AI agent built for every-
one. Meta Newsroom, 8 September 2026, 2026.
URLhttps://about.fb.com/news/2026/09/
introducing-muse-personal-ai-agent/.
[2] AlexandraE.MichaelandFranziskaRoesner. How
agentsaskforpermission: UserpermissionsforAI
agents,frominterfacestoenforcement,2026. URL
https://arxiv.org/abs/2607.13718.
[3] Kwansoo Kim and Byungjoon Yoo. Delega-
tion, tipping, and light-touch control in con-
sumer AI agents: A regime-switching theory of
misalignment. SSRN Working Paper 6909242,
2026. URLhttps://papers.ssrn.com/sol3/
papers.cfm?abstract_id=6909242.
[4] Se Yan, Han Zhong, Zemin Zhong, and Wenyu
Zhou. ShoppingwithaplatformAIassistant: Who
adopts, when in the journey, and what for, 2026.
[5] BenjaminLu,DanielMarkovits,AndrewC.Miller,
and Rory Van Loo. Measuring and mitigating
drip pricing overcharge: Evidence from an on-
line marketplace experiment with a digital shop-
ping assistant. SSRN Working Paper 5565238,
2025. URLhttps://papers.ssrn.com/sol3/
papers.cfm?abstract_id=5565238.
[6] Xavier Gabaix and David Laibson. Shrouded at-
tributes, consumer myopia, and information sup-
pression in competitive markets.Quarterly Jour-
nal of Economics, 121(2):505–540, 2006. doi:
10.1162/qjec.2006.121.2.505.
[7] Mark Armstrong and John Vickers. Consumer
protection and contingent charges.Journal of
Economic Literature, 50(2):477–493, 2012. doi:
10.1257/jel.50.2.477.
[8] Brendan Lucier, Nicole Immorlica, Markus Mo-
bius, Aleksandrs Slivkins, Daniel G. Goldstein,
Jake M. Hofman, Sonia Jaffe, and David M. Roth-
schild. Agentic markets: Equilibrium effects of
improving consumer search, 2026. URLhttps:
//arxiv.org/abs/2603.25893.
[9] Yann Delaprez and Ali Hortaçsu. The wel-
fare impact of delegating choice to large lan-
guage models. SSRN Working Paper 6631180,
2026. URLhttps://papers.ssrn.com/sol3/
papers.cfm?abstract_id=6631180.
8

[10] Khaled Abdelghany and Ahmed Abdelghany.
AgenticAIandairlinepricing: Demandcliffs,elas-
ticity migration, and the fate of fare fencing under
delegatedbooking. SSRNWorkingPaper7372267,
2026. URLhttps://papers.ssrn.com/sol3/
papers.cfm?abstract_id=7372267.
[11] David M. Rothschild, Nicole Immorlica, Brendan
Lucier, Markus Mobius, and Aleksandrs Slivkins.
The evolution of digital search: From blue links
to delegated decision-making, 2026. URLhttps:
//arxiv.org/abs/2607.21459.
[12] Ihsaan Basharat Want. When consumers del-
egate choice to AI: Strategic adaptation and
information asymmetry in agentic markets.
SSRN Working Paper 7282860, 2026. URL
https://papers.ssrn.com/sol3/papers.
cfm?abstract_id=7282860.
[13] LingxiuDong,KaiwenLuo,andFashengXu. From
product search to preference articulation: The eco-
nomics of agentic commerce, 2026. URLhttps:
//arxiv.org/abs/2608.08395.
[14] Chupeng Xie. When pricing agents meet buying
agents: Personalized pricing and verifiable trust,
2026. URLhttps://arxiv.org/abs/2607.
16343.
[15] Mingyang Fu and Ming Hu. Strategic buying
agents, 2026. URLhttps://arxiv.org/abs/
2607.04708.
[16] Rui Chen, Xianghua Gan, Taojie Qin, and
Xiaohang Yue. Open or restrict? plat-
form governance of AI-assisted comparison.
SSRN Working Paper 7033679, 2026. URL
https://papers.ssrn.com/sol3/papers.
cfm?abstract_id=7033679.
[17] Xiang Cheng and Manmohan Aseri. Break-
ing AI collusion with consumer AI. SSRN
Working Paper 6839464, 2026. URL
https://papers.ssrn.com/sol3/papers.
cfm?abstract_id=6839464.
[18] Benjamin Balzer and Benjamin Young. The depth
and reach of exploitation: Contracting with en-
dogenously naive consumers, 2026. URLhttps:
//arxiv.org/abs/2609.25509.
[19] Martin Bichler. Agentic markets.Elec-
tronic Markets, 36(1):55, 2026. doi: 10.1007/
s12525-026-00906-y.
[20] Seth Karten, Cameron Crow, and Chi Jin. Agent
bazaar: Enabling economic alignment in multi-
agent marketplaces, 2026. URLhttps://arxiv.
org/abs/2605.17698.
[21] GaganBansal,WenyueHua,ZezhouHuang,Adam
Fourney,AmandaSwearngin,WillEpperson,Tyler
Payne,JakeM.Hofman,BrendanLucier,Chinmay
Singh, Markus Mobius, Akshay Nambi, Archana
Yadav, Kevin Gao, David M. Rothschild, Aleksan-
drs Slivkins, Daniel G. Goldstein, Hussein Mozan-
nar, Nicole Immorlica, Maya Murad, Matthew Vo-
gel, Subbarao Kambhampati, Eric Horvitz, and
Saleema Amershi. Magentic marketplace: An
open-sourceenvironmentforstudyingagenticmar-
kets, 2025. URLhttps://arxiv.org/abs/
2510.25779.
[22] ZheyuanLiu,WeiliangZhao,XiangchiYuan,Ning-
shanMa,YueHuang,andMengJiang. Knowledge-
verified emergent deception in LLM agents un-
der conflicting incentives, 2026. URLhttps:
//arxiv.org/abs/2608.26372.
[23] Eric So. The profit alignment problem: How profit
mandatesinducealignmentfailuresinLLMs,2026.
URLhttps://arxiv.org/abs/2609.07731.
[24] Deyao Hong, Kehan Zheng, Qian Li, Jun Zhang,
Jie Jiang, and Hongning Wang. The user asks,
platforms compete: How agentic recommendation
markets take shape, 2026. URLhttps://arxiv.
org/abs/2607.25253.
[25] Sajal Regmi, Siddhartha Pudasaini, and
Chetan Phakami Pun. But how would AI
agents run a town’s economy?, 2026. URL
https://arxiv.org/abs/2609.11108.
[26] Zeyuan Li, Lukas Petersson, Alessandro Acquisti,
andMichielA.Bakker. Emergentmisalignedcom-
municationinlong-horizonmulti-agentLLMcom-
merce, 2026. URLhttps://arxiv.org/abs/
2608.14825.
[27] Glenn Ellison. A model of add-on pricing.Quar-
terly Journal of Economics,120(2):585–637,2005.
doi: 10.1093/qje/120.2.585.
[28] Paul Heidhues, Botond Kőszegi, and Takeshi
Murooka. Exploitative innovation.American Eco-
nomic Journal: Microeconomics, 8(1):1–23, 2016.
doi: 10.1257/mic.20140138.
[29] Paul Heidhues, Botond Kőszegi, and Takeshi
Murooka. Inferior products and profitable decep-
tion.Review of Economic Studies, 84(1):323–356,
2017. doi: 10.1093/restud/rdw037.
9

[30] RanSpiegler. Competitionoveragentswithbound-
edly rational expectations.Theoretical Economics,
1(2):207–231, 2006.
[31] Ran Spiegler. Choice complexity and mar-
ket competition.Annual Review of Eco-
nomics, 8:1–25, 2016. doi: 10.1146/
annurev-economics-070615-115216.
[32] Sumit Agarwal, Souphala Chomsisengphet, Neale
Mahoney, and Johannes Stroebel. Regulating con-
sumer financial products: Evidence from credit
cards.Quarterly Journal of Economics, 130(1):
111–164, 2015. doi: 10.1093/qje/qju037.
[33] Jennifer Brown, Tanjim Hossain, and John Mor-
gan. Shrouded attributes and information suppres-
sion: Evidence from the field.Quarterly Jour-
nal of Economics, 125(2):859–876, 2010. doi:
10.1162/qjec.2010.125.2.859.
[34] Tom Blake, Sarah Moshary, Kane Sweeney, and
Steve Tadelis. Price salience and product choice.
Marketing Science, 40(4):619–636, 2021. doi: 10.
1287/mksc.2020.1261.
[35] Jiwon Yang. Regulating drip pricing in plat-
form markets: Consumer behavioral responses
and host strategic adaptation under California’s
SB 478. SSRN Working Paper 7203424,
2026. URLhttps://papers.ssrn.com/sol3/
papers.cfm?abstract_id=7203424.
[36] Ginger Zhe Jin, Liad Wagman, and Jingyi
Xing. Clearing the fog: Price transparency,
market churn, and consumer welfare in short-
term rentals. SSRN Working Paper 7290239,
2026. URLhttps://papers.ssrn.com/sol3/
papers.cfm?abstract_id=7290239.
[37] Rory Van Loo. Consumer agents.Wash-
ington University Law Review, 103(3):705,
2026. URLhttps://wustllawreview.org/
2026/02/25/consumer-agents/.
[38] Eranga Bandara, Ross Gore, Ravi Mukka-
mala, Asanga Gunaratna, Safdar H. Bouk,
Xueping Liang, Peter Foytik, Abdul Rahman, Sa-
chini Rajapakse, Isurunima Kularathna, Pramoda
Karunarathna, Chalani Rajapakse, Ng Wee Keong,
KasunDeZoysa,TharakaHewa,AminHass,Wath-
salaHerath,ArunaWithanage,NilaanLoganathan,
Atmaram Yarlagadda, and Sachin Shetty. Towards
an agent-first web: Redesigning the web for AI
agents, 2026. URLhttps://arxiv.org/abs/
2606.19116.
[39] Devin Ersoy, Brandon Lee, Ananth Shreekumar,
Arjun Arunasalam, Muhammad Ibrahim, Anto-
nio Bianchi, and Z. Berkay Celik. Investigating
the impact of dark patterns on LLM-based web
agents, 2025. URLhttps://arxiv.org/abs/
2510.18113.
[40] Jingyu Tang, Chaoran Chen, Jiawen Li, Zhip-
ing Zhang, Bingcan Guo, Ibrahim Khalilov, Sim-
ret Araya Gebreegziabher, Bingsheng Yao, Dakuo
Wang,YanfangYe,TianshiLi,ZiangXiao,Yaxing
Yao, and Toby Jia-Jun Li. Dark patterns meet GUI
agents: LLM agent susceptibility to manipulative
interfaces and the role of human oversight, 2025.
URLhttps://arxiv.org/abs/2509.10723.
[41] Zijing Shi, Meng Fang, and Ling Chen. Bench-
marking web agent safety under e-commerce de-
ceptive interfaces, 2026. URLhttps://arxiv.
org/abs/2606.13686.
[42] Behzad Ousat, Nikita Turkmen, Lalchandra Ram-
persaud, Dillan Bailey, and Amin Kharraz. Broken
gates: Re-evaluatingwebbotdefensesintheageof
LLM agents, 2026. URLhttps://arxiv.org/
abs/2607.18659.
[43] John J. Horton, Apostolos Filippas, and Ben-
jamin S. Manning. Large language models as sim-
ulated economic agents: What can we learn from
homo silicus? NBER Working Paper 31122, Na-
tional Bureau of Economic Research, April 2023.
[44] Lisa P. Argyle, Ethan C. Busby, Nancy Fulda,
Joshua R. Gubler, Christopher Rytting, and David
Wingate. Out of one, many: Using language mod-
els to simulate human samples.Political Analysis,
31(3):337–351, 2023. doi: 10.1017/pan.2023.2.
[45] Gati V. Aher, Rosa I. Arriaga, and Adam Tau-
man Kalai. Using large language models to
simulate multiple humans and replicate human
subject studies. InProceedings of the 40th
International Conference on Machine Learn-
ing (ICML), volume 202 ofProceedings of
Machine Learning Research, pages 337–371.
PMLR, 2023. URLhttps://proceedings.
mlr.press/v202/aher23a.html.
[46] Joon Sung Park, Joseph C. O’Brien, Carrie Jun
Cai, Meredith Ringel Morris, Percy Liang, and
Michael S. Bernstein. Generative agents: Interac-
tivesimulacraofhumanbehavior.InProceedings of
the 36th Annual ACM Symposium on User Interface
Software and Technology (UIST ’23), pages 1–22.
ACM, 2023. doi: 10.1145/3586183.3606763.
10

[47] Pawel Struski, Jakub Swistak, Inez Okulska, and
Przemyslaw Biecek. Competitive market behavior
ofLLMs,2026. URLhttps://arxiv.org/abs/
2609.02580.
[48] Yi-Lin Tsai and Yung-Hsiu Lai. Seeing is not per-
ceiving: When synthetic consumers can and can-
not pretest visual marketing, 2026. URLhttps:
//arxiv.org/abs/2609.25677.
[49] LiangChen. Simulatedcustomersneverwalkaway:
DecisionfidelityofLLMusersimulatorsmeasured
againstrealpurchaseoutcomes,2026.URLhttps:
//arxiv.org/abs/2606.20708.
[50] Peiying Zhu and Sidi Chang. When guardrails
look effective: Construct validity failures in LLM
agent commerce evaluation, 2026. URLhttps:
//arxiv.org/abs/2609.01519.
[51] Davood Wadi and Yu Ma. Does rank still mat-
ter? position bias when AI agents shop on our
behalf, 2026. URLhttps://arxiv.org/abs/
2608.22697.
[52] Davood Wadi and Yu Ma. Shopping by algo-
rithm: How agentic AI deploys human heuris-
tics as a surrogate consumer, 2026. URLhttps:
//arxiv.org/abs/2609.28372.
[53] Yannis Bakos, Florencia Marotta-Wurgler, and
David R. Trossen. Does anyone read the fine
print? Consumer attention to standard-form con-
tracts.Journal of Legal Studies, 43(1):1–35, 2014.
doi: 10.1086/674424.
[54] Federal Trade Commission. Trade regulation rule
onunfairordeceptivefees. Finalrule,16CFRPart
464, 90 Fed. Reg. 2066–2167 (January 10, 2025);
effectiveMay12,2025;FRdocument2024-30293,
2025. URLhttps://www.federalregister.
gov/documents/2025/01/10/2024-30293/
trade-regulation-rule-on-unfair-or-deceptive-fees.
11
