---
title: 'When Shippers Become Algorithms: Candidate Exposure, Information Design, and the Concentration
  of LLM-Mediated Freight Markets'
url: https://arxiv.org/abs/2607.19967
category: digital-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Takahiro Ezaki
- Naoto Imura
- Katsuhiro Nishinari
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.19967
pages: 18
chars: 74972
fetched_at: '2026-11-08T13:06:07+00:00'
kb_version: 1
---

# When Shippers Become Algorithms: Candidate Exposure, Information Design, and the Concentration of LLM-Mediated Freight Markets

Highlights
When Shippers Become Algorithms: Candidate Exposure, Information Design, and the
Concentration of LLM-Mediated Freight Markets
Takahiro Ezaki, Naoto Imura, Katsuhiro Nishinari
•First simulation of freight procurement by populations of real LLM agents with endogenous capacity, pricing,
and ratings.
•Choices concentrate on one carrier on day one; capacity limits and congestion pricing then spread demand and
give unrated entrants work.
•Concentration rises steeply once each shipper’s randomly drawn candidate list exceeds about ten carriers; the
onset depends on which LLM the shippers use.
•Final market structure varies widely across sampled markets under every trust signal tested; displaying true
quality does not reduce this variability.
•Disclosing carriers’ remaining capacity lowers concentration and raises shipper surplus; diversification and list
shuffling do not.
arXiv:2607.19967v1  [physics.soc-ph]  22 Jul 2026

When Shippers Become Algorithms: Candidate Exposure,
Information Design, and the Concentration of LLM-Mediated
Freight Markets
Takahiro Ezakia,∗, Naoto Imuraa and Katsuhiro Nishinaria,b
aResearch Center for Advanced Science and Technology, The University of Tokyo, 4-6-1 Komaba, Meguro-ku, Tokyo, 153-8904, Japan
bDepartment of Aeronautics and Astronautics, School of Engineering, The University of Tokyo, 7-3-1 Hongo, Bunkyo-ku, Tokyo, 113-8656, Japan
ARTICLE INFO
Keywords:
Digital freight matching
Large language models
Algorithmic monoculture
Platform information design
Market concentration
Agent-based simulation
ABSTRACT
Shippers are beginning to delegate carrier selection to large language model (LLM) agents.
We ask what such delegation does to a freight matching market, and which platform design
choices contain it. We carried out agent-based simulations in which fifty shipper agents, built
on commercial LLMs from OpenAI (GPT), Anthropic (Claude), and Google (Gemini), procure
truckload capacity for thirty days. The market implements the rules of digital freight matching:
eachloadisoffereddowntheshipper’srankedlistofcarriers(waterfalltendering),carriershave
daily capacity limits, spot prices respond to congestion, and carrier ratings accumulate with
transactions. We found three risks and one remedy that works. Agents converged at once: for
a fixed sampled carrier population, the same carrier was the modal first choice of every model
on day one, attracting up to76%of requests. Because each agent picks from its own randomly
drawn list of displayed candidates, the platform controls how many options each shipper sees;
concentration rose steeply once lists exceeded about ten carriers, with the onset differing across
models. Which carriers ended up dominant varied widely from one sampled market to another,
and displaying true quality instead of estimated ratings changed neither the level nor this
variability (by design, quality affects only what agents see, never delivery outcomes). Against
these risks, disclosing each carrier’s remaining daily capacity cut concentration by a third and
doubled shipper surplus, while vendor diversification, list-order randomization, and popularity
displayshowednoclearlydetectableeffect.Platforminformationdesign,aheadofmodelchoice
or model regulation, is the lever that works.
1. Introduction
Freight procurement is becoming a task that firms delegate to machines. Large language models (LLMs) already
sit inside supply chain workflows, where they analyze contracts, screen suppliers, and forecast demand (Wang, Jiang,
Hong and Jiang, 2025; Song, Xie, Yang and Zhao, 2026; Nie, He, Mei, Qin, Li, Sun and Ma, 2025), and prototype
multi-agent systems automate vendor scoring and selection end to end (Joshi, Singh, Parashar and Singh, 2026); the
firstcommercialfreight-procurementagentsthatautomatecarriersourcingwereannouncedin2026(project44,2026).
Digitalfreightmatching(DFM)platformssuchasUberFreightandFullTruckAlliancehaveusedalgorithmstoprice
loadsandrecommendcarriersforadecade.Thestepnowunderwayisdifferentinkind.Shippersarehandingthechoice
of carrier itself to autonomous agents that read a list of candidates and pick one. When thousands of shippers choose
through a handful of foundation models, the matching process inherits whatever preferences those models share.
They share a great deal. On the first simulated day of the experiments reported below, with the carrier population
held fixed, GPT agents sent34to38of50requests to the same carrier out of twenty, and they did so under each
of the three information conditions we study (a list showing quoted prices together with true reliability scores, with
frozen ratings, or with live customer ratings); Claude and Gemini agents made that carrier their most frequent first
choice as well. Which carrier plays this role depends on the sampled population, not on the model (Section 5.1).
This isalgorithmic monoculture(Kleinberg and Raghavan, 2021; Peng and Garg, 2024) materialized in a market.
Independently deployed systems have been shown to hand the same individuals the same outcomes (Bommasani,
Creel, Kumar, Jurafsky and Liang, 2022), and LLM populations converge on collective conventions (Ashery, Aiello
∗Corresponding author.
tkezaki@g.ecc.u-tokyo.ac.jp(T. Ezaki)
ORCID(s):0000-0003-4175-3028(T. Ezaki);0000-0002-1428-7407(N. Imura);0000-0003-3069-1757(K. Nishinari)
T. Ezaki et al.:Preprint submitted to ElsevierPage 1 of 17

When Shippers Become Algorithms
andBaronchelli,2025).Inamatchingmarketwithcapacityconstraints,thiscreatesanimmediateoperationalproblem:
a carrier chosen by everyone cannot serve everyone’s demand, so most of that demand has to go somewhere else.
Existingmonocultureresultsarestatic.Theystudyone-shotallocationandabstractfromthefeedbackthatmarkets
supply. Carriers raise prices where demand piles up; capacity limits push displaced shippers onto second choices;
ratingsaccumulateforwhoevergetschosenandstayabsentforwhoeverdoesnot.Researchonhumanmarketsdescribes
howsuchfeedbackcangoeitherway.Herdingmodelsshowthatobservationalandreputationalsignalscanlockmarkets
into inefficient, path-dependent outcomes (Banerjee, 1992; Bikhchandani, Hirshleifer and Welch, 1992; Smith and
Sørensen, 2000), and the MusicLab experiment showed that social signals raise both inequality and unpredictability
of success (Salganik, Dodds and Watts, 2006), with rating-system field experiments finding related herding effects
(Muchnik, Aral and Taylor, 2013). Studies of platform reputation show that ratings inform but also inflate and lag
(Tadelis, 2016; Filippas, Horton and Golden, 2022), and that entrants without a track record face cold-start exclusion
(Pallais, 2014). No study yet follows LLM choosers, whose biases are documented and correlated, through a market
whoseprices,capacities,andratingsrespondtotheirchoices.WorkonLLMagentsinmarketshasshownthatpricing
agentscolludewithoutbeinginstructedto(Fish,GonczarowskiandShorrer,2024)andhasestablishedLLMsasusable
simulated economic agents (Filippas, Horton and Manning, 2024). The matching side, where monoculture should
matter most, remains open.
Freightistherightindustryforthisquestion,fortworeasons.First,truckloadprocurementalreadyhaswell-defined
rulesthatmaketheproblemconcreteandmeasurable.Shipperskeeprankedcarrierlists(routingguides)andoffereach
load down the list (waterfall tendering); carriers reject loads when they run out of capacity; and spot prices carry a
persistent premium over contract rates (Acocella and Caplice, 2023; Acocella, Caplice and Sheffi, 2020). Second, the
tension our agents exhibit, loyalty to incumbent carriers versus opportunistic spot search, is the central empirical fact
ofthisindustryforhumanshippers(HarrisandNguyen,2025b,a).Outcomesinthissettingcarrymanagerialmeaning:
service rates, freight rates, shipper surplus, and carrier revenue concentration, rather than abstract network statistics.
Recentworkquantifiestheinformationvalueoffreightplatforms(Wu,HuangandChen,2024).Weextendthatagenda
to the case where the platform’s users are themselves algorithms.
We build a simulation platform in which real LLM agents procure freight inside a market with endogenous
economics.Fiftyshipperagents,poweredbycommercialmodelsfromOpenAI,Anthropic,andGoogle,chooseamong
twenty carriers every day for thirty days. The market implements waterfall tendering over ranked preferences (each
load goes to the agent’s first choice if that carrier has capacity left, otherwise to the second, then the third), a fixed
daily capacity limit for each carrier, spot prices that adjust daily to excess-demand pressure, and a rating system in
which a carrier’s displayed score aggregates the reviews of its completed shipments. A carrier that no one chooses
accumulatesnoreviews.Wemanipulatethreelevers,eachundertheplatform’scontrol:theexposure𝐿,thenumberof
candidate carriers an agent can choose from (𝐿∈ {3,5,10,15,20}); theinformation structureof the trust signal (the
truereliabilitydiscloseddirectly,aratingfrozenatitsinitialvaluesothatitneverupdates,orthelivecustomerrating);
anddisclosure interventions, including real-time capacity visibility, list-order randomization, and popularity display,
plus a vendor-mix condition that splits shippers across the three LLMs. We report 226 experimental cells, five to ten
independent runs per condition and about 190,000 individual carrier choices, and we log every prompt and response
for audit.
We found four things. First, the concentration onto a single favorite forms on day one under every information
structure; the rules of the market then determine how much of it survives. Two mechanisms work against it. The
crowded carrier’s price spikes, and price-sensitive agents respond by trying cheap unrated entrants, whose ratings
converge to their true quality within thirty days. Thecold-start trapthat reputation theory predicts (entrants without
ratings never get chosen, so they never earn ratings; Pallais, 2014) did not arise, because high prices at the crowded
carrier keep pushing trials toward newcomers. Second, concentration rises sharply with exposure for two of the three
vendors, with most of the rise between𝐿= 10and𝐿= 15, while the third (Anthropic’s Claude) stays flat at every
exposure.Adeterministicscoringbaseline,bycontrast,concentratesfromsmall𝐿onward;adecompositionattributes
the shape of the rise largely to candidate-set overlap and the vendor contrast to the models themselves. Third, the
surviving market structure varies widely across independently sampled markets, and most of that variation traces to
the drawn market rather than to the trust signal: replacing estimated ratings with disclosed true reliability changed
neither the level nor the spread of final concentration. Fourth, of the four interventions, only capacity disclosure had
a clearly detectable effect. Displaying remaining daily capacity next to each candidate cut concentration by a third
anddoubledshippersurplus;vendordiversification,listshuffling,andpopularitydisplayshowednoclearlydetectable
T. Ezaki et al.:Preprint submitted to ElsevierPage 2 of 17

