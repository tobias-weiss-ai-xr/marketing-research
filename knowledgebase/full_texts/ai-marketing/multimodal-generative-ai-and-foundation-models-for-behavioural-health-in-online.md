---
title: Multimodal Generative AI and Foundation Models for Behavioural Health in Online Gambling
url: https://arxiv.org/abs/2503.03752
category: ai-marketing
subcategory: review
date: 2025-01
venue: arXiv (Cornell University)
authors:
- Konrad Samsel
- Mohammad Noaeen
- Neil Seeman
source: arxiv
pdf_url: https://arxiv.org/pdf/2503.03752
pages: 17
chars: 101560
fetched_at: '2026-11-08T13:19:21+00:00'
kb_version: 1
---

# Multimodal Generative AI and Foundation Models for Behavioural Health in Online Gambling

Multimodal Generative AI and Foundation Models for Behavioural
Health in Online Gambling
Konrad Samsela,∗, Mohammad Noaeena,∗, Neil Seemana,b, Karim Keshavjeea, Li-Jia Lic and
Zahra Shakeria,d,e,∗∗
aInstitute of Health Policy, Management and Evaluation, Dalla Lana School of Public Health, University of Toronto, Toronto, Ontario, Canada
bMassey College, University of Toronto, Toronto, Ontario, Canada
cLiveX AI, San Francisco California, United States
dSchwartz Reisman Institute, University of Toronto, Toronto, Ontario, Canada
eFaculty of Information, University of Toronto, Toronto, Ontario, Canada
ARTICLE INFO
Keywords:
generative AI
online gambling
behavioral health
multimodal AI
digital addiction
ABSTRACT
Online gambling platforms have transformed the gambling landscape, offering unprecedented acces-
sibility and personalized experiences. However, these same characteristics have increased the risk of
gambling-relatedharm,affectingindividuals,families,andcommunities.Structuralfactors,including
targeted marketing, shifting social norms, and gaps in regulation, further complicate the challenge.
Thisnarrativereviewexamineshowartificialintelligence,particularlymultimodalgenerativemodels
and foundation technologies, can address these issues by supporting prevention, early identification,
and harm-reduction efforts. We detail applications such as synthetic data generation to overcome re-
searchbarriers,customizedinterventionstoguidesaferbehaviors,gamifiedtoolstosupportrecovery,
and scenario modeling to inform effective policies. Throughout, we emphasize the importance of
safeguarding privacy and ensuring that technological advances are responsibly aligned with public
health objectives.
1. Introduction
The advent of in-person electronic gambling machines
(EGMs) introduced immersive experiences for players, al-
lowing wagers to be placed as rapidly as once every 2.5
seconds (Dowling, Smith and Thomas, 2005). These prin-
ciples now extend to online gambling, where fast-paced
digital platforms heighten the risk of behavioral addiction
and related harms (Gainsbury, 2015). This escalation is
facilitated by the unprecedented accessibility and person-
alized interfaces of many gambling sites, factors that can
furtherexacerbatepublichealthchallengestiedtodisordered
gambling (Gainsbury, 2015).
Online gambling has become a major global concern,
propelledbyrapidtechnologicalgrowthandevolvingsocial
norms. In 2023, the worldwide online gambling market
was valued at $92.9 billion and is projected to grow at
a compound annual rate of 11.7% to reach $145.6 billion
by 2028 (Market Research Report, 2023). Younger popu-
lations appear especially drawn to digital platforms, with
reports indicating that nearly 50% of gamblers aged 18–
34 prefer online options over traditional venues (National
Gambling Association, 2022). This surge has an escalating
publichealthtoll,asanestimated1–3%ofadultsworldwide
experiencedisorderedgambling,affectingtensofmillionsof
individuals (World Health Organization, 2019). The wider
societal costs are likewise striking. In the United States,
gambling-related problems are estimated to cost $6 billion
peryearinhealthcare,criminaljustice,andlostproductivity
∗These authors contributed equally to this work.
∗∗Corresponding author
ORCID(s):
(Smith and Doe, 2022), while the United Kingdom, where
0.7% of adults are classified as problem gamblers, sees
a related societal expense exceeding £1.2 billion annually
(Gambling Commission, 2021).
Growth in online gambling stems not only from tech-
nological advances but also from changes in social norms
and regulatory environments, creating novel challenges for
public health practitioners. While online offerings parallel
in-person betting in terms of game types and prizes, they
possess distinctive features argued to amplify their appeal
(Hubert and Griffiths, 2018). Surveys point to constant ac-
cessibility, anonymity, and mobile integration as influential
drivers of engagement (Hubert and Griffiths, 2018; Columb
and O’Gara, 2018), while user-friendly financial transac-
tions and immersive interfaces may further intensify addic-
tive tendencies (Gainsbury, 2015). Gambling behaviors can
spanacontinuumfromrecreationaltoat-risktoproblematic
(Latvala, Lintonen and Konu, 2019), suggesting a need for
proactiveinterventions,suchasuserfeedback,limit-setting,
self-exclusion measures, and mental health support, to miti-
gate escalation (Rodda, 2022).
Data analytics and artificial intelligence (AI) present in-
novative avenues for tackling these issues. Past research has
examined AI-driven methods for detecting risky behaviors
(Auer and Griffiths, 2023b) and supporting in-game limit-
setting (Auer and Griffiths, 2022). Lessons from AI appli-
cations in patient care, such as psychiatric referral manage-
ment (Habicht, Viswanathan, Carrington, Hauser, Harper
andRollwage,2024)andpersonalizedtreatment(D’Alfonso,
2020), indicate how similar frameworks might be adapted
to address online gambling addictions. Nonetheless, AI can
also aggravate negative outcomes if misapplied. Operators
Konrad Samsel et al.:Preprint submitted to Elsevier Page 1 of 17
arXiv:2503.03752v1  [cs.CY]  24 Jan 2025

Generative AI for Gambling Behavior Health
increasinglyleverageadvanceddataanalyticsandriskman-
agement solutions to make platforms appear more reward-
ing, which can inadvertently deepen gambling-related harm
(Tyler,Akerlof,Allegra,Arnold,Canino,Doornenbal,Gold-
stein,BudtzPedersenandSutherland,2023).Theunchecked
personalization behind these immersive environments risks
creating cycles of overexposure and escalating problematic
behaviors.
Multimodal Generative AI and foundation models offer
a new frontier for addressing these multifaceted challenges.
Throughreal-timeanalytics,personalizedinterventions,and
comprehensivepolicysimulations,theseemergingtechnolo-
gies hold potential for improving early detection and harm
reduction in online gambling. However, their responsible
deployment requires robust governance to avoid exacerbat-
ing existing harms or introducing new risks to vulnerable
populations.Inthisnarrativereview,wesynthesizethecon-
textsunderwhichgambling-relatedaddictivebehaviorsarise
and discuss how advanced AI technologies may strengthen
primary prevention, early screening, and addiction manage-
ment in online gambling. We also highlight ethical consid-
erations and oversight mechanisms needed to ensure these
innovations align with public health goals. Finally, we pro-
poseconcretestrategiesforachievingaparadigmshiftinAI-
driven harm reduction and detail a set of potentially high-
impact applications enabled by multimodal generative AI,
while underscoring the core challenges, ethical, technical,
and organizational, that must be addressed to realize their
full promise.
2. Understanding Problem Gambling
Problemgambling,alsoreferredtoaspathologicalgam-
bling or gambling disorder, is a behavioural addiction char-
acterized by 'frequent, repeated episodes of gambling that
dominatethepatient’slifetothedetrimentofsocial,occupa-
tional,material,andfamilyvaluesandcommitments '(World
HealthOrganization,2016).Thoughstandardizeddiagnostic
criteria are available, the condition is often underdiagnosed
duetothelowproportionofindividualsexperiencingharm-
ful effects who are willing to seek support (Lupo, Vitale,
Carriero, Calabrò, Imperiale, Ercolani, Filippini, Santoro,
Carvello, Rizzo et al., 2023). It has been estimated that
around 71% of those with problematic gambling have never
sought treatment for their condition (Suurvali, Hodgins,
Toneatto and Cunningham, 2008). Problematic gambling
behaviour, if left untreated, can be associated with harms
including bankruptcy, housing instability, and worsening
mental health (Latvala et al., 2019). In some cases, problem
gambling can also impair judgment and decision-making
abilities, leading to more impulsive and risky behaviours
(Vestergaard,Ulrichsen,Dahl,MarcussenandChristiansen,
2023).Importantly,thenegativeimpactsassociatedwiththis
conditioncanextendbeyondindividuals,oftenalsoaffecting
those around them (Tulloch, Hing, Browne, Rockloff and
Hilbrecht, 2021). These wider harms can include increased
household financial strain, relationship breakdowns, emo-
tionaldistressamongaffectedfamilymembers,andanover-
all decrease in one’s quality of life (Latvala et al., 2019).
Recently, Internet gaming disorder (IGD) and problem-
atic Internet use have been identified as conditions asso-
ciated with problematic gambling (Karlsson, Broman and
Håkansson, 2019). While it has been proposed that these
behaviouraladdictionsmaysharesimilarriskfactors,further
workisneededtodeterminewhetheranycausalassociations
exist between them (Karlsson et al., 2019). The distinction
between gaming and gambling is becoming increasingly
blurred, with some games incorporating gambling-like el-
ements, and gambling sites increasingly 'gamifying' core
features of their platforms (Wu, Sescousse, Yu, Clark and
Li, 2018; Raneri, Montag, Rozgonjuk, Satel and Pontes,
2022). The recent classification of IGD in the Fifth Edi-
tion of The Diagnostic and Statistical Manual of Mental
Illnesses(DSM-V)hashelpedinestablishingseveraldistinc-
tions between disordered gambling and gaming (Darvesh,
Radhakrishnan,Lachance,Nincic,Sharpe,Ghassemi,Straus
andTricco,2020).Differentiatingbetweenthesebehavioural
addictions can also assist in the development of tailored
approaches to mitigating their severity and impact. While
problematic gamblers tend to experience more financial-
related harms, IGD is more often characterized by physical
and health-related harms associated with recurrent gaming
behaviour (Delfabbro, King and Carey, 2021).
Approaches to aid in the screening of problem gam-
bling have previously been proposed, and serve as tools to
identify individuals requiring further intervention or diag-
nosticassessment.Thesecriteriatypicallyconsistofreadily
quantifiable factors such as the frequency and duration of
gamblingactivitiesandtheamountofmoneyspentongam-
bling (Gooding, 2023; Turner, Elton-Marshall, Shi, Wiebe,
Boak, van der Maas and Mann, 2018; Williams, Shaw,
Belanger, Christensen, el Guebaly, Hodgins, McGrath and
Stevens, 2023; Auer and Griffiths, 2023b). One example of
a screening tool is the Problem and Pathological Gambling
Measure (PPGM-R), a 15-item self-reported assessment for
classifying the risk of gambling disorder (Gooding, 2023).
In tandem with these screening tools, knowledge of high-
risk demographics, gender-based differences, and other be-
haviouralfactorsmaybeeffectiveininformingpublichealth
approaches to screening and early management.
2.1. Demographic Risk Factors
The risk of engaging in gambling behaviour has previ-
ously been associated with demographic factors including
age, initial age of gambling, and gender. These factors are
situated within a larger scope of social, behavioural, and
environmental determinants (Figure 1). Understanding risk
factors associated with problem gambling is essential for
designing effective interventions and prevention strategies
tailored to specific populations.
Adolescents and younger adults represent a particularly
vulnerable population, being prone to engaging in risky
gambling behaviours during their formative years (Bastiani,
Konrad Samsel et al.:Preprint submitted to Elsevier Page 2 of 17

Generative AI for Gambling Behavior Health
Figure 1: Environmental determinants of online gambling and
associated data sources for research and prevention. The
determinants are classified into accessibility, socioeconomic
factors, regulatory environments, and commercial influences.
These determinants interact to shape online gambling behav-
iors and outcomes. The figure also maps relevant data sources,
including demographic surveys, public health records, and
behavioral datasets, to support research on these influences
and inform interventions aimed at reducing gambling-related
harms.
Russell and Newall, 2023; Rizzo, La Rosa, Commodari,
Alparone, Crescenzo, Yıldırım and Chirico, 2023). Ado-
lescents’ developing cognitive control systems may hinder
effective decision-making in these contexts, making them
more susceptible to developing problematic gambling be-
haviours (Emond and Griffiths, 2020). The age at which
adolescents begin to engage in these activities has been
suggested as a risk factor, with one cross-sectional study
finding severe gamblers were more likely to have started
gambling at an earlier age (Sharman, Murphy, Turner and
Roberts, 2019). The growing inclusion of gambling-related
elements in adolescent games, such as virtual wagers and
loot boxes, underscores the need for research into the im-
pacts of these early exposures to gambling tendencies in
later life. Among other demographic factors, the preva-
lence of problem gambling has historically been higher
in males (Williams, Leonard, Belanger, Christensen, El-
Guebaly, Hodgins, McGrath, Nicoll, Smith and Stevens,
2021;Turneretal.,2018;Claesdotter-KnutssonandHåkans-
son, 2021). Online gambling, specifically, carries a similar
demographic risk profile, with males and younger adults
more likely to engage with these platforms (Hing, Russell
and Browne, 2017).
2.2. Social, Behavioural, and Health Determinants
The co-occurrence of alcohol and substance use with
gambling behaviours significantly increases the risk of de-
veloping gambling addiction (Hilbrecht, Baxter, Abbott,
Binde, Clark, Hodgins, Manitowabi, Quilty, SpÅngberg,
Volberg, Walker and Williams, 2020). Prior research has
suggested that individuals who engage in excessive alcohol
consumption or substance use are more likely to exhibit
impulsivebehaviours,includingproblemgambling(Yauand
Potenza, 2015). The link between gambling and substance
use may stem from similar neurobiological and psycholog-
ical factors underlying these conditions (Pettorruso, Testa,
Granero,Martinotti,d’Andrea,diGiannantonio,Fernández-
Aranda,Mena-Moreno,Gómez-Peña,Moragasetal.,2021).
Thecombinationofalcoholorsubstanceusewithgambling
mayleadtoacycleofaddictivebehaviours,exacerbatingthe
development and severity of gambling addictions (Yau and
Potenza, 2015). The underlying mechanisms of addiction,
including neurobiological (Potenza, Sofuoglu, Carroll and
Rounsaville, 2011), emotional (Jauregui, Estévez and Ur-
biola, 2016), and structural factors (Barnes, Welte, Tidwell
and Hoffman, 2015), can predispose individuals to engage
inmultipleaddictivebehaviours,includinggambling.Addi-
tionally, individuals with addiction to other substances may
turntogamblingasanalternativeorcomplementaryformof
seeking pleasure or relief (Potenza et al., 2011), increasing
the likelihood of experiencing gambling-related problems
(Armoon, Griffiths, Fleury, Mohammadi and Bayat, 2023;
Barnes et al., 2015).
Problematic gambling has also been noted to co-occur
with mental health diagnoses such as depression, anxiety
disorders, and personality disorders (Hilbrecht et al., 2020).
The co-occurrence of mental health disorders and problem
gambling presents complex challenges for diagnosis and
treatment, emphasizing the importance of integrated ap-
proaches that address both gambling behaviours and under-
lying mental health conditions. In tandem, lower socioeco-
nomic status (SES) is known to be associated with the over-
all incidence of problem gambling (Williams et al., 2021,
2023), mental health and substance use (Lasserre, Imtiaz,
Roerecke, Heilig, Probst and Rehm, 2022). Interestingly,
an opposite association has been observed in some studies
of online gambling, where those with higher incomes and
educational levels may be more likely to partake in betting
activities and exhibit problematic behavioural tendencies
(Gainsbury, 2015). It has also been argued that these dif-
ferences between online and offline offerings may become
lesspronouncedasonlinegamblingplatformsbecomemore
well-known and easier to access (Gainsbury, 2015). By
extension,socialmobilityandchangesinSES,predictiveof
mentalhealth(BarakatandKonstantinidis,2023),presentan
interesting domain that may benefit from investigation in an
online gambling context.
Other determinants suggested for their relationship with
problematic gambling include financial literacy, family his-
tory of gambling, and access to health services. A previous
investigation found financial literacy to be associated with
gambling,withlowerlevelsoffinancialliteracycorrespond-
ing to an elevated risk of unhealthy gambling behaviours
(Wang, Yang and Xin, 2023a). Moreover, family history
of gambling has been proposed as an additional predictive
factor of addictive gambling behaviour (Williams et al.,
2023; Gooding, 2023). Former investigations have found
Konrad Samsel et al.:Preprint submitted to Elsevier Page 3 of 17

