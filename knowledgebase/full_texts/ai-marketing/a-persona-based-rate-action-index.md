---
title: A Persona-based Rate Action Index
url: https://arxiv.org/abs/2607.26545
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Hayden Helm
- Andrew Dassori
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.26545
pages: 15
chars: 61859
fetched_at: '2026-11-08T13:21:40+00:00'
kb_version: 1
---

# A Persona-based Rate Action Index

A Persona-based Rate Action Index
Hayden Helm1∗ & Andrew Dassori2
1Helivan &2Wavelength Capital
/githubCode: github.com/helivan-research/fomc-personas
Data: huggingface.co/datasets/helivan/fomc-personas
Live Index: federalreserve.ai
Abstract
We propose an index for predicting the U.S. Federal Open
MarketCommittee(FOMC)decisiontohike/hold/cutthecur-
rent federal funds target rate based on how a collection of
personas responds to current market conditions. To construct
the index, we collected a new dataset consisting of nearly
25,000retrievable chunks from publicly available data. We
partitionthedataintoper-membercorporaanduseeachasthe
retrieval database of a generative system we refer to through-
out as a “persona”. We first evaluate the personas across two
complementary components of likeness: identifiability and
detectability. Each persona’s behavior is highly attributable
(average member-conditional recall is8×chance) and gen-
erated content is nearly indistinguishable from held-out real
content (ˆτdet = 0.23against a0.15floor). We then present
evidence that query-conditioned representations of the per-
sonas capture members’ monetary-policy stance relative to a
knownhawk–dovereputationalordering(Kendall’sτ= 0.63,
p <0.001), substantially outperforming retrieval-only repre-
sentations. These representations vary with time and current
marketconditionsandformthebasisofourproposedpersona-
based rate action index. For the2022–2025period the index
tracks the rate cycle (Kendall’sτ= 0.68,p <10 −6) and
can be used to construct a simple classifier that predicts per-
meetingoutcomesatnon-trivialaccuracy(0.69versusa0.47
base rate). Importantly, the index outperforms informative
baselines and leads the federal funds target rate by roughly
three quarters. As far as we are aware, our results are the
first to demonstrate the ability to capture time-varying group
behavior via a collection of digital personas.
1 Introduction
The U.S. federal funds target rate is among the most conse-
quential levers in the global economy. The rate is set by the
FederalOpenMarketCommittee(FOMC)ateightscheduled
meetingsthroughouttheyear.Eachdecisiontohike/hold/cut
the rate impacts asset prices, borrowing costs and the path
of inflation and employment. Market participants therefore
devote considerable time and effort to anticipate the com-
mittee’s actions: expectations of the next move are priced
continuously in federal funds futures, and surprises rela-
tivetothoseexpectationsmoveassetpricessharply(Kuttner
2001).Todate,quantitativeforecastsofrateactionshavebeen
market-implied (i.e., read from futures), rule-based (Taylor
∗Corresponding author:<first-name>@helivan.io.
1993),ordistilledfromthetoneofcentral-bankcommunica-
tion(LuccaandTrebbi2009;Shah,Paturi,andChava2023).
These approaches aggregate over the committee and do not
attempt to model the committee members’ heterogeneous
dispositions (Istrefi 2019; Bordo and Istrefi 2023).
Recent work in adjacent literatures has demonstrated that
modelingindividualsfromtheirpastbehaviorispossible.For
example,ingenerativesurveyingaprofile-conditionedmodel
reproduces survey responses (Argyle et al. 2023; Brand, Is-
raeli, and Ngwe 2023) and can recover subgroup opinions
(Santurkaretal.2023),replicatehuman-subjectexperiments
(Aher, Arriaga, and Kalai 2023; Horton, Filippas, and Man-
ning 2023; Yeykelis et al. 2024), and, given rich per-person
data, match the answers of thousands of named individuals
(Park et al. 2024). Closest to our setting, Helm et al. (2025)
build a persona of each member of the U.S. Congress and
predict their voting behavior on legislation. These results
share a structure we reuse: a person is modeled by a genera-
tive model with access to their past behavior, and the model
is then queried to predict a future action. The FOMC is a
favorable setting for this approach as it is a (relatively) fixed
body of public figures, each with a long attributed record.
Concretely, we build a persona – which, for our purposes,
is a base model combined with a member-specific retrieval
database–foreachmemberfromtheirpublicrecordanduse
their behavior with respect to a collection of market-aware
queries to construct an index for rate action. Our contri-
butions are threefold.(i) Data:we present a new speaker-
attributedtemporalcorpusofFOMCmembers’publicstate-
mentsdesignedforretrieval-augmentedgeneration.Thedata
covers seventeen of nineteen sitting members and includes
24,333chunks from2006to2026(§3, Appendix A).(ii) A
two-axislikenesscheck:weverifyeachpersonaisfaithfulto
itsmemberalongtwoaxes,identifiability(between-persona)
anddetectability(within-persona) (§4).(iii) A persona-
basedindex(PBI):comparingpersonabehavioracrosstime,
we find that query-conditioned behavioral representations
of the personas match a reputational ordering of the mem-
bers (§5). Importantly, the behavioral representations vary
withmarketconditionsandcanbeaggregatedintoaforward
committee-levelindex.Wevalidatetheindexagainstrealized
FOMC decisions and relevant baselines (§6). As far as we
areawarethisisthefirstvalidationofusingpersonastotrack
a time-varying covariate.
arXiv:2607.26545v1  [cs.MA]  29 Jul 2026