When Shippers Become Algorithms
effect.Congestionmanagement,whichArnosti,JohariandKanoria(2021)implementbylimitingapplicationsandwe
implement through disclosure, is the effective lever in AI-mediated matching as well.
The paper makes three contributions. We provide, to our knowledge, the first freight-specific market-level testbed
that embeds populations of real LLM agents in a matching market combining waterfall tendering, binding capacity,
congestion pricing, and endogenous ratings, with a decision-level audit trail; the platform extends to other two-sided
logistics questions. We recast algorithmic monoculture as a contest between two feedback loops, rating accumulation
thatentrenchestheearlyfavoriteandcongestionpricingthatworksagainstit,whichconnectsthemonocultureliterature
(KleinbergandRaghavan,2021;PengandGarg,2024)toherdingandmarketdesign(Banerjee,1992;Roth,2008)and
explains why static analyses overstate lock-in. For practice, we give DFM platforms design guidance for the arrival
of AI shippers: keep the exposure knob below the transition region, disclose capacity, and expect little from model
diversity or list randomization.
Theremainderofthepaperproceedsasfollows.Section2positionsourstudyintheliterature.Section3describes
the market institutions and the LLM agent architecture. Section 4 details the experimental design. Section 5 reports
results, and Section 6 draws managerial and regulatory implications, discusses limitations, and outlines extensions.
2. Related work
2.1. Algorithmic monoculture
Kleinberg and Raghavan (2021) show that when many decision makers adopt the same algorithm, welfare can
fall even if that algorithm beats every alternative each firm holds, because errors correlate across adopters. Peng and
Garg(2024)carrytheargumentintomatchingmarkets,wherecorrelatedevaluationsdistortbothmatchqualityandits
distributionacrossparticipants.Bommasanietal.(2022)documenttheempiricalsignature,outcomehomogenization:
thesameindividualsreceivethesamedecisionfromindependentlydeployedmodels.Anwar,SchoenebeckandDhillon
(2024) find homogenization of consumption in long-run recommender simulations, and Ashery et al. (2025) show
that populations of interacting LLMs converge on shared conventions without any central coordination. Ballestero,
Hosseini, Khanna and Shorrer (2026) add experimental evidence on the strategic side: in coordination games, LLM
subjects sustain their baseline similarity even when payoffs reward divergence, where human subjects differentiate.
These studies hold the environment fixed while the algorithms decide. We let the environment answer back. Prices,
capacities, and ratings in our market respond to what the agents do, and the imprint of monoculture then splits in two:
the day-one consensus is as extreme as the static literature would predict, while its persistence is a property of the
institutions, not of the model population.
2.2. Herding, social influence, and reputation
Sequential-choice models show how public signals crowd out private information and lock markets onto arbitrary
outcomes (Banerjee, 1992; Bikhchandani et al., 1992; Smith and Sørensen, 2000). The MusicLab experiment gave
the mechanism its sharpest empirical form: social signals raised the inequality and, above all, the unpredictability
of success (Salganik et al., 2006), and follow-up field experiments found the ratings version of the same asymmetry
(Muchnik et al., 2013). The platform-reputation literature documents both the value and the pathologies of feedback
systems:reputationshiftssalesandsurvival(CabralandHortaçsu,2010),ratingsinflateandcensor(NoskoandTadelis,
2015; Filippas et al., 2022; Tadelis, 2016), and workers without a track record face measurable cold-start exclusion
(Pallais, 2014). Our agents differ from the decision makers in herding models in a way that matters: LLM shippers
share a prior rather than observe one another, so the cascade is complete at𝑡= 0. What our experiments add is the
market’s reply. The unpredictability of outcomes that Salganik et al. (2006) induced with social signals appears in our
marketasabaselinepropertyofthefeedbackinstitutions,presentevenwhentruequalityisdisplayed,andthecold-start
trap does not close on entrants because tender rejection, not subsidy, supplies them with trials.
2.3. Congestion and information design in matching platforms
Roth (2008) lists congestion among the three failures a marketplace must manage. Arnosti et al. (2021) show that
application congestion destroys welfare in matching platforms and that limiting or redirecting applications restores it;
Guo,Haviv,LuoandWang(2023)analyzequeuedisclosureasasignalingdevice;KamenicaandGentzkow(2011)give
thegeneralframeworkinwhichadesignerchooseswhatinformationtorelease.Infreight,Wuetal.(2024)quantifythe
information value of a logistics platform, and Liu and Wahab (2025) design binding multi-period contracts to hedge
the same friction our model generates endogenously, tender rejection under tight capacity. Our capacity disclosure
T. Ezaki et al.:Preprint submitted to ElsevierPage 3 of 17

When Shippers Become Algorithms
intervention belongs to this family: it is congestion management executed inside the prompt, and it addresses with
information the same friction that Liu and Wahab (2025) address with contracts.
2.4. LLM agents in markets
Filippas et al. (2024) establish LLMs as simulated economic agents; Park, O’Brien, Cai, Morris, Liang and
Bernstein(2023)demonstratebelievablemulti-agentpopulations.Onthemarketside,Fishetal.(2024)showthatLLM
pricing agents reach supracompetitive prices without being instructed to collude, and a fast-growing set of simulation
studies examines governance, information asymmetries, and exploitation in LLM agent markets (Syrnikov, Pierucci,
Galisai,Prandi,Bisconti,Giarrusso,Sorokoletova,SurianiandNardi,2026;Lei,Nguyen,Mehta,Li,Fu,Zheng,Chen,
Liang, Torr and Yin, 2026; Erlei and Meub, 2026). Application work has moved procurement itself onto LLM rails,
from supplier evaluation frameworks (Joshi et al., 2026) and domain-specialized supply chain models (Wang et al.,
2025) to reviews of LLM adoption in supply chain management (Song et al., 2026), LLM-based demand prediction
(Nie et al., 2025), and automated design of routing optimizers (Wang, Zhang, Guo and Wu, 2026). Two testbeds
come closest to our aim. Liu, Shang and Jin (2026) build a programmable marketplace in which tool-using agents
postjobs,negotiate,andaccumulatereputation,andfindthatwell-meantinstitutionalinterventionscandegraderather
thanimprovemarketperformance;Long,Simchi-Levi,Zhu,Su,CalmonandCalmon(2026)replaceeveryplayerofa
serial supply chain with generative agents and identify run-to-run decision instability, which they call agent bullwhip,
as the central reliability risk. Neither market clears under binding capacity with congestion pricing and endogenous
ratings, and neither asks the concentration question. The matching side, where correlated preferences meet capacity
constraints, has lacked a testbed with endogenous economics. The simulation platform of this study provides one.
3. Market model and agent architecture
Figure 1a summarizes the simulated market. Fifty shipper agents, each controlled either by a commercial LLM or
by one of four reference algorithms described below, procure truckload service from twenty carriers over thirty days.
Each day every shipper issues one load with a random origin–destination pair, a dimensionless distance index drawn
uniformly from 10 to 100, and a weight drawn from{5,10,15,20,30}tons; the payment for a served load equals the
carrier’sunitpricetimesdistancetimestons,soallmonetaryquantitiesareexpressedperton-distance.Theinstitutions
follow truckload practice (Acocella and Caplice, 2023): the shipper agent returns a ranked list of three carriers, the
platformtenderstheloaddownthatlist,andthefirstcarrierwithremainingdailycapacityservesit.Ifallthreeranked
carriersarefull,theloadgoesunservedandtheshipperincursadelaycostof0.3,inthesameper-ton-distanceunitsas
prices. Within a day, loads are processed in a random order drawn each day, which also arbitrates who obtains scarce
capacity.Thiswaterfallcorrespondstotherouting-guidemechanicsthatshippersuseinpractice(Acocellaetal.,2020).
We cap the waterfall at three tenders because each additional tender costs the shipper coordination time and delay in
practice, and routing guides rarely go deeper before a load is re-brokered; letting agents rank the full displayed list is
a straightforward extension we leave for future work.
Carriers.Each carrier𝑗has four static attributes drawn independently and uniformly from[0.3,0.9]: an initial unit
price, a true reliability𝜌𝑗, a capacity weight, and a route specialty (Fig. 1b). Daily tonnage capacity is allocated in
proportion to the capacity weight and calibrated so that aggregate capacity equals1.3times expected daily demand;
individual carriers handle 27 to 70 tons per day. One carrier per sampled population has less daily capacity than the
largest30-tonload;itsimplyrejectssuchloadsinthewaterfall.Unitcostequals0.6timestheinitialprice,whichfixes
each carrier’s margin.
Prices.Carriers reprice daily in response to excess-demand pressure:
𝑝𝑗,𝑡+1 = min( max(̃ 𝑝𝑗,𝑡,1.05𝑐 𝑗),1.5 ),(1)
̃ 𝑝𝑗,𝑡 =𝑝 𝑗,𝑡 [ 1 +𝛼(𝜋 𝑗,𝑡 − 1) ],
𝜋𝑗,𝑡 =
𝑞srv 𝑗,𝑡 +𝑞 rej 𝑗,𝑡
𝑄𝑗
,
where𝑝𝑗,𝑡 iscarrier𝑗’sunitpriceonday𝑡,𝑐 𝑗 itsunitcost,𝑄 𝑗 itsdailytonnagecapacity,𝑞 srv 𝑗,𝑡 and𝑞 rej 𝑗,𝑡 thetonsitserved
and rejected that day, and𝛼= 0.10. In words: price moves by10%of the gap between demand pressure𝜋𝑗,𝑡 and one,
T. Ezaki et al.:Preprint submitted to ElsevierPage 4 of 17