Generative AI for Gambling Behavior Health
that individuals self-reporting perceived problematic gam-
blingbehavioursweremorelikelytohaveafamilyhistoryof
gambling compared to those not reporting such behaviours
(Gooding, H., Williams and Williams, 2023). Structural
barriers to accessing relevant health services and a lack of
social support networks can also serve as risk factors for
the progression of this behavioural addiction (Dąbrowska,
Moskalewicz and Wieczorek, 2017).
2.3. Commercial Determinants
Commercial determinants of health present an inter-
esting aspect of study in the context of gambling pro-
motion and severity. Reflecting aspects such as the broad
commercial landscape (Reith and Wardle, 2022), regula-
tory environments (Engebø, Torsheim and Pallesen, 2021;
Turner,SinclairandMatheson,2023),accessibility(Russell,
Browne,Hing,Rockloff,Newall,Dowling,Merkouris,King,
Stevens,Salonen,Breen,Greer,Thorne,Visintin,Rawatand
Woo, 2023), product design (McAuliffe, Edson, Louder-
back, LaRaja and LaPlante, 2021), and broader economic
conditions (Olason, Hayer, Meyer and Brosowski, 2017),
these determinants are increasingly being recognized as
important drivers of gambling behaviour. Marketing strate-
gies,whichservetoincreaseawarenessandpositivelyshape
perceptions on gambling, can be argued to influence social
norms and help normalize engagement in these platforms
(Guillou-Landreat, Gallopel-Morvan, Lever, Le Goff and
Le Reste, 2021). Recent attention has also focused on the
role of celebrities and social media influencers in the ap-
peal of these platforms (Pitt, McCarthy, Randle, Daube
and Thomas, 2024). With this marketing often occurring
on digital social media platforms, the risk of adolescents
and youth being exposed to gambling messaging is also
heightened (Guillou-Landreat et al., 2021).
3. Online Gambling Characteristics
Developments in gambling offerings have introduced
novelmethodsofparticipation,suchasin-personEGMsand
internet-based games. As a ’continuous’ form of gambling
(Williams et al., 2021), EGMs are characterized by their
repetitive nature, which translates to a shorter recovery pe-
riod in between gambling engagement and reward (Harris,
Gous, de Wet and Griffiths, 2021). Moreover, the increased
prominence of auditory and visual stimuli commonly found
in these machines further promotes continued user engage-
ment (Shao, Read, Behrens and Rogers, 2013). Recently,
a natural policy experiment from Australia highlighted the
effects of EGM access restrictions on the prevalence of
gambling-related harms (Russell et al., 2023). Lower levels
of harm were associated with access restrictions (Russell
et al., 2023), highlighting the contributions of accessibility
ingamblingpreventionandmanagement.Unfortunately,the
ease of access to gambling activities has tended to increase
due to the emergence and worldwide growth of online gam-
bling.
Thegamblinglandscapehasundergonesignificanttrans-
formations in recent years, with the proliferation of online
gambling platforms contributing to shifts in gambling be-
haviour and overall prevalence rates of problematic gam-
bling behaviours (Marionneau, Ruohio and Karlsson, 2023;
EmondandGriffiths,2020;Elton-Marshall,Leatherdaleand
Turner, 2016; Miles, Rothschild, Åkesson and A., 2023;
Langham, Thorne, Browne, Donaldson, Rose and Rockloff,
2016).Thereisgrowingevidencethatonlinegamblersareat
a greater risk of experiencing problem gambling compared
to those who engage in offline gambling (Scholes-Balog
andHemphill,2012;Griffiths,Wardle,Orford,Sprostonand
Erens, 2021). Overall, the popularity, lack of restrictions,
and personalization among online offerings are among the
factors proposed to increase the likelihood of problem gam-
bling.
Increasing Popularity of Online Gambling. Online
gamblingofferings,includingonlinewagerplatforms,sports
gambling apps, and virtual slot machines, have witnessed
an increase in popularity, particularly among adolescents
(Emond and Griffiths, 2020; Gainsbury, 2015). Accord-
ing to a 2016 cross-sectional survey of 10,035 Canadian
adolescents, 41.6% of respondents reported engaging in
gambling activities within the prior three months (Elton-
Marshall et al., 2016). Moreover, based on survey data col-
lected using the Canadian Adolescent Gambling Inventory
(CAGI), it was estimated that 17.4% and 18.2% of those
whohadself-reportedengaginginonlinegamblingactivities
were classified at a 'high' and 'low to moderate' level of
gamblingseverity,respectively(Elton-Marshalletal.,2016).
Comparable estimates for youth who reported engaging in
offline gambling yielded estimates of 1.2% for'high' and
7.2% for 'low to moderate' severity (Elton-Marshall et al.,
2016). Online sports betting emerged as the most popular
formofonlinegamblingamongadolescents(Elton-Marshall
et al., 2016). From this same survey, simulated gambling
such as free online poker and gambling games on social
media were also prevalent among Canadian youth, with
approximately9%ofrespondentsreportingpastengagement
in these platforms (Elton-Marshall et al., 2016).
EaseofAccess. Onlinegamblingplatformshaveshaped
the gambling experience by providing unparalleled accessi-
bility to users (Ghelfi, Scattola, Giudici and Velasco, 2023;
Emond and Griffiths, 2020; Marionneau et al., 2023). In
contrast to traditional brick-and-mortar casinos, which in-
clude age restrictions and have limitations based on oper-
ating hours and physical proximity, online platforms allow
individuals to participate in gambling activities from the
comfort of their own homes or while on-the-go via mobile
devices (Hilbrecht et al., 2020; Favieri, Forte, Casagrande,
Dalpiaz, Riglioni and Langher, 2023; Allami, Williams,
Hodgins, Stevens, Shaw, el Guebaly, Christensen, McGrath
and Belanger, 2003). Consequently, individuals may find
themselves more inclined to participate in these activities
due to the accessibility afforded by online platforms (Mar-
ionneau et al., 2023).
Lack of Sufficient Age Restrictions.One concerning
aspect of online gambling platforms is the lack of stringent
Konrad Samsel et al.:Preprint submitted to Elsevier Page 4 of 17

Generative AI for Gambling Behavior Health
ageverificationmeasurescomparedtotraditionalbrick-and-
mortar casinos. While physical casinos typically enforce
strict age restrictions and require identification verification
to prevent underage gambling, online platforms may have
less robust age verification mechanisms in place (Bastiani
et al., 2023). This lax enforcement increases the risk of un-
derage individuals engaging in gambling activities, as they
maycircumventagerestrictionsandaccessonlinegambling
platforms without adequate age verification checks (Elton-
Marshall et al., 2016).
Personalization of Gambling Experience. Online
gambling platforms leverage sophisticated and personalized
data analytics to tailor gambling experiences to individual
preferences (Tyler et al., 2023). By analyzing user data and
behaviouralpatterns,theseplatformscancustomizethepre-
sentation of games, offers, and incentives to align with each
user’s interests and preferences (Marionneau et al., 2023;
Milesetal.,2023).Thispersonalizedapproachmayenhance
userengagementandimmersioninthegamblingexperience.
Moreover,integratingpersonalizedfeatures,suchastargeted
advertisements (Nixon, 2022) and recommendations (Sa-
hota,2024)basedonpastbehaviour,mayfurtherincentivize
individuals to continue gambling and increase their partic-
ipation in gambling activities, particularly when presented
with tailored incentives and stimuli that resonate with their
preferences.
Increased Intensity.Online gambling platforms facil-
itate a higher intensity, frequency, and prevalence of gam-
bling activities compared to traditional venue-based gam-
bling (Marionneau et al., 2023). Features such as unlimited
pay-to-play options, minimal wait times between bets, and
theavailabilityofmultiplegamblingoptionsmaycontribute
to the heightened intensity and frequency of online gam-
bling experiences. The absence of physical and frequency
constraints, and the seamless transition between different
gambling activities, enable individuals to engage in con-
tinuous and uninterrupted sessions, leading to increased
intensityandfrequencyofproblematicgamblingbehaviours
(Allami, Hodgins, Young, Brunelle, Currie, Dufour, Flores-
Pajot and Nadeau, 2021; Ghelfi et al., 2023). Compared to
othergamblingforms,theamountoftimebetweenbetplace-
mentandoutcomesismuchshorter,whichmayinfluencean
individual’s ability to manage impulsive tendencies (Ghelfi
et al., 2023; Hilbrecht et al., 2020; Calado and Griffiths,
2016).
Online gambling has evolved into a dynamic and highly
engaging ecosystem, designed to captivate and retain users.
For vulnerable groups such as adolescents, the combina-
tion of instant accessibility and hyper-personalization is
not merely appealing, it is dangerous. Addressing these
challenges requires more than regulation; it necessitates a
comprehensive understanding of the psychological drivers
andstructuralfactorsunderpinningthisdigitalphenomenon,
laying the groundwork for innovative and effective public
health interventions.
4. Artificial Intelligence Addressing Problem
Gambling
Artificial Intelligence holds significant promise for ad-
dressing the complex issue of problem gambling, but it also
raises key ethical questions regarding fairness and trans-
parency. This section draws on a diverse body of research
across several key areas—Detection and Prediction,Behav-
ioral Analysis and Risk Factors, AI for Intervention and
Prevention,EthicalandFairnessConsiderations ,Preventive
Strategies,and LimitationsinAIforProblemGambling —to
provide a broad synthesis of current knowledge and chal-
lenges in this evolving field.
4.1. Core Applications of AI in Problem Gambling
Detection and Prediction. A substantial portion of AI
research in problem gambling focuses on developing pre-
dictive models that flag at-risk individuals early. Studies
have explored diverse machine learning approaches, in-
cluding logistic regression, random forests, and artificial
neural networks, to analyze betting transactions, session
durations, and user correspondence with customer ser-
vice (Murch, Kairouz and French, 2024b; Smith, Peters
and Reiter, 2024; Jach, Probierz, Kozak, Stefański, Dz-
iczkowski, Hrabia, Juszczuk, Głowania, Wołek, Sznapka
etal.,2024;Murch,Kairouz,Dauphinais,Picard,Costesand
French, 2023; Murch, Kairouz and French, 2024a; Kairouz,
Costes, Murch, Doray-Demers, Carrier and Eroukmanoff,
2023; Percy, d’Avila Garcez, Dragičević, França, Slabaugh
and Weyde, 2016b; Percy, França, Dragičević and d’Avila
Garcez, 2016a; Finkenwirth, MacDonald, Deng, Lesch and
Clark, 2021; Percy, Garcez, Dragicevic and Sarkar, 2020;
Auer and Griffiths, 2023b). Some of these models have
shownlastingstabilityovermonths,withonlyminorthresh-
oldadjustmentsrequiredtomaintainaccuracy(Murchetal.,
2024a,b). In parallel, AI chatbots have been trialed to de-
liver cognitive behavioral therapies, offering a scalable way
to connect individuals experiencing gambling problems to
early support (Murch et al., 2024b). This trend toward auto-
mateddetectionandscreeningsuggestsabroadermovefrom
reactive to proactive healthcare strategies.
Behavioral Analysis and Risk Factors.Complementing
predictive algorithms, a growing body of research is dedi-
cated to understandingwhich behaviorsbest indicate risk.
Studies highlight that problem gamblers typically deposit
more frequently, lose more money per session, and exhibit
wider fluctuations in betting stakes (Emond and Griffiths,
2020;AuerandGriffiths,2023b;Ghaharian,Binesh,Soligo,
Golab and Abarbanel, 2024). Further, analyses of online
forumpostsandchatdatasuggestacorrelationbetweenhigh
community engagement and heightened problem gambling
behaviors(Smithetal.,2024).However,thesefindingsoften
remain correlational rather than strictly causal, reflecting
the multifaceted nature of gambling harm (Deng, Lesch
and Clark, 2019; Ghaharian, Abarbanel, Phung, Puranik,
Kraus, Feldman and Bernhard, 2023). Detecting behavioral
Konrad Samsel et al.:Preprint submitted to Elsevier Page 5 of 17