Related Work
Synthetic respondents and digital twins.Beyond the
generative-surveyingresultsthatmotivateourapproach(§1),
abroadliteratureconditionslanguagemodelsonpersonasto
role-play identities or stand in for human respondents (Chen
et al. 2024; Tseng et al. 2024; Shanahan, McDonell, and
Reynolds2023)andrunsmulti-agentsimulationsinplaceof
human social studies (Park et al. 2023; McGuinness et al.
2024).Thepromiseiscontested–syntheticrespondentscan
misstate distributions and hinge on prompt phrasing (Dil-
lion et al. 2023; Helm and Priebe 2026) – which is why our
analysisisgroundedinper-memberdetectabilityandout-of-
sample validation. A more rigorous instance is thedigital
twin: a continuously updated computational counterpart of
a system that supports valuable inference about it (National
Academies of Sciences, Engineering, and Medicine 2024).
Agrowinglineofworkbuildslanguage-modeltwinsofindi-
vidualsandgroups–benchmarksforpersona-basedbehavior
simulation(Lietal.2025),datasetspairingthousandsofpeo-
ple with their twins (Toubia et al. 2025; Park et al. 2024),
andpopulation-scaletwinsforsimulatingresponsetopolicy
(Koaik, Gupta, and Sheikh 2026). We build on the frame-
work of Helm et al. (2025), which sets requirements for a
collection of personas to count as a digital twin – relevant
and continuously updated data, high likeness, valid infer-
ence, and useful predictions – and instantiate one for the
entireFOMC.Weevaluateourpersonasagainsttheseprinci-
ples. We further extend evidence of possible valid inference
fromastaticquantity(e.g.,adiscretevoteonlegislation)toa
dynamic one (e.g., continuously moving policy instrument),
which requires conditioning the personas on a time-varying
environment not necessary in previous work.
Measuring FOMC stance and action.A rich literature
extracts member disposition (often framed as the “hawk
(hike)–dove (cut) axis”) from central-bank text: dictio-
nary and lexicon scores (Lucca and Trebbi 2009; Tobback,
Nardelli, and Martens 2017; Picault and Renault 2017),
computational-linguistics analyses of transcripts (Hansen,
McMahon, and Prat 2018; Hansen and McMahon 2016),
objective-functionestimates(ShapiroandWilson2022),vo-
cal tone (Gorodnichenko, Pham, and Talavera 2023), and
market-implied surprises (Kuttner 2001). Recent work ap-
plies language models to Fed communication directly, clas-
sifyingstatementstance(HansenandKazinnik2023),quan-
tifying member dissent (Peskoff et al. 2023), and building
high-frequency sentiment indices from news coverage of
Fed communications (Wong, Hallmark, and Galvao 2023),
alongside datasets that label FOMC text for stance and mar-
ket impact (Shah, Paturi, and Chava 2023). Most of this
work scores statement- or institution-level communication.
We instead model each member as a generative persona and
aggregate the members’ inferred stances into a committee
index validated against realized rate decisions.
2 Setup and Notation
For our purposes, a generative systemf:Q → Xis a (ran-
dom) mapping from a collection of queries to a response
space. A system’s responsef(q)is assumed an indepen-
dent sample from a query-conditioned distribution. Con-
tent produced by a member of the FOMC is modeled as
an observation from the query-conditioned distribution of
a member-specific ground truth system. In particular, let
F ∗(t) ={f ∗(t) 1 , . . . , f∗(t) n }be the collection ofnmem-
bers at timet, where memberiis a systemf ∗(t) i and their
statements are realizations off∗(t) i (q)for a givenq. We ap-
proximateeachmember-specificsystemwithapersonaf (t) i ,
parameterized by a base modelfbase and a member-specific
retrieval databaseD (t) i . The personas form the collection
F (t) ={f (t) 1 , . . . , f(t) n }.HereD (t) i denotesmemberi’sstate-
ments dated≤t(§3) in the fullD i. We letg:X →R p
denote a fixed embedding function that maps each response
to ap-dimensional vector.
In our setting, each member also has a time-varying
system-level covariatey (t) i ∈R d that we wish to recover
– such as their disposition to hike/hold/cut the federal funds
target rate given market conditions at timet.
Likeness.Thefirstgoalofthispaperistoestablishthat,for
theD i described in §3, a persona approximates its member:
f (t) i ≈f ∗(t) i . We decompose thislikenessinto between- and
within-persona components in §4.
System-level covariate prediction.The second goal is to
recovereachmember’shike/cut/holddispositionfromitsper-
sona across variable market conditions.
3 Data and Corpus Construction
The FOMC comprises nineteen individuals: seven Board
governors and twelve regional Reserve Bank presidents. To
construct each persona’s member-specific corpus, we draw
onfourdocumenttypes:i)speeches,ii)testimony,iii)FOMC
meeting transcripts (exact speaker labels, released on a five-
year lag), and iv) FOMC press conferences (chairs only, no
lag).
Given a document, we extract retrievable chunks with an
LLM under a constrained schema. Each chunk is a record
⟨source, member id, time, is_voting, is_chair, topic, stance,
embedding⟩. The topic is a free-text label that we classify
into one of six themes: inflation and prices, employment
and labor, rates and policy, financial stability, growth and
outlook, or other. The stance is a self-contained sentence
stating the member’s position, and its embedding is a1024-
dimensional vector (text-embedding-3-large, Ope-
nAI 2024b). For example, one press-conference chunk has
stance “We want to ensure that inflation remains near our
symmetric 2 percent longer-run goal on a sustained basis,”
topic“inflationtarget,”andtheme“inflationandprices.”The
booleansis_votingandis_chairindicatewhetherthespeaker
was a voting member and whether they were the chair on
the statement’s date, derived from the member id and time
againsttheFOMCvotingrotationandchairtenure(nullwhen
astatementisundated).Weonlyadmitachunktoamember’s
corpus if their attribution is unambiguous.
We onboard seventeen of the nineteen members. Two we
cannot: one whose only outlet blocks automated access at

speechestranscriptspress conf.testimony
0
5k
10kchunks
(a) by source
1 5 10 15
member id
102
103
104
chunks (log)
(b) per member
2010 2020
0
2kchunks
(c) by year
Inflation
14%
Employment
9%
Rates
15%
Financial 19%
Growth
16%
Other
26%
(d) by topic
Figure1:Corpuscomposition(24,333chunks).(a)bysource;
(b) per member, by member id (Table 4); (c) by year of the
sourcedocument;(d)bytopictheme.Thecoremacrothemes
account for∼three quarters of the corpus.
thenetworklevel,andoneaninterimappointeewithnopub-
lished record. The resulting corpus spans883documents
and24,333chunks.Per-membercountsrangefrom285doc-
uments (9,855chunks) for the chair to6documents (83
chunks) for the most recently appointed president. Coverage
is continuous from 2006 to the present. We also create a
biography for each member to further ground the persona.
Biographiesshareacommonformatandareusedastheper-
sona’s system prompt. Figure 1 summarizes the corpus. Ap-
pendixAdocumentseverysource,theconstrainedextraction
schema and chunking, and the per-stage filters. Appendix B
provides per-member corpus size, channels, and collection
start dates.
Ours is not the first dataset consisting of public FOMC
data. Existing datasets annotate text at the sentence or state-
ment level for classification or measurement (Lucca and
Trebbi 2009; Hansen, McMahon, and Prat 2018; Gorod-
nichenko,Pham,andTalavera2023;Shah,Paturi,andChava
2023; Kanganis and Keith 2025). None attribute text to in-
dividual members across multiple sources and none include
pre-computed embeddings for retrieval-based personas. We
provide a more in-depth comparison of our dataset to others
in Appendix A in Table 3.
4 Likeness
Webuilduptothepersona-basedactionindexbyfirstdemon-
stratingthatthecollectedcorporaparameterizepersonasthat
have high likeness to their corresponding member. Unlike
previous work, we break this down into two complementary
components: (i)identifiabilityand (ii)detectability. We for-
malize each as a property of a query set and the risk of a
classification problem.
LetQ={q 1, . . . , qm}be a collection of queries and, for
asystemf,letP f (q)bethedistributionoftheresponsef(q)
andP f (Q)the distribution of its responses overQ. We let
h:X → Ybe a decision function onXandℓan appropri-
ately defined loss. We defineR(h) :=E(X,Y) [ℓ(h(X), Y)]
as the risk ofhandR i(h) :=E X|Y=i [ℓ(h(X), i)]its class-
conditional risk. Given a fixed set of decision functionsH,
we leth∗ = arg minh∈H R(h)be the decision function that
achieves minimal risk andhc a chance-level classifier. For
simplicity we assume zero-one loss.
The two components of likeness can then be described as
properties of two classification problems:
(i)identifiabilityis then-way problem of attributing a re-
sponseX∼P fi (Q)to its persona, assuming uniform
class-conditional priors. All personas are identifiable if
the best classifier inHoutperformshc on every persona:
max
i
Ri(h∗ id)< R i(hc id).
Estimating identifiability requires each persona to re-
spond to the same set of queries.
(ii)detectabilityis the binary problem of separating a mem-
ber’s real responsesPf ∗ i (Q)from its persona’s generated
onesP fi (Q); following Helm et al. (2025), we require
low detectability:
τdet = 1−R(h ∗ det)/R(hc det)≈0
(τdet=0indistinguishable,τ det=1always detected). Es-
timating detectability requires each persona to produce
content paired with content known to be written by its
member.
Personas.We usegpt-4o-mini(OpenAI 2024a) as
fbase. Each persona has a member-specific biography as its
system prompt and access toDi. We embed all text with
text-embedding-3-large(OpenAI 2024b). Given a
queryq,wescoreeverystances∈D i bythecosinesimilar-
ity between its embedding and the query’s and place the top
kin context, fork∈ {0, . . . ,5}(k=0is the biography-only
persona).
Methods.For(i)identifiability,everypersonaanswersthe
same query setQ–30monetary-policy questions designed
to elicit member behavior. We embed each response and
trainalinearclassifiertorecoverwhichpersonaproducedit.
A persona is identifiable when its attribution recall exceeds
chance (1/17 = 0.059). For(ii) detectability, we use the
seededcompletionsproposedbyHelmetal.(2025):foreach
member we hold out40of their real stances (≥8words),
revealtheopeningwordsofeach,andhavethepersonacom-
plete it. We train a linear classifier to predict the source of
the completed stance and report detectability (ˆτdet). As a
reference we also report the averagereal–realdetectability
– the detectability between two independent samples of a
member’s own real content. It is a lower bound on the aver-
agepersonadetectability:nopersonacanresembleamember
more closely than the member’s own writing does. The first
column of Figure 2 shows high- and low-scoring examples
on each axis.