When Shippers Become Algorithms
LLM shipper agents
N=50, three vendors
Candidate list
Lcarriers shown
Price·Rating·Size·Specialty
Ranked choices
(top 3 preferences)
Waterfall
tendering
Capacity consumed
/ tender rejected
Spot pricep j
∝Excess-demand pressure
Rating(¯rj, nj)
= Share of positive reviews
reads
daily
update
served loads→new reviews
Rating loop(+)
chosen→rated→chosen
entrenches the consensus
Price loop(−)
crowded→expensive→avoided
disperses demand, repairs information
Platform levers: ExposureL·Trust signal (Truth / Static / Endogenous)·Capacity disclosure·List order
next dayt+1(30 days)
a
0.4 0.6 0.8
Initial unit price
0.4
0.5
0.6
0.7
0.8
0.9
True reliability (hidden)
b
Carrier 18
(cheap, reliable)
Carrier population (bubble = capacity)
0
1
10
100
Initial track record n0 (log)
0 10 20 30
Day
0.0
0.2
0.4
0.6
0.8
1.0
Concentration κ
c Reference decision rules (L = 20)
Deterministic scoring
Random choice
d Market 50 shippers × 20 carriers
× 30 days
Agents GPT / Claude / Gemini
Lever 1 exposure L ∈ {3, 5, 10, 15, 20}
Lever 2 trust signal:
truth / static / endogenous
Lever 3 capacity disclosure, list order,
popularity display, vendor mix
Audit every prompt, response, and
market state logged
Experimental design
Figure 1:A freight matching market with two feedback loops.(a) Daily loop. Shipper agents read a candidate list,
returnrankedchoices,andtheplatformtenderseachloaddownthelistundercapacityconstraints.Ratingsaccumulate
for chosen carriers (red loop) while congestion pricing penalizes crowded carriers (blue loop). The dashed box marks
theleverswemanipulate.(b)Onesampledcarrierpopulation(seed0).Bubblesizegivesdailytonnagecapacity;color
givestheinitialnumberofratedshipments𝑛 0 (logscale);dashedblackcirclesmarkcarriersthatstartwithnoratings.
Carrier18combinesalowpricewithhighreliability.(c)Referencedecisionrulesat𝐿= 20(meanandseedrange):the
deterministic common-score rule concentrates strongly, random choice gives the floor. (d) Design summary; Table 1
gives the full condition-by-run accounting.
boundedbelowby1.05timesunitcostandabovebyanindexof1.5.Acarrierthatfillsitsbookexactlyholdsitsprice;
a carrier that turns demand away raises it. Because a rejected load continues down the routing guide, its tonnage can
enter the pressure of more than one carrier on the same day; this is intended, since each rejection is a demand signal
that carrier actually turned away, rather than double counting.
Ratings.The true reliability𝜌 𝑗 stays hidden. After each completed shipment the shipper leaves a review: a positive
review with probability𝜌𝑗, a neutral one otherwise. Real reviews are richer than this binary rule; we adopt it as a
deliberate simplification that makes the displayed rating an unbiased estimate of𝜌𝑗, so that any market pathology we
find cannot be blamed on biased reviews. The platform displays the running mean̄ 𝑟𝑗 of these reviews together with
the count𝑛𝑗 of reviewed shipments. Initial track records are set as𝑛0 = max(0,round(200𝑓 𝑗) − 10), where the fitness
𝑓𝑗 is a Pareto draw (shape1.5) rescaled to at most0.95, so the distribution of𝑛0 is heavy-tailed: in the population of
Fig. 1b, a few incumbents start with up to 180 reviewed shipments and four carriers start with none, displaying “no
T. Ezaki et al.:Preprint submitted to ElsevierPage 5 of 17

When Shippers Become Algorithms
customer ratings yet”. A carrier’s initial displayed rating is the mean of𝑛0 simulated reviews drawn with the same
Bernoulli rule. Ratings update only when a carrier serves a load, so selection and information accumulate together.
Reviews are distinct from thefailedflag that appears in an agent’s transaction history, which marks loads that none of
the three ranked carriers could serve. One design choice deserves emphasis: reliability affects outcomes only through
the reviews it generates. Whether a load is served depends on capacity alone, and payments do not depend on𝜌𝑗, so
the trust signal is a pure coordination device rather than a predictor of delivery failures. The information ablation of
Section5.3thereforemeasuresthesignal’scoordinationrole;achannelfrom𝜌 𝑗 tophysicalservicefailureisadeliberate
omission we return to in the limitations.
Shipper agents.Each shipper has a fixed procurement priority (cost, reliability, capacity, specialty, or balanced; ten
shippers each) and is controlled by a decision rule. In the LLM conditions, the rule is a commercial model that reads
a prompt and answers in JSON with three ranked carrier identifiers. The prompt shows the day’s load, a summary of
theshipper’s lastfiveshipments(unserved loadsflaggedasfailed),andone linepercandidatecarrier: thequotedtotal
price with its unit-price breakdown, the trust signal (which we manipulate below), the daily tonnage capacity, and the
specialtyscore.AppendixAreproducesacompletepromptandarawresponse.Weusegpt-5.4-mini(OpenAI),claude-
haiku-4-5(Anthropic),andgemini-3.5-flash(Google)attemperature0.7.GPTisthedefaultvendor;ClaudeandGemini
replicatetheexposuresweep,andoneconditionassignsthethreevendorstoshippersinnear-equalshares(17/17/16of
thefifty).Whenfewerthantwentycandidatesaredisplayed(𝐿<20),the𝐿candidatesaredrawnuniformlyatrandom
from the active carriers for each load; candidate order is randomized per prompt unless stated otherwise.
In the reference conditions, the rule is one of four simple algorithms:random, a uniform draw from the displayed
list;preferential attachment(Barabási and Albert, 1999), which picks carriers with probability proportional to their
discounted accumulated matches (the same0.95-per-day discounted record used for𝜅);conflicting attachment, a rule
of our construction named after Leung and Weitz (2016), in which accumulated matches first attract and then repel;
and acommon-scorerule that ranks all candidates by one fixed weighting of the displayed attributes (all parameters
in Appendix B). The common-score rule is deterministic and identical across shippers, which makes it the closest
analogueofamonocultureofliterallyidenticalclassifiers;itservesasthemain-textcontrasttogetherwiththerandom
floor (Fig. 1c). The two attachment rules stay near the random floor throughout and are reported in Appendix B.
Outcome measures.Concentration𝜅 𝑡 is computed on a running record of first choices that discounts the past: each
first choice adds one unit to the chosen carrier’s total, and at the end of every day all totals are multiplied by0.95
(relationship weights below0.05are dropped), giving the record an effective memory of about twenty days.𝜅𝑡 is the
share of this discounted record held by the three largest carriers; on day one it coincides with the day’s first-choice
share,and“final𝜅”averagesdays26–30.Arealizedversionofthesameindex,computedontheloadscarriersendup
servingratherthanonfirstchoices,trackstheallocationaftertenderrejections.WealsousetheHerfindahl–Hirschman
index (HHI) of daily first choices, the sum of squared choice shares across carriers, to measure how spread out each
day’s demand is. Welfare and service outcomes are the service rate, the mean paid unit price, shipper surplus, and
carrier revenue concentration. A served load is worth1.2per ton-distance to its shipper, so shipper surplus is1.2
minus the paid unit price, averaged over loads, with unserved loads entering at the delay cost of−0.3. Appendix C
shows that the results are unchanged under these alternative concentration indices.
4. Experimental design
We manipulate three platform levers (Fig. 1d). Theexposure sweepvaries the number of displayed candidates
𝐿∈ {3,5,10,15,20}for each vendor. Theinformation ablationreplaces the endogenous customer rating (the live
score that updates with each review) with either the disclosed true reliability (truth) or a rating frozen at its initial
value so that it never updates (static), holding everything else fixed; the comparison isolates what the rating dynamics
contribute beyond the informativeness of the signal. Theintervention comparisonstarts from the default condition
(GPT,𝐿= 20,endogenousratings)andadds oneinterventionatatime: real-timecapacitydisclosure(remainingtons
shownnexttoeachcandidate,updatedwithintheday),fixedlistorder,popularitydisplay(adiscountedcountofrecent
transactions shown as a popularity score), and the vendor mix that assigns GPT, Claude, and Gemini to shippers in
near-equal shares.
Every condition receives five independent runs that redraw the carrier population, the load stream, and the review
outcomes, except the three trust-signal conditions, which receive ten runs each: their result is a statement about
T. Ezaki et al.:Preprint submitted to ElsevierPage 6 of 17