Generative AI for Gambling Behavior Health
patterns, such as sudden increases in deposit amounts, en-
ablesresearchersandoperatorstoimprovemachinelearning
models and create more accurate methods for identifying
individuals at risk.
AI for InterventionAI is also being leveraged forinter-
vention and monitoringefforts, extending beyond detection
to deliver personalized harm-reduction materials. Systems
canrecommendcontactinglocalhelplinesorprovideimme-
diate feedback that contextualizes a user’s actual gambling
behaviors in real-time (Murch et al., 2024b; Kairouz et al.,
2023; Sándor and Bakó, 2024; Kim, Park and Lee, 2024;
Peres,Fallacara,Manzoni,Castelli,Popovič,Rodriguesand
Estevens, 2021). Some platforms employ nudges to encour-
age self-imposed deposit limits, while others focus on more
specialized use cases, such as detecting match-fixing in
sports (Kim et al., 2024). These interventions align with a
broader push toward public health models that proactively
supportvulnerableindividuals.Incorporatingshort 'motiva-
tionalcheck-ins ',tailoredtoauser’srecentbettingtrajectory,
may strengthen engagement and steer players toward safer
gambling habits.
Ethical and Fairness Considerations.Despite these ad-
vances, the ethical dimensions of AI in problem gambling
remain complex. Concerns include the potential for algo-
rithms to perpetuate existing inequalities if, for instance,
theyperformpoorlyforspecificdemographicgroups(Murch
et al., 2024a; Percy et al., 2020; Ghaharian et al., 2024).
Debatesaroundfairness(equalityvs.equity)furthercompli-
catehowlimitedresources,suchasfreecounselingsessions,
are offered to different user segments (Murch et al., 2024a).
Moreover, critiques exist that AI interventions may serve
as 'powermechanisms 'shapingindividualsinto 'responsible
gamblers' according to industry-driven norms, rather than
addressingdeeperstructuralfactors(Ghaharianetal.,2024).
Transparent communication about algorithmic limitations
and an inclusive approach to model validation are crucial to
mitigate such risks.
Despite these challenges and limitations in current AI
applications for problem gambling, advancements ingen-
erative AI and foundation modelsoffer a promising new
direction.Byenablingmoreadaptive,scalable,andcontext-
aware solutions, these technologies can address gaps in
data quality, fairness, and personalized interventions. In the
followingsection,weillustratehowGenerativeAIandfoun-
dation models can push beyond traditional approaches, en-
hancingresearch,prevention,andtreatmentstrategieswhile
maintaining robust ethical safeguards.
4.2. Prevention Strategies Enabled by AI
AI-basedmethodsshowpotentialforreducingthepublic
health burden of problem gambling via a structured pre-
vention framework, mirroring general public health models
(Figure 2).
PrimaryPrevention. Primarypreventionaddressesroot
causesandbroadriskfactorsbeforeproblemsarise(Kisling
and Das, 2023). In online gambling, this includes regulat-
ing commercial determinants and raising public awareness
(Petry, Zajac, Ginley, Lemmens, Rumpf, Ko and Rehbein,
2018). Multimodal foundation models can analyze text,
images, and videos to evaluate marketing tactics—such as
how prominently responsible gambling messages appear
on advertisements or if certain imagery targets underage
audiences. These AI-driven audits foster accountability in
advertising, promote clear disclosures, and facilitate more
informed public dialogue. Automated sentiment analysis on
social media can further capture public perceptions, fueling
data-driveneffortstorefinepreventioncampaigns(Olawade,
Wada, David-Olawade, Kunonga, Abaire and Ling, 2023;
Lim and Schmälzle, 2023).
Secondary Prevention.Secondary prevention aims to
identify and support individuals or communities at higher
risk (Kisling and Das, 2023). Existing work leverages AI-
based analyses of user engagement, demographic data,
and environmental exposures to pinpoint groups suscep-
tible to developing problem gambling (Booth, Dowling,
Landon, Lubman, Merkouris and Rodda, 2021; Monreal-
Bartolomé, Barceló-Soler, García-Campayo, Bartolomé-
Moreno, Cortés-Montávez, Acon, Huertes, Lacasa, Crespo,
Lloret-Irles et al., 2023). Additional data sources, including
socialmediasentimentononlinegamblinganddemographic
trendsinsitevisits,bettingfrequencies,andwageramounts,
may help identify emerging patterns and inform tailored
community prevention efforts.
TertiaryPrevention. Forindividualsalreadyexhibiting
harmful gambling behavior, tertiary prevention focuses on
limitingfurtherdamageandfosteringrecovery(Kislingand
Das, 2023). Screening tools combining machine learning
and user engagement metrics (e.g., deposit variability, mul-
tiple visits) can predict self-exclusion or problematic gam-
bling with moderate-to-high accuracy (Finkenwirth et al.,
2021; Auer and Griffiths, 2023b; Murch et al., 2023). For
example,oneCanadianstudy(Finkenwirthetal.,2021)em-
ployed 20 betting variables related to gambling frequency,
intensity, and variability to develop predictive models for
self-exclusion, reporting area under the curve (AUC) val-
ues ranging from 0.65 to 0.76. Another Canadian inves-
tigation (Murch et al., 2023) combined user engagement
and demographic data, achieving AUC values as high as
0.84 when predicting high-risk behaviors. Such findings
have prompted platforms to consider offering personalized
feedback, deposit-limit reminders, or prompts to seek help
(Auer and Griffiths, 2023a). Meanwhile, AI-enabled chat-
bots or telehealth tools can deliver ongoing monitoring and
individualized guidance, further reducing barriers to care.
4.3. Limitations in AI for Problem Gambling
Many studies still rely on self-reported data, such as the
Problem Gambling Severity Index (PGSI), which is suscep-
tible to recall and social desirability biases (Murch et al.,
2024b). In addition, results based on a single online gam-
blingplatformmaynotcaptureauser’sbroadergamblingbe-
haviors, including land-based activities (Hopfgartner, Auer,
Konrad Samsel et al.:Preprint submitted to Elsevier Page 6 of 17

Generative AI for Gambling Behavior Health
Figure 2: Technological interventions in online gambling prevention. This figure highlights a population health approach with
three tiers: primary prevention focuses on risk factor analysis and public health promotion; secondary prevention includes early
detection of gambling behaviors and risk modeling; and tertiary prevention addresses treatment and recovery with in-game
interventions and relapse prevention technologies.
22
0000000000000
0.0
0.5
1.0
1.5
2.0
Intersection Size
Detection_and_Prediction
Behavioral_Analysis
Intervention_and_Monitoring
Prevention

01234
Set Size
Intersection size
Figure 3: UpSet plot illustrating the intersections of
requirement vectors across AI application categories.
The vectors are defined as follows: Detection and Pre-
diction (𝑉DP = {1 ,0,1,0,0,1,0,1}), Behavioral Analysis
(𝑉BA = {1 ,0,1,0,0,1,0,1}), Intervention and Monitor-
ing (𝑉IM = {1 ,0,1,0,0,0,0,0}), and Prevention (𝑉P =
{1,0,1,0,0,0,0,0}). A size of two for intersections indicates
that two requirements co-occur across two categories. A size
of zero means that no category combination includes those
specific requirements simultaneously. The plot highlights the
consistent inclusion of demographic (𝑟1) and behavioral deter-
minants (𝑟3), while systemic factors like policy engagement
(𝑟7) and fairness ( 𝑟8) are underrepresented, particularly in
Intervention and Monitoring and Prevention.
Helic and Griffiths, 2024). Sample sizes vary greatly, as
does the granularity of available data, leading to hetero-
geneous reporting standards and difficulties in comparing
resultsacrossdifferentoperatorsorjurisdictions.Evaluation
metrics also lack uniform definitions, with area under the
curve(AUC),accuracy,precision,andrecallfrequentlyused
but differently interpreted (Murch et al., 2024a). Further-
more, co-morbid conditions (e.g., mental health issues) and
personal financial factors often remain unaccounted for,
creating gaps in the contextual understanding of gambling
harm. As AI tools become more prevalent, the sector must
addresstheselimitationsthroughlarger,morerepresentative
datasets,cross-platformvalidation,andconsensusonrobust
evaluation protocols. Only then can AI fulfill its potential to
guideethical,data-drivenstrategiesformitigatinggambling
harm.
Moreover,toprovideabroadsynthesisofcurrentknowl-
edge and challenges in this evolving field, we propose a
structuredevaluationoftheextenttowhichkeyrequirements
areaddressedbyvariousAIapplicationcategoriesinonline
gambling. Let 𝑅 = {𝑟1, 𝑟2,… , 𝑟8} denote the set of eight
requirements identified from the literature, comprising:
1. 𝑟1: Demographic Risk Factors
2. 𝑟2: Social Determinants
3. 𝑟3: Behavioral Determinants
4. 𝑟4: Health Determinants
5. 𝑟5: Commercial Determinants
6. 𝑟6: Real-world Player Data Access
7. 𝑟7: Policy Engagement
8. 𝑟8: Algorithmic Fairness and Bias
Each AI application category—Detection and Predic-
tion, Behavioral Analysis, Intervention and Monitoring,
and Prevention—is represented by a binary vector𝑉𝐴 =
{𝑣1, 𝑣2,… , 𝑣8},where 𝑣𝑖=1 indicatesthattherequirement
𝑟𝑖 is addressed by the existing literature that focused on
this specific application, and𝑣𝑖 = 0indicates it is not. For
instance, the vector forDetection and Predictionis
𝑉DP={1 , 0, 1, 0, 0, 1, 0, 1},
reflecting its emphasis on demographic, behavioral, data
access,andfairness-orientedcomponents,whileplacingless
Konrad Samsel et al.:Preprint submitted to Elsevier Page 7 of 17