Schmid
(high, 0.93)
(a) identifiability
Powell
(low, 0.30)
Collins
(k = 3, = 0.02)
(d) detectability
3
 0 3
discriminant
Hammack
(k = 0, = 0.68)
102 103 104
corpus size (chunks, log scale)
0.0
0.2
0.4
0.6
0.8
1.0
likeness axis
id = 0.37 (p = 0.04)
det = +0.23 (n.s.)
(f) neither axis tracks corpus size
identifiability
detectability
0.0
0.2
0.4
0.6
0.8
1.0
attribution recallchance
(b) identifiability vs k
mean
0.1
0.2
0.3
detectability
Kendall = 0.17 (n.s.)
(c) the two axes are uncorrelated
0 1 2 3 4 5
retrieval depth k (k = 0: no retrieval)
0.0
0.2
0.4
0.6
0.8
1.0
detectability
real real floor
(e) detectability vs k
mean
Figure 2: Likeness of the persona collection, measured along two axes:identifiability(top row, blue) anddetectability(bottom
row,orange).(a)Identifiabilityexample:the17-wayattributionclassifier’slog-probabilitythataresponseisthenamedmember,
on that member’s own responses vs. all others’ (grey), for a high- (Schmid) and a low-identifiability (Powell) member. (b) Per-
memberidentifiability(attributionrecall)vs.retrievaldepthk(faint=members,bold=mean;chance= 1/17).(d)Detectability
example:generatedcontinuationsvs.themember’srealones(grey)foralow-detectability(Collins,k=3)andahigh-detectability
(Hammack,k=0) member. (e) Per-memberˆτdet vs.k(real–real floor in grey). (c) Per-member identifiability vs. detectability
(k=3). (f) Both axes (k=3) vs. per-member corpus size (log scale).
Results.The center columns (b, e) of Figure 2 show how
identifiability and detectability vary with the retrieval depth
k. The biography-only persona (k=0) is weakly identifiable
– mean recall0.13(2.2×chance), with5of17members
below chance – and highly detectable (ˆτdet ≈0.5). Byk=3
every persona has enough member-specific signal (mean re-
call0.48, minimum0.30; averageˆτ det = 0.23relative to
average real–real lower bound of0.15).
Thetop-rightpanel(c)showsthatthetwocomponentsare
uncorrelated across members (Kendallτ=−0.17, n.s.) – an
identifiable persona may be detectable and vice versa. The
bottom-rightpanel(f)plotsbothaxesagainstcorpussizeand
showsthatneitherisadata-volumeartifact.Identifiabilityis,
if anything,negativelyassociated with corpus size (Kendall
τ=−0.37,p=0.04): the smallest twin (Schmid,83chunks)
isthemostidentifiable(0.93).Thisislikelyapropertyofthe
FOMCsincegovernorsandthechairhavethelargestcorpora
but are usually tightly aligned in their stances.
5 Stance Prediction
Wehaveestablishedthatthepersonasbehaveliketheircorre-
spondingmember.Wenowusethemtopredictthemembers’
relative position on the hawk–dove spectrum by their re-
sponsestoacollectionofqueries.Weuseanews-derivedor-
deringofthemembersalongthehawk–dovespectrum(Istrefi
2019; Bordo and Istrefi 2023) to validate and compare dif-
ferent ways of estimating the stance ordering.
Stance representations.We compare three representa-
tions, each providing a single vector per member summa-
rizing their position:
(i)corpus average: the mean of the embeddings of every
statement inDi;
(ii)retrieval-based: the mean embedding of the top-kstate-
ments retrieved fromDi, averaged over a query setQ;
(iii)persona-based: the mean embedding of the response the
persona generates, averaged over a query setQ.
Giventheper-memberrepresentations,weprojectthemonto
a spectrum defined by the mean embeddings of canonically
hawkishanddovishstatements, [hawkand ddove.Inparticular,
lettingu= [hawk− ddove, we predict each member’s stance
withbyi =⟨ψ i(Q), u⟩. We report the retrieval-based and
persona-basedestimatesacrossretrievaldepthsk,evaluating
eachprojectionbyKendall’sτagainstthereputationalorder-
ing. The curated set ofm= 30monetary-policy questions,
together with the hawkish and dovish anchor statements, is
provided in Appendix C.
Results.The results for recovering the reputational hawk–
dove ranking are provided in Figure 3. The top row shows
the estimated ranking of thebyi for each per-member rep-
resentation atk= 3. Panel (d) shows the sensitivity of

hawk dove
reputation rank
hawk
doveestimate rank
= 0.30
(a) retrieval-based
hawk dove
reputation rank
= 0.63
(b) corpus average
hawk dove
reputation rank
= 0.63
(c) persona-based
0 1 2 3 4 5
retrieval depth k
0.0
0.2
0.4
0.6
Kendall
(d) recovery vs. retrieval depth
corpus average
retrieval-based
persona-based
0 10 20 30
number of queries
0.0
0.2
0.4
0.6
Kendall
full set
(e) recovery vs. query-set size
random subsets
0.0 0.1 0.2 0.3
mean per-query Kendall's
tactics & timing
0.16
inflation strictness
0.23
mandate priorities
0.30
(f) per-query signal by type
Figure 3: Stance recovery against an external hawk–dove reputational ordering of the16scored members. (a–c) Atk=3, each
panelranksthemembersbytheirreputation(horizontal)againsttherankinducedbyoneestimate(vertical);thedasheddiagonal
is perfect recovery (Kendallτin the title, colour = reputation): (a) retrieval-based, (b) corpus average, (c) persona-based.
(d)Per-estimateτvs.retrievaldepthk(corpusaveragehasnoretrieval,dashed;k=0isthebiographyalone).(e)Persona-based
τvs. query set size. (f) Mean per-query Kendall’sτby query type.
recovery to retrieval depth. The retrieval-based estimate is
weak at every retrieval depth (Kendallτ= 0.23–0.32, not
significant).Thecorpusaveragerecoversthereputationalor-
dering well (τ= 0.63,p <0.001), and the persona-based
estimate matches or exceeds it once a few statements are re-
trieved – peaking atk=2(τ= 0.65) and holdingτ= 0.63
throughk=4(Figure 3d). The corpus–reputation agreement
is expected – the reputation is a tenure average, which any
career-leveldata-drivensummary willmatchalmostbycon-
struction.
The last two panels of Figure 3 show the effect of the
query-set size (panel e) and type (panel f) on the quality
of the persona-based estimates. For panel (e) we randomly
sample query sets of sizes{1, . . . ,20}from the30curated
queries to estimate the reputational ordering; we note di-
minishing returns in recovery beyondm≈10. For panel
(f) we instead score a separate, balanced pool of72queries
spanning12hawk–dove facets, grouped into three topics
(mandate priorities, inflation strictness, and tactics & tim-
ing). Ranking members from each single query (m=1) and
averaging Kendall’sτwithin each topic, questions about a
member’s mandate priorities discriminate most (τ= 0.30)
while timing- and tactics-oriented questions carry the least
signal (τ= 0.16). We compare the persona-based rank-
ing generated withgpt-4o-minito those generated with
ministral-8binAppendixC;theyhavelargeagreement
(Kendall’sτ= 0.69).
6 A Rate-Action Index
Reputationalstanceestimationvalidatesbasicinferencewith
thepersonasonastatictarget.Wenowextendstancepredic-
tion into a rate-action index that responds to market condi-
tions,byaddingtime-varyinginformationtoeachqueryand
tracking the personas’ behavior over time.
Incorporating market conditions.The FOMC makes its
decisiontohike/hold/cutthefederalfundsratebasedonsev-
eralfactors,includingheadlineandcoreinflation,theunem-
ployment rate, and the current target range for the rate, all
available from the FRED repository of economic data (Fed-
eralReserveBankofSt.Louis2025).Wesummarizecurrent
market conditions with a single stringc(t):
Current U.S. economic conditions as of {date}: CPI infla-
tion is running at about {cpi} year over year; core PCE
inflation is about {core_pce} year over year (the FOMC
targets2%);theunemploymentrateis{unemployment};
thecurrentfederalfundstargetrangetopsoutat{target}.
We prependc (t) to every query, formingQ (t) =
{c(t)+q1, . . . , c(t)+qm}.
GivenQ (t) we generate stance representations for each
memberusingD (t) i ,themember’scontentpubliclyavailable
strictly beforet. FOMC meeting transcripts (32% of the
corpus) are dated at the meeting they record but published
only after a≈5-year embargo, so filtering on the statement
date alone would let the backtest retrieve text that was not
publicattimet;wedatetranscriptsattheirreleaseandapplya
strictday-beforecutoff,sonothingapersonareadspostdates

2018 2019 2020 2021 2022 2023 2024 2025 2026
0.05
0.00
0.05
PBI
(a) PBI vs. fed funds target
PBI (left)
0
1
2
3
4
5
target upper (%)
hike
(n = 11)
hold
(n = 15)
cut
(n = 6)
0.03
0.04
0.05
0.06
0.07
PBI
(b) PBI by decision (2022--25)
chanceTaylorretr.directmacrostatic PBI persist.
0.0
0.2
0.4
0.6
0.8
OOS accuracy
0.53 0.56 0.53 0.50 0.59
0.69
0.78
base rate 0.47
at decision changes (n=7):
PBI 0.29, persist. 0.00
(c) decision accuracy vs. baselines
2
 0 2 4 6 8 10 12
lead (meetings)
0.0
0.2
0.4
0.6
0.8
Kendall  w/ target level
 = 0.84 at +8
series leads
(d) the PBI leads the rate level
CPI (control)
static idx (control)
PBI
Figure 4: The persona-based index (PBI). (a) The PBI (red, left axis) moderately tracks the fed funds target (black, right axis)
over 2018–2025. (b) PBI by realized decision (2022–25): hikes separate cleanly (hike-vs-rest AUC1.00), while restrictive-era
cuts and holds partially overlap. (c) Walk-forward decision accuracy (2022–25): the PBI (0.69) beats chance, the Taylor rule,
a fitted macro model, and the retrieved-text and static-query controls; only persistence is higher. (d) Kendall’sτbetween each
series and the funds-rate level as the series is slid forward. The PBI’s correlation rises from0.42(contemporaneous) to0.84at
a lead of+8meetings (≈3 quarters), significantly exceeding both controls.
– or was unpublished at – the meeting being predicted. We
project each representation onto the fixed hawk–dove axisu
(§5) and average across members to produce a committee-
level, persona-based index (PBI).
Validation.We validate PBI on two tasks: i)trackingthe
federal funds target rate and ii)predictingthe hike/hold/cut
outcomeofeachmeeting.Fortracking,wemeasurehowwell
PBI’s level co-moves with the per-meeting basis-point move
overthe64FOMCmeetingsfrom2018to2025,measuredby
Kendall’sτ.Forprediction,wefitalinearhike/hold/cutclas-
sifier on the committee index and evaluate it walk-forward.
We report three different accuracies: 3-class classification,
move versus hold, and hike versus rest.
We compare PBI to seven baselines under a walk-forward
protocol. Three are ablations to localize the signal:
1.Macro: a classifier fitted on the same macroeconomic
inputs(inflation,unemployment,thetargetlevel,andtheir
momentum) – does the persona signal add over the raw
macro data?
2.Retrieved-text: a no-generation index that projects each
member’sdate-≤tretrievedchunksontothesameaxis–
does generation beat scoring the recent text?
3.Static query set: the same generation pipeline over the
fixed queries,withoutthe time-varying briefingc (t) –
doesconditioningontheeconomybeatastaticqueryset?
The other four are simple baselines:chance(always predict
hold),persistence(repeat the previous meeting’s decision),
afixedTaylorrule(Taylor1993),andadirectvote(askeach
persona to vote hike/hold/cut directly).
Results.ThePBItracesthecycle(Figure4a):mildlyhawk-
ish in 2018, dovish through the 2019–21 easing, climbing
ahead of the 2022 pivot, and peaking in 2022–23 before
moderating through the 2024–25 easing to a level still ele-
vated relative to the pre-tightening cycle. Its level co-moves
with the realized move (Kendall’sτ= 0.35over the full
period;τ= 0.68,p <10 −6, over2022–2025) and only
persistence tracks comparably (Table 1).
ThePBIclassifieshike/hold/cutat0.69againsta0.47base
rate, with strong hike detection (hike/rest0.88; hike-vs-rest
AUC on the raw level1.00). It beats chance, the Taylor rule
(0.53), and the retrieved-text index (0.56). Most pointedly,
it beats a macro classifier fitted on the same briefing vari-
ablesc (t) the personas have access to (0.50), and removing
the briefing entirely (static query set) collapses tracking to
τ≈0. Generation alone is not enough, though – a direct
hike/hold/cutvotecollapsestowardtheholdbaserate(0.53)
– so the predictive power sits in both the generation and its
projection onto the stance axis.