When Shippers Become Algorithms
Family Conditions Runs Cells
Exposure sweep 3 vendors×5 exposures 5 75
Reference rules 4 rules×5 exposures 5 100
Information ablation truth, static (𝐿=20) 10 20
(endogenous) GPT𝐿=20cells+5 runs 10 5
Interventions capacity, order, popularity 5 15
Vendor mix GPT/Claude/Gemini 5 5
Price counterfactual𝛼∈ {0.05,0.02}3 6
Total 226
Table 1
Experimental design.Runscounts independent repetitions per condition; each run redraws the carrier population, the load
stream, and the review outcomes. The endogenous information condition reuses the five GPT𝐿= 20sweep cells and adds
five more runs, so only the additional cells are counted in its row.
dispersion across runs, and variance estimates from five runs would be too coarse to compare. For a given run index,
thethreeinformationconditionssharethecarrierpopulation,theloadstream,andthecandidatedraws,socomparisons
across them are paired; all other condition families redraw everything, and variation across their runs therefore mixes
differences in the drawn market with stochastic history (we return to this in Section 5.3). Throughout, final𝜅per run
is the unit of analysis: variance comparisons use Brown–Forsythe tests, location comparisons use exact two-sided
Mann–Whitney tests (no ties occurred), paired Wilcoxon tests are used where conditions share seeds, and we report
Holm–Bonferroni-corrected𝑝-values alongside the raw ones within each family of comparisons. We report 226 cells
(Table 1) and about 190,000 individual LLM decisions. The simulator logs every prompt, raw response, and market
state transition; the full audit logs are released with the code and data.
5. Results
5.1. Choices concentrate on day one; the market spreads them out
Figure 2a shows how first choices were distributed on the first day of the default condition. The single most-
requestedcarrierdrew14to37of50firstchoicesdependingontherun,andthethreemost-requesteddrew62to96%;
day-one𝜅averaged0.79,faraboveanythingthemarketlatersustained.Whichcarrierplaysthefavoritedependsonthe
drawncarrierpopulation,notonthedecisionmaker:eachrunredrawsthepopulationandelevatedadifferentfavorite,
but for a fixed population every vendor and information condition produced the same modal first choice. Under the
populationofFig.1b,carrier18,thecheapestofthehighlyreliableincumbents,toppedtheday-onetallyinthedefault
condition,underbothothervendors,andunderbothalternativeinformationstructures,with19to38of50firstchoices.
Thisinitialconcentrationthendeclinedsteadilyoverthefirstweekandsettledat𝜅= 0.42(range0.35–0.45across
runs), roughly2.4times the random-choice floor of0.18(Fig. 2b). Figure 2c shows what happened to the day-one
favorite itself: its excess demand drove its unit price to the cap within 13 days, and its first-choice share fell from0.74
to about0.12. Displaced and price-sensitive agents tried the cheap carriers that started with no or almost no reviews,
and those carriers’ displayed scores converged to their true reliability within the month. For example, the strongest of
theseentrants(truereliability0.90,displayedas0.25fromfourearlyreviews)served81loadsandendedatadisplayed
rating of0.84(Fig. 2d). Thecold-startexclusion that field evidence documents for human markets (Pallais, 2014) did
notappearhere,becausecongestionkeptroutingtrialstowardnewcomers.Shipperspaidforthispartialself-correction:
the mean paid price rose from0.53to0.96and shipper surplus halved (Fig. 2e).
A counterfactual that slows the price response separates the two market forces behind the correction (Fig. 2f). At
adjustmentratesof0.05and0.02insteadof0.10,thefavorite’sdeclineslowed(meanday-2share0.30and0.41versus
0.23) but arrived at the same endpoint: by day 30 the day-one favorite held a share of0.15–0.17at every rate, and the
initially unrated carriers still served160loads under the stickiest prices (196at the base rate). Tender rejection under
the capacity constraint did the dispersing and supplied the trials; congestion pricing set the pace. The cold-start trap
stayed open even when prices barely moved.
5.2. Concentration rises sharply with exposure, and the rise depends on the vendor
Figure 3a traces final concentration against the exposure𝐿. For GPT the curve stayed flat at𝜅= 0.26–0.31up to
𝐿= 10and then climbed steeply, reaching0.40at𝐿= 15and0.43at𝐿= 20. Every run increased from𝐿= 10to
T. Ezaki et al.:Preprint submitted to ElsevierPage 7 of 17

When Shippers Become Algorithms
Carriers (rank-sorted per run)
0
10
20
30
Day-1 first choices
a
Top-1 votes across models &
information structures: 19–38 / 50
(dots: individual runs)
Day 1: choices pile onto a few carriers
0 10 20 30
Day
0.0
0.2
0.4
0.6
0.8
1.0
Concentration κ
b
Consensus erodes, then persists
GPT, L = 20
Random reference
0 10 20 30
Day
0.0
0.2
0.4
0.6
0.8
First-choice share
c
The day-1 favorite prices itself out
First-choice share
Unit price
0.6
0.8
1.0
1.2
1.4
Unit price (dashed)
0 10 20 30
Day
0.2
0.4
0.6
0.8
1.0
Displayed rating
d
Unrated entrants earn accurate ratings
True reliability
0 10 20 30
Day
0.0
0.2
0.4
0.6
0.8
1.0
Index
e
Shippers pay for the correction
Mean paid price
Shipper surplus
0 10 20 30
Day
0.1
0.2
0.3
0.4
0.5
Day-1 favorite's share
f
Prices set the pace, capacity the endpoint
Price adj. rate
0.10 (base)
0.05
0.02 (sticky)
Figure2:Choicesconcentrateondayone;capacityandpricesspreadthemout(GPT,𝐿= 20,endogenousratings).
(a) Day-one first choices, carriers sorted by rank within each run: bars give the mean across five runs, dots individual
runs. The top-ranked carrier draws 14–37 of 50 first choices per run. For a fixed carrier population, the same carrier
tops every vendor and information condition (19–38 of 50). (b) Concentration𝜅over 30 days: thin lines are runs, the
thick line the mean, gray the random-choice band. (c) The day-one favorite’s first-choice share (solid) and unit price
(dashed)intherunofpanela:thepricereachesthecapbyday13andthesharecollapses.(d)Displayedratingsofthe
five initially unrated or underrated carriers converge to their true reliabilities (dotted), same run. (e) Mean paid price
and shipper surplus (mean±range across runs). (f) Share of the day-one favorite under three price-adjustment rates
(means over three runs): stickier prices slow the decline without changing its endpoint.
𝐿= 15(Fig. 3d). Gemini showed the same shape with a higher ceiling (0.51at𝐿= 20), and Claude never left the
0.25–0.31bandatanyexposure.Thedeterministiccommon-scorerule,incontrast,concentratedfromsmall𝐿onward
(the two attachment rules stayed near the random floor; see Appendix B).
Part of this rise is built into the display mechanics. The𝐿displayed candidates are a fresh uniform draw per load,
so raising𝐿does two things at once: it makes different shippers’ lists overlap more, and it raises the probability that
any given carrier, including the favorite, is on someone’s screen (𝐿∕20). At small𝐿the agents could not all pick the
same carrier even if they wanted to. To separate these mechanics from agent behavior, we ask two questions of the
data.First,doagentsseizethefavoritemoreeagerlywhenlistsarelong?No:conditionalontherun’sday-onefavorite
actuallybeingdisplayed,theprobabilitythatanagentpicksitfallsfrom0.57at𝐿= 3to0.14at𝐿= 20.Therisein𝜅
thereforecomesfromthefavoriteappearingonmorescreens,notfromstrongerattachmentperencounter.Second,how
muchoftheriseappearswithnochangeinagentbehaviorandnomarketfeedbackatall?Wefreezeeachrun’sday-one
choicefrequencies andreplaythem, redrawingonlythe displayedsubsets: thisstaticbenchmark yieldsdailytop-three
sharesof0.44∕0.57∕0.73∕0.78∕0.80at𝐿= 3∕5∕10∕15∕20.Candidate-setoverlapalonethusreproducesariseofthe
same shape, concentrated below𝐿= 15, though at a level far above what the interacting market sustains. Together
the two checks assign the roles: the display mechanics produce the shape of the rise, the market’s capacity and price
feedback compress its level, and the LLM-specific content is the vendor contrast, since Claude faces identical display
mechanics at every𝐿and does not rise. Whether model-level mechanisms such as long-context retrieval degradation
(Liu, Lin, Hewitt, Paranjape, Bevilacqua, Petroni and Liang, 2024) contribute on top of the mechanics would require
designs that vary list length while holding display probability fixed, which we leave to future work.
T. Ezaki et al.:Preprint submitted to ElsevierPage 8 of 17