Generative AI for Gambling Behavior Health
priority on social and health determinants. Using these rep-
resentations,anUpSetplot(Figure3)visualizestheintersec-
tions of requirements across these categories. The analysis
reveals consistent attention to demographic and behavioral
determinants across all application categories, highlighting
theirfoundationalroleinaddressinggambling-relatedharm.
However, systemic considerations like Policy Engagement
(𝑟7) and Algorithmic Fairness and Bias (𝑟8) are underrep-
resented, particularly inIntervention and Monitoringand
Prevention.
The requirement mapping highlights critical patterns
acrossAIapplicationsinonlinegambling.Demographic( 𝑟1)
andbehavioral( 𝑟3)determinantsareconsistentlyprioritized,
reflecting their central role in identifying and addressing
problemgambling.However,systemicfactorssuchaspolicy
engagement (𝑟7) and algorithmic fairness (𝑟8) are often
overlooked, despite their importance for ensuring ethical
andregulatorycompliance.Moreover,whiledataaccess( 𝑟6)
is essential for Detection and Prediction and Behavioral
Analysis,itslimitedpresencein InterventionandMonitoring
and Prevention presents challenges in acquiring granular,
real-time data. Connecting application categories with their
requirementvectorsexposesthesegapsandenablestargeted,
ethically grounded advancements. The following section
elaborates on howGenerative AI and Foundation Models
can tackle these challenges and redefine harm-reduction
strategies.
5. The Potential of Generative AI in Problem
Gambling
This section presents six use cases illustrating how
Generative AI and Foundation Models provide integrative
and innovative solutions that bridge gaps across disciplines.
While previous AI efforts have made strides in addressing
these challenges, the advanced capabilities of these models
enable more adaptive, scalable, and precise approaches,
offering transformative potential for behavioral health and
gambling studies.
5.1. Synthetic Player Profiles
Real-world datasets for online gambling research are
notoriously difficult to access due to privacy, legal, and
proprietary constraints (Perrot, Hardouin, Thiabaud, Sail-
lard, Grall-Bronnec and Challet-Bouju, 2022; Jach et al.,
2024;Drosatos,Nalbadis,Arden-Close,Baines,Bolat,Vuil-
lier, Kostoulas, Wasowska, Bonello, Palles et al., 2018;
Hopfgartner et al., 2024; Gainsbury, 2015). As a result,
researchersandpractitionersfrequentlylackthescopetode-
veloprobustharm-reductionstrategies.Byemployinglarge-
scalefoundationmodelsandmoderngenerativeAI,itisnow
possible to craftSynthetic Player Profilesthat authentically
mirror real gambling behaviors without revealing any indi-
vidual’s identity (Harris, Parke and Griffiths, 2018).
Instead of relying on extensive real-world datasets,
which are often scarce or inaccessible, we propose using a
small anonymized or aggregated collection{𝐕1,… , 𝐕𝑚}to
calibrateafoundationmodel 𝑀 withparametersΘ.Through
a suitable loss function (e.g., negative log-likelihood),𝑀
approximates 𝑝(𝐕) by learning 𝑞Θ(𝐕) over key behavioral
features—such as deposit amounts, session durations, chat
text, and self-exclusion flags (Shanahan, McDonell and
Reynolds, 2023; Wang, Peng, Que, Liu, Zhou, Wu, Guo,
Gan, Ni, Yang et al., 2023b; Park, Goldstein, O’Gara, Chen
and Hendrycks, 2024). Once trained, 𝑀 produces syn-
thetic profiles𝐕∗ ∼ 𝑞Θ∗(𝐕), capturing realistic correlations
while preserving anonymity. Privacy mechanisms (e.g.,𝑘-
anonymity, differential privacy) and a rigorous validation
pipeline ensure that these synthetic records remain secure
and reliable. Thus, even with limited or partial real data,
researchers and operators can generate lifelike player tra-
jectories for testing new interventions, policy changes, or
predictivemodelswithoutexposingactualuserinformation.
Transformer-basedmodels,GenerativeAdversarialNet-
works (GAN) variants (Goodfellow, Pouget-Abadie, Mirza,
Xu, Warde-Farley, Ozair, Courville and Bengio, 2014), and
diffusion-based techniques (Yang, Zhang, Song, Hong, Xu,
Zhao,Zhang,CuiandYang,2023)canfurtherintegratetext
logs,biometricsignals,ormobiledata,creatingmultifaceted
syntheticrecords.Similarmethodshavebeenusedinhealth-
care (e.g., blending clinical notes and diagnostic images)
(Moor, Banerjee, Abad, Krumholz, Leskovec, Topol and
Rajpurkar,2023;GiuffrèandShung,2023)andfinance(e.g.,
simulating trader actions) (Zuo, Jiang and Zhou, 2024),
enabling research free of confidentiality breaches. By align-
ing generation strategies with the unique traits of regional
betting cultures, researchers can reveal subtle risk patterns
that standardized models might miss, opening opportunities
for more focused and relevant interventions.
Still, careful audits are vital to avoid biases or loss of
minority patterns (Perrot et al., 2022; Gainsbury, 2015).
Fairness checks and federated learning can guard original
datasets and validate that the synthetic data genuinely re-
flectsreal-worlddistributions(Drosatosetal.,2018).Mean-
while, cognitive architectures like CoALA (Sumers, Yao,
Narasimhan and Griffiths, 2023) and multi-agent simula-
tions (Park, O’Brien, Cai, Morris, Liang and Bernstein,
2023) allow these synthetic actors to'bet', respond to out-
comes, and deploy responsible gambling tools, all with
memory-drivenandadaptivebehavior.Researcherscaneven
simulate real-time chat threads or forum interactions (Gha-
harian et al., 2023; Moor et al., 2023) to capture conversa-
tional nuances, including emojis or full natural language.
By providing a safe yet realistic testing ground, Synthetic
PlayerProfilespavethewayforlarge-scaleexperimentation
in online gambling studies.
5.2. Responsible Marketing
The gambling industry increasingly deploys sophisti-
cated, AI-driven marketing strategies to attract and re-
tain customers, raising significant concerns about poten-
tial harms as a commercial determinant of health (Kshetri,
Konrad Samsel et al.:Preprint submitted to Elsevier Page 8 of 17

Generative AI for Gambling Behavior Health
100% UP TO $150
FIRST DEPOSIT BONUS FOR
SPORT BETTING
SIGN UP
Play Responsibly Ontario Only. Gambling can be addictive. Concerned? Contact Us at 1-866-123-456789
Bet  times, earn free spins or
bonus bets!
WINLOOM
Kick Off Your Bets with
Register an account on WinLoom
24/7 Support
Mobile Apps Available
1
2
3
4
5
6
7
8 10 11 12
14 15
9
13
1. Brand Recognition/Logo: Normalizes the brand for underage viewers.
2. Sports Tie-In: Links betting to popular sports, attracting teens.
3. Promotional Enticement: Portrays 'free money ', skewing risk perception.
4. Signup Bonus: Lowers cost barriers, tempting younger users.
5. Direct Call to Action ( 'Register an account '): Prompts impulsive sign-ups.
6. Immediate CTA ( 'Sign Up ' Button): Prompts hasty clicks instead of caution.
7. Loyalty Mechanic ( 'Bet 5 times '): Promotes repeated betting and addiction.
8. Legitimization (19+ Icon): Highlights the legal age, but easily ignored.
9. Compliance Obfuscation: Often unnoticed, minimal protection.
10. Brief Warning ( 'Gambling can be addictive '): Overshadowed by bold ads.
11. Aspirational Athlete Imagery: Glamorizes gambling via sports heroism.
12. 24/7 Support Badge: Encourages around-the-clock engagement.
13. Social Media Icons: Stay connected with tech-savvy youth.
14. App Store Icons: Remove access barriers, even for underage users.
15. Mobile Apps Prompt: Promotes on-the-go betting, increasing play risk.
Figure 4: Generative AI-Driven Analysis of Marketing Strate-
gies in Online Gambling Advertisement . An online sports-
betting advertisement analyzed using generative AI (GPT-4O).
Marketing strategies were detected from visual and textual
elements, annotated numerically, and listed below. Model
parameters: temperature = 0.2 , max tokens = 950 , top-p = 0.9 ,
frequency penalty = 0.2 , presence penalty = 0.0 .
Dwivedi,DavenportandPanteli,2024;Singer,WöhrandOt-
terbach, 2024; Dunlop and Ballantyne, 2021). These strate-
giesleveragetargetedadvertising,personalizedcontent,and
persuasive messaging via digital channels (e.g., social me-
dia,email,in-appnotifications),oftennormalizinggambling
as both accessible and glamorous (Pettorruso et al., 2021;
Baek,2023;Rodgers,2021).Suchaggressivetactics,includ-
ing gamified promotions and immersive content, can dis-
proportionatelyexposeunderageandvulnerableindividuals,
exacerbating public health challenges.
MultimodalAIandfoundationmodels,includinggener-
ative AI and vision-language models (VLMs) (Zhu, Chen,
Shen, Li and Elhoseiny, 2023), offer a powerful means
of transforming these practices. They can synthesize and
analyze text, images, and videos to detect child-directed
language or visuals in ads, allowing regulators to enforce
stricter compliance standards (Campbell, Plangger, Sands
and Kietzmann, 2022; Bjørseth, Simensen, Bjørnethun,
Griffiths, Erevik, Leino and Pallesen, 2021). One promising
applicationinvolvesscrutinizinginfluencercontentonsocial
platforms (Kim, Jiang, Nakada, Han and Wang, 2020), flag-
ging gambling promotions lacking proper disclosure (Pitt
et al., 2024; Warraich, Tazbaz and Califf, 2024). Simi-
larly, tools used for misinformation detection in political
campaigns (Chen and Shu, 2024; Kuznetsova, Makhortykh,
Vziatysheva, Stolze, Baghumyan and Urman, 2025; Kumar
and Taylor, 2024) could be adapted to evaluate the factual
accuracy and ethical framing of gambling advertisements.
Inlinewithbroaderadvertisinginsights(Grewal,Satornino,
Davenport and Guha, 2024; Zhang, Shen, Zhang, Xu, Li,
Yao and Yu, 2021), AI-based audits can also uncover ma-
nipulative or stereotype-reinforcing elements (Shumanov,
Cooper and Ewing, 2022; Liu-Thompkins, Okazaki and Li,
2022),ensuringthatmarketingdoesnotglorifygamblingas
a fast path to financial security.
To illustrate these concepts more concretely, we define
an AI-driven function 𝑓Θ ∶ (, ) →  that assigns
a risk or relevance score𝑟 ∈  to marketing materials
aimed at specific user groups. Let = {𝑚1,… , 𝑚𝑘} be
marketing items (e.g., text, images, videos) and let =
{𝑢1,… , 𝑢𝑛}denoteusersegmentsdefinedbydemographics,
behaviors, and social ties. In practice,𝑓Θ combines VLMs
to process multimodal content (Zhu et al., 2023) and graph
neural networks (GNNs) to account for relational data (Wu,
Pan, Chen, Long, Zhang and Philip, 2020; Bhadra, Khanna
and Beuno, 2023). Once trained on labeled examples (e.g.,
adsdeemedhigh-risk), 𝑓Θ flagsharmfulcontentandrecom-
mendsinterventions(e.g.,restrictingaddistribution,altering
imagery, or providing disclaimers). This pipeline can in-
corporateprivacysafeguards(e.g.,dataanonymization)and
continuous validation (e.g., adherence to ethical marketing
guidelines) to ensure transparency and social responsibility.
As shown in Figure 4, generative AI can annotate suspi-
cious elements ranging from exaggerated reward claims to
youth-targeted graphics, thereby illustrating how𝑓Θ might
assign higher risk scores to unethical or misleading pro-
motions. Another emerging technique features GNNs that
model intricate relationships among users, behaviors, and
content (Bhadra et al., 2023). By mapping how a promotion
spreads through a user’s social network, these models can
forecastcascadingeffectsanddynamicallyadjustcampaigns
to reduce harm. When enhanced with emotion recognition
layers, they can further detect ads that exploit anxiety or
overconfidence, proactively flagging them for immediate
review.
5.3. Personalized Behavioral Interventions
Generative AI heralds a paradigm shift in delivering
personalized behavioral interventions for online gambling,
moving from static approaches to dynamic, adaptive strate-
gies(Baig,Hobson,GholamHosseini,UllahandAfifi,2024;
Yang,Khatibi,Nagesh,Abbasian,Azimi,JainandRahmani,
2024; Geng, Liu, Fu, Ge and Zhang, 2022). Large Lan-
guage Models (LLMs) and other generative methods enable
real-time customization of prompts, nudges, and supportive
messages based on user data such as spending habits, ses-
sion durations, and even emotional tone (Aggarwal, Tam,
Wu, Li and Qiao, 2023; An, Shen, Wang and Yang, 2024;
Nie, Shao, Fan, Shao, You, Preindl and Jiang, 2024). This
mirrors personalized marketing, yet applied to health and
well-being (Lee, Lee, Jeong and Kim, 2024), allowing in-
terventions to be generatedon the flyat critical moments
Konrad Samsel et al.:Preprint submitted to Elsevier Page 9 of 17

Generative AI for Gambling Behavior Health
andpotentiallyhaltingescalationintoproblematicgambling
behaviors. Let={ 𝑑1,… , 𝑑𝑚} represent key data streams
(e.g., betting amounts, session timestamps, chat logs), and
let  = {𝑖1,… , 𝑖𝑘} be a set of intervention strategies (e.g.,
nudges, cooldown reminders, self-reflection prompts). We
define an AI-driven mapping 𝑔Θ ∶  → , where the
generativemodel’sparameters Θarecalibratedusingrealor
synthetic datato ensure diverse scenarios while preserving
privacy. Once trained on historical gambling patterns and
labeled intervention outcomes, 𝑔Θ delivers personalized,
context-aware content in real time, with safeguards like
data anonymization and ethical review boards mitigating
potential misuse.
The personalization deepens when sentiment analysis
and contextual data are integrated, allowing the system to
react differently to frustration, overconfidence, or distress
(Nepal, Pillai, Campbell, Massachi, Heinz, Kunwar, Choi,
Xu,Kuc,Huckinsetal.,2024;Anetal.,2024;Maher,Davis,
Curtis,ShortandMurphy,2020;Subramanian,Yang,Azimi
and Rahmani, 2024). For instance, a user on a losing streak
might receive empathetic messages encouraging a break,
whileawinningusermightseeremindersaboutresponsible
wagering limits. This Generative AI-based adaptability par-
allelsadvancementsinmentalhealthapps,wherecontextual
prompts foster self-reflection (Kirk, Vidgen, Röttger and
Hale,2024;Mooretal.,2023).Onepromisingextensionisto
usedigital 'micro-rewards',which gentlyincentivize players
to follow recommended limits or take breaks, reinforcing
positivebehaviors withoutrelying onintrusive tactics.Over
time, this targeted personalization fosters a supportive envi-
ronment in which users feel guided and motivated to make
healthier gambling choices.
5.4. Gamified Recovery Tools
Generative AI offers powerful new possibilities for de-
veloping interactive, gamified recovery tools tailored for in-
dividualsaddressingproblemgambling(Stade,Stirman,Un-
gar,Boland,Schwartz,Yaden,Sedoc,DeRubeis,Willerand
Eichstaedt, 2024; Obradovich, Khalsa, Khan, Suh, Perlis,
Ajilore and Paulus, 2024). These tools move beyond tra-
ditional approaches by providing engaging, personalized
experiences that tackle the unique challenges of gambling
addiction (Cheng and Ebrahimi, 2023). For example, AI-
generated simulations can mimic real-life gambling scenar-
ios within a safe, controlled digital environment, enabling
userstopracticeimpulsecontrolanddecision-makingskills
under realistic triggers (Sezgin and McKay, 2024). This
strategy parallels the use of serious games in education and
health, where immersive learning environments reinforce
critical competencies.
In addition to simulations, generative AI can develop
gamified exercises that reward positive behaviors linked to
recovery, such as adhering to self-exclusion programs or
attending therapy sessions (Cheng and Ebrahimi, 2023).
These elements boost motivation and adherence, both vital
formaintainingprogress.Moreover,AIcanproducetailored
narratives and videos that highlight others’ recovery sto-
ries, instilling a sense of community, hope, and relatable
success (Sezgin and McKay, 2024; Arenas, Viduani and
Araujo, 2022; Nye, Delgadillo and Barkham, 2023). Let
 = {𝑠1,… , 𝑠𝑛} represent a user’s state (e.g., emotional
cues, triggers, progress metrics), and let={ 𝑚1,… , 𝑚𝑘}
denotegamifiedmodules(e.g.,simulations,rewardsystems,
narrative exercises). We define a generative mappingℎΘ ∶
 → , where the parametersΘ are learned from real or