Track Classification (2022–25)
Methodτ3-class hike/rest move/rest
Baselines
Chance (hold) — 0.47 0.66 0.47
Persistence 0.76 0.78 0.88 0.78
Taylor rule 0.57 0.53 0.72 0.53
Direct vote 0.60 0.53 0.75 0.53
Ablations
Macro (fitted)0.49 † 0.50 0.69 0.50
Retrieved text−0.080.56 0.69 0.62
Static query set−0.050.59 0.78 0.62
PBI (all)0.68 0.69 0.88 0.69
PBI (voting only) 0.70 0.72 0.91 0.72
PBI (chair only) 0.68 0.69 0.88 0.69
Table 1: All methods on both validations over the 2022–25
window. Tracking is Kendall’sτrelative to the realized per-
meeting move; the three walk-forward classification accu-
racies are 3-class hike/hold/cut plushike/restandmove/rest
one-vs-rest detection;†the fitted macro model has no unsu-
pervisedlevel,soitsτusesitsout-of-samplepredictedmove.
The PBI does not beat persistence on raw accuracy (0.69
vs.0.78), though persistence is wrong at every pivot out of
a regime by construction. At the seven decision changes in
the evaluation window it scores0.00and the PBI0.29. The
PBI’s residual deficit is concentrated entirely in cuts (0/6).
The PBI conditioned on the meeting’s decision is shown in
Figure 4b: the level separates cuts from holds only partially,
thoughnotenoughforthewalk-forwardclassifiertoevercall
a cut.
The index leads the rate level.Sliding the index forward
kmeetingsraisesits rank correlation with the funds-rate
level,fromτ= 0.42contemporaneouslytoτ= 0.84atk=8
(≈3 quarters; see Figure 4d). The lead is significant (block-
bootstrap95%CI[0.15,0.89]),andthePBIleadstherealized
rate better than a CPI-only baseline (paired difference 95%
CI[0.05,0.49]). That is, the members’ aggregated public
language – as picked up by the personas – turns hawkish or
dovish roughly three quarters before the policy rate arrives
at the corresponding level.
7 Discussion
We built a speaker-attributed, temporally-resolved corpus of
FOMC communications (24,333chunks,2006–2026, sev-
enteen of nineteen sitting members) and used it to con-
struct retrieval-augmented personas of the committee. The
personas pass both likeness checks –identifiabilitybetween
personas anddetectabilitywithin each – and, when queried,
recover an external reputational hawk–dove ordering (τ=
0.63). Conditioned on each meeting’s market environment
and aggregated over the committee, they form the persona-
basedindex(PBI),which–underastrictpoint-in-timecorpus
– reconstructs the2018–2025rate cycle (τ= 0.68out-of-
sample), classifies per-meeting hike/hold/cut at0.69against
a0.47baserate,and,mostdistinctively,leadsthefunds-rate
level by roughly three quarters (τrising0.42→0.84when
slidforward).Asfarasweareawarethisisthefirstquantita-
tivedemonstrationthattheoutputsofacollectionofpersonas
can track a time-varying system-level covariate.
Limitations.Several properties of the setting bound these
results. Committee members share an industry-specific
rhetoric, have overlapping backgrounds, and rarely dissent
formally, and per-member corpora span83to9,855chunks
– all of which could limit identifiability and detectability.
Thepersonasnonethelessdemonstratehighlikenessonboth
axes.
The corpora draw exclusively on official public sources
(speeches, testimony, meeting transcripts, and, for chairs,
press conferences). This keeps document types uniform but
omits potentially informative material such as media inter-
views, social media, and prior academic writing.
The evaluation window is also temporally bounded. The
committee operated under a single chair (Jerome Powell,
February 2018 through May 2026) for the entire backtest,
and the out-of-sample window contains only32meetings;
communication norms under new leadership may shift how
well personas built on this record represent their members.
Separately, the base model’s training data ends in late 2023,
so early “predictions” could partially reflect information al-
ready in the weights; on the post-cutoff meetings alone the
classifier matches but does not beat the hold-heavy base
rate, while the lead profile persists. Two further robustness
notes:withembargoedtranscriptsnaivelydatedatthemeet-
ing(i.e.,nopoint-in-timefilter)accuracyinflatesto0.75,and
the committee mean is robust to the choice of aggregation
(Appendix C).
Acknowledgingtheselimitations,thesynthesisofpersona-
based and economic modeling in the PBI both tracks the
aggregatepolicydecisionsoftheFOMCandholdspredictive
value – the index regularly leads the federal funds target
rate (Figure 4a,d) – for decisions that are among the most
scrutinized in the global economy.
Future WorkThree directions follow directly. (i) The
PBI’s honest boundary is cut-versus-hold: a recalibration
cutandahold-at-restrictivearestance-equivalentonasingle
hawk–dove axis, so a second, “easing-urgency” dimension
learned the same way could separate the easing turns the
single axis collapses. (ii) The briefingc(t) is a point-in-time
snapshot. Conditioning on the recent macro trajectory could
supplythedirectionalsignalalevelalonewithholds.(iii)Be-
cause the twins are the present committee, the contributing
roster thins historically (6 of∼12 voters in 2018, rising to
16 by 2025); twins of former members, built from the same
pipeline, would extend the backtest.
Reproducibility statement.All scripts for the data col-
lection and experiments are public: code at github.com/
helivan-research/fomc-personas, and the corpus (with pre-
computed embeddings) at huggingface.co/datasets/helivan/
fomc-personas. A live version of the index, updated as new
statements are published, is served at federalreserve.ai.