When Shippers Become Algorithms
Widerexposurecostshippersmoney.Surplusfellwith𝐿forallthreevendorswhiletheserviceratestayednear0.9
(Fig. 3b,c); the deterministic rule shows what a market breakdown would look like instead, with service collapsing to
0.23at𝐿= 20.Thedailytrajectories(Fig.3e)showwherethetransitionoperates:everyexposurestartedconcentrated,
but only at𝐿≥15did the day-one concentration survive the month.
3 5 10 15 20
Exposure L (log scale)
0.2
0.3
0.4
0.5
0.6
0.7
0.8
Final κ
a Concentration vs. exposure
3 5 10 15 20
Exposure L (log scale)
−0.2
0.0
0.2
0.4
Shipper surplus
b
Welfare mirrors concentration
3 5 10 15 20
Exposure L (log scale)
0.2
0.4
0.6
0.8
1.0
Service rate
c
LLMs keep the market serving
L = 10 L = 15
0.30
0.35
0.40
Final κ
d
The jump, seed by seed (GPT)
0 10 20 30
Day
0.3
0.4
0.5
0.6
0.7
0.8
Concentration κ
e
Daily paths by exposure (GPT)
L = 3
L = 5
L = 10
L = 15
L = 20
GPT Claude Gemini Deterministic Random
Figure3:Concentrationrespondstoexposurewithavendor-dependenttransition.(a)Final𝜅againstexposure𝐿
(mean±range across runs; bands are drawn where three or more runs are available; the shaded vertical band marks
the transition zone). (b) Shipper surplus and (c) service rate against𝐿. (d) Final𝜅at𝐿= 10versus𝐿= 15for GPT;
each dot is one run, lines connect runs. (e) Daily concentration for GPT by exposure (means across runs).
5.3. Information quality had no detectable effect on the level or the spread
Thesecondleveristhetrustsignalitself.Thedefaultistheendogenousrating,thelivecustomerscorethatupdates
as reviews arrive. Holding the market fixed, we replaced it with either the true reliability (truth) or a rating frozen at
itsinitialvalue(static),andaskedwhetherthequalityofthedisplayedinformationchangeswhatthemarketconverges
to.
The answer is that no effect is detectable. Mean final concentration barely moved across the three structures (0.46
under truth,0.43under static,0.46under endogenous; Fig. 4a; paired Wilcoxon𝑝≥0.19, unpaired Mann–Whitney
𝑝≥0.21, for every pairwise comparison). Neither did the dispersion: the standard deviation of final𝜅was0.10under
truth,0.10under static, and0.08under endogenous (Brown–Forsythe𝑝≥0.75for every pairwise comparison; no
pairwise difference in means exceeds0.04, and every bootstrap95%confidence interval brackets zero, the widest
being[−0.12,0.05]). Under every structure, individual runs ranged from dispersed (𝜅= 0.31–0.35) to locked onto an
arbitrary favorite (𝜅= 0.62–0.69), and the daily trajectories split into branches that never rejoined (Fig. 4b–d).
What produces this wide dispersion? Because runs redraw the carrier population and the load stream, variation
across them mixes differences in market fundamentals with stochastic history, and the shared seeds across the three
information conditions let us bound the two parts. Final𝜅is strongly correlated across conditions run on the same
population (𝑟= 0.93between truth and endogenous,0.49–0.68for the other pairs), and a variance decomposition
attributes76%of the total variation to which market was drawn, with the remaining24%arising within a market
acrossconditionsandstochastichistories.Thedispersionisthereforeprimarilyapropertyofthesampledmarket:even
witheachcarrier’struereliabilityondisplay,whichcarriersthemarketelevateddependedonthedrawnpopulationand
on the early path of prices and displaced demand, and no trust-signal design we tested reduced either the level or the
spread.Isolatingtruepathdependence,inthesenseofSalganiketal.(2006),wouldrequirerepeatedstochastichistories
T. Ezaki et al.:Preprint submitted to ElsevierPage 9 of 17

When Shippers Become Algorithms
on a fixed population, which our design does not include; we flag it as a direct extension. Two caveats apply. Failure
to detect a difference is not equivalence: with ten runs per condition, level effects smaller than roughly0.1would go
undetected. Reliability is also payoff-irrelevant here (Section 3), so this comparison of information structures isolates
the coordination role of the trust signal rather than its value as a predictor of failures. For a platform, the practical
reading is correspondingly narrow: in this market, neither keeping ratings live nor replacing them with verified true
quality made the resulting market structure any less variable.
truth static endogenous
0.3
0.4
0.5
0.6
0.7
Final κ (L = 20)
a
0 10 20 30
Day
0.2
0.4
0.6
0.8
1.0
Concentration κ
b
Truth
0 10 20 30
Day
0.2
0.4
0.6
0.8
1.0c
Static
0 10 20 30
Day
0.2
0.4
0.6
0.8
1.0d
Endogenous
Figure 4:Final concentration varies widely across sampled markets under every trust-signal structure(GPT,
𝐿= 20).(a)Final𝜅bytrust-signalstructure;barsgivemeansacrossruns,dotsindividualruns(tenrunsperstructure).
(b–d)Dailytrajectoriesperstructure,onelineperrun:undereverystructuretherunssplitintolocked-inanddispersed
branches.
5.4. Of the four interventions, only capacity disclosure has a clearly detectable effect
Thethirdleveriswhatelsetheplatformdisplays.Startingfromthedefaultcondition,weaddedoneinterventionat
atimeandcomparedfinalconcentrationagainsttheno-interventionbenchmark(Fig.5a).Capacitydisclosurelowered
final𝜅to0.29(range0.26–0.33), below every no-intervention run (Mann–Whitney𝑝 <0.001; the only effect that
survives Holm–Bonferroni correction across the four intervention comparisons, adjusted𝑝= 0.003; difference in
means−0.17,bootstrap95%CI[−0.23,−0.12]).Fixedlistorderandpopularitydisplaystraddledthebenchmarkwith
effects that changed sign from run to run (𝑝= 0.44and𝑝= 0.95; differences in means−0.04and−0.02, with CIs
[−0.11,0.03]and[−0.09,0.05]thatbracketzero);thepositionbiasdocumentedinevaluationsettings(Zheng,Chiang,
Sheng, Zhuang, Wu, Zhuang, Lin, Li, Li, Xing, Zhang, Gonzalez and Stoica, 2023) did not survive contact with price
and rating signals. The vendor mix ended slightly below the benchmark on average (final𝜅of0.36–0.43across runs,
mean0.41against0.46) without reaching significance (𝑝= 0.075; adjusted𝑝= 0.23), consistent with the day-one
resultthatthethreevendorssharethesamefavorite.Withfiverunsthedesigncannotdistinguishanullfromamodest
effect, but mixing models that agree clearly does not diversify demand the way capacity disclosure does.
Themechanismofcapacitydisclosureoperatesupstreamoftheratingloop(Fig.5b);theeffectisattributabletothe
displayedinformationitself,nottothesequentialexecutionthedisclosurerequires,sincepromptscarrynoinformation
about other shippers’ same-day decisions unless capacity is disclosed. With remaining capacity on display, the HHI
of daily requests started at0.11on day one, against0.31without disclosure, so the pile-up that capacity and prices
must undo later never formed. Service failures and their delay costs all but disappeared, which is where the surplus
gainoriginated:intheconcentration–surplusplane(Fig.5c),capacitydisclosureoccupiesitsowncorner,withshipper
surplus of0.41against the baseline0.19, while every other intervention clusters with the baseline. The gain is not a
transferfromcarriers:totalsurplusperton-distance(shippervalueminuscarrierresourcecost,withunservedloadsat
the delay cost, so that payments net out) rose from0.63under the benchmark to0.76under disclosure, because loads
that would have failed were served.
5.5. The settled matching: who ends up with whom
Concentrationindicescompresstheoutcomeintoonenumber.Theaudittrailalsoshowswhoendsupmatchedwith
whom.Figure6drawsthefinalweekoffirstchoices(days26–30)asanetworkfromthefiveprocurementprioritiesto
the twenty carriers, for three runs that span the results above: the default-condition run of Fig. 2c–d, a locked-in run
of the same condition, and a capacity-disclosure run.
T. Ezaki et al.:Preprint submitted to ElsevierPage 10 of 17