synthetic data(see Section 5.1) to preserve privacy. Once
trained, ℎΘ personalizes each module in real time, adjusting
difficulty or content based on user feedback (Sezgin and
McKay, 2024; Nye et al., 2023). Incorporating wearable-
sensor data (e.g., heart rate) into  could enhance early
detection of emotional distress, prompting instant delivery
of coping strategies.
Generative AI has already been leveraged in mental
health to create personalized images for emotional manage-
ment (Sezgin and McKay, 2024), and similar logic applies
togamblingrecovery:dynamiccontentandadaptivereward
systems can drive sustained engagement (Li, Zhang, Lee,
KrautandMohr,2023;Obradovichetal.,2024).AIchatbots
can further complement these modules, offering guidance
andreal-timeinterventionsbetweenhumantherapysessions.
The integration of simulations, gamified exercises, and on-
demand support delivers a comprehensive and data-driven
approach to achieving lasting recovery.
5.5. AI-Driven Counselor Training and Decision
Support
The rising complexities of online gambling demand
innovative approaches to counselor training and decision
support,andmultimodalAIcoupledwithfoundationmodels
offersatransformativesolution(Shen,Li,Yang,Ni,Tao,Yu,
Zheng, Xu and Hu, 2024; Li et al., 2023). One particularly
promising use case is the creation of AI-driven training
platforms that simulate realistic counseling scenarios for
diversebehavioralhealthissues(Shenetal.,2024;Steenstra,
Nouraei, Arjmand and Bickmore, 2024). For instance, a
virtual client could present with the intertwined challenges
of financial distress, strained relationships, and comorbid
mentalhealthconditions,incorporatingvoicetone,facialex-
pressions, and text-based interactions to capture the nuance
of real sessions (Stade et al., 2024; Magill, Mastroleo and
Martino, 2022). This mirrors systems in addiction counsel-
ing(e.g.,substanceabuse(Steenstraetal.,2024))andmental
health (e.g., depression or anxiety (Stade et al., 2024)),
wheretraineespracticetechniqueslikeCognitiveBehavioral
Therapy (CBT) or motivational interviewing and receive
instant, targeted feedback.
Beyondtraining,AIprovidesvitalclinicaldecisionsup-
portacrossmultipledomains.Byanalyzinggamblingtrans-
actions, online behaviors, and communication data, clini-
ciansgainaholisticviewofclientpatterns(Shenetal.,2024;
Maslej, Kloiber, Ghassemi, Yu and Hill, 2023). Similar
analyticshavebeenappliedtoeatingdisorders(e.g.,tracking
food logs, mood trends) (Li et al., 2023) and chronic pain
Konrad Samsel et al.:Preprint submitted to Elsevier Page 10 of 17

Generative AI for Gambling Behavior Health
Player Data
Conversation Data
Marketing Data
Inﬂuencer Videos Marketing Images Marketing Videos
In-App Chat logsDigital Conversations
𝒮={s1,…,sm} rΘ:(𝒞,𝒮)→ℱ
s1 s2
s3s4s5
s6s7
ℱ
c1∈𝒞
John, I noticed some changes in your
gambling activity recently, and I see that
you’re feeling frustrated about your
ﬁnances. Can we talk about setting
some limits to help you regain control?
I’ve been trying to stop, but those
ads and bonuses make it so hard.
I feel like I’m losing control.
Let's explore managing these urges.
We can set a deposit limit or practice
techniques to handle betting pressure.
Risk factors identiﬁed: Financial
stress, high deposit frequency.
Feedback and
Recommendation Space
Multimodal Input Space
Foundation Model
Figure 5: Multimodal Foundation Model for Problem Gambling Counseling. This figure illustrates the integration of multimodal
data ( ={ 𝑠1,… , 𝑠𝑚}), including player behaviors, marketing influences, and conversational cues, into a foundation model (𝑟Θ).
The model processes these inputs to generate actionable insights () that guide counselors () in providing tailored interventions.
The counselor (𝑐1 ∈ ) interacts with the model’s recommendations to address specific client concerns, such as identifying risk
factors (e.g., financial stress, high deposit frequency) and proposing strategies like deposit limits or behavioral exercises.
management (e.g., monitoring activity levels, medication
use) (Abedi, Colella, Pakosh and Khan, 2024), all with the
goalofenablinginformed,personalizedinterventions(Stade
et al., 2024). AI-powered conversational agents can also
serve as virtual peer counselors, helping practitioners pro-
cesscomplexcasesormanageemotionalstress(Stadeetal.,
2024; Shen et al., 2024; Xi, Chen, Guo, He, Ding, Hong,
Zhang, Wang, Jin, Zhou et al., 2023). This mirrors trauma
orfamilytherapysettings,wherevirtualpeersofferreal-time
guidanceonhandlingsensitivetopics(Xietal.,2023;Abedi
et al., 2024). Let  = {𝑐1,… , 𝑐𝑝} be counselor trainees
or practicing clinicians, and let = {𝑠1,… , 𝑠𝑚} represent
multimodal simulation elements (e.g., text dialogues, vocal
tones, facial cues, or virtual environments). We define a
generative mapping 𝑟Θ ∶ (, ) → , where  is a feed-
back or recommendation space (e.g., performance metrics,
evidence-based treatment steps). ParametersΘ are learned
from real orsynthetic data that reflect various behavioral
health scenarios. Once trained,𝑟Θ dynamically adapts each
simulationtoindividualcounselorneeds,suggestingtailored
techniques(e.g.,CBTvs.motivationalinterviewing)oreven
highlighting relevant ethical considerations (Figure 5).
Hyper-realistic virtual environments further expand
these capabilities by recreating specific situations such as
onlinecasinos(Magilletal.,2022),helpingcounselorsgrasp
the triggers and temptations their clients face. Comparable
setups apply to social anxiety, where users virtually en-
counter stress-inducing social scenarios. While these tech-
nologies offer substantial promise, it remains essential to
balanceinnovationwithethics(Althoff,ClarkandLeskovec,
2016; Xi et al., 2023), ensuring user safety, fairness, and
respectforprivacy.Augmentingratherthanreplacinghuman
expertise,AI-drivencounselortraininganddecisionsupport
have the potential to transform the quality and accessibility
of behavioral health services.
5.6. Scenario Modeling for Policy Development
Generative AI enables a proactive and data-driven ap-
proach to policy-making by creating detailed scenario mod-
els and simulations (Cao, Zhuang and He, 2024; Barnett,
Kieslich and Diakopoulos, 2024). Rather than merely re-
acting to existing issues, policymakers can explore'what-
if' scenarios in gambling regulation, such as changing ad-
vertising standards, adjusting self-exclusion rules, or al-
tering tax structures, and instantly gauge their effects on
addiction rates, economic outcomes, and social dynamics
(Barnett et al., 2024; Tyler et al., 2023). Similar modeling
appliestobroaderpublicpolicycontextslikeenvironmental
measures or public health, where AI can integrate large
datasets (e.g., demographics, economic indicators) to pro-
vide intuitive visual reports and interactive forecasts. In the
context of this use case, let = {𝑝1,… , 𝑝𝑧} denote a set
of policy options (e.g., advertising limits, tax incentives),
and let = {𝑣1,… , 𝑣𝑚} be relevant variables (e.g., player
behaviors, demographics). We define𝑆Θ ∶ (, ) → ,
where capturesmodeloutcomes(e.g.,projectedaddiction
rates, revenue forecasts). Once𝑆Θ is trained—potentially
Konrad Samsel et al.:Preprint submitted to Elsevier Page 11 of 17

Generative AI for Gambling Behavior Health
leveragingsyntheticdata forprivacyandcoverage(seeSec-
tion5.1)—policymakerscanmanipulate  inrealtime,gen-
erating scenario-driven insights to inform robust, forward-
thinking regulations. One promising extension is bridging
cross-border regulatory differences via a single integrated
model capable of unifying data from diverse jurisdictions.
This ability to produce complex, dynamic simulations
democratizes access to actionable insights, enabling non-
technical stakeholders to engage meaningfully with policy
decisions (Cao et al., 2024). Experimenting with different
policy levers and examining likely outcomes helps gov-
ernments, industry leaders, and advocacy groups anticipate
unintended consequences and refine strategies. AI-driven
scenario modeling turns policy-making into a dynamic and
forward-thinking process, proving safer and more account-
able gambling ecosystems.
6. Ethical and Technical Challenges
While AI technology presents promising opportunities
to reduce online gambling harm, practitioners must contend
witharangeofethicalandtechnicalchallengesindeploying
these systems. First,validationbecomes significantly more
complex when dealing with large, versatile AI models. Un-
like conventional software designed for narrow tasks, these
models can be repurposed in unforeseen ways, complicat-
ing efforts to certify performance across multiple domains
(Mitchell, Wu, Zaldivar, Barnes, Vasserman, Hutchinson,
Spitzer, Raji and Gebru, 2019). For instance, an algorithm
trained primarily for risk detection could be co-opted to
nudge players toward higher spending, necessitating rigor-
ous oversight and continual monitoring.
A related concern isverification. Multimodal models
that combine textual, behavioral, and biometric data can
be daunting for public health practitioners or non-technical
stakeholders to evaluate (Holstein, Wortman Vaughan,
Daumé III, Dudik and Wallach, 2019). For example, an AI-
driven system might flag excessive betting behaviors while
alsoproducingspecializedvisualorstatisticaljustifications.
Verifying the correctness of these outputs, potentially in-
volving large datasets, fluid user contexts, or proprietary
embedding layers, often requires cross-disciplinary reviews
andtailoredexplainabilitytools(Bender,Gebru,McMillan-
Major and Shmitchell, 2021).
Social biases pose an equally urgent problem. Large-
scale models risk perpetuating or amplifying unfair out-
comes, especially for minority groups underrepresented
in training data (Koenecke, Nam, Lake, Nudell, Quartey,
Mengesha, Toups, Rickford, Jurafsky and Goel, 2020). In
thegamblingcontext,thiscouldmanifestasAIinterventions
thatoverlookcertaindemographics,failingtoprovidetimely
harm-reduction measures. Frequent audits of model outputs
andcollaborationwithdomainexpertswhounderstandlocal
cultural nuances are essential to detect and mitigate such
biases.
Privacy remains a pressing issue as well. Foundation
models often rely on massive corpora of user-generated
content, which may inadvertently embed personally identi-
fiabledata(Gupta,Akiri,Aryal,ParkerandPraharaj,2023).
Even anonymized gambling logs can be susceptible to re-
identification attacks, especially if combined with external
data sources. Moreover, 'prompt attacks' or 'jailbreak' ex-
ploits can lure a model into revealing sensitive user infor-
mationdespitesafeguards(Weidinger,Mellor,Rauh,Griffin,
Uesato, Huang, Cheng, Glaese, Balle, Kasirzadeh et al.,
2021). Robust governance measures, including data mini-
mization, encryption, and real-time anomaly detection, are
crucial to protect users in this high-risk environment.
Finally, the scale of modern AI models raises both
environmental and economic concerns. Training and up-
dating large-scale systems can be computationally expen-
sive, resulting in substantial carbon footprints and elevated
operational costs (Patterson, Gonzalez, Hölzle, Le, Liang,
Munguia,Rothchild,So,TexierandDean,2022).Gambling
platforms that rely on frequently updated models must bal-
ance sophistication with sustainability to avoid prohibitive
resource demands.
Inadditiontothesetechnicalhurdles,practitionersmust
also address overarchingethical considerationsrelated to
data collection, transparency, and industry accountability.
For instance, re-identification risks could escalate when
operators link user betting data (e.g., for limit-setting) with
browsinghistoriestodeliverpersonalizedgamblingads.De-
cidingwhichdataaregatheredandhowitisstoredbecomes
central to preventing downstream harms (Price and Cohen,
2019). Likewise, clear communication about how data are
collected, models are developed, and technologies are de-
ployed is vital for fostering user autonomy and commu-
nity trust (Fisher and Rosella, 2022). Strengthening multi-
stakeholdergovernanceboards,includinghealthcareprofes-
sionals, ethicists, and gambling regulators, could help en-
sure that AI interventions complement, rather than replace,
the industry’s duty to address addictive platform features.
Although tools such as limit setting, feedback messaging,
and service referrals are beneficial, these do not necessarily
tackletherootcausesofproblematicbehaviors,highlighting
theneedforcontinuedvigilancearoundplatformdesignand
industry practices.
7. Conclusion
This review highlights the evolving challenges posed by
online gambling and the opportunities that artificial intelli-
gence,particularlymultimodalgenerativeAIandfoundation
models, offers for prevention and harm reduction. These
technologies enable advanced analytics, adaptive interven-
tions, and realistic policy modeling, expanding the possi-
bilities for responsible gambling research and practice. At
the same time, they emphasize the need for safeguarding
data privacy, mitigating algorithmic bias, and maintaining
accountability to protect user well-being.
The examples discussed in this review demonstrate how
AI can enhance our understanding of gambling behaviors,
support the development of personalized harm-reduction
Konrad Samsel et al.:Preprint submitted to Elsevier Page 12 of 17