References
Aher, G. V.; Arriaga, R. I.; and Kalai, A. T. 2023. Using
Large Language Models to Simulate Multiple Humans and
ReplicateHumanSubjectStudies. InProceedingsofthe40th
International Conference on Machine Learning (ICML).
Argyle, L. P.; Busby, E. C.; Fulda, N.; Gubler, J. R.; Ryt-
ting, C.; and Wingate, D. 2023. Out of One, Many: Using
Language Models to Simulate Human Samples.Political
Analysis, 31(3): 337–351.
Bordo, M. D.; and Istrefi, K. 2023. Perceived FOMC: The
MakingofHawks,DovesandSwingers.JournalofMonetary
Economics, 136: 125–143.
Brand, J.; Israeli, A.; and Ngwe, D. 2023. Using LLMs for
Market Research. Working Paper 23-062, Harvard Business
School.
Chen,J.;Wang,X.;Xu,R.;etal.2024. FromPersonatoPer-
sonalization: A Survey on Role-Playing Language Agents.
ArXiv:2404.18231, arXiv:2404.18231.
Dillion, D.; Tandon, N.; Gu, Y.; and Gray, K. 2023. Can AI
Language Models Replace Human Participants?Trends in
Cognitive Sciences, 27(7): 597–600.
Federal Reserve Bank of St. Louis. 2025. Federal Re-
serve Economic Data (FRED). https://fred.stlouisfed.org.
Database; accessed 2026.
Gorodnichenko, Y.; Pham, T.; and Talavera, O. 2023. The
Voice of Monetary Policy.American Economic Review,
113(2): 548–584.
Hansen, A. L.; and Kazinnik, S. 2023. Can ChatGPT Deci-
pher Fedspeak? Technical report, Federal Reserve Bank of
Richmond. SSRN Working Paper 4399406.
Hansen, S.; and McMahon, M. 2016. Shocking Language:
Understanding the Macroeconomic Effects of Central Bank
Communication.Journal of International Economics, 99:
S114–S133.
Hansen,S.;McMahon,M.;andPrat,A.2018. Transparency
and Deliberation within the FOMC: A Computational Lin-
guistics Approach.The Quarterly Journal of Economics,
133(2): 801–870.
Helm, H.; Chen, T.; McGuinness, H.; Lee, P.; Duderstadt,
B.; and Priebe, C. E. 2025. Toward a Digital Twin of U.S.
Congress. ArXiv:2505.00006, arXiv:2505.00006.
Helm, H.; and Priebe, C. E. 2026. When Prompt Perturba-
tions Break Your A/B Test: A Valid Statistical Test for Gen-
erative Surveying. ArXiv:2605.27463, arXiv:2605.27463.
Horton, J. J.; Filippas, A.; and Manning, B. S. 2023. Large
LanguageModelsasSimulatedEconomicAgents:WhatCan
WeLearnfromHomoSilicus? NBERWorkingPaper31122,
National Bureau of Economic Research.
Istrefi, K. 2019. In Fed Watchers’ Eyes: Hawks, Doves and
Monetary Policy. Working Paper 725, Banque de France.
Kanganis, A.; and Keith, K. A. 2025. Op-Fed: Opin-
ion, Stance, and Monetary Policy Annotations on FOMC
Transcripts Using Active Learning. ArXiv:2509.13539,
arXiv:2509.13539.
Koaik, F.; Gupta, A.; and Sheikh, F. R. 2026. LLM-
Powered Social Digital Twins: A Framework for Simulat-
ingPopulationBehavioralResponsetoPolicyInterventions.
ArXiv:2601.06111, arXiv:2601.06111.
Kuttner,K.N.2001. MonetaryPolicySurprisesandInterest
Rates:EvidencefromtheFedFundsFuturesMarket.Journal
of Monetary Economics, 47(3): 523–544.
Li,R.;Xia,H.;Yuan,X.;Dong,Q.;Sha,L.;Li,W.;andSui,
Z.2025. HowFarareLLMsfromBeingOurDigitalTwins?
ABenchmarkforPersona-BasedBehaviorChainSimulation.
InFindingsoftheAssociationforComputationalLinguistics:
ACL 2025.
Lucca, D. O.; and Trebbi, F. 2009. Measuring Central Bank
Communication:AnAutomatedApproachwithApplication
toFOMCStatements.NBERWorkingPaper15367,National
Bureau of Economic Research.
McGuinness, H.; Wang, T.; Priebe, C. E.; and Helm, H.
2024. Investigating Social Alignment via Mirroring in a
SystemofInteractingLanguageModels.ArXiv:2412.06834,
arXiv:2412.06834.
National Academies of Sciences, Engineering, and
Medicine. 2024.Foundational Research Gaps and Future
DirectionsforDigitalTwins. Washington,DC:TheNational
Academies Press.
OpenAI. 2024a. GPT-4o mini: Advancing Cost-
Efficient Intelligence. https://openai.com/index/gpt-4o-
mini-advancing-cost-efficient-intelligence/. Accessed2026-
06-16.
OpenAI.2024b. NewEmbeddingModelsandAPIUpdates.
https://openai.com/index/new-embedding-models-and-api-
updates/. Introducestext-embedding-3-large;
accessed 2026-06-14.
Park, J. S.; O’Brien, J. C.; Cai, C. J.; Morris, M. R.; Liang,
P.;andBernstein,M.S.2023. GenerativeAgents:Interactive
Simulacra of Human Behavior. InProceedings of the 36th
Annual ACM Symposium on User Interface Software and
Technology (UIST).
Park, J. S.; Zou, C. Q.; Shaw, A.; Hill, B. M.; Cai, C.;
Morris, M. R.; Willer, R.; Liang, P.; and Bernstein, M. S.
2024. Generative Agent Simulations of 1,000 People.
ArXiv:2411.10109, arXiv:2411.10109.
Peskoff,D.;Visokay,A.;Schulhoff,S.;Wachspress,B.;Blin-
der, A.; and Stewart, B. M. 2023. GPT Deciphering Fed-
speak: Quantifying Dissent Among Hawks and Doves. In
Findings of the Association for Computational Linguistics:
EMNLP 2023, 6529–6539.
Picault,M.;andRenault,T.2017.WordsAreNotAllCreated
Equal:ANewMeasureofECBCommunication.Journalof
International Money and Finance, 79: 136–156.
Santurkar,S.;Durmus,E.;Ladhak,F.;Lee,C.;Liang,P.;and
Hashimoto,T.2023. WhoseOpinionsDoLanguageModels
Reflect?InProceedingsofthe40thInternationalConference
on Machine Learning (ICML).
Shah, A.; Paturi, S.; and Chava, S. 2023. Trillion Dollar
Words: A New Financial Dataset, Task & Market Analysis.
InProceedingsofthe61stAnnualMeetingoftheAssociation
for Computational Linguistics (ACL), 6664–6679.