When Shippers Become Algorithms
None Capacity Order Popular. Mix
0.0
0.2
0.4
0.6
Final κ
a
p<0.001
p=0.44
p=0.95
p=0.08
Concentration by intervention
0 10 20 30
Day
0.1
0.2
0.3
0.4
0.5
0.6
HHI of daily requests
b
Disclosure disperses demand upstream
No intervention
Capacity disclosure
0.3 0.4 0.5 0.6
Final κ
0.1
0.2
0.3
0.4
0.5
Shipper surplus
c
Concentration vs. shipper surplus
No intervention
Capacity disclosure
Fixed list order
Popularity display
Vendor mix
Figure 5:Capacity disclosure lowers concentration and raises shipper surplus; the other interventions show
no clearly detectable effect(GPT,𝐿= 20). (a) Final𝜅by intervention (bars: means; dots: runs). Brackets give
uncorrected two-sided Mann–Whitney𝑝-values against the no-intervention benchmark; only capacity disclosure
remains significant after Holm–Bonferroni correction across the four comparisons (adjusted𝑝= 0.003). (b) HHI
of daily first choices with and without capacity disclosure (mean±range across runs). (c) Final𝜅against shipper
surplus, one marker per run.
Three points emerge. First, the concentration that survives in the default condition is structured by preference, not
arbitrary(Fig.6a).Cost-priorityshippersspreadoverthecheapendofthepricerange(meanpaidunitprice0.50),while
reliability-priorityshippersbuyattheexpensivetop(mean1.48),andthecarrierstheypickaverageatruereliabilityof
0.88against0.45for the cost segment; one carrier receives no first choice at all. The𝜅= 0.44at which this particular
run settles reflects a few favorites per segment rather than one market-wide favorite. Second, the locked-in tail of
Section 5.3 is a different matching structure under identical rules (Fig. 6b): the favorite absorbs58–68%of the first
choices of the reliability, capacity, and specialty segments (and none of the cost segment, which keeps buying cheap),
whilefourcarriersendthemonthwithoutanyfirstchoice.Third,capacitydisclosurechangesthenetwork,notjustthe
index(Fig.6c):demandspreadsovernearlyeverycarrier,thepreferencesortingatbothendsofthepricerangepersists,
and reliability-priority shippers pay1.09instead of1.48, because the pile-up that would have driven their favorites to
the price cap never forms.
a
Cost
Reliability
Capacity
Specialty
Balanced
Carriers by final unit price (cheap →  expensive)
Default run (κ = 0.44) b
Carriers by final unit price (cheap →  expensive)
Locked-in run (κ = 0.63) c
Carriers by final unit price (cheap →  expensive)
Capacity disclosure (κ = 0.26)
0.0
0.2
0.4
0.6
0.8
1.0
Final displayed rating
No demand in final week
Figure 6:The settled matching between shipper priorities and carriers(first choices, days 26–30). Left nodes: the
five procurement priorities (ten shippers each). Right nodes: the twenty carriers, ordered bottom to top by final unit
price, sized by first choices received, colored by final displayed rating; open dashed circles mark carriers that receive
no first choice in the final week. Edge width gives the number of first choices from a priority to a carrier. (a) The
default-condition run of Fig. 2c–d. (b) A locked-in run of the same condition. (c) A capacity-disclosure run.
T. Ezaki et al.:Preprint submitted to ElsevierPage 11 of 17

When Shippers Become Algorithms
6. Discussion and implications
6.1. Summary of results
Our simulations gave a consistent answer to the opening question. When LLM agents take over carrier selection,
theirchoicesconcentrateonasinglecarrierimmediately:thepile-upappearedondayoneineveryexperiment,atevery
exposure and under every trust signal, because the agents share the same preferences before the market has generated
any history. What happened next depended on the market’s rules rather than on the models. The capacity limit spread
the excess demand within days and gave unrated entrants work; congestion pricing set the speed of that spreading
and passed its cost to shippers; and the surviving concentration varied widely from one sampled market to another
under every trust signal we tested. Comparing the three levers by effect size: showing more candidates moved mean
concentration from0.26to0.43; replacing disclosed true quality with estimated ratings moved neither the mean nor
the run-to-run dispersion; and disclosing capacity moved concentration by−0.15while doubling shipper surplus.
6.2. Implications for platform design
Four operational lessons follow for DFM platforms preparing for algorithmic shippers. First, the length of the
candidate list is a market-structure decision, not a user-interface detail: below roughly ten displayed candidates the
monoculture stays inert, and the transition zone sits within the range platforms use today. Second, capacity disclosure
isthecheapesteffectivelever.Theplatformalreadyholdsthedata,theinterventionneedsonelineintheinterface,and
in our runs it cut concentration by a third and doubled shipper surplus by preventing the pile-up rather than repairing
it. Third, interventions that sound protective under-deliver: mixing model vendors fails because the vendors share the
samefavorite,andrandomizingorfreezinglistorderwashesoutagainstpriceandratingsignals.Fourth,donotexpect
better trust signals to stabilize the market. Neither keeping ratings live nor replacing them with disclosed true quality
reducedthevariabilityofthefinalmarketstructure,andmostofthatvariabilitytracedtothedrawnmarketitselfrather
than to the signal. The lesson is bounded by the model: quality here has no payoff consequences, so the signal’s only
role is coordination; where quality predicts physical failures, better signals may still earn their keep through match
qualityeveniftheydonotreduceconcentration.Aplatformthatwantsapredictablemarketstructurehastoactonthe
mechanisms that create the lock-in, the congestion of early demand and its pricing, rather than on the accuracy of the
scores it displays.
Thevendorcomparisoncarriesitsownmessage.Ashipper’schoiceoffoundationmodelismarket-relevant:Claude
populationsneverconcentratedatanyexposurewhileGeminipopulationsconcentratedmost,sotheaggregatemarket
outcome depends on a decision each firm makes privately for reasons of cost or convenience.
6.3. Implications for the monoculture debate
Our experiments speak to both sides of the policy discussion around algorithmic homogeneity. On one side, they
show that static audits of decision correlation overstate the danger: we found that in a market with binding capacity
andresponsiveprices,theworstmomentisthefirstone,afterwhichthemarketitselfundoespartoftheconcentration
(attheshippers’expense).Ontheotherside,theyshowthatthecorrectionhaslimits:concentrationsettledat2.4times
the random floor, the decline slowed when prices were sticky, and which carrier ends up dominant varies widely from
one sampled market to another regardless of the trust signal on display. The practical remedy our experiments single
out is transparency about capacity. This suggests disclosure obligations as a lighter-touch alternative to regulating
the models themselves, complementing the antitrust concerns raised for LLM pricing agents (Fish et al., 2024). The
dispersionresultconnectstoapatternnowemergingacrossautonomous-agentoperations:Longetal.(2026)document
agent bullwhip, run-to-run decision instability, in serial supply chains, and our market exhibits its matching-market
counterpart,astructurethatvarieswidelyfrommarkettomarketundereverytrustsignal.Inbothsettingstheinstability
survivesremediesaimedatthesignal(repeatedsamplingofthemodelthere,betterratingshere),whichpointsattention
toward the institutions the agents operate in rather than toward their outputs.
6.4. Relation to human freight markets
The behaviors our agents display have documented human counterparts: carriers respond to shippers’ tendering
consistency within a market cycle (Acocella et al., 2020), and long-term relationships coexist with spot opportunism
(Harris and Nguyen, 2025b,a). LLM shippers reproduce the relationship channel through their transaction history
and respond to spot prices, which makes the comparison meaningful, but we do not claim behavioral equivalence. A
head-to-headbenchmarkagainstestimatedhumancarrier-choicemodelsisthenaturalnextstep,andtheaudittrailour
platform produces makes that comparison feasible at the level of individual decisions.
T. Ezaki et al.:Preprint submitted to ElsevierPage 12 of 17

When Shippers Become Algorithms
6.5. Limitations
Five limitations bound the claims, and each points to a specific extension. First, the model is a stylized capacity-
constrained procurement market inspired by freight rather than a calibrated freight market: fifty shippers, twenty
carriers, a single stylized set of shipping routes, and stationary demand over thirty days; contract freight, differences
across routes, and seasonality are absent, origins and destinations do not affect carrier suitability, specialty is a carrier
scalar rather than a carrier–load match, and distance and tonnage scale every carrier’s quote by the same factor. The
economic parameters were likewise fixed at one point of a larger space (aggregate capacity at1.3×expected demand,
price cap1.5, delay cost0.3, three-tender routing guides, thirty days), and only the price-adjustment rate received a
robustnesscheck;thecapacity-disclosureeffectinparticularshouldstrengthenascapacitytightens,andmappingthese
sensitivities is the immediate next use of the platform. These features change where demand piles up, not the fact that
correlatedpreferencespileitup,soweexpecttheday-oneresulttosurvivethem.Twoquantitativequestionsdodepend
onscaleanddeservededicatedsweeps:whetherthesharpriseinconcentrationsitsatanabsolutelistlength(aboutten
candidates) or at a fraction of the carrier pool (half of twenty), and how𝜅and the HHI, which mechanically depend
on the number of carriers, translate to larger markets.
Second, carriers price mechanically and never act strategically: there is no carrier-side AI, no entry, and no exit.
Strategic carriers would likely amplify our mechanism rather than dampen it, since a carrier that anticipates LLM
preferences can court them, for instance with AI-written pitches that exploit the documented preference of LLMs for
LLM-generated text (Laurito, Davis, Grietzer, Gavenčiak, Böhm and Kulveit, 2025); carrier exit would convert the
welfarestakesfrompricepremiaintophysicaldeliveryfailures(Elliott,GolubandLeduc,2022).Bothareworthwhile
follow-ups.
Third, quality is informational rather than payoff-relevant in our market: reviews are unbiased binary draws,
reliability does not cause delivery failures, and so agents lose nothing by ignoring the trust signal. This isolates the
signal’s coordination role, but it also means the null result of Section 5.3 should not be read as “information quality
never matters”: where quality predicts physical failures, or where reviews inflate and censor as field studies document
(Filippasetal.,2022;NoskoandTadelis,2015),thecomparisoncouldcomeoutdifferently.Extensionswithapayoff-
relevant𝜌and biased review processes are the direct test; the same extensions would also let quality enter the surplus
accounting.
Fourth, results are snapshots of three specific commercial models at temperature0.7with one English prompt
format. We did not vary prompt wording, and LLM choices are known to shift with phrasing; the fact that three
independentlytrainedmodelsproducedthesameday-onefavoritesuggeststheconcentrationresultisnotanartifactof
our template, but a systematic prompt-sensitivity study, together with successor model versions, is needed before the
vendor-specific numbers are treated as stable.
Fifth, and related, our shipper populations are closer to replicated instances of one centrally designed agent than
to independently engineered procurement systems: all fifty shippers share the same prompt template, decision format,
temperature,andhistorystructure,differingonlyintheirstatedpriority.Realadopterswoulddifferincontracts,service-
level requirements, prompt engineering, tools, and organizational policy, and even firms using the same foundation
model would implement different agent architectures. The day-one convergence is therefore best read as an upper
bound, the worst case in which deployments share both the model and the task formulation, and the vendor-mix
condition,whichvariesonlythemodel,isaweaktestofgenuinelyindependentsystemdesign.Howmuchheterogeneity
in agent engineering dissolves the day-one consensus is an open question the platform can address directly.
7. Conclusion
We placed populations of real LLM agents inside a freight matching market that answers back, with binding
capacity, congestion pricing, and endogenous ratings, and measured what algorithmic procurement does to market
structure. Demand concentrated on a single carrier on the first day in every condition we tested, so the interesting
question is not whether AI shippers concentrate but what happens next, and that depends on the market’s rules. The
capacity limit spread the excess demand, prices set the speed of the spreading, the surviving market structure varied
widely from market to market under every trust signal, and the platform’s information choices, above all how many
candidates to show and whether to reveal remaining capacity, governed the result more than the choice of model. For
transportationresearch,thisrelocatesthequestion.ThearrivalofAIshippersisnotaforecastproblemaboutwhatthe
modelswillprefer;theirpreferenceisuniformandimmediate.Itisadesignproblemaboutthemarkettheywillprefer
it in.
T. Ezaki et al.:Preprint submitted to ElsevierPage 13 of 17