Generative AI for Gambling Behavior Health
tools, and inform regulatory strategies. Moving forward,
validating these applications across diverse contexts and
addressing their limitations will be crucial. Collaboration
among researchers, clinicians, policymakers, and technolo-
gists is key to ensuring these tools are implemented respon-
sibly and effectively. With careful integration, AI has the
potential to redefine prevention, early detection, and treat-
ment strategies for online gambling, supporting meaningful
progress in addressing gambling-related harms.
References
Abedi, A., Colella, T.J., Pakosh, M., Khan, S.S., 2024. Artificial
intelligence-driven virtual rehabilitation for people living in the com-
munity: A scoping review. NPJ Digital Medicine 7, 25.
Aggarwal, A., Tam, C.C., Wu, D., Li, X., Qiao, S., 2023. Artificial
intelligence–based chatbots for promoting health behavioral changes:
systematic review. Journal of medical Internet research 25, e40789.
Allami, Y., Hodgins, D.C., Young, M., Brunelle, N., Currie, S., Dufour,
M., Flores-Pajot, M.C., Nadeau, L., 2021. A meta-analysis of problem
gambling risk factors in the general adult population. Addiction 116,
2968–2977.
Allami,Y.,Williams,R.J.,Hodgins,D.C.,Stevens,R.,Shaw,C.A.,elGue-
baly, N., Christensen, D.R., McGrath, D.S., Belanger, Y.D., 2003. Pre-
dictors of problem gambling remission in adults: A canadian longitudi-
nal study. Psychology of Addictive Behaviors .
Althoff,T.,Clark,K.,Leskovec,J.,2016.Large-scaleanalysisofcounseling
conversations: An application of natural language processing to mental
health. Transactions of the Association for Computational Linguistics
4, 463–476.
An,R.,Shen,J.,Wang,J.,Yang,Y.,2024. Ascopingreviewofmethodolo-
giesforapplyingartificialintelligencetophysicalactivityinterventions.
Journal of Sport and Health Science 13, 428–441.
Arenas, D.L., Viduani, A., Araujo, R.B., 2022. Therapeutic use of role-
playing game (rpg) in mental health: A scoping review. Simulation &
Gaming 53, 285–311.
Armoon, B., Griffiths, M.D., Fleury, M.J., Mohammadi, R., Bayat, A.H.,
2023. Theglobalprevalenceofproblemandpathologicalgamblingand
itsassociatedfactorsamongindividualswithsubstanceusedisorders:A
meta-analysis. International Journal of Mental Health and Addiction ,
1–34.
Auer, M., Griffiths, M.D., 2022. Predicting limit-setting behavior of
gamblers using machine learning algorithms: A real-world study of
norwegiangamblersusingaccountdata. InternationalJournalofMental
Health and Addiction 20, 771–788.
Auer, M., Griffiths, M.D., 2023a. The impact of personalized feedback in-
terventionsbyagamblingoperatoronsubsequentgamblingexpenditure
in a sample of dutch online gamblers. Journal of Gambling Studies 39,
929–946.
Auer,M.,Griffiths,M.D.,2023b. Usingartificialintelligencealgorithmsto
predict self-reported problem gambling with account-based player data
inanonlinecasinosetting. JournalofGamblingStudies39,1273–1294.
Baek,T.H.,2023. Digitaladvertisingintheageofgenerativeai. Journalof
Current Issues & Research in Advertising 44, 249–251.
Baig, M.M., Hobson, C., GholamHosseini, H., Ullah, E., Afifi, S., 2024.
Generative ai in improving personalized patient care plans: Opportuni-
tiesandbarrierstowardsitswideradoption.AppliedSciences14,10899.
Barakat,C.,Konstantinidis,T.,2023. Areviewoftherelationshipbetween
socioeconomic status change and health. International Journal of
Environmental Research and Public Health 20, 6249.
Barnes, G.M., Welte, J.W., Tidwell, M.C.O., Hoffman, J.H., 2015. Gam-
blingandsubstanceuse:Co-occurrenceamongadultsinarecentgeneral
populationstudyintheunitedstates. InternationalGamblingStudies15,
55–71.
Barnett,J.,Kieslich,K.,Diakopoulos,N.,2024. Simulatingpolicyimpacts:
Developing a generative scenario writing method to evaluate the per-
ceived effects of regulation. arXiv preprint arXiv:2405.09679 .
Bastiani, O., Russell, A.M.T., Newall, P., 2023. Childhood use of coin
pusher and crane grab machines, and adult gambling: Robustness to
subjectiveconfidenceinayoungadultusasample. JournalofGambling
Studies .
Bender, E.M., Gebru, T., McMillan-Major, A., Shmitchell, S., 2021. On
the dangers of stochastic parrots: Can language models be too big?, in:
Proceedings of the 2021 ACM conference on fairness, accountability,
and transparency, pp. 610–623.
Bhadra, J., Khanna, A.S., Beuno, A., 2023. A graph neural network
approach for identification of influencers and micro-influencers in a
socialnetwork:*classifyinginfluencersfromnon-influencersusinggnn
and gcn, in: 2023 International Conference on Advances in Electron-
ics, Communication, Computing and Intelligent Information Systems
(ICAECIS), IEEE. pp. 66–71.
Bjørseth,B.,Simensen,J.O.,Bjørnethun,A.,Griffiths,M.D.,Erevik,E.K.,
Leino, T., Pallesen, S., 2021. The effects of responsible gambling pop-
upmessagesongamblingbehaviorsandcognitions:Asystematicreview
and meta-analysis. Frontiers in Psychiatry 11, 601800.
Booth, N., Dowling, N.A., Landon, J., Lubman, D.I., Merkouris, S.S.,
Rodda, S.N., 2021. Affected others responsivity to gambling harm:
Aninternationaltaxonomyofconsumer-derivedbehaviourchangetech-
niques. Journal of clinical medicine 10, 583.
Calado,F.,Griffiths,M.D.,2016. Problemgamblingworldwide:Anupdate
and systematic review of empirical research (2000–2015). Journal of
Behavioral Addictions 5, 592–613.
Campbell,C.,Plangger,K.,Sands,S.,Kietzmann,J.,2022.Preparingforan
era of deepfakes and ai-generated ads: A framework for understanding
responsestomanipulatedadvertising. JournalofAdvertising51,22–38.
Cao, C., Zhuang, J., He, Q., 2024. Llm-assisted modeling and simulations
for public sector decision-making: Bridging climate data and policy
insights,in:AAAI-2024WorkshoponPublicSectorLLMs:Algorithmic
and Sociotechnical Design.
Chen, C., Shu, K., 2024. Combating misinformation in the age of llms:
Opportunities and challenges. AI Magazine 45, 354–368.
Cheng,C.,Ebrahimi,O.V.,2023. Gamification:anovelapproachtomental
health promotion. Current Psychiatry Reports 25, 577–586.
Claesdotter-Knutsson, E., Håkansson, A., 2021. Changes in self-reported
web-based gambling activity during the covid-19 pandemic: Cross-
sectional study. JMIR Serious Games 9.
Columb, D., O’Gara, C., 2018. A national survey of online gambling
behaviours. Irish Journal of Psychological Medicine 35, 311–319.
Dąbrowska, K., Moskalewicz, J., Wieczorek, Ł., 2017. Barriers in access
to the treatment for people with gambling disorders. are they different
fromthoseexperiencedbypeoplewithalcoholand/ordrugdependence?
Journal of Gambling Studies 33, 487–503.
Darvesh, N., Radhakrishnan, A., Lachance, C.C., Nincic, V., Sharpe, J.P.,
Ghassemi, M., Straus, S.E., Tricco, A.C., 2020. Exploring the preva-
lence of gaming disorder and internet gaming disorder: a rapid scoping
review. Systematic reviews 9, 1–10.
Delfabbro,P.,King,D.L.,Carey,P.,2021. Harmseverityininternetgaming
disorder and problem gambling: A comparative study. Computers in
Human Behavior 124, 106898.
Deng, X., Lesch, T., Clark, L., 2019. Applying data science to behavioral
analysis of online gambling. Current Addiction Reports 6, 159–164.
Dowling, N., Smith, D., Thomas, T., 2005. Electronic gaming machines:
are they the ‘crack-cocaine’of gambling? Addiction 100, 33–45.
Drosatos, G., Nalbadis, F., Arden-Close, E., Baines, V., Bolat, E., Vuillier,
L., Kostoulas, T., Wasowska, S., Bonello, M., Palles, J., et al., 2018.
Empowering responsible online gambling by real-time persuasive in-
formation systems, in: 2018 12th International Conference on Research
Challenges in Information Science (RCIS), IEEE. pp. 1–11.
Dunlop, P., Ballantyne, E.E.F., 2021. Effective and responsible marketing
of online sports gambling to young adults in the uk. SN Business &
Economics 1.
D’Alfonso, S., 2020. Ai in mental health. Current opinion in psychology
36, 112–117.
Konrad Samsel et al.:Preprint submitted to Elsevier Page 13 of 17