Shanahan, M.; McDonell, K.; and Reynolds, L. 2023. Role
Play with Large Language Models.Nature, 623: 493–498.
Shapiro, A. H.; and Wilson, D. J. 2022. Taking the Fed
at its Word: A New Approach to Estimating Central Bank
Objectives Using Text Analysis.The Review of Economic
Studies, 89(5): 2768–2805.
Taylor,J.B.1993. DiscretionversusPolicyRulesinPractice.
Carnegie-RochesterConferenceSeriesonPublicPolicy,39:
195–214.
Tobback, E.; Nardelli, S.; and Martens, D. 2017. Between
HawksandDoves:MeasuringCentralBankCommunication.
ECB Working Paper 2085, European Central Bank.
Toubia, O.; Gui, G. Z.; Peng, T.; Merlau, D. J.; Li, A.; and
Chen,H.2025.Twin-2K-500:ADataSetforBuildingDigital
Twins of over 2,000 People Based on Their Answers to over
500 Questions.Marketing Science, 44(6): 1446–1455.
Tseng, Y.-M.; Huang, Y.-C.; Hsiao, T.-Y.; Chen, W.-L.;
Huang, C.-W.; Meng, Y.; and Chen, Y.-N. 2024. Two Tales
of Persona in LLMs: A Survey of Role-Playing and Person-
alization. InFindings of the Association for Computational
Linguistics: EMNLP 2024, 16612–16631.
Wong, A.; Hallmark, N.; and Galvao, A. 2023. Bloomberg
Economics Fedspeak: Towards a High-Frequency Fed Sen-
timent Index. Technical report, Bloomberg Economics.
Yeykelis, L.; Pichai, K.; Cummings, J. J.; and Reeves, B.
2024. Using Large Language Models to Create AI Personas
for Replication, Generalization and Prediction of Media Ef-
fects:AnEmpiricalTestof133PublishedExperimentalRe-
search Findings. ArXiv:2408.16073, arXiv:2408.16073.

A Data Collection, Chunking, and Filtering
This appendix documents the corpus-construction pipeline end to end: the public sources, how documents are discovered, how
raw text is segmented into passages, how each passage is distilled into retrievable chunks, and the filters applied at each stage.
Allsourcesarepublic;noauthentication,paywalled,orprivatedataisused.EverychunkcarriestheURLandaccesstimestamp
of its source document.
Sources and discovery
A member’s documents are gathered from the public outlets appropriate to their office (Table 2). Board governors publish
through the Federal Reserve Board; regional presidents publish through their home bank and, uniformly, through the Bank for
International Settlements (BIS) speech archive; all FOMC participants appear in the meeting transcripts.
•Board speeches and testimony.The Board exposes machine-readable feeds (/json/ne-speeches.json,
/json/ne-testimony.json); we keep items whose speaker field matches the member’s name. Coverage begins
at the member’s first listed item and has no embargo.
•FOMCmeetingtranscripts.Verbatim transcriptsarereleasedonafive-yearlag.We enumeratemeetingsfromtheBoard’s
per-year historical index pages (regex overFOMCYYYYMMDDmeeting.pdf), download each meeting PDF, and segment
it into speaker-attributed turns. The transcripts in the corpus currently end in 2020 (the latest released under the five-year
embargo at collection time); this is the single largest constraint on recent coverage.
•FOMCpressconferences.Chair-attributedpress-conferencetranscriptscarrynoembargoandarediscoveredfromthesame
historical index (through 2020) and the FOMC calendar page (2021+).
•Regional-president speeches via BIS.The BIS archive (bis.org/cbspeeches) aggregates Federal Reserve regional
speeches in one uniform place. We resolve a president’s BIS author page (by constructing candidate slugs, then falling back
to paging the global index until a speech by that speaker appears) and collect every speech linked there. Because BIS is a
single uniform source, it is the most robust president channel and the one used to onboard presidents whose home-bank site
refuses programmatic access.
•Regional-bank home pages.For some presidents we additionally scrape the home bank’s speech repository. These are
heterogeneous: discovery is by rendered listing page or bysitemap.xml, with per-bank link and date patterns; bodies
come from the HTML article or, when too short, the linked PDF.
•Biographies.Asingleofficialbiographypermember(Boardorhome-bankpage,normalizedtoauniformregister)grounds
the persona’s system prompt; it carries no time dimension and is not part of the chunk corpus.
Source Applies to Embargo / bound
Board speeches & testimony (JSON feeds) Governors none
FOMC meeting transcripts (PDF) All participants 5-year lag
FOMC press conferences (PDF) Chairs none
BIS speech archive Regional presidents none
Regional-bank speech pages Some presidents none
Official biography All members static
Table 2: Public sources per office. The five-year transcript embargo is the binding limit on recent coverage; speeches and press
conferences are contemporaneous.
Passage segmentation
Each raw document is split into passages of at most6,000characters by a hierarchical splitter: paragraphs (double-newline
boundaries)areaccumulateduptothelimit,andanysingleparagraphexceedingthelimitisfurthersplitonsentenceboundaries.
Transcripts are first segmented into speaker turns and only the target member’s turns are retained (turns shorter than80
characters are dropped as procedural). This preserves argument-level context within a passage while bounding the size handed
to the extraction model.
Chunk extraction
Eachpassageisdistilledintozeroormorechunksbyastructured-outputLLMcall(gpt-4o-mini,8-waypassageparallelism).
Themodelisinstructedtoextractonlythespeaker’sownexpressedviews,ignoringproceduralremarksandpositionsattributed
to others, and to return, for each chunk, atopic(a noun phrase naming the subject), astance(one self-contained sentence
stating the position), and a verbatimquotegrounding it. Thestancesentence becomes the chunk’stext(the field that is
embedded and retrieved against), so retrieval and generation operate on normalized, self-contained positions rather than raw
prose. We then assign each chunk a coarsetheme(keyword bucketing of thetopic) and, for FOMC members, the as-of-date
is_votingandis_chairroles derived from the member and statement date (§3 of the main paper).