When Shippers Become Algorithms
Appendix A. Prompt and example response
Each decision is one LLM call. The prompt below is reproduced verbatim from the audit log (default condition,
day 1, one shipper; carrier lines abbreviated to three of twenty). The system instruction asks for three ranked carrier
identifiers in JSON.
You are a decision-making agent in charge of freight
procurement at a shipper (cargo owner) company. From the
list of candidate carriers, choose 3 carriers in order of
preference, identified by their carrier ID (e.g.
"carrier_07"). If your 1st choice is fully booked, your
2nd choice will be tendered, then your 3rd. Respond ONLY
in the following JSON format (no other text before or
after):
{"choices": ["<1st choice>", "<2nd choice>",
"<3rd choice>"], "reason": "<your rationale in 1-2
sentences>"}
# Shipper ID: shipper_049
# Your priority: balanced (weigh all factors evenly)
# Today’s request: loc_12 -> loc_07, distance 17,
15 tons, within 1 day
# Summary of your past transactions: none
# Candidate carriers (in random order)
1) carrier_10: quoted price 138 (unit price 0.54 x
distance 17 x 15 tons), customer rating 0.42 (based
on 74 rated shipments), company size: up to 27
tons/day, specialty 0.65
2) carrier_05: ...
3) carrier_01: ...
Choose 3 carriers in order of preference (use their
carrier IDs) and respond in JSON.
The trust-signal line varies by condition: the truth condition showsreliability 0.42, the static condition
shows the same customer-rating format frozen at its initial value, and the capacity-disclosure condition appends
remaining capacity today: 34 tonsto each line. Carriers without reviews displayno customer ratings
yet (new carrier). The five procurement priorities are inserted verbatim into theYour priorityline:cost
first (minimize freight cost),reliability first (avoid delivery problems),capacity first
(prefer carriers that can handle volume),specialty first (prefer carriers whose expertise
fits the route),andbalanced (weigh all factors evenly);capacity-priorityshippersactonthedisplayed
companysize(tonsperday),sinceremainingcapacityishiddenoutsidethedisclosurecondition.Atypicalrawresponse
reads:{"choices": ["carrier_18", "carrier_16", "carrier_19"], "reason": "carrier_18 offers
the best overall value with a low quoted price, a high customer rating, and sufficient capacity
for 15 tons."}
Appendix B. Reference decision rules
The four reference rules replace the LLM call and receive the same candidate information.Randomdraws
uniformlyfromthedisplayedlist.Preferentialattachment(BarabásiandAlbert,1999)drawscarrier𝑗withprobability
proportionalto1 +𝑚 𝑗,where𝑚 𝑗 isthecarrier’saccumulatedmatchesdiscountedat0.95perday(thesamediscounted
record that underlies𝜅).Conflicting attachmentdraws with probability proportional to(1 +𝑚 𝑗) exp(−0.05𝑚𝑗), so
accumulated matches attract and then repel; the rule is our construction, and the name borrows from the conflicting
node-attachment mechanism of Leung and Weitz (2016).Common-scoreranks candidates deterministically by one
fixedlinearscoreofthedisplayedattributes,−0.8 price+1.1 rating+0.8 capacity+1.0 specialty(attributesnormalized
tocomparablescales);itseesthesameobservedratingtheLLMagentssee,neverthetruereliability(carrierswithout
T. Ezaki et al.:Preprint submitted to ElsevierPage 14 of 17

When Shippers Become Algorithms
reviews enter at the uninformative prior0.5, and capacity enters as the normalized weight underlying the displayed
tons per day). Figure A1 reports all four across the exposure sweep: the two attachment rules stay near the random
floor at every exposure, which is why the main text uses the common-score rule and the random floor as its contrasts.
3 5 10 15 20
Exposure L (log scale)
0.2
0.3
0.4
0.5
0.6
0.7
0.8
Final κ
a Concentration
Random
Preferential attachment
Conflicting attachment
Common-score
(deterministic)
3 5 10 15 20
Exposure L (log scale)
0.2
0.4
0.6
0.8
1.0
Service rate
b Service
Figure A1:Reference decision rules across the exposure sweep(five runs each; mean±range). (a) Final𝜅.
(b) Service rate.
Appendix C. Alternative concentration measures
Themaintextmeasuresconcentrationonfirstchoices.Threealternativesleadtothesameconclusions:therealized
version of𝜅, computed on the loads carriers end up serving after tender rejections; the revenue share of the three
highest-earning carriers; and the HHI of served loads. Figure A2 traces all three across the exposure sweep for GPT
against the random floor. The realized measures compress the differences, because the capacity limit truncates how
much demand any carrier can actually serve, but the ordering and the transition are unchanged. An attempted-tender
version, computed on every tender the waterfall issues rather than on first choices alone, sits between the two: its
final-week top-three share is0.39(range0.27–0.55) across the default-condition runs, against0.46for first choices.
3 5 10 15 20
Exposure L (log scale)
0.18
0.20
0.22
0.24
0.26
0.28
0.30
Final realized κ
a Realized allocation
GPT
Random
3 5 10 15 20
Exposure L (log scale)
0.20
0.25
0.30
0.35
0.40
0.45
Top-3 revenue share
b Carrier revenue
3 5 10 15 20
Exposure L (log scale)
0.060
0.065
0.070
0.075
0.080
HHI of served loads
c Served-load HHI
Figure A2:Alternative concentration measures across the exposure sweep(GPT versus random; five runs each;
mean±range). (a)𝜅computed on realized allocations. (b) Revenue share of the top three carriers. (c) HHI of served
loads.
Declaration of generative AI and AI-assisted technologies in the writing process
During the preparation of this work the authors used Claude (Anthropic) in order to improve the language and
readability of the manuscript and to assist with the implementation of the simulation and analysis code. After using
this tool, the authors reviewed and edited the content as needed and take full responsibility for the content of the
publication.
T. Ezaki et al.:Preprint submitted to ElsevierPage 15 of 17

When Shippers Become Algorithms
Declaration of competing interest
Theauthorsdeclarethattheyhavenoknowncompetingfinancialinterestsorpersonalrelationshipsthatcouldhave
appeared to influence the work reported in this paper.
Data availability
The simulation platform, prompt templates, experiment scripts, and the complete decision-level audit logs (every
prompt, raw model response, parsed ranking, and daily market state for all reported cells) are publicly available at
https://github.com/tkEzaki/llm-freight-market.
CRediT authorship contribution statement
Takahiro Ezaki:Conceptualization, Methodology, Software, Formal analysis, Writing – original draft.Naoto
Imura:Supervision, Writing – review & editing.Katsuhiro Nishinari:Supervision, Writing – review & editing.
References
Acocella, A., Caplice, C., 2023. Research on truckload transportation procurement: A review, framework, and future research agenda. Journal of
Business Logistics 44, 228–256. doi:10.1111/jbl.12333.
Acocella, A., Caplice, C., Sheffi, Y., 2020. Elephants or goldfish? an empirical analysis of carrier reciprocity in dynamic freight markets.
Transportation Research Part E: Logistics and Transportation Review 142, 102073. doi:10.1016/j.tre.2020.102073.
Anwar, M.S., Schoenebeck, G., Dhillon, P.S., 2024. Filter bubble or homogenization? disentangling the long-term effects of recommendations on
user consumption patterns, in: Proceedings of the ACM Web Conference 2024 (WWW ’24), pp. 123–134. doi:10.1145/3589334.3645497.
Arnosti, N., Johari, R., Kanoria, Y., 2021. Managing congestion in matching markets. Manufacturing & Service Operations Management 23,
620–636. doi:10.1287/msom.2020.0927.
Ashery, A.F., Aiello, L.M., Baronchelli, A., 2025. Emergent social conventions and collective bias in LLM populations. Science Advances 11,
eadu9368. doi:10.1126/sciadv.adu9368.
Ballestero, G., Hosseini, H., Khanna, S., Shorrer, R.I., 2026. Strategic algorithmic monoculture: Experimental evidence from coordination games.
arXiv preprint arXiv:2604.09502 doi:10.48550/arXiv.2604.09502.
Banerjee, A.V., 1992. A simple model of herd behavior. The Quarterly Journal of Economics 107, 797–817. doi:10.2307/2118364.
Barabási, A.L., Albert, R., 1999. Emergence of scaling in random networks. Science 286, 509–512. doi:10.1126/science.286.5439.509.
Bikhchandani, S., Hirshleifer, D., Welch, I., 1992. A theory of fads, fashion, custom, and cultural change as informational cascades. Journal of
Political Economy 100, 992–1026. doi:10.1086/261849.
Bommasani,R.,Creel,K.A.,Kumar,A.,Jurafsky,D.,Liang,P.,2022. Pickingonthesameperson:Doesalgorithmicmonocultureleadtooutcome
homogenization?, in: Advances in Neural Information Processing Systems 35 (NeurIPS 2022), pp. 3663–3678. doi:10.52202/068431-0265.
Cabral, L., Hortaçsu, A., 2010. The dynamics of seller reputation: Evidence from eBay. The Journal of Industrial Economics 58, 54–78.
doi:10.1111/j.1467-6451.2010.00405.x.
Elliott, M., Golub, B., Leduc, M.V., 2022. Supply network formation and fragility. American Economic Review 112, 2701–2747. doi:10.1257/
aer.20210220.
Erlei, A., Meub, L., 2026. LLM-agent interactions on markets with information asymmetries. arXiv preprint arXiv:2603.08853 doi:10.48550/a
rXiv.2603.08853.
Filippas, A., Horton, J.J., Golden, J.M., 2022. Reputation inflation. Marketing Science 41, 733–745. doi:10.1287/mksc.2022.1350.
Filippas, A., Horton, J.J., Manning, B.S., 2024. Large language models as simulated economic agents: What can we learn from homo silicus?, in:
Proceedingsofthe25thACMConferenceonEconomicsandComputation(EC’24),pp.614–615. doi:10.1145/3670865.3673513.extended
version: NBER Working Paper 31122.
Fish, S., Gonczarowski, Y.A., Shorrer, R.I., 2024. Algorithmic collusion by large language models. arXiv preprint arXiv:2404.00806 doi:10.485
50/arXiv.2404.00806.
Guo,P.,Haviv,M.,Luo,Z.,Wang,Y.,2023. Signalingservicequalitythroughqueuedisclosure. Manufacturing&ServiceOperationsManagement
25, 543–562. doi:10.1287/msom.2022.1170.
Harris, A., Nguyen, T.M.A., 2025a. Long-term relationships and the spot market: Evidence from US trucking. Working paper.https:
//nguyentmanh.github.io/files/HarrisNguyen_Truck_LTR-spot.pdf.
Harris, A., Nguyen, T.M.A., 2025b. Long-term relationships in the US truckload freight industry. American Economic Journal: Microeconomics
17, 308–353. doi:10.1257/mic.20210343.
Joshi,A.,Singh,M.,Parashar,D.,Singh,M.,2026. Amulti-agentlargelanguagemodelframeworkforintelligentvendorevaluationandrisk-aware
procurement decisions. Scientific Reports 16, 19826. doi:10.1038/s41598-026-50952-x.
Kamenica, E., Gentzkow, M., 2011. Bayesian persuasion. American Economic Review 101, 2590–2615. doi:10.1257/aer.101.6.2590.
Kleinberg, J., Raghavan, M., 2021. Algorithmic monoculture and social welfare. Proceedings of the National Academy of Sciences 118,
e2018340118. doi:10.1073/pnas.2018340118.
Laurito,W.,Davis,B.,Grietzer,P.,Gavenčiak,T.,Böhm,A.,Kulveit,J.,2025. AI-AIbias:Largelanguagemodelsfavorcommunicationsgenerated
by large language models. Proceedings of the National Academy of Sciences 122, e2415697122. doi:10.1073/pnas.2415697122.
T. Ezaki et al.:Preprint submitted to ElsevierPage 16 of 17

When Shippers Become Algorithms
Lei,S.,Nguyen,Q.,Mehta,S.S.,Li,Z.,Fu,H.,Zheng,X.,Chen,S.,Liang,Y.,Torr,P.,Yin,Z.,2026. StrategicexploitationinLLMagentmarkets:
A simulation framework for e-commerce trust. arXiv preprint arXiv:2605.10059 doi:10.48550/arXiv.2605.10059.
Leung, C.Y.J., Weitz, J.S., 2016. Conflicting attachment and the growth of bipartite networks. Physical Review E 93, 032303. doi:10.1103/Phys
RevE.93.032303.
Liu,N.F.,Lin,K.,Hewitt,J.,Paranjape,A.,Bevilacqua,M.,Petroni,F.,Liang,P.,2024. Lostinthemiddle:Howlanguagemodelsuselongcontexts.
Transactions of the Association for Computational Linguistics 12, 157–173. doi:10.1162/tacl_a_00638.
Liu, X., Shang, H., Jin, H., 2026. When agent markets arrive. arXiv preprint arXiv:2604.06688 doi:10.48550/arXiv.2604.06688.
Liu, Y., Wahab, M.I.M., 2025. Multi-period binding freight contract using swing options. Transportation Research Part E: Logistics and
Transportation Review 204, 104419. doi:10.1016/j.tre.2025.104419.
Long, C.X., Simchi-Levi, D., Zhu, F., Su, H., Calmon, A.P., Calmon, F.P., 2026. Reliability and effectiveness of autonomous AI agents in supply
chain management. arXiv preprint arXiv:2605.17036 doi:10.48550/arXiv.2605.17036.
Muchnik,L.,Aral,S.,Taylor,S.J.,2013.Socialinfluencebias:Arandomizedexperiment.Science341,647–651.doi:10.1126/science.1240466.
Nie, T., He, J., Mei, Y., Qin, G., Li, G., Sun, J., Ma, W., 2025. Joint estimation and prediction of city-wide delivery demand: A large language
model empowered graph-based learning approach. Transportation Research Part E: Logistics and Transportation Review 197, 104075.
doi:10.1016/j.tre.2025.104075.
Nosko, C., Tadelis, S., 2015. The Limits of Reputation in Platform Markets: An Empirical Analysis and Field Experiment. Working Paper 20830.
National Bureau of Economic Research. doi:10.3386/w20830.
Pallais, A., 2014. Inefficient hiring in entry-level labor markets. American Economic Review 104, 3565–3599. doi:10.1257/aer.104.11.3565.
Park, J.S., O’Brien, J.C., Cai, C.J., Morris, M.R., Liang, P., Bernstein, M.S., 2023. Generative agents: Interactive simulacra of human behavior, in:
Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology (UIST ’23), pp. 1–22. doi:10.1145/3586183.
3606763. article 2.
Peng, K., Garg, N., 2024. Monoculture in matching markets, in: Advances in Neural Information Processing Systems 37 (NeurIPS 2024), pp.
81959–81991. doi:10.52202/079017-2605.
project44, 2026. project44 launches AI freight procurement agent to cut freight spend and accelerate sourcing. Press release, 26 February 2026.
https://www.project44.com/press-releases/project44-launches-ai-freight-procurement-agent-to-cut-freight-s
pend-and-accelerate-sourcing/.
Roth,A.E.,2008. Whathavewelearnedfrommarketdesign? TheEconomicJournal118,285–310. doi:10.1111/j.1468-0297.2007.02121.x.
Salganik, M.J., Dodds, P.S., Watts, D.J., 2006. Experimental study of inequality and unpredictability in an artificial cultural market. Science 311,
854–856. doi:10.1126/science.1121066.
Smith, L., Sørensen, P., 2000. Pathological outcomes of observational learning. Econometrica 68, 371–398. doi:10.1111/1468-0262.00113.
Song, Z., Xie, Y., Yang, L., Zhao, Y., 2026. Large language models in supply chain management: a systematic literature review and application
framework. International Journal of Production Research doi:10.1080/00207543.2026.2641103. advance online publication.
Syrnikov, M.B., Pierucci, F., Galisai, M., Prandi, M., Bisconti, P., Giarrusso, F., Sorokoletova, O., Suriani, V., Nardi, D., 2026. Institutional AI:
Governing LLM collusion in multi-agent cournot markets via public governance graphs. arXiv preprint arXiv:2601.11369 doi:10.48550/arX
iv.2601.11369.
Tadelis, S., 2016. Reputation and feedback systems in online platform markets. Annual Review of Economics 8, 321–340. doi:10.1146/annure
v-economics-080315-015325.
Wang, H., Jiang, J., Hong, L.J., Jiang, G., 2025. LLMs for supply chain management. arXiv preprint arXiv:2505.18597 doi:10.48550/arXiv.2
505.18597.
Wang,Y.,Zhang,L.,Guo,Y.,Wu,L.,2026. TowardsautomatedoptimizationalgorithmdesignwithLLM:Anexploratorystudyinmulti-objective
weather routing. Transportation Research Part E: Logistics and Transportation Review 210, 104786. doi:10.1016/j.tre.2026.104786.
Wu, Y., Huang, J., Chen, X., 2024. The information value of logistics platforms in a freight matching market. European Journal of Operational
Research 312, 227–239. doi:10.1016/j.ejor.2023.06.043.
Zheng, L., Chiang, W.L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z., Li, D., Xing, E.P., Zhang, H., Gonzalez, J.E., Stoica, I.,
2023. JudgingLLM-as-a-judgewithMT-BenchandChatbotArena,in:AdvancesinNeuralInformationProcessingSystems36(NeurIPS2023),
Datasets and Benchmarks Track, pp. 46595–46623. doi:10.52202/075280-2020.
T. Ezaki et al.:Preprint submitted to ElsevierPage 17 of 17