Generative AI for Gambling Behavior Health
Elton-Marshall, T., Leatherdale, S.T., Turner, N.E., 2016. An examination
of internet and land-based gambling among adolescents in three cana-
dian provinces: Results from the youth gambling survey (ygs). BMC
public health 16, 1–10.
Emond,A.M.,Griffiths,M.D.,2020. Gamblinginchildrenandadolescents.
British Medical Bulletin 136, 21–29.
Engebø, J., Torsheim, T., Pallesen, S., 2021. Regulatory measures’ effect
on gambling participation: Experiences from norway. Frontiers in
Psychiatry 12, 672471.
Favieri,F.,Forte,G.,Casagrande,M.,Dalpiaz,C.,Riglioni,A.,Langher,V.,
2023. A portraitof gamblingbehaviors andassociated cognitivebeliefs
amongyoungadolescentsinitaly.InternationalJournalofMentalHealth
and Addiction .
Finkenwirth, S., MacDonald, K., Deng, X., Lesch, T., Clark, L., 2021.
Using machine learning to predict self-exclusion status in online gam-
blers on the playnow. com platform in british columbia. International
Gambling Studies 21, 220–237.
Fisher, S., Rosella, L.C., 2022. Priorities for successful use of artificial
intelligence by public health organizations: a literature review. BMC
Public Health 22, 2146.
Gainsbury, S.M., 2015. Online gambling addiction: the relationship be-
tween internet gambling and disordered gambling. Current addiction
reports 2, 185–193.
Gambling Commission, 2021. Gambling commission publishes latest
combined health survey.
Geng, S., Liu, S., Fu, Z., Ge, Y., Zhang, Y., 2022. Recommendation as
language processing (rlp): A unified pretrain, personalized prompt &
predict paradigm (p5), in: Proceedings of the 16th ACM Conference on
Recommender Systems, pp. 299–315.
Ghaharian, K., Abarbanel, B., Phung, D., Puranik, P., Kraus, S., Feldman,
A., Bernhard, B., 2023. Applications of data science for responsible
gambling: A scoping review. International Gambling Studies 23, 289–
312.
Ghaharian, K., Binesh, F., Soligo, M., Golab, L., Abarbanel, B., 2024. Ai
ethics in a controversial industry: the case of gambling and its ethical
paradox. AI and Ethics , 1–17.
Ghelfi,M.,Scattola,P.,Giudici,G.,Velasco,V.,2023. Onlinegambling:A
systematic review of risk and protective factors in the adult population.
Journal of Gambling Studies .
Giuffrè, M., Shung, D.L., 2023. Harnessing the power of synthetic data in
healthcare:innovation,application,andprivacy. NPJdigitalmedicine6,
186.
Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D.,
Ozair, S., Courville, A., Bengio, Y., 2014. Generative adversarial nets.
Advances in neural information processing systems 27.
Gooding, N.B., 2023. What’s the harm? predicting the risk of future
gambling problems.
Gooding, N.B., H., K., Williams, R.J., Williams, J.N., 2023. Individual
differences and predictors of general awareness in problem gambling.
Addictive Behaviors 136.
Grewal,D.,Satornino,C.B.,Davenport,T.,Guha,A.,2024.Howgenerative
ai is shaping the future of marketing. Journal of the Academy of
Marketing Science , 1–21.
Griffiths,M.,Wardle,H.,Orford,J.,Sproston,K.,Erens,B.,2021. Internet
gambling, health, smoking and alcohol use: Findings from the 2007
british gambling prevalence survey. International Journal of Mental
Health and Addiction 9, 1–11.
Guillou-Landreat, M., Gallopel-Morvan, K., Lever, D., Le Goff, D.,
Le Reste, J.Y., 2021. Gambling marketing strategies and the internet:
What do we know? a systematic review. Frontiers in Psychiatry 12,
583817.
Gupta,M.,Akiri,C.,Aryal,K.,Parker,E.,Praharaj,L.,2023. Fromchatgpt
to threatgpt: Impact of generative ai in cybersecurity and privacy. IEEE
Access .
Habicht, J., Viswanathan, S., Carrington, B., Hauser, T.U., Harper, R.,
Rollwage, M., 2024. Closing the accessibility gap to mental health
treatment with a personalized self-referral chatbot. Nature Medicine ,
1–8.
Harris, A., Gous, G., de Wet, B., Griffiths, M.D., 2021. The relationship
between gambling event frequency, motor response inhibition, arousal,
and dissociative experience. Journal of Gambling Studies 37, 241–268.
Harris, A., Parke, A., Griffiths, M.D., 2018. The case for using personally
relevant and emotionally stimulating gambling messages as a gambling
harm-minimisationstrategy. InternationalJournalofMentalHealthand
Addiction 16, 266–275.
Hilbrecht, M., Baxter, D., Abbott, M., Binde, P., Clark, L., Hodgins, D.C.,
Manitowabi, D., Quilty, L., SpÅngberg, J., Volberg, R., Walker, D.,
Williams, R.J., 2020. The conceptual framework of harmful gambling:
A revised framework for understanding gambling harm. Journal of
Behavioral Addictions 9, 190–205.
Hing, N., Russell, A.M., Browne, M., 2017. Risk factors for gambling
problemsononlineelectronicgamingmachines,racebettingandsports
betting. Frontiers in Psychology 8, 262938.
Holstein, K., Wortman Vaughan, J., Daumé III, H., Dudik, M., Wallach,
H., 2019. Improving fairness in machine learning systems: What do
industrypractitionersneed?,in:Proceedingsofthe2019CHIconference
on human factors in computing systems, pp. 1–16.
Hopfgartner, N., Auer, M., Helic, D., Griffiths, M.D., 2024. Using artifi-
cial intelligence algorithms to predict self-reported problem gambling
among online casino gamblers from different countries using account-
basedplayerdata. InternationalJournalofMentalHealthandAddiction
, 1–23.
Hubert, P., Griffiths, M.D., 2018. A comparison of online versus offline
gambling harm in portuguese pathological gamblers: An empirical
study. International journal of mental health and addiction 16, 1219–
1237.
Jach, T., Probierz, B., Kozak, J., Stefański, P., Dziczkowski, G., Hrabia,
A., Juszczuk, P., Głowania, S., Wołek, G., Sznapka, W., et al., 2024.
Identification of users in a gambling problem with the use of machine
learning, in: Asian Conference on Intelligent Information and Database
Systems, Springer. pp. 263–274.
Jauregui, P., Estévez, A., Urbiola, I., 2016. Pathological gambling and
associated drug and alcohol abuse, emotion regulation, and anxious-
depressive symptomatology. Journal of behavioral addictions 5, 251–
260.
Kairouz, S., Costes, J.M., Murch, W.S., Doray-Demers, P., Carrier, C.,
Eroukmanoff, V., 2023. Enabling new strategies to prevent problematic
online gambling: A machine learning approach for identifying at-risk
onlinegamblersinfrance. InternationalGamblingStudies23,471–490.
Karlsson, J., Broman, N., Håkansson, A., 2019. Associations between
problematicgambling,gaming,andinternetuse:Across-sectionalpop-
ulation survey. Journal of Addiction 2019, 1464858. URL: https:
//doi.org/10.1155/2019/1464858, doi:10.1155/2019/1464858.
Kim, C., Park, J.H., Lee, J.Y., 2024. Ai-based betting anomaly detection
system to ensure fairness in sports and prevent illegal gambling. Scien-
tific Reports 14, 6470.
Kim,S.,Jiang,J.Y.,Nakada,M.,Han,J.,Wang,W.,2020. Multimodalpost
attentiveprofilingforinfluencermarketing,in:ProceedingsofTheWeb
Conference 2020, pp. 2878–2884.
Kirk, H.R., Vidgen, B., Röttger, P., Hale, S.A., 2024. The benefits, risks
and bounds of personalizing the alignment of large language models to
individuals. Nature Machine Intelligence , 1–10.
Kisling, L.A., Das, J.M., 2023. Prevention strategies, in: StatPearls [inter-
net]. StatPearls Publishing.
Koenecke, A., Nam, A., Lake, E., Nudell, J., Quartey, M., Mengesha, Z.,
Toups,C.,Rickford,J.R.,Jurafsky,D.,Goel,S.,2020. Racialdisparities
in automated speech recognition. Proceedings of the national academy
of sciences 117, 7684–7689.
Kshetri, N., Dwivedi, Y.K., Davenport, T.H., Panteli, N., 2024. Generative
artificial intelligence in marketing: Applications, opportunities, chal-
lenges, and research agenda.
Kumar,A.,Taylor,J.W.,2024. Featureimportanceintheageofexplainable
ai: Case study of detecting fake news & misinformation via a multi-
modalframework. EuropeanJournalofOperationalResearch317,401–
413.
Konrad Samsel et al.:Preprint submitted to Elsevier Page 14 of 17

Generative AI for Gambling Behavior Health
Kuznetsova,E.,Makhortykh,M.,Vziatysheva,V.,Stolze,M.,Baghumyan,
A., Urman, A., 2025. In generative ai we trust: can chatbots effectively
verify political information? Journal of Computational Social Science
8, 15.
Langham, E., Thorne, H., Browne, M., Donaldson, P., Rose, J., Rockloff,
M.,2016. Understandinggamblingrelatedharm:aproposeddefinition,
conceptualframework,andtaxonomyofharms. BMCPublicHealth16.
Lasserre, A.M., Imtiaz, S., Roerecke, M., Heilig, M., Probst, C., Rehm, J.,
2022. Socioeconomic status, alcohol use disorders, and depression: A
population-based study. Journal of affective disorders 301, 331–336.
Latvala,T.,Lintonen,T.,Konu,A.,2019.Publichealtheffectsofgambling–
debate on a conceptual model. BMC public health 19, 1–16.
Lee, G.H., Lee, K.J., Jeong, B., Kim, T.K., 2024. Developing personalized
marketing service using generative ai. IEEE Access .
Li,H.,Zhang,R.,Lee,Y.C.,Kraut,R.E.,Mohr,D.C.,2023. Systematicre-
view and meta-analysis of ai-based conversational agents for promoting
mental health and well-being. NPJ Digital Medicine 6, 236.
Lim, S., Schmälzle, R., 2023. Artificial intelligence for health message
generation: an empirical study using a large language model (llm) and
prompt engineering. Frontiers in Communication 8, 1129082.
Liu-Thompkins, Y., Okazaki, S., Li, H., 2022. Artificial empathy in
marketinginteractions:Bridgingthehuman-aigapinaffectiveandsocial
customerexperience. JournaloftheAcademyofMarketingScience50,
1198–1218.
Lupo, R., Vitale, E., Carriero, M.C., Calabrò, A., Imperiale, C., Ercolani,
M., Filippini, A., Santoro, P., Carvello, M., Rizzo, E., et al., 2023.
Gambling and internet addiction: a pilot study among a population of
italianhealthcare:Gamblingandinternetadditioninahealthcaregroup.
Journal of Gambling Studies 39, 1337–1354.
Magill,M.,Mastroleo,N.R.,Martino,S.,2022. Technology-basedmethods
for training counseling skills in behavioral health: A scoping review.
Journal of technology in behavioral science 7, 325–336.
Maher, C.A., Davis, C.R., Curtis, R.G., Short, C.E., Murphy, K.J., 2020.
A physical activity and diet program delivered by artificially intelligent
virtualhealthcoach:proof-of-conceptstudy.JMIRmHealthanduHealth
8, e17558.
Marionneau,V.,Ruohio,H.,Karlsson,N.,2023.Gamblingharmprevention
and harm reduction in online environments: a call for action. Harm
Reduction Journal 20.
MarketResearchReport,2023.Globalonlinegamblingmarketreport2023-
2028. Accessed from Market Research Report.
Maslej, M.M., Kloiber, S., Ghassemi, M., Yu, J., Hill, S.L., 2023. Out
withai,inwiththepsychiatrist:apreferenceforhuman-derivedclinical
decision support in depression care. Translational Psychiatry 13, 210.
McAuliffe, W.H., Edson, T.C., Louderback, E.R., LaRaja, A., LaPlante,
D.A.,2021. Responsibleproductdesigntomitigateexcessivegambling:
A scoping review and z-curve analysis of replicability. Plos one 16,
e0249926.
Miles, M., Rothschild, J., Åkesson, G., A., H., 2023. Nationwide, mul-
tioperator self-exclusion and psychiatric comorbidity in patients with
gambling disorder: A retrospective chart review study from a regional
treatment unit. Journal of Addiction 2023.
Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson,
B., Spitzer, E., Raji, I.D., Gebru, T., 2019. Model cards for model
reporting, in: Proceedings of the conference on fairness, accountability,
and transparency, pp. 220–229.
Monreal-Bartolomé, A., Barceló-Soler, A., García-Campayo, J.,
Bartolomé-Moreno, C., Cortés-Montávez, P., Acon, E., Huertes,
M., Lacasa, V., Crespo, S., Lloret-Irles, D., et al., 2023. Preventive
gambling programs for adolescents and young adults: A systematic
review. International Journal of Environmental Research and Public
Health 20, 4691.
Moor, M., Banerjee, O., Abad, Z.S.H., Krumholz, H.M., Leskovec, J.,
Topol, E.J., Rajpurkar, P., 2023. Foundation models for generalist
medical artificial intelligence. Nature 616, 259–265.
Murch, W.S., Kairouz, S., Dauphinais, S., Picard, E., Costes, J.M., French,
M., 2023. Using machine learning to retrospectively predict self-
reported gambling problems in quebec. Addiction 118, 1569–1578.
Murch, W.S., Kairouz, S., French, M., 2024a. Comparing ‘fair’machine
learning models for detecting at-risk online gamblers. International
Gambling Studies , 1–23.
Murch, W.S., Kairouz, S., French, M., 2024b. Establishing the temporal
stabilityofmachinelearningmodelsthatdetectonlinegambling-related
harms. Computers in Human Behavior Reports 14, 100427.
National Gambling Association, 2022. Gambling trends among young
adults in 2022.
Nepal, S., Pillai, A., Campbell, W., Massachi, T., Heinz, M.V., Kunwar,
A., Choi, E.S., Xu, X., Kuc, J., Huckins, J.F., et al., 2024. Mindscape
study: Integrating llm and behavioral sensing for personalized ai-driven
journalingexperiences. ProceedingsoftheACMoninteractive,mobile,
wearable and ubiquitous technologies 8, 1–44.
Nie, J., Shao, H., Fan, Y., Shao, Q., You, H., Preindl, M., Jiang, X., 2024.
Llm-based conversational ai therapist for daily functioning screening
and psychotherapeutic intervention via everyday smart devices. arXiv
preprint arXiv:2403.10779 .
Nixon, G., 2022. Ontario’s gaming regulator to ban athletes, celebri-
ties from online gambling ads. https://www.cbc.ca/news/business/
ontario-online-gaming-advertising-changes-1.6952738 . Accessed:
2023-06-17.
Nye, A., Delgadillo, J., Barkham, M., 2023. Efficacy of personalized
psychological interventions: A systematic review and meta-analysis.
Journal of Consulting and Clinical Psychology 91, 389.
Obradovich,N.,Khalsa,S.S.,Khan,W.U.,Suh,J.,Perlis,R.H.,Ajilore,O.,
Paulus,M.P.,2024. Opportunitiesandrisksoflargelanguagemodelsin
psychiatry. NPP—Digital Psychiatry and Neuroscience 2, 8.
Olason, D.T., Hayer, T., Meyer, G., Brosowski, T., 2017. Economic
recession affects gambling participation but not problematic gambling:
Results from a population-based follow-up study. Frontiers in Psychol-
ogy 8, 274777.
Olawade,D.B.,Wada,O.J.,David-Olawade,A.C.,Kunonga,E.,Abaire,O.,
Ling, J., 2023. Using artificial intelligence to improve public health: a
narrative review. Frontiers in Public Health 11, 1196397.
Park, J.S., O’Brien, S., Cai, C.J., Morris, M., Liang, P., Bernstein, M.,
2023. Generative agents: Interactive simulacra of human behavior.
Proceedings of the ACM on Human-Computer Interaction 7, 1–36.
Park, P.S., Goldstein, S., O’Gara, A., Chen, M., Hendrycks, D., 2024. Ai
deception:Asurveyofexamples,risks,andpotentialsolutions. Patterns
5.
Patterson, D., Gonzalez, J., Hölzle, U., Le, Q., Liang, C., Munguia, L.M.,
Rothchild,D.,So,D.R.,Texier,M.,Dean,J.,2022. Thecarbonfootprint
of machine learning training will plateau, then shrink. Computer 55,
18–28.
Percy,C.,França,M.,Dragičević,S.,d’AvilaGarcez,A.,2016a. Predicting
online gambling self-exclusion: An analysis of the performance of
supervised machine learning models. International Gambling Studies
16, 193–210.
Percy,C.,d’AvilaGarcez,A.S.,Dragičević,S.,França,M.V.,Slabaugh,G.,
Weyde, T., 2016b. The need for knowledge extraction: Understanding
harmful gambling behavior with neural networks, in: ECAI 2016. IOS
Press, pp. 974–981.
Percy, C., Garcez, A.S.d., Dragicevic, S., Sarkar, S., 2020. Lessons
learned from problem gambling classification: Indirect discrimination
and algorithmic fairness., in: AI4SG@ AAAI Fall Symposium.
Peres, F., Fallacara, E., Manzoni, L., Castelli, M., Popovič, A., Rodrigues,
M., Estevens, P., 2021. Time series clustering of online gambling
activities for addicted users’ detection. Applied Sciences 11, 2397.
Perrot, B., Hardouin, J.B., Thiabaud, E., Saillard, A., Grall-Bronnec, M.,
Challet-Bouju, G., 2022. Development and validation of a prediction
model for online gambling problems based on players’ account data.
Journal of Behavioral Addictions 11, 874–889.
Petry, N.M., Zajac, K., Ginley, M., Lemmens, J., Rumpf, H.J., Ko, C.H.,
Rehbein, F., 2018. Policy and prevention efforts for gaming should
consider a broad perspective: Commentary on: Policy responses to
problematic video game use: A systematic review of current measures
and future possibilities (király et al., 2018). Journal of Behavioral
Addictions 7, 543–547.
Konrad Samsel et al.:Preprint submitted to Elsevier Page 15 of 17