Filtering
Filters are applied at every stage. (i)Speaker attribution: Board items are kept only on a name match in the speaker field;
transcript turns only when attributed to the member; bank-page bodies only when the surname appears in the article head or
byline. (ii)Length: transcript turns below80characters and speech bodies below400characters are discarded, and overly short
HTMLbodiestriggeraPDFfallback.(iii)Date:itemsareboundedbelowbyaper-memberstartdateand,fortranscripts,bythe
five-year embargo. (iv)Deduplication: when a member’s twin is updated, incoming chunks whosetextalready exists in the
stored corpus are dropped, so re-runs are idempotent and additive. Every Fed source carriesprobabilitySpeaker= 1.0
(attributioniscertainfromspeakerheadersandverifiedpages);thefieldisretainedsothesameschemasupportslower-confidence
sources elsewhere.
Chunk schema
Each chunk written to the per-member parquet has the fields:text(the stance sentence, embedded and retrieved on),
topic,theme(one of six topic themes),quote(verbatim support),stance(equal totext),handle(member
name, the chunk’s member id),postedAt(date of the underlying document, the chunk’s time),is_voting,is_chair
(as-of-date roles derived from the member and date; null when undated),source(document type, e.g.fed_speech,
fomc_transcript),sourceId,postUrl,accessedAt,probabilitySpeaker, andembedding(1024-d
text-embedding-3-large, attached at persona-creation time).
Relation to existing FOMC datasets
Table 3 summarizes how our corpus differs from prior FOMC text resources along the dimensions discussed in §3 of the main
paper.
Member Multi- Stance Pre-comp.
Dataset -level source labels embed.
Trillion Dollar Words×✓ ✓×
Op-Fed✓×✓×
Hansen et al.✓× × ×
Lucca & Trebbi× ×✓×
Voice of Monetary Policy† ✓× × ×
Ours✓ ✓ ✓ ✓
Table 3: FOMC text resources compared along the dimensions our method requires.Member-level: text resolved to individual
FOMC members.Multi-source: two or more document types.Stance labels: carries stance/opinion annotation.Pre-comp.
embed.: ships pre-computed embeddings for retrieval.†Chair only, vocal-tone modality. Citations as in §3 of the main paper.
B Member Roster
Table 4 lists the onboarded members, their office, the channels collected, and the per-member collection start date. This start
dateissettoeachmember’searliestplausibleFederalReserveactivity:governorsandlong-servingpresidentsarecollectedfrom
as early as 2006, while members appointed in 2018 or later start near their tenure (an earlier start yields no additional chunks
undertheirname,sincethespeakerfilteradmitsonlytheirownstatements).Coverageisthereforecontinuousinaggregatefrom
2006 to the present, with depth tracking tenure.
Members not onboarded.Two of the nineteen sitting members are absent. Alberto Musalem (St. Louis) publishes his
presidential remarks only on his home-bank domain, which refuses automated access at the network level. We confirmed
this block is robust: the host is unreachable from the collection infrastructure (connection refused), from a server-side fetch
service(HTTP403),andfromathird-partyFederalReservemirror(connectionrefused),whileeveryotherFederalReserveand
aggregator host returns normally. The only externally reachable Musalem speeches predate his presidency (2015–2016, from
his tenure as a New York Fed executive) and were judged too stale and off-role to represent his current monetary-policy stance,
so he is excluded rather than onboarded with misleading data. Cheryl Venable (Atlanta, interim) has no published speech or
transcript record. Both gaps are external-availability limits, not methodological ones.
Coverageboundaries.Beyondthetwoabsentmembers,thecollectedrecordhasprincipledboundariesthatareworthstating
plainly, as they bound what each twin can represent. (i)The 2011–2017 historical gap is closed:the back-fill collects the
longest-serving members — a governor from 2006, the New York president from 2011, the chair from 2012, and Minneapolis
from 2016 — so aggregate coverage is continuous from 2006 to the present (Figure 1 of the main paper); recent appointees
simplyhavenopre-tenureFederalReserverecord,whichisapropertyoftheinstitution,notthecollection.(ii)Speechchannels
are wired per office.Governors come through the Board feeds; the New York president through BIS; six recently appointed

ID Member Office Channels From Chunks
1Jerome H. Powell Chair (Board) Sp, Te, Tr, PC 20129,855
2Kevin M. Warsh Governor Sp, Te, Tr 20061,716
3Philip N. Jefferson Governor Sp, Te, Tr 2018521
4Michelle W. Bowman Governor Sp, Te, Tr 20182,904
5Michael S. Barr Governor Sp, Te, Tr 20181,022
6Lisa D. Cook Governor Sp, Te, Tr 2018731
7Christopher J. Waller Governor Sp, Te, Tr 20181,201
8John C. Williams President, New York Tr, BIS 20112,337
9Mary C. Daly President, San Francisco Tr 2018566
10Neel Kashkari President, Minneapolis Tr 20161,144
11Thomas I. Barkin President, Richmond Tr 2018548
12Lorie K. Logan President, Dallas Tr, Bank 2022606
13Susan M. Collins President, Boston Tr, Bank 2022525
14Austan D. Goolsbee President, Chicago Tr, Bank 2023249
15Beth M. Hammack President, Cleveland Tr, Bank 2024180
16Jeffrey R. Schmid President, Kansas City Tr, Bank 202383
17Anna Paulson President, Philadelphia Tr, Bank 2025145
Table 4: Onboarded roster. Channels: Sp = Board speeches, Te = testimony, Tr = FOMC transcripts, PC = press conferences,
BIS = BIS speech archive, Bank = home-bank speeches. “From” is the collection start date, not necessarily the appointment
date; “Chunks” is the per-member corpus size. “ID” is the member id used in Figure 1b of the main paper. Three presidents
(Daly, Kashkari, Barkin) are currently transcript-only; their home-bank speech scrapers are a staged follow-up.
presidents through their home-bank pages. Three presidents (Daly, Kashkari, Barkin) have no wired speech channel, since the
BIS archive returns no speeches for them. They are therefore represented only by their FOMC transcript turns, which, under
the five-year embargo, currently end in 2020. The underlying speeches are public; direct-site scrapers for these members are a
clearly scoped follow-up, not a limit of the public record. We report this because it bounds the recent coverage of those twins
and, in turn, their weight in the post-2020 index.
C Methods and Additional Analyses
Models, embeddings, and metrics
Eachpersonaisf base (gpt-4o-mini,temperature0.2)promptedwithamember-specificFED_MEMBERbiographyandtop-k
retrievaloverthemember’sownchunks.Allembeddingsaretext-embedding-3-largeat1024dimensions.Identifiability
uses a shrinkage Fisher LDA for17-way leave-one-query-out attribution on the shared queries (§5 of the main paper); LDA’s
pooledwithin-classcovarianceabsorbsthesharedper-queryboilerplate.Detectabilityˆτ det isacross-validatedshrinkageFisher
LDA on generated-vs-real continuations, each pair truncated to equal word length;ˆτdet = 2 max(A,1−A)−1for balanced
accuracyA, with a real–real floor. The hawk–dove axis isnormalize(emb(hawk anchors)− emb(dove anchors)), fixed and
model-independent; we use a single fixed linear projection rather than a per-condition data-kernel embedding so conditions
remain comparable.
Identifiability: attribution confusion
Figure 5 is the full17-way leave-one-query-out attribution atk=3(shrinkage Fisher LDA on raw responses, row-normalized
so the diagonal is per-member recall; member ids as in Table 4). The diagonal dominates — every member clears chance —
and the off-diagonal mass is diffuse rather than blocky: misattributions spread across the committee rather than concentrating
on a single look-alike, so the residual confusion reflects shared committee language, not indistinguishable pairs. The chair and
centrist governors carry the lightest diagonals (recall≈0.30), consistent with their role as consensus voices.
Detectability: % of message presented
Theseedfraction(howmuchoftheheld-outquoteisrevealed)setshowmuchthepersonamustgenerate,andthusitsdetectability
(Table 5,gpt-4o-mini,k=3): a short seed leaves more to generate and is more detectable, a long seed less; half is our
operatingpoint.Neitherlikenessaxisispredictedbycorpussize—thethinnesttwin(83chunks,Schmid)isthemostidentifiable,
anddetectabilityisuncorrelatedwithsize(Kendall’sτ(size,ˆτ det) = +0.23,p=0.21);theconsensusvoices(centristgovernors,
the New York president) are the least distinctive but still clear chance.
Query set: count and quality
We ask both how many queries are needed and which kind carries the signal. Count is not the lever: within the curated30-
questionset,thereputationalcorrelationsaturatesby∼15–20questions(Figure3eofthemainpaper).Forquerytype,wescore

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
predicted member id
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
true member id
0.0
0.1
0.2
0.3
0.4
0.5
0.6
row fraction
Figure 5: Identifiability attribution confusion (17-way leave-one-query-out, shrinkage Fisher LDA on raw responses,k=3),
row-normalized so the diagonal is per-member recall. Member ids as in Table 4.
a balanced pool of72spectrum-conditioned questions (12hawk–dove facets, the query generator) per facet (Figure 3f of the
main paper): per-facet discrimination ranges fromτ= 0.15to0.38, with the strongest facets probing disposition and priorities
(weight on labor slack vs. wage inflation, on financial-stability risk, on how restrictive to be) and the weakest probing timing
and tactics (recession-risk appetite, preemptive tightening, patience before cuts). Good queries ask what a member values, not
what the Committee should do next meeting.
The curated query set.The30monetary-policy questions used throughout (§5 of the main paper) are listed below.
1. Do you believe that the Federal Reserve should prioritize keeping inflation low over achieving maximum employment?
2. Do you believe that pursuing maximum employment should take precedence over maintaining price stability in the current economic
environment?
3. Do you believe that a temporary increase in inflation is acceptable if it leads to significant job growth?
4. Doyoubelievethattheoveralleconomichealthisbestservedbystabilizingpricesevenifitmeanshigherunemploymentratesintheshort
term?
5. Do you believe that the trade-off between inflation and unemployment justifies a more aggressive monetary policy approach?
6. Do you believe the Federal Reserve should prioritize reducing inflation below 2 percent even at the risk of higher unemployment?
7. Do you believe monetary policy should remain accommodative to support economic growth despite inflation readings above 2 percent?
8. Do you believe the Federal Reserve has the tools to effectively combat rising inflation without significantly hindering recovery efforts?
9. Do you believe maintaining a tolerable inflation rate above 2 percent could be beneficial for long-term economic stability?
10. Do you believe that current inflationary pressures warrant a preemptive increase in the federal funds rate to avoid long-term damage?
11. Do you believe the Federal Reserve should prioritize reducing inflation over maintaining low unemployment?
12. Do you believe that a temporary increase in unemployment is an acceptable trade-off for achieving long-term price stability?
13. Do you believe that the current inflationary environment justifies a more aggressive increase in the federal funds rate, even at the risk of
higher unemployment?
14. Do you believe that the benefits of keeping inflation in check outweigh the social costs of rising unemployment rates?
15. DoyoubelievethattheFederalReserveshouldadoptamoredovishstanceandfocusonsupportingemploymentdespitepersistentinflation?
16. Do you believe the Federal Reserve should raise interest rates now to preemptively combat potential inflationary pressures?
17. Do you believe that waiting to see actual signs of inflation before adjusting the federal funds rate is a prudent approach?