Generative AI for Gambling Behavior Health
Pettorruso, M., Testa, G., Granero, R., Martinotti, G., d’Andrea, G., di Gi-
annantonio,M.,Fernández-Aranda,F.,Mena-Moreno,T.,Gómez-Peña,
M., Moragas, L., et al., 2021. The transition time to gambling disorder:
The roles that age, gambling preference and personality traits play.
Addictive Behaviors 116, 106813.
Pitt,H.,McCarthy,S.,Randle,M.,Daube,M.,Thomas,S.L.,2024. Young
people’s views about the use of celebrities and social media influencers
in gambling marketing. Health Promotion International 39, daae012.
Potenza, M.N., Sofuoglu, M., Carroll, K.M., Rounsaville, B.J., 2011. Neu-
roscience of behavioral and pharmacological treatments for addictions.
Neuron 69, 695–712.
Price, W.N., Cohen, I.G., 2019. Privacy in the age of medical big data.
Nature medicine 25, 37–43.
Raneri, P.C., Montag, C., Rozgonjuk, D., Satel, J., Pontes, H.M., 2022.
The role of microtransactions in internet gaming disorder and gambling
disorder:apreregisteredsystematicreview.AddictiveBehaviorsReports
15, 100415.
Reith, G., Wardle, H., 2022. The framing of gambling and the commercial
determinantsofharm:Challengesforregulationintheuk,in:Theglobal
gamblingindustry:Structures,tactics,andnetworksofimpact.Springer,
pp. 71–86.
Rizzo, A., La Rosa, V.L., Commodari, E., Alparone, D., Crescenzo, P.,
Yıldırım, M., Chirico, F., 2023. Wanna bet? investigating the factors
related to adolescent and young adult gambling. European Journal of
Investigation in Health, Psychology and Education 13, 2202–2213.
Rodda, S.N., 2022. A systematic review of internet delivered interventions
forgambling:Prevention,harmreductionandearlyintervention.Journal
of Gambling Studies 38, 967–991.
Rodgers, S., 2021. Themed issue introduction: Promises and perils of
artificial intelligence and advertising.
Russell,A.M.T.,Browne,M.,Hing,N.,Rockloff,M.,Newall,P.,Dowling,
N.A., Merkouris, S., King, D.L., Stevens, M., Salonen, A.H., Breen,
H., Greer, N., Thorne, H.B., Visintin, T., Rawat, V., Woo, L., 2023.
Electronic gaming machine accessibility and gambling problems: A
natural policy experiment. Journal of Behavioral Addictions 12, 721–
732.
Sahota, N., 2024. The game changer: How ai is transforming the world of
sports gambling. Forbes URL:https://tinyurl.com/2s3b479s.
Sándor, M.C., Bakó, B., 2024. Unmasking risky habits: Identifying
and predicting problem gamblers through machine learning techniques.
Journal of Gambling Studies , 1–11.
Scholes-Balog, K.E., Hemphill, S.A., 2012. Relationships between online
gambling,mentalhealth,andsubstanceuse:areview. Cyberpsychology,
Behavior, and Social Networking 15, 688–692.
Sezgin, E., McKay, I., 2024. Behavioral health and generative ai: a
perspective on future of therapies and patient care. npj Mental Health
Research 3, 25.
Shanahan, M., McDonell, K., Reynolds, L., 2023. Role play with large
language models. Nature 623, 493–498.
Shao, R., Read, J., Behrens, T., Rogers, R., 2013. Shifts in reinforcement
signallingwhileplayingslot-machinesasafunctionofpriorexperience
and impulsivity. Translational psychiatry 3, e213–e213.
Sharman, S., Murphy, R., Turner, J., Roberts, A., 2019. Psychosocial
correlates in treatment seeking gamblers: Differences in early age onset
gamblers vs later age onset gamblers. Addictive Behaviors 97, 20–26.
Shen, H., Li, Z., Yang, M., Ni, M., Tao, Y., Yu, Z., Zheng, W., Xu, C.,
Hu, B., 2024. Are large language models possible to conduct cognitive
behavioral therapy? arXiv preprint arXiv:2407.17730 .
Shumanov,M.,Cooper,H.,Ewing,M.,2022.Usingaipredictedpersonality
toenhanceadvertisingeffectiveness. EuropeanJournalofMarketing56,
1590–1609.
Singer, J., Wöhr, A., Otterbach, S., 2024. Gambling operators’ use of
advertising strategies on social media and their effects: A systematic
review. Current Addiction Reports , 1–10.
Smith, E., Peters, J., Reiter, N., 2024. Automatic detection of problem-
gambling signs from online texts using large language models. PLOS
Digital Health 3, e0000605.
Smith, J., Doe, J., 2022. The economic cost of gambling problems in the
united states. Journal of Gambling Studies 38, 123–145.
Stade, E.C., Stirman, S.W., Ungar, L.H., Boland, C.L., Schwartz, H.A.,
Yaden,D.B.,Sedoc,J.,DeRubeis,R.J.,Willer,R.,Eichstaedt,J.C.,2024.
Largelanguagemodelscouldchangethefutureofbehavioralhealthcare:
a proposal for responsible development and evaluation. NPJ Mental
Health Research 3, 12.
Steenstra, I., Nouraei, F., Arjmand, M., Bickmore, T., 2024. Virtual
agents for alcohol use counseling: Exploring llm-powered motivational
interviewing, in: Proceedings of the ACM International Conference on
Intelligent Virtual Agents, pp. 1–10.
Subramanian, A., Yang, Z., Azimi, I., Rahmani, A.M., 2024. Graph-
augmented llms for personalized health insights: A case study in sleep
analysis, in: 2024 IEEE 20th International Conference on Body Sensor
Networks (BSN), IEEE. pp. 1–4.
Sumers, T.R., Yao, S., Narasimhan, K., Griffiths, T.L., 2023. Cognitive
architectures for language agents. arXiv preprint arXiv:2309.02427 .
Suurvali, H., Hodgins, D., Toneatto, T., Cunningham, J., 2008. Treatment
seeking among ontario problem gamblers: Results of a population sur-
vey. Psychiatric services 59, 1343–1346.
Tulloch, C., Hing, N., Browne, M., Rockloff, M., Hilbrecht, M., 2021. The
effect of gambling problems on the subjective wellbeing of gamblers’
family and friends: Evidence from large-scale population research in
australia and canada. Journal of behavioral addictions 10, 941–952.
Turner,N.E.,Elton-Marshall,T.,Shi,J.,Wiebe,J.,Boak,A.,vanderMaas,
M.,Mann,R.E.,2018.Crossvalidationofthegamblingproblemseverity
subscale of the canadian adolescent gambling index (cagi/gpss) on a
sample of ontario high school students. Journal of Gambling Studies
34, 521–537.
Turner, N.E., Sinclair, L., Matheson, F.I., 2023. Brief report: The rise of
online betting in ontario. Journal of Gambling Studies , 1–11.
Tyler, C., Akerlof, K., Allegra, A., Arnold, Z., Canino, H., Doornenbal,
M.A., Goldstein, J.A., Budtz Pedersen, D., Sutherland, W.J., 2023. Ai
tools as science policy advisers? the potential and the pitfalls. Nature
622, 27–30.
Vestergaard,S.V.,Ulrichsen,S.P.,Dahl,C.M.,Marcussen,T.,Christiansen,
C.F., 2023. Comorbidity, criminality, and costs of patients treated for
gambling disorder in denmark. Journal of Gambling Studies 39, 1765–
1780. doi:10.1007/s10899-023-10255-6.
Wang, Y., Yang, Z., Xin, Z., 2023a. Characteristics of chinese lottery
consumers’ financial literacy and its relationship with problem lottery
gambling. Journal of Gambling Studies .
Wang, Z.M., Peng, Z., Que, H., Liu, J., Zhou, W., Wu, Y., Guo, H., Gan,
R., Ni, Z., Yang, J., et al., 2023b. Rolellm: Benchmarking, eliciting,
and enhancing role-playing abilities of large language models. arXiv
preprint arXiv:2310.00746 .
Warraich, H.J., Tazbaz, T., Califf, R.M., 2024. Fda perspective on the
regulation of artificial intelligence in health care and biomedicine.
JAMA .
Weidinger, L., Mellor, J., Rauh, M., Griffin, C., Uesato, J., Huang, P.S.,
Cheng, M., Glaese, M., Balle, B., Kasirzadeh, A., et al., 2021. Eth-
ical and social risks of harm from language models. arXiv preprint
arXiv:2112.04359 .
Williams, R.J., Leonard, C.A., Belanger, Y.D., Christensen, D.R., El-
Guebaly, N., Hodgins, D.C., McGrath, D.S., Nicoll, F., Smith, G.J.,
Stevens, R.M., 2021. Predictors of gambling and problem gambling in
canada. Canadian journal of public health 112, 521–529.
Williams, R.J., Shaw, C.A., Belanger, Y.D., Christensen, D.R., el Guebaly,
N., Hodgins, D.C., McGrath, D.S., Stevens, R.M.G., 2023. Etiology of
problem gambling in canada. Psychology of Addictive Behaviors 37,
483–498.
World Health Organization, 2016. Icd-10 version. URL:https://icd.who.
int/browse10/2016/en#/F63.0. published 2016. [Google Scholar].
WorldHealthOrganization,2019. Gamblingandpublichealth:Whoglobal
report. World Health Organization.
Wu,Y.,Sescousse,G.,Yu,H.,Clark,L.,Li,H.,2018. Cognitivedistortions
and gambling near-misses in internet gaming disorder: A preliminary
study. PLoS One 13, e0191110. URL: https://doi.org/10.1371/
Konrad Samsel et al.:Preprint submitted to Elsevier Page 16 of 17

Generative AI for Gambling Behavior Health
journal.pone.0191110, doi:10.1371/journal.pone.0191110.
Wu, Z., Pan, S., Chen, F., Long, G., Zhang, C., Philip, S.Y., 2020. A
comprehensive survey on graph neural networks. IEEE transactions on
neural networks and learning systems 32, 4–24.
Xi, Z., Chen, W., Guo, X., He, W., Ding, Y., Hong, B., Zhang, M., Wang,
J.,Jin,S.,Zhou,E.,etal.,2023. Theriseandpotentialoflargelanguage
model based agents: A survey. arXiv preprint arXiv:2309.07864 .
Yang, L., Zhang, Z., Song, Y., Hong, S., Xu, R., Zhao, Y., Zhang, W., Cui,
B., Yang, M.H., 2023. Diffusion models: A comprehensive survey of
methods and applications. ACM Computing Surveys 56, 1–39.
Yang, Z., Khatibi, E., Nagesh, N., Abbasian, M., Azimi, I., Jain, R.,
Rahmani, A.M., 2024. Chatdiet: Empowering personalized nutrition-
oriented food recommender chatbots through an llm-augmented frame-
work. Smart Health 32, 100465.
Yau, Y.H., Potenza, M.N., 2015. Gambling disorder and other behavioral
addictions:recognitionandtreatment. HarvardReviewofPsychiatry23,
134–146.
Zhang, L., Shen, J., Zhang, J., Xu, J., Li, Z., Yao, Y., Yu, L., 2021.
Multimodal marketing intent analysis for effective targeted advertising.
IEEE Transactions on Multimedia 24, 1830–1843.
Zhu, D., Chen, J., Shen, X., Li, X., Elhoseiny, M., 2023. Minigpt-4:
Enhancingvision-languageunderstandingwithadvancedlargelanguage
models. arXiv preprint arXiv:2304.10592 .
Zuo, X., Jiang, A.A., Zhou, K., 2024. Reinforcement prompting for
financial synthetic data generation. The Journal of Finance and Data
Science 10, 100137.
Konrad Samsel et al.:Preprint submitted to Elsevier Page 17 of 17