% revealedˆτ det
10% 0.55
25% 0.53
50% 0.23
75% 0.18
90% 0.20
Table 5: % of the held-out message revealed as the seed vs. detectability (ˆτdet,gpt-4o-mini,k=3): a shorter seed leaves
more to generate and is more detectable;50%is our operating point.
18. Do you believe that tightening monetary policy too early could stifle economic growth and recovery?
19. Do you believe that current economic indicators warrant a hawkish stance on interest rates to mitigate future inflation risks?
20. Do you believe that a dovish approach, focused on maintaining low rates, could be harmful if inflation expectations become embedded?
21. Do you believe that the current level of inflation justifies a more restrictive monetary policy approach?
22. Do you believe that maintaining a low federal funds rate is essential for promoting long-term economic growth?
23. Do you believe that rising wage pressures warrant a shift towards a more hawkish stance on interest rates?
24. Do you believe that the risks of an economic slowdown should caution the Federal Reserve against tightening policy too quickly?
25. Do you believe that addressing asset bubbles should take precedence over concerns about short-term inflation rates?
26. Do you believe that prioritizing financial stability over economic growth is essential for the long-term health of the economy?
27. Do you believe that maintaining a low federal funds rate is the best approach to stimulate growth in the current economic environment?
28. Doyoubelievethattherisksofinflationshouldbeweighedmoreheavilythanthepotentialforfinancialinstabilitywhensettingmonetary
policy?
29. Do you believe that a more aggressive tightening of monetary policy is necessary to prevent asset bubbles from forming in the current
market?
30. Do you believe that the Federal Reserve should adopt a wait-and-see approach regarding interest rate changes to gauge the effects on both
growth and financial stability?
Hawk and dove anchors.The fixed dove→hawk axis isu= [hawk− ddove, the difference of the mean embeddings of the
following hand-written anchor statements.Hawkish:
1. Inflation is too high and we must raise interest rates decisively to restore price stability.
2. The risk of entrenched inflation outweighs concerns about slowing growth; policy should stay restrictive.
3. We should tighten monetary policy and shrink the balance sheet to combat inflationary pressures.
4. Premature easing would be a serious mistake; we must keep rates higher for longer.
5. Maintaining credibility on inflation requires a firm, hawkish stance even at the cost of some employment.
Dovish:
1. We should cut interest rates to support employment and economic growth.
2. The labor market needs support; the risk of overtightening into a recession is significant.
3. With inflation falling we can afford to ease policy to protect jobs.
4. Accommodative monetary policy is warranted to sustain the recovery and maximize employment.
5. The greater danger now is doing too much and weakening the economy, so policy should be more dovish.
Generator robustness
The persona-based stance ordering is not an artifact of a single base model. Re-running the persona-based estimate with
ministral-8bin place ofgpt-4o-miniyields a closely agreeing member ordering across the17personas (Kendall
τ= 0.69, Figure 6).
Index: aggregation robustness
The committee index is the mean of member axis-positions. It is robust to that choice (Table 6): median, trimmed-mean, and
chair-weighted aggregations giveτ∈[0.64,0.69]for the level↔move correlation, with the mean within noise of the best on
both metrics, so we keep it.
D Limitations
We note the boundaries of the present study. Detectability is read through one embedder (text-embedding-3-large);
a stronger or weaker discriminator would shiftˆτdet, and we validate indistinguishability statistically rather than with a human
Turingtest.Stanceisvalidatedagainstasingle,tenure-averagedreputationalordering(inthetraditionofIstrefi2019;Bordoand
Istrefi 2023); a second source or a time-varying ground truth would strengthen it, as would testing robustness to semantically-
equivalentqueryparaphrases(HelmandPriebe2026)andtothechoiceofhawk–doveanchors.Hawk–doveisasingleaxis,and

hawk dove
gpt-4o-mini rank
hawk
dove
ministral-8b rank
= 0.69
Figure6:Generatorrobustness:thepersona-basedmemberordering(k=3)undertwobasemodels,gpt-4o-mini(horizontal)
vs.ministral-8b(vertical). Points on the dashed diagonal agree (Kendallτ= 0.69).
Aggregatorτ(2022–25) OOS 3-class acc
mean 0.68 0.69
median 0.64 0.62
trimmed0.690.69
chair×20.680.72
chair×30.68 0.69
Table 6: Index aggregation robustness (point-in-time corpus, pure-relevance retrieval). The simple mean is within noise of the
best on both metrics.
the cut-vs-hold boundary suggests a second (“easing-urgency”) dimension. The index uses latest-release rather than real-time
(vintage) macro data, so the briefingc(t) can reflect reference months whose official releases postdate the meeting by a few
weeks.Residualgeneratorknowledgeofrealizedoutcomesisquantifiedratherthaneliminated:onpost-training-cutoffmeetings
the walk-forward classifier matches but does not beat the hold-heavy base rate, while the level-lead profile persists (§6 of the
main paper); the live index accumulates contamination-free meetings going forward. Decision-relevant power concentrates in
the well-covered2022–2025window. These are scoped limitations, not method failures, and each has a concrete next step.
